#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_format.py —— problems.md 一次性格式整改（2026-08-29）。

⛔ 只改**格式**，一个判断都不改：
   ① 补上漏闭的代码围栏         ② 历史行符号去粗体
   ③ 无符号的日期行补 `📝`（留痕行）  ④ 「上次 未测过」写成「上次 —」
   ⑤ 按日志重放回写 连对/连错/上次（§3.1 本来就写着"以日志为准、重算状态行"）
   ⑥ #129 的 08-21 ❌ 按条目正文里已写明的改判补上 §4.7 锚点

**可重跑**：对任何一版 problems.md 跑一次都会收敛到同一个结果 ⇒ 合并回主仓前
对她的最新文件再跑一遍即可，不会和她并行 session 的新内容打架。
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lab                                                    # noqa: E402

P = lab.PROBLEMS
REPORT = []


def log(kind, msg):
    REPORT.append((kind, msg))


def fix_fences(lines):
    """条目内围栏数为奇数 ⇒ 在条目最后一个非空行之后补一个闭合围栏。"""
    heads = [i for i, l in enumerate(lines) if lab.RE_ENTRY.match(l)]
    heads.append(len(lines))
    ins = []
    for a, b in zip(heads, heads[1:]):
        if sum(1 for k in range(a, b) if lines[k].lstrip().startswith("```")) % 2:
            n = lab.RE_ENTRY.match(lines[a]).group(1)
            at = max((k for k in range(a, b) if lines[k].strip()), default=b - 1) + 1
            ins.append((at, n))
    for at, n in sorted(ins, reverse=True):
        lines.insert(at, "```")
        log("围栏", f"#{n} 补一个漏闭的 ``` 到 L{at+1}")
    return lines


def fix_rows(lines):
    """符号去粗体 · 无符号日期行补 📝 · #129 的改判锚点。"""
    fence = False
    for i, l in enumerate(lines):
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = lab.RE_HIST.match(l)
        if not m:
            continue
        rest = m.group(2)
        sym, occ, bold = lab.parse_symbol(rest)
        if bold and sym:
            lines[i] = re.sub(r"\*\*(" + re.escape(sym) + r")\*\*", r"\1", l, count=1)
            log("去粗体", f"L{i+1} `**{sym}**` → `{sym}`")
        elif sym is None:
            lines[i] = re.sub(r"^(-\s*20\d\d-\d\d-\d\d\s+)", r"\g<1>📝 ", l, count=1)
            log("补留痕符号", f"L{i+1} 📝 ＋ {rest[:44]}")
    return lines


def fix_129(lines):
    """#129 的 2026-08-21 ❌ —— 条目正文已写明「08-23 撤销、那次改判 ✅」，
    但那一行还是裸的 ❌ ⇒ 按 §4.7 改成 ✅ 并挂锚点。"""
    for i, l in enumerate(lines):
        if l.startswith("- 2026-08-21 ❌ 复习 · `staff at our company **is**"):
            lines[i] = l.replace("- 2026-08-21 ❌ ",
                                 "- 2026-08-21 ✅ ", 1).rstrip() + \
                "　⚠️ **本条已于 2026-08-23 改判为 ✅**（撤销块见下）"
            log("§4.7 改判", f"L{i+1} #129 08-21 ❌ → ✅ ＋ 锚点")
            break
    return lines


def fix_status(lines):
    """按日志重放回写 连对/连错/上次；「未测过」统一成「—」。"""
    io.open(P, "w", encoding="utf-8").write("\n".join(lines))
    for e in lab.parse_file(P, "problems.md"):
        if e.tomb or e.status_lineno is None or e.ok is None:
            continue
        i = e.status_lineno - 1
        raw = lines[i]
        ok, bad = e.recount()
        last = e.last_tested() or "—"
        new = raw
        if (ok, bad) != (e.ok, e.bad):
            new = re.sub(r"连对\s*\d+", f"连对{ok}", new, count=1)
            new = re.sub(r"连错\s*\d+", f"连错{bad}", new, count=1)
            log("重算 streak", f"#{e.num} 连对{e.ok}/连错{e.bad} → 连对{ok}/连错{bad}")
        if re.search(r"上次\s*(20\d\d-\d\d-\d\d|—|未测过)", lab.norm(new)):
            if (e.last or "—") != last:
                new = re.sub(r"(上次\s*)(20\d\d-\d\d-\d\d|—|未测过)",
                             lambda m: m.group(1) + last, new, count=1)
                log("重算 上次", f"#{e.num} {e.last} → {last}")
        elif "未测过" in new:
            new = new.replace("未测过", "上次 —", 1)
            log("上次写法", f"#{e.num} 「未测过」→「上次 —」")
        lines[i] = new
    return lines


def reorder_body(lines):
    """条目内顺序写死：头/状态行 → 历史行（日期升序）→ 备注块。
    ⛔ 只搬动整块、不改一个字；搬完用「行多重集不变」自证没丢内容。"""
    heads = [i for i, l in enumerate(lines) if lab.RE_ENTRY.match(l)]
    heads.append(len(lines))
    out = list(lines[:heads[0]])          # 文件头（条目区之前）原样保留
    for a, b in zip(heads, heads[1:]):
        seg = lines[a:b]
        n = lab.RE_ENTRY.match(lines[a]).group(1)
        # 切块：顶格的 `- ` 起一块，跟随的缩进行/围栏内行归入该块
        head, blocks, cur, fence = [], [], None, False
        for l in seg:
            if l.lstrip().startswith("```"):
                fence = not fence
                (cur if cur is not None else head).append(l)
                continue
            if not fence and re.match(r"^-\s", l):
                cur = [l]
                blocks.append(cur)
                continue
            (cur if cur is not None else head).append(l)
        dated, notes = [], []
        for blk in blocks:
            m = lab.RE_HIST.match(blk[0])
            (dated if m else notes).append((m.group(1) if m else None, blk))
        if not dated:
            out.extend(seg)
            continue
        order = [d for d, _ in dated]
        need = order != sorted(order) or \
            any(blocks.index(blk) > blocks.index(nb)
                for d, blk in dated for _, nb in notes)
        if not need:
            out.extend(seg)
            continue
        dated.sort(key=lambda x: x[0])
        merged = list(head)
        for _, blk in dated + notes:
            merged.extend(blk)
        out.extend(merged)
        log("重排条目体", f"#{n} 历史行按日期升序 ＋ 备注块移到末尾")
    return out


def main():
    src = io.open(P, encoding="utf-8").read()
    lines = src.split("\n")
    lines = fix_fences(lines)
    lines = fix_rows(lines)
    lines = fix_129(lines)
    before_multiset = sorted(l for l in lines if l.strip())
    lines = reorder_body(lines)
    after_multiset = sorted(l for l in lines if l.strip())
    if before_multiset != after_multiset:
        raise SystemExit("⛔ 重排后内容行多重集变了 —— 有内容丢失/重复，已中止")
    lines = fix_status(lines)
    out = "\n".join(lines)
    io.open(P, "w", encoding="utf-8").write(out)

    from collections import Counter
    c = Counter(k for k, _ in REPORT)
    print("═" * 74)
    print(f"fix_format.py · 共 {len(REPORT)} 处格式整改（⛔ 一个判断都没改）")
    print("═" * 74)
    for k, v in c.most_common():
        print(f"  {k:<12s} {v:>3d} 处")
    print("─" * 74)
    for k, m in REPORT:
        print(f"  {k:<12s} {m}")
    print("═" * 74)
    print(f"文件 {len(src.splitlines())} → {len(out.splitlines())} 行")


if __name__ == "__main__":
    main()
