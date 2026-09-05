#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py check 的契约⑤（条目内顺序）正向／负向对抗测试。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, read, lab, LAB

P0 = open(os.path.join(LAB, "problems.md"), encoding="utf-8").read()


def errs_of(num):
    ents = lab.load_all()
    nums = {e.num for e in ents}
    e = [x for x in ents if x.num == num][0]
    return [m for lv, m in lab.check_entry(e, set(), nums) if lv == "ERROR"]


def span(text, num):
    lines = text.split("\n")
    a = b = None
    fence = False
    for i, l in enumerate(lines):
        if l.lstrip().startswith("```"):
            fence = not fence; continue
        if fence or not lab.RE_ENTRY.match(l): continue
        if a is None and int(lab.RE_ENTRY.match(l).group(1)) == num: a = i
        elif a is not None: b = i; break
    return lines, a, (b if b is not None else len(lines))


# 挑一条结构标准的未毕业条目当样本
_S = None
for e in lab.parse_file(os.path.join(LAB, "problems.md"), "problems.md"):
    if e.status_raw and e.kind and len(e.history) >= 2 and not e.tomb:
        _S = e.num; break

head("【K0 正】干净档案 ⇒ check 零违规")
# ⚠️ 用**合成**的干净档案，⛔ 不对真档案断言 —— 真档案的 ERROR 数是"今天干得怎么样"，
#   不是"checker 对不对"。2026-09-05 实证：一次合法的回潮就能把它打红 3 处，
#   而 §0.1.6 会因此把 lab.py 锁死。档案健康度归 §11③ C0 管（收尾时跑 check --all）。
P_CLEAN = ("# 问题总表\n\n---\n\n"
           "### 9001 · 干净的在池条目\n"
           "类型 语法 ｜ 题面 \"中文。\" ｜ 新建 2026-09-01\n"
           "状态 连对1 连错0 上次2026-09-03 未毕业\n"
           "- 2026-09-01 ❌ 首犯\n- 2026-09-03 ✅ 复习\n")
G_CLEAN = ("# 已毕业档\n\n---\n\n"
           "### 9002 · 干净的毕业条目\n"
           "类型 词组 ｜ 题面 \"中文。\" ｜ 新建 2026-09-01\n"
           "状态 连对2 连错0 上次2026-09-03 ｜ **🎓 已毕业 2026-09-03**\n"
           "- 2026-09-01 ✅\n- 2026-09-03 ✅\n")
with sandbox(p_text=P_CLEAN, g_text=G_CLEAN) as d:
    st, rc, out = run(lab.cmd_check, Args(all=True, changed=False))
    ck("干净档案 check --all ERROR 0", "ERROR 0" in out, out[-400:])
with sandbox() as d:
    bad = []
    for e in lab.load_all():
        if any("契约⑤" in m for m in
               [x[1] for x in lab.check_entry(e, set(), {y.num for y in lab.load_all()})]):
            bad.append(e.num)
    ck("全档没有契约⑤ 违规", not bad, bad[:6])

head(f"【K1 负】把状态行埋进日志行中间（样本 #{_S}）")
with sandbox() as d:
    lines, a, b = span(P0, _S)
    si = next(i for i in range(a, b) if lab.RE_STATUS.match(lines[i]))
    hi = next(i for i in range(a, b) if lab.RE_HIST.match(lines[i]))
    st_line = lines.pop(si)
    lines.insert(hi + 1, st_line)                     # 塞到第一条日志行之后
    open(lab.PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))
    e = errs_of(_S)
    ck("⇒ ERROR 且点名契约⑤", any("契约⑤" in m and "顺序不对" in m for m in e), e[:3])

head(f"【K2 负】元信息排到状态行之后（样本 #{_S}）")
with sandbox() as d:
    lines, a, b = span(P0, _S)
    mi = next(i for i in range(a, b) if lab.RE_META.match(lines[i]))
    si = next(i for i in range(a, b) if lab.RE_STATUS.match(lines[i]))
    lines[mi], lines[si] = lines[si], lines[mi]
    open(lab.PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))
    e = errs_of(_S)
    ck("⇒ ERROR 且点名契约⑤", any("契约⑤" in m for m in e), e[:3])

head(f"【K3 负】日期行写在 `- 备注` 之后（样本 #{_S}）")
with sandbox() as d:
    lines, a, b = span(P0, _S)
    hi = max(i for i in range(a, b) if lab.RE_HIST.match(lines[i]))
    lines.insert(hi + 1, "- 备注 测试用")
    lines.insert(hi + 2, "- 2026-09-30 ✅ 测试用日志行")
    open(lab.PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))
    e = errs_of(_S)
    ck("⇒ ERROR 且点名「写在 `- 备注` 之后」", any("备注" in m and "契约⑤" in m for m in e), e[:3])

head(f"【K4 负】历史行日期乱序（样本 #{_S}）")
with sandbox() as d:
    lines, a, b = span(P0, _S)
    hs = [i for i in range(a, b) if lab.RE_HIST.match(lines[i])]
    lines[hs[0]], lines[hs[-1]] = lines[hs[-1]], lines[hs[0]]
    open(lab.PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))
    e = errs_of(_S)
    ck("⇒ ERROR 且点名日期乱序", any("日期乱序" in m for m in e), e[:3])

head("【K5 正】墓碑条目不查顺序（它们本来就没有状态行）")
with sandbox() as d:
    tombs = [e for e in lab.load_all() if e.tomb]
    ck(f"{len(tombs)} 条墓碑一条 ERROR 都不报",
       all(not lab.check_entry(e, set(), {x.num for x in lab.load_all()}) for e in tombs))

sys.exit(report("lab.py check 契约⑤ 正/负向测试"))
