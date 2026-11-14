// 自然拼读练习工具（本地用，无第三方依赖）
//   node phonics/app/server.js [--port 4310] [--root <另一份 phonics 目录，测试用>]
//
// 网页只是界面。数据都在 phonics/data/ 和 phonics/rules.md：
//   data/sessions/NNN.json  教练写：题目 + 复核（review）
//   data/answers/NNN.json   她的作答。网页提交时写；她在对话里作答时由教练写（via: "chat"）
//   data/bank.json          教练写：加练题库（每个错选项都带一句「为什么不对」）
//   data/answers/drill.json 加练的作答，一题一条往后追加
//   data/pool.json          cli.js settle 算出来的规则池（网页显示时自己重放，不读它）
//   rules.md                教练写：规则正文
// 网页**只写** data/answers/。程序给的对错是临时的，以教练的复核为准。

const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const { execFile } = require('node:child_process');
const { toEspeak } = require('./lib/ipa.js');
const core = require('./lib/core.js');

function arg(name, def) {
  const i = process.argv.indexOf('--' + name);
  return i > -1 && process.argv[i + 1] ? process.argv[i + 1] : def;
}
const PORT = Number(arg('port', process.env.PORT || 4310));
const APP = __dirname;
const ROOT = path.resolve(arg('root', path.join(APP, '..')));
const PUBLIC = path.join(APP, 'public');
const store = core.createStore(ROOT);
const { PARTS, PART_LABEL, verdictOf, gateOf, statusOf, countsOf, partItems } = core;
const { sessionNumbers, loadSession, saveAnswers, ruleTitles } = store;

function itemView(s, it, open) {
  const base = {
    // 拼写题的 word 就是答案，作答前不发给页面
    id: it.id, part: it.part, type: it.type, word: it.type === 'spell' && !open ? null : it.word, pseudo: !!it.pseudo,
    syllables: it.syllables, options: it.options, prompt: it.prompt, promptAudio: !!it.promptAudio,
  };
  if (!open) return base;
  const ans = s.answers[it.id] || null;
  const v = verdictOf(it, ans, s.review) || {};
  return { ...base, answer: it.answer, ipa: it.ipa, rule: it.rule, explain: it.explain, my: ans, ...v };
}
function sessionView(s) {
  const gate = gateOf(s);
  const parts = [];
  for (const key of PARTS) {
    const items = partItems(s, key);
    if (!items.length) continue;
    const submitted = !!s.submitted[key];
    const locked = key === 'practice' && (gate === 'pending' || gate === 'hold');
    parts.push({
      key, label: PART_LABEL[key], submitted, locked, count: items.length,
      items: locked ? [] : items.map((it) => itemView(s, it, submitted)),
    });
  }
  return {
    n: s.n, date: s.date, stage: s.stage, newRule: s.newRule || null, note: s.note || null,
    reteach: gate === 'reteach' ? s.reteach : [],
    status: statusOf(s), gate, parts, counts: countsOf(s),
    review: s.review?.done ? {
      summary: s.review.summary || [], qa: s.review.qa || [],
      pool: core.poolDelta(sessionNumbers().map((n) => loadSession(n)), s.n),
    } : null,
  };
}

// ---------- 加练 ----------
// 一次一题，答完当场给结果。对错由程序按题库判；讲解和每个错选项的错因是教练事先写在题库里的。

function drillView(it, a) {
  const base = {
    id: it.id, part: 'drill', type: it.type, word: it.type === 'spell' && !a ? null : it.word, pseudo: !!it.pseudo,
    syllables: it.syllables, options: it.options, prompt: it.prompt, promptAudio: !!it.promptAudio,
  };
  if (!a) return base;
  const ok = a.choice === it.answer;
  return {
    ...base, answer: it.answer, ipa: it.ipa, rule: it.rule, explain: it.explain, my: a,
    verdict: ok ? 'ok' : 'wrong', final: true, trap: ok || a.choice === null ? null : it.traps?.[a.choice] || null,
  };
}
function drillOverview() {
  const st = core.drillState(store);
  return {
    total: st.total, done: st.done, ok: st.ok, wrong: st.wrong, byRule: st.byRule, titles: ruleTitles(),
    item: st.next ? drillView(st.next, null) : null,
    history: st.rows.map((r) => drillView(r.item, r.attempt)).reverse(),
  };
}
const drillRows = () => core.drillState(store).rows.map((r) => ({ n: null, partLabel: '加练', ...drillView(r.item, r.attempt) }));

// ---------- 发音 ----------

const ttsCache = new Map();
let hasEspeak = null;
function espeak(args) {
  return new Promise((resolve, reject) => {
    execFile('espeak-ng', args, { encoding: 'buffer', maxBuffer: 16 * 1024 * 1024 }, (err, stdout) => {
      if (err) reject(err); else resolve(stdout);
    });
  });
}
async function checkEspeak() {
  if (hasEspeak === null) hasEspeak = await espeak(['--version']).then(() => true, () => false);
  return hasEspeak;
}
async function tts(ipa, stress, slow) {
  const ph = toEspeak(ipa, stress || undefined);
  const key = ph + (slow ? '|slow' : '');
  if (!ttsCache.has(key)) {
    ttsCache.set(key, await espeak(['-v', 'en-us', '-s', slow ? '95' : '150', '--stdout', '[[' + ph + ']]']));
  }
  return ttsCache.get(key);
}

const wordCache = new Map();
// 美音真人录音：直接问 Wikimedia Commons 有没有 En-us-<词> 这个文件。
// （不再用 dictionaryapi.dev 给的 mp3 地址 —— 那批地址全部打不开。）
async function lookupWord(word) {
  if (wordCache.has(word)) return wordCache.get(word);
  const out = { word, us: null, source: null };
  try {
    const forms = [...new Set([word, word[0].toUpperCase() + word.slice(1)])];
    const titles = forms.flatMap((w) => ['ogg', 'oga', 'wav'].map((ext) => `File:En-us-${w}.${ext}`)).join('|');
    const r = await fetch('https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url&titles=' + encodeURIComponent(titles),
      { headers: { 'User-Agent': 'phonics-practice-tool/1.0 (local study tool)' } });
    if (r.ok) {
      const pages = Object.values((await r.json()).query?.pages || {});
      const hit = pages.find((p) => p.imageinfo?.[0]?.url);
      if (hit) {
        out.us = hit.imageinfo[0].url.split('?')[0];
        out.source = hit.imageinfo[0].descriptionurl || null;
      }
      wordCache.set(word, out);
    } else out.error = 'Wikimedia ' + r.status;
  } catch (e) {
    out.error = String(e.message || e);
  }
  return out;
}
function seenWord(word) {
  const seen = [];
  for (const n of sessionNumbers()) {
    const s = loadSession(n);
    for (const it of s.items) {
      if (it.word.toLowerCase() !== word || !s.submitted[it.part]) continue;
      seen.push({ n, partLabel: PART_LABEL[it.part], ...itemView(s, it, true) });
    }
  }
  seen.push(...drillRows().filter((r) => r.word.toLowerCase() === word));
  return seen;
}

// ---------- HTTP ----------

function send(res, code, body, type = 'application/json; charset=utf-8') {
  res.writeHead(code, { 'Content-Type': type, 'Cache-Control': 'no-store' });
  res.end(Buffer.isBuffer(body) || typeof body === 'string' ? body : JSON.stringify(body));
}
function readBody(req) {
  return new Promise((resolve, reject) => {
    let data = '';
    req.on('data', (c) => { data += c; if (data.length > 1e6) reject(new Error('too large')); });
    req.on('end', () => { try { resolve(JSON.parse(data || '{}')); } catch (e) { reject(e); } });
    req.on('error', reject);
  });
}
const STATIC = { '/': ['index.html', 'text/html'], '/app.js': ['app.js', 'text/javascript'], '/style.css': ['style.css', 'text/css'] };

async function handle(req, res) {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const p = url.pathname;

  if (STATIC[p]) {
    const [file, type] = STATIC[p];
    return send(res, 200, fs.readFileSync(path.join(PUBLIC, file)), type + '; charset=utf-8');
  }

  if (p === '/api/overview') {
    const titles = ruleTitles();
    const sessions = sessionNumbers().map((n) => {
      const s = loadSession(n);
      return { n, date: s.date, newRule: s.newRule || null, status: statusOf(s), counts: countsOf(s) };
    });
    const pool = core.replayPool(sessionNumbers().map((n) => loadSession(n)));
    const open = sessions.find((s) => s.status === 'open');
    const waiting = sessions.filter((s) => s.status === 'answered').map((s) => s.n);
    return send(res, 200, { pool, titles, sessions, open: open ? open.n : null, waiting, tts: await checkEspeak() });
  }

  if (p === '/api/rules') {
    return send(res, 200, { markdown: store.rulesText(), titles: ruleTitles() });
  }

  if (p === '/api/mistakes') {
    const out = [];
    for (const n of sessionNumbers()) {
      const s = loadSession(n);
      for (const it of s.items) {
        if (!s.submitted[it.part]) continue;
        const v = itemView(s, it, true);
        if (v.verdict === 'wrong' || v.my?.unsure) out.push({ n, partLabel: PART_LABEL[it.part], ...v });
      }
    }
    out.push(...drillRows().filter((r) => r.verdict === 'wrong' || r.my?.unsure));
    return send(res, 200, { items: out, titles: ruleTitles() });
  }

  if (p === '/api/drill' && req.method === 'GET') return send(res, 200, drillOverview());

  if (p === '/api/drill/answer' && req.method === 'POST') {
    const body = await readBody(req);
    const it = store.loadBank().find((x) => x.id === body.id);
    if (!it) return send(res, 404, { error: '题库里没有这道题' });
    const prev = store.loadDrill().find((a) => a.id === it.id);
    if (prev) return send(res, 200, { result: drillView(it, prev), ...drillOverview() }); // 每道题只记第一次
    const max = (it.type === 'stress' ? it.syllables : it.options).length;
    const c = body.choice;
    if (!(c === null || (Number.isInteger(c) && c >= 1 && c <= max))) return send(res, 400, { error: '选项不对' });
    const a = {
      id: it.id, choice: c, unsure: c !== null && !!body.unsure, via: 'web', at: new Date().toISOString(),
      after: Math.max(0, ...sessionNumbers()), // 逻辑时钟：做这道题时，最新出的一次练习是第几次
    };
    store.appendDrill(a);
    return send(res, 200, { result: drillView(it, a), ...drillOverview() });
  }

  let m;
  if ((m = p.match(/^\/api\/session\/(\d+)$/)) && req.method === 'GET') {
    const s = loadSession(Number(m[1]));
    return s ? send(res, 200, sessionView(s)) : send(res, 404, { error: '没有这一次练习' });
  }

  if ((m = p.match(/^\/api\/session\/(\d+)\/submit$/)) && req.method === 'POST') {
    const n = Number(m[1]);
    const s = loadSession(n);
    if (!s) return send(res, 404, { error: '没有这一次练习' });
    const body = await readBody(req);
    const part = body.part;
    const items = partItems(s, part);
    if (!PARTS.includes(part) || !items.length) return send(res, 400, { error: '没有这一部分' });
    if (s.review?.done) return send(res, 409, { error: '这次练习教练已经复核过，不能再提交' });
    if (s.submitted[part]) return send(res, 409, { error: '这一部分已经提交过了' });
    const gate = gateOf(s);
    if (part === 'practice' && (gate === 'pending' || gate === 'hold')) return send(res, 409, { error: '先完成复检' });
    const now = new Date().toISOString();
    const answers = { ...s.answers };
    for (const it of items) {
      const a = body.answers?.[it.id];
      if (!a || !('choice' in a)) return send(res, 400, { error: `第 ${it.id} 题还没作答` });
      const max = (it.type === 'stress' ? it.syllables : it.options).length;
      const ok = a.choice === null || (Number.isInteger(a.choice) && a.choice >= 1 && a.choice <= max);
      if (!ok) return send(res, 400, { error: `第 ${it.id} 题的选项不对` });
      answers[it.id] = { choice: a.choice, unsure: !!a.unsure, via: 'web', at: now };
    }
    saveAnswers(n, answers, { ...s.submitted, [part]: now });
    return send(res, 200, sessionView(loadSession(n)));
  }

  if ((m = p.match(/^\/api\/session\/(\d+)\/audio\/([\w-]+)$/))) {
    const s = loadSession(Number(m[1]));
    const it = s?.items.find((x) => x.id === m[2]);
    if (!it || !it.ipa) return send(res, 404, { error: '没有这道题的发音' });
    if (!it.promptAudio && !s.submitted[it.part]) return send(res, 403, { error: '作答前不能听这道题' });
    return send(res, 200, await tts(it.ipa, null, url.searchParams.get('slow') === '1'), 'audio/wav');
  }

  if ((m = p.match(/^\/api\/drill\/audio\/([\w-]+)$/))) {
    const it = store.loadBank().find((x) => x.id === m[1]);
    if (!it || !it.ipa) return send(res, 404, { error: '没有这道题的发音' });
    if (!it.promptAudio && !store.loadDrill().some((a) => a.id === it.id)) return send(res, 403, { error: '作答前不能听这道题' });
    return send(res, 200, await tts(it.ipa, null, url.searchParams.get('slow') === '1'), 'audio/wav');
  }

  if (p === '/api/tts') {
    const ipa = (url.searchParams.get('ipa') || '').trim();
    const stress = Number(url.searchParams.get('stress')) || null;
    if (!ipa || ipa.length > 120) return send(res, 400, { error: '没有音标' });
    try {
      return send(res, 200, await tts(ipa, stress, url.searchParams.get('slow') === '1'), 'audio/wav');
    } catch (e) {
      return send(res, 400, { error: String(e.message || e) });
    }
  }

  if (p === '/api/word') {
    const w = (url.searchParams.get('w') || '').trim().toLowerCase();
    if (!/^[a-z][a-z' -]{0,40}$/.test(w)) return send(res, 400, { error: '请输入一个英文单词' });
    return send(res, 200, { ...(await lookupWord(w)), seen: seenWord(w) });
  }

  send(res, 404, { error: 'not found' });
}

// 启动时跑一遍校验，题目写错了早点发现
function lint() {
  const { errors, warns } = core.checkAll(store);
  for (const w of warns) console.warn('WARN  ' + w);
  for (const e of errors) console.warn('ERROR ' + e);
}

http.createServer((req, res) => {
  handle(req, res).catch((e) => send(res, 500, { error: String(e.message || e) }));
}).listen(PORT, '127.0.0.1', () => {
  lint();
  console.log(`phonics: http://localhost:${PORT}  (root: ${ROOT})`);
});
