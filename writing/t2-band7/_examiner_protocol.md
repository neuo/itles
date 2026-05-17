# IELTS T2 Examiner Agent Protocol（校准协议）

> **目的**：防止 Claude 写出的"Band 7"范文不自觉漂移到 Band 8+。每一篇范文/句式/opener 模板都必须通过这个 agent 打分。
>
> **触发条件**：任何 Claude 输出给 suzy 仿写的英文 essay / paragraph / sentence template。
>
> **核心规则**：
> - 目标区间 **Band 6.5 - 7.0**（含两端）
> - **> 7.0 → 必须重写**（lexical de-escalation 或 structural simplification）
> - **< 6.5 → 必须修复**（找出 missing 的 7 级特征）
> - **🌟 禁止用低级失误降分**：不准故意加 grammar error / spelling error / wrong collocation / S-V mismatch / article 漏写。降分**只能**通过：替换 less common collocation 为更常见的、缩短复杂名词短语、用更直白的连接、减少高阶句式密度

---

## 1. Agent 调用模板

dispatch 一个 subagent，prompt 长这样：

```
你是一位资深 IELTS 写作考官，已批改 Task 2 essay 多年。你的标准严格，不放水。

## 任务
给下面这篇 T2 essay 按 4 个官方维度打分（半档精度：5.0 / 5.5 / 6.0 / 6.5 / 7.0 / 7.5 / 8.0），并给出最终 overall band。

## 评分依据
严格按下面的 Band 6 / 7 / 8 official descriptors 判断。

[paste descriptors here — 见 §2]

## 必读规则
- **不放水**。如果在 7.0 和 7.5 之间犹豫，给 7.5（这会触发 rewrite，对学生更负责）
- **不严苛**。如果在 6.5 和 7.0 之间犹豫，给 7.0（学生目标区间）
- 关注 Band 8 markers：cleft / inversion / mixed conditional / reduced relative / passive reporting / 复杂抽象名词链 / 学术高阶 collocation（如 "of considerable debate" / "a paramount importance" / "warrants serious consideration"）/ skilful uncommon vocabulary
- 关注 Band 7 markers：variety of complex structures（不是 wide range）/ frequent error-free（不是 majority）/ less common with some awareness（不是 skilfully uses uncommon）

## Essay
[题目]
[essay text]

## 输出格式（严格遵守）

### Per-dimension scores
- TR: X.X — [一句话理由]
- CC: X.X — [一句话理由]
- LR: X.X — [一句话理由]
- GRA: X.X — [一句话理由]

### Overall band
X.X

### Verdict
- ✅ PASS (6.5-7.0)
- ⚠️ TOO HIGH (> 7.0) — 必须降级
- ❌ TOO LOW (< 6.5) — 必须修复

### If TOO HIGH: 具体的"Band 8 markers"清单
列出 essay 里**每一处**让分数超过 7 的具体短语 / 句式 / 词汇，每条给出：
- 原文（精确引用）
- 为什么这是 Band 8（哪个 descriptor）
- **建议替换**（不引入 grammar error，仅 de-escalate）
  - 例：原 "is a subject of considerable debate" → 建议 "is widely debated" 或 "is much discussed"
  - 例：原 "the role of schools in preparing young people for adulthood" → 建议 "what schools should teach young people"

### If TOO LOW: 具体的"missing Band 7 markers"清单
列出哪些 Band 7 特征缺失，例如：
- Body 2 段缺 [L]，导致 "supports main ideas" 未达 7 级
- 全篇只有 1 种 complex structure，未达 "variety of complex structures"
- 立场不一致（Intro vs Conclusion），未达 "clear position throughout"
```

---

## 2. Official Band Descriptors（必须 embedded 在 prompt 里）

### Task Response

| Band | Descriptor |
|------|-----------|
| **6** | Addresses the task although some parts may be more fully covered than others; presents a relevant position although the conclusions may become unclear or repetitive; presents relevant main ideas but some may be inadequately developed/unclear |
| **7** | Addresses all parts of the task; presents a clear position throughout the response; presents, extends and supports main ideas, but there may be a tendency to over-generalise and/or supporting ideas may lack focus |
| **8** | Sufficiently addresses all parts of the task; presents a well-developed response to the question with relevant, extended and supported ideas |

**6→7 关键**：position throughout（不是只在 conclusion）+ supports main ideas（不只是 relevant）
**7→8 关键**：well-developed（不只是 supported）

### Coherence and Cohesion

| Band | Descriptor |
|------|-----------|
| **6** | Arranges information coherently and there is overall progression; uses cohesive devices effectively but cohesion within and/or between sentences may be faulty or mechanical; uses paragraphing, but not always logically |
| **7** | Logically organises information and ideas; there is clear progression throughout; uses a range of cohesive devices appropriately although there may be some under-/over-use; presents a clear central topic within each paragraph |
| **8** | Sequences information and ideas logically; manages all aspects of cohesion well; uses paragraphing sufficiently and appropriately |

**6→7 关键**：range of cohesive devices appropriately（不是 mechanical）+ clear central topic per paragraph
**7→8 关键**：manages all aspects（seamless，无 under/over-use）

### Lexical Resource

| Band | Descriptor |
|------|-----------|
| **6** | Uses an adequate range of vocabulary; attempts to use less common vocabulary but with some inaccuracy; makes some errors in spelling/word formation but they do not impede communication |
| **7** | Uses a sufficient range of vocabulary to allow some flexibility and precision; uses less common lexical items with some awareness of style and collocation; may produce occasional errors in word choice/spelling/formation |
| **8** | Uses a wide range of vocabulary fluently and flexibly to convey precise meanings; skilfully uses uncommon lexical items but there may be occasional inaccuracies in word choice and collocation; produces rare errors |

**6→7 关键**：less common items with **some awareness of collocation**（不只是 attempts）
**7→8 关键**：**skilfully** uses uncommon items + **wide range fluently and flexibly**

### Grammatical Range and Accuracy

| Band | Descriptor |
|------|-----------|
| **6** | Uses a mix of simple and complex sentence forms; makes some errors in grammar and punctuation but rarely reduce communication |
| **7** | Uses a variety of complex structures; produces frequent error-free sentences; has good control of grammar and punctuation but may make a few errors |
| **8** | Uses a wide range of structures; the majority of sentences are error-free; makes only very occasional errors or inappropriacies |

**6→7 关键**：variety of complex structures（不只 mix）+ frequent error-free（不只是 rarely reduce communication）
**7→8 关键**：**wide range**（不只是 variety）+ **majority error-free**（不只是 frequent）

---

## 3. Band 8 Markers 清单（agent 必须扫）

以下任一出现 = LR/GRA 自动 ≥ 7.5：

### LR Band 8 markers
- "considerable" / "substantial" / "paramount" 等高阶 academic intensifier 用 3+ 次
- "a subject of considerable debate" / "of paramount importance" / "warrants careful consideration"
- 抽象名词链：the role of X in doing Y / the nature of A in shaping B
- "thrive in" / "ill-equipped to" / "tantamount to"
- "well-rounded but unemployable"（精巧 antithesis）

### GRA Band 8 markers
- Cleft sentence: "It is X that Y" / "What X does is Y"
- Inversion: "Not only does X..." / "Never has..." / "Rarely do..."
- Mixed conditional: "If X had Y, Z would Y now"
- Reduced relative clause: "Students struggling to..." (= "who struggle to")
- Passive reporting clause: "It is widely believed that..." / "It has been claimed that..."
- Wide range of subordinators in one essay（since / although / while / whereas / despite / given that / provided that）

### CC Band 8 markers
- 0 mechanical transitions（不出现 Firstly/Secondly/Moreover 排排坐 of course，but 也几乎不出现任何 obvious 衔接词，靠 logical flow）
- 段间过渡完全靠 idea progression（"This pattern raises a deeper question..."）
- 每段 central topic 不仅清晰，且和题目核心 keyword 形成完美 echo

### TR Band 8 markers
- 论点不仅 supported，而是 extended with nuance（承认对立面但 reframe）
- Conclusion 不只重申，还提出 implication 或 trade-off
- 例子不仅 concrete，还 layered（多角度 reinforce 同一论点）

---

## 4. Band 7 安全区（agent 应该看到这些就给 7.0）

- 4 段结构 + 完整 TEEL（每段 1 个 L 即可）
- Intro 第 3 句明确表立场 + Conclusion 重申
- 衔接词覆盖 4-6 个不同功能（Furthermore + However + For instance + In conclusion 这种基本组合）
- 复杂句类型 3 种（状语 + 关系 + 名词性 that-clause）
- 升级词 5-8 个（但都是 mid-level，比如 significant / beneficial / mitigate / particularly / consequently）
- 全篇 ≤ 2 个小语法错（冠词或时态偶尔）
- 250-285 词
- 没有任何 §3 Band 8 markers

---

## 5. Rewriting Recipe（agent 给出 TOO HIGH 后，怎么 de-escalate）

| 漂移点 | 修法 | 不能用的修法 |
|--------|------|------------|
| 高阶 collocation | 换更常见同义（"of considerable debate" → "widely debated"）| ❌ 改成错的 collocation（"of much debate" — 不地道）|
| 抽象名词短语 | 拆成主谓句（"the role of schools in preparing young people" → "what schools should teach young people"）| ❌ 留一半改一半（半成品反而怪）|
| 复杂句密度过高 | 拆 1-2 个长句为短句 | ❌ 加 grammar error |
| Band 8 cohesion seamlessness | 增加 1-2 个 explicit 衔接（However / In addition）| ❌ 加 Firstly/Secondly（这是降到 Band 6）|
| Skilful uncommon vocabulary | 换 mid-level 同义（"thrive in" → "do well in"）| ❌ 换 极简词（"do well in" 是 OK，"be good in" 是 5.5）|

---

## 5.5 派 examiner 的两种模式（避免嵌套陷阱）

**Mode 1 — 主 agent 直接派 examiner**（推荐）
主 Claude agent 写一篇 essay → 主 agent 直接 dispatch examiner subagent → 等返回 → 迭代。

**Mode 2 — 主 agent 派写作 subagent，写作 subagent 内部再派 examiner**（容易踩坑）
当写作任务是批量（如同时重写 4 篇 essay）时，主 agent 派一个 "rewriter subagent"，期望它内部循环 dispatch examiner。

**踩坑案例（2026-05-17）**：rewriter subagent 报告"当前环境没有可用的 Task/Agent dispatch 工具"——可能是 ToolSearch 没正确暴露 Agent 工具，或 subagent 不知道要先 `ToolSearch query="select:Agent"` 加载。结果 subagent 自评了 4 篇 essay，违反"独立 examiner"原则。

**对策**：
1. **优先用 Mode 1**：主 agent 自己写 + 自己派 examiner，不嵌套
2. **如必须用 Mode 2**（批量场景），明确告诉 rewriter subagent：
   > 你需要 dispatch examiner subagent 验证。如果发现没有 Agent 工具：(1) 先 `ToolSearch query="select:Agent"` 加载；(2) 加载成功后 dispatch examiner；(3) 如果还是不行，**停下来报错**而不是自评（违反协议）。
3. **必须做事后独立 examiner 验证**：即使 rewriter subagent 声称已 examiner 验证，主 agent 完工后**仍要派独立 examiner 再扫一遍**（防止 rewriter 自评作弊）

---

## 6. 应用范围（writing-coach SKILL 同步）

以下情境**必须**调用 examiner agent：

1. 写 `t2-band7/examples/*.md` 范文
2. 写 `t2-band7/04_toolkit.md` § 2 句式模板 + § 3 openers
3. suzy 提交 essay 后，Claude 写"参考 Band 7 版本"作为反馈
4. 任何"我给你写一段示范"的请求

**不需要**调用：
- 句子级修改（"这句改这样会更好"）
- 错误诊断（指出 grammar error）
- 概念解释（不输出整篇 essay）

---

## 7. 使用记录

每次调用 examiner agent，在 essay 文件**尾部**记录：

```
---
**Calibration log**
- 2026-05-17: examiner verdict = 6.5 / 7.0 / 7.0 / 7.0 (overall 6.75) ✅ PASS
- [如果之前被 rejected，记录 rewriter iterations]
```

这样 suzy 能看到每篇范文经过校准，不是凭感觉。
