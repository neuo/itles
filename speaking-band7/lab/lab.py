#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py —— 口语 fluency-lab 线的机械工具。

⛔ 本脚本【一个字的内容都不产生】。行文全部由教练手写，脚本只碰位置和算术：
     · 读  problems.md / graduated.md / methods.md / sessions/
           ../question_bank.md / ../coach/asked.log（只读，重答队列实时算用）
     · 写  drawn.log（append-only 出题流水）
     · 写  problems.md —— 仅 `append` 子命令，且仅两件机器活：
            ① 把教练写好的历史行插到正确位置  ② 连对／连错／上次 三个数重算
          ⛔ 不改 🎓／状态／条目正文 —— 那些是判断，仍然手写（SKILL §0.1.2）

子命令
  出题（SKILL §3.5 召回队列 · §4① · §5）—— 开场跑一次，当天全部候选一次分完组
    python3 speaking-band7/lab/lab.py pick --type learn|review [--size 10] [--full] [--date D]
    python3 speaking-band7/lab/lab.py used --group N --used "12,45" [--dropped "88=与第2题同词族"]
  建号查重（SKILL §3.1 判重三步 · §4⑤1b）
    python3 speaking-band7/lab/lab.py dedup "look for" "找" [--limit 12] [--no-history]
    python3 speaking-band7/lab/lab.py list [--state 未毕业] [--type 词组]
    python3 speaking-band7/lab/lab.py show 12 45
  记账（SKILL §7 顺序写死 —— 落盘之后）
    python3 speaking-band7/lab/lab.py append --file rows.md --date YYYY-MM-DD [--dry-run]
  统计与校验（SKILL §0.1 §8 §11）
    python3 speaking-band7/lab/lab.py redo            重答队列（§5d，实时算，最久没重答的在最上面）
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
QBANK = os.path.join(os.path.dirname(ROOT), "question_bank.md")
ASKED = os.path.join(os.path.dirname(ROOT), "coach", "asked.log")
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
    # ⚡ 她自评免测 ＝ **一次通过**：在池推进连对／毕业推进 rc，等待时钟照样清零（§4③）
    "⚡": "ok",       # 她自评通过（来源是自评不是测试 ⇒ 另记校准数，见 SELFPASS）
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
#   ⚡ 自评免测（她 2026-09-05 定）：复检组发题前先亮清单，她说「这条会了」⇒ 省下这一次。
#      ⛔ 无类型限制 —— 免哪条由她定，脚本只留痕 ＋ 报校准数（§4③），不设门槛。
#      不推进连对/连错（毕业条目状态本来就冻结在毕业日），只在**召回梯子上前进一格**。
# JUDGE 的子集：算通过，但来源是**自评**不是测试 ⇒ §4③ 的校准数从这里数
SELFPASS = {"⚡"}
ALL_SYMBOLS = sorted(list(JUDGE) + list(NEUTRAL) + list(LEGACY) + list(TRACE),
                     key=len, reverse=True)

# ── 状态行上的标记（出题时据此剔除／限流）─────────────────────────────────
M_MORPH = "形态类·不召回"          # §3.4  永不出题
M_ONLYLOG = "只记录·不出题"        # §3.4④ 同上，08-27 起的新写法
M_SPELL = "拼写类·不召回"          # §2.1② 永不出题
M_MERGED = "合并条·出题多句覆盖"    # §3.2c 出题必须多句覆盖全部成员
M_STUBBORN = "顽固"

# ── 题型（SKILL §6.0，她 2026-09-11 定：比照写作线契约②第 7 格）──────────────
#   这条【怎么被行使】是**存在档案里的数据**，⛔ 不是每次出题当场重判一次。
#   状态行写 `｜ 题型 词组`；不写这一格 ＝ 整句（存量就是这么算的，不用回标）；
ASK_SENTENCE, ASK_PHRASE = "整句", "词组"
ASKS = (ASK_SENTENCE, ASK_PHRASE)
# 已取消的题型：产出验（连同旧标记「⛔ 复习组停出」）。那一类考点**只在自由产出里指出来**，
# ⛔ 不建号、⛔ 不占召回位；判据搬进 methods.md。
ASK_RETIRED = ("产出验",)
ASK_FROM = "2026-09-11"      # 这天**起**新建的条目，状态行必须自己写出题型；更早的缺格不报
RE_ASK = re.compile(r"｜\s*\**题型\s*([^\s｜*]+)")
# 词组题的提示里 ⛔ 不许出现的字眼 —— 它们把要她产出的形式从【块】改成了【句】（§6② 红线）
ASK_PHRASE_BAN = ("当主语", "说一句", "一句话", "整句", "完整句", "说完")
SENT_END = ("。", "！", "？", "!", "?")

# ── 条目正文四节（§3.1 契约⑪–⑭，她 2026-09-12 定：比照写作线契约④）────────────
#   条目 ＝ 头 → 元信息 → 状态行 → **问题是什么／怎么发现的／我错在哪／题面**（合并条再挂
#   **成员出题账**）→ 历史行 → 备注块。题面从元信息行里拆出来做独立节。
#   BODY_FROM 起新建的条目缺节 ⇒ ERROR；更早的一行式存量列「存量提示」，由 c 段／子代理
#   逐条手写升级（`count --type body-legacy` 列清单）。⛔ 严格匹配：节标题顶格、逐字、加粗。
BODY_FROM = "2026-09-12"
SECTIONS = ["问题是什么", "怎么发现的", "我错在哪", "题面"]
SECTION_HEADS = {f"**{s}**": s for s in SECTIONS}
MEMBERS_HEAD = "**成员出题账**"
MEMBERS_KEY = "成员出题账"
_SEC_NAMES = SECTIONS + [MEMBERS_KEY]
RE_SEC_STRIP = re.compile(r"[\s\*📒：:]+")     # 用来识别「写歪的节标题」：去掉装饰后正好等于节名
# 不带日期的尾块行（旧账／⚠️／★／⇒／（／检查触发）：出现在四节之后 ⇒ 正文到此为止（§3.1 契约⑫）
#   ⛔ 只用于结束正文，不并进 RE_NOTE —— RE_NOTE 还兼着「日期行不许写在备注之后」那条闸
RE_TAIL = re.compile(r"^-\s*(旧账|⚠️|★|⇒|（|\*\*检查触发)")

# ══════════════════════════════════════════════════════════════════════════
#  召回梯子（SKILL §3.5，她 2026-09-05 定）—— 一条梯子，毕业线只是中间一格
#
#  格上的数字 ＝ 应等几个【练习日】（⛔ 不是自然日：休息日不存在）。
#  数字的来历见 SKILL §3.5。★ 在池条目掉过 ❌ ⇒ 降一格；复检队列（🎓）不降格。
# ══════════════════════════════════════════════════════════════════════════
RUNGS = [
    ("首测未做·连错≥2", 1),
    ("连错1",           1),
    ("连对1",           2),
    ("🎓 rc0",          3),
    ("🎓 rc1",          7),
    ("🎓 rc2",         16),
    ("🎓 rc3",         32),
    ("🎓 rc≥4",        60),
]
GRAD_RUNG0 = 3              # 毕业线在梯子上的位置（RUNGS 的下标）
# 配额（她 2026-09-05 定）：日型 → (在池组数上限, 复检组数)
#   ★ 在池是**上限**，排不满就是没有；空出来的组数**下溢给复检队列**（⛔ 反向不成立）
QUOTA = {"learn": (3, 1), "review": (5, 3)}
GROUP_SIZE = 10             # 一组 ＝ 10 **题**（⛔ 不是 10 条：打包题一题装多条）
BUNDLE_KINDS = {"词组", "词汇", "搭配"}   # 复检队列可打包成中译英词组串
BUNDLE_MAX = 6              # 一道打包题最多装几条
BUNDLE_REACH = 24           # 打包时最多往后够多远（⛔ 防止把队尾的条目拽到队首来）

RE_ENTRY = re.compile(r"^### (\d+)\s*·\s*(.*)$")
RE_STATUS = re.compile(r"^状态\s+(.*)$")
RE_META = re.compile(r"^类型\s+(\S+)")
RE_HIST = re.compile(r"^-\s*(20\d\d-\d\d-\d\d)\s+(.*)$")
RE_NOTE = re.compile(r"^-\s*(备注|判重结论)")
# ★ 合并条的题面自成一段：顶格 `题面（N 句…` ＋ 若干缩进续行（§3.2c）。
RE_PROMPT_HEAD = re.compile(r"^题面(?:[（(]|\s|$)")
# 段内的**编号句**才是题面本体（① ② … ⑳）；★ 开头的是判据/沿革，不进比对
RE_ITEM = re.compile(r"^[①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳]")
RE_DAYTYPE = re.compile(r"^#\s*(20\d\d-\d\d-\d\d)\s*·\s*\**\s*(L[123]|R)\b")
# 反向通道的固定写法（闭集，⛔ 不认第二种）：`- YYYY-MM-DD 📝 她自评没底 · 优先召回`
RE_PULLBACK = re.compile(r"^她自评没底")
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
        self.created = None           # 元信息「新建 YYYY-MM-DD」（旧 B 表迁移的没有）
        self.ask = None               # 状态行「题型」格原文；None ＝ 没写这一格（§6.0）
        self.prompt = None            # 题面（v3 ＝ 题面节；存量 ＝ 元信息行里的题面字段）
        self.prompt_lines = []        # ★ 题面整块：v3 ＝ 题面节的非空行；存量合并条 ＝ 自成一段的题面
        self.prompt_inline = None     # 元信息行里的题面字段原文（v3 条目不该再有，check 报错）
        # ── 正文四节（§3.1 契约⑪）──────────────────────────────────────
        self.sections = {}            # 节名 → [行]（含空行与围栏行，逐字）
        self.section_order = []       # 节名按出现顺序（含「成员出题账」）
        self.section_dups = []        # 同一节出现两次：[(lineno, 节名)]
        self.section_head_bad = []    # 写歪的节标题：[(lineno, 原文)]
        self.dash_in_body = []        # 正文四节里顶格 `- ` 的行：[(lineno, 原文)]
        self.members = None           # 成员出题账 [行]；None ＝ 没挂
        self.body_end = None          # 正文最后一个非空行的行号（append 没有历史行时插在它后面）
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
    def body_v3(self):
        """正文已升级成四节（§3.1 契约⑪）。⛔ 只要出现过一个合法节标题就按 v3 查，缺的节报 ERROR。"""
        return bool(self.sections) or self.members is not None

    def section_text(self, name):
        return "\n".join(self.sections.get(name, []))

    @property
    def ask_kind(self):
        """题型（§6.0）。状态行没写这一格 ⇒ 整句。"""
        return self.ask or ASK_SENTENCE

    @property
    def no_ask_any(self):
        """**不出中译英题**的全部口径 —— 题面节写说明即可，⛔ 不要求引号句：
        `形态类·不召回` ／ `⚪ 只记录·不出题` ／ `拼写类·不召回`。
        ⛔ 别拿题型格当这个判据：形态类靠标记挡，题型格是默认档也照样不出题。"""
        return bool(self.marks & {M_MORPH, M_ONLYLOG, M_SPELL})

    @property
    def active(self):
        """会参与出题/统计的（排除墓碑）"""
        return not self.tomb

    @property
    def drawable(self):
        """能进复习组的：未毕业 · 非墓碑 · 无「不召回」标记"""
        if self.tomb or self.graduated:
            return False
        return not self.no_ask_any

    @property
    def block_reason(self):
        for m in (M_MORPH, M_ONLYLOG, M_SPELL):
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
        """历史上有过 ❌ 或 📖（全部历史）。"""
        return any(h.symbol in ("❌", "📖") for h in self.history)

    # ── 召回梯子（§3.5，她 2026-09-05 定）────────────────────────────────
    def eff_last(self):
        """**有效上次** ＝ 最后一行 ✅／❌（📖 按 ❌ 读）。
        ★ ⚡ **算** —— 她说"这条会了"就是对它做过一次处置，等待时钟照样清零。
        ⛔ ◎ ⚪ 与留痕行不算 —— ◎ 的定义就是「这次没测成」，它不该把条目往后推
        （这一条顺手吃掉了旧「必进池④ 改过题面、欠一次重测」整类）。
        ⚠️ 与状态行的「上次」**不是一个口径**：那个是「上次被出题」，含 ◎。"""
        ds = [h.date for h in self.history
              if h.symbol in JUDGE or h.symbol in LEGACY_JUDGE]
        return max(ds) if ds else None

    def rechecks(self):
        """复检次数 rc ＝ 毕业日**之后**的 ✅ 与 ⚡ 行数（＝ 在梯子上爬了几格）。
        ★ 全部导出，零新字段：回潮 ⇒ 状态行改回未毕业 ⇒ 重新毕业时 grad 更新
          ⇒ 这个数自动归零，不需要任何一条额外规则。"""
        g = self.freeze_at()
        if not g:
            return 0
        return len([h for h in self.history
                    if h.date > g and h.symbol in ("✅", "⚡")])

    def at_risk(self):
        """§3.5 降格口径：**未毕业 ＋ 历史里掉过 ❌／📖 ⇒ 降一格**。
        复检队列（🎓）不降格：复检只有对和不对，错了就回在池。"""
        return (not self.graduated) and self.ever_bad()

    def base_rung(self):
        """梯子上的**基准**格（不含风险修正）。"""
        if self.pulled_back():
            return 0                       # 她说没底 ⇒ 顶到队首（§4③ 反向通道）
        if self.graduated:
            return GRAD_RUNG0 + min(self.rechecks(), 4)
        ok, bad = self.recount()
        if bad >= 2 or self.eff_last() is None:
            return 0                       # 连错≥2 · 首测未做
        if bad == 1:
            return 1                       # 连错1
        if ok >= 1:
            # ★ ok≥2 也走这一格：那是「连对到 2、还没手标 🎓」的**工作流窗口**，
            #   不是"从没测过"。该标 🎓 由 check 的专门 ERROR 管，⛔ 梯子不兼职。
            return 2                       # 连对1
        return 0                           # 兜底：状态与日志对不上 ⇒ 往严的方向站

    def rung(self):
        """在池条目掉过 ❌ ⇒ 降一格（at_risk，§3.5）；复检队列不降格。"""
        return max(0, self.base_rung() - (1 if self.at_risk() else 0))

    def interval(self):
        """应等几个练习日。"""
        return RUNGS[self.rung()][1]

    def rung_name(self):
        """写成「基准格 ⇒ 落到第几格」—— ⛔ 不能只打落点的名字：
        一条 `连错1·险` 落在 rung0，而 rung0 的名字叫「首测未做·连错≥2」，
        只打落点会让卡片看起来在说「这条从没测过」。"""
        b, r = self.base_rung(), self.rung()
        return RUNGS[b][0] + ("·险" if self.at_risk() else "") + f" ⇒ rung{r}"

    def pulled_back(self):
        """★ 反向通道（§4③）：她说「这条我没底，拉回来」⇒ 记一行
             `- YYYY-MM-DD 📝 她自评没底 · 优先召回`
        然后**梯子钳到 rung0**（间隔 1 ⇒ 下一个练习日必出）。

        ⛔ 为什么不像原来那样"当场改状态行改回未毕业"：那会同时破两条不变量 ——
           写「连对清零」⇒ check 报「与历史重数不符」；写重放值 ⇒ check 报「连对已到 2 该标 🎓」。
           两条路都过不了闸，唯一能过的写法是把她的"没底"伪造成一次 ❌。
        ★ 自动失效：下次被判定后 eff_last 越过这一行，标记自然过期，⛔ 不需要谁去清。"""
        ds = [h.date for h in self.history
              if h.symbol == "📝" and RE_PULLBACK.match(h.occasion or "")]
        if not ds:
            return False
        el = self.eff_last()
        return (not el) or max(ds) > el

    def selfpassed(self):
        """⚡ 自评免测的行（§4③ 校准数就是从这里数的）"""
        return [h for h in self.history if h.symbol == "⚡"]

    @property
    def recallable(self):
        """会进召回队列的：非墓碑 ＋ 无「不召回／停出」标记。
        ⚠️ 与 drawable 的唯一差别 ＝ **毕业条目照样在队列里**
        （她 2026-09-05 定：毕业不是冻结，只是在梯子上往上一格）。"""
        if self.tomb or self.no_ask_any:
            return False
        return not (self.marks & {M_MORPH, M_ONLYLOG, M_SPELL})

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


def _prompt_from_sections(e):
    """v3 条目：题面 ＝ **题面** 节（§3.1 契约⑫）。
    · 非空行里 ★ 开头的是教练注释（判据/沿革/目标形式），⛔ 不算题面本体
    · 有编号句（① ② …）⇒ 只有编号句是题面本体（合并条，同存量口径）；没有 ⇒ 全部非注释行
    · prompt_lines ＝ 节里全部非空行（prompts 子命令整段打印，★ 行一起看）"""
    sec = e.sections.get("题面")
    if sec is None:
        return
    nonblank = [l for l in sec if l.strip()]
    # ★ 注释可以写成多行：★ 起头的那一行 ＋ 它后面的**缩进续行**都算注释（2026-09-12 实测：
    #   续行只看行首就会被当成题面本体，整句条目直接 ERROR、prompts --verify 还会要求续行里的引号）
    body, in_note = [], False
    for l in nonblank:
        s = l.strip()
        if s.startswith("★"):
            in_note = True
            continue
        # 编号句（合并条的 ①②… 本来就带全角缩进）与引号句永远是题面本体，⛔ 不算注释续行
        if in_note and l[:1] in (" ", "\t", "　") and not RE_ITEM.match(s) \
                and not s.startswith(('"', '“', '【')):
            continue
        in_note = False
        body.append(s)
    items = [l for l in body if RE_ITEM.match(l)]
    body = items if items else body
    e.prompt_lines = nonblank
    e.prompt = "　".join(body) if body else None


def _fill_prompt_block(e):
    """【存量】题面写成独立一段时（合并条），把整段收进来。⛔ 只在元信息行里没写题面时才找。"""
    if e.body_v3:
        return
    for i, l in enumerate(e.raw):
        if not RE_PROMPT_HEAD.match(l):
            continue
        blk = [l]
        for nxt in e.raw[i + 1:]:
            if nxt[:1] in (" ", "\t", "　"):
                blk.append(nxt)
            elif not nxt.strip():
                break
            else:
                break
        e.prompt_lines = blk
        if not e.prompt:
            # ★ 只有**编号句**（① ② ③ …）才是要她产出的题面；
            #   段首那行「题面（5 句，…）」和 ★ 开头的判据/沿革行是注释，
            #   ⛔ 不能进 --verify 的比对源（否则发题稿永远对不上）。
            items = [x.strip() for x in blk[1:]
                     if RE_ITEM.match(x.strip())]
            e.prompt = "　".join(items) if items else blk[0][2:].strip()
        return


def parse_file(path, src):
    if not os.path.exists(path):
        return []
    lines = open(path, encoding="utf-8").read().split("\n")
    entries, cur, fence = [], None, False
    sec = None            # 当前正文节（None ＝ 不在四节里）
    in_hist = False       # 已进入历史行/备注区 ⇒ 之后不再认节标题

    def close(idx):
        if cur is not None:
            cur.end = idx
            entries.append(cur)

    def body_line(raw, ln):
        """正文四节/成员出题账的内容行：逐字收进当前节，记 body_end。"""
        if sec == MEMBERS_KEY:
            cur.members.append(raw)
        else:
            cur.sections[sec].append(raw)
        if raw.strip():
            cur.body_end = ln

    for i, raw in enumerate(lines):
        ln = i + 1
        if raw.lstrip().startswith("```"):
            fence = not fence
            if cur is not None:
                cur.raw.append(raw)
                if sec is not None and not in_hist:
                    body_line(raw, ln)
            continue

        if not fence:
            m = RE_ENTRY.match(raw)
            if m:
                close(i)
                cur = Entry(int(m.group(1)), m.group(2).strip(), src, ln)
                cur.tomb = bool(RE_MERGED_TITLE.match(cur.title) or
                                RE_VOID_TITLE.match(cur.title))
                sec, in_hist = None, False
                continue

        if cur is None:
            continue
        cur.raw.append(raw)
        if fence:
            if sec is not None and not in_hist:
                body_line(raw, ln)
            continue

        m = RE_META.match(raw)
        if m and cur.kind is None:
            cur.kind = m.group(1)
            pm = re.search(r"题面\s*(.*?)(?:\s*｜|$)", raw)
            if pm:
                cur.prompt = pm.group(1).strip()
                cur.prompt_inline = cur.prompt
            cm = re.search(r"新建\s*(20\d\d-\d\d-\d\d)", raw)
            if cm:
                cur.created = cm.group(1)
            continue

        # ── 正文四节（§3.1 契约⑪）：状态行之后、第一条历史行/备注之前 ─────────
        if cur.status_raw is not None:
            is_head = raw in SECTION_HEADS or raw == MEMBERS_HEAD
            if in_hist:
                if is_head:               # 节标题跑到历史行后面 ⇒ 位置错，check 报
                    cur.section_head_bad.append((ln, raw.strip()[:40] + "（写在历史行之后）"))
            elif RE_HIST.match(raw) or RE_NOTE.match(raw) or RE_TAIL.match(raw):
                in_hist = True            # 正文到此为止，下面照常按历史行/尾块读
                sec = None
            elif is_head:
                name = SECTION_HEADS.get(raw, MEMBERS_KEY)
                if name == MEMBERS_KEY:
                    if cur.members is not None:
                        cur.section_dups.append((ln, name))
                    cur.members = cur.members or []
                else:
                    if name in cur.sections:
                        cur.section_dups.append((ln, name))
                    cur.sections.setdefault(name, [])
                cur.section_order.append(name)
                cur.body_end = ln
                sec = name
                continue
            else:
                if raw.strip() and RE_SEC_STRIP.sub("", raw) in _SEC_NAMES:
                    cur.section_head_bad.append((ln, raw.strip()[:40]))
                if sec is not None:
                    if raw.startswith("- "):
                        cur.dash_in_body.append((ln, raw.strip()[:40]))
                    body_line(raw, ln)
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
            for mk in (M_MORPH, M_ONLYLOG, M_SPELL, M_MERGED, M_STUBBORN):
                if mk in body:
                    cur.marks.add(mk)
            mo = RE_ASK.search(body)
            if mo:
                cur.ask = mo.group(1)
            continue

        m = RE_HIST.match(raw)
        if m:
            sym, occ, bold = parse_symbol(m.group(2))
            kind = ("selfpass" if sym in SELFPASS else     # ⛔ 必须排在 judge 之前
                    "judge" if sym in JUDGE else
                    "neutral" if sym in NEUTRAL else
                    "legacy" if sym in LEGACY else
                    "trace" if sym in TRACE else "unknown")
            cur.history.append(Hist(date=m.group(1), symbol=sym, occasion=occ,
                                    lineno=ln, kind=kind, bold=bold, raw=raw))
    close(len(lines))
    for e in entries:
        if e.body_v3:
            e.prompt, e.prompt_lines = None, []     # v3 只认题面节；元信息行里的题面留在 prompt_inline 给 check 报
            _prompt_from_sections(e)
        elif not e.prompt or not e.prompt_lines:
            _fill_prompt_block(e)
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
#  逾期分 —— 召回队列的唯一排序依据（SKILL §3.5）
#
#  逾期分 ＝ 距【有效上次】的练习日数 ÷ 应等间隔      （≥1 ＝ 到期）
#  ⇒ 它自己就是兜底不变量：等得越冤排得越前，
#    所以 ⛔ 不再需要「顺延队列」「不许连续两个付息日没被测到」这两套账
#    （她 2026-09-05 裁定删除 —— 没出完的条目第二天逾期分自动更高、自动排更前）。
# ══════════════════════════════════════════════════════════════════════════
_PDAYS = None


def practice_days():
    """练习日 ＝ sessions/ 里有文件的日期，升序。⛔ 不是自然日。"""
    global _PDAYS
    if _PDAYS is None:
        _PDAYS = [d for d, _ in day_types()]
    return _PDAYS


def waited_days(e, today, days=None):
    """距【有效上次】过了几个练习日。**今天算一个**（正在练）。
    从没被有效判定过 ⇒ 从建号日算起；建号日也没有 ⇒ 从最早的练习日算。"""
    days = practice_days() if days is None else days
    seq = sorted(set(days) | {today})
    base = e.eff_last() or e.created_on() or (seq[0] if seq else today)
    return len([d for d in seq if base < d <= today])


def overdue(e, today, days=None):
    """逾期分。≥1 ＝ 今天到期。"""
    return waited_days(e, today, days) / float(e.interval())


def queue_key(e, today, days=None):
    """§3.5 排序，两条队列各一套（确定性，可复算）：
      在池 ＝ 逾期分降序 → 掉过的优先 → 编号升序
      复检 ＝ 复检次数少的优先 → 已等练习日多的优先 → 编号升序（她说「没底·拉回来」的顶到队首）"""
    if e.graduated:
        first = -1 if e.pulled_back() else e.rechecks()
        return (first, -waited_days(e, today, days), e.num)
    return (-overdue(e, today, days), 0 if e.at_risk() else 1, e.num)


# ══════════════════════════════════════════════════════════════════════════
#  出题流水（append-only）
# ══════════════════════════════════════════════════════════════════════════
# 「弃」字段的写法：`<编号>=<理由>`（多条用逗号/分号隔开）。理由里可能出现 `#NNN`
# ⇒ ⛔ 只认**紧跟 `=` 的那个号**，绝不从理由文本里捡号 —— 捡错一个 ＝ 白白放宽对账闸。
RE_DROPPED = re.compile(r"(?:^|[,;；、\s])\s*#?(\d+)\s*=")


def drawn_rows(day):
    """→ {"抽": set, "用": set, "免": set, "弃": set}　某一天的出题流水，按动作分开。

    ★★ 口径（2026-09-05 定，⛔ 所有读 drawn.log 的地方必须一模一样）：
      · 「用」＝ 同一（日期,组）**以最后一行为准**，⛔ 不取并集 ——
        重跑 `used`（组内改判、当场作废）是正常操作，后写的覆盖先写的。
        取并集的话被撤下来的编号会自己爬回来（2026-09-05 实测：#136 撤两次都撤不掉）。
      · 「抽/免/弃」＝ 并集 —— 它们是**追加事实**（抽过了／她免了／这条作废了），
        不是"这一组最终出了哪些"的快照，⛔ 不适用后写覆盖。
    ⚠️ read_drawn 把三者并成一个集合（它只关心"别再抽第二次"），对账要的是分开的四份。"""
    out = {k: set() for k in ("抽", "用", "免", "弃")}
    last_used = {}                      # 组名 → 该组**最后一行**「用」的编号集合
    if not os.path.exists(DRAWN):
        return out
    for line in open(DRAWN, encoding="utf-8"):
        # ★ 只剥换行、⛔ 不 strip 整行：`used --used ""`（＝ 把这一组整组撤下来／整组免测）
        #   写出来的最后一个字段是空的，line.strip() 会连那个制表符一起吃掉 ⇒ 只剩 3 段 ⇒
        #   这一行被当成畸形行跳过 ⇒「后写覆盖先写」永远覆盖不掉（2026-09-09 实测：
        #   第 1 组整组 ⚡ 免测，deliver 仍拿着上一行的 10 条去要三件套块）。
        p = line.rstrip("\n").rstrip("\r").split("\t")
        if len(p) < 4 or p[0] != day or p[2] not in out:
            continue
        if p[2] == "弃":
            got = {int(m.group(1)) for m in RE_DROPPED.finditer(p[3])}
        else:
            got = set()
            for x in re.split(r"[,\s]+", p[3]):
                x = x.split("=")[0].strip().lstrip("#")
                if x.isdigit():
                    got.add(int(x))
        if p[2] == "用":
            last_used[p[1]] = got       # ★ 后写覆盖先写（⛔ 不是 |=）
        else:
            out[p[2]] |= got
    for g in last_used.values():
        out["用"] |= g
    return out


def read_drawn(today):
    """→ (used, groups)　used ＝ 今天**不该再抽第二次**的编号；groups ＝ 今天出现过的组名。

    ⛔ 与 drawn_rows 同一个口径（「用」以最后一行为准）—— 两边算得不一样，
       就会出现"对账那边减掉了、抽题这边还算着"。
    ★ 「弃」也算进 used：◎ 的条目当天⛔不再出（§3.3 当天改题面、次日再测）。"""
    groups = set()
    if not os.path.exists(DRAWN):
        return set(), groups
    for line in open(DRAWN, encoding="utf-8"):
        parts = line.strip().split("\t")
        if len(parts) < 4 or parts[0] != today:
            continue
        groups.add(parts[1])
    dr = drawn_rows(today)
    # 「用」＝ 定稿出过　「免」＝ 她 ⚡ 免测（§4③）　「弃」＝ 题面搞坏了作废（◎）
    #  —— 三者都不该在同一天再被抽第二次
    return dr["用"] | dr["免"] | dr["弃"], groups


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
        P.append(("ERROR",
                  "墓碑条目已废除（2026-09-05）—— 合并时**直接删掉被并的条目**，"
                  "记录写进目标条目的备注 ＋ cycles.md；编号自然作废、不复用"))
        return P
    hard_entry = (e.src, e.status_lineno) in touched_lines or \
                 any(h.date >= STRICT_FROM for h in e.history)

    # ── 契约⑤ 条目内顺序：头 → 元信息 → 状态行 →（正文四节）→ 历史行（日期升序）→ 备注块 ──
    idx = {}
    note_at = None
    hist_after_note = []
    fence = False
    for i, l in enumerate(e.raw):
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if RE_META.match(l):
            idx.setdefault("meta", i)
        elif RE_STATUS.match(l):
            idx.setdefault("stat", i)
        elif l in SECTION_HEADS or l == MEMBERS_HEAD:
            idx.setdefault("body", i)
        elif RE_HIST.match(l):
            idx.setdefault("hist", i)
            if note_at is not None:
                hist_after_note.append(l.strip()[:28])
        elif RE_NOTE.match(l) and note_at is None:
            note_at = i
    order = [(k, idx[k]) for k in ("meta", "stat", "body", "hist") if k in idx]
    if [v for _, v in order] != sorted(v for _, v in order):
        P.append(("ERROR",
                  "条目内顺序不对（§3.1 契约⑤ 写死：头 → 元信息 → 状态行 → 正文四节 → 历史行 → 备注块），"
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
        P.append(("WARN", "缺「类型」字段（元信息行 `类型 X ｜ 旧号 B…／新建 YYYY-MM-DD`）"))
    if not e.body_v3 and not e.graduated and not e.prompt and not e.no_ask_any:
        P.append(("WARN", "未毕业却没有题面字段 —— 抽到它就必须当场补成完整中文句"))
    if not e.history and not e.graduated:
        P.append(("ERROR", "一条历史行都没有"))
    P += check_body(e)
    P += check_ask(e)

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
        # ── ⚡ 自评免测（§4③）：⛔ 这里**故意不设任何限制** ──────────────
        #   免哪条由她定。⚡ 的约束只剩 §3.3 的通用符号规则（紧跟日期、不加粗）。

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
    if e.marks & {M_MORPH, M_ONLYLOG} and M_SPELL in e.marks:
        P.append(("WARN", "同时挂了两类「不召回」标记，口径重叠 —— 留一个就够"))
    return P


def check_body(e):
    """→ [(level, msg)]　正文四节（§3.1 契约⑪–⑭，她 2026-09-12 定，比照写作线契约④）。

    为什么是机器闸：口语线的条目九成是 08-18 从旧 B 表一行式迁进来的，正文从来没有规定节，
    判据靠可选的备注、题面塞在元信息行的括号里 ⇒ 建号时不被迫想清楚考点／邻居／找法，
    题面只能事后一个括号一个括号打补丁。写作线从建号那天就四节硬查，质量差在这里。
      · 出现过任一合法节标题 ⇒ 按 v3 查：四节齐 · 顺序死 · 题面只在节里 · 正文里不许顶格 `- `
      · 一个节标题都没有 ⇒ BODY_FROM 起新建的报 ERROR；更早的存量列「存量提示」（待升级）
      · 合并条（状态行 `合并条·出题多句覆盖`）必挂 **成员出题账**
      · v3 条目题型格必写（升级时一起回标）"""
    P = []
    if e.tomb:
        return P
    for ln, txt in e.section_head_bad:
        P.append(("ERROR", f"L{ln} 节标题写歪／放错位置：「{txt}」—— 必须顶格、逐字、加粗："
                           f"`**问题是什么**`／`**怎么发现的**`／`**我错在哪**`／`**题面**`／`**成员出题账**`，"
                           f"且全部在状态行之后、第一条历史行之前（§3.1 契约⑪）"))
    if not e.body_v3:
        if e.created and e.created >= BODY_FROM:
            P.append(("ERROR", f"正文缺四节 —— {BODY_FROM} 起新建的条目必须写 "
                               f"**问题是什么／怎么发现的／我错在哪／题面**（§3.1 契约⑪）"))
        else:
            P.append(("INFO", "正文还是一行式存量（无四节）—— 待升级（§3.1 契约⑭；清单 `count --type body-legacy`）"))
        return P
    missing = [s for s in SECTIONS if s not in e.sections]
    if missing:
        P.append(("ERROR", f"正文缺节：{'／'.join('**'+s+'**' for s in missing)}（§3.1 契约⑪ 一节都不许少）"))
    for ln, name in e.section_dups:
        P.append(("ERROR", f"L{ln} 「{name}」节出现了两次（§3.1 契约⑪）"))
    want = [s for s in _SEC_NAMES if s in e.sections or (s == MEMBERS_KEY and e.members is not None)]
    seen = [s for s in e.section_order if s in want]
    if seen != want and not e.section_dups:
        P.append(("ERROR", "正文四节顺序不对（§3.1 契约⑪ 写死：问题是什么 → 怎么发现的 → 我错在哪 → 题面 → 成员出题账），"
                           "实际是 " + " → ".join(e.section_order)))
    if e.prompt_inline:
        P.append(("ERROR", "题面写了两处（元信息行 ＋ 题面节）—— v3 只认 **题面** 节，把元信息行里的题面字段删掉（§3.1 契约⑫）"))
    for ln, txt in e.dash_in_body:
        P.append(("ERROR", f"L{ln} 正文四节里有顶格 `- ` 行：「{txt}」—— `- ` 只给历史行与备注块；正文列点用「·」或缩进（§3.1 契约⑪）"))
    for s in ("问题是什么", "怎么发现的", "我错在哪"):
        if s in e.sections and not e.section_text(s).strip():
            P.append(("ERROR", f"「{s}」节是空的（§3.1 契约⑪）"))
    if "题面" in e.sections and not e.no_ask_any:
        if not e.prompt:
            P.append(("ERROR", "「题面」节是空的 —— 整句/词组题出不了题（§3.1 契约⑫）"))
        elif not prompt_quotes(e):
            P.append(("ERROR", "「题面」节里没有引号句 —— 题面主体必须写在 \"…\" 里，提示写在（…）里（§3.1 契约⑫）"))
    if e.ask is None:
        P.append(("ERROR", "正文已是四节，状态行却没写题型格 —— 升级/建号必须一起写 `｜ 题型 整句／词组`（§3.1 契约⑫）"))
    if M_MERGED in e.marks and e.members is None:
        P.append(("ERROR", f"合并条缺 `{MEMBERS_HEAD}` —— 一个成员一行，出一次补一次（§3.2c④／§3.1 契约⑬）"))
    if e.members is not None:
        rows = [l for l in e.members if l.strip()]
        if not rows:
            P.append(("ERROR", "成员出题账是空的 —— 一个成员一行（§3.1 契约⑬）"))
        elif M_MERGED not in e.marks:
            P.append(("WARN", "挂了成员出题账，状态行却没标 `合并条·出题多句覆盖` —— 两边对齐"))
    wrong = e.section_text("我错在哪")
    if "我错在哪" in e.sections and wrong.strip() and "找法" not in wrong and "检查触发" not in wrong:
        P.append(("WARN", "「我错在哪」里没写找法（产出前问自己的那一句；形态类写「检查触发」）—— §3.1 字段规则"))
    return P


def _strip_parens(s):
    """去掉全部【括号提示】，只留题面**主体**。

    ⚠️ 2026-09-11 上线当天就踩到：提示里常常带引号（`（"比方说"用 Say 起头）`／
       `（别用"最重要的是…"起手）`），拿它们当题面本体去查"是不是完整句"⇒ 全是假阳性。
       §6② 说得清楚：括号里是**提示**，不是要她产出的东西 ⇒ 形式检查⛔不看括号。"""
    return re.sub(r"（[^（）]*）", " ", s or "")


def _uniq(xs):
    seen, out = set(), []
    for x in xs:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def prompt_quotes(e):
    """题面**主体**里的引号句（元信息行 ＋ 合并条自成一段的编号句），逐字，⛔ 不含括号提示里的。
    ★ 去重：合并条的 e.prompt 本身就是整段、prompt_lines 又逐行列一遍 ⇒ 不去重每句会报两次。"""
    qs = list(prompt_pieces(_strip_parens(e.prompt))[0])
    for l in e.prompt_lines:
        if RE_ITEM.match(l.strip()):
            qs += prompt_pieces(_strip_parens(l))[0]
    return _uniq(qs)


def prompt_parens(e):
    ps = list(prompt_pieces(e.prompt)[1])
    for l in e.prompt_lines:
        if RE_ITEM.match(l.strip()):
            ps += prompt_pieces(l)[1]
    return _uniq(ps)


def check_ask(e):
    """→ [(level, msg)]　题型格（§6.0）与题面形式的一致性 —— 2026-09-11 她点名补的闸。

    她的原话："词组只需要单次或者词组，整句（翻译）需要完全的句子"。
    当天两条题面各破一边、审核表第 6 项照样打了 ✅ ⇒ 只写在 skill 里的规则挡不住，
    这一条必须是机器闸：
      · 题型 词组 ⇒ 引号句⛔带句号；提示⛔含「当主语／说一句…」（提示不许改变产出形式，§6②）
      · 题型 整句 ⇒ 引号句必须以句末标点收尾（＝ 完整句的机器代理；有没有主语仍靠人）
      · 题型格缺 ⇒ ASK_FROM 起新建的报 ERROR；存量按整句读、不报（同写作线的口径）
    ⛔ 存量（没写题型格的）**不跑形式检查** —— 那是回标的活，不是报错的活。"""
    P = []
    if e.tomb:
        return P
    if e.ask in ASK_RETIRED:
        P.append(("ERROR", f"题型「{e.ask}」已取消 —— 那一类考点只在自由产出里指出来、⛔ 不建号，"
                           f"判据写进 methods.md；这条要么改成 整句／词组 出题，要么标"
                           f" `⚪ **只记录·不出题**`（§6.0）"))
        return P
    if e.ask is not None and e.ask not in ASKS:
        P.append(("ERROR", f"题型「{e.ask}」非法 —— 只许 {'／'.join(ASKS)}（§6.0）"))
        return P
    if e.ask is None and e.status_raw and "题型" in e.status_raw:
        # 写了「题型」二字却没被读出来 ＝ 写歪了（少了 ｜ 分隔、或值里带空格）⇒ 静默当成"没标"是最坏的结果
        P.append(("ERROR", "状态行里有「题型」二字，脚本却读不出这一格 —— 写法写死 `｜ 题型 整句／词组`"
                           "（前面要有 ｜，值不带空格）；写歪 ＝ 静默按整句读，正是 #26 那种漏"))
        return P
    if e.ask is None:
        if e.created and e.created >= ASK_FROM and not e.graduated:
            P.append(("ERROR", f"状态行缺「题型」格 —— {ASK_FROM} 起新建的条目必须自己写出"
                               f"`｜ 题型 整句／词组`（§6.0）"))
        return P
    qs, ps = prompt_quotes(e), prompt_parens(e)
    # 永不出题的（形态类／只记录／拼写类／停出／产出验）：题面节写的是说明，
    # 拿里面的引号去查「是不是完整句」「带不带句号」全是假阳性 ⇒ 这两支跳过。
    if e.ask == ASK_PHRASE and not e.no_ask_any:
        for q in qs:
            if any(ch in q for ch in SENT_END):
                P.append(("ERROR", f"题型是词组，题面引号句却带句号：「{q}」—— "
                                   f"词组题的题面是【块】不是句（§6.1）"))
        for p in ps:
            hit = [b for b in ASK_PHRASE_BAN if b in p]
            if hit:
                P.append(("ERROR", f"题型是词组，提示里却写着「{hit[0]}」：（{p}）—— "
                                   f"提示把要她产出的形式从块改成了句（§6② 红线：提示⛔不许改变产出形式）"))
    elif e.ask == ASK_SENTENCE and not e.no_ask_any:
        for q in qs:
            if not q.rstrip().endswith(SENT_END):
                P.append(("ERROR", f"题型是整句，题面引号句却不是完整句：「{q}」—— "
                                   f"整句题面必须有主语、能独立成句、句末标点收尾（§6.5⑥）"))
    return P


def fence_balance(path):
    """→ [(开始行, 说明)]  未闭合的代码围栏。
    ⚠️ 这是**文件级**检查，必须在条目检查之前跑 —— 围栏错位会让解析器把后面
    整片条目当成代码块吞掉。"""
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


def selfpass_audit():
    """→ [(level, 位置, 说明)]　drawn.log 的「免」 ⇄ 档案里的 ⚡ 行，逐日逐条对账。

    ⚠️ 这是 §11①b 唯一的闸：漏一行 ⚡ ＝ 这条没算通过 ＝ 下次又抽出来问一遍。"""
    P = []
    if not os.path.exists(DRAWN):
        return P
    days = sorted({l.split("\t")[0] for l in open(DRAWN, encoding="utf-8")
                   if l.count("\t") >= 3 and re.fullmatch(r"20\d\d-\d\d-\d\d", l.split("\t")[0])})
    ents = load_all()
    for day in days:
        if day < DELIVER_FROM:
            continue                       # 存量：那时还没有 ⚡ 这回事
        want = drawn_rows(day)["免"]
        if not want:
            continue
        got = {e.num for e in ents
               if any(h.symbol == "⚡" and h.date == day for h in e.history)}
        miss = sorted(want - got)
        if miss:
            P.append(("ERROR", f"drawn.log {day}",
                      f"记了 ⚡ 免测 {len(want)} 条，档案里少 {len(miss)} 行 ⚡："
                      f"{'／'.join('#'+str(x) for x in miss)} —— "
                      f"§11①b：漏一行 ＝ 这条没算通过 ＝ 下次又抽出来问一遍"))
        extra = sorted(got - want)
        if extra:
            P.append(("WARN", f"drawn.log {day}",
                      f"档案里有 {'／'.join('#'+str(x) for x in extra)} 的 ⚡ 行，"
                      f"drawn.log 没记 —— 免测也要走 `used --exempt`（§4③ 第 ⑤ 步）"))
    return P


def used_audit():
    """→ [(level, 位置, 说明)]　drawn.log 的「用」 ⇄ 档案里那一天的判定行，逐日逐条对账。

    ⚠️ 上线理由（2026-09-07 实测）：2026-09-05 的两个复检组（19 条 ＋ 15 条 ＝ 34 条）
       判定判了、写进了 session，却整整两组没交给 `append` ⇒ 档案里最后一行还停在 08-19
       ⇒ 梯子算出「已等 16 个练习日」⇒ 两天后又被整组抽出来重考一遍。
       当天 C0 check／C1 stats／C2 deliver **三条全绿**：
         check   只对账 ⚡（selfpass_audit），看不见判定行
         deliver 查的是 session 文件，而 session 里那 34 行写得好好的
       ⇒ 本函数 ＝ selfpass_audit 的另一半（§4⑤ 第 4 项「状态回写」的机器闸）。

    口径：
      · want ＝ 当天「用」－「免」－「弃」
        （§9.1④「弃」⛔ 不参与对账；「免」走 selfpass_audit 那条）
      · got  ＝ 当天有 ✅／❌／◎／📖 判定行的条目
      · ⛔ 只查单向（少）—— 反向多出来是**自由产出**（新题／重答）判的号，
        那些本来就不进 drawn.log，报出来全是噪音。"""
    P = []
    if not os.path.exists(DRAWN):
        return P
    days = sorted({l.split("\t")[0] for l in open(DRAWN, encoding="utf-8")
                   if l.count("\t") >= 3 and re.fullmatch(r"20\d\d-\d\d-\d\d", l.split("\t")[0])})
    ents = load_all()
    for day in days:
        if day < DELIVER_FROM:
            continue                       # 存量：这道闸上线之前的日子不回扫
        dr = drawn_rows(day)
        want = dr["用"] - dr["免"] - dr["弃"]
        if not want:
            continue
        got = {e.num for e in ents
               if any(h.date == day and h.symbol in ("✅", "❌", "◎", "📖")
                      for h in e.history)}
        miss = sorted(want - got)
        if miss:
            P.append(("ERROR", f"drawn.log {day}",
                      f"记了「用」{len(want)} 条，档案里少 {len(miss)} 行判定："
                      f"{'／'.join('#'+str(x) for x in miss)} —— "
                      f"§4⑤ 第 4 项：判定没落进档案 ＝ 梯子还停在上次 ＝ 过两天整组重考"))
    return P


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
    # ★ 两条文件级对账（与条目检查并列）：
    #   ⚡ 对账（§11①b）＝ drawn.log 的「免」⇄ 档案的 ⚡ 行
    #   用 对账（§4⑤ 第 4 项）＝ drawn.log 的「用」⇄ 档案那一天的判定行
    for lv, loc, msg in selfpass_audit() + used_audit():
        if lv == "ERROR":
            nerr += 1
        else:
            nwarn += 1
        print(f"{lv:<6} {loc}  {msg}")
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
#  stats —— 全档统计（SKILL §0.1.4：每个数带编号清单）
# ══════════════════════════════════════════════════════════════════════════
def fmt_ids(ids, per=16, indent="        "):
    ids = sorted(ids)
    if not ids:
        return ""
    out = []
    for i in range(0, len(ids), per):
        out.append(indent + " ".join("#%d" % n for n in ids[i:i + per]))
    return "\n".join(out)


# ── 重答队列（SKILL §5d）—— ⛔ 不存表，每次从 session 实时算 ──────────────────
#   R1–R36 是 session 文件出现之前（或 R 编号时期）就答过的题：它们的首答日、以及
#   session 标题上看不到的重答日，只在这里有记录 ⇒ 冻结成常量，⛔ 永不追加。
#   新题一律以 `bank:NNN` 进队列（session 标题 ／ coach/asked.log），不再发 R 号。
#   字段：(R 号, bank 行号, 类型, 首答日, 首答备注, session 标题外的重答日, 题目)
LEGACY_REDO = (
    ("R1", 1371, "P3", "2026-08-05", "08-05 前", (), "How can parents help children to be organized?"),
    ("R2", 1024, "P3", "2026-08-05", "", ("2026-08-17",), "Why do people prefer to watch movies in the cinema?"),
    ("R3", 1390, "P3", "2026-08-05", "", (), "What are good ways to manage traffic?"),
    ("R4", 220, "P3", "2026-08-05", "", (), "Do many people grow vegetables or flowers at home in your country?"),
    ("R5", 365, "P3", "2026-08-06", "", (), "What are the differences between everyday food and festival food?"),
    ("R6", 894, "P3", "2026-08-06", "", ("2026-08-17",), "Should parents limit their children's use of computer programs and computer games? Why and how?"),
    ("R7", 1086, "P3", "2026-08-06", "", (), "Do people buy things they don't need?"),
    ("R8", 254, "P3", "2026-08-07", "", (), "What do you think of communicating via social media?"),
    ("R9", 285, "P3", "2026-08-07", "", ("2026-08-10",), "Should governments provide financial support to start-ups?"),
    ("R10", 303, "P3", "2026-08-07", "", (), "How does technology help people make plans?"),
    ("R11", 367, "P3", "2026-08-08", "", (), "Do people today prefer eating at home or in a restaurant?"),
    ("R12", 892, "P3", "2026-08-08", "", (), "Why do some people not like using apps?"),
    ("R13", 879, "P3", "2026-08-08", "", (), "What are the differences between reading a book and visiting a museum?"),
    ("R14", 989, "P3", "2026-08-08", "", (), "Do you think there are too many subjects for students to learn?"),
    ("R15", 1186, "P3", "2026-08-09", "", (), "Why do old people prefer to live in quiet places?"),
    ("R16", 778, "P3", "2026-08-09", "", (), "What kind of job can be called a 'dream job'?"),
    ("R17", 911, "P3", "2026-08-09", "", (), "Is smiling important in your culture?"),
    ("R18", 1326, "P3", "2026-08-10", "", (), "What's the best way to learn a language?"),
    ("R19", 521, "P3", "2026-08-10", "", (), "Is it good for a person to be ambitious?"),
    ("R20", 364, "P3", "2026-08-11", "", (), "Why are there special foods on special occasions or events?"),
    ("R21", 450, "P2", "2026-08-11", "", (), "Describe a story/book with animals in it"),
    ("R22", 1011, "P2", "2026-08-11", "", (), "Describe a movie you watched and enjoyed recently"),
    ("R23", 834, "P2", "2026-08-12", "", (), "Describe a piece of technology (not a phone) that you would like to own"),
    ("R24", 991, "P3", "2026-08-12", "", (), "Do you think enterprises should provide training for their employees?"),
    ("R25", 308, "P2", "2026-08-12", "", (), "Describe a time when you worked in a group"),
    ("R26", 211, "P2", "2026-08-13", "", (), "Describe a person who loves to grow plants (e.g. vegetables, flowers) at home or in the garden"),
    ("R27", 349, "P3", "2026-08-13", "", (), "Where do people normally watch sports events?"),
    ("R28", 1286, "P2", "2026-08-15", "", (), "Describe a special cake you received from others"),
    ("R29", 478, "P2", "2026-08-15", "", (), "Describe a law on environmental protection"),
    ("R30", 340, "P2", "2026-08-16", "", (), "Describe a live sports event you watched and liked"),
    ("R31", 427, "P3", "2026-08-16", "", (), "What is the ideal length for a holiday?"),
    ("R32", 489, "P3", "2026-08-19", "", (), "How can parents and teachers help children understand and follow rules?"),
    ("R33", 187, "P3", "2026-08-20", "", (), "Why do most children think education is boring?"),
    ("R34", 927, "P3", "2026-08-20", "", (), "Do rewards help a child become better?"),
    ("R35", 434, "P2", "2026-08-21", "", (), "Describe a home that you like to visit but do not want to live in"),
    ("R36", 414, "P3", "2026-08-21", "", (), "Is advertising important for a company? Why?"),
)
RE_ASKED_BANK = re.compile(r"question_bank\.md:(\d+)$")


def redo_key(pid):
    """题号 → 队列键：有 bank 行号的 R 号与 `bank:NNN` 是同一道题 ⇒ 统一成 `bank:NNN`。"""
    m = re.fullmatch(r"R(\d+)", pid or "")
    if m:
        for rid, bank, *_ in LEGACY_REDO:
            if rid == pid and bank:
                return f"bank:{bank}"
    return pid


def redo_alias(key):
    """队列键 → 旧 R 号（没有 ⇒ ""）。"""
    for rid, bank, *_ in LEGACY_REDO:
        if key in (rid, f"bank:{bank}" if bank else None):
            return rid
    return ""


def _asked_rows():
    """coach/asked.log → [(bank 行号, 类型, 题目)]（按抽题顺序）。"""
    out = []
    if not os.path.exists(ASKED):
        return out
    for l in open(ASKED, encoding="utf-8"):
        f = l.rstrip("\n").split("\t")
        if len(f) < 4:
            continue
        m = RE_ASKED_BANK.search(f[1].strip())
        if m:
            out.append((int(m.group(1)), f[0].strip().upper(), f[3].strip()))
    return out


def _qbank_line(n):
    """question_bank.md 第 n 行 → (类型, 题目)；读不到 ⇒ ("?", "")。"""
    if not os.path.exists(QBANK):
        return "?", ""
    with open(QBANK, encoding="utf-8") as fh:
        for i, l in enumerate(fh, 1):
            if i == n:
                l = l.strip()
                if l.startswith("**Cue card**"):
                    return "P2", l.split(":", 1)[-1].strip()
                return "P3", l.lstrip("-").strip()
    return "?", ""


def _mention_date(bank):
    """asked.log 里有、session 标题里没有的题 ⇒ 到 session 正文里找它**最早**出现的日期。
    先认 `#` 标题行里的提及（回看标题不算），再认任意行。→ 日期 or None"""
    if not os.path.isdir(SESSIONS):
        return None
    rx = re.compile(r"(?:bank|question_bank\.md)\s*[:：]\s*%d(?!\d)" % bank)
    head = anyl = None
    for f in sorted(os.listdir(SESSIONS)):
        m = RE_SESS_NAME.match(f)
        if not m:
            continue
        for l in open(os.path.join(SESSIONS, f), encoding="utf-8"):
            if not rx.search(l):
                continue
            anyl = anyl or m.group(1)
            if l.startswith("#") and "回看" not in l:
                head = m.group(1)
                break
        if head:
            break
    return head or anyl


def redo_queue():
    """重答队列（§5d），**实时算** —— 最久没重答的在最前。
    题目集合 ＝ LEGACY_REDO ∪ session 里新题／加练／重答节标题上的题号 ∪ coach/asked.log。
    上次动它 ＝ max(首答日, 每一个引用它的新题／重答／加练节的日期)。
    排序 ＝ 上次动它（旧→新；日期不明的最前）→ 首答日 → 编号。
    → [dict(id, alias, type, first, first_note, redos, last, text, src)]"""
    items = {}

    def get(key):
        return items.setdefault(key, dict(id=key, alias=redo_alias(key), type="?", first=None,
                                          first_note="", redos=set(), touch=set(),
                                          text="", src=""))
    for rid, bank, typ, first, note, redos, text in LEGACY_REDO:
        it = get(f"bank:{bank}" if bank else rid)
        it.update(type=typ, first=first, first_note=note, text=text, src="legacy")
        it["redos"].update(redos)
    news, _ = scan_all_sessions()
    for x in news:
        if not x["id"]:
            continue
        it = get(redo_key(x["id"]))
        it["touch"].add(x["date"])
        if x["kind"] == "redo":
            it["redos"].add(x["date"])
        if not it["src"]:
            it["src"] = "session"
    for bank, typ, text in _asked_rows():
        it = get(f"bank:{bank}")
        if it["type"] == "?":
            it["type"] = typ
        if not it["text"]:
            it["text"] = text
        if not it["src"]:
            it["src"] = "asked.log"
    for key, it in items.items():
        if it["first"] is None:
            if it["touch"]:
                it["first"] = min(it["touch"])
            elif key.startswith("bank:"):
                it["first"] = _mention_date(int(key[5:]))
        # 首答当天之后的每一次再出现都算重答
        if it["first"]:
            it["redos"].update(d for d in it["touch"] if d > it["first"])
        if key.startswith("bank:") and (it["type"] == "?" or not it["text"]):
            t, q = _qbank_line(int(key[5:]))
            it["type"] = it["type"] if it["type"] != "?" else t
            it["text"] = it["text"] or q
        it["redos"] = sorted(it["redos"])
        it["last"] = max([it["first"] or ""] + it["redos"]) or None
        del it["touch"]

    def order(it):
        m = re.search(r"\d+", it["id"])
        return (it["last"] or "", it["first"] or "", 0 if it["alias"] else 1,
                int(it["alias"][1:]) if it["alias"] else int(m.group(0)) if m else 0)
    return sorted(items.values(), key=order)


def redo_totals(rq):
    never = [r for r in rq if not r["redos"]]
    return (f"重答队列   共 {len(rq)} 道 ／ 未重答过 {len(never)} 道"
            f"（§5d：⛔ 没有顺延这回事）")


def _redo_label(r):
    return r["id"] + (f"({r['alias']})" if r["alias"] and r["alias"] != r["id"] else "")


def cmd_redo(args):
    rq = redo_queue()
    W = "═" * 78
    print(W)
    print("lab.py redo · 重答队列（§5d）· 实时算：legacy R1–R36 ∪ session 新题／加练／重答 ∪ asked.log")
    print("  排序 ＝ 最久没重答的优先（上次动它 旧→新 → 首答日 → 编号）｜ 付息日 d 段从第 1 行往下取")
    print("  d 段节标题写 `## d 段 重答 · bank:NNN`（没有 bank 行号的旧题才写 RN）")
    print(W)
    for i, r in enumerate(rq, 1):
        first = r["first"] or "日期不明"
        if r["first_note"]:
            first += f"（{r['first_note']}）"
        last = r["redos"][-1] if r["redos"] else "从未"
        print(f"{i:>3}. {r['id']:<10} {r['alias']:<4} {r['type']:<3} 首答 {first:<12} "
              f"上次重答 {last:<10} {r['text']}")
    unk = [r for r in rq if not r["first"]]
    print("─" * 78)
    print(redo_totals(rq))
    if unk:
        print(f"⚠️ 首答日期不明 {len(unk)} 道（asked.log 里有、session 里找不到）：" +
              " ".join(r["id"] for r in unk))
    print(W)
    return 0


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
    for r in (M_MORPH, M_ONLYLOG, M_SPELL):
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
    print(redo_totals(rq))
    if rq and not args.brief:
        print("   最久没重答的 5 道：" +
              " · ".join(f"{_redo_label(r)}({r['redos'][-1] if r['redos'] else '从未'})"
                         for r in rq[:5]) + "　（全表：`lab.py redo`）")
    # ── 召回队列（§3.5 梯子，2026-09-05 上线）──────────────────────────
    today = date.today().isoformat()
    days = practice_days()
    rec = [e for e in act if e.recallable]
    due = [e for e in rec if overdue(e, today, days) >= 1]
    dpool = [e for e in due if not e.graduated]
    dgrad = [e for e in due if e.graduated]
    print("─" * 74)
    print(f"召回队列   进队列 {len(rec)} 条（⚠️ 🎓 也在里面）"
          f" ⇒ **今天到期 {len(due)} 条** ＝ 在池 {len(dpool)} ＋ 复检 {len(dgrad)}")
    print(f"           配额 学习日 在池{QUOTA['learn'][0]}组/复检{QUOTA['learn'][1]}组"
          f" ｜ 付息日 在池{QUOTA['review'][0]}组/复检{QUOTA['review'][1]}组"
          f"（在池是上限，空位下溢给复检）")
    # ⚠️ 按【基准格】分桶，⛔ 不按落点：落点 rung2 里既有"连对1零❌"也有"🎓rc0·险"，
    #    只打落点的名字会出现两个都叫「连对1」的桶。
    bars = []
    for i, (nm, iv) in enumerate(RUNGS):
        n = sum(1 for e in rec if e.base_rung() == i)
        if n:
            bars.append(f"{nm}={n}")
    print("           梯子分布（按基准格）" + " ｜ ".join(bars))
    print("           实际间隔（含在池掉过降一格）" + " ｜ ".join(
        f"{iv}d={sum(1 for e in rec if e.interval() == iv)}"
        for iv in sorted({r[1] for r in RUNGS})
        if sum(1 for e in rec if e.interval() == iv)))
    sp = [e for e in act if e.selfpassed()]
    if sp:
        fell = [e for e in sp if _selfpass_fell(e)]
        print(f"⚡ 自评免测 {len(sp)} 条，其中之后又掉过 {len(fell)} 条"
              f"（校准率 {len(fell)*100.0/len(sp):.0f}% —— §4③ 只报数、不设限）")
    v3 = [e for e in act if e.body_v3]
    legacy = [e for e in act if not e.body_v3]
    print(f"正文四节   已升级 {len(v3)} 条 ／ 待升级 {len(legacy)} 条"
          f"（§3.1 契约⑪–⑭ · 清单 `count --type body-legacy` · ⛔ 逐条手写，禁脚本）")
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


FIELD_W = {"标题": 3, "题面": 2, "正文": 2, "历史": 1}


def cmd_dedup(args):
    ents = [e for e in load_all() if e.active]
    terms = [t.strip() for t in args.terms if t.strip()]
    scored = []
    for e in ents:
        hits, sc = [], 0
        body = "\n".join(e.raw)
        fields = {"标题": e.title, "题面": e.prompt or "",
                  "正文": e.section_text("问题是什么") + "\n" + e.section_text("我错在哪")}
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
          f"（⛔ 这只是把候选捞出来给人看，判断必须逐条读完再下 —— §4⑤1b）")
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
# ★ 前缀一律用同一个口径：允许 ① ①b a a2 ⓪ ③b 这类编号（⛔ 不许各节各写各的）。
#   ⚠️ 各节口径不一致时，带前缀的节标题会被静默并进上一节、整节不查。
SEC_PFX = r"^\S{0,4}\s*"
# 「在池组」是 2026-09-05 §4①/§5a 的新名字，「复习组」是 09-05 之前全部 session 的旧名字
# ⇒ **两个都认**（存量 session 不改名），SKILL 侧统一写「在池组」。
RE_SEC_GROUP = re.compile(SEC_PFX + r"(?:在池组|复习组)\s*·\s*第\s*(\d+)\s*组")
# 复检组（§4①b，2026-09-05 上线）：`## ①b 复检组 · 第 N 组（M 题 / K 条）`
RE_SEC_RECHECK = re.compile(SEC_PFX + r"复检组\s*·\s*第\s*(\d+)\s*组")
RE_SEC_NEW = re.compile(SEC_PFX + r"新题\b")
RE_SEC_REDO = re.compile(r"^[dⓓ][\s·dD]*段|重答")
RE_SEC_EXTRA = re.compile(SEC_PFX + r"加练")
RE_SEC_LOOK = re.compile(SEC_PFX + r"回看\b")
RE_GROUP_N = re.compile(r"（\s*(\d+)\s*题\s*）")
# 复检组的标题必须**两个数都写**：`（N 题 / K 条）` —— 打包题一题装多条，
# 只报题数看不出覆盖了多少条（§8 两口径）。⛔ 不认只写题数的写法。
RE_RECHECK_N = re.compile(r"（\s*(\d+)\s*题\s*[/／]\s*(\d+)\s*条\s*）")
RE_BANK = re.compile(r"bank\s*[:：]\s*(\d+)")
RE_REDO_ID = re.compile(r"\bR(\d+)\b")
RE_QBLOCK = re.compile(r"^\[(\d+)\]\s*#(\d+)\s*·")
# 复检块头：`[3] #190 · 题面` 或 `[3] 打包 · #190 #232 #233 · 词组串`
RE_RBLOCK = re.compile(r"^\[(\d+)\]\s*(?:打包\s*·\s*)?((?:#\d+[\s·]*)+)")
RE_RJUDGE = re.compile(r"^判定\s*#(\d+)\s+(\S+)")
# 复检判定值的闭集：对 ✅ ／ 不对 ❌（§6.1③；题面出坏了记 ✅）
JUDGE_OK = ("✅", "❌")


def judge_val(raw):
    """把判定值归一化 → ✅ / ❌ / None（不认识）。
    ⚠️ 加粗写法要认出来**报错**，不是放过 —— 否则 `**❌**` 会被当成"不是 ❌"，
       三件套闸门整个绕过（加粗本身由调用处单独报，见 §3.3「符号紧跟、不加粗」）。"""
    v = (raw or "").strip().strip("*").strip()
    for k in JUDGE_OK:
        if v.startswith(k):
            return k
    return None
RE_NUMS = re.compile(r"#(\d+)")
RE_SBLOCK = re.compile(r"^\[S(\d+)\]")
RE_LOOK_NONE = re.compile(r"无(（|$|\s)")
# 回看节必须把原篇四件套逐字写进 session（§4② §5⓪ §9.1⑦）—— 这天起写的回看节硬查
LOOK_FROM = "2026-09-19"
# session 首行的日型标记：`# 2026-09-11 · **R**（付息日 …）`
RE_R_HEAD = re.compile(r"·\s*\*\*R\*\*")
# 四件套在原篇里的 `###` 小节：(显示名, 标题里认的关键词)。⛔ 五层诊断不在四件套里
QUAD_KEYS = [("题目原文", "题目"), ("她的原话", "原话"), ("① 最小修改版", "最小修改版"),
             ("② 更好版", "更好版"), ("③ 逐句 diff", "逐句")]
# 原篇缺了这几节 ⇒ 原篇本身写歪了，回看无从逐字取
QUAD_MUST = ("原话", "最小修改版", "更好版")
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
        #   先判 redo 会把回看节误判成重答节。
        kind = ("look" if RE_SEC_LOOK.match(title) else
                "recheck" if RE_SEC_RECHECK.match(title) else
                "group" if RE_SEC_GROUP.match(title) else
                "new" if RE_SEC_NEW.match(title) else
                "redo" if RE_SEC_REDO.search(title) else
                "extra" if RE_SEC_EXTRA.match(title) else "other")
        # ★ 节的作用域：一组的【出题】与【判定/三件套】常常写成两个 `##`
        #   （如 `## ① 在池组 · 第 1 组（3 题）` ＋ `## ① 第 1 组 · 判前自审`）。
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
# 省略记号：`…`(U+2026) ／ `...` ／ `. . .` —— diff 的两行完整句里出现即不合格（§7③：
# 看不到完整句就不算 diff）。⛔ 只查那两行，`· aaa → bbb` 的理由行照旧允许用省略号。
RE_ELLIPSIS = re.compile(r"…|\.\s*\.\s*\.")


ALL_LABELS = Q_LABELS + DIFF_LABELS


def _expand_compact(body):
    """§7 白纸黑字允许全对的题**压成一行**：
       `原句 … ｜判定 ✅ …｜最小改 ＝原句 ｜更好版 无更好版本 ｜diff-1 无 diff ｜diff-2 无 diff`
    ⇒ 一行里出现 ≥2 个已知标签才拆（⛔ 普通句子里的 ｜ 不受影响）。"""
    out = []
    for l in body:
        segs = [x.strip() for x in l.split("｜")]
        hit = sum(1 for x in segs if any(x.startswith(k) for k in ALL_LABELS))
        if len(segs) > 1 and hit >= 2:
            indent = l[:len(l) - len(l.lstrip())]
            out.extend(indent + x for x in segs if x)
        else:
            out.append(l)
    return out


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
    # ★ 围栏成对、却**跨过了节标题** ⇒ 那个 `##` 被当成代码吃掉，整节静默不查。
    #   未闭合检查抓不到它 —— 围栏是平衡的。
    for a, b in sc["fences"]:
        for i in range(a + 1, b):
            m = RE_H2.match(sc["lines"][i])
            if m:
                P.append(("ERROR", f"L{i+1}",
                          f"节标题「{m.group(1)[:32]}」落在 L{a+1}–L{b+1} 的 ``` 围栏**里面** ——"
                          f" 它会被当成代码吞掉，整节静默不查（围栏是成对的，未闭合检查抓不到）"))
    kinds = [s["kind"] for s in sc["sections"]]
    if not ({"group", "recheck", "new", "redo"} & set(kinds)):
        P.append((LV, "-", "整份 session 里认不出任何【复习组／复检组／新题／重答】节"
                           " —— §9.1 节标题写歪了"))

    # ── 与 drawn.log 对账（H2）：session 内部自洽 ≠ 没丢东西 ────────────
    #   `used --used "…"` 里有 ground truth：不拿它对，把一条从块头、判定行、
    #   标题条数里**一起**抹掉就查不出来。
    if not only and hard:
        dr = drawn_rows(sc["date"])
        # ★ 「弃」＝ 题面本身有毛病、本次作废（◎ §3.3）⇒ ⛔ 不进对账的期望集合：
        #   两边都要减（不要求它出现；出现了也不算「教练自己加题」——记 ◎ 是合法动作）。
        want = dr["用"] - dr["弃"]
        if dr["用"] or dr["免"]:
            insess = set()
            for sec in sc["sections"]:
                if sec["kind"] == "group":
                    for b in _blocks_in(sc, sec, RE_QBLOCK):
                        insess.add(int(b["m"].group(2)))
                elif sec["kind"] == "recheck":
                    for b in _blocks_in(sc, sec, RE_RBLOCK):
                        insess.update(int(x) for x in RE_NUMS.findall(b["m"].group(2)))
            miss = sorted(want - insess)
            extra = sorted(insess - want - dr["免"] - dr["弃"])
            if miss:
                P.append(("ERROR", "-",
                          f"drawn.log 记着今天定稿出了 {len(want)} 条，session 里找不到 "
                          f"{'／'.join('#'+str(x) for x in miss[:8])}"
                          f"{' 等' if len(miss) > 8 else ''} —— ⛔ 出了题就必须有记录"))
            if extra:
                P.append(("ERROR", "-",
                          f"session 里有 {'／'.join('#'+str(x) for x in extra[:8])}"
                          f"{' 等' if len(extra) > 8 else ''}，drawn.log 里没记 —— "
                          f"⛔ 教练自己加题（§4① 候选与分组由脚本定）"))
            if dr["免"] & insess:
                P.append(("ERROR", "-",
                          f"{'／'.join('#'+str(x) for x in sorted(dr['免'] & insess))} "
                          f"记了 ⚡ 免测，却又在 session 里出了题 —— 两者只能有一个"))
        elif dr["抽"]:
            P.append(("WARN", "-", "drawn.log 今天只有「抽」没有「用」—— "
                                   "每组定稿要跑 `lab.py used`（§4①），否则对不了账"))
        else:
            P.append(("WARN", "-", f"drawn.log 里 {sc['date']} 一条流水都没有 —— "
                                   f"这一场没跑过 `lab.py pick`？（§4① 候选由脚本定）"))
    # ── §5：付息日 ⛔ 不出新题 ────────────────────────────────────────
    first = sc["lines"][0] if sc["lines"] else ""
    dm = RE_DAYTYPE.match(first)
    if dm and dm.group(2) == "R":
        for sec in sc["sections"]:
            if sec["kind"] == "new":
                P.append((LV, f"L{sec['line']}",
                          f"付息日（首行写着 R）却有【新题】节 —— §5 ⛔ 付息日不出新题"))

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
            # ★ 例外 ＝ 标题**自己写着 0 题**：整组被她 ⚡ 免测掉（§4③，她说免就免，无类型/队列限制）
            #   ⇒ 一个块都没有是合法终局。⛔ 这不是放水：0 必须显式写进标题，
            #   而"出了题却没写块"仍由上面的数目对比 ＋ drawn.log 对账（用 ⇄ 块）各挡一道。
            if not blocks and (not m or int(m.group(1)) > 0):
                P.append((LV, loc, "复习组节里一个三件套块都没有（§7 每题都要给，含全对的）"))
            seen = set()
            for b in blocks:
                bl = f"L{b['line']}"
                idx, num = b["m"].group(1), b["m"].group(2)
                if num in seen:
                    P.append((LV, bl, f"#{num} 在同一节里出现两次"))
                seen.add(num)
                bodyN = _expand_compact(b["body"])
                headA = _head_area(bodyN)
                for lab_ in Q_LABELS:
                    v = _has_label(headA, lab_)
                    if v is None:
                        P.append((LV, bl, f"[{idx}] #{num} 缺「{lab_}」行（§7 六项一项不许省）"))
                    elif not v:
                        P.append((LV, bl, f"[{idx}] #{num} 的「{lab_}」是空的"))
                for f_ in _full_faults(sc, b, bodyN):
                    P.append((LV, bl, f"[{idx}] #{num} {f_}"))
                for lab_ in DIFF_LABELS:
                    v = _has_label(bodyN, lab_)
                    if v is None:
                        P.append((LV, bl, f"[{idx}] #{num} 缺「{lab_}」段（§7③ 两段必须分开）"))
                        continue
                    seg = _diff_seg(bodyN, lab_)
                    if not seg:
                        P.append((LV, bl, f"[{idx}] #{num} 的「{lab_}」段是空的"))
                    for f_ in _diff_faults(sc, b, seg, lab_):
                        P.append((LV, bl, f"[{idx}] #{num} {f_}"))
            h3 = [RE_H3.match(sc["lines"][i]).group(1)
                  for i in range(sec["start"], sec["end"])
                  if i not in sc["infence"] and RE_H3.match(sc["lines"][i])]
            if not any("新建条目" in x for x in h3):
                P.append((LV, loc, "缺【本组新建条目】块（§7「新建条目必须让她看见」，没有也要写「无」）"))

        elif sec["kind"] == "recheck":
            # ── 复检组（§4①b / §6.1）───────────────────────────────────
            #  目的是**定位**不是教 ⇒ 判两档：对 ✅ ／ 不对 ❌。
            #  ✅ 只要一行判定；❌ 才走三件套（它当场回潮，已经是在池条目了）。
            #  ★ 打包题最大的风险 ＝ **某个成员被悄悄漏判** ⇒ 这里逐条对账。
            m = RE_RECHECK_N.search(t)
            blocks = _blocks_in(sc, sec, RE_RBLOCK)
            if not m:
                P.append((LV, loc,
                          f"复检组节标题必须**两个数都写**「（N 题 / K 条）」，"
                          f"实际是 `{t[:44]}` —— 打包题一题装多条，"
                          f"只报题数看不出覆盖了多少条（§8 两口径）"))
            elif len(blocks) != int(m.group(1)):
                P.append((LV, loc,
                          f"标题写着 {m.group(1)} 题，节里只有 {len(blocks)} 个 `[n]` 块"))
            # ★ 同上：标题自己写着 0 题 ＝ 整组 ⚡ 免测掉了，合法终局（§4③）
            if not blocks and (not m or int(m.group(1)) > 0):
                P.append((LV, loc, "复检组节里一个 `[n] #NNN` 块都没有"))
            cover, seen = 0, set()
            for b in blocks:
                bl = f"L{b['line']}"
                idx = b["m"].group(1)
                nums = RE_NUMS.findall(b["m"].group(2))
                cover += len(nums)
                for n in nums:
                    if n in seen:
                        P.append((LV, bl, f"#{n} 在同一节里出现两次"))
                    seen.add(n)
                bodyN = _expand_compact(b["body"])
                judged = {j.group(1): j.group(2)
                          for j in (RE_RJUDGE.match(l.strip()) for l in bodyN) if j}
                miss = [n for n in nums if n not in judged]
                if miss:
                    P.append((LV, bl,
                              f"[{idx}] 块头列了 {len(nums)} 条，却缺 "
                              f"{'／'.join('#' + n for n in miss)} 的「判定 #NNN …」行"
                              f" —— 打包题**逐条对账**，⛔ 漏一条就是白测（§6.1）"))
                extra = [n for n in judged if n not in nums]
                if extra:
                    P.append((LV, bl,
                              f"[{idx}] 有 {'／'.join('#' + n for n in extra)} 的判定行，"
                              f"块头却没列它 —— 题头与判定必须一一对应"))
                # 加粗要**单独报**：认得出它是为了让闸报错，不是为了放过（同档案侧 §3.3）
                for n, v in judged.items():
                    if v.strip().startswith("**"):
                        P.append((LV, bl,
                                  f"[{idx}] #{n} 的判定符号加粗了（`{v[:8]}`）——"
                                  f" §3.3 符号紧跟、不加粗"))
                unknown = [(n, v) for n, v in judged.items() if judge_val(v) is None]
                for n, v in unknown:
                    P.append((LV, bl,
                              f"[{idx}] #{n} 的判定值「{v[:12]}」不在闭集 ✅／❌ 里 ——"
                              f" §6.1③ 复检只有对和不对（题面出坏了记 ✅）；"
                              f"⛔ 加粗写法（`**❌**`）也不认，符号必须裸写（§3.3）"))
                bad = [n for n, v in judged.items() if judge_val(v) == "❌"]
                if len(bad) > 1:
                    P.append((LV, bl,
                              f"[{idx}] 一个块里有 {len(bad)} 条 ❌ —— "
                              f"❌ 的条目当场回潮、各走各的三件套 ⇒ **拆成各自的块**（§6.1）"))
                if bad:
                    for lab_ in ("最小改", "更好版"):
                        if _has_label(_head_area(bodyN), lab_) is None:
                            P.append((LV, bl,
                                      f"[{idx}] #{bad[0]} 判了 ❌ 却缺「{lab_}」"
                                      f" —— 掉的题走全套三件套（§6.1）"))
                    for f_ in _full_faults(sc, b, bodyN):
                        P.append((LV, bl, f"[{idx}] #{bad[0]} {f_}"))
                    for lab_ in DIFF_LABELS:
                        if _has_label(bodyN, lab_) is None:
                            P.append((LV, bl, f"[{idx}] #{bad[0]} 判了 ❌ 却缺「{lab_}」段（§7③）"))
                            continue
                        seg = _diff_seg(bodyN, lab_)
                        for f_ in _diff_faults(sc, b, seg, lab_):
                            P.append((LV, bl, f"[{idx}] #{bad[0]} {f_}"))
            if m and cover != int(m.group(2)):
                P.append((LV, loc,
                          f"标题写着覆盖 {m.group(2)} 条，块头实际列了 {cover} 条"))
            h3 = [RE_H3.match(sc["lines"][i]).group(1)
                  for i in range(sec["start"], sec["end"])
                  if i not in sc["infence"] and RE_H3.match(sc["lines"][i])]
            if not any("免测" in x for x in h3):
                P.append((LV, loc,
                          "缺【本组 ⚡ 免测】块 —— 她免了哪几条是**校准数据**，"
                          "没有也要逐字写「无」（§4③）"))

        elif sec["kind"] in ("new", "redo", "extra"):
            if sec["kind"] == "new" and not RE_BANK.search(t):
                P.append((LV, loc, f"新题节标题没带题号：`{t[:40]}` —— §9.1 要求写 `bank:NNN`"))
            if sec["kind"] == "redo" and not (RE_BANK.search(t) or RE_REDO_ID.search(t)):
                P.append((LV, loc, f"重答节标题没带题号：`{t[:40]}` —— §9.1 要求写 `bank:NNN`"
                                   f"（没有 bank 行号的旧题写 `RN`）"))
            h3 = {RE_H3.match(sc["lines"][i]).group(1): i + 1
                  for i in range(sec["start"], sec["end"])
                  if i not in sc["infence"] and RE_H3.match(sc["lines"][i])}
            for want, key in FREE_H3:
                if not any(key in x for x in h3):
                    P.append((LV, loc, f"自由产出缺 `### {want}` 这一节（§7 四件套）"))
            for ln, which, s in _free_full_faults(sc, sec):
                P.append((LV, f"L{ln}",
                          f"`### {which}` 的正文用省略号截断了：`{s[:56]}`　"
                          f"§9.1③：**全文（一句都不省）**，⛔ 不许用 … 拼接"))
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
                    for f_ in _diff_faults(sc, b, seg, lab_):
                        P.append((LV, bl, f"[S{sid}] {f_}"))

        elif sec["kind"] == "look":
            rest = RE_SEC_LOOK.sub("", t).strip(" ·").strip()
            if not (RE_BANK.search(t) or RE_REDO_ID.search(t) or RE_LOOK_NONE.match(rest)):
                P.append((LV, loc,
                          f"回看节标题没写回看的是哪一篇：`{t[:44]}` —— "
                          f"§9.1 要求写 `## ② 回看 · bank:NNN`（没得回看写 `· 无（理由）`）"))
            elif sc["date"] >= LOOK_FROM and not RE_LOOK_NONE.match(rest):
                for f_ in _look_faults(sc, sec):
                    P.append(("ERROR", loc, f_))
    return P


def _look_faults(sc, sec):
    """回看节的四件套逐字闸（§9.1⑦）→ [说明]。
    标题里列了哪几篇，每一篇的原篇四件套（题目原文／原话／最小改／更好版／逐句 diff）
    **每一个内容行**都必须在本节里逐字出现（行首尾空白不计）。
    ⛔ 多写不管（旁注、更正行照样允许）；少一行就是压缩／截断／漏篇。"""
    out = []
    body = {sc["lines"][i].strip() for i in range(sec["start"], sec["end"])
            if sc["lines"][i].strip()}
    for pid in _ids_of(sec["title"]):
        src = find_free_source(pid, sc["date"])
        if not src:
            out.append(f"回看 {pid}：在 {sc['date']} 之前的 session 里找不到这篇自由产出的原篇"
                       f"（`## ③ 新题 …（bank:NNN）`／`## d 段 重答 · RN`）⇒ 标题写错了题号？")
            continue
        where = f"{src['file']}:L{src['line']}"
        lack = [n for n, k in QUAD_KEYS if k in QUAD_MUST and k not in src["parts"]]
        if lack:
            out.append(f"回看 {pid}：原篇 {where} 解析不出「{'／'.join(lack)}」节 "
                       f"⇒ 原篇写歪了（§9.1③），无从逐字转述")
            continue
        for name, key in QUAD_KEYS:
            need = _quad_need(src["parts"].get(key, []))
            miss = [x for x in need if x not in body]
            if miss:
                out.append(f"回看 {pid} 的「{name}」少了 {len(miss)}／{len(need)} 行"
                           f"（原篇 {where}）：`{miss[0][:48]}` —— "
                           f"跑 `lab.py lookback --print {pid}` 原样贴进本节（§4②：⛔ 不许压缩、不许省篇）")
    return out


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


def _locate(sc, blk, text):
    """把 diff 段里的一行映射回 session 原文的行号（1-based）；找不到 → None。
    ⛔ 不猜：_expand_compact 拆开过的行在原文里没有独立的一行 ⇒ 宁可不报行号。
    只在**这个块自己的行区间**里找（块体是块头之后的连续行）。
    ★ 起点句常常挂在标签行的尾巴上（`diff-1  原句   I need …`）⇒ 后缀也算命中。"""
    t = text.strip()
    a = blk["line"]                       # 块头 1-based ⇒ 块体第一行的 0-based 下标
    for i in range(a, min(a + len(blk["body"]), len(sc["lines"]))):
        s = sc["lines"][i].strip()
        if s == t or (s.endswith(t) and any(s.startswith(x) for x in DIFF_LABELS)):
            return i + 1
    return None


# §7 明写的两句固定写法 —— 它们不是句子，⛔ 不适用「完整」检查
FULL_EXEMPT = ("无更好版本", "＝原句", "=原句", EMPTY_DIFF)


def _truncated(text):
    """→ True ＝ 这一行用省略记号截断了（豁免上面那两句固定写法）。"""
    s = text.strip()
    if not s or any(x in s for x in FULL_EXEMPT):
        return False
    return bool(RE_ELLIPSIS.search(s))


def _full_faults(sc, blk, body):
    """三件套块里 `最小改` / `更好版` 两行的完整性（§7①②／§9.1③：全文，一句都不省）。
    ⛔ 只查这两行 —— 题面行 `[n] #NNN · …` 与 `原句` 行是**她的原话逐字**，
       她自己打的省略号不算违规。"""
    out, fname = [], os.path.basename(sc["path"])
    for l in _head_area(body):
        s = l.strip()
        for k in ("最小改", "更好版"):
            if not s.startswith(k) or not _truncated(s):
                continue
            ln = _locate(sc, blk, s)
            out.append(f"的「{k}」用省略号截断了 —— "
                       f"{fname} {('L%d' % ln) if ln else '（行号定位不到）'}："
                       f"`{s[:56]}`　§9.1③：最小改／更好版给**全文**，一句都不省")
    return out


def _free_full_faults(sc, sec):
    """自由产出的 `### ① 最小修改版` / `### ② 更好版` 正文段（§9.1③：全文，一句都不省）。
    → [(行号, 哪一节, 原文)]
    ★ 区段止于：下一个 `### `，或掉进逐句 diff（`[S1]` 块头／`diff-` 标签）——
      后者本身就是「缺 `### ③ 逐句 diff`」，另有一条闸报它，这里不重复叫。"""
    out, cur = [], None
    for i in range(sec["start"], sec["end"]):
        raw = sc["lines"][i]
        s = raw.strip()
        if i not in sc["infence"]:
            m = RE_H3.match(raw)
            if m:
                t = m.group(1)
                cur = ("最小修改版" if "最小修改版" in t else
                       "更好版" if "更好版" in t else None)
                continue
        if cur is None:
            continue
        if RE_SBLOCK.match(raw) or any(s.startswith(x) for x in DIFF_LABELS):
            cur = None
            continue
        if _truncated(raw):
            out.append((i + 1, cur, s))
    return out


def _diff_faults(sc, blk, seg, label):
    """一个 diff 段的硬格式检查（§7③）→ [说明]（空 list ＝ 合格）。
    ① 不是 `无 diff（＝上一版）` 的形态 ⇒ 必须摆两行完整句（⛔ 只写 xxx → yyy 不算）
    ② 那两行 ⛔ 不许带省略记号（… ／ ... ／ . . .）——
       句子被截断就看不出改的是哪里，跟没摆完整句是同一件事（§7③）。
    ⚠️ 这个闸只管**写进 session 文件**的 diff；聊天里发出去的内容它看不见（§9.1 已知缺口）。"""
    if not seg or EMPTY_DIFF in " ".join(seg):
        return []
    sents = _diff_sentences(seg)
    if len(sents) < 2:
        return [f"的「{label}」有改动却没摆两行完整句"
                f"（§7③：⛔ 只写 xxx → yyy 不算 diff）"]
    # ★ 这里直接用 RE_ELLIPSIS、不走 _truncated：`无 diff（＝上一版）` 已在段级豁免过了，
    #   摆出来的**句子行**里再出现省略记号一律不认（⛔ 别再给第二个豁免口子）。
    out, fname = [], os.path.basename(sc["path"])
    for i, s in enumerate(sents):
        if not RE_ELLIPSIS.search(s):
            continue
        pos = "起点句" if i == 0 else "终点句" if i == 1 else f"第 {i+1} 行"
        ln = _locate(sc, blk, s)
        out.append(f"的「{label}」{pos}用省略号截断了 —— "
                   f"{fname} {('L%d' % ln) if ln else '（行号定位不到）'}："
                   f"`{s[:56]}`　§7③：看不到完整句就不算 diff")
    return out


def cmd_deliver(args):
    path = args.session
    if not os.path.isabs(path) and not os.path.exists(path):
        path = os.path.join(SESSIONS, os.path.basename(path))
    if not os.path.exists(path):
        sys.exit(f"⛔ session 文件不存在：{args.session}")
    sc = scan_session(path)
    only = {"复习组": "group", "复检组": "recheck", "新题": "new", "重答": "redo",
            "加练": "extra", "回看": "look"}.get(args.section) if args.section else None
    if args.section and only is None:
        sys.exit(f"⛔ --section 只认 复习组／复检组／新题／重答／加练／回看，"
                 f"收到「{args.section}」")
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
def _ids_of(title):
    """节标题里的题号 → ['bank:238', 'R10', …]（顺序同标题）"""
    return (["bank:" + m.group(1) for m in RE_BANK.finditer(title)] +
            ["R" + m.group(1) for m in RE_REDO_ID.finditer(title)])


def _quad_parts(sc, sec):
    """自由产出节 → {关键词: [原文行]}：四件套各小节 `###` 标题之后、下一个 `###` 之前的原文。
    ★ 围栏照留（贴回去还是代码块）；围栏外的 ★ 注释行与空行不算四件套。"""
    lines, heads = sc["lines"], []
    for i in range(sec["start"], sec["end"]):
        if i in sc["infence"]:
            continue
        m = RE_H3.match(lines[i])
        if m:
            t = m.group(1)
            key = next((k for _, k in QUAD_KEYS
                        if k in t and not (k == "更好版" and "最小" in t)), None)
            heads.append((i, key))
    out = {}
    for n, (i, key) in enumerate(heads):
        if key is None or key in out:
            continue
        j = heads[n + 1][0] if n + 1 < len(heads) else sec["end"]
        keep, inf = [], False
        for l in lines[i + 1:j]:
            if l.startswith("```"):
                inf = not inf
                keep.append(l)
            elif inf or (l.strip() and not l.strip().startswith("★")):
                keep.append(l)
        out[key] = keep
    return out


def _quad_need(part):
    """一个小节里必须逐字出现的内容行（去掉围栏记号与空行，首尾空白不计）。"""
    return [l.strip() for l in part if l.strip() and not l.startswith("```")]


def find_free_source(pid, before):
    """→ 题号为 pid、日期早于 before 的**最近一篇**自由产出原篇：
    dict(file, date, line, parts)；找不到 → None。
    同一份 session 里同一题号的几个节（抽题记录＋逐题记录）合并取四件套。"""
    if not os.path.isdir(SESSIONS):
        return None
    best = None
    for f in sorted(os.listdir(SESSIONS)):
        m = RE_SESS_NAME.match(f)
        if not m or m.group(1) >= before:
            continue
        sc = scan_session(os.path.join(SESSIONS, f))
        parts, line = {}, None
        for s in sc["sections"]:
            # ★ 旧 R 号与它的 bank:NNN 是同一道题（redo_key）
            if s["kind"] not in ("new", "redo", "extra") or \
                    redo_key(pid) not in {redo_key(x) for x in _ids_of(s["title"])}:
                continue
            line = line or s["line"]
            for k, v in _quad_parts(sc, s).items():
                parts.setdefault(k, v)
        if line:
            best = dict(file=f, date=sc["date"], line=line, parts=parts)
    return best


def cycle_free_ids(today):
    """本周期（最后一个付息日之后、今天之前）全部自由产出的题号，按日期顺序。"""
    files = sorted(f for f in os.listdir(SESSIONS)
                   if RE_SESS_NAME.match(f) and f[:10] < today) if os.path.isdir(SESSIONS) else []
    last_r = None
    for f in files:
        with open(os.path.join(SESSIONS, f), encoding="utf-8") as fh:
            if RE_R_HEAD.search(fh.readline()):
                last_r = f
    news, _ = scan_all_sessions()
    ids = []
    for x in news:
        if x["id"] and x["file"] in files and (last_r is None or x["file"] > last_r) \
                and x["id"] not in ids:
            ids.append(x["id"])
    return ids


def pending_free_ids(today):
    """【没被回看过】的全部自由产出题号，按日期顺序（§4② 学习日回看口径 ＝ 全部，不是最近一篇）。"""
    news, looked = scan_all_sessions()
    ids = []
    for x in news:
        if x["id"] and not looks_of(x, looked) and x["date"] < today \
                and redo_key(x["id"]) not in {redo_key(y) for y in ids}:
            ids.append(x["id"])
    return ids


def looks_of(x, looked):
    """这一篇自由产出【之后】的回看记录 → [(日期, 文件, 行)]。
    ★ 按 redo_key 认（旧 R 号 ＝ 它的 bank:NNN）；同一道题重答过 ⇒ 更早的回看不算这一篇的。"""
    return [t for t in looked.get(redo_key(x["id"]), []) if t[0] > x["date"]]


def print_quads(ids, today):
    """把每一篇的四件套原文打出来 —— 原样贴进 session 的回看节，同一段发聊天（§4②）。"""
    rc = 0
    for pid in ids:
        src = find_free_source(pid, today)
        if not src:
            print(f"⛔ {pid}：{today} 之前找不到这篇自由产出的原篇")
            rc = 1
            continue
        print(f"### 回看 · {pid}（原篇 {src['file']}:L{src['line']} · 逐字）")
        print()
        for name, key in QUAD_KEYS:
            part = src["parts"].get(key)
            if not part:
                if key in QUAD_MUST:
                    print(f"⛔ 原篇缺「{name}」节")
                    rc = 1
                continue
            print(f"**{name}**")
            print()
            print("\n".join(part))
            print()
    return rc


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
                ids = _ids_of(s["title"])
                for pid in (ids or [None]):
                    # 同一文件同一题号只算一篇：抽题记录节与逐题记录节是同一篇产出
                    #   （旧 R 号与它的 bank:NNN 算同一个题号）
                    if pid and any(x["file"] == f and x["id"] and
                                   redo_key(x["id"]) == redo_key(pid) for x in news):
                        continue
                    news.append(dict(id=pid, kind=s["kind"], date=sc["date"],
                                     title=s["title"], line=s["line"], file=f))
            elif s["kind"] == "look":
                # ★ 键 ＝ redo_key：回看 R10 与回看 bank:303 是同一道题
                for pid in _ids_of(s["title"]):
                    looked.setdefault(redo_key(pid), []).append((sc["date"], f, s["line"]))
    return news, looked


def cmd_lookback(args):
    today = args.date or date.today().isoformat()
    if args.print_ids or args.cycle or args.pending:
        ids = list(args.print_ids or [])
        if args.cycle:
            ids += [x for x in cycle_free_ids(today) if x not in ids]
        if args.pending:
            ids += [x for x in pending_free_ids(today) if x not in ids]
        if not ids:
            if args.cycle:
                print("（本周期没有自由产出 ⇒ 回看节写 `## ⓪ 回看 · 无（理由）`）")
            else:
                print("（没有未回看的自由产出 ⇒ 回看节写 `## ② 回看 · 无（理由）`）")
            return 0
        print(f"<!-- lab.py lookback --print · {today} · 回看节标题写：回看 · {' · '.join(ids)} -->")
        print()
        return print_quads(ids, today)
    news, looked = scan_all_sessions()
    W = "═" * 78
    print(W)
    print(f"lab.py lookback · {today} · §4② 回看目标　【只读：⛔ 不写任何文件】")
    print(W)
    print("  口径　回看目标 ＝ **全部【没被回看过】的自由产出**（新题／重答／加练）—— ⛔ 不是只发最近一篇")
    print("  认法　自由产出 ＝ session 里 `## ③ 新题 …（bank:NNN）` / `## d 段 重答 · bank:NNN`（旧题 RN）的标题行")
    print("  　　　已回看 ＝ 任意 session 的 `## ② 回看 · bank:NNN` **标题行**上的题号")
    print(f"  扫的　{SESSIONS}/*.md")
    print()
    print("① 全部自由产出（逐条列）")
    noid = [x for x in news if not x["id"]]
    for x in news:
        tag = x["id"] or "⛔无题号"
        if x["id"] and looks_of(x, looked):
            mark = "✅ 已回看　← " + "／".join(f"{d}:{f}:{l}" for d, f, l in looks_of(x, looked))
        elif not x["id"]:
            mark = "⛔ 标题没带题号 ⇒ 追不了（§9.1 要求写 bank:NNN／RN）"
        elif x["date"] >= today:
            mark = "⚠️ 今天（或更晚）写的 ⇒ 本次⛔不作目标"
        else:
            mark = "⏳ 未回看"
        print(f"   {tag:<10} {x['date']}  {x['file']}:{x['line']}  {mark}")
    print(f"   ── 共 {len(news)} 篇（其中 {len(noid)} 篇标题没带题号）")
    print()
    cand = [x for x in news if x["id"] and not looks_of(x, looked) and x["date"] < today]
    print("② 本次回看目标 ＝ **全部没被回看过的**（⛔ 一篇都不许省，⛔ 不挑最近那一篇）")
    if not cand:
        print("   （没有未回看的自由产出 ⇒ 回看节写 `## ② 回看 · 无（理由）`）")
    else:
        cand = sorted(cand, key=lambda x: (x["date"], x["line"]))
        for t in cand:
            print(f"   ★ {t['id']}　{t['date']}　{t['file']}:{t['line']}")
            print(f"     标题：{t['title'][:60]}")
        print(f"   ── 共 {len(cand)} 篇，四件套逐字取自各自那一节，⛔ 禁止重新推导（§4②）")
        print("   ⇒ 执行：`lab.py lookback --pending` 一次打出全部原文 ⇒ 整段原样贴进回看节")
        print("     回看节标题写：## ② 回看 · " + " · ".join(x["id"] for x in cand))
    print(W)
    return 0

# ══════════════════════════════════════════════════════════════════════════
#  prompts —— 题面逐字核对（SKILL §6「执行动作写死」的机器版）
#
#  §6 原来写的是三步手工仪式：① 先 grep/awk 打出整行 ② 从打出来的那行复制
#  ③ 发送前逐句对一遍。第 ③ 步是纯散文钩子，挡不住。
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
        print(f"   #{n:<5} {e.src}:{e.start + off}　｜　题型 {e.ask_kind}"
              + ("" if e.ask else "（⚠️ 未标 · 按整句读 —— 发题前先回标状态行，§6.0）"))
        if e.body_v3:
            print(f"          ↓ **题面** 节（§3.1 契约⑫）⇒ 引号句与括号限定逐字复制；★ 行是教练注释，⛔ 不进发题稿")
            for l in e.prompt_lines:
                print(f"          {l}")
            continue
        print(f"          {meta}")
        print(f"          ⚠️ 存量一行式条目（正文未升级，§3.1 契约⑭）")
        if e.prompt_lines:
            print(f"          ↓ 题面自成一段（合并条 §3.2c）⇒ **整段逐字复制，一句都不许少**")
            for l in e.prompt_lines:
                print(f"          {l}")
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
#     grep 数的是字符串出现次数，不是符合口径的条目数。
#     `grep -c "^### "` 减它 ⇒ 未毕业 29（真值 13，把 17 条墓碑/迁出当成了在池）。
#  ★ 每个类型都并排打【全档】与【未毕业】两个数 —— 报数必须说清是哪一个。
# ══════════════════════════════════════════════════════════════════════════
def _has_oldno(e):
    return any("旧号" in l for l in e.raw[:3])


def _today():
    return date.today().isoformat()


def _selfpass_fell(e):
    """⚡ 自评免测之后又掉过 ⇒ 那一票没兑现（§4③ 的校准数，不是限制）。"""
    sp = e.selfpassed()
    if not sp:
        return False
    first = min(h.date for h in sp)
    return any(h.symbol in ("❌", "📖") and h.date > first for h in e.history)


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
    ("multi",     "合并条·多句覆盖", f"状态行标记 `{M_MERGED}`（§3.2c）"
                                    " ⇒ 出题必须多句覆盖全部成员",              lambda e: M_MERGED in e.marks),
    ("stubborn",  "顽固",         f"状态行标记 `{M_STUBBORN}`",                lambda e: M_STUBBORN in e.marks),
    # ── 进度类（只对未毕业有意义）──────────────────────────────────
    ("streak0",   "未毕业·连对 0", "未毕业 ＋ 连对 0",                          lambda e: not e.graduated and e.ok == 0),
    ("streak1",   "未毕业·连对 1", "未毕业 ＋ 连对 1（差一次毕业）",             lambda e: not e.graduated and e.ok == 1),
    ("streak2+",  "未毕业·连对 ≥2", "未毕业 ＋ 连对 ≥2 ⚠️ 到线未毕业，⛔ 要修",  lambda e: not e.graduated and (e.ok or 0) >= 2),
    ("bad2+",     "连错 ≥2",      "连错 ≥2（§3.5 梯子最急的一格）",                     lambda e: (e.bad or 0) >= 2),
    ("everbad",   "犯过错的",      "历史里出现过 ❌ 或 📖",                      lambda e: e.ever_bad()),
    # ── 召回队列类（§3.5 梯子）⛔ 这几个数只有 count 会算，grep 一律算不对 ──
    ("recallable", "进召回队列",  "非墓碑 ＋ 无「不召回／停出」标记"
                                  "（⚠️ 🎓 **也在队列里** —— 毕业不是冻结）",   lambda e: e.recallable),
    ("due",       "今天到期",     "进队列 ＋ 逾期分 ≥1（已等练习日 ÷ 应等间隔）",
                                                                lambda e: e.recallable and overdue(e, _today()) >= 1),
    ("overdue2",  "逾期 ≥2 倍",   "进队列 ＋ 逾期分 ≥2（该等的时间已经过去两轮）",
                                                                lambda e: e.recallable and overdue(e, _today()) >= 2),
    ("risk",      "在池降格",     "未毕业 ＋ 掉过 ❌/📖 ⇒ 在梯子上降一格（§3.5；复检队列不降格）",
                                                                lambda e: e.at_risk()),
    ("selfpass",  "⚡ 自评免测过", "日志里有 ⚡ 行（§4③ 校准数从这里数）",        lambda e: bool(e.selfpassed())),
    ("selfpass-fell", "⚡ 之后又掉过", "★ **自评校准数**：⚡ 之后还出现过 ❌/📖 ⇒ 那一票没兑现",
                                                                _selfpass_fell),
    # ── 题型类（§6.0，状态行「题型」格；三个相加 ＝ 全档总数）──────────
    ("ask-sentence", "题型·整句",   "状态行「题型」＝ 整句，**或没写这一格**（默认，存量就是这么算的）",
                                                                lambda e: e.ask_kind == ASK_SENTENCE),
    ("ask-phrase",   "题型·词组",   "状态行「题型」＝ 词组 —— 中文块 → 英文块（§6.1）",
                                                                lambda e: e.ask_kind == ASK_PHRASE),
    ("ask-retired",  "题型·已取消", "状态行「题型」＝ 产出验（机制已取消 ⇒ **应为 0**）",
                                                                lambda e: e.ask in ASK_RETIRED),
    ("ask-unmarked", "题型·未标",   "状态行没写「题型」格（按整句读；抽到时回标，付息日 c 段清）",
                                                                lambda e: e.ask is None and not e.tomb),
    # ── 题面类 ───────────────────────────────────────────────────
    ("prompt-todo", "题面待补",   "题面节／题面字段为空 ⇒ ⛔ 出不了题",          lambda e: not e.prompt),
    # ── 正文类（§3.1 契约⑪–⑭，2026-09-12 起）────────────────────────
    ("body-v3",     "正文四节",   "正文有 **问题是什么／怎么发现的／我错在哪／题面** 节（§3.1 契约⑪）",
                                                                lambda e: e.body_v3),
    ("body-legacy", "正文待升级", "一行式存量（无四节）⇒ 逐条手写升级（§3.1 契约⑭；⛔ 禁脚本）",
                                                                lambda e: not e.body_v3),
    ("members",     "挂成员出题账", "正文有 **成员出题账**（合并条必挂，§3.2c④）",  lambda e: e.members is not None),
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


def _rung_name(i):
    return RUNGS[i][0]


def cmd_count(args):
    ents = load_all()
    live = [e for e in ents if not e.tomb]          # 全档口径：墓碑不占数
    ungrad = [e for e in live if not e.graduated]
    W = "═" * 78

    def sel_of(slug):
        if slug.startswith("kind:"):
            k = slug[5:]
            return [e for e in live if e.kind == k], f"类型 {k}", f"元信息第一格 ＝ {k}"
        if slug.startswith("rung:"):
            try:
                i = int(slug[5:])
                assert 0 <= i < len(RUNGS)
            except Exception:
                sys.exit(f"⛔ rung 只有 0–{len(RUNGS)-1} 这几格（跑 count 看全表）")
            return ([e for e in live if e.recallable and e.rung() == i],
                    f"梯子第 {i} 格 · {RUNGS[i][0]}",
                    f"§3.5 召回梯子第 {i} 格 ⇒ 应等 {RUNGS[i][1]} 个练习日")
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
        print("─" * 78)
        rec = [e for e in live if e.recallable]
        for i, (nm, iv) in enumerate(RUNGS):
            n_all = sum(1 for e in rec if e.rung() == i)
            n_ug = sum(1 for e in rec if not e.graduated and e.rung() == i)
            print(f"{'rung:'+str(i):<15}{nm:<16}{n_all:>6}{n_ug:>8}"
                  f"   §3.5 梯子第 {i} 格 ⇒ 应等 {iv} 个练习日")
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
def bundlable(e):
    """能不能进打包题（§6.1）。
    ⛔ 合并条（§3.2c 出题须多句覆盖）与**题面待补**的条目永不打包 —— 它们各占一题。
    ★ 题型格（§6.0）说了算：标了「词组」的打包，标了「整句」的不打包；
      没标的（存量）沿用旧口径 —— 类型 ∈ 词组/词汇/搭配 才打包。"""
    if M_MERGED in e.marks or not e.prompt:
        return False
    ask = getattr(e, "ask", None)          # 测试夹具的 FakeE 可能没这个字段 ⇒ 当没标
    if ask == ASK_PHRASE:
        return True
    if ask == ASK_SENTENCE:
        return False
    return e.kind in BUNDLE_KINDS


def bundle(cands):
    """把队列切成【题】：词组/词汇/搭配 最多 6 条并成一道中译英词组串，其余一条一题。

    ★ 顺序保证：**每道题的头一条永远是队列里当下最靠前的那一条** ——
      打包只让它把后面同类的捎上，⛔ 绝不会把靠前的条目往后压。
    ★ 捎带范围封了顶（BUNDLE_REACH）：不许从队尾把排得远的条目拽上来。"""
    q = list(cands)
    out = []
    while q:
        head = q.pop(0)
        if not bundlable(head):
            out.append([head])
            continue
        grp, i = [head], 0
        while i < min(len(q), BUNDLE_REACH) and len(grp) < BUNDLE_MAX:
            if bundlable(q[i]):
                grp.append(q.pop(i))      # pop 之后 i 不前进
            else:
                i += 1
        out.append(grp)
    return out


def qtargets(q):
    t = set()
    for e in q:
        t |= e.targets()
    return t


def partition(qs, size):
    """切成 ≤size 一组，并做 §6 组内防撞：相邻两题不测同一个词。
    ⚠️ 单位是【题】—— 一道打包题里的多条条目算同一题。"""
    buckets = [qs[i:i + size] for i in range(0, len(qs), size)]
    for b in buckets:
        for i in range(1, len(b)):
            if qtargets(b[i]) & qtargets(b[i - 1]):
                for j in range(i + 1, len(b)):
                    if not (qtargets(b[j]) & qtargets(b[i - 1])):
                        b[i], b[j] = b[j], b[i]
                        break
    return buckets


def card(e, why, full=False):
    ok, bad = e.recount()
    mk = " ".join(sorted(e.marks)) if e.marks else ""
    st = f"🎓 rc{e.rechecks()}" if e.graduated else f"连对{ok} 连错{bad}"
    if e.pulled_back():
        st += " ｜🔙 她说没底·顶到队首"
    ask = f"题型 {e.ask_kind}" + ("" if e.ask else "（未标·按整句读 ⇒ 发题前回标）")
    out = [f"  #{e.num:<4d} [{e.kind or '—'}] {e.title[:60]}",
           f"        {st} ｜ 有效上次 {e.eff_last() or '—'} ｜ {why}"
           + (f" ｜ {mk}" if mk else ""),
           f"        {ask} ｜ 题面 {(e.prompt or '⚠️ 待补 —— 抽到就当场补成完整中文句')[:70]}"]
    if M_MERGED in e.marks:
        out.append("        ⚠️ 合并条：本次出题**必须多句覆盖全部成员**（§3.2c②），只出一句 ＝ 违规")
    if full:
        for h in e.history[-4:]:
            out.append(f"        · {h.date} {h.symbol or '?'} {(h.occasion or '')[:52]}")
    return "\n".join(out)


def cmd_pick(args):
    """§3.5 召回队列 —— 一条梯子、两条队列（在池／复检），逾期分排序。

    ⛔ 教练不许自己挑题、不许自己排序：候选、顺序、分组全在这里定死，
       同一天重跑这条命令结果完全一样（`used`／`免测` 过的自动不再出现）。"""
    today = args.date or date.today().isoformat()
    if args.type not in QUOTA:
        sys.exit(f"⛔ --type 只认 {' / '.join(QUOTA)}（learn ＝ 学习日，review ＝ 付息日）")
    if args.size < 1:
        sys.exit(f"⛔ --size 要 ≥1，收到 {args.size}"
                 f"（0 会直接抛 ValueError，负数会静默出 0 组还谎报「没有到期的」）")
    days = practice_days()
    npool, ngrad = QUOTA[args.type]
    used, done = read_drawn(today)

    drop = defaultdict(list)
    cand = []
    for e in load_all():
        if e.tomb:
            continue
        if not e.recallable:
            drop[e.block_reason or "?"].append(e.num)
            continue
        if e.created_on() == today:
            drop["今天刚建号 —— 建号当天不回考（§3.1）"].append(e.num)
            continue
        if e.num in used:
            drop["本场已出过／已 ⚡ 免测／已弃（drawn.log）"].append(e.num)
            continue
        cand.append(e)

    scored = sorted(cand, key=lambda e: queue_key(e, today, days))
    due = [e for e in scored if overdue(e, today, days) >= 1]
    notyet = [e for e in scored if overdue(e, today, days) < 1]
    pool = [e for e in due if not e.graduated]
    grd = [e for e in due if e.graduated]

    W = "═" * 78
    print(W)
    print(f"lab.py pick · {args.type} · {today}"
          f"（{'学习日' if args.type == 'learn' else '付息日'}·配额 在池 {npool} 组 ／ 复检 {ngrad} 组）")
    print(W)
    print("排序 ＝ 在池：逾期分降序 → 掉过的优先 → 编号升序"
          "　｜　复检：复检次数少的优先 → 已等练习日多的优先 → 编号升序")
    print("到期 ＝ 已等练习日 ≥ 梯子上的应等间隔　｜　逾期分 ＝ 已等练习日 ÷ 应等间隔")
    print(f"练习日共 {len(days)} 个（{days[0] if days else '—'}…{days[-1] if days else '—'}）"
          f"，今天{'也' if today in days else '不'}在其中，本场按【今天算一个练习日】计")
    print(f"进队列 {len(cand)} 条 ⇒ **今天到期 {len(due)} 条**"
          f"（在池 {len(pool)} ／ 复检 {len(grd)}）｜ 未到期 {len(notyet)} 条")
    noq = [e.num for e in due if not e.prompt]
    if noq:
        print(f"⚠️ 到期的里有 {len(noq)} 条**没有题面**，出不了题 ⇒ 抽到就当场补成完整中文句："
              f"{fmt_ids(noq, 16, '')}")
    if drop:
        print(f"⛔ 不进队列：")
        for w, ns in sorted(drop.items(), key=lambda x: -len(x[1])):
            print(f"     {w:<38s} {len(ns):>3d} 条  {fmt_ids(ns, 16, '')}")

    # ── 分组：在池是**上限**，空出来的组数下溢给复检（⛔ 反向不成立）────────
    want_pool = args.scope in ("pool", "both")
    pool_g = partition([[e] for e in pool], args.size)[:npool] if want_pool else []
    # ⚠️ 下溢只在【真的排了在池队列却没排满】时成立。
    #    --scope grad 时 pool_g 天然是空的，那不是"排不满"，是"根本没排" ——
    #    无条件 spill = npool 会把复检配额悄悄翻几倍。
    spill = max(npool - len(pool_g), 0) if want_pool else 0
    ngrad_eff = (ngrad + spill) if args.scope in ("grad", "both") else 0
    grad_g = partition(bundle(grd), args.size)[:ngrad_eff]
    if spill:
        print(f"★ 在池只排得出 {len(pool_g)} 组（上限 {npool}）⇒ 空出的 {spill} 组"
              f"**下溢给复检队列** ⇒ 复检 {ngrad} ＋ {spill} ＝ {ngrad_eff} 组")

    gno = 0
    for name, gs in (("在池组", pool_g), ("复检组", grad_g)):
        if not gs:
            print(f"\n── {name} ── 空（队列里没有到期的）")
            continue
        for bk in gs:
            gno += 1
            tag = f"第 {gno} 组"
            ncond = sum(len(q) for q in bk)
            print(f"\n── {name} · {tag}（**{len(bk)} 题 / 覆盖 {ncond} 条**）"
                  + ("　✅ 已 used" if tag in done else "") + " " + "─" * 20)
            for qi, q in enumerate(bk, 1):
                if len(q) > 1:
                    print(f"  [{qi}] 打包 · " + " ".join(f"#{e.num}" for e in q)
                          + f"　（{len(q)} 条中译英词组串，**逐条判定**）")
                else:
                    print(f"  [{qi}] #{q[0].num}")
                for e in q:
                    if e.graduated:
                        why = (f"复检 rc{e.rechecks()} ｜ 已等 {waited_days(e, today, days)}"
                               f" ｜ 应等 {e.interval()} ｜ 梯子 {e.rung_name()}")
                    else:
                        sc = overdue(e, today, days)
                        why = (f"逾期分 {sc:.1f} ｜ 梯子 {e.rung_name()} ｜ 应等 {e.interval()}"
                               f" ｜ 已等 {waited_days(e, today, days)}")
                    print(card(e, why, args.full))
            if not args.dry:
                append_drawn("\t".join(
                    [today, tag, "抽",
                     ",".join(str(e.num) for q in bk for e in q)]))

    print("\n" + "─" * 78)
    print("⛔ 脚本做不到、必须教练手工的两件（§6）：① 题面逐字核对 `lab.py prompts N N N`"
          " ② 第二译法自查（逐题写有/无，有就点名）")
    print('每组定稿后跑：lab.py used --group N --used "12,45" '
          '[--exempt "232,233"] [--dropped "88=理由"]')
    print(W)
    return 0


def cmd_used(args):
    """每组定稿写流水。--exempt ＝ 她当场 ⚡ 免测的条目（§4③）。

    ⚠️ 这里只写 **drawn.log 流水**（防同一天重复抽到）。
       ⚡ 行本身仍然由教练手写、走 `append` 落盘 —— 与判定行同一条边界：
       **脚本不产生任何一个字的内容**（§0.1.2）。"""
    today = args.date or date.today().isoformat()
    tag = f"第 {args.group} 组"
    append_drawn("\t".join([today, tag, "用", args.used.replace(" ", "")]))
    if args.exempt:
        append_drawn("\t".join([today, tag, "免", args.exempt.replace(" ", "")]))
    if args.dropped:
        append_drawn("\t".join([today, tag, "弃", args.dropped]))
    print(f"已记：{today} {tag} 用 [{args.used}]"
          + (f" ⚡免 [{args.exempt}]" if args.exempt else "")
          + (f" 弃 [{args.dropped}]" if args.dropped else ""))
    if args.exempt:
        ns = [x for x in args.exempt.replace(" ", "").split(",") if x]
        print(f"★ 还欠 {len(ns)} 行 ⚡：每条在档案里手写一行"
              f" `- {today} ⚡ 自评免测 · 复检{tag}`，再走 `lab.py append` 落盘（§4③）")
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
BAD_IN_BODY = ("状态 ", "### ", "**问题是什么**", "**怎么发现的**", "**我错在哪**", "**题面**", "**成员出题账**")


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


def _fell_after_grad(e):
    """毕业**之后**掉过 ⇒ 该回潮（§3.3）。
    ⛔ 不能拿 recount() 的连错判：那个数冻结在毕业日，毕业后的 ❌ 顶不上去。"""
    g = e.freeze_at()
    if not g:
        return False
    return any(h.symbol in ("❌", "📖") and h.date > g for h in e.history)


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
        if e.tomb:
            errs.append(f"{tag} 是墓碑/迁出条目 —— ⛔ 不再记判定")
        elif e.status_lineno is None:
            errs.append(f"{tag} 找不到状态行")
        else:
            b["pre_err"] = {m for lv, m in check_entry(e, set(), None) if lv == "ERROR"}
            if e.marks & {M_MORPH, M_ONLYLOG} and b["symbol"] in ("✅", "❌", "⚡"):
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

    # ── 两个文件都可能被写（§3.5 复检：毕业条目每天都在记判定行）───────────
    #    边界一个字没松：脚本仍然**只做插入位置 ＋ 三个数重算**，
    #    ⛔ 不改 🎓、不改状态、不碰正文；毕业条目的连对/连错本来就冻结在毕业日，
    #    所以写进去只会动「上次」这一个字段（§3.1 契约⑧）。
    FILES = {k: v for k, v in (("problems.md", PROBLEMS), ("graduated.md", GRADUATED))
             if os.path.exists(v)}          # ⚠️ 缺文件要容忍：别的子命令都容忍，只有这里会崩
    orig = {k: open(v, encoding="utf-8").read() for k, v in FILES.items()}
    plans = {}
    for srcname, path in FILES.items():
        mine = [b for b in blocks if b["entry"].src == srcname]
        if not mine:
            continue
        lines = orig[srcname].split("\n")
        plan = []
        for b in mine:
            e = b["entry"]
            hi = e.end or len(lines)
            # 插入点 ＝【最后一条日期行的正文之后】，⛔ 不是条目末尾 ——
            # 口语档案的约定：判定行按日期挨在一起，尾部的 `- 备注 …` 块留在最后。
            # 正文的边界：空行/缩进行/围栏内的行都算正文，第一个顶格非围栏行 ⇒ 停。
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
                # ★ v3 条目：正文四节挂在状态行后面 ⇒ 插到**正文最后一个非空行**之后（§3.1 契约⑤）
                at = e.body_end if e.body_end else e.status_lineno
                j, fence = at, False
                while j < hi:                # 跳过状态行后面的 ★ 续行
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
        plans[srcname] = plan

    if args.dry_run:
        print("═" * 74)
        print(f"lab.py append --dry-run · {sum(len(p) for p in plans.values())} 条"
              f" · {today}（⛔ 没写盘）")
        print("═" * 74)
        for srcname, plan in plans.items():
            for p in sorted(plan, key=lambda x: x["at"]):
                print(f"  #{p['e'].num}  插到 {srcname} L{p['at']}（{len(p['block'])} 行）")
                print(f"      {p['block'][0][:88]}")
        for w in warns:
            print("WARN   " + w)
        print("═" * 74)
        return 0

    moved = []
    for srcname, plan in plans.items():
        path = FILES[srcname]
        lines = orig[srcname].split("\n")
        for p in sorted(plan, key=lambda x: -x["at"]):
            body = list(p["block"])
            while body and not body[-1].strip():
                body.pop()
            lines[p["at"]:p["at"]] = body
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        # 三个数重算（⛔ 只这三个：连对／连错／上次）
        idx = {e.num: e for e in parse_file(path, srcname)}
        lines = open(path, encoding="utf-8").read().split("\n")
        for p in plan:
            e2 = idx[p["e"].num]
            ok, bad = e2.recount()
            last = e2.last_tested() or "—"
            i = e2.status_lineno - 1
            lines[i] = rewrite_status(lines[i], ok, bad, last)
            moved.append((srcname, e2, ok, bad, last))
        open(path, "w", encoding="utf-8").write("\n".join(lines))

    ents3 = load_all()
    all_nums = {e.num for e in ents3}
    idx3 = {e.num: e for e in ents3}
    hard = {(b["entry"].src, h.lineno) for b in blocks
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
        for k, v in FILES.items():                    # ⛔ 两个文件一起整批回滚
            open(v, "w", encoding="utf-8").write(orig[k])
        print("═" * 74)
        print(f"lab.py append · ⛔ 写完自查不过，{len(bad_rows)} 处 —— 两个文件已整批回滚")
        print("═" * 74)
        for n, m in bad_rows:
            print(f"ERROR  #{n}  {m}")
        print("═" * 74)
        return 1

    print("═" * 74)
    where = " ＋ ".join(f"{k} {len(v)} 条" for k, v in plans.items())
    print(f"lab.py append · {where} · {today} · 自查 ERROR 0")
    print("═" * 74)
    for srcname, e3, ok, bad, last in moved:
        flag = ""
        if not e3.graduated and ok >= 2:
            flag = "   ⇒ ★ 连对到 2，§3.3 要你原地标 🎓 已毕业（脚本⛔不代改）"
        elif e3.graduated and _fell_after_grad(e3):
            # ⚠️ ⛔ 不能用 recount() 的 bad 判 —— 毕业条目的连对/连错**冻结在毕业日**，
            #    毕业后的 ❌ 永远不会把 bad 顶上去。
            flag = "   ⇒ ★ 🎓 条目吃到 ❌，§3.3 回潮：要你把状态行改回未毕业（脚本⛔不代改）"
        print(f"  #{e3.num}  {'🎓' if e3.graduated else '未毕业'}  "
              f"连对{ok} 连错{bad} ｜ 上次 {last} ｜ {srcname}{flag}")
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

    p = sub.add_parser("pick", help="召回队列：按逾期分一次分完组（§3.5）")
    p.add_argument("--type", choices=["learn", "review"], required=True,
                   help="learn ＝ 学习日（在池 3 组 / 复检 1 组）"
                        " ｜ review ＝ 付息日（在池 5 组 / 复检 3 组）")
    p.add_argument("--scope", choices=["pool", "grad", "both"], default="both",
                   help="只看在池队列 / 只看复检队列 / 两条都要（默认）")
    p.add_argument("--size", type=int, default=GROUP_SIZE, help="一组几**题**（默认 10）")
    p.add_argument("--full", action="store_true", help="卡片带历史留痕")
    p.add_argument("--date")
    p.add_argument("--dry", action="store_true", help="不写 drawn.log")
    p.set_defaults(func=cmd_pick)

    p = sub.add_parser("used", help="记录本组定稿用了哪几条、免了哪几条、弃了哪几条")
    p.add_argument("--group", type=int, required=True)
    p.add_argument("--used", required=True)
    p.add_argument("--exempt", help="她 ⚡ 免测的条目号（§4③，⛔ 无类型限制）")
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
    p.add_argument("--section",
                   help="复习组／复检组／新题／重答／加练／回看；不给则扫全部")
    p.set_defaults(func=cmd_deliver)

    p = sub.add_parser("lookback", help="哪几篇自由产出还没被回看过（§4②，只读）")
    p.add_argument("--date", help="把哪一天当「今天」（默认今天）")
    p.add_argument("--print", dest="print_ids", nargs="+", metavar="ID",
                   help="打出这几篇（bank:NNN／RN）的四件套原文，原样贴进回看节")
    p.add_argument("--pending", action="store_true",
                   help="打出【全部没被回看过】的自由产出的四件套（学习日 ② 用）")
    p.add_argument("--cycle", action="store_true",
                   help="打出本周期全部自由产出的四件套（付息日 ⓪ 用）")
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

    p = sub.add_parser("redo", help="重答队列（§5d）：实时算，最久没重答的在最上面（只读）")
    p.set_defaults(func=cmd_redo)

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
