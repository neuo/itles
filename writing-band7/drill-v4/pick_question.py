#!/usr/bin/env python3
"""随机抽题器 —— 写作 drill 线唯一合法的出题方式（她 2026-08-11 定）。

她的原话：
    "出题应该随机抽，(这个随机脚本，别让llm自己选，做个题库，以后也能加题)
     但是同一个题之前隔3天以上才能再出"

为什么必须是脚本：教练自己排序会不自觉地挑"刚练过的 / 好判的 / 靶子刚好落得上的"。
脚本抽 = 教练无从选择。**抽到什么写什么，不许重抽、不许"这题不合适换一个"。**
（与"记录禁脚本"不冲突：记录禁脚本是为了不漏，抽题用脚本是为了教练无从选择。
  本脚本只【读 bank.md】+【append 一行 drawn.log】，不写任何内容文件。）

题库 = writing-band7/drill/bank.md 里所有 `### T2-nn` / `### T1-nn` 小节。
      ★ 加题 = 在 bank.md 里加一个 `### T2-26 …` 小节 + 紧跟一段 `> 题面`，
        脚本自动看见，**不需要改脚本**。

冷却 = 同一题距上次出题 < COOLDOWN_DAYS 天的，本次不抽（历史读 drawn.log）。

用法
    python3 writing-band7/drill/pick_question.py            按权重抽 1 题
    python3 writing-band7/drill/pick_question.py t2         强制只抽 T2
    python3 writing-band7/drill/pick_question.py t1 2       强制抽 2 道 T1
    python3 writing-band7/drill/pick_question.py any        T1+T2 混在一起等概率
    python3 writing-band7/drill/pick_question.py --dry      只看候选池，不写 drawn.log
    加 --repeat 忽略冷却
"""

import random
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent                 # writing-band7/drill/
BANK = ROOT / "bank.md"
DRAWN = ROOT / "drawn.log"

# ★ 冷却天数（她 2026-08-11 定）：同一题距上次出题 >= 这么多天才能再出
COOLDOWN_DAYS = 3

# ★ 权重 —— 改这一行就改了全局出题分布
#   依据：Writing 总分 = (T1 + 2×T2) / 3，且她当前主攻 T2
WEIGHTS = {"t2": 0.70, "t1": 0.30}

HEAD = re.compile(r"^### (T[12]-\d+)\s+(.*)$")


def parse_bank():
    """返回 ({'t2': [...], 't1': [...]}, excluded)。
    每项 = dict(id, title, prompt, line)。prompt = 标题后紧跟的第一段 blockquote。"""
    out = {"t2": [], "t1": []}
    excluded = []
    lines = BANK.read_text(encoding="utf-8").splitlines()

    for i, raw in enumerate(lines):
        m = HEAD.match(raw.rstrip())
        if not m:
            continue
        qid, title = m.group(1), m.group(2).strip()

        # 收题面 = 标题之后的 blockquote ＋ 图表数据表（T1 的数据也是题面的一部分）。
        # 停在下列任一处：历次成绩表 / 📍🎯📌 行 / 分隔线 / 下一个小节 / 备注型 blockquote
        prompt = []
        for nxt in lines[i + 1:]:
            s = nxt.rstrip()
            t = s.strip()
            if t.startswith("### ") or t.startswith("---"):
                break
            if t.startswith("| #") or "| 日期 |" in t:
                break
            if t[:1] in ("📍", "🎯", "📌", "⚠️"[:1]) and not t.startswith(">"):
                break
            if t.startswith(">") and t.lstrip("> ").startswith("⚠️"):
                break
            if t == "" or t == ">":
                continue
            prompt.append(s[2:] if s.startswith("> ") else s)
        prompt_text = "\n".join(prompt).strip()

        # 排除两类不可出的：交叉引用条 / 题面已丢失
        if re.search(r"见 T[12]-\d+", title) or not prompt_text:
            excluded.append((qid, "交叉引用条 / 无题面"))
            continue
        if "丢失" in prompt_text:
            excluded.append((qid, "题面或图已丢失，重跑需外部找图"))
            continue

        out["t2" if qid.startswith("T2") else "t1"].append(
            dict(id=qid, title=title, prompt=prompt_text, line=i + 1))

    return out, excluded


def load_drawn():
    """返回 {题号: 最近一次出题日期}。"""
    last = {}
    if not DRAWN.exists():
        return last
    for raw in DRAWN.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        parts = s.split("\t")
        if len(parts) < 2:
            continue
        try:
            d = datetime.strptime(parts[0].strip(), "%Y-%m-%d").date()
        except ValueError:
            continue
        qid = parts[1].strip()
        if qid not in last or d > last[qid]:
            last[qid] = d
    return last


def main():
    args = [a.lower() for a in sys.argv[1:]]
    dry = "--dry" in args
    repeat = "--repeat" in args
    args = [a for a in args if not a.startswith("--")]

    force = None
    n = 1
    for a in args:
        if a in ("t1", "t2"):
            force = a
        elif a == "any":
            force = "any"
        elif a.isdigit():
            n = int(a)

    pool, excluded = parse_bank()
    last = load_drawn()
    today = date.today()

    def eligible(items):
        if repeat:
            return list(items)
        keep = []
        for it in items:
            d = last.get(it["id"])
            if d is None or (today - d).days >= COOLDOWN_DAYS:
                keep.append(it)
        return keep

    avail = {k: eligible(v) for k, v in pool.items()}

    print(f"=== 题库 {len(pool['t2'])} 道 T2 · {len(pool['t1'])} 道 T1"
          f"（冷却 {COOLDOWN_DAYS} 天，今天 {today}）===")
    for k in ("t2", "t1"):
        blocked = [it["id"] for it in pool[k] if it not in avail[k]]
        print(f"  {k.upper()} 可抽 {len(avail[k])}/{len(pool[k])}"
              + (f"　冷却中: {' '.join(blocked)}" if blocked else ""))
    if excluded:
        print("  ⚠️ 不可出（已排除，不是静默丢弃）: "
              + " · ".join(f"{q}（{why}）" for q, why in excluded))
    print()

    if dry:
        return

    picked = []
    for _ in range(n):
        if force in ("t1", "t2"):
            bucket = force
        elif force == "any":
            flat = avail["t2"] + avail["t1"]
            if not flat:
                print("❌ 没有可抽的题（全在冷却里）。加 --repeat 忽略冷却。")
                return
            it = random.choice([x for x in flat if x not in picked] or flat)
            picked.append(it)
            continue
        else:
            bucket = random.choices(list(WEIGHTS), weights=list(WEIGHTS.values()))[0]

        cands = [x for x in avail[bucket] if x not in picked] or avail[bucket]
        if not cands:
            print(f"❌ {bucket.upper()} 没有可抽的题（全在冷却里）。加 --repeat 忽略冷却。")
            return
        picked.append(random.choice(cands))

    with DRAWN.open("a", encoding="utf-8") as f:
        for it in picked:
            f.write(f"{today}\t{it['id']}\n")

    for it in picked:
        print(f"🎲 {it['id']}　{it['title']}　(bank.md:{it['line']})")
        print()
        for ln in it["prompt"].splitlines():
            print(f"    {ln}")
        print()
    print(f"（已写进 {DRAWN.relative_to(ROOT.parent.parent)}）")


if __name__ == "__main__":
    main()
