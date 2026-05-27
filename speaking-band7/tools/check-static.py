#!/usr/bin/env python3
"""
check-static.py — Speaking Band 7 答案静态规则校验

输入：answer markdown 文件（或 stdin）
输出：JSON {phase: "done", valid, violations: [{rule_id, severity, message}]}
退出码：0 通过 / 1 hard 违规 / 2 加载错

规则来源：tools/content-rules.yaml（layer=static 部分）

用法：
    python check-static.py --file <path> --type p2|p3
    python check-static.py --file <path> --type p2 --persona-config personas.md
    cat answer.md | python check-static.py --type p2

设计：参考 skylark2 harness rule 模式
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# ============================================================
# 规则实现
# ============================================================

ESSAY_FORBIDDEN = [
    "furthermore", "moreover", "nevertheless", "however",
    "significant", "consequently", "thus", "hence",
    "in conclusion", "to summarise", "to summarize", "to conclude",
]

ESSAY_TO_ORAL = {
    "furthermore": "on top of that / plus",
    "moreover": "plus / what's more",
    "however": "but / having said that",
    "nevertheless": "still / even so",
    "significant": "big / important / really key",
    "consequently": "so / as a result",
    "thus": "so",
    "hence": "so",
    "in conclusion": "so yeah / all in all",
}

UNCONTRACTED_FORMS = [
    r"\bI would\b", r"\bI will\b", r"\bI have\b", r"\bI am\b",
    r"\bit is\b", r"\bdo not\b", r"\bdoes not\b", r"\bcannot\b",
    r"\bthat is\b", r"\bthere is\b", r"\bwe are\b", r"\bthey are\b",
    r"\bshe is\b", r"\bhe is\b",
]

ZHANGWEI_SELF_BIO = [
    r"(?i)\b(CS|computer science|programmer|programming|coding|developer|software engineer|software developer|SDE)\b",
    r"(?i)\b(\d+\s+years?\s+(in|of)\s+(tech|IT|software|computer))\b",
    r"(?i)\bfourteen\s+years?\b",
    r"(?i)\b(independent\s+researcher|CSAPP)\b",
    r"(?i)\bmy\s+(career|profession|job)\b.{0,40}(tech|IT|software|programmer|coding)",
]

PLACEHOLDER_NOUNS = [r"\bthings?\b", r"\bstuff\b"]

P2_OPENER_PATTERNS = [
    r"(?i)^\s*(?:So,?\s+|Well,?\s+|OK,?\s+)?(?:the\s+(?:person|place|thing|event|experience|story|day|memory)\s+I'?d\s+like\s+to\s+talk\s+about\s+is)",
    r"(?i)^\s*(?:So,?\s+|Well,?\s+)?(?:the\s+first\s+\w+\s+(?:that\s+|who\s+|which\s+)?came\s+to\s+mind\s+is)",
    r"(?i)^\s*(?:So,?\s+|Well,?\s+)?(?:I'?d\s+like\s+to\s+(?:share|talk\s+about|describe))",
    r"(?i)^\s*(?:So,?\s+|Well,?\s+)?(?:when\s+I\s+saw\s+this\s+card)",
    r"(?i)^\s*(?:So,?\s+|Well,?\s+)?(?:there'?s\s+(?:a|this)\s+\w+.{0,40}(?:I'?ve\s+been\s+wanting|I'?d\s+love))",
]

P2_CLOSER_PATTERNS = [
    r"(?i)\b(?:so\s+yeah|all\s+in\s+all|at\s+the\s+end\s+of\s+the\s+day|that'?s\s+pretty\s+much\s+it)\b",
    r"(?i)\b(?:that'?s\s+the\s+\w+\s+I\s+wanted\s+to\s+talk\s+about)\b",
    r"(?i)\b(?:one\s+of\s+those\s+(?:things|people|moments)\s+I'?ll\s+remember)\b",
]

CONNECTIVE_FUNCTIONS = {
    "start_buffer": [r"(?i)^\s*Well,?", r"(?i)^\s*So,?", r"(?i)^\s*Right,?", r"(?i)^\s*OK,?"],
    "add_point": [r"(?i)\bon\s+top\s+of\s+that\b", r"(?i)\bplus,?", r"(?i)\balso\b", r"(?i)\bwhat'?s\s+more\b"],
    "contrast": [r"(?i)\bbut\b", r"(?i)\bhaving\s+said\s+that\b", r"(?i)\balthough\b", r"(?i)\bthat\s+said\b"],
    "example": [r"(?i)\bfor\s+example\b", r"(?i)\blike\b", r"(?i)\bfor\s+instance\b", r"(?i)\bsuch\s+as\b"],
    "restate": [r"(?i)\bI\s+mean\b", r"(?i)\bwhat\s+I\s+mean\s+is\b", r"(?i)\bbasically\b"],
    "conclude": [r"(?i)\bso\s+yeah\b", r"(?i)\ball\s+in\s+all\b", r"(?i)\bat\s+the\s+end\s+of\s+the\s+day\b"],
}

PRO_TRAP_WORDS = {
    "comfortable": "/ˈkʌmftəbl/ — NOT comf-or-ta-ble",
    "vegetable": "/ˈvedʒtəbl/ — NOT ve-ge-ta-ble",
    "chocolate": "/ˈtʃɒklət/ — NOT cho-co-late",
    "interesting": "/ˈɪntrəstɪŋ/ — NOT in-te-resting",
    "specifically": "/spəˈsɪfɪkli/ — stress on '-sif-'",
    "particularly": "/pəˈtɪkjələli/ — 5 syllables, stress on '-tic-'",
    "regularly": "/ˈreɡjələli/",
}


# ============================================================
# Helpers
# ============================================================

def count_words(text: str) -> int:
    """Tokenize by whitespace; strip markdown markers like [T] [E] [Ex] [L]."""
    text = re.sub(r"\[(T|E\d?|Ex\d?|L)\]", " ", text)
    text = re.sub(r"\*+", "", text)
    text = re.sub(r"#+ ", "", text)
    tokens = re.findall(r"\b[\w']+\b", text)
    return len(tokens)


def violation(rule_id: str, severity: str, message: str) -> dict:
    return {"rule_id": rule_id, "severity": severity, "message": message}


def load_answer(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


# ============================================================
# 各规则 check 函数
# ============================================================

def check_word_count(text: str, answer_type: str) -> list[dict]:
    count = count_words(text)
    if answer_type == "p2":
        lo, hi = 155, 170
    elif answer_type == "p3":
        lo, hi = 45, 65
    else:
        return [violation("word-count", "hard", f"unknown answer-type: {answer_type}")]
    if not (lo <= count <= hi):
        return [violation(f"word-count-{answer_type}", "hard",
                          f"word count {count} not in [{lo}, {hi}]")]
    return []


def check_zhangwei_frequency(text: str) -> list[dict]:
    hits = []
    for pattern in ZHANGWEI_SELF_BIO:
        hits.extend(re.findall(pattern, text))
    if len(hits) > 1:
        return [violation("zhangwei-frequency", "hard",
                          f"self-bio markers found {len(hits)} times (max 1): {hits[:3]}")]
    return []


def check_wife_frequency(text: str) -> list[dict]:
    count = len(re.findall(r"(?i)\bwife\b", text))
    if count < 1:
        return [violation("wife-frequency", "soft",
                          "wife not mentioned (soft warn; OK for non-person/non-event topics)")]
    return []


def check_forbidden_essay_words(text: str) -> list[dict]:
    out = []
    for word in ESSAY_FORBIDDEN:
        if re.search(rf"(?i)\b{re.escape(word)}\b", text):
            suggestion = ESSAY_TO_ORAL.get(word.lower(), "(see toolkit §1)")
            out.append(violation("forbidden-essay-words", "hard",
                                 f"essay word '{word}' detected; use oral alt: {suggestion}"))
    return out


def check_contractions(text: str, answer_type: str) -> list[dict]:
    found = []
    for pattern in UNCONTRACTED_FORMS:
        matches = re.findall(pattern, text)
        if matches:
            found.extend(matches)
    if answer_type == "p2":
        if len(found) > 1:
            return [violation("contractions-required", "hard",
                              f"uncontracted forms detected {len(found)} times (max 1 for P2): {found[:5]}")]
    elif answer_type == "p3":
        if len(found) > 0:
            return [violation("contractions-required", "hard",
                              f"uncontracted forms detected {len(found)} times (max 0 for P3): {found[:5]}")]
    return []


def check_placeholder_nouns(text: str, answer_type: str) -> list[dict]:
    total = 0
    for pattern in PLACEHOLDER_NOUNS:
        total += len(re.findall(pattern, text))
    limit = 2 if answer_type == "p2" else 1
    if total > limit:
        return [violation("placeholder-noun-cap", "hard",
                          f"placeholder nouns (thing/stuff) used {total} times (max {limit})")]
    return []


def check_connectives_coverage(text: str) -> list[dict]:
    """P2 only"""
    functions_hit = set()
    for func, patterns in CONNECTIVE_FUNCTIONS.items():
        for pat in patterns:
            if re.search(pat, text):
                functions_hit.add(func)
                break
    if len(functions_hit) < 4:
        return [violation("connectives-coverage", "soft",
                          f"only {len(functions_hit)} connective functions covered (target ≥ 4): {sorted(functions_hit)}")]
    return []


def check_four_paragraph_structure(text: str) -> list[dict]:
    """P2 only; detect 4 paragraphs"""
    # Heuristic: count double-newline breaks OR [T]/[E]/[Ex]/[L] markers
    paragraphs = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    if len(paragraphs) < 4:
        markers = re.findall(r"\[(T|E\d?|Ex\d?|L)\]", text)
        if len(set(markers)) < 4:
            return [violation("four-paragraph-structure", "hard",
                              f"only {len(paragraphs)} paragraphs detected (target 4); markers found: {set(markers)}")]
    return []


def check_opener(text: str) -> list[dict]:
    """P2 only"""
    # Get first non-empty sentence
    first_para = next((p for p in text.split("\n\n") if p.strip()), "")
    first_sentence = first_para.strip().split("\n")[0].strip()
    # Strip markdown markers
    first_sentence = re.sub(r"\[(T|E\d?|Ex\d?|L)\]\s*", "", first_sentence)
    for pat in P2_OPENER_PATTERNS:
        if re.match(pat, first_sentence):
            return []
    return [violation("opener-required", "hard",
                      f"P2 must start with one of toolkit §2 openers; got: {first_sentence[:80]}")]


def check_closer(text: str) -> list[dict]:
    """P2 only"""
    last_para = [p for p in text.strip().split("\n\n") if p.strip()][-1] if text.strip() else ""
    for pat in P2_CLOSER_PATTERNS:
        if re.search(pat, last_para):
            return []
    return [violation("closer-required", "soft",
                      f"P2 should end with toolkit §4 closer (soft warn)")]


def check_pro_traps(text: str) -> list[dict]:
    out = []
    for word, guide in PRO_TRAP_WORDS.items():
        if re.search(rf"(?i)\b{re.escape(word)}\b", text):
            out.append(violation("pro-pronunciation-traps", "soft",
                                 f"pronunciation trap '{word}': {guide}"))
    return out


# ============================================================
# Main
# ============================================================

def check_all(text: str, answer_type: str) -> dict:
    violations: list[dict] = []

    violations.extend(check_word_count(text, answer_type))
    violations.extend(check_zhangwei_frequency(text))
    violations.extend(check_wife_frequency(text))
    violations.extend(check_forbidden_essay_words(text))
    violations.extend(check_contractions(text, answer_type))
    violations.extend(check_placeholder_nouns(text, answer_type))

    if answer_type == "p2":
        violations.extend(check_connectives_coverage(text))
        violations.extend(check_four_paragraph_structure(text))
        violations.extend(check_opener(text))
        violations.extend(check_closer(text))

    violations.extend(check_pro_traps(text))

    hard_violations = [v for v in violations if v["severity"] == "hard"]
    valid = len(hard_violations) == 0

    return {
        "phase": "done",
        "valid": valid,
        "answer_type": answer_type,
        "word_count": count_words(text),
        "violations": violations,
        "summary": {
            "hard_count": len(hard_violations),
            "soft_count": len(violations) - len(hard_violations),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Speaking Band 7 静态规则校验")
    parser.add_argument("--file", "-f", help="answer markdown file (default: stdin)")
    parser.add_argument("--type", "-t", required=True, choices=["p2", "p3"],
                        help="answer type (p2 or p3)")
    args = parser.parse_args()

    try:
        text = load_answer(args.file)
    except Exception as exc:
        print(json.dumps({"phase": "error", "message": str(exc)}), file=sys.stdout)
        return 2

    result = check_all(text, args.type)
    print(json.dumps(result, ensure_ascii=False, indent=2))

    for v in result["violations"]:
        print(f"violation [{v['severity']}] {v['rule_id']}: {v['message']}", file=sys.stderr)

    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
