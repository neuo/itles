// 数据层的全部机械规则：读档、判定、闸门、规则池重放、到期挑选、校验。
// 网页（server.js）和命令行（cli.js）共用这一份，免得两边算出两个数。

const fs = require('node:fs');
const path = require('node:path');
const { toEspeak, syllableCount, stressIndex } = require('./ipa.js');

const PARTS = ['recheck', 'practice'];
const PART_LABEL = { recheck: '复检', practice: '练习' };
const LADDER = [1, 2, 4, 8];
const RECHECK_CAP = 4; // 一次最多复检几条规则
const pad = (n) => String(n).padStart(3, '0');

function createStore(root) {
  const data = path.join(root, 'data');
  const rulesFile = path.join(root, 'rules.md');
  const readJson = (p, def) => (fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, 'utf8')) : def);
  const sessionFile = (n) => path.join(data, 'sessions', pad(n) + '.json');
  const answersFile = (n) => path.join(data, 'answers', pad(n) + '.json');
  const poolFile = path.join(data, 'pool.json');

  function sessionNumbers() {
    const dir = path.join(data, 'sessions');
    if (!fs.existsSync(dir)) return [];
    return fs.readdirSync(dir).filter((f) => /^\d{3}\.json$/.test(f)).sort().map((f) => Number(f.slice(0, 3)));
  }
  function loadSession(n) {
    const s = readJson(sessionFile(n), null);
    if (!s) return null;
    const a = readJson(answersFile(n), {});
    return { ...s, items: s.items || [], answers: a.answers || {}, submitted: a.submitted || {} };
  }
  function saveAnswers(n, answers, submitted) {
    fs.mkdirSync(path.join(data, 'answers'), { recursive: true });
    const file = answersFile(n);
    const tmp = file + '.tmp';
    // 保留文件里其他字段（如教练记下的对话原话 chatRaw）
    fs.writeFileSync(tmp, JSON.stringify({ ...readJson(file, {}), n, answers, submitted }, null, 2) + '\n');
    fs.renameSync(tmp, file);
  }
  const rulesText = () => (fs.existsSync(rulesFile) ? fs.readFileSync(rulesFile, 'utf8') : '');
  // 正文里的规则标题：### S1 · 标题（第 N 次讲）
  function ruleTitles() {
    const out = {};
    for (const m of rulesText().matchAll(/^### ([SP]\d+) · (.+?)(?:（[^）]*）)?\s*$/gm)) out[m[1]] = m[2];
    return out;
  }
  // 课表（「## 正文」之前的表格行）：按出现顺序给出每条规则和它的「讲于」格
  function syllabus() {
    const head = rulesText().split(/^## 正文\s*$/m)[0];
    const out = [];
    for (const line of head.split('\n')) {
      const m = line.match(/^\|\s*([SP]\d+)\s*\|/);
      if (!m) continue;
      const cells = line.replace(/^\||\|\s*$/g, '').split('|').map((c) => c.trim());
      out.push({ id: m[1], text: (cells[1] || '').replace(/\*\*/g, ''), taught: cells[cells.length - 1] });
    }
    return out;
  }
  // 规则正文和基线卷里出现过的英文词：她见过读法，不能再拿来当题
  function reservedWords() {
    const files = [rulesFile, ...fs.readdirSync(root).filter((f) => /^baseline.*\.md$/.test(f)).map((f) => path.join(root, f))];
    const out = new Map();
    for (const f of files) {
      if (!fs.existsSync(f)) continue;
      for (const m of fs.readFileSync(f, 'utf8').replace(/\*/g, '').matchAll(/[A-Za-z]{4,}/g)) {
        if (!out.has(m[0].toLowerCase())) out.set(m[0].toLowerCase(), path.basename(f));
      }
    }
    return out;
  }
  const readPool = () => readJson(poolFile, null);
  const writePool = (pool) => fs.writeFileSync(poolFile, JSON.stringify(pool, null, 2) + '\n');

  return { root, data, rulesFile, poolFile, sessionNumbers, loadSession, saveAnswers, rulesText, ruleTitles, syllabus, reservedWords, readPool, writePool };
}

// ---------- 判定 ----------

const optsOf = (it) => (it.type === 'stress' ? it.syllables : it.options) || [];
const partItems = (s, part) => s.items.filter((it) => it.part === part);

// 程序给的是临时判定；教练在 review.items 里写了 verdict 就以教练的为准。
function verdictOf(item, ans, review) {
  const r = review?.items?.[item.id];
  if (r?.verdict) return { verdict: r.verdict, note: r.note || null, final: true };
  if (!ans) return null;
  return { verdict: ans.choice === item.answer ? 'ok' : 'wrong', note: r?.note || null, final: !!review?.done };
}

// 闸门：复检错了一半以上 ⇒ hold（不讲新规则）；教练重讲后在题目文件里写 reteach ⇒ 放行
function gateOf(s) {
  const items = partItems(s, 'recheck');
  if (!items.length) return 'none';
  if (!s.submitted.recheck) return 'pending';
  const wrong = items.filter((it) => verdictOf(it, s.answers[it.id], s.review)?.verdict === 'wrong').length;
  if (wrong * 2 <= items.length) return 'pass';
  return (s.reteach || []).length ? 'reteach' : 'hold';
}
function statusOf(s) {
  if (s.review?.done) return 'reviewed';
  if (gateOf(s) === 'hold') return 'answered';
  const need = PARTS.filter((p) => partItems(s, p).length);
  return need.every((p) => s.submitted[p]) ? 'answered' : 'open';
}
function countsOf(s) {
  const c = { ok: 0, wrong: 0, warn: 0, total: 0 };
  for (const it of s.items) {
    if (!s.submitted[it.part]) continue;
    const v = verdictOf(it, s.answers[it.id], s.review);
    if (!v) continue;
    c[v.verdict] += 1;
    c.total += 1;
  }
  return c;
}

// 一条规则在某一部分的结果：wrong（有错）· hold（全对但有没把握的）· ok
function ruleResults(s, part) {
  const out = new Map();
  if (!s.submitted[part]) return out;
  for (const it of partItems(s, part)) {
    const ans = s.answers[it.id];
    const v = verdictOf(it, ans, s.review);
    if (!v) continue;
    const r = out.get(it.rule) || { wrong: [], unsure: [], total: 0 };
    r.total += 1;
    if (v.verdict === 'wrong') r.wrong.push(it.word);
    else if (ans?.unsure) r.unsure.push(it.word);
    out.set(it.rule, r);
  }
  for (const r of out.values()) r.result = r.wrong.length ? 'wrong' : r.unsure.length ? 'hold' : 'ok';
  return out;
}

// ---------- 规则池：从已复核的场次整个重放出来 ----------
// pool.json 不是手工账，是这个函数的输出。settle 写它，check 核它。

function replayPool(sessions) {
  const rules = new Map(); // id → 状态
  let last = 0;
  for (const s of sessions) {
    if (!s.review?.done) continue;
    const n = s.n;
    last = n;
    // 1) 复检
    for (const [id, r] of ruleResults(s, 'recheck')) {
      const st = rules.get(id);
      if (!st || st.graduated) continue;
      st.rechecks += 1;
      st.lastReview = n;
      const entry = { n, kind: 'recheck', result: r.result };
      if (r.result === 'ok') {
        const i = LADDER.indexOf(st.box);
        if (i === LADDER.length - 1) { st.graduated = true; st.graduatedAt = n; st.nextDue = null; }
        else { st.box = LADDER[i + 1]; st.nextDue = n + st.box; }
      } else if (r.result === 'hold') {
        st.nextDue = n + st.box;
        entry.words = r.unsure;
      } else {
        st.box = LADDER[0];
        st.nextDue = n + 1;
        entry.words = r.wrong;
      }
      st.log.push(entry);
    }
    // 2) 练习：只记错。池里的回第 1 格；已毕业的回池。当次新讲的规则不在这里算。
    for (const [id, r] of ruleResults(s, 'practice')) {
      if (id === s.newRule || r.result !== 'wrong') continue;
      const st = rules.get(id);
      if (!st) continue;
      st.graduated = false;
      st.graduatedAt = null;
      st.box = LADDER[0];
      st.nextDue = n + 1;
      st.log.push({ n, kind: 'practice', result: 'wrong', words: r.wrong });
    }
    // 3) 新规则：讲过并练过就进池，不管当场对没对
    if (s.newRule && s.submitted.practice && !rules.has(s.newRule)) {
      rules.set(s.newRule, { id: s.newRule, box: LADDER[0], added: n, lastReview: null, nextDue: n + 1, rechecks: 0, graduated: false, graduatedAt: null, log: [] });
    }
  }
  const all = [...rules.values()];
  const strip = ({ graduated, graduatedAt, ...rest }) => rest;
  return {
    session: last,
    ladder: LADDER,
    rules: all.filter((r) => !r.graduated).map(strip),
    graduated: all.filter((r) => r.graduated).map(({ graduated, nextDue, ...rest }) => rest),
  };
}

// 第 n 次让规则池变了什么。一行一条，给网页和教练反馈用。
function poolDelta(sessions, n) {
  const before = replayPool(sessions.filter((s) => s.n < n));
  const after = replayPool(sessions.filter((s) => s.n <= n));
  const was = new Map(before.rules.map((r) => [r.id, r]));
  const wasGrad = new Set(before.graduated.map((r) => r.id));
  const why = (r) => r.log.filter((l) => l.n === n).map((l) => {
    const words = l.words?.length ? `（${l.words.join('、')}）` : '';
    if (l.kind === 'practice') return `练习里错了${words}`;
    return { ok: '复检全对', hold: `复检全对但有没把握的${words}`, wrong: `复检有错${words}` }[l.result];
  }).join('，');
  const lines = [];
  for (const r of after.rules) {
    const o = was.get(r.id);
    if (wasGrad.has(r.id)) lines.push(`${r.id}：毕业后${why(r)}，回池第 1 格，下次最早第 ${r.nextDue} 次`);
    else if (!o) lines.push(`${r.id}：新讲，进池第 1 格，下次最早第 ${r.nextDue} 次`);
    else if (why(r)) lines.push(`${r.id}：${why(r)}，第 ${o.box} 格 → 第 ${r.box} 格，下次最早第 ${r.nextDue} 次`);
  }
  for (const g of after.graduated) if (!wasGrad.has(g.id)) lines.push(`${g.id}：复检全对，毕业`);
  return lines;
}

// 第 n 次该复检哪几条：到期的里面，复检次数少的 → 等得久的 → 课表靠前的，最多 RECHECK_CAP 条
function duePick(pool, n, order = []) {
  const rank = (id) => { const i = order.indexOf(id); return i < 0 ? 1e9 : i; };
  const due = pool.rules.filter((r) => r.nextDue <= n).sort((a, b) =>
    a.rechecks - b.rechecks ||
    (a.lastReview ?? a.added) - (b.lastReview ?? b.added) ||
    rank(a.id) - rank(b.id) || a.id.localeCompare(b.id));
  return { picked: due.slice(0, RECHECK_CAP).map((r) => r.id), overflow: due.slice(RECHECK_CAP).map((r) => r.id) };
}

// 复检时一条规则出几题：默认 2；它最近一次是错的（池里最后一条记录是 wrong）就出 3
function recheckCount(pool, id) {
  const r = pool.rules.find((x) => x.id === id);
  const last = r?.log[r.log.length - 1];
  return last?.result === 'wrong' ? 3 : 2;
}

// 下一条该讲的新规则：课表里第一条还没讲过的
function nextNewRule(store, sessions) {
  const taught = new Set(sessions.filter((s) => s.review?.done && s.newRule && s.submitted.practice).map((s) => s.newRule));
  const next = store.syllabus().find((r) => !taught.has(r.id));
  return next ? next.id : null;
}

// ---------- 校验 ----------

function checkAll(store) {
  const errors = [];
  const warns = [];
  const E = (where, msg) => errors.push(`${where}: ${msg}`);
  const W = (where, msg) => warns.push(`${where}: ${msg}`);

  const nums = store.sessionNumbers();
  nums.forEach((n, i) => { if (n !== i + 1) E('sessions/', `编号不连续：第 ${i + 1} 个文件是 ${pad(n)}.json`); });
  const titles = store.ruleTitles();
  const order = store.syllabus().map((r) => r.id);
  const sessions = [];
  for (const n of nums) {
    try { sessions.push(store.loadSession(n)); } catch (e) { E(`sessions/${pad(n)}.json`, 'JSON 读不了：' + e.message); return { errors, warns }; }
  }

  const taughtAt = new Map(); // 规则 → 第几次讲的
  const usedWords = new Map(); // 词 → 第一次出现在哪
  const reserved = store.reservedWords();
  sessions.forEach((s, idx) => {
    const F = `sessions/${pad(nums[idx])}.json`;
    const isLast = idx === sessions.length - 1;
    if (s.n !== nums[idx]) E(F, `n 写的是 ${s.n}，和文件名不一致`);
    if (!s.review?.done && !isLast) E(F, '还没复核，后面却已经有新的场次。只有最后一次可以是未复核的');

    // 题目
    const ids = new Set();
    for (const it of s.items) {
      const I = `${F} ${it.id}`;
      if (ids.has(it.id)) E(I, 'id 重复');
      ids.add(it.id);
      const w = String(it.word).toLowerCase();
      if (usedWords.has(w)) E(I, `「${it.word}」在 ${usedWords.get(w)} 用过了。进池的是规则不是词，每道题都要换新词`);
      else usedWords.set(w, `${F} ${it.id}`);
      if (!s.review?.done && reserved.has(w)) E(I, `「${it.word}」在 ${reserved.get(w)} 里出现过（规则例词或基线卷），她见过读法，换一个词`);
      if (!PARTS.includes(it.part)) { E(I, 'part 只能是 recheck / practice'); continue; }
      if (!String(it.id).startsWith(it.part === 'recheck' ? 'r' : 'p')) E(I, '复检题的 id 用 r 开头，练习题用 p 开头');
      if (!['stress', 'read', 'spell'].includes(it.type)) { E(I, 'type 只能是 stress / read / spell'); continue; }
      const opts = optsOf(it);
      if (it.type === 'stress') {
        if (opts.length < 2) E(I, '重音题至少两个音节');
        if (opts.join('').toLowerCase() !== String(it.word).toLowerCase().replace(/[^a-z]/g, '')) E(I, `syllables 拼起来不是 ${it.word}`);
      } else if (opts.length < 2 || opts.length > 4) E(I, '选项要 2–4 个');
      if (it.type === 'spell' && !it.prompt && !it.promptAudio) E(I, '拼写题要有 prompt（显示的音标）或 promptAudio');
      if (!Number.isInteger(it.answer) || it.answer < 1 || it.answer > opts.length) E(I, 'answer 不在选项范围内');
      if (typeof it.pseudo !== 'boolean') E(I, 'pseudo 要写 true / false');
      if (!it.explain) E(I, '缺 explain');
      if (!it.rule || !titles[it.rule]) E(I, `rule「${it.rule}」在 rules.md 正文里没有对应的 ### 标题`);
      if (!it.ipa) E(I, '缺 ipa');
      else {
        try {
          toEspeak(it.ipa);
          if (it.type === 'stress') {
            if (syllableCount(it.ipa) !== opts.length) E(I, `音标有 ${syllableCount(it.ipa)} 个音节，syllables 有 ${opts.length} 个`);
            else if (stressIndex(it.ipa) !== it.answer) E(I, `音标的主重音在第 ${stressIndex(it.ipa)} 个音节，answer 写的是 ${it.answer}`);
          }
        } catch (e) { E(I, '音标转不了：' + e.message); }
      }
    }

    // 复检：该检哪几条由规则池定，不由教练挑
    const before = replayPool(sessions.slice(0, idx));
    const expect = duePick(before, s.n, order).picked;
    const recheckRules = [...new Set(partItems(s, 'recheck').map((it) => it.rule))];
    const miss = expect.filter((r) => !recheckRules.includes(r));
    const extra = recheckRules.filter((r) => !expect.includes(r));
    if (miss.length) E(F, `复检漏了到期的规则：${miss.join(' ')}`);
    if (extra.length) E(F, `复检里有不该出的规则：${extra.join(' ')}（没到期，或没讲过）`);
    for (const r of recheckRules) {
      const k = partItems(s, 'recheck').filter((it) => it.rule === r).length;
      if (k < 2 || k > 3) E(F, `复检 ${r} 出了 ${k} 题，应为 2–3 题`);
    }

    // 新规则、练习
    const gate = gateOf(s);
    const held = gate === 'hold' || gate === 'reteach';
    const practice = partItems(s, 'practice');
    if (s.newRule) {
      if (taughtAt.has(s.newRule)) E(F, `newRule ${s.newRule} 在第 ${taughtAt.get(s.newRule)} 次已经讲过`);
      if (!titles[s.newRule]) E(F, `newRule ${s.newRule} 在 rules.md 里还没有正文`);
      const next = order.find((id) => !taughtAt.has(id));
      if (next && next !== s.newRule) W(F, `课表下一条是 ${next}，这次讲的是 ${s.newRule}`);
      if (held) E(F, '复检错过半，这次不能讲新规则：newRule 改成 null，练习题换成重讲规则的题');
      else if (practice.filter((it) => it.rule === s.newRule).length < 5) W(F, `新规则 ${s.newRule} 的练习题不到 5 题`);
    }
    if (gate === 'reteach') {
      const wrongRules = [...ruleResults(s, 'recheck')].filter(([, r]) => r.result === 'wrong').map(([id]) => id).sort();
      if ([...(s.reteach || [])].sort().join() !== wrongRules.join()) E(F, `reteach 应该正好是复检错的规则：${wrongRules.join(' ')}`);
    } else if ((s.reteach || []).length) E(F, '复检没有错过半，不该写 reteach');
    for (const it of practice) {
      if (it.rule !== s.newRule && !taughtAt.has(it.rule)) E(`${F} ${it.id}`, `练习题考的 ${it.rule} 还没讲过`);
    }
    if (practice.length && practice.length !== 10 && !held) W(F, `练习是 ${practice.length} 题，不是 10 题`);

    // 作答
    for (const [id, a] of Object.entries(s.answers)) {
      const it = s.items.find((x) => x.id === id);
      const A = `answers/${pad(s.n)}.json ${id}`;
      if (!it) { E(A, '题目文件里没有这道题'); continue; }
      if (!(a.choice === null || (Number.isInteger(a.choice) && a.choice >= 1 && a.choice <= optsOf(it).length))) E(A, 'choice 不在选项范围内');
      if (!['web', 'chat'].includes(a.via)) E(A, 'via 只能是 web / chat');
      if (!s.submitted[it.part]) E(A, `${PART_LABEL[it.part]}还没标记提交（submitted），却已经有作答`);
    }
    for (const p of PARTS) {
      if (!s.submitted[p]) continue;
      for (const it of partItems(s, p)) if (!s.answers[it.id]) E(`answers/${pad(s.n)}.json`, `${PART_LABEL[p]}已提交，但 ${it.id} 没有作答`);
    }

    // 复核
    if (s.review?.done) {
      if (!/^\d{4}-\d{2}-\d{2}$/.test(s.date || '')) E(F, '已复核的场次要填 date（YYYY-MM-DD）');
      if (!(s.review.summary || []).length) E(F, 'review.summary 是空的');
      for (const p of PARTS) if (partItems(s, p).length && !s.submitted[p]) E(F, `已复核，但${PART_LABEL[p]}没有提交。没做的题从题目文件里删掉`);
      const sum = s.review.summary;
      if (!Array.isArray(sum) || sum.some((x) => typeof x !== 'string' || !x)) E(F, 'review.summary 要写成字符串数组，一句一项');
      const qa = s.review.qa;
      if (!Array.isArray(qa) || qa.some((x) => !x || !x.q || !x.a)) E(F, 'review.qa 要写成数组，每项 { "q": …, "a": … }；她没提问就写 []');
      for (const [id, r] of Object.entries(s.review.items || {})) {
        const it = s.items.find((x) => x.id === id);
        if (!it) { E(`${F} review.items.${id}`, '没有这道题'); continue; }
        if (!r.verdict) continue;
        if (!['ok', 'wrong', 'warn'].includes(r.verdict)) E(`${F} review.items.${id}`, 'verdict 只能是 ok / wrong / warn');
        else if (!r.note) E(`${F} review.items.${id}`, '改判要写 note 说明理由');
        else {
          const auto = s.answers[id] && s.answers[id].choice === it.answer ? 'ok' : 'wrong';
          if (r.verdict === auto) E(`${F} review.items.${id}`, `verdict 和程序判的一样（${auto}），不是改判就不要写 verdict，只留 note`);
        }
      }
      for (const it of s.items) {
        const v = verdictOf(it, s.answers[it.id], s.review);
        if (v?.verdict === 'wrong' && !s.review.items?.[it.id]?.note) E(`${F} ${it.id}`, `错题（${it.word}）没有写 review.items 的 note：错在哪、为什么错`);
      }
      if (s.newRule && s.submitted.practice) taughtAt.set(s.newRule, s.n);
    } else if (s.date) W(F, '还没复核就填了 date');
  });

  // 规则池 = 重放结果
  const replay = replayPool(sessions);
  const pool = store.readPool();
  if (JSON.stringify(pool) !== JSON.stringify(replay)) E('pool.json', '和场次记录重放出来的不一致。跑 `node phonics/app/cli.js settle`');

  // 课表的「讲于」
  for (const row of store.syllabus()) {
    const n = taughtAt.get(row.id);
    if (n && !row.taught.startsWith(`第 ${n} 次`)) E('rules.md 课表', `${row.id} 是第 ${n} 次讲的，「讲于」写的是「${row.taught}」`);
    if (!n && !row.taught.startsWith('未讲')) E('rules.md 课表', `${row.id} 还没讲过（没有已复核的场次讲它），「讲于」写的是「${row.taught}」`);
  }
  for (const id of taughtAt.keys()) if (!order.includes(id)) E('rules.md 课表', `${id} 讲过了，课表里却没有这一行`);

  return { errors, warns };
}

module.exports = {
  PARTS, PART_LABEL, LADDER, RECHECK_CAP, pad, createStore,
  optsOf, partItems, verdictOf, gateOf, statusOf, countsOf, ruleResults,
  replayPool, poolDelta, duePick, recheckCount, nextNewRule, checkAll,
};
