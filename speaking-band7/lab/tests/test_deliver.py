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
    return p


def run_deliver(d, text, name="2026-09-09.md", **kw):
    return run(lab.cmd_deliver, Args(session=sess(d, text, name), **kw))


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

head("【D10 正】全档真实 session 扫一遍：只许 ERROR 0")
with sandbox() as d:
    bad = []
    for f in sorted(os.listdir(os.path.join(d, "sessions"))):
        if not re.match(r"^20\d\d-\d\d-\d\d\.md$", f):
            continue
        st, rc, out = run(lab.cmd_deliver, Args(session=os.path.join(d, "sessions", f)))
        if rc != 0:
            bad.append((f, out[-200:]))
    ck("18 份历史 session 全部 ERROR 0", not bad, bad[:2])

head("【L0 正】lookback 认得出题号与已回看")
with sandbox() as d:
    sess(d, GOOD)
    st, rc, out = run(lab.cmd_lookback, Args(date="2026-09-10"))
    ck("退出码 0", (st, rc) == ("OK", 0))
    ck("bank:1234 被列为自由产出", "bank:1234" in out, out[-600:])
    ck("bank:875 因 09-09 回看过而标已回看",
       re.search(r"bank:875.*已回看", out) is not None, out[-900:])
    ck("回看目标 ＝ 最近一篇没回看过的", "bank:1234" in out.split("② 本次回看目标")[1], out[-400:])

head("【L1 负】标题没题号 ⇒ 明说追不了，⛔ 不猜")
with sandbox() as d:
    sess(d, GOOD.replace("（bank:1234 · 自由产出 · cold）", "（自由产出 · cold）"))
    st, rc, out = run(lab.cmd_lookback, Args(date="2026-09-10"))
    ck("列为「标题没带题号 ⇒ 追不了」", "追不了" in out, out[-600:])
    ck("⛔ 没有凭空猜一个题号出来",
       "bank:1234" not in out.split("① 全部自由产出")[1].split("② 本次")[0])

head("【L2 正】没有未回看的 ⇒ 明确说跳过")
with sandbox() as d:
    for f in os.listdir(os.path.join(d, "sessions")):
        os.remove(os.path.join(d, "sessions", f))
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
