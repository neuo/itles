#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""复检组的三道闸 —— deliver 交付契约 / check ⚡ 契约 / count 新口径。正向＋负向。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import lab, ck, head, report, sandbox, run, Args

D = "2026-09-10"          # ≥ DELIVER_FROM ⇒ 硬查


def sess(body):
    return f"# {D} · **L1**\n\n" + body


GOOD = sess('''## ①b 复检组 · 第 1 组（2 题 / 4 条）
```
[1] 打包 · #190 #232 #233 · 中译英词组串
判定 #190 ✅ clear the table
判定 #232 ✅ to be honest
判定 #233 ✅ either way
```
```
[2] #205 · "市场变了。"
原句   the market has changed
判定 #205 ❌ 掉了 the
最小改 The market has changed.
更好版 无更好版本
diff-1  原句 → 最小改
  原句   the market has changed
  最小改 The market has changed.
  · market → the market   ❌ 系统性名词带 the
diff-2  最小改 → 更好版
  无 diff（＝上一版）
```
### 【本组 ⚡ 免测】
无
''')


def deliver(txt, section="复检组"):
    with sandbox(sessions=False) as d:
        os.makedirs(os.path.join(d, "sessions"), exist_ok=True)
        p = os.path.join(d, "sessions", D + ".md")
        open(p, "w", encoding="utf-8").write(txt)
        return run(lab.cmd_deliver, Args(session=p, section=section))[2]


def nerr(out):
    import re
    m = re.search(r"ERROR (\d+)", out)
    return int(m.group(1)) if m else -1


head("① deliver 复检组 —— 正向")
o = deliver(GOOD)
ck("合格的复检组节 ERROR 0", nerr(o) == 0, o[-700:])

head("② deliver 复检组 —— 负向（每个功能点各打一枪）")
cases = [
    ("标题只写题数、不写条数",
     GOOD.replace("（2 题 / 4 条）", "（2 题）"), "两个数都写"),
    ("题数与块数对不上",
     GOOD.replace("（2 题 / 4 条）", "（3 题 / 4 条）"), "只有 2 个"),
    ("条数与块头列的号对不上",
     GOOD.replace("（2 题 / 4 条）", "（2 题 / 9 条）"), "实际列了 4 条"),
    ("★ 打包题漏判一条（#232 没有判定行）",
     GOOD.replace("判定 #232 ✅ to be honest\n", ""), "缺 #232"),
    ("★ 判定行的号不在块头里",
     GOOD.replace("判定 #233 ✅ either way", "判定 #999 ✅ either way"), "#999"),
    ("一个块里两条 ❌（该拆开）",
     GOOD.replace("判定 #190 ✅ clear the table", "判定 #190 ❌ clear the table")
         .replace("判定 #232 ✅ to be honest", "判定 #232 ❌ to be honest"), "拆成各自的块"),
    ("❌ 的题缺「最小改」",
     GOOD.replace("最小改 The market has changed.\n", "", 1), "缺「最小改」"),
    ("❌ 的题缺「更好版」",
     GOOD.replace("更好版 无更好版本\n", ""), "缺「更好版」"),
    ("❌ 的题缺 diff-2 段",
     GOOD.replace("diff-2  最小改 → 更好版\n  无 diff（＝上一版）\n", ""), "diff-2"),
    ("★ diff 有改动却只写 xxx → yyy，没摆两行完整句",
     GOOD.replace("  原句   the market has changed\n"
                  "  最小改 The market has changed.\n", ""), "没摆两行完整句"),
    # ★ 省略号闸（2026-09-05 补，漏洞 B 的第四类行）：❌ 那条的三件套同样必须是完整句
    ("★ ❌ 的题 diff 起点句用 … 截断",
     GOOD.replace("  原句   the market has changed",
                  "  原句   … the market has changed"), "省略号截断"),
    ("★ ❌ 的题 diff 终点句用 ... 截断",
     GOOD.replace("  最小改 The market has changed.",
                  "  最小改 ... The market has changed."), "省略号截断"),
    ("★ ❌ 的题「最小改」用 … 拼接（全文，一句都不省）",
     GOOD.replace("\n最小改 The market has changed.",
                  "\n最小改 … The market has changed …"), "一句都不省"),
    ("同一条在一节里出现两次",
     GOOD.replace("[2] #205 ·", "[2] #190 ·"), "出现两次"),
    ("★ 缺【本组 ⚡ 免测】块",
     GOOD.replace("### 【本组 ⚡ 免测】\n无\n", ""), "免测"),
    ("围栏没闭合",
     GOOD.replace("判定 #233 ✅ either way\n```", "判定 #233 ✅ either way"), "没闭合"),
]
for name, txt, want in cases:
    o = deliver(txt)
    ck(f"负向：{name} ⇒ 报错", nerr(o) > 0 and want in o, o[-600:])

head("③ deliver 复检组 —— 边界（不该误报的）")
ok_cases = [
    ("全 ✅ 的打包题不要求三件套", GOOD),
    ("单条题（非打包）也认",
     GOOD.replace("[1] 打包 · #190 #232 #233 · 中译英词组串\n"
                  "判定 #190 ✅ clear the table\n"
                  "判定 #232 ✅ to be honest\n"
                  "判定 #233 ✅ either way",
                  "[1] #190 · \"他把桌上收拾了。\"\n判定 #190 ✅ clear the table")
         .replace("（2 题 / 4 条）", "（2 题 / 2 条）")),
    ("⚡ 免测块里写了条目号也算写了",
     GOOD.replace("### 【本组 ⚡ 免测】\n无", "### 【本组 ⚡ 免测】\n#232 #233（她说会了）")),
    ("节标题写成 `## 复检组 · 第 1 组` 也认",
     GOOD.replace("## ①b 复检组", "## 复检组")),
]
for name, txt in ok_cases:
    o = deliver(txt)
    ck(f"正向：{name}", nerr(o) == 0, o[-600:])

head("③b ★ ◎ ＝ 题面本身有毛病、本次作废（§3.3）—— SKILL 允许的档位，闸必须写得出来")
#  2026-09-05 实测：#136 的题面被当天的粒度整改截断成裸词组「说了实话」，与 🎓#232「说实话」
#  撞车，她答 to be honest ⇒ 这是教练把题面搞坏了，按 §3.3 该记 ◎，闸却判 ERROR。
VOID = GOOD.replace("判定 #233 ✅ either way",
                    "判定 #233 ◎ 题面被截断成裸词组、与 #232 撞车 —— 教练把题面搞坏了")
o = deliver(VOID)
ck("★ 正向：复检块里 `判定 #N ◎ <理由>` ⇒ ERROR 0", nerr(o) == 0, o[-700:])
ck("★ 正向：◎ 的块⛔不要求三件套（一行判定就够 —— 对着坏题面教 ＝ 教错东西）",
   "缺「最小改」" not in o and "缺「更好版」" not in o and "diff-1" not in o, o[-700:])

o = deliver(GOOD.replace("判定 #233 ✅ either way", "判定 #233 **◎** 题面坏了"))
ck("★ 负向：`**◎**` 加粗 ⇒ 报错（⛔ 只认裸符号，§3.3 符号紧跟、不加粗）",
   nerr(o) > 0 and "加粗" in o, o[-700:])
for v in ("稳", "掉", "?", "作废"):
    o = deliver(GOOD.replace("判定 #233 ✅ either way", f"判定 #233 {v} xxx"))
    ck(f"负向：判定值写「{v}」⇒ 仍然报错（闭集只多了 ◎，⛔ 没放宽别的）",
       nerr(o) > 0 and "闭集" in o, o[-700:])

# ★ §6.1⑤「一个块里最多一条 ❌」的计数里，◎ ⛔ 不算 ❌
MIX = (GOOD.replace('[2] #205 · "市场变了。"',
                    "[2] 打包 · #205 #206 · 中译英词组串")
           .replace("判定 #205 ❌ 掉了 the",
                    "判定 #205 ❌ 掉了 the\n判定 #206 ◎ 题面缺主语（教练现编）")
           .replace("（2 题 / 4 条）", "（2 题 / 5 条）"))
o = deliver(MIX)
ck("★ 正向：一个块里 一条 ❌ ＋ 一条 ◎ ⇒ ERROR 0（◎ ⛔ 不计进「最多一条 ❌」）",
   nerr(o) == 0, o[-700:])
o = deliver(MIX.replace("判定 #206 ◎ 题面缺主语（教练现编）", "判定 #206 ❌ 也掉了"))
ck("★ 负向：同一个块里两条 ❌ ⇒ 仍然报错（⛔ 没被 ◎ 顺手放宽）",
   nerr(o) > 0 and "拆成各自的块" in o, o[-700:])

head("④ 存量分界线 —— 2026-09-05 之前只提示不报错")
old = GOOD.replace(f"# {D}", "# 2026-09-01")
with sandbox(sessions=False) as d:
    os.makedirs(os.path.join(d, "sessions"), exist_ok=True)
    p = os.path.join(d, "sessions", "2026-09-01.md")
    open(p, "w", encoding="utf-8").write(
        old.replace("（2 题 / 4 条）", "（2 题）"))
    o = run(lab.cmd_deliver, Args(session=p, section="复检组"))[2]
ck("存量 session 的复检组问题 ⇒ 只提示，ERROR 0", nerr(o) == 0, o[-400:])

# ══════════════════════════════════════════════════════════════════════════
head("⑤ check —— ⚡ 的语义（2026-09-05 改：⚡ ＝ 一次通过，⛔ 不设任何类型限制）")


def one(status, rows):
    body = "### 5 · t\n类型 词组 ｜ 题面 \"x\"\n" + status + "\n" + "\n".join(rows) + "\n"
    return "# 问题总表\n\n---\n\n" + body


def errs(p_text, g_text="# 已毕业档\n"):
    with sandbox(p_text=p_text, g_text=g_text, sessions=False) as d:
        os.makedirs(os.path.join(d, "sessions"), exist_ok=True)
        ents = lab.load_all()
        nums = {e.num for e in ents}
        return [(lv, m) for e in ents for lv, m in lab.check_entry(e, set(), nums)]


G_OK = ("# 已毕业档\n\n---\n\n### 5 · t\n类型 词组 ｜ 题面 \"x\"\n"
        "状态 连对2 连错0 上次2026-09-06 ｜ **🎓 已毕业 2026-09-02**\n"
        "- 2026-09-01 ✅ a\n- 2026-09-02 ✅ b\n- 2026-09-06 ⚡ 自评免测\n")
e = errs("# 问题总表\n", G_OK)
ck("正向：毕业条目上的 ⚡ ⇒ 不报错", not [x for x in e if x[0] == "ERROR"], e)

# ★ 她 2026-09-05 原话："这个事情就我来决策……你不要加额外的限制"
P_POOL = one("状态 连对1 连错0 上次2026-09-06 未毕业",
             ["- 2026-09-02 ❌ a", "- 2026-09-06 ⚡ 自评免测"])
e = errs(P_POOL)
ck("★ 正向：**在池条目**上的 ⚡ 也合法（⛔ 脚本不许替她加类型限制）",
   not [x for x in e if x[0] == "ERROR"], e)

# ⚡ → 回潮 → 重新毕业：设计里的正常循环，旧周期的 ⚡ ⛔ 不许被判违规
G_CYCLE = ("# 已毕业档\n\n---\n\n### 5 · t\n类型 词组 ｜ 题面 \"x\"\n"
           "状态 连对2 连错0 上次2026-09-12 ｜ **🎓 已毕业 2026-09-12**\n"
           "- 2026-09-01 ✅\n- 2026-09-02 ✅\n"
           "- 2026-09-06 ⚡ 自评免测（上一个毕业周期里的）\n"
           "- 2026-09-08 ❌ 回潮\n- 2026-09-10 ✅\n- 2026-09-12 ✅\n")
e = errs("# 问题总表\n", G_CYCLE)
ck("★ 正向：⚡ → 回潮 → 重新毕业，旧周期的 ⚡ ⛔ 不报错",
   not [x for x in e if x[0] == "ERROR"], e)

with sandbox(p_text="# 问题总表\n", g_text=G_OK, sessions=False) as d:
    E = {x.num: x for x in lab.load_all()}
    ck("⚡ ⛔ 不推进毕业条目的连对（冻结在毕业日，仍 连对2）", E[5].recount() == (2, 0))
    ck("⚡ 计入 rc ⇒ 从 rung3 爬到 rung4", E[5].rechecks() == 1 and E[5].rung() == 4)
    ck("★ ⚡ **清零等待时钟**（有效上次 ＝ ⚡ 那天）—— 否则免测的比答对的还早回来",
       E[5].eff_last() == "2026-09-06", E[5].eff_last())

with sandbox(p_text=P_POOL, g_text="# 已毕业档\n", sessions=False) as d:
    E = {x.num: x for x in lab.load_all()}
    ck("在池条目上的 ⚡ 推进连对（0→1）", E[5].recount() == (1, 0), E[5].recount())
    ck("在池的 ⚡ 不计 rc（还没毕业）", E[5].rechecks() == 0)

head("⑥ count —— 新口径")
G_CAL = ("# 已毕业档\n\n---\n\n### 6 · t\n类型 词组 ｜ 题面 \"x\"\n"
         "状态 连对2 连错0 上次2026-09-02 ｜ **🎓 已毕业 2026-09-02**\n"
         "- 2026-09-01 ✅\n- 2026-09-02 ✅\n- 2026-09-06 ⚡ 自评免测\n"
         "- 2026-09-08 ❌ 又掉了\n")
with sandbox(p_text="# 问题总表\n", g_text=G_CAL, sessions=False) as d:
    os.makedirs(os.path.join(d, "sessions"), exist_ok=True)
    E = {x.num: x for x in lab.load_all()}
    ck("selfpass 认得出 ⚡ 条目", bool(E[6].selfpassed()))
    ck("★ selfpass-fell ＝ ⚡ 之后又掉过（自评校准数）", lab._selfpass_fell(E[6]))
    st, rc, o = run(lab.cmd_count, Args(type="rung:3"))
    ck("count --type rung:N 能跑", "梯子第 3 格" in o, o[:300])
    st, rc, o = run(lab.cmd_count, Args(type="rung:99"))
    ck("负向：rung 超范围 ⇒ 退出", st == "EXIT")
    st, rc, o = run(lab.cmd_count, Args(type="不存在的类型"))
    ck("负向：瞎编 slug ⇒ 退出", st == "EXIT")
    st, rc, o = run(lab.cmd_count, Args())
    ck("全表里有 due / risk / selfpass / rung 各行",
       all(k in o for k in ("due", "risk", "selfpass", "rung:0", "rung:7")))

# ══════════════════════════════════════════════════════════════════════════
head("⑦ append —— 复检的判定行要能落进 graduated.md（2026-09-05 放开）")
PT = ("# 问题总表\n\n---\n\n"
      "### 1 · 在池条目\n"
      "类型 语法 ｜ 题面 \"x\"\n"
      "状态 连对0 连错1 上次2026-09-02 未毕业\n"
      "- 2026-09-02 ❌ a\n")
GT = ("# 已毕业档\n\n---\n\n"
      "### 2 · 毕业条目\n"
      "类型 词组 ｜ 题面 \"y\"\n"
      "状态 连对2 连错0 上次2026-09-02 ｜ **🎓 已毕业 2026-09-02**\n"
      "- 2026-09-01 ✅\n- 2026-09-02 ✅\n- 备注 一条尾块\n\n"
      "### 3 · 形态条目\n"
      "类型 语法 ｜ 题面 \"z\"\n"
      "状态 连对2 连错0 上次2026-09-02 ｜ **🎓 已毕业 2026-09-02** ｜ 形态类·不召回\n"
      "- 2026-09-01 ✅\n- 2026-09-02 ✅\n\n"
      "### 4 · （已并入 #2）\n"
      "类型 词组 ｜ 题面 \"w\"\n"
      "状态 连对0 连错0 上次— 未毕业\n"
      "- 2026-09-02 📝 并入\n")
TD = "2026-09-10"


def app(rows, p=PT, g=GT, dry=False):
    with sandbox(p_text=p, g_text=g, sessions=False) as d:
        os.makedirs(os.path.join(d, "sessions"), exist_ok=True)
        f = os.path.join(d, "rows.md")
        open(f, "w", encoding="utf-8").write(rows)
        st, rc, out = run(lab.cmd_append, Args(file=f, date=TD, dry_run=dry))
        return (rc, out,
                open(os.path.join(d, "problems.md"), encoding="utf-8").read(),
                open(os.path.join(d, "graduated.md"), encoding="utf-8").read())


rc, out, p, g = app("#2 ✅ 复检第1组 · 稳\n")
ck("★ ✅ 落进 graduated.md", rc == 0 and ("- %s ✅ 复检第1组 · 稳" % TD) in g, out[-600:])
ck("插在日期行之后、`- 备注` 之前", g.index("- %s ✅" % TD) < g.index("- 备注 一条尾块"))
ck("毕业条目连对/连错冻结不变（仍是 连对2 连错0）", "状态 连对2 连错0" in g)
ck("「上次」跟着推进到今天", ("上次%s" % TD) in g)
ck("⛔ 没碰 problems.md", p == PT)

rc, out, p, g = app("#2 ⚡ 自评免测 · 复检第1组\n")
ck("★ ⚡ 也能落盘", rc == 0 and ("- %s ⚡ 自评免测" % TD) in g, out[-600:])
with sandbox(p_text=PT, g_text=g, sessions=False) as d:
    E = {x.num: x for x in lab.load_all()}
    ck("★ ⚡ 落盘后 rc ＋1、爬一格（rung3 → rung4）",
       E[2].rechecks() == 1 and E[2].rung() == 4)
    ck("★ ⚡ ⛔ 不推进连对（仍 连对2 连错0）", E[2].recount() == (2, 0))

rc, out, p, g = app("#2 ❌ 复检第1组 · 掉了\n")
ck("★ ❌ 能落进 graduated.md（回潮的证据先记下）", rc == 0 and ("- %s ❌" % TD) in g)
ck("★ 脚本⛔不代改状态，只打「回潮」待办",
   "回潮：要你把状态行改回未毕业" in out and "🎓 已毕业 2026-09-02" in g, out[-400:])

rc, out, p, g = app("#1 ✅ 组1\n#2 ✅ 组1\n")
ck("★ 一批里跨两个文件都能写",
   rc == 0 and ("- %s ✅ 组1" % TD) in p and ("- %s ✅ 组1" % TD) in g, out[-600:])
ck("报告里写清哪个文件各写了几条",
   "problems.md 1 条" in out and "graduated.md 1 条" in out, out[-600:])

rc, out, p, g = app("#3 ✅ 组1\n")
ck("负向：形态类条目仍拒记 ✅", rc == 1 and "形态类" in out)
rc, out, p, g = app("#4 ✅ 组1\n")
ck("负向：墓碑条目仍拒记", rc == 1 and "墓碑" in out)
rc, out, p, g = app("#99 ✅ 组1\n")
ck("负向：查无此号", rc == 1 and "查无此编号" in out)

# 写完自查不过 ⇒ 两个文件一起回滚。用打桩制造「只在写完之后才出现」的 ERROR ——
# ⛔ 不能拿档案里本来就有的毛病来测：那些进 pre_err，按设计**不该**阻断（会误判成通过）。
_real_check = lab.check_entry


def _stub(e, touched=None, nums=None):
    out = list(_real_check(e, touched, nums))
    if e.num == 2 and any(h.date == TD for h in e.history):
        out.append(("ERROR", "打桩：只在写完之后才出现的错"))
    return out


lab.check_entry = _stub
try:
    rc, out, p, g = app("#1 ✅ 组1\n#2 ✅ 组1\n")
finally:
    lab.check_entry = _real_check
ck("★ 负向：写完自查不过 ⇒ **两个文件一起整批回滚**",
   rc == 1 and p == PT and g == GT and "整批回滚" in out, (rc, out[-500:]))
ck("回滚后 problems.md 逐字节还原", p == PT)
ck("回滚后 graduated.md 逐字节还原", g == GT)

rc, out, p, g = app("#1 ✅ 组1\n#2 ✅ 组1\n", dry=True)
ck("--dry-run 一个字不写", p == PT and g == GT)
ck("--dry-run 打出两个文件的落点", "problems.md L" in out and "graduated.md L" in out)

sys.exit(report("lab.py 复检组 deliver/check/count/append 正/负向测试"))

