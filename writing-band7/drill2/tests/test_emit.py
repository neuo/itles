#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-02 四个新功能的回归测试 —— 全部跑临时副本，⛔ 一次都不碰真档案。

跑法：  python3 writing-band7/drill2/tests/test_emit.py
用途：  改过 drill.py 的 pick 排序 / deliver 切节 / trigger / emit 之后先跑这个。
        SKILL §0.6 已把 tests/ 登记为「测试台，不是工作脚本」。

覆盖：
  A  pick --type review：今天已判过的沉底 · 学习日排序一个字没动 ·
     同日重跑分组一致 · N=0 时不打印那一行
  B  deliver：一个 ／ 两个 ／ 零个 `## 回看` 节 · 两节各自块数守恒 ·
     某一节缺件时只有那一节报 ERROR
  C  trigger：正常搬运 · 幂等 · graduated.md 整批不写 · 题型＝词组拒绝 ·
     --dry-run 不写盘 · 自校失败整批回滚
  D  deliver --emit：ERROR>0 拒绝 emit · ERROR=0 输出与 session 逐字节一致 ·
     表格⛔不进围栏 · --section 省略时逐节 emit
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
        for k, v in dict(dry_run=False, changed=False, all=False, quiet=True,
                         type=None, detail=False, fam=None, state=None, pool=False,
                         size=10, groups=None, full=False, date=None, dry=False,
                         brief=False, file=None, session=None, section=None,
                         emit=False, group=None).items():
            setattr(self, k, v)
        for k, v in kw.items():
            setattr(self, k, v)


@contextlib.contextmanager
def sandbox(p_text=None, g_text=None):
    d = tempfile.mkdtemp(prefix="emit")
    for f in ("problems.md", "graduated.md", "review_pool.md", "log.md"):
        shutil.copy(os.path.join(WT, f), os.path.join(d, f))
    if p_text is not None:
        io.open(os.path.join(d, "problems.md"), "w", encoding="utf-8").write(p_text)
    if g_text is not None:
        io.open(os.path.join(d, "graduated.md"), "w", encoding="utf-8").write(g_text)
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
    """→ (rc, stdout, stderr)"""
    so, se = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(so), contextlib.redirect_stderr(se):
        rc = fn(*a, **kw)
    return rc, so.getvalue(), se.getvalue()


def read(d, n):
    return io.open(os.path.join(d, n), encoding="utf-8").read()


P = io.open(os.path.join(WT, "problems.md"), encoding="utf-8").read()
G = io.open(os.path.join(WT, "graduated.md"), encoding="utf-8").read()
DAY = "2026-09-05"


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


def inject_today(text, nums, day):
    """给指定条目塞一条【当天的判定行】—— 只为测 pick 的排序，⛔ 不动状态行。"""
    out, cur = [], None
    for l in text.split("\n"):
        out.append(l)
        m = re.match(r"^## (#\d{4})", l)
        if m:
            cur = m.group(1)
        if cur in nums and l.strip() == "### 历史记录":
            out.append("- %s ✅ 测试注入" % day)
            out.append("  测试注入的内容行。")
    return "\n".join(out)


def set_state_col(text, num, state):
    """只改状态行第 1 格。"""
    lines = text.split("\n")
    for i, l in enumerate(lines):
        if l.startswith("## " + num + " ") or l == "## " + num:
            lines[i + 1] = re.sub(r"^状态：\S+", "状态：" + state, lines[i + 1])
            return "\n".join(lines)
    raise SystemExit("找不到 " + num)


def add_stray_fence(text, num):
    """给某条的正文塞一个**不配对**的 ``` —— 造 P2-9 那个场景。"""
    lines = text.split("\n")
    at = None
    for i, l in enumerate(lines):
        if l.startswith("## " + num + " "):
            at = i
        elif at is not None and l == "**中文触发点**":
            lines.insert(i, "```")
            return "\n".join(lines)
    raise SystemExit("找不到 " + num)


def inject_trace(text, nums, day):
    """同上，但塞的是【留痕行 📝】—— 它⛔不算「今天已经判过」。"""
    out, cur = [], None
    for l in text.split("\n"):
        out.append(l)
        m = re.match(r"^## (#\d{4})", l)
        if m:
            cur = m.group(1)
        if cur in nums and l.strip() == "### 历史记录":
            out.append("- %s 📝 测试留痕" % day)
            out.append("  测试注入的内容行。")
    return "\n".join(out)


RE_CARD = re.compile(r"^\s+(#\d{4})\s+F\d\d\s")


def card_order(out):
    return [m.group(1) for m in (RE_CARD.match(l) for l in out.split("\n")) if m]


# ══════════════════════════════════════════════════════════════════════
print("\n【A】pick --type review：今天已经判过的沉到池底")

with sandbox() as d:
    ents = drill.load_all()
    pool = [e for e in ents if e.in_pool and not e.essay_only]
    pool.sort(key=lambda e: (e.last if e.last and e.last != "—" else "0000-00-00", e.num))
    HEAD3 = [e.num for e in pool[:3]]
    rc, out, _ = run(drill.cmd_pick, Args(type="review", date=DAY, dry=True))
    order0 = card_order(out)
    ck("前提：干净档案下这 3 条排在队首", order0[:3] == HEAD3, (order0[:3], HEAD3))
    ck("N=0 时⛔不打印「今天已经判过」那一行", "今天已经判过" not in out)
    BASE_ORDER = order0
    BASE_OUT = out

with sandbox(p_text=inject_today(P, set(HEAD3), DAY),
             g_text=inject_today(G, set(HEAD3), DAY)) as d:
    rc, out, _ = run(drill.cmd_pick, Args(type="review", date=DAY, dry=True))
    order1 = card_order(out)
    ck("退出码 0", rc == 0, out[-300:])
    ck("3 条全都还在候选池里（沉底，⛔ 不是被删掉）",
       all(n in order1 for n in HEAD3), (HEAD3, order1[:5]))
    pos = [order1.index(n) for n in HEAD3]
    others = [i for i, n in enumerate(order1) if n not in HEAD3]
    ck("3 条全部排在所有【今天没判过的】后面（＝沉到池底）",
       min(pos) > max(others), (sorted(pos), max(others)))
    ck("头部打出了「★ 其中 3 条今天已经判过」",
       "★ 其中 3 条今天已经判过" in out and "已沉到池底" in out,
       [l for l in out.split("\n") if "已经判过" in l])
    ck("其余条目的相对顺序没被打乱",
       [n for n in order1 if n not in HEAD3] == [n for n in BASE_ORDER if n not in HEAD3])
    ck("同一天重跑，分组完全一样",
       run(drill.cmd_pick, Args(type="review", date=DAY, dry=True))[1] == out)

with sandbox(p_text=inject_trace(P, set(HEAD3), DAY),
             g_text=inject_trace(G, set(HEAD3), DAY)) as d:
    rc, out, _ = run(drill.cmd_pick, Args(type="review", date=DAY, dry=True))
    ck("留痕符号 📝 ⛔ 不算「今天已经判过」", "今天已经判过" not in out,
       [l for l in out.split("\n") if "已经判过" in l])
    ck("📝 之后这 3 条仍然排在队首", card_order(out)[:3] == HEAD3, card_order(out)[:3])

print("\n【A2】学习日（--type learn）的排序与分组⛔一个字都没动")
with sandbox() as d:
    rc, learn0, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True))
    ck("学习日跑得动", rc == 0, learn0[-300:])
with sandbox(p_text=inject_today(P, set(HEAD3), DAY),
             g_text=inject_today(G, set(HEAD3), DAY)) as d:
    rc, learn1, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True))
    ck("注入「今天已判过」后，学习日输出逐字一致（⛔ 不受新排序影响）",
       learn1 == learn0)
    ck("学习日⛔不打印「今天已经判过」那一行", "今天已经判过" not in learn1)
with sandbox() as d:
    rc, learn2, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True))
    ck("学习日同日重跑分组一致（按日期定种）", learn2 == learn0)


# ══════════════════════════════════════════════════════════════════════
#  B / D 的 session 夹具 —— 全部写在临时目录里，⛔ 不碰 sessions/
# ══════════════════════════════════════════════════════════════════════
FENCE = "```"


def look_node(tag, sents, drop=None):
    """造一个完整的 `## 回看 · <tag>` 节。drop = 要故意缺掉的子件名。"""
    L = ["## 回看 · %s（测试）" % tag, ""]
    if drop != "题面与条件":
        L += ["### 回看 · %s · 题面与条件（逐字）" % tag, "", FENCE,
              "题号   %s" % tag, "限时   40 分钟", FENCE, ""]
    if drop != "她的原文":
        L += ["### 回看 · %s · 她的原文（逐句编号，逐字）" % tag, "", FENCE]
        L += ["S%d  Sentence %d." % (i + 1, i + 1) for i in range(sents)]
        L += [FENCE, ""]
    if drop != "三版对照块":
        L += ["### 回看 · %s · 三版对照块（%d 块，逐字）" % (tag, sents), "", FENCE]
        for i in range(sents):
            L += ["#S%d" % (i + 1),
                  "  原句　　　 Sentence %d." % (i + 1),
                  "  最小修改　 〔未改〕",
                  "  └ 改了什么 〔未改〕，一个字没改",
                  "  更好版　　 〔没有更好的版本〕",
                  "  └ 为什么好 已经到位", ""]
        L += [FENCE, ""]
    if drop != "最小修改版全文":
        L += ["### 回看 · %s · 最小修改版 · 全文" % tag, "", FENCE,
              " ".join("Sentence %d." % (i + 1) for i in range(sents)), FENCE, ""]
    if drop != "更好版全文":
        L += ["### 回看 · %s · 更好版 · 全文" % tag, "", FENCE,
              " ".join("Sentence %d." % (i + 1) for i in range(sents)), FENCE, ""]
    return L


def group_node(n=1, items=2):
    L = ["## 复习 · 第 %d 组" % n, "", "### 题面（发给她的逐字）", "", FENCE]
    L += ["%d. 中文题面第 %d 句。" % (i + 1, i + 1) for i in range(items)]
    L += [FENCE, "", "### 对应编号（不发给她）", "", FENCE, "1 #0000 F01", FENCE, "",
          "### 她的答案（逐字抄，一个字不改）", "", FENCE]
    L += ["%d. Sentence %d." % (i + 1, i + 1) for i in range(items)]
    L += [FENCE, "", "### 判定表 · 第 %d 组" % n, "",
          "| # | 编号 | 判定 |", "|---|---|---|"]
    L += ["| %d | #000%d | ✅ |" % (i + 1, i + 1) for i in range(items)]
    L += ["", "### 顺带判定 · 第 %d 组" % n, "",
          "**她顺带用错的**", "", "| 出处 | 写的 |", "|---|---|", "| 1 | x |", "",
          "### bc 三版对照块 · 第 %d 组" % n, "", FENCE]
    for i in range(items):
        L += ["#%d" % (i + 1),
              "  原句　　　 Sentence %d." % (i + 1),
              "  最小修改　 〔未改〕",
              "  └ 改了什么 〔未改〕，一个字没改",
              "  更好版　　 〔没有更好的版本〕",
              "  └ 为什么好 已经到位", ""]
    L += [FENCE, "", "### 战报 · 第 %d 组" % n, "",
          "① 一字未改率 2/2", "② 考点命中率 2/2", "③ 新建 无", "④ 本组毕业 无",
          "⑤ 今日毕业 无", ""]
    return L


def write_session(d, name, blocks):
    lines = ["# %s · 测试" % name[:10], ""]
    for b in blocks:
        lines += b
    p = os.path.join(d, name)
    io.open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    return p


print("\n【B】deliver：`## 回看` 节可以有多个")
with sandbox() as d:
    p1 = write_session(d, "2026-09-05.md", [look_node("T2-01", 3)])
    rc, out, _ = run(drill.cmd_deliver, Args(session=p1))
    ck("单个回看节 ⇒ ERROR 0", rc == 0 and "合计 ERROR 0" in out, out[-500:])
    ck("单节时也带上行号标签", "回看 · T2-01（测试）（L" in out, out[:400])
    ck("单节块数守恒 3 = 3", "块数守恒 3 = 3" in out, out)

    p2 = write_session(d, "2026-09-06.md", [look_node("T2-01", 3), look_node("T1-02", 5)])
    rc, out, _ = run(drill.cmd_deliver, Args(session=p2))
    ck("两个回看节 ⇒ ERROR 0", rc == 0 and "合计 ERROR 0" in out, out[-800:])
    ck("两个回看节都被检查了",
       out.count("── 回看 · ") == 2 and "T2-01" in out and "T1-02" in out,
       [l for l in out.split("\n") if l.startswith("── ")])
    ck("两节各自用【本节】的 S 编号数守恒（3 与 5）",
       "块数守恒 3 = 3" in out and "块数守恒 5 = 5" in out, out)
    ck("--section 回看 一次查全部回看节",
       run(drill.cmd_deliver, Args(session=p2, section="回看"))[1].count("── 回看 · ") == 2)

    p3 = write_session(d, "2026-09-07.md", [group_node(1)])
    rc, out, _ = run(drill.cmd_deliver, Args(session=p3))
    ck("零个回看节 ⇒ 不报回看的错，只查复习组",
       rc == 0 and "回看" not in out and "合计 ERROR 0" in out, out[-500:])
    rc, out, _ = run(drill.cmd_deliver, Args(session=p3, section="回看"))
    ck("零个回看节时 --section 回看 ⇒ 报「节不存在」",
       rc == 1 and "节不存在" in out, out[-400:])

    p4 = write_session(d, "2026-09-08.md",
                       [look_node("T2-01", 3), look_node("T1-02", 5, drop="更好版全文")])
    rc, out, _ = run(drill.cmd_deliver, Args(session=p4))
    seg = out.split("── 回看 · T2-01")[1].split("── 回看 · T1-02")[0]
    seg2 = out.split("── 回看 · T1-02")[1]
    ck("第 2 节缺件 ⇒ 合计 ERROR 1", rc == 1 and "合计 ERROR 1" in out, out[-500:])
    ck("只有缺件的那一节报 ERROR",
       "   ERROR  " not in seg and "   ERROR  " in seg2, (seg, seg2))
    ck("第 1 节仍然 ERROR 0 · 可以发", "ERROR 0 · 可以发" in seg, seg)

    p5 = write_session(d, "2026-09-09.md",
                       [look_node("T2-01", 3, drop="她的原文"), look_node("T1-02", 5)])
    rc, out, _ = run(drill.cmd_deliver, Args(session=p5))
    s1 = out.split("── 回看 · T2-01")[1].split("── 回看 · T1-02")[0]
    s2 = out.split("── 回看 · T1-02")[1]
    ck("第 1 节缺「她的原文」⇒ 只有它报错，第 2 节照常守恒 5",
       "   ERROR  " in s1 and "   ERROR  " not in s2 and "块数守恒 5 = 5" in s2, (s1, s2))
    ck("第 1 节的块数守恒⛔不会去数第 2 节的 S 编号",
       "块数守恒 3 = 3" not in s1 and "块数守恒 5 = 5" not in s1, s1)


# ══════════════════════════════════════════════════════════════════════
print("\n【C】trigger：把 session 里当天用的中文题面搬回条目")

_ents_p = drill.parse_file(os.path.join(WT, "problems.md"), "problems.md")
_pool = [e for e in _ents_p
         if e.state == "在池" and not e.is_phrase and not e.essay_only and e.trigger]
A_NUM, B_NUM = _pool[0].num, _pool[1].num
_grad = [e for e in drill.parse_file(os.path.join(WT, "graduated.md"), "graduated.md")][0].num
_phrase = next(e.num for e in _ents_p if e.is_phrase)

NEW1 = ["搬运测试的第一句中文题面。", "（★ 括号里的提示行也要一起搬过去）"]
NEW2 = ["搬运测试的第二句中文题面。"]


def trig_session(d, name, pairs, items):
    L = ["# %s · 测试" % name[:10], "", "## 复习 · 第 1 组", "",
         "### 题面（发给她的逐字）", "", FENCE]
    for i, body in enumerate(items, start=1):
        L.append("%d. %s" % (i, body[0]))
        for extra in body[1:]:
            L.append("   " + extra)
        L.append("")
    L += [FENCE, "", "### 对应编号（不发给她）", "", FENCE,
          " ｜ ".join("%d %s F01" % (k, n) for k, n in pairs), FENCE, ""]
    p = os.path.join(d, name)
    io.open(p, "w", encoding="utf-8").write("\n".join(L) + "\n")
    return p


def entry_of(num):
    return {e.num: e for e in drill.load_all()}[num]


def errcount():
    ents = drill.load_all()
    return Counter((e.num, lv, re.sub(r"\bL\d+\b", "L*", m))
                   for e in ents for lv, m in drill.check_entry(e, set(), {x.num for x in ents}))


def bodies_now():
    """两个文件里每个条目块的字节 —— 自校用。"""
    out = {}
    for path in (drill.PROBLEMS, drill.GRADUATED):
        _h, bl, _t = drill.split_file(path)
        for b in bl:
            if b.kind == "entry":
                out[b.key] = tuple(b.body)
    return out


with sandbox() as d:
    sess = trig_session(d, "2026-09-05.md", [(1, A_NUM), (2, B_NUM)], [NEW1, NEW2])
    before = read(d, "problems.md")
    e0a, e0b = entry_of(A_NUM), entry_of(B_NUM)
    old_a = e0a.trigger.strip()
    err0 = errcount()
    B0 = bodies_now()

    rc, out, _ = run(drill.cmd_trigger, Args(session=sess, group=1, dry_run=True))
    ck("--dry-run 退出码 0", rc == 0, out[-400:])
    ck("--dry-run ⛔ 一个字都没写盘", read(d, "problems.md") == before)
    ck("--dry-run 打出了新旧两版", "旧：" in out and "新：" in out and NEW1[0] in out, out[:600])

    rc, out, _ = run(drill.cmd_trigger, Args(session=sess, group=1))
    ck("真跑退出码 0", rc == 0, out[-600:])
    e1a, e1b = entry_of(A_NUM), entry_of(B_NUM)
    ck("第 1 题的中文逐字进了 %s 的中文触发点" % A_NUM,
       e1a.trigger.split("\n")[0].strip() == NEW1[0]
       and e1a.trigger.split("\n")[1].strip() == NEW1[1], repr(e1a.trigger[:200]))
    ck("第 2 题的中文逐字进了 %s" % B_NUM,
       e1b.trigger.split("\n")[0].strip() == NEW2[0], repr(e1b.trigger[:120]))
    ck("加了 ⚠️ 换题面 那一行（带日期 ＋ 源）",
       "⚠️ **2026-09-05 换题面**" in e1a.trigger
       and "sessions/2026-09-05.md 组1 第1题" in e1a.trigger, repr(e1a.trigger))
    ck("老触发点整段压成一行留档，⛔ 没删",
       "（老触发点留档不删：" in e1a.trigger
       and all(x.strip() in e1a.trigger for x in old_a.split("\n") if x.strip()),
       repr(e1a.trigger))
    ck("老触发点是**一行**（多行用 ／ 连接）",
       len([l for l in e1a.trigger.split("\n") if l.startswith("（老触发点留档不删：")]) == 1
       and (len(old_a.split("\n")) < 2 or "／" in e1a.trigger), repr(e1a.trigger))
    ck("状态行一个字没动", e1a.status_raw == e0a.status_raw, e1a.status_raw)
    ck("历史记录行数没变", len(e1a.history) == len(e0a.history))
    ck("check 无新增报告", sum((errcount() - err0).values()) == 0,
       list((errcount() - err0).items())[:4])

    # 除中文触发点以外逐字节不变
    b1 = bodies_now()
    ck("只有这 2 条的条目块变了",
       sorted(k for k in B0 if B0[k] != b1[k]) == sorted([A_NUM, B_NUM]),
       sorted(k for k in B0 if B0[k] != b1[k]))
    def _no_trigger(body):
        """把「中文触发点」节整段抠掉（测试自己的实现，⛔ 不复用 drill 的任何解析函数）"""
        out, skip = [], False
        for t in body:
            if t == "**中文触发点**":
                out.append(t); skip = True; continue
            if skip:
                if t in drill.TRIG_HARD_BOUND or t.startswith("### "):
                    skip = False
                else:
                    continue
            out.append(t)
        return tuple(out)
    ck("这 2 条【除中文触发点节以外】逐字节不变",
       all(_no_trigger(B0[k]) == _no_trigger(b1[k]) for k in (A_NUM, B_NUM)))
    ck("全档条目集合没变", set(B0) == set(b1))

    # 幂等
    snap = read(d, "problems.md")
    rc, out2, _ = run(drill.cmd_trigger, Args(session=sess, group=1))
    ck("第二遍退出码 0", rc == 0, out2[-400:])
    ck("第二遍零改动（幂等）", read(d, "problems.md") == snap)
    ck("第二遍打出「已是最新，跳过」", out2.count("跳过：已是最新") == 2, out2[:600])
    ck("第二遍打出跳过汇总行", "⏸ 跳过 2 条（已是最新 2）" in out2, out2[-400:])

print("\n【C2】trigger 的拒绝策略分两层（她 2026-09-02 定）")
print("  —— 输入坏了 ⇒ 整批不写 ／ 条目不适用 ⇒ 逐条跳过、其余照常写")

# 层 2：条目不适用 ⇒ 跳过它，⛔ 不挡住整组
for label, mk, want in (
        ("🎓（住 graduated.md）", lambda: (None, None, _grad), "🎓"),
        ("题型 ＝ 词组",          lambda: (set_grid(P, B_NUM, "词组"), None, B_NUM), "词组"),
        ("题型 ＝ 作文验",        lambda: (set_grid(P, B_NUM, "作文验"), None, B_NUM), "作文验"),
        ("状态 ＝ 退池",          lambda: (set_state_col(P, B_NUM, "退池"), None, B_NUM), "退池"),
):
    pt, gt, other = mk()
    with sandbox(p_text=pt, g_text=gt) as d:
        sess = trig_session(d, "2026-09-05.md", [(1, A_NUM), (2, other)], [NEW1, NEW2])
        rc, out, _ = run(drill.cmd_trigger, Args(session=sess, group=1))
        e1 = entry_of(A_NUM)
        ck("%s ⇒ 退出码 0（⛔ 不挡整组）" % label, rc == 0, out[-500:])
        ck("%s ⇒ 那一条被跳过并打出原因" % label,
           ("跳过：%s" % want) in out and other in out, out[-500:])
        ck("%s ⇒ 合法的那条照常写进去了" % label,
           e1.trigger.split("\n")[0].strip() == NEW1[0], repr(e1.trigger[:80]))
        ck("%s ⇒ 结尾有跳过汇总行" % label,
           ("⏸ 跳过 1 条（%s 1）" % want) in out, out[-300:])

# 层 1：输入坏了 ⇒ ⛔ 整批不写
BAD_INPUTS = [
    ("映射数 ≠ 题面题数", [(1, A_NUM)],            [NEW1, NEW2], "≠ 题面"),
    ("编号不是四位",      [(1, "#043"), (2, B_NUM)], [NEW1, NEW2], "不是四位"),
    ("编号全档不存在",    [(1, "#9998"), (2, B_NUM)], [NEW1, NEW2], "查无此编号"),
    ("同一编号出现两次",  [(1, A_NUM), (2, A_NUM)],  [NEW1, NEW2], "重复出现"),
    ("题号指向不存在的题", [(1, A_NUM), (3, B_NUM)], [NEW1, NEW2], "没有第 3 题"),
]
for label, pairs, items, key in BAD_INPUTS:
    with sandbox() as d:
        sess = trig_session(d, "2026-09-05.md", pairs, items)
        before = read(d, "problems.md")
        rc, out, _ = run(drill.cmd_trigger, Args(session=sess, group=1))
        ck("输入坏了：%s ⇒ 退出码 1" % label, rc == 1, out[-400:])
        ck("输入坏了：%s ⇒ ⛔ 整批不写" % label, read(d, "problems.md") == before)
        ck("输入坏了：%s ⇒ 报错点名原因" % label, key in out, out[-400:])

with sandbox() as d:
    sess = trig_session(d, "2026-09-05.md", [(1, A_NUM), (2, B_NUM)], [NEW1, NEW2])
    # 题面第 1 题的续行以「数字.」开头 —— ⛔ 不许被吃成新的第 3 题（P1-4）
    t = io.open(sess, encoding="utf-8").read().replace(
        "   （★ 括号里的提示行也要一起搬过去）",
        "   3.5 倍，涨得非常快。")
    io.open(sess, "w", encoding="utf-8").write(t)
    rc, out, _ = run(drill.cmd_trigger, Args(session=sess, group=1))
    ck("续行 `3.5 倍…` ⛔ 没被吃成新题 ⇒ 退出码 0", rc == 0, out[-500:])
    e1 = entry_of(A_NUM)
    ck("第 1 题的中文没被截断（续行还在）",
       "3.5 倍，涨得非常快。" in e1.trigger and NEW1[0] in e1.trigger, repr(e1.trigger[:150]))

with sandbox() as d:
    sess = trig_session(d, "2026-09-05.md", [(1, A_NUM), (2, B_NUM)], [NEW1, NEW2])
    t = io.open(sess, encoding="utf-8").read().replace("2. 搬运测试的第二句中文题面。",
                                                       "3. 搬运测试的第二句中文题面。")
    io.open(sess, "w", encoding="utf-8").write(t)
    before = read(d, "problems.md")
    rc, out, _ = run(drill.cmd_trigger, Args(session=sess, group=1))
    ck("题号跳号（1,3）⇒ 整批不写", rc == 1 and read(d, "problems.md") == before, out[-400:])
    ck("题号跳号 ⇒ 报错说「不是 1..N 连号」", "连号" in out, out[-400:])

print("\n【C3】留档⛔不许套娃 · CRLF 不许被改 · 不配对围栏必须报对原因")
with sandbox() as d:
    NEWS = [["第一次换的中文题面。"], ["第二次换的中文题面。"], ["第三次换的中文题面。"]]
    for r in range(3):
        sess = trig_session(d, "2026-09-0%d.md" % (5 + r), [(1, A_NUM)], [NEWS[r]])
        rc, out, _ = run(drill.cmd_trigger, Args(session=sess, group=1))
        ck("第 %d 次搬运退出码 0" % (r + 1), rc == 0, out[-400:])
    trg = entry_of(A_NUM).trigger
    keep = [l for l in trg.split("\n") if l.strip().startswith(drill.TRIG_OLD_PREFIX)]
    ck("留档行只有一行", len(keep) == 1, keep)
    ck("留档行里⛔没有嵌套的「老触发点留档不删」",
       drill.TRIG_OLD_PREFIX not in keep[0][len(drill.TRIG_OLD_PREFIX):], keep[0][:200])
    ck("留档行里⛔没有脚本自己生成的「换题面」标记",
       "`drill.py trigger` 自动搬运" not in keep[0], keep[0][:200])
    ck("三次的原始中文都还在留档里",
       all(x[0] in trg for x in NEWS[:2]) and NEWS[2][0] in trg, trg[:300])
    ck("⚠️ 换题面标记只有最新那一行",
       sum(1 for l in trg.split("\n") if drill.RE_TRIG_STAMP.match(l.strip())) == 1,
       trg[:300])

with sandbox(p_text=P.replace("\n", "\r\n")) as d:
    sess = trig_session(d, "2026-09-05.md", [(1, A_NUM), (2, B_NUM)], [NEW1, NEW2])
    raw0 = open(os.path.join(d, "problems.md"), "rb").read()
    ck("前提：夹具是 CRLF", raw0.count(b"\r\n") > 1000 and b"\r\n" in raw0)
    rc, out, _ = run(drill.cmd_trigger, Args(session=sess, group=1))
    raw1 = open(os.path.join(d, "problems.md"), "rb").read()
    ck("CRLF 档案：退出码 0", rc == 0, out[-500:])
    ck("CRLF 没被改成 LF", raw1.count(b"\r\n") >= raw0.count(b"\r\n") - 5
       and b"\n" in raw1 and raw1.count(b"\n") == raw1.count(b"\r\n"), 
       (raw0.count(b"\r\n"), raw1.count(b"\r\n"), raw1.count(b"\n")))
    ck("CRLF 档案的字节变化量与新旧内容差相当（⛔ 不是整档重写）",
       abs(len(raw1) - len(raw0)) < 4000, (len(raw0), len(raw1)))
    ck("CRLF 档案里新题面确实落地", NEW1[0] in raw1.decode("utf-8"))

with sandbox(p_text=add_stray_fence(P, A_NUM)) as d:
    sess = trig_session(d, "2026-09-05.md", [(1, A_NUM), (2, B_NUM)], [NEW1, NEW2])
    before = read(d, "problems.md")
    rc, out, _ = run(drill.cmd_trigger, Args(session=sess, group=1))
    ck("条目里有不配对的 ``` ⇒ 退出码 1", rc == 1, out[-400:])
    ck("报错指向真正的原因（不配对的围栏），⛔ 不是历史记录",
       "不配对" in out and "围栏" in out and "历史记录的问题" in out, out[-400:])
    ck("不配对围栏 ⇒ ⛔ 整批不写", read(d, "problems.md") == before)

with sandbox() as d:
    sess = trig_session(d, "2026-09-05.md", [(1, A_NUM), (2, B_NUM)], [NEW1, NEW2])
    before = read(d, "problems.md")
    real = drill._errmap
    calls = {"n": 0}

    def poisoned(ents, nums):
        calls["n"] += 1
        c = real(ents, nums)
        if calls["n"] > 1:                      # 写完自校那一次注入一条假 ERROR
            c[("#9999", "ERROR", "注入的假错")] += 1
        return c
    drill._errmap = poisoned
    try:
        rc, out, _ = run(drill.cmd_trigger, Args(session=sess, group=1))
    finally:
        drill._errmap = real
    ck("自校发现新增 ERROR ⇒ 退出码 1", rc == 1, out[-400:])
    ck("自校不过 ⇒ 整批回滚，problems.md 逐字节复原", read(d, "problems.md") == before)
    ck("回滚有明说", "已整批回滚" in out, out[-400:])


# ══════════════════════════════════════════════════════════════════════
print("\n【D】deliver --emit：直接产出要粘贴的那一段")


def fence_depth_map(lines):
    """→ [每一行所处的围栏深度]（围栏线本身记它外面的深度）"""
    out, inside = [], False
    for l in lines:
        if l.startswith(FENCE):
            out.append(0 if not inside else 1)
            inside = not inside
        else:
            out.append(1 if inside else 0)
    return out


with sandbox() as d:
    good = write_session(d, "2026-09-05.md",
                         [group_node(1), look_node("T2-01", 3), look_node("T1-02", 5)])
    src = io.open(good, encoding="utf-8").read().split("\n")

    rc, out, err = run(drill.cmd_deliver, Args(session=good, emit=True))
    ck("ERROR 0 ⇒ emit 退出码 0", rc == 0, out[-400:])
    ck("硬闸报告走 stderr，stdout 只留要粘贴的内容",
       "合计 ERROR 0" in err and "合计 ERROR 0" not in out, out[:300])
    lines = out.split("\n")
    absent = [l for l in lines if l.strip() and l != FENCE and l not in src]
    ck("每一行都逐字节取自 session（围栏本身除外）", not absent, absent[:3])
    ck("三个交付节全部 emit 了（--section 省略 ⇒ 逐节）",
       [l for l in lines if l.startswith("## ")]
       == ["## 复习 · 第 1 组", "## 回看 · T2-01（测试）", "## 回看 · T1-02（测试）"],
       [l for l in lines if l.startswith("## ")])
    ck("⛔ 没有把 session 里的行漏掉：三版对照块的每一块都在",
       all(("#S%d" % i) in lines for i in (1, 2, 3)) and all(("#%d" % i) in lines for i in (1, 2)))

    dep = fence_depth_map(lines)
    tbl = [i for i, l in enumerate(lines) if l.startswith("|")]
    ck("判定表／顺带判定的表格行⛔没被塞进围栏", tbl and all(dep[i] == 0 for i in tbl),
       [(i, lines[i]) for i in tbl if dep[i]][:3])
    war = [i for i, l in enumerate(lines) if l.startswith("①") or l.startswith("⑤")]
    ck("战报⛔没被塞进围栏", war and all(dep[i] == 0 for i in war), war)
    q = lines.index("### 题面（发给她的逐字）")
    ck("题面在围栏里（一组一个围栏）",
       lines[q + 2] == FENCE and dep[lines.index("1. 中文题面第 1 句。")] == 1)
    bidx = lines.index("### bc 三版对照块 · 第 1 组")
    ck("三版对照块整节一个围栏", lines[bidx + 2] == FENCE and dep[lines.index("#1")] == 1)
    ck("⛔ 没有套第二层围栏（session 里已经写了围栏的不再包一次）",
       FENCE + FENCE not in "\n".join(lines) and
       not any(lines[i] == FENCE and lines[i + 1] == FENCE for i in range(len(lines) - 1)))
    ck("她的答案⛔不进 emit（那是她自己写的，不是交付件）",
       "### 她的答案（逐字抄，一个字不改）" not in lines)
    ck("对应编号⛔不进 emit（`### 对应编号（不发给她）`）",
       "### 对应编号（不发给她）" not in lines)

    rc, out1, _ = run(drill.cmd_deliver, Args(session=good, section="组1", emit=True))
    h2 = [l for l in out1.split("\n") if l.startswith("## ")]
    ck("--section 组1 只 emit 这一节",
       rc == 0 and h2 == ["## 复习 · 第 1 组"], h2)
    rc, out2, _ = run(drill.cmd_deliver, Args(session=good, section="回看", emit=True))
    h2b = [l for l in out2.split("\n") if l.startswith("## ")]
    ck("--section 回看 emit 两节",
       rc == 0 and h2b == ["## 回看 · T2-01（测试）", "## 回看 · T1-02（测试）"], h2b)

    bad = write_session(d, "2026-09-06.md",
                        [look_node("T2-01", 3), look_node("T1-02", 5, drop="更好版全文")])
    rc, out, err = run(drill.cmd_deliver, Args(session=bad, emit=True))
    ck("ERROR > 0 ⇒ 拒绝 emit，退出码非 0", rc != 0, rc)
    ck("拒绝时打印 ERROR", "ERROR" in out and "拒绝 emit" in out, out[-400:])
    ck("拒绝时⛔一个交付件都不吐", "Sentence 1." not in out, out[-600:])

    # 块数不守恒也必须拦住 emit
    bad2 = write_session(d, "2026-09-07.md", [look_node("T2-01", 3)])
    t = io.open(bad2, encoding="utf-8").read().replace("S3  Sentence 3.\n", "")
    io.open(bad2, "w", encoding="utf-8").write(t)
    rc, out, _ = run(drill.cmd_deliver, Args(session=bad2, emit=True))
    ck("块数不守恒 ⇒ 拒绝 emit", rc != 0 and "块数不守恒" in out, out[-400:])


print("\n【E】2026-09-02 对抗测试报出的缺陷 —— 逐条回归")


def tail_node():
    """`## 收尾` 里放一个 `### 更好版 · 收尾复盘` —— 回看节收不了口就会被它顶掉（P0-1）。"""
    return ["## 收尾（§4⑥）", "", "### 更好版 · 收尾复盘", "",
            "这不是交付件，是收尾复盘。", ""]


def coach_node():
    return ["## 教练侧 · 本场犯规记录", "", "### 她的原文 · 教练侧引用", "",
            "S1  这不是回看的原文。", ""]


with sandbox() as d:
    # ── P0-1 回看节必须在 `## 教练侧` `## 收尾` 处收口 ──────────────────
    f = write_session(d, "2026-09-05.md",
                      [look_node("T2-01", 3, drop="更好版全文"), tail_node()])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("P0-1 回看真缺「更好版全文」⇒ 报 ERROR（⛔ 不被 ## 收尾 里的同名标题顶掉）",
       rc == 1 and "缺子件「更好版全文」" in out, out[-600:])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f, emit=True))
    ck("P0-1 ERROR>0 ⇒ 拒绝 emit", rc != 0 and "这不是交付件" not in out, out[-300:])

    f = write_session(d, "2026-09-06.md",
                      [look_node("T2-01", 3), coach_node(), tail_node()])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("P0-1 回看齐全 ＋ 后面有教练侧/收尾 ⇒ ERROR 0", rc == 0, out[-600:])
    ck("P0-1 块数守恒仍按本节的 3 句（⛔ 没吃进教练侧的 S1）",
       "块数守恒 3 = 3" in out, out)
    rc, out, _ = run(drill.cmd_deliver, Args(session=f, emit=True))
    ck("P0-1 emit ⛔ 不吐 `## 收尾` / `## 教练侧` 的内容",
       "这不是交付件" not in out and "这不是回看的原文" not in out, out[-400:])

    # ── P0-2 同名复习组出现两次 ⇒ 按行号切成两节 ────────────────────────
    g1, g2 = group_node(1, items=2), group_node(1, items=3)
    f = write_session(d, "2026-09-07.md", [g1, g2])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    heads = [l for l in out.split("\n") if l.startswith("── ")]
    ck("P0-2 同名组出现两次 ⇒ 切成两节（标签带行号，各不相同）",
       len(heads) == 2 and heads[0] != heads[1], heads)
    ck("P0-2 两节各按自己的题数守恒（2 与 3）",
       "块数守恒 2 = 2" in out and "块数守恒 3 = 3" in out, out)
    rc, oe, _ = run(drill.cmd_deliver, Args(session=f, emit=True))
    ck("P0-2 emit 两节各吐一次（⛔ 不是把第一节吐两遍）",
       rc == 0 and oe.count("3. 中文题面第 3 句。") == 1
       and len([l for l in oe.split("\n") if l.startswith("## ")]) == 2,
       [l for l in oe.split("\n") if l.startswith("## ")])
    rc, o1, _ = run(drill.cmd_deliver, Args(session=f, section="组1"))
    ck("P0-2 --section 组1 也查两节",
       len([l for l in o1.split("\n") if l.startswith("── ")]) == 2, o1[:400])

    # ── P1-3 old_four 豁免不许恒真 ─────────────────────────────────────
    f = write_session(d, "2026-09-08.md", [look_node("T2-01", 3, drop="三版对照块")])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("P1-3 回看整节没有三版对照块 ⇒ 报 ERROR（⛔ 不再被 old_four 恒真豁免）",
       rc == 1 and "缺子件「三版对照块」" in out
       and "旧四份格式" not in out, out[-600:])
    body = look_node("T2-01", 3, drop="三版对照块")
    body = body + ["### 回看 · T2-01 · diff 表A（旧格式）", "", "| 原句 | 改后 |",
                   "|---|---|", "| a | b |", ""]
    f = write_session(d, "2026-08-25.md", [body])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("P1-3 真的旧四份（最小修改版 ＋ diff 表 都在）⇒ 仍走存量豁免",
       "旧四份格式" in out, out[-600:])

    # ── P2-10 顺带判定进必查件（带日期线）───────────────────────────────
    def group_no_incident(n=1, items=2):
        out_ = []
        skip = False
        for l in group_node(n, items):
            if l.startswith("### 顺带判定"):
                skip = True
                continue
            if skip and l.startswith("### "):
                skip = False
            if not skip:
                out_.append(l)
        return out_
    f = write_session(d, "2026-09-09.md", [group_no_incident()])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("P2-10 2026-09-02 起缺「顺带判定」⇒ ERROR",
       rc == 1 and "缺子件「a 顺带判定」" in out, out[-500:])
    f = write_session(d, "2026-08-30.md", [group_no_incident()])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("P2-10 2026-09-02 之前缺「顺带判定」⇒ 存量提示，⛔ 不报错",
       rc == 0 and "顺带判定" in out and "存量" in out, out[-500:])

    # ── P3-12 表格被写进围栏 ⇒ WARN（⛔ 不静默）─────────────────────────
    fenced = []
    for l in group_node(1, items=2):
        if l.startswith("| ") or l.startswith("|---"):
            fenced.append(l)
        else:
            fenced.append(l)
    g = group_node(1, items=2)
    k = g.index("### 判定表 · 第 1 组")
    g = g[:k + 2] + [FENCE] + g[k + 2:k + 5] + [FENCE] + g[k + 5:]
    f = write_session(d, "2026-09-10.md", [g])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("P3-12 判定表被写进围栏 ⇒ 报 WARN，⛔ 不静默",
       "WARN" in out and "表格⛔不进围栏" in out, out[-600:])
    ck("P3-12 它只是 WARN，⛔ 不拦发", rc == 0 and "ERROR 0" in out, out[-300:])

    # ── P3-11 块内有围栏、外层没有 ⇒ emit 用更长的围栏包，⛔ 不是不包 ──────
    look = look_node("T2-01", 1)
    k = look.index("### 回看 · T2-01 · 最小修改版 · 全文")
    look = look[:k + 2] + ["Sentence 1.", "```", "inner fence", "```", ""] + look[k + 6:]
    f = write_session(d, "2026-09-11.md", [look])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("P3-11 前提：这个夹具本身 ERROR 0", rc == 0, out[-400:])
    rc, oe, _ = run(drill.cmd_deliver, Args(session=f, emit=True))
    ol = oe.split("\n")
    kk = ol.index("### 回看 · T2-01 · 最小修改版 · 全文")
    ck("P3-11 外层没围栏 ⇒ emit 补一个**更长**的围栏（⛔ 不是不补）",
       ol[kk + 2] == "````" and "inner fence" in oe, ol[kk:kk + 8])
    ck("P3-11 已带外层围栏的块⛔不再套第二层",
       oe.count("`````") == 0, [l for l in ol if set(l.strip()) == {"`"}][:6])

print("\n【F】pick 的承诺必须与事实一致（P1-5 / P3-13）")
with sandbox() as d:
    rc, o_r, _ = run(drill.cmd_pick, Args(type="review", date=DAY, dry=True))
    rc2, o_l, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True))
    ck("P1-5 ⛔ 不再承诺「完全一样」（复习日）", "完全一样" not in o_r,
       [l for l in o_r.split("\n") if "完全一样" in l])
    ck("P1-5 ⛔ 不再承诺「完全一样」（学习日）", "完全一样" not in o_l,
       [l for l in o_l.split("\n") if "完全一样" in l])
    ck("P1-5 复习日照实写：已 used 的不再出现 ＋ 已判过的沉底 ＋ 不保证逐字重现",
       "已 used 的不再出现" in o_r and "当天已判过的沉到池底" in o_r
       and "⛔ 不保证逐字重现" in o_r, o_r[:1200])
    ck("P1-5 学习日也照实写", "⛔ 不保证逐字重现" in o_l, o_l[:1200])
    ck("P1-5 复习日头部点明「今天已判过」是当天会变的状态",
       "当天会变" in o_r, o_r[:1200])
    ck("P3-13 带 --date 时打出「⛔ 不能用来忠实回放当天的分组」",
       "不能用来忠实回放当天的分组" in o_r and "不能用来忠实回放当天的分组" in o_l)

print("\n" + "═" * 70)
print(f"2026-09-02 四功能回归测试 · 通过 {len(PASS)} · 失败 {len(FAIL)}")
for f in FAIL:
    print("  ❌ " + f)
print("═" * 70)
sys.exit(1 if FAIL else 0)
