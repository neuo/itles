#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""drill.py migrate 的回归测试 —— 全部在临时目录的副本上跑，⛔ 一次都不碰真档案。

跑法：  python3 writing-band7/drill2/tests/test_migrate.py
用途：  改过 drill.py（尤其是 split_file / parse_file / check_entry）之后先跑这个，
        全绿才许拿去搬真档案。SKILL §0.6 已把本文件登记为「测试台，不是第三个工作脚本」。

覆盖：  T0 切块无损 · T1 真实双向搬迁 · T2 幂等 · T3 回程 · T4 目标缺族 ·
        T5 新族排在最前（at==0 边界）· T6 自校失败整批回滚 · T7 族不一致拒搬 ·
        T8 --dry-run 不写盘 · T9 搬完其余子命令照常 ·
        E1 搬走族内最后一条（族间 --- 要留下）· E2 带 --- 缝的条目 · E3 整族搬空再搬回 ·
        E4 文件不以换行结尾 · E5 一次搬空全部在池 · E6 同族双向交叉
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
        self.dry_run = False
        self.changed = False; self.all = True; self.quiet = True
        for k, v in kw.items(): setattr(self, k, v)

@contextlib.contextmanager
def sandbox(p_text=None, g_text=None):
    d = tempfile.mkdtemp(prefix="mig")
    shutil.copy(os.path.join(WT, "problems.md"), os.path.join(d, "problems.md"))
    shutil.copy(os.path.join(WT, "graduated.md"), os.path.join(d, "graduated.md"))
    shutil.copy(os.path.join(WT, "log.md"), os.path.join(d, "log.md"))
    if p_text is not None: open(os.path.join(d, "problems.md"), "w", encoding="utf-8").write(p_text)
    if g_text is not None: open(os.path.join(d, "graduated.md"), "w", encoding="utf-8").write(g_text)
    old = (drill.ROOT, drill.PROBLEMS, drill.GRADUATED, drill.LOG)
    drill.ROOT = d
    drill.PROBLEMS = os.path.join(d, "problems.md")
    drill.GRADUATED = os.path.join(d, "graduated.md")
    drill.LOG = os.path.join(d, "log.md")
    try:
        yield d
    finally:
        (drill.ROOT, drill.PROBLEMS, drill.GRADUATED, drill.LOG) = old
        shutil.rmtree(d, ignore_errors=True)

def run(fn, *a, **kw):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = fn(*a, **kw)
    return rc, buf.getvalue()

def read(d, n): return open(os.path.join(d, n), encoding="utf-8").read()

def bodies():
    out = {}
    for path in (drill.PROBLEMS, drill.GRADUATED):
        _, bl, _ = drill.split_file(path)
        for b in bl:
            if b.kind == "entry": out[b.key] = (os.path.basename(path), tuple(b.body))
    return out

def errset():
    ents = drill.load_all(); nums = {e.num for e in ents}
    return Counter((e.num, lv, re.sub(r"\bL\d+\b", "L*", m))
                   for e in ents for lv, m in drill.check_entry(e, set(), nums))

def statsnums():
    ents = drill.load_all()
    return (len(ents), sum(1 for e in ents if e.in_pool), sum(1 for e in ents if e.graduated),
            sum(1 for e in ents if e.state == "退池"), sum(1 for e in ents if str(e.state).startswith("并入")))

def nonblank(txt):
    return Counter(l for l in txt.split("\n") if l.strip() and l.strip() != "---")

P = open(os.path.join(WT, "problems.md"), encoding="utf-8").read()
G = open(os.path.join(WT, "graduated.md"), encoding="utf-8").read()


def set_state(text, nums, state, ok=None, bad=None):
    lines = text.split("\n")
    for i, l in enumerate(lines):
        m = re.match(r"^## (#\d{4})", l)
        if m and m.group(1) in nums:
            j = i + 1
            lines[j] = re.sub(r"^状态：\S+", "状态：" + state, lines[j])
            if ok is not None: lines[j] = re.sub(r"(连对[ 　]*)\d+", r"\g<1>" + str(ok), lines[j])
            if bad is not None: lines[j] = re.sub(r"(连错[ 　]*)\d+", r"\g<1>" + str(bad), lines[j])
    return "\n".join(lines)


def nums_in(text, fam):
    """某文件里某族的编号顺序"""
    seg = text.split("\n# " + fam + " ")[1].split("\n# F")[0]
    return re.findall(r"^## (#\d{4})", seg, re.M)


def fams_in(text):
    return re.findall(r"^# (F\d\d)", text, re.M)


def drop_fam(text, fam):
    """把某一族整段（族头 ＋ 该族全部条目）删掉 —— 造「目标档没有这个族」的夹具。"""
    lines = text.split("\n")
    a = next(i for i, l in enumerate(lines) if l.startswith("# " + fam + " "))
    b = len(lines)
    for i in range(a + 1, len(lines)):
        if re.match(r"^# F\d\d ", lines[i]):
            b = i
            break
    if b == len(lines):                       # 最后一族 ⇒ 前面那道 --- 缝一起带走
        while a > 0 and lines[a - 1].strip() in ("", "---"):
            a -= 1
        return "\n".join(lines[:a] + [""])
    return "\n".join(lines[:a] + lines[b:])


# ★★ 夹具⛔不许指望「活档案正好有东西可搬」——`migrate` 每天收尾都跑，
#    档案随时是**搬完**的状态（2026-09-01 之后就是），T1/T6/T8 会全部落空。
#    ⇒ 自己造出【待搬】状态，而且**只动状态行第 1 格、⛔ 不动任何一个数**，
#      这样 check 的报告集合一条都不多（连对连错仍与历史重数对得上）：
#        problems.md  每族挑 1 条【在池】改 🎓      （🎓 不查「连对到线」）
#        graduated.md 挑 2 条 🎓 改【退池】         （退池 check 直接 return，不查数）
#    搬迁的期望值全部从这两个集合**推出来**，⛔ 不写死编号、不写死条数。
#    ⚠️ 2026-09-03 再补一刀：活档案也可能**本来就有待搬的**（当天判完还没跑收尾 migrate 时
#      就是这个状态）。夹具⛔不许假设"活档案已经搬干净" ——
#      期望集合 ＝ 【本来就待搬的】∪【夹具自己造的】，两部分都从**当场解析**推出来。
def gaps_ok(_ignored=None):
    """两个文件的缝是不是全规范（用 drill 的唯一定义，⛔ 测试里不另写一套）。"""
    return drill.gap_anomalies(drill.PROBLEMS) == [] and drill.gap_anomalies(drill.GRADUATED) == []


def _make_pre():
    pe = drill.parse_file(os.path.join(WT, "problems.md"), "problems.md")
    ge = drill.parse_file(os.path.join(WT, "graduated.md"), "graduated.md")
    pend_out = [e.num for e in pe if e.state == "🎓"]        # 已经在 problems.md 里等着出去的
    fam_all = {e.num: e.fam for e in pe}                     # 族查表：待搬的那些也要能查到
    pend_back = [e.num for e in ge if e.state != "🎓"]       # 已经在 graduated.md 里等着回来的
    flip_out, fams, seen = [], {}, set()
    for e in pe:
        if e.state == "在池" and e.fam not in seen:
            seen.add(e.fam)
            flip_out.append(e.num)
            fams[e.num] = e.fam
        if len(flip_out) == 9:
            break
    flip_back = [e.num for e in ge if e.state == "🎓"][:2]
    for n in pend_out:
        fams[n] = fam_all[n]
    return flip_out, flip_back, pend_out, pend_back, fams


FLIP_OUT, FLIP_BACK, PEND_OUT, PEND_BACK, OUT_FAM = _make_pre()
OUT = FLIP_OUT + PEND_OUT          # 期望：problems → graduated
BACK = FLIP_BACK + PEND_BACK       # 期望：graduated → problems
PRE_P = set_state(P, set(FLIP_OUT), "🎓")
PRE_G = set_state(G, set(FLIP_BACK), "退池")
N_MOVE = len(OUT) + len(BACK)
print(f"（夹具：造 {len(OUT)} 条 problems→graduated · {len(BACK)} 条 graduated→problems，"
      f"⛔ 只改状态行第 1 格）")

# ══════════════════════════════════════════════════════════════════════
print("\n【T0】split_file 无损切块（真档案两份）")
with sandbox() as d:
    for n in ("problems.md", "graduated.md"):
        p = os.path.join(d, n)
        h, bl, t = drill.split_file(p)
        ck(f"{n} 切开再拼 == 原文", drill.join_file(h, bl) == t)
        ck(f"{n} 每块 body 非空且以块头开头",
           all(b.body and (b.body[0].startswith("# F") or b.body[0].startswith("## #")) for b in bl))
        ck(f"{n} trail 只含空行与 ---",
           all(all(x.strip() in ("", "---") for x in b.trail) for b in bl))

print(f"\n【T1】真实双向搬迁 —— {len(OUT)} 出 {len(BACK)} 回")
with sandbox(p_text=PRE_P, g_text=PRE_G) as d:
    p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
    b0, e0, s0 = bodies(), errset(), statsnums()
    rc, out = run(drill.cmd_migrate, Args())
    ck("退出码 0", rc == 0, rc)
    b1, e1, s1 = bodies(), errset(), statsnums()
    ck("条目集合不变", set(b0) == set(b1))
    ck("每条正文逐字节不变", all(b0[k][1] == b1[k][1] for k in b0),
       [k for k in b0 if b0[k][1] != b1[k][1]][:5])
    ck("check 报告集合不变（抹掉行号）", e0 == e1, list((e1 - e0).items())[:5] + list((e0 - e1).items())[:5])
    ck("stats 五个数不变", s0 == s1, (s0, s1))
    mv = {k for k in b0 if b0[k][0] != b1[k][0]}
    ck(f"恰好 {N_MOVE} 条换了文件", len(mv) == N_MOVE, sorted(mv))
    ck(f"{len(OUT)} 条 problems→graduated",
       sorted(k for k in mv if b1[k][0] == "graduated.md") == sorted(OUT),
       sorted(k for k in mv if b1[k][0] == "graduated.md"))
    ck(f"{len(BACK)} 条 graduated→problems  ({' '.join(BACK)})",
       sorted(k for k in mv if b1[k][0] == "problems.md") == sorted(BACK),
       sorted(k for k in mv if b1[k][0] == "problems.md"))
    ck("🎓 全在 graduated.md / 非🎓 全在 problems.md",
       all((e.state == "🎓") == (e.src == "graduated.md") for e in drill.load_all()))
    p1, g1 = read(d, "problems.md"), read(d, "graduated.md")
    ck("两文件合并后的非空非--- 行多重集不变", nonblank(p0) + nonblank(g0) == nonblank(p1) + nonblank(g1))
    ck("header 一字未动",
       p1.split("\n# F01")[0] == p0.split("\n# F01")[0] and g1.split("\n# F01")[0] == g0.split("\n# F01")[0])
    # 族头数量与文本
    ck("problems.md 族头不变", re.findall(r"^# F.*$", p0, re.M) == re.findall(r"^# F.*$", p1, re.M))
    ck("graduated.md 族头不变", re.findall(r"^# F.*$", g0, re.M) == re.findall(r"^# F.*$", g1, re.M))
    ck("--- 总数不变", (p0 + g0).count("\n---\n") == (p1 + g1).count("\n---\n"),
       ((p0 + g0).count("\n---\n"), (p1 + g1).count("\n---\n")))
    ck("check ⛔ 无新增（migrate 不引入任何错；夹具自带的那几条前后一样）",
       e1 == e0, list((e1 - e0).items())[:5] + list((e0 - e1).items())[:5])
    ck("文件仍以换行结尾", p1.endswith("\n") == p0.endswith("\n") and g1.endswith("\n") == g0.endswith("\n"))

    print("\n【T2】幂等 —— 再跑一次是 no-op 且逐字节不变")
    rc2, out2 = run(drill.cmd_migrate, Args())
    ck("退出码 0", rc2 == 0)
    ck("报告说无操作", "无操作" in out2, out2[-300:])
    ck("problems.md 逐字节不变", read(d, "problems.md") == p1)
    ck("graduated.md 逐字节不变", read(d, "graduated.md") == g1)

    print(f"\n【T3】回程 —— 把 {N_MOVE} 条状态改回去，再搬一次")
    def flip(path, nums, to):
        lines = open(path, encoding="utf-8").read().split("\n")
        ents = drill.parse_file(path, os.path.basename(path))
        for e in ents:
            if e.num in nums:
                i = e.status_lineno - 1
                lines[i] = re.sub(r"^状态：\S+", "状态：" + to, lines[i])
        open(path, "w", encoding="utf-8").write("\n".join(lines))
    flip(drill.GRADUATED, {k for k in mv if b1[k][0] == "graduated.md"}, "在池")
    flip(drill.PROBLEMS, set(BACK), "🎓")
    rc3, out3 = run(drill.cmd_migrate, Args())
    ck("退出码 0", rc3 == 0, out3[-400:])
    b3 = bodies()
    ck(f"{N_MOVE} 条都回到原来的文件", all(b3[k][0] == b0[k][0] for k in mv),
       [(k, b0[k][0], b3[k][0]) for k in mv if b3[k][0] != b0[k][0]])
    ck(f"全档正文除了那 {N_MOVE} 条的状态行外逐字节不变",
       all(b3[k][1] == b0[k][1] for k in b0 if k not in mv))
    ck(f"回程后非空行多重集只差那 {N_MOVE} 条状态行",
       sum(((nonblank(read(d, "problems.md")) + nonblank(read(d, "graduated.md")))
            - (nonblank(p0) + nonblank(g0))).values()) == N_MOVE)

print("\n【T4】目标文件没有这个族 —— 逐字抄族头、按族序插进去")
# 造夹具：挑一个**两边都有条目**的族，把 graduated.md 里它那一整族删掉，
# 再把 problems.md 里同族的某条改成 🎓，看族头会不会被正确造出来。
# ⚠️ 2026-09-03：原来这里写死了 F17 —— 那天 F17 的 4 条全部毕业搬走 ⇒ problems.md 里一条不剩
#    ⇒ `_f17[len//2]` 直接 IndexError。按 §0.6 夹具纪律改成**当场从活档案挑**，⛔ 不写死族号。
_p = open(os.path.join(WT, "problems.md"), encoding="utf-8").read()
_ents = drill.parse_file(os.path.join(WT, "problems.md"), "problems.md")
_gents = drill.parse_file(os.path.join(WT, "graduated.md"), "graduated.md")
_gfams = {e.fam for e in _gents}
_bypfam = {}
for e in _ents:
    _bypfam.setdefault(e.fam, []).append(e)
_cand = [f for f in sorted(_bypfam) if f in _gfams and len(_bypfam[f]) >= 1]
assert _cand, "活档案里找不到【两边都有】的族 —— 夹具无法构造"
_FAM = _cand[len(_cand) // 2]               # 取中间那个族，避开首尾特例
_f17 = _bypfam[_FAM]
_target = _f17[len(_f17) // 2].num          # 取中间一条，避开首尾特例
_m_head = re.search(r"^(# " + _FAM + r" .*)\n\n(> .*)$", _p, re.M)
_FAM_HEAD, _FAM_DESC = _m_head.group(1), _m_head.group(2)
_G_NO_F17 = drop_fam(G, _FAM)
def force_grad(text, num):
    lines = text.split("\n")
    for i, l in enumerate(lines):
        if l.startswith("## " + num):
            j = i + 1
            lines[j] = re.sub(r"^状态：\S+", "状态：🎓", lines[j])
            lines[j] = re.sub(r"(连对[ 　]*)\d+", r"\g<1>2", lines[j])
            lines[j] = re.sub(r"(连错[ 　]*)\d+", r"\g<1>0", lines[j])
            break
    return "\n".join(lines)
with sandbox(p_text=force_grad(_p, _target), g_text=_G_NO_F17) as d:
    g_before = read(d, "graduated.md")
    ck(f"前提：graduated.md 夹具里没有 {_FAM}", "\n# " + _FAM + " " not in g_before)
    b0 = bodies()
    rc, out = run(drill.cmd_migrate, Args())
    ck("退出码 0", rc == 0, out[-500:])
    g_after = read(d, "graduated.md")
    ck(f"graduated.md 造出了 {_FAM} 族头", "\n" + _FAM_HEAD + "\n" in g_after)
    fam_p = re.search(r"^# " + _FAM + r" .*\n\n> .*$", _p, re.M).group(0)
    ck("族头两行与 problems.md 逐字相同", fam_p in g_after, fam_p)
    ck(f"族序正确：{_FAM} 插在正确位置",
       [m.group(1) for m in re.finditer(r"^# (F\d\d)", g_after, re.M)] ==
       sorted([m.group(1) for m in re.finditer(r"^# (F\d\d)", g_after, re.M)]))
    ck(f"{_FAM} 段与前后族之间都有 ---",
       re.search(r"\n---\n\n# " + _FAM + " ", g_after) is not None and
       re.search(r"\n---\n\n# F18 ", g_after) is not None)
    b1 = bodies()
    ck(f"{_target} 换到了 graduated.md", b1[_target][0] == "graduated.md")
    ck("正文逐字节不变", all(b0[k][1] == b1[k][1] for k in b0))
    _e = [x for x in errset() if x[1] == "ERROR"]
    ck("check --all 只剩造数据自带的 ERROR（都挂在夹具那一条上）",
       all(n == _target for n, lv, m in _e), _e)
    ck("再跑一次幂等", run(drill.cmd_migrate, Args())[1].count("无操作") == 1)

print("\n【T5】新族排在全部族之前（at==0 边界）")
# 造一个只有 F14/F18 的目标档，让 F01 条目搬进去
_g = open(os.path.join(WT, "graduated.md"), encoding="utf-8").read()
_cut = _g.index("\n# F14 ")
_gsmall = _g[:_g.index("\n# F01 ")] + _g[_cut:]
# 待搬的 🎓 由 PRE_P 造（活档案本身已经搬干净了）；期望造出来的族 = OUT 里落在 F14 之前的那些族
_WANT_FAMS = sorted({OUT_FAM[n] for n in OUT} - set(fams_in(_gsmall)))
with sandbox(p_text=PRE_P, g_text=_gsmall) as d:
    ck("前提：目标档第一个族是 F14",
       re.search(r"^# (F\d\d)", read(d, "graduated.md"), re.M).group(1) == "F14")
    b0 = bodies(); e_before = errset()
    n0 = len(b0)
    rc, out = run(drill.cmd_migrate, Args())
    ck("退出码 0", rc == 0, out[-600:])
    g_after = read(d, "graduated.md")
    ck(f"造出了 {' '.join(_WANT_FAMS)} 共 {len(_WANT_FAMS)} 个族头",
       bool(_WANT_FAMS) and all(f"\n# {f} " in g_after for f in _WANT_FAMS),
       (_WANT_FAMS, fams_in(g_after)))
    ck("族序仍升序",
       [m.group(1) for m in re.finditer(r"^# (F\d\d)", g_after, re.M)] ==
       sorted(m.group(1) for m in re.finditer(r"^# (F\d\d)", g_after, re.M)))
    b1 = bodies()
    ck("条目数不变", len(b1) == n0)
    ck("正文逐字节不变", all(b0[k][1] == b1[k][1] for k in b0))
    ck("每个族头前都有 ---（除了第一个）",
       all(re.search(r"\n---\n\n# " + f + " ", g_after) for f in fams_in(g_after)[1:]),
       [f for f in fams_in(g_after)[1:] if not re.search(r"\n---\n\n# " + f + " ", g_after)])
    ck("check 报告没有比搬之前多（造数据把 F01–F12 砍掉了，并入目标找不到是自带的）",
       sum((errset() - e_before).values()) == 0, list((errset() - e_before).items())[:6])

print("\n【T6】回滚 —— 自校不过必须两个文件都复原")
with sandbox(p_text=PRE_P, g_text=PRE_G) as d:
    p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
    real = drill.split_file
    def poisoned(path):
        h, bl, t = real(path)
        if os.path.basename(path) == "graduated.md" and poisoned.armed:
            poisoned.armed = False
            for b in bl:
                if b.kind == "entry":
                    b.body = b.body + ["污染行"]      # 只在【写完后的自校】那一次污染
                    break
        return h, bl, t
    poisoned.armed = False
    # 第一次 split（读快照）不污染，写完自校那次污染 → 触发「正文被改动」
    calls = {"n": 0}
    def wrapper(path):
        calls["n"] += 1
        if calls["n"] > 2: poisoned.armed = True
        return poisoned(path)
    drill.split_file = wrapper
    try:
        rc, out = run(drill.cmd_migrate, Args())
    finally:
        drill.split_file = real
    ck("退出码 1", rc == 1, rc)
    ck("报告说整批回滚", "整批回滚" in out, out[-400:])
    ck("problems.md 逐字节复原", read(d, "problems.md") == p0)
    ck("graduated.md 逐字节复原", read(d, "graduated.md") == g0)

print("\n【T7】族与分段不一致 ⇒ 拒搬，⛔ 不写盘")
_pbad = _p
_BADNUM = next(e.num for e in _ents if e.state == "在池" and e.fam == "F01")
_l = _pbad.split("\n")
for i, l in enumerate(_l):
    if l.startswith("## " + _BADNUM):
        _l[i + 1] = re.sub(r"^状态：\S+", "状态：🎓", _l[i + 1]).replace("族 F01", "族 F09")
        break
with sandbox(p_text="\n".join(_l)) as d:
    p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
    rc, out = run(drill.cmd_migrate, Args())
    ck("退出码 1", rc == 1, rc)
    ck(f"报告点名 {_BADNUM}", _BADNUM in out and "不一致" in out, out[-400:])
    ck("两个文件都没写", read(d, "problems.md") == p0 and read(d, "graduated.md") == g0)

print("\n【T8】--dry-run 不写盘")
with sandbox(p_text=PRE_P, g_text=PRE_G) as d:
    p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
    rc, out = run(drill.cmd_migrate, Args(dry_run=True))
    ck("退出码 0", rc == 0)
    ck("两个文件逐字节不变", read(d, "problems.md") == p0 and read(d, "graduated.md") == g0)
    ck(f"打了 {N_MOVE} 条清单", out.count("#0") >= N_MOVE, out.count("#0"))

print("\n【T9】搬完其余子命令照常照常跑")
with sandbox(p_text=PRE_P, g_text=PRE_G) as d:
    run(drill.cmd_migrate, Args())
    for name, fn, kw in (("stats", drill.cmd_stats, dict(brief=False)),
                         ("check --all", drill.cmd_check, dict(changed=False, all=True, quiet=True)),
                         ("count", drill.cmd_count, dict(type=None, detail=False)),
                         ("list --pool", drill.cmd_list, dict(fam=None, state=None, pool=True))):
        try:
            rc, out = run(fn, Args(**kw))
            # check --all 在夹具档上本来就有 ERROR ⇒ rc 1 也算"跑得动"
            ck(f"{name} 跑得动", rc in (0, 1, None) and len(out) > 50, (rc, out[:200]))
        except SystemExit as ex:
            ck(f"{name} 跑得动", False, f"SystemExit {ex}")
    ents = drill.load_all()
    ck("dedup 仍能跨两档命中",
       len(drill.rank(ents, ["单复数"], limit=5)) > 0)


print("\n【E1】搬走某族最后一条 ⇒ 族间 --- 必须留下")
last_f01 = nums_in(P, "F01")[-1]
with sandbox(p_text=set_state(P, {last_f01}, "🎓", 2, 0)) as d:
    before = read(d, "problems.md")
    ck(f"前提：{last_f01} 是 problems.md F01 段最后一条",
       nums_in(before, "F01")[-1] == last_f01)
    def sep_before_fam(t, fam):
        seg = t.split("\n# " + fam + " ")[0]
        ls = seg.split("\n"); out = []
        while ls and ls[-1].strip() in ("", "---"): out.insert(0, ls.pop())
        return out
    sep0 = sep_before_fam(before, "F02")
    rc, out = run(drill.cmd_migrate, Args())
    after = read(d, "problems.md")
    ck("退出码 0", rc == 0, out[-400:])
    ck(f"{last_f01} 已不在 problems.md", "\n## " + last_f01 + " " not in after)
    ck("F02 族头前的分隔行与搬之前逐字一样",
       sep_before_fam(after, "F02") == sep0,
       (sep0, sep_before_fam(after, "F02")))
    ck("F01 段末尾没留下多余空行",
       not re.search(r"\n\n\n+(---\n)?\n?# F02 ", after))
    ck("check 无新增", sum((errset() - errset()).values()) == 0)

print("\n【E2】搬走【本族最后一条】—— 族间的 --- 必须留在来源、⛔ 不许跟着走")
# ⚠️ 2026-09-03 重写：原来这一条钉在"活档案里 #0378 前面正好有个 ---"上（那是族内杂散缝，
#    当天已规范化，而且新的第 5 项自校会直接**拒绝**带杂散缝的档案 ⇒ 见 E2b）。
#    这里改测真正该测的形状：**块自己的缝就是族边界**（本族最后一条）。
def _pick_last_in_fam(text):
    """挑一条【本族最后一条】的在池条目（它后面紧跟着下一个族头）。"""
    ents = drill.parse_file(os.path.join(WT, "problems.md"), "problems.md")
    st = {e.num: e.state for e in ents}
    heads = [(m.start(), m.group(1), m.group(2)) for m in
             re.finditer(r"^(?:(# F\d\d) |## (#\d{4}) )", text, re.M)]
    for k in range(len(heads) - 1):
        _, fam, num = heads[k]
        if num and heads[k + 1][1] and st.get(num) == "在池":
            return num
    return None

_LAST = _pick_last_in_fam(P)
with sandbox(p_text=set_state(P, {_LAST}, "🎓", 2, 0)) as d:
    before = read(d, "problems.md")
    ck(f"前提：{_LAST} 是本族最后一条（后面紧跟族头）",
       re.search(r"\n## " + _LAST + r" [^\n]*\n(?:.*\n)*?---\n\n# F", before) is not None)
    b0 = bodies()
    rc, out = run(drill.cmd_migrate, Args())
    ck("退出码 0", rc == 0, out[-400:])
    b1 = bodies()
    ck(f"{_LAST} 到了 graduated.md", b1[_LAST][0] == "graduated.md")
    ck("正文逐字节不变", all(b0[k][1] == b1[k][1] for k in b0))
    ck("来源的族边界 --- 还在（⛔ 没被带走）",
       gaps_ok(read(d, "problems.md")), drill.gap_anomalies(drill.PROBLEMS)[:3])
    ck("搬到目标后前面是普通空行缝，⛔ 没把 --- 带过去",
       re.search(r"\n---\n\n## " + _LAST + " ", read(d, "graduated.md")) is None)

print("\n【E2b】缝守恒 —— 2026-09-03 加的第 5 项自校（她：「migrate 行数一直不平，说明 check 的不靠谱呀」）")
# 活档案的缝已经规范化 ⇒ 这里**自己造**一处不规范的缝，验两件事：
#   ① check 当场报 ERROR   ② migrate 拒绝落盘并整批回滚（旧的四项自校对这个是瞎的）
def _pick_mid_entry(text):
    """挑一条前面紧挨着另一个条目（⇒ 不是族内第一条）的在池条目。"""
    ents = drill.parse_file(os.path.join(WT, "problems.md"), "problems.md")
    st = {e.num: e.state for e in ents}
    prev_is_entry = False
    for m in re.finditer(r"^(# F\d\d |## (#\d{4}) )", text, re.M):
        if m.group(2):
            if prev_is_entry and st.get(m.group(2)) == "在池":
                return m.group(2)
            prev_is_entry = True
        else:
            prev_is_entry = False
    return None


_MID2 = _pick_mid_entry(P)
_p_bad = set_state(P, {_MID2}, "🎓", 2, 0).replace(f"\n\n## {_MID2} ", f"\n\n\n---\n\n## {_MID2} ")
with sandbox(p_text=_p_bad) as d:
    ck("前提（夹具造的）：档案里有不规范的缝", len(drill.gap_anomalies(drill.PROBLEMS)) > 0)
    rc_c, out_c = run(drill.cmd_check, Args(changed=False, quiet=True, all=True))
    ck("check 把不规范的缝报成 ERROR", rc_c == 1 and "缝" in out_c,
       [l for l in out_c.split("\n") if "ERROR" in l][:3])
    before = read(d, "problems.md")
    rc_m, out_m = run(drill.cmd_migrate, Args())
    ck("migrate 拒绝落盘（退出码 1）", rc_m == 1, out_m[-400:])
    ck("problems.md 逐字节回滚", read(d, "problems.md") == before)
    ck("回滚理由里点名了「缝」或「丢」", ("缝" in out_m or "丢了" in out_m), out_m[-300:])

with sandbox(p_text=PRE_P, g_text=PRE_G) as d:
    rc, out = run(drill.cmd_migrate, Args())
    ck("缝规范的档案照常搬（退出码 0）", rc == 0)
    ck("搬完两个文件的缝全部规范",
       drill.gap_anomalies(drill.PROBLEMS) == [] and drill.gap_anomalies(drill.GRADUATED) == [],
       drill.gap_anomalies(drill.PROBLEMS)[:3] + drill.gap_anomalies(drill.GRADUATED)[:3])
    ck("搬完非空行一行没丢（行数一加一减对得上）",
       sum(nonblank(read(d, "problems.md")).values()) + sum(nonblank(read(d, "graduated.md")).values())
       >= sum(nonblank(PRE_P).values()) + sum(nonblank(PRE_G).values()))

print("\n【E3】整族搬空 ⇒ 空族段仍可解析，再搬回来还能落位")
f17 = nums_in(P, _FAM)
with sandbox(p_text=set_state(P, set(f17), "🎓", 2, 0), g_text=_G_NO_F17) as d:
    b0 = bodies()
    rc, _ = run(drill.cmd_migrate, Args())
    ck("退出码 0", rc == 0)
    p_after = read(d, "problems.md")
    ck(f"problems.md 的 {_FAM} 族头还在（空族段保留）", "\n# " + _FAM + " " in p_after)
    ck(f"{_FAM} 段已清空（原 {len(f17)} 条）", nums_in(p_after, _FAM) == [])
    ck(f"graduated.md 建出了 {_FAM} 段", nums_in(read(d, "graduated.md"), _FAM) == f17)
    ck("空族段照样能解析", len(drill.load_all()) == len(b0))
    # 全部降级搬回
    _demoted = set_state(read(d, "graduated.md"), set(f17), "在池", 1, 0)
    open(drill.GRADUATED, "w", encoding="utf-8").write(_demoted)
    rc, out = run(drill.cmd_migrate, Args())
    ck("回搬退出码 0", rc == 0, out[-400:])
    p_back = read(d, "problems.md")
    ck(f"{_FAM} 全部回到 problems.md 且顺序不变", nums_in(p_back, _FAM) == f17)
    ck(f"graduated.md 的空 {_FAM} 段仍在", "\n# " + _FAM + " " in read(d, "graduated.md"))
    b1 = bodies()
    ck("正文只差状态行", sum(1 for k in b0 if b0[k][1] != b1[k][1]) == len(f17))

print("\n【E4】文件不以换行结尾")
with sandbox(p_text=P.rstrip("\n"), g_text=G.rstrip("\n")) as d:
    b0 = bodies()
    rc, out = run(drill.cmd_migrate, Args())
    ck("退出码 0", rc == 0, out[-400:])
    b1 = bodies()
    ck("正文逐字节不变", all(b0[k][1] == b1[k][1] for k in b0))
    ck("仍然不以空行结尾", not read(d, "problems.md").endswith("\n\n"))
    ck("check 无新增 ERROR",
       sum(v for (n, lv, m), v in errset().items() if lv == "ERROR") ==
       0)

print("\n【E5】大批量 —— 把 problems.md 全部在池条目一次搬空")
pool = [e.num for e in drill.parse_file(os.path.join(WT, "problems.md"), "problems.md")
        if e.state == "在池"]
with sandbox(p_text=set_state(P, set(pool), "🎓", 2, 0), g_text=_G_NO_F17) as d:
    b0 = bodies(); e0 = errset()
    p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
    # 「回潮」的 = 搬之前住在 graduated.md 里、状态已经不是 🎓 的那些（⛔ 不写死编号）
    _back = sorted(e.num for e in drill.parse_file(drill.GRADUATED, "graduated.md")
                   if e.state != "🎓")
    rc, out = run(drill.cmd_migrate, Args())
    ck("退出码 0", rc == 0, out[-500:])
    b1 = bodies()
    ck(f"{len(pool)} 条全搬走", all(b1[n][0] == "graduated.md" for n in pool))
    ck("正文逐字节不变", all(b0[k][1] == b1[k][1] for k in b0))
    _a = nonblank(p0) + nonblank(g0)
    _b = nonblank(read(d, "problems.md")) + nonblank(read(d, "graduated.md"))
    ck("一行都没丢", sum((_a - _b).values()) == 0, list((_a - _b).items())[:8])
    ck(f"多出来的只有新建的 {_FAM} 族头两行（逐字抄自 problems.md）",
       sorted(k for k in (_b - _a)) == sorted([_FAM_HEAD, _FAM_DESC]),
       list((_b - _a).items())[:8])
    ck("graduated.md 每族内仍升序",
       all(nums_in(read(d, "graduated.md"), f) == sorted(nums_in(read(d, "graduated.md"), f))
           for f in re.findall(r"^# (F\d\d)", read(d, "graduated.md"), re.M)))
    ck("check 无新增", sum((errset() - e0).values()) == 0, list((errset() - e0).items())[:4])
    ck("problems.md 只剩退池/并入 ＋ 从 graduated 回潮的 %s" % (" ".join(_back) or "（无）"),
       sorted(e.num for e in drill.load_all()
              if e.src == "problems.md" and e.state == "在池") == _back,
       sorted(e.num for e in drill.load_all() if e.src == "problems.md" and e.state == "在池"))
    ck("再跑幂等", "无操作" in run(drill.cmd_migrate, Args())[1])

print("\n【E6】两个方向同族交叉搬（同一族里有出有进）")
# F06：#0347 #0348 #0369 出；#0248 进 —— T1 已覆盖，这里单看族内顺序
with sandbox() as d:
    run(drill.cmd_migrate, Args())
    for f in ("F06", "F07"):
        for fn in ("problems.md", "graduated.md"):
            t = read(d, fn)
            if "\n# " + f + " " in t:
                ck(f"{fn} {f} 段升序", nums_in(t, f) == sorted(nums_in(t, f)), nums_in(t, f))

print("\n" + "═" * 70)
print(f"drill.py migrate 回归测试 · 通过 {len(PASS)} · 失败 {len(FAIL)}")
for f in FAIL:
    print("  ❌ " + f)
print("═" * 70)
sys.exit(1 if FAIL else 0)
