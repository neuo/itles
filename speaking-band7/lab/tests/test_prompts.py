#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py prompts（题面逐字核对）的正向／负向对抗测试。

⛔ 全部跑在**自带夹具**上 —— 一个字都不来自真 problems.md／graduated.md／sessions/。

2026-09-05 教训（4 条同时变红，脚本却一行都没错）：
  · P1 拿真 session `sessions/2026-09-04.md` 当对照稿 ⇒ 全档题面粒度整改一动，
    #316 多了一个括号限定，历史 session 里当然没有 ⇒ verify 正确报"点名被吞"⇒ 测试判红。
  · P4 挑"碰巧有句号"的真编号 #315 做 `.replace("。","？")` ⇒ 该条被缩成词组、
    一个句号都没有 ⇒ replace 空操作 ⇒ 稿子与档案一致 ⇒ 负向用例**悄悄失去牙齿**。
本文件验的是 `prompts --verify` 的**逻辑**（档案里有什么，发题稿里就必须逐字有什么），
⛔ 不是某一天档案／session 的内容。所以每一处人为改动都先跑一条**夹具自检**：
先证明"确实改动了比对源里的字符"，再要求 verify 必须抓到。
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, read, lab, LAB

# ══════════════════════════════════════════════════════════════════════════
#  夹具 —— 三条在池 ＋ 一条已毕业，形状照抄真档案的写法，内容全是造的
# ══════════════════════════════════════════════════════════════════════════
A, B, C, G = 9001, 9002, 9003, 9004

QA = ("政府的资金支持很关键。", "政府对小企业的支持还不够。")
PA = "两句都用**名词 support ＋ 介词**说"
QB = ("我登不进去。", "登录页面打不开。")
PB = "两句都用 **log** 这个词说；第一句当**动作**，第二句当**东西**"
QC = ("说到网购这些，我挺挑的。",)
PC = "用 **come** 说"
QG = ("我老家在南方一个小城市，夏天特别热。",)
PG = "用一个 where 从句说"

WANT = {A: (QA, (PA,)), B: (QB, (PB,)), C: (QC, (PC,)), G: (QG, (PG,))}


def _entry(num, title, kind, prompt, status, rows):
    return "\n".join([f"### {num} · {title}",
                      f"类型 {kind} ｜ 题面 {prompt} ｜ 新建 2026-09-01",
                      status] + list(rows)) + "\n\n---\n\n"


def _pt(qs, p):
    """夹具的题面字段 ＝ 真档案的写法：**点名**："句1" ／ "句2"（括号限定）"""
    return "**点名**：" + " ／ ".join(f'"{q}"' for q in qs) + f"（{p}）"


ST_POOL = "状态 连对0 连错1 上次2026-09-01 未毕业"
ST_GRAD = "状态 连对2 连错0 上次2026-09-02 ｜ **🎓 已毕业 2026-09-02**"

P_FIX = ("# 问题总表\n\n---\n\n"
         + _entry(A, "support FROM sb ≠ support FOR sb", "搭配", _pt(QA, PA),
                  ST_POOL, ["- 2026-09-01 ❌ 首犯 · 夹具"])
         + _entry(B, "log in（动词）≠ login（名词）", "词汇", _pt(QB, PB),
                  ST_POOL, ["- 2026-09-01 ❌ 首犯 · 夹具"])
         + _entry(C, "when it comes TO sth", "词组", _pt(QC, PC),
                  ST_POOL, ["- 2026-09-01 ❌ 首犯 · 夹具"]))
G_FIX = ("# 已毕业档\n\n---\n\n"
         + _entry(G, "where 从句修饰地点", "结构", _pt(QG, PG),
                  ST_GRAD, ["- 2026-09-01 ✅ 夹具", "- 2026-09-02 ✅ 夹具"]))


def fix(**kw):
    """夹具沙箱：⛔ 不拷真 sessions/（本命令根本不读 session，拷了只是多一条数据依赖）。"""
    return sandbox(p_text=P_FIX, g_text=G_FIX, sessions=False, **kw)


def draft(d, text, name="draft.md"):
    p = os.path.join(d, name)
    open(p, "w", encoding="utf-8").write(text)
    return p


def ents():
    return {e.num: e for e in lab.load_all()}


def pieces(num):
    return lab.prompt_pieces(ents()[num].prompt)


def compose(nums):
    """★ 当场用**档案解析入口** prompt_pieces 合成一份合法发题稿 ——
    ⛔ 不读任何历史 session（那是会变的生产数据，一改就把测试踩空）。
    这正是 §6 要求教练做的事：发题稿只许从档案原文逐字复制。"""
    E = ents()
    out = []
    for n in nums:
        qs, ps = lab.prompt_pieces(E[n].prompt)
        out.append(f"### [{n}] 第 {n} 题")
        out += [f'   {i+1}. "{q}"' for i, q in enumerate(qs)]
        out += [f"   （{p}）" for p in ps]
        out.append("")
    return "\n".join(out)


head("【P-1 正】夹具自检 —— 解析入口把题面切成了预期的碎片")
with fix() as d:
    E = ents()
    ck(f"四条夹具全部解析出来（{A}/{B}/{C} 在池 · {G} 已毕业）",
       set(WANT) <= set(E) and len(E) == 4, sorted(E))
    for n, (wq, wp) in WANT.items():
        qs, ps = lab.prompt_pieces(E[n].prompt)
        ck(f"#{n} 切出 {len(wq)} 个引号句、{len(wp)} 个括号限定，且逐字相同",
           (tuple(qs), tuple(ps)) == (wq, wp), (qs, ps))

head("【P0 正】打档案原文")
with fix() as d:
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(A), str(B), str(C)]))
    ck("退出码 0", (st, rc) == ("OK", 0), (st, rc))
    for n in (A, B, C):
        ck(f"打出了 #{n} 的元信息整行", f"#{n}" in out and "类型" in out)
    ck("给出了 file:line 供回查", re.search(r"(problems|graduated)\.md:\d+", out) is not None, out[:300])
    ck("提示了下一步必须 --verify", "--verify" in out)
    st, rc, out = run(lab.cmd_prompts, Args(nums=[f"{A},{B}", f" {C} "]))
    ck("编号支持逗号/空格/带#混写", (st, rc) == ("OK", 0) and f"#{C}" in out)

head("【P1 正】当场从档案合成发题稿 ⇒ 全部逐字一致（⛔ 不读真 session）")
with fix() as d:
    body = compose([A, B, C])
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(A), str(B), str(C)], verify=draft(d, body)))
    ck("退出码 0", (st, rc) == ("OK", 0), out[-300:])
    ck("三条全 ✅", out.count("✅ #") == 3, out[-400:])
    ck("结论行说可以发", "可以发" in out)
    rows = re.findall(r"#(\d+)\s+引号句 (\d+)/(\d+) ｜ 括号限定 (\d+)/(\d+)", out)
    ck("三行明细都是 N/N ｜ M/M 全中", len(rows) == 3 and all(a == b and c == e for _, a, b, c, e in rows), rows)

head("【P2 负】少发一句 ⇒ 不许发")
with fix() as d:
    qs, ps = pieces(A)
    body = "\n".join(qs[1:]) + "\n" + "\n".join(f"（{p}）" for p in ps)   # 故意丢掉第 1 句
    ck("夹具自检：丢掉的那一句确实不在稿子里", qs[0] not in body, body[:80])
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(A)], verify=draft(d, body)))
    ck("退出码 1", rc == 1, (st, rc))
    ck("点名了丢掉的那一句", qs[0][:8] in out, out[-400:])
    ck("结论是不许发题", "不许发题" in out)

head("【P3 负】丢掉括号限定（点名被吞）⇒ 不许发")
with fix() as d:
    qs, ps = pieces(C)
    body = "\n".join(qs)                                  # 句子全在，括号没了
    ck("夹具自检：括号限定确实不在稿子里", ps[0] not in body, body[:80])
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(C)], verify=draft(d, body)))
    ck("退出码 1", rc == 1, (st, rc))
    ck("说清是点名被吞", "点名被吞" in out, out[-300:])

head("【P4 负】改比对源里的一个字符 ⇒ 必须抓到（⛔ 不硬绑「。」）")
with fix() as d:
    qs, ps = pieces(A)
    full = ("\n".join(f'"{q}"' for q in qs) + "\n"
            + "\n".join(f"（{p}）" for p in ps) + "\n")
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(A)], verify=draft(d, full, "clean.md")))
    ck("基线：一字未改的稿子放行 ⇒ 后面每一条红都只能来自那一个字符", rc == 0, out[-300:])

    cases = [("句子里改一个字", full.replace(qs[0][:2], "某某", 1), qs[0])]
    # ★ 标点用例：从「第一句里**确实存在**的标点」里挑 —— 2026-09-05 就是硬编码「。」
    #   碰上题面被缩成词组，replace 空操作，负向用例悄悄失效。
    PUN = "。，、；：？！"
    hit = next((c for c in PUN if c in qs[0]), None)
    ck("夹具自检：第一句里有可替换的标点（挑不到 ⇒ 夹具坏了，⛔ 不许当成脚本对）",
       hit is not None, qs[0])
    if hit:
        alt = next(c for c in PUN if c != hit)
        cases.append((f"标点 {hit}→{alt}", full.replace(hit, alt, 1), qs[0]))
    cases.append(("括号限定里改一个字", full.replace(ps[0][:2], "某某", 1), ps[0]))

    for tag, bad, broken in cases:
        ck(f"夹具自检：[{tag}] 确实改动了字符，且比对源被破坏",
           bad != full and broken not in bad, (tag, bad[:100]))
        st, rc, out = run(lab.cmd_prompts, Args(nums=[str(A)], verify=draft(d, bad)))
        ck(f"[{tag}] 被抓到，退出码 1", rc == 1, (tag, st, rc, out[-200:]))

    # ★ 引号**样式**不是比对源（RE_Q 只取引号里的字）—— 把这条隐含契约钉死。
    #   ⛔ 这不是把负向改成正向绕过：上面三条改的都是比对源里的字符，一条都没放过。
    swap = full.replace('"', "“", 1).replace('"', "”", 1)
    ck("夹具自检：引号样式确实被换掉了（句子本身一字未动）",
       swap != full and all(q in swap for q in qs), swap[:60])
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(A)], verify=draft(d, swap)))
    ck("只换引号样式 ⇒ 放行（比对源是引号里的字，不是引号本身）", rc == 0, out[-300:])

head("【P5 负】拿标题当题面现想句子 ⇒ 全不匹配")
with fix() as d:
    e = ents()[A]
    ck("夹具自检：标题里一句题面、一个括号限定都没有",
       all(q not in e.title for q in QA) and PA not in e.title, e.title)
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(A)], verify=draft(d, e.title)))
    ck("退出码 1", rc == 1, (st, rc))
    ck("引号句 0/N", re.search(r"引号句 0/\d", out) is not None, out[-300:])
    ck("括号限定 0/N", re.search(r"括号限定 0/\d", out) is not None, out[-300:])

head("【P6 负】题面待补的条目 ⇒ 直接拦")
# ⚠️ 用**合成档案**造这个条件，⛔ 不再依赖真档案里恰好有没题面的条目 ——
#   2026-09-05 解析器学会读「题面自成一段」的合并条之后，真档案的待补数变成 0，
#   这条测试当场变成假失败（数据依赖的测试早晚会这样）。
P_NOQ = ("# 问题总表\n\n---\n\n### 4242 · 没题面的条目\n"
         "类型 语法 ｜ 旧号 B1\n"
         "状态 连对0 连错1 上次2026-09-02 未毕业\n"
         "- 2026-09-02 ❌ a\n")
with sandbox(p_text=P_NOQ, g_text="# 已毕业档\n", sessions=False) as d:
    todo = [e.num for e in lab.load_all() if not e.prompt and not e.tomb]
    ck("合成档案里有 1 条题面待补", todo == [4242], todo)
    st, rc, out = run(lab.cmd_prompts, Args(nums=["4242"]))
    ck("不带 --verify 时就报题面待补", rc == 1 and "题面待补" in out, out[-300:])
    st, rc, out = run(lab.cmd_prompts, Args(nums=["4242"], verify=draft(d, "随便什么")))
    ck("--verify 时也拦住", rc == 1 and "题面待补" in out, out[-300:])

head("【P6b 正】合并条的题面自成一段 ⇒ 整段读进来，逐字比对每一句")
P_BLK = ("# 问题总表\n\n---\n\n### 4243 · 合并条\n"
         "类型 词组 ｜ **合并条·出题必须整组出**（§3.2c）｜ 新建 2026-09-01\n"
         "题面（2 句，两个成员各一句 —— 只出一句会漏掉另一个）\n"
         "　① \"话说回来，也不是每个人都合适。\"（用 **Then again** 起头）\n"
         "　② \"话虽如此，我还是觉得值得试。\"（用 **That said** 起头）\n"
         "　　★ 她的原话：这一族收进一条\n"
         "状态 连对0 连错1 上次2026-09-02 未毕业 ｜ 合并条·出题多句覆盖\n"
         "- 2026-09-02 ❌ a\n")
with sandbox(p_text=P_BLK, g_text="# 已毕业档\n", sessions=False) as d:
    e = [x for x in lab.load_all() if x.num == 4243][0]
    ck("题面整块被收进 prompt_lines", len(e.prompt_lines) == 4, e.prompt_lines)
    ck("⛔ 不算题面待补", bool(e.prompt))
    ck("★ 比对源只取编号句，⛔ 不含段首说明与 ★ 注释行",
       "只出一句会漏掉" not in e.prompt and "她的原话" not in e.prompt
       and "Then again" in e.prompt and "That said" in e.prompt, e.prompt)
    st, rc, out = run(lab.cmd_prompts, Args(nums=["4243"]))
    ck("prompts 把整段打出来（含 ★ 注释，那是给教练看的）",
       "整段逐字复制" in out and "她的原话" in out, out[-400:])
    full = ('　① "话说回来，也不是每个人都合适。"（用 **Then again** 起头）\n'
            '　② "话虽如此，我还是觉得值得试。"（用 **That said** 起头）\n')
    st, rc, out = run(lab.cmd_prompts, Args(nums=["4243"], verify=draft(d, full)))
    ck("正向：两句都在 ⇒ 放行", rc == 0, out[-400:])
    half = '　① "话说回来，也不是每个人都合适。"（用 **Then again** 起头）\n'
    st, rc, out = run(lab.cmd_prompts, Args(nums=["4243"], verify=draft(d, half)))
    ck("★ 负向：漏掉第 2 句 ⇒ 拦住（合并条「多句覆盖」第一次有机器闸）",
       rc == 1 and "That said" in out, out[-400:])

head("【P7 负】编号不存在 ／ 没给编号 ⇒ 退出")
with fix() as d:
    st, rc, out = run(lab.cmd_prompts, Args(nums=["99999"]))
    ck("不存在的编号被拒", st == "EXIT" and "全档没有这些编号" in out, out[-200:])
    st, rc, out = run(lab.cmd_prompts, Args(nums=[]))
    ck("没给编号被拒", st == "EXIT", (st, rc))
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(A)], verify=os.path.join(d, "没有这个文件.md")))
    ck("发题稿文件不存在被拒", st == "EXIT" and "不存在" in out, out[-200:])

head("【P8 正】已毕业条目也能查、也能 --verify（回看历史题面时要用）")
with fix() as d:
    e = ents()[G]
    ck(f"夹具自检：#{G} 在 graduated.md 且已毕业", e.graduated and e.src == "graduated.md",
       (e.src, e.grad))
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(G)]))
    ck(f"已毕业的 #{G} 查得到题面", rc == 0 and f"#{G}" in out, out[-200:])
    ck("file:line 指向 graduated.md", re.search(r"graduated\.md:\d+", out) is not None, out[:400])
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(G)], verify=draft(d, compose([G]))))
    ck("已毕业条目的发题稿也能逐字核对 ⇒ 放行", rc == 0 and "可以发" in out, out[-300:])

sys.exit(report("lab.py prompts 正/负向测试"))
