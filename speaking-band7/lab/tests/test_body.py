#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""条目正文四节（SKILL §3.1 契约⑪–⑭，她 2026-09-12 定）的正向／负向对抗测试。

覆盖：解析（四节 · 题面节 · 成员出题账 · body_end）· check_body 的每一条 ERROR/WARN ·
prompts 读题面节 · append 没有历史行时插在正文之后 · migrate 搬 v3 条目逐字不变 ·
count 的 body-v3 / body-legacy / members 三个口径。
⛔ 夹具全部自带，一个字不来自真档案。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, read, lab

HDR = "# 问题总表\n\n---\n\n"
GHDR = "# 已毕业档\n\n---\n\n"


def v3(num=9501, title="get TO ＋ 地点", kind="搭配", created="2026-09-12",
       status="状态 连对0 连错0 上次— 未毕业 ｜ 题型 词组",
       what="**get to** ＋ 地点 ＝ 到达。邻居（别串）：arrive **at**／reach ＋ 地点（不带介词）。\n判据一句话：get 后面挂地点必须有 to。",
       how="2026-09-11 重答 R10 · 她写 `how to get the destination`。\n查重：dedup \"get to\" ⇒ 命中 #81（get to know，不定式的 to）⇒ 否，两条规则。",
       wrong="她的：get the destination　正确：get **to** the destination\n找法：get 后面是地点吗？是 ⇒ 补 to。",
       prompt='"到目的地怎么走"（问路时那个"到"）',
       members=None, rows=(), notes=(), extra_meta=""):
    s = (f"### {num} · {title}\n"
         f"类型 {kind} ｜ 新建 {created}{extra_meta}\n"
         f"{status}\n\n"
         f"**问题是什么**\n{what}\n\n"
         f"**怎么发现的**\n{how}\n\n"
         f"**我错在哪**\n{wrong}\n\n"
         f"**题面**\n{prompt}\n")
    if members is not None:
        s += f"\n**成员出题账**\n{members}\n"
    s += "\n" if (rows or notes) else ""
    for r in rows:
        s += r + "\n"
    for n in notes:
        s += n + "\n"
    return s


def errs(num, level="ERROR"):
    ents = lab.load_all()
    nums = {e.num for e in ents}
    e = [x for x in ents if x.num == num][0]
    return [m for lv, m in lab.check_entry(e, set(), nums) if lv == level]


def ent(num):
    return [x for x in lab.load_all() if x.num == num][0]


# ══════════════════════════════════════════════════════════════════════════
head("【B0 正】标准 v3 条目 ⇒ 解析出四节、题面来自题面节、check ERROR 0")
P = HDR + v3(rows=["- 2026-09-12 新建 · 重答 R10"])
with sandbox(p_text=P, g_text=GHDR) as d:
    e = ent(9501)
    ck("四节都解析到", set(e.sections) == set(lab.SECTIONS), sorted(e.sections))
    ck("body_v3 为真", e.body_v3)
    ck("题面 ＝ 题面节的正文", e.prompt == '"到目的地怎么走"（问路时那个"到"）', e.prompt)
    ck("元信息行里没有题面 ⇒ prompt_inline 为空", e.prompt_inline is None, e.prompt_inline)
    ck("引号句切得出来", lab.prompt_quotes(e) == ["到目的地怎么走"], lab.prompt_quotes(e))
    ck("括号限定切得出来", lab.prompt_parens(e) == ['问路时那个"到"'], lab.prompt_parens(e))
    ck("历史行照常解析", len(e.history) == 1 and e.history[0].date == "2026-09-12", e.history)
    ck("body_end 指向题面那一行", e.body_end is not None and
       read(d, "problems.md").split("\n")[e.body_end - 1].startswith('"到目的地'), e.body_end)
    ck("check ERROR 0", errs(9501) == [], errs(9501))
    ck("不再报「存量一行式」", not any("一行式" in m for m in errs(9501, "INFO")))
    st, rc, out = run(lab.cmd_check, Args(all=True, changed=False))
    ck("check --all ERROR 0", "ERROR 0" in out, out[-300:])

head("【B0b 正】题面节里的 ★ 行是注释，⛔ 不进题面本体；合并条编号句只取 ①②…")
M = v3(num=9502, title="不可数名词一族", kind="词汇",
       status="状态 连对0 连错0 上次— 未毕业 ｜ **合并条·出题多句覆盖** ｜ 题型 词组",
       prompt='　① "一些建议"（给人出主意那种）\n　② "更多信息"（资料、消息那种）\n　　★ 目标形式（教练看）：① some advice ② more information',
       members="① advice ｜ 未出过\n② information ｜ 未出过",
       rows=["- 2026-09-12 新建"])
with sandbox(p_text=HDR + M, g_text=GHDR) as d:
    e = ent(9502)
    ck("题面 ＝ 两个编号句", e.prompt == '① "一些建议"（给人出主意那种）　② "更多信息"（资料、消息那种）', e.prompt)
    ck("★ 行不进引号句", lab.prompt_quotes(e) == ["一些建议", "更多信息"], lab.prompt_quotes(e))
    ck("prompt_lines 含 ★ 行（prompts 整段打印用）", len(e.prompt_lines) == 3, e.prompt_lines)
    ck("成员出题账解析到两行", e.members and len([l for l in e.members if l.strip()]) == 2, e.members)
    ck("合并条挂了账 ⇒ ERROR 0", errs(9502) == [], errs(9502))
    ck("count members 命中", 9502 in [x.num for x in lab.load_all() if x.members is not None])

head("【B0c 正】题面节里的 ★ 注释写成多行 ⇒ 缩进续行一并算注释，⛔ 不漏进题面本体")
ML = v3(prompt='"到目的地怎么走"（问路时那个"到"）\n　　★ 题面 2026-09-05 改：旧题面"怎么去那个地方。"\n　　　里 "怎么去" 被译成 how to go ⇒ 换成"到"',
        rows=["- 2026-09-12 新建"])
with sandbox(p_text=HDR + ML, g_text=GHDR) as d:
    e = ent(9501)
    ck("题面本体只剩第一行", e.prompt == '"到目的地怎么走"（问路时那个"到"）', e.prompt)
    ck("续行里的引号句不进 prompt_quotes", lab.prompt_quotes(e) == ["到目的地怎么走"], lab.prompt_quotes(e))
    ck("check ERROR 0", errs(9501) == [], errs(9501))

head("【B4b 正】不带日期的尾块行（- 旧账／- ⚠️…）放在四节之后 ⇒ 正文到此为止，⛔ 不算正文顶格 `- `")
TAIL = v3(rows=[], notes=["- 旧账 事件流无记录；08-09 前已毕业", "- ⚠️ 与 #9502 一起读"],
          status="状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-09-10** ｜ 题型 词组")
with sandbox(p_text=HDR + TAIL, g_text=GHDR) as d:
    e = ent(9501)
    ck("尾块行不算正文里的 `- `", e.dash_in_body == [], e.dash_in_body)
    ck("题面节没被尾块行污染", e.prompt == '"到目的地怎么走"（问路时那个"到"）', e.prompt)
    ck("check ERROR 0", errs(9501) == [], errs(9501))
TAIL_FIRST = HDR + ("### 9501 · 尾块行写在四节之前\n类型 搭配 ｜ 新建 2026-09-12\n"
                    "状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-09-10** ｜ 题型 词组\n\n"
                    "- 旧账 事件流无记录\n\n**问题是什么**\nx\n\n**怎么发现的**\nx\n\n**我错在哪**\n找法：x\n\n**题面**\n\"块\"\n")
with sandbox(p_text=TAIL_FIRST, g_text=GHDR) as d:
    ck("尾块行写在四节之前 ⇒ 节标题算写在历史行之后 ⇒ ERROR", any("历史行之后" in m for m in errs(9501)), errs(9501))

head("【B1 负】缺节 ⇒ ERROR 点名缺哪一节")
BAD = HDR + v3().replace("**我错在哪**\n她的：get the destination　正确：get **to** the destination\n找法：get 后面是地点吗？是 ⇒ 补 to。\n\n", "")
with sandbox(p_text=BAD, g_text=GHDR) as d:
    E = errs(9501)
    ck("报缺「我错在哪」", any("缺节" in m and "我错在哪" in m for m in E), E)

head("【B2 负】四节顺序错 ⇒ ERROR")
SW = HDR + v3().replace("**怎么发现的**", "**TMP**").replace("**我错在哪**", "**怎么发现的**").replace("**TMP**", "**我错在哪**")
with sandbox(p_text=SW, g_text=GHDR) as d:
    E = errs(9501)
    ck("报顺序不对", any("顺序不对" in m and "问题是什么 → 我错在哪" in m for m in E), E)

head("【B3 负】题面写了两处（元信息行 ＋ 题面节）⇒ ERROR")
TWO = HDR + v3(extra_meta=' ｜ 题面 "到目的地怎么走"')
with sandbox(p_text=TWO, g_text=GHDR) as d:
    E = errs(9501)
    ck("报题面写了两处", any("两处" in m for m in E), E)
    ck("题面仍以题面节为准", ent(9501).prompt == '"到目的地怎么走"（问路时那个"到"）')

head("【B4 负】正文里顶格 `- ` ⇒ ERROR（`- ` 只给历史行/备注）")
DASH = HDR + v3(what="**get to** ＋ 地点\n- 邻居：arrive at\n- 邻居：reach")
with sandbox(p_text=DASH, g_text=GHDR) as d:
    E = errs(9501)
    ck("报顶格 `- `", any("顶格 `- `" in m for m in E), E)
    ck("那两行仍算正文、不算历史行", len(ent(9501).history) == 0, ent(9501).history)

head("【B5 负】节标题写歪 ⇒ ERROR（缩进／📒／不加粗／带冒号）")
for bad_head, label in (("　**题面**", "缩进"), ("📒 **题面**", "📒 前缀"), ("题面", "不加粗"), ("**题面**：", "带冒号")):
    T = HDR + v3().replace("**题面**\n", bad_head + "\n")
    with sandbox(p_text=T, g_text=GHDR) as d:
        E = errs(9501)
        ck(f"{label} ⇒ 报写歪", any("写歪" in m for m in E), E)
        ck(f"{label} ⇒ 同时报缺「题面」节", any("缺节" in m and "题面" in m for m in E), E)

head("【B5b 负】节标题跑到历史行之后 ⇒ ERROR")
LATE = HDR + v3(rows=["- 2026-09-12 新建", "**成员出题账**", "① x ｜ 未出过"])
with sandbox(p_text=LATE, g_text=GHDR) as d:
    E = errs(9501)
    ck("报「写在历史行之后」", any("历史行之后" in m for m in E), E)

head("【B6 负】v3 条目没写题型格 ⇒ ERROR")
NOASK = HDR + v3(status="状态 连对0 连错0 上次— 未毕业")
with sandbox(p_text=NOASK, g_text=GHDR) as d:
    E = errs(9501)
    ck("报题型格", any("题型" in m and "四节" in m for m in E), E)

head("【B7 负】合并条没挂成员出题账 ⇒ ERROR；挂了却没标合并条 ⇒ WARN")
NOMEM = HDR + v3(status="状态 连对0 连错0 上次— 未毕业 ｜ **合并条·出题多句覆盖** ｜ 题型 词组")
with sandbox(p_text=NOMEM, g_text=GHDR) as d:
    ck("报缺成员出题账", any("成员出题账" in m for m in errs(9501)), errs(9501))
MEMONLY = HDR + v3(members="① x ｜ 未出过", rows=["- 2026-09-12 新建"])
with sandbox(p_text=MEMONLY, g_text=GHDR) as d:
    ck("WARN 两边对齐", any("两边对齐" in m for m in errs(9501, "WARN")), errs(9501, "WARN"))
    ck("不算 ERROR", errs(9501) == [], errs(9501))
EMPTYMEM = HDR + v3(status="状态 连对0 连错0 上次— 未毕业 ｜ **合并条·出题多句覆盖** ｜ 题型 词组", members="")
with sandbox(p_text=EMPTYMEM, g_text=GHDR) as d:
    ck("空账 ⇒ ERROR", any("是空的" in m for m in errs(9501)), errs(9501))

head("【B8 负】题面节空／没引号句 ⇒ ERROR；永不出题的条目题面节可写说明")
EMPTYQ = HDR + v3(prompt="")
with sandbox(p_text=EMPTYQ, g_text=GHDR) as d:
    ck("题面节空 ⇒ ERROR", any("题面」节是空的" in m for m in errs(9501)), errs(9501))
    ck("count prompt-todo 命中", not ent(9501).prompt)
NOQ = HDR + v3(prompt="到目的地怎么走（用 get 说）")
with sandbox(p_text=NOQ, g_text=GHDR) as d:
    ck("没引号句 ⇒ ERROR", any("没有引号句" in m for m in errs(9501)), errs(9501))
OUT = HDR + v3(status="状态 连对0 连错0 上次— 未毕业 ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题** ｜ 题型 整句",
               prompt="不出中译英题；挂自由产出抓（get 后面挂地点没有 to）")
with sandbox(p_text=OUT, g_text=GHDR) as d:
    ck("永不出题的条目题面节是说明，⛔ 不报引号句", not any("引号句" in m for m in errs(9501)), errs(9501))

head("【B9 负】「我错在哪」没写找法 ⇒ WARN；空节 ⇒ ERROR")
NOFIND = HDR + v3(wrong="她的：get the destination　正确：get to the destination")
with sandbox(p_text=NOFIND, g_text=GHDR) as d:
    ck("WARN 没写找法", any("找法" in m for m in errs(9501, "WARN")), errs(9501, "WARN"))
EMPTYW = HDR + v3(what="")
with sandbox(p_text=EMPTYW, g_text=GHDR) as d:
    ck("「问题是什么」空 ⇒ ERROR", any("问题是什么」节是空的" in m for m in errs(9501)), errs(9501))

head("【B10】存量一行式：BODY_FROM 之前建的 ⇒ 存量提示；BODY_FROM 起新建的 ⇒ ERROR")
OLD = HDR + ("### 9601 · 存量条目\n类型 语法 ｜ 题面 \"中文。\" ｜ 新建 2026-09-01\n"
             "状态 连对1 连错0 上次2026-09-03 未毕业\n- 2026-09-01 ❌ a\n- 2026-09-03 ✅ b\n")
NEW = HDR + ("### 9602 · 新建却没四节\n类型 语法 ｜ 题面 \"中文。\" ｜ 新建 2026-09-12\n"
             "状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句\n- 2026-09-12 新建\n")
with sandbox(p_text=OLD + "\n" + NEW, g_text=GHDR) as d:
    ck("存量 ⇒ 不是 ERROR", errs(9601) == [], errs(9601))
    ck("存量 ⇒ 列存量提示", any("一行式" in m for m in errs(9601, "INFO")), errs(9601, "INFO"))
    ck("存量的题面仍从元信息行读", ent(9601).prompt == '"中文。"')
    ck("新建缺四节 ⇒ ERROR", any("缺四节" in m for m in errs(9602)), errs(9602))
    st, rc, out = run(lab.cmd_count, Args(type="body-legacy", detail=False))
    ck("count body-legacy 列出两条", "#9601" in out and "#9602" in out, out[-300:])
    st, rc, out = run(lab.cmd_count, Args(type="body-v3", detail=False))
    ck("count body-v3 为零", "⇒ 0 条" in out or "0 条" in out, out[-200:])

head("【B11 正】prompts 读题面节（含 ★ 行）；--verify 查合并条多句覆盖")
with sandbox(p_text=HDR + M, g_text=GHDR) as d:
    st, rc, out = run(lab.cmd_prompts, Args(nums=["9502"], verify=None))
    ck("打出「档案题面节」标签", "档案题面节" in out, out[-500:])
    ck("三行都打出来（含 ★）", '"一些建议"' in out and '"更多信息"' in out and "★ 目标形式" in out, out[-500:])
    draft = os.path.join(d, "draft.md")
    open(draft, "w", encoding="utf-8").write('出题 1 · #9502（合并条，两句全出）\n'
                                             '  ① "一些建议"（给人出主意那种）\n  ② "更多信息"（资料、消息那种）\n')
    st, rc, out = run(lab.cmd_prompts, Args(nums=["9502"], verify=draft))
    ck("合并条两句都在 ⇒ 通过", rc == 0 and "可以发" in out, out[-300:])
    open(draft, "w", encoding="utf-8").write('出题 1 · #9502（合并条）\n  ① "一些建议"（给人出主意那种）\n')
    st, rc, out = run(lab.cmd_prompts, Args(nums=["9502"], verify=draft))
    ck("少一句 ⇒ 拦", rc == 1 and "更多信息" in out, out[-300:])

head("【B12 正】append：v3 条目没有历史行 ⇒ 插在正文最后一行之后（⛔ 不插进四节中间）")
FRESH = HDR + v3(rows=[], notes=["- 备注 判重：零命中"])
with sandbox(p_text=FRESH, g_text=GHDR) as d:
    rows = os.path.join(d, "rows.md")
    open(rows, "w", encoding="utf-8").write("#9501 ✅ 在池第 1 组 · `get to the destination`\n")
    st, rc, out = run(lab.cmd_append, Args(file=rows, date="2026-09-13", dry_run=False))
    txt = read(d, "problems.md").split("\n")
    i_prompt = next(i for i, l in enumerate(txt) if l.startswith('"到目的地'))
    i_row = next(i for i, l in enumerate(txt) if l.startswith("- 2026-09-13 ✅"))
    i_note = next(i for i, l in enumerate(txt) if l.startswith("- 备注"))
    ck("append 成功", rc == 0, out[-300:])
    ck("判定行在题面之后、备注之前", i_prompt < i_row < i_note, (i_prompt, i_row, i_note))
    ck("状态行三个数重算", "连对1 连错0 上次2026-09-13" in read(d, "problems.md"))
    e = ent(9501)
    ck("重读后仍是 v3、题面没丢", e.body_v3 and e.prompt == '"到目的地怎么走"（问路时那个"到"）')
    ck("append 后 check ERROR 0", errs(9501) == [], errs(9501))

head("【B12b 正】append：v3 条目已有历史行 ⇒ 仍按日期插在历史行区")
WITH = HDR + v3(rows=["- 2026-09-12 新建 · 重答 R10", "  她写 `get the destination`"], notes=["- 备注 x"])
with sandbox(p_text=WITH, g_text=GHDR) as d:
    rows = os.path.join(d, "rows.md")
    open(rows, "w", encoding="utf-8").write("#9501 ❌ 在池第 1 组\n")
    st, rc, out = run(lab.cmd_append, Args(file=rows, date="2026-09-13", dry_run=False))
    txt = read(d, "problems.md").split("\n")
    i_new = next(i for i, l in enumerate(txt) if l.startswith("- 2026-09-12 新建"))
    i_row = next(i for i, l in enumerate(txt) if l.startswith("- 2026-09-13 ❌"))
    i_note = next(i for i, l in enumerate(txt) if l.startswith("- 备注"))
    ck("插在建号行之后、备注之前", rc == 0 and i_new < i_row < i_note, (rc, i_new, i_row, i_note))

head("【B13 负】rows 块体里出现节标题 ⇒ append 整批拦下")
with sandbox(p_text=HDR + v3(rows=["- 2026-09-12 新建"]), g_text=GHDR) as d:
    rows = os.path.join(d, "rows.md")
    open(rows, "w", encoding="utf-8").write("#9501 ✅ 组1\n  内容\n**题面**\n")
    before = read(d, "problems.md")
    st, rc, out = run(lab.cmd_append, Args(file=rows, date="2026-09-13", dry_run=False))
    ck("拦下且一个字没写", rc == 1 and read(d, "problems.md") == before, out[-300:])

head("【B14 正】migrate 搬 v3 条目 ⇒ 整块逐字不变")
G3 = v3(num=9503, title="毕业的 v3", status="状态 连对2 连错0 上次2026-09-12 ｜ **🎓 已毕业 2026-09-12** ｜ 题型 词组",
        rows=["- 2026-09-10 ✅ a", "- 2026-09-12 ✅ b"])
with sandbox(p_text=HDR + G3, g_text=GHDR) as d:
    before = read(d, "problems.md")
    st, rc, out = run(lab.cmd_migrate, Args(dry_run=False))
    ck("migrate 成功", rc == 0, out[-300:])
    g = read(d, "graduated.md")
    ck("四节整块搬进 graduated.md", "**问题是什么**" in g and "**题面**" in g and "### 9503" in g)
    ck("problems.md 里不再有它", "### 9503" not in read(d, "problems.md"))
    e = ent(9503)
    ck("搬完仍是 v3、题面完整", e.body_v3 and e.src == "graduated.md" and e.prompt.startswith('"到目的地'))
    ck("搬完 check ERROR 0", errs(9503) == [], errs(9503))

head("【B15 正】pick 的卡片用题面节的题面；bundlable 按题型")
with sandbox(p_text=HDR + v3(rows=["- 2026-09-10 ❌ a"]), g_text=GHDR) as d:
    e = ent(9501)
    c = lab.card(e, "why")
    ck("卡片里是题面节的题面", "到目的地怎么走" in c, c)
    ck("题型 词组 ⇒ 可打包", lab.bundlable(e))

sys.exit(report("lab.py 正文四节（§3.1 契约⑪–⑭）正/负向测试"))
