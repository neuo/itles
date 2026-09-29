#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab.py prompts（题面核对，§6）的正向／负向对抗测试。

她 2026-09-29 定（比照写作线 §6）：同一编号**每次出题都换一个新场景**，⛔ 不再逐字复读档案题面。
--verify 查四件：① 每条有自己的段、有引号句（合并条多句覆盖）② 换场景（不等于／不近似任何已发过的）
③ 形式跟题型走 ④ 提示禁写法。

⛔ 全部跑在**自带夹具**上 —— 档案与"已发过的 session"都是造的，一个字不来自真 problems.md／sessions/。
每一条负向用例都先做**夹具自检**（证明确实造出了要测的状态），再要求 verify 必须抓到。
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _harness import ck, head, report, Args, sandbox, run, read, lab

A, B, C, G = 9001, 9002, 9003, 9004     # A 整句在池 · B 词组在池 · C 合并条 · G 整句已毕业


def _entry(num, title, kind, prompt, status, rows):
    return "\n".join([f"### {num} · {title}",
                      f"类型 {kind} ｜ 题面 {prompt} ｜ 新建 2026-09-01",
                      status] + list(rows)) + "\n\n---\n\n"


ST_POOL = "状态 连对0 连错1 上次2026-09-01 未毕业"
P_FIX = ("# 问题总表\n\n---\n\n"
         + _entry(A, "turn down ＋ 机会", "词组",
                  '"这么好的工作，没人会拒绝。"（"拒绝"用 **turn down** 说）',
                  ST_POOL + " ｜ 题型 整句", ["- 2026-09-01 ❌ 首犯 · 夹具"])
         + _entry(B, "leave a mess", "词组", '"东西乱丢一地"（屋里被弄乱的那种）',
                  ST_POOL + " ｜ 题型 词组", ["- 2026-09-01 ❌ 首犯 · 夹具"])
         + "### 9003 · 不可数名词一族\n类型 词汇 ｜ 新建 2026-09-01\n"
           "题面（2 句，两个成员各一句）\n"
           '　① "一些建议"（给人出主意那种）\n'
           '　② "更多信息"（资料、消息那种）\n'
           + ST_POOL + " ｜ 合并条·出题多句覆盖 ｜ 题型 词组\n- 2026-09-01 ❌ a\n\n---\n\n")
G_FIX = ("# 已毕业档\n\n---\n\n"
         + _entry(G, "where 从句修饰地点", "结构", '"我老家在南方一个小城市，夏天特别热。"（用 **where** 从句说）',
                  "状态 连对2 连错0 上次2026-09-02 ｜ **🎓 已毕业 2026-09-02** ｜ 题型 整句",
                  ["- 2026-09-01 ✅ 夹具", "- 2026-09-02 ✅ 夹具"]))

# 造出来的"已发过"：09-20 发过 A 与 B 的种子；09-25 发过 A 的一个新场景
S20 = ("# 2026-09-20 · L1\n\n## ① 在池组 · 第 1 组（2 题）\n\n```\n"
       '出题 1 · #9001 · "这么好的工作，没人会拒绝。"（"拒绝"用 **turn down** 说）\n'
       '出题 2 · #9002 · "东西乱丢一地"（屋里被弄乱的那种）\n```\n')
S25 = ("# 2026-09-25 · L2\n\n```\n"
       '[1] #9001 · "这么高的薪水，谁都不会推掉。"（"推掉"用 **turn down** 说）\n```\n')
# 今天（09-29）的 session 里已经贴了今天的发题稿 ⇒ ⛔ 不许把它当成"已发过"
S29 = ("# 2026-09-29 · L3\n\n```\n"
       '出题 1 · #9001 · "朋友请我去他公司，我没好意思拒绝。"（"拒绝"用 **turn down** 说）\n```\n')


class fix:
    """夹具沙箱 ＋ 造好的 sessions/（⛔ 不拷真 session）"""
    def __init__(self, sessions=(("2026-09-20", S20), ("2026-09-25", S25), ("2026-09-29", S29))):
        self.sessions = sessions
        self.cm = sandbox(p_text=P_FIX, g_text=G_FIX, sessions=False)

    def __enter__(self):
        d = self.cm.__enter__()
        os.makedirs(os.path.join(d, "sessions"), exist_ok=True)
        for day, text in self.sessions:
            open(os.path.join(d, "sessions", f"{day}.md"), "w", encoding="utf-8").write(text)
        return d

    def __exit__(self, *a):
        return self.cm.__exit__(*a)


def draft(d, text, name="draft.md"):
    p = os.path.join(d, name)
    open(p, "w", encoding="utf-8").write(text)
    return p


def verify(d, text, nums, day="2026-09-29"):
    return run(lab.cmd_prompts, Args(nums=[str(n) for n in nums], verify=draft(d, text), date=day))


GOOD = ('出题 1 · #9001 · "朋友请我去他公司，我没好意思拒绝。"（"拒绝"用 **turn down** 说）\n'
        '出题 2 · #9002 · "孩子吃完饭把桌上弄得一片狼藉"（饭后餐桌上那种乱）\n'
        '出题 3 · #9003（合并条，两句全出）\n'
        '  ① "给我点建议"（给人出主意那种）\n'
        '  ② "网上查到的信息"（资料、消息那种）\n'
        '出题 4 · #9004 · "我长大的那个镇子冬天很冷。"（用 **where** 从句说）\n')

head("【P-1 正】分段：开段行只认一个编号；打包头行不开段、成员各自开段；合并条续行并入")
segs = lab.split_segments(
    '出题 1 · 打包 · #1 #2\n  a #1 "一"（x）\n  b #2 "二二"\n'
    '出题 2 · #3（合并条）\n  ① "三三"\n  ② "四四"\n审核表 #5 "五五"\n[4] #6 · "六六。"\n')
ck("打包头行（两个编号）⛔ 不开段", 1 in segs and 2 in segs and len(segs[1]) == 1, dict(segs))
ck("合并条的 ①② 续行并进 #3 的段", len(segs[3]) == 1 and "三三" in segs[3][0] and "四四" in segs[3][0], segs.get(3))
ck("⛔ 非出题行（审核表）不开段", 5 not in segs, dict(segs))
ck("`[n] #N ·` 逐题记录行照样开段", 6 in segs, dict(segs))

head("【P0 正】不带 --verify：打种子题面 ＋ 已发过的全部题面（只算今天之前的 session）")
with fix() as d:
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(A), str(B)], verify=None, date="2026-09-29"))
    ck("退出码 0", (st, rc) == ("OK", 0), out[-300:])
    ck("打出 #9001 已发过 2 次（09-20 种子 ＋ 09-25 新场景）", "已发过 2 次" in out
       and "2026-09-20" in out and "2026-09-25" in out, out)
    ck("★ 今天 09-29 的 session ⛔ 不算已发过", "没好意思拒绝" not in out, out)
    ck("提示下一步必须 --verify", "--verify" in out)

head("【P1 正】换了场景 · 形式对 · 提示合规 ⇒ 可以发")
with fix() as d:
    st, rc, out = verify(d, GOOD, [A, B, C, G])
    ck("退出码 0", (st, rc) == ("OK", 0), out[-600:])
    ck("四条全 ✅", out.count("✅ #") == 4, out[-600:])
    ck("结论行说可以发", "可以发" in out)
    st, rc, out = verify(d, GOOD.replace('"朋友请我去他公司，我没好意思拒绝。"', '“朋友请我去他公司，我没好意思拒绝。”'), [A])
    ck("中文弯引号同样认", rc == 0, out[-300:])

head("【P2 负】复读：原样再发一次已发过的 ⇒ 不许发")
with fix() as d:
    bad = '出题 1 · #9001 · "这么好的工作，没人会拒绝。"（"拒绝"用 **turn down** 说）\n'
    ck("夹具自检：这一句确实在 09-20 发过", "这么好的工作，没人会拒绝。" in S20)
    st, rc, out = verify(d, bad, [A])
    ck("退出码 1", rc == 1, out[-300:])
    ck("点名「复读」与发过的日期", "复读" in out and "2026-09-20" in out and "一字不差" in out, out[-400:])
    ck("结论是不许发题", "不许发题" in out)

head("【P3 负】近似复读：只改一两个字 ⇒ 照样拦（相似度 ≥ SCENE_SIM）")
with fix() as d:
    bad = '出题 1 · #9001 · "这么好的工作，没有人会拒绝。"（"拒绝"用 **turn down** 说）\n'
    ck("夹具自检：与 09-20 那句不完全相同", "这么好的工作，没有人会拒绝。" not in S20)
    st, rc, out = verify(d, bad, [A])
    ck("退出码 1 且说「只改了几个字」", rc == 1 and "只改了几个字" in out, out[-400:])
    bad2 = '出题 1 · #9001 · "这么高的薪水，谁都不会推掉。"（"推掉"用 **turn down** 说）\n'
    st, rc, out = verify(d, bad2, [A])
    ck("09-25 的新场景再发一次 ⇒ 也是复读（已发过的全部都算，⛔ 不只看种子）",
       rc == 1 and "2026-09-25" in out, out[-400:])

head("【P4 正】从没发过的条目 ⇒ 种子题面可以原样用这一次")
with fix(sessions=()) as d:
    seed = '出题 1 · #9004 · "我老家在南方一个小城市，夏天特别热。"（用 **where** 从句说）\n'
    st, rc, out = verify(d, seed, [G])
    ck("没有任何 session ⇒ 种子放行", rc == 0, out[-400:])
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(G)], verify=None, date="2026-09-29"))
    ck("打印「从没发过」", "从没发过" in out, out[-300:])

head("【P5 负】形式跟题型走：词组题带句号 ／ 整句题不是完整句")
with fix() as d:
    st, rc, out = verify(d, '出题 1 · #9002 · "孩子把桌上弄得一片狼藉。"（饭后餐桌上那种乱）\n', [B])
    ck("词组题带句号 ⇒ 拦", rc == 1 and "带句号" in out, out[-300:])
    st, rc, out = verify(d, '出题 1 · #9001 · "没好意思拒绝朋友"（"拒绝"用 **turn down** 说）\n', [A])
    ck("整句题不是完整句 ⇒ 拦", rc == 1 and "不是完整句" in out, out[-300:])

head("【P6 负】提示禁写法：负向排除／首字母／词数／形态描述／词组题带英文")
with fix() as d:
    cases = [
        (A, '"朋友请我去他公司，我没好意思拒绝。"（"拒绝"用 **turn down** 说 · ⛔ 不许用 refuse）', "负向排除"),
        (A, '"朋友请我去他公司，我没好意思拒绝。"（"拒绝"用 **t** 开头的词组说）', "首字母"),
        (A, '"朋友请我去他公司，我没好意思拒绝。"（"拒绝"用两个词说）', "词数"),
        (A, '"朋友请我去他公司，我没好意思拒绝。"（"拒绝"用一个动词说）', "形态"),
        (B, '"孩子吃完饭把桌上弄得一片狼藉"（用 **mess** 说）', "零英文提示"),
    ]
    for n, body, tag in cases:
        st, rc, out = verify(d, f"出题 1 · #{n} · {body}\n", [n])
        ck(f"#{n} [{tag}] ⇒ 拦", rc == 1 and tag in out, (tag, out[-300:]))

head("【P7 负】合并条少发一个成员 ⇒ 拦（多句覆盖，§3.2c②）")
with fix() as d:
    half = '出题 1 · #9003（合并条）\n  ① "给我点建议"（给人出主意那种）\n'
    st, rc, out = verify(d, half, [C])
    ck("只有 1 句 ⇒ 拦且说出成员数", rc == 1 and "2 个成员" in out and "只有 1 句" in out, out[-300:])

head("【P8 负】发题稿里没有这一条的段 ／ 段里没有引号句 ⇒ 拦")
with fix() as d:
    st, rc, out = verify(d, GOOD, [A, B, C, G])
    ck("基线放行（下面每一条红只能来自那一处改动）", rc == 0, out[-300:])
    st, rc, out = verify(d, GOOD.replace("#9002", "#9999"), [B])
    ck("编号写错 ⇒ #9002 没有段 ⇒ 拦", rc == 1 and "没有这一条的段" in out, out[-300:])
    st, rc, out = verify(d, '出题 1 · #9002 · 孩子把桌上弄乱了\n', [B])
    ck("段里没有引号句 ⇒ 拦", rc == 1 and "没有引号句" in out, out[-300:])

head("【P9 ⚠️】整句题换场景时把档案点名的英文词弄丢了 ⇒ WARN（不拦）")
with fix() as d:
    body = '出题 1 · #9001 · "朋友请我去他公司，我没好意思拒绝。"（"拒绝"说得口语一点）\n'
    st, rc, out = verify(d, body, [A])
    ck("rc 0（只警告）且点名丢了 turn down", rc == 0 and "turn down" in out and "⚠️" in out, out[-400:])

head("【P10 负】题面待补 ／ 编号不存在 ／ 没给编号 ／ 稿子文件不存在")
P_NOQ = ("# 问题总表\n\n---\n\n### 4242 · 没题面的条目\n"
         "类型 语法 ｜ 旧号 B1\n"
         "状态 连对0 连错1 上次2026-09-02 未毕业\n"
         "- 2026-09-02 ❌ a\n")
with sandbox(p_text=P_NOQ, g_text="# 已毕业档\n", sessions=False) as d:
    st, rc, out = run(lab.cmd_prompts, Args(nums=["4242"], verify=None, date="2026-09-29"))
    ck("不带 --verify 时就报题面待补", rc == 1 and "题面待补" in out, out[-300:])
    st, rc, out = verify(d, '出题 1 · #4242 · "随便什么。"\n', [4242])
    ck("--verify 时也拦住", rc == 1 and "题面待补" in out, out[-300:])
with fix() as d:
    st, rc, out = run(lab.cmd_prompts, Args(nums=["99999"], verify=None))
    ck("不存在的编号被拒", st == "EXIT" and "全档没有这些编号" in out, out[-200:])
    st, rc, out = run(lab.cmd_prompts, Args(nums=[], verify=None))
    ck("没给编号被拒", st == "EXIT", (st, rc))
    st, rc, out = run(lab.cmd_prompts, Args(nums=[str(A)], verify=os.path.join(d, "没有这个文件.md")))
    ck("发题稿文件不存在被拒", st == "EXIT" and "不存在" in out, out[-200:])

sys.exit(report("lab.py prompts 正/负向测试"))
