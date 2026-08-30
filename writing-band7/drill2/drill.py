#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""drill.py —— 写作 drill 线的【只读机械工具】。

她 2026-08-23 定：抽题与统计交给脚本，教练只读脚本吐出来的清单 + 抽中的那几条条目，
                  不再整档读 problems.md（15.2 万 tokens → 0.7 万）。

⛔ 本脚本【一个字的内容都不产生】。行文全部由教练手写，脚本只碰位置和算术：
     · 读  problems.md / graduated.md / review_pool.md / log.md
     · 写  drawn_review.log（append-only 出题流水）
     · 写  problems.md —— 仅 `append` 子命令，且仅两件机器活：
            ① 把教练写好的历史行插到正确位置  ② 连对／连错／上次 三个数重算
          ⛔ 不改 🎓／状态／条目正文／成员出题账 —— 那些是判断，仍然手写（SKILL §0.3）
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
  交付物硬闸（SKILL §4③bc §4④ §4⑤e）—— 发给她之前跑，ERROR>0 ⇒ 不许发
    python3 drill.py deliver --session sessions/2026-08-30.md [--section 组1|回看|新题]
  统计与校验（SKILL §0.3 §0.4 §4⑥）
    python3 drill.py stats [--brief]
    python3 drill.py check [--changed | --all] [--quiet]

约定的档案格式见 SKILL §3.1 / §3.2。check 强制的就是那份格式，二者只有这一处定义。
⛔ 解析一律严格匹配，**不做兜底**：档案写歪 ⇒ check 报错 ⇒ 改档案，不改脚本。
"""

import argparse
import io
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
REVIEW_POOL = os.path.join(ROOT, "review_pool.md")
LOG = os.path.join(ROOT, "log.md")
DRAWN = os.path.join(ROOT, "drawn_review.log")

# ── 两条日期分界线（都在 SKILL §3.1 里明写，不是脚本自己的兜底）──────────────
# FORMAT_ERA：新体系建库日。这天**之后**写的历史行必须有缩进内容行；
#             更早的是从旧档案迁进来的，旧表就只记了日期/符号/场合（problems.md 头部已声明）。
FORMAT_ERA = "2026-08-19"
# STRICT_FROM：符号文法生效日。这天**之后**写的行，符号必须是 §3.2 表里的、且不加粗。
STRICT_FROM = "2026-08-24"

FAMILIES = [f"F{i:02d}" for i in range(1, 19) if i not in (13, 16)]

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
        self.fam_section = None   # 所在族分段
        self.review_mark = False
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
    def essay_only(self):
        """条目自己声明「挂作文验，不出单点题」⇒ 不进复习组，只在判作文时对着扫。
        锚点写死成「不出单点题」五个字（SKILL §6）。"""
        return "不出单点题" in self.trigger

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
                mm = re.match(r"(连对|连错|毕业线|上次|族)\s*(.*)", f)
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
    """往回数第 n 个【学习日】（复习日与休息日不占位次，§1）。"""
    days = sorted([d for d, t in types.items() if t == "learn" and d < today], reverse=True)
    return days[n - 1] if len(days) >= n else None


# ══════════════════════════════════════════════════════════════════════════
#  drawn_review.log
# ══════════════════════════════════════════════════════════════════════════
def read_drawn(today):
    """本日流水 → (已经用掉的编号, 已收尾的组号集合)

    全天计划模型（她 2026-08-23 定）：`pick` 一次把当天全部候选切成组打出来，
    所以「抽」只是**计划**，不构成排除；只有真正出过题、跑过 `used` 的才排除。
    ⇒ 中途重跑 pick，剩下的池子会重新分组，已经出过的不会再回来。
    """
    used, groups = set(), set()
    if not os.path.exists(DRAWN):
        return used, groups
    for raw in open(DRAWN, encoding="utf-8"):
        raw = raw.rstrip("\n")
        if not raw.strip() or raw.startswith("#"):
            continue
        parts = raw.split("\t")
        if len(parts) < 3 or parts[0] != today or parts[1] != "用":
            continue
        groups.add(parts[2])
        for f in parts[3:]:
            if f.startswith("用:"):
                used.update(re.findall(r"#\d{4}", f))
    return used, groups


def append_drawn(line):
    new = not os.path.exists(DRAWN)
    with open(DRAWN, "a", encoding="utf-8") as f:
        if new:
            f.write("# 复习出题流水 —— drill.py 自动 append，一行 = 一次抽题或一次定稿\n")
            f.write("# 格式：日期 \\t 抽|用 \\t 组N \\t 字段:值 …   ⛔ 禁手工编辑\n")
        f.write(line + "\n")


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
#  pick
# ══════════════════════════════════════════════════════════════════════════
def partition(cand, size, spread_by_family):
    """把当天全部候选切成若干组，每组 ≤ size。
    学习日：按族轮流发牌 ⇒ 同族尽量落在不同组（考点层提示的机械那一半）。
    复习日：保持「最久没测优先」的顺序顺序切 ⇒ 她中途停了，最该测的已经测过。"""
    if not cand:
        return []
    k = (len(cand) + size - 1) // size
    buckets = [[] for _ in range(k)]
    if not spread_by_family:
        for i, item in enumerate(cand):
            buckets[i // size].append(item)
        return buckets
    byfam = defaultdict(list)
    for item in cand:
        byfam[item[0].fam].append(item)
    flat = []
    for fam in sorted(byfam, key=lambda f: (-len(byfam[f]), f)):
        flat.extend(byfam[fam])
    for i, item in enumerate(flat):
        buckets[i % k].append(item)
    return [b for b in buckets if b]


def cmd_pick(args):
    today = args.date or date.today().isoformat()
    ents = load_all()
    types = day_types()

    pool_note = []
    if args.type == "learn":
        d1 = back_count(today, types, 1)
        d3 = back_count(today, types, 3)
        if not d1:
            print("⛔ log.md 里数不出 D-1（今天之前没有学习日）。按 §1 不兜底，人工确认。")
            return 1
        targets = [d for d in (d1, d3) if d]
        cand = []
        for e in ents:
            if not e.in_pool:
                continue
            hit = []
            for h in e.history:
                if h.date not in targets:
                    continue
                first = (e.history[0] is h)
                if first or JUDGE.get(h.symbol) == "bad":
                    hit.append(("新建" if first else "判❌") + h.date[5:])
            if hit:
                cand.append((e, "／".join(sorted(set(hit)))))
        pool_note = [f"D-1 = {d1}　D-3 = {d3 or '（不足 3 个学习日，按 §1 不兜底）'}"]
        rnd = random.Random(today)          # 按日期定种：同一天重跑得到同一份计划
        rnd.shuffle(cand)
        spread = True
    else:
        cand = [(e, f"上次 {e.last}") for e in ents if e.in_pool]
        cand.sort(key=lambda t: (t[0].last if t[0].last and t[0].last != "—" else "0000-00-00",
                                 t[0].num))
        pool_note = ["复习日：按「最久没测的优先」排序（§8②b），组号越小越该先测"]
        spread = False

    used_ids, done_groups = read_drawn(today)
    cand = [(e, why) for e, why in cand if e.num not in used_ids]
    essay = [(e, why) for e, why in cand if e.essay_only]
    cand = [(e, why) for e, why in cand if not e.essay_only]
    groups = partition(cand, args.size, spread)
    base = len(done_groups)                 # 今天已经收过尾的组数

    W = "═" * 78
    print(W)
    print(f"drill.py pick · {today} · "
          f"{'学习日' if args.type == 'learn' else '复习日'} · **全天计划**")
    print(W)
    for x in pool_note:
        print("  " + x)
    today_type = types.get(today)
    if today_type and today_type != args.type:
        print(f"  ⚠️ log.md 里今天写的是【{'复习日' if today_type == 'review' else '学习日'}】，"
              f"你传的是 --type {args.type} —— 按 §1 先确认今天到底是哪一天")
    elif not today_type:
        print("  （log.md 里今天还没有行 —— 收尾时记得补，§4⑥）")
    shown = groups if not args.groups else groups[:args.groups]
    if essay:
        print(f"  ⛔ 另有 {len(essay)} 条**挂作文验**，条目自己写着「不出单点题」⇒ 不进复习组：")
        print("     " + " ".join(e.num for e, _ in essay))
        print("     ⇒ 判作文时对着这几条扫全文（§4⑤d），⛔ 不要拿它们出中译英")
    print(f"  候选池 {len(cand)} 条（已排除本日已用 {len(used_ids)} 条"
          + (f"、挂作文验 {len(essay)} 条" if essay else "") + "）"
          f" ⇒ 分 {len(groups)} 组，每组 ≤ {args.size}"
          + (f"　（本次只打前 {len(shown)} 组）" if len(shown) < len(groups) else ""))
    print(f"  ★ 计划按日期定种，今天重跑这条命令得到的分组**完全一样**（compact 后可放心重跑）")
    if not args.full:
        print(f"  ★ 卡片是精简版；要看历史留痕/全部旧触发点/成员账全文 ⇒ 加 --full，"
              f"或 `show #NNNN`")
    print()

    def card(e, why, tag):
        star = " ⚠️🔍REVIEW" if e.review_mark else ""
        created_today = e.created_on() == today
        hint = ("⛔零提示" if (e.ok or 0) >= 1
                else "★给英文词（连对 0／建号当天／刚降级）")
        print(f"{tag} {e.num}  {e.fam}  {e.ok}/{e.bad}  上次 {(e.last or '—')[5:]}"
              f"  ←{why}{star}{'  ←本条今天建的号' if created_today else ''}")
        print(f"     考点 {e.title}")
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
            todo_m = [l.strip() for l in e.members.splitlines()
                      if "未出过" in l]
            if args.full:
                print("     成员出题账（§3.5 第3.5步：一题 ≥2 个成员）")
                for l in e.members.splitlines():
                    if l.strip() and not l.strip().startswith("```"):
                        print(f"          {l.strip()}")
            elif todo_m:
                print(f"     成员 ★未出过 {len(todo_m)} 个：" +
                      " ／ ".join(x.split("——")[0].split("  ")[0].strip()
                                  for x in todo_m[:4]))
        if args.full:
            occ = e.occasions()
            if occ:
                print("     历次 " + " ｜ ".join(occ))
            print(f"     正文 {e.src}:{e.start}")

    def scan(bucket, gno):
        fam_g = defaultdict(list)
        for e, _ in bucket:
            fam_g[e.fam].append(e.num)
        msgs = []
        for k, v in sorted(fam_g.items()):
            if len(v) > 1:
                msgs.append(f"⚠️ 同族 {k}：{' '.join(v)}")
        kw = {e.num: cn_keywords(e.trigger_for_keywords()) for e, _ in bucket}
        nums = [e.num for e, _ in bucket]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sh = {w for w in kw[nums[i]] & kw[nums[j]] if len(w) >= 2}
                if sh:
                    msgs.append(f"⚠️ 措辞 {nums[i]} ⇔ {nums[j]} 共享「{'／'.join(sorted(sh)[:4])}」")
        pset = {e.num for e, _ in bucket}
        for e, _ in bucket:
            for other in e.no_pair_with() & pset:
                msgs.append(f"⛔ 禁配 {e.num} 正文写死「不能和 {other} 同组」—— 必须换组")
        todo = [e.num for e, _ in bucket if e.trigger_todo]
        if todo:
            msgs.append(f"⚠️ 待补 {' '.join(todo)}")
        if msgs:
            print("     ── 本组机械扫描 ──")
            for m in msgs:
                print("     " + m)
        else:
            print("     ── 本组机械扫描：同族／措辞／禁配／待补 全部零命中 ──")

    for gi, bucket in enumerate(shown, start=base + 1):
        print("━" * 78)
        print(f"━━━ 组 {gi}（{len(bucket)} 条）")
        print("━" * 78)
        for e, why in bucket:
            card(e, why, " ")
        scan(bucket, gi)
        print()

    print("─" * 78)
    print("⛔ 脚本做不到、必须手工的两件：语言事实核查 · 中文题面自译落点（§6）")
    print("★ 冲突要挪题 ⇒ 在**组与组之间对调**，⛔ 不用重抽 —— 全天的池子已经在上面了")
    if args.dry:
        print("（--dry：没有写 drawn_review.log）")
    else:
        for gi, bucket in enumerate(shown, start=base + 1):
            append_drawn(f"{today}\t抽\t组{gi}\t正选:"
                         + ",".join(e.num for e, _ in bucket))
        print(f"已记流水：{today} 共 {len(shown)} 组")
    print("每组定稿后跑：python3 writing-band7/drill2/drill.py used --group N "
          "--used \"#a,#b,…\" [--dropped \"#c=理由\"]")
    return 0


def cmd_used(args):
    today = args.date or date.today().isoformat()
    used = re.findall(r"#\d{4}", args.used or "")
    fields = [f"用:{','.join(used)}"]
    if args.dropped:
        fields.append(f"弃:{args.dropped}")
    append_drawn(f"{today}\t用\t组{args.group}\t" + "\t".join(fields))
    print(f"已记流水：{today} 组{args.group} 用 {len(used)} 条"
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
        star = "🔍" if e.review_mark else " "
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


def _essay_only_body(e):
    """正文别处（不在中文触发点里）出现「不出单点题」⇒ pick 认不到 ⇒ 要报出来。"""
    return (not e.essay_only) and ("不出单点题" in "\n".join(e.raw))


TYPES = [
    # slug             中文名          口径（认哪个锚点）                                  predicate
    ("pool",       "在池",        "状态行第 1 格 ＝ 在池",                        lambda e: e.in_pool),
    ("grad",       "🎓 毕业",      "状态行第 1 格 ＝ 🎓",                          lambda e: e.graduated),
    ("retired",    "退池",        "状态行第 1 格 ＝ 退池",                        lambda e: e.state == "退池"),
    ("merged",     "并入",        "状态行第 1 格 ＝ 并入 #NNNN",                  lambda e: bool(e.state) and e.state.startswith("并入")),
    ("essay",      "挂作文验",     "**中文触发点**里有「不出单点题」五个字（§6）",    lambda e: e.essay_only),
    ("essay-bad",  "挂作文验·写歪", "「不出单点题」写在正文别处 ⇒ pick 认不到",      _essay_only_body),
    ("pickable",   "可出题",      "在池 ＋ 非挂作文验 ＋ 题面不待补",               lambda e: e.in_pool and not e.essay_only and not e.trigger_todo),
    ("trigger-todo", "题面待补",   "在池 ＋ 中文触发点为空或含「待补」",             lambda e: e.in_pool and e.trigger_todo),
    ("review",     "REVIEW 池",   "状态行下有 `⚠️🔍 **REVIEW 池**`（§3.3）",       lambda e: e.review_mark),
    ("wordlist",   "词表型",      "正文挂着 `**成员出题账**`（§3.5 第3.5步）",       lambda e: bool(e.members)),
    ("nopair",     "有禁配声明",   "正文写着「不能和 #NNNN」（§6 组内排布）",         lambda e: bool(e.no_pair_with())),
    ("streak0",    "在池·连对 0",  "在池 ＋ 连对 0",                               lambda e: e.in_pool and e.ok == 0),
    ("streak1",    "在池·连对 1",  "在池 ＋ 连对 1",                               lambda e: e.in_pool and e.ok == 1),
    ("streak2+",   "在池·连对 ≥2", "在池 ＋ 连对 ≥2 ⚠️ 到线未毕业，该改 🎓",        lambda e: e.in_pool and e.ok is not None and e.ok >= 2),
    ("by-error",   "建号·她犯错",  "历史记录第一行符号 ＝ ❌（§2①）",               lambda e: _first_symbol(e) == "❌"),
    ("by-request", "建号·她点名",  "历史记录第一行符号 ＝ ③（§2③）",               lambda e: _first_symbol(e) == "③"),
    ("migrated",   "旧档案迁移",   "第一条历史行日期 < 2026-08-19",                lambda e: bool(e.created_on()) and e.created_on() < "2026-08-19"),
    ("never",      "从未被判定",   "历史记录里写着「（从未被判定过）」",              lambda e: e.never_judged),
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
            star = "🔍" if e.review_mark else " "
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
    review = [e for e in ents if e.review_mark]
    grad_in_problems = [e for e in grad if e.src == "problems.md"]

    print("═" * 74)
    print("drill.py stats · 全档 = problems.md ＋ graduated.md（两文件合计逐条实数）")
    print("═" * 74)
    print(f"全档总数   {total} 条　＝ problems.md {sum(1 for e in ents if e.src=='problems.md')}"
          f" ＋ graduated.md {sum(1 for e in ents if e.src=='graduated.md')}")
    print(f"在池       {len(in_pool)} 条")
    print(f"🎓         {len(grad)} 条（占 {len(grad)/max(total,1)*100:.1f}%）")
    if grad_in_problems:
        print(f"   其中 {len(grad_in_problems)} 条仍在 problems.md，**待她手动搬进 graduated.md**（§3.3）")
        print(fmt_ids([e.num for e in grad_in_problems]))
    print(f"退池       {len(retired)} 条　并入 {len(merged)} 条")
    print(f"REVIEW 池  {len(review)} 条")
    if review:
        print(fmt_ids([e.num for e in review]))
    if os.path.exists(REVIEW_POOL):
        rp = set(re.findall(r"(?m)^### (#\d{4})", open(REVIEW_POOL, encoding='utf-8').read()))
        marked = {e.num for e in review}
        if rp != marked:
            print(f"   ⚠️ 与 review_pool.md 不符：只在标记 {sorted(marked-rp)} ／ 只在清单 {sorted(rp-marked)}")
        else:
            print("   ✔ 与 review_pool.md 一一对应")
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
        if e.src != "problems.md":
            errs.append(f"{tag} 在 {e.src} 里 —— ⛔ 已归档的条目不许再 append")
        elif e.state not in ("在池", "🎓"):
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
            b["pre_err"] = {m for lv, m in check_entry(e, set(), None) if lv == "ERROR"}
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

    # ── 组装：从后往前插，免得行号错位 ────────────────────────────────────
    src = open(PROBLEMS, encoding="utf-8").read()
    lines = src.split("\n")
    plan = []
    for b in blocks:
        e = b["entry"]
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
            at = max((i for i in range(lo, hi) if lines[i].strip()), default=hi - 1) + 1
        row = f"- {today} {b['symbol']}{b['raw_occ']}".rstrip()
        plan.append(dict(e=e, at=at, drop=drop, block=[row] + b["body"], b=b))

    for p in sorted(plan, key=lambda x: -x["at"]):
        body = [l for l in p["block"]]
        while body and not body[-1].strip():
            body.pop()
        lines[p["at"]:p["at"]] = body
        if p["drop"] is not None:
            del lines[p["drop"]]

    new = "\n".join(lines)
    if args.dry_run:
        print("═" * 74)
        print(f"drill.py append --dry-run · {len(plan)} 条 · {today}（⛔ 没写盘）")
        print("═" * 74)
        for p in sorted(plan, key=lambda x: x["at"]):
            print(f"  {p['e'].num}  插到 problems.md L{p['at']}  "
                  f"（{len(p['block'])} 行）{'· 顶掉「从未被判定过」' if p['drop'] is not None else ''}")
            print(f"      {p['block'][0][:88]}")
        for w in warns:
            print("WARN   " + w)
        print("═" * 74)
        return 0

    open(PROBLEMS, "w", encoding="utf-8").write(new)

    # ── 重算三个数（连对／连错／上次）────────────────────────────────────
    ents2 = parse_file(PROBLEMS, "problems.md")
    idx = {e.num: e for e in ents2}
    lines = open(PROBLEMS, encoding="utf-8").read().split("\n")
    moved = []
    for b in blocks:
        e2 = idx[b["num"]]
        ok, bad = e2.recount()
        last = e2.last_row_date() or "—"
        i = e2.status_lineno - 1
        before = lines[i]
        lines[i] = rewrite_status(before, ok, bad, last)
        moved.append((b["num"], e2.state, ok, bad, last, before != lines[i]))
    open(PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))

    # ── 自查：写完立刻按 check 的规矩硬查这几条，出 ERROR 就整批回滚 ──────
    ents3 = parse_file(PROBLEMS, "problems.md") + parse_file(GRADUATED, "graduated.md")
    all_nums = {e.num for e in ents3}
    idx3 = {e.num: e for e in ents3 if e.src == "problems.md"}
    hard = set()
    for b in blocks:
        e3 = idx3[b["num"]]
        for h in e3.history:
            if h.date == today:
                hard.add(("problems.md", h.lineno))
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
            if level != "ERROR" or msg in pre or msg.startswith(TODO):
                continue
            bad_rows.append((b["num"], msg))
    if bad_rows:
        open(PROBLEMS, "w", encoding="utf-8").write(src)
        print("═" * 74)
        print(f"drill.py append · ⛔ 写完自查不过，{len(bad_rows)} 处 —— 已整批回滚")
        print("═" * 74)
        for n, m in bad_rows:
            print(f"ERROR  {n}  {m}")
        print("═" * 74)
        return 1

    print("═" * 74)
    print(f"drill.py append · {len(plan)} 条已写进 problems.md · {today} · 自查 ERROR 0")
    print("═" * 74)
    for num, state, ok, bad, last, ch in moved:
        e3 = idx3[num]
        flag = ""
        if state == "在池" and ok >= 2:
            flag = "   ⇒ ★ 连对已到毕业线 2，§3.3 要你原地改 🎓（脚本⛔不代改）"
        elif state == "🎓" and bad >= 1:
            flag = "   ⇒ ★ 🎓 条目吃到 ❌，§3.3 要你决定是否降级回池（脚本⛔不代改）"
        print(f"  {num}  {state}  连对 {ok} ｜ 连错 {bad} ｜ 上次 {last}{flag}")
    for w in warns:
        print("WARN   " + w)
    print("─" * 74)
    print("下一步：`drill.py check --changed` 复核全部改动（§0.3）")
    print("═" * 74)
    return 0


# ══════════════════════════════════════════════════════════════════════════

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
        "parts": [
            ("题面",       ["题面"]),
            ("她的答案",   ["她的答案"]),
            ("a 判定表",   ["判定表"]),
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
}

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


RE_SKIP = re.compile(r"(本节跳过|⇒\s*\*?\*?跳过|按 §4④「D-1 没写新题就跳过」)")


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


def cmd_deliver(args):
    path = args.session
    if not os.path.exists(path):
        print("⛔ 找不到 session 文件：%s" % path)
        return 2
    lines = io.open(path, encoding="utf-8").read().split("\n")
    md = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(path))
    sdate = md.group(1) if md else "9999-99-99"
    legacy_blocks = sdate < DELIVER_FLOOR_BLOCKS
    legacy_nodes = sdate < DELIVER_FLOOR_NODES

    wanted = []
    if args.all or not args.section:
        # 全部：所有「复习 · 第 N 组」＋ 回看 ＋ 新题（存在才查）
        for i, ln in enumerate(lines):
            m = re.match(r"^## 复习 · 第 (\d+) 组", ln)
            if m:
                wanted.append("组%s" % m.group(1))
        for slug in ("回看", "新题"):
            if _slice_h2(lines, lambda x, h=DELIVER_SPECS[slug]["head"]: x.startswith(h)):
                wanted.append(slug)
    else:
        wanted = [args.section]

    if not wanted:
        print("⛔ 这个文件里没有可查的交付节（复习 · 第 N 组 ／ 回看 ／ 新题）")
        return 2

    print("═" * 74)
    print("drill.py deliver · 交付物完整性硬闸 · %s" % path)
    print("   ⛔ ERROR > 0 ⇒ 不许发（SKILL §4③bc / §4④ / §4⑤e，她 2026-08-30 定）")
    print("═" * 74)

    total_err = 0
    for slug in wanted:
        errs = []
        notes = []
        m = re.match(r"^组(\d+)$", slug)
        if m:
            spec = DELIVER_SPECS["组"]
            n = m.group(1)
            rng = _slice_h2(lines, lambda x, n=n: x.startswith("## 复习 · 第 %s 组" % n))
            label = "复习 · 第 %s 组" % n
        elif slug in DELIVER_SPECS:
            spec = DELIVER_SPECS[slug]
            rng = _slice_h2(lines, lambda x, h=spec["head"]: x.startswith(h))
            label = slug
        else:
            print("⛔ 不认识的 --section：%s（用 组N ／ 回看 ／ 新题）" % slug)
            return 2

        print("")
        print("── %s ──" % label)
        if rng is None:
            print("   ERROR  节不存在 —— 找不到这一节的 ## 标题")
            total_err += 1
            continue
        a, b = rng
        # 新题这条路历史上把 判分／对照／三版对照块 写成了 ## 级 —— 节区间要吃到 ## 收尾／## 教练侧 之前
        h2_too = slug in ("新题", "回看")
        if h2_too:
            # 回看 停在 ## 新题（否则会把新题的两份全文认成自己的）；
            # 新题 扫到文件末 —— 历史上 判分／对照／记账 被写在 ## 收尾 之后（08-20 就是）
            b = len(lines)
            stops = ("新题", "复习 ·") if slug == "回看" else ("复习 ·",)
            for j in range(a + 1, len(lines)):
                if lines[j].startswith("## ") and any(
                    lines[j].startswith("## " + stop) for stop in stops
                ):
                    b = j
                    break
        parts = _sub_parts(lines, a, b, h2_too=h2_too)

        # 声明跳过的节（§4④ D-1 没写新题就跳过）⇒ 不查
        head_txt = "\n".join(lines[a:min(a + 20, b)])
        if RE_SKIP.search(head_txt):
            print("   SKIP   本节已声明跳过（§4④），⛔ 不查")
            continue

        # ① 子件齐不齐
        found = {}
        for name, kws in spec["parts"]:
            hit = _find_part(parts, kws)
            found[name] = hit
            if hit is None:
                msg = "缺子件「%s」（### 标题里要出现：%s）" % (name, " / ".join(kws))
                old_four = any(
                    ("最小修改版" in t or "diff 表" in t)
                    for t, _s, _e in parts
                )
                if "三版对照块" in name and (legacy_blocks or old_four):
                    notes.append("存量 · %s —— 本节用的是 %s 之前的旧四份格式（最小修改版／更好版／diff 表A／表B），⛔ 不报错"
                                 % (msg, DELIVER_FLOOR_BLOCKS))
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
        qp = found.get("题面") or found.get("题面与条件")
        op = found.get("她的原文")
        if op:
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
        if expect is None and qp:
            _, qs, qe = qp
            nums = set()
            for ln in lines[qs:qe]:
                mm = RE_NUM_ITEM.match(ln)
                if mm:
                    nums.add(int(mm.group(1)))
            if nums:
                expect = len(nums)
                expect_src = "「题面」里的编号题数"
        if expect is None:
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
        if wp:
            _, ws, we = wp
            txt = "\n".join(lines[ws:we])
            for mark in "①②③④⑤":
                if mark not in txt:
                    if legacy_blocks:
                        notes.append("存量 · 战报缺第 %s 行（旧格式），⛔ 不报错" % mark)
                    else:
                        errs.append("战报缺第 %s 行" % mark)

        for n in notes:
            print("   ✔ %s" % n)
        for name, kws in spec["parts"]:
            if found.get(name) is not None:
                print("   ✔ 子件「%s」在" % name)
        for e in errs:
            print("   ERROR  %s" % e)
        print("   ⇒ %s" % ("ERROR 0 · 可以发" if not errs else "ERROR %d · ⛔ 不许发" % len(errs)))
        total_err += len(errs)

    print("")
    print("═" * 74)
    print("合计 ERROR %d %s" % (total_err, "· 可以发" if total_err == 0 else "· ⛔ 不许发，改完重跑"))
    print("═" * 74)
    return 1 if total_err else 0


def main():
    ap = argparse.ArgumentParser(description="写作 drill 线只读机械工具")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("pick", help="把当天全部候选一次抽出、切成 ≤10 一组")
    p.add_argument("--type", choices=["learn", "review"], required=True)
    p.add_argument("--size", type=int, default=10, help="每组最多几题（默认 10）")
    p.add_argument("--groups", type=int, help="只打前 N 组的卡片（分组仍按全池算）")
    p.add_argument("--full", action="store_true", help="打完整卡片（历史留痕/全部旧触发点/成员账全文）")
    p.add_argument("--date")
    p.add_argument("--dry", action="store_true")
    p.set_defaults(func=cmd_pick)

    p = sub.add_parser("used", help="记录本组定稿用了哪几条、弃了哪几条")
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

    p = sub.add_parser("deliver", help="交付物完整性硬闸（§4③bc/§4④/§4⑤e）")
    p.add_argument("--session", required=True, help="当日 session 文件路径")
    p.add_argument("--section", help="组N ／ 回看 ／ 新题；不给则扫全部")
    p.add_argument("--all", action="store_true", help="扫这个文件里全部交付节")
    p.set_defaults(func=cmd_deliver)

    p = sub.add_parser("check", help="格式校验")
    p.add_argument("--changed", action="store_true", help="只硬查本次改动的条目")
    p.add_argument("--all", action="store_true", help="全档扫描（存量只提示）")
    p.add_argument("--quiet", action="store_true")
    p.set_defaults(func=cmd_check)

    args = ap.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
