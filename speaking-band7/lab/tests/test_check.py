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


def errs_of(num, level="ERROR"):
    ents = lab.load_all()
    nums = {e.num for e in ents}
    e = [x for x in ents if x.num == num][0]
    return [m for lv, m in lab.check_entry(e, set(), nums) if lv == level]


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
    # ★ 2026-09-12 起：一行式存量正文会多一条「存量提示」（INFO，§3.1 契约⑭）—— 这是设计，
    #   不是脏；这里只断言 ERROR/WARN 为零。v3 四节的正向语料见 test_body.py。
    allp = {k: [x for x in v if x[0] != "INFO"] for k, v in allp.items()}
    ck("★ 而且整体一条 ERROR/WARN 都不报（语料自己得是干净的）",
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


# ══════════════════════════════════════════════════════════════════════════
#  K6 题型格（§6.0，她 2026-09-11 定：比照写作线契约②第 7 格）—— 正/负向
#  起因：09-11 两条题面各破一边（词组题提示写「人当主语说」／整句题面缺主语），
#       审核表第 6 项照样打了 ✅ ⇒ 只写在 skill 里的规则挡不住，这一条必须是机器闸。
# ══════════════════════════════════════════════════════════════════════════
def _ent(num, kind, prompt, status_mid, created="2026-09-01", extra=""):
    return (f"### {num} · 题型夹具\n"
            f"类型 {kind} ｜ 题面 {prompt} ｜ 新建 {created}\n"
            f"状态 连对1 连错0 上次2026-09-03{status_mid} 未毕业{extra}\n"
            "- 2026-09-01 ❌ 首犯\n- 2026-09-03 ✅ 复习\n")


def _errs(text, num):
    with sandbox(p_text="# 问题总表\n\n---\n\n" + text, g_text=G0, sessions=False):
        return errs_of(num)


head("【K6 正】题型 词组 ＋ 块状题面（无句号、提示不改形式）⇒ 零 ERROR")
e = _errs(_ent(9601, "词组", "\"把桌上收拾了\"（饭后收拾餐桌）", " ｜ 题型 词组"), 9601)
ck("词组题面合规 ⇒ ERROR 0", not e, e)

head("【K6 正】题型 整句 ＋ 完整句题面 ⇒ 零 ERROR")
e = _errs(_ent(9602, "结构", "\"他聪明到知道自己要什么。\"（用 **know** 起头说）", " ｜ 题型 整句"), 9602)
ck("整句题面合规 ⇒ ERROR 0", not e, e)

head("【K6 负】题型 词组，题面引号句却带句号")
e = _errs(_ent(9603, "词组", "\"他把桌上收拾了。\"（用 clear 说）", " ｜ 题型 词组"), 9603)
ck("⇒ ERROR 且点名「带句号」", any("带句号" in m for m in e), e)

head("【K6 负】题型 词组，提示里写「人当主语说」（提示改变了产出形式，§6② 红线）")
e = _errs(_ent(9604, "词组", "\"东西乱丢一地\"（**人**当主语说 · 用三个词的块说）", " ｜ 题型 词组"), 9604)
ck("⇒ ERROR 且点名「当主语」", any("当主语" in m for m in e), e)
for ban in ("说一句", "一句话", "整句"):
    e = _errs(_ent(9604, "词组", f"\"东西乱丢一地\"（{ban}说）", " ｜ 题型 词组"), 9604)
    ck(f"禁用字眼「{ban}」同样拦下", any(ban in m for m in e), e)

head("【K6 负】题型 整句，题面引号句却没有句末标点（＝ 不是完整句）")
e = _errs(_ent(9605, "结构", "\"聪明到知道自己要什么\"（用 know 起头说）", " ｜ 题型 整句"), 9605)
ck("⇒ ERROR 且点名「不是完整句」", any("不是完整句" in m for m in e), e)

head("【K6 负】题型格写了闭集之外的值")
e = _errs(_ent(9606, "词组", "\"把桌上收拾了\"", " ｜ 题型 加练"), 9606)
ck("⇒ ERROR 且点名「非法」", any("非法" in m for m in e), e)

head(f"【K6 负】{lab.ASK_FROM} 起新建的条目缺题型格 ⇒ ERROR；更早的缺格 ⇒ 不报（存量按整句读）")
e = _errs(_ent(9607, "搭配", "\"空气污染的主因\"（用 cause 说）", "", created=lab.ASK_FROM), 9607)
ck("新建 ≥ ASK_FROM 缺格 ⇒ ERROR", any("缺「题型」格" in m for m in e), e)
e = _errs(_ent(9608, "搭配", "\"空气污染的主因\"（用 cause 说）", "", created="2026-09-10"), 9608)
ck("新建 < ASK_FROM 缺格 ⇒ 不报（⛔ 存量不跑形式检查）", not e, e)

head("【K6】题型闭集只剩 整句／词组；产出验已取消 ⇒ 写它报 ERROR")
with sandbox(p_text="# 问题总表\n\n---\n\n"
             + _ent(9609, "结构", "【不出中译英题，挂自由产出抓】", " ｜ ⚪ **只记录·不出题**")
             + "\n" + _ent(9610, "结构", "【用英文答 3 句】", " ｜ 题型 产出验")
             + "\n" + _ent(9611, "词组", "\"把桌上收拾了\"", " ｜ 题型 词组"),
             g_text=G0, sessions=False):
    E = {x.num: x for x in lab.load_all()}
    ck("只记录·不出题 ⇒ 不 drawable、不 recallable", not E[9609].drawable and not E[9609].recallable)
    ck("题型写 产出验 ⇒ check 报「已取消」ERROR",
       any("已取消" in m for _l, m in lab.check_ask(E[9610]) if _l == "ERROR"),
       lab.check_ask(E[9610]))
    ck("产出验不在闭集里", "产出验" not in lab.ASKS and "产出验" in lab.ASK_RETIRED)
    ck("词组 ⇒ 照常 drawable", E[9611].drawable)
    ck("没写题型格 ⇒ ask 为 None、ask_kind 默认 整句", E[9609].ask is None and E[9611].ask == lab.ASK_PHRASE)
    ck("题型 词组 ⇒ bundlable（不看类型标签）", lab.bundlable(E[9611]))
    st, rc, out = run(lab.cmd_count, Args())
    ck("count 表里有 ask-sentence／ask-phrase／ask-retired／ask-unmarked 四行",
       all(k in out for k in ("ask-sentence", "ask-phrase", "ask-retired", "ask-unmarked")), out[-600:])

head("【K6 正】题型 整句 显式标了 ⇒ 即使类型是搭配也⛔不打包；未标的搭配沿用旧口径打包")
with sandbox(p_text="# 问题总表\n\n---\n\n"
             + _ent(9612, "搭配", "\"要是东西坏了，给我打个电话。\"（用 break 说）", " ｜ 题型 整句")
             + "\n" + _ent(9613, "搭配", "\"备课\"（用 prepare 说）", ""),
             g_text=G0, sessions=False):
    E = {x.num: x for x in lab.load_all()}
    ck("显式 整句 ⇒ 不 bundlable", not lab.bundlable(E[9612]))
    ck("未标 ＋ 类型 搭配 ⇒ 沿用旧口径 bundlable", lab.bundlable(E[9613]))



head("【K6 正】题型格能活过 append —— rewrite_status 只动三个数，`｜ 题型 X` 原样保留")
_P97 = ("# 问题总表\n\n---\n\n"
        "### 9701 · append 回环夹具\n"
        "类型 词组 ｜ 题面 \"把桌上收拾了\"（饭后收拾餐桌） ｜ 新建 2026-09-01\n"
        "状态 连对0 连错1 上次2026-09-03 未毕业 ｜ 题型 词组\n"
        "- 2026-09-01 ❌ 首犯\n- 2026-09-03 ❌ 复习\n")
with sandbox(p_text=_P97, g_text=G0, sessions=False) as d:
    f = os.path.join(d, "rows.md")
    open(f, "w", encoding="utf-8").write("#9701 ✅ 复习 · 夹具\n")
    st, rc, out = run(lab.cmd_append, Args(file=f, date="2026-09-05", dry_run=False))
    ck("append 退出码 0", (st, rc) == ("OK", 0), out[-300:])
    E = {x.num: x for x in lab.load_all()}
    ck("三个数重算了（连对1 连错0 上次09-05）", (E[9701].ok, E[9701].bad, E[9701].last) == (1, 0, "2026-09-05"),
       E[9701].status_raw)
    ck("★ `｜ 题型 词组` 还在状态行上、仍能读出", "｜ 题型 词组" in E[9701].status_raw and E[9701].ask == lab.ASK_PHRASE,
       E[9701].status_raw)
    ck("append 之后 check 仍 ERROR 0", not errs_of(9701), errs_of(9701))

head("【K6 负】「题型」二字写在状态行上、却写歪了（少 ｜）⇒ ERROR，⛔ 不许静默按整句读")
e = _errs(_ent(9702, "词组", "\"把桌上收拾了\"", " 题型 词组"), 9702)     # 没有 ｜
ck("⇒ ERROR 且点名「读不出这一格」", any("读不出这一格" in m for m in e), e)
e = _errs(_ent(9703, "词组", "\"把桌上收拾了\"", " ｜ **题型 词组**"), 9703)   # 加粗写法
ck("加粗 `**题型 词组**` ⇒ 照样读得出（不报错）", not e, e)


head("【K6 负→正】形式检查⛔不看括号提示里的引号（2026-09-11 上线当天的假阳性）")
# 整句题的提示里带引号短语：`（"比方说"用 Say 起头）` —— 那是提示，不是题面本体
e = _errs(_ent(9801, "词组", "**点名**：\"比方说你解决了一个全组都卡住的问题。\"（\"比方说\"用 Say 起头）",
               " ｜ 题型 整句"), 9801)
ck("整句题 · 提示里的引号短语 ⇒ ⛔ 不报「不是完整句」", not e, e)
e = _errs(_ent(9802, "减法型", "**点名**：\"最重要的一点是家长得有条理。\"（\"最重要的一点是…\"这层用 **the key thing** 说）",
               " ｜ 题型 整句"), 9802)
ck("整句题 · 提示里带省略号的引号 ⇒ ⛔ 不报", not e, e)
# 词组题的提示里带**句号**的引号短语，也不该被当成"题面带句号"
e = _errs(_ent(9803, "词组", "\"约会\"（\"我们去约会了。\"里的那件事）", " ｜ 题型 词组"), 9803)
ck("词组题 · 提示里的引号句带句号 ⇒ ⛔ 不报「带句号」", not e, e)
# ★ 但题面**主体**自己违规，照样要抓 —— 别把闸修没了
e = _errs(_ent(9804, "词组", "\"他把桌上收拾了。\"（用 clear 说）", " ｜ 题型 词组"), 9804)
ck("★ 主体带句号 ⇒ 仍然 ERROR（闸没被修没）", any("带句号" in m for m in e), e)
e = _errs(_ent(9805, "结构", "\"聪明到知道自己要什么\"（用 know 起头说）", " ｜ 题型 整句"), 9805)
ck("★ 主体不是完整句 ⇒ 仍然 ERROR", any("不是完整句" in m for m in e), e)

head("【K7 负】§6② 提示禁写法（她 2026-09-29 定：比照写作线 §6）—— 负向排除／首字母／词数／形态描述 ⇒ 未毕业 ERROR")
for hint, tag in (("用 **clear** 说 · ⛔ 不许用 clean", "负向排除"),
                  ("别用 tidy", "负向排除"),
                  ("用 **c** 开头的动词说", "首字母"),
                  ("两个词", "词数"),
                  ("用三个词的块说", "词数"),
                  ("用一个动词说", "形态"),
                  ("用【动词＋宾语】说", "形态"),
                  ("用最自然的说法", "空泛")):
    e = _errs(_ent(9901, "搭配", f"\"他把桌上收拾了。\"（{hint}）", " ｜ 题型 整句"), 9901)
    ck(f"整句 ·（{hint}）⇒ ERROR「{tag}」", any(tag in m for m in e), e)
e = _errs(_ent(9902, "搭配", "\"他把桌上收拾了。\"（\"收拾\"用 **clear** 说）", " ｜ 题型 整句"), 9902)
ck("★ 正向点名「X 用 Y 说」⇒ 放行", not e, e)
e = _errs(_ent(9903, "词组", "\"赚翻了\"（用 **bank** 说）", " ｜ 题型 词组"), 9903)
ck("词组题括号里有英文 ⇒ ERROR「零英文提示」", any("零英文提示" in m for m in e), e)
e = _errs(_ent(9904, "词组", "\"赚翻了\"（口语俚语，赚了一大笔）", " ｜ 题型 词组"), 9904)
ck("★ 词组题中文释义 ⇒ 放行", not e, e)

head("【K7 负】类型是语法／结构却标题型 词组 ⇒ ERROR（词组题只收 词组／搭配／词汇）")
for kind in ("语法", "结构", "句型", "减法型"):
    e = _errs(_ent(9905, kind, "\"容易多了\"", " ｜ 题型 词组"), 9905)
    ck(f"类型 {kind} × 题型 词组 ⇒ ERROR", any("却标了题型 词组" in m for m in e), e)
with sandbox(p_text="# 问题总表\n", g_text=("# 已毕业档\n\n---\n\n### 9908 · 毕业夹具\n"
      "类型 语法 ｜ 题面 \"容易多了\" ｜ 新建 2026-09-01\n"
      "状态 连对2 连错0 上次2026-09-03 ｜ **🎓 已毕业 2026-09-03** ｜ 题型 词组\n"
      "- 2026-09-01 ✅ a\n- 2026-09-03 ✅ b\n"), sessions=False) as d:
    ck("🎓 · 语法×词组 ⇒ 存量提示、⛔ 不报 ERROR", not errs_of(9908)
       and any("却标了题型 词组" in m for m in errs_of(9908, "INFO")), (errs_of(9908), errs_of(9908, "INFO")))
    open(os.path.join(d, "dr.md"), "w", encoding="utf-8").write('出题 1 · #9908 · "现在网上买票容易多了"\n')
    st, rc, out = run(lab.cmd_prompts, Args(nums=["9908"], verify=os.path.join(d, "dr.md"), date="2026-09-29"))
    ck("★ 但抽到它发题 ⇒ prompts --verify 硬拦（先回标题型）", rc == 1 and "先回标" in out, out[-300:])
for kind in lab.PHRASE_KINDS:
    e = _errs(_ent(9906, kind, "\"容易多了\"", " ｜ 题型 词组"), 9906)
    ck(f"★ 类型 {kind} × 题型 词组 ⇒ 放行", not e, e)

head("【K7 正】🎓 条目的旧提示不合规 ⇒ 只列存量提示（出题时发的是新写的题面，由 prompts --verify 硬查）")
_G = ("# 已毕业档\n\n---\n\n### 9907 · 毕业夹具\n"
      "类型 搭配 ｜ 题面 \"他把桌上收拾了。\"（⛔ 不许用 clean） ｜ 新建 2026-09-01\n"
      "状态 连对2 连错0 上次2026-09-03 ｜ **🎓 已毕业 2026-09-03** ｜ 题型 整句\n"
      "- 2026-09-01 ✅ a\n- 2026-09-03 ✅ b\n")
with sandbox(p_text="# 问题总表\n", g_text=_G, sessions=False):
    ck("🎓 · 负向排除 ⇒ ⛔ 不报 ERROR", not errs_of(9907), errs_of(9907))
    ck("🎓 · 负向排除 ⇒ 列存量提示", any("禁写法" in m for m in errs_of(9907, "INFO")), errs_of(9907, "INFO"))

sys.exit(report("lab.py check 契约⑤ 正/负向测试"))
