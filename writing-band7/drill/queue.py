# 只读：从 profile.md 生成【本场复习队列】。不写任何内容文件。
# 用法：python3 writing-band7/drill/queue.py [今天已测的E号...]
import re,sys
tested=set(a for a in sys.argv[1:] if a.startswith('E-'))
rows=[]
for l in open('writing-band7/drill/profile.md',encoding='utf-8').read().splitlines():
    m=re.match(r'\|\s*(?:\*\*)?(E-\d{3})(?:\*\*)?\s*\|\s*(.*?)\s*\|',l)
    if not m: continue
    e,trig=m.group(1),m.group(2)
    if any(x in l for x in ('留痕','⚪ 劝退')) and '待排序' not in l: kind='留痕'
    elif trig.strip() in ('—','-','') : kind='无题面'
    else: kind='可测'
    rows.append((e,kind,re.sub(r'（0?8-\d\d.*?）','',trig)[:38]))
seen={}
for e,k,t in rows: seen.setdefault(e,(k,t))       # 同号多行取第一条
ok=[(e,t) for e,(k,t) in sorted(seen.items()) if k=='可测' and e not in tested]
skip=[e for e,(k,t) in sorted(seen.items()) if k!='可测']
print(f"全库 {len(seen)} 号 · 可测 {len([1 for e,(k,_) in seen.items() if k=='可测'])} · 不出题 {len(skip)} · 今天已测 {len(tested)}")
print(f"⇒ 本场待出 {len(ok)} 条 = {-(-len(ok)//10)} 组\n")
for i in range(0,len(ok),10):
    print(f"── 第 {i//10+1} 组 ──")
    for e,t in ok[i:i+10]: print(f"   {e}  {t}")
