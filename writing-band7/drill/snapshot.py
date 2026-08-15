# 只读统计：从 profile.md 的 📋 事件台账算连击与快照。不写任何内容文件。
import re,collections
lines=[l for l in open('writing-band7/drill/profile.md',encoding='utf-8').read().splitlines() if l.startswith('📋')]
# 今天组1的结果尚未入台账，手工附加（教练本场判定，逐条来自消息）
today="📋 2026-08-15(D3 学习日)  ✅ E-045 E-049 E-062 E-080 E-112 E-118 E-120 E-125 E-129 E-130  ◎ E-054"
lines.append(today)
ev=collections.defaultdict(list)          # E号 -> [(日期,符号)]
for l in lines:
    date=re.match(r'📋 (\S+)',l).group(1)
    cur=None
    for tok in l.split():
        if tok in ('✅','❌','◎','△','📖'): cur=tok
        elif tok.startswith('E-') and cur: ev[tok].append((date,cur))
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
print("★ 连击为 0（最近一次是 ❌/📖）：", ' '.join(sorted(zero)) or '无')
