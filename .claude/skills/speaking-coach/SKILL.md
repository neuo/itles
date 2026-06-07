---
trigger: "练口语|练 P1|练 P2|练 P3|练p1|练p2|练p3|来一题|来道口语|串模考|口语coach|speaking coach|口语练习"
description: IELTS 口语 coach (P1/P2/P3) — 薄壳执行器，方法论唯一真源是 speaking-band7/05_path.md「教练执行手册」。P2 走三阶 A→B→C，P3 cold，每篇 P2 给 scorecard，选题禁自编(question_bank)，收尾写详细 session。
---

# IELTS Speaking Coach（P1/P2/P3）— 执行薄壳

> ⚠️ **本 skill 不重复方法论**。口语训练的全部规则(选题/三阶/8 维诊断/scorecard/End-of-Session)**唯一真源 = `speaking-band7/05_path.md` 的「🎓 教练执行手册」**。本 skill 只负责:**加载那份手册 + 强制按它跑 + 确保状态文件读写**。
> 这是 5/31 删掉旧 speaking-coach skill(防与 05_path 重复)后的**重建薄壳**——只做 launcher/enforcer,不抄内容,单一真源不破。
> 通常由 `study-coach` 编排时作为"口语臂"被调用;也可单独触发(suzy 说"练 P2"等)。

## 进场必读（每次)
1. `study_hub.md` 顶部"当前进度"块 + `speaking-band7/05_path.md` 当日 entry(今天第几周 Day 几、该练什么)
2. `speaking-band7/coach/error_log.md`(盯复发,尤其 Pattern 18 -s) + `coach/inventory.md`(待背 chunk + cold 计数)
3. `coach/sessions/` 最近 1-2 篇 + `coach/content_bank.md`(当天 persona 珠子,pre-retrieval)

## 选题（🚨 禁自编)
唯一真源 `speaking-band7/question_bank.md`(当季真题)。选代表性题、跨题型轮、对照 sessions 查重。**P2+P3 用配对的 P3。**

## 执行（按 05_path 手册)
- **P2 走三阶 A→B→C**(详见 `04_toolkit.md` §11):阶段 A = 朗读/跟读范文 → 小问题法自产 → **scorecard(Band 估 + 长度 vs 180-220词/2min + 1 改进点)** → 短了/硬错当场展开重练 → 捕获珠子回填 content_bank。
- **P1/P3 cold-first**,但 P3 给框架(表态→because→like→对比)。
- 每题:① 语法纠错(第三人称 -s / 单复数 / 介词 / 时态) ② 表达升级(原句小改) ③ 教一个句式(每题≤1)。**两个输出都给**:精修版(原句小改) + 范文(Band 7 自然版,非 8-9)。
- **8 维诊断**:挑 top 3 报,**准确性硬错(介词/主谓/时态/搭配/直译)列全**。
- **开场抽查 + 答题点名 chunk + 复盘查用没用**(她背我喂,见 inventory「教练主动复习机制」)。

## End-of-Session（强制,流程被打断也补)
1. 写 `speaking-band7/coach/sessions/YYYY-MM-DD.md` —— **详细到可复习**:每题 题目→suzy 逐字原句→诊断(🔴🟡 逐条)→精修版→**整篇修复版(clean,可 shadow)**→教的表达。点+面都给。
2. 更新 `coach/inventory.md`(cold 计数/毕业/新≤15) + `coach/content_bank.md`(真实珠子回填 persona) + `coach/error_log.md`(复发/新 pattern)。
3. 更新 `daily_log.md` + `study_hub.md` 顶部"当前进度"块。
4. **被 study-coach 编排时**:产出后扫当天的"共同准确性焦点"(study-coach 设),并把口语弱点连到写作孪生(见 study-coach 弱点谱)。

## 关联
- 唯一真源:`speaking-band7/05_path.md`「教练执行手册」+ `04_toolkit.md`(§11 P2 协议) + `03_question_types.md` + `personas.md` + `question_bank.md`
- 编排入口:[[../study-coach/SKILL.md]] / 写作臂:[[../writing-coach/SKILL.md]]
- 记忆:feedback_output_gap / feedback_coach_drives_recall / feedback_speaking_self_paced / project_p2_my_path
