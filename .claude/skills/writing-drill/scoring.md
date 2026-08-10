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

### 2.0 ★★ 计数归属唯一律（每个错只能进一个桶）

> 背景：原来没写，导致 `In Conclusion`（大小写）既被算进 LR 又弄脏 GRA 句 = 一个错扣两次；
> 中式块 `the leaving school time of students` 归属也没写死。**双计 = 系统性压低，和虚高一样是仪器坏了。**

```
GRA 桶（弄脏句子，进干净句率）
   冠词 · 单复数 · 主谓一致 · 动词形式/时态 · 介词框架 · 句子片段 · 逗号粘连
   · 悬垂修饰 · 词序 · ★大小写 · ★标点
LR 桶（进词汇错个数 K，不弄脏句子）
   拼写 · 词形（word class）· 词义 · 搭配 · 中式直译块

★★ 唯一的合法双计：**中式直译块**
   理由：它同时是"词选错"（LR）和"句子读不通"（GRA）。官方两条描述符各自命中。
   执行：① 计 1 个 LR 错  ② 该句同时判脏
        ③ **必须在 G3 阶段 1 的证据块（A3）里写明"双计：<原句片段>"** —— 不写 = 不许双计
★ 除此之外，任何一个错只能出现在一个桶里。G3 **阶段 1 断言 4** 就是查这个。
```

### 2.1 GRA：干净句率 = 唯一主判据

**步骤**：
1. 按句号切句（分号独立成句，逗号粘连算 1 句但记 1 个错）
2. 逐句判：**含 ≥1 个 GRA 桶的错 = 脏句**（桶的划分见 §2.0）
3. `干净句率 = 干净句 / 总句数`

**判档 —— ★★★ 唯一阈值表（全项目只此一处；其它文件一律【引用本表】，不许重述数字）**

> 🔴 **2026-08-10 更正史（这条留着当教训，别删）**：同一个阈值曾在三处给出互不兼容的值 ——
> 本节写 `≥70→8 / 40–70→7 / <50→6`（40–50 与 70 两处区间**重叠**）、§4 写 `≥35% ⇒ Band 7`、
> `profile.md §0` 写 `35% ⇒ GRA 6.0`。**同一个指标横跨整整一档。**
> 成因：阈值从 35% 改到 50% 时只改了本节，另外两处没跟。⇒ 现改为**半开区间、单一真源**。

> 🔴 **2026-08-10 二修（F57）**：表头写着"半开区间无重叠"，可四行写的是**闭合整数区间**
> `50 – 69% / 35 – 49%` —— `(49%, 50%)` 和 `(69%, 70%)` 两段**谁都不管**。
> 13 句里干净 9 句 = 69.23%，按老表**查不到任何一行**。⇒ 现真的写成半开区间。

| 干净句率（半开区间，四行覆盖 [0,100]，无缝无重叠） | GRA | 依据 |
|---|---|---|
| **[70%, 100%]** | **8.0** | 官方 "the majority of sentences are error-free"；IELTS Advantage："Most of the sentences are completely error-free" |
| **[50%, 70%)** | **7.0** | 官方 "error-free sentences are frequent"；IELTS Advantage 明确量化：**"around 50% of the sentences are completely error-free"** |
| **[35%, 50%)** | **6.0** | 官方无 error-free 要求；IELTS Advantage："**The majority of sentences have errors**, but these errors rarely stop the reader from understanding" |
| **[0%, 35%)** | **6.0**；若【回读句 ≥ 2】则 **5.5** | Band 5 "errors may be frequent and **cause some difficulty for the reader**" |

> 读法：`[a, b)` ＝ 含 a、不含 b。69.23% → `[50%,70%)` → **7.0**；50.0% → `[50%,70%)` → 7.0；
> 49.99% → `[35%,50%)` → 6.0。**不许四舍五入到整数再查表**，直接拿百分比落区间。

**★★ 回读句 —— GRA 唯一的 −0.5 杠杆，且【只在 `[0%, 35%)` 这一行】生效**
```
定义  读者必须回到句首重读一次才能解析的句子。只认四种结构性崩塌：
      ① 悬垂 / 无逻辑主语        （`With ages growing, …`）
      ② 中式语序整块搬            （`the leaving school time of students is usually before 5pm`）
      ③ 主谓被长名词块吃掉，读到句末才找到谓语
      ④ 成分缺失，句子闭合不了
执行  必须【逐句列出句号 S<n>】写进 G3 阶段 1 的证据块（A1）。**不列 = 不许用这个杠杆。**
阈值  回读句 ≥ 2 → 5.5 ｜ ≤ 1 → 6.0
边界  ★ 这个杠杆【不许】用在 ≥35% 的任何一行。35% 以上出现回读句只记录、不减分。
      理由：再开一个减分口 ＝ 又造一个不可复算的自由度，正是本文件要消灭的东西。
```
**★ GRA 的半档【只有】这一个合法来源。** 任何其它 GRA 半档（6.5 / 7.5）一律非法，见 §3.1。

**历史核对（新表必须能重现已记录的分，否则表是错的）**
| 样本 | 干净句率 | 回读句 | 查表 | 已记录 | 一致？ |
|---|---|---|---|---|---|
| 7/24 199 句普查基线 | 22% | 有（`With ages growing` 等） | `[0,35)` + ≥2 → **5.5** | profile §0 = 5.5 | ✅ |
| 07-14 T2-18 | ~23% | 2（见 §6） | `[0,35)` + ≥2 → **5.5** | §6 = 5.5 | ✅ |
| 08-10 T2-18 | 37.5% | 2（S7/S15） | `[35,50)` → **6.0**（杠杆不生效） | bank 曲线 = 6.0 | ✅ |
| （F57 的病例）13 句 / 干净 9 | 69.23% | — | `[50,70)` → **7.0** | 老表**查不到任何一行** | 新表 ✅ |

> 出处：https://www.ieltsadvantage.com/2015/04/18/difference-band-5-and-8-in-ielts-writing-task-2-band-scores/
> 🎯 **主战场两级台阶**：`22% → 35%`（GRA 5.5→6.0，服务近期目标 6.5）→ `35% → 50%`（GRA 6.0→7.0）。

### 2.2 LR：词汇错误计数

**计数对象**：拼写错 + 词形错（word class）+ 词义错 + 搭配错 + 中式直译块，各算 1（桶的边界见 §2.0）。
> 同一个词拼错 3 次算 3 次（考官读到的就是 3 次）。

**★ 归一化（F37：本表以 270 词为基准，别的长度必须先折算）**
```
词汇错密度 K270 = 词汇错个数 K ÷ 实际词数 × 270      ← 四舍五入到整数
★ 查表一律查 K270，不查原始 K。两个数都要写进 G3 阶段 1 的证据块（A2）。
★ 例：165 词的 T1 里 8 个词汇错 → K270 = 8 ÷ 165 × 270 = 13.1 → 13 → LR 5.0
  （不折算的话 8 个会被读成 LR 6.0 —— 差一整档）
```

| 词汇错密度 K270 | LR |
|---|---|
| 0–2 | 8 |
| **3–5** | **7** |
| **6–12** | **6** |
| 13+ | **5** |

**★★ LR 没有半档。** 上表是单值函数，`LR 6.5 / 7.5` 一律非法（见 §3.1）。
原表末行那句"**或错到让读者卡住**"改写成一条**可数的 Band 5 触发条款**：

```
形近词触发   【改变意思的形近词/错词】≥ 3 个不同的词 → 直接判 **LR 5.0**，不看密度
定义   拼写接近、但换成了另一个真实存在的词，因而改变意思。
       她的实例（profile §P5 的"形近/错词"那一行就是这个闭集）：
       go rural→viral · per capital→capita · model→modern · tread→trend
       · orderly→elderly · founded→found · faulty→fault · yam→yarn
计数   ★ 按【不同的词】计，同一个词错 3 次算 1 个
       （注意：这与 K 的计数规则相反 —— K 数实例，本条数种类。写进证据块时两个数都要写）
执行   必须逐个列出，写进 G3 阶段 1 的证据块（A2）。不列 = 不许触发。
```

**历史核对**
| 样本 | K270 | 形近词种类 | 查表 | 已记录 | 一致？ |
|---|---|---|---|---|---|
| 07-14 T2-18 | 14/280×270 ≈ 14 → 13+ | 1（orderly→elderly） | **5.0** | §6 = 5.0 | ✅ |
| 08-10 T2-18 | 9/284×270 ≈ 9 → 6–12 | 0（零拼写错） | **6.0** | bank 曲线 = 6.0 | ✅ |

> **她 7 月 cold 作文实测**：每篇原始 K = **6–20 个**（光拼写就 6–9 个）。
> ★ 原始 K **不查表**，先折成 K270（见上）。她 7 月那批折完落在本表的 `6–12` 与 `13+` 两行
> ⇒ **LR 6.0 或 LR 5.0，查表定，不另判。**
> ⚠️ **本行 2026-08-10 二修（F72）**：原文写的是「→ LR 6.0，个别 5.5」，三处都错 ——
> ① 拿原始 K 当查表输入（违反上面刚定的归一化强制）② 20 个错查本表是 `13+ → 5`，不是 6.0
> ③ `LR 5.5` 是 §3.1 明令非法的半档，**写在禁它的那一段下面五行**。
> ⚠️ `bank.md` 里还留着几行 `LR 5.5 / 6.5`，那是 **Gemini 时期的旧判分**。
> **它们是历史记录，不是先例** —— 新规起 LR 只出整档。

⚠️ **平实 ≠ 扣分**。锚文里 Band 7 全 7 的那篇最"高级"的词是 `pester`；Band 7.5 那篇写的是 `The wife is usually subjected to domestic violence`。
**LR 扣的是"错"，不是"平"。** 她的池是 FLOOR 不是 CEILING（[[feedback_writing_reuse_pool]]）——用对的词不许判。

### 2.3 TR/TA + CC：清单勾选

**★★ 走哪条清单由题型决定，不许混（F18）**
```
T2（Task 2）→ 走 §2.3a TR 清单（7 项） ＋ §2.3c CC 清单（4 项）
T1（Task 1）→ 走 §2.3b TA 清单（9 项） ＋ §2.3c CC 清单（4 项）
             ★ T1 另加 `anchors.md §9.8` 的 7 条可核查测试（全是封顶条款，逐条走）
★ G3 **阶段 2 断言 11** 检查的就是"分支选对了没有"：判 T1 却勾了 TR 清单 = FAIL
```

#### 2.3a T2 · TR 清单（7 项，每项 ✅/❌，**必须附一句原文证据**）
- [ ] 题目每一问都答了（两问题各占独立段落？）
- [ ] 立场在引言明确写出，且全文不自相矛盾
- [ ] 每个 body 段有 1–2 个**主论点**，且每个都展开了（不是罗列 5 个都不展开）
- [ ] 论证回答的是 **WHY**（为什么这样有效/成立），不是 **HOW**（怎么做）
- [ ] 每段最后有 L 句（`Therefore, [重述]`）把论点接回题目
- [ ] 结论重述立场 + 理由，不引入新内容
- [ ] ≥ 250 词

#### 2.3b T1 · TA 清单（9 项）
- [ ] 有 overview 段，且 `Overall,` 开头
- [ ] overview 有**两根互相独立的柱子**（不是同一事实的两种说法）
- [ ] overview 抓到了 odd-one-out / 最大 / 变化最陡
- [ ] 每个类别/数列都有真实数字支撑，没有"其余的"糊过去
- [ ] 多线/多图：有跨线跨图对比句（`whereas / in contrast / A outnumbered B`）
- [ ] 每个数字、每个年份逐一对着图核过
- [ ] 有时间轴 → 过去时 + rise/fall；无时间轴 → 现在时 + share 语言
- [ ] 没有图上没有的推测/原因（T1 三禁）
- [ ] ≥ 150 词

#### 2.3c CC 清单（4 项，T1/T2 通用）
- [ ] 4 段（T2）/ 4 段（T1：intro + overview + body×2）
- [ ] 每段一个中心，topic sentence 单独读能站住
- [ ] 连接词覆盖 ≥4 种功能且不是每句开头都挂一个
- [ ] 代词/替代（this / these / the former）指代无歧义

#### 2.3d ★★★ 勾选率 → 档位（TR/TA 与 CC 的唯一定档程序）

> 背景（F14）：原来只写"半档可以：6.5/7.0"，**没有任何推导规则** —— 于是 TR/CC 变成整套机制里
> 唯一凭印象的地方，而 §6.5 记录的两次虚高恰恰是"被 TR/CC 的好印象带跑"。**印象口必须封死。**

```
★ 每一项必须带【一句原文证据】才算勾到。没有证据句 = 不算勾到。
★ 用【勾到的项数】查表，不用百分比 —— CC 只有 4 项，用比例算永远出不了 6.5，是坏刻度。
```

> ⚠️ **2026-08-10 二修（F77）**：原表的行标签（全勾 / 差1 / 差2–3 / 差4–5 / 差更多）与格子里的数**对不上**
> —— TR 的「差2–3」格里只有 `5/7`（那是差 2），CC 的「差4–5」格里是 `1/4`（那是差 3）。
> **格子是对的（三条历史核对都能重现），标签是错的。** ⇒ 删掉「差 N」这一列，直接用勾到的项数当行键。

| Band | T2 · TR（共 7 项） | T1 · TA（共 9 项） | CC（共 4 项） |
|---|---|---|---|
| **7.0** | 7/7 | 9/9 | 4/4 |
| **6.5** | 6/7 | 8/9 | 3/4 |
| **6.0** | 5/7 | 6–7/9 | 2/4 |
| **5.5** | 3–4/7 | 4–5/9 | 1/4 |
| **5.0** | ≤2/7 | ≤3/9 | 0/4 |

> ★ 三列各自**穷尽**了 0…N，没有空档：TR 覆盖 0–7 ｜ TA 覆盖 0–9 ｜ CC 覆盖 0–4。
> 查表方式：拿勾到的**项数**在该题型那一列里找，读最左边的 Band。

```
★★ 三条硬约束
① 查完表【必须再过一遍 §3.3 硬顶】，硬顶更低就取硬顶（两个取低，见 §5.2）
② 7.0 以上（7.5 / 8.0）本 skill 【不判】—— 需要 §4 的 "7 vs 7.5/8" 三条测试各自写出证据才允许。
   她当前基线 5.5，凭空冒出 7.5 几乎必然是虚高（§6.5 的两次都是这么来的）。
③ 勾选表【必须整表打印】（勾到的和没勾到的都列，各带证据句），这是 G3 **阶段 2 断言 11** 的证据块
```

**历史核对（新规则必须能重现已记录的分）**
| 样本 | 项 | 勾/总 | 查表 | 已记录 | 一致？ |
|---|---|---|---|---|---|
| 08-10 T2-18 | TR | 6/7（差「每个 body 段主论点都展开」—— Body1 论点 1 偷换概念） | **6.5** | 6.5 | ✅ |
| 08-10 T2-18 | CC | 2/4（差「连接词非机械」= `On the one hand` 无对应下文（omission）；差「指代无歧义」= `it`/`which` 含糊 ×2） | **6.0** | 6.0 | ✅ |
| 07-14 T2-18 | CC | 2/4（差「连接词非机械」= 固定槽位；差「指代无歧义」） | **6.0** | 6.0 | ✅ |

> ⚠️ 07-14 的 TR 6.0 需要 5/7。原记录只写了"例子全是泛化"，没有逐项勾选表 —— **无法复算**。
> 这不是表的问题，是那次判分没留证据块。**从 G3 阶段 2 起，没有整表打印的 TR/CC 分一律不成立。**

---

## 3. 算总分

1. 四项各自定档（GRA 见 §2.1 · LR 见 §2.2 · TR/TA 与 CC 见 §2.3d）
2. **总分 = 四项平均**
3. 进位：**先算四项平均，再取最近的 0.5**；恰好落在 `.25` / `.75` 上 → **向上进**。
   例：6.5+6.5+6+6 = 25/4 = 6.25 → `.25` → **6.5**
   例：6.5+6+6+6  = 24.5/4 = 6.125 → 最近的 0.5 是 6.0 → **6.0**（= 08-10 已记录的分）
   例：6+6+5+5.5  = 22.5/4 = 5.625 → 最近的 0.5 是 5.5 → **5.5**（= §6 已记录的分）
4. **Writing 总分 = (T1 × 1 + T2 × 2) / 3**，同样进位

### 3.1 ★★ 半档的合法来源（穷举，此外一律非法）

```
GRA   只有一个：§2.1 的【回读句 ≥2】杠杆，且只在 <35% 行生效
LR    **一个都没有** —— §2.2 是单值表，LR 6.5 / 7.5 一律非法
TR/TA/CC  只有一个：§2.3d 的勾选数表（6.5 与 5.5 是表里的格子，不是"感觉在两档之间"）
总分  只有一个：§3 第 3 条的进位规则（四项平均后取最近 0.5，.25/.75 向上）

★ 出现任何其它半档 → G3 阶段 2 直接 FAIL，不许"两档之间取中"。
  "犹豫就取低"（§5.2）是【整档之间】的规则，**不是造半档的授权**。
★ 为什么要把半档口封到这么死：半档是整套机制里唯一没有刻度的自由度，
  而 §6.5 记录的两次虚高都发生在"没有刻度、凭印象"的地方。
```

### 3.2 惩罚（写进 TR/TA，不另外扣）
- T2 < 250 词 / T1 < 150 词 → **TR/TA −1**（考官原话：`7-1=6`）
- 完全跑题 → TR ≤ 3
- 明显背诵段落 → TR 大幅下压
- 抄题干原句 → 抄的部分不计入词数

### 3.3 🚧 硬顶（触发即封顶，不看其它表现 —— G3 **阶段 2 断言 10** 要求**逐行**打印触发与否 + 证据）
| 触发条件 | 封顶 | 出处 |
|---|---|---|
| 段落切分失败 / 只有一个 body 段 / 没分段 | **CC ≤ 5** | 考官原话 "Paragraphing is inadequate so your score is limited to 5"；Liz："only one body paragraph… you will get around band 5 for CC" |
| **没写结论段** | **TR ≤ 5** | Liz："Failure to write a conclusion for task 2 will result in band 5 for Task Response" |
| 只答了一半的题（两问题只答一问） | **TR ≤ 5** | Liz："if you fail to answer the whole question and only answer half of it, you will not get above band score 5 in task response" |
| 改写题干时错误频繁 | **LR ≤ 5** | Liz 原话："If you have frequent errors, you will get band score **5 or 5.5** in vocabulary"。★ 本表取 **5**（F54）：§3.1 穷举了合法半档，`LR` 一个都没有 ⇒ 封顶值写 5.5 会让 G3 阶段 2 断言 12 对着**正确行为**判 FAIL。两个值取低也符合 §5.2。 |
| 连接词机械（几乎每句开头挂一个 / Firstly-Secondly-Thirdly 套） | **CC ≤ 6** | Liz："Your use of linking words is mechanical, which is a feature of band 6" |
| T1 无 overview | **TA ≤ 5** | 官方 Band 5 描述符 "without referring to the bigger picture" |

### 3.4 📏 字数目标（不只是及格线）
- **T2 写 270–290 词**。Liz：`Band 5 = ideas are limited and not sufficiently developed` → `Band 7 = extends main ideas` → **"if you are aiming for band 7, you ought to be aiming for 270-290 words"**。低于 250 扣分；超过 ~320 会稀释焦点、也吃掉检查时间。
- **T1 写 165–190 词**。低于 150 扣分。

---

## 4. 相邻档的分界测试（可核查，不靠感觉）

### 5 vs 6
6 有的、5 没有的：**立场从头到尾能被读出来** + **段落切分成立** + **错误不让读者卡住**。
> 反例锚：ieltsanswers "免费大学教育"篇 LR 7 / GRA 7，但两个 body 段的 topic sentence 互相矛盾 → TR 3-4 → **总分 5.0**。语言好救不了立场崩。

### 6 vs 7 ← 她的战场
逐项对照，**7 必须四项都摸到**：

> 🔴 **本节【不许】重述任何阈值数字。** 阈值只有一处：GRA 见 §2.1 · LR 见 §2.2 · TR/TA/CC 见 §2.3d。
> 本节曾把 GRA 的 Band 7 门槛写成 35%（真值 50%），造成整整一档的分歧 —— 见 §2.1 的更正史。

| 项 | 6 的样子 | 7 的样子 | 定档程序 | 她的现状（2026-08-10） |
|---|---|---|---|---|
| TR | 各部分覆盖不均；主论点有但没展开 | 每部分都答到；论点 extended + supported | **查 §2.3d** | 6.5（勾 6/7） |
| CC | 连接机械/过度/遗漏；段落中心偶尔糊 | 逻辑清晰、进展明确、段落有效 | **查 §2.3d** | 6.0（勾 2/4） |
| LR | 词汇错密度中等 | 词汇错密度低 | **查 §2.2** | 6.0（K270 = 9） |
| GRA | 干净句率未过 Band 7 门槛 | 干净句率过 Band 7 门槛 | **查 §2.1** | 6.0（37.5%） |

**结论（这是判断，不是阈值，所以可以留在本节）**：
初版写的"她离 7 差的只是表层准确率、TR/CC 已经在 7"**已被实际考分 5.5 推翻**（见 §6.5）。
真实情况是**四项都在 6 附近**，权重排序 LR > GRA > CC > TR。**近期目标是 6.5，不是 7。**

### 7 vs 7.5/8
- GRA 干净句率进 **§2.1 的最高一行**（★ 二修 F56：原文这里写着"过 60%"，
  是一个只存在于本行、和 §2.1 四行都对不上的野生阈值 —— **写在"本节不许重述阈值"那句话的正下方**。已删。查 §2.1。）
- LR 出现自然的 less common / idiomatic 用法且用对（不是硬塞难词）
- TR 论点展开有深度，不停在 over-generalise
> 考官反例：`unnecessarily complex structures` 会被 **扣** CC —— "reading your writing causes me to feel frustrated"。**别为了上 8 把句子写复杂。**

---

## 5. 反虚高协议（🔒 硬规则）

1. **不数不判。** 每次给分必须先写出：总句数 / 干净句数 / 干净句率 / 词汇错个数。这三个数进 session 文件。
2. **两档之间取低的。** 6.5 和 7 之间犹豫 → 给 6.5。（注意：这和 `_examiner_protocol.md` 的"取高"方向相反 —— 那份是用来**压教练范文别超 Band 7**的，跟给她判分是两件事，别混。）
   > ⚠️ 这条是【查表结果 vs 硬顶】、【整档 vs 整档】之间的取低规则，**不是造半档的授权**。半档的合法来源穷举在 §3.1。
3. **限时才算数。** 未限时的分永远标 `(untimed)`，不进步曲线。40 分钟（T2）/ 20 分钟（T1）是分数的一部分。
   > **中文构思是否计时（模式 A 专用，F24）**：默认 **中文构思计入 40/20 分钟**（考场没有中文环节，不计就跟别的篇不可比）。
   > 她可以选"中文不计时"，那一篇标 `(zh-untimed)`：**照常判分、照常记错误档案，但不进 `bank.md` 进度曲线**（与 untimed 同待遇）。
   > ★ 这不是替她选交付形式（§5 是她的），只是给两种选择各自标好价格。
4. **查来源。** 只判她 cold 原稿。任何经过 Gemini/教练/语法工具修过的文本一律不判 —— 2026-07-12 那次就是把 Gemini 的改后稿当成她的 cold 判了 7 分，结论全错（见 `bank.md` 备注）。
   **★★ 出处问句必须【逐字】问出来，且必须问在【收稿的那一刻】（节点②），不许判完再补：**
   ```
   问   「这是你自己写完没动过的原稿吗？」
   记   把她的回答【逐字】抄进 session 文件
   判   回答 = "是 / 没动过 / 原稿"        → 正常判分，可进进度曲线
        回答 = 其它任何内容（改过一点 / 查了一个词 / 用了检查器）
             → 全篇标 `(edited)`，**照常判分但不进进度曲线**，且 📊 行必须带 `(edited)`
   ★ 这一条的违反史就是 2026-07-12：不是没规则，是规则写在判分节点、而唯一能问的时点在收稿节点。
     ⇒ 现在它是 **G2 收稿闸的断言 1**，问不出答案就 BLOCK，不许往下走。
   ```
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
- 语法错：`an ageing population put massive burden`（主谓+冠词）· `With ages growing`（悬垂）· `most parents have to overtime`（词类）… 约 15 句里干净 3–4 句 → **~23%** → **查 §2.1**，落在最低那一行；回读句 2 句（`the leaving school time of students is usually before 5pm` / `With ages growing`）⇒ 杠杆生效 → **GRA 5.5**
  > ⚠️ 二修（F56）：原文这里写的是「→ 低于 50% → GRA 6.0；但…→ GRA 5.5」。
  > "低于 50%" 是本文件明令禁止的野生阈值复述，而且它给同一篇文章推出的 6.0 **与 §2.1 历史核对表里这一行自己写的 5.5 直接打架**。已改成查表。
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

> ⚠️ 本模板是 **G3 这一个独立 pass 的产物**，内含两个有序阶段（阶段 2 在阶段 1 全部写完后才开始）。
> 输入输出契约见 `SKILL.md §G3`。符号一律用 `SKILL.md §9.2 符号总表`，本文件不另立符号。
> **2026-08-10 二修**：原来是 G3a / G3b 两个 subagent。合成一个 —— 要防的 anchoring 是
> 【教练自己的上一个数】，subagent 从头到尾没见过它，内部先数后判是正常顺序，不是 anchoring。
> ★ 证据块尺寸受 `SKILL.md §3.3` 约束：**A1 不许逐字重引原句**（G2 已经贴过一份带 S# 的全文）。

```
## Marking — [题号] [题型] · [timed | untimed | zh-untimed] · [(edited) 若适用] · [词数] words

### 阶段 1 · 计数复算（输入只有：G2 那份带 S# 的原文 + scoring.md §2 + 六层/七条清单。不许看任何已提出的分）
#### A1 逐句表（**每句恰好一行；「句」列只写 S<n>，不重引原句**）
| S# | 干净? | 错在哪（命名） | 桶 GRA/LR | 回读句? |
|---|---|---|---|---|
（S1…Sn 一句不漏，连续无跳号）
- 总句数 N ＝ __  ｜ 干净句 M ＝ __  ｜ **干净句率 = M/N = __%**
- 回读句：S__ , S__ （共 __ 句）        ← 不列就不许用 §2.1 的 −0.5 杠杆

#### A2 词汇错逐条（原文片段 ≤6 词）
| # | 原文片段 | 子类（拼写/词形/词义/搭配/中式块） | 改法 | 双计? |
|---|---|---|---|---|
- 词汇错 K ＝ __  ｜ 词数 ＝ __  ｜ **K270 = K ÷ 词数 × 270 = __**
- 形近/错词【种类】数 ＝ __（§2.2 的 Band 5 触发条款按种类数，与 K 的实例数计法相反）

#### A3 桶归属自查（§2.0）
- 每个错都恰好落在一个桶里？ 是/否　　双计的条目：__（必须逐条列出理由）

#### A4 六层诊断（SKILL §6.1，**每层一行，没问题写 `—`**；层5/层6 用本题型那一套）
| 层 | 结论 |
|---|---|
| 1 表层准确 | |
| 2 词与搭配 | |
| 3 句子结构 | |
| 4 衔接与段落 | |
| 5 （T2 论证质量 / T1 数据忠实） | |
| 6 任务达成 | |

#### A5 理解侧冗余七条（SKILL §6.2，**各一行**，命中指到 S<n>，没命中写 `—`）
1 修饰语紧贴 __ ｜ 2 并列同形 __ ｜ 3 分词逻辑主语 __ ｜ 4 比较对象对齐 __
5 时态同一平面 __ ｜ 6 代词唯一 __ ｜ 7 关系从句紧贴先行词 __

### 阶段 2 · 判档复算（阶段 1 全部写完之后才开始。不许看任何已提出的分）
#### B1 四项定档（每行必须【逐字引用查到的那一行表格】）
| 项 | 读到的表格行（逐字） | Band |
|---|---|---|
| TR/TA | | |
| CC | | |
| LR | | |
| GRA | | |

#### B2 清单整表（§2.3d，勾到与没勾到都列，各带证据句）
| # | 清单项 | 是/否 | 证据句（原文） |
|---|---|---|---|
→ TR/TA 勾 __/__ → 查表 __ ｜ CC 勾 __/4 → 查表 __
（★ 这一列的「是/否」不是 §9.2 的判定符号，不进任何 streak）

#### B3 硬顶逐条（§3.3 表的**每一行**，一行不许省；T1 另加 anchors.md §9.8 的 7 条）
| 触发条件 | 触发? | 证据 | 封顶 |
|---|---|---|---|
→ 硬顶封顶值 __ ｜ 与 B1 取低后 = __

#### B4 总分算术（写出算式）
(TR __ + CC __ + LR __ + GRA __) / 4 = __ → 取最近 0.5（.25/.75 向上）→ **__**
半档来源（§3.1 哪一条）：__      ← 写不出来 = 该半档非法

#### B5 四问自审（每个 ❌ 逐条过，§5.6）
（① 能否推翻自己 ② 是否延续上一条 ③ 判的是哪一层 ④ 假错比漏错贵）

#### B6 靶子内 / 靶子外
- 靶子内：<代号> ✅/❌ …
- **靶子外出现**：<代号> × n …（n = 该代号在本篇出现的【实例数】，不是句数）
  ★ 字段名 2026-08-10 二修（F58）：原名「靶子外复发」与 `SKILL 定义5` 的「复发」是**两个不同的量** ——
    定义5 是【同题相邻两次限时 cold 都出现】的代号级判定，本字段只是【本篇出现了几处】。
    一名两义 ⇒ `G6 断言 6` 无法求值。**「复发」一词从此只归定义5，本字段叫「靶子外出现」。**
- **全篇干净率 __% ｜ 靶子外干净率 __%**（两个都要报，见 SKILL §6.5；基线篇写 `n/a`）
- 桶和：靶子内错 __ + 靶子外错 __ = 总错 __

### What moved since last attempt on this question
(new / fixed / relapsed)

### Errors  ❌ 真错 · ⚠️ 不地道（她的也成立，可否决）
| S# | Your sentence | 档 | Type | Fix |

### Clean version
(her text, minimally corrected — 不重写，不升级词汇；★ 必须整篇，见 SKILL §7)

### One thing to carry into the next essay
```
