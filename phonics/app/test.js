#!/usr/bin/env node
// 回归测试：node phonics/app/test.js
// 只在临时目录里造数据，一次都不碰真档案。改过 lib/ 或 cli.js，全绿才许拿去动真档案。

const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const core = require('./lib/core.js');
const { toEspeak, syllableCount, stressIndex } = require('./lib/ipa.js');

let passed = 0;
const failed = [];
function test(name, fn) {
  try { fn(); passed += 1; } catch (e) { failed.push(name); console.log(`✗ ${name}\n    ${String(e.message).split('\n')[0]}`); }
}

// ---------- 造数据 ----------

// 一道重音题：n 个音节，第 answer 个重读
let wordSeq = 0;
function item(id, rule, answer, n = 3, extra = {}) {
  const tag = (wordSeq++).toString(26).replace(/\d/g, (d) => 'qrstuvwxyz'[d]); // 每道题一个不重复的词
  const syllables = Array.from({ length: n }, (_, i) => (i === 0 ? tag : '') + 'ta' + 'bdf'[i % 3]);
  return {
    id, part: id.startsWith('r') ? 'recheck' : 'practice', type: 'stress',
    word: syllables.join(''), pseudo: true, syllables, answer,
    ipa: syllables.map((_, i) => (i + 1 === answer ? 'ˈ' : '') + 'tæ').join('.'),
    rule, explain: '讲解', ...extra,
  };
}
// 内存里的一场（给 replayPool / gateOf 这些纯函数用）
function sess(n, { newRule = null, recheck = {}, practice = {}, reviewed = true, reteach } = {}) {
  const items = [];
  const answers = {};
  const add = (prefix, spec) => {
    for (const [rule, marks] of Object.entries(spec)) {
      [...marks].forEach((m) => {
        const id = prefix + (items.filter((x) => x.id.startsWith(prefix)).length + 1);
        items.push(item(id, rule, 2));
        answers[id] = { choice: m === 'x' ? 1 : 2, unsure: m === '?', via: 'web' }; // o 对 · x 错 · ? 对但没把握
      });
    }
  };
  add('r', recheck);
  add('p', practice);
  const submitted = {};
  if (Object.keys(recheck).length) submitted.recheck = 't';
  if (Object.keys(practice).length) submitted.practice = 't';
  const notes = Object.fromEntries(items.filter((it) => answers[it.id].choice !== it.answer).map((it) => [it.id, { note: '备注' }]));
  return { n, date: '2026-01-01', newRule, reteach, items, answers, submitted, review: reviewed ? { done: true, items: notes, summary: ['s'], qa: [] } : null };
}
const RULES = (taught) => ['# 规则表', '', '| 编号 | 规则 | 例词 | 讲于 |', '|---|---|---|---|',
  ...['S1', 'S2', 'S3', 'S4', 'S5', 'S6'].map((id) => `| ${id} | 规则 | 例 | ${taught[id] ? `第 ${taught[id]} 次` : '未讲'} |`),
  '', '## 正文', '', ...['S1', 'S2', 'S3', 'S4', 'S5', 'S6'].map((id) => `### ${id} · 标题${id}（第 N 次讲）\n\n正文\n`)].join('\n');
// 落盘成一份 phonics 目录
function mkRoot(sessions, taught) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'phonics-test-'));
  fs.mkdirSync(path.join(root, 'data', 'sessions'), { recursive: true });
  fs.mkdirSync(path.join(root, 'data', 'answers'), { recursive: true });
  const auto = {};
  for (const s of sessions) {
    const { answers, submitted, ...file } = s;
    fs.writeFileSync(path.join(root, 'data', 'sessions', core.pad(s.n) + '.json'), JSON.stringify(file, null, 2));
    fs.writeFileSync(path.join(root, 'data', 'answers', core.pad(s.n) + '.json'), JSON.stringify({ n: s.n, answers, submitted }, null, 2));
    if (s.review?.done && s.newRule && submitted.practice) auto[s.newRule] = s.n;
  }
  fs.writeFileSync(path.join(root, 'rules.md'), RULES(taught || auto));
  const store = core.createStore(root);
  store.writePool(core.replayPool(store.sessionNumbers().map(store.loadSession)));
  return store;
}
const errorsOf = (store) => core.checkAll(store).errors;
const hasError = (store, re) => assert.ok(errorsOf(store).some((e) => re.test(e)), `没报出 ${re}：${JSON.stringify(errorsOf(store))}`);
const rule = (pool, id) => pool.rules.find((r) => r.id === id);
const P10 = (r) => ({ [r]: 'oooooooooo' });

// ---------- 音标 ----------

test('音标转写：photography', () => assert.equal(toEspeak('fə.ˈtɑː.ɡrə.fi'), "f@t'A:gr@fi"));
test('音标转写：成音节的 l 和 n', () => { assert.equal(toEspeak('ˈteɪ.bl'), "t'eIb@L"); assert.equal(toEspeak('ˈneɪ.ʃn'), "n'eIS@n"); });
test('音标转写：带 r 的元音', () => assert.equal(toEspeak('ˌvɑː.lən.ˈtɪr'), "v,A:l@nt'i@3"));
test('音标转写：把重音挪到别的音节', () => assert.equal(toEspeak('fə.ˈtɑː.ɡrə.fi', 3), "f@tA:gr'@fi"));
test('音标转写：不认识的符号要报错', () => assert.throws(() => toEspeak('fɛt')));
test('音节数和重音位置', () => { assert.equal(syllableCount('fə.ˈtɑː.ɡrə.fi'), 4); assert.equal(stressIndex('fə.ˈtɑː.ɡrə.fi'), 2); assert.equal(stressIndex('kæt'), 1); assert.equal(stressIndex('kæ.tə'), 0); });

// ---------- 规则池重放 ----------

test('新规则讲过就进池：第 1 格，下一次复检', () => {
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: P10('S1') })]);
  assert.deepEqual([rule(pool, 'S1').box, rule(pool, 'S1').nextDue, pool.session], [1, 2, 1]);
});
test('新规则当场练错也照样进第 1 格', () => {
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: { S1: 'xxxxxooooo' } })]);
  assert.deepEqual([rule(pool, 'S1').box, rule(pool, 'S1').log.length], [1, 0]);
});
test('没复核的场次不进池', () => {
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: P10('S1'), reviewed: false })]);
  assert.deepEqual([pool.rules.length, pool.session], [0, 0]);
});
test('复检全对：升一格，间隔 = 格数', () => {
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: P10('S1') }), sess(2, { recheck: { S1: 'ooo' }, newRule: 'S2', practice: P10('S2') })]);
  assert.deepEqual([rule(pool, 'S1').box, rule(pool, 'S1').nextDue, rule(pool, 'S1').rechecks], [2, 4, 1]);
  assert.deepEqual([rule(pool, 'S2').box, rule(pool, 'S2').nextDue], [1, 3]);
});
test('复检有一题错：回第 1 格，下一次再检', () => {
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: P10('S1') }), sess(2, { recheck: { S1: 'oo' } }), sess(4, { recheck: { S1: 'ox' } })]);
  assert.deepEqual([rule(pool, 'S1').box, rule(pool, 'S1').nextDue], [1, 5]);
});
test('复检全对但有没把握：原地不动', () => {
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: P10('S1') }), sess(2, { recheck: { S1: 'oo' } }), sess(4, { recheck: { S1: 'o?' } })]);
  assert.deepEqual([rule(pool, 'S1').box, rule(pool, 'S1').nextDue, rule(pool, 'S1').log[1].result], [2, 6, 'hold']);
});
test('复检对了、同一次练习里又错：以练习为准，回第 1 格', () => {
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: P10('S1') }), sess(2, { recheck: { S1: 'ooo' }, newRule: 'S2', practice: { S2: 'oooooo', S1: 'ooox' } })]);
  assert.deepEqual([rule(pool, 'S1').box, rule(pool, 'S1').nextDue], [1, 3]);
});
test('练习里旧规则全对：不动', () => {
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: P10('S1') }), sess(2, { recheck: { S1: 'oo' }, newRule: 'S2', practice: { S2: 'oooooo', S1: 'oooo' } })]);
  assert.deepEqual([rule(pool, 'S1').box, rule(pool, 'S1').nextDue], [2, 4]);
});
test('教练改判：错改成不算错，规则算全对', () => {
  const s2 = sess(2, { recheck: { S1: 'ox' } });
  s2.review.items.r2 = { verdict: 'warn', note: '写法问题' };
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: P10('S1') }), s2]);
  assert.equal(rule(pool, 'S1').box, 2);
});
test('教练改判：对改成错，规则回第 1 格', () => {
  const s2 = sess(2, { recheck: { S1: 'oo' } });
  s2.review.items.r1 = { verdict: 'wrong', note: '蒙的' };
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: P10('S1') }), s2]);
  assert.equal(rule(pool, 'S1').box, 1);
});
const toGrad = [sess(1, { newRule: 'S1', practice: P10('S1') }), sess(2, { recheck: { S1: 'oo' } }), sess(4, { recheck: { S1: 'oo' } }), sess(8, { recheck: { S1: 'oo' } }), sess(16, { recheck: { S1: 'oo' } })];
test('一路全对：1 → 2 → 4 → 8 → 毕业', () => {
  assert.equal(rule(core.replayPool(toGrad.slice(0, 4)), 'S1').box, 8);
  const pool = core.replayPool(toGrad);
  assert.deepEqual([pool.rules.length, pool.graduated[0].id, pool.graduated[0].graduatedAt], [0, 'S1', 16]);
});
test('毕业的规则在练习里错了：回池，第 1 格', () => {
  const pool = core.replayPool([...toGrad, sess(17, { newRule: 'S2', practice: { S2: 'oooooo', S1: 'ooxo' } })]);
  assert.deepEqual([pool.graduated.length, rule(pool, 'S1').box, rule(pool, 'S1').nextDue], [0, 1, 18]);
});

// ---------- 到期挑选 ----------

test('到期：只取 nextDue ≤ 本次的', () => {
  const pool = { rules: [{ id: 'S1', nextDue: 3, rechecks: 0, added: 1 }, { id: 'S2', nextDue: 4, rechecks: 0, added: 2 }] };
  assert.deepEqual(core.duePick(pool, 3).picked, ['S1']);
});
test('到期太多：复检次数少 → 等得久 → 课表靠前，最多 4 条', () => {
  const pool = { rules: [
    { id: 'S1', nextDue: 5, rechecks: 2, lastReview: 1, added: 1 }, { id: 'S2', nextDue: 5, rechecks: 0, lastReview: null, added: 4 },
    { id: 'S3', nextDue: 5, rechecks: 1, lastReview: 3, added: 2 }, { id: 'S4', nextDue: 5, rechecks: 1, lastReview: 2, added: 2 },
    { id: 'S6', nextDue: 5, rechecks: 1, lastReview: 2, added: 2 }, { id: 'S5', nextDue: 5, rechecks: 1, lastReview: 2, added: 2 }] };
  const r = core.duePick(pool, 9, ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']);
  assert.deepEqual(r.picked, ['S2', 'S4', 'S5', 'S6']);
  assert.deepEqual(r.overflow, ['S3', 'S1']);
});

// ---------- 闸门与状态 ----------

test('闸门：没有复检题 = none', () => assert.equal(core.gateOf(sess(1, { newRule: 'S1', practice: P10('S1') })), 'none'));
test('闸门：复检没交 = pending', () => { const s = sess(2, { recheck: { S1: 'oo' } }); s.submitted = {}; assert.equal(core.gateOf(s), 'pending'); });
test('闸门：正好错一半 = pass', () => assert.equal(core.gateOf(sess(2, { recheck: { S1: 'ox' } })), 'pass'));
test('闸门：错过半 = hold', () => assert.equal(core.gateOf(sess(2, { recheck: { S1: 'oxx' } })), 'hold'));
test('闸门：错过半、教练写了 reteach = reteach', () => assert.equal(core.gateOf(sess(2, { recheck: { S1: 'oxx' }, reteach: ['S1'] })), 'reteach'));
test('状态：没做完 = open；做完 = answered；复核完 = reviewed', () => {
  const s = sess(2, { recheck: { S1: 'oo' }, newRule: 'S2', practice: P10('S2'), reviewed: false });
  assert.equal(core.statusOf(s), 'answered');
  assert.equal(core.statusOf({ ...s, submitted: { recheck: 't' } }), 'open');
  assert.equal(core.statusOf({ ...s, review: { done: true } }), 'reviewed');
});
test('状态：闸门拦住时算 answered（等教练）', () => {
  const s = sess(2, { recheck: { S1: 'oxx' }, reviewed: false });
  s.items.push(item('p1', 'S2', 2));
  assert.equal(core.statusOf(s), 'answered');
});

// ---------- 校验 ----------

const base = () => [sess(1, { newRule: 'S1', practice: P10('S1') }), sess(2, { recheck: { S1: 'oo' }, newRule: 'S2', practice: { S2: 'oooooo', S1: 'oooo' } })];
test('校验：正常的档案 ERROR 0', () => assert.deepEqual(errorsOf(mkRoot(base())), []));
test('校验：还没作答的最后一场也 ERROR 0', () => {
  const s3 = sess(3, { recheck: { S2: 'oo' }, newRule: 'S3', practice: P10('S3'), reviewed: false });
  s3.answers = {}; s3.submitted = {}; s3.date = null;
  assert.deepEqual(errorsOf(mkRoot([...base(), s3])), []);
});
test('校验：答案和音标的重音对不上', () => { const s = base(); s[0].items[0].answer = 1; hasError(mkRoot(s), /主重音在第 2 个音节/); });
test('校验：syllables 拼不成这个词', () => { const s = base(); s[0].items[0].word = 'wrongword'; hasError(mkRoot(s), /拼起来不是/); });
test('校验：音标音节数不对', () => { const s = base(); s[0].items[0].ipa = 'ˈtæ.tæ'; hasError(mkRoot(s), /音节，syllables 有/); });
test('校验：复检漏了到期的规则', () => { const s = base(); s[1].items = s[1].items.filter((it) => it.part !== 'recheck'); hasError(mkRoot(s), /复检漏了到期的规则：S1/); });
test('校验：复检出了没到期的规则', () => {
  const s3 = sess(3, { recheck: { S1: 'oo', S2: 'oo' }, newRule: 'S3', practice: P10('S3') }); // S1 第 2 次升到第 2 格，第 4 次才到期
  hasError(mkRoot([...base(), s3]), /不该出的规则：S1/);
});
test('校验：一条规则的复检题不是 2–3 题', () => { const s = base(); s[1].items.splice(0, 1); hasError(mkRoot(s), /复检 S1 出了 1 题/); });
test('校验：错题没写 note', () => {
  const s = [base()[0], sess(2, { recheck: { S1: 'ox' }, newRule: 'S2', practice: P10('S2') })];
  s[1].review.items = {};
  hasError(mkRoot(s), /没有写 review.items 的 note/);
});
test('校验：前一场没复核就出了下一场', () => {
  const s = [base()[0], sess(2, { recheck: { S1: 'oo' }, reviewed: false }), sess(3, { recheck: { S1: 'oo' }, reviewed: false })];
  hasError(mkRoot(s), /只有最后一次可以是未复核的/);
});
test('校验：同一条规则讲了两次', () => {
  const s = [...base(), sess(3, { recheck: { S2: 'oo' }, newRule: 'S1', practice: P10('S1') })];
  hasError(mkRoot(s, { S1: 1, S2: 2 }), /newRule S1 在第 1 次已经讲过/);
});
test('校验：练习考了没讲过的规则', () => { const s = base(); s[0].items[9].rule = 'S5'; hasError(mkRoot(s), /练习题考的 S5 还没讲过/); });
test('校验：课表「讲于」没更新', () => hasError(mkRoot(base(), { S1: 1 }), /S2 是第 2 次讲的/));
test('校验：课表「讲于」写早了', () => hasError(mkRoot(base(), { S1: 1, S2: 2, S3: 3 }), /S3 还没讲过/));
test('校验：pool.json 过期', () => {
  const store = mkRoot(base());
  store.writePool({ ...store.readPool(), session: 1 });
  hasError(store, /pool\.json/);
});
test('校验：没提交的部分却有作答', () => { const s = base(); delete s[1].submitted.recheck; hasError(mkRoot(s), /还没标记提交/); });
test('校验：已提交的部分缺作答', () => { const s = base(); delete s[1].answers.p3; hasError(mkRoot(s), /p3 没有作答/); });
test('校验：已复核却没填日期', () => { const s = base(); s[1].date = null; hasError(mkRoot(s), /要填 date/); });
test('校验：已复核却有部分没提交', () => { const s = base(); delete s[1].submitted.practice; for (const k of Object.keys(s[1].answers)) if (k.startsWith('p')) delete s[1].answers[k]; hasError(mkRoot(s), /练习没有提交/); });
test('校验：闸门拦住的那次不能讲新规则', () => {
  const s = [base()[0], sess(2, { recheck: { S1: 'xx' }, newRule: 'S2', practice: P10('S2') })];
  hasError(mkRoot(s), /这次不能讲新规则/);
});
test('校验：reteach 必须正好是复检错的规则', () => {
  const s = [base()[0], sess(2, { recheck: { S1: 'xx' }, practice: P10('S1'), reteach: ['S2'] })];
  hasError(mkRoot(s), /reteach 应该正好是复检错的规则：S1/);
});
test('校验：闸门拦住、重讲后练完，是合法的一场', () => {
  const s = [base()[0], sess(2, { recheck: { S1: 'xx' }, practice: P10('S1'), reteach: ['S1'] })];
  assert.deepEqual(errorsOf(mkRoot(s)), []);
});
test('校验：用过的词不能再出', () => { const s = base(); s[1].items[3] = { ...s[1].items[3], word: s[0].items[0].word, syllables: s[0].items[0].syllables }; hasError(mkRoot(s), /用过了/); });
test('规则池变化：新讲、升格、练习错', () => {
  const all = [sess(1, { newRule: 'S1', practice: P10('S1') }), sess(2, { recheck: { S1: 'ooo' }, newRule: 'S2', practice: { S2: 'oooooo', S1: 'ooox' } }), sess(3, { recheck: { S1: 'oo', S2: 'o?' } })];
  assert.match(core.poolDelta(all, 1)[0], /^S1：新讲，进池第 1 格，下次最早第 2 次$/);
  assert.match(core.poolDelta(all, 2)[0], /^S1：复检全对，练习里错了（.+），第 1 格 → 第 1 格，下次最早第 3 次$/);
  assert.match(core.poolDelta(all, 3).join('|'), /S1：复检全对，第 1 格 → 第 2 格，下次最早第 5 次\|S2：复检全对但有没把握的（.+），第 1 格 → 第 1 格，下次最早第 4 次/);
});
test('规则池变化：毕业', () => assert.deepEqual(core.poolDelta(toGrad, 16), ['S1：复检全对，毕业']));
test('校验：未复核的场次不能用规则正文里的例词', () => {
  const s3 = sess(3, { recheck: { S2: 'oo' }, newRule: 'S3', practice: P10('S3'), reviewed: false });
  s3.answers = {}; s3.submitted = {}; s3.date = null;
  const store = mkRoot([...base(), s3]);
  fs.appendFileSync(store.rulesFile, `\n例词：${s3.items[4].word.toUpperCase()}\n`);
  hasError(store, /她见过读法/);
});
test('校验：已复核的场次不查例词（历史不追）', () => {
  const store = mkRoot(base());
  fs.appendFileSync(store.rulesFile, `\n例词：${store.loadSession(1).items[0].word}\n`);
  assert.deepEqual(errorsOf(store), []);
});
test('校验：verdict 和程序判的一样就不该写', () => {
  const s = [base()[0], sess(2, { recheck: { S1: 'ox' }, newRule: 'S2', practice: P10('S2') })];
  s[1].review.items.r2 = { verdict: 'wrong', note: '备注' };
  hasError(mkRoot(s), /不是改判就不要写 verdict/);
});
test('校验：改判必须写理由', () => {
  const s = [base()[0], sess(2, { recheck: { S1: 'ox' }, newRule: 'S2', practice: P10('S2') })];
  s[1].review.items.r2 = { verdict: 'warn' };
  hasError(mkRoot(s), /改判要写 note/);
});
test('校验：summary 要数组、qa 要数组', () => {
  const a = base(); a[1].review.summary = '一句话'; hasError(mkRoot(a), /summary 要写成字符串数组/);
  const b = base(); delete b[1].review.qa; hasError(mkRoot(b), /qa 要写成数组/);
});
test('复检题数：默认 2，最近一次错了就 3', () => {
  const pool = core.replayPool([sess(1, { newRule: 'S1', practice: P10('S1') }), sess(2, { recheck: { S1: 'ox' }, newRule: 'S2', practice: P10('S2') })]);
  assert.deepEqual([core.recheckCount(pool, 'S1'), core.recheckCount(pool, 'S2')], [3, 2]);
});
test('下一条新规则 = 课表里第一条没讲过的', () => {
  const store = mkRoot(base());
  assert.equal(core.nextNewRule(store, store.sessionNumbers().map(store.loadSession)), 'S3');
});

// ---------- 加练 ----------

// 一道加练题：每个错选项都带错因
function bankItem(id, rule, answer, n = 3, extra = {}) {
  const { part, ...it } = item('p0', rule, answer, n);
  const traps = Object.fromEntries(it.syllables.map((_, i) => [i + 1, '错因']).filter(([k]) => k !== answer));
  return { ...it, id, traps, ...extra };
}
function withBank(store, items, attempts) {
  fs.writeFileSync(path.join(store.data, 'bank.json'), JSON.stringify({ items }, null, 2));
  if (attempts) fs.writeFileSync(path.join(store.data, 'answers', 'drill.json'), JSON.stringify({ attempts }, null, 2));
  return store;
}
const att = (id, choice, extra = {}) => ({ id, choice, unsure: false, via: 'web', at: 't', after: 2, ...extra });

test('加练：干净的题库和作答没有错误', () => {
  const store = withBank(mkRoot(base()), [bankItem('b001', 'S1', 2), bankItem('b002', 'S2', 1)], [att('b001', 2)]);
  assert.deepEqual(errorsOf(store), []);
});
test('加练：下一题 = 题库里第一道没做的；统计按规则分', () => {
  const store = withBank(mkRoot(base()), [bankItem('b001', 'S1', 2), bankItem('b002', 'S2', 1), bankItem('b003', 'S1', 2)],
    [att('b001', 1), att('b002', 1)]);
  const d = core.drillState(store);
  assert.equal(d.next.id, 'b003');
  assert.deepEqual([d.total, d.done, d.ok, d.wrong], [3, 2, 1, 1]);
  assert.deepEqual(d.byRule.S1, { total: 2, done: 1, ok: 0, wrong: 1 });
  assert.deepEqual(Object.keys(core.drillState(withBank(store, [bankItem('b001', 'S2', 1), bankItem('b002', 'S1', 2)])).byRule), ['S1', 'S2']); // 按课表顺序
  assert.deepEqual(d.rows.map((r) => [r.item.id, r.ok]), [['b001', false], ['b002', true]]);
});
test('加练：全做完就没有下一题', () => {
  const store = withBank(mkRoot(base()), [bankItem('b001', 'S1', 2)], [att('b001', null)]);
  const d = core.drillState(store);
  assert.equal(d.next, null);
  assert.equal(d.wrong, 1); // 「不知道」算错
});
test('加练：追加作答不动已有的记录', () => {
  const store = withBank(mkRoot(base()), [bankItem('b001', 'S1', 2), bankItem('b002', 'S2', 1)], [att('b001', 2)]);
  store.appendDrill(att('b002', 3));
  assert.deepEqual(store.loadDrill().map((a) => a.id), ['b001', 'b002']);
  assert.deepEqual(errorsOf(store), []);
});
test('加练：不改规则池', () => {
  const store = withBank(mkRoot(base()), [bankItem('b001', 'S1', 2)], [att('b001', 1)]);
  assert.deepEqual(core.replayPool(store.sessionNumbers().map(store.loadSession)), store.readPool());
  assert.deepEqual(errorsOf(store), []);
});
test('校验：加练题每个错选项都要有错因', () => {
  const it = bankItem('b001', 'S1', 2);
  delete it.traps[3];
  hasError(withBank(mkRoot(base()), [it]), /traps 缺第 3 个选项的错因/);
});
test('校验：正确答案不该有错因', () => {
  const it = bankItem('b001', 'S1', 2);
  it.traps[2] = '错因';
  hasError(withBank(mkRoot(base()), [it]), /是正确答案，不该有错因/);
});
test('校验：加练只出讲过的规则', () => {
  hasError(withBank(mkRoot(base()), [bankItem('b001', 'S3', 2)]), /加练只出讲过的规则，S3 还没讲/);
});
test('校验：加练题不能和场次题用同一个词', () => {
  const store = mkRoot(base());
  const used = store.loadSession(1).items[0];
  const it = bankItem('b001', 'S1', used.answer, used.syllables.length, { word: used.word, syllables: used.syllables, ipa: used.ipa });
  it.traps = Object.fromEntries(used.syllables.map((_, i) => [i + 1, '错因']).filter(([k]) => k !== used.answer));
  hasError(withBank(store, [it]), /场次题和加练题不能用同一个词/);
});
test('校验：没做过的加练题不能用规则正文里的例词，做过的不追', () => {
  const store = withBank(mkRoot(base()), [bankItem('b001', 'S1', 2)]);
  fs.appendFileSync(store.rulesFile, `\n例词：${store.loadBank()[0].word}\n`);
  hasError(store, /bank\.json b001: .+她见过读法/);
  withBank(store, store.loadBank(), [att('b001', 2)]);
  assert.deepEqual(errorsOf(store), []);
});
test('校验：加练题的音标重音要和 answer 一致', () => {
  hasError(withBank(mkRoot(base()), [bankItem('b001', 'S1', 2, 3, { ipa: 'ˈtæ.tæ.tæ' })]), /bank\.json b001: 音标的主重音在第 1 个音节/);
});
test('校验：加练作答要指向题库里的题、每题一条、字段齐全', () => {
  const bank = [bankItem('b001', 'S1', 2)];
  hasError(withBank(mkRoot(base()), bank, [att('b009', 1)]), /题库里没有 b009/);
  hasError(withBank(mkRoot(base()), bank, [att('b001', 1), att('b001', 2)]), /加练每道题只做一次/);
  hasError(withBank(mkRoot(base()), bank, [att('b001', 7)]), /drill\.json 第 1 条: choice 不在选项范围内/);
  hasError(withBank(mkRoot(base()), bank, [att('b001', 1, { via: 'x' })]), /drill\.json 第 1 条: via 只能是/);
  hasError(withBank(mkRoot(base()), bank, [att('b001', 1, { after: undefined })]), /after 要写/);
});
test('校验：加练题的 id 用 b 开头', () => {
  hasError(withBank(mkRoot(base()), [bankItem('x1', 'S1', 2)]), /加练题的 id 用 b 开头加数字/);
});

console.log(`\n${failed.length ? '✗' : '✓'} ${passed} 过 · ${failed.length} 挂`);
process.exit(failed.length ? 1 : 0);
