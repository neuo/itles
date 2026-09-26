#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py redo —— 重答队列实时算（§5d）的正向／负向测试。
⛔ 全部用自造的 session ／ asked.log ／ question_bank.md ／ LEGACY_REDO，不借真档案。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, lab

# 自造的冻结历史：R1 有 bank 行号 ＋ session 外重答日；R2 有 bank 行号；R3 没有 bank 行号
FAKE_LEGACY = (
    ("R1", 100, "P3", "2026-08-01", "08-01 前", ("2026-08-05",), "Legacy one?"),
    ("R2", 200, "P3", "2026-08-02", "", (), "Legacy two?"),
    ("R3", None, "P2", "2026-08-03", "", (), "Describe legacy three"),
)
REAL_LEGACY = lab.LEGACY_REDO


def free(date, title, s1="Parks is nice.", better="Parks are lovely."):
    fixed = s1.replace(" is ", " are ")
    return f"""# {date} · **L1**（周期 9）

## {title}

### 题目原文
```
[P3] question_bank.md:900 · test
Do you like parks?
```

### 她的原话（逐字）
```
{s1}
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
  · 更口语   ⚠️ 理由行
```

## ④ 收尾核对

（略）
"""


def put(d, name, text):
    sd = os.path.join(d, "sessions")
    os.makedirs(sd, exist_ok=True)
    p = os.path.join(sd, name)
    open(p, "w", encoding="utf-8").write(text)
    return p


def asked(d, rows):
    open(os.path.join(d, "asked.log"), "w", encoding="utf-8").write(
        "".join(f"{t}\tquestion_bank.md:{n}\tpersona\t{q}\n" for t, n, q in rows))


def qbank(d, lines):
    """lines ＝ {行号: 内容}，其余行填空。"""
    n = max(lines)
    open(os.path.join(d, "question_bank.md"), "w", encoding="utf-8").write(
        "\n".join(lines.get(i, "") for i in range(1, n + 1)) + "\n")


def world(d):
    """R1(bank:100) 09-01 以 RN 重答 ｜ R2(bank:200) 09-03 以 bank:200 重答 ｜ R3 从未重答
    bank:300 09-02 新题 ｜ bank:400 09-04 加练 ｜ asked.log 另有 500（### 标题提及）
    600（正文提及）700（哪都没有）"""
    put(d, "2026-09-01.md", free("2026-09-01", "d 段 重答 · R1（P3 · cold）"))
    put(d, "2026-09-02.md", free("2026-09-02", "③ 新题 · 第 1 道（bank:300 · P3 · cold）"))
    put(d, "2026-09-03.md", free("2026-09-03", "d 段 重答 · bank:200（P3 · cold）"))
    put(d, "2026-09-04.md", free("2026-09-04", "③b 加练新题（bank:400 · 她说再来一道）"))
    # bank:500：09-05 正文里先顺带提到（抽签记录），09-06 才在 `###` 标题里真答
    put(d, "2026-09-05.md", "# 2026-09-05 · **L2**\n\n剩余顺延：bank:500 · bank:6000\n")
    put(d, "2026-09-06.md", "# 2026-09-06 · **L3**\n\n## ③ 新题位 · 先清顺延\n\n"
                            "### 新题 · 逐题记录（顺延题 bank:500）\n\n（略）\n")
    # bank:600：只在正文里出现（question_bank.md:600 写法也认）
    put(d, "2026-09-07.md", "# 2026-09-07 · **L1**\n\n题目取自 question_bank.md:600。\n")
    asked(d, [("p3", 100, "Legacy one?"), ("p3", 300, "Three?"), ("p3", 500, "Five?"),
              ("p2", 600, "Describe six"), ("p3", 700, "Seven?")])
    qbank(d, {400: "**Cue card**: Describe four"})


def q(d):
    return {r["id"]: r for r in lab.redo_queue()}


class legacy:
    def __init__(self, v):
        self.v = v

    def __enter__(self):
        lab.LEGACY_REDO = self.v

    def __exit__(self, *a):
        lab.LEGACY_REDO = REAL_LEGACY


head("【Q0 正】题目集合 ＝ legacy ∪ session 新题／加练／重答 ∪ asked.log，⛔ 同一道题不重复")
with sandbox(p_text="", g_text="", sessions=False) as d, legacy(FAKE_LEGACY):
    world(d)
    Q = q(d)
    ids = sorted(Q)
    ck("共 8 道", len(Q) == 8, ids)
    for k in ("bank:100", "bank:200", "R3", "bank:300", "bank:400", "bank:500", "bank:600", "bank:700"):
        ck(f"{k} 在队列里", k in Q, ids)
    ck("⛔ R1 不另立一道（与 bank:100 同题）", "R1" not in Q, ids)
    ck("⛔ R2 不另立一道（与 bank:200 同题）", "R2" not in Q, ids)
    ck("⛔ 正文里的 bank:6000 不串成 bank:600 的提及", "bank:6000" not in Q, ids)
    ck("bank:100 的别名是 R1", Q["bank:100"]["alias"] == "R1")
    ck("没有 bank 行号的旧题用 RN 当编号", Q["R3"]["alias"] == "R3")

head("【Q1 正】首答日与重答日")
with sandbox(p_text="", g_text="", sessions=False) as d, legacy(FAKE_LEGACY):
    world(d)
    Q = q(d)
    ck("legacy 首答日照冻结值", Q["bank:100"]["first"] == "2026-08-01")
    ck("legacy 首答备注保留", Q["bank:100"]["first_note"] == "08-01 前")
    ck("R1：session 外重答日 ＋ 以 RN 写的 d 段都算",
       Q["bank:100"]["redos"] == ["2026-08-05", "2026-09-01"], Q["bank:100"]["redos"])
    ck("R2：以 bank:NNN 写的 d 段认成它的重答", Q["bank:200"]["redos"] == ["2026-09-03"],
       Q["bank:200"]["redos"])
    ck("新题节 ⇒ 首答日", Q["bank:300"]["first"] == "2026-09-02")
    ck("加练节 ⇒ 首答日", Q["bank:400"]["first"] == "2026-09-04")
    ck("新题／加练不算重答", not Q["bank:300"]["redos"] and not Q["bank:400"]["redos"])
    ck("asked.log 独有：`###` 标题提及优先于更早的正文提及",
       Q["bank:500"]["first"] == "2026-09-06", Q["bank:500"]["first"])
    ck("asked.log 独有：只有正文提及 ⇒ 取那天（question_bank.md:NNN 写法也认）",
       Q["bank:600"]["first"] == "2026-09-07", Q["bank:600"]["first"])
    ck("asked.log 独有、哪都找不到 ⇒ 首答日不明（None）", Q["bank:700"]["first"] is None)
    ck("last ＝ max(首答, 重答)", Q["bank:100"]["last"] == "2026-09-01"
       and Q["bank:300"]["last"] == "2026-09-02" and Q["R3"]["last"] == "2026-08-03")

head("【Q2 正】类型／题目：legacy → asked.log → question_bank.md 行")
with sandbox(p_text="", g_text="", sessions=False) as d, legacy(FAKE_LEGACY):
    world(d)
    Q = q(d)
    ck("legacy 题目用冻结值", Q["bank:100"]["text"] == "Legacy one?")
    ck("asked.log 的类型大写", Q["bank:600"]["type"] == "P2" and Q["bank:300"]["type"] == "P3")
    ck("asked.log 的题目", Q["bank:300"]["text"] == "Three?")
    ck("两处都没有 ⇒ 读 question_bank.md 那一行（Cue card ⇒ P2）",
       Q["bank:400"]["type"] == "P2" and Q["bank:400"]["text"] == "Describe four",
       (Q["bank:400"]["type"], Q["bank:400"]["text"]))

head("【Q3 正】排序 ＝ 最久没动的在前（日期不明最前）→ 首答日 → 编号")
with sandbox(p_text="", g_text="", sessions=False) as d, legacy(FAKE_LEGACY):
    world(d)
    order = [r["id"] for r in lab.redo_queue()]
    # bank:200：首答 08-02、09-03 重答 ⇒ last 09-03，排在 bank:300（09-02）之后
    ck("顺序", order == ["bank:700", "R3", "bank:100", "bank:300", "bank:200", "bank:400",
                          "bank:500", "bank:600"], order)
    ck("日期不明的排最前", order[0] == "bank:700", order)
    ck("从未重答的旧题排在刚重答过的前面", order.index("R3") < order.index("bank:100"), order)

head("【Q4 正】同一天打平 ⇒ 首答日早的在前，再打平 ⇒ 编号小的在前")
with sandbox(p_text="", g_text="", sessions=False) as d, legacy(()):
    put(d, "2026-09-10.md", free("2026-09-10", "③ 新题 · 第 1 道（bank:90 · P3）"))
    put(d, "2026-09-11.md", free("2026-09-11", "③ 新题 · 第 1 道（bank:12 · P3）"))
    put(d, "2026-09-12.md", free("2026-09-12", "③ 新题 · 第 1 道（bank:80 · P3）")
        .replace("## ④ 收尾核对", "## ③b 加练新题（bank:7 · 加练）\n\n## ④ 收尾核对"))
    put(d, "2026-09-13.md", free("2026-09-13", "d 段 重答 · bank:90（P3）"))
    put(d, "2026-09-14.md", free("2026-09-14", "d 段 重答 · bank:12（P3）"))
    order = [r["id"] for r in lab.redo_queue()]
    ck("09-12 两道同日首答 ⇒ 编号小的 bank:7 在前", order[:2] == ["bank:7", "bank:80"], order)
    ck("然后 bank:90（09-13）→ bank:12（09-14）", order[2:] == ["bank:90", "bank:12"], order)

head("【Q5 正】`lab.py redo` 全表 ＋ 合计行；stats 用同一个函数")
with sandbox(p_text="", g_text="", sessions=False) as d, legacy(FAKE_LEGACY):
    world(d)
    st, rc, out = run(lab.cmd_redo, Args())
    ck("退出码 0", rc == 0, out[-300:])
    ck("合计行：共 8 道 ／ 未重答过 6 道", "共 8 道 ／ 未重答过 6 道" in out, out[-400:])
    ck("逐行带名次", re.search(r"^\s*1\. bank:700", out, re.M), out[:900])
    ck("别名列出来", re.search(r"bank:100\s+R1\s+P3", out), out)
    ck("从未重答写「从未」", re.search(r"bank:300 .*从未", out), out)
    ck("上次重答写日期", re.search(r"bank:100 .*上次重答 2026-09-01", out), out)
    ck("首答日期不明要点名", "日期不明" in out and "bank:700" in out.split("日期不明")[-1], out[-300:])
    ck("告诉她 d 段标题怎么写", "d 段 重答 · bank:NNN" in out)
    ck("⛔ redo 只读：没有生成任何队列文件",
       not any("redo" in f for f in os.listdir(d)), os.listdir(d))

head("【Q6 正】stats 打合计行 ＋ 最久没重答的 5 道（来自实时队列）")
with sandbox(p_text="", g_text="", sessions=False) as d, legacy(FAKE_LEGACY):
    world(d)
    st, rc, out = run(lab.cmd_stats, Args(brief=False))
    ck("合计行", "重答队列   共 8 道 ／ 未重答过 6 道" in out, out[:1200])
    ck("最久没重答的 5 道：以 bank:700 打头、R1 带别名",
       "最久没重答的 5 道：bank:700(从未)" in out and "bank:100(R1)(2026-09-01)" in out,
       [l for l in out.split("\n") if "最久" in l])
    st, rc, out = run(lab.cmd_stats, Args(brief=True))
    ck("--brief 只打合计行", "共 8 道" in out and "最久没重答的 5 道" not in out)

head("【Q7 负】什么都没有 ⇒ 空队列，不崩")
with sandbox(p_text="", g_text="", sessions=False) as d, legacy(()):
    ck("空列表", lab.redo_queue() == [])
    st, rc, out = run(lab.cmd_redo, Args())
    ck("合计行 0 道", "共 0 道 ／ 未重答过 0 道" in out, out)

head("【K0 正】redo_key：旧 R 号有 bank 行号 ⇒ 统一成 bank:NNN；没有 ⇒ 原样")
with legacy(FAKE_LEGACY):
    ck("R1 → bank:100", lab.redo_key("R1") == "bank:100")
    ck("R3 → R3", lab.redo_key("R3") == "R3")
    ck("bank:5 → bank:5", lab.redo_key("bank:5") == "bank:5")
    ck("不认识的 R99 → R99", lab.redo_key("R99") == "R99")
ck("真常量 R1–R36 齐全、编号连续", [r[0] for r in REAL_LEGACY] ==
   [f"R{i}" for i in range(1, 37)])
ck("真常量的 bank 行号互不相同", len({r[1] for r in REAL_LEGACY}) == len(REAL_LEGACY))

head("【D0 正】deliver：重答节标题写 bank:NNN 或 RN 都认；一个都没有 ⇒ ERROR")
with sandbox(p_text="", g_text="", sessions=False) as d, legacy(FAKE_LEGACY):
    for title, bad in (("d 段 重答 · bank:200（P3 · cold）", False),
                       ("d 段 重答 · R3（P2 · cold）", False),
                       ("d 段 重答（P3 · cold）", True)):
        p = put(d, "2026-09-20.md", free("2026-09-20", title))
        sc = lab.scan_session(p)
        ck(f"「{title[:20]}」认成重答节", [s["kind"] for s in sc["sections"]][:1] == ["redo"],
           [s["kind"] for s in sc["sections"]])
        P = lab.check_session(sc, "redo")
        hit = [m for lv, loc, m in P if "重答节标题没带题号" in m]
        ck(f"「{title[:20]}」{'报' if bad else '不报'}缺题号", bool(hit) == bad, P)

head("【L0 正】回看：旧 R 号与 bank:NNN 是同一道题；同一道题重答后，更早的回看不算数")
with sandbox(p_text="", g_text="", sessions=False) as d, legacy(FAKE_LEGACY):
    put(d, "2026-09-01.md", free("2026-09-01", "d 段 重答 · R2（P3 · cold）", s1="Old is here."))
    ck("09-02 回看之前：R2 的 09-01 那篇待回看", lab.pending_free_ids("2026-09-02") == ["R2"],
       lab.pending_free_ids("2026-09-02"))
    put(d, "2026-09-02.md", "# 2026-09-02 · **L1**\n\n## ② 回看 · R2\n\n（略）\n")
    put(d, "2026-09-03.md", free("2026-09-03", "d 段 重答 · bank:200（P3 · cold）", s1="New is here."))
    ck("09-04：R2 那篇回看过了，bank:200 那篇（09-03 重答）要回看",
       lab.pending_free_ids("2026-09-04") == ["bank:200"], lab.pending_free_ids("2026-09-04"))
    src = lab.find_free_source("R2", "2026-09-04")
    ck("按 R2 找原篇 ⇒ 最近的那篇（标题写的是 bank:200）",
       src and src["date"] == "2026-09-03", src and src["date"])
    ck("原篇四件套取到的是新原话", src and any("New is here." in l for l in src["parts"]["原话"]))
    put(d, "2026-09-04.md", "# 2026-09-04 · **L2**\n\n## ② 回看 · R2\n\n（略）\n")
    ck("09-05：以 R2 回看也算回看了 bank:200", lab.pending_free_ids("2026-09-05") == [],
       lab.pending_free_ids("2026-09-05"))

sys.exit(report("lab.py redo 重答队列实时算 正/负向测试"))
