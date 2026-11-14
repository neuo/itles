// 自然拼读练习工具（本地用，无第三方依赖）
//   node phonics/app/server.js [--port 4310] [--data <数据目录>]
//
// 网页只是界面。数据都在 phonics/data/ 和 phonics/rules.md：
//   data/sessions/NNN.json  教练写：题目 + 复核（review）
//   data/answers/NNN.json   她的作答。网页提交时写；她在对话里作答时由教练写（via: "chat"）
//   data/pool.json          教练写：规则池
//   rules.md                教练写：规则正文
// 网页**只写** data/answers/。程序给的对错是临时的，以教练的复核为准。

const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const { execFile } = require('node:child_process');
const { toEspeak, syllableCount } = require('./lib/ipa.js');

function arg(name, def) {
  const i = process.argv.indexOf('--' + name);
  return i > -1 && process.argv[i + 1] ? process.argv[i + 1] : def;
}
const PORT = Number(arg('port', process.env.PORT || 4310));
const APP = __dirname;
const ROOT = path.join(APP, '..');
const DATA = path.resolve(arg('data', path.join(ROOT, 'data')));
const RULES = path.join(ROOT, 'rules.md');
const PUBLIC = path.join(APP, 'public');
const PART_LABEL = { recheck: '复检', practice: '练习' };
const PARTS = ['recheck', 'practice'];

// ---------- 数据读写 ----------

const pad = (n) => String(n).padStart(3, '0');
const readJson = (p, def) => (fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, 'utf8')) : def);

function sessionNumbers() {
  const dir = path.join(DATA, 'sessions');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter((f) => /^\d{3}\.json$/.test(f)).sort().map((f) => Number(f.slice(0, 3)));
}
function loadSession(n) {
  const s = readJson(path.join(DATA, 'sessions', pad(n) + '.json'), null);
  if (!s) return null;
  const a = readJson(path.join(DATA, 'answers', pad(n) + '.json'), { n, answers: {}, submitted: {} });
  return { ...s, answers: a.answers || {}, submitted: a.submitted || {} };
}
function saveAnswers(n, answers, submitted) {
  const dir = path.join(DATA, 'answers');
  fs.mkdirSync(dir, { recursive: true });
  const file = path.join(dir, pad(n) + '.json');
  const tmp = file + '.tmp';
  // 保留文件里其他字段（如教练记下的对话原话 chatRaw）
  fs.writeFileSync(tmp, JSON.stringify({ ...readJson(file, {}), n, answers, submitted }, null, 2) + '\n');
  fs.renameSync(tmp, file);
}
function ruleTitles() {
  const out = {};
  if (!fs.existsSync(RULES)) return out;
  for (const m of fs.readFileSync(RULES, 'utf8').matchAll(/^### ([SP]\d+) · (.+?)(?:（[^）]*）)?\s*$/gm)) out[m[1]] = m[2];
  return out;
}

// ---------- 判定 ----------

function verdictOf(item, ans, review) {
  const r = review?.items?.[item.id];
  if (r?.verdict) return { verdict: r.verdict, note: r.note || null, final: true };
  if (!ans) return null;
  return {
    verdict: ans.choice === item.answer ? 'ok' : 'wrong',
    note: r?.note || null,
    final: !!review?.done,
  };
}
const partItems = (s, part) => s.items.filter((it) => it.part === part);

function gateOf(s) {
  const items = partItems(s, 'recheck');
  if (!items.length) return 'none';
  if (!s.submitted.recheck) return 'pending';
  const wrong = items.filter((it) => verdictOf(it, s.answers[it.id], s.review)?.verdict === 'wrong').length;
  return wrong * 2 > items.length ? 'hold' : 'pass';
}
function statusOf(s) {
  if (s.review?.done) return 'reviewed';
  const gate = gateOf(s);
  if (gate === 'hold') return 'answered';
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

function itemView(s, it, open) {
  const base = {
    id: it.id, part: it.part, type: it.type, word: it.word, pseudo: !!it.pseudo,
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
    status: statusOf(s), gate, parts, counts: countsOf(s),
    review: s.review?.done ? { summary: s.review.summary || [], pool: s.review.pool || [], qa: s.review.qa || [] } : null,
  };
}

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
async function lookupWord(word) {
  if (wordCache.has(word)) return wordCache.get(word);
  const out = { word, us: null, source: null, license: null };
  try {
    const r = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`);
    if (r.ok) {
      for (const entry of await r.json()) {
        for (const p of entry.phonetics || []) {
          if (p.audio && /-us\.mp3$/.test(p.audio) && !out.us) {
            out.us = p.audio;
            out.source = p.sourceUrl || null;
            out.license = p.license?.name || null;
          }
        }
      }
    }
    wordCache.set(word, out);
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
    const pool = readJson(path.join(DATA, 'pool.json'), { session: 0, ladder: [1, 2, 4, 8], rules: [], graduated: [] });
    const open = sessions.find((s) => s.status === 'open');
    const waiting = sessions.filter((s) => s.status === 'answered').map((s) => s.n);
    return send(res, 200, { pool, titles, sessions, open: open ? open.n : null, waiting, tts: await checkEspeak() });
  }

  if (p === '/api/rules') {
    return send(res, 200, { markdown: fs.existsSync(RULES) ? fs.readFileSync(RULES, 'utf8') : '', titles: ruleTitles() });
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
    return send(res, 200, { items: out, titles: ruleTitles() });
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

// 启动时检查题目文件，写错了早点发现
function lint() {
  for (const n of sessionNumbers()) {
    const s = loadSession(n);
    const ids = new Set();
    for (const it of s.items) {
      const where = `sessions/${pad(n)}.json ${it.id}`;
      if (ids.has(it.id)) console.warn(`[题目] ${where}: id 重复`);
      ids.add(it.id);
      const opts = it.type === 'stress' ? it.syllables : it.options;
      if (!Array.isArray(opts) || !Number.isInteger(it.answer) || it.answer < 1 || it.answer > opts.length) {
        console.warn(`[题目] ${where}: answer 不在选项范围内`);
      }
      if (it.ipa) {
        try {
          toEspeak(it.ipa);
          if (it.type === 'stress' && syllableCount(it.ipa) !== it.syllables.length) {
            console.warn(`[题目] ${where}: 音标的音节数和 syllables 对不上`);
          }
        } catch (e) {
          console.warn(`[题目] ${where}: 音标转不了（${e.message}）`);
        }
      }
    }
  }
}

http.createServer((req, res) => {
  handle(req, res).catch((e) => send(res, 500, { error: String(e.message || e) }));
}).listen(PORT, '127.0.0.1', () => {
  lint();
  console.log(`phonics: http://localhost:${PORT}  (data: ${DATA})`);
});
