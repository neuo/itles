#!/usr/bin/env python3
"""随机抽题器 —— 口语训练唯一合法的出题方式（她 2026-08-05 定）。

为什么要脚本：教练自己挑题会不自觉地挑"好讲的""刚练过的"，
既违反 question_bank.md 禁自编的规矩，也让训练分布失真。
脚本抽 = 教练无从选择，抽到什么练什么。

用法
    python3 speaking-band7/coach/pick_question.py            随机 1 题（任意类型）
    python3 speaking-band7/coach/pick_question.py p3         只抽 P3
    python3 speaking-band7/coach/pick_question.py p1 3       抽 3 道 P1
    python3 speaking-band7/coach/pick_question.py p2         抽 1 张 P2 卡（连 P3 一起给）
    python3 speaking-band7/coach/pick_question.py p3 1 --repeat   允许抽到练过的

默认自动排除 asked.log 里已经练过的题；抽中后立刻写进 asked.log。
"""

import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # speaking-band7/
BANK = ROOT / "question_bank.md"
ASKED = ROOT / "coach" / "asked.log"


def parse_bank():
    """返回 {'p1': [...], 'p2': [...], 'p3': [...]}，每项 (topic, text, lineno)。"""
    out = {"p1": [], "p2": [], "p3": []}
    section = None          # 'p1' | 'p2p3'
    topic = ""
    in_p3 = False

    for i, raw in enumerate(BANK.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.rstrip()

        if line.startswith("## "):
            section = "p1" if line.startswith("## P1") else (
                "p2p3" if "P2" in line else None)
            in_p3 = False
            continue

        if line.startswith("### "):
            topic = line[4:].strip()
            in_p3 = False
            continue

        if section == "p1" and line.startswith("- "):
            out["p1"].append((topic, line[2:].strip(), i))

        elif section == "p2p3":
            m = re.match(r"\*\*Cue card\*\*[:：]\s*(.+)", line)
            if m:
                out["p2"].append((topic, m.group(1).strip(), i))
                in_p3 = False
            elif line.startswith("**P3 follow-ups**"):
                in_p3 = True
            elif in_p3 and line.startswith("- "):
                out["p3"].append((topic, line[2:].strip(), i))
            elif line.startswith("**"):
                in_p3 = False

    return out


def load_asked():
    if not ASKED.exists():
        return set()
    return {ln.split("\t")[-1].strip()
            for ln in ASKED.read_text(encoding="utf-8").splitlines() if ln.strip()}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    allow_repeat = "--repeat" in sys.argv

    kind = args[0].lower() if args else "any"
    n = int(args[1]) if len(args) > 1 else 1

    bank = parse_bank()
    pool = (bank["p1"] + bank["p2"] + bank["p3"]) if kind == "any" else bank.get(kind, [])
    if not pool:
        sys.exit(f"未知类型 {kind}（可用 p1 / p2 / p3 / any）")

    kind_of = {id(x): k for k in ("p1", "p2", "p3") for x in bank[k]}

    asked = set() if allow_repeat else load_asked()
    fresh = [q for q in pool if q[1] not in asked]
    if len(fresh) < n:
        print(f"⚠️ 未练过的只剩 {len(fresh)} 道，已放开重复\n")
        fresh = pool

    picked = random.sample(fresh, n)

    lines = []
    for topic, text, lineno in picked:
        k = kind_of[id((topic, text, lineno))] if False else (
            "p1" if (topic, text, lineno) in bank["p1"] else
            "p2" if (topic, text, lineno) in bank["p2"] else "p3")
        print(f"[{k.upper()}] {topic}  (question_bank.md:{lineno})")
        print(f"    {text}\n")
        lines.append(f"{k}\tquestion_bank.md:{lineno}\t{topic}\t{text}")

    with ASKED.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    total = {k: len(v) for k, v in bank.items()}
    print(f"题库总量 P1={total['p1']} P2={total['p2']} P3={total['p3']}｜"
          f"已练 {len(load_asked())} 道")


if __name__ == "__main__":
    main()
