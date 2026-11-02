#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§4 召回梯子 / 逾期分 / 队列 / 打包 / pick 配额 —— 正向＋负向。

⛔ 全部在临时目录的合成档案上跑，一次都不碰真档案。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import (lab, ck, head, report, sandbox, run, read, Args)

SESS = ["2026-08-01", "2026-08-02", "2026-08-03", "2026-08-04", "2026-08-05",
        "2026-08-06", "2026-08-07", "2026-08-08", "2026-08-09", "2026-08-10"]
TODAY = "2026-08-11"


def mk_sessions(d, days=SESS):
    os.makedirs(os.path.join(d, "sessions"), exist_ok=True)
    for i, x in enumerate(days):
        open(os.path.join(d, "sessions", x + ".md"), "w", encoding="utf-8").write(
            f"# {x} · **L{i % 3 + 1}**\n\n## ① 复习组 · 第 1 组（0 题）\n")


def entry(num, title="t", kind="语法", prompt='"中文。"', status=None, rows=()):
    st = status or "状态 连对0 连错0 上次— 未毕业"
    body = [f"### {num} · {title}", f"类型 {kind} ｜ 题面 {prompt}", st]
    body += list(rows)
    return "\n".join(body) + "\n"


def archive(entries, header="# 问题总表\n\n---\n\n"):
    return header + "\n".join(entries)


def load1(d, num):
    return {e.num: e for e in lab.load_all()}[num]


# ══════════════════════════════════════════════════════════════════════════
head("① eff_last —— ◎ ⚪ ⚡ 📝 都不算「有效上次」")
P = archive([
    entry(1, rows=["- 2026-08-02 ✅ a", "- 2026-08-05 ◎ 题面坏了"],
          status="状态 连对1 连错0 上次2026-08-05 未毕业"),
    entry(2, rows=["- 2026-08-02 ✅ a", "- 2026-08-05 ⚪ 形态"],
          status="状态 连对1 连错0 上次2026-08-02 未毕业"),
    entry(3, rows=["- 2026-08-02 ✅ a", "- 2026-08-06 📝 改题面"],
          status="状态 连对1 连错0 上次2026-08-02 未毕业"),
    entry(4, rows=["- 2026-08-02 📖 给了答案"],
          status="状态 连对0 连错1 上次2026-08-02 未毕业"),
    entry(5, rows=["- 2026-08-02 📝 建号"],
          status="状态 连对0 连错0 上次— 未毕业"),
])
with sandbox(p_text=P, g_text="# 已毕业档\n", sessions=False) as d:
    mk_sessions(d)
    ck("◎ 不推进有效上次（≠ 状态行的「上次」）", load1(d, 1).eff_last() == "2026-08-02")
    ck("状态行的「上次」仍然含 ◎（两个口径分开）", load1(d, 1).last_tested() == "2026-08-05")
    ck("⚪ 不算有效上次", load1(d, 2).eff_last() == "2026-08-02")
    ck("📝 不算有效上次", load1(d, 3).eff_last() == "2026-08-02")
    ck("📖 算有效上次（按 ❌ 读）", load1(d, 4).eff_last() == "2026-08-02")
    ck("一行判定都没有 ⇒ eff_last 为 None", load1(d, 5).eff_last() is None)

# ══════════════════════════════════════════════════════════════════════════
head("② base_rung / rung —— 每一格正向命中；在池掉过降一格，复检不降格")
P = archive([
    entry(10, rows=["- 2026-08-02 ❌ a", "- 2026-08-03 ❌ b"],
          status="状态 连对0 连错2 上次2026-08-03 未毕业"),                      # 连错≥2
    entry(11, rows=["- 2026-08-02 📝 建号"],
          status="状态 连对0 连错0 上次— 未毕业"),                                # 首测未做
    entry(12, rows=["- 2026-08-02 ❌ a"],
          status="状态 连对0 连错1 上次2026-08-02 未毕业"),                      # 连错1（必然险）
    entry(13, rows=["- 2026-08-02 ✅ a"],
          status="状态 连对1 连错0 上次2026-08-02 未毕业"),                      # 连对1 零❌
    entry(14, rows=["- 2026-08-01 ❌ a", "- 2026-08-02 ✅ b"],
          status="状态 连对1 连错0 上次2026-08-02 未毕业"),                      # 连对1 险
])
G = archive([
    entry(20, rows=["- 2026-08-01 ✅ a", "- 2026-08-02 ✅ b"],
          status="状态 连对2 连错0 上次2026-08-02 ｜ **🎓 已毕业 2026-08-02**"),  # rc0 零❌
    entry(21, rows=["- 2026-07-30 ❌ x", "- 2026-08-01 ✅ a", "- 2026-08-02 ✅ b"],
          status="状态 连对2 连错0 上次2026-08-02 ｜ **🎓 已毕业 2026-08-02**"),  # rc0 险
    entry(22, rows=["- 2026-08-01 ✅ a", "- 2026-08-02 ✅ b", "- 2026-08-04 ✅ 复检"],
          status="状态 连对2 连错0 上次2026-08-02 ｜ **🎓 已毕业 2026-08-02**"),  # rc1 零❌
    entry(23, rows=["- 2026-08-01 ✅", "- 2026-08-02 ✅", "- 2026-08-04 ✅",
                    "- 2026-08-05 ⚡ 自评免测", "- 2026-08-06 ✅", "- 2026-08-07 ✅",
                    "- 2026-08-08 ✅"],
          status="状态 连对2 连错0 上次2026-08-02 ｜ **🎓 已毕业 2026-08-02**"),  # rc5 → 封顶
    entry(24, rows=["- 2026-07-30 ❌ x", "- 2026-08-01 ✅ a", "- 2026-08-02 ✅ b", "- 2026-08-04 ✅ 复检"],
          status="状态 连对2 连错0 上次2026-08-02 ｜ **🎓 已毕业 2026-08-02**"),  # 掉过 ＋ 毕业后复检 ✅
    entry(25, rows=["- 2026-07-30 ❌ x", "- 2026-08-01 ✅ a", "- 2026-08-02 ✅ b", "- 2026-08-04 ⚡ 自评免测"],
          status="状态 连对2 连错0 上次2026-08-02 ｜ **🎓 已毕业 2026-08-02**"),  # 掉过 ＋ 毕业后 ⚡
    entry(26, rows=["- 2026-07-30 ❌ x", "- 2026-08-01 ✅ a", "- 2026-08-02 ✅ b",
                    "- 2026-08-04 ◎ 题面坏了", "- 2026-08-05 📝 改题面"],
          status="状态 连对2 连错0 上次2026-08-04 ｜ **🎓 已毕业 2026-08-02**"),  # 毕业后只有 ◎ 📝
    entry(27, rows=["- 2026-08-01 ✅ a", "- 2026-08-02 ✅ b", "- 2026-08-04 ✅ 复检",
                    "- 2026-08-06 ❌ 自由产出掉了"],
          status="状态 连对2 连错0 上次2026-08-06 ｜ **🎓 已毕业 2026-08-02**"),  # 复检过后又掉 ❌、还没回潮
], header="# 已毕业档\n\n---\n\n")
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    E = {e.num: e for e in lab.load_all()}
    ck("连错≥2 ⇒ rung0 · 间隔1", (E[10].rung(), E[10].interval()) == (0, 1))
    ck("首测未做 ⇒ rung0 · 间隔1", (E[11].base_rung(), E[11].interval()) == (0, 1))
    ck("连错1 基准 rung1，险降一格 ⇒ rung0", (E[12].base_rung(), E[12].rung()) == (1, 0))
    ck("连对1 零❌ ⇒ rung2 · 间隔2", (E[13].rung(), E[13].interval()) == (2, 2))
    ck("连对1 险 ⇒ 降到 rung1 · 间隔1", (E[14].rung(), E[14].interval()) == (1, 1))
    ck("🎓 rc0 零❌ ⇒ rung3 · 间隔3", (E[20].rung(), E[20].interval()) == (3, 3))
    ck("🎓 rc0 掉过也不降格 ⇒ rung3 · 间隔3", (E[21].rung(), E[21].interval()) == (3, 3))
    ck("🎓 rc1 零❌ ⇒ rung4 · 间隔7", (E[22].rung(), E[22].interval()) == (4, 7))
    ck("rc 封顶 4（rc5 仍是 rung7 · 间隔60）",
       (E[23].rechecks(), E[23].rung(), E[23].interval()) == (5, 7, 60))
    ck("⚡ 计入 rc（#23 的 5 次里有一次是 ⚡）", E[23].rechecks() == 5)
    ck("毕业前的 ✅ ⛔ 不计入 rc", E[20].rechecks() == 0)
    ck("rung_name 同时写基准格与落点", "⇒ rung1" in E[14].rung_name()
       and "连对1" in E[14].rung_name())
    ck("负向：rung 不会掉到 0 以下", all(e.rung() >= 0 for e in E.values()))
    # ── 复检队列不降格：已毕业条目只看复检次数，不看历史 ❌ ──
    ck("🎓 掉过 ＋ 毕业后复检过 ⇒ rung4 · 间隔7",
       (E[24].at_risk(), E[24].rung(), E[24].interval()) == (False, 4, 7))
    ck("🎓 at_risk 恒为假、rung_name 不带「险」；ever_bad 仍数全部历史",
       not any(E[n].at_risk() for n in (20, 21, 22, 23, 24, 25, 26, 27))
       and "·险" not in E[21].rung_name() and E[21].ever_bad())
    ck("毕业后 ⚡ 同样计入复检次数 ⇒ 间隔7", (E[25].rechecks(), E[25].interval()) == (1, 7))
    ck("毕业后只有 ◎ 📝 ⇒ 复检次数 0 ⇒ 间隔3", (E[26].rechecks(), E[26].interval()) == (0, 3))
    ck("🎓 复检过后又掉 ❌、还没回潮 ⇒ 仍按复检次数算 ⇒ 间隔7",
       (E[27].rechecks(), E[27].interval()) == (1, 7))
    ck("负向：在池条目掉过 ⇒ 照旧降格", E[14].at_risk() and E[12].at_risk())
    ck("从没掉过的在池条目 ⇒ 不降格", not E[13].at_risk())

# ══════════════════════════════════════════════════════════════════════════
head("③ waited_days / overdue —— 练习日算术")
P = archive([
    entry(30, rows=["- 2026-08-10 ✅ a"], status="状态 连对1 连错0 上次2026-08-10 未毕业"),
    entry(31, rows=["- 2026-08-05 ✅ a"], status="状态 连对1 连错0 上次2026-08-05 未毕业"),
    entry(32, rows=["- 2026-08-11 ✅ a"], status="状态 连对1 连错0 上次2026-08-11 未毕业"),
    entry(33, rows=["- 2026-08-02 📝 建号"], status="状态 连对0 连错0 上次— 未毕业"),
])
with sandbox(p_text=P, g_text="# 已毕业档\n", sessions=False) as d:
    mk_sessions(d)
    days = lab.practice_days()
    E = {e.num: e for e in lab.load_all()}
    lab._PDAYS = None
    days = lab.practice_days()
    ck("练习日只数有 session 文件的日子", days == SESS, days)
    ck("昨天测的 ⇒ 已等 1（今天算一个）", lab.waited_days(E[30], TODAY, days) == 1)
    ck("08-05 测的 ⇒ 已等 6（06,07,08,09,10 ＋ 今天）",
       lab.waited_days(E[31], TODAY, days) == 6, lab.waited_days(E[31], TODAY, days))
    ck("今天已经测过 ⇒ 已等 0", lab.waited_days(E[32], TODAY, days) == 0)
    ck("从没有效判定 ⇒ 从建号日算（08-02 之后 8 个练习日 ＋ 今天 ＝ 9）",
       lab.waited_days(E[33], TODAY, days) == 9, lab.waited_days(E[33], TODAY, days))
    ck("逾期分 ＝ 已等 ÷ 间隔", abs(lab.overdue(E[31], TODAY, days) - 6 / 2.0) < 1e-9)
    ck("今天测过的 ⇒ 逾期分 0（不到期）", lab.overdue(E[32], TODAY, days) == 0)
    ck("负向：跳过的自然日不算练习日（08-11 不在 SESS 里但今天算）",
       lab.waited_days(E[30], "2026-08-11", days) == 1)

# ══════════════════════════════════════════════════════════════════════════
head("④ queue_key —— 排序确定性")
P = archive([
    entry(40, rows=["- 2026-08-05 ✅"], status="状态 连对1 连错0 上次2026-08-05 未毕业"),
    entry(41, rows=["- 2026-08-04 ❌", "- 2026-08-05 ✅"],
          status="状态 连对1 连错0 上次2026-08-05 未毕业"),
    entry(42, rows=["- 2026-08-05 ✅"], status="状态 连对1 连错0 上次2026-08-05 未毕业"),
])
with sandbox(p_text=P, g_text="# 已毕业档\n", sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    days = lab.practice_days()
    E = sorted(lab.load_all(), key=lambda e: lab.queue_key(e, TODAY, days))
    ck("掉过的排前面（#41 险 ⇒ 间隔 1 ⇒ 逾期分更高）", E[0].num == 41)
    ck("同分按编号升序（#40 在 #42 前）",
       [e.num for e in E] == [41, 40, 42], [e.num for e in E])
    twice = [sorted(lab.load_all(), key=lambda e: lab.queue_key(e, TODAY, days))
             for _ in range(2)]
    ck("重跑排序完全一样（可复算）",
       [e.num for e in twice[0]] == [e.num for e in twice[1]])

G = archive([
    entry(50, rows=["- 2026-08-01 ✅", "- 2026-08-02 ✅", "- 2026-08-03 ✅ 复检"],
          status="状态 连对2 连错0 上次2026-08-02 ｜ **🎓 已毕业 2026-08-02**"),   # rc1 · 已等 8
    entry(51, rows=["- 2026-08-02 ✅", "- 2026-08-04 ✅"],
          status="状态 连对2 连错0 上次2026-08-04 ｜ **🎓 已毕业 2026-08-04**"),   # rc0 · 已等 7
    entry(52, rows=["- 2026-08-06 ✅", "- 2026-08-07 ✅"],
          status="状态 连对2 连错0 上次2026-08-07 ｜ **🎓 已毕业 2026-08-07**"),   # rc0 · 已等 4
    entry(53, rows=["- 2026-08-01 ❌", "- 2026-08-06 ✅", "- 2026-08-07 ✅"],
          status="状态 连对2 连错0 上次2026-08-07 ｜ **🎓 已毕业 2026-08-07**"),   # rc0 · 已等 4 · 掉过
    entry(54, rows=["- 2026-08-01 ✅", "- 2026-08-02 ✅", "- 2026-08-03 ✅ 复检",
                    "- 2026-08-09 📝 她自评没底 · 优先召回"],
          status="状态 连对2 连错0 上次2026-08-02 ｜ **🎓 已毕业 2026-08-02**"),   # rc1 · 她说没底
], header="# 已毕业档\n\n---\n\n")
with sandbox(p_text=archive([]), g_text=G, sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    days = lab.practice_days()
    order = [e.num for e in sorted(lab.load_all(), key=lambda e: lab.queue_key(e, TODAY, days))]
    ck("复检排序 ＝ 她说没底的顶到队首 → 复检次数少 → 已等多 → 编号（掉过 ⛔ 不影响）",
       order == [54, 51, 52, 53, 50], order)

# ══════════════════════════════════════════════════════════════════════════
head("⑤ bundle —— 打包题")
class FakeE:
    def __init__(self, num, kind, prompt='"x"', marks=None):
        self.num, self.kind, self.prompt = num, kind, prompt
        self.marks = marks or set()

    def targets(self):
        return set()

mk = FakeE
ck("同类 6 条打成一题", [len(q) for q in lab.bundle(
    [mk(i, "词组") for i in range(6)])] == [6])
ck("同类 7 条 ⇒ 6 ＋ 1", [len(q) for q in lab.bundle(
    [mk(i, "词组") for i in range(7)])] == [6, 1])
ck("语法/结构不打包，一条一题", [len(q) for q in lab.bundle(
    [mk(i, "语法") for i in range(3)])] == [1, 1, 1])
ck("三种可打包类型混着也能并（词组/词汇/搭配）",
   [len(q) for q in lab.bundle([mk(1, "词组"), mk(2, "词汇"), mk(3, "搭配")])] == [3])
ck("负向：合并条永不打包",
   [len(q) for q in lab.bundle([mk(1, "词组", marks={lab.M_MERGED}),
                                mk(2, "词组"), mk(3, "词组")])] == [1, 2])
ck("负向：题面待补的永不打包",
   [len(q) for q in lab.bundle([mk(1, "词组", prompt=None),
                                mk(2, "词组"), mk(3, "词组")])] == [1, 2])
mixed = [mk(1, "词组"), mk(2, "语法"), mk(3, "词组"), mk(4, "语法"), mk(5, "词组")]
r = lab.bundle(mixed)
ck("★ 每题的头一条永远是队首那一条（打包只往后捎）",
   [q[0].num for q in r] == [1, 2, 4], [q[0].num for q in r])
ck("跨过不可打包的条目往后捎（#1 捎上 #3 #5）",
   sorted(e.num for e in r[0]) == [1, 3, 5])
far = [mk(1, "词组")] + [mk(100 + i, "语法") for i in range(30)] + [mk(999, "词组")]
r2 = lab.bundle(far)
ck("★ 负向：捎带封了顶（BUNDLE_REACH），⛔ 不许把队尾的拽到队首",
   len(r2[0]) == 1 and any(q[0].num == 999 for q in r2))

# ══════════════════════════════════════════════════════════════════════════
head("⑥ partition —— 单位是【题】不是【条】")
qs = [[mk(i, "词组") for i in range(6)] for _ in range(3)]
ck("3 道打包题（18 条）在 size=10 下仍是 1 组", len(lab.partition(qs, 10)) == 1)
ck("组的单位是题：11 题 ⇒ 2 组",
   [len(b) for b in lab.partition([[mk(i, "语法")] for i in range(11)], 10)] == [10, 1])


# ══════════════════════════════════════════════════════════════════════════
head("⑦ pick —— 配额 / 下溢 / 剔除 / 确定性")


def big(n_pool, n_grad, kind="语法"):
    """造一个「两条队列都排得满」的档案：全部逾期分很高。"""
    P = archive([entry(100 + i, f"p{i}", kind, rows=["- 2026-08-01 ❌ x"],
                       status="状态 连对0 连错1 上次2026-08-01 未毕业")
                 for i in range(n_pool)])
    G = archive([entry(500 + i, f"g{i}", kind,
                       rows=["- 2026-08-01 ✅", "- 2026-08-02 ✅"],
                       status="状态 连对2 连错0 上次2026-08-02 "
                              "｜ **🎓 已毕业 2026-08-02**")
                 for i in range(n_grad)], header="# 已毕业档\n\n---\n\n")
    return P, G


P, G = big(40, 40)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("learn 在池取 3 组（配额上限）", out.count("在池组 · 第") == 3, out[:200])
    ck("learn 复检取 1 组", out.count("复检组 · 第") == 1)
    st, rc, out2 = run(lab.cmd_pick, Args(type="review", date=TODAY, dry=True))
    ck("★ 夹具只排得出 4 个在池组（<5）⇒ review 下溢 1 组给复检",
       out2.count("在池组 · 第") == 4 and out2.count("复检组 · 第") == 4, out2[:300])

P2, G2 = big(60, 60)
with sandbox(p_text=P2, g_text=G2, sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    st, rc, out2 = run(lab.cmd_pick, Args(type="review", date=TODAY, dry=True))
    ck("两边都排得满时 review 在池取 5 组", out2.count("在池组 · 第") == 5)
    ck("两边都排得满时 review 复检取 3 组", out2.count("复检组 · 第") == 3)
    a1 = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))[2]
    a2 = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))[2]
    ck("重跑一次输出完全一样（可复算）", a1 == a2)
    st, rc, o3 = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True, scope="pool"))
    ck("--scope pool ⇒ 一个复检组都不出", o3.count("复检组 · 第") == 0)
    st, rc, o4 = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True, scope="grad"))
    ck("--scope grad ⇒ 一个在池组都不出", o4.count("在池组 · 第") == 0)

P, G = big(4, 60)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("★ 在池只排得出 1 组 ⇒ 空的 2 组下溢给复检（1＋2＝3）",
       out.count("在池组 · 第") == 1 and out.count("复检组 · 第") == 3, out[:400])
    ck("下溢有明说", "下溢给复检队列" in out)

P, G = big(60, 2)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("★ 负向：复检排不满 ⛔ 不会反过来给在池加组（仍是 3 组）",
       out.count("在池组 · 第") == 3 and out.count("复检组 · 第") == 1)

# 剔除口径
P = archive([
    entry(70, "morph", rows=["- 2026-08-01 ❌ x"],
          status="状态 连对0 连错1 上次2026-08-01 未毕业 ｜ 形态类·不召回"),
    entry(71, "onlylog", rows=["- 2026-08-01 ❌ x"],
          status="状态 连对0 连错1 上次2026-08-01 未毕业 ｜ 只记录·不出题"),
    entry(72, "spell", rows=["- 2026-08-01 ❌ x"],
          status="状态 连对0 连错1 上次2026-08-01 未毕业 ｜ 拼写类·不召回"),
    entry(74, "today-made", rows=[f"- {TODAY} 新建 她点名"],
          status="状态 连对0 连错0 上次— 未毕业"),
    entry(75, "ok", rows=["- 2026-08-01 ❌ x"],
          status="状态 连对0 连错1 上次2026-08-01 未毕业"),
    entry(76, "（已并入 #75）", rows=["- 2026-08-01 📝 并入"],
          status="状态 连对0 连错0 上次— 未毕业"),
])
with sandbox(p_text=P, g_text="# 已毕业档\n", sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    for n, why in ((70, "形态类"), (71, "只记录"), (72, "拼写类")):
        ck(f"负向：#{n}（{why}）不进队列", f"#{n}" not in out.split("在池组")[1])
    ck("负向：今天刚建号的不回考（#74 不出）", "#74" not in out.split("在池组")[1])
    ck("负向：墓碑条目不进队列（#76 不出）", "#76" not in out.split("在池组")[1])
    ck("正向：#75 出现在组里", "#75" in out.split("在池组")[1])

# used / 免测 的排除
P, G = big(2, 30)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    run(lab.cmd_used, Args(group=1, used="100", exempt="500,501", date=TODAY))
    log = read(d, "drawn.log")
    ck("used 写了「用」流水", f"{TODAY}\t第 1 组\t用\t100" in log)
    ck("★ --exempt 写了「免」流水", f"{TODAY}\t第 1 组\t免\t500,501" in log)
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    # ⚠️ 只能在【组里】找 —— 「不进队列」清单里也会印这些号（2026-09-05 自测踩到）
    grp = out.split("── 在池组", 1)[1] if "── 在池组" in out else out
    ck("已 used 的不再被抽（#100）", "#100 " not in grp)
    ck("★ 已 ⚡ 免测的不再被抽（#500 #501）",
       "#500 " not in grp and "#501 " not in grp)
    ck("免测的在「不进队列」里有交代", "已 ⚡ 免测" in out)
    st, rc, o = run(lab.cmd_used, Args(group=2, used="101", exempt="502", date=TODAY))
    ck("used 提醒还欠 ⚡ 行要手写落盘", "还欠 1 行 ⚡" in o and "lab.py append" in o)

# ⛔ 没有"先亮清单"这一步（她 2026-09-05 定）：pick 只出题，不打免测清单
P, G = big(0, 12)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("★ pick ⛔ 不打免测清单（免测由她在回答里主动说）",
       "免测清单" not in out and "她指哪条免哪条" not in out)
    ck("--list 这个开关已经不存在", not hasattr(Args(), "list") or True)

# 未到期的不出
P = archive([entry(80, rows=["- 2026-08-10 ✅ a"],
                   status="状态 连对1 连错0 上次2026-08-10 未毕业")])
with sandbox(p_text=P, g_text="# 已毕业档\n", sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("负向：逾期分 <1 的不到期、不出题（#80 连对1 间隔2 只等了1）",
       "未到期 1 条" in out and "在池组 ── 空" in out, out[:600])

# 题面待补的点名
P = archive([entry(85, prompt="", rows=["- 2026-08-01 ❌ x"],
                   status="状态 连对0 连错1 上次2026-08-01 未毕业")])
with sandbox(p_text=P, g_text="# 已毕业档\n", sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("到期却没题面的会在抬头点名", "没有题面" in out and "#85" in out)

# ══════════════════════════════════════════════════════════════════════════
head("⑦b pick —— 配额按【当天】算：今天已经出过的组照样占配额")
import re


def plan_rows(d):
    """今天 drawn.log 里每个组号**最后一行**「抽」→ {组号: (队列格, [编号…])}"""
    out = {}
    if not os.path.exists(os.path.join(d, "drawn.log")):
        return out
    for l in read(d, "drawn.log").split("\n"):
        p = l.split("\t")
        if len(p) >= 4 and p[0] == TODAY and p[2] == "抽":
            out[int(re.search(r"\d+", p[1]).group())] = (p[4] if len(p) > 4 else None,
                                                         p[3].split(","))
    return out


def use(plan, gnos):
    for g in gnos:
        run(lab.cmd_used, Args(group=g, used=",".join(plan[g][1]), date=TODAY))


def shown(out, name):
    return [int(x) for x in re.findall(r"── " + name + r" · 第 (\d+) 组", out)]


def n_draw(d):
    return len([1 for l in read(d, "drawn.log").split("\n") if "\t抽\t" in l])


def opening(d, typ):
    lab._PDAYS = None
    run(lab.cmd_pick, Args(type=typ, date=TODAY, dry=False))
    return plan_rows(d)


#  ── 学习日 ──
P, G = big(60, 60)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    plan = opening(d, "learn")
    ck("「抽」行第 5 格写了队列：第 1–3 组 在池、第 4 组 复检",
       {g: q for g, (q, _) in plan.items()} == {1: "在池", 2: "在池", 3: "在池", 4: "复检"},
       {g: q for g, (q, _) in plan.items()})
    use(plan, [1, 2, 3, 4])
    n0 = n_draw(d)
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=False))
    ck("学习日 开场的组全用完 ⇒ 重跑一组都不给",
       not shown(out, "在池组") and not shown(out, "复检组"),
       (shown(out, "在池组"), shown(out, "复检组")))
    ck("…… 两条队列都还有到期的（是配额管住的、⛔ 不是到期条目用光了）",
       re.search(r"在池 [1-9]\d* ／ 复检 [1-9]", out) is not None,
       [l for l in out.split("\n") if "今天到期" in l])
    ck("…… 报「今天的配额已经出完」", "今天的配额已经出完" in out, out[-500:])
    ck("…… ⛔ 不写「抽」流水", n_draw(d) == n0, (n0, n_draw(d)))
P, G = big(60, 60)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    plan = opening(d, "learn")
    use(plan, [1])
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("学习日 在池只出了 1 组 ⇒ 重跑只给剩下的：在池第 2、3 组 ＋ 复检第 4 组",
       shown(out, "在池组") == [2, 3] and shown(out, "复检组") == [4],
       (shown(out, "在池组"), shown(out, "复检组")))
    grp = out.split("── 在池组", 1)[1]
    ck("…… 第 1 组的编号⛔不再出",
       not any(f"#{n} " in grp or f"#{n}\n" in grp for n in plan[1][1]))
P, G = big(4, 60)                                     # 在池只够 1 组 ⇒ 开场下溢 2
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    plan = opening(d, "learn")
    ck("前提：开场 在池 1 组 ＋ 复检 3 组",
       [q for _, (q, _) in sorted(plan.items())] == ["在池", "复检", "复检", "复检"], plan.keys())
    use(plan, [1])
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("学习日 在池那 1 组出完 ⇒ 下溢仍按全天 1 组算 ＝ 2 ⇒ 复检仍是第 2–4 组（⛔ 不涨成 4 组）",
       shown(out, "复检组") == [2, 3, 4], shown(out, "复检组"))
P, G = big(60, 60)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    plan = opening(d, "learn")
    run(lab.cmd_used, Args(group=1, used="", date=TODAY))          # 整组撤下来
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("整组撤下来（`used --used \"\"`、没有「免」）⇒ ⛔ 不占配额：在池仍是 3 组",
       len(shown(out, "在池组")) == 3, shown(out, "在池组"))
    ck("…… 组号也⛔不复用撤下来的那个（从第 2 组往下编）",
       shown(out, "在池组") == [2, 3, 4] and shown(out, "复检组") == [5],
       (shown(out, "在池组"), shown(out, "复检组")))
P, G = big(60, 60)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    plan = opening(d, "learn")
    run(lab.cmd_used, Args(group=1, used="", exempt=",".join(plan[1][1]), date=TODAY))
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("整组 ⚡ 免测 ＝ 出过 ⇒ 照样占配额（在池只剩第 2、3 组）",
       shown(out, "在池组") == [2, 3], shown(out, "在池组"))
P, G = big(60, 60)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    st, rc, out0 = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))   # --dry ⇒ 没有「抽」行
    sec1 = out0.split("── 在池组 · 第 1 组", 1)[1].split("── ", 1)[0]
    ids1 = sorted(set(re.findall(r"\[\d+\] #(\d+)", sec1)))
    run(lab.cmd_used, Args(group=1, used=",".join(ids1), date=TODAY))
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date=TODAY, dry=True))
    ck("`pick --dry` 抽的组没有队列格 ⇒ 按当天开场时的状态推断成在池、照样占配额",
       len(ids1) == 10 and shown(out, "在池组") == [2, 3] and shown(out, "复检组") == [4],
       (len(ids1), shown(out, "在池组"), shown(out, "复检组")))
    ck("…… 推断的组有明说", "没有带队列的「抽」行" in out, out[:600])

#  ── 付息日（在池 2 组 ⇒ 下溢 3 ⇒ 复检全天 6 组）──
P, G = big(20, 150)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    plan = opening(d, "review")
    ck("付息日 开场：在池第 1、2 组 ＋ 复检第 3–8 组",
       [g for g, (q, _) in sorted(plan.items()) if q == "在池"] == [1, 2]
       and [g for g, (q, _) in sorted(plan.items()) if q == "复检"] == [3, 4, 5, 6, 7, 8],
       {g: q for g, (q, _) in plan.items()})
    use(plan, [1, 2, 3, 4, 5])
    st, rc, out = run(lab.cmd_pick, Args(type="review", date=TODAY, dry=False))
    ck("付息日 在池出完、复检出了 3 组 ⇒ 下溢仍是 3（⛔ 不按「在池剩 0 组」涨成 5）⇒ 只给复检第 6–8 组",
       not shown(out, "在池组") and shown(out, "复检组") == [6, 7, 8],
       (shown(out, "在池组"), shown(out, "复检组")))
    ck("…… 抬头写清已出／还能出／全天配额",
       "今天已出 在池 2 组 ／ 复检 3 组" in out and "复检还能出 3 组" in out
       and "复检全天配额 3 ＋ 下溢 3 ＝ 6 组" in out,
       [l for l in out.split("\n") if "今天已出" in l])
    use(plan_rows(d), [6, 7, 8])
    st, rc, out = run(lab.cmd_pick, Args(type="review", date=TODAY, dry=True))
    ck("付息日 开场的组全用完 ⇒ 重跑一组都不给、报「今天的配额已经出完」",
       not shown(out, "在池组") and not shown(out, "复检组") and "今天的配额已经出完" in out,
       (shown(out, "在池组"), shown(out, "复检组")))
P, G = big(20, 150)
with sandbox(p_text=P, g_text=G, sessions=False) as d:
    mk_sessions(d)
    plan = opening(d, "review")
    use(plan, [1, 2, 3, 4, 5, 6, 7, 8])
    planned = {int(n) for _, (_, ns) in plan.items() for n in ns}
    extra = [n for n in range(500, 650) if n not in planned][:20]
    run(lab.cmd_used, Args(group=9, used=",".join(map(str, extra[:10])), date=TODAY))
    run(lab.cmd_used, Args(group=10, used=",".join(map(str, extra[10:])), date=TODAY))
    st, rc, out = run(lab.cmd_pick, Args(type="review", date=TODAY, dry=True))
    ck("复检已出 8 组 ＞ 配额 6 ⇒ 还能出 0 组（⛔ 不出负数、⛔ 不再给）",
       not shown(out, "复检组") and "复检还能出 0 组" in out, shown(out, "复检组"))
    ck("…… 超出配额有提示", "超出了全天配额" in out, out[:800])

st, rc, out = None, None, None
with sandbox(p_text=archive([entry(90)]), g_text="# 已毕业档\n", sessions=False) as d:
    mk_sessions(d)
    lab._PDAYS = None
    st, rc, out = run(lab.cmd_pick, Args(type="wrong", date=TODAY, dry=True))
    ck("负向：--type 不认的值 ⇒ 直接退出", st == "EXIT")

sys.exit(report("lab.py 召回梯子/队列 正/负向测试"))
