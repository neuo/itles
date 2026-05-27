#!/usr/bin/env python3
"""
orchestrate.py — Speaking Band 7 答案生成 orchestrator

Workflow（参考 skylark2 harness pattern）:
  generate → static-check → llm-check → human-review → approve|reject

输入：题目 + 类型（p2|p3）
输出：
  - 通过 → 入 examples/<auto-named>.md
  - 不通过 → 反馈 violations + retry counter

用法：
    # 单个生成 + 检查（不走 LLM 生成，只 verify 已写好的答案）
    python orchestrate.py verify --file <answer.md> --type p2

    # 批处理（未来扩展：自动调用 Claude API 生成 + verify）
    python orchestrate.py batch --question-bank <path> --type p2 --limit 5

设计原则（来自 skylark2 harness）:
  - Each rule = independent facet with check() interface
  - Static + LLM 联合（脚本秒级 + LLM 语义）
  - 输出 JSON 可被下游 consume
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

TOOLS_DIR = Path(__file__).resolve().parent
STATIC_CHECKER = TOOLS_DIR / "check-static.py"


def run_static_check(answer_file: Path, answer_type: str) -> dict:
    """Run static checker subprocess."""
    proc = subprocess.run(
        [sys.executable, str(STATIC_CHECKER), "--file", str(answer_file), "--type", answer_type],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        return {
            "phase": "error",
            "layer": "static",
            "message": f"static check output not parseable: {exc}",
            "raw_stdout": proc.stdout,
            "raw_stderr": proc.stderr,
        }
    result["layer"] = "static"
    result["exit_code"] = proc.returncode
    return result


def run_llm_check_stub(answer_file: Path, answer_type: str, cue_card: str = "") -> dict:
    """
    LLM check stub — actual implementation requires Claude API integration.
    For now, returns a placeholder. Future: invoke subagent via SDK.

    Implementation note:
    - Load tools/check-llm.md as system prompt
    - Send answer text + cue card as user message
    - Parse JSON response per schema in check-llm.md
    """
    return {
        "phase": "stub",
        "layer": "llm",
        "message": "LLM check requires manual subagent invocation; see tools/check-llm.md",
        "instructions": [
            "1. Load tools/check-llm.md as Claude subagent system prompt",
            "2. Pass cue card + answer text as user message",
            "3. Parse response JSON per schema in check-llm.md",
        ],
        "answer_file": str(answer_file),
        "answer_type": answer_type,
        "cue_card": cue_card,
    }


def verify(answer_file: Path, answer_type: str, cue_card: str = "") -> dict:
    """Single-answer verification: static + llm checks."""
    if not answer_file.exists():
        return {"phase": "error", "message": f"answer file not found: {answer_file}"}

    static_result = run_static_check(answer_file, answer_type)
    llm_result = run_llm_check_stub(answer_file, answer_type, cue_card)

    static_valid = static_result.get("valid", False) if static_result.get("layer") == "static" else False
    llm_valid = True  # stub passes; real impl will set based on hard fails

    overall = {
        "phase": "done",
        "answer_file": str(answer_file),
        "answer_type": answer_type,
        "cue_card": cue_card,
        "static": static_result,
        "llm": llm_result,
        "decision": "approve" if (static_valid and llm_valid) else "revise",
    }
    return overall


def batch_stub(question_bank: Path, answer_type: str, limit: int) -> dict:
    """Batch generation stub. Future: iterate questions, call LLM gen, verify each."""
    return {
        "phase": "stub",
        "message": "Batch mode requires LLM generation integration",
        "next_steps": [
            "1. Parse question-bank-raw.md to extract individual cue cards",
            "2. For each cue card, call Claude API with persona + toolkit context",
            "3. Run verify() on generated answer",
            "4. If approve → write to examples/; if revise → log + retry up to N times",
        ],
        "question_bank": str(question_bank),
        "answer_type": answer_type,
        "limit": limit,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Speaking Band 7 orchestrator")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_verify = sub.add_parser("verify", help="Verify a single answer file")
    p_verify.add_argument("--file", "-f", required=True, type=Path)
    p_verify.add_argument("--type", "-t", required=True, choices=["p2", "p3"])
    p_verify.add_argument("--cue-card", "-c", default="", help="Cue card text (for LLM context)")

    p_batch = sub.add_parser("batch", help="Batch generate (stub)")
    p_batch.add_argument("--question-bank", "-q", required=True, type=Path)
    p_batch.add_argument("--type", "-t", required=True, choices=["p2", "p3"])
    p_batch.add_argument("--limit", "-l", type=int, default=5)

    args = parser.parse_args()

    if args.cmd == "verify":
        result = verify(args.file, args.type, args.cue_card)
    elif args.cmd == "batch":
        result = batch_stub(args.question_bank, args.type, args.limit)
    else:
        parser.error(f"unknown command: {args.cmd}")
        return 2

    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get("decision") == "revise":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
