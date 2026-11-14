// 界面层。只读数据、提交作答；判定和记录以教练复核为准。

const view = document.getElementById('view');
const ICON = { ok: '✅', wrong: '❌', warn: '⚠️' };
let overview = null;
let rulesCache = null;

// ---------- 小工具 ----------

function h(tag, attrs, ...kids) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v === false || v == null) continue;
    if (k === 'onclick') e.onclick = v;
    else if (k === 'html') e.innerHTML = v;
    else e.setAttribute(k, v === true ? '' : v);
  }
  for (const kid of kids.flat(Infinity)) if (kid !== null && kid !== undefined && kid !== false) e.append(kid);
  return e;
}
async function api(path, opts) {
  const r = await fetch(path, opts);
  const j = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(j.error || '请求失败 ' + r.status);
  return j;
}
const store = {
  get(k, d) { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch { return d; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
  del(k) { try { localStorage.removeItem(k); } catch {} },
};
const showIpa = (ipa) => '/' + ipa.replace(/\./g, '') + '/';

// ---------- 发音 ----------

const player = new Audio();
function playUrl(url, rate = 1) {
  speechSynthesis.cancel();
  player.src = url;
  player.preservesPitch = true;
  player.playbackRate = rate;
  player.play().catch(() => {});
}
function ttsUrl(ipa, { stress, slow } = {}) {
  const q = new URLSearchParams({ ipa });
  if (stress) q.set('stress', stress);
  if (slow) q.set('slow', '1');
  return '/api/tts?' + q;
}
function speakText(word, rate = 1) {
  player.pause();
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(word);
  u.lang = 'en-US';
  const vs = speechSynthesis.getVoices().filter((v) => v.lang === 'en-US');
  const v = vs.find((x) => /Samantha/.test(x.name)) || vs[0];
  if (v) u.voice = v;
  u.rate = rate;
  speechSynthesis.speak(u);
}
// 真词：优先真人录音，没有就用系统合成音。假词：按音标合成。
async function playItem(it, slow) {
  if (it.pseudo) return playUrl(ttsUrl(it.ipa, { slow }));
  const d = await api('/api/word?w=' + encodeURIComponent(it.word.toLowerCase())).catch(() => ({}));
  if (d.us) playUrl(d.us, slow ? 0.6 : 1);
  else speakText(it.word, slow ? 0.6 : 1);
}

// ---------- 迷你 Markdown ----------

const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
function inline(s) {
  return esc(s).replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
}
function mdTable(rows) {
  const cells = (r) => r.replace(/^\||\|\s*$/g, '').split('|').map((c) => c.trim());
  const head = cells(rows[0]);
  const body = rows.slice(/^\|[\s:|-]+\|?\s*$/.test(rows[1] || '') ? 2 : 1).map(cells);
  const blankHead = head.every((c) => !c);
  return '<table>' + (blankHead ? '' : '<thead><tr>' + head.map((c) => `<th>${inline(c)}</th>`).join('') + '</tr></thead>') +
    '<tbody>' + body.map((r) => '<tr>' + r.map((c) => `<td>${inline(c)}</td>`).join('') + '</tr>').join('') + '</tbody></table>';
}
function md(text) {
  const lines = text.split('\n');
  const lists = [];
  let html = '';
  const closeLists = (to = -1) => {
    while (lists.length && lists[lists.length - 1].indent > to) html += '</li></' + lists.pop().type + '>';
  };
  for (let i = 0; i < lines.length;) {
    const line = lines[i];
    let m;
    if (/^\s*$/.test(line)) { closeLists(); i++; continue; }
    if ((m = line.match(/^(#{1,4})\s+(.*)$/))) {
      closeLists();
      const idm = m[2].match(/^([SP]\d+)\s*·/);
      html += `<h${m[1].length}${idm ? ` id="rule-${idm[1]}"` : ''}>${inline(m[2])}</h${m[1].length}>`;
      i++; continue;
    }
    if (/^---+\s*$/.test(line)) { closeLists(); html += '<hr>'; i++; continue; }
    if (line.startsWith('|')) {
      closeLists();
      const rows = [];
      while (i < lines.length && lines[i].startsWith('|')) rows.push(lines[i++]);
      html += mdTable(rows); continue;
    }
    if (line.startsWith('>')) {
      closeLists();
      const buf = [];
      while (i < lines.length && lines[i].startsWith('>')) buf.push(lines[i++].replace(/^>\s?/, ''));
      html += '<blockquote>' + buf.map(inline).join('<br>') + '</blockquote>'; continue;
    }
    if ((m = line.match(/^(\s*)([-*]|\d+\.)\s+(.*)$/))) {
      const indent = m[1].length;
      const type = /\d/.test(m[2]) ? 'ol' : 'ul';
      closeLists(indent);
      const top = lists[lists.length - 1];
      if (top && top.indent === indent) html += '</li><li>' + inline(m[3]);
      else { html += `<${type}><li>` + inline(m[3]); lists.push({ indent, type }); }
      i++; continue;
    }
    if (lists.length && /^\s+\S/.test(line)) { html += '<br>' + inline(line.trim()); i++; continue; }
    closeLists();
    const buf = [lines[i++]];
    while (i < lines.length && !/^\s*$/.test(lines[i]) && !/^(#{1,4}\s|\||>|---|\s*([-*]|\d+\.)\s)/.test(lines[i])) buf.push(lines[i++]);
    html += '<p>' + buf.map(inline).join('<br>') + '</p>';
  }
  closeLists();
  return html;
}
async function loadRules() {
  if (!rulesCache) rulesCache = await api('/api/rules');
  return rulesCache;
}
function ruleSection(markdown, id) {
  const lines = markdown.split('\n');
  const start = lines.findIndex((l) => l.startsWith(`### ${id} ·`));
  if (start < 0) return null;
  let end = lines.length;
  for (let i = start + 1; i < lines.length; i++) if (/^#{1,3}\s/.test(lines[i])) { end = i; break; }
  return lines.slice(start, end).join('\n');
}
const ruleTag = (id) => id ? h('button', { class: 'tag rule', title: overview?.titles?.[id] || '', onclick: () => { location.hash = '#/rules/' + id; } }, id) : null;

// ---------- 题目：作答 ----------

const optsOf = (it) => (it.type === 'stress' ? it.syllables : it.options);
const TYPE_HINT = { stress: '点重读的那个音节', read: '选读音', spell: '选拼写' };

function itemForm(it, no, draft, onChange) {
  const choices = h('div', { class: 'choices' });
  const dunno = h('button', { class: 'ghost mini' }, '不知道');
  const cb = h('input', { type: 'checkbox' });
  const paint = () => {
    const d = draft[it.id];
    [...choices.children].forEach((b, i) => b.classList.toggle('on', !!d && d.choice === i + 1));
    dunno.classList.toggle('on', !!d && d.choice === null);
    cb.checked = !!d?.unsure;
  };
  optsOf(it).forEach((txt, i) => {
    choices.append(h('button', {
      class: 'chip' + (it.type === 'stress' ? ' syl' : ''),
      onclick: () => { draft[it.id] = { choice: i + 1, unsure: !!draft[it.id]?.unsure }; paint(); onChange(); },
    }, txt));
  });
  dunno.onclick = () => { draft[it.id] = { choice: null, unsure: false }; paint(); onChange(); };
  cb.onchange = () => { if (draft[it.id]) { draft[it.id].unsure = cb.checked; onChange(); } else cb.checked = false; };
  paint();
  const head = h('div', { class: 'item-head' },
    h('span', { class: 'no' }, no + '.'),
    h('span', { class: 'word' }, it.prompt || it.word),
    it.pseudo && h('span', { class: 'tag' }, '假词'),
    it.promptAudio && h('button', { class: 'mini', onclick: () => playUrl(`/api/session/${it.session}/audio/${it.id}`) }, '▶ 听'),
    h('span', { class: 'muted small' }, TYPE_HINT[it.type] || ''));
  return h('div', { class: 'item' }, head, choices,
    h('div', { class: 'under' }, h('label', {}, cb, '没把握'), dunno));
}

function partForm(s, part, onDone) {
  const key = 'phonics-draft-' + s.n;
  const draft = store.get(key, {});
  const counter = h('span', { class: 'muted small' });
  const btn = h('button', { class: 'primary' }, '提交' + part.label);
  const msg = h('span', { class: 'err small' });
  const refresh = () => {
    const done = part.items.filter((it) => draft[it.id]).length;
    counter.textContent = `已答 ${done} / ${part.items.length}`;
    btn.disabled = done < part.items.length;
    store.set(key, draft);
  };
  btn.onclick = async () => {
    btn.disabled = true;
    const answers = {};
    for (const it of part.items) answers[it.id] = draft[it.id];
    try {
      await api(`/api/session/${s.n}/submit`, {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ part: part.key, answers }),
      });
      store.del(key);
      view.dataset.tab = '';
      onDone();
    } catch (e) { msg.textContent = e.message; btn.disabled = false; }
  };
  const box = h('section', {},
    h('h2', {}, `${part.label}（${part.items.length} 题）`),
    h('p', { class: 'muted small' }, '每个词先出声读一遍，再选。不查词典。'),
    part.items.map((it, i) => itemForm({ ...it, session: s.n }, i + 1, draft, refresh)),
    h('div', { class: 'row' }, btn, counter, msg));
  refresh();
  return box;
}

// ---------- 题目：结果 ----------

function itemResult(it, no, extraTags = []) {
  const opts = optsOf(it);
  const mine = it.my?.choice ?? null;
  const cells = opts.map((txt, i) => h('span', {
    class: i + 1 === it.answer ? 'good' : (i + 1 === mine ? 'bad' : ''),
  }, txt));
  const mineText = !it.my ? '（没有作答）' : mine === null ? '不知道' : opts[mine - 1];
  const audio = h('div', { class: 'row audio' },
    h('button', { class: 'mini', onclick: () => playItem(it) }, '▶ 听'),
    h('button', { class: 'mini', onclick: () => playItem(it, true) }, '▶ 慢速'));
  if (it.type === 'stress' && it.ipa && it.verdict === 'wrong' && mine) {
    audio.append(
      h('span', { class: 'muted small' }, '对比（合成音）：'),
      h('button', { class: 'mini', onclick: () => playUrl(ttsUrl(it.ipa, { stress: mine })) }, `▶ 你选的：重读 ${opts[mine - 1]}`),
      h('button', { class: 'mini', onclick: () => playUrl(ttsUrl(it.ipa)) }, `▶ 正确的：重读 ${opts[it.answer - 1]}`));
  }
  return h('div', { class: 'item ' + (it.verdict || '') },
    h('div', { class: 'item-head' },
      h('span', {}, ICON[it.verdict] || ''),
      no && h('span', { class: 'no' }, no + '.'),
      h('span', { class: 'word' }, it.prompt || it.word),
      it.pseudo && h('span', { class: 'tag' }, '假词'),
      ruleTag(it.rule),
      it.my?.unsure && h('span', { class: 'tag warn' }, '没把握'),
      it.verdict && !it.final && h('span', { class: 'tag warn' }, '待教练复核'),
      extraTags),
    h('div', { class: 'syls' }, cells),
    h('div', { class: 'small muted' },
      `你选：${mineText}`,
      it.my?.raw ? `（对话里写的「${it.my.raw}」）` : '',
      ` · 正确：${opts[it.answer - 1]}`,
      it.ipa ? h('span', { class: 'ipa' }, '　' + showIpa(it.ipa)) : ''),
    it.explain && h('div', { class: 'explain' }, it.explain),
    it.note && h('div', { class: 'coach' }, '教练：' + it.note),
    audio);
}
function partResult(part) {
  const ok = part.items.filter((it) => it.verdict !== 'wrong').length;
  return h('section', {},
    h('h2', {}, `${part.label}：${ok} / ${part.items.length}`),
    part.items.map((it, i) => itemResult(it, i + 1)));
}

// ---------- 规则池 ----------

function poolPanel() {
  const p = overview.pool;
  const ladder = p.ladder || [1, 2, 4, 8];
  const rows = (p.rules || []).map((r) => h('tr', {},
    h('td', {}, ruleTag(r.id), ' ', overview.titles[r.id] || ''),
    h('td', {}, h('span', { class: 'boxes' }, ladder.map((b) => h('i', { class: b <= r.box ? 'on' : '' }))), ` 第 ${r.box} 格`),
    h('td', {}, `第 ${r.nextDue} 次`),
    h('td', {}, (r.log || []).map((l) => `${l.kind === 'recheck' ? '复检' : '练习'}${l.ok ? '✅' : '❌'}`).join(' ') || '—')));
  return h('section', {},
    h('h2', {}, '规则池'),
    h('p', { class: 'muted small' }, `已练 ${p.session} 次。格子 ${ladder.join(' → ')} 是距离下次复检的最少次数；最后一格再对一次就毕业。`),
    rows.length
      ? h('table', {}, h('thead', {}, h('tr', {}, ['规则', '在第几格', '下次最早', '记录'].map((t) => h('th', {}, t)))), h('tbody', {}, rows))
      : h('p', { class: 'muted' }, '池里还没有规则。'),
    (p.graduated || []).length ? h('p', { class: 'small' }, '已毕业：' + p.graduated.map((g) => g.id).join('、')) : null);
}

// ---------- 页面：练习 ----------

function reviewBlock(s) {
  if (!s.review) return null;
  const list = (title, arr) => arr.length ? [h('h3', {}, title), h('ul', {}, arr.map((t) => h('li', {}, t)))] : [];
  return h('section', { class: 'card' },
    h('h2', { style: 'margin-top:0' }, '教练复核'),
    list('小结', s.review.summary),
    list('规则池的变化', s.review.pool),
    s.review.qa.length ? [h('h3', {}, '你问的问题'), s.review.qa.map((x) => h('p', {}, h('strong', {}, x.q), h('br'), x.a))] : null);
}

async function sessionBody(s, { live }) {
  const out = [];
  const rerender = () => render();
  const recheck = s.parts.find((p) => p.key === 'recheck');
  const practice = s.parts.find((p) => p.key === 'practice');

  if (recheck) out.push(recheck.submitted ? partResult(recheck) : partForm(s, recheck, rerender));

  if (s.gate === 'hold') {
    out.push(h('div', { class: 'banner warn' },
      '复检错了一半以上，这次先不讲新规则。回对话告诉教练：', h('strong', {}, `「第 ${s.n} 次复检做完了」`), '，教练会把错的规则重讲一遍。'));
  }

  const canGoOn = !recheck || (recheck.submitted && s.gate !== 'hold');
  if (canGoOn && s.newRule) {
    const { markdown } = await loadRules();
    const sec = ruleSection(markdown, s.newRule);
    const readKey = `phonics-read-${s.n}`;
    const seen = !live || practice?.submitted || store.get(readKey, false);
    out.push(h('section', {},
      h('h2', {}, '新规则'),
      h('div', { class: 'card md', html: sec ? md(sec) : `<p class="muted">rules.md 里还没有 ${s.newRule} 的正文。</p>` }),
      !seen && h('div', { class: 'row' },
        h('button', { class: 'primary', onclick: () => { store.set(readKey, true); rerender(); } }, '看完了，开始练习'),
        h('span', { class: 'muted small' }, '有疑问可以先回对话问教练。'))));
    if (!seen) return out;
  }

  if (canGoOn && practice && !practice.locked) {
    out.push(practice.submitted ? partResult(practice) : partForm(s, practice, rerender));
  }
  return out;
}

async function viewPractice() {
  const out = [];
  const waiting = overview.waiting;
  const target = overview.open ?? waiting[waiting.length - 1] ?? null;
  for (const n of waiting) {
    out.push(h('div', { class: 'banner good' },
      `第 ${n} 次已经做完，等教练复核。回对话说一句：`, h('strong', {}, `「第 ${n} 次做完了」`),
      n !== target ? [' ', h('a', { href: `#/log/${n}` }, '看我的作答')] : null));
  }
  if (target === null) {
    out.push(h('div', { class: 'card' },
      h('h1', {}, '现在没有待做的练习'),
      h('p', { class: 'muted' }, '回对话说「开始下一次」，教练出好题，这里就会出现。也可以直接在对话里作答，结果一样会记到这里。')));
    out.push(poolPanel());
    return out;
  }
  const s = await api('/api/session/' + target);
  out.push(h('h1', {}, `第 ${s.n} 次`), s.note && h('p', { class: 'muted' }, s.note));
  out.push(...await sessionBody(s, { live: true }));
  out.push(poolPanel());
  return out;
}

// ---------- 页面：规则 ----------

async function viewRules(arg) {
  const { markdown, titles } = await loadRules();
  const jump = h('div', { class: 'row' }, Object.keys(titles).map((id) =>
    h('button', { class: 'mini', onclick: () => { location.hash = '#/rules/' + id; } }, `${id} ${titles[id]}`)));
  const body = h('div', { class: 'md', html: md(markdown) });
  if (arg) setTimeout(() => document.getElementById('rule-' + arg)?.scrollIntoView({ behavior: 'smooth' }), 30);
  return [jump, body];
}

// ---------- 页面：错题 ----------

async function viewMistakes() {
  const { items, titles } = await api('/api/mistakes');
  const wrong = items.filter((it) => it.verdict === 'wrong');
  const unsure = items.filter((it) => it.verdict !== 'wrong');
  if (!items.length) return [h('h1', {}, '错题'), h('p', { class: 'muted' }, '还没有错题。')];
  const out = [h('h1', {}, '错题'), h('p', { class: 'muted small' }, '按规则分组。进池复检的是规则，不是这些词；这里用来回看当时错在哪。')];
  const byRule = {};
  for (const it of wrong) (byRule[it.rule || '其他'] ||= []).push(it);
  for (const [rule, list] of Object.entries(byRule)) {
    out.push(h('h2', {}, `${rule} ${titles[rule] || ''}（${list.length}）`));
    out.push(...list.map((it) => itemResult(it, null, [h('span', { class: 'tag' }, `第 ${it.n} 次 · ${it.partLabel}`)])));
  }
  if (unsure.length) {
    out.push(h('h2', {}, `答对但没把握（${unsure.length}）`));
    out.push(...unsure.map((it) => itemResult(it, null, [h('span', { class: 'tag' }, `第 ${it.n} 次 · ${it.partLabel}`)])));
  }
  return out;
}

// ---------- 页面：发音 ----------

const PALETTE = [
  ['ɪ', 'e', 'æ', 'ʌ', 'ʊ', 'ə'], ['iː', 'uː', 'ɑː', 'ɔː', 'ɜː'], ['eɪ', 'aɪ', 'ɔɪ', 'aʊ', 'əʊ'],
  ['ɑːr', 'ɔːr', 'ɜːr', 'ər', 'ɪr', 'er', 'ʊr', 'aɪər'], ['ʃ', 'tʃ', 'dʒ', 'θ', 'ð', 'ŋ', 'ʒ'], ['ˈ', 'ˌ', '.'],
];
async function viewAudio() {
  // 查词
  const input = h('input', { type: 'text', placeholder: '输入一个英文单词', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false' });
  const result = h('div');
  const lookup = async () => {
    const w = input.value.trim().toLowerCase();
    if (!w) return;
    result.replaceChildren(h('p', { class: 'muted' }, '查询中…'));
    try {
      const d = await api('/api/word?w=' + encodeURIComponent(w));
      const card = h('div', { class: 'card' }, h('div', { class: 'word' }, w));
      card.append(h('div', { class: 'row audio' },
        d.us
          ? [h('span', { class: 'small muted' }, '真人录音'), h('button', { class: 'mini primary', onclick: () => playUrl(d.us) }, '▶ 正常'), h('button', { class: 'mini', onclick: () => playUrl(d.us, 0.6) }, '▶ 慢速')]
          : h('span', { class: 'small muted' }, '这个词没有美音真人录音'),
        h('span', { class: 'small muted' }, '合成音'),
        h('button', { class: 'mini' + (d.us ? '' : ' primary'), onclick: () => speakText(w) }, '▶ 正常'),
        h('button', { class: 'mini', onclick: () => speakText(w, 0.6) }, '▶ 慢速')));
      card.append(h('p', { class: 'small' }, h('a', { href: 'https://www.oxfordlearnersdictionaries.com/search/english/?q=' + encodeURIComponent(w), target: '_blank', rel: 'noopener' }, '在 Oxford 打开（看音标，点 US 喇叭）')));
      card.append(h('p', { class: 'small muted' }, '合成音是电脑读的，重音一般对，偶尔会错；以真人录音和 Oxford 为准。'));
      const pseudo = d.seen.some((it) => it.pseudo);
      if (pseudo) card.append(h('div', { class: 'banner warn' }, '这是练习里的假词。上面的合成音是电脑乱猜的，别信；按下面练习记录里的「▶ 听」，那个是按音标读的。'));
      result.replaceChildren(card);
      if (d.us) playUrl(d.us); else if (!pseudo) speakText(w);
      if (d.seen.length) {
        result.append(h('h3', {}, '练习里出现过'), ...d.seen.map((it) => itemResult(it, null, [h('span', { class: 'tag' }, `第 ${it.n} 次 · ${it.partLabel}`)])));
      }
    } catch (e) { result.replaceChildren(h('p', { class: 'err' }, e.message)); }
  };
  input.onkeydown = (e) => { if (e.key === 'Enter') lookup(); };

  // 按音标读
  const ipa = h('input', { type: 'text', class: 'ipa', placeholder: '例：fə.ˈtɑː.ɡrə.fi', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', style: 'flex:1' });
  const msg = h('span', { class: 'err small' });
  const say = async (slow) => {
    msg.textContent = '';
    const v = ipa.value.trim();
    if (!v) return;
    const r = await fetch(ttsUrl(v, { slow }));
    if (!r.ok) { msg.textContent = (await r.json().catch(() => ({}))).error || '读不了'; return; }
    playUrl(URL.createObjectURL(await r.blob()));
  };
  const palette = h('div', { class: 'palette' }, PALETTE.map((group) => [
    group.map((sym) => h('button', { class: 'ipa', onclick: () => { ipa.value += sym; ipa.focus(); } }, sym)), h('span', { class: 'sep' })]));

  return [
    h('h1', {}, '查词 · 听真词'),
    h('div', { class: 'row' }, input, h('button', { class: 'primary', onclick: lookup }, '听')),
    result,
    h('h2', {}, '按音标读（假词也能读）'),
    overview.tts ? null : h('div', { class: 'banner warn' }, '这台电脑没装 espeak-ng，按音标读用不了。'),
    h('p', { class: 'muted small' }, '音节之间用 . 隔开，重读音节前加 ˈ。点下面的符号可以直接输入，普通辅音用键盘打。声音是机器合成的，偏机械，但每个音和重音位置是准的。'),
    h('div', { class: 'row' }, ipa,
      h('button', { class: 'primary', onclick: () => say(false) }, '▶ 读'),
      h('button', { onclick: () => say(true) }, '▶ 慢速'),
      h('button', { class: 'ghost', onclick: () => { ipa.value = ''; msg.textContent = ''; } }, '清空')),
    msg, palette,
  ];
}

// ---------- 页面：记录 ----------

const STATUS = { open: '待做', answered: '等教练复核', reviewed: '已复核' };
async function viewLog(arg) {
  if (arg) {
    const s = await api('/api/session/' + Number(arg));
    return [
      h('p', {}, h('a', { href: '#/log' }, '← 所有记录')),
      h('h1', {}, `第 ${s.n} 次`, ' ', h('span', { class: 'tag' }, STATUS[s.status])),
      h('p', { class: 'muted' }, [s.date, s.note].filter(Boolean).join(' · ')),
      reviewBlock(s),
      ...await sessionBody({ ...s, parts: s.parts.filter((p) => p.submitted) }, { live: false }),
    ];
  }
  const rows = [...overview.sessions].reverse().map((s) => h('tr', {},
    h('td', {}, h('a', { href: `#/log/${s.n}` }, `第 ${s.n} 次`)),
    h('td', {}, s.date || '—'),
    h('td', {}, s.newRule ? [ruleTag(s.newRule), ' ', overview.titles[s.newRule] || ''] : '—'),
    h('td', {}, s.counts.total ? `✅ ${s.counts.ok + s.counts.warn}  ❌ ${s.counts.wrong}` : '—'),
    h('td', {}, STATUS[s.status])));
  return [h('h1', {}, '练习记录'),
    h('table', {}, h('thead', {}, h('tr', {}, ['', '日期', '新规则', '结果', '状态'].map((t) => h('th', {}, t)))), h('tbody', {}, rows))];
}

// ---------- 路由 ----------

const VIEWS = { practice: viewPractice, rules: viewRules, mistakes: viewMistakes, audio: viewAudio, log: viewLog };
let renderSeq = 0;
async function render() {
  const [, tab = 'practice', arg] = location.hash.split('/');
  const name = VIEWS[tab] ? tab : 'practice';
  document.querySelectorAll('#tabs a').forEach((a) => a.classList.toggle('on', a.dataset.tab === name));
  const seq = ++renderSeq;
  const keepScroll = view.dataset.tab === name + (arg || '') ? window.scrollY : 0;
  try {
    overview = await api('/api/overview');
    const nodes = await VIEWS[name](arg);
    if (seq !== renderSeq) return;
    view.replaceChildren(...nodes.flat(Infinity).filter(Boolean));
    view.dataset.tab = name + (arg || '');
    if (!(name === 'rules' && arg)) window.scrollTo(0, keepScroll);
  } catch (e) {
    if (seq === renderSeq) view.replaceChildren(h('p', { class: 'err' }, '出错了：' + e.message));
  }
}
window.addEventListener('hashchange', render);
speechSynthesis.getVoices();
render();
