# 只读统计：从 profile.md 的 📋 事件台账算连击与快照。不写任何内容文件。
import re,collections
lines=[l for l in open('writing-band7/drill/profile.md',encoding='utf-8').read().splitlines() if l.startswith('📋')]
# ⛔⛔ 这里【永远不许】硬编"本场结果"注入台账。
#    2026-08-15 为了先看快照，把当天组1硬编成一行临时 today 追加进来；收尾写了真台账行后
#    这段没删 ⇒ 那 10 条被【重复计一遍】，连对数集体虚高一档，08-16 据此误报"10 条毕业"（真实 3 条）。
#    ⇒ 铁律：快照只读 profile.md 的 📋 行。要看本场结果，先把台账行写进文件再跑。
ev=collections.defaultdict(list)          # E号 -> [(日期,符号)]
for l in lines:
    date=re.match(r'📋 (\S+)',l).group(1)
    cur=None
    for tok in l.split():
        if tok in ('✅','❌','◎','△','📖'): cur=tok
        # ★ 用正则抽 E 号，不能用 startswith：'E-015(回潮)' 那样带批注的会变成另一个实体，
        #   同一条的 ❌ 就落到影子键上、真键的连击不清零（2026-08-16 实测 E-015 同时出现在
        #   「连对2」和「连击归零」两张清单里，就是这个 bug）
        elif cur:
            m=re.match(r'(E-\d{3})',tok)
            if m: ev[m.group(1)].append((date,cur))
def streak(h):
    s=0
    for _,sym in h:
        if sym=='✅': s+=1
        elif sym in ('❌','📖'): s=0
        # ◎ △ 跳过，不加不清
    return s
buckets=collections.Counter()
for e,h in ev.items():
    s=streak(h)
    buckets['🎓 已毕业' if s>=3 else f'连对 {s}' if s>0 else '连错/未过'] += 1
print(f"台账行数 {len(lines)}（含本场）· 出现过的条目 {len(ev)} 条")
for k in ['🎓 已毕业','连对 2','连对 1','连错/未过']:
    print(f"  {k:<8} {buckets.get(k,0)} 条")
cand=[e for e,h in ev.items() if streak(h)==2]
print("\n★ 连对 2（再对一次就毕业，全库最该先清）：", ' '.join(sorted(cand)) or '无')
zero=[e for e,h in ev.items() if streak(h)==0]
      # ★ 标签必须说准：streak==0 有两种，别都说成"被清零"（08-16 ◎ 项被误标）
seen_ok=lambda h: any(s=='✅' for _,s in h)
print("★ 连击为 0 · **被清零**（最近一次 ❌/📖）：", ' '.join(sorted(e for e,h in ev.items() if streak(h)==0 and seen_ok(h))) or '无')
print("★ 连击为 0 · **从没 ✅ 过**（只拿过 ◎/△，或首测就错）：", ' '.join(sorted(e for e,h in ev.items() if streak(h)==0 and not seen_ok(h))) or '无')
