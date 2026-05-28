#!/usr/bin/env python3
"""verify-p3.py — validate the 6 P3 answers inside a P2 example file.

Parses the '## P3 follow-ups（答案）' section, splits on '**Q' markers,
and checks each answer against the P3 static rules:
  - word count in [45, 65]
  - 0 uncontracted forms
  - 0 banned essay words
  - <= 1 placeholder noun (thing/stuff)

Usage: python3 verify-p3.py <file.md> [<file.md> ...]
Exit 0 if all answers in all files pass; 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ESSAY_FORBIDDEN = [
    "furthermore", "moreover", "nevertheless", "however",
    "significant", "consequently", "thus", "hence",
    "in conclusion", "to summarise", "to summarize", "to conclude",
]
UNCONTRACTED_FORMS = [
    r"\bI would\b", r"\bI will\b", r"\bI have\b", r"\bI am\b",
    r"\bit is\b", r"\bdo not\b", r"\bdoes not\b", r"\bcannot\b",
    r"\bthat is\b", r"\bthere is\b", r"\bwe are\b", r"\bthey are\b",
    r"\bshe is\b", r"\bhe is\b",
]
PLACEHOLDER = [r"\bthings?\b", r"\bstuff\b"]


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w']+\b", text))


def extract_p3_section(text: str) -> str:
    m = re.search(r"^##\s*P3\s*follow-ups.*$", text, flags=re.MULTILINE)
    if not m:
        return ""
    rest = text[m.end():]
    cut = re.search(r"^##\s|^---\s*$", rest, flags=re.MULTILINE)
    return rest[:cut.start()] if cut else rest


def split_answers(section: str) -> list[tuple[str, str]]:
    """Return list of (question_line, answer_text)."""
    parts = re.split(r"^\*\*Q.*?\*\*\s*$", section, flags=re.MULTILINE)
    qlines = re.findall(r"^\*\*Q.*?\*\*\s*$", section, flags=re.MULTILINE)
    answers = [p.strip() for p in parts[1:]]  # parts[0] is preamble
    return list(zip(qlines, answers))


def check_answer(ans: str) -> list[str]:
    problems = []
    wc = count_words(ans)
    if not (45 <= wc <= 65):
        problems.append(f"word-count {wc} not in [45,65]")
    unc = []
    for pat in UNCONTRACTED_FORMS:
        unc.extend(re.findall(pat, ans))
    if unc:
        problems.append(f"uncontracted: {unc}")
    for w in ESSAY_FORBIDDEN:
        if re.search(rf"(?i)\b{re.escape(w)}\b", ans):
            problems.append(f"essay-word '{w}'")
    ph = sum(len(re.findall(p, ans)) for p in PLACEHOLDER)
    if ph > 1:
        problems.append(f"placeholder-nouns {ph} (max 1)")
    return problems


def main() -> int:
    files = sys.argv[1:]
    if not files:
        print("usage: verify-p3.py <file.md> ...", file=sys.stderr)
        return 2
    all_ok = True
    for fp in files:
        text = Path(fp).read_text(encoding="utf-8")
        section = extract_p3_section(text)
        pairs = split_answers(section)
        name = Path(fp).name
        if len(pairs) != 6:
            print(f"FAIL {name}: found {len(pairs)} answers (expected 6)")
            all_ok = False
            continue
        file_ok = True
        details = []
        for i, (_q, ans) in enumerate(pairs, 1):
            probs = check_answer(ans)
            wc = count_words(ans)
            if probs:
                file_ok = False
                details.append(f"  Q{i} ({wc}w): " + "; ".join(probs))
        if file_ok:
            wcs = [count_words(a) for _, a in pairs]
            print(f"OK   {name}: 6/6 pass, words={wcs}")
        else:
            all_ok = False
            print(f"FAIL {name}:")
            print("\n".join(details))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
