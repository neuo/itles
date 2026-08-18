# IELTS 备考项目（口语 + 写作）

> **范围**：本项目只 cover **口语（P1/P2/P3）和写作（T2 为主，T1 维护）**。
> **听力 suzy 自管**——不在教练 scope，不主动询问 / 规划听力（她主动 ping 才介入）。

## 考生情况

- 考试：2026 年 6 月（首考 6/20）+ 7 月（二考），机考 CDI
- 目标：6.5–7
- 学习风格：理科强，逻辑分析好，语言靠重复量积累
- **核心瓶颈 = 输出能力（production gap）**：阅读 7–7.5 / 听懂 > 说出来。被动理解 OK 但主动输出困难——"一输出就死机"

### 输出 gap 的本质（贯穿所有训练）

**不是 knowledge gap，是 retrieval-under-pressure gap。** 她知道表达、懂语法，但压力下检索不出来。证据：cold 写/说完能自标几乎所有 gap（知道好坏）+ 单点低压能产出正确版 + cold 整段时调出骨架句/直翻版。

**三个层面**：
1. **单句组装**：cold production 时态/体态错、结构断裂
2. **多句衔接**：缺连接词和过渡，信息堆砌
3. **整体框架**：缺开头-展开-收尾层次（P2/P3 明显）

**修法核心**：不是"背更多"，是**增加正确版本在压力下的检索成功率** = 多 cold 产出 + 段落/语境复用 + 高脚手架渐进（不直接 cold，P3 除外）。

**跨技能同源发现**：口语"一句话没了"（`…, like [例子]`）= 写作"干巴巴没副词"（`…, making [展开]`）—— 同一根源，cold 时认知带宽只够搭骨架。解药同构：bare claim 后立刻问"能不能再加一层"。

### 为什么偏科：三通路诊断（6/27 suzy 自己想明白，根本框架）

**她的观察**：浅学的日语，听/读/说三项基本平衡；英语却严重偏科——阅读 7-7.5 领先，听/说出奇差，且"花了时间效果不好"。

**诊断（确认正确，是 retrieval-gap 的更深一层）**：偏科不是能力问题，是**学法决定的**。
- **日语**从声音+使用学 → 每个词"音+意+用过"一起编码 → 三项平衡。
- **英语**从眼睛+阅读+考试学 → 每个词存的是"拼写+意思"、**为识别（recognition）服务，和声音、和产出脱钩**。

**三条神经通路，她只修了第一条**：
1. 👁 **看→认**（拼写→意思）：练了十几年，超强（阅读 7.5）。
2. 👂 **听→认**（音→认出词）：几乎没修——存的是拼写不是音 → 听不懂。
3. 💭 **意→调→说**（意思→调取→产出）：几乎没修——只练过被动识别，没练"调取" → 说不出（= retrieval-under-pressure gap 的来源）。

**关键推论（指导所有训练）**：
- **"更多阅读 ≠ 更好口语"**——不同通路。她"白花时间"的真因 = 一直在加固已最强的第 1 条腿，第 2/3 条空着。**别再用"多读/多背词"当口语听力的练法。**
- **不用"忘掉重学"**：庞大阅读词汇是资产（意+拼写已在），**只缺"声音+调取"，在已有基础上补这两样，比从零快**。学法必须换：**每个词/chunk 都要过耳朵、过嘴**（听+说+用），不只"看懂"。
- **cold production + shadow 范文 + chunk 出声滚 = 直接在修第 2/3 条腿**，不是锦上添花。慢，是因为强腿练了十几年、弱腿才几周。
- 🔑 **方法论铁律**：碰到任何英文，问"我是**看懂了**，还是**听过+说过**了？"——只看懂=又喂强腿；**出声才算修弱腿**。所有材料默认 shadow 出声，不默读。

---

## 目录结构（就两个 subject 目录）

```
ielts/
├── CLAUDE.md            本文件
├── study_hub.md         ⭐ 总入口路由（refresh session 第一站，顶部"当前进度"块）
├── daily_log.md         跨学科每日复盘日志
│
├── speaking-band7/      所有口语
│   ├── lab/             ⭐ 当前训练线数据真源（v2，2026-08-18 起）
│   │   ├── problems.md    问题总表（编号·题面·状态·日志）170 条未毕业
│   │   ├── graduated.md   已毕业 83 条（连对 3，不再召回）
│   │   ├── methods.md     方法类 35 条（**不进复习召回**，只当诊断判据）
│   │   ├── redo_queue.md  重答队列 ／ cycles.md 周期与合并记录
│   │   └── sessions/      一天一文件 YYYY-MM-DD.md
│   ├── question_bank.md + coach/pick_question.py + coach/asked.log   抽题（禁自编）
│   ├── 01_my_situation / 02_band7_target / 03_question_types
│   ├── 04_toolkit       工具集（含 §11 P2 实战协议=三阶训练+死机3秒清单）
│   ├── 05_path          3 周训练 path（5/30→6/20，speaking-coach 线用）
│   ├── personas.md      7 个 persona（54 P2 取材来源）
│   ├── examples/        54 P2 + 324 P3 范文
│   ├── coach/           旧状态文件（fluency_lab.md 70 万字 **只读归档，不再写入**）
│   └── _archive/        旧资料（含 skill_v1_fluency_lab_20260818.md，仅参考）
│
├── writing-band7/       所有写作
│   ├── 01-05 + 04_toolkit + _examiner_protocol + proofreading_routine
│   ├── examples/        Band 7 标杆范文（5 题型）
│   ├── log/             状态：sessions/ + errors.md + active_phrases.md（与口语共享 phrase 池）
│   ├── t1/              T1 维护材料（coach/ + methods + guide）
│   └── _archive/        废弃（task2_my_path / docx 等，仅参考）
│
├── plan/_archive/       旧 10 周计划（calendar / master_plan_v3，过时）
├── listening/ practice-app/ third/ 单词听力/   ← suzy 自管，不动
```

---

## 判断"今天做什么"

1. **读 `study_hub.md` 顶部"当前进度"块**——5 行内定位今天在哪（这是 anti-跑偏的核心机制，每次 session 结束必须更新）
2. 不直接抽题——先确认是浸泡日 / 练习日，按 `speaking-band7/05_path.md` + `writing-band7/05_path.md` 的当日 entry 执行
3. 日期分界：以**美东时间中午 12:00** 为界
4. 进度核查**按 sessions 文件**，不能从 daily_log 推断（daily_log 是 partial 记录）

---

## 互动方式

> **学习入口 = `study-coach` skill**（触发"继续学习/今天练什么"）：整合编排——一次 session 同时驱动口语+写作,先报当周**共同准确性焦点**(两科同一个根:-s/attraction/冠词/介词/搭配/副词/衔接) + 配对话题域,再分别调用下面两个子 coach,最后做跨科综合 + 确保两科收尾文件都写。单练一科可直接进对应子 coach。详见 `.claude/skills/study-coach/SKILL.md`。

### ⭐ 口语训练主线（触发"练口语/复习/继续练说/说不出来" → **fluency-lab skill v2**）

**方法唯一真源 ＝ `.claude/skills/fluency-lab/SKILL.md`（v2，2026-08-18 重写；v1 归档在 `speaking-band7/_archive/`）**，
数据真源 ＝ `speaking-band7/lab/`。核心：

```
周期 = 4 个【有行为的】练习日：L1 L2 L3 R(付息日)；休息/没练跳过不占位
学习日  ①复习 D-1＋D-3 被测到的未毕业条目（10 题一组）→ ②回看 D-1 新题四件套（只读）
        → ③新题 1 道（脚本抽，保底做）→ ④收尾核对
付息日  ⓪回看 → a 本周期全量 → b 向前抽样（最久没测的优先）→ c 合并去重 → d 重答 0–X 道
问题 = 她犯的错 ＋ 说得不地道 ＋ 她主动提出的（复习/新题/重答一视同仁）
四档 ✅ ❌ 📖 ◎ ｜ 连对 3 → 毕业 ｜ 每题都给 最小修改版＋更好版＋diff
★★ 顺序写死：先写 session 文件 → 再把反馈发给她
```

### 口语应试线（触发"练 P1/P2/P3/来一题/串模考" → speaking-coach skill）

**speaking-coach skill = 薄壳执行器,方法论唯一真源仍是 `speaking-band7/05_path.md`「🎓 教练执行手册」**（选题/三阶/8 维诊断/scorecard/End-of-Session 全在那;skill 只 load+enforce,不重复内容——5/31 删旧 skill 后的干净重建,单一真源不破）。P2 走三阶（A→B→C，详见 `04_toolkit.md` §11），P1/P3 cold-first。选题从 `speaking-band7/question_bank.md` 真题库,禁自编。

每题：① 语法纠错（第三人称 s / 单复数 / 介词 / 时态）② 表达升级（原句小改，不重写）③ 教一个句式（每题最多一个）。
**两个输出都给**：先精修版（原句小改）再范文（Band 7）。书面词给口语替代。

### 写作练习流程（触发"练 T2/T1"→ writing-coach skill）

T2 按 `writing-band7/05_path.md` 当周阶段。选题从 `writing-band7/question_bank.md`（A 区剑 16-20 真题 / B 区机经）,禁自编。错误沉淀进 `writing-band7/log/errors.md`，cold 产出是核心训练。

### 每次练习结束（**强制,流程被打断也要补**）

1. 写 session 文件：口语 `speaking-band7/lab/sessions/YYYY-MM-DD.md`（应试线仍写 `coach/sessions/`）/ 写作 `writing-band7/log/sessions/YYYY-MM-DD-*.md`——**加练也要写**，errors.md + daily_log 不能替代
   ★ 口语线的顺序是**先写文件再反馈**（不是练完补记）
2. 更新对应状态文件：口语 `lab/problems.md`（日志行＋状态行）/ 写作 errors.md（毕业进度、新模式）
3. 更新 `daily_log.md`（当日复盘）
4. 更新 `study_hub.md` 顶部"当前进度"块（下次进场定位）

---

## 教练纪律（硬规则）

1. **不主动建议收工**——只在 suzy 说累/没时间时停；工作量大≠该停。继续出题/练
2. **进度按 sessions 文件核查**，不从 daily_log 推断
3. **path 验收清单是 hard check**——每周末逐条核对，没达标明确指出不顺延
4. **session 文件必写 + 详细**（见上，流程被打断也补）
5. **练习节奏**：知识累计多时倾向复习（~70% 复习 + 30% 新），错的反复练到毕业再换
6. **简短只对聊天,不对 session 文件**：给 suzy 的**聊天回复**简短(行动指令,不甩长文档)；但 **session 文件必须详细到可复习**(每题 原句→诊断→精修→教的表达)。两者别混。
7. 反馈用英文写（阅读本身是练习），概念难才用中文

---

## 版本管理

git 管理。每次结构性变更或练习收尾应 commit。
