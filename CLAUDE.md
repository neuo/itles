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

---

## 目录结构（就两个 subject 目录）

```
ielts/
├── CLAUDE.md            本文件
├── study_hub.md         ⭐ 总入口路由（refresh session 第一站，顶部"当前进度"块）
├── daily_log.md         跨学科每日复盘日志
│
├── speaking-band7/      所有口语
│   ├── 01_my_situation / 02_band7_target / 03_question_types
│   ├── 04_toolkit       工具集（含 §11 P2 实战协议=三阶训练+死机3秒清单）
│   ├── 05_path          3 周训练 path（5/30→6/20）
│   ├── personas.md      7 个 persona（54 P2 取材来源）
│   ├── p1_question_bank.md   P1 188 题
│   ├── examples/        54 P2 + 324 P3 范文
│   ├── coach/           状态文件：error_log / inventory / sessions/
│   └── _archive/        旧资料（v5/v6/v7 + p2_my_path，仅参考）
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

### 口语练习流程（触发"练口语/练 P1/P2/P3/来一题"→ speaking-coach skill）

P2 走三阶（A Shadow → B 骨架填充 → C Cold），P1/P3 cold-first。详见 `speaking-band7/04_toolkit.md` §11。

每题：① 语法纠错（第三人称 s / 单复数 / 介词 / 时态）② 表达升级（原句小改，不重写）③ 教一个句式（每题最多一个）。
**两个输出都给**：先精修版（原句小改）再范文（Band 7）。书面词给口语替代。

### 写作练习流程（触发"练 T2/T1"→ writing-coach skill）

T2 按 `writing-band7/05_path.md` 当周阶段。错误沉淀进 `writing-band7/log/errors.md`，cold 产出是核心训练。

### 每次练习结束（**强制,流程被打断也要补**）

1. 写 session 文件：口语 `speaking-band7/coach/sessions/YYYY-MM-DD.md` / 写作 `writing-band7/log/sessions/YYYY-MM-DD-*.md`——**加练也要写**，errors.md + daily_log 不能替代
2. 更新对应 error_log / inventory / errors（毕业进度、新模式）
3. 更新 `daily_log.md`（当日复盘）
4. 更新 `study_hub.md` 顶部"当前进度"块（下次进场定位）

---

## 教练纪律（硬规则）

1. **不主动建议收工**——只在 suzy 说累/没时间时停；工作量大≠该停。继续出题/练
2. **进度按 sessions 文件核查**，不从 daily_log 推断
3. **path 验收清单是 hard check**——每周末逐条核对，没达标明确指出不顺延
4. **session 文件必写**（见上，流程被打断也补）
5. **练习节奏**：知识累计多时倾向复习（~70% 复习 + 30% 新），错的反复练到毕业再换
6. 分析不输出长文档给 suzy 看，给简短行动指令
7. 反馈用英文写（阅读本身是练习），概念难才用中文

---

## 版本管理

git 管理。每次结构性变更或练习收尾应 commit。
