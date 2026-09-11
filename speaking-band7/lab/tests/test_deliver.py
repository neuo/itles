#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py deliver / lookback 的正向／负向对抗测试。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, read, lab, LAB

GOOD = """# 2026-09-09 · L2 · 周期 5

## ① 复习组 · 第 1 组（2 题）

```
[1] #12 · "他劝我耐心点。"
原句   I keep patient.
判定   ❌ 考点：keep → stay
最小改 I stay patient.
更好版 无更好版本

diff-1  原句 → 最小改
  原句   I keep patient.
  最小改 I stay patient.
  · keep patient → stay patient
    ❌ 状态动词用 stay。
diff-2  最小改 → 更好版
  无 diff（＝上一版）
```

```
[2] #34 · "我七点到家。"
原句   I get to home at seven.
判定   ❌ 考点：get home
最小改 I get home at seven.
更好版 I'm usually home by seven.

diff-1  原句 → 最小改
  原句   I get to home at seven.
  最小改 I get home at seven.
  · get to home → get home
    ❌ home 是副词。
diff-2  最小改 → 更好版
  最小改 I get home at seven.
  更好版 I'm usually home by seven.
  · 更口语。
```

### 【本组新建条目】

**无。**

## ② 回看 · bank:875

四件套逐字取自 2026-09-04.md。

## ③ 新题 · 第 1 道（bank:1234 · 自由产出 · cold）

### ① 最小修改版

> I need a box to put these things in.

### ② 更好版

> I need a box for these things.

### ③ 逐句 diff

```
[S1] I need a box to put these thing in.
diff-1  原句   I need a box to put these thing in.
        最小改 I need a box to put these things in.
  · thing → things
diff-2  最小改 I need a box to put these things in.
        更好版 I need a box for these things.
  · 更简。
```

## ④ 收尾核对

（略）
"""


def sess(d, text, name="2026-09-09.md"):
    p = os.path.join(d, "sessions", name)
    open(p, "w", encoding="utf-8").write(text)
    # ★★ 合成 session ⇒ 真 drawn.log 必须清空（§0.1.6「测试⛔不许依赖真档案的内容」）。
    #   2026-09-11 实证：09-09 上线的「用⇄块」对账闸（§9.1④）拿真 drawn.log 里 09-09 的
    #   「用」去对这份合成 session ⇒ D0/D4b/D7 共 9 条当场变红，而 lab.py 一行都没错。
    #   需要流水的用例自己往 d/drawn.log 里写（test_gates 一直是这么做的）。
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write("")
    return p


def run_deliver(d, text, name="2026-09-09.md", **kw):
    return run(lab.cmd_deliver, Args(session=sess(d, text, name), **kw))


def fresh(d):
    """清空 sessions/ —— 只留本用例自己写的那几份。
    ⛔ 真 session 是会变的生产数据：lookback 扫的是**整个目录**，
       借真 session 当背景板 ＝ 判据挂在"今天写了什么"上（2026-09-05 已实证会红）。"""
    sd = os.path.join(d, "sessions")
    os.makedirs(sd, exist_ok=True)
    for f in os.listdir(sd):
        os.remove(os.path.join(sd, f))
    return sd


head("【D0 正】完全合规的 session ⇒ ERROR 0")
with sandbox() as d:
    st, rc, out = run_deliver(d, GOOD)
    ck("退出码 0", (st, rc) == ("OK", 0), out[-700:])
    ck("结论是可以发", "可以发" in out, out[-300:])
    ck("认出 4 个节（组/回看/新题/收尾闭合）",
       "group@" in out and "look@" in out and "new@" in out, out[:400])
    ck("日期 ≥ DELIVER_FROM ⇒ 硬查（不是存量）", "存量" not in out.split("──")[1], out[:400])

head("【D1 正】--section 只查指定节")
with sandbox() as d:
    for sec in ("复习组", "新题", "回看"):
        st, rc, out = run_deliver(d, GOOD, section=sec)
        ck(f"--section {sec} 跑得动且 ERROR 0", (st, rc) == ("OK", 0), out[-300:])
    st, rc, out = run_deliver(d, GOOD, section="乱写的")
    ck("--section 乱写 ⇒ 退出", st == "EXIT" and "只认" in out, out[-200:])

head("【D2 负】三件套缺项 —— 六项每项都要能被抓到")
LABELS = ["原句", "判定", "最小改", "更好版", "diff-1", "diff-2"]
with sandbox() as d:
    for lab_ in LABELS:
        bad = "\n".join(l for l in GOOD.split("\n")
                        if not l.strip().startswith(lab_) or "[2]" in l)
        # 只删第 1 题的那一行
        lines, killed, seen1 = [], False, False
        for l in GOOD.split("\n"):
            if l.startswith("[1] "):
                seen1 = True
            if l.startswith("[2] "):
                seen1 = False
            if seen1 and l.strip().startswith(lab_) and not killed:
                killed = True
                continue
            lines.append(l)
        st, rc, out = run_deliver(d, "\n".join(lines))
        ck(f"[1] 缺「{lab_}」⇒ ERROR、不许发",
           rc == 1 and lab_ in out and "不许发" in out, (rc, out[-400:]))

head("【D3 负】题数对不上 ／ 一个块都没有")
with sandbox() as d:
    st, rc, out = run_deliver(d, GOOD.replace("（2 题）", "（3 题）"))
    ck("标题写 3 题实际 2 块 ⇒ ERROR", rc == 1 and "标题写着 3 题" in out, out[-300:])
    st, rc, out = run_deliver(d, GOOD.replace("## ① 复习组 · 第 1 组（2 题）",
                                              "## ① 复习组 · 第 1 组"))
    ck("标题没写题数 ⇒ ERROR", rc == 1 and "没写（N 题）" in out, out[-300:])
    nb = GOOD.split("### 【本组新建条目】")[0].split("## ① 复习组")[0] + \
         "## ① 复习组 · 第 1 组（2 题）\n\n（什么块都没有）\n\n### 【本组新建条目】\n无\n" + \
         GOOD.split("### 【本组新建条目】")[1].split("## ② 回看")[1].join(["## ② 回看", ""])
    st, rc, out = run_deliver(d, "# 2026-09-09 · L2\n\n## ① 复习组 · 第 1 组（2 题）\n\n（空）\n")
    ck("一个三件套块都没有 ⇒ ERROR", rc == 1 and "一个三件套块都没有" in out, out[-400:])

head("【D4 负】diff 只写 xxx → yyy，没摆两行完整句")
with sandbox() as d:
    bad = GOOD.replace("""diff-1  原句 → 最小改
  原句   I keep patient.
  最小改 I stay patient.
  · keep patient → stay patient
    ❌ 状态动词用 stay。""",
                       """diff-1  原句 → 最小改
  · keep patient → stay patient""")
    st, rc, out = run_deliver(d, bad)
    ck("⇒ ERROR 且点名「不算 diff」", rc == 1 and "不算 diff" in out, out[-400:])

# ══════════════════════════════════════════════════════════════════════════
#  D4b 省略号闸（2026-09-05 补）—— 漏洞 B：完整句被 … 截断，闸却放过
#  覆盖四类行：① diff 两段的起点/终点句 ② 块内 最小改/更好版
#              ③ 自由产出 `### ① 最小修改版`/`### ② 更好版` 正文 ④ 复检 ❌ 那条（在 test_recheck）
#  ⛔ 不查题面行与 `原句` 行 —— 那是她的原话逐字，她自己打的省略号不算违规。
# ══════════════════════════════════════════════════════════════════════════
head("【D4b 正】完整句摆齐 ／ 固定写法（无 diff・无更好版本）⇒ 不误伤")
with sandbox() as d:
    st, rc, out = run_deliver(d, GOOD)
    ck("合规 session 里一条省略号报警都没有", rc == 0 and "省略号" not in out, out[-400:])
    for name, txt in [
        ("题面行带省略号（她的原话）",
         GOOD.replace('[1] #12 · "他劝我耐心点。"', '[1] #12 · "他劝我耐心点……"')),
        ("块内 `原句` 行带省略号（她的原话逐字）",
         GOOD.replace("\n原句   I keep patient.", "\n原句   I keep patient …")),
        ("diff 里的 `· aaa → bbb` 理由行带省略号",
         GOOD.replace("  · keep patient → stay patient",
                      "  · keep patient → stay patient（… 之类的状态词同族）")),
        ("`更好版 无更好版本` 这句固定写法",
         GOOD),
    ]:
        st, rc, out = run_deliver(d, txt)
        ck(f"{name} ⇒ ERROR 0", rc == 0 and "省略号" not in out, out[-400:])

head("【D4b 负】① diff 两段的起点句／终点句 ⛔ 不许带省略记号")
with sandbox() as d:
    cases = [
        ("diff-1 起点句带 `…`（U+2026）",
         GOOD.replace("  原句   I keep patient.", "  原句   … I keep patient."), "起点句"),
        ("diff-1 终点句带 `…`",
         GOOD.replace("  最小改 I stay patient.", "  最小改 I stay patient …"), "终点句"),
        ("diff-2 起点句带 `...`（三个半角点）",
         GOOD.replace("  最小改 I get home at seven.",
                      "  最小改 ... I get home at seven."), "起点句"),
        ("diff-2 终点句带 `. . .`（带空格）",
         GOOD.replace("  更好版 I'm usually home by seven.",
                      "  更好版 I'm usually home by seven . . ."), "终点句"),
        ("自由产出 [S1] 的 diff-1 起点句带 `…`",
         GOOD.replace("原句   I need a box to put these thing in.",
                      "原句   … a box to put these thing in."), "[S1]"),
        ("自由产出 [S1] 的 diff-2 终点句带 `…`",
         GOOD.replace("        更好版 I need a box for these things.",
                      "        更好版 … a box for these things."), "[S1]"),
    ]
    for name, txt, want in cases:
        st, rc, out = run_deliver(d, txt)
        ck(f"{name} ⇒ ERROR", rc == 1 and "省略号截断" in out and want in out, out[-500:])
        ck(f"{name} ⇒ 文案带文件名 ＋ 行号 ＋ 是哪一段",
           "2026-09-09.md" in out and re.search(r"用省略号截断了 —— \S+ L\d+", out)
           and ("diff-1" in out or "diff-2" in out), out[-500:])

head("【D4b 负】② 三件套块里的 `最小改` / `更好版` 也必须是全文")
with sandbox() as d:
    cases = [
        ("块内 `最小改` 用 … 拼接",
         GOOD.replace("\n最小改 I get home at seven.",
                      "\n最小改 … meeting your deadlines …"), "最小改"),
        ("块内 `更好版` 用 … 拼接",
         GOOD.replace("\n更好版 I'm usually home by seven.",
                      "\n更好版 … releasing a new version …"), "更好版"),
        ("块内 `最小改` 用 `...` 拼接",
         GOOD.replace("\n最小改 I get home at seven.",
                      "\n最小改 ... I get home at seven."), "最小改"),
    ]
    for name, txt, want in cases:
        st, rc, out = run_deliver(d, txt)
        ck(f"{name} ⇒ ERROR", rc == 1 and "省略号截断" in out and want in out, out[-500:])
        ck(f"{name} ⇒ 点名「全文，一句都不省」", "一句都不省" in out, out[-400:])

head("【D4b 负】③ 自由产出 `### ① 最小修改版` / `### ② 更好版` 正文不许省略")
with sandbox() as d:
    st, rc, out = run_deliver(d, GOOD.replace("> I need a box to put these things in.",
                                              "> I need a box … these things in."))
    ck("最小修改版正文带 `…` ⇒ ERROR", rc == 1 and "最小修改版" in out and "省略号" in out,
       out[-500:])
    st, rc, out = run_deliver(d, GOOD.replace("> I need a box for these things.",
                                              "> I need a box ... for these things."))
    ck("更好版正文带 `...` ⇒ ERROR", rc == 1 and "更好版" in out and "省略号" in out, out[-500:])
    st, rc, out = run_deliver(d, GOOD.replace("> I need a box for these things.",
                                              "> 无更好版本"))
    ck("更好版正文逐字写「无更好版本」⇒ 不误伤", rc == 0 and "省略号" not in out, out[-400:])

head("【D4b 正】分界线 2026-09-05 —— 更早的 session 只出存量提示，不计 ERROR")
with sandbox() as d:
    bad = GOOD.replace("  最小改 I stay patient.", "  最小改 I stay patient …") \
              .replace("\n更好版 I'm usually home by seven.",
                       "\n更好版 … releasing a new version …")
    st, rc, out = run_deliver(d, bad, name="2026-09-04.md")
    ck("09-04（＜ 分界线）⇒ ERROR 0", rc == 0 and "ERROR 0" in out, out[-500:])
    ck("但两处都列进「存量提示」", "存量提示" in out and out.count("省略号截断") == 2, out[-600:])
    st, rc, out = run_deliver(d, bad, name="2026-09-05.md")
    ck("09-05（＝ 分界线当天）⇒ 同样的内容变 ERROR", rc == 1 and "不许发" in out, out[-500:])

head("【D5 负】缺【本组新建条目】块")
with sandbox() as d:
    st, rc, out = run_deliver(d, GOOD.replace("### 【本组新建条目】", "### 随便别的标题"))
    ck("⇒ ERROR", rc == 1 and "新建条目" in out, out[-300:])

head("【D6 负】自由产出缺四件套里的任一节")
with sandbox() as d:
    for want in ("① 最小修改版", "② 更好版", "③ 逐句 diff"):
        st, rc, out = run_deliver(d, GOOD.replace(f"### {want}", "### 别的"))
        ck(f"缺 `### {want}` ⇒ ERROR", rc == 1 and want.split()[-1] in out, out[-400:])
    st, rc, out = run_deliver(d, GOOD.replace("[S1] ", "[X1] "))
    ck("逐句 diff 里没有 [S1] 块 ⇒ ERROR", rc == 1 and "[S1]" in out, out[-300:])

head("【D7 负】节标题没带题号")
with sandbox() as d:
    st, rc, out = run_deliver(d, GOOD.replace("（bank:1234 · 自由产出 · cold）", "（自由产出 · cold）"))
    ck("新题标题没 bank:NNN ⇒ ERROR", rc == 1 and "没带题号" in out, out[-300:])
    st, rc, out = run_deliver(d, GOOD.replace("## ② 回看 · bank:875", "## ② 回看 D-1 自由产出"))
    ck("回看标题没题号 ⇒ ERROR", rc == 1 and "回看的是哪一篇" in out, out[-300:])
    st, rc, out = run_deliver(d, GOOD.replace("## ② 回看 · bank:875", "## ② 回看 · 无（D-1 是付息日）"))
    ck("回看写「· 无（理由）」⇒ 放行", rc == 0, out[-300:])

head("【D8 负】围栏没闭合 ⇒ 一律 ERROR（不管日期）")
with sandbox() as d:
    st, rc, out = run_deliver(d, GOOD + "\n```\n没闭合\n", name="2026-08-01.md")
    ck("存量日期也照报 ERROR", rc == 1 and "没闭合" in out, out[-300:])

head("【D9 正】存量口径 —— DELIVER_FROM 之前只提示不报错")
with sandbox() as d:
    broken = GOOD.replace("最小改 I stay patient.", "")
    st, rc, out = run_deliver(d, broken, name="2026-08-01.md")
    ck("存量 session ⇒ ERROR 0", rc == 0, out[-300:])
    ck("但问题以「存量提示」列出来", "存量提示" in out and "最小改" in out, out[-400:])
    st, rc, out = run_deliver(d, broken, name="2026-09-09.md")
    ck("同样的问题在新 session ⇒ ERROR", rc == 1, out[-300:])

head("【D10 正】一整批**合法形状**的整份 session 扫一遍：一份都不许误伤")
# ⚠️ 2026-09-05 改：原来这里扫 `sessions/` 里的**真 session**。那验的不是"闸对不对"，
#   是"今天这一场写完了没有" —— 当天下午 session 才写到复检组的节标题、块还没贴，
#   这一条就红了，而 §0.1.6 会因此把 lab.py 锁死。真 session 的健康度归收尾时
#   `lab.py deliver --session <今天>` 管（＝ test_check K0 对真档案下过的同一条裁决）。
#   ⇒ 改成**自带语料**：合法整份 session 的几种形状各造一份，闸一份都不许误伤；
#     末尾再塞一份人为破坏的当空转自检 —— 语料哪天退化成"随便什么都过"，那一发会红。
RECHECK_SEC = """## ①b 复检组 · 第 1 组（2 题 / 4 条）
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

"""
CORPUS = {
    "整份（复习组＋回看＋新题＋收尾）": ("2026-09-09.md", GOOD),
    "回看写「· 无（理由）」": ("2026-09-09.md",
        GOOD.replace("## ② 回看 · bank:875", "## ② 回看 · 无（D-1 是付息日）")),
    "复习组＋复检组＋回看＋新题": ("2026-09-09.md",
        GOOD.replace("## ② 回看", RECHECK_SEC + "## ② 回看")),
    "只有复检组的一场": ("2026-09-09.md", "# 2026-09-09 · **L1**\n\n" + RECHECK_SEC),
    "只有复习组＋收尾（没有新题）": ("2026-09-09.md",
        GOOD.split("## ② 回看")[0] + "## ④ 收尾核对\n\n（略）\n"),
    "分界线当天（2026-09-05）照样干净": ("2026-09-05.md", GOOD),
    "存量日期（2026-08-01）": ("2026-08-01.md", GOOD),
}
with sandbox(sessions=False) as d:
    fresh(d)
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write("")   # ⛔ 连流水都不借真的
    ck(f"语料覆盖 {len(CORPUS)} 种合法形状（⛔ 语料空了这个 loop 就是空转）",
       len(CORPUS) >= 6, sorted(CORPUS))
    bad = []
    for name, (fn, txt) in CORPUS.items():
        st, rc, out = run(lab.cmd_deliver, Args(session=sess(d, txt, fn)))
        if rc != 0:
            bad.append((name, [l for l in out.split("\n") if l.startswith("ERROR")][:2]))
    ck(f"{len(CORPUS)} 种合法形状全部 ERROR 0（闸⛔不许误伤）", not bad, bad[:2])
    st, rc, out = run_deliver(d, GOOD.replace("最小改 I stay patient.", ""))
    ck("★ 空转自检：同一个 loop 塞一份坏的 ⇒ 抓得到（证明上面那一发不是空过）",
       rc == 1 and "最小改" in out, out[-300:])

head("【L0 正】lookback 认得出题号与已回看")
# ★ 「已回看」要跨两份 session 才验得到：D-1 出了 bank:875，D 那天回看了它。
#   ⛔ 以前这条靠**真 session 里恰好有 bank:875 的自由产出**才绿 —— 真 session 一动就断，
#     这里把 D-1 那一份也自己造出来。
with sandbox(sessions=False) as d:            # ⛔ 不借真 sessions 当背景板（lookback 扫整个目录）
    fresh(d)
    PREV = (GOOD.replace("# 2026-09-09", "# 2026-09-08")
                .replace("## ② 回看 · bank:875", "## ② 回看 · 无（D-1 是付息日）")
                .replace("bank:1234", "bank:875"))
    sess(d, PREV, "2026-09-08.md")
    sess(d, GOOD)
    ck("夹具自检：D-1 那份确实出了 bank:875 的自由产出",
       "（bank:875 · 自由产出" in PREV and "bank:1234" not in PREV)
    st, rc, out = run(lab.cmd_lookback, Args(date="2026-09-10"))
    ck("退出码 0", (st, rc) == ("OK", 0))
    ck("bank:1234 被列为自由产出", "bank:1234" in out, out[-600:])
    ck("bank:875 因 09-09 回看过而标已回看",
       re.search(r"bank:875.*已回看", out) is not None, out[-900:])
    ck("回看目标 ＝ 最近一篇没回看过的", "bank:1234" in out.split("② 本次回看目标")[1], out[-400:])

head("【L1 负】标题没题号 ⇒ 明说追不了，⛔ 不猜")
with sandbox(sessions=False) as d:            # 同上：真 session 里要是也有 bank:1234，这条会假红
    fresh(d)
    sess(d, GOOD.replace("（bank:1234 · 自由产出 · cold）", "（自由产出 · cold）"))
    st, rc, out = run(lab.cmd_lookback, Args(date="2026-09-10"))
    ck("列为「标题没带题号 ⇒ 追不了」", "追不了" in out, out[-600:])
    ck("⛔ 没有凭空猜一个题号出来",
       "bank:1234" not in out.split("① 全部自由产出")[1].split("② 本次")[0])

head("【L2 正】没有未回看的 ⇒ 明确说跳过")
with sandbox(sessions=False) as d:
    fresh(d)
    sess(d, "# 2026-09-09\n\n## ② 回看 · 无（D-1 是付息日）\n")
    st, rc, out = run(lab.cmd_lookback, Args(date="2026-09-10"))
    ck("说「无自由产出可回看」", "无自由产出可回看" in out, out[-300:])

head("【L3 正】lookback 只读 —— 不写任何文件")
with sandbox() as d:
    before = {f: read(d, f) for f in ("problems.md", "graduated.md", "drawn.log")
              if os.path.exists(os.path.join(d, f))}
    run(lab.cmd_lookback, Args(date="2026-09-10"))
    ck("档案与流水一个字节都没动",
       all(read(d, f) == v for f, v in before.items()))

sys.exit(report("lab.py deliver / lookback 正/负向测试"))
