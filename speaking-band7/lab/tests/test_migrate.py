#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py migrate 的正向／负向对抗测试。跑法：python3 speaking-band7/lab/tests/test_migrate.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import *          # noqa: F401,F403
from _harness import (ck, head, report, Args, sandbox, run, read, bodies, errset,
                      set_status, status_of, lab, LAB)
from collections import Counter

P0 = open(os.path.join(LAB, "problems.md"), encoding="utf-8").read()
G0 = open(os.path.join(LAB, "graduated.md"), encoding="utf-8").read()

# ══════════════════════════════════════════════════════════════════════
#  夹具：⛔ 不依赖真档案此刻的形状（搬完之后 problems.md 里就没有 🎓 了）——
#  自己造出"两个方向都有活干"的局面：把 K 条 🎓 塞回 problems.md，
#  再把 R 条在 graduated.md 里降级成未毕业。
# ══════════════════════════════════════════════════════════════════════
K_PENDING, N_RELAPSE = 5, 2


def make_pending(k=K_PENDING, r=N_RELAPSE):
    """→ (problems.md 文本, graduated.md 文本, 待搬编号, 回潮编号)"""
    ph, pb, pt, _ = lab.split_file(os.path.join(LAB, "problems.md"))
    gh, gb, gt, _ = lab.split_file(os.path.join(LAB, "graduated.md"))
    # ★★ 先把真档案**此刻**待搬的 🎓 归位（§0.1.6「测试⛔不许依赖真档案的内容」）：
    #   收尾 migrate 之前的白天，problems.md 里本来就躺着当天刚毕业的几条 ⇒
    #   "恰好 k+r 条换了文件"会被这几条撑爆（2026-09-11 实证：4 条当日毕业 ⇒ M1/M5 红）。
    #   夹具要的是"两个方向都有活干"这个**形状**，不是真档案今天的状态。
    def _is_grad(b):
        return any(lab.RE_STATUS.match(l) and "🎓" in l for l in b.body)
    settled = [b for b in pb if _is_grad(b)]          # 当天刚毕业、还没 migrate 的
    relapsed = [b for b in gb if not _is_grad(b)]     # 当天刚回潮、还没 migrate 的
    pb = [b for b in pb if not _is_grad(b)] + relapsed
    gb = sorted([b for b in gb if _is_grad(b)] + settled, key=lambda b: b.num)
    pb = sorted(pb, key=lambda b: b.num)
    assert len(gb) > k + r, "graduated.md 里条目不够造夹具"
    take = gb[:k]                       # 前 k 条搬回 problems.md（仍是 🎓 ⇒ 该被搬走）
    rest = gb[k:]
    for b in take:
        b.trail = [""]
    newpb = sorted(pb + take, key=lambda b: b.num)
    for b in newpb[:-1]:
        b.trail = [""]
    newpb[-1].trail = [""]
    ptext = lab.join_file(ph, newpb, pt)
    # 回潮要造成**真实形态**：追一条 ❌ 日志行，状态行随之重算 ——
    # ⛔ 不能只把状态行改成"连对0 连错1"，那与历史重放对不上，check 会当场报错，
    #    夹具自己带着 ERROR 会把 migrate 的自校口径搅浑（2026-09-04 踩过）。
    relapse = [b.num for b in rest[:r]]
    for b in rest[:r]:
        # ❌ 行要插在 `- 备注` 之前（契约⑤：日期行不许写在备注块之后）
        # ★ 日期必须**晚于这一条已有的全部日志行** —— 写死一个 2026-09-05 会在
        #   "这条今天刚被判定过"时与「上次」对不上（2026-09-11 实证：夹具自带 ERROR）。
        seen = [m.group(1) for l in b.body for m in [lab.RE_HIST.match(l)] if m]
        day = "2026-09-05"
        if seen and max(seen) >= day:
            y, mo, dd = map(int, max(seen).split("-"))
            day = f"{y:04d}-{mo:02d}-{dd + 1:02d}"      # 同月内 +1 天，够用
        at = next((i for i, l in enumerate(b.body) if lab.RE_NOTE.match(l)), len(b.body))
        b.body = b.body[:at] + [f"- {day} ❌ 回潮（测试夹具）",
                                "  夹具造的回潮行，仅用于测试。"] + b.body[at:]
        for i, l in enumerate(b.body):
            if lab.RE_STATUS.match(l):
                # ★ 题型格要保留：v3 四节正文的条目缺题型格 ⇒ check 报 ERROR（§3.1 契约⑫）
                m = lab.RE_ASK.search(l)
                ask = f" ｜ 题型 {m.group(1)}" if m else ""
                b.body[i] = f"状态 连对0 连错1 上次{day} 未毕业{ask}"
                break
    gtext = lab.join_file(gh, rest, gt)
    return ptext, gtext, [b.num for b in take], relapse


PT, GT, PENDING, RELAPSE = make_pending()


def nonblank(t):
    return Counter(l for l in t.split("\n") if l.strip() and l.strip() != "---")


# ══════════════════════════ 正向 ══════════════════════════
head("【M0 正】split_file 无损切块")
with sandbox(p_text=PT, g_text=GT) as d:
    for n in ("problems.md", "graduated.md"):
        h, bl, tr, t = lab.split_file(os.path.join(d, n))
        ck(f"{n} 切开再拼 == 原文", lab.join_file(h, bl, tr) == t)
        ck(f"{n} 每块以条目头开头",
           all(b.body and b.body[0].startswith("### ") for b in bl))
        ck(f"{n} trail 只含空行与 ---",
           all(all(x.strip() in ("", "---") for x in b.trail) for b in bl))
    h, bl, tr, _ = lab.split_file(os.path.join(d, "problems.md"))
    ck("problems.md 的块数 ＝ 条目头数",
       len(bl) == len(re.findall(r"^### \d+", read(d, "problems.md"), re.M)), len(bl))
    ck("trailer 就是「迁移说明」那一节",
       tr and tr[0].startswith("## 迁移说明"), tr[:1])
    ck("graduated.md 的块数 ＝ 条目头数",
       len(lab.split_file(os.path.join(d, "graduated.md"))[1]) ==
       len(re.findall(r"^### \d+", read(d, "graduated.md"), re.M)))

head("【M1 正】双向搬迁：5 条出池 ＋ 2 条回潮")
with sandbox(p_text=PT, g_text=GT) as d:
    p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
    b0, e0 = bodies(), errset()
    snap0 = lab._statesnap(lab.load_all())
    st, rc, out = run(lab.cmd_migrate, Args())
    ck("退出码 0", (st, rc) == ("OK", 0), out[-500:])
    b1, e1 = bodies(), errset()
    ck("条目集合不变", set(b0) == set(b1) and len(b1) == len(b0))
    ck("每条正文逐字节不变", all(b0[k][1] == b1[k][1] for k in b0),
       [k for k in b0 if b0[k][1] != b1[k][1]][:5])
    ck("状态字段快照不变", lab._statesnap(lab.load_all()) == snap0)
    ck("check 无新增报告（抹掉行号）", not (e1 - e0), list((e1 - e0).items())[:4])
    ck("消掉的只能是「回潮该搬回」这一类（migrate 的本职）",
       all("必须搬回" in m or "却不是 🎓" in m for _, _, m in (e0 - e1)),
       list((e0 - e1).items())[:4])
    mv = {k for k in b0 if b0[k][0] != b1[k][0]}
    ck(f"恰好 {len(PENDING)+len(RELAPSE)} 条换了文件", len(mv) == len(PENDING) + len(RELAPSE), sorted(mv))
    ck("待搬的 🎓 都进了 graduated.md",
       all(b1[n][0] == "graduated.md" for n in PENDING), PENDING)
    ck("回潮的都回了 problems.md",
       all(b1[n][0] == "problems.md" for n in RELAPSE), RELAPSE)
    ents = lab.load_all()
    ck("🎓 全在 graduated.md · 非🎓 全在 problems.md（墓碑除外）",
       all(e.graduated == (e.src == "graduated.md") for e in ents if not e.tomb))
    p1, g1 = read(d, "problems.md"), read(d, "graduated.md")
    ck("两文件非空非--- 行多重集不变",
       nonblank(p0) + nonblank(g0) == nonblank(p1) + nonblank(g1))
    ck("problems.md 头部一字未动", p1.split("\n### ")[0] == p0.split("\n### ")[0])
    ck("「迁移说明」收尾节仍在 problems.md 且逐字相同",
       p1.split("## 迁移说明")[1] == p0.split("## 迁移说明")[1])
    ck("graduated.md 头部一字未动",
       g1.split("\n### ")[0] == g0.split("\n### ")[0])
    for name, txt in (("problems.md", p1), ("graduated.md", g1)):
        ns = [int(m.group(1)) for m in re.finditer(r"^### (\d+)", txt, re.M)]
        ck(f"{name} 编号升序", ns == sorted(ns))
    # ⚠️ ⛔ 不断言"真档案零 ERROR" —— 那测的是**当天档案的健康度**，不是 migrate。
    #    2026-09-05 实证：一次合法的业务操作就能把它打红，
    #    而 §0.1.6「测试全绿才许动 lab.py」于是把脚本一起锁死。
    #    真正该测的性质是：**搬迁不引入新的 ERROR**（多重集只减不增）。
    before = {k: v for k, v in e0.items() if k[1] == "ERROR"}
    after = {k: v for k, v in e1.items() if k[1] == "ERROR"}
    ck("搬迁⛔不引入新 ERROR（多重集只减不增）",
       all(after.get(k, 0) <= before.get(k, 0) for k in after),
       [k for k in after if after[k] > before.get(k, 0)][:4])

    head("【M2 正】幂等 —— 再跑一次 no-op 且逐字节不变")
    st2, rc2, out2 = run(lab.cmd_migrate, Args())
    ck("退出码 0 且报无操作", (st2, rc2) == ("OK", 0) and "无操作" in out2, out2[-200:])
    ck("problems.md 逐字节不变", read(d, "problems.md") == p1)
    ck("graduated.md 逐字节不变", read(d, "graduated.md") == g1)

    head("【M3 正】回程 —— 3 条回潮搬回 problems.md")
    back = sorted(n for n in mv if b1[n][0] == "graduated.md")[:3]
    g2 = read(d, "graduated.md")
    for n in back:
        g2 = set_status(g2, n, "状态 连对0 连错1 上次2026-09-05 未毕业")
    open(lab.GRADUATED, "w", encoding="utf-8").write(g2)
    st3, rc3, out3 = run(lab.cmd_migrate, Args())
    ck("退出码 0", (st3, rc3) == ("OK", 0), out3[-400:])
    b3 = bodies()
    ck(f"{len(back)} 条都回到 problems.md {back}",
       bool(back) and all(b3[n][0] == "problems.md" for n in back), back)
    ck("其余条目正文仍逐字节不变",
       all(b3[k][1] == b1[k][1] for k in b1 if k not in back))
    ck("problems.md 仍升序",
       [int(m.group(1)) for m in re.finditer(r"^### (\d+)", read(d, "problems.md"), re.M)] ==
       sorted(int(m.group(1)) for m in re.finditer(r"^### (\d+)", read(d, "problems.md"), re.M)))

head("【M4 正】墓碑条目一律不动")
with sandbox(p_text=PT, g_text=GT) as d:
    tombs = {e.num for e in lab.load_all() if e.tomb}
    b0 = bodies()
    run(lab.cmd_migrate, Args())
    b1 = bodies()
    ck(f"{len(tombs)} 条墓碑全部留在 problems.md",
       all(b1[n][0] == "problems.md" for n in tombs), sorted(tombs)[:5])

head("【M5 正】--dry-run 不写盘")
with sandbox(p_text=PT, g_text=GT) as d:
    p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
    st, rc, out = run(lab.cmd_migrate, Args(dry_run=True))
    ck("退出码 0", (st, rc) == ("OK", 0))
    ck("两个文件逐字节不变",
       read(d, "problems.md") == p0 and read(d, "graduated.md") == g0)
    ck("打了两个方向的清单",
       f"{len(PENDING)} 条（状态行有 🎓）" in out and f"{len(RELAPSE)} 条" in out, out[:600])

head("【M6 正】搬完其余子命令照常")
with sandbox(p_text=PT, g_text=GT) as d:
    run(lab.cmd_migrate, Args())
    for name, fn, kw in (("stats", lab.cmd_stats, {}),
                         ("check --all", lab.cmd_check, dict(all=True, changed=False)),
                         ("count", lab.cmd_count, dict(type=None)),
                         ("list", lab.cmd_list, {})):
        st, rc, out = run(fn, Args(**kw))
        # ★ check 的 rc 反映的是**档案内容**（夹具拿真 🎓 条目造回潮，回潮后它们的旧题面按 §6② 就该报 ERROR），
        #   ⛔ 不是 migrate 的对错 ⇒ 这里只验"正常跑完、打出汇总行"；migrate 自己的自校由 M1–M5 验
        ok_rc = rc in (0, 1) and "ERROR " in out if name == "check --all" else rc in (0, None)
        ck(f"{name} 跑得动", st == "OK" and ok_rc and len(out) > 50, (st, rc, out[:120]))
    st, rc, out = run(lab.cmd_stats, Args())
    ck("stats 不再报「待她手动搬」", "待她手动搬" not in out, out[:400])

# ══════════════════════════ 负向 ══════════════════════════
head("【N1 负】切块自校失败 ⇒ 拒绝，⛔ 不写盘")
_mid = re.search(r"^### (\d+) · ", PT[len(PT)//2:], re.M).group(0)
_bad = PT.replace(_mid, "## 夹在中间的标题\n\n" + _mid, 1)
with sandbox(p_text=_bad, g_text=GT) as d:
    p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
    st, rc, out = run(lab.cmd_migrate, Args())
    ck("退出（非 0）", st == "EXIT" or rc == 1, (st, rc))
    ck("说清是标题夹在条目中间", "夹在条目中间" in out, out[-300:])
    ck("两个文件都没写", read(d, "problems.md") == p0 and read(d, "graduated.md") == g0)

head("【N2 负】全档重号 ⇒ 拒绝")
_first = re.search(r"^### (\d+) · ", PT, re.M)
_dup = PT[:_first.end()] + PT[_first.end():].replace(re.search(r"^### (\d+) · ", PT[_first.end():], re.M).group(0), _first.group(0), 1)
with sandbox(p_text=_dup, g_text=GT) as d:
    p0 = read(d, "problems.md")
    st, rc, out = run(lab.cmd_migrate, Args())
    ck("退出（非 0）", st == "EXIT" or rc == 1, (st, rc))
    ck("说清是重号", "出现了两次" in out or "重号" in out, out[-300:])
    ck("没写盘", read(d, "problems.md") == p0)

head("【N3 负】自校抓改动 ⇒ 两个文件整批回滚")
for why, poison in (
    ("正文被改", lambda bl: bl[0].body.append("⛔ 偷偷加的一行")),
    ("条目被吞", lambda bl: bl.pop(0)),
):
    with sandbox(p_text=PT, g_text=GT) as d:
        p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
        real = lab.split_file
        calls = {"n": 0}

        def spy(path, _real=real, _poison=poison):
            h, bl, tr, t = _real(path)
            calls["n"] += 1
            if calls["n"] > 2 and os.path.basename(path) == "graduated.md":
                _poison(bl)
            return h, bl, tr, t
        lab.split_file = spy
        try:
            st, rc, out = run(lab.cmd_migrate, Args())
        finally:
            lab.split_file = real
        ck(f"[{why}] 退出码 1", rc == 1, (st, rc, out[-300:]))
        ck(f"[{why}] 报了整批回滚", "整批回滚" in out, out[-300:])
        ck(f"[{why}] problems.md 逐字节复原", read(d, "problems.md") == p0)
        ck(f"[{why}] graduated.md 逐字节复原", read(d, "graduated.md") == g0)

head("【N4 负】状态字段被改 ⇒ 回滚")
with sandbox(p_text=PT, g_text=GT) as d:
    p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
    real_snap = lab._statesnap
    calls = {"n": 0}

    def spy(ents):
        calls["n"] += 1
        s = real_snap(ents)
        if calls["n"] > 1:                       # 第二次（搬完自校）时篡改
            k = sorted(s)[0]
            s[k] = ("动过了",) + s[k][1:]
        return s
    lab._statesnap = spy
    try:
        st, rc, out = run(lab.cmd_migrate, Args())
    finally:
        lab._statesnap = real_snap
    ck("退出码 1", rc == 1, (st, rc))
    ck("报的是状态字段变了", "状态字段变了" in out, out[-300:])
    ck("两个文件都复原",
       read(d, "problems.md") == p0 and read(d, "graduated.md") == g0)

head("【N5 负】check 多出 ERROR ⇒ 回滚")
with sandbox(p_text=PT, g_text=GT) as d:
    p0, g0 = read(d, "problems.md"), read(d, "graduated.md")
    real_err = lab._errmap
    calls = {"n": 0}

    def spy(ents, nums):
        calls["n"] += 1
        c = real_err(ents, nums)
        if calls["n"] > 1:
            c[(999, "ERROR", "凭空多出来的错")] += 1
        return c
    lab._errmap = spy
    try:
        st, rc, out = run(lab.cmd_migrate, Args())
    finally:
        lab._errmap = real_err
    ck("退出码 1", rc == 1, (st, rc))
    ck("报的是多出 check 报告", "多出" in out and "check" in out, out[-300:])
    ck("两个文件都复原",
       read(d, "problems.md") == p0 and read(d, "graduated.md") == g0)

sys.exit(report("lab.py migrate 正/负向测试"))
