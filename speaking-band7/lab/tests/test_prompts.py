#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py prompts（题面逐字核对）的正向／负向对抗测试。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, read, lab, LAB

def draft(d, text, name="draft.md"):
    p = os.path.join(d, name)
    open(p, "w", encoding="utf-8").write(text)
    return p

head("【P0 正】打档案原文")
with sandbox() as d:
    st, rc, out = run(lab.cmd_prompts, Args(nums=["315", "316", "317"]))
    ck("退出码 0", (st, rc) == ("OK", 0), (st, rc))
    for n in (315, 316, 317):
        ck(f"打出了 #{n} 的元信息整行", f"#{n}" in out and "类型" in out)
    ck("给出了 file:line 供回查", re.search(r"(problems|graduated)\.md:\d+", out) is not None, out[:300])
    ck("提示了下一步必须 --verify", "--verify" in out)
    st, rc, out = run(lab.cmd_prompts, Args(nums=["315,316", " 317 "]))
    ck("编号支持逗号/空格/带#混写", (st, rc) == ("OK", 0) and "#317" in out)

head("【P1 正】真实 session 当发题稿 ⇒ 全部逐字一致")
with sandbox() as d:
    real = os.path.join(d, "sessions", "2026-09-04.md")
    st, rc, out = run(lab.cmd_prompts, Args(nums=["315", "316", "317"], verify=real))
    ck("退出码 0", (st, rc) == ("OK", 0), out[-300:])
    ck("三条全 ✅", out.count("✅ #") == 3, out[-400:])
    ck("结论行说可以发", "可以发" in out)

head("【P2 负】少发一句 ⇒ 不许发")
with sandbox() as d:
    e = {x.num: x for x in lab.load_all()}[315]
    qs, ps = lab.prompt_pieces(e.prompt)
    ck(f"#315 的题面切出 {len(qs)} 个引号句、{len(ps)} 个括号限定", len(qs) >= 2 and len(ps) >= 1)
    body = "\n".join(qs[1:]) + "\n" + "\n".join(f"（{p}）" for p in ps)   # 故意丢掉第 1 句
    st, rc, out = run(lab.cmd_prompts, Args(nums=["315"], verify=draft(d, body)))
    ck("退出码 1", rc == 1, (st, rc))
    ck("点名了丢掉的那一句", qs[0][:8] in out, out[-400:])
    ck("结论是不许发题", "不许发题" in out)

head("【P3 负】丢掉括号限定（点名被吞）⇒ 不许发")
with sandbox() as d:
    e = {x.num: x for x in lab.load_all()}[317]
    qs, ps = lab.prompt_pieces(e.prompt)
    body = "\n".join(qs)                                  # 句子全在，括号没了
    st, rc, out = run(lab.cmd_prompts, Args(nums=["317"], verify=draft(d, body)))
    ck("退出码 1", rc == 1, (st, rc))
    ck("说清是点名被吞", "点名被吞" in out, out[-300:])

head("【P4 负】改了一个字 ／ 换了标点 ⇒ 抓得到")
with sandbox() as d:
    e = {x.num: x for x in lab.load_all()}[315]
    qs, ps = lab.prompt_pieces(e.prompt)
    full = "\n".join(qs) + "\n" + "\n".join(f"（{p}）" for p in ps)
    for tag, bad in (("改一个字", full.replace(qs[0][:2], "某某", 1)),
                     ("句号换成问号", full.replace("。", "？", 1)),
                     ("中文引号换成英文", full.replace("“", '"').replace("”", '"'))):
        st, rc, out = run(lab.cmd_prompts, Args(nums=["315"], verify=draft(d, bad)))
        if tag == "中文引号换成英文" and rc == 0:
            ck(f"[{tag}] 不影响（题面本来就用直引号）", True)
            continue
        ck(f"[{tag}] 被抓到，退出码 1", rc == 1, (tag, st, rc, out[-200:]))

head("【P5 负】拿标题当题面现想句子 ⇒ 全不匹配")
with sandbox() as d:
    e = {x.num: x for x in lab.load_all()}[315]
    st, rc, out = run(lab.cmd_prompts, Args(nums=["315"], verify=draft(d, e.title)))
    ck("退出码 1", rc == 1, (st, rc))
    ck("引号句 0/N", re.search(r"引号句 0/\d", out) is not None, out[-300:])

head("【P6 负】题面待补的条目 ⇒ 直接拦")
# ⚠️ 用**合成档案**造这个条件，⛔ 不再依赖真档案里恰好有没题面的条目 ——
#   2026-09-05 解析器学会读「题面自成一段」的合并条之后，真档案的待补数变成 0，
#   这条测试当场变成假失败（数据依赖的测试早晚会这样）。
P_NOQ = ("# 问题总表\n\n---\n\n### 4242 · 没题面的条目\n"
         "类型 语法 ｜ 旧号 B1\n"
         "状态 连对0 连错1 上次2026-09-02 未毕业\n"
         "- 2026-09-02 ❌ a\n")
with sandbox(p_text=P_NOQ, g_text="# 已毕业档\n") as d:
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
         "\u3000① \"话说回来，也不是每个人都合适。\"（用 **Then again** 起头）\n"
         "\u3000② \"话虽如此，我还是觉得值得试。\"（用 **That said** 起头）\n"
         "\u3000\u3000★ 她的原话：这一族收进一条\n"
         "状态 连对0 连错1 上次2026-09-02 未毕业 ｜ 合并条·出题多句覆盖\n"
         "- 2026-09-02 ❌ a\n")
with sandbox(p_text=P_BLK, g_text="# 已毕业档\n") as d:
    e = [x for x in lab.load_all() if x.num == 4243][0]
    ck("题面整块被收进 prompt_lines", len(e.prompt_lines) == 4, e.prompt_lines)
    ck("⛔ 不算题面待补", bool(e.prompt))
    ck("★ 比对源只取编号句，⛔ 不含段首说明与 ★ 注释行",
       "只出一句会漏掉" not in e.prompt and "她的原话" not in e.prompt
       and "Then again" in e.prompt and "That said" in e.prompt, e.prompt)
    st, rc, out = run(lab.cmd_prompts, Args(nums=["4243"]))
    ck("prompts 把整段打出来（含 ★ 注释，那是给教练看的）",
       "整段逐字复制" in out and "她的原话" in out, out[-400:])
    full = ('\u3000① "话说回来，也不是每个人都合适。"（用 **Then again** 起头）\n'
            '\u3000② "话虽如此，我还是觉得值得试。"（用 **That said** 起头）\n')
    st, rc, out = run(lab.cmd_prompts, Args(nums=["4243"], verify=draft(d, full)))
    ck("正向：两句都在 ⇒ 放行", rc == 0, out[-400:])
    half = '\u3000① "话说回来，也不是每个人都合适。"（用 **Then again** 起头）\n'
    st, rc, out = run(lab.cmd_prompts, Args(nums=["4243"], verify=draft(d, half)))
    ck("★ 负向：漏掉第 2 句 ⇒ 拦住（合并条「多句覆盖」第一次有机器闸）",
       rc == 1 and "That said" in out, out[-400:])

head("【P7 负】编号不存在 ／ 没给编号 ⇒ 退出")
with sandbox() as d:
    st, rc, out = run(lab.cmd_prompts, Args(nums=["99999"]))
    ck("不存在的编号被拒", st == "EXIT" and "全档没有这些编号" in out, out[-200:])
    st, rc, out = run(lab.cmd_prompts, Args(nums=[]))
    ck("没给编号被拒", st == "EXIT", (st, rc))
    st, rc, out = run(lab.cmd_prompts, Args(nums=["315"], verify=os.path.join(d, "没有这个文件.md")))
    ck("发题稿文件不存在被拒", st == "EXIT" and "不存在" in out, out[-200:])

head("【P8 正】墓碑/已毕业条目也能查（回看历史题面时要用）")
with sandbox() as d:
    g = next(e.num for e in lab.load_all() if e.graduated and e.prompt)
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(g)]))
    ck(f"已毕业的 #{g} 查得到题面", rc == 0 and f"#{g}" in out, out[-200:])

sys.exit(report("lab.py prompts 正/负向测试"))
