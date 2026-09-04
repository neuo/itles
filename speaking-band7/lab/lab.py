#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py —— 口语 fluency-lab 线的机械工具（2026-08-29 从写作线 drill.py 移植）。

⛔ 本脚本【一个字的内容都不产生】。行文全部由教练手写，脚本只碰位置和算术：
     · 读  problems.md / graduated.md / methods.md / redo_queue.md / sessions/
     · 写  drawn.log（append-only 出题流水）
     · 写  problems.md —— 仅 `append` 子命令，且仅两件机器活：
            ① 把教练写好的历史行插到正确位置  ② 连对／连错／上次 三个数重算
          ⛔ 不改 🎓／状态／条目正文 —— 那些是判断，仍然手写（SKILL §0.3）

子命令
  出题（SKILL §4① §5 §6）—— 开场跑一次，当天全部候选一次分完组
    python3 speaking-band7/lab/lab.py pick --type learn|review [--size 10] [--full] [--date D]
    python3 speaking-band7/lab/lab.py used --group N --used "12,45" [--dropped "88=与第2题同词族"]
  建号查重（SKILL §3.1 判重三步 · §4④1b）
    python3 speaking-band7/lab/lab.py dedup "look for" "找" [--limit 12] [--no-history]
    python3 speaking-band7/lab/lab.py list [--state 未毕业] [--type 词组]
    python3 speaking-band7/lab/lab.py show 12 45
  记账（SKILL §7 顺序写死 —— 落盘之后）
    python3 speaking-band7/lab/lab.py append --file rows.md --date YYYY-MM-DD [--dry-run]
  统计与校验（SKILL §0.1 §8 §11）
    python3 speaking-band7/lab/lab.py stats [--brief]
    python3 speaking-band7/lab/lab.py check [--changed | --all] [--quiet]

约定的档案格式见 SKILL §3.1 / §3.3。check 强制的就是那份格式，二者只有这一处定义。
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
METHODS = os.path.join(ROOT, "methods.md")
REDO = os.path.join(ROOT, "redo_queue.md")
SESSIONS = os.path.join(ROOT, "sessions")
DRAWN = os.path.join(ROOT, "drawn.log")

# ── 日期分界线（SKILL §3.1 明写，不是脚本自己的兜底）────────────────────────
# STRICT_FROM：符号文法生效日。这天**之后**写的历史行，符号必须是 §3.3 表里的。
#              更早的是旧体系迁移进来的，只提示不报错。
STRICT_FROM = "2026-08-29"

# ── 符号文法（SKILL §3.3）──────────────────────────────────────────────────
#   判定符号：推进 streak
JUDGE = {
    "✅": "ok",       # 考点位置一字不差
    "❌": "bad",      # 真错（含"忘了/不会"）
}
#   📖 已停用，但历史里它 ＝「教练给了答案、她照写」＝ 没做出来 ⇒ 按 bad 参与重算
LEGACY_JUDGE = {"📖": "bad"}
#   不推进 streak 的记号
NEUTRAL = {
    "◎": "题面本身有毛病（教练现编／截断／缺主语），本次作废",
    "⚪": "形态类记号（§3.4②）—— 不判档位、不动状态行",
}
LEGACY = {
    "📖": "2026-08-23 起停用（'不会就错' ⇒ 一律记 ❌），只保留读历史",
}
TRACE = {
    "📝": "留痕行（拆号/合并/题面整改/判重结论/她的裁决等，不推进 streak）",
    "新建": "建号行（§2③ 她点名要学 / 教练当场建）",
    "⛔": "留痕行（题面加死、停出声明、并入说明等）",
    "⚠️": "留痕行（改判、回写、口径更正）",
}
ALL_SYMBOLS = sorted(list(JUDGE) + list(NEUTRAL) + list(LEGACY) + list(TRACE),
                     key=len, reverse=True)

# ── 状态行上的标记（出题时据此剔除／限流）─────────────────────────────────
M_MORPH = "形态类·不召回"          # §3.4  永不出题
M_ONLYLOG = "只记录·不出题"        # §3.4④ 同上，08-27 起的新写法
M_SPELL = "拼写类·不召回"          # §2.1② 永不出题
M_NOREVIEW = "复习组停出"          # §6    只在自由产出里判
M_MERGED = "合并条·出题多句覆盖"    # §3.2c 出题必须多句覆盖全部成员
M_STUBBORN = "顽固"

RE_ENTRY = re.compile(r"^### (\d+)\s*·\s*(.*)$")
RE_STATUS = re.compile(r"^状态\s+(.*)$")
RE_META = re.compile(r"^类型\s+(\S+)")
RE_HIST = re.compile(r"^-\s*(20\d\d-\d\d-\d\d)\s+(.*)$")
RE_NOTE = re.compile(r"^-\s*(备注|判重结论)")
RE_DAYTYPE = re.compile(r"^#\s*(20\d\d-\d\d-\d\d)\s*·\s*\**\s*(L[123]|R)\b")
RE_MERGED_TITLE = re.compile(r"^（已并入")
RE_VOID_TITLE = re.compile(r"^⛔\s*作废")
# 状态行以「→ 已迁入 …」开头 ＝ 条目整条迁出（如 #157 迁进 methods.md）⇒ 同墓碑
RE_MOVED_OUT = re.compile(r"^\s*→\s*\**\s*已迁[入出]")
# 「上次」的三种合法写法（闭集，⛔ 不再认第四种）
LAST_NEVER = ("—", "未测过")


def norm(s):
    return s.replace("**", "").replace("​", "").replace("　", " ").strip()


def parse_symbol(rest):
    """从历史行日期之后切出符号。⛔ 不做兜底：符号必须紧跟日期。
    认得出加粗写法是为了让 check 报错，不是为了放过。"""
    s = rest.strip()
    bold = s.startswith("**")
    if bold:
        s = s[2:]
    for sym in ALL_SYMBOLS:
        if s.startswith(sym):
            occ = s[len(sym):]
            if bold:
                occ = occ.lstrip("*")
            return sym, occ.replace("　", " ").strip(), bold
    return None, s.replace("　", " ").strip(), bold


# ══════════════════════════════════════════════════════════════════════════
#  Parser —— 全脚本唯一一处「档案长什么样」的定义
# ══════════════════════════════════════════════════════════════════════════
class Hist:
    __slots__ = ("date", "symbol", "occasion", "lineno", "kind", "bold", "raw")

    def __init__(self, **kw):
        for k in self.__slots__:
            setattr(self, k, kw.get(k))


class Entry:
    def __init__(self, num, title, src, start):
        self.num = num                # int
        self.title = title
        self.src = src                # 'problems.md' / 'graduated.md'
        self.start = start            # 1-based
        self.end = None
        self.kind = None              # 类型字段（词组/搭配/语法/结构/词汇…）
        self.prompt = None            # 题面字段
        self.status_raw = None
        self.status_lineno = None
        self.ok = self.bad = None
        self.last = None
        self.grad = None              # 🎓 已毕业 的日期，未毕业则 None
        self.marks = set()            # 状态行上的标记
        self.history = []
        self.raw = []
        self.tomb = False             # （已并入）／⛔ 作废 —— 不占池、不出题
        self.problems = []

    # ── 派生 ──────────────────────────────────────────────────────────
    @property
    def graduated(self):
        return self.grad is not None

    @property
    def active(self):
        """会参与出题/统计的（排除墓碑）"""
        return not self.tomb

    @property
    def drawable(self):
        """能进复习组的：未毕业 · 非墓碑 · 无「不召回／停出」标记"""
        if self.tomb or self.graduated:
            return False
        return not (self.marks & {M_MORPH, M_ONLYLOG, M_SPELL, M_NOREVIEW})

    @property
    def block_reason(self):
        for m in (M_MORPH, M_ONLYLOG, M_SPELL, M_NOREVIEW):
            if m in self.marks:
                return m
        return None

    def judged_rows(self, upto=None):
        """按**出现顺序**列出判定行 —— §3.3「同一条同一天被产出多次，每一次都算一次」。
        ✅ ＝ ok ｜ ❌ 与 📖 ＝ bad ｜ ◎ ⚪ 与留痕行不参与。
        upto 给日期 ⇒ 只数到那天为止（毕业冻结用）。"""
        out = []
        for h in self.history:
            if upto and h.date > upto:
                continue
            v = JUDGE.get(h.symbol) or LEGACY_JUDGE.get(h.symbol)
            if v:
                out.append((h.date, v))
        return out

    def freeze_at(self):
        """已毕业条目的状态行冻结在毕业那一天 —— 毕业后的 ✅ 是「自发命中」证据，
        只留痕、不再推进数字（§3.3 毕业 ＝ 复习不再召回）。"""
        return self.grad if (self.graduated and self.grad != "—") else None

    def recount(self):
        ok = bad = 0
        for _, v in self.judged_rows(self.freeze_at()):
            if v == "ok":
                ok += 1
                bad = 0
            else:
                bad += 1
                ok = 0
        return ok, bad

    def tested_days(self):
        """真正被测到的日子 ＝ 判定行（✅❌📖）＋ ◎（出了题，只是题面坏了）。
        ⚪ 只是记号、留痕/备注行不算被测（§3.1「上次」＝ 上次复习）。"""
        return sorted({h.date for h in self.history
                       if h.symbol in JUDGE or h.symbol in LEGACY_JUDGE or h.symbol == "◎"})

    def last_tested(self):
        d = self.tested_days()
        return d[-1] if d else None

    def last_row_date(self):
        return max((h.date for h in self.history), default=None)

    def ever_bad(self):
        """历史上有过 ❌ 或 📖（§4① 必进池①）"""
        return any(h.symbol in ("❌", "📖") for h in self.history)

    def seen_on(self, d):
        return any(h.date == d for h in self.history)

    def created_on(self):
        for h in self.history:
            if h.symbol == "新建" or "新建" in (h.occasion or ""):
                return h.date
        return self.history[0].date if self.history else None

    def targets(self):
        """标题里的英文目标形式 —— 组内防撞（相邻两题不测同一个词）用。"""
        t = re.sub(r"（[^）]*）", " ", self.title)
        return {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'\-]{2,}", t)}


def parse_file(path, src):
    if not os.path.exists(path):
        return []
    lines = open(path, encoding="utf-8").read().split("\n")
    entries, cur, fence = [], None, False

    def close(idx):
        if cur is not None:
            cur.end = idx
            entries.append(cur)

    for i, raw in enumerate(lines):
        ln = i + 1
        if raw.lstrip().startswith("```"):
            fence = not fence
            if cur is not None:
                cur.raw.append(raw)
            continue

        if not fence:
            m = RE_ENTRY.match(raw)
            if m:
                close(i)
                cur = Entry(int(m.group(1)), m.group(2).strip(), src, ln)
                cur.tomb = bool(RE_MERGED_TITLE.match(cur.title) or
                                RE_VOID_TITLE.match(cur.title))
                continue

        if cur is None:
            continue
        cur.raw.append(raw)
        if fence:
            continue

        m = RE_META.match(raw)
        if m and cur.kind is None:
            cur.kind = m.group(1)
            pm = re.search(r"题面\s*(.*?)(?:\s*｜|$)", raw)
            if pm:
                cur.prompt = pm.group(1).strip()
            continue

        m = RE_STATUS.match(raw)
        if m and cur.status_raw is None:
            cur.status_raw = raw
            cur.status_lineno = ln
            body = m.group(1)
            mo = re.search(r"连对\s*(\d+)\s*连错\s*(\d+)", norm(body))
            if mo:
                cur.ok, cur.bad = int(mo.group(1)), int(mo.group(2))
            mo = re.search(r"上次\s*(20\d\d-\d\d-\d\d|—|未测过)", norm(body))
            if mo:
                cur.last = "—" if mo.group(1) in LAST_NEVER else mo.group(1)
            elif any(k in norm(body) for k in LAST_NEVER):
                cur.last = "—"          # 「连对0 连错0 未测过」＝ 省掉了「上次」二字
            if RE_MOVED_OUT.match(body):
                cur.tomb = True
            mo = re.search(r"🎓\s*已毕业\s*(20\d\d-\d\d-\d\d)?", body)
            if mo:
                cur.grad = mo.group(1) or "—"
            for mk in (M_MORPH, M_ONLYLOG, M_SPELL, M_NOREVIEW, M_MERGED, M_STUBBORN):
                if mk in body:
                    cur.marks.add(mk)
            continue

        m = RE_HIST.match(raw)
        if m:
            sym, occ, bold = parse_symbol(m.group(2))
            kind = ("judge" if sym in JUDGE else
                    "neutral" if sym in NEUTRAL else
                    "legacy" if sym in LEGACY else
                    "trace" if sym in TRACE else "unknown")
            cur.history.append(Hist(date=m.group(1), symbol=sym, occasion=occ,
                                    lineno=ln, kind=kind, bold=bold, raw=raw))
    close(len(lines))
    return entries


def load_all():
    return parse_file(PROBLEMS, "problems.md") + parse_file(GRADUATED, "graduated.md")


# ══════════════════════════════════════════════════════════════════════════
#  日型（L1/L2/L3/R）—— 真源 sessions/ 的文件首行
# ══════════════════════════════════════════════════════════════════════════
def day_types():
    """→ [(date, 'L1'|'L2'|'L3'|'R')]，按日期升序。只收有 session 文件的日子。"""
    out = []
    if not os.path.isdir(SESSIONS):
        return out
    for fn in sorted(os.listdir(SESSIONS)):
        if not re.fullmatch(r"20\d\d-\d\d-\d\d\.md", fn):
            continue
        path = os.path.join(SESSIONS, fn)
        with open(path, encoding="utf-8") as f:
            first = f.readline()
        m = RE_DAYTYPE.match(first)
        d = fn[:-3]
        if not m:
            out.append((d, None))
        else:
            out.append((d, m.group(2)))
    return out


def back_days(today, n):
    """D-1 / D-3 ＝ sessions/ 里按日期倒数第 1 / 第 3 个文件（不含 today）。"""
    ds = [d for d, _ in day_types() if d < today]
    return ds[-n] if len(ds) >= n else None


def cycle_start(today):
    """本周期起点 ＝ 上一个 R 之后的第一天（不含 today）。"""
    ds = [(d, t) for d, t in day_types() if d < today]
    for i in range(len(ds) - 1, -1, -1):
        if ds[i][1] == "R":
            return ds[i + 1][0] if i + 1 < len(ds) else today
    return ds[0][0] if ds else today


# ══════════════════════════════════════════════════════════════════════════
#  出题流水（append-only）
# ══════════════════════════════════════════════════════════════════════════
def read_drawn(today):
    used, groups = set(), set()
    if not os.path.exists(DRAWN):
        return used, groups
    for line in open(DRAWN, encoding="utf-8"):
        parts = line.strip().split("\t")
        if len(parts) < 4 or parts[0] != today:
            continue
        groups.add(parts[1])
        if parts[2] == "用":
            used.update(int(x) for x in parts[3].split(",") if x.strip().isdigit())
    return used, groups


def append_drawn(line):
    with open(DRAWN, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# ══════════════════════════════════════════════════════════════════════════
#  check —— 格式校验（SKILL §3.1 机器契约）
# ══════════════════════════════════════════════════════════════════════════
def changed_entries(ents):
    touched, touched_lines = set(), set()
    for path, src in ((PROBLEMS, "problems.md"), (GRADUATED, "graduated.md")):
        if not os.path.exists(path):
            continue
        try:
            out = subprocess.run(["git", "diff", "-U0", "HEAD", "--", path],
                                 cwd=ROOT, capture_output=True, text=True,
                                 timeout=30).stdout
        except Exception:
            continue
        lines = []
        for h in re.finditer(r"^@@ -\S+ \+(\d+)(?:,(\d+))? @@", out, re.M):
            st, cnt = int(h.group(1)), int(h.group(2) or 1)
            lines.extend(range(st, st + max(cnt, 1)))
        touched_lines.update((src, l) for l in lines)
        for e in ents:
            if e.src == src and any(e.start <= l <= (e.end or 10 ** 9) for l in lines):
                touched.add(e.num)
    return touched, touched_lines


def check_entry(e, touched_lines=None, all_nums=None):
    """→ [(level, msg)]  level ∈ ERROR/WARN/INFO
    硬查口径：**本次 diff 里新写的行**，或条目有 ≥ STRICT_FROM 的历史行。
    更早的存量按当时的规矩留痕，只提示不报错。"""
    touched_lines = touched_lines or set()
    P = []
    if e.tomb:
        return P                                    # 墓碑条目不再查
    hard_entry = (e.src, e.status_lineno) in touched_lines or \
                 any(h.date >= STRICT_FROM for h in e.history)

    # ── 契约⑤ 条目内顺序：头 → 元信息 → 状态行 → 历史行（日期升序）→ 备注块 ──────
    #   2026-09-04 加：此前只写在 §3.1 里、没人查 ⇒ 全档 4 条（#1 #88 #95 #136）
    #   把状态行埋在了日志行中间，同日已整改。
    idx = {}
    note_at = None
    hist_after_note = []
    for i, l in enumerate(e.raw):
        if RE_META.match(l):
            idx.setdefault("meta", i)
        elif RE_STATUS.match(l):
            idx.setdefault("stat", i)
        elif RE_HIST.match(l):
            idx.setdefault("hist", i)
            if note_at is not None:
                hist_after_note.append(l.strip()[:28])
        elif RE_NOTE.match(l) and note_at is None:
            note_at = i
    order = [(k, idx[k]) for k in ("meta", "stat", "hist") if k in idx]
    if [v for _, v in order] != sorted(v for _, v in order):
        P.append(("ERROR",
                  "条目内顺序不对（§3.1 契约⑤ 写死：头 → 元信息 → 状态行 → 历史行 → 备注块），"
                  "实际是 " + " → ".join(k for k, _ in sorted(order, key=lambda x: x[1]))))
    if hist_after_note:
        P.append(("ERROR",
                  f"有 {len(hist_after_note)} 条日期行写在 `- 备注` 之后（§3.1 契约⑤）："
                  + "／".join(hist_after_note[:3])))
    hd = [h.date for h in e.history]
    if hd != sorted(hd):
        P.append(("ERROR", "历史行日期乱序（§3.1 契约⑤ 要求日期升序）"))

    if e.status_raw is None:
        P.append(("ERROR", "缺状态行（`状态 连对N 连错N 上次<D|—> …`）"))
        return P
    legacy_grad = e.graduated and re.match(r"^\s*—\s*｜", e.status_raw[2:].strip())
    if e.ok is None or e.bad is None:
        # 🎓 旧账／她指定的条目允许写 `状态 — ｜ **🎓 已毕业 …**`（从来没数过连击）
        if not legacy_grad:
            P.append(("ERROR", "状态行读不出「连对N 连错N」"
                               "（🎓 旧账条目可写 `状态 — ｜ **🎓 已毕业 …**`）"))
    if e.last is None and not legacy_grad:
        P.append(("ERROR", "状态行读不出「上次<YYYY-MM-DD|—>」"))
    if e.kind is None:
        P.append(("WARN", "缺「类型」字段（`类型 X ｜ 题面 …`）"))
    if not e.graduated and not e.prompt:
        P.append(("WARN", "未毕业却没有题面字段 —— 抽到它就必须当场补成完整中文句"))
    if not e.history and not e.graduated:
        P.append(("ERROR", "一条历史行都没有"))

    for h in e.history:
        hard = (e.src, h.lineno) in touched_lines or h.date >= STRICT_FROM
        loc = f"L{h.lineno}"
        if h.bold:
            P.append((("ERROR" if hard else "INFO"),
                      f"{loc} 符号加粗了（`**{h.symbol}**`）—— §3.3 符号紧跟日期、不加粗"))
        if h.kind == "unknown":
            P.append((("ERROR" if hard else "INFO"),
                      f"{loc} {h.date} 这一行切不出符号 ⇒ 按【留痕行】处理，不推进 streak："
                      f"{(h.occasion or '')[:34]}"))
        if h.kind == "legacy":
            P.append(("INFO", f"{loc} {h.date} 📖 已停用（§3.3），只读历史"))

    if e.ok is not None:
        ro, rb = e.recount()
        if (ro, rb) != (e.ok, e.bad):
            P.append((("ERROR" if hard_entry else "INFO"),
                      f"连对连错与历史重数不符：档 {e.ok}/{e.bad} vs 重数 {ro}/{rb}"))
        if not e.graduated and ro >= 2:
            P.append((("ERROR" if hard_entry else "INFO"),
                      f"连对已到 2 —— §3.3 该在原地标 🎓 已毕业"))
    lt = e.last_tested() or "—"
    if (e.last or "—") != lt:
        P.append((("ERROR" if hard_entry else "INFO"),
                  f"「上次」写着「{e.last}」，最后一次被测是「{lt}」"))

    if not e.graduated and e.src == "graduated.md":
        P.append(("ERROR", "在 graduated.md 里却不是 🎓 —— 回潮的条目必须搬回 problems.md"))
    if e.marks & {M_MORPH, M_ONLYLOG} and e.marks & {M_SPELL, M_NOREVIEW}:
        P.append(("WARN", "同时挂了两类「不召回」标记，口径重叠 —— 留一个就够"))
    return P


def fence_balance(path):
    """→ [(开始行, 说明)]  未闭合的代码围栏。
    ⚠️ 这是**文件级**检查，必须在条目检查之前跑 —— 围栏错位会让解析器把后面
    整片条目当成代码块吞掉（2026-08-29 实测：一个漏闭的围栏吞掉 71 个条目）。"""
    if not os.path.exists(path):
        return []
    lines = open(path, encoding="utf-8").read().split("\n")
    bad, stack = [], []
    for i, l in enumerate(lines, 1):
        if not l.lstrip().startswith("```"):
            continue
        if stack:
            open_at = stack.pop()
            # 围栏区间里出现条目头 ⇒ 这个"闭合"是别人的，真正的闭合漏了
            inner = [k for k in range(open_at, i - 1)
                     if RE_ENTRY.match(lines[k])]
            if inner:
                bad.append((open_at, f"L{open_at} 开的代码围栏没闭合 —— 它一路吞掉了 "
                                     f"{len(inner)} 个条目头（首个在 L{inner[0]+1}）"))
        else:
            stack.append(i)
    for open_at in stack:
        bad.append((open_at, f"L{open_at} 开的代码围栏到文件末都没闭合"))
    return bad


def cmd_check(args):
    ents = load_all()
    all_nums = {e.num for e in ents}
    seen, dup = {}, []
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
    print(f"lab.py check · {scope} · 严格分界 {STRICT_FROM}")
    print("═" * 74)
    for n, a, b in dup:
        print(f"ERROR  #{n} 编号重复：{a} 与 {b}（§3.1 编号只增不复用）")

    nerr = nwarn = ninfo = 0
    for path, src in ((PROBLEMS, "problems.md"), (GRADUATED, "graduated.md")):
        for _, msg in fence_balance(path):
            nerr += 1
            print(f"ERROR  {src}  {msg}")
    info_kind = Counter()
    for e in ents:
        if e.num not in target:
            continue
        for level, msg in check_entry(e, touched_lines, all_nums):
            if level == "ERROR":
                nerr += 1
                print(f"ERROR  #{e.num} {e.src}:{e.start}  {msg}")
            elif level == "WARN":
                nwarn += 1
                if not args.quiet:
                    print(f"WARN   #{e.num} {e.src}:{e.start}  {msg}")
            else:
                ninfo += 1
                info_kind[re.sub(r"[#L]?\d+", "N", msg)[:38]] += 1
    print("─" * 74)
    print(f"ERROR {nerr} · WARN {nwarn} · 存量提示 {ninfo}"
          f"（{STRICT_FROM} 之前写下的，不报错）")
    if ninfo and not args.quiet:
        for k, v in info_kind.most_common(8):
            print(f"   存量 · {k} … {v} 处")
    print("═" * 74)
    return 1 if nerr else 0


# ══════════════════════════════════════════════════════════════════════════
#  stats —— 全档统计（SKILL §0.4：每个数带编号清单）
# ══════════════════════════════════════════════════════════════════════════
def fmt_ids(ids, per=16, indent="        "):
    ids = sorted(ids)
    if not ids:
        return ""
    out = []
    for i in range(0, len(ids), per):
        out.append(indent + " ".join("#%d" % n for n in ids[i:i + per]))
    return "\n".join(out)


def redo_queue():
    """redo_queue.md 的表 `| R1 | 题目 | 类型 | 首答 | 上次重答 |`
    → [(编号, 题目, 类型, 上次重答 or None)]，**最久没重答的在前**（§5d）。"""
    if not os.path.exists(REDO):
        return []
    out = []
    for l in open(REDO, encoding="utf-8"):
        m = re.match(r"^\|\s*(R\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|(.*)\|\s*$", l)
        if not m:
            continue
        last = re.search(r"(20\d\d-)?(\d\d)-(\d\d)\s*已重答", m.group(5))
        d = f"2026-{last.group(2)}-{last.group(3)}" if last else None
        out.append((m.group(1), m.group(2).strip(), m.group(3).strip(), d))
    out.sort(key=lambda x: (x[3] or "0000-00-00", int(x[0][1:])))
    return out


def cmd_stats(args):
    ents = load_all()
    act = [e for e in ents if e.active]
    grad = [e for e in act if e.graduated]
    ug = [e for e in act if not e.graduated]
    pending_move = [e for e in grad if e.src == "problems.md"]
    drawable = [e for e in ug if e.drawable]
    ok1 = [e for e in drawable if e.recount()[0] == 1]
    bad2 = [e for e in drawable if e.recount()[1] >= 2]
    noprompt = [e for e in drawable if not e.prompt]
    blocked = defaultdict(list)
    for e in ug:
        r = e.block_reason
        if r:
            blocked[r].append(e.num)
    merged = [e for e in drawable if M_MERGED in e.marks]

    print("═" * 74)
    print("lab.py stats · 全档 ＝ problems.md ＋ graduated.md（两文件合计逐条实数）")
    print("═" * 74)
    print(f"全档总数   {len(act)} 条　＝ problems.md {sum(1 for e in act if e.src=='problems.md')}"
          f" ＋ graduated.md {sum(1 for e in act if e.src=='graduated.md')}"
          f"　（另有墓碑/迁出 {len(ents)-len(act)} 条，不占数）")
    print(f"🎓 已毕业   {len(grad)} 条（占 {len(grad)*100.0/max(len(act),1):.1f}%）")
    if pending_move:
        print(f"   ⏸ 其中 {len(pending_move)} 条还留在 problems.md —— "
              f"**跑 `lab.py migrate` 把它们搬进 graduated.md**（§3.3 / §11）")
        if not args.brief:
            print(fmt_ids([e.num for e in pending_move]))
    print(f"未毕业     {len(ug)} 条")
    print(f"可出题     {len(drawable)} 条　←【复习组只从这里抽】")
    if not args.brief:
        print(fmt_ids([e.num for e in drawable]))
    for r in (M_MORPH, M_ONLYLOG, M_SPELL, M_NOREVIEW):
        if blocked.get(r):
            print(f"   ⛔ 剔除 · {r:<14s} {len(blocked[r])} 条")
            if not args.brief:
                print(fmt_ids(blocked[r]))
    print(f"连对1（差一次毕业） {len(ok1)} 条")
    if not args.brief:
        print(fmt_ids([e.num for e in ok1]))
    print(f"连错≥2             {len(bad2)} 条")
    if not args.brief:
        print(fmt_ids([e.num for e in bad2]))
    if merged:
        print(f"合并条（出题须多句覆盖） {len(merged)} 条")
        if not args.brief:
            print(fmt_ids([e.num for e in merged]))
    if noprompt:
        print(f"⚠️ 题面待补 {len(noprompt)} 条 —— 抽到就必须当场补成完整中文句")
        if not args.brief:
            print(fmt_ids([e.num for e in noprompt]))
    rq = redo_queue()
    never = [r for r in rq if r[3] is None]
    print(f"重答队列   共 {len(rq)} 道 ／ 未重答过 {len(never)} 道（§5d：⛔ 没有顺延这回事）")
    if rq and not args.brief:
        print("   最久没重答的 5 道：" +
              " · ".join(f"{r[0]}({r[3] or '从未'})" for r in rq[:5]))
    ds = day_types()
    if ds:
        print(f"最近日型   " + " ".join(f"{d[5:]}·{t or '?'}" for d, t in ds[-6:]))
    print("═" * 74)
    return 0


# ══════════════════════════════════════════════════════════════════════════
#  list / show / dedup —— 判重三步的机械部分（SKILL §3.1）
# ══════════════════════════════════════════════════════════════════════════
def cmd_list(args):
    ents = [e for e in load_all() if e.active]
    if args.state == "未毕业":
        ents = [e for e in ents if not e.graduated]
    elif args.state == "🎓":
        ents = [e for e in ents if e.graduated]
    if args.type:
        ents = [e for e in ents if e.kind == args.type]
    if args.drawable:
        ents = [e for e in ents if e.drawable]
    print(f"# lab.py list · {len(ents)} 条（非 detail；判重第 ① 步先在这里眼过一遍）")
    for e in sorted(ents, key=lambda x: x.num):
        flag = "🎓" if e.graduated else ("⛔" if e.block_reason else "  ")
        print(f"{flag} #{e.num:<4d} {e.kind or '—':<4s} {e.title[:66]}")
    return 0


def cmd_show(args):
    idx = {e.num: e for e in load_all()}
    lines = {}
    for path, src in ((PROBLEMS, "problems.md"), (GRADUATED, "graduated.md")):
        if os.path.exists(path):
            lines[src] = open(path, encoding="utf-8").read().split("\n")
    for a in args.nums:
        n = int(str(a).lstrip("#"))
        e = idx.get(n)
        if not e:
            print(f"⛔ 全档查无 #{n}")
            continue
        L = lines[e.src]
        print("─" * 74)
        print(f"# {e.src}:{e.start}-{e.end}")
        print("\n".join(L[e.start - 1:(e.end or len(L))]).rstrip())
    return 0


FIELD_W = {"标题": 3, "题面": 2, "历史": 1}


def cmd_dedup(args):
    ents = [e for e in load_all() if e.active]
    terms = [t.strip() for t in args.terms if t.strip()]
    scored = []
    for e in ents:
        hits, sc = [], 0
        body = "\n".join(e.raw)
        fields = {"标题": e.title, "题面": e.prompt or ""}
        if not args.no_history:
            fields["历史"] = body
        for t in terms:
            tl = t.lower()
            ascii_term = re.fullmatch(r"[A-Za-z][A-Za-z'\- ]*", t) is not None
            pat = re.compile(r"(?<![A-Za-z])" + re.escape(tl) + r"(?![A-Za-z])") \
                if ascii_term else None
            for f, txt in fields.items():
                low = (txt or "").lower()
                found = bool(pat.search(low)) if pat else (tl in low)
                if found:
                    sc += FIELD_W[f]
                    hits.append(f"{f}:{t}")
        if sc:
            scored.append((sc, e, hits))
    # 规则字段（标题/题面）命中优先，避免长条目靠正文体量刷分
    scored.sort(key=lambda x: (-sum(1 for h in x[2] if not h.startswith("历史")),
                               -x[0], x[1].num))
    print("═" * 74)
    print(f"lab.py dedup · 查 {terms} · 命中 {len(scored)} 条"
          f"（⛔ 这只是把候选捞出来给人看，判断必须逐条读完再下 —— §4④1b）")
    print("═" * 74)
    for sc, e, hits in scored[:args.limit]:
        flag = "🎓" if e.graduated else ("⛔" if e.block_reason else "  ")
        print(f"{flag} #{e.num:<4d} [{sc:>2d}] {e.kind or '—':<4s} {e.title[:56]}")
        print(f"        题面 {(e.prompt or '（无）')[:62]}")
        print(f"        命中 {' · '.join(sorted(set(hits))[:6])}")
    if len(scored) > args.limit:
        print(f"   … 还有 {len(scored)-args.limit} 条未列（--limit 调大）")
    print("═" * 74)
    return 0


# ══════════════════════════════════════════════════════════════════════════
#  session 扫描器 —— deliver 与 lookback 共用（SKILL §9.1 session 机器契约）
#
#  ⛔ 严格匹配，不做兜底：session 写歪了 ⇒ deliver 报错 ⇒ **改 session，不改脚本**。
#  DELIVER_FROM 之前的 session 是存量，只提示不报错（与 check 的存量口径同一个设计）。
# ══════════════════════════════════════════════════════════════════════════
DELIVER_FROM = "2026-09-05"

RE_SESS_NAME = re.compile(r"^(20\d\d-\d\d-\d\d)\.md$")
RE_H2 = re.compile(r"^## +(.*?)\s*$")
RE_H3 = re.compile(r"^### +(.*?)\s*$")
RE_SEC_GROUP = re.compile(r"^[①]?\s*复习组\s*·\s*第\s*(\d+)\s*组")
RE_SEC_NEW = re.compile(r"^[③]?\s*新题\b")
# ⚠️ 这三条 2026-09-04 修过：原来 `^[d]?\s*段?\s*重答` 认不出 `d 段 · 整题重答 2 道`，
#    `^加练` 认不出 `③b 加练新题` ⇒ **重答与加练整类都没被扫到**（漏了 8 个节）。
RE_SEC_REDO = re.compile(r"^[dⓓ][\s·dD]*段|重答")
RE_SEC_EXTRA = re.compile(r"^\S{0,3}\s*加练")
RE_SEC_LOOK = re.compile(r"^[⓪②]?\s*回看\b")
RE_GROUP_N = re.compile(r"（\s*(\d+)\s*题\s*）")
RE_BANK = re.compile(r"bank\s*[:：]\s*(\d+)")
RE_REDO_ID = re.compile(r"\bR(\d+)\b")
RE_QBLOCK = re.compile(r"^\[(\d+)\]\s*#(\d+)\s*·")
RE_SBLOCK = re.compile(r"^\[S(\d+)\]")
RE_LOOK_NONE = re.compile(r"无(（|$|\s)")
# 认不出的 `##` 里，只有这些算「把上一节收掉」（其余一律并入当前节）
RE_SEC_CLOSE = re.compile(r"收尾|本日纵向|待她裁|明天进场")

Q_LABELS = ["原句", "判定", "最小改", "更好版"]
DIFF_LABELS = ["diff-1", "diff-2"]
FREE_H3 = [("① 最小修改版", "最小修改版"), ("② 更好版", "更好版"), ("③ 逐句 diff", "逐句 diff")]
EMPTY_BETTER = "无更好版本"
EMPTY_DIFF = "无 diff"


def _fences(lines):
    """→ [(起, 止)] 顶格 ``` 围栏的行区间（含边界行下标）。"""
    out, open_at = [], None
    for i, l in enumerate(lines):
        if l.startswith("```"):
            if open_at is None:
                open_at = i
            else:
                out.append((open_at, i))
                open_at = None
    return out, open_at


def scan_session(path):
    """把一个 session 切成节。→ dict(date, sections=[…], fence_open)"""
    lines = open(path, encoding="utf-8").read().split("\n")
    fences, unclosed = _fences(lines)
    inf = set()
    for a, b in fences:
        inf.update(range(a, b + 1))
    secs, cur = [], None
    for i, l in enumerate(lines):
        if i in inf:
            continue
        m = RE_H2.match(l)
        if not m:
            continue
        title = m.group(1)
        # ★ 判序写死：**回看最先** —— 「② 回看 · D-1 两道整题重答」标题里带「整题重答」，
        #   先判 redo 会把回看节误判成重答节（2026-09-04 实测）。
        kind = ("look" if RE_SEC_LOOK.match(title) else
                "group" if RE_SEC_GROUP.match(title) else
                "new" if RE_SEC_NEW.match(title) else
                "redo" if RE_SEC_REDO.search(title) else
                "extra" if RE_SEC_EXTRA.match(title) else "other")
        # ★ 节的作用域：一组的【出题】与【判定/三件套】常常写成两个 `##`
        #   （实证 09-04：`## ① 复习组 · 第 1 组（3 题）` ＋ `## ① 第 1 组 · 判前自审`）。
        #   ⇒ **认不出的 `##` 并入当前节**，只在【认得出的节标题】或【收尾】处闭合。
        #   ⛔ 不做兜底的是节标题本身的写法（§9.1），不是这条作用域规则。
        if kind == "other" and not RE_SEC_CLOSE.search(title):
            continue
        if cur:
            cur["end"] = i
        if kind == "other":
            cur = None
            continue
        cur = dict(kind=kind, title=title, line=i + 1, start=i, end=len(lines))
        secs.append(cur)
    d = RE_SESS_NAME.match(os.path.basename(path))
    return dict(date=d.group(1) if d else "?", path=path, lines=lines,
                sections=secs, fences=fences, unclosed=unclosed, infence=inf)


def _blocks_in(sc, sec, head_re):
    """节内、围栏里的块：块头匹配 head_re ⇒ 块体到下一个块头／围栏结束。"""
    out = []
    for a, b in sc["fences"]:
        if not (sec["start"] <= a < sec["end"]):
            continue
        cur = None
        for i in range(a + 1, b):
            m = head_re.match(sc["lines"][i])
            if m:
                cur = dict(m=m, line=i + 1, body=[])
                out.append(cur)
            elif cur is not None:
                cur["body"].append(sc["lines"][i])
    return out


# diff 段里的小标题（`diff-1  原句 → 最小改`）不是内容行，也不能顶替块头的六项
RE_DIFF_CAPTION = re.compile(r"^(原句|最小改|更好版)\s*→\s*(原句|最小改|更好版)\s*$")
RE_DIFF_SENT = re.compile(r"^(原句|最小改|更好版)\s+\S")


def _head_area(body):
    """块头的六项只认【第一个 diff- 之前】那一段 ——
    ⛔ 不能被 diff 段里的 `原句 …`／`最小改 …` 顶替（它们是 diff 的两行完整句）。"""
    out = []
    for l in body:
        if any(l.strip().startswith(x) for x in DIFF_LABELS):
            break
        out.append(l)
    return out


def _has_label(body, label):
    for l in body:
        s = l.strip()
        if s.startswith(label):
            return s[len(label):].strip()
    return None


def check_session(sc, only=None):
    """→ [(level, 位置, 说明)]"""
    P = []
    hard = sc["date"] >= DELIVER_FROM
    LV = "ERROR" if hard else "INFO"
    if sc["unclosed"] is not None:
        P.append(("ERROR", f"L{sc['unclosed']+1}", "有一个 ``` 围栏没闭合 —— 后面整片会被吞成代码块"))
    kinds = [s["kind"] for s in sc["sections"]]
    if "group" not in kinds and "new" not in kinds and "redo" not in kinds:
        P.append((LV, "-", "整份 session 里认不出任何【复习组／新题／重答】节 —— §9.1 节标题写歪了"))

    for sec in sc["sections"]:
        if only and sec["kind"] != only:
            continue
        loc = f"L{sec['line']}"
        t = sec["title"]

        if sec["kind"] == "group":
            m = RE_GROUP_N.search(t)
            blocks = _blocks_in(sc, sec, RE_QBLOCK)
            if not m:
                P.append((LV, loc, f"复习组节标题没写（N 题）：`{t[:40]}` —— §9.1 要求写死题数"))
            elif len(blocks) != int(m.group(1)):
                P.append((LV, loc,
                          f"标题写着 {m.group(1)} 题，节里只有 {len(blocks)} 个 `[n] #NNN ·` 三件套块"))
            if not blocks:
                P.append((LV, loc, "复习组节里一个三件套块都没有（§7 每题都要给，含全对的）"))
            seen = set()
            for b in blocks:
                bl = f"L{b['line']}"
                idx, num = b["m"].group(1), b["m"].group(2)
                if num in seen:
                    P.append((LV, bl, f"#{num} 在同一节里出现两次"))
                seen.add(num)
                headA = _head_area(b["body"])
                for lab_ in Q_LABELS:
                    v = _has_label(headA, lab_)
                    if v is None:
                        P.append((LV, bl, f"[{idx}] #{num} 缺「{lab_}」行（§7 六项一项不许省）"))
                    elif not v:
                        P.append((LV, bl, f"[{idx}] #{num} 的「{lab_}」是空的"))
                better = _has_label(b["body"], "更好版")
                if better is not None and not better:
                    pass
                for lab_ in DIFF_LABELS:
                    v = _has_label(b["body"], lab_)
                    if v is None:
                        P.append((LV, bl, f"[{idx}] #{num} 缺「{lab_}」段（§7③ 两段必须分开）"))
                        continue
                    seg = _diff_seg(b["body"], lab_)
                    if not seg:
                        P.append((LV, bl, f"[{idx}] #{num} 的「{lab_}」段是空的"))
                    elif EMPTY_DIFF not in " ".join(seg) and len(_diff_sentences(seg)) < 2:
                        P.append((LV, bl,
                                  f"[{idx}] #{num} 的「{lab_}」有改动却没摆两行完整句"
                                  f"（§7③：⛔ 只写 xxx → yyy 不算 diff）"))
            h3 = [RE_H3.match(sc["lines"][i]).group(1)
                  for i in range(sec["start"], sec["end"])
                  if i not in sc["infence"] and RE_H3.match(sc["lines"][i])]
            if not any("新建条目" in x for x in h3):
                P.append((LV, loc, "缺【本组新建条目】块（§7「新建条目必须让她看见」，没有也要写「无」）"))

        elif sec["kind"] in ("new", "redo", "extra"):
            if sec["kind"] == "new" and not RE_BANK.search(t):
                P.append((LV, loc, f"新题节标题没带题号：`{t[:40]}` —— §9.1 要求写 `bank:NNN`"))
            if sec["kind"] == "redo" and not RE_REDO_ID.search(t):
                P.append((LV, loc, f"重答节标题没带 `RN`：`{t[:40]}`"))
            h3 = {RE_H3.match(sc["lines"][i]).group(1): i + 1
                  for i in range(sec["start"], sec["end"])
                  if i not in sc["infence"] and RE_H3.match(sc["lines"][i])}
            for want, key in FREE_H3:
                if not any(key in x for x in h3):
                    P.append((LV, loc, f"自由产出缺 `### {want}` 这一节（§7 四件套）"))
            sb = _blocks_in(sc, sec, RE_SBLOCK)
            if not sb:
                P.append((LV, loc, "逐句 diff 里一个 `[S1]` 块都没有（§7③ 多句逐句走两段）"))
            for b in sb:
                bl = f"L{b['line']}"
                sid = b["m"].group(1)
                for lab_ in DIFF_LABELS:
                    if _has_label(b["body"], lab_) is None:
                        P.append((LV, bl, f"[S{sid}] 缺「{lab_}」段（§7③）"))
                        continue
                    seg = _diff_seg(b["body"], lab_)
                    if seg and EMPTY_DIFF not in " ".join(seg) \
                            and len(_diff_sentences(seg)) < 2:
                        P.append((LV, bl,
                                  f"[S{sid}] 的「{lab_}」有改动却没摆两行完整句（§7③）"))

        elif sec["kind"] == "look":
            rest = RE_SEC_LOOK.sub("", t).strip(" ·").strip()
            if not (RE_BANK.search(t) or RE_REDO_ID.search(t) or RE_LOOK_NONE.match(rest)):
                P.append((LV, loc,
                          f"回看节标题没写回看的是哪一篇：`{t[:44]}` —— "
                          f"§9.1 要求写 `## ② 回看 · bank:NNN`（没得回看写 `· 无（理由）`）"))
    return P


def _diff_seg(body, label):
    """取 diff-1／diff-2 标签之后、下一个 diff 标签之前的非空行。
    标签行的尾巴照收（自由产出写成 `diff-1  原句   I need …`），
    但小标题 `原句 → 最小改` 会在下面被 RE_DIFF_CAPTION 滤掉。"""
    out, on = [], False
    for l in body:
        s = l.strip()
        if s.startswith(label):
            on = True
            tail = s[len(label):].strip()
            if tail:
                out.append(tail)
            continue
        if on and any(s.startswith(x) for x in DIFF_LABELS):
            break
        if on and s:
            out.append(s)
    return out


def _diff_sentences(seg):
    """段里【摆出来的完整句】＝ 以 原句／最小改／更好版 打头且不是小标题的行。"""
    return [s for s in seg if RE_DIFF_SENT.match(s) and not RE_DIFF_CAPTION.match(s)]


def cmd_deliver(args):
    path = args.session
    if not os.path.isabs(path) and not os.path.exists(path):
        path = os.path.join(SESSIONS, os.path.basename(path))
    if not os.path.exists(path):
        sys.exit(f"⛔ session 文件不存在：{args.session}")
    sc = scan_session(path)
    only = {"复习组": "group", "新题": "new", "重答": "redo", "加练": "extra",
            "回看": "look"}.get(args.section) if args.section else None
    if args.section and only is None:
        sys.exit(f"⛔ --section 只认 复习组／新题／重答／加练／回看，收到「{args.section}」")
    P = check_session(sc, only)
    W = "═" * 78
    print(W)
    print(f"lab.py deliver · {os.path.basename(path)} · 交付物硬闸（§7 / §9.1）")
    print(W)
    print(f"  日期 {sc['date']}　节 {len(sc['sections'])} 个："
          + "／".join(f"{s['kind']}@L{s['line']}" for s in sc["sections"] if s["kind"] != "other"))
    if sc["date"] < DELIVER_FROM:
        print(f"  ⚠️ 这份 session 早于 {DELIVER_FROM} ⇒ **存量**：只提示，不报错（§9.1）")
    print("─" * 78)
    err = [x for x in P if x[0] == "ERROR"]
    warn = [x for x in P if x[0] == "WARN"]
    info = [x for x in P if x[0] == "INFO"]
    for lv, loc, msg in err + warn:
        print(f"{lv:<6} {loc:<8} {msg}")
    if info:
        print(f"存量提示 {len(info)} 条（{sc['date']} < {DELIVER_FROM}，不报错）")
        for lv, loc, msg in info[:12]:
            print(f"       {loc:<8} {msg}")
        if len(info) > 12:
            print(f"       …… 还有 {len(info)-12} 条")
    print("─" * 78)
    print(f"⇒ ERROR {len(err)} · WARN {len(warn)} · 存量提示 {len(info)}"
          + ("　⇒ **可以发**" if not err else "　⇒ ⛔ **不许发**"))
    print(W)
    return 1 if err else 0


# ══════════════════════════════════════════════════════════════════════════
#  lookback —— 哪几篇自由产出还没被回看过（SKILL §4② / §5⓪）
#     ⛔ 只读：不写任何文件。
# ══════════════════════════════════════════════════════════════════════════
def scan_all_sessions():
    news, looked = [], {}
    if not os.path.isdir(SESSIONS):
        return news, looked
    for f in sorted(os.listdir(SESSIONS)):
        if not RE_SESS_NAME.match(f):
            continue
        sc = scan_session(os.path.join(SESSIONS, f))
        for s in sc["sections"]:
            if s["kind"] in ("new", "redo", "extra"):
                ids = ["bank:" + m.group(1) for m in RE_BANK.finditer(s["title"])]
                ids += ["R" + m.group(1) for m in RE_REDO_ID.finditer(s["title"])]
                for pid in (ids or [None]):
                    # 同一文件同一题号只算一篇：抽题记录节与逐题记录节是同一篇产出
                    if pid and any(x["file"] == f and x["id"] == pid for x in news):
                        continue
                    news.append(dict(id=pid, kind=s["kind"], date=sc["date"],
                                     title=s["title"], line=s["line"], file=f))
            elif s["kind"] == "look":
                for m in RE_BANK.finditer(s["title"]):
                    looked.setdefault("bank:" + m.group(1), []).append((sc["date"], f, s["line"]))
                for m in RE_REDO_ID.finditer(s["title"]):
                    looked.setdefault("R" + m.group(1), []).append((sc["date"], f, s["line"]))
    return news, looked


def cmd_lookback(args):
    today = args.date or date.today().isoformat()
    news, looked = scan_all_sessions()
    W = "═" * 78
    print(W)
    print(f"lab.py lookback · {today} · §4② 回看目标　【只读：⛔ 不写任何文件】")
    print(W)
    print("  口径　回看目标 ＝ **最近一篇【没被回看过】的自由产出**（新题／重答／加练）")
    print("  认法　自由产出 ＝ session 里 `## ③ 新题 …（bank:NNN）` / `## d 段 重答 · RN` 的标题行")
    print("  　　　已回看 ＝ 任意 session 的 `## ② 回看 · bank:NNN` **标题行**上的题号")
    print(f"  扫的　{SESSIONS}/*.md")
    print()
    print("① 全部自由产出（逐条列）")
    noid = [x for x in news if not x["id"]]
    for x in news:
        tag = x["id"] or "⛔无题号"
        if x["id"] and x["id"] in looked:
            mark = "✅ 已回看　← " + "／".join(f"{d}:{f}:{l}" for d, f, l in looked[x["id"]])
        elif not x["id"]:
            mark = "⛔ 标题没带题号 ⇒ 追不了（§9.1 要求写 bank:NNN／RN）"
        elif x["date"] >= today:
            mark = "⚠️ 今天（或更晚）写的 ⇒ 本次⛔不作目标"
        else:
            mark = "⏳ 未回看"
        print(f"   {tag:<10} {x['date']}  {x['file']}:{x['line']}  {mark}")
    print(f"   ── 共 {len(news)} 篇（其中 {len(noid)} 篇标题没带题号）")
    print()
    cand = [x for x in news if x["id"] and x["id"] not in looked and x["date"] < today]
    print("② 本次回看目标")
    if not cand:
        print("   （没有未回看的自由产出 ⇒ 写一句「无自由产出可回看」跳过）")
    else:
        t = max(cand, key=lambda x: (x["date"], x["line"]))
        print(f"   ★ {t['id']}　{t['date']}　{t['file']}:{t['line']}")
        print(f"     标题：{t['title'][:60]}")
        print(f"     ⇒ 四件套逐字取自这一节，⛔ 禁止重新推导（§4②）")
        if len(cand) > 1:
            print(f"     （另有 {len(cand)-1} 篇也没回看过："
                  + "／".join(x["id"] for x in sorted(cand, key=lambda x: x['date'])[:6]) + "）")
    print(W)
    return 0

# ══════════════════════════════════════════════════════════════════════════
#  prompts —— 题面逐字核对（SKILL §6「执行动作写死」的机器版）
#
#  §6 原来写的是三步手工仪式：① 先 grep/awk 打出整行 ② 从打出来的那行复制
#  ③ 发送前逐句对一遍。第 ③ 步是纯散文钩子 —— 写作线的实证是这种钩子活不过一天。
#  本命令把 ① 和 ③ 都变成机器动作：
#      lab.py prompts 315 316 317              打出这几条的【元信息整行】，供逐字复制
#      lab.py prompts --verify draft.md 315 …  拿发题稿与档案逐字比，不一致 ⇒ ERROR
#
#  核对口径（⛔ 不做兜底、不做模糊匹配）：
#     题面字段里的每一个【引号句】与每一个【括号限定】都必须**逐字**出现在发题稿里。
#     · 引号句 ＝ 要她翻译的中文本体　　· 括号限定 ＝ 点名（§6 出题前自查的落点）
#     ⇒ 少一句 ＝ 改了题面；丢一个括号 ＝ 把点名吞了（她会答对却被判没到考点）
# ══════════════════════════════════════════════════════════════════════════
RE_Q = re.compile(r"[\"“]([^\"”]{2,})[\"”]")
RE_PAREN = re.compile(r"（([^（）]{2,})）")


def prompt_pieces(prompt):
    """题面 → (引号句列表, 括号限定列表)。⛔ 逐字，不归一化。"""
    if not prompt:
        return [], []
    return RE_Q.findall(prompt), RE_PAREN.findall(prompt)


def cmd_prompts(args):
    ents = {e.num: e for e in load_all()}
    nums = []
    for x in (args.nums or []):
        for y in re.split(r"[,\s]+", str(x)):
            y = y.strip().lstrip("#")
            if y:
                nums.append(int(y))
    if not nums:
        sys.exit("⛔ 要核对哪几条？`lab.py prompts 315 316 317`")
    miss = [n for n in nums if n not in ents]
    if miss:
        sys.exit(f"⛔ 全档没有这些编号：{miss}")

    W = "═" * 78
    print(W)
    print("lab.py prompts · 题面逐字核对（§6）")
    print(W)
    print("① 档案原文（发题稿**只许从这里复制**，⛔ 不许照着标题现想句子）")
    for n in nums:
        e = ents[n]
        meta = next((l for l in e.raw if RE_META.match(l)), None)
        loc = f"{e.src}:{e.start}"
        if meta is None:
            print(f"   #{n:<5} ⛔ 这一条没有【类型 … ｜ 题面 …】元信息行（{loc}）")
            continue
        off = e.raw.index(meta) + 1
        print(f"   #{n:<5} {e.src}:{e.start + off}")
        print(f"          {meta}")
    if not args.verify:
        print("─" * 78)
        todo = [n for n in nums if not ents[n].prompt]
        if todo:
            print(f"⛔ 题面待补 {len(todo)} 条：{' '.join('#'+str(x) for x in todo)}"
                  f" —— §6 出不了题，先补题面再出")
        print("② 发题稿写好后，⛔ 必须回来跑一次：")
        print(f"   lab.py prompts --verify <发题稿文件> {' '.join(str(x) for x in nums)}")
        print(W)
        return 1 if todo else 0

    if not os.path.exists(args.verify):
        sys.exit(f"⛔ 发题稿文件不存在：{args.verify}")
    draft = open(args.verify, encoding="utf-8").read()
    print("─" * 78)
    print(f"② 逐字核对：{os.path.basename(args.verify)}（{len(draft)} 字）")
    errs = []
    for n in nums:
        e = ents[n]
        qs, ps = prompt_pieces(e.prompt)
        if not e.prompt:
            errs.append((n, "题面待补 —— §6 出不了题"))
            continue
        if not qs:
            errs.append((n, f"题面里没有引号句，脚本核不了：{e.prompt[:40]}"))
            continue
        for q in qs:
            if q not in draft:
                errs.append((n, f"发题稿里找不到这一句（逐字）：「{q}」"))
        for p in ps:
            if p not in draft:
                errs.append((n, f"发题稿里丢了这个括号限定（＝点名被吞）：「（{p}）」"))
        ok_q = sum(1 for q in qs if q in draft)
        ok_p = sum(1 for p in ps if p in draft)
        flag = "✅" if (ok_q == len(qs) and ok_p == len(ps)) else "⛔"
        print(f"   {flag} #{n:<5} 引号句 {ok_q}/{len(qs)} ｜ 括号限定 {ok_p}/{len(ps)}")
    print("─" * 78)
    if errs:
        print(f"⛔ **{len(errs)} 处不一致 —— 不许发题**（§6 题面逐字）")
        for n, m in errs:
            print(f"   #{n}  {m}")
        print(W)
        return 1
    print(f"✅ {len(nums)} 条题面逐字一致 —— 可以发（§6.5 审核表第 5 项的证据就是这一段）")
    print(W)
    return 0

# ══════════════════════════════════════════════════════════════════════════
#  migrate —— problems.md ⇄ graduated.md 双向搬迁（SKILL §3.3 / §11）
#
#  ⛔ 本命令【一个字都不产生】：只把**已经存在的整块字节**从一个文件搬到另一个。
#     判断（谁毕业、谁回潮）仍然全部由教练手写状态行，脚本只认状态行的 🎓。
#       problems.md 里状态有 🎓  ⇒ 搬进 graduated.md
#       graduated.md 里没有 🎓   ⇒ 搬回 problems.md（＝ 🎓 后回潮的）
#       墓碑/迁出条目 ⇒ ⛔ 一律不动（它们是指针，留在原地）
#
#  切块口径（本函数是全脚本唯一一处「档案的块状结构」定义）：
#     文件 ＝ header ＋ Σ(块 body ＋ 块 trail) ＋ trailer
#       header   第一个 `### N ·` 之前的全部行
#       块       一个条目：`### N · 标题` → 尾部分隔行之前
#       trail    紧跟其后的空行／`---`（＝ 这个块与下一个块之间的「缝」）
#       trailer  最后一个条目之后、以 `#`/`##` 开头的收尾节（problems.md 的「迁移说明」）
#     ⇒ 拼回去必须与原文逐字节相同（每次都先自校这一条，不过就退出）
# ══════════════════════════════════════════════════════════════════════════

ENTRY_GAP = [""]                 # 条目与条目之间的缝


class Blk:
    __slots__ = ("num", "body", "trail")

    def __init__(self, num, body, trail):
        self.num = num
        self.body = body          # 条目头那行 + 正文，⛔ 逐字不动
        self.trail = trail        # 块后面的缝

    def __repr__(self):
        return f"<Blk #{self.num} body={len(self.body)} trail={self.trail!r}>"


def split_file(path):
    """→ (header, [Blk…], trailer, 原文本)。⛔ 严格：拼回去与原文逐字节相同。"""
    text = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    lines = text.split("\n")
    heads, tops, fence = [], [], False
    for i, l in enumerate(lines):
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if RE_ENTRY.match(l):
            heads.append(i)
        elif re.match(r"^#{1,2} ", l):
            tops.append(i)
    if not heads:                                   # 还没有条目（graduated.md 初始态）
        return lines, [], [], text
    # trailer ＝ 最后一个条目之后的第一个 `#`/`##` 节
    after = [t for t in tops if t > heads[-1]]
    tstart = after[0] if after else len(lines)
    inner = [t for t in tops if heads[0] < t < heads[-1]]
    if inner:
        sys.exit(f"⛔ {os.path.basename(path)} L{inner[0]+1} 有个 `#`/`##` 标题夹在条目中间"
                 f"（{lines[inner[0]][:40]}）—— 脚本读不懂这个结构，先修档案")
    header = lines[:heads[0]]
    trailer = lines[tstart:]
    blocks = []
    for k, i in enumerate(heads):
        stop = heads[k + 1] if k + 1 < len(heads) else tstart
        j = stop
        while j > i + 1 and lines[j - 1].strip() in ("", "---"):
            j -= 1
        blocks.append(Blk(int(RE_ENTRY.match(lines[i]).group(1)), lines[i:j], lines[j:stop]))
    back = header[:]
    for b in blocks:
        back += b.body + b.trail
    back += trailer
    if "\n".join(back) != text:
        sys.exit(f"⛔ {os.path.basename(path)} 切块自校失败 —— 脚本读不懂这个文件，⛔ 不动它")
    return header, blocks, trailer, text


def join_file(header, blocks, trailer):
    out = header[:]
    for b in blocks:
        out += b.body + b.trail
    return "\n".join(out + trailer)


def _msg_key(msg):
    return re.sub(r"\bL\d+\b", "L*", msg)


def _errmap(ents, all_nums):
    out = Counter()
    for e in ents:
        for level, msg in check_entry(e, set(), all_nums):
            out[(e.num, level, _msg_key(msg))] += 1
    return out


def _statesnap(ents):
    return {e.num: (e.status_raw, e.ok, e.bad, e.grad, tuple(sorted(e.marks)),
                    e.kind, e.prompt, len(e.history), e.tomb) for e in ents}


def cmd_migrate(args):
    ph, pb, pt, ptext = split_file(PROBLEMS)
    gh, gb, gt, gtext = split_file(GRADUATED)
    body_before = {}
    for bl in (pb, gb):
        for b in bl:
            if b.num in body_before:
                sys.exit(f"⛔ #{b.num} 在全档出现了两次 —— 先修重号再搬")
            body_before[b.num] = tuple(b.body)

    ents0 = load_all()
    nums0 = {e.num for e in ents0}
    err0, snap0 = _errmap(ents0, nums0), _statesnap(ents0)
    pre_err = sum(v for (n, lv, m), v in err0.items() if lv == "ERROR")

    by_num = {e.num: e for e in ents0}
    p2g = sorted(e.num for e in ents0
                 if e.src == "problems.md" and e.graduated and not e.tomb)
    g2p = sorted(e.num for e in ents0
                 if e.src == "graduated.md" and not e.graduated and not e.tomb)

    W = "═" * 78
    print(W)
    print("lab.py migrate · problems.md ⇄ graduated.md 双向搬迁（§3.3 / §11）")
    print(W)
    if pre_err:
        print(f"⚠️ 搬之前全档已有 {pre_err} 处 ERROR —— 搬迁不修它们、也不新增；"
              f"搬完照常跑 `check --all`")
    if not p2g and not g2p:
        print("两边都没有要搬的：problems.md 无 🎓 · graduated.md 无非 🎓 ⇒ 无操作")
        print(f"全档 {len(body_before)} 条 ＝ problems.md {len(pb)} ＋ graduated.md {len(gb)}")
        print(W)
        return 0
    print(f"problems.md → graduated.md  {len(p2g)} 条（状态行有 🎓）")
    print(fmt_ids(p2g))
    print(f"graduated.md → problems.md  {len(g2p)} 条（状态行已无 🎓 ＝ 🎓 后回潮）")
    print(fmt_ids(g2p) if g2p else "        （无）")
    if args.dry_run:
        print("─" * 78)
        print("--dry-run：⛔ 没有写盘。去掉 --dry-run 才真搬。")
        print(W)
        return 0

    def take(blocks, nums):
        got, idx = {}, []
        for i, b in enumerate(blocks):
            if b.num in nums:
                got[b.num] = b
                idx.append(i)
        for i in reversed(idx):
            # 缝交给前一个块（族间/收尾的 `---` 因此不会被带走）；
            # 下标 0 没有"前一个块" ⇒ 缝直接丢掉，下一块自带自己的缝。
            if i > 0:
                blocks[i - 1].trail = blocks[i].trail
            del blocks[i]
        return got

    def put(blocks, header, blk):
        at = len(blocks)
        for i, b in enumerate(blocks):
            if b.num > blk.num:
                at = i
                break
        if at == 0:
            blk.trail = list(ENTRY_GAP) if blocks else list(ENTRY_GAP)
            if blocks:
                blk.trail = list(ENTRY_GAP)
            blocks.insert(0, blk)
            if header and header[-1].strip():          # 目标文件头部没留空行 ⇒ 补一行
                header.append("")
        else:
            prev = blocks[at - 1]
            blk.trail = prev.trail
            prev.trail = list(ENTRY_GAP)
            blocks.insert(at, blk)

    got_p = take(pb, set(p2g))
    got_g = take(gb, set(g2p))
    for n in p2g:
        put(gb, gh, got_p[n])
    for n in g2p:
        put(pb, ph, got_g[n])
    if gb and gb[-1].trail == []:                      # 目标文件末尾留一个空行收口
        gb[-1].trail = list(ENTRY_GAP)
    if pb and pb[-1].trail == [] and not pt:
        pb[-1].trail = list(ENTRY_GAP)

    new_p, new_g = join_file(ph, pb, pt), join_file(gh, gb, gt)
    open(PROBLEMS, "w", encoding="utf-8").write(new_p)
    open(GRADUATED, "w", encoding="utf-8").write(new_g)

    def rollback(why, detail):
        open(PROBLEMS, "w", encoding="utf-8").write(ptext)
        open(GRADUATED, "w", encoding="utf-8").write(gtext)
        print("─" * 78)
        print(f"⛔ 搬完自校不过：{why} —— 两个文件已整批回滚，档案回到搬之前")
        for d in detail[:20]:
            print("   " + d)
        print(W)
        return 1

    ph2, pb2, pt2, _ = split_file(PROBLEMS)
    gh2, gb2, gt2, _ = split_file(GRADUATED)
    body_after, dup = {}, []
    for bl in (pb2, gb2):
        for b in bl:
            if b.num in body_after:
                dup.append(b.num)
            body_after[b.num] = tuple(b.body)
    if dup:
        return rollback("搬完出现重号", [f"#{x}" for x in sorted(set(dup))])
    if set(body_after) != set(body_before):
        lost = sorted(set(body_before) - set(body_after))
        extra = sorted(set(body_after) - set(body_before))
        return rollback("条目集合变了", [f"丢了 #{x}" for x in lost] + [f"多了 #{x}" for x in extra])
    diff = [n for n in body_before if body_before[n] != body_after[n]]
    if diff:
        return rollback("有条目正文被改动了（搬迁必须逐字节原样）", [f"#{x}" for x in sorted(diff)])
    if ph2 != ph or pt2 != pt or gt2 != gt:
        return rollback("文件的头部/收尾节被动过（⛔ 搬迁不碰它们）", ["header 或 trailer"])
    ents1 = load_all()
    snap1 = _statesnap(ents1)
    bad = [n for n in snap0 if snap0.get(n) != snap1.get(n)]
    if bad:
        return rollback("有条目的状态字段变了（⛔ 搬迁不改状态/连对/连错/标记/题面）",
                        [f"#{n}" for n in sorted(bad)])
    err1 = _errmap(ents1, {e.num for e in ents1})
    new_errs = [f"#{n} {lv} {m}" for (n, lv, m), c in (err1 - err0).items()]
    if new_errs:
        return rollback(f"多出 {len(new_errs)} 处 check 报告", sorted(new_errs))
    wrong = [f"#{e.num} 状态{'有' if e.graduated else '无'} 🎓 却住在 {e.src}"
             for e in ents1 if not e.tomb and (e.graduated != (e.src == "graduated.md"))]
    for bl, name in ((pb2, "problems.md"), (gb2, "graduated.md")):
        order = [b.num for b in bl]
        if order != sorted(order):
            wrong.append(f"{name} 编号不是升序")
    if wrong:
        return rollback("搬完位置不对", wrong)

    print("─" * 78)
    print(f"✔ 已搬 {len(p2g)+len(g2p)} 条 · 条目正文逐字节未变 · 状态字段未变 · check 无新增")
    print(f"  全档 {len(body_after)} 条 ＝ problems.md {len(pb2)} ＋ graduated.md {len(gb2)}"
          f"　（搬前 {len(pb)+len(got_p)} ＋ {len(gb)-len(got_p)+len(got_g)}）")
    for path, before, after in ((PROBLEMS, ptext, new_p), (GRADUATED, gtext, new_g)):
        b, a = before.split("\n"), after.split("\n")
        print(f"  {os.path.basename(path):<14} {len(b)} 行 → {len(a)} 行（{len(a)-len(b):+d}）")
    print("─" * 78)
    try:
        out = subprocess.run(["git", "diff", "--numstat", "--", PROBLEMS, GRADUATED],
                             cwd=ROOT, capture_output=True, text=True, timeout=30)
        print("git 侧核对（§11 收尾要贴的就是这个）：")
        for l in out.stdout.strip().splitlines():
            add, dele, f = (l.split("\t") + ["", "", ""])[:3]
            print(f"  {os.path.basename(f):<14} +{add} −{dele}")
    except Exception as ex:                                   # noqa: BLE001
        print(f"  （git diff 跑不了：{ex}）")
    print("─" * 78)
    print("下一步：① `lab.py check --all` ERROR 必须 0　② `lab.py stats` 抄新数")
    print("  ⛔ 搬完这一次不要用 `check --changed`：整体位移会让 git diff 把大批没动过的")
    print("    条目算成「改过」⇒ 存量行被按新文法查 ⇒ 全是假阳性")
    print(W)
    return 0

# ══════════════════════════════════════════════════════════════════════════
#  count —— 按【类型】数条目（SKILL §8）
#
#  ⛔ 禁用 grep 数条目：grep 数的是"字符串出现了几次"，本命令数的是"符合口径的
#     条目有几条"。两者天生不等 —— 同一条里写两遍、或那句话落在正文别处，grep 都会错。
#     实证 2026-09-04：§8 旧公式 `grep -c "^状态.*🎓"` ⇒ 291（真值 290，多数了一条墓碑）；
#     `grep -c "^### "` 减它 ⇒ 未毕业 29（真值 13，把 17 条墓碑/迁出当成了在池）。
#  ★ 每个类型都并排打【全档】与【未毕业】两个数 —— 报数必须说清是哪一个。
# ══════════════════════════════════════════════════════════════════════════
def _has_oldno(e):
    return any("旧号" in l for l in e.raw[:3])


TYPES = [
    # slug            中文名          口径 —— 脚本认的锚点                       predicate
    # ── 状态类（互斥；前两类相加 ＝ 全档总数，墓碑不占数）────────────────
    ("grad",      "🎓 已毕业",    "状态行有 `🎓 已毕业`（§3.3）",              lambda e: e.graduated),
    ("ungrad",    "未毕业",       "非墓碑 ＋ 状态行无 🎓",                     lambda e: not e.graduated),
    ("tomb",      "墓碑/迁出",    "标题是（已并入…）／⛔ 作废，或状态行写着已迁入/迁出"
                                  " —— ⛔ **不占全档数**",                     lambda e: e.tomb, True),
    # ── 出题口径类（决定这条会不会被 pick 抽到）──────────────────────
    ("drawable",  "可出题",       "未毕业 ＋ 非墓碑 ＋ 无「不召回／停出」标记",   lambda e: e.drawable),
    ("morph",     "形态类·不召回", f"状态行标记 `{M_MORPH}`（§3.4）",           lambda e: M_MORPH in e.marks),
    ("onlylog",   "只记录·不出题", f"状态行标记 `{M_ONLYLOG}`（§3.4④）",        lambda e: M_ONLYLOG in e.marks),
    ("spell",     "拼写类·不召回", f"状态行标记 `{M_SPELL}`（§2.1②）",          lambda e: M_SPELL in e.marks),
    ("noreview",  "复习组停出",    f"状态行标记 `{M_NOREVIEW}`（§6）",           lambda e: M_NOREVIEW in e.marks),
    ("multi",     "合并条·多句覆盖", f"状态行标记 `{M_MERGED}`（§3.2c）"
                                    " ⇒ 出题必须多句覆盖全部成员",              lambda e: M_MERGED in e.marks),
    ("stubborn",  "顽固",         f"状态行标记 `{M_STUBBORN}`",                lambda e: M_STUBBORN in e.marks),
    # ── 进度类（只对未毕业有意义）──────────────────────────────────
    ("streak0",   "未毕业·连对 0", "未毕业 ＋ 连对 0",                          lambda e: not e.graduated and e.ok == 0),
    ("streak1",   "未毕业·连对 1", "未毕业 ＋ 连对 1（差一次毕业）",             lambda e: not e.graduated and e.ok == 1),
    ("streak2+",  "未毕业·连对 ≥2", "未毕业 ＋ 连对 ≥2 ⚠️ 到线未毕业，⛔ 要修",  lambda e: not e.graduated and (e.ok or 0) >= 2),
    ("bad2+",     "连错 ≥2",      "连错 ≥2（§4① 必进池）",                     lambda e: (e.bad or 0) >= 2),
    ("everbad",   "犯过错的",      "历史里出现过 ❌ 或 📖",                      lambda e: e.ever_bad()),
    # ── 题面类 ───────────────────────────────────────────────────
    ("prompt-todo", "题面待补",   "元信息里没有「题面」字段或为空 ⇒ ⛔ 出不了题", lambda e: not e.prompt),
    # ── 来源类 ───────────────────────────────────────────────────
    ("migrated",  "旧 B 表迁移",  "元信息里有「旧号 B…」（2026-08-18 迁移）",     _has_oldno),
    ("never",     "从未被测",     "「上次」＝ —（一次都没被判定过）",            lambda e: not e.last_tested()),
    # ── 位置类 ───────────────────────────────────────────────────
    ("in-problems",  "住 problems.md",  "解析时的来源文件（＝ 未毕业／待搬的 🎓）", lambda e: e.src == "problems.md"),
    ("in-graduated", "住 graduated.md", "解析时的来源文件（＝ 已搬走的 🎓）",      lambda e: e.src == "graduated.md"),
]
TYPE_MAP = {t[0]: t for t in TYPES}


def _kind_slugs(ents):
    """类型（元信息第一格）动态成 slug：kind:搭配 / kind:语法 …"""
    return sorted({e.kind for e in ents if e.kind})


def cmd_count(args):
    ents = load_all()
    live = [e for e in ents if not e.tomb]          # 全档口径：墓碑不占数
    ungrad = [e for e in live if not e.graduated]
    W = "═" * 78

    def sel_of(slug):
        if slug.startswith("kind:"):
            k = slug[5:]
            return [e for e in live if e.kind == k], f"类型 {k}", f"元信息第一格 ＝ {k}"
        t = TYPE_MAP.get(slug)
        if not t:
            sys.exit(f"⛔ 不认识的类型「{slug}」—— 跑一次不带 --type 看全表，"
                     f"⛔ 不许临时发明类型名（SKILL §8）")
        pool = ents if len(t) > 4 and t[4] else live   # 墓碑类要在全集里数
        return [e for e in pool if t[3](e)], t[1], t[2]

    if not args.type:
        print(W)
        print("lab.py count · 按类型数条目（⛔ 禁用 grep 数条目，§8）")
        print(W)
        print(f"全档 {len(live)} 条（墓碑/迁出 {len(ents)-len(live)} 条不占数）"
              f" ｜ 其中未毕业 {len(ungrad)} 条")
        print(f"{'slug':<15}{'类型':<16}{'全档':>6}{'未毕业':>8}   口径")
        print("─" * 78)
        for t in TYPES:
            pool = ents if len(t) > 4 and t[4] else live
            n_all = sum(1 for e in pool if t[3](e))
            n_ug = sum(1 for e in ungrad if t[3](e))
            print(f"{t[0]:<15}{t[1]:<16}{n_all:>6}{n_ug:>8}   {t[2]}")
        print("─" * 78)
        for k in _kind_slugs(live):
            n_all = sum(1 for e in live if e.kind == k)
            n_ug = sum(1 for e in ungrad if e.kind == k)
            print(f"{'kind:'+k:<15}{'类型 '+k:<16}{n_all:>6}{n_ug:>8}   元信息第一格")
        print(W)
        print("★ 报数必须写清是【全档】还是【未毕业】口径 —— 两个数不一样（§8）")
        print("  逐条清单：`lab.py count --type <slug>`　逐条详情：再加 --detail")
        print(W)
        return 0

    sel, name, rule = sel_of(args.type)
    ug = [e for e in sel if not e.graduated and not e.tomb]
    print(W)
    print(f"lab.py count --type {args.type} · **全档 {len(sel)} 条**"
          f"（其中**未毕业 {len(ug)} 条**）/ 全档总数 {len(live)}")
    print(f"口径：{name} —— {rule}")
    print("★ 报这个数时必须写清是【全档】还是【未毕业】口径（§8）")
    print(W)
    if not args.detail:
        print(fmt_ids([e.num for e in sorted(sel, key=lambda x: x.num)]))
    else:
        for e in sorted(sel, key=lambda x: x.num):
            st = ("🎓" + (e.grad or "") if e.graduated else
                  f"连对{e.ok} 连错{e.bad}")
            mk = ("｜" + "／".join(sorted(e.marks))) if e.marks else ""
            print(f"  #{e.num:<5} {st:<18} 上次 {(e.last_tested() or '—'):<11}"
                  f" {e.kind or '—':<5} {e.title[:40]} {mk}")
    print(W)
    print(f"⇒ {len(sel)} 条。正文用 `lab.py show N`")
    return 0

# ══════════════════════════════════════════════════════════════════════════
#  pick / used —— 出题（SKILL §4① 学习日 · §5 付息日）
# ══════════════════════════════════════════════════════════════════════════
def must_pool(e):
    """§4① 必进池四类 → (是否进池, 理由)。都不沾 ⇒ 不进池。"""
    body = "\n".join(e.raw)
    if e.recount()[1] >= 2:
        return True, "连错≥2"
    if e.ever_bad():
        return True, "有过 ❌/📖"
    if e.recount()[0] == 1:
        return True, "连对1（差一次毕业）"
    if "回潮" in body:
        return True, "回潮过"
    last_judged = [h for h in e.history if h.symbol == "◎"]
    if last_judged and last_judged[-1].date == (e.last_tested() or ""):
        return True, "◎ 改过题面，欠一次重测"
    return False, "连对0 且零 ❌/📖 —— 学习日不出，付息日 a 段统一召回"


def order_key(e):
    """§6 组内排序：① 连错≥2 → ② 连对1 → ③ 距上次被测最久 → ④ 其余"""
    ok, bad = e.recount()
    tier = 0 if bad >= 2 else (1 if ok == 1 else 2)
    return (tier, e.last_tested() or "0000-00-00", e.num)


def partition(cand, size):
    """切成 ≤size 一组，并做 §6 组内防撞：相邻两题不测同一个词。"""
    buckets = [cand[i:i + size] for i in range(0, len(cand), size)]
    for b in buckets:
        for i in range(1, len(b)):
            if b[i].targets() & b[i - 1].targets():
                for j in range(i + 1, len(b)):
                    if not (b[j].targets() & b[i - 1].targets()):
                        b[i], b[j] = b[j], b[i]
                        break
    return buckets


def card(e, why, full=False):
    ok, bad = e.recount()
    mk = " ".join(sorted(e.marks)) if e.marks else ""
    out = [f"  #{e.num:<4d} [{e.kind or '—'}] {e.title[:60]}",
           f"        连对{ok} 连错{bad} ｜ 上次 {e.last_tested() or '—'} ｜ {why}"
           + (f" ｜ {mk}" if mk else ""),
           f"        题面 {(e.prompt or '⚠️ 待补 —— 抽到就当场补成完整中文句')[:70]}"]
    if M_MERGED in e.marks:
        out.append("        ⚠️ 合并条：本次出题**必须多句覆盖全部成员**（§3.2c②），只出一句 ＝ 违规")
    if full:
        for h in e.history[-4:]:
            out.append(f"        · {h.date} {h.symbol or '?'} {(h.occasion or '')[:52]}")
    return "\n".join(out)


def cmd_pick(args):
    today = args.date or date.today().isoformat()
    ents = [e for e in load_all() if e.active]
    used, done = read_drawn(today)
    print("═" * 74)
    print(f"lab.py pick · {args.type} · {today}"
          f"（同一天重跑这条命令，分组完全一样；已 `used` 过的自动不再出现）")
    print("═" * 74)

    if args.type == "learn":
        d1, d3 = back_days(today, 1), back_days(today, 3)
        print(f"D-1 ＝ {d1}　D-3 ＝ {d3}　（sessions/ 里按日期倒数第 1 / 第 3 个文件）")
        seen = [e for e in ents if (d1 and e.seen_on(d1)) or (d3 and e.seen_on(d3))]
        pool, dropped = [], []
        for e in seen:
            if not e.drawable:
                dropped.append((e, e.block_reason or ("🎓 已毕业" if e.graduated else "?")))
                continue
            if e.created_on() == today:
                dropped.append((e, "今天刚新建 —— 当天不测（§3.1）"))
                continue
            keep, why = must_pool(e)
            (pool if keep else dropped).append((e, why))
        pool = [e for e, _ in pool if e.num not in used]
        why = {e.num: w for e, w in
               [(x, must_pool(x)[1]) for x in ents]}
        print(f"D-1∪D-3 被测到 {len(seen)} 条 → 必进池 {len(pool)} 条"
              f"（已 used {len(used)} 条不再出）")
        print(f"⛔ 不进池 {len(dropped)} 条：")
        agg = defaultdict(list)
        for e, w in dropped:
            agg[w].append(e.num)
        for w, ns in sorted(agg.items(), key=lambda x: -len(x[1])):
            print(f"     {w:<34s} {len(ns):>3d} 条  {fmt_ids(ns, 18, '')}")
        segs = [("复习组", sorted(pool, key=order_key))]
    else:
        cs = cycle_start(today)
        print(f"本周期起点 ＝ {cs}（上一个 R 之后的第一天）")
        drawable = [e for e in ents if e.drawable and e.num not in used]
        a = [e for e in drawable if any(h.date >= cs for h in e.history)]
        b = [e for e in drawable if e not in a]
        a.sort(key=order_key)
        b.sort(key=lambda e: (e.last_tested() or "0000-00-00", e.num))
        stale = [e for e in b if len([d for d, t in day_types()
                                      if t == "R" and d > (e.last_tested() or "")]) >= 2]
        print(f"a 段（本周期全量）{len(a)} 条 ｜ b 段（向前抽样，最久没测优先）{len(b)} 条")
        if stale:
            print(f"⚠️ 兜底不变量：{len(stale)} 条已连续两个付息日没被测到 ⇒ **本场必须出**"
                  f"  {fmt_ids([e.num for e in stale], 18, '')}")
        segs = [("a 段 · 本周期全量", a), ("b 段 · 向前抽样", b)]

    gno = 0
    for name, lst in segs:
        if not lst:
            print(f"\n── {name} ── 空")
            continue
        for bk in partition(lst, args.size):
            gno += 1
            tag = f"第 {gno} 组"
            print(f"\n── {name} · {tag}（{len(bk)} 题）"
                  + ("　✅ 已 used" if tag in done else "") + " " + "─" * 24)
            for e in bk:
                w = must_pool(e)[1] if args.type == "learn" else \
                    f"连对{e.recount()[0]}"
                print(card(e, w, args.full))
            if not args.dry:
                append_drawn("\t".join([today, tag, "抽",
                                        ",".join(str(e.num) for e in bk)]))
    print("\n" + "─" * 74)
    print("⛔ 脚本做不到、必须教练手工的两件（§6）：① 题面逐字核对（grep 原行）"
          " ② 第二译法自查（逐题写有/无，有就点名）")
    print("每组定稿后跑：lab.py used --group N --used \"12,45\" [--dropped \"88=理由\"]")
    print("═" * 74)
    return 0


def cmd_used(args):
    today = args.date or date.today().isoformat()
    tag = f"第 {args.group} 组"
    append_drawn("\t".join([today, tag, "用", args.used.replace(" ", "")]))
    if args.dropped:
        append_drawn("\t".join([today, tag, "弃", args.dropped]))
    print(f"已记：{today} {tag} 用 [{args.used}]"
          + (f" 弃 [{args.dropped}]" if args.dropped else ""))
    return 0


# ══════════════════════════════════════════════════════════════════════════
#  append —— 把教练写好的判定行放进 problems.md 的正确位置（§7 落盘之后）
#
#  ⚠️ 全脚本唯一一处【写内容文件】的地方，边界写死：
#     · 脚本 ⛔ 不产生任何一个字的内容 —— 行文全部由教练在 rows 文件里写好
#     · 脚本只做两件机器活：① 插到哪一行  ② 连对／连错／上次 三个数重算
#     · ⛔ 不改 🎓、不改状态、不碰条目正文 —— 那些是判断，仍然手写
# ══════════════════════════════════════════════════════════════════════════
RE_ROWHEAD = re.compile(r"^#(\d+)[ 　]+(.*)$")
BAD_IN_BODY = ("状态 ", "### ")


def parse_rows_file(path):
    """rows 文件 → [dict]，格式见 SKILL §3.1 契约⑨。

        #156 ✅ 复习第1组 · `the difference is huge`——同根词位置对
          ⇒ 连对1 → 2，毕业
        #280 ❌ 复习第1组 · `make a big different`
          ——difference 是名词位，她给了形容词形
    · 块头顶格：`#N` ＋ 一个空格 ＋ 符号 ＋ 场合
    · 块体 = 直到下一个块头／EOF 的全部行（允许顶格 ``` 围栏，围栏内不认块头）
    · 块体可以为空（口语档案里 `- 2026-08-10 ✅` 这种裸行是合法的）
    """
    if not os.path.exists(path):
        sys.exit(f"⛔ rows 文件不存在：{path}")
    lines = open(path, encoding="utf-8").read().split("\n")
    blocks, cur, fence = [], None, False
    for i, raw in enumerate(lines):
        if raw.lstrip().startswith("```"):
            fence = not fence
        m = None if fence else RE_ROWHEAD.match(raw)
        if m:
            sym, occ, bold = parse_symbol(m.group(2))
            rest = m.group(2)
            raw_occ = rest[len(sym):] if sym and rest.startswith(sym) else ""
            cur = dict(num=int(m.group(1)), symbol=sym, occasion=occ, raw_occ=raw_occ,
                       bold=bold, body=[], lineno=i + 1, head=raw)
            blocks.append(cur)
            continue
        if cur is None:
            if raw.strip():
                sys.exit(f"⛔ rows L{i+1}：开头有不属于任何块的内容「{raw.strip()[:30]}」")
            continue
        cur["body"].append(raw)
    return blocks


def rewrite_status(line, ok, bad, last):
    out = re.sub(r"(连对[ 　]*)\d+", lambda m: m.group(1) + str(ok), line, count=1)
    out = re.sub(r"(连错[ 　]*)\d+", lambda m: m.group(1) + str(bad), out, count=1)
    out = re.sub(r"(上次[ 　]*)(20\d\d-\d\d-\d\d|—)",
                 lambda m: m.group(1) + last, out, count=1)
    return out


def cmd_append(args):
    today = args.date or date.today().isoformat()
    if not re.fullmatch(r"20\d\d-\d\d-\d\d", today):
        sys.exit(f"⛔ --date 要写成 YYYY-MM-DD，收到「{today}」")
    blocks = parse_rows_file(args.file)
    if not blocks:
        sys.exit("⛔ rows 文件里一个块都没有")

    ents = load_all()
    by_num = defaultdict(list)
    for e in ents:
        by_num[e.num].append(e)

    errs, warns, seen = [], [], {}
    for b in blocks:
        tag = f"rows L{b['lineno']} #{b['num']}"
        if b["num"] in seen:
            errs.append(f"{tag} 同一批里重复出现（上一次在 L{seen[b['num']]}）")
        seen[b["num"]] = b["lineno"]
        if b["symbol"] is None:
            errs.append(f"{tag} 切不出符号：「{b['head'][:40]}」—— §3.3 符号必须紧跟编号")
        elif b["symbol"] in LEGACY:
            errs.append(f"{tag} 📖 已于 2026-08-23 停用（§3.3「不会就错」⇒ 记 ❌）")
        if b["bold"]:
            errs.append(f"{tag} 符号加粗了 —— §3.3 符号紧跟日期、不加粗")
        for k, l in enumerate(b["body"]):
            for bad in BAD_IN_BODY:
                if l.startswith(bad):
                    errs.append(f"{tag} 块体第 {k+1} 行顶格写了「{bad.strip()}」—— "
                                f"⛔ 状态行/条目头不许写进历史行")
        first = next((l for l in b["body"] if l.strip()), None)
        if first is not None and first[:1] not in (" ", "\t", "　"):
            errs.append(f"{tag} 内容行没缩进：「{first[:30]}」")
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
            errs.append(f"{tag} 在 {e.src} 里 —— ⛔ 已归档的条目不许再 append，"
                        f"回潮的先搬回 problems.md")
        elif e.tomb:
            errs.append(f"{tag} 是墓碑/迁出条目 —— ⛔ 不再记判定")
        elif e.status_lineno is None:
            errs.append(f"{tag} 找不到状态行")
        else:
            b["pre_err"] = {m for lv, m in check_entry(e, set(), None) if lv == "ERROR"}
            if e.marks & {M_MORPH, M_ONLYLOG} and b["symbol"] in ("✅", "❌"):
                errs.append(f"{tag} 这是**形态类**条目 —— §3.4② 在哪儿掉都只记 ⚪，"
                            f"⛔ 不许记 {b['symbol']}")
            if e.graduated and b["symbol"] == "✅" and e.grad != "—" and today > e.grad:
                warns.append(f"{tag} 🎓（{e.grad} 毕业）记 ✅ ＝ 自发命中，只留证据；"
                             f"状态行按 §3.3 冻结在毕业日，数字不会变")
            same = [h for h in e.history if h.date == today]
            if same:
                warns.append(f"{tag} 该条今天已有 {len(same)} 行 —— §3.3「每一次各记一行、"
                             f"各算一次」，这一行会照常推进 streak")

    if errs:
        print("═" * 74)
        print(f"lab.py append · ⛔ 校验没过，{len(errs)} 处 —— 一个字都没写")
        print("═" * 74)
        for x in errs:
            print("ERROR  " + x)
        print("═" * 74)
        return 1

    src = open(PROBLEMS, encoding="utf-8").read()
    lines = src.split("\n")
    plan = []
    for b in blocks:
        e = b["entry"]
        lo, hi = e.start - 1, (e.end or len(lines))
        # 插入点 ＝【最后一条日期行的正文之后】，⛔ 不是条目末尾 ——
        # 口语档案的约定：判定行按日期挨在一起，尾部的 `- 备注 …` 块留在最后。
        # 正文的边界：空行/缩进行/围栏内的行都算正文，第一个顶格非围栏行（＝ 备注行）⇒ 停。
        prior = [h.lineno for h in e.history if h.date <= today]
        if prior:
            at = max(prior)
            j, fence = at, False
            while j < hi:
                l = lines[j]
                if l.lstrip().startswith("```"):
                    fence = not fence
                    at = j + 1
                elif fence or l[:1] in (" ", "\t", "　"):
                    at = j + 1
                elif not l.strip():
                    pass
                else:
                    break
                j += 1
        else:
            # 没有更早的历史行（含整条空的）⇒ 排在状态行之后、所有更晚的行之前
            at = e.status_lineno
            j, fence = at, False
            while j < hi:                    # 跳过状态行后面的 ★ 续行
                l = lines[j]
                if l.lstrip().startswith("```"):
                    fence = not fence
                    at = j + 1
                elif fence or l.startswith(("　", "\t")):
                    at = j + 1
                else:
                    break
                j += 1
        row = f"- {today} {b['symbol']}{b['raw_occ']}".rstrip()
        plan.append(dict(e=e, at=at, block=[row] + b["body"], b=b))

    for p in sorted(plan, key=lambda x: -x["at"]):
        body = list(p["block"])
        while body and not body[-1].strip():
            body.pop()
        lines[p["at"]:p["at"]] = body

    if args.dry_run:
        print("═" * 74)
        print(f"lab.py append --dry-run · {len(plan)} 条 · {today}（⛔ 没写盘）")
        print("═" * 74)
        for p in sorted(plan, key=lambda x: x["at"]):
            print(f"  #{p['e'].num}  插到 problems.md L{p['at']}（{len(p['block'])} 行）")
            print(f"      {p['block'][0][:88]}")
        for w in warns:
            print("WARN   " + w)
        print("═" * 74)
        return 0

    open(PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))

    idx = {e.num: e for e in parse_file(PROBLEMS, "problems.md")}
    lines = open(PROBLEMS, encoding="utf-8").read().split("\n")
    moved = []
    for b in blocks:
        e2 = idx[b["num"]]
        ok, bad = e2.recount()
        last = e2.last_tested() or "—"
        i = e2.status_lineno - 1
        lines[i] = rewrite_status(lines[i], ok, bad, last)
        moved.append((e2, ok, bad, last))
    open(PROBLEMS, "w", encoding="utf-8").write("\n".join(lines))

    ents3 = load_all()
    all_nums = {e.num for e in ents3}
    idx3 = {e.num: e for e in ents3 if e.src == "problems.md"}
    hard = {("problems.md", h.lineno) for b in blocks
            for h in idx3[b["num"]].history if h.date == today}
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
        print(f"lab.py append · ⛔ 写完自查不过，{len(bad_rows)} 处 —— 已整批回滚")
        print("═" * 74)
        for n, m in bad_rows:
            print(f"ERROR  #{n}  {m}")
        print("═" * 74)
        return 1

    print("═" * 74)
    print(f"lab.py append · {len(plan)} 条已写进 problems.md · {today} · 自查 ERROR 0")
    print("═" * 74)
    for e3, ok, bad, last in moved:
        flag = ""
        if not e3.graduated and ok >= 2:
            flag = "   ⇒ ★ 连对到 2，§3.3 要你原地标 🎓 已毕业（脚本⛔不代改）"
        elif e3.graduated and bad >= 1:
            flag = "   ⇒ ★ 🎓 条目吃到 ❌，§3.3 回潮：要你把状态行改回未毕业（脚本⛔不代改）"
        print(f"  #{e3.num}  {'🎓' if e3.graduated else '未毕业'}  "
              f"连对{ok} 连错{bad} ｜ 上次 {last}{flag}")
    for w in warns:
        print("WARN   " + w)
    print("─" * 74)
    print("下一步：`lab.py check --changed` 复核全部改动")
    print("═" * 74)
    return 0


# ══════════════════════════════════════════════════════════════════════════
def main():
    ap = argparse.ArgumentParser(description="口语 fluency-lab 线机械工具")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("pick", help="把当天全部候选一次抽出、切成 ≤10 一组")
    p.add_argument("--type", choices=["learn", "review"], required=True)
    p.add_argument("--size", type=int, default=10)
    p.add_argument("--full", action="store_true", help="卡片带历史留痕")
    p.add_argument("--date")
    p.add_argument("--dry", action="store_true", help="不写 drawn.log")
    p.set_defaults(func=cmd_pick)

    p = sub.add_parser("used", help="记录本组定稿用了哪几条、弃了哪几条")
    p.add_argument("--group", type=int, required=True)
    p.add_argument("--used", required=True)
    p.add_argument("--dropped")
    p.add_argument("--date")
    p.set_defaults(func=cmd_used)

    p = sub.add_parser("list", help="全量条目一览（非 detail），判重第 ① 步")
    p.add_argument("--state", choices=["未毕业", "🎓"])
    p.add_argument("--type")
    p.add_argument("--drawable", action="store_true", help="只列能进复习组的")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="打印指定条目的正文全文")
    p.add_argument("nums", nargs="+")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("dedup", help="按词查重（判重三步的第 ② 步，⛔ 判断仍须逐条读）")
    p.add_argument("terms", nargs="+")
    p.add_argument("--limit", type=int, default=12)
    p.add_argument("--no-history", action="store_true")
    p.set_defaults(func=cmd_dedup)

    p = sub.add_parser("append", help="把写好的判定行插进 problems.md 并重算三个数")
    p.add_argument("--file", required=True)
    p.add_argument("--date")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_append)

    p = sub.add_parser("deliver", help="交付物硬闸（§7/§9.1）：ERROR>0 ⇒ ⛔ 不许发")
    p.add_argument("--session", required=True, help="当日 session 文件（可只给文件名）")
    p.add_argument("--section", help="复习组／新题／重答／加练／回看；不给则扫全部")
    p.set_defaults(func=cmd_deliver)

    p = sub.add_parser("lookback", help="哪几篇自由产出还没被回看过（§4②，只读）")
    p.add_argument("--date", help="把哪一天当「今天」（默认今天）")
    p.set_defaults(func=cmd_lookback)

    p = sub.add_parser("prompts", help="题面逐字核对（§6）：打档案原文 ／ --verify 比发题稿")
    p.add_argument("nums", nargs="*", help="条目编号，空格或逗号分隔")
    p.add_argument("--verify", help="发题稿文件 —— 拿它与档案逐字比，不一致 ⇒ ⛔ 不许发")
    p.set_defaults(func=cmd_prompts)

    p = sub.add_parser("migrate", help="problems.md ⇄ graduated.md 双向搬迁（§3.3/§11）")
    p.add_argument("--dry-run", action="store_true", help="只打搬迁清单，⛔ 不写盘")
    p.set_defaults(func=cmd_migrate)

    p = sub.add_parser("count", help="按【类型】数条目：不带 --type 打全表，带了打清单")
    p.add_argument("--type", help="类型 slug（见不带参数时打印的那张表），或 kind:搭配")
    p.add_argument("--detail", action="store_true", help="逐条打 编号·状态·上次·类型·标题")
    p.set_defaults(func=cmd_count)

    p = sub.add_parser("stats", help="全档统计（每个数带编号清单）")
    p.add_argument("--brief", action="store_true")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("check", help="格式校验")
    p.add_argument("--changed", action="store_true")
    p.add_argument("--all", action="store_true")
    p.add_argument("--quiet", action="store_true")
    p.set_defaults(func=cmd_check)

    args = ap.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
