# 判分机制（writing-drill 唯一评分真源）

> 目的：把"打分"从感觉变成**可复算的程序**。同一篇文章、不同时间判两次，必须得同一个分。
> 来源：IELTS 官方 Writing Band Descriptors（public version, Updated May 2023, ielts.org）+ `anchors.md` 里 30+ 篇真实带分范文的考官评语反推。

---

## 0. 为什么要重建这套机制（必读，别跳）

**历史问题**：2026-06 教练给她的 cold 作文判 7.0–7.5。同期 Gemini 给同类作文判 6.5（LR 6.0 / GRA 6.0）。7/24 的 199 句普查给出裁决性证据：**她的干净句率只有 22%**。

官方 Band 7 GRA 要求 `error-free sentences are frequent`。22% 不是 frequent。**所以 6 月那批 7.0–7.5 是虚高**，原因有三：
1. **未限时**（6/14–6/15 那 7 篇全是 untimed，她自己标注的）
2. 教练按"她想表达的水平"判，不是按纸面判
3. 没有真实带分样本做锚，全凭印象

**所以本 skill 的第一条规则是：判分必须先数数，再给分。** 不数不给分。

---

## 1. 四项标准 · 官方描述符关键句（Band 5/6/7/8）

只摘每档的**裁决句**。完整表见 ielts.org 官方 PDF。

### Task 2 — Task Response
| Band | 裁决句（官方原文） |
|---|---|
| 8 | "The prompt is appropriately and sufficiently addressed." / "A clear and well-developed position is presented." / "Ideas are relevant, well extended and supported." |
| **7** | "The main parts of the prompt are appropriately addressed." / "A clear and developed position is presented." / "Main ideas are extended and supported **but there may be a tendency to over-generalise or there may be a lack of focus and precision in supporting ideas/material**." |
| **6** | "The main parts of the prompt are addressed (**though some may be more fully covered than others**)." / "A position is presented that is directly relevant to the prompt, **although the conclusions drawn may be unclear, unjustified or repetitive**." / "Main ideas are relevant, **but some may be insufficiently developed or may lack clarity**." |
| 5 | "The main parts of the prompt are **incompletely** addressed." / "The writer expresses a position, **but the development is not always clear**." / "Some main ideas are put forward, but they are **limited and are not sufficiently developed**." |

### Task 1 (Academic) — Task Achievement
| Band | 裁决句 |
|---|---|
| 8 | "Key features are skilfully selected, and clearly presented, highlighted and illustrated." |
| **7** | "Key features which are selected are covered and clearly highlighted **but could be more fully or more appropriately illustrated or extended**." + "**It presents a clear overview, the data are appropriately categorised, and main trends or differences are identified.**" |
| **6** | "Key features which are selected are covered and adequately highlighted. **A relevant overview is attempted.**" / "**Some irrelevant, inappropriate or inaccurate information may occur in areas of detail**" / "Some details may be missing (or excessive)" |
| 5 | "Key features which are selected are **not adequately covered**. The recounting of detail is **mainly mechanical**. There may be **no data to support the description**." / "a tendency to focus on details (**without referring to the bigger picture**)" / "The inclusion of irrelevant, inappropriate or **inaccurate material in key areas** detracts from the task achievement." |

🔑 **T1 三道硬门**（直接从上表读出来的）：
- **没有 overview → 上限 5**（"without referring to the bigger picture"）
- **overview 有但只是"尝试"（一根柱子 / 两根柱子说的是同一件事 / 漏 odd-one-out）→ 上限 6**
- **数据错在关键特征上（不是细节）→ 掉向 5**；数据错只在细节 → 停在 6

### Coherence & Cohesion（T1/T2 措辞几乎一致）
| Band | 裁决句 |
|---|---|
| 8 | "Information and ideas are logically sequenced, and cohesion is well managed." |
| **7** | "Information and ideas are logically organised, and there is a clear progression throughout." / "A range of cohesive devices including reference and substitution is used flexibly **but with some inaccuracies or some over/under use**." / "Paragraphing is generally used effectively." |
| **6** | "generally arranged coherently and there is a clear overall progression." / "Cohesive devices are used to some good effect **but cohesion within and/or between sentences may be faulty or mechanical due to misuse, overuse or omission**." / "**Paragraphing may not always be logical and/or the central topic may not always be clear**." |
| 5 | "Organisation is evident but is not wholly logical" / "**Paragraphing may be inadequate or missing**." |

🔑 **CC 硬门**：段落切分失败 → 上限 5（考官原话见 anchors：*"Paragraphing is inadequate so your score is limited to 5."*）

### Lexical Resource
| Band | 裁决句 |
|---|---|
| 8 | "Occasional errors in spelling and/or word formation may occur, **but have minimal impact on communication**." |
| **7** | "The resource is sufficient to allow some flexibility and precision." / "An awareness of style and collocation is evident, **though inappropriacies occur**." / "There are **only a few errors** in spelling and/or word formation and they **do not detract from overall clarity**." |
| **6** | "The resource is generally adequate and appropriate for the task." / "Examples of ... **a rather restricted range or a lack of precision in word choice**." / "There are **some errors** in spelling and/or word formation, **but these do not impede communication**." |
| 5 | "**frequent lapses in the appropriacy of word choice**, and a lack of flexibility is apparent in frequent simplifications and/or repetitions." / "Errors ... **may be noticeable and may cause some difficulty for the reader**." |

### Grammatical Range & Accuracy
| Band | 裁决句 |
|---|---|
| 8 | "**The majority of sentences are error-free**, and punctuation is well managed." |
| **7** | "A variety of complex structures is used with some flexibility and accuracy." / "Grammar and punctuation are generally well controlled, and **error-free sentences are frequent**." / "A few errors in grammar may persist, **but these do not impede communication**." |
| **6** | "A mix of simple and complex sentence forms is used **but flexibility is limited**." / "Examples of more complex structures are **not marked by the same level of accuracy as in simple structures**." / "Errors in grammar and punctuation occur, **but rarely impede communication**." |
| 5 | "Although complex sentences are attempted, **they tend to be faulty**, and the greatest accuracy is achieved on simple sentences." / "Grammatical errors may be **frequent and cause some difficulty for the reader**." / "Punctuation may be faulty." |

---

## 2. 数数程序（判分前必做，结果要写进反馈）

### 2.1 GRA：干净句率 = 唯一主判据

**步骤**：
1. 按句号切句（分号独立成句，逗号粘连算 1 句但记 1 个错）
2. 逐句判：**含 ≥1 个语法/标点错 = 脏句**。算错的包括：冠词、单复数、主谓一致、动词形式/时态、介词框架（`invest into` / `disagree this`）、句子片段、逗号粘连、悬垂修饰、词序
3. 不算 GRA 的：拼写、词汇选择、搭配（那些进 LR）
4. `干净句率 = 干净句 / 总句数`

**判档**：
| 干净句率 | GRA | 依据 |
|---|---|---|
| ≥ 70%，错误罕见且小 | **8** | 官方 "the majority of sentences are error-free"；IELTS Advantage："Most of the sentences are completely error-free" |
| **≈ 50%**（40–70%），复杂句有对的，无阻碍性错误 | **7** | 官方 "error-free sentences are frequent"；IELTS Advantage 明确量化：**"around 50% of the sentences are completely error-free"** |
| **< 50%**，错误贯穿但不妨碍理解 | **6** | 官方无 error-free 要求；IELTS Advantage："**The majority of sentences have errors**, but these errors rarely stop the reader from understanding" |
| 复杂句普遍崩，读者需要重读 | **5** | "errors may be frequent and cause some difficulty for the reader" |

> 出处：https://www.ieltsadvantage.com/2015/04/18/difference-band-5-and-8-in-ielts-writing-task-2-band-scores/
> **她 7/24 普查基线 = 22% → GRA 6.0（离 50% 还差一半以上）。**
> 🎯 **唯一的主战场：干净句率 22% → 50%。** 这一项就值 0.5 分。

### 2.2 LR：词汇错误计数

**计数对象**（每 ~270 词）：拼写错 + 词形错（word class）+ 词义/搭配错 + 中式直译块，各算 1。
> 同一个词拼错 3 次算 3 次（考官读到的就是 3 次）。

| 词汇错个数 | LR |
|---|---|
| 0–2 | 8 |
| **3–5** | **7** |
| **6–12** | **6** |
| 13+，或错到让读者卡住 | **5** |

> 她 7 月 cold 作文实测：每篇 6–20 个（光拼写就 6–9 个）→ **LR 6.0**，个别 5.5。

⚠️ **平实 ≠ 扣分**。锚文里 Band 7 全 7 的那篇最"高级"的词是 `pester`；Band 7.5 那篇写的是 `The wife is usually subjected to domestic violence`。
**LR 扣的是"错"，不是"平"。** 她的池是 FLOOR 不是 CEILING（[[feedback_writing_reuse_pool]]）——用对的词不许判。

### 2.3 TR/TA + CC：清单勾选

**T2 · TR 清单**（每项 ✅/❌，附证据句）
- [ ] 题目每一问都答了（两问题各占独立段落？）
- [ ] 立场在引言明确写出，且全文不自相矛盾
- [ ] 每个 body 段有 1–2 个**主论点**，且每个都展开了（不是罗列 5 个都不展开）
- [ ] 论证回答的是 **WHY**（为什么这样有效/成立），不是 **HOW**（怎么做）
- [ ] 每段最后有 L 句（`Therefore, [重述]`）把论点接回题目
- [ ] 结论重述立场 + 理由，不引入新内容
- [ ] ≥ 250 词

**T1 · TA 清单**
- [ ] 有 overview 段，且 `Overall,` 开头
- [ ] overview 有**两根互相独立的柱子**（不是同一事实的两种说法）
- [ ] overview 抓到了 odd-one-out / 最大 / 变化最陡
- [ ] 每个类别/数列都有真实数字支撑，没有"其余的"糊过去
- [ ] 多线/多图：有跨线跨图对比句（`whereas / in contrast / A outnumbered B`）
- [ ] 每个数字、每个年份逐一对着图核过
- [ ] 有时间轴 → 过去时 + rise/fall；无时间轴 → 现在时 + share 语言
- [ ] 没有图上没有的推测/原因（T1 三禁）
- [ ] ≥ 150 词

**CC 清单**（T1/T2 通用）
- [ ] 4 段（T2）/ 4 段（T1：intro + overview + body×2）
- [ ] 每段一个中心，topic sentence 单独读能站住
- [ ] 连接词覆盖 ≥4 种功能且不是每句开头都挂一个
- [ ] 代词/替代（this / these / the former）指代无歧义

---

## 3. 算总分

1. 四项各自定档（半档可以：6.5 / 7.0）
2. **总分 = 四项平均**
3. 进位：`.25 → 进 .5`；`.75 → 进下一整档`。例：6.5+6.5+6+6 = 25/4 = 6.25 → **6.5**
4. **Writing 总分 = (T1 × 1 + T2 × 2) / 3**，同样进位

**惩罚**（写进 TR/TA，不另外扣）：
- T2 < 250 词 / T1 < 150 词 → **TR/TA −1**（考官原话：`7-1=6`）
- 完全跑题 → TR ≤ 3
- 明显背诵段落 → TR 大幅下压
- 抄题干原句 → 抄的部分不计入词数

### 🚧 硬顶（触发即封顶，不看其它表现）
| 触发条件 | 封顶 | 出处 |
|---|---|---|
| 段落切分失败 / 只有一个 body 段 / 没分段 | **CC ≤ 5** | 考官原话 "Paragraphing is inadequate so your score is limited to 5"；Liz："only one body paragraph… you will get around band 5 for CC" |
| **没写结论段** | **TR ≤ 5** | Liz："Failure to write a conclusion for task 2 will result in band 5 for Task Response" |
| 只答了一半的题（两问题只答一问） | **TR ≤ 5** | Liz："if you fail to answer the whole question and only answer half of it, you will not get above band score 5 in task response" |
| 改写题干时错误频繁 | **LR ≤ 5.5** | Liz："If you have frequent errors, you will get band score 5 or 5.5 in vocabulary" |
| 连接词机械（几乎每句开头挂一个 / Firstly-Secondly-Thirdly 套） | **CC ≤ 6** | Liz："Your use of linking words is mechanical, which is a feature of band 6" |
| T1 无 overview | **TA ≤ 5** | 官方 Band 5 描述符 "without referring to the bigger picture" |

### 📏 字数目标（不只是及格线）
- **T2 写 270–290 词**。Liz：`Band 5 = ideas are limited and not sufficiently developed` → `Band 7 = extends main ideas` → **"if you are aiming for band 7, you ought to be aiming for 270-290 words"**。低于 250 扣分；超过 ~320 会稀释焦点、也吃掉检查时间。
- **T1 写 165–190 词**。低于 150 扣分。

---

## 4. 相邻档的分界测试（可核查，不靠感觉）

### 5 vs 6
6 有的、5 没有的：**立场从头到尾能被读出来** + **段落切分成立** + **错误不让读者卡住**。
> 反例锚：ieltsanswers "免费大学教育"篇 LR 7 / GRA 7，但两个 body 段的 topic sentence 互相矛盾 → TR 3-4 → **总分 5.0**。语言好救不了立场崩。

### 6 vs 7 ← 她的战场
逐项对照，**7 必须四项都摸到**：

| 项 | 6 的样子 | 7 的样子 | 她的现状 |
|---|---|---|---|
| TR | 各部分覆盖不均；主论点有但没展开 | 每部分都答到；论点 extended + supported | ✅ 已在 7 |
| CC | 连接机械/过度；段落中心偶尔糊 | 逻辑清晰、进展明确、段落有效 | ✅ 已在 7 |
| LR | 6–12 个词汇错 | ≤5 个 | ❌ **卡在 6** |
| GRA | 干净句率 15–35% | **≥35%** | ❌ **卡在 6（22%）** |

**结论：她离 7 差的不是想法、不是结构、不是连接词，是表层准确率。**
两件事，各值 0.5 分：**拼写清零** 和 **干净句率 22%→35%**。

### 7 vs 7.5/8
- GRA 干净句率过 60%
- LR 出现自然的 less common / idiomatic 用法且用对（不是硬塞难词）
- TR 论点展开有深度，不停在 over-generalise
> 考官反例：`unnecessarily complex structures` 会被 **扣** CC —— "reading your writing causes me to feel frustrated"。**别为了上 8 把句子写复杂。**

---

## 5. 反虚高协议（🔒 硬规则）

1. **不数不判。** 每次给分必须先写出：总句数 / 干净句数 / 干净句率 / 词汇错个数。这三个数进 session 文件。
2. **两档之间取低的。** 6.5 和 7 之间犹豫 → 给 6.5。（注意：这和 `_examiner_protocol.md` 的"取高"方向相反 —— 那份是用来**压教练范文别超 Band 7**的，跟给她判分是两件事，别混。）
3. **限时才算数。** 未限时的分永远标 `(untimed)`，不进步曲线。40 分钟（T2）/ 20 分钟（T1）是分数的一部分。
4. **查来源。** 只判她 cold 原稿。任何经过 Gemini/教练/语法工具修过的文本一律不判 —— 2026-07-12 那次就是把 Gemini 的改后稿当成她的 cold 判了 7 分，结论全错（见 `bank.md` 备注）。判前先问一句"这是你自己写完没动过的原稿吗"。
5. **平实不扣分。** 只扣错，不扣"简单"。
6. **发反馈前跑四问自审**（[[feedback_coach_selfreview_before_output]]）：① 我能不能推翻自己这条 ② 这条和上一条矛盾吗 ③ 这是 ❌真错 / ⚠️不地道 / ✅有更好的，哪一层 ④ 假错比漏错代价大。
7. **🔴 数完必须查表，不许"感觉上不至于这么低"。** 数出 14 个词汇错就是 LR 5.0。**教练两次虚高都是死在这一步。** 如果查表结果让你意外，那说明表是对的、你的印象是错的。
8. **🔴 AI 判分不算交叉验证。** Gemini / ChatGPT / 各种 checker 和教练是同一类不可靠仪器，两个都判 6.5 不构成印证。**唯一的 ground truth 是真实考试分数**（见 §6.5）。
9. **🔴 TR/CC 不许因为"她结构好"就默认给 7。** 逐条查硬顶：连接词是不是固定槽位（→CC 6）？论据有没有具体地名/数字/机制（没有 →TR 6）？她的强项是**相对**强，不是绝对达标。

---

## 6. 走一遍：用她的真实作文校准

**样本**：2026-07-14 cold，剑18T4 老龄化 outweigh 变体，40 分钟（`gemini/corrections_2026-07.md:695-701`）

- 拼写错：cruial · maintainance · neccessary · goverments · popution · orderly/oderly(×2) = **7 个**
- 词义/搭配/中式块：`bring in some benefits` · `On the society side` · `These knowledge` · `more clear` · `the leaving school time of students is usually before 5pm` · `long-term ills` · `the youth workplace` = **7 个**
- → 词汇错 **14 个** → 查表 13+ → **LR 5.0**
  > ⚠️ 本文件初版在这里写了 LR 6.0 —— **数了 14 个却给了 6 分，等于没用自己的表**，因为当时拿 Gemini 的 6.0 当参照。这就是虚高是怎么发生的。
- 语法错：`an ageing population put massive burden`（主谓+冠词）· `With ages growing`（悬垂）· `most parents have to overtime`（词类）… 约 15 句里干净 3–4 句 → **~23%** → 低于 50% → **GRA 6.0**；但 `the leaving school time of students is usually before 5pm` / `With ages growing` 这类要读者回读 → 触及 Band 5 的 "cause some difficulty for the reader" → **GRA 5.5**
- TR：两边覆盖、立场清楚、有 L 句，但例子全是泛化的（无具体地名/数字/机制）→ 官方 Band 6 "Main ideas are relevant, but some may be insufficiently developed" → **6.0–6.5**
- CC：四段、进展清楚，但连接是**固定槽位**（每段末 `Therefore,`、每处举例 `For example`、转折固定 `On the other hand`）→ Liz："mechanical … is a feature of band 6" → **6.0**
- **总分 = (6+6+5+5.5)/4 = 22.5/4 = 5.625 → 5.5**

✅ **这与她的真实考试分数一致。**

---

## 6.5 🔴 Ground truth：实际考试 Writing = **5.5**

**判分历史（同一批作文，三次判分）**：

| 判分者 | 结论 | 错在哪 |
|---|---|---|
| 教练 2026-06 | 7.0–7.5 | 未限时 + 完全没数错误 |
| Gemini / 教练 2026-08 初版 | 6.5 | 数了错误，但**没按自己的表定档**，且拿 AI 判分当交叉验证 |
| **实际考试** | **5.5** | ← **唯一的 ground truth** |

**教练同一个方向连错两次，每次差一个整档。** 这不是随机误差，是系统性偏高。三个成因：
1. **拿 AI 判分当交叉验证** —— Gemini 和教练是同一类不可靠仪器，两个都偏高不构成印证。（研究材料里的原话：AI 判分器"mostly produced the wrong grades"。）
2. **被 TR/CC 的好印象带跑** —— 她结构确实清楚，于是连带把 LR/GRA 也往上判。
3. **数完不查表** —— 数出 14 个词汇错，却写 LR 6.0。

**新增的三条防线** → 见 §5 规则 7–9。

**⚠️ 还需要验证的两个假设**（初版判 TR/CC 都是 7.0–7.5，真实考试说明至少有一项更低）：
- **假设 A：CC 只有 6.0** —— 她的连接词是固定槽位（Therefore / For example / On the other hand 各就各位），这正是官方和 Liz 说的 "mechanical"，硬顶 6。
- **假设 B：TR 只有 6.0–6.5** —— 她的论据全是泛化陈述，没有具体地名/数字/机制（对照 `anchors.md §8` 的 Band 6/7/8 三档演示，她多数段落落在 Band 6 那一档）。
→ **下一篇限时 cold 专门验这两条**，别再默认 TR/CC 是 7。

---

## 7. 每次判分的输出模板（照抄）

```
## Marking — [题号] [题型] · [timed/untimed] · [词数] words

### Counts
- Sentences: N total / M clean → **X% clean**  (last time on this question: Y%)
- Lexical errors: K  (spelling S / word-form F / word-choice W / Chinglish C)

### Bands
| | Band | Why (evidence) |
|---|---|---|
| TR/TA | | |
| CC | | |
| LR | | |
| GRA | | |
| **Overall** | **x.x** | |

### What moved since last attempt on this question
(new / fixed / relapsed)

### Errors  ❌ real error  ⚠️ unnatural  ✅ better version available
| Your sentence | Type | Fix |

### Clean version
(her text, minimally corrected — 不重写，不升级词汇)

### One thing to carry into the next essay
```
