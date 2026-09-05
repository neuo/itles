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
                         brief=False, file=None, scope="both", queue="pool").items():
            setattr(self, k, v)
        for k, v in kw.items(): setattr(self, k, v)

@contextlib.contextmanager
def sandbox(p_text=None, g_text=None):
    d = tempfile.mkdtemp(prefix="ask")
    for f in ("problems.md", "graduated.md", "log.md"):
        shutil.copy(os.path.join(WT, f), os.path.join(d, f))
    if p_text is not None:
        open(os.path.join(d, "problems.md"), "w", encoding="utf-8").write(p_text)
    if g_text is not None:
        open(os.path.join(d, "graduated.md"), "w", encoding="utf-8").write(g_text)
    old = (drill.ROOT, drill.PROBLEMS, drill.GRADUATED, drill.LOG, drill.DRAWN)
    drill.ROOT = d
    drill.PROBLEMS = os.path.join(d, "problems.md")
    drill.GRADUATED = os.path.join(d, "graduated.md")
    drill.LOG = os.path.join(d, "log.md")
    drill.DRAWN = os.path.join(d, "drawn_review.log")
    try:
        yield d
    finally:
        (drill.ROOT, drill.PROBLEMS, drill.GRADUATED,
         drill.LOG, drill.DRAWN) = old
        shutil.rmtree(d, ignore_errors=True)

def run(fn, *a, **kw):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = fn(*a, **kw)
    return rc, buf.getvalue()

P = open(os.path.join(WT, "problems.md"), encoding="utf-8").read()
G = open(os.path.join(WT, "graduated.md"), encoding="utf-8").read()

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

# ★ 夹具不许写死编号 —— 档案会动（2026-09-01 那次 migrate 把 #0005 搬进了 graduated.md，
#   写死的夹具当场全崩）。改成**按条件从活档案里挑**，条件写在下面这一行里。
def _pick_fixture():
    """挑一条：住 problems.md · 在池 · 状态行没写题型格 · 有历史行且建号早于 ASK_FROM ·
    非词表型 · 非挂作文验 · 族不在 NO_PHRASE_FAMS（这样 G 段把它标成词组也不该报错）。"""
    for e in drill.parse_file(os.path.join(WT, "problems.md"), "problems.md"):
        if (e.state == "在池" and e.ask is None and e.history and not e.members
                and not e.essay_prose and e.fam not in drill.NO_PHRASE_FAMS
                and e.created_on() and e.created_on() < drill.ASK_FROM):
            return e.num
    raise SystemExit("⛔ 档案里挑不出符合条件的夹具条目 —— 先看档案是不是变形了")


_A = _pick_fixture()
print(f"（夹具：_A = {_A}，从活档案按条件挑的，⛔ 不写死编号）")


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
    # ⚠️ 2026-09-03：原来这两条写死「44 条」「45 条」—— 每天新挂一条作文验就红一次
    #    （09-03 把 #0108 改挂作文验，两条当场失效）。按 §0.6 夹具纪律改成**结构不变式**：
    ck("标了「题型 作文验」的，essay_only 一定认得出来（⇒ 前者是后者的子集）",
       {e.num for e in ents if e.ask == "作文验"} <= {e.num for e in ents if e.essay_only},
       sorted({e.num for e in ents if e.ask == "作文验"} - {e.num for e in ents if e.essay_only}))
    _only_prose = {e.num for e in ents if e.essay_only and e.ask != "作文验"}
    ck("多出来的那些，全部是**只在触发点散文里**写着「不出单点题」的（过渡期并集）",
       all(any("不出单点题" in x for x in (e.trigger or "").split("\n"))
           for e in ents if e.num in _only_prose),
       sorted(_only_prose))

for grid in ("整句", "词组", "作文验"):
    with sandbox(p_text=set_grid(P, "#0053", grid)) as d:
        e, _ = probs("#0053")
        ck(f"显式写「题型 {grid}」解析得到 {grid}", e.ask == grid and e.ask_kind == grid, e.ask)

print("\n【B】非法值与缺格")
with sandbox(p_text=set_grid(P, _A, "句子")) as d:
    _, pr = probs(_A)
    ck("题型写成非法值 ⇒ ERROR", any("题型「句子」非法" in m for m in lv(pr, "ERROR")), pr)
with sandbox() as d:
    e, pr = probs(_A)
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
_LATE_NUM = _A
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
_ents_g = drill.parse_file(os.path.join(WT, "graduated.md"), "graduated.md")
_byfam, _srcfam = {}, {}
for e in _ents_p:
    if e.state == "在池" and not e.members and not e.essay_prose:
        _byfam.setdefault(e.fam, e.num)
        _srcfam.setdefault(e.fam, "P")
# ★ 族覆盖⛔不许随档案缩水：某族的在池条目全毕业了（09-01 之后 F11 F15 F18 就是），
#   就从 graduated.md 借一条来测 —— 这一段测的是**族的判据**，与条目死活无关。
for e in _ents_g:
    if e.fam not in _byfam and not e.members and not e.essay_prose:
        _byfam[e.fam] = e.num
        _srcfam[e.fam] = "G"
_missing = [f for f in drill.FAMILIES if f not in _byfam]
ck("C 段族覆盖 = 全部 %d 个族（⛔ 不许因为某族全毕业就少测）" % len(drill.FAMILIES),
   not _missing, _missing)


def _fixture(num):
    """把某条标成「题型 词组」——它住哪个文件就改哪个文件。"""
    if _srcfam.get(_bynum_fam(num)) == "G":
        return dict(g_text=set_grid(G, num, "词组"))
    return dict(p_text=set_grid(P, num, "词组"))


def _bynum_fam(num):
    for e in _ents_p + _ents_g:
        if e.num == num:
            return e.fam
    raise SystemExit("找不到 " + num)
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
    with sandbox(**_fixture(num)) as d:
        _, pr = probs(num)
        ck(f"{fam}（句子层）标词组 ⇒ ERROR  [{num}]",
           any("不许标词组" in m for m in lv(pr, "ERROR")), lv(pr, "ERROR"))
allowed = [f for f in drill.FAMILIES if f not in drill.NO_PHRASE_FAMS and f in _byfam]
# C3/F 段要在 problems.md 里改，挑一个住 problems.md 的
allowed_p = [f for f in allowed if _srcfam.get(f) == "P"] or allowed
for fam in allowed:
    num = _byfam[fam]
    with sandbox(**_fixture(num)) as d:
        _, pr = probs(num)
        ck(f"{fam}（非句子层）标词组 ⇒ 不报 ERROR  [{num}]",
           not any("不许标词组" in m for m in lv(pr, "ERROR")), lv(pr, "ERROR"))
# C3 词组题面里有句号 ⇒ WARN
_num = _byfam[allowed_p[0]]
with sandbox(**_fixture(_num)) as d:
    e, pr = probs(_num)
    has_period = "。" in e.trigger
    ck("词组 ＋ 触发点里有句号 ⇒ WARN",
       (not has_period) or any("是**块**不是句" in m for m in lv(pr, "WARN")),
       (has_period, lv(pr, "WARN")))

print("\n【D】作文验：状态行是真源，散文是理由")
with sandbox(p_text=set_grid(P, _A, "作文验")) as d:
    e, pr = probs(_A)
    ck("标了作文验、散文里没理由行 ⇒ WARN",
       any("没有那句理由行" in m for m in lv(pr, "WARN")), lv(pr, "WARN"))
    ck("标了作文验 ⇒ essay_only 成立（不进复习组）", e.essay_only)
    rc, out = run(drill.cmd_pick, Args(type="review"))
    # 口径（2026-09-05 起）：挂作文验的条目**列在排除清单里**、⛔ 不出现在任何一组的卡片里
    cards = "\n".join(l for l in out.split("\n") if l.startswith("  #"))
    excl = out.split("⛔ 挂作文验")[1].split("\n\n")[0] if "⛔ 挂作文验" in out else ""
    ck("pick 把挂作文验的列进排除清单", _A in excl, excl[:200])
    ck("pick 不把它发进任何一组", _A not in cards, cards[:200])
with sandbox(p_text=set_grid(P, "#0053", None)) as d:   # 把已回标的 #0053 退回散文态
    e, pr = probs("#0053")
    ck("散文写着「不出单点题」、状态行没标 ⇒ 存量提示（INFO，不是 ERROR）",
       any("回标成" in m for m in lv(pr, "INFO")) and not lv(pr, "ERROR"),
       (lv(pr, "INFO"), lv(pr, "ERROR")))
    ck("过渡期 essay_only 仍然认散文", e.essay_only)

print("\n【E】count 的新 slug")
with sandbox() as d:
    ents = drill.load_all()
    # ★★ 期望值⛔不许拿被测对象（`ask_kind`）自己算 —— 那样口径整体错了也照样绿。
    #    改成在**夹具文本上直接数状态行第 7 格**，两个独立来源互相印证（她 2026-09-02 定）。
    _txt = (open(os.path.join(d, "problems.md"), encoding="utf-8").read()
            + open(os.path.join(d, "graduated.md"), encoding="utf-8").read())
    _grep = lambda g: len(re.findall(r"^状态：.*｜\s*题型\s*" + g + r"\s*$", _txt, re.M))
    _want = {"ask-essay": _grep("作文验"), "ask-phrase": _grep("词组")}
    ck("期望值来自 grep 状态行（⛔ 不是 ask_kind 自己算的）",
       _want["ask-essay"] > 0 and _want["ask-phrase"] > 0, _want)
    ck("grep 出来的作文验条数 == ask_kind 数出来的（两个独立来源对得上）",
       _want["ask-essay"] == sum(1 for e in ents if e.ask == "作文验"),
       (_want["ask-essay"], sum(1 for e in ents if e.ask == "作文验")))
    ck("grep 出来的词组条数 == ask_kind 数出来的",
       _want["ask-phrase"] == sum(1 for e in ents if e.ask == "词组"),
       (_want["ask-phrase"], sum(1 for e in ents if e.ask == "词组")))
    for slug, want in (("ask-essay", _want["ask-essay"]), ("ask-phrase", _want["ask-phrase"])):
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
_num = _byfam[allowed_p[0]]          # pick 只出【在池】⇒ 必须挑住 problems.md 的
with sandbox(**_fixture(_num)) as d:
    rc, out = run(drill.cmd_pick, Args(type="review", full=False))
    ck("pick 头部报了词组条数", "条词组型" in out, out[:0])
    if _num in out:
        seg = out.split(_num, 1)[1][:400]
        ck(f"{_num} 的卡片打出「题型 **词组**」", "题型 **词组**" in seg, seg[:200])
        ck("词组条目的提示档写死零提示", "词组题给词 ＝ 给答案" in seg, seg[:200])
    else:
        ck(f"{_num} 出现在本次计划里", False, "没被抽到，换一条再测")

print("\n【G】append 不会被第 7 格弄坏")
with sandbox(p_text=set_grid(P, _A, "词组")) as d:
    e0, _ = probs(_A)
    before = e0.status_raw
    rows = os.path.join(d, "rows.md")
    open(rows, "w", encoding="utf-8").write(
        f"{_A} ✅ 测试组 第 1 题\n  测试用内容行。\n")
    rc, out = run(drill.cmd_append, Args(file=rows, date="2026-09-30"))
    ck("append 退出码 0", rc == 0, out[-400:])
    e1, pr = probs(_A)
    ck("题型格没被 append 改掉", e1.ask == "词组", e1.status_raw)
    ck("连对/上次 照常重算", e1.last == "2026-09-30" and e1.ok == (e0.ok or 0) + 1,
       (e1.ok, e1.last))
    ck("状态行仍然是七格", e1.status_raw.count("｜") == 6, e1.status_raw)

# ══════════════════════════════════════════════════════════════════════
#  【F】append 插到本族最后一条时，⛔ 不许把族边界 --- 顶进条目内部
#      （2026-09-03 实测到的 bug：新历史行被插到 --- 的下面）
# ══════════════════════════════════════════════════════════════════════
print("\n【F】append × 本族最后一条 —— 族边界 --- 必须留在条目之后")
import re as _re


def _last_in_fam(text):
    """挑一条【本族最后一条】的在池条目（后面紧跟着下一个族头）。"""
    ents = drill.parse_file(os.path.join(WT, "problems.md"), "problems.md")
    st = {e.num: e.state for e in ents}
    heads = [(m.group(1), m.group(2)) for m in
             _re.finditer(r"^(?:(# F\d\d) |## (#\d{4}) )", text, _re.M)]
    for k in range(len(heads) - 1):
        fam, num = heads[k]
        if num and heads[k + 1][0] and st.get(num) == "在池":
            return num
    return None


_LAST = _last_in_fam(P)
with sandbox() as d:
    rows = os.path.join(d, "rows.md")
    open(rows, "w", encoding="utf-8").write(
        f"{_LAST} 📝 回归测试用的一行\n  测试内容行（⛔ 不进真档案，只在临时副本里）\n")
    rc, out = run(drill.cmd_append, Args(file=rows, date="2026-09-03", dry_run=False))
    ck(f"append 退出码 0（{_LAST}）", rc == 0, out[-400:])
    after = open(drill.PROBLEMS, encoding="utf-8").read()
    ck("新历史行**在**族边界 --- 之前",
       _re.search(r"回归测试用的一行(?:.*\n)*?\n---\n\n# F", after) is not None,
       after[after.index(f"## {_LAST} "):][:1600][-500:])
    ck("缝仍然全部规范（族边界没被顶进条目里）",
       drill.gap_anomalies(drill.PROBLEMS) == [], drill.gap_anomalies(drill.PROBLEMS)[:3])
    ck("check 无 ERROR", run(drill.cmd_check, Args(changed=False, quiet=True, all=True))[0] == 0)

print("\n" + "═" * 70)
print(f"题型回归测试 · 通过 {len(PASS)} · 失败 {len(FAIL)}")
for f in FAIL: print("  ❌ " + f)
sys.exit(1 if FAIL else 0)