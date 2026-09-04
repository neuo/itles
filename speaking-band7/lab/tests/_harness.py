#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py 回归测试的公共台子 —— 全部在临时目录的副本上跑，⛔ 一次都不碰真档案。"""
import contextlib, io, os, re, shutil, sys, tempfile
from collections import Counter

LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # = speaking-band7/lab/
sys.path.insert(0, LAB)
import lab                                                          # noqa: E402

PASS, FAIL = [], []


def ck(name, cond, note=""):
    (PASS if cond else FAIL).append(name)
    print(("  ✅ " if cond else "  ❌ ") + name + (("  — " + str(note)) if note and not cond else ""))


def head(t):
    print("\n" + t)


def report(title):
    print("\n" + "═" * 70)
    print(f"{title} · 通过 {len(PASS)} · 失败 {len(FAIL)}")
    for f in FAIL:
        print("  ❌ " + f)
    print("═" * 70)
    return 1 if FAIL else 0


class _ArgsMeta(type):
    """把 lab.py 里 argparse 的**真默认值**全部收集起来当兜底 ——
    ⛔ 不手工列清单：手工列漏一个就炸一次（已踩两次）。"""


def _all_defaults():
    import argparse
    d = {}
    real = argparse.ArgumentParser.add_argument

    def spy(self, *a, **kw):
        act = real(self, *a, **kw)
        if act.dest not in ("help", "==SUPPRESS=="):
            d.setdefault(act.dest, act.default)
        return act
    argparse.ArgumentParser.add_argument = spy
    try:
        lab.build_parser() if hasattr(lab, "build_parser") else _probe_main()
    finally:
        argparse.ArgumentParser.add_argument = real
    return d


def _probe_main():
    """lab.py 没有单独的 build_parser ⇒ 用 --help 触发一次 main() 的建表。"""
    import argparse
    argv, real_exit = sys.argv[:], sys.exit
    sys.argv = ["lab.py", "--help"]
    sys.exit = lambda *a: (_ for _ in ()).throw(SystemExit(0))
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            lab.main()
    except SystemExit:
        pass
    finally:
        sys.argv = argv
        sys.exit = real_exit


_DEFAULTS = _all_defaults()


class Args:
    def __init__(self, **kw):
        for k, v in _DEFAULTS.items():
            setattr(self, k, v)
        for k, v in kw.items():
            setattr(self, k, v)


COPY = ("problems.md", "graduated.md", "methods.md", "redo_queue.md", "drawn.log")


@contextlib.contextmanager
def sandbox(p_text=None, g_text=None, sessions=True):
    d = tempfile.mkdtemp(prefix="lab")
    for f in COPY:
        s = os.path.join(LAB, f)
        if os.path.exists(s):
            shutil.copy(s, os.path.join(d, f))
    if sessions:
        shutil.copytree(os.path.join(LAB, "sessions"), os.path.join(d, "sessions"))
    if p_text is not None:
        open(os.path.join(d, "problems.md"), "w", encoding="utf-8").write(p_text)
    if g_text is not None:
        open(os.path.join(d, "graduated.md"), "w", encoding="utf-8").write(g_text)
    old = {k: getattr(lab, k) for k in
           ("ROOT", "PROBLEMS", "GRADUATED", "METHODS", "REDO", "SESSIONS", "DRAWN")}
    lab.ROOT = d
    lab.PROBLEMS = os.path.join(d, "problems.md")
    lab.GRADUATED = os.path.join(d, "graduated.md")
    lab.METHODS = os.path.join(d, "methods.md")
    lab.REDO = os.path.join(d, "redo_queue.md")
    lab.SESSIONS = os.path.join(d, "sessions")
    lab.DRAWN = os.path.join(d, "drawn.log")
    try:
        yield d
    finally:
        for k, v in old.items():
            setattr(lab, k, v)
        shutil.rmtree(d, ignore_errors=True)


def run(fn, *a, **kw):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            rc = fn(*a, **kw)
        except SystemExit as ex:
            return ("EXIT", ex.code if isinstance(ex.code, int) else 2,
                    buf.getvalue() + str(ex.code if not isinstance(ex.code, int) else ""))
    return ("OK", rc, buf.getvalue())


def read(d, n):
    return open(os.path.join(d, n), encoding="utf-8").read()


def bodies():
    out = {}
    for p in (lab.PROBLEMS, lab.GRADUATED):
        _, bl, _, _ = lab.split_file(p)
        for b in bl:
            out[b.num] = (os.path.basename(p), tuple(b.body))
    return out


def errset():
    ents = lab.load_all()
    nums = {e.num for e in ents}
    return Counter((e.num, lv, re.sub(r"\bL\d+\b", "L*", m))
                   for e in ents for lv, m in lab.check_entry(e, set(), nums))


def _entry_span(lines, num):
    """→ (条目头下标, 下一个条目头下标)。用与 lab 一致的口径（围栏内不认头）。"""
    a = b = None
    fence = False
    for i, l in enumerate(lines):
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence or not lab.RE_ENTRY.match(l):
            continue
        if a is None and int(lab.RE_ENTRY.match(l).group(1)) == num:
            a = i
        elif a is not None:
            b = i
            break
    if a is None:
        raise SystemExit(f"找不到 #{num}")
    return a, (b if b is not None else len(lines))


def set_status(text, num, new_status_line):
    """整块内找状态行（⛔ 不用「头后 5 行」这种脆口径 —— 存量条目里
    历史行排在元信息之前的有的是，见 #1）。"""
    lines = text.split("\n")
    a, b = _entry_span(lines, num)
    for j in range(a + 1, b):
        if lines[j].startswith("状态"):
            lines[j] = new_status_line
            return "\n".join(lines)
    raise SystemExit(f"#{num} 整块里没有状态行")


def status_of(text, num):
    lines = text.split("\n")
    a, b = _entry_span(lines, num)
    for j in range(a + 1, b):
        if lines[j].startswith("状态"):
            return lines[j]
    return None
