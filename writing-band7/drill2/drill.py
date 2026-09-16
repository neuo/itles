#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""drill.py —— 写作 drill 线的【只读机械工具】。

她 2026-08-23 定：抽题与统计交给脚本，教练只读脚本吐出来的清单 + 抽中的那几条条目，
                  不再整档读 problems.md（15.2 万 tokens → 0.7 万）。

⛔ 本脚本【一个字的内容都不产生】。行文全部由教练手写，脚本只碰位置和算术：
     · 读  problems.md / graduated.md / log.md
     · 写  drawn_review.log（append-only 出题流水）
     · 写  problems.md —— 仅 `append` 子命令，且仅两件机器活：
            ① 把教练写好的历史行插到正确位置  ② 连对／连错／上次 三个数重算
          ⛔ 不改 🎓／状态／条目正文／成员出题账 —— 那些是判断，仍然手写（SKILL §0.3）
     · 搬  problems.md ⇄ graduated.md —— 仅 `migrate` 子命令，只按状态行第 1 格
          把**已有的整块字节**从一个文件挪到另一个文件（逐字节，搬完自校，不过就整批回滚）
          ⛔ 不改状态、不改正文、不改任何一个数、不碰两个文件的头部说明块
     · 搬  session ⇒ problems.md —— 仅 `trigger` 子命令，把 session 的「### 题面」围栏里
          **当天实际用的中文题面**逐字搬进条目的 `**中文触发点**` 节；老触发点压成一行留档不删
          ⛔ 不改状态、不改别的节、不碰历史记录；graduated／词组 ⇒ 报错整批不写；
          已搬过的跳过（幂等）；写完自校，不过就整批回滚
   session、战报、条目正文仍然全部手工写。

子命令
  出题（SKILL §4① §6 §8）—— 开场跑一次，当天全部候选一次分完组
    python3 drill.py pick  --type learn|review [--size 10] [--full] [--date YYYY-MM-DD] [--dry]
    python3 drill.py used  --group N --used "#0095,#0266" [--dropped "#0303=与第2题同词族"]
  建号查重（SKILL §3.5 第 1 步）
    python3 drill.py dedup "works" "workers" [--fam F05] [--limit 12] [--no-history]
    python3 drill.py list  [--fam F04] [--pool] [--state 在池]
    python3 drill.py show  #0059 [#0071 …]
  记账（SKILL §4③d ／ §3.1 契约⑪）—— 判定行写好后一次落盘，⛔ 不再手写插入位置
    python3 drill.py append --file rows.md --date 2026-08-25 [--dry-run]
  搬迁（SKILL §3.3 ／ §4⑥）—— 每天收尾自动做，🎓 出池、复发回池，整块字节搬
    python3 drill.py migrate [--dry-run]
  换题面（SKILL §0.3 ／ §6）—— 把 session 里当天用的中文题面搬回条目，幂等
    python3 drill.py trigger --session sessions/2026-09-01.md --group 1 [--dry-run]
  交付物硬闸（SKILL §4③bc §4④ §4⑤e）—— 发给她之前跑，ERROR>0 ⇒ 不许发
    python3 drill.py deliver --session sessions/2026-08-30.md [--section 组1|回看|新题|追加练]
  产出要粘贴的那一段（SKILL §0.9b⑥）—— 硬闸 ERROR 0 才吐，吐出来的一个字不许改
    python3 drill.py deliver --session sessions/2026-09-01.md [--section 组1] --emit
  统计与校验（SKILL §0.3 §0.4 §4⑥）
    python3 drill.py stats [--brief]
    python3 drill.py check [--changed | --all] [--quiet]

约定的档案格式见 SKILL §3.1 / §3.2。check 强制的就是那份格式，二者只有这一处定义。
⛔ 解析一律严格匹配，**不做兜底**：档案写歪 ⇒ check 报错 ⇒ 改档案，不改脚本。
"""

import argparse
import bisect
import contextlib
import io
import math
import os
import random
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
PROBLEMS = os.path.join(ROOT, "problems.md")
GRADUATED = os.path.join(ROOT, "graduated.md")
LOG = os.path.join(ROOT, "log.md")
DRAWN = os.path.join(ROOT, "drawn_review.log")

# ── 两条日期分界线（都在 SKILL §3.1 里明写，不是脚本自己的兜底）──────────────
# FORMAT_ERA：新体系建库日。这天**之后**写的历史行必须有缩进内容行；
#             更早的是从旧档案迁进来的，旧表就只记了日期/符号/场合（problems.md 头部已声明）。
FORMAT_ERA = "2026-08-19"
# STRICT_FROM：符号文法生效日。这天**之后**写的行，符号必须是 §3.2 表里的、且不加粗。
STRICT_FROM = "2026-08-24"

FAMILIES = [f"F{i:02d}" for i in range(1, 19) if i not in (13, 16)]

# ── 题型（SKILL §3.1 契约②第 7 格）─────────────────────────────────────────
#   「这条【怎么被行使】」，互斥三选一。⛔ 与 §3.1 契约⑫ 的「类型」不是一回事：
#   那些全是派生的，这一格是档案里**唯一存下来的**出题方式。
ASK_SENTENCE = "整句"      # 中译英整句单点题 —— 默认，状态行不写这一格就是它
ASK_PHRASE   = "词组"      # 中译英词组题，一题可打包多个（§3.1 契约⑬）
ASKS = (ASK_SENTENCE, ASK_PHRASE)
# 已取消的题型：作文验。这一类考点现在**只在判作文时指出来**，⛔ 不建号、⛔ 不判错。
ASK_RETIRED = ("作文验",)
# ASK_FROM：题型格生效日。这天**起**新建的条目，状态行必须自己写出题型；
#           更早的条目不写 ＝ 整句（存量默认，脚本只提示不报错）。
ASK_FROM = "2026-09-02"
# 定义上就是**句子层**的族 ⇒ ⛔ 不许标「词组」。
#   动词的形态与论元（F01 F09）· 数的一致（F04）· 句法（F07）· 丢层（F10）·
#   篇章任务层（F12）· 整句仿写（F17 F18）—— 这些只在句子里才失守，词组题测不到。
NO_PHRASE_FAMS = {"F01", "F04", "F07", "F09", "F10", "F12", "F17", "F18"}

# ── 符号文法（SKILL §3.2）────────────────────────────────────────────────
#   判定符号：推进 streak
JUDGE = {
    "✅":  "ok",       # 考点命中
    "◎✅": "ok",       # 题面逼不出考点但她的答案成立 ⇒ 算对
    "❌":  "bad",      # 真错（含答不出）
    "📖":  "bad",      # 教练给了答案、她照写
    "△":   "neutral",  # 有更好的表达，她的也成立
    "◎−":  "neutral",  # 题面诱发的错，两边都不动
}
#   留痕符号：不是判定，不推进 streak
TRACE = {
    "③":  "建号行（§2③ 她点名要学）",
    "📋": "顺带用对（🎓 状态不变／不推进）",
    "📝": "留痕行（高压留痕、题面加死、并入说明等）",
}
LEGACY = {
    "◎": "光杆 ◎（2026-08-22 之前的写法，之后必须写成 ◎✅ 或 ◎−）",
}
# 被 §4.7 改判／撤销掉的历史行：留痕不删，但【不参与 streak 重算】。
# 锚点写死成这四个字，教练写更正块时必须带上（SKILL §4.7）。
SUPERSEDED = "本条已于"
ALL_SYMBOLS = list(JUDGE) + list(TRACE) + list(LEGACY)
# 长符号优先，免得 ◎✅ 被切成 ◎
ALL_SYMBOLS.sort(key=len, reverse=True)

# ── 召回梯子（SKILL §3.6）──────────────────────────────────────────────────
#   一条梯子，毕业线只是中间一格。格上的数字 ＝ 应等几个【练习日】（休息日不存在）。
#     1  →  1  →  2  → ┃毕业线 连对2┃ →  3  →  7  →  16 →  32 →  60
#   首测未做 连错1  连对1                 rc0   rc1   rc2   rc3  rc≥4
RUNGS_POOL = [1, 1, 2]                  # 未毕业：0 首测未做/连错≥2 · 1 连错1 · 2 连对1
RUNGS_GRAD = [3, 7, 16, 32, 60]         # 已毕业：rc0 rc1 rc2 rc3 rc≥4
POOL_RUNG_NAME = ["首测未做·连错≥2", "连错1", "连对1"]
GRAD_RUNG_NAME = ["🎓 rc0", "🎓 rc1", "🎓 rc2", "🎓 rc3", "🎓 rc≥4"]

# 配额：(在池上限组数, 复检基础组数)。在池排不满 ⇒ 空出的组数下溢给复检，⛔ 反向不成立。
QUOTA = {"learn": (3, 1), "review": (5, 3)}
GROUP_SIZE = 10

#   ★ 进「有效上次」的符号（＝ 这一次真的被测到了，等待时钟从这天重新起算）
#     ✅ ◎✅ ❌ 📖  —— 判定符号里的 ok/bad
#     △            —— 她答出来了、只是有更好的说法 ⇒ 考点被行使过（⛔ 不推 rc）
#     📋 顺带用对   —— 毕业条目在作文里被自发用对 ⇒ 与一次复检通过同权
#   ⛔ 不算：◎−（题面诱发 ＝ 这次没测成）· 光杆 ◎ · ③ 建号行 · 📝 留痕行 · 被改判的行
EFF_LAST_SYMBOLS = {"✅", "◎✅", "❌", "📖", "△", "📋"}
#   ★ 推进 rc（复检次数）的符号：毕业日**之后**的「对」
RECHECK_SYMBOLS = {"✅", "◎✅", "📋"}

SECTIONS = ["问题是什么", "怎么发现的", "我错在哪", "中文触发点"]
# ⛔ 节标题严格逐字，不做兜底：档案写歪 ⇒ check 报错 ⇒ 改档案，不改脚本
SECTION_HEADS = {f"**{s}**" for s in SECTIONS}
MEMBERS_HEAD = "**成员出题账**"

RE_ENTRY = re.compile(r"^## (#\d{4})\s*(.*)$")
RE_STATUS = re.compile(r"^状态：(.*)$")
RE_HIST_HEAD = re.compile(r"^### 历史记录\s*$")
RE_HIST_ROW = re.compile(r"^-\s*(20\d\d-\d\d-\d\d)\s*(.*)$")
RE_FAM_HEAD = re.compile(r"^# (F\d\d)\b")
RE_LOG_ROW = re.compile(r"^[📊⏸]\s*\**\s*(20\d\d-\d\d-\d\d)\s*(.*)$")


def norm(s):
    """去掉加粗/零宽/全角空格，方便比对符号。"""
    s = s.replace("**", "").replace("​", "")
    s = s.replace("　", " ")
    return s.strip()


# ══════════════════════════════════════════════════════════════════════════
#  Parser —— 全脚本唯一一处「档案长什么样」的定义
# ══════════════════════════════════════════════════════════════════════════
class Hist:
    __slots__ = ("date", "symbol", "raw_symbol", "occasion", "has_body",
                 "lineno", "kind", "problem", "superseded", "bold")

    def __init__(self, **kw):
        for k in self.__slots__:
            setattr(self, k, kw.get(k))


class Entry:
    def __init__(self, num, title, src, start, end):
        self.num = num
        self.title = title
        self.src = src            # 'problems.md' / 'graduated.md'
        self.start = start        # 1-based 起始行
        self.end = end
        self.state = None
        self.ok = self.bad = self.goal = None
        self.last = None
        self.fam = None
        self.ask = None           # 状态行第 7 格「题型」原文；None ＝ 没写这一格
        self.fam_section = None   # 所在族分段
        self.review_mark = False   # 存量残留：`⚠️🔍 **REVIEW 池**`（机制已废除，check 报 ERROR）
        self.sections = {}
        self.history = []
        self.members = None       # 成员出题账原文
        self.status_raw = None
        self.status_lineno = None
        self.hist_seen = False    # 有没有 `### 历史记录` 这一节
        self.never_judged = False  # 节里写的是 `- （从未被判定过）`
        self.raw = []             # 条目全文（只用来找同组禁配声明）
        self.members_head_bad = None  # 成员出题账标题写歪了，check 要报
        self.members_misplaced = None  # 成员出题账埋进历史行里了，check 要报
        self.problems = []        # 解析期发现的格式问题 (level, msg, lineno)

    # ── 派生 ──────────────────────────────────────────────────────────
    @property
    def in_pool(self):
        return self.state == "在池"

    @property
    def graduated(self):
        return self.state == "🎓"

    @property
    def active(self):
        """会参与出题/统计的（排除 退池 / 并入）"""
        return self.state in ("在池", "🎓")

    @property
    def trigger(self):
        return self.sections.get("中文触发点", "").strip()

    @property
    def trigger_todo(self):
        return "待补" in self.trigger or not self.trigger

    @property
    def ask_kind(self):
        """题型。状态行没写这一格 ⇒ 整句（SKILL §3.1 契约②）。"""
        return self.ask or ASK_SENTENCE

    @property
    def is_phrase(self):
        """词组题：中译英词组翻译，一题可打包多个（§3.1 契约⑬）。"""
        return self.ask_kind == ASK_PHRASE

    @property
    def rule_line(self):
        """条目的一句话规则 = 标题（出题卡用）"""
        return self.title

    def created_on(self):
        return self.history[0].date if self.history else None

    def judged_days(self):
        """{date: 'ok'/'bad'/'neutral'} —— 同日只结算一次，当天有 ❌/📖 就记 ❌（§3.2）。
        被 §4.7 改判／撤销的行留痕但不参与。"""
        byday = defaultdict(list)
        for h in self.history:
            if h.superseded:
                continue
            v = JUDGE.get(h.symbol)
            if v:
                byday[h.date].append(v)
        out = {}
        for d, vs in byday.items():
            if "bad" in vs:
                out[d] = "bad"
            elif "ok" in vs:
                out[d] = "ok"
            else:
                out[d] = "neutral"
        return out

    def recount(self):
        """从历史记录重算 (连对, 连错)"""
        ok = bad = 0
        days = self.judged_days()
        for d in sorted(days):
            v = days[d]
            if v == "bad":
                bad += 1
                ok = 0
            elif v == "ok":
                ok += 1
                bad = 0
        return ok, bad

    def judged_on(self, day):
        """当天有没有【判定行】＝ §3.2 判定符号表里的那六个（✅ ◎✅ ❌ 📖 △ ◎−）。
        ⛔ 留痕符号 ③ 📋 📝 不算 —— 那几个不是读数。
        ★ 被 §4.7 改判的行（`本条已于`）仍然算 —— 那天这条确实被问过了，
          「今天已经问过」问的是出题重复，不是 streak。"""
        return any(h.date == day and h.symbol in JUDGE for h in self.history)

    def last_row_date(self):
        """「上次」的口径 = 最后一条历史记录行的日期（③建号行、📝留痕行同样算，
        因为那天这条确实被处理过）。没有历史行 ⇒ None。"""
        return max((h.date for h in self.history), default=None)

    def trigger_for_keywords(self):
        """只留真正的中文题面，去掉 ★ ⚠️ ⛔ 那些说明行 —— 否则关键词扫描全是噪音。"""
        out = []
        for l in self.trigger.splitlines():
            s = l.strip().lstrip("-").strip()
            s = re.sub(r"^20\d\d-\d\d-\d\d\s*", "", s)
            if not s or s[0] in "★⚠⛔⇒·（(":
                continue
            s = re.split(r"[★⛔⚠⇒]", s)[0]
            s = re.sub(r"（[^）]*）", "", s)
            s = re.sub(r"~~[^~]*~~", "", s)
            out.append(s)
        return "\n".join(out)

    def no_pair_with(self):
        """条目里写死的「不能和 #NNNN 同组」声明（§6 组内排布）。"""
        txt = "\n".join(self.raw)
        return set(re.findall(r"(?:不能和|不要和|别和|不许和|不可和)\s*(#\d{4})", txt))

    def occasions(self, limit=6):
        out = []
        for h in self.history:
            if h.symbol in JUDGE:
                out.append(f"{h.date[5:]} {h.symbol} {h.occasion[:24]}")
        return out[-limit:]

    # ── 召回梯子（SKILL §3.6）—— 全部**从历史记录导出**，档案里零新字段 ──────
    def eff_last(self):
        """有效上次 ＝ 最后一行 EFF_LAST_SYMBOLS 的日期（§3.6）。

        ⚠️ 与状态行的「上次」不是一个口径：那一格是「上次被**处理**过」（③ 📝 也算），
           这里问的是「上次被**测**到」。没有 ⇒ None ＝ 从未测过 ⇒ 无条件到期。"""
        out = None
        for h in self.history:
            if h.superseded or h.symbol not in EFF_LAST_SYMBOLS:
                continue
            if out is None or h.date > out:
                out = h.date
        return out

    def grad_day(self):
        """本次毕业的日子 ＝ 重放历史、连对最后一次到达 2 的那一天。
        ⛔ 回潮会把它清掉 —— 重新毕业时 rc 从 0 重算（§3.3）。"""
        ok = 0
        day = None
        days = self.judged_days()
        for d in sorted(days):
            v = days[d]
            if v == "bad":
                ok = 0
                day = None
            elif v == "ok":
                ok += 1
                if ok >= 2 and day is None:
                    day = d
        return day

    def rechecks(self):
        """rc ＝ 毕业日**之后**有「对」的**天数**（✅ ◎✅ 📋，§3.6）。

        按天数不按行数 —— §3.2 同一天同一编号只结算一次，rc 跟着同一个口径。"""
        gd = self.grad_day()
        if not gd:
            return 0
        return len({h.date for h in self.history
                    if not h.superseded and h.symbol in RECHECK_SYMBOLS and h.date > gd})

    def ever_bad(self):
        """历史里掉过 ❌／📖（全部历史；被 §4.7 改判的行不算）。"""
        return any(JUDGE.get(h.symbol) == "bad" for h in self.history if not h.superseded)

    def at_risk(self):
        """§3.6 降格口径：**未毕业 ＋ 历史里掉过 ❌／📖 ⇒ 降一格**。
        复检队列（🎓）不降格：复检只有对和不对，错了就回在池。"""
        return (not self.graduated) and self.ever_bad()

    def base_rung(self):
        """降级修正**之前**站在哪一格。返回 (是不是复检队列, 格号)。"""
        if self.graduated:
            return True, min(self.rechecks(), len(RUNGS_GRAD) - 1)
        ok, bad = ((self.ok, self.bad) if self.ok is not None and self.bad is not None
                   else self.recount())
        if ok and ok >= 1:
            return False, 2
        if bad == 1:
            return False, 1
        return False, 0

    def rung(self):
        """落到哪一格（在池条目掉过的降一格，at_risk）。返回 (是不是复检队列, 格号)。"""
        grad, r = self.base_rung()
        if self.at_risk():
            r = max(0, r - 1)
        return grad, r

    def interval(self):
        """应等几个练习日。"""
        grad, r = self.rung()
        return (RUNGS_GRAD if grad else RUNGS_POOL)[r]

    def rung_name(self):
        grad, base = self.base_rung()
        _, land = self.rung()
        names = GRAD_RUNG_NAME if grad else POOL_RUNG_NAME
        if base == land:
            return names[land]
        return f"{names[base]} ⇒ 降一格 {names[land]}"


def parse_symbol(rest):
    """从历史行日期之后切出符号。返回 (symbol, occasion, raw, bold)。

    ⛔ 不做兜底：符号必须**紧跟日期**、**不加粗**、是 §3.2 表里的那几个之一。
       加粗写法（`**◎✅**`）能认出来，但会被 check 当成格式违规报出来 —— 认出来是为了报错，
       不是为了放过。切不出符号 ⇒ (None, …) ⇒ check 报「历史行没有符号」。
    """
    raw = rest
    s = rest.strip()
    bold = False
    if s.startswith("**"):
        bold = True
        s = s[2:]
    for sym in ALL_SYMBOLS:
        if s.startswith(sym):
            occ = s[len(sym):]
            if bold:
                occ = occ.lstrip("*")
            return sym, occ.replace("　", " ").strip(), raw, bold
    return None, s.replace("　", " ").strip(), raw, bold


def parse_file(path, src):
    if not os.path.exists(path):
        return []
    lines = open(path, encoding="utf-8").read().splitlines()
    entries = []
    cur = None
    fam_section = None
    in_hist = False
    sec = None
    fence = False

    def close(idx):
        if cur is not None:
            cur.end = idx
            entries.append(cur)

    for i, raw in enumerate(lines):
        ln = i + 1
        m = RE_FAM_HEAD.match(raw)
        if m and cur is None:
            fam_section = m.group(1)
            continue
        if m and cur is not None:
            close(i)
            cur = None
            fam_section = m.group(1)
            continue

        m = RE_ENTRY.match(raw)
        if m:
            close(i)
            cur = Entry(m.group(1), m.group(2).strip(), src, ln, None)
            cur.fam_section = fam_section
            in_hist = False
            sec = None
            fence = False
            continue

        if cur is None:
            continue
        cur.raw.append(raw)

        if raw.strip().startswith("```"):
            fence = not fence

        # 状态行
        m = RE_STATUS.match(raw)
        if m and cur.state is None:
            cur.status_raw = raw
            cur.status_lineno = ln
            fields = [norm(x) for x in m.group(1).split("｜")]
            cur.state = fields[0].strip() if fields else ""
            for f in fields[1:]:
                mm = re.match(r"(连对|连错|毕业线|上次|族|题型)\s*(.*)", f)
                if not mm:
                    continue
                k, v = mm.group(1), mm.group(2).strip()
                if k == "连对":
                    cur.ok = int(v) if v.isdigit() else None
                elif k == "连错":
                    cur.bad = int(v) if v.isdigit() else None
                elif k == "毕业线":
                    cur.goal = v
                elif k == "上次":
                    cur.last = v
                elif k == "族":
                    cur.fam = v
                elif k == "题型":
                    cur.ask = v
            continue

        if "⚠️🔍" in raw and "REVIEW" in raw and not in_hist:
            cur.review_mark = True

        if RE_HIST_HEAD.match(raw):
            in_hist = True
            cur.hist_seen = True
            sec = None
            continue

        if in_hist and "从未被判定过" in raw:
            cur.never_judged = True
            continue

        # 成员出题账埋进历史行的内容块里 ⇒ pick 看不到它 ⇒ 报错，让它挪回条目正文
        if in_hist and re.match(r"^\s+\**成员出题账\**", raw):
            cur.members_misplaced = ln

        if not in_hist:
            # ⛔ 严格匹配，不做兜底：节标题必须**逐字**是 `**问题是什么**` 这种形状。
            #   写歪了 ⇒ 这一节解析不到 ⇒ check 报「缺 X 节」，当场改档案，不改脚本。
            if not fence and raw in SECTION_HEADS:
                sec = raw[2:-2]
                cur.sections.setdefault(sec, "")
                continue
            if not fence and raw == MEMBERS_HEAD:
                sec = "__members__"
                cur.members = ""
                continue
            if not fence and "成员出题账" in raw and raw.strip().startswith(("**", "📒", "成员")):
                cur.members_head_bad = raw.strip()[:40]
            if sec == "__members__":
                cur.members = (cur.members or "") + raw + "\n"
                continue
            if sec:
                cur.sections[sec] += raw + "\n"
            continue

        # 历史记录区
        m = RE_HIST_ROW.match(raw.strip())
        if m and not fence:
            sym, occ, rawrest, bold = parse_symbol(m.group(2))
            # 内容行 = 这一行之后的**第一个非空行**，必须是缩进的。
            # 中间隔一个空行是排版，不是违规；真正的违规是「压根没写内容」。
            has_body = False
            for nxt in lines[i + 1:]:
                if not nxt.strip():
                    continue
                has_body = nxt[:1] in (" ", "\t", "　")
                break
            kind = ("judge" if sym in JUDGE else
                    "trace" if sym in TRACE else
                    "legacy" if sym in LEGACY else "unknown")
            cur.history.append(Hist(date=m.group(1), symbol=sym, raw_symbol=rawrest,
                                    occasion=occ, has_body=has_body, lineno=ln,
                                    kind=kind, problem=None, bold=bold,
                                    superseded=(SUPERSEDED in raw)))
    close(len(lines))
    return entries


def load_all():
    ents = parse_file(PROBLEMS, "problems.md") + parse_file(GRADUATED, "graduated.md")
    return ents


# ══════════════════════════════════════════════════════════════════════════
#  日型（学习日 / 复习日）—— 真源 log.md
# ══════════════════════════════════════════════════════════════════════════
def day_types():
    """→ {date: 'learn'/'review'}，只收【有行为的练习日】。"""
    out = {}
    if not os.path.exists(LOG):
        return out
    for raw in open(LOG, encoding="utf-8"):
        m = RE_LOG_ROW.match(raw.strip())
        if not m:
            continue
        d, rest = m.group(1), norm(m.group(2))
        if "复习日" in rest:
            out[d] = "review"                      # 复习日优先判（"D4 复习日" 里也有 D4）
        elif "学习日" in rest or re.search(r"·\s*D\d", rest):
            out[d] = "learn"
        elif d not in out:
            pass                                   # 迁移建库 / 无练习 ⇒ 不占位
    return out


def back_count(today, types, n):
    """往回数第 n 个【有行为的练习日】—— 学习日与复习日**一视同仁**，休息日不占位次。

    ★★ 2026-09-03 她定：「**甲要做，不区别学习日和复习日**」。
       原写法只数 learn ⇒ 复习日新建／判❌ 的条目永远进不了任何一个学习日的候选池
       （实证：22 条词组条目全部建于 09-01 复习日，C5 的三个学习日一条都够不着）。
    ⛔ 旧口径「复习日不占位次」整条作废（SKILL §1 同步改）。"""
    days = sorted([d for d, t in types.items() if t in ("learn", "review") and d < today],
                  reverse=True)
    return days[n - 1] if len(days) >= n else None


# ══════════════════════════════════════════════════════════════════════════
#  drawn_review.log
# ══════════════════════════════════════════════════════════════════════════
#  组号在流水里的写法（两条队列各自编号，⛔ 不共用一个计数器）
GROUP_TAG = {"pool": "组", "grad": "复检组"}


def read_drawn(today):
    """本日流水 → (已经用掉的编号, {'pool': 已收尾组号集, 'grad': 同})

    全天计划模型（她 2026-08-23 定）：`pick` 一次把当天全部候选切成组打出来，
    所以「抽」只是**计划**，不构成排除；只有真正出过题、跑过 `used` 的才排除。
    ⇒ 中途重跑 pick，剩下的池子会重新分组，已经出过的不会再回来。
    """
    used = set()
    groups = {"pool": set(), "grad": set()}
    if not os.path.exists(DRAWN):
        return used, groups
    for raw in open(DRAWN, encoding="utf-8"):
        raw = raw.rstrip("\n")
        if not raw.strip() or raw.startswith("#"):
            continue
        parts = raw.split("\t")
        if len(parts) < 3 or parts[0] != today or parts[1] != "用":
            continue
        # ⛔ 严格匹配：`复检组N` 先判，否则 `组N` 会把它也吃掉
        q = "grad" if parts[2].startswith(GROUP_TAG["grad"]) else (
            "pool" if parts[2].startswith(GROUP_TAG["pool"]) else None)
        m = re.search(r"(\d+)\s*$", parts[2])
        if q and m:
            groups[q].add(int(m.group(1)))
        for f in parts[3:]:
            if f.startswith("用:"):
                used.update(re.findall(r"#\d{4}", f))
    return used, groups


def next_group_no(done_numbers):
    """下一组的组号 ＝ 今天已收尾组号的**最大值** ＋ 1。
    ⛔ 不是「已收尾的组数 ＋ 1」—— 中途跳号（组5 先收尾）会撞号覆盖。"""
    return (max(done_numbers) if done_numbers else 0) + 1


def append_drawn(line):
    new = not os.path.exists(DRAWN)
    with open(DRAWN, "a", encoding="utf-8") as f:
        if new:
            f.write("# 复习出题流水 —— drill.py 自动 append，一行 = 一次抽题或一次定稿\n")
            f.write("# 格式：日期 \\t 抽|用 \\t 组N \\t 字段:值 …   ⛔ 禁手工编辑\n")
        f.write(line + "\n")


# ══════════════════════════════════════════════════════════════════════════
#  lookback —— §4④「回看哪一篇」（**只读**：⛔ 不写任何文件、⛔ 不 append 任何流水）
# ══════════════════════════════════════════════════════════════════════════
#  口径（她 2026-09-03 当场裁定）：回看 ＝ **最近一篇【没被回看过】的新题**，
#  ⛔ 不再是「D-1 那天的新题」。
#  为什么改：「甲」（2026-09-03 上线，§1）把 D-1 改成「上一个**练习日**」之后，
#  只要前一天是复习日，§4④ 就自动跳过（复习日不写作文）⇒ 排成
#  「复习日 → 学习日A（写了作文）→ 复习日 → 学习日B」时，**A 那篇永远碰不到回看**。
#  实证 2026-09-03：D-1 ＝ 09-01（复习日）⇒ 旧口径直接跳过。
#  ⇒ 改成跟着「哪一篇还没回看过」走，与日期彻底脱钩。
RE_ESSAY_NO = re.compile(r"\bT[12]-\d{1,3}\b")     # 作文题号：T1-15 / T2-22
RE_SESS_NAME = re.compile(r"^(20\d\d-\d\d-\d\d)\.md$")
RE_DATE_ONLY = re.compile(r"^20\d\d-\d\d-\d\d$")


def _rel(path):
    """打印用：相对工作目录（§0.6 里全部路径都写成 `sessions/…` 这种）。"""
    try:
        r = os.path.relpath(path, ROOT)
    except ValueError:
        return path
    return path if r.startswith("..") else r


def _essay_drawn(path):
    """作文抽题流水 drawn.log → [(日期, 题号)]，按文件顺序。⛔ 只读。"""
    out = []
    if not os.path.exists(path):
        return out
    for raw in io.open(path, encoding="utf-8"):
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        parts = [p.strip() for p in raw.split("\t") if p.strip()]
        if len(parts) < 2 or not RE_DATE_ONLY.match(parts[0]):
            continue
        for q in RE_ESSAY_NO.findall(parts[1]):
            out.append((parts[0], q))
    return out


def scan_lookback(today, sess_dir=None, drawn_path=None):
    """扫 sessions/*.md ＋ drawn.log，算出「本次该回看哪一篇」。

    认法**严格**（写歪了就报出来，⛔ 不兜底 —— 与 §0.9a 的标题锚点同一条哲学）：
      · 新题   ＝ session 里 `## 新题…` 节里出现的**第一个**题号
                 （节里出现的其它题号是靶子/历史的引用，另行列出，⛔ 不当作本篇）
                 一个 session 认不到题号 ⇒ 列进「⚠️ 认不出题号」，⛔ 不静默丢掉
      · 已回看 ＝ 任意 session 里 `## 回看…` 的**标题行**上出现的题号
                 ⚠️ 标题行上没有题号的回看节 ⇒ **不算回看了任何一篇**
      · 与 drawn.log 交叉核对：流水里有、却没有任何 session 证据的题号 ⇒ 单独列出
    → dict（全部字段都是逐条清单，⛔ 不只给数量，§0.4）
    """
    sess_dir = sess_dir or os.path.join(ROOT, "sessions")
    drawn_path = drawn_path or os.path.join(ROOT, "drawn.log")
    news, unknown, noqno, warn = [], [], [], []
    reviewed = {}
    if os.path.isdir(sess_dir):
        files = sorted(os.listdir(sess_dir))
    else:
        files = []
        warn.append(f"⚠️ 找不到 sessions 目录：{_rel(sess_dir)}")
    for name in files:
        if not name.endswith(".md"):
            continue
        m = RE_SESS_NAME.match(name)
        path = os.path.join(sess_dir, name)
        if not m:
            warn.append(f"⚠️ 文件名不是 YYYY-MM-DD.md ⇒ 数不出日期，本次⛔不算它：{_rel(path)}")
            continue
        d = m.group(1)
        lines = io.open(path, encoding="utf-8").read().split("\n")
        picked = None                      # 本 session 认下来的那一篇
        others = []                        # 新题节里出现的其它题号（引用，不是本篇）
        for i, ln in enumerate(lines):
            if ln.startswith("## 新题"):
                b = _node_end(lines, i)
                for k in range(i, b):
                    for q in RE_ESSAY_NO.finditer(lines[k]):
                        if picked is None:
                            picked = {"qno": q.group(0), "date": d, "path": path,
                                      "line": k + 1, "head": ln.strip(), "others": others}
                        elif q.group(0) != picked["qno"]:
                            others.append((q.group(0), k + 1))
                if picked is None:
                    unknown.append({"date": d, "path": path, "line": i + 1,
                                    "head": ln.strip()})
            elif ln.startswith("## 回看"):
                qs = RE_ESSAY_NO.findall(ln)
                if not qs:
                    noqno.append({"date": d, "path": path, "line": i + 1,
                                  "head": ln.strip()})
                for q in qs:
                    reviewed.setdefault(q, []).append(
                        {"date": d, "path": path, "line": i + 1, "head": ln.strip()})
        if picked:
            news.append(picked)
            # 同一个 session 里认不到题号的续节（08-29 的 `## 新题 · b 收稿` 就是），
            # 归到本篇名下 ⇒ ⛔ 不重复报「认不出题号」
            unknown = [u for u in unknown if u["date"] != d]
    news.sort(key=lambda x: (x["date"], x["line"]))

    seen = {x["qno"] for x in news}
    orphan, mismatch = [], []
    by_date = {}
    for x in news:
        by_date.setdefault(x["date"], []).append(x["qno"])
    for d, q in _essay_drawn(drawn_path):
        if q not in seen:
            orphan.append((d, q))
        elif d in by_date and q not in by_date[d]:
            mismatch.append((d, q, "／".join(by_date[d])))
    ghost = [q for q in reviewed if q not in seen]

    todays = [x for x in news if x["date"] >= today]
    cand = [x for x in news if x["date"] < today and x["qno"] not in reviewed]
    return {"news": news, "reviewed": reviewed, "unknown": unknown, "noqno": noqno,
            "orphan": orphan, "mismatch": mismatch, "ghost": ghost,
            "todays": todays, "cand": cand,
            "target": cand[-1] if cand else None,
            "warn": warn, "sess_dir": sess_dir, "drawn": drawn_path}


def lookback_line(today, sess_dir=None, drawn_path=None):
    """`pick --type learn` 头部那一行 —— 与 `lookback` 是**同一个函数**算出来的。"""
    sc = scan_lookback(today, sess_dir, drawn_path)
    t = sc["target"]
    if t:
        return (f"★ §4④ 回看目标 ＝ {t['qno']}（{t['date']}）　"
                f"{_rel(t['path'])}:{t['line']}　⇒ 详情跑 `drill.py lookback`"), sc
    if not sc["news"]:
        return ("★ §4④ sessions/ 里一篇新题都认不出来 ⇒ 回看节跳过"
                "（⇒ 跑 `drill.py lookback` 看认法在哪一步断的）"), sc
    return ("★ §4④ 全部已回看 ⇒ 回看节跳过"
            "（口径 ＝ 最近一篇没被回看过的新题，⛔ 不再看 D-1）"), sc


def cmd_lookback(args):
    today = args.date or date.today().isoformat()
    sc = scan_lookback(today)
    W = "═" * 78
    print(W)
    print(f"drill.py lookback · {today} · §4④ 回看目标"
          f"　【只读：⛔ 不写任何文件、⛔ 不 append 流水】")
    print(W)
    print("  口径　回看 ＝ **最近一篇【没被回看过】的新题**（她 2026-09-03 定）")
    print("  　　　⛔ 不再是「D-1 那天的新题」—— D-1 落在复习日时那一篇永远碰不到回看")
    print("  认法　新题 ＝ `## 新题` 节里的**第一个**题号（节里别的题号是引用，另列）")
    print("  　　　已回看 ＝ 任意 session 里 `## 回看` **标题行**上的题号；"
          "⛔ 标题行没题号 ＝ 没回看任何一篇")
    print(f"  扫的　{_rel(sc['sess_dir'])}/*.md　＋　{_rel(sc['drawn'])}")
    print()

    rev = sc["reviewed"]
    print("① 全部新题（逐条列，§0.4）")
    if not sc["news"]:
        print("   （一篇都没认出来）")
    for x in sc["news"]:
        mark = "✅ 已回看" if x["qno"] in rev else "⏳ 未回看"
        tail = ""
        if x["qno"] in rev:
            tail = "　← " + "／".join(f"{_rel(r['path'])}:{r['line']}" for r in rev[x["qno"]])
        elif x["date"] >= today:
            tail = "　⚠️ 今天（或更晚）写的 ⇒ 本次⛔不作目标（§4④ 回看排在 §4⑤ 新题之前）"
        print(f"   {x['qno']:<7} {x['date']}  {_rel(x['path'])}:{x['line']}  {mark}{tail}")
        if x["others"]:
            print("           （本节还提到 "
                  + "／".join(f"{q}@{ln}" for q, ln in x["others"][:6])
                  + " —— 靶子/历史的引用，⛔ 不当作本篇）")
    print(f"   ── 共 {len(sc['news'])} 篇")
    print()

    print("② 已经回看过的（`## 回看` 标题行上带题号的才算）")
    if not rev:
        print("   （一篇都没有）")
    for q in sorted(rev, key=lambda q: rev[q][0]["date"]):
        for r in rev[q]:
            print(f"   {q:<7} ← {_rel(r['path'])}:{r['line']}　{r['head']}")
    print(f"   ── 共 {len(rev)} 篇 / {sum(len(v) for v in rev.values())} 个回看节")
    if sc["noqno"]:
        print(f"   ⚠️ 另有 {len(sc['noqno'])} 个 `## 回看` 节**标题行上没有题号** "
              f"⇒ ⛔ 不算回看了任何一篇（要算就把题号写进标题行）：")
        for r in sc["noqno"]:
            print(f"      {_rel(r['path'])}:{r['line']}　{r['head']}")
    print()

    print("③ ⇒ 本次该回看的 ＝ 最近一篇没被回看过的新题")
    t = sc["target"]
    if t:
        print(f"   ⇒ **{t['qno']}**（{t['date']}）　{_rel(t['path'])}:{t['line']}")
        if len(sc["cand"]) > 1:
            print("   　 排在它后面的（更早、也还没回看）：" + "／".join(
                f"{x['qno']}({x['date']})" for x in sc["cand"][:-1]))
        print("   ⇒ 交付件仍是 §4④ 写死的 5 件：题面与条件 · 她的原文 · 三版对照块 · "
              "最小修改版全文 · 更好版全文")
    else:
        print("   ⇒ **全部已回看 ⇒ §4④ 本节跳过**"
              "（在 session 里写明「本节跳过」＋理由，脚本认这四个字，打 SKIP）")
    print()

    bad = 0
    if sc["unknown"]:
        bad += len(sc["unknown"])
        print(f"⚠️ 认不出题号的 `## 新题` 节 {len(sc['unknown'])} 个（⛔ 没有静默丢掉）：")
        for u in sc["unknown"]:
            print(f"   {_rel(u['path'])}:{u['line']}　{u['head']}")
    if sc["orphan"]:
        bad += len(sc["orphan"])
        print(f"⚠️ drawn.log 里抽了、却没找到 session 记录的 {len(sc['orphan'])} 题：")
        for d, q in sc["orphan"]:
            print(f"   {d}  {q}")
    if sc["mismatch"]:
        bad += len(sc["mismatch"])
        print(f"⚠️ 题号与 drawn.log 对不上的 {len(sc['mismatch'])} 处：")
        for d, q, got in sc["mismatch"]:
            print(f"   {d}  drawn.log ＝ {q}　session 认到的 ＝ {got}")
    if sc["ghost"]:
        bad += len(sc["ghost"])
        print(f"⚠️ 回看了、却没有对应 `## 新题` 记录的 {len(sc['ghost'])} 题："
              + "／".join(sorted(sc["ghost"])))
    for w in sc["warn"]:
        bad += 1
        print(w)
    if not bad:
        print("⚠️ 零告警：新题／回看／drawn.log 三边对得上")
    return 0


# ══════════════════════════════════════════════════════════════════════════
#  关键词（措辞层重叠扫描，§6）
# ══════════════════════════════════════════════════════════════════════════
STOP = set("的了是在和与或也都很就还这那些个不有把被为对从到与及其中一二三四五六七八九十"
           "他她它我你们个人事物很多少大小上下前后里外因所以但而且如果这个那个题面改成原句")


def cn_keywords(text):
    text = re.sub(r"（[^）]*）", "", text)          # 去掉解释性括号
    text = re.sub(r"~~[^~]*~~", "", text)          # 去掉被划掉的旧题面
    runs = re.findall(r"[一-鿿]{2,}", text)
    out = set()
    for r in runs:
        for size in (2, 3):
            for i in range(len(r) - size + 1):
                w = r[i:i + size]
                if w not in STOP and not any(c in STOP for c in w[:1]):
                    out.add(w)
    return out


# ══════════════════════════════════════════════════════════════════════════
#  召回队列（SKILL §3.6）—— 取哪些、什么顺序，全脚本唯一一份定义
#
#  ⛔ 这一段是 learn 与 review **共用**的：两种日子不是两套取法，
#     差别只有【配额】和【有没有新题】两件事。
# ══════════════════════════════════════════════════════════════════════════
def practice_days(types=None):
    """全部【有行为的练习日】升序 —— 梯子的单位（真源 log.md，§1）。"""
    return sorted(types if types is not None else day_types())


def day_index(pdays, day):
    """day 是第几个练习日（1-based）。不在表里 ⇒ 按「排在它之后」算。"""
    return bisect.bisect_right(pdays, day)


def today_index(pdays, today):
    """今天是第几个练习日 —— **今天算一个**，哪怕 log.md 里还没写今天这一行。

    ⚠️ 只有当 `pdays` **已经含今天**时它才和 `day_index` 同一把尺；
       `plan_queues` 正是这么做的（见那里的 `pdays` 合并）。"""
    i = bisect.bisect_right(pdays, today)
    if i and pdays[i - 1] == today:
        return i
    return i + 1


def waited_days(e, pdays, tidx):
    """距有效上次过了几个练习日。从未测过 ⇒ None（＝ 无条件到期）。"""
    el = e.eff_last()
    if not el:
        return None
    return tidx - day_index(pdays, el)


def overdue(e, pdays, tidx):
    """逾期分 ＝ 距有效上次的练习日数 ÷ 应等间隔。≥1 ＝ 到期。
    从未测过 ⇒ 正无穷（排最前）。"""
    w = waited_days(e, pdays, tidx)
    if w is None:
        return float("inf")
    return w / e.interval()


def queue_key(e, pdays, tidx):
    """排序，两条队列各一套（确定性，重跑一模一样）：
      在池 ＝ 逾期分降序 → 掉过的优先 → 编号升序
      复检 ＝ 复检次数少的优先 → 已等练习日多的优先（从未测过排最前）→ 编号升序"""
    if e.graduated:
        w = waited_days(e, pdays, tidx)
        return (e.rechecks(), -(float("inf") if w is None else w), e.num)
    return (-overdue(e, pdays, tidx), 0 if e.at_risk() else 1, e.num)


def plan_queues(ents, today, types, day_type, size=GROUP_SIZE, used_ids=frozenset()):
    """把两条队列一次排完 —— **不打印、不写盘**，pick 与测试共用同一份计算。

    返回 dict：
      pdays tidx d1                 练习日表 · 今天的序号 · 上一个练习日
      pool_due grad_due             两条队列**全部到期**的条目（已排序）
      must                          必出层 ＝ D-1 那天**新建的**（她 2026-09-05 定）
      pool_take grad_take           今天实际要出的条目
      pool_groups grad_groups       切好的组
      cap base spill                配额 · 基础组 · 下溢组
      excluded                      各类被剔除的编号（报告用）
    """
    # ★★ **今天并进练习日表**（她 2026-09-05 的口径：今天算一个练习日）。
    #    ⛔ 不并的后果是两把尺：`log.md` 的今日行**收尾才写**（§4⑥）⇒ 整场 session 里
    #    今天都不在表里 ⇒ `today_index` 数到 n+1、而 `day_index(有效上次=今天)` 只数到 n
    #    ⇒ 今天刚判过的条目算成「等了 1 个练习日」⇒ 间隔 1 的档位逾期分 1.0 ＝ 到期
    #    ⇒ **同一天被重新排进后面的组**（顺带判定不进 `used`，挡不住它）。
    #    实证 2026-09-05 对抗演练：同一份 pick 输出一边报「义务已尽⛔今天不再问」、
    #    一边把那一条排进了组 1。
    pdays = sorted(set(practice_days(types)) | {today})
    tidx = day_index(pdays, today)
    d1 = back_count(today, types, 1)

    ex_fresh, ex_used, ex_dead = [], [], []
    live = []
    for e in ents:
        if e.state not in ("在池", "🎓"):
            ex_dead.append(e)
            continue
        if e.num in used_ids:
            ex_used.append(e)
        elif e.created_on() == today:
            ex_fresh.append(e)
        else:
            live.append(e)

    key = lambda e: queue_key(e, pdays, tidx)
    pool_due = sorted([e for e in live if e.in_pool and overdue(e, pdays, tidx) >= 1], key=key)
    grad_due = sorted([e for e in live if e.graduated and overdue(e, pdays, tidx) >= 1], key=key)

    # ★★ 必出层（她 2026-09-05 定）：**上一个练习日新建的条目必须全部出完，不设上限**。
    #    ⛔ 不排在队首就会被上限截掉 —— 它们只等了 1 个练习日，逾期分最高也就 1.0，
    #    在「逾期分降序」里天生排最后。这一层就是为这件事存在的。
    #    ⛔ 口径是「D-1 那天**新建的**」而不是「D-1 那天到期的」⇒ **不到期也要出**
    #    （建号当天顺带判过一次 ⇒ 逾期分 0.5 ⇒ 光看到期会把它漏掉）。
    #    ⛔ 但**今天已经测过的不再算必出** —— 义务是"出完"，不是"同一天问两遍"
    #    （顺带判定／📋 也算测过 ⇒ 口径就是「有效上次 ＝ 今天」）。
    is_must = (lambda e: bool(d1) and e.in_pool and e.created_on() == d1
               and e.eff_last() != today)
    must = sorted([e for e in live if is_must(e)], key=key)
    must_done = [e for e in live if bool(d1) and e.in_pool and e.created_on() == d1
                 and e.eff_last() == today]
    must_set = {e.num for e in must}
    rest = [e for e in pool_due if e.num not in must_set]
    ordered = must + rest

    cap, base = QUOTA[day_type]
    n_must = math.ceil(len(must) / size)
    if n_must >= cap:
        # 必出层自己就超过上限 ⇒ **只出必出层**，⛔ 不再补别的
        pool_take = must
        n_pool = n_must
    else:
        n_pool = min(cap, math.ceil(len(ordered) / size))
        pool_take = ordered[:n_pool * size]
    spill = max(0, cap - n_pool)                 # ⛔ 反向不成立：复检排不满不回补在池
    n_grad = min(base + spill, math.ceil(len(grad_due) / size))
    grad_take = grad_due[:n_grad * size]

    return dict(
        pdays=pdays, tidx=tidx, d1=d1,
        pool_due=pool_due, grad_due=grad_due, must=must, must_done=must_done,
        pool_take=pool_take, grad_take=grad_take,
        pool_groups=partition(pool_take, size, spread_by_family=True),
        grad_groups=partition(grad_take, size, spread_by_family=False),
        cap=cap, base=base, spill=spill,
        excluded=dict(fresh=ex_fresh, used=ex_used, dead=ex_dead),
    )


# ══════════════════════════════════════════════════════════════════════════
#  pick
# ══════════════════════════════════════════════════════════════════════════
def partition(cand, size, spread_by_family):
    """把要出的条目切成若干组，每组 ≤ size。

    ★★ **组间一律按传进来的顺序切**（＝ §3.6 的队列排序，必出层在最前）——
       组 1 就是今天最该测的那 10 条。她中途喊停，停在最该测的**之后**。
    ⛔ 旧写法「按族轮流发牌」整条作废：它把队列打散重排，组 1 变成"族最杂的 10 条"
       而不是"最该测的 10 条"，梯子的优先级到组一级就全丢了。
    ★ 发牌想解决的「同族不撞」降级成**组内排布**：只在组内错开相邻同族，
      跨组冲突照旧由 `pick` 的机械扫描点名、教练在**组与组之间对调**（§4①）。"""
    if not cand:
        return []
    groups = [cand[i:i + size] for i in range(0, len(cand), size)]
    if spread_by_family:
        groups = [_spread_in_group(g) for g in groups]
    return groups


def _spread_in_group(bucket):
    """组内错开相邻同族：每次从**剩得最多**的族里取一个，且尽量不与上一个同族。
    ⛔ 只动组内次序，⛔ 不跨组搬人 —— 队列的优先级不受影响。"""
    left = defaultdict(list)
    for e in bucket:
        left[e.fam].append(e)
    out, prev = [], None
    while any(left.values()):
        # ⛔ 档案漏写「族」那一格 ⇒ fam 是 None，`None < str` 会崩。
        #    这里只保证 pick 不崩（排到最后）；漏格本身由 `check` 报错（§3.1 契约）。
        fams = sorted([f for f in left if left[f]],
                      key=lambda f: (-len(left[f]), f or ""))
        pick = next((f for f in fams if f != prev), fams[0])
        out.append(left[pick].pop(0))
        prev = pick
    return out


def cmd_pick(args):
    today = args.date or date.today().isoformat()
    if args.size < 1:
        print(f"⛔ --size 要 ≥ 1，收到 {args.size}")
        return 1
    ents = load_all()
    types = day_types()
    used_ids, done = read_drawn(today)
    P = plan_queues(ents, today, types, args.type, size=args.size, used_ids=used_ids)
    scope = args.scope
    want_pool = scope in ("pool", "both")
    want_grad = scope in ("grad", "both")

    W = "═" * 78
    print(W)
    print(f"drill.py pick · {today} · "
          f"{'学习日' if args.type == 'learn' else '复习日'} · **全天计划**（§3.6 召回队列）")
    print(W)
    print(f"  练习日 {P['tidx']} 个（真源 log.md）　"
          f"上一个练习日 D-1 = {P['d1'] or '（今天之前一个练习日都没有）'}")
    print(f"  梯子 1 1 2 ┃毕业线┃ 3 7 16 32 60（单位 ＝ 练习日）　"
          f"逾期分 ＝ 等了几个练习日 ÷ 应等间隔，≥1 ＝ 到期")
    if args.type == "learn":
        print("  " + lookback_line(today)[0])
    today_type = types.get(today)
    if today_type and today_type != args.type:
        print(f"  ⚠️ log.md 里今天写的是【{'复习日' if today_type == 'review' else '学习日'}】，"
              f"你传的是 --type {args.type} —— 按 §1 先确认今天到底是哪一天")
    elif not today_type:
        print("  （log.md 里今天还没有行 —— 收尾时记得补，§4⑥）")

    ex = P["excluded"]
    if ex["fresh"]:
        print(f"  ⛔ 今天刚建的号 {len(ex['fresh'])} 条（第一条历史行 ＝ {today}）"
              f"⇒ **建号当天不回考**：")
        print(fmt_ids([e.num for e in ex["fresh"]], indent="     "))
        print("     ⇒ 当天回考考的是半小时前的记忆、不是产出；下一个练习日照常回队列")
    if ex["used"]:
        print(f"  ⛔ 本日已用 {len(ex['used'])} 条 ⇒ 不再出：")
        print(fmt_ids([e.num for e in ex["used"]], indent="     "))
    bad_grad = [e for e in ents if e.graduated and not e.grad_day()]
    if bad_grad:
        print(f"  ⚠️ {len(bad_grad)} 条 🎓 的历史重放不出「连对到 2」那一天 ⇒ rc 只能按 0 算"
              f"（间隔 {RUNGS_GRAD[0]}）—— 先跑 `check --all` 修档案：")
        print(fmt_ids([e.num for e in bad_grad], indent="     "))
    print()

    n_pool_g, n_grad_g = len(P["pool_groups"]), len(P["grad_groups"])
    print(f"  在池队列  到期 {len(P['pool_due'])} 条 ⇒ 今天出 {len(P['pool_take'])} 条 / "
          f"{n_pool_g} 组（上限 {P['cap']} 组）")
    if P["must"]:
        due_set = {e.num for e in P["pool_due"]}
        extra = [e for e in P["must"] if e.num not in due_set]
        print(f"     ★ 必出层 {len(P['must'])} 条 ＝ D-1（{P['d1']}）那天**新建的**，"
              f"⛔ 不受上限约束、⛔ 不许挪到明天：")
        print(fmt_ids([e.num for e in P["must"]], indent="        "))
        if extra:
            print(f"        ⇒ 其中 {len(extra)} 条按逾期分还没到期，**照样出**（必出层不看到期）："
                  + " ".join(e.num for e in extra))
        if P["must_done"]:
            print(f"        ⇒ 另有 {len(P['must_done'])} 条 D-1 新建的**今天已经测过**"
                  f"（有效上次 ＝ 今天）⇒ 义务已尽，⛔ 今天不再问："
                  + " ".join(e.num for e in P["must_done"]))
        if math.ceil(len(P["must"]) / args.size) >= P["cap"]:
            print(f"        ⇒ 必出层自己就占满／超过 {P['cap']} 组 ⇒ **今天只出必出层**，"
                  f"⛔ 不再补别的（下溢 0）")
    print(f"  复检队列  到期 {len(P['grad_due'])} 条 ⇒ 今天出 {len(P['grad_take'])} 条 / "
          f"{n_grad_g} 组（基础 {P['base']} 组 ＋ 在池下溢 {P['spill']} 组）")
    if P["grad_due"] and not P["grad_take"]:
        print("     ⚠️ 复检到期却一组都没排上 —— 检查配额是不是被必出层吃光了")
    print(f"  ★ 组 1 就是今天最该测的 {args.size} 条（组间按队列顺序切）；"
          f"她中途喊停 ⇒ 停在最该测的之后，⛔ 不记欠账")
    n_phrase = sum(1 for e in P["pool_take"] + P["grad_take"] if e.is_phrase)
    if n_phrase:
        print(f"  ★ 今天要出的里有 **{n_phrase} 条词组型** —— 混在组里照常发牌（组的大小不因此调整），"
              f"出题时可把同组的几条并成一道词组题（§6.1）")
    if not args.full:
        print("  ★ 卡片是精简版；要历史留痕/全部旧触发点/成员账全文 ⇒ 加 --full，或 `show #NNNN`")
    if args.date:
        print("  ⚠️ --date 只影响「今天」的口径，⛔ 不能用来忠实回放当天的分组")
    print()

    def card(e, tag):
        w = waited_days(e, P["pdays"], P["tidx"])
        od = overdue(e, P["pdays"], P["tidx"])
        must = e in P["must"]
        hint = ("⛔零提示（词组题给词 ＝ 给答案）" if e.is_phrase
                else "★默认零提示；有特别想考的就把它写进题面（§6）")
        print(f"{tag} {e.num}  {e.fam}  {e.ok}/{e.bad}  "
              f"档位 {e.rung_name()}（应等 {e.interval()}）  "
              f"有效上次 {(e.eff_last() or '从未测过')[5:] if e.eff_last() else '从未测过'}"
              f"  等了 {'—' if w is None else w}  逾期分 {'∞' if od == float('inf') else f'{od:.1f}'}"
              + ("  ★必出（D-1 新建）" if must else ""))
        print(f"     考点 {e.title}")
        if e.is_phrase:
            print("     题型 **词组** —— 中译英词组题：中文块 → 英文块，⛔ 不出整句、⛔ 零提示")
            print("          本组别的词组条目可以并进同一道题（§6.1 词组题）")
        print(f"     提示 {hint}")
        tp = [l.strip() for l in e.trigger.splitlines() if l.strip()]
        if e.trigger_todo:
            print("     题面 ⚠️ 待补 —— 出题前必须当场写成完整中文句（§3.1 B4）")
            for l in tp[:2]:
                print(f"          {l[:100]}")
        elif args.full:
            print("     题面（全文，含历次改写留痕 —— §6 不许重复用老触发点）")
            for l in tp:
                print(f"          {l}")
        else:
            for i, l in enumerate(tp[:3]):
                print(f"     {'题面' if i == 0 else '    '} {l[:100]}"
                      + ("…" if len(l) > 100 else ""))
            if len(tp) > 3:
                print(f"          （还有 {len(tp) - 3} 行旧触发点留痕，--full 看）")
        if e.members:
            todo_m = [l.strip() for l in e.members.splitlines() if "未出过" in l]
            if args.full:
                print("     成员出题账（§3.5 第3.5步：一题 ≥2 个成员）")
                for l in e.members.splitlines():
                    if l.strip() and not l.strip().startswith("```"):
                        print(f"          {l.strip()}")
            elif todo_m:
                print(f"     成员 ★未出过 {len(todo_m)} 个：" +
                      " ／ ".join(x.split("——")[0].split("  ")[0].strip() for x in todo_m[:4]))
        if args.full:
            occ = e.occasions()
            if occ:
                print("     历次 " + " ｜ ".join(occ))
            print(f"     正文 {e.src}:{e.start}")

    def scan(bucket):
        fam_g = defaultdict(list)
        for e in bucket:
            fam_g[e.fam].append(e.num)
        msgs = []
        for k, v in sorted(fam_g.items(), key=lambda kv: kv[0] or ""):
            if len(v) > 1:
                msgs.append(f"⚠️ 同族 {k}：{' '.join(v)}")
        kw = {e.num: cn_keywords(e.trigger_for_keywords()) for e in bucket}
        nums = [e.num for e in bucket]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sh = {w for w in kw[nums[i]] & kw[nums[j]] if len(w) >= 2}
                if sh:
                    msgs.append(f"⚠️ 措辞 {nums[i]} ⇔ {nums[j]} 共享「{'／'.join(sorted(sh)[:4])}」")
        pset = {e.num for e in bucket}
        for e in bucket:
            for other in e.no_pair_with() & pset:
                msgs.append(f"⛔ 禁配 {e.num} 正文写死「不能和 {other} 同组」—— 必须换组")
        todo = [e.num for e in bucket if e.trigger_todo]
        if todo:
            msgs.append(f"⚠️ 待补 {' '.join(todo)}")
        ph = [e.num for e in bucket if e.is_phrase]
        if ph:
            msgs.append(f"★ 词组型 {len(ph)} 条：{' '.join(ph)} —— 可并成一道词组题（§6.1）")
        if msgs:
            print("     ── 本组机械扫描 ──")
            for m in msgs:
                print("     " + m)
        else:
            print("     ── 本组机械扫描：同族／措辞／禁配／待补 全部零命中 ──")

    shown = []
    if want_pool:
        for gi, bucket in enumerate(P["pool_groups"], start=next_group_no(done["pool"])):
            shown.append(("pool", gi, bucket))
    if want_grad:
        for gi, bucket in enumerate(P["grad_groups"], start=next_group_no(done["grad"])):
            shown.append(("grad", gi, bucket))
    if args.groups:
        keep_p = [x for x in shown if x[0] == "pool"][:args.groups]
        keep_g = [x for x in shown if x[0] == "grad"][:args.groups]
        shown = keep_p + keep_g

    for q, gi, bucket in shown:
        label = "在池组" if q == "pool" else "复检组"
        print("━" * 78)
        print(f"━━━ {label} {gi}（{len(bucket)} 条）"
              + ("　判两档：稳 ✅ ／ 掉 ❌；✅ 只记一行判定，❌ 才走三版对照块（§4③e）"
                 if q == "grad" else ""))
        print("━" * 78)
        for e in bucket:
            card(e, " ")
        scan(bucket)
        print()

    print("─" * 78)
    print("⛔ 脚本做不到、必须手工的两件：语言事实核查 · 中文题面自译落点（§6）")
    print("★ 冲突要挪题 ⇒ 在**组与组之间对调**，⛔ 不用重抽 —— 全天的池子已经在上面了")
    if args.dry:
        print("（--dry：没有写 drawn_review.log）")
    else:
        for q, gi, bucket in shown:
            append_drawn(f"{today}\t抽\t{GROUP_TAG[q]}{gi}\t正选:"
                         + ",".join(e.num for e in bucket))
        print(f"已记流水：{today} 共 {len(shown)} 组")
    print("每组定稿后跑：python3 writing-band7/drill2/drill.py used --queue pool|grad "
          "--group N --used \"#a,#b,…\" [--dropped \"#c=理由\"]")
    return 0


def cmd_used(args):
    today = args.date or date.today().isoformat()
    used = re.findall(r"#\d{4}", args.used or "")
    fields = [f"用:{','.join(used)}"]
    if args.dropped:
        fields.append(f"弃:{args.dropped}")
    tag = f"{GROUP_TAG[args.queue]}{args.group}"
    append_drawn(f"{today}\t用\t{tag}\t" + "\t".join(fields))
    print(f"已记流水：{today} {tag} 用 {len(used)} 条"
          + (f"，弃 {args.dropped}" if args.dropped else ""))
    drop_ids = re.findall(r"#\d{4}", args.dropped or "")
    if drop_ids:
        print(f"⇒ {' '.join(drop_ids)} 已退回候选池，下一组 pick 会重新抽到")
    return 0


# ══════════════════════════════════════════════════════════════════════════
#  list / show / dedup —— 建号前的查重三件套（SKILL §3.5 第 1 步）
# ══════════════════════════════════════════════════════════════════════════
#  字段权重：越靠近「规则本身」的字段，命中越算数
FIELD_W = {
    "标题": 3,
    "我错在哪": 3,
    "问题是什么": 2,
    "成员出题账": 2,
    "中文触发点": 1,
    "历史记录": 1,
}


def entry_fields(e, use_history=True):
    f = {
        "标题": e.title,
        "问题是什么": e.sections.get("问题是什么", ""),
        "我错在哪": e.sections.get("我错在哪", ""),
        "中文触发点": e.sections.get("中文触发点", ""),
        "成员出题账": e.members or "",
    }
    if use_history:
        f["历史记录"] = "\n".join(h.raw_symbol or "" for h in e.history) + "\n" + \
                        "\n".join(e.raw[-200:])
    return f


#  「规则字段」＝ 讲规则本身的那几节。§3.5 的三问判的是规则，所以先按规则字段排，
#  历史记录只当次要信号 —— 否则条目一长（#0126 两万五千字）就把所有查询都吃掉。
RULE_FIELDS = ("标题", "问题是什么", "我错在哪", "成员出题账")


def score_entry(e, terms, use_history=True, skip_lines=None):
    """→ (命中的 term 数, 加权分, {term: 命中的最高权字段})"""
    fields = entry_fields(e, use_history)
    if skip_lines:                                   # 测试用：屏蔽某几行（模拟"这条记录还不存在"）
        keep = [l for i, l in enumerate(e.raw, start=e.start) if i not in skip_lines]
        fields["历史记录"] = "\n".join(keep) if use_history else ""
    hits, total = {}, 0
    for t in terms:
        best, bw = None, 0
        tl = t.lower()
        # 纯英文的查询词按**词边界**匹配 —— 否则 `as` 会命中 cases、`weigh` 会命中 outweigh，
        # 结果全是噪音。中文没有词边界，仍按子串。
        ascii_term = re.fullmatch(r"[A-Za-z][A-Za-z'\- ]*", t) is not None
        pat = re.compile(r"(?<![A-Za-z])" + re.escape(tl) + r"(?![A-Za-z])") if ascii_term else None
        for name, txt in fields.items():
            if not txt:
                continue
            low = txt.lower()
            ok = pat.search(low) if pat else (tl in low)
            if ok:
                w = FIELD_W.get(name, 1)
                if w > bw:
                    best, bw = name, w
        if best:
            hits[t] = best
            total += bw
    return len(hits), total, hits


def sort_key(n, sc, hits, e):
    """先看有几个词打在【规则字段】上，再看总共命中几个词，再看权重。
    ⇒ 一条 25000 字的条目不会因为历史记录里碰巧出现过某个词就排到前面。"""
    rule_hits = sum(1 for f in hits.values() if f in RULE_FIELDS)
    return (-rule_hits, -n, -sc, e.num)


def rank(ents, terms, fam=None, use_history=True, limit=12, states=("在池", "🎓"),
         exclude=()):
    out = []
    for e in ents:
        if e.num in exclude:
            continue
        if fam and e.fam != fam:
            continue
        if states and e.state not in states:
            continue
        n, sc, hits = score_entry(e, terms, use_history)
        if n:
            out.append((n, sc, e, hits))
    out.sort(key=lambda t: sort_key(t[0], t[1], t[3], t[2]))
    return out[:limit]


def cmd_list(args):
    ents = load_all()
    sel = [e for e in ents
           if (not args.fam or e.fam == args.fam)
           and (not args.pool or e.in_pool)
           and (not args.state or e.state == args.state)]
    sel.sort(key=lambda e: (e.fam or "", e.num))
    print("═" * 78)
    print(f"drill.py list · {len(sel)} 条"
          + (f" · 族 {args.fam}" if args.fam else "")
          + (" · 只看在池" if args.pool else "")
          + "　（非 detail；要看正文用 `show #NNNN`）")
    print("═" * 78)
    fam = None
    for e in sel:
        if e.fam != fam:
            fam = e.fam
            print(f"\n── {fam} ──")
        star = " "
        st = {"在池": "在池", "🎓": "🎓 ", "退池": "退池"}.get(e.state, "并入")
        print(f"{e.num} {st}{star}{e.ok}/{e.bad} {(e.last or '—')[5:]:>5}  {e.title}")
    print()
    print(f"⇒ 共 {len(sel)} 条。建号前必须先跑 `dedup`（§3.5 第 1 步），"
          "不许只凭印象说「查过了」。")
    return 0


def cmd_show(args):
    ents = {e.num: e for e in load_all()}
    for n in args.nums:
        n = n if n.startswith("#") else "#" + n
        e = ents.get(n)
        if not e:
            print(f"⛔ 没有 {n}")
            continue
        print("═" * 78)
        print(f"{e.src}:{e.start}-{e.end}")
        print("═" * 78)
        print("\n".join([f"## {e.num} {e.title}"] + e.raw).rstrip())
        print()
    return 0


def cmd_dedup(args):
    ents = load_all()
    terms = args.terms
    excl = {n if n.startswith("#") else "#" + n for n in (args.exclude or [])}
    hits = rank(ents, terms, fam=args.fam, use_history=not args.no_history,
                limit=args.limit, exclude=excl)
    print("═" * 78)
    print(f"drill.py dedup · 查 {len(terms)} 个词：{' / '.join(terms)}"
          + (f" · 限定族 {args.fam}" if args.fam else " · 全档（跨族）")
          + (f" · 已排除 {' '.join(sorted(excl))}" if excl else ""))
    print("═" * 78)
    if not hits:
        print("零命中。")
        print("⇒ §3.5 第 1 步的 grep 这一关过了，但**三问还得自己过**（B0 闸要写出理由）。")
        return 0
    for n, sc, e, h in hits:
        mark = "★" if n == len(terms) else " "
        print(f"{mark} {e.num}  {e.fam}  {e.state}  命中 {n}/{len(terms)} 词 · 权重 {sc}")
        print(f"    {e.title}")
        for t, field in h.items():
            print(f"    · 「{t}」命中于 {field}")
        print(f"    正文 {e.src}:{e.start}　⇒ `python3 writing-band7/drill2/drill.py show {e.num}`")
    print("─" * 78)
    print("⇒ ★ = 所有词都命中，**必须打开正文逐条过 §3.5 1.2 的三问**，不许跳过。")
    print("⇒ 命中不等于同一条；零命中也不等于可以直接建号 —— 判据永远是三问，不是 grep。")
    return 0


# ══════════════════════════════════════════════════════════════════════════
#  stats
# ══════════════════════════════════════════════════════════════════════════
def fmt_ids(ids, per=14, indent="        "):
    ids = sorted(ids)
    out = []
    for i in range(0, len(ids), per):
        out.append(indent + " ".join(ids[i:i + per]))
    return "\n".join(out)


# ══════════════════════════════════════════════════════════════════════════
#  count —— 按【类型】数条目（SKILL §0.4：全档级的数一律由脚本产出）
#  类型的定义（口径 + 认哪个锚点）写死在 SKILL §3.1 契约⑫，改这里必须同步改那里。
# ══════════════════════════════════════════════════════════════════════════
def _first_symbol(e):
    return e.history[0].symbol if e.history else None


TYPES = [
    # slug             中文名          口径（认哪个锚点）                                  predicate
    ("pool",       "在池",        "状态行第 1 格 ＝ 在池",                        lambda e: e.in_pool),
    ("grad",       "🎓 毕业",      "状态行第 1 格 ＝ 🎓",                          lambda e: e.graduated),
    ("retired",    "退池",        "状态行第 1 格 ＝ 退池",                        lambda e: e.state == "退池"),
    ("merged",     "并入",        "状态行第 1 格 ＝ 并入 #NNNN",                  lambda e: bool(e.state) and e.state.startswith("并入")),
    ("ask-sentence", "题型·整句",   "状态行「题型」＝ 整句（**不写这一格就是它**）",   lambda e: e.ask_kind == ASK_SENTENCE),
    ("ask-phrase",   "题型·词组",   "状态行「题型」＝ 词组（§3.1 契约⑬）",           lambda e: e.ask_kind == ASK_PHRASE),
    ("ask-retired",  "题型·已取消",  "状态行「题型」＝ 作文验（机制已取消 ⇒ **应为 0**）", lambda e: e.ask in ASK_RETIRED),
    ("pickable",   "可出题",      "在池 ＋ 题面不待补",                            lambda e: e.in_pool and not e.trigger_todo),
    ("trigger-todo", "题面待补",   "在池 ＋ 中文触发点为空或含「待补」",             lambda e: e.in_pool and e.trigger_todo),
    ("review-left", "REVIEW 残留", "状态行下还留着 `⚠️🔍 **REVIEW 池**`（机制已废除）", lambda e: e.review_mark),
    ("wordlist",   "词表型",      "正文挂着 `**成员出题账**`（§3.5 第3.5步）",       lambda e: bool(e.members)),
    ("nopair",     "有禁配声明",   "正文写着「不能和 #NNNN」（§6 组内排布）",         lambda e: bool(e.no_pair_with())),
    ("streak0",    "在池·连对 0",  "在池 ＋ 连对 0",                               lambda e: e.in_pool and e.ok == 0),
    ("streak1",    "在池·连对 1",  "在池 ＋ 连对 1",                               lambda e: e.in_pool and e.ok == 1),
    ("streak2+",   "在池·连对 ≥2", "在池 ＋ 连对 ≥2 ⚠️ 到线未毕业，该改 🎓",        lambda e: e.in_pool and e.ok is not None and e.ok >= 2),
    ("by-error",   "建号·她犯错",  "历史记录第一行符号 ＝ ❌（§2①）",               lambda e: _first_symbol(e) == "❌"),
    ("by-request", "建号·她点名",  "历史记录第一行符号 ＝ ③（§2③）",               lambda e: _first_symbol(e) == "③"),
    ("migrated",   "旧档案迁移",   "第一条历史行日期 < 2026-08-19",                lambda e: bool(e.created_on()) and e.created_on() < "2026-08-19"),
    ("never",      "占位·从未判定", "历史记录里写着「（从未被判定过）」",             lambda e: e.never_judged),
    ("untested",   "建了号没测过",  "历史行里一条 §3.2 判定符号都没有（③📋📝 不算读数）",
     lambda e: not any(h.symbol in JUDGE for h in e.history)),
    ("in-problems", "住 problems.md", "解析时的来源文件",                          lambda e: e.src == "problems.md"),
    ("in-graduated", "住 graduated.md", "解析时的来源文件",                        lambda e: e.src == "graduated.md"),
]
TYPE_MAP = {t[0]: t for t in TYPES}


def cmd_count(args):
    ents = load_all()
    total = len(ents)

    if args.type and args.type.startswith("fam:"):
        fam = args.type[4:].upper()
        slug, label, rule = args.type, f"族 {fam}", "状态行最后一格 ＝ 族 FNN"
        sel = [e for e in ents if e.fam == fam]
    elif args.type:
        if args.type not in TYPE_MAP:
            print(f"⛔ 没有这个类型：{args.type}")
            print("   可用类型：" + " ".join(t[0] for t in TYPES) + " fam:FNN")
            return 1
        slug, label, rule, pred = TYPE_MAP[args.type]
        sel = [e for e in ents if pred(e)]
    else:
        slug = None

    print("═" * 78)
    if slug is None:
        print(f"drill.py count · 全档 {total} 条 · 按类型逐类实数（SKILL §3.1 契约⑫）")
        print("═" * 78)
        print(f"{'类型':<14}{'全档':>5}{'在池':>6}   口径（认哪个锚点）")
        print("─" * 78)
        for s, label, rule, pred in TYPES:
            n = sum(1 for e in ents if pred(e))
            npool = sum(1 for e in ents if pred(e) and e.in_pool)
            flag = (f"  ⛔ 要修" if npool else ("  （都出池了，不影响 pick）" if n else "")) \
                if s in ("essay-bad", "streak2+") else ""
            print(f"{s:<14}{n:>5}{npool:>6}   {label} —— {rule}{flag}")
        print("─" * 78)
        fams = Counter(e.fam for e in ents if e.fam)
        print("fam:FNN       " + "  ".join(f"{f}={fams[f]}" for f in sorted(fams)))
        print("─" * 78)
        st = sum(1 for e in ents if e.in_pool or e.graduated or e.state == "退池"
                 or (e.state or "").startswith("并入"))
        print(f"✔ 状态四类相加 {st} ＝ 全档总数 {total}" if st == total
              else f"⚠️ 状态四类相加 {st} ≠ 全档总数 {total} —— 有条目的状态没解析出来")
        print()
        print("⇒ 要某一类的编号清单：`drill.py count --type <类型>`")
        print("⇒ 再要逐条详情　　　：`drill.py count --type <类型> --detail`")
        print("⇒ 要正文全文　　　　：`drill.py show #NNNN`")
        print("═" * 78)
        return 0

    npool = sum(1 for e in sel if e.in_pool)
    print(f"drill.py count --type {slug} · **全档 {len(sel)} 条**（其中**在池 {npool} 条**）/ 全档总数 {total}")
    print(f"口径：{label} —— {rule}")
    print("★ 报这个数时必须写清是【全档】还是【在池】口径 —— 两个数不一样（SKILL §0.4）")
    print("═" * 78)
    sel.sort(key=lambda e: (e.fam or "", e.num))
    if not sel:
        print("（零条）")
    elif args.detail:
        fam = None
        for e in sel:
            if e.fam != fam:
                fam = e.fam
                print(f"\n── {fam} ──")
            star = " "
            st = {"在池": "在池", "🎓": "🎓 ", "退池": "退池"}.get(e.state, "并入")
            print(f"{e.num} {st}{star}{e.ok}/{e.bad} {(e.last or '—')[5:]:>5} "
                  f"{e.src[0]}  {e.title}")
    else:
        print(fmt_ids([e.num for e in sel], indent="  "))
    print("═" * 78)
    print(f"⇒ {len(sel)} 条。逐条详情加 --detail；正文用 `show #NNNN`")
    return 0


def cmd_stats(args):
    ents = load_all()
    total = len(ents)
    by_state = Counter(e.state for e in ents)
    in_pool = [e for e in ents if e.in_pool]
    grad = [e for e in ents if e.graduated]
    merged = [e for e in ents if e.state and e.state.startswith("并入")]
    retired = [e for e in ents if e.state == "退池"]
    ok1 = [e for e in in_pool if e.ok == 1]
    ok0 = [e for e in in_pool if e.ok == 0]
    okx = [e for e in in_pool if e.ok not in (0, 1)]
    todo = [e for e in ents if e.in_pool and e.trigger_todo]
    review = [e for e in ents if e.review_mark]      # 存量残留，正常应为 0
    grad_in_problems = [e for e in grad if e.src == "problems.md"]
    relapsed_in_grad = [e for e in ents if e.src == "graduated.md" and e.state != "🎓"]

    print("═" * 74)
    print("drill.py stats · 全档 = problems.md ＋ graduated.md（两文件合计逐条实数）")
    print("═" * 74)
    print(f"全档总数   {total} 条　＝ problems.md {sum(1 for e in ents if e.src=='problems.md')}"
          f" ＋ graduated.md {sum(1 for e in ents if e.src=='graduated.md')}")
    print(f"在池       {len(in_pool)} 条")
    print(f"🎓         {len(grad)} 条（占 {len(grad)/max(total,1)*100:.1f}%）")
    if grad_in_problems:
        print(f"   ⏸ 其中 {len(grad_in_problems)} 条还留在 problems.md —— "
              f"**跑 `drill.py migrate` 把它们搬进 graduated.md**（§3.3 / §4⑥）")
        print(fmt_ids([e.num for e in grad_in_problems]))
    print(f"退池       {len(retired)} 条　并入 {len(merged)} 条")
    if relapsed_in_grad:
        print(f"   ⏸ graduated.md 里有 {len(relapsed_in_grad)} 条已经不是 🎓（🎓 后复发）—— "
              f"**跑 `drill.py migrate` 把它们搬回 problems.md**（§3.3 / §4⑥）")
        print(fmt_ids([e.num for e in relapsed_in_grad]))
    if review:
        print(f"⛔ REVIEW 残留 {len(review)} 条 —— REVIEW 池机制 2026-09-05 已废除，"
              f"这几条的 `⚠️🔍 **REVIEW 池**` 标记该删（§3.3）")
        print(fmt_ids([e.num for e in review]))
    print()
    print(f"在池 · 连对 1   {len(ok1)} 条")
    if not args.brief:
        print(fmt_ids([e.num for e in ok1]))
    print(f"在池 · 连对 0   {len(ok0)} 条")
    if not args.brief:
        print(fmt_ids([e.num for e in ok0]))
    if okx:
        print(f"在池 · 连对 ≥2  {len(okx)} 条 ⚠️ 到线未毕业，按 §3.3 该改 🎓")
        print(fmt_ids([e.num for e in okx]))
    print(f"题面待补        {len(todo)} 条（口径＝在池 ＋ 中文触发点标「待补」）")
    print()
    print("题型（§3.1 契约②第 7 格 · 状态行不写这一格 ＝ 整句）")
    for a in ASKS:
        n_all = sum(1 for e in ents if e.ask_kind == a)
        n_pool = sum(1 for e in in_pool if e.ask_kind == a)
        expl = sum(1 for e in ents if e.ask == a)
        print(f"  {a:<4}  全档 {n_all:>3} 条 ｜ 在池 {n_pool:>3} 条"
              f"　（其中状态行显式写出的 {expl} 条）")
    if not args.brief:
        print(fmt_ids([e.num for e in todo]))
    print()
    # streak 重算
    bad = []
    for e in ents:
        if not e.active or e.ok is None:
            continue
        ro, rb = e.recount()
        if (ro, rb) != (e.ok, e.bad):
            bad.append((e, ro, rb))
    print(f"状态行 vs 历史重数  参与 {sum(1 for e in ents if e.active and e.ok is not None)} 条"
          f" · 不符 {len(bad)} 条")
    for e, ro, rb in bad:
        print(f"   ⚠️ {e.num} {e.src}:{e.status_lineno}  档 {e.ok}/{e.bad} vs 重数 {ro}/{rb}")
    # 上次
    lastbad = []
    for e in ents:
        if not e.active:
            continue
        lj = e.last_row_date()
        want = lj or "—"
        if (e.last or "").strip() != want:
            lastbad.append((e, want))
    print(f"上次 vs 最后判定行  不符 {len(lastbad)} 条")
    for e, want in lastbad[:20]:
        print(f"   ⚠️ {e.num} {e.src}:{e.status_lineno}  档「{e.last}」 vs 应为「{want}」")
    if len(lastbad) > 20:
        print(f"   … 另 {len(lastbad)-20} 条")
    print("═" * 74)
    return 0


# ══════════════════════════════════════════════════════════════════════════
#  check
# ══════════════════════════════════════════════════════════════════════════
def changed_entries(ents):
    """用 git diff 找出本次改动落在哪些条目、哪些行上（零新增状态文件）。
    → (改动的编号集合, 改动的行号集合 {(src, lineno)})"""
    touched, touched_lines = set(), set()
    for path, src in ((PROBLEMS, "problems.md"), (GRADUATED, "graduated.md")):
        if not os.path.exists(path):
            continue
        try:
            out = subprocess.run(["git", "diff", "-U0", "HEAD", "--", path],
                                 cwd=ROOT, capture_output=True, text=True, timeout=30).stdout
        except Exception:
            continue
        lines = []
        for h in re.finditer(r"^@@ -\S+ \+(\d+)(?:,(\d+))? @@", out, re.M):
            start = int(h.group(1))
            cnt = int(h.group(2) or 1)
            lines.extend(range(start, start + max(cnt, 1)))
        touched_lines.update((src, l) for l in lines)
        for e in ents:
            if e.src != src:
                continue
            if any(e.start <= l <= (e.end or 10 ** 9) for l in lines):
                touched.add(e.num)
    return touched, touched_lines


def check_entry(e, touched_lines=None, all_nums=None):
    """→ [(level, msg)]  level ∈ ERROR/WARN/INFO
    历史行的硬查口径：**本次 diff 里新写的行**，或日期 ≥ STRICT_FROM 的行。
    更早的存量行按当时的规矩留痕，只提示不报错。"""
    touched_lines = touched_lines or set()
    P = []
    if not e.state:
        P.append(("ERROR", "缺状态行"))
        return P
    if e.state not in ("在池", "🎓", "退池") and not e.state.startswith("并入 #"):
        P.append(("ERROR", f"状态值非法「{e.state}」，只许 在池／🎓／退池／并入 #NNNN"))
    if e.state.startswith("并入"):
        tgt = re.search(r"#\d{4}", e.state)
        if not tgt:
            P.append(("ERROR", "并入状态没写目标编号（写法：并入 #NNNN）"))
        elif all_nums is not None and tgt.group(0) not in all_nums:
            P.append(("ERROR", f"并入的目标 {tgt.group(0)} 全档不存在"))
        return P
    if e.state == "退池":
        return P                                   # 退池 不再查其余字段
    # ★★ REVIEW 池机制 2026-09-05 废除（她定：「就移除待 review，就是正常毕业，
    #    等新增的毕业照召回，统一」）⇒ 靠 ◎✅ 凑线的和别的 🎓 一样进复检队列（§3.6）。
    #    残留的标记会让人以为这条"不出题"，⛔ 一律报错，把存档题面搬进「中文触发点」后删掉。
    if e.review_mark:
        P.append(("ERROR", "状态行下还留着 `⚠️🔍 **REVIEW 池**` —— 该机制 2026-09-05 已废除；"
                           "把存档新题面搬进「中文触发点」，再把这一行删掉（§3.3）"))
    if e.members_head_bad:
        P.append(("ERROR",
                  f"成员出题账标题写成「{e.members_head_bad}」—— 必须逐字是 `**成员出题账**`"))
    if e.members_misplaced:
        P.append(("ERROR",
                  f"L{e.members_misplaced} 成员出题账埋在历史行的内容块里 —— "
                  f"必须挂在条目正文（`### 历史记录` 之前），否则 pick 看不到"))
    for k, v in (("连对", e.ok), ("连错", e.bad)):
        if v is None:
            P.append(("ERROR", f"状态行缺 {k} 或不是数字"))
    if e.goal != "2":
        P.append(("ERROR", f"毕业线写成「{e.goal}」—— §3.3 全档一律 2"))
    if e.fam not in FAMILIES:
        P.append(("ERROR", f"族「{e.fam}」不在 F01–F18（F13/F16 不存在）"))
    elif e.fam_section and e.fam_section != e.fam:
        P.append(("ERROR", f"条目在 {e.fam_section} 分段里，状态行却写 {e.fam}"))

    # ── 题型（契约②第 7 格 ＋ 契约⑬）──────────────────────────────────
    created = e.created_on()
    if e.ask is not None and e.ask not in ASKS:
        P.append(("ERROR",
                  f"题型「{e.ask}」非法 —— 只许 {' ／ '.join(ASKS)}（§3.1 契约②）"))
    elif e.ask is None and created and created >= ASK_FROM:
        P.append(("ERROR",
                  f"状态行缺「题型」格 —— {ASK_FROM} 起新建的条目必须自己写出题型"
                  f"（§3.1 契约② · 判型走 §3.5 第 2.5 步）"))
    if e.ask_kind == ASK_PHRASE:
        if e.members:
            P.append(("ERROR",
                      "挂着「成员出题账」的是**词表型**，考的是挑得对不对 ⇒ ⛔ 不许标词组，"
                      "走整句（§3.5 第3.5步）"))
        if e.fam in NO_PHRASE_FAMS:
            P.append(("ERROR",
                      f"族 {e.fam} 是句子层的族（动词形态论元／数／句法／丢层／篇章／整句仿写）"
                      f"⇒ ⛔ 不许标词组（§3.1 契约⑬）"))
        if "。" in e.trigger:
            P.append(("WARN",
                      "题型是词组，中文触发点里却有句号 —— 词组题的题面是**块**不是句"))
    if e.ask in ASK_RETIRED:
        P.append(("ERROR",
                  f"题型「{e.ask}」已取消 —— 这一类考点只在判作文时指出来、⛔ 不建号；"
                  f"这条要么改成 整句／词组 出题，要么状态改 退池（§2④）"))
    for s in SECTIONS:
        if s not in e.sections:
            P.append(("ERROR", f"缺「{s}」节"))
    if "中文触发点" in e.sections and not e.trigger:
        P.append(("ERROR", "「中文触发点」节是空的"))
    if e.trigger_todo and e.state == "在池":
        P.append(("WARN", "触发点标着「待补」—— 抽到它就必须当场补成完整中文句"))
    if not e.hist_seen:
        P.append(("ERROR", "缺「### 历史记录」节"))
    elif not e.history and not e.never_judged:
        P.append(("ERROR", "历史记录节是空的（从未被判定过的写 `- （从未被判定过）`）"))
    elif e.history and e.never_judged:
        P.append(("ERROR",
                  f"已有 {len(e.history)} 条历史行，却还留着 `- （从未被判定过）` —— "
                  f"第一次判定时必须把那一行顶掉"))
    for h in e.history:
        hard = (e.src, h.lineno) in touched_lines or h.date >= STRICT_FROM
        loc = f"L{h.lineno}"
        if h.symbol is None:
            P.append((("ERROR" if hard else "INFO"), f"{loc} 历史行没有符号：{h.raw_symbol[:30]}"))
        elif h.kind == "legacy":
            P.append((("ERROR" if hard else "INFO"),
                      f"{loc} 光杆 ◎ —— §3.2 起必须写成 ◎✅ 或 ◎−"))
        if h.bold:
            P.append((("ERROR" if hard else "INFO"),
                      f"{loc} 符号加粗了（`**{h.symbol}**`）—— §3.2 符号紧跟日期、不加粗"))
        if h.symbol and not h.has_body and h.date >= FORMAT_ERA:
            P.append(("ERROR",
                      f"{loc} {h.date} 只写符号没写内容行（§3.1「记录不合格」）"))
        elif h.symbol and not h.has_body:
            P.append(("INFO", f"{loc} {h.date} 迁移条目，旧档案没记内容（§3.1 已声明豁免）"))
    ro, rb = e.recount()
    if e.ok is not None and (ro, rb) != (e.ok, e.bad):
        P.append(("ERROR", f"连对连错与历史重数不符：档 {e.ok}/{e.bad} vs 重数 {ro}/{rb}"))
    if e.ok is not None and e.state == "在池" and ro >= 2:
        P.append(("ERROR", "连对已到 2 —— §3.3 该在原地改 🎓"))
    # ★★ 反向那一条（2026-09-05 补）：🎓 吃到 ❌ 就要**当场回潮**（§3.3）。
    #    ⛔ 忘了改状态的后果不是"下次照常召回"，而是**比答对的还晚回来**：
    #    状态还挂着 🎓 ⇒ 那次 ❌ 把毕业日清掉 ⇒ rc 算 0 ⇒ 站 🎓rc0 ＝ 应等 3 个练习日；
    #    而它本该回在池站「连错1」＝ 应等 1 个练习日（§3.6）。
    #    `append` 只会打一行 ★ 待办、⛔ 不代改 ⇒ 这一条闸就是兜住"忘了改"的那张网。
    if e.ok is not None and e.state == "🎓" and ro < 2:
        P.append(("ERROR",
                  f"状态是 🎓 但历史重数连对只有 {ro} —— §3.3：🎓 吃到 ❌ 要**当场回潮**"
                  f"（状态行改回「在池 ｜ 连对 0」），⛔ 不改的话它反而等更久才回来"))
    lj = e.last_row_date() or "—"
    if (e.last or "").strip() != lj:
        P.append(("ERROR", f"「上次」写着「{e.last}」，最后一个判定行是「{lj}」"))
    return P


def cmd_check(args):
    ents = load_all()
    all_nums = {e.num for e in ents}
    seen = {}
    dup = []
    for e in ents:
        if e.num in seen:
            dup.append((e.num, seen[e.num], f"{e.src}:{e.start}"))
        seen[e.num] = f"{e.src}:{e.start}"

    if args.changed:
        target, touched_lines = changed_entries(ents)
        scope = f"本次改动的 {len(target)} 条（git diff HEAD）"
    else:
        target, touched_lines = {e.num for e in ents}, set()
        scope = f"全档 {len(target)} 条"

    print("═" * 74)
    print(f"drill.py check · {scope} · 严格分界 {STRICT_FROM}")
    print("═" * 74)
    if dup:
        for n, a, b in dup:
            print(f"ERROR  {n} 编号重复：{a} 与 {b}（§3.1 编号只增不复用）")

    nerr = nwarn = ninfo = 0
    legacy_by_kind = Counter()
    for e in ents:
        if e.num not in target:
            continue
        for level, msg in check_entry(e, touched_lines, all_nums):
            if level == "ERROR":
                nerr += 1
                print(f"ERROR  {e.num} {e.src}:{e.start}  {msg}")
            elif level == "WARN":
                nwarn += 1
                if not args.quiet:
                    print(f"WARN   {e.num} {e.src}:{e.start}  {msg}")
            else:
                ninfo += 1
                legacy_by_kind[msg.split("」")[0].split(" ", 1)[-1][:20]] += 1
    # ★ 文件级结构校验（2026-09-03 加，她："migrate 行数一直不平，说明 check 的不靠谱呀"）
    #   条目级契约一条都没漏，但**条目之间的缝**从来没有人查 ——
    #   于是 15 处不规范的缝在档案里活了两周，直到 migrate 吃掉行数才暴露。
    #   ⚠️ 这一条是**整份文件**的性质，⛔ 不受 --changed 的范围限制（缝坏在哪都得报）。
    for f, name in ((PROBLEMS, "problems.md"), (GRADUATED, "graduated.md")):
        for key, got, want in gap_anomalies(f):
            nerr += 1
            print(f"ERROR  {name} {key} 之后的缝是 {got}，应为 {want}"
                  f"（族内只空一行／族间 空行+---+空行，§3.1 缝规范）")
    print("─" * 74)
    print(f"ERROR {nerr} · WARN {nwarn} · 存量提示 {ninfo}（{STRICT_FROM} 之前写下的行，不报错）")
    if ninfo and not args.quiet:
        for k, v in legacy_by_kind.most_common():
            print(f"   存量 · {k} … {v} 处")
    print("═" * 74)
    return 1 if nerr else 0


# ══════════════════════════════════════════════════════════════════════════
#  append —— 把教练写好的历史行放进 problems.md 的正确位置（她 2026-08-25 定）
#
#  ⚠️ 全脚本唯一一处【写内容文件】的地方，边界写死：
#     · 脚本 ⛔ 不产生任何一个字的内容 —— 行文全部由教练在 rows 文件里写好
#     · 脚本只做两件机器活：① 插到哪一行  ② 连对／连错／上次 三个数重算
#     · 判断仍然全在教练手上：⛔ 不自动改 🎓、⛔ 不自动改状态、⛔ 不碰条目正文
#  理由（08-25 实测）：那天组2 的记账 7.3 分钟里有 4.2 分钟是位置返工 ——
#  成员出题账被写进历史行里、#0343 正文改了三遍。位置和算术是机器规则，
#  让 LLM 每次重推一遍 ＝ 每次重犯一遍。
# ══════════════════════════════════════════════════════════════════════════
RE_ROWHEAD = re.compile(r"^#(\d{4})[ 　]+(.*)$")
BAD_IN_BODY = ("**成员出题账**", "### 历史记录") + tuple(SECTION_HEADS)


def parse_rows_file(path):
    """rows 文件 → [dict(num, symbol, occasion, body, lineno)]，格式见 SKILL §3.1 契约⑪。

        #0292 ✅ D3 学习日 C3·组2 第 1 题（**主考点**）
          题面「…」
          ⇒ …
        #0270 ◎✅ …
          …
    · 块头顶格：`#NNNN` ＋ 空格 ＋ 符号 ＋ 场合
    · 块体 = 直到下一个块头／EOF 的全部行（允许顶格 ``` 围栏，围栏内不认块头）
    · 块体第一个非空行必须缩进 —— 与 check 的「内容行」同一条口径
    """
    if not os.path.exists(path):
        sys.exit(f"⛔ rows 文件不存在：{path}")
    lines = open(path, encoding="utf-8").read().splitlines()
    blocks, cur, fence = [], None, False
    for i, raw in enumerate(lines):
        if raw.lstrip().startswith("```"):
            fence = not fence
        m = None if fence else RE_ROWHEAD.match(raw)
        if m:
            sym, occ, _, bold = parse_symbol(m.group(2))
            # ⛔ occ 是 parse_symbol 归一化过的（全角空格被压成半角），只能拿去比对，
            #    ⛔ 不许拿去回写。回写用 raw_occ —— 教练写的字节原样保留。
            rest = m.group(2)
            raw_occ = rest[len(sym):] if sym and rest.startswith(sym) else ""
            cur = dict(num="#" + m.group(1), symbol=sym, occasion=occ, raw_occ=raw_occ,
                       bold=bold, body=[], lineno=i + 1, head=raw)
            blocks.append(cur)
            continue
        if cur is None:
            if raw.strip():
                sys.exit(f"⛔ rows L{i+1}：文件开头有不属于任何块的内容「{raw.strip()[:30]}」")
            continue
        cur["body"].append(raw)
    return blocks


def rewrite_status(line, ok, bad, last):
    out = re.sub(r"(连对[ 　]*)\d+", lambda m: m.group(1) + str(ok), line, count=1)
    out = re.sub(r"(连错[ 　]*)\d+", lambda m: m.group(1) + str(bad), out, count=1)
    out = re.sub(r"(上次[ 　]*)(\S+)", lambda m: m.group(1) + last, out, count=1)
    return out


def cmd_append(args):
    today = args.date or date.today().isoformat()
    if not re.fullmatch(r"20\d\d-\d\d-\d\d", today):
        sys.exit(f"⛔ --date 要写成 YYYY-MM-DD，收到「{today}」")

    blocks = parse_rows_file(args.file)
    if not blocks:
        sys.exit("⛔ rows 文件里一个块都没有")

    ents = load_all()
    by_num = {}
    for e in ents:
        by_num.setdefault(e.num, []).append(e)

    # ── 校验：⛔ 一条不过就整批不写（no 兜底、no 部分成功）─────────────────
    errs, warns = [], []
    seen = {}
    for b in blocks:
        tag = f"rows L{b['lineno']} {b['num']}"
        if b["num"] in seen:
            errs.append(f"{tag} 同一批里重复出现（上一次在 L{seen[b['num']]}）")
        seen[b["num"]] = b["lineno"]

        if b["symbol"] is None:
            errs.append(f"{tag} 切不出符号：「{b['head'][:40]}」"
                        f" —— 符号必须紧跟编号，且是 §3.2 表里的那几个")
        elif b["symbol"] in LEGACY:
            errs.append(f"{tag} 光杆 ◎ —— §3.2 起必须写成 ◎✅ 或 ◎−")
        if b["bold"]:
            errs.append(f"{tag} 符号加粗了 —— §3.2 符号紧跟日期、不加粗")

        first = next((l for l in b["body"] if l.strip()), None)
        if first is None:
            errs.append(f"{tag} 只有块头没有内容行（§3.1「记录不合格」）")
        elif first[:1] not in (" ", "\t", "　"):
            errs.append(f"{tag} 第一个内容行没缩进：「{first[:30]}」")
        for k, l in enumerate(b["body"]):
            for bad in BAD_IN_BODY:
                if l.strip().startswith(bad):
                    errs.append(f"{tag} 块体第 {k+1} 行是「{bad}」—— "
                                f"节标题／成员出题账⛔不许写进历史行，它们挂在条目正文")

        got = by_num.get(b["num"])
        if not got:
            errs.append(f"{tag} 全档查无此编号")
            continue
        if len(got) > 1:
            errs.append(f"{tag} 编号重复出现在 {[f'{e.src}:{e.start}' for e in got]}")
            continue
        e = got[0]
        b["entry"] = e
        if e.state not in ("在池", "🎓"):
            errs.append(f"{tag} 状态是「{e.state}」—— ⛔ 退池／并入的条目不再记判定")
        elif e.status_lineno is None:
            errs.append(f"{tag} 找不到状态行")
        elif not e.history and not e.never_judged:
            errs.append(f"{tag} 这条既没有历史行、也没有 `- （从未被判定过）` 占位行 —— "
                        f"档案坏了，先补好（`drill.py check` 也会报）")
        elif e.never_judged and e.history:
            errs.append(f"{tag} 这条既有 {len(e.history)} 条历史行、又留着 "
                        f"`- （从未被判定过）` —— 先把那一行删掉再 append（⛔ 脚本不代删）")
        else:
            # ⚠️ 用 `_msg_key` 抹掉行号再比：`pre_err` 是**插入前**算的，同一批里
            #    排在前面的条目一插行，后面那条的存量错误行号整体下移 ⇒ 同一个存量错
            #    换个 `L` 号就会被当成「append 自己引入的新错」⇒ **整批假回滚**。
            #    （`_msg_key` 就是 migrate 为同一件事写的，这里复用同一把尺。）
            b["pre_err"] = {_msg_key(m) for lv, m in check_entry(e, set(), None)
                            if lv == "ERROR"}
            same = [h for h in e.history if h.date == today]
            if same:
                warns.append(f"{tag} 该条今天已有 {len(same)} 行"
                             f"（{same[-1].symbol} {same[-1].occasion[:22]}）"
                             f" —— §3.2 同日只结算一次，这一行只留痕不推进")

    if errs:
        print("═" * 74)
        print(f"drill.py append · ⛔ 校验没过，{len(errs)} 处 —— 一个字都没写")
        print("═" * 74)
        for x in errs:
            print("ERROR  " + x)
        print("═" * 74)
        return 1

    # ── 组装：**两个文件**各自从后往前插，免得行号错位 ────────────────────
    #  ★★ 2026-09-05 放开写 graduated.md：复检队列天天要在毕业条目上记判定行（§4③e）。
    #     旧写法 `if e.src != "problems.md": ERROR` 会把复检的每一条判定都挡在门外。
    #     ⛔ 放开的只是【往哪个文件写】—— 校验、自查、回滚一条都没松：
    #        任何一步不过 ⇒ **两个文件一起回滚到原样**。
    FILES = {"problems.md": PROBLEMS, "graduated.md": GRADUATED}
    orig = {}
    buf = {}
    for name, path in FILES.items():
        orig[name] = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        buf[name] = (orig[name] or "").split("\n")

    plan = []
    for b in blocks:
        e = b["entry"]
        lines = buf[e.src]
        lo, hi = e.start - 1, (e.end or len(lines))
        # 「从未被判定过」占位行：只有【真的一条历史行都没有】时才顶掉它。
        # 既有历史行又留着那一行 ⇒ 上面已经拦下来了，不会走到这儿。
        drop = None
        if e.never_judged and not e.history:
            for i in range(lo, hi):
                if lines[i].strip() == "- （从未被判定过）":
                    drop = i
                    break
        if drop is not None:
            at = drop + 1
        else:
            # 插入点 ＝ 条目最后一个非空行之后 —— 这是档案既有的约定（08-25 回放实证：
            # 11 条全部字节一致）。`### 历史记录` 之后挂着的 `<details>原始行` 迁移块、
            # `---` 分隔线、`> 🗑 撤销说明` 都留在原处，新行接在整条之后。
            # ⚠️ 换约定（比如"插到 </details> 之前"）会动到全档 97 条的排版 —— 要改先问她。
            # ⚠️ 2026-09-03 修：往回走时要**跳过条目末尾的空行与族边界 `---`**。
            #    条目是本族最后一条时，它的 span 尾巴上挂着族边界（空行 ＋ --- ＋ 空行），
            #    旧写法「最后一个非空行之后」= 插到 `---` 的**下面** ⇒ 新历史行掉到下一族头前面，
            #    族边界被顶进条目内部（09-03 在 #0404 上实测到，是当天新加的缝校验抓出来的）。
            j = hi
            while j > lo and (not lines[j - 1].strip() or lines[j - 1].strip() == "---"):
                j -= 1
            at = j
        row = f"- {today} {b['symbol']}{b['raw_occ']}".rstrip()
        plan.append(dict(e=e, src=e.src, at=at, drop=drop, block=[row] + b["body"], b=b))

    # ⛔ 倒序插入必须**按文件分别排**：两个文件的行号各数各的，混在一起排会错位
    for name in FILES:
        lines = buf[name]
        for p in sorted([x for x in plan if x["src"] == name], key=lambda x: -x["at"]):
            body = [l for l in p["block"]]
            while body and not body[-1].strip():
                body.pop()
            lines[p["at"]:p["at"]] = body
            if p["drop"] is not None:
                del lines[p["drop"]]

    touched = sorted({p["src"] for p in plan})
    if args.dry_run:
        print("═" * 74)
        print(f"drill.py append --dry-run · {len(plan)} 条 · {today}（⛔ 没写盘）")
        print("═" * 74)
        for p in sorted(plan, key=lambda x: (x["src"], x["at"])):
            print(f"  {p['e'].num}  插到 {p['src']} L{p['at']}  "
                  f"（{len(p['block'])} 行）{'· 顶掉「从未被判定过」' if p['drop'] is not None else ''}")
            print(f"      {p['block'][0][:88]}")
        for w in warns:
            print("WARN   " + w)
        print("═" * 74)
        return 0

    def rollback():
        for nm in touched:
            if orig[nm] is not None:
                open(FILES[nm], "w", encoding="utf-8").write(orig[nm])

    for name in touched:
        open(FILES[name], "w", encoding="utf-8").write("\n".join(buf[name]))

    # ── 重算三个数（连对／连错／上次）────────────────────────────────────
    ents2 = {}
    for name in touched:
        ents2[name] = {e.num: e for e in parse_file(FILES[name], name)}
    lines2 = {name: open(FILES[name], encoding="utf-8").read().split("\n") for name in touched}
    moved = []
    for b in blocks:
        name = b["entry"].src
        e2 = ents2[name][b["num"]]
        ok, bad = e2.recount()
        last = e2.last_row_date() or "—"
        i = e2.status_lineno - 1
        before = lines2[name][i]
        lines2[name][i] = rewrite_status(before, ok, bad, last)
        moved.append((b["num"], name, e2.state, ok, bad, last, before != lines2[name][i]))
    for name in touched:
        open(FILES[name], "w", encoding="utf-8").write("\n".join(lines2[name]))

    # ── 自查：写完立刻按 check 的规矩硬查这几条，出 ERROR 就整批回滚 ──────
    ents3 = parse_file(PROBLEMS, "problems.md") + parse_file(GRADUATED, "graduated.md")
    all_nums = {e.num for e in ents3}
    idx3 = {e.num: e for e in ents3}
    hard = set()
    for b in blocks:
        e3 = idx3[b["num"]]
        for h in e3.history:
            if h.date == today:
                hard.add((e3.src, h.lineno))
    # 只对【append 自己引入的新 ERROR】回滚。
    # ⛔ 「连对已到 2 该改 🎓」「🎓 吃到 ❌ 该降级」不算错 —— 那是 append 正常的结果、
    #    是留给教练的判断（脚本⛔不代做），下面会当 ★ 待办打出来；`check --changed`
    #    仍然会报它，直到教练亲手改掉状态。
    TODO = ("连对已到 2",)
    bad_rows = []
    for b in blocks:
        e3 = idx3[b["num"]]
        pre = b.get("pre_err", set())
        for level, msg in check_entry(e3, hard, all_nums):
            if level != "ERROR" or _msg_key(msg) in pre or msg.startswith(TODO):
                continue
            bad_rows.append((b["num"], msg))
    if bad_rows:
        rollback()
        print("═" * 74)
        print(f"drill.py append · ⛔ 写完自查不过，{len(bad_rows)} 处 —— 已整批回滚"
              f"（{'／'.join(touched)} 都退回原样）")
        print("═" * 74)
        for n, m in bad_rows:
            print(f"ERROR  {n}  {m}")
        print("═" * 74)
        return 1

    print("═" * 74)
    print(f"drill.py append · {len(plan)} 条已写进 {'／'.join(touched)} · {today} · 自查 ERROR 0")
    print("═" * 74)
    for num, name, state, ok, bad, last, ch in moved:
        flag = ""
        if state == "在池" and ok >= 2:
            flag = "   ⇒ ★ 连对已到毕业线 2，§3.3 要你原地改 🎓（脚本⛔不代改）"
        elif state == "🎓" and bad >= 1:
            flag = "   ⇒ ★ 🎓 条目吃到 ❌，§3.3 要你把状态改回在池（回潮，脚本⛔不代改）"
        print(f"  {num}  {name}  {state}  连对 {ok} ｜ 连错 {bad} ｜ 上次 {last}{flag}")
    for w in warns:
        print("WARN   " + w)
    print("─" * 74)
    print("下一步：`drill.py check --changed` 复核全部改动（§0.3）")
    print("═" * 74)
    return 0

# ══════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════
#  migrate —— problems.md ⇄ graduated.md 双向搬迁（SKILL §3.3 / §4⑥）
#
#  ⛔ 这是本脚本第二个会写内容文件的子命令（第一个是 append），同样【一个字都不产生】：
#     它只把**已经存在的整块字节**从一个文件搬到另一个文件，
#     判断（谁毕业、谁降级）仍然全部由教练手写状态行，脚本只认状态行的第 1 格。
#       problems.md 里状态 ＝ 🎓        ⇒ 搬进 graduated.md
#       graduated.md 里状态 ≠ 🎓        ⇒ 搬回 problems.md
#     ⛔ 不改状态、不改正文、不改历史记录、不改任何一个数、不碰两个文件的头部说明块。
#
#  切块口径（下面 split_file 是全脚本唯一一处「档案的块状结构长什么样」的定义）：
#     文件 ＝ header ＋ Σ(块 body ＋ 块 trail)
#       块       `# FNN …`（族头）或 `## #NNNN …`（条目），认法与 parse_file 完全一致
#       body     块头那行 → 尾部分隔行之前
#       trail    紧跟在 body 后面的**空行与 `---`**，＝ 这个块与下一个块之间的「缝」
#     ⇒ 拼回去必须与原文逐字节相同（每次 migrate 都先自校这一条，不过就退出）
#     搬块时缝跟着走：删块 ⇒ 它的 trail 交给前一个块（族间的 `---` 不会被带走）；
#                     插块 ⇒ 新块接管前一个块的 trail，前一个块换成条目缝 `[""]`。
# ══════════════════════════════════════════════════════════════════════════

ENTRY_GAP = [""]                 # 条目与条目之间的缝
FAM_GAP = ["", "---", ""]        # 族与族之间的缝（graduated.md 的写法，全档 15 处都是它）


class Blk:
    """档案里的一个块。kind ∈ 'fam' / 'entry'。"""
    __slots__ = ("kind", "key", "body", "trail")

    def __init__(self, kind, key, body, trail):
        self.kind = kind
        self.key = key            # 'F08' 或 '#0342'
        self.body = body          # 块头那行 + 正文，⛔ 逐字不动
        self.trail = trail        # 块后面的缝（空行／---）

    def __repr__(self):
        return f"<Blk {self.kind} {self.key} body={len(self.body)} trail={self.trail!r}>"


def split_file(path):
    """→ (header_lines, [Blk…], 原文本)。⛔ 严格：拼回去与原文逐字节相同。"""
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    heads = []
    for i, l in enumerate(lines):
        m = RE_FAM_HEAD.match(l)          # 与 parse_file 同一条认法
        if m:
            heads.append((i, "fam", m.group(1)))
            continue
        m = RE_ENTRY.match(l)
        if m:
            heads.append((i, "entry", m.group(1)))
    if not heads:
        sys.exit(f"⛔ {os.path.basename(path)} 里一个块都没有 —— 档案结构不对，先修档案")
    header = lines[:heads[0][0]]
    blocks = []
    for k, (i, kind, key) in enumerate(heads):
        stop = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        j = stop
        while j > i + 1 and lines[j - 1].strip() in ("", "---"):
            j -= 1
        blocks.append(Blk(kind, key, lines[i:j], lines[j:stop]))
    # 自校：切开再拼回去必须一模一样
    back = header[:]
    for b in blocks:
        back += b.body + b.trail
    if "\n".join(back) != text:
        sys.exit(f"⛔ {os.path.basename(path)} 切块自校失败 —— 脚本读不懂这个文件，⛔ 不动它")
    return header, blocks, text


#  ★★ 缝的规范形状（2026-09-03 她定，起因："migrate 行数一直不平，说明 check 的不靠谱呀"）
#     档案的排版惯例只有两条，写死在这里，`check` 与 `migrate` 自校共用同一份定义：
#       族内条目之间   ⇒ 只空一行            trail == [""]
#       族与族之间     ⇒ 空行 + --- + 空行    trail == ["", "---", ""]
#       文件最后一块   ⇒ 只空一行（文件以单个换行结尾）
#     ⛔ 为什么必须机器查：`migrate` 删块时把「前一块的缝」换成「被删块的缝」——
#        缝不规范时就会被吃掉一两行，而**旧的四项自校全部只看条目正文，看不见缝**
#        ⇒ 报告里那句「行数一加一减对得上」只是打印给人看的，⛔ 从来没有人／没有断言在验它。
#        2026-09-03 实测：problems.md 15 处缝不规范，搬一条 #0378 就凭空少 2 行 1 个 `---`，
#        而自校四项**全绿**。⇒ 加第 5 项，并在 check 里同样硬查。
def gap_of(blocks, i):
    """第 i 块**应该**带的缝。
    ★ 最后一块是例外：文件可以以单个换行结尾（trail ＝ [""]），也可以完全不带换行（[]）——
      两种都合法，⛔ 别把「文件末尾没有换行」当成缝坏了（E4 就是这个形状）。"""
    if i + 1 >= len(blocks):
        return None                                    # None ＝ 只要不含 --- 就放行
    return ["", "---", ""] if blocks[i + 1].kind == "fam" else [""]


def gap_anomalies(path):
    """→ [(块 key, 实际缝, 应有的缝)]，空列表 ＝ 全部规范。"""
    _, bl, _ = split_file(path)
    out = []
    for i, b in enumerate(bl):
        want = gap_of(bl, i)
        if want is None:
            if b.trail not in ([], [""]):
                out.append((b.key, b.trail, '[] 或 [""]（文件末尾）'))
            continue
        if b.trail != want:
            out.append((b.key, b.trail, want))
    return out


def join_file(header, blocks):
    out = header[:]
    for b in blocks:
        out += b.body + b.trail
    return "\n".join(out)


def fam_of(blocks, fam):
    """族 fam 的 [族头下标, 该族最后一个块的下标+1)；没有这个族返回 None。"""
    lo = None
    for i, b in enumerate(blocks):
        if b.kind == "fam" and b.key == fam:
            lo = i
            break
    if lo is None:
        return None
    hi = len(blocks)
    for i in range(lo + 1, len(blocks)):
        if blocks[i].kind == "fam":
            hi = i
            break
    return lo, hi


def insert_block(blocks, at, blk):
    """把 blk 插到下标 at（＝插在 blocks[at] 前面）。缝按上面的规则倒手。"""
    prev = blocks[at - 1]
    blk.trail = prev.trail
    prev.trail = list(ENTRY_GAP)
    blocks.insert(at, blk)


def make_fam_section(blocks, fam, donor_blocks):
    """目标文件还没有这个族 ⇒ 从来源文件把族头那几行**逐字**抄过来、按族序插进去。
    ⛔ 一个字都不新写：族头与那句族说明全部是 donor 文件里的原字节。"""
    donor = next((b for b in donor_blocks if b.kind == "fam" and b.key == fam), None)
    if donor is None:
        sys.exit(f"⛔ 两个文件里都没有 {fam} 的族头 —— 不代写，先手工加上族头再跑")
    at = len(blocks)
    for i, b in enumerate(blocks):
        if b.kind == "fam" and b.key > fam:
            at = i
            break
    head = Blk("fam", fam, list(donor.body), list(ENTRY_GAP))
    if at == 0:                            # 新族排在全部族之前 ⇒ 前面只有 header
        keep = list(FAM_GAP)
    else:
        prev = blocks[at - 1]
        keep = prev.trail                  # 这条缝原本是给 blocks[at] 的，留给本族最后一块
        prev.trail = list(FAM_GAP)         # 族与族之间隔 `---`
    blocks.insert(at, head)
    return at, keep


def _msg_key(msg):
    """把报错信息里的行号抹掉 —— 搬完行号必然变，比对的是「有没有多出新错」。"""
    return re.sub(r"\bL\d+\b", "L*", msg)


def _errmap(ents, all_nums):
    out = Counter()
    for e in ents:
        for level, msg in check_entry(e, set(), all_nums):
            out[(e.num, level, _msg_key(msg))] += 1
    return out


def _statesnap(ents):
    return {e.num: (e.state, e.ok, e.bad, e.goal, e.last, e.fam, e.fam_section,
                    len(e.history), e.review_mark) for e in ents}


def cmd_migrate(args):
    # ── 0. 搬之前的全档快照（内容比对的基准）──────────────────────────
    ph, pb, ptext = split_file(PROBLEMS)
    gh, gb, gtext = split_file(GRADUATED)
    body_before = {}
    for src, bl in (("problems.md", pb), ("graduated.md", gb)):
        for b in bl:
            if b.kind == "entry":
                if b.key in body_before:
                    sys.exit(f"⛔ {b.key} 在全档出现了两次 —— 先修重号再搬")
                body_before[b.key] = tuple(b.body)

    ents0 = load_all()
    nums0 = {e.num for e in ents0}
    err0 = _errmap(ents0, nums0)
    snap0 = _statesnap(ents0)
    pre_err = sum(v for (n, lv, m), v in err0.items() if lv == "ERROR")

    # ── 1. 定搬迁清单：只认状态行第 1 格，⛔ 不做任何判断 ─────────────────
    p2g = [e for e in ents0 if e.src == "problems.md" and e.state == "🎓"]
    g2p = [e for e in ents0 if e.src == "graduated.md" and e.state != "🎓"]
    p2g.sort(key=lambda e: (e.fam or "", e.num))
    g2p.sort(key=lambda e: (e.fam or "", e.num))

    print("═" * 74)
    print("drill.py migrate · problems.md ⇄ graduated.md 双向搬迁（§3.3 / §4⑥）")
    print("═" * 74)
    if pre_err:
        print(f"⚠️ 搬之前全档已有 {pre_err} 处 ERROR —— 搬迁不会修它们，也不会新增；"
              f"搬完请照常跑 `check --all` 收拾")
    if not p2g and not g2p:
        print("两边都没有要搬的：problems.md 无 🎓 · graduated.md 无非 🎓 ⇒ 无操作")
        print(f"全档 {len(ents0)} 条 ＝ problems.md {sum(1 for e in ents0 if e.src=='problems.md')}"
              f" ＋ graduated.md {sum(1 for e in ents0 if e.src=='graduated.md')}")
        print("═" * 74)
        return 0

    print(f"problems.md → graduated.md  {len(p2g)} 条（状态 🎓）")
    for e in p2g:
        print(f"   {e.num}  {e.fam}  {e.title[:38]}")
    print(f"graduated.md → problems.md  {len(g2p)} 条（状态已不是 🎓 ＝ 🎓 后复发）")
    for e in g2p:
        print(f"   {e.num}  {e.fam}  状态「{e.state}」 {e.title[:30]}")

    # 族一致性：搬迁按状态行的「族」放段，与 check 契约③ 同一口径
    bad_fam = [e for e in p2g + g2p if e.fam not in FAMILIES or e.fam != e.fam_section]
    if bad_fam:
        print("─" * 74)
        for e in bad_fam:
            print(f"⛔ {e.num} 族「{e.fam}」与所在分段「{e.fam_section}」不一致 —— "
                  f"先修族再搬（否则搬完位置就是错的）")
        print("═" * 74)
        return 1

    if args.dry_run:
        print("─" * 74)
        print("--dry-run：⛔ 没有写盘。去掉 --dry-run 才真搬。")
        print("═" * 74)
        return 0

    # ── 2. 搬：先从来源摘块，再按族＋编号升序插进目标 ────────────────────
    def take(blocks, nums):
        got, keep = {}, []
        for i, b in enumerate(blocks):
            if b.kind == "entry" and b.key in nums:
                got[b.key] = b
                keep.append(i)
        for i in reversed(keep):                       # 缝交给前一个块（族间 --- 不被带走）
            if i == 0:
                sys.exit("⛔ 条目排在第一个族头之前 —— 档案结构不对，先修档案")
            blocks[i - 1].trail = blocks[i].trail
            del blocks[i]
        return got

    def put(blocks, blk, fam, donor):
        span = fam_of(blocks, fam)
        if span is None:
            at, keep = make_fam_section(blocks, fam, donor)
            blocks.insert(at + 1, blk)
            blk.trail = keep
            return
        lo, hi = span
        at = hi
        for i in range(lo + 1, hi):
            if blocks[i].kind == "entry" and blocks[i].key > blk.key:
                at = i
                break
        insert_block(blocks, at, blk)

    got_p = take(pb, {e.num for e in p2g})
    got_g = take(gb, {e.num for e in g2p})
    for e in p2g:
        put(gb, got_p[e.num], e.fam, pb)
    for e in g2p:
        put(pb, got_g[e.num], e.fam, gb)

    new_p, new_g = join_file(ph, pb), join_file(gh, gb)
    open(PROBLEMS, "w", encoding="utf-8").write(new_p)
    open(GRADUATED, "w", encoding="utf-8").write(new_g)

    # ── 3. 搬完自校 —— 任何一条不过就整批回滚（与 append 同一个仪式）────────
    def rollback(why, detail):
        open(PROBLEMS, "w", encoding="utf-8").write(ptext)
        open(GRADUATED, "w", encoding="utf-8").write(gtext)
        print("─" * 74)
        print(f"⛔ 搬完自校不过：{why} —— 两个文件已整批回滚，档案回到搬之前")
        for d in detail[:20]:
            print("   " + d)
        print("═" * 74)
        return 1

    ph2, pb2, _ = split_file(PROBLEMS)
    gh2, gb2, _ = split_file(GRADUATED)
    body_after, dup = {}, []
    for bl in (pb2, gb2):
        for b in bl:
            if b.kind == "entry":
                if b.key in body_after:
                    dup.append(b.key)
                body_after[b.key] = tuple(b.body)
    if dup:
        return rollback("搬完出现重号", sorted(set(dup)))
    if set(body_after) != set(body_before):
        lost = sorted(set(body_before) - set(body_after))
        extra = sorted(set(body_after) - set(body_before))
        return rollback("条目集合变了", [f"丢了 {x}" for x in lost] + [f"多了 {x}" for x in extra])
    diff_body = [n for n in body_before if body_before[n] != body_after[n]]
    if diff_body:
        return rollback("有条目正文被改动了（搬迁必须逐字节原样）", sorted(diff_body))
    if (ph2 != ph) or (gh2 != gh):
        return rollback("文件头部被动过（搬迁⛔不碰头部说明块）", ["problems.md 或 graduated.md 的 header"])

    ents1 = load_all()
    nums1 = {e.num for e in ents1}
    snap1 = _statesnap(ents1)
    moved_bad = [n for n in snap0 if snap0[n] != snap1[n]]
    if moved_bad:
        return rollback("有条目的状态字段变了（搬迁⛔不改状态/连对/连错/上次/族）",
                        [f"{n}  {snap0[n]}  →  {snap1[n]}" for n in sorted(moved_bad)])
    err1 = _errmap(ents1, nums1)
    new_errs = [f"{n} {lv} {m}" for (n, lv, m), c in (err1 - err0).items()]
    if new_errs:
        return rollback(f"多出 {len(new_errs)} 处 check 报告", sorted(new_errs))

    # 位置硬查：🎓 全在 graduated.md、非 🎓 全在 problems.md、族内编号升序
    wrong = [f"{e.num} 状态「{e.state}」却住在 {e.src}" for e in ents1
             if (e.state == "🎓") != (e.src == "graduated.md")]
    for bl, src in ((pb2, "problems.md"), (gb2, "graduated.md")):
        fam, order = None, []
        for b in bl + [Blk("fam", "ZZZ", [], [])]:
            if b.kind == "fam":
                if order != sorted(order):
                    wrong.append(f"{src} {fam} 段内编号不是升序")
                fam, order = b.key, []
            else:
                order.append(b.key)
    if wrong:
        return rollback("搬完位置不对", wrong)

    # ★ 第 5 项（2026-09-03 加）：缝守恒 —— 条目正文之外的东西也不许丢
    #   ① 搬完两个文件的缝必须全部规范（否则下一次搬迁会继续吃行）
    #   ② 非空行多重集**只许多不许少**，且多出来的只能是新造的族头／族间 `---`
    gap_bad = []
    for f in (PROBLEMS, GRADUATED):
        for key, got, want in gap_anomalies(f):
            gap_bad.append(f"{os.path.basename(f)} {key} 缝是 {got}，应为 {want}")
    if gap_bad:
        return rollback("搬完缝不规范（族内只空一行／族间 --- ）", gap_bad)
    def nonblank(t):
        c = {}
        for l in t.split("\n"):
            if l.strip():
                c[l] = c.get(l, 0) + 1
        return c
    n0, n1 = nonblank(ptext + "\n" + gtext), nonblank(new_p + "\n" + new_g)
    lost = [f"{l}  ×{n0[l] - n1.get(l, 0)}" for l in n0 if n1.get(l, 0) < n0[l]]
    if lost:
        return rollback(f"有 {len(lost)} 种非空行**丢了**（搬迁只许挪、⛔ 不许少）", lost)
    gained = [l for l in n1 if n1[l] > n0.get(l, 0)]
    bad_gain = [l for l in gained if not (RE_FAM_HEAD.match(l) or l.strip() == "---"
                                          or l.startswith("> "))]
    if bad_gain:
        return rollback(f"凭空多出 {len(bad_gain)} 种非空行（只允许新造族头与 --- ）", bad_gain)

    # ── 4. 报告 ────────────────────────────────────────────────────────
    print("─" * 74)
    print(f"✔ 已搬 {len(p2g) + len(g2p)} 条 · 条目正文逐字节未变 · 状态字段未变 · "
          f"check 无新增报告 · **缝规范且非空行一行没丢**")
    print(f"  全档 {len(ents1)} 条 ＝ problems.md "
          f"{sum(1 for e in ents1 if e.src=='problems.md')} ＋ graduated.md "
          f"{sum(1 for e in ents1 if e.src=='graduated.md')}"
          f"　（搬前 {sum(1 for e in ents0 if e.src=='problems.md')} ＋ "
          f"{sum(1 for e in ents0 if e.src=='graduated.md')}）")
    for path, before, after in ((PROBLEMS, ptext, new_p), (GRADUATED, gtext, new_g)):
        b, a = before.split("\n"), after.split("\n")
        print(f"  {os.path.basename(path):<14} {len(b)} 行 → {len(a)} 行"
              f"（{len(a)-len(b):+d}）")
    print("─" * 74)
    print("git 侧核对（§4⑥ 收尾要贴的就是这个）：")
    try:
        out = subprocess.run(["git", "diff", "--numstat", "--", PROBLEMS, GRADUATED],
                             cwd=ROOT, capture_output=True, text=True, timeout=30)
        for l in out.stdout.strip().splitlines():
            add, dele, f = (l.split("\t") + ["", "", ""])[:3]
            print(f"  {os.path.basename(f):<14} +{add} −{dele}")
    except Exception as ex:                                   # noqa: BLE001
        print(f"  （git diff 跑不了：{ex}）")
    print("─" * 74)
    print("下一步（§4⑥）：")
    print("  1) `drill.py check --all`  —— ERROR 必须为 0")
    print("  2) `drill.py stats`        —— 把新数抄进 problems.md 头部「全档状态」块")
    print("     ⛔ 搬完这一次不要用 `check --changed`：两个文件整体位移，git diff 会把")
    print("       大批没动过的条目算成「改过」⇒ 存量行被按新文法查 ⇒ 全是假阳性")
    print("═" * 74)
    return 0


# ══════════════════════════════════════════════════════════════════════════
#  trigger —— 把 session 里【当天实际用的中文题面】搬回条目（她 2026-09-02 定）
#
#  ⛔ 这是本脚本第三个会写内容文件的子命令（前两个是 append / migrate），
#     同样【一个字的内容都不产生】：新题面逐字取自 session 的「### 题面」围栏，
#     脚本只做搬运 ＋ 固定格式的包装（老触发点留档那一行 ＋ 日期标记）。
#     ⛔ 不改状态、不改别的节、不改任何一个数、不碰历史记录。
#  为什么要它：§6 通则要求「同一编号在不同日子出题必须换新的中文触发点」，
#     换出来的题面本来只活在 session 里 —— 下次 `pick` 打的还是老触发点，
#     教练得手工回填 N 条（09-01 那天手工件③ 一节回填了 7 条）。
#     位置和搬运是机器活，判断（写什么题面）仍然全在教练手上。
#
#  跑：python3 drill.py trigger --session sessions/2026-09-01.md --group 1 [--dry-run]
# ══════════════════════════════════════════════════════════════════════════
#  拒绝策略分两层（她 2026-09-02 定，⛔ 不许混）：
#    【输入坏了】⇒ 整批不写 —— 映射数 ≠ 题面题数 · 映射读不出 · 编号不存在 · 编号重复 ·
#                            题号跳号/重复 · 条目里有不配对的 ``` 围栏
#    【条目不适用】⇒ 逐条跳过并打印原因，其余照常写 —— 🎓／退池／并入 · 词组 · 作文验 ·
#                            已经搬过（幂等）
#  理由：今天毕业的条目**根本不需要换题面**（它出池了、不会再被抽到），
#        为它把整组挡死是过严（09-01 组2 就是：7 条当天毕业 ⇒ 整组写不了）。
# ══════════════════════════════════════════════════════════════════════════
#  ★ 题面里的编号题：`N.` 后面必须**跟空白**，且 N 必须正好是下一个题号 ——
#    否则续行里的 `3.5 倍，涨得非常快。` 会被吃成新的第 3 题（P1-4）。
RE_TRIG_ITEM = re.compile(r"^[ \t　]*(\d+)\.(?:[ \t　]+(.*))?$")
RE_TRIG_MAP = re.compile(r"(?<![0-9#])(\d+)[ \t　]*(#\d+)")
RE_TRIG_MAPLINE = re.compile(r"^[ \t　]*\d+[ \t　]*#\d")
RE_TRIG_ANYNUM = re.compile(r"#\d+")
TRIG_OLD_PREFIX = "（老触发点留档不删："
TRIG_OLD_SEP = "／"
#  脚本自己生成的那一行 —— 折叠留档时必须先剥掉它，⛔ 不许套娃（P2-7）
RE_TRIG_STAMP = re.compile(r"^⚠️\s*\*\*20\d\d-\d\d-\d\d 换题面\*\*（`drill\.py trigger`")
TRIG_HARD_BOUND = tuple(SECTION_HEADS) + (MEMBERS_HEAD,)


def _read_raw(path):
    """→ (lines, nl, text)。⛔ 不做换行翻译 —— CRLF 的档案写回去仍然是 CRLF（P2-8）。
    行下标与 `parse_file`（universal newlines + splitlines）一一对齐。"""
    text = io.open(path, encoding="utf-8", newline="").read()
    nl = "\r\n" if text.count("\r\n") * 2 > text.count("\n") else "\n"
    return text.split(nl), nl, text


def _raw_blocks(lines):
    """按顶格 `## #NNNN` 切条目块 → {编号: (起, 止)}（0-based，止不含）。
    ⛔ **独立实现**：自校不许和被校对象共用同一个解析函数（P2-9）——
       `_trigger_span` 那套错了，用它自己去校自己就永远看不见。"""
    heads = [(i, m.group(1)) for i, l in enumerate(lines)
             for m in (RE_ENTRY.match(l),) if m]
    out = {}
    for k, (i, num) in enumerate(heads):
        stop = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        out[num] = (i, stop)
    return out


def _first_fence_body(lines, s, e):
    """[s,e) 里第一个顶格 ``` 围栏的内容行；没有围栏 ⇒ None。"""
    a = None
    for i in range(s, e):
        if lines[i].startswith("```"):
            if a is None:
                a = i + 1
            else:
                return lines[a:i]
    return None


def _parse_numbered_items(body):
    """围栏里的编号题 → ({k: [行…]}, err)。
    一题可跨多行，直到**下一个题号**或围栏结束。
    ⛔ 逐字保留中文，只剥掉行首的 `N. ` 与续行的缩进 —— 那是位置，不是内容。
    ★ 判据两道：① `N.` 后面必须跟空白　② N 必须正好是下一个题号
      ⇒ `3.5 倍，涨得非常快。` 这种续行⛔不会被吃成新题。"""
    cand = [int(m.group(1)) for m in (RE_TRIG_ITEM.match(l) for l in body) if m]
    if cand != list(range(1, len(cand) + 1)):
        return None, "题面围栏里的题号不是 1..N 连号：%s" % cand
    out, cur = {}, None
    for raw in body:
        m = RE_TRIG_ITEM.match(raw)
        if m and int(m.group(1)) == len(out) + 1:
            k = int(m.group(1))
            cur = [(m.group(2) or "").rstrip()]
            out[k] = cur
        elif cur is not None:
            cur.append(raw.strip())
        elif raw.strip():
            return None, "题面围栏里第 1 题之前还有正文：「%s」" % raw.strip()[:30]
    for k in out:
        while out[k] and not out[k][-1].strip():
            out[k].pop()
    return out, None


def _trigger_span(lines, e):
    """条目的「**中文触发点**」节 → (head, start, end)，0-based，end 不含尾部空行。
    ⛔ **硬边界**：下一个加粗节标题 ／ 成员出题账 ／ 任何 `### ` ——
       ⛔ 不跑围栏状态机（P2-9：条目里有不配对的 ``` 时，状态机会把 `### 历史记录`
          整节吞进触发点节，而自校用同一套坏状态机 ⇒ 看不见破坏）。"""
    lo, hi = e.start - 1, (e.end or len(lines))
    head = None
    for i in range(lo, min(hi, len(lines))):
        t = lines[i]
        if head is None:
            if t == "**中文触发点**":
                head = i
            continue
        if t in TRIG_HARD_BOUND or t.startswith("### "):
            hi = i
            break
    if head is None:
        return None
    end = min(hi, len(lines))
    while end > head + 1 and not lines[end - 1].strip():
        end -= 1
    return head, head + 1, end


def _entry_fence_unpaired(lines, e):
    """条目里 ``` 的条数是不是奇数（＝有不配对的围栏）。"""
    lo, hi = e.start - 1, min(e.end or len(lines), len(lines))
    return sum(1 for i in range(lo, hi) if lines[i].strip().startswith("```")) % 2 == 1


def _strip_trig_wrappers(body):
    """折叠留档前先剥掉**脚本自己生成的包装**（P2-7）：
      · `⚠️ **YYYY-MM-DD 换题面**（`drill.py trigger` …）` 整行
      · 既有的 `（老触发点留档不删：…）`（可能已经套了好几层）
    ⇒ 剩下的每一句都是**在某个 session 里找得到出处的原始中文**，⛔ 不再一层层套娃。"""
    work, out = list(body), []
    while work:
        t = work.pop(0)
        t = t.strip() if isinstance(t, str) else t
        if not t or RE_TRIG_STAMP.match(t):
            continue
        if t.startswith(TRIG_OLD_PREFIX):
            inner = t[len(TRIG_OLD_PREFIX):]
            if inner.endswith("）"):
                inner = inner[:-1]
            work = [x for x in inner.split(TRIG_OLD_SEP) if x.strip()] + work
            continue
        out.append(t)
    return out


def _norm_lines(seq):
    return [x.strip() for x in seq if x.strip()]


def _contains_run(hay, needle):
    """needle（归一化后）是不是 hay（归一化后）的一段连续子序列 —— 幂等判据。"""
    h, n = _norm_lines(hay), _norm_lines(needle)
    if not n:
        return False
    for i in range(len(h) - len(n) + 1):
        if h[i:i + len(n)] == n:
            return True
    return False


SKIP_LABEL = {"🎓": "🎓", "退池": "退池", "并入": "并入", "词组": "词组",
              "作文验": "作文验", "已是最新": "已是最新"}


def cmd_trigger(args):
    sess = args.session
    if not os.path.exists(sess):
        print("⛔ 找不到 session 文件：%s" % sess)
        return 2
    md = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(sess))
    if not md:
        print("⛔ session 文件名里读不出日期（要 sessions/YYYY-MM-DD.md）：%s" % sess)
        return 2
    sdate = md.group(1)
    sname = "sessions/" + os.path.basename(sess)
    gno = args.group
    slines = io.open(sess, encoding="utf-8").read().split("\n")

    rng = _slice_h2(slines, lambda x: x.startswith("## 复习 · 第 %d 组" % gno))
    if rng is None:
        print("⛔ %s 里没有「## 复习 · 第 %d 组」这一节" % (sname, gno))
        return 2
    a, b = rng
    parts = _sub_parts(slines, a, b)
    qp = _find_part(parts, ["题面"])
    mp = _find_part(parts, ["对应编号"])
    if qp is None:
        print("⛔ 组%d 里找不到「### 题面…」子件" % gno)
        return 2
    if mp is None:
        print("⛔ 组%d 里找不到「### 对应编号…」子件" % gno)
        return 2
    qbody = _first_fence_body(slines, qp[1], qp[2])
    mbody = _first_fence_body(slines, mp[1], mp[2])
    if qbody is None:
        print("⛔ 「### 题面…」里没有 ``` 围栏 —— 改 session，⛔ 不改脚本")
        return 2
    if mbody is None:
        print("⛔ 「### 对应编号…」里没有 ``` 围栏 —— 改 session，⛔ 不改脚本")
        return 2
    items, perr = _parse_numbered_items(qbody)

    print("═" * 74)
    print("drill.py trigger · %s 组%d" % (sname, gno))
    print("═" * 74)

    # ── 层 1：输入坏了 ⇒ ⛔ 整批不写 ─────────────────────────────────────
    hard = []
    if perr:
        hard.append(perr)
        items = {}
    # 只认**映射行**（行首就是 `k #…`）；围栏里的备注行（`⏸ 第二次调出：#0349（…）`）
    # 不是映射，⛔ 不参与数量核对（09-01 组6 就有这么一行）。
    map_lines = [l for l in mbody if RE_TRIG_MAPLINE.match(l)]
    mtext = "\n".join(map_lines)
    pairs = RE_TRIG_MAP.findall(mtext)
    all_nums_in_map = RE_TRIG_ANYNUM.findall(mtext)
    if not pairs:
        hard.append("「### 对应编号…」围栏里一对「题号 #编号」都读不出来")
    if len(pairs) != len(all_nums_in_map):
        hard.append("「### 对应编号…」里有 %d 个 #编号，却只读出 %d 对「题号 #编号」"
                    " —— 写法必须是 `k #NNNN`（⛔ 不做兜底）"
                    % (len(all_nums_in_map), len(pairs)))
    for ks, num in pairs:
        if not re.fullmatch(r"#\d{4}", num):
            hard.append("映射里的编号「%s」不是四位（§3.1 契约①）" % num)
    if items and pairs and len(pairs) != len(items):
        hard.append("映射 %d 对 ≠ 题面 %d 题 —— 数量对不上⛔不许部分搬运"
                    % (len(pairs), len(items)))

    ents = load_all()
    by_num = {}
    for e in ents:
        by_num.setdefault(e.num, []).append(e)

    plines, nl, ptext = _read_raw(PROBLEMS)

    seen_num, seen_k = {}, {}
    todo = []
    for ks, num in pairs:
        k = int(ks)
        tag = "组%d 第%d题 %s" % (gno, k, num)
        if num in seen_num:
            hard.append("%s 同一批里重复出现（上一次是第 %d 题）" % (tag, seen_num[num]))
            continue
        seen_num[num] = k
        if k in seen_k:
            hard.append("%s 题号 %d 在映射里出现了两次" % (tag, k))
            continue
        seen_k[k] = num
        if k not in items:
            hard.append("%s 题面围栏里没有第 %d 题" % (tag, k))
            continue
        if not _norm_lines(items[k]):
            hard.append("%s 第 %d 题的中文是空的" % (tag, k))
            continue
        got = by_num.get(num)
        if not got:
            hard.append("%s 全档查无此编号" % tag)
            continue
        if len(got) > 1:
            hard.append("%s 编号重复出现在 %s" % (tag, [f"{x.src}:{x.start}" for x in got]))
            continue
        todo.append((k, num, got[0], tag))

    for _k, _num, e, tag in todo:
        if e.src == "problems.md" and _entry_fence_unpaired(plines, e):
            hard.append("%s 条目里有**不配对的 ``` 围栏**（%s:%d–%d）—— "
                        "先把围栏补齐再搬；⛔ 不是历史记录的问题"
                        % (tag, e.src, e.start, e.end or 0))

    if hard:
        print("⛔ 输入有问题，%d 处 —— 一个字都没写（§0.3 整批不写）" % len(hard))
        for x in hard:
            print("ERROR  " + x)
        print("═" * 74)
        return 1

    # ── 层 2：条目不适用 ⇒ 逐条跳过，其余照常写 ──────────────────────────
    plan, skipped = [], []

    def skip(num, k, why, detail=""):
        skipped.append((num, k, why))
        print("  ⏸ %s  第%d题 —— 跳过：%s%s" % (num, k, why, ("　" + detail) if detail else ""))

    for k, num, e, tag in todo:
        if e.src != "problems.md" or e.state != "在池":
            why = ("🎓" if e.state == "🎓" else
                   "退池" if e.state == "退池" else
                   "并入" if str(e.state).startswith("并入") else str(e.state))
            skip(num, k, why,
                 "已出池的条目不会再被抽到，⛔ 不需要换题面（住 %s）" % e.src)
            continue
        if e.ask_kind == ASK_PHRASE:
            skip(num, k, "词组",
                 "词组题的触发点是【块】、不写句号（契约⑬）⇒ 整句题面不许写进去")
            continue
        span = _trigger_span(plines, e)
        if span is None:
            skip(num, k, "无触发点节", "条目里找不到 `**中文触发点**`，先补好再搬")
            continue
        head, cs, ce = span
        old_body = plines[cs:ce]
        new_body = list(items[k])
        if _contains_run(old_body, new_body):
            skip(num, k, "已是最新")
            continue
        kept = _strip_trig_wrappers(old_body)
        old_flat = TRIG_OLD_SEP.join(kept)
        old_line = (TRIG_OLD_PREFIX + old_flat + "）") if old_flat else ""
        warn_line = ("⚠️ **%s 换题面**（`drill.py trigger` 自动搬运，源：%s 组%d 第%d题）"
                     % (sdate, sname, gno, k))
        new_sec = new_body + [warn_line] + ([old_line] if old_line else [])
        plan.append(dict(num=num, k=k, e=e, head=head, cs=cs, ce=ce,
                         old=list(old_body), new=new_sec, new_body=list(new_body),
                         todo_flag=("待补" in old_flat)))

    def skip_summary():
        if not skipped:
            return
        c = Counter(w for _n, _k, w in skipped)
        print("⏸ 跳过 %d 条（%s）" % (len(skipped),
                                     " · ".join("%s %d" % (w, n) for w, n in sorted(c.items()))))

    if not plan:
        skip_summary()
        print("─" * 74)
        print("本组没有要改的条目 ⇒ 零改动（trigger 是幂等的）")
        print("═" * 74)
        return 0

    for p in plan:
        print("─" * 74)
        print("  %s  第%d题  problems.md L%d–%d" % (p["num"], p["k"], p["cs"] + 1, p["ce"]))
        print("    旧：")
        for l in p["old"]:
            print("      " + l)
        print("    新：")
        for l in p["new"]:
            print("      " + l)
    print("─" * 74)
    for p in plan:
        if p["todo_flag"]:
            print("WARN   %s 老触发点里带着「待补」两个字，压成一行后仍留在节里 ⇒ "
                  "这条在 stats／count 里仍会算「题面待补」，⛔ 脚本不代删，手工清" % p["num"])
    skip_summary()

    if args.dry_run:
        print("（--dry-run：⛔ 一个字都没写盘）")
        print("═" * 74)
        return 0

    # ── 写盘：从后往前替换，免得行号错位；⛔ 保留原文件的换行风格 ────────────
    blocks_before = _raw_blocks(plines)
    ents0 = load_all()
    err0 = _errmap(ents0, {x.num for x in ents0})
    snap0 = _statesnap(ents0)

    pre = []
    for p in plan:
        blk = blocks_before.get(p["num"])
        if blk is None or not (blk[0] < p["cs"] and p["ce"] <= blk[1]):
            pre.append("%s 的触发点区间落在条目块外面" % p["num"])
        if plines[p["cs"]:p["ce"]] != p["old"]:
            pre.append("%s 要替换的区间与读到的旧内容对不上" % p["num"])
        # 独立复核边界：块内 `**中文触发点**` 的下一行起、到第一个硬边界为止
        if blk is not None:
            body = plines[blk[0]:blk[1]]
            try:
                h = body.index("**中文触发点**")
            except ValueError:
                pre.append("%s 块里找不到 `**中文触发点**`" % p["num"])
                continue
            stop = len(body)
            for j in range(h + 1, len(body)):
                if body[j] in TRIG_HARD_BOUND or body[j].startswith("### "):
                    stop = j
                    break
            if not (blk[0] + h + 1 == p["cs"] and p["ce"] <= blk[0] + stop):
                pre.append("%s 触发点区间与独立复核算出来的边界不一致" % p["num"])
    spans = sorted((p["cs"], p["ce"]) for p in plan)
    for i in range(1, len(spans)):
        if spans[i][0] < spans[i - 1][1]:
            pre.append("两条的触发点区间重叠了：%s 与 %s" % (spans[i - 1], spans[i]))
    if pre:
        print("⛔ 写之前的区间自检没过，%d 处 —— 一个字都没写" % len(pre))
        for x in pre:
            print("ERROR  " + x)
        print("═" * 74)
        return 1

    out = list(plines)
    for p in sorted(plan, key=lambda x: -x["cs"]):
        out[p["cs"]:p["ce"]] = p["new"]
    new_text = nl.join(out)
    io.open(PROBLEMS, "w", encoding="utf-8", newline="").write(new_text)

    def rollback(why, detail):
        io.open(PROBLEMS, "w", encoding="utf-8", newline="").write(ptext)
        print("─" * 74)
        print("⛔ 写完自查不过：%s —— 已整批回滚，档案回到搬之前" % why)
        for d in detail[:20]:
            print("   " + d)
        print("═" * 74)
        return 1

    # ── 自校 ①字节级 ─────────────────────────────────────────────────
    if open(PROBLEMS, "rb").read() != new_text.encode("utf-8"):
        return rollback("写出去的字节与算出来的不一致", [])
    if ("\r\n" in ptext) != ("\r\n" in new_text):
        return rollback("换行风格被改了（CRLF ⇄ LF）", [])

    # ── 自校 ②块级（⛔ 不复用 _trigger_span）──────────────────────────
    after, _nl2, _t2 = _read_raw(PROBLEMS)
    blocks_after = _raw_blocks(after)
    if set(blocks_after) != set(blocks_before):
        lost = sorted(set(blocks_before) - set(blocks_after))
        extra = sorted(set(blocks_after) - set(blocks_before))
        return rollback("条目集合变了", ["丢了 " + x for x in lost] + ["多了 " + x for x in extra])
    changed = {p["num"]: p for p in plan}
    bad = []
    for num, (s0, e0_) in blocks_before.items():
        b0 = plines[s0:e0_]
        s1, e1_ = blocks_after[num]
        b1 = after[s1:e1_]
        p = changed.get(num)
        if p is None:
            if b0 != b1:
                bad.append("%s 没在本批里，正文却变了" % num)
            continue
        off = p["cs"] - s0
        if (b0[:off] != b1[:off]
                or b0[off + len(p["old"]):] != b1[off + len(p["new"]):]
                or b1[off:off + len(p["new"])] != p["new"]):
            bad.append("%s 除中文触发点以外的正文被动了" % num)
    if bad:
        return rollback("条目正文对不上（trigger 只许改中文触发点这一节）", sorted(bad))

    # ── 自校 ③语义级 ─────────────────────────────────────────────────
    ents1 = load_all()
    snap1 = _statesnap(ents1)
    bad_state = [n for n in snap0 if snap0[n] != snap1[n]]
    if bad_state:
        return rollback("有条目的状态字段变了（trigger ⛔ 不改状态/连对/连错/上次/族/题型）",
                        ["%s  %s  →  %s" % (n, snap0[n], snap1[n]) for n in sorted(bad_state)])
    idx1 = {e.num: e for e in ents1}
    notin = [p["num"] for p in plan
             if not _contains_run(idx1[p["num"]].trigger.split("\n"), p["new_body"])]
    if notin:
        return rollback("新题面没有逐字落进中文触发点", sorted(notin))
    err1 = _errmap(ents1, {e.num for e in ents1})
    new_errs = ["%s %s %s" % (n, lv, m) for (n, lv, m), c in (err1 - err0).items()]
    if new_errs:
        return rollback("多出 %d 处 check 报告" % len(new_errs), sorted(new_errs))

    print("✔ 已改 %d 条的中文触发点 · 除这一节外正文逐字节不变 · 换行风格不变 · "
          "状态字段不变 · check 无新增" % len(plan))
    print("  " + " ".join(p["num"] for p in plan))
    print("─" * 74)
    print("下一步：`drill.py check --changed`（§0.3）")
    print("═" * 74)
    return 0


# ══════════════════════════════════════════════════════════════════════════
# deliver —— 交付物完整性硬闸（SKILL §4③bc / §4④ / §4⑤e）
#
# 她 2026-08-30 定（方案 A）。原话：「我觉得你改不了，想想有没有别的方案」——
# 起因：交付物完整性这条规则只写在 skill 里，08-29 破一次（三版对照块发成 4 块片段）、
#       08-30 再破一次（回看只发动过的 5 块 ＋「其余全部未改」，还漏发两份全文）。
#       08-29 加过一条「发出前先数一遍」的散文钩子，存活不到 24 小时。
# ⇒ 结论：这一类只能上机器闸，⛔ 不许再加第三条散文钩子。
#
# ⛔ 本子命令【只读 session 文件 + 数数 + 打印】，不写任何文件、不产生任何内容。
# ══════════════════════════════════════════════════════════════════════════

# 节的锚点：section slug -> (## 标题匹配, 必需子件清单)
#   子件 = (人读的名字, 该子件的 ### 标题里必须出现的关键词 列表[任一命中即算有])
DELIVER_SPECS = {
    "组": {
        "head": None,  # 运行时用 "## 复习 · 第 N 组" 拼
        # ★ 条件性子件（§4③d③）：本节自己报了「新建 ≥1 条」才要求「新建条目的正文」
        "newborn": True,
        "parts": [
            ("题面",       ["题面"]),
            ("她的答案",   ["她的答案"]),
            ("a 判定表",   ["判定表"]),
            ("a 顺带判定", ["顺带判定"]),
            ("bc 三版对照块", ["三版对照块"]),
            ("d 战报",     ["战报"]),
        ],
    },
    # ★★ 复检组（§4③e，她 2026-09-05 定）——【必须登记在这里 ＋ KNOWN_H2】
    #    ⛔ 不登记的后果不是"漏查"而是**假绿**：`## 复检 · 第 N 组` 会被上一节整段吞掉，
    #       整节一个字都没查，硬闸照报 ERROR 0。
    #    与「组」的差别只有两条：
    #      · 三版对照块是**条件性**的 —— 判 ✅ 只记一行，判 ❌ 才走全套（复检快的全部理由）
    #      · 块数守恒对的是**战报里声明的 ❌ 条数**，⛔ 不是本组题数
    "复检组": {
        "head": None,   # 运行时用 "## 复检 · 第 N 组" 拼
        "newborn": True,
        "recheck": True,
        "parts": [
            ("题面",       ["题面"]),
            ("她的答案",   ["她的答案"]),
            ("a 判定表",   ["判定表"]),
            ("a 顺带判定", ["顺带判定"]),
            ("bc 三版对照块", ["三版对照块"]),
            ("d 战报",     ["战报"]),
        ],
    },
    "回看": {
        "head": "## 回看",
        "parts": [
            ("题面与条件",     ["题面", "出题"]),
            ("她的原文",       ["她的原文", "逐句编号", "原文"]),
            ("三版对照块",     ["三版对照块"]),
            ("最小修改版全文", ["最小修改版全文", "最小修改版"]),
            ("更好版全文",     ["更好版全文", "更好版"]),
        ],
    },
    "新题": {
        "head": "## 新题",
        # ★ 条件性子件（§4⑤e 一并发 → §4③d③ 同一条口径）
        "newborn": True,
        "parts": [
            ("题面与条件",     ["题面", "出题"]),
            ("她的原文",       ["她的原文", "逐句编号", "原文"]),
            ("收稿",           ["收稿"]),
            ("判分",           ["判分"]),
            ("对照 problems",  ["对照 problems", "对照"]),
            ("三版对照块",     ["三版对照块"]),
            ("最小修改版全文", ["最小修改版全文", "最小修改版"]),
            ("更好版全文",     ["更好版全文", "更好版"]),
        ],
    },
    "追加练": {
        "head": "## 追加练",
        "parts": [
            ("允许集", ["允许集"]),
            ("找点",   ["找点"]),
            ("三闸",   ["三闸"]),
            ("重数",   ["重数"]),
        ],
    },
}

# 追加练：每个 #A<n> 块里必须齐的行（label 是行首 strip 后的前缀）
FOLLOWUP_ASK_LINES = ["原句", "出处", "要求", "目标量"]      # 出题档就要齐
FOLLOWUP_JUDGE_LINES = ["实际量", "判定"]                    # 判定档追加要齐
FOLLOWUP_ANS_LINES = ["她的答案", "练档答案"]                # 二选一必须有其一
RE_FU_HEAD   = re.compile(r"^#(A\d+)\s*$")
RE_FU_PLAN   = re.compile(r"计划\s*(\d+)\s*题")
RE_FU_TARGET = re.compile(r"(\d+)\s*(?:→|->|—>)\s*[~约]?\s*(\d+)\s*词")
RE_FU_ACTUAL = re.compile(r"(\d+)\s*(?:→|->|—>)\s*(\d+)\s*词")

# 块内必须齐的五行（label 是行首 strip 后的前缀）
BLOCK_LINES = [
    ("原句",       "原句"),
    ("最小修改",   "最小修改"),
    ("└ 改了什么", "└ 改了什么"),
    ("更好版",     "更好版"),
    ("└ 为什么好", "└ 为什么好"),
]

# 摘要句黑名单 —— 只在【三版对照块】子件里查（别处出现是记录，不是交付物）
DELIVER_BLACKLIST = [
    "其余全部未改", "其余均未改", "其余略", "以下略", "余下略",
    "其余同上", "不再逐一", "其余各句均", "其余各题均", "略去",
]

# ★ 两条日期线（与 check 的存量提示同一个设计）：更早的写法列为「存量提示」，⛔ 不报错
#   2026-08-23  她定下三版对照块，取代旧的「最小修改版／更好版／diff 表A／表B」四份
#   2026-08-30  她定下回看／新题的交付件清单（含最小修改版全文 ＋ 更好版全文）
DELIVER_FLOOR_BLOCKS = "2026-08-23"
DELIVER_FLOOR_NODES  = "2026-08-30"
#   2026-09-02 她定：复习组的「顺带判定」进必查件（§4③a 本来就写着它是交付内容）。
#     更早的写法把它写成正文里的 `**顺带判定**`（08-30 就是）⇒ 列为存量提示，⛔ 不报错。
DELIVER_FLOOR_INCIDENT = "2026-09-02"
#   2026-09-03 她定：**新建条目的正文**进必查件（§4③d③ 白纸黑字：⛔ 只写「新建 #0267」＝ 没交付）。
#     起因：09-03 的作文节里教练只做了「对照」、⛔ 没建条目，8 件全齐 ⇒ 硬闸照样 ERROR 0。
#     ★ 这一件是**条件性**的：只有本节自己报了「新建 ≥1 条」才要求；报 0 条／没报 ⇒ ⛔ 不适用。
DELIVER_FLOOR_NEWBORN = "2026-09-03"
# 这天起「本节跳过」是唯一合法写法；更早的 session 还认那两个松写法（08-20 用过）
DELIVER_FLOOR_SKIP = "2026-09-05"

# 「新建条目的正文」子件的标题关键词（与其它子件同一个匹配方式：某一【段】以它开头）
NEWBORN_KWS = ["新建条目", "新建的条目",
               "本组新建条目", "本组新建的条目",
               "本篇新建条目", "本篇新建的条目",
               "本节新建条目", "本节新建的条目"]
# 「报了新建 N 条」的行：⛔ 严格匹配、不兜底 —— `新建　N 条` ／ `本组新建  N 条` ／ `新建 N 条：#0415 …`
RE_NEW_DECL = re.compile(r"新建[\s\u3000]*\d+\s*条")
# 复检组战报里的四行（§4③e）——⛔ 严格匹配，写歪了改 session，不改脚本
RE_RC_SIZE = re.compile(r"^本组[\s\u3000]*(\d+)[\s\u3000]*题[\s\u3000]*/[\s\u3000]*(\d+)[\s\u3000]*条")
RE_RC_OK   = re.compile(r"^本组[\s\u3000]*✅[\s\u3000]*(\d+)[\s\u3000]*条")
RE_RC_BAD  = re.compile(r"^本组[\s\u3000]*❌[\s\u3000]*(\d+)[\s\u3000]*条")
RE_RC_FALL = re.compile(r"^本组回潮[\s\u3000]*(\d+)[\s\u3000]*条")
RE_NEW_NUM  = re.compile(r"#(\d{4})")


def _declared_new(lines, a, b):
    """本节自己报的「新建 N 条」→ (N, [声明的编号…], 行下标)。
    取**第一条**这样的行：N ＝ 该行里的第一个整数，编号 ＝ 该行里所有 `#dddd`。
    ⛔ 找不到这样的行 ⇒ (0, [], -1) ⇒ 这一条不适用、⛔ 不报错（不兜底、不猜）。"""
    for i in range(a, b):
        if RE_NEW_DECL.search(lines[i]):
            m = re.search(r"\d+", lines[i])
            return (int(m.group(0)) if m else 0), RE_NEW_NUM.findall(lines[i]), i
    return 0, [], -1

# ★★ 已知顶层节全集 —— 全脚本唯一一处「一个 ## 节到哪儿为止」的定义（她 2026-09-02 定）。
#    此前只有追加练用它，回看／新题各写各的 stops ⇒ 回看不在 `## 教练侧` `## 收尾` 处收口，
#    结果「回看缺更好版全文」被 `## 收尾` 里的 `### 更好版 · 收尾复盘` 顶掉、硬闸报 ERROR 0。
#    ⇒ 现在**所有节**都在这一集合处收口，⛔ 不再各写各的。
#  ⚠️ 新加一种 `## 节` 一定要登记进来 —— 不登记 ＝ 它被上一节吞掉、整节不查、硬闸假绿
KNOWN_H2 = ("开场", "复习 ·", "复检 ·", "回看", "新题", "教练侧", "收尾", "追加练")


RE_TBL_CELL = re.compile(r"^#\d{4}$")


def _table_judgements(lines, found):
    """从本节「判定表」子件里逐行读出 {编号: {符号…}}。

    ⛔ 这是复检那套降档（✅ 只记一行 / ❌ 才走全套）**唯一可信的读数来源** ——
       战报里那几个数是教练手打的，⛔ 不能拿它当真源（2026-09-05 对抗演练实证：
       判定表里明写 ❌、战报写 ❌ 0 条、块也不写 ⇒ 硬闸照报 ERROR 0）。
    认法：markdown 表格行，某一格恰好是 `#NNNN`，**紧邻的下一格**是 §3.2 的判定符号。
    ⛔ 严格匹配、不兜底：符号写歪／加粗 ⇒ 这一行读不出来 ⇒ 下面按"漏判"报错。"""
    out = {}
    tp = found.get("a 判定表") or found.get("判定表")
    if tp is None:
        return out
    _t, ts, te = tp
    for i in range(ts, te):
        ln = lines[i]
        if "|" not in ln:
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        for k, c in enumerate(cells[:-1]):
            if RE_TBL_CELL.match(c) and cells[k + 1] in JUDGE:
                out.setdefault(c, set()).add(cells[k + 1])
    return out


def _declared_recheck(lines, a, b, parts, found):
    """复检组战报里的四行（§4③e）。返回 (dict, errs)。

    ⛔ 严格匹配、不兜底：`本组 N 题 / K 条`『本组 ✅ N 条』『本组 ❌ N 条』『本组回潮 N 条』。
    ★ 「❌ 数」是块数守恒的**唯一来源** —— 复检判 ✅ 只记一行、⛔ 不给三版对照块。
    ★ 「回潮数 ＝ ❌ 数」是硬不变量：🎓 吃到 ❌ ⇒ 当场回潮（§3.3），
      判了 ❌ 却没回潮 ＝ 状态行忘了改，这正是最容易漏的一步。"""
    wp = found.get("d 战报")
    errs = []
    got = {}
    if wp is None:
        return got, ["缺「战报」子件 ⇒ 数不出 ❌ 条数（§4③e 战报四行）"]
    _t, ws, we = wp
    pat = [("size", RE_RC_SIZE, "本组 N 题 / K 条"),
           ("ok", RE_RC_OK, "本组 ✅ N 条"),
           ("bad", RE_RC_BAD, "本组 ❌ N 条"),
           ("fall", RE_RC_FALL, "本组回潮 N 条")]
    nums = []
    for key, rx, shape in pat:
        hit = None
        for i in range(ws, we):
            m = rx.match(lines[i].strip())
            if m:
                hit = (m, i)
                break
        if hit is None:
            errs.append("战报缺「%s」这一行（§4③e，⛔ 严格这个写法）" % shape)
        else:
            m, i = hit
            got[key] = int(m.group(2) if key == "size" else m.group(1))
            if key in ("ok", "bad", "fall"):
                got[key + "_nums"] = RE_NEW_NUM.findall(lines[i])
    # ── 与【判定表】对账（2026-09-05 补）：战报的数只是**声明**，判定表才是读数 ──
    tbl = _table_judgements(lines, found)
    if not tbl:
        errs.append("「判定表」里一行都读不出来 —— 每行要有 `| #NNNN |` 紧跟一格 §3.2 的判定符号"
                    "（⛔ 符号不加粗、不写「稳／掉」）")
    else:
        t_bad = {n for n, syms in tbl.items() if any(JUDGE[x] == "bad" for x in syms)}
        t_ok = {n for n, syms in tbl.items()
                if n not in t_bad and any(JUDGE[x] == "ok" for x in syms)}
        for key, want, shape in (("bad", t_bad, "❌"), ("ok", t_ok, "✅")):
            if key not in got:
                continue
            nums = {"#" + x for x in got.get(key + "_nums", [])}
            if nums != want:
                errs.append("战报「本组 %s %d 条」与**判定表**对不上：判定表判 %s 的是 %s，"
                            "战报写的是 %s —— 战报的数是手打的，判定表才是读数（§4③e）"
                            % (shape, got[key], shape,
                               " ".join(sorted(want)) or "（无）",
                               " ".join(sorted(nums)) or "（没列编号）"))
            elif len(nums) != got[key]:
                errs.append("战报报了「%s %d 条」，同一行却列了 %d 个编号 —— §0.4 数与编号清单要对得上"
                            % (shape, got[key], len(nums)))
        if "fall" in got:
            fall = {"#" + x for x in got.get("fall_nums", [])}
            if fall != t_bad:
                errs.append("战报「本组回潮 %d 条」与判 ❌ 的那几条对不上：判 ❌ 的是 %s，"
                            "回潮写的是 %s —— 🎓 吃到 ❌ 就要当场回潮（§3.3），"
                            "这一行的编号就是「哪几条要改状态行」的凭据"
                            % (got["fall"], " ".join(sorted(t_bad)) or "（无）",
                               " ".join(sorted(fall)) or "（没列编号）"))
            elif len(fall) != got["fall"]:
                errs.append("战报报了「回潮 %d 条」，同一行却列了 %d 个编号（§0.4）"
                            % (got["fall"], len(fall)))
    return got, errs


def _node_end(lines, a, known=KNOWN_H2):
    """节 [a, ?) 的右边界 ＝ 下一个【已知顶层节】的 ## 标题；没有就到文件末。"""
    for j in range(a + 1, len(lines)):
        if lines[j].startswith("## ") and any(
                lines[j].startswith("## " + k) for k in known):
            return j
    return len(lines)


def _outer_fence(body):
    """这一块在 session 里**外层**是不是已经包在 code 围栏里了（只看第一个非空行）。
    ⛔ 不能用「任一行 startswith ```」—— 块内出现围栏会被误判成"已带围栏"、整节不加围栏。"""
    for l in body:
        if l.strip():
            return l.startswith("```")
    return False

RE_BLOCK_HEAD = re.compile(r"^#(S?\d+[a-z]?)\s*$")
RE_NUM_ITEM   = re.compile(r"^\s*(\d+)\.\s")
RE_SENT_ID    = re.compile(r"^S(\d+)\s")
RE_TOTAL_SENT = re.compile(r"共\s*(\d+)\s*句")


def _slice_h2(lines, head_pred):
    """取出一个 ## 节的行区间 [a,b)。找不到返回 None。"""
    a = None
    for i, ln in enumerate(lines):
        if ln.startswith("## ") and head_pred(ln):
            a = i
            break
    if a is None:
        return None
    for j in range(a + 1, len(lines)):
        if lines[j].startswith("## "):
            return (a, j)
    return (a, len(lines))


def _sub_parts(lines, a, b, h2_too=False):
    """把节切成子件：[(标题行, s, e), …]。节首到第一个标题之间算 '(节首)'。
    h2_too=True 时 ## 级标题也算子件 —— 新题这条路历史上把判分/对照/三版对照块写成了 ##。"""
    if h2_too:
        idx = [i for i in range(a, b) if lines[i].startswith("### ") or (lines[i].startswith("## ") and i != a)]
    else:
        idx = [i for i in range(a, b) if lines[i].startswith("### ")]
    out = []
    if not idx:
        return [("(节首)", a, b)]
    if idx[0] > a + 1:
        out.append(("(节首)", a, idx[0]))
    for k, i in enumerate(idx):
        e = idx[k + 1] if k + 1 < len(idx) else b
        out.append((lines[i], i, e))
    return out


RE_LABEL = re.compile(r"^(?:[a-zA-Z]{1,3}\s*[·．.]?\s*){0,3}")


def _title_segments(title):
    """把 ### 标题拆成可比对的段：去掉 ### 前缀、按 · ／ ＋ （ 切开、剥掉 a/b/bc/d/e 这类短标号。"""
    t = title
    for pre in ("### ", "## "):
        if t.startswith(pre):
            t = t[len(pre):]
            break
    t = t.strip()
    segs = re.split(r"[·・／/＋+（(]", t)
    out = [t]   # 整条标题也算一段（`### 最小修改版 · 全文` 这种）

    for seg in segs:
        seg = seg.strip().lstrip("★⚠️🔴📒 ")
        if not seg:
            continue
        out.append(seg)
        stripped = RE_LABEL.sub("", seg).strip()
        if stripped and stripped != seg:
            out.append(stripped)
    return out


def _find_part(parts, keywords):
    """⛔ 严格：标题的某一【段】必须以关键词开头，不是"标题里出现过这几个字"。
    （否则 `### 手工件② · 中文题面自译落点` 会被当成「题面」—— 08-27 组1 就是这么误报的）"""
    for title, s, e in parts:
        for seg in _title_segments(title):
            if any(seg.startswith(k) for k in keywords):
                return (title, s, e)
    return None


# ⛔ **只认「本节跳过」这四个字**（2026-09-05 收紧）。
#    旧写法还认松散的 `⇒ 跳过`：只要节的**前 20 行**里出现那三个字
#    （哪怕是在讲别的事），整节就不查、还报 ERROR 0 —— 闸在它唯一要防的场景上给假绿。
#    ⚠️ 存量放行：`按 §4④「D-1 没写新题就跳过」` 是 08-20 那场真的用过的写法
#    （那条规则本身 09-03 已废），⛔ 只对这个日期线之前的 session 认。
RE_SKIP = re.compile(r"本节跳过")
RE_SKIP_LEGACY = re.compile(r"(⇒\s*\*?\*?跳过|按 §4④「D-1 没写新题就跳过」)")


def _blocks_in(lines, s, e):
    """在区间里找三版对照块：返回 [(编号, 起, 止)]。块头必须顶格 `#N` / `#SN`。"""
    heads = []
    for i in range(s, e):
        m = RE_BLOCK_HEAD.match(lines[i])
        if m:
            heads.append((m.group(1), i))
    out = []
    for k, (nid, i) in enumerate(heads):
        end = heads[k + 1][1] if k + 1 < len(heads) else e
        out.append((nid, i, end))
    return out


def _wc_en(t):
    """数英文词：只认含字母或数字的 token。"""
    return len([x for x in t.split() if re.search(r"[A-Za-z0-9]", x)])


def _fu_fence_mask(lines, a, b):
    """标出 [a,b) 里哪些行在 ``` 围栏内。"""
    inside, mask = False, {}
    for i in range(a, b):
        t = lines[i].lstrip()
        if t.startswith("```"):
            mask[i] = True
            inside = not inside
            continue
        mask[i] = inside
    return mask


def _fu_blocks(lines, a, b):
    """取出 [a,b) 里顶格、非围栏内的 #A<n> 块。
    块的终点 = 下一个块头 ／ 下一个 ### 标题 ／ b，三者取最近。
    另返回「长得像块头却没解析出来」的行号，交给调用方报错。"""
    mask = _fu_fence_mask(lines, a, b)
    heads, bad = [], []
    for i in range(a, b):
        if mask.get(i):
            continue
        ln = lines[i]
        if RE_FU_HEAD.match(ln):
            heads.append((RE_FU_HEAD.match(ln).group(1), i))
        elif ln.lstrip().startswith("#A") and not ln.startswith("#A"):
            bad.append(i)
        elif ln.startswith("#A") and not RE_FU_HEAD.match(ln):
            bad.append(i)
    out = []
    for k, (bid, i) in enumerate(heads):
        stop = heads[k + 1][1] if k + 1 < len(heads) else b
        for j in range(i + 1, stop):
            if lines[j].startswith("### ") and not mask.get(j):
                stop = j
                break
        out.append((bid, i, stop))
    return out, bad


def _fu_split_body(body):
    """块体切成【块级行】与【三版对照块行】两段；没有那一行标记返回 (body, None)。"""
    for k, ln in enumerate(body):
        if "三版对照块" in ln:
            return body[:k], body[k + 1:]
    return body, None


def _fu_val(body, prefix):
    """块体里以 prefix 开头的第一行，返回它后面的值（没有返回 None）。
    ★ 标签后面必须紧跟空白／全角空格／冒号，⛔ 否则「要求逐条对」会顶掉「要求」。"""
    for ln in body:
        t = ln.strip()
        if not t.startswith(prefix):
            continue
        rest = t[len(prefix):]
        if rest and rest[0] not in " \t\u3000：:":
            continue
        return rest.strip(" \t\u3000：:")
    return None


def _check_followup(lines, a, b, found, whole):
    """§4.8 追加练：返回 (errs, notes)。脚本只读、只数、只报错，⛔ 不产生内容。"""
    errs, notes = [], []

    # 头一行（入口A 写「扣分项：…」／入口B 写「入口B …」）＋ 计划题数，必须同一行
    plan = None
    head_line = None
    for i in range(a, b):
        t = lines[i].lstrip()
        if t.startswith("扣分项：") or t.startswith("入口B"):
            head_line = lines[i]
            break
    if head_line is None:
        errs.append("缺头一行 ——「扣分项：X（命中第 N 条）」或「入口B …」（§4.8 S1）")
    else:
        mp = RE_FU_PLAN.search(head_line)
        if not mp:
            errs.append("「扣分项：」那一行里没有「计划 N 题」（§4.8 S1／S4，两样必须同一行）")
        else:
            plan = int(mp.group(1))
            if plan < 1:
                errs.append("「计划 %d 题」不合法 —— 必须 ≥ 1" % plan)
                plan = None

    # 三闸三行齐
    tp = found.get("三闸")
    if tp:
        _, ts, te = tp
        ttxt = "\n".join(lines[ts:te])
        for g in ("闸1", "闸2", "闸3"):
            if g not in ttxt:
                errs.append("三闸缺「%s」这一行（§4.8 S6）" % g)

    blocks, bad = _fu_blocks(lines, a, b)
    for i in bad:
        errs.append("L%d 长得像题块头却解析不出来 ——「#A<数字>」必须顶格、独占一行：%s"
                    % (i + 1, lines[i].strip()[:40]))
    # 节外的 #A 块（被 ## 标题截断的）
    others = [i for i, ln in enumerate(whole) if ln.startswith("## 追加练") and i != a]
    lim = min([x for x in others if x > a] or [len(whole)])
    stray = [i for i in range(a, lim) if whole[i].startswith("#A") and not (a <= i < b)]
    if stray:
        errs.append("节外还有 %d 个 #A 块（L%s）—— 中间插了 `## ` 标题把节截断了，把它们挪进 ## 追加练"
                    % (len(stray), ",".join(str(i + 1) for i in stray[:5])))
    if not blocks:
        errs.append("一个 #A<n> 题块都没有（§4.8 S5）")
        return errs, notes

    seen = {}
    for bid, i, _e in blocks:
        if bid in seen:
            errs.append("题号 #%s 重复（L%d 与 L%d）" % (bid, seen[bid] + 1, i + 1))
        seen[bid] = i

    live = []   # 非作废块
    for bid, s_, e_ in blocks:
        head, _tail = _fu_split_body(lines[s_ + 1:e_])
        if _fu_val(head, "作废") is None:
            live.append(bid)
    if not live:
        errs.append("全部 %d 块都标了「作废」—— 本轮一题都没实练（§4.8）" % len(blocks))

    # 档位：最后一个【非作废】块有没有答案
    last_live_has_ans = False
    last_live_id = live[-1] if live else None
    for bid, s_, e_ in reversed(blocks):
        head, _t = _fu_split_body(lines[s_ + 1:e_])
        if _fu_val(head, "作废") is not None:
            continue
        last_live_has_ans = any(_fu_val(head, x) is not None for x in FOLLOWUP_ANS_LINES)
        break
    n_live = len(live)
    if not last_live_has_ans:
        stage = "出题"
    elif plan is not None and n_live >= plan:
        stage = "收官"
    else:
        stage = "判定"
    notes.append("档位 = %s 档（实练 %d 块／作废 %d 块%s）"
                 % (stage, n_live, len(blocks) - n_live,
                    "／计划 %d" % plan if plan is not None else ""))
    if plan is not None and n_live > plan:
        errs.append("实练题块 %d 多于「计划 %d 题」—— 改计划或删块（§4.8 S4）" % (n_live, plan))
    if plan is not None and n_live < plan and last_live_has_ans and stage != "出题":
        errs.append("实练题块 %d 少于「计划 %d 题」且已全部判完 —— 补出剩下的题或改计划（§4.8 S4）"
                    % (n_live, plan))

    for bid, s_, e_ in blocks:
        body = lines[s_ + 1:e_]
        head, blk = _fu_split_body(body)
        is_last_live = (bid == last_live_id)
        need_judge = not (is_last_live and stage == "出题")

        # 作废的题：只要求 原句／要求／作废理由，⛔ 其余全部不查，也不计入计划
        void = _fu_val(head, "作废")
        if void is not None:
            if not void:
                errs.append("#%s 标了「作废」但没写理由" % bid)
            else:
                notes.append("#%s 作废 ⇒ ⛔ 不查判定与词数，也不计入计划" % bid)
            for lab in ("原句", "要求"):
                if _fu_val(head, lab) is None:
                    errs.append("#%s 缺「%s」这一行" % (bid, lab))
            continue

        for lab in FOLLOWUP_ASK_LINES:
            v = _fu_val(head, lab)
            if v is None:
                errs.append("#%s 缺「%s」这一行（§4.8 S5 四件）" % (bid, lab))
            elif not v:
                errs.append("#%s 的「%s」是空的" % (bid, lab))
        if not need_judge:
            continue

        for lab in FOLLOWUP_JUDGE_LINES:
            v = _fu_val(head, lab)
            if v is None:
                errs.append("#%s 缺「%s」这一行（§4.8 S8）" % (bid, lab))
            elif not v:
                errs.append("#%s 的「%s」是空的" % (bid, lab))
        ans_lab = None
        for x in FOLLOWUP_ANS_LINES:
            if _fu_val(head, x) is not None:
                ans_lab = x
                break
        if ans_lab is None:
            errs.append("#%s 缺「她的答案」／「练档答案」（§4.8 S8，二选一必须有其一）" % bid)
        elif not _fu_val(head, ans_lab):
            errs.append("#%s 的「%s」是空的" % (bid, ans_lab))

        # 三版对照块：必须有那一行标记 ＋ 五行齐 ＋ 非空
        if blk is None:
            errs.append("#%s 里没有「三版对照块」这一行标记（§4.8 S8）" % bid)
        else:
            for name, prefix in BLOCK_LINES:
                v = _fu_val(blk, prefix)
                if v is None:
                    errs.append("#%s 缺三版对照块的「%s」这一行（§4.8 S8）" % (bid, name))
                elif not v:
                    errs.append("#%s 三版对照块的「%s」是空的" % (bid, name))

        # 「不会」⇒ 必须有练档答案
        jd = _fu_val(head, "判定") or ""
        if "不会" in jd and _fu_val(head, "练档答案") is None:
            errs.append("#%s 的判定里出现「不会」，但没有「练档答案」这一行（§4.8 S9）" % bid)

        # 量：目标量必须是【词】或【处】两种写法之一
        tgt = _fu_val(head, "目标量") or ""
        act = _fu_val(head, "实际量") or ""
        mt = RE_FU_TARGET.search(tgt)
        if not mt:
            if "处" in tgt:
                mtp = re.search(r"(\d+)\s*处", tgt)
                map_ = re.search(r"(\d+)\s*处", act)
                if not mtp or not map_:
                    errs.append("#%s 的目标量／实际量读不出「N 处」（§4.8 S4）" % bid)
                else:
                    t_n, a_n = int(mtp.group(1)), int(map_.group(1))
                    if a_n <= 0:
                        errs.append("#%s 实际 0 处 —— ⛔ 这一题没达成目的（§4.8 S8）" % bid)
                    elif a_n < t_n:
                        notes.append("WARN #%s 实际 %d 处 < 目标 %d 处 —— 处置写进 session"
                                     % (bid, a_n, t_n))
                    else:
                        notes.append("#%s %d 处（目标 %d 处）" % (bid, a_n, t_n))
            else:
                errs.append("#%s 的「目标量」不合法 —— 只许两种写法：`N → ~M 词` 或 `N 处`（§4.8 S4）"
                            % bid)
            continue

        t_from, t_to = int(mt.group(1)), int(mt.group(2))
        src = _fu_val(head, "原句")
        ans = _fu_val(head, ans_lab) if ans_lab else None
        if src is None or ans is None:
            continue
        n_src, n_ans = _wc_en(src), _wc_en(ans)
        delta = n_ans - n_src
        pairs = RE_FU_ACTUAL.findall(act)
        if not pairs:
            errs.append("#%s 的「实际量」里读不出 `N → M 词`（脚本数出来是 %d → %d 词；"
                        "答案必须写成一行）" % (bid, n_src, n_ans))
        elif (str(n_src), str(n_ans)) not in [(x, y) for x, y in pairs]:
            errs.append("#%s 实际量对不上：session 写的是 %s，脚本数出来是 %d → %d 词"
                        "（答案必须写成一行）"
                        % (bid, "／".join("%s → %s" % pr for pr in pairs), n_src, n_ans))
        if delta <= 0:
            errs.append("#%s 净增量 %+d 词（%s）—— ⛔ 这一题没达成目的；"
                        "要么改题重出，要么在块里写一行「作废　<理由>」（§4.8 S8）"
                        % (bid, delta, ans_lab))
        elif n_ans < t_to:
            notes.append("WARN #%s 实际 %d 词 < 目标 %d 词（净 %+d，目标 %+d）—— 处置写进 session"
                         % (bid, n_ans, t_to, delta, t_to - t_from))
        else:
            notes.append("#%s 词数 %d → %d（净 %+d，目标 %+d）"
                         % (bid, n_src, n_ans, delta, t_to - t_from))

    return errs, notes


def _deliver_scan(args, path, lines):
    """跑硬闸并打印报告 → (rc, sections)。
    sections = [dict(slug, label, a, b, parts, found)]，供 `--emit` 复用同一份切节结果。
    ⛔ 只读、只数、只打印。"""
    sections = []
    md = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(path))
    sdate = md.group(1) if md else "9999-99-99"
    legacy_blocks = sdate < DELIVER_FLOOR_BLOCKS
    legacy_nodes = sdate < DELIVER_FLOOR_NODES

    # ★★ 全部交付节一律**按行号**切（她 2026-09-02 定）：同名节可以有多个 ——
    #    回看（本周期两篇新题都要回看）、追加练（各带标签）、
    #    甚至同一个「## 复习 · 第 N 组」写了两次（此前对着第一节查两遍、emit 也吐两遍）。
    wanted = []
    if args.all or not args.section:
        for i, ln in enumerate(lines):
            if re.match(r"^## 复习 · 第 \d+ 组", ln):
                wanted.append("组@%d" % i)
            if re.match(r"^## 复检 · 第 \d+ 组", ln):
                wanted.append("复检组@%d" % i)
        # 回看／追加练：**可多个**（§0.9a §4.8）⇒ 逐节都查
        for kind in ("回看", "追加练"):
            for i, ln in enumerate(lines):
                if ln.startswith("## " + kind):
                    wanted.append("%s@%d" % (kind, i))
        # 新题：§9 一天**只有一篇**⇒ 只认第一个 `## 新题`；后面的 `## 新题 · b 收稿`
        #   这种是同一篇的续节（08-29 就是），⛔ 不能当成第二个新题节
        for i, ln in enumerate(lines):
            if ln.startswith("## 新题"):
                wanted.append("新题@%d" % i)
                break
    else:
        mg = re.match(r"^组(\d+)$", args.section or "")
        mr = re.match(r"^复检(\d+)$", args.section or "")
        if mg:
            head = "## 复习 · 第 %s 组" % mg.group(1)
            wanted = ["组@%d" % i for i, ln in enumerate(lines) if ln.startswith(head)]
            if not wanted:
                wanted = ["组@-1"]
        elif mr:
            head = "## 复检 · 第 %s 组" % mr.group(1)
            wanted = ["复检组@%d" % i for i, ln in enumerate(lines) if ln.startswith(head)]
            if not wanted:
                wanted = ["复检组@-1"]
        elif args.section in ("回看", "新题", "追加练"):
            pre = args.section
            wanted = ["%s@%d" % (pre, i) for i, ln in enumerate(lines)
                      if ln.startswith("## " + pre)]
            if pre == "新题":
                wanted = wanted[:1]                  # §9 一天只有一篇新题
            if not wanted:
                wanted = ["%s@-1" % pre]
        else:
            wanted = [args.section]

    if not wanted:
        print("⛔ 这个文件里没有可查的交付节"
              "（复习 · 第 N 组 ／ 复检 · 第 N 组 ／ 回看 ／ 新题 ／ 追加练）")
        return 2, sections

    print("═" * 74)
    print("drill.py deliver · 交付物完整性硬闸 · %s" % path)
    print("   ⛔ ERROR > 0 ⇒ 不许发（SKILL §4③bc / §4④ / §4⑤e / §4.8）")
    print("═" * 74)

    total_err = 0
    total_warn = 0
    for slug in wanted:
        errs = []
        notes = []
        warns = []
        mm = re.match(r"^(组|复检组|回看|新题|追加练)@(-?\d+)$", slug)
        if mm:
            slug, a0 = mm.group(1), int(mm.group(2))
            spec = DELIVER_SPECS[slug]
            rng = None if a0 < 0 else (a0, _node_end(lines, a0))
            label = ("%s（L%d）" % (lines[a0].lstrip("# ").strip(), a0 + 1)
                     if rng else slug)
        elif slug in DELIVER_SPECS:
            spec = DELIVER_SPECS[slug]
            rng = _slice_h2(lines, lambda x, h=spec["head"]: x.startswith(h))
            if rng:
                rng = (rng[0], _node_end(lines, rng[0]))
            label = slug
        else:
            print("⛔ 不认识的 --section：%s（用 组N ／ 复检N ／ 回看 ／ 新题 ／ 追加练）" % slug)
            return 2, sections

        print("")
        print("── %s ──" % label)
        if rng is None:
            print("   ERROR  节不存在 —— 找不到这一节的 ## 标题")
            total_err += 1
            continue
        a, b = rng
        # 新题这条路历史上把 判分／对照／记账 写在 `## 收尾` 之后（08-20 就是）——
        # 那是 DELIVER_FLOOR_NODES 之前的旧写法，只对存量放行，⛔ 新 session 一律在已知顶层节收口。
        h2_too = slug in ("新题", "回看")
        if slug == "新题" and legacy_nodes:
            b = len(lines)
        parts = _sub_parts(lines, a, b, h2_too=h2_too)

        # 声明跳过的节（§4④ D-1 没写新题就跳过）⇒ 不查。⛔ 追加练不吃这条
        head_txt = "\n".join(lines[a:min(a + 20, b)])
        skipped = RE_SKIP.search(head_txt) or (
            sdate < DELIVER_FLOOR_SKIP and RE_SKIP_LEGACY.search(head_txt))
        if slug != "追加练" and skipped:
            print("   SKIP   本节已声明跳过（§4④），⛔ 不查")
            continue

        # ★ §4.8 追加练：走自己的一套检查，⛔ 不套用组／回看／新题的块数守恒与战报
        if slug == "追加练":
            parts = _sub_parts(lines, a, b)          # b 已由 _node_end 收口
            found = {}
            for name, kws in spec["parts"]:
                found[name] = _find_part(parts, kws)
            hl = ""
            for i in range(a, b):
                t = lines[i].lstrip()
                if t.startswith("扣分项：") or t.startswith("入口B"):
                    hl = lines[i]
                    break
            if found.get("允许集") is None:
                if "入口B" in hl:
                    notes.append("允许集：本场走入口B ⇒ ⛔ 不查")
                else:
                    errs.append("缺子件「允许集」（§4.8 S2；走入口B 时把「入口B」写在【扣分项那一行】）")
            for name in ("找点", "三闸"):
                if found.get(name) is None:
                    errs.append("缺子件「%s」（§4.8）" % name)
            e2, n2 = _check_followup(lines, a, b, found, lines)
            errs.extend(e2)
            notes.extend(n2)
            is_final = any(x.startswith("档位 = 收官") for x in n2)
            if found.get("重数") is None:
                if is_final:
                    errs.append("缺子件「重数」（§4.8 S11）")
                else:
                    notes.append("重数：本轮还没走完 ⇒ ⛔ 不查")
            elif not is_final:
                errs.append("写了「### 重数」但本轮还没走完（题没出齐或没判完）—— 先走完再写重数（§4.8 S11）")
            for n in notes:
                print("   ✔ %s" % n)
            for name, kws in spec["parts"]:
                if found.get(name) is not None:
                    print("   ✔ 子件「%s」在" % name)
            for e in errs:
                print("   ERROR  %s" % e)
            print("   ⇒ %s" % ("ERROR 0 · 可以发" if not errs else "ERROR %d · ⛔ 不许发" % len(errs)))
            total_err += len(errs)
            sections.append(dict(slug=slug, label=label, a=a, b=b, parts=parts,
                                 found=found, errs=list(errs), warns=[]))
            continue

        # ① 子件齐不齐
        found = {}
        rc_blocks_missing = False
        for name, kws in spec["parts"]:
            hit = _find_part(parts, kws)
            found[name] = hit
            if hit is None:
                # ★ 复检组：三版对照块是**条件性**的（判 ✅ 只记一行）⇒ 等战报数出 ❌ 再判
                if spec.get("recheck") and "三版对照块" in name:
                    rc_blocks_missing = True
                    continue
                msg = "缺子件「%s」（### 标题里要出现：%s）" % (name, " / ".join(kws))
                # ⚠️ 旧判据是「出现『最小修改版』**或**『diff 表』」⇒ 恒真：
                #    2026-08-30 起回看／新题本来就必须有「最小修改版全文」，
                #    于是整节没有三版对照块也被当成旧四份放行（08-30 那次破的就是这一条）。
                #    ⇒ 收紧成【两样都得有】—— 那才是旧四份格式真正的签名。
                old_four = (any("最小修改版" in t for t, _s, _e in parts)
                            and any("diff 表" in t for t, _s, _e in parts))
                if "三版对照块" in name and (legacy_blocks or old_four):
                    notes.append("存量 · %s —— 本节用的是 %s 之前的旧四份格式（最小修改版／更好版／diff 表A／表B），⛔ 不报错"
                                 % (msg, DELIVER_FLOOR_BLOCKS))
                elif "顺带判定" in name and sdate < DELIVER_FLOOR_INCIDENT:
                    notes.append("存量 · %s —— 顺带判定 %s 起才进必查件（更早写成正文里的 "
                                 "`**顺带判定**`，08-30 就是），⛔ 不报错"
                                 % (msg, DELIVER_FLOOR_INCIDENT))
                elif legacy_nodes and slug in ("回看", "新题") and ("全文" in name or name in ("她的原文", "收稿", "对照 problems")):
                    notes.append("存量 · %s —— 交付件清单 %s 才定，⛔ 不报错" % (msg, DELIVER_FLOOR_NODES))
                else:
                    errs.append(msg)

        # ② 块数守恒
        blk_part = found.get("bc 三版对照块") or found.get("三版对照块")
        blocks = []
        if blk_part:
            _, bs, be = blk_part
            blocks = _blocks_in(lines, bs, be)

        expect = None
        expect_src = ""
        rc_decl = {}
        if spec.get("recheck"):
            rc_decl, rc_errs = _declared_recheck(lines, a, b, parts, found)
            errs.extend(rc_errs)
            if "bad" in rc_decl:
                expect = rc_decl["bad"]
                expect_src = "战报里的『本组 ❌ %d 条』" % rc_decl["bad"]
                if expect == 0:
                    if rc_blocks_missing:
                        notes.append("本组 ❌ 0 条 ⇒ ⛔ 不需要三版对照块（§4③e：✅ 只记一行）")
                    elif blocks:
                        errs.append("本组报了「❌ 0 条」，却写了 %d 个三版对照块 —— "
                                    "复检判 ✅ 只记一行（§4③e），要么改战报、要么删块"
                                    % len(blocks))
                elif rc_blocks_missing:
                    errs.append("本组 ❌ %d 条却没有「三版对照块」子件 —— "
                                "复检判 ❌ 的**要走全套**（§4③e）" % expect)
        qp = found.get("题面") or found.get("题面与条件")
        op = found.get("她的原文")
        # ⛔ 复检组的应有块数**只认战报里的 ❌ 数** —— 数不出来就报错，
        #    ⛔ 不许回退到「题面编号题数」（那会把 10 题都要求写成块，复检就跑不动了）
        rc_only = bool(spec.get("recheck"))
        if op and expect is None and not rc_only:
            _, os_, oe = op
            ids = [ln for ln in lines[os_:oe] if RE_SENT_ID.match(ln)]
            if ids:
                expect = len(ids)
                expect_src = "「她的原文」里的 S 编号"
            else:
                for ln in lines[os_:oe]:
                    mm = RE_TOTAL_SENT.search(ln)
                    if mm:
                        expect = int(mm.group(1))
                        expect_src = "「她的原文」里的『共 N 句』"
                        break
        if expect is None and qp and not rc_only:
            _, qs, qe = qp
            nums = set()
            for ln in lines[qs:qe]:
                mm = RE_NUM_ITEM.match(ln)
                if mm:
                    nums.add(int(mm.group(1)))
            if nums:
                expect = len(nums)
                expect_src = "「题面」里的编号题数"
        if expect is None and rc_only:
            pass                      # 战报四行缺哪一行，_declared_recheck 已经点名报过
        elif expect is None:
            msg = "数不出应有块数 —— 「她的原文」里没有 S 编号／『共 N 句』，「题面」里也没有编号题"
            if legacy_blocks or (legacy_nodes and slug in ("回看", "新题")):
                notes.append("存量 · %s，⛔ 不报错" % msg)
            else:
                errs.append(msg)
        elif blk_part is None:
            pass  # 已在①报过
        elif len(blocks) != expect:
            errs.append("块数不守恒：三版对照块 %d 块 ≠ 应有 %d（来源：%s）"
                        % (len(blocks), expect, expect_src))
        else:
            notes.append("块数守恒 %d = %d（来源：%s）" % (len(blocks), expect, expect_src))

        # ③ 块内五行齐 + 三行英文非空
        for nid, s_, e_ in blocks:
            body = lines[s_ + 1:e_]
            for name, prefix in BLOCK_LINES:
                hits = [ln for ln in body if ln.strip().startswith(prefix)]
                if not hits:
                    errs.append("块 #%s 缺「%s」这一行" % (nid, name))
                    continue
                val = hits[0].strip()[len(prefix):].strip()
                if not val:
                    errs.append("块 #%s 的「%s」是空的" % (nid, name))

        # ④ 摘要句黑名单（只在三版对照块子件里查）
        if blk_part:
            _, bs, be = blk_part
            for i in range(bs, be):
                for bad in DELIVER_BLACKLIST:
                    if bad in lines[i]:
                        errs.append("三版对照块里出现摘要句「%s」（L%d）—— 未改也要逐块列出来"
                                    % (bad, i + 1))

        # ⑤ 复习组的战报 ①–⑤ 五行齐
        wp = found.get("d 战报")
        if wp and not spec.get("recheck"):
            _, ws, we = wp
            txt = "\n".join(lines[ws:we])
            for mark in "①②③④⑤":
                if mark not in txt:
                    if legacy_blocks:
                        notes.append("存量 · 战报缺第 %s 行（旧格式），⛔ 不报错" % mark)
                    else:
                        errs.append("战报缺第 %s 行" % mark)

        # ⑥ ★ 条件性子件「新建条目的正文」（§4③d③ / §4⑤e，她 2026-09-03 定）
        #    只有本节自己报了「新建 ≥1 条」才要求；报 0 条／没报 ⇒ ⛔ 不适用、不报错。
        #    起因：09-03 的作文节只做了「对照」、没建条目，8 件全齐 ⇒ 硬闸照样 ERROR 0。
        if spec.get("newborn"):
            decl_n, decl_nums, decl_i = _declared_new(lines, a, b)
            if decl_n > 0:
                nb = _find_part(parts, NEWBORN_KWS)
                shown = " ".join("#" + x for x in decl_nums) or "（该行没写编号）"
                if sdate < DELIVER_FLOOR_NEWBORN:
                    notes.append("存量 · 本节报了新建 %d 条（L%d）—— 「新建条目的正文」%s 起才进"
                                 "必查件，⛔ 不报错" % (decl_n, decl_i + 1, DELIVER_FLOOR_NEWBORN))
                elif nb is None:
                    errs.append("报了「新建 %d 条」（L%d：%s）却没有「新建条目的正文」子件 —— "
                                "§4③d③：⛔ 只报编号 ＝ 没交付（### 标题的某一段要以「新建条目」／"
                                "「新建的条目」开头）" % (decl_n, decl_i + 1, shown))
                else:
                    _t, ns_, ne_ = nb
                    body_txt = "\n".join(lines[ns_:ne_])
                    miss = [x for x in decl_nums if ("#" + x) not in body_txt]
                    if miss:
                        errs.append("「新建条目的正文」里缺这几条的正文：%s —— 本节报了新建 %d 条"
                                    "（L%d：%s），§4③d③ 每一条都要把正文发出来"
                                    % (" ".join("#" + m for m in miss), decl_n, decl_i + 1, shown))
                    else:
                        notes.append("新建条目的正文：报 %d 条 · 正文在 · 编号齐（%s）"
                                     % (decl_n, shown))

        # ⑦ §0.9b④ 表格⛔不进围栏 —— session 里已经写进围栏的，emit 会原样照搬，
        #    产出的粘贴件就是坏的（表格不再渲染）。⇒ 报 WARN，⛔ 不静默（她 2026-09-02 定）
        for name, _kws, mode in EMIT_PARTS.get(slug) or []:
            if mode != "raw":
                continue
            hit = found.get(name) or _find_part(parts, _kws)
            if hit is None:
                continue
            _t, hs, he = hit
            if _outer_fence(_trim_blank(lines[hs + 1:he])):
                warns.append("子件「%s」在 session 里被写进了 code 围栏 —— §0.9b④ 表格⛔不进围栏"
                             "（判定表／顺带判定／战报进了围栏就不再渲染成表）" % name)

        for n in notes:
            print("   ✔ %s" % n)
        for name, kws in spec["parts"]:
            if found.get(name) is not None:
                print("   ✔ 子件「%s」在" % name)
        for w in warns:
            print("   WARN   %s" % w)
        for e in errs:
            print("   ERROR  %s" % e)
        print("   ⇒ %s%s" % ("ERROR 0 · 可以发" if not errs else "ERROR %d · ⛔ 不许发" % len(errs),
                             "（WARN %d）" % len(warns) if warns else ""))
        total_err += len(errs)
        total_warn += len(warns)
        sections.append(dict(slug=slug, label=label, a=a, b=b, parts=parts,
                             found=found, errs=list(errs), warns=list(warns)))

    print("")
    print("═" * 74)
    print("合计 ERROR %d%s %s" % (total_err, " · WARN %d" % total_warn if total_warn else "",
                                  "· 可以发" if total_err == 0 else "· ⛔ 不许发，改完重跑"))
    print("═" * 74)
    return (1 if total_err else 0), sections


# ══════════════════════════════════════════════════════════════════════════
#  deliver --emit —— 直接产出「要粘贴给她的那一段」（她 2026-09-02 定）
#
#  背景：交付物完整性的闸只验 session 文件，**看不到教练在聊天里粘了什么** ——
#        已经连续三次发生「只发动过的块、其余略」。解法是把方向倒过来：
#        脚本按 §0.9b 的排版产出**唯一合法的粘贴内容**，教练一个字不许改。
#
#  ⛔ 它仍然【一个字的内容都不产生】：只把 session 文件里已有的字节原样打出来，
#     唯一加的是 code 围栏（§0.9b ①②③）——而且只在那一块本来就没写围栏时才加。
#     ⛔ 不重排、不省略、不摘要；表格（判定表／顺带判定／战报）⛔ 不进围栏（§0.9b ④）。
# ══════════════════════════════════════════════════════════════════════════
#   每一项 = (人读的名字, 该子件 ### 标题里必须出现的关键词, 排版)
#   排版 fence ＝ 一块一个 code 围栏 ｜ raw ＝ markdown 原样（表格）
EMIT_PARTS = {
    "复检组": [
        ("题面",       ["题面"],           "fence"),
        ("判定表",     ["判定表"],         "raw"),
        ("顺带判定",   ["顺带判定"],       "raw"),
        ("三版对照块", ["三版对照块"],     "fence"),
        ("战报",       ["战报"],           "raw"),
    ],
    "组": [
        ("题面",       ["题面"],           "fence"),
        ("判定表",     ["判定表"],         "raw"),
        ("顺带判定",   ["顺带判定"],       "raw"),
        ("三版对照块", ["三版对照块"],     "fence"),
        ("战报",       ["战报"],           "raw"),
    ],
    "回看": [
        ("题面与条件",     ["题面", "出题"],                "fence"),
        ("她的原文",       ["她的原文", "逐句编号", "原文"], "fence"),
        ("三版对照块",     ["三版对照块"],                  "fence"),
        ("最小修改版全文", ["最小修改版全文", "最小修改版"], "fence"),
        ("更好版全文",     ["更好版全文", "更好版"],        "fence"),
    ],
    "新题": [
        ("题面与条件",     ["题面", "出题"],                "fence"),
        ("她的原文",       ["她的原文", "逐句编号", "原文"], "fence"),
        ("收稿",           ["收稿"],                        "raw"),
        ("判分",           ["判分"],                        "raw"),
        ("对照 problems",  ["对照 problems", "对照"],       "raw"),
        ("三版对照块",     ["三版对照块"],                  "fence"),
        ("最小修改版全文", ["最小修改版全文", "最小修改版"], "fence"),
        ("更好版全文",     ["更好版全文", "更好版"],        "fence"),
    ],
    # 追加练（§4.8）的排版 §0.9b 没写 ⇒ ⛔ 不自作主张加围栏，整节 markdown 原样
    "追加练": None,
}


def _trim_blank(seq):
    """去掉首尾空行，中间一行不动。"""
    s, e = 0, len(seq)
    while s < e and not seq[s].strip():
        s += 1
    while e > s and not seq[e - 1].strip():
        e -= 1
    return list(seq[s:e])


def _emit_fence(body):
    """emit 给这一块补的围栏；已经带外层围栏 ⇒ None（⛔ 不套第二层，套了复制出来就是坏的）。
    ★ 判据是**外层**（第一个非空行是不是 ```），⛔ 不是「任一行 startswith ```」——
      后者会把「正文里带一个围栏、外面没围栏」的块误判成已带围栏、整节不加围栏（P3-11）。
    ★ 块内已有围栏时，外层用**更长的**一串反引号，否则内层那道会把外层提前关掉。"""
    if _outer_fence(body):
        return None
    longest = 0
    for l in body:
        t = l.lstrip()
        if t.startswith("```"):
            longest = max(longest, len(t) - len(t.lstrip("`")))
    return "`" * max(3, longest + 1)


def _emit_section(lines, sec, out):
    """按 §0.9b 把一个交付节的交付件打出来。⛔ 内容逐字节取自 session。"""
    a, b = sec["a"], sec["b"]
    out.append(lines[a])                       # 节标题，逐字
    plan = EMIT_PARTS.get(sec["slug"], None)
    if plan is None:                           # 追加练：整节原样
        body = _trim_blank(lines[a + 1:b])
        if body:
            out.append("")
            out.extend(body)
        return
    for name, kws, mode in plan:
        hit = _find_part(sec["parts"], kws)
        if hit is None:
            continue                           # 缺件在硬闸那一步已经判过（缺了就不会走到 emit）
        title, s_, e_ = hit
        if title == "(节首)":
            continue
        body = _trim_blank(lines[s_ + 1:e_])
        if not body:
            continue
        out.append("")
        out.append(title)                      # ### 标题逐字，⛔ 在围栏外（§0.9b「说明写在围栏外」）
        out.append("")
        fen = _emit_fence(body) if mode == "fence" else None
        if fen:
            out.append(fen)
            out.extend(body)
            out.append(fen)
        else:
            out.extend(body)


def cmd_deliver(args):
    path = args.session
    if not os.path.exists(path):
        print("⛔ 找不到 session 文件：%s" % path)
        return 2
    lines = io.open(path, encoding="utf-8").read().split("\n")
    if not getattr(args, "emit", False):
        rc, _ = _deliver_scan(args, path, lines)
        return rc

    # ★ --emit：先跑本来的硬闸；ERROR > 0 ⇒ ⛔ 拒绝 emit
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc, sections = _deliver_scan(args, path, lines)
    if rc:
        sys.stdout.write(buf.getvalue())
        print("⛔ ERROR > 0 ⇒ **拒绝 emit** —— 先把 session 改到 ERROR 0 再来（§0.9a）")
        return rc
    # 报告走 stderr，stdout 只留【要粘贴的那一段】
    sys.stderr.write(buf.getvalue())
    out = []
    for k, sec in enumerate(sections):
        if k:
            out.append("")
        _emit_section(lines, sec, out)
    sys.stdout.write("\n".join(out) + "\n")
    return 0


def main():
    ap = argparse.ArgumentParser(description="写作 drill 线只读机械工具")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("pick", help="把当天全部候选一次抽出、切成 ≤10 一组")
    p.add_argument("--type", choices=["learn", "review"], required=True)
    p.add_argument("--size", type=int, default=10, help="每组最多几题（默认 10）")
    p.add_argument("--groups", type=int, help="每条队列只打前 N 组的卡片（分组仍按全池算）")
    p.add_argument("--scope", choices=["pool", "grad", "both"], default="both",
                   help="只看一条队列。⚠️ 两条队列的**配额照常一起算**，"
                        "⛔ 不会因为只看一条就把上限让给它")
    p.add_argument("--full", action="store_true", help="打完整卡片（历史留痕/全部旧触发点/成员账全文）")
    p.add_argument("--date",
                   help="把哪一天当「今天」。⚠️ 只影响「今天」的口径，"
                        "⛔ 不能用来忠实回放当天的分组（那天之后才写下的判定行也会被算成已判过）")
    p.add_argument("--dry", action="store_true")
    p.set_defaults(func=cmd_pick)

    p = sub.add_parser("used", help="记录本组定稿用了哪几条、弃了哪几条")
    p.add_argument("--queue", choices=["pool", "grad"], default="pool",
                   help="pool ＝ 在池组（默认）｜ grad ＝ 复检组。两条队列各自编号")
    p.add_argument("--group", type=int, required=True)
    p.add_argument("--used", required=True)
    p.add_argument("--dropped")
    p.add_argument("--date")
    p.set_defaults(func=cmd_used)

    p = sub.add_parser("list", help="全量条目一览（非 detail），建号查重第一步")
    p.add_argument("--fam")
    p.add_argument("--state")
    p.add_argument("--pool", action="store_true", help="只列在池")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="打印指定条目的正文全文")
    p.add_argument("nums", nargs="+")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("dedup", help="按词查重：出错的词／改正后的词／规则关键词")
    p.add_argument("terms", nargs="+")
    p.add_argument("--fam", help="先限定族（§3.5 1.1①）；拿不准就不加，跨族查")
    p.add_argument("--limit", type=int, default=12)
    p.add_argument("--no-history", action="store_true", help="不搜历史记录，只搜规则本身")
    p.add_argument("--exclude", nargs="*", help="排除这些编号（§3.5 第4步 C3 复查自己时用）")
    p.set_defaults(func=cmd_dedup)

    p = sub.add_parser("count", help="按【类型】数条目：不带 --type 打全表，带了打清单")
    p.add_argument("--type", help="类型 slug（见不带参数时打印的那张表），或 fam:F08")
    p.add_argument("--detail", action="store_true", help="逐条打 编号·状态·连对/连错·上次·标题")
    p.set_defaults(func=cmd_count)

    p = sub.add_parser("stats", help="全档统计（每个数带编号清单）")
    p.add_argument("--brief", action="store_true")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("append", help="把写好的历史行插进 problems.md 并重算三个数")
    p.add_argument("--file", required=True, help="rows 文件，格式见 SKILL §3.1 契约⑪")
    p.add_argument("--date", help="判定日期 YYYY-MM-DD（默认今天）")
    p.add_argument("--dry-run", action="store_true", help="只打计划，⛔ 不写盘")
    p.set_defaults(func=cmd_append)

    p = sub.add_parser("trigger", help="把 session 里当天用的中文题面搬回条目的中文触发点")
    p.add_argument("--session", required=True, help="当日 session 文件路径")
    p.add_argument("--group", type=int, required=True, help="第几组（读它的 题面 ＋ 对应编号）")
    p.add_argument("--dry-run", action="store_true", help="只打将要改哪几条，⛔ 不写盘")
    p.set_defaults(func=cmd_trigger)

    p = sub.add_parser("migrate", help="problems.md ⇄ graduated.md 双向搬迁（§3.3/§4⑥）")
    p.add_argument("--dry-run", action="store_true", help="只打搬迁清单，⛔ 不写盘")
    p.set_defaults(func=cmd_migrate)

    p = sub.add_parser("deliver", help="交付物完整性硬闸（§4③bc/§4④/§4⑤e）")
    p.add_argument("--session", required=True, help="当日 session 文件路径")
    p.add_argument("--section", help="组N ／ 复检N ／ 回看 ／ 新题 ／ 追加练；不给则扫全部")
    p.add_argument("--all", action="store_true", help="扫这个文件里全部交付节")
    p.add_argument("--emit", action="store_true",
                   help="ERROR 0 时把【要粘贴给她的那一段】按 §0.9b 排版打到 stdout")
    p.set_defaults(func=cmd_deliver)

    p = sub.add_parser("lookback",
                       help="§4④ 回看哪一篇 ＝ 最近一篇【没被回看过】的新题（只读）")
    p.add_argument("--date", help="把哪一天当「今天」（默认今天）")
    p.set_defaults(func=cmd_lookback)

    p = sub.add_parser("check", help="格式校验")
    p.add_argument("--changed", action="store_true", help="只硬查本次改动的条目")
    p.add_argument("--all", action="store_true", help="全档扫描（存量只提示）")
    p.add_argument("--quiet", action="store_true")
    p.set_defaults(func=cmd_check)

    args = ap.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
