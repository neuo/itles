# P2 从 cue 入手：模式组合 + 怎么展开（v3 · 从 p2_answers_tagged 重导 6/21）

> **本文件已对齐 ground truth `p2_answers_tagged.md`**（54 张逐句标签的成品语料）。骨架的 glue 字符串、whichBullets、复用卡号、陷阱，全部 re-derived **FROM 那 54 张**，不是从旧推演稿。和旧 `p2_frames_and_swaps.md` 有出入的地方，以本文件 + 语料为准。
> 配套：填空骨架+降级词 [[p2_frames_and_swaps.md]] / 全 54 张 spec [[p2_card_specs.md]] / **信息量补充技巧 [[p2_supplement_techniques.md]]**（骨架之外把珠子长出更多）/ 范文珠子 [[ielts_p2_speaking_bank.md]] / 成品语料（真源）[[p2_answers_tagged.md]]。

---

## 一、核心方法：cue 的每个 bullet 各调一个模式 = 组合

**反套发现"一卡一模式"是错的 —— 真答案是混合。真因：cue 的每个 bullet 各调一个模式，一道 P2 = 模式的组合。** cue card 本身就是结构，**零 per-card 模版、零考场活决策**。

```
HOOK → CORE(一个角度) → 按 bullet 顺序走，每个 bullet 跑它的模式 → 末 bullet = EXPLAIN=LAND
```

- **HOOK = 万能第一拍**：语料 54/54 张全部以 HOOK 开（无例外）。它最低风险、最高复用，最该 drill 到自动 —— freeze 风险最高的那一刻它给你买 5-7 秒思考时间。
- **CORE = 第二拍角度句**：54 张里 36 张用，是除 EXPLAIN=LAND 外用得最广的 PRIMARY 骨架。
- **末 bullet 永远是 EXPLAIN=LAND**：54 张里 53 张以它收尾（唯一例外老03 用 CORE 收）。它不是一句，是 2-4 句的**落地块**。

**你不挑一个全局模式，是每个 bullet 切一次 —— 切哪个由 bullet 决定（offline 预定），考场零活决策。** 这天然处理混合卡。

模式池 = **9 个骨架**（PRIMARY）+ **若干补充招**（SUPPLEMENT，一句最多挂一个）。PRIMARY 标签：HOOK / CORE / 点名 / 平移 / 习惯 / NARRATE / NARRATE-lite / ONE-MOMENT / PLOT / FACT-DROP / WEIGH / WISH-BEAT / EXPLAIN=LAND。

---

## 二、bullet 的自然语义：SHOW / TELL / JUDGE（理解这层，模式不用背 = 听出来）

> P2 的 bullet 其实就是**任何人聊一个东西时自然会问的顺序：「是什么 → 什么样/咋回事 → 你怎么看」**。考官只是把它拆成几行。听出 bullet 在问哪一类，模式自动跟上。

**先塌成 3 个语义大类（记这个就够）—— SHOW / TELL / JUDGE：**

| 自然语义 | 大类 | 模式 | 你的动作 |
|---|---|---|---|
| **"给我看看它"**（静态：是什么/什么样/平时咋样） | **SHOW** 给我看 | DESCRIBE = 点名 / 平移 / 习惯 | 画一幅画（不动） |
| **"讲讲发生了啥"**（动态：一段经过） | **TELL** 讲给我听 | NARRATE / NARRATE-lite | 讲个故事（推时间） |
| **"你怎么看"**（主观：为什么/感受/意义） | **JUDGE** 你怎么看 | EXPLAIN=LAND | 给个说法（讲道理） |

**外加三个边角：**
- **数数**（how much/often/long/big/how many people）= **FACT-DROP** 一拍事实，答完立刻交棒。
- **掂量**（会不会受欢迎 / 两面比较）= **WEIGH** 一拍两面，摆一句再落自己边。
- **未来愿望**（你想要啥 / 怎么实现 / 为啥想要）= **WISH-BEAT**，`I'd love to… so I could…`。

**每种 bullet 真正在问啥（疑问词就暴露语义）：**
- SHOW：`what/who/where it is` = 指认哪个东西（**点名**） · `what it's like / looks like` = 让我看见它（**平移**） · `what you do there / how he does it` = 那个反复的画面（**习惯**） · 媒体的 `what's it about / what happens` = 内容三拍（**PLOT**）
- TELL：`what you did / happened / how solved` = 按顺序走一遍（**NARRATE**） · `how you met / knew / got it` = 它怎么进入你生活的（**NARRATE-lite**，一拍） · 想给个具体证据瞬间 = （**ONE-MOMENT** 嵌入小场景）
- JUDGE：`and explain why / how you feel` = 你自己怎么想（**EXPLAIN=LAND**，永远最后）

> ⚠️ **唯一最大陷阱：字面像 TELL，语义是 SHOW。** 最典型 `What you did there`（地方卡）—— 字面"做了啥"像故事，但**地方没时间线**（"然后呢"返回空），真问的是"那地方平时啥样" = SHOW（**习惯** PAN，不叙事）。这就是新03 的坑：去无聊小镇"做了啥"要 PAN 那个空荡荡的镇子，不是 then-then 讲故事。语料里 `What you did there` 一律落 **习惯**（`What I did there was V, V, and V` 新18）或 **平移**，从不落 NARRATE。

---

## 三、bullet → 模式 速查表（看 bullet 措辞就知道跑哪个 · 对齐语料）

| bullet 长这样 | 模式 | 怎么跑（语料里的 glue） |
|---|---|---|
| **任何 cue 的第一行**（是什么/谁/哪里/什么法/什么决定/什么目标） | **HOOK** | 5 个固定开头挑一个，只填 `[TOPIC]` 一颗珠子（见下§五） |
| **它是什么/在哪/谁**（What/Who/Where it is） | **点名**（最轻） | `It's basically [X], over in [WHERE].`（+可选 `It's known for [锚]`，锚是**可选**的，只 ~4/16 句有）。别问"然后呢" |
| **什么样/什么用/种了啥/会哪些语言/院里有啥**（What it's like / looks like） | **平移**（视觉主块） | `When you walk around, there's so much to see. You've got [X], like [Y]. And [下一拍].` —— 相机摇，不是时钟。`like` 挂在 "You've got…, like…" 这行 |
| **平时在那干啥/他平时怎么做/怎么学/怎么做出来的**（What you do there / how he does it） | **习惯**（反复画面） | `What [he/I] usually do(es) is V, V, and V.` + 收尾 tic：地方→`There's no rush — you can just…` / 人→`He just keeps at it.` |
| **何时/做了啥/发生了啥/怎么解决/怎么反应**（When / What you did / happened） | **NARRATE**（连接链，非模版句） | `So [起] → And then [展开] → So [转/我做了啥] → In the end [收场]`。litmus：`first…then…in the end` 成立 |
| **怎么认识/怎么知道/怎么得到的**（How you met / knew / got it） | **NARRATE-lite**（一拍起源） | `…, so that's how I [met him / heard about it].` 给一个渠道/瞬间就够，**别 then-pump** → 交给下一 bullet |
| **想给一个具体证据瞬间**（人物/事件题 "有一次他…"） | **ONE-MOMENT**（嵌入小场景） | `I remember one time [SETUP], and [he/she] just [一个生动动作].` 跑完回到 CORE/EXPLAIN |
| **讲了啥/什么剧情/什么内容**（媒体题：电影/视频/广告/书/节目） | **PLOT**（内容 3 拍） | `It's basically about [X]. → It starts with [起], then [展]. → And the cool part is [payoff].` 无剧情卡 Beat2 换 `You get to see [范围]` |
| **多少钱/多久一次/多久/多大/几个人**（How much / often / long） | **FACT-DROP**（一拍事实） | 一句平的答完立刻交棒（"一个月一两次，我通常在那…"）。⚠️ 是门不是房，别填，后面接个"胖"接收者（习惯/平移） |
| **会不会受欢迎/两面比较**（Whether popular / X vs Y） | **WEIGH**（一拍两面） | `Most people would [like it], although some [GROUP] wouldn't, because [成本]. But honestly, for me it's [worth it].` |
| **想要啥/怎么实现/为啥想要/为啥做了它**（why you'd like / what it'd take / why you did it） | **WISH-BEAT**（未来愿望/动机） | `I'd love to [X], so I could [PAYOFF].` 或目标卡 `To get there, I'd need to [步骤], so I could [PAYOFF].` |
| **And explain 为什么/感受如何** — **永远是最后一个 bullet** | **EXPLAIN=LAND**（落地块，2-4 句） | `The reason [I like it] is [角度], because [机制非"because good"]. → So [downstream payoff]. → So for me, [回扣 CORE].` |

---

## 四、各题型的典型组合（语料里真实出现的组合）

> 这些不是规定，是 54 张里反复出现的成型组合。读 bullet 就能读出来。

| 题型 | 典型组合（语料里真实） | 代表卡 |
|---|---|---|
| **人物** | HOOK → CORE（角度） → NARRATE-lite（怎么认识） → 习惯（他平时干啥） → **嵌 1 个 ONE-MOMENT 场景**（我记得有次） → EXPLAIN=LAND（佩服特质）。**"双倍佩服"**：CORE 一次 + LAND 一次。**别 then-pump 人物** | 新05 爷爷 / 新07 张伟 / 老06 老19 |
| **物品** | HOOK → CORE（我爱它哪点） → FACT-DROP（多少钱/多久前） → NARRATE-lite（怎么得的/谁传的） → EXPLAIN=LAND（常带 dash 转折"不值钱 but 珍贵"） | 老11 爷爷表 / 老20 高配电脑 |
| **地方** | HOOK → 点名（是什么/哪里） → 平移（视觉主块） → 习惯（我通常在那干啥） → EXPLAIN=LAND（感受）。**几乎纯 DESCRIBE，别 NARRATE**（地方无时间线 = "然后呢"返回空 = 新03 陷阱） | 新18 京都 / 老24 书店 / 老26 湖边 |
| **事件/场合** | HOOK（One time that comes to mind is when…） → NARRATE（连接链：起→然后→转→收场） → FACT-DROP（跟谁/在哪） → EXPLAIN=LAND（感受）。**最纯 NARRATE**，常带"At first…But…"情绪弧 | 新10 改计划 / 新23 没回信 / 老09 笑脸 |
| **经历（你做的事）** | HOOK → CORE → NARRATE（做了啥/问题） → NARRATE（怎么解决/转折） → EXPLAIN=LAND（感受/教训）。陷阱：改看法 = 假 NARRATE（前后对比）；给建议 = 引用建议+结局，中段塌缩别 then-pump | 老04 给建议 / 老18 想象力 / 老21 鼓励游泳 |
| **观点/未来/愿望** | HOOK（A [job/trip] I'd love to…） → 点名/CORE（是啥角度） → NARRATE-lite（怎么知道） → **WISH-BEAT**（怎么实现，`I'd love to… so I could…`） → EXPLAIN=LAND（自由/钱/感受） | 老01 完美工作 / 老05 VR / 老12 自驾 / 老22 日本工作 |
| **法律** | HOOK（If I could introduce a law…） → CORE（核心是啥/谁受益） → FACT-DROP（会带来什么变化） → **WEIGH**（受欢迎吗，两面） → EXPLAIN=LAND（立场）。EXPLAIN 主导最难，最需预载 | 新06 护公园 / 新22 限塑 / 新27 工厂污染 |
| **媒体/故事** | HOOK → CORE（我爱它哪点） → **PLOT**（内容 3 拍：basically about → starts → the cool part is） → WISH-BEAT（为啥看） → EXPLAIN=LAND（感受/意义）。PLOT 块永远 3 拍，是这 corpus 最定型的骨架 | 新02 SpaceX / 新20 毛毛虫 / 老16 星际 / 老27 地球脉动 |

---

## 五、9 个骨架的固定 glue（背一次 glue，填珠子 —— 全部 verbatim from 语料）

> 哲学：**只背少量固定 glue 字符串，填珠子，不背 prose。** 每个骨架 glue 下面是它真正盖哪些 bullet + 语料里见到的补充招。

### HOOK（万能第一拍，54/54）
5 个真模版（按提示类型 ~1 秒挑一个），只填 `[TOPIC]`：
1. **NOUN-pick**（人/物/地/app/书/电影/事件/店/楼，最常用 ~30 张）：`[OK so / So] the [X] I'd like to talk about is [TOPIC].`
2. **TIME-event**（a time you…，~9 张）：`[OK so] one time that comes to mind is when I [DID THING].`
3. **WANT-future**（想要的工作/旅行/科技）：`A [job/trip/tech] I'd love to [have/take/own] is [TOPIC].`
4. **DECISION/GOAL**：`[So] one important [decision I made / goal I have] is/was [TOPIC].`
5. **LAW**（假设）：`[So] if I could introduce [a/one] [new] law, it'd be one that [DOES THING].`
- **暖场词 3 选 1**：`OK so`（~20 张）/ `So`（~18 张）/ 裸开头无暖场（~16 张）。
- **第 2 行 HOOK（8 张：新04/05/06/08/12/20/23/24）**：再挂**一个**事实——时间锚（`It was on a trip a few years ago…` 新04）/ rel-who（`who took care of me when I was little` 新05）/ 时长 stakes（`It's a long-term thing, and I've had it for several years now` 新24）。HOOK 可以 1 行也可以 2 行。
- **whichBullets**：永远第一个 bullet（提示的 headline 名词/事件）。偶尔第 2 行 HOOK 预答"何时/多久"子 bullet。
- **补充招见到**：appositive（`my younger cousin, Lin` 新08）/ rel-who / which-tag / dash-unpack / so-tag / like。**HOOK 一句最多挂一个补充，绝不叠**（护 -s）。

### CORE（角度句，36/54）
3 个固定 glue（按卡型挑）：
- **人物卡** → `What really stands out about [him/her] is [ANGLE].`
- **物/地/影/节目/物件卡** → `The thing I love about it is [ANGLE].`（过去事件用 `The thing I loved about it was ___`）
- **观点/法律/目标/抽象卡** → `For me it really comes down to [ANGLE].`（注意 `really` 现在是 baked in；旧 doc 的 `For me it comes down to` 已漂移到带 `really`）
- **两个负面卡变体**：`The thing about it is ___`（新03 无聊小镇，丢掉 "I love"）/ `The thing I'll say about it is ___`（老15 不喜欢的音乐，hedge 版）。
- **whichBullets**：盖"它是什么角度"+ "为什么喜欢"的前半（CORE 给角度，EXPLAIN=LAND 给原因）。常和前一小句融合：`He's five years old, and what really stands out about him is…`（老07）。
- **补充招见到**：dash-unpack / the-kind-of（老05 `the kind of thing you wear on your head`）/ like / rel-who。约 30/41 句**裸跑无补充**——CORE 是承重角度句，要说干净。

### 点名（DESCRIBE-点名 · 薄"指认"句，14 张 / 16 行）
- **glue（主导开头词 = `It's basically`，7/16）**：`It's basically [WHAT], over in [WHERE].`（+可选 `It's known for [锚]`）
- **薄无锚尾巴**：`It's [WHAT], [WHERE/WHO], [小 tag: nothing special / and it's one I really like].`
- ⚠️ **DRIFT**：旧 doc 的 `It's kind of famous for [锚]` 在语料里出现 **ZERO 次**——真实锚一律 `It's known for [Z]`，且锚是**可选的**（只 ~4/16 行有）。很多点名行用小人情 tag 收尾而非锚：`nothing special at all`（新03）/ `and it's one I really like`（老26）/ `But it felt just like a real home`（新19）/ `nothing fancy`（老03）。
- ⚠️ **人物卡多半不用点名**——身份折进 HOOK/CORE/NARRATE-lite；点名-on-人只活在老11/老19/老21 的短关系从句。
- **whichBullets**：身份/位置 bullet（地方=WHAT+WHERE；物=WHAT；人=关系；事件法律=什么场所）。永远是 HOOK 后第一个 body 行，最轻，无时间线。
- **补充招见到**：appositive / dash-unpack / rel-where / rel-who / so-tag。

### 平移（DESCRIBE-平移 / 相机摇，10 张 / 23 行）
- **glue 三件**（背一次，换 2-3 颗 feature 珠子）：
  - 开头：`When you walk around, there's so much to see.`（地方主导；旧 doc 的 `just so much to see` 已漂移，真实是 `there's so much to see`，丢了 `just`）
  - 载体行（`like` 补充挂这）：`You've got [X], like [Y].`
  - 续摇：`And [下一拍你看到的].`
- **变体**：`There's so much to do`（老25 活动卡）/ `When you look at it, there's so much to see`（新05 院子）/ `When you look at what he does, there's a lot going on`（老23 人的活动）/ 反转负面 `there's not much to see`（新03）。
- **whichBullets**：地方/家/店/景的"什么样/看到啥"视觉中段；延伸到两张人物卡的院子 sweep（新05/老23）。⚠️ 两个 tag-drift 用例（老01 `the kind of job where…`、新22 `when you go shopping`）是泛描述 sweep 非真摇，最松。
- **补充招见到**：like（签名招，7/23 行）/ with-tag / so-tag / the-kind-of。

### 习惯（DESCRIBE-习惯 / 习惯走位，14 张 / 21 行）
- **LEAD（永远固定）**：`What [he/she/I] usually do(es) [there] is [V], [V], and [V].`
- **TAIL（挑一个收尾 tic）**：人 → `He/She just keeps at it [every day].`（可+`very patiently`）；地方 → `There's [really] no rush — you can just [低调动作].`
  - ⚠️ **mode-split**：地方=no-rush，人=keeps-at-it（语料让这分界很锐）。
- **口语 comma-restart**：`What he usually does is, he grabs his pens, sits down…`（老06/07/08 全这样，是真实降级，留着）。
- **过去时变体**（cue 问"你在那做了啥"）：`What I did there was [V]…`（新18）/ `What we usually did was…`（新07）。
- **whichBullets**：要"反复/典型动作"的 SHOW bullet（不是一次性故事）。地方="平时在那干啥"；人="他平时怎么做/怎么学/怎么做出来"。**陷阱**：地方卡"做了啥"= SHOW-习惯（PAN 典型），别 then-then。
- **补充招见到**：so-tag / dash-unpack / rel-who / rel-where / to-purpose。

### NARRATE（事件链，14 张）
- **不是固定模版句，是连接链**——只背 4 个 glue token，把事件穿过去：
  `So [起：何时/何地/谁] → And then [展开：复杂化] → So [转/反应：我做/说了啥] → In the end [收场].`
- 整条 so-spine：起/转用 `So`（21×），展开用 `And/And then`（15×），收场用 `In the end / So in the end`（8×），可选情绪弧 `At first… But after a while…`（2×）。
- **两个常用子模式**：**情绪弧** `At first [负面]… But in the end [没事/挺好]`（自带 mini 张力→解决，新10/老03）；**3 动作拍** `we visited X, ate Y, and let him Z`（一口气压缩"做了啥"，新10/新25）。
- **whichBullets**：要"讲一段顺序"的事件卡叙事 bullet（何时/做了啥/接着/怎么收场）。人物卡上盖"他做 X 的一次例子"（新21/老13 轶事）。
- ⚠️ 和 **NARRATE-lite 别混**：NARRATE = 有转折有结尾的序列；NARRATE-lite = 一两句平的背景/起源。
- **补充招见到**：so-tag（主导）/ which-tag / with-tag / to-purpose / dash-unpack。整条过去时——live trap = 时态滑移和转折动词的 -s，**答后扫**。

### NARRATE-lite（一拍起源 / how-I-met-knew-found-got，15 张）
- **JOB 1（主导起源 glue）**：`…, so that's how I [met him / got to know him / heard about it].` 那个尾巴自标 `so that's how I ___` 是签名 glue。填一个渠道/瞬间就 off，**别 then-pump**。
  - 变体：`We've known each other since university, so that's how I got to know him.`（老06）/ `A friend told me about it years ago, …, so that's how I heard about it.`（老08）/ `I actually found it by accident…`（老26）。
- **JOB 2（溢出，非起源）**：一句平的过去 backdrop/payoff 拍，无固定 glue：`[主语] [过去动词] [一个细节].` 常 `And in the end, ___` 或 `He basically ___` 收（老10/老19）。
- ⚠️ **DRIFT**：旧 doc 把 新07/新21/新25/老20 算进来是错的——它们其实跑 [N]/[NARRATE]/无。真实 15 张 = 新02/08/09/15、老01/02/05/06/07/08/10/11/19/22/26。
- **whichBullets**：怎么认识他/怎么知道它/怎么找到/怎么得到/怎么传下来 的 bullet。
- **补充招见到**：so-tag / dash-unpack / with-tag / which-tag / rel-who / like（内嵌）。

### ONE-MOMENT（嵌入小场景，5 张：新05/07/21、老09/19）
- **glue 两个钉子**：开头 `I remember one time [SETUP],` + 转轴 `and [he/she] just [一个生动动作].` 跑完回到佩服/解释。
- **多行扩展**（新07/老19）：同开头 + 对比拍 `While everyone else was freaking out, he just…` + payoff `So in about twenty minutes he fixed it — he basically saved us.`
- **开头变体**：`I remember the moment…`（老09 瞬间事件）/ 裸 `I remember he just…` 丢 "one time"（新21）。
- ⚠️ 语料里 ONE-MOMENT **全部裸跑无补充**——场景内的设备 baked 进 glue 本身（`and…just`、对比从句、payoff dash、`with this big grin` 尾像）。这是唯一不挂补充的骨架，天然护 -s。
- **whichBullets**：人物/事件卡想要 ONE 个具体证据瞬间（非整条 NARRATE）。card-specs 里是 bullet #6，骑在 习惯 之后（人物卡）或 NARRATE setup 之后（事件卡老09）。"show, don't just tell" 那颗珠子。

### PLOT（媒体内容 3 拍，5 张：新02/17/20、老16/27）
- **3 个固定 glue-stub，按序说**：
  - Beat 1（前提）：`(So) it's basically about [SUBJECT].`
  - Beat 2（弧）：`It starts with/off [START], then / and then [PROGRESSION].`（无弧卡换 `You get to see [SCOPE]` —— 老27 自然纪录片没 plot 可 start）
  - Beat 3（payoff，verbatim 不变）：`And the cool part is [PAYOFF].`
- Beat 1 + 3 永远不变，只 Beat 2 flex。整 corpus 最定型骨架（5 张各正好 3 行 = 15 行 100% 一致）。
- **whichBullets**：电影/视频/广告/书/电视的"讲什么/什么剧情/发生啥"bullet。= 媒体卡的 SHOW 块。**不盖**"为啥喜欢"（CORE+EXPLAIN=LAND）或"何时看的"（FACT-DROP/WISH-BEAT）。
- **补充招见到**：只 Beat 3 偶尔挂（新20 so-tag / 老27 which-tag）；Beat 1+2 永远裸跑——故意护 -s。Beat 3 的第三人称动词（`becomes/succeeds/looks`）是这块唯一 -s 扫描点。

### FACT-DROP（一拍事实，31 张 / 37 行）
- **glue = 就一句平事实，立刻交棒**。是**门不是房**。核心形：`[I went / I use / I'd planned / it was at] [事实], [a couple of years ago / once or twice a month / a few thousand yuan].`
- 框架开头变体：`As for how it turned out, it went really well…`（新12 结果）/ `Function-wise, it's mainly…`（老17 功能）/ `So far she speaks Chinese and English…`（新15 会啥语言）/ `The reason was partly… and partly…`（老03 原因）。
- **whichBullets**：薄低值的"数据"bullet：跟谁/何时/何地/多久一次/多少钱/多久/多大/几个人。+ 漂移集：结果（新12）/会啥语言（新15）/功能（老17）/甚至原因（老03）。是 5-bullet 卡第 4/5 个低值 bullet 的标准处理。
- ⚠️ **要"胖"接收者**：薄卡 FACT-DROP 后没料 = 开门见空。语料把它直接 route 进 习惯（老24/26/08/07）或 平移（新03/老25）。
- **补充招见到**：so-tag / rel-who / like / dash-unpack / to-purpose。-s 风险：第三人称事实（`she speaks` / `he draws almost every day`），答后扫。

### WEIGH（一拍两面，4 张：新06/19/22/27 + 老14）
> 别只背一个串，背这个收尾动作：**"两面，一拍，落我这边。"** 语料里两个形：
- **SHAPE A（法律卡投票式）**：`[As for whether it'd be popular,] most [normal] people would [like it / be for it], although some [GROUP] wouldn't[, because [成本]]. But honestly, for me it's still worth it[, because [一个理由]].`（新06/22/27、老14）
- **SHAPE B（去 vs 住 / 偏好收尾，新19，无 "most people"）**：`But honestly, I wouldn't want to actually live there. [节奏太慢], so [日常会很烦]. So for me, it's [好] for [X], but I'd [get bored].`
- 两形都落同一个词：`But honestly, for me…` / `So for me, …` —— `for me` 尾巴是全 11 行唯一不变的东西。
- ⚠️ **DRIFT**：旧 doc 只给 SHAPE A 一个串、只 scope 到"法律卡+老14"。语料实际 WEIGH 也盖**偏好对比收尾**（新19，非法律地方卡，3 行）。卡数 = 4，不是"法律卡+老14"。实践中常 2-3 短拍铺开（新19 三拍、老14 三拍），非单句密包。
- **whichBullets**：(1) 法律卡"会不会受欢迎/人们怎么看这法"= SHAPE A 投票；(2) 比较/二选一的**最后**bullet——老14"跟老师学是不是更容易"（A 当收尾）、新19"为啥你不想住那"（B）。触发 = 任何要你比两面/判受欢迎/掂量 trade-off 的 bullet。
- **补充招见到**：so-tag（新19，全 corpus 唯一挂 WEIGH 的）。其余 `because` 子句 baked 进框架本身，不算单独补充。

### WISH-BEAT（未来愿望/动机，16 张 / 21 行）
- **glue**：`[WISH-OPENER] [DESIRE], so I could [PAYOFF].`
  - WISH-OPENER 固定集：`I'd love to…`（最常）/ `I'd always liked…` / `I'd really wanted to…` / `To get there, I'd need to…`（目标卡）
  - 脊柱链几乎永远 `so I could [PAYOFF]`（软目的从句，**不是**重语法的 `if…would`）。
- **第三人称换代词**：`He'd always loved…, so he wanted…`（新09）/ `she'd love to be…, so she could…`（新08）。
- **两个退化形**：`because` 动机版（新02/20，无 `so I could`）/ hedge `I figured I'd give it a go`（老15）。
- **whichBullets**：WANT / 未来愿望 / 为啥做了它 / 怎么实现 的 bullet。目标/工作/旅行/科技-想要卡上盖计划 bullet（怎么实现/需要啥）。
- ⚠️ **WISH-BEAT 主要用于未来/愿望卡，不是普通 why**（普通 why 用 EXPLAIN=LAND）。退化的 `because I watched it…` 动机版只在过去事件卡当"为啥做"那拍。
- **补充招见到**：to-purpose / so-tag / dash-unpack / like。一句最多一个（护 -s）。`I'd need` vs `I needed` 时态，答后扫。

### EXPLAIN=LAND（落地块，53/54，**不是一句**）
- 它是 **2-4 句的落地块，永远收尾**。固定 3-move 链（铺在连续 bullet 上）：
  1. **REASON 句**：`The reason [I'd recommend it / I like it / I'm proud] is [角度], because [机制——HOW 它管用，不是 "because it's good"].`
  2. **（可选）SO-tag downstream 句**：`So [downstream——这给你啥/啥感觉]`（这行挂 so-tag 补充 ~32×）。
  3. **LAND 一句**（几乎每张）：`So for me, [一句平的回扣 CORE 角度].`
- **第一槽按卡型换**：地方/影/广告/店/节目 → `The reason I'd recommend/like/love it is…`；人物/骄傲/决定 → `How I feel is I really look up to him…` / `Honestly I really admire…`；物/目标/法律/场合 → `The reason it's important / The reason most people were smiling is…`。
- `so for me` 尾巴是常数：49 行含 `for me / for us / for him`。MECHANISM 常自成一个 bullet 起手 `Because…`（新01/02/04/23）。
- ⚠️ **DRIFT**：旧 doc 说它是单句 ~22s 收尾、"全 54 张"——语料是**多行落地块**（53 张、130 行、平均 ~2.5 行/卡）；唯一例外老03 用 [CORE] 收（`For me it really comes down to realising how much I rely on it…`）。
- **whichBullets**：几乎每张卡的**最后**bullet——"为什么/怎么感受"的所有表面形（为啥推荐/为啥重要/为啥这么做/感受如何）。是万能收尾，非 body bullet。
- **补充招见到**：so-tag（32×，全 corpus 36 个 so-tag 里 32 个落在 EL）/ dash-unpack / which-tag / rel-who / the-kind-of。把 downstream 的 `So…` 拍当 EXPLAIN=LAND glue 的一部分，不是可选 add-on。

---

## 六、展开到 ~2 分钟：加"拍"，不升"词"

> 详细招法见 **[[p2_supplement_techniques.md]]**（9 个安全补充招 + drill 优先级）。这里只记**一条总规则**：

**"先连 so/because，再润；一句一个补充不叠，6-6.5 大白话，补完回扫 -s/冠词。"**

1. **连（唯一必做）**：两个事实之间永远放一个 `so`（结果）或 `because/since`（原因）——这修你最硬的散句 gap，且**不花一个生词**。EXPLAIN 里强制。
2. **一句一补充不叠**：同一句别 `which` + `-ing` + `so` 三个一起上——**你的 -s 正是在又长又满的句子里掉的**。一句一个 bolt-on 封顶。
3. **6-6.5 大白话**：长 = 更多小拍，每拍一句大白话。绝不靠更大的词——大词正是你卡住的来源。语料全程 `comes to mind` / `I'd love to` / `the cool part is` / `keeps at it`，无 Band-8 creep。
4. **回扫 -s**：每加长一句，1 秒自查"单数主语带 -s 没？a/an 在没？"。

---

## 七、⚠️ 边界陷阱（语料抓出来的坑）

1. **新03 PAN 不叙事**：地方卡的 `What you did there` 字面像 TELL，语义是 SHOW。地方无时间线，"然后呢"返回空 → 用**平移/习惯** PAN 那个空荡荡的镇子，别 then-then 讲故事。
2. **老14 WEIGH 当结尾**：最后一个 bullet 是"跟老师学是不是更容易"——两面比较不是感受。两面摆一句 + `But honestly, for me…` 落自己边收尾，**别套 EXPLAIN=LAND 的"佩服/感受"模板**。
3. **媒体 PLOT 永远 3 拍**：新02/17/20、老16/27 全是 `basically about → starts/get-to-see → the cool part is`。无剧情卡（老27 自然纪录片）Beat 2 换 `You get to see [范围]`，别硬塞不存在的剧情弧。
4. **bespoke 卡（新26 改看法 / 老04 给建议）**：
   - **新26 改看法 = 前后对比，不是 NARRATE**：用 `[BESPOKE-before]` 旧观点 + `[BESPOKE-after]` 新观点对比，不 then-then。
   - **老04 给建议 = 引用建议 + 结局，中段塌缩**：`I told him…` + `And in the end he decided to…`，别 then-pump 把建议过程拉成故事。
5. **WISH-BEAT 用于未来卡，非普通 why**：愿望/未来/目标卡用 `I'd love to… so I could…`（新09/老01/05/12/22）；普通"为什么喜欢"用 EXPLAIN=LAND。退化的 `because I watched it…` 动机版只在过去事件卡当"为啥做"那拍（新02/20/04），别拿它替代 EXPLAIN=LAND 的收尾。
6. **LAND 保护（法律卡）**：中段 FACT-DROP 说"带来什么变化"时别把 `because→so→健康` 提前用光，留给 EXPLAIN=LAND（新06 / 新27 都把立场 because 留到最后）。
7. **FACT-DROP 要有"胖"接收者**：薄卡（老26 安静地方 / 老07 多久画一次）FACT-DROP 后没料 = 开门见空 → 直接上"我通常干啥"习惯走位（老24/26/08/07）或平移（新03/老25）。

---

## 八、真源声明
- **ground truth = `p2_answers_tagged.md`**（v2 单卡精修 54 张逐句标签）。本文件的 glue/whichBullets/卡号/陷阱全部 re-derived FROM 它。
- 旧"一卡一模式"框架（templates.md / narrate_reflex_check.md）已移 `_deprecated/`。
- 和旧 `p2_frames_and_swaps.md` 出入处（点名锚=`It's known for` 非 `kind of famous for` 且可选；CORE 的 `really` baked in；EXPLAIN=LAND 是多行块非单句；NARRATE-lite 真实 15 张；WEIGH 含 SHAPE B 偏好收尾）——**以本文件 + 语料为准**。
