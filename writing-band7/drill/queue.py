#!/usr/bin/env python3
"""只读：生成【本场复习队列】。不写任何内容文件。

用法
  python3 writing-band7/drill/queue.py --scope D-1,D-3 [--done E-045 E-049 ...]
  python3 writing-band7/drill/queue.py --scope all     [--done ...]      # 全库（只在复习日用）

★ --scope 必须显式给，没有默认值 —— 2026-08-15 两次事故都是因为脚本只会报全库，
  而学习日的范围是 D-1 ＋ D-3，两个数差了四倍，报出来就是误导。

批次 = 条目实际产生的那一天（不盖任何章）。D 只数学习日；没写成作文的那天也是学习日。
排序 = 连击归零 → 久没出现 → 连对 2 → E 号升序（不是单纯 E 号升序）。
"""
import re, sys, collections

PROFILE = 'writing-band7/drill/profile.md'

# ── 批次表：改成新的一天时在这里加一行（日期, D编号, E号起, E号止）──
BATCHES = [
    ('2026-08-10', 'D1',   1,  39),
    ('2026-08-11', 'D2',  40,  57),
    ('2026-08-12', 'D3',  58, 117),
    ('2026-08-13', 'D4', 118, 144),
    ('2026-08-12', 'D3', 145, 152),
    ('2026-08-15', 'D5', 153, 182),
    ('2026-08-15', 'D5', 183, 192),   # 08-16 补建：08-15 复习组漏记的 10 条（战报假记录第三例）
]
TODAY_D = 5          # 今天是第几个学习日（改日期时同步改）


def batch_of(e):
    n = int(e[2:])
    for d, dn, lo, hi in BATCHES:
        if lo <= n <= hi:
            return d, dn
    return '（本场新建）', f'D{TODAY_D}'


def parse_scope(arg):
    """把 D-1,D-3 这样的相对标记翻成允许的 D 编号集合。"""
    if arg == 'all':
        return None
    want = set()
    for tok in arg.split(','):
        tok = tok.strip()
        m = re.fullmatch(r'D-(\d+)', tok)
        if m:
            want.add(f'D{TODAY_D - int(m.group(1))}')
        elif re.fullmatch(r'D\d+', tok):
            want.add(tok)
        else:
            sys.exit(f'看不懂的 scope: {tok}（只接受 D-1 / D-3 / D2 / all）')
    return want


def load_rows():
    rows = {}
    for l in open(PROFILE, encoding='utf-8').read().splitlines():
        m = re.match(r'\|\s*(?:\*\*)?(E-\d{3})(?:\*\*)?\s*\|\s*(.*?)\s*\|', l)
        if m:
            rows.setdefault(m.group(1), (m.group(2), l))
    return rows


def testable(trig, line):
    """三类里只有第①类能出中译英。"""
    if any(x in line for x in ('留痕', '⚪ 劝退')) and '待排序' not in line:
        return False, '留痕'
    # ★ 08-16 加：第②类（她的 floor 判不出错）与减法型，中译英测不了
    if '第②类' in line or '不出中译英' in line or '第③类' in line:
        return False, '第②类/第③类（中译英测不出）'
    if trig.strip() in ('—', '-', ''):
        return False, '无题面'
    # 「教练给的更好版」那张表第二列是她的 floor 英文，不是中文题面
    if re.fullmatch(r'[\x00-\x7f\s`*]+', trig):
        return False, '无中文题面（更好版表缺触发点列）'
    return True, ''


def streaks():
    """从 📋 事件台账算每条的连对数与最后出现日。"""
    ev = collections.defaultdict(list)
    for l in open(PROFILE, encoding='utf-8').read().splitlines():
        if not l.startswith('📋'):
            continue
        date = re.match(r'📋 (\S+)', l).group(1)
        cur = None
        for tok in l.split():
            if tok in ('✅', '❌', '◎', '△', '📖'):
                cur = tok
            elif cur:
                # ★ 正则抽号，不用 startswith：'E-015(回潮)' 会被当成另一个实体（08-16 实测 bug）
                m2 = re.match(r'(E-\d{3})', tok)
                if m2:
                    ev[m2.group(1)].append((date, cur))
    out = {}
    for e, h in ev.items():
        s = 0
        for _, sym in h:
            if sym == '✅':
                s += 1
            elif sym in ('❌', '📖'):
                s = 0
        out[e] = (s, len(h))
    return out


def main():
    a = sys.argv[1:]
    if '--scope' not in a:
        sys.exit(__doc__)
    scope = parse_scope(a[a.index('--scope') + 1])
    done = set(x for x in a if x.startswith('E-'))

    rows, st = load_rows(), streaks()
    ok, skipped, excluded = [], collections.Counter(), collections.defaultdict(list)
    for e in sorted(rows):
        trig, line = rows[e]
        d, dn = batch_of(e)
        if scope is not None and dn not in scope:
            continue
        good, why = testable(trig, line)
        if not good:
            skipped[why] += 1; excluded[why].append(e)
            continue
        if e in done:
            skipped['本场已出'] += 1
            continue
        s, seen = st.get(e, (0, 0))
        ok.append((e, dn, d, re.sub(r'（0?8-\d\d.*?）', '', trig)[:40], s, seen))

    # 排序：从没测过的和连击归零的排最前，然后连对少的在前
    ok.sort(key=lambda r: (r[5] > 0, r[4], r[0]))

    label = '全库' if scope is None else '＋'.join(sorted(scope))
    print(f"范围 = {label}（今天 = D{TODAY_D}）· 本场已出 {len(done)} 条")
    print(f"⇒ **本场待出 {len(ok)} 条 = {-(-len(ok)//10)} 组**")

    # ★★ 排除项必须【逐条】列出去处 —— 只报数量就是静默丢弃的出口（她 2026-08-15 抓到）
    if excluded:
        print(f"\n⚠️ 排除 {sum(len(v) for v in excluded.values())} 条，逐条列出（每一条都必须有去处）：")
        DISPOSAL = {
            '留痕': '按设计不出中译英 → **必须挂在本场作文里当场验**；没写作文就写进债行',
            '无题面': '按设计不出中译英 → 同上',
            '无中文题面（更好版表缺触发点列）':
                '🔴 **这不是合法排除，是数据缺陷** —— 条目建的时候漏了中文触发点，'
                '必须当场补写回 profile.md 再出题，不许跳过',
            '本场已出': '本场去重，正常',
            '第②类/第③类（中译英测不出）':
                '第②类＝她的 floor 判不出错 → 走【对比判断题】或整篇产出里验；'
                '第③类＝减法型（"不产出某形式"）→ 挂作文里当场抓。**两者都不许就这么没了**',
        }
        for k, lst in excluded.items():
            print(f"  · {k}（{len(lst)} 条）：{' '.join(lst)}")
            print(f"      去处 → {DISPOSAL.get(k, '未定义 —— 不许排除，先给它一个去处')}")
    print()
    for i in range(0, len(ok), 10):
        print(f"── 第 {i//10+1} 组 ──")
        for e, dn, d, t, s, seen in ok[i:i+10]:
            mark = '🔴归零' if seen and s == 0 else ('·' if seen else '🆕未测')
            print(f"   {e} [{dn} {d}] {mark:<6} 连对{s}  {t}")


if __name__ == '__main__':
    main()
