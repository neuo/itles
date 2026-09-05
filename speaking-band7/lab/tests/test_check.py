#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py check 的契约⑤（条目内顺序）正向／负向对抗测试。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, read, lab, LAB

# ══════════════════════════════════════════════════════════════════════════
#  ⛔ 自带夹具：一个字都不来自真 problems.md／graduated.md。
#     2026-09-05 教训（test_prompts 那 4 条红）：把判据挂在真档案此刻的内容上，
#     生产数据一整改就把测试踩空 —— 红的是夹具，脚本一行都没错。
# ══════════════════════════════════════════════════════════════════════════
_S = 9101                                   # K1–K4 的样本条目（结构标准、两条日志）
P0 = ("# 问题总表\n\n---\n\n"
      f"### {_S} · 结构标准的样本条目\n"
      "类型 语法 ｜ 题面 \"我昨天去了图书馆。\" ｜ 新建 2026-09-01\n"
      "状态 连对1 连错0 上次2026-09-03 未毕业\n"
      "- 2026-09-01 ❌ 首犯 · 夹具\n"
      "  `i go to library yesterday.`\n"
      "  → I went to the library yesterday.\n"
      "- 2026-09-03 ✅ 复习 · 夹具\n")
G0 = "# 已毕业档\n"


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

head("【K0b 正】一整批**合法形状**的条目 ⇒ checker 一条都不许误伤")
# ⚠️ 2026-09-05 改：原来这里对**真档案**断言"全档没有契约⑤ 违规"。
#   那验的是"今天档案干净不干净"，不是"checker 对不对" —— 与本文件 K0 上面那段
#   已经下过的裁决同一条口径（§0.1.6 会因此把 lab.py 锁死）。档案健康度归 §11③ C0
#   收尾时跑 `lab.py check --all` 管。⇒ 这里换成自带语料：合法写法各造一条。
# ⚠️ 已知缺口（⛔ 未修，见交接）：正文里的**围栏内**若有形似日期行的内容，
#   check_entry 的契约⑤ 循环直接扫 e.raw、不认围栏（parse_file 是认的），会假报
#   "日期行写在 `- 备注` 之后"。所以下面的语料**故意不含围栏**，⛔ 不在这里把 bug 焊死。
SHAPES = [
    ("标准形状（头→元信息→状态→两条日志）",
     "### 9201 · 标准形状\n类型 语法 ｜ 题面 \"中文。\" ｜ 新建 2026-09-01\n"
     "状态 连对1 连错0 上次2026-09-03 未毕业\n- 2026-09-01 ❌ a\n- 2026-09-03 ✅ b\n"),
    ("日志带缩进续行与 ★ 注释行",
     "### 9202 · 缩进续行\n类型 词组 ｜ 题面 \"中文。\" ｜ 新建 2026-09-01\n"
     "状态 连对0 连错1 上次2026-09-01 未毕业\n- 2026-09-01 ❌ a\n"
     "  `her sentence`\n  → the fix\n  ★ 归因写在这里\n"),
    ("末尾有 `- 备注` 块（日志全在备注之前）",
     "### 9203 · 备注块\n类型 搭配 ｜ 题面 \"中文。\" ｜ 新建 2026-09-01\n"
     "状态 连对1 连错0 上次2026-09-03 未毕业\n- 2026-09-01 ❌ a\n- 2026-09-03 ✅ b\n"
     "- 备注 这一族的口径写在这里\n  第二行备注\n"),
    ("`- 判重结论` 块",
     "### 9204 · 判重结论\n类型 词汇 ｜ 题面 \"中文。\" ｜ 新建 2026-09-01\n"
     "状态 连对1 连错0 上次2026-09-03 未毕业\n- 2026-09-01 ❌ a\n- 2026-09-03 ✅ b\n"
     "- 判重结论 与 #9201 不同族\n"),
    ("同一天两条日志（§3.3 各记一次）",
     "### 9205 · 同日两次\n类型 结构 ｜ 题面 \"中文。\" ｜ 新建 2026-09-01\n"
     "状态 连对1 连错0 上次2026-09-04 未毕业\n- 2026-09-04 ❌ 第一次\n- 2026-09-04 ✅ 第二次\n"),
]
G_SHAPE = ("# 已毕业档\n\n---\n\n### 9301 · 已毕业条目\n"
           "类型 词组 ｜ 题面 \"中文。\" ｜ 新建 2026-09-01\n"
           "状态 连对2 连错0 上次2026-09-03 ｜ **🎓 已毕业 2026-09-03**\n"
           "- 2026-09-01 ✅\n- 2026-09-03 ✅\n")
with sandbox(p_text="# 问题总表\n\n---\n\n" + "\n---\n\n".join(x[1] for x in SHAPES),
             g_text=G_SHAPE, sessions=False) as d:
    ents = lab.load_all()
    nums = {e.num for e in ents}
    ck(f"语料覆盖 {len(SHAPES)+1} 种合法形状（⛔ 语料空了这两发就是空转）",
       len(ents) == len(SHAPES) + 1, sorted(e.num for e in ents))
    v5 = {e.num: [m for _, m in lab.check_entry(e, set(), nums) if "契约⑤" in m] for e in ents}
    ck("合法形状一条契约⑤ 都不报", not any(v5.values()), {k: v for k, v in v5.items() if v})
    allp = {e.num: lab.check_entry(e, set(), nums) for e in ents}
    ck("★ 而且整体一条 ERROR 都不报（语料自己得是干净的）",
       not any(p for p in allp.values()), {k: v for k, v in allp.items() if v})

head(f"【K1 负】把状态行埋进日志行中间（样本 #{_S}）")
with sandbox(p_text=P0, g_text=G0, sessions=False) as d:
    lines, a, b = span(P0, _S)
    si = next(i for i in range(a, b) if lab.RE_STATUS.match(lines[i]))
    hi = next(i for i in range(a, b) if lab.RE_HIST.match(lines[i]))
    st_line = lines.pop(si)
    lines.insert(hi + 1, st_line)                     # 塞到第一条日志行之后
    open(lab.PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))
    e = errs_of(_S)
    ck("⇒ ERROR 且点名契约⑤", any("契约⑤" in m and "顺序不对" in m for m in e), e[:3])

head(f"【K2 负】元信息排到状态行之后（样本 #{_S}）")
with sandbox(p_text=P0, g_text=G0, sessions=False) as d:
    lines, a, b = span(P0, _S)
    mi = next(i for i in range(a, b) if lab.RE_META.match(lines[i]))
    si = next(i for i in range(a, b) if lab.RE_STATUS.match(lines[i]))
    lines[mi], lines[si] = lines[si], lines[mi]
    open(lab.PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))
    e = errs_of(_S)
    ck("⇒ ERROR 且点名契约⑤", any("契约⑤" in m for m in e), e[:3])

head(f"【K3 负】日期行写在 `- 备注` 之后（样本 #{_S}）")
with sandbox(p_text=P0, g_text=G0, sessions=False) as d:
    lines, a, b = span(P0, _S)
    hi = max(i for i in range(a, b) if lab.RE_HIST.match(lines[i]))
    lines.insert(hi + 1, "- 备注 测试用")
    lines.insert(hi + 2, "- 2026-09-30 ✅ 测试用日志行")
    open(lab.PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))
    e = errs_of(_S)
    ck("⇒ ERROR 且点名「写在 `- 备注` 之后」", any("备注" in m and "契约⑤" in m for m in e), e[:3])

head(f"【K4 负】历史行日期乱序（样本 #{_S}）")
with sandbox(p_text=P0, g_text=G0, sessions=False) as d:
    lines, a, b = span(P0, _S)
    hs = [i for i in range(a, b) if lab.RE_HIST.match(lines[i])]
    lines[hs[0]], lines[hs[-1]] = lines[hs[-1]], lines[hs[0]]
    open(lab.PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))
    e = errs_of(_S)
    ck("⇒ ERROR 且点名日期乱序", any("日期乱序" in m for m in e), e[:3])

head("【K5 正】墓碑条目 ⇒ 只报「墓碑已废除」，⛔ 不再拿契约⑤／状态行去查它")
# ⚠️ 2026-09-05 改：原来这里遍历**真档案里的墓碑**。墓碑整类已在 2026-09-05 废除，
#   真档案的墓碑数变成 0 ⇒ `all([])` 恒真，这一发悄悄变成空转（与 test_count 那条
#   "⛔ 不再拿真档案的墓碑当证据"同一个坑）。⇒ 换成**合成墓碑**，重新长出牙齿。
P_TOMB = ("# 问题总表\n\n---\n\n### 9401 · （已并入 #9201）\n"
          "→ **已迁出**：本条已并入 #9201，编号作废、不复用。\n")
with sandbox(p_text=P_TOMB, g_text="# 已毕业档\n", sessions=False) as d:
    tombs = [e for e in lab.load_all() if e.tomb]
    ck("合成档案里确实有 1 条墓碑（⛔ 空列表 ＝ 空转）", len(tombs) == 1,
       [(e.num, e.tomb) for e in lab.load_all()])
    P = lab.check_entry(tombs[0], set(), {x.num for x in lab.load_all()})
    ck("⛔ 不拿契约⑤／状态行去查墓碑（它本来就没有状态行）",
       not any("契约⑤" in m or "缺状态行" in m for _, m in P), P)
    ck("只报「墓碑条目已废除」这一条（2026-09-05 整类废除）",
       len(P) == 1 and "墓碑条目已废除" in P[0][1], P)

sys.exit(report("lab.py check 契约⑤ 正/负向测试"))
