#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-02 四个新功能的回归测试 —— 全部跑临时副本，⛔ 一次都不碰真档案。

跑法：  python3 writing-band7/drill2/tests/test_emit.py
用途：  改过 drill.py 的 pick 排序 / deliver 切节 / trigger / emit 之后先跑这个。
        SKILL §0.6 已把 tests/ 登记为「测试台，不是工作脚本」。

覆盖：
  A  pick --type review：今天已判过的沉底 · 学习日排序一个字没动 ·
     同日重跑分组一致 · N=0 时不打印那一行
  A3 pick 的「建号当天不回考」（2026-09-03 上线）：建号日 ＝ 今天的⛔不进池 ·
     同类但建号日 ≠ 今天的仍在 · 报告逐条列编号 · 学习日与复习日都过滤 ·
     ⛔ 判据是第一条历史行、不是「上次」那一格
  B  deliver：一个 ／ 两个 ／ 零个 `## 回看` 节 · 两节各自块数守恒 ·
     某一节缺件时只有那一节报 ERROR
  C  trigger：正常搬运 · 幂等 · graduated.md 整批不写 · 题型＝词组拒绝 ·
     --dry-run 不写盘 · 自校失败整批回滚
  D  deliver --emit：ERROR>0 拒绝 emit · ERROR=0 输出与 session 逐字节一致 ·
     表格⛔不进围栏 · --section 省略时逐节 emit
  H  deliver 的条件性子件「新建条目的正文」（2026-09-03 上线）：报了新建就必须发正文 ·
     少写一条正文点名缺号 · 没报／报 0 条 ⇒ ⛔ 不要求 · 09-03 之前是存量提示 ·
     「组」与「新题」都吃、回看⛔ 不吃
  G  lookback（2026-09-03 上线）：目标 ＝ 最近一篇【没被回看过】的新题 ·
     标题行没题号的 `## 回看` ⛔ 不算回看 · 多篇未回看取最近 · 今天写的那篇⛔不作目标 ·
     认不出题号／drawn.log 孤儿逐条列 · 只读（⛔ 不写任何文件）· pick --type learn 头部那一行
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
                         emit=False, group=None, scope="both", queue="pool").items():
            setattr(self, k, v)
        for k, v in kw.items():
            setattr(self, k, v)


@contextlib.contextmanager
def sandbox(p_text=None, g_text=None):
    d = tempfile.mkdtemp(prefix="emit")
    for f in ("problems.md", "graduated.md", "log.md"):
        shutil.copy(os.path.join(WT, f), os.path.join(d, f))
    if p_text is not None:
        io.open(os.path.join(d, "problems.md"), "w", encoding="utf-8").write(p_text)
    if g_text is not None:
        io.open(os.path.join(d, "graduated.md"), "w", encoding="utf-8").write(g_text)
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
    """→ (rc, stdout, stderr)"""
    so, se = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(so), contextlib.redirect_stderr(se):
        rc = fn(*a, **kw)
    return rc, so.getvalue(), se.getvalue()


def read(d, n):
    return io.open(os.path.join(d, n), encoding="utf-8").read()


P = io.open(os.path.join(WT, "problems.md"), encoding="utf-8").read()
G = io.open(os.path.join(WT, "graduated.md"), encoding="utf-8").read()
# ⚠️ **2026-09-06 改**：原来这里写死 `DAY = "2026-09-05"`。
#    队列的每个数都是**相对 DAY 算**的（逾期分 ＝ 距有效上次的练习日数 ÷ 应等间隔），
#    而档案每天都在长 —— 只要活档案里出现了比 DAY 更晚的判定行，
#    那些条目的「有效上次」就落在 DAY **之后**，队列行为无法预期 ⇒ 测试台假红
#    （09-06 那天就是这么红的：#0441 #0450 的有效上次 ＝ 09-06 ＞ DAY）。
#    ⇒ 改成**取 log.md 里最后一个练习日**，跟着档案走（§0.6 夹具规矩：⛔ 不许写死）。
DAY = sorted(drill.day_types().keys())[-1]


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


def inject_row(text, nums, day, sym, note):
    """给指定条目的【历史记录节末尾】追加一条当天的行 —— 只为测 pick，⛔ 不动状态行、⛔ 不动任何数。

    ★ 2026-09-03 改成追加到节**末尾**（原写法插在 `### 历史记录` 的**下一行** ⇒ 那一行就成了
      **第一条历史行** ＝ 契约里的「建号日」，会被新规则『建号当天不回考』当成今天新建的挡掉）。
      判定行本来就该按时间追加在最后（契约⑧「上次 ＝ 最后一条历史行」），原写法是夹具写反了。
    ⛔ 只加行，不碰条目之间的缝（契约⑭）：先摘掉尾部空行，追加，再原样放回。"""
    out, cur, in_hist = [], None, False

    def flush():
        while out and not out[-1].strip():
            tail.append(out.pop())
        out.append("- %s %s %s" % (day, sym, note))
        out.append("  测试注入的内容行。")
        while tail:
            out.append(tail.pop())

    for l in text.split("\n"):
        m = re.match(r"^## (#\d{4})", l)
        boundary = bool(m) or l.strip() == "---" or l.startswith("# ")
        if in_hist and boundary:
            tail = []
            flush()
            in_hist = False
        if m:
            cur = m.group(1)
        out.append(l)
        if cur in nums and l.strip() == "### 历史记录":
            in_hist = True
    if in_hist:
        tail = []
        flush()
    return "\n".join(out)


def inject_today(text, nums, day):
    """给指定条目塞一条【当天的判定行】—— 只为测 pick 的排序，⛔ 不动状态行。"""
    return inject_row(text, nums, day, "✅", "测试注入")


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
    return inject_row(text, nums, day, "📝", "测试留痕")


RE_CARD = re.compile(r"^\s+(#\d{4})\s+F\d\d\s")


def card_order(out):
    return [m.group(1) for m in (RE_CARD.match(l) for l in out.split("\n")) if m]


# ══════════════════════════════════════════════════════════════════════
print("\n【A】召回队列（§3.6）：今天判过的当天不再到期")
#  ⛔ 旧断言「复习日按最久没测优先 ＋ 今天已判过沉底」**整段作废**（2026-09-05）——
#     梯子上线后两件事变了：
#       ① 学习日与复习日**同一条队列、同一套排序**，只差配额与有没有新题
#       ② 「今天判过」不再靠一条特判沉底 —— 有效上次 ＝ 今天 ⇒ 逾期分 0 ⇒ **压根不到期**
#     要守的东西没变：同一天里⛔不许把刚判过的再问一遍。

with sandbox() as d:
    ents0 = drill.load_all()
    PLAN0 = drill.plan_queues(ents0, DAY, drill.day_types(), "review")
    rc, out, _ = run(drill.cmd_pick, Args(type="review", date=DAY, dry=True, scope="pool"))
    order0 = card_order(out)
    # ★ 组间按逾期分切、**组内**按族错开 ⇒ 比的是【组 1 的集合】，⛔ 不是组内次序
    ck("组 1 的集合 ＝ 队列最前面的 10 条",
       set(order0[:10]) == {e.num for e in PLAN0["pool_take"][:10]},
       (order0[:10], [e.num for e in PLAN0["pool_take"][:10]]))
    ck("卡片打出了档位与逾期分", "逾期分" in out and "档位" in out)
    HEAD3 = order0[:3]
    BASE_ORDER = order0

with sandbox(p_text=inject_today(P, set(HEAD3), DAY),
             g_text=inject_today(G, set(HEAD3), DAY)) as d:
    rc, out, _ = run(drill.cmd_pick, Args(type="review", date=DAY, dry=True, scope="pool"))
    order1 = card_order(out)
    ck("退出码 0", rc == 0, out[-300:])
    ck("今天判过的 3 条**今天不再出**（有效上次＝今天 ⇒ 逾期分 0）",
       all(n not in order1 for n in HEAD3), (HEAD3, order1[:5]))
    ck("⛔ 不是被删掉：它们仍在档案里、状态没动",
       all(any(e.num == n and e.in_pool for e in drill.load_all()) for n in HEAD3))
    ck("其余条目仍在队列里（只少掉那 3 条，⛔ 不多不少）",
       set(BASE_ORDER) - set(order1) == set(HEAD3),
       sorted(set(BASE_ORDER) - set(order1)))
    ck("同一天重跑，分组完全一样",
       run(drill.cmd_pick, Args(type="review", date=DAY, dry=True, scope="pool"))[1] == out)

# ⚠️ **2026-09-06 改**：这一段原来直接拿 HEAD3（队列最前面 3 条）去注入 📝。
#    可队首现在常常是**从未被判定过**的条目（09-06 那天有 16 条作文验改回出题、`上次 —`，
#    逾期分 ∞ ⇒ 全部排在队首）。给一条没有历史的条目追加一行今天的 📝，
#    那一行就成了它的**第一条历史行 ＝ 建号行** ⇒ 被「建号当天不回考」正确地挡下 ⇒ 假红。
#    ⇒ 改成**按条件挑**：队列里前 3 条**已经有真判定行**的（📝 才不会变成建号行）。
_JUDGED = {"✅", "◎✅", "❌", "📖", "△", "◎−", "📋"}
_hist_ok = {e.num for e in drill.load_all()
            if any(h.symbol in _JUDGED for h in e.history)}
HEAD3 = [n for n in BASE_ORDER if n in _hist_ok][:3]
assert len(HEAD3) == 3, "⛔ 队列里挑不出 3 条已有判定行的条目"
with sandbox(p_text=inject_trace(P, set(HEAD3), DAY),
             g_text=inject_trace(G, set(HEAD3), DAY)) as d:
    rc, out, _ = run(drill.cmd_pick, Args(type="review", date=DAY, dry=True, scope="pool"))
    # ⚠️ **2026-09-06 改**：原来断言「这 3 条仍然在**组 1** 里」—— 那假定 HEAD3 就是队首 3 条。
    #    现在 HEAD3 是"前 3 条**已有判定行**的"，它们本来就排在一批 ∞ 逾期分（从未测过）的后面。
    #    本条真正要守的是：**📝 ⛔ 不进「有效上次」⇒ 注入前后整个队列的顺序一模一样**。
    #    这比原来的"还在前 10 里"更强，也不再依赖队首长什么样。
    ck("留痕符号 📝 ⛔ 不进「有效上次」⇒ 注入前后队列顺序完全不变",
       card_order(out) == BASE_ORDER,
       [(a, b) for a, b in zip(card_order(out), BASE_ORDER) if a != b][:5])

print("\n【A2】学习日与复习日 ＝ 同一条队列、同一套排序，只差配额")
with sandbox() as d:
    rc, learn0, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True))
    rc2, rev0, _ = run(drill.cmd_pick, Args(type="review", date=DAY, dry=True))
    ck("两种日子都跑得动", rc == 0 and rc2 == 0, learn0[-300:])
    _, learn_p, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True, scope="pool"))
    _, rev_p, _ = run(drill.cmd_pick, Args(type="review", date=DAY, dry=True, scope="pool"))
    lo, ro = card_order(learn_p), card_order(rev_p)
    ck("学习日的卡片顺序 ＝ 复习日的**前缀**（同一条队列，只是学习日出得少）",
       ro[:len(lo)] == lo or lo[:len(ro)] == ro, (lo[:6], ro[:6]))
    ck("学习日在池 ≤3 组、复习日 ≤5 组",
       "上限 3 组" in learn0 and "上限 5 组" in rev0)
    ck("复检基础组：学习日 1 组、复习日 3 组",
       "基础 1 组" in learn0 and "基础 3 组" in rev0)
with sandbox(p_text=inject_today(P, set(HEAD3), DAY),
             g_text=inject_today(G, set(HEAD3), DAY)) as d:
    rc, learn1, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True, scope="pool"))
    ck("学习日同样把今天判过的移出队列",
       all(n not in card_order(learn1) for n in HEAD3), card_order(learn1)[:5])
with sandbox() as d:
    rc, learn2, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True))
    ck("学习日同日重跑逐字一致（排序是确定性的，⛔ 不再洗牌）", learn2 == learn0)


# ══════════════════════════════════════════════════════════════════════
#  A3  建号当天不回考（她 2026-09-03 定）
#  判据 ＝ 条目**第一条历史行**的日期 ＝ 今天；学习日与复习日**都**过滤。
#  ⛔ 夹具不写死编号、不写死「恰好 N 条」：从活档案按条件挑**一对**同类条目，
#     两条用**同一套构造**，只有【建号日】这一个变量不同（§0.6 夹具纪律）。
# ══════════════════════════════════════════════════════════════════════
OLD_DAY = "2026-08-20"          # 任何早于 DAY 的日子都行，只是「不是今天」


def set_history(text, num, rows):
    """把某条的 `### 历史记录` 整节换成给定的行 —— 用来造「建号日 ＝ X」这个状态。
    rows = [(日期, 符号, 场合), …]，每行都配一条缩进内容行（契约⑥）。
    ⛔ 只动这一节：状态行、四节正文、条目之间的缝（契约⑭）一个字不改，⛔ 不动任何一个数。"""
    lines = text.split("\n")
    a = None
    for i, l in enumerate(lines):
        if l.startswith("## " + num + " ") or l == "## " + num:
            a = i
        elif a is not None and l.strip() == "### 历史记录":
            b = i + 1
            e = b
            while e < len(lines) and not (re.match(r"^## #\d{4}", lines[e])
                                          or re.match(r"^# F\d\d\b", lines[e])
                                          or lines[e].strip() == "---"):
                e += 1
            seg = lines[b:e]
            nb = 0
            while nb < len(seg) and not seg[len(seg) - 1 - nb].strip():
                nb += 1
            keep = seg[len(seg) - nb:] if nb else []
            body = []
            for dt, sym, occ in rows:
                body.append("- %s %s %s" % (dt, sym, occ))
                body.append("  测试夹具的内容行。")
            return "\n".join(lines[:b] + body + keep + lines[e:])
    raise SystemExit("找不到 " + num)


print("\n【A3】建号当天不回考：第一条历史行 ＝ 今天 ⇒ 当天不进候选池")

with sandbox() as d:                                   # 按条件挑一对，⛔ 不写死编号
    _p = [e for e in drill.load_all()
          if e.in_pool and e.src == "problems.md"]
    TGT, CTL = _p[0].num, _p[1].num
    ck("前提：从活档案按条件挑到了两条【在池】的条目",
       TGT != CTL and TGT and CTL, (TGT, CTL))

# 基线：两条都造成「建号日 ＝ OLD_DAY 的③建号行」⇒ 都是 untested ⇒ 学习日两条都该在池
BOTH_OLD = set_history(set_history(P, TGT, [(OLD_DAY, "③", "夹具建号")]),
                       CTL, [(OLD_DAY, "③", "夹具建号")])
# 变量只有一个：把 TGT 的建号日挪到今天
TGT_TODAY = set_history(set_history(P, TGT, [(DAY, "③", "夹具建号")]),
                        CTL, [(OLD_DAY, "③", "夹具建号")])

with sandbox(p_text=BOTH_OLD) as d:
    rc, base_l, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True))
    ck("前提：两条建号日都不是今天 ⇒ 学习日计划里两条都在（走 untested 通道）",
       TGT in card_order(base_l) and CTL in card_order(base_l),
       (TGT in card_order(base_l), CTL in card_order(base_l)))
    # ⚠️ **2026-09-06 改**：原来断言「整段不出现」—— 那假定了**活档案里今天没有任何新建条目**。
    #    DAY 现在跟着最后一个练习日走，而练习日当天本来就会新建一批号（09-06 建了 19 条）
    #    ⇒ 这一段合法地出现了 ⇒ 假红。断言改成本条真正要守的东西：
    #    **基线里 TGT 与 CTL 都没有被当成「建号当天」挡下**。
    _seg = base_l.split("建号当天不回考")[1][:800] if "建号当天不回考" in base_l else ""
    ck("前提：基线里 TGT／CTL 都没被「建号当天」挡下",
       TGT not in _seg and CTL not in _seg, _seg[:200])

with sandbox(p_text=TGT_TODAY) as d:
    rc, out_l, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True))
    ck("退出码 0", rc == 0, out_l[-300:])
    ck("① 建号日 ＝ 今天的那条⛔不在学习日计划里", TGT not in card_order(out_l),
       card_order(out_l)[:6])
    ck("② 建号日 ≠ 今天的同类条目仍在学习日计划里", CTL in card_order(out_l),
       card_order(out_l)[:6])
    ck("③ 报告里逐条列出了被挡下的编号（⛔ 不是只报数量，§0.4）",
       "建号当天不回考" in out_l and TGT in out_l.split("建号当天不回考")[1][:400],
       [l for l in out_l.split("\n") if "建号当天" in l])
    ck("③ 被挡下的那一段写清了理由（记忆 ≠ 产出）",
       "半小时前的记忆" in out_l,
       [l for l in out_l.split("\n") if "记忆" in l])
    ck("③ 排除清单是**逐条列编号**的，⛔ 不是只报数量",
       re.search(r"⛔ 今天刚建的号 \d+ 条", out_l) is not None,
       [l for l in out_l.split("\n") if "刚建的号" in l])
    ck("⛔ 挡下的只是不出题，CTL 与 TGT 的差集恰好是这一条",
       set(card_order(base_l)) - set(card_order(out_l)) == {TGT},
       sorted(set(card_order(base_l)) - set(card_order(out_l))))

with sandbox(p_text=TGT_TODAY) as d:                   # ④ 复习日同样过滤
    rc, out_r, _ = run(drill.cmd_pick, Args(type="review", date=DAY, dry=True))
    ck("④ 复习日（--type review）同样挡下建号日 ＝ 今天的那条",
       rc == 0 and TGT not in card_order(out_r), card_order(out_r)[:6])
    ck("④ 复习日里建号日 ≠ 今天的那条仍在", CTL in card_order(out_r))
    ck("④ 复习日也逐条列了被挡下的编号",
       "建号当天不回考" in out_r and TGT in out_r.split("建号当天不回考")[1][:400],
       [l for l in out_r.split("\n") if "建号当天" in l])

# ⛔ 判据是**第一条**历史行，不是「上次」那一格（＝最后一条历史行）
LAST_TODAY = inject_row(set_history(P, CTL, [(OLD_DAY, "③", "夹具建号")]),
                        {CTL}, DAY, "📝", "夹具留痕")
with sandbox(p_text=LAST_TODAY) as d:
    _e = [x for x in drill.load_all() if x.num == CTL][0]
    ck("前提：夹具造出了「最后一条历史行 ＝ 今天、第一条 ≠ 今天」",
       _e.created_on() == OLD_DAY and _e.last_row_date() == DAY,
       (_e.created_on(), _e.last_row_date()))
    rc, out_x, _ = run(drill.cmd_pick, Args(type="learn", date=DAY, dry=True))
    ck("⛔ 不许拿最后一条历史行判：今天有留痕行、但建号日不是今天 ⇒ 照常在池",
       CTL in card_order(out_x), card_order(out_x)[:6])


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


def group_node(n=1, items=2, new_nums=None, newborn_part=True, body_nums=None):
    """new_nums = 本组在战报里【报出来】的新建编号（None ⇒ 战报写「③ 新建 无」，即没报）。
    newborn_part=False ⇒ 故意不写「新建条目的正文」子件。
    body_nums ⇒ 正文子件里实际写了哪几条（默认 ＝ 报的那些）。"""
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
          "① 一字未改率 2/2", "② 考点命中率 2/2",
          ("③ 新建 无" if not new_nums else
           "③ 本组新建  %d 条：%s（正文见下）"
           % (len(new_nums), " ".join("#" + x for x in new_nums))),
          "④ 本组毕业 无", "⑤ 今日毕业 无", ""]
    if new_nums and newborn_part:
        L += ["### 本组新建条目的正文（§4③d③）", "", FENCE]
        for x in (new_nums if body_nums is None else body_nums):
            L += ["#%s 夹具条目 %s　〔词组 · F01〕" % (x, x), "  正文一行", ""]
        L += [FENCE, ""]
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
         if e.state == "在池" and not e.is_phrase and e.trigger]
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
    # ★ 2026-09-05 梯子上线后排序变成**确定性**的（逾期分 → 掉过的 → 编号），
    #   不再洗牌、不再有「今天已判过沉底」这条特判 ⇒ 旧的"不保证逐字重现"承诺整条作废。
    ck("P1-5 复习日头部写清了排序口径（逾期分）", "逾期分" in o_r, o_r[:1200])
    ck("P1-5 学习日头部写清了排序口径（逾期分）", "逾期分" in o_l, o_l[:1200])
    ck("P1-5 头部写清了组 1 ＝ 今天最该测的", "组 1 就是今天最该测的" in o_r
       and "组 1 就是今天最该测的" in o_l, o_r[:1200])
    ck("P3-13 带 --date 时打出「⛔ 不能用来忠实回放当天的分组」",
       "不能用来忠实回放当天的分组" in o_r and "不能用来忠实回放当天的分组" in o_l)

# ══════════════════════════════════════════════════════════════════════
#  G  lookback —— §4④ 回看目标 ＝ 最近一篇【没被回看过】的新题（她 2026-09-03 定）
#  ★ 夹具纪律（SKILL §0.6）：⛔ 不写死真档案里的题号、⛔ 不写死「恰好 N 篇」——
#    session 文件全部**自己在临时目录里造**，⛔ 一个字都不碰 sessions/ 真目录。
#    断言一律是**关系式**（目标 ＝ 哪一篇 / 谁在谁不在），⛔ 不数总数。
# ══════════════════════════════════════════════════════════════════════
print("\n【G】lookback：回看目标 ＝ 最近一篇没被回看过的新题")

QA, QB, QC = "T2-91", "T1-92", "T2-93"          # 夹具自造的题号，⛔ 与真档案无关
D_OLD, D_MID, D_NEW = "2026-09-01", "2026-09-02", "2026-09-03"
LB_DAY = "2026-09-04"                            # 「今天」，三篇夹具都在它之前


def lb_dir(d):
    sd = os.path.join(d, "sessions")
    if not os.path.isdir(sd):
        os.makedirs(sd)
    return sd


def lb_session(d, day, essay=None, look="__none__"):
    """造一个 session：essay ＝ `## 新题` 节里的题号（None ⇒ 该节没有题号）；
    look ＝ `## 回看` 标题行上的题号（"" ⇒ 标题行⛔无题号；"__none__" ⇒ 没有回看节）。"""
    out = [f"# {day} · D1 · 周期 X", ""]
    if look != "__none__":
        for q in (look if isinstance(look, (list, tuple)) else [look]):
            out += [f"## 回看 · {q}（夹具）" if q else "## 回看（夹具·标题行⛔无题号）",
                    "", "（夹具正文）", ""]
    if essay is not None or look == "__none__":
        out += ["## 新题", "", "```",
                (f"{essay}　夹具题面" if essay else "（夹具：这一节⛔没有题号）"),
                "```", ""]
    out += ["## 收尾", "", "（夹具）", ""]
    p = os.path.join(lb_dir(d), f"{day}.md")
    io.open(p, "w", encoding="utf-8").write("\n".join(out))
    return p


def lb_drawn(d, rows):
    p = os.path.join(d, "drawn.log")
    io.open(p, "w", encoding="utf-8").write(
        "# 夹具流水\n" + "".join(f"{a}\t{b}\n" for a, b in rows))
    return p


def lb_scan(day=LB_DAY):
    return drill.scan_lookback(day)


def lb_run(day=LB_DAY):
    return run(drill.cmd_lookback, Args(date=day))


# ── ① 有一篇新题、没有任何回看节 ⇒ 它就是目标 ────────────────────────────
with sandbox() as d:
    lb_session(d, D_MID, essay=QA)
    sc = lb_scan()
    rc, out, _ = lb_run()
    ck("① 一篇新题 · 零回看节 ⇒ 它就是目标",
       sc["target"] and sc["target"]["qno"] == QA, sc["target"])
    ck("① 报告 ③ 块打出了这一篇（题号 ＋ 日期 ＋ session 路径）",
       rc == 0 and QA in out.split("③ ⇒ 本次该回看的")[1]
       and D_MID in out.split("③ ⇒ 本次该回看的")[1]
       and f"{D_MID}.md" in out.split("③ ⇒ 本次该回看的")[1],
       out.split("③ ⇒ 本次该回看的")[-1][:300])
    ck("① ① 块逐条列了题号 · 日期 · 出处（⛔ 不是只报数量，§0.4）",
       re.search(re.escape(QA) + r"\s+" + D_MID + r"\s+sessions/" + D_MID + r"\.md:\d+", out)
       is not None, [l for l in out.split("\n") if QA in l])

# ── ② 那一篇被带题号的 `## 回看` 标题回看过 ⇒ 目标退到更早的一篇 ────────
with sandbox() as d:
    lb_session(d, D_OLD, essay=QB)
    lb_session(d, D_MID, essay=QA)
    sc0 = lb_scan()
    ck("④ 两篇都没回看 ⇒ 取**最近**的那一篇（⛔ 不是最早的）",
       sc0["target"]["qno"] == QA, sc0["target"])
    lb_session(d, D_NEW, look=QA)          # 只回看了最近那一篇
    sc1 = lb_scan()
    ck("② 最近那篇被回看后，目标退到更早的那一篇",
       sc1["target"]["qno"] == QB, sc1["target"])
    ck("② 被回看的那篇进了 ② 块（记着在哪个 session 哪一行）",
       QA in sc1["reviewed"] and sc1["reviewed"][QA][0]["date"] == D_NEW
       and sc1["reviewed"][QA][0]["line"] > 0, sc1["reviewed"].get(QA))
    lb_session(d, D_NEW, look=[QA, QB])    # 复习日那一篇 session 里两个回看节（§8③）
    sc2 = lb_scan()
    ck("② 一篇 session 里多个 `## 回看` 节都算数（§8③ 复习日回看本周期全部新题）",
       set(sc2["reviewed"]) == {QA, QB}, sorted(sc2["reviewed"]))
    ck("② 全部回看过 ⇒ ⛔ 没有目标", sc2["target"] is None, sc2["target"])
    rc, out, _ = lb_run()
    ck("② 全部回看过 ⇒ 明确打印「全部已回看 ⇒ §4④ 本节跳过」",
       rc == 0 and "全部已回看" in out and "本节跳过" in out,
       out.split("③ ⇒ 本次该回看的")[-1][:300])

# ── ③ 标题行没题号的回看节 ⛔ 不算回看（最容易写错的一条）───────────────
with sandbox() as d:
    lb_session(d, D_MID, essay=QA)
    lb_session(d, D_NEW, look="")          # `## 回看（…）` 标题行上没有题号
    sc = lb_scan()
    rc, out, _ = lb_run()
    ck("③ 标题行⛔没题号的回看节 ⇒ 不算回看了任何一篇 ⇒ 目标仍是那一篇",
       sc["target"] and sc["target"]["qno"] == QA and not sc["reviewed"],
       (sc["target"], sc["reviewed"]))
    ck("③ 这种节被单独列出来（⛔ 不静默）",
       "标题行上没有题号" in out and f"sessions/{D_NEW}.md" in
       out.split("标题行上没有题号")[1][:400],
       [l for l in out.split("\n") if "没有题号" in l])
    # 同一个 session，只把题号加进标题行 ⇒ 立刻算回看（变量只有这一个）
    lb_session(d, D_NEW, look=QA)
    ck("③ 把题号写进标题行 ⇒ 同一个节立刻算回看（变量只有这一个）",
       lb_scan()["target"] is None and QA in lb_scan()["reviewed"])

# ── 今天自己写的那一篇⛔不作本次目标（§4④ 排在 §4⑤ 之前）────────────────
with sandbox() as d:
    lb_session(d, LB_DAY, essay=QC)        # 「今天」写的
    sc = lb_scan()
    rc, out, _ = lb_run()
    ck("⛔ 今天写的那一篇不作目标，但仍逐条列出来（⛔ 不静默丢掉）",
       sc["target"] is None and any(x["qno"] == QC for x in sc["news"]) and QC in out,
       sc["target"])
    lb_session(d, D_MID, essay=QA)
    ck("⛔ 今天那篇被跳过后，目标是它之前最近的一篇",
       lb_scan()["target"]["qno"] == QA, lb_scan()["target"])

# ── 认不出题号 ／ drawn.log 交叉核对 ／ 只读 ─────────────────────────────
with sandbox() as d:
    lb_session(d, D_MID, essay=None)       # `## 新题` 节里没有题号
    lb_drawn(d, [(D_OLD, QB), (D_MID, QA)])
    sc = lb_scan()
    rc, out, _ = lb_run()
    ck("⚠️ 认不出题号的 `## 新题` 节单独列出（⛔ 不静默丢掉）",
       len(sc["unknown"]) == 1 and sc["unknown"][0]["date"] == D_MID
       and "认不出题号" in out, sc["unknown"])
    ck("⚠️ drawn.log 里抽了、没 session 证据的题号逐条列出",
       sorted(q for _, q in sc["orphan"]) == sorted([QA, QB])
       and QA in out and QB in out, sc["orphan"])
    before = {f: os.stat(os.path.join(d, f)).st_mtime_ns
              for f in sorted(os.listdir(d)) if os.path.isfile(os.path.join(d, f))}
    bs = {f: os.stat(os.path.join(d, "sessions", f)).st_mtime_ns
          for f in sorted(os.listdir(os.path.join(d, "sessions")))}
    lb_run(); lb_run()
    after = {f: os.stat(os.path.join(d, f)).st_mtime_ns
             for f in sorted(os.listdir(d)) if os.path.isfile(os.path.join(d, f))}
    as_ = {f: os.stat(os.path.join(d, "sessions", f)).st_mtime_ns
           for f in sorted(os.listdir(os.path.join(d, "sessions")))}
    ck("⛔ lookback 只读：⛔ 没新建文件、⛔ 没改任何一个文件（含 sessions/）",
       before == after and bs == as_ and not os.path.exists(drill.DRAWN),
       (sorted(set(after) - set(before)), sorted(set(as_) - set(bs))))

# ── ⑤ pick --type learn 的头部出现那一行（与 lookback 同一个函数）────────
with sandbox() as d:
    lb_session(d, D_MID, essay=QA)
    rc, out, _ = run(drill.cmd_pick, Args(type="learn", date=LB_DAY, dry=True))
    head = out.split("候选池")[0]
    ck("⑤ pick --type learn 头部打出「★ §4④ 回看目标 ＝ <题号>（<日期>）」",
       rc == 0 and f"★ §4④ 回看目标 ＝ {QA}（{D_MID}）" in head,
       [l for l in out.split("\n") if "§4④" in l])
    ck("⑤ 那一行紧挨着 D-1／D-3 那一行（§4① 要求）",
       [l for l in head.split("\n") if "D-1 = " in l or "§4④" in l][:2][0].find("D-1 = ") >= 0
       and "§4④" in [l for l in head.split("\n") if "D-1 = " in l or "§4④" in l][1],
       [l for l in head.split("\n") if "D-1 = " in l or "§4④" in l])
    lb_session(d, D_NEW, look=QA)
    rc, out2, _ = run(drill.cmd_pick, Args(type="learn", date=LB_DAY, dry=True))
    ck("⑤ 全部回看过时，pick 头部改打「全部已回看 ⇒ 回看节跳过」",
       "★ §4④ 全部已回看 ⇒ 回看节跳过" in out2 and "回看目标 ＝" not in out2,
       [l for l in out2.split("\n") if "§4④" in l])
    ck("⑤ 复习日（--type review）⛔ 不打这一行（§4④ 是学习日流程）",
       "§4④" not in run(drill.cmd_pick, Args(type="review", date=LB_DAY, dry=True))[1])



# ══════════════════════════════════════════════════════════════════════
#  H  条件性子件「新建条目的正文」（§4③d③ / §4⑤e，她 2026-09-03 定）
#  起因：09-03 的作文节里教练只做了「对照」、⛔ 没建条目，8 件全齐 ⇒ 硬闸照样 ERROR 0。
#  ★ 夹具纪律（SKILL §0.6）：编号全部**夹具自造**（9xxx），⛔ 与真档案无关；
#    ⛔ 不写死「恰好 N 条」—— 断言一律对着**这个夹具自己报的那几条**。
# ══════════════════════════════════════════════════════════════════════
print("\n【H】deliver：报了新建就必须发「新建条目的正文」")


def nb_nums(k, base=9000):
    """夹具自造的 4 位编号，⛔ 与 problems.md 真档案无关。"""
    return ["%04d" % (base + i) for i in range(k)]


def essay_node(sents=2, new_nums=None, newborn_part=True, body_nums=None):
    """造一个 8 件齐的 `## 新题` 节（§4⑤e）。"""
    L = ["## 新题 · T2-99（测试）", "", "### 题面与条件（发给她的逐字）", "", FENCE,
         "T2-99　夹具题（⛔ 与真题库无关）", FENCE, "",
         "### 她的原文（逐句编号，逐字抄）", "", FENCE]
    L += ["S%d  Sentence %d." % (i + 1, i + 1) for i in range(sents)]
    L += [FENCE, "", "### 收稿", "", "⛔ 不设收稿闸（§4⑤b）。", "",
          "### 判分（§5 八步）", "", "| 步 | 数 |", "|---|---|",
          "| 1 | %d 句 |" % sents, "",
          "### 对照 problems.md 在池清单扫全文", "", "| 编号 | 判定 |", "|---|---|",
          "| #0001 | ✅ |", ""]
    if new_nums:
        L += ["**本篇新建  %d 条：%s（正文见下）**"
              % (len(new_nums), " ".join("#" + x for x in new_nums)), ""]
    L += ["### 三版对照块（§4⑤e，%d 块）" % sents, "", FENCE]
    for i in range(sents):
        L += ["#S%d" % (i + 1),
              "  原句　　　 Sentence %d." % (i + 1),
              "  最小修改　 〔未改〕",
              "  └ 改了什么 〔未改〕，一个字没改",
              "  更好版　　 〔没有更好的版本〕",
              "  └ 为什么好 已经到位", ""]
    L += [FENCE, "", "### 最小修改版 · 全文", "", FENCE,
          " ".join("Sentence %d." % (i + 1) for i in range(sents)), FENCE, "",
          "### 更好版 · 全文", "", FENCE,
          " ".join("Sentence %d." % (i + 1) for i in range(sents)), FENCE, ""]
    if new_nums and newborn_part:
        L += ["### 本篇新建条目的正文（§4③d③）", "", FENCE]
        for x in (new_nums if body_nums is None else body_nums):
            L += ["#%s 夹具条目 %s　〔词组 · F01〕" % (x, x), "  正文一行", ""]
        L += [FENCE, ""]
    return L


def errs_of(out):
    return [l.strip() for l in out.split("\n") if l.strip().startswith("ERROR")]


with sandbox() as d:
    # ── ① 报了新建 ＋ 有正文子件 ＋ 编号齐 ⇒ 过 ──────────────────────
    N3 = nb_nums(3)
    f = write_session(d, "2026-09-15.md", [group_node(1, new_nums=N3)])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("① 报了新建 ＋ 正文子件在 ＋ 编号齐 ⇒ ERROR 0",
       rc == 0 and "合计 ERROR 0" in out, out[-600:])
    ck("① 打出「新建条目的正文」那一行 ✔，并把报的编号逐条列出（⛔ 不只报数）",
       "新建条目的正文：报 %d 条" % len(N3) in out
       and all(("#" + x) in out for x in N3), out[-800:])

    # ── ② 报了新建、⛔ 没有正文子件 ⇒ ERROR ──────────────────────────
    f = write_session(d, "2026-09-16.md",
                      [group_node(1, new_nums=N3, newborn_part=False)])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    e = errs_of(out)
    ck("② 报了新建却没有「新建条目的正文」子件 ⇒ ERROR",
       rc == 1 and len(e) == 1 and "新建条目的正文" in e[0], out[-600:])
    ck("② 报错文案点明 §4③d③「只报编号 ＝ 没交付」＋ 报了几条",
       "§4③d③" in e[0] and "只报编号" in e[0]
       and "新建 %d 条" % len(N3) in e[0], e)
    ck("② 其余 6 件照旧全齐（⛔ 只多这一条 ERROR）",
       out.count("   ✔ 子件") == 6, [l for l in out.split("\n") if "✔ 子件" in l])

    # ── ③ 有正文子件、但少写了一条的正文 ⇒ ERROR 并点名缺的那个 ───────
    f = write_session(d, "2026-09-17.md",
                      [group_node(1, new_nums=N3, body_nums=N3[:-1])])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    e = errs_of(out)
    ck("③ 正文里少一条 ⇒ ERROR", rc == 1 and len(e) == 1, out[-600:])
    ck("③ 点名缺的正是没写正文的那一条",
       "缺这几条的正文：#%s" % N3[-1] in e[0], e)
    ck("③ ⛔ 不把已经写了正文的那几条也算成缺",
       all(("缺这几条的正文：#%s" % x) not in e[0] for x in N3[:-1]), e)

    # ── ④ 没报新建 ／ 报 0 条 ⇒ ⛔ 不要求、不报错 ─────────────────────
    f = write_session(d, "2026-09-18.md", [group_node(1)])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("④ 整节没报「新建 N 条」⇒ ⛔ 不适用（不报错、也不打那一行）",
       rc == 0 and "新建条目的正文" not in out, out[-600:])
    g0 = ["③ 本组新建  0 条" if l.startswith("③ 新建 无") else l
          for l in group_node(1)]
    f = write_session(d, "2026-09-19.md", [g0])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("④ 报「新建 0 条」⇒ ⛔ 不要求正文子件",
       rc == 0 and "新建条目的正文" not in out, out[-600:])

    # ── ⑤ 日期线：2026-09-03 之前 ⇒ 存量提示、⛔ 不 ERROR ─────────────
    blk = [group_node(1, new_nums=N3, newborn_part=False)]
    f = write_session(d, "2026-09-02.md", blk)
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("⑤ 09-03 之前缺正文子件 ⇒ 存量提示，⛔ 不报错",
       rc == 0 and "存量" in out and "新建条目的正文" in out
       and not errs_of(out), out[-700:])
    f = write_session(d, "2026-09-03.md", blk)
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("⑤ 日期线当天（2026-09-03）起就硬查",
       rc == 1 and errs_of(out), out[-600:])

    # ── ⑥ 「新题」这条路同样吃这一条（§4⑤e）────────────────────────
    N2 = nb_nums(2, 9100)
    f = write_session(d, "2026-09-20.md", [essay_node(2, new_nums=N2)])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("⑥ 新题：8 件齐 ＋ 报了新建 ＋ 正文在 ⇒ ERROR 0",
       rc == 0 and "新建条目的正文：报 %d 条" % len(N2) in out, out[-800:])
    f = write_session(d, "2026-09-21.md",
                      [essay_node(2, new_nums=N2, newborn_part=False)])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("⑥ 新题：8 件全齐、但报了新建没发正文 ⇒ 照样 ERROR（09-03 的漏洞）",
       rc == 1 and out.count("   ✔ 子件") == 8
       and any("新建条目的正文" in x for x in errs_of(out)), out[-800:])
    f = write_session(d, "2026-09-22.md", [essay_node(2)])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("⑥ 新题：没报新建 ⇒ ⛔ 不适用", rc == 0 and "新建条目的正文" not in out,
       out[-600:])

    # ── ⑦ 回看／追加练 ⛔ 不吃这一条（回看只看不做、追加练建号走 §4.8 S10）──
    look = look_node("T2-01", 2)
    look = look[:2] + ["本节新建  1 条：#%s" % nb_nums(1, 9200)[0], ""] + look[2:]
    f = write_session(d, "2026-09-23.md", [look])
    rc, out, _ = run(drill.cmd_deliver, Args(session=f))
    ck("⑦ 回看节里就算写了「新建 N 条」也⛔ 不要求正文子件",
       rc == 0 and "新建条目的正文" not in out, out[-600:])
    ck("⑦ DELIVER_SPECS 里只有「组」「复检组」「新题」挂了这一条",
       sorted(k for k, v in drill.DELIVER_SPECS.items() if v.get("newborn"))
       == sorted(["组", "复检组", "新题"]),
       sorted(k for k, v in drill.DELIVER_SPECS.items() if v.get("newborn")))


print("\n" + "═" * 70)
print(f"2026-09-02 四功能回归测试 · 通过 {len(PASS)} · 失败 {len(FAIL)}")
for f in FAIL:
    print("  ❌ " + f)
print("═" * 70)
sys.exit(1 if FAIL else 0)
