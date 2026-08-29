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
        print(f"   其中 {len(pending_move)} 条仍在 problems.md，**待她手动搬进 graduated.md**（§3.3）")
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
