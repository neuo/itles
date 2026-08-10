#!/usr/bin/env python3
"""随机抽题器 —— 口语训练唯一合法的出题方式（她 2026-08-05 定）。

为什么要脚本：教练自己挑题会不自觉地挑"好讲的""刚练过的"，
既违反 question_bank.md 禁自编的规矩，也让训练分布失真。
脚本抽 = 教练无从选择，抽到什么练什么。

★ 权重写死在脚本里（她 2026-08-10 定）：
    默认抽一题 → 30% 概率抽 P2，70% 概率抽 P3
    选中大类后，在该类内部【等概率】随机
    —— 权重和随机全部由脚本决定，不许 LLM 参与挑选

用法
    python3 speaking-band7/coach/pick_question.py            按 30/70 权重抽 1 题
    python3 speaking-band7/coach/pick_question.py 3          按权重抽 3 题（每题独立掷骰）
    python3 speaking-band7/coach/pick_question.py p3         强制只抽 P3
    python3 speaking-band7/coach/pick_question.py p2 2       强制抽 2 张 P2 卡
    python3 speaking-band7/coach/pick_question.py p1         强制只抽 P1
    python3 speaking-band7/coach/pick_question.py any        P1+P2+P3 混在一起等概率
    加 --repeat 允许抽到练过的

默认自动排除 asked.log 里已经练过的题；抽中后立刻写进 asked.log。
P2 会连 "You should say" 的四个 bullet 一起输出（那是卡片的一部分）。
"""

import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # speaking-band7/
BANK = ROOT / "question_bank.md"
ASKED = ROOT / "coach" / "asked.log"

# ★ 权重（她 2026-08-10 定）—— 改这里就改了全局出题分布
WEIGHTS = {"p2": 0.30, "p3": 0.70}


def parse_bank():
    """返回 {'p1': [...], 'p2': [...], 'p3': [...]}。
    每项 = (topic, text, lineno, bullets)；bullets 只有 P2 有。"""
    out = {"p1": [], "p2": [], "p3": []}
    section = None          # 'p1' | 'p2p3'
    topic = ""
    in_p3 = False
    in_bullets = False      # 正在收 P2 的 "You should say" 列表
    cur_p2 = None

    for i, raw in enumerate(BANK.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.rstrip()

        if line.startswith("## "):
            section = "p1" if line.startswith("## P1") else (
                "p2p3" if "P2" in line else None)
            in_p3 = in_bullets = False
            cur_p2 = None
            continue

        if line.startswith("### "):
            topic = line[4:].strip()
            in_p3 = in_bullets = False
            cur_p2 = None
            continue

        if section == "p1" and line.startswith("- "):
            out["p1"].append((topic, line[2:].strip(), i, []))

        elif section == "p2p3":
            m = re.match(r"\*\*Cue card\*\*[:：]\s*(.+)", line)
            if m:
                cur_p2 = (topic, m.group(1).strip(), i, [])
                out["p2"].append(cur_p2)
                in_p3 = False
                in_bullets = False
            elif line.startswith("You should say"):
                in_bullets = True
            elif line.startswith("**P3 follow-ups**"):
                in_p3 = True
                in_bullets = False
            elif in_bullets and line.startswith("- ") and cur_p2 is not None:
                cur_p2[3].append(line[2:].strip())
            elif in_p3 and line.startswith("- "):
                out["p3"].append((topic, line[2:].strip(), i, []))
            elif line.startswith("**"):
                in_bullets = False

    return out


def load_asked():
    if not ASKED.exists():
        return set()
    return {ln.split("\t")[-1].strip()
            for ln in ASKED.read_text(encoding="utf-8").splitlines() if ln.strip()}


def draw_kind():
    """按权重掷一次骰子，决定这一题抽 P2 还是 P3。★ 由脚本决定，不由 LLM 决定。"""
    return "p2" if random.random() < WEIGHTS["p2"] else "p3"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    allow_repeat = "--repeat" in sys.argv

    forced, n = None, 1
    for a in args:
        if a.lower() in ("p1", "p2", "p3", "any"):
            forced = a.lower()
        elif a.isdigit():
            n = int(a)

    bank = parse_bank()
    asked = set() if allow_repeat else load_asked()

    def pool_of(kind):
        pool = (bank["p1"] + bank["p2"] + bank["p3"]) if kind == "any" else bank[kind]
        fresh = [q for q in pool if q[1] not in asked]
        if not fresh:
            print(f"⚠️ {kind.upper()} 未练过的已抽完，放开重复\n")
            fresh = pool
        return fresh

    picked = []
    for _ in range(n):
        kind = forced if forced else draw_kind()      # ★ 每题独立掷骰
        cand = [q for q in pool_of(kind) if q not in picked]
        if not cand:
            continue
        picked.append((kind, random.choice(cand)))

    lines = []
    for kind, (topic, text, lineno, bullets) in picked:
        k = kind if kind != "any" else (
            "p1" if (topic, text, lineno, bullets) in bank["p1"] else
            "p2" if (topic, text, lineno, bullets) in bank["p2"] else "p3")
        print(f"[{k.upper()}] {topic}  (question_bank.md:{lineno})")
        print(f"    {text}")
        for b in bullets:
            print(f"      - {b}")
        print()
        lines.append(f"{k}\tquestion_bank.md:{lineno}\t{topic}\t{text}")

    if lines:
        with ASKED.open("a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

    total = {k: len(v) for k, v in bank.items()}
    mode = f"强制 {forced.upper()}" if forced else f"权重 P2 {WEIGHTS['p2']:.0%} / P3 {WEIGHTS['p3']:.0%}"
    print(f"题库 P1={total['p1']} P2={total['p2']} P3={total['p3']}｜"
          f"已练 {len(load_asked())} 道｜{mode}")


if __name__ == "__main__":
    main()
