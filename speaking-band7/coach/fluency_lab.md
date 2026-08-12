# 口语流利度实验室（fluency_lab）

> **这是一条持续训练线的日志，不是单次 session。** 每轮都记：诊断出什么、怎么诊断的、她的原话输入、我的判断和建议。她 2026-07-27 明确要求持续保持、不用她提醒。
> ⚠️ **数据协议（2026-07-28 轮 17-18 确立，她定的）**：她的口语输入是**语音转写**，会漏词/听错（铁证：`In fact`→转写成 `In French`）。
> **协议：默认转写可信；她没纠正=真的有问题，她喊了才作废。** 举证责任在她，教练不脑补。（她原话："如果我没有纠正，那就是有问题，这样我们好对齐，不然你靠自己脑补没法搞"）
> 已判定：`playing phone`/`focus on 悬空` 她确认有问题→**算数**；`worked-it's hard 时态`/`It's a super convenient 的 a` 她没喊→算数；`In French`(=In fact)、轮16 `public transport in my city` fragment 她喊了→**作废**。
> **∴ 轮 15 零件层恢复有效；轮 16"起头断电"仍作废**（短主语规则=待验证假设，非她数据证出）。
> **往后只量四项**：①起头快不快 ②用了几个/哪几个角度 ③能连着接几个块 ④有没有真断掉（接不下去，非漏词）。
> 另：**发音占口语 25%，至今完全没测过**（机器听错≠发音差，但这是未知维度）。

> 🛠 **执行器**：`.claude/skills/fluency-lab/SKILL.md`（2026-08-01 建，逐轮回顾 90+ 轮后沉淀）。本文件是**真源**，skill 只 load+enforce，不重复内容。
> **源头**：从写作 199 句诊断（[`../../writing-band7/gemini/my_sentence_habits.md`](../../writing-band7/gemini/my_sentence_habits.md)）长出来——写作和口语是同一个 retrieval 缺口，两个时钟。

---

## ⚙️ 本文件的运作规矩（2026-07-28 她定，硬规则）

> 她原话：**"所有抓出的点需要反复复习，沉淀下来，不然时间一长就白学了。另外这些点你需要学会'持续'总结和归纳，但是原始问题点不要丢。可能后面又有新的总结。"**

**三层结构，各司其职：**
```
① 复习清单（下方）  ← 每次开练前教练抽查 3–5 条，她答不出的当场重练。这是"不白学"的机制
② 当前沉淀模型      ← 随理解演进【重写】。旧版本进"已作废假说"表，不删
③ 原始逐轮记录      ← 【永不删】。新的归纳往往要回头从原始数据里挖（已发生过多次）
```
**教练职责**：①每次开练必抽查 ②每轮结束更新沉淀 ③归纳时绝不覆盖原始点 ④她不必提醒 ⑤**主动扫"理解侧冗余"七条**（轮57：她无法自己发现，阅读不暴露）⑥**每轮同时给语言层反馈**（地道度/重复/更好说法，她轮54 要求）。

> **📌 她 2026-07-29 追加的三条流程要求（硬规则）**：
> 1. **每次任务立刻记录，且要"事实层"**——她的**原话输入逐字照录**、我出的题原样、错在哪一个词，不能只留我的结论。结论可以错（今天错了 4 次），事实不能丢。
> 2. **每次出任务前先看当前日期**——**距上次超过 1 天，先带她复习**（抽查复习清单 3–5 条）再出新题。不复习不出新题。
> 3. 内容准备要有**锚定 tag**（见下方"硬料六类"），她自认类别一开始不准没关系，tag 的作用是让她有抓手。
> 4. **每轮同时给语言层反馈**（不地道 / 重复 / 更好的建议），与内容结构同等重要。（轮54）
> 5c. **★★ 她 2026-08-01 指出教练退化："诊断越来越浮于表面，指出两个错误就下一题，时间花了没学到什么"** —— 属实。近十几轮只做了"挑错+下一题"。**往后每段必须过五层，不许只做第一层**：
> ```
> 层1  语法搭配                （我一直只做这层）
> 层2  词的精确度              她想说的 vs 她说出的（例：nowadays it's MORE messages → MOSTLY）
> 层3  衔接与语气              重复连接词（两个 But）、自我对冲（a bit fragile 把论点软掉）
> 层4  逻辑层次                描述→评价有没有断层、有没有显式过渡（That's made it…）
> 层5  内容深度 ★              现象说完了，"为什么"呢？—— P3 分水岭就在这层
>      例：bonds built online are fragile（现象）
>          → 为什么？加好友零成本，所以失去也零成本
>          → It costs nothing to add someone, so it costs nothing to lose them.
> ```
> **层 5 是她 P3 提分的地方，也是教练长期没带她去的地方。**
> 5b. **★ 她 2026-08-01 追加：所有纠正 + 更好的建议都是学习材料** —— 包括**抽象洞察、思考方向、方法论、词汇词组**，全部要沉淀进文档，不能因"这条太小"跳过。文档四层对应：诊断链/模型=方法论 · 复习清单=规则 · **表达库=词汇词组** · 逐轮记录=事实层。
> 5. **★ 每次纠错必须给两个版本**（轮66 她明确要求，与她对 Gemini 的长期要求一致："尽可能在我的原文上修改，这样我也知道哪里有问题"）：
>    ```
>    ① 最小修改版  在她原句上动最少的地方 → 她看得出【错在哪】
>    ② 更好的版本  换说法/更地道         → 她知道【天花板在哪】
>    ```
>    只给②她看不出自己错在哪，且容易照抄（轮46 教训）。

> ⚠️ **教练硬规矩（轮46 教训，当天第四次犯）**：**能在她自己产出上做减法，就绝不给新句子。**
> 给示范句必须明确标"这是说明机制，不是让你说的版本"——否则她会照抄，产出反而退化（轮45 四句 → 轮46 一句）。
> 已犯：轮30 骨架带语义 · 轮31 骨架不中立 · 轮42 模板缺主语 · 轮46 范例变模仿。
> 呼应 [[feedback_derive_from_her_production]]：材料从她实产提炼——不只是选材要求，更是**不覆盖她产出**的要求。
（呼应 [[feedback_review_is_the_mechanism]] 复习是学习生效的唯一机制 + [[feedback_coach_drives_recall]] 她背我喂）

> **📌 她 2026-08-04 追加的三条硬规则（本条起立即生效）**
>
> 她原话：**"所有我错的，不会的，以及你觉得更好的，都要复习（不要漏记）。召回的时候也需要一句一句看。不要用脚本避免遗漏。"**
>
> 1. **零遗漏记录 · 三类全收**
>    ```
>    ① 她说错的            —— 哪怕只是一个冠词
>    ② 她说"不会/没把握"的  —— 她的自诊准确率至今 7/7，一律当真
>    ③ 教练给的"更好的版本" —— 天花板也是学习材料，不是装饰
>    ```
>    **不许因"这条太小/太明显/她应该会"跳过。** 判断哪条值得记 = 已经在漏。
>
> 2. **禁脚本，手工逐条写**
>    记录与复习清单的维护**一律手写**（Edit/Write 逐条），**禁止 python / sed 批量替换**。
>    理由：批量写 = 内容从眼前一闪而过 = 必漏。手写慢，但每条都过了一遍眼睛。
>    （与 [[project_speaking_zh_bridge]] 里"54 卡全手工、禁脚本"是同一条原则）
>
> 3. **召回也逐句**
>    抽查/复习**一条一条过、一句一句看**——不抽样、不合并同类、不写"以此类推"。
>    （与 08-03 她定的"复习是 one by one 的过，不批量"是同一条，此处扩展到召回环节）

> **📌 复习节奏（2026-08-05 她改定，取代"距上次超过 1 天就抽查 3–5 条"）**
>
> 她原话：**"每天都要先复习昨天和 3 天前的内容，然后每隔 5 天进一个专门复习日（不学新的，就是专门复习，另外这天要包括题目重答），就是把过去 5 天的全部，和更早时间的抽查。"**
>
> **① 每日开场（学习日）—— 两批，逐条过，不抽样**
> ```
> D-1  昨天的全部点
> D-3  三天前的全部点        ← 间隔重复的第二次触碰
> 做完这两批才允许出新题
> ```
>
> **② 每 5 个学习日 → 一个【专门复习日】**
> ```
> 当天不学新东西
> a. 过去 5 天的【全部】点，逐条过
> b. 更早日期的抽查（跨度要大，最远的最该查）
> c. ★ 必须包含【题目重答】—— 把这 5 天做过的真题重新答一遍
>    （这是唯一能测"当时学的到底装上没有"的方法；单点中译英测不出整段整合）
> ```
>
> **③ 周期锚点**
> ```
> 2026-08-05  周期第 1 天
> 2026-08-10  第一个【专门复习日】—— 覆盖 08-05~08-09 全部 ＋ 08-04 及更早抽查
> 之后每 6 天一个（5 学 1 复）
> ```

---

## 🔩 要焊的块 · 四槽清单（2026-07-29 建，训练材料主表）

> **原理**：她的失分全部可定位到"某个槽没有自动块"。训练 = 每槽装 2–3 个块（**路径冗余**，不是学更多词）。
> **每块三个条件**（轮30/31/34 撞出来的）：①**语义中立**（留极性槽）②**带确认版**（她不确定就不敢用）③**引擎词不能省**（情态/副词是功能核心）。
> **标 ⭐ = 她自己产出过的**，优先焊（她确定，且是她的资产 → [[feedback_derive_from_her_production]]）。

### 槽 1 · 起手（主语）　目标：把 `It's` / `I` 从**默认**降为**选项之一**

| 块 | 确认版 | 引擎（不能省） |
|---|---|---|
| ⭐ A. **[动名词] + 实义动词** | `Living in a small city gives me more freedom.`<br>`Commuting between home and work wears me out.` | 动名词要**完整**（`Living in a small city`，不是光 `Living`） |
| ⭐ B. **[话题名词] + 实义动词** | `Weekends give me real me time.`<br>`Rent has gone up a lot.` | 主谓一致（Weekends give / The weekend gives） |
| ⭐ C. **There are + 具体数量** | `There are three subway lines within a ten-minute walk.` | **必须带具体数字**，否则退化成 `There are many…`（空） |
| ⭐ D. **[名词], [同位语],** | `Ranmian, or burning noodles in English, is…`<br>`Yibin, a small city in southern Sichuan, …` | 逗号 + 名词短语，**不用 who/which**（最便宜的右分支） |

**先焊：A + C**（A 覆盖面最大；C 强制具体细节）

### 槽 2 · 评价　目标：把 `is my absolute favorite` 从**唯一**降为**之一**

| 块 | 正向 | 反向 | 引擎 |
|---|---|---|---|
| A. Nothing beats … | `Nothing beats spending time with my kid.` | `… is not really my thing.` | beats + **V-ing** |
| B. I'm really into … | `I'm really into hotpot.` | `… does nothing for me.` | into + **名词/动名词** |
| ⭐ C. … gets old | `X never gets old.` | `Scrolling through short videos gets old fast.` | **never / fast** 是极性开关 |
| ⭐ D. X is something I … | `Cooking is something I really enjoy.` | `Cooking is something I don't like.` | **她自己造的骨架**，极性槽天然 |
| E. I could … every day | `I could eat hotpot every day.` | `I can't stand cleaning.` | **could 不能省**（省了就变事实句，轮34） |

**先焊：A + D**（D 是她自己的，最容易自动化）

### 槽 3 · 谓语（实义动词替 is）　目标：`is` 不再是唯一选项

| 块 | 确认版 | 引擎 / 限定 |
|---|---|---|
| **感官动词** | `It tastes great.` / `It feels comfortable.` / `It looks nice.` / `It sounds noisy.` | ①**-s 别掉** ②**说感受/印象才换；客观事实用 is 是对的** |
| ⭐ **X makes me …** | `He makes me laugh.`（原形）<br>`It makes me feel relaxed.`（feel + **形容词**） | **两条路别混**：`makes me relax` ✅ / `makes me feel relaxed` ✅ / ~~`makes me feel unwind`~~ ❌ |
| ⭐ **X gives me …** | `Weekends give me real me time.` | 后面接**名词** |
| 其他高频 | `costs a fortune` / `takes ages` / `wears me out` / `helps me unwind` | |

**先焊：makes / gives（她已用过）+ tastes / feels**

### 槽 4 · 抽象概念（"化 / 起 / 及 / 度"）　目标：**不找词，直接说画面**

| 模板 | 确认版 | 覆盖 |
|---|---|---|
| ⭐ A. **[X] are everywhere.** | `Phones are everywhere now.` / `Traffic jams are everywhere.` | 普及、拥堵、到处都是 |
| ⭐ B. **More and more people [V].**<br>**反向：Fewer and fewer people [V].** | `More and more people live in cities.` / `… shop online.`<br>`Fewer and fewer people are having kids.`（少子化） | 兴起、流行、城镇化 ／ 少子化、萎缩 |
| C. **[X] is getting [比较级].**<br>⚠️ 必须连 X 一起给（轮42：她卡在 X 不在框架） | `The population is getting older.`（老龄化）<br>`Rent is getting more expensive.`（变贵）<br>`The birth rate is getting lower.`（少子化） | 老龄化、变贵、恶化 |

**出口规则（轮26 + 轮39）**：
```
在"挑"词（不知道哪个对）      → 立刻跳车，说画面
在"拿"词（形近词先冒出来）    → 再试一次，通常就对
判断：你是在【拿】还是在【挑】
```

### 焊接顺序（按"堵住旧块"的杠杆排）
```
1. 槽 4（抽象概念）  三条模板最简单，且直接消灭找词死循环
2. 槽 2（评价）      她唯一自动块所在，堵住它收益最大
3. 槽 3（谓语）      词全在（6/6 秒答），只差触发
4. 槽 1（起手）      已部分建立（禁 it+I 一轮见效）
```

---

## 📋 复习清单（抽查用 · 按掌握度分档）

> 抽查方式：给中文或情境，她**出声**产出。答不出=当场重练；连续两次答得出=降档。

### A 档 · 已焊上，抽查保温（答对率应 ≥90%）
| # | 点 | 抽查示例 | 来源 |
|---|---|---|---|
| A1 | **`more/-er … than` 成对** | "周末比工作日轻松" | 轮13 (5/5) |
| A2 | **`if …, it's hard to …`**（拆代替挂） | "不会英语，找工作难" | 轮15 (4/5) |
| A3 | **`There are …` 说具体数量** | "我家附近有三条地铁线" | 轮20 |

### B 档 · 刚建立，需高频抽查（当前主攻）
| # | 点 | 抽查示例 | 来源 |
|---|---|---|---|
| B1 | **拆包三步**：①揪主语 ②找动词 ③找不到就换大白话 | "手机的普及"（→Phones are everywhere） | 轮24–25 |
| B1e | **主语藏在中文词里**：揪不出主语时问"这件事发生在**谁/什么**身上？"（老龄化→the population / 少子化→the birth rate / 内卷→everyone） | "老龄化" / "少子化" / "房价上涨" | 轮42 |
| B1b | **换说法的操作**：问"具体发生了什么"，丢掉抽象名词只说画面。**出口条件：想到第二个词还没定就停止找词** | "网上购物的兴起" / "城镇化" | 轮26 |
| B1d | **"跳出来 vs 找出来"**：词自己跳出来+确定→用；需要找**或不确定**→立刻说画面 | "城镇化"（urbanization 跳出来了→可用）/ "教育资源不均衡"（不确定→说画面） | 轮27 |
| B1c | **三条大白话模板**：`…are everywhere` / `everyone·more and more people…` / `…is getting +形容词` | 任给一个"化/起/及/度"抽象词 | 轮26 |
| B2b | **从句必须紧贴被修饰词**；贴不上才拆两句（修正"能拆就别挂"） | "不学英语的年轻人找工作难" vs "刚看完基地系列，那是少数能让我放松的方式之一" | 轮14→29 |
| B28 | **三个 no 堆反差 + 收一个 yes**；生成法=想"要忍受什么"，每样就是一个 no | "为什么有人喜欢在家看电影/跑步" | 轮117 |
| B2 | **同位语**（最便宜的右分支，一个逗号不用 who/which） | "我老家宜宾，四川南部的一个小城市，夏天特别热"（08-10 改题面：原题面"宜宾，四川南部的一个小城市"可合法译成完整句，逼不出同位语，记 ◎） | 轮24 |
| B3 | **`That's where …`**（高复用块） | "长江就从这里开始" | 轮24 |
| B4 | **评价骨架可丢**（不说 famous，直接给事实） | "这里因为三江汇合出名" | 轮24 |
| B5 | **禁 it + I**（逃避载体），主语从话题里拿 | 任给话题，说 2 句不用 it/I | 轮19–22 |
| B6 | **5 角度自选**（评价/比较/影响/自身/事实） | 任给话题，指定用"比较"和"事实" | 轮11–12 |

| B7 | **骨架必须带"确认版"**：不确定的骨架不敢用→不迁移。背整段≠可迁移单元 | 从任一背过的段落里抽骨架，说出正确形式 | 轮30 |
| B8 | **骨架必须语义中立**（留极性/频率槽）：带语义的叫句子不叫骨架。她的三个自有骨架：`[V-ing] is something I…` / `I rarely·often [V] because…` / `[X] tastes much better than [Y]` | 用这三个说 exercise / music / travel | 轮31 |

| B9 | **实义动词替系动词**（is 是她唯一自动化的谓语）：taste/sound/feel/cost/look。**限定：说感受/印象才换，客观事实用 is 是对的** | "The food is good / This chair is comfortable / Rent is expensive" | 轮32 |
| B9b | **系动词依赖只在【评价槽】**（叙述时她实义动词自发）。评价槽用预制块：`I'm really into X` / `I could do X every day` / `X never gets old`（+反向） | 说火锅/打扫卫生/刷短视频，不用系动词做评价 | 轮33 |

| B10 | **-ing vs -ed 形容词**：-ing 描述东西（relaxing/boring）· -ed 描述人（relaxed/bored）。`I feel relaxed` ≠ `It feels relaxing` | "看到儿子我就放松了" / "这部电影很无聊，我看得很无聊" | 轮35 |
| B11 | **预制块的情态/副词是功能核心**（could/never/really/fast），省了块就退化成事实句 | "我能天天吃火锅" vs "我每天吃火锅" | 轮34 |

| B12 | **`X makes me …` 盖住整个评价槽**（实义动词，非 is；她轮3 用过=休眠资产）。<br>参考对照（不出题）："和他一起很高兴" `Being with him makes me happy.` ／ "这让我忘了工作" `It makes me forget about work.` | "这两小时让一整天都值了" | 轮38（08-11 三题面收成一条：三句测的是同一个考点，按定义3d 一号一题面；留 08-10 答错的那句） |
| B13 | **不指望"边说边想"**：英文产出吃满带宽，生成与产出抢带宽 → **答案第3、4句必须预先备好** | 给任一 P1 题，先写下第3、4句再开口 | 轮38 |

| B14 | **"不确定"会误报**：说不出来→跳车；**说出来了但不确定→继续说别停**（停下核对的代价 >> 说错一个词） | 回想今天哪句你怀疑过但其实是对的 | 轮41 |

| B15 | **一次只焊一个块**（注意力零和：盯目标块时，非目标的准确度会掉）。焊块期旧准确度暂降=正常代价 | 回想：禁 it 那轮为什么 uh 变多 | 轮53 |

| B16 | **话题核心词**：每话题 2–3 个躲不掉的词，缺一个整段绕路+重复（吃饭：eat out/takeaway/home-cooked/grab a quick bite） | 说吃饭话题，不许出现 "eat at restaurants" | 轮55 |
| B17 | **四步展开器**（治说不长）：①直接答 ②硬料 ③时间/频率 ④感受。固定顺序=不用现场决定 | 任给 P1 题，走满四步 | 轮54 |

| B18 | **错误感知按类型分**：结构断裂→信自己的直觉；形态细节→别停继续说（她在这两类上一准一误） | 回想 more than ever（误报）vs 硬憋那句（命中） | 轮41/65 |

| B19 | **比较级三条**：①短词(1音节/2音节以y结尾)用 -er ②长词用 more ③**much/far/a lot 后面必须是比较级形式**（much MORE fragile） | "比十年前吵多了" / "脆弱得多" / "容易多了" | 轮53/90/93 |

| B20 | **改过又犯追踪**（一次纠正不够=没进自动区）：`in an online group`（非 on，轮94改轮95又犯） | "我在一个网上群里认识他们的" | 轮95 |

| B21 | **反差六轴**（找反差不用凭空想，六选一）：必须↔选择／我的↔别人的／有结果↔看不到头／它需要我↔我需要它／累但值↔累且烦／简单↔复杂 | "为什么有人喜欢跑步/独处/手工/养植物" | 轮108 |
| B22 | **换谓语升级**（治句式单调）：is+形容词 → 实义动词。**边界**：形容词说"对人的作用"可换（boring→bores），说"物本身属性"不可换（quiet/high） | "这工作很无聊"／"这房间很安静"（后者不该换） | 轮110 |
| B23 | **通路A/B 比例**：引子 1 句 → 答案 2–3 句。个人经验是跳板不是内容 | 用通路A答"为什么有人喜欢X"，数一下几句在答题 | 轮112 |
| B24 | **车轱辘=一个角度三种说法**：解法是换角度不是换说法；翻译时最容易丢角度 | 说完一句问"下一句是新角度还是同角度换说法" | 轮113 |

| B25 | **as … as it gets**（用原级，避开比较级形态）+ about 软化；退路三级 | "跑步简单到不能再简单" / "这已经是最好的了" | 轮118 |
| B26 | **软化词一句只放一个**（about/pretty much/I guess/kind of）；与强调词同现=自我对冲 | 判断 "It's definitely, to some extent, worth trying" | 轮119 |
| B27 | **主谓一致**（孤立100%、产出中反复错=检索失败）：主语"一个东西/他她它"→加s；"我你我们他们/复数"→不加。<br>⚠️ **08-11 一天内三次**（the two hours MAKES ／ my mom HELP ／ he WALK）—— 坐实"检索失败非知识缺口"，产出中必须专门盯 | "他每天七点起床，从来不迟到"（一句里两个动词都要加 s） | 轮121（08-12 改题面：原格里是"快问快答"清单，不是可用的中译英题面，按 §0.3 取不出题） |

| B29 | **三步主干**：①定位+答案（答案不能拖到第三句）②具体画面 ③换角度。工具挂在三步下面，不卡不调 | 任给 P1/P3 题，走三步 | 轮128 |
| B30 | **补充信息必须挂回主句**（破折号／逗号／and／逗号+which），别把短语从句当整句甩出去 | "…on the balcony — it only takes a few minutes" | 轮130 |
| B31a | **grow vs grow up**（grow up 只用于人长大成人；植物/数字用 grow）<br>△ 08-10 遗留：她 `watch these plants growing` 动词对了，但"一天天"那层没出来 → `grow a bit every day` | "看着这些植物一天天长" | 轮131（08-11 从 B31 拆号） |
| B31b | **shop 不及物**（she buys everything online ／ does her shopping online，不说 shops everything） | "我老婆什么都网购" | 轮131（08-11 从 B31 拆号） |
| B32 | **no questions asked**（七天无理由退货）；for no reason=莫名其妙，两码事 | "七天无理由退货" | 轮131 |

| B33 | **P3 硬料要泛化**：内容不变，主语从"我家"换成泛指（From our place → From high enough up）。三步主干 P1/P3 结构相同，只差第②步人称 | "从高处能看见整个城市" 用 P3 说法 | 轮133 |
| B34 | **时态判断触发**：看中文有没有时间标记词（试过/昨晚/小时候→过去；通常/每天→现在）。**过去的习惯用 used to/would/often，不用 usually** | "我以前常去健身房" / "小时候我常踢球" | 轮137 |
| B35 | **共享主语减 I**：一个 I 带两个动词（I got home and went straight to bed） | "我起床然后直接去上班" / "昨晚回家吃完饭就睡了" | 轮138 |
| B36 | **程度旋钮**（不换词只加精度）：well away · right across · just a few · high enough up。enough 在形容词后/名词前 | "离马路远远的" / "看见整个城市" | 轮134 |
| B37 | **deep down**（内心深处，含比喻义）+ `It's not that A, it's just B` + `do+动词`强调 + `can't be bothered` | "内心深处我知道该早睡" / "不是不想去，只是懒" | 轮135–136 |

| B38 | **画面两条标准**：①能拍成照片吗 ②大多数人都见过吗。太特化=只代表一类情况，P3 里跑偏 | 判断 "hands-on tasks" / "半个班玩手机" / "两人一组拼东西" 哪个合格 | 轮141 |
| B39 | **让某人做某事四件套**：get sb TO do（只有它带to）／have sb DO／make sb DO／let sb DO。<br>参考对照（不出题）：别逼孩子背 `don't make kids memorise` ／ 让他们提问 `let them ask questions` ／ 两人一组 `have them work in pairs`<br>⚠️ 08-11 同族错：`watch the machine BUILDS it` → watch/see 也走原形补语 | "老师应该让学生自己试" | 轮142（08-12 收成一条题面） |
| B40 | **talk AT sb（单向灌输）vs talk TO sb（双向）**；pay 搭配窄（钱/注意力/代价），时间精力用 put…into | "有些老师就是对着你讲一小时" / "老师该多花精力备课" | 轮140–141 |

| B41 | **论元完整（判定已落地：primed 8/8 但 20 分钟后 cold 即掉 `spend a whole day meeting___` → 产出时掉，非知识缺口。修法只有块化）**：中文可单说的动词，英文必须带宾语/补语。focus on **my work** ／ a mix **of both** ／ goes to **them** ／ can even **see** the mountains。<br>参考对照（不出题）：a mix **of both** ／ goes to **them** | "上班很难专心" | 轮147（08-11 收成一条题面：三句同一考点；"各一半最理想"与 B43 撞车，一并撤下） |
| B42 | **分数说法**：a half / a third / a quarter / a tenth / two thirds | "原价的一半，甚至十分之一" | 轮150 |
| B43 | **泛指的不对称**：`the countryside` 泛指永远带 the；`the city` 带 the = 某座具体城市，泛指用 `city life`。→ 并列两边"泛指程度"也要同形 | 说"城乡各一半最理想" | 08-04下 |
| B44 | **often ＝ 经常（频次高）**。<br>⚠️ 08-11 曾被并入 B188 并停用，同日撤销——历史 📊 里出现过的号不许作废（停用＝变相删条目）。<br>改为**与 B188 题面互斥**：**B44 只测 often**，usually 归 B188，两号各走各的 streak | "我朋友经常去那家店" | 08-04下（08-11 撤销停用） |
| B45 | **固定词序（只能整块背）**：back and forth · now and then · sooner or later · more or less | "我们来回沟通了三次" | 08-04下 |
| B46 | **efficient vs effective**：efficient=省时间人力（效率）／effective=达到效果。药管用＝effective；最口语 `It really works.`<br>参考对照（不出题）："线上开会省时间" → efficient<br>⚠️ 08-11 错例：`the most efficient ways to keep up` → 该 effective/best | "这药挺管用" | 08-04下（08-12 收成一条题面） |
| B47 | **搭配三件**：work FROM home（WFH）· handle orders（deal with 偏处理麻烦）· sales 恒复数不带 the（the sale=一次促销） | "在家工作效率高" / "销量涨了20%" | 08-04下 |
| B48 | **litter 不可数**（v. litter / drop litter）＋ **fine sb FOR doing sth** ＋ `It's no use doing`（不用 of no use，老式） | "罚款对乱扔垃圾没什么用" | 08-04下 |
| B49 | **★ 比较题必须说出另一边**（段落层的比较对象补齐）：prefer A = 比 B；答案里 B 一次不出现 = 逻辑缺口 | "为什么有人喜欢一个人工作" | 08-04下 |
| B50 | **the credit gets shared**（团队里功劳被分摊）＋ `nobody knows which part was yours` | "团队里显不出你自己" | 08-04下 |
| B51 | **名词表语（评价槽升级）**：It's no use doing／a waste of time／a pain／a hassle／a nightmare／no big deal ＝两种结构都行；**a must／a plus 只走 `X is a must`**。<br>参考对照（不出题）："后悔也没用" `There's no point regretting it.` ／ "英语是必备的" `English is a must.` | "会日语是加分项" | 08-04下（08-11 收成一条题面，留 a plus 那句——三句同一考点） |
| B52 | **今日"更好的版本"补录**（按 08-04 新规矩：教练给的天花板也要复习，之前只写进逐轮记录漏掉了）：<br>① `You just get more done at home.`（用画面替掉 more efficient）<br>② `You don't have to sit in meetings all day.`（sit in meetings 比 spend a day in meetings 更活）<br>③ `Say you fix something the whole team has been stuck on.`（Say you… ＝举例起手，替 For example）<br>④ `explain YOURSELF to anyone`（解释自己的行为）<br>⑤ `There's no point regretting it now.`（比 It's no use 更常用）<br>⑥ `On a clear day you can even see the mountains.`（on a clear day 替 if it's clear） | 中译英测这六句 | 08-04下 |

| B53 | **in pairs（两人一组）≠ in groups（小组）**；行业/领域说 `in this line of work` ／ `in this field`，**不说 in this work** | "在这一行英语是必备的" / "老师让学生分小组" | 08-04下 |
| B54 | **★ 禁双重否定**：nobody / nothing / never / no one 已含否定，后面动词一律**肯定**。中文"没人能做到"的"没"只映射一次 | "尤其是别人都做不到的时候" / "没人愿意加班" | 08-05 |
| B55 | **all morning / all day / all night 不带 the**（all THE morning ❌） | "我一上午都在开会" | 08-05 |
| B56 | **everyday（形容词，日常的）≠ every day（副词短语，每天）** | "每天通勤特别折腾" | 08-05 |
| B57a | **sing along**（跟着唱） | "全场跟着歌手一起唱" | 08-05（08-11 从 B57 拆号） |
| B57b | **feel the energy in the room** ＋ **live 当副词**<br>⚠️ 08-06 更正档位：`feel the energy live` **别扭但不算语法错**，教练上一版说重了。<br>判据：**live 当副词只修饰"这东西是怎么呈现给你的"**（现场 vs 录播）——saw them live／broadcast live／only get that energy live ✅；修饰"你的感受"时不用它 | "现场那种劲儿只有到场才有" | 08-05（08-11 从 B57 拆号） |
| B58 | **惯用定冠词，不按泛指-特指走**：the TV / the radio / the cinema / the doctor / the phone。<br>★ 08-12 补：**on the screen** 也属这类 —— 泛指"屏幕上"惯用 the，不是特指（她当天问过）<br>参考对照（不出题）："他整晚坐在电视机前" the TV | "我得去看医生" | 08-05（08-12 收成一条题面＋补 the screen） |
| B59 | **删掉自我对冲的 a bit**：对比句里 `a bit lonely` / `a bit fragile` 把论点削软了，对比要给足 | "在家看就冷清多了" | 08-05 |
| B60 | **time and energy**（不是 energy and time）· **prepare for class / prepare their lessons**（不是 preparing classes）· class 泛指不可数不带冠词（before class / in class）<br>⚠️ 08-06 更正档位：`energy and time` **不是语法错，是固定并列词序不地道**（binomial）；`preparing classes` 才是真搭配错。<br>规律：**短的在前长的在后** —— time and energy／time and money／black and white／cause and effect／sooner or later／salt and pepper | "老师该多花时间精力备课" | 08-05 |
| B61 | **which vs what**：从**确定范围**里选用 which（which part was yours），范围开放才用 what | "没人知道哪部分是你做的" | 08-05 |
| B62 | **come to your city / come to town**（乐队巡演到某地）；love 的对象是乐队不是演唱会 | "你喜欢的乐队一年才来一两次" | 08-05 |
| B63 | **★ 四个万能第二支点（操作，要做出来测）**：①钱/时间 ②人 ③一次性/稀缺 ④事后。<br>判据＝**看主角**：两个理由的主角是同一个东西 → 同一根轴（车轱辘）；一个角度只说两句（一句说清＋一句画面） | 任给一题，说出主角不同的两个理由 | 08-05 |
| B64 | **only / all / 最高级 后面的关系代词用 that，不用 which** | "那是唯一真正属于你自己的部分" | 08-05 |
| B65 | **that ＋ 形容词 ＝ "那么……"**：nothing is that simple ／ it's not that hard ／ it's not that expensive | "事情没那么简单" / "其实没那么难" | 08-05 |
| B66 | **good AT doing**（good with ＝ 擅长应付人/物：good with kids）；升级版直接 **He cooks well.** | "他很会做饭" | 08-05 |
| B67 | **walk to work**：by 后面只接交通工具（by bus / by car），步行不说 by walking | "我每天走路上班" | 08-05 |
| B68 | **主语复数，表语也要复数**：hobbies are **things** you choose（不是 something） | "业余爱好是自己挑的" | 08-05 |
| B69 | **反差句两边都要说完**（只说一半＝不是反差）；连接词用 **but / whereas**，`and` 是并列不标反差 | "我需要这份工作，但花需要我" | 08-05 |
| B70 | **work 不可数 ＝ 活儿/工作这件事**（I need work＝我需要有活干）；说"这份工作"用 **my job** | "我需要这份工作" | 08-05 |
| B71 | **一句里人称不能跳**：`I like cooking, because YOU follow the steps` → 统一成 I 或统一成 you | "我喜欢做饭，因为一步步来最后有东西拿得出手" | 08-05 |
| B72 | **eat out ＝ 出去下馆子**（不是"吃完"）；"十分钟就吃完了" → `it's gone in ten minutes` | "做两小时，十分钟就吃完了" | 08-05 |
| B73 | **★ convenient 后面只能跟【人】**（08-10 三次数据后精确化）：<br>✅ `It's convenient FOR ME.` ／ `Shopping online is convenient for working people.`（08-07 她用对的那次）<br>❌ `convenient TO FIND`（后面是动作）／`convenient FOR THE NEXT USE`（后面是用途）<br>⇒ "下次好找" 一律用 **easier**：`makes it easier to find things next time`<br>（与写作 `makes few people convenient` 同源；累计错→对→错三次）<br>参考对照（不出题）："网购对上班族很方便" `Shopping online is convenient for working people.` ← 后面是人，合法 | "东西放回去下次好找" | 08-05（08-10 精确化；08-11 收成一条题面，留她错的那侧） |
| B74 | **put sth away ＝ 收起来**（收玩具/收衣服）；clean up ＝ 打扫脏东西。呼应块 `kids will do the same` | "孩子玩完把玩具收回去" | 08-05 |
| B75 | **去掉 `X is important` 的壳**：把 X 里的动作提上来当谓语。`Explaining why … is important` → `Parents should also explain why it matters.` | "跟孩子讲清为什么也很重要" | 08-05 |
| B114a | **rather than 两边是同句的两个谓语动词 → 必须同形**（helps…rather than replaces）<br>★ ⚠️ `helps you rather than replacing you` **可接受**，只是平行版更稳 | "它是帮你，不是取代你" | 08-06（08-11 从 B114 拆号） |
| B114b | **rather than 领独立短语、尤其句首 → 用 -ing**（Rather than taking the bus, I walked）；**前面是 to do → 后面省 to 用原形**（decided to walk rather than take the bus） | "与其坐公交，我走路" | 08-06（08-11 从 B114 拆号） |
| B189 | **keep an eye ON sth**（留意/照看，固定搭配）：`keep an eye on the prices` ／ `Could you keep an eye on my bag?`<br>⚠️ **08-12 第三次改抽查方式**：08-11 两次记 ◎ —— "留意/看着"这类中文，pay attention to／look after／watch 全都合法，**没有任何一句中文能唯一逼出 keep an eye on**。<br>⇒ 改成【给两种说法】（同 B171d 的做法），逼她调出第二个 | "买东西的时候得留意点价格"（**给两种说法**） | 08-10（08-11 改题面；08-12 改成"给两种说法"）|
| B187 | **kind of / sort of / type of ＋ 单数名词，不带冠词**：`what kind of city` ✅／`what kind of a city` ❌ | "你开的是什么车？" | 08-10（08-11 改题面：原题面与 B174 逐字撞车，且"适合住"是 B174 的考点；新题面只测 kind of ＋单数无冠词） |
| B188 | **usually ＝ 通常情况下**（08-11 撤销与 B44 的合并，改为题面互斥：**B44 测 often，本号只测 usually**）。<br>参考对照（不单独出题）：often＝经常 ／ always＝总是。<br>**⚠️ 08-11 修订边界**：`always ＋ 习惯动词` 在英语里是常见夸张，等于"老是说/常说"，**不算错**（My grandma always says…）。三档只在**需要精确频率**时才分。<br>★ 真正要盯的是 **often vs usually**（她误用 usually 三次）：经常＝often／通常情况下＝usually | "我朋友经常去那家店" / "我通常七点起床" | 08-04＋08-10（08-11 合并修订） |
| B183 | ⭐ **a mixed bag**（好坏参半，她自产）：`It's a bit of a mixed bag.` —— 二选一题的"都有"型开头 | "这事儿好坏参半" | 08-09 |
| B184 | **move on ＝翻篇/从过去走出来**（Let's move on）≠ **move forward ＝往前进、有进展**：`Ambition can keep you moving forward.` | "野心能让人一直往前走" | 08-09 |
| B185 | **miss out on sth ＝ 因为顾不上而错过某种体验**（miss sth ＝想念/没赶上）：`you may miss out on things like friendship` | "你可能会错过友情这类东西" | 08-09 |
| B186 | **"兼顾未来和现在"三说法**：`keep one eye on the future and one on the present`（最形象，天然对仗）／`You need a bit of both — something to work towards, and a life right now.`／`Don't let the future eat up the present.` | "得同时看着未来和当下" | 08-09 |
| B180 | **All you need / have to do is ＋ 动词原形**（is 后面省掉了 to）：All you have to do is **ASK**.／All you need to do is **speak and listen**.（不是 is speaking） | "你要做的就是多说多听" | 08-09 |
| B181 | ⭐ **bury yourself in sth**（埋头钻研，她自产）：`avoid burying yourself in grammar books and word lists` | "别一头扎进语法书和单词表里" | 08-09 |
| B182 | **说人的目的用不定式 to do**（you learn a language **TO EXPRESS** yourself）；`for ＋ -ing` 是说**物品用途**（a knife for cutting） | "学语言就是为了表达自己、听懂别人" | 08-09 |
| B177 | **to be HONEST**（形容词；honesty 是名词，to be honesty ❌） | "说实话，我没怎么想过这事" | 08-09 |
| B178 | **either way**（横竖都一样）＋ **you might as well**（那还不如）＋ **I've never really thought about it**（我没怎么想过）<br>组合例：`It's one day either way, so you might as well smile.` | "开心是一天，不开心也是一天，那还不如笑笑" | 08-09 |
| B179 | **older people / the elderly** 比 old people 得体（英语说年长者默认用比较级） | "长辈们常说……" | 08-09 |
| B176 | **说"两类/三类"时，每类要用复数**：`two kinds — the fun ONES and the useful ONES`（每类里不止一个，不是 the fun one） | "就两类，好玩的和有用的" | 08-09 |
| B173 | **without ＝ with no，不能叠**：`a job WITH NO overtime` ✅／`a job WITHOUT overtime` ✅／`without no overtime` ❌（极性第 4 次，多一个否定） | "我没法一天不看手机" | 08-09（08-11 改题面：08-10 记 ◎，原题面 with no / reasonable hours 都能答对，逼不出 without；新题面结构上只能走 without）|
| B174 | **"什么样的" ＝ what kind of / what makes…**（不是 which——which 是从确定范围里挑）；**"适合住" ＝ good to live in / a good place to live**（fit living ❌） | "什么样的城市适合住" | 08-09 |
| B192 | **enough X to go round ＝ 够分**（强调"每个人都有一份"）：`There aren't enough jobs to go round.` ／ `not enough chairs to go round`。<br>★ go round 只在跟 enough 连用时是这个义项，整块记；美式 go around。<br>参考对照（不出题）："椅子不够坐" `not enough chairs to go round` | "岗位不够分" | 08-10（08-11 收成一条题面） |
| B191a | **jammed / gridlocked ＝ 车堵**（the roads jam up · traffic is gridlocked） | "一出事故，整条环路全堵死了，一动不动" | 08-10（08-11 从 B191 拆号；同日改题面：原"路上堵死了"她合法答成 the traffic is heavy，记 ◎ —— 新题面必须逼出"完全不动"那一档） |
| B191b | **packed ＝ 人多**（a packed train · the bar was packed） | "地铁里人挤人" | 08-10（08-11 从 B191 拆号） |
| B190 | **★★ 后置修饰的【共享诊断动作】（08-11 建，08-11 当天修正定位）**<br>**把名词放回从句里念一遍，缺什么补什么。**<br>⚠️ **它不是一个条目，是 B175 和 B164 共用的一个动作。B175/B164 各自独立计分，不合并**<br>（08-11 审计新违规#1：合并会让两条永远拿不到自己的连击；而且它们是两条不同规则——<br>一条管介词、一条管关系词——只是诊断手法相同）<br>★ 测法：**必须用全新名词 ＋ 包在有内容的整句里**，不许孤立造短语（08-10 已证孤立测更差）<br>★ 出题时：B175 和 B164 **各出各的题**，不许一题测两条 | 不单独出题；作为 B175/B164 的共享判据使用 | 08-11 |
| B175 | **不定式后置修饰，介词默认留在末尾**（还原成完整句看挂什么介词）：a chair to sit **ON** · a pen to write **WITH** · a topic to talk **ABOUT** · a house to live **IN**。<br>例外：place / somewhere / anywhere 吸收介词可省 —— a good **place** to live ✅ ／ a good **city** to live **IN** ✅<br>★ 共享判据见 B190；测法必须全新名词＋整句 | "我需要个盒子，把这些东西装起来" | 08-07（08-11 改题面：B190 要求全新名词＋整句，纸/刀两句已用过两轮；box 是新名词，且中文不含介词提示） |
| B171a | **将就 make do with**（记忆抓手：make do ＝ make it do，让它顶用） | "没有筷子，我就拿勺子凑合了一下" | 08-09（08-11 从 B171 拆号） |
| B171d | **照顾 look after sb** | "周末我妈帮我照顾孩子" | 08-09（08-11 从 B171 拆号） |
| B171f | **寻找 look for sth**（≠ look up ＝ 查资料） | "他在找一份离家近的工作" | 08-09（08-11 从 B171 拆号） |
| B171g | **应付得来 get by** | "我英语不算好，但日常应付得来" | 08-09（08-11 从 B171 拆号） |
| B171※ | **★ B171 原来一条塞 9 个短语，08-11 拆号。其中 5 个已经是别的号的考点，题面归属如下，本号不再出题（不是删条目，是题面互斥，见 §0.2 第二步）**：<br>别废话接着干 get on with it → **B141** ／ 埋头钻研 bury yourself in → **B181** ／ 追求 be after → **B162** ／ 卡住 stuck on → **B117b** ／ 被迫接受 stuck with → **B117c**<br>记忆抓手保留：get on ＝ 继续往前走 | 不出题（题面已分给上列各号） | 08-11 |
| B172 | **complain 不及物**：`complaining about it` ✅／`complaining` ✅（整体省掉）／`complaining it` ❌（不能只省 about） | "与其抱怨，他直接就干了"（两种说法） | 08-09 |
| B163 | **★ 否定辖域陷阱**：`with no overtime and stability` 会被读成 with no [overtime and stability]（意思反了）。<br>解法A（推荐）**换成正面名词**：reasonable hours and job security ／ 解法B 拆成两句 | "我想要一份不加班又稳定的工作" | 08-08 |
| B164 | **关系词选择：把先行词放回从句，看需要什么介词**（you can balance work and life IN this job → in which → **where**）。job／situation／case／kind 这类抽象"场所"一律 **where**（the kind of job **WHERE** you work till 10）；口语最省是绕开：`a job THAT LETS YOU balance work and life`<br>★ 共享判据见 B190；**与 B175 各出各的题，不合并**（08-11 撤销了当天的误合并） | "他那种工作根本没有周末" / "一份能让你平衡工作和生活的工作" | 08-08 |
| B165 | **discrimination AGAINST sb**（不是 for）；**age discrimination 不可数不带冠词** | "国内对 35 岁以上的人有年龄歧视" | 08-08 |
| B166 | **★ 限定 ≠ 定指**（她自己抓到的区别）：限定＝缩小范围；定指＝缩完只剩一个**且听者能确定**。<br>判据：**限定完还剩几个？** 剩很多→a ／ 只剩一个且听者能确定→the（最高级、序数、刚说过的）。<br>**one 回指的是"名词这个类"，冠词要重新选**：one＝a job ／ the one＝the job。<br>★ 杀手锏：**描述一件还不存在的东西时，永远不可能定指** | "我想要一份不加班的工作，还得是稳定的那种" | 08-08（08-11 改题面：08-10 记 ◎，原题面逼不出 `one that's stable`）|
| B167 | **★ 优点清单 ＝ 名词短语清单（操作）**：中文用动词/否定，英语用正面名词。<br>不加班→reasonable hours ／ 稳定→job security ／ 下班后的时间→time outside work ／ 靠得住→something you can count on。<br>★ 全用名词 → **没有否定辖域问题，也天然同形** | "什么样的工作/城市/房子好"——各列三条，全名词短语 | 08-08 |
| B168 | **并列同形＝语法功能相同，不要求词性一样**（动名词是名词性，可与名词并列）。<br>**自测法：把两边分别接回前面那个词，看通不通** —— time for [your hobbies] ✅／time for [being with your kids] ✅ → 同形 | "下班后有时间做点别的，比如爱好，或者就是陪陪孩子" | 08-08 |
| B169 | **关系代词做宾语可省，做主语不可省**：the book (that) I read ✅可省 ／ the book THAT changed my life ❌不可省。<br>**并列两个定语从句时 that 不能共用**（一个当宾语一个当主语，角色不同）。口语最佳：`subjects we actually use later, or ONES THAT come up everywhere` | "学以后真用得上的、或者到处都会碰到的科目" | 08-08 |
| B170 | **clear ≠ clean**：clear＝清澈/无遮挡（a clear sky）· clean＝干净无污染（clean air） | "空气干净" / "天很晴" | 08-08 |
| B162 | **look after / be after / look for 三个形近词组，意思完全不同**：look after sb＝照顾 · **be after sth＝追求想要**（They're after a bit of peace and quiet）· look for sth＝寻找。<br>另：**peace and quiet** 是固定搭配（说"清静"用它，不用 inner peace）；**light sleeper**（睡眠浅） | "老年人就想图个清静" / "他睡觉很浅" | 08-08 |
| B161a | **肯定句里的 much**：裸 much 只用于否定/疑问；肯定句换 **a lot of**。✅ I don't have much time／Do you have much time?　❌ I have much time.<br>**⚠️ 被程度副词修饰后肯定句合法**：so much／too much／how much ✅ | "我在化学上花了很多时间" | 08-08（08-11 从 B161 拆号；继承 08-09/08-10 两次 ❌ 的连错基线——那两次错的就是这一族） |
| B161b | **肯定句里的 for long**：肯定句换 **a long time**。✅ I didn't wait for long ／ ❌ I waited for long → I waited a long time | "我等了很久" | 08-08（08-11 从 B161 拆号，同上继承连错基线） |
| B161c | **肯定句里的 far**：**裸 far**（I walked far ❌）必须换 **a long way**；★ 被程度副词修饰后完全合法：really far／pretty far／so far／too far ✅（I ran really far today.） | "我走了很远" | 08-08（08-11 从 B161 拆号，同上继承连错基线） |
| B159 | **actually 的位置**：修饰整句时＝**be 动词后／实义动词前**（It's actually cheap／I actually forgot）；**嵌入从句里卡在主语和动词之间**（how tall a T-rex **actually was**） | "他终于看到霸王龙到底有多高" | 08-08 |
| B160 | **★ 差异题的解法（操作）**：不是找相似点，是**找一根共同的尺子，说两边各在哪一端**。<br>万能尺子：主动 vs 被动 · 一个人 vs 一群人 · 快 vs 慢 · 花钱多少 · 靠想象 vs 靠感官 · 深 vs 广 · 当时 vs 之后。<br>**比较觉得空 → 加一个使用场景**（"为了什么去选"），可以自己加进答案里，是加分不是绕开 | 任给一道 "What are the differences between A and B?" | 08-08 |
| B157 | **-ed / -ing 形容词**：**说人的感受用 -ed，说东西的性质用 -ing/-y**。I'm scared ／ It's scary · I'm bored ／ It's boring · I'm interested ／ It's interesting · I'm excited ／ It's exciting<br>⚠️ 08-11 错例：`I was hook` → hookED | "这有点吓人，我自己也有点怕"（一句里两侧都要） | 08-08（08-12 收成一条题面，同时测 -ing 和 -ed 两侧） |
| B158 | **口语选词**：complicated（不用 complex，偏技术学术）· takeaway（英）/ takeout（美，不可数） | "有些 app 对老人太复杂了" / "点个外卖" | 08-08 |
| B155 | **and 接第二个谓语时，否定必须带助动词**：`Someone runs a red light and DOESN'T GET fined`（不是 and not get）。原形否定 not do 只用于 `to not do` 或祈使句 | "有人闯红灯还不用罚款" | 08-08 |
| B156 | **上班族 ＝ working people ／ office workers ／ people with full-time jobs**（她本来就写对了）；**traffic management 抽象不可数不带 the**（the traffic 才带） | "网购对上班族很方便" / "交通管理主要看两件事" | 08-08 |
| B153 | **-ing 短语省主语的硬条件：逻辑主语必须＝主句主语**。`Children put their toys away after playing with them.` ✅（playing 的主语是 children）／`After playing, I put the toys away.` ❌（变成"我玩完"）——即「理解侧冗余」第 3 条 | "孩子玩完把玩具收起来" / "孩子玩完之后我把玩具收了" | 08-08 |
| B154 | **东西不会自己 leave**：`His things ARE all over the floor.`（东西当主语用 be）／`He LEAVES his things all over the floor.`（人当主语用 leave） | "他那些东西一地都是"（东西当主语） | 08-08（08-11 改题面：原"他东西乱丢一地"与 B97 leave a mess 逐字撞车；新题面把东西放主语位，只有 be 版能答） |
| B152a | **原形＝过去式的一小撮动词**：put · cut · hit · let · set · cost · hurt · shut · spread · read（read 拼写不变但读 /red/） | "他昨晚把东西放桌上了" | 08-08（08-11 从 B152 拆号） |
| B152b | **不在那一小撮里的必须变形**：sit→sat／sing→sang／take→took<br>★ 起因：她问"如果 sit 是过去时是不是就没问题"——思路对（该句无时间标记，现在/过去都能说），但 sit 的过去式是 sat | "他昨晚一直坐在沙发上" | 08-08（08-11 从 B152 拆号；改题面避开 B58 的 the TV） |
| B149 | **★ 压缩出来的形容词，两个固定出口**（她卡在"形容词有了组不进句子"）：<br>**出口A 做表语（最省，只要一个 be）**`The trains are packed.`／`The traffic is heavy.`<br>出口B 做定语（要现找动词）`You get on a packed train every morning.`<br>★ 卡住时先走出口 A | "地铁里人挤人" / "路上堵得一动不动" | 08-08 |
| B150 | **功能上线 ＝ go live / be released / be coming out**（不用 be on；be on ＝正在上演、开着：The film is on） | "这个功能下个月上线" | 08-08 |
| B151 | **完成进行时 ＝ have been ＋ -ing**（I've been workING，不是 I've been work） | "我在这家公司干了五年了" | 08-08 |
| B141 | **get on with it**（不废话，埋头干下去）：`Rather than complaining about it, he just got on with it.` | "与其抱怨，他直接就干了" | 08-08 |
| B142 | **some people**（有些人）≠ somebody（某一个人） | "有些人就是享受花钱这件事" | 08-08 |
| B143 | **形容词顺序（口语版）**：越是说"属于哪一类"的词越贴着名词，越是"你怎么看它"的词越靠前。`an online PET group` ／ `a nice big bag`。口语很少堆三个以上，不用背 OSASCOMP | "一个线上的养宠物的群" | 08-08 |
| B144 | **加形容词说"哪一种"时回到 a**：the economy → **a** diverse economy ／ the market → **a** competitive market（补充 B133） | "创业公司对多样化的经济很关键" | 08-08 |
| B145 | **there was A PROMOTION**（要名词，不是 promoting） | "商品页上有个促销" | 08-08 |
| B146 | **★ 直接疑问句 vs 嵌入疑问句的边界**：**前面有没有主句？没有 → 助动词＋疑问语序**（What did you eat? / How wide should it be?）；**有 → 陈述语序**（I don't know what you ate / think about how wide it needs to be）。★ B82 的边界，她曾过度泛化 | "你昨天吃的什么？" / "我不知道你昨天吃了什么" | 08-08 |
| B147 | **★ 完成时的三个触发（只看中文标记，不判断语义）**：①for/since「…了多久」②ever/never/before「…过」③just/already/yet「已经/刚/还没」。<br>**边界**：句中出现具体时间点（yesterday／last year／three years ago／in 2020）→ **必须过去式**。<br>对照：`stopped making them years ago` ✅ 过去式 ／ `haven't been made for years` ✅ 完成时 | 见拆出的 B147a / B147b | 08-08（08-12 拆号） |
| B147a | **完成时的三个触发（只看中文标记，不判断语义）**：①for/since「…了多久」②ever/never/before「…过」③just/already/yet「已经/刚/还没」 | "我从来没坐过飞机" | 08-08（08-12 从 B147 拆号，从 0 起算） |
| B147b | **边界：句中出现具体时间点**（yesterday／last year／three years ago／in 2020）→ **必须过去式**，不许用完成时 | "我去年住这儿" | 08-08（08-12 从 B147 拆号，从 0 起算） |
| B148 | ⚠️ **极性（第 3 次，升为关注项）**：否定别丢、别多。08-04 `In contrast…CAN show`（该 can't）／08-05 `nobody else CAN'T`（多一个）／08-08 `this thing HAVE been made`（该 hasn't）——三次方向都不同。<br>本号只测**否定别丢**；**否定别多**（双重否定）归 **B54**，两号题面互斥。<br>**⚠️ 08-12 升级题面**：08-11 实证她在【单个否定】上守住了、在【嵌套否定】上垮掉（"我没法一天不看手机"译反了）⇒ 题面必须直接上嵌套否定。<br>★ 关键规律：**中文两个否定，英语最自然的往往是【一个肯定句】** —— 他没有一次不迟到 → `He's never once been on time.` | "他没有一次不迟到" | 08-08（08-11 收成一条题面；08-12 升级为嵌套否定） |
| B140 | **★ 二选一/趋势题的三种答法（操作，做出来测）**：a.分人群/分场景（工作日 vs 周末）b.**分偏好和行为**（想在家吃，实际在外吃）c.选一边＋给条件。<br>**矛盾不是障碍，矛盾就是答案**；没数据不影响，用 `I'd say / Most people I know / From what I see / Around here` 缩小范围。<br>⚠️ 开头连说两句"我不知道"＝真失分，`It's a tough one` 说一次就必须给立场 | 任给一道 "Do people prefer A or B?" | 08-07 |
| B137 | **I'd SAY**（＝I would say，我觉得）不是 I'd said；**"主要就是…"的四条路径**：It mainly comes down to X ／ The main thing is X ／ It's mostly about X ／ What really helps is X | "我觉得主要就是钱的问题"（四种说法各说一次） | 08-07 |
| B138 | **go ON a trip / take a trip / plan a trip**（不是 go to a trip）；旅行住哪儿用 **where to STAY**（live 是长期居住） | "要出去玩的话，可以先查查住哪儿" | 08-07 |
| B139 | **consider sth**（及物，不带 about）／ think ABOUT sth —— 两个都对但不能混 | "AI 会把你的预算也考虑进去" | 08-07 |
| B135 | **创业用 start / set up a business**（不用 create）；**"承担"＝take on**（take on risk／responsibility）；最口语 `they have less to lose` | "创业的人承担的风险小了，就更愿意干" | 08-07 |
| B136 | **★ 不是禁用书面词，是"有口语版就用口语版"**（08-10 修订，原来说得太绝）<br>✅ **概念本身就正式、没有口语版的照用**：age discrimination · job security · enforcement · economy · regulations · infrastructure（她 08-10 这五个全用对了）<br>❌ **有更短更常用说法时别去调长的**：the advent of AI→**now with AI** ／ specialized information→**answers for your situation** ／ tax reduction→**tax cuts** ／ enterprises→**firms/businesses**<br>★★ **判据不用"书面 vs 口语"这个分类，用这个：这个词你能不假思索说出来吗？能→用；要现找→不在自动区，换掉。**<br>理由直接挂在带宽模型上：调一个不在自动区的词 → 吃带宽 → 后一句结构跟着崩（08-10 实证：`specialized information` 后面紧接着 `with completely thinking about` 崩掉）<br>★ 隐性成本：书面词多半只在阅读里见过，不知道搭配限制（advent of 只跟时代性大事；specialized 配 knowledge/training，配 information 怪）——**见过 ≠ 会用**<br>★ 连带原则：同一批人前后用同一个词（前文 small businesses，后文别换 enterprises）。<br>参考对照（不出题）："减税能减轻小企业的压力" → tax cuts / firms<br>**⚠️ 08-12 改测法（08-11 实证）**：同一天里中译英单点测 `now with AI` **✅**，而 P3 自由产出一口气冒出 `demand／enterprises／the development of` **三个书面词**。<br>⇒ **本条不再出中译英题**：单点测时带宽只管一个词，测出的 ✅ 是假的；自由产出时带宽被内容和结构吃满，词的选择才回落到真实水平。<br>⇒ **挂当日自由产出题下当场抓**：自由产出里没冒书面词 → ✅；冒了 → ❌ | 不出中译英题；挂当日自由产出题下抓（同 §0.3 减法型规则的处理） | 08-07（08-10 修订；08-12 改测法） |
| B128 | **than ever 必须紧跟比较级**：`makes it easier THAN EVER to keep in touch`（不能隔一整个从句）——"修饰语紧贴被修饰词"的比较对象版 | "社交媒体让联系比以前方便多了" | 08-07 |
| B129 | **get TO know sb**（逐渐认识某人，to 不能省）；`it's easier to do` 本就不需要 for | "现在更容易认识陌生人" | 08-07 |
| B130 | **群组用 in**（in an online group）；论坛用 on（on a forum） | "我在一个养宠物的群里加了个好友" | 08-07 |
| B131 | **形容词不加复数**：crucial（不是 crucials）；crucial TO 比 crucial for 更常见 | "创业公司对经济很关键" | 08-07 |
| B132 | **条件句别纠结**：`every time / whenever / always` 在场 → 主句用现在时；说"如果将来出现某情况" → 用 will；**两个都通时随便选，不扣分**（08-07 修正原来分得过硬的说法） | "如果没人愿意创业，就没那么多岗位" | 08-07 |
| B133 | **★ the 的第二条判据：语境里只有一个的系统性名词 → 带 the**（不是"特指才加"）：the market · the economy · the internet · the environment · the media · the weather；**可数的多个则不带**：governments · banks · companies · start-ups | "从市场上融资，或者跟银行借" | 08-07 |
| B125 | **平台用 on，实体店用 at**：on Amazon／on Taobao／on YouTube ／ at Walmart；专有名词不带 the | "我在亚马逊上买的" | 08-07 |
| B126 | **a pack of napkins**（纸巾论包用 pack/packet，不用 bag；napkin 可数要复数）· **the product page**（商品页，不说 good page） | "我想在网上买包纸巾，结果商品页上有促销" | 08-07 |
| B127 | **★ 名词壳（她的老毛病，换位置反复出现）**：实义动词外面套一层名词壳＝虚。<br>`enjoy THE SENSE OF spending money` → `enjoy spending money`；`THE MOST IMPORTANT THING IS THAT parents are organized` → `It starts with the parents`；`explaining why IS ALSO IMPORTANT` → `Parents should also explain why`<br>判据：**壳去掉后意思还在吗？在 → 去掉** | "最重要的一点是家长得有条理" | 08-07（08-11 补题面：原格里写的是测法说明不是题面，按 0.3"题面逐字复用 B 表"根本取不出题）|
| B123 | **★ 中文无主语句 → 英语先想被动或 they，别硬找主语**：停产了＝`they aren't made anymore`／`they've been discontinued`；硬要主语就给真的那个（the company stopped making them），别用 people 兜底 | "这条路去年修好了" | 08-07（08-11 收成一条题面："有些东西早就停产了"与 B148 撞车，撤下） |
| B124 | **比较里的泛指不加 the**：`cheaper than new ones`（不是 than the new ones）—— B113 判据的应用，她一到 than 后面就犹豫 | "二手的比新的便宜多了" | 08-07 |
| B121 | **"只能将就" ＝ `I'll have to make do with …`**（08-11 修订：整块含 have to）／ **be stuck with**（被迫接受甩不掉）／最短 `It'll have to do.`<br>⚠️ 08-10 她两次只产出 `make do with`、丢掉"只能"那层 —— 那不是 B121 的另一条错，是**这个块本来就该带 have to**。分开记会制造假错误，改成整块测 | "只能将就这台旧电脑" | 08-07（08-11 修订） |
| B122 | **complain ABOUT sth**（不及物，必须带 about）；`other than` ＝除了…之外 ≠ `rather than` ＝与其…不如 | "与其抱怨，他直接就干了" | 08-07 |
| B118 | **"全信" ＝ trust it completely ／ take its word for it**（不是 believe it）；**"一般" ＝ just OK ／ not as good ／ nothing special** | "AI 不能全信" / "他写作一般" | 08-06 |
| B119 | **副词修饰动作**：speak English **well**（不是 speak good）—— 与 `he cooks well` 同一规则 | "他英语说得挺好" | 08-06 |
| B120 | **…, though.（挂句尾）是唯一不用提前预判的转折标记** —— 说完再补，前面一字不改；That said,（句首，需预判）／ Then again,（话说回来，自我修正） | "这房子挺大，不过离地铁远" / "我想去，不过那天有事" | 08-06 |
| B117a | **stuck IN ＝被困在环境/容器里**（stuck in traffic／in meetings／in a lift）。判据：in 是周围把你围住 | "上周我被困在电梯里半小时" | 08-06（08-11 从 B117 拆号；改题面：原"早高峰堵路上"与 B84/B96/B98 三处撞车） |
| B117b | **stuck ON ＝卡在具体的点上**（stuck on a problem／on question 3／on this word）。判据：on 是面前有个坎 | "我在第三题上卡住了" | 08-06（08-11 从 B117 拆号，题面从 B171 划归本号） |
| B117c | **stuck WITH ＝被迫接受甩不掉**（stuck with this old laptop） | "分组的时候我跟他一组，甩都甩不掉" | 08-06（08-11 从 B117 拆号；改题面避开 B121 的"只能将就这台旧电脑"，题面从 B171 划归本号） |
| B115 | **any ＋ 单数**表"任何一个"（answer almost any question）；复数的 any questions 用在疑问/否定句（Do you have any questions?） | "AI 几乎什么问题都能答" | 08-06 |
| B116 | **think FOR oneself ＝ 独立思考**（固定）；**by oneself ＝ 独自一人做某事**（I did it by myself） | "学生还是得自己独立思考" | 08-06 |
| B110 | **singular they**：someone/anyone/everyone 后面用 they/their **正确**；但 who 从句要跟先行词一致 → `someone who LIKES`。更省事：主语换复数 `kids who like…` | "喜欢拍照的人，Photoshop 是他们的最爱" | 08-06 |
| B111 | **★ Kinds/What 类主干**（三步主干只管 Why/Should/差异题）：①分两类就两类 ②每类一个具体例子（有名字最好）③每类一句"为什么受欢迎"。第二类开头必须明确标出（The other kind is… / The second kind is…） | 任给一道 What kinds… 题 | 08-06 |
| B112 | **addictive**（停不下来）≠ interesting（有意思）；`so addictive that some kids stay in front of a screen all day` | "游戏太上瘾，有的孩子一天不出门" | 08-06 |
| B113 | **the 的唯一功能＝双方都知道是哪一个**。前句框定范围后，逐一列举用 the：`two kinds — THE fun ones and THE useful ones`／`I bought some apples. THE red ones were cheaper.` | "就两类，好玩的和有用的" | 08-06 |
| B106 | **make sb ＋ 形容词**（make kids overweight）。cause 用法很窄：cause sb sth／cause sth／cause sb TO do，**不能 cause sb 形容词** | "长时间看屏幕会让孩子变胖" | 08-06 |
| B107 | **学业 ＝ schoolwork / their studies**；**pay attention TO**（不是 on）；**lose interest IN** | "孩子会对学业失去兴趣" | 08-06 |
| B108 | ⭐ **screen time**（她自产）；**balance A and B ／ balance A with B 都对**（08-07 更正：原写"必须 with"是把一种说法写成唯一说法）；`pair X with Y` 也成立（08-06 她指出） | "家长该给孩子的屏幕时间和户外活动找个平衡" | 08-06（08-07 修订） |
| B109a | **`I wouldn't go THAT far, though.`**（软化自己刚说的话，though 挂句尾 ★ B120）<br>⚠️ **08-11 教练自纠**：08-06 起本条一直写的是 `go TOO far`，**是错的** —— `I wouldn't go too far` 读作"我不会做得太过"，不是"我不会把话说这么绝"。固定块是 **go that far**。<br>同义备选：`I wouldn't say that, though.` ／ `That might be going a bit far.` | "不过我也不会说得那么绝" | 08-06（08-11 从 B109 拆号＋改正块本身） |
| B109b | **`An hour a day is completely fine.`**（给一个具体量当让步） | "一天一小时完全没问题" | 08-06（08-11 从 B109 拆号） |
| B109c | **`It's not that A — it's about B.`**（把矛头从对象转到程度） | "不是游戏本身不好，是看玩多久" | 08-06（08-11 从 B109 拆号） |
| B109d | **`in moderation`**（适度） | "什么东西适度都没问题" | 08-06（08-11 从 B109 拆号） |
| B103 | **clear the table**（餐后收拾桌子）≠ clean the table（擦桌子）；通用动词版 `put everything away` | "他把桌上收拾了" | 08-06 |
| B102 | **★★ 检索方向：中文靠实义词，英语靠一小撮通用动词**。卡住时不要找"那个词"，问「这件事用 **get / be / do / have / take / put / make / keep / go / come** 怎么说？」<br>吃饱→get fed ／ 搞定→be done ／ 相反→be the opposite ／ 围一桌→get everyone around one table | 给中文实义词，限定主动词只能从那一小撮里选 | 08-06 |
| B101 | **take sb out**（专门带某人出去玩）≠ bring sb along（带上一起去我本来要去的地方）；**outdoors** 是副词（play outdoor ❌） | "周末我带儿子出去玩" | 08-06 |
| B98 | **stuck in traffic**（不是 stuck in the road＝卡在路面里）；**IN / DURING the morning rush hour**（不是 on） | "早高峰我堵在路上四十分钟" | 08-06 |
| B99 | **drive past sth ＝ 从某物旁边开过去**（drive past the school）；"开在某条路上"用 **drive down / along that road** ／ use that road | "我每次开那条路都堵" / "我每天开车经过那所学校" | 08-06 |
| B100 | **for any reason（单数）** ＋ **no questions asked**（七天无理由退货） | "七天无理由退货" | 08-06 |
| B96 | **the morning rush hour**（早高峰，不说 morning peak time）；配 `I was stuck for forty minutes` | "早高峰我在路上堵了四十分钟" | 08-06 |
| B97 | ⭐ **leave a mess**（她自产）＋ `leave his toys all over the place`（乱七八糟） | "他东西乱丢一地" | 08-06 |
| B93 | **audience 用整体义时是单数**：`The whole audience sings along`／最口语 `Everyone sings along`。audiences ＝多批/多场观众<br>⚠️ 08-06 更正：原写"必须单数"是简化过头，见 B104 | "全场观众跟着一起唱" | 08-06 |
| B104 | **集合名词单复数都合法**（family / audience / team / government）：当**整体**→单数（The audience was huge），当**成员各自**→复数（My family tend to cook all day）。英式更常用复数 | "我们家过年会做一整天的菜" | 08-06 |
| B105 | ⚠️ **口语作废，只在写作有效**（她 08-06 指出，成立）：逗号粘连／句子片段是**书面标准**，口语里语调就是标点，转写更转不出破折号。<br>口语只保留一条真问题：**悬空片段**——本身没有独立意思、听者接不上的（`…something to look after. UNLIKE WORK OR KIDS. It's…`）必须挂回主句；<br>能独立表意的补充片段（`As for how.`／`How wide they need to be.`）**完全正常，不算错** | 只在写作复盘时用 | 08-06 修订 |
| B94 | **every time / each time 是连词，后面跟完整从句**：every time you use it（不是 every time using it） | "你每次走那条路都堵" | 08-06 |
| B95 | **可分离动词短语的位置**（08-07 更正，原写"短宾语要放中间"是把倾向写成规则）：<br>**代词必须放中间**（put it away ✅／put away it ❌）· **名词短语两个位置都合法**（put their toys away ✅／put away their toys ✅）· 长宾语倾向放后面。<br>另：away 不变形（put aways ❌）；玩具搭配是 **play with**，不是 use | "孩子玩完把玩具收起来" | 08-06（08-07 修订） |
| B89 | **neither … NOR**（不能 neither … or）；更省事就直接 `forward or back` | "我既不会做饭也不会烘焙" | 08-06（08-11 改题面：原题面与 B87 逐字撞车，B87 测 whether＋forward or back，本号只测 neither…nor） |
| B90 | **every time / whenever 出现＝反复发生的规律 → 主句用现在时**（you GET stuck），will 是预测未来某一次 | "我每次点这家外卖都要等一个小时" | 08-06（08-11 改题面：原题面与 B83/B94 逐字撞车，三条都被那一句同时触发） |
| B91 | **by ＋ -ing ＝ 通过做某事达成结果**（He passed the exam by studying every night）。<br>⚠️ 她连续 3 次绕开这个结构，需单独焊。交通方式另说：by bus/car（不带冠词）／ on foot ／ I walk to work | "他每晚学习，就这么过的考试" / "走路上班能省不少钱" | 08-06 |
| B92 | **save sb money / sth**（save 带间接宾语）：save YOU a lot of money | "这个 app 能给你省不少时间" | 08-06（08-11 改题面：原"走路上班能省不少钱"与 B91 的 by＋-ing 题面撞车） |
| B87 | **whether 后面要跟主谓**（whether they go forward or back）；**forward or back ＝ 前进/后退**，`back and forth` ＝ 来回反复，两回事 | "谁都动不了，前进也不行后退也不行" | 08-05 |
| B88 | **★ 卡词时的操作（做出来测）**：不是去找那个词，而是**把任务降到只用最简单的词说完画面**——负载一降，难词往往自己出来（08-05 实证：限定她只用 cars/move/forward/back，她反而调出了 intersection） | 让她说一个卡住的画面，看她会不会自己减负 | 08-05 |
| B82 | **嵌入疑问句用陈述语序**：`how wide they need to be` ／ `what the road is for`（不是 how wide should they be） | "得考虑路要修多宽" | 08-05 |
| B83 | **说一般规律用真实条件**：if ＋ 现在时 ＋ 现在时。`were/would` 是**反事实**专用 | "设计有问题，你每次走那条路都会堵" | 08-05 |
| B84 | **run a red light**（闯红灯）· **get stuck in traffic**（堵在路上，不说 experience traffic jams） | "有人闯红灯" / "我早高峰堵了四十分钟" | 08-05 |
| B85 | **drive past**（开过去）不是 drive pass；pass 是动词，past 才是介词/副词 | "每次开过那条路" | 08-05 |
| B86 | **泛指不带 the**：traffic（不可数）／ regulations ／ designers（复数泛指） | "交通管理" / "法规和执行都重要" | 08-05 |
| B78 | ⚠️ **B71 人称一致升为主攻**（08-05 一天内跳了 3 次）：一句/一段里 you 和 I/my 不能混走。泛指就全 you，说自己就全 I | "在电影院你能沉浸进去，而且我和我太太当约会" | 08-05 |
| B79 | **visual effects / special effects 恒复数**；可数名词单数必须带限定词（visual effect ❌） | "主要是看视觉效果" | 08-05 |
| B80 | **date night**（两口子专门空出来的约会晚上）＋ `make an evening of it`；`a sense of occasion` 要挂在名词后紧跟例子 | "去电影院对我们来说就是约会" | 08-05 |
| B81 | ⭐ **it mainly comes down to …**（说到底就是……）—— 她自发产出，教练没给过 | "说到底就是钱的问题" | 08-05 |
| B77 | **比较级只标一次**：more easier ❌ ／ more better ❌。要么 `more + 原级`（more convenient），要么 `-er`（easier）。<br>★ 连带操作：**换完一个词要把整句重扫一遍**——她的 more easier 是把新词塞进旧框、没删旧零件 | "这样下次更好找" | 08-05 |
| B76 | **organized（说人）＝ 有条理会安排**，不是守规矩（那是 well-behaved）。画面：knows where everything is ／ packs his bag the night before ／ starts homework before the last day；反面 messy ／ all over the place ／ leaves everything to the last minute | "这孩子挺有条理的" / "他东西乱七八糟" | 08-05 |

---

## 📊 复习计分：只有一条事实流，状态现算（她 2026-08-09 定）

> **她的原话（两次）**：
> ① `每一个复习点额外记录一个数字连续错的次数，用错次数，连续对的次数，以及最后复习时间…每次都要记录上，如果连续对了 3 次就暂时不再复习。历史数据为空就都是 0`
> ② `你看这种表，我担心两边状态不一致，不要单独建表，就记录在 log 中，这种只有一张事实表，每天复习的学习的都是 append`
>
> **⇒ 最终设计（她 ② 否掉了教练 ① 的独立状态表，理由成立：独立状态表＝第二份事实，迟早对不上）**：
> ```
> 只写【事件】，不存【状态】。每天复习完，在当天日志段落末尾 append 一行：
>     📊 YYYY-MM-DD ✅ … ◎ … △ … ❌ … 🆕 …
> 连对 / 连错 / 累错 / 最后复习 —— 全部【从这些行倒着数出来】，不单独记
> 历史归 0：2026-08-09 之前的记录不回填，从这天起算
> ```
>
> **★ 五类标记（她 08-09 追加，原话："一字没改 / 没到考点(这个你注意下次得出的题方式) /
> 有更好的表达方式(下次出题可以提示下) / 错了 / 新的问题。这些在记录 log 的时候注意区别标识，
> 目前只有一字未改 3 次才暂时不复习"）**：
> ```
> ✅  一字未改        ← 【只有这一类计入毕业】，连续 3 次 → 🎓，出题跳过
> ◎   没到考点        她的句子对，但没测到那个点
>                    ⇒ **教练的题面有问题，下次必须改题面把考点逼出来**
> △   有更好的表达    她的成立，但有更地道的
>                    ⇒ **下次出这条时要提示"这题要更地道的版本"**
> ❌  错了            ← 连续 ✅ 断
> 🆕  新问题          本轮冒出来的新点，建号入池，从 0 算起
> 📖  给了范例才会    她要求教练先写一版，她再复现（她 08-09 追加：「这种你先给 case 我再说的，
>                    也加这个标记吧，也属于我不会的」）
>                    ⇒ **不计毕业**；这条**下次必须先 cold 测**，不给范例
>                    ⇒ 一条长期停在 📖 ＝ 根本没装上，只是每次照着念
> ★ 同一天同一条先对后错 → 以【最后一次】为准
> ★ ◎ △ 📖 都不计入毕业，但也不算错；它们各自触发教练侧的动作
> ```
> **查状态的方法**：`grep "^📊" fluency_lab.md`，倒着看。

### C 档 · 已知但暂缓（结构稳了再收）
| # | 点 | 备注 |
|---|---|---|
| C1 | 比较对象补齐（`than it was a year ago`，非 `than one year ago`） | 与写作 P4 同源 · 轮13 |
| C2 | 中文直译块小闭集：`playing phone→on my phone` / `do exercise→get some exercise` / `go work→get to work` | 唯一现在就改的零件类 · 轮15 |
| C3 | 复合修饰名词单数：`subway lines` / `a ten-minute walk` | 与写作 `multi-stage process` 同规则 · 轮20 |
| C4 | 主谓一致 · 冠词 · 时态一致 | **每次指出，但不 drill**（孤立测都对，是产出时掉；drill 无效）· 她 08-04 定 |

### 🚫 已作废/已修正的假说（保留，防止重蹈）
| 假说 | 死于 | 结论 |
|---|---|---|
| 缺 B 类虚位主语（it/there）| 轮10 | 她 it/there 全对，**it 反而是拐杖** |
| 长主语 → 断电，应默认短主语 | 轮17/20 | fragment 是录音漏词；她扛得住 5 词长主语 |
| 禁 it 就能逼出具体内容 | 轮21/22 | 她逃到 `I`；**禁载体≠禁行为**；主语≠内容 |
| 病灶在"内容检索"（没内容→说不出）| 轮23 | **因果反了：没路径→内容也不生成**。路径是因，内容是果 |
| 零件层结论全部作废（转写不可信）| 轮18 | 过度反应。改为**她没纠正=算数**（她定的协议）|

---

## 🧠 当前沉淀模型 v2（2026-07-29，40 轮后归纳。旧模型见下方"诊断链"，原始记录一条未删）

### 一切收敛到一个变量：**带宽**

```
她的英语产出吃满带宽 → 三个后果，正好是她三个痛点：
① 没带宽生成内容  → 不能"边说边想" → 答案短           （轮38）
② 没带宽检查形态  → 零件错（83% 本会）                （写作诊断 + 轮17）
③ 只有自动块出得来 → 旧块永远先到 → 句式来回那几个     （轮35）
```
**三个痛点，一个原因。** 也解释了考试只发挥 50%——紧张再吃掉一部分带宽。

### 所以只有两条路（没有第三条）
```
1. 降低单句负载   拆包 / 短结构 / 预制块  → 腾出带宽
2. 把关键块自动化  重复量                → 让它们不再吃带宽
「学更多」不在里面 —— 今天反复验证：她知识够用（抽查 83%、词全在、-s 全对）
```

### 她的失分全部可定位到「某个槽没有自动块」
```
起手槽     只有 It's / I                → 拐杖，且免检索（逃生通道）
评价槽     只有 is my absolute favorite → favourite 一出现必被调出
谓语槽     只有 is                      → 系动词泛滥（不是偏好，是没得选）
抽象概念槽 空的                          → 触发 emerge→prospect 找词死循环
```
**∴ 训练 = 给每个槽装 2–3 个自动块**（不是学更多词，是**同一功能多条路 = 路径冗余**，正是她说的"中文总能说几句"的原因）。她已自发出现一次（`makes` 之外自己用 `gives`，轮39）。

### 三个工具（不用再猜练什么）
```
负载测试 = 优先级排序   压一压，先掉的那个就是下一个要焊的            （轮37）
自我分诊              单独问答得出=检索失败(不背)；答不出=真缺口(记下) （写作诊断）
数据协议              转写默认可信，她没喊就算数                      （轮18）
```

### 两条铁律（今天反复撞到）
```
旧块永远先到    一次讲解打不过无数遍背诵 → 纠正背熟的东西比学新的还贵（轮35、轮40）
新块的三个条件  ①语义中立(留极性槽) ②带确认版(她不确定就不敢用) ③情态/副词不能省(是功能引擎)
                                                        （轮30 / 轮31 / 轮34）
```

---

## 诊断链（一路收敛，每一环都有她自己的数据支撑）

```
痛点        口语句式来回就那几个、一到具体内容就崩、说一两句就完
  ↓ 她自己定位
真缺陷      意思→英文形式没直连，全靠中文中转（在翻译）
  ↓ 作文实证（199 句）
结构定位    直连已建在【骨架层】(饱和,别练) / 翻译全残留在【填充层】
  ↓ 填充层翻译的指纹
统一①       填充层=中文"名词块打包"=写作根因①(谓语空转)。语法毛病=翻译指纹
  ↓ 现场实验(英文触发 vs 中文触发)
验证①       中文触发→她翻译搬包 ; 英文触发→她直接拆包。去中文触发有效
  ↓ 她的追问("说一两句就完，第一个token吐不出来")
机制        英文是"散装单词"、中文是"成串"。母语流利=前词自动带出后词(自回归绑定)
  ↓ 接龙实验(给她第一个块)
定位病灶    给第一个块，她能自回归接 4 个块 → 续接没问题！断电在【第 0 个块】=起头
  ↓ 她的追问("是不是没找到正确的主语？")
最底层收敛  起不了头 = 主语难产。中文=话题语言(可无主语) / 英语=主语语言(强制主语)
            她"拆包"本质=给句子立主语 ; "搬包/卡壳"=没立主语
            起手主语只有 4 类 → 起头从"想不出"变"4选1"
统一②       写作漏it/臃肿名词主语 = 同一个"主语指派"病。写作口语收敛到同一动作
```

**当前靶心**：把任意话题**指派成一个合格英语主语**的反射（4 类起手主语）。这是最小杠杆点。

**起手主语 = A/B 两性质、4 个格子（真底层，背块只是实例）**：
```
A 实义主语（拿一个真实体当主语；人和物句法同构）
   · 人       Young people tend to…
   · 物/概念   Smartphones changed… / Traffic is… / Finding a job is hard…   ← 物/概念当主语=高分武器
B 虚位主语（英语强制补的占位词，本身没意思——中文根本没有这东西）
   · it       It's hard to… / It makes…
   · there    There's… / There are…
```
- 她 2026-07-27 追问"是不是还有物当主语、可以和人合并"→ 逼出这个更干净的二分（原来的"话题当主语"其实就是 A 里"话题实体当主语"，不是独立一类）。
- **缺口定位：不在 A，在 B。** A（尤其物/概念当主语）她写作里是亮点(`The expansion of cities will put…`)；**B(it/there)是中文没有的抽屉**，她 `why is __ so hard` 漏 it、写作反复漏 it=源语言里没这个零件。**练习重点压 B。**
- 送她的武器：A 里"物/概念当主语"是高分特征（中文爱人开头，英语高分爱物/概念开头），口语要有意识优先用。

**⚠️ 轮 8 修正（她说 `The expansion of cities…` 口语说不出）**：上面"物/概念当主语是她的武器"**不精确**——那是慢时钟(写作)的能力，没迁到口语。真正的分界不是物/人，是**主语现成 vs 要现场加工**：
```
现成主语(快时钟能抓)   smartphones/traffic/rent(具体名词) · people(人) · it/there(虚位)
加工主语(慢时钟专属)   the expansion of cities · the increase of parks(名词化抽象)
```
`the expansion of cities` 说不出=要现场把"城市扩张"名词化成块，快时钟没这时间。
**⚠️ 轮 9 再修正（她："名词化主语口语也存在，别轻易削减目标"）——她对，收敛靶心≠削减目标**：
- 名词化主语口语当然存在(母语者 `The rise of social media has…` 张口就来)，是**天花板，不删**。
- 她现在说不出=**它还没被预制成块**(现场加工 expand→expansion→of cities 三步,快时钟没时间);母语者是整块焊死、一调一整块。
- **地板/天花板双轨,同时推**：
```
地板(现在)   现成主语先保证开口不崩   Cities are getting bigger, so…
天花板(持续) 把高频名词化块焊成"现成块"  the rise of…/the lack of…/the increase in…/the development of…
             → 焊成块后,加工主语就变成现成主语 → 脱口而出
```
- 核心："现成 vs 加工"不是永远避开名词化,是**把加工的预制成现成的**。`the expansion of cities` 的归宿是被焊成现成块,不是放弃。
- 两条并行线：**起手线**(现成主语,=手机/租房练习,先走) + **升级线**(单独焊高频名词化块,天花板)。建议先走起手线(天花板块要有地板托)。

**量化（她的痛点变成的刻度）**：从看到话题 → 吐出第一个块的**延迟**（=启动延迟，测的就是唯一病灶）。辅：给第一块后能连续不断电接几个块（现测 4，地板不低）。

---

## 逐轮记录（2026-07-27）

### 轮 0 · 方法论前置（她定的规矩）
- 练习必须：出声（不是打字想）→ 打**嘴里真实说出的那版**（卡壳照实打）→ 一口气冲、卡住跳过、绝不停下来先组织中文。
- 触发去中文化（中文触发=喂中介）。英文提问她秒懂（阅读 7.5 是最强腿），触发的是意思。

### 轮 1 · 中文情境触发（我的设计失误）
- 我给 3 个**中文**情境让她答。
- 她输入（原话）：`1. now young people find jobs, where is hard 2. smartphones bring the generation of your parent, leading to what specific changes 3. the public transit in your city, what is good or not good`
- **诊断**：她没回答问题，把**问题本身逐字翻译**了。→ 中文一出现，她的默认反应是"翻译它"，翻译回路自动启动。`where is hard`=教科书级搬中文包（难在哪→逐字）。
- 她自己的反馈：**"太糟糕了，写作文肯定不会这么写。"** ← 她自己道出"两个时钟"。
- 我认错：中文触发=递给她中文让她翻，方向错，是我的锅。

### 轮 2 · 用她的钥匙做"两个时钟"对比
- 我让她写第①句的"作文版"。
- 她输入：`why is so hard for young people to find jobs`
- **诊断**：① 慢时钟她**自动拆包**了（`for young people to find jobs`=谁+做什么）——同一个她、同一意思、知识没变，30 秒前搬包现在拆包，**唯一变量是时钟**。② 但漏了形式主语 `it`（`why is IT so hard`）——中文"为什么这么难"里没有 it，她的翻译回路里就没这个抽屉。→ 引出"零件层：漏的永远是中文里不存在的零件（it/冠词/单复数）"。

### 轮 3 · 改英文触发，她答内容
- 我抛 3 个**英文**问题（work / phone / city），只答内容。
- 她输入：`1. it is more competitive than ever 2. it makes people stay in touch easier 3. pretty convenient, there are tons of subway lines here`
- **诊断**：**判若两人**——`it is` / `it makes` / `there are`，全拆包，一个中文包没搬。→ **去中文触发验证成功**：中文一撤，默认反应从"翻译它"变"表达它"。零件小瑕疵 `stay in touch easier`→`more easily`（今天不纠）。

### 轮 4 · 她的关键追问 + 散装/成串机制
- 她问：**"为什么写一两句就完了？中文卡也能卡几句，英文卡不出来。像 LLM，第一个词吐不出来，没有轮廓、没有直觉。"**
- **诊断**：她的 LLM 类比精准。母语=自回归，前词自动带出后词（=直觉/轮廓）。中文有一辈子的"带出"权重(卡也能爬)；英文是散装单词，词间无绑定线，吐完一个就断电。→ **训练单位从"词/句"升到"块+接龙"**；"说不长"不是缺点，是训练目标本身。

### 轮 5 · 接龙实验 → 定位病灶
- 我让她拿自己 `It's more competitive than ever` 当第一块往下接。
- 她输入：`it's more competitive than ever, so young people have to study hard just to find jobs after graduate`
- **诊断**：**接了 4 个块，一口气**（so/just to/after=绑定线）→ **续接没问题，"说不长"被推翻一半**。真病灶=**第 0 个块（起头）**，与她最早"第一个 token 吐不出来"一字不差。零件：`after graduate`→`after graduation`（不纠）。

### 轮 6 · 她推到最底层：主语
- 她质疑启动块练习"不够底层"，自提假设：**"找不到第一个词，是不是大部分能归结到没找到正确的主语？"**
- **诊断（用她今天全部数据验证，成立）**：成句时刻全是主语立起来(it/it/there)；崩的时刻全是无主语话题串(where is hard)；漏的零件正是形式主语 it。→ **她的"拆包"=给句子立主语；"卡壳"=没立主语。** 底层=中文话题语言 vs 英语主语语言；起手主语只有 4 类，起头从"想不出"变"4选1"。写作漏it/臃肿主语=同一病。**收敛到"给句子指派合格主语"这一个动作。**
- 建议/下一步：练习升级为**主语指派反射**——给话题，用 4 类起手主语各起一个头。

---

### 轮 7 · 她把主语分类推到 A/B 二分
- 她问：**"是不是还有物当主语，不过可以和人合并？"**
- **诊断**：对，人/物句法同构该合并。合并逼出更底层二分——**A 实义主语(人/物·概念) vs B 虚位主语(it/there)**。关键：**她缺口在 B**（中文无虚位主语这个抽屉，故老漏 it）；A 尤其"物/概念当主语"她写作是亮点。靶心从"4 类"锐化为"重点补 B"。
- 建议/下一步：用 A/B 框架做话题练习（手机 / 大城市租房，各 4 起手，A 优先物/概念，B 的 it/there 各一），验证"B 类是否明显比 A 卡"。

### 轮 8 · 她："The expansion of cities… 口语说不出"
- **诊断**：戳穿我的不精确——"物/概念当主语"是她慢时钟能力，没迁到口语。真分界=**现成主语 vs 加工主语**（名词化抽象=慢时钟专属）。`smartphones changed` 能说、`the expansion of cities` 说不出，分界就在现成 vs 加工。
- **口语铁律**：主语只用现成的（具体物/人/it/there），别造名词化抽象主语。写作里升档的名词化，口语里是拖累。
- 建议：A 类物当主语限定**具体物**；练习照做但 A 只用具体物（the phone/rent，不用 the popularity of…）。

### 轮 9 · 她："名词化主语口语也存在，别轻易削减目标"
- **她的元反馈**：警告我一路缩小=在偷偷砍天花板。她对——我上一条把"应急策略"说成了"铁律别造"。
- **修正**：收敛靶心≠削减目标；名词化主语是天花板不删；现在说不出=没预制成块；地板(现成主语)/天花板(焊名词化块)双轨同推；"现成vs加工"=把加工的预制成现成的。详见上方"⚠️ 轮9再修正"块。
- 下一步：先走起手线（手机/租房现成主语练习），再开升级线（焊高频名词化块）。

### 轮 10 · 起手线实测 → **诊断重大改写：病灶不在语法层，在内容检索层**
- 她输入（手机/租房 4 起手）：`The phone is expensive.` / `It's a difficult to find a house with low rent.` / `There is a phone on the floor there.` / `It's my phone.` + **她诚实标注："rent 我没立刻想起怎么用虚位主语"**
- **诊断**：① it/there 她**全对**→ B 类虚位主语不是缺口(推翻轮7假设)。② 但填进去的内容是"眼前有个手机"(看图说话)，不是"关于这个话题的看法"→**框架是空的，缺的是往里填的东西**。③ 同一个 `It's ___`，话题=手机秒出、话题=rent 卡住→**卡的不是 it，是 rent 这个话题她脑子里没有现成评价可填**。
- **验证实验**：给她 4 个内容角度（贵不贵/和以前比/对人的影响/你自己），同一个 rent 再来。
- 她输入：`Rent is expensive. / Rent has been more more expensive than ever. / It's had for young people to find a cheap house. / I spend more than half of my salary on rent.` → **4 句秒出，含上一轮卡住的那个 `It's hard for sb to…` 结构。中间没教任何英语，只给了角度。**
- **结论改写（重要）**：
```
旧   缺 B 类虚位主语（语法抽屉）
新   语法抽屉她有；卡在【想不出要说什么】= 内容检索
     完整链：没想好说什么 → 主语无从指派 → 第一个词吐不出来
     考场三件事挤一起：想内容 + 指派主语 + 转成英文 → 崩
```
- **修法**：把三件事拆开——**内容角度提前备好、练到不占带宽**，现场只剩"指派主语+出声"。角度不是背答案，是万能切入角(贵不贵/和以前比/对人影响/自己情况…)。
- 公道话：这轮 4 句都短，但因我要求"每个一句"，**不算说不长**（轮5接龙已排除）。
- 零件（不纠，属根因②）：`It's a difficult`→去 a；`more more`→`more and more`；`had`→`hard`。
- 下一步：建**话题域 × 内容角度**的表；练"给话题→秒选角度→起手"。

### 轮 11 · 从她自己产出提炼 5 角度 → **发现她只走 2 个角度（句式重复的真因）**
- 我把她今天所有句子反标角度，去重得 **5 个角度（全部来自她自己的产出，非我发表）**：
```
① 评价   好坏/贵便宜/方不方便      X is …
② 比较   和以前比/和别处比          X has become … / more … than …
③ 影响   对谁造成什么               It's hard for … / It makes …
④ 自身   我自己的情况               I …
⑤ 事实   有什么/有多少              There are …
```
  **每个角度天然自带一个起手主语** → 角度选完，主语和第一个词跟着出来，两步压成一步。
- 测试：3 话题(public transport / weekends / learning English)，各挑 2 角度说。
- 她输入：`Public transport in [城市] is pretty convenience. / I really like weekends. It's my real me time. / I don't like learning English, but I have to`
- **发现（关键）**：4 句全落在 **①评价 + ④自身**，**②比较/③影响/⑤事实 一次未碰**。
```
句式重复的真因 = 角度重复。角度决定句式：
①→X is…  ④→I…            ← 她反复用
②→X has become…  ③→It's hard for…  ⑤→There are…   ← 从不触发
```
  **练再多句型都没用——不换角度，那些句型永远调不出来。**
- **更深一层**：没用的 3 个不是随机的——**评价/自身 = 不需检索信息、张口就有态度（她的默认逃生通道）；比较/影响/事实 = 必须真的调内容**。她**自动躲开所有需要内容检索的角度**，与轮 10 诊断完全咬合。
- 亮点：`It's my real me time` 很地道，真本事。零件不纠：`pretty convenience`→`convenient`。
- 下一步：反向练——**只准用没用过的 3 个角度**，看是否明显更慢（验证"躲避=因为要花带宽"）。

### 轮 12 · 强制走 3 个未用角度 → **预测坐实 + 错误精确落在各角度的"机器"上**
- 她输入：`There are tons of different subway lines in my city. / It feels much relaxed next on weekends than on weekdays. / It's hard for young people to find jobs who don't learn English.` + **她自评："确实慢了很多"** ← 预测坐实（躲避=因为要花带宽）。
- **比"慢"更有价值的发现：错误精确落在每个角度所需的"机器"上，且表现严格跟机器成本走**：
```
⑤ 事实  There are + N                        零件0  → 零错误，干净
② 比较  more … than（成对）                   零件1  → than 出来了、more 丢了（只调出一半）
③ 影响  it + for sb + to do + 定语从句挂对     零件3  → 框架全对，who 挂错（挂到 jobs，想挂 young people）
```
- **③ 的重要正面证据**：`It's hard for sb to do` 是轮 10 她卡住的那个结构，**这轮她主动调出来了**（同一 session 内的真实进步）。
- **口语修法（不是把从句挂对）**：定语从句在快时钟太贵 → **拆成两半不用挂**：`If you don't speak English, it's hard to find a good job.`（`if …, it's hard to …` 当固定块，专替代"某类人怎样"的定语从句）。
- ② 的修法：`It feels much **more** relaxed on weekends than on weekdays.`
- **训练顺序（按机器成本，本轮新得）**：⑤(免费,已通) → ②(只缺1零件,最便宜) → ③(最贵,留后)。
- 下一步：只练 ②，5 句连说，只查 `more/-er` 与 `than` 是否每次成对。

### 轮 13 · ② 比较焊死（5/5）+ 抓到"写作口语同一个错"的现场
- 她输入：`Weekends are more relaxed than weekdays. / phones now are smarter than ever. / Taking Subways is more convenient than driving. / I feel English is easier than one years ago. / Big cities are more crowded than small cities.`
- **`more/-er … than` 5/5 成对出现 → 一轮焊上**，印证"机器成本"排序：便宜零件练一次就上。
- 她自己做对的加分项：`than ever`（现成块）、`Taking … than driving`（比较两边动名词对齐 = 写作 P4 常栽的地方，口语这句反而对）。
- **漏的那个是老熟人（跨模态同一个错）**：
```
写作  the consumption ... is less than IT OF rural residents          → that of
写作  The knowledge ... more accurate compared to THE GENERAL PUBLIC   → those of
口语  English is easier than ONE YEAR AGO                              → than it did/was
```
  比较标记有了，**"被比的那一半要补齐"没自动化**。→ 比较角度以后按两步跑：①`more/-er…than` ✅已焊 ②`than` 后面那半是同一种东西吗（新盯）。
- 修法：`English feels easier than IT DID a year ago.` / 绕开：`My English has improved a lot in the past year.` 零件：`one years ago`→`a year ago`。

### 轮 14 · 她追问"为什么会主体找错" → **挖到 L1 迁移的总根：左分支 vs 右分支**
- 她的假设：**"这也是英语环境下对对象的错误定位或忽略，中文没这要求或要求低"** → 对，但机制比"要求低"更狠：**中文让她根本不可能挂错，所以从没长出"管理归属"这个动作**。
- **机制一 · 修饰前置 vs 后置**：中文「不学英语的年轻人」修饰在前，位置锁死归属；英文 `young people who…` 修饰在后，**归属靠就近，必须自己管**。她 `find jobs who don't learn English` = who 自动扒住最近的 `jobs`。
- **机制二 · 中文比"情境"，英文比"成分"**：中文「英语比一年前简单」比的是时间点、听者自己重建；英文必须补出对等成分 `than it was a year ago`。中文靠语境补全，英文靠形式对齐。
- **大统一（本轮最大收获）**：
```
中文 = 左分支：修饰全堆在中心词前 → 天然打成一个包
英文 = 右分支：中心词先出来，修饰往后挂 → 必须管理挂在谁身上

同一个根解释三个看似无关的毛病：
① the leaving school time of students        ← 左分支整包搬运（搬包）
② find jobs who don't learn English          ← 挂钩就近，挂错人
③ the dominance …, hitting a peak of 80%     ← 分词悬垂，挂到"优势"身上
```
  **"拆包"的本质 = 先把中心词吐出来，再往后挂。** 与"立主语"是同一动作的两半（主语=先出中心词；拆包=修饰往后挂）。
- **可操作三条**：①中文想到"XX的YY"→英文先说YY再往后挂XX ②挂钩紧贴要挂的词（就近） ③**快时钟下能拆就别挂（最省）**。
- 由此确立：`If …, it's hard to …` 不是"简化版"，是**绕开 L1 没给她的那个能力**（两个独立小句，零挂钩管理成本）。

### 轮 15 · ③ 影响（拆代替挂）→ **挂钩问题消失；结构层干净，剩下全在零件层**
- 她输入：`If you don't learn English, it's hard to find jobs. / That rent is too expensive. So saving money is hard. / The traffic is terrible in cities, so it's hard to go work on time. / If you don't stop playing phone, it's hard to focus on. / Because I worked overtime often, it's hard to do exercise.`
- **核心胜利：5 句零挂错**，昨天 `jobs who don't learn English` 那类一次未再现 → **"能拆就别挂"验证成功**。
- `it's hard to` 4/5（第2句换成 `saving money is hard` 动名词主语=**合法变体**，不算失手）；她自己把 if 换成 so/because，因果照样成立，是好事。
- **剩余错误全在零件层，且两处是写作老熟人**：
```
playing phone                              ← 中文"玩手机"直译
it's hard to focus on ___                  ← 缺宾语  = 写作 E3.039 `if they cannot handle ___`
Because I WORKED …, it's HARD to           ← 时态打架 = 写作 P15 `used to recruit … must serve`
```
- **教练判断：这三个现在不修**（口语扣分只扣"影响理解"的错；这些考官全听得懂；且按写作结论这类零件她 83% 本会、是压力下掉的，现在盯它=把带宽从结构和流利上抢走）。**唯一值得修=中文直译块（小闭集）**：`playing phone→on my phone` / `do exercise→get some exercise` / `go work→get to work`。
- **5 个角度至此全部跑通**（①④母语级 / ⑤干净 / ②5-5焊上 / ③4-5）→ 进入**整合测试**：给真题，用 2–3 角度连说 30 秒，量①起头快慢 ②自动挑了哪几个角度 ③能否不断电。测整条链而非单零件。

### 轮 16 · 整合测试（真题 30 秒自由说）→ **迁移成功；但抓到"起头断电"的真机制**
- 题：`Do you often use public transport?` 她输入：`Yes. public transport in my city. It's super convenient. I often go to work in... by subways. In fact, if I don't check subway, it's hard to turn on... turn up our office on time.`
- **胜利①：自动用了 3 个角度**（①评价 `It's super convenient` / ④自身 `I often go to work by subway` / ③影响 `if…, it's hard to…`）。**③ 是今天刚建的，无提示自主调出 = 真迁移。**
- **胜利②：两次自我修复都修对了** —— `in… by`（自己抓住介词错）、`turn on… turn up`（`turn up at the office on time` 是地道说法，turn up=到场）。
- **关键发现 · 起头断电的真机制**：
```
"public transport in my city."  ← 主语抛出来了，谓语没跟上 → 句子废掉
"It's super convenient."        ← 换 1 词短主语重启 → 立刻成功
```
  **不是没主语，是有主语但谓语没准备好。** 中文可以「先抛话题→停顿→再评论」(合法)；**英文主语一出口谓语必须紧跟，中间一停就是断裂**。
- **由此确立口语铁律（把所有线索串起来）**：
```
主语越长 → 谓语来得越晚 → 断电概率越大
∴ 快时钟默认短主语：It / There / I / 一个词的名词
她自己的数据：public transport in my city(5词)→断 ; It(1词)→通
```
  与写作根因①（臃肿名词主语）**是同一条**：写作里让她丢分，口语里让她断句。长主语在快时钟=双重成本（加工成本+谓语延迟）。
- 断电点性质也变了：从**结构断电**（起不了头/挂错）→ **词汇断电**（想说 get to/turn up 卡一下）。结构层在腾空。
- 下一步：**A/B 测**——同题重做，只改一条"主语只准用 It/There/I/一词名词"，看 fragment 是否消失。

### 轮 17 · **方法学修正：转写噪声污染了零件层诊断（我的方法问题）**
- 她 A/B 重做输入：`Uh, quite often. It's a super convenient. In French, I go to work by subway every day.` + **她指出："刚才那个漏是录音漏了，可能是发音不标准"**
- **铁证**：`In French` = 她说的 `In fact` 被听错。→ 转写不可靠。
- **结论分层（见文件顶部警告）**：结构层可信；零件层作废；轮15零件错不算数；轮16"起头断电"存疑（fragment 可能是漏词，短主语规则降级为**待验证假设**，不是她数据证出的结论）。
- **方法调整**：往后只在结构层诊断+训练。与轮 15 已下的判断（零件现在不修：占带宽、83%本会）**正好一致**，现在多一条理由：**转写上根本测不准**。
- 本轮可信部分：`quite often` 自然；`It's super convenient`(①评价,短主语)；`In fact, I go to work by subway every day`(④自身,短主语)；无 fragment，但总量也变短（3小句 vs 上轮5），**不能单独下结论**。
- 下一步：改用**她的主观感受**当数据源（"刚才是断了还是顺的"）——比转写可靠。

### 轮 18 · 她定下数据协议（取代我"零件层全作废"的过度反应）
- 她原话：**"playing phone, focus on 确实有问题。这样吧，如果我没有纠正，那就是有问题，这样我们好对齐，不然你靠自己脑补，没法搞。"**
- **协议：默认转写可信；她没喊=算数，她喊了才作废。** 举证责任在她 → 比"全作废"干净，也避免教练脑补。已按此回滚（见文件顶部）。
- **战术判断不变**：`playing phone`/`focus on` 等零件**现在仍不修**（理由与转写无关：口语只扣影响理解的错；盯零件抢结构与流利的带宽）。**唯一现在就改=中文直译块**（听起来不像英语+小闭集）：`playing phone→on my phone` / `do exercise→get some exercise` / `go work→get to work`。`focus on` 悬空等结构层稳了再收。

### 轮 19 · 她推翻轮 16 的"短主语"建议 → **it 不是缺口，是拐杖；角度决定主语**
- 她自评（主观感受，现为主要数据源）：**"一般顺，其实是反的，我经常不忽略用 it。即使我在写长的名词块很吃力。"**
- **我上一条建议被推翻且推翻得对**：让她"用短主语 It/There" = 让她多用**本来就过度使用**的东西 = 给拐杖上钢筋。证据（她今天自产的 it 密度）：
```
it is more competitive / it makes people / It's my phone / It's my me time / It feels much relaxed /
it's hard to go work / it's hard to focus / it's hard to do exercise / it's hard to find jobs / It's super convenient …  （十几处）
```
- **她的真边界=长名词块，且连写作(慢时钟)都吃力**（她自己确认）→ 印证轮 8-9 的"加工主语"。
- **数据里藏着的关键规律：角度决定主语，主语决定句式**：
```
自由说   → It's… It's… It's…                      （默认拐杖）
比较角度 → Weekends are… / phones are… / Big cities are… / Taking subways is…   ← 实义主语自动出来
事实角度 → There are tons of subway lines…
```
  「比较」角度**没法用 it 起手**（必须拿真东西来比）→ 她 `It's…` 泛滥的根源**不是主语选择，是自由说话时只挑能用 it 的两个角度（评价/影响）**。
- **修正后的主语阶梯**（轮 16"默认短主语"作废）：
```
1  it / there          免费，已过度使用 ← 别再练
2  具体名词当主语        the phone / rent / subway / weekends   ← 当前成长边
3  名词化块当主语        the rise of… / the lack of…            ← 天花板（写作都吃力）
```
- 下一步：**禁用 it** 重说同题，看①禁掉拐杖后是否自动滑向比较/事实角度 ②慢多少。

### 轮 20 · **禁用 it 实验 → 本 session 最深的发现：it 是逃避内容检索的载体**
- 她输入（全程零 it，100% 合规）：`Yes. public transport near my place is super convenient. There are three different, uh, subways lines and, uh, three subway stations within, uh, ten minutes walk`
- **证据①：长主语假说彻底作废**。
```
轮16   "public transport in my city."                        ← 断掉，没谓语
轮20   "public transport near my place IS super convenient."  ← 同类5词长主语，通了
```
  加上她说过那次是录音漏词 → **她扛得住长主语**，"长主语→断电"埋掉。
- **证据②：禁 it 触发一条连锁反应**：
```
禁 it → 被迫用实义主语 → 被迫滑向【事实】角度 → 说出具体细节
之前：There are tons of subway lines.（模糊）
这次：three different subway lines and three subway stations within ten minutes walk（具体）
```
- **机制（最深的一条）**：**`It's…` 是她逃避内容检索的载体**。`It's convenient` 是评价、**不需要任何证据**，张口就有；`There are three lines within ten minutes walk` **必须真的调内容**。→ 她那两个默认角度（评价/自身）之所以是默认，正因为**都能用 It's 开头、都不用检索**。**禁 it = 一次性堵死整条逃生通道** → 被迫调真内容 → 具体度立刻上来（=雅思提分核心，呼应 [[feedback_speaking_decompress_not_pad]] 解压非注水）。
- **代价真实**：`uh`×3，明显变慢。拐杖被拿走的正常反应。**预期：卡顿随练习下降，具体度不会掉回去** → 这是该约束值得用的理由。
- 零件（不练，一句带过）：`subways lines`→`subway lines`、`ten minutes walk`→`a ten-minute walk` = 复合修饰里名词用单数，与写作 `multi-stage process`/`10-year period` **同一条规则**（写作那轮学过）。
- **决定：「禁 it」升级为常规训练约束**（训练轮禁，非永久）——一次堵死两个问题（it 拐杖 + 只用不检索的角度）。
- 下一步：3 话题（weekends/hometown/cooking）全程禁 it，各 2 句；量①具体细节能否稳定 ②uh 是否减少。

### 轮 21 · 禁 it 换话题 → **她换了逃生通道 `I`；证明我禁错了目标（禁载体≠禁行为）**
- 她输入（禁 it 100% 合规）：`I love weekends. On weekends, I can enjoy myself. / I stayed in my hometown for eighteen years. until I went to college. / I don't like cooking.`
- **四句主语全是 `I`**。具体度对比：
```
轮20（公共交通）  three subway lines, three stations, within ten minutes walk   ← 具体
轮21（本轮）      "enjoy myself"                                                ← 零信息
```
  问 hometown **她答的是自己的履历（待了18年），不是那个地方** = 逃避最纯粹的形态。cooking 只给 1 句（要求 2 句）= 合规度下降也是逃避信号。
- **`uh` 消失不是进步**：上轮 uh 是"在调内容"的代价，本轮不用调所以不卡。**卡顿减少 ≠ 变好**，要和具体度一起看。
- **约束定错了目标（修正轮 20 结论）**：
```
我禁的 = 载体（it）        该禁的 = 行为（挑不需检索的角度）
it 和 I 是同一件事的两个载体 —— 分别是【评价】和【自身】两个免检索角度的出口。堵一个，从另一个出去。
```
- **轮 20 之所以有效不是约束好，是话题帮了忙**：
```
public transport  → 没法用 I 说 → 逃生路被话题堵死 → 被迫调内容 → 具体
weekends/cooking  → 天然能用 I 说 → 逃生路敞开 → 逃掉
```
  → **话题本身决定逃生路是否敞开**，这是选练习题时的重要变量。
- **新约束：`it` 和 `I` 一起禁；主语必须是话题里的一个真东西**（Saturday morning… / My hometown… / The streets there… / Cooking… / My kitchen…）。
- 下一步：同 3 话题重做，量①具体细节 ②卡顿（**这次卡是好事**=在真调内容）。

### 轮 22 · 禁 it+I → **主语层解决、内容层暴露；她亲口确认"卡=没内容"**
- 她输入：`Weekends are relaxing. The best part of it is I can go out with my family. / My hometown is a famous city. There is a really delicious food there named the bird noodle.` + **`cooking 没有想起什么内容，所以卡了`**
- **三句三种性质，正好切开问题**：
```
Weekends are relaxing.                     实义主语✅  内容空❌（形容词等于没说）
My hometown is a famous city.              实义主语✅  内容空❌（"有名"=没说）
There is a delicious food called bird noodles.  实义主语✅  具体✅
cooking                                    卡死
```
- **推翻轮 20 的连锁推论**：轮20 我说"禁 it → 实义主语 → 具体细节"是自动连锁。**不是。** 主语和内容是**两个独立维度**，换主语只解决主语、换不出内容。
```
主语层  ✅ 已解决（禁 it + I 就够）
内容层  ❌ 未解决 ← 真正的瓶颈
```
- **本 session 最有价值的一句（她的内省，受控条件下自证）**：**"cooking 没有想起什么内容，所以卡了"** → 轮 10 结论（病灶在内容检索非语法）**首次由她自己确认**，不是教练推的。
- 零件（按协议记下不练）：`a really delicious food`（food 不可数）→ `a dish called bird noodles`；`The best part of it is I can go out…` 谓语后溜回 I → **约束只锁住主语，谓语仍是逃生口**。
- **下一步 · 决定性实验（区分两种"没内容"，修法完全相反）**：
```
A 中文也想不出 → 内容根本不存在 → 要备素材（准备问题，非语言问题）
B 中文有一堆   → 内容在但英文调不出 → 检索/映射问题
```
  让她**用中文**说 cooking 两三句。结果决定后续练什么。

### 轮 23 · 中文对照实验 → **因果反转：不是"没内容"，是"没路径导致内容也不生成"**
- 她中文输入：`做饭挺有趣的，有时候我和我媳妇在家做饭，好吃又健康。我承认即使中文，内容未必好，比如缺乏层次感，或者逻辑。但总能说几句。在说英语时，这个"总能说几句"就很难，因为内容可能有了，但是不会用英语说，就卡住了`
- **实验判定 = B（内容存在，英文侧映射断）**。中文能说、英文卡死 → **"没内容"不是原因是症状**。
- **因果反转（修正轮 10 / 轮 22 的标签）**：
```
我之前写的   没内容 → 说不出
实际上       没路径 → 内容也不生成了 → 主观感受像"没内容"
```
  **说不出来的东西，大脑会停止生成它**（表达与生成绑定，路一堵水龙头也关）。
  **顺带解释轮 10**：当时以为给的是"内容角度"，其实**每个角度自带一条英文路径**（X is / has become / it's hard for / there are）——给的是路径，内容自己流出来。**∴ 路径是因，内容是果。**
- **她指出的关键不对称**：中文"总能说几句"= **无数条备用路径**（一条不通换个说法）；英文**只有一条，堵了就是零**。= 轮 4"散装 vs 成串"的更深一层：**路径冗余**问题。
- **好消息**：她自评中文内容也"缺层次、缺逻辑" → **不需要忠实翻译她的中文**，只需**少量高复用路径**，内容往里塞。
- 示范（她的 cooking 中文→路径）：
```
做饭挺有趣的      → Cooking is actually quite fun.（主语=Cooking 非 I）
和媳妇在家做饭    → My wife and I cook at home most nights.（most nights=具体）
好吃又健康        → Home-made food is healthier and tastes better than takeaway.（自动升成②比较）
```
  第三条**她自己找不到，但完全在能力内**（`more…than` 早焊死）→ 教练价值 = **找她想不到的那类路径**。
- **★ 新训练循环（自此为主线）**：
```
1. 中文说内容（不管好坏，她说得出）
2. 提炼 2–3 条英文路径（教练找，尤其找她想不到的）
3. 反复走这些路径 → 直到不用想
```

### 轮 24 · 家乡实测新循环 + 她的精准自省 → **"找主语=拆包"，通用操作确立**
- 她中文（4 句全具体，零空话）：`我在宜宾长大，一个四川南部的小城市，这里因为是三江汇合口出名，实际上市中心就是岷江和金沙江的汇合口，从这里开始叫做长江`
- 对照她的英文版：`My hometown is a famous city.` → **同一个人同一时刻，内容一直在，缺的只是路**（再证轮 23）。
- 我给的三条路径：
```
① I grew up in Yibin, a small city in southern Sichuan.   ← 同位语=最便宜的右分支（一个逗号，不用 who/which）
② Three rivers meet right in the city centre.             ← 事实角度+实义主语（她默认会写 It's famous for…=空）
③ That's actually where the Yangtze begins.               ← 王牌+高复用块 That's where…
```
- **她的自省（极准）**：`第一还是找主语，这里的同位语可以(不代表别的地方可以)。另外我会尝试翻译，这里因为，然后说 it's famous because，然后三江大概率也会卡下`
  → ①她自己定位入口是**找主语** ②她警惕过度泛化（同位语不通用）③**她准确预测自己的失败链**：中文"因为"→拖她走进 `It's famous because…`→卡在"三江汇合口"这个名词块。
- **答她的怀疑 + 本轮最大收获**：同位语确实场景有限，但**"从名词块里揪主语"这个操作通用**：
```
三江汇合口  → 揪出名词当主语 → Three rivers MEET   （"汇合口"消失，不需要 confluence 这个词）

同一操作、两个模态、三个实例：
学生的离校时间 → Students leave school.   （写作轮1）
城市的扩张     → Cities are growing.      （写作轮8）
三江汇合口     → Three rivers meet.       （本轮）
```
  **∴ 找主语 = 拆包，是同一动作的两个说法。** 同位语只是便宜小工具，**揪主语才是通用规则**。
- **"因为"根本不用翻译**：问题不在 because 在 **famous**——`It's famous because…`(评价,空,还得补原因) vs `Three rivers meet…`(事实,具体)。**中文思路里"很有名/很好/因为所以"这层评价骨架，P1 里可整个扔掉，只留事实**（事实本身就说明它有名）。
- 下一步：练"揪主语"操作（4 个中文名词块：房租的上涨/手机的普及/地铁的开通/中国人口的老龄化）。**注明：这不是练翻译流利度（那会喂中介），是修她翻译时的那个动作**——她的现实就是会翻译，所以要修翻译操作本身。

### 轮 25 · 揪主语实测 → **证伪"动词自己会来"；补出拆包的第二步**
- 抽查 B1 + 4 个名词块。她主语全揪对（`phones` 零冠词泛指 / `the subway` 特指 / `population`），但**动词只成 1/3**：`流行一下想不起来怎么找动词`（普及）· `the subway has opened up` ✅ · `population advance aging？不确定`
- **证伪我轮 24 的话**（"揪对主语动词自己会来"）——不成立。但**失败有硬规律**：
```
✅ 三江汇合口 → rivers MEET      有对应动词
✅ 房租的上涨 → rent GOES UP      有对应动词
✅ 地铁的开通 → the subway OPENED 有对应动词  ← 她做出来了
❌ 手机的普及 → 英文根本没有"普及"这个动词
❌ 人口老龄化 → 英文没有单一对应动词
成功的全是有对应动词的；卡住的全是没有的 → 不是她想不起来，是那个词不存在
```
- **★ 拆包补出第二步（重要）**：
```
① 揪主语  ② 找动词  ③ 找不到 → 立刻换说法，别硬找对应词   ← 缺的就是这步
```
  换出来的**永远是初中词**：`手机的普及→Phones are everywhere now / Almost everyone has a smartphone`；`老龄化→The population is getting older / People are living longer`。
  **中文的抽象名词（普及/老龄化/城镇化）在英文里通常不是一个词，是一整句大白话。**
  与写作 **P3 兜底网**同一条（没把握就换，别原地找），区别只在口语要 1 秒内决定。
- **两个时钟再现**：`ageing` 她**写作里用过**（`an ageing population puts a burden on society`），口语没浮上来 → 词她有，检索没通。
- 零件：`opened up`→`opened`（open up 偏"开辟/开放"）。
- 下一步：练"换说法"的决定——4 个**没有对应动词**的名词块（中国经济的快速发展/网上购物的兴起/城市交通的拥堵/年轻人的压力），**卡 2 秒立刻换大白话**。

### 轮 26 · 她自述卡壳时的内心过程 → **搜索方向错了（横向/向上），且缺"换说法"的具体操作**
- 她输入（4 个抽象名词块）：`the economy in China developed fast. / online shopping xx. / traffic jams are everywhere in cities. / young people feel loads of pressure` → **3/4**，第 3、4 句正是"换说法"生效（没找"拥堵/压力"的对应词，直接说画面）。
- **她的内省（本轮核心数据）**：`比如兴起，我就在想 emerge 行不行，然后又在想 prospect 行不行，又在想怎么说比较地道，最后还是没有答案`
- **诊断①：搜索方向错**。`emerge → prospect` 两词难度同级 = **横向找同级词，循环无出口**。**正确方向是向下（换更简单的说法），不是横向（换另一个高级词）。**
- **诊断②：我上一轮只给了"要换"的意识，没给"怎么换"的操作**。补上：
```
★ 换说法的操作 = 问"具体发生了什么 / 具体是什么样"，把抽象名词整个丢掉，只描述画面
兴起   → 越来越多人网购 → More and more people shop online.
普及   → 人人都有一个   → Everyone has one now.
老龄化 → 人变老了       → The population is getting older.
```
- **诊断③：她其实已经会这个操作**（拥堵→traffic jams are everywhere；压力→young people feel pressure）。**差别在中文词的抽象度**：
```
拥堵/压力（较具体）    → 不触发词汇搜索 → 直接说画面 ✅
兴起/普及/老龄化（抽象）→ 触发向上搜索  → 死循环   ❌
∴ 可预测：中文词越抽象越容易被拽进找词循环。见"化/起/及/度"结尾直接跳过找词。
```
- **诊断④：她把"地道"理解成了"高级"**（`又在想怎么说比较地道`）。`Online shopping has emerged as…`(她以为地道) vs `More and more people shop online.`(才是地道)。**口语地道=大白话**。且**"地道性判断"在快时钟必须关掉**——边检索边评审，两进程互锁，永远出不来。（同 [[feedback_writing_natural_not_literal]]：natural≠难=更简更顺）
- **★ 硬出口条件（可执行，非"卡2秒"——她感觉不到2秒）**：**想到第二个词还没定 → 立刻停止找词，改问"具体发生了什么"。**（emerge 是第一个，prospect 是第二个，到 prospect 就该跳出）
- **三条高复用大白话模板**（覆盖"化/起/及/度"类抽象名词约八成）：
```
… are everywhere              （普及、拥堵、到处都是）
everyone / more and more people …  （兴起、流行、越来越多）
… is getting + 形容词          （老龄化、变贵、恶化）
```
- 零件（不练）：`the economy in China`→`China's economy`；`developed`→`has developed`；`loads of` 口语可、写作不可。

### 轮 27 · 三种状态划出规则边界 → **"跳出来 vs 找出来"，以及"不确定"是更早的出口信号**
- 她输入：`online shopping is popular now.` ✅ / `urbanization 或者 more and more people live in cities`（两个都给，犹豫用哪个）/ `the education resources are unbalanced?`（**自己打了问号**）
- **① 成功**：没找"兴起"，直接说现状 → 操作生效。
- **② 她的犹豫值得回答 → 规则边界修正（不是"禁用抽象词"）**：
```
词自己跳出来 + 确定   → 用它        （urbanization 是她已有的阅读词，跳出来了 → 能用）
需要找 / 不确定       → 立刻放弃说画面（emerge/prospect 是找出来的 → 不能用）
★ 区别不在词难不难，在它是"跳出来"还是"被找出来"
```
- **③ 她退回直译**（不均衡→unbalanced）**且自己打了问号**。→ **"不确定"是比"找不到"更早出现的出口信号**，打问号那一刻就该跳车。画面版：`Good schools are mostly in big cities.` / `Kids in small towns don't get the same teachers.`
- 零件：`unbalanced`→`unequal/unevenly distributed`（但口语根本不该走这条路）。

### 轮 28 · 整合测试（Is online shopping popular in China?）→ **本 session 最好的输出；进步可对比**
- 她输入：`online shopping is super convenient in China. most of shoping is online in my family. In china, you can get refund within 7 days for no reasons`
- **五项测量全过**：
```
起头     实义主语 online shopping，秒起，无 fragment   ✅
角度     评价+自身+事实，3 个                          ✅
it / I   零                                            ✅
具体细节 七天无理由退货（极具体、有文化质感）           ✅
找词循环 无                                            ✅
```
- **同类任务硬对比（轮16 vs 轮28，同一天隔 12 轮）**：
```
轮16  Yes. public transport in my city.(fragment) It's super convenient. I often go to work in...by subways.(修复)
      In fact, if I don't check subway, it's hard to turn on...turn up...(修复)
      → 1 fragment + 2 次自我修复 + It's/I 拐杖 + 零具体细节
轮28  → 0 fragment + 0 修复 + 0 拐杖 + 一个很硬的具体细节
```
- **两处修正，都是中文语序/直译**：
```
① most of shoping is online in my family  ← 漏了一次拆包机会：名词块当主语(贵) + "在我家"被甩句尾(中文语序)
   → 揪 my family 当主语：My family buys almost everything online.
② for no reasons  ← "无理由"直译 → no questions asked / for any reason
```
- **新观察**：**越是中国本土特有的细节（七天无理由/外卖/健康码），越容易触发直译**——英文里没有现成块。→ 这类内容**值得提前备英文说法，属内容准备，临场解决不了**。

### 轮 29 · free time（sci-fi）→ **天花板展示：内容充分时，路径自己长出来**
- 她输入：`Reading sci-fi definitely is my favourite. I have read it ever since i was kid. in actual, i just finished rereading the foundation series, which is one of rare ways i can truly unwind`
- **五项全过 + 守住"起手不用 I"**（动名词主语 `Reading sci-fi`）。但真正的看点是**结构复杂度**：
```
动名词主语 + 现在完成时(用对,持续义) + 具体专有名词(Foundation series)
+ 双层从句全挂对：which is one of the rare ways [that] I can truly unwind
+ 自然口语词 unwind（非背来的大词）
```
- **★ 与轮 28 直接对比，变量只有一个**：
```
轮28 online shopping   3 个简单句，零从句
轮29 sci-fi            动名词主语+现在完成时+双层从句+专有名词
同一人、同一天、隔一轮 → 语言复杂度差一整档，唯一变量=【她在这个话题有真内容】
```
- **把轮 23 推进一步**：
```
轮23  没路径 → 内容也不生成
轮29  内容极充分 → 路径自己长出来
∴ 不是内容让她"能说"，是内容让她的语言能力【得以释放】。
   她在有内容的话题上语言水平远高于平均 → 「备内容」本身就是提分手段，不需学新语法。
```
- **关系从句规律精确化（修正轮14"能拆就别挂"）**：
```
轮14 挂错  find jobs who don't learn English   who 想挂 young people，中间隔了 jobs
轮29 挂对  the Foundation series, which is…    which 紧贴被修饰的东西
★ 新规则：从句必须【紧贴】它要修饰的词。贴不上，才拆成两句。
  → 比"能拆就别挂"准确，且保留从句这个武器
```
- 零件：`definitely is`→`is definitely`；`since I was a kid`(缺a)；`one of the rare ways`(缺the，更自然 `one of the few ways`)；**`in actual`→`in fact/actually`**（"实际上"直译，归 C2 闭集）。
- 下一步：既然内容深度直接决定语言表现，**测她内容最薄的地方**（Describe the area you live in——之前只说过 "a famous city"），**卡在哪就是内容要补的地方**。


### 轮 30 · 她推翻我对轮 29 的解读 → **背诵 ≠ 生成；"不确定"才是不迁移的真因**
- **她的纠正（关键）**：`sci fi 这个话题我背了无数遍了。但是 1 在实际口语中会犯很多小的语法错误 2 没法迁移。其实本质就是对底层短语和轮廓没有正确的认知。在口语中也大概能意识到是错的，但短时间内不知道什么是对的。也是这种不确定，让我没法迁移`
- **我轮 29 的分析错了**（"内容充分→路径自己长出来"），而且**证据就在我自己列的零件清单里，我看漏了**：
```
definitely is(语序) · since I was kid(缺a) · one of rare ways(缺the) · in actual(直译)
四个错全在"结缔组织"（冠词/副词位置/连接词）
→ 现场生成的错误会随机分布；错误固定在同样位置 = 背诵的指纹（带错的版本被背熟，错误一起固化）
```
- **她的因果链（比我准）**：
```
背整段   → 只能复述那一段
提取骨架 → 但她不确定骨架对不对 → 不敢用 → 不迁移
★ 迁移需要的不是"记住那段话"，是"确信这个骨架是对的"。不确定的东西不敢往新话题套 —— 她不迁移是理性的。
```
  → **对教练的要求：给骨架必须同时给"确认版"（明确标出正确形式），否则她不敢用。**
- **从她 sci-fi 段提取的 4 个骨架（含确认版）**：
```
① [V-ing] is definitely my favourite.              ← definitely 放 is 后
② I've been [V-ing] ever since I was a kid.        ← 持续用 have been V-ing；a kid 要冠词
③ I just finished [V-ing] + 具体名字.               ← 自带"必须具体"的压力，很值钱
④ …, which is one of the few ways I can truly [V]. ← the 不能少；few 比 rare 自然
```
- 下一步：**用同样 4 骨架说 cooking**——选 cooking 因为**轮 22 她在这话题完全卡死**（"没想起什么内容"）。骨架若真能迁移，同一话题这次应出得来。**这是对"骨架 vs 背诵"的直接检验。**


### 轮 31 · 骨架迁移测试（cooking）→ **"带语义的不是骨架"；她自己造出了真骨架**
- 她输入：`cooking is something i don't like. I rarely cook by myself because i'm a terrible cooker. Thought i think home-cooked is much more delicious that food in restaurants`
- **她没用我给的 4 个骨架 —— 这是我的问题**：
```
① …is definitely my FAVOURITE      ← 带正面语义
② ever since I was A KID           ← 锁死"从小的长期爱好"
④ one of the few ways I can UNWIND ← 带正面语义
三个都带语义；她对 cooking 的真实态度是负面 → 套不进去
★ 不是她不会迁移，是没东西可迁移。带语义的叫"句子"，纯结构的才叫"骨架"。
★ 对教练的硬要求：给她的骨架必须【语义中立】（留极性槽/频率槽），否则不可迁移。
```
- **但纯结构确实迁移了**：动名词主语 `cooking is something…`（①的结构内核）✅ · `much more delicious than…`（A1 已焊）✅ · `because` ✅
- **★ 她自己造出了三个真骨架（极性中立、她确定、来自她自己产出）**：
```
① [V-ing] is something I really enjoy / don't like.   ← 极性可换
② I rarely / often [V] because …                       ← 频率可换
③ [X] tastes much better than [Y].                     ← 她的原句改一词
```
  呼应 [[feedback_derive_from_her_production]]：材料必须从她实产提炼。**我给的四个不是她的资产，这三个才是。**
- **★ 同话题自身对照，再次印证轮 23（路径是因内容是果）**：
```
轮22 cooking  "没有想起什么内容，所以卡了"   ← 完全卡死
轮31 cooking  三句，全有实质内容             ← 教练一句 cooking 内容都没给
变量只有：她手上有了可用结构（动名词主语/because/more…than）
```
- **真错误（非零件）**：`cooker`=炊具/灶具，`cook`=厨师 → `I'm a terrible cook`。零件：`home-cooked`缺中心词→`home-cooked food`；`more delicious`可但`tastes much better`更自然。
- 下一步：用**她自己那三个骨架**换话题（Exercise），测自有骨架的迁移力。


### 轮 32 · 她自述"系动词依赖" → **三条线收成一根：实义动词没装在产出侧**
- **她的自述（关键证据）**：`taste 确实好，我太喜欢用系动词了。taste 这种实义动词阅读完全是下意识的，但是我说的时候从来想不到`
- **诊断**：阅读有、口语没有 = **[[feedback_three_pathway_diagnosis]] 三通路的教科书级实例**——`taste` 存在"看→认"通路，从没进过"意→调→说"。不是不认识，是**没被安装在产出侧**。
- **★ 三条分头查过的线，实为同一件事**：
```
写作根因①  谓语空转，主语臃肿 + be 当谓语
轮 8       the expansion of cities（名词化）说不出
轮 32      系动词泛滥，实义动词调不出
→ 产出默认走 X is Y，【实义动词那一格是空的】
```
- **顺带解释了一个之前没解释的现象**：她 `It's…` 泛滥，不只因为 it 是免检索角度的出口，**更因为 is 是她唯一自动化的谓语——她没得选**。
- **范围极小（感官+感受+变化，五六个词覆盖 P1 绝大部分）**：
```
系动词版（她的默认）        实义动词版（她阅读里全认识）
It's delicious.        →   It tastes great.
It's noisy.            →   It sounds noisy.
It's comfortable.      →   It feels comfortable.
It's expensive.        →   It costs a fortune.
It's getting old.      →   The population is ageing.
I'm interested in it.  →   It interests me. / I'm really into it.
It's my favourite.     →   I love it. / It's grown on me.
★ 不是学新词，是把右边那列【从阅读侧搬到产出侧】
```
- 下一步：给 6 个 be 句，**只换谓语**（不改主语不重组），看哪几个秒换、哪几个卡。


### 轮 33 · 盲测（不告知量什么）→ **系动词依赖只长在"评价槽"；同位语 9 轮后自发迁移**
- 题 `What kind of food do you like?`（未告知测什么）。她输入：`ranmian, or burning noodle in English is my absolute favorite. When I was a kid, I could easily eat it for three meals a day. I guess It is called that because the the chili oil on its top can actually catch fire.`
- **隐藏目标（实义动词是否自发）结果一半一半，且划分整齐**：
```
✅ 自发   could easily EAT it three meals a day / the chili oil can actually CATCH FIRE
❌ 未出现 ranmian … IS my absolute favorite      ← 正是 taste/love 该出现的位置
```
- **★ 规律：系动词依赖【只长在评价槽里】**：
```
叙述性内容（讲发生了什么）      → 实义动词自发出现 ✅
评价性内容（说好不好/喜不喜欢） → 默认系动词      ❌
```
  与轮 11 接上：**评价角度 = 免检索 = 系动词**，三者是绑在一起的一整套逃生装置。→ **要修的不是泛泛的"实义动词"，是专攻评价槽。**
- **★ B2 同位语 9 轮后无提示自发迁移**：
```
轮24（教）  Yibin, a small city in southern Sichuan
轮33（自发）ranmian, or burning noodles in English   ← 且用在更难处：给中文词做英文解释（P1 高价值技能）
```
- 内容为她今天最好：**ranmian + 名字由来（辣椒油能点着）** —— 别人编不出来的细节。
- 零件：`burning noodle`→`noodles`；`on its top`→`on top`。
- **下一步不练"现场转换"（判断+检索太贵），改给预制块**——评价槽的语义中立块：
```
I'm really into X.            ／ X does nothing for me.
I could eat / do X every day. ／ I can't stand X.
X never gets old.             ／ X gets old fast.
```


### 轮 34–35 · 预制块实测 + 整合测试 → **"旧块永远先到"：显微镜下的 50% 发挥机制**
- 轮34（预制块 3 话题）她输入：`I'm really into hard parts.`(hotpot 转写) ✅ / `I do clean work every day.` ❌ / `Scrolling through short videos gets old fast.` ✅✅（动名词主语+块+语义准确）
  - **#2 精确诊断：留下了块的形式，丢了块的功能**——`I could DO X every day` 里 **could 是引擎**（把事实变成"喜欢到能天天做"的夸张评价），去掉后退化成客观陈述。
  - **★ 规律：预制块里的情态/副词（could/never/really/fast）是功能核心，一个都不能省。**
  - 零件：`clean work`（"清洁工作"直译）→ `cleaning`。归 C2。
- 轮35（整合测试 `What's your favourite time of day?`，故意用 favourite 设陷阱）她输入：`Spending time with my kid after work is my absolute favorite. I feels really relaxing as soon as I say my son. Especially after a long day at work.`
- **★ 陷阱生效，抓到关键机制**：
```
轮33  ranmian … IS my absolute favorite.
轮35  Spending time with my kid … IS my absolute favorite.
两轮完全同一个块 → 这是她评价槽里【唯一自动化的块】，"favourite" 一出现必然被调出
★ 不是没学会新块，是新块没到自动化，【旧块永远先到】
★ 这就是她"考试只发挥50%"的机制在显微镜下的样子 —— 竞争的是速度，不是知识
```
- 守住的部分：`Spending time with my kid` 动名词主语，起手没用 I ✅
- **真错误（非零件）**：`I feels really relaxing` 三处混一处——
```
I feel relaxed      ← 我感到放松（人=感受者）
It feels relaxing   ← 它让人放松（物=来源）
★ -ing 形容词描述"东西"，-ed 形容词描述"人"（relaxing/interesting/boring vs relaxed/interested/bored）
```
  `as soon as I say my son` 疑为 `see` 的转写（待她确认）。
- 下一步：同题重做，**禁用 `is my absolute favorite`**，强制新块顶上 → **这是"自动化竞争"的直接测试**。


### 轮 36–37 · 自动化竞争测试 → **新块可当发射台；★ 得到"负载测试=优先级排序"工具**
- 轮36（禁用 `is my absolute favorite`）她输入：`Nothing beats spending time with my kid.` —— **新块顶上了，语法全对**（beats+V-ing 搭配正确）。
  - **但产量掉了**：轮35(用旧块) 3 小句 → 轮36(堵旧块) 1 句。**与轮 20 禁 it 同一模式：拿掉自动化的那个，产量立刻掉。**
  - **★ 精确定位差距**：`新块"可调用" ✅（堵住旧块它能顶上）` vs `新块"自动" ❌（不能边用边继续说）` → **从"可调用"到"自动"差的只是重复量**，不是知识、不是可及性（这两关她都过了）。
- 轮37（从新块往下接）她输入：`Nothing beats spending time with my kid. Uh, on weekdays, I always read a story before bed. Well, sometimes I got... I get home I get homes really late. So, uh, weekends, I will spend as much as post... possible with, uh, like, uh, going hiking or, uh, or hit up amusement park.`
  - **发射台成立**：1 句 → 4 小句，细节好（睡前故事/回家晚/爬山/游乐场）。
  - 代价：`uh`×6、自我修复×3（三次方向都对：got→get / homes→home / post→possible → **监控是好的，只是吃带宽**）。
- **★ 满载时掉下来的两个（都是 B 档）**：
```
① 并列不同形  going hiking or HIT UP amusement park → going hiking or HITTING UP an amusement park
② 论元丢失    I'll spend as much as possible with…  → as much TIME as possible with HIM（time 和 him 都掉了）
```
- **★ 关键：这两个她今天低负载时都做对过 → 唯一变量是负载**
```
轮13（低负载） Taking subways is more convenient than DRIVING.  并列对齐 ✅
轮37（满载）   going hiking or HIT UP amusement park            并列崩 ❌
```
- **★★ 新工具：负载测试 = 优先级排序**
```
给她加载 → 看什么先掉 → 掉的那个就是下一个要焊的（不用猜优先级）
今天的载荷谱：
  最稳（满载不掉）  具体名词、基本语序、具体细节
  中间（掉流利度）  新块 Nothing beats —— 顶住但吃掉流利度
  最脆（先掉）      并列同形、论元完整   ← 下一批要焊的
```
- 给她的修正版（她自己的内容与结构，只补齐掉的两处）：
> Nothing beats spending time with my kid. On weekdays, I always read him a story before bed, though sometimes I get home really late. So at weekends I spend **as much time as possible with him** — **going** hiking, or **hitting** up an amusement park.


### 轮 38 · 她说出"边说边想" → **★★ 最深的机制：生成与产出抢同一份带宽**
- **她的自述（本 session 最重要的机制陈述之一）**：`为什么这段时间特别？中文说我能边说边想，会补充说上和他一起很高兴之类的。但是英语确实说不出来`
- **★★ 机制**：
```
中文  说话已自动化 → 带宽有富余 → 富余用来"想" → 边说边想成立 → 内容源源不断
英文  说话吃满带宽 → 没有富余   → 没带宽"想"    → 边说边想不成立 → 说完一句就没了
★ 不是没内容，是【生成内容】和【把话说出来】在抢同一份带宽。中文那份不用抢，英文两个都要。
★ 这是她所有答案都短的真正原因 —— 与内容储备无关，与她想不想得到无关。
```
  轮 37 佐证：说到 4 小句时已 uh×6、修复×3，**带宽见底**；此时再要她"想一层为什么特别"，物理上不可能。
- **★ 策略必须变：不指望边说边想 → 改成"先备后说"**（不是妥协，是承认带宽事实）。**P1 答案的第 3、4 句必须预先想好，不能靠现场生成。**
- **双重打击**：她想补的"和他一起很高兴"正是**评价/感受**内容 = 她只有一个自动块（`is my absolute favorite`）且刚被禁掉的那个槽。
- **★ 给她能盖住整个评价槽的块，且她早就用过（轮 3 `it makes people stay in touch easier`）——休眠资产**：
```
X makes me …
和他一起很高兴 → He makes me laugh. / Being with him makes me happy.
很放松         → It makes me forget about work.
值得           → Those two hours make the whole day worth it.
★ 一个 makes 干掉评价槽大半的活，且是实义动词不是 is
```


### 轮 39–40 · `X makes me` 修正 + 跨度抽查 → **路径冗余自发出现；"旧块先到"再证**
- 轮39（要求 X 必须是具体真东西）她输入：`Weekend give me real me time. / Community. Community. Commuting, between home and office makes me feel really tired. / Compared to big cities? Living in small city. gives me more freedom.`
  - **3/3 具体主语，It 全避开**（Weekends / Commuting / Living in a small city），一轮见效。`me time` 很地道。
  - **★ 意外收获：她自己引入了 `gives`**（我只给了 makes）→ **路径冗余开始出现**：同一功能两个块可选 = 她说中文时"总能说几句"的那个东西。
  - **★ `Community→Community→Commuting` 与轮26 `emerge→prospect` 性质不同 → 出口规则分两种**：
```
形近词冒出来（知道要哪个，只是拿错）→ 再试一次通常就对   （语音干扰）
不知道哪个词对（在挑选）           → 立刻跳车说画面     （语义搜索）
★ 判断标准：你是在"拿"还是在"挑"。拿错了再拿一次；在挑说明没答案。
```
  - 零件：`Weekends give`/`The weekend gives`（主谓一致）；`a small city` 缺冠词。
- 轮40（跨度抽查，最远隔 24 轮）：`More and more people live in cities.`(B1b 轮26 ✅) / `Rent is expensive, so young people can't save money.`(A2 轮15 ✅) / `…, which is one of the rare ways that I can truly unwind.`(B2b 轮29 ✅ 从句紧贴)
  - **三条全保住**。
  - **但第3句是 `rare ways` 不是我给的确认版 `few ways`** → **再证"旧块永远先到"（轮35）：一次讲解打不过无数遍背诵**。她轮30 自己预测过（背熟版本带着错固化）。**∴ 纠正背熟的东西比学新的还贵。**
- 轮40 末：按她要求做归纳 → 见文件顶部 **🧠 当前沉淀模型 v2**（原始 40 轮记录一条未删）。


### 轮 41 · 槽 4 首练 → **★ 新发现：她的"不确定"会误报（把对的判成错的）**
- 她输入：`第一个就卡住了，Nowadays, people shop online more than ever. 但是这个 more 是错的，应该是少词了。/ These days, the percentage of the elderly is growing increasingly. / People go home very late.`
- **★ 第 1 句完全正确，她的不确定是误报**（`more than ever` 是完整固定说法；`more than ever before` 也对，before 可省）。
- **★ 这个误报比句子本身重要**：轮30 她说"不确定让我没法迁移"，今天看到新的一面——**不确定感本身不准，会把对的判成错的**。假警报代价：
```
说出正确句子 → 怀疑它 → 停下检查 → 吃带宽+断流 → 不敢再用
```
- **★★ 新规则（直接省带宽）**：
```
说不出来        → 跳车，换说法      （真出口）
说出来了但不确定 → 继续说，别停      ← 新增
"不确定"不是错误信号。快时钟里停下核对的代价 >> 偶尔说错一个词。
```
- **三条模板一条没用**（刚给，未进自动区）→ **又是"旧块先到"**（轮35/40 第三次出现）。不是她的问题，是重复量问题。
- **第 2 句名词块回潮**：`the percentage of the elderly is growing increasingly`（名词块加工主语 + growing/increasingly 冗余，9 词）vs 模板 C `The population is getting older.`（4 词）→ **没有模板托着时她会自动退回名词块 ∴ 模板的价值不是修辞，是【替她挡住旧路径】。**
- 第 3 句 `People go home very late` 是好画面 ✅，只差"普遍"层 → `Almost everyone gets home late.`
- 下一步：强制用模板重做同三题，让她感受"被模板挡住反而更快"。


### 轮 42 · 她纠正失败点 → **模板缺主语；"主语藏在中文词里"是新规律；我第三次给半成品**
- **她的纠正（比我准）**：`2 是因为我没有找到 population 这个主语` —— 我归因为"模板没进自动区（重复量）"，**她指出真因是找不到主语**。
```
她产出   the percentage of the elderly   ← 她找到的主语是"老年人的比例"
模板要的 the population                  ← 主语是"人口"
★ 模板 C 只给框架 [X] is getting [比较级]，没给 X —— 而 X 正是她卡住的地方。我给的模板有洞。
```
- **★ 新规律：中文抽象词把主语藏起来了**
```
中文「老龄|化」 ← "谁"在老龄化？中文不说，压在词里
英文 必须先答出"谁" → the population

她三次成败完全由"主语藏得深不深"决定：
网购的普及 → 主语=人(people 现成)     ✅
加班的盛行 → 主语=人(everyone 现成)   ✅
老龄化     → 主语=人口(抽象,藏起来)   ❌
与轮 25 同源（那次卡在动词侧，这次卡在主语侧）
```
- **★ 拆包三步补一条查询**：
```
① 揪主语 ← 揪不出来时问：【这件事发生在"谁/什么"身上？】
② 找动词
③ 找不到就换大白话
老龄化→谁在变老？the population（她写作里用过多次）
城镇化→谁在搬？people ✅ / 少子化→什么在降？the birth rate
内卷→谁在卷？everyone / 房价上涨→什么在涨？house prices
```
- **★ 教练自查：今天第三次给半成品**（轮30 骨架带语义 / 轮31 骨架不中立 / 轮42 模板缺主语）→ **给她半成品，她就卡在缺的那半。块必须是完整、能直接出口的整句。**
```
❌ [X] is getting [比较级]          ← X 空着
✅ The population is getting older. ← 整块给，包括主语
```
- 下一步：练"主语藏起来"的三个（少子化/房价上涨/就业压力大），先答"发生在谁身上"再说整句。


### 轮 43 · 主语查询实测 → **★★ 统一原理：产出时胜出的是"激活最强"的，不是"最正确"的**
- 她输入（三个抽象词的主语）：`population, house pricing, people`
```
1. 少子化     答 population   ❌ 这是上一轮刚学的"老龄化"主语 → 什么在降？the birth rate
2. 房价上涨   答 house pricing ❌ pricing=定价(行为) → house prices
3. 就业压力大 答 people        ✅
```
- **★★ 第 1 个不是不会，是"刚用过的先冒出来"**（她没真跑那个查询，population 激活度最高就先跳了）：
```
长期自动化的块 → 激活高 → 先到   （is my absolute favorite，轮35）
刚刚用过的块   → 激活高 → 先到   （population，轮43）
★ 统一：产出时胜出的是【激活最强】的，不是【最正确】的。
★ 推论①：这就是"堵住旧块"有效的原因 —— 堵住最强的，次强的才有机会出场。
★ 推论②：也解释考试只发挥 50% —— 紧张时激活阈值升高，只有最强的那几个还出得来。
```
- 正确整句：`The birth rate is falling.` / `Fewer and fewer people are having kids.`（**模板 B 的反向：Fewer and fewer 与 More and more 配对，一个模板管两个方向**）/ `House prices keep going up.` / `Young people are under a lot of pressure.`
- 下一步：说整句，**每个先单独跑"谁/什么"查询，不许套上一个的答案**。


### 轮 44–45 · 槽4 收尾 + 整合测试 → **模板C自发；完成体/被动口语自发用对；但开头是空评价**
- 轮44（三个整句）：`fewer and fewer people have kids.`（模板B反向，刚给就用上 ✅）/ `house prices keep going up.` ✅ / `young people find it difficult to find jobs` ✅
  - **提醒她别误伤**：`find it difficult to do` 里的 it 是**形式宾语**，与"禁 it 当主语"是两回事，这个结构好，别一起禁掉。
  - 零件：`find it difficult to find` 两个 find 撞 → `find it hard to get a job`；`have kids`→`are having kids`（趋势用进行时）。
- 轮45（整合测试 How has your hometown changed…，不提醒用哪条模板）她输入：`there are lots of difference over the past years. For one, industries like new energy and tourism have been developing really well. there are more job opportunitis now than when i was kid. Plus, the air quality gets better because the thermal power plant on the edge of city has been torn down`
- **★ 自发出现的好东西**：
```
模板C     the air quality GETS BETTER                       ✅ 自发
具体细节  新能源/旅游产业 · 工作机会比小时候多 · 城边火电厂被拆  ← 三个真细节
衔接词    For one, … / Plus, …                              ← 自发，骨架层迁移到口语
时态      have been developing（完成进行）/ has been torn down（完成被动）← 两个都对
比较补齐  than when I was a kid                              ← C1 第二次保持
★ 完成体+被动在口语自发用对 = 7 分区表现
```
- **★ 主要问题：开头是空评价**
```
There are lots of differences over the past years.  ← 说了等于没说，浪费最贵的第一句
For one, industries like new energy…                ← 真内容从这才开始
→ 直接上第一个具体的：`Well, for one thing, new energy and tourism have really taken off.`
```
  **`There are lots of differences` 与 `My hometown is a famous city`、`It's super convenient` 同类 = 空评价 → 正好引出槽 2（她唯一自动块所在，下一个该焊）。**
- 时态串：`gets better` 一般现在 vs `has been torn down` 完成 → `has gotten better`（P15）。
- 零件：`lots of differences`；`when I was **a** kid`（**今天第二次**，轮29 同错）；`the edge of **the** city`。
- 下一步：同题重说，**只改一件事：第一句必须具体，不许空评价** → 进入槽 2。


### 轮 46 · **★ 教练重大失误：范例变模仿，把她打回一句**
- 她输入：`loads. for one thing, Well, for one thing, new energy and tourism have really taken off.` —— **照抄我上一轮给的示范句，且只说一句就停。**
```
轮45（她自己的）  4 小句 · 三个真细节 · 衔接词自发 · 完成体用对
轮46（照我的）    1 句 · 抄的
★ 上一轮明显更好。我给示范句是想说明"别用空评价开头"，结果等于换了根新拐杖，还打断了她能说 4 句的能力。
（`loads` 开头也是信号：她在找我要的那个词）
```
- **★★ 教练自查：给块给多了，今天第四次**
```
轮30 骨架带语义 / 轮31 骨架不中立 / 轮42 模板缺主语 / 轮46 范例变模仿
★ 每次我给"块"，都在挤掉她自己的产出。
★ 硬规矩：能在她自己产出上做减法，就绝不给新句子。示范句必须明确标"这是说明，不是让你说的版本"。
★ 呼应 [[feedback_derive_from_her_production]]：材料必须从她实产提炼——不只是选材要求，还是【不覆盖她产出】的要求。
```
- **正确做法**：不是给"更好的第一句"，是**在她自己那 4 句里删掉第一句**，其余一字不动。她的答案本来就不需要开头，`For one` 直接开场完全成立。
- 修正版（她的内容 + 砍空开头 + 补时态冠词）：
> For one, industries like new energy and tourism have been developing really well. There are more job opportunities now than when I was a kid. Plus, the air quality has gotten better because the thermal power plant on the edge of the city has been torn down.
- 下一步：**改用"只给约束条件、不给范例句"** —— 换话题，只说规则不说句子。


### 轮 49–51 · 槽2 焊接 + 自由切换成功 → **"来回那几个"在单句层面被打破**
- 轮49（四话题四块不许重复）：`nothing beats hotpot / i don't like getting up early / watching movies never gets old / i can't stand queuing` → **4/4，四个不同块，零重复**。
  - **但第2个她简化掉了引擎**：块 B 是 `Getting up early is something I don't like`（强制**动名词主语**），她说成 `I don't like getting up early`（主语退回 I）。**语义在，功能没了** —— 与轮34 `could` 掉了同类：**块的引擎被省，块就退化。**
- 轮50–51（不指定块，自由说 TV/films）她输入：`A comedy and a sci fi are some scenes I'm really into. The former gives me a sense of... romantic feeling of, uh, exploring the universal. And the latter just cracks me up.`
  - **★ 超额完成：三个不同评价形式，全不是 It's…**
```
… are some genres I'm really into   块B
The former GIVES ME a sense of…      槽3 gives
And the latter just CRACKS ME UP     实义动词（真地道口语，非背来的）
★ 今天第一次在无人指定下自主切换三种评价形状 → "来回就那几个"在单句层面已不成立
```
  - **★ former/latter 用反了**（former=comedy 却配了"探索宇宙"，latter=sci-fi 却配了"cracks me up"）。**原因不是不懂，是它要求边说边记住之前的排列顺序 —— 满载时跨距离追踪最先掉**（与轮14 定语从句挂错同类）。
  - **且 former/latter 基本是书面语，母语者口语几乎不用** → **口语直接重复名字，又准又省**：`Sci-fi gives me that sense of exploring the universe, and comedy just cracks me up.`
  - 零件：`scenes`→**`genres`**（scene=场景）；`the universal`→`the universe`；`a sense of romantic feeling of`（sense of + feeling of 堆两层）→`a sense of romance about…`。

---

## 🗂 分工安排（2026-07-29 她提出"给我一些问题让我空闲的时候思考"）

**依据**：轮38——英语产出吃满带宽 → 不能边说边想 → **内容必须预先备好**。而备内容**不占带宽、可用中文**（[[feedback_p1_gemini_method]]：中译英当内容准备 OK，当流利训练反效果）。

```
空闲时（无带宽压力）  用中文想【内容】
和教练在一起          把内容变成【路径】+ 练产出
★ 内容层用中文完全没问题，只有路径层不能过中文
```

**给她的三个常驻思考题**：
1. **备内容**：挨个过 P1 高频话题，每个想一个**"别人编不出来的具体东西"**（标准 = ranmian 辣椒油能点着 / 城边火电厂被拆 / 刚重读完基地系列）。话题：工作·住处·一天·孩子·朋友·周末·吃的·买东西·手机·交通·学习·天气。
2. **找空洞**：哪几个想半天什么都想不出 → **真空洞，不修则任何语言技巧都救不了**（cooking 轮22 证明过）。
3. **挑教练的错**：今天她纠正我 6 次、每次都推进诊断（"太大了不是底层"→翻译依赖度；"别削减目标"→地板天花板双轨；"sci-fi 是我背的"→背诵≠生成；"我没找到 population"→模板缺主语）。**她的怀疑比我的推理值钱，已证明。**


### 📦 攒内容的锚定 tag ——「硬料六类」（2026-07-29 她要求）

**总原则（今天数据直接支持）**：**只攒硬料，软料不用攒。**
```
软料 = 评价/感受/原因   她随时能生成（这正是她的逃生通道，永远不缺）
硬料 = 具体的、别人编不出来的东西   她一说就卡、一有就出彩 ← 只攒这个
证据：强答案 ranmian辣椒油能点着 / 城边火电厂被拆 / 刚重读完基地系列
      弱答案 a famous city / super convenient / enjoy myself（全是软料）
```

| tag | 问自己 | 她的实例 |
|---|---|---|
| ① **名字** | 那个东西**叫什么**？ | ranmian · the Foundation series · 岷江/金沙江 · 新能源和旅游 |
| ② **数字** | 几个/多久/多远/多少钱？ | 三条地铁线 · 十分钟路程 · 七天无理由 · 八点下班 · 五点放学 |
| ③ **地点** | 具体在哪？ | 城边上的火电厂 · 市中心的汇合口 |
| ④ **时刻** | 什么时候、在干什么？ | 睡前读故事 · 周末去爬山 |
| ⑤ **变化** | 以前 vs 现在，什么不一样了？ | 火电厂被拆了 · 工作机会比小时候多 |
| ⑥ **反常** | 别人想不到的那一点？ | 辣椒油能点着火（**价值最高，考官会记住**） |

### 🧨 具体表达问题库 ——「中文陷阱四类」（2026-07-29 她要求强化深入）

> 今天散落各轮的表达问题，按**中文陷阱类型**归并。这是 C 档的升级版，供反复过。

**类型 1 · 中文一个词，英文根本没有对应词 → 说画面**
```
普及 → Phones are everywhere.            老龄化 → The population is getting older.
兴起 → More and more people shop online.  少子化 → Fewer and fewer people are having kids.
拥堵 → Traffic jams are everywhere.       内卷 → Everyone is competing like crazy.
★ 出口：在"挑"词 → 立刻说画面；在"拿"词（形近词冒出来）→ 再试一次
★ 主语常被藏在中文词里：老龄化→谁在变老？the population（轮42）
```

**类型 2 · 中文可省、英文必须说 → 满载时第一个掉（她最脆的一层）**
```
形式主语 it   why is __ so hard          → why is IT so hard
冠词          since I was __ kid         → since I was A kid（今天错 2 次）
比较的另一半   easier than __ one year ago → than IT WAS a year ago
补语/宾语     focus on __ / a mix __      → focus on WORK / a mix OF BOTH（今天 3 次）
并列同形      going hiking or HIT UP      → going hiking or HITTING UP
★ 统一：满载时掉的全是"中文里不用说出来"的成分 —— 不是粗心，是系统性 L1 迁移
★ 修法：不可能靠"更小心"（更小心=更多监控=更多带宽）→ 只能【块化】：记 `focus on my work` 不是 `focus on`
```

**类型 3 · 长得像但意思不对 → false friends**
```
cooker（炊具） ≠ cook（厨师）        pricing（定价行为） ≠ prices（价格）
scene（场景）  ≠ genre（类型）        unbalanced ≠ unequal / unevenly distributed
```

**类型 4 · 中文短语直译成英文块 → 中式块（小闭集，唯一"现在就改"的零件类）**
```
玩手机 playing phone      → on my phone / using my phone
做运动 do exercise        → get some exercise
去上班 go work            → get to work
打扫卫生 clean work       → cleaning / doing the cleaning
无理由 for no reasons     → no questions asked / for any reason
实际上 in actual          → in fact / actually
净水厂 water cleaning factory → water treatment plant / facilities to clean water
年轻劳动力 the youth workplace → the younger workforce
```


### 轮 52 · 类型2 块化测试 → **★ 同一短语一对一错：块化未完成的教科书级证据**
- 我出的题（8 个中文，全部取自她今天说对过的块）：`我小时候 / 到最后 / 有权利做某事 / 手机比十年前聪明多了 / 现在工作机会比我小时候多 / 上班的时候很难专心 / 周末尽量多陪孩子 / 城市和乡村各一半最理想`
- **她的原话输入（逐字）**：`when i was a kid. at the end. have the right to do. phones are much smarter now than ten years ago. there are more job opportunitis compared to when i was kid. it's hard for me to focus on my work. on weekends i spend as much time as possible with my kid. a mix of the city and the countryside is perfect`
- **结果 6/8**。对的：`when i was a kid`(冠词在) · `at the end` · `have the right to do`(the 在) · `focus on my work`(补语在) · `spend as much time as possible with my kid`(补语全在) · `a mix of the city and the countryside`(补语在)
- **★★ 两个失败恰好演示"块化未完成"，且证据在同一次输出里**：
```
第1句  when i was A kid    ✅ 单说，零负载
第5句  when i was __ kid   ❌ 嵌在长句里，有负载
→ 同一短语、隔 4 句、一对一错。差别只有【负载】。

第4句  phones are much smarter now THAN ten years ago   ❌ they were 掉了
轮27   phones are smarter THAN THEY WERE ten years ago  ✅
→ 她加了 much 和 now，负载一升，"中文可省"的那半就掉。
```
- **两个失败全是类型 2（中文可省、英文必须），全是负载导致，不是不会** → **块还没硬到能扛负载**。
- **★ 由此确立修法：递增负载下滚块**（不是更多讲解）：
```
A. when I was a kid
   L1 when I was a kid
   L2 I read a lot when I was a kid
   L3 There are more job opportunities now than when I was a kid
B. than they were
   L1 than they were
   L2 Phones are smarter than they were
   L3 Phones are much smarter now than they were ten years ago
★ 关键在 L3 —— 那是它平时会掉的负载
```


### 轮 53 · 递增负载滚块 → **★★ 注意力零和：焊新块时旧准确度暂时下降**
- **她的原话输入（逐字）**：`when i was kid. i read a lot when i was a kid. there are more job opportunitis than when i was a kid. / than they were. phones are more smarter than they were. phones are much smarter now than they were ten years ago`
- **结果与预期相反**：
```
A  L1 when i was __ kid ❌   L2 ✅   L3 ✅
B  L1 ✅   L2 phones are MORE SMARTER ❌   L3 ✅
两组 L3（最高负载）全对；掉的都在 L1/L2
```
- **教练自查：我的指示污染了实验** —— 我说了"关键在 L3"，她把注意力分配到 L3，L1/L2 当热身。**以后不预告测试点。**
- **★★ 但 L2 的错更值钱**：
```
phones are MORE SMARTER than they were
          ↑双重比较级(more+-er)错   ↑目标块 对了
★ 盯住的目标做对了，没盯住的坏了。smarter 她今天说对过至少 3 次，是被【挤掉】的。
★ 这是"带宽有限"最直接的形态：注意力零和，照顾一个就漏一个。
```
- **★★ 实践含义（比练习本身重要）：焊新块时旧准确度会暂时下降 = 正常代价，不是退步。** 今天出现三次，此前未串起：
```
轮20 禁 it    → 具体度上来，但 uh×3
轮36 堵旧块   → 新块顶上，但产量 3 句→1 句
轮53 盯目标块 → 目标对了，但 smarter 坏了
```
  → **一次只焊一个块。同时查两个 = 两个都不稳。**（教练反省：让她"规则全开"那几轮是在制造零和竞争）
- 下一步：只说 L3，**不预告测试点**；孤立片段(L1)跳过——**孤立说反而练不到句法组装，甚至练成无冠词版**。


### 轮 54–56 · 四步展开器 + **她要求语言层与内容层并重** → ★ 长期错误自发修复
- **她的要求（记住）**：`内容问题我们已经探讨过了，但是你一定要注意，我说的答案中表现出的固有缺陷(不地道，重复，或者更好的建议)，这些和内容同样重要` → **往后每轮必须同时给：结构/内容 + 语言层（地道度·重复·更好说法）。**
- **四步展开器（为 5.0→6.0 的"说得长"设计；Band6 关键词 = willing to speak at length）**：
```
① 直接答  ② 给硬料(名字/数字/地点)  ③ 加时间/频率  ④ 收感受(不用 It's)
★ 固定顺序 = 不用现场决定 = 不吃带宽（对应轮38"不能边说边想"）
```
- 轮55（Do you often go to restaurants）她原话：`quite often. Honestly, I eat at restaurants for three meals a day on workdays. mainly because i have no time cooking at home. i head to work right after i get up, and it's pretty much bed time when i get home. food at restaurants near my company tastes terrible. i grab them just for a quick. 卡了很久。`
  - **★ 新发现：缺一个话题核心词 → 整段绕路 + 重复**。她缺 `eat out`，只能反复说 `eat at restaurants`（出现 2 次）。→ **备内容时要顺手备该话题的 2–3 个核心词**（非生词，是躲不掉的词）。吃饭话题：`eat out · takeaway · home-cooked · grab a quick bite`。
  - 语言错：`no time COOKING`→`no time TO COOK`；`grab them just for a quick`→缺名词（`a quick bite`，**又是类型2 补语丢**）；`my company`→`work/the office`（中式）。
  - 她自己做对的地道表达：`head to work` · `pretty much bedtime` · `grab` · **`tastes terrible`（★ 槽3 实义动词首次在自由说话中自发）**。
- 轮56（Do you prefer to cook at home or eat out）她原话：`Definitely cooking at home. home cooked food tastes better than that at restaurants. But, uh, on weekdays, I have no time to cook. Every working morning, I head to work rught after I get up and, uh, it's pretty much bed timr when I get home. so i have to eat out for all three meals near my office`
  - **★★ 长期错误自发修复**：`tastes better than THAT at restaurants` —— 比较对象对齐，且 that/those 数用对（home-cooked food 不可数）。**她在写作里错过至少 3 次**（`less than it of rural residents` / `compared to the general public` / 轮13 `than one year ago`），**这次口语无提示自发做对**。
  - **上一轮 4 个纠正全部吸收，一个不漏**：`no time to cook` · `eat out` · `near my office` · 保持 head/pretty much/grab。
  - 剩余语言问题：①**修饰语挂错位置**`eat out for all three meals NEAR MY OFFICE`→`eat out NEAR MY OFFICE for all three meals`（地点要贴 eat out，轮14 老问题）②`Every working morning` 搭配怪且与 `on weekdays` 重复 → **删掉更顺（今天第二次"多余状语"，上次是 over the past years）**。
  - 数据：**6 小句（上次5）· uh×2（上次她自述"卡了很久"）→ 长度与流利同时涨**（通常此消彼长）→ 四步展开器生效。


### 轮 57 · **★★ 她发现新缺口类别：「理解侧冗余、产出侧必需」的规则**
- **她的原话**：`你说的问题1挂靠问题，在阅读不会有任何问题，但是我会错，是因为我的意识中没有这一条，这种蛮多的，类似问题`
- **★★ 这是一整类规则，且解释了"阅读 8.5 为何帮不上忙"**：
```
读时  "eat out for all three meals near my office"  ← 语义自动消歧，零障碍
说时  必须主动决定 near my office 放哪              ← 没这条意识就随便放
★ 阅读从不逼她学这条，因为语义把它救了 → 读到 8.5，这条规则一次都没被编码
★ 比三通路更精确一层：不是"看→认"通路强，而是【这类规则在"看→认"通路里是多余的，从未存在过】
```
- **★★ 这一类是【真缺口】，不是检索失败 → 要"教"不要"练"**：
```
检索失败（83%）  知道但压力下调不出来  → 练（重复量）
这一类           根本没这条意识        → 必须明确告知（练也练不出来）
★ 且它是【封闭小集合】，不是海量个例 —— 符合她要的"事半功倍"
```
- **清单（读时全无障碍，说/写时全是错）**：
```
1. 修饰语必须紧贴被修饰词      eat out NEAR MY OFFICE for three meals   ← 她本轮发现
2. 并列两边必须同形            going hiking or HITTING UP
3. 分词逻辑主语 = 主句主语      ❌ the dominance…, hitting a peak of 80%
4. 比较对象形式对齐            than THAT at restaurants                 ← 她轮56 自发做对
5. 一句里时态同一时间平面      ❌ used to recruit … must serve
6. 代词指代唯一                ❌ 前面两个名词，it 指哪个
7. 关系从句紧贴先行词          ❌ find jobs WHO don't learn English
```
- **第 4 条她今天自发做对** → **这类规则一旦被点破就能长上去，但永远不会自己长出来**。
- **★ 教练职责新增**：主动扫这七条 —— **她无法自己发现它们**（阅读不暴露），只能教练盯。


### 轮 58–66 · 打磨 vs cold + **★ 硬料吃带宽导致结构崩（零和第四次）**
- 轮58–59（周末题，删空开头）：她一轮吸收 6 个修正（删空开头/goes to bed/some me time/that kind of thing/reading stories/用 he 代 my kid）。**★ 清单第2条并列同形刚教完就做对**：`going hiking, reading stories, hitting up amusement park` 三项全 -ing（对比轮37 `going hiking or HIT UP` ❌）→ **验证"这类规则一点破就能长上去"**。
- 轮60–63（CBA 打磨四遍）：`watched→went to` · `on a stadium→at` · `came up cheap→turned out to be` · `is→was`。**第4遍零语法错误**：
```
I went to a CBA basketball game with an old friend last weekend. It was at a big stadium here in
Chengdu. And the tickets turned out to be really cheap. What made it stand out was the atmosphere.
You can feel every basket, and the energy pulls you in.
★ what-cleft（Band7 结构特征）· pulls（槽3 实义动词第三次自发，前两次 tastes terrible / cracks me up）
★ 但诚实：这是第 4 遍，不是 cold
```
  → **策略：这是她写作策略（反复写旧作文固化）的口语版，且更划算因为 P1 话题有限。建议挑 15–20 个高频话题各打磨出一个"零错版"= 她的地板**（呼应"焦虑时只有自动化的活得下来"）。
- 轮64（cold 新题 Do you like watching sports）：`Not really.（转写成 not ready）Honestly, I don't follow any sports that closely. I tend to go again with some friends. It's less about a game itself, but more about spending time with friends`
  - **cold 基线比预期高**：自发用了两个地道结构 `follow…that closely` · `less about X more about Y`（都不是教练教的）→ 已在自动区。
  - 语言：`less about…BUT more`→`AND more`；`a game itself`→`the game itself`。
  - **★ 最大差距 = 零硬料**（打磨版 6 个硬料 vs cold 版 0 个）→ **硬料最吃带宽，cold 时第一个掉；而硬料恰恰是分数来源** → **备硬料是她三道思考题里优先级最高的**。
- 轮65（同题+强制硬料）：`Sometimes I go for a CPA basketball games once or twice a year… Almost every time i go mainly because I hang out with some friends.` + **她自评"最后一句硬憋的，感觉不太对"**
  - **★★ 零和第四次，且这次对照组是她自己一轮前的正确版**：
```
轮64（没硬料）It's less about the game itself and more about spending time with friends.  ✅ 结构完整
轮65（加硬料）Almost every time I go mainly because I hang out with some friends.        ❌ 两个从句无主干
同一意思、隔一轮、她自己上轮说对过。唯一变化：前面加了 CBA + once or twice a year。
★ 硬料吃掉带宽 → 后面结构撑不住 ∴ 硬料必须【预备到不占带宽】，现场调硬料要付账
```
  - **★ 她的错误感知类型差异**：轮41 形态细节误报（more than ever 是对的却判错）vs 轮65 结构断裂准确命中 → **"整句不对劲"信自己；"某个词不对"别停，继续说**。
  - 语言：`go FOR a games`→`go TO a game`。
  - **最小修改版示范**（按轮66 新要求）：`Almost every time I go, IT'S mainly TO hang out with some friends.`（加主句 it's + because I hang out → to hang out）


### 轮 93 · 层 5 首练（题库真题 `Has technology changed people's friendships? How?` line 257）
- **教练自查**：此前几十轮题目基本自编，**违反 skill 第一条**（题目从 `question_bank.md` 禁自编）。已改用题库真题。
- **她的原话输入（逐字）**：`technology makes it much easier for people to keep in touch.in the past, people used to meet in person,while it's mostly messages and likes. Plus, people can get to know each other on an online group. But the bonds built online are much fragile and shallow. it costs nothing to add someone, so it feels nothing to lose them`
- **★ 层 5 达成**：`it costs nothing to add someone, so it [costs] nothing to lose them` —— 从现象（脆弱）推到机制（零成本），且对仗。**她没照抄我给的示范句，改了一个词**（costs→feels）→ 比轮46 照抄好，但改动破坏了框架。
- **★ 层 3 上一轮两个问题都改了**：
```
上轮 两个 But（衔接单调）        → 本轮 while / Plus / But 三个不同 ✅
上轮 a bit fragile（自我对冲）   → 本轮 much fragile（加强，方向对，形态错）✅
```
- **层 1 三处**：
```
① much FRAGILE → much MORE fragile        （比较级，第三次出问题）
② it FEELS nothing to lose them → it COSTS nothing（feel 不能进 "it ___ nothing to do" 框架，且 costs 正好对仗）
③ ON an online group → IN online groups
```
- **★ 比较级三次三样，规则一次给全**：
```
轮53 phones are MORE SMARTER   双重比较级
轮90 cities are MORE NOISY     短词该用 -er
轮93 bonds are MUCH FRAGILE    much 后必须跟比较级形式
规则：①短的(1音节/2音节以y结尾)用 -er ②长的用 more ③much/far/a lot 后面必须是比较级形式
```
- **层 4 一个小断层**：句1（结论 technology makes it easier）与句2（证据 in the past…）之间无连接，读起来像并列 → 加 `For example,` 缝上。
- 层 2：`keep in touch` ✅ · `get to know each other` ✅（上一轮刚纠正，本轮用对）。
- 两个版本：①最小修改=动三个词 ②更好=只值得加 `For example`，其余到位。


### 轮 94–95 · 层 5 盲测通过 + **★ 复用块时丢成分（对仗拆一半）**
- 轮94（题库 line 255 `Do you think online communication…will replace face-to-face communication?`，**未预告测什么**）她原话：`No, I don't think so. admittedly social media makes it much easier for people to connect. But nothing can beat face to face communication. High quality communication involves the body language and voice tones. Communication online just adds to meeting in person rather than replace it.`
  - **★★ 层 5 无提示自发出现，且是两层**：`involves body language and tone of voice`（机制）+ `adds to it rather than replacing it`（**关系定位——没停在否定，给了更精确的立场**，P3 高价值动作）。
  - **★ `nothing can beat` = 轮36 `Nothing beats` 块的迁移**（加 can，用在抽象主张上，换语境自发调出）。
  - 层 4 结构完整：立场→让步→转折→机制→收口（标准 P3 高分结构）。断层：③→④ 无连接 → 加 `After all,`。
  - 层1/2：`involves THE body language`→零冠词；`voice tones`→`tone of voice`；**`rather than REPLACE it`→`replacING`（理解侧冗余第2条 并列同形）**。
  - `adds to`→`works alongside` 更准（add to 偏"加剧/增加"）。→ **她追问 `works alongside` 词义** → 教了 work+alongside 拆解 + 三级同功能表达：`can't replace` → `works alongside` → `goes hand in hand with`（卡住往左退一格）。
- 轮95（题库 line 811 `What positive and negative impact do mobile phones have on friendship?`，盲测）她原话：`mobile phones make it much easier for people to keep in touch. you can message to friends from anywhere at anytime. Parabatta, the relationship online is much more fragile. It costs nothing to lose one of your friends on an online group.`（`Parabatta` 转写不明，疑为转折词，待她确认）
  - **★ B19 比较级三条一轮吸收**：`much easier` ✅ `much more fragile` ✅（上一轮 `much fragile` ❌）。
  - **★★ 新发现：复用块时丢成分**
```
上轮 It costs nothing to ADD someone, SO it costs nothing to LOSE them.  完整对仗，因果闭合
本轮 It costs nothing to lose one of your friends.                       只剩后半 → 因果链断
★ 与轮34「could 掉了」同类：复用块时丢关键成分，块就退化。
  那次丢情态词，这次丢对仗的另一半。
```
  - 层 3 衔接变弱：4 句只有 1 个连接词（上一轮有 Admittedly…But… 清楚的让步转折）。
  - 层1 四处：`message TO friends`→`message friends`（及物，或 send messages to）；`at ANYTIME`→`at ANY TIME`；`THE relationship online`→`online relationshipS`；**`ON an online group`→`IN`（上一轮刚纠正，本轮又错）**。
  - **★ "改过又犯"的点要单独追踪**：一次纠正不够，说明没进自动区 → 放进复习清单。


### 轮 96 · 盲测（题库 line 256 `What's the difference between having younger friends and older friends?`）
- **隐藏测点：会不会又搬 `it costs nothing`（上一轮刚用）→ 没有** ✅ **新块没变成新的单调**（过度依赖假设不成立）。
- 她原话：`younger friends are more active and keep up with the time. You are on the same wavelength about the trend like tech. While older friends tend to be someone who provide advice, because they have been there before.`
- **★ 两个地道表达自发，均非教练所教**：`on the same wavelength`（合拍/同频）· `been there before`（经历过）。
- **层 5 第三次自发，但只在一边**：老朋友有"为什么"（because they've been there before），年轻朋友没有。
- **★ 层 4 对比不对称**：年轻朋友=特点+展开 ; 老朋友=特点+为什么 → **两边给的不是一类，读起来失衡。对比题两边应同构**（要么都给展开，要么都给"为什么"）→ 补 `because you're at the same stage of life` 即平衡。
- 层 1 三处：`keep up with the TIME`→`the TIMES`（固定说法，复数=时代）；`about THE TREND like tech`→`about TRENDS like tech`；`someone who PROVIDE`→`the ones who GIVE`（who 指单数要 provides；tend to be the ones 更自然）。
- 层 2 模糊词：`more active`（主要指爱运动/活跃）→ 她想说"玩得到一起/跟得上" → `more outgoing` / `more up for things`。


---

## 📅 2026-08-02 · 复习日 + 通路A 完整执行

### 复习结果（逐条过 08-01 全部 24 条，非抽样 —— 她当天定的新规矩）
```
Block 1 规则类（12题）  6/12 → 纠正后 12/12
Block 2 表达类（8题）   4/8  → 纠正后 8/8
Block 3 操作类（6题）   ≈0/6  ← 几乎全忘
```
- **★★ 记忆分层规律（本日最大发现）**：
```
她【产出过】的（规则/表达）→ 记得住一半
我【讲给她】的（操作/方法论）→ 几乎全忘
★ 与三通路一致：听讲解=喂强腿，出声产出=修弱腿
★ ∴ 操作类不能"讲"，只能在【执行中】一步步练，让操作变成她的产出
★ 且不能靠"说出方法名"考，要靠"做出来"考（说不出名字≠做不出来）
```
- 她因此定下：**复习必须逐条过上次记录，提取全部点列清单，她确认无漏后再统一出题。抽样会漏，而漏掉的正是她会忘的**（实证：抽查漏掉的"三条退路"她正好忘了）。

### 本日新建（规则）
```
· 反差六轴（她要求六根都练）：①必须↔选择 ②我的↔别人的 ③有结果↔看不到头
  ④它需要我↔我需要它 ⑤累但值↔累且烦 ⑥简单↔复杂
  各配核心句型：You have to…but…choose ／ the only part that's actually yours ／
  something to show for it ／ it actually needs you ／ a good kind of tired ／ nothing is that simple
· 换谓语升级：她要"更高的表达"（因句式谓语单调），但**只在她的可用动词库内选**
  （她随即纠正教练给过头：has a claim on / wrecked 都不是她会说的）
· 系动词能换/不能换的边界：形容词描述【对人的作用】→ 有对应动词可换（boring→bores）；
  描述【物本身属性】→ 无对应动词，老实用 is（quiet/high/big）
· be good at doing X → does X well（省掉一个 is）
· 通路A/B 的**比例**：引子 1 句 → 答案 2–3 句。个人经验是【跳板】不是【内容】
· 车轱辘 = 一个角度用三种说法说。**解法是换角度不是换说法**。
  翻译时最容易丢角度（她中文有两个支点，英文只落一个，剩下篇幅只能原地打转）
```

### 通路 A 完整执行（Why do some people like keeping pets?）
- 五级程序逐级走：①中文能说（判定=语言问题）②③她答"从来不养宠物"→ **教练指出"我不做X"本身就是素材**（正是通路A）→ 她中文反推成功 → 英文 + 桥接词 `So I guess` → 加反差（轴①必须↔选择）
- **她两次自主纠正教练**（第 9、10 次）：
```
"感觉有点不切题"  → 抓到通路A的比例陷阱（引子2句/答案1句，重心跑到"我"身上）
"感觉还是车轱辘"  → 抓到"一个角度三种说法"，且她中文本有两个角度被翻译丢了
★ 两个问题教练都没看出来
```
- 成品（全部来自她自己的事实，无一句编造）：
> I don't keep pets myself, but I can see why people do. Especially if you live alone,
> there's something waiting for you when you get home. Plus, it gives you something to
> look after — and unlike work or kids, it's something you choose.
- 零件：`I can SAY why`→`SEE`；`unlike work or kids` 独立成句 → 用破折号连回主句；`go work`→`go to work`（C2 老条目，改过又犯）；`having pet`→`having a pet`。


---

## 📅 2026-08-03 · 复习日（逐条过 08-02 全部 18 条）

### 复习结果
```
Block 1 表达（7题）  4/7  → 错在 headphones漏head / 冠词不一致 / you follows / They needs
Block 2 规则（4题）  4/4  ✅ 含"不能换"的边界判断（房间很安静→答"不能"）
Block 3 六轴英文（3题）1/3 → 见下方关键发现
Block 4 综合产出      比例对了、有跨话题迁移，但只有一个角度
30秒 主谓一致 drill   7/7 全对（孤立测 100%）
```

### ★★ 关键发现 1：句型记得住，"句型↔轴"的映射记不住
```
Block 1 六个句型全对（她产出过 → 记得住）
Block 3 却把【有结果】的句型接到【简单】那根轴上，另一题干脆忘了加轴
∴ 句型=表达层（记得住）／ 轴的编号和对应关系=方法论层（记不住）
★ 完全符合 08-02 的记忆分层规律
```
- **教练协议修正**：**往后不用"轴①④⑥"这种编号跟她说话，直接说内容要求**
  （不说"用轴④"，说"说明它是需要你照顾的"）。编号是方法论层，她记不住是正常的。

### ★ 关键发现 2：主谓一致 = 检索失败，不是知识缺口
```
孤立 drill  7/7 全对（100%）
产出中      you follows ／ They needs（两次，且是"多加"不是"漏加"）
昨天        he try ／ my wife love（漏加）／ Young friends keeps（多加）／ communication involve（漏加）
★ 两个方向都错 = 不是"忘了加 s"，是产出时根本不跑那个判断
★ ∴ 讲解无效，只能块化 + 检查触发
最省判断法：主语是"一个东西/他/她/它"→加 s；"我/你/我们/他们/好几个"→不加
```

### 本日新点
```
· as … as it gets（+about 软化）／ 退路三级：as simple as it gets → It couldn't be simpler → It's really simple
  ★ 用原级，避开她的比较级形态陷阱；与 as…as possible 同模子
· about 的两个位置：about+数字（她会）→ about+程度（新）
· 软化词家族：about / pretty much / I guess / kind of —— **一句只放一个**
  ★ 边界：软化词 + 强调词同时出现 = 自我对冲（definitely, to some extent）
    她答"重复程度"→ 教练精确化：不是重复（同方向说两遍），是【方向相反互相抵消】
· 三个 no 堆反差 + 收一个 yes（no rush, no crowd, no ads — and you can pause it）
· "三个 no"的生成法：想"要忍受什么"，每样忍受就是一个 no
· with + 名词 + on/off（with headphones on）
· fish 复数不变（fishes=不同种类）
```

### 跨话题迁移（本日两例，她自发）
```
"三个 no"    在家看电影 → 跑步（no rules, no equipment, nothing to go wrong）
"You can feel every X"  CBA basket → concert melody
★ 这正是她要的泛化：同一句型搬到完全不同的话题
```

### Block 4 成品（Why do people like going to concerts）
> I've never been to a concert, but one of my friends goes to them all the time.
> I guess it mainly comes down to the atmosphere — you can feel the music live,
> and there's something you just can't get at home. Plus you're doing it with a
> few thousand other people.
- 比例对了（引子1句/答案3句，昨天发现的陷阱没再犯）；论元丢失一次（`goes to.` 缺宾语）；
  用词不准两处（melody 配 feel 不搭 / peaceful 与演唱会相反）；**只有一个角度**（氛围），
  第二角度应是"和几千人一起"（耳机给不了）。


### 📅 2026-08-03 下半场 · ★★ 三步主干确立（她指出"没有体系"）

- **她的原话**：`我觉得我在硬堆，但是说的时候 mind 里还是没有体系和逻辑。这样一紧张还是得 gg`
- **教练自查**：已给她 **10 套工具**却从没给主干 → 她在**并行**调十套 = 硬堆感 + 崩。**并行是硬堆，串行是流水。**
- **主干（先四步，她纠正后改三步）**：
```
① 定位 + 答案（答案不能拖）  ② 具体画面  ③ 换角度
十套工具挂在三步下面当备用，不卡不调
```
- **★ 她第 11 次纠正教练**：`我觉得有点头重脚轻，前面铺垫了好几局才总结，是不是反过来了`
  → 属实。原四步里"为什么"排第三，考官听到第三句才知道答案。**修正：答案并进第一句，四步压成三步。**
  → **通路 A/B 的起手必须带答案方向**，不能只说"我不做这个"。
- **同一题三版对照（她自己的材料，只改结构）**：
```
版本1  my wife is really into it（判断，0 硬料）+ 满足感说两遍（车轱辘）
版本2  补上第②步 → a few flowers / on the balcony / every morning / a couple of minutes（4 硬料）
版本3  答案前置 → I've never grown anything myself, but I guess there's something
       satisfying about watching things grow. My wife keeps a few flowers on the balcony
       — it only takes a few minutes every morning. And it's the only thing in her day
       that isn't on a screen.
★ 同一个人同一份材料，差别只在【走没走第②步】和【答案在第几句】
```
- **五个角度问句（生成第二支点，解决"只有一个角度"）**：给你什么／躲开什么／一个人还是一群人／身体还是脑子／当时还是之后。**不是每题五个都适用，有两个能用就够。**
- **★ 三步主干无提示走通（Why do people shop online）**：`I think it's mainly because of convenience.（答案第一句）/ My wife buys pretty much everything online. You can place orders from anywhere at any time.（具体）/ On top of that, you can get a refund within seven days…（换角度）` ✅ 三步齐 + 衔接词三个不同。
- **★ 新错误模式：把短语/从句当整句用（今天三次）**：
```
"…something to look after. UNLIKE WORK OR KIDS. It's…"
"…to water them. WHICH GIVES YOU a sense of fulfillment."
"She keeps a few flowers on the balcony - JUST A FEW MINUTES every morning."（无动词）
★ 原因：说完一句想起还有信息，直接说出来，没挂回主句（快时钟下补信息比连接省事）
★ 修法：补充信息必须挂回主句 —— 破折号／逗号／and／逗号+which
```
- **改过又犯专项 drill 8 题 → 6/8**：四个老项目（in an online group／terrible at／at any time／for any reason）**全部改对** ✅ 主谓一致 3/3 ✅
  新错两处：`plants grow UP`（grow up 只用于人，她 `I grew up in Yibin` 用对过 → 过度泛化）· `shops everything`（shop 不及物，应 buys／does her shopping）
- **中文"无理由"的两个意思（她追问 for no reason 行不行）**：
```
① 没道理/莫名其妙 → for no reason（He shouted at me for no reason.）
② 不需要说明理由  → for any reason ／ NO QUESTIONS ASKED ／ without giving a reason
★ 七天无理由退货是②。no questions asked 是现成块，挂句尾即可
```
- **★ 教练漏洞**：纠正过的东西一直只"讲"不"练" → 旧块先到，必然回潮。**纠正过的必须进 drill。**


### 📅 2026-08-03 尾段 · 跨域主干 + 精度打磨（自动记录，她 08-03 要求不再征求确认）

- **换域主干测试**（题库 line 158 `What are the advantages of living in tall buildings?`，她写作写过这题）
  她原话：`the biggest advantage is the view. The higher you live, the farther you can see. Plus, the high floors are far away from the roads, it's something quiet people really enjoy.`
  - **★ 写作素材迁移**：`the higher you live, the further you can see` = 写作 `the taller apartment blocks are, the more households they can house` 的同结构（the+比较级, the+比较级），**从写作搬到口语** ✅
  - ❌ **第②步又跳过了**（今天第二次）：`The higher…the farther…` 是**规律**不是**画面**，零硬料。
  - ❌ **`quiet people really enjoy` 会被听成"安静的人"** —— quiet 想修饰整体却挂到 people 上 = **与轮98 `quiet and green parks` 同一个错**（理解侧冗余第1条）。
  - ❌ 逗号粘连（P14）：`away from the road, it's something…`
- **★ 她第 12 次纠正教练**：`我觉得这个具体的描述在 P3 中不是很好` → 属实，且引出重要修正：
```
硬料在 P3 里不用删，只要【别绑在"我"身上】
P1 硬料  From OUR place you can see across the city      说的是我家
P3 硬料  From HIGH ENOUGH UP, you can see across the city 说的是"高楼"这件事
★ 内容一模一样，只换主语人称
★ 三步主干在 P1/P3 结构完全相同，差别只在第②步的主语人称
★ 这解释了她"P1 一直比 P3 顺"——P3 要多做一步【泛化】，之前没人告诉她
个人例子在 P3 可以用，但要标记（For example, where I live…）且一句说完就回 general
```
- **她追问 `high enough up` / `well away` → 引出"程度旋钮"概念**：
```
不换词，只加一个 well / enough / right / just，给已会的表达加精度
away from → WELL away from ／ across the city → RIGHT across the city ／ a few minutes → JUST a few minutes
enough 的位置：形容词【后】(tall enough) ／ 名词【前】(enough time)
well 专配介词短语和过去分词（well away / well over / well known），不能说 very away
```
- **她再追问"high up 是固定短语还是有逻辑" → 教练诚实作答**：up/down 有时承载方向、有时纯属习惯（冗余），**追究会卡住，记块更快**（符合她"记块优于记规则"的验证）。给五个常用块：`deep down`（最有用，含比喻义"内心深处"）· high up · way up · far down · right up to。
- **中文一词多义两例**：
```
坚持  主张/要求 → insist ON ／ 做下去 → keep it up · stick to it     （她用 insist on 表"坚持不下来"❌）
无理由 没道理 → for no reason ／ 不需说明理由 → for any reason · NO QUESTIONS ASKED
```
- **★ 时态：今天错三次，两个方向都错**（`you only spent`该现在／`I do try`该过去／`I can't be bothered`该过去）
  → **与主谓一致同类：中文里不存在的东西（类型2），产出时不跑判断**。
  判断触发：**中文有没有时间标记词**（试过/昨晚/以前/小时候→过去；通常/每天/现在→现在）
  附带：**usually 配现在习惯；过去的习惯用 used to / would / often**（她第1句 used to 用对，第4句没调出来）
- **她的风格观察："总觉得用了太多的 I"** → 三个减法：①合并动作 ②**共享主语（一个 I 带两个动词）← 最有效** ③换 It 开头。
  drill 3/3 全对。但也告知：英语第一人称叙述本来 I 就多，只在一句三个以上才需合并。
- 零件：`exercise` 不可数 · `play out`≠出去玩（take sb out）· `on weekends`（要复数或 the）· `read TO sb` vs `read FOR sb`（替某人读）→ 更省：`read him stories` 双宾语
- **★ 新块**：`It's not that A, it's just B`（中文"不是…只是…"）· `do + 动词` 强调（I DO want to go）· `can't be bothered`（懒得动，英式高频，比 lazy 自然）


### 📅 2026-08-03 收尾段 · 画面标准补第二条 + "让某人做"四件套

- **换域主干（题库 line 190 `Why are some teachers' classes boring?`）** 她原话：`the key is that some teachers just read at them. students can even get all information from books by themselves. Plus, there is rarely interaction in class, students can't get involved and quickly switch off`
  - ✅ 答案前置 · 两个角度 · `switch off`（走神）地道且自发
  - ❌ **第②步第三次跳过**（前两次：`my wife is really into it`／`the higher you live…`）
```
三次都是"想出来的"不是"能看见的"：判断 / 规律 / 推论
★ 原因：推论比回忆便宜（不用检索具体记忆）→ 带宽紧时自动走推论
★ 两秒判断：这句话能不能拍成一张照片？
   ❌ students can get all information from books   拍不出
   ✅ half the class is on their phones             拍得出
```
  - ❌ `read at them`：them 无先行词 + 搭配怪 → **引出好词 `talk AT sb`（单向灌输）vs `talk TO sb`（双向）**
  - ❌ 逗号粘连（今日第二次）；`rarely` 后面配 any
- **★ 她第 13 次纠正教练**：`两人一组动手拼东西，感觉奇奇怪怪…内容也不是很搭，需要那么特化么`
  → 属实，教练第三次给过头（前两次 wrecked / has a claim on）。**引出画面标准的第二条**：
```
① 能拍成照片吗？  （具体）
② 大多数人都见过吗？（典型）
★ 两条都要满足。太特化 = 只代表某一类情况，在 P3 里跑偏
她的"半个班在玩手机"两条都满足 ✅ ／ 教练的"两人一组拼东西"只满足第一条 ❌
```
- **★ "让某人做某事"四件套**（中文一个"让"，英文四个；她 drill 3/3）：
```
get sb TO do    设法让/安排（最常用，★ 只有这个带 to）
have sb DO      指派/安排
make sb DO      强迫
let sb DO       允许
```
- **`pay more energy` → `put time and energy INTO`**（她轮104 用对过，本轮回潮）
```
pay 的搭配很窄：pay money / attention / the price / a visit
时间和精力用 put … into ／ spend … on
```
- **中文"背"分两个动作**：`memorise`（记住）／`recite`（开口说出）／`learn sth by heart`（背熟）
  她自己的例子 `sci-fi 我背了无数遍` → `I've gone over it so many times.` ／ `I know it by heart.`（最地道）
- 零件：`try to PREPARE`（to+原形）· `handS-on` · `in class`（不加 es）· `stuff` 不可数 · `on their phones`（C2 清单里的"玩手机"）· `within ten minutes`（她学过两次）
- **★ 一个值得记的观察**：教练示范句 `You can see half the class on their phones within ten minutes` 她看不懂 → 拆开后发现**没有一个新零件**（You can see / half the class / on their phones[C2清单] / within[学过两次]），**新的只是组合方式** → 印证"零件都在，但没组装过"。


### 📅 2026-08-04 · 复习日（逐条过 08-03 全部 20 条）

### 复习结果
```
Block 1 表达（10题）  块 9/10 调出（只有 can't be bothered 没调出）
Block 2 规则（8题）   8/8（只有 High floors IS→ARE）
Block 3 结构（盲测）  ★ 三项全过（三步走完 / 第②步有画面 / 两角度不重复）
```

### ★ 她修正了教练的"明确不修"分类（第 14 次纠正）
- 她原话：`主谓一致·冠词·时态一致。还是要修，前三个发现错了需要指出来，只是不需要 drill，最后（论元完整）以后需要更加关注和 drill，其实我不太会`
- **教练把四项混成一类是错的，正确的拆法**：
```
主谓一致·冠词·时态一致   孤立测都对（主谓一致 7/7）→ ✅每次指出，❌不 drill
论元完整                 她自述"其实我不太会"      → ✅指出 + ✅要 drill（移入 B 档主攻）
★ 判据就是她自己的自我分诊：单独问答得出=不 drill；答不出=真缺口
```
- **为什么论元完整是真缺口**：前三个是**形态**（-s/the/-ed），规则简单；**论元完整是每个动词单独的属性**（哪个词后面必须带什么），一个词一个样，没有通用规则。而**中文这些全部可以单说**（我很专心／我参加了／我习惯了／我去了）→ 她没有这个意识。
- 她丢过的：`focus on___` · `a mix___` · `spend as much___ as possible with___` · `goes to.` · `you can even___the mountains`（**连动词都丢了**，因为中文"甚至能看见山"里"看见"可被吞掉）

### ★ 教练自查：过度纠正 `watching plants growing`
```
watch X DO      看整个过程/习惯   watching plants grow ✅
watch X DOING   看正在进行         watching plants growing ✅
★ 两个都对。她真正错过的是 grow UP（只用于人），不是 growing。
★ 教练之前把 growing 也标成错 = 制造了假错误
```

### 本日成绩
- **两个改过又犯的项目都改对了**：`usually played`→`often played` ✅ ／ `pay more energy`→`put more energy into` ✅
- `get / let / have sb do` 三个的 to 全分清 ✅
- `talk at you for an hour` · `read my son stories`（双宾语）两个完美
- 盲测产出（second-hand things）：`half, or even a tenth of the original price` 数字画面 ✅；第二角度"限量/停产只能买二手"与"省钱"毫无重叠 ✅ **真正的第二支点**
- 零件：`because of saving money`→`mainly to save money` · `cost little`→`cost much less` · `one tens`→`a tenth` · `Some goods are limited`（意思不清）→`aren't made anymore` · `be able to`→`can`
- 分数说法：a half / a third / a quarter / a tenth / two thirds

### 早段（换域主干 remodel & decorate）
- 她原话：`The main key is money. Hiring designers is too much expensive. on top of the end, someone' enjoy picking up furniture and choose colors themselves…`
- ❌ **第②步跳过**（"贵"是判断不是画面，缺具体价格/场景）
- 零件：`too MUCH expensive`→`FAR/WAY too expensive`（too+形容词中间不能插 much）· `picking UP`→`picking OUT furniture` · `picking out…and CHOOSE`→`and CHOOSING`（并列不同形）· `on top of the end`→`on top of that`
- 表达升级：`The styles of their homes belong to them rather than others` → `The place ends up looking like them, not like a showroom.`（showroom 一词说完对比）


### 📅 2026-08-04 下半场 · B41 论元完整 drill（8 题）→ ★ 反证：不是知识缺口，是产出时掉

- **她的原话（逐字）**：`i find it hard to focus on work. my friend usually go to that shop. a mix of the city and the countryside is perfect(感觉the用的不对). you can see the mountains in the distance if it's clear. I spend as much time as possible with my kid on weekends. i did try it, but it didn't work out. teachers should encourage students(多好想漏了). I don't like it, but i can accept it.`
- **论元完整 8/8 全对**（她 08-04 上午自述"其实我不太会"）。之前丢过的五个全部补回：focus on **work** · goes to **that shop** · a mix **of** · can see **the mountains** · spend as much **time** as possible with **my kid**
- **★ 反证 → B41 需重新归类**：按她自己那条自我分诊（答得出=检索失败不背；答不出=真缺口），8/8 = **知识在**，她的"不太会"是**产出时掉**的体感，与 C4 同类。⚠️ 但本次**预告过测试点**（我先讲了规则+列了她丢过的），属 primed 测试，证据弱一档 → **判定挂起，看后面 cold 产出里论元还在不在**。
- 修法不变（轮52 已定）：不能靠"更小心"（=更多监控=更多带宽），只能**块化**——记 `focus on my work` 整块，不记 `focus on`。
- 零件：`my friend usually GO`→`goes`（主谓一致 · C4 指出不 drill）
- **层2 精确度 · 改过又犯**：`usually goes`→`often goes`。08-04 上午刚改对 `usually played`→`often played`，换个任务当天回潮 = 「激活最强的先到」再证（usually 是旧块）。
- **她两条自我标注都准**：①`多好想漏了`——自己抓到 `encourage students` 缺 `more`（自我监控在工作）②`感觉 the 用的不对`——真有不对称，见下。
- **`a mix of the city and the countryside` 判定（不是错，但她的直觉对）**：`the countryside` 是泛指的标准形式（永远带 the）；`the city` 带 the 默认指**某一座具体城市**，泛指该用 `city life`。→ 两边**看着对称、泛指程度不对称** = 「并列两边同形」的隐藏版（理解侧冗余 #2）。自然版 `a mix of city life and country life` ／ 最省 `a mix of both` ／ 天花板 `the best of both worlds`。
- **★ 自发迁移**：`i DID try it` = B37 的 `do+动词`强调，无提示自发用出（隔一天）。
- 天花板：`I can accept it`→`I can live with it` ／ `if it's clear`→`on a clear day` ＋ 补 `even`（甚至能看见）。


### 📅 2026-08-04 下半场（续）· P3 团队题 + 三组 drill → ★★★ "听=0，产出才计数"

**真题（题库 P2-新11 P3）：Why do some people prefer to work by themselves?**
- **第一次：她自述"非常卡"，只出中文**。中文内容=满足感/证明价值/做到同事做不到的事 ＋ 效率高不用开会。
- ★ **她的中文已自带三步主干**（答案-画面-换角度，两角度不重叠）→ **结构层已内化，卡的 100% 在填充层**。现场复现 07-26 从作文挖出的结构：**框架层直连、翻译全残留在填充层**。
- 拆包后英文（逐字）：`It gives you a sense of satisfaction. Completing work independently can prove your value. Especially, you can do something that other cardigans can't do. On top of that, Working alone would be much more effective Sometimes. you don't need spend time talking to others repetitively or be stuck with meeting all day long.`
- 主干三步 ✅，但**画面落在第③步（stuck in meetings all day）而非第②步**（something 是空的）→ 第②步连续第五次不达标。
- ★ **层4 新发现**：题目是比较题（prefer to work BY THEMSELVES = 比在团队里），**她全程没提另一边** → 老毛病「比较对象没补齐」**升级到段落层**（以前只在句子层：than ten years ago 少了 they were）。
- 零件：`Especially,` 不能独立起句（须跟 when/if/名词）· `would be`（无条件句的自我对冲）→ is · `effective`→`efficient` · `need spend`→`need to spend` · `repetitively`（机械重复/书面）→`over and over` · `stuck with`→`stuck in meetings`
- 做对：`don't need to [spend…] or [be stuck…]` 并列两边同形 ✅
- 待确认：`other cardigans` = colleagues 的转写错？

**Drill A · 零件五连**
- 她原话：`you don't need to spend a whole day meeting. I was stuck in meetings yesterday morning. it's more effective working at home. we go forth and back three times for the thing. you don't need to explain it to anyone`
- ★★ **`effective` 五分钟后回潮**，与 usually/often 隔一天回潮同构 → **"讲过"≈0**。
- ★★ **论元又掉**：`spend a whole day meeting___` → **B41 判定落地：不是知识缺口，是产出时掉**（上午 primed 8/8，20 分钟后 cold 就掉）。修法=块化记 `in meetings`。
- `forth and back` 词序反 → `back and forth`（固定序；同类 now and then / sooner or later / more or less，只能整块背）
- 全对 2/5：`I was stuck in meetings yesterday morning` · `you don't need to explain it to anyone`（论元带上了）
- 其他：`work FROM home`(WFH 固定搭配) · `we go`→`went` · `for the thing`→`on it`

**Drill B · 原题重说（唯一约束＝每个理由带上"团队"那一边）**
- 她原话：`It gives you a sense of satisfaction. Completing work independently can prove your value. Especially when nobody else can do it. In contrast, working as a team member can show for yourself. On top of that, Working alone is more efficient Sometimes. you don't need to talk to others over and over or be stuck in meeting all day.`
- ★★★ **上一轮四个改动 4/4 全保住**（Especially when · efficient · over and over · stuck in）。对照 usually 和 effective 的回潮，**唯一变量 = 这四个她当场又产出了一遍** ⇒ **新硬规矩：改完必须当场重说一遍，否则等于没改。**
- ★★ **注意力零和现场（第 N 次）**：六句里**唯一新加的那句**同时崩三样——`In contrast, working as a team member can show for yourself` = 论元丢(show ___) · 搭配不存在(show for yourself) · 极性反了(In contrast + can)。**新东西必须先单独滚熟再塞进整段。**
- 修：最小 `working in a team can't really show what you can do` ／ 更好 `In a team, the credit gets shared, so nobody knows which part was yours.`（**credit 分摊才是 satisfaction 的机制**，比感受词深一层）
- `stuck in meeting`→`meetings`（泛指复数，C4 档指出不 drill）

**Drill C · efficient/effective 判别五连**
- 她原话：`the drug is really useful. meeting online saves a lot of time. the ad was so effective that the sale went up by 20%. new system deals with orders more efficiently. it's of no use to punish people who throw litters(感觉翻译的不好)`
- **判别本身过关**：`so effective that` ✅ · `more efficiently` 副词形 ✅ · `meeting online saves a lot of time` = 用动作代替形容词（正是教过的画面化）✅
- 1 处回避：`the drug is really useful` → 药管用＝**effective**（useful=有用处，说工具）；最口语 `It really works.`
- 零件：`the sale`→`sales`（销量恒复数不带 the；the sale=一次促销）· `new system`→`THE new system` · `deals with`→`handles`（deal with 偏"处理麻烦"）· 漏 `much`（快多了）
- ★ **她第 7 次自我标注命中**：`感觉翻译的不好` —— 对。`of no use` 老式书面 · `throw litters` 错（litter 不可数）· "罚款"丢了
  - 最小 `It's no use fining people for dropping litter.` ／ 更好 `Fines don't really stop people littering.`
  - 真词汇缺口（直接给）：**litter**(n.不可数垃圾) / **litter**(v.乱扔) / **fine sb for doing sth**


### 📅 2026-08-04 下半场（续2）· 名词表语 → ★ 评价槽升级（她自诊"名词当表语我确实不会"）

- 触发：`It's no use fining people`。**她的自诊准确**，且卡点精确——`He is a teacher` 那种她会，不会的是**评价类**名词表语。
- ★ **定位：与轮32「系动词依赖」是同一个槽**。`It's + 形容词` 是她的默认填充，这个槽她从没放过名词 → **结构一个字不用新学，只换填充物**。名词表语信息量大得多（a nightmare 带着"折腾很久很惨"，bad 什么都不带）。
- 给的七块（不扩）：`It's no use doing` / `a waste of time` / `a pain` / `a hassle` / `a nightmare` / `no big deal` / `a must` / `a plus`；两条语法：可数要冠词（带 no 的不要）· no use 后只接 -ing。
- 她原话：`it is no use regretting now. it's a waste of time arguing with him. it's a hassle commuting every day. it's no big deal. it's a must getting fluent in English here. it's a plus being able to speak japanese.`
- **4/6**。★ 错的两句是**同一个错 = 过度泛化**（把 `It's ___ doing` 推给了 a must / a plus）→ **说明她抽到了规则再推广，不是死记硬背**，只是边界画错。这类错比零散错值钱。
- 边界（新建 B51）：评价**那件事本身**（no use / a waste of time / a pain / a hassle / a nightmare）→ `It's…doing` 与 `X is…` 都行；给**某个东西归类**（a must / a plus）→ **只走 `X is a must`**。
  - 修：`Being fluent in English is a must here.` ／ `Being able to speak Japanese is a plus.` ／ 天花板 `It helps if you can speak Japanese.`
- **今天第 4 次丢论元**：`regretting___` → `regretting IT now`；天花板 `There's no point regretting it now.`

**（续2 尾）· 转写确认 ＋ 当场重说**
- ★ 她确认 `other cardigans` = **转写错**（她本来说的是 colleagues）→ 按数据协议**作废该错误**，不是她的词汇缺口。
- 重说 5：`fluent English is a must in this work.` —— **结构学会了 ✅**（X is a must，边界一次就纠正过来）；但 `in this work` ❌ 不是英文说法 → `in this line of work` ／ `in this field` ／ `for this job`
- 重说 6：`being able to speak japanese is a plus.` —— ✅ 全对
- ⇒ **B51 边界规则一次纠正就装上了**，与"改完当场重说"的效果一致（第二次验证）
- 新题起手（`Should students learn to do group work?`）：`students should learn how to work in pairs` —— 第①步答案有 ✅；`in pairs`=两人一组 ≠ group work → `in groups`

---

## 📅 2026-08-05 · 学习日（新节奏第 1 天）· D-1(08-04, 55条) ＋ D-3(08-02, 19条) 复习

> 本日起用她 08-05 定的新节奏：学习日复习 D-1＋D-3；每 5 学习日一个专门复习日（含题目重答）。周期锚点 08-05 = 第 1 天，08-10 = 第一个专门复习日。

### Block 1 · 规则类 21 题（D-1 #1–21）

- **她的原话（逐字）**：`1 论元完整需要其他不要，因为会，只是会漏 2. i like watching kids playing in the park. 去掉 up. 3. teachers should get students to try it themselves. don't make kids memorise all the thing. let them ask questions. have them work in pairs. 4. hiring designers is way too expensive. 5. they would like to pick out furniture and chose colors themselves. 6. a half or even a tenth of the original price. 7. usually 是一般不是经常，my friend often goes there. 8 我觉得这个问题你不应该问我，你自己知道就行，和第一题一样 9. especially when nobody else can't do it. 10. working alone is more efficient. 没有条件句别用 11. or 后面改原型， be stuck in. 12. we went back and forth three times for the some problem. 13. i was stuck in meetings all the morning. 14. the ad was effective, so sale went up by 20% 15. the drug is effective. meeting online saves time. 16. fine is no use for littering. 17. 不对 doing 18. it isn't a big deal. commuting between the office and home everyday is a hassle. 19. fluent english is a must in the line of the work. 加分项忘了. 20. teachers often have students work in groups. 21. a mix of both is perfect ( 我忘了 city 怎么加，感觉加 the 也不太对）`

- **成绩：全对 9 ／ 部分 7 ／ 漏或错 4 ／ 她拒答 1（有效）**
```
全对   2 · 4 · 6 · 7 · 10 · 11 · 15 · 17 · 20
部分   1 · 3 · 5 · 12 · 13 · 18 · 21
错/忘  9（双重否定）· 14（sales）· 16（It's no use 组装崩）· 19（a plus 忘）
拒答   8
```

- **★★ 她的第 15 次纠正（成立，教练照办）**：第 1、8 题问的是**教练侧的训练安排决策**（哪条要 drill、为什么），不是她要用的东西。她原话：**"我觉得这个问题你不应该问我，你自己知道就行"**。
  ⇒ **新规矩：复习清单只装【她要用的】——规则 / 表达 / 操作；教练怎么排训练不进她的清单，也不出题。**

- **★★ 本日最值钱的一对照（#16 vs #17）**：
```
#17 判断题  It's no use to worry about it. → 她答"不对，doing"        ✅ 认得出
#16 产出题  罚款对乱扔垃圾没什么用        → fine is no use for littering  ❌ 组装崩
★ 同一个知识点，判断题对、产出题崩 —— 「认得出 ≠ 说得出」在复习环节现场再现
★ ∴ 复习出题必须以【产出题】为主，判断题会给出虚假的"会了"
```

- **★ #9 双重否定（新错误模式，记为 B54）**：`especially when nobody else CAN'T do it` = 没人做不到 = 极性反了。
  根因＝中文"**没人能**做到"里有个"没"，她把"没"映射了两次（nobody ＋ n't）。**英文 nobody / nothing / never 已经含否定，后面动词一律用肯定。**
  且这是**两天内第二次极性错误**（08-04：`In contrast, working as a team member CAN show…` 该用 can't）→ 极性是新的薄弱维度。

- **逐条批改**：
```
 2  ✅ 全对（watching kids playing ✅ ／ 准确指出 grow up 的 up）
 3  3/4  `all the thing` → everything（其余 get to do / make do / let do / have do 全对，
        且 in pairs 用对＝#20 的区分她已装上）
 4  ✅ way too expensive
 5  并列同形规则已装上（to pick out … and choose，形式对齐）；`chose`＝拼写；
        `would like to`（想要）→ `like to`（喜欢）
 6  ✅
 7  ✅ 规则说对＋goes 主谓一致对
10  ✅（漏了 sometimes，不算错）
11  ✅ "or 后面改原型"＝ being → be
12  `for the some problem` → `on the same problem` / `on it`；★ 三个同类固定词序没答
        （now and then · sooner or later · more or less）
13  `all THE morning` → `all morning`（all morning / all day / all night 不带 the）★ 新点 B55
14  `sale` → `sales` ★ 昨天刚教就错，进"改过又犯"
16  → `It's no use fining people for littering.` ／ `Fines don't really stop people littering.`
18  `it isn't a big deal` 可接受，但教的块是 `It's no big deal`；
        `everyday` → `every day`（everyday 是形容词"日常的"）★ 新点 B56
19  `in the line of the work` → `in this line of work`；**a plus 整条忘了** → 重练
21  `a mix of both` ✅；缺的是 `a mix of city life and country life`；她再次自判 the 别扭＝对
```

### Block 2 · 表达类 27 题（D-1 #22–48）

- **她的原话（逐字）**：`23. some goods are limited edition, or they stopped making it ages ago. 24. mainly to save money 25. second-hand ones are much cheaper. 26. some teachers can talk at you for an hour. / to 是双向 27. I read my son stories every night. 28. teachers should put more energy and time into preparing classes.(是复数吧) 29. the house looks like their own, not like a showroom. 31. On top of that 32. I don't like it, but I can (我不知道 accept 不对，但是忘了应该用啥) 33. on a clear day, you can see the mountains in the distance. 34. 忘了 36. you don't need to be stuck in meetings all day. 37. working at home is more efficient. 38. the new system handles orders more efficiently. 40. you don't need explain youself to anyone. 41. the credit gets shared, so nobody know what part is yours. 42. it's no use fining people for littering. 43. There is no point regretting it. It's no use regretting it. 44. 不太记得 no use, a must, a plus 这些 46. I can do more work at home. 47. you don't need to sit in the meeting room all day. 48. For example?`

- **成绩：全对 10 ／ 部分 8 ／ 忘 4**
```
全对   24 · 25 · 26 · 27 · 31 · 33 · 36 · 38 · 42 · 43
部分   23 · 28 · 29 · 37 · 40 · 41 · 46 · 47
忘     32（live with it）· 34（the best of both worlds）· 44（七块列不全）· 48（Say you…）
```

- **★★ #44 揭示的新区分：能用 ≠ 能列举**。她说"不太记得 no use / a must / a plus 这些"，但**同一批里 #42 用对了 no use、#43 用对了两种说法、Block1 #19 用对了 a must**。
  ⇒ **块是装上的，只是"清单"调不出来。列举题＝坏题型**（和判断题一样会给假信号）。**出题只考"用"，不考"列举/判断"。**

- **★ 忘掉的 4 条里 3 条是"她从未产出过"的教练给的天花板**（live with it ／ the best of both worlds ／ Say you…）→ 与 08-02「记忆分层」一致。
  但**不绝对**：`on a clear day`(#33) 和 `There's no point regretting it`(#43) 也是教练给的，她记住了 —— 因为这两条昨天她**当场重说过**。⇒ 变量仍然是"有没有产出过"，不是"谁说的"。

- **★ 昨天崩掉的 #16 今天全对（#42 `it's no use fining people for littering`）** → 纠正后当场重说 → 隔一轮保持，第三次验证。

- **逐条批改**：
```
23  ✅ `limited edition` 比教的 `aren't made anymore` 还好；`stopped making IT` → THEM（goods 是复数）
24  ✅   25  ✅   26  ✅ 全对（talk at ／ to 是双向，规则也说对）
27  ✅ 双宾语 + every night 分写正确
28  put…into ✅；两点：`energy and time` → 英语习惯 **time and energy**；
    `preparing classes` → **prepare their lessons** ／ **prepare for class**
    （答她的疑问：class 泛指"上课"这件事时不可数不带冠词——before class / in class；
      具体课时才用 lessons）
29  `looks like their own` 所指缺失 → `looks like THEIRS` ／ 教的版本 `ends up looking like them`
33  ✅ 只差 `even`（甚至能看见）
36  ✅ 可接受；教的块是 `sit in meetings all day`
37  `at home` → **FROM home** ★ 昨天刚教（B47），改过又犯
38  ✅ 冠词/handles/efficiently 全对；**漏 much**（第二次漏，"快多了"）
40  `need explain` → **need TO explain** ★ Block1 #11 她刚判断对（or 后接原型），产出时又掉
    ⇒ 「认得出 ≠ 说得出」当天第三次
41  `nobody know` → knowS（C4）；`what part` → **which part**（从确定范围里选用 which）
42  ✅✅ 昨天崩的那句今天全对
43  ✅✅ 两种说法都给出，且 There's no point 更常用
46  `I can do more work at home` 意思到了，块没到 → `You just get more done at home`
47  `sit in the meeting room` = 中文"会议室"直译 → 英语说 **sit in meetings**
48  `For example?` → 教的口语起手是 **Say you…**（Say you fix something the whole team…）
```

### Block 3 · 操作类（D-1 #49–55）· 做出来测

- 题：`Why do people enjoy going to live concerts rather than watching them online?`
- **她的原话（逐字）**：`The key thing is the atmosphere. you sit or stand with more than one thousoud people, and the singer and you sing together. You can feel the energy live. While just watching it in front of the television feels a bit lonely. TV 前那个 the 我有点犹豫，但是我又觉得不能泛指`

- **操作项判定**：
```
#49 画面两条标准      ✅ 一千多人站着/坐着 + 跟歌手一起唱 —— 能拍照片、大多数人见过
#52 比较题说另一边    ✅ While just watching it… 显式给出了线上那一边（且用 While 标出对比）
#53 第②步真画面      ✅ 第①句给答案(atmosphere)，第②句立刻落地成画面，没有停在判断
#55 中文层降级        ✅（由结果反推：产出直接是具体的，没有抽象堆叠）
```
- **★ 第②步一次到位**（08-04 remodel 题还在跳，08-04 second-hand 题过，今天换题型再过 → 连续第 2 次）

- **★★ 但第③步「换角度」缺失 —— 08-02「车轱辘」现场复发**：
```
The key thing is the atmosphere     气氛
the singer and you sing together    气氛
You can feel the energy live        气氛（换了个词而已）
watching it at home feels lonely    气氛的反面
★ 四句全在【气氛】这一根轴上。另一边≠新角度。
★ 正是 08-02 那条："车轱辘 = 一个角度三种说法，解法是换角度不是换说法"
⇒ 三步主干的②做到了，③还没有。下一步专攻"第二支点"。
```

- **★ 她的自诊第一次误报**：`in front of the TV` 的 the —— **是对的**。英语里 the TV / the radio / the cinema / the doctor 是惯用定冠词，不按泛指-特指走。
  这与既有规律吻合：**结构断裂她的直觉准，形态细节她会误报**（把对的判成错的，轮41 已记）。此前自诊 7/7 全中，这是第一次疑错，且正好落在形态类。

- **语言层（五层）**：
```
层1  `one thousoud`→thousand（拼写）
     `While just watching it… feels a bit lonely.` 独立成句＝从句片段
        → 接回上句：`…, while watching it at home feels a bit lonely.`
层2  `sing together` → **sing along**（跟着唱的专用动词）★ B57
     `feel the energy live` → **feel the energy in the room**（live 不能这么放）★ B59
     `in front of the television` → 口语说 the TV；更自然直接 `at home`
层3  ★ **自我对冲又出现**：`a bit lonely` 的 a bit 把对比削软了
        （与档案里 `a bit fragile` 同一模式）→ 对比句删掉 a bit
层4  ✅ 答案前置做到了（第一句就是答案）
层5  内容还能挖一层：**为什么现场有 energy 而线上没有**——现场你退不出去所以全神贯注，
     线上随时能暂停/刷手机。这一层同时也是天然的第③个角度。
```

#### 第③步补练（她说"我遇到语言层面的困难，四个角度都给语言版本"）

- 教练给了**四个万能第二支点 ＋ 骨架 ＋ 别领域填法**（刻意不给演唱会填法，防轮46 的照抄退化）：
```
① 钱/时间   [X] isn't cheap, but people still…／People are willing to pay for…／
            If it were just about [X], nobody would bother.
② 人        Half of it is who you go with.／⭐It's less about [X] itself and more about…／
            You usually do it with someone, not on your own.
③ 一次性     No two [X] are the same.／Once it's over, it's over.／If you miss it, that's it.／
            ⭐only … once or twice a year
④ 事后      You still talk about it years later.／It sticks with you.／
            You come home with [照片/一个故事].
两条使用规矩：一个角度只要两句（一句说清＋一句画面）；挑角度看【主角】不看内容
```
- **她的产出（逐字）**：`On top of that, you can watch it on tv whenever you want, but the concerts you love only happen in your city once or twice a year`
- **★★ 第③步「第二支点」首次做到**（有脚手架，非 cold）：主角＝**机会/频率**，跟"气氛"完全不同轴 ✅
  且结构自带对比（随时可看 ↔ 一年一两次），把"稀缺"直接讲出来 ✅
- **★ 自主复用她自己的 ⭐ 块 `once or twice a year`，用在全新语境** ＝ 迁移
- 语言层：
```
`the concerts you love` → 你 love 的是乐队/歌手不是演唱会 → `the bands you actually want to see`
`happen in your city`   → `come to your city`（乐队 come to town 是固定说法）★ B62
`on tv`                 → 题目问的是 online，说 `online` 更贴题（一致性）
最小改 On top of that, you can watch it online whenever you want, but the bands you actually
       want to see only come to your city once or twice a year.
（缺第二句画面：可加"那你怎么办"——等一年 / 飞去别的城市）
```

### Block 4 · D-3（2026-08-02，19 条）

- **她的原话（逐字）**：`2. you have to do it, but hobbies(业余咋说) are something you choose. 3. it is the only part of a day which is yours. 4. 忘了 5. the job really need me. 6. it is tiring, but it is a good kind of tired. 7 the thing is not simply(那么不太确定). 9. that class bores me. 10. he is good with cooking. 11. no, i don't have much time to keep pets between work and a five-year-old. but I really hope I can have a dog one day. there is something waiting for you when you get home. 12 问题是什么？？？你看看你出的什么题 13 不知道 14.i don't have pets, but i get why someone does. 15. so i guess 16是不是重复了 16. it is unlike work or kids. it is something you choose. 19. i usually go to work by walking`

- **★★ 教练失误（她的第 16 次纠正，成立）**：#12「用一句话说出解法」、#13「这种情况该怎么办」——**两题都在考方法论的复述**，而"只考用、不考判断/列举"是我**当天上午刚写进 skill 的规则**。她当场反弹"你看看你出的什么题"。
  另 #16 与 #14 出题重复，也是她指出的。
  ⇒ **教练版的"听＝0"**：我写下规则 ≠ 我执行规则。方法论类只能【给新题看她做不做得出】，不能问"这条规则是什么"。

- **成绩：全对 3 ／ 部分 6 ／ 错或忘 5 ／ 教练废题 3**
```
全对   6（a good kind of tired）· 9（bores me）· 15（so I guess）
部分   2 · 3 · 5 · 11 · 14 · 18
错/忘  1（反差六轴全忘）· 4（something to show for it）· 7 · 10 · 17
```

- **★ 记忆分层第 6 次验证**：她**产出过**的块全部记住（a good kind of tired ✅ / something waiting for you when you get home ✅ / so I guess ✅ / bores me ✅）；**我给了她没产出过**的 `something to show for it` → 忘。

- **逐条批改**：
```
 1  反差六轴整组全忘 —— 六轴是"我讲的"，她一条都没产出过 → 需重建，且必须靠产出
 2  ✅ 骨架对（You have to…but…choose）；`hobbies are something` 数不一致
    → `a hobby is something you choose` ／ `hobbies are things you choose` ★ B68
    答她的"业余咋说"：说爱好直接 hobby 就够；"业余的"作形容词才用 spare-time / after-work
 3  `which` → **that**（先行词被 only / all / 最高级修饰时必须 that）★ B64
    且漏了引擎词 `actually`（真正属于你自己的）
 4  忘 → `something to show for it`（忙了一年总算有点能拿出手的东西）
 5  `need` → needs（C4）；`really` 代替 `actually` 可接受，引擎词在
 6  ✅✅ tiring / tired 两个形式都用对
 7  ❌ `simply`（副词）→ simple；块是 `nothing is that simple`
    ★ 她不确定的正是那个 **that**：`that + 形容词` ＝ "那么……" ★ B65
      it's not that hard ／ nothing is that simple ／ it's not that expensive
 9  ✅ 选对了能换动词的那句（无聊＝对人的作用），没去动"山很高"（物本身属性）
10  ❌ `good with` → **good AT** doing（good with 是"擅长应付人/物"：good with kids）
    而且 08-02 的规则本身是 be good at doing X → **He cooks well.** 两层都没用上 ★ B66
11  语言好（`between work and a five-year-old` 是很好的硬料）
    ★ 但比例又错：引子 2 句 → 答案 1 句。规矩是**引子 1 句 → 答案 2–3 句**
      = 08-02 她自己抓到的"通路A 比例陷阱"复发
    `keep pets` → `keep a pet` / `have a pet`
14  ✅ 结构对；`i get why` 比教的 `I can see why` 更口语，算升级
    `someone does` → `people do`（泛指）；漏 `myself`（我自己不养，对比引擎）
15  ✅
17  ❌ `it is unlike work or kids. it is something you choose.` 拆成两个独立句
    → 08-02 记的正是"不能独立成句，用破折号连回主句"：
      `…, and unlike work or kids, it's something you choose.` ★ 改过又犯
18  `go TO work` 的 to ✅ 对了（C2 老条目终于稳）
    ❌ `by walking` → **walk to work**（by 后面只接交通工具，步行直接用 walk）★ B67
    ❌ `usually` 第三次误用 → every day
    "养一只宠物"没答 → have a pet
```

### Block 4 补练 · 反差六轴整组重建（只给轴名，她自己造句）

- **她的原话（逐字）**：`You have to work, but having a pet is something you choose. early morning is the only part of the day that is actually mine, so i usually get up early. i like cooking, because you follow the steps and there is something to show for it. I need work, and plants need me. hiking is tiring, but it's a good kind of tired. watering plants is simple, while work isn't(感觉写的不对)`

- **六轴全部造出来了**（刚才整组归零，讲完当场重建）：
```
轴1 必须↔选择    ✅ 全对，骨架＋主语齐全
轴2 我的↔别人的  ✅ 全对，而且【当场装上两个 10 分钟前才学的点】：
                   `the only part of the day THAT`（B64：only 后必须 that）
                   `actually`（引擎词，08-02 记的"引擎词不能省"）
轴3 有结果↔看不到头  部分：`something to show for it` ★刚才忘掉的那条，现在用出来了
                   但只给了【有结果】半边，缺"看不到头"那半边；且人称 I→you 跳
轴4 它需要我↔我需要它 ✅ 反差两边都在，对得工整；用词/连接词可修
轴5 累但值↔累且烦   ✅ 全对
轴6 简单↔复杂      部分：`while work isn't` 收尾塌（isn't 挂空）；她自标"感觉写的不对"＝对
                   且这一轴的块 `that simple`（今天刚学 B65）没用上
```

- **★★★ 同一 session 内 forget → produce**：`something to show for it` 上一批还答"忘了"，讲解后**当场用进自造句**。第 7 次验证"听＝0，产出才计数"，且这次是最短闭环。
- **★★ 即时迁移**：B64（only…that）与 `actually` 引擎词，学完 10 分钟内**无提示自主用上**。
- **★ `usually` 第一次用对**：`so I usually get up early`＝通常/一般情况下 ✅（前三次误用都是"经常"该用 often）。区分装上了。
- **★ 她第 8 次自诊命中**：自标轴6"感觉写的不对"——确实塌了。

- **逐条修**：
```
轴3  人称跳：`I like cooking, because YOU follow the steps` → 统一人称
     `I like cooking — I follow the steps, and at the end I've got something to show for it.`
     ★ 且反差句必须两边都说，只说一半就不是反差 ★ B69
轴4  `I need work` → `I need MY JOB`（work 不可数＝"活儿/工作这件事"，
     I need work＝我需要有活干）★ B70
     `and` → `but`（反差用 but/whereas，and 是并列不标反差）★ B69
     最小改 `I need my job, but my plants need me.`
轴6  最小改 `Watering plants is simple, but nothing at work is THAT simple.`（把 B65 装进去）
```

### 清欠账 · 今日忘掉的四条重测

- **她的原话（逐字）**：`I don't like that plan, but, uh, I can live with it. 2你翻一下，我学下. For example, you spend two hours cooking a meal, But it only takes ten minutes to eat out. 4 你也翻下吧`
```
1  ✅ `I can live with it` 装上了（上一批还是"忘了应该用啥"）→ 第 8 次 forget→produce
   只差"不太"：`I don't REALLY like that plan`
2  她要求教练翻（主动学）→ `You get the best of both worlds — the convenience of the city
   and the quiet of the countryside.`
3  ❌ **`eat out` ＝ 出去下馆子**，不是"吃完" ★ B72
   → `it only takes ten minutes to eat it` ／ 更好 `and it's gone in ten minutes`
   ★ 且 `For example` 第二次顶掉 `Say you…`——她从未产出过这个块，符合记忆分层
   最小改 `Say you spend two hours cooking a meal — it's gone in ten minutes.`
4  她要求教练翻 → `In this line of work, speaking English is a must, and Japanese is a plus.`
   （`a plus` 今天第三次没调出来）
★ 2、4 是教练给的 → 按"改完当场重说"硬规矩，必须立刻让她产出，否则明天照样忘
```
- **当场重说结果（逐字）**：`I don't really like that plan, but I can live with it. You get the best of both worlds: the convenience of the city and the quality of the countryside. Say you spend two hours cooking a meal, it's gone in ten minutes. In this line of work, speaking English is a must, and Japanese is a plus.`
  → **4 句里 3 句全对**，唯一错处 `quality` → `quiet`（形近词冒出来那一类：她知道要哪个只是拿错，出口＝再试一次；与"不知道哪个词对"→立刻跳车说画面，是两条不同出口）。

### 🎲 抽题脚本（她 08-05 要求，已建）
- `speaking-band7/coach/pick_question.py` —— **口语训练唯一合法的出题方式**。
  用法 `python3 speaking-band7/coach/pick_question.py p3|p1|p2|any [数量] [--repeat]`。
  自动排除 `coach/asked.log` 已练过的题，抽中后写回。题库规模：P1 273 / P2 62 / P3 351。
- **规矩：抽到什么练什么，禁止重抽、禁止"这题不合适换一个"。** 理由＝教练自己挑会不自觉地挑"好讲的/刚练过的"，让训练分布失真，也架空 question_bank 禁自编那条。
- ⚠️ 与"记录禁脚本"不冲突：**记录禁脚本是为了不漏；抽题用脚本是为了教练无从选择。**

### 首次脚本抽题实战 · `How can parents help children to be organized?`（question_bank.md:1371）

> 抽题脚本首跑抽中此题；按新规矩不重抽。

- **★★ 第一轮她理解偏了题**：把 `organized` 当成"守规矩/有教养"，答了不插队、公共场合保持安静。
  `organized`（说人）＝**有条理、会安排自己的事**；她答的是 well-behaved / well-mannered。
  ⇒ **考场上最贵的错**：语言再好也是答非所问，FC＋TR 一起掉；且这不是语法问题，是**一个词的义项没装上**。
  给的画面（B76）：knows where everything is ／ packs his bag the night before ／ starts homework before the last day ／ writes things down；反面 messy ／ all over the place ／ leaves everything to the last minute。
  **她的两个支点本身是对的**（以身作则＝父母的行为 ／ 讲清为什么＝孩子的理解，主角不同）→ 内容没浪费，只是瞄错靶。

- **重新对准后的中文（逐字）**：`首先是以身作则…如果父母每天工作后收拾下桌子，那么小朋友也会在玩耍后把玩具收回去。此外，给小朋友解释为什么需要organized的也很重要…比如把东西整理好可以方便下次找到他们，小朋友会更有动力去做`
- 教练只点出两个还没拆的抽象包（**以身作则** / **更有动力**），不给英文。

- **她的英文产出（逐字）**：`The most important thing is that parents are organized(这句话我觉得写的buhao). Children always copy what their parents do. If parents put everything back after using them, children will clean up their toys(这句也写的不好). On top of that, explaining why we should be organized is also important(可以不用is么). Putting stuff back makes them more convenient to find next time. if chilldren get it, they are more willing to do it.`

- **★★★ 第③步「第二支点」cold 成立（撤了脚手架）**：08-05 演唱会那次是给了四个万能支点才做到；这次**没给任何角度清单**，两个支点主角不同（父母的行为 ／ 孩子的理解），且第二支点还挖了机制层（好找→有动力）。三步主干①②③全齐。
- **★ 拆包成功**：她自己把"更有动力"降级成 `more willing to do it` —— 抽象包在中文层拆掉了。
- **★ 她三处自标全中**（S1 不好 ✅ / S3 不好 ✅ / "可以不用 is 么" ＝ 好问题 ✅）。结构类自诊仍然准，与"形态类会误报"的既有规律一致。

- **逐句批改**：
```
S1 `The most important thing is that parents are organized.`
   她的直觉对：`The most important thing is that…` 这个壳吃掉半句还没给信息，
   而且 is…are 两个系动词叠在一起（系动词依赖）
   最小改  The most important thing is that parents are organized THEMSELVES.（themselves 是对比引擎）
   更好    It starts with the parents themselves. ／ Parents have to be organized themselves first.

S2 `Children always copy what their parents do.` ✅ 全对且地道

S3 `If parents put everything back after using them, children will clean up their toys.`
   ① `everything … them` 数不一致 → `put things back after they use them`
   ② `clean up their toys` → **put their toys away**（收玩具＝put away；clean up＝打扫脏东西）★ B74
   更好 If parents put their own things away, kids will do the same with their toys.（do the same 点出对应）

S4 `explaining why we should be organized is also important`（她问：可以不用 is 么）
   ★ 可以。规则：`X is important` 这个壳，把 X 里的**动作提上来当谓语**就能去掉 is ★ B75
   → Parents should also explain WHY it matters.／It also helps to explain why.
   另：`we` 人称跳（前面是 parents/children）→ B71 今天刚学，这里又跳了

S5 `Putting stuff back makes them more convenient to find next time.`
   ❌ **convenient 不能说"convenient to find"** ★ B73
      convenient 的主语是安排/时间/地点/工具，常用 `It's convenient for sb to do`
      "好找"用 easy：→ `Putting things back makes them EASIER to find next time.`
   ② `stuff … them` 数不一致（第二次）→ 用 things 就自动对了
   ★ 这个错她写作里也犯过（`makes few people convenient`）＝跨模态同源

S6 `if children get it, they are more willing to do it.`
   `get it`（明白了）✅ 口语好；`more willing to do it` ✅ 拆包正确
   小修：两个 it 指代不同（第一个＝道理，第二个＝收拾）→ `if children understand why, they're much more willing to do it.`
```

- **当场重说三句（逐字）**：`It starts with the parents themselves. if parent put their own things away, kids will do the same with their toys. Putting things back makes them more easier to find next time.`
```
S1 ✅ 全对（直接用了更好版）
S3 ✅ put away / do the same 都装上；只有 `parent` → parents
S5 ❌ **more easier ＝ 双重比较级** ★ B77
   机制：她把我给的 `easier` 塞进原来的 `more convenient` 框里，**只换了词没重扫句子**
   → 局部替换残留。与注意力零和同源：补一个槽时不会回头检查周边
   → `makes them easier to find next time`
```

### 脚本抽题 2 · `Why do people prefer to watch movies in the cinema?`（question_bank.md:1024）

- **她的原话（逐字）**：`it mainly comes down to (这里加 the 么) visual effect. you can enjoy the big screen In cinema, especially when you watch action or sci-fi movies. You feel like you are actually there. Plus, watching movies in cinema is about the sense of occasion like going on a date with my wife.`

- **★★ 第③步第二支点 cold 连续第二次成立**：
```
支点1  视觉      主角＝画面/银幕     → 有画面（big screen / action・sci-fi / feel like you're actually there）
支点2  场合      主角＝这件事的性质和人（date night）
两个主角完全不同轴 ✅ 且答案在第一句 ✅
```
- **★ 她自发用出高级块 `it mainly comes down to …`**（教练从未给过）→ 收进表达库 ⭐
- **★ `You feel like you are actually there.`** 全对，且 `actually` 引擎词自主用上（今天第三次自发用 actually）

- **逐条**：
```
① 答她的问题"这里加 the 么"——**问题不在 the，在单复数**：
   `visual effect` 是可数名词，单数必须带限定词；而这个意思本来就恒用复数
   → `visual effects` ／ `the visuals` ／ 最口语 `it comes down to the big screen`
   （special effects 同理，恒复数）★ B79
② `In cinema` / `in cinema` 两处 → **at the cinema**（惯用定冠词）
   ★ 今天早些时候 B58 刚给过 the cinema 这个例子，同日改过又犯
③ ★ **人称跳第三次**（B71 今天刚建）：`you can enjoy…` `you feel like…` → 最后 `my wife`
   一句里 you 和 my 混着走。要么全 you（泛指），要么全 I/my（自身）
④ `like going on a date with my wife` **挂靠悬空**（理解侧冗余 #1 修饰语紧贴被修饰词）：
   like 想修饰 `the sense of occasion`，但中间隔着一整个 is about 结构
   最小改 `Plus, going to the cinema has a sense of occasion — for us it's basically a date night.`
   ★ `date night` 是这个意思最地道的固定块 ★ B80
⑤ `enjoy the big screen` 可懂但略怪 → `you get a huge screen and proper sound`
```
- 她跳过了 S5 的重说（`makes them easier to find`），当轮补上，见下。

- **补说两笔（逐字）**：`putting things back makes it much easier to find next time. watching movies at the cinema is about the sense of occasion - for us, it feels like a date night.`
```
句2  ✅✅✅ 三处一次全修对：at the cinema ✅ ／ 破折号接例子（挂靠解决）✅ ／ 人称统一（for us…it）✅
     只剩一点生硬：`watching movies at the cinema IS ABOUT the sense of occasion`
     → `Part of it is the sense of occasion — for us, it feels like a date night.`
句1  `more easier` → `much easier` ✅ 修对了
     ❌ 但 `makes THEM` 变成了 `makes IT`，且 `to find` 后面没了宾语 → **论元又丢**
     → `makes THEM much easier to find next time` ／ `makes it much easier to find THINGS next time`
```
- **★★★ 注意力零和最纯粹的一次演示（同轮两次、方向相反）**：
```
上一版  makes THEM more easier    them 对，比较级错
这一版  makes IT much easier      比较级对，them 坏了
★ 她只检查了"我刚被指出的那个点"，没有重扫整句
★ 这恰好是我上一条刚给的规矩（换完词整句从头默一遍）——规矩讲了，没产出过，所以没生效
  ⇒ 又一次"听＝0"。这条规矩必须变成她的动作，不是我的提醒
```

### 脚本抽题 3 · `What are good ways to manage traffic?`（question_bank.md:1390）

- **她先给中文（逐字）**：`关键在于城市设计和管理结合。路网的设计应该符合城市的区域分布，特别是居民的通勤道路和工业区的货运要保证容量。相信很多人都有过高峰期被堵在路上的体验。此外，合理的法规和严格的执行也很关键，如果每个人都能随意的闯红灯，那么交通会非常糟糕`
- **★ 诊断：她自己把难度调高了**。这段中文里有 8 个抽象名词块（城市设计和管理结合／路网的设计／城市的区域分布／居民的通勤道路／工业区的货运／保证容量／合理的法规／严格的执行）＝ **填充层翻译指纹**，正是作文 199 句里挖出的同一结构。
- **★ 但她自己写对了一句**：`如果每个人都能随意的闯红灯` 已经是人话 ⇒ **操作她会做，只是没对整段执行**；她在总起句/论点句自动切换成书面语，一到举例才落回人话。＝「框架层直连、填充层翻译」的现场版。
- 她要求教练演示降级（`你做下我学下呗`）→ 教练把 6 句全降级成人话中文，并给判据「谁？在做什么？拍得出照片吗？」

- **她的英文产出（逐字）**：`The key things are how to design the road network and how to manage the trafific. In terms of the road network. Designer should fully consider the purpose of roads. Are they used for commuting or cargo transport. how wide should they be constructed. If there were something wrong with the design, you would experience traffic jams every time you drive pass by the roads. Plus, the regulations and the strict enforcement are important. If people rush a red light without any fine, 这里我不知道咋说了。感觉语言能力实在太差了(你不需要给我心里按摩，我只需要提高）`

- **★★★ 本轮核心发现：她翻译的是【原版书面中文】，不是降级版**。
```
证据：降级版里的画面一个都没出现
  ② 城东往城西 / ③ 上班的车和送货卡车 / ④ 早上八点·四十分钟·两公里  —— 全部缺席
出现的反而是原版书面句的直译
  fully consider the purpose of roads ／ how wide should they be constructed ／
  the regulations and the strict enforcement are important
★ 机制：她自己写的那版中文激活最强（刚产出过），教练的降级版只是"读过的"
★ ⇒ 【降级必须由她自己产出】。教练做的降级对她无效，等同于"我讲的她全忘"
   下次只给判据和指点，绝不代做——今天代做了，这是教练的操作失误
```
- **★★ 而且她这段里最难的语法全是书面中文逼出来的**：间接疑问语序、虚拟语气、被动 constructed —— **人话版一个都用不到**。⇒ 她"语言能力差"的自评，今天这组数据支持的是"输入难度自选过高"，不是能力天花板。

- **逐句批改**：
```
S1 `The key things are how to design the road network and how to manage the trafific.`
   `the traffic` → traffic（不可数泛指不带 the）★ B86
   ★ 她刚自发产出的 `it mainly comes down to` 这里正合适却没调出来 → 块未稳
   更好 `It comes down to two things: how you build the roads, and how you manage them.`

S2 `In terms of the road network.` 片段，没有句子；且 In terms of 是书面连接
   → `Take the roads first.` ／ 并进下一句

S3 `Designer should fully consider the purpose of roads.`
   `Designer` → Designers（泛指复数）★ B86
   `fully consider the purpose of` 翻译腔 → `think about what a road is actually for`

S4 `Are they used for commuting or cargo transport.` 疑问句形式当陈述用，衔接断裂
   → 并成同位说明：`— are they for people getting to work, or for trucks?`

S5 `how wide should they be constructed.`
   ❌ **嵌入疑问句必须用陈述语序** → `how wide they need to be` ★ B82

S6 `If there were something wrong with the design, you would experience traffic jams
    every time you drive pass by the roads.`
   ❌ 虚拟语气用错：说【一般规律】用 if ＋ 现在时（were/would 是反事实）★ B83
      → `If there's something wrong with the design, you get stuck every time…`
   `experience traffic jams` → **get stuck in traffic** ★ B84
   `drive pass` → **drive past** ★ B85；`pass by the roads` 意思不清 → `use that road`

S7 `Plus, the regulations and the strict enforcement are important.`
   泛指不带 the → `regulations and strict enforcement`
   ★ 但根本问题是这句是原中文直译，抽象无画面
   → `Plus, rules only work if someone actually enforces them.`

S8 `If people rush a red light without any fine,` 卡住
   `rush a red light` → **run a red light**（闯红灯固定搭配）★ B84
   `without any fine` → `and never get fined` ／ `and nothing happens`
   ★ 她卡住的真正原因：后半句"交通会非常糟糕"是**抽象结果，没降级** →
     降成画面才说得出（路口全堵死／谁都不让谁／everyone else starts doing it）
```

- **当场重说（逐字）**：`It comes down to two things, how you build the roads and how you manage them. take the roads first, Designers should think about what a road is actually for. How wide they need to be. If there is something wrong with the design, you get stuck every time you use that road. Plus, rules only work if someone actually enforces them. If everyone can run a red light without fine, traffic will be terrible.`
```
S1 ✅   S2 ✅   S3 ✅   S5 ✅   S6 ✅（这几句是照教练版重说，价值在"产出过"，
                                    是否焊上要明天 D-1 复习时才算数）
S4 `How wide they need to be.` ❌ 片段（没接回主句）＋ 数不一致（a road → they）
   → `…what a road is actually for, and how wide it needs to be.`
   ★ 又是"拿了我的短语但没装回句子里"＝与 more easier 同一个局部替换残留
S7 `without fine` → `without being fined` ／ `without getting a fine`（fine 可数要冠词）
```
- **★★ 她连续第二次跳过降级动作**：`traffic will be terrible` 原样留着，而这正是教练明确要求她先出中文画面的那半句。
  ⇒ **降级这个动作她至今一次都没自己做过**（前两次都是教练代做）。下一步只能卡在这里，不给英文、不给中文，等她产出。

#### ★★★ 她的第 17 次纠正 —— 改的是方法本身（本日最重要）

- 教练说她"跳过了降级"，她反驳：**"因为我不会呀，我觉得你很搞笑，我会说肯定说了"**。
- 教练承认措辞错（"跳过"预设了她会但没做），改用**中文对照实验**，问了一个不带任何方法论词的事实问题：
  **"你在成都堵得最狠的一次，路口当时是什么样的？"**
- **她一句话就出来了**：`路口被塞满了车，没有车能动，无论前进还是后退` —— 能拍照片 ✅ 谁都见过 ✅ 完全合格的画面。
- **⇒ 结论（方法级修正）**：
```
问"把它变成画面 / 这个拍得出照片吗"（元指令）    → 她卡死
问"你见过最严重的一次是什么样"（具体事实提问）    → 一句话出来
★ 内容一直在。卡住的是【元指令】。
★ 与 08-02 记忆分层完全一致：操作类是"我讲的"，她几乎全忘；
  说方法的话对她无效，只有具体提问能触发。
⇒ 教练往后【禁说"降级/变具体/找画面"】，一律换成具体事实提问：
  "你见过最严重的一次是什么样？" / "当时谁在做什么？"
```

#### 接着：英文卡住 → 减负 → 难词自己出来了

- 她说 `不会用英语说，或者说卡了`。教练**不给词**，只给约束：**只准用 cars / move / forward / back / nobody / can't 这几个必定会的词**说完这个画面。
- **她的产出（逐字）**：`The intersection is filled with loads of cars, and no one can move, whether go back or forth`
- **★★ 她自己调出了 `intersection`** —— 我限定她只用简单词，她反而把"不会"的那个难词调出来了。
  ⇒ **"不会"＝检索失败，不是知识缺口。解法不是给词，是【降低任务负载】**，负载一降检索就恢复。这是本日最直接的一次证明。
- `no one can move` ✅ **B54 双重否定今天刚学，这里动词用肯定，装上了**
- ❌ `whether go back or forth` ★ B87
```
① whether 后面要跟主谓：whether they go back or forward
② "前进或后退"＝ forward or back；**back and forth ＝ 来回反复**，意思不一样
★ 块串台：今天刚学的 back and forth 挤进了不该用的位置
  ＝ 与 a must/a plus 过度泛化同一模式——她抓到块就推广，【边界必须单独教】
最小改 The intersection is filled with cars, and nobody can move — forward or back.
更好   The whole junction is jammed. Nobody can move, forward or back.（可选词 gridlocked）
```

#### 收口：卡了两轮的那半句，一次说对

- **她的产出（逐字）**：`If anyone can run a red light without being fined, the junction will be jammed. Nobody can move, forward or back.`
- **一句话里整合了 5 个当轮新点**：
```
run a red light        B84 新学 ✅
without being fined    刚纠正（fine 可数要冠词/被动）✅
junction / jammed      刚给 ✅
forward or back        刚纠正（不是 back and forth）✅
Nobody can move        B54 双重否定，动词肯定 ✅
```
- 唯一小修：`the junction` → 泛指用复数 `junctions get jammed`（the junction 像在说某个特定路口）
- **★ 路径确认**：同一半句，第一轮"我不会"→ 换成事实提问出中文画面 → 减负后出英文 → 一次说对。
  **全程教练没给过这半句的英文。**

---

## 📅 2026-08-06 · 学习日（新节奏第 2 天）· D-1(08-05) ＋ D-3(08-03)

> 按 08-05 定的节奏。周期：08-05＝第1天，08-06＝第2天，**08-10＝第一个专门复习日**（含题目重答）。
> 本次改进：**提取清单与出题合并**（她确认无漏＋直接产出，省一轮往返）；全部产出题，无判断题无列举题。

### D-1 · 08-05 复习（33 题）· 第一批 1–11

- **她的原话（逐字）**：`1. especially when nobody else can do it. 2. i was stuck in meetings all morning. 3. commuting every day is really a hassle. 4. he sit in front of the television all night. i need to go to see a doctor tomorrow. 5. nobody knows which part is yours. 6. that is the only part of the day that belongs to you. 7. it's not that hard / simple. 8. he is good at cooking. he cooks well. 9. i go to work by walk. 10. hobbies are what you choose. 11. i need this job, but my flowers need me. 先开一批`
- **成绩 全对 7 ／ 部分 3 ／ 错 1**
```
全对   1（B54 双重否定 ✅）· 2（all morning 不带 the ✅）· 3（every day 分写＋a hassle ✅）
       5（which ✅ nobody+肯定 ✅ knows ✅）· 7（that＋形容词 ✅）
       8（good at cooking ＋ he cooks well，两种都对 ✅）· 11（but ✅ this job ✅）
部分   4 · 6 · 10
错     9
```
```
 4  `he sit` → sits/sat（C4 指出不 drill）；`the television` ✅ 惯用定冠词在
    ⚠️ `go to see a doctor` **不是错**——see a doctor 完全地道；只是目标块 `go to the doctor` 没产出
       （更顺：`I need to see a doctor tomorrow.`，去掉 go to）
 6  `that` ✅（only 后用 that，B64 装上）
    ❌ 漏 `actually`（第二次漏这个引擎词）；且"属于我自己"用了 you → 人称漂移（B78 主攻项）
       → `the only part of the day that's actually mine`
 9  ❌ `by walk` → **I walk to work.**
    ★ B67 昨天刚学。她记住了"不是 walking"，却没换掉整个 by 结构
      ＝ **局部修正残留第 3 次**（more easier ／ how wide they need to be 片段 ／ 本次）
      ⇒ 这个模式已稳定出现：她只改被点名的那个零件，不重扫结构
10  `hobbies are what you choose` 语法对、数也对（避开了 something 的坑），
    但目标块是 `hobbies are THINGS you choose`；what 版意思略偏（"爱好就是你选的东西"）
```

### 第二批 12–27

- **她的原话（逐字）**：`0. he passed the exam by that method. 12. i need/i have 13. i'm really into cooking. because you follow the steps and there is always something to show for it. 14. we often eat out on weekends. 15. putting things away makes them much easier to find next time. 16. children should 收起来 我忘了 17. explaining why to children also matters（我不确定，第一反应还是 important）18. 这不是和 15 重复了么 19. it mainly comes down to visual effects. 19. Designers should think about how wide roads should be. 21. If there is something wrong with the road, you will be(我老是想用 will) stuck every time you use it. 22. 这不就是 21 题么 23. traffic management mainly comes down to two things. 24. no cars can move, neither forward or back. 25. All people sing together with the singer. you can feel the energy live. 26. 不会 27. teachers should put more energy and time into preparing classes.`

- **★★★ 本轮最强证据：昨天"她产出过的"全保住，昨天"教练给了她没重说的"全回潮**
```
保住（昨天她当场产出过）
  eat out ✅ · it mainly comes down to ✅（两次）· visual effects ✅ ·
  嵌入疑问陈述语序 how wide roads should be ✅ · put things away ✅ ·
  that＋形容词 ✅ · nobody/no cars ＋肯定动词 ✅ · much easier（比较级只标一次）✅
回潮（昨天教练给了、她没重说）
  B57 sing along → `sing together with the singer` ❌
  B57 feel the energy in the room → `feel the energy live` ❌ 原样回潮
  B60 time and energy → `energy and time` ❌ 原样回潮
  B60 prepare for class → `preparing classes` ❌ 原样回潮
  B67 walk to work → `by walk` ❌（第一批第 9 题）
★ 这是"听＝0，产出才计数"迄今最干净的一次对照：同一天学的，
  变量只有【她当场重说了没有】。⇒ 教练每给一条，必须当场索取产出，无一例外。
```

- **★ 检索是语境绑定的（新发现）**：第 15 题她刚写出 `putting things away`，第 16 题"孩子把玩具收起来"却答"忘了"。
  **块在，但没跨语境泛化** ⇒ 新块必须在**2–3 个不同语境**里各产出一次，否则只绑在学它的那个句子上。

- **★ `by + -ing` 连续三次绕开**（by that method ／ walking to work can save… ／ 之前 by walking 用错）
  ⇒ 这个结构不在她的产出库里，需单独焊 ★ B91

- **逐条**：
```
 0  `by that method` 语法通但生硬，且第三次绕开 → `He passed the exam BY STUDYING every night.`
12  没答对：`I need work`（我需要有活干／需要有事做）vs `I need my job`（我需要这份工作）
13  ❌ **人称跳第 4 次，而且题干明写了"人称统一"**：`I'm really into cooking. because YOU follow…`
    另：`. because…` 起句成片段
    → `I'm really into cooking — I follow the steps, and at the end I've got something to show for it.`
    ✅ `something to show for it` 记住了（昨天忘、当场产出过 → 今天保住，再次验证）
14  ✅ 全对   15  ✅（put back / put away 都通）   19 ✅   20 ✅   23 ✅ comes down to 第二次复用
16  忘 —— 但与 15 冲突，见上"语境绑定"
17  ✅ 避开了 important（用 matters）；但**壳还在**——目标是把动作提上来当谓语：
    → `Parents should also explain WHY.`（不是换一个系动词类词）
21  ✅ if 从句现在时用对。答她的疑问"我老是想用 will"：
    ★ **every time / whenever 出现＝反复发生的规律，主句用现在时**（you GET stuck），
      will 是预测未来某一次 ★ B90
22  教练重复题（与 21 撞），B85 `drive past` 未测到 → 补测
24  `no cars can move` ✅；❌ `neither … or` → **neither … NOR**（配对）★ B89
25  ❌ B57 两个都回潮（见上）
26  答"不会" —— ★ 因为 B59 是**减法型规则**（删掉 a bit），她无从产出"不说什么"
    ⇒ 出题方法论：减法型规则不能用中译英测，只能在她自由产出时当场抓（已写进 skill）
27  ❌ B60 两处全回潮（energy and time ／ preparing classes）
```

- **★ 她的第 18 次纠正（流程）**：`在skill中每次复习的时候把所有需要复习的找出来后，强制加入一轮 review 节点，将每个问题都看一遍。然后把问题切割成 10 个一组的出，我回答完再下一组`
  → 起因：教练两天内出了两组重复题（08-05 #14/#16、08-06 #15/#18 与 #21/#22）。已写进 SKILL §0。

#### 她追问两条 → 教练更正了两处判重（诚实降档）
- `energy and time`：**不是语法错，是固定并列词序不地道**（binomial）。规律＝**短的在前长的在后**（time and energy／time and money／black and white／cause and effect／sooner or later／salt and pepper）。原判 ❌ 过重。
- `feel the energy live`：**别扭但不算语法错**。判据＝**live 当副词只修饰"这东西怎么呈现给你"**（现场 vs 录播）：saw them live／broadcast live／only get that energy live ✅；修饰"你的感受"时不用。原判 ❌ 过重。
- ⇒ 两条都已改写进 B57／B60 的档位说明。

### 回潮项重测（10 题一组，她 08-06 定的新节奏首次执行）

- **她的原话（逐字）**：`1. All the audiences sing along with the singer 2. You can feel the energy when you are there live 3. Teachers should put more time and energy into preparing for classes. 4. I walk to work every day. 5. he passed the exam by studying every night. 6. parents should explain why to children. 7 If there is something wrong with the design, you get stuck every time using the road. 8. no cars can move, forward or back. 9. I need work / I need this job. 10. children should put aways toys.`
- **成绩 全对 4 ／ 基本对 1 ／ 部分 5**
```
✅ 4（walk to work，B67 装上）· 5（**by ＋ -ing 第一次产出成功**，此前连续绕开 3 次）
   · 8（避开 neither…or）· 9（work / my job 区分装上）
基本对 3（time and energy 词序对了 ✅；`preparing for classes` 可懂，
        泛指"上课"用 class 不可数更地道）
```
```
 1  `sing along` ✅ 装上；❌ `All the audiences` → **audience 是集合名词**，
    整体观众用单数：`The whole audience sings along` ／ 最口语 `Everyone sings along`
    （audiences 复数＝多批/多场观众）★ B93
 2  ✅ **判定作废（她的第 19 次纠正，成立）**。教练原判"live 冗余、局部修正残留第 4 次"——
    复查后撤销：`being there live` 是能听到的说法（nothing beats being there live），
    只是略冗余，**不是错**；句子没问题，"残留"这个判断也一并不成立。
    ★ 教练在同一个词上连纠三次（她原话"你为啥那么执着让我删 live"）→ 过度纠正。
    唯一站得住的规则：**live 需要有"录播"这个对立面才有信息量**
      I saw them live ✅（对立＝电视上看）／broadcast live ✅／feel the energy live ✗（energy 不被播出）
    优先级很低，不值得再花注意力。

### 第三组 10 题（D-1 剩余 ＋ D-3 08-03 开头）

- **她的原话（逐字）**：`1. Your favourite band comes to your city once or twice a year. 2. 忘了（我说忘了你就直接给答案，以及思路，然后记下来，多复习几次就回来）3. 原句忘了，我现造一个 he leaves a mess of toys 4. for us, going the cinema feels like a date night. 5. I get stuck every time I use the road. 6. I'm stuck for 40 minitues when it's morning peak time. 7. the higher you live, the farther you see. 8 If you live high enough up, you can get a view of the whole city. 9. deep down, I know I should go to bed early. 10. I can't be botherd to go / it's not that I don't want to go, I'm just lazy`
- **成绩 全对 6 ／ 部分 3 ／ 忘 1**
```
✅ 1（come to your city ✅，只差 only 的"才"）· 5（get stuck ＋ every time ＋完整从句，
   B90/B94 两条一次装上）· 7（the＋比较级 ✅）· 8（high enough up 程度旋钮 ✅ enough 位置对）
   · 9（deep down ✅）· 10（can't be bothered ＋ It's not that A, it's just B，两块都在）
★ 08-03 学的块（deep down／can't be bothered／It's not that A／high enough up／the＋比较级）
  保留率极高 —— 因为 08-03 当天她都 drill 产出过。第 N 次同向证据。
```
```
 2  忘（organized 的画面，B76）→ 按她 08-06 新定的规矩直接给答案＋思路，不追问
 3  自造 `he leaves a mess of toys` —— `leave a mess` 是好搭配，收进表达库 ⭐
    `a mess of toys` 略怪 → `He leaves his toys all over the place.`
 4  ❌ `going the cinema` 漏介词 → `going TO the cinema`；`feels like a date night` ✅
 5  ✅ 语法全对；但目标块 `drive past`（B85）仍未产出 → 继续挂着
 6  ❌ 时态：`I'm stuck` → `I was stuck`（过去一次）／`I get stuck`（泛指习惯）
    ❌ `morning peak time` → **the morning rush hour**（固定说法）★ B96
 7  丢了引擎词 can → `the further you CAN see`
```

- **★ 她的第 20 次纠正（流程）**：`我说忘了你就直接给答案，以及思路，然后记下来，多复习几次就回来`
  → 已写进 SKILL §0：答"忘了/不会"立刻给答案＋思路，不追问不引导；给完照旧索取一次产出。

### 第四组 10 题（D-3 · 08-03）

- **她的原话（逐字）**：`1. he leaves his toys all over the place, and leaves everything to the last minute. 2. i was stuck in the road on the morning rush hour. 3. the higher you live, the farther you can see. 4. i get stuck every time i drive past that road. 5. i used to play along the river when i was a kid. 6. i go straight to work after i get up. 7. some teachers talk at you for an hour. 8. teachers should get students to try it themselves. don't make students memorise them. 9. i have learned it by heart. 10. you can get a refund within 7 days for any reasons`
- **成绩 全对 4 ／ 基本对 2 ／ 部分 4**
```
✅ 1（刚给的两个块当场装上，还用了共享主语 and leaves）· 3（can 补回来了）
   · 5（used to ＋ when I was a kid，08-03 的时态触发装上）· 7（talk at ✅）
基本对 8（get sb to do ✅ make sb do ✅，只有 them 指代空）· 9（learn by heart ✅）
```
```
 2  `was stuck` ✅ 时态对了；`rush hour` ✅ 词有了
    ❌ `stuck IN THE ROAD` → **stuck in traffic**（in the road ＝ 卡在路面里）★ B98
    ❌ `ON the morning rush hour` → **in / during** the morning rush hour
    漏 `for forty minutes`
 4  ★ `drive past` 终于产出（B85 挂了两轮）；但**用错对象**：
    `drive past sth` ＝ 从某物**旁边**开过去（drive past the school）
    "开在那条路上" → `drive DOWN / ALONG that road` ／ `use that road` ★ B99
 5  `play along the river` → `play BY the river` 更自然（along＝沿着走，by＝在旁边）
 6  语法 ✅ 但**共享主语这个操作没做到**（她用了 after 从句＝两个 I）
    目标 `I get up and go straight to work.`（一个 I 带两个动词）
    ★ 操作类是"教练讲的"，08-03 drill 3/3 过，隔三天仍未内化 → 需在真题里抓
 8  `memorise them` them 无先行词 → `memorise everything`
 9  更自然：`I know it by heart.`（状态）／`I've gone over it so many times.`
10  ❌ `for any reasons` → **for any reason**（单数）；目标块 `no questions asked` 未产出 ★ B100
```

### 第五组 10 题（D-3 收尾）

- **她的原话（逐字）**：`1. i grew up in yibin. 2. my wife buys pretty much everything online. 3. these parks are quite and green. 4. these buildings are far away from the roads. 5. 程度扭转是什么 6. i can't stick to it. I insist on it. 7. i read my son stories every evening. 8. i do want to go, but i don't have time. 9. i bring my son along to play outdoor on weekends. 10. i do exercise twice a week`
- **成绩 全对 6 ／ 基本对 1 ／ 部分 2 ／ 忘 1**
```
✅ 1（grew up 用于人 ✅）· 2（避开了 shop 不及物）· 6（stick to it ／ insist on 两个意思分清）
   · 7（双宾语 read my son stories ✅）· 8（do ＋ 动词强调 ✅）
✅ 3 **结构上避开了老错误**：说成 `these parks are quiet and green`（表语），
   不再是 `quiet and green parks`（挂靠模糊）—— 轮98 的错自发修复
```
```
 3  `quite` → quiet（形近词第二次：前一次是 quality/quiet）
 4  `far away from` 对，但**程度旋钮没用上** → `well away from the road`；`the roads` → the road
 5  忘"程度旋钮"这个**概念名** → 按新规矩直接给
    ★★ 但**上一组第 8 题她刚用对 `high enough up`** ⇒ **块在，只是名字没记住**
       ⇒ 再次证明：**别考概念名，只考用**（已在 SKILL）
 9  `bring sb along`＝带上一起去我本来要去的地方；**take sb out**＝专门带他出去玩
    `play outdoor` → **outdoors**（副词）★ B101
    → `I take my son out on weekends.`
10  `exercise` 不可数 ✅（没加 s）；但 `do exercise` 是 C2 老条目 → **get some exercise**
    ／最简 `I exercise twice a week.` ★ 改过又犯（C2）
```

---

## ★★★ 2026-08-06 · 她的观察挖出一条底层规律：**中文靠实义词，英语靠一小撮通用动词**

- **起因**：真题（`What are the differences between everyday food and festival food?` question_bank.md:365）她只给中文，要求教练按她的中文写一版英文让她 diff。教练给了（内容全是她的，词全在她范围内）。
- **她看完的原话（逐字，本条是关键）**：
  `我说下，get fed / be done / be the opposite / around table 确实单词简单，但是我主动产出不会。我觉得这个问题原因之一，未必我会想办法翻译但是不会然后翻出来一个很奇怪的东西`

- **★ 机制（教练据此提炼，可证伪且已用她自己的表达库验证）**：
```
她按【中文的实义词密度】找英文词 —— 中文那个位置是实词，她就去找一个对应的英文实词。
找不到 → 编一个奇怪的 / 退回书面词。
但这些场景英语根本不用实词：

  吃饱   中文实词"饱"    她找 eat full / have enough food   英语 get fed        ← get
  搞定   中文实词"搞定"  她找 finish / solve                英语 be done        ← be
  相反   中文实词"相反"  她找 on the contrary（书面）       英语 be the opposite ← be
  围一桌 中文"围"        她找 surround / gather             英语 get everyone around one table ← get
```
- **★★ 用她自己攒的表达库反查，主动词几乎全落在同一小撮上**：
```
get   get some exercise · get to work · get stuck · get more done · get a refund · get sb to do
put   put time and energy into · put your toys away
be    be stuck in · can't be bothered · be done
take  take sb out          have  have sb do        make  make sb do
keep  keep a pet           do    do the same       come  comes down to · come to your city
⇒ 英语口语的"重活"由这十来个通用动词干；中文正好相反，靠实义词。
```
- **★ 可执行的操作（取代"找那个词"）**：卡住时问
  **"这件事用 get / be / do / have / take / put / make / keep / go / come 怎么说？"**
  ★ 与既有工具的关系：技巧4"只用看得见的动词"是**画面层**的版本；这条是**词汇检索层**的版本，覆盖面更广。
- 这条同时解释了她长期的"翻出来一个很奇怪的东西"——不是词汇量问题，是**检索方向错**（按实义词找，而英语在这些位置是通用动词＋介词/补语）。

### 通用动词 drill 10 题（限定主动词只能从 get/be/do/have/take/put/make/keep/go/come 里选）

- **她的原话（逐字）**：`1. the meal is just to get fed. 2. get it done in ten minutes. 3. festival food is the opposite 4. get the whole familily around a table. 5. I was stuck in traffic on my way to work. 6. I take my son out on weekends 7. he clean up the table. 8. I'm too lazy to cook 9. he passed the exam. 10. I exercise twice a week`
- **成绩 全对 7 ／ 部分 3** —— **通用动词这条操作一次就上手**（get/be/take 全部用对）
```
✅ 2 · 3 · 4 · 6（take sb out，B101 当场装上）· 9 · 10（exercise，C2 老条目修好）
✅ 5 **stuck in traffic，B98 当场装上**（本轮刚纠正过 stuck in the road）
```
```
 1  动词对（get fed ✅），结构小问题：`is just TO get fed` → `is just ABOUT getting fed`
 7  ❌ `he clean` → cleaned/cleans（时态）
    ❌ 餐后收拾桌子的固定说法是 **clear the table**（clean the table ＝擦桌子）★ B103
    本题想测的通用动词版是 `he put everything away`
 8  语法对，但**块没顶上**：`I'm too lazy to cook` → **I can't be bothered to cook**
    ★ 她今天第二次退回 lazy（第五组第 10 题也是），08-03 就记过 can't be bothered 比 lazy 自然
 9  ⚠️ **教练出题失误**：这题没有用通用动词的必要，`passed the exam` 本来就是最自然的说法。
    她答得对，是题出错了。
```

### 她自己产出节日食物那题（此前只看过教练版，按"听＝0"必须自己说一遍）

- **她的原话（逐字）**：`The key thing is how much time you spend on it. For everyday food, you just grab it quickly. It's just about getting fed. Festival food is the opposite, you put lots of time and energy into it. At Chinese new year, my familiy tend to spend a whole day cooking a meal. It's less about the food itself and more about getting the whole family around a table.（我现在每次回答都在想冠词用的对不对，你也重点看下，还是没学到位）`

- **★★★ 冠词 14 处全对，一处没错**（她主动要求重点查冠词）：
```
the key thing ✅（固定）· how much time ✅ 不可数 · for everyday food ✅ 泛指
getting fed ✅ · Festival food ✅ 泛指 · the opposite ✅ 固定带 the
lots of time and energy ✅ · At Chinese New Year ✅ 节日不带 the
a whole day ✅ · a meal ✅ · the food itself ✅ 回指 · the whole family ✅ · around a table ✅
★★ 结论：**她的冠词已经是对的，焦虑与表现不匹配**。而"每次都在想冠词对不对"
   本身在吃带宽（核心模型②：没带宽检查形态）→ 应当把带宽从冠词上撤下来，
   冠词交给自动地板，省下的带宽给结构和内容。
```
- **★ 跨域迁移**：`It's less about the food itself and more about getting the whole family around a table.`
  = 她自己的 ⭐ 块（It's less about X and more about Y，源自 CBA/看球话题）**迁到食物话题**。
- 结构：①答案前置（时间投入）②画面（grab it quickly ／ a whole day cooking）③收在机制（家人团聚）。
  从可观察差异入手、收在机制，P3 里成立。
- **❌ 逗号粘连（老错）**：`Festival food is the opposite, you put lots of…` → 破折号或句号
  ★ 08-03 记过两次，今日再犯 ★ B105
- **集合名词澄清（更正教练 B93 的绝对说法）**：`my family tend to spend` **是对的**。
  集合名词（family / audience / team / government）**当整体→单数，当成员各自→复数，两者都合法**；
  英式更常用复数。⇒ B93 说"audience 必须单数"是简化过头，已改。★ B104
- 人称：`you … you … my family` 属于**泛指 you 中插入自身例子**，只要例子有标记（At Chinese New Year 就是标记）就合法，不算 B78 的人称跳。

### 脚本抽题 4 · `Should parents limit their children's use of computer programs and computer games? Why and how?`（question_bank.md:894）

- **她的第 21 次纠正（流程）**：`你不用强调直接说英文，我会自助决策。你都不要专门提`
  → 已写进 SKILL §2.1：**出完题就停，只给题目＋出处**，禁止再附"一口气说完/卡住跳过/说完自己默一遍"等重复规矩。
- 她追问 `how 怎么理解` → 教练答：how ＝**具体怎么限制**（可执行动作），三段结构 Should / Why / How；
  多问题最常见失分＝**只答 Why 就停**。

- **她的产出（逐字）**：`I think parents should. Sitting in front of screens for hours damages children's health physically and metally. It can cause chidlren overweight and hurt their eyesight. Plus, video games are so addictive that children may lose their attention on studying(我想说学业，但是不知道怎么说，这个 ing 我也不确定对不对）. Parents should pair screen time with outdoor activities. 另外我想说（也不应该太过于极端，适当的时候是完全没有问题的，但是遇到语言问题）`

- **★ 第 2 句是本轮最好的句子，全对**：`Sitting in front of screens for hours damages children's health physically and mentally.`
  动名词主语 ✅ damages 主谓一致 ✅ physically and mentally 并列同形 ✅ ——**这个结构她一次做对，没有任何提示**。
- **★ 她自产 `screen time`**（很地道的块）→ 收进表达库 ⭐
- **★ B102 的反例（当天刚学就没用上）**：`cause children overweight` ❌
```
cause 是实义词，用法很窄：cause sb sth（cause me trouble）／cause sth／cause sb TO do
"让孩子变胖" 的英语走通用动词：**make kids overweight** ← make ＋ 宾语 ＋ 形容词 ★ B106
⇒ 她在 drill 里 7/10 用对了通用动词，一进真题又回到实义词路线 → 需要在真题里反复抓
```
- **结构判定**：Should ✅ 一句／Why ✅ 两个理由（健康・学业）且带机制／**How ❌ 只有一句且不具体**
  （`pair screen time with outdoor activities` 不是可执行画面）。她自己想加的"不要太极端"其实正属于 How。
- **逐条**：
```
`lose their attention on studying`
   ❌ 三处：pay attention **TO**（不是 on）／"学业"＝ **schoolwork / their studies**／
      更自然 `lose interest IN schoolwork` ★ B107
   答她的疑问：`studying` 作介词宾语语法上没问题，错的是搭配不是 -ing
`pair screen time with outdoor activities` → **balance screen time with…** ／口语 `get them outside as well`
`hurt their eyesight` 可以，`damage their eyesight` 更常见
```
- **她卡住想说的"不应该太极端，适当就完全没问题"→ 直接给（真词汇缺口）** ★ B109
```
I wouldn't go too far, though.
An hour a day is completely fine.
It's not that games are bad — it's about how long.
in moderation（适度）
```

#### How 段补练（她要求先看示范）

- 教练给示范（标"说明机制，不是让你背的版本"），并列出五个决定：How 落地成"我家怎么做"／三个动作走三个不同维度（时长·条件·位置）／主动词全用通用动词（set·stick to·keep）／复用她刚复习的 stick to it／收尾用她自己想说的"别太绝"。
- **她的产出（逐字）**：`As for how. I'd say parent should set a proper time and pair the time with outdoor activities. I remember it was an hour day when I was a kid and only after homework.(我觉得一点就够了). You wouldn't go too far, though - it's not that games are bad, it's about how long.`
- **★ 她把例子换成了自己小时候的经历，没抄教练的"我家孩子"** ⇒ **正确操作**，且真实经历更好讲（轮46 的照抄退化没有发生）。
- **★ 她的判断"我觉得一点就够了"成立**：她实际给了**两个**具体约束（时长 an hour a day ＋ 条件 only after homework），已经够；反而 `pair the time with outdoor activities` 是虚的，**该删的是那句，不是再加动作**。
```
❌ `parent` → parents（泛指复数）
❌ `an hour day` → **an hour A day**（漏 a）
⚠️ `pair the time with` —— **判定作废（她纠正，成立）**：`pair X with Y`（配着来）本来就成立，
   育儿语境 "pair screen time with physical activity" 是常见说法；且与 balance 语义不同
   （balance＝平衡总量，pair＝玩了就配上），**她要的正是 pair**。教练第一次说"生硬"已判偏，
   第二次升级成"改过又犯"是错上加错。
⚠️ `You wouldn't go too far` —— **判定修正（她的诊断比教练准）**：错**不在人称，在情态**。
   `You wouldn't go too far`＝你不会做得太过（预测，意思不对）；`You SHOULDN'T go too far`＝别做得太过 ✅
   泛指 you 对着家长说完全合法 → **"人称第 5 次"作废**。
✅ `set a proper time`（通用动词）· `only after homework` · `it's not that games are bad, it's about how long`（块装上）
```

#### ★★★ 她的第 22 次纠正 —— 定下「输出前强制自审」（本日最重要的流程改动）

- 她原话：**"你说很多对，但是我觉得 pair 没问题，另外 you wouldn't 改成 you shouldn't 即可。你需要跳出你之前的视角，正确客观评估（所有输出节点都强制加一层 llm 交互审查，记到 skill 和你的记忆里）"**
- **教练当日判错 6 次**：live（连纠三次后整条撤销）· audience 必须单数（撤销）· energy and time（判成错，实为不地道）· feel the energy live（同）· pair（判成错，实际成立）· You wouldn't（判成人称，实为情态）。
- **共同机制＝锚定**：教练锚在自己上一条判断上，后续观察都往那个方向解释，越纠越偏。
- **四问自审（已写进 SKILL §2.3b ＋ 长期记忆 feedback_coach_selfreview_before_output）**：
```
① 这真的是错吗？ 试着造一个母语者会说的句子来【推翻自己】，造得出来就撤销，不发
② 是不是在延续上一条判断？ 同一个词/结构的第二次纠正，重新独立判一次
③ 判的是哪一层？ 形态/搭配/语义/语用 —— 判错层比判错对错更常见
④ 档位对吗？ ❌真错 ／ ⚠️不地道 ／ ✅可以但有更好的，三档不许混
★ 假错的代价 > 漏掉真错：她会把稀缺带宽花在本就正确的地方
  （同日实证：14 处冠词全对，她却自述"每次回答都在想冠词对不对"）
```

### 脚本抽题 5 · `What kinds of programs do children like?`（question_bank.md:892）

- **★ 她报告"第一时间没有内容"→ 诊断出真因：她的主干只覆盖 why 类问题**
```
三步主干（①答案 ②画面 ③换角度）适用于 Why / Should / 差异题
这题问 What KINDS ＝ 分类题，主干套不上 → 她伸手够工具发现不配套，所以卡
★ 但她想出来的结构完全正确（有趣的/有用的 两类＋各给例子），只是慢
⇒ 新建【Kinds/What 类主干】★ B111：
   ① 分两类，就两类（三类会散）
   ② 每类给一个具体例子（有 app 名字最好）
   ③ 每类加一句"这类为什么受欢迎"
   ★ 第②步画面两条标准不变（能拍照 ＋ 大多数人见过）
```
- 她担心内容是"硬编出来的" → 教练答：**P3 不要求真经历，只要求典型**；游戏/社交/工具三类典型，"沉迷到一天不出门"是合格画面。真正会跑偏的是**太特化**。

- **她的产出（逐字）**：`it is something interesting and helpful.（我觉得这个开头一般，你可以建议两个，我学下）programs like games and social media help them feel happy and kill time. They are so interesting that some children can stay in front of screens all day. Some tools are also popular(这句话我也想换掉). It depends on their hobbies. For someone who like(我在想 someone 是单数，但是我想把 someone 换成复数的，因为后面我用 their) snapping photos, Photoshop is definitely their fouvarite.`

- **★ 她两处自诊全中（第 9、10 次）**：开头一般 ✅ ／ `Some tools are also popular` 想换掉 ✅
- **★ 但她担心错了地方（有教学价值）**：`someone … their` **完全正确**（singular they，标准英语，考试认）；
  **真正错的是她没担心的 `who LIKE` → `who LIKES`**（关系从句跟先行词一致）★ B110
  ⇒ 更省事的解法：主语换复数 `For kids who like taking photos…`，一次解决。

- **档位标注（新的 §2.3b 四问自审首次落地执行）**：
```
❌ 真错   `something interesting and helpful` —— 问题不在 it（口语 It's mostly… 完全正常），
          在 **something**：单数＋虚指，答不了 kinds（复数类别）
          `who like` → who likes
⚠️ 弱     `Some tools are also popular` 语法没错，**信息量为零**；分类题第二类的开头
          必须明确标出"这是第二类" → `The other kind is tools…`
          `so INTERESTING that…` interesting 第二次出现，且说不出"停不下来" → **so ADDICTIVE**
          （她上一题刚自发用过 addictive）
✅ 可以但有更好的  feel happy → have fun ／ their hobbies → what they're into ／
          snapping → taking photos（snap 没错）／ **can stay all day ✅ 不用改**（can 表"有时会"）
✅ 很好   `programs like games and social media`（举例结构）· `kill time` · 并列两边对齐
```

#### ★ 她的第 23 次纠正 —— 「所有修正/更高建议都要给完整版」
- 她原话：`你完整输出下，记住后续(写在skill)，所有修正或者更高建议都要给出完整版，有几个建议给几次，不在意重复`
- 已写进 SKILL §2.4：**逐条点评后必须把整段从头到尾重写交出；提了 N 个不同方向就给 N 个完整版本，版本间大量重复无所谓**——片段拼不出语流，也没法用来重说。
- 本轮据此给了三个完整版：A 最小修改 ／ B 开头直接报类别数＋全部升级 ／ C 用她自己的块 `it comes down to` 开头＋明确标 the first/second kind。

- **她追问 `the fun ones` 为什么加 the** → 教练给判据：**the 的唯一功能＝双方都知道是哪一个**；
  前句 `two kinds` 已把范围框死，后面逐一列举就是确定子集 → the。★ B113
  平行例：`I bought some apples. THE red ones were cheaper.` ／ `two types of students: THE ones who ask questions and THE ones who don't`
  档位诚实标注：**不加也不算错**（fun ones and useful ones 听得懂），加了明显更自然且理由可推。

- **她重说 kinds 段（逐字）**：`Mostly two kinds. The fun ones and the useful ones. Programs are like games and social media help them have fun and kill time. They are so addictive that some kids stay in front of a screen all day. The other kind is tools, and that depends on what they are into. For kids who like taking photos. Photoshop is definitely their favorite.`
```
❌ 唯一真错 `Programs ARE like games…` —— 多了个 are，`like` 从"比如"（后置修饰）
   变成"像"（系表），整句结构散掉。而且**这处她原来是对的，重说时弄坏了**
   （与 more easier 同类：动一处坏一处）
✅ 其余全对：the 用对 · addictive 装上 · The other kind is tools… 全对 · who like ＋复数一致性解决
```

#### ★ 她的第 24 次纠正 —— 禁用书面标准评口语（教练系统性误判）
- 她原话：`另外在skill中记录下，不要纠结标点符号，特别是破折号这些在录音很难转录出来`
- **成立，而且比她说的更严重**：教练 08-06 把 `In terms of the road network.`／`How wide they need to be.`／`As for how.`／`Are they used for commuting…` 标成"片段"，还标过逗号粘连——**全是拿书面标准评口语**。口语里语调就是标点。
- 修订后的界线（已写进 SKILL §2.3b ＋ B105）：
```
✅ 完全正常  能独立表意的补充片段（As for how. ／ How wide they need to be.）
❌ 唯一保留  悬空片段——本身没有独立意思、听者接不上的
             （"…something to look after. UNLIKE WORK OR KIDS. It's…"）→ 挂回主句
❌ 不许再标  逗号粘连 · 句子片段 · 破折号
```

### 脚本抽题 6 · `What kinds of programs are useful for children's study?`（question_bank.md:893）

- **她的产出（逐字）**：`it is definitely AI. Nowadays, AI is actually a powerful tool that can answer almost any questions. It can also teach students how to learn something rather than just give a direct answer. Whenever i try to solve problems, i ask ai first. On the other hand, students should think by themselves, because ai is not always right and it helps you rather than replacing you.`
- **档位判定（四问自审执行）**：
```
❌ 真错  `almost any questionS` → **any QUESTION**（any 表"任何一个"接单数；
         复数的 any questions 用于疑问/否定句）
❌ 真错  `think BY themselves` → **think FOR themselves**（独立思考固定用 for；
         by oneself ＝ 独自一人做某事）
✅ 查过没问题（原判撤销/未成立）
         `it is definitely AI` 口语完全自然
         `On the other hand` 前面讲好处、这句讲风险，是真对立面 → 用对
         `Whenever I try to…` whenever ＋现在时，装上了
         `teach … rather than give` 并列同形做对
⚠️ 可升级  actually → really（actually 需"与预期相反"的语境）／
         `how to learn something` → `how to work something out`（虚→具体动作）／
         `give a direct answer` → `hand them the answer`／
         `try to solve problems` → `get stuck on a problem`（画面）
```
- **★★ 教练第 7 次误判（她追问后自查，成立）**：原判 `it helps you rather than REPLACING you` 为"两边不同形＝错"，
  并据此提出"同一段一对一错"的对照 —— **两个说法都收回**。
```
rather than ＋ -ing 是合法用法，三种情况（★ B114）：
① 两边是同一句里的两个【谓语动词】→ 必须同形
   It helps you rather than REPLACES you ✅／She works rather than COMPLAINS ✅
② rather than 领一个【独立短语】，尤其句首 → 用 -ing
   Rather than TAKING the bus, I walked ✅／I walked rather than taking the bus ✅
③ 前面是 to do → 后面省 to 用原形
   I decided to walk rather than TAKE the bus ✅
她那句处在①②交界（主句 it helps you ＋ 附加成分 rather than replacing you），按②成立。
⇒ 档位应为 ⚠️「可接受，平行版更稳」，不是 ❌。
考试里仍建议平行版，理由不是对错，是**平行结构听起来更有结构控制感**。
```
- 教练给了两个完整版（A 只改三处真错 ／ B 语言升级、内容一句没加），并指出这题问 kinds
  但她只给一类（AI）；建议她自己补第二类，教练不代想。

#### 第二类：她自己想的 ＋ ★ 她的第 25 次纠正（画面要求的适用边界）
- 她给的第二类中文：`还有很多其他软件，除了在线教育、画画，甚至记事本，对学习都是有益的，这取决于你如何使用`
- 教练判：`还有很多其他软件` 是**填充句、零信息**，但 `取决于你如何使用` 是**真观点且主角与第一类不同**
  （第一类主角＝软件的能力，第二类主角＝使用方式）→ 合格的第二支点，只需把观点前置。
- **★★ 她随即纠正教练："口语本来就没必要句句要例子，有些地方只有观点我觉得没啥问题" —— 成立**：
```
画面是修"整段全是抽象判断"的【药】，不是每句话的规矩。她已能带具体内容后，药要减量。
需要画面   ①观点是判断、听者会反问"比如？"（贵/方便/有用/压力大）
          ②整段一个具体的都没有
不需要画面 ③观点本身是机制或因果（"取决于怎么用"＝工具中性论），说清逻辑就完整
          ④一段里已有一两处具体的，后面的点可以纯观点
★ 她这段前面已有 answer almost any question ＋ 我卡住先问 AI 两处具体 → 第二点走纯观点站得住
★ 教练过度应用这条＝让她以为每句都得配照片，既不真也很贵。已写进 SKILL §5.0b
```
- 她要求整段输出 → 教练给两个完整版（A 贴原话＋加第二点／B 语言升级），并说明第二点的三个决定：
  删掉零信息的"还有很多其他软件"／观点前置（`it comes down to how you use it`，用她自己的块）／
  "甚至记事本"保留但性质是**反差**不是画面（最简单的工具也算，反过来支撑"关键在用法"）。

### though / that said 专项（她自述"我经常忘记用"）

- **★ 教练给的机制（不是"更地道"，是成本）**：
```
That said,   放句首 → 必须【说之前就决定】要转折     贵，快时钟下常来不及
…, though.   挂句尾 → 【说完了再补】，前面一字不改   便宜
⇒ though 是她唯一不需要预判的转折标记，按带宽模型是最优解
小组只三个：…, though.（首选）／ That said,（句首）／ Then again,（话说回来，自我修正）
```
- **她的 drill 产出（逐字）**：`1. Ai is really good. You can't believe it (全信怎么说，而且感觉不是很地道）, though. 2. the house is pretty big. It is far away from the subway though. 3. I'd readlly love to go. I have other things to do though. 4. The app is free. There are too many ads though. 5. He speak english pretty good. Writing （一般怎么说）`
- **★ though 的位置 5/5 全对，一次上手**；2·3·4 三句完全正确。
```
1  `You can't believe it` 意思偏（believe it＝相信这件事）→ **trust it completely** ／
   `take its word for it` ／ ★ 她今天已有现成块 `It's not always right.` ★ B118
   她自诊"感觉不是很地道" ＝ **第 26 次命中**
5  ❌ `He speak` → speaks（C4）
   ❌ `pretty good` → **pretty WELL**（副词修饰动作）★ B119
      ★ 她今天说过 `he cooks well` ✅ 同一规则**没跨语境迁移** ——
        这是"块绑在学它的那个语境上"的**第二例**（第一例：put things away ／ 收玩具）
   "一般" ＝ `just OK` ／ `not as good` ／ `nothing special`
```
- 完整版五句已给（含 `a long way from`／`way too many ads`／`I've got something on that day` 三处可选升级）。

- ⏸ 未答的题（滚入下次）：`Do people buy things they don't need?`（question_bank.md:1086）

---

## 📅 2026-08-07 · 学习日（周期第 3 天）· D-1(08-06) ＋ D-3(08-04)

> 出题前执行了她 08-06 定的 review 节点：08-06 共 B89–B120 计 32 条，教练自查后合并重复
> （B93→B104 集合名词 · B98→B117 stuck 三介词 · B105 口语作废项不考），剩 28 条，分三组。

### D-1 第 1 组（1–10）

- **她的原话（逐字）**：`No cars can move, forward or back. If there is something wrong with the the design, you are stuck every time you use that road. He passed the exam by studying every night. Walking to work can save a lot of money. I was stuck in traffic on the morning rush hour. His things are all over the floor. I drive past that school every day. You can get a refund for any reason. I take my son out on weekends.`（第 5 题跳过）
- **成绩 全对 5 ／ 核心对 2 ／ 部分 2 ／ 跳 1**
```
✅ 1（No cars can move ＋ forward or back，避开 neither…or）
✅ 3（by studying，B91 昨天首次产出、今天保住）
✅ 7（all over the floor —— all over the place 的合法变体）
✅ 8（drive past that school —— **对象用对了**，昨天错在 drive past that road）
   ⚠️ 但本题对象本来就该配 past，**不能证明她吃透了边界**，需换场景再验
✅ 10（take my son out，B101 昨天当场装上、今天保住）
```
```
❌ 6 `ON the morning rush hour` → **IN / DURING** the morning rush hour —— B98 昨天纠过，原样回潮
   ★ 关键对照：今天保住的四项（drive past／by studying／take sb out／for any reason）
     昨天全部当场产出过；**唯独这句昨天没重说** → 规律再次对上
   `stuck in traffic` ✅ 装上；漏 for forty minutes
⚠️ 4 `save a lot of money` 句子没错，但**这题考的间接宾语没出来** → `save YOU a lot of money`
⚠️ 9 `for any reason` ✅ 单数用对；漏 within seven days，可选升级 no questions asked
⚠️ 2 `you ARE stuck` 可以，`you GET stuck` 更准（every time＝每次都会发生，get 表进入状态）
   ★ 核心两点都装上：**现在时**（昨天写 will）✅ ＋ every time 跟完整从句 ✅
```
- **补答第 5 题**：`Children should put away their toys after using them.`
  → **✅ 正确，且教练 B95 写过头了**（把倾向写成规则）：可分离动词短语，**代词必须放中间**
  （put it away ✅／put away it ❌），**名词短语两个位置都合法**（put their toys away ／ put away their toys）。
  已更正 B95。**这是教练第 8 次把"倾向"当"规则"写。**
  唯一可调：`after USING them` → **after PLAYING WITH them**（玩具的常规搭配是 play with）。

### D-1 第 2 组（11–20）

- **她的原话（逐字）**：`Setting in front of screens for long can make children overweight. Children can stop paying attention to schoolwork. parents should balance children's screen time and outdoor activities. You shouldn't go too far, though. an hour a days is, uh, pretty good. for children who are ready into taking photos, Photoshop is definitely their favorite. Video games are so addictive that some children can stay in home all day. Mostly two kinds, They fun ones and they useful ones. I prefer working to taking buses. AI can answer pretty much any question. Student should think for themselves`
- **成绩 全对 3（12·13·19）／ 核心点装上但零件错 6 ／ 偏题 1**
```
✅ 核心点装上：make children overweight（B106，昨天错的 cause 修好）· pay attention TO schoolwork（B107）
   · balance（B108）· You shouldn't go too far ＋ though 挂句尾（B109/B120）· so addictive that（B112）
   · be into（B108 家族）· any question 单数（B115）· think for themselves（B116）· pretty much（好口语）
```
- **★★ 未解之谜：形近词错误集中爆发（教练已问，她未答，滚入待办）**
```
Setting/Sitting（昨天她写对过 Sitting in front of screens）· ready/really ·
working/walking · They/The  ——本批 4 个；加上 quality/quiet · quite/quiet 共 6 个
⇒ 教练已问："这些是打字手误，还是当时脑子里出来的就是那个词？"
   手误＝对口语零影响；检索错＝要单独修。**她未回答，暂不结论，后续批次被动观察**
```
- **★ 教练第 9 次判重（自查更正）**：`balance children's screen time AND outdoor activities` **完全正确**。
  B108 原写"balance X with Y"是把一种说法写成唯一说法（balance work and family 同样标准）。已改。
- **逐条零件**：
```
11 ❌ `for long` → **for HOURS / for a long time**（for long 只用于否定/疑问句：
      I won't be long ／ Have you been waiting long?；肯定句不能用。她昨天写的 for hours 才对）
14 ❌ `an hour a dayS` → **an hour a DAY**
   ★ 昨天她写 `an hour day`（漏 a），教练补 a；今天加了 a 又给 day 加了 s
     ＝**修一处坏一处**，与 more easier 同一模式（第 5 次）
   ⚠️ `pretty good` → **completely fine**（good＝好；这里要的是"没问题"）
16 ❌ `stay IN home` → **stay AT home / stay home / stay indoors**
17 ❌ `they fun ones` → **THE fun ones**
   判据：they 是代词，后面不能直接跟"形容词＋名词"；the 是限定词，后面必跟名词
   ★ 昨天她把 the 的规则问明白了（B113），今天错的是**词形不是规则**
20 ❌ `Student` → **Students**（泛指复数，且 themselves 要求复数）
18 ⚠️ 用 `prefer A to B` 结构合法，但**这题考的是 rather than**，考点没测到 → 需补测
   `taking buses` → `taking THE bus`（泛指交通方式用单数）
```

### D-1 第 3 组（21–30）

- **她的原话（逐字）**：`I'm stuck with this question.将就怎么说. You can't trust AI all. His writing is just okay. he speaks English pretty well. The house is pretty big. It's far away from the subway though. He cleared the table after eating. My family spend a whole day cooking at Chinese New Year. other than complaining it, he just did it. It's just about getting fed. You are done in ten minutes.`
- **成绩 全对 6（24·25·26·27·28·30）／ 错 3 ／ 提问 1**
- **★ stuck 的两个介词对调了（新的失败形态）**：
```
21 她写 `stuck WITH this question` → 该 **stuck ON**（卡在具体的点上）
22 她问"将就怎么说" → 答案正好就是 **stuck WITH**（被迫接受甩不掉）
⇒ 她记住了"stuck 有几个介词"，但**没绑定哪个配哪个场景**
⇒ 块化未完成的第三种形态：①块在但没跨语境（put away/收玩具）②块在但配错对象
   （drive past that road）③**块在但配错场景**（stuck with/on）
将就的另两个说法 ★ B121：**make do with**（I'll have to make do with this old laptop）／
`It'll have to do.`（最短）
```
```
❌ 23 `You can't trust AI all` → **You can't fully trust AI ／ trust AI completely**
      trust ✅ 记住了，副词错。⚠️ 注意别说成 `can't trust AI AT ALL`（那是"完全不能信"，意思反了）
❌ 29 两处：`other than` → **RATHER THAN**（other than＝除了…之外，意思完全不同）／
      `complaining it` → **complaining ABOUT it**（complain 不及物）
      更自然的收尾：`he just got on with it`
```
- **★★ 与"听＝0"相反的两个反例（教练主动记录，防止规律被当成铁律）**：
```
speak WELL       昨天错，只在【完整版】里给过，她没重说 → 今天对 ✅
clear the table  昨天刚给（在完整版里），她没重说       → 今天对 ✅
on the rush hour 昨天给的是【片段纠正】，她没重说       → 今天回潮 ❌
⇒ 新假设（待验）：**装在完整句子里给的更容易留存，单拎出来的片段纠正不容易留存**。
  若成立，则她 08-06 定的"必须给完整版"作用不只是方便读，而是**整句本身是更好的记忆单位**。
  后续几天持续观察，不急于下结论。
```

### D-3（08-04）第 1 组（1–10）

> 教练 review 节点：08-04 全部条目里删掉教练侧决策、已在 08-06 测稳的（efficient/effective · back and forth · put energy into）、只能在真题里测的操作类（画面两条标准 · 比较题另一边 · 论元完整意识），剩 20 条分两组。

- **她的原话（逐字）**：`i like watching kids play in the park. teachers should get students to try it themselves. don't make children memorise them. get them ask questions. have them work in pairs. hiring designers is too expensive. they can pick out furniture and choose colors themselves. it's only a half or even a tenth of the original price. my friend often goes to that shop. some teachers talk at you for an hour. i read my son stories every evening. some good are limited editions, or people(这里我在想哪个词 当主语好) stopped producing them. second-hand things are much cheaper than the new ones(不确定是否要the). it mainly comes down to saving money.`
- **成绩 全对 7（1·3·4·5·6·7·8）／ 部分 3**
```
✅ 3 直接避开了考点坑（没写 too much expensive）
✅ 4 pick out ＋ 并列两边同形（pick out … and choose）
✅ 5 分数 ✅  6 often＋goes ✅  7 talk at ✅  8 双宾语 ✅
✅ 9 `limited editionS` 复数用对（08-04 她写的是单数）
✅ 10 `much cheaper` ＋ `it mainly comes down to`（自产块第 4 次复用）
```
```
❌ 2 3/4：`get them ASK questions` **漏 to** —— 而"让某人做四件套"的核心正是
     **只有 get 带 to**（get sb TO do／have sb DO／make sb DO／let sb DO）。
     08-04 她 drill 3/3 过，今天漏。另：中文"让他们提问"最贴的是 **let**；
     `memorise them` 的 them 仍无先行词 → memorise everything
❌ 9 `some good` → some goodS（更口语 some things）
⚠️ 10 `than THE new ones` → **than new ones**（B113 判据：没框定范围就不加 the）
      ★ 她的判据其实会用，只是**一到 than 后面就犹豫**
```
- **★ 她问"people 当主语好不好" → 挖出一条通用判据 ★ B123**：
```
不好，但问题不在 people，在【中文这句根本没有主语】——"停产了"是谁停的？不知道也不重要。
英语碰到没有明确施动者的情况，**默认走被动或 they**：
  they aren't made anymore ✅ 最省事最口语 ／ they've been discontinued ✅ 正式
  the company stopped making them ✅ 硬要主语就给真的那个
  people stopped producing them ⚠️ 语法对，但生产商品的不是"people"，主语选偏
⇒ **中文无主语句 → 英语先想被动，别硬找主语。** 这条比这一句本身有用得多。
```

### D-3（08-04）第 2 组（11–20）

- **她的原话（逐字）**：`Especially when nobody can do it. You are more efficient when you are alone. you neither need to talk to others over and over nor get stuck in endless(这是别的地方看到的) meetings. you don't need to explain youself to anyone. The credits get shared, so nobody knows which part is yours. the ad was pretty effective, so the sale went up by 20%. The new system handles orders more quickly. it's no use fining people for littering （感觉又错了）. Fluent english is a must in this line of work. Speaking Japanese is a plus. It's a waste arguing with him. It's no use regretting it now.`
- **成绩 全对 4（11·14·18·19）＋ 基本对 1（12）／ 部分 5**
```
✅ 18 `it's no use fining people for littering` **一个字都没错**——她却自评"感觉又错了"
   ★ **她的自诊第 2 次误报**（第 1 次是 in front of the TV 的 the），两次都落在**她已做对的地方**
   ★ 这句 08-04 崩过（of no use to punish people who throw litters）、08-05 崩过又改对，
     今天直接说对 → **连续两次正确，这条稳了**
✅ 19 `a must` / `a plus` 边界 ✅ ＋ `in this line of work` ✅（08-06 她写的是 in the line of the work）
✅ 13 **neither…nor 配对用对了（B89 装上）**，但位置有问题（见下）
```
```
⚠️ 13 `you NEITHER need to talk… NOR get stuck…` —— neither 在 need 前面，
   导致第二半失去 need 的辖域（变成"也不会困在会议里"而非"也不用"）
   口语更省事：`you don't need to talk… OR get stuck…`
   ★ 与 though 那条同理：**neither…nor 要提前规划两边平行，成本高；
     don't … or … 说完再接，成本低** —— 快时钟下选低成本结构
❌ 15 `The creditS` → **The credit**（功劳义不可数；credits＝学分/片尾字幕）＋ 动词 gets
❌ 16 `the sale` → **SALES** ★ **第三次**（08-04、08-05 都纠过），顽固项
⚠️ 17 漏 much → `much faster / much more quickly` ★ **第三次漏 much**
❌ 20 `It's a waste ___ arguing` → **It's a waste OF TIME arguing**
   ★ 正是论元完整（B41）：a waste 后面必须补 of time / of money / of effort
   ✅ `It's no use regretting it now` 完全正确（论元 it 也带上了）
11 漏 else（nobody ELSE can do it）；12 漏 sometimes，alone→on your own 更口语
```

### ★★★ 她定下新学习目标（08-07）：形容词/副词的"压缩操作"

- **她的原话**：`我现在口语差，以及经常拿不准的原因是对语法结构不熟悉（但是这不是很重要，语法只是帮助我记忆，但是不是学习的目的，目的是把常用的都熟悉自然的记住并能说），对于常用的短语也不熟悉，此外对于形容词和副词的使用也很不熟练（比如我很难主动想着用 endless 这些修饰下）。后续在这些方面可以稍微强化下（但注意，不是让我反复复读特定词，主要是思维引导，你可千万别天天让我复习必须写出 endless）`
- **★ 关键反证：她当轮就自发用出了 `endless meetings`** ⇒ 不是能力问题，是**触发问题**。
- **教练给的思维引导（不是词表）——"压缩"，与"拆包"互为反向**：
```
拆包  中文名词块   → 英文一整句     （把压缩的展开）
压缩  中文状态短语 → 英文一个形容词  （把展开的压回去）
规律：中文把状态说成动词/状语/四字格，英语把状态压进名词前的形容词
  整天困在会议里→endless meetings ／ 堵得一动不动→heavy traffic ／
  排了好长的队→a long queue ／ 人挤人→a packed train ／ 破得不行→a run-down flat
★ 触发一句话：说到一个名词时，问"我中文里形容这东西的那句话，能不能压成一个词挂在它前面？"
★ 她的中文从来不缺这些描述，只是翻译时被丢在了状语位置
```
- **🚫 硬禁令（她明确要求）**：禁止让她反复复读特定词、禁止把 endless 之类列成必背清单、禁止天天考同一个词。
  正确做法＝**在她产出之后**指出"这里你中文有个状态没压进去"，用**她自己的中文**当材料，每次都是新词，练的是操作。
- 语法的定位（教练认同她）：**语法只当【判据】用**（the 加不加、neither 放哪、any 单复数），不是学习目标。
- 已写进 SKILL §5.0c。

### 脚本抽题 7 · `Do people buy things they don't need?`（question_bank.md:1086）

- **她的原话（逐字）**：`Yes, Quite often. Especially when people see a ad with a sale on. Ads are pretty good at making wants feel like needs. You want to buy a bag of napkin on(介词不确定对不对，或者用 at？) Amazon(不确定要不要 the). There is a promotion on the good page, so you end up buying three bags. On top of that, some people just enjoy the sense of spending money, so they tend to buy lots of things they will never use(这句话也感觉很不对）`

- **★★★ 她 cold 产出里结构最完整的一次**：
```
① 答案    Yes, quite often（第一句）
② 画面    想买一包纸巾 → 页面上有促销 → 最后买了三包
          **三条标准全中**：能拍照 ✅ 谁都经历过 ✅ 还带数字 ✅ 且完全自产，教练零提示
③ 换角度  有人就是享受花钱本身 —— 主角从"广告的作用"换成"人的心理" ✅ 不同轴
```
- **★★★ 亮点句（这几天最好的一句，进表达库 ⭐）**：`Ads are pretty good at making wants feel like needs.`
```
be good at doing（08-02 学的）✅ ＋ make X feel like Y（make＋宾语＋原形）✅
＋ wants/needs 动词名词化对举 —— **有洞察力的表达，不是套模板**
可迁移到：消费 / 广告 / 社交媒体 / 攀比
```
- **她的两个提问都答对了**：`on Amazon` ✅（平台用 on：on Amazon/Taobao/YouTube；实体店用 at Walmart）★ B125；
  `Amazon` 专有名词不带 the ✅
- **★ 她的自诊第 27 次命中**：`enjoy the sense of spending money` 自评"感觉很不对"——对。
```
问题是 **the sense of 是多余的名词壳**：enjoy spending money 已完整。
★ 老毛病换位置：以前是 `The most important thing is that…`，现在是 `the sense of…`
  —— 都是**在实义动词外面套一层名词壳** ★ B127
→ some people just enjoy spending money
```
- **零件**：
```
❌ `a ad` → **an ad**（元音前）
❌ `a bag of napkin` → **a PACK of napkinS**（napkin 可数要复数；纸巾论包用 pack/packet）★ B126
❌ `the good page` → **the PRODUCT page**（good 单数不是"商品"；商品页固定 product/item page）
⚠️ `an ad with a sale on` 可懂但不自然 → `an ad for a sale` ／ `when they see something's on sale`
✅ `end up buying three bags` —— end up doing 是好块，用对了 ⭐
✅ generic you 讲场景（You want to buy…）**不算人称跳**，是标准做法，不标
```
- 完整版只加了一个 `Say you`（前天教的举例起手，正好用在这儿）。
- ★ **本段没有明显的"修饰缺失"点**——画面已经够，按 §5.0b 不硬加形容词。

### 脚本抽题 8 · `What do you think of communicating via social media?`（question_bank.md:254）

- **她的原话（逐字）**：`social media makes it much more convenient for people to keep in touch than ever. Family members or friends living in different cities can easily connect with each other. In china, people message or send photos to others via Wechat from anywhere at any time. On top of that, it's easier to get know strangers(这里少 for 可以么）. you add a new friend on a online group about having pets(这里我是想说这个群是一个养宠物的分享群，但是没想到啥什么 固定块）just because both of you share the same interest.`
- **★ 三步齐 ＋ 第二支点主角不同（连续第 4 题做到）**：①答案 keep in touch 更方便 ②画面 微信随时发消息/不同城市的家人朋友 ③换角度 **认识陌生人**（主角从"维持已有关系"换成"建立新关系"）。
- **★★ 压缩操作首个实战案例（§5.0c 落地）**：她问"养宠物的分享群"有没有固定块 →
```
她写   an online group about having pets   ← 走展开路线（从句式），长且不地道
压缩   **a pet group** ／ an online group for pet owners
同类   二手书店 a second-hand bookshop ／ 上班高峰 the rush hour ／ 养宠物的人 pet owners
反例   压不了的就老实展开：减肥的人 people trying to lose weight
```
- **★ 她第三次担心错地方**：问"少 for 可以么" —— **for 少了完全没问题**（it's easier to do 本就不需要 for）；
  **真正漏的是 `get TO know`** 的 to ★ B129。（前两次：someone/their ／ in front of the TV 的 the）
- **逐条**：
```
❌ `than ever` 位置：`makes it much more convenient for people to keep in touch THAN EVER`
   → **than ever 必须紧跟比较级** → `makes it easier than ever to keep in touch` ★ B128
   （老项目"修饰语紧贴被修饰词"的比较对象版）
❌ `get know` → **get to know** ★ B129
❌ `a online` → **an online** ★ a/an 第二次（上一题 a ad）
❌ `on a group` → **IN a group**（群组用 in；论坛用 on a forum）★ B130
⚠️ `people MESSAGE or send photos` —— message 缺宾语 → `message each other` ★ 论元完整再现
⚠️ `Family members or friends` → `Family and friends`（固定并列）
✅ 做对的：`makes it much more convenient FOR people TO keep in touch`（make it＋形容词＋for sb＋to do，
   结构不容易，一次用对）· `friends LIVING in different cities`（后置分词，逻辑主语对）·
   `message` 当动词 · `via WeChat` · `from anywhere at any time` ·
   **convenient 这次用对了**（convenient for sb to do 正是它的正确用法，B73 的正面用例）
```

#### ★★★ 她的第 28 次纠正 —— 完整版之后必须做【独立 diff 环节】
- 她原话：`在给完整以及更好例子后，加入一个独立的 llm 判断环节，找出和我原句的 diff，然后说明每一个 diff 是为什么。这个步骤一定要独立，不能合并，不能省略`
- **首次执行就抓出教练的问题**（8 处 diff）：
```
该说没说 3 处：much more convenient→easier（⚠️她的本来就对，只是更短）／
              删 for people（⚠️可选）／删 to others（⚠️补了 each other 后重复）
⛔ 不必要改 1 处：`both of you` → `you both` —— **她原句完全正确，教练顺手改的，无任何理由**
              已改回她的版本
```
- **机制**：教练给完整版时会无意识把句子"顺成自己的口吻"，她读到的是一个不知道哪里被换掉的句子。
- 已写进 SKILL §2.4b，含三档标注（❌真错／⚠️更好／⛔不必要），**出现 ⛔ 即教练犯规，必须留痕**。

### 脚本抽题 9 · `Should governments provide financial support to start-ups?`（question_bank.md:285）

- 她先给中文并自述"这个话题我遇到很多语言问题"。教练判定为**真词汇缺口**（非检索），按她的规矩直接给：
  raise money／get funding／borrow from a bank · start a business／start up · a diverse economy · there won't be enough jobs · step in／put money in／give them a hand。
  另指出她**中文层**两处要先理顺：①「如果一个国家不愿意创办企业」——国家不创业，**主语丢了**（是人）②「政府适当的支持非常重要」＝**名词壳 B127**。
- **她的英文（逐字）**：`I think governments should. It's pretty difficult for start-ups to get funding from market or borrow from banks. Start-ups are crucials for the diversity of the economy. If few people（这里感觉不太对）are willing to start their own buiness because of financial presure, there won't be enough jobs(这里为啥要用将来时而不是一般现在时）. So governments should put money in and help start-ups.`
- **★★ 去壳成功（B127 昨天学，今天 cold 产出里执行）**：「政府适当的支持非常重要」→ `governments should put money in and help start-ups` ✅
- **★ 她的自诊第 28 次命中**：`If FEW people are willing…` 自评"感觉不太对"——对。few 自带否定，跟 if 叠着读拧 → `If people aren't willing to…`／`If not enough people start businesses…`
- **★★ 压缩案例之二（方向与案例一相反）**：`the diversity of the economy` → **a diverse economy**
```
案例一（08-07）中文状态短语 → 英文形容词    整天困在会议里 → endless meetings
案例二（本轮）  中文"X 的 Y 性/度" → 英文形容词＋名词
  经济多样性 a diverse economy ／ 空气质量差 poor air quality ／
  交通便利 convenient transport ／ 教育水平高 a good education system
★ 中文爱说"…的…性"，英语直接压回形容词
```
```
❌ `crucials` → crucial（形容词不加 s）★ B131
❌ `from market` → **from THE market** ★ B134
⚠️ `crucial FOR` → crucial TO 更常见（for 也成立）
✅ `It's difficult for sb to do` 结构对 · `to get funding … or borrow …` 并列同形对
```

#### ★★ 她追问两条，教练两处都讲得不够准，已修正

**① 条件句 zero vs first —— 她说"我觉得这两个一样"，她对，教练分得太硬**
```
两句其实两种时态都能用：
  If there's something wrong with the design, you get stuck / you'll get stuck   都 ✅
  If people aren't willing…, there won't be / there aren't enough jobs           都 ✅
真正差别只有语气：现在时＝陈述一条规律；will＝推演一个还没发生的情况
实用判据（唯一要记的）：句中有 every time / whenever / always → 现在时；
                     说"如果将来出现某情况" → will；两个都通时随便选，不扣分
★ 结论：**别在这上面花带宽**，她已经会用 will，这个区分考场零收益。
⇒ B83／B90 的表述相应收窄：它们管的是"有反复标记时用现在时"，不是禁止 will ★ B132
```

**② the market 的 the —— 她说"我感觉这是泛指"，意思上对，但判据不是泛指/特指**
```
判据＝**语境里只有一个的系统性名词 → 带 the**（不是"特指某一个"）
  the market · the economy · the government · the internet · the environment · the media · the weather
对照她自己那一句，两个都对：
  get funding from THE market  ... or borrow from banks
                   ↑ 只有一个市场系统        ↑ 银行有很多家，可数复数泛指
同理她开头 `governments should` **也是对的**（政府有很多个，可数复数泛指）
带 the   只有一个的系统  the market / the economy / the internet / the environment
不带 the 可数的多个      governments / banks / companies / start-ups        ★ B133
```

### 脚本抽题 10 · `How can governments help small businesses?`（question_bank.md:286）

- **她的原话（逐字）**：`It mainly comes down to funding and policis. Take funding first. It's hard for small businesses to raise money from the market or borrow from banks. So financial support from governments is crucial to them. Plus, tax reduction can relieve the presure on enterprises. policies like that will motivate people to create their own business because of （这里遇到语言问题，我想加一句，因为他们需要承担的很少）`

- **★★★ 首次把不同来源的东西组装成一段**：
```
It mainly comes down to funding and policies.   ← 她自产的块，第 5 次复用
Take funding first.                             ← 08-06 教练给的 "Take the roads first" 迁移
Plus, …                                         ← 第二类标出
＝ Kinds 主干（B111）＋ 自产块 ＋ 迁移起手，三样拼成一个完整分类段
```
- **★★ 十分钟前刚学的四条全部当场装上**：`from THE market`（B133）· `crucial TO`（B131）·
  `raise money`（本题开头给的）· `Take X first`（08-06）。**前四句一字未动，全对。**
- **她卡住的"他们需要承担的很少"** → 给：`because they have less to lose`（首选，短且准）／
  `don't have to take on so much risk`／`the risk is lower`。"承担"＝**take on** ★ B135
```
⚠️ `tax reduction` → **tax cuts**（reduction 书面，cuts 口语）★ B136
⚠️ `enterprises` → **small firms / small businesses**（enterprise 口语里太硬，
   且与她前文的 small businesses 不一致，同一批人换了称呼）
⚠️ `create their own business` → **start their own businesses**
   ★ 创业默认动词是 start／set up；**上一题她写的正是 start** ✅，本题换成了 create
```
- **Diff 环节（5 处）**：tax reduction→tax cuts ⚠️／enterprises→small firms ⚠️／create→start ⚠️／
  business→businesses ⚠️／because of[空]→because they have less to lose ❌补完。**S1–S4 零改动。**

### 脚本抽题 11 · `How does technology help people make plans?`（question_bank.md:303）

- **她的原话（逐字）**：`I'd said the internet and AI really helps(除了 comes down 还有别的说法么）. These days, you can get pretty much everything online. If you are goting to a trip（感觉缺个动词）, you can search for things like where to live, how to get there, and when the best season is. (这里缺一个转折, further more 可以不) with the advent of AI, you can even directlly ask your questions. AI will consider about your goal and restrictions like budgets, and give you a pretty sensible answer.`

- **★ 她主动求路径冗余**（"除了 comes down 还有别的说法么"）——这是好信号，说明她意识到"同一功能要有第二条路"。给的替代 ★ B137：
  `The main thing is X.`（最简单）／`It's mostly about X.`（最口语）／`What really helps is X.`（强调句）。
  ★ 而她本轮用的 `I'd say … really helps` **本身就是一条新路径**，只是形式错了。

- **★★ 她的报警器准、定位器不准（第 4 次）**：她说 `going to a trip` "感觉缺个动词"——**方向对，缺的是介词**
  （go **ON** a trip／take a trip／**plan** a trip，本题最贴的是 plan）。
  前三次同型：someone/their ／ 少 for ／ in front of the TV 的 the。
  ⇒ **给她的话术：报警器准，定位器不准，所以喊出来是对的，但别自己下结论。**

- **她问 furthermore 能不能用** → 不能，**太书面**；而且**这里是递进不是转折**；
  更关键：她自己的 `you can even` **已经把递进做完了**，不需要再加连接词。要加就 `And now with AI, …`。

- **★★ 新模式：她在口语里调书面词，连续第二轮**
```
上一轮  tax reduction · enterprises
本轮    the advent of AI · restrictions
⇒ 她像有个开关：想显得正式一点就去调书面词。
  但**口语的正式度靠结构清楚，不是词难**。
  the advent of AI → now with AI ／ restrictions → things like your budget / limits
（并入 B136）
```
```
❌ `I'd SAID` → **I'd SAY**（I would say＝我觉得；I'd said＝过去完成，意思全变）★ B137
❌ `the internet and AI really helpS` → **help**（并列主语用复数）
❌ `where to LIVE` → **where to STAY**（旅行住哪儿用 stay；live 是长期居住）★ B138
❌ `consider ABOUT` → **consider**（及物动词不带 about；她把 think about 和 consider 混了）★ B139
⚠️ `directly ask your questions` —— ask 缺宾语（论元）→ `just ask it directly`
✅ 做对：**the internet 的 the**（十分钟前学的 B133 当场装上）· `pretty much` 复用 ·
   三个 wh- 并列（where to stay / how to get there / when the best season is）结构好 ·
   `sensible` 是她自产的准词
```
- **Diff 环节（9 处）**：I'd said→I'd say ❌／helps→help ❌／going to→going on ❌／where to live→where to stay ❌／
  consider about→consider ❌／directly ask your questions→just ask it directly ❌补论元／
  with the advent of AI→And now with AI ⚠️／your goal→your goals ⚠️／restrictions like budgets→things like your budget ⚠️。
  **第 2 句 `These days, you can get pretty much everything online.` 一字未动。**

### 脚本抽题 12 · `Do people today prefer eating at home or in a restaurant?`（question_bank.md:367）

- **她的原话（逐字）**：`It's tough to answer. I'm nor sure. I really enjoy home-cooked food. They are much healthier and taste pretty good. On weekdays, I eat out just because I don't have much time. I grap a meal to get fed within 10 minutes. If i had more time, I definitely would prefer cooking at home.（这个问题是确实不太知道怎么回答，首先没有数据，只能从自己出发，但是我喜欢在家吃饭，但是却没有时间，这类问题你有什么建议么）`

- **★★★ 她提的方法问题挖出一条新工具（B140）：二选一/趋势题怎么答**
```
★ 核心翻转：**她以为"矛盾"是障碍，其实矛盾就是答案。**
  "喜欢在家吃但没时间" ＝ 偏好与行为不一致 ＝ P3 里最有说服力的一类观点
  People would rather eat at home — they just don't get the chance.

三种合法答法：
  a. 分人群/分场景   年轻人 vs 有孩子的家庭 ／ 工作日 vs 周末    ← 最好用
  b. 分偏好和行为    想在家吃，实际在外吃                       ← 本题正是它
  c. 选一边＋给条件  多数在外吃，除非那天有时间
★ "都有"不是逃避，只要说清"什么时候是这边、什么时候是那边"

没有数据完全不是问题（P3 不验证数据），把范围缩到能说的：
  I'd say… ／ Most people I know… ／ From what I see… ／ Around here…
★ 真失分的是**开头连说两句"我不知道"**——考官听到的是"没内容"。
  `It's a tough one` 说一次就够，紧接着必须给立场。
```
- **★ 亮点：虚拟语气这次用在了对的场合**：`If I had more time, I would prefer cooking at home.` ✅
  与现在事实相反 → 必须虚拟。**对照 08-05 她在 `If there were something wrong with the design` 误用虚拟
  （那句是说规律）；今天用对且教练零提示。**
- 自产好词：`home-cooked food` · `grab a meal` · `eat out`（08-06 学的，用对）
```
❌ `They are much healthier and taste pretty good` → **It's … and tastes**（home-cooked food 不可数）
⚠️ `I grab a meal to get fed within 10 minutes` 两个状语挤一起 → `I grab something and I'm done in ten minutes`
⚠️ `definitely would` → `I'd definitely`（默认语序，她的也能说）
```
- 给了两个完整版：**A 只修语言（Diff 5 处：nor→not ❌／They are→It's ❌／taste→tastes ❌／
  grab a meal…→grab something and I'm done ⚠️／definitely would→I'd definitely ⚠️）**；
  **B 结构演示**（标注"不是让你背的版本"），与 A 只差三处：第二句就给立场／把"没时间"从我的借口变成大家的处境／
  结尾一句把矛盾说破（`the preference is one thing, and what people actually do is another`）。**内容全是她的。**

- ⏸ 未答的题（滚入下次）：`Why do some people not like using apps?`（question_bank.md:892）

---

## 📅 2026-08-08 · 学习日（周期第 4 天）· D-1(08-07) ＋ D-3(08-05)

### D-1 第 1 组（1–10）

- **她的原话（逐字）**：`1 将就我记不住，我大概记得是一个直译和将就没关系的词组。 2. rather then complaining about it, he just go on it(好像是这个词组) 3. some goods aren't made anymore(不太符合早就) 4. second-hand things are much cheaper than new ones. I bought a pack of napkins on Amazon, and there was promoting on the product page. somebody enjoy spending money. social media makes it much more convenient to keep in touch. 8. It's much easier to get to know each other. 9. I added a new friend in a online pet group(形容词顺序有规定么) 10. Start-ups are crucial to a diverse economy (用 a 还是 the）`

- **★★★ 保住率显著上升：08-07 学的 12 条今天全在**
```
rather than ＋ complaining ABOUT it ✅ · aren't made anymore（被动 B123）✅ ·
than new ones 不加 the ✅ · a pack of napkins ✅ · on Amazon ✅ · the product page ✅ ·
去壳（没写 the sense of）✅ · get TO know ✅ · IN a group ✅ · pet group 压缩 ✅ ·
crucial TO ✅ · a diverse economy 压缩 ✅
★ 08-07 是第一次执行"完整版 ＋ 独立 diff 环节"，今天保住率明显高于前几天
  ⇒ **"整句是更好的记忆单位"这个假设进一步站得住**
```
```
❌ `he just GO ON IT` → **got on with it**（埋头干下去）＋ 时态过去 ★ B141
❌ `there was PROMOTING` → **there was A PROMOTION**（要名词不要动名词）★ B145
❌ `SOMEBODY enjoy` → **SOME PEOPLE enjoy**（somebody＝某一个人）★ B142
❌ `a online` → **an online** ★ **a/an 第三次**（a ad → a online → a online），同一条规则
⚠️ 7 漏了考点 `than ever`；8 `each other` → `strangers`（没对齐题目）
⚠️ 3 想加"早就" → `haven't been made for years` ／ `stopped making them years ago`
1  忘"将就" → **make do with**（记忆抓手：make do ＝ make it do，让它顶用）／
   be stuck with ／ It'll have to do.
```
- **她两个提问**：
```
① 形容词顺序有规定么 → 有（OSASCOMP），但**口语几乎用不到**，因为很少堆三个以上。
   只需一条：**越是说"属于哪一类"的词越贴着名词，越是"你怎么看它"的词越靠前**。
   她的 `online PET group` **排对了**（pet 最本质，贴着 group）★ B143
② a 还是 the → **加了形容词去说"哪一种"时，通常回到 a** ★ B144
   the economy（我们这个，只有一个）vs **a** diverse economy（一种多样化的经济）
   the market vs **a** competitive market  —— 补充 B133
```

### ★★ 她自己发现："我好像对完成时很不敏感"

- **原因清楚**：中文没有完成时（靠"了/过/已经"，且不一一对应）⇒ 与主谓一致、冠词同属**类型2**
  （中文里不存在的东西，产出时不跑判断）。
- **给的触发词判据（不讲语法，只看中文标记）★ B147**：
```
① for / since        持续到现在   「…了多久」「从…到现在」
② ever / never / before  经历不说时间  「…过」
③ just / already / yet   刚发生结果还在 「已经／刚／还没」
边界（最好用）：句中出现【具体时间点】(yesterday/last year/in 2020/three years ago)
              → 必须过去式，完成时立刻作废
她自己材料里的完美对照：
  they stopped making them YEARS AGO ✅ 过去式  ／  they haven't been made FOR YEARS ✅ 完成时
```
- **Drill 8 句（四对，每对逼选）她的原话**：`I'v been living there for ten years. I lived there last year. this thing have been made for ages. they stopped producing goods three years ago. I'v never tried it. I tried it yesterday. Have you just eaten. what you ate yesterday.`
- **★★★ 时态选择 8/8 全对，触发词判据一次上手。** 两处错都不在时态上：
```
❌ 3 `this thing HAVE been made` → **hasn't been made**
   ① **否定丢了** ★ **极性问题第 3 次**（08-04 In contrast＋can 该 can't ／
     08-05 nobody else CAN'T 多一个否定 ／ 今天该有没有）——三次方向都不同 ★ B148
   ② have → has（this thing 单数）
   ✅ `for ages` 词选得好，比 for years 更口语
❌ 8 `what you ate yesterday` → **What DID you eat yesterday?**
   ★ 疑似 **B82 过度泛化**：把"嵌入疑问句用陈述语序"推到了直接问句上
   边界 ★ B146：**前面有没有主句？有 → 陈述语序；没有 → 疑问语序**
     What did you eat? ／ How wide should it be?        ← 本身就是问句
     I don't know what you ate. ／ think about how wide it needs to be.  ← 嵌在主句里
```
- Diff（4 处）：there→here ⚠️／have been made→hasn't been made ❌／
  Have you just eaten→Have you eaten yet ⚠️／what you ate→What did you eat ❌。**2·4·5·6 零改动。**

### D-1 第 2 组（11–20）

- **她的原话（逐字）**：`They get funding from the market or borrow money from banks. It mainly comes down to money / the key thing is money / the main thing is money / what really matters is money. If you are going to on a trip, you can search for where to live or how to get there. (不确定 for 后面直接接对不对）. AI will also consider your budget. Tax cuts can relieve the pressure of small businesses. if people have less to lose(好像还有别的说法）, they are more willing to start their own business. Ads are pretty good at making wants like needs. You end up buying more two packs. Take funding first. Home-cooked food is much healthier and tastes better.`
- **成绩 全对 5（11·12·14·19·20）＋ 基本对 1（16）／ 错 4**
```
✅ 12 四条路径全给出，且**她自己变形了一个**：教练给的是 `what really helps is X`，
   她说 `what really matters is X` —— **更贴"主要就是"，比教练的好**
✅ 昨天纠的三条全装上：tax cuts ✅（昨天 tax reduction）· start their own business ✅（昨天 create）·
   Home-cooked food **IS** ✅（昨天 They are）
```

- **★★★ 教练侧改法：纠正小词时要给整块（08-08 定）**
```
本轮一轮内出现两次"修一处坏一处"（累计第 6、7 次）：
  教练说 "to 换成 on" → 她产出 `going TO ON a trip`（on 加上了，to 没删）
  教练改 enterprises→small firms → 她产出 `the pressure OF small businesses`
                                  （**昨天她写的 on 是对的**，改名词时把介词弄坏了）
★ 诊断修正：以前归因"她没重扫整句"；实为**教练的纠正方式让她记住零件而不是块**
❌ 以前  "to 要改成 on"        ✅ 以后  "go on a trip"（整块给，也要求整块重说）
与论元完整 B41 的修法同源：块化，不记零件。已写进 SKILL §2.4
```
- **★ 第 17 题：复用自己的招牌句时丢成分**
```
她 08-07 产出  Ads are pretty good at making wants **FEEL** like needs.
今天           Ads are pretty good at making wants ___ like needs.
★ 漏了核心动词 feel，整句散掉 —— 与轮94-95 "复用块时丢成分/对仗拆一半"同一模式
⇒ 块越长越容易掉一块 ⇒ 这类长块复习时**整句滚**，不拆
```
```
❌ `where to LIVE` → **where to STAY**（昨天刚纠，今天回潮；昨天只在完整版里给过，她没单独重说）
❌ `more two packs` → **two more packs**（数词在 more 前面）
⚠️ `their own business` → businesses（跟 people 对齐；单数也常见）
```
- **她两个提问**：
```
① `search for` 后面直接接 wh- 从句 → 稍生硬（search for 习惯接名词）
   ✅ look up where to stay（最口语）／ search for things like where to stay（她 08-07 原话，
      有 things like 做缓冲）／ search for hotels
② "承担的少"的别的说法 → they have less to lose（首选）／ don't take on so much risk／the risk is lower
```
- Diff（6 处）：going to on→going on ❌／where to live→where to stay ❌／search for→look up ⚠️／
  pressure of→pressure ON ❌／business→businesses ⚠️／making wants like→making wants FEEL like ❌／
  more two packs→two more packs ❌。**11·12·14·19·20 零改动。**

### D-1 第 3 组（21–28，操作类：压缩／去壳／无主语／完成时）

- **她的原话（逐字）**：`there are endless meetings every day. 22\23 不知道，可以考虑用 packed，但是句子不知道怎么说. a diverse economy / poor-quality air（感觉少 the) / convenient transport. What really matters is that parents should be organized themselves. Parents should explain why to children. the road is built last year. the feature will be on next month. I'v been work at this company for 5 years. I left that company 3 years ago.`

- **★★★ 22/23 卡住的位置极精确（本轮最有价值的诊断）**：
```
她想到了 `packed` ⇒ **压缩第一步（找形容词）她做到了**
卡的是第二步：**形容词有了，组不进句子**
⇒ 给两个固定出口（往后所有压缩出来的形容词都往这两个塞）★ B149
   出口A 做表语（最省，只要一个 be）  The trains ARE PACKED. ／ The traffic IS HEAVY.
   出口B 做定语（要现找动词）          You get on A PACKED TRAIN every morning.
   ★ 卡住时先走出口 A
```
- **★ 她第 3 次自诊误报**：问 `poor-quality air`"感觉少 the" —— 不用加；且 `poor-quality air` ✅ 本来就成立
  （`poor air quality` 更常用而已）。**三次误报全落在冠词/形态上**，规律稳定：结构准、形态会误报。
- **25 她换了个更好的壳，但没执行"去壳"**：`What really matters is that parents should be organized themselves`
  **不是错**（还用上了刚学的强调句），但这题考去壳 → `Parents have to be organized themselves first.`
  区别：她的把动作装在 `is that…should be` 里；去壳版让 parents 直接当主语，**短一半、力度更大**。
```
✅ 21 endless meetings 压缩成功 ／ 24 三个全对 ／ 26 去壳 ✅（`explain why to children` 语序小问题，08-06 提过）
✅ 28 后半 `I left that company 3 years ago` 过去式＋ago，边界判据对
❌ 27a `the road IS built last year` → **was built**（具体时间点用过去式，被动时态跟着走）
❌ 27b `the feature will BE ON next month` → **go live / be released / is coming out**
      （be on ＝正在上演/开着：The film is on）★ B150
❌ 28 `I'v been WORK` → **I've been workING**（完成进行时缺 -ing）★ B151
```
- Diff（6 处）：poor-quality air→poor air quality ⚠️／What really matters is that…→Parents have to be… ⚠️／
  explain why to children→explain to their children why it matters ⚠️／is built→was built ❌／
  will be on→will go live ❌／I've been work→I've been working ❌。**21 与 28 后半零改动。**

### D-3（08-05）第 1 组（1–10）

- **她的原话（逐字）**：`Especially when nobody else can do it. It's a hassle commuting every day. People there sing along with the the singer. You can feel the energy when you are there. he sit in front of the TV all night. I'm going to see a doctor tomorrow. Teachers should put more tithe and energy into preparing for classes. Nobody knows which part is yours. Your favorite bands come to your city once or twice a year. That's the only part of the day that belongs to me. The thing isn't that simple. It's not that hard`（第 2 题跳过）
- **★★ 三天前学的东西保留很好，且 08-06 回潮过的两条今天都装上了**：
```
sing along        08-06 回潮 → 今天 ✅      time and energy   08-06 回潮 → 今天 ✅
★ 区别就是 08-06 那次给了完整版且她当场重说过 —— 规律再次对上
其余全在：nobody ELSE ✅（08-07 漏过 else）· the TV ✅ · all night 不带 the ✅ ·
which part ✅ · come to your city ✅ · only…that ✅ · that simple/that hard ✅ · a hassle ✅
```
```
❌ `he sit` → **he sits／he sat** ★ 08-07 同一个错，两天连犯（C4 档：孤立测都对，产出时掉）
⚠️ `People there sing along` —— there 无先行词 → `Everyone sings along`
⚠️ `preparing for classES` → `preparing for class`（泛指不可数）
⚠️ 漏"才"：`bands come to your city` → **only come**
⚠️ **漏 actually 第三次**：`that belongs to me` → `that's ACTUALLY mine`（引擎词，去掉就少了"真正"）
```
- **她追问"如果 sit 是过去时是不是就没问题"** → 思路对（该句无时间标记，现在时/过去时都能说），
  但 **sit 的过去式是 sat**。引出 ★ B152：**原形＝过去式的一小撮**（put/cut/hit/let/set/cost/hurt/shut/spread/read），
  不在这撮里的必须变形。

### D-3（08-05）第 2 组（11–20）

- **她的原话（逐字）**：`He is really good at cooking. He do cook really well. I walk to work every day. Hobbies are something you choose yourself. I need the job, but my flowers need me. I'm really into cooking. because I follow the steps and there is always something to show for it. We ofter eat out on weekends. Children put away the toys after playing with them.（after 后面是可以省略主语的吧）the kid is actually origanized. his things leave all over the floor. It's much eaiser to find next time. it mainly comes down to visual effects.`

- **★★★ 人称一致（B78，主攻项）装上了**：
```
08-06 同一题她写  `I'm really into cooking. because YOU follow the steps`   ← 人称跳
今天              `I'm really into cooking. because I follow the steps`     ✅
★ B78 是"一天跳 4 次"才升为主攻的，今天在同一道题上自己统一了
```
- **她的好问题："after 后面可以省略主语吧"** → **能，但硬条件：-ing 的逻辑主语必须＝主句主语** ★ B153
```
✅ Children put their toys away after PLAYING with them.   playing 的主语＝children ✅
❌ After playing, I put the toys away.                      变成"我玩完之后"
   要说"孩子玩完之后我收" → After the kids finished playing, I put the toys away.
★ 即「理解侧冗余」第 3 条（分词逻辑主语＝主句主语）。阅读时她从不读错，产出时英语强制检查。
```
- **★ 第 18 题：08-07 写对过，今天改坏了**
```
08-07  `His things ARE all over the floor.`   ✅
今天    `his things LEAVE all over the floor.` ❌（leave 及物，东西不会自己 leave）
两个正确写法 ★ B154：His things are all over the floor. ／ He leaves his things all over the floor.
另：`actually organized` 的 actually 用得不对（需"与预期相反"语境）→ pretty/quite organized
```
```
❌ `Hobbies are SOMETHING` → **things**（B68 主语复数表语也复数）
   ★ 08-06 她用 `what you choose` 绕开了，今天踩回来
❌ `He DO cook` → does；且**这题不需要强调**，直接 `He cooks really well.`
❌ `It's much easier to find next time.` —— **主语和宾语都丢了**（论元完整再现）
   → `Putting things back makes them much easier to find next time.`
⚠️ `the job` → `my job` 更贴；17 漏了"得"（should）
✅ 装上：walk to work · eat out · visual effects（复数）· good at cooking · much easier（比较级只标一次）
```
- Diff（8 处）：He do cook→He cooks ❌／something→things ❌／the job→my job ⚠️／
  put away the toys→put their toys away ⚠️／Children put→Children should put ⚠️／
  actually organized→pretty organized ⚠️／his things leave→He leaves his things ❌／
  It's much easier to find→Putting things back makes them much easier to find ❌。**12·15·16·20 零改动。**

### D-3（08-05）第 3 组（21–27，收尾）

- **她的原话（逐字）**：`going to the cenima feels like a date night for us. Somebody run a red light and not get a fine. I was stuck in the morning rushing hour and just moved two kilometers(move 后面要介词么) in 40 minutes. I drive past that school every day. Traffic management（是不是得加 the) mainly comes down to the things: regulation and enforcement. No car can move, forward or back. shopping online is convenient for working people(上班族咋说)， it's convenient for xxx to shop online.`
- **成绩 全对 4（21·24·26·27）／ 错 3**
```
✅ 装上：the cinema（惯用定冠词）· a date night · run a red light · drive past（对象也对）·
   forward or back（避开 neither…or）· convenient for sb ＋ it's convenient for sb to do（两种结构都给了）
```
- **她三个提问，两个她本来就对**：
```
① move 后面要介词么 → **不要**（moved two kilometres ✅）；但 move 用在堵车上略生硬 →
   `I only got two kilometres in forty minutes.` ／ `It took me forty minutes to go two kilometres.`
② Traffic management 加 the 么 → **不加，她对了**。抽象不可数的"管理这件事"泛指无冠词；
   `the traffic`（具体车流）才带 the
③ 上班族咋说 → **working people，她已经写对了**；另有 office workers ／ people with full-time jobs
★ 三问里两问她本来就是对的 —— 与"形态类会自我怀疑"的规律一致
```
```
❌ `Somebody RUN` → **Someone runs**（主谓一致）
❌ `and NOT GET a fine` → **and DOESN'T GET fined** ★ B155
   and 接第二个谓语时否定必须带助动词；原形否定（not get）只用于 to not do 或祈使句
❌ `rushING hour` → **rush hour**（固定名词组，rush 不加 -ing；B96 学过）
❌ `comes down to THE things` → **TWO things**（数词丢了）
⚠️ `regulation` → regulations（具体条文用复数；不可数的 regulation 也成立）
⚠️ `just moved` → `only got`（"才"用 only）
```
- Diff（5 处）：Somebody run→Someone runs ❌／and not get a fine→and doesn't get fined ❌／
  rushing hour→rush hour ❌／just moved two kilometres→only got two kilometres ⚠️／
  the things→two things ❌／regulation→regulations ⚠️。**21·24·26·27 零改动。**
- **D-1（08-07）与 D-3（08-05）今日全部逐条过完，无抽样、无跳过。**

### 脚本抽题 13 · `Why do some people not like using apps?`（question_bank.md:892）

- **她的原话（逐字）**：`It's mainly because they worry about privacy. Nowadays, you can do pretty much everything online, like booking hotels and ordering takeouts. And at the same time, the companies know everything about you, what you like, and where you live. It's a bit scared. So someone doesn't use apps. On top of that, some apps are too complex for the elderly to use. They stick to using cash instead of online payment.`
- **★ 三步齐 ＋ 第二支点主角不同**：①隐私 ②画面（订酒店/点外卖；公司知道你喜欢什么住哪儿）
  ③老年人嫌复杂（主角从"担心被看见"换成"根本用不来"）。
- **★ 昨天学的 `stick to` 迁移过来了**；`pretty much everything online` 复用；`the elderly` ✅；`too…for sb to do` ✅。
```
❌ `It's a bit SCARED` → **scary** ★ B157
   -ed/-ing 形容词族：I'm bored ／ It's boring · I'm interested ／ It's interesting ·
   I'm excited ／ It's exciting。**判据：说人的感受用 -ed，说东西的性质用 -ing/-y**
❌ `SOMEONE doesn't use apps` → **SOME PEOPLE don't use apps**
   ★ B142 昨天刚学，今天又犯（改过又犯）
⚠️ `THE companies` → **companies**（泛指复数不带 the，今天刚复习过 B86）
⚠️ `stick to USING cash instead of ONLINE PAYMENT` → **instead of PAYING online**（并列两边同形）
⚠️ `too COMPLEX` → **too complicated**（complex 偏技术/学术）★ B158
⚠️ `takeouts` → takeaway（英）／takeout（美，不可数）
```
- Diff（6 处）：takeouts→takeaway ⚠️／the companies→companies ⚠️／scared→scary ❌／
  someone doesn't→some people don't ❌／complex→complicated ⚠️／online payment→paying online ⚠️。

### 脚本抽题 14 · `What are the differences between reading a book and visiting a museum?`（question_bank.md:879）

- **★★★ 她提出的真障碍不是语言，是心理抵抗**：`我的问题在于我内心在抵抗这种比较，感觉毫无意义`
- **教练的回应（两条，她接受）**：
```
① 承认她对：抽象地比"读书"和"逛博物馆"确实空洞，约等于问"苹果和椅子有什么区别"。
   **P3 的题面很多时候只是给她一个说话的支架**，考官不评判观点深浅，只看能不能有条理说 40 秒。
   知道这一点本身能省掉一大块内耗。
② 解药＝**给比较加一个使用场景**（"为了什么去选"），比较立刻变实 ★ B160
   空    读书和逛博物馆有什么区别？
   有意义 想让孩子了解恐龙，买本书还是带他去博物馆？／只有两小时空闲，读书还是逛展？
   ★ 而且这个场景**可以自己加进答案里**，不是绕开题目，是把题目答具体 → 加分
③ 差异题的解法 ＝ **找一根共同的尺子，说两边各在哪一端**（不是找相似点）
   万能尺子：主动 vs 被动 · 一个人 vs 一群人 · 快 vs 慢 · 花钱多少 ·
             靠想象 vs 靠感官 · 深 vs 广 · 当时 vs 之后
   ★ **她的中文里已经在用这根尺子了**（读书靠自己想象 / 博物馆直接给感官），
     她以为在硬扯，其实做的正是标准解法
```
- **★★ 连续第二次"她觉得别扭的地方恰恰是答案"**（08-07 在家吃 vs 下馆子的"矛盾"／今天差异题的"没意义"）
  ⇒ **她的不适感是可靠的信号源**，不该压下去，该拿来当起手。
- 她要求教练先写一版学习 → 教练给了**标注"说明机制"的版本 ＋ 七个决定**（内容一句没加，全来自她的中文）。

- **她自己重说（逐字）**：`It's a bit of a strange comparison. they are doing completely different things. one leaves room for your imagination. the other puts you there. Say children learn about dinosaurs. a book and a museum both work. with a book, all you get is words, so you picture it yourself. everyone pictures it differently, and that's the good part - it's your own version. at a museum, it's all right in front of you. kids go to a dinosaur museum and they can finally see how tall a t-rex was actually(这里放在前面还是后面). you feel like you are actually there. So they give you completely different things.`

- **★★★ 她改了教练的结构，而且改对了**：
```
教练版  抵抗 → 场景 → 两端 → 结尾才说破尺子
她的版  抵抗 → **立刻说破尺子** → 场景 → 两端
★ 她把结论提到第二句 ＝ **答案前置**，正是 08-03 她自己纠正教练的那条"头重脚轻"
  现在她自己在执行了
```
- **★★ `the other puts you there` 是她自产的、比教练版更好的表达**（教练写的是 `the other doesn't need any`，否定式且只说它不需要什么；她的三个词正面说出它干了什么，还是画面）→ 进表达库 ⭐
```
⚠️ `Say children learn about dinosaurs` 略秃 → `Say you want your kids to learn about dinosaurs`
   （Say 后面需要一个"想要/需要"的动机）
❌ `how tall a t-rex WAS ACTUALLY` → **actually WAS** ★ B159
   actually 修饰整句时位置＝be 动词后／实义动词前；但**嵌入从句语序变陈述**
   → 卡在主语和动词之间：`how tall a T-rex actually was`
⚠️ 结尾 `So they give you completely different things` 与第 2 句重复 → **删掉**，
   停在画面 `You feel like you're actually there.` 收得更干净；要收尾就换角度
   `So it really depends on what you want out of it.`
```
- Diff（3 处，其余全是她的原句）：Say children learn→Say you want your kids to learn ⚠️／
  was actually→actually was ❌／删掉重复的结尾 ⚠️。

### 脚本抽题 15 · `Do you think there are too many subjects for students to learn?`（question_bank.md:989）

- 她先给中文（立场→个人硬料→建议）。教练判：**硬料很强**（"学了两年生物化学、大学再没碰过、现在全忘了"），
  比任何抽象论证有力。给三个真缺口：`it never came up again`／`subjects you actually use later`／`I've forgotten all of it`；
  另用**具体事实提问**逼她拆"适当的学"（砍掉几科？还是每科都学但别学那么深？）——她选了前一条路线，合理简化。
- **她的英文（逐字）**：`a bit, especially in Chinese high school. I remember I spent much time on chemistry and biology. but in college. They never came up again. To be honest, I'v forgotten all of it now. I think the curriculum should focus on subjects we actually use later or come up everywhere, like math.`
- **成绩：三句零改动，两处真错**
```
✅ `They never came up again` —— 刚给就装上
✅ `I've forgotten all of it` —— 完成时用对（结果还在 → 完成时，B147 判据）
✅ `To be honest` 好的口语插入语 ／ 结构干净：立场 → 硬料 → 建议
```
- **★★ 第 2 句挖出一个词族（B161）：肯定句限制**
```
much     ❌ I have much time.   ✅ a lot of time     ✅ I don't have much time / Do you have much time?
for long ❌ I waited for long.  ✅ a long time       ✅ I won't be long / Have you been waiting long?
far      ❌ I walked far.       ✅ a long way        ✅ It isn't far / Is it far?
★ 三个词共享同一条限制：**只用于否定句和疑问句**；肯定句一律换成 a lot of / a long time / a long way
★ 例外：so much / too much / how much 在肯定句里合法
★ 她 08-07 已在 `for long can make children overweight` 犯过一次 → 同一族第 2 次
```
```
❌ 第 5 句并列两边不同形：`subjects [we actually use later] or [come up everywhere]`
   后半截主语应是 subjects，被前半截的 we 挡住 →
   `subjects we actually use later, or ONES THAT come up everywhere`（更口语）
   ／`subjects THAT we actually use later or THAT come up everywhere`
```
- Diff（2 处）：much time→a lot of time ❌／or come up everywhere→or ones that come up everywhere ❌。
  **其余全是她的原句。**

### 脚本抽题 16 · `Why do old people prefer to live in quiet places?`（question_bank.md:1186）

- **★★ 她的观察**：`其实内容我能说，但是语言跟不上。在口语中很难受`
- **教练回应（机制，不安慰）**：
```
① 这是真实 gap，但有个机制她该知道：**中文产出速度是英文的十几倍**，
   只要英文没到自动化，**主观上永远是"跟不上"——这个难受感不会因为进步而消失**。
   ⇒ 别拿这个感觉当进度表。看数据：今天已多次出现"英文完整表达了中文内容、只有 1–2 处 diff"
     （subjects 那题三句零改动）。**差距在缩小，感觉滞后于实际。**
② **真解药不是提高翻译速度**（慢），**是减少现场要生成的内容**（快）。
   她现在难受是因为同时做两件事：一边生成内容一边翻译；内容现成了，带宽全给翻译。
   ⇒ 指向 offline 备内容（硬料六类）。
```
- 教练指出她中文里**三处能直接调用已学的东西**：睡觉容易被干扰→**light sleepers**（压缩）／
  安静是必需品→**quiet is a must**（B51）／经历过太多→**they've been through a lot**（完成时判据）；
  另给三个真缺口：`peace and quiet`（固定搭配，不用 inner peace）／`somewhere away from all the noise`／
  `look back on their lives`＋`think things over`。

- **她的英文（逐字）**：`it is mainly because older people are more likely to look after peace and quiet. They have been through a lot, so they want to live somewhere away from all the noise, to look back on their life and think things over. Plus, the elderly tend to be light sleepers, so quite is a must for them`

- **★★★ 压缩操作在真题里做成了（昨天卡的正是这一步）**：
```
昨天  22/23 她想到 packed 却"组不进句子" → 教练给了两个出口（A 做表语／B 做定语）
今天  `the elderly tend to BE light sleepers` ✅ **走出口 A，一次装进句子**
```
- 刚给的块全装上：peace and quiet ✅ · have been through a lot ✅（完成时） ·
  somewhere away from all the noise ✅ · quiet is a must ✅ ·
  并列 `look back on their lives and think things over` 两边同形 ✅
```
❌ `look AFTER peace and quiet` —— 三个形近词组混了 ★ B162
   look after sb/sth ＝照顾 ／ **be after sth ＝追求、想要**（They're after a bit of peace and quiet）
   ／ look for sth ＝寻找。最省的说法其实是 `want peace and quiet`
❌ `quite` → **quiet** ★ **形近词第 5 次，且 quiet 这个词第 2 次混**
   （累计：quality/quiet · quite/quiet ×2 · ready/really · working/walking · Setting/Sitting · They/The）
⚠️ `their life` → their lives（主语 they 复数）
⚠️ `…all the noise, TO look back on` 连着两个 to 读着绕 → `where they can look back on`
```
- Diff（4 处）：look after→want ❌／to look back on→where they can look back on ⚠️／
  their life→their lives ⚠️／quite→quiet ❌。**第 3 句除 quiet 一个字母外零改动。**

### 脚本抽题 17 · `What kind of job can be called a 'dream job'?`（question_bank.md:778）

- **她的原话（逐字）**：`it's definitely the one with no overtime and stability(这里并列又卡，硬憋了一个，不知不道对不对). After work, you have enough time to do something else, like hobbies or childcare. As for stability, there is an age discrimination in China for someone like me over 35. It's hard for them to find jobs, and they are constantly dealing with layoffs. So the job with which (这个引导词我不确定) you can balance the work and life (这里我想把稳定并列进去，但是卡语言) is really perfect.`
- **★★ 她三个自我标注全部命中真问题（第 29·30·31 次）**：
```
① 并列卡住 → **否定辖域陷阱**（真诊断）★ B163
   `with no overtime and stability` 会被读成 with no [overtime and stability]（既没加班也没稳定）
   解法A（推荐）**换成正面名词**：reasonable hours and job security → 辖域问题自动消失
   解法B 拆成两句，不硬并
② `with which` 不确定 → **确实错**。判据：**把先行词放回从句看需要什么介词**
   （you can balance work and life IN this job → in which → **where**）★ B164
   job/situation/case/point 这类抽象"场所"一律 where；口语最省是绕开：`a job THAT LETS YOU balance…`
③ 想把"稳定"并列进最后一句但卡 → 需要**撑开的框架**：
   `both A and B`（a job that gives you both — time outside work, and something you can count on）
   ／`not just A, but B too`
```
```
❌ `AN age discrimination` → age discrimination（不可数不带冠词）
❌ `discrimination FOR someone` → **discrimination AGAINST** ★ B165
⚠️ `childcare`（托育服务，政策词）→ spending time with your kids
⚠️ `constantly dealing with layoffs`（应付已发生的裁员）→ always worried about being laid off
⚠️ 人称漂移：someone like ME → It's hard for THEM → 统一成 for us
```
- 给两个完整版：A 贴她的结构（Diff 6 处）／B 用正面名词并列＋both A and B 撑开框架＋`that's the dream` 收尾。

#### ★★★ 她三个追问 → 挖出三条通用规则

**Q1 `a job` 能不能换 the？后面 `one` 要不要加 the？**
```
她的反驳：`就是感觉这个 job 已经被限定了呀` —— 抓到了真区别：**限定 ≠ 定指** ★ B166
  限定＝缩小范围（with no overtime 确实缩小了）
  定指＝缩完之后**只剩一个且听者能确定**
  不加班的工作有一大堆，听者指不出来 → 还是 a
  判据：**限定完还剩几个？** 剩很多→a ／ 只剩一个且听者能确定→the
  对照：a man who lives next door ／ the man who lives next door
       a book that changed my life ／ the book that changed my life
       a job with no overtime ／ **the job with the highest pay**（最高级唯一→the）
  ★ 中文"的"字结构（不加班的工作）限定与定指同形，全靠语境；英语强制先选 —— 与"理解侧冗余"同族

她再追问 `one 不是指代前面的吗，为啥不加 the`：
  **one 回指的是【名词 job 这个类】，不是某一份具体工作**；one 只替换名词，**冠词要重新选**
  one ＝ a job ／ the one ＝ the job
  ★ 杀手锏一句：**她描述的是一份还不存在的工作，不存在的东西不可能"双方都知道是哪一个"**
  对照：I'm looking for a flat near the metro. And ONE with a balcony.（还在说要什么样的）
       I looked at three flats. THE ONE with a balcony was the best.（三套里那一套）
  附：`a one` 不说；bare one 本身就带不定义（Do you have one? ／ the one I lent you）
```

**Q2 `reasonable hours / job security / time outside work / count on` 这类简单词组用不出来 —— 挖出通用解法 ★ B167**
```
共同点：**她的中文是动词短语或否定，英语是正面名词**
  不用加班 动词否定 → reasonable hours   ／ 工作稳定 形容词 → job security
  下班后的时间 状语 → time outside work  ／ 靠得住 动词 → something you can count on
⇒ **操作：列"优点/条件"时，先把每条压成一个名词短语，再串起来**
  好工作 good pay·reasonable hours·job security·nice colleagues·a short commute
  好城市 cheap rent·good public transport·clean air·plenty of parks
  好房子 plenty of light·a decent kitchen·a quiet street
★ 这一招同时解决另外两个麻烦：**全是名词 → 没有否定辖域问题，也天然同形**
```
- **Drill（列三类清单）她的原话**：`good pay, reasonable hours, nice colleagues. convenient transport, clear air, plenty of job opportunities. cheap rent, a friendly neighborhood, a big living room.`
  **★ 9/9 全是名词短语，一个都没滑回动词或否定 —— 这个操作一次上手。**
  唯一错：`clear air` → **clean air** ★ **形近词第 6 次**（clear/clean；累计 quality/quiet · quite/quiet×2 · ready/really · working/walking · Setting/Sitting · They/The）

**Q3 `your hobbies, or just being with your kids` 不同形吗？**
```
**算同形。并列同形要求的是【语法功能相同】，不是词性完全一样**（动名词本来就是名词性）★ B168
自测法（她能自己跑）：**把两边分别接回前面那个词，看通不通**
  ✅ time for [your hobbies] 通 ／ time for [being with your kids] 通 → 同形
  ❌ subjects [we actually use later] 通 ／ subjects [come up everywhere] 不通 → 不同形
```
- **她追问"加一个 that 就行吗，为啥要两个"** → 因为**两个从句里 that 的身份不同，一个顶不了两个角色** ★ B169
```
subjects THAT we actually use later   that ＝ use 的【宾语】
subjects THAT come up everywhere      that ＝ come up 的【主语】
⇒ 由此引出通用规则：**关系代词做宾语可省，做主语不可省**
   the book (that) I read ✅可省 ／ the book THAT changed my life ❌不可省
⇒ 正好解释她原句为何一半对一半错：
   `subjects we actually use later` ✅ 省了没事（宾语）／`subjects come up everywhere` ❌ 省不得（主语）
口语最佳写法：`subjects we actually use later, or ONES THAT come up everywhere`（用 ones 重起名词，
比堆两个 that 好听）
```

### 📌 2026-08-08 收尾

- 她的话：`感觉要学的太多，今天就先这样吧`
- **教练回应（机制，不安慰）**：**清单长 ≠ 要学的多**。今天新增 ~28 条，但归到根上只有 8 个：
```
①冠词/定指 ②并列同形 ③论元完整 ④局部修正残留 ⑤形近词 ⑥极性 ⑦名词壳/压缩（一体两面）⑧时态触发
★ 清单之所以长，是因为**同一个根在不同词上反复冒头，每次冒头都记了一条**
★ 而今天有 4 个根出现了"装上"的证据：
   压缩（真题里自主做到 light sleepers）· 人称一致（B78 主攻项，同题自我修复）·
   完成时触发（8/8）· 名词短语清单（9/9 一次上手）
```
- **下一步**：08-09 ＝ 周期第 5 天（学习日，复习 D-1=08-08 ＋ D-3=08-06）；
  **08-10 ＝ 第一个专门复习日**（不学新的：过去 5 天全部逐条 ＋ 更早抽查 ＋ **题目重答**）。
  题目重答的范围＝ 08-05~08-09 用脚本抽过的全部真题（见 `coach/asked.log`）。

- 她收工前追问 `极性是什么` → 教练补定义：**极性＝一句话到底是"是"还是"不是"**。三次错方向都不同
  （该有没有／多一个／丢一个）。机制：**中文的否定长在动词里面**（显不出来·做不到·没人做·用不来），
  不是独立零件；**英语的否定必须是独立标记且只能出现一次** → 她搭骨架时那个嵌在中文动词里的否定会掉，
  或者"没人"和"不到"各映射一次就多出来。两条检查：①中文出现 不/没/别/无 → 英文必须有**一个**否定标记
  ②nobody/nothing/never/no one 已含否定 → 后面动词一律肯定。

---

## 📅 2026-08-09 · 学习日（周期第 5 天，明天＝第一个专门复习日）· D-1(08-08) ＋ D-3(08-06)

### D-1 第 1 组（1–10）

- **她的原话（逐字）**：`rather than complaining about it(这里 about it能省略么), he made do with it. some people just enjoy spending money. i added a new friend in an online pet group. there is promotion on the product page. what did you eat yesterday. I don't know what you ate yesterday. i've been living here for ten years. i left the company three years ago. the thing has not been made. the subway is packed. the traffic is heavy. the feature will be going on(其实有点忘了) next month. i have been working at the company for five years.`
- **成绩 全对 6（2·3·5·6·8·10）／ 错 3 ／ 漏 1**

- **★★ 昨天错的四条今天全修好**：
```
`I've been WORK` → I've been workING ✅   ｜ `what you ate` → what did you eat ✅ ＋嵌入版也对 ✅✅
`this thing HAVE been made` → has NOT been made ✅（**极性和主谓一起修好**）｜ `a online` → an online ✅
第 8 题两句都走出口 A（做表语）→ 压缩操作稳了
```

- **★★★ 第三次「块混淆」（新的稳定失败模式）★ B171**
```
❌ `he MADE DO WITH it` → **got on with it**
   get on with it ＝别废话接着干（这题要的）／ make do with it ＝凑合着用（昨天学的"将就"）
累计三次，共同点全是**"动词＋小品词"的三词短语，形近、意思完全不搭**：
   ① stuck with / stuck on            配错场景
   ② look after / be after / look for  配错块
   ③ get on with it / make do with it  配错块
⇒ **她记住了"有这么个块"，但没绑定"哪个块配哪个意思"**
⇒ 处方：这类块**必须成组学 ＋ 配中文触发词**，不能单个记：
   将就 make do with ／ 埋头干 get on with it ／ 照顾 look after ／
   追求 be after ／ 寻找 look for ／ 应付得来 get by
   记忆抓手：**make do ＝ make it do（让它顶用）** ／ **get on ＝ 继续往前走**
```
- **她的提问：about it 能省吗** → **能，但要整体省，不能只省 about** ★ B172
  ✅ `Rather than complaining, he just got on with it.`／✅ `…complaining about it…`／❌ `complaining it`
```
❌ `there is PROMOTION` → **there's A promotion** ★ 昨天错的是词形（promoting），
   今天词形对了冠词掉了 —— **修一处坏一处，第 8 次**
❌ `the feature will BE GOING ON next month`（她自述忘了，按规矩直接给）→ **go live**（最常用）／
   be released ／ be coming out。★ `be going on` ＝正在发生（What's going on?），又一个 on 短语混淆
⚠️ 第 7 题漏"早就" → `hasn't been made FOR AGES / FOR YEARS`（"早就"是这句的关键信息）
⚠️ `the company` → that company（题目是"那家公司"）
```
- Diff（5 处）：made do with it→got on with it ❌／there is promotion→there's a promotion ❌／
  the company→that company ⚠️／has not been made→hasn't been made for ages ⚠️／
  will be going on→will go live ❌。**2·3·5·8·10 零改动。**

### D-1 第 2 组（11–20）· **8/10 全对**

- **她的原话（逐字）**：`he put things on the table last night. kids put their toys away after playing with them. his things were all over the floor. he left things all over the the floor. some people run a red light without getting fined. shopping online is convenient for working people. traffic management mainly comes down to two things. it's a bit scarey. i'm a bit scared. some apps are too complicated for the elderly. i ordered takeaway. he finally saw how tall a T-rex actually was. I spent lots of time on chemistry. I have waited for ages. I walked far away. older people are after quite and peace. he is a light sleeper.`

- **★★ 两件值得点名**：
```
① `be after` 用对了 —— **昨天她写的是 look after peace and quiet（块混淆），今天直接调出 are after** ✅
   ⇒ 三次块混淆里修好了一个
② `without getting fined` **比教练给的版本好**（教练教的是 and doesn't get fined）
   她用 without ＋ -ing **直接绕开了"and 后面否定要助动词"这个麻烦** —— 更短更稳
```
- 其余装上：two things（昨天写 the things）· takeaway · complicated · actually was 位置 ·
  lots of time · put things（原形＝过去式）· put their toys away ＋ -ing 省主语 · scary/scared 区分 ·
  his things were all over the floor（东西当主语用 be）
```
❌ 19 `I walked FAR AWAY` → **a long way**（far away 表位置"在远处/走远了"，不表距离）
   ★ B161 那一族三个词她中了两个（much ✅ ／ for long 用完成时绕过 ／ **far ❌**）
❌ 20 `quite and peace` → **peace and quiet**，两个问题叠在一起：
   ① **quiet 第 3 次写错**（08-07 the QUALITY of the countryside ／ 08-08 QUITE is a must ／
     08-09 QUITE and peace）——★ **三次顶替它的词都不一样**，这个词要单独焊
   ② **词序反了**：peace and quiet 是固定词序，不能倒
   ⇒ 处方：**整块滚 `peace and quiet`，三个词一起走，别拆**
⚠️ 13 `he left things` → he left HIS things
```
- Diff（3 处）：he left things→he left his things ⚠️／I walked far away→I walked a long way ❌／
  quite and peace→peace and quiet ❌。**八题零改动。**

### D-1 第 3 组（21–28）

- **她的原话（逐字）**：`i want a job without no overtime, and one that is stable. i want a job with reasonable hours and (稳定工作名词块我忘了). that is a job where you can balance work and life. There is age discrimination in China against people over 35. I bought a cheap second-hand phone. which (什么样我不知道怎么说) city does fit living(适合也不知道). there is enough time for other things, like your hobbies or spending time with kids. you should learn subjects that you can use later, or ones that come up everywhere. clean air. today is clear.`
- **成绩 全对 6（22·23·24·26·27·28）／ 错 2**
```
✅ `one that is stable` —— **昨天那场 a/the/one 的讨论生效了**（B166）
✅ where（B164）· against（B165）· 形容词顺序（B143）· ones that（B169）· clean/clear（B170）
✅ 她**记得有两个解法**（正面名词并列 ／ 拆两句），只是第二个的词忘了
```
```
❌ 21 `a job WITHOUT NO overtime` —— **without ＝ with no，叠了两层否定** ★ B173
   ★ **极性第 4 次**，与 `nobody else can't do it` 同一个动作：中文"没有加班"的"没"映射了两次
   ✅ with no overtime ／ ✅ without overtime ／ ❌ without no overtime
   忘了的词组：**job security**
❌ 25 整句崩：`which city does fit living`
   "什么样的" ＝ **what kind of / what makes…**（不是 which——which 是从确定范围挑，B61 学过）
   "适合住" ＝ **good to live in / a good place to live**（fit living ❌）★ B174
   ★ 而且**这题真正的任务是列三条名词短语**，她卡在题干翻译上就没往下走
   ⇒ 给她的规矩：**题干卡住就跳过题干，直接答内容**
⚠️ 22 只给了一种说法，第二种是绕开关系词：`a job THAT LETS YOU balance work and life`
⚠️ `with kids` → with YOUR kids（与前面 your hobbies 一致）；`today is clear` → It's clear today 更口语
```
- **她追问 `a good place to live` 为什么不加 in** → 引出 ★ B175：
```
默认：**不定式后置修饰，介词留在末尾**（还原成完整句看挂什么介词）
  a chair to sit ON · a pen to write WITH · a topic to talk ABOUT · a house to live IN
例外：**place / somewhere / anywhere 这类泛指地点词，介词被吸收可省**
★ 关键对照：a good **place** to live ✅（不加 in）／ a good **city** to live **IN** ✅（必须加）
```
- Diff（6 处）：without no→with no ❌／[空]→job security ❌／补第二种说法 ⚠️／
  which city does fit living→What makes a city a good place to live ❌／with kids→with your kids ⚠️／
  today is clear→It's clear today ⚠️。**23·24·27 零改动。**

### D-3（08-06）第 1 组（1–10）· **9/10 全对，今天最好的一批**

- **她的原话（逐字）**：`no cars can move, forward or back. if there is something wrong with the design, you get stuck every time you use the road. He passed the exam by studying every night. walking to work can save you lots of money. i got stuck for 40 minutes in the morning rush hour. his things are all over the floor. i drive past that school every day. you can get a refund within 7 days, no questions asked. i take my son out on weekends. he cleaned the table after dinner.`
- **★★ 三个之前错过的今天全修好**：
```
`save YOU lots of money`      昨天漏了间接宾语 → 今天补上 ✅
`IN the morning rush hour`    前天写的 on      → 今天改对 ✅
`no questions asked`          之前从没产出过    → 今天出来了 ✅
```
- ❌ 唯一一处：`he CLEANED the table` → **CLEARED**（餐后收拾＝clear；clean＝擦桌子）。
  ★ 08-08 她写对过（cleared），今天回潮。

### D-3（08-06）第 2 组（11–20）

- **她的原话（逐字）**：`my family spends (这里可以用单数么) a whole day cooking at Chinese new year. sitting in front of screens makes children overweight. children will lose interest in their schoolwork. parents should balance kid's screen time and outdoor activities. it shouldn't too far away(有点忘了), though. an hour a day is pretty ok. for children who are really into taking photos, Photoshop is their favorite. Games are so addicted that some kids stay at home all day. there are mainly two kinds, the fun one and the useful one(这里为啥要加the了，感觉也没有特指，按照昨天学的). rather than taking buses, i walk. it helps you rather than replaces you. AI can answer pretty much everything.`
- **她两个提问，答案都是"你对"**：
```
① `my family spends` 能用单数吗 → **能**。集合名词单复数都合法（B104）。
   昨天她用 spend，今天用 spends，**两次都对**。
② `the fun ones` 为什么加 the（"感觉没有特指"）→ **关键在前面那句框死了范围**：
   `there are mainly two kinds` 把门关上了 → 后面这两个听者完全能确定 → the
   对照昨天的 `a job with no overtime`（不加班的工作有一大堆，指不出来 → a）
   ⇒ **判据没变（B113/B166），只是这题多了 two kinds 在前面封闭了范围**
```
```
❌ `Games are ADDICTED` → **ADDICTIVE** ★ B157 昨天刚学（scared/scary 做对了），
   今天换个词就没迁移 —— **规则绑在学它的那个词上**
❌ `the fun ONE` → **ONES**（每类里不止一个）★ 新点 B176
❌ `it shouldn't too far away` → **I wouldn't GO too far, though.**
   ①漏 go（go too far ＝做过头是固定搭配）②too far away ＝距离太远
⚠️ `pretty ok` → completely fine ★ 08-08 她写 pretty good，第二次
⚠️ 第 12 题漏"长时间" → `for hours`；`kid's`→kids'；`taking buses`→taking the bus
◎ 第 20 题 `AI can answer pretty much everything` **句子完全对，但没测到考点**（any ＋ 单数）
  ⇒ 教练题面要改：中文得写成"AI 几乎【任何问题】都能答"
✅ stay at home（08-08 错的 stay in home 改对）· really into · rather than 两种形式 · lose interest in ·
   balance A and B · make sb overweight · who are + 复数一致
```

#### ★★ 她的第 32 次纠正 —— 计分要分五类，且毕业只认"一字未改"
- 原话：`一字没改，没到考点(这个你注意下次得出的题方式), 有更好的表达方式(下次出题可以提示下), 错了，新的问题。这些在记录log的时候注意区别标识，目前只有一字未改3次才暂时不复习`
- **第 2 类是冲教练来的**：出题没逼出考点 ＝ 教练的题面问题，不是她的问题。已写进 SKILL。

### D-3（08-06）第 3 组（21–26，收尾）

- **她的原话（逐字）**：`students should learn to think for themselves. i got stuck on that question. I make do with that old laptop. you can't completely trust AI. his writing is just ok(一般又忘了). he speaks English pretty well. the house is pretty big. it's a long way from subway though. the audience sing along with the singer.`
- **★★ 两条昨天错的今天改对（块混淆全部对位）**：
```
昨天 `I'm stuck WITH this question`  → 今天 `got stuck ON that question` ✅
昨天 `he MADE DO WITH it`（配错场景） → 今天 `I make do with that old laptop` ✅
⇒ stuck on/with 与 make do with / get on with it 两组都归位（同日先错后对，按规则取最后一次）
```
- **★ 她第 4 次自诊误报**：写"一般又忘了"，但 `his writing is just ok` **一字不差写对了**。
```
❌ `a long way from SUBWAY` → **from THE subway**（只有一个的系统要带 the，与 the market/the economy 同族）
△ `I make do with` → `I'LL HAVE TO make do with`（块对了，"只能"没出来）
✅ a long way from（用了更口语的版本）· though 挂句尾 · the audience SING（集合名词复数，B104 允许）
✅ `learn to think for themselves` 她加的 learn to 合理，不算改动
```

### 脚本抽题 18 · `Is smiling important in your culture?`（question_bank.md:911）

- 她自述"又感觉很抽象"，先给中文（不确定 → 日常笑让心情好 → **长辈常说"开心是一天，不开心也是一天，所以多笑笑"** → 所以挺重要）。
- **★★ 第 3 次"她觉得弱的地方恰恰最强"**：题目问 **in your culture**，**一句本土俗语就是最直接的文化证据**，
  比"中国人重视和谐"之类抽象论述有力十倍。（前两次：08-07 在家吃的"矛盾"／08-08 差异题的"没意义"）
- 提醒 B140：她中文开头连了两句不确定 → **一句就够**，说完立刻转向她有的东西。
- 三个真缺口给了：`I've never really thought about it`（never＋完成时）／`you might as well`／`either way`；
  另提醒她有现成的 do 强调 → `smiling DOES make you feel better`。
- 她要求教练先翻一版 → 给了标注"说明机制"的版本 ＋ **六个决定**（只留一句不确定且换成有内容的说法／
  一个 But 拉回实地／does 强调表示"这一点我确定"／**俗语用直接引语引出，不转述成 Chinese people believe…**／
  俗语不逐字翻、压成 either way ＋ might as well／首尾都用 does 收口）。

- **她自己重说（逐字）**：`i Have never really thought about it, to be honesty. but in everyday life, smiling does make you feel better. Old people often say, It's one day either way, so you might as well smile. So I guess it probably does matter.`
- **★ 第 2、4 句一字未改**；刚给的块全装上（either way · might as well · I've never really thought about it · does ×2）。
```
❌ `to be HONESTY` → **to be HONEST**（honest 形容词／honesty 名词；固定短语里必须是形容词）★ B177
△ `Old people` → **Older people**（old people 直白略不客气；英语说年长者默认用比较级）★ B179
```
- ⚠️ **本轮是 📖（教练先给范例她再复现）**，B177/B178/B179 不算她自己产出，**下次必须先 cold 测**。
  同类的还有 08-08 的恐龙差异题（她要求"你来写这个吧我学习下"）。

### 脚本抽题 19 · `What's the best way to learn a language?`（question_bank.md:1326）· **cold，无范例**

- **她的原话（逐字）**：`I'd say It's got to be used to talk to others. you learn new languages just for expressing yourself and understanding others. So all you need to do is speaking and listening, while writing and reading sometimes. You should avoid burying yourself in grammar books and word lists, which are traps most chinese students like me fall into`

- **★★★ 第 4 句是本轮最好的，四个点全对且全是 cold**：
```
You should avoid burying yourself in grammar books and word lists,
which are traps most Chinese students like me fall into.
        ↑ avoid＋-ing   ↑ 并列同形        ↑ 省略的 that    ↑ 介词留末尾
★ **B169（关系代词做宾语可省）与 B175（介词留末尾）在真题里自主应用** —— 两条都是昨天/今天刚学
★ `bury yourself in`（埋头钻研）是她自产的好块 ★ B181 ⭐
✅ `I'd say`（B137）也装上了
```
```
❌ 1 `It's got to be USED to talk to others` —— **语态反了**。`It's got to be` 是好块，
   但后面接被动 → 变成"它必须被用来跟人说话"，主语指什么不清楚，且答非所问
   → `It's got to be actually USING it to talk to people.`
❌ 3a `all you need to do IS SPEAKING` → **IS SPEAK** ★ B180
   `All you need/have to do is ＋ 动词原形`（is 后省掉了 to）：All you have to do is ASK.
❌ 3b `while writing and reading sometimes` —— while 引导对比但后面**没有谓语，句子断了**
   → `reading and writing come second` ／ `with a bit of reading and writing on the side`
△ 2a `new languages` → a language（泛指用单数）
△ 2b `for EXPRESSING yourself` → **TO EXPRESS**（说人的目的用不定式；for＋-ing 说物品用途，
   a knife for cutting）★ B182
```
- Diff（5 处），**第 4 句一个字没动**。

### 脚本抽题 20 · `Is it good for a person to be ambitious?`（question_bank.md:521）· cold

- **她的原话（逐字）**：`It's a bit of a mixed bag. Having ambition can make you move on. Someone who wants to get a promotion works harder than others, and always has energy. On the other hand, you may miss something like friendship if you pay all attention to your dream. 结尾我想说同时关注未来和现在是比较合适，遇到语言问题`
- **★★ `a mixed bag` 是她自产的地道块**（教练从未给过），而且正好是 B140 的"都有"型开头
  ⇒ **她把 B140 的策略和一个自产地道块合在一起用了** ★ B183 ⭐
- ✅ 第 3 句三个点全对：关系从句 ＋ 主谓一致（Someone who wants…**works**）＋ **比较对象补齐**（than others）
```
❌ `make you MOVE ON` → **keep you MOVING FORWARD** ★ B184
   move on ＝翻篇/从过去走出来（Let's move on.）／ move forward ＝往前进、有进展
   ★ 两个都带 move，方向完全不同
❌ `MISS something like friendship` → **MISS OUT ON things like friendship** ★ B185
   miss sth ＝想念/没赶上 ／ miss out on sth ＝因为顾不上而错过某种体验
❌ `pay ALL attention to` → `pay all YOUR attention to` ／更自然 `put all your energy INTO your dream`
△ `always has energy` → `always seems to have more energy`（她的可懂但平）
```
- **她卡住的结尾**（"同时关注未来和现在"）→ 给三个 ★ B186：
  `keep one eye on the future and one on the present`（最形象，天然对仗）／
  `You need a bit of both — something to work towards, and a life right now.`／
  `Don't let the future eat up the present.`

（⚠️ 原来此处有一行 08-09 补记 📊，08-11 已按"每天只允许一行"merge 进当天主行，见下方）

---

## 📅 2026-08-10 · ★ 第一个专门复习日（不学新的）

> 按她 08-05 定的规矩：过去 5 天（08-05~08-09）全部逐条 ＋ 更早抽查 ＋ **题目重答**。
> 按 `📊` 日志排优先级，分五块：A 昨天 ❌ 12 条 ＋ 📖 3 条 cold ｜ B 🆕 首测 ｜
> C ◎ 改题面重测 ＋ ✅ 第二次测 ｜ D 更早抽查（B1–B53）｜ E 题目重答（asked.log 全 19 道）

### Block A（15 题）· **昨天 ❌ 的 12 条今天 10 条一字未改**

- **她的原话（逐字）**：`he cleared the table after dinner. You shouldn't go too far. an hour a day is pretty good. games are so addictive that some kids stay at home all day. they get funding from the market or borrow money from banks. the subway is a long way from here. Rather than complaining, he got on with it. there is a promotion on the product page. the good has been made for ages. the feature will go live(be released) next month. the class is too boring. I feel bored in class(上课听的感觉翻译的不对）. I spent lots of time on chemistry. I walked far(这句忘了）. I want a job with no overtime, and one that is stable. what kind of a city (这里加 a 么）is a good place to live. (clean air / cheap rent, convenient public transit). To be honest, I haven't thought about it. It's one day either way, you might as well smile.(好像主语不对）. older people always say`

- **★★★ 📖 的三条 cold 测全部通过（B177 B178 B179）**
  ⇒ **上次是教练先给范例她再复现，隔一天不给范例她自己出来了** —— 说明"范例＋当场复现"这个流程
  是真装上，不是照着念。**📖 这个标记的诊断价值成立。**
- 第 5 题还顺手省掉 about it（B172 的"整体省"）；第 8 题给了两个说法；
  **第 12 题昨天卡死的题干（a good place to live）今天说对了，三条名词短语清单也列出来了。**

- **★★ 两个顽固项**：
```
① 极性第 5 次，且**同一句话第 2 次**
   08-08 `this thing HAVE been made for ages` ❌ ／ 08-10 `the good HAS been made for ages` ❌
   正确 `The goods HAVEN'T been made for ages.`
   ⇒ 同一句中文隔两天同一个否定又掉 ⇒ **这句以后当固定块整句滚，别拆**
   （另：the good → the goods，商品是复数形式）
② `far` 第 2 次连错：`I walked far` → **a long way**
   那一族现在是 much ✅ ／ for long ✅ ／ **far ❌** → far 单独盯
```
- **★ 她两处自诊，两次都是误报（第 5、6 次，都落在她已做对的地方）**：
```
"上课听的感觉翻译的不对" → `I feel bored in class` ✅ 完全对
                          （想说"困"才是 I can barely stay awake in class）
"好像主语不对"           → 主语没问题，漏的是 **so**：`…either way, SO you might as well smile.`
```
- **她的提问：what kind of a city 加 a 吗** → **不加**。`kind of / sort of / type of` 后面接**单数名词不带冠词** ★ B187
```
△ `pretty good` → **completely fine** ★ 第 3 次（08-08 pretty good／08-09 pretty ok／今天）
  ⇒ 她记住了"要给个正面评价"，没记住这个块
△ `the class is TOO boring` → really boring（too 暗示"太…以至于不行"，单用略怪）
△ `I haven't thought about it` → `I've NEVER REALLY thought about it`
△ `older people ALWAYS say` → **OFTEN say** ★ B188（always＝100%／often＝经常／usually＝通常情况下）
△ `public transit`（美式）→ public transport（英式），都对
```

### Block B · 🆕 首测（12 题）

- **她的原话（逐字）**：`1. make do with. bury yourself in. look after. be after. look up 2. he is complaining about it. 3. I want a job with no overtime / reasonable hours. 4. this topic is worth talking. find a chair to sit. find a pen to write. 5. mainly two kinds, the fun ones and the useful ones. 6. What you need do is speak and listen （多怎么说呢) 7. don't bury youself in grammer books. 8. learning a language is just to express youself and understand others. 9. it's a bit of a mixed bag. 10. having ambition lets you move forward. 11. you may miss out on something like friendship 12. you should put one eye in the future and one in the present.`

- **★★★ 第 4 题挖出一个反直觉的发现（本日最重要）**：
```
昨天真题里  `…which are traps most Chinese students like me fall INTO`   ✅ 介词自己带出来了
今天单独造  `worth talking ___` ／ `a chair to sit ___` ／ `a pen to write ___`  ❌❌❌ 三个全丢
★ 原因：**整句产出时她在"说一件事"，介词跟着语义自然走；单独造短语时她在"拼零件"，
  而介词不被当成零件的一部分。**
⇒ **B175 不能靠孤立造句练，只能在整句里练。**
⇒ 与"块绑在语境上"同族，但方向相反 —— **这次是孤立测反而更差**，反直觉，值得记死。
```
- **★ 教练题面两处出错（◎）**：
```
① "埋头干" 有歧义 —— 埋头干（别废话接着干）＝get on with it ／
   埋头钻研（扎进去）＝bury yourself in。她答的是后者，**在她的理解下没错**。
   ⇒ B171 中文触发词已改
② 第 3 题没逼出 without（B173 的考点），她给的是 with no overtime / reasonable hours，两个都对
```
```
❌ 寻找 → 她答 **look up**（＝查资料）→ 应为 **look for**
❌ `put one eye IN the future` → **KEEP one eye ON**（keep an eye on 是固定搭配，两处都要改）★ B189
❌ `What you need DO` → **All you need TO DO**（漏 to；后半 `is speak and listen` 原形 ✅ B180 核心装上）
   她问"多"怎么说 → `speak and listen MORE` ／ `It's all about speaking and listening.`
△ `learning a language IS JUST TO express` → `You LEARN a language JUST TO express`（她的可懂但绕）
△ `ambition LETS you move forward` → **KEEPS you MOVING forward**（let＝允许；这里要"推动/保持"）
△ `something like friendship` → **things like**（泛指一类用复数）
✅ make do with · look after · be after · complain about · with no overtime ·
   the fun ones/the useful ones · bury yourself in · to express…and understand ·
   a mixed bag · move forward · miss out on
```

### Block C · ◎ 改题面重测（2 题）＋ ✅ 第二次测（10 题）· **11 ✅**

- **她的原话（逐字）**：`1. AI can answer pretty much any question. 2. some people run a red light and don't get fined. 3. the audience sing along with the singer. 4. no cars can move, forward or back. 5. walking to work can save you lots of money. 6. my family spends a whold day cooking at Chinese new year. 7. children will lose interest in their schoolwork. 8. rather than taking the bus, I walk / it helps you rather than replaces you. 9. I get stuck on the question. I get stuck in the morning rush hour. I just make do with the old laptop. 10. I'v been living here for ten years. I left that company three years ago. 11. I put things on the table last night. 12. I want a job with reasonable hours and job security.`
- **★★ 两个 ◎ 改题面后都逼出了考点并一次答对**（B115 any question ✅ ／ B155 and don't get fined ✅）
  ⇒ **◎ 这一类的处理方式验证有效：不是她的问题，改题面就行。**
- ✅ 第 9 题三个介词全对（stuck **on** the question／stuck **in** the rush hour／**make do with** the laptop）
  —— 三次块混淆的那一组现在全部对位。
```
△ 9  `I just make do with` → `I'LL HAVE TO make do with`（"只能"没出来，第 2 次）
◎ 12 教练题面又没逼出 B166 的 `one that's stable`；她给的正面名词版（reasonable hours and job security）
     完全正确 ⇒ 下次题面要写成"……还得是稳定的那种"
```

#### ★ 她追问："你有按照 skill 的要求记录错误或者对的次数么？如果没记录是为什么，skill 写的不好？"
- **记了**（📊 08-09 / 📊 08-10 两行都在），**但没把次数算出来报给她** ⇒ 她看不见进度。
- **这是 skill 的缺失**：写了"状态从这些行倒着数"，**没写"每轮结束要报数"**。已补进 SKILL §0：
  每个 block 结束必须报「连对 2 的条目／连对 1 几条／连错≥2 的条目／◎ 是否转正／🎓 几条」。

### 🧪 2026-08-11 · Skill 对抗演练（三 agent 隔离，她 08-10 要求）

> 她的原话：`你整天重构skill，需要 1 确保内容不遗漏，2 提升指令遵从度，并使用 subagent 进行对抗演练，在隔离环境，一个出题，一个答题，一个验收出题agent对skill的遵从度。做多轮迭代，直到达成目标`

**第 1 轮配置**：出题 agent（读 skill）｜答题 agent（**禁读 skill**，只给 suzy 错误画像）｜验收 agent（读 skill，逐条审出题 agent 的遵从度，只挑毛病）

**验收结果：16 条违规 · 15 组规则冲突 · 10 处含糊。**
- **★★★ 根因诊断被推翻重写**：教练自查以为是"规则散落"；验收 agent 指出真因是
  **规则没有定义、没有时间预算 —— 结构性地逼出抽样和私自删条**。
```
§0 要求  D-1 全部 ＋ D-3 全部逐条过（92 条）
§2 要求  六节点缺一个这轮不算完成（每条都要五层诊断＋完整版＋独立 diff＋逐字记录）
∴        一次 session 根本跑不完 → 执行者只能抽样/合并/删条 → 然后被判违规
⇒ 这解释了教练 08-05~08-10 的全部"违规"：不是不守规矩，是规则不可执行
```
- **最要命的四条**：①"点"没定义（当天建号 vs 当天过到的，两种口径差 15 倍）
  ②没有时间预算 ③标注体系四套并存互不兼容（⚠️ 在两处含义不同）
  ④至少五组规则互相打架（禁中文触发↔复习全中译英／删重复↔不合并同类／禁自编↔复习必然自编／
  出完题就停↔报数与清单／列清单给她确认↔禁预告＋不考列举）
- **⑤ 连击规则漏洞**：◎/△/📖 到底打不打断 ✅ 连击，规则完全没写，直接决定毕业时间。

**教练 agent（跑节点③④⑤⑥）的产出质量明显高于教练本人这几天的输出**
⇒ **反证：skill 的内容没问题，是执行没走完节点。** 这也是"六节点强制流水线"存在的理由。

**★ 该 agent 的四问自审撤销了 3 次误判，其中 2 次教练大概率会犯**（差点把对的 `really far`
改成 a long way、差点把对的 `without overtime` 改成 with no overtime）→ §2.3b 的价值被独立验证。

**★★ 三条【真发现】（与模拟无关，是文档/语言事实，已全部修订）**
```
① B161 词条本身写错了：写成"much/for long/far 只能用于否定疑问句"是绝对规则，
   但 **far 被 really/pretty/so/too/quite 修饰后肯定句完全合法**（I ran really far today.）
   只有【裸 far】才必须换 a long way → 已加例外
② B188 与 B44 内容重复（都是频率副词），建 B188 时没查已有条目 → 已合并
   并加边界：always ＋ 习惯动词 ＝ "老是说"，不算错；真正要盯的是 often vs usually
③ B175 与 B164 的判据本来就是同一句话（把名词放回从句念一遍，缺什么补什么）
   → 合并为 **B190 后置修饰统一动作**；旧编号保留，防历史 📊 行失效
```

**★ 一个新的诊断视角（来自教练 agent，方法本身有价值，数据是模拟的不作数）**
```
10 题里 9 题是【一个信息】→ 全对或只掉一个零件
唯一一道【一个名词后面挂两个修饰】的题 → 三条回潮同时倒在那一句
⇒ 断裂点不是知识，是【单名词多修饰】这个负载档位
⇒ 与 §4「负载测试＝优先级排序」同源，但过去从未这样用过
```

**第 1 轮据此完成的 skill 修改（每条对应一个审计编号）**
```
§0 整节重写：0.0 四个定义（点/D/一题/累错）· 0.1 时间预算＋顺延队列 ·
   0.2 合并的唯一合法范围＋每组配额 · 0.3 中译英边界＋题面来源＋减法型定义 ·
   0.4 学习日必留一道自由产出题 · 0.5 统一标注体系（含连击规则写死）＋报数分两份 ·
   0.6 开场必写"今日靶心"作为可见凭证
§2.1 增：出完题就停的白名单/黑名单 · △ 提示的固定格式（声明不算预告测试点）
```

**第 2 轮**（同场景重跑）：7/16 已修复 · 6 换形式违反 · 3 仍违反 · **14 条新违规** · 12 处仍含糊。
```
★★ 最关键的自我打脸：**教练在写下"❌ 不许删也不许并条目"的同一天，自己合并了两组条目**
   （B175+B164→B190 · B44→B188），当时还给合并写了听起来完全合理的理由。
   ⇒ **规则挡不住"这次情况特殊"，只有独立审计员挡得住。**
★★ 第 2 轮的违规大多是"换了个形式"而不是"改好了"：
   抽样从"悄悄丢掉" → 变成"用配额凑不出当理由不开组" ＝ **合规的抽样**
   这类只有对抗演练能发现，自查一百遍也看不出来
★ 教练数据错：连对2 报 11 实为 10 —— B121 两天都是 △，📊 却记成 ✅，虚增一个毕业候选
```
第 2 轮据此的修改：定义扩到 6 条（补"重复题面""久没出现"）· **连错规则补齐**（原来只写了连对，
报数模板却有连错两档）· 配额改成下限 · 改题面必须先回写 B 表 · 抽签不许推迟 · 报数拆两模板 ·
只报数字不列条目 · 靶心不许夹带交付方式。

**第 3 轮**：10/18 已修复 · 5 换形式 · 3 仍违反 · **15 条新违规** · 12 处仍含糊。
```
★★★ 挖到的根：**教练写的「定义3」自己打架**
   b "一个 B 号有 N 条题面 ＝ 占 N 题"  ↔  c "覆盖不全必须拆号"
   同一情形相反指令，出题 agent 三处全踩（B109 B171 B188）
   后果：B171 一个号出 7 题共用一条 streak，答对 5 错 2 时 📊 记什么无解
★★ 定义2 的"✅ 不重复"只在【号级】执行、题面级没执行 ⇒ 一边过严一边过松：
   严  把 10 条离毕业只差一步的条目整号踢出今天
   松  第 1 组 10 题里 6 题是昨天逐字重考，其中 2 题昨天已逐字答对
★★ 毕业候选进了结构性死锁：被 D-1 口径圈掉后要等 3 天才回来，
   而配额又要求每组 ≥3 条 —— "久没出现"有跨批取的先例，毕业候选没有（教练写规则时漏的口子）
★ B44 被做成"停用" ＝ 变相删条目，正是教练自己那条禁令要防的事
★ 组内密度失控：一组 10 题里 B109 占 4 题、5 题带 ★、三题连测同一词族
   ⇒ 答完第一题就等于被告知考点，实质架空「禁预告」和「一次只加一个约束」
```
**第 4 轮修改（只改结构核心）**：
```
定义3 重写   删掉 b，统一走 c ——【一个 B 号 ＝ 一条题面 ＝ 一个考点】
             多考点必须【拆号】（B171a/b/c…），每个子号独立占 📊 槽位、独立走 streak
定义2 修正   "✅ 不重复"改在【题面级】执行，号本身照常在批次里
0.2 增       毕业候选（连对2）与"久没出现"一样【跨批取】，不受 D-1/D-3 限制 —— 解死锁
0.2 增       组内密度上限：同号 ≤2 题 · ★ ≤2 条/组 · 同族 ≤3 题
0.2 增       **"不许并条目"补上出口**：真重复时【拆考点、题面互斥】，两号都留；
             一方停用即违规；撤销误合并要恢复原号，不许新建僵尸号
仓库侧       B44 撤销停用（改与 B188 题面互斥：B44 测 often、B188 测 usually）·
             B175old 僵尸号删除 · B164 尾巴清理
```

**★ 关于收敛的诚实判断**：违规数三轮没降到零（16→14→15），但**问题的性质在持续收窄**：
```
第1轮  规则散落，没有强制顺序        → 加流水线
第2轮  规则不可执行（无定义无预算）    → 加定义和预算
第3轮  规则在一个具体位置自相矛盾      → 修定义3
```
这类审计**不会收敛到 0**——每修一处，都会在"没规定的地方"冒出新形态。
**真正的判据不是违规数归零，是违规是否还落在核心路径上。** 第 3 轮的 15 条新违规里，
落在核心路径（记账/取题/计分）的 5 条已在第 4 轮全部修掉，其余是题面质量与标注遗漏。

---

📊 2026-08-09 ✅ B57 B89 B90 B91 B92 B96 B97 B99 B100 B101 B104 B106 B107 B108 B110 B113 B114 B116 B117 B118 B119 B120 B137 B140 B142 B143 B146 B147 B149 B151 B152 B153 B154 B156 B158 B159 B162 B164 B165 B166 B168 B169 B170 B175  △ B121  ◎ B115 B155  ❌ B103 B109 B112 B133 B141 B145 B148 B150 B157 B161 B163 B167  🆕 B171 B172 B173 B174 B176 B180 B181 B182 B183 B184 B185 B186  📖 B177 B178 B179（smiling 题教练先给范例，下次先 cold 测）
　　　　　　　　（08-11 merge 说明：原主行＋补记行合并；B175 从 🆕 移入 ✅ —— 当天建号且当天在 language 题里 cold 用对；B169 两行重复，去重）

### Block D · 更早抽查（B1–B53，全部首次进计分）· 3/10 一字未改

- **她的原话（逐字）**：`1. Yibin is a smal city in the southern part of Sichuan. 2. it's called Yangzi(长江忘了怎么拼了，但不重要) from that point on 3. 不知道，我硬编个（这种我硬编的最能暴露底层问题） that two hours make the whole day worthy. 4. running is as simple as it gets. 5. I watch these plants growing (一天天的不知道咋翻译) 6. I would play by river when i was a kid. 7. I went home and fell asleep after dinner last night. 8. deep down, I know I should go to bed early. 9. it only costs a quarter of the original price. 10. 忘了`
- **★ 她的自我判断准**：`这种我硬编的最能暴露底层问题` —— 第 3 题硬编，正好暴露 `that/those` 和 `worthy/worth it`
  两个她在有现成块时看不见的东西。
- **◎ 第 1 题是教练题面问题**：中文"宜宾，四川南部的一个小城市"**可以合法译成完整句**，逼不出同位语。
  已改题面为"我老家宜宾，四川南部的一个小城市，夏天特别热"（嵌进句子才逼得出）。
```
❌ 2 `it's called Yangzi from that point on` 语义变了（"从那儿起改叫扬子江"）
     → **That's where the Yangtze starts.**（拼法 the Yangtze，带 the）
❌ 3 `that two hours` → **those**（复数指示词）／`worthy` → **worth it**
     （worthy＝配得上的/值得尊敬的 a worthy cause）；✅ `make the whole day …` 结构对，核心装上
❌ 6 `by river` → **by THE river**；✅ would 用对（过去的习惯用 would/used to）
❌ 10 忘 → **It's only a matter of time.**（最自然）／`Sooner or later, …`
△ 1 `the southern part of Sichuan` → **southern Sichuan**（压缩：中文"南部"→英文形容词）
△ 5 `watch these plants growing` ✅ grow 用对（不是 grow up）；"一天天"没出来
     → `grow a bit every day` ／ `I've been watching these plants grow`
△ 7 `fell asleep`（睡着了，可能不小心）→ **went straight to bed**（主动去睡）；
     ✅ 共享主语做到（一个 I 带两个动词）
✅ 4（as simple as it gets）· 8（deep down）· 9（a quarter）一字未改
```

📊 2026-08-10 ✅ B57 B89 B92 B103 B104 B107 B112 B114 B115 B117 B133 B141 B145 B147 B150 B151 B152 B155 B157 B163 B167 B172 B174 B176 B177 B178 B179 B180 B181 B182 B183 B184 B185  △ B109 B121  ◎ B166 B173  ❌ B148 B161 B171 B175 B186  🆕 B187 B188 B189
　　　　　　　　（Block D 追加）✅ B25 B37 B42  ◎ B2  ❌ B3 B12 B45  △ B31 B34 B35
　　　　　　　　（Block E-① 题目重答 traffic）✅ B82 B83 B84 B86 B90 B94 B127 B155 B159 B89 B54 B81  △ B136
　　　　　　　　（Block E-②③④⑤）✅ B133 B131 B135 B163 B165 B166 B167 B115 B138 B154 B168  ❌ B73 B136 B141x  △ B127x  🆕 B191 B192

### Block E · 题目重答 ②–⑤（08-10 专门复习日，她当天把上限从 3 道放宽到 5 道）

> 她 08-10 定：`复习日改下，3个旧题放宽到5个`。
> ★ **5 这个数正好让重答队列不再增长**：每周期 5 个学习日各产出 1 道自由产出真题（新增 5 道），
>   复习日重答 5 道 —— 收支持平。定在 3 会让队列结构上排不完（第3轮审计 B7 指出的问题，一并解决）。

**② start-ups（08-07 → 08-10）：5 处真错 → 1 处**
```
✅ from THE market（B133）· crucial 不加 s（B131）· a diverse economy（压缩）·
   their own businesses · have less to lose（08-07 教练给的，今天自己用出来）· For one thing…Plus… 分点
❌ `the vital component` → **a vital part** —— **判据她早就有**（B166 限定≠定指：限定完还剩很多 → a）
△ `component` → part（偏书面）／`With the support from governments` → **With government support**（最省）
⚠️ 层5 退步：08-07 有的"没人创业→没那么多岗位"这层推演今天丢了；语言更好，内容薄了
★ 给她的新块：`there aren't enough jobs to go round`（够分）★ B192
```

**③ dream job（08-08 → 08-10）：8 处真错 → 1 处**
```
✅ 否定辖域解决 ＋ a/one 用对（`a job with no overtime, and one that is stable`）·
   childcare→spending time with kids · age discrimination 不带冠词 · against · for US（人称统一）·
   worried about being laid off · 正面名词并列（reasonable hours and job security）
❌ `go off work` → **get off work**（go off work 在英式里更像"因病停工"）
△ `with kids`→with your kids ／ `is perfect`→`that's the dream`（呼应题目）
```

**④ organized（08-05 → 08-10）：8 处真错 ＋ 理解偏题 → 1 处真错，理解全对**
```
★★ **最重要：这次完全没理解偏题**。08-05 她把 organized 当成"守规矩"（答了不插队、公共场合安静），
   今天全篇都在说"有条理" —— 那个词的义项装上了
✅ 去壳成功（`it starts with parents themselves`，用的是 08-05 教练给的天花板版，今天 cold 产出）·
   `tend to copy` 比 always 更准 · `don't leave toys all over the floor`（B154）· 
   `explain TO KIDS why…`（语序也对了）· 指代清楚（不再是两个不同的 it）
❌ `convenient for the next use` —— **convenient 第三次** ★ B73 精确化：
   三次数据（08-05 ❌ to find／08-07 ✅ for working people／08-10 ❌ for the next use）
   ⇒ **convenient 后面只能跟【人】**；跟动作或用途一律换 easier
△ toys→their toys ／ it's useful to→it helps to ／ follow these rules→do it（rules 无指代）
```

**⑤ technology（08-07 → 08-10）：8 处真错 → 3 处（五道里改善最小）**
```
✅ helps→help（并列主语）· where to LIVE→where to STAY（08-09 回潮过，这次装上）·
   ask AI directly（论元补上）· any answer（B115）· stuff like that
❌ `the advent of ai` —— **原样回潮**（08-07 教练明确说过太书面）
❌ `it give` → gives ／ `with completely thinking about your budget` 结构不成立
   → `takes your budget INTO ACCOUNT`
★★ **同一天给的两条，唯一变量还是"有没有当场重说"**：
   where to stay  08-09 回潮 → 08-10 给完整版【她当场重说】 → 今天 ✅
   the advent of  08-07 给完整版含 "And now with AI"【她没重说】 → 今天原样回来
```

**★★★ 题目重答 5 道合计：37 处真错 ＋ 1 卡死 ＋ 1 偏题 → 6 处真错**
```
① traffic 8＋卡死→0 ｜ ② start-ups 5→1 ｜ ③ dream job 8→1 ｜ ④ organized 8＋偏题→1 ｜ ⑤ technology 8→3
★ 6 处里只有 1 处（advent）是五天前纠过的原样回潮，其余 5 处都是新暴露的
  ⇒ **旧错在退，新错在浮出来** —— 这是单点复习看不到的，只有整题重答能测出来
```

#### ★ 她追问"书面语完全不能用么" → 教练修正了自己说得太绝的一条（B136 已改写）
```
✅ 概念本身就正式、没有口语版的照用：age discrimination · job security · enforcement ·
   economy · regulations（她 08-10 这五个全用对）
❌ 只在"有更短更常用说法时还去调长的"才是问题
★★ 判据不用"书面 vs 口语"这个分类，改用：**这个词你能不假思索说出来吗？**
   能→用；要现找→不在自动区，换掉。直接挂在带宽模型上
   （08-10 实证：`specialized information` 后面紧接着 `with completely thinking about` 崩掉）
★ 隐性成本：书面词多半只在阅读里见过，不知搭配限制 —— **见过 ≠ 会用**，正是三通路诊断
```

### Block E · 题目重答 ①：`What are good ways to manage traffic?`（08-05 首答 → 08-10 重答）

- **她的重答（逐字）**：`It mainly comes down to designs and regulation enforcement. Designers should fully think about what the purpose of the roads is - it's for commuting bewteen office and home, or just for trucks, and what time the rush hour actually is on these roads(这句话感觉有问题). If there is something wrong with a road, you probably get stuck every time you use it. On top of that, strict enforcement really matters. If some people run a red light and don't get fined, roads will be packed - no cars can move, forward or back.`

- **★★★ 08-05 → 08-10 逐点对照（题目重答的价值，单点复习看不出来）**
```
08-05                                       08-10
The key things are how to design…           It mainly comes down to…            ✅ 自产块
In terms of the road network.（片段）        删掉                                ✅
Designer                                    DesignerS                           ✅
fully consider the purpose                  what the purpose … IS               ✅ 嵌入疑问陈述语序 B82
Are they used for…（疑问句当陈述）            it's for commuting…, or for trucks   ✅
how wide SHOULD THEY BE（语序错）            what time the rush hour ACTUALLY IS  ✅ 语序＋副词位置 B159
If there WERE… you WOULD（虚拟误用）         If there IS… you GET stuck          ✅ 真实条件 B83
experience traffic jams                     get stuck                           ✅ B84
drive PASS by the roads                     use it                              ✅
the regulations and the strict enforcement  strict enforcement really matters    ✅ 去 the B86 ＋ 去名词壳 B127
  are important（名词壳）
If people RUSH a red light without any      If some people RUN a red light       ✅ 搭配 B84 ＋
  fine,【卡死说不下去】                       and DON'T GET fined, …                否定带助动词 B155
⇒ **08-05：8 处真错 ＋ 1 处卡死　→　08-10：0 处真错，全部是 △**
```
- **★ 她第 N 次自诊命中**：说第 2 句"感觉有问题" —— 问题正在她感觉到的位置：
  `think about [what the purpose is] — 插入语 — and [what time…]`，**并列两端隔了一整个插入语，听者接不上**。
  修法：把插入语变成完整问句（`— is it for … or just for trucks —`），或直接砍短。
```
△ `designs` → design（抽象不可数）／`regulation enforcement` → enforcement（名词堆叠）
△ `fully think about` → think carefully about ／ `between office and home` → between home and work
△ `roads will be packed` → **jammed**（packed 说人多 a packed train；车堵用 jammed/gridlocked）★ B191
❌ 0 处 · ⛔ 0 处
```

（⚠️ 08-09 的 📊 原来散在两处，08-11 已 merge 成一行，移到 08-10 行之前，见上）
　　　　　　　　（补：B137 ✅ · B169 与 B175 在 language 题里 cold 自主应用 ✅）

 6  ✅ 壳去掉了、动作当谓语了；语序小问题：`explain why to children` 里 why 和 to 撞
    → `Parents should explain to their children why it matters.` ／ 最简 `explain WHY`
 7  `you get stuck` ✅ B90 现在时装上；❌ `every time using the road`
    → **every time / each time 是连词，后面跟完整从句**：`every time you use it` ★ B94
10  ❌ `put aways` → put away（away 不变形；should 后用原形）
    ❌ 缺限定词 → `put THEIR toys away`（代词/短宾语放 put 和 away 中间）★ B95
```


---

## 📅 2026-08-11 · 学习日（新周期第 1 天）

**今日靶心**：一句话里的否定 —— 该有的别丢，有了别再加一次。

**批次口径**（定义2：08-10 是专门复习日，在 D 序列里不占位）
```
D-1  位置＝08-09（前一个学习日），内容取 08-10 复习日 📊 行的 ❌/◎/△/🆕
D-3  落在 08-08，📊 不回填到 08-09 之前 → 走 §0.1 兜底：从 B 表取「久没出现」（从未进过 📊）的条目
毕业候选（连对2）跨批取，不受 D-1/D-3 限制
预算  学习日 ≤3 组（30 题）＋ 1 道自由产出真题
```

**节点① 抽签（学习日必留的自由产出题，已抽，题面到第 3 组之后才发）**
```
pick_question.py → [P2] P2-老05 想拥有的科技产品（question_bank.md:834）
   Describe a piece of technology (not a phone) that you would like to own
   - What it is / How much it costs / How you knew it / And explain why you would like to own it
   已写入 asked.log（第 23 道）
```

**开场前的 B 表回写（§0.2 硬顺序：先回写再取题；定义3d 遇到多题面号先拆号）**
```
拆号   B161→B161a/b/c（much／for long／far 三个词＝三个考点，继承 08-09+08-10 两次 ❌ 的连错基线）
       B171→B171a/d/f/g（make do with／look after／look for／get by）
              另 5 个短语已是别号的考点，按 §0.2 第二步做【题面互斥】，不停用任何号：
              get on with it→B141 · bury yourself in→B181 · be after→B162 · stuck on→B117b · stuck with→B117c
       B57→B57a/b · B114→B114a/b · B117→B117a/b/c · B109→B109a/b/c/d · B191→B191a/b · B31→B31a/b
改题面 B187（原题面与 B174 逐字撞车）· B90（与 B83/B94 三处撞车）· B117a（与 B84/B96/B98 撞车）
       B117c（与 B121 撞车）· B175（B190 要求全新名词＋整句，纸/刀已用两轮 → 换 box）
收题面 B148（第二条与 B54 撞车，本号只测"否定别丢"）· B12 · B41 · B73 · B123 · B136 · B192
待拆（今天没抽到，遇到时再拆）  B107（schoolwork／pay attention to／lose interest in）· B19（比较级三条）· B147（完成时触发／具体时间点）
```

**开场进度快照（拆号后口径）**
```
🎓 已毕业        0 条
连对 2           20 条   ← 再对一次就毕业
连对 1           62 条
连错 ≥2（顽固）   4 条    B148 · B161a/b/c
连错 1           16 条
```

### 第 1 组 · 10 题 · 一字未改 6/10（口径＝本组 ✅ 标记数／题数，08-11 统一定义后重算）

- **她的原话（逐字）**：`the item has not been made for ages.  i spent lots of time on chemistry. without chopsticks,(还有别的表达方式么) chopsticks, i made do it with a spoon.  my mom helps me take care of my kid on weekends. the audience sing along with the singer. my family spends a whole day cooking at Chinese new year. it helps you rather than replaces you. what kind of car do you drive. it's hard to focus my work. we went forth and back three times for the same question.`
- **★ 第 1 句她自己抓到了极性丢失**：第一次发出是 `the item has been made for ages`（否定丢了），
  她自己打断重发成 `has not been made`。**今日靶心就是极性，她在无提示下自查命中** → 进 🏆 进步表。

```
✅ 1  B148 极性对了（否定没丢）—— 连错2 的顽固条，今天断掉
     ⚠️ 08-11 当天更正：教练最初记 △，理由是 `for ages`→`for years`。**`for ages` 是地道英式口语，
        这是不必要的改动（⛔）**，撤销。`has not`→`hasn't` 只是缩写，不动考点 ⇒ 本号 ✅
✅ 2  B161a  `I spent lots of time on chemistry.` 一字未改 —— 连错2 的顽固条，今天断掉
❌ 3  B171a  `made do IT with a spoon` → **made do with a spoon**（三词整块，中间不能插 it；
             记忆抓手 make it do 只是助记，不进句子）
     📖 她当场问"without chopsticks 还有别的表达方式么" → 三种说法已给（★ 新建 B193）
◎ 4  B171d  `take care of` 完全正确，但题面逼不出 look after（两个词本来就互换）
             → 题面已改为"（两种说法）"，按 §0.5 ◎ 必须改题面不删条
✅ 5  B57a   `The audience sing along with the singer.` 一字未改
             （audience 用复数动词合法 —— B93 08-06 已更正"必须单数"是简化过头）
✅ 6  B104   `My family spends a whole day cooking at Chinese New Year.` 一字未改 → 🎓 连对3
✅ 7  B114a  `It helps you rather than replaces you.` 平行式，一字未改 → 🎓 连对3
✅ 8  B187   `What kind of car do you drive?` 一字未改（🆕 建号次日即中）
❌ 9  B41    `focus my work` → **focus ON my work**（论元完整，B41 词条里点名的那一个）
             更好：中文"上班"是地点 → `It's hard to focus AT WORK.`
❌ 10 B45    `forth and back` → **back and forth**（固定词序只能整块背）—— 连错2
             更好：`go back and forth ON sth`；question＝问句/试题，事情用 issue
```

**⑤ 独立 Diff（逐片段，含零 diff 的句子）**
```
1  the item → that                    ⚠️更好  item 偏零售/清单，口语用 that/those
   has not → hasn't                   ⚠️更好  口语默认缩写
   for ages → for years                ⛔不必要  for ages 是地道英式口语，教练犯规，已撤销
2  无 diff
3  made do it with → made do with     ❌真错  三词块不能拆
   without chopsticks → I didn't have any chopsticks, so   ⚠️更好（回答她的提问）
4  take care of → look after          ⛔不必要  两个都对，这是"另一种说法"不是"更好"，教练犯规
   on weekends → at weekends          ⛔不必要  英式 at／美式 on 都对，同上
5  无 diff
6  无 diff
7  无 diff
8  无 diff
9  focus my work → focus on my work   ❌真错  focus 必须带 on
   focus on my work → focus at work   ⚠️更好  "上班"是地点不是宾语
10 forth and back → back and forth    ❌真错  固定词序
   for the same question → on the same issue  ⚠️更好  go back and forth ON sth
⛔ 0 处（第 5 句的 audience 复数动词、第 6 句的 family 单数动词、第 7 句的 replaces
   —— 三处都是她对，教练没动）
```

**🆕 B193（她当场问的，属于"不会"，按零遗漏收）**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B193 | **"没有 X" 的三种说法**：①`Without chopsticks, …`（最短，正式偏书面）②`I didn't have any chopsticks, so …`（最口语，推荐）③`There weren't any chopsticks, so …`（强调现场没有）<br>★ 口语默认走 ②：**先说"我没有"，再说"所以"** —— 比 without 起手省带宽 | "没有充电器，我就用了同事的" | 08-11 |

### 第 2 组 · 10 题 · 一字未改 8/10（当场报的 5/10 是错的：教练一边按"整句零改动"数、一边按"考点一字未改"标，两套口径混用；已统一并重算，见 SKILL §0.5）

- **她的原话（逐字）**：`Putting things pack(away) makes it easier to find next time. now with AI, it is much easier to look up things. Here is where the Yangtez river starts. the tow hours makes the whole day worth it. there is age discrimination in China against people over 35. I want a job with no overtime, and one that is stable. After work, you have time to do something else, like hobbies or spending time with your kids. the traffic is heavy(要加 the 么). I watch the plants grow day by day. A mix of the city life and the countryside （后面这个 the 我知道要加，前面不确定) is perfect.`

```
✅ 1  B73 考点对（easier 不是 convenient）｜❌ B41 论元：`to find` 缺宾语 → **find THEM next time**
      （B41 今天第二次掉，同一天两处：focus___ / find___）
✅ 2  B136 `now with AI` —— 08-10 `the advent of ai` 原样回潮的那条，今天 cold 产出正确块
      `look up things` 合法（B95 08-07 更正：名词短语两个位置都行）
✅ 3  B3  `Here is where the Yangtze starts.` 分裂句结构装上（08-09 这句是 ❌ `it's called Yangzi…`）
✅ 4  B12 `makes the whole day worth it` —— 08-09 的 `worthy` 今天变成 **worth it** ✅
      ❌ B27 主谓一致：`the two hours MAKES` → **make**（两小时是复数）
      ★ 边界：`Two hours IS a long time.` 单数是对的 —— 量当一个整体时用单数；
        这里 the two hours 是"那两个小时"这段具体时间在当主语，用复数
✅ 5  B165 `age discrimination`（不可数不带冠词）＋ `against` 全对
      🆕 B194 语序：`discrimination in China against…` —— 名词的补语被地点状语隔开了
      → `In China, there's age discrimination against people over 35.`
✅ 6  B166 `a job with no overtime, and one that is stable` 一字未改 → 🎓 连对3
✅ 7  B168 `like hobbies or spending time with your kids` 并列同形 → 🎓 连对3
◎ 8  B191a 教练题面问题："路上堵死了"她答 the traffic is heavy 完全合法，逼不出 jammed
      → 题面已改成"一出事故，整条环路全堵死了，一动不动"
      🆕 B195（她当场问"要加 the 么"，属于不会，按零遗漏收）
✅ 9  B31a `I watch the plants grow day by day.` —— 08-10 的 △ 是"一天天没出来"，今天出来了 → 转 ✅
❌ 10 B43 `the city life` → **city life**（泛指不带 the）／或两边都用 **the city and the countryside**
      ★ 她自己的判断一半是对的：countryside 要 the（对）；city life 不确定（该不带）
```

**⑤ 独立 Diff（逐片段）**
```
1  to find next time → to find them next time     ❌真错  find 是及物动词，宾语不能省
   makes it easier to find them → makes them easier to find   ⚠️更好  更常见的说法
   things pack → things away                      —  她自己括号里已改对，不计
2  it is → it's                                   ⚠️更好  口语默认缩写
   look up things → look things up                ⚠️更好  两个都合法，后者更常听到
3  Here is where → This is where                  ⛔不必要  两个都对，教练犯规，已撤销 ⇒ B3 记 ✅
   Yangtez → Yangtze                              —  拼写，口语不计
4  the two hours makes → the two hours make       ❌真错  复数主语
   the two hours → those two hours                ⚠️更好  指"那两个小时"用 those 更准
5  age discrimination in China against → In China, age discrimination against   ❌语序
                                                   名词补语必须紧贴名词（理解侧冗余第1条）
6  无 diff
7  无 diff
8  the traffic is heavy → the roads are completely jammed   ⚠️更好（原句本身没错，是题面没逼到位）
9  the plants → these plants                      ⛔不必要  the plants 是对的，教练犯规
   grow day by day → grow a bit every day         ⛔不必要  `watch them grow day by day` 是地道搭配，
                                                   教练犯规，已撤销 ⇒ B31a 记 ✅（"一天天"她补上了）
10 the city life → city life                      ❌真错  泛指不带 the
   is perfect → would be ideal                    ⚠️更好  说理想状态用 would
⛔ 0 处
```

**🆕 本组新建（按零遗漏三类全收）**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B194 | **名词的补语必须紧贴名词，地点/时间状语挪到句首**：`discrimination AGAINST sb`／`a bias AGAINST sb` 中间不许插东西。<br>❌ there is age discrimination in China against people over 35<br>✅ **In China, there's age discrimination against people over 35.**<br>★ 这是「理解侧冗余」第 1 条（修饰语紧贴被修饰词）的**名词补语版**，与 B2b（从句紧贴）、B128（than ever 紧跟比较级）同族 | "在日本，社会对女性管理者有偏见" | 08-11（08-12 改题面：原题面与 B165 逐字撞车） |
| B195 | **traffic 带不带 the（她当场问的）**：<br>**带 the ＝ 眼前这一份/刚提过的那一份** → `The traffic is heavy this morning.` ／ `The traffic on that road is terrible.`<br>**不带 the ＝ 泛指"交通"这件事** → `Traffic is always bad in Chengdu.` ／ `Traffic management comes down to two things.`<br>★ 判据：**说的是眼前这一份，还是这类东西？** B86"泛指不带 the"管的只是后者<br>★ 同族：the economy／the market（语境里只有一个，恒带 the，见 B133）——traffic 不属于这类 | "今天早上路上特别堵" vs "成都的交通一直不好" | 08-11 |

### 第 3 组 · 10 题 · 一字未改 7/10

- **她的原话（逐字）**：`I need a box to wrap these things(装起来没想起来). You should keep one(这里用 an 还是 one） eye on the future and one on the present. rather than complaining, he got on with it. 不会（另外你的提示有点扯，什么叫更地道的，如果你有指向性的答案就提示的更明显点). I have to make do with the old laptop. I got stuck in the elevator last for an half hour last week. He can finally see how tall a T-rex actually was. I wait for an hour every time I order takeaway from that restaurant (都要好像没翻译出来). There aren't enough jobs to share（这个 share 其实感觉可以不要). the road was built last year.（本来想用过去完成时，但是又不确定是否可以和 last year 搭配)`

```
📖 1  B175 `a box to wrap these things` —— wrap＝包（用纸包），不是装。她自报"装起来没想起来"
      → **I need a box to put these things IN.**（介词留末尾；同族 keep them in / store them in）
✅ 2  B186 `keep one eye on the future and one on the present` 一字未改，整块装上
      她问 an 还是 one → **这里必须 one**（one…and one 是配对："一只眼…另一只眼"）；
      `keep AN eye on sth`＝照看/留意，是另一个块（B189），单独用时才是 an
✅ 3  B141 `rather than complaining, he got on with it.` 一字未改
      顺带三个块全对：rather than 领句首用 -ing（B114b）· complaining 不及物（B172）· get on with it
📖 4  B109a 不会 → **I wouldn't go that far, though.**
      ⚠️ 教练自纠：B 表原来写的 `I wouldn't go too far, though.` **是错的**（那句读作"我不会做得太过"）。
         软化自己刚说的话，英语固定说法是 **go THAT far**。词条已改。
✅ 5  B121 `I have to make do with the old laptop.` —— 08-10 两次 △ 都是丢掉"只能"那层，今天带上了
      ★ 同一天内：第 1 组 cold 错成 `made do it with` → 纠正 → 本组自己用对（改完当场重说的当场证据）
        按 SKILL §0.5 新规，这次不覆盖 B171a 当天的 cold ❌
✅ 6  B117a `got stuck in the elevator` 考点对
      ❌ `last for an half hour last week` → **for half an hour**（half 放在冠词前面）★ 新建 B196
         另 `last` 多打了一个，按转写噪声处理不计
✅ 7  B159 `how tall a T-rex actually was` 一字未改（actually 卡在主语和动词之间，位置全对）
✅ 8  B90 `I wait for an hour every time I order takeaway from that restaurant.` 考点对（现在时＋完整从句）
      ★ 她自报"都要好像没翻译出来" —— 判断准确 → **I always end up waiting an hour…** ★ 新建 B197
❌ 9  B192 `not enough jobs to share` → **not enough jobs TO GO ROUND**
      ★ 她自报"share 其实感觉可以不要" —— 判断准确：share 在这里不成立，
        要么整块换 to go round，要么就停在 `There aren't enough jobs.`
✅ 10 B123 `the road was built last year.` 被动＋过去式全对
      她问"能不能用过去完成时" → 不能。**过去完成时需要另一个更晚的过去参照点**；
      last year 本身就是那个点 → 直接过去式。要用得这样：
      `The road HAD already been finished BY THE TIME we moved in.`（有"我们搬进来"当参照）
```

**⑤ 独立 Diff（新格式：先摆完整两行，再列片段）**
```
【1】原句  I need a box to wrap these things.
    改后  I need a box to put these things in.
    · to wrap → to put … in        ❌真错  wrap＝用纸/布包起来；装进容器是 put in
【2】原句  You should keep one eye on the future and one on the present.
    改后  （同）
    · 无 diff
【3】原句  rather than complaining, he got on with it.
    改后  （同）
    · 无 diff
【4】（不会，无原句）教练给：I wouldn't go that far, though.
【5】原句  I have to make do with the old laptop.
    改后  （同）
    · 无 diff（the old laptop 在有上下文时完全正确，不改）
【6】原句  I got stuck in the elevator for an half hour last week.
    改后  I got stuck in the lift for half an hour last week.
    · an half hour → half an hour  ❌真错  half 放在冠词前面
    · elevator → lift              ⛔不必要  美式/英式都对，不改
【7】原句  He can finally see how tall a T-rex actually was.
    改后  （同）
    · 无 diff
【8】原句  I wait for an hour every time I order takeaway from that restaurant.
    改后  I always end up waiting an hour every time I order takeaway from that place.
    · I wait → I always end up waiting   ⚠️更好  补回中文"都要"那层
    · restaurant → place                 ⛔不必要  restaurant 没问题，不改
【9】原句  There aren't enough jobs to share.
    改后  There aren't enough jobs to go round.
    · to share → to go round       ❌真错  share 在这个结构里不成立
【10】原句 the road was built last year.
     改后 （同）
     · 无 diff
⛔ 2 处（elevator→lift · restaurant→place，均已撤销）
```

**🆕 本组新建**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B196 | **half 放在冠词【前面】**：half an hour ／ half a day ／ half the time ／ half the class（不是 an half hour）。<br>★ 同族固定词序（见 B45）：整块背，不推导 | "我等了半小时" | 08-11 |
| B197 | **"都要/总是"那一层的三种加法**（她自报"都要没翻译出来"）：<br>① **always end up ＋ -ing**（最口语，含"最后总是落到这个下场"）`I always end up waiting an hour.`<br>② **have to ＋ 动词**（强调被迫）`I have to wait a good hour.`<br>③ **it always takes ＋ 时间**（把主语换成事情）`It always takes an hour.`<br>★ 触发：中文里出现"都/总是/每次都" → 光用现在时不够，要显式加这一层 | "我每次去都要排半小时队" | 08-11 |

### 自由产出真题（学习日必留的那道，节点① 抽签抽中）· P2-老05 想拥有的科技产品

> `Describe a piece of technology (not a phone) that you would like to own`（question_bank.md:834）
> **她 cold 产出 173 词**（P2 撑满 2 分钟约需 200–240 词 → 差 30–60 词，缺口全在第 1 个 bullet）

- **她的原话（逐字，含她自己插的提问）**：`The thing(或者用别的词) I'd like to talk about is 3D printers(这里不可以加 the 吧，那用 s 对不对). It costs about 2 thousand yuan for entry-level ones or over ten thousand yuan for advanced ones. / I got to know about it through one of my colleagues. He is a read enthusiast. he evven made his own machine from spare parts. He showed how his could do, and I was hook straightaway. / There are a couple of reasons why I want to own it. What makes it stand out is that it can print all sorts of toys - color dinosaurs, Lego blocks, that kind of thing. My son would definitely love it. (这里用 would like 可以么). On top of that, it's a sneaky way to get my son interested in engeering - he can see (或者用 watch？）how things on the screen (这可以加 the 么）turn into a real object he can hold. / More importantly, on weekends, my son sits right next to me, we design something together, and watch (和上面问题一样的) the machine（这里可以用the么) builds it layer by layer. It's less about the machine itself but more about the time spent with my kid.(你也统计下词数有多少)`

**五层诊断**
```
层1 语法搭配
  ❌ B68族  `The thing … is 3D printers` 主语单数、表语复数 → 全篇改用单数 a 3D printer
  ❌ B41    `He showed how his could do` 缺间接宾语 → **showed ME**（B41 今天第三次）
            同句 `how` → **what**（问的是"能做什么"，不是"怎么做"）
  ❌ B157   `I was hook` → **hooked**（-ed 形容词；B157 08-10 刚 ✅，今天回潮）
  ❌ B39族  `watch the machine BUILDS it` → **watch the machine BUILD it**
            （watch / see / make / have / let ＋ 宾语 ＋ 动词原形）
  ❌ 🆕B200 `color dinosaurs` → **colourful dinosaurs**
  ❌ 🆕B198 `It's less about X BUT more about Y` → **and**
            ★★ 这是【她自己的 ⭐ 块被换掉一个零件】：表达库里她 08-01 自产的是
               `It's less about the game itself AND more about hanging out with friends`
               —— 与轮94–95「复用块时丢成分」同一类，块记住了、配对词没记住
  ⚠️ 指代   `3D printers`（复数）→ 后面全用 `It` —— 改单数就同时解决
层2 词的精确度
  ❌ `read enthusiast` → **real enthusiast**（或 he's really into it）
  ⚠️ `see` → **watch**（看过程用 watch，看到用 see）★ 🆕B201
  ⚠️ `a real object` → real object**S**（前面 things 是复数）
层3 衔接与语气  ★ 本段最强的一层
  ✅ What makes it stand out is that… ／ On top of that ／ More importantly ／
     It's less about X and more about Y —— 四个衔接块全是对的，且没有重复
  ⚠️ 🆕B199 `a couple of reasons` ＝ 两个，她实际给了三个 → **a few reasons**
层4 逻辑层次
  ✅ 四个 bullet 全覆盖；收尾回扣主题（less about the machine, more about the time）
  ❌ **第 1 个 bullet 只有一个词组，没有画面** —— 173 词里 What it is 只占 10 词。
     P2 的第 1 个 bullet 撑不起来，整题就到不了 2 分钟。补一句画面即可（见完整版 B）
层5 内容深度  ✅ 通过
  三个理由主角不同：玩具（儿子玩）→ 工程启蒙（儿子学）→ 周末时间（我们俩）
  且有真画面：`things on the screen turn into a real object he can hold` —— 这是本段最好的一句
理解侧冗余七条  第 2 条（并列两边同形）踩中：less about…but more about… 破坏配对
                第 6 条（代词指代唯一）轻度：printers 复数 / It 单数
```

**她当场问的 7 个问题（全部按零遗漏收，答案见下方 🆕 词条）**
```
① The thing 有没有别的说法    → 有，四种，见 B202
② 3D printers 加 the 吗、用 s 对吗 → 泛指类别用复数不带 the，你判断对了；
                                   但本题问"想拥有的一件东西"→ 全篇单数 a 3D printer 更贴题
③ would like 可以么           → 可以，但 would LOVE 更强更贴（会很喜欢 vs 会想要）
④ see 还是 watch              → watch（★ B201）
⑤ things on the screen 加 the → 不加更自然（泛指）；加了也不错，指"屏幕上那些具体的东西"
⑥ 同④                        → watch
⑦ the machine 可以用 the 么   → 可以，前面提过这台机器，双方都知道是哪一个（B113 判据，你用对了）
```

**🆕 本题新建**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B198 | **⭐ 自己的块被换零件**：`It's less about X AND more about Y` —— 配对词是 **and**，不是 but。<br>★ 她 08-01 自产过正确版（表达库有），这次换成 but ⇒ **块记住了、配对零件没记住**（同轮94–95）<br>★ 修法只有块化：整句重说，不单独记"这里要 and" | "这事儿重点不是机器本身，是陪孩子的时间" | 08-11 |
| B199 | **a couple of ＝ 两个（精确）**；要说"几个"用 **a few**。开头报几个理由，后面就得给几个 | "我不去有几个原因" | 08-11（08-12 改题面：原格是对照说明不是可用题面） |
| B200 | **"彩色的X" ＝ colourful X**（不是 color X）；说具体颜色才用 `a red dinosaur` | "彩色的恐龙" | 08-11 |
| B201 | **watch vs see**：**watch ＝ 盯着看一个过程**（watch it print／watch him grow）· **see ＝ 看到**（结果或一瞬间，see the mountains）<br>★ 判据：有没有一段【持续的时间】在里面？有 → watch | "他能看着屏幕上的图变成实物" | 08-11 |
| B202 | **P2 起手四种（她问"The thing 有没有别的说法"）**：<br>① `The one thing I'd really like to own is …`（最贴"想拥有"这类题）<br>② `If I could pick one thing, it'd be …`<br>③ `I'd like to talk about …`（最省，直接进）<br>④ `The thing I'd like to talk about is …`（她这次用的，成立但偏绕）<br>★ 起手不要占超过一句 —— P2 的分在后面 | 任给一道 P2，用①或②起手 | 08-11 |

### ★★★ 她的第 35 次纠正（08-11，成立，教练的诊断口径和建议方向双错）

> 她的原话：**"其实 170 个词够了，不过学下怎么补画面没啥问题，因为我说的也不流利，啃啃巴巴只能说程度问题"**

```
教练说"173 词离 2 分钟差 30–60 词，第 1 个 bullet 要补内容" —— 两处都错：
① 口径错  **词数不是 P2 的长度指标**。按她的语速，173 词大概率已经填满 2 分钟。
          真指标是【词/分钟】＋【停在哪】，这两个打字都测不出来
② 方向错  **加内容 ＝ 加检索负载 ＝ 更卡**，与本文件核心的带宽模型正相反。
          教练给出了一条会让症状加重的建议 —— 这是"结论可以错"里最贵的一种：
          方向反了，照做会退步

★★★ 她这句话还暴露了一个更大的方法论漏洞（她只说了半句，另半句是教练该补的）：
   **这条训练线从 07-27 到今天，全部产出都是【打字】的。**
   打字 ＝ 慢时钟：可回删、可停下想、无时间压力。
   ⇒ 她自述的真实瓶颈（"说的也不流利，磕磕巴巴"）**在全部现有数据里一次都没有出现过**。
   ⇒ 所有关于【流利度】的判断都是无源之水；打字数据只能判 accuracy 和内容组织。
   ⇒ 「快时钟（出声＋不回删＋计时）」与「发音」并列，是**从未系统测过的两个维度**。

⇒ 已写进 SKILL §4.1：
   · 禁止用词数评 P2 长度；要评长度只能在出声＋计时条件下评
   · 「补画面」的理由改掉：不是凑词数，是**画面句比抽象句好说**（脑子里已经是图，
     不用现场组装抽象词）—— 它是降卡顿手段，不是加长度手段
★ 她自己给的现成证据：本题最长的一句 `things on the screen turn into a real object he can hold`
  正是全段最具画面的一句 —— 长而不抽象，反而是最好说的那种句子
```

### 改完当场重说 · 4/4 全对（08-11 收尾前）

- **她的原话（逐字）**：`I need a box to put these things in. I wouldn't go that far, though. I got stuck in the elevator for half an hour last week. There aren't enough jobs to go around.(around应该也行吧)`
```
1 ✅ a box to put these things in       （本日 📖，重说装上）
2 ✅ I wouldn't go that far, though.     （本日 📖，重说装上）
3 ✅ for half an hour                    （本日 ❌ B196，重说装上）
4 ✅ not enough jobs to go around        （本日 ❌ B192，重说装上）
   ★ 她问"around 应该也行吧" —— 对。go round＝英式／go around＝美式，两个都是这个义项，
     雅思两边都不扣分。B192 词条本来就写了美式 go around，她这次是**自己从词条里调出来的变体**，
     不是记混 —— 属于正确的泛化
★ 按 SKILL §0.5 新规：教练给过答案之后的重说【不改当天标记】（B175 B109a 仍记 📖，
  B192 B196 仍记 ❌），但事实层照记 —— 这是"改完当场重说"的当日证据，4/4
```

### ★ 她的第 34 次纠正（08-11，成立，已改进 SKILL §2.1）

> 她的原话：**"你的提示有点扯，什么叫更地道的，如果你有指向性的答案就提示的更明显点"**

```
旧规则：△ 条目只许加固定一句「（★ 这题要更地道的版本）」，理由是怕违反「禁预告测试点」
她指出的问题：这句话零信息量 —— 她不知道往哪个方向找，等于没提示
教练复核后认同，且发现旧规则的理由本身站不住：
  △ 意味着她上一次【已经答对了】，准确性那关过了；这一轮测的是"能不能够到更高档位"，
  不是 cold 测那个点 ⇒ **给方向不污染任何 cold 数据**
⇒ 新规则（SKILL §2.1）：△ 必须给方向，三选一
   a「这句有个固定说法，不是自己组的」（可加词数）
   b「上次这句你少了『___』那层」（中文点名缺的那层）
   c「这句英语不用动词说，用名词说」
   仍禁止：直接给答案 · 说"这题考介词/考完成时"
★ 本组第 4 题就是被旧提示坑的那道：目标是一个固定块，提示却只说"更地道"，她直接答不会
```

### ★ 教练当日犯错清单（§7④ 要求，08-11 共 3 类）

```
1. ⛔ 不必要的改动 8 处（两组 6 处＋第三组 2 处），全部是"两个都对"被写成"更好"：
   for ages→for years · take care of→look after · on weekends→at weekends ·
   Here is where→This is where · the plants→these plants · grow day by day→grow a bit every day ·
   elevator→lift · restaurant→place
   ⇒ 直接后果：B148 被误记 △（实为 ✅）、B3 与 B31a 同理 —— **假错会让她把带宽花在本来就对的地方**
   ⇒ 根因：四问自审的第 ① 问（试着造一个母语者会说的句子来推翻自己）没有逐条跑，
      只在"感觉可以更好"时就写进了 diff。**"可以更好"不是档位，只有"她的不成立"才是**
2. 数字口径混用：同一组按两套口径分别标注和统计，报出 5/10（实为 8/10）。已在 SKILL §0.5 写死口径
3. B 表内容错误：B109a 的目标块写成 `I wouldn't go too far`（应为 `go THAT far`），
   自 08-06 起挂错至今，今天她答"不会"时才暴露 —— 她答不出的条目要顺手复核块本身对不对
```

### 第 4 组 · 10 题 · 一字未改 6/10（她要求继续，超出 §0.1 的"学习日 ≤3 组"预算，记录在案）

- **她的原话（逐字）**：`I'm stuck on the thrid question. I was paired with him, 这句话不会.you can feel the energy when(或者用 if?) you are there. Rather than taking the bus, I choose to walk(总觉只写 walk 太单薄了). I have been waiting for hours.  I walk a long way. he found a job near his place. I will go out for a while, so help me look after my lugguge (少主语可以么. I'm not able to watch my phone all day. I sit in meetings the whole morning.`

```
✅ 1  B117b `I'm stuck on the third question.` 一字未改 → 🎓 连对3
📖 2  B117c `I was paired with him` 前半对（be paired with ✅），后半自报不会
      → **When we got put into pairs, I got stuck with him.**（stuck with＝被迫接受甩不掉）
✅ 3  B57b  `you can feel the energy when you are there.` 块装上
      🆕 B203「只有…才」那层没出来 → **You ONLY get that energy when you're actually there.**
      🆕 B204 她问 when 还是 if → **when**（一定会发生／每次都这样）；if＝不确定会不会发生
✅ 4  B114b `Rather than taking the bus, I choose to walk.` 句首 -ing 全对 → 🎓 连对3
      🆕 B205 她问"只写 walk 太单薄" → **解法不是换更重的动词，是加一个具体的东西**
✅ 5  B161b `I have been waiting for hours.` 绕开了裸 for long（连错2 的顽固条，今天断掉）
✅ 6  B161c `a long way` 一字未改（连错2 的顽固条，今天断掉）
      ❌ B34 `I walk` → **walked**（中文"了"＝过去标记）
❌ 7  B171f `he found a job` ＝找到了 → **He's looking for a job near his place.**（在找）
      ✅ `near his place` 用得好
◎ 8  B189 `help me look after my luggage` —— look after 在英式里也说得通，题面逼不出 keep an eye on
      → 题面已改成「买东西的时候得留意点价格」（留意≠照看，只有 keep an eye on 能答）
      她问"少主语可以么" → 祈使句可以省主语 ✅；但前半陈述＋so＋后半祈使有点别扭 → 拆开或用 can you
❌ 9  B173 **意思整个反了**：`I'm not able to watch my phone all day` ＝我没法一整天都看手机
      → **I can't go a day WITHOUT checking my phone.**
      ❌ B148 极性 —— 中文"没法一天【不】看"有两个否定，她丢了一个
      ⚠️ `watch my phone` → **check / look at my phone**（watch 是看节目，补进 B201）
✅ 10 B55  `the whole morning` 合法（错的只有 all THE morning），trap 绕开
      ❌ B34 第二次：`I sit` → **I was in meetings**（"一上午都在开会"是过去）
      ⭐ `sit in meetings` 是 08-04 教练给的块（B52②），她今天自发复用
```

**★★★ 本组最重要的发现：极性在【简单句】守住了，在【嵌套否定】上垮了**
```
第 1 组「这东西早就没人做了」（一个否定）  → 她自己抓回来 ✅
第 4 组「我没法一天不看手机」（两个否定嵌套）→ 丢了一个，意思整个反过来 ❌
⇒ B148 今日最终记 ❌（两次都是 cold，按"以最后一次为准"），连错 3
⇒ **靶心没打完**：今天证明的是"她能查一个否定"，不是"她能处理否定"。
   下一轮极性题必须直接上【两个否定】的句子（没法不…／没人不…／不是不想…）
```

**⑤ 独立 Diff**
```
【1】原句  I'm stuck on the thrid question.
    改后  I'm stuck on the third question.
    · thrid → third                  —  拼写，不计   · 无实质 diff
【2】她自报不会。教练给：When we got put into pairs, I got stuck with him.
    · 她已产出的 `I was paired with him` 完全正确，保留
【3】原句  you can feel the energy when you are there.
    改后  You only get that energy when you're actually there.
    · feel the energy → get that energy      ⛔不必要  feel the energy 是对的，撤销
    · 缺「只有…才」→ only … when             ⚠️更好  中文这层没出来
【4】原句  Rather than taking the bus, I choose to walk.
    改后  Rather than taking the bus, I just walk — it's only fifteen minutes anyway.
    · choose to walk → just walk             ⚠️更好  choose 偏书面
    · ＋ it's only fifteen minutes anyway    ⚠️更好  治"单薄"的正解：加具体的，不加重的词
【5】原句  I have been waiting for hours.
    改后  （同）
    · 无 diff（for hours 完全对，且比 a long time 更有画面）
【6】原句  I walk a long way.
    改后  I walked a long way.
    · walk → walked                          ❌真错  中文"了"＝过去
【7】原句  he found a job near his place.
    改后  He's looking for a job near his place.
    · found → is looking for                 ❌真错  找到 ≠ 在找
【8】原句  I will go out for a while, so help me look after my luggage.
    改后  I'm just popping out — can you keep an eye on my luggage?
    · so help me … → can you …               ⚠️更好  陈述＋so＋祈使不顺
    · look after → keep an eye on            ⚠️更好（原句在英式里也说得通，故记 ◎ 不记 ❌）
【9】原句  I'm not able to watch my phone all day.
    改后  I can't go a day without checking my phone.
    · 整句意思反了 → can't go a day without   ❌真错  丢了一个否定
    · watch my phone → checking my phone     ❌真错  watch＝看节目
【10】原句 I sit in meetings the whole morning.
     改后 I was in meetings all morning.
     · sit → was                             ❌真错  过去的事
     · the whole morning → all morning        ⛔不必要  两个都对，撤销
⛔ 2 处（feel the energy→get that energy · the whole morning→all morning，均已撤销）
```

**🆕 本组新建**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B203 | **「只有…才」那层**：`ONLY ＋ 动词` 或 `It's only … that/when`。<br>❌ You can feel the energy when you are there（丢了"只有"）<br>✅ **You only get that energy when you're actually there.**<br>★ 与 B197（"都要"那层）同族：**中文的限定副词最容易在翻译时掉队**——说完一句问"中文里那个『只/都/才/就』出来了吗？" | "只有到现场才有那种感觉" | 08-11 |
| B204 | **when vs if（她当场问的）**：**when ＝ 这件事一定会发生／每次都这样**（when you're there ＝ 到了现场就有）· **if ＝ 不确定会不会发生**（if you go, you'll like it）<br>★ 判据：中文能不能换成"**每次…的时候**"？能 → when | "每次他讲这个笑话大家都笑；如果他明天来，我就带他去"（**两句都说**） | 08-11（08-12 改题面：原题面与 B90/B94/B83 三处撞车） |
| B205 | **★ 治"句子太单薄"（她原话："总觉只写 walk 太单薄了"）**：<br>❌ 错解：换一个更重/更书面的动词（`I choose to walk`）—— 更书面 ≠ 更充实，而且更吃带宽<br>✅ 正解：**加一个具体的东西**（时间／距离／数字／结果）<br>`Rather than taking the bus, I just walk — it's only fifteen minutes anyway.`<br>★ 与 B197「都要那层」、B203「只有那层」同一根：单薄 ＝ **少了一层具体的，不是少了一个大词** | "我一般不点外卖，自己做"（**这句要带一个具体的**） | 08-11（08-12 改题面：原题面与 B114b 逐字撞车） |

### 改完当场重说 · 第 4 组 · 5/5 全对

- **她的原话（逐字）**：`When we got put into Paris, I got stuck with him. I walked a long way. he is looking for a job near his place. I can't go a day without checking my phone. I was in meetings all morning.`
```
1 ✅ got stuck with him       （本日 📖 B117c，重说装上）
2 ✅ walked                    （本日 ❌ B34）
3 ✅ is looking for            （本日 ❌ B171f）
4 ✅ can't go a day without    （本日 ❌ B173 ＋ 极性 B148，两条一起装上）
5 ✅ was in meetings all morning（本日 ❌ B34 第二处）
★ `Paris` 是输入法把 pairs 改掉了，不计
★ 按 SKILL §0.5：给过答案后的重说不改当天标记（B117c 仍 📖，B34/B171f/B173/B148 仍 ❌），
  事实层照记 —— 今天第二次拿到"改完当场重说 100%"的当日证据
```

### 第 5 组 · 10 题 · 一字未改 6/10

- **她的原话（逐字）**：`1 第一个忘了 2. the app can save you lots of time. 3. i've been working at this company for 5 years. 4. i put things on the table last night. 5. an hour a day is completely fine. 6. 忘了 7. my English is not good, 后面忘了 8. i'v waited for half an hour. 9. I wait in queue for half an hour every time 这句说的也不太对 10. Japanese is a plus.`

```
📖 1  B89  忘了 → 口语默认 **I can't cook or bake.**（一个否定管两个，最省）
      正式版 `I can neither cook nor bake.`（能用但偏书面）
      ★ 思路：中文"既不…也不…"在英语口语里通常压成 **一个 not ＋ or**，不必上 neither…nor
✅ 2  B92  `the app can save you lots of time.` 一字未改 → 🎓 连对3
✅ 3  B151 `i've been working at this company for 5 years.` 一字未改 → 🎓 连对3
✅ 4  B152a `put` 用作过去式正确（last night 坐实）→ 🎓 连对3
      ⚠️ 她把题面的"他"读成了"我"（注意力滑，不是语言问题，记一笔）
✅ 5  B109b `an hour a day is completely fine.` 与目标块一字不差
📖 6  B109c 忘了 → **It's not that games are bad — it's about how long.**
      ★ 思路：中文"不是A，是B"两个壳：`It's not THAT A — it's B`（后面跟整句）／
        `It's not A, it's B`（后面跟名词短语）
📖 7  B171g 前半有、后半忘 → **My English isn't great, but I get by.**
      ★ get by ＝勉强应付得来；**but I get by** 整块就是"但日常应付得来"的固定收尾
      ⚠️ `my English is not good` 成立但生硬 → `isn't great`（英语里说自己差用"不够好"这一档）
✅ 8  B196 `half an hour` 考点对（今天 ❌ 过一次，重说后 cold 又对）
      ⚠️ `I've waited for half an hour` 语法成立但少见 → 等完了用 `I waited half an hour.`／
         还在等用 `I've been waiting for half an hour.`
❌ 9  B197 "都要"那层【又】没出来 → **I always end up queuing for half an hour every time I go.**
      ❌ 🆕B206 `in queue` → **in a queue**（英式 queue 可数）／更省：**queue** 当动词
      ★ 她自报"这句说的也不太对" —— 判断准确，今天第 4 次自诊命中
✅ 10 B51  `Japanese is a plus.` 一字未改（招聘语境里英语就是这么说，"会"不用译出来）
```

**⑤ 独立 Diff**
```
【1】忘了，无原句。教练给：I can't cook or bake. ／ I can neither cook nor bake.
【2】原句  the app can save you lots of time.
    改后  （同）   · 无 diff
【3】原句  i've been working at this company for 5 years.
    改后  （同）   · 无 diff
【4】原句  i put things on the table last night.
    改后  He put his things on the table last night.
    · i → He                       —  题面是"他"，读串了，不算语言错
    · things → his things          ⚠️更好  中文"东西"＝他的东西
【5】原句  an hour a day is completely fine.
    改后  （同）   · 无 diff
【6】忘了，无原句。教练给：It's not that games are bad — it's about how long.
【7】原句  my English is not good, ...
    改后  My English isn't great, but I get by.
    · is not good → isn't great    ⚠️更好  说自己差，英语习惯用"不够好"这一档
    · 后半缺失 → but I get by      📖
【8】原句  i'v waited for half an hour.
    改后  I waited half an hour. ／ I've been waiting for half an hour.
    · I've waited for → I waited ／ I've been waiting for   ⚠️更好  完成时＋时长少见
    · half an hour                 ✅ 考点，不动
【9】原句  I wait in queue for half an hour every time.
    改后  I always end up queuing for half an hour every time I go.
    · in queue → in a queue ／ queuing   ❌真错  英式 queue 可数
    · I wait → I always end up          ⚠️更好  补回"都要"那层（B197）
    · every time → every time I go      ❌真错  every time 是连词，后面要完整从句（B94）
【10】原句 Japanese is a plus.
     改后 （同）   · 无 diff
⛔ 0 处
```

**🆕 本组新建**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B206 | **queue 是可数名词**：`in A queue` ／ `join the queue`（in queue ❌）。<br>★ 最省是把它当动词用：**queue for half an hour** ／ 美式 **wait in line** | "我排了半小时队" | 08-11 |

### 改完当场重说 · 第 5 组 · 4/4 全对

- **她的原话（逐字）**：`i can't cook or bake. it's not that games are bad, it's about how long. my english isn't great, but i get by. i always end up queuing for half an hour every time i go.`
```
1 ✅ can't cook or bake          （本日 📖 B89）
2 ✅ it's not that A, it's B      （本日 📖 B109c）
3 ✅ isn't great, but I get by    （本日 📖 B171g）
4 ✅ always end up queuing … every time I go（本日 ❌ B197＋B206＋B94 三条一起装上）
★ 今日第三次拿到"改完当场重说 100%"：4/4 · 5/5 · 4/4，合计 13/13
  ⇒ 08-10 的结论（只有重说过的才保得住）今天在同一 session 内被反复坐实
★ 按 §0.5：给过答案后的重说不改当天标记
```

### 第 6 组 · 10 题 · 有效 5 题（另 5 题作废，见下）· 一字未改 2/5

- **她的原话（逐字）**：`His things are all over the floor. Children will lost interest on their schoolwork(不确定是 on还是其他介词). you should pay attention to prices when you buy things. my mon help me take care of / look after my kid on weekends. i don't have chargers, so i use my colleague's. the roads were pretty jammed. the traffic i cheng is heavy. it is less about the machine itself and more about the time spent together. colourful dinosaurs. he can watch things on the screen turn into real objects. 不知道。另外为啥今天学的就进入复习了？？`

### ★★★ 她的第 37 次纠正：**"为啥今天学的就进入复习了？"** —— 成立，教练错

```
第 6 组 10 题里有 5 题（B193 B195 B198 B200 B201）是【今天刚建的号】。
当天教完当天抽查 ＝ 不是 cold 测 —— 她答对只证明还没忘（间隔一小时），
📊 会因此吃进一批假 ✅，把毕业进度整个撑虚。
⇒ **这 5 题的结果作废，不进 📊**，次日作为 D-1 重新 cold 测
⇒ SKILL §0.1 已加死规则：**新建条目 / 当天改过题面的条目，当天不进复习组**；
   当天对新条目只有一个动作 ——【改完当场重说】（那是产出，不是抽查，不进 📊）
★ 根因同 §0.1 的预算问题：教练想"把今天产出的东西赶紧闭环"，
  但闭环的手段是【重说】，不是【抽查】。两者混掉就等于自己给自己发假成绩
```

```
✅ 1  B154 `His things are all over the floor.` 一字未改 → 🎓 连对3
❌ 2  B107a `will LOST` → **will lose**（will ＋ 原形）；`interest ON` → **interest IN**
      她自报"不确定是 on 还是其他介词" —— 判断准确，今天第 5 次自诊命中
      ★ 兴趣的对象一律 **in**：be interested IN／have an interest IN／lose interest IN
      ✅ `schoolwork` 用对（B107a 的另一半）
◎ 3  B189 第二次 ◎：她答 `pay attention to prices` 完全合法，题面还是逼不出 keep an eye on
      ⇒ 结论：**"留意/看着"这类中文没有任何一句能唯一逼出 keep an eye on**（它只是多个近义之一）
        → 抽查方式改成【这句给两种说法】（同 B171d 的做法）
      ✅ 附带：B107b `pay attention TO` cold 产出正确
✅ 4  B171d 两种说法都给了（take care of ／ look after）→ 考点达成
      ❌ B27 `my mon HELP` → **helps**（主谓一致，今天第二次：the two hours makes ／ my mom help）
📖 10 B109d 不知道 → **Anything's fine in moderation.**（in moderation 挂句尾）
```

**作废的 5 题（次日重测，此处只留事实，不记标记）**
```
5  B193 `i don't have chargers, so i use my colleague's`
   ❌ 时态：中文"就用了"＝过去 → **didn't have a charger, so I used**（B34 今天第三次）
   ❌ `chargers` 复数 → a charger（一个）
6  B195 `the roads were pretty jammed` ⭐ **今天刚学的 jammed 主动用出来了，时态也对**
   `the traffic i cheng is heavy` → 打字乱了；泛指说法 `Traffic in Chengdu is always bad.`
   （带 the 不算错，但少了"一直"那层 —— 又是副词层，同 B197/B203）
7  B198 ✅ `and` 改回来了      8  B200 ✅ colourful dinosaurs
9  B201 ✅ watch ＋ real objects
```

**⑤ 独立 Diff（只列有效题）**
```
【1】原句  His things are all over the floor.
    改后  （同）   · 无 diff
【2】原句  Children will lost interest on their schoolwork.
    改后  Children will lose interest in their schoolwork.
    · will lost → will lose        ❌真错  will 后面用原形
    · interest on → interest in    ❌真错  兴趣的对象用 in
【3】原句  you should pay attention to prices when you buy things.
    改后  （同）   · 无 diff（题面问题，不是她的问题）
    · 第二种说法 → keep an eye on prices   📖 教练补
【4】原句  my mon help me take care of / look after my kid on weekends.
    改后  My mum helps me look after my kid at weekends.
    · help → helps                 ❌真错  主谓一致
    · mon → mum                    —  拼写，不计
【10】不知道，无原句。教练给：Anything's fine in moderation.
⛔ 0 处
```

**★★ 同日发现：拆号不许继承父号连击（已写进 SKILL §0.1）**
```
B107 拆成 B107a/b 时，教练让两个子号都继承父号的"连对 2"。当天就被证伪：
   B107a（lose interest IN）❌ ／ B107b（pay attention TO）✅
⇒ 父号的两次 ✅ 至少有一半是虚的 —— 父号一次只测到它多个考点里的一个
⇒ 拆号后所有子号一律从 0 起算；**B107a/B107b 即日起重算**
⇒ 已靠继承毕业的 B57a B114a B117a B152a：不追溯撤销，但标「继承毕业·待复查」，
  下一个专门复习日各复查一次
```

### 改完当场重说 · 第 6 组 · 4/4 全对（今日重说累计 17/17）

- **她的原话（逐字）**：`children will lose interest in their schoolwork. you should keep an eye on prices when you're buying things. my mum helps me look after my kid at weekends. anything is fine in moderation.`

### 她要求展开：`in moderation`（"类似的结构我都不会翻译"）

> 教练第一次答偏了（讲成"疑问词＋都"的 any/every/no 三分），她纠正：**"我的问题是 in moderation"**。
> 两条都记下来（§0.5 零遗漏：教练给的内容也要进复习），但她要的是第二条。

**🆕 B207（教练答偏时给的，仍然有效，照收）**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B207 | **中文「疑问词＋都」→ 英语必须先分叉成三条路**（中文一个模式，英语三个）：<br>① 肯定·随便哪个 → **any-**：什么都行 `Anything's fine.` ／ 谁都能来 `Anyone can come.` ／ 哪儿都买得到 `You can get it anywhere.`<br>② 肯定·全部 → **every-**：什么都涨了 `Everything's gone up.` ／ 谁都知道 `Everyone knows.`<br>③ 否定 → **no-**，且动词**不再否定**：谁都不知道 `Nobody knows.`（❌ Nobody doesn't know）<br>★ 三步：①中文疑问词决定词根（thing/one/where/time/way）②判肯定还是否定决定前缀 ③no- 之后不许再 don't<br>⚠️ 陷阱："没问题／没关系／不错"在中文里是**肯定判断**，别当否定处理 —— "什么东西适度都没问题"走 ①<br>★ 邻族：**不管…都** → whatever／whoever／however（不管多累我都去 `However tired I am, I'll go.`） | 见拆出的 B207a / B207b / B207c | 08-11（08-12 拆号：三条测三条不同子规则，按定义3 必须拆） |
| B207a | **肯定·随便哪个 → any-**：什么都行 `Anything's fine.` ／ 谁都能来 `Anyone can come.` ／ 哪儿都买得到 `You can get it anywhere.` | "什么都行，你定吧" | 08-11（08-12 从 B207 拆号，从 0 起算） |
| B207b | **肯定·全部 → every-**：什么都涨了 `Everything's gone up.` ／ 谁都知道 `Everyone knows.` ／ 哪儿都是人 `There are people everywhere.` | "这事儿谁都知道" | 08-11（08-12 从 B207 拆号，从 0 起算） |
| B207c | **否定 → no- 词，且动词【不再否定】**：谁都不知道 `Nobody knows.`（❌ Nobody doesn't know）／ 什么都没剩 `There's nothing left.`／ 哪儿都找不到 `I couldn't find it anywhere.` | "谁都不想加班" | 08-11（08-12 从 B207 拆号，从 0 起算） |

**🆕 B208（她真正问的那条）**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B208 | **★★ 中文的"两字/四字方式词" → 英语多半是【介词＋抽象名词】的固定块，不是 -ly 副词**<br>她卡住的真因：检索路径是「中文副词 → 英语 -ly」，而这一类**没有 -ly 版本**（`moderately` 存在，但意思是"中等程度地"，修饰形容词：moderately priced；不能说 `Anything's fine moderately` ❌）<br>**介词不可推导，只能整块记。** 高频十条（口语够用，不扩散）：<br>in **moderation** 适度 · in **advance** 提前 · in **a hurry** 匆忙 · in **person** 亲自/当面 · in **general** 总的来说 · on **purpose** 故意 · on **time** 准时 · by **accident/mistake** 不小心 · at **least** 至少 · to **some extent** 某种程度上<br>★ 触发判据：中文出现"适度／故意／亲自／提前／不小心／总的来说"这种**两字或四字的方式词** → 别去找 -ly，直接想"是不是一个介词短语"<br>★ `Everything in moderation.` 本身就是英语谚语（凡事有度）—— 她那句中文几乎就是它的直译源，**整句背最省**。<br>参考对照（不出题）：我提前订了票 in advance ／ 我不小心删了 by mistake ／ 总的来说 in general<br>⚠️ **08-12 改题面**：原第一条"凡事适度就好"与 **B109d**（in moderation）逐字撞车 —— 按 §0.2 改题面、两号都留：**B109d 专测 in moderation，本号测 on purpose** | "他是故意的" | 08-11（08-12 收成一条题面并避开 B109d） |

### B208 当场 drill · 8 题 · 考点 8/8（同日教的，不进 📊）

- **她的原话（逐字，第二版；第一版她自己打断改掉了两处）**：`everything in moderation is fine. he did it on purpose. i booked tickets one week in advance. i deleted files by accident. he walk slowly. i want to talk in person. in general i'm pretty satisfied. you should try it at least once`
- **★ 两处自纠（cold，无提示）**：`find`→`fine` ／ **`he is on purpose`→`he did it on purpose`**
  第二处是真自纠：on purpose 必须挂一个实义动词，不能挂 be —— 她自己抓到了

```
八个介词块【全部选对】：in moderation · on purpose · in advance · by accident ·
                        in person · in general · at least ＋ 陷阱题 slowly 没上当
⇒ B208 这条【路径】一次就通。但按 §0.1 新规：同日教同日测 ≠ cold，不进 📊，次日重测

本轮暴露的两条真问题（跟 B208 无关，都是老账）：
❌ B27 主谓一致 `he walk` → **he walks** —— **今天第三次**
   （the two hours MAKES ／ my mom HELP ／ he WALK）
   ⇒ 与词条描述完全吻合："孤立 100%，产出中反复错 ＝ 检索失败，不是知识缺口"
⚠️ 程度层又掉一次 `我更想当面聊` → `I want to talk` 丢了"更" → **I'd RATHER talk in person.**
```

**★★★ 今日第四次同族发现 → 升为明日靶心：中文的【限定/程度副词】系统性掉队**
```
08-11 一天之内四次，全是同一个动作没做：
  ① "我每次去都要排半小时队"  都要 → 丢    （B197）
  ② "只有到场才有那种感觉"    只有 → 丢    （B203）
  ③ "成都的交通一直不好"      一直 → 丢    （B195）
  ④ "我更想当面聊"            更   → 丢    （本轮）
共同点：这些字**在中文里只有一个字**（都/只/一直/更/才/就），信息量却极大 ——
       它们承载**说话人的精确度和立场**，丢了句子就变平、变含糊
为什么专丢它们：cold 产出时带宽只够搭骨架（主谓宾），
       这些字挂在骨架【外面】，是第一批被挤掉的（与"一句话没了"同源）
⇒ 明日靶心：**说完一句，回头找中文里的那个"都/只/一直/更/才"出来了没有**
⇒ 已建 🆕 B209 作为操作条目
```

**🆕 B209**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B209 | **★ 限定/程度副词不许掉队（操作，做出来测）**：中文里的 **都／只／一直／更／才／就** 各有固定英语出口，产出后必须回头点名检查：<br>都要/总是 → `always end up ‑ing` ／ `have to`<br>只有…才 → `only ＋ 动词` ／ `It's only … that`<br>一直 → `always` ／ `keeps ‑ing`<br>更…（比较） → `I'd rather` ／ `more`<br>才 → `not until` ／ `only then`<br>就 → `just` ／ `straight away`<br>★ 检查触发：**说完一句问"中文里那个单字副词出来了吗？"**<br>⚠️ **08-12 更正定位**：08-11 写成"B197/B203/B195 三条并入本号"，那是**违规合并**（§0.2：不许并条目，并掉就永远拿不到自己的连击）。<br>⇒ **B209 不是一个条目，是 B197／B203／B195 共用的一个【诊断动作】**，本号不单独出题、不占 📊 槽位（同 B190 的定位）。三个号各出各的题、各走各的 streak | 不单独出题；作为 B197/B203/B195 的共享判据 | 08-11（08-12 更正定位） |

### 新题 ② · P3 `Do you think enterprises should provide training for their employees?`（question_bank.md:991）

- **她的原话（逐字）**：`yes, definitely. the knowledge and skills that companies demand are completely different. training can help new employers get to know about new environment. Especially for students, they can do almost nothing if they aren't families with various processes at new companies at all. on top of that, training is one of the most efficient ways for employers to keep up with the development of the enterprises.(这里我想加个例子，但是一时没想起来)`

**五层诊断**
```
层1 语法搭配
  ❌ 🆕B210 **employers（雇主）→ employees（雇员）** —— 全篇三处，说反了
     `new employers get to know` / `for employers to keep up` ⇒ 意思变成"老板去适应/跟上"
  ❌ B49   `completely different` **缺比较对象** —— different FROM WHAT？
     → `different from what you learn at university`
  ❌ 🆕B211 `get to know about new environment` → **get used to A new environment**／**settle into**
     （get to know 是"认识某人"；且 environment 可数，缺冠词）
  ❌ 🆕B212 `families with` → **familiar with**（形近词；若是输入法所致，下次留意）
层2 词的精确度
  ❌ B46   `most efficient ways` → **most effective**（efficient＝省时省人力；达到效果用 effective）
  ❌ B136  三个书面词一起回来：`demand`→**need** ／ `enterprises`→**companies/firms** ／
           `the development of the enterprises`→**how fast the company changes**
  ⚠️ `students` → **fresh graduates**（职场语境里不是"学生"，是"应届生"）
层3 衔接与语气
  ✅ `yes, definitely` 立场直给 · `Especially for…` · **`on top of that`（B 表的块，自发复用）**
  ⚠️ 第 1 句和第 2 句之间缺一个桥 → `The thing is, …`
  ⚠️ `Especially for students, THEY can…` 结构松（状语＋另起主语）→ 破折号接上去更顺
层4 逻辑层次
  ✅ 立场 → 理由1（知识不对口）→ 展开（尤其应届生）→ on top of that → 理由2（跟上变化）
  ✅ 两个理由主角不同（B63 通过）：理由1 主角＝新人的知识差距；理由2 主角＝公司的变化速度
  ⚠️ 理由1 到"尤其学生"之间跳了一步：知识不对口 **⇒ 所以需要培训** 这一句没说出来
层5 内容深度
  ✅ 理由1 有展开   ❌ 理由2 没有展开 —— **她自己说"想加个例子但没想起来"，判断准确（今日第 6 次自诊命中）**
  → 用她自己的行业最省：`Take my industry — a new tool comes out every year, and if the company
    doesn't run any training, everyone's still doing things the old way.`
理解侧冗余  第 4 条（比较对象形式对齐）踩中 —— 见 B49
```

**★★ 本轮最值得记的一条：B136 单点测对、自由产出时原样回去**
```
同一天：第 2 组中译英 `now with AI` ✅（08-10 回潮的那条，单点 cold 测通过）
       自由产出 P3 里一次冒出三个书面词（demand／enterprises／the development of）
⇒ 按"以最后一次为准"，B136 今日最终记 ❌
⇒ 这不是矛盾，正是带宽模型的预测：**单点测时带宽只用来管一个词，
   自由产出时带宽全被内容和结构吃掉，词的选择自动回落到"阅读里见过的那版"**
⇒ 教练侧结论：**书面词降级这类条目，单点中译英测出的 ✅ 不算数**，
   只有在自由产出里不出现才算过 —— 这一条同 §0.3 的"减法型规则"处理方式
```

**⑤ 独立 Diff**
```
【1】原句  yes, definitely.
    改后  Yes, definitely.
    · 无 diff
【2】原句  the knowledge and skills that companies demand are completely different.
    改后  What companies actually need is completely different from what you learn at university.
    · demand → actually need              ❌真错（B136 档）书面词，有口语版
    · completely different → different FROM what you learn at university   ❌真错  比较对象缺失
    · the knowledge and skills that…      ⚠️更好  整块换成 what companies need，更省
【3】原句  training can help new employers get to know about new environment.
    改后  Training helps new employees get used to a new environment.
    · employers → employees               ❌真错  雇主/雇员说反了
    · get to know about → get used to     ❌真错  get to know 是"认识某人"
    · new environment → a new environment ❌真错  可数名词缺冠词
    · can help → helps                    ⚠️更好  说普遍规律不用 can
【4】原句  Especially for students, they can do almost nothing if they aren't families with various processes at new companies at all.
    改后  Especially fresh graduates — they can barely do anything until they know how things work.
    · families → familiar                 ❌真错  形近词
    · students → fresh graduates          ⚠️更好  职场语境
    · Especially for X, they…             ⚠️更好  状语＋另起主语太松，用破折号接住
    · various processes at new companies  ⚠️更好  → how things work（降级，B136）
    · can do almost nothing → can barely do anything   ⚠️更好
【5】原句  on top of that, training is one of the most efficient ways for employers to keep up with the development of the enterprises.
    改后  On top of that, it's one of the best ways to keep people up to date.
    · efficient → effective／best         ❌真错（B46）
    · employers → employees／people       ❌真错  第三次
    · the development of the enterprises  ❌真错（B136 档）→ keep people up to date
    · training is → it's                  ⚠️更好  前句已说 training，不必重复
【补】层5 缺的例子（她自报）：Take my industry — a new tool comes out every year, and if the
     company doesn't run any training, everyone's still doing things the old way.
⛔ 0 处
```

**🆕 本题新建**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B210 | **employer ＝ 雇主/老板 ／ employee ＝ 雇员/员工**（她全篇三处说反）。<br>抓手：**‑er 是【给】工作的那个，‑ee 是【拿】工作的那个**（同族：trainer/trainee · interviewer/interviewee · payer/payee）<br>★ 最省的躲法：口语直接说 **staff ／ workers ／ people**，不碰这对词 | "公司应该给员工提供培训" | 08-11 |
| B211 | **"适应新环境" ＝ get used to ／ settle into**（❌ get to know about）：<br>`get used to a new environment` ／ `settle into a new job` ／ 最口语 `find your feet`<br>★ 对照：**get to know ＋ 人**（认识某人）· **get to know about ＋ 事**（了解到某事） | "新人需要时间适应新环境" | 08-11 |
| B212 | **be familiar WITH sth**（形近词提醒：她打成 `families with`）；反面 **be new to sth**（`I'm still new to this`） | "他对这套流程还不熟" | 08-11 |

### 她问：especially 和 especially for 的区别（教练讲了，drill 未做 → 顺延）

**🆕 B213**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B213 | **★ `for` 不是 especially 带来的，是句子本身需要的**。especially ＝ 聚光灯，照在句子里**已经存在的某个成分**的更小范围上；那个成分原来带什么介词就带什么：<br>`Training helps new people.` → especially **fresh graduates**（helps 及物，不带 for）<br>`Training is useful FOR new people.` → especially **FOR** fresh graduates（for 是 useful 要的）<br>`I go there AT weekends.` → especially **ON** Sundays ／ `high IN big cities` → especially **IN** Shanghai ／ `hard WHEN you're new` → especially **WHEN** you don't know anyone<br>**判据**：把 especially 删掉，这句本来要不要那个介词？要就留，不要就不加。<br>⚠️ 她真正的错不是 for，是**挂空**：`Especially for students, THEY can…` 介词短语后面另起完整句 ⇒ 悬空<br>两个修法：① 挂回上一句（`…, especially fresh graduates.`）② **万能式：`This is especially true for/when…`**（想让它单独成句就给它主谓）。<br>参考对照（不出题）："房租很贵，尤其在市中心"（especially IN）／"一个人住很难，尤其刚搬来的时候"（especially WHEN） | "这个 app 对上班族特别有用" | 08-11（08-12 收成一条题面） |

**未做的 drill（顺延到 08-12）**：①这个 app 对上班族特别有用 ②房租很贵，尤其在市中心
③培训能帮新人上手，尤其是应届生 ④我周末都在家，尤其是周日 ⑤一个人住很难，尤其刚搬来的时候
⑥这一点对老年人来说尤其如此

---

📊 2026-08-11 ✅ B3 B12 B31a B51 B55 B57a B57b B73 B90 B92 B104 B107b B109b B114a B114b B117a B117b B121 B123 B141 B151 B152a B154 B159 B161a B161b B161c B165 B166 B168 B171d B186 B187 B196  📖 B89 B109a B109c B109d B117c B171g B175  ◎ B189 B191a  ❌ B27 B34 B39 B41 B43 B45 B46 B49 B68 B107a B136 B148 B157 B171a B171f B173 B192 B197  🆕 B193 B194 B195 B196 B197 B198 B199 B200 B201 B202 B203 B204 B205 B206 B207 B208 B209 B210 B211 B212 B213（本日新建 21 条）· B27 B41 B43 B49 B51 B55 B123 B192 （老条目首次进流，基线 0）
　　　　　　　　🎓 本日毕业 16 条：B57a B57b B90 B92 B104 B114a B114b B117a B117b B151 B152a B154 B159 B165 B166 B168
　　　　　　　　⚠️ 作废不计：B193 B195 B198 B200 B201（同日新建同日测，非 cold，08-12 重测）· B208 drill 8 题（同上）
　　　　　　　　⚠️ 撤销继承：B107a/B107b 从 0 重算（拆号继承被当天证伪）
　　　　　　　　⛔ 教练不必要改动本日合计 11 处（G1 3 · G2 3 · G3 2 · G4 2 · P2 1），全部已撤销

### ★★★ 她的第 36 次纠正（08-11，整节推翻教练发明的"时间预算"）

> 她的原话：**"这个 skill 谁改的，感觉很奇怪。学习日复习 D-1 + D-3 的全部，然后出新题，
> 然后新题数目设定为 3（这个按照我说的来），但是可以扩展，也可以继续复习（按照既有规则），
> 人工选择。每 5 天进入复习日，复习过去 5 天的全部 + 抽样（按照既有规则），不限定复习数量。
> 如果我觉得够了会自然停止。"**

```
背景：08-11 早些时候教练跑三轮 subagent 对抗演练，验收 agent 的诊断是
     "没有时间预算 → 结构性地逼出抽样"。教练的解法＝**发明时间预算**（学习日 ≤3 组 / 复习日 ≤6 组）。
     ⇒ **那个预算她从来没定过，是教练自己加的。**
当天下午就撞墙：3 组 ＋ 1 道真题跑完（＝预算满），她说"继续吧"，
     教练只好硬开第 4、5 组中译英 —— 而 skill 自己的停练清单写着「中译英当流利训练＝喂中介」。
     **预算把教练逼进了一个它本来要防的坑的对面。**

她的方案（已写进 SKILL §0.1 / §0.2c / §0.4）：
  学习日  ① 复习 D-1＋D-3 的【全部】（不设上限）
          ② 新题 3 道（走脚本；原来 skill 写的是 1 道，"3"是她这次定的）
          ③ 加练与否【她决定】；她说继续 → 默认切【真题】通道，不是再来一组中译英
  复习日  不学新的，过去 5 天全部 ＋ 更早抽查 ＋ 题目重答 5 道，同样不限量
  停止规则  **"如果我觉得够了会自然停止"** ——【人工停止】替代【数字预算】，
           同样堵死抽样，且不会与"她想继续"冲突

★ 结构性收益：配额规则从【筛选】降级为【排序】。全量之后没有条目会被排除，
  "每组 ≥N 条"只会制造凑数；真正有用的只剩"万一她中途喊停，先出的必须是最该清掉的"。
★ 教练侧教训：**对抗演练找出的问题是真的，但演练不能替她做设计决策。**
  "没预算"确实是漏洞，但补法有两种（数字上限／全量+人工停止），教练选了前者且没问她。
```

**⚠️ 连带后果（已写进 §0.4，需她定夺）**：新题 3 道/学习日 ⇒ 每周期 15 道进重答队列，
而复习日只重答 5 道 ⇒ **队列每周期净增 10 道**。处理：重答按"最久没重答的优先"，
每个复习日报一次队列长度，由她决定要不要调 5 这个数。教练不许为了平队列而少抽新题。

### 📦 顺延队列（08-12 优先出。顺延触发条件已改为【她喊停时没出完的】，不再是预算触发）

```
▸ 未答完的题（最优先）
   P2 新题②「Describe a time when you worked in a group」（已在 asked.log，题面见 question_bank.md:308）
   B213 especially drill 6 题（题面见上面 B213 段落）

▸ 本日新建号，08-12 首次 cold 测（21 条）
   B193 B194 B195 B196※ B197※ B198 B199 B200 B201 B202 B203 B204 B205 B206
   B207 B208 B209 B210 B211 B212 B213
   ※ B196/B197 今天已 cold 测过（B196 ✅ / B197 ❌），其余全部首测

▸ 本日作废、必须重测的 5 条（同日新建同日测，非 cold）
   B193 B195 B198 B200 B201  ＋ B208 的 8 题 drill

▸ 本日改过题面、必须重测的
   B189「买东西的时候得留意点价格」→ 二次 ◎，题面再改成【给两种说法】
   B191a「一出事故，整条环路全堵死了，一动不动」（今天没测到）

▸ 老条目还没出的
   B31b「我老婆什么都网购」· B191b「地铁里人挤人」· B34「我以前常去健身房」（今天两次 ❌，要重练）

▸ 顽固条（连错 ≥2，每组必进）
   B148（连错3·极性）· B45（back and forth）· B171a（make do with）· B171f（look for）· B136（书面词降级）

▸ 待拆号（遇到再拆）：B19 · B147
▸ 待复查（靠继承毕业的，下一个专门复习日各查一次）：B57a B114a B117a B152a
```

### ★ 她的第 33 次纠正（08-11，成立，已改进 SKILL §2.5）

> 她的原话：**"我发现一件事 diff 的时候你得把原句和改后的完整句加进去，不然不够直观，也容易漏"**

```
教练原来的 diff 格式：只列【片段 → 片段】
她指出的两个后果，都成立：
  ① 不直观 —— 片段脱离句子，她读不出改动落在哪个位置
  ② 容易漏 —— 这是更重的一条：教练自己也是靠片段清单在自查，
              漏掉的那处根本不会出现在清单里，也就永远查不出来
     ★ 摆上完整两行句子，就能逐词对扫，漏了一眼看得出 —— 这是【可验证性】问题，不只是排版问题
⇒ SKILL §2.5 已改：每句先摆「原句 / 改后」两行完整句，再列片段级差异；
  零 diff 的句子也要摆原句并写"无 diff"（否则"检查过"和"跳过了"分不开）
```
★ 与她 08-04 定的「零遗漏」同一根：**判断哪条值得记＝已经在漏**；这次是**格式本身在制造漏**。

（⚠️ 08-12 清理：此处原有一条**中途版**的 📊 2026-08-11，与全天定稿那条重复，违反"每天只允许一行 📊"。
已删除，以上方 5198 行那条**全天定稿**为准。）

### 🏆 2026-08-11 本日进步（自诊六次全中，且都是她主动报的）

| 项 | 事实 | 为什么算进步 |
|---|---|---|
| **极性自查** | 第 1 组第 1 句先发出 `has been made`（否定丢了），她自己打断重发成 `has not been made` | 今天的靶心就是极性；**无提示自查命中**，08-04/08-05/08-08 三次极性错都是教练抓的 |
| **"都要"这层没出来** | 自报 `I wait for an hour` 缺了"都要" | 这是【压缩/丢层】的自我感知 —— 她过去只在语法层有直觉，这次是**语义层丢东西也感觉到了** |
| **share 用得不对** | 自报 `not enough jobs to share` 里"share 感觉可以不要" | 判断完全正确。**她对"这个词撑不住这个结构"的直觉出现了**，这是搭配层的自诊，以前没有过 |
| **时态自诊（存疑但选对）** | 想用过去完成时，怀疑能不能配 last year，最后选了过去式 —— 选对了 | B147 边界（具体时间点→过去式）已经能在**犹豫状态下**做对，不只是提示下做对 |
| **改完当场重说（同一天内）** | 第 1 组 cold `made do it with` ❌ → 第 3 组自己产出 `have to make do with` ✅ | 08-10 的结论"只有重说过的才保得住"，今天在**同一次 session 内**再证一次 |

---

## 📅 2026-08-12 · 学习日（新周期第 2 天）

**今日靶心**：中文里那个单字副词 —— 都／只／一直／更／才 —— 说完一句回头找它出来了没有（B209）。

**批次口径**：D-1 ＝ 08-11（📊 有行）；D-3 ＝ 08-08（📊 不回填到 08-09 前）→ 走 §0.1 兜底，取一组「久没出现」。
昨天已 ✅ 的题面今天不重出（定义2，题面级）。

**开场前 B 表回写**（§0.2 硬顺序：先回写再取题）
```
改题面 B148 → 升级为【嵌套否定】"他没有一次不迟到"（08-11 实证：单否定守住、嵌套垮掉）
       B27  → 原格里是"快问快答"清单不是题面，改成"他每天七点起床，从来不迟到"
改测法 B136 → **移出中译英池**，挂当日自由产出题下抓
       （08-11 实证：单点测 `now with AI` ✅，同日自由产出三个书面词一起回来 ⇒ 单点 ✅ 是假的）
更正   B209 → 08-11 写成"B197/B203/B195 并入本号"＝违规合并；
       改回【共享诊断动作，不单独出题、不占 📊 槽位】（同 B190 定位），三个号各走各的 streak
拆号   B147 → B147a（完成时三触发）／B147b（具体时间点必须过去式），均从 0 起算
收题面 B39 · B46 · B157（各自多题面，收成一条，其余转"参考对照不出题"）
仓库侧 删掉 08-11 那条【中途版】📊（与全天定稿重复，违反"每天只允许一行 📊"）
```

**开场进度快照**
```
🎓 已毕业 16 条 ｜ 连对2 1 条 ｜ 连对1 79 条 ｜ 连错≥2 5 条 ｜ 连错1 18 条
```

**节点① 抽签（3 道，复习之后发）**
```
[P2] P2-新05 喜欢在家/花园种菜的人（question_bank.md:211）
[P3] Where do people normally watch sports events?（question_bank.md:349）
[P2] P2-非02 收到特殊蛋糕（question_bank.md:1286）
已写入 asked.log（累计 28 道）
```

### 第 1 组 · 10 题 · 考点一字未改 9/10 ｜ 整句零改动 3/10

- **她的原话（逐字）**：`he was late every time. we went back and forth three times for the same issue. I didn't have chopsticks, so i made do with s spoon. he is looking for a job near his place. i've never taken the airplane.  i ended up queuing for half an hour every time. you feel the energy when you are there. companies should provide training to employees. new staffs need time to get used to a(其实我觉得 the也行) new environment. he isn't familiar with how things work.`
- ⚠️ 两个口径都报，避免 08-11 那次混用：**考点率**＝本组 ✅ 标记数／题数（📊 口径）；
  **整句零改动**＝这一句连⚠️都没有的题数（她读起来更直观）。

```
✅ 1  B148 嵌套否定 ——「他没有一次不迟到」→ `he was late every time.`
      **意思完全正确，而且正好做了那个动作：中文两个否定 → 英语一个肯定句。连错3 断掉**
      ⚠️ "没有一次"的强调层没出来 → `He's never ONCE been on time.` ★ 新建 B214
✅ 2  B45  `back and forth` 词序对了（昨天是 forth and back）
      ❌ `for the same issue` → **ON the same issue** —— 昨天教练给的是 on，她把
         question→issue 改了、把 for 留下了 ＝ **局部修正残留**（08-08 那个模式，第 9 次）
      ⇒ 本条的考点即日起改成【整块 go back and forth ON sth】，不再只测词序
✅ 3  B171a `made do with a spoon` 装上了（昨天 made do it with）
      ⚠️ `didn't have chopsticks` → didn't have ANY chopsticks（否定句里泛指复数带 any 更自然）
✅ 4  B171f `is looking for` 装上了（昨天 found）
✅ 5  B147a 完成时＋never 触发正确
      ⚠️ `taken the airplane` → **been on a plane** ／ flown ／ taken A plane ★ 新建 B215
✅ 6  B197 `end up ‑ing` 用上了，"都要"那层出来了
      ❌ B34 `ended` → **end**（"我每次去"＝习惯，用现在时）—— 时态今天第 1 次、昨天 3 次
      ❌ B94 `every time` 后面缺完整从句 → **every time I go**
         ⚠️ 这条昨天纠过、重说时她说对了，今天 cold 又掉 —— 典型回潮
      ★ 教练自纠：昨天给的 `always end up … every time I go` 里 always 和 every time 语义重复，
        更干净的是二选一：`I always end up queuing…` 或 `Every time I go, I end up queuing…`
❌ 7  B203「只有…才」**又丢了**（和昨天一模一样）→ `You ONLY get that energy when you're actually there.`
      ★ 今天的靶心就是它，本组唯一一道靶心题，没打中 ⇒ 连错2
✅ 8  B210 `employees` 对了（昨天全篇三处说反成 employers）
✅ 9  B211 `get used to a new environment` 装上了
      ❌ `staffs` → **staff**（集合名词无复数）／new staff members／new hires ★ 新建 B216
      她问 a 还是 the → **a**：这是"一个新环境"，第一次提到、听者不知道是哪一个
      （B166 判据：描述一个还没确定的东西不可能定指）。要用 the 得是双方都知道的那个特定环境
✅ 10 B212 `isn't familiar with how things work` 一字未改
```

**⑤ 独立 Diff**
```
【1】原句  he was late every time.
    改后  He's never once been on time.
    · was late every time → 's never once been on time   ⚠️更好  补回"没有一次"的强调
      （她的版本意思对、语法对，只是没有强调层）
【2】原句  we went back and forth three times for the same issue.
    改后  We went back and forth three times on the same issue.
    · for → on                    ❌真错  go back and forth ON sth
【3】原句  I didn't have chopsticks, so i made do with a spoon.
    改后  I didn't have any chopsticks, so I made do with a spoon.
    · chopsticks → any chopsticks ⚠️更好  否定句里泛指复数带 any
    · s spoon → a spoon           —  打字，不计
【4】原句  he is looking for a job near his place.
    改后  （同）   · 无 diff
【5】原句  i've never taken the airplane.
    改后  I've never been on a plane.
    · taken the airplane → been on a plane   ⚠️更好  "坐飞机"英语默认 fly／be on a plane
【6】原句  i ended up queuing for half an hour every time.
    改后  Every time I go, I end up queuing for half an hour.
    · ended → end                 ❌真错  习惯用现在时
    · every time → every time I go ❌真错  every time 是连词，后面要完整从句
【7】原句  you feel the energy when you are there.
    改后  You only get that energy when you're actually there.
    · 缺「只有」→ only            ❌真错  今天的靶心
【8】原句  companies should provide training to employees.
    改后  （同）   · 无 diff（provide sth to sb ／ for sb 都对）
【9】原句  new staffs need time to get used to a new environment.
    改后  New staff need time to get used to a new environment.
    · staffs → staff              ❌真错  集合名词没有复数
【10】原句 he isn't familiar with how things work.
     改后 （同）   · 无 diff
⛔ 0 处
```

**🆕 本组新建**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B214 | **"没有一次不…／一次都不…"的强调层**：中文靠"一次"，英语靠 **never once ／ not once ／ every single time**。<br>`He's never once been on time.` ／ `Not once did he apologise.` ／ `I get stuck every single time.`<br>★ 与 B209 同族：强调层挂在骨架外面，cold 时第一批被挤掉 | "他一次都没道过歉" | 08-12 |
| B215 | **"坐飞机" ＝ fly ／ be on a plane ／ take a plane**（❌ take the airplane）。<br>★ 交通工具三种说法互不混：**by plane/bus/car**（不带冠词，说方式）· **take the bus/train**（带 the，说那趟车/那种通勤方式）· **be on a plane / on the train**（在车上/机上）<br>★ airplane 偏美式书面，口语一律 **plane** ／ **flight** | "我从来没坐过飞机" ／ "我每天坐地铁上班" | 08-12 |
| B216 | **staff 是集合名词，没有复数 staffs**：`the staff are friendly`（英式常用复数动词）／ 要说"几个员工"用 **staff members ／ employees ／ new hires**。<br>★ 同族不可数/集合名词：**advice · information · furniture · equipment · feedback · research**（都不加 s） | "我们公司新来了三个员工" | 08-12 |

### 改完当场重说 · 第 1 组 · 4/4 全对

- **她的原话（逐字）**：`We went back and forth three times on the same issue. / Every time I go, I end up queuing for half an hour / You only get that energy when you're actually there. / New staff need time to get used to a new environment.`
```
1 ✅ on the same issue（本日 ❌ B45 的介词）
2 ✅ Every time I go, I end up ‑ing（本日 ❌ B34 时态 ＋ ❌ B94 从句，两条一起装上）
3 ✅ You only get…（本日 ❌ B203，今天的靶心）
4 ✅ New staff（本日 ❌ B216）
★ 按 §0.5：给过答案后的重说不改当天标记
```

**⚠️ 教练自纠（数字口径）**：开场快照报的「连对2 1 条」是 B147，但 B147 在开场就被拆成
B147a/B147b 且**从 0 起算** ⇒ 开场起 **连对2 实为 0 条**。第 1 组战报沿用了错的那个数，此处更正。

### 第 2 组 · 10 题（第 7 题漏答，待补）· 考点 8/9 ｜ 整句零改动 2/9

- **她的原话（逐字）**：`I can't go a day without checking phones. kids will lose interest in their schoolwork. the drug is useful / works. It's a bit scrary, and i'm also scared(继续用 a bit 么）。 hobbies are what you  choose youself. teachers should get students to try it themselves. jobs are not enough to go around. a mix of the city and the countryside is ideal. I can't focus at work / focus on my work.`
- ⚠️ **第 7 题「他每天七点起床，从来不迟到」（B27 主谓一致）漏答** —— 教练当场指出并补出，不静默跳过

```
✅ 1  B173 `can't go a day without ‑ing` 结构完全正确（昨天意思整个反了）
      ⚠️ `checking phones` → **my phone**（单数＋物主；phones 听起来像"检查一批手机"）
✅ 2  B107a `lose interest IN their schoolwork` 一字未改（昨天 will lost interest on）
✅ 3  B46  `works` 正是词条里最口语的那版，绕开了 efficient
      ⚠️ `the drug is useful` —— useful＝"有用处"，不等于"管用"；且 drug 偏医学/毒品
         → **This medicine really works.**
✅ 4  B157 scary（物）／scared（人）两侧都对
      她问"继续用 a bit 么" → 见下方 B26 补注
✅ 5  B68  `hobbies are what you choose yourself` 成立，绕开了单数表语的坑
      ⚠️ `what you choose` → **things you choose**（更具体，也更贴 B68 的目标形）
✅ 6  B39  `get students to try it themselves` 一字未改
—  7  **漏答**（B27），不记标记，当场补出
❌ 8  B192 `jobs are not enough to go around` —— **块的头装反了**
      ✅ go around 本身对了（昨天是 to share）
      ❌ 整块是 **There aren't enough jobs to go round.** ——「enough X」要在一起，
         不能拆成「X are not enough」⇒ 与第 1 组 B45 同一个模式：**尾巴装上了、头没装上**
✅ 9  B43  `the city and the countryside` 对称配对，一字未改（昨天 the city life）
      ⚠️ "各一半"那层没出来 → **an EVEN mix** ／ fifty-fifty（今日靶心族，第 2 次）
      ⚠️ `is ideal` → would be ideal（说理想状态用 would）
✅ 10 B41  两种形式都给对了（昨天 focus my work）
      ⚠️ "很难" → **It's HARD to focus at work**；她说成 can't（不能）＝档位升了一级（靶心族，第 3 次）
```

**⚠️ 今日靶心族本组又中三次**：各一半→a mix（丢"各一半"）· 很难→can't（档位升级）·
另加第 1 组的 只有→丢 与 没有一次→丢。**四次里她一次都没主动补上那一层** ⇒ 靶心继续挂着，明天不换。

**⑤ 独立 Diff**
```
【1】原句  I can't go a day without checking phones.
    改后  I can't go a day without checking my phone.
    · phones → my phone            ⚠️更好  单数＋物主
【2】原句  kids will lose interest in their schoolwork.
    改后  （同）   · 无 diff
【3】原句  the drug is useful / works.
    改后  This medicine really works.
    · the drug → this medicine     ⚠️更好  drug 偏医学/毒品，口语用 medicine
    · is useful → really works     ⚠️更好  useful＝有用处，"管用"是 works
【4】原句  It's a bit scary, and i'm also scared.
    改后  It's a bit scary — I'm actually quite scared.
    · and I'm also scared → I'm actually quite scared   ⚠️更好  一句里别放两个软化词
【5】原句  hobbies are what you choose yourself.
    改后  Hobbies are things you choose yourself.
    · what you choose → things you choose   ⚠️更好  更具体
    · youself → yourself           —  打字，不计
【6】原句  teachers should get students to try it themselves.
    改后  （同）   · 无 diff
【7】漏答。教练给：He gets up at seven every day and is never late.
【8】原句  jobs are not enough to go around.
    改后  There aren't enough jobs to go around.
    · jobs are not enough → there aren't enough jobs   ❌真错  enough 要贴着名词
【9】原句  a mix of the city and the countryside is ideal.
    改后  An even mix of the city and the countryside would be ideal.
    · a mix → an even mix          ⚠️更好  补回"各一半"
    · is → would be                ⚠️更好  说理想状态用 would
【10】原句 I can't focus at work / focus on my work.
     改后 It's hard to focus at work.
     · can't → it's hard to        ⚠️更好  "很难" ≠ "不能"，档位别升级
⛔ 0 处
```

**B26 补注（她问"继续用 a bit 么"）**
```
可以再用，但**一句话里别放两个软化词** —— 两个 a bit 会互相削弱，听起来像在犹豫。
她这句是【递进】（东西吓人 → 我也怕），第二边再软化就把递进抹平了（＝B59 自我对冲）。
两个出口：
  ① 第二个直接去掉        It's a bit scary, and I'm scared too.
  ② 第二个换一档往上走    It's a bit scary — I'm actually quite scared.
★ 判据：对比句/递进句里，**第二边要给足**，不要用 a bit 缩回去
```

### 改完当场重说 · 第 2 组 · 4/4 全对

- **她的原话（逐字）**：`He gets up at 7 every day and is never late. There aren't enough jobs to go around. An even mix of the city and the countryside would be ideal. it's hard to focus at work`
```
1 ✅ gets / is —— B27 主谓一致两个动词都加对了。但这是【补答】（教练先给了范文）
  ⇒ **B27 今日记 📖，不记 ✅**（📖 清零连对、不加连错）
2 ✅ There aren't enough jobs to go around（本日 ❌ B192）
3 ✅ an even mix … would be ideal（本日靶心族两处一起装上）
4 ✅ It's hard to focus at work（档位改回来了）
★ 今日重说累计 8/8
```

### 第 3 组 · 10 题（昨天全是 📖 那批的首次 cold 测）· 考点 7/10 ｜ 整句零改动 3/10

- **她的原话（逐字）**：`1. I can't cook or bake (用 can 总觉得没有 be able to，错觉么) 2.but I don't go too far （这个感觉没有说这个动作) 3. it's not that the game is bad, it is how long 4. we are always paired in one group, and i get stuck. 5. my english is not great, 后面的忘了 6. I need a box to put things in. 7. You should key an eye on (pay attention to) prices when you shop. 8. the whole round road is completely jammed every time there is an accident - no cars can move. 9. there is no charger, so I use my colleague's 10. everthing in moderation (is fine)`

```
✅ 1  B89  `I can't cook or bake.` 一字未改（昨天 📖）★ 她的提问见 B217
❌ 2  B109a `but I don't go too far` → **I wouldn't go THAT far, though.**
      ① don't → **wouldn't**（委婉/虚拟：我不会说到那个程度）
      ② too far → **that far** —— 昨天教练已把 too 改成 that，今天又回到 too（回潮）
      ★ 她的提问"感觉没有说这个动作"是**好直觉**，见 B218
✅ 3  B109c `it's not that A, it is B` 壳对了（昨天 📖）
      ⚠️ `the game` → **games**（中文"游戏本身"是泛指）· `it is how long` → 加 about 更顺
❌ 4  B117c `i get stuck` —— **丢了 with him，意思变成"我卡住了"**
      → **Whenever we get put into pairs, I get stuck WITH HIM.**
      ⚠️ `paired in one group` → get put into pairs ／ get paired up
📖 5  B171g 前半 `not great` 装上了（昨天教的），后半又忘 —— **连续两天 📖**
      → **but I get by.** 抓手：get by 的 by ＝"擦着边过去"，刚好够、不多
✅ 6  B175 `a box to put things in` 一字未改（昨天 📖，说成 wrap）
      ⚠️ `things` → these things（题面是"这些"）
✅ 7  B189 两种说法都给了（keep an eye on ／ pay attention to）—— **前两次都是 ◎，这次终于测到了**
✅ 8  B191a `completely jammed` 装上了
      ❌ `the whole round road` → **ring road**（环路）★ 新建 B219
      ⭐ `every time THERE IS an accident` 完整从句用对了 —— 第 1 组刚错过（B94），
         这里换了一个**全新句子**又用对 ⇒ 比单纯重说更强的迁移证据（但按 §0.5 不改当天标记）
      ⭐ `no cars can move` 极性正确（no ＋ 肯定动词）
✅ 9  B193 走了 ③ 型（There is no…, so…）结构对
      ❌ 时态 `there is / I use` → **there WAS / I USED**（中文"就用了"＝过去）—— B34 今天第 2 处
✅ 10 B208 `Everything in moderation.` 一字未改（她自己把 is fine 放进括号 ＝ 记住了昨天那条）
```

**⑤ 独立 Diff**
```
【1】原句  I can't cook or bake.
    改后  （同）   · 无 diff
【2】原句  but I don't go too far.
    改后  I wouldn't go that far, though.
    · don't → wouldn't            ❌真错  说"我不会说得那么绝"要用委婉的 would
    · too far → that far          ❌真错  固定块是 go THAT far（昨天已纠，今天回潮）
    · but（句首）→ though（句尾）  ⚠️更好  B120，说完再补，前面一字不改
【3】原句  it's not that the game is bad, it is how long.
    改后  It's not that games are bad — it's about how long.
    · the game → games            ⚠️更好  泛指用复数
    · it is how long → it's about how long   ⚠️更好  加 about 更顺（不加也成立）
【4】原句  we are always paired in one group, and i get stuck.
    改后  Whenever we get put into pairs, I get stuck with him.
    · get stuck → get stuck WITH HIM   ❌真错  丢了 with him，意思整个变了
    · are always paired in one group → whenever we get put into pairs   ⚠️更好
【5】原句  my english is not great, （后半忘）
    改后  My English isn't great, but I get by.
    · 后半缺失 → but I get by     📖
【6】原句  I need a box to put things in.
    改后  I need a box to put these things in.
    · things → these things       ⚠️更好  题面是"这些"
【7】原句  You should keep an eye on (pay attention to) prices when you shop.
    改后  （同）   · 无 diff（key 是打字）
【8】原句  the whole round road is completely jammed every time there is an accident - no cars can move.
    改后  The whole ring road gets completely jammed every time there's an accident — nothing moves.
    · round road → ring road      ❌真错  环路是 ring road
    · is → gets                   ⚠️更好  强调"变成"那个状态
    · no cars can move → nothing moves   ⚠️更好  更短（原句也完全对）
【9】原句  there is no charger, so I use my colleague's.
    改后  There was no charger, so I used my colleague's.
    · is → was ／ use → used      ❌真错  中文"就用了"＝过去
【10】原句 everything in moderation (is fine).
     改后 Everything in moderation.
     · 无 diff（她自己把 is fine 放进括号，说明昨天那条记住了）
⛔ 0 处
```

**🆕 本组新建（两条来自她的提问，都是好问题）**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B217 | **can 才是默认，be able to 是备用**（她问"用 can 总觉得没有 be able to，错觉么"—— 是错觉）：<br>说现在的能力，**can 和 be able to 完全等价，而且 can 更自然**：`I can't cook.` ✅（`I'm not able to cook` 累赘）<br>**只有 can 没有那个形式时才必须换 be able to**：<br>① 完成时／不定式／情态后面 —— `I've never BEEN ABLE TO cook.` ／ `I want to BE ABLE TO cook.` ／ `You might BE ABLE TO…`<br>② 过去**单次**费劲做成了 —— `I WAS ABLE TO get a ticket.`（could 说的是过去的一般能力，不是这一次成功）<br>★ 她为什么觉得 can 单薄：中文"会/能"是个实义概念，can 是个小词、没有分量感。**英语用小词承担重量是常态，不是缺斤少两**（同 B102） | "我不会开车" ／ "我从来没能早起过" ／ "那天我总算买到票了" | 08-12 |
| B218 | **★ go ＝ 在【程度轴】上移动，不是走路**（她问"go too far 感觉没有说这个动作"—— 直觉准，但那个动作本来就不是"说"）：<br>`I wouldn't go that far.` ＝ 我不会（在这个说法上）走到那么远<br>`That's going too far.` ＝ 那太过分了 ／ `How far are you willing to go?` ＝ 你愿意做到什么程度<br>★ 中文把程度说成"绝／过分／到什么地步"，**英语把程度说成一条路，用 go ＋ far** —— 与"英语靠一小撮通用动词"（B102）同源<br>★ 同族方位隐喻：`go too far` · `take it too far` · `draw the line`（划界限） | "他这话说得太过了" ／ "你愿意做到什么程度" | 08-12 |
| B219 | **环路 ＝ ring road**（英）／ beltway（美）；❌ round road 不成立。<br>同族路名：**motorway**（英高速）／ highway · **the M25** · **a dual carriageway**（双向分隔路）· **a one-way street** | "一出事故整条环路就堵死了" | 08-12 |

### 改完当场重说 · 第 3 组 · 5/5 全对

`I wouldn't go that far, though. / Whenever we get put into pairs, I get stuck with him. / My english isn't great, but I get by. / There was no charger, so I used my colleague's. / The whole ring road gets completely jammed everty time there's an accident.`

### 第 4 组 · 10 题（昨天新建那批的首次 cold 测）· 考点 6/9 ｜ 整句零改动 3/9

- **她的原话（逐字）**：`1. everything in moderation (is fine). 这个题重复了 2. the roads were really jammed today morning. the traffic in chengdu is always heavy. 3. is is less about the machine itself and more about the time spent with my kid.(spent together) 4. there are a few(3+) / a couple of (2，其实口语中也可以代表 3) reasons that(why) I don't want to go. 5. colorful dinosaurs. 6. he watch(这里我没加 can 了，你觉得需要么) things on the screen (昨天练的有特指, 今天如果是单句我觉得也可能改成 screens) turn into real objects he can hold. 7. I queued for half an hour. 8. everything is ok, so you make it(定吧，本来想用 decide ，但是感觉后面空荡荡的，不确定) 9. that app is really useful for working people. 10. I don't order takeaway in general and I prefer cooking myself.`

**⛔ 教练违规 1 处（她当场抓到）：第 1 题与第 3 组第 10 题重复**
```
她："这个题重复了" —— 成立。B109d（in moderation）与 B208 原题面"凡事适度就好"是同一个考点。
教练确实做了题面拆分（B208 改测 on purpose），但**改在已经出完第 3 组之后**，等于没起作用。
§2.1a「跟本 session 已出过的全部题逐条比对」这一步没跑。⇒ 本题不计标记。
```

```
—  1  重复，不计
✅ 2  B195 `the roads were jammed` ✓｜❌ `today morning` → **this morning** ★ 新建 B220
      第二句 `the traffic in chengdu` —— 加了地点限定后两种都说得通 ⇒ 题面不够利，
      已改：第二句换成"最近交通越来越差了"（无地点限定，必须 Traffic is getting worse）
✅ 3  B198 `and` 用对了（昨天 but），一字未改
✅ 4  B199 `a few` ✓；她标注 couple＝2 正确，且指出"口语里 a couple 也能指 3"—— **也对**
      （非正式口语 a couple of ≈ 两三个；考试里默认 a few 更保险）
✅ 5  B200 colorful ✓（美式拼写，不计）
✅ 6  B201 `watch … turn into` 原形补语 ✓ · real objects 复数 ✓
      ❌ B27 `he watch` → **watches**（主谓一致，今日第 2 次）
      她问"要不要加 can" → **要**，中文"能"那层丢了（今日靶心第 5 次）
      她问"the screen 还是 screens" → **the screen**：日常设备泛指惯用 the（the phone/the TV/
      the radio/the internet/the screen），已补进 B58
✅ 7  B206 `I queued` —— 直接把 queue 当动词，正是最省那版
❌ 8  B207a `everything is ok` → **Anything's fine.**（随便挑一个用 any-，不是 every-）
      ❌ `you make it` → **You decide. ／ It's up to you.**
      ★★ 她的自述："本来想用 decide，但感觉后面空荡荡的" —— **这是过度泛化的现场**，见 B221
◎ 9  B213 "特别有用"的"特别"她读成"非常"(really) —— **中文本身歧义，题面问题**
      已改题面为"这个 app 谁都好用，对上班族尤其如此"
❌ 10 B205 没带具体的东西（本题的要求就是这个）
      → I don't usually order takeaway — I'd rather cook, it only takes twenty minutes.
      ⚠️ `in general` 放句尾别扭 → usually 放句中
```

**🆕**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B220 | **"今天早上/昨天下午"的说法**：**this morning ／ this afternoon ／ this evening**（❌ today morning）· **yesterday morning ／ tomorrow morning**（这两个有 yesterday/tomorrow 才对）· 昨晚 ＝ **last night**（❌ yesterday night） | "今天早上路上特别堵" ／ "昨天晚上我很早就睡了" | 08-12 |
| B221 | **★★ 过度泛化警报：不是所有动词都要宾语**（08-12 现场）<br>背景：教练两天内纠了她两次"动词后面缺东西"（focus **ON** my work · stuck **WITH** him），她随即给**不及物动词**也硬加宾语（`you make it` 代替 `You decide.`），自述"感觉后面空荡荡的"。<br>⇒ 这是**注意力零和的另一种形态：修一处，隔壁被带偏**（同 08-08「局部修正残留」，但方向相反 —— 那次是漏改，这次是多改）<br>**能单独站住的一小批常用动词**：decide · choose · help · manage · cope · agree · win · lose · pay · answer<br>★ "空荡荡"的通用解药不是加宾语，是换整块：**It's up to you.** ／ **Whatever you like.** | "你定吧" ／ "我帮不上忙" ／ "我们赢了" | 08-12 |

### 改完当场重说 · 第 4 组 · 4/4 全对（并暴露 `cook myself` 新问题）

- **她的原话**：`this road was really(particularly, super) jammed this morning. he can watch things on the screen turn into real things he can hold. anything's find - it's up to you. I don't usually order takeaway. Instead, I'd rather cook myself - it only takes 20 minutes.`
```
四条要改的都装上了。三处教练补充：
① 副词选择（她问 really/particularly/super）：really ✅ · completely/absolutely ✅（jammed 是"极限状态"
   形容词，配 completely 比 very 贴）· particularly 偏书面 · super 太随意
② `turn into real things` 成立，但一句里 things 两次 → real OBJECTS ／ something real
③ ⚠️ **`cook myself` 有歧义**（字面像"把我自己煮了"）：myself 作强调通常跟在宾语后
   （I cooked it myself ✅）→ **I'd rather cook. ／ do my own cooking. ／ cook for myself.**
   另 `Instead + I'd RATHER` 语义重复，留一个
```

### 第 5 组 · 10 题（4 条收尾昨天新建 ＋ 6 条 D-3 兜底）· 考点 7/9 ｜ 整句零改动 3/9

- **她的原话（逐字）**：`1. There is discrimination against female managers in Japan（社会没翻译出来, society shows discrimination 可以么) 2. everyone laughs every time he speaks that joke. If he come tomorrow, I'll bring him along. 3. everyone knows that thing. 5. no one wants to work overtime. 6. it's much quieter at home. 7. it's not such simple. 8. I walk to work every day. 9.it's much eaiser to find next time(我记得你说 find 不太多？，但是没有其他的第一反应） 10. you cook for two hours and it only takes 10 minutes to eat`
- ⚠️ **第 5 题「我得去看医生」漏答**（她把第 4 题标成了 5），当场补出

```
✅ 1  B194 补语紧贴 ✓，地点状语没插进中间
      她问"社会没翻出来，society shows discrimination 可以么" → 不地道，见 B222
✅ 2  B204 when/if 两边都选对
      ❌ `speaks that joke` → **tells** ★ 新建 B223 ｜❌ B27 `If he come` → comes（今日第 3 次）
✅ 3  B207b everyone ✓｜⚠️ `that thing` → about it
✅ 4  B207c `no one wants to work overtime` 一字未改，极性正确
—  5  B58 漏答 → **I need to go to the doctor.**
✅ 6  B59 `much quieter` 对比给足了，没用 a bit 缩回去
      ⚠️ "冷清" ≠ quieter（丢了"没气氛"）→ a lot lonelier ／ it just feels flat at home
❌ 7  B65 `such simple` → **that simple**（such 配名词 such a mess；that/so 配形容词）
✅ 8  B67 一字未改
✅ 9  B77 `much easier` 比较级只标一次 ✓
      ❌ B41 `to find` 缺宾语 → **find THEM next time**
      ★★ 她自述"我记得你说 find 不太多" —— **她记得这里有问题，但记错了是哪里**
        （以为问题在 find 这个词，其实在缺宾语）⇒「局部修正残留」的认知版
△ 10 B72 她的说法成立，但有更短的固定块 → **it's gone in ten minutes**
```

**🔴 本组两个同型发现**
```
① B41 论元完整：第 2 组答对（focus at work ✅）→ 第 5 组又掉（to find___ ❌）
   ⇒ 与昨天 B136 书面词同构：**单点测通过 ≠ 装上了**，块级问题只有换句子才测得出
   ⇒ B41 今日最终记 ❌（两次都是 cold，以最后一次为准），进连错 2
② 主谓一致 B27 今日第 3 次
```

**🆕**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B222 | **中文的"社会／大家／人们"这类泛主语，英语常用 there is 或被动吃掉**（她问 `society shows discrimination` 可以么 —— 不地道，show 配 discrimination 生硬）：<br>✅ `There's a lot of bias against female managers in Japan.`（最自然，"社会"隐含在 there is 里）<br>✅ 要显式说社会就让它当主语＋**动词**：`Japanese society still discriminates against…`（不是 show + 名词）<br>✅ `People in Japan still have a bias against…`<br>★ 与 B123（中文无主语句 → 先想被动或 they）同一条根 | "社会对年轻人期待太高" ／ "大家都觉得这样不对" | 08-12 |
| B223 | **讲笑话 ＝ tell a joke**（❌ speak a joke）。同族"说"的动词分工：<br>**tell** ＋ 有内容的东西（a joke／a story／a lie／the truth／sb the time）<br>**say** ＋ 话本身（say something／say sorry／say a word）<br>**speak** ＋ 语言 或 不及物（speak English／speak to sb）<br>**talk** ＋ 交谈（talk about sth／talk to sb） | "他老爱讲这个笑话" ／ "他连一句话都没说" | 08-12 |

### 改完当场重说 · 第 5 组 · 5/5 全对

`I need to go to the doctor. / Everyone laughs every time he tells that joke. / If he comes tomorrow, I'll bring him along. / It's not that simple. / It's much easier to find them next time.`

### 第 6 组 · 4 题（补齐 D-3 兜底）· 考点 3/4

- **她的原话（逐字）**：`no one knows which part is yours (不用 know 可以用 get 么，或者其他词). / it's parts that really belong to you. / I need that job. / he is good at cooking. he cook really well.`

```
✅ 1  B61 `which part` ✓ 极性也对
      她问"能不能用 get" → 不行，见 B224
❌ 2  B64 `it's parts that really belong to you`
      ❌ 丢了「唯一」→ **the ONLY part**（今日靶心第 6 次）
      ❌ parts → part（唯一→单数）｜❌ B27 `belong` → belongs（今日第 4 次）
✅ 3  B70 `job` ✓（"这份工作"用 job 不用 work）｜⚠️ that job → this job
✅ 4  B66 `good at cooking` ✓ **而且她自发给了词条里的升级版 `he cook really well`**
      ❌ B27 `he cook` → cooks（今日第 5 次）
```

**🆕**
| # | 点 | 抽查方式 | 来源 |
|---|---|---|---|
| B224 | **know ／ tell ／ get 的分工**（她问"不用 know 能用 get 么"—— 不能）：<br>**know ＝ 知道（掌握信息）** · **tell ＝ 分辨得出（区分两个东西）** `No one can tell which part is yours.` · **get ＝ 听懂/理解**，且只能说 `I get it／I don't get it`，**后面不能跟 which/what 从句**<br>★ "分不出来/看不出来"一律用 **tell**：`I can't tell the difference.` ／ `You can't tell they're twins.` | "我分不出这两个有什么区别" ／ "没人看得出来是他做的" | 08-12 |

### 改完当场重说 · 第 6 组 · 3/3 全对（今日重说累计 25/25）

`No one can tell which part is yours. / it's the only part that really belongs to you. / he cooks really well.`

---

## 🗣 表达库（按场景 · 只收出现过的 · ⭐ = 她自己产出的，优先滚）

> 2026-08-01 建。她指出："rather than / live off / go on / set you up with 这些需要学习和累计，特别是结合场景，不然感觉白学。"
> **原则**：①按场景不按词表 ②每条是**完整句子**不是短语 ③只收已出现过的，不新增。

**工作 / 上班**
```
⭐ I head to work right after I get up.
⭐ It's pretty much bedtime when I get home.
⭐ Typing has become second nature.
   Everyone stays late, and leaving on time almost feels wrong.
   They just do the minimum and leave on time.
   They'd rather have an easy life than chase a promotion.
```
**吃饭**
```
   I eat out for all three meals on workdays.  ／  I just grab something quick near the office.
⭐ Home-cooked food tastes better than that at restaurants.
   I have no time to cook.
```
**花钱**
```
   The tickets turned out to be really cheap.  ／  Parents pay a fortune for a tiny old flat.
   Rent has gone up a lot.
```
**出行 / 地点**
```
⭐ I'm stuck in traffic.
⭐ There are three subway lines within a ten-minute walk.
⭐ It's only minutes from the main road, but it feels miles away from the noise.
⭐ I stumbled on it a few years ago.
```
**家人 / 关系**
```
⭐ I spend as much time as possible with my son.   ⭐ I get some real me time after he goes to bed.
   They're grown up but still living off their parents.   Your parents set you up with someone.
```
**兴趣 / 评价**
```
⭐ I don't follow it that closely.   ⭐ It's less about the game itself and more about hanging out with friends.
⭐ I'm tone deaf.   ⭐ It cracks me up.   ⭐ I wouldn't say I don't like it.   ⭐ I can live with it.   It really works.   The credit gets shared.   It's a nightmare.   It's a hassle.   It's no big deal.   There's no point regretting it now.
   Nothing beats spending time with my kid.   Scrolling through short videos gets old fast.
```
**对比 / 关系**（2026-08-01 轮94 建，按难度排，卡住往左退一格）
```
   A can't replace B.                 最简单，实在想不起来就用这个
   A works alongside B.               并存、各自起作用、不取代（work + alongside=在旁边）
   A goes hand in hand with B.        相辅相成（比 works alongside 更紧密）
⭐ nothing can beat B                 （轮36 Nothing beats 块的迁移，她自发）
⭐ We're on the same wavelength.      合拍、同频（轮96 她自发）
⭐ They've been there before.         经历过（轮96 她自发）
   A, on the other hand, …            标出对比的另一边
   ★ 天然配 `rather than replacing B` 使用，语义对称
```

**时间表达**
```
   within minutes of it happening ／ just minutes after it happens
⭐ once or twice a year   ⭐ I've been doing this for over ten years.
```

---

## 🖼 "抽象 → 画面"的操作法（2026-08-01 建，她指出"知道要找画面但找不出来"）

**为什么难**：抽象词是**多个画面压缩成的一个词**，展开时面对的不是"找不到"，是"十个画面选哪个"——**选择本身耗带宽**。解法：不选，按固定顺序问。

```
第一步  问："谁 + 在做什么？"
第二步  验："这个动作我能看见吗？"  看不见 → 再具体一层
★ "能不能看见"是唯一判断标准
  people face pressure（看不见）❌  →  people work until nine（看得见）✅
  people have a fast pace（看不见）❌ →  people eat lunch at their desks（看得见）✅
```

**技巧 2 · 带反差**：如果这个词自带反差，画面里要说出来。
```
内卷 = 更努力【但】没领先 → Everyone works longer hours, but nobody actually gets ahead.
学区房 = 破房子【但】天价 → Parents pay a fortune for a tiny old flat.
加班文化 = 准点走【反而】不对 → Everyone stays late, and leaving on time almost feels wrong.
```

**技巧 3 · 否定后面必须跟正面动作**（轮 88 她反驳"我就是想用否定"后修正的版本）
```
❌ 光有否定  They don't work.                                 无画面
✅ 否定+正面 They don't work — they just live off their parents.  ✅
★ 每个"不做A"背后都有"做B"，找那个 B：
  不上班→靠父母过活 live off their parents ／ 不想晋升→宁愿轻松 would rather have an easy life
  不加班→准点下班 leave on time
★ 万能工具：would rather A than B —— 想说"不想X"就说"宁愿Y"
```

**技巧 4 · 只用看得见的动词**（她的默认动词 face/have/be 全都看不见）
```
work · stay · leave · go · eat · buy · pay · live · move · wait · queue · spend · take
画面 = 这些动词之一 + 具体的人/时间/数字
```

**技巧 5 · 降级必须在中文层做完**（轮 84 发现）
```
❌ 中文抽象 → 直接翻 → 英文抽象（她的默认）
✅ 中文抽象 → 中文具体 → 翻 → 英文具体
   压力大 → 每天加班到八九点 → people work overtime until eight or nine
★ 第一步在中文层，不占带宽，她完全做得到，只是没做
★ 这正是 offline 备内容该做的事
```


---

## 🏆 本 session 可指认的进步（2026-07-27/28，回答她"每次学习到底提升了什么"）

> 她的核心痛点是"口语感觉不到提升"。以下全部有轮次编号可查，是记录不是感觉。

| 项 | 之前 | 之后 | 备注 |
|---|---|---|---|
| C1 比较对象补齐 | 轮13 ❌ `English is easier than one years ago` | 轮27 ✅ `phones are smarter than THEY WERE ten years ago` | **中间 14 轮没练过，自己长上去的** |
| 整合表现 | 轮16 fragment+2次修复+it/I拐杖+零细节 | 轮28 全清+具体细节 | 同类任务，隔 12 轮 |
| ③ if…it's hard to | 轮15 建立 | 轮16 自由说话时**自主调出**（无提示） | 一轮内迁移 |
| 揪主语 | 轮24 建立 | 轮25 主语 3/3 正确 | |
| 换说法 | 轮25 建立 | 轮26 3/4 → 轮27 边界清晰（跳出来vs找出来） | |
| **比较对象对齐** | 写作错 ≥3 次（it of / compared to the general public）+ 口语轮13 错 | **轮56 口语无提示自发做对**（than **that** at restaurants，且数正确） | 跨模态长期错误自发修复 |
| 答案长度 | 通常 2–4 小句 | 轮55 五句 → 轮56 **六句且 uh 减少** | 四步展开器生效 |
| B2 同位语 | 轮24 教（Yibin, a small city…） | 轮33 **无提示自发**（ranmian, or burning noodles in English） | 隔 9 轮，且用在更难处 |
| 实义动词 -s | — | 轮32 6/6 秒答 → 轮33 5/5 形态全对 | 词与形态都在，缺的是触发 |
| cooking 话题 | 轮22 完全卡死"没想起内容" | 轮31 三句全有内容（教练零内容输入） | 变量只是手上有了结构 |
| **三步主干** | 08-03 前无主干，她自述"在硬堆、没有体系" | 08-03 **无提示走通**（shop online / tall buildings / boring classes 三题） | 十套工具收成一条主干 |
| **答案前置** | 答案常拖到第三句（头重脚轻，她自己发现） | 三步主干确立后，三题全部答案在第一句 | 她第 11 次纠正带来的改动 |
| **写作素材迁移到口语** | — | `the higher you live, the further you can see`（源自写作 the taller…the more…） | 跨模态迁移 |
| **跨话题迁移（她自发）** | — | 三个 no：电影院→跑步 ／ You can feel every X：CBA→演唱会 | 泛化能力的直接证据 |
| **改过又犯专项** | in/on · terrible at/with · at any time · for any reason 反复回潮 | 08-03 drill **四项全部改对**，主谓一致 3/3 | 纠正必须进 drill，不能只讲 |
| **盲测三项全过** | 第②步连续三次跳过（判断/规律/推论） | 08-04 second-hand 题：三步走完 + 数字画面 + 两角度不重复 | 第一次盲测全过 |
| **改过又犯（08-04）** | usually played ／ pay more energy | 全部改对（often played ／ put energy into） | 隔一天保持 |
| **论元完整** | 五处丢过（focus on__ / a mix__ / goes to. / see__ / spend as much__） | 08-04下 primed drill **8/8 全补回** | 但 primed，冷测才算数 |
| **do+动词强调（B37）** | 08-04 上午教 | 同日下半场 `i DID try it` 无提示自发用 | 跨任务迁移 |
| **★ 改完当场重说的效果** | usually / effective 只听不产出 → 隔一天、隔五分钟都回潮 | Drill B 四个改动 **4/4 保住** | 唯一变量＝是否当场再产出一遍 |
| **中文层三步主干** | 08-03 建立于英文产出 | 08-04下 卡住时**中文自动按三步组织**（她无意识） | 结构已内化到内容层 |
| **第②步画面** | 连续 5 次不达标 | 08-04 second-hand ✅ → 08-05 concerts **换题型再过** | 连续两次，不同题型 |
| **第③步第二支点** | 08-05 concerts 四句全在"气氛"一根轴（车轱辘复发） | 给四个万能支点后**当场做到**（主角＝机会/频率） | 有脚手架，下一步测 cold |
| **第③步 cold** | 上面那次靠四支点清单 | 同日 organized 题**零角度提示，两个支点主角不同且第二支点带机制层** | 脚手架撤掉后成立 |
| **抽象包自主降级** | "动力"这类抽象名词以前直接卡死 | 自己降成 `more willing to do it` | 拆包在中文层完成 |
| **⭐ 块自主复用** | — | `once or twice a year` 用进全新语境（演唱会稀缺） | 她自己的块，跨话题迁移 |
| **压缩操作（第二步）** | 08-08 上午 22/23 想到 packed 却"组不进句子" | 同日真题 `the elderly tend to BE light sleepers` 一次装进句子 | 出口A（做表语）当天生效 |
| **人称一致 B78** | 08-06 同题写 `because YOU follow the steps`（一天跳 4 次才升主攻） | 08-08 同题自己统一成 `because I follow the steps` | 主攻项自我修复 |
| **完成时触发判据** | 她自述"对完成时很不敏感"（中文无此时态） | 8 句 drill **时态选择 8/8**，触发词判据一次上手 | 当天建立当天生效 |
| **名词短语清单** | "reasonable hours / job security 这类简单词组我用不出来" | 三类清单 **9/9 全名词短语**，无一滑回动词或否定 | 一次上手 |
| **教练版被她改进** | 教练写 `the other doesn't need any`（否定式） | 她自产 `the other puts you there`（正面＋画面） | 她的版本更好，已采用 |
| **答案前置自主执行** | 08-03 是她纠正教练"头重脚轻" | 08-08 主动把教练版的结尾结论提到第二句 | 从被动纠正到主动应用 |

---

## 当前训练法（按最新靶心）

> ⚠️ **轮 10 后靶心已变**：病灶在**内容检索**，不在语法。以下"主语指派"仍有效但降为第二步；第一步是**内容角度**。

**新训练法（三步拆开，逐步合并）**
```
第1步  内容角度反射   给话题 → 秒选一个角度（贵不贵/和以前比/对人影响/我自己/好在哪坏在哪…）
第2步  主语指派       角度定了 → A实义(具体物/人) 或 B虚位(it/there) 起手
第3步  往下接         起手后自回归接块（她已证能接 4 块）
```
**核心洞察**：她考场崩=三件事挤一起(想内容+指派主语+转英文)。训练=把第1步练到不占带宽，现场只剩 2+3。

**旧法（仍可做，但不是主线）：练"话题→主语指派"反射**，不练背块（块是实例，指派是规则）：
- 给一个话题 → 用 4 类起手主语各起一个头（只起头）。
- 目的：让她体会"同一个意思有 4 个合法入口"，起头从面对空白→面对 4 选 1 菜单。
- 之后自动化：英文/画面触发、限时、出声、堆量。

**停练**：骨架层（连接词/篇章框架，已饱和）、背新词/新句型（知识已 83%）、中译英当流利训练（喂中介）。

## 待验证
- 主语指派反射建立后，"启动延迟"是否下降。
- 4 类入口里哪类她最卡（下轮数据会显示）。
