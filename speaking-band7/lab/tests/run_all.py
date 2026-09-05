#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次跑完 lab.py 的全部回归测试。跑法：python3 speaking-band7/lab/tests/run_all.py
★ 改过 lab.py 就跑它，全绿才许拿去动真档案（SKILL §0.1）。"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SUITES = ["test_migrate.py", "test_count.py", "test_prompts.py", "test_deliver.py",
          "test_check.py", "test_queue.py", "test_recheck.py"]
tot = {"pass": 0, "fail": 0}
bad = []
for s in SUITES:
    r = subprocess.run([sys.executable, os.path.join(HERE, s)],
                       capture_output=True, text=True)
    tail = [l for l in r.stdout.split("\n") if "通过 " in l and "失败 " in l]
    line = tail[-1] if tail else "(没跑出汇总行)"
    print(f"{'✅' if r.returncode == 0 else '❌'} {s:<20} {line}")
    if r.returncode != 0:
        bad.append(s)
        print("\n".join(l for l in r.stdout.split("\n") if l.strip().startswith("❌")))
        if r.stderr.strip():
            print(r.stderr.strip()[-800:])
    for l in tail:
        import re
        m = re.search(r"通过 (\d+) · 失败 (\d+)", l)
        if m:
            tot["pass"] += int(m.group(1))
            tot["fail"] += int(m.group(2))
print("─" * 60)
print(f"合计 通过 {tot['pass']} · 失败 {tot['fail']}")
sys.exit(1 if bad else 0)
