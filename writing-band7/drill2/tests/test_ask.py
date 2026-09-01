#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""题型（整句／词组／作文验）的回归测试 —— 全部跑临时副本，⛔ 一次都不碰真档案。

跑法：  python3 writing-band7/drill2/tests/test_ask.py
用途：  改过 drill.py 的状态行解析 / check / count / pick 之后先跑这个。
        SKILL §0.6 已把 tests/ 登记为「测试台，不是工作脚本」。

覆盖：  A 题型格解析与默认值（不写 ＝ 整句、三类相加 ＝ 全档总数）
        B 非法值 · ASK_FROM 前后的缺格口径
        C 词组的三条硬闸（词表型禁标 · 八个句子层族禁标 · 题面带句号 WARN）
        D 作文验：状态行是机器真源、散文是理由、过渡期并集、pick 排除
        E count 的 ask-* slug
        F pick 卡片认得词组（题型行 ＋ 零提示档）
        G append 不会被第 7 格弄坏
"""
import io, os, re, shutil, sys, tempfile, contextlib
from collections import Counter

WT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # = writing-band7/drill2/
sys.path.insert(0, WT)
import drill

PASS, FAIL = [], []
def ck(name, cond, note=""):
    (PASS if cond else FAIL).append(name)
    print(("  ✅ " if cond else "  ❌ ") + name + (("  — " + str(note)) if note and not cond else ""))

class Args:
    def __init__(self, **kw):
        for k, v in dict(dry_run=False, changed=False, all=True, quiet=True,
                         type=None, detail=False, fam=None, state=None, pool=False,
                         size=10, groups=None, full=False, date=None, dry=False,
                         brief=False, file=None).items():
            setattr(self, k, v)
        for k, v in kw.items(): setattr(self, k, v)

@contextlib.contextmanager
def sandbox(p_text=None):
    d = tempfile.mkdtemp(prefix="ask")
    for f in ("problems.md", "graduated.md", "review_pool.md", "log.md"):
        shutil.copy(os.path.join(WT, f), os.path.join(d, f))
    if p_text is not None:
        open(os.path.join(d, "problems.md"), "w", encoding="utf-8").write(p_text)
    old = (drill.ROOT, drill.PROBLEMS, drill.GRADUATED, drill.REVIEW_POOL, drill.LOG, drill.DRAWN)
    drill.ROOT = d
    drill.PROBLEMS = os.path.join(d, "problems.md")
    drill.GRADUATED = os.path.join(d, "graduated.md")
    drill.REVIEW_POOL = os.path.join(d, "review_pool.md")
    drill.LOG = os.path.join(d, "log.md")
    drill.DRAWN = os.path.join(d, "drawn_review.log")
    try:
        yield d
    finally:
        (drill.ROOT, drill.PROBLEMS, drill.GRADUATED, drill.REVIEW_POOL,
         drill.LOG, drill.DRAWN) = old
        shutil.rmtree(d, ignore_errors=True)

def run(fn, *a, **kw):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = fn(*a, **kw)
    return rc, buf.getvalue()

P = open(os.path.join(WT, "problems.md"), encoding="utf-8").read()

def set_grid(text, num, grid):
    """给某条的状态行换 / 加题型格。grid=None ⇒ 去掉题型格。"""
    lines = text.split("\n")
    for i, l in enumerate(lines):
        if l.startswith("## " + num + " ") or l == "## " + num:
            j = i + 1
            base = re.sub(r"\s*｜\s*题型\s*\S+", "", lines[j]).rstrip()
            lines[j] = base + (f" ｜ 题型 {grid}" if grid else "")
            return "\n".join(lines)
    raise SystemExit("找不到 " + num)

def set_trigger_line(text, num, add):
    """在某条的「中文触发点」节第一行前插一行"""
    lines = text.split("\n")
    at = None
    for i, l in enumerate(lines):
        if l.startswith("## " + num + " "): at = i
        elif at is not None and l == "**中文触发点**":
            lines.insert(i + 1, add); return "\n".join(lines)
    raise SystemExit("找不到触发点 " + num)

def probs(num):
    ents = drill.load_all(); nums = {e.num for e in ents}
    e = [x for x in ents if x.num == num][0]
    return e, drill.check_entry(e, set(), nums)

def lv(pr, level):
    return [m for l, m in pr if l == level]

# ══════════════════════════════════════════════════════════════════════
print("\n【A】题型格的解析与默认值")
with sandbox() as d:
    ents = drill.load_all()
    ck("不写题型格 ⇒ ask_kind = 整句",
       all(e.ask_kind == drill.ASK_SENTENCE for e in ents if e.ask is None))
    ck("全档三类相加 = 全档总数",
       sum(1 for e in ents if e.ask_kind == "整句") +
       sum(1 for e in ents if e.ask_kind == "词组") +
       sum(1 for e in ents if e.ask_kind == "作文验") == len(ents))
    ck("回标后 44 条题型 = 作文验",
       sum(1 for e in ents if e.ask == "作文验") == 44)
    ck("essay_only 仍是 45 条（含并入的 #0218 靠散文认出来）",
       sum(1 for e in ents if e.essay_only) == 45)

for grid in ("整句", "词组", "作文验"):
    with sandbox(p_text=set_grid(P, "#0053", grid)) as d:
        e, _ = probs("#0053")
        ck(f"显式写「题型 {grid}」解析得到 {grid}", e.ask == grid and e.ask_kind == grid, e.ask)

print("\n【B】非法值与缺格")
with sandbox(p_text=set_grid(P, "#0005", "句子")) as d:
    _, pr = probs("#0005")
    ck("题型写成非法值 ⇒ ERROR", any("题型「句子」非法" in m for m in lv(pr, "ERROR")), pr)
with sandbox() as d:
    e, pr = probs("#0005")
    ck(f"{drill.ASK_FROM} 之前建的条目缺题型格 ⇒ 不报错",
       not any("缺「题型」格" in m for m in lv(pr, "ERROR")), pr)
# 造一条「ASK_FROM 之后建的」：把某条**第一条**历史行的日期改掉
def make_late(text, num):
    lines = text.split("\n")
    at = None
    for i, l in enumerate(lines):
        if l.startswith("## " + num + " "): at = i; continue
        if at is not None and re.match(r"^-\s*20\d\d-\d\d-\d\d", l.strip()):
            lines[i] = re.sub(r"20\d\d-\d\d-\d\d", "2026-09-30", l, count=1)
            return "\n".join(lines)
    raise SystemExit("没找到历史行 " + num)
_LATE_NUM = "#0005"
_late = make_late(P, _LATE_NUM)
with sandbox(p_text=_late) as d:
    e, pr = probs(_LATE_NUM)
    ck("构造出一条 ASK_FROM 之后新建的条目",
       e.created_on() >= drill.ASK_FROM and e.ask is None, e.created_on())
    ck("ASK_FROM 之后新建、缺题型格 ⇒ ERROR",
       any("缺「题型」格" in m for m in lv(pr, "ERROR")), lv(pr, "ERROR"))
with sandbox(p_text=set_grid(make_late(P, _LATE_NUM), _LATE_NUM, "整句")) as d:
    _, pr = probs(_LATE_NUM)
    ck("ASK_FROM 之后新建、写了题型格 ⇒ 不报错",
       not any("缺「题型」格" in m for m in lv(pr, "ERROR")), lv(pr, "ERROR"))

print("\n【C】词组的三条硬闸")
_ents_p = drill.parse_file(os.path.join(WT, "problems.md"), "problems.md")
_byfam = {}
for e in _ents_p:
    if e.state == "在池" and not e.members and not e.essay_prose:
        _byfam.setdefault(e.fam, e.num)
# C1 词表型（挂成员出题账）不许标词组 —— 挑一条住 problems.md 的在池词表型
_wl = next(e.num for e in _ents_p if e.members and e.state == "在池"
           and e.fam not in drill.NO_PHRASE_FAMS)
with sandbox(p_text=set_grid(P, _wl, "词组")) as d:
    e, pr = probs(_wl)
    ck(f"前提：{_wl} 挂着成员出题账", bool(e.members))
    ck("词表型标词组 ⇒ ERROR",
       any("词表型" in m for m in lv(pr, "ERROR")), lv(pr, "ERROR"))
# C2 句子层的族不许标词组
for fam in sorted(drill.NO_PHRASE_FAMS):
    if fam not in _byfam: continue
    num = _byfam[fam]
    with sandbox(p_text=set_grid(P, num, "词组")) as d:
        _, pr = probs(num)
        ck(f"{fam}（句子层）标词组 ⇒ ERROR  [{num}]",
           any("不许标词组" in m for m in lv(pr, "ERROR")), lv(pr, "ERROR"))
allowed = [f for f in drill.FAMILIES if f not in drill.NO_PHRASE_FAMS and f in _byfam]
for fam in allowed:
    num = _byfam[fam]
    with sandbox(p_text=set_grid(P, num, "词组")) as d:
        _, pr = probs(num)
        ck(f"{fam}（非句子层）标词组 ⇒ 不报 ERROR  [{num}]",
           not any("不许标词组" in m for m in lv(pr, "ERROR")), lv(pr, "ERROR"))
# C3 词组题面里有句号 ⇒ WARN
_num = _byfam[allowed[0]]
with sandbox(p_text=set_grid(P, _num, "词组")) as d:
    e, pr = probs(_num)
    has_period = "。" in e.trigger
    ck("词组 ＋ 触发点里有句号 ⇒ WARN",
       (not has_period) or any("是**块**不是句" in m for m in lv(pr, "WARN")),
       (has_period, lv(pr, "WARN")))

print("\n【D】作文验：状态行是真源，散文是理由")
with sandbox(p_text=set_grid(P, "#0005", "作文验")) as d:
    e, pr = probs("#0005")
    ck("标了作文验、散文里没理由行 ⇒ WARN",
       any("没有那句理由行" in m for m in lv(pr, "WARN")), lv(pr, "WARN"))
    ck("标了作文验 ⇒ essay_only 成立（不进复习组）", e.essay_only)
    rc, out = run(drill.cmd_pick, Args(type="review"))
    ck("pick 把它排除出候选池", "#0005" not in out.split("挂作文验")[1].split("候选池")[0]
       or "#0005" in out.split("⛔ 另有")[1][:400], out[:0])
with sandbox(p_text=set_grid(P, "#0053", None)) as d:   # 把已回标的 #0053 退回散文态
    e, pr = probs("#0053")
    ck("散文写着「不出单点题」、状态行没标 ⇒ 存量提示（INFO，不是 ERROR）",
       any("回标成" in m for m in lv(pr, "INFO")) and not lv(pr, "ERROR"),
       (lv(pr, "INFO"), lv(pr, "ERROR")))
    ck("过渡期 essay_only 仍然认散文", e.essay_only)

print("\n【E】count 的新 slug")
with sandbox() as d:
    ents = drill.load_all()
    for slug, want in (("ask-essay", 44), ("ask-phrase", 0)):
        rc, out = run(drill.cmd_count, Args(type=slug))
        ck(f"count --type {slug} 跑得动且数对",
           rc == 0 and f"全档 {want} 条" in out, out[:200])
    rc, out = run(drill.cmd_count, Args())
    ck("count 全表里有三个 ask-* slug",
       all(s in out for s in ("ask-sentence", "ask-phrase", "ask-essay", "ask-todo")))
    ck("ask-todo 现在是 0（44 条已回标，#0218 是并入不计）",
       sum(1 for e in ents if e.essay_prose and e.ask_kind != "作文验"
           and e.state in ("在池", "🎓")) == 0)

print("\n【F】pick 卡片认得词组")
_num = _byfam[allowed[0]]
with sandbox(p_text=set_grid(P, _num, "词组")) as d:
    rc, out = run(drill.cmd_pick, Args(type="review", full=False))
    ck("pick 头部报了词组条数", "条词组型" in out, out[:0])
    if _num in out:
        seg = out.split(_num, 1)[1][:400]
        ck(f"{_num} 的卡片打出「题型 **词组**」", "题型 **词组**" in seg, seg[:200])
        ck("词组条目的提示档写死零提示", "词组题给词 ＝ 给答案" in seg, seg[:200])
    else:
        ck(f"{_num} 出现在本次计划里", False, "没被抽到，换一条再测")

print("\n【G】append 不会被第 7 格弄坏")
with sandbox(p_text=set_grid(P, "#0005", "词组")) as d:
    e0, _ = probs("#0005")
    before = e0.status_raw
    rows = os.path.join(d, "rows.md")
    open(rows, "w", encoding="utf-8").write(
        "#0005 ✅ 测试组 第 1 题\n  测试用内容行。\n")
    rc, out = run(drill.cmd_append, Args(file=rows, date="2026-09-30"))
    ck("append 退出码 0", rc == 0, out[-400:])
    e1, pr = probs("#0005")
    ck("题型格没被 append 改掉", e1.ask == "词组", e1.status_raw)
    ck("连对/上次 照常重算", e1.last == "2026-09-30" and e1.ok == (e0.ok or 0) + 1,
       (e1.ok, e1.last))
    ck("状态行仍然是七格", e1.status_raw.count("｜") == 6, e1.status_raw)

print("\n" + "═" * 70)
print(f"题型回归测试 · 通过 {len(PASS)} · 失败 {len(FAIL)}")
for f in FAIL: print("  ❌ " + f)
sys.exit(1 if FAIL else 0)
