#!/usr/bin/env node
// 自然拼读的机械工具。只读档、打印、做算术；不产生任何一个字的内容。
//   node phonics/app/cli.js status            现在到哪了、下一步该做什么
//   node phonics/app/cli.js answers N         第 N 次她的作答（复核用）
//   node phonics/app/cli.js drill             加练的作答：逐题「她选 / 正确」＋ 按规则汇总
//   node phonics/app/cli.js settle            按已复核的场次重算 data/pool.json（唯一会写文件的命令）
//   node phonics/app/cli.js check             全面校验，ERROR 必须为 0
// 都可以加 --root <目录>，指向另一份 phonics 目录（测试用）。

const path = require('node:path');
const core = require('./lib/core.js');

const args = process.argv.slice(2);
const rootAt = args.indexOf('--root');
const root = rootAt > -1 ? path.resolve(args.splice(rootAt, 2)[1]) : path.join(__dirname, '..');
const [cmd, arg] = args;
const store = core.createStore(root);
const { pad, PART_LABEL } = core;
const ICON = { ok: '✅', wrong: '❌', warn: '⚠️' };
const STATUS = { open: '已出题，等她作答', answered: '她做完了，待复核', reviewed: '已复核' };
const loadAll = () => store.sessionNumbers().map((n) => store.loadSession(n));

function poolTable(pool, titles) {
  if (!pool.rules.length && !pool.graduated.length) return '  （池是空的）';
  const lines = pool.rules.map((r) =>
    `  ${r.id.padEnd(4)} 第 ${r.box} 格 · 下次最早第 ${r.nextDue} 次 · 已复检 ${r.rechecks} 次 · ${titles[r.id] || ''}`);
  for (const g of pool.graduated) lines.push(`  ${g.id.padEnd(4)} 已毕业（第 ${g.graduatedAt} 次） · ${titles[g.id] || ''}`);
  return lines.join('\n');
}

const DRILL_LOW = 20; // 题库里没做的少于这个数就提醒补题
const mineOf = (r) => (r.attempt.choice === null ? '不知道' : core.optsOf(r.item)[r.attempt.choice - 1]);
const rightOf = (r) => core.optsOf(r.item)[r.item.answer - 1];
// 按规则数错题：{ S2: [行, 行] }
function wrongByRule(rows) {
  const out = {};
  for (const r of rows) if (!r.ok) (out[r.item.rule] ||= []).push(r);
  return out;
}
function drillSummary(d, since) {
  if (!d.total) return ['  （题库是空的）'];
  const lines = [`  题库 ${d.total} 题 · 已做 ${d.done} · ✅${d.ok} ❌${d.wrong} · 没做的还有 ${d.total - d.done}`];
  const per = Object.entries(d.byRule).filter(([, r]) => r.done).map(([id, r]) => `${id} ${r.ok}/${r.done}`);
  if (per.length) lines.push(`  按规则（对 / 做过）：${per.join(' · ')}`);
  const recent = d.rows.filter((r) => r.attempt.after === since);
  if (recent.length) {
    lines.push(`  第 ${since} 次出题之后做的：${recent.length} 题 · ❌${recent.filter((r) => !r.ok).length}`);
    for (const r of recent.filter((x) => !x.ok)) lines.push(`    ❌ ${r.item.word}（${r.item.rule}）她选 ${mineOf(r)}，正确 ${rightOf(r)}`);
    const shaky = recent.filter((r) => r.ok && r.attempt.unsure).map((r) => `${r.item.word}（${r.item.rule}）`);
    if (shaky.length) lines.push(`    对但没把握：${shaky.join('、')}`);
  } else lines.push(`  第 ${since} 次出题之后还没做过加练`);
  return lines;
}

function status() {
  const sessions = loadAll();
  const titles = store.ruleTitles();
  const order = store.syllabus().map((r) => r.id);
  const pool = core.replayPool(sessions);
  console.log(`已复核到第 ${pool.session} 次`);
  console.log('\n场次');
  for (const s of sessions) {
    const c = core.countsOf(s);
    const st = core.statusOf(s);
    const parts = core.PARTS.filter((p) => core.partItems(s, p).length)
      .map((p) => `${PART_LABEL[p]}${s.submitted[p] ? '已交' : '未交'}`).join(' · ');
    console.log(`  第 ${s.n} 次  ${STATUS[st]}  新规则 ${s.newRule || '—'}  ✅${c.ok + c.warn} ❌${c.wrong}${st === 'reviewed' ? '' : '  （' + parts + '）'}`);
  }
  console.log('\n规则池（按已复核的场次重放）');
  console.log(poolTable(pool, titles));

  const d = core.drillState(store);
  const lastN = Math.max(0, ...store.sessionNumbers());
  console.log('\n加练（不进规则池）');
  for (const l of drillSummary(d, lastN)) console.log(l);

  console.log('\n下一步');
  const last = sessions[sessions.length - 1];
  if (last && core.statusOf(last) !== 'reviewed') {
    const gate = core.gateOf(last);
    if (gate === 'hold') {
      const wrong = [...core.ruleResults(last, 'recheck')].filter(([, r]) => r.result === 'wrong').map(([id]) => id);
      console.log(`  第 ${last.n} 次复检错过半（闸门）。在对话里把 ${wrong.join(' ')} 重讲一遍，`);
      console.log(`  然后改 sessions/${pad(last.n)}.json：newRule 改 null，练习题换成这几条规则的题，加 "reteach": ${JSON.stringify(wrong)}`);
    } else if (core.statusOf(last) === 'answered') {
      console.log(`  第 ${last.n} 次她做完了 → 复核。先看作答：node phonics/app/cli.js answers ${last.n}`);
    } else {
      console.log(`  第 ${last.n} 次已经出好题，等她作答。⛔ 不要再出新题。`);
    }
    return;
  }
  const n = pool.session + 1;
  const { picked, overflow } = core.duePick(pool, n, order);
  console.log(`  该出第 ${n} 次：`);
  const counts = picked.map((id) => `${id}×${core.recheckCount(pool, id)}`);
  console.log(`    复检  ${picked.length ? counts.join(' ') + `（共 ${picked.reduce((k, id) => k + core.recheckCount(pool, id), 0)} 题，全用新词）` : '无（没有到期的规则）'}`);
  if (overflow.length) console.log(`    到期但这次排不下、顺延的：${overflow.join(' ')}`);
  const next = core.nextNewRule(store, sessions);
  const row = store.syllabus().find((r) => r.id === next);
  console.log(`    新规则  ${next ? `${next}（${titles[next] ? '正文已有' : 'rules.md 里还没有正文，先写'}）` : '课表讲完了'}`);
  if (row) console.log(`            课表原文：${row.text}`);
  const weak = Object.entries(wrongByRule(d.rows.filter((r) => r.attempt.after === lastN))).filter(([, rows]) => rows.length >= 2);
  if (weak.length) console.log(`    练习的旧规则题  加练里 ${weak.map(([id, rows]) => `${id} 错了 ${rows.length} 题`).join('、')} → 旧规则题优先出${weak.length > 1 ? '这几条' : '这条'}`);
  if (d.total - d.done < DRILL_LOW) console.log(`    加练题库  没做的只剩 ${d.total - d.done} 题 → 这次顺手补题（data/bank.json）`);
}

function drill() {
  const d = core.drillState(store);
  for (const l of drillSummary(d, Math.max(0, ...store.sessionNumbers()))) console.log(l);
  let after = null;
  for (const r of d.rows) {
    if (r.attempt.after !== after) { after = r.attempt.after; console.log(`\n第 ${after} 次出题之后`); }
    console.log(`  ${r.ok ? ICON.ok : ICON.wrong} ${r.item.id.padEnd(5)} ${String(r.item.word).padEnd(15)} ${String(r.item.rule).padEnd(4)}` +
      ` 她选 ${String(mineOf(r)).padEnd(6)} 正确 ${String(rightOf(r)).padEnd(6)}` +
      `${r.attempt.unsure ? ' 没把握' : ''}${r.attempt.raw ? ` 原话「${r.attempt.raw}」` : ''} [${r.attempt.via}]`);
  }
}

function answers(n) {
  const s = store.loadSession(Number(n));
  if (!s) { console.error(`没有第 ${n} 次`); process.exit(1); }
  console.log(`第 ${s.n} 次 · ${STATUS[core.statusOf(s)]} · 闸门 ${core.gateOf(s)}`);
  for (const part of core.PARTS) {
    const items = core.partItems(s, part);
    if (!items.length) continue;
    console.log(`\n${PART_LABEL[part]}${s.submitted[part] ? '' : '（未提交）'}`);
    for (const it of items) {
      const a = s.answers[it.id];
      const opts = core.optsOf(it);
      const v = core.verdictOf(it, a, s.review);
      const mine = !a ? '—' : a.choice === null ? '不知道' : opts[a.choice - 1];
      console.log(`  ${(v ? ICON[v.verdict] : '· ')} ${it.id.padEnd(4)} ${String(it.word).padEnd(15)} ${String(it.rule).padEnd(4)}` +
        ` 她选 ${String(mine).padEnd(6)} 正确 ${String(opts[it.answer - 1]).padEnd(6)}` +
        `${a?.unsure ? ' 没把握' : ''}${a?.raw ? ` 原话「${a.raw}」` : ''}${a ? ` [${a.via}]` : ''}`);
    }
    const res = [...core.ruleResults(s, part)].map(([id, r]) => `${id} ${{ ok: '全对', hold: '全对但有没把握', wrong: '有错' }[r.result]}`);
    if (res.length) console.log(`  按规则：${res.join(' · ')}`);
  }
}

function settle() {
  const before = store.readPool();
  const after = core.replayPool(loadAll());
  store.writePool(after);
  console.log(`pool.json 已重算（已复核到第 ${after.session} 次）${JSON.stringify(before) === JSON.stringify(after) ? '，没有变化' : ''}`);
  console.log(`第 ${after.session} 次带来的变化：`);
  const lines = core.poolDelta(loadAll(), after.session);
  for (const l of lines) console.log('  ' + l);
  if (!lines.length) console.log('  （无）');
}

function check() {
  const { errors, warns } = core.checkAll(store);
  for (const w of warns) console.log('WARN  ' + w);
  for (const e of errors) console.log('ERROR ' + e);
  console.log(`\ncheck：ERROR ${errors.length} · WARN ${warns.length}`);
  process.exit(errors.length ? 1 : 0);
}

const run = { status, answers: () => answers(arg), drill, settle, check }[cmd];
if (!run) {
  console.log('用法：node phonics/app/cli.js status | answers N | drill | settle | check  [--root 目录]');
  process.exit(1);
}
run();
