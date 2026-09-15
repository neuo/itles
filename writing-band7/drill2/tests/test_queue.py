#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""召回队列（SKILL §3.6）的回归测试 —— 全部跑**自己造的**合成档案，⛔ 一次都不碰真档案。

跑法：  python3 writing-band7/drill2/tests/test_queue.py
用途：  改过 drill.py 的梯子／逾期分／排序／配额／必出层／分组／复检交付闸之后先跑这个。

⚠️ 夹具纪律（§0.6）：⛔ 不写死真档案里的某个编号、⛔ 不写死「恰好 N 条」——
   这里全部条目都是**当场造出来的**，改档案不会把这个台弄红。

覆盖：
  A  梯子档位与间隔：未毕业 1/1/2 · 毕业 3/7/16/32/60 · 在池掉过的降一格（复检队列不降格）
  B  有效上次：✅ ◎✅ ❌ 📖 △ 📋 进 ｜ ◎− ③ 📝 与被改判的行⛔不进
  C  rc（复检次数）：只数毕业日之后的 ✅ ◎✅ 📋 · 按天去重 · 回潮后归零
  D  逾期分与排序：单位是练习日（休息日不占位）· 在池：逾期分降序 → 掉过的优先 → 编号升序 · 复检：复检次数少 → 已等多 → 编号
  E  剔除口径：退池／并入／挂作文验／本日已用／建号当天
  F  必出层：D-1 新建的全出 · 不受上限 · 不到期也出 · 今天已测过的不算
  G  配额与下溢：learn 3/1 · review 5/3 · 在池排不满 ⇒ 下溢 · 必出层超上限 ⇒ 下溢 0
     · --scope 只影响**打印**，⛔ 不改配额
  H  分组：组间按队列顺序切（组 1 ＝ 最该测的）· 组内错开同族 · --size 边界
  I  append 写 graduated.md：能写 · 自查不过时**两个文件一起回滚**
  J  流水：used --queue grad 写「复检组N」· read_drawn 两条队列分开数 · 组号取 max+1
  K  deliver 复检节：登记进 KNOWN_H2（⛔ 不被上一节吞）· ❌0 免块 · ❌N 要块 ·
     回潮数 ≠ ❌ 数报错 · 战报四行缺一行报错
"""
import io, os, re, shutil, sys, tempfile, contextlib

WT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, WT)
import drill

PASS, FAIL = [], []


def ck(name, cond, note=""):
    (PASS if cond else FAIL).append(name)
    print(("  ✅ " if cond else "  ❌ ") + name + (("  — " + str(note)) if note and not cond else ""))


class Args:
    def __init__(self, **kw):
        for k, v in dict(dry_run=False, changed=False, all=False, quiet=True,
                         type=None, detail=False, fam=None, state=None, pool=False,
                         size=10, groups=None, full=False, date=None, dry=True,
                         brief=False, file=None, session=None, section=None,
                         emit=False, group=None, scope="both", queue="pool",
                         used=None, dropped=None).items():
            setattr(self, k, v)
        for k, v in kw.items():
            setattr(self, k, v)


def run(fn, *a, **kw):
    so, se = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(so), contextlib.redirect_stderr(se):
        rc = fn(*a, **kw)
    return rc, so.getvalue(), se.getvalue()


# ══════════════════════════════════════════════════════════════════════
#  合成档案：一条条目一个块，格式严格照 §3.1
# ══════════════════════════════════════════════════════════════════════
HEAD_P = "# 问题总档（测试用）\n\n"
HEAD_G = "# 毕业档（测试用）\n\n"


def entry(num, state="在池", ok=0, bad=0, last="—", fam="F01", ask=None, rows=(),
          trigger="这是一句测试用的中文题面。"):
    ask_cell = f" ｜ 题型 {ask}" if ask else ""
    out = [f"## {num} 测试条目 {num}",
           f"状态：{state} ｜ 连对 {ok} ｜ 连错 {bad} ｜ 毕业线 2 ｜ 上次 {last} ｜ 族 {fam}{ask_cell}",
           "",
           "**问题是什么**", "测试。", "",
           "**中文触发点**", trigger, "",
           "### 历史记录"]
    if rows:
        for d, sym, note in rows:
            out.append(f"- {d} {sym} 测试场合{note}")
            out.append("  测试内容行。")
    else:
        out.append("- （从未被判定过）")
    out.append("")
    return "\n".join(out)


def archive(pool_entries=(), grad_entries=(), days=()):
    """→ (problems.md 文本, graduated.md 文本, log.md 文本)"""
    p = HEAD_P + "# F01 测试族\n\n" + "\n".join(pool_entries)
    g = HEAD_G + "# F01 测试族\n\n" + "\n".join(grad_entries)
    lg = "# 总账（测试用）\n\n" + "\n".join(
        f"📊 {d} · D1 学习日 C1" if t == "learn" else f"📊 {d} · D4 复习日 C1"
        for d, t in days)
    return p, g, lg


@contextlib.contextmanager
def sandbox(p_text, g_text, log_text):
    d = tempfile.mkdtemp(prefix="queue")
    io.open(os.path.join(d, "problems.md"), "w", encoding="utf-8").write(p_text)
    io.open(os.path.join(d, "graduated.md"), "w", encoding="utf-8").write(g_text)
    io.open(os.path.join(d, "log.md"), "w", encoding="utf-8").write(log_text)
    old = (drill.ROOT, drill.PROBLEMS, drill.GRADUATED, drill.LOG, drill.DRAWN)
    drill.ROOT = d
    drill.PROBLEMS = os.path.join(d, "problems.md")
    drill.GRADUATED = os.path.join(d, "graduated.md")
    drill.LOG = os.path.join(d, "log.md")
    drill.DRAWN = os.path.join(d, "drawn_review.log")
    try:
        yield d
    finally:
        (drill.ROOT, drill.PROBLEMS, drill.GRADUATED, drill.LOG, drill.DRAWN) = old
        shutil.rmtree(d, ignore_errors=True)


#  10 个练习日：09-01 … 09-10（中间 09-05 休息 ⇒ 不占位）
DAYS = [(f"2026-09-{n:02d}", "learn") for n in (1, 2, 3, 4, 6, 7, 8, 9, 10, 11)]
TODAY = "2026-09-12"          # 第 11 个练习日（log.md 里还没有它）


def one(num, **kw):
    """造一条、装进沙箱、返回解析出来的 Entry。"""
    st = kw.get("state", "在池")
    pe = [entry(num, **kw)] if st != "🎓" else []
    ge = [entry(num, **kw)] if st == "🎓" else []
    return archive(pe, ge, DAYS)


def load1(num, **kw):
    p, g, lg = one(num, **kw)
    with sandbox(p, g, lg):
        return [e for e in drill.load_all() if e.num == num][0]


# ══════════════════════════════════════════════════════════════════════
print("【A】梯子档位与间隔")
cases = [
    ("首测未做 ⇒ 间隔 1", dict(rows=()), 1),
    ("连错 1 ⇒ 间隔 1", dict(ok=0, bad=1, last="2026-09-01",
                            rows=(("2026-09-01", "❌", ""),)), 1),
    ("连错 2 ⇒ 间隔 1", dict(ok=0, bad=2, last="2026-09-02",
                            rows=(("2026-09-01", "❌", ""), ("2026-09-02", "❌", ""))), 1),
    ("连对 1 且从没掉过 ⇒ 间隔 2", dict(ok=1, bad=0, last="2026-09-01",
                                      rows=(("2026-09-01", "✅", ""),)), 2),
    ("连对 1 但掉过 ⇒ 降一格 ⇒ 间隔 1",
     dict(ok=1, bad=0, last="2026-09-02",
          rows=(("2026-09-01", "❌", ""), ("2026-09-02", "✅", ""))), 1),
]
for name, kw, want in cases:
    e = load1("#9001", **kw)
    ck(f"{name}（实得 {e.interval()}）", e.interval() == want, (e.rung_name(), e.interval()))

GROWS = [("2026-09-01", "✅", ""), ("2026-09-02", "✅", "")]          # 连对 2 ⇒ 毕业
grad_cases = [(0, 3), (1, 7), (2, 16), (3, 32), (4, 60), (7, 60)]
for rc_want, iv in grad_cases:
    rows = list(GROWS) + [(f"2026-09-{2+i+1:02d}", "✅", "") for i in range(rc_want)]
    e = load1("#9002", state="🎓", ok=2 + rc_want, bad=0, last=rows[-1][0], rows=tuple(rows))
    ck(f"🎓 rc{rc_want} ⇒ 间隔 {iv}", e.rechecks() == min(rc_want, 99) and e.interval() == iv,
       (e.rechecks(), e.interval()))
e = load1("#9003", state="🎓", ok=2, bad=0, last="2026-09-04",
          rows=(("2026-09-01", "❌", ""), ("2026-09-02", "✅", ""), ("2026-09-04", "✅", "")))
ck("🎓 掉过也不降格 ⇒ rc0 间隔 3", not e.at_risk() and e.interval() == 3, (e.rung_name(), e.interval()))
e = load1("#9004", state="🎓", ok=3, bad=0, last="2026-09-06",
          rows=(("2026-09-01", "❌", ""), ("2026-09-02", "✅", ""),
                ("2026-09-04", "✅", ""), ("2026-09-06", "✅", "")))
ck("🎓 rc1 掉过也不降格 ⇒ 间隔 7（复检队列不看历史 ❌）",
   e.rechecks() == 1 and not e.at_risk() and e.interval() == 7,
   (e.rechecks(), e.rung_name(), e.interval()))
ck("ever_bad 仍数全部历史", e.ever_bad(), e.ever_bad())
e = load1("#9006", state="🎓", ok=2, bad=0, last="2026-09-06",
          rows=(("2026-09-01", "❌", ""), ("2026-09-02", "✅", ""),
                ("2026-09-04", "✅", ""), ("2026-09-06", "△", "")))
ck("毕业后只有 △ ⇒ 复检次数 0、不降格 ⇒ 间隔 3",
   e.rechecks() == 0 and not e.at_risk() and e.interval() == 3,
   (e.rechecks(), e.at_risk(), e.interval()))
e = load1("#9007", state="🎓", ok=2, bad=0, last="2026-09-06",
          rows=(("2026-09-01", "✅", ""), ("2026-09-02", "✅", ""),
                ("2026-09-04", "✅", ""), ("2026-09-06", "❌", "")))
ck("🎓 状态下出现 ❌（还没回潮）⇒ at_risk 仍为假（回潮靠改状态行）", not e.at_risk(),
   (e.grad_day(), e.rechecks(), e.at_risk()))
e = load1("#9008", state="🎓", ok=2, bad=0, last="2026-09-06",
          rows=(("2026-09-01", "❌", ""), ("2026-09-02", "✅", ""),
                ("2026-09-04", "✅", ""), ("2026-09-06", "📋", "")))
ck("毕业后作文里 📋 顺带用对 ⇒ 计入复检次数 ⇒ 间隔 7", not e.at_risk() and e.interval() == 7,
   (e.rechecks(), e.at_risk(), e.interval()))

# ══════════════════════════════════════════════════════════════════════
print("\n【B】有效上次认哪些符号")
for sym, want in (("✅", True), ("◎✅", True), ("❌", True), ("📖", True),
                  ("△", True), ("📋", True), ("◎−", False), ("③", False), ("📝", False)):
    e = load1("#9005", ok=0, bad=0, last="2026-09-02",
              rows=(("2026-09-01", "✅", ""), ("2026-09-02", sym, "")))
    got = e.eff_last() == "2026-09-02"
    ck(f"{sym} {'进' if want else '⛔ 不进'}有效上次", got == want, e.eff_last())
e = load1("#9006", ok=1, bad=0, last="2026-09-02",
          rows=(("2026-09-01", "✅", ""),
                ("2026-09-02", "❌", "　⚠️ **本条已于 2026-09-03 改判为 ✅，见下方更正块**")))
ck("被 §4.7 改判的行⛔不进有效上次", e.eff_last() == "2026-09-01", e.eff_last())
e = load1("#9007")
ck("一条判定行都没有 ⇒ 有效上次 None ＝ 从未测过", e.eff_last() is None, e.eff_last())

# ══════════════════════════════════════════════════════════════════════
print("\n【C】rc ＝ 毕业日之后的「对」")
e = load1("#9008", state="🎓", ok=2, bad=0, last="2026-09-04",
          rows=(("2026-09-01", "✅", ""), ("2026-09-02", "✅", ""),
                ("2026-09-04", "📋", "")))
ck("📋 顺带用对推进 rc", e.rechecks() == 1, e.rechecks())
e = load1("#9009", state="🎓", ok=2, bad=0, last="2026-09-04",
          rows=(("2026-09-01", "✅", ""), ("2026-09-02", "✅", ""),
                ("2026-09-04", "📋", ""), ("2026-09-04", "✅", "（同一天第二次）")))
ck("同一天两行「对」只算 1 次 rc", e.rechecks() == 1, e.rechecks())
e = load1("#9010", state="🎓", ok=2, bad=0, last="2026-09-02",
          rows=(("2026-09-01", "✅", ""), ("2026-09-02", "✅", "")))
ck("毕业日当天的那次⛔不算 rc", e.rechecks() == 0, (e.grad_day(), e.rechecks()))
e = load1("#9011", state="🎓", ok=2, bad=0, last="2026-09-08",
          rows=(("2026-09-01", "✅", ""), ("2026-09-02", "✅", ""),
                ("2026-09-04", "❌", ""),                       # 回潮
                ("2026-09-06", "✅", ""), ("2026-09-08", "✅", "")))
ck("回潮后重新毕业 ⇒ 毕业日重算、rc 归零",
   e.grad_day() == "2026-09-08" and e.rechecks() == 0, (e.grad_day(), e.rechecks()))
e = load1("#9012", state="🎓", ok=2, bad=0, last="2026-09-06",
          rows=(("2026-09-01", "✅", ""), ("2026-09-02", "✅", ""),
                ("2026-09-06", "△", "")))
ck("△ ⛔ 不推 rc（但进有效上次）",
   e.rechecks() == 0 and e.eff_last() == "2026-09-06", (e.rechecks(), e.eff_last()))

# ══════════════════════════════════════════════════════════════════════
print("\n【D】逾期分与排序")
p, g, lg = one("#9013", ok=1, bad=0, last="2026-09-04", rows=(("2026-09-04", "✅", ""),))
with sandbox(p, g, lg):
    e = [x for x in drill.load_all() if x.num == "#9013"][0]
    pd = drill.practice_days()
    tidx = drill.today_index(pd, TODAY)
    ck("今天算一个练习日（log.md 里还没写今天）", tidx == len(DAYS) + 1, (tidx, len(DAYS)))
    ck("休息日不占位：09-04 → 今天 ＝ 7 个练习日（09-05 休息不算）",
       drill.waited_days(e, pd, tidx) == 7, drill.waited_days(e, pd, tidx))
    ck("逾期分 ＝ 7 ÷ 2 ＝ 3.5", abs(drill.overdue(e, pd, tidx) - 3.5) < 1e-9,
       drill.overdue(e, pd, tidx))

ents_p = [
    entry("#9020", ok=1, last="2026-09-10", rows=(("2026-09-10", "✅", ""),)),   # 逾期分 1.0
    entry("#9021", ok=1, last="2026-09-04", rows=(("2026-09-04", "✅", ""),)),   # 3.5
    entry("#9022", ok=1, bad=0, last="2026-09-10",                              # 掉过 ⇒ 间隔1 ⇒ 2.0
          rows=(("2026-09-01", "❌", ""), ("2026-09-10", "✅", ""))),
    entry("#9023"),                                                             # 从未测过 ⇒ ∞
]
p, g, lg = archive(ents_p, [], DAYS)
with sandbox(p, g, lg):
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    order = [e.num for e in P["pool_due"]]
    ck("排序 ＝ 逾期分降序（∞ → 3.5 → 2.0 → 1.0）",
       order == ["#9023", "#9021", "#9022", "#9020"], order)

ents_p = [entry("#9030", ok=1, last="2026-09-04", rows=(("2026-09-04", "✅", ""),)),
          entry("#9031", ok=1, bad=0, last="2026-09-02",
                rows=(("2026-09-01", "❌", ""), ("2026-09-02", "✅", "")))]
#  #9030：等 7 ÷ 2 = 3.5　｜ #9031：掉过 ⇒ 间隔 1，等 9 ⇒ 9.0 —— 逾期分先分胜负
p, g, lg = archive(ents_p, [], DAYS)
with sandbox(p, g, lg):
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    ck("逾期分优先于「掉过的优先」", [e.num for e in P["pool_due"]] == ["#9031", "#9030"],
       [e.num for e in P["pool_due"]])

ents_p = [entry("#9041", ok=1, bad=0, last="2026-09-10",
                rows=(("2026-09-01", "❌", ""), ("2026-09-10", "✅", ""))),   # 掉过，间隔1，2.0
          entry("#9040", ok=0, bad=1, last="2026-09-10",
                rows=(("2026-09-10", "❌", ""),))]                            # 掉过，间隔1，2.0
p, g, lg = archive(ents_p, [], DAYS)
with sandbox(p, g, lg):
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    ck("逾期分相同 ⇒ 编号升序", [e.num for e in P["pool_due"]] == ["#9040", "#9041"],
       [e.num for e in P["pool_due"]])

ents_g = [
    entry("#9050", state="🎓", ok=3, bad=0, last="2026-09-03",
          rows=(("2026-09-01", "✅", ""), ("2026-09-02", "✅", ""), ("2026-09-03", "✅", ""))),   # rc1 · 已等 8
    entry("#9051", state="🎓", ok=2, bad=0, last="2026-09-04",
          rows=(("2026-09-01", "✅", ""), ("2026-09-04", "✅", ""))),                           # rc0 · 已等 7
    entry("#9052", state="🎓", ok=2, bad=0, last="2026-09-07",
          rows=(("2026-09-06", "✅", ""), ("2026-09-07", "✅", ""))),                           # rc0 · 已等 5
    entry("#9053", state="🎓", ok=2, bad=0, last="2026-09-07",
          rows=(("2026-09-01", "❌", ""), ("2026-09-06", "✅", ""), ("2026-09-07", "✅", ""))),   # rc0 · 已等 5 · 掉过
]
p, g, lg = archive([], ents_g, DAYS)
with sandbox(p, g, lg):
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    order = [e.num for e in P["grad_due"]]
    ck("复检排序 ＝ 复检次数少 → 已等多 → 编号（掉过 ⛔ 不影响）",
       order == ["#9051", "#9052", "#9053", "#9050"], order)

# ══════════════════════════════════════════════════════════════════════
print("\n【D2】今天判过的条目，逾期分必须是 0（2026-09-05 对抗演练查出的阻断级 bug）")
#  ⛔ `log.md` 的今日行是**收尾才写**的 ⇒ 整场 session 里今天都不在 log 里。
#     旧写法两把尺（today_index 数 n+1、day_index 数 n）⇒ 今天刚判过的算成「等了 1」
#     ⇒ 间隔 1 的档位逾期分 1.0 ＝ 到期 ⇒ 同一天被重新排进后面的组。
#     顺带判定**不进 used**，挡不住它 —— 真档案里 `❌ …（顺带）` 有 195 条。
D1_ = DAYS[-1][0]
for tag, days in (("log.md 里【没有】今天（收尾前的常态）", DAYS),
                  ("log.md 里【已有】今天（收尾后）", DAYS + [(TODAY, "learn")])):
    p_, g_, lg_ = archive([entry("#9060", ok=0, bad=1, last=TODAY,
                                 rows=((D1_, "③", "建号"), (TODAY, "❌", "顺带")))], [], days)
    with sandbox(p_, g_, lg_):
        e = drill.load_all()[0]
        P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
        w = drill.waited_days(e, P["pdays"], P["tidx"])
        od = drill.overdue(e, P["pdays"], P["tidx"])
        ck(f"{tag}：今天判过 ⇒ 等了 0 · 逾期分 0", w == 0 and od == 0, (w, od))
        ck(f"{tag}：⛔ 不排进任何一组",
           not P["pool_groups"], [[x.num for x in g] for g in P["pool_groups"]])
        ck(f"{tag}：列进「义务已尽」而不是必出层",
           [x.num for x in P["must_done"]] == ["#9060"] and not P["must"],
           ([x.num for x in P["must_done"]], [x.num for x in P["must"]]))
#  对照：昨天判过的照常到期（⛔ 别把尺子改过头）
p_, g_, lg_ = archive([entry("#9061", ok=0, bad=1, last=D1_,
                             rows=((D1_, "❌", "组1"),))], [], DAYS)
with sandbox(p_, g_, lg_):
    e = drill.load_all()[0]
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    ck("对照：昨天判过 ⇒ 等了 1 · 逾期分 1.0 · 照常到期",
       drill.waited_days(e, P["pdays"], P["tidx"]) == 1
       and drill.overdue(e, P["pdays"], P["tidx"]) == 1.0
       and [x.num for x in P["pool_take"]] == ["#9061"],
       [x.num for x in P["pool_take"]])

print("\n【D3】档案写歪时 pick ⛔ 不许崩（崩了教练连开场都跑不起来）")
nofam = "\n".join(["## #9070 漏写族这一格",
                   "状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 —", "",
                   "**问题是什么**", "测试。", "",
                   "**中文触发点**", "一句中文。", "",
                   "### 历史记录", "- （从未被判定过）", ""])
p_, g_, lg_ = archive([nofam, entry("#9071")], [], DAYS)
with sandbox(p_, g_, lg_):
    try:
        rc, out, _ = run(drill.cmd_pick, Args(type="learn", date=TODAY))
        ok_ = rc == 0 and "#9070" in out
    except Exception as ex:
        ok_, out = False, f"{type(ex).__name__}: {ex}"
    ck("状态行漏写「族」这一格 ⇒ pick 照常跑完（漏格本身由 check 报）", ok_, out)
    ents_ = drill.load_all()
    e0 = [x for x in ents_ if x.num == "#9070"][0]
    ck("⛔ 但 check 必须报得出这一条",
       any(lv == "ERROR" and "族" in m for lv, m in drill.check_entry(e0, set(), None)),
       drill.check_entry(e0, set(), None))

print("\n【E】剔除口径")
ents_p = [
    entry("#9050"),                                              # 正常
    entry("#9051", state="退池"),
    entry("#9052", state="并入 #9050"),
    entry("#9053", ask="作文验",
          trigger="这一条挂作文验。⛔ **挂作文验，不出单点题**（2026-09-01）—— 理由。"),
    entry("#9054", rows=((TODAY, "③", "建号"),), last=TODAY),     # 建号当天
]
p, g, lg = archive(ents_p, [], DAYS)
with sandbox(p, g, lg):
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    due = {e.num for e in P["pool_due"]}
    ck("退池⛔不进队列", "#9051" not in due, due)
    ck("并入⛔不进队列", "#9052" not in due, due)
    ck("挂作文验⛔不进队列", "#9053" not in due, due)
    ck("建号当天⛔不进队列", "#9054" not in due, due)
    ck("挂作文验列进排除报告", "#9053" in {e.num for e in P["excluded"]["essay"]})
    ck("建号当天列进排除报告", "#9054" in {e.num for e in P["excluded"]["fresh"]})
    P2 = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn",
                           used_ids={"#9050"})
    ck("本日已用⛔不进队列", "#9050" not in {e.num for e in P2["pool_due"]})
    ck("本日已用列进排除报告", "#9050" in {e.num for e in P2["excluded"]["used"]})

# ══════════════════════════════════════════════════════════════════════
print("\n【F】必出层 ＝ D-1 那天新建的（她 2026-09-05 定）")
D1 = DAYS[-1][0]              # 2026-09-11
#  35 条老条目（逾期分都比必出层高）＋ 4 条 D-1 新建的
old = [entry(f"#9{100+i:03d}", ok=1, last="2026-09-01",
             rows=(("2026-09-01", "✅", ""),)) for i in range(35)]
fresh = [entry(f"#9{200+i:03d}", rows=((D1, "③", "建号"),), last=D1) for i in range(4)]
p, g, lg = archive(old + fresh, [], DAYS)
with sandbox(p, g, lg):
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    must = {e.num for e in P["must"]}
    take = {e.num for e in P["pool_take"]}
    ck("D-1 新建的 4 条全部进必出层", must == {f"#9{200+i:03d}" for i in range(4)}, must)
    ck("必出层排在队首（⛔ 不会被上限截掉）", must <= take, (must - take))
    ck("学习日在池上限 3 组 ⇒ 出 30 条", len(P["pool_take"]) == 30, len(P["pool_take"]))
#  必出层自己超过上限
fresh40 = [entry(f"#9{300+i:03d}", rows=((D1, "③", "建号"),), last=D1) for i in range(35)]
p, g, lg = archive(old + fresh40, [], DAYS)
with sandbox(p, g, lg):
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    ck("必出层 35 条 > 3 组 ⇒ 今天**只出必出层**，⛔ 不补别的",
       {e.num for e in P["pool_take"]} == {e.num for e in P["must"]} and len(P["pool_take"]) == 35,
       len(P["pool_take"]))
    ck("必出层撑爆上限 ⇒ 下溢 0", P["spill"] == 0, P["spill"])
#  D-1 新建、但**今天已经测过**
done = [entry("#9400", ok=1, last=TODAY, rows=((D1, "③", "建号"), (TODAY, "✅", "顺带")))]
p, g, lg = archive(done, [], DAYS)
with sandbox(p, g, lg):
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    ck("D-1 新建但今天已测过 ⇒ ⛔ 不再算必出", not P["must"], [e.num for e in P["must"]])
    ck("它列进「义务已尽」那一栏", [e.num for e in P["must_done"]] == ["#9400"],
       [e.num for e in P["must_done"]])
#  D-1 新建、当天判过一次 ⇒ 逾期分 0.5 不到期，但必出层照样出
half = [entry("#9401", ok=1, last=D1, rows=((D1, "③", "建号"), (D1, "✅", "同日")))]
p, g, lg = archive(half, [], DAYS)
with sandbox(p, g, lg):
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    ck("必出层⛔不看到期：逾期分 0.5 也照样出",
       [e.num for e in P["must"]] == ["#9401"] and not P["pool_due"],
       ([e.num for e in P["must"]], [e.num for e in P["pool_due"]]))

# ══════════════════════════════════════════════════════════════════════
print("\n【G】配额与下溢")
grads = [entry(f"#95{i:02d}", state="🎓", ok=2, last="2026-09-01",
               rows=(("2026-08-01", "✅", ""), ("2026-09-01", "✅", "")))
         for i in range(60)]
pool_many = [entry(f"#96{i:02d}", ok=1, last="2026-09-01",
                   rows=(("2026-09-01", "✅", ""),)) for i in range(60)]
p, g, lg = archive(pool_many, grads, DAYS)
with sandbox(p, g, lg):
    L = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    R = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "review")
    ck("学习日 在池 3 组 ＋ 复检 1 组", len(L["pool_groups"]) == 3 and len(L["grad_groups"]) == 1,
       (len(L["pool_groups"]), len(L["grad_groups"])))
    ck("复习日 在池 5 组 ＋ 复检 3 组", len(R["pool_groups"]) == 5 and len(R["grad_groups"]) == 3,
       (len(R["pool_groups"]), len(R["grad_groups"])))
    ck("在池排满 ⇒ 下溢 0", L["spill"] == 0 and R["spill"] == 0)
p, g, lg = archive(pool_many[:5], grads, DAYS)          # 在池只够 1 组
with sandbox(p, g, lg):
    L = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    ck("在池只排 1 组 ⇒ 下溢 2 组给复检", L["spill"] == 2 and len(L["grad_groups"]) == 3,
       (L["spill"], len(L["grad_groups"])))
p, g, lg = archive([], grads, DAYS)                     # 在池空
with sandbox(p, g, lg):
    L = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    ck("在池空 ⇒ 下溢 3 组 ⇒ 复检 4 组", L["spill"] == 3 and len(L["grad_groups"]) == 4,
       (L["spill"], len(L["grad_groups"])))
    rc, out, _ = run(drill.cmd_pick, Args(type="learn", date=TODAY, scope="grad"))
    ck("--scope grad ⛔ 不把在池的上限让给复检（仍是 4 组）",
       "基础 1 组 ＋ 在池下溢 3 组" in out,
       [l for l in out.split("\n") if "复检队列" in l])
    ck("--scope grad 只打印复检组", "━━━ 在池组" not in out and "━━━ 复检组" in out)
    rc, out, _ = run(drill.cmd_pick, Args(type="learn", date=TODAY, scope="pool"))
    ck("--scope pool 只打印在池组", "━━━ 复检组" not in out)
p, g, lg = archive(pool_many, [], DAYS)                 # 复检空
with sandbox(p, g, lg):
    L = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "learn")
    ck("复检空⛔不回补在池（在池仍是 3 组）", len(L["pool_groups"]) == 3, len(L["pool_groups"]))

# ══════════════════════════════════════════════════════════════════════
print("\n【H】分组")
mixed = []
for i in range(25):
    mixed.append(entry(f"#97{i:02d}", ok=1, last="2026-09-01", fam="F0%d" % (1 + i % 3),
                       rows=(("2026-09-01", "✅", ""),)))
p, g, lg = archive(mixed, [], DAYS)
with sandbox(p, g, lg):
    P = drill.plan_queues(drill.load_all(), TODAY, drill.day_types(), "review", size=10)
    gs = P["pool_groups"]
    ck("25 条切成 3 组（10/10/5）", [len(x) for x in gs] == [10, 10, 5], [len(x) for x in gs])
    ck("组 1 的集合 ＝ 队列最前面的 10 条",
       {e.num for e in gs[0]} == {e.num for e in P["pool_take"][:10]})
    adj = sum(1 for x in gs for a, b in zip(x, x[1:]) if a.fam == b.fam)
    ck("组内错开同族：相邻同族 0 次", adj == 0, adj)
    rc, out, _ = run(drill.cmd_pick, Args(type="review", date=TODAY, size=0))
    ck("--size 0 ⇒ 报错退出，⛔ 不静默产出 0 组", rc == 1, out[:200])
    rc, out, _ = run(drill.cmd_pick, Args(type="review", date=TODAY, size=-3))
    ck("--size 负数 ⇒ 报错退出", rc == 1, out[:200])

# ══════════════════════════════════════════════════════════════════════
print("\n【I】append 写 graduated.md（复检天天要用）")
gg = [entry("#9800", state="🎓", ok=2, last="2026-09-01",
            rows=(("2026-08-01", "✅", ""), ("2026-09-01", "✅", "")))]
p, g, lg = archive([entry("#9801")], gg, DAYS)
with sandbox(p, g, lg) as d:
    rows = os.path.join(d, "rows.md")
    io.open(rows, "w", encoding="utf-8").write("#9800 ✅ 复检组1 第 1 题\n  稳。\n")
    rc, out, _ = run(drill.cmd_append, Args(file=rows, date="2026-09-12", dry_run=False))
    ck("append 能往 graduated.md 写判定行", rc == 0 and "graduated.md" in out, out[-400:])
    txt = io.open(drill.GRADUATED, encoding="utf-8").read()
    ck("判定行真的落进了 graduated.md", "2026-09-12 ✅ 复检组1" in txt)
    e = [x for x in drill.load_all() if x.num == "#9800"][0]
    ck("rc 跟着涨（毕业日之后又对了一次）", e.rechecks() == 1, e.rechecks())
with sandbox(p, g, lg) as d:
    rows = os.path.join(d, "rows.md")
    io.open(rows, "w", encoding="utf-8").write("#9800 ✅ 复检组1\n  稳。\n#9999 ✅ 不存在\n  x。\n")
    before_g = io.open(drill.GRADUATED, encoding="utf-8").read()
    before_p = io.open(drill.PROBLEMS, encoding="utf-8").read()
    rc, out, _ = run(drill.cmd_append, Args(file=rows, date="2026-09-12", dry_run=False))
    ck("批里有一条查无此编号 ⇒ 整批不写", rc == 1
       and io.open(drill.GRADUATED, encoding="utf-8").read() == before_g
       and io.open(drill.PROBLEMS, encoding="utf-8").read() == before_p, out[:300])

# ══════════════════════════════════════════════════════════════════════
print("\n【I2】append 自查⛔不许把【存量】错误当成自己引入的（假回滚）")
#  行号会随插入整体下移 ⇒ 比对必须先用 `_msg_key` 抹掉 L 号（migrate 早就是这么干的）。
def broken_entry(num, day):
    """带一条存量坏行：只写符号、没有缩进内容行 ⇒ check 本来就报 ERROR。"""
    return "\n".join([f"## {num} 测试 {num}",
                      f"状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 {day} ｜ 族 F01", "",
                      "**问题是什么**", "测试。", "",
                      "**中文触发点**", "一句中文。", "",
                      "### 历史记录", f"- {day} ✅ 场合", ""])
body = [entry("#9080", ok=1, last="2026-09-10", rows=(("2026-09-10", "✅", ""),)),
        broken_entry("#9081", "2026-09-10")]
p_, g_, lg_ = archive(body, [], DAYS)
for tag, txt, want in (
        ("只 append 后面那条（行号不移）", "#9081 ✅ 场合\n  内容行。\n", 0),
        ("两条一批（前面先插行 ⇒ 后面行号下移）",
         "#9080 ✅ 场合\n  内容行。\n#9081 ✅ 场合\n  内容行。\n", 0)):
    with sandbox(p_, g_, lg_) as dd:
        rf = os.path.join(dd, "rows.md")
        io.open(rf, "w", encoding="utf-8").write(txt)
        rc, out, _ = run(drill.cmd_append, Args(file=rf, date="2026-09-12", dry_run=False))
        ck(f"{tag} ⇒ 照常写盘（⛔ 不因存量坏行整批回滚）", rc == want, out[-400:])

print("\n【I3】🎓 吃到 ❌ 却忘了改状态行 ⇒ check 必须报（2026-09-05 补）")
#  ⛔ 忘了改的后果不是"下次照常召回"，而是**比答对的还晚回来**：
#     状态还挂 🎓 ⇒ 那次 ❌ 把毕业日清掉 ⇒ rc 算 0 ⇒ 站 🎓rc0 ＝ 等 3 个练习日；
#     本该回在池站「连错1」＝ 等 1 个练习日。
forgot = entry("#9090", state="🎓", ok=0, bad=1, last="2026-09-10",
               rows=(("2026-09-01", "✅", ""), ("2026-09-02", "✅", ""),
                     ("2026-09-10", "❌", "复检组1")))
p_, g_, lg_ = archive([], [forgot], DAYS)
with sandbox(p_, g_, lg_):
    e = [x for x in drill.load_all() if x.num == "#9090"][0]
    probs = drill.check_entry(e, set(), None)
    ck("check 报 ERROR：状态是 🎓 但历史重数连对 < 2",
       any(lv == "ERROR" and "当场回潮" in m for lv, m in probs), probs)
    ck("坐实后果：忘了改 ⇒ 应等 3 个练习日（🎓rc0）", e.interval() == 3,
       (e.rung_name(), e.interval()))
fixed = entry("#9090", state="在池", ok=0, bad=1, last="2026-09-10",
              rows=(("2026-09-01", "✅", ""), ("2026-09-02", "✅", ""),
                    ("2026-09-10", "❌", "复检组1")))
p_, g_, lg_ = archive([fixed], [], DAYS)
with sandbox(p_, g_, lg_):
    e = [x for x in drill.load_all() if x.num == "#9090"][0]
    ck("改回在池之后 ⇒ 应等 1 个练习日（连错1 掉过降级）", e.interval() == 1,
       (e.rung_name(), e.interval()))
    ck("⇒ 差别是 3 天 vs 1 天：不修的话答错的反而回得更晚", True)
    ck("改对了 check 就不报", not [m for lv, m in drill.check_entry(e, set(), None)
                                  if lv == "ERROR" and "当场回潮" in m])

print("\n【I4】「跳过」只认「本节跳过」四个字（2026-09-05 收紧）")
SKIP_SESS = """# 2026-09-12 · D1 · 周期 1

## 复检 · 第 1 组（1 题 / 1 条）
这一组我打算 ⇒ 跳过 不测了，理由写在下面。

## 收尾
"""
rc, out = (lambda t: (lambda d: (lambda f: (
    io.open(f, "w", encoding="utf-8").write(t),
    run(drill.cmd_deliver, Args(session=f))[:2])[1])(
        os.path.join(d, "2026-09-12.md")))(tempfile.mkdtemp(prefix="skip")))(SKIP_SESS)
ck("松写法「⇒ 跳过」⛔ 不再让整节免检", rc != 0 and "SKIP" not in out, out[-500:])
rc2, out2 = (lambda t: (lambda d: (lambda f: (
    io.open(f, "w", encoding="utf-8").write(t),
    run(drill.cmd_deliver, Args(session=f))[:2])[1])(
        os.path.join(d, "2026-09-12.md")))(tempfile.mkdtemp(prefix="skip")))(
    SKIP_SESS.replace("⇒ 跳过", "本节跳过"))
ck("「本节跳过」照旧打 SKIP", rc2 == 0 and "SKIP" in out2, out2[-500:])

print("\n【J】流水：两条队列各自编号")
p, g, lg = archive([entry("#9900")], [], DAYS)
with sandbox(p, g, lg) as d:
    run(drill.cmd_used, Args(queue="pool", group=1, used="#9900", date=TODAY))
    run(drill.cmd_used, Args(queue="grad", group=1, used="#9901", date=TODAY))
    used, groups = drill.read_drawn(TODAY)
    ck("两条队列的组号分开数", groups["pool"] == {1} and groups["grad"] == {1}, groups)
    ck("用过的编号两条队列合起来算", used == {"#9900", "#9901"}, used)
    line = io.open(drill.DRAWN, encoding="utf-8").read()
    ck("复检组写成「复检组N」", "\t复检组1\t" in line and "\t组1\t" in line, line)
ck("组号取已收尾的最大值 ＋1（⛔ 不是组数 ＋1）",
   drill.next_group_no({5}) == 6 and drill.next_group_no(set()) == 1 and
   drill.next_group_no({1, 2, 5}) == 6)

# ══════════════════════════════════════════════════════════════════════
print("\n【K】deliver 复检节")
ck("「复检 ·」已登记进 KNOWN_H2（⛔ 不登记 ＝ 被上一节吞掉、整节不查）",
   "复检 ·" in drill.KNOWN_H2, drill.KNOWN_H2)

SESS = """# 2026-09-12 · D1 · 周期 1

## 开场
今天类型 学习日

## 复检 · 第 1 组（2 题 / 2 条）

### 题面（发给她的逐字）
```
1. 第一句中文。
2. 第二句中文。
```

### 她的答案（逐字抄）
```
1. First sentence.
2. Second sentence.
```

### a 判定表
| 题 | 编号 | 判定 |
|---|---|---|
| 1 | #9800 | ✅ |
| 2 | #9801 | ❌ |

### a 顺带判定
R1/R2 本组零命中。

### bc 三版对照块
```
#2
  原句　　　 Second sentence.
  最小修改　 The second sentence.
  └ 改了什么 补冠词（⇒ #9801）
  更好版　　 〔没有更好的版本〕
  └ 为什么好 最小修改已到位
```

### d 战报
本组 2 题 / 2 条
本组 ✅ 1 条：#9800
本组 ❌ 1 条：#9801
本组回潮 1 条：#9801

## 收尾
"""


def deliver_on(text, section=None):
    d = tempfile.mkdtemp(prefix="sess")
    f = os.path.join(d, "2026-09-12.md")
    io.open(f, "w", encoding="utf-8").write(text)
    rc, out, _ = run(drill.cmd_deliver, Args(session=f, section=section))
    shutil.rmtree(d, ignore_errors=True)
    return rc, out


rc, out = deliver_on(SESS)
ck("复检节被认出来并查了（⛔ 没被上一节吞掉）", "复检 · 第 1 组" in out, out[:400])
ck("正常一节 ⇒ ERROR 0", rc == 0, out[-600:])
ck("块数守恒对的是战报里的 ❌ 数", "战报里的『本组 ❌ 1 条』" in out, out[:800])

rc, out = deliver_on(SESS.replace("本组回潮 1 条：#9801", "本组回潮 0 条"))
ck("❌ 数 ≠ 回潮数 ⇒ ERROR（判了 ❌ 却没回潮）", rc != 0 and "回潮" in out, out[-500:])

no_blocks = SESS[:SESS.index("### bc 三版对照块")] + SESS[SESS.index("### d 战报"):]
rc, out = deliver_on(no_blocks)
ck("❌ 1 条却没有三版对照块 ⇒ ERROR", rc != 0 and "要走全套" in out, out[-500:])

all_ok = no_blocks.replace("本组 ✅ 1 条：#9800", "本组 ✅ 2 条：#9800 #9801") \
                  .replace("本组 ❌ 1 条：#9801", "本组 ❌ 0 条") \
                  .replace("本组回潮 1 条：#9801", "本组回潮 0 条") \
                  .replace("| 2 | #9801 | ❌ |", "| 2 | #9801 | ✅ |")
rc, out = deliver_on(all_ok)
ck("全 ✅ ⇒ ⛔ 不要求三版对照块，ERROR 0", rc == 0 and "不需要三版对照块" in out, out[-600:])

rc, out = deliver_on(all_ok.replace("本组 ❌ 0 条\n", ""))
ck("战报缺「本组 ❌ N 条」⇒ ERROR", rc != 0 and "本组 ❌ N 条" in out, out[-500:])
rc, out = deliver_on(SESS.replace("本组 2 题 / 2 条\n", ""))
ck("战报缺「本组 N 题 / K 条」⇒ ERROR", rc != 0 and "本组 N 题 / K 条" in out, out[-500:])
rc, out = deliver_on(SESS.replace("本组 ❌ 1 条：#9801", "本组 ❌ 1 条"))
ck("报了 ❌ 却不列编号 ⇒ ERROR（§0.4）", rc != 0 and "没列编号" in out, out[-600:])

#  ★★ 2026-09-05 补：战报的数是**手打的**，判定表才是读数（对抗演练查出的假绿）
rc, out = deliver_on(
    no_blocks.replace("本组 ✅ 1 条：#9800", "本组 ✅ 2 条：#9800 #9801")
             .replace("本组 ❌ 1 条：#9801", "本组 ❌ 0 条")
             .replace("本组回潮 1 条：#9801", "本组回潮 0 条"))
ck("判定表判了 ❌、战报却写「❌ 0 条」⇒ ERROR（⛔ 不许自报数蒙混过关）",
   rc != 0 and "判定表" in out and "对不上" in out, out[-700:])
rc, out = deliver_on(SESS.replace("本组回潮 1 条：#9801", "本组回潮 1 条：#9999"))
ck("回潮列的编号 ≠ 判 ❌ 的那几条 ⇒ ERROR（数对得上也不行）",
   rc != 0 and "回潮" in out and "凭据" in out, out[-700:])
rc, out = deliver_on(SESS.replace("| 2 | #9801 | ❌ |", "| 2 | #9801 | **❌** |"))
ck("判定表里符号加粗 ⇒ 读不出来 ⇒ ERROR（⛔ 不兜底）",
   rc != 0 and ("读不出来" in out or "对不上" in out), out[-700:])
rc, out = deliver_on(SESS, section="复检1")
ck("--section 复检1 能定位到这一节", rc == 0 and "复检 · 第 1 组" in out, out[:400])

print("\n" + "═" * 70)
print(f"召回队列回归测试 · 通过 {len(PASS)} · 失败 {len(FAIL)}")
for f in FAIL:
    print("  ❌ " + f)
print("═" * 70)
sys.exit(1 if FAIL else 0)
