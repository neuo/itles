// 自然拼读发音工具（本地用）。无第三方依赖：node server.js
// - /                 页面
// - /api/word?w=xxx   查词：返回美音真人录音地址（来自 Free Dictionary API / Wikimedia Commons）
// - /api/session      最近一次练习（sessions/NNN.md）表格里的题目词

const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const PORT = Number(process.env.PORT) || 4310;
const ROOT = __dirname;
const SESSIONS = path.join(ROOT, '..', 'sessions');
const cache = new Map();

function send(res, code, body, type = 'application/json; charset=utf-8') {
  res.writeHead(code, { 'Content-Type': type, 'Cache-Control': 'no-store' });
  res.end(typeof body === 'string' ? body : JSON.stringify(body));
}

async function lookup(word) {
  if (cache.has(word)) return cache.get(word);
  const out = { word, us: null, uk: null, source: null, license: null, found: false };
  try {
    const r = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`);
    if (r.ok) {
      const data = await r.json();
      out.found = true;
      for (const entry of data) {
        for (const p of entry.phonetics || []) {
          if (!p.audio) continue;
          if (/-us\.mp3$/.test(p.audio) && !out.us) {
            out.us = p.audio;
            out.source = p.sourceUrl || null;
            out.license = p.license?.name || null;
          } else if (/-uk\.mp3$/.test(p.audio) && !out.uk) {
            out.uk = p.audio;
          }
        }
      }
    }
  } catch (e) {
    out.error = String(e.message || e);
  }
  if (!out.error) cache.set(word, out);
  return out;
}

function latestSession() {
  if (!fs.existsSync(SESSIONS)) return { session: null, words: [] };
  const files = fs.readdirSync(SESSIONS).filter((f) => /^\d{3}\.md$/.test(f)).sort();
  if (!files.length) return { session: null, words: [] };
  const file = files[files.length - 1];
  const text = fs.readFileSync(path.join(SESSIONS, file), 'utf8');
  const words = [];
  // 表格行：| 1 | technology (4) | ...
  for (const m of text.matchAll(/^\|\s*\d+\s*\|\s*([A-Za-z][A-Za-z' -]*?)\s*(?:（[^）]*）)?\s*(?:\(\d+\))?\s*\|/gm)) {
    const w = m[1].trim().toLowerCase();
    if (w && !words.includes(w)) words.push(w);
  }
  return { session: file.replace('.md', ''), words };
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  if (url.pathname === '/' || url.pathname === '/index.html') {
    return send(res, 200, fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8'), 'text/html; charset=utf-8');
  }
  if (url.pathname === '/api/word') {
    const w = (url.searchParams.get('w') || '').trim().toLowerCase();
    if (!/^[a-z][a-z' -]{0,40}$/.test(w)) return send(res, 400, { error: 'bad word' });
    return send(res, 200, await lookup(w));
  }
  if (url.pathname === '/api/session') {
    return send(res, 200, latestSession());
  }
  send(res, 404, { error: 'not found' });
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`phonics audio: http://localhost:${PORT}`);
});
