#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-05 三场对抗演练逼出来的闸 —— 每条都对应一个真发生过的漏网。正向＋负向。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import lab, ck, head, report, sandbox, run, read, Args

D = "2026-09-10"


def sess(body, day="L1"):
    return f"# {D} · **{day}**\n\n" + body


def deliver(txt, drawn=None, section=None):
    with sandbox(sessions=False) as d:
        os.makedirs(os.path.join(d, "sessions"), exist_ok=True)
        p = os.path.join(d, "sessions", D + ".md")
        open(p, "w", encoding="utf-8").write(txt)
        if drawn is not None:
            open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write(drawn)
        return run(lab.cmd_deliver, Args(session=p, section=section))[2]


def nerr(out):
    m = re.search(r"ERROR (\d+)", out)
    return int(m.group(1)) if m else -1


GRP = sess('''## ① 在池组 · 第 1 组（2 题）
```
[1] #318 · "题面一"
原句 a ｜判定 ✅ 考点 ｜最小改 ＝原句 ｜更好版 无更好版本 ｜diff-1 无 diff ｜diff-2 无 diff
```
```
[2] #319 · "题面二"
原句 b ｜判定 ✅ 考点 ｜最小改 ＝原句 ｜更好版 无更好版本 ｜diff-1 无 diff ｜diff-2 无 diff
```
### 【本组新建条目】
无
''')
DRAWN_OK = f"{D}\t第 1 组\t抽\t318,319\n{D}\t第 1 组\t用\t318,319\n"

# ══════════════════════════════════════════════════════════════════════════
head("① 节标题术语：SKILL 叫「在池组」，闸必须认（H1 —— 写错不报错、整节不查）")
ck("正向：`## ① 在池组 · 第 N 组` 被认出并查", nerr(deliver(GRP, DRAWN_OK)) == 0,
   deliver(GRP, DRAWN_OK)[-500:])
ck("正向：旧名字「复习组」照样认（存量 session 不改名）",
   nerr(deliver(GRP.replace("在池组", "复习组"), DRAWN_OK)) == 0)
for pfx in ("a ", "a2 ", "①b ", "⓪ "):
    t = GRP.replace("## ① 在池组", f"## {pfx}在池组")
    ck(f"正向：前缀「{pfx.strip()}」也认（⛔ 各节前缀口径必须一致）",
       nerr(deliver(t, DRAWN_OK)) == 0, deliver(t, DRAWN_OK)[-300:])
bad = GRP.replace("原句 b ｜判定 ✅ 考点 ｜最小改 ＝原句 ｜更好版 无更好版本 ｜diff-1 无 diff ｜diff-2 无 diff",
                  "原句 b")
ck("★ 负向：认出来了就真查（第 2 题缺五项 ⇒ 报错，⛔ 不再静默跳过）",
   nerr(deliver(bad, DRAWN_OK)) > 0)

# ══════════════════════════════════════════════════════════════════════════
head("② §7 允许全对的题压成一行 —— 闸要对上 SKILL（手写量 12 行 → 1 行）")
ck("正向：一行 ｜ 分隔的六项算齐", nerr(deliver(GRP, DRAWN_OK)) == 0)
miss = GRP.replace("｜更好版 无更好版本 ", "")
ck("负向：压缩行里真少一项 ⇒ 照样报错",
   nerr(deliver(miss, DRAWN_OK)) > 0 and "更好版" in deliver(miss, DRAWN_OK))
ck("负向：压缩行里 diff 有改动却没摆两行完整句 ⇒ 报错",
   nerr(deliver(GRP.replace("｜diff-1 无 diff", "｜diff-1 aaa → bbb"), DRAWN_OK)) > 0)

# ══════════════════════════════════════════════════════════════════════════
head("③ 与 drawn.log 对账（H2 —— 内部自洽 ≠ 没丢东西）")
o = deliver(GRP.replace('''```
[2] #319 · "题面二"
原句 b ｜判定 ✅ 考点 ｜最小改 ＝原句 ｜更好版 无更好版本 ｜diff-1 无 diff ｜diff-2 无 diff
```
''', "").replace("（2 题）", "（1 题）"), DRAWN_OK)
ck("★ 负向：把 #319 从块头/标题里一起抹掉 ⇒ 对账抓住（此前 ERROR 0）",
   nerr(o) > 0 and "#319" in o, o[-500:])
o = deliver(GRP, f"{D}\t第 1 组\t用\t318\n")
ck("★ 负向：session 里有 drawn.log 没记的题 ⇒ 报「教练自己加题」",
   nerr(o) > 0 and "自己加题" in o, o[-400:])
o = deliver(GRP, f"{D}\t第 1 组\t用\t318\n{D}\t第 1 组\t免\t319\n")
ck("★ 负向：记了 ⚡ 免测却又出了题 ⇒ 报错", nerr(o) > 0 and "只能有一个" in o, o[-400:])
o = deliver(GRP, "")
ck("负向：drawn.log 这天一条流水都没有 ⇒ WARN「没跑过 pick」", "没跑过" in o, o[-400:])
o = deliver(GRP, f"{D}\t第 1 组\t抽\t318,319\n")
ck("负向：只有「抽」没有「用」⇒ WARN", "只有「抽」没有「用」" in o, o[-400:])

# ══════════════════════════════════════════════════════════════════════════
head("③b ★ 对账要减掉「弃」＋ 同组多行「用」以最后一行为准（2026-09-05 实测缺口）")
#  真事：#136 的题面被当天的粒度整改截断成裸词组，与 🎓#232 撞车 ⇒ 该记 ◎、该 `--dropped`，
#  可对账既不减「弃」、又对两行「用」取并集 ⇒ 撤两次都撤不掉，`deliver` 死活报缺 #136。
ONE = GRP.replace('''```
[2] #319 · "题面二"
原句 b ｜判定 ✅ 考点 ｜最小改 ＝原句 ｜更好版 无更好版本 ｜diff-1 无 diff ｜diff-2 无 diff
```
''', "").replace("（2 题）", "（1 题）")
DR_DROP = (f"{D}\t第 1 组\t用\t318,319\n"
           f"{D}\t第 1 组\t弃\t319=题面被整改截断，与 #318 撞车 ⇒ 教练把题面搞坏了（◎ §3.3）\n")
DR_RERUN = f"{D}\t第 1 组\t用\t318,319\n{D}\t第 1 组\t用\t318\n"

o = deliver(ONE, DR_DROP)
ck("★ 正向：drawn.log 记了 `弃 319=…`、session 里没有 #319 ⇒ ERROR 0", nerr(o) == 0, o[-500:])
o = deliver(GRP, DR_DROP)
ck("★ 正向：被弃的 #319 仍写进 session（＝ 判 ◎）⛔ 不算「教练自己加题」",
   nerr(o) == 0, o[-500:])
o = deliver(ONE, DR_RERUN)
ck("★ 正向：同组两行「用」、后一行撤掉 #319 ⇒ 以最后一行为准，ERROR 0", nerr(o) == 0, o[-500:])

o = deliver(ONE, f"{D}\t第 1 组\t用\t318\n{D}\t第 1 组\t用\t318,319\n")
ck("★ 负向：最后一行「用」里有 #319、session 里却没有 ⇒ 仍然报错",
   nerr(o) > 0 and "#319" in o, o[-500:])
ck("★ 负向：既没被弃、也在最后一行「用」里 ⇒ 闸⛔没被放宽", "出了题就必须有记录" in o, o[-500:])
o = deliver(ONE, DR_DROP.replace("319=", "999="))
ck("负向：弃的是别的号（#999）⇒ #319 照样必须出现", nerr(o) > 0 and "#319" in o, o[-500:])

with sandbox(sessions=False) as d:
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write(DR_DROP)
    dr = lab.drawn_rows(D)
    ck("★ 「弃」只认紧跟 `=` 的那个号：理由文本里的 `#318` ⛔ 不许被捡进来",
       dr["弃"] == {319}, dr["弃"])
    ck("「用」照旧读得到 318/319", dr["用"] == {318, 319}, dr["用"])
    ck("★ pick 与对账同口径：弃掉的号当天也⛔不再抽（§3.3 次日再测）",
       lab.read_drawn(D)[0] == {318, 319}, lab.read_drawn(D)[0])
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write(DR_RERUN)
    ck("★ drawn_rows 的「用」按最后一行算（#319 被撤）", lab.drawn_rows(D)["用"] == {318}, lab.drawn_rows(D)["用"])
    ck("★ read_drawn 同口径（⛔ 不能一边减掉、一边还算着）",
       lab.read_drawn(D)[0] == {318}, lab.read_drawn(D)[0])
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write(
        f"{D}\t第 1 组\t用\t318\n{D}\t第 2 组\t用\t319\n")
    ck("★ 「最后一行为准」只在**组内**生效，⛔ 不许把别组的盖掉",
       lab.drawn_rows(D)["用"] == {318, 319}, lab.drawn_rows(D)["用"])

# ══════════════════════════════════════════════════════════════════════════
head("④ 围栏跨节 —— 成对但把节标题吞了（未闭合检查抓不到）")
span = sess('''## ① 在池组 · 第 1 组（1 题）
```
[1] #318 · "题面一"
原句 a ｜判定 ✅ 考点 ｜最小改 ＝原句 ｜更好版 无更好版本 ｜diff-1 无 diff ｜diff-2 无 diff

## ② 回看 · bank:281

```
### 【本组新建条目】
无
''')
o = deliver(span, DRAWN_OK.replace(",319", ""))
ck("★ 负向：节标题落在围栏里 ⇒ 报错（围栏是成对的）",
   nerr(o) > 0 and "围栏" in o and "回看" in o, o[-500:])

# ══════════════════════════════════════════════════════════════════════════
head("⑤ 复检组判定值闭集（加粗／自造词此前全被当成「不是 ❌」⇒ 绕过三件套）")
RCK = sess('''## ①b 复检组 · 第 1 组（1 题 / 2 条）
```
[1] 打包 · #190 #232 · 词组串
判定 #190 ✅ ok
判定 #232 %s 掉了
```
### 【本组 ⚡ 免测】
无
''')
DR2 = f"{D}\t第 1 组\t用\t190,232\n"
o = deliver(RCK % "**❌**", DR2, section="复检组")
ck("★ 负向：`**❌**` 加粗 ⇒ **两件都报**：加粗违规 ＋ 照样按 ❌ 要三件套"
   "（此前加粗被当成「不是 ❌」⇒ 三件套闸整个绕过）",
   nerr(o) > 0 and "加粗" in o and "缺「最小改」" in o, o[-600:])
for v in ("稳", "掉", "?"):
    o = deliver(RCK % v, DR2, section="复检组")
    ck(f"负向：判定值写「{v}」⇒ 报错", nerr(o) > 0 and "闭集" in o)
o = deliver(RCK % "✅", DR2, section="复检组")
ck("正向：闭集内的 ✅ 放行", nerr(o) == 0, o[-400:])
# ★ 2026-09-05 实测缺口：SKILL §3.3 定义了 ◎，闸的闭集里却没有 ⇒ SKILL 允许的状态写不出来
o = deliver(RCK % "◎", DR2, section="复检组")
ck("★ 正向：裸 ◎（题面本身有毛病、本次作废 §3.3）⇒ ERROR 0", nerr(o) == 0, o[-500:])
ck("★ 正向：◎ ⛔ 不要求三件套（和 ✅ 一样只记一行判定）",
   "缺「最小改」" not in o and "缺「更好版」" not in o, o[-500:])
o = deliver(RCK % "**◎**", DR2, section="复检组")
ck("★ 负向：`**◎**` 加粗 ⇒ 照样报错（⛔ 只认裸符号，§3.3）",
   nerr(o) > 0 and "加粗" in o, o[-500:])

# ══════════════════════════════════════════════════════════════════════════
head("⑥ 付息日 ⛔ 不出新题（§5，此前无闸）")
R = sess('''## ① 在池组 · 第 1 组（1 题）
```
[1] #318 · "题面一"
原句 a ｜判定 ✅ 考点 ｜最小改 ＝原句 ｜更好版 无更好版本 ｜diff-1 无 diff ｜diff-2 无 diff
```
### 【本组新建条目】
无

## ③ 新题 · 第 1 道（bank:12）
### ① 最小修改版
x
### ② 更好版
y
### ③ 逐句 diff
```
[S1] 一句
diff-1  原句 → 最小改
  原句   aaa
  最小改 bbb
  · a → b   ❌ 理由
diff-2  无 diff
```
''', day="R")
o = deliver(R, f"{D}\t第 1 组\t用\t318\n")
ck("★ 负向：首行写着 R 却有【新题】节 ⇒ 报错", nerr(o) > 0 and "付息日" in o, o[-500:])
ck("正向：同一份改成 L1 ⇒ 不报这条",
   "付息日" not in deliver(R.replace("**R**", "**L1**"), f"{D}\t第 1 组\t用\t318\n"))

# ══════════════════════════════════════════════════════════════════════════
head("⑦ 崩溃与静默算错（B 组对抗挖出来的）")
SESSD = ["2026-09-01", "2026-09-02", "2026-09-03"]


def mk(d, days=SESSD):
    os.makedirs(os.path.join(d, "sessions"), exist_ok=True)
    for i, x in enumerate(days):
        open(os.path.join(d, "sessions", x + ".md"), "w", encoding="utf-8").write(
            f"# {x} · **L{i % 3 + 1}**\n\n## ① 在池组 · 第 1 组（0 题）\n")


def ent(n, kind="语法", status=None, rows=(), title="t"):
    return ("### %d · %s\n类型 %s ｜ 题面 \"中文。\"\n%s\n%s\n"
            % (n, title, kind, status or "状态 连对0 连错1 上次2026-09-01 未毕业",
               "\n".join(rows)))


PBIG = "# 问题总表\n\n---\n\n" + "\n".join(
    ent(100 + i, rows=["- 2026-09-01 ❌ x"]) for i in range(40))
GBIG = "# 已毕业档\n\n---\n\n" + "\n".join(
    ent(500 + i, status="状态 连对2 连错0 上次2026-09-01 ｜ **🎓 已毕业 2026-09-01**",
        rows=["- 2026-08-01 ✅", "- 2026-09-01 ✅"]) for i in range(40))

with sandbox(p_text=PBIG, g_text=GBIG, sessions=False) as d:
    mk(d)
    lab._PDAYS = None
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date="2026-09-04", dry=True, size=0))
    ck("★ 负向：--size 0 ⇒ 干净退出（此前抛 ValueError traceback）",
       st == "EXIT" and "要 ≥1" in out, (st, out[-200:]))
    st, rc, out = run(lab.cmd_pick, Args(type="learn", date="2026-09-04", dry=True, size=-3))
    ck("★ 负向：--size 负数 ⇒ 干净退出（此前静默出 0 组还谎报「没有到期的」）",
       st == "EXIT", (st, out[-200:]))
    st, rc, o1 = run(lab.cmd_pick, Args(type="learn", date="2026-09-04", dry=True))
    st, rc, o2 = run(lab.cmd_pick, Args(type="learn", date="2026-09-04", dry=True, scope="grad"))
    ck("★ 负向：--scope grad ⛔ 不许让复检配额翻倍（此前 1 组 → 4 组）",
       o2.count("复检组 · 第") == 1, o2.count("复检组 · 第"))
    ck("正向：--scope both 时复检 ＝ 1 ＋ 下溢", o1.count("复检组 · 第") >= 1)

# append 少一个文件不许崩
with sandbox(p_text=PBIG, g_text=None, sessions=False) as d:
    mk(d)
    os.remove(os.path.join(d, "graduated.md"))
    f = os.path.join(d, "rows.md")
    open(f, "w", encoding="utf-8").write("#100 ✅ 组1\n")
    st, rc, out = run(lab.cmd_append, Args(file=f, date="2026-09-04"))
    ck("★ 负向：graduated.md 不存在时 append ⛔ 不崩（别的子命令都容忍）",
       st == "OK" and rc == 0, (st, rc, out[-300:]))

# 「连对到 2、还没手标 🎓」的工作流窗口
P2 = "# 问题总表\n\n---\n\n" + ent(
    777, status="状态 连对2 连错0 上次2026-09-03 未毕业",
    rows=["- 2026-09-02 ✅", "- 2026-09-03 ✅"])
with sandbox(p_text=P2, g_text="# 已毕业档\n", sessions=False) as d:
    mk(d)
    lab._PDAYS = None
    e = [x for x in lab.load_all() if x.num == 777][0]
    ck("★ 连对≥2 未毕业（等着手标 🎓）⇒ 落在 rung2，⛔ 不倒退到 rung0",
       e.base_rung() == 2 and e.rung() == 2, (e.base_rung(), e.rung()))
    ck("⛔ 卡片不许把它写成「首测未做」", "首测未做" not in e.rung_name(), e.rung_name())

# 反向通道：她说「这条我没底」
P3 = "# 问题总表\n\n---\n\n" + ent(
    888, status="状态 连对1 连错0 上次2026-09-02 未毕业",
    rows=["- 2026-09-02 ✅ 复习", "- 2026-09-03 📝 她自评没底 · 优先召回"])
with sandbox(p_text=P3, g_text="# 已毕业档\n", sessions=False) as d:
    mk(d)
    lab._PDAYS = None
    e = [x for x in lab.load_all() if x.num == 888][0]
    ck("★ 正向：`📝 她自评没底 · 优先召回` ⇒ 梯子钳到 rung0（下个练习日必出）",
       e.pulled_back() and e.rung() == 0, (e.pulled_back(), e.rung()))
    ck("⛔ 状态行一个字没动（连对仍是 1，⛔ 不伪造 ❌、不改状态）",
       e.recount() == (1, 0), e.recount())
    ck("check ⛔ 不因此报错",
       not [1 for lv, m in lab.check_entry(e, set(), {888}) if lv == "ERROR"],
       [m for lv, m in lab.check_entry(e, set(), {888}) if lv == "ERROR"])
P4 = P3.replace("- 2026-09-03 📝 她自评没底 · 优先召回",
                "- 2026-09-03 📝 她自评没底 · 优先召回\n- 2026-09-04 ✅ 复检答对了")
with sandbox(p_text=P4, g_text="# 已毕业档\n", sessions=False) as d:
    mk(d, SESSD + ["2026-09-04"])
    lab._PDAYS = None
    e = [x for x in lab.load_all() if x.num == 888][0]
    ck("★ 自动失效：之后被判定过 ⇒ 标记过期，⛔ 不用谁去清",
       not e.pulled_back() and e.rung() == 2, (e.pulled_back(), e.rung()))

# ⚡ 对账
with sandbox(p_text=PBIG, g_text=GBIG, sessions=False) as d:
    mk(d)
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write(
        "2026-09-10\t第 1 组\t免\t500,501\n")
    a = lab.selfpass_audit()
    ck("★ 负向：drawn.log 记了免测、档案里没写 ⚡ ⇒ ERROR（§11①b 的唯一闸）",
       any(x[0] == "ERROR" and "#500" in x[2] for x in a), a)
    g2 = read(d, "graduated.md").replace(
        "### 500 · t\n类型 语法 ｜ 题面 \"中文。\"\n"
        "状态 连对2 连错0 上次2026-09-01 ｜ **🎓 已毕业 2026-09-01**\n"
        "- 2026-08-01 ✅\n- 2026-09-01 ✅\n",
        "### 500 · t\n类型 语法 ｜ 题面 \"中文。\"\n"
        "状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-09-01**\n"
        "- 2026-08-01 ✅\n- 2026-09-01 ✅\n- 2026-09-10 ⚡ 自评免测\n")
    open(os.path.join(d, "graduated.md"), "w", encoding="utf-8").write(g2)
    a = lab.selfpass_audit()
    ck("正向：补上 #500 的 ⚡ 之后只剩 #501 报错",
       [x for x in a if x[0] == "ERROR"] and "#501" in a[0][2] and "#500" not in a[0][2], a)
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write("")
    a = lab.selfpass_audit()
    ck("负向反向：档案有 ⚡ 但 drawn.log 没记 ⇒ WARN 不是 ERROR",
       all(x[0] != "ERROR" for x in a), a)

head("④ 「用」⇄ 判定行 对账（2026-09-07 补的闸 —— ⚡ 那道闸的另一半）")
# ⚠️ 上线理由：2026-09-05 两个复检组共 34 条判了、写进了 session，却整组没交给 append；
#   当天 check／stats／deliver 三条全绿 ⇒ 两天后整组被重新抽出来重考。
with sandbox(p_text=PBIG, g_text=GBIG, sessions=False) as d:
    mk(d)
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write(
        "2026-09-10\t第 1 组\t抽\t500,501\n2026-09-10\t第 1 组\t用\t500,501\n")
    a = lab.used_audit()
    ck("★ 负向：drawn.log 记了「用」、档案里没有那天的判定行 ⇒ ERROR",
       any(x[0] == "ERROR" and "#500" in x[2] and "#501" in x[2] for x in a), a)
    g2 = read(d, "graduated.md").replace(
        "状态 连对2 连错0 上次2026-09-01 ｜ **🎓 已毕业 2026-09-01**\n"
        "- 2026-08-01 ✅\n- 2026-09-01 ✅\n",
        "状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-09-01**\n"
        "- 2026-08-01 ✅\n- 2026-09-01 ✅\n- 2026-09-10 ✅ 复检\n", 1)
    open(os.path.join(d, "graduated.md"), "w", encoding="utf-8").write(g2)
    a = lab.used_audit()
    ck("正向：补上第一条的判定行之后，只剩另一条报错",
       [x for x in a if x[0] == "ERROR"] and "#501" in a[0][2] and "#500" not in a[0][2], a)

    # 「免」与「弃」都不进这道闸（§9.1④ 弃不参与对账；免走 selfpass_audit）
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write(
        "2026-09-10\t第 1 组\t用\t500,501\n"
        "2026-09-10\t第 1 组\t免\t501\n")
    ck("★ 正向：被「免」掉的那条 ⛔ 不进「用」对账（免走 ⚡ 那道闸）",
       all(x[0] != "ERROR" for x in lab.used_audit()), lab.used_audit())
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write(
        "2026-09-10\t第 1 组\t用\t500,501\n"
        "2026-09-10\t第 1 组\t弃\t501=题面被截断，本次作废\n")
    ck("★ 正向：被「弃」掉的那条 ⛔ 不进「用」对账（§9.1④）",
       all(x[0] != "ERROR" for x in lab.used_audit()), lab.used_audit())

    # 反向不查：自由产出（新题／重答）判的号本来就不进 drawn.log
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write("")
    ck("正向：档案有判定行但 drawn.log 没记 ⇒ 一条都不报（自由产出的常态）",
       lab.used_audit() == [], lab.used_audit())

    # 闸的分界线：DELIVER_FROM 之前的日子不回扫
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write(
        "2026-08-20\t第 1 组\t用\t500,501\n")
    ck("正向：分界线之前的存量日子 ⛔ 不回扫",
       lab.used_audit() == [], lab.used_audit())

sys.exit(report("2026-09-05 演练补的闸 正/负向测试"))
