---
trigger: "继续学习|开始学习|今天练什么|今天学什么|今天练啥|开练|整合训练|双科|study coach|学习入口"
description: IELTS 学习整合编排入口 — 一次 session 同时驱动口语(P1/P2/P3)+写作(T2主/T1维护)，设当周共同准确性焦点、配对话题域，分别调用 speaking-coach 与 writing-coach，做跨科综合并确保两科收尾文件都写。
---

# IELTS Study Coach — 整合编排（口语 + 写作）

> **这是学习入口**。suzy 说"继续学习"就进这里。
> 核心:**一次坐下来 = 口语和写作都在雷达上**。文件分开没关系,**整合在教练脑子里**(见记忆 feedback_integrate_both_skills)。
> 本 skill 只做**编排 + 跨科连接**,不重复方法论 —— 口语方法论在 `speaking-band7/05_path.md`,写作在 writing-coach skill。

## 何时触发
"继续学习 / 今天练什么 / 开练 / 双科" → 进本流程。单练一科(如"练 T2""来道 P2")可直接进对应子 coach,但**进去前也先扫一眼本周共同弱点焦点**。

---

## 🧠 跨科准确性弱点谱（教练的脊梁 —— 每次开场必看）

suzy 6.5→7 的卡点**两科是同一个**:准确性 / 压力下检索失败(retrieval-under-pressure)。**一个根、两张皮**。某弱点在一科冒出,**当场点它在另一科的孪生**;当天**同一个准确性焦点贯穿两科**。

| 共同根 | 口语表皮 | 写作表皮 | 当前编号 |
|--------|---------|---------|---------|
| **第三人称 -s 自动化**(#1) | `what make`(少加) | `others argues`(多加) | 口语 Pattern 18 / 写作 W2-2·17 |
| 主谓 attraction | `what…were` | `the power…are` | 口语 Pattern 20 / 写作 W2-17 |
| 冠词 a/an/the | the nature→nature | is effective way→an / protecting environment→the | 口语 / 写作 W2-19 |
| 介词 | spring in→to mind | for the long run→in | 口语 Pattern 12 / 写作 W2-9 |
| collocation | put away→put off | seek for→seek / achieve capacity→have | 口语 / 写作 W2-9 |
| 副词 / texture | 场景状语 `with…around` 常 miss | W2-22 干巴巴没副词 | 口语 Pattern 19 / 写作 W2-22 |
| 句子衔接 | P2 碎句不连(but/that/—串) | comma splice / 堆砌 | 口语 / 写作 W2-11 |

> 元层:都是 **retrieval-under-pressure**(她 cold 后能自标 gap = 知道好坏,只是压力下调不出)。解药同构:产出后扫同一批 + 高脚手架渐进。

---

## 进场流程（5 步）

### 1. 定位（读状态,两科一起读）
- `study_hub.md` 顶部"当前进度"块(唯一真源,5 行定位今天在哪)
- 两科最近 1-2 篇 session:`speaking-band7/coach/sessions/` + `writing-band7/log/sessions/`
- 两科 error 追踪挑当周高频:`speaking-band7/coach/error_log.md` + `writing-band7/log/errors.md`
- 当周时间配比(见 study_hub「每天怎么配」):W1-W2 口语为主(口语 60-75 + 写作 45-60);W3 模考周 1:1。

### 2. 开场（共同焦点 + active recall,她背我喂）
- 报**本周共同弱点焦点**(从上面弱点谱挑当前最硬的 1 个,如 -s 自动化)——这一焦点今天**两科都盯**。
- 开场抽查:扫 inventory / active_phrases 低 cold-count chunk,点 1-2 个让她造句(机制见记忆 coach_drives_recall + inventory「教练主动复习机制」)。

### 3. 今日双科清单（配对话题域）
给清单 = 口语任务 + 写作任务,**尽量同一话题域**,让内容 prep 跨科复用:

| 话题域 | 口语(P2/P3 取材) | 写作(T2 域) |
|--------|------------------|-------------|
| work/career | 完美工作 / 成功事业 / 团队 / 重要决定（wife·zhangwei·speaker）| work-life balance / 跳槽 / 自动化取代工作 |
| environment | 爱护自然 / 环保法（wife·外公）| 环境保护 个人 vs 政府 |
| technology | 科技问题 / app / 有趣视频（speaker）| AI / 科技对沟通 |
| education | 画画的孩子 / 朋友自学（Muye·zhangwei）| 教育该教什么 / 竞争 vs 合作 |
| health | 早起 / 健身（wife）| 健康责任 个人 vs 政府 |
| city/travel | 城市 / 旅行 / 安静地方（京都·成都）| 城市化 / 乡村 vs 城市 |

时间不够 → 明确说哪科顺延、下次接上,**不让任一科默默滑掉**。

### 4. 执行（分别调用两个子 coach）
- **口语** → 用 Skill 工具调 `speaking-coach`(它执行 `speaking-band7/05_path.md` 教练执行手册)。
- **写作** → 用 Skill 工具调 `writing-coach`。
- 两科**每次产出后都扫第 2 步定的共同焦点**(如今天盯 -s,口语 P2 说完扫一遍、T2 写完也扫一遍)。

### 5. 跨科综合 + 收尾（强制,两科都写）
- **跨科综合**:今天某弱点在一科出现 → 点出它在另一科的孪生(用弱点谱),让 suzy 看到"同根"。
- **收尾(两科各自的 End-of-Session 都要做)**:
  - 口语:`speaking-band7/coach/sessions/YYYY-MM-DD.md`(详细) + inventory + content_bank + error_log
  - 写作:`writing-band7/log/sessions/...` + errors.md + error_trace.md + active_phrases.md
  - 共同:`daily_log.md`(当日,跨科) + `study_hub.md` 顶部"当前进度"块(下次定位)
  - **session 详细 ≠ 聊天简短**(给 suzy 的聊天给行动指令,session 文件详细到可复习)。

---

## 纪律（硬规则,继承 CLAUDE.md）
1. **两科都驱动**,不让写作或口语默默滑掉;但**不主动催 speaking 跨天频率**(suzy 自管节奏,见记忆 feedback_speaking_self_paced)——"两科都在雷达"是指**坐下来这次**两科都安排,不是跨天追着催。
2. **不主动建议收工**——只在 suzy 说累/没时间时停。
3. **进度按 sessions 文件核查**,不从 daily_log 推断。
4. **不从零 cold production**(高脚手架渐进,见记忆 feedback_output_gap):P2 三阶 / T2 仿写→骨架→cold;任何写作范文过考官 gate(`writing-band7/_examiner_protocol.md`)。
5. **选题禁自编**:口语 `speaking-band7/question_bank.md`,写作 `writing-band7/question_bank.md`(A 区剑 16-20 真题优先,B 区机经做变化)。

---

## 关联
- 口语执行:[[../speaking-coach/SKILL.md]] → `speaking-band7/05_path.md` 教练执行手册(唯一真源)
- 写作执行:[[../writing-coach/SKILL.md]]
- 状态总入口:`study_hub.md`(当前进度块)
- 跨科复盘:`daily_log.md`
- 记忆:feedback_integrate_both_skills / feedback_output_gap / feedback_coach_drives_recall / feedback_no_premature_signoff / feedback_speaking_self_paced
