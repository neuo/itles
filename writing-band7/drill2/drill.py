#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""drill.py —— 写作 drill 线的【只读机械工具】。

她 2026-08-23 定：抽题与统计交给脚本，教练只读脚本吐出来的清单 + 抽中的那几条条目，
                  不再整档读 problems.md（15.2 万 tokens → 0.7 万）。

⛔ 本脚本【绝不写任何内容文件】。它只：
     · 读  problems.md / graduated.md / review_pool.md / log.md
     · 写  drawn_review.log（append-only 出题流水，与 pick_question.py 的 drawn.log 同款）
   所有条目内容、session、战报仍然全部手工写（SKILL §0.3 不变）。

子命令
  出题（SKILL §4① §6 §8）—— 开场跑一次，当天全部候选一次分完组
    python3 drill.py pick  --type learn|review [--size 10] [--full] [--date YYYY-MM-DD] [--dry]
    python3 drill.py used  --group N --used "#0095,#0266" [--dropped "#0303=与第2题同词族"]
  建号查重（SKILL §3.5 第 1 步）
    python3 drill.py dedup "works" "workers" [--fam F05] [--limit 12] [--no-history]
    python3 drill.py list  [--fam F04] [--pool] [--state 在池]
    python3 drill.py show  #0059 [#0071 …]
  统计与校验（SKILL §0.3 §0.4 §4⑥）
    python3 drill.py stats [--brief]
    python3 drill.py check [--changed | --all] [--quiet]

约定的档案格式见 SKILL §3.1 / §3.2。check 强制的就是那份格式，二者只有这一处定义。
⛔ 解析一律严格匹配，**不做兜底**：档案写歪 ⇒ check 报错 ⇒ 改档案，不改脚本。
"""

import argparse
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
        for name, txt in fields.items():
            if not txt:
                continue
            if tl in txt.lower():
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

    p = sub.add_parser("stats", help="全档统计（每个数带编号清单）")
    p.add_argument("--brief", action="store_true")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("check", help="格式校验")
    p.add_argument("--changed", action="store_true", help="只硬查本次改动的条目")
    p.add_argument("--all", action="store_true", help="全档扫描（存量只提示）")
    p.add_argument("--quiet", action="store_true")
    p.set_defaults(func=cmd_check)

    args = ap.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
