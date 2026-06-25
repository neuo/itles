# P3 逐句标签 · GROUND TRUTH（每函数最干净 2-3 张 · 8 函数全覆盖）—— v1 6/23

> ⭐ **这是 P3 系统的 GROUND TRUTH（真源）**。整个 P3 教练系统的 opener glue / land tic / fill-in skeleton 全部 **re-derived FROM 本文件**（本文件 = 324-answer corpus / 6 批 mining 聚合里每函数最干净的样本）。
> ⚠️ **verbatim 范围说明**：**opener glue 与 land tic 是 corpus verbatim**（可直接背），但**正文 body 句已清洗/重组到 3-5 句地板模型**（不是逐字整段照抄原答案）——这是有意的教学选择：把 corpus 的好骨架压到她 cold 能说的长度与词级。frames / swaps 文件出现矛盾时，**以本文件 + corpus 为准**。
>
> 每张 = 一个 P3 cold 答案（**3-5 句 / ~30-50s / ~45-65 词**——不是 2-min monologue，跑完脊就下车），每句标 `[骨架拍 · glue]`，**opener glue / land glue 加粗**。
>
> **P3 唯一一条脊（universal spine）**：`[STANCE] → [BECAUSE 机制] → [E.G. 例子 / SECOND 第二点] → [LAND 让步收尾]`。= 05_path 既有 `表态→because→like→对比` 的对齐扩展。
>
> 用法：① 看标签理解每拍干嘛 ② 盖标签 shadow ③ cold 答后对照。答完**答后扫** -s / a·an / `because of+noun` vs `because+clause` / 固定搭配（她 6/22-23 主 error zone）。
>
> 标签字典：`[STANCE]`=买时间的第一拍立场/数量 commit（= P2 的 HOOK）/ `[BECAUSE]`=机制行（HOW 它管用，不是 because good）/ `[E.G.]`=一个具体例子 / `[SECOND]`=叠第二点 / `[SPLIT]`=X…而 Y…对比行 / `[TIER]`=多群体分层 / `[LAND]`=让步收尾（不引入新词）。

---

## 0. 8 函数 + 三动作速查（标签前先定位）

| 大动作 | function | 在本文件的张数 | opener 起手（STANCE 拍） |
|---|---|---|---|
| **STAND** 站个队 | OPINION/AGREE · TWO-SIDED · PREDICT | 3 + 2 + 2 | "Definitely." / "It's a mixed bag." / "I doubt it." |
| **SPLIT** 摆两边 | COMPARE · CHANGE | 3 + 2 | "They're worlds apart." / "Massively, yeah." |
| **SORT** 列出来 | REASON · ENUMERATE · FREQUENCY | 3 + 3 + 2 | "Mainly trust, I'd say." / "Loads, actually." / "Oh, tons of them." |

> 🔑 **STANCE = P3 唯一最该背到自动的东西**（同 P2 的 HOOK）：freeze 风险最高的开口那一刻，它给你买 3-5 秒。下面每张第一拍都是它，**无例外**。

---

## ⭐ 一、OPINION/AGREE（107 张 · DOMINANT · STAND）

> 三桶 opener（AGREE / DISAGREE / HEDGE）1 秒选一桶 → commit 一个立场词 → because 机制 → 一句 `To be fair` 让步收。**站队后只让一步就停，不要铺成对称两段（那是 TWO-SIDED）。**

### OP-1 · "Do you think being a doctor is easy or difficult?"

- **[STANCE]** **Honestly, it's pretty difficult.**
- **[BECAUSE]** Doctors carry a huge responsibility **because** they're dealing with people's lives, **so** one small mistake can really matter.
- **[SECOND]** **Plus,** the hours are long and the pressure doesn't really stop.
- **[LAND]** **To be fair, though,** it's also rewarding, **since** you're genuinely helping folk get better. **So it's tough, but worthwhile.**

> 🔑 **clean model 因为**：STANCE 一句 commit（`pretty difficult`）→ because 给的是机制（"dealing with people's lives → one mistake matters"）不是 `because it's hard` → `Plus` 叠一点 → `To be fair` 让步 + 一句净判断收。教科书四拍。**注意 `the pressure doesn't really stop` = 已降级**（corpus 原 `the pressure never really lets up`，floor 版）。

### OP-2 · "What do you think of communicating via social media?"

- **[STANCE]** **I'm pretty mixed on it, to be fair.**
- **[SPLIT]** **On one hand,** it's brilliant for staying in touch with people far away. **But on the other,** people scroll endlessly and it eats their whole evening.
- **[LAND]** So I reckon it's a great tool **as long as** you don't let it swallow your whole day.

> 🔑 **clean model 因为**：HEDGE 桶起手（`mixed on it`）→ 直接走 `On one hand… But on the other…` 双面 → `as long as` 条件让步收。**只三句也达标**——P3 不奖励注水。这是 OPINION 走两面的标准短打。

### OP-3 · "What do you think of people going after high positions?"

- **[STANCE]** **Honestly, I'm fine with it as long as they're not stepping on others to get there.**
- **[BECAUSE]** Wanting a top job often shows drive, **and** someone with that hunger usually pushes a whole team forward.
- **[LAND]** **But if it tips into pure ego** and they forget the people around them, **then** it starts to feel a bit empty.

> 🔑 **clean model 因为**：STANCE 自带条件（`as long as…`）= 立场 + 边界一句给完 → because 给机制（drive → pushes team） → `But if it tips into…` 条件让步收。**swap 提示**：`tips into pure ego` 她会卡 → floor `turns into showing off`；`feel a bit empty`（corpus 原 `feels hollow`，已降）。

---

## ⭐ 二、ENUMERATE/WHAT-KINDS（77 张 · 2nd 高频 · SORT）

> 先甩数量词 commit 方向（`Loads, actually.`）→ 命名 THE 最大/最先那颗 → `like / for instance` 一个例子 → `To be fair` 收。**别试图列 5 个珠子——corpus 里没有，冷扫会死机。3-4 颗就停。**

### EN-1 · "What skills can people learn from watching videos?"

- **[STANCE]** **Loads, actually.**
- **[E.G.]** You can pick up really practical skills, **like** cooking a new dish or playing a few chords on a guitar.
- **[SECOND]** **What's more,** language is a big one — people improve their listening massively just by watching shows.
- **[LAND]** So I reckon videos are brilliant for hands-on, visual learners who learn by doing.

> 🔑 **clean model 因为**：数量 opener（`Loads`）瞬间 commit "很多" → `like` 直接一个具体例子（不冷扫抽象类别）→ `What's more` 叠第二颗 → 一句收。**swap 提示**：`hands-on, visual learners` 她会卡 → floor `people who learn by doing / by watching`。

### EN-2 · "Who can children turn to for help when making a decision?"

- **[STANCE]** **Mostly their parents, I'd say,**
- **[BECAUSE]** **because** mum and dad usually know them best and want what's good for them.
- **[SECOND]** Teachers help too, especially with school or career choices.
- **[LAND]** **Honestly,** older siblings can be brilliant as well, **since** they've recently been through the same stage themselves.

> 🔑 **clean model 因为**：起点变体——直接命名 THE 最大那颗（`Mostly their parents`）避免冷扫 → because 给一句机制 → 列第二、第三颗珠子，每颗带一句小展开（`especially with…` / `since they've recently…`）。**ENUMERATE 也可以走"命名主项→补两项"，不一定靠数量词。**

### EN-3 · "What qualities help people overcome difficulties and succeed?"

- **[STANCE]** **Honestly, I'd say persistence matters most.**
- **[BECAUSE]** Talent's great, **but** plenty of gifted people give up. The ones who actually make it just refuse to quit.
- **[E.G.]** They keep showing up, day after day, even when nothing's working.
- **[LAND]** **To be fair,** a bit of luck helps too, but you can't rely on that.

> 🔑 **clean model 因为**：ENUMERATE 题但答成"命名一个最重要的 → 论证 → 让步补一个"——这是 corpus 里 ENUMERATE 最稳的形态（**不冷列清单**）。`To be fair` 让步收同 OPINION。注意她的 `but / even when` 连接词全 FINE，**不教**。

---

## ⭐ 三、REASON/WHY（49 张 · SORT）

> 先甩主因 commit（`Mainly trust, I'd say.`）→ 她就不是冷枚举 → since/so 机制（她已 own）→ `Plus` 叠第二因 → `To be fair` 收。**REASON 是 abstract-noun leak 重灾区**——floor 名词必预载。

### RE-1 · "Why do most children think education is boring?"

- **[STANCE/BECAUSE]** **Honestly, I'd say it's because a lot of schooling feels disconnected from their real lives.**
- **[BECAUSE]** Kids sit there memorising facts they can't relate to, **so** naturally it drags.
- **[E.G.]** **For instance,** learning dates by heart for a history test is just dull.
- **[LAND]** **If** lessons were more hands-on, I reckon they'd find it far more engaging.

> 🔑 **clean model 因为**：STANCE 和主因合一（`it's because…disconnected from real lives`）→ 再补一句机制 → `For instance` 一个具体例子 → `If…` 反事实收。她的 `because / so / if` 三连 **全 FINE，不点名**——frame 价值只在 opener + floor 名词。

### RE-2 · "Why do some people prefer to grow their own fruits and vegetables?"

- **[STANCE]** **Mainly trust, I'd say.**
- **[BECAUSE]** When you grow your own, you know exactly what's gone into it — no chemicals, no surprises.
- **[SECOND]** It also tastes far fresher **since** you pick it the same day.
- **[LAND]** **And to be fair,** there's a real pride in serving food you've grown yourself.

> 🔑 **clean model 因为**：主因 opener（`Mainly trust`）2 词 commit → because 解释那个因 → `also` 叠第二因（`tastes fresher`）→ `And to be fair` 收。**模板级**：`Mainly [X], I'd say.` 是 REASON 最便宜的买时间。

### RE-3 · "Why are employees reluctant to ask their managers for help?"

- **[STANCE]** **Mostly it's pride and fear, I'd say.**
- **[BECAUSE]** People worry that asking makes them look like they can't do it, **so** they'd rather struggle quietly.
- **[SECOND]** There's also the power gap, **since** managers control promotions and pay rises.
- **[LAND]** **To be fair,** a supportive boss who asks the right questions can really break down that wall over time.

> 🔑 **clean model 因为**：命名两个主因（`pride and fear`）= 一句 commit 两颗珠子，省一次冷扫 → 每因一句机制（`so they'd rather…` / `since managers control…`）→ `To be fair` 让步收。**swap 提示**：corpus 原 `look incompetent` → 已降 `look like they can't do it`。

---

## 四、COMPARE（38 张 · SPLIT）

> 先 commit "有差异"（`They're worlds apart.`）或命名差异轴 → `X tends to… whereas Y…`（她的 STRENGTH，**绝不 over-teach**）→ `So it's really about [那一个维度]` 收。**frame 价值只在 opener + land，中段她自己跑。**

### CO-1 · "Are there any differences between the videos that young and old people like?"

- **[STANCE]** **Definitely.**
- **[SPLIT]** Young people are glued to fast, snappy content, **whereas** older folk **tend to** go for slower stuff, **like** news or documentaries, **because** it's easier to follow.
- **[LAND]** I reckon it comes down to how long each group can focus and what they grew up watching.

> 🔑 **clean model 因为**：一词 STANCE（`Definitely`）commit "有差异" → 一句 `whereas` 双面 + `because` 一句因 + `like` 一个例子全塞中段（她连接词 own，吃得下）→ land 命名那个维度收。**swap 提示**：`attention spans` → floor `how long they can focus`（已降）。

### CO-2 · "How are transportation systems in urban and rural areas different?"

- **[STANCE]** **They're worlds apart, really.**
- **[SPLIT]** In cities you've got metros, buses and ride-hailing apps, **so** getting about is dead easy. Out in the countryside, **though,** options are pretty thin.
- **[LAND]** **So** most folk there rely on their own car just to get anywhere at all.

> 🔑 **clean model 因为**：`worlds apart` = corpus 最高频 COMPARE opener（出现 2×，最该背）→ `X… so…. Y, though, …` 自然对比 → `So…` 推一个后果收。**注意 land 不引入新词**——只是把对比的后果讲清。

### CO-3 · "Differences between shopping in street markets and big malls?"

- **[STANCE]** **Quite a few, actually.**
- **[SPLIT]** Street markets feel livelier and you can haggle, **but** the quality's a bit hit-or-miss. Malls, **on the other hand,** are cleaner and better organised.
- **[LAND]** I'd say markets have more character, **while** malls win on convenience, **so it really depends what you're after.**

> 🔑 **clean model 因为**：数量 opener（`Quite a few`）也能开 COMPARE → 每边一句（livelier+haggle / cleaner+organised）→ `while… so it really depends what you're after.` = COMPARE 万能收尾（避免硬选哪个更好）。**`hit-or-miss` / `worlds apart` 是 floor-OK spoken marker，保留不压。**

---

## 五、FREQUENCY/COUNTRY（23 张 · 最轻 P1-ish · SORT-lite）

> ✅ **P3 最 SAFE 的 function**——plain、concrete、短。**当一组 P3 的 warm-up / confidence opener 用。** 瞬间数量 commit（`Oh, tons of them.`）→ 分层（`Most… Others… And then there's the…`）→ `Having said that` 反例收。⚠️ 但仍要答后扫 `because of + noun`（她 error zone）。

### FR-1 · "Are there many tall buildings in your country?"

- **[STANCE]** **Oh, tons of them.**
- **[E.G.]** In big cities like Chengdu or Shanghai, new skyscrapers are going up constantly.
- **[BECAUSE/LAND]** I'd say it's **mainly because of** the huge population, **so** building upwards is really the only sensible way to fit everyone in.

> 🔑 **clean model 因为**：`Oh, tons of them.` = 瞬间数量 commit，零 freeze → 一个例子（具体城市）→ `mainly because of + NOUN` 一句因收。🔴 **DRILL 靶**：这里 `mainly because of the huge population` 是 **`because of + noun` 的正确 exemplar**（vs `because + clause`）——她 6/22-23 主 error zone，**当固定 chunk 背**。

### FR-2 · "Where do people normally watch sports events?"

- **[STANCE]** **These days, most people just watch from home on the telly,**
- **[BECAUSE]** **since** it's cheap and you don't have to fight the crowds.
- **[TIER]** Others head to a pub to watch with mates, **because** cheering with strangers is half the fun.
- **[LAND]** **And then there's** the die-hard fans who'll always pay for a ticket and go in person.

> 🔑 **clean model 因为**：`These days, most people just [V]…` = 概括 commit 起手 → 分层链 `most… Others… And then there's the die-hard who…`（FREQUENCY 标准三层）→ 每层一句因。**`head to` 是她 error-zone 固定搭配**——预载当 chunk，别现场生成。

---

## 六、TWO-SIDED（10 张 · STAND）

> 最干净的两面起手（`It's a mixed bag, honestly.` / `On the plus side…`）→ `On the plus side… The downside is…` 对称骨架 → 一句 `Having said that` concession 收。⚠️ **多数"advantages"题其实只问好处**——答 2 个好处 + ONE 让步即可，**不必写满平衡 essay**。

### TS-1 · "What are the advantages and disadvantages of AI?"

- **[STANCE/PLUS]** **Well, on the plus side, AI saves us loads of time** — it can draft emails or do the numbers in seconds.
- **[MINUS]** **The downside, honestly, is that** people start leaning on it too much and stop thinking for themselves.
- **[LAND]** **Plus** there's the worry about jobs disappearing. **So it's brilliant, but you've got to use it wisely.**

> 🔑 **clean model 因为**：opener 直接进 `on the plus side` + 第一个好处（省掉单独 STANCE 句，更紧）→ `The downside, honestly, is that…` 对称转 → `Plus… So… but…` 净判断收。**swap 提示**：`crunch data` 她会卡 → floor `do the numbers`（已降）。

### TS-2 · "Advantages and disadvantages of being a famous child?"

- **[STANCE]** **Honestly, it's a real mixed bag.**
- **[PLUS]** **On the plus side,** a famous kid gets amazing opportunities most children never get.
- **[MINUS/LAND]** **But the downside's huge** — they lose any normal childhood, **so I'd say the pressure usually outweighs the perks.**

> 🔑 **clean model 因为**：`mixed bag` opener（floor-OK spoken marker，保留）→ `On the plus side… But the downside's huge…` → 一句净判断收。**只三句达标。** swap 提示：`the pressure outweighs the perks` 她会卡 → floor `the bad stuff is usually bigger than the good stuff`。

---

## 七、CHANGE/PAST-PRESENT（8 张 · SPLIT）

> ✅ **frame 价值 = `We used to X, but now Y` 这一条骨架。** 先 commit 变了多少（`Massively, yeah.`）→ `We used to…, but now…` → 个人具体锚（最低抽象）→ `Having said that` 一个 downside 收。她的过去/现在时态在这里 **FINE**。

### CH-1 · "Has technology changed people's friendships? How?"

- **[STANCE]** **Massively, yeah.**
- **[SPLIT]** **We used to** wait days for a letter, **but now** you can message a mate halfway across the world in seconds.
- **[E.G.]** That's brilliant for staying close even when you're far apart.
- **[LAND]** **Having said that,** it's also made friendships feel a bit shallower, **since** a quick text isn't the same as actually meeting up.

> 🔑 **clean model 因为**：`Massively, yeah.` = 一词 commit 变化规模 → `We used to… but now…` 核心骨架（**整个 CHANGE 答案就这一招**）→ 一句好处 → `Having said that` 一个 downside 收。**swap 提示**：corpus 原 `keeping bonds alive over distance` → 已降 `staying close even when you're far apart`。

### CH-2 · "Differences between food today and in the past?"

- **[STANCE]** **Definitely.**
- **[SPLIT]** **In the past,** people mostly ate what was local and in season. **Now, though,** we've got food from all over the world on our doorstep.
- **[LAND]** **Having said that,** a lot of folk reckon modern food is more processed, **so it's a mix now.**

> 🔑 **clean model 因为**：`In the past… Now, though…` = `We used to/but now` 的同义骨架 → `Having said that… so it's a mix now.` 收。**`on our doorstep` / `so it's a mix now` 是 floor-OK spoken marker，保留。** 只三句达标。

---

## 八、PREDICT/FUTURE（7 张 · STAND）

> ✅ **最安全 hedge**：任何 future 题，"won't fully replace / it'll just help / I doubt it but…" 是她最稳默认立场（corpus 仅 7 张但全走这方向）。软方向 commit（`I doubt it.`）→ `Sure [对方], but [我方]` → 一个具体 → `So it'll add to it, not replace it.` 收（ready-made，预载）。

### PR-1 · "Will online communication replace face-to-face?"

- **[STANCE]** **I really don't think so.**
- **[BECAUSE]** Social media's handy for quick chats, **but** it can't match sitting down with someone over coffee.
- **[E.G.]** You miss all the body language and the little things that make a real conversation.
- **[LAND]** **So I'd say it'll add to it, not replace it.**

> 🔑 **clean model 因为**：`I really don't think so.` = 软 no（避免硬 yes/no freeze）→ `handy for X, but can't match Y` 让一步再立 → 一个具体（body language）→ **`add to it, not replace it`** = PREDICT 默认 ready-made 收尾（**预载，别现场生成**）。**swap 提示**：corpus 原 `complement face-to-face` → 已降 `add to it`。

### PR-2 · "Will shops and malls disappear in the future?"

- **[STANCE]** **I doubt they'll vanish completely.**
- **[BECAUSE]** **Sure,** online shopping keeps growing, **but** malls offer something a screen can't — you can touch things and make a day of it.
- **[LAND]** I'd say they'll just change instead of dying out, **so instead of disappearing, they'll probably reinvent themselves as more of a place to hang out.**

> 🔑 **clean model 因为**：`I doubt they'll vanish completely.` = 软 no 起手 → `Sure [对方理由], but [我方]` = PREDICT 标准让步骨架 → "change not die" land。**swap 提示**：`vanish` → floor `disappear / die out`；`evolve / reinvent themselves` → floor `change instead of dying out`（保留 `reinvent themselves` 当 spoken color OK，但她卡就降）。

---

## 📊 跨函数 LAND tic 复用池（说完每张都能挂上去的万能收尾）

> 一句让步 land 收**所有** function。drill 重点 = 前两个，压力下不用选。

| land glue | 默认挂哪些 function |
|---|---|
| ⭐ **`To be fair, …`** | OPINION · REASON · ENUMERATE · COMPARE |
| ⭐ **`Having said that, …`** | OPINION · TWO-SIDED · CHANGE · FREQUENCY |
| `So it really depends what you're after.` | COMPARE（避免硬选） |
| `So it's a mix now.` / `It's about balance, really.` | CHANGE · OPINION |
| `So I'd say it'll add to it, not replace it.` | PREDICT（默认） |
| `So it's tough, but worthwhile.` | OPINION（二面收） |
| `and that's about it really.` | ENUMERATE（收短） |

> 🔑 教学动作：**`To be fair` + `Having said that` 两条当万能 P3 closer drill 到自动**——"先 concede 一小点，然后停" = 她最便宜的 Band-7 收尾。

---

## ⚠️ 标注时反复出现的 trap（drill 前默念）

1. **STANCE 拍不能省**：每张第一拍必须是 2-5 词的立场/数量 commit。没有它 = 开口 freeze。这是 P3 唯一最该背到自动的拍。
2. **跑完脊就下车**：STANCE→because→e.g.→land，3-4 句即停。**P3 不加长**（≠ P2 三阶段），别试图列 5 个点或铺两个对比——corpus 里没有一张这么干。
3. **不点名连接词**："散句不垮、垮的是词"——她的 `because / so / since / whereas / but / if` cold 全 own。frame 只 ship ① opener glue ② floor-level abstract-noun swap。**别给她加 budget 去想连接词。**
4. **OPINION ≠ TWO-SIDED**：OPINION 站队后只让一句（`To be fair…`）就收；TWO-SIDED 才铺对称两边。别把 OPINION 撑成平衡 essay。
5. **答后扫她的 error zone**（说完才扫，不打断产出）：`-s`（mostly held）/ `a·an`（occasional slip）/ **`because of + NOUN` vs `because + CLAUSE`**（见 FR-1 的正确 exemplar）/ 固定搭配（`head to` / `top the list` / `comes down to` / `lead by example`——预载当 chunk，别现场生成）。

---

## 真源声明 · cross-links

- ⭐ **本文件 = P3 系统 GROUND TRUTH**。`[[function_driven_p3]]`（METHOD）和 `[[p3_frames_and_swaps]]`（fill-in skeleton + 降级词表）里所有 opener glue / land tic / skeleton **全部 re-derived FROM 本文件**（本文件 = 324-answer corpus / 6 批 mining 聚合的逐句标注成品）。三者矛盾时 **以本文件 + corpus 为准**。
- 旧 `[[03_question_types]]` §P3 的 5-frame（Compare / Cause-Effect / Agree-Disagree / Hypothetical / Prediction）已被本 **8-function 系统取代**——5-frame 漏了 ENUMERATE（实证最高频 77 张）、TWO-SIDED、FREQUENCY；`Hypothetical / Should…` 并入 **OPINION**。旧 5-frame 退到参考。
- `[[05_path]]` 既有 `表态→because→like→对比` framework = 本系统 **universal spine 的早期版**；本系统是其对齐与扩展（`STANCE→because→e.g.→land` + 8 function opener 库）。
- 对齐 P2 五件套（`[[cue_driven_p2]]` / `[[p2_frames_and_swaps]]` / `[[p2_card_specs]]` / `[[p2_answers_tagged]]` / `[[p2_supplement_techniques]]`）的结构、bilingual voice、emoji markers、"背 glue 填珠子"哲学。**P3 = P2 的 mirror，差在切的粒度**（P2 一题切 4 次=组合；P3 一题切 1 次=单 frame）。
- 关键 ruling（6/23）**"散句不垮、垮的是词"**：P3 frame **不重教连接词**（她已 cold own），只 ship per-function **opener glue + floor-level abstract-noun 预载 swap**。
- 协议落地：standalone P3（cold-first-with-framework + 一拍接龙）+ combined P2+P3（full_pass Round 2，每张 P2 行下挂 6 个 P3 逐 function 过）见 `[[function_driven_p3]]` 末节 + speaking-coach `SKILL.md` 的 P3 协议块。
