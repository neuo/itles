#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py count 的正向／负向对抗测试。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import (ck, head, report, Args, sandbox, run, read, lab, LAB, Counter)

P0 = open(os.path.join(LAB, "problems.md"), encoding="utf-8").read()

head("【C0 正】口径自洽 —— 相加必须等于全档")
with sandbox() as d:
    ents = lab.load_all()
    live = [e for e in ents if not e.tomb]
    st, rc, out = run(lab.cmd_count, Args())
    ck("退出码 0", (st, rc) == ("OK", 0), out[:200])
    ck("grad ＋ ungrad ＝ 全档（墓碑不占数）",
       sum(1 for e in live if e.graduated) + sum(1 for e in live if not e.graduated) == len(live))
    ck("墓碑不进 live", all(not e.tomb for e in live))
    ck("全表把 tomb 单列且不计入全档",
       re.search(r"^tomb\s+墓碑/迁出\s+(\d+)", out, re.M).group(1) == str(len(ents) - len(live)),
       out[:0])

head("【C1 正】每个 slug 的数与逐条手算一致")
with sandbox() as d:
    ents = lab.load_all()
    live = [e for e in ents if not e.tomb]
    ug = [e for e in live if not e.graduated]
    for t in lab.TYPES:
        slug, name, rule, pred = t[0], t[1], t[2], t[3]
        pool = ents if len(t) > 4 and t[4] else live
        want_all = sum(1 for e in pool if pred(e))
        want_ug = sum(1 for e in ug if pred(e))
        st, rc, out = run(lab.cmd_count, Args(type=slug))
        m = re.search(r"\*\*全档 (\d+) 条\*\*（其中\*\*未毕业 (\d+) 条\*\*）", out)
        ck(f"--type {slug} 的两个数与手算一致",
           bool(m) and (int(m.group(1)), int(m.group(2))) == (want_all, want_ug),
           (m.groups() if m else out[:150], want_all, want_ug))

head("【C2 正】kind: 动态 slug ＋ --detail")
with sandbox() as d:
    live = [e for e in lab.load_all() if not e.tomb]
    kinds = sorted({e.kind for e in live if e.kind})
    ck(f"认出 {len(kinds)} 个类型 {kinds}", len(kinds) >= 5)
    for k in kinds:
        st, rc, out = run(lab.cmd_count, Args(type="kind:" + k))
        want = sum(1 for e in live if e.kind == k)
        ck(f"kind:{k} 数对", f"全档 {want} 条" in out, out[:150])
    st, rc, out = run(lab.cmd_count, Args(type="drawable", detail=True))
    ck("--detail 逐条打印且行数 ＝ 条数",
       len([l for l in out.split("\n") if l.startswith("  #")]) ==
       sum(1 for e in live if e.drawable))

head("【C3 正】清单里的编号 ＝ predicate 选出来的编号")
with sandbox() as d:
    live = [e for e in lab.load_all() if not e.tomb]
    for slug in ("drawable", "streak1", "bad2+", "prompt-todo", "never"):
        st, rc, out = run(lab.cmd_count, Args(type=slug))
        got = {int(x) for x in re.findall(r"#(\d+)", out)}
        pred = lab.TYPE_MAP[slug][3]
        want = {e.num for e in live if pred(e)}
        ck(f"{slug} 的编号清单与 predicate 一致", got == want,
           (sorted(got ^ want)[:6]))

head("【C4 负】乱编类型名 ⇒ 退出并说清不许发明")
with sandbox() as d:
    for bogus in ("在池", "essay", "fam:F08", "kind", "ASK"):
        st, rc, out = run(lab.cmd_count, Args(type=bogus))
        ck(f"--type {bogus} 被拒", st == "EXIT",
           (st, rc, out[-120:]))
        ck(f"--type {bogus} 的报错说清了口径", "不认识的类型" in out or "不许临时发明" in out,
           out[-160:])

head("【C5 负】kind: 后面跟不存在的类型 ⇒ 0 条（不炸，但也不含糊）")
with sandbox() as d:
    st, rc, out = run(lab.cmd_count, Args(type="kind:不存在的类型"))
    ck("退出码 0", (st, rc) == ("OK", 0))
    ck("报 0 条", "全档 0 条" in out, out[:200])

head("【C6 负】grep 数条目一定会错 —— 这就是 count 存在的理由")
# ⚠️ 用**合成档案**，⛔ 不再拿真档案的墓碑当证据：2026-09-05 墓碑整类废除之后
#   那个分歧源没了，测试当场变成假失败。围栏里的 `###` 是仍然活着的分歧源。
P_TRAP = ("# 问题总表\n\n---\n\n"
          "### 1 · 真条目\n类型 语法 ｜ 题面 \"中文。\"\n"
          "状态 连对0 连错1 上次2026-09-01 未毕业\n- 2026-09-01 ❌ x\n"
          "- 备注 举个例子说明格式：\n"
          "```\n### 999 · 这行在围栏里，⛔ 不是条目\n状态 连对2 连错0 上次2026-09-01 ｜ **🎓 已毕业 2026-09-01**\n```\n")
with sandbox(p_text=P_TRAP, g_text="# 已毕业档\n") as d:
    txt = read(d, "problems.md")
    grep_total = len(re.findall(r"^### ", txt, re.M))
    grep_grad = len(re.findall(r"^状态.*🎓", txt, re.M))
    live = [e for e in lab.load_all() if not e.tomb]
    real_grad = sum(1 for e in live if e.graduated)
    real_ungrad = len(live) - real_grad
    ck(f"grep 数出 {grep_total} 个条目头，真值 {len(live)} —— 围栏里的也被数了",
       grep_total == 2 and len(live) == 1, (grep_total, len(live)))
    ck(f"grep 数出 {grep_grad} 个 🎓，真值 {real_grad}",
       grep_grad == 1 and real_grad == 0, (grep_grad, real_grad))
    # ★ 这个例子里两个 grep 各错各的（2 vs 1、1 vs 0），**差值凑巧对上** ——
    #   比直接报错更危险：它看起来是对的。⇒ 判据只能是"每个数各自对不对"，
    #   ⛔ 不能拿"减出来的数看着合理"当验证。
    ck("★ 两个 grep 各自都错，差值却凑巧对上 —— 看起来对的数最危险",
       grep_total != len(live) and grep_grad != real_grad
       and grep_total - grep_grad == real_ungrad)
    st, rc, out = run(lab.cmd_count, Args())
    ck("count 报的是真值 1 条", "全档 1 条" in out, out[:200])

head("【C7 负】墓碑不许混进任何出题口径")
with sandbox() as d:
    for slug in ("drawable", "streak0", "streak1", "ungrad"):
        pred = lab.TYPE_MAP[slug][3]
        leak = [e.num for e in lab.load_all() if e.tomb and pred(e)]
        st, rc, out = run(lab.cmd_count, Args(type=slug))
        shown = {int(x) for x in re.findall(r"#(\d+)", out)}
        tombs = {e.num for e in lab.load_all() if e.tomb}
        ck(f"{slug} 的清单里没有墓碑", not (shown & tombs), sorted(shown & tombs)[:5])

sys.exit(report("lab.py count 正/负向测试"))
