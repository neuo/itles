#!/usr/bin/env python3
"""只读：把两份全文逐句比对，列出每一处不同。给 ④a vs ④b、或原文 vs ④a 用。

用法  python3 writing-band7/drill/difftext.py a.txt b.txt
为什么存在（2026-08-15）：08-12 那篇的 diff 表 B 只列了 10 行、声称 8 句"未改动"，
而更好版全文里那 8 句全都改了 ⇒ 8 处更好版一条条目都没建。
教练靠肉眼从"我打算讲的点"出发挑行，必然漏。这是纯字符串比对，秒级，不许再用眼睛代替。
★ 它列出的【每一处不同都必须有一个 E 号】；条目数 < 差异句数 = 漏了。
"""
import re, sys, difflib

def sents(p):
    t = re.sub(r'\s+', ' ', open(p, encoding='utf-8').read()).strip()
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+', t) if x.strip()]

a, b = sents(sys.argv[1]), sents(sys.argv[2])
if len(a) != len(b):
    print(f"⚠️ 句数不等：{len(a)} vs {len(b)} —— 先检查是不是漏句/多句")
n = diff = 0
for i, (x, y) in enumerate(zip(a, b), 1):
    n += 1
    if x == y:
        print(f"S{i:<3} 相同")
    else:
        diff += 1
        print(f"S{i:<3} ★不同")
        print(f"     A  {x}")
        print(f"     B  {y}")
        sm = difflib.SequenceMatcher(None, x.split(), y.split())
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != 'equal':
                print(f"       {tag:<8} 「{' '.join(x.split()[i1:i2])}」 → 「{' '.join(y.split()[j1:j2])}」")
print(f"\n共 {n} 句 · **不同 {diff} 句** ⇒ 至少要有 {diff} 个 E 号，少一个就是漏了")
