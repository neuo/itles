#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""退池（SKILL §3.6）的正向／负向对抗测试。

退池 ＝ 测不出缺口的条目永不出题：不进召回队列 · 不算可出题 · 题面节不要求引号句；
理由必须留一行 📝；退池条目上记 ✅❌⚡ ⇒ append 拒绝（先撤销退池）。
⛔ 夹具全部自带，一个字不来自真档案。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, read, lab

HDR = "# 问题总表\n\n---\n\n"
GHDR = "# 已毕业档\n\n---\n\n"


def ent(num, status, rows, prompt='"他把桌上收拾了。"（"收拾"用 **clear** 说）'):
    return (f"### {num} · 夹具 {num}\n类型 搭配 ｜ 新建 2026-09-01\n{status}\n\n"
            f"**问题是什么**\n规则。\n\n**怎么发现的**\n夹具。\n\n**我错在哪**\n她的 vs 正确。找法：先问一句。\n\n"
            f"**题面**\n{prompt}\n\n" + "\n".join(rows) + "\n\n---\n\n")


RET_G = ent(9701, "状态 连对2 连错0 上次2026-09-03 ｜ **🎓 已毕业 2026-09-03** ｜ 退池 ｜ 题型 整句",
            ["- 2026-09-01 ✅ a", "- 2026-09-03 ✅ b",
             "- 2026-09-20 📝 退池 · 目标版只是同级说法，中译英里产不出 ❌"],
            prompt="（退池 · 不出题）")
RET_P = ent(9702, "状态 连对0 连错1 上次2026-09-03 未毕业 ｜ 退池 ｜ 题型 整句",
            ["- 2026-09-03 ❌ a", "- 2026-09-20 📝 退池 · 考点只在整段里现形"])
LIVE = ent(9703, "状态 连对0 连错1 上次2026-09-03 未毕业 ｜ 题型 整句", ["- 2026-09-03 ❌ a"])
NOWHY = ent(9704, "状态 连对0 连错1 上次2026-09-03 未毕业 ｜ 退池 ｜ 题型 整句", ["- 2026-09-03 ❌ a"])


def E():
    return {e.num: e for e in lab.load_all()}


def errs(num, lv="ERROR"):
    es = lab.load_all()
    e = [x for x in es if x.num == num][0]
    return [m for l, m in lab.check_entry(e, set(), {x.num for x in es}) if l == lv]


head("【R1 正】退池条目：不进召回队列、不算可出题、题面节写说明不报错")
with sandbox(p_text=HDR + RET_P + LIVE, g_text=GHDR + RET_G, sessions=False) as d:
    es = E()
    ck("解析出退池标记", lab.M_RETIRED in es[9701].marks and lab.M_RETIRED in es[9702].marks)
    ck("🎓 退池 ⇒ ⛔ 不进召回队列", not es[9701].recallable)
    ck("未毕业退池 ⇒ ⛔ 不可出题、⛔ 不进召回队列", not es[9702].drawable and not es[9702].recallable)
    ck("对照：没退池的照常可出题", es[9703].drawable and es[9703].recallable)
    ck("block_reason ＝ 退池", es[9702].block_reason == lab.M_RETIRED, es[9702].block_reason)
    ck("题面节只写说明（无引号句）⇒ ⛔ 不报错", not errs(9701), errs(9701))
    ck("有 📝 退池理由 ⇒ ERROR 0", not errs(9702), errs(9702))
    st, rc, out = run(lab.cmd_count, Args(type="retired", detail=False))
    ck("count --type retired 列出两条", "#9701" in out and "#9702" in out and "#9703" not in out, out[-300:])
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date="2026-09-30", dry=True))
    ck("pick 把它们列进「⛔ 不进队列 · 退池」", "退池" in out and "9702" in out, out[:900])
    ck("pick 照常出没退池的那条", "#9703" in out, out[-900:])

head("【R2 负】标了退池却没写理由 ⇒ ERROR")
with sandbox(p_text=HDR + NOWHY, g_text=GHDR, sessions=False) as d:
    ck("缺 📝 退池 理由行 ⇒ ERROR", any("理由必须留档" in m for m in errs(9704)), errs(9704))

head("【R3 负】退池条目上记判定 ⇒ append 拒绝（先撤销退池）")
with sandbox(p_text=HDR + RET_P, g_text=GHDR, sessions=False) as d:
    p0 = read(d, "problems.md")
    f = os.path.join(d, "rows.md")
    open(f, "w", encoding="utf-8").write("#9702 ❌ 新题自由产出 · 夹具\n  又掉了\n")
    st, rc, out = run(lab.cmd_append, Args(file=f, date="2026-09-25", dry_run=False))
    ck("被拒（非 0）且说清先撤销退池", (st == "EXIT" or rc == 1) and "撤销退池" in out, (st, rc, out[-300:]))
    ck("档案一个字没动", read(d, "problems.md") == p0)
    open(f, "w", encoding="utf-8").write("#9702 📝 撤销退池 · 夹具\n  自由产出里又掉了\n")
    st, rc, out = run(lab.cmd_append, Args(file=f, date="2026-09-25", dry_run=False))
    ck("★ 📝 留痕行照常能记（撤销退池那一行就走它）", (st, rc) == ("OK", 0), out[-300:])

sys.exit(report("lab.py 退池 正/负向测试"))
