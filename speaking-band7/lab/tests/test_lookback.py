#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py lookback --print／--cycle 与回看节四件套逐字闸（§4② §5⓪ §9.1⑦）的正向／负向测试。
⛔ 全部用自造的 session，不借真 sessions 当背景板（lookback 扫整个目录）。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, read, lab


def free(date, day, pid_title, s1, better, extra_head=""):
    """一份带一篇自由产出的 session。s1 ＝ 她的原话（一句），better ＝ 更好版。"""
    fixed = s1.replace(" is ", " are ")
    return f"""# {date} · **{day}**（周期 9）
{extra_head}
## {pid_title}

### 题目原文
```
[P3] question_bank.md:900 · test
Do you like parks?
```
★ 开场 pick_question.py 抽定（这行是注释，不属于四件套）

### 她的原话（逐字）
```
{s1}
```

### 五层诊断（§7，每层都过）
```
层1 语法搭配 真错 1 处：is → are（诊断不属于四件套）
```

### ① 最小修改版
```
{fixed}
```

### ② 更好版
```
{better}
```

### ③ 逐句 diff

```
[S1] {s1}
diff-1  原句 → 最小改
  原句   {s1}
  最小改 {fixed}
  · is → are   ⚪ 形态类
diff-2  最小改 → 更好版
  最小改 {fixed}
  更好版 {better}
  · 更口语   ⚠️ 理由行也要逐字
```

### 【本篇新建条目】

无

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
    """周期边界：09-19 R ｜ 09-20 L1 bank:900 ｜ 09-21 L2 bank:901 ｜ 09-22 L3 重答 R7 ｜ 今天 09-23。
    09-18 那篇 bank:800 在上一个周期里，⛔ 不该进 --cycle。"""
    sd = os.path.join(d, "sessions")
    os.makedirs(sd, exist_ok=True)
    for f in os.listdir(sd):
        os.remove(os.path.join(sd, f))
    put(d, "2026-09-18.md", free("2026-09-18", "L3", "③ 新题 · 第 1 道（bank:800 · P3 · cold）",
                                 "Old parks is nice.", "Old parks are lovely."))
    put(d, "2026-09-19.md", "# 2026-09-19 · **R**（付息日 · 周期 8 收尾）\n\n## ② 回看 · 无（测试）\n")
    put(d, "2026-09-20.md", free("2026-09-20", "L1", "③ 新题 · 第 1 道（bank:900 · P3 · cold）",
                                 "I like parks because they is quiet.",
                                 "I love parks because they're so quiet."))
    put(d, "2026-09-21.md", free("2026-09-21", "L2", "③ 新题 · 第 1 道（bank:901 · P3 · cold）",
                                 "Lakes is calm in the morning.",
                                 "Lakes are really calm first thing in the morning."))
    put(d, "2026-09-22.md", free("2026-09-22", "L3", "d 段 重答 · R7（P3 · cold）",
                                 "Rivers is loud.", "Rivers can get pretty loud."))


def printed(ids, today="2026-09-23"):
    st, rc, out = run(lab.cmd_lookback, Args(print_ids=ids, date=today))
    return rc, out


def look_session(body, title="⓪ 回看 · 本周期（bank:900 · bank:901）", date="2026-09-23"):
    return f"# {date} · **R**（付息日）\n\n## {title}\n\n{body}\n\n## ④ 收尾核对\n\n（略）\n"


def look_errs(d, text, name="2026-09-23.md"):
    p = put(d, name, text)
    st, rc, out = run(lab.cmd_deliver, Args(session=p))
    return [l for l in out.split("\n") if l.startswith("ERROR") and "回看 " in l], out


head("【P0 正】--print 打出四件套原文：题目／原话／最小改／更好版／逐句 diff，诊断与 ★ 注释不打")
with sandbox(sessions=False) as d:
    world(d)
    rc, out = printed(["bank:900"])
    ck("退出码 0", rc == 0, out[-300:])
    for k in ("题目原文", "她的原话", "① 最小修改版", "② 更好版", "③ 逐句 diff"):
        ck(f"打出了「{k}」", f"**{k}**" in out, out[:600])
    ck("原话逐字", "I like parks because they is quiet." in out)
    ck("更好版逐字", "I love parks because they're so quiet." in out)
    ck("diff 的理由行也打了", "· 更口语   ⚠️ 理由行也要逐字" in out)
    ck("⛔ 五层诊断不在四件套里", "诊断不属于四件套" not in out)
    ck("⛔ 围栏外的 ★ 注释不打", "这行是注释" not in out)
    ck("围栏成对（贴回去不吞节）", out.count("```") % 2 == 0)
    ck("注明原篇出处", "2026-09-20.md:L" in out)

head("【P1 正】--cycle ＝ 最后一个付息日之后、今天之前的全部自由产出（含重答），按日期顺序")
with sandbox(sessions=False) as d:
    world(d)
    st, rc, out = run(lab.cmd_lookback, Args(cycle=True, date="2026-09-23"))
    order = re.findall(r"### 回看 · (\S+)（", out)
    ck("三篇：bank:900 → bank:901 → R7", order == ["bank:900", "bank:901", "R7"], order)
    ck("⛔ 上一周期的 bank:800 不进来", "bank:800" not in out)
    ck("首行提示回看节标题怎么写", "回看 · bank:900 · bank:901 · R7" in out, out[:200])

head("【P2 正】--cycle 本周期没有自由产出 ⇒ 明说写「无」")
with sandbox(sessions=False) as d:
    world(d)
    st, rc, out = run(lab.cmd_lookback, Args(cycle=True, date="2026-09-20"))
    ck("09-19 R 当天之后、09-20 之前没有产出 ⇒ 提示写 无", "无（理由）" in out, out[:300])

head("【P3 负】--print 题号不存在 ⇒ 退出码 1，⛔ 不瞎打")
with sandbox(sessions=False) as d:
    world(d)
    rc, out = printed(["bank:999"])
    ck("退出码 1 ＋ 找不到", rc == 1 and "找不到" in out, out[-300:])

head("【P4 正】--print 只读 —— 不写任何文件")
with sandbox(sessions=False) as d:
    world(d)
    before = {f: read(d, os.path.join("sessions", f)) for f in os.listdir(os.path.join(d, "sessions"))}
    printed(["bank:900", "bank:901"])
    ck("session 一个字节都没动",
       all(read(d, os.path.join("sessions", f)) == v for f, v in before.items()))

head("【G0 正】回看节原样贴了 --print 的输出 ⇒ 回看闸 ERROR 0")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = printed(["bank:900", "bank:901"])
    errs, out = look_errs(d, look_session(body))
    ck("没有任何「回看 …」ERROR", not errs, errs[:3])

head("【G1 负】少一行更好版 ⇒ 点名「② 更好版」")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = printed(["bank:900", "bank:901"])
    bad = body.replace("I love parks because they're so quiet.\n```", "（更好版略）\n```", 1)
    ck("夹具自检：真的删掉了更好版正文那一行", bad != body)
    errs, out = look_errs(d, look_session(bad))
    ck("报 bank:900 的「② 更好版」", any("bank:900" in e and "② 更好版" in e for e in errs), errs[:3])

head("【G2 负】diff 被压成一行箭头（整段只剩理由）⇒ 报「③ 逐句 diff」")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = printed(["bank:900", "bank:901"])
    bad = body.replace("  原句   Lakes is calm in the morning.\n", "", 1)
    ck("夹具自检：删掉了 diff-1 的起点句", bad != body)
    errs, out = look_errs(d, look_session(bad))
    ck("报 bank:901 的「③ 逐句 diff」少 1 行",
       any("bank:901" in e and "③ 逐句 diff" in e and "少了 1／" in e for e in errs), errs[:3])

head("【G3 负】标题列了两篇、正文只贴一篇（＝ 以「昨天发过」为由省篇）⇒ 报漏的那篇")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = printed(["bank:900"])
    errs, out = look_errs(d, look_session(body))
    ck("报 bank:901", any("bank:901" in e for e in errs), errs[:3])
    ck("⛔ 不冤枉贴全了的 bank:900", not any("bank:900" in e for e in errs), errs[:3])

head("【G4 正】多写的旁注／更正行不管（只查少，不查多）")
with sandbox(sessions=False) as d:
    world(d)
    rc, body = printed(["bank:900", "bank:901"])
    extra = body.replace("  · is → are   ⚪ 形态类", "  · is → are   ⚪ 形态类\n    ★ 今天更正：这是旁注", 1)
    errs, out = look_errs(d, look_session(extra))
    ck("加旁注不报错", not errs, errs[:3])

head("【G5 正】`回看 · 无（理由）` ⇒ 不查四件套")
with sandbox(sessions=False) as d:
    world(d)
    errs, out = look_errs(d, look_session("本周期没有自由产出。", title="⓪ 回看 · 无（本周期没练新题）"))
    ck("无回看 ⇒ 回看闸不报", not errs, errs[:3])

head("【G6 正】LOOK_FROM 之前的 session ⇒ 存量，不查四件套")
with sandbox(sessions=False) as d:
    world(d)
    old = look_session("四件套见原篇。", title="② 回看 · bank:800", date="2026-09-18")
    errs, out = look_errs(d, old, name="2026-09-18b.md")
    ck("夹具自检：日期早于 LOOK_FROM", "2026-09-18" < lab.LOOK_FROM)
    # 文件名不合 YYYY-MM-DD.md ⇒ date 读成 "?"；改用正名单独目录验
    sd = os.path.join(d, "sessions")
    os.remove(os.path.join(sd, "2026-09-18b.md"))
    os.rename(os.path.join(sd, "2026-09-18.md"), os.path.join(sd, "keep.txt"))
    put(d, "2026-09-17.md", free("2026-09-17", "L2", "③ 新题 · 第 1 道（bank:800 · P3 · cold）",
                                 "Old parks is nice.", "Old parks are lovely."))
    errs, out = look_errs(d, old, name="2026-09-18.md")
    ck("09-18 的回看节只有一句指针 ⇒ 不报", not errs, errs[:3])

head("【G7 负】标题的题号在更早的 session 里找不到 ⇒ 报找不到原篇")
with sandbox(sessions=False) as d:
    world(d)
    errs, out = look_errs(d, look_session("（空）", title="⓪ 回看 · bank:999"))
    ck("报找不到原篇", any("bank:999" in e and "找不到" in e for e in errs), errs[:3])

head("【G8 负】原篇缺更好版节 ⇒ 报原篇写歪，⛔ 不当成回看节合格")
with sandbox(sessions=False) as d:
    world(d)
    p = os.path.join(d, "sessions", "2026-09-20.md")
    t = read(d, os.path.join("sessions", "2026-09-20.md")).replace("### ② 更好版", "### ② 另一种说法")
    open(p, "w", encoding="utf-8").write(t)
    rc, body = printed(["bank:900"])
    ck("--print 同样报缺节、退出码 1", rc == 1 and "缺「② 更好版」" in body, body[-300:])
    errs, out = look_errs(d, look_session(body, title="⓪ 回看 · bank:900"))
    ck("deliver 报原篇解析不出", any("bank:900" in e and "解析不出" in e for e in errs), errs[:3])

head("【G9 正】原篇同一题号拆成两个节（抽题记录＋逐题记录）⇒ 合并取四件套")
with sandbox(sessions=False) as d:
    world(d)
    t = read(d, os.path.join("sessions", "2026-09-21.md")).replace(
        "### ① 最小修改版", "## ③ 新题 · 逐题记录（bank:901）\n\n### ① 最小修改版", 1)
    open(os.path.join(d, "sessions", "2026-09-21.md"), "w", encoding="utf-8").write(t)
    rc, body = printed(["bank:901"])
    ck("拆开的两节合起来五节齐", rc == 0 and all(f"**{k}**" in body for k in
       ("题目原文", "她的原话", "① 最小修改版", "② 更好版", "③ 逐句 diff")), body[-400:])

head("【G10 正】取原篇只看今天之前 —— 同一个题号重答过两次，取最近那次")
with sandbox(sessions=False) as d:
    world(d)
    put(d, "2026-09-10.md", free("2026-09-10", "L1", "d 段 重答 · R7（P3 · cold）",
                                 "Rivers is very loud long ago.", "Rivers were really loud back then."))
    rc, body = printed(["R7"])
    ck("取的是 09-22 那次", "Rivers can get pretty loud." in body and "long ago" not in body, body[:500])

sys.exit(report("lab.py lookback --print／回看四件套闸 正/负向测试"))
