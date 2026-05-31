# T2 Band 7 学习路径（suzy 专属）

> **目标**：2026 年 6 月 / 7 月雅思 CDI 机考 T2 得分 6.5-7。
>
> **方法**：从零规划，不受现有材料（docx / task2_band7_examples.md 等）影响。一切以本目录为准。
>
> **建立日期**：2026-05-17

---

## 这份材料的不同之处

旧材料（`writing/` 根目录的 task2_*.md 系列、docx 等）的核心问题：
1. **多个文件互相引用**，导致"单点源"原则崩塌（A 文档说 X，B 文档说 Y，不一致时不知信哪个）
2. **docx 是冲满分写的**（Band 8.5-9），跟 6.5-7 目标错配
3. **task2_band7_examples.md 是降级版**，质量不稳，需要逐篇审计修复
4. **DBV Intro 等具体写法**，docx 模板和 Band 7 评分细则之间有矛盾，旧材料没说清

**这份材料的设计原则**：
- ✅ **本目录是 T2 的唯一权威**——所有 T2 决定查这里
- ✅ 每篇范文都按 Band 7 标准写（不是从 9 降级）
- ✅ 评分细则 + 实操行为之间有明确映射（02_band7_target.md）
- ✅ 工具集严格限量（25 衔接词 + 8 句式 + 5 opener + 20 升级词），不堆砌
- ✅ 5 个题型骨架建立在 Band 7 自身要求上，不混 docx 不一致的版本

---

## 文件地图（按阅读顺序）

| # | 文件 | 角色 | 多长 |
|---|------|------|------|
| 0 | **README.md**（本文件）| 入口 + 导航 | 短 |
| 1 | **01_my_situation.md** | 我的现状 + 学习风格 + Gap 诊断 | 中 |
| 2 | **02_band7_target.md** | Band 7 评分细则拆解 + 自查清单 | 长 |
| 3 | **03_question_types.md** | 5 种题型骨架 + T 句模板 + 高频陷阱 | 长 |
| 4 | **04_toolkit.md** | 限量工具集（衔接 + 句式 + opener + 词汇 + 复杂句）| 长 |
| 5 | **05_path.md** | 5 周训练路径（5/17 → 6 月考）| 中 |

### 范文（按训练周次顺序）

| # | 文件 | 题型 | 训练周 |
|---|------|------|--------|
| 01 | **examples/01_education_dbv.md** | DBV | W1 |
| 02 | **examples/02_technology_ad.md** | A/D | W2 |
| 03 | **examples/03_health_ps.md** | P/S | W2 |
| 04 | **examples/04_environment_ce.md** | C/E | W3 |
| 05 | **examples/05_society_2pt.md** | 2-Pt | W3 |

### 进度跟踪

```
log/
├── sessions/             ← 每次训练详细记录（YYYY-MM-DD.md）
│   └── ...              （suzy + Claude 共同填写）
└── errors.md            ← 错误模式追踪（重复出现的 bug，必修）
```

---

## 怎么开始

### 第一次打开（今天 2026-05-17）

按顺序读 5 个框架文档：
1. `01_my_situation.md`（先确认这个画像准不准——不准告诉我修）
2. `02_band7_target.md`（建立标准认知）
3. `03_question_types.md`（5 题型骨架）
4. `04_toolkit.md`（工具集）
5. `05_path.md`（看本周该做什么）

然后照 `05_path.md` W1 的日历执行。

### 训练时（每天）

1. 看 `05_path.md`，找到今天对应的任务
2. 执行任务
3. 完成后记录到 `log/sessions/YYYY-MM-DD.md`
4. 发现错误 → 录入 `log/errors.md`

### 周日复盘

按 `05_path.md` 末尾的"周复盘格式"做。

---

## 状态

| 文档 | 状态 |
|------|------|
| 00_README.md | ✅ |
| 01_my_situation.md | ✅ |
| 02_band7_target.md | ✅ |
| 03_question_types.md | ✅ |
| 04_toolkit.md | ✅ |
| 05_path.md | ✅ |
| examples/01_education_dbv.md | ✅ 已写（gold standard 标杆范文）|
| examples/02_technology_ad.md | ⏳ 写作 agent 后台生成中 |
| examples/03_health_ps.md | ⏳ 同上 |
| examples/04_environment_ce.md | ⏳ 同上 |
| examples/05_society_2pt.md | ⏳ 同上 |
| log/sessions/ | 📁 空目录，按日期建文件 |
| log/errors.md | ⏳ 第一次训练后建立 |

---

## 和旧材料的关系

| 旧材料 | 新地位 |
|--------|--------|
| `writing-band7/_archive/task2_my_path.md` | **被本目录取代**（不再是 T2 权威）|
| `writing-band7/_archive/task2_band7_examples.md` | **被 examples/ 取代**（旧范文降级有 bug，不再用）|
| `writing-band7/_archive/ielts_task2_guide.docx` | **完全跳过**（冲满分写的，水平错配）|
| `writing-band7/t1/ielts_writing_methods.md` | **T1 部分继续用**（T1 的方法论部分有效）；**T2 部分忽略**（已被本目录取代）|
| `writing-band7/t1/coach/` | **继续用**（T2 错误日志 + sessions 移到 `writing-band7/log/`）|
| `writing/english_check_prompt.md` | **继续用**（独立工具，非 T2 训练 pipeline，保留）|

---

## 给未来的 Claude 看

如果在新对话里被问到 T2 怎么练——**直接看本目录**，不要回去翻 `writing-band7/_archive/task2_*.md` 旧文件。它们已经被取代，留着只是历史归档（怕意外丢失上下文）。

CLAUDE.md 和 writing-coach skill 都会指向本目录。
