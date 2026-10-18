#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py attempts（全部旧答）与重答节旧答对比闸、⛔ 不出新题闸（§4④ §7④ §9.1⑧）的正向／负向测试。
⛔ 全部用自造的 session 与旧档案，不借真 sessions 当背景板（attempts 扫整个目录）。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, read, lab


def free(date, day, title, said, better):
    """一份带一篇自由产出的 session。said ＝ 她的原话（可多行），better ＝ 更好版。"""
    return f"""# {date} · **{day}**（周期 12）

## {title}

### 题目原文
```
[P3] question_bank.md:700 · test
Do you like rivers?
```

### 她的原话
```
{said}
```

### 五层诊断（§7，每层都过）
```
层1 本层无对象
```

### ① 最小修改版
```
{said}
```

### ② 更好版
```
{better}
```

### ③ 逐句 diff

```
[S1] {said.splitlines()[0]}
diff-1  原句 → 最小改
  无 diff（＝上一版）
diff-2  最小改 → 更好版
  无 diff（＝上一版）
```

## ④ 收尾核对

（略）
"""


def put(d, name, text):
    sd = os.path.join(d, "sessions")
    os.makedirs(sd, exist_ok=True)
    open(os.path.join(sd, name), "w", encoding="utf-8").write(text)
    open(os.path.join(d, "drawn.log"), "w", encoding="utf-8").write("")
    return os.path.join(sd, name)


def world(d):
    """bank:700 答过两次：09-20 新题 · 10-01 重答；bank:701 只在 09-21 答过一次；
    10-20 那篇 bank:700 在「今天」之后，⛔ 不该算旧答。"""
    put(d, "2026-09-20.md", free("2026-09-20", "L1", "③ 新题 · 第 1 道（bank:700 · P3 · cold）",
                                 "Rivers is nice.\nI walk there on weekend.",
                                 "Rivers are lovely. I go walking there on weekends."))
    put(d, "2026-09-21.md", free("2026-09-21", "L2", "③ 新题 · 第 1 道（bank:701 · P3 · cold）",
                                 "Lakes is calm.", "Lakes are really calm."))
    put(d, "2026-10-01.md", free("2026-10-01", "R", "d 段 重答 · bank:700（P3 · cold）",
                                 "Rivers are relaxing for me.", "Rivers really help me unwind."))
    put(d, "2026-10-20.md", free("2026-10-20", "L1", "③ 重答 · bank:700（P3 · cold）",
                                 "FUTURE ANSWER should not show.", "x"))


def attempts(ids, today="2026-10-14"):
    st, rc, out = run(lab.cmd_attempts, Args(ids=ids, date=today))
    return rc, out


def redo_session(compare, date="2026-10-14", pid="bank:700", day="L1", extra_sec=""):
    """今天的重答节：四件套齐 ＋ 可选的 `### ④ 与旧答对比` 正文。"""
    cmp_ = f"\n### ④ 与旧答对比\n\n{compare}\n" if compare is not None else ""
    return f"""# {date} · **{day}**（周期 12）
{extra_sec}
## ③ 重答 · {pid}（P3 · cold）

### 题目原文
```
Do you like rivers?
```

### 她的原话
```
I really like rivers.
```

### ① 最小修改版
```
I really like rivers.
```

### ② 更好版
```
I really love rivers.
```

### ③ 逐句 diff

```
[S1] I really like rivers.
diff-1  原句 → 最小改
  无 diff（＝上一版）
diff-2  最小改 → 更好版
  最小改 I really like rivers.
  更好版 I really love rivers.
  · like → love   ⚠️ 测试
```
{cmp_}
### 【本篇新建条目】

```
无
```

## ④ 收尾核对

（略）
"""


VERDICT = "```\n进步   · 主谓一致对了\n退步   无\n没变   · 还是没举例\n总评   本次更好\n```"


def errs(d, text, name="2026-10-14.md", key="旧答"):
    p = put(d, name, text)
    st, rc, out = run(lab.cmd_deliver, Args(session=p))
    return [l for l in out.split("\n") if l.startswith("ERROR") and key in l], out


head("【A0 正】attempts 打出 lab 里全部旧答（日期升序）：原话 ＋ 当时的更好版 ＋ 逐句 diff 逐字 ＋ 出处；⛔ 今天及以后的不算")
with sandbox(sessions=False) as d:
    world(d)
    rc, out = attempts(["bank:700"])
    ck("退出码 0", rc == 0, out[-300:])
    order = re.findall(r"^旧答 (\d+) · (\S+)", out, re.M)
    ck("两次旧答，按日期：09-20 → 10-01", order == [("1", "2026-09-20"), ("2", "2026-10-01")], order)
    ck("报了次数", "lab 里的旧答 2 次" in out, out[:300])
    for l in ("Rivers is nice.", "I walk there on weekend.", "Rivers are relaxing for me."):
        ck(f"原话逐字：{l}", l in out.split("\n"), out[:600])
    ck("当时的更好版也打了（两次都有）", "Rivers really help me unwind." in out
       and "Rivers are lovely. I go walking there on weekends." in out, out[:900])
    for n in ("1", "2"):
        ck(f"旧答 {n} 的更好版／逐句 diff 各有小标题", f"（旧答 {n} · 当时的② 更好版）" in out
           and f"（旧答 {n} · 当时的③ 逐句 diff）" in out, out[:900])
    ck("逐句 diff 逐字打出（旧答 1 的 [S1]）", "[S1] Rivers is nice." in out.split("\n"), out[:900])
    ck("逐句 diff 逐字打出（旧答 2 的 [S1]）", "[S1] Rivers are relaxing for me." in out.split("\n"), out[:900])
    ck("每次旧答内部顺序：原话 → 更好版 → 逐句 diff",
       out.index("I walk there on weekend.") < out.index("（旧答 1 · 当时的② 更好版）")
       < out.index("[S1] Rivers is nice.") < out.index("旧答 2 · "), out[:900])
    ck("⛔ 输出里没有 ``` 行（整段要贴进 ④ 的同一个围栏）",
       not any(l.startswith("```") for l in out.split("\n")), out[:900])
    ck("注明原篇出处", "2026-09-20.md:L" in out and "2026-10-01.md:L" in out)
    ck("⛔ 今天之后那篇不算旧答", "FUTURE ANSWER" not in out)
    ck("⛔ 别的题（bank:701）不混进来", "Lakes is calm." not in out)
    ck("⛔ 没有 lab 外首答提示（这题不是旧 R 题）", "★ 首答" not in out)

head("【A1 正】--date 卡在两次旧答之间 ⇒ 只打更早的那一次")
with sandbox(sessions=False) as d:
    world(d)
    rc, out = attempts(["bank:700"], today="2026-10-01")
    ck("只有 1 次（10-01 当天的不算）", "lab 里的旧答 1 次" in out and "Rivers are relaxing" not in out, out[:400])

head("【A2 正】旧 R 号 ＝ 它的 bank:NNN：首答在 lab 之前 ⇒ 打出首答日 ＋ 旧档案里提到这道题的行")
with sandbox(sessions=False) as d:
    world(d)
    # R20 ＝ bank:364（LEGACY_REDO，首答 2026-08-11）
    put(d, "2026-09-30.md", free("2026-09-30", "R", "d 段 重答 · bank:364（R20 · P3 · cold）",
                                 "Special food is for ritual.", "It's mostly about the ritual."))
    cdir = os.path.join(d, "coach", "sessions")
    os.makedirs(cdir, exist_ok=True)
    open(os.path.join(d, "coach", "fluency_lab.md"), "w", encoding="utf-8").write(
        "# 旧档案\n### 新题 · `Why are there special foods?`（question_bank.md:364）\n"
        "- **她的原话（逐字）**：`Because of culture.`\n其它行 question_bank.md:3640 不该命中\n")
    open(os.path.join(cdir, "2026-08-11.md"), "w", encoding="utf-8").write(
        "# 08-11\n题：question_bank.md：364\n")
    rc, out = attempts(["R20"])
    ck("R20 与 bank:364 认成同一道题（lab 旧答 1 次）", "lab 里的旧答 1 次" in out, out[:400])
    ck("打出首答在 lab 之前的提示", "★ 首答 2026-08-11（R20）在 lab/sessions 之前" in out, out[:600])
    ck("旧档案命中 fluency_lab.md 那一行", re.search(r"coach/fluency_lab\.md:L2 ", out), out)
    ck("旧档案命中 coach/sessions（全角冒号也认）", re.search(r"coach/sessions/2026-08-11\.md:L2 ", out), out)
    ck("⛔ question_bank.md:3640 不算 364", "3640" not in out, out)

head("【A3 正】lab 里一次旧答都没有、也不是旧 R 题 ⇒ 明说，⛔ 不瞎编")
with sandbox(sessions=False) as d:
    world(d)
    rc, out = attempts(["bank:999"])
    ck("提示 lab 里一次旧答都没有", "lab 里一次旧答都没有" in out, out)
    ck("旧档案不存在 ⇒ 说没有提到的行", "旧档案里没有提到这道题的行" in out, out)

head("【A4 正】attempts 只读 —— 不写任何文件")
with sandbox(sessions=False) as d:
    world(d)
    sd = os.path.join(d, "sessions")
    before = {f: read(d, os.path.join("sessions", f)) for f in os.listdir(sd)}
    attempts(["bank:700", "bank:701"])
    ck("session 一个字节都没动", all(read(d, os.path.join("sessions", f)) == v for f, v in before.items()))
    ck("没多出文件", sorted(os.listdir(sd)) == sorted(before))

head("【G0 正】④ 原样贴了 attempts 的输出 ＋ 四栏 ⇒ 旧答对比闸 ERROR 0")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = attempts(["bank:700"])
    e, out = errs(d, redo_session("```\n" + body + "\n```\n\n" + VERDICT))
    ck("没有任何「旧答」ERROR", not e, e[:3])

head("【G1 负】重答节没有 `### ④ 与旧答对比` ⇒ ERROR")
with sandbox(sessions=False) as d:
    world(d)
    e, out = errs(d, redo_session(None))
    ck("报缺 ④", any("缺 `### ④ 与旧答对比`" in x for x in e), e or out[-600:])

head("【G2 负】旧答 1 少一行原话 ⇒ ERROR 点名旧答 1 与日期")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = attempts(["bank:700"])
    cut = body.replace("I walk there on weekend.\n", "")
    e, out = errs(d, redo_session("```\n" + cut + "\n```\n\n" + VERDICT))
    ck("点名旧答 1（09-20）少了 1／2 行", any("旧答 1（2026-09-20" in x and "1／2" in x for x in e), e)
    ck("⛔ 旧答 2 没被冤枉", not any("旧答 2" in x for x in e), e)

head("【G3 负】只贴了最近一次、省掉更早那次 ⇒ ERROR 点名旧答 1")
with sandbox(sessions=False) as d:
    world(d)
    only_last = "旧答 2 · 2026-10-01\nRivers are relaxing for me."
    e, out = errs(d, redo_session("```\n" + only_last + "\n```\n\n" + VERDICT))
    ck("点名旧答 1", any("旧答 1（2026-09-20" in x for x in e), e)

head("【G4 负】四栏少了「退步」⇒ ERROR；改写成「退步 无」就过")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = attempts(["bank:700"])
    no_back = VERDICT.replace("退步   无\n", "")
    e, out = errs(d, redo_session("```\n" + body + "\n```\n\n" + no_back))
    ck("点名缺「退步」", any("缺「退步」" in x for x in e), e)
    e2, out2 = errs(d, redo_session("```\n" + body + "\n```\n\n" + VERDICT))
    ck("写了「退步 无」⇒ 不报", not e2, e2)

head("【G5 正】分界线之前（10-13）的重答节 ⛔ 不查旧答对比")
with sandbox(sessions=False) as d:
    world(d)
    e, out = errs(d, redo_session(None, date="2026-10-13"), name="2026-10-13.md")
    ck("10-13 没有 ④ 也不报", not e, e)

head("【G6 负】分界线起学习日出现【新题】节 ⇒ ERROR；分界线之前照旧允许")
with sandbox(sessions=False) as d:
    world(d)
    newsec = "## ③ 新题 · 第 1 道（bank:702 · P3 · cold）\n\n（略）\n"
    rc, body = attempts(["bank:700"])
    e, out = errs(d, redo_session("```\n" + body + "\n```\n\n" + VERDICT, extra_sec=newsec), key="不出新题")
    ck("10-14 L1 有新题节 ⇒ 报 §4④ 不出新题", len(e) == 1, e or out[-500:])
    e2, out2 = errs(d, free("2026-10-13", "L1", "③ 新题 · 第 1 道（bank:702 · P3 · cold）", "A.", "B."),
                    name="2026-10-13.md", key="不出新题")
    ck("10-13 有新题节 ⇒ 不报", not e2, e2)

head("【G7 负】付息日有新题 ⇒ 只报付息日那一条，⛔ 不重复报两条")
with sandbox(sessions=False) as d:
    world(d)
    newsec = "## ③ 新题 · 第 1 道（bank:702 · P3 · cold）\n\n（略）\n"
    rc, body = attempts(["bank:700"])
    p = put(d, "2026-10-14.md", redo_session("```\n" + body + "\n```\n\n" + VERDICT, day="R",
                                             extra_sec=newsec).replace("## ③ 重答", "## d 段 重答"))
    st, rc2, out = run(lab.cmd_deliver, Args(session=p))
    hits = [l for l in out.split("\n") if l.startswith("ERROR") and "新题" in l]
    ck("恰好 1 条（付息日口径）", len(hits) == 1 and "付息日" in hits[0], hits)

head("【G8 负／正】lab 里没有旧答：④ 一行「旧答」都没写 ⇒ ERROR；写明「旧答 · 首答原话未存」⇒ 过")
with sandbox(sessions=False) as d:
    world(d)
    e, out = errs(d, redo_session("```\n（这里什么都没写）\n```\n\n" + VERDICT, pid="bank:999"))
    ck("没摆任何旧答 ⇒ 报", any("没摆任何旧答" in x for x in e), e or out[-500:])
    e2, out2 = errs(d, redo_session("```\n旧答 · 首答原话未存\n```\n\n" + VERDICT, pid="bank:999"))
    ck("写明未存 ⇒ 不报", not e2, e2)

head("【G9 正】多写不管：旁注、自己加的对照行照样允许")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = attempts(["bank:700"])
    e, out = errs(d, redo_session("```\n" + body + "\n★ 旁注：两次都没举例\n```\n\n" + VERDICT))
    ck("没有任何「旧答」ERROR", not e, e[:3])

head("【G10 正】重答节的 ④ ⛔ 不渗进四件套：之后回看这篇时 lookback --print 不打对比内容")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = attempts(["bank:700"])
    put(d, "2026-10-14.md", redo_session("```\n" + body + "\n```\n\n" + VERDICT))
    st, rc2, out = run(lab.cmd_lookback, Args(print_ids=["bank:700"], date="2026-10-15"))
    ck("打的是 10-14 那篇", "2026-10-14.md:L" in out, out[:300])
    ck("⛔ 旧答原话不在四件套里", "Rivers is nice." not in out, out)
    ck("⛔ 四栏不在四件套里", "主谓一致对了" not in out, out)
    ck("本篇原话照打", "I really like rivers." in out, out)

head("【G11 正】attempts 认 10-14 当天写好的重答为下一次的旧答（同一道题第三次作答）")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = attempts(["bank:700"])
    put(d, "2026-10-14.md", redo_session("```\n" + body + "\n```\n\n" + VERDICT))
    rc, out = attempts(["bank:700"], today="2026-10-15")
    order = re.findall(r"^旧答 (\d+) · (\S+)", out, re.M)
    ck("三次：09-20 → 10-01 → 10-14", [x[1] for x in order] == ["2026-09-20", "2026-10-01", "2026-10-14"], order)
    ck("⛔ 10-14 那篇的 ④ 里贴的旧原话不被当成第三次的原话",
       out.split("\n旧答 3 · ")[1].count("Rivers is nice.") == 0, out)

head("【A5 正】原篇没写「③ 逐句 diff」节 ⇒ attempts 明说没有，⛔ 不补编")
with sandbox(sessions=False) as d:
    world(d)
    nodiff = free("2026-09-22", "L3", "③ 新题 · 第 1 道（bank:703 · P3 · cold）", "Seas is big.", "Seas are vast.")
    nodiff = nodiff[:nodiff.index("### ③ 逐句 diff")] + "## ④ 收尾核对\n"
    put(d, "2026-09-22.md", nodiff)
    rc, out = attempts(["bank:703"])
    ck("更好版照打", "Seas are vast." in out, out)
    ck("明说原篇没有逐句 diff", "原篇没有「③ 逐句 diff」这一节" in out, out)

head("【H0 正】10-17 起的重答节：④ 原样贴 attempts（原话 ＋ 更好版 ＋ 逐句 diff）⇒ ERROR 0")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = attempts(["bank:700"], today="2026-10-17")
    e, out = errs(d, redo_session("```\n" + body + "\n```\n\n" + VERDICT, date="2026-10-17"),
                  name="2026-10-17.md")
    ck("没有任何「旧答」ERROR", not e, e[:3])

head("【H1 负】10-17 起：旧答 1 的更好版没贴 ⇒ ERROR 点名旧答 1 当时的② 更好版")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = attempts(["bank:700"], today="2026-10-17")
    cut = body.replace("Rivers are lovely. I go walking there on weekends.\n", "")
    e, out = errs(d, redo_session("```\n" + cut + "\n```\n\n" + VERDICT, date="2026-10-17"),
                  name="2026-10-17.md")
    ck("点名旧答 1（09-20）当时的② 更好版少了 1／1 行",
       any("旧答 1（2026-09-20" in x and "② 更好版" in x and "1／1" in x for x in e), e)
    ck("⛔ 旧答 2 没被冤枉", not any("旧答 2" in x for x in e), e)

head("【H2 负】10-17 起：旧答 2 的逐句 diff 没贴（只贴了原话 ＋ 更好版）⇒ ERROR 点名旧答 2 当时的③ 逐句 diff")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = attempts(["bank:700"], today="2026-10-17")
    cut = body.replace("[S1] Rivers are relaxing for me.\n", "")
    e, out = errs(d, redo_session("```\n" + cut + "\n```\n\n" + VERDICT, date="2026-10-17"),
                  name="2026-10-17.md")
    ck("点名旧答 2（10-01）当时的③ 逐句 diff", any("旧答 2（2026-10-01" in x and "③ 逐句 diff" in x for x in e), e)
    ck("⛔ 旧答 1 没被冤枉", not any("旧答 1" in x for x in e), e)

head("【H3 正】分界线之前（10-14）的重答节：只贴原话、没贴更好版／diff ⇒ ⛔ 不按新口径查")
with sandbox(sessions=False) as d:
    world(d)
    only_raw = ("旧答 1 · 2026-09-20\nRivers is nice.\nI walk there on weekend.\n"
                "旧答 2 · 2026-10-01\nRivers are relaxing for me.")
    e, out = errs(d, redo_session("```\n" + only_raw + "\n```\n\n" + VERDICT))
    ck("10-14 只有原话也不报", not e, e)
with sandbox(sessions=False) as d:
    world(d)
    e2, out2 = errs(d, redo_session("```\n" + only_raw + "\n```\n\n" + VERDICT, date="2026-10-17"),
                    name="2026-10-17.md")
    ck("同样内容放到 10-17 ⇒ 报（更好版、逐句 diff 两次旧答各一条）",
       len([x for x in e2 if "当时的" in x]) == 4, e2)

head("【H4 正】原篇本来就没写逐句 diff ⇒ 10-17 起也只查原篇有的（⛔ 不冤枉）")
with sandbox(sessions=False) as d:
    world(d)
    nodiff = free("2026-09-22", "L3", "③ 新题 · 第 1 道（bank:703 · P3 · cold）", "Seas is big.", "Seas are vast.")
    nodiff = nodiff[:nodiff.index("### ③ 逐句 diff")] + "## ④ 收尾核对\n"
    put(d, "2026-09-22.md", nodiff)
    rc, body = attempts(["bank:703"], today="2026-10-17")
    e, out = errs(d, redo_session("```\n" + body + "\n```\n\n" + VERDICT, date="2026-10-17", pid="bank:703"),
                  name="2026-10-17.md")
    ck("没有任何「旧答」ERROR", not e, e[:3])

sys.exit(report("lab.py attempts／旧答对比闸 正/负向测试"))
