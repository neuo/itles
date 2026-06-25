# P3 从问题入手：听 SHAPE 调一个 FRAME + 怎么展开（v1 · 从 p3_answers_tagged 重导）

> **本文件已对齐 ground truth `p3_answers_tagged.md`**（324 答案语料 · 6 批 mining 聚合 · 每函数 2-3 张逐句标签的成品）。frame 的 opener glue、land tic、whichStems、降级 swap、陷阱，全部 re-derived **FROM 那 324 张**，不是从旧 5-frame 推演稿。和旧 `03_question_types.md` §P3 五框架有出入的地方，以本文件 + 语料为准。
> 配套：填空骨架+降级词 [[p3_frames_and_swaps.md]] / 逐句标签成品语料（真源）[[p3_answers_tagged.md]] / 训练计划 [[p3_training_plan.md]]。

---

## ⭐ 一、核心方法：听问题的 SHAPE → 调一个 FRAME

这是 P2「每个 bullet 各调一个模式」的 P3 类比。**差别在切的粒度**：P2 一道题切 4 次（每 bullet 一次 = **组合**），P3 一道题切 **1 次**（整道题就一个 function = **单 frame**）。考官的疑问词 / stem 直接暴露 function——**听 stem 选 frame，零考场活决策**，和 P2「读 bullet 措辞就知道跑哪个」完全同构。

```
听问题 stem → 1 秒分类成 8 function 之一 → 调对应 FRAME → STANCE 开口买时间 → 跑 spine（stance→because→eg→land）
```

> 🔑 **整个 P3 系统区别于 P2 的最大单点设计决策（必读）：散句不垮、垮的是词。**
> 语料实证：她的中段连接词（`because / since / so / which / for instance / plus / whereas / on the other hand`）**全部已 cold 掌握**——P3 frame **绝不重教连接词**。每个被 flag 的 leak 都是一个 **abstract noun**（function / predictability / generation gap / sense of achievement / attention spans / highlight reel / durability / range anxiety）。所以 P3 frame 只 ship 两样东西：
> 1. **per-function 的 OPENER GLUE**（2-5 词的表态 / 数量 commit，买时间、防 freeze）——这是 P3 的「HOOK」。
> 2. **floor-level 的 abstract-noun 预载 swap**（她卡的就是够到那个抽象名词的瞬间，把名词预降成大白话）。
> 中段她自己 own，**不给她加 budget 去想连接词**。

---

## 二、问题的自然动作：STAND / SPLIT / SORT（理解这层，frame 不用背 = 听出来）

> P2 的 bullet mnemonic 是 SHOW（给我看）/ TELL（讲故事）/ JUDGE（你怎么看）。P3 没有「给我看一个东西」也没有「讲一段经过」——P3 全是抽象讨论。所以塌成 **P3 三动作 mnemonic = STAND / SPLIT / SORT**。听出问题在要哪个大动作，frame 自动跟上。

| P3 自然动作 | 大类 | 覆盖的 function | 你的动作 |
|---|---|---|---|
| **「站个队」**（你信哪个 / 会不会 / 将来咋样） | **STAND** 表态 | OPINION · TWO-SIDED · PREDICT | 先甩一个立场词，再讲为什么 |
| **「摆两边」**（X 和 Y 咋分 / 谁更好 / 过去 vs 现在） | **SPLIT** 摆两边 | COMPARE · CHANGE | 命名差异的那个轴，再 `X… 而 Y…` |
| **「列出来」**（为啥 / 哪几种 / 谁能 / 有多少） | **SORT** 列出来 | REASON · ENUMERATE · FREQUENCY | 先甩数量 / 主因词，再列 2-3 颗珠子 |

> **运行口诀（考场默念）**：`听到 → STAND / SPLIT / SORT？ → 对应那句 opener glue 先出口`。三动作各有一句「万能 opener 起手」（STAND→`Definitely.` / `Not really, no.` · SPLIT→`They're quite different, I reckon.` · SORT→`Loads, actually.` / `Mainly [X], I'd say.`），所以即使 1 秒没分清细 function，**先按大动作出口一个 opener 也不会死机**——这就是 P3 的防 freeze 第一层。

---

## 三、stem → function 速查表（听 stem 措辞就知道跑哪个 frame · 对齐语料）

| 问题 stem 长这样 | function | 大动作 / opener |
|---|---|---|
| `Do you think…?` / `Should…?` / `Is it good/important/necessary to…?` / `Some people think X, what do you think?` | **OPINION/AGREE** | STAND → `Definitely.` / `Honestly, it depends…` |
| `advantages and disadvantages` / `positive and negative` / `is it good or bad` | **TWO-SIDED** | STAND → `It's a bit of a mixed bag, honestly.` |
| `differences between X and Y` / `which is more…` / `do people prefer X or Y` / `how do X and Y differ` | **COMPARE** | SPLIT → `They're quite different, I reckon.` |
| `Why do people…` / `Why are some people…` / `Why do most children…` | **REASON/WHY** | SORT → `Mainly [X], I'd say.` |
| `What kinds of…` / `What types…` / `What things…` / `Who can…` / `What can X do to…` | **ENUMERATE/WHAT-KINDS** | SORT → `Loads, actually.` / `Quite a few, actually.` |
| `How has X changed` / `differences past vs today` / `in recent decades` | **CHANGE/PAST-PRESENT** | SPLIT → `Massively, yeah.` + `We used to…, but now…` |
| `Will X…` / `do you think X will…` / `in the future` / `universally` | **PREDICT/FUTURE** | STAND → `I really don't think so.` / `I doubt it.` |
| `Are there many…` / `Do people in your country…` / `Where do people…` | **FREQUENCY/COUNTRY** | SORT (light) → `Oh, tons of them.` / `These days, most people just…` |

> ⚠️ **DRIFT vs 旧 5-frame**（`03_question_types.md` §P3）：旧系统只有 5 frame（Compare / Cause-Effect / Agree-Disagree / Hypothetical / Prediction），把 ENUMERATE、TWO-SIDED、FREQUENCY 都漏了——而语料实证 **ENUMERATE 是第二高频 function**，且旧系统没法处理「列举/有多少/在哪」这一大类。新系统用 8 function。频次（6 批合计）：

📊 **OPINION 107 · ENUMERATE 77 · REASON 49 · COMPARE 38 · FREQUENCY 23 · TWO-SIDED 10 · CHANGE 8 · PREDICT 7**（319 张明确归类 + ~5 张混合/难分 = 324；频次为分类子集的近似分布，非 324 的精确划分）。

> 旧 frame 的「Hypothetical / Should」并入 OPINION（`Should…` = OPINION stem）。**以本系统 + 语料为准**，旧 5-frame 退到参考。

---

## 四、三个 workhorse + frame 投资优先级（语料实证哪几个最高频）

> 语料实证 **OPINION + ENUMERATE + REASON = 233/324 ≈ 72%**。frame 教学的脚手架预算必须压倒性投在这三个。

| 投资档位 | function | 语料张数 | 教学动作 |
|---|---|---|---|
| ⭐ **WORKHORSE（重投）** | OPINION · ENUMERATE · REASON | 107 / 77 / 49 | 多 opener 桶、多预载 floor 名词、反复 drill |
| 🟡 **小样本但骨架最干净** | TWO-SIDED · CHANGE · PREDICT | 10 / 8 / 7 | 各一个清晰 skeleton 即可（骨架水晶清晰） |
| ✅ **最轻 / 最低 freeze** | COMPARE · FREQUENCY | 38 / 23 | COMPARE 她连接词最强（只给 opener+land）；FREQUENCY 当一组的 warm-up / confidence opener |

---

## 五、UNIVERSAL SPINE：P3 的 STANCE → because → e.g. → land

P2 的脊是 `HOOK → CORE → …bullet 模式… → EXPLAIN=LAND`（多块）。P3 的脊更短更固定，**每道 P3 答案都是同一条 4 拍脊**（= `05_path` 既有 `表态→because→like→对比` framework 的扩展与对齐）：

```
STANCE/DIRECT-ANSWER  →  BECAUSE（机制,不是 "because good"）  →  e.g. EXAMPLE 或 SECOND-POINT  →  (可选) LAND 让步收尾
```

| 拍 | P3 脊 | = P2 类比 | 作用 | glue 来源 |
|---|---|---|---|---|
| 1 | **STANCE / DIRECT-ANSWER** | = HOOK（买时间的万能第一拍） | 2-5 词先 commit 一个立场 / 数量，**堵死 freeze** | per-function opener（§六各 frame） |
| 2 | **BECAUSE（机制）** | = EXPLAIN 的 because 行 | 给 HOW 它管用，不是 "because it's good" | 她自己的 `because/since/so`（**不教**） |
| 3 | **e.g. EXAMPLE / SECOND-POINT** | = body bullet | 一个具体例子 `For instance / like…` 或第二个点 `Plus…` | 她自己的 `for instance/like/plus`（**不教**） |
| 4 | **LAND（可选让步）** | = EXPLAIN=LAND 收尾 | 一句让步收干净，**不引入新词** | 通用 land tic（见 §五.1） |

**和 P2 的核心同构**：P2「HOOK buys time」（54/54 张全用 HOOK 开，最该 drill 到自动）→ P3「STANCE buys time」（语料里每张答案首 2-5 词都是一个 stance / 数量 commit，无例外）。**STANCE 是 P3 唯一最该背到自动的东西**，理由完全同 P2 的 HOOK：freeze 风险最高的开口那一刻，它给你买 3-5 秒。

> ⚠️ **长度纪律（P3 ≠ P2）**：P3 一道答案 = **3-5 句 / ~30-50s / ~45-65 词**，**不是** 2-min monologue、**没有** 4-paragraph 结构。脊跑完就停。Pattern 是：STANCE → because（1 个）→ for instance（1 个）→ land（1 句），4 句即可下车。**别让她试图列 5 个点或铺两个对比**（语料里没有一张这么干）。

### 五.1 LAND tic —— 通用收尾池（跨所有 function 复用，verbatim）

语料最强发现：**一句让步 land 收所有 function**。dedup 后的通用收尾池（全部列出，但 drill 重点 = 前两个）：

- ⭐ **`To be fair, …`**（最高频，跨 OPINION / REASON / ENUMERATE / COMPARE）
- ⭐ **`Having said that, …`**（跨 OPINION / TWO-SIDED / CHANGE / FREQUENCY）
- `That said, …` / `Still, …`
- `So it's not black and white.`（COMPARE）
- `So it's a mix now.` / `It's about balance, really.`（CHANGE / OPINION）
- `so it really depends what you're after.`（COMPARE）
- `So it's tough, but worthwhile.`（OPINION 二面收）
- `So I'd say it'll add to it, not replace it.` / `it'll help, not replace it.`（PREDICT 默认收）
- `and that's about it really.`（ENUMERATE 收短）

> 教学动作：**drill `To be fair` + `Having said that` 两条当万能 P3 closer**，让她压力下不用选。「先 concede 一小点，然后停」= 她最便宜的 Band-7 收尾。

---

## 六、8 个 FRAME 的固定 glue（背一次 glue，填珠子 —— 全部 verbatim from 语料）

> 哲学：**只背少量固定 opener glue 字符串，填珠子，不背 prose。** 每个 frame 给：① 固定 OPENER glue（= P3 的 HOOK，买时间）② 中段 shape + 连接 glue（她已有，标「不教」）③ LAND tic ④ fill-in skeleton ⑤ floor-level 降级 swap ⑥ whichStems。

---

### ⭐ Frame 1 — OPINION/AGREE（107 张，DOMINANT · STAND）

**OPENER glue（背 3 桶，1 秒选一）**——她最该背到自动的一组（覆盖最多题）：
- **AGREE 桶**：`Definitely.` / `Absolutely.` / `For sure.` / `Definitely, I think they should.` / `Yes, very much so.` / `Hugely important, honestly.` / `Absolutely, within reason.`
- **DISAGREE 桶**：`Not really, no.` / `Not at all, honestly.` / `No, I don't reckon so.` / `Not necessarily, I'd say.` / `Not for everyone, no.`
- **HEDGE 桶**：`Honestly, it depends on [the kid / the animal].` / `It depends, really.` / `I'd say it's a bit of both, really.` / `To some extent, yes.` / `I'm pretty mixed on it, to be fair.` / `It really splits people, I'd say.`
- 每桶配一个 1-词买时间 tag：`honestly` / `within reason` / `to be fair`。

**中段 shape + 连接 glue（她已有，不教）**：`because + clause`（机制）/ `since + clause` / `Plus, …`（叠第二点）/ `On one hand… But on the other…`（双面 hedge）/ `But if it tips into [X], …`（条件让步）。

**LAND tic**：`To be fair, though, it's also rewarding…` / `Having said that, it can backfire if…` / `It's about balance, really.` / `So it's tough, but worthwhile.`

**fill-in skeleton（背 glue 填珠子）**：
```
[AGREE/DISAGREE/HEDGE opener]. [主体] because [机制珠子], so [downstream 珠子].
For instance, [一个具体例子珠子]. To be fair, [一句让步珠子].
```

**floor-level swap（这 function 的真 leak）**：
| 别追（会卡） | 改说（能 cold 说） |
|---|---|
| the pressure never really lets up | the pressure doesn't really stop |
| highlight reel | their best moments / the good bits |
| tips into pure ego | turns into showing off |
| feels hollow | feels empty / pointless |
| blanket ambition | everyone being ambitious |
| at the heart of what they do | a really big part of their work |

**whichStems**：`Do you think…?` / `Should…?` / `Is it important/good/necessary to…?` / `Some people think X — what do you think?`（旧 frame 的 Hypothetical / `Should the government…` 全并入此处）。

> ⚠️ **trap**：OPINION 答案天然会走两面（via `To be fair / Having said that` 让步），但**它不是 TWO-SIDED**——只 concede 一句就收，**不要铺成对称两段**。OPINION 是 STAND（站队后让一步），TWO-SIDED 才是真两边平衡。

---

### ⭐ Frame 2 — ENUMERATE/WHAT-KINDS（77 张，2nd 高频 · SORT）

**OPENER glue（背这组数量-commit，是 P3 最便宜的买时间）**——先甩一个数量词把方向 commit，再一拍接龙列珠子：
- `Loads, actually.` / `Loads of small steps, really.` / `Loads of creative ones, I'd say.`
- `Quite a few, actually.` / `Quite a mix, really.` / `There's quite a range, honestly.`
- `Plenty of them.` / `There's loads they can do, really.`
- **起点变体（直接命名 THE 最大那个，避免冷扫）**：`The biggest one's [X], I'd say.` / `Mainly [X], I reckon —` / `A few key things, I'd say.`

**中段 shape + 连接 glue（她已有，不教）**：列表链 `like A, B or C. But there's also Y, such as…` / `There's [X]… Then there are [Y]… Plus [Z]…` / `Even small gestures like [X]` / `What's more, [Y] is a big one`。

**LAND tic**：`To be fair, [一个软化/边界].` / `and that's about it really.` / `So really, it's [一句收束].`

**fill-in skeleton**：
```
[数量 opener]. The biggest one's [珠子1] — [一句展开].
There's also [珠子2], like [珠子3]. To be fair, [收尾珠子].
```

**floor-level swap**：
| 别追（会卡） | 改说（能 cold 说） |
|---|---|
| boils down to | it's mostly about / it comes down to |
| predictability | people know what to expect |
| modelling it themselves | just doing it themselves |
| hands-on, visual learners | people who learn by doing / by watching |
| mapping out a career | planning a career |
| in total isolation | completely on their own |

**whichStems**：`What kinds of…` / `What types…` / `What things…` / `Who can…` / `What can X do to…` / `How do people [learn/decide]…`（机制型但答成 list）。

> ⚠️ **trap**：开数量词 → 命名 THE 最大 / 最快那个 → `For instance / like` 一个例子 → 停（3-4 句）。**别让她试图列 5 个**——语料里没有，她会冷扫死机。

---

### ⭐ Frame 3 — REASON/WHY（49 张 · SORT）

**OPENER glue（背这组主因-commit）**——先甩一个主因，她就不是冷枚举：
- `Mainly [X], I'd say.` / `Mostly [X], I reckon.` / `Mainly trust, I'd say.`
- `Well, it's mostly about [X], really.` / `Well, I'd say it's mostly about freedom —`
- `I reckon it's mainly because [clause].` / `Mostly it's pride and fear, I'd say.`（命名两个主因）
- `A couple of reasons, really.` / `Loads of reasons, really.`
- `Mainly because of [noun].`（⚠️ 见下 drill 点）

**中段 shape + 连接 glue（她已有，不教）**：`since + clause` / `so + 结果` / `Plus, …`（叠第二因）/ `For instance, …` / `Young folk… while older people…`（对比因）。

**LAND tic**：`To be fair, though, …` / `That said, with a bit of patience…` / `It's a sense of belonging, really.`（注意此处 leak，见 swap）。

**fill-in skeleton**：
```
[主因 opener]. [主体 clause] since [机制珠子].
Plus, [第二因珠子]. To be fair, [让步珠子].
```

**floor-level swap（REASON 是 abstract-noun leak 重灾区）**：
| 别追（会卡） | 改说（能 cold 说） |
|---|---|
| comes down to function | it's about what it's for（预载 "what it's for"） |
| generation gap | they grew up in a different time |
| sense of achievement | feels good when it works |
| sense of belonging | feeling part of it |
| bragging rights | something to brag about |
| drone on | talk on and on |
| pilgrimage | a kind of dream trip |
| wiring themselves up | still developing |

> 🔴 **DRILL 点（她 6/22-23 的精确 error）**：`mainly because OF + noun` vs `mainly because + clause`。语料有正确 exemplar `mainly because of the huge population`（FREQ frame）。**预载成固定 chunk 对比**，是高价值 drill 靶：
> - `mainly because of` + **名词**（the huge population / the price）
> - `mainly because` + **整句**（they grew up differently / it's free）

**whichStems**：`Why do people…` / `Why are some people…` / `Why do most children…` / `Why do some prefer…`。

> ⚠️ **trap**：她的 `because/so/if` 连接词 **FINE，不要 over-teach**。leak 只在抽象名词。frame 的全部价值 = opener + 预载 floor 名词。

---

### Frame 4 — COMPARE（38 张 · SPLIT）

**OPENER glue（先 commit「有差异」再命名轴）**：
- `They're quite different, I reckon.` / `They're worlds apart, really.`（出现 2× verbatim，最可复用）/ `They're worlds apart, honestly.`
- `Quite a lot, honestly.`（差异多）/ `There's a big gap, honestly.` / `The biggest gap is space, I reckon.`（命名轴）
- `Honestly, it depends what you're after.` / `It really depends on the person, but…`
- `Honestly, it shifts with age.`（轴 = 年龄）

**中段 shape + 连接 glue（她的 STRENGTH，绝不 over-teach）**：`Some are A… while others B` / `X tends to… whereas Y…` / `With X, you…; Y, on the other hand, …` / `X, though, tends to be…`。

**LAND tic（命名那一个维度收束 —— 不引入新词）**：`So it's really about [purpose / what they're after].` / `So it's not black and white.` / `so it really depends what you're after.` / `So I'd say they're helpful in totally different ways.` / `so the smartest brands tend to mix both.`（"which is better" 型避免硬选）。

**fill-in skeleton**：
```
[差异 commit opener]. [名词轴].
[X] tends to [A], whereas [Y] [B]. So it's really about [那一个维度珠子].
```

**floor-level swap**：
| 别追（会卡） | 改说（能 cold 说） |
|---|---|
| horses for courses | **DROP** → it depends what they're after / different things for different people |
| attention spans | how long they can focus |
| lean towards | go more for / prefer |
| snappy content | short fast videos |
| carry more weight | matter more |
| the main difference is depth | the main difference is how deep it is |

**whichStems**：`differences between X and Y` / `which is more effective/better` / `do people prefer X or Y` / `how do X and Y differ`。

> ⚠️ **trap**：COMPARE 是她连接词最强的 function。frame 的价值 **只在 opener（commit「有差异」）+ land（命名那一个维度收束）**，中段她自己跑。**真正去对比，别把 X 和 Y 各描述一段**——必须 `X tends to A, whereas Y B` 在同一句里咬住差异，不是平行铺两段。

---

### ✅ Frame 5 — FREQUENCY/COUNTRY（23 张 · 最轻 P1-ish · SORT-lite）

**OPENER glue（瞬间数量 / 概括 commit）**：
- `Oh, tons of them.` / `Sure, quite a few actually.` / `More than you'd think, especially [GROUP].`
- `These days, most people just [V]…` / `Most people here head to…`
- `In China, I'd say [X] tops the list.` / `Yeah, loads of people do these days.`
- `Honestly, yeah, all the time.` / `Honestly, it's getting harder.` / `Not as often as I'd like, sadly.`

**中段 shape + 连接 glue（她已有，不教）**：tier 链 `Most people X… Others Y… And then there's the [die-hard / minority] who Z.` / `mostly [noun]` / `mainly because of [noun]` / `since they've got the time for it`。

**LAND tic**：`Having said that, [一群反例] still…` / `But it's definitely a popular hobby among [GROUP].`

**fill-in skeleton**：
```
[数量 commit opener]. [主群体] since [一个原因珠子].
Others [次群体], because [原因]. Having said that, [反例群体].
```

**floor-level swap**：
| 别追（会卡） | 改说（能 cold 说） |
|---|---|
| sprawling out endlessly into the countryside | spreading out into the countryside |
| pull in massive crowds | are still really popular |
| gravitate towards | go for / really like |
| top the list / head to | 当固定 chunk drill（她 error zone） |
| lags behind | is still behind |
| social hub | more of a hangout spot |
| accessible | easy to get |

**whichStems**：`Are there many…` / `Do people in your country…` / `Where do people…` / `Do many people…`。

> ✅ **这是 P3 最 SAFE 的 function**——plain、concrete、短。**当一组 P3 的 warm-up / confidence opener 用**。⚠️ 但仍要扫 `because of + noun`（她 error zone）。

---

### 🟡 Frame 6 — TWO-SIDED（10 张 · STAND）

**OPENER glue（最干净的两面起手）**：
- `It's a bit of a mixed bag, honestly.` / `Honestly, it's a real mixed bag.` / `Honestly, it cuts both ways.`
- `Well, on the plus side, [X]…` / `Well, the big plus is that [X]…` / `Well, the biggest perk's [X] —`

**中段 shape + 连接 glue（背这个对称骨架）**：`On one hand, X… But on the other, Y…` / `On the plus side… The downside, honestly, is that…` / `the big plus is… On the downside, though, …`。

**LAND tic（一句 concession 收干净）**：⭐ `Having said that, you do feel a bit [downside] sometimes.` / `So it's a handy tool, though it shouldn't replace [X].` / `So I'd say it's helpful as long as you stay a bit careful.` / `I'd say the pressure often outweighs the perks.`（注意 swap）。

**fill-in skeleton**：
```
[mixed-bag opener]. On the plus side, [好处珠子].
But the downside is [坏处珠子]. So it's [净判断], though [收尾让步].
```

**floor-level swap**：
| 别追（会卡） | 改说（能 cold 说） |
|---|---|
| the pressure often outweighs the perks | the bad stuff is usually bigger than the good stuff |
| water down real connection | make the connection weaker |
| crunch data | do the numbers |
| fund loads of free services | pay for a lot of free stuff |
| manipulative / sceptical | pushy / a bit careful |
| perk | 保留（spoken OK），floor backup = the best thing is |

**whichStems**：`advantages and disadvantages` / `positive and negative impact` / `is it good or bad`。

> ⚠️ **trap**：语料里多数「advantages」问其实是**单边**（只问好处）——答 2 个好处 + ONE `Having said that` 让步即可。**她不需要写满平衡 essay**。`Having said that, [一句]` 是此 function 的标准 ender。

---

### 🟡 Frame 7 — CHANGE/PAST-PRESENT（8 张 · SPLIT）

**OPENER glue（先 commit 变了多少）**：
- `Massively, yeah.` / `Massively, I reckon.` / `A lot, actually.` / `Definitely.`
- `I think it's loads harder for young people now.`（命名方向）

**中段 shape（背这条对比骨架 —— 整个 CHANGE 答案就这一招）**：
- ⭐ `We used to [X], but now [Y].` / `In the past, people mostly [X]… Now, though, we've got [Y]…`
- 个人锚（最低抽象，最该预载）：`My parents could buy a flat on one salary, which feels unthinkable today.` / `Take cameras — film ones meant [X], but now you [Y].`
- CHANGE 子句：`The biggest shift's [X] —`

**LAND tic**：⭐ `Having said that, it's also made [X] feel a bit [downside].` / `So it's a mix now.` / `So I reckon the big shift is from [X] towards [Y].`

**fill-in skeleton**：
```
[变了多少 commit opener]. We used to [过去珠子], but now [现在珠子].
That's brilliant for [好处]. Having said that, [一个 downside].
```

**floor-level swap**：
| 别追（会卡） | 改说（能 cold 说） |
|---|---|
| keeping bonds alive over distance | staying close even far apart |
| durability towards novelty and constant upgrades | stuff that lasts → new stuff all the time |
| wholesome | healthy / good for you |
| argue their corner | stand up for what they think |

**whichStems**：`How has X changed` / `differences past vs today` / `in recent decades` / `food today vs the past`。

> ✅ **frame 价值 = `We used to X, but now Y` 这一条骨架**——她的过去 / 现在时态控制在这里 FINE，opener commit 规模 + 个人具体锚 = 全部。语料仅 8 张但骨架水晶清晰、高价值。

---

### 🟡 Frame 8 — PREDICT/FUTURE（7 张 · STAND）

**OPENER glue（commit 方向，避免硬 yes/no freeze）**：
- `I really don't think so.` / `Honestly, I doubt it.` / `I doubt they'll vanish completely.`（「会不会取代 / 消失」型默认软 no）
- `Loads of ways, honestly.`（「将来怎么帮」型）
- `I'm pretty optimistic, honestly.` / `Absolutely, they shift quite a lot.`

**中段 shape + 连接 glue（她已有，不教）**：`X is handy for [Y], but it can't match [Z]` / `Plus, [第二点]` / `I doubt they'll X completely, but they might Y a bit` / `Sure, [对方理由], but [我方]…`。

**LAND tic（ready-made 默认收尾，预载）**：⭐ `So I'd say it'll add to it, not replace it.` / `it'll help, not replace it.` / `But I don't think machines will replace [X], since [人 still need…].` / `Still, [反向力量], so [X stays].` / `Having said that, [一个不完美], so they're not a perfect fix just yet.`

**fill-in skeleton**：
```
[软方向 commit opener]. [对方理由], but [我方理由珠子].
[一个具体]. So I'd say it'll [help/add to it], not replace it.
```

**floor-level swap**：
| 别追（会卡） | 改说（能 cold 说） |
|---|---|
| complement face-to-face, not replace it | add to it, not replace it |
| that human touch and reassurance | that human side / a real person |
| vanish | disappear / die out |
| evolve into / reinvent themselves / stay relevant | change instead of dying out |
| range anxiety's slowly fading | people worry less about running out of charge |

**whichStems**：`Will X…` / `Do you think X will replace/disappear` / `in the future` / `universally accepted`。

> ✅ **最安全 hedge**：任何 future 题，「won't fully replace / it'll just help / I doubt it but…」是她最稳的默认立场。语料仅 7 张但全部走这个方向。

---

## 七、展开：太短怎么补满（不升「词」，加「拍」）

> 这是 P3 的「展开」规则。P3 答案**短就对**（3-5 句），但偶尔会短到 2 句就干了。补满的办法**和 P2 同源**：bare claim 后立刻问「能不能再加一层」——**加一颗珠子，不是换更大的词**。

**太短 = 缺了脊的某一拍。按这个顺序补（只补一拍就停）：**

1. **缺 e.g. → 加一个具体例子**（最高价值，最便宜）：claim 后接 `For instance, …` / `like…` 一个具体画面。
   - 干巴：`Kids find school boring.` → 加一拍：`…, like sitting there memorising dates they can't relate to.`
2. **缺第二点 → 加第二个 reason / 第二颗珠子**：`Plus, …` 叠一个并列点（**不是**第二段，就一句）。
3. **缺 land → 加一句让步收尾**：`To be fair, …` / `Having said that, …` 一句 concede 收干净。

> ⚠️ **展开三条铁律**：
> - **加例子或加第二个 reason，不是换更大的词**——她干巴的真因不是词穷，是认知带宽只够搭 bare claim（同口语「一句话没了」= 写作「干巴巴没副词」的同根）。解药 = bare claim 后问「能不能再加一层」。
> - **绝不展成 essay**：P3 不是 P2 的三阶段加长。补到 3-5 句、跑完脊就**下车**。补一拍够了，别铺第二个对比、别列第 5 个点。
> - **连接词她已 own，不在展开时点名连接词**——展开只点「再给一个例子」或「让步收一句」。

---

## 八、⚠️ 边界陷阱（语料抓出来的坑）

1. **别无止境列 → 命名 THE 最大那个就停**（ENUMERATE）：开数量词 → 命名最大 / 最快那个 → 一个例子 → 停（3-4 句）。语料里没有一张列 5 个，她试图列满 = 冷扫死机。
2. **快速 commit 一个 stance，别一直 hedge**：STANCE 是 P3 的 HOOK，开口 2-5 词必须先甩一个立场 / 数量买时间。`It depends` 也行，但**必须立刻接 `on [X]`** 把 hedge 落地，不能空 hedge 三秒。
3. **"because 机制" 不是 "because good"**（REASON / OPINION 通病）：第 2 拍要给 HOW 它管用——`because they're dealing with people's lives, so one small mistake matters`，**不是** `because it's good / because it's important`。空 because = 没解释。
4. **COMPARE 真去对比，别各描述一段**：必须 `X tends to A, whereas Y B` 在同一句咬住差异，**不是** X 一段、Y 一段平行铺。frame 价值就在 opener（commit「有差异」）+ 这个 whereas 轴 + land（命名那一个维度）。
5. **OPINION 的让步 ≠ TWO-SIDED 的平衡**：OPINION 站队后只 concede **一句** `To be fair…` 就收；TWO-SIDED 才铺对称两边。别把 OPINION 答成两段平衡 essay。
6. **TWO-SIDED 多数其实单边**：语料里多数「advantages」问只问好处——答 2 个好处 + ONE `Having said that` 让步即可，不需要写满平衡 essay。
7. **`because OF + noun` vs `because + clause`**（她 6/22-23 主 error zone）：`mainly because of the huge population`（名词）vs `mainly because they grew up differently`（整句）。预载成固定 chunk 对比，答后必扫。

---

## 九、P2-vs-P3 差异 + 什么 carries over

### 九.1 差异（P3 frame 系统为什么不是 P2 系统的复制）

| 维度 | P2 | P3 |
|---|---|---|
| 输入 | cue card（4 bullet，结构给好了） | 单个 cold 问题（无卡，无结构提示） |
| prep | 1 min 准备 | **零准备**，听完即答 |
| 长度 | ~2 min monologue（地板 ~160 词） | **3-5 句 / ~30-50s / ~45-65 词** |
| 切模式粒度 | 一题切 4 次（每 bullet 一个模式 = **组合**） | 一题切 **1 次**（整题一个 function = **单 frame**） |
| 结构 | HOOK→CORE→…→EXPLAIN=LAND（多块） | STANCE→because→e.g.→land（一条短脊） |
| 内容来源 | persona / 自己的具体经历（具体、私人） | **抽象 / general**（people / society / 趋势） |
| freeze 风险点 | 开口 HOOK + 中段铺长 | **per-question 开口表态 + 够到抽象名词** |
| 展开 | 三阶段加长（产出→润色加长→扫错），加拍撑到 ~2min | **不加长**——短而紧就是对的，跑完脊下车 |
| 模式数 | 9 骨架 + 补充招 | **8 frame**（一函数一个） |

### 九.2 Carries over（P2 系统直接搬过来的）

| P2 机制 | P3 对应 |
|---|---|
| **HOOK buys time**（背到自动） | → **STANCE buys time**（per-function opener，P3 唯一最该背到自动的东西） |
| **一拍接龙**（卡住一次只接一拍，给下一拍 glue 让她填一颗珠子） | → **完全沿用**：P3 卡住 → 给下一拍脊的 glue（because / for instance / land），她只填一颗。拍序 = STANCE→because→e.g.→land |
| **降级 + 地板词**（只砍真生词，不压她会的） | → **完全沿用**，且是 P3 的核心（散句不垮、垮的是词） |
| **答后扫**（说完才扫 -s / 冠词 / 固定搭配） | → **完全沿用**：P3 答完扫 `-s`（held mostly）/ `a/an`（occasional slip）/ `because of+noun` vs `because+clause` / 固定搭配（这是她 6/22-23 主 error zone） |
| **scorecard**（长度 / FC / LR / GRA） | → **沿用**，但长度维度按 P3 标准（~45-65 词 = 达标，不是越长越好） |
| **背 glue 填珠子哲学 / 一句最多一个补充护 -s** | → **完全沿用** |
| **anti-机械轮换 opener** | → **沿用**：3 桶 opener 轮换，别每题都 `Definitely` |

---

## 十、真源声明

- **ground truth = `p3_answers_tagged.md`**（逐句标 `[STANCE]/[BECAUSE]/[E.G.]/[SECOND-POINT]/[LAND]` 的 P3 成品语料，本系统所有 opener glue / land tic / skeleton / 降级 swap 全部 re-derived FROM 那 324 答案，6 批 mining 聚合）。
- 旧 `03_question_types.md` §P3 的 5-frame（Compare / Cause-Effect / Agree-Disagree / Hypothetical / Prediction）已被本 8-function 系统取代——5-frame 漏了 ENUMERATE（第二高频）、TWO-SIDED、FREQUENCY；Hypothetical / `Should` 并入 OPINION。**以本系统 + 语料为准**，旧 5-frame 退到参考。
- `05_path.md` 既有 `表态→because→like→对比` framework = 本系统 universal spine 的早期版，本系统是其对齐与扩展（STANCE→because→e.g.→land + 8 function opener 库 + 通用 land 池）。
- 对齐 P2 五件套（[[cue_driven_p2.md]] / [[p2_frames_and_swaps.md]] / [[p2_card_specs.md]] / [[p2_answers_tagged.md]] / [[p2_supplement_techniques.md]]）的结构、voice、「背 glue 填珠子」哲学。
- 关键 ruling（6/23）「散句不垮、垮的是词」：P3 frame **不重教连接词**（她已 cold own），只 ship per-function opener glue + floor-level abstract-noun 预载 swap。

**配套文件**：填空骨架 + 降级词 [[p3_frames_and_swaps.md]] · 逐句标签成品语料（真源） [[p3_answers_tagged.md]] · 训练计划 [[p3_training_plan.md]]。
