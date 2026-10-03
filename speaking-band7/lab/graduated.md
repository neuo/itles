# 已毕业档 · graduated.md

> **🎓 条目的归宿**（2026-08-29 从写作线移植的机制）。
>
> ```
> 毕业当天：教练**只在 problems.md 原地把状态行改成 🎓 已毕业 YYYY-MM-DD**，
>           条目和全部日志行一个字不动、不搬家。
> 搬家：    **脚本做 —— 每天收尾跑一次 `python3 speaking-band7/lab/lab.py migrate`**
>           （她 2026-09-04 定，取代此前"她手动搬"的老规矩；SKILL §3.3 ＋ §11 第 ② 件）。
>           教练仍然**只在条目原地改状态行**，⛔ 不手工搬文件、⛔ 不建清单、⛔ 不留墓碑行。
>           脚本只挪**已有的整块字节**：problems.md 里的 🎓 搬进来、本文件里已无 🎓 的搬回去；
>           墓碑/迁出条目一律不动。⛔ 不改状态、不改正文、不改任何一个数、不碰头部说明块；
>           搬完自校（正文逐字节·状态字段·check 报告·编号升序），不过就两个文件整批回滚。
> 脚本口径：lab.py 把 problems.md ＋ graduated.md **当成一个档案**读，
>           所以搬没搬都不影响 stats / count / pick / dedup / check 的任何一个数。
> 回潮：    本文件里的条目再犯 ⇒ **在原地**把状态行改回未毕业、记日志，
>           当天收尾的 `migrate` 会自动把它搬回 problems.md。
>           ⛔ `lab.py append` 拒绝往 graduated.md 里写判定行。
> ```
>
> 格式与 problems.md 完全一致（§3.1 机器契约），`lab.py check` 两个文件一起查。

---

### 1 · 同位语（一个逗号，不用 who/which）
类型 结构 ｜ 旧号 B2
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 整句

**问题是什么**
**同位语**：一个逗号就能把解释性名词块挂在名词后面，⛔ 不用 who／which 从句 ——
`my hometown is Yibin, **a small city in the south of Sichuan**`。
同一格里的邻居（别串）：`Yibin, **which is** a small city…` 是完全合法的英语、也符合旧题面，
但它把本条考点整个绕开 ⇒ 2026-09-10 起题面已把它排除。
判据一句话：这个解释块前面有没有 who／which？有 ⇒ 拆掉，只留一个逗号。

**怎么发现的**
旧 B 表迁移（B2，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流（久没出现，基线 0）。
2026-08-19 ✅ `my hometown is Yibin, a small city in the south of Sichuan`（逗号同位语，没用从句壳）⇒ 毕业。
2026-09-10 复检第 3 组发题前补了排除项，考位才真正露出来；当天复检 ✅。

**我错在哪**
她的：本条两次判定都是 ✅、历史里没有掉过（🎓 零 ❌ 线），触发原话未存。
找法：说完一个地名／人名还想再解释一句，先只放一个逗号，⛔ 别去够 who／which。

**题面**
"我老家宜宾，四川南部的一个小城市，夏天特别热。"（⛔ 不许用 who／which 从句）

- 2026-08-17 ✅ 首次进流（久没出现，基线 0）
- 2026-08-19 ✅ `my hometown is Yibin, a small city in the south of Sichuan`（逗号同位语，没用从句壳）
- 2026-09-10 📝 题面补排除项「⛔ 不许用 who／which 从句」· 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面「"我老家宜宾，四川南部的一个小城市，夏天特别热。"」——
  `Yibin, **which is** a small city in southern Sichuan, …` 是完全合法的英语、也完全符合题面，
  却把本条考点（同位语：一个逗号，⛔ 不用 who／which）整个绕开 ⇒ 判 ✅ 但等于没测。
  ⇒ 补排除项；⛔ 未说"用同位语"（那是考点本身，§6② 红线）。
- 2026-09-10 ✅ 复检 · 第 3 组 · `I'm from Yibin, a small out in the south of sichuan, where it's pretty hot in summer.`
  ★ 同位语命中：`Yibin, a small [town] in the south of Sichuan,` —— 一个逗号，⛔ 没用 who／which。
    本场发题前刚补了排除项「⛔ 不许用 who／which 从句」，考位这才真正露出来。
  ★ `a small out` ⛔ 不判错：明显是打字漏字（想写 town）⇒ §2.1 拼写／滑手不算错、不建条目
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ①④ 同级说法 ＋ 底子不明
  `Yibin, which is a small city…` 本身完全成立（换不换都行），中译英里产不出 ❌；旧 B 表迁移、原话未存、历史零 ❌ ⇒ 测不出缺口
- 备注 ⚠️ **收尾 1b 复核追加（2026-08-21）**：复查时发现 🎓#255 的 08-20 日志里有 `sleep is vital **to** health`，
  当时判 ✅ —— **那次判 ✅ 是对的，不追改**。两处不是同一件事：

  ⇒ 与 #255 的分工：#255 管**选 vital 还是 virtual**（选词），本条管 **good for 后面缺限定词**（搭配）⇒ 不并
- 备注 旧账：同位语在 08-09 之前的早期档里判过一次毕业（轮24 教、轮33 无提示自发），
  但 08-17 重新进流时按 0 起算 —— 以本条的日志为准，旧账那次不计

### 2 · 修饰语必须紧贴它修饰的那个东西（从句贴先行词／补语贴名词／状语贴动词）
类型 结构 ｜ 旧号 B2b＋B194
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 整句

**问题是什么**
**修饰语必须紧贴它修饰的那个东西**，三种形态是同一件事：
· 从句贴先行词：young people **who don't learn English** struggle to find a job
· 名词补语贴名词 ／ 地点状语挪句首：**In Japan,** there is a bias **against female managers**
· 时间副词贴动词：`I found he had gone later` 里 later 停在句尾就挂到了最近的动词 gone 上
判据一句话：这个修饰语紧挨着的，是不是它真正要修饰的那个词？不是就挪过去。
★ 本条 ＝ 原 #111（名词的补语必须紧贴名词）2026-08-19 并入 —— 同一条规则，只是形态不同。

**怎么发现的**
旧 B 表迁移（B2b＋B194，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅（原 #111）。
2026-08-19 ❌ `I found he had gone later`——later 停在句尾，被读成"他后来走的"。
2026-08-21 ✅ 复习（点名题面首测）`young people who don't learn english struggle to find a job.` ⇒ 连对 2，毕业。

**我错在哪**
她的：`I found he had gone later`　　正确：`Later I found…` ／ `I only found out later that…`
找法：写完一个修饰语，回头看它紧挨着的那个词 —— 是它要修饰的那个吗？不是就挪。

**题面**
**点名**："不学英语的年轻人找工作难。"（"不学英语的"用一个 who 从句说） ／ "在日本，社会对女性管理者有偏见。"

- 2026-08-12 ✅（原 #111）
- 2026-08-15 ❌（原 #111）
- 2026-08-16 ✅（原 #111）
- 2026-08-19 ❌ `I found he had gone later`——later 停在句尾，挂到最近的动词 gone 上，
  读成"他后来走的"；应 `Later I found…`／`I only found out later that…`
- 2026-08-20 ✅ 复习 · `young people who don't learn english to find a job`（从句紧贴 young people）
  ｜`In Japan, there is a bias against female managers.`（地点状语挪句首，没停在句尾）
- 2026-08-21 ✅ 复习（点名题面首测）· `young people who don't learn english struggle to find a job.`
  ——who 从句紧贴 young people，且这次谓语补全了（08-20 那次是 `…to find a job` 没谓语）→ **连对2，毕业**
- 2026-09-05 ✅ 复检组 · 第 4 组 · `it's hard for young people who can't speak english to find jobs. / In Japan, there is bias against female managers.`
  who 从句紧贴 young people；bias **against** female managers 介词短语紧贴 bias ⇒ 修饰语位置两句都对。
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 7 组（她原话："5-9 直接过"）
- 备注 三种形态是同一件事：从句贴先行词 ／ 名词补语贴名词（地点/时间状语挪句首）／ 时间副词贴动词
- 备注 合并 2026-08-19：#111（名词的补语必须紧贴名词）并入本条

### 3 · That's where …（高复用块）
类型 词组 ｜ 旧号 B3
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-19**（复习不再召回；再犯就把状态行改回未毕业，连对清零）｜ 题型 整句

**问题是什么**
**That's where …** ＝ 高复用块，用来点"就是在这儿／这就是…的地方"：`That's where the Yangtze River starts.`
同一格里的邻居（别串）：It starts here ／ This is the place —— 两个都合法，但都绕开这个块 ⇒ 题面正向点名 That's where。
判据一句话：中文说"就从这里／就是在那儿"⇒ 先落 **That's where**，再把句子接下去。

**怎么发现的**
旧 B 表迁移（B3，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ◎ 题面没逼出 ⇒ 当天改点名；2026-08-19 ✅ 点名 · `That's where the Yangtze river starts.` ⇒ 毕业。
2026-09-09 复检第 4 组 ✅ `That's where the Yangtze River begins.`

**我错在哪**
她的：本条历史里没有掉过（2026-08-15 那次是 ◎ ＝ 题面没逼出，⛔ 不是她错），触发原话未存。
找法：中文出现"就是从这儿／这就是…的地方"⇒ 张口先给 **That's where**，别现造句子。

**题面**
"这家咖啡馆，我就是在这儿第一次见到我老公的。"（"就是在这儿"用 **That's where** 说）

- 2026-08-11 ✅
- 2026-08-15 ◎ 题面没逼出
- 2026-08-16 ✅
- 2026-08-19 ✅ 点名 · `That's where the Yangtze river starts.`
- 2026-09-09 ✅ 复检 · 第 4 组 · `That's where the Yangtze River begins.`
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉负向排除，正向点名 That's where；换成咖啡馆场景

### 5 · -ing 描述东西 / -ed 描述人（一句里两侧都要）
类型 语法 ｜ 旧号 B10＋B157
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-17**（合并后按并入日志重算：连对 3 落在 08-17）｜ 题型 整句

**问题是什么**
**-ing 描述东西 ／ -ed 描述人**，一句里两侧都要：
`This movie is **boring**. I feel so **bored** watching it.` · `I feel **relaxed** once I see my son.` · `you are **hooked** on a new game`
判据一句话：这个形容词说的是**东西的性质**还是**人的感受**？东西 ⇒ -ing，人 ⇒ -ed。
★ 本条 ＝ 原 #94（-ed 说人的感受／-ing 说东西的性质）2026-08-19 并入 —— **完全同一条规则**。

**怎么发现的**
旧 B 表迁移（B10＋B157，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ❌（原 #94）。
2026-08-11 ❌ `I was hook` → hooked（原 #94）。
2026-08-19 ✅ `I feel relaxed once I see my son. This movie is boring. I feel so bored watching it.`（relaxed／boring／bored 三个形态一次全对）。
2026-09-04 📝 自发命中 · 新题第 2 道 · `when you say you are **hooked** on a new game`（-ed 描述人，介词 on 也对）。

**我错在哪**
她的：`I was hook`（2026-08-11）　　正确：`I was **hooked**`
找法：写完一个 -ing／-ed 形容词，问一句 —— 它贴着的是东西还是人？东西 -ing、人 -ed。

**题面**
"看到儿子我就放松了。" ／ "这部电影很无聊，我看得很无聊。"

- 2026-08-09 ❌（原 #94）
- 2026-08-10 ✅（原 #94）
- 2026-08-11 ❌ `I was hook` → hooked（原 #94）
- 2026-08-12 ✅（原 #94）
- 2026-08-16 ✅（原 #94）
- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `I feel relaxed once I see my son. This movie is boring. I feel so bored watching it.`
  （relaxed／boring／bored 三个形态一次全对）
- 2026-09-04 📝 **自发命中**（本条已毕业，只留痕、不推进数字）· 新题第 2 道
  `when you say you are **hooked** on a new game`
  ★ -ed 描述人，一次到位，介词 on 也对。
  ★ 对照本条 08-11 的日志行：`I was hook` → hooked（当时是 ❌）。
- 2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："直接过"）
- 备注 合并 2026-08-19：#94（-ed 说人的感受／-ing 说东西的性质）并入本条 —— **完全同一条规则**
  ⚠️ 合并前本条按"零 ❌ 线"判 08-19 毕业；并入 #94 的日志后发现历史有两个 ❌，
     零 ❌ 线不适用 —— 但连对已达 4，**仍然毕业，只是毕业日回正到 08-17**
- 备注 备用题面（原 #94）："这有点吓人，我自己也有点怕。"

### 6 · 预制块的情态/副词是功能核心（could/never/really 不能省）
类型 结构 ｜ 旧号 B11
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 整句

**问题是什么**
**预制块里的情态／副词是功能核心**（could／never／really 这一层不能省）：`I **could** eat hotpot every day.`
同一格里的邻居（别串）：⛔ can —— could 那层是"我天天吃都愿意"（表达喜欢），can 是"有能力"，两者不是一回事；题面用中文释义把"能"限定成夸张说法。
判据一句话：把这个情态词／副词拿掉，意思还是原来那个吗？不是 ⇒ 它就是核心，⛔ 不许省。

**怎么发现的**
旧 B 表迁移（B11，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ◎ 她答 `I can eat hotpot every day` 完全合法（"我有能力天天吃"）⇒ 题面的锅，当天加点名、次日再测。
2026-08-20 ✅ 复习（点名题面首测）· `I could eat hotpot every day.` ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `I could eat hotpot pretty much every day` —— could 没被吞。

**我错在哪**
她的：`I can eat hotpot every day`（2026-08-19；那次判 ◎ ＝ 题面没逼出，⛔ 不记错）　　正确：`I could eat hotpot every day.`
找法：中文里那个"能／从来／真的"先别丢 —— 去掉它意思变不变？变就必须说出来。

**题面**
"这家的小笼包，我能天天吃都不腻。"（"能"是夸张地说自己特别爱吃，不是说有这个能力）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ◎ 她答 `I can eat hotpot every day` 完全合法（"我有能力天天吃"）
  ⇒ 中文两种译法都成立，题面的锅 → 当天加点名"用 could 说"，次日再测
- 2026-08-20 ✅ 复习（点名题面首测）· `I could eat hotpot every day.`——could 出来了
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `I could eat hotpot pretty much every day` —— could 没被吞（pretty much 是她自己加的口语缓冲）
- 2026-09-12 📝 题面整改：点名「用 could 说一遍」→「"能"那一层不许省 · ⛔ 不许用 can」—— 原点名把考点（could 不能省）直接交出去（§6② 红线一），排除 can 之后 could 要她自己调 · 全档题面 review
- 2026-09-22 ✅ 复检第 2 组 [3] · `I'd be able to eat hotpot every single day.` —— 预制块里的情态层没省（'d be able to），也没用 can ⇒ 稳
  ★ ⛔ 不收窄回 could：题面 09-12 已整改，考点是"情态层不许丢"不是"背出 could"（§3.3 硬顺序①②）⇒ 题面不改
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 中文释义收敛）
  去掉「⛔ 不许用 can」，改用中文释义把"能"限定成夸张说法（could 那层）；换成小笼包场景
- 备注 could 那层是"我天天吃都愿意"（表达喜欢），can 是"有能力"，两者不是一回事

### 8 · 群组用 in，论坛用 on（in an online group／on a forum）
类型 搭配 ｜ 旧号 B20＋B130
状态 连对2 连错0 上次2026-09-22 ｜ **回潮 2026-08-31**（08-20 毕业 → 08-31 在 R8 重答里再犯 `on an online pet group`，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-03**（连对2 ＝ 09-01 ＋ 09-03；08-31 回潮后第二次毕业）｜ 题型 词组
　　★ 复测题面**不改**：现有题面第二句「我在一个养宠物的群里加了个好友。」与她 08-31 掉的那句逐字同场景（§4① 配套动作已满足）
　　★ 本条备注里"不走零 ❌ 线、仍需连对 3"是 08-19 旧口径；现行 ＝ **连对 2 即毕业**（她 08-20 定）

**问题是什么**
**群组用 in，论坛用 on**：
· 群 ＝ 有边界的空间 ⇒ **in**（in a WeChat group／in an online pet group／in a Facebook group）
· 论坛／平台 ＝ 面 ⇒ **on**（on a forum／on Instagram／on Reddit）
判据一句话：它是一个"能进去的圈子"还是一块"铺开的平台"？圈子 ⇒ in，平台 ⇒ on。
★ 本条 ＝ 原 #82（群组用 in，论坛用 on）2026-08-19 并入 —— 同一条介词规则。

**怎么发现的**
旧 B 表迁移（B20＋B130，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-20 ✅ 复习 · `I got to know them in an online group. I added a new friend in a pet group.`（两处 in 都对）⇒ 毕业。
2026-08-31 付息日 d 段重答 R8 · `You add a friend **on** an online pet group just because both of you are really into cats.` ⇒ **回潮**
（与本条题面第二句逐字同场景；08-20 她自己写的是 `in a pet group` ✅ ⇒ 是**退回**，不是没学过）。
★ 教练犯规留痕：那次第一遍判 ⚠️、不建条目、不回潮，理由是造得出母语句 `on a WhatsApp group` ⇒ **判轻了**；
　纠回来的路径是全档 grep 撞上本条 ⇒ 教训写死：**先 grep，再造句**（§7 四问① 不能替代 §3.1 判重第②步）。
2026-09-01 ✅ ／ 2026-09-03 ✅ ⇒ 连对 2，第二次毕业。

**我错在哪**
她的：`You add a friend **on** an online pet group…`（2026-08-31 重答 R8）
正确：`I added a friend **in** a pet group.`
找法：说"在某个群里"之前先看它有没有边界 —— 有边界的圈子一律 in，只有论坛／平台才 on。

**题面**
"在一个网上群里" ／ "在一个养宠物的群里"（两个都译）

- 2026-08-17 ✅ 首次进流 ｜同日原 #82 也 ✅
- 2026-08-19 ✅ `I got to know them in an online group`（in 用对）
- 2026-08-20 ✅ 复习 · `I got to know them in an online group. I added a new friend in a pet group.`（两处 in 都对）
- 2026-08-31 ❌ 付息日 d 段 · 重答 R8（P3 · What do you think of communicating via social media?）· **回潮**
  `You add a friend **on** an online pet group just because both of you are really into cats.`
  ★ 本条题面第二句逐字就是「**我在一个养宠物的群里加了个好友。**」——与今天这句**同一个场景**。
  ★ 本条 08-20 日志里她自己写的是 `I added a new friend **in** a pet group.` ✅
    ⇒ 今天是**退回**，不是没学过。
  ★ 判据：群 ＝ 有边界的空间 ⇒ **in**（in a WeChat group／in an online pet group／in a Facebook group）；
    论坛/平台 ＝ 面 ⇒ **on**（on a forum／on Instagram／on Reddit）。
  ★★ **教练犯规留痕（本篇唯一一处）**：第一遍我判的是 ⚠️、不建条目、不回潮，理由是造得出母语句
    `on a WhatsApp group`（BrE 口语确有此说）。**判轻了。**
    纠回来的路径 ＝ 全档 grep 撞上本条。教训：§7 四问① 的"造母语句"是**防假错**用的，
    ⛔ 不能替代 §3.1 判重三步的第②步（**全档 grep，范围含已毕业**）——
    顺序反了就会把**回潮**判成"不建条目"。以后：**先 grep，再造句。**
  ★ 复测题面够不够用（§4① 配套）：现有题面第二句与今天这句逐字同场景 ⇒ **题面不改**。
  ★ 本条备注原有「不走零 ❌ 线，仍需连对 3」是 08-19 的旧口径；现行规则 ＝ **连对 2 即毕业**（她 08-20 定）。
  ⇒ 🎓 吃到 ❌ ⇒ **撤销毕业、连对清零**（状态行手写，见下）
- 2026-09-01 ✅ 复习第1组 [7] · 题面 `我在一个网上群里认识他们的。／我在一个养宠物的群里加了个好友。`
  `I met them **in** an online group. / I added a friend **in** an online pet group.`
  考点两处介词全对（08-31 掉的正是第二句：`on an online pet group`）。
  ★ 她自己加的 online（中文第二句没有）不改变任何考位 ⇒ **不判**（同 08-20 先例）。
  ★ 教练自审留痕：一度想提"online 中文里没有" ⇒ **撤**，属 ⛔ 不必要的改动。
  ⇒ 连对0 连错1 → **连对1**（回潮后第一次翻正，差一次毕业）
- 2026-09-03 ✅ 复习第1组 [3] · 题面 `我在一个网上群里认识他们的。／我在一个养宠物的群里加了个好友。`
  `I met them **in** an online group.` ／ `I added a friend **in** a pet group.`
  **考点两句都用 in**（群组用 in，论坛才用 on）—— 两句介词一致，冠词 an／a 也都对。
  ★ 出题前第二译法自查结论沿用 09-01（题面未动）：考点位无第二译法 ——
    第二句「加了个好友」把 `through a pet group` 这条绕道堵死，介词是被句意逼出来的；
    且 3/3 次历史测试（08-24 · 08-29 · 09-01）她给出的全是介词 ⇒ 无需点名。
  ⇒ 连对1 → **连对2，毕业**（状态行手写，见上）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 5 组（第 11 题整串，她事后补的原话："11直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 备注 合并 2026-08-19：#82（群组用 in，论坛用 on）并入本条 —— 同一条介词规则
  ★ 不走零 ❌ 线：备注里明写它"改过又犯"过，只是那次发生在事件流之前 ⇒ 按有 ❌ 处理，仍需连对 3
- 备注 曾"改过又犯"（轮94 改、轮95 又犯）

### 9 · 换谓语升级：is+形容词 → 实义动词（只在说"对人的作用"时换）
类型 结构 ｜ 旧号 B22
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个也毕业"）｜ 退池 ｜ 题型 整句

**问题是什么**
**换谓语升级：is ＋ 形容词 → 实义动词**，**只在说"对人的作用"时换**。
· 说它对人的作用 ⇒ 换：`this job is very boring` → `the job really **bores** me`
· 只是描述客观状态 ⇒ **不换**：`the room **is** very quiet`（题面第二句就是这个对照）
判据一句话：这句在说"它让人怎么样"吗？是 ⇒ 换实义动词；只是说它本身什么样 ⇒ 保持 is ＋ 形容词。

**怎么发现的**
旧 B 表迁移（B22，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ◎ **教练把题面砍成一句**（丢了"这房间很安静"那个不该换的对照），她给出完全正确的原型
`this job is very boring` ⇒ 记 ◎ 不记 ❌；题面当天恢复两句并加点名。
2026-08-20 ✅ 复习（两句完整题面首测）· `the job really bores me. the room is very quiet.` ⇒ 她当天指定毕业。
2026-09-11 复检 ✅ 两句都照题面走。

**我错在哪**
她的：本条没有掉过（2026-08-19 那次是 ◎ ＝ 教练把题面砍坏了），触发原话未存。
找法：想把 is ＋ 形容词换成实义动词之前先问一句 —— 这句说的是"它让人怎么样"吗？不是就别换。

**题面**
**点名**："这工作很无聊。"（第一句用实义动词说） ／ "这房间很安静。"（这句不用换）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ◎ **教练把题面砍成一句**（丢了"这房间很安静"那个不该换的对照），
  她给出完全正确的原型 `this job is very boring` ⇒ 记 ◎ 不记 ❌；题面已恢复两句并加点名
- 2026-08-20 ✅ 复习（两句完整题面首测）· `the job really bores me. the room is very quiet.`
  ——**两半都对**：第一句换实义动词，第二句没过度套用（这正是被砍掉的那个对照）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `this job bores me. This room is really quite.`
  —— 第一句换成实义动词 bores me ✔ 第二句照题面不换 ✔ ｜ ✏️ 拼写 quite→quiet（§2.1 不算错）
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ① 同级说法
  `this job is very boring` 本身完全成立，换成 bores me 只是风格升级 ⇒ 中译英里产不出 ❌；另一半（客观状态不换）是她一直会的

### 11 · no questions asked ＋ for any reason（单数）
类型 词组 ｜ 旧号 B32＋B100
状态 连对2 连错0 上次2026-09-27 ｜ **回潮 2026-09-05**（08-20 她指定毕业 → 09-05 复检两个成员只到一个：no questions asked 有、for any reason 没调出来，撤销毕业、连对清零。★ 2026-09-07 补：这一判定 09-05 当天写进了 session 却漏了 `append`，回潮同步迟到两天） ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）｜ 题型 词组
**问题是什么**
"无理由退货"的两个固定块 —— 一条规则下的两个成员：
· **no questions asked**（questions 是被问的一方 ⇒ 过去分词 **asked**；整块背，⛔ 不拆开想时态）
· **for any reason**（reason 用**单数**）
同一格里的邻居（别串）：without a reason（合法，但不是这两个固定块）。
判据一句话：这两个块是整块背的 —— questions 后面永远是 asked，reason 永远单数。
★ 本条 ＝ 原 #188（for any reason ＋ no questions asked）2026-08-19 并入，**同题面同块**。

**怎么发现的**
旧 B 表迁移（B32＋B100，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅（原 #188）。
2026-08-19 ❌ `no questions ask`——漏了 -ed ⇒ 回潮、重新入池；2026-08-20 ✅ 后她当场指定毕业。
2026-09-05 复检 a2 第 3 组 ❌：合并条两个成员只到一个（no questions asked ✅、for any reason 没调出来）⇒ 再次回潮。
2026-09-07 ✅ 在池第 4 组两个成员都到位；2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。

**我错在哪**
她的：`no questions ask`（08-19 漏 -ed）／ 只给出 `no questions asked`、for any reason 没调出来（09-05）
正确：`no questions asked ／ for any reason`
找法：这两个块一起想 —— 一个带 questions（后面必须是 ask**ed**），一个带 reason（**单数**）。

**题面**
题面（2 句，两个成员各一句）
　① "不问原因、直接给退"（商家承诺的那种，不追问你为什么）
　② "出于任何原因"（不管什么理由都行）

**成员出题账**
① no questions asked ｜ 08-19 ❌ · 08-20 ✅ · 09-05 ✅ · 09-07 ✅
② for any reason ｜ 09-05 ❌ · 09-07 ✅
★ 08-09／08-13／08-15（原 #188 的三次）与 09-09 ⚡ 自评免测未按成员记录。

- 2026-08-09 ✅（原 #188）
- 2026-08-13 ✅（原 #188）
- 2026-08-15 ✅（原 #188）→ 当时判毕业
- 2026-08-17 ✅（原 #11）
- 2026-08-19 ❌ `no questions ask`——漏了 -ed ⇒ 回潮，重新入池
- 2026-08-20 ✅ 复习 · `you can get a refund with 7 days, no questions asked`——目标块一字不差
  ｜`with` 该是 `within`，判为打漏 in、按 §2.1 不算错、不建号 ⇒ 她当场指定毕业
- 2026-09-05 ❌ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· 两个成员只到一个：no questions asked ✅，
  for any reason 没调出来
  原句 `no questions asked`
  最小改 `no questions asked ／ for any reason`
- 2026-09-07 ✅ 复习 · 在池第 4 组 · `no questions asked. / for any reason`
  —— 合并条两个成员都到位（09-05 只到一个），reason 是单数
- 2026-09-09 ⚡ 自评免测 · 在池第 1 组（她原话："这 10 个题直接过吧，算对"）
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉英文点名与"不要 without a reason"，题面改成两个成员各一个中文块（合并条多句覆盖）
- 备注 整块背：questions 是被问的一方 ⇒ 过去分词 asked（＝ with no questions being asked），不拆开想时态
- 备注 合并 2026-08-19：#188（for any reason ＋ no questions asked）并入本条，**同题面同块**

### 13 · 共享主语减 I（一个 I 带两个动词）
类型 结构 ｜ 旧号 B35
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 整句

**问题是什么**
**共享主语减 I**：并列两个动作用的是同一个主语时，第二个 I 不用再说 —— `I get up **and** go straight to work.`
判据一句话：and 后面那个动词的主语跟前面是同一个吗？是 ⇒ 主语只说一次。

**怎么发现的**
旧 B 表迁移（B35，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `I get up and go straight to work.`（一个 I 带两个动词）⇒ 毕业。
2026-09-10 复检第 3 组 ✅ `I get up and head straight to work` —— 第二个 I 没冒出来。

**我错在哪**
她的：本条两次判定都是 ✅、历史里没有掉过（🎓 零 ❌ 线），触发原话未存。
找法：说完 and 先别急着再说一次 I —— 主语一样就直接上动词。

**题面**
"我起床然后直接去上班。"

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `I get up and go straight to work.`（一个 I 带两个动词）
- 2026-09-10 ✅ 复检 · 第 3 组 · `I get up and head straight to work` —— 一个 I 带两个动词，第二个 I 没冒出来
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；共享主语只说一次 I 是她稳定会的基础结构，不是一个能学的表达

### 14 · well away（程度旋钮：不换词只加精度）
类型 词组 ｜ 旧号 B36
状态 连对1 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-20 · 她指定** ｜ 题型 整句
　　（原话："我觉得这道题不好，我不喜欢用 well，用 far 没啥问题，这道题毕业"）
　　⇒ 判定：**这是可选升级块，不是缺口** —— `far away from the road` 本身完全正确，
　　　 well away 只是另一个说法。她已有正确产出且明确不想用这个块 ⇒ 停止召回

**问题是什么**
**well away**（程度旋钮：不换词，只加精度）—— "离马路远远的" ＝ well **away** from the road。
同一格里的邻居（别串）：`far away from the road` 本身完全正确，well away 只是另一个说法；
⛔ 标准英语 well 不叠 far（`well far` 只在英式口语俚语里出现 ＝ very far，考场语域不搭）⇒ 题面正向点名 well，后面那个词留给她。
判据一句话：well 后面能挂的是一个**闭集**，far 不在里面 —— 要调的那个词是 away。

**怎么发现的**
旧 B 表迁移（B36，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ◎ 题面没逼出（far away 也合法）→ 当天改点名。
2026-08-19 ❌ `well far from the traffic`——点名生效（她确实产出 well ＋ 一个词），但词选错。
2026-08-20 ✅ `he lives well far away from the road`：教练先判 ❌、她质疑后撤销 ——
题面当时只说"well ＋ 一个词"，`well far` 是照着点名执行的合法产出 ⇒ 按【符合题面就算对 ＋ 改题面】记 ✅，题面当天加"那个词不是 far"。
她当天指定毕业（原话见状态行下方）。

**我错在哪**
她的：`well far from the traffic`（2026-08-19）　　正确：`well **away** from the road`
找法：要用 well 加精度时先想一句 —— 它后面挂的是不是那几个固定词之一？不是就别硬挂。

**题面**
"我们家的狗，我都拴得离马路远远的。"（"远远的"用 **well** 说）

- 2026-08-17 ◎ 题面没逼出（far away 也合法）→ 08-17 改点名
- 2026-08-19 ❌ `well far from the traffic`——点名生效（她确实产出 well ＋ 一个词），但词选错
- 2026-08-20 ✅ `he lives well far away from the road`
  ⛔ **教练先判 ❌、她质疑后撤销**：题面只说"well ＋ 一个词"，`well far` 是**照着点名执行**的合法产出
  ⇒ 按 08-20 新规则【符合题面就算对 ＋ 改题面】，本次记 ✅，题面已加"那个词不是 far"
  ⚠️ 语言点仍成立、只是不计分：标准英语 well 不叠 far（well away／far away 各自成立；
     `well far` 只在英式口语俚语里出现＝ very far，考场语域不搭）
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· well away from（well ＋ away，⛔ 不是 far）
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  far away 合法 ⇒ 中文块单独映射不回 well away；改整句、正向点名 well，away 留给她（她掉过的就是 well far）；换成拴狗场景
- 2026-10-01 ✅ 复检 · 学习日 复检第 4 组 [2] · `I keep my dog leashed well aways from the road.` —— well away from（aways 拼写，§2.1 不算）
  ｜leashed 她标「这个单词背一下」⇒ 新建 #382
- 备注 更高一档的说法（房子离马路退得远）：`His house is set well back from the road.`
- 备注 well 当程度旋钮只配固定那几个：well away／well worth／well past／well over／well aware／well ahead
- 备注 08-19 她问"the road 哪个好" → the road 对（马路这条路）；the traffic 是路上的车流

### 15 · deep down（内心深处：副词块）
类型 词组 ｜ 旧号 B37
状态 连对2 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

**问题是什么**
**deep down** ＝ 内心深处（**副词块**，放句首：`Deep down, I know I should go to bed early.`）。
同一格里的邻居（别串）：in my heart ／ inside（能懂，但 deep down 才是口语里说"心底里其实知道"的那个块）
判据一句话："内心深处"想到名词（心／里面）就走错了，它是个副词块。
★ 拆号：原条目捆着三个块 —— It's not that A, it's just B 与 🎓#71 同一个框 ⇒ 归 #71；can't be bothered 拆成 #374。

**怎么发现的**
旧 B 表迁移（B37，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `deep down, I know I should go to bed early. It's not that I don't want to go. I'm just lazy.`
⭐ 她自纠：先写 `It's just lazy`，当场改成 `I'm just lazy`（lazy 说人）。
2026-09-09 复检第 4 组 ✅ 两个考点块都在位（deep down ⛔ 没用 heart／inside ＋ It's not that A, it's just B）。

**我错在哪**
她的：deep down 这一块历史里没有掉过（触发原话未存）；另两块的记录见历史行（08-19 `It's just lazy` 自纠 ／ 09-09 want to 漏译）
正确：`Deep down, I know …`
找法：说"内心深处"直接找副词块 deep down，⛔ 别去够 heart／inside。

**题面**
"心底里其实明白"（嘴上不承认、心里最真实的那一层）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `deep down, I know I should go to bed early. It's not that I don't want to go. I'm just lazy.`
  ⭐ 她自纠：先写 `It's just lazy` 当场改成 `I'm just lazy`（lazy 说人）
- 2026-09-09 ✅ 复检 · 第 4 组 · `deep down` ／ `It's not that I don't go, I'm just lazy`
  —— 两个考点块都在位：deep down（⛔ 没用 heart／inside）＋ It's not that A, it's just B
- 2026-09-09 📝 复检第 4 组 [4] 漏译留痕（⛔ 不判档位、⛔ 不建新条目）
  她答 `It's not that I don't go, I'm just lazy` —— 题面是"不是**不想**去"，`want to` 被漏掉，
  句意变成"不是我不去"。⛔ 不建条目：她会 want to（同场 #225 `I want a job…` 就在用），
  这是漏译不是缺口（§3.2b：说不出"她不会哪个词组/句型" ⇒ 不建）
  最小改 `It's not that I don't want to go, I'm just lazy.`
- 2026-09-12 📝 题面整改：第二句「不是不想去，只是懒。」→「不是不想去，只是懒得动」（⛔ 不许用 lazy）—— 去句号、与第一块统一成词组题（§6.0 一条一种形式）；"懒得动"逼的正是下面备注里那个 can't be bothered · 全档题面 review
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 拆号（§3.1 一条 ＝ 一个考点）
  原条目捆着三块：deep down 留本条；It's not that A, it's just B 与 🎓#71 同一个框 ⇒ 归 #71；can't be bothered 拆成 #374（她从没自己说出过）
  题面改成 deep down 一个中文块（零英文提示）
- 备注 第三个块 can't be bothered（懒得动）比 lazy 更口语，下次可以往这上引

### 16 · 让某人做某事四件套（get sb TO do 只有它带 to；have/make/let/watch/see sb DO）
类型 搭配 ｜ 旧号 B39
状态 连对3 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

**问题是什么**
**让某人做某事四件套**：`get sb **TO** do` —— 这一族里**只有 get 带 to**；
have／make／let／watch／see sb **DO**（光杆原形，⛔ 不加 to）。
判据一句话：动词是 get 吗？是 ⇒ 补 to；是 have／make／let／watch／see ⇒ 后面一律光杆。
★ 与 🎓#143（哪些动词后面要带 to）是同一条规则的两个角度（尾部 ⚠️ 已记，付息日 c 段处理）。

**怎么发现的**
旧 B 表迁移（B39，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ❌ 同族 `watch the machine BUILDS it`。
2026-08-19 ✅ `teachers should get students to try it themselve`（get sb TO do 选对）⇒ 毕业。
2026-09-05 ✅ `let students ... try`（原形，⛔ 没多加 to）；2026-09-07 ✅ `get students to try it themselves`。

**我错在哪**
她的：`watch the machine BUILDS it`（2026-08-11）　　正确：`watch the machine **build** it`
找法：写完 have／make／let／watch／see ＋ 人（物），后面那个动词一律光杆；只有 get 要补 to。

**题面**
"我让孩子自己把房间收拾好，还在门口看着他收完。"（"让"用 **get** 说，"看着他收"用 **watch** 说）

- 2026-08-11 ❌ 同族 `watch the machine BUILDS it`
- 2026-08-12 ✅
- 2026-08-16 ✅

- 2026-08-19 ✅ `teachers should get students to try it themselve`（get sb TO do 选对）
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· `let students ... try`（原形，⛔ 没多加 to）
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `get students to try it themselves`（get sb TO do，四件套里只有 get 带 to）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  考点是 to／光杆原形挂在哪 ＝ 靠句子现形；一句覆盖两半（get sb to do ＋ watch sb do，她掉过的是 watch 那半）
- 2026-10-01 ✅ 复检 · 学习日 复检第 4 组 [3] · `I got my kid to clean up his room and stood at the door to watch him finish.` —— get sb to do ＋ watch sb do 两处都对
- ⚠️ 与已毕业的 #143（哪些动词后面要带 to）是同一条规则的两个角度 —— 付息日 c 段处理

### 17 · talk AT sb（单向灌输）vs talk TO sb
类型 搭配 ｜ 旧号 B40
状态 连对2 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

**问题是什么**
**talk AT sb** ＝ 单向灌输（对着你说教，不听你说）／ **talk TO sb** ＝ 跟你说话（双向）。
同一格里的邻居（别串）：talk to you 同样合法 ⇒ 2026-09-12 题面补了"单向灌输那种'讲'"，at／to 的分辨才逼得出来。
判据一句话：对方有没有机会回话？没有 ⇒ talk **at**；有 ⇒ talk **to**。

**怎么发现的**
旧 B 表迁移（B40，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `some teachers just talk at you for an hour.` ⇒ 毕业。
2026-09-04 📝 自发命中 · 新题第 2 道 · `parents or order people may just **talk at you** when you say you are hooked on a new game.`
—— 隔 16 天、在完全不同的场景里自发调出来，是那一篇最硬的一条证据。
2026-09-09 复检第 4 组 ✅ `talk at you for an hour`。

**我错在哪**
她的：本条历史里没有掉过（三次判定都是 ✅ ＋ 一次自发命中），触发原话未存。
找法：说"对着某人讲"之前先问一句 —— 对方有没有机会回话？没有就用 **at**。

**题面**
"有些家长只会对着孩子说教，从来不听孩子怎么想。"（"对着孩子说教"用 **talk** 说）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `some teachers just talk at you for an hour.`
- 2026-09-04 📝 **自发命中**（本条已毕业，只留痕、不推进数字）· 新题第 2 道
  `parents or order people may just **talk at you** when you say you are hooked on a new game.`
  ★ 语义、介词、语境三层全中：talk AT ＝ 单向灌输（不听你说），她这里正是"父母只会对着你说教"。
  ★ 本条上一次被测是 **2026-08-19**（题面"有些老师就是对着你讲一小时。"）——
    **隔 16 天、在完全不同的场景里自发调出来**，是本篇最硬的一条证据。
  ｜`order` 是 older 打歪（§2.1 拼写，不算错）。
- 2026-09-09 ✅ 复检 · 第 4 组 · `talk at you for an hour` —— talk **at**（单向灌输）
- 2026-09-12 📝 题面整改：补（单向灌输那种"讲" · 用 **talk** ＋ 一个介词说）—— 原题面裸给"对着你讲一小时"，talk to you 同样合法 ⇒ at／to 的分辨逼不出来（§6.5 第 7 项）· 全档题面 review
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 talk，介词 at 留给她；"说教、不听孩子怎么想"把单向那层写进中文

### 18 · 论元完整（中文可单说的动词，英文必须带宾语/补语）
类型 结构 ｜ 旧号 B41
状态 连对2 连错0 上次2026-09-22 ｜ **累错 7** ｜ **🎓 已毕业 2026-09-01**（连对2 ＝ 08-31 ＋ 09-01；08-29 回潮后第二次毕业）｜ 题型 整句
　　★ 08-30 同日两记：[3] 点名直测 ✅ → [4] 顺带产出 ❌，连对1 当日清零（§3.3 每次各算一次）

**问题是什么**
**论元完整**：中文里可以单说的动词，英文必须把宾语／补语带出来 ——
look for **it** · find **it** · regret **it** · supply **water** for … · span **China** from west to east。
同一格里的邻居（别串）：span 后面**直接跟宾语、永远不带 to**（✓ The bridge spans the river ／ ✗ spans to east）；
"向东"不是 span 的宾语，是方向状语。
判据一句话：这个及物动词后面那个"东西"说出来了吗？中文能省，英文不能。
⚠️ **必须和 🎓#134 一起读**（08-19 判重发现两条会互相带偏）：#134 是白名单
（decide／choose／help／manage／win 这些能单独站住）—— **先查这个动词在不在白名单里**，不在才补宾语。
★ 判重口径（08-29／08-30 两次写死）：按本条规则去改，**能不能得到那句正确答案**？能 ⇒ 归本条、⛔ 不新建号。

**怎么发现的**
旧 B 表迁移（B41，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ❌（累错一路到 7）。
2026-08-19 ❌ `I found ＿ for hours`——及物动词没带宾语（look for **it**）；同日第二次 `There's no point regretting ＿ now`。
2026-08-21 ✅ 后毕业；2026-08-29 新题 P2 · `supplying for both residential and industrial use` ⇒ **回潮**。
2026-08-30 同日两记：[3] 点名直测 ✅ → [4] 顺带产出 `This river spans to east` ❌ ⇒ 连对当日清零。
⚖️ 她 2026-08-30 当场裁定（原话）："**没有什么自由或者不自由产出，只有产出你就认**"
　⇒ 点名题与自由产出一视同仁，⛔ 不分档、不加权、不设特例。
2026-08-31 ✅ ／ 2026-09-01 ✅ ⇒ 连对 2，第二次毕业。

**我错在哪**
她的：`I found ＿ for hours` ／ `supplying **for** both residential and industrial use` ／ `This river **spans to east**`
正确：`I still couldn't find **it**` ／ `supplying **water** for …` ／ `spans **China** from west to east`
找法：写完一个动词先问一句 —— 它在不在 #134 的白名单里？不在 ⇒ 把那个"东西"说出来再往下走。

**题面**
"我找了半天也没找到。"

- 2026-08-11 ❌
- 2026-08-12 ❌
- 2026-08-13 ❌
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ❌ `I found ＿ for hours`——及物动词没带宾语（look for **it**）
  ｜同日第二次：`There's no point regretting ＿ now`（regret 也要带宾语 it）—— 同日只记一次档位
- 2026-08-20 ✅ 复习 · `I searched for hours and I still couldn't found it`——**宾语 it 带上了**（考点达成）；
  searched 作不及物用法在这句里成立 ｜同句 found→find 的形态错归 #147，不算本条头上
- 2026-08-21 ✅ 复习#32 句里 · `there's no point regretting **it**.`——08-19 掉的正是这句的宾语 it，
  今天 cold 重测带上了 → **连对2，毕业**（§3.3 标记打在条目上，不打在整句上）
- 2026-08-29 ❌ 新题 P2（Describe an important river/lake）· **回潮**（08-21 毕业 → 08-29 再犯）·
  `it is the primary source for YiBin, **supplying for** both residential and industrial use across the city.`
  → supplying **water** for both residential and industrial use
  ❌ supply 是及物动词，供应的那个东西必须说出来。中文"供全市生活和工业使用"可以不说"水"，英文不行
  ★ **判重的决定性证据（为什么归本条、不新建号）**：按本条的规则去改（把动词的宾语补出来），
    得到的正是 `supplying **water** for…` —— **本条给得出那个正确答案 ⇒ 是同一条规则**，归本条、判回潮。
    ★ 对照被排除的另一条路：若按"supply for 是搭配错"去改 ⇒ `supplying both … use`
      —— 供应的不是"用途"，**还是不对** ⇒ 那条路给不出答案
  ★ 照本条备注的老规矩，必须和 🎓#134（白名单：decide/choose/help/manage/win 能单独站住）一起读 ——
    **supply 不在白名单里**，所以要补宾语
  ⚠️ 同句同根的第二处**落在名词上**：`the primary source for Yibin` → the main source **of water** for Yibin
    —— 她把"水"连丢了两次（名词一次、动词一次）。本条只管动词 ⇒ 名词那一处**不另开号**，只记在这里
- 2026-08-30 ✅ 复习第1组 [3] · 题面 `我找了半天也没找到。` ·
  `I searched everywhere, but I still couldn't find it.`
  ——考点位置达成：**couldn't find it**（中文"没找到"省了宾语，英文把 it 带上了）
  ⇒ 连对0 连错1 → 连对1 连错0（回潮后第一次翻正）
  ★ `searched everywhere` 本身不判错：search 作不及物用法在这句里成立（同 08-20 先例）
  ★ 她把题面的"半天"（时长）译成 everywhere（范围）—— 内容轻微偏移，**不是考点**，
    按 §3.3 记 ✅，题面不改
  ⚠️ **同日 [4] 里本条又掉了一次，本次的连对1 被清零 —— 见下一行**
  ★ 教练侧留痕：发题前一度想给本条补题面（因为 08-29 掉的那一格是 supply，
    原题面测的是 find／look for），四问②自审后否掉 ——
    ① §4① 那句"回潮后必须换能测到那一格的题面"适用范围是**加速通道边界**，不是普通 ❌ 回潮；
    ② 原题面本身就是同构句（中文"没找到"省宾语，英文必须补 it）；
    ③ 上两次 ✅ 是 08-20／08-21，距今 9／10 天，不构成"昨天的记忆"。
- 2026-08-30 ❌ 复习第1组 [4] 句里 · **同日第二次记录**（§3.3「同一条同一天被产出多次 ⇒ 每次各记一行、
  各算一次」）· `This river **spans to east**, eventually emptying into the East China Sea.`
  → spans **China from west to east**
  ❌ span 是及物动词，**后面直接跟宾语，永远不带 to**（✓ The bridge spans the river ·
     ✓ The empire spanned three continents ／ ✗ spans to）。"向东"不是 span 的宾语，是方向状语。
  ⇒ 本次 ❌ 把同日 [3] 刚拿到的连对1 清零 ⇒ **连对0 连错1，累错 7**
  ★★ **判重的决定性证据（为什么归本条、不新建号）**：按本条的规则去改（把及物动词的宾语补出来）
    ⇒ 得到 `spans China from west to east` —— **正是她 08-29 自己写对过的那一句**
    （见 #308 日志：「同句另外两处全对：`spanning China from west to east`」）
    ⇒ **本条给得出正确答案 ⇒ 同一条规则**。
    ★ 对照被排除的另一条路：判成"选词错（span 不表流向，该用 flow/run）"⇒ 也能得到正确句，
      但**与她的实际状态不符** —— 她 08-29 刚用对过 span＋宾语，span 不是她的选词缺口；
      今天丢的是**块的论元**（把 `span China from west to east` 压成 `span to east`）。
  ★ `to east` 那一处（缺起点、缺冠词）**不另开号**：补全块之后自动消失，
    同 08-29「名词那一处不另开号，只记在这里」的先例。
  ★★★ **本日最重要的发现**：同一条规则、同一天、隔三题 ——
    **[3] 点名直测就带上宾语（✅），[4] 顺带产出就把宾语丢了（❌）**。
    这正是本条备注里写死的形状：「primed 8/8 但 20 分钟后 cold 即掉 ⇒ 产出时掉」，
    今天把它**压缩到同一场、同一组之内**复现了一次。
  ⚖️ **她 2026-08-30 当场裁定**（教练曾提议"这类老大难是否只认自由产出里的那一次"）：
     原话 **"没有什么自由或者不自由产出，只有产出你就认"**
     ⇒ **点名题与自由产出一视同仁，一次产出就是一次记录**，⛔ 不分档、不加权、不设特例。
     ⇒ 教练提的那条出题建议**当场作废**，SKILL 一个字不改。
  ★ 同日新题 P3 里本条**没有再掉**：`search information` 缺的是介词不是宾语（判重时已排除本条）。
- 2026-08-31 ✅ 付息日 a 段第 1 组
  `I **looked for it** everywhere, but I still coundn't **find it**.`
  考点 论元完整：looked for **it** ／ find **it** 两个宾语同时在位。
  ★ 对比 08-29 回潮句 `spans to east`（缺宾语）与 08-30 的 `I searched everywhere`——
    这是回潮以来第一次两个动词的宾语同时补全。coundn't 属拼写，不计错。
  ⇒ 连对1（回潮后第一次对）
- 2026-09-01 ✅ 复习第1组 [1] · 题面 `我找了半天也没找到。`
  `I spent forever **looking for it**, but I still could't **find it**.`
  考点 论元完整：两个宾语同时在位（looking for **it** ／ find **it**）。
  ★ could't 属拼写（§2.1①），不建条目、不记档位、不计错。
  ★ 回潮（08-29）以来第四次记录：08-30 [3] ✅ → 08-30 [4] ❌（同日清零）→ 08-31 ✅ → 09-01 ✅
    ⇒ **第一次连着两天都没掉**。
  ★ 三次三种说法（searched everywhere ／ looked for it everywhere ／ spent forever looking for it），
    考位一次没丢 ⇒ 起作用的是规则，不是背下来的那一句。
  ⇒ 连对1 → **连对2 ⇒ 毕业**（状态行手写）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（她原话："1-4 直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 备注 primed 8/8 但 20 分钟后 cold 即掉 ⇒ 产出时掉，修法只有块化
- ⚠️ **必须和 #134 一起读**（08-19 判重发现两条会互相带偏）：本条说"英文动词必须带宾语"，
  #134 说"decide/choose/help/manage/win 这些能单独站住"。**先查这个动词在不在 #134 的白名单里**，
  不在名单里才补宾语 —— 否则修一处带偏隔壁（#134 的备注里已经记过这个教训）

### 19 · 分数说法（a half / a third / a quarter / two thirds）
类型 词组 ｜ 旧号 B42
状态 连对2 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 词组

**问题是什么**
**分数说法**：a half ／ a third ／ a quarter ／ two thirds；"十分之一" ＝ **a tenth ／ one tenth**。
同一格里的邻居（别串）：half 后面加不加 of 都对（half the price ／ half of the price）；
一个 of 可以管住两个数量 —— `only half, even a tenth, of the original price`。
判据一句话：分母用序数词（third／quarter／tenth），分子大于 1 就给分母加 -s（two thirds）。

**怎么发现的**
旧 B 表迁移（B42，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `only half, even a tenth, of the original price`（一个 of 管住两个数量）⇒ 毕业。
2026-09-09 复检第 4 组 ✅ `half of the original price` ／ `one tenth`。

**我错在哪**
她的：本条历史里没有掉过（三次判定都是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：说分数先定分母 —— 用序数词；再看分子，大于 1 就给分母加 -s。

**题面**
"原价的一半" ／ "十分之一"

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `only half, even a tenth, of the original price`（一个 of 管住两个数量）
- 2026-09-09 ✅ 复检 · 第 4 组 · `half of the original price` ／ `one tenth`
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；分数说法是她稳定会的基础知识，不是一个能学的表达
- 备注 她问"half 可以加 of" → 可以：half the price／half of the price 都对

### 20 · 泛指的不对称（the countryside 带 the／city life 不带）
类型 语法 ｜ 旧号 B43
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**泛指的不对称**：the countryside 带 the ／ city life 不带 —— 同样是泛指，冠词两边不一样。
`Living half in **the** city and **the** country would be perfect.`
判据一句话：city／country／countryside 这一族当地点泛指时带 the；life 这类抽象名词泛指时不带。
同一格里的邻居（别串）：⚠️ half A and half B 两边都要 half（09-05 顺带记，⛔ 不落号）。

**怎么发现的**
旧 B 表迁移（B43，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ❌。
2026-08-12 ✅ ／ 2026-08-16 ✅ ⇒ 2026-08-20 按新规则（连对 2 即毕业）毕业。
2026-09-05 复检第 1 组 ✅ `Living half in the city and the country would be perfect.` —— 冠词两边都对。

**我错在哪**
她的：2026-08-11 记过一次 ❌，触发原话未存（旧 B 表迁移）。
找法：说到"城／乡／农村"先停一句 —— 这一族泛指时是带 the 的，⛔ 别按"泛指不带 the"一刀切。

**题面**
"城乡各住一半最理想。"

- 2026-08-11 ❌
- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `Living half in the city and the country would be perfect.` —— in the city ／ the country 冠词两边都对
  ｜ ⚠️ 顺带：half A and half B 两边都要 half（不落号，§3.2b 第三档，见 session【本组顺带产出】①）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 7 组（她原话："5-9 直接过"）

### 21 · often ＝ 经常（频次高）
类型 词汇 ｜ 旧号 B44
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

**问题是什么**
**often ＝ 经常**（频次高）。位置：主语后、实义动词前 —— `my friend **often** goes to that shop.`
同一格里的邻居（别串）：usually ＝ 通常情况下（＝ #22，两条**题面互斥**）；
frequently／a lot 也是"频次高"、也合法（都算对）；**真缺口是反方向**：她早期把"经常"说成 usually（#22 备注记了三次）
⇒ 题面用"最近老是…"这种明摆着讲次数的场景，usually 放进去就不对。
判据一句话：说的是**次数多** ⇒ often；说的是**一般情况下** ⇒ usually。

**怎么发现的**
旧 B 表迁移（B44，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `my friend often goes to that shop.`（often 位置对 ＋ goes 的 -s 没掉）⇒ 毕业。
2026-09-10 复检第 3 组（打包）✅ —— 新题面（补了「**o** 开头」）下首测即命中。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：中文"经常"先分一刀 —— 讲的是次数（often）还是常态（usually）？

**题面**
"他最近经常迟到，老板已经说过他两回了。"

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `my friend often goes to that shop.`（often 位置对 ＋ goes 的 -s 没掉）
- 2026-09-10 📝 题面补首字母提示「**o** 开头」· 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面只排除了 usually，但 `frequently`／`a lot` 同样是"频次高"的副词、同样不在排除项里
  ⇒ 题面不唯一可判。补 `**o** 开头` 把 often 框死。
- 2026-09-10 ✅ 复检 · 第 3 组（打包）· `often` —— 新题面（补了「**o** 开头」）下首测即命中
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 去首字母）· 题型 词组 → 整句
  often／frequently／a lot 都算对；题面改成"最近老是迟到"这种讲次数的场景，逼的是 usually 这条错路（#22 备注里她误用过三次）

### 22 · usually ＝ 通常情况下
类型 词汇 ｜ 旧号 B188
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-21** ｜ 退池 ｜ 题型 词组

**问题是什么**
**usually ＝ 通常情况下**。位置：主语后、实义动词前 —— `I **usually** get up at 7.`
同一格里的邻居（别串）：often ＝ 次数多（＝ #21，两条**题面互斥**）；
always ＋ 习惯动词是常见夸张，⛔ 不算错 ⇒ 题面把 often／always 都排除掉。
判据一句话：说的是**一般情况下** ⇒ usually；说的是**次数多** ⇒ often。

**怎么发现的**
旧 B 表迁移（B188，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
尾部备注记着她早期**误用 usually 三次**（发生在事件流之前，原话未存）。
2026-08-21 ✅ 复习（点名题面首测）· `i usually get up at 7.`——位置也对 ⇒ 连对 2，毕业。
2026-09-11 复检 · 付息日 a2 第 3 组 ✅ `usually`。

**我错在哪**
她的：早期误用 usually 三次（只在备注里留了计数，触发原话未存）。
找法：中文"通常"先分一刀 —— 是"一般情况下"（usually）还是"次数多"（often）？

**题面**
**点名**："通常"（副词 · u 开头 · ⛔ 不许用 often／always）
★ 与 #21 题面互斥（原写在元信息行；元信息行留"题面"二字会被 check 当成第二处题面 ⇒ 移到本节）

- 2026-08-17 ✅
- 2026-08-21 ✅ 复习（点名题面首测）· `i usually get up at 7.`——usually 位置也对（主语后、实义动词前）→ **连对2，毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `usually`
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ① 同级说法
  "通常"→ usually／normally／generally 都成立，中译英里产不出 ❌；她误用 usually 的那一侧（把"经常"说成 usually）由 #21 的新题面去测
- 备注 她误用 usually 三次；always ＋ 习惯动词是常见夸张，不算错

### 23 · 固定词序整块背（back and forth · now and then · sooner or later · more or less）
类型 词组 ｜ 旧号 B45
状态 连对2 连错0 上次2026-09-27 ｜ **回潮 2026-09-05**（08-19 毕业 → 09-05 复检答"忘了"、在 forward／forth 之间不确定，撤销毕业、连对清零） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）｜ 题型 词组
**问题是什么**
**固定词序整块背**：back and forth · now and then · sooner or later · more or less ·
give or take · sick and tired · safe and sound —— 词序焊死（back and forth ✅ ／ forth and back ❌）。
同一格里的邻居（别串）：forth 今天几乎只活在 back and forth ／ and so forth 里 ⇒ **只按块记、⛔ 不当单词记**；
`to and fro` 同样是焊死词序的块、同样合法（答它算对）。
判据一句话：这类块是整串背下来的 —— 拆开去想哪个词在前，一定错。

**怎么发现的**
旧 B 表迁移（B45，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ❌。
2026-08-19 ✅ `we went back and forth three times.`（词序没倒）⇒ 毕业。
2026-09-05 复检第 1 组（打包）❌ `go back and forward(还是 forth) 忘了.` —— 在 forward／forth 之间不确定 ⇒ **回潮**。
2026-09-07 ✅ `go back and forth`；2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。

**我错在哪**
她的：`go back and forward(还是 forth) 忘了.`（2026-09-05 复检）　　正确：`We went **back and forth** three times.`
找法：这一串整块调，⛔ 别现场推哪个词在前 —— 推得出来就说明块还没背熟。

**题面**
"为了一份合同在两个城市之间来来回回跑"（反复往返，两头来回）

- 2026-08-11 ❌
- 2026-08-12 ✅
- 2026-08-16 ✅

- 2026-08-19 ✅ `we went back and forth three times.`（词序没倒）
- 2026-09-05 ❌ 复检组 · 第 1 组（打包）· **回潮**
  `go back and forward(还是 forth) 忘了.` → We went **back and forth** three times.
  ❌ 块没稳：她在 forward／forth 之间不确定 ＝ 没调出来（§3.3「不会」也是 ❌）。
  ★ 判据：这是词序焊死的整块，back and forth ✅ ／ forth and back ❌；
    forth 今天几乎只活在 back and forth ／ and so forth 里 ⇒ **只按块记、不当单词记**。
  ★ 同族一起记：back and forth · now and then · sooner or later · more or less ·
    give or take · sick and tired · safe and sound
- 2026-09-07 📝 题面加提示「**b 开头**」：原题面的「三个词 · 中间用 and 连 · 词序不许倒」被 to and fro
  逐条满足 ⇒ 第二译法没被排除（§6.5 第 7 项硬阻断）。补首字母只锁词，不泄露 forth／forward
  这个真考点。
- 2026-09-07 ✅ 复习 · 在池第 1 组 · `go back and forth`（词序没倒，09-05 回潮时正是 forward／forth 之间不确定）
- 2026-09-09 ⚡ 自评免测 · 在池第 1 组（她原话："这 10 个题直接过吧，算对"）
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉词数／首字母／排除项；to and fro 同样算对

### 24 · 搭配三件（work FROM home · handle orders · sales 恒复数不带 the）
类型 搭配 ｜ 旧号 B47
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 词组

**问题是什么**
三件搭配焊在一条里（旧 B 表迁来的捆绑条，未拆）：
· **work FROM home**（在家工作，介词是 **from**，⛔ 不是 at）
· **handle orders**（处理订单）
· **sales** 恒复数、⛔ 不带 the（sales go up by 20%）
判据一句话：这三处各占一格 —— 介词一格、数一格、冠词一格，逐格核。

**怎么发现的**
旧 B 表迁移（B47，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `working from home is more efficient. sales go up by 20%.`（三件全中）⇒ 毕业。
2026-09-01 📝 新题 P3（bank:490）自发命中留痕 · `some allow staff to work flexibly or **work from home**.`
2026-09-10 复检第 3 组（打包）✅ `work from home` ／ `sales rise by 20%` —— 三件里测到两件。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：说"在家工作"先确认介词是 **from**；说"销量"记住它恒复数、前面不加 the。

**题面**
"在家工作" ／ "销量涨了 20%"

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `working from home is more efficient. sales go up by 20%.`（三件全中）
  ⚠️ 同句 `go up` 该是 went up（中文"涨了"）——泛述读法也成立，只提醒不记档位
- 2026-09-01 📝 新题 P3（bank:490）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）
  `some allow staff to work flexibly or **work from home**.` —— 介词 from 一字不差（本条三件之一）。
- 2026-09-10 ✅ 复检 · 第 3 组（打包）· `work from home` ／ `sales rise by 20%`
  ★ 三件里测到两件：work **FROM** home ✅ · sales 复数且不带 the ✅
  ⚪ 同句时态：中文"涨了"是已完成，英文给的是现在时 rise ⇒ rose by 20%（记在 #12，形态类不判档位）
- 2026-09-12 📝 题面整改：第二句去句号「销量涨了 20%」—— 与第一块统一成词组题（§6.0 一条一种形式）· 全档题面 review
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移的捆绑条（work from home／handle orders／sales），原话未存、历史零 ❌；work from home 她自发用过多次，三块都是稳定会的

### 25 · It's no use doing sth（做某事没用）
类型 搭配 ｜ 旧号 B48
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 整句

**问题是什么**
**It's no use doing sth** ＝ 做某事没用（固定框，后面挂 **-ing**）：`it's no use fining people for littering`。
同一格里的邻居（别串）：#32 记的是"There's no point 比 It's no use 更常用"——两条**不矛盾**（都成立，只是常用度不同）
⇒ **她用 It's no use ⛔ 不许判错**；只有她问"哪个更常听"时才提 There's no point。题面正向点名 It's no use。
判据一句话：It's no use 后面挂的必须是 **-ing**。
★ 本条原是捆绑条（litter 不可数 ／ fine sb FOR doing ／ It's no use doing）——
　2026-08-23 c 段拆出 **#272（litter 不可数）· #273（fine sb FOR doing）**，本条只留第三块。

**怎么发现的**
旧 B 表迁移（B48，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ❌ 首次进流（三块都没出来）。
2026-08-19 ✅ `it is no use fining people for littering`（三个点一次全中）；
2026-08-20 ✅ **自发命中**（#257 那题，本条没被出题）· `it's no use just talking` ⇒ 连对 2，毕业。
2026-09-05 复检 ✅ `it's no use fining people for littering`；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：2026-08-17 首次进流 ❌（三块都没出来），触发原话未存。
找法：中文说"…没什么用"⇒ 先落 It's no use，再把那个动词改成 -ing 挂上去。

**题面**
"跟他讲道理没用，他根本听不进去。"（"没用"用 **It's no use** 说）

- 2026-08-17 ❌ 首次进流
- 2026-08-19 ✅ `it is no use fining people for littering`（三个点一次全中）
- 2026-08-20 ✅ **自发命中**（#257 那题，本条没被出题）· `it's no use just talking`
- 2026-08-23 📝 c 段 **拆号**：本条原来装了**三条不同规则** —— litter 不可数 ／ fine sb FOR doing ／
  It's no use doing。三块里只有第三块被反复验过（08-19 ＋ 08-20），前两块各只验过一次
  ⇒ 拆出 **#272（litter 不可数）· #273（fine sb FOR doing）**，各按日志重放 ＝ 连对1、进池；
  本条只留 It's no use doing，🎓 不动
- 2026-08-23 📝 c 段 **与 #32 的关系写进两条备注**（08-20 待办 #6，今天办掉）：
  #32 记的是"There's no point 比 It's no use 更常用"—— 两条**不矛盾**（都成立，只是常用度不同）
  ⇒ **她用 It's no use 不许判错**；只有在她问"哪个更常听"时才提 There's no point
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· it's no use fining people for littering
  （It's no use doing sth 整块）
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉负向排除，正向点名 It's no use，-ing 留给她；换成讲道理场景
- 2026-10-01 ✅ 复检 · 学习日 复检第 4 组 [4] · `It's no use reasoning with him; he won't listen to a word of it.` —— It's no use ＋ -ing
  ｜reasoning with him 她标「这个词组需要背一下」⇒ 新建 #383
- ⚠️ **捆绑条目**：本次只验了 It's no use doing 一块；litter 不可数／fine sb FOR doing 两块未再验
  ⇒ 付息日按"一条＝一个考点"拆号时，那两块各自从 0 起算重建
- ⚠️ 与 #32 的关系（付息日 c 段要写进两条备注）：#32 记的是"There's no point 比 It's no use 更常用"，
  两条**不矛盾**（都成立，只是常用度不同），别把她用 It's no use 判成错

### 27 · the credit gets shared（团队里功劳被分摊）
类型 词组 ｜ 旧号 B50
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 退池 ｜ 题型 词组

**问题是什么**
**the credit gets shared** ＝ 团队里功劳被分摊（口语默认走 **get-passive**，不必补 by everyone）。
同一格里的邻居（别串）：`the credit is ours` ／ `is shared by everyone` ／ `Credit is shared.` **都合法**，
⛔ 不许判错 —— 只是不是本条的目标形式 ⇒ 题面靠排除项（⛔ everyone／we／people 开头 · ⛔ is／are）把 gets 逼出来。
判据一句话：主语落 the credit，动词走 **gets** ＋ 过去分词。

**怎么发现的**
旧 B 表迁移（B50，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ◎ **教练现编题面**（"我们组是一起做的，功劳算大家的。"），她答 `the credit is ours` 完全合法但不是本条的块 ⇒ 记 ◎。
2026-08-20 ✅ 复习（改题面后首测）· `you don't stand out in a team because the credit is shared by everyone.` ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `Credit is shared.`（符合题面 ⇒ 记 ✅；同日 📝 补排除项 ⛔ is／are，下次才逼得出 gets shared）。

**我错在哪**
她的：`the credit is ours`（08-19，判 ◎）／ `Credit is shared.`（09-11，判 ✅）—— 两次都**合法**，只是不是目标形式。
找法：说"功劳大家分"时主语先落 the credit，动词走 **gets** shared（get 被动更口语、更"落到某人头上"）。

**题面**
**点名**："功劳是大家分的"（用 credit 那个词说 · ⛔ 不许用 everyone／we／people 开头 · ⛔ 不许用 is／are）
　　★ 题面 2026-08-20 改：原题面只说"显不出你自己"，逼不出 the credit gets shared
　　★ （"You don't stand out in a team" 完全合法）⇒ 补上后半句并点名 credit

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ◎ **教练现编题面**（"我们组是一起做的，功劳算大家的。"），
  她答 `the credit is ours` 完全合法但不是本条的块 ⇒ 记 ◎；下次必须用文件里这句题面
- 2026-08-20 ✅ 复习（改题面后首测）· `you don't stand out in a team because the credit is shared by everyone.`
  ——credit 出来了，被动也对 ｜`is shared by everyone` 不是本条原写法 `gets shared`，但符合题面 ⇒ ✅
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `Credit is shared.` —— 用 credit 当主语走被动、未用 everyone／we／people 开头 ⇒ 符合题面，记 ✅（§3.3 硬顺序②）
  ⚠️ 目标形式是 the credit **gets** shared；`is shared` 同样合法 ⇒ ⛔ 不算错
  ⇒ 同日 📝 改题面补 ⛔ is／are（§3.3 硬顺序③），下次才逼得出 gets shared
- 2026-09-11 📝 题面整改：补 ⛔ 不许用 is／are · **判定时**暴露（§3.3 硬顺序③）
  她答 `Credit is shared.` —— 用 credit 当主语走被动、未犯任何排除项 ⇒ 记 ✅，
  但本条目标形式是 the credit **gets** shared（get 被动更口语、更"被动落到某人头上"）⇒ 补排除项，下次逼出 gets。
  ★ `is shared` 与 `gets shared` **都合法**，这不是纠她的错，是把目标形式钉死
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ① 同级说法
  `the credit is shared`／`Credit is shared.` 都完全成立（条目自己也写着"都合法、⛔ 不许判错"），gets 与 is 只是被动式的风格选择 ⇒ 中译英里产不出 ❌
- 备注 口语默认走 get-passive：`the credit just gets shared`（不必补 by everyone）

### 28 · You just get more done at home.（用画面替掉 more efficient）
类型 词组 ｜ 旧号 B52①
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-24** ｜ 题型 整句

**问题是什么**
**get more done** ＝ 干得更多（用画面替掉 more efficient）：`I get more done when I work from home.`
同一格里的邻居（别串）：do more／finish more（合法，但不是这个块 ⇒ 题面正向点名 get … done）；
比较式走法 `you just won't get as much done as your coworkers`（08-25 那次她在自由产出里没调出来的正是它）。
判据一句话：结构是 **get ＋ more ＋ 过去分词**（done），⛔ 不是 do ＋ 名词。

**怎么发现的**
旧 B 表迁移（B52①，2026-08-18；B52 六句补录按 Q4 拆成 #28–#33），原始触发原话未存；
最早记录 2026-08-19 ◎ 首次进池 · 她答 `you can do more things working from home` 完全合法
⇒ 教练没做第二译法自查、没点名 ⇒ 题面当场加点名。
2026-08-23 ✅ `working from home actually makes me get more done.`；2026-08-24 ✅ `I get more done when I work from home.` ⇒ 毕业。
2026-09-11 复检 ✅ `get more down`（down 是 done 打歪，§2.1 拼写不算错）。

**我错在哪**
她的：`you can do more things working from home`（08-19，判 ◎ ＝ 教练没点名，⛔ 不记错）／
2026-08-25 自由产出写 `your output at work will be less than your coworkers'`（语法全对，只是这个块没调出来）
正确：`I get more done when I work from home.` ／ `you just won't get as much done as your coworkers`
找法：想说"效率高／干得多"时先去够 **get … done** 这个块，⛔ 别停在 do more things／more efficient。

**题面**
"在家办公没人打扰，我反而干得更多。"（"干得更多"用 **get … done** 说）

- 2026-08-19 ◎ 首次进池 · 她答 `you can do more things working from home` 完全合法
  ⇒ 教练没做第二译法自查、没点名 ⇒ 题面当场加点名
- 2026-08-23 ✅ 付息日 a 段（08-19 记 ◎ 改题面后首测）· `working from home actually makes me get more done.`
  ——目标块 `get more done` 一字不差；make ＋ 原形也对 ⇒ 一次到位
  ⚠️ `makes me get` → `helps me get`：make 带一点"逼着我"的味道，说效率高用 help 更贴
    （更口语：`I actually get more done working from home.`）—— 不是错，不建条目
- 2026-08-24 ✅ 复习第1组 · `I get more done when I work from home.`——目标块一字不差
  ⇒ **连对 1 → 2 ⇒ 🎓 毕业**
  ⚠️ 中文"反而"那一层没出来：`I **actually** get more done when I work from home.`
    （actually 放实义动词前，复用 🎓#220）—— 不是错，不落号
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `get more down` —— get ＋ more ＋ 过去分词这个块调对了；down 是 done 打歪（§2.1 拼写不算错）
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉负向排除，点名 get … done，more 放哪留给她（08-25 自由产出里没调出来的正是这个块）
- （B52 六句补录，迁移时按 Q4 拆成 #28–#33 六条）
- 备注 2026-08-25 · **反向留痕（不改状态、不回潮）**：自由产出（新题 bank:987 P3）里她写的是
  `your output at work will be less than your coworkers'` —— 语法全对、比较也对齐，
  但口语走法就是本条这个块：**you just won't get as much done as your coworkers**。
  ⇒ 昨天在中译英里调出来了、今天在自由产出里没调出来。
  **不判回潮**（本条的考点是"会不会用这个块"，她会；掉的是 retrieval，不是知识），
  但这是"知识在、检索没跑"最干净的一个实例，记在这里备查

### 29 · You don't have to sit in meetings all day.
类型 词组 ｜ 旧号 B52②
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-24 · 她指定** ｜ 退池 ｜ 题型 词组

**问题是什么**
**sit in meetings (all day)** ＝ 泡在会里：`You don't have to sit in meetings all day.`
同一格里的邻居（别串）：`get stuck in meetings all day` 完全合法（还更生动）⇒ 题面已排除 stuck／trapped；
`don't need to` 与 `don't have to` 两个都成立、意思一样 ⇒ ⛔ 不判错、不标 ⚠️。
判据一句话："泡在会里"那个动词就是 **sit**。

**怎么发现的**
旧 B 表迁移（B52②，2026-08-18），原始触发原话未存；
最早记录 2026-08-19 ◎ 首次进池 · 她答 `get stuck in meetings all day` ⇒ 教练第②类自查漏了，题面当场加点名。
2026-08-23 ✅ `you don't need to sit in meetings all day.`；2026-08-24 ✅ 与前一天逐字一致 ⇒ 连对 2，
**她当场指定毕业**（原话："毕业，不要再问了"）。
2026-09-11 复检 ✅ `sit in meetings`——"泡"用 sit，⛔ 没用 stuck／trapped。

**我错在哪**
她的：`get stuck in meetings all day`（08-19，判 ◎ ＝ 教练没点名，⛔ 不记错）　　正确：`sit in meetings all day`
找法：说"泡在会里"先把动词定成 **sit**，⛔ 别滑到 stuck／trapped。

**题面**
**点名**："泡在会里"（"泡"用 **sit** 那个动词说，⛔ 不许用 stuck／trapped）

- 2026-08-19 ◎ 首次进池 · 她答 `get stuck in meetings all day` 完全合法（还更生动）
  ⇒ 教练第②类自查又漏，题面当场加点名
- 2026-08-23 ✅ 付息日 a 段（08-19 记 ◎ 改题面后首测）· `you don't need to sit in meetings all day.`
  ——目标块 `sit in meetings` ＋ `all day` 一字不差
  ★ `don't need to` vs 条目名里的 `don't have to`：两个都成立、意思一样，且符合题面
    ⇒ 按 §3.3（她 08-20 定）记 ✅，不记 ◎
- 2026-08-24 ✅ 复习第1组 · `you don't need to sit in meetings all day.`——与 08-23 逐字一致
  ⇒ **连对 1 → 2 ⇒ 🎓 毕业**；**她当场指定**（原话："毕业，不要再问了"）⇒ 记「🎓·她指定」
  ★ 教练自审：想把 `don't need to` 标 ⚠️ 换 `don't have to` —— 两个在此语境都完全自然
    ⇒ 档位不成立，写「无更好版本」，不标
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `sit in meetings` —— "泡"用 sit，⛔ 没用 stuck／trapped
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ① 同级说法
  她答的 `get stuck in meetings all day` 完全合法、还更生动（条目自己写着），sit 只是另一个说法 ⇒ 中译英里产不出 ❌
- 备注 **#28–#33 这六条全部是"用块替掉平铺说法"型 ⇒ 天生第②类，出题一律点名**

### 30 · Say you fix something …（Say you… ＝ 举例起手，替 For example）
类型 词组 ｜ 旧号 B52③
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 整句

**问题是什么**
**Say you …** ＝ 举例起手（一个词替掉 For example），后面直接接完整从句：
`Say you fix a problem that the entire team got stuck on`。
同一格里的邻居（别串）：for example／for instance／suppose／imagine／let's —— 都合法，但都绕开这个词 ⇒ 题面正向点名 Say。
判据一句话："比方说"只用**一个词** Say 起头，后面跟一整句。

**怎么发现的**
旧 B 表迁移（B52③，2026-08-18），原始触发原话未存；最早记录 2026-08-19 ✅ 首次进池 · 点名 ·
`Say you solve a problem the whole team was stuck on`
（⭐ 同句还自发用对三个已毕业点：关系代词省略 ＋ 介词留末尾 ＋ stuck ON）。
2026-08-20 ✅ 复习 · `Say you solve a problem that the whole team is stuck with.` ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `Say you fix a problem that the entire team got stuck on`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：要举例时先落一个 **Say**，再把整句接上去，⛔ 别起 For example。

**题面**
"比方说你周末加了一天班，公司就该给你补一天假。"（"比方说"用 **Say** 起头）

- 2026-08-19 ✅ 首次进池 · 点名 · `Say you solve a problem the whole team was stuck on`
  ⭐ 同句还自发用对三个已毕业点：关系代词省略 ＋ 介词留末尾 ＋ stuck ON
- 2026-08-20 ✅ 复习 · `Say you solve a problem that the whole team is stuck with.`——Say you 起手对
  ｜同句 `stuck with`（该 stuck on）归 🎓#248 回潮 —— **同一道题昨天写的是 stuck on，一天之内从对变错**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `Say you fix a problem that the entire team got stuck on` —— Say 起头 ＋ 后接完整从句
  ⚠️ 顺带（不计档位）：entire → whole（口语默认）· got stuck → is stuck（现在还卡着 ⇒ 现在时）
- 2026-09-12 📝 题面整改：点名「用 Say 起头」→「用一个词起头 · ⛔ 不许用 for example／for instance／suppose／imagine／let's」—— 原点名把考点 Say 本身交出去（§6② 红线一）· 全档题面 review
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉五个排除项，正向点名 Say；换成加班补假场景

### 31 · explain YOURSELF to anyone（解释自己的行为）
类型 搭配 ｜ 旧号 B52④
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ ⚠️ 状态行 08-21 按日志重算（08-20 的 ✅ 当天漏回写）｜ 题型 整句

**问题是什么**
**explain YOURSELF to anyone** ＝ 解释自己的行为 —— **反身代词是块的一部分**，丢了 yourself 这个块就没出来。
同一格里的邻居（别串）：`You don't need to explain.`（不带宾语的 explain）**本身合法** ——
2026-09-04 教练差点据此判回潮，按 §7 四问① 造母语句推翻了自己 ⇒ 判据记死：**形状像 ≠ 同一个错，回潮是重动作**。
判据一句话：解释的对象是"自己（的行为）"吗？是 ⇒ 必须带 yourself。

**怎么发现的**
旧 B 表迁移（B52④，2026-08-18）；最早记录 2026-08-19 ❌ 首次进池 · 触发原话
`you don't need to explain to anyone`——丢了 yourself。
2026-08-20 ✅ ／ 2026-08-21 ✅ `you don't need to explain youself to anyone.`（youself 属拼写，§2.1 不算）⇒ 连对 2，毕业。
2026-09-05 复检 ✅ explain yourself；2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：`you don't need to explain to anyone`（2026-08-19 首犯）　　正确：`you don't need to explain **yourself** to anyone`
找法：写 explain 之前先问一句 —— 解释的是"自己"吗？是就把 yourself 带上。

**题面**
"我辞职是我自己的事，不用跟谁解释。"（"解释"用 **explain** 说）

- 2026-08-19 ❌ 首次进池 · `you don't need to explain to anyone`——丢了 yourself
- 2026-08-20 ✅ 复习（点名题面首测）· `you don't need to explain youself to anyone`
  ——yourself 补回来了（youself 是打字，按 §2.1 不算）
- 2026-08-21 ✅ 复习 · `you don't need to explain youself to anyone.`——explain **yourself** to anyone
  → **连对2，毕业**（`youself` 按 §2.1 拼写不算）
- 2026-09-04 📝 **留痕：本次未判**（⛔ 不判回潮、状态行一个字不动）· 新题第 2 道收尾
  `It's about whether you **need to explain**.`
  ★ 教练**差点判本条回潮**：本条 08-19 首犯正是 `you don't need to explain to anyone`（丢了 yourself），
    形状看着一模一样。
  ★ **推翻的理由（§7 四问①：试造一个母语者会说的句子来推翻自己）**：
    本条的 ❌ 是在**点名题面**（"你不用跟任何人解释自己。"）下丢了 yourself；
    而她今天这句 `whether you need to explain` **本身合法** —— `You don't need to explain.`
    是英语里常说的（不带宾语的 explain 成立）⇒ **不是错** ⇒ ⛔ 不判回潮。
  ★ 处置：只在 diff-2 给更准的块（`have to explain yourself`），本条状态一个字不动。
  ★ 记一笔判据：**回潮是重动作，形状像 ≠ 同一个错。**
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· explain yourself（反身代词是块的一部分）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 7 组（打包串，她原话："除了 3）忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  考点是 yourself 挂不挂 ＝ 靠句子现形；点名 explain，yourself 留给她；换成辞职场景
- 备注 同族块：explain yourself／behave yourself／enjoy yourself／help yourself —— 反身代词是块的一部分

### 32 · There's no point regretting it now.（比 It's no use 更常用）
类型 结构 ｜ 旧号 B52⑤
状态 连对2 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-21 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零）

**问题是什么**
**There's no point ＋ -ing** ＝ 做这件事没意义（比 It's no use 更常用）。
同一格里的邻居（别串）：加 in 也对（There's no point **in** regretting it now.）·
⛔ 不是 There's no point **to do** · It's no use 也合法（＝ #25，题面正向点名 There's no point 区分两条）。
同族：There's no point arguing with him. ／ There's no point worrying about it now.
判据一句话：There's no point 后面挂的那个动词，必须是 **-ing** 形。
★ 2026-09-12 类型由 词组 改 结构：考点是 There's no point ＋ -ing 这个**句框**，不是一个词（§6① 类型标签必须跟考点一致）。

**怎么发现的**
旧 B 表迁移（B52⑤，2026-08-18），原始触发原话未存；最早记录 2026-08-19 ✅ 首次进池 · 点名 ·
`There's no point regretting now`（块用对，同句 regret 少了宾语 it ⇒ 记进 #18）。
2026-09-11 付息日 a2 第 3 组复检：她答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**，撤销 08-21 的毕业、连对清零。

**我错在哪**
她的：答"忘了"（2026-09-11 复检）　　正确：`There's no point regretting it now.`
找法：中文说到"…也没用／没意义"，先落 There's no point，再把那个动词改成 -ing 挂上去。

**题面**
"事情都已经这样了，现在生气也没用。"（"也没用"用 **There's no point** 说）

- 2026-08-19 ✅ 首次进池 · 点名 · `There's no point regretting now`（块用对）
  ⚠️ 同句 regret 少了宾语 it ⇒ 记进 #18 当天日志，不计本条档位
- 2026-08-21 ✅ 复习 · `there's no point regretting it.`——块用对，**且宾语 it 带上了** → **连对2，毕业**
  ★ 同句 **#18 ✅**（08-19 正是这句漏了 it）
- 2026-09-11 ❌ 复检 · 付息日 a2 第 3 组 · 答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**
  最小改 `There's no point regretting it now.`
  ❌ 这个框是 **There's no point ＋ -ing**；⛔ 不是 There's no point **to do**、⛔ 不是 It's no use（题面已排除）。
  ★ 加 in 也对：There's no point **in** regretting it now.
  同族 There's no point arguing with him.／There's no point worrying about it now.
- 2026-09-12 📝 类型改正 词组 → 结构：考点是 There's no point ＋ -ing 这个句框，不是一个词（§6① 类型标签必须跟考点一致）· 全档题面 review
- 2026-09-13 📝 题面整改：补（⛔ 不许用 use）· 发题前审核（§6.5 第 7 项）
  `There's no use regretting it now.` 同样 There's 起头、同样合法，绕开 There's no point ⇒ 补排除项
- 2026-09-13 ✅ 学习日 在池第 1 组 · `there is no point (in) regretting it now.`——框对、-ing 对、宾语 it 在（09-11 回潮后首测）
- 2026-09-15 ✅ 学习日 在池第 1 组 · `There is no point regretting it.` —— There's no point ＋ -ing 框对；"现在"省了 ＝ 信息略省，不记档位 → **连对2，毕业**
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉负向排除，正向点名 There's no point，-ing 留给她；换成生气场景
- 2026-09-30 ✅ 复检 · 付息日 a2 第 3 组 [4] · `there is no point in chasing after it now.`

### 33 · on a clear day（替 if it's clear）
类型 词组 ｜ 旧号 B52⑥
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-24** ｜ 退池 ｜ 题型 词组

**问题是什么**
**on a clear day** ＝ 天晴的时候（用【介词 ＋ 名词】替掉从句 if it's clear／when it's clear）。
同一格里的邻居（别串）：`when it's clear` 完全合法 —— 本条要的正是把这个从句换成介词块；题面另外排除 weather／sunny。
判据一句话：中文"…的时候"先试一个介词块，装得下就别开从句。

**怎么发现的**
旧 B 表迁移（B52⑥，2026-08-18），原始触发原话未存；
最早记录 2026-08-19 ◎ 首次进池 · 她答 `when it's clear` 完全合法 ⇒ 教练没点名，题面当场加点名。
2026-08-23 ✅ `you can see the mountains on a clear day.`；2026-08-24 ✅ `On a clear day, you can even see the mountains.` ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `on a clear day`——介词 ＋ 名词，⛔ 没用从句。

**我错在哪**
她的：`when it's clear`（08-19，判 ◎ ＝ 教练没点名，⛔ 不记错）　　正确：`on a clear day`
找法：中文"天晴的时候"别先想从句 —— 先试【介词 ＋ 名词】：on a clear day。

**题面**
**点名**："天晴的时候"（用【介词＋名词】说，不用从句 · ⛔ 不许用 weather／sunny）

- 2026-08-19 ◎ 首次进池 · 她答 `when it's clear` 完全合法（本条要的就是把从句换成 on a clear day）
  ⇒ 教练没点名 ⇒ 题面当场加点名
- 2026-08-23 ✅ 付息日 a 段（08-19 记 ◎ 改题面后首测）· `you can see the mountains on a clear day.`
  ——`on a clear day` 一字不差；the mountains 带 the 也对（特指那片山）⇒ 一次到位
- 2026-08-24 ✅ 复习第1组 · `On a clear day, you can even see the mountains.`
  ——介词块放句首也对；"还能"＝ can **even** see 也落到了 ⇒ **连对 1 → 2 ⇒ 🎓 毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 4 组 · `on a clear day` —— 介词 ＋ 名词，⛔ 没用从句、没碰本场新排除的 weather／sunny
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ① 同级说法
  她答的 `when it's clear` 完全合法，on a clear day 只是把从句换成介词块的风格选择 ⇒ 中译英里产不出 ❌

### 34 · in groups（小组）≠ in pairs（两人一组）
类型 词组 ｜ 旧号 B53
状态 连对2 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ 题型 词组 ｜ **回潮 2026-09-11**（08-20 毕业 → 09-11 复检写成 `get paired in groups`，把 paired 与 groups 焊在一起 ＝ 正中本条要分开的那两个词，撤销毕业、连对清零）

**问题是什么**
**in groups**（以小组为单位）≠ **in pairs**（两人一组）——
**pair ＝ 两个人配成一对**，**group ＝ 三个人以上的小组**，这一组区分就是本条考点。
同一格里的邻居（别串）：in groups ／ in pairs 都是【介词 ＋ 名词复数】的裸块；
要带动词说 ⇒ get put into groups ／ split into groups ／ form groups（都合法）。
判据一句话：几个人？两个 ⇒ in pairs；三个以上 ⇒ in groups。

**怎么发现的**
旧 B 表迁移（B53，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ◎（题面没逼出，form groups／get into groups 都合法 → 当天改点名）。
2026-08-19 ✅ `working in groups is better than working alone`；2026-08-20 ✅ 复习 `the teacher get the students to work in groups.` ⇒ 毕业。
2026-09-11 付息日 a2 第 3 组复检：她写 `get paired in groups` —— 把 paired 与 groups 焊在一起 ⇒ **回潮**。

**我错在哪**
她的：`get paired in groups`（字面成了"被两两配对成小组"，自相矛盾）　　正确：`get put in groups`（只译这个块 ⇒ `in groups` 就够）
找法：说"分组"之前先数人数 —— 两个人才是 paired／in pairs，三个人以上一律 in groups。

**题面**
"两人一组"（两个人配成一对） ／ "按小组来"（三个人以上一组）

- 2026-08-17 ◎ 题面没逼出（form groups／get into groups 都合法）→ 08-17 改点名
- 2026-08-19 ✅ `working in groups is better than working alone`
  （教练现编了题面"分组做作业比一个人做强"、还丢了点名，但 in groups 确实被 cold 逼出来了 ⇒ ✅ 有效）
- 2026-08-20 ✅ 复习 · `the teacher get the students to work in groups.`——in groups 对，
  附带 get sb to do（🎓#143）也用对 ｜同句 `the teacher get`（该 gets）归 #10 主谓一致
- 2026-09-11 ❌ 复检 · 付息日 a2 第 3 组 · `get paired in groups` ⇒ **回潮**
  最小改 `get put in groups`
  ❌ **pair ＝ 两个人配成一对**（in pairs），**group ＝ 三个人以上的小组**（in groups）——
    把 paired 和 groups 焊在一起，字面成了"被两两配对成小组"，自相矛盾；
    而 in groups ≠ in pairs 这一组区分**正是本条考点** ⇒ 这一格没通过。
  ★ 只译"分小组"这个块，答 `in groups` 就够；要带动词 ⇒ get put into groups／split into groups
- 2026-09-12 📝 题面整改：「分小组」→「以小组为单位」—— "分小组"念回去先想到的是动词 divide／split，映射不回 in groups 这个介词块（§6① 缩短的硬前提）· 全档题面 review
- 2026-09-13 📝 题面整改：补（⛔ 不许用 teams）· 发题前审核（§6.5 第 7 项）
  `in teams` 同样是【介词＋名词复数】、同样合法，测不到 group 与 pair 那一格 ⇒ 补排除项
- 2026-09-13 ✅ 学习日 在池第 1 组 · `get put in groups.`——in groups 一字不差（09-11 回潮后首测）
- 2026-09-15 ✅ 学习日 在池第 1 组 · `in groups` → **连对2，毕业**
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉【介词＋名词复数】形态描述与三个排除项；题面改成两个中文块（两人一组 ／ 按小组），逼的就是她焊在一起的 pair／group 那一刀
- 2026-09-30 ✅ 复检 · 付息日 a2 第 3 组 [2] · `Pair up for a workout. split into small groups to discuss.`

### 35 · 禁双重否定：否定 → no- 词，动词一律肯定（Nobody knows.）
类型 语法 ｜ 旧号 B54＋B207c
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-20**（她 08-20 定：连对 2 即毕业，不论历史有无 ❌）｜ 题型 整句

**问题是什么**
**禁双重否定**：否定落在 **no- 词**上，动词一律肯定 ——
`Nobody knows.` ／ `no one else **can** do it` ／ `no one **is** willing to work overtime`。
同一格里的邻居（别串）：⛔ `neither of us didn't follow`（否定标了两次）。
判据一句话：一句里否定只标一次 —— 用了 nobody／no one／nothing／neither，动词就不许再带 not。
★ 本条 ＝ 原 #124（否定 → no- 词，且动词不再否定）2026-08-19 并入 —— 同一条规则。

**怎么发现的**
旧 B 表迁移（B54＋B207c，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅（原 #124）。
2026-08-16 ❌ 自由产出 `neither of us didn't follow`（原 #124）。
2026-08-19 ✅ `nobody else can do it` ＋ `no one is willing to work overtime`（否定都只标一次）⇒ 2026-08-20 毕业。
2026-09-05 复检 ✅ 两句都走 no- 词 ＋ 动词肯定；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：`neither of us didn't follow`（2026-08-16 自由产出）　　正确：`neither of us **followed**`
找法：写完 nobody／no one／nothing／neither，回头看动词上还有没有第二个 not。

**题面**
"别人都做不到。" ／ "没人愿意加班。"

- 2026-08-12 ✅（原 #124）
- 2026-08-16 ❌ 自由产出 `neither of us didn't follow`（原 #124）
- 2026-08-17 ✅ 首次进流 ｜同日原 #124 也 ✅
- 2026-08-19 ✅ `nobody else can do it` ＋ `no one is willing to work overtime`（否定都只标一次）
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· 两句都走 no- 词 ＋ 动词肯定
  （no one else **can** do it ／ no one **is** willing）⛔ 无双重否定
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-10-01 ✅ 复检 · 学习日 复检第 4 组 [5] · `Nobody tell me a thing about it. There's nothing left in the fridge.` —— 否定都只标一次（Nobody 配 a thing · There's nothing left）
  ｜⚪ tell → told 归 #12（形态类·时态），不影响本条
- 备注 合并 2026-08-19：#124（否定 → no- 词，且动词不再否定）并入本条 —— 同一条规则
  ⚠️ **本条 08-19 曾按"零 ❌ 线"判毕业，合并后撤销**：并入 #124 的日志后 08-16 有一个 ❌，
     零 ❌ 线不适用，连对只有 2 ⇒ 回到未毕业，还差一次

### 36 · all morning / all day / all night 不带 the
类型 搭配 ｜ 旧号 B55
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**all morning ／ all day ／ all night 不带 the**：`he played games **all night**`。
同一格里的邻居（别串）：the whole morning 也合法，但不是本条的块（09-07 复检写明"⛔ 没落进 the whole morning"）；
⚠️ 与 🎓#39（the TV／the radio 惯用带 the）方向相反，⛔ 别互相带跑。
判据一句话：all ＋ 时段名词，中间**不插 the**。

**怎么发现的**
旧 B 表迁移（B55，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅；2026-08-15 ❌ ／ 2026-08-16 ❌。
2026-08-19 ✅ `he played games all night` ⇒ 2026-08-20 按"连对 2 即毕业"毕业
（★ 教练一度按"零 ❌ 线"判它毕业 —— **判错了**，本条日志里就有两个 ❌，当天已撤销）。
2026-09-05 ✅ all morning；2026-09-07 复检（打包）✅ `all morning`。

**我错在哪**
她的：2026-08-15 与 08-16 各记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：写完 all ＋ 时段，回头看中间有没有混进一个 the。

**题面**
"他昨天打游戏打了一整晚，今天上课一直犯困。"（"一整晚"用 **all** 说）

- 2026-08-11 ✅
- 2026-08-15 ❌
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ✅ `he played games all night`（all night 不带 the）
  ★ 教练一度按"零 ❌ 线"判它毕业 —— **判错了**，本条 08-15/08-16 两个 ❌ 就在日志里，
    零 ❌ 线不适用；已撤销，仍需连对 3
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· all morning（⛔ 不带 the）
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `all morning`（⛔ 没落进 the whole morning）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  the whole night 合法 ⇒ 中文块单独逼不出 all ＋ 时段；改整句、点名 all，中间插不插 the 留给她（她掉过两次的就是这个）
- 2026-10-01 ✅ 复检 · 学习日 复检第 4 组 [6] · `He played games all night last night and kept nodding off in class today.` —— all night 不带 the
  ｜nodding off 她标「这个词组背一下」⇒ 新建 #384

### 37 · everyday（形容词）≠ every day（副词短语）
类型 语法 ｜ 旧号 B56
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 词组

**问题是什么**
**everyday（形容词，连写）≠ every day（副词短语，分写）**：
`**everyday** commute`（修饰名词）／ `commuting **every day** is really a hassle.`（修饰动词）。
同一格里的邻居（别串）：`daily commute` 是最常见说法、也是名词短语、完全合法，
但它绕开这个分工 ⇒ 2026-09-10 题面补了排除项「⛔ 不许用 daily」。
判据一句话：它挨着的是名词 ⇒ 连写 everyday；挨着的是动词（多久一次）⇒ 分写 every day。

**怎么发现的**
旧 B 表迁移（B56，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `commuting every day is really a hassle.` ⇒ 毕业。
2026-09-10 复检第 3 组 ✅ `everyday commute` —— 本场发题前刚补了排除项，考位才露出来。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：下笔前先看它挨着谁 —— 名词就连写 everyday，动词就分写 every day。

**题面**
"每天通勤"（写成名词短语 · ⛔ 不许用 daily）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `commuting every day is really a hassle.`
- 2026-09-10 📝 题面补排除项「⛔ 不许用 daily」· 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面「"每天通勤"（写成名词短语）」—— `daily commute` 是最常见的说法、也是名词短语，
  完全合法却绕开 everyday／every day 的分工（＝ 本条考点）⇒ 补排除项。
- 2026-09-10 ✅ 复检 · 第 3 组 · `everyday commute` —— 形容词 everyday 连写
  ★ 本场发题前刚补了排除项「⛔ 不许用 daily」，考位才露出来（daily commute 是最常见说法）
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ③ 口语里测不出
  everyday／every day 连写分写**读音完全一样**，只是书写差别（§2.1 拼写层）⇒ 口语线测不出；旧 B 表迁移、历史零 ❌

### 38 · feel the energy in the room
类型 词组 ｜ 旧号 B57b
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-20**（08-20 全库回扫漏网，08-21 按日志重放补记）｜ 题型 整句

**问题是什么**
**feel the energy in the room** ＝ 感觉到现场那种气氛 —— "气氛／那种劲儿"这个名词用 **energy**。
判据一句话：说"现场那种劲儿"时，名词落 **energy**、动词落 feel。
★ 与 #118 的分工（2026-08-19 题面整改写明）：两条原来的题面几乎是同一句，考点却不同 ——
　本条 ＝ feel the energy 这个块，#118 ＝ "只有…才"那一层；她每次答中一条、另一条就记不上，
　**这正是 #118 一直毕不了业的真原因** ⇒ 本条题面去掉"只有…才"、改成对比"现场 vs 视频"，两条从此互斥。

**怎么发现的**
旧 B 表迁移（B57b，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅（继承毕业，08-17 复查）。
2026-08-17 ◎ 题面没逼出（同日删掉 live 那一半，她两次指出与 there 语义重复）。
2026-08-19 ✅ 她在 #118 的句子里**自发**说出 `You can feel that energy when you are there`。
2026-08-21 ⛔ 教练犯规·本题作废：她当场提异议"这题我不想答了，我记得明明就让它毕业了"——**她是对的**；
状态行按日志重算、毕业日期回填 08-20。2026-09-10 ⚡ 自评免测。

**我错在哪**
她的：本条没有掉过（08-17 是 ◎ ＝ 题面没逼出；08-21 是教练排错题作废），触发原话未存。
找法：说"现场那种气氛／那种劲儿"时，名词直接落 **energy**，动词用 feel。

**题面**
"那场演唱会我是在网上看的，完全感觉不到现场那种气氛。"（"那种气氛"用 **energy** 说）

- 2026-08-11 ✅（继承毕业，08-17 复查）
- 2026-08-17 ◎ 题面没逼出；同日删掉 live 那一半（她两次指出与 there 语义重复）
- 2026-08-19 ✅ 她在 #118 的句子里自发说出 `You can feel that energy when you are there`
- 2026-08-19 📝 **题面整改（撞车）**：原题面"现场那种劲儿只有到场才有。"与 #118 的题面
  "只有到现场才有那种感觉。"几乎是同一句，而两条考点不同（本条 ＝ feel the energy 这个块，
  #118 ＝ "只有…才"那一层）⇒ 她每次答中一条、另一条就记不上，**这就是 #118 一直毕不了业的真原因**
  ⇒ 本条题面去掉"只有…才"，改成对比"现场 vs 视频"，两条从此互斥
- 2026-08-21 ⛔ **教练犯规·本题作废**：本条被排进 L3 第 1 组第 8 题，她当场提异议
  "这题我不想答了，我记得明明就让它毕业了"—— **她是对的**。日志重放 ＝ 08-11 ✅（连对1）→
  08-17 ◎（§3.3 跳过，不加不清 ⇒ 仍 1）→ 08-19 ✅（连对2），而状态行一直写着"连对1"
  （08-17 那次 ◎ 被当成清零），于是 08-20 执行「连对2 即毕业」全库回扫时**按状态行读成连对1、漏掉本条**。
  ⇒ 状态行按日志重算，毕业日期回填 08-20；本题不计档位、不算她的错。
  ⇒ 规则本来就有（§3.1「状态由日志重放而来，不一致时以日志为准」），是执行没做。
  ⇒ 同类扫查：全库"日志含 ◎ 且未毕业"共 6 条（#28 #29 #33 #38 #88 #129），除本条外五条状态行与日志一致 ⇒ 孤例。
- 2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："直接过"）
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 energy，动词 feel 与冠词留给她；换成网上看演唱会场景（⛔ 不带"只有…才"，与 🎓#118 互斥照旧）

### 39 · 惯用定冠词：the TV / the radio / the cinema / on the screen
类型 语法 ｜ 旧号 B58
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**惯用定冠词**：the TV ／ the radio ／ the cinema ／ on the screen —— 这一族名词习惯带 **the**。
`he sat in front of **the** TV all night.`
同一格里的邻居（别串）：同一句里的 all night **不带** the（＝ 🎓#36）—— 两条方向相反，⛔ 别互相带跑。
判据一句话：TV／radio／cinema／screen 这一族，前面默认补 the。

**怎么发现的**
旧 B 表迁移（B58，2026-08-18），原始触发原话未存；最早记录 2026-08-12 📖 给了答案才会。
2026-08-15 ◎ 题面没逼出（"看医生"两种说法都成立，已废该题面）；2026-08-16 ❌。
2026-08-19 ✅ `he sat in front of the TV all night.`（the TV ＋ all night 不带 the ＋ sat 变形，三处都对）⇒ 2026-08-20 毕业。
2026-09-05 复检 ✅ in front of **the** TV；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：2026-08-16 记过一次 ❌、08-12 是"给了答案才会"（📖），触发原话未存。
找法：说到 TV／radio／cinema／screen，先把 the 补上再往下说。

**题面**
"他整晚坐在电视机前。"

- 2026-08-12 📖 给了答案才会
- 2026-08-13 ✅
- 2026-08-15 ◎ 题面没逼出（"看医生"两种说法都成立，已废该题面）
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ✅ `he sat in front of the TV all night.`（the TV ＋ all night 不带 the ＋ sat 变形，三处都对）
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· in front of **the** TV（惯用定冠词）
  ｜ ⚠️ 顺带自发命中 #36：all night ⛔ 不带 the
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-10-01 ✅ 复检 · 学习日 复检第 4 组 [8] · `My grandma listens to the radio every single morning.` —— the radio

### 40 · 删掉自我对冲的 a bit（对比句要给足）
类型 结构 ｜ 旧号 B59
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 整句

**问题是什么**
**删掉自我对冲的 a bit**：做对比就要把程度给足 ——
`It's **much** lonelier watching it at home` ／ `It's **a lot** lonelier watching at home.`
同一格里的邻居（别串）：much／a lot 这类加强词才是对比句要的；⛔ a bit 把自己的对比对冲掉了。
判据一句话：这一句是在做对比吗？是 ⇒ 程度词只许往上加，不许往回缩。

**怎么发现的**
旧 B 表迁移（B59，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `It's much lonelier watching it at home`（没有 a bit，对比给足）⇒ 毕业。
2026-09-10 复检第 3 组 ✅ `It's a lot lonelier watching at home.` —— 程度给足。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存 —— 条目名里的 a bit 是要她**减掉**的那个词。
找法：写完对比句回头看程度词 —— 出现 a bit 就换成 much／a lot。

**题面**
"在家看就冷清多了。"

- 2026-08-12 ✅
- 2026-08-16 ✅

- 2026-08-19 ✅ `It's much lonelier watching it at home`（没有 a bit，对比给足）
  ⚠️ 同句 lonelier→duller／doesn't feel the same（"冷清"≠"孤单"），词义层，不影响本条考点
- 2026-09-10 ✅ 复检 · 第 3 组 · `It's a lot lonelier watching at home.` —— 程度给足（⛔ 没拿 a bit 自我对冲）
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ① 同级说法
  a bit lonelier 本身完全成立，删掉对冲词是表达风格建议 ⇒ 中译英里产不出 ❌；旧 B 表迁移、历史零 ❌

### 41 · time and energy（并列词序：短的在前长的在后）
类型 搭配 ｜ 旧号 B60
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

**问题是什么**
**time and energy**（固定并列词序：短的在前、长的在后）。
判据一句话：并列两个名词先比长短 —— `energy and time` **不是语法错**，是词序不地道。
同一格里的邻居（别串）：同句里的 `preparing classes` 才是真搭配错（该 prepare **for** class）——
那一半已于 2026-08-23 c 段拆出成 **#274**，本条只管并列词序。

**怎么发现的**
旧 B 表迁移（B60，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ❌ 首次进流。
2026-08-19 ✅ `spend more time and energy preparing for class`（词序＋介词两处都对）；
2026-08-20 ✅ **自由产出自发命中**（#26 那题，无点名无提示）· `requires more time and energy for communication` ⇒ 毕业。
2026-08-27 ✅ 自发命中 · 付息日 d 段重答 R5 · `cooking festival food needs more **time and energy**`
—— 本条毕业以来**第一次在没有中文题面的情况下自己排对**。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：2026-08-17 首次进流 ❌（触发原话未存，旧 B 表迁移）。
找法：并列两个名词时先比长短 —— 短的放前面（time and energy）。

**题面**
"时间精力"（两个名词并列）

- 2026-08-17 ❌ 首次进流
- 2026-08-19 ✅ `spend more time and energy preparing for class`（词序＋介词两处都对）
- 2026-08-20 ✅ **自由产出自发命中**（#26 那题，无点名无提示）· `requires more time and energy for communication`
- 2026-08-23 📝 c 段 **拆号**：`prepare for class`（介词搭配）与本条（并列词序）是**两条不同规则**；
  08-20 那次只验了本条这一半，prepare for class 跟着毕业了
  ⇒ 拆出 **#274（prepare FOR class）**，按日志重放 ＝ 连对1、进池；本条只留 time and energy，🎓 不动
- 2026-08-27 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 付息日 d 段重答（R5）·
  `cooking festival food needs more **time and energy**`——并列词序对（短的在前长的在后）
  ★ **本条从 08-20 毕业起第一次在自由产出里自发命中** —— 之前的 ✅ 全是中译英复习，
    这次是在没有中文题面的情况下自己排对的
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 4 组（打包串里，她原话："其他的直接过"）
- 备注 `energy and time` 不是语法错，是固定并列词序不地道；`preparing classes` 才是真搭配错
- ⚠️ **捆绑条目**：prepare for class 那半 08-20 未再验（只验了 time and energy）⇒
  付息日拆号时按"一条＝一个考点"重建 prepare for class 一条，从 0 起算

### 42 · which（确定范围里选）vs what（范围开放）
类型 语法 ｜ 旧号 B61
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 整句

**问题是什么**
**which（在确定范围里选）vs what（范围开放）**：`no one knows **which** part is yours.`
判据一句话：备选是不是已经框死的那几个？框死了 ⇒ which；没框死 ⇒ what。

**怎么发现的**
旧 B 表迁移（B61，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `no one knows which part is yours.`（范围确定用 which）⇒ 毕业。
2026-09-10 复检第 3 组 ✅ 同一句，which 用对。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"哪个"之前先问一句 —— 备选数得清吗？数得清就用 which。

**题面**
"没人知道哪部分是你做的。"

- 2026-08-12 ✅
- 2026-08-16 ✅

- 2026-08-19 ✅ `no one knows which part is yours.`（范围确定用 which）
- 2026-09-10 ✅ 复检 · 第 3 组 · `no one knows which part is yours.` —— which（确定范围里选）用对
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；which／what 在"哪部分"这种句子里她一直用对，口语里 what part 也有人说 ⇒ 测不出缺口

### 43 · come to your city / come to town（乐队巡演到某地）
类型 词组 ｜ 旧号 B62
状态 连对1 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个题毕业了，不要再考了"）｜ 题型 整句

**问题是什么**
**come to your city ／ come to town** ＝ 乐队巡演到某地。
判据：说"巡演到某地"的 come 必须带落点 —— come **to town** ／ to your city（同 #18 论元完整一族）。
判据一句话：这个意义上的 come **站不住脚** —— 后面必须挂一个"到哪儿"。

**怎么发现的**
旧 B 表迁移（B62，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ◎ 题面没逼出。
2026-08-19 ❌ `your favourate band comes once or twice a year`——come 缺落点。
2026-08-20 ✅ 复习（改题面后首测）· `your favourite band comes here once or twice a year`——落点有了；
她当场指定毕业（原话："这个题毕业了，不要再考了"）。
2026-09-05 复检 ✅ comes **here** once or twice（正是 08-19 掉、08-20 修回的那一格）；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：`your favourate band comes once or twice a year`（2026-08-19）
正确：`your favourite band comes **here** once or twice a year`
找法：写完 come 回头找那个"到哪儿"——没有就补上（come here／to town／to your city）。

**题面**
"你喜欢的乐队一年才来我们这儿一两次。"（"来我们这儿"用 **come** 说）
　　★ 题面 2026-08-20 改：中文补上"我们这儿"这个落点（08-19 她 `comes once or twice a year` 缺落点，
　　★ 是题面里根本没有落点可译）—— **用改题面而不是点名**，因为点名"come 要带地点"等于给答案

- 2026-08-17 ◎ 题面没逼出

- 2026-08-19 ❌ `your favourate band comes once or twice a year`——come 缺落点
- 2026-08-20 ✅ 复习（改题面后首测）· `your favourite band comes here once or twice a year`——落点有了
  ｜⚠️ 题面的"才"（only）没译出，属同族弱信息，**故意不建号**（她当场指定本条毕业）
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· comes **here** once or twice —— 落点在
  （这正是 08-19 掉、08-20 修回的那一格）
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-10-01 ✅ 复检 · 学习日 复检第 4 组 [7] · `My favorite band only comes through here once or twice a year.` —— come 后面挂了落点（through here；come through ＝ 巡演路过某地，合法）

### 44 · good AT doing ／ 升级版 He cooks well.
类型 搭配 ｜ 旧号 B66
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 整句

**问题是什么**
**good AT doing**（介词写死是 **at** ＋ -ing）／ 升级版直接换实义动词：**He cooks well.**
· `he's really good **at** cooking` · `he cooks really well.`
判据一句话：用 good 就必须配 at ＋ -ing；不想绕就直接把动词说出来加 well。

**怎么发现的**
旧 B 表迁移（B66，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `he cooks really well.`（直接上升级版，没绕 good at cooking）⇒ 毕业。
2026-09-10 复检第 3 组（打包）✅ `he's really good at cooking` —— good **AT** doing。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"很会…"时两条路挑一条 —— good **at** ＋ -ing，或者直接上动词 ＋ well。

**题面**
"他很会做饭。"

- 2026-08-12 ✅
- 2026-08-16 ✅

- 2026-08-19 ✅ `he cooks really well.`（直接上升级版，没绕 good at cooking）
- 2026-09-10 ✅ 复检 · 第 3 组（打包）· `he's really good at cooking` —— good **AT** doing
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；good at -ing 与 cooks well 她一直用对，是稳定会的基础搭配

### 45 · walk to work（by 后面只接交通工具）
类型 搭配 ｜ 旧号 B67
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**walk to work** ＝ 走路上班 —— **by 后面只接交通工具**（by bus／by car），⛔ 没有 by walk 这个说法。
判据一句话：by 那个位置只放交通工具；"走路"本身是动词，直接说 walk to work。

**怎么发现的**
旧 B 表迁移（B67，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `I walk to work every day.`（不是 by walk）⇒ 毕业。
2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存 —— 条目名里的 by walk 是要她避开的那条路。
找法：想说"走路上班"时别先摸 by —— by 只接交通工具，走路直接用动词 walk。

**题面**
"走路上班"

- 2026-08-12 ✅
- 2026-08-16 ✅

- 2026-08-19 ✅ `I walk to work every day.`（不是 by walk）
- 2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；by walk 这条错路她从没走过，walk to work 是稳定会的基础说法

### 46 · 主语复数，表语也要复数（hobbies are things you choose）
类型 语法 ｜ 旧号 B68
状态 连对2 连错0 上次2026-09-27 ｜ **回潮 2026-09-05**（08-20 毕业 → 09-05 复检用了 what 从句，题面点名的"表语用名词"没测到，撤销毕业、连对清零。★ 2026-09-07 补：这一判定 09-05 当天写进了 session 却漏了 `append`，回潮同步迟到两天） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）｜ 题型 整句

**问题是什么**
**主语复数，表语也要复数**：hobbies **are things** you choose —— 表语用**名词**说。
同一格里的邻居（别串）：`hobbies are what you choose` 完全合法，但它把表语换成了 what 从句、绕开考点
⇒ 题面正向点名表语那个名词的原形 thing，复数留给她自己变。
判据一句话：主语是复数 ⇒ 表语那个名词也得是复数（things，不是 thing）。

**怎么发现的**
旧 B 表迁移（B68，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ❌。
2026-08-16 ◎ 加"事"想逼出名词位、无效；2026-08-17 ◎ 她照样合法绕开（hobbies are what you choose）→ 改点名。
2026-08-19 ✅ 点名 · `hobbies are things you choose, but the job isn't`（复数表语 ＋ 名词位，一次到位）⇒ 08-20 毕业。
2026-09-05 ❌ 复检 · `hobbies are what you choose youself, but jobs are not.` —— 用了 what 从句、考位没测到 ⇒ **回潮**。
2026-09-07 ✅ `Hobbies are things you choose youself, but jobs aren't`；2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。

**我错在哪**
她的：`hobbies are what you choose youself, but jobs are not.`（2026-09-05 复检）
正确：`Hobbies are things you choose yourself, but jobs are not.`
找法：主语一复数，表语那个名词就跟着复数；⛔ 别拿 what 从句把名词位躲掉。

**题面**
"我这些爱好都是我自己选的事，上班可不是。"（"事"用 **thing** 说）

- 2026-08-11 ❌
- 2026-08-12 ✅
- 2026-08-16 ◎ 加"事"想逼出名词位，无效
- 2026-08-17 ◎ 她照样合法绕开（hobbies are what you choose）→ 改点名
- 2026-08-19 ✅ 点名 · `hobbies are things you choose, but the job isn't`（复数表语＋名词位，一次到位）
- 2026-09-05 ❌ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· 题面点名"表语用名词说，不用 what 从句"，
  她用了 what 从句 ⇒ 考位没测到
  原句 `hobbies are what you choose youself, but jobs are not.`
  最小改 `Hobbies are things you choose yourself, but jobs are not.`
- 2026-09-07 ✅ 复检 · 第 3 组 · `Hobbies are things you choose youself, but jobs aren't`
  —— 主语复数 ⇒ 表语也复数（things），⛔ 没再用 what 从句（09-05 掉的正是这一格）；youself 拼写不算错
- 2026-09-09 ⚡ 自评免测 · 在池第 1 组（她原话："这 10 个题直接过吧，算对"）
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"不用 what 从句"负向写法，改成点名表语名词的原形 thing，复数留给她；换成"我这些爱好"场景

### 47 · 反差句两边都要说完（连接词用 but/whereas，不用 and）
类型 结构 ｜ 旧号 B69
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 整句

**问题是什么**
**反差句两边都要说完**，连接词用 **but／whereas**，⛔ 不用 and：`I need that job, **but** flowers need me.`
判据一句话：这一句是在讲反差吗？是 ⇒ 连接词必须是 but／whereas，且两边各自说完整。

**怎么发现的**
旧 B 表迁移（B69，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `I need that job, but flowers need me.`（but ＋ 两边都说完）⇒ 毕业。
2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：写反差句先把连接词定成 but／whereas，再回头看两边是不是都说完了。

**题面**
"我需要这份工作，但花需要我。"（两边都要说完 · 连接词 ⛔ 不许用 and）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `I need that job, but flowers need me.`（but ＋ 两边都说完）
  ⚠️ 同句 that job→this job · flowers→the flowers（指称层，归 #63 备注）
- 2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；反差句用 but 是她稳定会的基础连接，不是一个能学的表达

### 48 · work 不可数 ＝ 活儿（说"这份工作"用 my job）
类型 语法 ｜ 旧号 B70
状态 连对2 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 退池 ｜ 题型 词组

**问题是什么**
**work 不可数 ＝ 活儿**；说"这份工作"要用可数的 **this job ／ my job**。
同一格里的邻居（别串）：题面已排除 work。
判据一句话：指**一份具体的工作** ⇒ job（可数）；指"活儿／干活这件事" ⇒ work（不可数）。

**怎么发现的**
旧 B 表迁移（B70，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅、2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-09-09 复检第 3 组 ✅ `this job`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"工作"先分一刀 —— 一份具体的工作用 job，"活儿"才用 work。

**题面**
"这份工作"（名词短语 · ⛔ 不许用 work）

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-09-09 ✅ 复检 · 第 3 组 · `this job`
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；"这份工作"说 this job 她一直对，work 当可数的错路她从没走过

### 49 · 人称一致：一句里、一段里都不能跳（统一 I 或统一 you）
类型 结构 ｜ 旧号 B71＋B78
状态 连对2 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-20 毕业 → 09-05 复检 ✅ → 09-11 复检答"忘了"，撤销毕业、连对清零）

**问题是什么**
**人称一致**：一句之内、一段之内人称都不许跳 —— 统一 **I** 或统一 **you**，开头定了就不换。
同一格里的邻居（别串）：you（泛指）与 my wife and me（具体）**指称对象不同**、且分属两个独立句子
⇒ **不算跳**（08-20 定的判据，09-05 复检照此执行）。
判据一句话：句子里第二次、第三次出现的那个人称，跟第一个是不是同一个？
★ 本条 ＝ 原 #55（人称一致·一段里）2026-08-19 并入：同一条规则，只差范围是一句还是一段。

**怎么发现的**
旧 B 表迁移（B71＋B78，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ❌ 首次进流
（同日原 #55 记 ✅ ⇒ 同日一对一错，保守记 ❌）；原 #55 另有一条备注：08-05 一天内跳了 3 次。
2026-09-11 付息日 a2 第 7 组复检：她答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**，撤销 08-20 的毕业、连对清零。

**我错在哪**
她的：答"忘了"（2026-09-11 复检）
正确：`I like cooking because I go step by step and end up with something to show for it.` ／
`At the cinema I can really get into the film, and my wife and I treat it as a date night.`
找法：开口前先定死一个人称，说完回头数一遍 —— 后面每一个人称是不是都跟第一个同一个。

**题面**
"喜欢跑步，因为跑完整个人都轻松了，一整天都有精神。" ／ "在家办公能自己安排时间，中午还能陪孩子吃饭。"（中文省了主语 —— 人称自己定，定了就一路用到底）

- 2026-08-17 ❌ 首次进流 ｜同日原 #55 记 ✅ ⇒ 同日一对一错，保守记 ❌
- 2026-08-19 ✅ `I like cooking because I follow the steps and get something to show for it`（全句人称统一在 I）
- 2026-08-20 ✅ 两句都答 · `I like cooking - I follow the steps and end up getting things to show for it.`
  ＋ `At the cinema, you can immerse youself in the movie. For my wife and me, going to the cinema feels like date night`
  ★ 第二段 you → my wife and me **不算跳**：you ＝ 泛指、my wife and me ＝ 具体，
    **指称对象不同**且分属两个独立句子 ⇒ 判据以后照此执行
  ｜⚠️ `things to show for it` 该 something（固定块量词），不建号，只进 diff
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· 人称一致：句 1 全段统一在 I；
  句 2 的 you → my wife and me 与 **08-20 判 ✅ 的那次同形**
- 2026-09-11 ❌ 复检 · 付息日 a2 第 7 组 · 答"忘了" ⇒ **回潮**
  最小改 `I like cooking because I go step by step and end up with something to show for it. ／ At the cinema I can really get into the film, and my wife and I treat it as a date night.`
  ❌ 一句之内、两句之间人称都不许跳：第一句 because 后面仍是 **I**；第二句中文泛指"你"统一成 I，后半 my wife and I 才顺
- 2026-09-12 📝 题面整改：两句中文改成**省主语**版 —— 旧题面第二句自带"你…我"的跳人称，照译反而被判 ❌ ＝ 题面在逼她猜；改成中文不给主语，人称由她定、只判跳不跳 · 全档题面 review
- 2026-09-13 ✅ 学习日 在池第 1 组 · ① `I like cooking because I follow the steps and get something to show for it.`
  ② `At a cinema, you can get completely immersed, plus it doubles as a data night with your partner.`
  ① 全句 I、② 全句 you —— 一句之内零跳；① I → ② 泛指 you 与 08-20 判据同形（泛指 vs 具体、两个独立句 ⇒ 不算跳）
  ⇒ §3.3「答得合法但不是题面预期 ⇒ ✅ ＋ 当场改题面」
  ｜⚠️ follow the steps → take it step by step；data → date 拼写不算
- 2026-09-13 📝 题面整改：提示「一句之内和两句之间都不许跳」→「一句之内不许跳」——
  09-12 整改写过头了，与本条 08-20 判据（泛指 you 换具体 I 分属两句 ⇒ 不算跳）打架；题面照判据改回
- 2026-09-15 ✅ 学习日 在池第 1 组 · ① `I like cooking because I follow the steps and get something to show for it.` ② `At the cinema, you can get fully immersed in the movie; it also doubles as a date night.` —— ① 全句 I，② you…it，一句之内零跳 → **连对2，毕业**
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 提示改正向）
  去掉"一句之内不许跳"负向写法，改成"定了就一路用到底"；换成跑步、在家办公两个新场景（两句都省主语，照旧逼她自己定人称）
- 2026-09-30 ✅ 复检 · 付息日 a2 第 3 组 [5] · 两句人称一路 I／my／me
- 备注 08-05 一天内跳了 3 次（原 #55）
- 备注 合并 2026-08-19：#55（人称一致·一段里）并入本条 —— 同一条规则，只是范围一句/一段

### 50 · "好找/好用/好记"用 easier，不用 more convenient（convenient ＝ 方式省事）
类型 搭配 ｜ 旧号 B73
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

**问题是什么**
**"好找／好用／好记"用 easier，⛔ 不用 more convenient**：
· **convenient ＝ 方式／安排省事、省时间**（跟【人】或【做法】走）——
　convenient for you ／ a convenient time ／ more convenient to book online ／ to stay in touch
· **easy／easier ＝ 难度低、不费劲**（跟【动作本身的难度】走）——
　easier to find ／ to remember ／ to use ／ to get to
判据一句话：这句说的是【方式省事】还是【事情不难】？方式省事 → convenient ｜ 事情不难 → easy／easier。
⚠️ 判据 2026-08-21 收紧过一次：原来写的"convenient 后面只能跟【人】"是从 08-16 一个实例过度概括出来的，太宽
（当天 #80 那句 `makes it much more convenient than ever to stay in touch` 判 ✅ 是对的，详见当天历史行）。

**怎么发现的**
旧 B 表迁移（B73，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-16 ❌ `more convenient to find` → easier to find。
2026-08-19 ✅ `makes them much easier to find` ⇒ 2026-08-20 毕业。
2026-09-05 ✅ easy to find；2026-09-07 复检（打包）✅ `it's easier to find next time`。

**我错在哪**
她的：`more convenient to find`（2026-08-16）　　正确：`easier to find`
找法：要写 convenient 之前先问一句 —— 说的是"方式省事"还是"事情不难"？不难就换 easier。

**题面**
"下次好找"

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-16 ❌ `more convenient to find` → easier to find
- 2026-08-17 ✅
- 2026-08-19 ✅ `makes them much easier to find`（同句主语形态错归新建 #254）
- 2026-08-21 ⚠️ **判据修正（不动档位、不动毕业）**：原判据"convenient 后面只能跟【人】"是
  **从 08-16 那一个实例过度概括出来的，太宽**。今天 #80 那题她写 `makes it much more convenient
  than ever to stay in touch`，教练判 ✅ 不扣 —— 复核后确认判 ✅ 是对的，是**判据本身要收紧**：
```
convenient ＝ **方式/安排省事、省时间**（跟【人】或【做法】走）
   ✓ convenient for you ／ a convenient time ／ It's more convenient to pay by card
   ✓ more convenient to book online ／ to stay in touch      ← 说的是"这个方式省事"
easy / easier ＝ **难度低、不费劲**（跟【动作本身的难度】走）
   ✓ easier to find ／ easier to remember ／ easier to use ／ easier to get to
判据一句话：问"这句说的是【方式省事】还是【事情不难】？"
   方式省事 → convenient ｜ 事情不难 → easy/easier
   ✗ more convenient **to find** —— 找东西是难度问题，不是方式问题
```
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· easy to find（easier 一族，⛔ 没落进 more convenient）
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `it's easier to find next time`（easier，⛔ 没落进 more convenient）
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [2b] · `Easy to find next time.` —— easy，没落成 convenient
- 备注 ★ 本条就是她 08-21「直译要 case by case 建」那条规则的**正面样本**：
  `more convenient to find` 这个具体 case 早在 08-11 就有自己的号（本条），
  却又被 08-16 复制进伞形条目 #157 的日志里 ⇒ **同一个 case 占两个号、走两条 streak**，
  #157 那条永远清零、她被反复问。#157 已于 08-21 迁出 methods.md，本条保留。

### 51 · put sth away ＝ 收起来（clean up ＝ 打扫脏东西）
类型 词组 ｜ 旧号 B74
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 词组

**问题是什么**
**put sth away** ＝ 把东西收起来（put sth **back** 同样对）；**clean up ＝ 打扫脏东西** —— 两件事。
同一格里的邻居（别串）：`tidy up the toys` 合法、也符合旧题面，但绕开 put sth **away**（＝ 考点）
⇒ 2026-09-10 题面补点名「用 **put** 说」（点动词、留介词，⛔ 未泄露 away）。
判据一句话：东西本来干净、只是没归位 ⇒ put away／back；地上脏了要擦 ⇒ clean up。

**怎么发现的**
旧 B 表迁移（B74，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `children put toys back/away after playing with them.`（put away／back 都对）⇒ 毕业。
2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：说"收拾"先分一刀 —— 是归位（put away／back）还是擦干净（clean up）？

**题面**
"把玩具收回去"（用 **put** 说）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `children put toys back/away after playing with them.`（put away／back 都对）
  ⚠️ 同句 toys→their toys（指称层，归 #63 备注）
- 2026-09-10 📝 题面补点名「用 **put** 说」· 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面「"把玩具收回去"」—— `tidy up the toys` 合法且符合题面，绕开 put sth **away**（＝ 考点）。
  ⇒ 点动词、留介词（与 #104「"扎进"用 bury 说」同一个做法），⛔ 未泄露 away。
- 2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ① 同级说法
  tidy up the toys／clean up your toys 在"收玩具"上都是地道说法（美式 clean up 就是归位），put away 只是其中一个 ⇒ 中译英里产不出 ❌；历史零 ❌

### 52 · 去掉 "X is important" 的壳（把动作提上来当谓语）
类型 减法型 ｜ 旧号 B75
状态 连对2 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
**去掉 "X is important" 的壳**：把动作提上来当谓语 —— `parents should **explain** why to kids.` ／ `You also need to explain…`
⛔ 不要 `explaining what rules are for … is also important`（动作被降级成主语，句子重心塌了）。
判据一句话：谓语是 is important 吗？是 ⇒ 把主语里那个动作提上来当谓语，壳整个拆掉。

**怎么发现的**
旧 B 表迁移（B75，2026-08-18）；最早记录 2026-08-17 ✅（教练当天误判 ❌ 已撤销：她那句是完全正确的英语）。
2026-08-19 ❌ **自由产出**（新题 bank:489）· 触发原话 `explaining what rules are for … is also important`。
2026-08-20 ✅ `parents should explain the 'why' to kids`；2026-08-23 ✅ `parent should explain why, not just what, to kids.` ⇒ 连对 2，毕业。
2026-09-05 复检第 4 组 ✅ `Parents should **explain** why to kids.`

**我错在哪**
她的：`explaining what rules are for … is also important`（2026-08-19 自由产出）
正确：`You also need to explain…` ／ `parents should explain why to kids.`
找法：写完一句回头看重心 —— 谓语要是 is important，就把主语里的那个动作提上来。

**题面**
**点名**："跟孩子讲清为什么也很重要。"（把 it's important 的壳拆掉说）

- 2026-08-17 ✅（教练当天误判 ❌ 已撤销：她那句是完全正确的英语）
- 2026-08-19 ❌ **自由产出**（新题 bank:489）· `explaining what rules are for … is also important`
  ⇒ 把动作降级成主语、重心塌了；口语做法是提上来当谓语：You also need to explain…
- 2026-08-20 ✅ 复习 · `parents should explain the 'why' to kids`——壳整个拆掉，explain 提上来当谓语
- 2026-08-23 ✅ 付息日 a 段（08-21 泄题顺延，今天补出）· `parent should explain why, not just what, to kids.`
  ——壳整个拆掉，动作提上来当谓语 → **连对2，毕业**
  ⚪ `parent` 单数裸用（该 parents）⇒ 属 #63（泛指不带 the），形态类·不召回，只做记号
  ⚠️ `why／what` 当名词用时要带 the（08-20 她写的 `explain the 'why' to kids` 是对的）；
    收件人也别被插入语推远：`explain **to their kids** the why, not just the what` 更顺 —— 不建条目（§3.2b 第三档）
- 2026-09-05 ✅ 复检组 · 第 4 组 · `Parents should **explain** why to kids.` —— it's important 的壳拆掉，动作提上来当谓语
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组 · `Explaining why to your kids matters.`——壳拆掉了，"讲清为什么"直接当主语

### 53 · organized（说人）＝ 有条理会安排，不是守规矩
类型 词汇 ｜ 旧号 B76
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 词组

**问题是什么**
**organized（说人）＝ 有条理、会安排**，⛔ 不是"守规矩"。
同一格里的邻居（别串）：同一道题里的"东西乱七八糟" ＝ **leave a mess**（＝ 🎓#186，08-19 她自发调出来过）。
判据一句话：说一个人 organized，讲的是他**会安排自己的事**，不是他听话。

**怎么发现的**
旧 B 表迁移（B76，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `ths kid is pretty organised. he left a mess.` ⇒ 毕业。
2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：用 organized 说人之前确认一句 —— 要夸的是"会安排"，不是"守规矩"。

**题面**
"有条理"（形容词，说人） ／ "东西乱七八糟"

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `ths kid is pretty organised. he left a mess.`（organised 说人 ＋ 自发调出 🎓#186 的 leave a mess）
- 2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；organized 说人她一直用对，是稳定会的基础词

### 54 · 比较级只标一次（more easier ❌）
类型 语法 ｜ 旧号 B77
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 词组

**问题是什么**
**比较级只标一次**：`it's much **easier**`，⛔ 不是 more easier。
判据一句话：一个形容词的比较级要么加 **-er**、要么加 **more**，⛔ 不许两样同时上。
★ 与 #10（主谓一致）／#147（时态只标一次）／#92（否定别丢）同属一条元规则：
　**每个语法标记在一个谓语上只能出现一次，而且必须出现一次**。

**怎么发现的**
旧 B 表迁移（B77，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅，08-16／08-17 各 ✅ ⇒ 2026-08-17 毕业。
2026-09-09 复检第 3 组 ✅ `it's much easier` —— 比较级只标一次。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存 —— 条目名里的 `more easier` 是要她避开的那条路。
找法：写完比较级数一下标记 —— -er 和 more 只能留一个。

**题面**
"容易多了"

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 3 组 · `it's much easier` —— 比较级只标一次
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌（形态类但从没掉过 ⇒ 不走只记录，§3.6）；much easier 她一直对
- 备注 与 #10 主谓一致／#147 时态只标一次／#92 否定别丢同属一条元规则：
  **每个语法标记在一个谓语上只能出现一次，而且必须出现一次**

### 57 · date night（约会之夜）
类型 词组 ｜ 旧号 B80
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

**问题是什么**
**date night** ＝ 约会之夜（【date ＋ 一个名词】的固定块）。
同一格里的邻居（别串）：`make an evening of it` ＝ 把一晚上过得像回事
（We usually make an evening of it — dinner first, then a film.）——
2026-08-23 c 段定：**降为备注、⛔ 不单独建条目**（她从没测过、也不是她犯的错，频率偏低）。
判据一句话："约会（那一晚）"这一层直接调固定块 date night。

**怎么发现的**
旧 B 表迁移（B80，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-21 ✅ 复习（点名题面首测）· `for us, going to the cinema feels like date night.` ⇒ 连对 2，毕业。
2026-09-11 复检 · 付息日 a2 第 3 组 ✅ `date night`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"约会"时直接调 date night 这个块，⛔ 别去造一句话解释它。

**题面**
"两口子的约会之夜"（专门留出来、两个人单独出去过的那一晚）

- 2026-08-17 ✅ 首次进流
- 2026-08-21 ✅ 复习（点名题面首测）· `for us, going to the cinema feels like date night.`——date night 一字不差 → **连对2，毕业**

- 2026-08-23 📝 c 段 **降为备注，不拆号**：`make an evening of it` 从未测过，也不是她犯的错，
  是迁移时带进来的目标块、频率偏低 ⇒ **不单独建条目**，留作备注：
  make an evening of it ＝ 把一晚上过得像回事（We usually make an evening of it — dinner first, then a film.）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `date night`
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉【date ＋ 一个名词】形态描述，改成中文释义

### 58 · it mainly comes down to …（说到底就是……）
类型 词组 ｜ 旧号 B81 ｜ ⭐ 她自产
状态 连对2 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

**问题是什么**
**it mainly comes down to …** ＝ 说到底就是……（把一堆原因收成一个点）。
同一格里的邻居（别串）：boil down to（同义、合法；题面正向点名 come，down／to 两个小词的去留正是考点）；
⚠️ 与 #317（when it comes to）只差一个 **down** —— 2026-09-03 她把本块错塞进了 when it comes to 的槽位，
　09-04 同一天里两个方向各测到一次、都对 ⇒ 归因成立："太熟的块会去占相邻槽位，要靠问自己要哪个意思来挡"。
判据一句话：要说"归根到底是…"⇒ comes **down** to；要说"谈到…"⇒ when it comes to（**没有** down）。

**怎么发现的**
旧 B 表迁移（B81，2026-08-18，⭐ 她自产），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `It mainly comes down to money.`（全程零 ❌，连对 2 出池）⇒ 毕业。
此后四次自发命中留痕：08-28 `it just comes down to different reasons…` · 08-31 `it mainly comes down to visual effects.` ·
09-04 `It mainly comes down to two factors.` · 09-11 重答 R10 `It mainly comes down to the internet.`

**我错在哪**
她的：本条历史里没有掉过（🎓 零 ❌ 线）；唯一一次相邻滑动是 09-03 把这个块塞进 when it comes to 的槽位（已另立 #317）。
找法：说"说到底"之前先问自己要哪个意思 —— 归根到底（comes **down** to）还是谈到（when it comes to）。

**题面**
"我们最后没买那套房子，说到底还是因为离学校太远。"（"说到底"用 **come** 说）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `It mainly comes down to money.`（全程零 ❌，连对 2 出池）
- 2026-08-28 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 复习第3组 #290 句里 ·
  `it just **comes down to** different reasons…`——**题面完全没提这个块**，她自己接上去的
  （同句里 comes down to ＋ 发散的复数理由语义顶牛，那一层归 #290 的 ⚠️，与本条的"块调不调得出"无关）
- 2026-08-31 📝 付息日 c 段 · **自发命中留痕**（🎓 状态行冻结，契约⑦，不推进不改判）
  a 段第 2 组 [2]（#56 的题面"主要是看视觉效果"）· `it **mainly comes down to** visual effects.`
  ★ 题面只逼 visual effects 这一处，**本块是她自己接上去的** ⇒ 自发命中。
  ★ §4① 加速通道边界核：本条 08-19 即零 ❌ 毕业，不存在"刚掉的那一格" ⇒ 不涉边界，正常留痕。
  上一次同类留痕 ＝ 08-28（`it just comes down to different reasons…`，同样是她自己接上去的）。
- 2026-09-04 📝 **自发命中**（本条已毕业，只留痕、不推进数字 · §3.1⑦）· 新题第 1 道开头
  `**It mainly comes down to** two factors.`
  ★ 与本条判据**逐字相同**，而且落在它真正的槽位（把一堆原因收成一个数）。
  ★★ 值得单独记的一笔：09-03 她把这个块错塞进了 `when it comes to` 的槽位（→ 新建 #317）；
    今天同一天里，第 1 组她挡住了不该有的 down（#317 ✅），这里放行了该有的 down（本条命中）——
    **同一个块的两个方向，一天之内各测到一次，都对。**
    ⇒ 09-03 归因（"太熟的块会去占相邻槽位，要靠问自己要哪个意思来挡"）当场被证成。
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 7 组（打包串，她原话："除了 3）忘了，其他直接过"）
- 2026-09-11 ✅ 自发命中 · 付息日 d 段重答 R10（自由产出）· `It mainly comes down to the internet.` —— 块一字不差；今天第 7 组她刚 ⚡ 免测它，自由产出里自己用出来了（§3.5 rc 证据，冻结的连对不动）
- 2026-09-13 ✅ 自发命中 · 学习日 新题 bank:238（P3 · 自由产出）· `Most of it really comes down to respect`——09-11 R10 里刚自发用过一次，今天又来（rc 证据，冻结的连对不动）
- 2026-09-15 ✅ 新题 bank:1059 自发命中 · `I think it mainly comes down to his patience and willingness to help`
- 2026-09-18 ✅ 自发命中 · 学习日 新题 bank:353（P3 · 自由产出）· `A big part of it comes down to the place each sport needs`——连续第四篇自发用出来（rc 证据，冻结的连对不动）
- 2026-09-19 ✅ 自发命中 · 付息日 d 段重答 R11（P3 · 自由产出）· `It all comes down to whether you have time.`——连续第五篇自发用出来（rc 证据，冻结的连对不动）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉「⛔ boil」，点名 come —— down／to 的去留正是她和 #317（when it comes to）互相串槽的地方；换成买房场景

### 59 · 直接疑问 vs 嵌入疑问：嵌进句子里就用陈述语序
类型 语法 ｜ 旧号 B82＋B146
状态 连对2 连错0 上次2026-08-29 ｜ 回潮已断（08-20 回潮）｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
**直接疑问 vs 嵌入疑问**：
· 直接疑问（含修辞问句）⇒ **倒装**：`what **will it** be next time?` ／ `what **did you** eat yesterday?`
· 嵌进句子里（名词性从句／关系从句）⇒ **陈述语序**：`I don't know what **you ate** yesterday.` ／
　`depending on **who you ask**` ／ `As for **how important the Yangtze River is**`
判据一句话：这个疑问词后面还是不是一个独立的问句？是 ⇒ 倒装；已经嵌进别的句子 ⇒ 陈述语序。
★ 本条 ＝ 原 #211（直接疑问 vs 嵌入疑问的边界）2026-08-19 并入 —— 同一条规则。

**怎么发现的**
旧 B 表迁移（B82＋B146，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅（原 #211）。
2026-08-20 ❌ **自由产出**（加练新题 bank:927）· 触发原话
`This time it's an iPhone, but what it will be next time.`（修辞问句用了陈述语序）⇒ 回潮
——⚠️ 这是本条**第一次在真实产出里被测到**，前四次全是中译英，测不出这一层。
2026-08-21 ✅ ／ 2026-08-23 ✅ ⇒ 连对 2，毕业；08-24～08-29 连续多篇自由产出里自发命中。

**我错在哪**
她的：`but what it will be next time`（2026-08-20 自由产出）　　正确：`but what **will it** be next time`
找法：写完疑问词先看它挂在哪 —— 独立问句就倒装，挂在别的句子底下就用陈述语序。

**题面**
"你昨天吃的什么？" ／ "我不知道你昨天吃了什么。"

- 2026-08-09 ✅（原 #211）
- 2026-08-13 ✅（原 #211）
- 2026-08-15 ✅（原 #211）→ 连对 3，判毕业
- 2026-08-17 ✅ 首次进流（08-19 回补：迁移时误写"未测过"，📊 08-17 ✅ 里有 B82）
- 2026-08-20 ❌ **自由产出**（加练新题 bank:927）· `This time it's an iPhone, but what it will be next time.`
  ——这是**直接疑问**（修辞问句），要倒装 what **will it** be；陈述语序只用在嵌进句子里的时候
  ⇒ 回潮。⚠️ 这是本条**第一次在真实产出里被测到**（前四次全是中译英）—— 中译英测不出这一层
- 2026-08-21 ✅ 复习 · `what did you ate yesterday. I don't know what you ate yesterday.`
  ——本条考点两半都对；⚪ 第一句 `did you **ate**`（该 eat）属 #147，形态类·不召回，只做记号
- 2026-08-23 ✅ 付息日 a 段 · `what did you eat yesterday. I don't know what you ate yesterday.`
  ——两半都对：第一句倒装 ＋ 第二句陈述语序，连续第二次 → **连对2，毕业**（回潮后走完两次）
  ⚪ 顺带：`did you **eat**`（原形）这次也对了（08-21 写的是 did you ate）——属 #147，形态类·不召回，只做记号
- 2026-08-24 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 新题 bank:1027 两处：
  `Chengdu, where I've lived for years` ／ `a handy spot we keep coming back to`
  ——关系从句都用陈述语序、都紧贴先行词；后一句还省对了关系代词
- 2026-08-25 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 自由产出（新题 bank:987 P3）·
  `it has significantly changed the world — **how you study and work**`
  ——名词性从句用陈述语序（不是 how do you study），且两个动词并列同形
- 2026-08-25 ✅ **自发命中·同日第 2 篇**（加练新题 bank:1043 P2）· **一篇五处，全部陈述语序、全部紧贴**：
  `where each of us would **make** whatever we **wanted**` ／ `who **built** the coolest thing` ／
  `what **counted** as 'good'` ／ `whether I **was** actually engaged` ／
  `things I've seen before`（还省对了关系代词）
  ★ 这一条已经稳到"整篇不用想"的程度，记一笔备查
- 2026-08-26 ✅ **自发命中·连续第三篇**（本条未被出题，不改已毕业状态）· 自由产出（新题 bank:244 P2
  Describe a friend from your childhood，202 词）· **一篇四处，全部陈述语序、全部紧贴**：
  `how he **solves** problems under pressure` ／ `one time (when) we **needed** to present` ／
  `the kind of person (that) everyone **turns to**` ／ `the best developers (that) I **know**`
  ★ 后两处还**都省对了关系代词**（从句里那个人当宾语 ⇒ 可省）—— 与 08-25 的
    `things I've seen before` 同一个动作，连着两篇都做对
- 2026-08-27 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 付息日 b 段 #290 句里 ·
  `… totally different depending on **who you ask**.`——疑问词从句用**陈述语序**
  （✗ who do you ask）。#290 的判据里点名写着这条规则同属本条 ⇒ 两条同时命中
- 2026-08-28 ✅ **自发命中·连续第四篇**（本条未被出题，不改已毕业状态）· 复习第3组 #290 句里 ·
  `depending on **who you ask**`（不是 who do you ask）—— 陈述语序，一字不差
- 2026-08-29 ✅ 新题 P2 · **自发命中**（本条已毕业，只留痕、不推进数字）·
  `As for **how important the Yangtze River is**, …`（不是 how important is the Yangtze River）
  ——嵌入疑问用陈述语序，一次到位；而且这句同时当第四个 bullet 的路标，两件事一句话办完
  ★ **连续第二篇**在自由产出里自发命中（08-27 R5 `how much effort you put in`）
- 备注 合并 2026-08-19：#211（直接疑问 vs 嵌入疑问的边界）并入本条 —— 同一条规则；
  题面取 #211 那两句（一直一嵌，对照最清楚）。备用题面（原 #59）："得考虑路要修多宽。"

### 60 · 说一般规律用真实条件（if ＋ 现在时 ＋ 现在时）
类型 语法 ｜ 旧号 B83
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
**说一般规律用真实条件**：**if ＋ 一般现在时 ＋ 一般现在时**，从句里⛔ 不放 will／may
（if they have less to lose ／ if they're taking on less risk）。
同一格里的邻居（别串）：`every time ＋ 现在时` 完全合法，但那样测不到"if 从句里不放 may／will"这一层
⇒ 题面正向点名 if；**主句放 will 是另一回事**
（见 #286 的 `if public transport is …, many commuters **will** …`）。
判据一句话：if 从句里一出现 will／may ⇒ 一定错。

**怎么发现的**
旧 B 表迁移（B83，2026-08-18）；最早记录 2026-08-19 ❌ 复习 #85 句里 ·
触发原话 `if they may lose less`——真实条件句里放了 may。
2026-08-20 ✅ 全句现在时、没有情态混入（未用 if ⇒ 题面当天改，下次逼 if）；
2026-08-23 ✅ `The design is flawed. you always get stuck if you take that road.` ⇒ 连对 2，毕业。
2026-08-27 ✅ 自发命中（#286 句里）；2026-09-11 复检 ✅。

**我错在哪**
她的：`if they may lose less`（2026-08-19）　　正确：`if they **have** less to lose` ／ `if they're taking on less risk`
找法：写完 if 从句扫一眼 —— 里面混进 will／may 了吗？有就删掉、换回现在时。

**题面**
"周末去那家火锅店的话，一般都得排一个小时的队。"（"…的话"用 **if** 说）

- 2026-08-19 ❌ 复习#85 句里 · `if they may lose less`——真实条件句里放了 may
- 2026-08-20 ✅ 复习 · `there is something wrong with the desgin, so you get stuck every time you drive down the road`
  ——全句现在时，没有情态混入（desgin 是打字，按 §2.1 不算）｜ 未用 if ⇒ 题面已改，下次逼 if
- 2026-08-23 ✅ 付息日 a 段（08-21 泄题顺延，今天补出）· `The design is flawed. you always get stuck if you take that road.`
  ——**if ＋ 现在时 ＋ 现在时**，一字不差；用 always 顶掉 every time 也正合题面 → **连对2，毕业**
  ★ `The design is flawed.` 比 08-20 的 `there is something wrong with the design` 利落一档
- 2026-08-27 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 付息日 b 段 #286 句里 ·
  `**if** public transport **is** cheap, frequent and reliable, many commuters **will** …`
  ——从句用一般现在时（is，不是 will be），主句才放 will ⇒ 本条规则用对
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `If the design is flawed, you get stuck in traffic every time you take that route.` —— if ＋ 现在时 ＋ 现在时，⛔ 没用 will（本场新补的排除项生效）；every time 只当时间状语、没顶替 if
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"别用 every time／⛔ 不用 will"，正向点名 if；if 从句里放不放 will 留给她（她掉过的就是 may 混进 if 从句）；换成火锅店排队场景

### 61 · run a red light ／ get stuck in traffic
类型 词组 ｜ 旧号 B84
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

**问题是什么**
两个固定块：**run a red light** ＝ 闯红灯 ／ **get stuck in traffic** ＝ 堵在路上。
判据一句话：动词是块的一部分 —— 红灯配 **run**，堵车配 **get stuck in**。

**怎么发现的**
旧 B 表迁移（B84，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流
（08-19 回补：迁移时误写"未测过"）。
2026-08-19 ✅ **自由产出里自发用对**（新题 bank:489）· `if everyone run red lights at will`
—— 这个块当天没在任何讲评里出现过，是干净的 cold 数据 ⇒ 2026-08-20 毕业。
2026-09-10 ⚡ 自评免测 · 复检第 3 组。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：这两个块整块调 —— 红灯前面放 run，堵车用 get stuck in。

**题面**
"半夜路上没车也闯红灯"（没等绿灯就开过去） ／ "在环线上堵了一个多小时"（被车流困住动不了）

- 2026-08-17 ✅ 首次进流（08-19 回补：迁移时误写"未测过"，📊 08-17 ✅ 里有 B84）
- 2026-08-19 ✅ **自由产出里自发用对**（新题 bank:489）：`if everyone run red lights at will`
  —— 这个块今天没在任何讲评里出现过，是干净的 cold 数据
- 2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景）
  题面补齐两个块（闯红灯 ／ 堵在路上），各配中文释义；换场景

### 62 · drive past sth／drive down that road（past 是介词，pass 是动词）
类型 搭配 ｜ 旧号 B85＋B99
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**drive past sth**（past 是**介词**）／ **drive down that road** —— pass 是动词、past 是介词，两个别混。
同一格里的邻居（别串）：⛔ by／through（题面已排除）。
判据一句话：drive 后面接"经过某地"这一层 ⇒ 用介词 **past**。
★ 本条 ＝ 原 #187 2026-08-19 并入（同一个词组 drive past）。

**怎么发现的**
旧 B 表迁移（B85＋B99，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅（原 #187）。
2026-08-15 ✅（原 #187）⇒ 判毕业；2026-08-17 ✅（原 #62）。
2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写 drive past 时记住 past 是**介词** —— ⛔ 别写成动词 pass。

**题面**
"开车经过那所学校"（⛔ 不许用 by／through）

- 2026-08-09 ✅（原 #187）
- 2026-08-13 ✅（原 #187）
- 2026-08-15 ✅（原 #187）→ 判毕业
- 2026-08-17 ✅（原 #62；08-19 回补：迁移时误写"未测过"，📊 08-17 ✅ 里有 B85）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 3 题整串，她原话："1-4 直接过"）
- 2026-09-29 📝 退池 · ①③ 同级说法 ＋ 口语里测不出
  drive by 同样地道；past／pass 在口语里几乎同音，那一半是书写层 ⇒ 中译英口语里产不出 ❌；历史零 ❌
- 备注 合并 2026-08-19：#187 并入本条（同一个词组 drive past）。题面取 #187 那句——
  原 #62 的题面"我每次开过那条路都堵。"里的"堵"会串到 #61／#68，弃用

### 64 · forward or back ≠ back and forth（固定词序）
类型 词组 ｜ 旧号 B87
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个也毕业了"）｜ 退池 ｜ 题型 词组

**问题是什么**
**forward or back**（三词块，固定词序）≠ **back and forth**（来回，＝ 🎓#23）—— 两个块意思不同、词序不同。
同一格里的邻居（别串）：⛔ back and forth（题面已排除；同组出题时它最容易把本条带跑）。
判据一句话：说"前进也不行、后退也不行"用 **forward or back**；说"来回跑"才是 back and forth。
★ 标题里"whether 后面要跟主谓"那一半 2026-08-23 已拆出成 **#275**（本条题面根本测不到它），本条只留固定词序。

**怎么发现的**
旧 B 表迁移（B87，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ◎ 题面没逼出。
2026-08-19 ✅ `no non can move, forward or back.`（没被同组的 back and forth 带跑）；
2026-08-20 ✅ `no one can move, forward or back` ⇒ 她当场指定毕业（"这个也毕业了"）。
2026-09-11 复检 ✅ `fowward or back`（fowward 属拼写，§2.1 不算错）。

**我错在哪**
她的：本条没有掉过（08-17 那次是 ◎ ＝ 题面没逼出），触发原话未存。
找法：说"前进也不行后退也不行"时整块调 forward or back，⛔ 别让 back and forth 抢跑。

**题面**
"前进也不行，后退也不行"（一个三词块 · ⛔ 不许用 back and forth）

- 2026-08-17 ◎ 题面没逼出
- 2026-08-19 ✅ `no non can move, forward or back.`（forward or back 没被同组的 back and forth 带跑；no non 是打字滑）
- 2026-08-20 ✅ `no one can move, forward or back`——同上，且 no one 也写对了
- 2026-08-23 📝 c 段 **拆号**：标题里"whether 后面要跟主谓"那一半与本条（固定词序）是**两条不同规则**，
  而本条题面（"谁都动不了，前进也不行后退也不行"）**根本测不到 whether** ⇒ 那一块从未被验过却跟着毕业了
  ⇒ 拆出 **#275（whether 后面要跟主谓）**，从 0 起算、进池；本条只留 forward or back，🎓 不动
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `fowward or back` —— 三词块、词序对、未用 back and forth（fowward 属拼写，§2.1 不算错）
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ① 同级说法
  "前进也不行后退也不行"说 forward or backward／move at all 都成立，三词块只是其中一种 ⇒ 中译英里产不出 ❌；历史零 ❌
- ⚠️ 拆号待办：标题里"whether 后面要跟主谓"那一半**本题面测不到** ⇒ 付息日另立一条，从 0 起算
  ★ **2026-08-31 c 段结案：已兑现，属陈账。** 见本条上方 08-23 那行 —— 已拆出 **#275
    （whether 后面要跟主谓）**，从 0 起算并进池，条目现存于档案。⛔ 本条的 🎓 与任何数字未动。

### 65 · neither … NOR（不能 neither … or）
类型 语法 ｜ 旧号 B89
状态 连对2 连错0 上次2026-09-13 ｜ 旧账 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 退池 ｜ 题型 整句

**问题是什么**
**neither … NOR**（双联词焊死）—— ⛔ 不能 neither … or。
`I can **neither** cook **nor** bake.` ／ `users could **neither** log in **nor** place orders`（两边都是光动词原形，共用前面的 could）。
同一格里的邻居（别串）：`I can't cook or bake` 完全合法、还更口语（08-19 她答的正是这句）⇒ 题面已排除 can't … or；
⚠️ 同族的 `neither of us didn't follow` 是**双重否定**（＝ #35），别混。
判据一句话：起头用了 neither，后面那个连接词只能是 **nor**。

**怎么发现的**
旧 B 表迁移（B89，2026-08-18，旧账），原始触发原话未存；最早记录 2026-08-09 ✅；2026-08-11 📖 给了答案才会。
2026-08-19 ◎ 她答 `I can't cook or bake` 完全合法且更口语 ⇒ 题面的锅，当天加点名。
2026-09-01 📝 新题 P3（bank:490）自发命中留痕 · `users could **neither** log in **nor** place orders`。
2026-09-05 复检第 1 组 ✅ `I can neither cooke nor bake.`（cooke 属拼写，§2.1 不算错）。

**我错在哪**
她的：2026-08-11 那次"给了答案才会"（📖），触发原话未存；08-19 的 `I can't cook or bake` 是合法绕路、⛔ 不算错。
找法：一旦起头用了 neither，后面那个连接词只能写 nor。

**题面**
**点名**："我既不会做饭也不会烘焙。"（用 **neither** 起头的那个双联词说，⛔ 不许用 can't … or）

- 2026-08-09 ✅
- 2026-08-10 ✅
- 2026-08-11 📖 给了答案才会
- 2026-08-12 ✅
- 2026-08-16 ✅

- 2026-08-19 ◎ 她答 `I can't cook or bake` 完全合法且更口语 ⇒ 题面的锅，当天加点名
- 2026-09-01 📝 新题 P3（bank:490）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）
  `users could **neither** log in **nor** place orders` —— nor 用对，且两边都是光动词原形（共用前面的 could）。
  ★ 08-16 她在自由产出里掉过同一族（`neither of us didn't follow`，原 #124），今天 cold 一次到位。
- 2026-09-05 ✅ 复检组 · 第 1 组 · `I can neither cooke nor bake.`（cooke 属拼写，§2.1 不算错）
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组 · `I neither cook nor bake.`——neither … nor
- 2026-09-29 📝 退池 · ① 同级说法
  她答的 `I can't cook or bake` 完全合法、还更口语（条目自己写着）；neither … nor 她 09-01 已自发用对 ⇒ 口语线里测不出缺口

### 67 · 可分离动词短语的位置（代词必须放中间：put it away）
类型 结构 ｜ 旧号 B95
状态 连对1 连错0 上次2026-09-28 ｜ **🎓 已毕业 2026-08-21 · 她指定**（"这个也是"）｜ 题型 整句

**问题是什么**
**可分离动词短语的位置**：唯一硬规则是**代词只能放中间** —— put **them** away ✅ ／ put away **them** ✗。
同族：turn it off ／ pick her up ／ throw it away ／ work it out ／ give it back。
同一格里的邻居（别串）：**名词两边都行** —— put the toys away ＝ put away the toys
⇒ 这正是中译英测不到本条的原因（她把"它们"还原成名词就绕过去了）。
判据一句话：宾语是代词吗？是 ⇒ 必须夹在动词和小品词中间。
★ 本条 `⛔ 复习组停出`（2026-08-21 定）：只在自由产出里抓。

**怎么发现的**
旧 B 表迁移（B95，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ❌ 首次进流。
2026-08-21 ✅ 复习（当天刚改的题面首测）· `put away the toys after playing with them.`——句子合法且符合题面 ⇒ 记 ✅，
**她当场指定毕业**（原话："这个也是"）；但她把"它们"还原成了名词 the toys ⇒ **本条真正的考点仍然没被测到**。
★ 她 08-21 的质疑："这个也是，为什么反反复复问，上次错了？"——核数据后确认本条只被测过 2 次（详见下方 ★★ 块）。

**我错在哪**
她的：2026-08-17 首次进流 ❌（触发原话未存）；08-21 那次把"它们"还原成 the toys，绕开了考点。
找法：宾语是 it／them／her 这类代词时，把它塞进动词和小品词中间（put **them** away）。

**题面**
**点名**："玩具玩完了就把它们收起来。"（用 put … away 说 —— 考点是"它们"摆在哪儿）
★ 题面 2026-08-21 改：旧题面"孩子玩完把玩具收起来。"里"玩具"是名词，**逼不出本条考点**（考点是"代词必须放中间 put it/them away"，名词放中间放后面都合法）⇒ 改成"它们"，让代词位置成为唯一解

- 2026-08-17 ❌ 首次进流
- 2026-08-21 ✅ 复习（今天刚改的题面首测）· `put away the toys after playing with them.`
  ——句子完全合法**且符合题面** ⇒ 按 §3.3（她 08-20 定）记 ✅ ＋ **她当场指定毕业**
  ★ 但她把"它们"还原成了名词 the toys ⇒ **本条真正的考点（代词必须放中间）今天仍然没被测到**
- ★★ **她 08-21 的质疑**："这个也是，为什么反反复复问，上次错了？"
```
数据       本条**只被测过 2 次**：08-17 ❌ 首次进流 → 08-21（今天），中间隔 4 天没出过
           ⇒ 不属于"反复问"那一类；她的感觉大概率是被 #157（6 天 5 次）带出来的
但真问题   **中译英这个测法对本条无效**：
           旧题面"孩子玩完把玩具收起来"里"玩具"是名词，而考点是"代词放中间"，
           名词放中间放后面都合法 ⇒ 这条**从建立起就测不到自己**。
           今天改成"它们"想逼出来，她又把"它们"还原成 the toys ⇒ 中译英绕得掉，测法本身不成立。
⇒ 处理     ① 照她指定毕业 ② 打 `⛔ 复习组停出`：本条**只在自由产出里抓**
           （出现 put away it／turn off it／pick up her 这种才判档位）
```
- 2026-09-15 📝 产出验机制取消 ⇒ 恢复出题：题型格回默认「整句」、删掉 ⛔ 复习组停出 标记、题面换回留档的那条真题面（点名「它们」，逼出代词必须放中间）
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 2026-09-28 ✅ 复检第 2 组 · `After playing toys, you should put them away.`
- 备注 唯一硬规则：**代词只能放中间** —— put **them** away ✅ ／ put away **them** ✗
  同族：turn it off ／ pick her up ／ throw it away ／ work it out ／ give it back
  名词则两边都行：put the toys away ＝ put away the toys
- 备注 另：away 不变形；玩具搭配是 play with

### 68 · IN/DURING the morning rush hour（早高峰）
类型 搭配 ｜ 旧号 B98＋B96
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-15**（合并后重算）｜ 退池 ｜ 题型 词组

**问题是什么**
**IN／DURING the morning rush hour** ＝ 早高峰的时候（介词用 in／during，⛔ 不是 at）。
同一格里的邻居（别串）：本条原来还捆着 stuck in traffic，那一块 2026-08-19 归了 #61，本条只留 rush hour。
判据一句话：rush hour 是一**段**时间 ⇒ 介词用 in／during，⛔ 别摸点时间的 at。
★ 本条 ＝ 原 #185（the morning rush hour）2026-08-19 并入 —— 两条题面几乎逐字相同。

**怎么发现的**
旧 B 表迁移（B98＋B96，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅（原 #185）。
2026-08-15 ✅（原 #185）⇒ 连对 3、判毕业；2026-08-17 ✅ 首次进流。
2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"高峰的时候"先看它是一段时间 —— 一段就用 in／during。

**题面**
"早高峰的时候"（用【介词＋名词】说 · ⛔ 不许用 at）

- 2026-08-09 ✅（原 #185）
- 2026-08-13 ✅（原 #185）
- 2026-08-15 ✅（原 #185）→ 连对 3，判毕业
- 2026-08-17 ✅ 首次进流
- 2026-08-19 📝 **合并＋拆条**：#185（the morning rush hour）并入本条 —— 两条题面几乎逐字相同；
  本条原来还捆着 stuck in traffic，那个归 #61，本条只留 rush hour
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 3 题整串，她原话："1-4 直接过"）
- 2026-09-29 📝 退池 · ① 同级说法（原判据有误）
  at rush hour 本身就是标准说法（in／during 也对），原条目"⛔ 不是 at"是假错；历史零 ❌

### 69 · pay attention TO sth（同族：listen TO／focus ON／concentrate ON）
类型 搭配 ｜ 旧号 B107b
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**pay attention TO sth**（介词写死是 **to**）；同族：listen **TO** ／ focus **ON** ／ concentrate **ON**。
判据一句话：pay attention 要接对象 ⇒ 一律 to；focus／concentrate 那一族才是 on。

**怎么发现的**
旧 B 表迁移（B107b，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-17 ◎ 她答 `pay much attention in class` 完全合法 → 当天改点名。
2026-08-19 ✅ 点名 · `he doesn't pay much attention to his teachers in class` ⇒ 毕业。
2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）。

**我错在哪**
她的：`pay much attention in class`（08-17，判 ◎ ＝ 题面没逼出，⛔ 不记错）
正确：`pay much attention **to** his teachers in class`
找法：写完 pay attention 就问一句 —— 注意的是什么？把 to ＋ 那个对象接上去。

**题面**
**点名**："注意听老师讲的东西"（"注意"用 **pay attention** 说 —— 后面接什么自己定）

- 2026-08-11 ✅
- 2026-08-16 ✅
- 2026-08-17 ◎ 她答 `pay much attention in class` 完全合法 → 改点名
- 2026-08-19 ✅ 点名 · `he doesn't pay much attention to his teachers in class`
- 2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌（08-17 是 ◎）；pay attention to 是她稳定会的基础搭配

### 70 · I wouldn't go THAT far, though.（软化自己刚说的话）
类型 词组 ｜ 旧号 B109a
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**I wouldn't go THAT far, though.** ＝ 软化自己刚说的话（整块背，重心在 **that far**）。
同一格里的邻居（别串）：块本身是 go **that** far —— ⛔ 不是 go too far（08-11 教练自己写错过一次，见尾部备注）。
判据一句话：要往回收一步时整块调 `I wouldn't go that far, though.`，⛔ 别现造。

**怎么发现的**
旧 B 表迁移（B109a，2026-08-18），原始触发原话未存；最早记录 2026-08-11 📖 给了答案才会，
08-12／08-13／08-15 连三次 ❌。
2026-08-16 ✅ ／ 2026-08-19 ✅ `I wouldn't go that far, tough`（tough 是打字滑，块本身对）⇒ 2026-08-20 毕业。
2026-09-05 ✅ ／ 2026-09-07 复检（打包）✅ `but I wouldn't go that far`。

**我错在哪**
她的：08-12／08-13／08-15 连三次 ❌（触发原话未存，旧 B 表迁移）；08-11 是"给了答案才会"。
找法：要把刚说过的话收一收时，整块调 `I wouldn't go that far, though.`

**题面**
"不过我也不会说得那么绝。"（用 **go** 那个词说）

- 2026-08-11 📖 给了答案才会
- 2026-08-12 ❌
- 2026-08-13 ❌
- 2026-08-15 ❌
- 2026-08-16 ✅
- 2026-08-19 ✅ `I wouldn't go that far, tough`（tough 是打字滑，块本身对）
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· I wouldn't go that far（整块调出，that far 一字不差）
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `but I wouldn't go that far`（go that far 整块；wouldn't 拼写不算错 §2.1）
- 2026-10-01 ✅ 复检 · 学习日 复检第 4 组 [9] · `Calling him a genius? I wouldn't go that far.` —— I wouldn't go that far
- 备注 08-11 教练自纠：块本身写错过（go too far → go that far）

### 71 · It's not that A — it's about B.（把矛头从对象转到程度）
类型 词组 ｜ 旧号 B109c
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**It's not that A — it's about B.** ＝ 把矛头从**对象**转到**程度**：
`it's not that the game itself is bad — it's about how long you play.`
同一个框的后半随语境换：**It's not that A, it's just B**（"不是…，只是…"：`It's not that I don't want to go, I'm just lazy.`，原 🎓#15 的一块归到这里）
同一格里的邻居（别串）：`It's not the game itself; it's how long you play.` 英文没问题，但框没出来 ⇒ 题面正向点名 It's not that。
判据一句话：起手必须是 **It's not that ＋ 一个完整从句**，后半用 it's about … ／ it's just … 接。

**怎么发现的**
旧 B 表迁移（B109c，2026-08-18），原始触发原话未存；最早记录 2026-08-11 📖。
2026-08-12 ✅ ／ 2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-09-05 复检第 1 组（打包）✅ `it's not that the game itself is bad - it's about how long to play.` 框整块调出。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：2026-08-11 那次"给了答案才会"（📖），触发原话未存；此后没有掉过。
找法：要把话从"这东西不好"转到"多少的问题"时，起手先落 It's not that …，后半接 it's about …。

**题面**
"不是我不想帮你，只是我这周真的忙不过来。"（用 **It's not that** 起头）

- 2026-08-11 📖
- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-09-05 📝 题面整改 · 复检组第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面 "不是游戏本身不好，是看玩多久。" 存在第二个同样合法、且**绕开考位**的译法：
  `It's not the game itself; it's how long you play.` —— 英文没问题，但本条的目标框
  （It's not that A — it's about B）一次都没出现 ⇒ 测了等于没测。
  ⇒ 按 §6「有第二译法 → 当场在题面点名（可点句型/块）」补上框限定，⛔ 未给整句答案。
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· `it's not that the game itself is bad - it's about how long to play.` 框整块调出
  ｜ ⚠️ 顺带：how long to play → how long you play（不落号，考位已命中）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 7 组（她原话："5-9 直接过"）
- 2026-09-29 📝 归并 · 🎓#15 的 It's not that A, it's just B 块归本条（同一个 It's not that … 框，后半 just／about 各随语境）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉负向排除，正向点名 It's not that；题面换成"不是不想帮，只是忙"—— 用上并进来的 it's just B 那一半

### 72 · in moderation（适度）
类型 词组 ｜ 旧号 B109d
状态 连对2 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

**问题是什么**
**in moderation** ＝ 适度（【in ＋ 一个名词】的固定块）。
同一格里的邻居（别串）：`Everything in moderation` 本身是英语现成的**省略式谚语**，
⛔ 不按"悬空片段"判（§7 禁用书面标准评口语）；完整版是 `Everything's fine in moderation.`
判据一句话："适度"这一层用介词块 in moderation，⛔ 不拆成形容词讲。

**怎么发现的**
旧 B 表迁移（B109d，2026-08-18），原始触发原话未存；最早记录 2026-08-11 📖，2026-08-17 ✅。
2026-08-21 ✅ 复习（点名题面首测）· `everything in moderation`——一字不差 ⇒ 连对 2，毕业。
2026-09-05 复检第 4 组（打包）✅ in moderation。

**我错在哪**
她的：2026-08-11 那次"给了答案才会"（📖），触发原话未存；此后没有掉过。
找法：说"适度／悠着点"时直接调 in moderation 这个介词块。

**题面**
"甜食可以吃，适度就好"（不过量、有节制）

- 2026-08-11 📖
- 2026-08-17 ✅
- 2026-08-21 ✅ 复习（点名题面首测）· `everything in moderation`——in moderation 一字不差 → **连对2，毕业**
  ★ `Everything in moderation` 本身是英语现成的省略式谚语，不按"悬空片段"判（§7 禁用书面标准评口语）；
    完整版是 `Everything's fine in moderation.`
- 2026-09-05 ✅ 复检组 · 第 4 组（打包）· in moderation
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组（打包）· `in moderation`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉【in ＋ 一个名词】形态描述，改成中文释义；换成吃甜食场景

### 73 · stuck WITH ＝ 被迫接受甩不掉
类型 词组 ｜ 旧号 B117c
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-19 · 她指定** ｜ 题型 整句

**问题是什么**
**stuck WITH sb／sth** ＝ 被迫接受、甩不掉（介词写死是 **with**）：`I got stuck with him`。
同一格里的邻居（别串）：stuck **ON**（＝ 卡在某道题上，🎓#248）—— 同一个 stuck、两个介词，⛔ 别混。
判据一句话：甩不掉的是**人或东西** ⇒ stuck with；卡住的是**一道题** ⇒ stuck on。

**怎么发现的**
旧 B 表迁移（B117c，2026-08-18），原始触发原话未存；最早记录 2026-08-11 📖；08-12 ❌ ／ 08-15 ❌。
2026-08-19 ✅ `every time we got put in pairs, i got stuck with him` ⇒ **她当场指定毕业**
（原话："没错的都赶紧毕业了，不知道回答多少次了"）。
2026-09-05 ✅ get stuck with；2026-09-07 复检（打包）✅ `get stuck with`。

**我错在哪**
她的：08-12 与 08-15 各记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：说"甩不掉"先看甩不掉的是谁／什么 —— 人或东西 ⇒ stuck **with**。

**题面**
"那个沙发买错了又退不掉，我只能一直凑合着用。"（"只能凑合着用"用 **stuck** 说）

- 2026-08-11 📖
- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-15 ❌
- 2026-08-16 ✅
- 2026-08-19 ✅ `every time we got put in pairs, i got stuck with him`
  🎓·她指定（"没错的都赶紧毕业了，不知道回答多少次了"）—— 连对 2 提前出池
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· get stuck with
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `get stuck with`（介词 with 对）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 stuck，介词 with 留给她（她掉过两次）；换成买错沙发场景（⛔ 不再用"跟他一组"原句）
- 2026-10-01 ✅ 复检 · 学习日 复检第 4 组 [10] · `I bought the wrong sofa and can't return it, so I'm just stuck with it.` —— stuck with it

### 74 · make do with（将就）／整块 I'll have to make do with …
类型 词组 ｜ 旧号 B121＋B171a
状态 连对2 连错0 上次2026-10-02 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**make do with sth** ＝ 将就用（整块：`I'll just have to make do with this old computer`）。
同一格里的邻居（别串）：⛔ made do **it** with（08-11 她写过的错形）——
make do 后面**直接**接 with，中间不插宾语。
判据一句话：make do 和 with 之间不许再塞东西。
★ 本条 ＝ 原 #99（make do with）2026-08-19 并入 —— 同一个词组，#74 只是多带一个 have to。

**怎么发现的**
旧 B 表迁移（B121＋B171a，2026-08-18）；最早记录 2026-08-11 ❌ · 触发原话 `made do it with`（原 #99）。
2026-08-15 ❌ ／ 2026-08-16 ❌（原 #74）；2026-08-17 ✅ ／ 2026-08-19 ✅ `you have to make do with that old laptop` ⇒ 2026-08-20 毕业。
2026-08-19 ⛔ 题面整改：原题面"只能将就这台旧电脑。"没有主语，**她当场指出**（"出题出完整，这主意我自己补的"）。
2026-09-05 ✅ `I'll just have to make do with this old computer`；2026-09-07 复检（打包）✅ `make do with`。

**我错在哪**
她的：`made do it with`（2026-08-11）　　正确：`make do **with** that old laptop`
找法：make do 后面直接上 with，⛔ 中间别塞 it。

**题面**
"我这台旧电脑只能将就着用了。"（"将就"用 **make** 那个词组说）

- 2026-08-11 ❌ `made do it with`（原 #99）｜同日原 #74 记过 ✅ ⇒ 同日一对一错，按"以最后一次为准"
  无法判先后，**保守记 ❌**
- 2026-08-12 ✅（原 #99）
- 2026-08-15 ❌（原 #74）
- 2026-08-16 ❌（原 #74）｜同日原 #99 记 ✅ ⇒ 同上，保守记 ❌
- 2026-08-17 ✅
- 2026-08-19 ✅ `you have to make do with that old laptop`
- 2026-08-19 ⛔ 题面整改：原题面"只能将就这台旧电脑。"没有主语，她当场指出
  （"出题出完整，这主意我自己补的"）—— §6 已写死题面必须完整句，08-17 提过一次，教练又犯
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· I'll just have to make do with this old computer
  （整块 ＋ 语气词 just have to 全中）
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `make do with`
- 2026-10-02 ✅ 复检 · 学习日 复检第 4 组 [7] · `My dorm room didn't have a desk, so I had to make do with my suitcase.` —— make do with，with 没漏

- 备注 合并 2026-08-19：#99（make do with）并入本条 —— 同一个词组，#74 只是多带一个 have to
- 备注 备用题面（原 #99）："没有筷子，我就拿勺子凑合了一下。"

### 75 · other than（除了）≠ rather than（与其/而不是）
类型 搭配 ｜ 旧号 B122
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 退池 ｜ 题型 词组

**问题是什么**
**other than（除了）≠ rather than（与其／而不是）**—— 两个 than 收尾的两词块，词义完全不同：
`other than him`（除了他）／ `rather than waiting`（与其等着）。
同一格里的邻居（别串）：#266（"除了…" ＝ apart from／other than／except，besides 放句首会被读成"此外"）
同管"除了"这个意思，但目标形式不同 —— 本条考的是**别和 rather than 混**，#266 考的是**选哪个词组最稳**；
rather than 的两条**形态**规则在 🎓#245（两边同形）／🎓#246（领独立短语用 -ing），本条只管词义辨析。
判据一句话：说"除了" ⇒ other than；说"与其／而不是" ⇒ rather than。

**怎么发现的**
旧 B 表迁移（B122，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 📝 拆条＋改题面：本条原来还捆着 complain ABOUT（已是 🎓#229），原题面又与 #88 逐字相同 ⇒ 只留辨析、换题面。
2026-08-20 ✅ 复习（改题面后首测）· `no one knows the thing, other than him.` ＋ `rather than waiting, we should just leave.` ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `other than him` ／ `rather than waiting` —— 两处没用同一个块。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写到 than 收尾的两词块时先问一句 —— 这句是"除了"还是"与其"？

**题面**
**点名**："除了他" ／ "与其等着"（两个都译 —— 各是一个 **than** 收尾的两词块，⛔ 两处不许用同一个块）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 📝 **拆条＋改题面**：本条原来捆着 complain ABOUT（已经是 🎓#229）和 other than ≠ rather than；
  原题面"与其抱怨，他直接就干了。"又和 #88（get on with it）逐字相同 ⇒
  本条只留 other than／rather than 的辨析，题面换成两句能分开测的
- 2026-08-20 ✅ 复习（改题面后首测）· `no one knows the thing, other than him.` ＋
  `rather than waiting, we should just leave.`——两个块词义都用对 ⇒ 连对2 毕业
  ｜同句 `the thing` 归新建 #260，不算本条头上
- 2026-08-21 📝 **互斥留痕**（不动档位、不动毕业）：新建 #266（"除了…" ＝ apart from／other than／except，
  besides 放句首会被读成"此外"）与本条同管"除了"这个意思，但**目标形式不同**：
  本条 ＝ other than（且考点是**别和 rather than 混**）｜#266 ＝ apart from（考点是**选哪个词组最稳**）。
  ⚠️ 本条题面"除了他没人知道这事。"与 #260 共用一句已经在跑（两条落在句子不同位置，可分别记档），
  但**不能再让 #266 也用这句**（同一个槽位会互斥）⇒ #266 题面另起"除了我妈，没人知道我辞职了。"
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `other than him` ／ `rather than waiting` —— 两个 than 收尾的两词块，两处没用同一个
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ③④ 题面收不拢 ＋ 底子不明
  "除了他"→ except him／apart from him，"与其等着"→ instead of waiting 都合法，不点英文词逼不出 other／rather than，点了又等于给答案；旧 B 表迁移、历史零 ❌
- 备注 rather than 的两条形态规则在 🎓#245（两边同形）／🎓#246（领独立短语用 -ing），本条只管词义辨析

### 76 · 比较里的泛指不加 the（cheaper than new ones）
类型 语法 ｜ 旧号 B124
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 整句

**问题是什么**
**比较里的泛指不加 the**：`Second-hand ones are much cheaper than **new ones**.`——两侧都不带 the。
同一格里的邻居（别串）：**ones** 用来替掉重复的那个名词（second-hand ones ／ new ones）。
判据一句话：比较的两边都是"泛指的一类" ⇒ 都不带 the，可数就用复数（或 ones）。

**怎么发现的**
旧 B 表迁移（B124，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `Second-hand ones are much cheaper than new ones.` ⇒ 毕业。
2026-09-10 复检第 4 组 ✅ 同一句，泛指两侧都不带 the。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：写完 than 看后面那个名词 —— 泛指就别带 the，重复的名词换成 ones。

**题面**
"二手的比新的便宜多了。"

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `Second-hand ones are much cheaper than new ones.`（new ones 不带 the ＋ ones 替重复名词）
- 2026-09-10 ✅ 复检 · 第 4 组 · `second-hand ones are much cheaper than new ones.` —— 泛指两侧都不带 the
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；泛指比较两边不带 the 她一直对（冠词类，从没掉过 ⇒ 不走只记录）

### 77 · 平台用 on，实体店用 at（on Amazon／at Walmart）
类型 搭配 ｜ 旧号 B125
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 词组

**问题是什么**
**平台用 on，实体店用 at**：on Amazon ／ at Walmart。
判据一句话：它是一个**线上平台** ⇒ on；是一家**实体店** ⇒ at。

**怎么发现的**
旧 B 表迁移（B125，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `I bought it on Amazon.`（平台用 on；过去式也对）⇒ 毕业。
2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：说"在某处买的"先分一刀 —— 线上平台 on，实体店 at。

**题面**
"在亚马逊上"

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `I bought it on Amazon.`（平台用 on；过去式也对）
- 2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；on Amazon 她一直对

### 78 · a pack of napkins（量词块）
类型 词组 ｜ 旧号 B126
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 退池 ｜ 题型 词组

**问题是什么**
**a pack of napkins** ＝ 一包纸巾（量词块：a ＋ 量词 ＋ of ＋ 名词，整块调）。
同一格里的邻居（别串）：网购说"商品页"是 **the product page**（同族 the checkout page／the listing）——
那一半 2026-08-23 c 段定**降为备注、⛔ 不单独建条目**（低频网购名词，不是她的语言缺口），08-27 她在自由产出里自己补齐了。
判据一句话："一包／一盒 X"整块调 a pack of ＋ 名词，⛔ 别把量词丢了。

**怎么发现的**
旧 B 表迁移（B126，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `a pack of napkins`（量词块对）⚠️ 另一半 the **product** page 只写了 the page ⇒ 2026-08-20 毕业。
2026-08-27 ✅ 自发命中 · 付息日 d 段重答 R7 · `a pack of tissues` ＋ `on the product page`
—— `the product page` 那一半**第一次写全**，08-23"不单独建条目"的判断被证实。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：2026-08-19 量词块对、但"商品页"只写了 the page（⚠️ 不判档位）；量词块本身没有掉过。
找法：说"一包／一盒 X"时整块调 a pack of ＋ 名词。

**题面**
"一包纸巾" ／ "商品页"

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `a pack of napkins`（量词块对）⚠️ 另一半 the **product** page 只写了 the page；
  同句时态该落过去（记进 #12 当天日志）
- 2026-08-23 📝 c 段 **降为备注，不拆号**：`the product page` 那一半 08-19 她只写了 the page、从未验过，
  但它是个**低频网购名词**、不是她的语言缺口 ⇒ **不单独建条目**（§3.2b：说不出"她不会哪个词组/句型"就别建），
  留在这里当备注：网购说"商品页"是 **the product page**；同族 the checkout page／the listing
- 2026-08-27 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 付息日 d 段重答 R7 ·
  `Imagine you're on Amazon to buy **a pack of** tissues, but you spot a 'buy 3, get 1 free'
   promotion **on the product page**`
  ——① 量词块 `a pack of` 用对（本条考点）
    ② ★★ **`the product page` 那一半今天第一次写全** —— 08-23 c 段的备注写着"08-19 她只写了
      the page、从未验过"，今天在没有任何提示的自由产出里自己补齐了
      ⇒ 当初"不单独建条目"的判断（§3.2b：不是她的语言缺口）**被证实是对的**
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（她原话："7-9 直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；a pack of 量词块她 08-27 自由产出里自发用对
- 备注 本条是捆绑条目（a pack of ＋ the product page），下个付息日按"一条＝一个考点"拆开

### 79 · 名词壳（别用"最重要的是…"这种起手）
类型 减法型 ｜ 旧号 B127
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-21** ｜ 退池 ｜ 题型 整句

**问题是什么**
**名词壳（别用"最重要的是…"这种起手）**：直接说主语该做什么 —— `parents should be organized.`
（类型标"减法型"＝ 要她**少说**一层，不是多学一个块。）
同一格里的邻居（别串）：⚠️ must → need to（must 在口语里带强制／规定味，09-11 顺带给过更好版）。
判据一句话：句子起手是不是一个名词壳（"最重要的一点是…"）？是 ⇒ 整个拆掉，直接上主谓。
★ 2026-08-17 她指出"拆壳"是术语看不懂 ⇒ 指令已改成大白话。

**怎么发现的**
旧 B 表迁移（B127，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-21 ✅ 复习 · `parents should be organized.`——"最重要的一点是"这个壳整个拆掉了 ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `Parents must be orgnized.`（orgnized 属拼写，§2.1 不算错）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：开口前先看第一个词 —— 要是"最重要的一点是"，直接删掉，从主语说起。

**题面**
**点名**："最重要的一点是家长得有条理。"（别用"最重要的是…"起手，直接说家长该做什么）

- 2026-08-17 ✅
- 2026-08-21 ✅ 复习 · `parents should be organized.`——"最重要的一点是"这个壳整个拆掉了 → **连对2，毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `Parents must be orgnized.` —— 名词壳整个拆掉、直接上主谓（orgnized 属拼写）
  ⚠️ 顺带：must → need to（must 口语里带强制/规定味）
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ① 同级说法
  "The most important thing is that parents should be organized." 本身完全成立，拆掉名词壳是表达风格建议 ⇒ 中译英里产不出 ❌；历史零 ❌
- 备注 08-17 她指出"拆壳"是术语看不懂，指令已改成大白话

### 80 · than ever 必须紧跟比较级
类型 结构 ｜ 旧号 B128
状态 连对2 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-21** ｜ ⚠️ 状态行 08-21 按日志重算（08-20 的 ✅ 当天漏回写）｜ 题型 整句

**问题是什么**
**than ever 必须紧跟比较级**：`much easier **than ever**` ／ `more convenient **than ever**` ／ `far easier than ever`。
判据一句话：中文"比以前…多了"里的"比以前" ＝ **than ever**，位置就贴在比较级后面。
同一格里的邻居（别串）：口语里 easier 比 convenient 常用得多；
但 `make it more convenient to stay in touch` 本身完全成立 ⇒ ⛔ 不许沿用 #157 对
`more convenient **to find**` 的那次结论（搭配对象不同，08-21 四问自审已留痕）。

**怎么发现的**
旧 B 表迁移（B128，2026-08-18）；最早记录 2026-08-19 ❌ 首次进池 · 触发原话
`much convenient for people to stay in touch`——than ever 整个没出来。
2026-08-20 ✅ ／ 2026-08-21 ✅ `social media makes it much more convenient than ever to stay in touch.` ⇒ 连对 2，毕业。
2026-08-31 📝 重答 R8 自发命中 · `Social media makes communicating **far easier than ever**.`
—— 同题材、零点名、开口第一句就带出来，且比较级选词也对。
2026-09-05 复检第 4 组 ✅。

**我错在哪**
她的：`much convenient for people to stay in touch`（2026-08-19 首次进池）
正确：`social media makes it much **easier than ever** for people to stay in touch`
找法：写完比较级马上问一句 —— "比以前"那半说了吗？没说就补 than ever，且贴着比较级放。

**题面**
**点名**："社交媒体让联系比以前方便多了。"（"比以前"用 than ever 说）

- 2026-08-19 ❌ 首次进池 · `much convenient for people to stay in touch`——than ever 整个没出来
- 2026-08-20 ✅ 复习（点名题面首测）· `social media makes it much easier than ever for people to stay in touch`
  ——than ever 紧跟比较级，位置对；且 easier 而不是 convenient（比较级选词也对）
- 2026-08-21 ✅ 复习 · `social media makes it much more convenient than ever to stay in touch.`
  ——than ever 紧跟比较级 more convenient，位置对 → **连对2，毕业**
  ★ 四问自审留痕：`more convenient` 不判。`make it more convenient to stay in touch` 完全成立；
    #157 在 08-16 判过的是 `more convenient **to find**`（找东西不说 convenient），**搭配对象不同**，
    不许沿用那次结论（#157 08-20 的教训就是这条）
- 2026-08-31 📝 付息日 d 段 · 重答 R8 · **自发命中留痕**（🎓 状态行冻结，契约⑦）
  `Social media makes communicating **far easier than ever**.`
  than ever **紧跟比较级**，位置一字不差 ⇒ 本条考位命中。
  ★ 含金量：本条题面就是「社交媒体让联系比以前方便多了」，08-19 她在这条上掉过
    （`much convenient for people to stay in touch`——than ever 整个没出来）。
    今天**同题材、零点名、开口第一句**就带出来了，且比较级选词也对（far easier 而非 more convenient）。
- 2026-09-05 ✅ 复检组 · 第 4 组 · `Social media makes it much **easier than ever** for people to stay in touch.`
  than ever 紧跟比较级，位置一字不差。
- 2026-09-12 📝 题面整改：删掉点名里的「考点是它摆在哪儿」（§10 禁令 5 禁预告测试点，同 #300 08-27 那次）· 全档题面 review
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组 · `Social media makes it much easier than ever for people to stay in touch.`——than ever 紧跟比较级
- 备注 中文"比以前…多了"里的"比以前" ＝ **than ever**，且必须**紧跟比较级**：
  more convenient than ever／easier than ever；口语里 easier 比 convenient 常用得多

### 81 · get TO know sb（to 不能省）
类型 搭配 ｜ 旧号 B129
状态 连对2 连错0 上次2026-09-22 ｜ **回潮 2026-08-31**（08-21 毕业 → 08-31 在 R8 重答里再犯 `know new friends`，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-03**（连对2 ＝ 09-01 ＋ 09-03；08-31 回潮后第二次毕业）｜ 题型 整句
　　★ 复测题面**不改**：现有题面 **点名**「现在更容易认识陌生人。」（"认识"用 get ＋ know 说）测的正是掉的那一格（§4① 配套动作已满足）

**问题是什么**
**get TO know sb**（to 不能省）。判据两条：
① 中文"认识（某人）"这个**动作** → get to know（know sb ＝ 已经认识的**状态**）
② stranger／new people 只能"变得认识" ⇒ `know a stranger`／`know new friends` 自相矛盾
判据一句话：说的是"从不认识到认识"的**过程** ⇒ get **to** know。
★ 与 #336（get TO ＋ 地点）的分工：那条的 to 是**介词**，本条的 to 是**不定式标记** ⇒ 两条规则，题面互斥。

**怎么发现的**
旧 B 表迁移（B129，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ❌ `It's much eaiser to know strangers`——漏了 get。
2026-08-20 ✅ 自发命中（#8 那题）· `I got to know them in an online group`；2026-08-21 ✅ 点名首测 ⇒ 连对 2、毕业。
2026-08-31 ❌ 付息日 d 段重答 R8 · `On top of that, it's convenient to **know new friends**.` ⇒ **回潮**
（与 08-19 首犯同形；教练第一反应想新建条，判重三步第②步撞上本条后当场撤销新建）。
2026-09-01 ✅ ／ 2026-09-03 ✅ ⇒ 第二次毕业；2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：`It's much eaiser to know strangers`（08-19）／ `it's convenient to know new friends`（08-31 回潮）
正确：`It's much easier to **get to know** strangers.` ／ `it's easy to **get to know** new people`
找法：写 know ＋ 人 之前先问一句 —— 说的是"已经认识"还是"认识上"？认识上就补 get to。

**题面**
"刚搬来那会儿，我是靠打羽毛球认识了不少新朋友。"（"认识"用 **know** 说）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ❌ `It's much eaiser to know strangers`——漏了 get（know sb ＝ 已经认识的状态；
  get to know sb ＝ 从不认识到认识的过程）；另 know a stranger 自相矛盾
- 2026-08-20 ✅ **自发命中**（#8 那题，本条没被出题）· `I got to know them in an online group`（get to 齐了）
- 2026-08-21 ✅ 复习（点名题面首测）· `it's much eaiser to get to know others.`——get **to** know 的 to 没省
  → **连对2，毕业**（08-19 掉的正是这个 to）
  ｜`eaiser` 按 §2.1 拼写不算错
  ｜`others` 而不是 strangers ＝ ⚠️ 信息窄了一档，不建条目（她知道 strangers，是产出时简化）
- 2026-08-31 ❌ 付息日 d 段 · 重答 R8（P3 · What do you think of communicating via social media?）· **回潮**
  `On top of that, it's convenient to **know new friends**.`
  ★ 与 08-19 首犯（`It's much eaiser to **know strangers**`）**同形**：know sb ＝ 已经认识的状态，
    "认识新朋友"说的是**从不认识到认识的那个过程** ⇒ get to know。
    且 know new **friends** 自相矛盾（既然已是 friends 就已经认识）。
  ★ **决定性证据（为什么归本条、不新建）**：本条备注逐字写着「判据两条：① 中文"认识（某人）"这个
    **动作** → get to know ② stranger/**new people** 只能"变得认识"」——"new people" 四个字
    就写在判据里；按本条规则改 ⇒ `it's easy to get to know new people` ⇒ **得到正确答案** ⇒ 同一条规则。
  ★ 教练侧留痕：第一反应是新建一条（"认识新朋友 ＝ make friends／meet people"），
    §3.1 判重三步的第②步（全档 grep 含已毕业）撞上本条后**当场撤销新建**。
  ★ 复测题面够不够用（§4① 配套）：现有题面 **点名**「现在更容易认识陌生人。」（"认识"用 get ＋ know 说）
    —— 测的正是今天掉的这一格 ⇒ **题面不改**。
  ⇒ 🎓 吃到 ❌ ⇒ **撤销毕业、连对清零**（状态行手写，见下）
- 2026-09-01 ✅ 复习第1组 [6] · 点名直测 · 题面 `现在更容易认识陌生人。`
  `It's much easier to **get to know** strangers.`
  考点 get **TO** know —— to 在位（08-31 掉的正是这个 to：`know new friends`）。
  ⚠️ 同句另一处（**不属本条考点，不判 ❌、不新建号**）：漏译"现在" ⇒ 更好版
    `It's much easier to get to know strangers **these days**.`
    判据：中文"**现在**更容易"里的"现在"是比较的另一头（＝比以前）；
    英文 comparative ＋ 没有 than ⇒ 必须有一个时间／范围词兜住（these days／now／
    compared with ten years ago），否则"比什么"悬着。
    ★ 不建号：§3.2b 自查说不出"她不会的是哪个词组／句型"（这是漏译一个词，不是缺口）。
    ★ 另比对 🎓#26（比较题必须说出另一边）：那条 `⛔ 复习组停出`、只在自由产出里判，
      管的是整段答案里 B 那一边有没有出现，不是句内时间坐标 ⇒ **不适用**，未归号。
  ★ 组内对调生效验证：本条排在 #8 之前测（见 session 文件留痕），
    #8 那题她第一句用的是 met 而不是 got to know ⇒ **本次 ✅ 是干净的独立数据点**，未被污染。
  ⇒ 连对0 连错1 → **连对1**（回潮后第一次翻正，差一次毕业）
- 2026-09-03 ✅ 复习第1组 [1] · 点名直测 · 题面 `现在更容易认识陌生人。`
  `It's much eaiser to **get to konw** strangers.`
  考点 get **TO** know —— to 在位（08-31 回潮掉的正是这个 to：`know new friends`）。
  ｜`eaiser`／`konw` 按 §2.1 拼写不算错（正确拼法 easier／know），不建条目、不记档位。
  ⚠️ 同句另一处（**不属本条考点，不判 ❌、不新建号**）：**第二次**漏译"现在" ⇒ 更好版
    `It's much easier to get to know strangers **these days**.`
    ★ 与 09-01 那次**同题、同处、同一个词**，裁定完全一致（⚠️ 不建号）——
      理由 ＝ `It's much easier to meet people.` 母语者天天说 ⇒ "比较级必须带时间锚"不是硬规则
      ⇒ §3.2b 说不出"她不会的是哪个词组／句型" ⇒ 建号就是假错。
    ★ 但**第二次这件事本身要记**：08-31 她在自由产出（R8）里自己写过 `far easier than ever`，
      锚是她自己加的 ⇒ **她会**，缺的是产出时那一下检查 ⇒ 走检查触发，不走条目。
      检查触发：写完一个比较级，回头看 —— **"比什么"说出来了吗？**（than … ／ 时间词，二选一）
  ★ 组内重排生效验证（第二次，见 session 文件留痕）：本条排在 #8 **之前**测，
    #8 那题她第一句写的是 `met` 而不是 got to know ⇒ **本次 ✅ 是干净的独立数据点**。
  ⇒ 连对1 → **连对2，毕业**（08-31 回潮后第二次翻正；状态行手写，见上）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 5 组（第 11 题整串，她事后补的原话："11直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  考点是 know 前面补不补 get to ＝ 靠句子现形；点名 know（给 lemma，get to 留给她 —— 她掉过两次的正是漏 get to）；换成打羽毛球场景

### 83 · 形容词不加复数（crucial 不是 crucials）；crucial TO
类型 语法 ｜ 旧号 B131
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 退池 ｜ 题型 整句

**问题是什么**
**形容词不加复数**（crucial 不是 crucials）；**crucial TO sth**（接对象的介词是 **to**）：
`Start-ups are **crucial to** the economy.`
同一格里的邻居（别串）：同一句她曾把 vital 写成 virtual（选词，已另立 #255），与本条考点无关。
判据一句话：形容词永远不带 -s；crucial 后面接对象用 to。

**怎么发现的**
旧 B 表迁移（B131，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `start-ups are virtual to the economy`——形容词不加复数 ＋ TO 都对 ⇒ 2026-08-20 毕业。
2026-09-10 复检第 4 组 ✅ `Start-ups are crucial to the economy.`

**我错在哪**
她的：本条考点历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写完形容词看一眼尾巴有没有多出 -s；要接对象时用 to。

**题面**
"创业公司对经济很关键。"（形容词用 **crucial** 说）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `start-ups are virtual to the economy`——形容词不加复数 ＋ TO 都对
  ⚠️ 同句选错了词（virtual 应为 vital）⇒ 新建 #255，不影响本条考点
- 2026-09-10 ✅ 复检 · 第 4 组 · `Start-ups are crucial to the economy.` —— crucial 不加 -s ＋ crucial **TO**
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；形容词不加 -s、crucial to 她一直对（vital／virtual 那一块已另立 #255）

### 84 · 条件句别纠结（every time/whenever 在场 → 现在时；说将来 → will）
类型 语法 ｜ 旧号 B132
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-21** ｜ 退池 ｜ 题型 整句

**问题是什么**
**条件句别纠结**：every time／whenever 在场 ⇒ 现在时；说将来 ⇒ will。
说一般规律走**真实条件**：`if no one **is** willing to start a business, there **aren't** as many jobs.`
同一格里的邻居（别串）：`If nobody **wanted** to start a business, there **wouldn't** be so many jobs.` 完全合法，
但它绕开"说一般规律用真实条件"这一格 ⇒ 2026-09-11 题面补了「⛔ 不用虚拟语气」。
⚠️ 顺带：as many → so many（as many 要有比较对象）。
判据一句话：讲的是**一般规律**还是**假设**？一般规律 ⇒ 真实条件（现在时 ＋ 现在时）。

**怎么发现的**
旧 B 表迁移（B132，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-21 ✅ 复习（点名题面首测）· `if no one wants to start their own business, there are enough jobs to go around.` ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `if no one is willing to start a business, there aren't as many jobs.` —— ⛔ 没滑进虚拟语气。

**我错在哪**
她的：本条考点历史里没有掉过（判定全是 ✅）；08-21 同句丢掉的否定归 🎓#92、只做记号。触发原话未存。
找法：写 if 之前先定性 —— 说的是一般规律就全用现在时，⛔ 别顺手滑进 wanted／wouldn't。

**题面**
**点名**："如果没人愿意创业，就没那么多岗位。"（用 if 从句说 · 当一般规律说，⛔ 不用虚拟语气）

- 2026-08-17 ✅ 首次进流
- 2026-08-21 ✅ 复习（点名题面首测）· `if no one wants to start their own business, there are enough jobs to go around.`
  ——考点＝条件句时态：if 从句 wants ／ 主句 are，同一平面、合法 → **连对2，毕业**
  ⚠️ 同句**否定丢了、意思反了**（"就没那么多岗位"写成"岗位够分"）⇒ 归 🎓#92 **只做记号、不记档位**
    （她 08-21 定："漏了否定，不是不会，不要练"；#92 带 `形态类·不召回`，按 §3.4 只在自由产出里判档位）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `if no one is willing to start a business, there aren't as many jobs.`
  —— if ＋ 现在时 ＋ 现在时，真实条件，⛔ 没滑进虚拟语气（本场新补的排除项正是挡这个）
  ⚠️ 顺带：as many → so many（as many 要有比较对象）
- 2026-09-11 📝 题面整改：补（· 当一般规律说，⛔ 不用虚拟语气）· 发题前审核（§6.5 第 7 项 · **换结构**那一类）
  `If nobody wanted to start a business, there wouldn't be so many jobs.` 完全合法，
  却绕开「说一般规律用真实条件」这一格 ⇒ 补时态限定。今天她答的正是真实条件 ⇒ 排除项生效
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ① 同级说法
  "如果没人愿意创业"用虚拟语气 `If nobody wanted …, there wouldn't be …` 完全合法（条目自己写着），真实／虚拟只是说话人的立场选择 ⇒ 中译英里产不出 ❌；历史零 ❌

### 85 · start / set up a business（不用 create）＋ take on risk
类型 搭配 ｜ 旧号 B135
状态 连对2 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-20**（连对2） ｜ **合并条·出题多句覆盖** ｜ 题型 词组

**问题是什么**
一道题面覆盖两个成员：
· **start ／ set up a business** ＝ 创业（落成**动词短语**，⛔ 不用 create、⛔ 不落成名词）
· **take on risk** ＝ 承担风险（"承担"用 **take on**）
同一格里的邻居（别串）：`entrepreneurs face lower risks` 完全合法、也符合题面（08-20 判 ✅），只是不是本条的目标块。
判据一句话："创业"要落成一个动词短语；"承担风险"整块调 take on risk。

**怎么发现的**
旧 B 表迁移（B135，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ❌ 首次进流。
2026-08-19 ✅ `start their own business` ＋ 她自己补的 `take on less risk`（两个块都出来了）；
2026-08-20 ✅ 走 `When entrepreneurs face lower risks…`——不是原目标块，但完全合法且符合题面 ⇒ 连对 2，毕业。
2026-08-31 📝 重答 R9 自发命中 · `people are more willing to **start their own businesses** if they **take on less risk**.`
—— 零点名、题目本身没提风险，是她自己加进来的，两个成员一次全中。
2026-09-05 复检 ✅ 两个成员都到位：start（⛔ 不是 create）／take on risks。

**我错在哪**
她的：2026-08-17 首次进流 ❌（触发原话未存，旧 B 表迁移）。
找法："创业"先找动词（start／set up），⛔ 别落成名词或 create；"承担风险"整块调 take on risk。

**题面**
题面（2 句，两个成员各一句）
　① "辞职出来自己创业"（自己开公司当老板）
　② "敢承担风险"（愿意冒这个险、担后果）

**成员出题账**
① start／set up a business ｜ 08-19 ✅ · 08-20 ✅（走 entrepreneurs 那条合法路）· 08-31 ✅ 自发 · 09-05 ✅
② take on risk ｜ 08-19 ✅ · 08-20 ✅（同上）· 08-31 ✅ 自发 · 09-05 ✅
★ 08-17 首次进流那一次 ❌ 未按成员记录。

- 2026-08-17 ❌ 首次进流
- 2026-08-19 ✅ `start their own business` ＋ 她自己补了 `take on less risk`（两个块都出来了）
  ⚠️ 同句 `if they may lose less` 的条件句错归 #60
- 2026-08-20 ✅ `When entrepreneurs face lower risks, tthey are more willing to take actions.`
  ——走的是 entrepreneurs ＋ face lower risks，不是本条原目标块，但**完全合法且符合题面**
  ⇒ 按 08-20 新规则算 ✅（两个原目标块 08-19 已验过）
  ｜同句 `take actions` 归新建 #261，`tthey` 是打字不算
- 2026-08-31 📝 付息日 d 段 · 重答 R9 · **自发命中留痕**（🎓 合并条，状态行冻结）
  `people are more willing to **start their own businesses** if they **take on less risk**.`
  ★ 本条是合并条（start／set up a business ＋ take on risk），今天**两个成员一次全中**。
  ★ 零点名，且**题目本身没提风险** —— 是她自己把这一层加进来的。
  ★ 本条题面就是「创业的人承担的风险小了，就更愿意干」⇒ 今天等于在自由产出里原样命中了题面那句话的两个块。
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· 两个成员都到位：start（⛔ 不是 create）／take on risks
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组 · 两个成员都出都对 · ① `start a business` ② `take on risks`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉英文点名，题面改成合并条的编号句（两个成员各一个中文块，§3.2c 多句覆盖）

### 86 · go ON a trip / take a trip（不是 go to a trip）＋ where to STAY
类型 搭配 ｜ 旧号 B138
状态 连对2 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ **合并条·出题多句覆盖** ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-21 毕业 → 09-05 复检 ✅ → 09-11 付息日重答 R10 自由产出里写成 `where to live`，后半格 where to STAY 掉了 —— 与 08-07 建号触发句一字不差，撤销毕业、连对清零。顽固已断的记号撤回：同一格五周后原样回来）

**问题是什么**
一道题面覆盖两个成员（同一场旅行语境里的两个块）：
· **go ON a trip ／ take a trip**（出去玩、旅行）—— ⛔ 不是 go **to** a trip
· **where to STAY**（旅行说"住哪儿"）—— ⛔ 不是 where to live
判据：live ＝ 长期居住／**stay ＝ 短期落脚**（旅行说"住哪儿"永远是 stay）；
go out ＝ 出门一晚／**go on a trip ＝ 出去玩（旅行）**
同一格里的邻居（别串）：plan a trip 也完全合法（08-20 判 ✅，只是不是本条的目标形式）；
"查"住哪儿 ＝ look **up**（查资料），⛔ 不是 look for（＝ 找，见 #100）。
★ 判定的唯一依据是**题面**，不是条目的目标形式 —— 09-05 她提异议、教练当场改判 ✅ 的那次就是这个口径。

**怎么发现的**
旧 B 表迁移（B138，2026-08-18）；建号触发句留在 09-11 那一行里：
**08-07 首答这道题时她写的就是 `where to live`**（B138 建号触发句）。
最早记录 2026-08-17 ❌ 首次进流；2026-08-19 ❌ `look up where to live` ＋ `if you want to go out`——两个块都掉。
2026-08-21 ✅ `look up where to stay before going on a trip.` 两个目标块一字不差 ⇒ 毕业。
2026-09-11 付息日 d 段重答 R10 自由产出 · `where to live` ⇒ **回潮**：同一格五周后原样回来。

**我错在哪**
她的：`where to live`（09-11 重答 R10；08-07 建号那次一字不差）　　正确：`where to **stay**`
找法：说"住哪儿"之前先问一句 —— 这次是**落脚几天**还是**长住**？几天 ⇒ stay。

**题面**
"下个月我们要出去玩几天，酒店还没定，得先查查住哪儿。"（"出去玩"用 **trip** 说，"住哪儿"用 **where to** 说）

**成员出题账**
① go on a trip／take a trip ｜ 08-19 ❌ · 08-20 ✅ · 08-21 ✅ · 09-05 ✅ · 09-11 未测到（本篇没出现）
② where to stay ｜ 08-19 ❌ · 08-20 ✅ · 08-21 ✅ · 09-05 ✅ · 09-11 ❌
★ 08-17 首次进流那一次 ❌ 未按成员记录。

- 2026-08-17 ❌ 首次进流
- 2026-08-19 ❌ `look up where to live` ＋ `if you want to go out`——两个块都掉
- 2026-08-20 ✅ 复习 · `you can look up where to stay if you're planning a trip`——**where to stay 对了**
  ｜ `plan a trip` 不是本条目标（go on a trip），但完全合法且符合题面 ⇒ 按她 08-20 新规则**算对＋改题面**，不记 ◎
  ｜ 题面已改：加"出去玩**之前**"逼出 before you go on a trip
- 2026-08-21 ✅ 复习 · `look up where to stay before going on a trip.`——**两个目标块都一字不差**：
  `where to stay` ＋ `going on a trip` → **连对2，毕业**（改题面后一次到位）
  ★ 顺带 `look up`（查资料）用对，正是 #100（look for ＝ 找）的反面，同一天两个方向都拿住；只做记号
  ★ 祈使句省了"可以"那层 ＝ 信息略省，不是语法错，不记档位
- 2026-09-05 ✅ 复检组 · 第 4 组 · `go on a trip. look for a place to live`
  两个成员都**符合题面**：go **on** a trip（⛔ 不是 go to a trip）／"查住哪儿" ＝ look for a place to live。
  ★★★ **教练当场改判（❌ → ✅）—— 她提异议，复核证实她对**：
    教练最初按"条目的目标形式是 where to **stay**"判 ❌；她的原话 ——
    "**6 题我写的没错，我希望你知道，无论是在池还是不在池，不是让我去猜你想要什么，
      至少我的回答是对的语言层面，且符合题目那就是对**"。
    复核：§3.3 硬顺序① 写死「判她这句是否**符合题面**」⇒ 教练拿错了判据对象；
    且本条原题面是带语境的整句「出去玩之前可以先查查住哪儿。」，
    今天 c 段粒度整改把它拆成两个**裸块**，第二个块脱离 trip 语境后
    `a place to live` 完全合法、完全符合题面 ⇒ **✅ 成立**。
  ｜ ⚠️ look for → look up（"查"住哪儿是查资料）—— ⛔ 不判错，只给更自然版
- 2026-09-05 📝 题面整改 · 复检第 4 组当场（**⛔ 不是因为她答错**，是缩短丢了语境）
  旧："出去玩"（用 go ＋ trip 那个说法） ／ "查住哪儿"（两个裸块，第二个无语境）
  新：**点名**："出去玩之前，先查查住哪儿。"（"出去玩"用 go ＋ trip 那个说法；"住哪儿"用 **where to ＋ 一个动词** 说）
  ★ 判据：想让某个形式成为唯一答案 ⇒ **去题面里加提示**（§6②），⛔ 不许靠判定去补题面的缺口。
  ★ 规则已补进 SKILL §6③「缩短的两个已知代价」第 ②（连同她的原话）。
- 2026-09-11 ❌ 付息日 d 段重答 R10（自由产出）· `where to live` → where to **stay** ⇒ **回潮**
  旅行语境（how to get to the destination／which restaurants）里"住"＝ stay，live ＝ 定居 —— 本条后半格 where to STAY 掉了；
  前半格 go on a trip 本篇没出现（没测到）。
  ★ 08-07 首答这道题时她写的就是 `where to live`（B138 建号触发句），五周后原样回来 ⇒ 这一格没长稳
- 2026-09-13 ✅ 学习日 在池第 1 组 · `Before going on a trip, you need to first look up for where to stay.`
  成员 ① go on a trip ✅ · 成员 ② where to stay ✅（09-11 掉的是 ②，这次回来了）
  ｜同句 `look up for` ❌ 不归本条 ⇒ 新建 #337（look up sth 不带 for）
- 2026-09-15 ✅ 学习日 在池第 1 组 · `before going on a trip, you can look up where to stay.` —— 成员 ① going on a trip ✅ · 成员 ② where to stay ✅ → **连对2，毕业**
  ｜同句 look up（⛔ look up for）对了 ⇒ #337 自发命中记 ✅
- 2026-09-20 ⚡ 自评免测 · 复检第 3 组（她答"直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"用 where to ＋ 一个动词"形态描述，正向点名 trip／where to；动词 stay 留给她（她掉过的就是 where to live）；换成订酒店场景
- 2026-09-30 ✅ 复检 · 付息日 a2 第 3 组 [6] · `We're planing to take a trip for National Day, but we haven't figured out where to stay yet.`

### 87 · consider sth（及物，不带 about）
类型 搭配 ｜ 旧号 B139
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 词组

**问题是什么**
**consider sth** 是**及物**动词 —— 后面直接跟宾语，⛔ 不带 about：`AI will **consider your budget**.`
同一格里的邻居（别串）："考虑**进去**"那一层更地道的说法是 take X into account ／ factor X in。
判据一句话：consider 后面直接上宾语，中间什么介词都不加。

**怎么发现的**
旧 B 表迁移（B139，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `AI will consider your budget.`（consider 直接跟宾语，不带 about）⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ `consider your budget`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：写完 consider 直接上宾语 —— ⛔ 手别往 about 上滑。

**题面**
"考虑你的预算"（"考虑"用 **consider** 说）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `AI will consider your budget.`（consider 直接跟宾语，不带 about）
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `consider your budget` —— 及物，⛔ 没带 about
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；consider 直接接宾语她一直对，about 这条错路从没走过
- 备注 更地道的说法是 take X into account／factor X in（"考虑**进去**"那一层）

### 88 · get on with it（不废话，埋头干下去）
类型 词组 ｜ 旧号 B141
状态 连对2 连错0 上次2026-10-02 ｜ 回潮已断（08-11 曾毕业）｜ 回潮 2026-09-05（08-21 毕业 → 09-05 复检写成 `go on with it`）｜ 回潮 2026-09-27（09-10 第二次毕业 → 09-27 复检答"忘了"，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-29**（连对2 ＝ 09-28 ✅ ＋ 09-29 ✅；09-27 回潮后第三次毕业）｜ 题型 整句

**问题是什么**
**get on with it** ＝ 不废话、埋头干下去（催促）。
同一格里的邻居（别串 —— 都合法，全靠题面排除）：
· **go** on with it ＝ 接着往下讲／往下做（让他继续）—— 09-05 就是被它顶掉的
· get moving／get cracking／get going／**get a move on** —— 同样 get 起头、同样"赶紧"
⇒ 题面正向点名 get on（出整句），with it 两个词的去留正是她掉过的地方（go on with it ／ get on with）。
判据一句话：催他**动手干** ⇒ get on with it；让他**接着往下** ⇒ go on with it。块尾那个 **it** 是块的一部分。

**怎么发现的**
旧 B 表迁移（B141，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ❌。
2026-08-19 ◎ 她答 `stop talking, be quick` 完全合法（"赶紧干吧"至少三种译法）⇒ 教练没做第二译法自查，题面当场加点名。
2026-08-20 ✅ ／ 2026-08-21 ✅ `stop talking and just get on with it.` ⇒ 连对 2，毕业。
2026-09-05 ❌ 复检第 4 组 · `go on with it.` —— get 被 go 顶掉 ⇒ **回潮**。
2026-09-07 ❌ 在池第 1 组 · `get on with.` —— 块尾的 it 丢了（掉的位置和上次不一样）。
2026-09-09 ⚡ 自评免测 ／ 2026-09-10 ✅ `get on with it.` ⇒ 第二次毕业。

**我错在哪**
她的：`go on with it.`（09-05）／ `get on with.`（09-07）　　正确：`Get on with it.`（四个词一个不少）
找法：说"赶紧干"时先把动词定成 get，再把 on with **it** 三个词一个不落地跟上。

**题面**
"作业就剩最后一页了，别玩手机了，赶紧写吧。"（"赶紧写"用 **get on** 说）

- 2026-08-09 ❌
- 2026-08-10 ✅
- 2026-08-11 ✅ → 毕业
- 2026-08-15 ✅
- 2026-08-17 ❌ 回潮，重新入池
- 2026-08-19 📝 题面整改：原题面"与其抱怨，他直接就干了。"与 #75 逐字相同（那条测 rather than），
  且句里的"与其"会先触发 rather than ⇒ 换成只逼 get on with it 的句子
- 2026-08-19 ◎ 她答 `stop talking, be quick` 完全合法 ——「赶紧干吧」至少三种译法，
  **教练出题前没做第二译法自查、没点名** ⇒ 题面当场加点名，次日再测
- 2026-08-20 ✅ 复习（点名题面首测）· `Stop talking and just get on with it.`——目标块一字不差
- 2026-08-21 ✅ 复习 · `stop talking and just get on with it.`——一字不差，just 加得很自然
  → **连对2，毕业**（08-11 毕业 → 08-17 回潮，这一轮才真正走完）
- 2026-09-05 ❌ 复检组 · 第 4 组 · **回潮**
  `go on with it.` → **Get** on with it.
  ❌ 两个块形状几乎一样、意思差一整层：
    get on with it ＝ 别磨蹭了动手干（催促）／ go on with it ＝ 接着往下讲、往下做（让他继续）。
  ★ 教练侧留痕：本条**旧题面把答案 `get on with it` 整个写在括号里** ⇒ 这一测退化成"抄一遍"，
    她却抄成了 go —— 反而说明这个块在她脑子里被 go on with it 顶掉了。题面当天已改（见下条 📝）。
- 2026-09-05 📝 题面整改 · 复检第 4 组当场（⛔ 不许把考点本身写进题面）
  旧："赶紧干吧"（用 get on with it 说一遍）—— 答案整块写在括号里，测不出检索
  新："赶紧干吧"（用 **get** 起头的那个词组说，⛔ 不是 go）
  ★ 这与 09-05 粒度整改时 agent 标出的 #262／#266 是同一个病（点名把目标块整个给出）；
    #262 #266 是"工具箱"型（考摆放不考检索）⇒ 维持不改，本条是检索型 ⇒ 必须改。
- 2026-09-07 📝 题面加提示「**一共四个词**」：原题面只限「用 get 起头」，get moving／get cracking／
  get going 同样合法且同样符合题面 ⇒ 补词数把 get on with it 框死，一个实词都没泄露。
- 2026-09-07 ❌ 复习 · 在池第 1 组 · `get on with.` —— get 对了、块尾的 it 丢了
  （09-05 是 get 被 go 顶掉，这次掉的位置不一样）
- 2026-09-09 ⚡ 自评免测 · 在池第 1 组（她原话："这 10 个题直接过吧，算对"）
- 2026-09-10 📝 题面加排除项「⛔ 不是 get a move on」· 在池第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  09-07 补的「一共四个词」框不死：**get a move on** 同样是 get 起头、同样四个词、同样是"赶紧"，
  完全合法且完全符合题面 ⇒ 她答对了却会被判"没到考点"（＝ 白测一次）。
  ⇒ 补排除项 `⛔ 不是 get a move on`；⛔ 未泄露 on with it 任何一个实词。
- 2026-09-10 ✅ 复习 · 在池第 1 组 · `get on with it.` —— 四个词一字不差
  ★ 09-05 是 get 被 go 顶掉、09-07 是块尾的 it 丢了，这次两处都没掉 ⇒ **连对2，毕业**
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ❌ 复检组 · 第 2 组 · **回潮** · 她答"忘了"
  最小改 `Get on with it.`
- 2026-09-28 ✅ 在池第 1 组 · `get on with it.`
- 2026-09-29 ✅ 在池第 1 组 · `get on with it.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"get 起头／一共四个词／⛔ go／⛔ get a move on"猜谜式框法；改整句、点名 get on，with it 留给她（她掉过的正是 go on with it／get on with）；换成催写作业场景
- 2026-10-02 ✅ 复检 · 学习日 复检第 4 组 [1] · `Stop complaining and get on with the work.` —— get on with ＋ 宾语合法；题面写了"把活儿"，宾语说出来正贴题面（下次换场景别在中文里给宾语，留给 it）

### 90 · 完成时的三个触发（for/since · ever/never/before · just/already/yet）
类型 语法 ｜ 旧号 B147a
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

**问题是什么**
**完成时的三个触发**：① for／since ② ever／never／before ③ just／already／yet。
`I've **never** been on a plane.` ／ `things I've seen **before**`
同一格里的邻居（别串）：recently／lately／so far 这一族**从来没写进本条** ——
2026-08-23 按 §3.2c③ 摘出成 **#271**，本条已毕业、不动、不回潮。
⚠️ 与 🎓#91 的分工：本条管"什么词触发完成时"，#91 管"句中有具体时间点就必须过去式、不许完成时"。
判据一句话：句子里出现这三组词之一 ⇒ 把谓语切到完成时。

**怎么发现的**
旧 B 表迁移（B147a，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅，2026-08-13 ❌。
2026-08-19 ✅ `i've never been on a plane`（never 触发完成时）⇒ 毕业。
2026-08-25 ✅ 自发命中 · `I can only copy things **I've seen before**`（第二组成员）。
2026-09-11 复检 ✅ `I've never been on a plane.` —— ⛔ 没写成 I never took a plane。

**我错在哪**
她的：2026-08-13 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：写完一句扫一眼有没有 for／since、ever／never／before、just／already／yet —— 有就把谓语切到完成时。

**题面**
"我从来没坐过飞机。"

- 2026-08-12 ✅
- 2026-08-13 ❌
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `i've never been on a plane`（never 触发完成时）

- 2026-08-23 ⚪ **判据缺口留痕（不动档位、不回潮）**：她在 #269 的句子里写 `I don't have much time recently.`
  —— **recently 也是完成时触发词**，但本条只列了三组（for/since · ever/never/before · just/already/yet），
  recently／lately／so far 这一族**从来没写进本条**。
  ⇒ 按 §3.2c ③（她 08-23 定）**摘出成 #271**；本条已毕业、连对3，**不动、不回潮** ——
    她不能为一条从没写进条目里的成员被判退步
- 2026-08-25 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 加练新题 bank:1043 P2 ·
  `I can only copy things **I've seen before**`——before ⇒ 完成时，本条第二组成员，自发用对
- 2026-09-11 ✅ 复检 · 付息日 a2 第 4 组 · `I've never been on a plane.` —— never 拉出完成时，⛔ 没写成 I never took a plane

### 91 · 边界：句中有具体时间点 → 必须过去式，不许用完成时
类型 语法 ｜ 旧号 B147b
状态 连对2 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-24 · 她指定** ｜ 退池 ｜ 题型 整句

**问题是什么**
**边界：句中有具体时间点 ⇒ 必须过去式，⛔ 不许用完成时**：`I lived here **last year**.`
同一格里的邻居（别串）：一句里可以两个平面并存、各有各的理由 ——
`AI only **came out** a few years ago, but it **has** significantly **changed** the world`
（前半钉着 a few years ago ⇒ 过去式；后半说"到现在的影响" ⇒ 完成时）。
判据一句话：句子里钉着一个具体时间点（last year／a few years ago／那天）⇒ 一般过去式。
★ 与 🎓#90（完成时的三个触发）的分工：2026-08-19 判重结论**不并入 #90** ——
　两条是同一个决策的两面，但 #90 已毕业不再召回、本条当时从没被测过，并进去等于把没验过的点埋掉
　⇒ 保留本条、两边写互相引用。

**怎么发现的**
旧 B 表迁移（B147b，2026-08-18），原始触发原话未存；
2026-08-23 付息日 a 段 **本条从建立起第一次被测到** ✅ `I lived there last year.`
（⚠️ 同句 there 该是 here ⇒ ⛔ 不落号，只给检查触发："中文里的'这/那'译完回头对一眼"）。
2026-08-24 ✅ `I lived here last year` ⇒ 连对 2，**她当场指定毕业**（原话："毕业，不要再问了"）。
2026-08-25 ／ 2026-08-26 连续两篇自由产出里自发用对。

**我错在哪**
她的：本条没有掉过（两次判定都是 ✅），建号时的触发原话未存。
找法：写完一句先找时间点 —— 钉着 last year／ago／那天 就一律过去式。

**题面**
"我去年住这儿。"

- 2026-08-19 📝 判重结论：**不并入 🎓#90（完成时的三个触发）**。两条确实是同一个决策的两面，
  但 #90 已经毕业、不再召回；本条**从来没被测过**，并进去等于把一个没验过的点直接埋掉。
  ⇒ 保留，写互相引用；等它自己走完连对 3 再说
- 2026-08-23 ✅ 付息日 a 段 · **本条从建立起第一次被测到**（付息日 a 段正是这批的召回点）
  `I lived there last year.`——last year 这个具体时间点在场 ⇒ 用一般过去式 lived，没上完成时，考点达成
  ⚠️ 同句 `there` 该是 `here`（中文是"住**这儿**"）⇒ **不落号、不建条目**：
    单独问她"这儿/那儿"一定分得清，属产出时指示方向没核对（同 08-21 `缺 ago` 那次的处理）
    → 检查触发：中文里的"这/那"译完回头对一眼，here／there 别搞反
- 2026-08-24 ✅ 复习第1组 · `I lived here last year`——过去式 lived 稳住，且 here 这次没搞反
  ⇒ **连对 1 → 2 ⇒ 🎓 毕业**；**她当场指定**（原话："毕业，不要再问了"）⇒ 记「🎓·她指定」
- 2026-08-25 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 自由产出（新题 bank:987 P3）·
  `AI, for instance, only **came out** a few years ago, but it **has** significantly **changed** the world`
  ——`a few years ago` 是具体时间点 ⇒ 过去式 came out；后半句说"到现在的影响" ⇒ 完成时 has changed。
  **两个平面各有理由、没混**，正是本条要的分辨（毕业后第一次在自由产出里自发用对）
- 2026-08-26 ✅ **自发命中·连续第三篇**（本条未被出题，不改已毕业状态）· 自由产出（新题 bank:244 P2）·
  过去叙事整段全部落过去（met／ended up／were／needed／crashed／were panicking／kept／sat／went／
  found／fixed／saved，12 处）＋ `he's **become** one of the best developers I know` 用完成时说
  "到现在的变化" ＋ `These days he's **doing** really well` 用现在进行说当下
  ⇒ 有具体时间点的全落过去、说到现在的切完成时，一处没混
  ⚠️ 同篇 S4 `we **hang** out … and **mess** around`（Back then 在场，谓语停在现在时）
    按 §3.4⑤b 记 ⚪ 落在 #12，不算本条头上（本条管的是"一句里别换档"，那处是"该用哪个时态"）
- 2026-09-19 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、触发原话未存、历史零 ❌（五次判定全对）；时间点 → 过去式是她稳定会的时态判断（形态类、从没掉过 ⇒ 不走只记录）

### 92 · 否定别丢（嵌套否定：中文两个否定，英语常是一个肯定句）
类型 语法 ｜ 旧号 B148
状态 连对2 连错0 上次2026-08-19 ｜ 旧账 ｜ **累错 4** ｜ **形态类·不召回** ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**否定别丢**（嵌套否定：中文两个否定，英语常常是一个肯定句）：
"他没有一次不迟到。" → `he has **never** been on time`（两个中文否定塌成英语一个否定）。
同一格里的邻居（别串）：**自己换了说法时最容易把否定换没** ——
`there **are** enough jobs to go around`（中文是"就**没**那么多岗位"）／
`a necessary but **sufficent** condition`（漏了 not，but 两边成了同向）。
判据一句话：中文里有几个"不／没"，英文就核几次 —— 通常只标一次，但**一次都不能少**。
★ 本条 **形态类·不召回**；她 2026-08-21 定："**漏了否定，不是不会，不要练**" ⇒ 在哪儿掉都只记 ⚪。
★ 与 #10（主谓一致）／#54（比较级只标一次）／#147（时态只标一次）同属一条元规则：
　每个语法标记在一个谓语上只能出现一次，而且必须出现一次。

**怎么发现的**
旧 B 表迁移（B148，2026-08-18，旧账 · 累错 4），原始触发原话未存；最早记录 2026-08-09 ❌，连三次。
2026-08-19 ✅ `he has never been on time` ⇒ 2026-08-20 毕业。
2026-08-21 ⚪ 同日两次只做记号：复习 #84 句里 `there are enough jobs to go around`（否定整个丢了、意思反了）；
加练新题 bank:414 `Overall, advertising is a necessary but sufficent condition.`（漏了 not）。
⛔ 教练犯规·当场撤销：第一次按 §3.3 把本条掉回未毕业，**她当场否掉、她是对的** ——
§3.4 写着形态类只在自由产出／新题／重答里判档位，中译英复习不在其中 ⇒ 🎓 状态还原（毕业日期仍是 08-20）。

**我错在哪**
她的：`there are enough jobs to go around`（该 there **won't** be as many jobs）／
`a necessary but sufficent condition`（该 but **not** sufficient）
正确：`he has **never** been on time` 这一类 —— 中文两个否定塌成英语一个，但那一个不能少。
检查触发：中文出现"没有…不…／谁都不…"⇒ 英语只标一次否定
· 中译英写完，回头把中文和英文的"有／没有"对一遍；**自己换了说法（enough to go around 这类块）时最容易把否定换没**（08-21 扩写）
· 写完带 but 的对比句，回头念一遍问"**but 两边是不是真的相反？**"（08-21 再扩写）

**题面**
不出中译英题（题型 产出验 ＋ 形态类·不召回）；挂自由产出抓：否定整个丢了（意思反了）、but 两边其实不相反。
★ 原题面（留档，⛔ 不再发题）："他没有一次不迟到。"

- 2026-08-09 ❌
- 2026-08-10 ❌
- 2026-08-11 ❌
- 2026-08-12 ✅
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ✅ `he has never been on time`（两个中文否定塌成英语一个否定）
- 2026-08-21 ⚪ **只做记号，不记档位**（她 08-21 定：**"漏了否定，不是不会，不要练"**）
  复习#84 句里 · `if no one wants to start their own business, there **are** enough jobs to go around.`
  ——中文是"就**没**那么多岗位"，否定整个丢了、意思反了（→ there **won't** be as many jobs to go around）
  ⛔ **教练犯规·当场撤销**：先按 §3.3「已毕业条目在任何产出里再犯 → 回潮」把本条掉回未毕业，
    她当场否掉。**她是对的，§3.4 早就写着形态类"只在【自由产出／新题／重答】里判档位"**——
    中译英复习不在那三个里面，§3.3 的"任何产出"不适用于带 `形态类·不召回` 的条目。
    ⇒ 🎓 状态还原（毕业日期仍是 08-20），不记 ❌、不掉毕业、不进池。
  ★ 检查触发扩写（保留，属"回头自查"不属"练"）：中译英写完，回头把中文和英文的"有／没有"对一遍；
    自己换了说法（enough to go around 这类块）的时候最容易把否定换没
- 2026-08-21 ⚪ **第二次，只做记号，不记档位**（**自由产出**里的，教练做了取舍并留痕）
  加练新题（bank:414）· `Overall, advertising is a necessary but **sufficent** condition.`
  —— 漏了 **not**（necessary but **not** sufficient），but 标着转折、后面却跟同向的词 ⇒ 整句自相矛盾
  ⚠️ **她自己的两条规则在这里指向不同**：
     · §3.4② 说形态类"只在【自由产出】里判档位" ⇒ 按字面，本处该让本条回潮
     · 她 08-21 的裁决说 **"漏了否定，不是不会，不要练"** ⇒ 按精神，不该记
     取舍 ＝ **按她的裁决**（更新、更针对这一类错），只做记号。
     依据："必要不充分条件"这个概念和英文说法她都有（工科出身），单独问必答得出 ⇒ 检查没跑，不是缺口。
     **她要在自由产出里也记档位的话，一句话就能改回来。**
  ★ **检查触发再扩写**：写完带 but 的对比句，回头念一遍问"**but 两边是不是真的相反？**"

- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）


### 95 · be after ＝ 图个（追求想要的东西）
类型 词组 ｜ 旧号 B162
状态 连对2 连错0 上次2026-10-02 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**be after sth** ＝ 图个、追求想要的东西：`older people are just **after** peace and quiet`。
同一格里的邻居（别串）：本条原来还捆着 look after（＝ 照顾，已是 🎓#228）与 look for（＝ 找，＝ #100）——
2026-08-19 按"一条＝一个考点"拆条，本条只留 **be after**。
判据一句话：主语是人、后面跟的是他**想要的那样东西** ⇒ be after。

**怎么发现的**
旧 B 表迁移（B162，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅；08-13 ❌ ／ 08-15 ❌。
2026-08-19 ✅ `older people are just after peach and quiet`（peach 是打字滑；be after ＋ peace and quiet 都对）⇒ 2026-08-20 毕业。
2026-08-19 📝 题面整改：原题面第二句"他睡觉很浅。"逼不出本条任何一个词（那是 a light sleeper）⇒ 删掉。
2026-09-05 ✅ be after peace and quiet；2026-09-07 复检（打包）✅ `be after`。

**我错在哪**
她的：08-13 与 08-15 各记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：中文"图个…"直接落 be after ＋ 那样东西。

**题面**
"他退休以后搬到乡下，就想图个清静。"（"图个"用 **after** 说）

- 2026-08-09 ✅
- 2026-08-13 ❌
- 2026-08-15 ❌
- 2026-08-16 ✅
- 2026-08-19 📝 **拆条**（一条＝一个考点）：本条原来捆着 look after／be after／look for 三个词组 ——
  look after 已经是 🎓#228（08-17 毕业）· look for 是 #100 ⇒ 本条只留 **be after**，
  日志不动（它们本来就是用"图个清静"这句题面测出来的）
- 2026-08-19 ✅ `older people are just after peach and quiet`（peach 是打字滑；be after ＋ peace and quiet 都对）
- 2026-08-19 📝 题面整改：原题面第二句"他睡觉很浅。"逼不出本条任何一个词（那是 a light sleeper），
  属迁移带进来的杂质 → 删掉，只留能测 be after 的第一句
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· be after peace and quiet
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `be after`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 after，be 与宾语怎么挂留给她；换成退休搬乡下场景
- 2026-10-02 ✅ 复检 · 学习日 复检第 4 组 [8] · `She's working overtime every single day—she's only after that year-end bonus.` —— be after ＋ 想要的东西

### 96 · 否定辖域陷阱（with no overtime and stability 会被读反）
类型 结构 ｜ 旧号 B163
状态 连对1 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个也问了很多很多次了，毕业了"）｜ 旧账 ｜ 题型 整句

**问题是什么**
**否定辖域陷阱**：`a job with no overtime and stability` 会被读成"既不加班也不稳定"——
no 一路盖到 and 后面那半。两条解法：
· 解法 A 换正面名词：reasonable hours and job security
· 解法 B 拆成两个并列项：`a job **with no overtime**, and **one that is stable**`
同一格里的邻居（别串）：`I don't usually order takeaway and cook` 是同一个病（not 盖到 and 后面，听起来成了"也不做饭"）。
判据一句话：句子里出现 `not／no … and …` ⇒ 把 and 后面那半单独接回否定念一遍，意思变了就得拆。

**怎么发现的**
旧 B 表迁移（B163，2026-08-18，旧账），原始触发原话未存；最早记录 2026-08-09 ❌。
2026-08-19 ✅ `i want a job with no overtime, and one that is stable`（自己选到了解法 B）→ 当时判毕业；
**同日** ❌ `I don't usually order takeaway and cook` ⇒ 两次都是 cold、以最后一次为准 ⇒ 撤销毕业。
2026-08-20 ✅ 复习辖域正确（no 只管 overtime，stable 被拆进另一个并列项）⇒ 她当场指定毕业。
2026-09-07 复检（加练）✅ ⛔ 没写成 with no overtime and stability。

**我错在哪**
她的：`I don't usually order takeaway and cook`（2026-08-19 同日第二次）
正确：把 and 后面那半拆出去别让 not 盖过去 —— 标准解法 ＝ `a job with no overtime, and one that is stable`
找法：句子里出现 `not … and …`，把 and 后面那半单独接回否定念一遍。

**题面**
"我想要一份不加班又稳定的工作。"

- 2026-08-09 ❌
- 2026-08-10 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `i want a job with no overtime, and one that is stable`——自己选到了解法 B → 当时判毕业
- 2026-08-19 ❌ 同日 · `I don't usually order takeaway and cook`——not 一路盖到 and 后面，
  听起来是"也不做饭" ⇒ 两次都是 cold，以最后一次为准 ⇒ **撤销毕业**
- 2026-08-20 ✅ 复习 · `I want a job with no overtime, and one that is stable`——辖域正确
  （no 只管 overtime，stable 被拆进另一个并列项）⇒ 她当场指定毕业
  ★ 检查触发保留有效：`not … and …` 出现时，把 and 后面那半单独接回否定念一遍
- 2026-09-07 ✅ 复检 · 第 5 组（加练）· `I want a job with no overtime, and one that is stable.`
  —— 把 stable 挪出了 no 的辖域（另起 one that is stable），⛔ 没写成 with no overtime and stability
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 备注 分诊（与 #7 同型）：**上午单句测对、下午在长句里掉** ——
  单句时她会主动拆；句子一长、and 后面跟的是动词时，辖域检查就不跑了
  ⇒ **检查触发**：句子里出现 `not … and …`，把 and 后面那半单独接回否定念一遍
- 备注 解法A 换正面名词（reasonable hours and job security）／解法B 拆两句

### 97 · 关系词 where（先行词是 job/situation/case/kind 这类抽象"场所"）
类型 结构 ｜ 旧号 B164
状态 连对2 连错0 上次2026-10-02 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

**问题是什么**
**关系词 where**：先行词是 job／situation／case／kind 这类抽象"场所"时，关系词用 **where** ——
`he has a job **where** weekends don't exist` ／ `just an occasion **where** we could hang out` ／ `that kind of job **where** …`。
判据一句话：先行词不是真地点、但能当"一种场合／局面"读 ⇒ 用 where。

**怎么发现的**
旧 B 表迁移（B164，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅；08-13 ◎；08-15 📖 → 当天改点名 drill。
2026-08-16 ✅（同日自由产出里自发用对：`just an occasion WHERE we could hang out`）；
2026-08-19 ✅ 点名 · `he has a job where weekends don't exist` ⇒ 🎓 零 ❌ 线毕业。
2026-09-05 复检 ✅；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：本条没有掉过（08-13 是 ◎、08-15 是"给了答案才会"📖），触发原话未存。
找法：先行词是 job／situation／case／kind 这一类时，关系词直接用 where。

**题面**
**点名**："他那种工作根本没有周末。"（用 where 说）

- 2026-08-09 ✅
- 2026-08-13 ◎
- 2026-08-15 📖 → 当天改点名 drill
- 2026-08-16 ✅（同日自由产出里自发用对：`just an occasion WHERE we could hang out`）
- 2026-08-19 ✅ 点名 · `he has a job where weekends don't exist`
  🎓 零 ❌ 线（全程没有过 ❌，连对 2 提前出池；依她 08-19"没错的都赶紧毕业"）
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· that kind of job **where** …（抽象"场所"先行词配 where）
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-10-02 ✅ 复检 · 学习日 复检第 4 组 [9] · `I want to find a job where I can work remotely.` —— a job where …

### 98 · 并列两边必须同形（语法功能相同 ＋ 可数性/单复数要齐）
类型 结构 ｜ 旧号 B168＋B240
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **回潮 2026-09-19**（08-20 毕业 → 09-19 重答 R12 里 `know … even guessing what …` 第三项接不回 know，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-21**

**问题是什么**
**并列两边必须同形**：语法功能相同 ＋ 可数性／单复数要齐。
· 功能相同：`like hobbies, or just being with your kids`——名词 vs 动名词短语，同为 like 的宾语 ⇒ **成立**
　（08-20 那一行明文锁死过这个判据，09-05 反用它判 ❌ 就是假错）
· 数要齐：`sweets and biscuits`
· 三项并列也不打折：`turning up on time, meeting your deadlines, and getting along with your colleagues`
判据一句话：把两边分别接回前面那个词念一遍，都接得上才是同形。
★ 本条 ＝ 原 #151（并列两边可数性/单复数要齐）2026-08-19 并入 —— 同一条规则的两个面，题面保留两句各测一面。

**怎么发现的**
旧 B 表迁移（B168＋B240，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅；2026-08-17 ❌ 同日回潮。
2026-08-19 ✅ ／ 2026-08-20 ✅ ⇒ 连对 2，毕业。
2026-09-01 与 2026-09-03 两篇新题 P3 里自发命中共五处（三项并列、neither 两边、共用一个 to 的两个动词）。
2026-09-05 那次记的 ❌ 已于 2026-09-07 按 §3.1⑩ **改判 ✅**（母语句反证见当天行）；2026-09-07 复习 ✅ 两句都中。

**我错在哪**
她的：2026-08-17 记过一次 ❌（触发原话未存）；09-05 那次是**教练判错**，已改判 ✅。
找法：把并列的两边分别接回前面那个词念一遍 —— 都接得上才算同形。

**题面**
"下班后有时间做点别的，比如爱好，或者就是陪陪孩子。" ／ "蛋糕上面那些字是用糖果和饼干拼的。"

- 2026-08-09 ✅
- 2026-08-11 ✅
- 2026-08-17 ❌ 同日回潮 ｜同日原 #151 记 ✅ ⇒ 一对一错，保守记 ❌
- 2026-08-19 ✅ `like hobbies, or just being with your kid` ＋ `sweets and biscuits`（功能同形＋数齐，两面都中）
- 2026-08-20 ✅ `like hobbies or just being with your kids`（名词 vs 动名词，语法功能相同 ⇒ 同形成立，
  判据与 08-19 一致，没改口）＋ `sweets and biscuits`（数也齐）
  ★ 同句自发命中 🎓#162：`spelt out **in** sweets`（08-17 曾写成 spelt out OF）
- 2026-09-01 📝 新题 P3（bank:490）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）· **本篇三处**
  ① S3 三项全 -ing：`turning up on time, meeting your deadlines, and getting along with your colleagues`
  ② S5 neither 两边同形：`neither log in nor place orders`（都是光动词原形）
  ③ S6 两项同形：`doing your share and not causing problems for the team`
  ★ 一篇 98 词里三处并列全部同形，且最难的 S3 三项没打折。
- 2026-09-03 📝 新题 P3（bank:831）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）· **本篇两处**
  ① `like **how to pay**, **how to video call**, that kind of thing` —— 两项齐平（how to ＋ 原形）
  ② `to **keep up with** what's going on or **better understand** their grandchildren's interests`
     —— 两个动词共用前面那一个 to，语法功能相同
  ★ 长句里并列还能保持同形，是本篇结构上最稳的一处。
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· 句 1 并列两边**不同形**：
  hobbies（名词）／being with your kids（动名词短语）
  原句 `After work, you have some time to do other things like hobbies or just being with your kids.`
  最小改 `After work, you have some time to do other things like hobbies or just time with your kids.`
  ⚠️ **本条已于 2026-09-07 改判为 ✅**（§3.1⑩ 原行留痕）——
  改判理由：08-20 那一行白纸黑字锁死过判据「名词 vs 动名词，语法功能相同 ⇒ 同形成立，
  判据与 08-19 一致，没改口」，而 09-05 的原句与 08-20 判 ✅ 的原句几乎逐字相同 ⇒ 09-05 那次是假错。
  母语句反证：`After work you've got time for other things — hobbies, or just spending time with the kids.`
  完全自然：动名词短语本身是名词性成分，与 hobbies 并列时语法功能相同（同为 like 的宾语）。
  同日句 2 `These letters on the cake is written in sweets and biscuits.` —— 本条考点（数齐）
  sweets and biscuits **中**；`letters … is` 是主谓一致 ⇒ 形态类归 ⚪#10，⛔ 不落在本条头上。
  ⇒ 09-05 的回潮一并撤销，状态行改回 🎓（连对2 仍冻结在 2026-08-20）。
- 2026-09-07 ✅ 复习 · 在池第 4 组 · `After work, you can do something else, like hobbies, or just spending time with the kids.`
  ／ `The words on the cake are spelled out with sweets and biscuits.`
  —— 句 1 并列两边语法功能相同（都是 like 的宾语、都是名词性）；句 2 数齐 sweets and biscuits ＋ The words **are**
  ★ 与 08-19／08-20 判 ✅ 的那两次同形 ⇒ 本题连带触发 09-05 那次 ❌ 的改判（见该行行尾）
- 2026-09-19 ❌ 付息日 d 段重答 R12（P3 · 自由产出）· `tech giants know everything about you—where you live, your preferences, even guessing what you're craving today`
  最小改 `…where you live, your preferences, even what you're craving today`
  ❌ 破折号后三项都挂在 know 上：know where you live ✓ · know your preferences ✓ · know even guessing … ✗ ⇒ 第三项接不回 know ⇒ **回潮**
- 2026-09-20 ✅ 学习日 在池第 1 组 · `After work, you have time for other things — like hobbies, or just spending time with your kids.` ／ `The letters on top of cake are spelled out with sweets and biscuits.`
  —— 句1 hobbies（名词）与 spending time（动名词短语）同为 like 的宾语 ⇒ 语法功能相同（判据与 08-19／08-20／09-07 一致，没改口）；句2 sweets and biscuits 数齐
  ★ 同句 `on top of cake` 缺限定词 ⇒ 归 ⚪#56（形态类只记录，⛔ 不落在本条头上）；`spelled out with sweets` 自发命中 🎓#162
  ⚠️ diff-2：on top of the cake → on the cake（字写在蛋糕表面，on top of 是"摞在上面"）—— 删一个词，⛔ 不建号
- 2026-09-20 📝 学习日 新题 bank:1038（P3）· 自发命中留痕 · **本篇两处**（🎓 冻结，只留痕、不推进数字）
  ① 冒号后两项齐平：`the real-life feeling and a change of pace`（两个名词块）
  ② 末句三项齐平：`It looks cool, it's great for taking photos, and you just get to chill …`（三个完整分句）
- 2026-09-21 ✅ 学习日 在池第 1 组 [1] · `After working, you have time for other things — like hobbies, or spending time with your kids.` ／ `The letters on the cake is spelled out with sweets and biscuits.`
  —— 两面都中：句1 hobbies（名词）与 spending time with your kids（动名词短语）同为 like 的宾语 ⇒ 功能相同；句2 sweets and biscuits 两边同为复数 ⇒ 数齐。连对 1 → 2 ⇒ 🎓
  ★ 同句 `is spelled out` 主谓一致 ⇒ ⚪#10（形态类只记录，不影响本条判定）；`After working` ⇒ ⚠️ 不建号（她 09-07／09-20 都产出过 After work）
- 2026-09-22 📝 留痕（⛔ 不判回潮、状态行不动）· 新题 bank:1102（P3）· `understanding people, good reasoning ability, and being good at expressing yourself` 三项不同形（动名词／名词短语／动名词）
  ⇒ 判 ⚠️ 不判 ❌：母语句反证 `It comes down to three things: understanding people, good timing, and a bit of luck.` 混着摆在口语里成立；更好版把中间一项改成 reasoning well
- 2026-09-26 📝 重答 bank:778（R16）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）· `other things like hobbies, or spending time with your kid` —— 名词与动名词短语同为 like 的宾语，功能同形
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 备注 自测法：把两边分别接回前面那个词念一遍
- 备注 合并 2026-08-19：#151（并列两边可数性/单复数要齐）并入本条 —— 同一条规则的两个面，
  题面保留两句，一句测"功能相同"、一句测"数要齐"

### 100 · look for sth（≠ look up ＝ 查资料）
类型 词组 ｜ 旧号 B171f
状态 连对2 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-25 · 连对2 ＋ 她当场指定**（"不问了，直接毕业"）｜ 题型 整句

**问题是什么**
**look for sth**（找 ＝ **过程**）≠ **look up**（查资料）≠ **find**（找到 ＝ **结果**）。
判据：**find ＝ 找到（结果）／look for ＝ 找（过程）**。中文一个"找"字盖两件事，英语必须分开。
· 补一层（08-23）：**进行时 ＋ find** 只在"正在（一点点）发现"时成立（I'm finding it harder…）；
　"找工作／找房子／找钥匙"这种**过程**一律 look for。
同一格里的邻居（别串）：searching for ／ trying to find 都合法、也都完全绕开考点 ⇒ 题面正向点名 look。
判据一句话：说的是**过程** ⇒ look for；**结果** ⇒ find；**查资料** ⇒ look up。

**怎么发现的**
旧 B 表迁移（B171f，2026-08-18）；最早记录 2026-08-11 ❌。
2026-08-19 ❌ 复习 #18 句里 · "我找了半天" → 触发原话 `I found for hours`（用了 find，没调出 look for）。
2026-08-23 ❌ 付息日 a 段 · `he is finding a job near he place.`——08-21 刚答对，今天又掉回 find。
2026-08-24 ✅ ／ 2026-08-25 ✅ `he is looking for a job near his place.` ⇒ 连对 2 毕业 ＋ 她当场指定（"不问了，直接毕业"）。
2026-08-31 📝 自发命中留痕 · `I looked for it everywhere`（#18 那题没点名动词，她自己选了 look for、方向也对）。
2026-09-09 复检第 3 组 ✅ `look for a job`。

**我错在哪**
她的：`I found for hours`（08-19）／ `he is finding a job near he place.`（08-23）
正确：`I looked for it everywhere` ／ `he is **looking for** a job near his place.`
找法：说"找"之前先分一刀 —— 过程（look for）、结果（find）还是查资料（look up）？

**题面**
"我把钥匙弄丢了，在家里找了一上午也没找到。"（"找"用 **look** 说）
　　★ 一句里"找"（过程）和"找到"（结果）各一次 —— look for ／ find 的分工正是考点

- 2026-08-11 ❌
- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-19 ❌ 复习#18 句里 · "我找了半天" → `I found for hours`（用了 find，没调出 look for）
- 2026-08-21 ✅ 复习（08-20 泄题顺延，今天首出）· `he is looking for a job near his place.`——look for 一字不差，连错清零
- 2026-08-23 ❌ 付息日 a 段 · `he is finding a job near he place.` → is **looking for** a job
  ——**考点位置正是这里**：find ＝ 找到（结果）／look for ＝ 找（过程）。"正在找工作"是过程
  ⚠️ 08-21 刚答对（`he is looking for a job near his place.`），今天掉回 find ⇒ 连对 1→0
  ★ 判据补一层：**进行时 ＋ find** 只在"正在（一点点）发现"时成立（I'm finding it harder…）；
    "找工作／找房子／找钥匙"这种**过程**一律 look for
  ｜`he place` 漏了 s，按 §2.1 拼写不算错
- 2026-08-24 ✅ 复习第1组（题面当天加点名后首测）· `he is looking for a job near his place.`
  ——`looking for` 一字不差 ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
- 2026-08-25 ✅ 复习第1组 · `he is looking for a job near his place.`
  ——`looking for` 一字不差 ⇒ **连对 1 → 2 ⇒ 毕业**；她当场加了一句"不问了，直接毕业"
  ★ 教练自审留痕：想把 `near his place` 标 ⚠️ 换 `close to home`（中文"离家近"），
    造母语句推翻自己 —— `He's looking for a job near his place.` 母语者照说 ⇒ 档位不成立，未标
- 2026-08-31 📝 付息日 c 段 · **自发命中留痕**（🎓 状态行冻结，契约⑦）
  a 段第 1 组 [5]（#18 的题面"我找了半天也没找到"）· `I **looked for it** everywhere`
  ★ #18 的题面**没有点名**用哪个动词（第二译法自查里写明：所有合法译法都必须带宾语，
    考位在译法之间不变 ⇒ 不点名）⇒ 她自己选了 look for，且方向对（找东西 ＝ look for，
    不是查资料 ＝ look up）⇒ 自发命中本条的辨析。
- 2026-09-09 ✅ 复检 · 第 3 组 · `look for a job`
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  一句里"找"（过程）和"找到"（结果）各一次，点名 look —— for／find 的分工正是她掉过三次的地方；换成找钥匙场景（⛔ 不再用"找工作"）

### 101 · get by（应付得来）
类型 词组 ｜ 旧号 B171g
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **回潮 2026-09-05**（08-19 毕业 → 09-05 复检答"忘了"，撤销毕业、连对清零。★ 2026-09-07 补：这一判定 09-05 当天写进了 session 却漏了 `append`，回潮同步迟到两天） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
**问题是什么**
**get by** ＝ 应付得来、凑合过得去：`my English isn't great, but I **get by**.`
判据一句话：说"不算好，但够用／对付得过去" ⇒ get by（两个词，后面不挂宾语）。

**怎么发现的**
旧 B 表迁移（B171g，2026-08-18），原始触发原话未存；最早记录 2026-08-11 📖（连三天 📖 起家）。
2026-08-19 ✅ `my English isn't great, but i get by` ⇒ 毕业。
2026-09-05 ❌ 复检 a2 第 2 组 · 答"忘了"（§3.3「忘了/不会」也是 ❌）⇒ **回潮**。
2026-09-07 ✅ `get by`；2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。

**我错在哪**
她的：答"忘了"（2026-09-05 复检）　　正确：`My English isn't great, but I get by.`
找法：说"凑合／对付得来"时直接调 get by 这两个词。

**题面**
"我的西班牙语不算好，不过出去旅游日常够用。"（"够用"用 **get** 说）

- 2026-08-11 📖
- 2026-08-12 📖
- 2026-08-13 📖
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `my English isn't great, but i get by`（📖📖📖 起家，三次连对出池）
- 2026-09-05 ❌ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· 忘了（§3.3「忘了/不会」也是 ❌）
  最小改 `My English isn't great, but I get by.`
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `get by`（09-05 答"忘了"，这次调出来了）
- 2026-09-09 ⚡ 自评免测 · 在池第 1 组（她原话："这 10 个题直接过吧，算对"）
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 get，by 留给她（她答"忘了"掉过一次）；换成西班牙语旅游场景

### 102 · without ＝ with no，不能叠（without no ❌）
类型 语法 ｜ 旧号 B173
状态 连对2 连错0 上次2026-09-13 ｜ 旧账 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**without ＝ with no，不能叠**（⛔ without no）：`I can't go a day **without** looking at my phone.`
同一格里的邻居（别串）：⚠️ watching my phone → looking at／checking my phone（顺带更好版，⛔ 不落号）。
判据一句话：without 自己已经带着否定 ⇒ 后面不许再冒第二个否定词。

**怎么发现的**
旧 B 表迁移（B173，2026-08-18，旧账），原始触发原话未存；最早记录 2026-08-10 ◎、2026-08-11 ❌。
2026-08-12 ✅ ／ 2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-09-05 复检第 1 组 ✅ `I can't go a day without wacthing my phone.`——without ⛔ 未叠否定。

**我错在哪**
她的：2026-08-11 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：写完 without 回头扫后半句 —— 里面还有没有 no／not？有就删掉一个。

**题面**
"我没法一天不看手机。"（"不看"那层用 **without** 说）

- 2026-08-10 ◎
- 2026-08-11 ❌
- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `I can't go a day without wacthing my phone.` —— without ⛔ 未叠否定
  ｜ ⚠️ 顺带：watching my phone → looking at／checking my phone（不落号，⭐ 再犯一次就建号，见 session 顺带②）
  ｜ wacthing → watching（拼写，不算错）
- 2026-09-13 📝 题面整改：补（"不看"那层用 **without** 说）· 复检组发题前审核（§6.5 第 7 项）
  `I can't spend a day not looking at my phone` 合法但整个绕开 without，测不到"without 不叠否定"这一格 ⇒ 点名 without（考点是叠不叠 no，不是 without 本身）
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组 · `I can't go a day without my phone.`——without 后面没叠 no

### 103 · 不定式后置修饰，介词默认留在末尾（a box to put these things IN）
类型 结构 ｜ 旧号 B175
状态 连对1 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-23 · 她指定**（"这条毕业"）｜ 旧账 ｜ 题型 整句

**问题是什么**
**不定式后置修饰名词时，介词默认留在末尾**：`a box to put these things **in**`。
同族整块记：someone to talk **to** ／ a chair to sit **on** ／ something to work **towards** ／
something to look forward **to** ／ a pen to write **with**。
判据一句话：**把名词放回从句里念一遍**（"I move forward ___ it" 念不通 ⇒ 尾巴上缺一个介词）——即 methods M34 的诊断动作。
⚠️ 本条**不是形态类**（类型 ＝ 结构）⇒ "形态类在中译英里只记号"那条例外不适用，掉了照常回潮。

**怎么发现的**
旧 B 表迁移（B175，2026-08-18，旧账），原始触发原话未存；最早记录 2026-08-09 ✅；08-10 ❌；08-16 ◎ 题面没逼出 → 改题面。
2026-08-19 ✅ `I need a box to put the thing in`——介词留末尾对。
2026-08-23 ❌ **回潮** · 付息日 a 段复习 #264 句里 · `rewards give kids something to move forward.`；
**同一场内**翻正 ✅ `I need a box to put these things in.` ⇒ 她当场指定毕业（"这条毕业"）。
2026-09-05 复检第 4 组 ✅ `a box to put these things **in**.`

**我错在哪**
她的：`rewards give kids something to move forward.`（2026-08-23）
正确：`something to work **towards**`（或 something to move forward **with**）
找法：把名词放回从句里念一遍 —— "I move forward ___ it" 念不通，就说明尾巴上缺一个介词。

**题面**
"我想找个盒子，能把这一堆充电线都放进去。"（用 **a box to** 说）

- 2026-08-09 ✅
- 2026-08-10 ❌
- 2026-08-11 📖
- 2026-08-12 ✅
- 2026-08-16 ◎ 题面没逼出（并列小句也合法）→ 改题面
- 2026-08-17 ✅
- 2026-08-19 ✅ `I need a box to put the thing in`——介词留末尾对（同句 the thing 的错归 #150）
- 2026-08-23 ❌ **回潮** · 付息日 a 段 · 复习#264 句里 · `rewards give kids something to move forward.`
  → something to work **towards**（或 something to move forward **with**）
  —— **不定式后置修饰名词时，介词必须留在末尾**：move forward 是不及物的，尾巴上缺一个介词
  ★ 同族整块记：a box to put these things **in** ／ someone to talk **to** ／ a chair to sit **on**
    ／ something to work **towards** ／ something to look forward **to** ／ a pen to write **with**
  ★ 判据一句话：**把名词放回从句里念一遍**（"I move forward ___ it" 念不通 ⇒ 缺介词）
    —— 这就是 methods M34 的诊断动作
  ⚠️ 本条**不是形态类**（类型 ＝ 结构）⇒ 08-21 那条"形态类在中译英里只记号"的例外**不适用**，照常回潮
  ⚠️（原写"顺延到明天"—— 她 08-23 当天作废了"讲评泄题扫描"这条规则，本条当天就重测了）

- 2026-08-23 ✅ 付息日 a 段（同一场内翻正）· `I need a box to put these things in.`
  ——末尾的 **in** 留住了；上午那处 `something to move forward` 的回潮，下午同一场就修回来了
  ⇒ **她当场指定毕业**（"这条毕业"）
- 2026-09-05 ✅ 复检组 · 第 4 组 · `a box to put these things **in**.` —— 不定式后置修饰，介词留在末尾
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组（打包）· `a box to put these things in`——介词留在末尾
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句（类型 结构 ⛔ 不许标词组）
  点名 a box to，句尾那个 in 留给她；换成充电线场景

### 104 · bury yourself in sth（比喻义只配 in，不配 into）
类型 搭配 ｜ 旧号 B181 ｜ ⭐ 她自产
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **回潮 2026-09-05**（08-20 毕业 → 09-05 复检写成 bury **into**，正是本条守的那个错，撤销毕业、连对清零。★ 2026-09-07 补：这一判定 09-05 当天写进了 session 却漏了 `append`，回潮同步迟到两天） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
**问题是什么**
**bury yourself in sth**：比喻义**只配 in、不配 into** —— `don't bury yourself **in** grammar books and word lists`。
判据：**in 标状态、into 标轨迹**；"埋在书里"说的是状态 ⇒ in。
判据一句话：比喻义的 bury 后面永远是 in。

**怎么发现的**
旧 B 表迁移（B181，2026-08-18，⭐ 她自产），原始触发原话未存；最早记录 2026-08-10 ✅；08-13 ❌；
08-15 ❌ → 当天档位更正（INTO 从 ❌真错降为 ⚠️非标准搭配）。
2026-08-19 ✅ 点名 · `don't bury youself in grammar books and word lists` ⇒ 2026-08-20 毕业。
2026-09-05 ❌ 复检 · `bury into`——正是本条守的那个错 ⇒ **回潮**。
2026-09-07 ✅ `bury in`；2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。
★ 尾部备注记着：教练曾连续两天判 ❌ 却没给理由 ⇒ 她只能背不能学。

**我错在哪**
她的：`bury into`（2026-09-05 复检）　　正确：`Don't bury yourself **in** grammar books.`
找法：写完 bury 就问一句 —— 说的是"埋在里面那个状态"吗？是就用 in。

**题面**
"考试前那一周，他整个人都扎进复习资料里了。"（"扎进"用 **bury** 说）

- 2026-08-10 ✅
- 2026-08-13 ❌
- 2026-08-15 ❌ → 当天档位更正：INTO 从 ❌真错 降为 ⚠️非标准搭配
- 2026-08-16 ✅
- 2026-08-19 ✅ 点名 · `don't bury youself in grammar books and word lists`
- 2026-09-05 ❌ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· bury into —— 正是本条守的那个错
  原句 `bury into`
  最小改 `Don't bury yourself in grammar books.`
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `bury in` —— 考点＝比喻义只配 in、不配 into，她给的正是 in
  （09-05 写成 bury into）。完整形 bury yourself in sth，她给的是裸块，考点位置一字不差 ⇒ ✅
- 2026-09-09 ⚡ 自评免测 · 在池第 1 组（她原话："这 10 个题直接过吧，算对"）
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 bury，in／into 留给她（她掉过的就是 into）；换成考前复习场景
- 备注 教练连续两天判 ❌ 却没给理由 ⇒ 她只能背不能学；in 标状态、into 标轨迹

### 105 · "兼顾未来和现在"三说法（keep one eye on the future…）
类型 词组 ｜ 旧号 B186
状态 连对2 连错0 上次2026-10-02 ｜ 旧账 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
"兼顾未来和现在"的整句块：**keep one eye on the future and one on the present**。
判据一句话：这是一个**整句块**（keep one eye on X and one on Y），整块调，⛔ 不拆成两句讲。
★ 与 🎓#240（keep an eye ON sth ＝ 留意）的分工（2026-08-19 判重结论）：**不合并** ——
　本条要的是"兼顾未来和当下"那个整句块，目标形式不同；两条题面互不撞车，各出各的。

**怎么发现的**
旧 B 表迁移（B186，2026-08-18，旧账），原始触发原话未存；最早记录 2026-08-10 ❌；08-15 ❌ ／ 08-16 ❌。
2026-08-17 ✅（教练当天用表里没写的标准判过她一次，已撤销）。
2026-08-19 ✅ `Keep one eye on the futher, and one on the present.`（整句块调出来了；futher 是打字滑）⇒ 2026-08-20 毕业。
2026-09-05 复检 ✅；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：08-10／08-15／08-16 三次 ❌（触发原话未存，旧 B 表迁移）。
找法：说"既看未来又看当下"时整块调 keep one eye on … and one on …。

**题面**
"存钱这件事，得兼顾以后和眼下。"（"兼顾"用 **one eye** 说）

- 2026-08-10 ❌
- 2026-08-11 ✅
- 2026-08-15 ❌
- 2026-08-16 ❌
- 2026-08-17 ✅（教练当天用表里没写的标准判过她一次，已撤销）
- 2026-08-19 ✅ `Keep one eye on the futher, and one on the present.`（整句块调出来了；futher 是打字滑）
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· keep one eye on the future and one on the present
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-09-12 📝 题面整改：「得同时看着未来和当下。」→「同时看着未来和当下」—— 原句无主语却带句号（§6.5 第 6 项 ✗ 例），缩成块、回标词组 · 全档题面 review
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"用一个带 eye 的说法"，正向点名 one eye，整块怎么接留给她；换成存钱场景
- 2026-10-02 ✅ 复检 · 学习日 复检第 4 组 [10] · `When saving money, you've got to have one eye on the future and one eye on the present.` —— 整句块一口气调出来（have／keep 都是这个块的合法动词）

### 106 · kind of / sort of / type of ＋ 单数名词，不带冠词
类型 语法 ｜ 旧号 B187
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**kind of ／ sort of ／ type of ＋ 单数名词，不带冠词**：
`what **kind of car** do you drive` ／ `this **kind of thing**`（✗ this kind of things ／ ✗ this kind of a thing）。
同一格里的邻居（别串）：`What car do you drive?` 也合法，但绕开这个块 ⇒ 题面点名"用 kind 说"。
判据一句话：kind／sort／type of 后面那个名词**既不加 -s 也不加 a**。

**怎么发现的**
旧 B 表迁移（B187，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-19 ✅ `what kind of car do you drive`（没走 What car 那条合法绕开路）⇒ 毕业。
2026-08-27 ✅ 自发命中 · `older folks are really obsessed with **this kind of thing**.`——两格都对。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写完 kind of 看后面那个名词 —— 尾巴别加 -s，前面别加 a。

**题面**
"什么车"（用 **kind** 说）

- 2026-08-11 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `what kind of car do you drive`（没走 What car 那条合法绕开路）
- 2026-08-27 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 付息日 b 段 #289 句里 ·
  `older folks are really obsessed with **this kind of thing**.`
  ——kind of ＋ **单数名词**、**不带冠词**，两格都对（✗ this kind of things ／ ✗ this kind of a thing）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 7 组（打包串，她原话："除了 3）忘了，其他直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；kind of ＋ 单数名词她一直对、08-27 自发用对（类型 语法却标词组的旧题面也一并作废）

### 107 · jammed / gridlocked（车堵到一动不动）
类型 词汇 ｜ 旧号 B191a
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 退池 ｜ 题型 词组

**问题是什么**
**jammed ／ gridlocked** ＝ 车堵到一动不动（一个形容词就够）。
同一格里的邻居（别串）：#108 的 **packed** 说的是**人多**（a packed train）—— 一堵车一挤人，⛔ 别串。
判据一句话：堵的是**车** ⇒ jammed／gridlocked；挤的是**人** ⇒ packed。

**怎么发现的**
旧 B 表迁移（B191a，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-12 ✅（📊 记 B191a／B191b 分号后）／ 2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-09-07 复检第 5 组（打包）✅ `jammed`（形容词槽位，一个词到位）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"堵死了"时只给一个形容词 —— jammed／gridlocked，⛔ 别去造从句。

**题面**
"堵死了，一动不动"（一个形容词 · ⛔ 不许用 stuck／blocked）

- 2026-08-11 ✅
- 2026-08-12 ✅（📊 记 B191a／B191b 分号后）
- 2026-08-16 ✅
- 2026-09-07 ✅ 复检 · 第 5 组（打包）· `jammed`（形容词槽位，一个词到位）
- 2026-09-19 📝 题面整改：补（⛔ 不许用 stuck／blocked）· 复检组发题前审核（§6.5 第 7 项）
  `The traffic was stuck.`／`The road was blocked.` 都是一个形容词、都合法，绕开 jammed／gridlocked ⇒ 补排除项
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ① 同级说法
  "堵死了"说 stuck in traffic／bumper to bumper 都完全地道，jammed 只是其中一个 ⇒ 不点名逼不出、点名等于给答案；历史零 ❌

### 108 · packed（人多：a packed train）
类型 词汇 ｜ 旧号 B191b
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**packed** ＝ 人多、挤（a packed train ／ `The subway is packed`）。
同一格里的邻居（别串）：#107 的 jammed／gridlocked 说的是**车堵**—— 一挤人一堵车，⛔ 别串；题面用首字母 **p** 框死。
判据一句话：挤的是**人** ⇒ packed。

**怎么发现的**
旧 B 表迁移（B191b，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅。
2026-08-19 ✅ `the subway is packed.` ⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ `The subway is packed`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"人挤人"时只给一个形容词 packed。

**题面**
"地铁里人挤人"（**一个形容词**，**p** 打头）

- 2026-08-13 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `the subway is packed.`
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `The subway is packed`
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ① 同级说法
  "人挤人"说 crowded／jam-packed 都完全地道，packed 只是其中一个（旧题面靠首字母 p 硬框）⇒ 中译英里产不出 ❌；历史零 ❌

### 109 · enough X to go round（够分）
类型 词组 ｜ 旧号 B192
状态 连对2 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**enough X to go round** ＝ 够分：`There aren't enough jobs **to go around**.`（go round／go around 两拼都对）
同一格里的邻居（别串）：`There aren't enough jobs.` 完全合法，但整块 to go round 不会出现
⇒ 2026-09-05 题面点名"用 go 起头的那个块"，⛔ 未把 to go round 直接给出来。
判据一句话：中文"不够**分**"里的那个"分"就是 **to go round**，少了它只剩"不够"。

**怎么发现的**
旧 B 表迁移（B192，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ❌、2026-08-12 ❌。
2026-08-13 ✅ ／ 2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-09-05 复检第 1 组（打包）✅ `jobs are not enough to go around`。

**我错在哪**
她的：08-11 与 08-12 各记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：中文出现"不够分／不够大家用"时，把 **to go round** 接到 enough X 后面。

**题面**
**点名**："岗位不够分。"（"不够分"那个"分"用 **go** 那个词起头的块说）

- 2026-08-11 ❌
- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-16 ✅
- 2026-09-05 📝 题面整改 · 复检组第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面 "岗位不够分。" 的默认译法 `There aren't enough jobs.` 完全合法，
  但整块 enough X **to go round** 不会出现 ⇒ 考位被绕开。
  ⇒ 点名到"用 go 起头的那个块"，⛔ 未把 to go round 直接给出来。
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· `jobs are not enough to go around` 块在（go round／go around 两拼都对）
  ｜ ⚠️ 顺带：默认句型是 There aren't enough jobs to go around.（不落号）
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组 · `there aren't enough jobs to go around`

### 110 · "没有 X" 的三种说法（口语默认走 I didn't have any…, so…）
类型 结构 ｜ 旧号 B193
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 退池 ｜ 题型 整句

**问题是什么**
**"没有 X" 的三种说法，口语默认走 `I didn't have any…, so…`**：
`I didn't have a charger, so I used my colleague's`。
同一格里的邻居（别串）：⛔ without 起头（题面已排除）—— 那是偏书面的走法。
判据一句话："没有 X"这半句在口语里落成一个**完整的句子**（I didn't have …），后面用 so 接。

**怎么发现的**
旧 B 表迁移（B193，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅、2026-08-16 ❌。
2026-08-19 ✅ `I didn't have a charge(r), so I used my colleague's` ⇒ 2026-08-20 毕业。
2026-09-05 复检 ✅ 与本条写死的口语默认走法逐字一致；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：2026-08-16 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法："没有 X"先落成一个完整句子 I didn't have …，⛔ 别起 without。

**题面**
"没有充电器，我就用了同事的。"（"没有充电器"那半句用一个**完整的句子**说，⛔ 不用 without 起头）

- 2026-08-12 ✅
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ✅ `I didn't have a charge(r), so I used my colleague's`（口语默认走 I didn't have…, so…）
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· I didn't have a charger, so I used my colleague's
  —— 与本条写死的口语默认走法逐字一致
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-09-29 📝 退池 · ① 同级说法
  `Without a charger, I used my colleague's.` 本身完全成立，"I didn't have …, so …"只是口语默认走法的偏好 ⇒ 中译英里产不出 ❌（08-16 那次 ❌ 原话未存、无从确认是真错）

### 113 · "都要/总是"那一层（always end up -ing／have to／it always takes）
类型 结构 ｜ 旧号 B197
状态 连对2 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 整句

**问题是什么**
**"都要／总是"那一层必须显式说出来**：always end up -ing ／ have to ／ it always takes ——
`I **always end up** queuing for half an hour every time I go.`
同一格里的邻居（别串）：`I queued for half an hour every time I went there` 完全合法，
但"都要"那层没落地 ⇒ 2026-08-19 题面当天加点名。
判据一句话：中文里的"都要／总是"是一整层意思，英文必须有一个块扛住它。

**怎么发现的**
旧 B 表迁移（B197，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ❌、2026-08-16 ❌。
2026-08-19 ◎ 她答 `I queued for half an hour every time I went there` 完全合法，但"都要"那层没落地 ⇒ 当天加点名。
2026-08-20 ✅ 复习（点名题面首测）· `I always ended up queuing for half an hour every time I went` ⇒ 连对 2，毕业。
2026-09-05 复检 ✅ `I always end up queuing`。

**我错在哪**
她的：`I queued for half an hour every time I went there`（08-19，判 ◎ ＝ 教练没点名，⛔ 不记错）
正确：`I always end up queuing for half an hour every time I go.`
找法：中文出现"都要／总是"时，先找一个块把它扛住（always end up -ing／have to），⛔ 别指望时态替你说。

**题面**
**点名**："我每次去都要排半小时队。"（"都要"那层用 always end up／have to 说出来）

- 2026-08-11 ❌
- 2026-08-12 ✅
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ◎ 她答 `I queued for half an hour every time I went there` 完全合法，
  但"都要"那层没落地 ⇒ 教练第②类自查又漏，当天加点名
- 2026-08-20 ✅ 复习（点名题面首测）· `I always ended up queuing for half an hour every time I went`
  ——always end up -ing 整块出来了 ⇒ 连对2 毕业（时态整句一致，不扣）
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· I always end up queuing —— "都要"那一层显式说出来了
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组 · `I always end up to queuing for half an hour every time I go.`——"都要"那层（always end up）落地了
  ｜同句 `end up to queuing` ❌ 不归本条 ⇒ 新建 #338（end up ＋ -ing）

### 114 · It's less about X AND more about Y（配对词是 and，不是 but）
类型 词组 ｜ 旧号 B198 ｜ ⭐ 她自产
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

**问题是什么**
**It's less about X AND more about Y** —— 配对词是 **and**，⛔ 不是 but：
`it is less about the machine itself **and** more about the time spent with kids`。
同一格里的邻居（别串）：not … but … 完全合法（08-17 她答的就是它），但绕开这个块 ⇒ 题面正向点名 less about。
判据一句话：less about … 后面接的是 **and** more about …，两半靠 and 连。

**怎么发现的**
旧 B 表迁移（B198，2026-08-18，⭐ 她自产），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-17 ◎ 她答 not…but… 完全合法 → 改点名。
2026-08-19 ✅ 点名 · `it is less about the machine itself and more about the time spent with kids` ⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ 配对词是 and、⛔ 不是 but。
★ 尾部备注记着：这个块她在自由产出里已自发用对四次（08-11／13／15／16 四篇 P2 结尾）。

**我错在哪**
她的：本条没有掉过（08-17 那次是 ◎ ＝ 教练没点名），触发原话未存。
找法：说完 less about X，下一个词直接给 **and**，再接 more about Y。

**题面**
"学乐器重点不在天赋，而在每天练多久。"（用 **It's less about** 起头）

- 2026-08-12 ✅
- 2026-08-15 ✅
- 2026-08-17 ◎ 她答 not…but… 完全合法 → 改点名
- 2026-08-19 ✅ 点名 · `it is less about the machine itself and more about the time spent with kids`
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `It's less about the machine itself **and** more about the time you spend with your kids.`
  配对词是 and，⛔ 不是 but（⭐ 本条是她自产的块）
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  点名 It's less about，后半 and more about 的配对词留给她（考点就是 and ⛔ but）；换成学乐器场景
- 备注 这个块她在自由产出里已自发用对四次（08-11/13/15/16 四篇 P2 结尾）

### 115 · a couple of ＝ 两个（精确）；"几个"用 a few
类型 词汇 ｜ 旧号 B199
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19**（08-20 的回潮已撤销，见下）｜ 退池 ｜ 题型 词组

**问题是什么**
**a couple of ＝ 两个（精确）**；"几个"要用 **a few**：`there were **a few** reasons I didn't go.`
同一格里的邻居（别串）：**few（不带 a）＝ 几乎没有**（否定色彩）／**a few ＝ 少数几个**（肯定）——
2026-08-20 教练一度把 `only few people are really interested` 判错，她说"only few 没错呀，特意说的"后撤销：
她要的正是"几乎没人真感兴趣"，改成 a few 反而把否定色彩改没了。
⚠️ 只保留一条提醒：口语里 very few／hardly anyone 更常听到，only few 偏书面。
判据一句话：说"两个" ⇒ a couple of；说"几个" ⇒ a few；说"几乎没有" ⇒ few（不带 a）。

**怎么发现的**
旧 B 表迁移（B199，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `there were a few reasons I didn't go.` ⇒ 毕业。
2026-08-20 ⛔ 教练误判并让本条回潮，**她当场否掉、教练撤销**（理由见当天行）⇒ 本次不计档位，恢复 🎓。
2026-09-10 复检第 4 组（打包）✅ `a few reasons`。

**我错在哪**
她的：本条历史里没有掉过；08-20 那次是**教练判错**（她的 only few 是对的），已撤销。触发原话未存。
找法：中文"几个"先落 a few；要表达"几乎没有"才把那个 a 去掉。

**题面**
"几个原因"（⛔ 不许用 several／some）

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-19 ✅ `there were a few reasons I didn't go.`（a few ＝ 几个，不是 a couple of）
- 2026-08-20 ⛔ 教练一度把 `only few people are really interested` 判 ❌ 并让本条回潮，
  **她说"only few 没错呀，特意说的"后撤销**。
  撤销理由（教练自己的判据反过来打自己）：**few（不带 a）＝ 几乎没有**（否定色彩）／
  **a few ＝ 少数几个**（肯定）—— 她要表达的正是"几乎没人真感兴趣"，**few 才是对的那个**，
  改成 a few 反而把否定色彩改没了。且 `Only few studies have looked at this.` 这类用法成立。
  ⇒ 本次不计档位，恢复 🎓。仅保留 ⚠️：口语里 very few／hardly anyone 更常听到，only few 偏书面
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `a few reasons`
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌（08-20 那次是教练误判、已撤销）；a few／a couple of 她一直用对

### 116 · colourful X（不是 color X）
类型 词汇 ｜ 旧号 B200
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**colourful X**（形容词是 **-ful** 形式）—— ⛔ 不是 color X、⛔ 不是 -ed 形式：
`he bought his son a **colorful** dinosaur.`
同一格里的邻居（别串）：color／colour 只是美英拼写变体（§2.1 不算错）。
判据一句话："彩色的"是形容词 colourful；名词 color 不能直接拿去修饰名词。

**怎么发现的**
旧 B 表迁移（B200，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `he bought his son a colorful dinosaur.` ⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ `colorful`——-ful 形式对。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：要拿 color 去修饰名词时，先给它补上 -ful。

**题面**
"彩色的"（形容词，⛔ 不许用 -ed 形式）

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-19 ✅ `he bought his son a colorful dinosaur.`
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `colorful` —— -ful 形式对；color／colour 只是美英拼写变体（§2.1 不算错）
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；colorful 她一直用对

### 117 · watch（盯着看一个过程）vs see（看到结果/一瞬间）
类型 词汇 ｜ 旧号 B201
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**watch（盯着看一个过程）vs see（看到结果／一瞬间）**；watch ＋ 宾语 ＋ **动词原形**：
`watch the pictures on the screen **turn** into real objects.`
同一格里的邻居（别串）：watch 属 🎓#16 那个四件套（have／make／let／watch／see ＋ 光杆原形）。
判据一句话：看的是一个**过程** ⇒ watch，后面那个动词用原形。

**怎么发现的**
旧 B 表迁移（B201，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `he can watch pictures on the screen turn into real objects.`（watch ＋ 宾语 ＋ 原形）⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ 同形。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：看的是过程就用 watch，后面那个动词一律光杆原形。

**题面**
"看着屏幕上的图变成实物"

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-19 ✅ `he can watch pictures on the screen turn into real objects.`（watch ＋ 宾语 ＋ 原形）
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `watch the pictures on the screen turn into real objects.` —— watch ＋ 宾语 ＋ 动词原形
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；watch ＋ 宾语 ＋ 原形这一格已由 🎓#16 的新题面（"看着他收完"用 watch）去测

### 118 · 只有…才（ONLY ＋ 动词／It's only … that/when）
类型 结构 ｜ 旧号 B203
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **回潮 2026-09-05**（08-20 她指定毕业 → 09-05 复检 only 那一层整个没出来，★ 与 08-19 掉的那次逐字相同，撤销毕业、连对清零。★ 2026-09-07 补：这一判定 09-05 当天写进了 session 却漏了 `append`，回潮同步迟到两天） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
**问题是什么**
**"只有…才"那一层必须显式说出来**，两个落点：① **only ＋ 动词** ② **It's only … that／when …**
`you can **only** feel that energy when you are there.`
判据一句话：中文里有"只有…才"，英文就得有一个 only（或 It's only … that），⛔ 不能靠 when 从句顶替。
★ 与 🎓#38（feel the energy）的分工：两条题面原来几乎是同一句、考点却不同 ——
　#38 ＝ feel the energy 这个块，本条 ＝ "只有…才"那一层；她每次答中一条、另一条就记不上，
　**这就是本条一直毕不了业的真原因**；2026-08-19 已把 #38 的题面换掉，两条从此互斥。

**怎么发现的**
旧 B 表迁移（B203，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ❌。
2026-08-19 ❌ `You can feel that energy when you are there`——**only 那一层整个没出来**。
2026-08-20 ✅ `you can only feel that energy if you are there` ⇒ 她当场指定毕业。
2026-09-05 ❌ 复检 · 与 08-19 掉的那次**逐字相同** ⇒ **回潮**。
2026-09-07 ✅ ／ 2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。

**我错在哪**
她的：`You can feel that energy when you are there.`（08-19 与 09-05 两次逐字相同）
正确：`You can **only** feel that energy when you are there.`
找法：中文出现"只有…才"时，先把 only 放到主句动词前面，再往下说。

**题面**
"只有到了现场，你才有那种感觉。"（"只有…才"那层要显式说出来）

- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-16 ✅
- 2026-08-19 ❌ `You can feel that energy when you are there`——**only 那一层整个没出来**
- 2026-08-20 ✅ 复习 · `you can only feel that energy if you are there`——only ＋ 动词那一层出来了
  （if → when 只是 ⚠️ 更好，不影响考点）⇒ 她当场指定毕业
- 2026-09-05 ❌ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· **only 那一层整个没出来**
  —— ★ 与 2026-08-19 掉的那次**逐字相同**
  原句 `You can feel that energy when you are there.`
  最小改 `You can only feel that energy when you are there.`
- 2026-09-07 ✅ 复习 · 在池第 4 组 · `you can only feel that energy when you are there.`
  —— only ＋ 动词那一层显式说出来了，与 08-20 判 ✅ 的那次同形；⛔ 没落回 08-19／09-05 的"整层丢失"
- 2026-09-09 ⚡ 自评免测 · 在池第 1 组（她原话："这 10 个题直接过吧，算对"）
- 2026-09-15 📝 题面整改 · 复检第 3 组发题前审核（§6.5 第 6 项：中文无主语）
  旧："只有到现场才有那种感觉。"
  新："只有到了现场，你才有那种感觉。"（"只有…才"那层要显式说出来）
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 备注 2026-08-19 她问"这条怎么还没毕业，考了十次了吧" ⇒ 查记录只有 **3 次**（08-12 ❌ 08-13 ✅ 08-16 ✅），
  真正的原因是**题面与 #38 撞车**（两条题面几乎同一句、考点却不同）：她每次答中一条，另一条就记不上
  ⇒ 08-19 已把 #38 的题面换掉，两条从此互斥
- 备注 两个落点：① only ＋ 动词　② It's only … that/when …

### 119 · when（一定会发生/每次都这样）vs if（不确定）
类型 语法 ｜ 旧号 B204
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 整句

**问题是什么**
**when（一定会发生／每次都这样）vs if（不确定）**：
`everyone laughs **every time** he tells that joke; **if** he comes tomorrow, I'll take him.`
同一格里的邻居（别串）：every time 与 when 同族（都表示"一定会／每次"）。
判据一句话：这件事**一定会发生** ⇒ when／every time；**说不准** ⇒ if。

**怎么发现的**
旧 B 表迁移（B204，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `everyone laughs every time he tells a joke. if he comes tomorrow, I will bring him.`（两边都对）⇒ 毕业。
2026-09-10 复检第 4 组 ✅ 两侧分工对。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写连词前先问一句 —— 这件事一定会发生吗？会 ⇒ when／every time；不一定 ⇒ if。

**题面**
"每次他讲这个笑话大家都笑；如果他明天来，我就带他去。"

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-19 ✅ `everyone laughs every time he tells a joke. if he comes tomorrow, I will bring him.`
  （every time ＋ 现在时 ／ if ＋ 现在时，两边都对；bring/take 因题面没写去哪儿，不判）
- 2026-09-10 ✅ 复检 · 第 4 组 · `everyone laughs every time he tells that joke; if he comes tomorrow, I'll take him.`
  前半 every time（＝ 一定会发生，与 when 同族）· 后半 if（不确定）⇒ 两侧分工对
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；when／every time ／ if 的分工她一直对

### 120 · 治"句子太单薄"：加一个具体的东西（时间/距离/数字/结果），不是换大词
类型 结构 ｜ 旧号 B205
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

**问题是什么**
治"句子太单薄"的动作 ＝ **加一个具体的东西**（时间／距离／数字／结果），⛔ 不是换大词：
`it just takes **ten minutes**`（09-05 复检给的是"只要 20 分钟"）。
判据一句话：句子觉得空 ⇒ 补一个**能抓的量**，而不是把词换难。

**怎么发现的**
旧 B 表迁移（B205，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ❌。
2026-08-19 ✅ `it just takes ten minutes`——加了一个具体的量，正是本条要的动作 ⇒ 连对 3 出池
（她当天问"考了好多次了" ⇒ 查记录其实只有 3 次）。
2026-09-05 复检 ✅ 带上了具体的量；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：2026-08-12 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：一句说完觉得空，就补一个具体的数 —— 几分钟、几公里、几次、结果怎样。

**题面**
"我一般不点外卖，自己做。"（这句要**加一个具体的**：时间／数字／距离／结果，任选一个）

- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-16 ✅
- 2026-08-19 ✅ `it just takes ten minutes`——加了一个具体的量，正是本条要的动作
  （同句的否定辖域错归 #96 回潮；她问"考了好多次了" ⇒ 记录是 3 次，今天第 3 次连对出池）
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· 带上了具体的（只要 20 分钟）
  —— 本条的考位就是"给一个能抓的量"
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）

### 121 · queue 是可数名词（in A queue／queue for half an hour）
类型 语法 ｜ 旧号 B206
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**queue 是可数名词**（in **a** queue）；当动词用时后面直接接时长：`I queued **for half an hour**.`
判据一句话：名词形要带冠词 a，动词形后面直接跟 for ＋ 时长。

**怎么发现的**
旧 B 表迁移（B206，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `I queued for half an hour.` ⇒ 毕业。
2026-09-10 复检第 4 组 ✅ `queue for half an hour`——queue 当动词、后面直接接时长。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：用 queue 的名词形就补上 a（in a queue）；用动词形就直接接 for ＋ 时长。

**题面**
"排了半小时队"（用 queue 那个词说）

- 2026-08-12 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `I queued for half an hour.`
- 2026-09-10 ✅ 复检 · 第 4 组 · `queue for half an hour` —— queue 当动词、后面直接接时长
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；旧题面"排了半小时队（用 queue 说）"她答 queued for half an hour，根本碰不到 a queue 这个考点

### 122 · 肯定·随便哪个 → any-（Anything's fine.）
类型 语法 ｜ 旧号 B207a
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**肯定句里的"随便哪个"用 any-**：`Anything's fine.` ／ `anything is fine. it's up to you.`
同一格里的邻居（别串）：whatever 与 `I don't mind` 在口语里同样地道、同样合法，但都完全绕开 any-
⇒ 题面把两个都排除掉（第二条是 09-07 补的），真考点一个字都没泄露。
判据一句话：肯定句说"随便哪个" ⇒ any- 那一族（anything／anywhere／anyone）。

**怎么发现的**
旧 B 表迁移（B207a，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ❌、2026-08-13 ❌。
2026-08-19 ✅ `anything is fine. it's up to you.` ⇒ 毕业。
2026-09-05 复检 ✅；2026-09-07 复检 ✅ `anything is fine`（⛔ 没落进 whatever／I don't mind）。

**我错在哪**
她的：08-12 与 08-13 各记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：说"什么都行"时先落 anything，⛔ 别顺口滑到 whatever／I don't mind。

**题面**
"什么都行"（⛔ 不许用 whatever · ⛔ 不许用 I don't mind）

- 2026-08-12 ❌
- 2026-08-13 ❌
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `anything is fine. it's up to you.`
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· anything is fine（any- 那一族，⛔ 没用 whatever）
- 2026-09-07 📝 题面补一条排除「⛔ 不许用 I don't mind」：原题面只排除了 whatever，而 "I don't mind"
  是「什么都行」在口语里同样地道的译法、且完全绕开 any- ⇒ 考点测不到（§6.5 第 7 项）。
  排除它之后 any- 这个真考点一个字都没泄露。
- 2026-09-07 ✅ 复检 · 第 3 组 · `anything is fine`（肯定句里用 any-，⛔ 没落进 whatever／I don't mind）
- 2026-09-29 📝 退池 · ③ 题面收不拢
  "什么都行"说 whatever／I don't mind 同样地道（条目自己写着），不点名逼不出 anything、点了就是给答案；08-12／08-13 两次 ❌ 原话未存，此后五次全对

### 123 · 肯定·全部 → every-（Everything's gone up.）
类型 语法 ｜ 旧号 B207b
状态 连对2 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 退池 ｜ 题型 词组

**问题是什么**
**肯定句里的"全部"用 every-**：`Everything's gone up.` ／ `everyone knows`。
同一格里的邻居（别串）：#122 管的是"随便哪个" ⇒ any- 那一族 —— 一个"全部"一个"随便"，⛔ 别串。
判据一句话：肯定句说"谁都／全都" ⇒ every- 那一族，主语一个词就够。

**怎么发现的**
旧 B 表迁移（B207b，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅、2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-09-09 复检第 3 组 ✅ `everyone knows`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"谁都…"时主语直接落一个 everyone／everything，不用再拼成短语。

**题面**
"谁都知道"（主语用一个词）

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-09-09 ✅ 复检 · 第 3 组 · `everyone knows`
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；everyone／everything 当主语她一直对

### 125 · employer（给工作的）／employee（拿工作的）
类型 词汇 ｜ 旧号 B210
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**employer（给工作的）／employee（拿工作的）**—— 两个词只差词尾：
`companies should provide training to **employees**.`
同一格里的邻居（别串）：staff／worker 也能说"员工"，但绕开这组辨析 ⇒ 题面已排除。
判据一句话：**-er 是雇人的那方，-ee 是被雇的那方**。

**怎么发现的**
旧 B 表迁移（B210，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `companies should provide training to employees.` ⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ `employee`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写这个词前先问一句 —— 是发工资的那方还是拿工资的那方？拿工资的是 employ**ee**。

**题面**
"员工"（一个词，⛔ 不许用 staff／worker）

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-19 ✅ `companies should provide training to employees.`
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `employee`
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；employee 她一直用对，staff／worker 也都地道

### 126 · get used to ／ settle into（适应新环境）
类型 词组 ｜ 旧号 B211
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**get used to ／ settle into（settle in）** ＝ 适应新环境：
`new staff need time to **settle in**.` ／ `get used to the new environment`。
同一格里的邻居（别串）：adapt／adjust 也能说"适应"，但绕开这两个口语块 ⇒ 题面已排除。
判据一句话："适应"在口语里走 get used to 或 settle in／into。

**怎么发现的**
旧 B 表迁移（B211，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-19 ✅ `new staff need time to settle in.`（settle in 用对）⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ `get used to the new environment`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"适应"时先在 get used to 和 settle in 里挑一个，⛔ 别先去够 adapt／adjust。

**题面**
"适应新环境"（⛔ 不许用 adapt／adjust）

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-19 ✅ `new staff need time to settle in.`（settle in 用对；句中的 staff 因教练刚给过，不计 #129）
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `get used to the new environment`
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ① 同级说法
  "适应新环境"说 adapt to／adjust to 同样成立，get used to／settle in 只是口语偏好（旧题面靠排除项硬框）⇒ 中译英里产不出 ❌；历史零 ❌

### 127 · especially 不带来介词：句子本来要什么介词就用什么
类型 结构 ｜ 旧号 B213
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 整句

**问题是什么**
**especially 不带来介词**：句子本来要什么介词就用什么 ——
`this app is great **for** everyone, especially **for** commuters.`（前面是 for，后半也用 for；整个省掉那个 for 也对）。
她真正的错是**"挂空"**：介词短语后面另起一个完整句 ⇒ 悬空；万能式是 `This is especially true for…`。
判据一句话：especially 只是加重语气，介词跟着**原来那个搭配**走，⛔ 别现挑一个新的。

**怎么发现的**
旧 B 表迁移（B213，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ◎。
2026-08-19 ✅ `this app is useful for everyone, especially working people.`（没硬塞介词、没挂空）⇒ 毕业；
同日她问"省一个 for 可以么" → 可以（前面已有 for everyone，后面省略式母语者常用）。
2026-09-10 复检第 4 组 ✅ `this app is great for everyone, especially **for** commuters.`

**我错在哪**
她的：本条判定里没有掉过（08-12 那次是 ◎）；尾部备注记着她的典型错是"挂空"——介词短语后面另起完整句。触发原话未存。
找法：写完 especially 回头看前半句用的是哪个介词 —— 照抄那个，或者整个省掉。

**题面**
"这个 app 谁都好用，对上班族尤其如此。"

- 2026-08-12 ◎
- 2026-08-13 ✅
- 2026-08-16 ✅
- 2026-08-19 ✅ `this app is useful for everyone, especially working people.`（没硬塞介词、没挂空）
- 2026-09-10 ✅ 复检 · 第 4 组 · `this app is great for everyone, especially **for** commuters.`
  考点命中：especially 自己不带介词 —— 句子本来是 great **for** everyone，所以后半也用 for
  ⚠️ 选词（⛔ 未建条目）：中文"上班族"更贴 office workers／working people，commuters 侧重"通勤的人"；
     在 app 语境里说得通 ⇒ ⛔ 不判错（§3.2b：说不出"她不会哪个词组"就不建条目）
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌（08-12 是 ◎）；especially 后面的介词她一直跟对
- 备注 她真正的错是"挂空"：介词短语后面另起完整句 ⇒ 悬空。万能式 `This is especially true for…`
- 备注 08-19 她问"省一个 for 可以么" → 可以：前面已有 for everyone，后面省略式母语者常用；
  写成 especially for working people 也对

### 128 · 坐飞机 ＝ fly／be on a plane／take a plane（❌ take the airplane）
类型 搭配 ｜ 旧号 B215
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

**问题是什么**
**坐飞机 ＝ fly ／ be on a plane ／ take a plane**（❌ take the airplane）。
同一格里的邻居（别串）：by air ／ go by plane **同属正确形**（09-05、09-07 两次判 ✅ 时写明）——
条目只排除 take the airplane，⛔ 不因为她没用目标形就判错。
判据一句话：口语最短的是 **fly**；要用 take 就 take **a** plane。

**怎么发现的**
旧 B 表迁移（B215，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅、2026-08-15 ❌。
2026-08-19 ✅ `Shanghai is far away, so I usually take a plane`（更口语的是 I usually fly）⇒ 2026-08-20 毕业。
2026-08-19 📝 题面整改：原题面"我每天坐地铁上班。"根本测不到本条（迁移时串行）⇒ 换成能逼出 fly／take a plane 的句子。
2026-09-05 ✅ by air；2026-09-07 复检（打包）✅ `by plane`。

**我错在哪**
她的：2026-08-15 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：说"坐飞机"最省事就一个 fly；要用 take 就记住是 take **a** plane。

**题面**
"坐飞机去"

- 2026-08-13 ✅
- 2026-08-15 ❌
- 2026-08-16 ✅
- 2026-08-19 ✅ `Shanghai is far away, so I usually take a plane`（更口语的是 I usually fly）
- 2026-08-19 📝 题面整改：原题面"我每天坐地铁上班。"根本测不到本条（本条讲的是坐飞机怎么说），
  是迁移时串行 → 换成能逼出 fly／take a plane 的句子
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· by air（合法但非预期 ⇒ §3.3 记 ✅ ＋ 当场改题面）
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `by plane`（§3.3 合法但非条目字面预期 ⇒ 记 ✅；
  条目只排除 take the airplane，go by plane 与 fly／take a plane 同属正确形 ⇒ ⛔ 不改题面）
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [2c] · `Take a flight.` —— 与 fly／take a plane 同属正确形，没落成 take the airplane

### 129 · staff 是集合名词，没有复数 staffs（the staff ARE friendly）
类型 语法 ｜ 旧号 B216
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21**（08-23 撤销 08-21 的误判后按日志重放补记；她 08-23 也当场指定）｜ 退池 ｜ 题型 词组

**问题是什么**
**staff 是集合名词，没有复数 staffs** —— 唯一的硬错就是写出 staff**s**。
同族一起记：staff ／ police ／ people ／ the media —— 没有 -s 但配复数动词。
⚠️ `the staff **is**` 在美式里是标准用法（2026-08-23 教练为此撤销过一次误判）⇒ is／are **只是偏好**：
　说"里面的人好相处"时 are 更常听、也更贴题面里的"都"，但 ⛔ 不判错。
同一格里的邻居（别串）：employees 完全合法、三次把本条绕开过 ⇒ 题面点名"用 **staff** 这个词说"。
判据一句话：staff 后面永远不加 -s。

**怎么发现的**
旧 B 表迁移（B216，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅；
08-16 ◎ 与 08-19 ◎ 都被 employees 合法绕开（教练欠了三天没改题面）⇒ 08-19 当场加点名。
2026-08-20 ✅ ／ 2026-08-21 ✅（那次一度被误判 ❌，08-23 撤销、改判 ✅）⇒ 连对 2，毕业日回填 08-21。
2026-08-23 ✅ 付息日 a 段，她当场也指定毕业（"这条毕业"）。
2026-09-01 📝 自发命中留痕 · `some allow **staff** to work flexibly or work from home.`；2026-09-11 复检 ✅ `our company staff`。

**我错在哪**
她的：本条的硬错（staffs）**三次都没犯**；08-17 那次是"给了答案才会"（📖），08-21 那次 ❌ 是**教练判错**、已改判 ✅。
找法：写 staff 时手别顺出那个 -s；要强调"里面的人"就配 are。

**题面**
**点名**："我们公司的员工"（用 **staff** 这个词说）

- 2026-08-13 ✅
- 2026-08-16 ◎ 题面没逼出（employees 可绕开）→ 改题面
- 2026-08-17 📖 给了答案才会（连对清零）
- 2026-08-19 ◎ **第三次**被 employees 合法绕开 —— 08-16 就写了"要改题面"，教练欠了三天没改
  ⇒ 今天当场加点名
- 2026-08-20 ✅ 复习（点名题面第一次生效）· `staff at our complany are easy to get along with`
  ——没写 staffs，动词也用了复数 are ｜`complany` 是打字，按 §2.1 不算
- 2026-08-21 ✅ 复习 · `staff at our company **is** very easy to get along with.`　⚠️ **本条已于 2026-08-23 改判为 ✅**（撤销块见下）
  ——staffs 没写（对），但 **staff 作主语必须配复数动词 are**，她写了 is ⇒ 考点位置没达成
  ⚠️ **同一条上的回退**：08-20 她写的正是 `staff … **are** easy to get along with`
  ★ 四问自审留痕：美式确有 `the staff is` 的整体用法，先自问了能不能推翻 —— 不能：
    ① 雅思按英式口径 ② `easy to get along with` 说的是里面的人不是机构，这个语义连美式也倾向 are
    ③ 本条条目名本身就写着 `the staff ARE friendly`，考点定义就是它
  ★ 同族一起记：staff ／ police ／ people ／ the media —— 没有 -s 但配复数动词

- 2026-08-23 ✅ 付息日 a 段 · `The staff at our company is easy to get along with.`
  —— **考点达成**：本条考点 ＝ staff 没有复数形式 staffs，她 08-20／08-21／08-23 三次都没写 staffs
  ⇒ **她当场指定毕业**（"这条毕业"）
- 2026-08-23 ⛔ **教练犯规·撤销 08-21 的 ❌**（往松的方向改，理由写全）：
  08-21 教练因为她写 `staff … **is**` 判 ❌，理由是"雅思按英式口径，staff 一律配复数 are"。**这条理由不成立**：
  ① **雅思英美两种变体都接受**，AmE 里 `The staff is …` 是标准用法
     （`The staff is committed to helping every student.`）
  ② 本条条目名写的是"**没有复数 staffs**"，括号里的 `(the staff ARE friendly)` 是**举例**，不是考点定义
  ③ 08-21 教练自己在日志里也写了"美式确有 the staff is 的整体用法"，然后用"雅思按英式"把它压下去 —— 站不住
  ⇒ 判罚降级为 **⚠️**（偏好：说"里面的人好相处"时 are 更常听，也更贴题面里的"都"），
    **08-21 那次改判 ✅**；状态按日志重放 ⇒ 08-20 ✅(1) → 08-21 ✅(2) **连对2，毕业日期回填 2026-08-21**
    → 08-23 ✅(3)
  ★ 唯一的硬错仍然是 **staffs** —— 三次她都没犯
- 2026-09-01 📝 新题 P3（bank:490）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）
  `some allow **staff** to work flexibly or work from home.` —— staff 没加 s。
  ★ 本条 08-20／08-21／08-23 连测三次（中间还有一次教练误判撤销）才稳住，今天在**自由产出**里一次到位。
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `our company staff` —— staff 单数，⛔ 没写成 staffs（考点命中）
  ⚠️ 顺带：our company staff → the staff at our company（三个名词叠着读着生硬）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存；staffs 这个硬错她一次都没犯过（08-21 的 ❌ 是教练误判、已撤销）

### 130 · can 才是默认，be able to 是备用（只在完成时/不定式/情态后才必须换）
类型 语法 ｜ 旧号 B217
状态 连对2 连错0 上次2026-09-13 ｜ **累错 4** ｜ **🎓 已毕业 2026-08-21** ｜ 题型 整句

**问题是什么**
**can 才是默认，be able to 是备用**。
一句话判据：**平时用 can；句子里出现 have/had ／ to ／ 另一个情态时，才换 be able to**
（`I **can't** drive.` ／ `I've never **been able to** get up early.`）。
⚠️ 与 🎓#259（have ＋ 过去分词）互斥写死（2026-09-05 c 段裁决）：
　**"从来没能早起过" ⇒ #259（分词形式 been）／ 别的完成时句 ⇒ 本条（can vs be able to）** ——
　本条第二句因此换成"我一直没能联系上他。"
判据一句话：这个位置放得下 can 就放 can；放不下才换 be able to。

**怎么发现的**
旧 B 表迁移（B217，2026-08-18，累错 4），原始触发原话未存；最早记录 2026-08-13 ❌，连三次。
2026-08-19 ❌ `I've never got up early`——完成时里必须换 be able to（→ never been able to get up early）。
2026-08-20 ✅ ／ 2026-08-21 ✅ `I can't drive. I've never been able to get up early.` ⇒ 连对 2，毕业（累错 4 的老账结清）。
2026-09-05 复检第 4 组 ✅ 两格都对。

**我错在哪**
她的：`I've never got up early`（2026-08-19）　　正确：`I've never **been able to** get up early`
找法：想说"没能…"时先看这个位置放不放得下 can —— 放不下就换 be able to。

**题面**
**点名**："我不会开车；我一直没能联系上他。"（两句都说，第二句用现在完成时说）

- 2026-08-13 ❌
- 2026-08-15 ❌
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ❌ `I've never got up early`——完成时里必须换 be able to（never been able to get up early）
  ｜前半 `I can't drive` ✅
- 2026-08-20 ✅ 复习 · `I can't drive. I've never be able to get up early.`
  ——**"换成 be able to"这一步做到了**，本条考点位置达成 ⇒ ✅
  ｜同句 be→been 的形态错**不算在本条头上**，归新建 #259（have ＋ 过去分词）
- 2026-08-21 ✅ 复习 · `I can't drive. I've never been able to get up early.`——两处都一字不差：
  默认位用 can't、进了完成时才换 be able to → **连对2，毕业**（累错 4 的老账结清）
  ★ 同句 been 归 #259 记 ✅
- 2026-09-05 ✅ 复检组 · 第 4 组 · `I can't drive. / I have never been able to get up early.`
  两格都对：默认走 can ／ 现在完成时才换 been able to。
- 2026-09-05 📝 题面整改 · c 段撞车裁决（§3.1③ 第三档）
  与 🎓#259 撞车：本条第二句「我从来没能早起过。」**与 #259 的整个题面逐字相同**。
  两条考位不同（本条 ＝ can 默认／何时必须换 be able to；#259 ＝ have 之后必须用过去分词 been），
  但同一句话先答哪条，另一条就只剩抄写。
  ⇒ 本条第二句换成 **"我一直没能联系上他。"**（仍是现在完成时，仍逼出 been able to，但不与 #259 撞车）。
  ★ 互斥写死：**"从来没能早起过" ⇒ #259（分词形式）／ 别的完成时句 ⇒ 本条（can vs be able to）。**
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组 · `I can't drive. I'v not been able to get reach hime.`——第一句 can't、第二句 haven't been able to，两格都对（I'v／hime 拼写不算）
  ｜同句 `get reach him` ❌ 不归本条 ⇒ 新建 #339（reach sb 直接带宾语）

### 131 · go ＝ 在程度轴上移动（go too far／How far are you willing to go?）
类型 词组 ｜ 旧号 B218
状态 连对2 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
**go ＝ 在程度轴上移动**：far 的搭档永远是 **go** —— `How **far** are you willing to **go**?`
同族整块背：go too far ／ go all the way ／ How far would you go?
判据一句话：句子里出现 far 这个程度词，后面那个动词就必须是 go，⛔ 不许塌成 do。

**怎么发现的**
旧 B 表迁移（B218，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ❌；
08-16 📖（教练自相矛盾的题面已删，❌ 撤销）。
2026-08-20 ❌ 复习 · `how far are you willing to **do**`——far 调对了、**动词塌成 do** ⇒ 连对清零。
2026-08-21 ✅ ／ 2026-08-23 ✅ `how far are you willing to go.` ⇒ 连对 2，毕业。
2026-09-05 复检第 5 组（打包）✅ `how far are you willing to go`。

**我错在哪**
她的：`how far are you willing to do`（2026-08-20）　　正确：`how far are you willing to **go**`
找法：句子里一出现 far，后面那个动词直接定成 go。

**题面**
**点名**："你愿意做到什么程度？"（用 far 说一遍）

- 2026-08-13 ❌
- 2026-08-15 ✅
- 2026-08-16 📖（教练自相矛盾的题面已删，❌ 撤销）
- 2026-08-17 ✅
- 2026-08-20 ❌ 复习 · `how far are you willing to **do**`——far 调对了，**动词塌成 do**
  ⇒ 考点位置就是这个动词（far 只跟 go 走），未达成，连对清零
- 2026-08-21 ✅ 复习 · `how far are you willing to go.`——一字不差，08-20 那次动词塌成 do，这次 go 出来了
- 2026-08-23 ✅ 付息日 a 段 · `how far are you willing to go.`——一字不差，连续第二次 → **连对2，毕业**
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `how far are you willing to go`
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组 · `how far are you willing to go`
- 备注 同族整块背：go too far ／ go all the way ／ How far would you go? —— far 的搭档永远是 go

### 132 · 环路 ＝ ring road（❌ round road）
类型 词汇 ｜ 旧号 B219
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**环路 ＝ ring road**（❌ round road）：`I live just off the second **ring road**.`
同一格里的邻居（别串）：loop／circle 也能想到"环"，但那不是这条路的名字 ⇒ 题面已排除。
判据一句话："几环路"就是 the Nth **ring road**，一个固定名字。

**怎么发现的**
旧 B 表迁移（B219，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅。
2026-08-19 ✅ `I live just off the second ring road.`（ring road ＋ ⭐ just off 把"边上"译准了）⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ `the second ring road`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存 —— 条目名里的 round road 是要她避开的那条路。
找法："几环"直接调 ring road 这个固定名字。

**题面**
"二环路"（⛔ 不许用 loop／circle）

- 2026-08-13 ✅
- 2026-08-16 ✅
- 2026-08-19 ✅ `I live just off the second ring road.`（ring road ＋ ⭐ just off 把"边上"译准了）
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `the second ring road`
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；ring road 她一直对（round road 这条错路从没走过）

### 133 · this morning / last night（❌ today morning／yesterday night）
类型 搭配 ｜ 旧号 B220
状态 连对2 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 退池 ｜ 题型 词组

**问题是什么**
**this morning ／ last night**（❌ today morning ／ yesterday night）。
同一格里的邻居（别串）：yesterday **evening** 同样是两个词、也完全正确，但绕开 last night 这个考位
⇒ 2026-09-07 题面补了「⛔ 不许用 evening」。
判据一句话：这一族靠 **this／last** 搭（this morning ／ last night），⛔ 不用 today／yesterday 去配。

**怎么发现的**
旧 B 表迁移（B220，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅、2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-09-07 复检第 5 组（打包）✅ `last night`（⛔ 没写成 yesterday night，也没退到 evening）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存 —— 条目名里的 today morning／yesterday night 是要她避开的那条路。
找法：说昨晚／今早时先摸 last／this。

**题面**
"昨天晚上"（两个词 · ⛔ 不许用 evening）

- 2026-08-13 ✅
- 2026-08-16 ✅
- 2026-09-07 📝 题面补「⛔ 不许用 evening」：原题面只限"两个词"，而 yesterday evening 同样是两个词、
  且完全正确 ⇒ 绕开了 last night 这个考位（§6.5 第 7 项）。
- 2026-09-07 ✅ 复检 · 第 5 组（打包）· `last night`（⛔ 没写成 yesterday night，也没退到 evening）
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；last night／this morning 她一直对（yesterday night 这条错路从没走过）

### 134 · 不是所有动词都要宾语（decide/choose/help/manage/win 能单独站住）
类型 语法 ｜ 旧号 B221
状态 连对2 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 退池 ｜ 题型 整句

**问题是什么**
**不是所有动词都要宾语**：decide／choose／help／manage／win 这几个能单独站住 —— `I can't **help**.`
⚠️ **必须和 #18 一起读**（08-19 判重发现）：#18 是"英文动词必须带宾语"，**本条是它的白名单**；
　两条不冲突但会互相带偏 ⇒ 判之前先查白名单。
判据一句话：这个动词在不在白名单里？在 ⇒ ⛔ 不用补宾语。
★ 过度泛化警报：修一处、隔壁被带偏（教练纠了两次"缺宾语"，她给不及物动词也硬加）。

**怎么发现的**
旧 B 表迁移（B221，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅、2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-09-09 复检第 3 组 ✅ `I can't help` —— 动词单独站住，⛔ 没补宾语。

**我错在哪**
她的：本条判定里没有掉过；尾部备注记的是**反向**风险 —— 被"动词必须带宾语"带偏、给不及物动词硬加。触发原话未存。
找法：想给动词补宾语之前先查一眼白名单（decide／choose／help／manage／win），在里面就别补。

**题面**
"我帮不上忙。"

- 2026-08-13 ✅
- 2026-08-16 ✅
- 2026-09-09 ✅ 复检 · 第 3 组 · `I can't help` —— 动词单独站住，⛔ 没补宾语
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；I can't help 这类不及物用法她一直对（过度泛化只是风险提示，没有一次实例）
- 备注 过度泛化警报：修一处，隔壁被带偏（教练纠了两次"缺宾语"，她给不及物动词也硬加）
- ⚠️ **必须和 #18 一起读**（08-19 判重发现）：#18 是"英文动词必须带宾语"，本条是它的白名单。
  两条不冲突但会互相带偏 ⇒ 判之前先查白名单

### 135 · 中文的"社会/大家/人们"→ 英语常用 there is 或被动吃掉
类型 结构 ｜ 旧号 B222
状态 连对2 连错0 上次2026-09-28 ｜ 题型 整句 ｜ 退池 ｜ **回潮 2026-09-09**（08-20 毕业 → 09-09 复检答"忘了"：题面当天补上排除项、考位才露出来，there is ／ 被动两条路都没调出来，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-11**（连对2 ＝ 09-10 ✅ ＋ 09-11 ✅；09-09 回潮后第二次毕业）
**问题是什么**
中文的"社会／大家／人们"→ 英语常用 **there is** 或**被动**吃掉：
`There are really high expectations on young people.` ／ `**there is** widespread agreement that this is wrong.` ／
`In Japan, **there is** bias against female managers.`；也可以把受事提上主语位：
`young people **are facing** expectations that are too high.`
同一格里的邻居（别串）：`Society expects too much of young people.` ／ `Everyone thinks this is wrong.`
都是地道英语，却把考点整个绕开 ⇒ 2026-09-09 题面补了「⛔ 不许用 society／everyone／people 当主语」。
判据一句话：中文主语是"社会／大家／人们"这种虚主语 ⇒ 换成 There is …，或者把受事提上来当主语。

**怎么发现的**
旧 B 表迁移（B222，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅、2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-09-05 📝 自发命中留痕 · `In Japan, there is bias against female managers.`
2026-09-09 ❌ 复检第 3 组 · 题面当天补上排除项、考位才露出来，她答"忘了" ⇒ **回潮**
（★ 09-05 那次是自由产出里的偶发命中，≠ 点名就能产出）。
2026-09-10 ✅ ／ 2026-09-11 ✅ ⇒ 连对 2，第二次毕业。

**我错在哪**
她的：答"忘了"（2026-09-09 复检 —— there is ／ 被动两条路都没调出来）
正确：`There are really high expectations on young people.` ／ `There's a feeling that this isn't right.`
找法：中文主语是"社会／大家／人们"时先别直译 —— 换成 There is …，或者把受事提上来当主语。

**题面**
"社会对年轻人期待太高。" ／ "大家都觉得这样不对。"（两句都 ⛔ 不许用 society／everyone／people／we／they 当主语）

- 2026-08-13 ✅（📊 当日记在 B222）
- 2026-08-16 ✅
- 2026-09-05 📝 复检第 4 组 [1] 自发命中留痕（🎓 冻结，只留痕、⛔ 不推进数字）
  `In Japan, **there is** bias against female managers.` —— 中文的"社会"用 there is 吃掉了，⛔ 没硬翻成 society。
- 2026-09-09 📝 题面整改 · 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面两句都能合法地硬翻主语：`Society expects too much of young people.` ／ `Everyone thinks this is wrong.`
  —— 两句都是地道英语，却把本条考点（用 there is ／ 被动把中文的"社会/大家/人们"吃掉）整个绕开
  ⇒ 补排除项「⛔ 不许用 society／everyone／people 当主语」；⛔ 未点名 there is 或被动（那是考点本身）
- 2026-09-09 ❌ 复检 · 第 3 组 · 答"忘了" —— **回潮**
  题面本场已加排除项（⛔ society／everyone／people 当主语），考位这才露出来 ⇒ there is ／ 被动两条路都没调出来
  最小改 `There are really high expectations on young people.` ／ `There's a feeling that this isn't right.`
  ★ 09-05 自由产出里她**自发**用过 `there is bias against female managers` ⇒ 偶发命中 ≠ 点名就能产出
- 2026-09-10 ✅ 复习 · 在池第 1 组 · 两句都没让"社会／大家"当主语
  `① young people are facing high expectations ② there is widespread agreement that this is wrong.`
  ★ ① 把受事提上主语位、把"社会"整个吃掉；② 正是本条点名的 there is。09-09 回潮后第一次通过。
  ⚠️ ① 漏了"太高"的"太"那一层（只剩"有很高的期待"）—— 归 diff-2 的 ⚠️，⛔ 不影响本条考点判定
- 2026-09-11 ✅ 付息日 a 段 · 第 1 组 · `young people are facing expectations that are too high. / There is a general sense that this is wrong`
  —— 两句都没让 society／everyone／people 当主语：① young people 提上来当主语 ② 走 There is ⇒ 连对2 **毕业**
  ⚠️ 更好版 are facing → face（长期普遍状况用简单现在时）· There is → There's（口语缩读）
- 2026-09-18 📝 题面整改：排除项补 `／we／they` · 复检组发题前审核（§6.5 第 7 项）
  `We all think this is wrong.`／`They expect too much of young people.` 用代词把"大家／社会"原样翻成主语，同样合法，绕开 there is／被动 ⇒ 补排除项
- 2026-09-18 ✅ 复检 · 学习日 复检第 3 组 · `Young people face high expectations now. / The general feeling is that is wrong.`——两句都没让"社会／大家"当主语（受事提上来 ／ 名词化 the general feeling）
  ｜⚠️ that is wrong → that this is wrong（that 从句自己要有主语，只进这一行）
- 2026-09-28 ✅ 复检第 2 组 · `Expectations for young people run way too high. There's a widespread feeling that it's just wrong.`
- 2026-09-29 📝 退池 · ① 同级说法
  `Society expects too much of young people.`／`Everyone thinks this is wrong.` 都是地道英语（条目自己写着），there is／被动只是另一种说法；09-09 那次"忘了"是没调出偏好走法，⛔ 不是说错 ⇒ 中译英里产不出 ❌

### 136 · tell ＋ 有内容的东西（a joke／a story／the truth）
类型 搭配 ｜ 旧号 B223
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **回潮 2026-09-07**（08-20 毕业 → 09-07 复检答 `to be honest`，题面已是完整句、主语与"终于"都在，插入语挂不上去 ⇒ 真掉，撤销毕业、连对清零。★ 09-05 那次答的也是 to be honest，但当时题面被粒度整改截断成裸块「说了实话」与 🎓#232 撞车 ⇒ 判 ◎ 作废，⛔ 不计连击）｜ **🎓 已毕业 2026-09-10**（连对2 ＝ 09-09 ⚡ 自评免测 ＋ 09-10 ✅；09-07 回潮后第二次毕业）
**问题是什么**
**tell ＋ 有内容的东西**：a joke ／ a story ／ **the truth** —— `He finally **told the truth**.`
同一格里的邻居（别串）：confess／admit／**come clean** 都合法、都绕开这个搭配 ⇒ 题面正向点名 tell；
⚠️ `to be honest` 是**插入语**，在主语与"终于"都在的完整句里挂不上去（09-07 那次就是这么掉的）；
　🎓#232（"说实话"）与本条只差一个"了"，缩短题面时会撞车（09-05 判 ◎ 的原因）。
判据一句话："说了实话"这件事是句子的**谓语** ⇒ tell ＋ the truth；`to be honest` 只能当插入语。

**怎么发现的**
旧 B 表迁移（B223，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅、2026-08-16 ❌。
2026-08-19 ✅ `he finally told the truth.` ⇒ 2026-08-20 毕业。
2026-09-07 ❌ 复检第 3 组 · `to be honest` —— 完整句题面下插入语挂不上去 ⇒ **回潮**
（09-05 那次答的也是 to be honest，但当时题面被截断成裸块、判 ◎ 作废）。
2026-09-09 ⚡ 自评免测 ／ 2026-09-10 ✅ `he finally told the truth.` ⇒ 第二次毕业。

**我错在哪**
她的：`to be honest`（2026-09-07 复检）　　正确：`He finally told the truth.`
找法：中文"说了实话"是谓语，先落 told the truth；`to be honest` 只放在句首当插入语。

**题面**
"他憋了好几天，最后还是跟他妈妈说了实话。"（"说了实话"用 **tell** 说）

- 2026-08-13 ✅
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 📝 题面整改：原题面"他跟我说了实话。"带了人，与当天新建的 #171（tell sb／say 不接人）撞车
  ⇒ 去掉"跟我"，本条只测"tell ＋ 有内容的东西"
- 2026-08-19 ✅ `he finally told the truth.`
- 2026-09-07 ❌ 复检 · 第 3 组 · `to be honest` —— 题面已还原成完整句「他终于说了实话。」，主语与"终于"都在，
  插入语 to be honest 挂不上去 ⇒ 这次是真掉（09-05 那次是题面被截断成裸块、判 ◎）
  最小改 `He finally told the truth.`
- 2026-09-09 📝 题面整改 · 在池第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面只排除 confess／admit，而 `He finally came clean.` 同样合法、且完全绕开 tell ＋ the truth 这个考位
  ⇒ 排除项补上 come clean；⛔ 未点名 tell（那是考点本身，§6② 红线）
- 2026-09-09 ⚡ 自评免测 · 在池第 1 组（她原话："这 10 个题直接过吧，算对"）
- 2026-09-10 ✅ 复习 · 在池第 1 组 · `he finally told the truth.` —— tell ＋ the truth 一字不差
  ★ 09-05 那次是缩短题面撞了 🎓#232，整句题面下直接命中 ⇒ **连对2，毕业**
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉三个排除项，正向点名 tell，the truth 留给她（她掉过的是用插入语 to be honest 去顶谓语）；换成跟妈妈坦白场景

### 137 · know（掌握信息）／tell（分辨得出）／get（听懂，只说 I get it）
类型 词汇 ｜ 旧号 B224
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 退池 ｜ 题型 整句

**问题是什么**
**know（掌握信息）／tell（分辨得出）／get（听懂，只说 I get it）**：
`I can't **tell** the difference between the two` ／ `no one can **tell** he was the one who did it`。
同一格里的邻居（别串）：题面排除 know 与 see —— 两句的"分不出／看得出"用的是**同一个动词** tell。
判据一句话：说"分辨得出／看得出来" ⇒ tell；"知道某件事" ⇒ know；"听懂了" ⇒ I get it。

**怎么发现的**
旧 B 表迁移（B224，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅、2026-08-16 ❌。
2026-08-19 ✅ 两句都对 ⇒ 2026-08-20 毕业。
2026-09-05 复检 ✅ I can't tell the difference；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：2026-08-16 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：中文"分不出／看得出"时先落 tell，⛔ 别滑到 know／see。

**题面**
"我分不出这两个有什么区别。" ／ "没人看得出来是他做的。"（两句的"分不出／看得出"用**同一个动词**说，⛔ 不用 know、⛔ 不用 see）

- 2026-08-13 ✅
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ✅ `I can't tell the difference between the two` ＋ `no one can tell he was the one who did it`
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· I can't tell the difference（tell 调出来了）
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-09-29 📝 退池 · ③ 题面收不拢
  "分不出区别"说 can't see the difference 同样地道，不点名逼不出 tell、点了就是给答案；08-16 那次 ❌ 原话未存，此后全对

### 138 · a / an 看【读音】不看拼写（an hour／a university）
类型 语法 ｜ 旧号 B225
状态 连对2 连错0 上次2026-08-16 ｜ **形态类·不召回**（2026-08-25 她定）｜ **🎓 已毕业 2026-08-20** ｜ 题型 整句

**问题是什么**
**a / an 看【读音】不看拼写**：an hour ／ a university ／ **an** indoor playground（indoor 的第一个音是元音 /ɪ/）。
判据一句话：每写一个 a/an，念一遍后面那个词的第一个**音**，元音就用 an。
★ 本条 2026-08-25 标 **形态类·不召回**（她定，原话："**an 和 a 一样处理**"）：
　冠词在 §3.4 的形态类清单里，她自我分诊是"会，只是会漏"（08-13／08-16 两次中译英都答对）
　⇒ ① ⛔ 不进中译英复习组 ② 自由产出里掉了也只记 ⚪ ③ 教练只点出来 ＋ 复述检查触发。

**怎么发现的**
旧 B 表迁移（B225，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅、2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-08-24 ⚪ 自由产出（新题 bank:1027 P2）· `letting him run around in **a** indoor playground`（→ an indoor playground）
—— 当时原判 ❌ ＋ 回潮，2026-08-25 她当天裁决后撤销（原话："an 和 a 一样处理"）⇒ 改记 ⚪、🎓 状态还原到 08-20。

**我错在哪**
她的：`a indoor playground`（2026-08-24 自由产出）　　正确：`**an** indoor playground`
检查触发：每写一个 a/an，念一遍后面那个词的第一个音。

**题面**
不出中译英题（题型 产出验 ＋ 形态类·不召回）；挂自由产出抓：a/an 跟后面那个词的**读音**对不上。
★ 原题面（留档，⛔ 不再发题）："一次挑战" ／ "一台外接显示器"

- 2026-08-13 ✅
- 2026-08-16 ✅
- 2026-08-24 ⚪ **只做记号**（不记 ❌／不掉毕业）· 自由产出（新题 bank:1027 P2 Describe an
  interesting building）· `letting him run around in **a** indoor playground` → **an** indoor playground
  ——indoor 的第一个音是元音 /ɪ/ ⇒ an
  ★★★ **原判 ❌ ＋ 回潮，2026-08-25 她当天裁决后撤销**。她的原话（先就 #254 说，
     教练问冠词是否同办，她答）：**"an 和 a 一样处理"**（承前一句"我会，不用新建，
     和单复数一样，这种你点出来就行"）
     ⇒ 冠词 ＝ §3.4 形态类清单里的"限定词／冠词·指称"，她自我分诊"会，只是会漏"；
       08-13／08-16 两次中译英复习都答对，也是证据。
       ⇒ 本次改记 ⚪、**🎓 毕业状态还原到 2026-08-20**、连对连错回到 08-16 的数
  ★ 08-24 那篇因此重算：真错 2 → **1**，密度 1/90 → **1/181**（已回写 sessions/2026-08-24.md）
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）
- 备注 2026-08-25 标 `形态类·不召回`（§3.4）：冠词在 §3.4 的形态类清单里（"单复数/限定词 · 冠词/指称"），
  自我分诊判据也成立 —— 08-13／08-16 两次中译英复习她都答对，08-24 掉的是**自由产出里检查没跑**。
  ⇒ ① **不进中译英复习组**（孤立测她会，信息量为零）
     ② **自由产出里掉了也只记 ⚪**，不记 ❌／不掉毕业（她 2026-08-25 定，见上条日志）
     ③ 教练的动作只剩一个：**点出来 ＋ 复述检查触发**

### 139 · every / each / another / any(单指) 后面永远跟单数
类型 语法 ｜ 旧号 B226＋B115
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-15**（合并后重算）｜ 退池 ｜ 题型 词组

**问题是什么**
**every / each / another / any（单指）后面永远跟单数**：every student ／ almost any question。
判据一句话：这四个词后面那个名词一律不带 -s。
★ 本条 ＝ 原 #199（any ＋ 单数 ＝ 任何一个）2026-08-19 并入 —— 本条是全集，#199 只是其中 any 那一格。
⚠️ 题面沿革：原题面"每个人都要签到。"与 🎓#143 的第一句完全相同 ⇒ 2026-08-19 换成只测"every ＋ 单数"的一句。

**怎么发现的**
旧 B 表迁移（B226＋B115，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ◎ 题面没逼出（原 #199）。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3、判毕业；2026-08-16 ✅。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：本条判定里没有掉过（08-09 那次是 ◎ ＝ 题面没逼出），触发原话未存。
找法：写完 every／each／another／any，看后面那个名词的尾巴 —— 不许有 -s。

**题面**
"每个学生" ／ "几乎任何问题"

- 2026-08-09 ◎ 题面没逼出（原 #199）
- 2026-08-10 ✅（原 #199）
- 2026-08-13 ✅（两条同日都 ✅）
- 2026-08-15 ✅（原 #199）→ 连对 3，判毕业
- 2026-08-16 ✅
- 2026-08-19 📝 题面整改：原题面"每个人都要签到。"与 🎓#143 的第一句完全相同 ⇒ 换一句只测"every ＋ 单数"
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 4 题整串，她原话："1-4 直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌（08-09 是 ◎）；every／each ＋ 单数她一直对（形态类、从没掉过）
- 备注 合并 2026-08-19：#199（any ＋ 单数 ＝ 任何一个）并入本条 —— 本条是全集
  （every/each/another/any 后面永远跟单数），#199 只是其中的 any 那一格

### 140 · I'd love（现在的意愿）≠ I love（长期喜好）
类型 语法 ｜ 旧号 B227
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**I'd love（当下这件事的意愿）≠ I love（长期喜好）**：`I'd love to try it.`
同一格里的邻居（别串）：really want 完全合法（08-16 她答的就是它）⇒ 题面点名"用 love 说，⛔ 不许用 want"。
判据一句话：说**当下想做这件事** ⇒ I'**d** love to；说**一向喜欢** ⇒ I love。

**怎么发现的**
旧 B 表迁移（B227，2026-08-18），原始触发原话未存；最早记录 2026-08-13 ✅。
2026-08-16 ◎ 她答 really want 完全合法 → 改点名。
2026-08-19 ✅ 点名 · `I'd love to try it if I have a chance` ⇒ 毕业。
2026-09-10 复检第 4 组 ✅ `I'd love to try it.`——**I'd** love ＝ 当下的意愿。

**我错在哪**
她的：本条没有掉过（08-16 那次是 ◎ ＝ 题面没逼出），触发原话未存。
找法：说"很想试试"时前面那个 **'d** 不能丢 —— 丢了就成了"我一向喜欢"。

**题面**
**点名**："我很想试试"（"很想"用 **love** 说，⛔ 不许用 want）

- 2026-08-13 ✅
- 2026-08-16 ◎ 她答 really want 完全合法 → 改点名
- 2026-08-17 ✅
- 2026-08-19 ✅ 点名 · `I'd love to try it if I have a chance`（同句 have a chance 归新号 #172）
- 2026-09-10 ✅ 复检 · 第 4 组 · `I'd love to try it.` —— **I'd** love ＝ 当下的意愿，⛔ 不是 I love
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ① 同级说法
  "很想试试"说 I really want to try it 完全成立（08-16 她答的就是它），I'd love to 只是更客气的说法 ⇒ 中译英里产不出 ❌；历史零 ❌

### 141 · 过去完成时必须有另一个更晚的过去事件当参照
类型 语法 ｜ 旧号 B228
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 整句

**问题是什么**
**过去完成时必须有另一个更晚的过去事件当参照**：
`the store **had already closed** by the time we got there.` ／ `I had waited half an hour **before he came**`。
参照词 ✅ before ／ by the time ／ when ／ until ／ after ｜ ❌ and（并列，同一时间平面）。
判据一句话：用 had done 之前先指出那个参照事件 —— 指不出来就退回一般过去式。
★ 2026-08-13 教练用这条判错过一次，**她当场推翻**（until 本身就是参照点），成立。

**怎么发现的**
旧 B 表迁移（B228，2026-08-18），原始触发原话未存；最早记录 2026-08-15 ✅。
2026-08-19 ✅ `I had waited half an hour before he came`（参照点 before he came 在场）⇒ 毕业。
2026-09-10 复检第 4 组 ✅ 第二句的过去完成有参照事件（by the time we got there）。

**我错在哪**
她的：本条判定里没有掉过；08-13 那次是**教练判错**、被她当场推翻。触发原话未存。
找法：写 had done 之前先找那个更晚的过去事件 —— 找不到就别用过去完成时。

**题面**
"我等了一小时他才来。" ／ "我们到的时候店已经关了。"

- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `I had waited half an hour before he came`（参照点 before he came 在场）
- 2026-09-10 ✅ 复检 · 第 4 组 · `I waited for an hour before he showed up.` ／ `the store had already closed by the time we got there.`
  第二句的过去完成有参照事件（by the time we got there）⇒ 本条考点正面命中
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌（08-13 是教练误判、被她推翻）；过去完成时她一直用对（时态类、从没掉过）
- 备注 参照词 ✅ before/by the time/when/until/after ｜ ❌ and（并列，同一时间平面）
- 备注 08-13 教练用这条判错一次，她当场推翻（until 本身就是参照点），成立

### 142 · 中文"连…都没/都不" → 否定放助动词上，even 跟在后面
类型 结构 ｜ 旧号 B231
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 整句

**问题是什么**
中文"连…都没／都不" → **否定放助动词上，even 跟在后面**：
`He didn't **even** say a single word.` ／ `I don't **even** know his name.`
同一格里的邻居（别串）：`He didn't say a word.` ／ `He didn't say a single word.` 都地道、也都符合旧题面，
却把 **even 的位置**这个考点整个绕开 ⇒ 2026-09-10 题面补点名"两句都用 even 说"（⛔ 未说它该放哪儿）。
判据一句话：否定挂在助动词上（didn't／don't），even 紧跟在它后面。

**怎么发现的**
旧 B 表迁移（B231，2026-08-18），原始触发原话未存；最早记录 2026-08-15 ✅。
2026-08-19 ✅ `he didn't even say a word. I don't even know his name.`（两句都对）⇒ 毕业。
2026-09-10 复检第 4 组 ✅ 两句位置都对 —— 本场发题前刚补的点名把这一格真正测到了。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：中文出现"连…都不"时，先把 not 挂到助动词上，再把 even 紧跟着放下去。

**题面**
"他连一句话都没说。" ／ "我连他名字都不知道。"（两句都用 **even** 说）

- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `he didn't even say a word. I don't even know his name.`（两句都对）
- 2026-09-10 📝 题面补点名「两句都用 **even** 说」· 复检第 4 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面「"他连一句话都没说。" ／ "我连他名字都不知道。"」——
  `He didn't say a word.`／`He didn't say a single word.` 都地道、都符合题面，
  却把本条考点（**even 的位置**：否定放助动词上，even 跟在后面）整个绕开 ⇒ 判 ✅ 但等于没测。
  ⇒ 点名 even 这个词，⛔ 未说它该放哪儿（位置才是考点，§6② 红线）。
- 2026-09-10 ✅ 复检 · 第 4 组 · `He didn't even say a single word.` ／ `I don't even know his name.`
  两句都是「否定挂在助动词上、even 跟在后面」⇒ 位置对
  ★ 本场发题前刚补的点名「两句都用 even 说」把这一格真正测到了：旧题面下 `He didn't say a word.` 就能过关
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；"连…都不"里 even 的位置她每次都放对，`He didn't say a word.` 这类绕法也完全地道

### 143 · 哪些动词后面要带 to（need to/want to/manage to；情态和 make/let/watch 不带）
类型 语法 ｜ 旧号 B232
状态 连对2 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-24**（08-19 曾毕业 → 08-24 回潮 → 同日两次 ✅ 重新毕业）｜ 题型 整句

**问题是什么**
**哪些动词后面要带 to**：need to ／ want to ／ manage to 这一族带 **to**；
情态动词和 make／let／watch 那一族**不带**（`he made me **wait**`）。
判据一句话：need 作**实义动词**时后面一律带 to；make／let／watch ＋ 人，后面一律光杆原形。
★ 与 🎓#16（让某人做某事四件套）是同一条规则的两个角度（#16 尾部 ⚠️ 已记，付息日 c 段处理）。

**怎么发现的**
旧 B 表迁移（B232，2026-08-18），原始触发原话未存；最早记录 2026-08-15 ✅。
2026-08-19 ✅ `every one nedd to sign in` ＋ `he made me wait half en hour`（带 to／不带 to 两边都对）⇒ 毕业。
2026-08-24 ❌ **回潮** · 自由产出（新题 bank:924 P3）· 触发原话 `they **need be** mind of how often and how much`；
**同篇**另两处 ✅（`parents need to keep their promises` ／ `a way to get kids to do what parents want`）⇒ 当天重新毕业。
★ 三记合起来的读法：同一段 128 词里带 to 的三处她对了两处 ⇒ 不是知识缺口，是 S1 那一处滑掉了。
2026-09-09 复检第 3 组 ✅ `every one needs to check in / he made me wait for half an hour`。

**我错在哪**
她的：`they need be mind of how often and how much`（2026-08-24 自由产出）
正确：`they **need to be** mindful of…`
找法：写完 need 就问一句 —— 它是实义动词吗？是就补 to；make／let／watch 后面反过来一律不带 to。

**题面**
"每个人都要签到。" ／ "他让我等了半小时。"

- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `every one nedd to sign in` ＋ `he made me wait half en hour`（带 to／不带 to 两边都对）
- 2026-08-24 ❌ **回潮** · 自由产出（新题 bank:924 P3 Should parents reward children）·
  `they **need be** mind of how often and how much` → they **need to be** mindful of…
  ——need 作实义动词，后面一律带 to ⇒ 状态改回未毕业、连对清零
- 2026-08-24 ✅ **同篇第 2 记**（§3.3 同一天同一条多次产出，每次各记一行各算一次）·
  `parents **need to keep** their promises` ⇒ 连对 0 → 1，连错清零
- 2026-08-24 ✅ **同篇第 3 记** · `a way to **get kids to do** what parents want`
  ⇒ 连对 1 → 2 ⇒ **当天重新毕业**
  ★★ 三记合起来的读法（写下来防下次误读）：**同一段 128 词里，带 to 的三处她对了两处**
     ⇒ 不是知识缺口，是 S1 那一处滑掉了。日志留下证据，状态回 🎓，两边都不欠。
  ★ 若她指认 S1 是打漏了 to（同 #292 那种）⇒ 第 1 记的 ❌ 撤销，只留两条 ✅，状态不变
- 2026-09-09 ✅ 复检 · 第 3 组 · `every one needs to check in / he made me wait for half an hour`
  —— needs **to** check in（带 to）／ made me **wait**（不带 to）两边都对位；every one 只是拼写，§2.1 不算错
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）

### 144 · so … that ／ too … to ／ very 的分工（too…that 不存在）
类型 语法 ｜ 旧号 B233
状态 连对1 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这句话不要考了，直接毕业"）｜ 题型 整句

**问题是什么**
**so … that ／ too … to ／ very 的分工**（**too…that 不存在**）。
判据：**后面跟"句子" → so…that ／ 跟"动作" → too…to ／ 只加强 → very**
`It's **so** good **that** some kids stay at home all day.` ／ `It's **too** expensive **to** buy.` ／ `he must have been **really** tired.`
判据一句话：先看那个程度词后面挂的是句子、动作，还是什么都不挂 —— 三条路各走各的。

**怎么发现的**
旧 B 表迁移（B233，2026-08-18）；最早记录 2026-08-15 ❌。
2026-08-19 ❌ 触发原话 `it's too additive that some kids stay at home all day`——**too…that** 又出现。
2026-08-20 ✅ 两半都对（so…that 跟句子／too…to 跟动作）⇒ 她当场指定毕业。
2026-08-30 📝 `he must have been **too tired**.` ⇒ 按本条判据记备注、给更好版 really／very tired，
**⛔ 不判回潮**（有上下文时那是成立的英语，档位是 ⚠️）；08-31 同一道题面她自己给出了 **really** tired。
2026-09-05 复检 ✅ so good that …（跟句子）／ too expensive to buy（跟动作）。

**我错在哪**
她的：`it's too additive that some kids stay at home all day`（2026-08-19）
正确：`It's **so** addictive **that** some kids stay at home all day.`
找法：写完 so／too 先看后面挂什么 —— 挂整句用 so…that，挂动作用 too…to，什么都不挂就换 very／really。

**题面**
**点名**："这剧太好看了，孩子一天不出门。" ／ "太贵了，我买不起。"（两句都用 so…that ／ too…to 这一族说）

- 2026-08-15 ❌
- 2026-08-16 ✅（同日自由产出里首次用对：`so addictive that…`）
- 2026-08-19 ❌ `it's too additive that some kids stay at home all day`——**too…that** 又出现
  （同句两个打字滑不建号：additive→addictive · too buy→to buy）
- 2026-08-20 ✅ 复习 · `It's so addictive that some kids stay at home all day. It's too expensive to buy.`
  ——两半都对（so…that 跟句子／too…to 跟动作，分工全中）⇒ 她当场指定毕业
  ｜同句 `additive` 是拼写，**按她 08-20 的裁决不算错、不记账**（教练当天误判后已撤销）
- 2026-08-30 📝 复习第1组 [5] 句里 · **记备注，不判回潮**（本条 08-20 她指定毕业，状态行不动）·
  `he must have been **too tired**.` → really tired
  ★ **决定性证据（为什么归本条）**：按本条的判据改（备注写死「跟句子 → so…that ／
    跟动作 → too…to ／ **只加强 → very**」）⇒ 得到 `really/very tired` ⇒ **正确答案**
    ⇒ 是同一条规则，不新建号。
  ★ **不判回潮的理由（四问④档位）**：她这句在有上下文时是**成立的英语**
    （"Why didn't he show up?" "He must have been too tired." ＝ too tired [to come]），
    四问①造得出母语句 ⇒ 档位是 ⚠️ 不是 ❌
    ⇒ 沿用 08-27（🎓#206 `In today's fast-paced world`）与 08-29 的先例：归本条记备注、不回潮。
  ★ **成因有教练一份**：题面"那时候他一定是太累了"是**孤立句**，两种读法都合法
    （"很累" ／ "累到做不了某事"）—— 这不是她的缺口。
    ⇒ #309 的题面**不改**（考点 must have 没受影响），只在此留痕。
- 2026-08-31 📝 付息日 c 段 · **自发命中留痕 ＋ 教练给过的更好版被她调出来**（🎓 状态行冻结，契约⑦）
  a 段第 1 组 [2]（#309 的题面"那时候他一定是太累了"）· `he must have been **really** tired.`
  ★ **08-30 同一条题面**她说的是 `must have been **too** tired`——当天按本条判据记了备注、
    给的更好版正是 `really／very tired`（见本条 08-30 那行）。
    今天同一题面她自己给的就是 **really** ⇒ 隔一天把更好版调出来了。
  ★ 信息量最高的一条：它**不是**"她本来就稳的那一半"，恰恰是**昨天刚被点出来的那一格**
    ⇒ §4① 加速通道边界在这里指向"真命中"，不是"只记 ⚪"。
  ★ 仍不推进连对：本条 08-20 已由她指定毕业，契约⑦ 冻结在毕业那一天。
- 2026-09-05 📝 题面整改 · 付息日 c 段（§6.5 第 6 项 完整句 ＋ 第 8 项 题面撞车，一起解）
  原题面第一句 "太上瘾了，孩子一天不出门。" **缺主语**（残句）；
  但直接补成"这游戏太上瘾了"会**撞回 #197（上瘾 ＝ addictive）** —— 一句中文被两个号考。
  ⇒ **换场景绕开**："这剧太好看了，孩子一天不出门。" ／ "太贵了，我买不起。"
  考点（so…that 跟句子 ／ too…to 跟动作 ／ too…that 不存在）一个字未动，两句都补成完整句。
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· so good that …（跟句子）／too expensive to buy（跟动作）
  —— 分工两边都对
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组

### 145 · bring（到我这儿）／take（从这儿到别处）／fetch（去拿了再回来）
类型 词汇 ｜ 旧号 B234
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19** ｜ 退池 ｜ 题型 词组

**问题是什么**
**bring（到我这儿）／take（从这儿到别处）／fetch（去拿了再回来）**：
`**bring** your computer when you come tomorrow.`
判据一句话：东西的终点是**说话人这边** ⇒ bring；从这儿拿走 ⇒ take；去了再折回来 ⇒ fetch。

**怎么发现的**
旧 B 表迁移（B234，2026-08-18），原始触发原话未存；最早记录 2026-08-16 ✅。
2026-08-19 ✅ `bring your computer when you come tomorrow.` ⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ `bring the computer`——"到我这儿"用 bring，⛔ 没用 take／fetch。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"带过来／带过去"前先定方向 —— 冲着我这边就是 bring。

**题面**
"把电脑带过来"（**一个动词**）

- 2026-08-16 ✅
- 2026-08-17 ✅
- 2026-08-19 ✅ `bring your computer when you come tomorrow.`
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `bring the computer` —— "到我这儿"用 bring，⛔ 没用 take／fetch
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；bring／take 的方向她一直用对

### 146 · know 是状态，不能表"得知"这个动作（find out／hear about）
类型 词汇 ｜ 旧号 B235
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 整句

**问题是什么**
**know 是状态，不能表"得知"这个动作** —— 那个动作要用 **find out ／ hear about ／ realise**：
`I **found out** about it from the news` ／ `I only **realised** later that he'd left`。
同一格里的邻居（别串）：the news 要带 the（on／from／in **the** news）。
判据一句话：说的是"知道"的那**一瞬间** ⇒ find out／hear about／realise；说"一直知道"才是 know。

**怎么发现的**
旧 B 表迁移（B235，2026-08-18），原始触发原话未存；最早记录 2026-08-16 ❌、2026-08-17 ❌。
2026-08-19 ✅ ／ 2026-08-20 ✅ 两句都用动作动词、know 一次没出现 ⇒ 连对 2，毕业。
2026-09-05 复检 ✅ found out about this ／ realized later；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：08-16 与 08-17 各记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：中文"知道了／发现"如果指的是那一瞬间，就别用 know —— 换 find out／realise。

**题面**
"我是刷手机的时候才知道他们俩分手了。"（"知道"指得知消息的那一下）

- 2026-08-16 ❌
- 2026-08-17 ❌
- 2026-08-19 ✅ 复习 · `I found out about it from the news` ＋ `I found he had gone`（两句都没用 know）
- 2026-08-20 ✅ 复习 · `I found out the thing from the news` ＋ `I only realised later that he'd left`
  ——两句都用动作动词（found out／realised），know 一次没出现 ⇒ 连对2 毕业
  ｜同句 `the thing` 归新建 #260（中文"这事"直译），不算本条头上
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· found out about this ／ realized later
  —— 两句都避开了 know 表"得知"
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 中文释义收敛）
  去掉"不许用 know"负向写法，改成中文释义把"知道"限定成得知的那一下（find out／hear／realise 都算对，knew 就是她掉过两次的那条路）；换成刷手机得知分手场景
- 备注 the news 要带 the（on/from/in the news）—— 08-19 她自发带了 the；08-20 仍带对

### 148 · 状态用简单时，变化用完成时（He isn't familiar with it yet.）
类型 语法 ｜ 旧号 B237
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 整句

**问题是什么**
**状态用简单时，变化用完成时**：`He **isn't** familiar with it yet.`（状态）／ `I'**ve known** him for five years.`（for ＋ 时长）。
判据一句话：**for ＋ 时长／since ＋ 时点**强制完成时；单纯描述状态就用简单时。
⚠️ 与 🎓#214 互斥写死（2026-09-05 c 段裁决）：
　**状态动词（know／be）＋ for ⇒ 本条的完成时 ／ 动作动词（work／live）＋ for 且强调"一直在做" ⇒ #214 的完成进行时。**
★ 与 🎓#90（完成时的三个触发）／🎓#91（具体时间点用过去式）三条互相引用、各走各的连击
　（2026-08-19 判重结论：**不并入 #90** —— #90 已毕业不再召回、本条当时只测过一次，并进去等于把"状态 vs 变化"这个面埋掉）。
★ 2026-08-16 她质疑并修正了教练的过度概括（always 不强制完成时），成立；真正强制的只有 for ＋ 时长／since ＋ 时点。

**怎么发现的**
旧 B 表迁移（B237，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ✅ `he isn't familiar with the process` ＋ `I've lived here for 5 years`（两边分工全中）⇒ 🎓 零 ❌ 线毕业。
2026-09-11 复检 ✅ `he's not familiar with the process yet. / I've known him for five years.`

**我错在哪**
她的：本条历史里没有掉过（🎓 零 ❌ 线），触发原话未存。
找法：先看有没有 for ＋ 时长／since ＋ 时点 —— 有就切完成时；只是描述状态就用简单时。

**题面**
"他还不熟悉这套流程。" ／ "我认识他五年了。"

- 2026-08-17 ✅
- 2026-08-19 ✅ `he isn't familiar with the process` ＋ `I've lived here for 5 years`
  （状态用简单时 ／ for ＋ 时长强制完成时，两边分工全中）
- 2026-08-19 📝 判重结论：**不并入 🎓#90**（同上：#90 已毕业不再召回，本条只测过一次，
  并进去等于把"状态 vs 变化"这个面埋掉）。三条（#90 触发词 ／ #91 具体时间点 ／ 本条 状态vs变化）
  互相引用，各走各的连击
- 2026-09-05 📝 题面整改 · c 段撞车裁决（§3.1③ 第三档：目标形式不同 ⇒ 两条，当场改题面互斥）
  与 🎓#214 撞车：本条第二句「我在这儿住了五年了。」与 #214「我在这家公司干了五年了。」同一个中文框，
  **判据却相反**：本条要"for ＋ 时长 ⇒ 完成时"（她 08-19 答 `I've lived here for 5 years` ✅），
  #214 要"完成进行时 have been ＋ -ing" ⇒ **同一句话在两条下会被判出相反结果**。
  ⇒ 本条第二句换成 **"我认识他五年了。"**（know 是状态动词，进行式本来就不成立 ⇒ 只可能走完成时）
  ★ 互斥写死：**状态动词（know／be）＋ for ⇒ 本条的完成时 ／ 动作动词（work／live）＋ for 且强调"一直在做" ⇒ #214 的完成进行时。**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `he's not familiar with the process yet. / I've known him for five years.`
  —— 状态用简单时（⛔ 没写成 hasn't been familiar）＋ 持续到现在用完成时
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；状态用简单时／for ＋ 时长用完成时她一直对（时态类、从没掉过）

- 备注 08-16 她质疑并修正了教练的过度概括（always 不强制完成时），成立；真正强制的只有 for＋时长／since＋时点

### 149 · 动词后面别多加词（celebrate sth／discuss sth／marry sb／bring sb up）
类型 搭配 ｜ 旧号 B238
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-21** ｜ 退池 ｜ 题型 词组

**问题是什么**
**动词后面别多加词**：celebrate sth ／ discuss sth ／ marry sb ／ bring sb up ——
`we usually **celebrate festivals** at home` ／ `**bring me up**`。
判据一句话：这几个动词后面直接跟宾语，⛔ 中间不插介词。

**怎么发现的**
旧 B 表迁移（B238，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-21 ✅ 复习（点名题面首测）· `we usually celebrate festivals at home rather than eating out.` ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `celebrate the holidays` ／ `bring me up`——两个动词后面都没多加词。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写完 celebrate／discuss／marry 直接上宾语，⛔ 手别往介词上滑。

**题面**
**点名**："过节"（用 celebrate 说） ／ "把我带大"（用 bring 说）

- 2026-08-17 ✅
- 2026-08-21 ✅ 复习（点名题面首测）· `we usually celebrate festivals at home rather than eating out.`
  ——celebrate ＋ 直接宾语，后面没多加介词 → **连对2，毕业**
  ★ `rather than ＋ -ing` 跟在完整分句后面成立（We stayed in rather than going out.），不判错
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `celebrate the holidays` ／ `bring me up` —— 两个动词后面都没多加词
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；celebrate／bring up 后面直接跟宾语她一直对（旧题面点名即答案）

### 153 · work AT（下功夫）／work ON（做某项目）／work IN（领域）；"干这行"＝ I've been doing this
类型 搭配 ｜ 旧号 B242
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 整句

**问题是什么**
**work AT（下功夫）／work ON（做某个项目）／work IN（领域）**；
"干这行…年了" ＝ **I've been doing this**（完成进行时，中文这句的固定落点）。
同一格里的邻居（别串）：`I've been in this field for fourteen years.` 也合法 ——
她 09-10 正是换这条路绕开了 work 的介词坑，按 §6「判定依据是题面」判 ✅。
判据一句话：先定意思再挑介词（下功夫 at ／ 做项目 on ／ 在某行业 in）；说"干了多少年"直接走 I've been doing this。

**怎么发现的**
旧 B 表迁移（B242，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ✅ `I'v been doing this for 14 years.` ⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ `I've been in this field for fourteen years.`

**我错在哪**
她的：本条历史里没有掉过（🎓 零 ❌ 线），触发原话未存。
找法：写 work 之前先定意思再挑介词；"干这行 N 年了"整句直接走 I've been doing this for N years。

**题面**
"我干这行十四年了。"

- 2026-08-17 ✅
- 2026-08-19 ✅ `I'v been doing this for 14 years.`（完成进行时，中文"干这行…年了"的固定落点）
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `I've been in this field for fourteen years.`
  ★ 她换了一条路（be in this field）绕开了 work 的介词坑 —— 合法且符合题面 ⇒ 判 ✅（§6「判定依据是题面」）
- 2026-09-21 ⚡ 自评免测 · 复检第 4 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ① 同级说法
  "干这行十四年了"说 I've been in this field for fourteen years 完全成立（09-10 她答的就是它），I've been doing this 只是另一种落点 ⇒ 中译英里产不出 ❌；历史零 ❌

### 154 · 法律/政策配的动词不是 happen（came in／was introduced）
类型 搭配 ｜ 旧号 B243
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 词组

**问题是什么**
**法律／政策配的动词不是 happen**：`the law **came in**` ／ was introduced。
判据：主语是"事" → happen；是"人定出来的东西" → come in。
判据一句话：法律、政策、规定这一类是**被人定出来的**，⛔ 不会自己"发生"。

**怎么发现的**
旧 B 表迁移（B243，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ✅ `the law came in when I was a kid.` ⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ `The law came in`——⛔ 不是 happen。

**我错在哪**
她的：本条历史里没有掉过（🎓 零 ❌ 线），触发原话未存。
找法：主语是法律／政策时先停一下 —— 它不会"发生"，只会"出台"（came in）。

**题面**
"这条法律出台了"

- 2026-08-17 ✅
- 2026-08-19 ✅ `the law came in when I was a kid.`
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `The law came in` —— ⛔ 不是 happen
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；"法律出台"她答 came in，was introduced／was passed 也都对，happen 这条错路从没走过

### 155 · as … as 中间只能放原级；few（可数）／little（不可数）
类型 语法 ｜ 旧号 B244
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-21** ｜ 退池 ｜ 题型 词组

**问题是什么**
**as … as 中间只能放原级**；**few（可数）／little（不可数）**：
`use **as few** plastic bags **as** possible` ／ `speak **as little as** possible`。
同一格里的邻居（别串）：`as less as possible` ❌ —— as…as 本身就是比较结构，里面再放比较级 ＝ 标两遍。
判据一句话：as…as 中间保持原级；名词数得清用 few，数不清用 little。

**怎么发现的**
旧 B 表迁移（B244，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-21 ✅ 复习（点名题面首测）· `the teacher taught him to use as few plastic bags as possible.` ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ 两侧原级、可数用 few、不可数用 little。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写 as…as 时中间那个词保持原级；再看名词数不数得清，选 few 还是 little。

**题面**
**点名**："尽量少用塑料袋"（"尽量少"用 as … as possible 说） ／ "尽量少说话"

- 2026-08-17 ✅
- 2026-08-21 ✅ 复习（点名题面首测）· `the teacher taught him to use as few plastic bags as possible.`
  ——few（可数）选对、中间是原级、taught sb to do 也对 → **连对2，毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `use as few plastic bags as possible` ／ `speak as little as possible` —— 可数用 few、不可数用 little，两侧原级
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；as few／as little as possible 她一直对（as less as 这条错路从没走过）
- 备注 `as less as possible` ❌ —— as…as 本身就是比较结构，里面再放比较级 ＝ 标两遍

### 156 · 同根词：位置决定名词形还是形容词形（the difference／different ways）
类型 语法 ｜ 旧号 B245
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-08-23**（连对2 · 08-20 回潮后走完两次）｜ 题型 整句
　　★★ **2026-08-30 撤销 08-28 的"第二次回潮"**（她当天裁定 `makes a huge different` ＝ 手滑）：
　　　 §2.1 拼写一律不算错 ⇒ 那一次不成立 ⇒ **本条从 08-23 起一直是 🎓，中间没断过**。
　　　 08-29／08-30 的两次 ✅ 相应降为**毕业后留痕**，只作自发命中证据，不推进数字。
　　★ 回潮史（现在只剩一次）：08-20 回潮（`use it with cautious`）→ 08-23 毕业，至今未断
**问题是什么**
**同根词：位置决定名词形还是形容词形**：
`**the difference** between the two versions is pretty obvious.`（主语位 ⇒ 名词形）／
`They handle problems in completely **different** ways.`（贴着名词修饰 ⇒ 形容词形）。
判据：这个词前面有 **the／a／of／with／in／by** 这类介词或限定词吗？有 → 一律**名词形**
（08-20 的 `use it with cautious` 就栽在这里，该 with **caution**）。
判据一句话：看它站在什么位置 —— 主语／宾语位要名词形，修饰名词要形容词形。
⚠️ 与 #280 的分工（2026-08-29 写死）：本条的复测 ⛔ **不许与 #280 排在同一组** ——
　#280 的点名里印着 `difference` 这个词，词形是送的，本条考点根本测不到。
★ 拼写手滑 ⛔ 不算本条的错（她 2026-08-30 裁定 `makes a huge different` ＝ 手滑，§2.1：判据是她脑子里调的词对不对）。

**怎么发现的**
旧 B 表迁移（B245，2026-08-18）；最早记录 2026-08-16 ❌ · 触发原话 `the different between the two`。
2026-08-20 ❌ 自由产出（加练新题 bank:927）· `use it with cautious`（该 with **caution**）⇒ 回潮。
2026-08-21 ✅ ／ 2026-08-23 ✅ ⇒ 连对 2，毕业。
2026-08-28 那次原判 ❌ ＋ 回潮，**2026-08-30 她裁定是"手滑"后整个撤销** ⇒ 本条自 08-23 起一直是 🎓、中间没断过；
08-29／08-30 的两次 ✅ 相应降为毕业后留痕。

**我错在哪**
她的：`the different between the two`（08-16）／ `use it with cautious`（08-20 自由产出）
正确：`the **difference** between the two` ／ `use it with **caution**`
找法：写这个词之前先看它前面有没有 the／a／of／with —— 有就必须用名词形。

**题面**
**点名**："这两个版本之间的差别其实挺明显的。"（用"差别"当**名词**说，主语就是那个差别） ／ "他们处理问题的方式完全不同。"
　　★ 旧题面（"他的耐心让我印象很深。"／"他一直很有耐心。"）2026-09-05 撤出题面字段 —— 沿革见 08-29 那条（§4① 配套动作："回潮后的复测必须用能测到掉的那一格的题面"；08-28 掉的那一格 ＝ **difference／different**，原题面的 patience／patient 测不到它）

- 2026-08-16 ❌ `the different between the two`
- 2026-08-17 ✅
- 2026-08-19 ✅ `his patience really impressed me. he is always patient.`（名词形/形容词形两个位置都对）
- 2026-08-20 ❌ **自由产出**（加练新题 bank:927）· `use it with cautious`——该 with **caution**
  ⇒ 回潮。判据扩写：前面有 **the／a／of／with／in／by** 这类介词或限定词 → 一律名词形
- 2026-08-21 ✅ 复习 · `his patience really impressed me. he is always patient.`
  ——两个位置词形都对（主语位 patience／表语位 patient）⇒ 回潮后第一次翻正，连对 0→1
- 2026-08-23 ✅ 付息日 a 段 · `his patience really impressed me. he is always patient.`
  ——主语位 patience（名词）／表语位 patient（形容词），连续第二次 → **连对2，毕业**（回潮后走完两次）
- 2026-08-28 📝 复习第2组 #280 句里 · `makes a huge **different**` ⚠️ **本条已于 2026-08-30 改判为 📝**（原判 ❌ · 回潮 已撤销）
  → makes a huge **difference**（前面有 **a** ⇒ 必须名词形）
  ★★ **2026-08-30 撤销留痕（她的裁决）**：她当天答"**手滑**" ⇒ §2.1「拼写一律不算错，
     判据 ＝ 她脑子里调的词对不对」⇒ 她调的是名词 difference，手指跑成了高频词 different
     ⇒ **本条的考点（选名词形）这一次其实是达成的** ⇒ 撤销 ❌、撤销回潮、毕业不断。
     ★ 与 #280 同一处、同一个裁决：**一个字符串不可能对一个号是手滑、对另一个号是词形错**
       ⇒ 两条一起撤（教练当天曾写"#156 的回潮不撤"，那句的前提被她的答案取消了）。
  ★ 原判的理由（保留留痕，不删）：08-27 她在同一道题里写的就是 difference（🎓#275 日志可查），
     隔一天重说退成 different —— 当时判成"写对过 → 重说退回形容词形"这个固有形状的第三次出现。
     ⇒ 现在这条形状**只剩 08-16 那一次实证**（"原答案写对，重说时反而退成 different"）。
  ★ 同一处同时落到 #280（考点位置）⇒ 1 处 → 2 个号（§3.3）；两个号今天一起改判
- 2026-08-29 ✅ 复习第1组（**回潮后第一次复测，用的是当天补的第二组题面**：§4① 配套动作
  "回潮后的复测必须用能测到掉的那一格的题面"—— 原 patience／patient 题面测不到 difference／different）·
  a) `the difference between thest two versions is actually pretty obvious.` ——主语位要名词 → **difference** ✅
  b) `They handle problems in completely different ways.` ——修饰 ways 要形容词 → **different** ✅
  ——两端全中。★ **08-30 撤销 08-28 的回潮之后，本条那时已是 🎓（08-23 毕业未断）
    ⇒ 本次降为毕业后留痕，不推进数字**（当时按旧判定记的是"连对0 连错1 → 连对1 连错0"，留痕不删）
  ★ `thest` ＝ these 的手滑，§2.1 拼写一律不算错（判据：她脑子里调的词对不对）⇒ 不记档位、不建条目
  ★ 讽刺的一处对照：**同一天她在这一行被判"手滑不算错"（thest），在 08-28 那一行却被判了 ❌**
    —— 08-30 她一句"手滑"把后者也拉回了同一条规则下。
- 2026-08-29 ⚪ **只做记号，不记第二次 ✅、不推进连对** · 同日复习第1组 #280 句里 ·
  `Having someone to help makes a huge **difference**`（词形对）
  ★ 为什么不按 §3.3「同一天多次各算一次」给第二次 ✅（那样就连对2、当天毕业了）：
    **#280 的题面点名里印着 `difference` 这个词**（"用 make ＋ difference 说"）⇒ 词形是**送给她的**，
    本条的考点（选名词形还是形容词形）这一次**根本没被测到**
  ★ 判据 ＝ §4① 加速通道边界（她 2026-08-27 认可）："刚掉的那一格根本没被测到 ⇒ 只记 ⚪，不推进连对"
    ——不这么切，本条会在**没被真正测到的情况下重新毕业** ＝ 假毕业
  ★ 今天真正算数的那一次是同日 [2] 的**冷测**（题面里没有 difference 这个词，她自己选的名词形）
  ⇒ 配套出题约束（写死）：**本条以后的复测一律用 08-29 补的第二组题面**，
    且**不许与 #280 排在同一组**（#280 的点名会把本条的答案送掉）
- 2026-08-30 ✅ 复习第1组 [1]（逐字沿用 08-29 补的第二组题面）·
  a) `the difference between the two versions is pretty obvious.` ——主语位要名词 → **difference** ✅
  b) `They handle problems in completely different ways.` ——修饰 ways 要形容词 → **different** ✅
  ——两端全中。★ **同日晚些时候她裁定 08-28 是手滑 ⇒ 回潮撤销 ⇒ 本条自 08-23 起一直是 🎓
    ⇒ 本次降为毕业后留痕，不推进数字**（当时按旧判定记的是"连对1 → 连对2，毕业"，留痕不删）
  ★★ 语言侧的价值不变：**这是"重说"测试** —— 08-29 她写 `the difference between thest two
     versions is actually pretty obvious`，隔一天逐字重说，**没有退回 different**。
     ⇒ 08-16 那次"写对过、重说退回形容词形"的形状，这次没有复现。
  ★ 与 08-29 的差异只有两处，都不碰考点：`thest`→`the`（§2.1 拼写不算错）· 省了 `actually`
  ★ 教练侧留痕：一度想换句（怕"昨天刚答对、今天重复＝假毕业"），四问②自审后否掉 ——
    本条要看的就是"重说会不会退"，逐字重说恰恰是有效测试。
- 2026-08-30 ⚪ 复习第2组 [6] 句里 · **只留痕，不推进任何数字**（本条 08-23 起即为 🎓，
  按 §3.1⑦ 冻结在毕业日）· `Whether you have help or not makes a huge **difference**.`
  ★ 不算自发命中证据：**#280 的题面点名里印着 `difference` 这个词** ⇒ 词形是送的
  ★★ **08-29 写死的"#156 与 #280 不许排在同一组"今天执行到位**：
     #156 的冷测（第1组 [1]）排在前、#280 的送答案题（第2组 [6]）排在后
     ⇒ 冷测没被污染，分组措施验证有效。
- 2026-09-05 📝 题面字段整理 · c 段撞车裁决（执行本条 08-29 自己写下的裁定）
  本条元信息里**同时挂着两套题面**：旧的（"他的耐心让我印象很深。"／"他一直很有耐心。"）
  与 08-29 补的回潮复测题面（"这两个版本之间的差别…"／"他们处理问题的方式完全不同。"）。
  ⇒ 两个后果：① `prompts --verify` 会要求发题稿逐字包含**全部四句**；
             ② 旧题面里的「他一直很有耐心。」与 #305（stay patient）撞车。
  ⇒ 08-29 那条日志**自己就写着**"原题面的 patience／patient 测不到掉的那一格" ⇒ 旧题面已被取代。
    本次把旧题面移出题面字段（沿革保留在元信息尾部与 08-29 的日志行里），题面只留复测那两句。
  ★ ⛔ 这不是新裁决，是**执行本条已有的裁定**。
- 2026-09-12 📝 元信息行整理：撤出的旧题面与沿革移到 ★ 行，题面字段只留两句（§3.1② 解析口径：★ 行不算题面本体）· 全档题面 review
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [10] · `The difference between these two versions is actually pretty obvious. They handle problems in a totally different way.`
- 备注 08-16 实证：原答案写对，重说时反而退成 different

### 158 · 场所介词 on（面）／in（有边界的空间）；on the balcony／on the bus
类型 搭配 ｜ 旧号 B247
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 词组

**问题是什么**
**场所介词 on（面）／in（有边界的空间）**：on the balcony ／ on the bus ／ on the table，但 **in** the drawer。
判据一句话：贴在一个**面**上 ⇒ on；装在一个**有边界的空间**里 ⇒ in。

**怎么发现的**
旧 B 表迁移（B247，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ✅ `on his balcony` ＋ `on the table, not in the drawer`（三个场所介词全中）⇒ 毕业。
2026-09-11 复检 ✅ `on the balcony. on the desk, not in the drawer.`

**我错在哪**
她的：本条历史里没有掉过（🎓 零 ❌ 线），触发原话未存。
找法：说位置之前先问一句 —— 是贴在一个面上，还是装在一个空间里？

**题面**
"在阳台上" ／ "在桌上，不在抽屉里"

- 2026-08-17 ✅
- 2026-08-19 ✅ `on his balcony` ＋ `on the table, not in the drawer`（三个场所介词全中）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `on the balcony. on the desk, not in the drawer.` —— 面用 on、有边界的空间用 in
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；on the balcony／in the drawer 她一直对

### 159 · "…的时刻/地方/原因 是…" → 表语用 when／where／that 引导
类型 结构 ｜ 旧号 B248
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 整句

**问题是什么**
**"…的时刻／地方／原因 是…" → 表语用 when／where／that 引导**：
`one moment that really stuck with me **was when** he taught me to prune flowers`。
同一格里的邻居（别串）：`What impressed me most was the time he taught me…` ＝ what 分裂句，完全合法，
却把这一格整个绕开 ⇒ 2026-09-11 题面补了「⛔ 不许用 What 起头的句子说」。
连带：讲过去的事，主句系动词也要过去时（is → **was**）。
判据一句话：主语是"时刻／地方／原因" ⇒ 表语那半用 when／where／that 起头。

**怎么发现的**
旧 B 表迁移（B248，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ✅ `one moment that really stuck with me was when he tought me to prune flowers` ⇒ 🎓 零 ❌ 线毕业。
2026-09-11 复检 ✅ 表语位置用 **when** 引导（本场新补的 ⛔ What 排除项挡住了分裂句那条路）。

**我错在哪**
她的：本条历史里没有掉过（🎓 零 ❌ 线），触发原话未存。
找法：主语是"最…的一刻／地方／原因"时，系动词后面直接给 when／where／that，⛔ 别绕 What 分裂句。

**题面**
"让我印象最深的一刻，是他教我剪花那次。"（⛔ 不许用 What 起头的句子说）

- 2026-08-17 ✅
- 2026-08-19 ✅ `one moment that really stuck with me was when he tought me to prune flowers`
  （表语用 when 引导 ＋ 主句系动词 was 也对；发题前审核预判"可能被 The thing I remember most 绕开"，没绕）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `The moment that really stuck with me the most was when he taught me how to prune flowers.`
  —— 表语位置用 **when** 引导，考点命中（本场新补的 ⛔ What 排除项挡住了分裂句那条路）
  ⚠️ 顺带（不计档位）：really 与 the most 都在做"最"这一层，二选一
- 2026-09-11 📝 题面整改：补（⛔ 不许用 What 起头的句子说）· 发题前审核（§6.5 第 7 项）
  `What impressed me most was the time he taught me…` ＝ what 分裂句，完全合法，
  却把「表语用 when／where／that 引导」这一格整个绕开 ⇒ 补排除项。
  ⛔ 未点名 when／that（考点本身，§6② 红线一）
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ① 同级说法
  `What impressed me most was the time …` 完全合法（条目自己写着），was when 只是另一种表语落点 ⇒ 中译英里产不出 ❌；历史零 ❌
- 备注 连带：讲过去的事，主句系动词也要过去时（is → was）

### 161 · (the) N of us —— 加 the ＝ 全体，不加 ＝ 一部分
类型 语法 ｜ 旧号 B250
状态 连对2 连错0 上次2026-09-22 ｜ 题型 整句 ｜ **回潮 2026-09-04**（08-19 毕业·零 ❌ 线 → 09-04 新题里写成 `the three of my family`，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-07**（连对2 ＝ 09-05 ＋ 09-07；09-04 回潮后第二次毕业）

**问题是什么**
**(the) N of us —— 加 the ＝ 全体，不加 ＝ 一部分**：
`**The three of us** went together.`（我们仨全去了）／ `**two of us** didn't come.`（我们当中有两个）。
同一格里的邻居（别串）：⛔ the three of **my family**（09-04 她从中文"我家的三个人"直译出来的）——
"我们一家三口"英文照样落在 **the three of us**；另：person 的复数口语一律 people。
判据一句话：说"我们当中"这一层 ⇒ of **us**；说"全体"就在前面加 the。

**怎么发现的**
旧 B 表迁移（B250，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ✅ `The three of us went together. two of us didn't come.` ⇒ 🎓 零 ❌ 线毕业。
2026-09-04 ❌ **回潮** · 新题第 1 道（自由产出 · bank:875 P3）· 触发原话
`he pointed at three circles on it, saying they are **the three of my family**.`
★ 掉的**不是 the**（the 她加对了），是 **of us 那一半在"一家三口"这个框里没调出来** ⇒ 当场补了一句题面专测这一格。
2026-09-05 ✅ ／ 2026-09-07 ✅ ⇒ 连对 2，第二次毕业；2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：`they are the three of my family`（2026-09-04 自由产出）　　正确：`the three of **us**`
找法：说"我们（家）几口／几个"时，of 后面永远先填 us，⛔ 别把中文的"我家"直译进去。

**题面**
"上个周末我们一家三口去海边玩了两天，结果我们当中有两个都晒伤了。"（"一家三口"用 **the three of** 说）

- 2026-08-17 ✅
- 2026-08-19 ✅ `The three of us went together. two of us didn't come.`（带 the ＝ 全体／不带 ＝ 一部分）
- 2026-09-04 ❌ **回潮** · 新题第 1 道（自由产出 · bank:875 P3 · Why do most children draw more often than adults do?）
  `he pointed at three circles on it, saying they are **the three of my family**.` → the three of **us**
  ❌ 她要说的是"我们一家三口"，从中文"我家的三个人"直译成了 the three of my family。
  ★ 判重／回潮的**决定性证据**（§3.1，逐条人读，⛔ 未用脚本判）：
    目标英文形式 ＝ `the three of us`；按本条的目标形式去改她这句 ——
    `the three of my family` → `the three of **us**` ⇒ **得到正确答案** ⇒ 同一条 ⇒ 判回潮。
  ★ 掉的是哪一格：**不是 the**（the 她加对了，本条"加 the ＝ 全体"那一半是对的），
    掉的是 **of us 那一半在"一家三口"这个框里没调出来** ——
    08-17／08-19 两次测的都是"我们仨一起去的"（人已经在句子里），
    今天是"这就是我们一家三口"（要自己把 us 想出来）⇒ 新的一格，第一次测到。
  ★ 配套动作（§4① 加速通道边界那条：回潮后的复测必须能测到掉的那一格）：
    **当场补一句题面** ——"他说这就是我们一家三口。"（也用 the ＋ 数字 ＋ of 说）
  ⇒ 撤销毕业、连对清零，状态行改回未毕业（手工改，见状态行）。
- 2026-09-05 ✅ 在池组 · 第 1 组（付息日 a 段）
  `The three of us went together. two of us didn't come. hi said they are the three of us.`
  三句全部命中 (the) N of us：带 the ＝ 全体 ／ 不带 ＝ 一部分。
  ★ 关键：第三句正是 09-04 回潮时掉的那一格（"一家三口"要自己把 us 想出来）——
    题面补句奏效，她这次自己调出了 `the three of us`，⛔ 没有再直译成 the three of my family。
  ｜ `hi` → he 是同一个词写歪 ＝ 拼写（§2.1），不算错、不建条目
  ｜ ⚠️ `they are` → that was（讲画里的东西用 that ／ 说话动词 said 之后时态同一平面），
    diff-2 已给，不记 ❌
- 2026-09-05 📝 题面整改 · 付息日 c 段（题面里不许夹沿革说明）
  第三个成员的括号原本写着"（也用 the ＋ 数字 ＋ of 说，2026-09-04 回潮后补，专测"要自己把 us 想出来"那一格）"
  —— 沿革说明混进了题面字段，而且里面嵌了一对引号，
  `lab.py prompts --verify` 会把它当成**必须逐字出现在发题稿里**的引号句 ⇒ 发题稿被迫带上元信息。
  ⇒ 括号只留点名"（也用 the ＋ 数字 ＋ of 说）"，沿革保留在 09-04 那条日志行里（本来就有）。
  ★ 同一个坑今天在 #234 上先踩过一次（当场改掉了）⇒ 口径定死：**题面字段只放题面和点名，不放沿革。**
- 2026-09-07 ✅ 复习 · 在池第 1 组 · `the three of us. two of us. the three of us` —— 三句 the 的有无全部对位
  ⇒ 连对 2，**毕业**
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 7 组（打包串，她原话："除了 3）忘了，其他直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句（类型 语法 ⛔ 不许标词组）
  一句里放"一家三口"（全体 the）和"我们当中有两个"（部分，不加 the），点名 the three of，of 后面填 us 留给她（她掉过的是 the three of my family）；换成海边晒伤场景
- 备注 person 的复数口语一律 people

### 162 · made OF ／ OUT OF ＋ 材料；写画出来的 ＋ IN（written in pencil）
类型 搭配 ｜ 旧号 B251
状态 连对2 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这题毕业了"） ｜ **合并条·出题多句覆盖** ｜ 题型 词组

**问题是什么**
一道题面覆盖两个成员：
· **写／画出来的 ＋ IN**：written **in** pencil ／ spelt out **in** sweets
· **材料 ＋ made OF ／ OUT OF**：made **of** wood
同一格里的邻居（别串）：08-17 她把 spell out 和 made out of **串台**了（`spelt out OF sweets`）——
两个块各有各的介词，⛔ 不能互相借。
判据一句话：说"用什么写／画的" ⇒ in；说"用什么材料做的" ⇒ of／out of。

**怎么发现的**
旧 B 表迁移（B251，2026-08-18）；最早记录 2026-08-17 ❌ · 触发原话 `spelt out OF sweets`。
2026-08-19 ✅ 两个介词都中；2026-08-20 ✅ `the letter was written in pencil. the box is made of wood.`
⇒ 她当场指定毕业（"这题毕业了"）。
2026-09-05 复检 ✅ in pencil ／ made of wood，两个成员都对。

**我错在哪**
她的：`spelt out OF sweets`（2026-08-17）　　正确：`spelt out **in** sweets`
找法：先分一刀 —— 这是"写／画上去的"还是"拿材料做的"？写画用 in，材料用 of／out of。

**题面**
题面（2 句，两个成员各一句）
　① "蛋糕上那行字是用巧克力酱写的"（字是拿什么写上去的）
　② "这个玩具屋是纸板做的"（拿什么材料做的）

**成员出题账**
① 写／画出来的 ＋ in（written／spelt in） ｜ 08-17 ❌ · 08-19 ✅ · 08-20 ✅ · 09-05 ✅
② 材料 ＋ made of／out of ｜ 08-19 ✅ · 08-20 ✅ · 09-05 ✅
★ 08-17 那一次只测到成员 ①。

- 2026-08-17 ❌ `spelt out OF sweets`（把 spell out 和 made out of 串台）
- 2026-08-19 ✅ `written in pen（该 pencil，但介词对）` ＋ `made of wood`——两个介词都中
- 2026-08-20 ✅ `the letter was written in pencil. the box is made of wood.`——两个介词都对，pencil 也对了
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· in pencil（写画出来的用 in）／made of wood（材料用 of）
  —— 两个成员都对
- 2026-09-18 📝 题面整改：补（第一句 ⛔ 不许用 with）· 复检组发题前审核（§6.5 第 7 项）
  `written with a pencil` 合法，绕开 written in pencil ⇒ 补排除项；made from wood 仍在"made ＋ 材料介词"规则内，判 ✅
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 2026-09-20 📝 学习日 在池第 1 组（#98 句2）· 自发命中留痕 · `spelled out with sweets and biscuits`（🎓 冻结，只留痕、不推进数字）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉"⛔ 不许用 with"，题面改成合并条的编号句，各配中文释义；换成巧克力酱写字／纸板玩具屋

### 163 · "愣住了／说不出话"（I just stood there.／I froze.）
类型 词组 ｜ 旧号 B252
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 退池 ｜ 题型 词组

**问题是什么**
"愣住了／说不出话" ＝ **I just stood there.** ／ **I froze.**
同一格里的邻居（别串）：speechless ／ didn't know what to say 都完全合法，却绕开 stood there／froze
⇒ 2026-09-11 题面补了排除项。
判据一句话：这一层走**动作**（stood there／froze），⛔ 不走形容词或解释性从句。

**怎么发现的**
旧 B 表迁移（B252，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ⛔ 本次作废不计档位：她答得完全对，但那个答案教练上一组讲评里刚展示过 ⇒ 不是 cold 数据，责任在教练。
2026-08-20 ✅（真 cold）· `I just stood there and couldn't say a word` ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `Froze there, unable to say a word.`
★ 尾部备注记着：08-15 给过、当天重说对了，08-16 再问已经不会 ⇒ "当场重说对 ≠ 装上了"。

**我错在哪**
她的：本条判定里没有掉过（08-19 那次作废的责任在教练），触发原话未存。
找法：说"愣住了"时先找那个动作 —— stood there 或 froze。

**题面**
"愣在那儿，一句话也说不出来"（⛔ 不许用 speechless／didn't know what to say）

- 2026-08-17 ✅
- 2026-08-19 ⛔ **本次作废不计档位**：她答得完全对（`I just stood there and didn't say a word`），
  但这个答案教练在上一组讲评里刚展示过 ⇒ 不是 cold 数据。责任在教练，本条顺延重测
- 2026-08-20 ✅ 复习（真 cold，本次没有任何前置展示）· `I just stood there and couldn't say a word`
  ——目标块一字不差，后半 couldn't say a word 也是地道说法 ⇒ 连对2 毕业
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `Froze there, unable to say a word.` —— froze 调出来了，未用被排除的 speechless／didn't know what to say
- 2026-09-11 📝 题面整改：补（⛔ 不许用 speechless／didn't know what to say）· 发题前审核（§6.5 第 7 项）
  两条都完全合法，却绕开 stood there／froze ⇒ 补排除项
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ① 同级说法
  "愣住了说不出话"说 I was speechless／I didn't know what to say 都完全成立（条目自己写着），froze／stood there 只是另一种说法 ⇒ 中译英里产不出 ❌；历史零 ❌
- 备注 08-15 给过、当天重说对了，08-16 再问已经不会 ⇒ "当场重说对 ≠ 装上了"

### 164 · 一句话里时态只能有一个平面
类型 语法 ｜ 旧号 B253
状态 连对2 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-21** ｜ 退池 ｜ 题型 整句

**问题是什么**
**一句话里时态只能有一个平面**：`i found the door locked, so i just went home.`（found／went 全在过去平面）。
判据一句话：换平面要在**句子边界**上换，句内 ⛔ 不许串。
★ 与 #12 的分工：#12 管"该用哪个时态"，本条管"一句里别换档"。

**怎么发现的**
旧 B 表迁移（B253，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-21 ✅ 复习 · `i found the door locked, so i just went home.` ⇒ 连对 2，毕业
（"那天"没译出只是信息略省，⛔ 不记档位）。
2026-08-25 ／ 2026-08-26 连续两篇自由产出里自发命中 —— 一篇四个平面，每次换档都有理由、句内没串。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：一句说完回头看谓语 —— 它们是不是都站在同一个时间平面上。

**题面**
"那天我发现门锁着，所以我就回家了。"

- 2026-08-17 ✅
- 2026-08-21 ✅ 复习 · `i found the door locked, so i just went home.`——found／went 全在过去平面 → **连对2，毕业**
  ★ "那天"没译出，只是信息略省，不是语法错，不记档位
- 2026-08-25 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 加练新题 bank:1043 P2（163 词）·
  **一篇四个时态平面，一个都没串**：
```
现在      he is only 5 / is really into Lego          ＝ 现在仍如此
现在完成  Over the past year, I've bought him…        ＝ 到现在的一段
过去      That time … had to / suggested / built      ＝ 那一次
一般现在  when I draw, I can only copy…               ＝ 说自己的常态
```
  ★ 每一次换平面都有理由，且换回来时没乱 ⇒ 本条 ＋ 🎓#91（有时间点用过去式）同时命中
- 2026-08-26 ✅ **自发命中·连续第二篇**（本条未被出题，不改已毕业状态）· 自由产出（新题 bank:244 P2）·
  **四个平面各有理由**：
```
过去叙事    We met … / the program crashed / he kept calm, sat down, went through   ＝ 那一次
现在泛述    Whenever something breaks, he **is** the kind of person…                ＝ 他一贯如此
现在完成    he's **become** one of the best developers I know                        ＝ 到现在的变化
现在进行    These days he's **doing** really well                                    ＝ 当下这阵子
```
  ★ 从"那一次"泛化到"一贯如此"再到"现在"，三次换档都在句子边界上换，句内没串
  ⚠️ 唯一串了的是 S10 `That is not just that one time.`（前段是过去，这句跳到现在）——
    但那处判的是**层3 衔接/指代**（两个 that 撞在一起），⚠️ 不记 ❌、不落本条
- 2026-09-19 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；一句里时态不串她一直对、自由产出里也自发命中（时态类、从没掉过）
- 备注 与 #12 分工：#12 管"该用哪个时态"，本条管"一句里别换档"

### 165 · even（修饰一个词）／even though（已经发生的事实）
类型 语法 ｜ 旧号 B254
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-19 · 她指定** ｜ 退池 ｜ 题型 整句

**问题是什么**
**even（修饰一个词）／even though（已经发生的事实）**：`**Even though** the home team lost, I was very happy.`
判据：even 后面跟的是**一个词**还是**一整句**？一整句 → 必须 even though／even if。
同一格里的邻居（别串）：although／though／despite 是同义连接词，`We lost, **but** I was still happy.` 是**换结构**——
两类都合法、都绕开考点 ⇒ 题面 2026-09-11 分两步把四个都排除掉。
★ even if（假设）那一半 2026-08-19 已拆出成 **#256**，本条只管 even though。

**怎么发现的**
旧 B 表迁移（B254，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ✅ `Even though the home team lost, I was very happy.` ⇒ **她当场指定毕业**
（原话："你就记对就行，别让我重复练了"）。
2026-09-11 复检 ✅ `We lost, but I was still happy.`——合法、达意、未犯任何排除项 ⇒ 记 ✅；
⛔ 教练犯规：第二译法自查只想了同义词替换、漏了"换结构"（but）⇒ 当天补排除项，⛔ 不扣她的分。

**我错在哪**
她的：本条历史里没有掉过；09-11 走的 but 是合法的另一条路（教练题面没堵住）。触发原话未存。
找法：even 后面挂的是一整句吗？是 ⇒ 必须写成 even though（已发生）或 even if（假设）。

**题面**
"虽然我们输了，我还是很开心。"（⛔ 不许用 although／though／despite）

- 2026-08-17 ✅
- 2026-08-19 ✅ `Even though the home team lost, I was very happy.`
  🎓·她指定：**"你就记对就行，别让我重复练了"**
- 2026-08-19 📝 **拆条**：even if（假设）那一半拆出去 → **#256**（她今天在那一半上答错了，
  捆着测等于让她陪着已经会的 even though 一起重练）
- 2026-08-19 ⛔ 题面整改：原题面"虽然输了，我还是很开心。"**没有主语**，她当场指出"看不懂是谁输"
  ⇒ 改成"虽然我们输了…"；§6 早写死题面必须完整句，发题前审核第 6 项我误判通过
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `We lost, but I was still happy.`
  —— 合法、达意、未犯任何排除项 ⇒ 符合题面，记 ✅（§3.3 硬顺序②），⛔ 不记 ◎、⛔ 不扣分
  ⛔ **教练犯规**：审核表第 7 项只排除了 although／though／despite 三个**同义连接词**，
    漏了**换结构**那条路（but）—— 她走的正是那条 ⇒ 同日 📝 补 ⛔ but
- 2026-09-11 📝 题面整改：补（⛔ 不许用 although／though／despite）＋ 判定后再补 ／but · 两步都在今天
  第一步（发题前，§6.5 第 7 项）：although 合法且更常见，绕开 even though ⇒ 补三个同义连接词。
  第二步（判定后）：⛔ **教练犯规** —— 第 7 项只想了「同义词替换」，没想「换结构」，
    漏掉最自然的 `We lost, **but** I was still happy.`，她走的正是那条 ⇒ 判 ✅、⛔ 不扣分，当场补 ⛔ but。
  ★ 执行修补（写进 SKILL §6.5 第 7 项）：第二译法自查要**分两类想** ——
    ① 同义词替换　② 换结构（but／分裂句／被动／if／名词化）
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ① 同级说法
  "虽然输了还是开心"说 although／but 都完全成立（09-11 她答 but 被判 ✅），even though 只是其中一个 ⇒ 中译英里产不出 ❌；历史零 ❌
- 备注 08-16 当天纠、隔一道题她在全新语境里自发用对 ⇒ 迁移窗口很短但很实

### 166 · see sb（见面）／meet（初次认识）／meet up（约着碰头）—— 选哪个动词
类型 词汇 ｜ 旧号 B255
状态 连对2 连错0 上次2026-09-13 ｜ 顽固已断 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

**问题是什么**
**see sb（见面）／meet（初次认识）／meet up（约着碰头）—— 选哪个动词**：
`I haven't **seen** him …` ／ `We **met** at university.`
判据一句话：见的是**老熟人** ⇒ see；**第一次认识** ⇒ meet；**约着碰头** ⇒ meet up。
⚠️ 与 #276（for ages／in ages）互斥写死（2026-09-05 两次整改）：
　**"好久"怎么说 ⇒ #276（ages）／ 两句的动词选哪个 ⇒ 本条。**
　沿革：#276 是 2026-08-23 从本条拆出去的，当时**老条目的题面没剥干净**，两条一直在考同一句中文
　⇒ 教训写死：**拆号之后必须回头剥老条目的题面**。

**怎么发现的**
旧 B 表迁移（B255，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ❌。
2026-08-19 ❌ **同一个错第二次**：`I haven't seen him for long`（该 for ages／in ages —— 那一格后来拆给了 #276）。
2026-08-20 ✅ ／ 2026-08-21 ✅ `We haven't seen each other in ages. We met at university.` ⇒ 连对 2，毕业。
2026-09-05 复检（打包）✅ 两句动词各自选对 —— 题面当天刚整改完，整改后**首测即过**。

**我错在哪**
她的：`I haven't seen him for long`（2026-08-19；那一处的量词错已归 #276）
正确：`We haven't seen each other **in ages**. We **met** at university.`
找法：先分一刀 —— 见老熟人 see、第一次认识 meet、约着碰头 meet up。

**题面**
"上周跟老同学见了一面"（见的是早就认识的人） ／ "我们俩是大学时认识的"（第一次认识）

- 2026-08-17 ❌
- 2026-08-19 ❌ **同一个错第二次**：`I haven't seen him for long`（该 for ages／in ages）
- 2026-08-20 ✅ 复习 · `we haven't seen each other for ages. We met at university.`
  ——for ages 与 met 两半都对（主语换成 we…each other 等价合法，不扣）
  ｜同句 `we met at university` ✅（meet ＝ 初次认识那一半是对的）
- 2026-08-21 ✅ 复习（点名"用 ages 那个词"后首测）· `We haven't seen each other in ages. We met at university.`
  ——`in ages` ＋ `met` 两半都对 → **连对2，毕业**（08-17／08-19 连着两次写成 for long，这次彻底翻过来）
  ⚠️ 毕业时仍是**捆绑条目**（see／meet／meet up ＋ for ages）：付息日 c 段照样要拆，
    否则将来任一半掉了会把已经会的那半也拖回池子
- 2026-08-23 📝 c 段 **拆号**：`for ages` 那一半（"很久"的量）与本条（选哪个动词）是**两条不同规则**
  ⇒ 拆出 **#276（for ages／in ages）**。两块在 08-20／08-21 的同一句里都产出过两次
  ⇒ **两条都直接 🎓，零池成本**；拆的意义 ＝ 将来任一半掉了只有那一半回潮，不拖累另一半
- 2026-09-05 ✅ 复检组 · 第 4 组（打包）· `I haven't **seen** him … We **met** at university.`
  两句用了不同的动词，且各自选对：see ＝ 见面 ／ meet ＝ 初次认识。
  ★ 本条题面今天刚整改（剥掉与 #276 撞车的 ages 那一格），整改后**首测即过**。
- 2026-09-05 📝 题面整改 · 复检第 4 组发题前审核（§6.5 第 8 项 · **存量撞车**）
  #166 与 #276 的题面里有**逐字相同的一句**：**点名**："跟他好久没见了"（"好久"用 ages 那个词说）。
  沿革：#276 是 2026-08-23 **从本条拆出去**的（§3.2c③），拆的时候把 ages 那一格给了 #276，
  但**老条目（本条）的题面没剥干净** ⇒ 两条至今在考同一句中文，且本轮还被打包进同一道题。
  ⇒ 本条题面剥掉 ages 那一格，只留自己的考点：
    旧：**点名**："跟他好久没见了"（"好久"用 ages 那个词说） ／ "大学认识的"
    新：**点名**："跟他好久没见了" ／ "大学认识的"（两句用**不同的动词**说）
  ★ 互斥写死：**"好久"怎么说 ⇒ #276（ages）／两句动词选哪个 ⇒ #166（see vs meet）。**
  ★ 教训：**拆号之后必须回头剥老条目的题面** —— §3.2c③ 只写了"顽固成员单拆、老条目照常走连击"，
    没写"老条目题面要同步剥掉那一格" ⇒ 方法论真空，今天靠 §6.5 第 8 项才兜住（待她裁是否补进 SKILL）。
- 2026-09-05 📝 题面整改 · c 段撞车裁决（§3.1③ 第三档 · 承接本日第 4 组的第一次整改）
  本日第 4 组发题前已把本条的 ages 那一格剥给 #276，但**中文主体仍重叠**：
  本条「跟他好久没见了」与 #276「我跟他好久没见了。」几乎逐字 ⇒ 同日抽到就互相泄题。
  ⇒ 第一句换成 **"上周跟他见了一面"** —— 去掉"好久"这个 #276 的触发词，
    本条只剩自己的考点（see ／ meet ／ meet up 选哪个动词）。
  ★ 互斥写死：**出现"好久" ⇒ #276（ages）／ 两句的动词选哪个 ⇒ 本条。**
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组（打包）· `I caught up with him last week. I met at college.`——两句动词不同：caught up with（合法，题面没排除 ⇒ ✅ ＋ 当场改题面）／met（认识）
  ｜⚠️ `I met at college` 少了宾语 ⇒ `we met at college`／`I met him at college`，只进 diff，不建号
- 2026-09-13 📝 题面整改：补（⛔ 不许用 catch up）· 复检判定后（§3.3「答得合法但不是条目预期 ⇒ ✅ ＋ 当场改题面」）
  她答 `caught up with him` 合法且符合题面，但本条要分的是 see sb／meet／meet up 三个动词 ⇒ 补排除项，下次逼出 saw him
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉"用不同的动词／⛔ catch up"，两个中文块各配中文释义（老熟人 ／ 第一次认识）—— see／meet 的分工靠释义逼出来
- 备注 `hadn't MET FOR LONG` 意思反了；说"很久"这个量一律 for ages／for a long time，
  for long 只在"没持续多久"里出现（I didn't stay for long.）
- 备注 **捆绑条目**（see／meet／meet up ＋ for ages）：08-19 出现"块的一半对一半错" ⇒
  下个付息日按"一条＝一个考点"拆开，否则她要为已经会的 meet 陪着 for ages 一起重测

### 167 · be in a hurry 的主语必须是人；There's no rush.
类型 搭配 ｜ 旧号 B256
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-18** ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-19 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零。★ 今天回标成「题型 整句」才从词组串里单独拎出来 —— 旧口径按「类型 搭配」打包，主语根本不出现、考点永远测不到）

**问题是什么**
**be in a hurry 的主语只能是人**（I'm in a hurry ／ he's in a hurry）—— 事情和时间不会"赶"，
⛔ 不能说 It isn't in a hurry；"这件事不急"要换一个框：**There's no rush.**（＝ There's no hurry.）
一条规则两个落点：主语是人 ⇒ in a hurry ｜ 主语是"这件事" ⇒ There's no rush。
同一格里的邻居（别串）：`Take your time.` 完全合法，但它绕开了 There's no rush ⇒ 题面正向点名 There's 起头。
判据一句话：这句的主语是人还是事？人 ⇒ in a hurry；事 ⇒ There's no rush。

**怎么发现的**
旧 B 表迁移（B256，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ✅ `there's no rush. I'm in a rush, so I have to head out now.`（两半都对）⇒ 毕业。
2026-09-11 付息日 a2 第 2 组复检：她答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**。
★ 本条今天正是因为回标成「题型 整句」才从词组串里拎出来单独出的 —— 塞在词组串里主语根本不出现，考点测不到。

**我错在哪**
她的：答"忘了"（2026-09-11 复检）　　正确：`There's no rush. ／ I'm in a hurry, so I'd better go.`
找法：说"赶时间"之前先看主语 —— 是人就 in a hurry，是"这件事不急"就换成 There's no rush。

**题面**
"你慢慢挑，一点都不着急。" ／ "我还要赶火车，得先走了。"（第一句用 **There's** 起头，第二句"赶"用 **hurry** 说）

- 2026-08-17 ✅
- 2026-08-19 ✅ `there's no rush. I'm in a rush, so I have to head out now.`（两半都对）
- 2026-09-11 ❌ 复检 · 付息日 a2 第 2 组 · 答"忘了" ⇒ **回潮**
  最小改 `There's no rush. ／ I'm in a hurry, so I'd better go.`
  ❌ **be in a hurry 的主语只能是人**（I'm in a hurry／he's in a hurry）—— 事情和时间不会"赶"，
    ⛔ 不能说 It isn't in a hurry；"不急"这件事本身换一个框：**There's no rush.**（＝ There's no hurry.）
  ★ 一条规则两个落点：主语是人 ⇒ in a hurry；主语是"这件事" ⇒ There's no rush
  ★ 本条今天正是因为回标成「题型 整句」才从词组串里拎出来单独出的 —— 塞在词组串里主语根本不出现，考点测不到
- 2026-09-11 📝 题面整改：补（⛔ 不许用 take your time）· 发题前审核（§6.5 第 7 项）
  `Take your time.` 完全合法，绕开 There's no rush ⇒ 补排除项
- 2026-09-13 📝 题面整改：补（第一句用 **There's** 起头）· 发题前审核（§6.5 第 7 项）
  `No need to hurry.`／`You don't have to hurry.` 都合法，绕开 There's no rush 这个框 ⇒ 用起头词收敛（§6② 提示不改题型，仍是整句）
- 2026-09-13 ❌ 学习日 在池第 1 组 · `no need to rush. I'm in a hurry, I have to go.`
  最小改 `There's no rush. I'm in a hurry, I have to go.`
  ❌ 第一句题面点名 There's 起头，她给的 no need to rush 合法但 There's no rush 这个框没出来 ＝ 没到考点；
    第二句 I'm in a hurry（主语是人）那半格对
- 2026-09-15 ✅ 学习日 在池第 1 组 · `There is no rush. I'm in a hurry, so I've gotta to go.` —— There's no rush 框 ＋ I'm in a hurry 主语是人，两个落点都到；连错2 → 连对1
  ｜同句 gotta to go：教练建 #342 后她当场说明手滑 ⇒ 撤销、不建条目、不记档位（§2）
- 2026-09-18 📝 题面整改：排除项补 `／need` · 发题前审核（§6.5 第 7 项）
  `There's no need to rush.` 同样 There's 起头、同样合法，绕开 There's no rush 这个框 ⇒ 补排除项
- 2026-09-18 ✅ 学习日 在池第 1 组 · `there is no rush. I'm in a hurry, I've gotta go.`——There's no rush（事）＋ I'm in a hurry（人）两个落点都到 ⇒ **连对 2，毕业**
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉负向排除，第一句正向点名 There's 起头；换成挑东西／赶火车两个新场景
- 2026-10-01 📝 题面补点名「第二句"赶"用 **hurry** 说」· 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  第二句只给中文时 `I've got a train to catch` 同样合法，绕开"主语是人 ⇒ in a hurry"这个落点 ⇒ 补正向点名；
  第一句答 There's no hurry 与 There's no rush 同属本条正确形
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [4] · `There's no rush — take your time. I need to hurry to catch my train, so I gotta get going.` —— There's no rush（事）＋ I need to hurry（人当主语）两个落点都到
- 备注 同族"块记了一半"：`stood on their feet`（该 be on your feet）

### 168 · tick things off a list（打卡式旅游）
类型 词组 ｜ 旧号 B257 ｜ ⭐ 她想说卡住、📖 给的
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 词组

**问题是什么**
**tick things off a list** ＝ 打卡式旅游（完整块是 tick things off **a list**，清单单数）。
同一格里的邻居（别串）：**check** off 同样地道、⛔ 不是错（09-11 她答的就是它，判 ✅）——
本条的目标形式是英式／雅思默认的 **tick**，所以当天补了 ⛔ check 把它逼出来；
并列时 taking a photo and moving on 更齐。
判据一句话：这一层用"从清单上划掉"这个画面说，动词优先 tick。

**怎么发现的**
旧 B 表迁移（B257，2026-08-18；⭐ 她想说卡住、📖 给的），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ✅ `their trips are just about ticking off lists`（08-17 还是 📖 给的，今天自己调出来了）⇒ 🎓 零 ❌ 线毕业。
2026-09-11 复检 ✅ `Traveling is just checking things off a list.`——带 list 的块整个调出来了 ⇒ 记 ✅；同日补 ⛔ check。

**我错在哪**
她的：本条历史里没有掉过（🎓 零 ❌ 线）；08-17 那次这个块是教练 📖 给的。触发原话未存。
找法：说"打卡式旅游"时先落"从清单上划掉"这个画面，动词用 tick off。

**题面**
"旅游就是打卡"（"打卡"用一个带 **list** 的块说）

- 2026-08-17 ✅
- 2026-08-19 ✅ `their trips are just about ticking off lists`（08-17 还是 📖 给的，今天自己调出来了）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `Traveling is just checking things off a list.`
  —— 带 list 的块整个调出来了，符合题面 ⇒ 记 ✅（§3.3 硬顺序②）
  ⚠️ 但她用的是 check off，本条目标形式是 **tick** off（英式/雅思默认）——两个都地道、⛔ 不是错
  ⇒ 同日 📝 改题面补 ⛔ check（§3.3 硬顺序③），下次才逼得出 tick
- 2026-09-11 📝 题面整改：补 ⛔ 不许用 check · **判定时**暴露（§3.3 硬顺序③）
  她答 `checking things off a list` —— 完全合法、完全符合题面（"用一个带 list 的块说"）⇒ 记 ✅，
  但本条目标形式是 **tick** things off a list（英式/雅思默认）⇒ 补排除项，下次才逼得出 tick。
  ★ check off 与 tick off **都地道**，这不是纠她的错，是把条目的目标形式钉死
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ① 同级说法
  check things off a list 同样地道（09-11 她答的就是它、判 ✅），tick 只是英式偏好 ⇒ 中译英里产不出 ❌；块本身她已会、历史零 ❌
- 备注 完整块是 tick things off **a list**（清单单数）；并列时 taking a photo and moving on 更齐

### 169 · 不带 if 的条件句：[量/程度短语] ＋ and ＋ [结果]
类型 结构 ｜ 旧号 B258
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 退池 ｜ 题型 整句

**问题是什么**
**不带 if 的条件句：[量/程度短语] ＋ and ＋ [结果]**：
`**Another week and** I'd miss home.` ／ `**A little more expensive and** I wouldn't buy it.`
· and 前面只能放**比较级或量**（ten minutes EARLIER）
· would（假设）vs will（真打算）
· **and 是关节**，⛔ 不能用逗号代替
同一格里的邻居（别串）：`If I stayed one more week, I'd get homesick.` 完全合法，却绕开这个结构
⇒ 2026-09-11 题面补了「两句都 ⛔ 不许用 if」。
判据一句话：想说"再…一点就…"时，先摆一个量／比较级，再用 and 接结果。

**怎么发现的**
旧 B 表迁移（B258，2026-08-18），原始触发原话未存；
最早记录 2026-08-16 📝 drill 两轮 10 题**结构零错误 ⇒ 已装上**（掉的全是词）。
2026-08-19 ✅ `Another week and I'd miss home.`（[量]＋and＋[结果] ＋ would 表假设，三点全中）⇒ 🎓 零 ❌ 线毕业。
2026-09-11 复检 ✅ 两句都成、都没碰 if。

**我错在哪**
她的：本条历史里没有掉过（🎓 零 ❌ 线），触发原话未存。
找法：说"再…就…"时先摆量／比较级，再用 **and** 接结果 —— ⛔ 别顺手写 if，⛔ 别用逗号顶替 and。

**题面**
"再多待一周我就想家了。" ／ "再贵一点我就不买了。"（两句都 ⛔ 不许用 if）

- 2026-08-16 📝 drill 两轮 10 题 **结构零错误 ⇒ 已装上**（掉的全是词）
- 2026-08-17 ✅
- 2026-08-19 ✅ `Another week and I'd miss home.`（[量]＋and＋[结果] ＋ would 表假设，三点全中）
  ⚠️ 第二句她改用了 if 虚拟句（语法完全正确，只是没走本条要练的省 if 版本），不记错
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `Anther one week and I'd miss home. A little more expensive and I wouldn't buy it.`
  —— [量/程度短语] ＋ and ＋ [结果] 两句都成，考点完全命中，两句都没碰 if
  ⚠️ 顺带（不计档位、⛔ 不建条目）：`Another one week` → Another week ／ One more week
    （another 后面直接跟名词，⛔ 中间不夹 one）—— 同题第二句 `A little more expensive` 构造完全正确 ⇒ 这次是拼串，不是缺口
  ✏️ 拼写 Anther→Another（§2.1 不算错）
- 2026-09-11 📝 题面整改：补（两句都 ⛔ 不许用 if）· 发题前审核（§6.5 第 7 项）
  `If I stayed one more week, I'd get homesick.` 完全合法，绕开「不带 if 的条件句」⇒ 补排除项。
  ⛔ 未点名 and 那个结构（考点本身）
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ① 同级说法
  `If I stayed one more week, I'd get homesick.` 完全合法（条目自己写着），[量] ＋ and 只是另一种句式 ⇒ 中译英里产不出 ❌；历史零 ❌
- 备注 and 前面只能放比较级或量（ten minutes EARLIER）；would（假设）vs will（真打算）；and 是关节，不能用逗号代替

### 170 · 并列人称在介词后/宾语位置一律用宾格 me
类型 语法 ｜ 旧号 B259
状态 连对2 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个也毕业了"）｜ 题型 整句

**问题是什么**
**并列人称在介词后／宾语位置一律用宾格 me**：
`it's for my wife and **me**.`（介词后）／ `**My wife and I** go together.`（主语位用主格）。
判据：把"我太太和"去掉、只留一个人念一遍 —— for **me** ✓ ／ for I ✗。
判据一句话：看这个人称站在哪个位置 —— 介词后／宾语位 ⇒ me，主语位 ⇒ I。

**怎么发现的**
旧 B 表迁移（B259，2026-08-18）；最早记录 2026-08-17 ❌ 建号当天，触发原话未存。
2026-08-19 ✅ ／ 2026-08-20 ✅ 宾格／主格两个位置都对 ⇒ 她当场指定毕业（"这个也毕业了"）。
2026-09-05 复检 ✅ 介词后 for my wife and **me** ／ 主语位 My wife and **I**。
★ 尾部备注记着：建号后隔一题她就用对了（迁移窗口）。

**我错在哪**
她的：2026-08-17 建号当天记过一次 ❌，触发原话未存。
找法：把"我太太和"去掉，只留一个人念一遍 —— 念得通的那个形式就是对的。

**题面**
"这是给我太太和我的。" ／ "我太太和我一起去的。"（两句都说）

- 2026-08-17 ❌ 建号当天
- 2026-08-19 ✅ `it is for my wife and me.` ＋ `My wife and I go together.`（宾格/主格两个位置都对）
- 2026-08-20 ✅ `it's for my wife and me. my wife and I go together.`——宾格/主格两个位置又都对
  ⚠️ 第二句时态 go／went：题面"一起去的"过去与习惯两读都成立 ⇒ **题面歧义，不判错**；
     要测过去时得把题面写成"那次我太太和我是一起去的"
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· 两个位置都对：介词后 for my wife and **me**（宾格）
  ／主语位 My wife and **I**（主格）
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 备注 建号后隔一题她就用对了（迁移窗口）

### 171 · 要把"跟谁说"说出来就得用 tell sb（say 后面不接人）
类型 搭配 ｜ 新建 2026-08-19
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
**要把"跟谁说"说出来就得用 tell sb**（say 后面不接人）：`he didn't **tell me** before he left.`
判据：say 后面直接接人不成立（say me ✗）；要出现人就换 **tell sb sth** ／ **say sth TO sb**。
判据一句话：句子里要带上"跟谁" ⇒ 动词换成 tell。

**怎么发现的**
2026-08-19 新建 · 复习 #147 句里 · 触发原话 "也没跟我说他要走" → `didn't say he was going to leave`（"我"整个漏掉）。
2026-08-21 ✅ ／ 2026-08-23 ✅ `he didn't tell me before leaving.` ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `didn't tell me`。

**我错在哪**
她的：`didn't say he was going to leave`（2026-08-19）　　正确：`he didn't **tell me** before he left.`
找法：中文里出现"跟我／跟他"这个人时，动词先定成 tell。

**题面**
"他辞职之前都没跟我们说一声。"
　　★ 零提示：tell us／say anything to us／give us a heads-up 都算对；她掉过的是把"跟我们"整个丢掉（didn't say …）

- 2026-08-19 新建 · 复习#147 句里 · "也没跟我说他要走" → `didn't say he was going to leave`（漏掉"我"）
- 2026-08-21 ✅ 复习（点名题面首测）· `he didn't tell me before he left.`——tell ＋ 人、语序对、两分句时态平面一致
- 2026-08-23 ✅ 付息日 a 段 · `he didn't tell me before leaving.`——tell ＋ 人一字不差；
  `before leaving` 的分词逻辑主语 ＝ 主句主语 he，挂对了 → **连对2，毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `didn't tell me` —— 要把"跟谁说"说出来就得用 tell sb
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）· 题型 词组 → 整句
  考点是"跟我们"这个人有没有说出来 ＝ 靠句子现形；零提示（tell us／say anything to us 都对），换成辞职场景
- 备注 say 后面直接接人不成立（say me ✗）；要出现人就换 tell sb sth／say sth TO sb

### 172 · 机会用 get：get the chance to do（不用 have a chance）
类型 搭配 ｜ 新建 2026-08-19
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-21** ｜ 退池 ｜ 题型 词组

**问题是什么**
**机会用 get：get the chance to do**（⛔ 不用 have a chance）：`if I **get the chance**, I'd love to see it`。
同一格里的邻居（别串）：`a chance` 与 `the chance` **两个都成立**（get a chance／get the chance 同样常用），冠词⛔ 不是考点；
have a chance 更多用在"有可能性"（There's a chance it'll rain）。
判据一句话："有机会做某事"默认动词是 **get**。

**怎么发现的**
2026-08-19 新建 · 复习 #140 句里 · 触发原话 `if I have a chance`（→ if I (ever) get the chance）。
2026-08-20 ✅ ／ 2026-08-21 ✅ ⇒ 连对 2，毕业。
2026-09-11 复检 ✅ `check it out if you get the chance`——⛔ 没写 have a chance。

**我错在哪**
她的：`if I have a chance`（2026-08-19）　　正确：`if I (ever) **get** the chance`
找法：说"有机会…"时动词先落 get，⛔ 别顺手用 have。

**题面**
**点名**："有机会去看看"（"有机会"用 get 说）

- 2026-08-19 新建 · 复习#140 句里 · `if I have a chance` → if I (ever) get the chance
- 2026-08-20 ✅ 复习（新建后首测）· `if i get the chance, I'd love to see it`——get the chance 一字不差
- 2026-08-21 ✅ 复习 · `If i get a chance someday I want to go see it.`——考点是动词选 **get** 不选 have
  → **连对2，毕业**
  ★ `a chance` vs `the chance`：**两个都成立**（get a chance／get the chance 同样常用），
    本条的对比对象是 have a chance，冠词不是考点 ⇒ 不判
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `check it out if you get the chance` —— "有机会"走 get the chance，⛔ 没写 have a chance
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ① 同级说法
  `If I have the chance, I'd love to …` 本身完全地道，get the chance 只是更常用 ⇒ 中译英里产不出 ❌（08-19 那次 have a chance 也不是错）
- 备注 have a chance 更多用在"有可能性"（There's a chance it'll rain）；"有机会做某事"默认 get

### 173 · X makes me …（实义动词盖住整个评价槽，不用 is）
类型 结构 ｜ 旧号 B12
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**X makes me …** —— 用**实义动词**盖住整个评价槽，⛔ 不用 be 动词：
`the two hours **made** the whole day worth it`。
同一格里的邻居（别串）：`Because of those two hours, the whole day **was** worth it.` 完全合法，
但评价槽用了 be 动词、考位就没了 ⇒ 2026-09-09 题面点名「用 **make** 说」。
★ 点名的是**动词**、⛔ 不是结构：made ＋ 宾语 ＋ 补语这一整块仍要她自己搭（与 #104「用 bury 说」同规格）。
判据一句话：评价那一层能不能由一个实义动词扛住？能就别退回 is。

**怎么发现的**
旧 B 表迁移（B12，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 3 组 ✅ `the two hours made the whole day worth it`（题面当天刚补点名）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：想说"…让…变得怎样"时先找一个实义动词扛住评价槽（make／bore／bring），⛔ 别退回 is。

**题面**
"这两小时让一整天都值了。"（用 **make** 说）

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-09 📝 题面整改 · 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面可合法译成 `Because of those two hours, the whole day was worth it.` —— 评价槽用 be 动词，
  本条考的"实义动词盖住整个评价槽"就没考位 ⇒ 点名「用 **make** 说」
  ★ 点名的是动词，⛔ 不是结构：made ＋ 宾语 ＋ 补语这一整块仍要她自己搭（与 #104「用 bury 说」同规格）
- 2026-09-09 ✅ 复检 · 第 3 组 · `the two hours made the whole day worth it`
- 2026-09-20 ⚡ 自评免测 · 复检第 3 组（她答"直接过"）
- 2026-09-29 📝 退池 · ① 同级说法
  `the whole day was worth it` 完全合法（条目自己写着），用 make 扛评价槽只是风格升级 ⇒ 中译英里产不出 ❌；历史零 ❌

### 174 · as … as it gets（用原级避开比较级形态）
类型 词组 ｜ 旧号 B25
状态 连对3 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

**问题是什么**
**as … as it gets** ＝ 用原级避开比较级形态（"已经是最…的了"）：`running is **as simple as it gets**`。
· 这个块**不随句子变过去式**（08-12 她写成 `as simple as it got` ⇒ 回潮）
· 边界：as…as it gets ≠ "尽量…"（那是 as…as possible）
同一格里的邻居（别串）：`Running couldn't be simpler.` 合法，但走的是**比较级**，而本条的立身之本正是用原级
⇒ 2026-09-05 题面点名到 as … as 那个块 ＋ 明写 ⛔ 不用比较级。
判据一句话：这个块是**固定形**，永远 as … as it **gets**。

**怎么发现的**
旧 B 表迁移（B25，2026-08-18）；最早记录 2026-08-12 ❌ 回潮 · 触发原话 `as simple as it got`。
2026-08-13 ✅ ／ 2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 1 组（打包）✅ `running is as simple as it gets`——原级，⛔ 没落进比较级。

**我错在哪**
她的：`as simple as it got`（2026-08-12）　　正确：`as simple as it **gets**`
找法：这个块整块调、时态不跟着句子走 —— 永远是 gets。

**题面**
"那次露营的装备简单到不能再简单了，就一顶帐篷一个睡袋。"（用 **as simple as it** 说）

- 2026-08-12 ❌ 回潮：写成 `as simple as it got`（这个块不随句子变过去式）
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-05 📝 题面整改 · 复检组第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面 "跑步简单到不能再简单。" 可以译成 `Running couldn't be simpler.`（合法，比较级）——
  而本条的立身之本正是**用原级避开比较级形态** ⇒ 绕开就测不到。
  ⇒ 点名到 as … as 那个块 ＋ 明写 ⛔ 不用比较级，⛔ 未给出 as simple as it gets。
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· `running is as simple as it gets` 原级，⛔ 没落进比较级
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组（打包）· `as simple as it gets`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"⛔ 不用比较级"，点名 as simple as it，句尾 gets 留给她；故意用过去的场景 —— 她掉过的正是跟着句子写成 got
- 备注 边界：as…as it gets ＝"已经是最…的了"，不等于"尽量…"（那是 as…as possible）

### 175 · grow vs grow up（grow up 只用于人长大成人）
类型 词汇 ｜ 旧号 B31a
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 词组

**问题是什么**
**grow vs grow up** —— **grow up 只用于人长大成人**；植物／数量变大一律 **grow**：`grow day by day`。
同一格里的邻居（别串）：get bigger／get taller 也合法，但动词槽位被绕开、这组分工就测不到
⇒ 2026-09-07 题面补点名「用 grow 说」。
判据一句话：主语是人、说的是"长大成人" ⇒ grow up；其余一律 grow。

**怎么发现的**
旧 B 表迁移（B31a，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-07 复检第 5 组（打包）✅ `grow day by day`（植物用 grow，⛔ 没落进 grow up）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写 grow 之前看主语 —— 只有人"长大成人"才加 up。

**题面**
"这些植物一天天长"（用 **grow** 说）

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-07 📝 题面补点名「用 grow 说」：原题面可合法译成 get bigger / get taller，动词槽位被绕开 ⇒
  grow / grow up 的分工（本条考点）测不到。
- 2026-09-07 ✅ 复检 · 第 5 组（打包）· `grow day by day`（植物用 grow，⛔ 没落进 grow up）
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；grow／grow up 的分工她一直对

### 176 · efficient（省时间人力）vs effective（达到效果）
类型 词汇 ｜ 旧号 B46
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **回潮 2026-09-05**（08-17 毕业 → 09-05 复检用 works well 绕开形容词槽位，形容词一次没出现，撤销毕业、连对清零） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
**问题是什么**
**efficient（省时间人力）vs effective（达到效果）**：
判据：effective ＝ 达到效果（有没有用）／ efficient ＝ 省时间省人力（快不快、省不省）。
`The drug is pretty **effective**.`
同一格里的邻居（别串）：`works well` 完全合法，但它**绕开形容词槽位** —— 09-05 掉的正是这一点
（不是分不清这一对，是压力下用 works well 躲开了）；works well／useful 本身都合法。
判据一句话：问的是"有没有用" ⇒ effective；"省不省事" ⇒ efficient。

**怎么发现的**
旧 B 表迁移（B46，2026-08-18）；最早记录 2026-08-11 ❌ · 触发原话 `the most efficient ways to keep up`（该 effective／best）。
2026-08-17 ✅ ⇒ 毕业。
2026-09-05 ❌ 复检（打包）· `the drug works pretty well` —— 题面点名"写出那个形容词"，形容词一次没出现 ⇒ **回潮**。
2026-09-07 ✅ `effective`；2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。

**我错在哪**
她的：`the most efficient ways to keep up`（08-11）／ `the drug works pretty well`（09-05，形容词整个没出现）
正确：`the most **effective** ways …` ／ `The drug is pretty **effective**.`
找法：先问这句说的是"有没有用"还是"省不省事"，再把那个**形容词**说出来 —— ⛔ 别用 works well 躲过去。

**题面**
"这种背单词的方法对我特别有效，就是挺花时间的。"
　　★ 零提示：effective／works well 都算对；"花时间"那半句正好把 efficient 放进对照 —— 她掉过的是把 efficient 当成"有效"

- 2026-08-11 ❌ `the most efficient ways to keep up` → 该 effective/best
- 2026-08-12 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-05 📝 题面整改 · 复检组第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面 "这药挺管用。" 可以译成 `This medicine works well.`（合法，绕开形容词）——
  而本条考的就是 efficient ／ effective 的**选词** ⇒ 不出形容词就没有考位。
  ⇒ 点名"写出那个形容词"，⛔ 未说是哪一个。
- 2026-09-05 ❌ 复检组 · 第 1 组（打包）· **回潮**
  `the drug works pretty well` → The drug is pretty **effective**.
  ❌ 题面点名"写出那个形容词"，形容词一次没出现 ⇒ 考位没测到，按"没调出来"记。
  ★ 判据：effective ＝ 达到效果（有没有用）／efficient ＝ 省时间省人力（快不快、省不省）。
  ★ 掉的是哪一格：**不是分不清这一对，是压力下用 works well 绕开了形容词槽位**
    ⇒ 回潮后的复测必须继续钉死"写出那个形容词"，否则测不到。
  ｜ ⚠️ 顺带：drug → medicine（日常吃的药用 medicine；drug 口语默认偏毒品），diff-2 已给，不记 ❌
- 2026-09-07 ✅ 复习 · 在池第 1 组 · `effective`
- 2026-09-09 ⚡ 自评免测 · 在池第 1 组（她原话："这 10 个题直接过吧，算对"）
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）· 题型 词组 → 整句
  去掉"⛔ useful／helpful"，改成零提示整句：effective／works well 都算对，"花时间"半句把 efficient 放进对照 —— 她 08-11 掉的正是拿 efficient 当"有效"

### 177 · 名词表语（a waste of time／a must／a plus）
类型 结构 ｜ 旧号 B51
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**名词表语**：a waste of time ／ a must ／ **a plus** —— `Japanese is **a plus**.`
同一格里的邻居（别串）：`It helps if you know Japanese.` 完全合法，但名词表语那一格根本没出现
⇒ 2026-09-09 题面加结构限定「表语用**名词**说」（⛔ 未给出 a plus／a must／a waste of time 中的任何一个）。
判据一句话：能用一个**名词**当表语说完的，就别展开成从句。

**怎么发现的**
旧 B 表迁移（B51，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 3 组 ✅ `Japanese is a plus`——名词表语到位。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"是个加分项／是浪费时间"时先找那个名词（a plus／a waste of time），⛔ 别改成从句。

**题面**
"会日语是加分项。"（表语用**名词**说）

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-09 📝 题面整改 · 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面可合法译成 `It helps if you know Japanese.` —— 名词表语那一格根本没出现
  ⇒ 加结构限定「表语用**名词**说」；⛔ 未给 a plus／a must／a waste of time 里的任何一个
- 2026-09-09 ✅ 复检 · 第 3 组 · `Japanese is a plus` —— 名词表语到位
- 2026-09-20 ⚡ 自评免测 · 复检第 3 组（她答"直接过"）
- 2026-09-29 📝 退池 · ① 同级说法
  `It helps if you know Japanese.` 完全合法（条目自己写着），名词表语 a plus 只是另一种说法 ⇒ 中译英里产不出 ❌；历史零 ❌

### 178 · only／all／最高级后面用 that 不用 which
类型 语法 ｜ 旧号 B64
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**only／all／最高级后面用 that 不用 which**：`That's the **only** part **that** truly belongs to you.`
判据一句话：先行词前面挂着 only／all／最高级 ⇒ 关系词一律 that。

**怎么发现的**
旧 B 表迁移（B64，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ❌。
2026-08-13 ✅ ／ 2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 1 组 ✅ `That's the only part that truly belongs to you.`——⛔ 没用 which。

**我错在哪**
她的：2026-08-12 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：写关系词前先看先行词前面有没有 only／all／最高级 —— 有就只能用 that。

**题面**
"那是唯一真正属于你自己的部分。"（"属于"用 **belong** 说 · 用一个关系从句说，关系词不许省）

- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `That's the only part that truly belongs to you.` —— only 后面用 that，⛔ 没用 which
- 2026-09-18 📝 题面整改：补（"属于"用 belong 说 · 用一个关系从句说，关系词不许省）· 复检组发题前审核（§6.5 第 7 项）
  `That's the only part you really own.` 省掉关系词，合法且完全绕开 that／which ⇒ 用 belong 逼出主语关系从句，并写明关系词不许省
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ① 同级说法（原规则过严）
  "the only part which …"在现代英语里并不算错（only 后用 that 只是偏好），口语里更常直接省掉关系词 ⇒ 中译英里产不出真错；08-12 那次 ❌ 原话未存

### 179 · that ＋ 形容词 ＝ "那么…"
类型 语法 ｜ 旧号 B65
状态 连对3 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 词组

**问题是什么**
**that ＋ 形容词 ＝ "那么…"**：`It's not **that** simple.` ／ `It's actually not **that** hard.`
判据一句话：中文"没那么…"里的那个"那么"就是 **that**，直接贴在形容词前面。

**怎么发现的**
旧 B 表迁移（B65，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ❌。
2026-08-13 ✅ ／ 2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 1 组 ✅ 两句都对。

**我错在哪**
她的：2026-08-12 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：中文"没那么…"里的"那么"直接落一个 that，贴在形容词前面。

**题面**
"没那么简单" ／ "其实没那么难"（⛔ 不许用 so／such）

- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `It's not that simple. It's actually not that hard.` —— that ＋ 形容词，两句都对
- 2026-09-13 📝 题面整改：补（⛔ 不许用 so／such）· 复检组发题前审核（§6.5 第 7 项）
  `not so simple`／`not that simple` 都合法，so 绕开 that＋形容词 ⇒ 补排除项
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组（打包）· `it's not that simple. it's not that hard.`
- 2026-09-29 📝 退池 · ① 同级说法
  "没那么简单"说 not so simple 同样成立（旧题面靠"⛔ so／such"硬框），that ＋ 形容词只是更口语 ⇒ 中译英里产不出 ❌；08-12 那次 ❌ 原话未存

### 180 · eat out ＝ 出去下馆子
类型 词组 ｜ 旧号 B72
状态 连对3 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 词组

**问题是什么**
**eat out ＝ 出去下馆子**（两个词，⛔ 不绕 go to a restaurant）。
同一格里的邻居（别串）：**out ≠ outside** —— "在外面吃"的"外"＝ 不在家/不在公司 ⇒ out
　（eat out ／ grab a bite out）；outside ＝ 户外、建筑物外面（eat outside ＝ 坐在院子里吃）。
判据一句话："出去吃饭"这一层用 eat out 一个块说完。
⚠️ 题面沿革（2026-09-05 发现）：**原题面根本测不到本条考点** ——
　条目是 eat out，题面却是"做两小时，十分钟就吃完了。"，那句里没有"出去吃"这层意思
　⇒ 08-13／08-15／08-17 那三次 ✅ **等于白测**；⛔ 不改历史判定（不知道她当时逐字答了什么，回头改判就是编）。

**怎么发现的**
旧 B 表迁移（B72，2026-08-18），原始触发原话未存；最早记录 2026-08-12 📝 △ 有更好的说法（不加不清）。
2026-08-13 ✅ ／ 2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业（三次用的都是测不到本条的旧题面，见上）。
2026-09-05 📝 题面改为"出去下馆子"（不用 restaurant 那个词说）；2026-09-09 复检第 3 组 ✅ `eat out`。

**我错在哪**
她的：本条判定里没有掉过；09-05 之前那三次是旧题面下的白测。触发原话未存。
找法：说"出去吃饭"时直接给 eat out 这两个词。

**题面**
"出去下馆子"（不用 restaurant 那个词说）

- 2026-08-12 📝 △ 有更好的说法（不加不清）
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-05 📝 题面整改 · 付息日 c 段（题面粒度整改的顺带发现，⛔ 不是粒度问题）
  **原题面测不到本条考点**：条目 ＝ eat out（出去下馆子），题面却是 "做两小时，十分钟就吃完了。"
  —— 那句话里根本没有"出去吃"这层意思，怎么翻都碰不到 eat out ⇒ 08-13／08-15／08-17 那三次 ✅
  **等于白测**（她当时答的是别的东西）。
  ⇒ 题面改为 "出去下馆子"（不用 restaurant 那个词说）——块级粒度 ＋ 排除项收敛到 eat out。
  ★ ⛔ **不改历史判定**：不知道她当时逐字答了什么，回头改判就是编（§7 四问①）。
    本条已在复检队列里，按新题面重测一次即可。
- 2026-09-09 ✅ 复检 · 第 3 组 · `eat out`
- 2026-09-20 📝 学习日 在池第 1 组（#347）· 她说 `grab a quick bite outside` ⇒ 给了 eat out／grab a bite **out**
  ⛔ 不判回潮：本题题面没要求产出它，grab a quick bite 本身合法（§3.3 回潮限于复检 ❌ 或自由产出里掉）
  ⇒ 本日复检组里 #180 当场弃（刚被教练给过答案，再测就是白测）
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ① 同级说法
  "出去下馆子"说 go out for dinner／go to a restaurant 都完全成立，eat out 只是其中一个（09-05 前三次还是题面测不到的白测）⇒ 中译英里产不出 ❌

### 181 · every time／whenever 引导的从句 → 主句用现在时
类型 语法 ｜ 旧号 B90
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**every time／whenever 引导的从句 → 主句用现在时**：
`I **have to wait** for an hour **every time I order** takeaway.`（主句与从句同在现在时平面）
同一格里的邻居（别串）：#184 管的是"every time 后面必须跟完整从句"，本条管**主句的时态**。
判据一句话：every time／whenever 说的是一般规律 ⇒ 两边都用一般现在时。

**怎么发现的**
旧 B 表迁移（B90，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-11 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 3 组 ✅ 主句与从句同在现在时平面。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写完 every time／whenever 从句，回头看主句是不是也停在现在时。

**题面**
"我每次点这家外卖都要等一个小时。"

- 2026-08-09 ✅
- 2026-08-11 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 3 组 · `I have to wait for an hour every time I order takeaway` —— 主句与从句同在现在时平面
- 2026-09-20 ⚡ 自评免测 · 复检第 3 组（她答"直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；every time 从句配现在时她一直对（时态类、从没掉过）

### 182 · by ＋ -ing ＝ 通过做某事达成结果
类型 结构 ｜ 旧号 B91
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**by ＋ -ing ＝ 通过做某事达成结果**：`passed the exam **by studying** …` ／ `save money **by walking**`。
同一格里的邻居（别串）：⚠️ by -ing 的**逻辑主语必须是人** —— `It can save…` 会挂空，该 `You can save…`（⛔ 不落号）。
判据一句话：说"靠做某事…"时介词用 by、后面挂 -ing，主句主语要跟那个动作同一个人。

**怎么发现的**
旧 B 表迁移（B91，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组 ✅ 两句 by ＋ -ing 都在。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅）；09-05 唯一的顺带是 by walking 的逻辑主语挂空（⛔ 不落号）。触发原话未存。
找法：写完 by ＋ -ing，回头看主句主语是不是做那个动作的人。

**题面**
"他每晚学习，就这么过的考试。" ／ "走路上班能省不少钱。"（两句都用 **by ＋ -ing** 说）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `passed the exam **by studying** … save money **by walking**` 两句 by ＋ -ing 都在
  ｜ ⚠️ `It can save…` 主语挂空（by walking 的逻辑主语是人）⇒ 该 You can save…；不落号
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；by ＋ -ing 她一直对

### 183 · save sb money／sth（带间接宾语）
类型 搭配 ｜ 旧号 B92
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-11** ｜ 退池 ｜ 题型 词组

**问题是什么**
**save sb money／sth（带间接宾语）**：`this app can save **you** a lot of time.`
同一格里的邻居（别串）：`This app saves a lot of your time.` 完全合法，但**间接宾语那一格不出现**、考位被绕开
⇒ 2026-09-05 题面补点名（用 **save** ＋ 人在前说）。
判据一句话：save 走双宾语框 —— **人在前、东西在后**。

**怎么发现的**
旧 B 表迁移（B92，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-10 ✅ ／ 2026-08-11 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 4 组（打包）✅ `this app can save **you** a lot of time.`——题面当天补了点名，整改后首测即过。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写完 save 先把"给谁省"那个人放上去，再说省了什么。

**题面**
"给你省不少时间"（用 **save** ＋ 人在前说）

- 2026-08-09 ✅
- 2026-08-10 ✅
- 2026-08-11 ✅
- 2026-09-05 ✅ 复检组 · 第 4 组（打包）· `this app can save **you** a lot of time.` —— 人在前的双宾语框
  ★ 本条题面今天补了点名（用 save ＋ 人在前说），整改后首测即过。
- 2026-09-05 📝 题面整改 · 复检第 4 组发题前审核（§6.5 第 7 项）
  `This app saves a lot of your time.` 完全合法，但**间接宾语那一格不出现** ⇒ 考位被绕开
  ⇒ 补点名（用 **save** ＋ 人在前说）。
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ① 同级说法
  `This app saves a lot of your time.` 完全合法（条目自己写着），双宾语只是另一种说法 ⇒ 中译英里产不出 ❌；历史零 ❌

### 184 · every time／each time 是连词，后面跟完整从句
类型 结构 ｜ 旧号 B94
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**every time／each time 是连词，后面跟完整从句**：`he brings something to eat **every time he comes**.`
同一格里的邻居（别串）：#181 管的是"这种从句在场时主句用什么时态"，本条管**它后面必须跟一个完整从句**。
判据一句话：every time 后面必须有主语 ＋ 谓语，⛔ 不能只挂一个名词。

**怎么发现的**
旧 B 表迁移（B94，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ❌。
2026-08-13 ✅ ／ 2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 1 组 ✅ `he brings something to eat every time he comes.`

**我错在哪**
她的：2026-08-12 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：写完 every time 就接一个完整的主谓，⛔ 别只挂一个名词。

**题面**
"他每次来都带点吃的。"（"每次"用 **every time** 说 · ⛔ 不许用 whenever）

- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `he brings something to eat every time he comes.` —— every time ＋ 完整从句
- 2026-09-15 📝 题面整改 · 复检第 3 组发题前审核（§6.5 第 7 项：Whenever he comes 同样合法，绕开 every time ＋ 从句）
  旧："他每次来都带点吃的。"
  新："他每次来都带点吃的。"（"每次"用 **every time** 说 · ⛔ 不许用 whenever）
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存；08-12 那次 ❌ 无从确认，此后四次全对；every time ＋ 完整从句她一直对（whenever 也同样成立）

### 186 · leave a mess（⭐ 她自产）
类型 词组 ｜ 旧号 B97
状态 连对2 连错0 上次2026-09-30 ｜ 回潮 2026-09-09（08-17 毕业 → 09-09 复检答"忘了"，撤销毕业、连对清零）｜ **回潮 2026-09-28**（09-11 第二次毕业 → 09-28 复检答成 `mess up the floor`，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-30**（连对2 ＝ 09-29 ＋ 09-30；09-28 回潮后第三次毕业）｜ 题型 整句

**问题是什么**
**leave a mess**（⭐ 她自产的块，三个词）＝ 弄乱了就走、留给别人收拾。
同一格里的邻居（别串 —— 都合法）：
`He **makes** a mess.`（只说弄乱，没有"留下"那层）· `He **throws** stuff around.` · `leave stuff lying around`
⇒ 几种说法都合法 ⇒ 出整句题、正向点名 **leave**，块里的 **a mess**（冠词 ＋ 名词）留给她自己搭。
判据一句话：这一层用 **leave ＋ a mess** 三个词说完。

**怎么发现的**
旧 B 表迁移（B97，2026-08-18）；⭐ 本条是她自产的块，2026-08-09 首次出现即 ✅。
2026-08-13 ◎ 题面没逼出；2026-08-17 ✅ ⇒ 毕业。
2026-09-09 ❌ 复检第 3 组 · 答"忘了" ⇒ **回潮**（08-17 毕业后三周没再碰）。
2026-09-10 ✅ `he left a mess` ／ 2026-09-11 ✅ `he left a mess` ⇒ 连对 2，第二次毕业。
★ 09-11 发出时题面括号里还带着「**人**当主语说」，与词组题主体打架（**她当场点出**，原话：
"词组只需要单次或者词组，整句（翻译）需要完全的句子"）⇒ 同日删掉该提示；
毛病是形式不是映射、考点 100% 被测到 ⇒ 按 §3.3 硬顺序记 ✅、⛔ 不记 ◎。

**我错在哪**
她的：答"忘了"（2026-09-09 复检）　　正确：`He leaves a mess.`
找法：说"乱丢一地"时直接调 leave a mess 这三个词，⛔ 别滑到 make／throw。

**题面**
"我儿子每次吃完零食，都把客厅弄得乱七八糟就跑了。"（"弄得乱七八糟就跑了"用 **leave** 说）

- 2026-08-09 ✅
- 2026-08-13 ◎ 题面没逼出
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-09 ❌ 复检 · 第 3 组 · 答"忘了" —— **回潮**
  最小改 `He leaves a mess.`
  ★ 本条是 ⭐ 她自产的块（08-09 首次出现），08-17 毕业后三周没再碰 ⇒ 掉了
- 2026-09-10 📝 题面整改：补词数与排除项 · 在池第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面「"东西乱丢一地"（**人**当主语说，⛔ 不许用 everywhere／all over）」——
  `He makes a mess.` 完全合法、完全符合题面，却把本条考点（**leave** a mess 这个搭配）整个绕开；
  `leave stuff lying around` 同理（四个词，绕开 mess 这个名词）。
  ⇒ 补「"乱丢一地"用**三个词**的块说」＋ 排除项 `／make`，把 leave a mess 框死；
    ⛔ 未点名 leave、⛔ 未点名 mess（那是考点本身，§6② 红线）。
- 2026-09-10 ✅ 复习 · 在池第 1 组 · `he left a mess`（另给了 `he left his stuff scattered around`）
  ★ 09-09 答"忘了"回潮，本场题面补了「三个词的块」＋ 排除 make 之后，块整个调出来了
- 2026-09-11 📝 题面整改：排除项补 `／throw` · 在池第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  `He throws stuff around.` ＝ 三个词的块、人当主语、不含已排除的词 ⇒ **完全合法且符合题面**，
  却把 leave a mess 整个绕开（§6 第二译法白测）⇒ 补进排除项。
  ⛔ 仍未点名 leave、⛔ 仍未点名 mess（那是考点本身，§6② 红线）
- 2026-09-11 ✅ 付息日 a 段 · 第 1 组 · `he left a mess` —— 块整个调出来（不是 make／throw）⇒ 连对2 **毕业**
  ★ 发出时题面括号里带「**人**当主语说」，与词组题主体打架（她当场点出）⇒ 同日 📝 整改；
    毛病是形式不是映射，考点 100% 被测到 ⇒ 按 §3.3 硬顺序记 ✅、⛔ 不记 ◎
- 2026-09-11 📝 题面整改：删「**人**当主语说」，恢复成纯词组题 · 她当场点出（原话："词组只需要单次或者词组，整句（翻译）需要完全的句子"）
  旧 "东西乱丢一地"（**人**当主语说 · "乱丢一地"用**三个词**的块说 · ⛔ 不许用 everywhere／all over／make／throw）
  新 "东西乱丢一地"（用**三个词**的块说 · ⛔ 不许用 everywhere／all over／make／throw）
  ⇒ 考点 leave a mess 一个块就覆盖得了 ⇒ 词组题；「人当主语说」这个提示把要她产出的形式改成了整句 ⇒ 越界，删
- 2026-09-18 📝 题面整改：排除项补 `／around` · 复检组发题前审核（§6.5 第 7 项）
  `leave stuff around`／`scatter things around` 同样三个词、合法，绕开 leave a mess ⇒ 补排除项
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 2026-09-28 ❌ 复检第 2 组 · 答成 `mess up the floor`（没调出 leave a mess）—— **回潮**
- 2026-09-29 ✅ 在池第 1 组 · `leave a mess.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  make a mess／throw stuff around 都合法，中文块单独映射不回 leave a mess ⇒ 改整句、正向点名 leave，a mess 留给她搭；
  旧的「三个词 ＋ ⛔ 排除五个词」写法作废（负向排除永远排不完）
- 2026-09-30 ✅ 付息日 a 段在池第 1 组 [1] · `friends leave the kitchen a total mess and just walk away` ⇒ 连对2 **毕业**

### 189 · take sb out ≠ bring sb along；outdoors 是副词
类型 词汇 ｜ 旧号 B101
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**take sb out ≠ bring sb along**；**outdoors 是副词**。
`take my son **out**`——out 是块的一部分（09-05 她写的 `take my son to play outside` 考点已命中，只是不如带 out 自然）。
判据一句话："带某人出去"用 **take sb out**（从这儿带出去）；bring 是"带到我这儿来"。

**怎么发现的**
旧 B 表迁移（B101，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组（打包）✅ `take my son to play outside`——考点 take（⛔ 没落进 bring）命中。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"带某人出去"先定方向 —— 从这儿带走是 take，带到我这儿才是 bring；out 别丢。

**题面**
"带儿子出去玩"（"带…出去"用【一个动词 ＋ 人 ＋ out】说）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `take my son to play outside` —— 考点 take（⛔ 没落进 bring）命中
  ｜ ⚠️ 更自然 take my son **out**（out 是块的一部分），不落号
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；take sb out 的方向她一直对（旧题面还是形态描述）

### 190 · clear the table ≠ clean the table
类型 词汇 ｜ 旧号 B103
状态 连对3 连错0 上次2026-09-13 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

**问题是什么**
**clear the table ≠ clean the table**：clear ＝ 把上面的东西拿走；clean ＝ 擦干净。
同一格里的邻居（别串）：🎓#51 的 put sth away ＝ 把东西**归位**，也跟"擦干净"是两件事。
判据一句话：东西在上面挡着 ⇒ clear；表面脏了要擦 ⇒ clean。

**怎么发现的**
旧 B 表迁移（B103，2026-08-18）；最早记录 2026-08-09 ❌，触发原话未存。
2026-08-10 ✅ ／ 2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 1 组（打包）✅ clear（⛔ 没落进 clean）。

**我错在哪**
她的：2026-08-09 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：说"收拾桌子"先问一句 —— 是把东西拿走（clear）还是把桌面擦干净（clean）？

**题面**
"吃完饭帮忙把桌子收拾了"（把碗盘撤下去，不是擦桌面）

- 2026-08-09 ❌
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· clear（⛔ 没落进 clean）
- 2026-09-13 📝 题面整改：补（⛔ 不许用 tidy／wipe）· 复检组发题前审核（§6.5 第 7 项）
  `tidy the table`／`wipe the table` 都合法、都绕开 clear／clean 那一格 ⇒ 补排除项；⛔ 不排除 clean —— 它正是本条要测的错路
- 2026-09-13 ✅ 复检 · 学习日 复检第 4 组（打包）· `clear the table`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 中文释义收敛）
  去掉"⛔ tidy／wipe"，改成中文释义（把碗盘撤下去、不是擦桌面）—— clear／clean 的分工靠释义逼出来

### 191 · 集合名词单复数都合法（family／audience／team）
类型 语法 ｜ 旧号 B104＋B93
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-11** ｜ 退池 ｜ 题型 整句

**问题是什么**
**集合名词单复数都合法**（family／audience／team）：`My family **spend** a whole day cooking a big meal.`
—— 英式偏复数、美式偏单数，**两边都成立**。
同一格里的邻居（别串）：`all the audience laugh` **按本条是对的**（08-19 那次原 #66 判 ◎ 就是因为这个）；
与 #129（staff 没有复数形式 staffs）**不冲突** —— 那条管**词形**，本条管**动词一致**。
判据一句话：集合名词配单数还是复数都行，⛔ 不许拿这一条判她错。
★ 本条 ＝ 原 #66（audience 作整体时配单数动词）2026-08-19 并入 —— #66 是一条**写错了的绝对化规则**，已撤销。

**怎么发现的**
旧 B 表迁移（B104＋B93，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-10 ✅ ／ 2026-08-11 ✅ ⇒ 连对 3，毕业。
2026-08-17 ◎ ／ 2026-08-19 ◎（都来自原 #66，题面撞车或规则写错，作废）。
2026-09-05 复检第 4 组 ✅ 集合名词配复数谓语（合法的那一边）。

**我错在哪**
她的：本条判定里没有掉过（两次 ◎ 的责任都在条目／题面），触发原话未存。
找法：碰到 family／audience／team 时别纠结 —— 单数复数都算对，只要一句之内保持一致。

**题面**
"我们家过年会做一整天的菜。"（用 **family** 当主语说）

- 2026-08-09 ✅
- 2026-08-10 ✅
- 2026-08-11 ✅
- 2026-08-17 ◎（原 #66，题面撞车作废）
- 2026-08-19 ◎（原 #66）她答 `all the audience laugh` —— **按本条是对的**（英式复数成立，美式偏单数）
- 2026-09-05 ✅ 复检组 · 第 4 组 · `My family **spend** a whole day cooking a big meal.`（集合名词配复数谓语，合法的那一边）
- 2026-09-18 📝 题面整改：补（用 family 当主语说）· 复检组发题前审核（§6.5 第 7 项）
  `We cook all day during Spring Festival.` 用 we 当主语完全绕开集合名词 ⇒ 点名 family；单数复数动词都判 ✅（本条规则）
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ① 同级说法
  集合名词配单数配复数都成立（条目自己写着"⛔ 不许拿这一条判她错"）⇒ 没有可测的缺口
- 备注 合并 2026-08-19：#66（audience 作整体时配单数动词）并入本条 ——
  #66 是一条**写错了的绝对化规则**，与本条直接矛盾，已撤销
- 备注 与 #129（staff 没有复数形式 staffs）不冲突：那条管**词形**，本条管**动词一致**

### 192 · make sb ＋ 形容词（cause 不能这么用）
类型 搭配 ｜ 旧号 B106
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**make sb ＋ 形容词**（cause 不能这么用）：`too much screen time **makes kids overweight**`。
同一格里的邻居（别串）：⛔ cause ——它后面挂不了"宾语 ＋ 形容词"这个框。
判据一句话：要说"让某人变得怎样"，动词只能是 make ＋ 宾语 ＋ 形容词。

**怎么发现的**
旧 B 表迁移（B106，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组 ✅ `too much screen time makes kids overweight`（⛔ 没用 cause）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"让某人变得怎样"时动词先定成 make，再挂宾语 ＋ 形容词。

**题面**
"让孩子变胖"（用【一个动词 ＋ 宾语 ＋ 形容词】说）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `too much screen time **makes kids overweight**`（⛔ 没用 cause）
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；make sb ＋ 形容词她一直对（cause 这条错路从没走过）

### 193 · lose interest IN sth（介词是 in）
类型 搭配 ｜ 旧号 B107a
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **回潮 2026-09-05**（08-17 毕业 → 09-05 复检写成 lose interest **to**，她自己标注"这个介词不确定"，撤销毕业、连对清零） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
**问题是什么**
**lose interest IN sth**（介词写死是 **in**）。
判据：interest 后面要接"对什么"一律 **in** —— be interested **in** ／ have an interest **in** ／ lose interest **in**，
三个说法共用同一个介词 ⇒ 记「interest ＋ in」这一对，而不是三条规则。
同一格里的邻居（别串）：get bored with 也能说"失去兴趣"，但绕开 interest 这个名词 ⇒ 2026-09-07 题面补点名「用 **interest** 说」
（介词 ＝ 本条真考点，仍然留空）。
判据一句话：句子里只要出现 interest，介词就是 in。

**怎么发现的**
旧 B 表迁移（B107a，2026-08-18）；最早记录 2026-08-11 ❌，触发原话未存。
2026-08-17 ✅ ⇒ 毕业。
2026-09-05 ❌ 复检第 1 组（打包）· 触发原话 `kids will lose interest to（这个介意不确定) thier housework.`
—— 她自己标注"这个介词不确定" ⇒ 是真不确定、不是手滑 ⇒ **回潮**。
2026-09-07 ✅ `lose interest in`；2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。

**我错在哪**
她的：`kids will lose interest to … housework.`（2026-09-05 复检）　　正确：`lose interest **in** …`
找法：写完 interest 直接跟 in —— 三个说法（be interested／have an interest／lose interest）共用它。

**题面**
"他学了两个月吉他，就慢慢没兴趣了。"（"没兴趣"用 **interest** 说）

- 2026-08-11 ❌
- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-17 ✅

- 2026-08-23 📝 c 段 **改名，不是拆号**：原条目名写作"lose interest IN sth ＋ schoolwork"，
  但 schoolwork 只是那句题面里的名词、不是独立考点 ⇒ 条目名去掉后半，内容一字未动
- 2026-09-05 ❌ 复检组 · 第 1 组（打包）· **回潮**
  `kids will lose interest to（这个介意不确定) thier housework.` → lose interest **in**
  ❌ 介词错（to → in）。她自己标注了"这个介词不确定" ⇒ 是真不确定，不是手滑。
  ★ 判据给死：interest 后面要接"对什么"一律 in —— be interested **in** ／ have an interest **in** ／
    lose interest **in**，三个说法共用同一个介词，记"interest ＋ in"这一对而不是三条规则。
  ｜ ⚠️ housework（想说"学业" ＝ schoolwork／their studies）：**⛔ 未建条目、未记账** ——
    分不清是打字打歪（homework → housework，属拼写 §2.1 不算）还是真调错了词，
    已在反馈里交回给她判（§7 四问①：假错的代价 > 漏错）。她说要记再建。
  ｜ thier → their（拼写，不算错）
- 2026-09-07 📝 题面加提示「用 **interest** 说」：原题面「对学业失去兴趣」可合法译成 get bored with
  ⇒ 补名词点名，介词（＝本条真考点 IN）仍然留空。
- 2026-09-07 ✅ 复习 · 在池第 1 组 · `lose interest in` —— 介词 IN 对了（09-05 写成 to）
- 2026-09-09 ⚡ 自评免测 · 在池第 1 组（她原话："这 10 个题直接过吧，算对"）
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 interest，介词 in 留给她（她 09-05 写成 lose interest to）；换成学吉他场景

### 194 · screen time（⭐ 她自产）；balance A and／with B
类型 搭配 ｜ 旧号 B108
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
两个块：**screen time**（⭐ 她自产）＝ 屏幕时间；**balance A and／with B** ＝ 在两者之间找平衡。
`balance kids' **screen time and** outdoor activities`
判据一句话：balance 后面直接摆两件事、用 and 或 with 连；"看屏幕的时间"整块调 screen time。

**怎么发现的**
旧 B 表迁移（B108，2026-08-18；⭐ screen time 是她自产的块），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组（打包）✅ `balance kids' screen time and outdoor activities`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"平衡 A 和 B"时 balance 后面直接摆两件事；"屏幕时间"整块调 screen time。

**题面**
"给孩子的屏幕时间和户外活动找个平衡"

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `balance kids' screen time and outdoor activities`
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；screen time 是她自产的块、balance A and B 一直对

### 195 · An hour a day is completely fine.（给具体量当让步）
类型 结构 ｜ 旧号 B109b
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**An hour a day is completely fine.** ＝ 给一个**具体的量**当让步（量块直接当主语）。
同一格里的邻居（别串）：这跟 🎓#120（句子太单薄就补一个具体的量）是同一个动作的两个用处 ——
那条用它**补信息**，本条用它**让一步**。
判据一句话：要让步就先摆一个具体的量，让它直接当主语，⛔ 别绕成从句。

**怎么发现的**
旧 B 表迁移（B109b，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 4 组 ✅ `an hour a day is totally fine`——量块当主语，让步句成立。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：要让一步时先给一个具体的量，让它直接当主语。

**题面**
"一天一小时完全没问题。"

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 4 组 · `an hour a day is totally fine` —— 量块当主语，让步句成立
- 2026-09-20 ⚡ 自评免测 · 复检第 3 组（她答"直接过"）
- 2026-09-29 📝 退池 · ① 同级说法
  "一天一小时没问题"怎么说都成立（It's fine if it's just an hour a day 等），量块当主语只是表达风格 ⇒ 中译英里产不出 ❌；历史零 ❌

### 196 · singular they（someone → they／their）
类型 语法 ｜ 旧号 B110
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**singular they**：someone → **they／their** —— `For **someone** who … **their** favourite`。
同一格里的邻居（别串）：⚪ `Photoshop are` → is 是主谓一致（归 #10 形态类），与本条无关。
判据一句话：先行词是 someone／anyone／a person 这种不指明性别的单数 ⇒ 后面的代词一律 they／their。

**怎么发现的**
旧 B 表迁移（B110，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组 ✅ singular they 命中。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：主语是 someone 这种不指明性别的单数时，后面的代词直接用 they／their。

**题面**
"喜欢拍照的人，Photoshop 是他们的最爱。"（主语用 **someone** 起头说，后面的代词跟着它走 · ⛔ 不许用 his／her）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `For **someone** who … **their** favourite` —— singular they 命中
  ｜ ⚪ `Photoshop are` → is（主谓一致，归 #10 形态类）：同场 [4] 的 `screen time makes` 就是对的
- 2026-09-18 📝 题面整改：补（⛔ 不许用 his／her）· 复检组发题前审核（§6.5 第 7 项）
  `his or her favourite` 合法，绕开 singular they ⇒ 补排除项
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ① 同级说法
  someone 后面用 his or her 也不算错（旧题面靠"⛔ his／her"硬框），singular they 她一直用对 ⇒ 中译英里产不出 ❌；历史零 ❌

### 197 · addictive ≠ interesting
类型 词汇 ｜ 旧号 B112
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15**（08-20 的回潮已撤销，见下）｜ 题型 词组

**问题是什么**
**addictive ≠ interesting**：addictive ＝ 上瘾的、让人放不下的。
判据：**addictive ＝ 上瘾的（重音 ə-DIC-tive）／ additive ＝ 添加剂（重音 AD-di-tive）**
—— 留作参考，⛔ 不出复习题。
判据一句话：说"让人放不下"就是 addictive，⛔ 不是 interesting。
★ 拼成 additive ⛔ 不算错（她 2026-08-20 裁定："单词打错不算错（除非我主动说需要记录）"）。

**怎么发现的**
旧 B 表迁移（B112，2026-08-18）；最早记录 2026-08-09 ❌，触发原话未存。
2026-08-10 ✅ ／ 2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-08-19 📝 拼成 `additive`（判打字滑，未建号、未记档位）；
2026-08-20 ⛔ 教练一度按"同词反复错拼"记 ❌ 并让本条回潮 —— **她当天裁决后撤销**，🎓 恢复、不计任何档位。
2026-09-05 复检第 1 组（打包）✅ addictive。

**我错在哪**
她的：2026-08-09 记过一次 ❌（触发原话未存）；08-19／08-20 那两次是拼写，按她的裁定不算错。
找法：说"上瘾"时直接落 addictive，⛔ 别退成 interesting。

**题面**
"上瘾"（形容词 · 说的是游戏本身让人上瘾）
　　★ 题面 2026-08-20 改：原题面"游戏太上瘾，有的孩子一天不出门。"与 #144 的题面撞车，两条互相盖

- 2026-08-09 ❌
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-19 📝 拼成 `additive`（判打字滑，未建号、未记档位）
- 2026-08-20 ⛔ 教练一度按"同词反复错拼"记 ❌ 并让本条回潮 —— **当天她裁决后撤销**：
  「单词打错不算错（除非我主动说需要记录）」⇒ 本条恢复 🎓，08-20 不计任何档位
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· addictive
- 2026-09-18 📝 题面整改：补（说的是游戏本身让人上瘾）· 复检组发题前审核（§6.5 第 7 项）
  "上瘾"光秃秃给出，addicted（人上瘾）同样是形容词、同样合法 ⇒ 点明主语是游戏，逼出 addictive
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组

### 198 · the 的唯一功能 ＝ 双方都知道是哪一个
类型 语法 ｜ 旧号 B113
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**the 的唯一功能 ＝ 双方都知道是哪一个**：`**the** funny ones and **the** useful ones`。
同一格里的邻居（别串）：与 **#231（the fun ONES）共用这句中文** —— 两条各判各的格：
本条判 **the**、#231 判 **ones**；两条都已毕业，若回潮需先把题面改成互斥。
⚠️ 顺带：funny → **fun**（好玩的 ＝ fun／搞笑的 ＝ funny）—— ⛔ 未落号，交回她判。
判据一句话：听的人知不知道你指的是哪一个？知道就加 the。

**怎么发现的**
旧 B 表迁移（B113，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组 ✅ `the funny ones and the useful ones`——冠词两边都带上了。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：加不加 the 只问一句 —— 对方知道我指的是哪一个吗？

**题面**
"就两类，好玩的和有用的。"（两类各用一个名词短语说，⛔ 不许只说 fun and useful · ⛔ 不许用 stuff／things）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `**the** funny ones and **the** useful ones` —— 冠词两边都带上了
  ｜ ⚪ `Two kind of things` → kinds ｜ ⚠️ funny → **fun**（好玩的 ＝ fun／搞笑的 ＝ funny），⛔ 未落号，交回她判
- 2026-09-12 📝 题面整改：点名「冠词是考点…」→「两类各用一个名词短语说，⛔ 不许只说 fun and useful」（§10 禁令 5 禁预告测试点；与 #231 同句同改，两条各判各的格：本条判 the、#231 判 ones）· 全档题面 review
- 2026-09-18 📝 题面整改：补（⛔ 不许用 stuff／things）· 复检组发题前审核（§6.5 第 7 项）
  `fun stuff and useful stuff` 是不可数泛称，冠词位根本不出现 ⇒ 补排除项；只改本条题面，#231 的同句题面不动
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；这里的 the 她一直带对（冠词类、从没掉过），旧题面还堆了两层排除项
- 备注 与 #231（the fun ONES）共用这句中文 —— 两条都已毕业，若回潮需先把题面改成互斥

### 200 · think FOR oneself ≠ by oneself
类型 搭配 ｜ 旧号 B116
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**think FOR oneself ≠ by oneself**：整块是 **think for yourself**（自己独立思考），考点是介词 **for**。
同一格里的邻居（别串）：by oneself ＝ 独自一个人（没人陪），跟"独立思考"不是一回事；题面另排除 independently。
判据一句话：说"自己动脑子" ⇒ for oneself；说"一个人做" ⇒ by oneself。

**怎么发现的**
旧 B 表迁移（B116，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组（打包）✅ `consider **for** yourself`——考点介词 for 命中
（整块是 think for yourself，动词是块内另一格 ⇒ ⛔ 不落号）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写完 think 就问一句 —— 说的是"自己动脑子"吗？是就配 for yourself。

**题面**
"自己独立思考"（⛔ 不许用 independently）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `consider **for** yourself` —— 考点是介词 for（⛔ 不是 by），命中
  ｜ ⚠️ 整块是 think for yourself；考点已命中，动词是块内另一格 ⇒ 不落号
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ① 同级说法
  "独立思考"说 think independently 完全成立（旧题面靠排除项硬框），think for yourself 只是另一种说法 ⇒ 中译英里产不出 ❌；历史零 ❌

### 201 · "全信" ＝ trust it completely／take its word for it
类型 词组 ｜ 旧号 B118
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
"全信"的两个说法：**trust it completely** ／ **take its word for it**。
判据一句话：这一层只是一个**块**，一个词组就覆盖得了 ⇒ ⛔ 不必展开成句子。
★ 题面粒度由**她点名**改过（2026-09-05，原话："比如 AI 不能全信，如果你要考 trust，你就问 相信怎么说，
　或者 AI 不能全信 的 信怎么翻译"）⇒ 旧的整句题面"AI 不能全信。"改成块。

**怎么发现的**
旧 B 表迁移（B118，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组（打包）✅ `can't trust AI entirely`；同日按她的点名把题面缩成块。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"全信"时直接给块 —— trust … completely，或 take its word for it。

**题面**
"全信"（两个说法都要：一个用 trust 说，一个用 word 说）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `can't trust AI entirely`
- 2026-09-05 📝 题面整改 · 复检第 5 组当场（**她点名**：粒度不对）
  她的原话："比如 AI 不能全信，如果你要考 trust，你就问 相信怎么说，或者 AI 不能全信 的 信怎么翻译"
  旧："AI 不能全信。"（整句）　→　新："全信"（两个说法都要：一个用 trust 说，一个用 word 说）
  ★ 判据：考点只是"全信"这个块 ⇒ 一个词组就能覆盖 ⇒ 词组题，⛔ 不许给整句（SKILL §6①）。
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ① 同级说法
  "全信"说 trust it completely／believe everything it says 都成立，旧题面点名 trust／word 等于给答案 ⇒ 中译英里产不出 ❌；历史零 ❌

### 202 · 副词修饰动作：speak English well（不是 speak good）
类型 语法 ｜ 旧号 B119
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**副词修饰动作**：speak English **well**（⛔ 不是 speak good）。
判据一句话：修饰的是**动作**就用副词（well），修饰名词才用形容词（good）。

**怎么发现的**
旧 B 表迁移（B119，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组 ✅ `speak English pretty **well**`（⛔ 没写 good）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存 —— 条目名里的 speak good 是要她避开的那条路。
找法：这个词修饰的是动词还是名词？动词 ⇒ well。

**题面**
"英语说得挺好"（用 **speak** 说）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `speak English pretty **well**`（⛔ 没写 good）
- 2026-09-18 📝 题面整改：补（用 speak 说）· 复检组发题前审核（§6.5 第 7 项）
  `His English is pretty good.` 合法，good 修饰名词本来就对，完全绕开"动作用副词" ⇒ 点名 speak
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；speak English well 她一直对（speak good 这条错路从没走过）

### 203 · …, though.（挂句尾，唯一不用提前预判的转折标记）
类型 结构 ｜ 旧号 B120
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**…, though.** 挂句尾 —— **唯一不用提前预判的转折标记**：`It's far away from the subway **though**`。
同一格里的邻居（别串）：but／although 都要在**开口前**就知道要转折；though 挂句尾、说完再补 ⇒ 题面把两个都排除。
判据一句话：本条考的是 though 的**位置**（句尾），⛔ 不是它是个什么词。
★ 类型由 词组 改 **结构**（2026-09-05 **她点名**，原话："这种为什额是词组？我单独写个 though 可以么，
　词组的意思是，我只需要回答一个单词或者词组就能覆盖"）—— 这句话已被写进 SKILL §6① 当粒度判据的唯一定义。

**怎么发现的**
旧 B 表迁移（B120，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组（打包）✅ though 挂句尾；同日按她的点名改了类型与题面。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：话说完了才想转折 ⇒ 句尾补一个 though，⛔ 不用回头改成 but／although 起头。

**题面**
"房子挺好，不过离地铁远。"（"不过"那一层挂到**句尾**说，⛔ 不用 but／although 起头）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `It's far away from the subway **though**` —— though 挂句尾
  ｜ ⚠️ `big enough`（＝够大了）→ pretty big；不落号
- 2026-09-05 📝 题面整改 ＋ **类型改正** · 复检第 5 组当场（**她点名**）
  她的原话："这种为什额是词组？我单独写个 though 可以么，词组的意思是，我只需要回答一个单词或者词组就能覆盖"
  旧：类型 词组 ｜ "这房子挺大，不过离地铁远。"（转折用 though 说，⛔ 不用 but）
  新：类型 **结构** ｜ "……，不过离地铁远。"（"不过"那一层挂到**句尾**说，⛔ 不用 but 起头）
  ★ 判据：本条考的是 though 的**位置**（不是一个词组）⇒ 类型该是"结构"；
    题面只保留能显出位置的最小片段，⛔ 不给完整的两分句。
  ★ 她这句话已被写进 SKILL §6① 当**粒度判据的唯一定义**（逐字引用）。
- 2026-09-12 📝 题面整改：「……，不过离地铁远。」→「房子挺好，不过离地铁远。」＋ 排除 although —— 整句题不许用省略号顶掉前半句（§6.5 第 6 项：有主语、能独立成句）· 全档题面 review
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ① 同级说法
  "不过离地铁远"用 but 起头完全成立（旧题面靠"⛔ but／although"硬框），句尾 though 只是另一种说法 ⇒ 中译英里产不出 ❌；历史零 ❌

### 204 · 中文无主语句 → 先想被动或 they
类型 结构 ｜ 旧号 B123
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**中文无主语句 → 先想被动或 they**：`this road **was built** last year`。
同一格里的邻居（别串）：🎓#135 管的是"社会／大家／人们"这种**虚主语**，本条管的是中文**压根没给主语**。
判据一句话：中文句子里找不到主语时，先试被动，再试 they。
★ built ⛔ 不判错：中文"路修好了"本身兼含"修建完成"，built 是合法读法（§7 四问① 自我推翻通过）。

**怎么发现的**
旧 B 表迁移（B123，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 4 组 ✅ `this road was built last year`——无主语句用被动吃掉。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：中文句子里找不到主语时，先试被动（was done），再试 they。

**题面**
"这条路去年修好了。"

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 4 组 · `this road was built last year` —— 无主语句用被动吃掉
  ★ built 不判错：中文"路修好了"本身就兼含"修建完成"，built 是合法读法（§7 四问① 自我推翻通过）
- 2026-09-20 ⚡ 自评免测 · 复检第 3 组（她答"直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；无主语句用被动她一直对

### 205 · the market／the economy 这类系统性名词带 the
类型 语法 ｜ 旧号 B133
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ ⚪ **只记录·不出题** ｜ 题型 词组

**问题是什么**
**the market／the economy 这类系统性名词带 the**：`raise funding from **the market**`。
同一格里的邻居（别串）：同一句里的 banks 是可数复数泛指、**不带** the（borrow from banks）—— 两边方向不同。
判据一句话：指的是"整个市场／整个经济"这种独一份的系统 ⇒ 带 the。

**怎么发现的**
旧 B 表迁移（B133，2026-08-18）；最早记录 2026-08-09 ❌，触发原话未存。
2026-08-10 ✅ ／ 2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 1 组 ✅ `raise funding from the market or borrow from banks.`

**我错在哪**
她的：2026-08-09 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：说到 market／economy 这种"整个系统"时先把 the 补上。

**题面**
"从市场上融资，或者跟银行借"

- 2026-08-09 ❌
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `raise funding from the market or borrow from banks.` —— from **the** market
- 2026-09-12 📝 题面整改：去句号「从市场上融资，或者跟银行借」—— 中文无主语，按块出、回标词组（§6.5 第 6 项）· 全档题面 review
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 改标只记录·不出题（§3.4／§3.6：形态类掉过的 ⛔ 不走退池）
  冠词类（系统性名词带 the），08-09 掉过一次、此后四次全对 ⇒ 她会、缺口在"产出时检查不运行"；以后在哪儿掉都只记 ⚪
  检查触发：说到 market／economy 这种"整个系统"时先把 the 补上

### 206 · 书面词降级（有口语版就用口语版）
类型 减法型 ｜ 旧号 B136
状态 连对2 连错0 上次2026-08-25 ｜ **⚪ 只记录·不出题** ｜ **🎓 已毕业 2026-08-24**（08-17 曾毕业 → 08-23 回潮 → 08-24 两篇自由产出连过）｜ 题型 整句

**问题是什么**
**书面词降级（有口语版就用口语版）**——类型"减法型"：要她**换档**，不是多学词。
· **词本身不许判错，只判"有口语版却没走口语版"**（08-23 写死）：那些词她**用得准、没用错**，
　判的是**档位** —— 口语 Band7 ≠ 写作 Band7（她 07 月自己定的）。
· 要盯死的三种形状：
　① 动名词／抽象名词当主语 ＋ plays a crucial role／is of great importance 这类套话
　② regarding／in terms of ＋ 抽象名词（公文体）
　③ 学术动词：internalize／facilitate／mirror／utilize／enhance（后来又撞上 consult／operate／present）
⚠️ 与"该不该建条目"的分界线（2026-08-27 c 段定）：
　**她产出的形式错了**（搭配／介词／形态站不住）⇒ **建条目**（#300 · #301 就是这么补的）；
　**形式对、只是偏正式** ⇒ **归本条、⛔ 不建条目**（口语替换版是开放集合，给每个开号 ＝ #157 那种伞形陷阱）。
　一句话：**判"她写错了没有"，不判"有没有更口语的说法"。**
★ 她 2026-08-30 裁决（原话："另外我选b" ／ "B 后面别问了。"）：继续记备注、⛔ 不判回潮，
　升级成**每篇自由产出必扫的教练侧固定检查项** ⇒ ⛔ 不占她的复习位、⛔ 不再逐次提请裁决。

**怎么发现的**
旧 B 表迁移（B136，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅（连续 5 篇自由产出通过 ⇒ 08-17 毕业）。
2026-08-23 ❌ **回潮** · 付息日 d 段重答 R1 · **整篇 86 词是写作腔**，六处书面块都有现成口语版
（a blend of ／ gradual autonomy ／ introduce predictable daily schedules ／ internalize time management ／
shaping … plays a crucial role ／ provide designated storage spaces ／ mirror … regarding orderliness）。
2026-08-24 ✅ ×2（同一天两篇 cold 自由产出，§3.3 各算一次）⇒ 连对 2，第二次毕业。
此后按选项 B 逐篇扫描留痕：08-27 命中1 → 08-29 命中3 → 08-30 命中1 → 08-31 R8 命中0（反向1）
→ 08-31 R9 命中1 → 09-01 命中0 → 09-03 命中3 → 09-04 命中2 → 09-10 命中3 → 09-11 命中2。

**我错在哪**
她的：`internalize time management` ／ `shaping … plays a crucial role` ／ `financial support … plays a crucial role` ／
`consult them on how to …` ／ `the primary source` ／ `with the advent of AI`
正确（同一个意思的口语版）：`get the hang of managing their own time` ／ `how you set the place up matters too` ／
`really helps the economy grow` ／ `ask them how to …` ／ `the main source` ／ `now that AI is around`
检查触发：说完一句问自己 —— **"这句话我会当面对朋友这么说吗？"** 不会就换成会说的那版。
· 一段里**动名词主语不许连着超过两句**（08-23 扩写）
· **降档时清点例子个数** —— 降档不该丢内容（08-23 扩写）
· 写完一段回头看：**这一段前面有没有现成的块可以直接再用一次？**（08-25 扩写）

**题面**
不出中译英题；**挂当日自由产出抓**（出现书面词而有现成口语版 → ❌）
★ 题型 产出验 ＋ 状态行 `⛔ 复习组停出`（2026-09-05 补的机器闸）⇒ ⛔ 不进召回队列。

- 2026-08-12 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-16 ✅
- 2026-08-17 ✅（连续 5 篇自由产出通过）
- 2026-08-23 ❌ **回潮** · 付息日 d 段重答（R1 How can parents help children to be organized?）
  **整篇 86 词是写作腔**，六处书面块都有现成口语版：
```
a blend of                              → a mix of
gradual autonomy                        → giving them a bit more freedom
introduce predictable daily schedules   → set up a regular daily routine
internalize time management             → get the hang of managing their own time
shaping … plays a crucial role          → how you set the place up matters too
provide designated storage spaces       → give everything somewhere to go
mirror … regarding orderliness and planning → pick up … how tidy they are, whether they plan ahead
```
  ★ 依据 ＝ 本条 08-19 自己写的备注"再出现一次按回潮处理"。今天不是一次，是**六处**
  ★★ **判回潮的理由必须写清，否则下次会读成"她词汇好反而被扣分"**：
     这些词她**用得准、没用错**，单看词汇是加分的。判的不是词，是**档位** ——
     口语 Band7 ≠ 写作 Band7（她 07 月自己定的），一个她在压力下调不出来的档位，
     考场上要么卡住、要么听着像背的。**词本身不许判错，只判"有口语版却没走口语版"**
  ★ 检查触发（本条原有，今天扩写）：说完一句问"**这句话我会当面对朋友这么说吗？**"
    不会 → 换成会说的那版。特别盯三种形状：
    ① 动名词/抽象名词当主语 ＋ plays a crucial role／is of great importance 这类套话
    ② regarding／in terms of ＋ 抽象名词（公文体）
    ③ 学术动词：internalize／facilitate／mirror／utilize／enhance
- 2026-08-23 ⚪ **同题第二版（她读完讲评后自己重写，90 词）—— 档位对了，但按 §3.3 不改当天标记**
  `Well, I'd say it's mainly about building good/standard habits while giving kids room to manage themselves.
   First off … On top of that … and honestly … So overall …`
  —— 第一版那六个书面块**一个没剩**；七个口语标记全自发；`get a feel for time` 比
     `internalize time management` 又口语又准
  ⚠️ **本次不计 ✅，回潮不撤销**：§3.3 明写"**教练给过答案后的重说不改当天标记**"。
     它证明她**改得动**（很重要），但不能拿来抵消 cold 那次的档位。
     ⇒ 下一次在**没看过讲评**的自由产出里通过，才计 ✅
  ★ 检查触发扩写（本条今天第二次扩）：
    ① 一段里**动名词主语不许连着超过两句**（她这版 Using…／creating…／Having… 连着三句）
      —— 第三句改成祈使句或"主语 ＋ 实义动词"
    ② **降档时清点例子个数**：第一版四个具体例子（visual timetables／task charts／labeled bins／
      color-coded folders），降档后只剩两个 ⇒ **降档不该丢内容**
- 2026-08-24 ✅ **回潮后第一次通过** · 自由产出（新题 bank:1027 P2 Describe an interesting building，181 词）
  整篇口语档，**零书面块**：basically ／ quite often ／ pretty much everyone ／ honestly ／
  not really into ／ wander around ／ grab a meal ／ nothing fancy ／ a handy spot
  ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ⚠️ 全篇唯一偏正式的是 `a glass exterior`（口语更常说 a tall glass building）——
    单点、且母语者也说 ⇒ 按 08-19 备注的惯例只在更好版里给，**不判回潮**
  ★ 对照价值：与 08-23 R1 v1（同为 cold 自由产出、六个书面块）只隔一天，
    差别不在词汇量而在**这次她瞄的是口语目标** —— 这正是本条要固化的东西
- 2026-08-24 ✅ **同日第 2 篇**（§3.3 每次各记一行各算一次）· 自由产出（新题 bank:924 P3
  Should parents reward children，128 词）整篇口语档：
  work toward ／ a little push to get started ／ Say you promise… ／ cut corners ／
  everything in moderation ／ a way to get kids to do…
  ⇒ **连对 1 → 2 ⇒ 🎓 毕业**
  ⚠️ 两处偏正式，**只记备注不判回潮**（同 08-19 `at will`／同日 P2 `glass exterior` 的惯例）：
    `kids' lack of motivation` → when they're just not motivated ｜ `use it with caution` → go easy on it
    —— 两处都不是学术词、母语者也说，且全篇没有本条检查触发里那三种形状
  ★ 毕业理由写清（防下次误读成放水）：两次 ✅ 都是**同一天的两篇 cold 自由产出**，
    §3.3（她 08-23 定）明写"同一天同一条被产出多次 ⇒ 每次各记一行、各算一次"；
    安全网仍是回潮 —— 再出现写作腔照样掉回来
- 2026-08-25 ✅ **同日第 2 篇通过**（加练新题 bank:1043 P2，163 词）—— 整篇口语档：
  really into ／ a whole afternoon ／ follow the manual ／ the coolest thing ／ had the final say ／
  much of an imagination ／ tough
  ⚠️ **唯一 1 处偏正式**：`whether I was actually **engaged**`（HR／绩效报告词）→ really into it
    —— 按 08-19 `at will`／08-24 两篇的同一惯例：不属检查触发的三种形状、母语者也说
    ⇒ **只记备注，不判回潮**（本条已毕业，状态不动）
  ★★ 这一处值得单独记，和同日 P3 的 `output at work` 是**同一个形状**：
     `is really into Lego` 就写在**同一篇的第二句**，到第十一句没复用上 ——
     ⇒ 检查触发再加一条：**写完一段回头看，这一段前面有没有现成的块可以直接再用一次？**
- 2026-08-29 📝 新题 P2 · **记备注，不判回潮**（本条已毕业，状态行不动）·
  两处书面登记：`**Additionally**, the river **holds special significance** in ancient Chinese history`
  → On top of that, the river **means a lot in** Chinese history
  ★ 裁法沿用 08-27 R7 `In today's fast-paced world` 那一次（归本条记备注、不判回潮）——
    档位是 ⚠️（母语者也说），不是 ❌
  ⚠️ **但这是连续第二篇被记同一件事** ⇒ 若第三篇再出现，把"是否该回潮"提给她裁
- 2026-08-30 📝 新题 P3（What technology do young people like to use?）· **记备注，不判回潮**
  （本条已毕业，状态行不动）· `While smartphones **offer great convenience**, they also take up
  too much of our time.` → make life a lot easier
  ★ 档位 ⚠️（母语者也说，只是登记偏书面），不是 ❌ ⇒ 沿用 08-27／08-29 的裁法
  ★★★ **这是连续第三篇被记同一件事**：
     08-27 R7  `In today's fast-paced world`
     08-29 P2  `Additionally` ＋ `holds special significance`
     08-30 P3  `offer great convenience`
  ★★★ **她 2026-08-30 当场裁决 ＝ 选项 B**（原话：`另外我选b` ／ `B 后面别问了。`）：
     **继续记备注、不判回潮，但升级成「每篇自由产出必扫」的教练侧固定检查项，⛔ 不占她的复习位。**
     ⇒ 本条状态行**保持 🎓 不变，一个字不改**。
     ⇒ 落实动作：写进 `.claude/skills/fluency-lab/SKILL.md` §7（教练侧动作），
       依据 ＝「规则只进两个来源：她定的／她认可的教练提案」。
     ⇒ ⛔ **以后不再逐次提请她裁决**（`B 后面别问了`）——教练自己扫、自己在 diff-2 给口语版、
       自己记 📝 到本条；本项从今天起**不再进"待她裁"清单**。
- 2026-08-31 📝 付息日 d 段 · 重答 R8 · **书面登记扫描：本篇零命中 ＋ 反向命中一次**（🎓 状态行冻结）
  `**On top of that**, it's convenient to get to know new people.`
  ★ 这正是 08-29 那篇 `Additionally` 的更好版 —— **隔两天她自己调出来了**。
  ★ 逐词核过本族全部成员：Additionally／Furthermore／Moreover · In today's fast-paced world ·
    hold special significance · offer great convenience · primary ⇒ **一个都没出现**。
  ★ 连续四篇走向：08-27 命中 1 → 08-29 命中 3 → 08-30 命中 1 → **08-31 命中 0 ＋ 反向 1**。
- 2026-08-31 📝 付息日 d 段 · 重答 R9 · **书面登记命中 1 处**（🎓 状态行冻结，契约⑦；按她 08-30 定的选项 B）
  `So **financial support** from governments **plays a crucial role** in economic growth.`
  ★ 命中的正是**本条检查触发① 逐字点名的那个形状**：「动名词/抽象名词当主语 ＋ plays a crucial role／
    is of great importance 这类套话」——抽象名词 financial support 当主语。
  ★ 口语版已在 diff-2 给出：`really helps the economy grow` ／ `makes a real difference to the economy`。
  ★ 固定三步走完（⛔ 不多不少）：① diff-2 给口语版（⚠️ 不是 ❌）② 本行 📝、**不判回潮、状态行不动**
    ③ 完事，⛔ 不再提请她裁决。
  ★ 教练自审留痕：第一反应是"这词组挺好、考官吃这套，不该判"，靠 grep 撞上本条的检查触发才纠回来。
  ★ 连续五篇走向：08-27 命中1 → 08-29 命中3 → 08-30 命中1 → 08-31 R8 命中0（反向1）→ **R9 命中1**。
- 2026-09-01 📝 新题 P3（bank:490）· **书面登记扫描：本篇零命中**（🎓 状态行冻结，机器契约⑦；她 08-30 定的选项 B）
  逐词核过本族全部成员：Additionally／Furthermore／Moreover · In today's fast-paced world ·
  hold special significance · offer great convenience · primary ⇒ **一个都没出现**。
  ★ 反向证据（全篇口语 register）：`it depends on`／`turning up on time`／`a big one`／
    `one careless mistake`／`real trouble`／`doing your share`／`not causing problems for the team`。
  ★ 连续六篇走向：08-27 命中1 → 08-29 命中3 → 08-30 命中1 → 08-31 R8 命中0（反向1）
    → 08-31 R9 命中1 → **09-01 命中0**。
  ★ 固定三步走完（⛔ 不多不少）：① 零命中、无口语版可给 ② 本行 📝、状态行不动 ③ 完事，不提请裁决。
- 2026-09-03 📝 新题 P3（bank:831 · When would old people ask young people for advice?）· 书面登记（§7 固定三步的第②步，她 08-30 定 B）· **不判回潮、状态行一个字不动**
  本篇命中 **3 处**（都不判 ❌ —— 本条备注写死"词本身不许判错，只判有口语版却没走口语版"）：
```
consult them on how to …   → ask them how to …      （consult ＝ 咨询专业人士的档位）
operate smartphones         → use smartphones         （operate 配机器设备，日常东西用 use）
current developments        → what's going on         （新闻/报告说法 → 大白话）
```
  ★ 三处的共同形状 ＝ **学术动词 ＋ 抽象名词**，正是本条检查触发第③栏那一类
    （与 08-23 回潮那次的 internalize／facilitate／mirror 同族）。
  ★ 本篇干净的部分：无 Additionally／Furthermore／Moreover ／无 In today's fast-paced world
    ／无 hold special significance ／无 primary；开头 `Mostly with technology, I'd say.` 是纯口语。
  ⇒ 连续第七篇执行书面登记扫描。**⛔ 不再逐次提请她裁决**（她 08-30 原话："B 后面别问了"）。
- 2026-09-04 📝 **书面登记 ×2**（§7 固定检查项 · 不判回潮、状态行一个字不动）· 新题第 1 道
  ① `he **presented** me a picture` → **showed** me a picture
     两岁孩子把画拿给妈妈看，口语只用 show；present 是"颁发／正式呈递"的档位。
  ② `kids have fewer **entertainment options**` → fewer **things to do**
     things to do 她明明会，压力下先蹦出来的是抽象名词块。
  ★ 不算的一处（自己推翻，留痕）：`two factors` —— 口语本来就说 come down to two factors
    ⇒ 造得出母语句 ⇒ 不判为书面登记。
  ★ 按她 08-30 定的选项 B：diff-2 给口语版 ⇒ 本条记一行 📝 ⇒ **完事，⛔ 不提请裁决**。
- 2026-09-05 📝 状态行加剔除标记 · 付息日 c 段（⛔ 真缺陷：靠散文钩子挡，机器闸没接管）
  本条题面写死 "不出中译英题；挂当日自由产出抓"，但**状态行没有任何剔除标记**
  ⇒ `lab.py pick` 照样能把它抽进复习组（只是至今没抽到）。
  ⇒ 加 `⛔ 复习组停出`，交给 §3.5 的剔除口径机械挡掉。
  ★ 与 §7「书面登记扫描」一致：它是**教练侧固定检查项**，本来就不该占她的复习位。
- 2026-09-10 📝 书面登记 · 新题 bank:956 自由产出（P3）· 本篇 3 处命中，按 §7 三步处理（⛔ 不判回潮、⛔ 状态行不动）
  `the **primary** source`            → the **main** source（primary 是本条清单里点名列着的那个词）
  `Chengdu … **constructed** a big chemical factory` → **built** a big chemical **plant**
  `**According to my observation**,`  → **From what I've seen,**（"据我观察"的直译）
  ★ 判据不变：这三处她**不是不会**口语版，是压力下先蹦出书面那个 ⇒ 挂教练侧当固定检查项，
    ⛔ 不占她的复习位、⛔ 不再逐次提请她裁决
  ★ 对照：09-09 那篇 P2 是**零命中**（did great／a bunch of／take it slow 全口语档）⇒ 本篇回升 3 处，
    差别在题型：P3 说理一开口就往"论文腔"上靠，P2 讲故事天然是口语档
- 2026-09-11 📝 书面登记 · 付息日 d 段重答 R10 · 2 处：`with the advent of AI`（→ now that AI is around）· `state your requirements`（→ tell it what you want）
  ★ advent 这一处 08-07 首答就被标过书面词，今天原样回来 —— "想显得正式就调书面词"那个开关还在。只记 📝，⛔ 不判回潮
- 2026-09-15 📝 书面登记 · 学习日 在池第 2 组 [8]（#334 题）· `The primary cause` → main（⛔ 不判回潮、状态行不动）
- 2026-09-15 📝 书面登记 · 新题 bank:1059（P2）· 3 处：`failed to find` → couldn't find ｜ `addressed the issue` → sorted it out ｜ `builds your own capabilities` → you end up learning a lot yourself
  （⛔ 不判回潮、状态行不动；`using his own device` → on his own laptop 那一处她点名要学 ⇒ 已单独建号 #345）
- 2026-09-18 📝 书面登记 · 新题 bank:353（P3）· `whereas` → while（⛔ 不判回潮、状态行不动）
- 2026-09-19 📝 书面登记 · 付息日 d 段重答 R12（P3）· `digital payments` → using their phones（⛔ 不判回潮、状态行不动）
- 2026-09-22 📝 书面登记 · 学习日 在池第 1 组 [7]（#355 题）· `various ballads` → all sorts of ballads（⛔ 不判回潮、状态行不动）
- 2026-09-26 📝 书面登记 · 重答 bank:778（R16）S4 · `in recent years` → over the past few years（不判回潮、状态行不动）
- 2026-09-27 📝 书面登记 · 新题 bank:1339（P3）[S4] · `offer space for recreation` → give us somewhere to hang out（⛔ 不判回潮、状态行不动）
- 2026-09-29 📝 书面登记 · 学习日新题 bank:534 · `far outstrip those of other industries` → are way better than in other industries（⛔ 不判回潮）
- 2026-09-30 📝 书面登记 · 付息日 d 段重答 bank:911 [S4] · `makes you appear more friendly` → look（状态行不动）
- 备注 2026-08-19 新题里出现 `at will`（有现成口语版 whenever they feel like it）——
  单次、且 at will 母语者也说，**这次只记备注不判回潮**；再出现一次按回潮处理

- 备注 2026-08-25 · 自由产出（新题 bank:987 P3，84 词）**3 处偏正式，不判回潮**（毕业状态不动）：
```
significantly changed                      → completely／really changed
your output at work … than your coworkers' → you just won't get as much done as your coworkers
in all stages of your life                 → at every stage of your life
```
  判据走 08-19 `at will`／08-24 `glass exterior`／08-24 `use it with caution` 三次的同一惯例：
    ① 三处**都不属于**本条检查触发点名的三种形状（无套话主语／无 regarding·in terms of／无学术动词）
    ② 三处**母语者也说**，只是场合更正式
    ③ 全篇骨架是口语的：Yes, definitely ／ for instance ／ On top of that ／ kill time ／
       know nothing about it ／ keep up with the times
  ⇒ **只记备注**。★ 阈值写死：下一篇若再出现偏正式，**且落在三种形状里的任意一种 ⇒ 按回潮处理**
  ★★ 其中 `your output at work` 这一处值得单独记：口语走法就是 **🎓#28 `get more done`** ——
     她 08-24 刚在中译英里把这条调出来并毕业，今天自由产出时没调出来。
     **这是"知识在、检索没跑"最干净的一个证据**，不是词汇缺口
- 备注 2026-08-26 · 自由产出（新题 bank:244 P2，202 词）**1 处偏正式，不判回潮**（毕业状态不动）：
```
Within several minutes    → within a few minutes ／ in a couple of minutes
```
  判据走 08-19 `at will`／08-24 两篇／08-25 两篇的同一惯例：不属检查触发点名的三种形状、
  母语者也说；且全篇骨架是口语的：mess around ／ hang out ／ wander around ／ right up until ／
  saved the day ／ keeps his cool ／ doing really well ／ turns to ／ happy to help
  ⇒ **只记备注**。★ 阈值不变：下一篇若再出现偏正式且落在三种形状里 ⇒ 按回潮处理
  ★★ **靶心 A 今天没复现，反而拿到反面证据**：`What makes him stand out is …` 这个 cleft
     是她 08-24 P2 `What makes it stand out is …` 用过的块，隔两天在一道全新的题里又调出来了
     ⇒ 块**跨天复用**成立；本篇也没找到"另造一个"的位置
- 备注 ★★★ **本条与"该不该建条目"的分界线（2026-08-27 付息日 c 段定，起因是她 08-26 抓到
  #300 #301 漏建）** —— 扫完本条从 08-19 到 08-26 记下的全部 10 处 ⚠️ 后得出：
```
她产出的形式【**错了**】—— 搭配/介词/形态站不住 ⇒ **建条目**
    实证：in all stages of your life（stage 该配 at）⇒ #300
          enjoyed **the** time（该用物主代词）⇒ #301
她产出的形式【**对，只是偏正式**】⇒ **归本条，不建条目**
    实证：at will ／ a glass exterior ／ significantly changed ／ Within several minutes ／
          use it with caution（口语版 go easy on it）
    理由：口语替换版是**开放集合**（每个书面词都配一个口语版）——
          给每个都开条目 ＝ #157 那种"结构上永远毕不了业"的伞形陷阱（§3.2b）
★ 一句话：**判"她写错了没有"，不判"有没有更口语的说法"。**
  后者是本条的活（减法型、挂自由产出抓），前者才建号。
★ 降级的**操作**另有归宿：抽象名词那一类走 methods **M40**（抽象名词 ⇒ 摊成小句）
```
- 备注 c 段扫描留痕（2026-08-27）：本条 10 处 ⚠️ 逐条跑过 §3.2b 自查，结论 ——
  已建 1（#300，08-26 补）· 已归已有号 1（🎓#28 get more done）· 她已拥有该块 1（really into it）·
  应归本条不建 6 · **方法漏落 1 → 已补 methods M40**（kids' lack of motivation 那一处，
  连同 08-24 同篇的 the purpose of doing things，两处同形）⇒ **无第二个 #300/#301 式的漏网**

### 207 · I'd say ＋ "主要就是…"四条路径
类型 词组 ｜ 旧号 B137 ｜ ⛔ **条目内容待补**
状态 连对3 连错0 上次2026-09-28 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**I'd say ＋ "主要就是…"** —— 用 I'd say 起头，把观点软化着抛出来。
⛔ **条目内容待补**：本条正文只有标题，**那四条路径一个字都没有** ——
　2026-09-05 复检时题面还写着「（四种说法各说一次）」，而那四种说法**在档案里根本不存在**
　⇒ 任何人都答不出来（她的原话："我不懂 4 种说法什么意思"）⇒ 判 ◎，状态行加 `⛔ 复习组停出`。
判据一句话：内容补回来之前 ⛔ 不再出题，只在自由产出里看她抛观点时有没有自发用 I'd say 起头。

**怎么发现的**
旧 B 表迁移（B137，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 ◎ 复检第 5 组（打包）· **题面不可执行，本次作废**（⛔ 不动连击）；当场改题面 ＋ 标 ⛔ 条目内容待补。

**我错在哪**
她的：本条判定里没有掉过（09-05 那次 ◎ 的责任在条目内容缺失），触发原话未存。
找法：要抛观点时先落一句 `I'd say …`，把话软化着说出来。

**题面**
"我觉得主要就是时间不够。"（用 **I'd say** 起头说）
★ ⛔ 条目内容待补：本条正文那"四条路径"至今一个字都没有 —— 题面本身可用，内容补回来之前只考 I'd say 这一句起头。

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ◎ 复检组 · 第 5 组（打包）· **题面不可执行，本次作废**（⛔ 不动连击）
  她的原话："我不懂 4 种说法什么意思"。
  ★ 查证属实：题面写着「（四种说法各说一次）」，而**那四种说法在档案里根本不存在** ——
    本条正文只有标题，**零判据块**，四条路径一个字都没有 ⇒ 任何人都答不出来。
  ⇒ 题面已改成只考 I'd say；元信息标 `⛔ 条目内容待补`，状态行加 `⛔ 复习组停出`，
    内容补回来之前不再出题。
- 2026-09-15 📝 产出验机制取消 ⇒ 恢复出题：题型格回默认「整句」、删掉 ⛔ 复习组停出 标记、题面换回留档的「我觉得主要就是……」（⛔ 条目内容待补保留成一行 ★ 注释）
- 2026-09-18 ✅ 复检 · 学习日 复检第 3 组 · `I'd say it mainly boils down to not having enough time.`——I'd say 起头
- 2026-09-28 ✅ 复检第 2 组 · `I'd say it mainly comes down to a lack of time.`
- 2026-09-29 📝 退池 · ③ 题面收不拢 ＋ 条目内容缺失
  "我觉得"说 I think／I guess 都成立，不点名逼不出 I'd say、点了就是给答案；正文那"四条路径"至今空着 ⇒ 测不出缺口

### 208 · some people ≠ somebody
类型 词汇 ｜ 旧号 B142
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**some people ≠ somebody**：说"有些人"用 **some people**（复数人称）。
同一格里的邻居（别串）：somebody／someone ＝ 某一个人（🎓#196 的 singular they 用的正是它）——
2026-09-05 那次 ◎ 就是因为教练在同一组的点名里逐字塞了 `someone` 给她 ⇒ **组内污染**。
★ 规则缺口留痕：§6.5 第 8 项「组内防撞」只写了查**题面**互不撞车，**没写"点名里塞进去的词也算撞车源"**。
判据一句话：说的是"一部分人" ⇒ some people；"某一个人"才是 somebody。

**怎么发现的**
旧 B 表迁移（B142，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 ◎ 复检第 5 组 · 教练组内污染，本次作废（⛔ 不记 ❌）。
2026-09-07 复检第 5 组（打包）✅ `some people`（⛔ 没落进 somebody）。

**我错在哪**
她的：本条判定里没有掉过（09-05 那次 ◎ 的责任在教练），触发原话未存。
找法：说"有些人"时先数人 —— 一部分人是 some people，一个人才是 somebody。

**题面**
"有些人"

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ◎ 复检组 · 第 5 组（打包）· **教练组内污染，本次作废**（⛔ 不动连击）
  本条考 some people ≠ somebody，她答 `someone`。
  ★ 但**教练在同一组 [5] 的点名里逐字塞了 `someone` 给她**（"主语用 someone 起头说"），
    隔三题就考"有些人" ⇒ 答案是教练自己污染进去的 ⇒ ◎，⛔ 不记 ❌。
  ★ 规则缺口：§6.5 第 8 项「组内防撞」只写了查**题面**互不撞车，
    **没写"点名里塞进去的词也算撞车源"** ⇒ 今天实测踩中（待她裁是否补进 SKILL）。
- 2026-09-07 ✅ 复检 · 第 5 组（打包）· `some people`（复数人称，⛔ 没落进 somebody）
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌（09-05 是教练组内污染的 ◎）；some people 她一直对

### 209 · 形容词顺序（口语版）
类型 结构 ｜ 旧号 B143
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**形容词顺序（口语版）**：`an **online pet** group` —— 限定性最强的那个贴名词最近。
判据一句话：越是说"属于哪一类"的形容词，越贴着名词放。
★ 她 2026-09-05 当场点评本条："**反而这个才应该是词组**" —— 她说得对，本条正是粒度合格的样子。

**怎么发现的**
旧 B 表迁移（B143，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组 ✅ `an online pet group`（gourp 是拼写，⛔ 不算错）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：几个形容词排队时，把"属于哪一类"的那个贴到名词旁边。

**题面**
"一个线上的养宠物的群"（两个修饰词都放在 group 前面）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `an online pet group`（形容词顺序）｜ gourp 是拼写，⛔ 不算错
  ★ 她当场点评本条："反而这个才应该是词组" —— **她说得对**，本条正是粒度合格的样子。
- 2026-09-18 📝 题面整改：补（两个修饰词都放在 group 前面）· 复检组发题前审核（§6.5 第 7 项）
  `a group online for pet owners` 把修饰语挪到后面，顺序问题不出现 ⇒ 限定位置，不给顺序
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；形容词顺序她一直对（类型 结构却标词组的旧题面一并作废）

### 210 · there was A PROMOTION（要名词，不能塞形容词/动词）
类型 结构 ｜ 旧号 B145
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**there was A PROMOTION** —— there is／was 后面要的是**名词**，⛔ 不能塞形容词或动词。
`there is **a promotion** on the product page.`
同一格里的邻居（别串）：on sale／discounted 是形容词那条路、完全合法，但绕开这个名词槽 ⇒ 题面已排除。
判据一句话：there is 后面必须跟一个名词短语。

**怎么发现的**
旧 B 表迁移（B145，2026-08-18）；最早记录 2026-08-09 ❌，触发原话未存。
2026-08-10 ✅ ／ 2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-08-27 ✅ 自发命中·同篇两处（付息日 d 段重答 R7）—— 毕业 12 天后第一次在自由产出里自发验到，
而且是在**同一句里**把 #78（a pack of ／ the product page）和本条一起调出来的。
2026-09-11 复检 ✅ `thers is a promotion on the product page.`（thers 属拼写，§2.1 不算错）

**我错在哪**
她的：2026-08-09 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：写完 there is／was，回头看后面挂的是不是一个名词。

**题面**
"商品页上有个促销。"（用 **there** 起头说 · ⛔ 不许用 on sale／discounted）

- 2026-08-09 ❌
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅

- 2026-08-27 ✅ **自发命中·同篇两处**（本条未被出题，不改已毕业状态）· 付息日 d 段重答 R7 ·
  `especially when **there is a promotion**` ／ `you spot **a … promotion** on the product page`
  ——两处都用名词 promotion，没塞形容词/动词 ⇒ 毕业 12 天后第一次在自由产出里自发验到
  ★ 而且她是在**同一句里**把 #78（a pack of ／ the product page）和本条一起调出来的 ——
    这两条同源（都出自 08-09 那道网购题），块整体留住了
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `thers is a promotion on the product page.` —— there is ＋ **a promotion**（名词），⛔ 没塞形容词/动词；thers 属拼写（§2.1 不算错）
- 2026-09-29 📝 退池 · ① 同级说法
  "有个促销"说 it's on sale／discounted 完全合法（条目自己写着），there is a promotion 只是另一种说法；08-09 那次 ❌ 原话未存，此后五次全对

### 212 · 压缩出来的形容词两个出口（表语最省）
类型 结构 ｜ 旧号 B149
状态 连对2 连错0 上次2026-09-26 ｜ 题型 整句 ｜ 退池 ｜ **回潮 2026-09-18**（08-15 毕业 → 09-05 复检 ✅ → 09-18 复检答"忘了"，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-20**

**问题是什么**
**压缩出来的形容词两个出口，表语最省**：把中文"…得…不…"这种程度补语压成**一个形容词**放表语位 ——
主语 ＋ be ＋ 一个形容词（`the road is … **jammed**`）。
同一格里的邻居（别串）：⚠️ 修饰形容词要用副词形（`complete jammed` → **completely** jammed，归 🎓#202 同族）。
⚠️ 与 🎓#107（jammed／gridlocked）互斥写死（2026-09-05 c 段裁决）：
　**堵车那个形容词 ⇒ #107（词汇）／ 把"…得…不…"压成表语形容词 ⇒ 本条（结构）。**
　沿革：本条题面撞过两次（先撞 #108 packed、再撞 #107），现已换成"他气得说不出话。"
判据一句话：中文那一长串补语能不能压成一个形容词？能就放到 be 后面。
★ 与 🎓#163（"愣住了／说不出话" ＝ I just stood there／I froze）分工：那条走**动作**、题面排除 speechless；
　本条走**表语形容词**，speechless 正是合法答案之一 ⇒ 两条题面不同句（"气得说不出话" vs "愣在那儿"）、考点不同，互斥成立。

**怎么发现的**
旧 B 表迁移（B149，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组 ✅ `the road is … jammed`（走了表语出口）；同日按撞车裁决换了题面。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅）；09-05 唯一的顺带是 `complete jammed`（副词形，归 #202 同族）。触发原话未存。
找法：中文"…得…不…"先试着压成一个形容词，放到 be 后面。

**题面**
"他气得说不出话。"（用**表语**说：主语 ＋ be ＋ 一个形容词）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `the road is … jammed`（走了表语出口）
  ｜ ⚠️ `complete jammed` → completely（修饰形容词要用副词形），归 📝 🎓#202 同族，⛔ 不记 ❌
- 2026-09-05 📝 题面整改 · c 段撞车裁决（§3.1③ 第三档）
  与 🎓#107（jammed／gridlocked）撞车：本条题面「路上堵得一动不动。」与 #107「堵死了，一动不动」几乎同句，
  **而教练 09-05 给本条加的点名（"用表语说：主语 ＋ be ＋ 一个形容词"）恰好把她逼向 #107 的那个形容词**
  ⇒ 两条互相盖：先答哪条，另一条就只剩抄写。
  ⇒ 本条题面换成 **"他气得说不出话。"**（同一个考点：把中文的程度补语压成一个形容词放表语位），
    ⛔ 未动 #107 一个字（它的题面「堵死了，一动不动」按新粒度规则本来就是合格的词汇题）。
  ★ 互斥写死：**堵车那个形容词 ⇒ #107（词汇）／ 把"…得…不…"压成表语形容词 ⇒ 本条（结构）。**
  ★ 本条备注里已有一次同型整改（原题面的"地铁里人挤人"撞 #108 ⇒ 已删）——**这是第二次**。
- 2026-09-18 ❌ 复检 · 学习日 复检第 4 组 · 答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**
  最小改 `He was speechless.`
  ❌ "…气得说不出话"这一长串补语压成一个形容词放 be 后面：speechless ＝ 说不出话的；with anger 可以把"气"补回来
- 2026-09-19 ✅ 付息日 a 段在池第 1 组 · `he was speechless with anger.`——压成一个表语形容词 speechless，with anger 把"气"补回来（09-18 回潮后首测）
- 2026-09-19 📝 c 段 review · 与 🎓#163 的"说不出话"互斥核对（09-18 收尾待办）
  #163 走动作（stood there／froze）、题面排除 speechless；本条走表语形容词、speechless 是合法答案 ⇒ 题面不同句、考点不同，互斥成立；分工写进「问题是什么」
- 2026-09-20 ✅ 学习日 在池第 1 组 · `He is speechless with anger.` —— 主语 ＋ be ＋ 一个形容词表语，整串补语压成 speechless；连对2 ⇒ 毕业
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [1] · `he was speechless with anger.`
- 2026-09-29 📝 退池 · ① 同级说法
  "气得说不出话"说 He was so angry he couldn't speak 完全成立，压成一个表语形容词只是风格（旧题面还是"主语＋be＋一个形容词"形态描述）⇒ 中译英里产不出 ❌
- 备注 原题面还有"地铁里人挤人"，与 #108（packed）撞车 ⇒ 本条只留"路上堵得一动不动"

### 213 · 功能上线 ＝ go live／be released
类型 词组 ｜ 旧号 B150
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**功能上线 ＝ go live ／ be released**：`the developer **released** a wrong version.`
判据一句话：说"上线／发版"这个动作，动词落 go live 或 release。

**怎么发现的**
旧 B 表迁移（B150，2026-08-18）；最早记录 2026-08-09 ❌，触发原话未存。
2026-08-10 ✅ ／ 2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-01 📝 新题 P3（bank:490）自发命中留痕 · `because the developer **released** a wrong version.`
2026-09-05 复检第 1 组（打包）✅ be released。

**我错在哪**
她的：2026-08-09 记过一次 ❌（触发原话未存，旧 B 表迁移）。
找法：说"上线／发版"时动词直接落 go live 或 release。

**题面**
"这个功能上线"（⛔ 不许用 launch）

- 2026-08-09 ❌
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-01 📝 新题 P3（bank:490）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）
  `because the developer **released** a wrong version.` —— "上线/发版"这个动作的动词选对。
  ★ 同句里另有 ❌（`login in`，新建 #316）与 ⚪（`a wrong` → `the wrong`，归本档 #63），
    三处各归各号（§3.3 标记打在条目上，不打在整句上）。
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· be released
- 2026-09-18 📝 题面整改：补（⛔ 不许用 launch）· 复检组发题前审核（§6.5 第 7 项）
  `The feature launches.` 合法，绕开 go live／be released ⇒ 补排除项
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ①（原判据有误）
  "功能上线"说 launch 本身就是标准说法（旧题面"⛔ launch"是假错），go live／be released 同样对；08-09 那次 ❌ 原话未存

### 214 · 完成进行时 ＝ have been ＋ -ing
类型 语法 ｜ 旧号 B151
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-11** ｜ 退池 ｜ 题型 整句

**问题是什么**
**完成进行时 ＝ have been ＋ -ing**：`I've **been working** at this company for five years.`
（强调这五年一直在干、现在还在）
同一格里的邻居（别串）：`I've worked here for five years.` 完全合法（现在完成时），但不是本条要的形式
⇒ 2026-09-05 题面补点名（只点**时态类别**，⛔ 未给出 have been ＋ -ing）。
⚠️ 与 🎓#148 互斥写死：**状态动词（know／be）＋ for ⇒ #148 的完成时 ／ 动作动词（work／live）＋ for 且强调"一直在做" ⇒ 本条。**
判据一句话：强调"这段时间一直在做、现在还在做" ⇒ have been ＋ -ing。

**怎么发现的**
旧 B 表迁移（B151，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-10 ✅ ／ 2026-08-11 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 4 组 ✅ `I've been working at this company for five years.`——题面当天补了点名，整改后首测即过。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：要强调"一直在做、现在还在"时，把谓语拆成 have been ＋ -ing。

**题面**
"我在这家公司干了五年了。"（用**完成进行时**说 —— 强调这五年一直在干、现在还在）

- 2026-08-09 ✅
- 2026-08-10 ✅
- 2026-08-11 ✅
- 2026-09-05 ✅ 复检组 · 第 4 组 · `I've **been working** at this company for five years.`（have been ＋ -ing）
  ★ 本条题面今天补了点名（用完成进行时说），整改后首测即过；⛔ 只点了时态类别，没给形式。
- 2026-09-05 📝 题面整改 · 复检第 4 组发题前审核（§6.5 第 7 项）
  `I've worked here for five years.` 完全合法（现在完成时），但本条考的是**完成进行时**
  ⇒ 补点名（用**完成进行时**说 —— 强调这五年一直在干、现在还在）；⛔ 只点时态类别，未给 have been ＋ -ing。
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ① 同级说法
  `I've worked here for five years.` 完全合法（条目自己写着），完成进行时只是强调方式 ⇒ 中译英里产不出 ❌；历史零 ❌

### 215 · -ing 短语省主语的硬条件（逻辑主语＝主句主语）
类型 结构 ｜ 旧号 B153
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**-ing 短语省主语的硬条件：逻辑主语 ＝ 主句主语**。
· 成立：`kids put toys away **after playing** them.`（playing 的人就是主句主语 kids）
· **不成立**：玩的是孩子、收的是我 ⇒ 只能换成带自己主语的从句（`After kids played toys, I put them away.`）
同一格里的邻居（别串）：两句都能用 after 从句整句译出、-ing 就一次不出现 ⇒ 2026-09-07 题面补了
「两句都要求用 -ing 短语开头；哪一句这么说不通，就改成说得通的形式」（⛔ 不透露是哪一句不能用）。
判据一句话：-ing 那个动作是谁做的？跟主句主语不是同一个人 ⇒ ⛔ 不许省主语。

**怎么发现的**
旧 B 表迁移（B153，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-07 复检第 5 组 ✅ 两句分别处理 —— 句 1 用 -ing、句 2 换成带自己主语的 After 从句，正是本条要她做的判断。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅）；09-07 同题的 `play toys`（该 play **with** toys）已另建 #322。触发原话未存。
找法：要用 -ing 开头之前先问一句 —— 这个动作是主句主语做的吗？不是就老实写从句。

**题面**
"孩子玩完把玩具收起来。" ／ "孩子玩完之后我把玩具收了。"（两句都要求用 **-ing 短语**开头；哪一句这么说不通，就改成说得通的形式）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 📝 题面补「两句都要求用 -ing 短语开头；哪一句这么说不通，就改成说得通的形式」：
  原题面两句都可以整句用 after 从句译出，-ing 一次不出现 ⇒ 本条考点（逻辑主语＝主句主语）
  结构上测不到。新写法⛔ 不透露是哪一句不能用。
- 2026-09-07 ✅ 复检 · 第 5 组 · `kids put toys away after playing them.` ／
  `After kids played toys, I put them away.`
  —— 句 1 playing 的逻辑主语＝主句主语 kids ⇒ -ing 合法；句 2 玩的是孩子、收的是我 ⇒
  她没有硬套 -ing、换成带自己主语的 After 从句 ⇒ 正是本条要她做的判断
  ｜ ⚠️ play toys → play **with** toys（同题两次）⇒ 新建 #322
  ｜ ⚪ After kids → After **the** kids ⇒ 归 #63（形态类只记录）
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；-ing 短语的逻辑主语她每次都判对（09-07 两句分别处理正是这一判断）

### 216 · 东西不会自己 leave（His things ARE all over the floor）
类型 结构 ｜ 旧号 B154
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**东西不会自己 leave** —— 东西当主语时用 be：`His stuff **is** all over the floor.`
同一格里的邻居（别串）：🎓#186 的 leave a mess 是**人**当主语的块 —— 主语一换成东西就不能再用 leave。
判据一句话：主语是"东西" ⇒ 谓语用 be ＋ 位置（all over the floor）。

**怎么发现的**
旧 B 表迁移（B154，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-11 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 4 组 ✅ `His stuff is all over the floor.`——⛔ 没让东西自己 leave。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：主语一换成"东西"就先问一句 —— 它能自己做这个动作吗？不能就改成 be ＋ 位置。

**题面**
"他那些东西一地都是。"（东西当主语）

- 2026-08-09 ✅
- 2026-08-11 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 4 组 · `His stuff is all over the floor.` —— 东西当主语配 be，⛔ 没让东西自己 leave
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；东西当主语用 be ＋ 位置她一直对

### 217 · and 接第二个谓语时，否定必须带助动词
类型 语法 ｜ 旧号 B155
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**and 接第二个谓语时，否定必须带助动词**：
`Someone ran a red light **and didn't get fined**.`（⛔ 不是 and not get fined）
同一格里的邻居（别串）：`without being fined` 完全合法，但那样只剩一个谓语、考点没有落点
⇒ 2026-09-07 题面补点名「用 **and** 连两个谓语说」。
判据一句话：and 后面还是一个谓语 ⇒ 否定要自己带 didn't／doesn't，⛔ 不能光写 not。

**怎么发现的**
旧 B 表迁移（B155，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ◎ 题面没逼出。
2026-08-10 ✅ ／ 2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-07 复检第 5 组 ✅ `Someone ran a red light and didn't get fined.`——否定带住了助动词。

**我错在哪**
她的：本条判定里没有掉过（08-09 那次是 ◎ ＝ 题面没逼出），触发原话未存。
找法：and 后面要接第二个谓语时，先给它配一个自己的助动词再挂 not。

**题面**
"有人闯红灯还不用罚款。"（用 **and** 连两个谓语说 · ⛔ 不许用 get away with）

- 2026-08-09 ◎ 题面没逼出
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 📝 题面补点名「用 and 连两个谓语说」：原题面可合法译成 without being fined，
  只剩一个谓语 ⇒ 考点（and 接第二个谓语时否定必须带助动词）没有落点。
- 2026-09-07 ✅ 复检 · 第 5 组 · `Someone ran a red light and didn't get fined.`
  —— and 接第二个谓语时否定带住了助动词（**didn't** get fined），⛔ 没写成 and not get fined
  ｜ ⚠️ Someone ran → Some people run（中文"还不用罚款"说的是常态，不是一次具体事件）；考点不受影响
- 2026-09-19 📝 题面整改：补（⛔ 不许用 get away with）· 复检组发题前审核（§6.5 第 7 项）
  `Some people run red lights and get away with it.` 合法，第二个谓语不带否定，绕开"and 后否定要带助动词" ⇒ 补排除项
- 2026-09-19 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌（08-09 是 ◎）；and 后第二个谓语带助动词否定她一直对

### 218 · working people；traffic management 不带 the
类型 语法 ｜ 旧号 B156
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**working people**（上班族）；**traffic management 不带 the**（抽象领域泛指裸用）：
`working people.` ／ `**traffic management** mainly comes down to two things.`
同一格里的邻居（别串）：⚠️ "不带 the"这一格**只在句子里才现形** —— 裸词组谁都不会加 the
⇒ 2026-09-12 把两句统一成整句题。
判据一句话：抽象领域／一类人泛指 ⇒ 裸着用，⛔ 不加 the。

**怎么发现的**
旧 B 表迁移（B156，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-07 复检第 5 组 ✅ 两处泛指都是裸的（⛔ 无 the）；comes down to 是很地道的选择。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"某个领域／某一类人"时先别加 the —— 泛指就裸着用。

**题面**
"上班族最需要这个。" ／ "交通管理主要看两件事。"（第二句"交通管理"用 **management** 说）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 ✅ 复检 · 第 5 组 · `working people.` ／ `traffic management mainly comes down to two things.`
  —— 两处泛指都是裸的（⛔ 无 the）；comes down to 是很地道的选择
- 2026-09-12 📝 题面整改：「上班族」→「上班族最需要这个。」—— 两句统一成整句题（§6.0 一条一种形式；"不带 the"这一格只在句子里才现形，裸词组谁都不会加 the）· 全档题面 review
- 2026-09-19 📝 题面整改：补（第二句"交通管理"用 management 说）· 复检组发题前审核（§6.5 第 7 项）
  `Managing traffic comes down to two things.` 用动名词绕开 traffic management 这个名词块，冠词位不出现 ⇒ 点名 management
- 2026-09-19 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；泛指裸用（冠词类、从没掉过）她一直对

### 219 · 口语选词 complicated／takeaway
类型 词汇 ｜ 旧号 B158
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
口语选词：**complicated**（⛔ 不用 complex）／ **takeaway**（点外卖）。
判据一句话：口语里"复杂"默认 complicated、"外卖"默认 takeaway —— 各有一个默认款，别现挑。

**怎么发现的**
旧 B 表迁移（B158，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组（打包）✅ `too complicated`（⛔ 没用 complex）／`order takeaway`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：这两个词各有口语默认款 —— 复杂 complicated、外卖 takeaway。

**题面**
"太复杂了"（形容词，⛔ 不用 complex） ／ "点个外卖"（"外卖"用一个名词说 · ⛔ 不许用 food／delivery）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `too complicated`（⛔ 没用 complex）／`order takeaway`
- 2026-09-18 📝 题面整改：第二句补（"外卖"用一个名词说 · ⛔ 不许用 food／delivery）· 复检组发题前审核（§6.5 第 7 项）
  `order in`／`order food`／`order delivery` 都合法，绕开 takeaway ⇒ 限定成名词并排除两个泛称；takeout（美式）在规则内
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-19 ✅ 自发命中 · 付息日 d 段重答 R11（P3 · 自由产出）· `eat out or order takeout`——外卖走口语默认款（takeout 与 takeaway 同一个块）
- 2026-09-19 ✅ 自发命中 · 付息日 d 段重答 R12（P3 · 自由产出）· `order takeout, hail a ride, pay utility bills`
- 2026-09-29 📝 退池 · ① 同级说法
  "太复杂了"说 too complex 同样成立（旧题面"⛔ complex"是偏好不是错），takeaway 她一直对 ⇒ 中译英里产不出 ❌；历史零 ❌

### 220 · actually 的位置
类型 结构 ｜ 旧号 B159
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**actually 的位置**：落在**主语与动词之间**（be 动词则放它后面）——
`He can finally see how tall a T-rex **actually** was.`
判据一句话：actually 贴着谓语放，⛔ 别甩到句尾。

**怎么发现的**
旧 B 表迁移（B159，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-11 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 4 组 ✅ actually 落在主语与动词之间，位置对。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写 actually 时把它贴到谓语前面（实义动词前、be 动词后）。

**题面**
"他终于看到霸王龙到底有多高。"（"到底"用 **actually** 说）

- 2026-08-09 ✅
- 2026-08-11 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 4 组 · `He can finally see how tall a T-rex actually was.` —— actually 落在主语与动词之间，位置对
- 2026-09-20 ⚡ 自评免测 · 复检第 3 组（她答"直接过"）
- 2026-09-20 📝 学习日 新题 bank:1038（P3）· 自发命中留痕 · `people actually built this hundreds of years ago`（actually 的位置）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；actually 的位置她一直放对

### 221 · 肯定句里的 much → a lot of
类型 语法 ｜ 旧号 B161a
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**肯定句里的 much → a lot of**：`I spent **lots of** time on chemistry.`
同一格里的邻居（别串）：much 留给**否定句和疑问句**（don't have much time）；
#222（for long → a long time）与 #223（far → a long way）是同一族的另两格。
判据一句话：肯定句里说"很多／很久／很远"，一律换成 a lot of ／ a long time ／ a long way。

**怎么发现的**
旧 B 表迁移（B161a，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 4 组 ✅ `I spent lots of time on chemistry.`——⛔ 没用 much。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：先看这句是不是肯定句 —— 是 ⇒ much 换成 a lot of／lots of。

**题面**
"我在化学上花了很多时间。"

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 4 组 · `I spent lots of time on chemistry.` —— 肯定句用 lots of，⛔ 没用 much
- 2026-09-20 ⚡ 自评免测 · 复检第 3 组（她答"直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；肯定句用 a lot of 她一直对（much 这条错路从没走过）

### 222 · 肯定句里的 for long → a long time
类型 语法 ｜ 旧号 B161b
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**肯定句里的 for long → a long time**：目标形式是 `I waited **a long time**.`
同一格里的邻居（别串）：`for ages`（＝ #276）与 `for hours` 都是"我等了很久"的**合法**译法、也都绕开这一格
⇒ 2026-09-09 分两轮把两个都排除掉（⛔ 未点名 a long time —— 那是考点本身）。
⚠️ 与 #276 互斥写死：**"好久"用 ages 说 ⇒ #276 ／ 肯定句里的"久" ⇒ 本条（a long time）。**
判据一句话：for long 只活在否定句里；肯定句说"久"一律 a long time。

**怎么发现的**
旧 B 表迁移（B161b，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 4 组 ✅ `I wait for hours.`——按**题面**判（§3.3 硬顺序①）：本条真正守的错（for long）没有出现 ⇒ ✅；
同日两轮改题面，把 ages 与 hours 都排除掉，次日起按新题面测。

**我错在哪**
她的：本条判定里没有掉过；09-09 那次 `I wait for hours.` 合法且符合当时的题面 ⇒ 记 ✅（目标形式仍未测到）。触发原话未存。
找法：肯定句里说"很久"直接给 a long time —— for long 留给否定句。

**题面**
"我等了很久。"（⛔ 不许用 ages／hours —— 说的是"久"，不是"几个小时"）

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-09 📝 题面整改 · 复检第 4 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面可合法译成 `I waited for ages.` —— for long 那一格根本没出现，而且与 #276（"好久"用 ages 说）撞车：
  她 09-07 刚练过 ages ⇒ 这次极可能直接调它 ⇒ 补排除项「⛔ 不许用 ages」
  ⇒ 两条从此互斥（§3.1 判重三步 ③：像但目标形式不同 ⇒ 当场改题面互斥）；⛔ 未点名 a long time（那是考点本身）
- 2026-09-09 ✅ 复检 · 第 4 组 · `I wait for hours.`
  ★ 判 ✅ 的依据是**题面**（§3.3 硬顺序①）：题面只排除了 ages，for hours 是"我等了很久"的合法译法，
    且本条真正守的错（肯定句里的 for long）没有出现 ⇒ 合法且符合题面 ⇒ ✅
  ★ 目标形式仍是 `I waited a long time.` ⇒ 当场改题面（§3.3③）：排除项加 hours
  ｜ ⚪ 顺带：`wait` 没标过去（"等了"）—— 形态类，只记不判（见 #12）
- 2026-09-09 📝 题面整改（第二轮，当天）· §3.3③「她答得合法但不是条目预期 ⇒ 判 ✅ ＋ 当场改题面」
  她答 `I wait for hours.`（合法、符合题面）⇒ 判 ✅；目标形式 `a long time` 仍未测到
  ⇒ 排除项由「⛔ ages」扩成「⛔ ages／hours —— 说的是"久"，不是"几个小时"」，次日起按新题面测
- 2026-09-20 ⚡ 自评免测 · 复检第 3 组（她答"直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；肯定句说"很久"她从没用过 for long（旧题面还堆了排除项）

### 223 · 肯定句里的 far → a long way
类型 语法 ｜ 旧号 B161c
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**肯定句里的 far → a long way**：`I walked **a long way**.`
同一格里的邻居（别串）：far 留给否定句和疑问句（not far ／ How far…?）；
#221（much → a lot of）与 #222（for long → a long time）是同一族的另两格。
判据一句话：肯定句里说"很远"用 a long way。

**怎么发现的**
旧 B 表迁移（B161c，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 4 组 ✅ `I walked a long way.`——⛔ 没用 far。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：先看这句是不是肯定句 —— 是 ⇒ far 换成 a long way。

**题面**
"我走了很远。"

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 4 组 · `I walked a long way.` —— 肯定句用 a long way，⛔ 没用 far
- 2026-09-20 ⚡ 自评免测 · 复检第 3 组（她答"直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；肯定句说"很远"她一直用 a long way

### 224 · discrimination AGAINST sb；age discrimination 不可数
类型 搭配 ｜ 旧号 B165
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 词组

**问题是什么**
**discrimination AGAINST sb**（介词写死是 against）；**age discrimination 不可数**：
`**age discrimination against** people over 35`。
同一格里的邻居（别串）：#261（这一小撮抽象名词不可数）只管 feedback／advice 那几个词，
本条管 discrimination 这个**具体词**的可数性 ＋ 它的介词（2026-08-23 c 段定：不并、只交叉引用）。
判据一句话：discrimination 后面接对象一律 **against**，词本身不加 -s。

**怎么发现的**
旧 B 表迁移（B165，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-11 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 3 组 ✅ `age discrimination against people over 35`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写完 discrimination 直接接 against ＋ 被歧视的那群人；词尾不加 -s。

**题面**
"对 35 岁以上的人有年龄歧视"

- 2026-08-09 ✅
- 2026-08-11 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 3 组 · `age discrimination against people over 35`
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；discrimination against 她一直对

### 225 · 限定 ≠ 定指（她自己抓到的区别）
类型 语法 ｜ 旧号 B166
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 整句

**问题是什么**
**限定 ≠ 定指**（⭐ 她自己抓到的区别）：
`I want **a job** with no overtime, and **one** that is stable.`
—— job 后面挂了限定语，但它**仍是不定指** ⇒ 用 a job；第二个用 **one** 顶替，⛔ 不写 the job。
同一格里的邻居（别串）：🎓#198（the 的唯一功能 ＝ 双方都知道是哪一个）是同一条判据的正面说法。
判据一句话：后面挂了限定语 ≠ 对方知道是哪一个 —— 只有"双方都知道"才配 the。

**怎么发现的**
旧 B 表迁移（B166，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-10 ◎ 题面没逼出；2026-08-11 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 4 组 ✅ `I want a job with no overtime, and one that is stable.`——两处都对位。

**我错在哪**
她的：本条判定里没有掉过（08-10 那次是 ◎ ＝ 题面没逼出），触发原话未存。
找法：名词后面挂了一长串限定语时别顺手加 the —— 先问对方知不知道是哪一个。

**题面**
"我想要一份不加班的工作，还得是稳定的那种。"

- 2026-08-09 ✅
- 2026-08-10 ◎ 题面没逼出
- 2026-08-11 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 4 组 · `I want a job with no overtime, and one that is stable.`
  —— a job（限定不定指）＋ one that is stable（用 one 顶替、⛔ 没写 the job）两处都对位
- 2026-09-20 ⚡ 自评免测 · 复检第 4 组（她答"直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌（08-10 是 ◎）；这是她自己抓到的区别，a job … and one that … 她一直对（冠词类、从没掉过）

### 226 · 关系代词做宾语可省、做主语不可省
类型 结构 ｜ 旧号 B169
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**关系代词做宾语可省、做主语不可省**：
`Subjects (that) you'll actually use later`——that 是 use 的宾语 ⇒ **可省**；
关系词做从句主语时 ⇒ **不可省**。
同一格里的邻居（别串）：形容词／介词短语定语（useful in the future）完全合法，但一个关系代词都不出现
⇒ 2026-09-07 题面补点名「两个定语都用**从句**说」。
判据一句话：把关系词盖住念一遍从句 —— 还有主语吗？没有 ⇒ 它不能省。

**怎么发现的**
旧 B 表迁移（B169，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-07 复检第 5 组 ✅ 两个定语都用了从句、关系词都在（语言正确且符合题面）；
★ 但两个 that 都落在**宾语**位 ＝ 可省的那一档，本条真正的考点"做主语时不可省"没被测到
⇒ 按 §3.3③ 记 ✅ ＋ 当场改题面（第二个定语的中文主语改成"科目"本身，关系词只能做主语）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅）；09-07 那次考点没被测到，责任在题面。触发原话未存。
找法：把关系词盖住念一遍从句 —— 没主语了就说明它不能省。

**题面**
"以后真用得上的、或者能让你少走弯路的科目"（两个定语都用**从句**说）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 📝 题面补点名「两个定语都用从句说」：原题面可合法译成形容词/介词短语定语
  （useful in the future, common everywhere），一个关系代词都不出现 ⇒ 考点没有落点。
- 2026-09-07 ✅ 复检 · 第 5 组 · `Subjects that you'll actually use later, or ones that you run into everywhere.`
  —— 两个定语都用了从句、关系词都在，语言正确且符合题面（§6③）
  ★ 但两个 that 都落在**宾语**位（use／run into 的宾语）⇒ 都是"可省的那一档"，
    本条真正的考点「做主语时不可省」没被测到 ⇒ 按 §3.3③ 记 ✅ ＋ 当场改题面：
    旧 "以后真用得上的、或者到处都会碰到的科目" → 新 "以后真用得上的、或者能让你少走弯路的科目"
    （第二个定语的中文主语变成"科目"本身 ⇒ 关系词只能做主语 ⇒ 不可省，考点这才有落点）
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；关系词省不省她一直判对（类型 结构却标词组的旧题面一并作废）

### 227 · clear ≠ clean（形容词层面）
类型 词汇 ｜ 旧号 B170
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**clear ≠ clean（形容词层面）**：`air is **clean**`（干净、没脏东西）／ `it's **clear**`（晴、通透）。
同一格里的邻居（别串）：#190 是同一对词的**动词**层面（clear the table ≠ clean the table）。
判据一句话：说"脏不脏"用 clean；说"通不通透／晴不晴"用 clear。

**怎么发现的**
旧 B 表迁移（B170，2026-08-18），原始触发原话未存；最早记录 2026-08-09 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组（打包）✅ 两个形容词的分工都对。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：先问这句说的是"脏不脏"还是"通不通透" —— 脏用 clean、通透用 clear。

**题面**
"空气干净。" ／ "天很晴。"（两句都用一个 **c** 开头的形容词说）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `air is **clean**` ／ `it's **clear**`（形容词层面的分工）
- 2026-09-19 📝 题面整改：补（两句都用一个 c 开头的形容词说）· 复检组发题前审核（§6.5 第 7 项）
  `The air is fresh.`／`It's sunny.` 都合法，两句都绕开 clean／clear 的分工 ⇒ 首字母 c 同时框住两个词，分不分得开正是考点
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；clean air／clear sky 她一直对（旧题面还靠首字母 c 硬框）

### 228 · look after sb（照顾）
类型 词组 ｜ 旧号 B171d
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 词组

**问题是什么**
**look after sb** ＝ 照顾。
同一格里的邻居（别串）：take care of 完全合法，但绕开这个块 ⇒ 题面已排除；
🎓#95（be after ＝ 图个）与本条同一个 after、是两个不同的块，⛔ 别串。
判据一句话："照顾某人"直接调 look after。

**怎么发现的**
旧 B 表迁移（B171d，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 3 组 ✅ `look after kids`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"照顾"时先调 look after，⛔ 别退回 take care of。

**题面**
"照顾孩子"（⛔ 不用 take care of）

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 3 组 · `look after kids`
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 退池 · ① 同级说法
  "照顾孩子"说 take care of 完全成立（旧题面靠"⛔ take care of"硬框），look after 只是另一个说法 ⇒ 中译英里产不出 ❌；历史零 ❌

### 229 · complain 不及物（complaining about it）
类型 搭配 ｜ 旧号 B172
状态 连对3 连错0 上次2026-09-18 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**complain 不及物** —— 要接对象就得带 **about**：`complaining **about** it`。
判据一句话：complain 后面不能直接跟宾语，中间必须有 about。

**怎么发现的**
旧 B 表迁移（B172，2026-08-18），原始触发原话未存；最早记录 2026-08-10 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 5 组（打包）✅ `complain **about**`（不及物 ＋ about）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写完 complain 先补 about，再说抱怨的是什么。

**题面**
"抱怨这件事"（用 **complain** 说）

- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `complain **about**`（不及物 ＋ about）
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；complain about 她一直对（旧题面点名即答案）

### 230 · "什么样的" ＝ what kind of；"适合住" ＝ good to live in
类型 结构 ｜ 旧号 B174
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**"什么样的" ＝ what kind of**；**"适合住" ＝ good to live in**（句尾那个 in 不能丢）：
`**What kind of** city is **good to live in**?`
同一格里的邻居（别串）：`What makes a city a good place to live?` 完全合法，但两个考位一个都不出现
⇒ 2026-09-07 题面补了排除项（排除它不泄露任何一个考位）。
⚠️ 与 🎓#103（不定式后置修饰，介词留末尾）同一族：live **in** 的 in 就是留在句尾的那个介词。
判据一句话："什么样的"用 what kind of；"适合做某事"用 good to do ＋ 那个介词。

**怎么发现的**
旧 B 表迁移（B174，2026-08-18），原始触发原话未存；最早记录 2026-08-10 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-07 复检第 5 组 ✅ `What kind of city is good to live in.`——介词没丢。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：问"什么样的…"先落 what kind of；说"适合住"记得把 in 留在句尾。

**题面**
"什么样的城市适合住？"（⛔ 不许用 What makes … 起头 · ⛔ 不许用 Which 起头 · ⛔ 不许用 livable）

- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 📝 题面补「⛔ 不许用 What makes … 起头」：What makes a city a good place to live? 完全合法，
  但 what kind of 与 good to live in 两个考位一个都不出现。排除它不泄露任何一个考位。
- 2026-09-07 ✅ 复检 · 第 5 组 · `What kind of city is good to live in.`（what kind of ＋ good to live **in**，介词没丢）
- 2026-09-19 📝 题面整改：补（⛔ 不许用 Which 起头 · ⛔ 不许用 livable）· 复检组发题前审核（§6.5 第 7 项）
  `Which cities are good to live in?`／`What kind of city is livable?` 各绕开一半考点 ⇒ 补排除项
- 2026-09-19 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ① 同级说法
  "什么样的城市适合住"说 What makes a city a good place to live? 完全合法（条目自己写着，旧题面堆了三个排除项）；live in 的句尾介词归 🎓#103 管

### 231 · 说"两类/三类"时每类要用复数（the fun ONES）
类型 语法 ｜ 旧号 B176
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**说"两类／三类"时每类要用复数**：`Just two kinds: fun **ones** and useful **ones**.`
同一格里的邻居（别串）：与 **#198（the 的唯一功能）共用这句中文** —— 本条判 **ones**、#198 判 **the**；
两条都已毕业，回潮时先把题面改成互斥。
判据一句话：分成几类说时每一类都得是复数（ones／things），⛔ 不能只丢一个形容词。

**怎么发现的**
旧 B 表迁移（B176，2026-08-18），原始触发原话未存；最早记录 2026-08-10 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-07 复检第 5 组 ✅ `Just two kinds: fun ones and useful ones.`（两类各自都用复数 ones）。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"分成两类"时给每一类都配一个复数名词（ones），⛔ 别停在形容词上。

**题面**
"就两类，好玩的和有用的。"（两类各用一个名词短语说，⛔ 不许只说 fun and useful · ⛔ 不许用 stuff／things）

- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 ✅ 复检 · 第 5 组 · `Just two kinds: fun ones and useful ones.`（两类各自都用复数 ones）
- 2026-09-12 📝 题面整改：点名「单复数是考点…」→「两类各用一个名词短语说，⛔ 不许只说 fun and useful」（§10 禁令 5 禁预告测试点；与 #198 同句同改，本条判 ones、#198 判 the）· 全档题面 review
- 2026-09-19 📝 题面整改：补（⛔ 不许用 stuff／things）· 复检组发题前审核（§6.5 第 7 项）
  `fun stuff and useful stuff` 是不可数泛称，每类用复数（ones）那一格不出现 ⇒ 补排除项；与 #198 同句题面同步
- 2026-09-19 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；"分两类"每类配复数 ones 她一直对
- 备注 与 #198（the 的唯一功能）共用这句中文，回潮时先改成互斥题面

### 232 · to be HONEST（不是 honesty）
类型 词组 ｜ 旧号 B177
状态 连对3 连错0 上次2026-09-15 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**to be HONEST**（形容词，⛔ 不是 honesty）。
同一格里的邻居（别串）：`Honestly, …` 完全合法且常用，但那是**副词**、绕开词性考位
⇒ 2026-09-05 题面点名到"to be ＋ 一个形容词"（⛔ 未说是哪个 —— honest／frank 都算命中词性）；
⚠️ 与 #136（tell the truth）的分界：to be honest 是**插入语**，"说了实话"那件事的谓语才是 tell the truth。
判据一句话：be 后面要的是形容词 honest，⛔ 不是名词 honesty。

**怎么发现的**
旧 B 表迁移（B177，2026-08-18），原始触发原话未存；最早记录 2026-08-09 📖 给了才会。
2026-08-10 ✅ ／ 2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 复检第 1 组（打包）✅ to be honest（形容词，⛔ 不是 honesty）。

**我错在哪**
她的：2026-08-09 那次"给了才会"（📖），触发原话未存；此后没有掉过。
找法：to be 后面必须是形容词 —— honest，不是 honesty。

**题面**
**点名**："说实话"（用 **to be ＋ 一个形容词** 说）

- 2026-08-09 📖 给了才会
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 📝 题面整改 · 复检组第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面 "说实话，我没怎么想过这事。" 的默认译法 `Honestly, …` 完全合法且常用，
  但本条考的是 to be **honest**（不是 honesty）这个**词性** ⇒ 用副词就绕过去了。
  ⇒ 点名到 "to be ＋ 一个形容词"，⛔ 未说是哪个形容词（honest／frank 都算命中词性考位）。
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· to be honest（形容词，⛔ 不是 honesty）
- 2026-09-15 ✅ 新题 bank:1059 自发命中 · `To be honest, that's something I'd love to learn from him.`
- 2026-09-29 📝 退池 · ① 同级说法
  "说实话"说 Honestly 完全合法（条目自己写着），to be honest 她 08-10 起一直对（08-09 那次 📖 原话未存）⇒ 中译英里产不出 ❌

### 233 · either way ＋ you might as well
类型 词组 ｜ 旧号 B178
状态 连对2 连错0 上次2026-09-30 ｜ 题型 整句 ｜ **回潮 2026-09-05**（08-15 毕业 → 09-05 复检把 might as well 拆成 might … as well，撤销毕业、连对清零） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
**问题是什么**
两个块：**either way**（横竖都一样）＋ **you might as well**（那还不如）。
· 本条真正的考位是 **might as well 的内部词序** —— **as well 必须在动词前**
　（09-05 她写成 `might smile as well`，as well 退回本义"也"，"那还不如"整层丢失）
同一格里的邻居（别串）：整句意译 `Either way it's a day, so just smile.` 完全合法，
但两个目标块一个都不出现 ⇒ 题面正向点名 either way ／ might，as well 放在哪留给她。
判据一句话：写完 might，as well 必须紧跟着放在动词**前面**。

**怎么发现的**
旧 B 表迁移（B178，2026-08-18），原始触发原话未存；最早记录 2026-08-09 📖 给了才会。
2026-08-10 ✅ ／ 2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-05 ❌ 复检第 1 组（打包）· `it's one day either way, so you might smile as well.` ⇒ **回潮**
（either way 那一半对了，掉的是块的内部词序）。
2026-09-07 ✅ `It's one day either way, you might as well smile.`；2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。

**我错在哪**
她的：`so you might smile as well.`（2026-09-05 复检）　　正确：`so you **might as well smile**`
检查触发：写完 might，问一句 —— as well 在动词前面还是后面？必须在前面。

**题面**
"早去晚去都一样要排队，那还不如先去吃点东西。"（"都一样"用 **either way** 说，"那还不如"用 **might** 说）

- 2026-08-09 📖 给了才会
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 📝 题面整改 · 复检组第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面 "开心是一天，不开心也是一天，那还不如笑笑。" 可以整句意译
  （`Either way it's a day, so just smile.`）而**两个目标块一个都不出现**。
  ⇒ 按 §6 点名到两个块（either way ／ might as well），⛔ 未给整句答案 ——
    她仍要自己决定 either way 摆哪儿、might as well 后面接什么形式。
- 2026-09-05 ❌ 复检组 · 第 1 组（打包）· **回潮**
  `it's one day either way, so you might smile as well.` → so you **might as well smile**
  ❌ either way 那一半对了；might as well 被拆开 ⇒ as well 退回本义"也"，"那还不如"整层丢失。
  ★ 掉的是哪一格：不是"想不起这个块"，是**块的内部词序**（as well 必须在动词前）。
    ⇒ 回潮后的复测要能测到这一格：题面已点名两个块，考位就在摆放位置上。
  ★ 检查触发：写完 might，问一句 —— as well 在动词前面还是后面？必须在前面。
- 2026-09-07 ✅ 复习 · 在池第 1 组 · `It's one day either way, you might as well smile.`
  —— either way 挂句尾 ＋ might as well ＋ 原形（09-05 写成 might smile as well）
- 2026-09-09 ⚡ 自评免测 · 在池第 2 组（她原话："前 7 题直接过"）
- 2026-09-12 📝 题面整改：点名「用 either way 说」「用 might as well 说」→ 首字母＋词数提示 —— 原点名把两个目标块整个交出去（§6② 红线一）；09-05 那次拆成 might … as well 正说明给了块也白给 · 全档题面 review
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉首字母／词数／排除项，改整句、点名 either way 与 might —— as well 放在动词前还是后留给她（她掉过的正是 might smile as well）；换成排队场景
- 2026-09-30 ✅ 自发命中 · 付息日 d 段重答 bank:911 [S3] · `…, so you might as well smile.`

### 234 · older people／the elderly
类型 词汇 ｜ 旧号 B179
状态 连对2 连错0 上次2026-09-27 ｜ 题型 词组 ｜ 退池 ｜ **回潮 2026-09-05**（08-15 毕业 → 09-05 复检答"忘了"，撤销毕业、连对清零；★ 09-03 自由产出里刚有过自发命中留痕 ⇒ 认得出 ≠ 产得出） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
**问题是什么**
**older people ／ the elderly** ＝ 长辈们、上了年纪的人 —— 两个说法各占一个结构。
同一格里的邻居（别串）：seniors ／ elders ／ the old 也都说得通（09-03 她自由产出里就用过 seniors，⛔ 不判错）
⇒ 题面只给**结构骨架**（一个是 "…… people"、一个是 "the ……"），⛔ 没给 older／elderly 任何一个词。
判据一句话：一个走【形容词 ＋ people】，一个走【the ＋ 形容词】。
★ 09-03 自由产出里刚自发命中过、09-05 点名直测却答"忘了" ⇒ **认得出 ≠ 产得出**。

**怎么发现的**
旧 B 表迁移（B179，2026-08-18），原始触发原话未存；最早记录 2026-08-09 📖 给了才会。
2026-08-10 ✅ ／ 2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-03 📝 自发命中留痕 · `**older people** might ask for recommendations …`。
2026-09-05 ❌ 复检第 1 组（打包）· 她答"忘了"（§3.3「忘了/不会」也是 ❌）⇒ **回潮**；同日补题面点名。
2026-09-07 ✅ `older people, the erlerly`（拼写不算错）；2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。

**我错在哪**
她的：答"忘了"（2026-09-05 复检）　　正确：`Older people` ／ `the elderly`
找法：说"上了年纪的人"时给两个结构各填一个词 —— 形容词 ＋ people，或 the ＋ 形容词。

**题面**
"长辈们／上了年纪的人"（两个说法都要：一个是 "…… people"，一个是 "the ……"）

- 2026-08-09 📖 给了才会
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-03 📝 新题 P3（bank:831）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）
  `**older people** might ask for recommendations …`
  自由产出、无中文触发，是她自己调的词 ⇒ 本条考点位命中。
  ★ 同篇她也用了 `seniors` —— 两个词都对，并存不判。
- 2026-09-05 📝 题面整改 · 复检组第 1 组发题前审核（§6.5 **第 6 项** · 完整句）
  原题面 "长辈们常说……" 以省略号收尾，**不是完整句**，违 §6「题面必须是完整句」。
  ⇒ 补成 "长辈们常说年轻人不懂事。"。考位（长辈 ＝ older people／the elderly）一字未动，
    补出来的宾语与本条无关，⛔ 不构成新考点、⛔ 不影响连击。
- 2026-09-05 ❌ 复检组 · 第 1 组（打包）· **回潮** · 她答"忘了"（§3.3「忘了/不会」也是 ❌）
  给了答案：Older people often say young people don't know any better.
  ★ 本条 09-03 在自由产出里有过自发命中留痕（📝），今天点名直测却调不出来
    ⇒ 说明"能认出来"和"能产出"不是一格。
- 2026-09-05 📝 题面点名补齐 · 付息日 c 段（承接本日复检 ❌ 回潮）
  粒度整改把主体缩成了 "长辈们／上了年纪的人"（名词），但**不唯一可判** ——
  elders／seniors／the old 都能算"合法但非预期"，判卷时全靠教练裁。
  ⇒ 补最小点名："（两个说法都要：一个是 "…… people"，一个是 "the ……"）"
    —— 只给**结构骨架**，⛔ 没给 older／elderly 任何一个词（§6② 红线：不许把考点本身给出来）。
- 2026-09-07 ✅ 复习 · 在池第 1 组 · `older people, the erlerly`（拼写 elderly，§2.1 不算错）
- 2026-09-09 ⚡ 自评免测 · 在池第 2 组（她原话："前 7 题直接过"）
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 退池 · ① 同级说法
  "上了年纪的人"说 seniors／elderly people／older people 都成立（条目自己写着 seniors ⛔ 不判错），旧题面只能靠结构骨架硬框 ⇒ 任何一个对的说法都测不出缺口

### 235 · All you need to do is ＋ 原形
类型 结构 ｜ 旧号 B180
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 整句

**问题是什么**
**All you need to do is ＋ 原形**：`**All** you need to do **is speak** more and listen more.`
同一格里的邻居（别串）：`You just need to …` 完全合法，但这个框整个不出现 ⇒ 2026-09-07 题面点名"用 **All** 起头说"；
`All you need do is …` 也是标准说法（need 在这里当情态动词，英式常见）⇒ ⛔ 不算错，
只是口语默认走 All you need **to** do is …。
判据一句话：All … is 后面接**动词原形**，⛔ 不加 to。

**怎么发现的**
旧 B 表迁移（B180，2026-08-18），原始触发原话未存；最早记录 2026-08-10 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-07 复检第 5 组 ✅ `All you need do is speak more and listen more.`——框 ＋ 原形两个考位都中。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：用 All … is 这个框时，is 后面直接上动词原形。

**题面**
"你要做的就是多说多听。"（用 **All** 起头说）

- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 📝 题面补点名「用 All 起头说」：原题面可合法译成 You just need to …，
  All you need to do is ＋ 原形 这个框整个不出现。§6② 允许点"用哪个词起头"。
- 2026-09-07 ✅ 复检 · 第 5 组 · `All you need do is speak more and listen more.`
  —— All … is 的框 ＋ is 后面接原形，两个考位都中。`All you need do is …` 是标准说法
  （need 在这里当情态动词，英式常见）⇒ ⛔ 不算错；⚠️ 口语默认走 All you need **to** do is …
- 2026-09-19 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 退池 · ① 同级说法
  `You just need to speak more and listen more.` 完全合法（条目自己写着），All … is 只是另一种框 ⇒ 中译英里产不出 ❌；历史零 ❌

### 236 · 说人的目的用不定式 to do；for ＋ -ing 是物品用途
类型 结构 ｜ 旧号 B182
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-29**（连对2 · 回潮后走完两次）｜ **回潮 2026-08-27**（08-15 毕业 → 08-27 首犯 → 08-28 拿回第一次 → 08-29 换句复测拿回第二次）｜ 题型 整句

**问题是什么**
**说人的目的用不定式 to do；for ＋ -ing 是物品用途。**
判据（2026-08-27 回潮当天补写 —— 本条建立至今只有三行 ✅、没有判据块）：
```
**表"目的/用来做什么"，看挂在谁后面：**
① 挂在**句子**上（状语）＝ 人的目的 ⇒ **to do**
   ✅ I learn languages **to express myself** and understand others.
   ✗ I learn languages for expressing myself.
② 挂在**物品**上（用途）⇒ **for ＋ -ing**
   ✅ This app is **for booking** tickets.　✅ a box **for keeping** cables
③ 挂在**名词**上（那个名词"用来做什么"）⇒ **to do** ／ **for doing** ／ **why ＋ 主谓**
   ✅ a reason **to bring** the family together　✅ a reason **for doing** it
   ✅ the reason **why** we do it
   ✗ a reason **bringing** the family together
     —— 光挂一个 -ing 会被读成"这个理由**正在**把家人聚起来"（省略的定语从句），不是目的
★ 边界（别把它判成错）：**the ＋ 名词 ＋ -ing** 在讲"当时正在起作用的那个东西"时是成立的：
  ✅ The real reason **bringing** them together was money.
  区别在**冠词和语义**：a reason ＋ 目的义 ⇒ 只有 to do／for doing／why 三条路
★ 与 🎓#295 的分工写死：**#295** 管的是名词 **purpose** 的介词搭配（the purpose **of** doing）；
  **本条** 管的是"目的该用什么形式挂上去"。两条题面互斥（一个"做事的目的"、一个"聚一聚的理由"）
```

**怎么发现的**
旧 B 表迁移（B182，2026-08-18），原始触发原话未存；最早记录 2026-08-10 ✅（08-10／08-13／08-15 三次 ✅ 全落在**状语位**）。
2026-08-27 ❌ **回潮** · 付息日 d 段重答 R5 · 触发原话 `it's more about **a reason bringing** my family together`
（→ a reason **to bring** my family together）—— 掉的是**名词后面挂目的**那一格，原题面只覆盖状语位 ⇒ 当天补第二句题面。
★ 判重的决定性证据：按本条规则去改就得到正确答案 ⇒ 同一条规则、归本条；
　对照 **#295**：那次按本条改会得到 `the purpose to do things`（也是错的）⇒ 本条给不出答案 ⇒ 那次才新建。
2026-08-28 ✅ ／ 2026-08-29 ✅（当天换句，避开与 #306 的撞车）⇒ 连对 2，第二次毕业。
2026-09-11 复检 ✅ 考点位置（"为了"）走的是不定式 to express。

**我错在哪**
她的：`a reason bringing my family together`（2026-08-27 重答 R5）
正确：`a reason **to bring** my family together`
检查触发：写完"一个……的理由／办法／机会"，回头看后面那个动词 —— **是 to do 吗？**

**题面**
"这次同学聚会给了大家一个重新联系起来的理由。"
　　★ 零提示：a reason to reconnect／a reason for getting back in touch 都算对；她掉过的是"理由"后面挂光秃秃的 -ing（a reason bringing …）

- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-27 ❌ **回潮** · 付息日 d 段重答（R5 What are the differences between everyday food
  and festival food?）· `it's more about **a reason bringing** my family together`
  → a reason **to bring** my family together
  ★ **判重的决定性证据（为什么不新建号）**：按本条的规则去改，得到的正是 `a reason to bring`
    —— **本条给得出那个正确答案 ⇒ 是同一条规则**，归本条、判回潮。
    ★ 对照 **#295**：那次按本条改会得到 `the purpose to do things`（也是错的）
      ⇒ 本条给不出答案 ⇒ 那次才新建。**两次用的是同一个判据，方向相反**
  ★ 她掉的那一格是**名词后面挂目的**，原题面只覆盖状语位 ⇒ 当天补了第二句题面
- 2026-08-27 ⚪ **只记录，不推进连击**（**她当场裁的**：教练提案改判、她答"可以只记录"）·
  同日 · 自发命中 · 付息日 d 段第 2 道重答 R7（本条未被出题）·
  `Imagine you're on Amazon **to buy** a pack of tissues` ／
  `people don't even slow down **to ask** if they actually need something`
  ——两处 to 表目的，形式对，**但不计入连对，状态行一个字不动**（仍是 连对0 连错1 回潮）
  ★ 改判理由（教练提案 → 她认可）：这两处都是【**状语位**】——
    正是她**一直就稳的那一半**（08-10／08-13／08-15 三次 ✅ 全是状语位）。
    她今天回潮掉的是【**名词后面挂目的**】那一格（a reason ___ bring my family together），
    **本篇一次都没测到**。
    若按 §4① 加速通道照记 ✅，本条会**在从没修过掉的那一格的情况下重新毕业** ⇒ 假毕业
  ⇒ **出题约束（写死）：本条回潮后的复测，一律用今天新加的第二句题面**
    （"过年更多的是给全家一个聚一聚的**理由**"）—— 状语位那一半不再单独用来凑毕业
- 2026-08-28 ✅ 复习第1组 · **回潮后第一次复测，用的正是 08-27 新加的第二句题面**（名词后面挂目的，
  ＝ 她掉的那一格）· `Chinese New year is more about giving the whole family **a reason to get together**.`
  ——考点位置一字不差 ⇒ 连对0 → **1**。★ 出题约束照旧：本条以后的复测仍用第二句题面
- 2026-08-29 ✅ 复习第1组（**题面当天换句**：旧稿与 #306 共用"更多的是"＝§6.5⑧撞车，且与 08-28 一字不差
  ＝ 测昨天的记忆。新句"春节给全家提供了一个聚在一起的理由"仍打在同一格：名词 ＋ to do）·
  `Chinese New Year provides the entire family with **a reason to get together**.`
  ——换了句子照样打中 ⇒ **不是昨天的记忆，是规则** ⇒ 连对1 → **连对2，毕业**
  ⚠️ 同句 `provides … with` ／ `the entire family` 属书面登记 ⇒ 更好版降级 `gives the whole family a reason to…`
     —— 只进 diff-2，**不判 ❌、不触发 🎓#206 回潮**：这句英文本身成立，且书面登记是**我的题面诱导的**
     （题面写"提供"，直译就是 provide；08-28 旧题面写"给"，她当时产出的就是 giving）
  ⛔ **教练留痕**：中文题面的动词选词直接决定她调哪个英文动词 ⇒ 以后想让她走口语版的题面，
     中文就用大白话动词（给／让／带），不用书面动词（提供／实现／进行）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 4 组 · `Language learning is all to express youself and understand others.`
  —— 考点位置（"为了"）走的是**不定式** to express，⛔ 没走 for expressing ⇒ 本条考点命中
  ⚠️ 句框 `is all to ＋ 动词` 不成立（**题面诱发**：我禁了 about，她没备用框）⇒ ⛔ 不落本条、不另建号；
    正路：`You learn a language to express yourself…`／`The whole point of learning a language is to express…`
  ⚠️ 第二句「过年给了大家一个聚在一起的理由。」**未答**（漏了，不是"忘了"）⇒ 只留痕、⛔ 不计 ❌
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）
  去掉负向排除与"用不定式挂上去"形态描述；只留她掉过的那一格（名词后挂目的），改成零提示一句（a reason to … ／ a reason for -ing 都算对）；换成同学聚会场景

### 237 · a mixed bag（⭐ 她自产）
类型 词组 ｜ 旧号 B183
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-15** ｜ 退池 ｜ 题型 词组

**问题是什么**
**a mixed bag**（⭐ 她自产）＝ 好坏参半（【a ＋ 形容词 ＋ 名词】）。
同一格里的邻居（别串）：a mixed blessing 也说得通，但那是另一个块 ⇒ 题面已排除 blessing；
口语常见的软化形是 `It's a bit of a mixed bag.`（08-20 她自己就这么开的场）。
判据一句话："有好有坏"这一层整块调 a mixed bag。

**怎么发现的**
旧 B 表迁移（B183，2026-08-18；⭐ 她自产），原始触发原话未存；最早记录 2026-08-10 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-08-20 ✅ **自发命中**（加练新题开场第一句 `It's a bit of a mixed bag.`）—— 毕业后 5 天仍在线。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"有好有坏"时整块调 a mixed bag，⛔ 别滑到 blessing。

**题面**
"好坏参半"（用【a ＋ 形容词 ＋ 名词】说 · ⛔ 不许用 blessing）

- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-20 ✅ **自发命中**（加练新题开场第一句 `It's a bit of a mixed bag.`）——毕业后 5 天仍在线
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 3 题整串，她原话："1-4 直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；a mixed bag 是她自产的块、08-20 自发用出

### 238 · move on ≠ move forward
类型 词汇 ｜ **合并条·出题多句覆盖**（§3.2c，2026-09-07 定：只出一句测不到这一对的分工）｜ 旧号 B184
状态 连对2 连错0 上次2026-10-02 ｜ **🎓 已毕业 2026-09-19** ｜ 题型 整句 ｜ **合并条·出题多句覆盖** ｜ **回潮 2026-09-15**（09-10 第二次毕业 → 09-15 复检答"忘了"，两个成员都没出来，撤销毕业、连对清零）
**问题是什么**
**move on ≠ move forward** —— 一道题面两个成员，本条考的就是这两个块的分工：
· **move on** ＝ 翻篇、别老想着了（`It's in the past, just **move on**.`）
· **move forward** ＝ 继续往前推进（`the company has to keep **moving forward**.`）
同一格里的邻居（别串）：`move ahead` 同样是 move 起头、同样地道（答它算对）—— 真正要分的是 on 与 forward／ahead。
判据一句话：放下过去 ⇒ move **on**；事情继续推进 ⇒ move **forward**。
★ 08-10／08-13／08-15 那三次 ✅ 是在旧题面（"一直往前走"）下拿到的，**两个块都套得上** ⇒ 证明不了她分得清。

**怎么发现的**
旧 B 表迁移（B184，2026-08-18），原始触发原话未存；最早记录 2026-08-10 ✅（旧题面下的三次 ✅ ＝ 白测）。
2026-09-07 📝 题面整改 ＋ 转合并条；同日 ❌ 复检第 5 组（加练）· 两个成员只到一个 ——
只给了 `move forward`，第 ① 句要的 **move on** 没出来 ⇒ **回潮**（新题面第一次上场就抓到了这一格）。
2026-09-09 ⚡ 自评免测 ／ 2026-09-10 ✅ 两个成员都到 ⇒ 连对 2，第二次毕业（**新题面下**第一次走完连对 2）。

**我错在哪**
她的：2026-09-07 复检只给出 `move forward`，`move on` 一次没出现；2026-09-15 复检两句都答"忘了"
正确：`① It's all in the past, just move on. ② No matter what happens, the company still has to move forward.`
找法：先分一刀 —— 放下过去用 move **on**，事情往前推进用 move **forward**。

**题面**
★ 2 句，两个成员各一句 —— 本条考的就是这两个块的分工，只出一个等于没测
　① "分手都半年了，你也该放下了。"（"放下"用 **move** 说）
　② "项目遇到了点麻烦，但我们还是得接着往前推进。"（"往前推进"用 **move** 说）

**成员出题账**
① move on ｜ 09-07 ❌ · 09-10 ✅ · 09-15 ❌ · 09-18 ✅ · 09-19 ✅ · 10-02 ✅
② move forward ｜ 09-07 ✅ · 09-10 ✅ · 09-15 ❌ · 09-18 ✅ · 09-19 ✅ · 10-02 ✅
★ 08-10／08-13／08-15 三次在旧题面下（两个块都套得上）⇒ 无法按成员记录；09-09 ⚡ 自评免测也未按成员记录。

- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 📝 题面整改 ＋ 转合并条（§3.2c / §6「题面必须唯一可判」）：原题面「"一直往前走"（用 move 说）」
  ——move on 和 move forward **两个都套得上**，而本条考点恰恰是这两个的分工
  ⇒ 原题面在结构上测不到自己的考点，三次 ✅ 都无法证明她分得清。
  改成两句、两个成员各一句：① "都过去了，别老想着了。" ② "不管出什么事，公司还是得往前推进。"
  状态行加 `合并条·出题多句覆盖`，⛔ 连击数字与毕业日一个字不动。
- 2026-09-07 ❌ 复检 · 第 5 组（加练）· 合并条两个成员只到一个：只给了 `move forward`，
  第 ① 句"都过去了，别老想着了"要的 **move on** 没出来 ⇒ 🎓 回潮
  最小改 `① Just move on. ② The company still has to move forward.`
  ★ 今天发题前刚把本条题面从"一直往前走（用 move 说）"改成两成员对照 —— 旧题面两个都套得上，
    08-10／08-13／08-15 三次 ✅ 全是白测；新题面第一次上场就抓到了这一格。
- 2026-09-09 ⚡ 自评免测 · 在池第 2 组（她原话："前 7 题直接过"）
- 2026-09-10 📝 题面 ② 补排除项「⛔ 不许用 ahead」· 在池第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  第 ② 句「不管出什么事，公司还是得往前推进。」（用 move 说）—— `move ahead` 同样是 move 起头、
  同样地道，且同样证明她没错用 move on ⇒ 判 ✅ 不吃亏，但本条 09-07 刚为"两个成员的分工"改过题面，
  成员 ② 的目标形式必须是 move forward 才测得到那一格。
  ⇒ 补排除项 `⛔ 不许用 ahead`；第 ① 句不动（move on 在"用 move 说"下已唯一）。
- 2026-09-10 ✅ 复习 · 在池第 1 组 · 合并条两个成员都到
  `① It's in the past, just move on. ② No matter what happens, the company has to keep moving forward.`
  ★ 09-07 只到 move forward、move on 没出来；这次分工分清了 ⇒ **连对2，毕业**
  ⚪ 同句 `No matter what happen` 主谓一致 ⇒ 记在 #10，形态类不判档位（§3.4②）
- 2026-09-15 📝 题面整改 · 复检第 3 组发题前审核（§6.5 第 7 项：② "往前推进"用 move on 也说得通）
  旧：② "不管出什么事，公司还是得往前推进。"（用 **move** 说 · ⛔ 不许用 ahead）
  新：② "不管出什么事，公司还是得往前推进。"（用 **move** 说，"推进"是往前取得进展 · ⛔ 不许用 ahead）
- 2026-09-15 ❌ 复检第 3 组 · 答"忘了"，两个成员都没出来 ⇒ **回潮**
  最小改 `① It's all in the past, just move on. ② No matter what happens, the company still has to move forward.`
  ❌ 放下过去 ⇒ move on；事情继续往前推进 ⇒ move forward
- 2026-09-18 📝 题面整改：① 补（⛔ 不许用 past）· 发题前审核（§6.5 第 7 项）
  `move past it` 同样用 move、同样能翻"别老想着了"，绕开成员 ① move on ⇒ 补排除项
- 2026-09-18 ✅ 学习日 在池第 1 组 · ① `It's in the past, move on.` ② `No matter what happened, the company still needs to move forward.`——两个成员都对（09-15 回潮后首测）
  ｜⚠️ what happened → what happens（泛指以后）只进 diff-2
- 2026-09-19 ✅ 付息日 a 段在池第 1 组 · ① `It's in the past, just move on.` ② `No matter what happens, the company still needs to move forward.`——两个成员都对 ⇒ **连对 2，毕业**
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"⛔ past／⛔ ahead"，两个成员各一句、只点名 move（on／forward 的分工留给她）；换成分手、项目推进两个新场景；move ahead 同样算对
- 2026-10-02 ✅ 复检 · 学习日 复检第 4 组 [5] · ① `You lost the game, but stop dwelling on it and just move on.` ② `With the funding secured, construction of the new subway line can finally move forward.` —— ① move on ② move forward，两个成员都分对

### 239 · miss out on sth
类型 词组 ｜ 旧号 B185
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **回潮 2026-09-07**（08-15 毕业 → 09-07 复检写成 `miss something like friendship`，**out on 整个丢了**，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-10**（连对2 ＝ 09-09 ⚡ 自评免测 ＋ 09-10 ✅；09-07 回潮后第二次毕业）
**问题是什么**
**miss out on sth** ＝ 本来能得到却没得到。
同一格里的邻居（别串）：光一个 miss ＝ 想念／没赶上（miss the bus）；lose out on 同样地道，
但绕开 miss out on 这个块 ⇒ 2026-09-07 题面点名「用 **miss** 说」（点动词、⛔ 不泄露 out on）。
判据一句话：说"错过了本该属于自己的东西" ⇒ miss **out on**，两个小词都不能丢。

**怎么发现的**
旧 B 表迁移（B185，2026-08-18），原始触发原话未存；最早记录 2026-08-10 ✅。
2026-08-13 ✅ ／ 2026-08-15 ✅ ⇒ 连对 3，毕业。
2026-09-07 ❌ 复检第 5 组（打包）· `miss something like friendship` —— **out on 整个丢了** ⇒ **回潮**。
2026-09-09 ⚡ 自评免测 ／ 2026-09-10 ✅ `miss out on things like friendship` ⇒ 连对 2，第二次毕业。

**我错在哪**
她的：`miss something like friendship`（2026-09-07 复检）　　正确：`miss **out on** things like friendship`
找法：写完 miss 就问一句 —— 是"想念／没赶上"还是"本来能得到却没得到"？后者必须补 out on。

**题面**
"他整天埋头加班，错过了孩子成长的很多瞬间。"（"错过"用 **miss** 说）

- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 📝 题面补点名「用 miss 说」：原题面没点动词，lose out on 同样地道 ⇒ 考位（miss out on 的 out on）
  可能测不到。点 miss 不泄露 out on。
- 2026-09-07 ❌ 复检 · 第 5 组（打包）· `miss something like friendship` —— **out on 丢了** ⇒ 🎓 回潮
  最小改 `miss out on things like friendship`
  ★ 光 miss ＝ 想念／没赶上；"本来能得到却没得到"必须 miss **out on** sth。
- 2026-09-09 ⚡ 自评免测 · 在池第 2 组（她原话："前 7 题直接过"）
- 2026-09-10 ✅ 复习 · 在池第 1 组 · `miss out on things like friendship` —— out on 一个字没丢
  ★ 09-07 掉的正是 out on（写成 miss something like friendship）⇒ **连对2，毕业**
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 miss，out on 两个小词留给她（她掉过的正是 out on 整个丢了）；换成加班错过孩子成长场景

### 240 · keep an eye ON sth
类型 搭配 ｜ 旧号 B189
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 词组

**问题是什么**
**keep an eye ON sth** ＝ 留意（介词写死是 on）。
同一格里的邻居（别串）：🎓#105（keep one eye on X and one on Y ＝ 兼顾两头）是**另一个整句块**——
2026-08-19 判重结论已写死**不合并**，两条题面互不撞车；
#294（be mindful of）与本条是**同义替换**关系，题面互斥（#294 点名 mindful，本条点名 eye）。
判据一句话：keep an eye 后面接对象一律 **on**。

**怎么发现的**
旧 B 表迁移（B189，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ◎ 题面没逼出 → 改点名。
2026-08-12 ✅ ／ 2026-08-16 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 3 组 ✅ `keep an eye on prices`。

**我错在哪**
她的：本条判定里没有掉过（08-11 那次是 ◎ ＝ 题面没逼出），触发原话未存。
找法：写完 keep an eye 直接接 on ＋ 要留意的东西。

**题面**
**点名**："留意点价格"（用 keep an eye 说一遍）

- 2026-08-11 ◎ 题面没逼出 → 改点名
- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 3 组 · `keep an eye on prices`
- 2026-09-20 ⚡ 自评免测 · 复检第 4 组（她答"直接过"）
- 2026-09-29 📝 退池 · ① 同级说法
  "留意价格"说 watch prices／keep track of prices 都成立，keep an eye on 只是其中一个（旧题面点名即答案）；历史零 ❌（08-11 是 ◎）

### 241 · half 放在冠词前面（half an hour）
类型 语法 ｜ 旧号 B196
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 词组

**问题是什么**
**half 放在冠词前面**：`**half an hour**`（⛔ 不是 a half hour）。
判据一句话：half 是前置限定词 —— 它站在 a／an／the 的**前面**。

**怎么发现的**
旧 B 表迁移（B196，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 4 组 ✅ `half an hour`——half 在冠词前。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写 half 时先把它放到冠词前面 —— half an hour，不是 a half hour。

**题面**
"半小时"（用 **half** 说）

- 2026-08-11 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 4 组 · `half an hour` —— half 在冠词前
- 2026-09-20 ⚡ 自评免测 · 复检第 4 组（她答"直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；half an hour 她一直对（a half hour 在美式里也不算错）

### 242 · 介词＋抽象名词的方式块（in moderation／on purpose）
类型 词组 ｜ 旧号 B208
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 词组

**问题是什么**
**介词 ＋ 抽象名词的方式块**：**on purpose** ／ in moderation —— 用【介词 ＋ 名词】说"怎么做的"，⛔ 不用 -ly 副词。
同一格里的邻居（别串）：🎓#72 就是这一族里的 in moderation —— 那条单独立号考"适度"这个**意思**，本条考的是**这种结构**。
判据一句话：这一层能不能用【介词 ＋ 名词】说？能就别退回 -ly 副词。

**怎么发现的**
旧 B 表迁移（B208，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-15 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-08-24 ✅ 自发命中（新题 bank:924）· `More importantly, **everything in moderation**.`——整块调出来、位置也对。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"怎么做的"这一层先试【介词 ＋ 名词】（on purpose／in moderation），装得下就别用 -ly。

**题面**
"故意"（用【介词＋名词】那种说法，不用 -ly 副词）

- 2026-08-12 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-08-24 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 新题 bank:924 ·
  `More importantly, **everything in moderation**.`——整块调出来，位置也对
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 4 题整串，她原话："1-4 直接过"）
- 2026-09-29 📝 退池 · ① 同级说法
  "故意"说 deliberately／intentionally 完全成立（旧题面靠"不用 -ly"形态描述硬框），on purpose 只是另一种说法；历史零 ❌

### 243 · 形容词 ＋ 固定介词整块记（familiar WITH／interested IN）
类型 搭配 ｜ 旧号 B212
状态 连对3 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17** ｜ 退池 ｜ 题型 词组

**问题是什么**
**形容词 ＋ 固定介词整块记**：familiar **WITH** ／ interested **IN** ——
`I'm not **interested in** that at all.`
同一格里的邻居（别串）：🎓#193（lose interest **in**）与本条共用同一对 interest ＋ in ——
那条管**名词**形，本条管**形容词**形。
判据一句话：这一类形容词的介词是**块的一部分**，跟形容词一起背。

**怎么发现的**
旧 B 表迁移（B212，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-08-16 ✅ ／ 2026-08-17 ✅ ⇒ 连对 3，毕业。
2026-09-09 复检第 4 组 ✅ `I'm not interested in that at all.`

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：这类形容词别单背 —— 把介词一起记（familiar with／interested in）。

**题面**
"对那个一点兴趣都没有"（用 **interested** 说）

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-17 ✅
- 2026-09-09 ✅ 复检 · 第 4 组 · `I'm not interested in that at all.` —— interested **in**
- 2026-09-20 ⚡ 自评免测 · 复检第 4 组（她答"直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；interested in／familiar with 她一直对

### 244 · sing along
类型 词组 ｜ 旧号 B57a
状态 连对1 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-11（08-17 复查通过）** ｜ 退池 ｜ 题型 词组

**问题是什么**
**sing along** ＝ 跟着一起唱（**along** 是块的一部分）。
同一格里的邻居（别串）：with／together 说得通，但绕开 along 这个小品词 ⇒ 题面已排除。
判据一句话："跟着（音乐／别人）一块儿做"这一层用 **along**。

**怎么发现的**
旧 B 表迁移（B57a，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅ ⇒ 毕业。
2026-08-17 ✅ 复查（拆号继承毕业的四条之一，复查通过）。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"跟着一起唱"时，动词后面直接挂 along。

**题面**
"跟着歌手一起唱"（用 **sing** 起头说，⛔ 不许用 with／together）

- 2026-08-11 ✅
- 2026-08-17 ✅ 复查（拆号继承毕业的四条之一，复查通过）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 3 题整串，她原话："1-4 直接过"）
- 2026-09-29 📝 退池 · ① 同级说法
  "跟着一起唱"说 sing with them／sing together 都能懂能用（旧题面靠排除项硬框），sing along 只是更地道的一个；历史零 ❌

### 245 · rather than 两边同形（helps…rather than replaces）
类型 结构 ｜ 旧号 B114a
状态 连对1 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-11（08-17 复查通过）** ｜ 退池 ｜ 题型 整句

**问题是什么**
**rather than 两边同形**：`it **helps** you rather than **replaces** you.`（两侧都是三单）
同一格里的邻居（别串）：🎓#246 管的是 rather than **领独立短语时用 -ing**；#75 管的是 rather than 与 other than 的**词义**辨析
—— 三条各管一格。
判据一句话：rather than 两边挂的东西，形式必须一模一样。

**怎么发现的**
旧 B 表迁移（B114a，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅ ⇒ 毕业。
2026-08-17 ✅ 复查。
2026-09-11 复检 ✅ `it helps you rather than replaces you.`——两侧同形（helps／replaces），一字不差。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写完 rather than，把两边摆在一起看一眼 —— 形式一样吗？

**题面**
"它是帮你，不是取代你。"（用 **rather than** 说）

- 2026-08-11 ✅
- 2026-08-17 ✅ 复查
- 2026-09-11 ✅ 复检 · 付息日 a2 第 6 组 · `it helps you rather than replaces you.` —— rather than 两侧同形（helps／replaces），一字不差
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；rather than 两边同形她一直对

### 246 · rather than 领独立短语时用 -ing
类型 结构 ｜ 旧号 B114b
状态 连对1 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-11（08-17 复查通过）** ｜ 退池 ｜ 题型 整句

**问题是什么**
**rather than 领独立短语时用 -ing**：`**Rather than taking** the bus, I walk.`
同一格里的邻居（别串）：🎓#245 管的是 rather than **两边同形**（helps／replaces）；#75 管的是它与 other than 的**词义**辨析。
判据一句话：rather than 后面自己领一个短语（不跟前面的动词并列）⇒ 动词写成 **-ing**。

**怎么发现的**
旧 B 表迁移（B114b，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅ ⇒ 毕业。
2026-08-17 ✅ 复查。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：rather than 后面是它自己领头的短语吗？是 ⇒ 动词写成 -ing。

**题面**
"与其坐公交，我走路。"（用 **rather than** 说）

- 2026-08-11 ✅
- 2026-08-17 ✅ 复查
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（她原话："7-9 直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；Rather than taking … 她一直对

### 247 · stuck IN ＝ 被困在环境/容器里
类型 搭配 ｜ 旧号 B117a
状态 连对1 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-11（08-17 复查通过）** ｜ 退池 ｜ 题型 词组

**问题是什么**
**stuck IN ＝ 被困在环境／容器里**：stuck **in** a lift ／ get stuck **in** traffic。
同一格里的邻居（别串，三条一族）：stuck **ON** ＝ 卡在具体的点上（🎓#248）｜
stuck **WITH** ＝ 被迫接受甩不掉（🎓#73）—— 三个 stuck 各配一个介词，⛔ 别串。
判据一句话：困住她的是一个**空间／环境** ⇒ in。

**怎么发现的**
旧 B 表迁移（B117a，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅ ⇒ 毕业。
2026-08-17 ✅ 复查。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写完 stuck 先问一句 —— 困住她的是空间（in）、一道题（on），还是甩不掉的人（with）？

**题面**
**点名**："被困在电梯里"（用 stuck 说）

- 2026-08-11 ✅
- 2026-08-17 ✅ 复查
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 3 题整串，她原话："1-4 直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；stuck in（空间）她一直对 —— 这一族真掉过的是 on／with，由 🎓#248／🎓#73 去测

### 248 · stuck ON ＝ 卡在具体的点上
类型 搭配 ｜ 旧号 B117b
状态 连对2 连错0 上次2026-09-18 ｜ 回潮已断（08-20 回潮）｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
**stuck ON ＝ 卡在具体的点上**：`get **stuck on** the third question` ／ `the whole team was **stuck on** a problem`。
同一格里的邻居（别串，三条一族）：stuck **WITH** ＝ 被迫接受甩不掉（🎓#73）｜
stuck **IN** ＝ 被困在环境／容器里（🎓#247）。
判据一句话：卡住她的是**一道题／一个问题** ⇒ on。

**怎么发现的**
旧 B 表迁移（B117b，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-19 ✅ 自发（#30 那题里 `the whole team was stuck on`）；
2026-08-20 ❌ 复习 #30 句里 · `a problem that the whole team is stuck **with**`——在 on／with 之间选反 ⇒ **回潮**
（★ 一天之内从对变错：08-19 同一道题她写的就是 stuck on）。
2026-08-21 ✅ ／ 2026-08-23 ✅ `I get stuck on the third question.` ⇒ 连对 2，第二次毕业。
2026-09-05 复检第 5 组（打包）✅ `get stuck on the third question`。

**我错在哪**
她的：`a problem that the whole team is stuck **with**`（2026-08-20）　　正确：`… is stuck **on**`
找法：写完 stuck 先分一刀 —— 卡在一道题上（on）、困在一个空间里（in）、还是甩不掉一个人（with）？

**题面**
"做数学作业的时候，他在最后一道题上卡了半天。"（"卡"用 **stuck** 说）

- 2026-08-11 ✅
- 2026-08-17 ✅ 复查
- 2026-08-19 ✅（自发，#30 那题里 `the whole team was stuck on`）
- 2026-08-20 ❌ 复习#30 句里 · `a problem that the whole team is stuck **with**`——在 on/with 之间选反
  ⇒ 回潮，重新入池。**一天之内从对变错**（08-19 同一道题她写的是 stuck on）
- 2026-08-21 ✅ 复习（点名题面首测）· `I got stuck on the third question.`——介词选 **on**（08-20 那次选反成 with）
  ⇒ 回潮后第一次翻正，连对 0→1
- 2026-08-23 ✅ 付息日 a 段 · `I get stuck on the third question.`——介词 **on** 一字不差，连续第二次
  → **连对2，毕业**（回潮后走完两次）
  ⚪ `I **get** stuck`（该 got）——中文"卡住**了**"是完成的事件；属 #12 时态判断触发（形态类·不召回）
    ⇒ 中译英里只做记号，不记档位
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `get stuck on the third question`（卡在具体的点上用 on）
- 2026-09-18 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 stuck，介词 on 留给她（她掉过的是 on／with 选反）；换成数学作业场景
- 备注 三条一族，判据放在一起记：stuck **ON** ＝ 卡在具体的点上（a problem／question 3）｜
  stuck **WITH** ＝ 被迫接受甩不掉（🎓#73）｜ stuck **IN** ＝ 被困在环境/容器里（🎓#247）

### 249 · 原形＝过去式的一小撮动词（put／cut／hit／let／cost）
类型 语法 ｜ 旧号 B152a
状态 连对1 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-11（08-17 复查通过）** ｜ 退池 ｜ 题型 整句

**问题是什么**
**原形 ＝ 过去式的一小撮动词**：put ／ cut ／ hit ／ let ／ cost —— 过去时**不变形**。
同一格里的邻居（别串）：#93 是这条规则的**另一面**（不在这一小撮里的动词必须变形：sit→sat／sing→sang）——
2026-08-19 判重结论写明两条**不合并**、互相引用。
判据一句话：这个动词在不在这一小撮里？在 ⇒ 过去式原样不动。

**怎么发现的**
旧 B 表迁移（B152a，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅ ⇒ 毕业。
2026-08-17 ✅ 复查。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：写过去式之前先查这一小撮（put／cut／hit／let／cost）—— 在里面就别动它。

**题面**
"他昨晚把东西放桌上了。"（"放"用 **put** 说）

- 2026-08-11 ✅
- 2026-08-17 ✅ 复查
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（她原话："7-9 直接过"）
- 2026-09-29 📝 退池 · ④ 底子不明 ＋ 基础形式
  旧 B 表迁移、原话未存、历史零 ❌；put 的过去式她一直对（形态类、从没掉过）

### 250 · that far vs too far（有没有"刚才那句话"可指）
类型 词组 ｜ 旧号 B229
状态 连对0 连错0 上次2026-09-20 ｜ **🎓 已毕业 2026-08-17 · 她指定**（"这句毕业了，别问了"）｜ 题型 整句

**问题是什么**
**that far vs too far（有没有"刚才那句话"可指）**：
· **too far** ＝ 过分了（不指向谁的话）：`don't go **too far**.`
· **that far** ＝ 我倒不至于说到**那个份上**（指着对方刚说的那一句）：`I wouldn't go **that far**.`
同一格里的邻居（别串）：🎓#70 是 that far 那一半的整块（I wouldn't go that far, though.）；
🎓#131 管的是 far 的搭档永远是 go。
判据一句话：话里有没有"刚才那句"可指？有 ⇒ that far；没有 ⇒ too far。

**怎么发现的**
旧 B 表迁移（B229，2026-08-18）；2026-08-17 📝 **她指定毕业**（原话："这句毕业了，别问了"），触发原话未存。
2026-09-09 📝 状态行从旧账写法 `状态 —` 补成三个字段（连对／连错冻结在毕业日 ＝ 0/0，她指定毕业时从没数过连击）。
2026-09-09 复检第 4 组 ✅ `don't go too far.` ／ `I wouldn't go that far.`——两者分工对。

**我错在哪**
她的：本条历史里没有掉过（08-17 直接由她指定毕业），触发原话未存。
找法：说"别太过分"用 too far；要回应对方刚说的那句话才用 that far。

**题面**
"开玩笑可以，但别太过分。" ／ （朋友说"他就是个骗子"）"我倒不至于这么说。"（两句都用 **far** 说）

- 2026-08-17 📝 🎓·她指定
- 2026-09-09 📝 状态行从旧账写法 `状态 —` 补成三个字段（连对/连错冻结在毕业日 ＝ 0/0，因为她指定毕业时从没数过连击）
  —— 09-09 复检第一次真测到它，`append` 要写「上次」而旧写法没有这个字段 ⇒ 自查报错、整批回滚（§3.1③ 允许旧账，但一旦被测就得补齐）
- 2026-09-09 ✅ 复检 · 第 4 组 · `don't go too far.` ／ `I wouldn't go that far.` —— too far 与 that far 分工对
- 2026-09-20 ⚡ 自评免测 · 复检第 4 组（她答"直接过"）
- 2026-09-29 📝 题面整改（§6 换场景）
  两句都换新场景（开玩笑／朋友说"骗子"），照旧点名 far —— too／that 的分工留给她

### 251 · cost ＋ 钱／take ＋ 时间／spend ＋ 人做主语
类型 搭配 ｜ 旧号 B230
状态 连对2 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-17**（记录里明确判定毕业）｜ 题型 整句

**问题是什么**
**cost ＋ 钱 ／ take ＋ 时间 ／ spend ＋ 人做主语**：
`**it takes** two hours to cook a meal.`（时间 ⇒ take）｜ 钱 ⇒ cost ｜ 人当主语 ⇒ spend。
同一格里的邻居（别串）：⚠️ **cost 只配钱**这条边界还没固化（08-19 她在自由句里 takes／costs 两个都列了出来，
首选 takes 是对的 ⇒ 当时不记回潮，再出现一次按回潮处理）。
判据一句话：先看花的是**钱**还是**时间**、主语是**人**还是 it —— 三条路各走各的。

**怎么发现的**
旧 B 表迁移（B230，2026-08-18）；最早记录 2026-08-15 ❌，触发原话未存。
2026-08-16 ✅ ／ 2026-08-17 ✅ ⇒ 毕业。
2026-09-05 复检第 1 组 ✅ `it takes two hours to cook a meal.`——take ＋ 时间。

**我错在哪**
她的：2026-08-15 记过一次 ❌（触发原话未存）；08-19 自由句里写过 `it just takes/costs ten minutes`（两个都列，⛔ 不记回潮）。
找法：说"要花多少"先分一刀 —— 时间用 take、钱用 cost、人当主语用 spend。

**题面**
"从我家开车到机场要一个多小时。"
　　★ 零提示：It takes …／The drive is … 都算对；她掉过的是时间配 cost

- 2026-08-15 ❌
- 2026-08-16 ✅
- 2026-08-17 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `it takes two hours to cook a meal.` —— take ＋ 时间
- 2026-09-19 📝 题面整改：补（⛔ 不许用 need）· 复检组发题前审核（§6.5 第 7 项）
  `I need two hours to cook a meal.` 合法，绕开 take ＋ 时间 ⇒ 补排除项；spend 以人做主语在规则内
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-19 ✅ 自发命中 · 付息日 d 段重答 R11（P3 · 自由产出）· `my family spends the whole day cooking`——spend 以人做主语
- 2026-09-19 ✅ 自发命中 · 付息日 d 段重答 R12（P3 · 自由产出）· `People spend hours in front of screens every day now.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）
  去掉"⛔ need"，改零提示（It takes …／The drive is … 都算对），逼的是时间配 cost 这条她掉过的路；换成开车去机场场景
- 备注 2026-08-19 她在自由句里写 `it just takes/costs ten minutes`（两个都列出来）——
  首选 takes 是对的，不记回潮；但 **cost 只配钱** 这条边界还没固化，再出现一次就按回潮处理

### 254 · 主语位置的动词必须变成 -ing（Putting things back makes…）
类型 语法 ｜ 新建 2026-08-19
状态 连对2 连错0 上次2026-08-23 ｜ **形态类·不召回**（2026-08-25 她定）｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
**主语位置的动词必须变成 -ing**：`**Putting** things back makes them much easier to find` ／
`**Going** to bed early is good for your health.`
判据：英语主语只能是"名词性的东西"，光秃秃的动词原形站不住 ⇒ **句子开头是个动作 → 先给它加 -ing**
（同一天她的 `Commuting every day is really a hassle` 是对的 —— 同一条规则两题一对一错 ⇒ 不是不会，是产出时检查没跑）。
★ 本条是**形态类**（2026-08-25 她定，原话：**"studying 我会，不用新建，和单复数一样，这种你点出来就行"**）
　⇒ 在哪儿掉都只记 ⚪，⛔ 不进召回队列。

**怎么发现的**
2026-08-19 新建 · 首犯 · 复习 #50 句里 · 触发原话 `put things back makes them much easier to find`。
2026-08-21 ✅ ／ 2026-08-23 ✅ `going to bed early is good for your health.` ⇒ 连对 2，毕业。
2026-08-25 ⚪ 自由产出（新题 bank:987 P3）· `On top of that, **study something** makes your mind stay active.`
—— 教练原判 ❌ ＋ 回潮，**当天她驳回**（同篇 S2 `Learning helps…`、S6 `watching short videos` 两处都对 ⇒ 不是不会）
⇒ 改记 ⚪、🎓 还原、状态行加 `形态类·不召回`。
2026-08-26 ⚪ 观察行 · `learning something new keeps your mind active.`——同一个位置隔一天做对
（⚠️ 但那是低压中译英，⛔ 不能据此说漏洞补上了：形态类的失败只发生在高压那一侧）。

**我错在哪**
她的：`put things back makes …`（08-19 首犯）／ `study something makes your mind stay active`（08-25 自由产出）
正确：`**Putting** things back makes …` ／ `**Studying** something makes …`
检查触发：**一句话开头是个动作 ⇒ 先给它加 -ing**（说完一段回扫每个句首）。

**题面**
不出中译英题（题型 产出验 ＋ 形态类·不召回）；挂自由产出抓：句首那个动作还光着（没加 -ing）。
★ 原题面（留档，⛔ 不再发题）："早点睡对身体好。"（句子开头是个动作）

- 2026-08-19 ❌ 首犯 · 复习#50 句里 · `put things back makes them much easier to find`
- 2026-08-21 ✅ 复习 · `going to bed early is good for health.`——主语位 -ing 一字不差，连错清零
- 2026-08-23 ✅ 付息日 a 段 · `going to bed early is good for your health.`——主语位 -ing 一字不差
  → **连对2，毕业** ｜同句 `good for **your** health` 归 #265 记 ✅
  ⚠️ 同句 `good for health` 搭配不成立 → **新建 #265**（good for you／your health），不算本条头上
- 2026-08-25 ⚪ **只做记号**（不记 ❌／不掉毕业）· 自由产出（新题 bank:987 P3 Is it necessary to
  keep learning after graduating from school?）· `On top of that, **study something** makes your
  mind stay active.` → **studying something** makes…
  ★★★ **教练原判 ❌ ＋ 回潮，当天她驳回**。她的原话：
     **"studying 我会，不用新建，和单复数一样，这种你点出来就行"**
     ⇒ 按 §3.4 自我分诊，本条 ＝ **形态类**（她会，缺口在产出时检查不运行）⇒
       状态行加 `形态类·不召回`，本次改记 ⚪，🎓 毕业状态还原（08-23 那次毕业不动）
  ★ 她是对的，同篇就有证据：S2 `**Learning** helps you keep up with the times.` 主语位 -ing 用对，
    S6 `watching short videos` 也对 —— **一篇里三处同结构，两处对** ⇒ 不是不会
  ⛔ 教练犯规：本条 08-19 的备注**早就写着**"同一条规则两题一对一错 ⇒ 不是不会，是产出时检查没跑"，
    今天判 ❌ 时把自己写的这句读成了"所以照记 ❌"，没跑 §3.4 的自我分诊。留痕见 sessions/2026-08-25.md
- 2026-08-26 ⚪ **观察行（不改状态、不算档位）**· 复习第1组 #297 句里 ·
  `**learning** something new keeps your mind active.`——主语位 -ing 做对了，
  **正是 08-25 掉的那个点**（`study something makes…`），同一个位置隔一天做对
  ⚠️ **不能据此说漏洞补上了**：08-25 那次是**自由产出（cold）**，本次是**中译英单句（低压）**，
  条件不同 —— 形态类的失败本来就只发生在高压那一侧（§3.4 判据）⇒ 真正的验证点在自由产出里
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）

### 255 · vital（至关重要）≠ virtual（虚拟的）
类型 词汇 ｜ 新建 2026-08-19
状态 连对1 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个也毕业了"）｜ 退池 ｜ 题型 词组

**问题是什么**
**vital（至关重要）≠ virtual（虚拟的）**。
判据：vital ＝ crucial／essential（至关重要）｜ virtual ＝ 虚拟的（virtual reality／a virtual meeting）。
同一格里的邻居（别串）：#83 管的是**形态和介词**（形容词不加复数；crucial TO），本条管**选哪个词** ——
规则不同、题面不撞车（2026-08-19 判重结论）。
判据一句话：要说"至关重要"时看清词形 —— vi-**tal**，⛔ 不是 virtual。

**怎么发现的**
2026-08-19 新建 · 首犯 · 复习 #83／#89 两句里 · 触发原话 `start-ups are **virtual** to the economy`
—— **两句都写 virtual** ⇒ 不是打字滑，是存错了形。
判重（当天新建复核）：grep vital／virtual／crucial → 命中 #83（形容词不加复数；crucial TO）——
#83 管形态和介词、本条管选词，规则不同 ⇒ 保留；#83 题面不含"关键"以外的干扰，不撞车。
2026-08-20 ✅ 复习（点名"vi- 开头"后首测）· `sleep is vital to health` ⇒ 她当场指定毕业（"这个也毕业了"）。
08-31 ／ 09-01 ／ 09-03 三次自发命中留痕；2026-09-05 复检 ✅；2026-09-07 ⚡ 自评免测。

**我错在哪**
她的：`start-ups are **virtual** to the economy`（2026-08-19 首犯，同日两句都这么写）
正确：`start-ups are **vital** to the economy`
找法：写"至关重要"时看清词形 —— vital；virtual 是"虚拟的"。

**题面**
**点名**："至关重要"（用 vi- 开头的那个形容词说）

- 2026-08-19 ❌ 首犯 · 复习#83／#89 两句里 · `start-ups are **virtual** to the economy`
  ⇒ 两句都写 virtual ⇒ 不是打字滑，是存错了形
- 2026-08-20 ✅ 复习（点名"vi- 开头"后首测）· `sleep is vital to health`——词形词义都对
- 2026-08-31 📝 付息日 d 段 · 重答 R9 · 自发命中留痕（🎓 状态行冻结）
  `Start-ups are **vital** to a diverse economy`
  vital 不是 virtual，介词也是 to ⇒ 考位命中。
  ⚠️ **证据强度如实标注**：这句是**同日 a 段第 2 组（#89 的题面）刚测过的原句复用**，
    不是独立的自发命中。★ 仍照记（§3.3「每一次各记一行、各算一次」），只是在此写明它的成色。
  ★ 纵向：08-19 她在这一处写的是 `start-ups are **virtual** to the economy`（本条首犯）。
- 2026-09-01 📝 复习第1组 [8] 句里 · 自发命中留痕（🎓 冻结，机器契约⑦：只留痕、不推进数字）
  `Financial support for governments is **vital** to economic growth.`
  ★ 连续第二天自发用对（08-31 R9 `Start-ups are **vital** to a diverse economy`）。
  ★ 状态行一个字不动。
- 2026-09-03 📝 复习第1组 [5]（#314 那题）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）
  `Government financial support **is vital to** economic growth`
  中文「关键」可选 crucial／key／essential／important，题面只点了 econom-，
  **vital 是她自己调的**，且没写成 virtual、介词也是 to ⇒ 本条两个考点位（选词 ＋ to）全中。
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· vital（⛔ 没写成 virtual）
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-09-29 📝 退池 · ③ 题面收不拢
  不点名她可以用 crucial／essential 合法绕开，点名 vital 就是给答案，提示首字母又是猜谜 ⇒ 单点题测不出；⚠️ 自由产出里再冒出 virtual（当"至关重要"用）⇒ 撤销退池、记 ❌

### 256 · even if ＝ 还没发生的假设（"就算…"）
类型 语法 ｜ 新建 2026-08-19（从 #165 拆出）
状态 连对2 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 整句

**问题是什么**
**even if ＝ 还没发生的假设（"就算…"）**：`Even **if** it rains, I'll go`（even if ＋ 一般现在时 ＋ 主句 will）。
一句话判据：**已经这样了 → even though ｜ 万一这样 → even if**。
同一格里的邻居（别串）：虚拟语气**不用上** —— 只在"跟事实相反"时才上
（Even if it were sunny, I'd still stay in ＝ 其实是阴天）；她两种都会，只是选错场合。
★ 本条 2026-08-19 从 #165 拆出：#165 只留 even though（已毕业），两条题面互斥。

**怎么发现的**
2026-08-19 新建（从 #165 拆出）· 首犯 · 触发原话 `Even though it is rainy, I will go`——把假设写成了事实。
判重（当天新建复核）：grep even → 命中 #165（even／even though）—— 本条正是从它拆出来的，两条题面互斥、不重复。
2026-08-20 ✅ ／ 2026-08-21 ✅ `Even if it rains, I'll go` ⇒ 连对 2，毕业。
2026-09-05 复检第 4 组 ✅ `Even **if** it rains, I will go.`

**我错在哪**
她的：`Even though it is rainy, I will go`（2026-08-19 首犯）　　正确：`Even **if** it rains, I will go`
找法：先问这件事发生没有 —— 已经这样了用 even though，万一这样用 even if。

**题面**
"就算明天下大雨，比赛也照常进行。"（"就算"用 **even** 说）

- 2026-08-19 ❌ 首犯 · `Even though it is rainy, I will go`——把假设写成了事实
- 2026-08-20 ✅ 复习 · `even if it rains, I will go`——even if ＋ 一般现在时，选对了场合
- 2026-08-21 ✅ 复习（点名题面首测）· `Even if it rains, I'll go`——even if ＋ 一般现在时 ＋ 主句 will
  → **连对2，毕业**（08-19 那次写成 Even though ＝ 把假设写成事实，这次分清了）
- 2026-09-05 ✅ 复检组 · 第 4 组 · `Even **if** it rains, I will go.`（还没发生的假设）
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"even ＋ 一个词"形态描述，只点名 even —— if／though 的选择留给她（她掉过的就是把假设写成 even though）；换成比赛照常进行场景
- 备注 她当天问"要用虚拟语气么" → **不用**：even if ＋ 一般现在时（Even if it rains, I'll go）；
  虚拟只在"跟事实相反"时上（Even if it were sunny, I'd still stay in ＝ 其实是阴天）。
  同日第 4 题她的 `if it were a bit more expensive` 正是正确的虚拟用法 ⇒ **两种都会，只是选错场合**

### 257 · 以身作则 ＝ lead by example／practise what you preach
类型 词组 ｜ 新建 2026-08-19
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **回潮 2026-09-05**（08-21 毕业 → 09-05 复检写成 `lead by yourself`，by 后面塞了人，撤销毕业、连对清零） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
**问题是什么**
**以身作则 ＝ lead by example ／ practise what you preach**。整块记：lead by **example**（example 单数，⛔ 不带 the／your／a）。
判据：这句话是**说给谁听的**？对小孩 → behave yourself ／ 对大人（要求他做榜样）→ lead by example。
同一格里的邻居（别串）：**by yourself ＝ 独自、没人帮**，意思完全跑偏（09-05 她就是掉在这里）。
判据一句话：by 后面填的是 **example**，⛔ 不是人。

**怎么发现的**
2026-08-19 新建 · 首犯 · 自由产出（新题 bank:489）· 触发原话 `Stop just talking and behave yourself`
—— behave yourself ＝ **对小孩说的"你规矩点"**，用在家长身上就变成训他们了。
判重（当天新建复核）：grep behave／example／preach → 命中 #31（explain yourself to anyone）——
#31 管"反身代词不能丢"、本条管"选哪个块"，规则不同 ⇒ 保留；两条题面互不撞车。
2026-08-20 ✅ ／ 2026-08-21 ✅ `parents should lead by exmaple.`（拼写不算错）⇒ 连对 2，毕业。
2026-09-05 ❌ 复检第 4 组 · `lead by youself` ⇒ **回潮**。
2026-09-07 ✅ `lead by example`；2026-09-09 ⚡ 自评免测 ⇒ 第二次毕业。

**我错在哪**
她的：`Stop just talking and behave yourself`（08-19 首犯）／ `lead by youself`（09-05 回潮）
正确：`parents should **lead by example**.`
找法：by 后面填的是"做出来的样子"（example），⛔ 不是人；说之前先想这句是讲给谁听的。

**题面**
"当经理的得以身作则，不能光让员工加班、自己早早走人。"（"以身作则"用 **lead** 说）

- 2026-08-19 ❌ 首犯 · 自由产出（新题 bank:489）· `Stop just talking and behave yourself`
  —— behave yourself ＝ **对小孩说的"你规矩点"**，用在家长身上就变成训他们了
- 2026-08-20 ✅ 复习（点名"用 lead 说"后首测）· `it's no use just talking. parents should lead by example.`
  ——目标块一字不差 ｜同句 `It's no use just talking` 自发命中 #25
- 2026-08-21 ✅ 复习 · `it's no use just talking. parents should lead by exmaple.`——lead by example 一字不差
  → **连对2，毕业**（`exmaple` 按 §2.1 拼写不算）
- 2026-09-05 ❌ 复检组 · 第 4 组 · **回潮**
  `lead by youself` → lead by **example**
  ❌ by example ＝ 用做出来的样子带头；by yourself ＝ 独自、没人帮 —— 意思完全跑偏。
  ★ 整块记：lead by example（example 单数，⛔ 不带 the／your／a）；同义块 practise what you preach。
  ｜ youself 是拼写（§2.1 不算错）
- 2026-09-07 ✅ 复习 · 在池第 1 组 · `lead by example`
- 2026-09-09 ⚡ 自评免测 · 在池第 2 组（她原话："前 7 题直接过"）
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 lead，by example 留给她（她掉过的是 lead by yourself）；换成经理场景
- 备注 来源有意思：这个块是同日第 9 组讲 explain yourself 时顺带列的同族（behave/enjoy/help yourself），
  她当场抓来用了 ⇒ **迁移意识对，但块的使用对象没跟着记** —— 以后给同族清单时要连"对谁用"一起给

### 259 · 完成时：have/has/had 之后一律用【过去分词】（I've never BEEN able to）
类型 语法 ｜ 新建 2026-08-20
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
完成时：**have／has／had 之后一律用【过去分词】**（`I've never **been** able to`）。
一句话判据：**看助动词是哪一类** —— 情态（can／will／should）后面不带任何标记；
完成时的 have 后面必须带 **-ed／-en** 那个标记。
同一格里的邻居（别串）：高频不规则 be→**been** ｜ go→**gone** ｜ do→**done** ｜ see→**seen** ｜ take→**taken** ｜ get→**got(ten)**
★ 与 **#147** 的分工（互斥，⛔ 不许同组出题，见下方 ⚠️ 行）：#147 ＝ did／will／can／should／must 之后 → **原形**（couldn't **find**）；
　本条 ＝ have／has／had 之后 → **过去分词** ⇒ 同一个决策点（"助动词后面动词变什么形"）的两个方向。

**怎么发现的**
2026-08-20 新建 · 复习 #130 句里 · 她写 `I've never **be** able to get up early`（→ **been**）。
判重：建号当天未留判重记录（旧口径建号，B0 逐条判重是 2026-09-12 才立的规矩）；
事后由下方 ⚠️ 行确认与 **#147** 是同一决策点的两个方向 ⇒ 两条互斥、不合并、不许同组出题。

**我错在哪**
她的：`I've never **be** able to get up early`　　正确：`I've never **been** able to get up early.`
找法：写完 have／has／had，回头看下一个动词 —— **-ed／-en 那个标记带上了吗？**

**题面**
"我从来没能早起过。"（用现在完成时说）

- 2026-08-20 新建 · 复习#130 句里 · `I've never **be** able to get up early` → **been**
- 2026-08-21 ✅ 复习#130 句里 · `I've never been able to get up early.`——been 带对了，连错清零
- 2026-08-23 ✅ 付息日 a 段 · `I've never been able to get up early.`——been 一字不差，连续第二次
  → **连对2，毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `I've never been able to get up early.` —— have ＋ **been**（过去分词）
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- ⚠️ **必须和 #147 一起读，两条互斥**（同 #18／#134 那一对的教训）：
  **#147** ＝ did／will／can／should／must 之后 → **原形**（couldn't **find**）
  **本条** ＝ have／has／had 之后 → **过去分词**（I've **been**／he's **gone**／I've **done**）
  ⇒ 她两次掉的都在"助动词后面动词变什么形"这个决策点上，只是方向不同 ⇒ **不许同组出题**
- 备注 高频不规则：be→been ｜ go→gone ｜ do→done ｜ see→seen ｜ take→taken ｜ get→got(ten)

### 260 · 中文的"这事／这个东西"→ it／this／about it（不要 the thing）
类型 词汇 ｜ 新建 2026-08-20
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
中文的"这事／这个东西"→ **it／this／about it**（⛔ 不要 **the thing**）。
判据：中文的"这事/那个东西"是**空指代**，英语用代词 it／this／that 顶上去；
the thing 在英语里指"那个具体物件"，拿来指抽象的事会很怪。
同一格里的邻居（别串 —— 常配的介词）：find out **about** it ／ know **about** it ／ hear **about** it ／ talk **about** it
★ 与 **#150**（限定词与数一致，形态类）的分工：#150 掉的是【数】，本条掉的是【选词】（该用代词却搬了个名词）⇒ 两条并存。
★ 与 **#157**（直译搭配）的分工：#157 管动词/形容词搭配，本条管空泛名词 ⇒ 目标形式不同。

**怎么发现的**
2026-08-20 新建 · **同一天两次** · 复习 #75 句里 `no one knows **the thing**, other than him`
＋ 复习 #146 句里 `I found out **the thing** from the news`。
判重（当天新建复核）：grep "the thing" 全库（含已毕业）→ 命中 #150（限定词与数一致，
08-19 她把"这些东西"写成 the thing）。**区别**：#150 掉的是【数】（形态类），
本条掉的是【选词】（该用代词却搬了个名词）⇒ 两条并存。
另比 #157（直译搭配）：#157 管动词/形容词搭配，本条管空泛名词 ⇒ 目标形式不同，保留。

**我错在哪**
她的：`no one knows **the thing**, other than him` ／ `I found out **the thing** from the news`
正确：`no one knows **about it**` ／ `I found out **about it** from the news`
找法：中文说"这事／这个东西"时问一句 —— 指的是一个**看得见的物件**吗？不是 ⇒ 用 it／this，别搬 the thing。

**题面**
"你是从哪儿听说这事的？"
　　★ 零提示：about it／about this 都算对；她掉过的是把"这事"搬成 the thing

- 2026-08-20 新建 · 同一天两次 · 复习#75 句里 `no one knows **the thing**, other than him`
  ＋ 复习#146 句里 `I found out **the thing** from the news`
- 2026-08-21 ✅ 复习（新建后首测）· `Besides him, no one knows about it.`——`knows **about it**` 一字不差
- 2026-08-23 ✅ 付息日 a 段 · `no one knows about it except him.`——`knows **about it**` 一字不差，
  连续第二次；语序比 08-21 的前置式更自然 → **连对2，毕业**
  ★ 同句 `except him` 用对了（#266 三成员之一）⇒ 按 §3.2c **合并条要整组覆盖才计档位**，
    只中一个成员**不给 #266 记 ✅**，只做正面记号
  ⚠️ `Besides him` 判 ✅ 不扣：besides 在**否定句里**确实可当 except 用（No one besides me knows.）；
    但放句首更容易被读成"此外／而且"（加法义）⇒ 更稳的是 **Apart from him ／ Other than him**
    **不建条目**（§3.2b 她 08-21 定的第三档）：她的选择合法，说不出"不会的是哪个词组"⇒ 只给更稳版本
  ⇒ 2026-08-21 后续：她说 **"Apart from him 可以建一个，非常不熟练"** ⇒ **新建 #266**（题面另起一句，与本条不撞车）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `know about it` —— ⛔ 没用 the thing
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）· 题型 词组 → 整句
  去掉"不许用 the thing"，改零提示整句（about it／about this 都算对），逼的是她掉过两次的 the thing
- 备注 常配的介词：find out **about** it ／ know **about** it ／ hear **about** it ／ talk **about** it

### 261 · 这一小撮抽象名词不可数：feedback／advice／information／knowledge／research／progress（action 已于 09-11 拆出 → #335）
类型 语法 ｜ **合并条·出题必须整组出**（§3.2c，她 2026-08-23 定：只出一句 ＝ 违规）｜ 新建 2026-08-20
状态 连对2 连错0 上次2026-09-29 ｜ **🎓 已毕业 2026-09-13** ｜ **合并条·出题多句覆盖** ｜ 题型 整句 ｜ **回潮 2026-09-07**（08-23 她指定毕业 → 09-07 复检七个成员六个对、`take actions` 又加了 -s，与 08-20 首犯同一个成员，撤销毕业、连对清零。★ action 已于 2026-09-11 付息日 c 段按 §3.2c③ 单拆成 #335，本条剩六个成员照常走连击）

**问题是什么**
**这一小撮抽象名词不可数**：feedback ／ advice ／ information ／ knowledge ／ research ／ progress
⇒ 既不加 **-s**，也不带 **a／an**；真要计数得借量词（a piece of feedback）。
量词只能用 a lot of ／ much ／ some ／ a bit of ／ plenty of —— ⛔ 不能用 **many**
（08-23 成员 advice 就是栽在这里：`he gave me many advice`，量词那一格已摘出 → #270）。
同一格里的邻居（别串）：take **action** 是固定块、这个意义上不可数；
同族的 take **steps**／take **measures** 才有复数（steps／measures 本身可数）——
action 这个成员已于 2026-09-11 按 §3.2c③ 单拆成 **#335**，不在本条了。
判据一句话：这个抽象名词在不在这张表里？在 ⇒ 去掉 -s、去掉 a。
★ 与相邻条目的分工（2026-08-23 c 段定，不并、只交叉引用）：本条只管这一小撮抽象名词这**一条规则**；
　具体某个词的可数性各留各条 —— #272（litter）· 🎓#48（work）· #224（discrimination）· #270（advice 的量词）。
★ 与形态类 #10（主谓一致）／#150（限定词与数一致）不同层：那两条管**形态检查是否运行**，本条管**这个词本身可不可数**。

**怎么发现的**
2026-08-20 新建 · 复习 #85 句里 · 触发原话 `they are more willing to take actions`（→ take action）；
同一天自由产出（新题 bank:187）又写 `can get good feedbacks`（→ feedback）——
⚠️ 同一篇第 1 句她写的是 `the feedback`（对）⇒ 不是不知道，是产出时没检查。
同一天两处规则完全相同 ＝「这类抽象名词不加 -s」⇒ 当天由「take action 一个块」**改写成规则条**，
按【判重三档·同一条规则→同一条】合成一条，避免每碰到一个不可数名词就开一个新号。
判重（当天新建复核）：grep "不可数"／"take action" 全库（含已毕业）→ 命中 #25（litter 不可数）·
🎓#48（work 不可数）· #224（discrimination 不可数）—— 三条都是**具体某个词**的可数性，
按 §3.2「词汇/搭配按具体的词一条一号」⇒ action 另立一条，不并。
另比对形态类 #10（主谓一致）／#150（限定词与数一致）：那两条管**形态检查是否运行**，
本条管**这个词本身可不可数** ⇒ 不同层，保留新建。

**我错在哪**
她的：`take actions` ／ `can get good feedbacks` ／ `he gave me many advice.` ／ `get a positive feedback`
正确：take action ／ get good feedback ／ he gave me **a lot of** advice ／ **get positive feedback**
找法：写完一个抽象名词，先问它在不在这张表里，在表里就把 -s 去掉 —— 顺手再看一眼前面有没有多一个 a。

**题面**
★ 6 句，六个不可数名词各一句（考点是 -s／a 挂不挂 ＝ 靠句子现形 ⇒ 整句题）
　① "这次演讲我收到了很多正面反馈。"（"反馈"用 **feedback** 说）
　② "我姐给了我几条很实用的建议。"（"建议"用 **advice** 说）
　③ "官网上能查到更多信息。"（"信息"用 **information** 说）
　④ "要做好这份工作，只有理论知识可不够。"（"知识"用 **knowledge** 说）
　⑤ "医生对这种病了解得很少，相关的研究也不多。"（"研究"用 **research** 说）
　⑥ "她这学期英语进步很大。"（"进步"用 **progress** 说）
　　★ 目标形式（教练看，⛔ 不进发题稿）：① a lot of positive feedback ② some useful advice／a few pieces of advice ③ more information ④ theoretical knowledge ⑤ not much research ⑥ has made a lot of progress

**成员出题账**
① feedback ｜ 08-20 ❌ · 08-21 ✅ · 08-23 ✅ · 09-05 ✅ · 09-07 ✅ · 09-10 ❌（加了 a）· 09-13 ✅ · 09-29 ✅
② advice ｜ 08-23 ❌（`many advice`，量词那一格摘出 → #270）· 09-05 ✅ · 09-07 ✅ · 09-10 ✅ · 09-13 ✅ · 09-29 ✅
③ information ｜ 08-23 ✅ · 09-05 ✅ · 09-07 ✅ · 09-10 ✅ · 09-13 ✅ · 09-29 ✅
④ knowledge ｜ 08-23 ✅ · 09-05 ✅ · 09-07 ✅ · 09-10 ✅ · 09-13 ✅（第一轮漏答，补答后判）· 09-29 ✅
⑤ research ｜ 08-23 ✅ · 09-05 ✅ · 09-07 ✅ · 09-10 ✅ · 09-13 ✅ · 09-29 ✅
⑥ progress ｜ 08-23 ✅ · 09-05 ✅ · 09-07 ✅ · 09-10 ✅ · 09-13 ✅ · 09-29 ✅
★ 09-09 与 09-11 两次是她 ⚡ 自评免测（整组过），未按成员记录；09-05 那次整组判 ◎（题面①坏了），六个成员都答对。

- 2026-08-20 新建 · 复习#85 句里 · `they are more willing to take actions` → take action
- 2026-08-20 ❌ **自由产出**（新题 bank:187）· `can get good feedbacks` → feedback
  ⚠️ 同一篇第 1 句她写的是 `the feedback`（对）⇒ **不是不知道，是产出时没检查**
- 2026-08-21 ✅ 复习（点名题面首测）· `he gets positive feedback in a short time.`——feedback 没加 -s，连错 2 清零
- 2026-08-23 ✅ 付息日 a 段 · **合并条 7 句整组首测，6/7 对**（§3.2c）：
  ① `with less risk, people are more willing to take action.` ✅ ② `he can get positive feedback quickly.` ✅
  ③ `he gave me **many** advice.` ❌ ④ `I need more information.` ✅ ⑤ `Just having knowledge isn't enough.` ✅
  ⑥ `there isn't much research on this yet.` ✅ ⑦ `he's made huge progress this semester.` ✅
  ⇒ **她当场指定毕业**（"这个不可数条目毕业，太简单了"）
  ★★ ③ 暴露出本条**判据缺了一半**：原来只写"不加 -s"，她那句 -s 确实没加，
     但**量词用了 many** —— 不可数名词的量词只能是 a lot of／much／some／a bit of／plenty of
  ⇒ 按她 08-23 定的 §3.2c ③【顽固成员单独摘出来新建条目，老的毕业】：
     **advice 摘出成 #270**，本条（其余六个成员）照她指定毕业
  ★ ⑥ `there isn't much research` 顺带命中 #269 的成员之一 ⇒ 合并条要整组覆盖才计档位，只做正面记号
  ⚠️ 同句 `in a short time` 判 ⚠️ 不建条目（配习惯性的 gets 略别扭，quickly／soon 更顺）；
  `in **a** short time` 冠词带对（08-20 写的是 in short time）⇒ 属 #89 形态类·不召回，只记号不记档位
- 2026-08-23 📝 c 段 **08-20 待办 #1 的结论：不并，改成交叉引用**
  原待办写"把 #25 litter／🎓#48 work／#224 discrimination 里的『不可数』那一面并进本条"。
  今天**不执行**，理由两条：
  ① 本条**今天已毕业**（她指定）—— 往一条已毕业的条目里塞新成员，等于把它悄悄复活，
     而那些成员根本没被本条的题面测过 ⇒ 制造假 🎓
  ② §3.2 写着"词汇/搭配按**具体的词**一条一号"：litter／work／discrimination 各自还带着别的考点
     （litter 有动词用法 · work 要对比 my job · discrimination 要管 AGAINST 这个介词）⇒ 本来就不该并
  ⇒ 改成**交叉引用**：本条只管这七个抽象名词；具体词的可数性各留在各条
    #272（litter）· 🎓#48（work）· #224（discrimination）· #270（advice 的量词，今天从本条摘出）
- 2026-09-05 ◎ 复检组 · 第 5 组 · **题面①映射断裂，本次作废**（⛔ 不动连击）
  她的产出：① 忘了 ② get positive feedback ③ a lot of advice ④ more information
  ⑤ knowledge alone isn't enough ⑥ research in this field isn't enough ⑦ make huge progress
  ★ 为什么是教练的锅（**她当场点出来**："take action 是更愿意干的意思？？"）：
    ① 的原题面是整句「风险小了，大家就更愿意干。」→ take action；
    今天 c 段粒度整改把它砍成裸块「更愿意干」—— **光看这四个字想不到 take action**
    ⇒ 映射断裂 ⇒ 这一句任何人都答不出来 ⇒ ◎，⛔ 不记 ❌、⛔ 不回潮。
  ★ 其余六个成员**全部答对**（六个不可数名词一个 -s 都没加）⇒ 条目实际状态是好的，坏的只有题面。
  ★ ⛔ **撤回"把 take action 单拆出来"的决定** —— §3.2c③ 单拆的前提是那次测试有效，这次无效。
  ⇒ 题面①已改回整句，次日再测。
- 2026-09-07 ❌ 复检 · 第 5 组（加练）· 七个成员六个对，**action 又加了 -s**：`take actions`
  —— 08-20 首犯就是 take actions，今天同一个成员再掉 ⇒ 🎓 回潮
  最小改 `take action`
  ★ §3.2c③ 待办：action 是本条顽固成员（08-20 ❌ · 09-07 ❌，其余六个从未掉过）⇒
    下个付息日单拆成新条目，老条目（剩六个成员）照常走连击。
    09-05 曾提过一次拆号，但依据是判 ◎ 的那次（题面缩坏）⇒ 当时撤回；今天是题面完好下的真掉，依据成立。
- 2026-09-09 ⚡ 自评免测 · 在池第 2 组（她原话："前 7 题直接过"）
- 2026-09-10 ❌ 复习 · 在池第 1 组 · 合并条七个成员，**成员 ② feedback 掉了**
  `get a positive feedback` → **get positive feedback**
  ❌ feedback 不可数 ⇒ 既不加 a／an 也不加 -s；要计数得借量词 a piece of feedback。
  ★ 其余六个成员全部命中：take action ✅ · some advice ✅ · more information ✅ ·
    knowledge alone is not enough ✅ · There isn't much research ✅ · make a lot of progress ✅
  ★ 08-20 建号那天她掉的是 `take actions` 与 `good feedbacks`（都是加 -s）；这次 -s 没再加，
    改成在 feedback 前面加了 a ⇒ 同一条规则的另一侧（不可数名词也不带不定冠词）
  ⚠️ 本条状态行带「顽固」：连对1 → 归零，连错1
- 2026-09-11 📝 题面整改：① 句补排除项 `⛔ 不许用 steps／measures` · a 段第 1 组发题前审核（§6.5 第 7 项）
  `take steps`／`take measures` ＝ **take ＋ 一个名词**、完全符合题面①，
  但那两个名词本身可数（见下方备注），答出来一次都测不到 action 不可数这个考点 ⇒ 白测。
  ⛔ 仍未点名 action（考点本身，§6② 红线）
- 2026-09-11 ⚡ 自评免测 · 付息日 a 段第 1 组（她原话："3. 直接过"）
- 2026-09-11 📝 付息日 c 段 · **拆号**：顽固成员 action 单拆成 #335（§3.2c③），本条剩六个成员照常走连击
  依据（一条一条数的）：七个成员里只有 action 掉过两次（08-20 首犯 · 09-07 复检，两次题面完好）；
  09-05 那次是题面缩坏判 ◎ 不算；其余六个从未掉过（09-10 掉的 feedback 是 a 不是 -s，也只一次）。
  题面从 7 句改成 6 句（原 ① 整句搬去 #335，②–⑦ 重编成 ①–⑥）；标题去掉 action；状态行补「题型 整句」。
  ⛔ 本条连对／连错不动（拆出去的子条从 0 起算、不继承，§3.1）
- 2026-09-13 ✅ 学习日 在池第 1 组 · 六个成员全出全对 · `get position feedback. some advice. more information. Not much research. a lot of progress.` ＋ 补答 ④ `knowledge alone is not enough`
  ① positive feedback ✅（无 a、无 -s；position 是拼写不算）② some advice ✅ ③ more information ✅ ④ knowledge alone ✅ ⑤ not much research ✅ ⑥ a lot of progress ✅
  ★ 第一轮她只答了五句、④ 漏了 ⇒ 没按 5/6 记 ✅，请她补答之后才落判定（合并条成员没测全不许毕业）
  ⇒ **连对 2，毕业**（09-07 回潮 → 09-11 ⚡ → 今天六成员齐）
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-21 ⚪ 留痕 · 新题 bank:1005（P3）[S2] · `folk musics` → `folk music`
  —— music 不可数，永远不加 -s，与本条"这一小撮抽象名词不可数"同一条规则。§3.4 执行自查：**同一句里她自己写对了 pop music**（隔八个词）⇒ 是产出时检查没跑，不是不会 ⇒ 只记 ⚪、⛔ 不判回潮、⛔ 不把 music 加进成员出题账（加了就是让她重练已经会的）
- 2026-09-29 ✅ 复检第 2 组 · 六成员全出 · `get positive feedback. some advice. more information. knowledge alone. not much research. make great progress.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句（类型 语法 ⛔ 不许标词组）
  考点是 -s／a 挂不挂 ＝ 靠句子现形；六个成员各写一句新场景（避开 09-07 发过的"光有知识是不够的／这方面的研究还不多"），只点名那个名词
- 备注 中文"更愿意干"口语不走"采取行动"：**more willing to give it a go／to go for it／to have a crack at it**
- ★ **2026-08-31 c 段结案：本条下面那个"付息日待办"已被 08-23 裁掉，属陈账。**
  结论见本条上方 08-23 那行：**不并，改成交叉引用**（理由两条：往已毕业条目塞成员 ＝ 制造假 🎓；
  §3.2「词汇/搭配按具体的词一条一号」）。⛔ 原待办文字一字不删，数字未动。
- ⚠️ 付息日待办：#25（litter 不可数）／🎓#48（work 不可数）／#224（discrimination 不可数）
  里的"不可数"那一面考虑并入本条（那三条还各自带别的考点，不能整条并）

### 262 · 口语转折工具箱（Then again／That said／Having said that／On the flip side／Mind you）
类型 词组 ｜ **合并条·出题必须整组出**（§3.2c，她 2026-08-23 定：只出一句 ＝ 违规）｜ 新建 2026-08-20（**她当场指定**）
状态 连对2 连错0 上次2026-09-18 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
**口语转折工具箱**：Then again ／ That said ／ Having said that ／ On the flip side ／ Mind you
—— 同一条规则下的五个成员（合并条，§3.2c①），按【放句子的哪一段】分三档（详表见下方备注）：
· 开一个反面段落（放句首）：**Then again**（最口语，她已会）· **That said**（略正式）·
　**Having said that**（更长更缓，顺带争取思考时间）· **On the flip side**（专配"另一面"）
· 句中插入让步：**Mind you**（英式口语，插在两句之间）
判据一句话：这一句是要**拐到反面**吗？是 ⇒ 从这五个里挑一个起头（别一路 but／however）。
★ 与 🎓**#203**（…, though.）的分工：#203 管 though 这一个标记的**位置**（挂句尾）；
　本条管**有哪些可选、各自什么味道、放哪一段** ⇒ 规则不同，本条只做索引、不重复。
★ 与 🎓**#237**（a mixed bag）配套：先用 mixed bag 立"两面都有"，再用 Then again／On the flip side
　开第二面 —— 这是 P3 双面题最省力的骨架。

**怎么发现的**
2026-08-20 新建 · 加练新题（bank:927）· 她写 `Then again, rewards can slightly change what you intend.`
—— **她自己用对了**，并当场要求把这一族收进一条（**她当场指定**）。
★ 她的原话："Then again 可以新建条目，再几个转折方法在同一个条目，用于学习口语转折"
判重（当天新建复核）：grep "转折"／"though"／"Then again" 全库（含已毕业）→ 只命中 🎓#203（…, though.）。
**分工**：#203 管 though 这一个标记的**位置**（挂句尾）；本条管**有哪些可选、各自什么味道、放哪一段**
⇒ 规则不同，保留新建。

**我错在哪**
她这次没有错（`Then again, rewards can slightly change what you intend.` 用对了），
建号理由是 §2③ **她点名要学** —— 08-20 那天她只会 Then again 这一个，另外四个不会调。
找法：要拐到反面时先问一句 —— 这是"另一面"还是"补一刀"？另一面 ⇒ 从这五个里挑一个，⛔ 别一路 but。

**题面**
★ 5 句，五个转折标记各一句（她点名要学的工具箱 ⇒ 每句直接点名那个标记 ＝ 练用法：放哪一段、后面怎么接）
　① "网购确实方便，话说回来，退货也挺麻烦的。"（"话说回来"用 **Then again** 说）
　② "这家店是有点贵。话虽如此，东西确实好。"（"话虽如此"用 **That said** 说）
　③ "我不太喜欢加班。不过话说回来，这个月奖金确实多。"（"不过话说回来"用 **Having said that** 说）
　④ "在家办公很自由；反过来说，也特别容易分心。"（"反过来说"用 **on the flip side** 说）
　⑤ "他脾气是不太好——不过他从来不记仇。"（"不过"用 **Mind you** 插在中间说）

**成员出题账**
① Then again ｜ 08-20 新建（她自产）· 08-21 ✅（自由产出自发命中）· 08-23 ✅ · 08-31 📝（自发留痕）· 09-11 ✅
② That said ｜ 08-23 ✅ · 09-11 ✅
③ Having said that ｜ 08-23 ✅ · 08-31 📝（自发留痕，与 ① 并排备选）· 09-11 ✅
④ On the flip side ｜ 08-23 ✅ · 09-04 📝（自发留痕）· 09-11 ✅
⑤ Mind you ｜ 08-23 ✅ · 09-11 ✅

- 2026-08-20 新建 · 加练新题（bank:927）· `Then again, rewards can slightly change what you intend.`
  —— **她自己用对了**，并当场要求把这一族收进一条
- 2026-08-21 ✅ **自由产出自发命中**（加练新题 bank:414）· `Then again, you shouldn't only rely on ads.`
- 2026-08-23 ✅ 付息日 a 段 · **合并条 5 句整组首测，5/5 全对**（§3.2c）：
  `then again, rewards can also throw off a kid's motivation.` ／ `That said, I think it's worth a try.` ／
  `Having said that, it's not for everyone.` ／ `on the flip side, shopping online has its own hassles.` ／
  `mind you, he did nothing wrong.`
  —— 五个转折标记位置全对 → **连对2，毕业**
  ★ 08-20 建条目时她只会 Then again；今天五个一次全产出 ⇒ **装上了**
  ⚠️ ① 的 `throw off a kid's motivation` 搭配偏（throw off 配 balance／rhythm／concentration）
    → `knock their motivation off course`／`skew what kids are working for`。不建条目（§3.2b 第三档）
  ★ ⑤ `did nothing wrong` 顺带命中 🎓#35（否定只标一次），记进日志不改状态
  —— 又一次用在真转折点上。按 §4① 的**加速通道**（"在自由产出里自发出现就当场记 ✅，不用等"）记 ✅
  ★ 本条 08-20 新建、今天因"连对0 且零 ❌/📖"没进学习日池，结果**自己在产出里冒出来了** ——
    正是那条加速通道设计的场景
- 2026-08-31 📝 付息日 d 段 · 重答 R8 · **自发命中留痕**（🎓 合并条，状态行冻结）
  `**Then again/Having said that**, the relationship online is a bit more fragile.`
  一次带出本条工具箱里的**两个**成员（Then again ／ Having said that），转折位也选得准
  （前两句说好处，这里拐弯）。
  ★ 不计错：她是在打字里并排备选 ⇒ 只提醒"说的时候只能挑一个"，⛔ 不记档位、不判"不会选"。
- 2026-09-04 📝 **自发命中**（本条已毕业，只留痕、不推进数字）· 新题第 2 道
  `**On the flip side**, parents or older people may just talk at you…`
  ★ 本条题面第 ④ 句就是"反过来说，网上买也有网上买的麻烦。（用 On the flip side 起头）"。
  ★ 用得也对：前半句说朋友（同频）、后半句说父母（说教）—— 正是"另一面"，不是简单追加。
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · **合并条 5 句整组出，5/5 全中**
  `Then again, rewards can also mess up a kid's motivation.` ／ `That said, I still think it's worth a shot.` ／
  `Having said that, it's not for everyone.` ／ `On the flip side, buying online has its own hassles.` ／
  `Mind you, he didn't do anything wrong, either.`
- 2026-09-12 📝 题面整改：五句点名从「用 Then again 起头」这类整块给出改成首字母＋词数（§6② 红线一：本条要学的就是这五个标记本身，给出来 ＝ 零信息量；09-11 那次 5/5 全中是照抄提示，不算证据）· 全档题面 review
- 2026-09-18 ✅ 自发命中 · 学习日 新题 bank:353（P3 · 自由产出）· `Then again, people who play team sports are generally more passionate about working out.`——话锋一转的位置用对
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉首字母／词数／排除项的猜谜写法；她点名要学的工具箱 ⇒ 五句各直接点名一个转折标记，练的是放哪一段、后面怎么接
- 备注 六个标记，按【放句子的哪一段】分三档：
```
① 开一个反面段落（放句首）
   Then again, …          话说回来（最口语，她已会）
   That said, …           话虽如此（略正式，书面口语都能用）
   Having said that, …    同上，更长更缓，顺带给自己争取思考时间
   On the flip side, …    反过来说（专配"另一面"，和 a mixed bag 这类立论天生一对）
② 句中插入让步
   Mind you, …            不过话说回来（英式口语，插在两句之间）
③ 挂句尾
   …, though.             ＝ 🎓#203，本条只做索引，不重复
```
- 备注 与 🎓#237（a mixed bag）配套：先用 mixed bag 立"两面都有"，再用 Then again／On the flip side
  开第二面 —— 这是 P3 双面题最省力的骨架

### 263 · 双宾语语序：promise／give／tell／show／send 一律【人在前，东西在后】
类型 搭配 ｜ **合并条·出题必须整组出**（§3.2c，她 2026-08-23 定：只出一句 ＝ 违规）｜ 新建 2026-08-20
状态 连对2 连错0 上次2026-09-11 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
双宾语语序：**promise／give／tell／show／send** 一律【**人在前，东西在后**】。
判据：这一族动词带两个宾语时，顺序固定 **动词 ＋ 人 ＋ 东西**
```
✅ promise your kid the iPhone ／ give me the book ／ tell her the truth ／ show him the photo
要把"东西"放前面，就必须加介词把人挂后面：
✅ promise the iPhone TO your kid ／ give the book TO me ／ buy a coffee FOR her
❌ promise the iPhone your kid（中文"承诺一台 iPhone 给你孩子"是东西在前，直接照搬就反）
```
★ 与 **#171**（tell sb：say 后面不接人）的分工：#171 管"要出现人就不能用 say"（选哪个动词）；
　本条管"两个宾语谁在前"（语序）⇒ 规则不同。
★ 与 🎓**#143**（哪些动词后面要带 to）的分工：那条管"后面接不定式"，与双宾语无关。
★ 与 **#319** 的分工（2026-09-04 从本条的过度泛化里另开）：**present 不在这一族**
　（只有 present sth TO sb ／ present sb WITH sth）⇒ 成员名单是封闭的，⛔ 不许往外套。

**怎么发现的**
2026-08-20 新建 · 加练新题（bank:927）· 她写 `You promise a lastest iPhone your kid`
（→ promise **your kid** the latest iPhone）—— 东西在前、人在后，正好反了。
判重（当天新建复核）：grep "双宾"／"promise"／"tell sb" 全库（含已毕业）→ 命中 #171（tell sb：say 后面不接人）。
**区别**：#171 管"要出现人就不能用 say"（选哪个动词）；本条管"两个宾语谁在前"（语序）⇒ 规则不同，保留。
另比 🎓#143（哪些动词后面要带 to）：那条管"后面接不定式"，与双宾语无关。

**我错在哪**
她的：`You promise a lastest iPhone your kid`　　正确：`You promise **your kid** the latest iPhone`
找法：说完 promise／give／tell／show／send，先看紧跟着的那个词 —— **是"人"吗？**
不是 ⇒ 要么把人提到前面，要么给人加 TO／FOR 挂到后面。

**题面**
★ 4 句，覆盖这一族的不同动词（只点动词；人和东西谁在前留给她 —— 加 to 把人挂后面也算对）
　① "我答应过女儿一只小狗。"（"答应"用 **promise** 说）
　② "过年奶奶给了每个孙子一个红包。"（用 **give** 说）
　③ "他把新房子的照片给我们看了。"（用 **show** 说）
　④ "我每年都给老同学寄一张贺卡。"（用 **send** 说）

**成员出题账**
① promise ｜ 08-20 ❌（首犯）· 08-21 ✅ · 08-23 ✅ · 08-24 ✅（自由产出自发命中）· 09-11 ✅
② give ｜ 08-23 ✅ · 09-11 ⚡（她当场免测："2) - 3) 直接过"）
③ show ｜ 08-23 ✅ · 09-11 ⚡（她当场免测："2) - 3) 直接过"）
④ send ｜ 08-23 ✅ · 09-11 ✅
⑤ tell ｜ 未出过（题面 4 句未覆盖，只在判据表里出现过 tell her the truth）

- 2026-08-20 新建 · 加练新题（bank:927）· `You promise a lastest iPhone your kid` → promise **your kid** the latest iPhone
- 2026-08-21 ✅ 复习（新建后首测）· `He promised his son the lastest phone.`——语序一字不差：
  promised ＋ **his son**（人）＋ **the latest phone**（东西），08-20 首犯正好是反的
- 2026-08-23 ✅ 付息日 a 段 · **合并条 4 句整组首测，4/4 全对**（§3.2c 她当天定的新规则第一次实战）：
  `he promised his son the lastest phone.` ／ `she gave me a really old book.` ／
  `he showed me the photo.` ／ `I sent her a postcard.`
  —— promise／give／show／send 四个动词的语序全是【人在前、东西在后】→ **连对2，毕业**
  ★ 08-20 只在 promise 上错过、也只测过 promise；这次四个成员全覆盖后毕业，含金量与以前不同
  ｜`lastest` 是拼写，按 §2.1 不算
  ★ "买"没译出不扣：promise sb sth 本身就含"给"｜`lastest` 按 §2.1 拼写不算
- 2026-08-24 ✅ **自发命中**（本条未被出题，不改已毕业状态）· 新题 bank:924 ·
  `Say you **promise your kid the latest iPhone** if they do well in their finals`
  ——人在前、东西在后，一次到位（08-20 同话题加练时她走的是 `it's an iPhone` 绕开了双宾语）
- 2026-09-04 📝 **过度泛化留痕**（⛔ 不判回潮、状态行一个字不动）· 新题第 1 道
  `he **presented me a picture**`（语序 ＝ 动词 ＋ 人 ＋ 东西）
  ★ 她的**语序是对的**，本条的规则她执行得没问题 —— 错在把本条的规则
    **套到了不属于这一族的动词上**（present 只有 present sth TO sb ／ present sb WITH sth）。
  ★ **决定性证据**：按本条的规则去改她这句 ⇒ 语序已经对了 ⇒ **改不出正确答案**
    ⇒ 不同考点 ⇒ 另开 #319，本条只留痕。
  ★ 本条 备注 早写过「过度泛化警报：修一处，隔壁被带偏」（原是冲着 #18／🎓#134 写的）——
    **这是它的第二次实证，方向不同**：这次被带偏的是"动词能不能进双宾语这一族"。
- 2026-09-11 ✅ 复检 · 付息日 a2 第 7 组 · 合并条 4 句：① `he promised his son the latest phone.` ✔ ④ `I sent her a postcard.` ✔（人在前、没用 to）；②③ 她当场免测（"2) - 3) 直接过"）⇒ 整组覆盖记 ✅
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"两个宾语／不用 to"写法，只点动词，人和东西谁在前留给她（加 to 挂后面也算对）；四句全换新场景


### 264 · a sense of ＋ 表示"一种感受／意识"的名词（⛔ a sense of payoff／reward／result）
类型 搭配 ｜ 新建 2026-08-20（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

**问题是什么**
**a sense of** ＋ 一个表示"人能感觉到的一种状态／意识"的抽象名词。
判据：a sense of 后面那个名词得是一种**感受**；是**结果／回报**就不进这个框：
```
✅ a sense of achievement（成就感）｜ a sense of purpose（目标感）｜ a sense of belonging（归属感）
   a sense of control（掌控感）｜ a sense of direction ｜ a sense of urgency ｜ a sense of humor
   a sense of community ｜ a sense of occasion ｜ a sense of ritual（仪式感）
❌ a sense of payoff／a sense of reward／a sense of result —— 这些是结果，不是感受
★ 想说"有奔头/值得"，走别的说法，不要硬塞进 a sense of：
   something to work towards（有个目标可奔）
   make the effort feel worth it（让努力显得值）
   feel like it's paying off（感觉有回报了）—— payoff 的动词形式反而好用
```
一句话规则：a sense of 后面的名词是一种感受吗？是 ⇒ 成立；是结果／回报 ⇒ 换整个说法。
★ 与 🎓**#206**（书面词降级）的分工：那条管"这个词太书面，换口语版"；
　本条管"a sense of 后面能挂什么" ⇒ 不同层，不重复。

**怎么发现的**
2026-08-20 新建 · 加练新题（bank:927）· 她写 `Rewards can give kids a sense of payoff`
⇒ 语法没错，但 **a sense of ＋ payoff 不是现成搭配**；payoff 这个词是前一道题教练更好版里给的，
她隔一道题就抓来用了（迁移意识好），只是塞进了一个装不下它的框架 ⇒ **她当场指定**建号。
判重（当天新建复核）：grep "a sense of"／"payoff"／"achievement" 全库（含已毕业）→ **零命中**，
全库没有任何条目管这个框架 ⇒ 保留新建。
另比对 🎓#206（书面词降级）：那条管"这个词太书面，换口语版"；本条管"这个**框架**只收哪几个词"
⇒ 不同层，不重复。

**我错在哪**
她的：`Rewards can give kids **a sense of payoff**`
正确：`a sense of **purpose**`（框里的词）／或整个换说法 `something to work towards`
找法：a sense of 一出口就问 —— 后面那个名词是一种感受吗？是结果／回报（payoff／reward）⇒ ⛔ 别硬塞，换整句说法。

**题面**
"跑完第一个马拉松，我特别有成就感。"（"成就感"用 **a sense of** 说）

- 2026-08-20 新建 · 加练新题（bank:927）· `Rewards can give kids a sense of payoff`
  ⇒ 语法没错，但 **a sense of ＋ payoff 不是现成搭配**；payoff 这个词是前一道题教练更好版里给的，
    她隔一道题就抓来用了（迁移意识好），只是塞进了一个装不下它的框架
- 2026-08-21 ✅ 复习（点名题面首测）· `rewards makes children feel that their efforts are worth it.`
- 2026-08-23 ✅ 付息日 a 段 · `rewards give kids something to move forward.`
  ——**完全绕开 a sense of**，而且直接走到本条备注列的出口模板（something to …）⇒ 考点位置达成
  → **连对2，毕业**
  ❌ 同句 `something to move forward` 短语本身不成立（不定式尾部丢了介词）⇒ 归 **🎓#103 回潮**，
    不算本条头上。现成块是 **something to work towards**
  ——完全绕开 a sense of，用的正是本条备注列的出口之一（make the effort feel worth it）
  ⚪ 同句 `rewards **makes**` 主谓一致 ⇒ 属 #10（形态类·不召回），只做记号不记档位
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `a sense of purpose` —— a sense of ＋ 固定名词，⛔ 没自己造词、⛔ 没走本场新排除的 pay off
- 2026-09-11 📝 题面整改：补（用 **a sense of** ＋ 一个固定搭配的名词说，⛔ 不许自己造词、⛔ 不许用 pay off）· 发题前审核（**换结构**那一类）
  `Your effort pays off.` 完全合法，绕开 a sense of ＋ 固定名词 ⇒ 补排除项。今天她答 a sense of purpose ⇒ 排除项生效
- 2026-09-19 📝 卡片规则改正 · 付息日 d 段重答 R11 · 她说 `there's a nice sense of ritual to it`
  原卡片写"a sense of 只收 achievement／purpose／belonging／control／direction 五个"，照它判会把地道的 a sense of ritual 冤成错
  ⇒ 改成"后面是一种感受就成立（urgency／humor／community／occasion／ritual…），是结果／回报（payoff／reward／result）才不进"；
    标题、问题是什么、找法、题面（去掉"⛔ 不许自己造词"）同步改，⛔ 状态行不动、⛔ 不记档位
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"＋ 一个名词／⛔ pay off"，点名 a sense of，后面挂哪个名词留给她（她掉过的是 a sense of payoff）；换成跑马拉松场景

### 265 · 对身体好 ＝ good for you／good for your health（health 前面不能光秃秃）
类型 搭配 ｜ **合并条·出题必须整组出**（§3.2c，她 2026-08-23 定：只出一句 ＝ 违规）｜ 新建 2026-08-21
状态 连对2 连错0 上次2026-09-22 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-23**（连对达线 ＋ 她当场指定"这条毕业"）｜ 题型 整句

**问题是什么**
对身体好 ＝ **good for you** ／ **good for your health**（health 前面不能光秃秃）。
判据：英语里 `for health` 前面必须有东西托住 —— 要么整句换成 **good for you**（最口语），
要么补物主代词 **good for your health**。裸的 for health 是中文"对健康好"直译过来的。
同一格里的邻居（别串 —— 中文不说"你的"、英文必须说的一族）：
your health ／ your memory ／ your eyesight ／ your mood ／ your back ／ your skin —— 身体和心智属性一律带物主代词。
★ 范围只到 **good/bad for ___**：`vital/essential **to** health` 裸的**成立**（偏正式书面）⇒ ⛔ 不许扩大成
　"所有 health 前面都要物主代词"（见下方 ⚠️ 收尾 1b 复核）。
★ 与 🎓**#255** 的分工：#255 管**选 vital 还是 virtual**（选词），本条管 **good for 后面缺限定词**（搭配）⇒ 不并。
★ 与 **#254** 的分工：#254 考点在**主语位 -ing**，本条考点在 **good for 后面的限定词** —— 落在句子不同位置。

**怎么发现的**
2026-08-21 新建 · 复习 #254 句里 · 她写 `going to bed early is good for **health**`
（→ good for **you**／good for **your** health）—— 裸的 for health。
判重（当天新建复核）：① 目标形式 ＝ `good for you`／`good for your health`
② grep "good for"（含已毕业）→ 全库零命中；grep "物主"／"your health"／"身体" → 零命中
③ 最接近三条逐条读过：#63（泛指 vs 特指）管 the ／复数，对象是可数名词，health 不可数 ⇒ 不同规则；
　 #157（直译搭配）管"这个词配不配"（power 配不配 weak），本条是"这个位置缺限定词" ⇒ 层不同；
　 #89（加形容词回到 a）管冠词 a，与物主代词无关 ⇒ 保留新建。

**我错在哪**
她的：`going to bed early is good for **health**`　　正确：`good for **you**` ／ `good for **your** health`
找法：说完 good／bad for，看下一个名词 —— **前面有没有 your（或换成 you）？** 光秃秃 ⇒ 补上。

**题面**
★ 3 句，覆盖 good/bad for ＋ 不同的身体/心智属性（考点是 good for 后面托不托住 ＝ 靠句子现形 ⇒ 整句题）
　① "饭后出去走走对身体好。"（用 **good for** 说）
　② "老熬夜对记忆力不好。"（用 **bad for** 说）
　③ "少吃盐对心脏好。"（用 **good for** 说）
　　★ 目标形式（教练看，⛔ 不进发题稿）：① good for you ② bad for your memory ③ good for your heart

**成员出题账**
① good for you ｜ 08-21 ❌（首犯，裸 good for health）· 08-23 ✅（复习 #254 句里，带上 your）· 08-23 ✅（整组首测，走 good for your health ＝ 同一规则另一合法出口）· 09-11 ✅
② bad for your memory ｜ 08-23 ✅ · 09-11 ✅
③ good for your heart ｜ 08-23 ✅ · 09-11 ✅

- 2026-08-21 新建 · 复习#254 句里 · `going to bed early is good for **health**` → good for **you**／good for **your** health
- 2026-08-23 ✅ 复习#254 句里 · `going to bed early is good for **your** health.`
  —— 08-21 那次写的是裸的 `good for health`（正是因此新建本条），今天限定词带上了 ⇒ 连对 0→1，连错清零
- 2026-08-23 ✅ 付息日 a 段 · **合并条 3 句整组首测，3/3 全对**（§3.2c）：
  ① `this kind of tea is good for your health.`（题面目标是 good for you；她走 good for your health，
     同一条规则的另一个合法出口 ⇒ 考点达成）
  ② `staying up late is bad for your memory.` ③ `walking more is really good for your heart.`
  —— 三个位置的限定词全带上了，08-21 那次的裸 `good for health` 彻底翻过来
  → **连对2，毕业**；她同时当场指定"这条毕业"
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · **合并条 3 句整组出，3/3 全中** · `good for your health.` ／ `bad for your memory.` ／ `good for your heart.`
  —— 三处 health／memory／heart 前面都带了 your，⛔ 没有光秃秃的裸名词
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  考点是 good for 后面托不托住 ＝ 靠句子现形；三句换新场景，只点 good for／bad for
- 备注 同族（中文不说"你的"，英文必须说）：
  your health ／ your memory ／ your eyesight ／ your mood ／ your back ／ your skin
  —— 身体和心智属性一律带物主代词
- 备注 ⚠️ **收尾 1b 复核追加（2026-08-21）**：复查时发现 🎓#255 的 08-20 日志里有 `sleep is vital **to** health`，
  当时判 ✅ —— **那次判 ✅ 是对的，不追改**。两处不是同一件事：
```
good/bad **for** health        ⇒ 裸的不成立 ⇒ good for **you** ／ good for **your** health　← 本条管这个
vital/essential **to** health  ⇒ 裸的**成立**（偏正式书面：Sleep is vital to health.）
                                  口语里仍然更常说 vital to **your** health
★ 所以本条的范围**只到 good/bad for ___**，不许扩大成"所有 health 前面都要物主代词"——
  那就又是今天 #50 那种"从一个实例过度概括"的毛病
```
  ⇒ 与 #255 的分工：#255 管**选 vital 还是 virtual**（选词），本条管 **good for 后面缺限定词**（搭配）⇒ 不并

### 266 · "除了…（排除）" ＝ apart from ／ other than ／ except（besides 放句首会被读成"此外"）
类型 词组 ｜ **合并条·出题必须整组出**（§3.2c，她 2026-08-23 定：只出一句 ＝ 违规）｜ 新建 2026-08-21（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-24** ｜ 题型 整句

**问题是什么**
"除了…（排除）" ＝ **apart from** ／ **other than** ／ **except**（**besides** 放句首会被读成"此外"）。
四个可选按口语常用度排（详表见下方备注）：apart from（最稳、最口语，句首句尾都不歧义 ★ 目标形式）·
other than（同义，略正式）· except (for)（也对，except for 更常挂句首）·
besides（否定句里成立，但**放句首容易被读成"此外／而且"** ⇒ 想说"排除"就别用它开头）。
一句话判据：**要"减掉一个人/一样东西" → apart from ｜ 要"再加一层理由" → besides**
（besides 的主业是**加法**：Besides, it's too expensive. ＝ 再说，太贵了）。
★ 与 **#75**（other than ≠ rather than）的分工：#75 管**两个形近词组别混**（形近误用），目标形式是 other than；
　本条管"除了"这个意思**该选哪个词组、besides 为什么不稳**（选词），目标形式是 apart from ⇒ 两条并存。
★ 与 🎓**#260**（"这事"→ it／about it）的分工：那条管句子另一个位置的选词，不冲突。

**怎么发现的**
2026-08-21 新建 · **她主动提出**（§2③）· 复习 #260 句里她写 `Besides him, no one knows about it.`
—— 教练判 ✅ 不扣（besides 在否定句里确实成立），但她说 **apart from 非常不熟练** ⇒ 建条目。
★ 她的原话："Apart from him 可以建一个，非常不熟练"
判重（当天新建复核，§4④1b）：
　① 目标英文形式 ＝ `apart from`
　② grep "apart from" 全库（含已毕业）→ **零命中**；grep "other than" → 命中 #75；
　　 grep 中文"除了" → 命中 #75 与 #260 的题面
　③ 逐条读：**#75**（other than ≠ rather than）管的是**两个形近词组别混**（形近误用），
　　 目标形式是 other than；**本条**管的是"除了"这个意思**该选哪个词组、besides 为什么不稳**（选词），
　　 目标形式是 apart from ⇒ 规则不同、目标形式不同 ⇒ **两条并存**。
　　 **#260**（"这事"→ it/about it）管的是句子另一个位置的选词，不冲突。
⚠️ **题面必须互斥**（§3.1 第三档）：#75 的题面正好是"除了他没人知道这事。"（用 other than 说），
　 #260 的题面也是同一句 ⇒ 本条题面**另起一句**："除了我妈，没人知道我辞职了。"，三条从此不撞车。

**我错在哪**
她这次没有错（`Besides him, no one knows about it.` 教练判 ✅ 不扣 —— besides 在否定句里确实成立），
建号理由是 §2③ **她点名要学**（原话："Apart from him 可以建一个，非常不熟练"）。
找法：想说"除了…（排除）"时，⛔ 别拿 besides 开头 —— 默认调 **apart from**，要 besides 就问自己"我是在加还是在减？"

**题面**
★ 3 句，三个成员各一句（她点名要学、三个都是同义 ⇒ 每句直接点名那个词组 ＝ 练用法：放句首还是句中、后面接什么）
　① "除了我妈，家里没人会做饭。"（"除了"用 **apart from** 说）
　② "除了我哥，谁都不知道这件事。"（"除了"用 **other than** 说）
　③ "除了周末，我每天都在家吃早饭。"（"除了"用 **except** 说）
　★ besides 不进出题：它在否定句里成立、放句首却会被读成"此外"，属**判据**不属目标形式

**成员出题账**
① apart from ｜ 08-23 ✅ · 08-24 ✅ · 09-11 ✅
② other than ｜ 08-23 ✅ · 08-24 ✅ · 09-11 ✅
③ except ｜ 08-23 ✅ · 08-24 ✅ · 09-11 ✅

- 2026-08-21 新建 · **她主动提出**（§2③）· 复习#260 句里她写 `Besides him, no one knows about it.`
  —— 教练判 ✅ 不扣（besides 在否定句里确实成立），但她说 **apart from 非常不熟练** ⇒ 建条目
- 2026-08-23 ✅ 付息日 a 段 · **合并条 3 句整组首测，3/3 全对**（§3.2c）：
  ① `Apart from my mum, no one knows I quit my job.` ② `Other than him, I don't know anyone.`
  ③ `I barely have any free time, except for weekends.`
  —— 三个成员一次全产出。08-21 她自陈"apart from 非常不熟练"，两天就装上了 ⇒ 连对 0→1
  ★ ③ 她把句序反过来说（"我基本没空，除了周末"）—— 完全合法且符合题面 ⇒ 记 ✅
  ★ ① 顺带命中 🎓#59（嵌进句子里用陈述语序）｜ ③ 的 `barely have any` 与 #269 同一条规则
- 2026-08-24 ✅ 复习第1组 · **合并条 3 句整组第二次，3/3 全对**（§3.2c）：
  ① `Apart from my mum, no one knows I quit my job.` ② `Other than him, I don't know anyone else.`
  ③ `I barely have any free time except for weekends` ⇒ **连对 1 → 2 ⇒ 🎓 毕业**
  ★ 教练自审留痕：一度想给 ② 标"other than him ＋ anyone else 语义重复"。试造母语句推翻自己
    —— `Apart from my brother, I don't know anyone else in this city.` 完全自然 ⇒ **不是冗余，不标**。
    与 08-23 `So overall` 假错同一形状（拿书面冗余标准评口语，§2.3b 禁令）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 4 组 · 合并条 3 句整组出，3/3 全中 · `Apart from my mum.` ／ `Other than my brother.` ／ `except on weekends`
- 2026-09-12 📝 题面整改：三句点名从整块给出（apart from／other than／except）改成首字母＋词数（§6② 红线一：她建号的原话就是"非常不熟练"，块给出来 ＝ 零信息量）；目标形式移到 ★ 行 · 全档题面 review
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉首字母／词数／排除项；她点名要学、三个成员同义 ⇒ 每句直接点名那个词组，练句首／句中的用法
- 备注 四个可选，按口语常用度排：
```
apart from him    ← 最稳、最口语，句首句尾都不歧义        ★ 本条的目标形式
other than him    ← 同义，略正式一点；#75 测的是这个
except (for) him  ← 也对；except for 更常挂句首
besides him       ← 否定句里成立（No one besides me knows.），
                    但**放句首容易被读成"此外／而且"** ⇒ 想说"排除"就别用它开头
```
- 备注 反向记：besides 的主业是**加法**（Besides, it's too expensive. ＝ 再说，太贵了）
  ⇒ 一句话判据：**要"减掉一个人/一样东西" → apart from ｜ 要"再加一层理由" → besides**
- 备注 常见搭配位置：Apart from that, … ／ Apart from a few typos, it's fine. ／
  I don't know anyone here apart from you.

### 267 · get sth in front of sb（把产品／信息摆到人眼前）
类型 词组 ｜ 新建 2026-08-21（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-24** ｜ 题型 整句

**问题是什么**
**get sth in front of sb** ＝ 把产品／信息摆到人眼前、让人看见（营销／传播的默认说法）。
同一格里的邻居（别串）：**reach** people ＝ 触达（中性、略正式）；
**get sth in front of** people ＝ 摆到眼前（更具体、更口语）—— 详例见下方备注。
判据一句话：要说"让人看见／送到眼前"时，别绕 see／show／notice，直接调 get sth in front of sb 这个块。
★ 与 🎓**#39**（惯用定冠词 the TV／the radio）的分工：那条里的 "in front of" 只是**字面义**顺带出现；
　本条管的是**引申块 get sth in front of sb** ⇒ 目标形式不同、规则不同，两条题面互不撞车。

**怎么发现的**
2026-08-21 新建 · **她主动提出**（§2③）· 加练新题（bank:414）· 她写
`Ads help get your product or service in front of the public.` —— **她自己用对了**，并当场要求建条目。
★ 她的原话："in front of 这个词组要新建条目"
判重（当天新建复核）：① 目标形式 ＝ `get sth in front of sb`
② grep "in front of" 全库（含已毕业）→ 只命中 🎓#39 的日志行（`he sat in front of the TV all night.`）
③ 逐条读 #39：那条管的是**惯用定冠词**（the TV／the radio／the cinema／on the screen），
　 "in front of" 只是那句话里顺带出现的**字面义**；本条管的是**引申块 get sth in front of sb**
　 ⇒ 目标形式不同、规则不同 ⇒ 保留新建，两条题面互不撞车。

**我错在哪**
她这次没有错（`Ads help get your product or service in front of the public.` 一次用对），
建号理由是 §2③ **她点名要学**（原话："in front of 这个词组要新建条目"）。
找法：要说"让人看见 X"时，先问一句 —— 能不能说成"把 X 摆到人眼前"？能 ⇒ get X in front of sb。

**题面**
"开网店最难的，是怎么让更多人看到你的东西。"（"让人看到"用 **in front of** 说）

- 2026-08-21 新建 · **她主动提出**（§2③）· 加练新题（bank:414）· `Ads help get your product or service in front of the public.`
  —— **她自己用对了**，并当场要求建条目
- 2026-08-23 ✅ 付息日 a 段 · **本条从建立起第一次被测到，一次到位** ·
  `you need to get your product in front of people first.`——`get your product in front of people` 一字不差
- 2026-08-24 ✅ 复习第1组 · `you need to get your product in front of people.`——目标块一字不差
  ⇒ **连对 1 → 2 ⇒ 🎓 毕业**
  ⚠️ 这次丢了句尾的 `first`（08-23 那次是带着的）：题面的"**先**"要落成句尾 first
    —— 句首 `First, …` ＝ 列点"第一条"，不是排先后。不是错，不落号
- 2026-09-11 ✅ 复检 · 付息日 a2 第 4 组 · `get your production in front of people` —— get sth in front of sb 一字不差
  ⚠️ production 是 product 的选词滑手（§2.1 边界：另一个词，照常记）；⛔ 不建条目 —— 本条 08-21／08-23／08-24 三次她写的都是 product
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"get 起头 ＋ ⛔ see／show／notice"，她点名要学的块 ⇒ 点名 in front of，get sth … 怎么搭留给她；换成开网店场景
- 备注 内容：get sth **in front of** sb ＝ 把东西摆到人眼前、让人看见（营销/传播的默认说法）
```
✅ get your product in front of the right people ／ in front of customers
✅ get your message in front of a bigger audience
✅ get your CV in front of the hiring manager
★ 跟 reach 的分工：reach people ＝ 触达（中性、略正式）
                  get sth in front of people ＝ 摆到眼前（更具体、更口语）
```

### 268 · "卖得好／好读／好洗" 用【主动形式】：it sells well（不用 is sold well）
类型 语法 ｜ **合并条·出题必须整组出**（§3.2c，她 2026-08-23 定：只出一句 ＝ 违规）｜ 新建 2026-08-21
状态 连对2 连错0 上次2026-09-22 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-24** ｜ 题型 整句

**问题是什么**
"卖得好／好读／好洗" 用【**主动形式**】：**it sells well**（⛔ 不用 is sold well）。
判据：英语里有一小族动词 **主语是东西、动词用主动、意思却是被动**（中动语态）
```
✅ This product **sells** well.        ✅ The book **reads** easily.
✅ This shirt **washes** well.         ✅ The recipe **cooks** in ten minutes.
✅ She **photographs** well.           ✅ The door **won't open**.   ✅ The cake **cuts** easily.
✗ is sold well ＝ "被人用好的方式卖掉"，不是"畅销"
★ 一句话判据：说的是"**这东西本身好不好卖/好不好用**" ⇒ 主动；
             说的是"**谁把它怎么样了**" ⇒ 才用被动
★ 这一族基本固定，背这几个就够：sell／read／wash／cook／photograph／open／cut
```
★ 这一族**成员数得出来 ＝ 有限集合** ⇒ 按 §3.2c⑤ 合成一条，⛔ 不是伞形条目。
★ 附带一格（④ 句里现形）：**won't open** 的 won't 不是将来时，是"**就是不肯**"
　（The car won't start. ／ The lid won't come off.）—— doesn't open ＝ 设计上就不开／平时不开。

**怎么发现的**
2026-08-21 新建 · 加练新题（bank:414）· 她写 `they will wonder whether it **is sold well**`
（→ it **sells** well）—— 中文"卖得好"直接搬成了被动。
判重（当天新建复核）：① 目标形式 ＝ `it sells well`
② grep "sell"／"卖"／"主动表被动"／"中动" 全库（含已毕业）→ **零命中**
　（grep "卖" 只命中三条"外卖"题面 ＝ takeaway，与本条无关）
③ 全库没有任何条目管"主动形式表被动"这条规则 ⇒ 保留新建。

**我错在哪**
她的：`they will wonder whether it **is sold well**`　　正确：`whether it **sells** well`
找法：主语是**东西**、要说"好不好卖／好不好用"时问一句 —— 我是在说"这东西本身怎么样"吗？
是 ⇒ 动词用**主动**，⛔ 别加 be ＋ 过去分词。

**题面**
★ 4 句，覆盖中动语态那一族的不同动词 —— 只出 sell 一句会漏掉她真正错的那个
　① "这款卖得特别好。"（用 **sell** 说）
　② "这本书很好读。"（用 **read** 说）
　③ "这件衬衫很好洗。"（用 **wash** 说）
　④ "这门打不开。"（用 **open** 说）
　　★ 目标形式（教练看，⛔ 不进发题稿）：① it sells well ② it reads easily ③ it washes well ④ the door won't open

**成员出题账**
① sell ｜ 08-21 ❌（首犯 is sold well）· 08-23 ✅ · 08-24 ✅ · 09-11 ⚡（她当场免测："8. 直接过"）
② read ｜ 08-23 ✅ · 08-24 ✅ · 09-11 ⚡（同上）
③ wash ｜ 08-23 ✅ · 08-24 ✅（washs 是拼写，§2.1 不算）· 09-11 ⚡（同上）
④ open ｜ 08-23 ✅（doesn't open，教练给 ⚠️ won't）· 08-24 ✅（零提示自己调出 won't ＝ 真迁移）· 09-11 ⚡（同上）

- 2026-08-21 新建 · 加练新题（bank:414）· `they will wonder whether it **is sold well**` → it **sells** well
- 2026-08-23 ✅ 付息日 a 段 · **合并条 4 句整组首测，4/4 全对**（§3.2c）：
  ① `this one sells really well.` ② `this book reads really well.` ③ `This shirt washes really well.`
  ④ `this door doesn't open.` —— 四个动词全部走主动形式（08-21 她写的是 is sold well）⇒ 连对 0→1，连错清零
  ⚠️ ④ `doesn't open` → **won't open**：不是错，但差一层意思 ——
    doesn't open ＝ 这门（设计上）就是不开／平时不开；**won't open ＝ 现在推不动、打不开**（中文"打不开"要的是这个）
    ★ 这个 won't 不是将来时，是"**就是不肯**"：The car won't start. ／ The lid won't come off.
- 2026-08-24 ✅ 复习第1组 · **合并条 4 句整组第二次，4/4 全对**（§3.2c）：
  ① `this product sells really well` ② `this book reads really well.` ③ `this shirt washs easily.`
  ④ `this door won't open.` ⇒ **连对 1 → 2 ⇒ 🎓 毕业**
  ★★ ④ 是一次**真迁移**：08-23 她写 `doesn't open`、教练给了 ⚠️（won't ＝ 就是不肯开），
     **今天她零提示自己调出了 won't** —— 那条 ⚠️ 装上了
  ｜③ `washs` → 正确拼法 washes（sh/ch/s/x/o 结尾加 -es）；按 §2.1 **拼写不算错**，
     调的词是 wash 一字没歪 ⇒ 考点照常 ✅
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 4 组（她原话："8. 直接过"）
- 2026-09-12 📝 题面整改：删掉四句点名里的「不用被动」（§6② 红线一：本条考点就是"不用被动"，写在提示里 ＝ 把考点交出去）；目标形式移到 ★ 行 · 全档题面 review
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组

### 269 · "不太了解／知道得少" 口语走 don't know much about it（不用 know little／only know little）
类型 结构 ｜ **合并条·出题必须整组出**（§3.2c，她 2026-08-23 定：只出一句 ＝ 违规）｜ 新建 2026-08-21（**她当场指定**）
状态 连对1 连错0 上次2026-09-22 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-23 · 她指定**（"这条毕业"）｜ 题型 整句

**问题是什么**
"不太了解／知道得少" 口语走 **don't know much about it**（⛔ 不用 know little／only know little）。
判据：**中文说"少"，英语口语优先走【否定 ＋ much/any】，不走【肯定 ＋ little】**
```
✅ People don't know much about it.          ← 口语默认，最常听
✅ People hardly know anything about it.     ← 更强（几乎完全不知道）
✅ Most people have never even heard of it.  ← 换个角度，更有画面
⚠️ People know little about it.              ← 成立，但是**书面语**
                                                （We know little about his early life.）
✗ People only know little about it.          ← only ＋ little 两个"少"叠着，生硬
★ 同一条规则的其他形态（口语一律否定起头）：
   don't have much time（不说 have little time）
   there isn't much to do（不说 there is little to do）
   I haven't got many left（不说 I have few left）
```
★ 边界（08-20／08-21 两次裁决方向相反，详表见下方 ⚠️ 备注）：**few/little 修饰名词当主语 → 正常；
　用来说"知道得少/有得少" → 换成否定 ＋ much**。
★ 与 **#271** 的分工（互斥写死，2026-09-05 定）：**带"最近/这阵子" ⇒ #271（时态拉完成时）；
　不带时间副词 ⇒ 本条（much/any）**。
★ 与 🎓**#115**（a couple of ＝ 两个；"几个"用 a few）的分工：那条管"几个"该用哪个量词；
　本条管"知道得少"这个意思口语该怎么说 ⇒ 规则不同、目标形式不同。

**怎么发现的**
2026-08-21 新建 · **她主动提出**（§2③）· 加练新题（bank:414）· 她写
`If people **only know little** about the product, …`（→ If people **don't know much** about it, …）。
⛔ **教练犯规·漏错**：教练当场按 08-20 的先例（`only few` 那次）判"不判"，
她当场指出**这次不是 few/little 的问题，是整个说法生硬** ⇒ 判罚恢复，建条目。
★ 她的原话："only know little 这个也建一个条目吧，确实不地道（很生硬，有更好的表达方式，
　是需要建条目的）**不是 little 的问题**"
判重（当天新建复核）：① 目标形式 ＝ `don't know much about it`
② grep "know much"／"know little"／"hardly"／"not much" 全库（含已毕业）→
　 只命中 🎓#115 的 08-20 备注行（`only few` 那次撤销的记录）
③ 逐条读 #115（a couple of ＝ 两个；"几个"用 a few）：那条管的是**"几个"这个量该用哪个量词**，
　 且 08-20 的裁决明确说 few 不带 a 是对的；**本条管的是"知道得少"这个意思口语该怎么说**
　（否定 ＋ much，而不是肯定 ＋ little）⇒ 规则不同、目标形式不同 ⇒ 保留新建，两条题面互不撞车。

**我错在哪**
她的：`If people **only know little** about the product, …`
正确：`If people **don't know much** about it, …`
找法：中文冒出"少／不太"时问一句 —— 我是在说"知道得少／有得少"吗？
是 ⇒ 句子从 **don't／there isn't** 起头 ＋ much／any，⛔ 别用肯定 ＋ little。

**题面**
★ 3 句，覆盖"说少一律走否定 ＋ much/any"这条规则的三个高频位置
　① "我对这个行业不太了解。"（"不太了解"用 **don't** 起头说）
　② "月底了，我手头没多少钱了。"（"没多少钱"用 **don't** 起头说）
　③ "这个小镇晚上没什么可做的。"（"没什么可做的"用 **there isn't** 起头说）
　　★ 目标形式（教练看，⛔ 不进发题稿）：① don't know much about it ② don't have much money ③ there isn't much to do

**成员出题账**
① don't know much about it ｜ 08-21 ❌（首犯 only know little）· 08-23 ✅ · 09-11 ✅
② don't have much money ｜ 08-23 ✅（当时题面是"我最近没什么时间。"，09-05 因与 #271 撞车换题面）· 09-11 ✅
③ there isn't much to do ｜ 08-23 ✅ · 09-11 ✅

- 2026-08-21 新建 · **她主动提出**（§2③）· 加练新题（bank:414）·
  `If people **only know little** about the product, …` → If people **don't know much** about it, …
  ⛔ **教练犯规·漏错**：教练当场按 08-20 的先例（`only few` 那次）判"不判"，
    她当场指出**这次不是 few/little 的问题，是整个说法生硬** ⇒ 判罚恢复，建条目
- 2026-08-23 ✅ 付息日 a 段 · **合并条 3 句整组首测，考点 3/3**（§3.2c）：
  ① `we don't know much about that brand.` ② `I don't have much time recently.` ③ `there isn't much to do there.`
  ⇒ **她当场指定毕业**（"这条毕业"）
  ⚠️ ② 的 `recently` 配一般现在时不搭 —— **recently／lately／so far 这一族默认拉完成时**
    （I **haven't had** much time recently.）；想留现在时就换成 these days／at the moment
    ⇒ 这一层不在本条考点里，**新建 #271**（从 🎓#90 摘出），不算本条头上
- 2026-09-05 📝 题面整改 · 付息日 c 段（§6.5 第 8 项 · 与 #271 题面逐字撞车）
  本条 ② 与 #271 ① **逐字同一句中文**："我最近没什么时间。"
  两条考位完全不同：本条考"说少一律走否定 ＋ much"（don't have much time）；
  #271 考"recently 把时态拉成完成时"（I haven't had much time recently）。
  同一句中文被两个号考 ⇒ 先答哪一条就污染另一条。
  ⇒ **本条 ② 换成 "我没什么时间陪孩子。"**（去掉"最近"这个时态触发词），#271 ① 原样保留。
  ★ 互斥关系写死：**带"最近/这阵子" ⇒ #271（时态）；不带时间副词 ⇒ 本条（much/any）。**
  ★ 合并条成员数不变（仍 3 句），`prompts --verify` 照常。
- 2026-09-11 ✅ 复检 · 付息日 a2 第 4 组 · 合并条 3 句整组出，3/3 全中 · `People don't know much about this brand.` ／ `I don't have much money.` ／ `There isn't much to do there.`
  —— 三句全是否定 ＋ much；本场新补的 ⛔ well／little 没被碰
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 去负向排除）
  三个成员各换新场景，只留正向点名（don't／there isn't 起头），去掉"⛔ well／little"
- 备注 ⚠️ **边界写死，防止教练再判反**（08-20／08-21 两次裁决方向相反，必须分清）：
```
`only few people are really interested`（08-20 她的句子）
   ＝ few 作**主语限定词**，"几乎没有人"是 few 的本职工作 ⇒ **成立，不判**（她 08-20 裁决）
`only know little about it`（08-21 她的句子）
   ＝ 用 little 表"知道得少"，这个意思口语一律走 **don't know much** ⇒ **判，建条目**（她 08-21 裁决）
一句话分辨：**few/little 修饰名词当主语 → 正常；用来说"知道得少/有得少" → 换成否定 ＋ much**
```

### 270 · advice 的量词：a lot of／loads of／some advice（不用 many advice；一条建议 ＝ a piece of advice）
类型 搭配 ｜ 新建 2026-08-23（**从 #261 摘出**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-25** ｜ 题型 整句

**问题是什么**
**advice 的量词**：a lot of／loads of／some advice（⛔ 不用 many advice；一条建议 ＝ **a piece of advice**）。
判据：advice 不可数 ⇒ 量词只能用
```
✅ a lot of advice ／ loads of advice ／ plenty of advice ／ much advice ／ some advice ／ a bit of advice
✗ many advice ／ a few advices ／ an advice ／ three advices
"一条建议" ＝ **a piece of advice**
同样吃 a piece of 的：a piece of news／information／furniture／equipment／research／music
```
★ 判据一句话：**中文"很多建议"直接映射成 many suggestions 是对的**，
但一旦换成 advice 这个词，**量词必须跟着换** —— 错不在"知不知道 advice 不可数"，在"换词时量词没跟着换"。
★ 与母条 **#261**（这一小撮抽象名词不可数）的分工：#261 管"**不加 -s**"那一半（她那句 -s 就没加），
　本条管**量词选哪个**（many vs a lot of）⇒ 同一条可数性规则的另一半，按 §3.2c③ 摘出。
★ 与 🎓**#115**（a couple of ＝ 两个；"几个"用 a few）的分工：那条的对象是**可数**名词 ⇒ 与本条无关。

**怎么发现的**
2026-08-23 新建 · 付息日 a 段 · **#261 七句整组里唯一掉的一句** · 她写 `he gave me **many** advice.`
（→ a lot of advice）。⚠️ **-s 那一半她是对的**（没写 advices）；掉的是**量词** —— many 只配可数名词。
★ **从 #261 摘出**（§3.2c ③：合并条里有顽固成员就单独摘出来新建，老的毕业）——
　#261 已于同日按她指定毕业，本条接着走自己的连击。
判重（当天新建复核，§4④1b）：
　① 目标英文形式 ＝ `a lot of advice`／`a piece of advice`
　② grep "advice"／"a piece of"／"many " 全库（含已毕业）→ 命中 **#261**（本条的母条）
　　 ＋ **🎓#115**（a couple of ＝ 两个；"几个"用 a few）
　③ 逐条读：**#261** 管"这一小撮抽象名词**不加 -s**"—— 她今天那句 -s 就没加，母条那一半是对的；
　　 本条管**量词选哪个**（many vs a lot of）⇒ 是同一条可数性规则的**另一半**，
　　 而母条已毕业 ⇒ 按 §3.2c ③ 摘出成立，不是重号。
　　 **🎓#115** 管"几个"该用 a few 还是 a couple of，对象是**可数**名词 ⇒ 与本条无关
　⇒ 保留新建。

**我错在哪**
她的：`he gave me **many** advice.`　　正确：`he gave me **a lot of** advice.`（一条 ＝ `a piece of advice`）
找法：把"建议"换成 advice 这个词之后，回头看前面那个量词 —— **many 还站在那儿吗？**
站着 ⇒ 换成 a lot of／some／a bit of。

**题面**
"出国前朋友们给了我很多建议。"（"建议"用 **advice** 说） ／ "我就给你一条建议：先别辞职。"（"建议"用 **advice** 说）

- 2026-08-23 新建 · 付息日 a 段 · #261 七句整组里唯一掉的一句 · `he gave me **many** advice.`
  → a lot of advice
  ⚠️ **-s 那一半她是对的**（没写 advices）；掉的是**量词** —— many 只配可数名词
- 2026-08-24 ✅ 复习第1组 · 2 句整组 · ① `he give me a lot of advice.` ② `I give you a piece of advice.`
  ——**本条考点两句都对**（a lot of advice ／ a piece of advice，没出现 many，没加 -s）
  ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ⚪ ① `he give` → `he gave`：中文"给**了**"的过去标记没落到动词上 ⇒ 挂 #12（形态类），
     按 §3.4⑤ 中译英复习里**只做记号**，#12 状态行不动
  ⚠️ ② `I give you a piece of advice.` 语法无错但英语不这么起句（"现在这就给"要 `Let me …`）
     ⇒ **新建 #291**，本条不受影响
- 2026-08-25 ✅ 复习第1组 · 2 句整组（§3.2c 多句覆盖）· ① `he gave me a lot of advice.`
  ② `I have just one piece of advice for you.`
  ——**本条考点两句都对**：① a lot of（不是 many）、advice 没加 -s；② 量词块 `one piece of advice` 在位
  ⇒ **连对 1 → 2 ⇒ 毕业**
  ★ ② 她答的是 `one piece of`，题面点名的是 `a piece of` —— **同一个量词块**，考点位置一字不差 ⇒ 记 ✅，题面不改
  ★ ① 昨天写的是 `he **give** me…`，今天 `gave` 对了 ⇒ 只做正向留痕；
    按 §3.4② 形态类只在自由产出里判档位，**#12 状态行不动**（与 08-24 那次 ⚪ 对称）
  ★ 教练自审留痕：想把 ② 标 ⚠️ 换 `I've only got one piece of advice for you.`，
    造母语句推翻自己 —— `I have just one piece of advice for you.` 本身就是母语固定说法 ⇒ 档位不成立，未标
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 4 组（打包串里，她原话："其他的直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 3 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"⛔ many／一个量词块"，两句只点名 advice —— "很多"配什么量词、"一条"怎么说留给她（她掉过的是 many advice）


### 271 · recently／lately／so far 这一族默认拉完成时（要用一般现在时就换成 these days）
类型 语法 ｜ **合并条·出题多句覆盖**（§3.2c）｜ 新建 2026-08-23
状态 连对3 连错0 上次2026-09-11 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-25** ｜ 题型 整句

**问题是什么**
**recently ／ lately ／ so far** 这一族默认**拉完成时**（要用一般现在时就换成 **these days**）。
判据：
```
recently ／ lately ／ so far ／ up to now ＝ "**到现在为止的一段**" ⇒ **拉完成时**
   ✅ I haven't had much time recently.      ✅ Things have got busier lately.
   ✅ We've done three so far.                ✅ It hasn't rained up to now.
想用一般现在时 ⇒ 换成**指现在这个阶段**的副词：
   these days ／ at the moment ／ right now ／ nowadays
   ✅ I don't have much time these days.
★ 判据一句话：**这个副词说的是"一段"还是"此刻"？** 一段 → 完成时；此刻 → 现在时
★ 例外（不用改）：recently ＋ **过去时**说一个具体的点也成立 —— I saw him recently.（那次见面是个点）
```
★ 与 🎓**#90** 的分工写死（见下方备注）：**#90 ＝ for/since · ever/never/before · just/already/yet**
　｜ **本条 ＝ recently／lately／so far／up to now**。两条题面互斥，各走各的连击。
★ 与 **#259**（have 后面用过去分词）的分工：#259 管 have 后面动词**变什么形**（形态），
　本条管"**要不要用完成时**" ⇒ 不同层。
★ 与 **#269** 的分工（互斥写死，2026-09-05 定）：**带"最近/这阵子" ⇒ 本条（时态）；
　不带时间副词 ⇒ #269（否定 ＋ much）**。

**怎么发现的**
2026-08-23 新建 · 付息日 a 段 · 复习 #269 句里 · 她写 `I don't have much time **recently**.`
（→ I **haven't had** much time recently.）—— 副词是"一段"，动词却停在一般现在时。
★ **从 🎓#90 摘出**（§3.2c ③：合并条里冒出没覆盖到的成员就单独摘出来，老的不动）
判重（当天新建复核，§4④1b）：
　① 目标英文形式 ＝ `haven't had much time recently`（recently ⇒ 完成时）
　② grep "完成时"／"recently"／"lately"／"these days" 全库（含已毕业）→
　　 命中 **🎓#90**（完成时的三个触发：for/since · ever/never/before · just/already/yet）
　　 · #259（have 后面用过去分词）· 🎓#130（can vs be able to）
　③ 逐条读：**#90** 列的是"**哪些词触发完成时**"—— recently 是同一条规则的**第四组成员，
　　 但它从来没被写进 #90**。按 §3.2c ③ 摘出成新条；**#90 已毕业、连对3，不动、不回潮**
　　（她不能为一条从没写进条目里的成员被判退步）。
　　 **#259** 管 have 后面动词**变什么形**（形态），不是"要不要用完成时" ⇒ 不同层。
　　 **🎓#130** 管 can／be able to 的选择 ⇒ 无关
　⇒ 保留新建。

**我错在哪**
她的：`I don't have much time **recently**.`　　正确：`I **haven't had** much time recently.`
找法：句子里蹦出 recently／lately／so far 时，回头看动词 —— **have/has ＋ 过去分词 在不在？**
不在 ⇒ 要么把动词拉成完成时，要么把副词换成 these days。

**题面**
★ 2 句，一句测"副词拉完成时"、一句测"换副词保现在时"
　① **点名**："我最近没什么时间。"（用 **recently** 说）
　② **点名**："这阵子东西贵了不少。"（用 **lately** 说）
　　★ 目标形式（教练看，⛔ 不进发题稿）：① I haven't had much time recently. ② Things have got a lot pricier lately.

**成员出题账**
① recently ｜ 08-23 ❌（首犯）· 08-24 ✅ · 08-25 ✅ · 09-11 ✅
② lately ｜ 08-24 ✅ · 08-25 ✅ · 09-11 ✅
★ 题面外的两次**自发命中**（不出题、只留痕）：08-25 `over the past year`（拉完成时）·
　08-26 `These days he's doing really well.`（判据的另一半，走现在时）⇒ 她调的是判据不是那几个词。

- 2026-08-23 新建 · 付息日 a 段 · 复习#269 句里 · `I don't have much time **recently**.`
  → I **haven't had** much time recently.
- 2026-08-24 ✅ 复习第1组 · **合并条 2 句整组首测，2/2 全对**（§3.2c）：
  ① `I haven't had much time recently.`（与目标形式一字不差）
  ② `Things have become a lot more expensive lately.`
  ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ★ ② 条目预期是 `have got a lot pricier`，她答的 `have become a lot more expensive`
    **完全合法且正中考点**（现在完成时 ＋ lately）⇒ 按 §3.3 记 ✅，不记 ◎
  ★ 教练自审：想把 `have become` 标 ⚠️ 降级成 have got／have gone up。试造母语句推翻自己 ——
    `Things have become a lot more expensive lately.` 母语者说得毫无问题、不书面 ⇒ 档位不成立，
    写「无更好版本」，不标
- 2026-08-25 ✅ 复习第1组 · **合并条 2 句整组，2/2 全对**（§3.2c）：
  ① `I haven't had much time recently.`　② `Things have become a lot more expensive lately.`
  ⇒ **连对 1 → 2 ⇒ 毕业**
  ★ 教练自审留痕（§7 四问②）：② 的条目预期是 `have got a lot pricier`；08-24 已就
    `have become a lot more expensive` 自审过一次并判**档位不成立**（母语者照说）。
    今天无任何新证据 ⇒ **不翻案**，照记 ✅ ＋ 无更好版本
- 2026-08-25 ✅ **自发命中**（毕业当天下午，本条未被出题，不改状态）· 加练新题 bank:1043 P2 ·
  `**Over the past year**, I've bought him a lot of Lego sets.`
  ——`over the past year` ＝ "到现在为止的一段" ⇒ 拉现在完成时，她自己拉对了
  ★★ **一次真迁移**：本条今天上午刚毕业（中译英两句全对），下午在**没有中文题面**的自由产出里
     换了一个从没测过的成员（over the past year，不在本条的四个成员里）照样拉对
     ⇒ 说明她调的是**判据**（一段 vs 此刻），不是背下来的那四个词
- 2026-08-26 ✅ **自发命中·第二次真迁移**（本条未被出题，不改已毕业状态）· 自由产出（新题 bank:244 P2）·
  `**These days** he's doing really well.`
  ——本条判据的**另一半**（"要用一般现在时就换成 these days，别用 recently 拉完成时"）
  这次是正向用：想说"现在这阵子"⇒ 直接上 these days ＋ 现在进行，没去写 recently he is…
  ★ 两天两次、两个不同成员、两个方向（08-25 over the past year 拉完成时 ／
    今天 these days 走现在时）⇒ 判据本身已经在手，不是背词
- 2026-09-11 ✅ 复检 · 付息日 a2 第 7 组 · 合并条 2 句：① `I haven't had much time recently.` ② `Things have got to a lot more expensive lately.` —— 两句都拉出完成时，考点 2/2
  ⚠️ ② `have got **to** a lot more expensive` 多了 to（get ＋ 形容词中间⛔不加 to），一次性滑手，⛔ 不落本条、不建号
- 备注 与 🎓#90 的分工写死：**#90 ＝ for/since · ever/never/before · just/already/yet**
  ｜ **本条 ＝ recently／lately／so far／up to now**。两条题面互斥，各走各的连击

### 272 · litter 不可数（"乱扔垃圾" ＝ littering／dropping litter，不说 litters）
类型 语法 ｜ **从 #25 拆出 2026-08-23**
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-27**（连对2）｜ 题型 整句

**问题是什么**
**litter 不可数**（"乱扔垃圾" ＝ **littering**／**dropping litter**，⛔ 不说 litters）。
判据：litter ＝ 地上的垃圾（不可数）｜ **litter 也能当动词**（乱扔）⇒ littering
```
✅ Don't drop litter.  ✅ a fine for littering  ✅ There's litter everywhere.
✗ litters ／ ✗ a litter（a litter ＝ 一窝小动物，完全另一个意思）
★ 同族：rubbish／trash／garbage 也都不可数
```
★ 与 **#261**（抽象名词不可数：action／feedback／…）的分工：那条管**抽象名词**那一小撮，
　本条管 **litter 这个具体的词**（且它还有动词用法）⇒ 按 §3.2 词汇按具体词一条一号，不并。
★ 与 **#273**（fine sb FOR doing）的分工：那是"罚"那一格的考点 ⇒ 本条题面已去掉"罚"字，两条不互相泄题。

**怎么发现的**
2026-08-17 ❌ ＝ #25 首次进流那次，**三块都没出来**（旧捆绑条时期，触发原话未存）；
2026-08-19 在 `it is no use fining people for **littering**` 一句里第一次产出成功。
★ 拆号理由（§3.1 一条＝一个考点）：#25 原来装了**三条不同规则** ——
　litter 不可数 ／ fine sb FOR doing ／ It's no use doing。三块里只有第三块被反复验过，
　前两块各只验过一次（08-19 那一句里），却跟着第三块一起毕业了 ⇒ 拆出来各走各的连击。
判重：本条是**从 #25 拆出**（2026-08-23），不是新考点 ⇒ 走拆号程序、不走判重三步；
与 #261 的分工见上（抽象名词一小撮 vs litter 这个具体词）。

**我错在哪**
她的：08-17 那次 litter 这一块**根本没产出**（原话未存）；目标形式一直是动名词 littering。
正确：`littering` ／ `drop litter`（⛔ litters ／ ⛔ a litter）
找法：说"垃圾"之前问一句 —— 这个词能数吗？litter／rubbish／trash 都不能 ⇒ ⛔ 不加 -s、⛔ 不加 a。

**题面**
"公园里到处都是垃圾，可还是有人在乱扔。"（"垃圾"和"乱扔"都用 **litter** 说）
★ ⛔ 题面不带"罚"字 —— 那是 #273（fine sb FOR doing）的考点，两条互不泄题

- 2026-08-17 ❌（＝ #25 首次进流那次，三块都没出来）
- 2026-08-19 ✅ `it is no use fining people for **littering**`——litter 用作动名词、没加 -s，本块达成
  ★ 连击**不从 0 起算**：08-11 定"拆号不继承"的理由是"父号一次只测到多个考点中的一个"；
    而 08-19 那一句**逐字含三块**，✅ 对每一块都是真的 ⇒ 继承成立（理由写在这里，可复查）
- 2026-08-27 ✅ 付息日 b 段（题面当天整句改后首测）· `**littering** is a pretty problem around here.`
  ——litter 用作动名词、没加 -s、也没写成 a litter ⇒ **连对 1 → 2，🎓 毕业**
  ⚪ 同句 `a pretty problem` 缺一个形容词（应为 a pretty **serious** problem）——
    **打漏，不记 ❌、不建号**：pretty 是程度副词，后面必须挂形容词；
    **同一组第 10 题她自己写了 `it's pretty common`**（同一个词、同一个用法、相隔十分钟）
    ⇒ 决定性反证。已给她反悔通道（"若你觉得是真不会，说一声我补号"）
    ⚠️ 教练自审留痕：这不是"形态"（不是词尾差几个字母）⇒ **不吃 §3.4⑤b 的豁免**，
      是按 §2.1 的**边界精神**（她脑子里调的东西对不对）判的打漏，口径写在这里备查
    ★ 顺带：`a pretty problem` 在英语里另有其义（麻烦事，偏古旧/反讽），会被听岔
  ★ 今天改题面的收益：旧题面"乱扔垃圾**罚**得挺重"会把她逼向 `fined for littering`，
    那是 #273 的考点 ⇒ 两条互相泄题。改后本条独立命中
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `littering` —— litter 当动词，⛔ 没写成 litters
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句（类型 语法 ⛔ 不许标词组）
  考点是 litter 加不加 -s ＝ 靠句子现形；一句里放名词和动词两个用法；换成公园场景，照旧不带"罚"字（与 #273 互斥）
- 备注 与 #261（抽象名词不可数：action／feedback／…）的分工：那条管**抽象名词**那一小撮，
  本条管 **litter 这个具体的词**（且它还有动词用法）⇒ 按 §3.2 词汇按具体词一条一号，不并

### 273 · fine sb FOR doing sth（罚款的介词是 for，不是 of／on）
类型 搭配 ｜ **从 #25 拆出 2026-08-23**
状态 连对2 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-27 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零。★ 本条 08-23 才从 #25 拆出来，拆出后只被测过两次 ⇒ 基础本来就薄）

**问题是什么**
**fine sb FOR doing sth** —— 罚款的介词是 **for**（为了哪件事罚你）；
⛔ 不是 fine sb **of**（那是 accuse sb of／rob sb of 那一族）、⛔ 不是 fine sb **on**。
整条结构：被罚的人当主语 ⇒ get／be fined ＋ 金额 ＋ for ＋ -ing。
同一格里的邻居（别串）：`for illegal parking`（for ＋ 名词块）与 `for parking illegally`（for ＋ doing）**都对**。
判据：**处罚/责备类动词，"因为什么"一律用 for**
```
✅ fine sb **for** doing ／ punish sb **for** doing ／ blame sb **for** doing
   ／ tell sb off **for** doing ／ apologise **for** doing
✅ 被动：He was fined 200 yuan **for** parking illegally.
★ 钱直接跟在动词后面，不带介词：fine sb **£50** for…（不是 fine sb with £50）
```
★ 与 #272（litter）的分工：08-27 改 #272 题面（去掉"罚"字）之后两条不再互相泄题，本条独立命中。

**怎么发现的**
2026-08-23 从 #25 拆出；最早记录 2026-08-17 ❌（＝ #25 首次进流那次，三块都没出来），原始触发原话未存。
2026-08-19 ✅ `it is no use fining people **for** littering`——介词 for 对，本块达成。
2026-08-27 付息日 b 段 ✅ `They were fined $200 **for** illegal parking.` ⇒ 连对 1 → 2，毕业。
2026-09-11 付息日 a2 第 2 组复检：她答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**。

**我错在哪**
她的：答"忘了"（2026-09-11 复检）　　正确：`I got fined two hundred for parking in the wrong place.`
找法：写"因为…被罚款／被责怪"时，中间那个介词一律先填 **for**，再往后挂 -ing 或名词块。

**题面**
"我上周超速，被罚了三百块。"（"被罚"用 **fine** 说）

- 2026-08-17 ❌（＝ #25 首次进流那次，三块都没出来）
- 2026-08-19 ✅ `it is no use fining people **for** littering`——介词 for 对，本块达成
  ★ 连击继承理由同 #272（08-19 那句逐字含三块）
- 2026-08-27 ✅ 付息日 b 段 · `They were fined $200 **for** illegal parking.`
  ——介词 **for** 一字不差（不是 of／on），fined ＋ 金额 ＋ for ＋ 事由的语序也对
  ⇒ **连对 1 → 2，🎓 毕业**
  ★ `for illegal parking`（for ＋ 名词块）与判据里的 `for parking illegally`（for ＋ doing）**都对**
  ★ 结构限定"fine ＋ 一个介词"当场生效：不这么限定，
    `They were fined 200 **because** they parked illegally.` 是合法英语，介词那一格整个测不到
  ★ 今天改 #272 题面（去掉"罚"字）的收益：两条不再互相泄题，本条独立命中
- 2026-09-11 ❌ 复检 · 付息日 a2 第 2 组 · 答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**
  最小改 `I got fined two hundred for parking in the wrong place.`
  ❌ 罚款的介词是 **for**（为了哪件事罚你）：fine sb **for** doing sth；
    ⛔ 不是 fine sb of（那是 accuse sb of／rob sb of 那一族）、⛔ 不是 fine sb on。
  ★ 整条结构：被罚的人当主语 ⇒ get／be fined ＋ 金额 ＋ for ＋ -ing
- 2026-09-12 📝 题面整改：「被罚了两百」→「被罚了款」＋ 给出"乱停车"＝ illegal parking —— 金额和"乱停车"怎么说都是本条考点之外的噪音（§6① 把考点单独摆出来，剩下的全是噪音 ⇒ 去掉）· 全档题面 review
- 2026-09-13 ✅ 学习日 在池第 1 组 · `got fined for illegal parking.`——fined **for**（09-11 掉的就是介词）
- 2026-09-15 ✅ 学习日 在池第 1 组 · `got fined for illegal parking.` → **连对2，毕业**
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"fine ＋ 一个介词"形态描述，只点名 fine，for 留给她；换成超速场景
- 2026-09-30 ✅ 复检 · 付息日 a2 第 3 组 [8] · `He got fined fifty bucks for eating on the subway.`

### 274 · prepare FOR class（备课／备考，介词是 for；prepare sth ＝ 把东西准备好）
类型 搭配 ｜ **从 #41 拆出 2026-08-23**
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-27**（连对2）｜ 题型 整句

**问题是什么**
**prepare FOR class**（备课／备考，介词是 **for**；prepare sth ＝ 把东西准备好）。
判据：**prepare 后面有没有介词，看宾语是"事"还是"东西"**
```
✅ prepare **for** class／for an exam／for the trip　← 为某件事做准备（事）
✅ prepare dinner／prepare a presentation　　　　  ← 把某样东西做出来（东西）
✗ prepare classes（＝ 把课本身做出来，不是备课）
★ 口语更常说：get ready for class ／ plan his lessons
```
★ class 前不加冠词是对的（prepare for class ＝ 为"上课"这件事做准备）。
★ 与母条 **#41** 的分工：#41 剩下的是 time and energy（**并列词序**），本条是 **prepare 的介词搭配** ⇒ 两条规则。
★ 与 **#273**（fine sb FOR doing）撞车提醒：两条的答案介词**都是 for**，⛔ 不许相邻出题（会互相 priming）。

**怎么发现的**
2026-08-17 ❌ ＝ #41 首次进流那次（旧捆绑条时期，触发原话未存）；
2026-08-19 在 `spend more time and energy **preparing for class**` 一句里第一次产出成功（介词 for 对）。
★ 拆号理由：#41 原来装了 time and energy（**并列词序**）＋ prepare for class（**介词搭配**）
　两条不同规则；08-20 那次只验了前半，后半跟着毕业了 ⇒ 拆出来各走各的连击。
判重：本条是**从 #41 拆出**（2026-08-23），不是新考点 ⇒ 走拆号程序、不走判重三步。

**我错在哪**
她的：08-17 那次 prepare for class 这一块**根本没产出**（原话未存）。
正确：`preparing **for** class`（⛔ prepare classes ＝ 把课本身做出来）
找法：说完 prepare，看后面那个宾语 —— **是"一件事"还是"一样东西"？** 是事 ⇒ 补 for。

**题面**
"考试前一晚她一直在准备，到凌晨一点才睡。"（"准备"用 **prepare** 说）

- 2026-08-17 ❌（＝ #41 首次进流那次）
- 2026-08-19 ✅ `spend more time and energy **preparing for class**`——介词 for 对，本块达成
  ★ 连击继承理由同 #272
- 2026-08-27 ✅ 付息日 b 段（排在第 8 位，离 #273 最远）·
  `he spends two hours every day **preparing for** class.`
  ——介词 **for** 一字不差；外加 `spend ＋ 时间 ＋ doing` 的载体句型也对
  ⇒ **连对 1 → 2，🎓 毕业**
  ★ `class` 前不加冠词是对的（prepare for class ＝ 为"上课"这件事做准备）
  ★ 排位收益：本条与 #273 的答案介词**都是 for**，相邻会互相 priming；隔了 6 题她仍一次给对
    ⇒ 这个 for 是调出来的，不是刚看过的
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `prepare for class` —— 介词 for
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"prepare ＋ 一个介词"形态描述，只点名 prepare，for 留给她；换成考前一晚场景

### 275 · whether 后面要跟【主谓】，不能只跟名词或形容词
类型 结构 ｜ **从 #64 拆出 2026-08-23**
状态 连对3 连错0 上次2026-09-19 ｜ **🎓 已毕业 2026-08-27**（同日两次产出各算一次，§3.3）｜ 题型 整句

**问题是什么**
**whether 后面要跟【主谓】，不能只跟名词或形容词**。
判据：**whether／if 引导的是【从句】，从句必须有自己的主语和谓语**
```
✅ I'm not sure whether **it's worth it**.        ✅ It depends on whether **he turns up**.
✅ whether **or not** it works                   ✅ I'll go whether **you come** or not.
✗ I'm not sure whether worth.  ✗ It depends on whether possible.
★ 想只跟一个词，就别用 whether，改成：I'm not sure **if it's worth it**／**about that**
★ 与 🎓#59（嵌进句子里用陈述语序）配套：whether 从句同样**不倒装**
  ✅ I'm not sure whether **he is** coming.（✗ whether is he coming）
```
★ 与母条 **#64** 的分工：#64 剩下的是 forward or back（**固定词序**），本条是 whether 的**从句结构** ⇒ 两条规则。

**怎么发现的**
本条是 **2026-08-23 从 #64 拆出**的：#64 原来装了 forward or back（**固定词序**）＋ whether 后跟主谓（**从句结构**）
两条不同规则，而 #64 的题面（"谁都动不了，前进也不行后退也不行"）**根本测不到 whether 那一半**
⇒ whether 这块**从未被验过**却跟着毕业了 ⇒ 拆出来从 0 起算。
因此**本条没有首犯记录、触发句未存**；最早记录是 2026-08-27 付息日 b 段第 2 组 [2]
（拆出后第一次被测到）：`I'm not sure whether **it is** worth it.` ✅。
判重：拆号（走 §3.1 一条＝一个考点），不走判重三步。

**我错在哪**
她在本条上**没有留下过错例**（拆出来时这一块从未被验过，原话未存）；08-27 第一次被测就一次到位。
正确：`I'm not sure whether **it is** worth it.`（⛔ whether worth ／ whether possible）
找法：说出 whether 之后问一句 —— **后面跟上主语和动词了吗？** 只有一个词 ⇒ 换成 if it's … 或干脆不用 whether。

**题面**
**点名**："我不确定这样做值不值。"（用 **whether** 说）

- 2026-08-27 ✅ 付息日 b 段第 2 组 [2]（**从 #64 拆出后第一次被测到**）·
  `I'm not sure whether **it is** worth it.`——whether ＋ **主谓**，不是只跟形容词 ⇒ 连对 0 → 1
- 2026-08-27 ✅ **同日第 2 次 · 自发命中**（b 段第 2 组 [5] 的 #280 句里，本条未被出题）·
  `**whether you have help or not** makes a huge difference.`
  ——whether 从句**当整个句子的主语**，且谓语用单数 makes ⇒ 比第 1 次那档更难，也过了
  ⇒ **连对 1 → 2，🎓 毕业**
  ★ 依据：§3.3（她 08-23 定）"同一条同一天被产出多次 ⇒ 每次各记一行、各算一次"
    ＋ §4① 加速通道"自由产出里自发出现就当场记 ✅" —— 本句的 whether 结构**不是题面要求的**
    （题面是"有没有人帮忙差别很大"，她完全可以写 `Having someone to help makes a huge difference.`）
    ⇒ 是她自发选的
  ⚠️ **保留意见（教练主动写出来，不藏）**：第 1 次就在三题之前，**priming 真实存在**；
    拿一个被 priming 过的重复去凑毕业，证据强度不如隔天独立测。
    安全网 ＝ 回潮（毕业后再犯就掉回池子）。**她若认为不该算，当场撤销即可**
- 2026-08-27 ✅ **同日第 3 次 · 自发命中**（毕业当天，b 段第 3 组 #288 句里，本条未被出题，
  不改已毕业状态）· `you naturally start thinking **whether it's really necessary**.`
  ——whether 后面跟**主谓**（it's），本条规则用对
  ★ 这一次的价值高于前两次：**题面完全没提 whether**（#288 的点名只说 start asking whether，
    重点在 asking），她是在写别的考点时顺手用对的 ⇒ 三次里最接近"无提示"的一次
- 2026-08-28 ⚪ **观察行（不改已毕业状态、不算命中）** · 复习第2组 #280 句里 ·
  `**Whether you have help or not** makes a huge different.`
  ——whether ＋ 主谓、从句当主语，结构对；但**与 08-27 是同一道题面**（#280 的"有没有人帮忙差别很大"）
  ⇒ 属**重复不属自发**，按 §4① 加速通道的边界（她 08-27 认可的那条）只记 ⚪，不当第 4 次命中
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 5 组（她原话："3. 直接过" —— 答卷上第二个"3."，按位置 ＝ 第 4 题）
- 2026-09-19 ✅ 自发命中 · 付息日 d 段重答 R11（P3 · 自由产出）· `whether you have time`——whether ＋ 完整主谓


### 276 · for ages ／ in ages ＝ "很久"（for long 只用在"没持续多久"里）
类型 词汇 ｜ **从 #166 拆出 2026-08-23**
状态 连对2 连错0 上次2026-09-22 ｜ 题型 整句 ｜ **回潮 2026-09-05**（08-21 毕业 → 09-05 复检里**同日两次产出**：不点名那次写成 `for long` ❌ ⇒ 撤销毕业、连对清零；点名那次写出 `in ages` ✅ ⇒ 连对回到 1。★ `for long` 这个错 08-19 已犯过一次，今天是**第三次**）｜ **🎓 已毕业 2026-09-07**（连对2 ＝ 09-05 ＋ 09-07；09-05 回潮后第二次毕业）

**问题是什么**
**for ages ／ in ages** ＝ "很久"（**for long** 只用在"没持续多久"里）。
判据：说"很久"这个**量** ⇒ for ages／in ages／for a long time
```
✅ I haven't seen him for ages. ／ in ages.    ✅ It's been ages.
✗ for long —— 它只活在**否定句说"没持续多久"**里：I didn't stay for long.
★ `hadn't met for long` 意思是反的（＝ 没认识多久），不是"很久没见"
```
★ 与母条 **#166** 的分工：#166 管 see／meet／meet up **选哪个动词**，本条管 **"很久"这个量**
　⇒ 两条不同规则，将来任一半掉了只有那一半回潮。

**怎么发现的**
2026-08-17 ❌ ＝ #166 首次进流那次（旧捆绑条时期，触发原话未存）；
2026-08-19 **同一个错第二次**：她写 `I haven't seen him **for long**`（该 for ages／in ages）。
★ 拆号理由：#166 原来装了 see／meet／meet up 的**分工**（选哪个动词）＋ for ages（**"很久"的量**）
　两条不同规则。两块在 08-20 与 08-21 的同一句里都产出过两次 ⇒ **拆完两条都直接 🎓，零池成本**；
　拆的意义在于：将来任一半掉了，只有那一半回潮，不拖累另一半。
★ 2026-09-05 回潮那次是**本日最值钱的一条数据**：同一分钟里，不点名的那句写成 `for long` ❌、
　点了名"用 ages 那个词说"的那句写出 `in ages` ✅ ⇒ 缺口不在"会不会"，在**检索触发**。
判重：拆号（走 §3.1 一条＝一个考点），不走判重三步。

**我错在哪**
她的：`I haven't seen him **for long**.`（08-19 ／ 09-05 两次同一个错）
正确：`I haven't seen him **in ages**.` ／ `for ages`
找法：中文"很久没…"一出现就问 —— 我说的是"**没持续多久**"吗？不是 ⇒ 用 **ages**，⛔ 别写 for long。

**题面**
**点名**："我跟他好久没见了。"（"好久"用 ages 那个词说）

- 2026-08-17 ❌（＝ #166 首次进流那次）
- 2026-08-19 ❌ **同一个错第二次**：`I haven't seen him **for long**`（该 for ages／in ages）
- 2026-08-20 ✅ `we haven't seen each other **for ages**.`
- 2026-08-21 ✅ `We haven't seen each other **in ages**.` → 连对2，毕业
- 2026-09-05 ❌ 复检组 · 第 4 组（打包 · 第 3 句的顺带产出）· **回潮**
  `I haven't seen him **for long**.` → I haven't seen him **in ages**.
  ❌ for long 只用在"没持续多久"里（It didn't last for long.）；说"很久没…"一律 for ages ／ in ages。
  ★★★ **本日最值钱的一条数据 —— 同一个块、同一分钟、一次错一次对**：
    这一次（打包第 3 句）题面**没点名** ⇒ 写成 for long ❌；
    下一次（打包第 5 句，本条自己的题面）**点了名**"用 ages 那个词说" ⇒ 写出 in ages ✅。
    ⇒ 与本日 #118（only 那一层）**完全同型**：**点名就出得来，不点名就丢**
      ⇒ 缺口不在"会不会"，在**检索触发**（中文那个词没有直接指向英文块）。
- 2026-09-05 ✅ 复检组 · 第 4 组（打包 · 第 5 句 · 本条自己的题面，已点名）
  `We haven't met **in ages**.` —— 块调出来了。
  ｜ ⚠️ 同句 `met` 按 #166 的分工更准的是 seen each other（口语里 met in ages 也有人说）⇒ 只给更准版，⛔ 不记 ❌
  ★ §3.3「同一天同一条被产出多次 ⇒ 每次各记一行、各算一次」：本条今天两行，先 ❌ 后 ✅，⛔ 不挑"以谁为准"。
- 2026-09-07 ✅ 复习 · 在池第 1 组 · `I haven't seen him for ages / in ages` ⇒ 连对 2，**毕业**
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 7 组（她原话："5-9 直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组

### 277 · 双面立论句型：It's mainly about A while B-ing（一句话同时给"要做的"和"要放的"）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）
　　※ 状态与日志见下（2026-08-27 首测通过）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
双面立论句型：**It's mainly about A while B-ing**（一句话同时给"要做的"和"要放的"）。
骨架：`(Well,) I'd say it's mainly about ＋【动名词/名词 A】while ＋【动名词 B】.`
用途 ＝ P3 开场**一句话立两面**（详例见下方备注）。
判据一句话：这道题要说"既要…又要…／两面都有"吗？要 ⇒ 上这个框架，两个空都填**动名词**。
★ while 后面只能跟 **-ing 或形容词**，不能跟完整句（跟完整句要用 whereas／but）。
★ 与 🎓**#58**（it mainly comes down to）／🎓**#207**（I'd say ＋"主要就是…"四条路径）的分工：
　那两条管的是**起手块**（"主要就是…"这四个字用哪个说法）；本条管 **while 把第二面挂上去**这个**整句结构**
　⇒ 目标形式不同（一个是短语，一个是双面句型）；**题面互斥**：#207 的题面是**单面**，本条题面必须是**两面**的。
★ 与 **#283**（收尾句型）天然配套：开头立两面 → 收尾把两面排成先后 ⇒ 首尾呼应。
★ 与 **#278**（give sb room）的分工：那条考"空间"这个词 ⇒ 本条题面已于 08-27 去掉"空间"，两条互不泄题。

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第二版 · 她自己写出
`Well, I'd say it's mainly about building standard habits while giving kids room to manage themselves.`
★ 她的原话："这一整句子的句型…新建条目"（指 `Well, I'd say it's mainly about building good habits while giving kids room to manage themselves.`）
判重（当天新建复核）：① 目标形式 ＝ `it's mainly about A while B-ing`（**整句双面结构**）
② grep "mainly about"／"comes down to"／"I'd say" 全库（含已毕业）→ 命中 **🎓#58**（it mainly comes down to）
　 · **🎓#207**（I'd say ＋"主要就是…"四条路径）
③ 逐条读：#58 和 #207 管的都是**起手块**（"主要就是…"这四个字用哪个说法）；
　 本条管的是 **while 把第二面挂上去**这个**整句结构** ⇒ 目标形式不同（一个是短语，一个是双面句型）
　 ⇒ 保留新建。**题面互斥**：#207 的题面"我觉得主要就是钱的问题"是**单面**；本条题面必须是**两面**的。

**我错在哪**
她这次没有错（这句型是她自己在 R1 第二版里产出来的），建号理由是 §2③ **她点名要学** ——
她要的是把这**一整句的句型**固定下来，以后 P3 开场能直接调。
找法：P3 开口前先问一句 —— 这题有没有两面？有 ⇒ `it's mainly about …**ing** while …**ing**` 一句话把两面都摆上。

**题面**
**点名**："关键是既要把规矩立起来，又要让他们自己去管。"（用 `it's mainly about … while …` **一句话**说完）
★ 题面 2026-08-27 微改（§6.5 审核项 8 题面撞车）：原题面后半"给孩子自己管的**空间**"正是 **#278（give sb room）的考点** —— 她答本条时会顺手把 room 写出来。改成"让他们自己去管"（letting them manage it themselves），只留本条的句型这一格

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第二版 ·
  `Well, I'd say it's mainly about building standard habits while giving kids room to manage themselves.`
- 2026-08-27 ✅ 付息日 b 段（题面当天微改后**首测**）·
  `It's mainly about setting up the rules while letting them mange themselves.`
  ——三格全中：框架 ／ about 后面用**动名词**（setting）／ while 后面也用**动名词**（letting）
  ⇒ **连对 0 → 1（差一次毕业）**（`mange` 是打字，§2.1 不算错）
  ★ 教练自审留痕：`the rules` 差点被标（想换成泛指的 rules）——试造母语句推翻自己：
    `It's mainly about setting up the rules and then getting out of the way.` 母语者照说
    ⇒ **假错，未判**
  ★ 改题面的收益：旧题面后半含 #278 的考点（"空间"→room），会泄题；改后她给的是
    `letting them manage themselves`，两条互不干扰
- 2026-08-28 ✅ 复习第2组 · `It's mainly about setting up rules while letting them manage themselves.`
  ——整句框架一字不差（it's mainly about ＋ -ing ／ while ＋ -ing）⇒ 连对2，**毕业**
  ★ 自审留痕：`setting up rules` 曾想判 ⚠️（更常说 setting rules），试造母语句
    `We set up a few rules about screen time.` 成立 ⇒ 不判
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `It's mainly about setting clear rules while giving them the room to self-manage.` —— it's mainly about … while … 一句话，两头都在
  ⚪ the room → room（冠词，形态类 #63 只记号）；⚠️ 顺带 self-manage → manage themselves（不建条目）
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组

- 备注 骨架与用法：
```
(Well,) I'd say it's mainly about ＋【动名词/名词 A】while ＋【动名词 B】.
用途   P3 开场**一句话立两面** —— 听者第一句就知道你要讲哪两块，后面几点直接对应
✅ It's mainly about building good habits while giving kids room to manage themselves.
✅ It's mainly about keeping costs down while not cutting quality.
✅ It's mainly about staying flexible while still having a plan.
★ while 后面只能跟 **-ing 或形容词**，不能跟完整句（跟完整句要用 whereas／but）
★ 天然和 #283（收尾句型）配套：开头立两面 → 收尾把两面排成先后 ⇒ 首尾呼应
```

### 278 · give sb room to do sth（给某人自己来的空间）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
**give sb room to do sth**（给某人自己来的空间）。
判据：
```
✅ give kids room to manage themselves ／ room to grow ／ room to make mistakes
✅ 同族：leave room for … ／ there's room for improvement ／ no room for error
★ room 在这个意思上**不可数、不带 a**（✗ a room to grow —— a room 是"一个房间"，完全另一个意思）
★ 与 space 的分工：give them space 偏"别打扰他"；give them room 偏"让他自己发挥" —— 说成长用 room
```
判据一句话：说的是"让他自己去长／自己去做"吗？是 ⇒ **room**（不带 a）＋ to do。
★ 与 **#277**（It's mainly about A while B-ing）的分工：#277 考整句框架 ⇒ 它的题面已于 08-27 去掉"空间"，
　两条互不泄题。

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第二版 · 她自己写出 `giving kids room to manage themselves`。
判重：grep "room to"／"give …room"／"space to" 全库（含已毕业）→ **零命中** ⇒ 保留新建。

**我错在哪**
她这次没有错（`giving kids room to manage themselves` 是她自己产出的），建号理由是 §2③ **她点名要学**。
找法：想说"给他空间"时先问 —— 是"别打扰他"（space）还是"让他自己发挥"（room）？
是后者 ⇒ **room**，⛔ 前面不加 a。

**题面**
"家长得给孩子留一点自己试错的空间。"（"空间"用 **room** 说）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第二版 · `giving kids room to manage themselves`
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `you should give kids **room to** manage their own time.`
  ——**room**（不是 space）＋ 后面挂不定式 to do ⇒ 一字不差，**连对 0 → 1（差一次毕业）**
  ★ `manage their own time` 是她自己补的（题面只说"自己安排"）—— 落到具体的东西上，加分
  ★ 今天改 #277 题面的收益：#277 旧题面里带着"空间"两个字，会把本条答案先泄出去；改后独立命中
- 2026-08-28 ✅ 复习第2组 · `you need to give kids room to manage their own time.`
  ——room 不带冠词，正是这个块的形状 ⇒ 连对2，**毕业**
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 4 组（打包串里，她原话："其他的直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"r- 开头 ＋ ⛔ space／freedom"猜谜写法，她点名要学的块 ⇒ 点名 room，a／to do 怎么挂留给她

### 279 · get a feel for sth（慢慢摸出感觉／找到手感）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-28 毕业 → 09-11 复检写成 `get a feel of time`，介词滑到 of，撤销毕业、连对清零）

**问题是什么**
**get a feel for sth** ＝ 慢慢摸出感觉／摸出门道（对某个**领域**生出直觉）。
判据一句话：**a feel 配 for、the feel 配 of**，两个块各自成立，⛔ 不许交叉。
判据：
```
✅ get a feel for time ／ for the place ／ for how it works ／ for the rhythm of it
★ 固定带 **a**：get **a** feel for（✗ get feel for ／ ✗ get the feel for）
★★ **补全（2026-08-27）：`get the feel of sth` 是【另一个成立的块】，不是错路** ——
   两个都真、分工不同，别混也别互判：
     get **a** feel **for** sth  ＝ 摸出感觉／摸出门道（对某个**领域**生出直觉）
                                  get a feel for time／for the market／for how it works
     get **the** feel **of** sth ＝ 上手／熟悉手感（适应某个**具体东西**怎么使）
                                  get the feel of the car／of the new keyboard
   ⛔ 真正的错路只有一条：**the ＋ for 混搭**（get the feel for）
★ 用途：说"不是学会某个知识，是慢慢摸出感觉" —— 比 learn／understand 准得多
★ 同族分工：get the hang of sth（掌握窍门，偏操作）· get used to sth（习惯，偏适应）
             · get a feel for sth（摸出感觉，偏体感）
```

**怎么发现的**
2026-08-23 新建（**她当场指定**，§2③）· d 段重答 R1 第二版 · 她的原话 `kids actually get a feel for time`
　★ 这个说法**比第一版的 `internalize time management` 又口语又准** —— 她自己换出来的。
判重：grep "get a feel"／"feel for" 全库（含已毕业）→ **零命中** ⇒ 保留新建。
2026-09-11 付息日 a2 第 5 组复检：她写 `gradually get a feel of time`，介词滑到 of ⇒ **回潮**。

**我错在哪**
她的：`gradually get a feel of time`　　正确：`gradually get a feel **for** time`
找法：写完 feel 这个块，回头把冠词和介词一起看 —— **a feel for** ／ **the feel of**，配错一半就是错。

**题面**
"做了几个月销售，我慢慢摸出了客户心理的门道。"（"摸出门道"用 **feel** 说）
　　★ 宾语是抽象领域（客户心理）⇒ 只有 a feel for 通；具体物件才走 the feel of —— 题面⛔不用具体物件

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第二版 · `kids actually get a feel for time`
  ★ 这个说法**比第一版的 `internalize time management` 又口语又准** —— 她自己换出来的
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `you'll get **the feel of** it after practicing a few times.`
  ⇒ **合法但不是条目预期**，按 §3.3 记 **✅ ＋ 当场改题面** ⇒ 连对 0 → 1（差一次毕业）
  ★★ 教练自审留痕：**差点判 ❌**（判据里写着"固定带 a"）。试造母语句推翻自己 ——
    `Give it a few tries and you'll get the feel of it.` 母语者照说 ⇒ **假错，未判**。
    关键区分：判据禁的是 `get **the** feel **for**`（the ＋ for 混搭），
    她写的是 `get **the** feel **of**`，是**另一个成立的固定块** ⇒ 不在禁区里
  ⇒ 判据当天写漏了这条合法路，**今天补进判据**（补事实，不是改规则）
- 2026-08-28 ✅ 复习第2组 · `With a bit of practice, kids will gradually get a feel for time.`
  ——`get a feel for time` 一字不差（抽象宾语那一档也过了）⇒ 连对2，**毕业**
- 2026-09-11 ❌ 复检 · 付息日 a2 第 5 组 · `gradually get a feel of time` ⇒ **回潮**
  最小改 `gradually get a feel for time`
  ❌ get a feel **for** sth（for 是这个块的固定介词）；⛔ of 属于另一个块 get **the** feel **of** sth（带 the）——
    a feel 配 for、the feel 配 of，两个块不能混。★ 08-23 她自己产出的是 get a feel for time（对的），今天介词滑到 of
- 2026-09-13 ✅ 学习日 在池第 1 组 · `gradually get a feel for time.`——get **a** feel **for**
- 2026-09-15 ✅ 学习日 在池第 1 组 · `gradually get a feel for time.` —— get a feel FOR → **连对2，毕业**
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 feel，a／for 留给她（她掉过的是 a feel of）；宾语用抽象领域（客户心理）保证只有 a feel for 通
- 2026-09-30 ✅ 复检 · 付息日 a2 第 3 组 [10] · `I'm slowly getting a feel for the rhythm.`

### 280 · make a huge difference（差别很大／很管用）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-15 ｜ **🎓 已毕业 2026-08-29**（连对2 ＝ 08-27 ＋ 08-29）｜ 题型 整句
　　★★ **2026-08-30 撤销 08-28 的 ❌**（她当天裁定 `makes a huge different` ＝ 手滑，§2.1 拼写不算错）
　　　 ⇒ 08-27 的连对1 没被清零，08-29 那次就已经是连对2 ⇒ **毕业日回填到 2026-08-29**。
　　　 08-30 那次 ✅ 相应降为**毕业后留痕**（自发命中证据，不推进数字）。
　　★ 与 🎓#156 同一处、同一个裁决，两条今天一起改判

**问题是什么**
**make a huge difference**（差别很大／很管用）。
判据：
```
✅ make a **huge／big／real／massive** difference    ✅ It doesn't make much difference.
✅ That made **all the** difference.（就是它起了决定作用，最强的一档）
★ 动词是 **make**，不是 have／bring（✗ have a big difference ／ ✗ bring a big difference）
★ 想说"对谁有差别"用 to：It makes a huge difference **to** kids.
```
判据一句话：这个块三样东西一起来 —— 动词 **make** · 冠词 **a** · 形容词档位（huge／big／real／massive）。
★ 与 🎓**#156**（同根词：the difference／different ways）的分工：#156 管 difference／different 的**词形**
　（前面有 the/a/of 就用名词形）；本条管 **make a … difference 这个块**（选哪个动词 ＋ 形容词档位）
　⇒ 规则不同；同一处写歪时**两个号各判各的**（§3.3 标记打在条目上，不打在整句上）。

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第二版 · 她自己写出
`creating an organized environment makes a huge difference`；同日 R3 再现 `makes a massive difference`。
判重：grep "difference" 全库（含已毕业）→ 命中 **#156**（同根词：the difference／different ways）
逐条读：#156 管的是 difference／different 的**词形**（前面有 the/a/of 就用名词形）；
本条管的是 **make a … difference 这个块**（选哪个动词 ＋ 形容词档位）⇒ 规则不同 ⇒ 保留新建。

**我错在哪**
她这次没有错（08-23 两句都是她自己产出的、块一字不差），建号理由是 §2③ **她点名要学**。
唯一一次写歪是 08-28 的 `makes a huge **different**` —— **已于 08-30 按她的裁决撤销**（她答"手滑"，
§2.1 拼写不算错）⇒ 那一行改判为 📝，不进连错。
找法：说出 make 之后，回头点三样东西 —— **make ＋ a ＋ 形容词 ＋ difference**（名词形，不是 different）。

**题面**
"每天多睡一个小时，对我白天的状态影响特别大。"（"影响特别大"用 **make** 说）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第二版 · `creating an organized environment makes a huge difference`
- 2026-08-23 ⚪ 同日再现 · d 段重答 R3 · `upgrading to smart traffic systems makes a massive difference`
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `whether you have help or not **makes a huge difference**.`
  ——冠词 a ＋ 形容词位 huge 全对 ⇒ **连对 0 → 1（差一次毕业）**
  ★ 同句自发命中 **#275**（whether 从句当主语，本条句子里另记一次 ✅，见 #275 日志）
    ＋ **#10**（主谓一致：whether 从句当主语 ⇒ 谓语单数 makes，⚪ 观察行）
  ★ 她主动把题面的"有没有人帮忙"翻成 whether 从句当主语 —— 比直译 `Having someone to help`
    更难也更地道，是自己选的路
  **不计连击**（§3.1 新建条目当天不测 —— 同一天记 ✅ 就是假 ✅）；massive 在下面 ✅ 档里，用对了
- 2026-08-28 📝 复习第2组 · `Whether you have help or not makes a huge **different**.` ⚠️ **本条已于 2026-08-30 改判为 📝**（原判 ❌ 已撤销）
  → makes a huge **difference**
  ★★ **2026-08-30 撤销留痕（她的裁决）**：教练当天问她"这是手滑打漏字母，还是当时真想着
    different"，她答 **"手滑"** ⇒ 按 §2.1（她 08-20 定）「拼写一律不算错，判据 ＝ **她脑子里
    调的词对不对**」⇒ 她调的是名词 difference，手指跑成了高频词 different
    ⇒ **不记档位、不进连错、不清连对** ⇒ 本行由 ❌ 改判为 📝。
    ★ 毕业日期**不追溯改动**：撤销是事后的，改不掉"她 08-29／08-30 又实打实走完两次复测"
      这个事实 ⇒ 🎓 仍记 2026-08-30。
  ★ 原判 ❌ 的理由（保留留痕，不删）：**题面点名里就印着 difference 这个词**，写出来的仍是 different
    ⇒ 考点位置不是一字不差 ⇒ 当时判 连对1 → 连对0 连错1（不毕业）
  ★ 同一处错误**同时落到 🎓#156**（同根词形位置规则）⇒ #156 **回潮**。
    两条各判各的，依据 §3.3「标记打在条目上，不打在整句上」；落号口径 ＝ **1 处 → 2 个号**
  ★ 为什么不按 §2.1 判成"拼写不算错"（四问②的完整留痕）：
    · 反证一：08-23 她自己写对过两次（makes a huge difference／a massive difference）
    · 反证二：**08-27 同一道题她写的就是 difference**（见 🎓#275 日志逐字）
    · 但 **#156 备注早有实证**："08-16 原答案写对，重说时反而退成 different"
      —— "写对过 → 重说退回形容词形"正是她这条的**固有形状**，不是随机手滑 ⇒ 判 ❌
    ⚠️ 她若说"就是手滑打漏了 -ce"，**本条的 ❌ 当场撤回**（§7 她的怀疑比教练的推理值钱）；
       #156 的回潮不撤（它的判据本来就是"重说时退回形容词形"）
  ⚪ 同句正面观察（不改状态）：🎓#275 whether ＋ 主谓结构对，但**与 08-27 同题面**属重复不属自发；
     #10 主谓一致 —— whether 从句当主语，谓语 makes 用单数，一次到位
- 2026-08-29 ✅ 复习第1组（她第一轮漏答一题，补答）· `Having someone to help makes a huge difference`
  ——考点位置一字不差：**makes a huge difference**
  ★ **08-30 撤销 08-28 的 ❌ 之后，本次 ＝ 连对1 → 连对2 ⇒ 毕业就发生在这一天**
    （当时按旧判定记的是"连对0 连错1 → 连对1 连错0"，留痕在此，不删）
  ★ 走的是与 08-27/08-28 不同的一条路（`Having someone to help` 直译主语，不是 whether 从句），
    块照样调出来了 ⇒ 本条测的是**块本身**，与主语怎么搭无关
  ★ **"有没有"没丢**（教练四问①推翻了自己的第一判断）：`A makes a difference` 这个块**自带对照义**
    ——"有 A 和没 A 不一样"就写在块里，不必再补 whether … or not ⇒ 不判缺失、不给更好版
  ★★ **本句里的 #156 只记 ⚪，不记第二次 ✅**（见 #156 同日日志）：
     本题题面点名里**印着 `difference` 这个词** ⇒ 词形是送的，#156 的考点这一次根本没被测到。
     判据 ＝ §4① 加速通道边界（她 08-27 认可）"刚掉的那一格没被测到 ⇒ 只记 ⚪，不推进连对"
- 2026-08-30 ✅ 复习第2组 [6] · `Whether you have help or not makes a huge difference.`
  ——考点位置一字不差：**makes a huge difference**（动词 make · 冠词 a · 形容词档位 huge）
  ★ **毕业后留痕**（同日晚些时候她裁定 08-28 是手滑 ⇒ 毕业日回填到 08-29）：
    本次是自发命中证据，**不推进数字**。当时按旧判定记的是"连对1 → 连对2，毕业"，留痕在此，不删。
  ★★ **本次是把 08-28 那一句原样重说**：
     08-27 ✅ `whether you have help or not makes a huge difference`
     → 08-28 `a huge different`（当日判 ❌，**08-30 已撤销为手滑**）
     → 08-29 ✅ 换了条路（`Having someone to help…`）⇒ 连对2，毕业
     → 08-30 ✅ **回到那一句，没退** ⇒ 毕业后的加固证据
  ⚪ 同句留痕（都不推进数字，各自记在本行）：
    · **#156** —— 词形又对了一次，但题面印着 difference ⇒ 送的，不算自发命中（见 #156 同日 ⚪ 行）
    · **🎓#275**（whether 从句当主语）—— 与 08-27／08-28 逐字同句，**属重复不属自发**，不记 ✅
      （沿用 08-29 的裁法）
    · **#10**（主谓一致：whether 从句当主语 ⇒ 谓语单数 makes）—— 形态类 ⚪ 正面记号，一次到位
- 2026-09-12 📝 题面整改：点名「用 make ＋ difference 说」→「用 make 说 · ⛔ 不许用 different」—— 原点名把块的两头都给了，中间只剩 a huge（§6② 红线一）· 全档题面 review
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"⛔ different"，点名 make，a ＋ 形容词 ＋ difference 留给她；换成多睡一小时场景


### 281 · step back（往后退一步，不插手）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
**step back**（往后退一步，不插手）。
判据：
```
✅ Parents need to **step back** and let them try.   ✅ It's about **stepping back**.
✅ take a step back（＝ 抽身看全局，略不同：偏"先别急，退开看看"）
★ 与 back off 的分工：**step back ＝ 主动不插手**（中性/正面，说家长/领导放手）
                      **back off ＝ 别管我**（带火气，是冲突语境）
★ 与 let go 的分工：let go 更彻底（撒手不管）；step back 是"退一步但还在旁边"
```
同一格里的邻居（别串 · 08-27 记下的细微分工，不判错）：`step back` ＝ 退开、不插手（持续状态，最常用）；
`take a step back` ＝ 退一步**重新看一看**（偏"跳出来审视"，常接 and look at it）⇒ 说家长别插手时 step back 更贴。
判据一句话：副词是 **back**（⛔ 不是 aside／away），说的是"退开不插手"。

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第三版 · 她自己写出 `Lastly, it's about stepping back.`
判重：grep "step back"／"back off" 全库（含已毕业）→ **零命中** ⇒ 保留新建。

**我错在哪**
她这次没有错（`Lastly, it's about stepping back.` 是她自己产出的），建号理由是 §2③ **她点名要学**。
找法：说"别插手／放手"时先问 —— 是中性地"退开"吗？是 ⇒ **step back**（⛔ 不是 step aside／step away／back off）。

**题面**
"孩子开始学做饭了，我就在旁边退一步，让他自己来。"（"退一步"用 **step** 说）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第三版 · `Lastly, it's about stepping back.`
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `Sometimes parents need to **step back** / **take a step back**.`
  ——副词 back 对（不是 step aside／step away）；**她给了两个版本，两个都成立**
  ⇒ **连对 0 → 1（差一次毕业）**
  ★ 两个的细微分工（记进判据，不判错）：
    `step back` ＝ 退开、不插手（持续状态，最常用）
    `take a step back` ＝ 退一步**重新看一看**（偏"跳出来审视"，常接 and look at it）
    ⇒ 说家长别插手时 `step back` 更贴
- 2026-08-28 ✅ 复习第1组 · `parents sometimes need to **step back**.`—— 连对2，**毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `step back`
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 step，back 留给她；换成孩子学做饭场景

### 282 · take ownership (of sth)（把它当成自己的事，自己扛起来）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-18** ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-28 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零）

**问题是什么**
**take ownership (of sth)** ＝ 把它当成自己的事、自己扛起来。
判据：
```
✅ learn to take ownership ／ take ownership **of** their own learning／of the problem
★ ownership 在这个意思上**不可数、不带 a**（✗ take an ownership）
★ 与 take responsibility 的分工：
    take **responsibility** ＝ 该我负责（义务、有时是被追责）
    take **ownership**      ＝ 我把它当自己的事（主动、有投入感）
  说孩子成长／员工成长时 **ownership 更贴**，也更像母语者会挑的词
```
同一格里的邻居（别串）：take ownership of ＋ **一件具体的东西**（their own work／their mistakes／what they do／the project）——
⛔ 别接一个和 ownership 同义的抽象名词（`of their own responsibility` 语义重叠，像"把责任的责任担起来"）；
最省事的一条：后面**整个不接**——`They learn to take ownership.` 本身就是完整句。
判据一句话：说的是"这是**我的**事"（主动）⇒ ownership；只是"该我负责"（义务）⇒ responsibility。
★ 与 #307（That's how …）分工：#307 是 08-28 同句里她主动提出建的号，本条只管 take ownership，不并进去。

**怎么发现的**
2026-08-23 新建（**她当场指定**，§2③）· d 段重答 R1 第三版 · 她的原话 `so they learn to take ownership`。
判重：grep "ownership"／"take charge"／"take responsibility" 全库（含已毕业）→ **零命中** ⇒ 保留新建。
2026-08-27 付息日 b 段本条建立以来第一次被测到 ✅；2026-08-28 复习第2组 ✅ ⇒ 毕业。
2026-09-11 付息日 a2 第 5 组复检：她答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**。

**我错在哪**
她的：答"忘了"（2026-09-11 复检）　　正确：`take ownership of it`
找法：中文出现"当成自己的事／自己扛"就先落 take ownership，⛔ 别滑到 take responsibility（那是"该我负责"）。

**题面**
"新员工得学会把手上的项目当成自己的事来扛。"（"当成自己的事来扛"用 **ownership** 说）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第三版 · `so they learn to take ownership`
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `that's how they'll learn to **take ownership of** their own responsibility.`
  ——ownership 不可数、不加冠词 ＋ 介词 **of** 全对 ⇒ **连对 0 → 1（差一次毕业）**
  ⚠️ 1 处更好版（不记档位）：`of their own **responsibility**` 与 ownership **语义重叠**——
    两个说的是同一件事（把担子接过来），叠着读像"把责任的责任担起来"
    ⇒ 更好版 `take ownership of their own **stuff**`
    ★ 判据：**take ownership of ＋ 一件具体的东西**（他们的作业／他们的房间／他们自己的事），
      别接一个和 ownership 同义的抽象名词
    ★ 同族都对：of their own work ／ of their mistakes ／ of what they do
    ★ 最省事的一条：后面**整个不接**——`They learn to take ownership.` 本身就是完整句
- 2026-08-28 ✅ 复习第2组 · `That's how they learn to take ownership.`
  ——`take ownership` 一字不差 ⇒ 连对2，**毕业**
  ★ 同句她主动提出要给 **That's how** 建条目（原话："That's how(这才可以建个条目) they learn…"）
    ⇒ 新建 **#307**（本条只管 take ownership，不并进去）
- 2026-09-11 ❌ 复检 · 付息日 a2 第 5 组 · 答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**
  最小改 `take ownership of it`
  ❌ "把自己的事当回事／自己扛起来" ＝ take **ownership** of sth；⛔ 不是 take responsibility（"负责"，偏被动担责）——
    ownership 多一层"这是**我的**事"。同族 take ownership of your mistakes／of the project
- 2026-09-12 📝 题面整改：「把自己的事当回事」→「把这事当成自己的事扛起来」—— 旧题面念回去是 take it seriously，映射不回 ownership（§6① 缩短的硬前提：中文必须还能映射回那个英文块）· 全档题面 review
- 2026-09-13 ❌ 学习日 在池第 1 组 · 答"忘了"（§3.3「忘了/不会」＝ ❌）
  最小改 `take ownership of it`
  ❌ ownership ＝ "这事归我管"的主人翁感；近邻 take responsibility for（担责任）没有"当成自己的事"那层
- 2026-09-15 ✅ 学习日 在池第 1 组 · `take ownership of it.` —— 连错2 → 连对1
- 2026-09-18 ✅ 学习日 在池第 1 组 · `take ownership of it.` ⇒ **连对 2，毕业**
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"take ＋ o- 开头的名词"猜谜写法，点名 ownership，take … of 怎么搭留给她（09-11／09-13 掉过）；换成新员工场景
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [5] · `Once you hit college, you need to take ownership of your learning.` —— take ownership of ＋ 具体的东西，ownership 不带 a

### 283 · 收尾句型：It's really about A first, and then B（把前面几点排成先后，收成一条线）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
收尾句型：**It's really about A first, and then B**（把前面几点排成先后，收成一条线）。
骨架：`So it's really about ＋【动名词 A】first, and then ＋【动名词 B】.`
用途 ＝ P3 收尾一句把前面几点**排成先后顺序**（详例见下方备注），比"总之两点都重要"有力得多。
判据一句话：四格一起验 —— 框架 ／ **first 的位置**（挂在 A 后面）／ **and then** ／ 两边都用动名词。
★ 与 **#277**（双面开头）天然配套：开头立两面 → 收尾把两面排成先后 ⇒ **首尾呼应**，P3 高分特征。
★ 与 🎓**#58**／🎓**#207** 的分工：那两条管**起手**，本条管**收尾** ⇒ 位置不同。
★ 与 **#284**（boil down to sth）的分工：中文触发词"说到底就是"整个让给 #284 ⇒ 本条题面已改成"我觉得就是"。
★ ⛔ **不许标 So overall 叠词**（2026-08-23 当天撤回的教练假错，见下方备注最后一条）。

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第二版 · 她自己写出
`So overall, it's really about setting up the structure first, and then slowly letting them take control.`
★ 她的原话："收尾句型，新建条目"（指 `So overall, it's really about setting up the structure first, and then slowly letting them take control.`）
判重：grep "really about"／"收尾句"／"Overall" 全库（含已毕业）→ 只命中 #206 的日志行（书面词降级，
与本条无关）与 🎓#58／🎓#207（那两条管**起手**，不管收尾）⇒ **零真命中，保留新建**。

**我错在哪**
她这次没有错（这句收尾是她自己在 R1 第二版里产出的），建号理由是 §2③ **她点名要学** ——
她要把这**一整句的收尾句型**固定下来，以后 P3 收尾能直接调。
找法：P3 最后一句开口前问一句 —— 前面那几点有没有**先后**？有 ⇒
`it's really about …**ing** first, and then …**ing**`，⛔ 别收成"两点都重要"。

**题面**
**点名**："我觉得就是先把框架搭起来，再慢慢放手。"（用 `it's really about … first, and then …` **一句话**收尾）
★ 题面 2026-08-27 微改（§6.5 审核项 8 题面撞车）：原题面开头"**说到底就是**"正是 **#284（boil down to sth）的中文触发词** —— 两条同一天出，中文一模一样、点名不同，她要在两句之间来回切。改成"我觉得就是"，把这个触发词整个让给 #284

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第二版 ·
  `So overall, it's really about setting up the structure first, and then slowly letting them take control.`
- 2026-08-27 ✅ 付息日 b 段（题面当天微改后**首测**）·
  `I think it's really about building the framework fist, and then gradually letting go.`
  ——四格全中：框架 ／ **first 的位置**（挂在 A 后面）／ **and then** ／ 两边都用动名词
  ⇒ **连对 0 → 1（差一次毕业）**（`fist` 是打字，§2.1 不算错）
  ★ `gradually letting go` 是很好的口语块（比 giving them more freedom 短且准），
    与 #281 `step back` 是同一个意思的两种说法，她两处都调得出来
  ★ 改题面的收益：中文换成"我觉得就是"之后她自然跟着换成 `I think`，
    没有被 #284 的 boil down to 干扰
- 2026-08-28 ✅ 复习第2组 · `I think it's really about building the framework first, and then gradually letting go.`
  ——整句收尾框架一字不差，两半都是 -ing、形也齐 ⇒ 连对2，**毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `it's really about setting up the framework first, and then gradually letting go.` —— 收尾句型完整
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 备注 骨架与用法：
```
So it's really about ＋【动名词 A】first, and then ＋【动名词 B】.
用途   P3 收尾一句把前面几点**排成先后顺序** —— 比"总之两点都重要"有力得多
✅ It's really about setting up the structure first, and then slowly letting them take control.
✅ It's really about getting the basics right first, and then worrying about speed.
✅ It's really about listening first, and then giving your own take.
⛔ ~~So overall 两个收尾词别叠着，选一个~~ —— **2026-08-23 当天撤回，是教练假错**：
   口语里 `So all in all, …` `So overall, …` 完全自然（"So" 是接上文，"overall" 是收总，
   两个功能不同，不算叠）。判紧的根因 ＝ 拿书面冗余标准评口语（§2.3b 禁令）。**不许再标。**
★ 与 #277（双面开头）天然配套：开头立两面 → 收尾把两面排成先后 ⇒ **首尾呼应**，P3 高分特征
```

### 284 · boil down to sth（说到底就是……）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
**boil down to sth**（说到底就是……）。
判据：
```
✅ It (all) boils down to X.
✅ It boils down to a combination of A, B and C.
✅ What it boils down to is trust.
★ 主语是 **it／整件事／某个动名词**，不是人（✗ I boil down to）
★ 后面接**名词或动名词**：boils down to **money** ／ boils down to **planning ahead**
★ 语义 ＝ 熬掉水分剩下最核心的那一点 —— 和 comes down to 同义，比它更口语、更有画面
```
判据一句话：中文"说到底就是"⇒ 调 **boil down to**（介词 **to**，主语是事不是人）。
★ 与 🎓**#58**（it mainly comes down to）的分工：同义，但**目标形式不同**（boil ≠ come）
　⇒ §3.1 判据三档第 3 档【两条 ＋ 题面互斥】：#58 题面不点名（测 comes down to），本条题面**点名 boil**。
★ 与 **#283**（收尾句型）的分工：中文触发词"说到底就是"2026-08-27 起**专属本条** ⇒ 触发词与考点一一对应。

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R3 · 她自己写出
`managing traffic boils down to a combination of smart technology, better public transport, and clever incentives`。
★ 她的原话："boils down to（新建条目，学）"
判重：grep `boil`／`comes down to`／`说到底` 全库（含已毕业）→ 命中 **🎓#58**（it mainly comes down to）。
逐条读：同义，但**目标形式不同**（boil ≠ come）⇒ §3.1 判据三档第 3 档【两条 ＋ 当场改题面互斥】。
**互斥关系**：🎓#58 题面 "说到底就是钱的问题。"（不点名，测 comes down to）；
本条题面**点名 boil** ⇒ 两条各测各的词，不撞车。

**我错在哪**
她这次没有错（R3 那句 `boils down to` 是她自己产出的、介词一字不差），建号理由是 §2③ **她点名要学**。
找法：中文冒出"说到底／归根到底"时，先问主语是**事**还是**人** —— 是事 ⇒ `It boils down to …`（⛔ 别接人当主语）。

**题面**
"学好一门语言，说到底就是每天坚持开口。"（"说到底就是"用 **boil** 说）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R3 · `managing traffic boils down to a combination of smart technology, better public transport, and clever incentives`
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `solving traffic congestion **boils down to** just a few key things.`
  ——介词 **to** 对，主语用动名词短语 ⇒ **连对 0 → 1（差一次毕业）**
  ★ 教练自审留痕：`solving traffic congestion` 差点被标（想换成 tackling／easing）——
    试造母语句推翻自己：`How do we solve traffic congestion?` 母语者照说 ⇒ **假错，未判**
  ★ `just a few key things` 比判据里的 `a combination of things` **更口语**，是她自己换的 ⇒ 加分
  ★ 今天把"说到底就是"这个中文触发词从 **#283** 收回、**专属本条** ⇒ 触发词与考点一一对应，
    她一次就调出了 boil down to
- 2026-08-28 ✅ 复习第2组 · `solving traffic congestion ultimately boils down to a few key things.`
  ——`boils down to` 一字不差 ⇒ 连对2，**毕业**
  ★ 自审留痕：ultimately ＋ boils down to 语义略重，但母语者确实这么说 ⇒ 不判
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `It boils down to a few things coming together.` —— boil down to 一字不差（题面本场缩成块，她照样给了整句，⛔ 不扣）
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 boil，down to 留给她；换成学语言场景（与 🎓#58 点名 come 互斥照旧）


### 285 · give sb (real) alternatives to sth／doing sth（给人别的选择，而不是只能……）
类型 搭配 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
**give sb (real) alternatives to sth／doing sth**（给人别的选择，而不是只能……）。
判据：
```
✅ alternatives **to** driving ／ alternatives **to** the car ／ an alternative **to** meat
   —— **to 是介词**，后面跟名词或 -ing
✗ alternatives **of** driving   ✗ alternatives **for** driving
★ choice ＝ 在几个里挑哪个 ｜ alternative ＝ **除了这条路之外还有的另一条路**
  （交通／能源／习惯／方案，凡是"不想让人只能 X"的题都能用）
★ 常配形容词：**real ／ viable ／ decent ／ genuine** alternatives（"像样的替代选择"）
★ 整块最好用的是 `give people real alternatives to X` —— 一句话把"堵不如疏"说完
```
判据一句话：说的是"**除了 X 之外还有别的路**"吗？是 ⇒ alternative **to** ＋ 名词/-ing（⛔ 不用 choice、⛔ 不用 of／for）。
★ 同一格里的邻居（都成立，不判错）：give ／ offer ／ provide sb alternatives 三个动词都标准；
　单数 `a real alternative` ＝ 一条替代路，复数 `real alternatives` ＝ 好几条可选。

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R3 · 她自己写出
`cities need to give people real alternatives to driving`。
★ 她的原话："real alternatives to（新建条目）"
判重：grep `alternativ`／`替代`／`别的选择` 全库（含已毕业）→ **零命中**，保留新建。

**我错在哪**
她这次没有错（R3 那句块一字不差，介词 to 也对），建号理由是 §2③ **她点名要学**。
找法：写出 alternative 之后立刻看下一个词 —— **是 to 吗？** 是 of／for ⇒ 改掉；
想说"选择"先分清：在几个里挑 ＝ choice，另有一条路 ＝ alternative。

**题面**
"想让大家少吃肉，就得给他们真正好吃的替代品。"（"替代品"用 **alternative** 说）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R3 · `cities need to give people real alternatives to driving`
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `cities need to **offer** people **a real alternative to** driving.`
  ——**alternative**（不是 choice）＋ 介词 **to** ＋ 后接动名词 driving ⇒ **连对 0 → 1（差一次毕业）**
  ★ 两处她自己换的，都成立、都未判：
    · `offer` 换掉判据里的 `give` —— offer sb alternatives 同样标准
    · `a real alternative`（单数）换掉 `real alternatives`（复数）—— 单数 ＝"一条替代路"，
      复数 ＝"好几条可选"；政策语境里复数更常见，但单数完全成立
- 2026-08-28 ✅ 复习第2组 · `Cities must provide a real alternative to driving.`
  ——`a real alternative to driving`（alternative TO ＋ -ing，没用 choice）⇒ 连对2，**毕业**
  ★ 她省了"给大家"（sb）那一格，句子合法 ⇒ 按 §3.3 记 ✅，不记 ◎
  ⚠️ 更好版给了口语降级：must provide → need to give people ／ a real alternative → real alternatives
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `a real alternative to driving` —— alternative **to**，⛔ 没用 choice
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"别用 choice"，点名 alternative，to 留给她；换成少吃肉场景

### 286 · 整句句型：If A, B and C, a lot of X will happily do Y（条件够好 → 人自愿去做）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）｜ 点名 2026-08-28 加结构限定（08-27 她走了 `will be happy to` 这条绕路）
状态 连对2 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-29 毕业 → 09-11 复检掉了 will：`many commuters happily leave…`，题面点名的 will happily 少了一半；08-27 绕 will be happy to、今天丢 will ⇒ 框没长稳，撤销毕业、连对清零）

**问题是什么**
整句句型：**If A, B and C, a lot of X will happily do Y**（条件够好 → 人就自愿去做）。
骨架：If ＋【主语】＋ are ＋【形1, 形2, and 形3】, ＋【一群人】＋ **will happily** ＋【一个具体动作】.
· 三个形容词必须**同形**（cheap, frequent, reliable；✗ cheap, frequent, and it's reliable）
· 主句是**预测** ⇒ **will 不能掉**；掉了 will 就成了零条件句（句子合法，但不是本条要她产出的那句）
· "乐意做某事"在论证句里走【副词】，⛔ 不走【be ＋ 形容词 ＋ to】：will happily leave ／ will gladly pay ／ would happily do it again
· 收尾动作要**具体可画面**：leave their cars at home ＞ use public transport more
同一格里的邻居（别串）：be happy to ／ be willing to ／ want to —— 它们正是 will happily 要替掉的那一族 ⇒ 题面正向点名 will happily。
判据一句话：主句里 **will ＋ 一个 -ly 副词 ＋ 一个具体动作**三样齐不齐？缺一样就不是这个框。
★ 位置分工：#277 管 P3 开头立两面 · 本条管中间"条件 → 反应" · #283 管收尾排先后。

**怎么发现的**
2026-08-23 新建（**她当场指定**，§2③）· d 段重答 R3 · 她的原话：
"这一整句，包括前面的并列好处，和后面的 will happily，新建条目"；
当时的产出原句 `If buses and trains are cheap, frequent, and reliable, a lot of commuters will happily leave their cars at home.`
判重：grep `happily`／`愿意`／`乐意` 全库（含已毕业）→ 命中的全是 willing／want 那一族
（#98 #100 #218 等只管"愿意"这个词怎么说），**无一条管这个整句框架** ⇒ 零真命中，保留新建。
2026-08-27 ❌ 首犯 · 付息日 b 段（本条建立以来第一次被测到）· 她走了 `will be happy to` 这条绕路。
2026-09-11 付息日 a2 第 4 组复检 · `many commuters happily leave their cars at home.` —— will 掉了 ⇒ **回潮**。

**我错在哪**
她的：`many commuters happily leave their cars at home.`（09-11 复检；08-27 那次是另一条绕路 `will be happy to`）
正确：`… many commuters **will** happily leave their cars at home.`
找法：条件那半句说完，主句先落 **will**，再挂一个 -ly 副词，最后才是那个具体动作。

**题面**
"只要上班时间灵活、离家近、工资也还行，很多年轻妈妈会很乐意回去工作。"（用 **if** 起头，"很乐意"用 **will happily** 说）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R3 · `If buses and trains are cheap, frequent, and reliable, a lot of commuters will happily leave their cars at home.`
- 2026-08-27 ❌ **首犯** · 付息日 b 段（**本条从建立起第一次被测到**）·
  `…many commuters **will be happy to** leave their cars at home.` → **will happily** leave…
  ⛔ **她这句英语本身是对的** —— ❌ 打的是"**题面点名的那个块没出来**"，不是语法错。
    题面白纸黑字写着"主句用 **will happily** ＋ 一个具体动作"
  ★ 可迁移的判据（本条判据里早就写着）："will happily 比 will be willing to 短、比 want to 有力"
    —— 她换的 `will be happy to` **正是它要替掉的那一族**（系动词 ＋ 形容词 ＋ to）
    ⇒ **"乐意做某事"在论证句里走【副词】，不走【be ＋ 形容词 ＋ to】**：
      will happily leave ／ will gladly pay ／ would happily do it again
  ✅ 另外三格全对，单独记：三个并列形容词**同形**（cheap, frequent, reliable）·
     收尾动作**具体可画面**（leave their cars at home）· `if ＋ 现在时`（＝🎓#60 自发命中）
  ★★ 教练自审（§3.3 为什么不给 ✅）：§3.3 的「答得合法但不是条目预期 ⇒ ✅ ＋ 改题面」
    立意是"她按题面答对了却拿不到分，等于罚她教练题面没写好"；**本题题面写得很清楚**
    （will happily 五个字直接印在题面上），她没照做 ⇒ 那一条不适用，档位是 ❌
  ⚠️ **出题提案（教练侧，未改题面，等她认可）**：下次点名改成
    "主句用**一个副词**加动词说（**不许用 be ＋ 形容词 ＋ to**）" —— 把她手里那个够用的
    替代品当场封掉，才测得到目标块
     → **2026-08-28 已落实进题面**（⛔ 主句不许写成 will be ＋ 形容词 ＋ to）；
       合法性依据 ＝ 08-27 立的分界：说得出封掉了哪条合法绕路 ⇒ 结构限定，不是预告测试点
- 2026-08-28 ✅ 复习第1组（**题面当天加 ⛔ 结构限定后首测**）·
  `If public transport is cheap, frequent and reliable, many commuter will happily leave their cars at home.`
  ——整句结构全中：if ＋ 三个并列形容词 ＋ 主句 `will happily leave their cars at home`
  ★★ **08-27 走的 `will be happy to` 这条绕路今天没再走** ⇒ 加结构限定有效（不是记不住，是没东西封绕路）
  ⚪ 同句 `many commuter` → many commuters ＝ **#150**（限定词与数一致，形态类只记号），不计入本条
  ⇒ 连对0 连错1 → **连对1 连错0**
- 2026-08-29 ✅ 复习第1组 · `if public transport is cheap, frequent and reliable, many commuters will happily leave their cars at home.`
  ——四格全中：if ＋ 三个并列形容词**同形**（cheap, frequent, reliable）＋ 主句 `will happily leave their cars at home`
  （具体可画面）＋ 一句话说完；⛔ 封住的 `will be happy to` 连续两天没再出现
  ⇒ 连对1 → **连对2，毕业**
  ⚪ 同句 `many commuters` —— 08-28 这里写的是 `many commuter`（当时记了 #150 的 ⚪），今天数对上了
     ⇒ **#150 记一条正面 ⚪**（形态类只记号，不动状态行）
- 2026-09-11 ❌ 复检 · 付息日 a2 第 4 组 · `If public transport is cheap, frequent, and reliable, many commuters happily leave their cars at home.` ⇒ **回潮**
  最小改 `… many commuters **will** happily leave their cars at home.`
  ❌ 题面点名 **will happily**，她掉了 will ⇒ 考点位置不是一字不差。这条句型是"条件够好 → 人就会自愿去做"的**预测**，主句要 will；
    掉了 will 就成了零条件句（句子合法、但不是本条要她产出的那句）。
  ★ 骨架 3/4 在：三个并列形容词 ✔ · happily ✔ · 具体动作 ✔ —— 08-27 绕 will be happy to、今天丢 will ⇒ 这个框还没长稳
- 2026-09-12 📝 题面整改：点名「主句用 will happily ＋ 一个具体动作」→「用 will ＋ 一个 -ly 副词 ＋ 一个具体动作；⛔ 不许用 be happy to／be willing to」—— 原点名把 will happily 整块交出去（§6② 红线一），09-11 给了块她照样丢 will ⇒ 给了也白给；改成结构限定后 happily 要她自己调 · 全档题面 review
- 2026-09-13 ✅ 学习日 在池第 2 组 · `If public transport is cheap, frequent, and reliable, many commuters will happily leave their cars at home.`——if＋三形容词、will＋happily＋leave their cars at home，整句一字不差（09-11 回潮后首测）
- 2026-09-15 ✅ 学习日 在池第 1 组 · `If public transport is cheap, frequent, and reliable, many commuters will happily leave their cars at home.` —— 整句框一字不差 → **连对2，毕业**
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"⛔ be happy to"与形态描述，点名 if ／ will happily —— 三个并列条件同形、will 不能掉留给她（她掉过的就是丢了 will）；换成年轻妈妈回去工作场景
- 2026-09-30 ✅ 复检 · 付息日 a2 第 3 组 [9] · `If the rent is cheap, transit is convenient, and the neighborhood is quiet, plenty of young people will happily move to the suburbs.`
- 备注 骨架与用法：
```
If ＋【主语】＋ are ＋【形1, 形2, and 形3】, ＋【一群人】＋ will happily ＋【一个具体动作】.
✅ If buses and trains are cheap, frequent, and reliable, a lot of commuters will happily
   leave their cars at home.
✅ If the courses are short, free, and online, a lot of people will happily pick one up.
✅ If the rules are clear, fair, and the same for everyone, most kids will happily follow them.
★ 三个形容词必须**同形**（都是形容词；✗ cheap, frequent, and it's reliable）
★ **will happily** ＝ 乐意／心甘情愿 —— 比 will be willing to 短、比 want to 有力
  它的真正作用：把**政策**翻译成**人的反应** ⇒ 正好补 P3 最常缺的层5（"为什么会有效"）
★ 收尾动作要**具体可画面**：leave their cars at home ＞ use public transport more
★ 位置 ＝ P3 的**中段**（#277 管开头立两面 · 本条管中间"条件→反应" · #283 管收尾排先后）
```

### 287 · flow smoothly ／ keep sth flowing（车流顺畅／让它一路走得顺）
类型 搭配 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ **keep 族·一组最多 2 条**（c 段 2026-08-27 加）｜ 题型 整句

**问题是什么**
**flow smoothly ／ keep sth flowing**（车流顺畅／让它一路走得顺）。
判据：
```
✅ Traffic flows smoothly.          ✅ keep the traffic ／ the cars **flowing** (smoothly)
✅ keep things moving（同族，更口语的一个）
★ flow 的主语是**成股走的东西**：车流／人流／水／信息／资金 —— 不是单个人（✗ he flows）
★ 载体句型 `keep ＋ 宾语 ＋ -ing` ＝ 让它**持续**处在那个状态（她本篇两处都用对了：
  keeps cars **moving** ／ keep the cars **flowing**）
★ 反面（同一题可以拿来对照）：traffic is at a standstill ／ traffic grinds to a halt（彻底堵死）
```
★ **keep 三兄弟交叉引用**（§6 组内防撞：同族 ≤2 题，而全库有三条 ⇒ 必须标出来）：
　**#287（本条）** keep ＋ 宾语 ＋ **-ing**　　keep the cars **flowing**　＝ 让它持续在**动**
　**#297**　　　　 keep ＋ 宾语 ＋ **形容词**　keep your mind **active**　＝ 持续处在某**状态**
　**#305**　　　　 keep ＋ **形容词**（无宾语）✗ keep patient ⇒ **stay patient**（封闭名单）
　⇒ 出题时**三条里最多同组出两条**

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R3 · 她自己写出
`using tech to keep the remaining cars flowing smoothly`。
★ 她的原话："flow smoothly 新建条目"
判重：grep `flow`／`smooth`／`顺畅`／`通畅` 全库（含已毕业）→ **零命中**
（grep 命中的 flow 行全部是 flowers，与本条无关）⇒ 保留新建。

**我错在哪**
她这次没有错（`keep the remaining cars flowing smoothly` 是她自己产出的），建号理由是 §2③ **她点名要学**。
找法：说"让它一路顺"时先看主语 —— 是**成股走的东西**（车流/人流/资金）吗？
是 ⇒ flow；挂在 keep 后面时宾语后面跟 **-ing**（flowing），⛔ 不是形容词。

**题面**
"新修的高架通车以后，早高峰的车流顺畅多了。"（"顺畅"用 **flow** 说）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R3 · `using tech to keep the remaining cars flowing smoothly`
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `and using technology to **keep the remaing cars flowing smoothly**`
  ——`keep ＋ 宾语 ＋ **-ing**`（flowing）＋ 副词 smoothly，与判据逐字相同
  ⇒ **连对 0 → 1（差一次毕业）**（`remaing` 是打字，§2.1 不算错）
  ⚠️ 1 处更好版（不记档位）：她给的是**分词片段**（句首还带个 and），题面本身是完整句
    ⇒ 更好版 `We can use technology to keep the remaining cars flowing smoothly.`
    ★ 中译英是单点抽测，片段不影响考点判定；但真答题时片段要挂回主句（＝ methods **M23**）
  ★★★ **今天最漂亮的一条对照**：同一天早上 a 段 #297 她写 `keeps mind **active**`
    （keep ＋ 宾语 ＋ **形容词**），本题写 `keep the cars **flowing**`（keep ＋ 宾语 ＋ **-ing**）
    ⇒ **两边都给对了**，正是这两条条目互相写进对方判据的那条边界（**状态** vs **持续在动**）
- 2026-08-28 ✅ 复习第2组 · `use technology to keep the remaining traffic flowing smoothly.`
  ——`keep … flowing smoothly` 一字不差（keep ＋ 宾语 ＋ -ing 那一格）⇒ 连对2，**毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `keep the remaining cars flowing smoothly` —— keep sth flowing
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 flow，flows smoothly／keep … flowing 怎么搭留给她；换成新修高架场景
- 2026-09-29 📝 补题型格 · 题型 词组 → 整句（09-29 题面整改时状态行漏改，本行补记）

### 288 · 机制句型：once X costs you something, you start asking whether …（把政策翻译成人的心理反应）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-29**（连对2）｜ 题型 整句

**问题是什么**
机制句型：**once X costs you something, you start asking whether …**（把政策翻译成人的心理反应）。
骨架：`(because) once ＋【代价发生的从句】, ＋ you ＋ start ＋ -ing ＋ whether ＋【主谓】.`
（详例与用法见下方备注）
判据一句话：**once ＝ "一旦……就"**（比 if 强：if 是"如果会"，once 假定它一定会发生，只讲发生之后人怎么变）；
这里的 **you ＝ 泛指所有人**，不是"你"。
★ 同一格里的邻居（别串 —— whether 前面接什么动词分两档）：ask／wonder／see／know／decide 可以**直接接 whether**；
　think／talk／worry **必须先加 about**（think **about** whether）⇒ ⛔ think whether 站不住。
★ 与 **#275**（whether 后面要跟主谓）的分工：#275 是本句**内部用对的一条规则**，不是本条考点；
　本条管的是整句机制框架 ⇒ 不同考点，两条并存。
★ 与 **#286** **配对使用**（P3 讨论任何政策都能一正一反各来一句）：#286 胡萝卜（条件变好 → 人自愿去做）／
　本条大棒（加了代价 → 人自我审查）⇒ 连词、主语、主句块都不同，题面天然互斥。

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R3 的 [S6] 更好版 ·
`…work really well, because once a trip costs you something, you start asking whether you actually need to make it.`
★ 她的原话："because once a trip costs you something, you start asking whether you actually need to make it. 这句很好，也要学"
★ 来源 ＝ 教练在 R3 [S6] diff-2 给的更好版（不是她的产出）⇒ 属 §2③「她主动提出的」
判重：grep `once`／`一旦`／`只要`／`whether`／`泛指` 全库（含已毕业）→ 两条候选，逐条读完：
· **#275**（whether 后面要跟主谓）—— 是本句**内部用对的一条规则**，不是本条的考点；
　本条管的是整句机制框架 ⇒ 不同考点，两条并存（本条判据里已引用 #275）
· **#286**（If A, B and C, … will happily do Y）—— 同族（都是"条件 → 人的反应"），
　但**连词不同**（if / once）、**主语不同**（一群人 / 泛指 you）、**主句块不同**
　（will happily ＋ 动作 / start asking whether ＋ 从句）⇒ §3.1 第 3 档【两条 ＋ 题面互斥】；
　题面天然互斥（#286 公交又便宜又密又靠得住 ／ #288 出门要花钱）
⇒ **零真命中，保留新建**。

**我错在哪**
她的（2026-08-27 首犯）：`…you naturally start **thinking whether** it's really necessary.`
正确：`start **asking** whether …` ／ `start thinking **about** whether …`
—— 两处叠在一起：① 题面点名了 start asking，她写的是 start thinking；
② 更要紧：**`think whether` 这个搭配站不住** —— think 接 whether 必须先加 **about**。
找法：写完 think／talk／worry，紧接着要接 whether 时问一句 —— **about 掉了没有？**
（ask／wonder／decide 才能直接接 whether。）

**题面**
"一旦外卖要多收五块配送费，你就会开始琢磨是不是自己做饭更划算。"（用 **once** 起头，"开始琢磨是不是"用 **start asking whether** 说）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R3 的 [S6] 更好版 · `…work really well, because once a trip costs you something, you start asking whether you actually need to make it.`
- 2026-08-27 ❌ **首犯** · 付息日 b 段（**本条从建立起第一次被测到**）·
  `…you naturally start **thinking whether** it's really necessary.`
  → start **asking** whether ／ start thinking **about** whether
  ❌ 两处叠在一起：① 题面点名了 **start asking**，她写的是 start thinking
     ② **更要紧**：`think whether` 这个搭配站不住 —— think 接 whether 必须先加 **about**
  ★ 可迁移的判据（比点名本身值钱）：**whether 前面接什么动词，分两档**
```
✅ 直接接 whether：ask ／ wonder ／ see ／ know ／ decide ／ not sure
✅ 必须先加 about：think **about** whether ／ talk **about** whether ／ worry **about** whether
✗ think whether   ✗ talk whether
★ 一句话：**think／talk／worry 这几个"要带 about 的动词"，接 whether 时 about 不能掉。**
```
  ★ 本条判据里其实已写着 `start asking／start thinking **about** ＋ whether 从句` ——
    她走 thinking 那条路本身可以，**只是 about 掉了**
  ✅ 其余三格全对，单独记：`Once ＋ 现在时`（costs，没写 will cost）· 泛指 **you**（不是 people）·
     whether 后面跟**主谓**（it's really necessary）＝ **🎓#275 自发命中**（本条今天刚毕业）
  ★★ 教练自审：与同组 #286 的 ❌ **不是同一个理由**（#286 是"块换成了同义说法"，
    本题是"搭配缺了必需的介词"）⇒ 两处独立判断，不是连着往严里判
  ⚠️ **出题提案（教练侧，未改题面，等她认可）**：下次点名保留 asking，另加"**不许用 think**"
     → **2026-08-28 已落实进题面**（⛔ 动词就用 asking，不许换成 think／wonder）；
       合法性依据 ＝ 08-27 立的分界：说得出封掉了哪条合法绕路 ⇒ 结构限定，不是预告测试点
- 2026-08-28 ✅ 复习第1组（**题面当天加 ⛔ 结构限定后首测**）·
  `Once every trip costs you a little something, you naturally start asking whether it's really necessary.`
  ——`once … you start asking whether` 整块一字不差
  ★★ **08-27 走的 `start thinking whether` 今天没再走** ⇒ 与 #286 同日两处互证：封住绕路就调得出
  ⚠️ 同句 `costs you a little something` → costs you something（a little something 默认读作"一件小礼物"）
     —— 只进 diff-2，**不建条目**（08-27 分界：判她写错了没有，不判有没有更口语的说法）
  ⇒ 连对0 连错1 → **连对1 连错0**
- 2026-08-29 ✅ 复习第1组 · `Once every trip costs you a bit of money, you'll naturally start asking whether the trip is really necessary.`
  ——`once … you'll naturally start asking whether …` 整块一字不差；⛔ 封住的 think／wonder 连续两天没再出现
  ⇒ 连对1 → **连对2，毕业**
  ⚠️ 同句 `whether **the trip** is really necessary` → whether **it's** really necessary
     ——前半句刚点过 every trip，同句第二次点名 ＝ 重复，英语默认用代词顶回去（指代唯一）
     只进 diff-2，**不建条目**（她别处代词用得好，说不出"她不会的是哪个词组／句型" ⇒ §3.2b 禁伞形）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 4 组 · `Once every trip costs a little money, you naturally start asking whether it's really necessary.` —— once ＋ start asking whether，一字不差
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"⛔ think／wonder"，正向点名 once ／ start asking whether；换成外卖配送费场景
- 备注 骨架与用法：
```
(because) once ＋【代价发生的从句】, ＋ you ＋ start ＋ -ing ＋ whether ＋【主谓】.
✅ Once a trip costs you something, you start asking whether you actually need to make it.
✅ Once you have to pay for a bag, you start asking whether you really need one.
✅ Once feedback is public, people start thinking about whether the comment is worth posting.
★ once ＝ "一旦……就" —— 比 if 更强：if 是"如果会"，once 假定它**一定会发生**，只讲发生之后人怎么变
★ 这里的 you ＝ **泛指所有人**，不是"你"—— P3 讲机制用泛指 you 最自然（比 people 更近、更快）
★ start asking／start thinking about ＋ whether 从句 ＝ "开始掂量……是不是"
  whether 后面必须跟**主谓**（＝#275 那条规则），✗ start asking whether necessary
★ 真正的作用 ＝ **层5 的机制层**：把一个政策翻译成【人的心理反应】，
  答案立刻从"这个办法是什么"变成"这个办法为什么有效"
★★ 与 #286 **配对使用**（P3 讨论任何政策都能一正一反各来一句）：
    #286 胡萝卜  条件变好 → 人自愿去做    If A, B and C, a lot of X will happily do Y.
    #288 大棒    加了代价 → 人自我审查    Once X costs you something, you start asking whether …
```

### 289 · be obsessed with sth（特别迷／上头）
类型 搭配 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
**be obsessed with sth**（特别迷／上头）。
判据：
```
✅ be obsessed **with** sth ／ **with** doing sth      ✅ 名词形 an obsession **with** sth
✗ obsessed **about** ／ 这个意思上也不用 obsessed **by**
★ 介词写死是 **with** —— 这是本条唯一的考点
★ 语气 ＝ 夸张的"特别迷／上头"，褒贬都能用，口语里常带一点调侃
  P1/P3 讲爱好、讲一代人的习惯最顺手：My dad's obsessed with fishing.
★ 主语是**人**。想说"这东西现在很火"另有说法：it's all the rage ／ it's a big thing now
```
判据一句话：obsessed 后面**只跟 with**，主语是人。

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R4 · 她自己写出 `I mean, older folks are obsessed with it.`
★ 她的原话："older folks are obsessed with it（新建条目）"
判重：grep `obsess`／`痴迷`／`着迷`／`入迷`／`特别喜欢` 全库（含已毕业）→ **零命中**，保留新建。

**我错在哪**
她这次没有错（`older folks are obsessed with it` 是她自己产出的、介词一次到位），
建号理由是 §2③ **她点名要学**。
找法：写出 obsessed 就立刻挂 **with**（⛔ 不是 about／in／by）。

**题面**
"我儿子最近特别迷恐龙，天天让我给他讲。"（"特别迷"用 **obsessed** 说）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R4 · `I mean, older folks are obsessed with it.`
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `older folks are really **obsessed with** this kind of thing.`
  ——介词 **with** 对（不是 about／in）⇒ **连对 0 → 1（差一次毕业）**
  ★ 教练自审留痕：`really obsessed` 差点被标（怕强调词叠强调词自我对冲，＝ methods M22 的形状）——
    试造母语句推翻自己：`He's really obsessed with cars.` 母语者极常说 ⇒ **假错，未判**。
    M22 管的是**软化词**（about／kind of／I guess）叠强调词，不是强调词叠形容词
  ★ 同句自发命中 **🎓#106**：`this **kind of thing**`——kind of ＋ 单数名词、不带冠词，用对了
  ★ `older folks` 与判据里的写法**逐字一致**（她 08-23 自己的原话）⇒ 块留住了
- 2026-08-28 ✅ 复习第1组 · `older folks are especially **obsessed with** this.`—— 连对2，**毕业**
  ★ 四问自审留痕：especially 曾想判 ⚠️（"特别"更常说 really），试造母语句
    `Older folks are especially into this kind of thing.` 成立，且中文本身含"相对别人更"这层 ⇒ **不判**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `be obsessed with this`
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 obsessed，with 留给她；换成儿子迷恐龙场景

### 290 · 收尾块：… for totally different reasons depending on who you ask（同一个现象，不同的人理由完全不一样）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
收尾块：**… for totally different reasons depending on who you ask**（同一个现象，不同的人理由完全不一样）。
骨架：`…, just for totally different reasons **depending on** ＋【名词 或 疑问词从句】.`（详例见下方备注）
判据一句话：前面分了两类人／两种情况 ⇒ 收尾用这个块，把它们收成"同一个现象、不同的理由"
（比 "So it depends." 强得多 —— 那句等于什么都没说）。
★ depending on 后面的疑问词从句用**陈述语序**（＝ 🎓#59 那条规则）：
　✅ depending on who you ask　✗ depending on who do you ask。
★ 与 **#283** 的分工（两个都是收尾块，别混）：#283 把几点排成**先后**（It's really about A first, and then B.）；
　本条把几点收成**同一现象的不同版本**。

**怎么发现的**
2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R4 · 她自己写出
`So yeah, it's pretty common, just for totally different reasons depending on who you ask!`
★ 她的原话："for totally different reasons depending 新建条目"
判重：grep `depend`／`取决`／`因人而异`／`看情况`／`而定` 全库（含已毕业）→ 命中 2 行，
逐条读：两行都是 **#275**（whether 后跟主谓）判据里的例句 `It depends on whether…`，与本条无关
⇒ **零真命中，保留新建**。

**我错在哪**
她这次没有错（这个收尾块是她自己在 R4 里产出的），建号理由是 §2③ **她点名要学**。
找法：P3 收尾前问一句 —— 我前面是不是分了两类人／两种情况？
是 ⇒ 用 `for different reasons **depending on** who you ask`，⛔ 别收成一句 "So it depends."。

**题面**
**点名**："所以这种情况挺普遍的，只是问不同的人，理由完全不一样。"（用 **depending** 那个词收尾）
★ 点名 2026-08-27 收窄（§6.5 审核项 7 自查时记的待办，当天兑现）：原点名给的是**整块** `depending on who you ask` —— 属 §6 允许的"点块"，但它同时**把答案给了大半**（含 who you ask 那半里的 🎓#59 陈述语序考点）。收窄到只点 **depending** 之后，后半截要她自己凑 ⇒ 考点密度回来了

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R4 · `So yeah, it's pretty common, just for totally different reasons depending on who you ask!`
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `So it's pretty common, but the reasons are totally different **depending on who you ask**.`
  ——收尾块 ＋ 里面的疑问词从句用陈述语序（who you ask，不是 who do you ask）⇒ 一字不差
  ⇒ **连对 0 → 1（差一次毕业）**
  ★ 她把骨架重排了（判据是 `…, just for totally different reasons depending on…`，
    她写成 `…, but the reasons are totally different depending on…`）——
    两个都成立，她这版把 but 的转折点出来了，甚至更清楚 ⇒ 不改、不标 ⚠️
  ★ 同句自发命中 🎓#59（who you ask 陈述语序）
- 2026-08-28 ✅ 复习第3组（点名收窄成只点 depending 后**第一次复测**）·
  `So it's pretty common -- it just comes down to different reasons **depending on who you ask**.`
  ——收尾块一字不差；后半截（who you ask 的陈述语序）**不点名她也自己凑出来了** ⇒ 连对2，**毕业**
  ⚪ 同句两处自发命中（已毕业，不改状态）：🎓#58 `comes down to`（题面完全没提）· 🎓#59 `who you ask`
  ⚠️ `comes down to different reasons` 语义顶牛（comes down to 收敛到一个点／后面接发散的复数理由）
     ⇒ 更好版 `it's just for totally different reasons depending on who you ask`，只进 diff-2，不建号
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `So it's pretty common, just for different reasons depending on who you ask.` —— 收尾块一字不差
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组

- 备注 骨架与用法：
```
…, just for totally different reasons **depending on** ＋【名词 或 疑问词从句】.
✅ So yeah, it's pretty common, just for totally different reasons depending on who you ask.
✅ It varies a lot depending on where you live ／ how old you are ／ what you're after.
✅ 同族尾巴：depending on the person ／ depending on the city
★ depending on 后面的疑问词从句用**陈述语序**（＝#59 那条规则）
  ✅ depending on who you ask        ✗ depending on who do you ask
★ 用途 ＝ **P3 收尾专用**：前面分了两类人／两种情况，最后一句把它们收成
  "同一个现象、不同的理由" —— 比 "So it depends." 强得多（那句等于什么都没说）
★★ 与 #283 的分工（两个都是收尾块，别混）：
    #283  把几点排成**先后**          It's really about A first, and then B.
    #290  把几点收成**同一现象的不同版本**  …, just for different reasons depending on who you ask.
```

### 291 · "说话当下就要做的事" ＝ Let me … ／ I'll …（不用一般现在时）
类型 语法 ｜ 新建 2026-08-24
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-26**（连对2）｜ 题型 整句

**问题是什么**
"说话当下就要做的事" ＝ **Let me …** ／ **I'll …**（⛔ 不用一般现在时）。
判据：
```
中文"我就给你…／我先给你看…／那我帮你问一下"这一类【说话当下发起的动作】，
英语**不能用一般现在时** —— 一般现在时说的是"习惯／常态"：
   I give my students advice every week.  ＝ 我每周都给（习惯）
   I show people around on weekends.      ＝ 我周末带人参观（常态）
"现在这就做"只有两条路：
   Let me ＋ 动词原形   ← 请对方允许／缓一拍   Let me give you a piece of advice.
                                              Let me check.  Let me put it another way.
   I'll ＋ 动词原形     ← 当场决定／答应对方   I'll show you something first.
                                              I'll ask him for you.  I'll get you a coffee.
✗ I give you a piece of advice.   ✗ I show you something.   ✗ I ask him for you.
★ 判据一句话：**这件事是"现在这就做"还是"平时都做"？** 现在这就做 ⇒ Let me ／ I'll
```
★ 与 **#12**（时态判断触发）的分工：#12 管"看中文时间标记词选时态"（触发词"以前／常／了"，目标过去式／used to）；
　本条管"**当下发起的动作**不能用一般现在时"（触发"我就…／我先…／那我…"，目标 Let me／I'll）⇒ 触发与目标形式都不同。
★ 与 **#270**（advice 的量词）的题面互斥见下方备注：#270 题面是"我就给你一条建议。"，本条另起一句。

**怎么发现的**
2026-08-24 新建 · 复习第 1 组 #270 句里 · 她写 `I give you a piece of advice.`
（→ **Let me give you** a piece of advice.）—— 语法没错，但英语不这么起句 ⇒ ⚠️（§2② 说得不地道），本条由它触发。
判重（当天新建复核，§4④1b）：
　① 目标英文形式 ＝ `Let me give you …`／`I'll show you …`
　② grep `Let me`／`let me` 全库（含已毕业）→ **零命中**；
　　 grep `I'll` → 命中 #74（make do with 整块）· 🎓 even if 那条（`Even if it rains, I'll go`）·
　　 whether or not 那条（`I'll go whether you come or not.`）—— 三条都只是**例句里恰好含 I'll**；
　　 grep `一般现在时` → 命中 #12 · if 条件句那条 · #271
　③ 逐条读：**#12**（时态判断触发）管的是"看中文时间标记词选时态"，触发词是"以前／常／了"，
　　 目标是过去式／used to；**本条**管的是"**当下发起的动作**不能用一般现在时"，
　　 触发是"我就…／我先…／那我…"，目标是 Let me／I'll ⇒ **触发不同、目标形式不同**。
　　 **if 条件句那条**管从句里不放 will ⇒ 无关。**#271** 管副词拉完成时 ⇒ 无关。
　　 **#74／even if／whether** 只是例句撞了 I'll 三个字母 ⇒ 无关
　⇒ **保留新建**。

**我错在哪**
她的：`I give you a piece of advice.`　　正确：`**Let me give you** a piece of advice.` ／ `I'll give you …`
找法：开口前问一句 —— 这件事是"**现在这就做**"还是"平时都做"？
现在这就做 ⇒ Let me ／ I'll，⛔ 不许用一般现在时。

**题面**
"你等一下，我帮你问问前台还有没有空房。"
★ 零提示：Let me ask／I'll ask／I'm going to ask 都算对；她掉过的错路是一般现在时 `I ask …`

- 2026-08-24 新建 · 复习第1组 #270 句里 · `I give you a piece of advice.`
  → **Let me give you** a piece of advice.
  ——语法没错，但英语不这么起句 ⇒ ⚠️（§2② 说得不地道），本条由它触发
- 2026-08-25 ✅ 复习第1组（建立后首测，题面当天加点名）· `Let me show you something first.`
  ——与目标形式一字不差 ⇒ **连对 0 → 1（差一次毕业）**
  ★ 新加的点名"不用 want／going to"封掉了两条合法绕路（`I want to show you…`／`I'm going to show you…`），
    一个字没泄目标形式；她直接产出 Let me ⇒ 首测即命中
  ★ 同组 #270② 她写的是 `I have just one piece of advice for you.` —— **也没走 `I give you…` 那条错路**，
    两处独立佐证本条的目标形式已经上手
- 2026-08-26 ✅ 复习第1组 · `Let me show you something first.`
  ——与 08-25 逐字相同、与目标形式 A 一字不差 ⇒ **连对 1 → 2，🎓 毕业**
  ★ 两天两测，错路 `I show you something first.` 一次都没再出现；触发它的那句
    `I give you a piece of advice.`（08-24）之后再未复现 ⇒ 目标形式已上手
- 2026-09-11 ✅ 复检 · 付息日 a2 第 4 组 · `Let me show you something first.` —— 说话当下就要做的事走 Let me…，句尾 first 也落对
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）
  去掉"不用 want／going to"，改零提示（Let me／I'll／I'm going to 都算对），逼的是她掉过的一般现在时；换成前台问空房场景
- 备注 题面互斥（§3.1 第三档）：**#270** 的题面是"我就给你一条建议。"（考点 ＝ a piece of advice），
  本条题面另起一句"我先给你看个东西。" ⇒ 两条永不撞车

### 293 · "其中的一侧／一头／一角" ＝ one side of it ／ one of its sides（不说 its one side）
类型 结构 ｜ 新建 2026-08-24
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-26**（连对2）｜ 题型 整句

**问题是什么**
"其中的一侧／一头／一角" ＝ **one side of it** ／ **one of its sides**（⛔ 不说 its one side）。
判据：
```
表示"**从整体里挑出一个部分**"（partitive）时，英语只有两条路：
   one side **of it**        ／   **one of** its sides
`its ＋ 数词 ＋ 名词` 不成立 —— its 已经把归属指死了，再加 one 就和它冲突
✅ climbing up one side of it     ✅ one of its walls is all glass
✅ one corner of the room         ✅ one end of the street       ✅ one of the bedrooms
✗ its one side   ✗ its one corner   ✗ its one end
★ 判据一句话：**说"它的某一个 X" ⇒ 把 one 挪到 of 前面去**
★ 边界：不是 partitive 的时候 its ＋ 名词照常用（its roof／its glass exterior／its two towers）
```
★ 与 **#26**（比较题必须说出另一边）的分工：那条管**论证时必须把 B 面说出来**（逻辑结构），
　与"部分-整体怎么表达"无关 —— 只是 grep 时撞了 one side 三个字。

**怎么发现的**
2026-08-24 ❌ 首犯 · 自由产出（新题 bank:1027 P2）· 她写
`a giant panda sculpture climbing up **its one side**`（→ climbing up **one side of it**）。
判重（当天新建复核，§4④1b）：
　① 目标英文形式 ＝ `one side of it`／`one of its sides`
　② grep `one side`／`its one`／`一侧`／`一边`／`一头` 全库（含已毕业）→ **零真命中**
　　（`one side` 唯一命中是 **#26** 的标题"比较题必须说出另一边"——那条管的是
　　 **论证时必须把 B 面说出来**，是逻辑结构，与"部分-整体怎么表达"无关）
　⇒ **保留新建**。

**我错在哪**
她的：`climbing up **its one side**`　　正确：`climbing up **one side of it**` ／ `one of its sides`
找法：想说"它的某一个 X"时，**把 one 挪到 of 前面去** —— its 后面⛔不许再跟数词。

**题面**
"那栋老楼的一面墙上画满了涂鸦。"（"一面墙"用 **one** 说）

- 2026-08-24 ❌ 首犯 · 自由产出（新题 bank:1027 P2）· `a giant panda sculpture climbing up **its one side**`
  → climbing up **one side of it**
- 2026-08-25 ✅ 复习第1组 · `there is a tree growing out of **one side of the building**.`
  ——one 挪到了 of 前面，错路 `its one side` 没再出现 ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ★ 顺带 `growing out of` 这个动词块也用准了（树从建筑长出来的标准说法），本条不额外落号
- 2026-08-26 ✅ 复习第1组 · `there is a tree growing out of **one side of it**.`
  ——换成了本条列出的**另一个**目标形式（08-25 走 one side of the building，今天走 one side of it），
  两个都在判据里 ⇒ **连对 1 → 2，🎓 毕业**
  ★ 教练自审留痕：孤立句里 `it` 没有先行词（理解侧"代词指代唯一"），差点被判 ⚠️ ——
    但本条判据白纸黑字把 `one side of it` 列为目标形式，且中译英是单句抽测、上下文就在题面里
    ⇒ 拿这个扣她 ＝ **假错**，不判；只作一行语境提示发给她（不落号、不记档位）
  ★ `growing out of` 连续第二天自发用准
- 2026-09-10 ✅ 复检 · 第 3 组 · `on one side of the building` —— one side **of** the building，⛔ 没说 its one side
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句（类型 结构 ⛔ 不许标词组）
  点名 one，one … of it／one of its … 怎么摆留给她（她掉过的是 its one side）；换成老楼涂鸦场景

### 294 · "留心／注意着点" ＝ be mindful of sth（mind 没有形容词用法）
类型 搭配 ｜ 新建 2026-08-24（**她当场指定**）
状态 连对2 连错0 上次2026-09-29 ｜ **🎓 已毕业 2026-09-13** ｜ 题型 整句 ｜ **回潮 2026-09-10**（08-26 毕业 → 09-10 复检写成 `be mind of`，名词 mind 被塞进 be ___ of 的槽，撤销毕业、连对清零）

**问题是什么**
"留心／注意着点" ＝ **be mindful of sth**；**mind 没有形容词用法**。
判据：
```
mind 只有名词（心思）和动词（介意）用法；**"留心着点"的形容词是 mindful**
be mindful **of** ＋ 名词 ／ of how… ／ of what…      ★ 介词写死是 of
✅ You need to be mindful of how often you do it.    ✅ be mindful of other people's time
✅ Just be mindful of the cost.
✗ be mind of   ✗ be minded of   ✗ mindful about
★★ **同义替换（口语更常用、难度更低）**：想不起 mindful 就用这两个顶，别卡在那儿 ——
   **keep an eye on how much**（＝🎓#240）／ **watch how often you do it**
★ 边界：`Do you mind…?`（你介意吗）／`Never mind`（算了）是动词 mind，与本条无关
```
同一格里的邻居（别串）：同族全是「形容词 ＋ of」—— be careful of ／ be aware of ／ be mindful of
⇒ ⛔ 不能把名词塞进 be ___ of 的槽。
判据一句话：要填进 be ___ of 的那个词，是形容词吗？mind 不是，mindful 才是。
★ 与 🎓#240（keep an eye ON sth）的分工：同义替换关系、题面互斥 ——
　#240 题面点名 eye（"买东西的时候得留意点价格。"），本条题面点名 mindful ⇒ 不撞车。

**怎么发现的**
2026-08-24 新建（**她当场指定**）· 自由产出（新题 bank:924 P3）· 她的原话："they need be mind of（新建个条目）"；
当时的产出原句 `they need be **mind** of how often and how much` → need to be **mindful** of…
判重（当天新建复核，§4④1b）：
  ① 目标英文形式 ＝ `be mindful of`
  ② grep `mindful`／`be mind`／`留心`／`注意着点` 全库（含已毕业）→ **零命中**；
     grep `keep an eye` → 命中 **🎓#240**（keep an eye ON sth ＝ 留意）
  ③ 逐条读：**#240** 的目标形式是 `keep an eye on`（动词 ＋ eye ＋ on），
     本条的目标形式是 `be mindful of`（系动词 ＋ 形容词 ＋ of）⇒ **词组不同、介词不同**。
     两条是同义替换关系，按 §3.1 第三档 **题面必须互斥**：
     #240 题面点名 eye（"买东西的时候得留意点价格。"），本条题面点名 mindful ⇒ 不撞车
  ⇒ **保留新建**
2026-09-10 复检第 3 组（打包）· `be mind of how often and how much you give` ⇒ **回潮**：
隔了 15 个练习日再测，派生这一步没跑起来，直接把名词 mind 塞进了 be ___ of 的槽。

**我错在哪**
她的：`be mind of how often and how much you give`（09-10 复检；08-24 首犯 `they need be mind of…` 同形）
正确：`be mindful of how often and how much you give`
找法：往 be ___ of 这个槽里填词之前，先问一句它是不是形容词 —— mind 是名词／动词，形容词是 **mindful**。

**题面**
"零食可以吃，但要留心吃了多少。"（"留心"用 **mindful** 说）
　　★ 她点名要学的块 ⇒ 直接点名 mindful（练），be … of ＋ how much 怎么挂留给她

- 2026-08-24 ❌ 首犯 · 自由产出（新题 bank:924 P3）· `they need be **mind** of how often and how much`
  → need to be **mindful** of…
- 2026-08-25 ✅ 复习第1组（题面当天改点名后首测）· `parents should be **mindful of** how often and how much they give.`
  ——形容词形式对（mindful，不是 mind）、介词对（of，不是 about）
  ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ★ 这个 ✅ 是真的：新点名只给了 mind 这个**词根**，**mindful 是她自己派生出来的**；
    若沿用旧点名（直接写 mindful）这一题就是零信息量的白测
  ★ `need be` → `should be`：她换成情态动词绕开了（情态 ＋ 原形本来就不带 to）⇒ 合法，
    🎓#143 已于 08-24 毕业，不动
- 2026-08-26 ✅ 复习第1组 · `parents should be mindful of how often and how much they give.`
  ——与 08-25 逐字相同：形容词形式 mindful ＋ 介词 of 两处都对 ⇒ **连对 1 → 2，🎓 毕业**
  ★ 教练自审留痕：要不要因为"和昨天一模一样"怀疑是背下来的？—— 不怀疑。
    题面逐字复用是 §6 硬规则，同题面同答案属设计内；毕业线（连对2）本来就定义为
    "两次独立场合都调得出来"，本次成立
  ★ 08-25 改点名的收益二次确认：点名只给词根 **mind**，她连续两天自己派生出 **mindful**
    ⇒ 那次改题面改对了（旧点名直接写 mindful ＝ 把考点整个交出去）
- 2026-09-10 ❌ 复检 · 第 3 组（打包）· `be mind of how often and how much you give` —— **回潮**
  最小改 `be mindful of how often and how much you give`
  ❌ mind 是名词／动词，⛔ **没有形容词用法**；"留心着点"要用形容词 mindful，后面固定接 of。
  ★ 同族全是「形容词 ＋ of」：be careful of／be aware of／be mindful of ⇒ ⛔ 不能把名词塞进 be ___ of。
  ★ 08-25／08-26 连续两天她都自己从词根 mind 派生出了 mindful ⇒ 那两次 ✅ 是真的；
    隔了 15 个练习日再测，派生这一步没跑起来，直接把名词 mind 塞进了 be ___ of 的槽。
- 2026-09-11 ✅ 付息日 a 段 · 第 1 组 · `be mindful of how often and how much you give`
  —— mind → mindful 派生这一步跑起来了（昨天写成 be mind of 回潮的）⇒ 连对1
- 2026-09-13 ✅ 学习日 在池第 2 组 · `be mindful of how often and how much you give.`——mindful 形容词形出来了
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 ✅ 复检第 2 组 · `be mindful of how often and how much you give.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"mind 的形容词形式"形态描述；她点名要学的块 ⇒ 直接点名 mindful（练），be … of 怎么挂留给她；换成吃零食场景

### 295 · "做某事的目的" ＝ the purpose OF doing sth（口语直接说 why they do it）
类型 搭配 ｜ 新建 2026-08-24
状态 连对2 连错0 上次2026-09-21 ｜ **🎓 已毕业 2026-08-26**（连对2）｜ 题型 整句

**问题是什么**
"做某事的目的" ＝ **the purpose OF doing sth**（口语直接说 **why they do it**）。
判据：
```
名词 purpose 后面接 **of ＋ 动名词**，介词写死
✅ the purpose of doing this      ✅ the whole purpose of the trip
✗ the purpose for doing this
（for 只出现在 `the purpose **for which** it was built` 这种正式关系结构里，口语用不上）
★★ **口语替换才是主用法** —— "change the purpose of doing things" 这一整个说法口语几乎不出现：
   **Rewards change why kids do things.**  ／  **That's not what they're doing it for.**
★ 同族（抽象名词 ⇒ 摊成小句）：the reason for → why… ｜ the way of doing → how they do it
```
★ 与 🎓**#236**（说人的目的用不定式 to do；for ＋ -ing 是物品用途）的分工：#236 管的是**状语**位置
　怎么说"为了做某事"；本条的 purpose 是**名词中心词**、后面挂介词短语，管的是**这个名词的搭配**
　⇒ 按 #236 的规则去改会改出 `the purpose to do things`，**也是错的** ⇒ 不是同一条规则。
★ 与 🎓**#242**（on purpose ＝ 故意）／🎓**#264**（a sense of ＋ purpose）的分工：一个是固定块、
　一个是 a sense of 的框 ⇒ 都无关。
★ 与 🎓**#206**（书面词降级）的边界：本条**题面点名了 purpose** ⇒ 复习里⛔不许再拿 #206 标 ⚠️；
　那条降级只在**自由产出**里判。

**怎么发现的**
2026-08-24 ❌ 首犯 · 自由产出（新题 bank:924 P3）· 她写 `Rewards change the purpose **for** doing things`
（→ the purpose **of** doing things）。
判重（当天新建复核，§4④1b）：
　① 目标英文形式 ＝ `the purpose of doing sth`
　② grep `purpose`／`目的` 全库（含已毕业）→ 命中 **🎓#236**（说人的目的用不定式 to do；
　　 for ＋ -ing 是物品用途）· **🎓#242**（on purpose）· **🎓#264**（a sense of ＋ purpose 等）
　③ 逐条读：**#236** 管的是**状语**位置怎么说"为了做某事"（to do vs for -ing）；
　　 本条的 purpose 是**名词中心词**、后面挂介词短语，管的是**这个名词的搭配**。
　　 决定性证据：按 #236 的规则去改会改出 `the purpose to do things`，**也是错的**
　　 ⇒ #236 给不出正确答案 ⇒ **不是同一条规则**。
　　 **#242** 是 on purpose（故意）这个固定块 ⇒ 无关；**#264** 管 a sense of 跟哪几个名词 ⇒ 无关
　⇒ **保留新建**。

**我错在哪**
她的：`Rewards change the purpose **for** doing things`　　正确：`the purpose **of** doing things`
找法：写出 purpose 之后，后面那个介词**只能是 of**（⛔ 不是 for）；口语里更该问一句 ——
能不能干脆说成 `why they do it`？能就别用这个名词。

**题面**
"报班之前，你得先想清楚学这个的目的是什么。"（"目的"用 **purpose** 说）

- 2026-08-24 ❌ 首犯 · 自由产出（新题 bank:924 P3）· `Rewards change the purpose **for** doing things`
  → the purpose **of** doing things
- 2026-08-25 ✅ 复习第1组 · `rewards change the purpose **of** doing things.`
  ——介词 of 对（昨天写的是 for）⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ★ 教练自审留痕（§7 四问④）：本条备注写着"口语替换才是主用法"（`Rewards change why kids do things.`），
    按 🎓#206 本该给 ⚠️ 降级 —— **但本题题面点名了 purpose**，是教练把这个书面名词钉在她句子里的；
    再拿"你不该用 purpose"标 ⚠️ ＝ 罚她照题面答题 ⇒ **本题不标**，
    口语走法只作一行提示发给她（不落号、不记档位）。该降级只在**自由产出**里判
- 2026-08-26 ✅ 复习第1组 · `rewards change the purpose **of** doing things.`
  ——介词 of 连续第二次对（08-24 首犯写的是 for）⇒ **连对 1 → 2，🎓 毕业**
  ★ 08-25 那条留痕今天照办：题面点名了 purpose，就**不许**再拿 🎓#206（书面词降级）标 ⚠️；
    `Rewards change why kids do things.` 只作一行提示发出，不进 diff-2、不落号、不记档位
  ★ 本条的降级判定只在**自由产出**里跑 —— 她哪天在 P2/P3 里自己冒出 the purpose of doing things，
    那时才按 🎓#206 给 ⚠️
- 2026-09-10 ✅ 复检 · 第 3 组（打包）· `the purpose of doing things` —— 介词 **of** 用对
- 2026-09-21 ⚡ 自评免测 · 复检第 4 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 purpose，of／for 留给她（她掉过的是 the purpose for doing）；换成报班场景

### 296 · cut corners（偷工减料／图省事把该做的步骤跳掉）
类型 词组 ｜ 新建 2026-08-24（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
**cut corners**（偷工减料／图省事把该做的步骤跳掉）。
判据：
```
cut corners ＝ 为了省事／省钱／省时间，**把该做的步骤跳掉**（贬义）
✅ They cut corners on the materials.      ✅ Don't cut corners on safety.
✅ If you cut corners now, it'll cost you later.
★ 用在她那句里是准的：答应了 iPhone 结果买个便宜山寨的 ＝ cut corners
★★ 边界（三个都对应中文"打折扣／走捷径"，方向不同，别混）：
   · cut corners       ＝ 该做的没做全（偷工减料，贬）
   · take a shortcut   ＝ 抄近路／找捷径（中性，可以是聪明办法）
   · go back on sth    ＝ 说话不算数（承诺整个不认了）
```
判据一句话：贬义的"该做的没做全" ⇒ **cut corners**，挂宾语用介词 **on**。

**怎么发现的**
2026-08-24 新建 · **她主动提出**（§2③）· 自由产出（新题 bank:924 P3）· 她自己写出
`parents need to keep their promises and not cut corners` —— 用得准，不是错。
★ 她的原话："not cut corners（新建个条目）"
判重（当天新建复核，§4④1b）：grep `cut corners`／`偷工`／`走捷径`／`shortcut`
全库（含已毕业）→ **零命中** ⇒ 保留新建。

**我错在哪**
她这次没有错（`not cut corners` 是她自己用准的），建号理由是 §2③ **她点名要学**。
找法：说"偷工减料／打折扣"时先分三档 —— 该做的没做全 ⇒ cut corners（介词 on）；
抄近路 ⇒ take a shortcut；说话不算数 ⇒ go back on sth。

**题面**
"这家餐厅换了老板以后就开始偷工减料，菜的分量越来越少。"（"偷工减料"用 **cut** 说）

- 2026-08-24 新建 · **她主动提出**（§2③）· 自由产出（新题 bank:924 P3）·
  `parents need to keep their promises and not cut corners`——用得准，不是错
- 2026-08-27 ✅ 付息日 a 段 · **本条从建立起第一次被测到，一次到位** ·
  `they cut corners on materials to save money.`——词组 ＋ 介词 **on** 一字不差
  ⇒ **连对 0 → 1（差一次毕业）**
  ★ 教练自审留痕：`on materials` 缺 the 差点被判 ⚠️（判据例句写的是 on **the** materials）——
    试造母语句推翻自己：`They cut corners on materials to save money.` 母语者照说
    （materials 作泛指复数时不带 the）⇒ **假错，未判**
  ★ 本条 08-24 建（她当场指定），按 §4① 学习日一律不出 ⇒ **付息日 a 段是它唯一的召回点**，
    这次证明"她自己用对了才建的"那一批不是白建
- 2026-08-28 ✅ 复习第1组 · `they **cut corners on** materials to save money.`
  ——词组和介词都对（cut corners **on** sth）⇒ 连对2，**毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `cut corners on materials`
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"cut ＋ 一个名词"形态描述，只点名 cut；换成餐厅换老板场景


### 297 · keep your mind active（"保持…活跃"用 keep ＋ 宾语 ＋ 形容词，不用 make sth stay adj）
类型 搭配 ｜ 新建 2026-08-25
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-27**（连对2）｜ **keep 族·一组最多 2 条**（c 段 2026-08-27 加）｜ 题型 整句

**问题是什么**
**keep your mind active**（"保持…活跃"用 keep ＋ 宾语 ＋ 形容词，⛔ 不用 make sth stay adj）。
判据：
```
"让某个东西保持某个状态"，英语一个动词就够 —— **keep ＋ 宾语 ＋ 形容词**，
中文那个"保持"**不翻**，直接吃进 keep 里：
   ✅ keeps your mind active      ✅ keep fit          ✅ keep busy
   ✅ keep things simple          ✅ keep the noise down   ✅ keep your options open
   ✗ make your mind stay active   ✗ make things stay simple   ✗ let your mind keep active
★ 判据一句话：**看见中文"让…保持…"，先把"保持"删掉，剩下的直接塞进 keep ＋ 宾语 ＋ 形容词**
★ 边界（别混）：
   · keep ＋ 宾语 ＋ **-ing** ＝ 让它持续在**动**（keeps cars moving／keep things flowing）＝ #287
   · keep ＋ 宾语 ＋ **形容词** ＝ 让它持续处在某个**状态**（本条）
   · make ＋ 宾语 ＋ 形容词 ＝ **使它变成**那样（makes children fat）＝ 🎓#192 —— 是"变"不是"保持"
```
★ **keep 三兄弟交叉引用**：**#287** keep ＋ 宾语 ＋ **-ing**（keep the cars flowing）／
　**#297（本条）** keep ＋ 宾语 ＋ **形容词**（keep your mind active）／
　**#305** keep ＋ **形容词**（无宾语，✗ keep patient ⇒ stay patient）
　⇒ 出题时三条里最多同组出两条。**本条已毕业不再召回**，标记留给另两条防撞用

**怎么发现的**
2026-08-25 ❌ 首犯 · 自由产出（新题 bank:987 P3 Is it necessary to keep learning after
graduating from school?）· 她写 `studying something makes your mind **stay** active`
（→ **keeps your mind active**）。
判重（当天新建复核，§4④1b ⛔ 严禁脚本批量判 —— grep 只捞候选，判断逐条人读）：
　① 目标英文形式 ＝ `keep your mind active`（keep ＋ 宾语 ＋ 形容词）
　② grep `keep your mind`／`mind active`／`active` 全库（含已毕业）→ **零命中**；
　　 grep `keep ＋`／`keeps` → 命中 **#287**；grep `make sb`／`make O` → 命中 **🎓#192**；
　　 grep 中文 `保持`／`活跃`／`脑子` → 零真命中（唯一 `脑子` 是 08-24 犯规留痕里的引文）
　③ 逐条读：
　　 **#287**（flow smoothly ／ keep sth flowing）—— 它的核心词是 **flow**，载体是
　　　 keep ＋ 宾语 ＋ **-ing**（持续在动）。本条是 keep ＋ 宾语 ＋ **形容词**（持续处在某状态），
　　　 核心词是 active、补语类型不同 ⇒ **不同条**，题面也互斥（车流 vs 脑子）
　　 **🎓#192**（make sb ＋ 形容词，cause 不能这么用）—— 决定性证据：
　　　 按 #192 的规则去改，得到的是 `makes your mind active`（＝"使脑子变活跃"），
　　　 **不是她要表达的"保持活跃"，也不是母语者在这句里会说的那个** ⇒ #192 给不出正确答案
　　　 ⇒ 不是同一条规则（同 #295 vs 🎓#236 的判法）
　⇒ **保留新建**。

**我错在哪**
她的：`studying something makes your mind **stay** active`　　正确：`learning something **keeps your mind active**`
找法：看见中文"让…保持…"，先把"保持"两个字**删掉**，剩下的直接塞进 `keep ＋ 宾语 ＋ 形容词`
（⛔ 不许再往里塞一个 stay）。

**题面**
"退休以后多出去走走，能让身体一直保持灵活。"（"保持"用 **keep** 说）

- 2026-08-25 ❌ 首犯 · 自由产出（新题 bank:987 P3 Is it necessary to keep learning after
  graduating from school?）· `studying something makes your mind **stay** active`
  → **keeps your mind active**
- 2026-08-26 ✅ 复习第1组（建立后首测）· `learning something new keeps your mind active.`
  ——keep ＋ 宾语 ＋ **形容词**一次到位，错路 `makes your mind stay active` 换掉了
  ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ★ 她自己加对的两处：`learning`（比 studying 更贴"学点东西"）· `something new`
    （learn something new 是母语者常搭）—— 加分不扣分
  ★ 出题前写死的预判没发生：审核表 7 里预判"若她走 keep ＋ -ing（keeps your mind working）
    ⇒ 按 §3.3 记 ✅ ＋ 当场改题面"。她直接给了形容词补语 ⇒ **题面不用改**
- 2026-08-27 ✅ 付息日 a 段 · `learning something keeps mind active.`
  ——keeps／mind／active 三格一格不差 ⇒ **连对 1 → 2，🎓 毕业**
  ⚪ 同句 `mind` 前缺限定词（应为 your mind）—— **形态类·限定词，只做记号**（§3.4⑤b）：
    同一组里限定词她做对了 5 次（the final say ／ my time ／ the kind of person ／
    their lives ／ his cool）⇒ 不记 ❌、不影响本条毕业
    ★ 检查触发：**说完一个名词回头看它前面有没有东西**（the／a／my／your）——
      光秃秃的单数可数名词在英语里站不住
  ★ 两次通过用的是两个不同的宾语壳（08-26 `your mind` ／ 今天 `mind`），框架本身没动 ⇒ 稳
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `keep your brain sharp / active` —— keep ＋ 宾语 ＋ 形容词 这个框（⛔ 没走 make sth stay adj）
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 keep，宾语 ＋ 形容词怎么接留给她（她掉过的是 make … stay active）；换成退休保持身体灵活场景

- 备注 ★ **这不是句型缺口，是一个具体搭配没调出来**：她已经会 keep ＋ 宾语 ＋ 补语 ——
  08-23 R3 `keeps cars moving`、08-23 R1 `keeps things simple` 两处都自发用对。
  ⇒ 出题只出这一个搭配，别扩成"keep 句型"整片（§3.2b：考点必须能收敛成一个词组）

### 298 · have the final say（拍板／最后说了算）
类型 词组 ｜ 新建 2026-08-25（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
**have the final say**（拍板／最后说了算）。
判据：
```
have ／ get the final say (**on** sth) ＝ 最后拍板的那个人
   ✅ Mom had the final say.               ✅ Who has the final say on this?
   ✅ She gets the final say on the budget.   ✅ The final say is his.
★ 介词写死是 **on**（the final say on sth），不是 about／for
★ 同族（一起记，方向不同，别混）：
   · have the last word  ＝ 争论里说最后一句（偏"不肯认输"，略贬）
   · call the shots      ＝ 做主／说了算（整体掌权，不限于某一次决定）
   · it's up to sb       ＝ 由某人定（三个里最口语）
```
判据一句话：考点是 **say 当名词**这个块（the final **say**），不是 final 这个词。

**怎么发现的**
2026-08-25 新建 · **她主动提出**（§2③）· 加练新题 bank:1043 P2 · 她自己写出
`As for what counted as 'good', Mom had the final say.` —— 块本身用得准（`find` 是打字，§2.1 不算错）。
★ 她的原话："Mom had the find say（**the final say 可以建个条目**)"
判重（当天新建复核，§4④1b ⛔ 严禁脚本批量判）：
　① 目标英文形式 ＝ `have the final say (on sth)`
　② grep `final say`／`拍板`／`说了算`／`决定权` 全库（含已毕业）→ **零条目命中**
　　（`拍板` 两处命中都是散文行：#157 的迁出记录 ＋ methods 讨论的行文，不是条目考点）
　③ 无候选可并 ⇒ **保留新建**。

**我错在哪**
她这次没有错（`Mom had the final say.` 块用得准），建号理由是 §2③ **她点名要学**。
找法：说"最后拍板"时，中心词是**名词 say**（the final say），挂宾语用 **on**（⛔ 不是 about／for）。

**题面**
"家里装修的事，最后都是我爸拍板。"（"拍板"用 **say** 说）

- 2026-08-25 新建 · **她主动提出**（§2③）· 加练新题 bank:1043 P2 ·
  `As for what counted as 'good', Mom had the final say.`——块本身用得准（`find` 是打字，§2.1 不算错）
- 2026-08-27 ✅ 付息日 a 段 · **本条从建立起第一次被测到**（题面当天改点名后首测）·
  `My mon has the final say.`——the final **say**（say 当名词）一字不差（`mon` 是打字，§2.1 不算错）
  ⇒ **连对 0 → 1（差一次毕业）**
  ★★ **今天改点名的收益当场验证**：旧点名点 **final**，`my mum made the final decision`
    既合法又含 final ⇒ 会白测；改点 **say** 之后，**final 是她自己想出来的** ⇒ 改对了
  ⚠️ 1 处更好版（不记档位）：题面里的"**这事儿**"没落地，且本条判据把介词写死是 **on** ——
    不带宾语时这一格测不到 ⇒ 更好版给 `My mom has the final say **on this**.`
    **下次出题沿用同一题面即可**，她已经知道要补 on this
- 2026-08-28 ✅ 复习第3组 · `My mom has the final say.`——`the final say` 一字不差 ⇒ 连对2，**毕业**
  ★ "这事儿"那一格仍然没译（08-27 就提示过要补 on this），但句子完整合法 ⇒ 按 §3.3 记 ✅，不判档位
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `have the final say` —— say 当名词
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 say，the final say 怎么凑留给她；换成家里装修拍板场景
- 2026-09-29 📝 补题型格 · 题型 词组 → 整句（09-29 题面整改时状态行漏改，本行补记）


### 299 · not much of a/an ＋ 名词（"算不上一个…／没多少…"）
类型 词组 ｜ 新建 2026-08-25（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
**not much of a/an ＋ 名词**（"算不上一个…／没多少…"）。
判据：
```
not much of ＋ **a/an** ＋ 【单数可数名词】＝ "算不上一个…"
   ✅ He's not much of a cook.            ✅ It wasn't much of a party.
   ✅ That's not much of an excuse.       ✅ I don't have much of a choice.
   ✅ I didn't have much of an imagination.
★ 名词可数时 **of a/an 不能省**：✗ he's not much cook
★ 名词不可数时两条路都通，**of 版更口语、语气更足**：
   I don't have much imagination.（平）／ I don't have much of an imagination.（更像在说话）
★ 边界（另外两个固定块，别混）：
   · much of the time      ＝ 大部分时候
   · too much of a good thing ＝ 好事过了头
```
判据一句话：本条唯一要测的那一格 ＝ **of a／an 有没有省掉**。
★ 与 🎓**#269**（"不太了解／知道得少"走否定 ＋ much）的分工：#269 的 much 后面直接跟不可数名词
　或介词，**没有一个带 of a/an**；按 #269 的规则改"他算不上个厨师"给不出 `he's not much of a cook`
　⇒ 结构不同，两条题面也互斥。

**怎么发现的**
2026-08-25 新建 · **她主动提出**（§2③）· 加练新题 bank:1043 P2 · 她自己写出
`What made it challenging was that I didn't have much of an imagination.` —— 一个字不用改。
★ 她的原话："I didn't have much of（**much of 的用法可以建一个条目**)an imagination"
★ **她这一句是用对了的**，建条目是因为她主动要（§2③），不是因为犯错。
判重（当天新建复核，§4④1b ⛔ 严禁脚本批量判）：
　① 目标英文形式 ＝ `not much of a/an ＋ 名词`
　② grep `much of`／`not much`／`算不上`／`没什么` 全库（含已毕业）→ 命中 **🎓#269**
　　（"不太了解／知道得少"口语走 don't know much about it，合并条 3 句）
　　 ＋ 🎓#25 的题面"罚款对乱扔垃圾没什么用"（中文"没什么"撞字，考点是 It's no use doing）
　③ 逐条读：
　　 **🎓#269** 的规则是"中文说**少**，口语走【否定 ＋ much/any】"，三个成员分别是
　　　 don't know much **about it**／don't have much **time**／there isn't much **to do** ——
　　　 much 后面直接跟不可数名词或介词，**没有一个带 of a/an**。
　　　 决定性证据：按 #269 的规则去改"他算不上个厨师"，只能改出 `he doesn't know much…` 这类，
　　　 **给不出 `he's not much of a cook`** ⇒ 结构不同、#269 覆盖不到 ⇒ 不是同一条
　　　（同 #295 vs 🎓#236 的判法）。两条题面也互斥：#269 三句是"不太了解/没什么时间/没什么可玩的"，
　　　 本条题面是"他算不上个厨师"
　　 **🎓#25** 的考点是 It's no use doing sth，只是中文题面里有"没什么"三个字 ⇒ 无关
　⇒ **保留新建**。

**我错在哪**
她这次没有错（`I didn't have much of an imagination.` 一个字不用改），建号理由是 §2③ **她点名要学**。
找法：说"算不上一个 X"时，X 可数就**别省 of a／an**（⛔ not much cook ⇒ not much of a cook）。

**题面**
"我这人不怎么爱动，算不上个运动型的人。"（"算不上"用 **much of** 说）

- 2026-08-25 新建 · **她主动提出**（§2③）· 加练新题 bank:1043 P2 ·
  `What made it challenging was that I didn't have much of an imagination.`——一个字不用改
- 2026-08-27 ✅ 付息日 a 段 · **本条从建立起第一次被测到** ·
  `he is not much of a chief`——**`of a` 的冠词没省**（✗ not much cook），这正是本条唯一要测的
  那一格，一字不差 ⇒ **连对 0 → 1（差一次毕业）**
  ⚪ `chief` → **chef**：判成**拼写**不判选词（§2.1 边界"她脑子里调的词对不对"）——
    chef→chief 只是中间插了个 i（ie/ei 类混淆），且她阅读 7–7.5，chief 在她词库里是"首领"，
    不可能认为 厨师 ＝ chief；同批打字噪音也重（mon／thaty）。**已给她反悔通道**：
    她若说是真不会，当场补号
    ⚠️ 反向自查留痕：#255 `virtual` 想说 vital 当年判的是**选词**（照常算）——
      区别在词形距离：virtual/vital 差三个字母、词形不相邻；chef/chief 只差一个插入的 i
  ★ 不标 ⚠️ 但给她一行信息（§7 四问④：够不上 ⚠️ 的一律不标）：
    口语里"算不上个厨师"最常说的是 **not much of a cook**（cook ＝ 会做饭的人，日常；
    chef ＝ 职业厨师）。题面"厨师"两义都通 ⇒ 她用 chef 不算错也不算生硬
- 2026-08-28 ✅ 复习第1组 · `he is **not much of a** chef.`—— 连对2，**毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `not much of a chef`
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 much of，a ＋ 名词怎么接留给她；换成"算不上运动型的人"场景


### 300 · stage 前面的介词是 at（at every stage／at this stage，不用 in）
类型 搭配 ｜ 新建 2026-08-26（**补建**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
名词 **stage** 前面的介词是 **at**（at every stage／at this stage，⛔ 不用 in）。
判据：
```
名词 stage 表"阶段"时，**默认介词是 at**：
   ✅ at every stage of your life     ✅ at this stage       ✅ at some stage
   ✅ at a later stage                ✅ at all stages of the process
   ✗ in all stages of your life
★ in 只用在 **in the early / final / later stages of sth**（"处在某个阶段之中"，
  前面必须有 the ＋ 形容词）：in the early stages of the project ✅
★ 第二处（顺带记，不单独建号）：**every stage（单数）比 all stages 更口语、更有节奏**
★ 判据一句话：**说"在……阶段" ⇒ 先写 at；只有 the early/final stages 才轮到 in**
★ 档位说明：这是 ⚠️（不地道）不是 ❌ —— `in all stages of the disease` 这类母语者也说，
  但 `in all stages of your life` 不是他们会选的说法
```
★ 全库**没有**别的条目管 stage ⇒ 无最接近项（判重见下）。

**怎么发现的**
2026-08-25 ⚠️ 首犯 · 自由产出（新题 bank:987 P3）· 她写 `learning is necessary **in all stages of** your life`
（→ necessary **at every stage of** your life）。
⛔ **教练漏建**（08-26 她主动问"昨天的复习点都出全了吗"时才发现）：当天这一处只写进了
🎓#206 的一行备注、**没有单独建号** ⇒ 08-26 **补建**本号。
判重（补建当天复核，§4④1b ⛔ 严禁脚本批量判 —— grep 只捞候选，判断逐条人读）：
　① 目标英文形式 ＝ `at every stage of` / `at this stage`
　② grep `stage`／`阶段` 全库（含已毕业）→ 只有 2 处命中，逐条读：
　　 · 🎓#206 的一行备注（正是 08-25 漏建的那处，就是本条的来源）⇒ 不是条目
　　 · #271 备注里的"想用一般现在时 ⇒ 换成**指现在这个阶段**的副词"—— 说的是
　　　 these days 那一族副词，与名词 stage 的介词搭配无关 ⇒ 无关
　③ 与最接近的条目的区别：全库**没有**管 stage 的条目 ⇒ 无最接近项
　⇒ **保留新建**。

**我错在哪**
她的：`learning is necessary **in all stages of** your life`
正确：`necessary **at every stage of** your life`
找法：写出"阶段"这个词先落 **at**；只有说 the early／final stages 时才轮到 in。

**题面**
"在孩子成长的每个阶段，父母要操心的事都不一样。"（"每个阶段"用 **stage** 说）

- 2026-08-25 ⚠️ 首犯 · 自由产出（新题 bank:987 P3）· `learning is necessary **in all stages of** your life`
  → necessary **at every stage of** your life
  ⛔ **教练漏建（08-26 她主动问"昨天的复习点都出全了吗"时才发现）**：当天这一处只写进了
    🎓#206 的一行备注（"3 处偏正式，不判回潮"），**没有单独建号** ⇒ 它既不在池里、
    也不会在任何复习组出现，等于当天判完就丢了。
    根因：把它和同段的"代词链""双层从句摊平"（那两个确实是开放集合 §3.2b）一起塞进了
    "⚠️ 不建条目 4 处"那一行 —— **没有逐条跑 §3.2b 的自查**
    （"说得出她不会的是哪个词组／哪个句型就建"）。本条明显收敛得出：**stage 配 at**。
- 2026-08-27 ✅ 付息日 a 段（补建后首测）·
  `People need to learn something new **at every stage of** their lives.`
  ——介词 **at** ＋ **every stage**（单数）两格全中，08-25 的 `in all stages` 换掉了
  ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ★ `their lives` 复数也对（主语 People 是复数 ⇒ 每人一条命），比单数更地道，未改
  ★ 删掉点名里"注意介词"四个字之后考点仍存活：她没走 `at every point in your life`／
    `throughout your life` 两条合法绕路
  ★★ **补建的价值当场兑现**：这一处 08-25 判完只写进了 🎓#206 的一行档位备注、没有编号 ——
    若不是她 08-26 质询覆盖率，它今天根本不会出现在任何题里。补建 → 次日首测 → 一次修正
- 2026-08-28 ✅ 复习第1组 · `You have to keep learning something new **at every stage** of life.`
  ——介词 at 对 ⇒ 连对2，**毕业**。★ 从补建（08-26）到毕业只用了 3 天，全程零 ❌
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `At every stage of life` —— 介词 at
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 stage，介词 at 留给她（她掉过的是 in all stages）；换成孩子成长场景

### 301 · enjoy ＋ 物主代词 ＋ time／stay（不说 enjoy the time）
类型 搭配 ｜ 新建 2026-08-26（**补建**）
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-18** ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-28 毕业 → 09-11 复检写成 `enjoy the time with him`，与 08-26 建号触发句一模一样，撤销毕业、连对清零）

**问题是什么**
**enjoy ＋ 物主代词 ＋ time／stay**：enjoy 后面接"时光"类名词时，那个名词前面要**物主代词**，⛔ 不是 the。
判据：
```
enjoy 后面跟"一段时光／一次经历"时，那个名词前面要**物主代词**，不是 the：
   ✅ I really enjoyed **my** time with him.        ✅ Enjoy **your** stay!
   ✅ We enjoyed **our** weekend at the beach.      ✅ Did you enjoy **your** holiday?
   ✗ I enjoyed the time with him.   ✗ Enjoy the stay.
★ 例外（带从句限定时 the 反而对）：**the time I spent with him** ／
  **the time we had together** —— 后面挂了限定从句，the 就站得住了
★ 边界（别扩大）：enjoy 后面跟**别的东西**时照常用 the：
  enjoy the film ／ enjoy the food ／ enjoy the view —— 本条只管"时光"这一类
★ 判据一句话：**enjoy ＋ 时光 ⇒ 先想 my／your／our，除非后面要挂从句**
★ 档位说明：这是 ⚠️（不地道）不是 ❌
```
同一格里的邻居（别串）：题面已排除 spending（`enjoy spending time with him` 是另一条合法路，绕开考点）。
★ 与 #67（enjoy yourself 那一族）的分工：那边是**反身代词**做固定块的一部分、后面不接名词；本条是**物主代词 ＋ 名词**。
★ 与 🎓#265（good for your health）的分工：#265 自己写死了范围只到 good/bad for ___，按它去改得到的是 `good for my time` ⇒ 不是同一条规则。

**怎么发现的**
2026-08-25 ⚠️ 首犯 · 自由产出（加练新题 bank:1043 P2）· 她的原话 `I really enjoyed **the time** with him`
（→ enjoyed **my time** with him）；当天教练漏建（同 #300），**2026-08-26 补建**。
判重（补建当天复核，§4④1b ⛔ 严禁脚本批量判 —— grep 只捞候选，判断逐条人读）：
  ① 目标英文形式 ＝ `enjoy my time`
  ② grep `enjoy`／`享受`／`时光`／`物主代词` 全库（含已毕业）→ 4 处命中，逐条读：
     · #67 的备注"同族块：explain yourself／behave yourself／**enjoy yourself**／help yourself"
       —— 那是**反身代词**是固定块的一部分（enjoy yourself ＝ 玩得开心），
       本条是**物主代词 ＋ 名词**（enjoy my time）⇒ 两个不同的结构，且 enjoy yourself
       后面不接名词 ⇒ 无关
     · 同上的第二处引用（2616 行，讲 explain yourself 时列的同族）⇒ 同上，无关
     · 🎓#208「some people ≠ somebody」，题面"有些人就是享受花钱这件事。" ——
       只是中文题面里有"享受"两个字，考点是 some people ⇒ 无关
     · 🎓#265「good for you／good for your health」的备注里有"物主代词" ——
       决定性证据：#265 的备注**自己写死了范围**"本条的范围只到 good/bad for ___，
       不许扩大成'所有 health 前面都要物主代词'"；且按 #265 的规则去改，
       得到的是 `good for my time`，**根本不是本条要的答案** ⇒ 不是同一条规则
       （同 #295 vs 🎓#236、#297 vs 🎓#192 的判法）
  ⇒ **保留新建**
2026-09-11 付息日 a2 第 5 组复检 · `enjoy the time with him` —— 与 08-26 建号触发句一模一样 ⇒ **回潮**。

**我错在哪**
她的：`enjoy the time with him`（09-11 复检；08-25 首犯 `I really enjoyed the time with him` 同形）
正确：`enjoy my time with him`
找法：enjoy 后面要接"时光"了 —— 先想 my／your／our，除非后面还要挂一个从句。

**题面**
"这次在海边住的几天，我过得特别开心。"（用 **enjoy** 说，"住的几天"用 **stay** 说）

- 2026-08-25 ⚠️ 首犯 · 自由产出（加练新题 bank:1043 P2）· `I really enjoyed **the time** with him`
  → enjoyed **my time** with him
  ⛔ **教练漏建（同 #300，08-26 补）**：当天写进了 [S12] 的 diff-2 和落号对账的
    "⚠️ 不建条目 4 处"，**没有单独建号**。同一处根因：没逐条跑 §3.2b 自查。
    本条收敛得出：**enjoy 后面接"时光"类名词时要带物主代词**。
- 2026-08-27 ✅ 付息日 a 段（补建后首测）· `I really enjoy **my time** with him thaty day.`
  ——考点位置（time 前面放什么）给的是 **my**，08-25 的 `the time` 换掉了
  ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ⚪ 同句 `enjoy` 应为 **enjoyed**（"那天"是过去）—— **形态类·时态标记，只做记号**，
    落在已有号 **#12**，不记 ❌、不影响本条档位（§3.4⑤：中译英复习里掉了只做记号）
  ★ `thaty` → that ｜拼写，§2.1 不算错
  ★★ 补建的价值第二次兑现（同 #300）
- 2026-08-28 ✅ 复习第3组 · `I really enjoy **my time** with him that day.`
  ——`enjoy my time`（物主代词，不是 the time）一字不差 ⇒ 连对2，**毕业**
  ⚪ 同句 enjoy → enjoyed（that day ＝ 过去）＝ **#12** 形态类只记号，**与 08-27 同一处、连续两天同一漏**
- 2026-09-11 ❌ 复检 · 付息日 a2 第 5 组 · `enjoy the time with him` ⇒ **回潮**
  最小改 `enjoy my time with him`
  ❌ enjoy 后面接"时光"时 time 前面要**物主代词**（enjoy my time／your stay／our evening），⛔ 不是 the；
    `the time` 只在后面有限定语时成立（I enjoyed the time **we spent together**）。
  ★ 08-26 建号的触发句就是 `enjoy the time`，今天原样掉回来 ⇒ 这一格没长稳
- 2026-09-13 ❌ 学习日 在池第 2 组 · `enjoy the time with him`
  最小改 `enjoy my time with him`
  ❌ enjoy 后面接"时光"要挂**物主代词**：enjoy **my／your／his** time ／ enjoy your stay；the time 正是本条要她别说的那一格（09-11 回潮后首测又掉）
- 2026-09-15 ✅ 学习日 在池第 2 组 · `enjoy my time with him` —— enjoy ＋ 物主代词 ＋ time；连错2 → 连对1
- 2026-09-18 ✅ 学习日 在池第 1 组 · `enjoy my time wth him.`——enjoy **my** time（wth 拼写不算）⇒ **连对 2，毕业**
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"⛔ spending"，点名 enjoy，my／the 留给她（她掉过两次的就是 enjoy the time）；换成海边度假场景
- 2026-10-01 📝 题面补点名「"住的几天"用 **stay** 说」· 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  只点 enjoy 时 `I really enjoyed staying by the sea` 同样合法，绕开"物主代词 ＋ 时光名词"这一格 ⇒ 点名名词 stay，my／the 仍留给她
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [6] · `I really enjoyed my stay at the beach this time.` —— enjoyed my stay（物主代词，没落成 the stay）


### 302 · something breaks（东西坏了／出故障，break 当不及物动词，不用 be broken）
类型 搭配 ｜ 新建 2026-08-26（**她当场指定**）
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
**something breaks**（东西坏了／出故障，break 当**不及物**动词，⛔ 不用 be broken）。
判据：
```
break 当**不及物**动词 ＝ 那个东西自己坏掉／出故障，主语就是那个东西，不用被动：
   ✅ Whenever something breaks, …        ✅ My laptop broke last week.
   ✅ The washing machine keeps breaking.  ✅ If anything breaks, just call me.
   ✗ Whenever something is broken, …（这是"已经是坏的"这个状态，不是"坏掉"这个动作）
★★ 三个都对应中文"坏了"，方向不同，别混：
   · something breaks   ＝ 坏掉这个**动作/事件**（本条）——用在 whenever／when／if 后面最自然
   · it's broken        ＝ 现在**是坏的**这个状态（The printer is broken. 打印机现在坏着）
   · it broke down      ＝ 机器/车/系统**整个罢工**（My car broke down on the way.）
★ 同族（同样"东西自己出事"，全不用被动）：it stopped working ／ it crashed ／
  something goes wrong（更泛：出岔子，不限于东西）
★ 判据一句话：**中文"坏了"是在说一件事发生了 ⇒ 用 break；在说现在什么样 ⇒ 用 is broken**
```
★ 与 **#304**（turn to sb）的分工：那是"去找谁"那一格 ⇒ 本条题面 08-27 已整句换掉，两条不互相泄题。
★ 边界（08-28 实证）：**块调得出来 ≠ 盖得住那句** —— 她在 #304 的题里写 `If something breaks, …`，
　形式对但语义用错了地方（题面是"遇到麻烦"，不是"东西坏了"）。

**怎么发现的**
2026-08-26 新建 · **她主动提出**（§2③）· 自由产出（新题 bank:244 P2）· 她自己写出
`Whenever something breaks, he is the kind of person everyone turns to` —— 用得准，不是错。
★ 她的原话："这整句话 break, the kind of, turn to 都可以新建个条目"
判重（当天新建复核，§4④1b ⛔ 严禁脚本批量判 —— grep 只捞候选，判断逐条人读）：
　① 目标英文形式 ＝ `something breaks`
　② grep `broken`／`break`／`坏`／`故障`／`出问题` 全库（含已毕业）→ **1 处命中**，逐条读：
　　 · 🎓 那条题面"这事儿好坏参半。"（旧号 B183）—— 只是中文"坏"字撞了，考点是
　　　 "好坏参半"那个词组 ⇒ **无关**
　③ 与最接近的条目的区别：全库**没有**管 break/be broken 的条目 ⇒ 无最接近项
　⇒ **保留新建**。

**我错在哪**
她这次没有错（`Whenever something breaks, …` 是她自己产出的、不及物用法一次到位），
建号理由是 §2③ **她点名要学**（同一句她一次点了三个条目：break／the kind of／turn to）。
找法：中文"坏了"出口前分一下 —— 说的是**一件事发生了** ⇒ `something breaks`；
说的是**现在什么样** ⇒ `it's broken`。

**题面**
"家里的东西一坏，我就自己上网查怎么修。"（"坏"用 **break** 说）
★ ⛔ 题面不带"去找某人"的意思 —— 那是 #304（turn to sb）的考点，两条互不泄题

- 2026-08-26 新建 · **她主动提出**（§2③）· 自由产出（新题 bank:244 P2）·
  `Whenever something breaks, he is the kind of person everyone turns to`——用得准，不是错
- 2026-08-27 ✅ 付息日 a 段（题面当天整句改后首测）· `If something breaks,  just call me.`
  ——break 当不及物动词，没走 is broken；**与判据里的原型句逐字相同**
  ⇒ **连对 0 → 1（差一次毕业）**
  ★ 今天改题面的收益：旧题面"…大家都**去找他**"会把 **#304（turn to sb）** 的答案先泄出去；
    改成判据原型句后两条互不干扰，同一组里 #302 和 #304 都独立命中
- 2026-08-28 ✅ 复习第1组 · `if **anything breaks**, just give me a call.`
  ——break 用作不及物、没写 is broken；if 从句里 anything 比 something 还更贴 ⇒ 连对2，**毕业**
- 2026-08-28 ⚪ **同日再现·观察行（不改已毕业状态）** · 复习第3组 #304 句里 · `If something breaks, …`
  ——形式对，但**语义用错了地方**（题面是"遇到麻烦"，不是"东西坏了"）。
  ★ 这是本条第一次出现"块调得出来、但盖不住那句"的证据 ⇒ 见 #304 的同日日志
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 5 组（她原话："10. 直接过"）
- 2026-09-15 📝 新题 bank:1059 · `the network connected with my office broken` 教练原判 ❌（something breaks）⇒ **她当场判定手滑、撤销**
  原话："这两个条目都不用建（手滑）" ⇒ §2 当场撤、不记档位、⛔ 不回潮；状态行一个字不动
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [3] · `If something breaks, just give me a call.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"不用 broken"，点名 break；换成东西坏了自己上网查场景（照旧不带"去找某人"，与 #304 互斥）


### 303 · sb is the kind of person ＋ 关系从句（形容一个人是"那种人"）
类型 结构 ｜ 新建 2026-08-26（**她当场指定**）
状态 连对2 连错0 上次2026-09-15 ｜ **🎓 已毕业 2026-08-28**（连对2 · **主语位和宾语位两半都验过**）｜ 题型 整句

**问题是什么**
**sb is the kind of person ＋ 关系从句**（形容一个人是"那种人"）。
判据：
```
框架 ＝ **sb is the kind of person ＋ 关系从句**（who/that 常省）
   ✅ He's the kind of person everyone turns to.       ✅ She's the kind of person who never gives up.
   ✅ I'm not the kind of person who complains.        ✅ He's the sort of person you can rely on.
★ **前面必须有 the**（the kind of person），但 person 前面不加冠词（＝ 🎓#106 那条：
  kind of ＋ 单数名词、不带冠词）
★★ **who/that 什么时候能省** —— 看那个人在从句里当主语还是宾语：
   · 当**宾语** ⇒ 可以省：the kind of person (that) everyone turns to ／
                        the sort of person (that) you can rely on
   · 当**主语** ⇒ **不能省**：the kind of person **who** never gives up
★ sort 可以换 kind，意思一样（sort 更英式、更口语）
★ 用处：P2「描述一个人」和 P3「什么样的人…」两栏的万能句 —— 一句话给出人物定性
★ 互斥（§3.1 第三档）：🎓#106 管的是 kind of 后面**名词的形式**（单数、不带冠词），
  🎓#230 管的是提问用 what kind of；**本条管的是整句框架 ＋ 后面挂关系从句** ⇒ 题面不撞车
```
判据一句话：这是一句**人物定性**吗？是 ⇒ `he's the kind of person …`，再看从句里那个人是主语（who 不能省）还是宾语（可省）。
★ 与 **#304**（turn to sb）的分工：那是"去找谁"那一格 ⇒ 本条题面两次都避开"去找"，同组不互相泄题。

**怎么发现的**
2026-08-26 新建 · **她主动提出**（§2③）· 自由产出（新题 bank:244 P2）· 她自己写出
`he is the kind of person everyone turns to` —— 关系代词省对了、紧贴、陈述语序，不是错。
（同一句她一次点了三个条目：break／the kind of／turn to，见 #302 的原话。）
判重（当天新建复核，§4④1b ⛔ 严禁脚本批量判）：
　① 目标英文形式 ＝ `the kind of person (who) …`
　② grep `kind of`／`sort of`／`type of`／`这种人`／`那种人` 全库（含已毕业）→ 3 处命中，逐条读：
　　 · **🎓#106**（kind of / sort of / type of ＋ 单数名词，不带冠词）—— 决定性证据：
　　　 按 #106 的规则去改，得到的还是 `kind of person` 这两个词，
　　　 **它给不出"he's the kind of person everyone turns to"这个整句框架**
　　　 ⇒ #106 给不出本条的答案 ⇒ 不是同一条规则（同 #295 vs 🎓#236 的判法）
　　 · **🎓#230**（"什么样的" ＝ what kind of）—— 那是**提问**形式，本条是**陈述**框架 ⇒ 无关
　　 · 🎓#265 备注里的 `this kind of tea is good for your health`——只是例句里含 kind of ⇒ 无关
　⇒ **保留新建**。

**我错在哪**
她这次没有错（`he is the kind of person everyone turns to` 关系代词省得对），
建号理由是 §2③ **她点名要学**。
找法：说完 the kind of person，看后面那个人在从句里干什么 —— **当主语 ⇒ who 不能省**；
当宾语 ⇒ 省不省都行。

**题面**
**点名**："他就是那种谁都信得过的人。"（用 **the kind of person** 那个框架说）
★ 题面 2026-08-27 整句改（§6.5 审核项 8 题面撞车）：原题面"…大家有事都**去找**的人"含 **#304（turn to sb）的考点**，同组出会互相泄题。新题面换成**主语位关系从句**（who never gives up）——顺带把本条更难的那一半测到了：从句里那个人当**主语** ⇒ **who 不能省**（原题面那种当宾语的才可省）
★ 题面 2026-08-28 换成**宾语位从句**（08-27 用的是主语位 who never gives up，宾语位那一半从没验过；旧稿"他就是那种大家有事都会去找的人"因和 #304"去找"撞车弃用）

- 2026-08-26 新建 · **她主动提出**（§2③）· 自由产出（新题 bank:244 P2）·
  `he is the kind of person everyone turns to`——关系代词省对了、紧贴、陈述语序，不是错
- 2026-08-27 ✅ 付息日 a 段（题面当天整句改后首测）· `he is the kind of person who never gives up`
  ——三格全中：整句框架 ／ person 前不加冠词 ／ **who 没省**（从句里那个人当主语，本来就不能省），
  外加 gives 的 -s 也对 ⇒ **连对 0 → 1（差一次毕业）**
  ★ 改题面的额外收益：为了避开与 #304 撞车才换成主语位从句，结果**顺带把本条更难的那一格
    测掉了**。⇒ **下次出题回到宾语位那句**（"他就是那种大家有事都会去找的人。"），
    两半都验过就更稳（那时 #304 别同组出）
- 2026-08-28 ✅ 复习第1组（**题面当天换成宾语位从句后首测**）· `He's **the kind of person everyone trusts**.`
  ——关系代词省略正确（the kind of person (who/that) everyone trusts）⇒ 连对2，**毕业**
  ★★ 这是"两半都验过才毕业"：08-27 验主语位（who never gives up，who 不能省），
     08-28 验宾语位（可省，她也确实省了）—— 不是半边过关就放走
  ★ 08-27 收尾写的旧稿"他就是那种大家有事都会去找的人。"**弃用**：与 #304"去找"撞车（§6.5 项 8）；
    换成"谁都信得过的人"同样是宾语位，且与全库零重叠
- 2026-08-28 ⚪ **同日再现·观察行（不改已毕业状态）** · 复习第3组 #304 句里 ·
  `he is **the kind of person everyone turns to**`——宾语位从句第二次，形也对
  （同场 priming 下的复用，不算独立命中）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（她原话："1-4 直接过"）
- 2026-09-15 ✅ 新题 bank:1059 自发命中 · `he's the kind of person everyone turns to`（the kind of person ＋ 关系从句）


### 304 · turn to sb (for sth)（有事去找某人／求助）
类型 词组 ｜ 新建 2026-08-26（**她当场指定**）
状态 连对2 连错0 上次2026-09-15 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

**问题是什么**
**turn to sb (for sth)**（有事去找某人／求助）。
判据：
```
turn to sb ＝ 遇到麻烦时**去找某人**（求助、要主意、要支持）
   ✅ Everyone turns to him.              ✅ He's the first person I'd turn to.
   ✅ She turned to her sister for advice. ✅ I didn't know who to turn to.
★ 介词写死：turn to sb **for** sth（for advice／for help／for support）
★★ 边界（同一个 turn，三件事，别混）：
   · turn **to** sb        ＝ 去找人求助（本条）—— 不可分离，人跟在 to 后面
   · turn sth **off**／turn it off ＝ 关掉（**可分离**，代词必须放中间 ＝ 🎓#67）
   · turn **up**          ＝ 露面／出现（He never turned up.）
★ 同族（一起记，语气不同）：go to sb (for help)（最平）／ ask sb for help（最直白）／
  lean on sb（偏情感依靠）／ count on sb（偏"靠得住"）
★ 判据一句话：**中文"有事找他"⇒ turn to him；"打电话找他"那种单纯联系用 call/contact，不用 turn to**
```
★ 与 🎓**#67**（可分离动词短语的位置）的分工：#67 管**位置**（代词放中间），本条管**这个词组本身**
　（不可分离 ＋ 介词 for）—— turn to 正好是 #67 的反例。
★ 与 🎓**#302**（something breaks）的分工：题面已于 08-27 隔开；但 08-28 实证**同场 priming 隔不开**
　（她把第 1 组的 `If something breaks` 搬进了第 3 组本条的句子里）。

**怎么发现的**
2026-08-26 新建 · **她主动提出**（§2③）· 自由产出（新题 bank:244 P2）· 她自己写出
`he is the kind of person everyone turns to` —— 用得准，不是错。
判重（当天新建复核，§4④1b ⛔ 严禁脚本批量判）：
　① 目标英文形式 ＝ `turn to sb`
　② grep `turn`／`for help`／`求助`／`依赖` 全库（含已毕业）→ 4 处命中，逐条读：
　　 · **🎓#67**（可分离动词短语的位置：put it away／turn it off）—— 决定性证据：
　　　 按 #67 的规则去改，得到的是"代词放中间"（turn him to？）——**根本不成句**
　　　 ⇒ #67 给不出本条的答案；且 turn to 是**不可分离**的，正好是 #67 的反例 ⇒ 两条规则
　　 · 🎓 `It depends on whether he turns up.` —— 那是 turn up（露面），例句里的另一个词组 ⇒ 无关
　　 · 🎓 `watch pictures on the screen turn into real objects` —— turn into（变成）⇒ 无关
　　 · #291 备注里的 `I'll ask him for you.` —— 那是 Let me／I'll 的例句 ⇒ 无关
　③ 与最接近的条目的区别：#67 管**位置**（可分离动词），本条管**这个词组本身**（不可分离＋介词 for）
　⇒ **保留新建**。

**我错在哪**
她这次没有错（`everyone turns to him` 是她自己产出的、介词一次到位），建号理由是 §2③ **她点名要学**。
找法：中文"有事去找他"先分一下 —— 是**求助**吗？是 ⇒ turn to sb（要东西时挂 **for**）；
只是联系一下 ⇒ call／contact，⛔ 别用 turn to。

**题面**
"我心情不好的时候，第一个想去找的就是我姐。"（"去找"用 **turn** 说）
★ ⛔ 题面不带"东西坏了"的意思 —— 那是 #302 的考点；同场尽量别排在一起（08-28 同场 priming 过一次）

- 2026-08-26 新建 · **她主动提出**（§2③）· 自由产出（新题 bank:244 P2）·
  `he is the kind of person everyone turns to`——用得准，不是错
- 2026-08-27 ✅ 付息日 a 段（题面当天微改后首测）·
  `Everyone turns to him when they are in trouble.`——介词 **to** 一字不差
  ⇒ **连对 0 → 1（差一次毕业）**
  ★ 教练自审留痕：`Everyone … they` 差点被判单复数不一致 —— 试造母语句推翻自己：
    `Everyone turns to him when they're in trouble.` 母语者照说：everyone 谓语走**单数**
    （turns ✅ 她做对了），回指代词走 **singular they** ⇒ **完全正确，假错未判**
    ★ 判据备查：everyone／somebody／nobody 回指一律可以用 they
  ★ 她把中英语序倒过来了（中文"遇到麻烦的时候…去找他"／英文主句在前）——
    **主动重排**不是照搬，英语里主句在前更自然 ⇒ 加分，未改
- 2026-08-28 ✅ 复习第3组 · `If something breaks, he is **the kind of person everyone turns to**.`
  ——`everyone turns to` 一字不差 ⇒ 连对2，**毕业**
  ⚠️ 前半 `If something breaks` —— "遇到麻烦"被收窄成"东西坏了"（break ＝ 物理损坏）
     ⇒ 更好版 `When something goes wrong, he's the kind of person everyone turns to.`
  ⚪ 同句两处是**今天第 1 组刚毕业的块**：🎓#302 `If something breaks` ＋ 🎓#303 `the kind of person…`
     —— 同场 priming 下的复用，记观察行，不改状态
  ★★ **教练侧发现**：题面层面已经把 break 和 turn to 隔开了（08-27 改的），
     **但同一场里跨组的 priming 隔不开** —— #302 在第 1 组、本条在第 3 组，块照样搬过来
     ⇒ 见 sessions/2026-08-28.md 的教练提案（等她裁，未写进任何规则）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 5 组（第 11 题整串，她事后补的原话："11直接过"）
- 2026-09-15 ✅ 新题 bank:1059 自发命中 · `he's the kind of person everyone turns to`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 turn，to 留给她；换成心情不好找姐姐场景（不带"东西坏了"，与 #302 互斥）


### 305 · stay patient（keep ＋ 形容词只跟一小撮词，patient 不在里面）
类型 搭配 ｜ 新建 2026-08-26
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ **keep 族·一组最多 2 条**（c 段 2026-08-27 加）｜ 题型 整句

**问题是什么**
**stay patient**（keep ＋ 形容词只跟一小撮词，**patient 不在里面**）。
判据：
```
**keep ＋ 形容词**（后面不带宾语）只跟一小撮固定的词，是个**封闭名单**：
   ✅ keep calm ／ keep quiet ／ keep still ／ keep busy ／ keep warm ／ keep safe ／
      keep healthy ／ keep fit ／ keep dry
   ✗ keep patient   ✗ keep positive   ✗ keep focused
"一直保持耐心" ⇒ **stay patient**（也可 be patient ／ remain patient）
★★ **判据一句话（这条才是要背的）：拿不准用 keep 还是 stay ⇒ 一律先用 stay。**
   stay 的名单大得多，几乎不出错：stay calm／stay positive／stay focused／stay awake／
   stay healthy／stay safe／stay patient
★ 边界一：`keep his cool` **是对的** —— 那是 keep ＋ **名词**（cool 在这里是名词）的固定块，
  和"keep ＋ 形容词"不是一件事。她同一句前面就用对了
★ 边界二：与 **#297**（keep ＋ **宾语** ＋ 形容词，keeps your mind active）不是一条 ——
  那条有宾语，本条没有；按 #297 改会得到 `keeps himself patient`，**也不是母语者的说法**
★ 检查触发：说完 keep ＋ 一个形容词，问一句"这个词在 calm/quiet/busy/warm/safe/fit 那个名单里吗？"
  不在 ⇒ 换 stay
```
★ **keep 三兄弟交叉引用**：**#287** keep ＋ 宾语 ＋ **-ing**（keep the cars flowing）／
　**#297** keep ＋ 宾语 ＋ **形容词**（keep your mind active）／
　**#305（本条）** keep ＋ **形容词**（无宾语）—— 这一格是**封闭名单**，patient 不在里面
　⇒ 出题时三条里最多同组出两条
★ 与 🎓**#156**（同根词的形态：patience 名词 vs patient 形容词）的分工：那条管**词形**，
　本条管**选哪个动词**（keep→stay）—— 她本来就用的是形容词 ⇒ #156 给不出本条的答案。

**怎么发现的**
2026-08-26 ❌ 首犯 · 自由产出（新题 bank:244 P2 Describe a friend from your childhood）· 她写
`he nerver panics and **keeps patient**`（→ never panics and **stays patient**）。
判重（当天新建复核，§4④1b ⛔ 严禁脚本批量判 —— grep 只捞候选，判断逐条人读）：
　① 目标英文形式 ＝ `stay patient`（keep ＋ 形容词的名单边界）
　② grep `keep patient`／`stay patient`／`耐心`／`keep calm`／`keep fit`／`keep busy` 全库
　　（含已毕业）→ 2 处命中，逐条读：
　　 · **🎓#156** 题面"他的耐心让我印象很深。／他一直很有耐心。"—— 那条考的是
　　　 **同根词的形态**（the difference／different；patience 名词 vs patient 形容词），
　　　 决定性证据：按 #156 的规则去改，得到的是"这里该用形容词 patient"——**她本来就用的是
　　　 形容词**，#156 给不出 keep→stay 这个答案 ⇒ 不是同一条规则
　　 · **#297** 备注里的 `keep fit／keep busy` 例句 —— 那是本条的名单，但 #297 的考点是
　　　 **带宾语**的 keep ＋ O ＋ adj（见上"边界二"）⇒ 两条，题面互斥
　　　（#297 题面 "学点东西能让脑子保持活跃"／本条题面 "他从来不慌，一直很有耐心"）
　⇒ **保留新建**。

**我错在哪**
她的：`he nerver panics and **keeps patient**`　　正确：`never panics and **stays patient**`
找法：说完 keep ＋ 一个形容词，问一句 —— **这个词在 calm／quiet／busy／warm／safe／fit 那个名单里吗？**
不在 ⇒ 换 **stay**（拿不准一律先用 stay）。

**题面**
"带小孩得一直保持耐心，急也没用。"（"耐心"用 **patient** 说）
★ stay／remain／be patient 都算对；她掉过的错路是 keeps patient

- 2026-08-26 ❌ 首犯 · 自由产出（新题 bank:244 P2 Describe a friend from your childhood）·
  `he nerver panics and **keeps patient**` → never panics and **stays patient**
- 2026-08-27 ✅ 付息日 a 段（题面当天改点名后首测）·
  `he always keeps his cool and stay patient.`——**没走 keep patient，用的是 stay patient**，
  本条真正要的那一格命中 ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ⚪ `stay` 应为 **stays**（and 后面同主语要同形）—— **形态类·主谓一致，只做记号**，
    落在已有号 **#10**，不记 ❌、不影响本条档位
    ★ 检查触发：**and 后面还有一个动词时，回头看它跟不跟前面那个同主语**——同主语就得同形
  ★★★ **本条最值钱的一条证据**：她在**同一句话里**同时用对了 `keep ＋ 名词`（his cool）和
    `stay ＋ 形容词`（patient）—— 昨天建条目时写进判据的那条**边界一**（keep his cool 是对的、
    keep patient 不对），她隔一天就把两边分开用了 ⇒ **判据本身进去了，不是背了个词**
  ★★ **今天改点名的收益当场验证**：旧点名直接写 stay ＝ 把考点（keep 还是 stay）整个交出去；
    改成点结构（一个动词 ＋ patient，不用 is/be）之后，`keeps patient` 那条错路仍开着，她**没走**
  ★ `从来不慌` 她译成 `always keeps his cool`（正说代反说）—— 合法改写，意思对上，未改
- 2026-08-28 ✅ 复习第3组 · `he never panics and **stays patient**.`
  ——动词 ＋ patient，没用 is／be；`keeps patient` 那条错路仍开着、她第二次没走 ⇒ 连对2，**毕业**
  ⚪ **正面观察**：`stays` 的 -s 带上了（#10）—— 08-27 同一道题写的是 `and **stay** patient`，今天补上
  ⚠️ `never panics and stays patient` —— never 的否定辖域会盖到 and 后面那个动词
     ⇒ 更好版 `He never panics; he always stays patient.`；**不建条目**（她没写错，只是有歧义），列入观察
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `stayed patient the whole time` —— 动词 ＋ patient，⛔ 没走 keep、⛔ 没用 is／be
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 去形态描述）· 题型 词组 → 整句
  去掉"一个动词 ＋ patient／不用 is／be"，只点名 patient；stay／remain／be patient 都算对，逼的是她掉过的 keeps patient；换成带小孩场景


### 306 · not just A — it's more B（"不只是A，更多的是B"：中间不能用 and）
类型 结构 ｜ 新建 2026-08-27
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-08-29**（连对2）｜ 题型 整句

**问题是什么**
**not just A — it's more B**（"不只是A，更多的是B"：**中间不能用 and**）。
判据：
```
"不只是 A，更多的是 B"这个框架，中间**不能用 and**：
   ✅ It's not just about A — **it's** more about B.      ← 最口语（破折号 ＋ 重起一个 it's）
   ✅ It's not just about A, **but** more about B.        ← but 也行
   ✅ It's **not so much** about A **as** about B.        ← 更正式一点
   ✗ It's not just about A, **and** more about B.
★ 判据一句话：**前半句一出现 not just／not only，后半句就必须由【but】或【重起的 it's】接**
  —— and 是"并列再加一条"，接不住"否定 → 修正"这个转折
★ 同族（同一个框架的其它壳）：
   It's not that A, it's more that B.        ／  Less about A, more about B.
   A is part of it, but the real thing is B.
★ 用处 ＝ **P2/P3 收尾拔一层的标准动作**（"不只是……，更多的是……"）——
  她 R5 这一句的**立意是全篇最高的一层**，只是连词接错了，值得单独焊住
```
★ 全库**没有**别的条目管这个相关连词框架 ⇒ 无最接近项（判重见下）。

**怎么发现的**
2026-08-27 ❌ 首犯 · 付息日 d 段重答（R5）· 她写
`It's not just about the food itself, **and** more about a reason bringing my family together.`
（→ It's not just about the food itself **— it's** more about…）。
判重（当天新建复核，§4④1b ⛔ 严禁脚本批量判 —— grep 只捞候选，判断逐条人读）：
　① 目标英文形式 ＝ `not just A — it's more B`
　② grep `not just`／`not only`／`but also`／`不只是`／`不仅仅`／`而是更` 全库（含已毕业）
　　 → **3 行命中**，逐条读：
　　 · 🎓#52 的日志例句 `parent should explain why, not just what, to kids` —— 只是例句里
　　　 恰好含 not just，#52 的考点是"去掉 X is important 的壳" ⇒ 无关
　　 · 🎓#52 同一处的讲评行 ⇒ 同上
　　 · sessions 引文 `That is not just that one time` ⇒ 是记录不是条目
　③ 与最接近的条目的区别：全库**没有**管这个相关连词框架的条目 ⇒ 无最接近项
　⇒ **保留新建**。

**我错在哪**
她的：`It's not just about the food itself, **and** more about a reason bringing my family together.`
正确：`It's not just about the food itself **— it's** more about …`（或 `, **but** more about …`）
找法：句子里一出现 **not just／not only**，就盯住后半句的接头 ——
**只能是 but，或重起一个 it's**，⛔ 不能是 and。

**题面**
**点名**："旅行不只是去看风景，更多的是换个环境放松一下。"（用 **not just … it's more …** 说完）
★ 题面 2026-08-28 换话题（旧稿"过年这事儿不只是吃，更多的是一家人聚一聚"与 #236 回潮复测题面"过年更多的是给全家一个聚一聚的理由"内容几乎重合，同日出会互相污染）

- 2026-08-27 ❌ 首犯 · 付息日 d 段重答（R5）·
  `It's not just about the food itself, **and** more about a reason bringing my family together.`
  → It's not just about the food itself **— it's** more about…
- 2026-08-28 ✅ 复习第2组（**新建次日进池首测，题面当天换话题避开与 #236 撞车**）·
  `Travel is not just seeing the sights**;** it's more about relaxing in different environment.`
  ——中间用**分号 ＋ 重起的 it's**，不是 and ⇒ **08-27 掉的那一格今天没再掉**，连对0 → **1**
  ⚠️ 同句 not just seeing／it's more about relaxing 两半不同形 ⇒ 更好版补成 not just **about** seeing（并列同形）
  ⚪ 同句 `in different environment` → in **a** different environment ＝ #56（形态类，只记号）
- 2026-08-29 ✅ 复习第1组 · `travel is not just about seeing sights —— it's more about relaxing in a different environment.`
  ——中间用**破折号 ＋ 重起的 it's**，不是 and ⇒ 连对1 → **连对2，毕业**
  ★ 比 08-28 那版更整齐：两边都用 about（not just **about** seeing／it's more **about** relaxing）
    ⇒ 08-28 diff-2 给的"并列同形"当场用上了
  ⚪ 同句 `in a different environment` —— 08-28 这里漏了冠词（记过 #56 的 ⚪），今天补上了
     ⇒ **#56 记一条正面 ⚪**（形态类只记号，不动状态行）
  ⚠️ 同句 `seeing sights` → seeing **the** sights（see the sights 是整块，the 是词组的一部分；
     裸复数 sights 会被读成"一些景象"）—— 只进 diff-2，**不记 ❌、不建条目**：
     §3.4 执行自查「同一篇里她有没有把同一个形态做对过？」→ 本篇 the difference／a bit of money／
     a different environment／the entire family 四处冠词全对，且 08-27 本条日志里她写的就是 `the sights`
     ⇒ 属"产出时检查没跑"，不是缺口
- 2026-09-11 ✅ 复检 · 付息日 a2 第 4 组 · `Traveling is not just about the scenery; it's more about a change of environment to relax.` —— not just … it's more … 完整，中间没塞 and
  ⚠️ 顺带：a change of environment to relax → a change of scene to help you relax（to relax 悬着）
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [4] · `Traveling is not just about seeing the sights; it's more about getting to chill in a new environment.`

### 307 · That's how ＋ 主谓（"这样一来他们才会…／就是这么来的"）
类型 结构 ｜ 新建 2026-08-28（**她当场指定**）
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-08-30**（连对2 · **毕业那次已换句**）｜ 题型 整句

**问题是什么**
**That's how ＋ 主谓**（"这样一来他们才会…／就是这么来的"）。
判据：
```
用途 ＝ 把**前面说的做法**和**它带来的结果**焊在一起，一句话收口。
形状 ＝ That's how ＋ 【陈述语序的主谓】
   ✅ That's how they learn to take ownership.
   ✅ That's how it works.　　✅ That's how I got into it.
   ✗ That's how do they learn.（里面不许用疑问语序 —— 那一处归 🎓#59，不归本条）
★ 同族（一个族，先只立 how 这一个壳）：
   That's why ＋ 主谓（给原因）　／　That's what ＋ 主谓（给内容）
   ⇒ 以后她要 why／what 那两个壳，各自单开号，不并进本条（§3.1 一条 ＝ 一个考点）
★ 用处 ＝ P3 里"给完机制之后收口"的标准动作：先说做法，再 That's how ＋ 结果
```
★ 与 🎓**#283**（It's really about A first, and then B）／**#290**（… depending on who you ask）的分工：
　那两条是**别的收尾块**（排先后／同一现象不同理由），本条是"做法 → 结果"的因果收口。
★ 与 🎓**#59**（嵌入疑问用陈述语序）的**互斥关系写死**：她若写成 `That's how do they learn`，
　那一处判 #59，⛔ 不判本条。

**怎么发现的**
2026-08-28 新建 · **她主动提出**（§2③）· 复习第 2 组 #282 句里 · 她写
`That's how they learn to take ownership.` —— 她这一句**是用对了的**，建条目是因为她主动要
（同 #299 那种情况），不是因为犯错。
★ 她的原话："That's how(这才可以建个条目) they learn to take ownership."
判重（当天新建复核，§4④1b ⛔ 严禁脚本批量判 —— grep 只捞候选，判断逐条人读）：
　① 目标英文形式 ＝ `That's how ＋ 主谓`
　② grep `That's how`／`that's how`／`That's why`／`这就是`／`收尾块`／`收尾句型` 全库（**含已毕业**）
　　 → 命中逐条读：
　　 · **#282 自己 08-23 的日志行**（`that's how they'll learn to take ownership of…`）
　　　 —— 这个块**第一次出现却没建号**，正是今天补的这一条；#282 只管 take ownership
　　 · 🎓#283（It's really about A first, and then B）—— 把几点**排成先后**，不是"做法 → 结果"
　　 · #290（… for totally different reasons depending on who you ask）—— 同一现象不同理由，不是因果收口
　　 · 🎓#59（嵌入疑问用陈述语序）—— 管的是 how／what 从句**怎么排语序**，不管"这个块什么时候用"
　　　 **互斥关系写死**：她若写成 `That's how do they learn`，那一处判 #59，不判本条
　③ 说得出差在哪：#283／#290 是**别的收尾块**（不同词组）｜#59 是**语序规则**（不同层）
　⇒ **保留新建**。

**我错在哪**
她这次没有错（`That's how they learn to take ownership.` 是她自己用对的），
建号理由是 §2③ **她点名要学**。
找法：P3 讲完一套做法，收口前问一句 —— 我要说的是"**这样一来就会…**"吗？
是 ⇒ `That's how ＋ 主谓`（里面**陈述语序**，⛔ 不许倒装）。

**题面**
**点名**："我当初就是这么开始的。"（用 **That's how** 起头说）
★ 08-29 那次与她建条目时说的句子逐字相同（含"昨天的记忆"），08-30 换成 `我当初就是这么开始的。` 壳照样调出来 ⇒ 毕业不是假毕业

- 2026-08-28 新建 · **她主动提出**（§2③）· 复习第2组 #282 句里 · `That's how they learn to take ownership.`
  ——她这一句**是用对了的**，建条目是因为她主动要（同 #299 那种情况），不是因为犯错
- 2026-08-29 ✅ 复习第1组（新建次日进池首测）· `That's how they learn to take ownership.`
  ——That's how ＋ 陈述语序主谓，一字不差 ⇒ 连对0 → **连对1**
  ⚠️ **出题约束（写死）**：这一句与她 08-28 建条目时说的那句**逐字相同** ⇒ 本次成绩里含"昨天的记忆"。
     **毕业那一次（连对2）必须换句打同一个考点**，否则是假毕业（同 #236 08-29 换句的理由）。
     备选题面：`这门手艺就是这么传下来的。`／`我当初就是这么开始的。`（That's how ＋ 主谓，换内容不换壳）
- 2026-08-30 ✅ 复习第1组 [2]（**毕业那一次，已按 08-29 写死的约束换句**）·
  题面 `我当初就是这么开始的。` · `That's how I got started in the first place.`
  ——That's how ＋ 陈述语序主谓，一字不差 ⇒ 连对1 → **连对2，毕业**
  ★★ **换句的必要性已兑现**：08-29 那次用的句子与她 08-28 建条目时说的那句**逐字相同**
     （`That's how they learn to take ownership.`），成绩里含"昨天的记忆"；
     今天换成完全不同的内容，**壳照样调出来了** ⇒ 毕业成立，不是假毕业。
  ★ 备选题面用的是条目里写好的第二句（`我当初就是这么开始的`），
    没选第一句（`这门手艺就是这么传下来的`）—— 后者要她同时处理"被动＋现在完成"，
    引入与考点无关的难度。
  ★ 她自己加的 `got started`（不是 started）：get ＋ 过去分词表"进入某状态"，比裸 start 更口语；
    `in the first place` ＝ "当初"的准确对应。两处都是她自己选的，不是题面给的。
  ★ 教练四问①留痕：一度想给更好版 `That's how I originally got started.`，
    **造母语句推翻了自己**（"My dad had an old PC lying around. That's how I got started in
    the first place." 中性叙述完全自然）⇒ 属 §7「⛔ 教练不必要的改动」，未发。
- 2026-09-11 ✅ 复检 · 付息日 a2 第 6 组 · `That's how I got start.` —— That's how ＋ 主谓，考点命中
  ⚪ got start → got **started**（get started 固定块的 -ed，形态类只记号 §3.4；同日 got stuck／got fined 都带对了 ⇒ 会，产出时检查没跑）
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [5] · `That's how I got started in the first place.`

### 308 · empty into ＋ 海／湖（河流"注入"某处的介词）
类型 搭配 ｜ 新建 2026-08-29
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-08-31**（连对2 ＝ 08-30 ＋ 08-31）｜ 题型 整句

**问题是什么**
**empty into** ＋ 海／湖（河流"注入"某处的介词）。
判据：
```
河流"注入／流进"某处 ⇒ 介词一律 **into**，不是 in。三个动词都配 into：
  ✅ The river **empties into** the sea.      ← 最正式、地理描述默认
  ✅ The river **flows into** the sea.        ← 最常用
  ✅ The river **runs into** the sea.         ← 最口语
★ 上位判据（可迁移到所有 in／into）：**句子里有"移动 / 进入"的意思 → into；只是说"在里面" → in**
  ✅ He walked **into** the room.（进去，有动作）　　✅ He's **in** the room.（在里面，静态）
  ✅ Pour it **into** the glass.                 ✅ It's **in** the glass.
★ 检查触发：写完一个介词，先问"这里在讲**位置**还是在讲**进去这个动作**？"
```
★ 与 🎓**#104**（bury yourself **in** sth，比喻义只配 in 不配 into）的分工 —— **最接近的一条**：
　按 #104 的规则改这句得到的是 `emptying in`（＝她写的错句）⇒ 给不出正确答案，方向还相反 ⇒ 两条。

**怎么发现的**
2026-08-29 ❌ 首犯 · 新题 P2（Describe an important river/lake）· 她写
`…spaning China from west to east and eventually emptying **in** the east China sea.`
（→ eventually emptying **into** the East China Sea）。
判重（新建当天复核，§4④1b ⛔ 严禁脚本批量判 —— dedup 只捞候选，判断逐条人读）：
```
① 目标英文形式 ＝ `empty into`
② `lab.py dedup into "in/into" 流进` → 命中 10 条（含已毕业），逐条读：
   · 🎓#104（bury yourself **in** sth，比喻义只配 in 不配 into）—— **最接近的一条**。
     **决定性证据**：按 #104 的规则改这句 ⇒ 得到 `emptying in`（＝她写的错句）
     ⇒ **给不出正确答案 ⇒ 不是同一条规则**。而且方向相反（#104 是"该 in 不该 into"）
   · 🎓#126（settle into）／🎓#34（in groups）—— 各自是别的固定词组
   · 🎓#87 #117 #164 #206 #289 #304 #307 —— 命中的都是历史行例句里恰好出现 into，不是考点
③ 说得出差在哪：#104 差在**词组不同、方向相反** ⇒ **保留新建**
```

**我错在哪**
她的：`eventually emptying **in** the east China sea`　　正确：`eventually emptying **into** the East China Sea`
找法：写完一个介词先问一句 —— **这里在讲"位置"还是在讲"进去这个动作"？**
有移动／进入 ⇒ **into**。

**题面**
"村口那条小河最后流进了一个大湖。"（"流进"用 **empty** 说）

- 2026-08-29 ❌ 首犯 · 新题 P2（Describe an important river/lake）·
  `…spaning China from west to east and eventually emptying **in** the east China sea.`
  → eventually emptying **into** the East China Sea
  ★ 同句另外两处**全对**，单独记：`spanning China from west to east`（分词逻辑主语＝river，挂得住）·
    `eventually` 的位置
- 2026-08-30 ✅ 复习第1组 [4]（**新建次日进池首测**）·
  `This river spans to east, eventually **emptying into** the East China Sea.`
  ——考点位置一字不差：**emptying into** ⇒ 连对0 连错1 → **连对1 连错0（差一次毕业）**
  ★ 08-29 首犯正是这一处（`emptying **in** the east China sea`），隔一天点名复测拿回。
  ★ 同句 span 那一处归 #18（见上），本条只管介词。
- 2026-08-31 ✅ 付息日 a 段第 1 组
  `this river runs all the way to east and **emptys into** the East China sea.`
  考点 empty **into** 一字不差命中 —— 08-29 首犯正是同一句的 `emptying **in** the east China sea`，
  隔两天点名复测拿回。emptys／East China sea 小写属拼写，不计错（§2.1）。
  ⇒ 连对2 · 达毕业线
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 4 组（打包串里，她原话："其他的直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 empty，into 留给她（她掉过的是 emptying in）；换成小河流进湖场景

### 309 · 推测过去 ＝ must have ＋ 过去分词
类型 语法 ｜ 新建 2026-08-29
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-08-31**（连对2 ＝ 08-30 ＋ 08-31）｜ 题型 整句

**问题是什么**
推测过去 ＝ **must have ＋ 过去分词**。
判据：
```
对**过去**的事下推测 ⇒ 情态词后面挂 **have ＋ 过去分词**，不是原形。三档一起记：
  must have been …    一定是（有把握）
  can't have been …   不可能是（否定的确信）
  might/could have been …  可能是（不确定）
★ 对照（同一个情态词，时间不同，形式不同）：
  ✅ He must **be** tired.        （现在看着他就累）
  ✅ He must **have been** tired. （那天他一定是累了）
★ 检查触发：写完 must／can't／might，先问一句 —— **我在猜的是"现在"还是"当时"？**
  当时 ⇒ 后面必须有一个 have。
★ 与 ⛔#147 的分工写死：**#147** 管"情态词后面动词一律原形"（must be，不是 must is）；
  **本条** 管"该不该在情态词后面插一个 have 进来"。两条互不覆盖
```
★ 与 🎓**#259**（完成时：have/has/had 之后一律用过去分词）的分工：那条管 have **后面**挂什么形式，
　管不到"该不该把 have 插进来" ⇒ 不同考点。
★ **不是形态类**（§3.4 自查）：`must have done` 是一个**结构**（要多插一个助动词），不是词尾标记
　⇒ 照常出题、照常走连击。

**怎么发现的**
2026-08-29 ❌ 首犯 · 新题 P2（Describe an important river/lake）· 她写
`When i was a kid, the water was super cloudy - it **must be** full of sand.`
（→ it **must have been** full of sand）。
★ 为什么是真错不是小毛病：`must be` 说的是**现在**，而她下一段刚说现在水已经清了
⇒ **同一篇里前后打架**。
判重（新建当天复核，§4④1b ⛔ 严禁脚本批量判）：
```
① 目标英文形式 ＝ `must have been`
② `lab.py dedup must 情态 "have been"` → 命中 10 条（含已毕业），逐条读：
   · ⛔#147（时态只标一次：did/will/should/can/must 一出现，后面动词一律原形）—— **最接近的一条**。
     **决定性证据**：按 #147 的规则改这句 ⇒ 得到 `must be`（＝她写的）
     ⇒ **给不出正确答案 ⇒ 不是同一条规则**（且 #147 是形态类·不出题，归它等于永远不测）
   · 🎓#259（完成时：have/has/had 之后一律用过去分词）—— 它管的是 have **后面**挂什么形式，
     管不到"该不该把 have 插进来" ⇒ 不同考点
   · 🎓#214（完成进行时 have been ＋ -ing）—— 目标形式不同（been ＋ -ing vs been ＋ 形容词/名词）
   · 🎓#130 #6 #143 #177 #60 #285 #294 —— 各自别的规则，与"对过去的推测"无关
③ 说得出差在哪：#147 差在**它只管原形、不管 have** ⇒ **保留新建**
```

**我错在哪**
她的：`the water was super cloudy - it **must be** full of sand.`
正确：`it **must have been** full of sand`
找法：写完 must／can't／might，先问一句 —— **我在猜的是"现在"还是"当时"？**
当时 ⇒ 后面必须插一个 **have**。

**题面**
**点名**："那时候他一定是太累了。"（用 **must** 说这个推测）

- 2026-08-29 ❌ 首犯 · 新题 P2（Describe an important river/lake）·
  `When i was a kid, the water was super cloudy - it **must be** full of sand.`
  → it **must have been** full of sand
  ★ 为什么是真错不是小毛病：`must be` 说的是**现在**（"现在它一定满是泥沙"），
    而她下一段刚说现在水已经清了 ⇒ **同一篇里前后打架**，不是可有可无的时态装饰
- 2026-08-30 ✅ 复习第1组 [5]（**新建次日进池首测**）· 题面 `那时候他一定是太累了。` ·
  `he must have been too tired.`
  ——考点位置一字不差：**must have been**（猜的是"当时"，have 插进来了）
  ⇒ 连对0 连错1 → **连对1 连错0（差一次毕业）**
  ★ 08-29 首犯正是这一处（`it **must be** full of sand`，讲的是童年），隔一天复测拿回。
  ★ 她省了题面的"那时候"（Back then）—— **不算错**：must have been 本身就锁定过去，
    时间信息在结构里。更好版里把 Back then 加回去，只是让听者更容易跟上时间平面。
- 2026-08-31 ✅ 付息日 a 段第 1 组
  `he must have been really tired.`
  考点 must ＋ have ＋ 过去分词 一字不差命中。中文"那时候"未落地 ⇒ 走更好版（At the time, …），不判错。
  ⇒ 连对2 · 达毕业线
- 2026-09-11 ✅ 复检 · 付息日 a2 第 5 组 · `He must have been exhausted back then` —— must **have been**，一字不差
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [6] · `At that time, he must have been tired.`

### 310 · all the way ＋ 方向／终点（"一路…"／"大老远…"）
类型 词组 ｜ 新建 2026-08-30（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-09-01**（连对2 ＝ 08-31 ＋ 09-01）｜ 题型 整句
　　★ 09-01 那次同句里的 `ran → came` 是**本条考点之外**的动词选择（⚠️ 不判 ❌、未新建号），不影响毕业

**问题是什么**
**all the way ＋ 方向／终点**（"一路…"／"大老远…"）。
判据：
```
all the way ＝ **把"整段距离／整个过程"标出来**，位置永远在动词或方向短语的前面。
  ✅ He walked **all the way** home.              （整段路都是走的，没坐车）
  ✅ The road goes **all the way to** the top.     （一直通到顶，中间不断）
  ✅ She came **all the way from** Beijing.        （大老远从北京来 —— 强调远）
  ✅ The river runs **all the way** east.          （一路向东）
★ 三个高频搭档，整块背：
  **all the way to ＋ 终点** ／ **all the way from ＋ 起点** ／
  **all the way ＋ 方向副词**（home／back／up／down／east）
★ 它加的是"力气/距离"这层意思，不是可有可无的装饰：
   He walked home.             ＝ 他走回家的（中性）
   He walked all the way home. ＝ 一路走回去的（远、费劲，说话人在强调这个）
★ 检查触发：说完一个"从 A 到 B"的移动，问一句 —— **我想不想强调"整段／大老远"？**
  想 ⇒ 在动词后面塞 all the way。
```
★ 与 🎓**#131**（go ＝ 在程度轴上移动）的**互斥关系写死**：`go all the way` ＝ **程度义**
　（做到底、豁出去）⇒ 归 #131；`all the way ＋ 方向／地点` ＝ **空间义**（整段距离）⇒ 归本条。
★ 与 🎓**#223**（肯定句里的 far → a long way）的**互斥写死**：只说距离远 ⇒ a long way（#223）；
　强调整段／大老远 ⇒ all the way（本条）。
★ 与 **#311**（V ＋ its way）的分工：本条说"**整段都**"（有多远／多费劲），#311 说"**怎么过去的**"。

**怎么发现的**
2026-08-30 📝 新建 · **她当场指定**（§2③）· 复习第 1 组 [4] 的更好版里教练给了
`This river **runs all the way east** and eventually empties into the East China Sea`，
她当场说："run all the way，这个 **all the way** 或者 **its way** 我不太主动会用，也建一个条目吧"。
★ 她**没有产出过错句** —— 本条是"**教练给的更好版本**"进池（零遗漏原则），不是她犯的错。
★ 她原话里并列提到的第二样（its way）**另开 #311**。
判重（新建当天复核，§4④1b ⛔ 严禁脚本批量判 —— dedup 只捞候选，判断逐条人读）：
```
① 目标英文形式 ＝ `all the way ＋ 方向／to ＋ 终点`
② `lab.py dedup "all the way" "its way" "way"` → 命中 9 条（含已毕业），逐条读：
   · 🎓#131（go ＝ 在程度轴上移动：go too far／How far are you willing to go?）—— **最接近的一条**，
     它的备注里就有 `go all the way`。
     **决定性证据**：按 #131 的规则去改 `The river runs ___ east` ⇒ 它给的是
     **go ＋ far／程度轴** 那一族（"做到什么程度"），得不到 `runs all the way east`
     ⇒ **给不出正确答案 ⇒ 不是同一条规则**。
     **互斥关系写死**：`go all the way` ＝ **程度义**（做到底、豁出去）⇒ 归 #131；
                      `all the way ＋ 方向／地点` ＝ **空间义**（整段距离）⇒ 归本条。
   · 🎓#223（肯定句里的 far → a long way）—— 目标形式是 **a long way**（距离量词），
     管的是"我走了很远"里不能用 far；本条管的是"整段都…"这个强调。
     **互斥写死**：只说距离远 ⇒ a long way（#223）；强调整段／大老远 ⇒ all the way（本条）。
   · 🎓#233（either way ＋ you might as well）—— 另一个固定词组，与距离无关
   · 🎓#143 #206 #277 #291 #295 #302 —— 命中的都是历史行例句里恰好出现 way，不是考点
③ 说得出差在哪：#131 差在**程度义 vs 空间义**｜#223 差在**距离量词 vs 全程强调**
   ⇒ **保留新建**
```

**我错在哪**
建号时她**没有写错**（本条来自教练的更好版本，建号理由是 §2③ 她点名要学 ——
她的原话："这个 all the way 或者 its way 我不太主动会用"）。
真正掉的一次在 2026-08-31：她写 `runs **all the way to east**`（多插一个 to），
正确 ＝ `all the way ＋ 方向副词`（east／home／back），要用 to 必须连冠词加名词（all the way to the east coast）。
找法：塞完 all the way，看后面那个词 —— **是方向副词（home／back／east）就不要 to**；
要用 to 就得跟一个带冠词的名词。

**题面**
"末班地铁没了，他只好一路走回家。" ／ "为了参加我的婚礼，她大老远从国外飞回来。"（两句都用 **all the way** 说）

- 2026-08-30 📝 新建 · **她当场指定**（§2③）· 复习第1组 [4] 的更好版里教练给了
  `This river **runs all the way east** and eventually empties into the East China Sea`，
  她当场说："run all the way，这个 **all the way** 或者 **its way** 我不太主动会用，也建一个条目吧"
  ★ 她**没有产出过错句** —— 本条是"**教练给的更好版本**"进池（零遗漏原则：错的／不会的／
    教练给的更好版本，三类全进复习清单），不是她犯的错 ⇒ 新建行记 📝，不记档位
  ★ 她原话里并列提到的第二样（its way）**另开 #311** —— 拆号理由见 #311 判重
  ⇒ 新建当天不测（§3.1），2026-08-31（R 付息日）a 段起进池
- 2026-08-31 ❌ 付息日 a 段第 1 组 · 顺带产出（第 1 记，同日共两记）
  在 #308 的答句里自发用了本条结构却写歪：`runs **all the way to east**`（多插一个 to）。
  正确 ＝ `all the way ＋ 方向副词`（home／back／up／down／east），要用 to 必须连冠词加名词：
  `all the way to the east coast`。
  ★ 判重留痕：与 #63（冠词族·形态类）两条路都能改出正确句，取**差值方向**定案 ——
    她与目标形式（08-30 建号时写死的 `runs all the way east`）的差是**多了一个 to**，
    不是**漏了一个 the** ⇒ 不属 §3.4 的"形态标记漏掉" ⇒ 不走 ⚪，判 ❌。
  ★ 与 08-30 #18 日志「`to east` 不另开号」不冲突：本次也没有新建，归的是已有的 #310。
- 2026-08-31 ✅ 付息日 a 段第 1 组 · 点名直测（第 2 记，同日共两记 —— §3.3「每次各记一行、各算一次」）
  `he walked **all the way home**.` ／ `he came **all the way from** Beijing`
  两句考位全中：all the way ＋ 方向副词（home）｜ all the way ＋ from ＋ 地点。
  ★ 同日第 1 记见上方 ❌（在 #308 的答句里 `all the way **to** east`）——
    顺序 ＝ 先 ❌（顺带产出）后 ✅（点名直测）⇒ 重放结果 连对1 连错0。
  ★ 她 08-30 的裁决口径："没有什么自由或者不自由产出，只有产出你就认" ⇒ 两记都认，不分档不加权。
  建号后首次点名直测即中。
- 2026-09-01 ✅ 复习第1组 [2] · 点名直测 · 题面 `他一路走回家的。／他大老远从北京跑过来。`
  `he walked **all the way home**. / he ran **all the way from** Beijing.`
  考点两句全中：all the way ＋ 方向副词（home）｜ all the way ＋ from ＋ 地点。
  ⚠️ 第二句动词选错方向（**不属本条考点，不判 ❌、不新建号**）：`ran` → `came`。
    中文"跑过来"这里不是真的跑，是"大老远来一趟"（跑＝奔波）；
    英文 `ran all the way from Beijing` 只有一个读法 —— 他真的一路跑步过来。
    ★ 不建号的三条理由：① 正确形式 `She came all the way from Beijing.` 逐字写在本条 08-30 判据块里；
      ② 她 08-31 在**同一个题面**上写的正是 `he came all the way from Beijing` ✅ ⇒ 不是"不会"；
      ③ §3.2b 自查：说不出"她不会的是哪个词组／句型" ⇒ 不建条目，diff-2 给更好版即可。
  ⇒ 连对1 → **连对2 ⇒ 毕业**（状态行手写）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 5 组（第 11 题整串，她事后补的原话："11直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  两句换新场景（走回家 ／ 从国外飞回来），照旧点名 all the way，后面接不接 to 留给她（08-31 掉过 all the way to east）

### 311 · 动词 ＋ its／his／my way ＋ 方向（"一路…着过去"）
类型 结构 ｜ 新建 2026-08-30（**她当场指定**）
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-09-01**（连对2 ＝ 08-31 ＋ 09-01）｜ 题型 整句

**问题是什么**
**动词 ＋ its／his／my way ＋ 方向**（"一路…着过去"）。
判据：
```
形状 ＝ **动词 ＋ one's way ＋ 方向短语**。way 是个**虚宾语**（不指真的路），
       真正的信息量在**那个动词**上 —— 它说的是"以什么方式移动过去"。
  ✅ The river **makes its way** through the city.   （一路流过市区 —— make ＝ 中性默认款）
  ✅ The path **winds its way** up the hill.          （蜿蜒着上山）
  ✅ He **pushed his way** through the crowd.         （挤过人群）
  ✅ I **worked my way** through college.             （一路打工读完大学 —— 也能用在非空间上）
★ 所有格必须跟主语一致：the river → **its** ／ he → **his** ／ I → **my**（✗ make **the** way）
★ 与 #310 的分工，一句话：
   **all the way** 说的是"**整段都**"（有多远／多费劲）
   **V ＋ its way** 说的是"**怎么过去的**"（用什么方式穿过去）
   两个可以同时出现：It winds its way all the way to the sea.
★ 检查触发：写完一个移动的句子，问 —— **我想说的是"走了多远"还是"怎么走过去的"？**
  后者 ⇒ 把动词换成有姿态的那个，后面加 its way。
```
★ 为什么不与 **#310** 合成一条（她原话说的是"建一个条目"）：§3.1「一条 ＝ 一个考点」——
　两者语法形状完全不同（副词短语 vs 动词带虚宾语的句法结构），不满足 §3.2c 合并条的条件。

**怎么发现的**
2026-08-30 📝 新建 · **她当场指定**（§2③）· 与 #310 同一句话触发
（她的原话："这个 all the way 或者 **its way** 我不太主动会用，也建一个条目吧"）。
★ 同 #310：她**没有产出过错句**，本条是"教练给的更好版本"进池，新建行记 📝、不记档位。
判重（新建当天复核，§4④1b）：
```
① 目标英文形式 ＝ `V ＋ one's way ＋ 方向短语`
② `lab.py dedup "all the way" "its way" "way"` → 命中 9 条，**"its way" 一条都没命中**
   （全库此前从未出现过这个结构）。逐条读命中 way 的：
   · #310（本日同时新建）—— **最接近**。**决定性证据**：按 #310 的规则去改
     `The river ___ through the city` ⇒ 得到 `The river runs all the way through the city`
     —— 这句是对的，但它**只加了"整段"那层意思，没有"怎么过去的"那层**；
     且 #310 是**副词短语**、本条是**动词带虚宾语的句法结构** ⇒ 目标形式不同 ⇒ 两条。
   · 🎓#223（a long way）／🎓#233（either way）／🎓#131（go all the way）——
     都是别的词组，形状不同，逐条读过
③ 说得出差在哪：与 #310 差在**副词短语 vs 动词＋虚宾语结构**，且信息落点不同
   （多远 vs 怎么过去的）⇒ **保留新建**
★ 为什么不与 #310 合成一条（她原话说的是"建一个条目"）：§3.1「一条 ＝ 一个考点」＋
  「⛔ 捆绑条目必然与别的号重叠，且一个块掉整条清零」。两者语法形状完全不同，
  不满足 §3.2c 合并条的条件（不是"同一条规则下的不同成员"）。
  📌 她若认为该并回一条，当场合并（她的裁决优先）。
```

**我错在哪**
她没有写错过（本条来自教练的更好版本，建号理由是 §2③ **她点名要学** ——
原话："这个 all the way 或者 its way 我不太主动会用"）。
08-31 首测那次唯一的瑕疵 `it way` 判**拼写不计错**（§2.1，its 就印在题面里）。
找法：写完一个移动的句子，问 —— **我想说的是"走了多远"还是"怎么走过去的"？**
后者 ⇒ 动词换成有姿态的那个（wind／push／make），后面加 **its way**（所有格跟主语一致）。

**题面**
**点名**："那条河一路穿过市区流过去。"（用 "**动词 ＋ its way**" 这个结构说）

- 2026-08-30 📝 新建 · **她当场指定**（§2③）· 与 #310 同一句话触发（"这个 all the way
  或者 **its way** 我不太主动会用"）
  ★ 同 #310：她**没有产出过错句**，本条是"教练给的更好版本"进池，新建行记 📝、不记档位
  ⇒ 新建当天不测（§3.1），2026-08-31（R 付息日）a 段起进池
- 2026-08-31 ✅ 付息日 a 段第 1 组
  `that river runs **it way** through the city.`
  结构考位 `动词 ＋ ___ way ＋ 方向` 完整命中 ⇒ ✅。
  ★ `it way` 判**拼写不计错**（§2.1）：its 就印在题面里（"动词 ＋ its way"），她照着少打一个 s；
    同批 [4b] `her friends` 所有格限定词用对 ⇒ 不是形态缺口。
  ★ 更好版给了 `winds its way`（本结构的动词负责"怎么走"，不负责"走"本身）——属 ⚠️，不影响档位。
  建号后首测即中。
- 2026-09-01 ✅ 复习第1组 [4] · 点名直测 · 题面 `那条河一路穿过市区流过去。`
  `That river **winds its way** through the city.`
  考点 动词 ＋ its way ＋ 方向短语。
  ★ 与 08-31 的 `that river runs **it** way through the city` 相比两处都进步：
    ① its 修好（08-31 写成 it）② 动词自己换成 winds。
    `wind one's way` 正是英语给河／路／小径配的那个动词（蜿蜒着走），比 run 更贴 ——
    **不是教练教过的，是她自己换上去的**。
  ⇒ 连对1 → **连对2 ⇒ 毕业**（状态行手写）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 7 组 · `that river winds its way through the city center.` —— winds its way ＋ 方向，结构一字不差
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [7] · `That river winds its way through the city center.`

### 312 · search for sth（search 找"东西"必须带 for）
类型 搭配 ｜ 新建 2026-08-30
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-09-01**（连对2 ＝ 08-31 ＋ 09-01）｜ 题型 整句

**问题是什么**
**search for sth**（search 找"东西"必须带 **for**）。
判据：
```
search ＋ 宾语      ＝ **把某个地方／某个库翻一遍**（宾语是"被搜的范围"）
  ✅ search the room（把房间翻一遍）　✅ search the web　✅ search the database　✅ They searched him.
search **for** ＋ 宾语 ＝ **找某个东西**（宾语是"你要的那个东西"）
  ✅ search for information　✅ search for a job　✅ search for an answer
★ 一句话判据：**你在搜"哪儿" → search ＋ 地方；你在找"什么" → search for ＋ 东西。**
★ 同族一起记（都是"找"，介词各不同）：
  **look for sth**（找东西）／ **look sth up**（查资料）／ **search for sth**（搜索某物）
★ 检查触发：写完 search，问一句 —— **后面这个词是"地方"还是"东西"？** 东西 ⇒ 补 for。
★ 口语升级（不是本条考点，附记）：手机上"查东西"最顺的是 **look sth up ／ look up whatever…**；
  search for information 偏正式一点。
```
★ 与 🎓**#100**（look for sth ≠ look up ＝ 查资料）的**互斥关系写死**：想说"查资料" ⇒ look up（#100）；
　想用 search 说"搜某物" ⇒ search for（本条）。
★ 与 **#18**（论元完整：动词必须带宾语）的分工：#18 是宾语**空着**，本条是宾语**有、缺的是介词**。
★★ 与 **#313** **方向正好相反，两条必须一起读**：本条 search 后面**要补** for；
　#313 message 后面**不许加** with ⇒ 动词跟不跟介词是**每个词自己的性质**，只能整块记。

**怎么发现的**
2026-08-30 ❌ 首犯 · 新题 P3（What technology do young people like to use?）· 她写
`People can **search information** they want, order takeaway and even call a ride on their phones.`
（→ search **for** information they want）—— search 后面直接跟的是"被搜查的地方／库"，不是"要找的东西"。
判重（新建当天复核，§4④1b ⛔ 严禁脚本批量判 —— dedup 只捞候选，判断逐条人读）：
```
① 目标英文形式 ＝ `search for sth`
② `lab.py dedup "search" "look up" "打车"` ＋ `grep -n "search" problems.md` → 命中逐条读：
   · 🎓#100（look for sth ≠ look up ＝ 查资料）—— **最接近的一条**。
     **决定性证据**：按 #100 的规则去改这句 ⇒ 它给的是"把动词换成 look up"
     （`look up the information they want`）—— 那是**换一个词组**，不是修 search 的用法；
     她若坚持用 search，#100 **给不出 `search for`** ⇒ 不是同一条规则。
     **互斥关系写死**：想说"查资料" ⇒ look up（#100）｜想用 search 说"搜某物" ⇒ search for（本条）。
   · #18（论元完整：动词必须带宾语）—— **方向相反**：#18 是宾语**空着**，
     本条是宾语**有、缺的是介词**。按 #18 的规则改 ⇒ "把宾语补出来" ⇒ 她本来就有宾语
     ⇒ **给不出正确答案** ⇒ 不同条。
   · #18 的 08-20 日志行（`I searched for hours`）—— 那里 search 作**不及物**用，
     是另一种用法，不是考点行。
   · 🎓#86（go on a trip ＋ where to stay）—— 命中的是历史行例句里的 look up，不是考点。
③ 说得出差在哪：#100 差在**换动词 vs 修介词**｜#18 差在**缺宾语 vs 缺介词** ⇒ **保留新建**
```

**我错在哪**
她的：`People can **search information** they want`　　正确：`search **for** information they want`
找法：写完 search，问一句 —— **后面这个词是"地方"还是"东西"？** 是东西 ⇒ 补 **for**。

**题面**
"我在网上搜了半天去成都的便宜机票。"（"搜"用 **search** 说）

- 2026-08-30 ❌ 首犯 · 新题 P3（What technology do young people like to use?）·
  `People can **search information** they want, order takeaway and even call a ride on their phones.`
  → search **for** information they want
  ❌ search 后面直接跟的是"被搜查的地方／库"，不是"要找的东西"
  ★ 同句另外两处**全对**，单独记：`order takeaway`（口语词，不是书面词）·
    三个动词并列同形（search／order／call 全跟 can 走原形，一处不乱）
- 2026-08-31 ✅ 付息日 a 段第 1 组
  `he's been **searching** online **for a part-time job** for weeks.`
  考点 search **for** ＋ 东西：介词在、宾语在 —— 08-30 首犯 `search information`，隔一天拿回。
  顺带全对两处：has been searching（"找了好几个星期"还在找）· online 的位置。
  ⇒ 连对1
- 2026-09-01 ✅ 复习第1组 [3] · 点名直测 · 题面 `他在网上找一份兼职找了好几个星期。`
  `He has been **searching** online **for** a part-time job for several weeks.`
  考点 search **for** sth —— for 在位。
  ★ 与 08-31 的 `he's been searching online for a part-time job for weeks` 相比考位一字未动，
    是稳定的第二次（只多了 several）。
  ★ 教练自审留痕：一度想把语序改成 `searching for a part-time job online` ⇒ **撤**，
    两种语序母语者都说，属 ⛔ 教练不必要的改动。
  ⇒ 连对1 → **连对2 ⇒ 毕业**（状态行手写）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 5 组（第 11 题整串，她事后补的原话："11直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 search，for 留给她（她掉过的是 search information）；换成搜机票场景

### 313 · message sb（发消息给某人，后面直接跟人）
类型 搭配 ｜ 新建 2026-08-30（**她当场指定**）
状态 连对2 连错0 上次2026-09-22 ｜ **🎓 已毕业 2026-09-01**（连对2 ＝ 08-31 ＋ 09-01）｜ 题型 整句

**问题是什么**
**message sb**（发消息给某人，后面**直接跟人**）。
判据：
```
message 当**动词**时，**后面直接跟人**，不加 to／with：
  ✅ I'll **message you** later.                        （✗ message **to** you）
  ✅ She was **messaging her friends** all afternoon.    （✗ messaging **with** her friends）
  ✅ He **messaged me** around midnight.
★ 同一族（都直接跟人）：**text sb ／ call sb ／ email sb ／ answer sb**
⚠️ **反例也在同一族里，别一起推**：**write to sb ／ reply to sb ／ talk to sb** —— 这几个要 to。
★★ 与 #312 **方向正好相反，两条必须一起读**：
     #312  search 后面**要补** for（search **for** information）
     #313  message 后面**不许加** with（message her friends）
   ⇒ 动词跟不跟介词，**不是一条规则能管的，是每个词自己的性质** ⇒ 只能整块记。
     背的时候永远背整块：`search for sth` ／ `look sth up` ／ `message sb` ／ `call sb`。
     （方法论侧写在 methods.md M45）
★ 检查触发：写完一个"跟人说话／联系"的动词，问一句 ——
  **这个词是直接跟人，还是要先架个 to？** 想不起来就换成一定直接跟人的 text／call。
★★ **出题约束（写死）**：第二句题面（"**跟**朋友发消息"）才是本条的真正考位 ——
  中文的"跟"最容易被直译成 with。⛔ 出题时不许只出第一句。
```
★ 与 **#18**（论元完整：动词必须带宾语）的分工：#18 是宾语**空着**，本条是宾语**有、却多架了一个介词**。

**怎么发现的**
2026-08-30 📝 新建 · **她当场指定**（§2③）· 新题 P3 里 · 她写
`… scrolling through short videos or just **messaging with others**.`（→ messaging **their friends**）。
★ **为什么新建行不记 ❌**（四问④档位）：`messaging with others` 在口语里不是明确的错
（类比 chat with）⇒ 档位 ⚠️ 不是 ❌ ⇒ 记 📝、不记档位、不进连错。
★ **教练犯规留痕**：本篇诊断里教练只判了"others 太泛"，**漏说 `with` 本身多余** ——
她读出来了并当场指定建号。
判重（新建当天复核，§4④1b ⛔ 严禁脚本批量判）：
```
① 目标英文形式 ＝ `message sb`（动词后直接接人，无介词）
② `lab.py dedup "message" "text sb" "email"` → 命中 **1 条**，逐条读：
   · 🎓#267（get sth in front of sb）—— 命中的是历史行例句里的**名词** message
     （`get your message in front of a bigger audience`），不是考点 ⇒ 无关。
   再手工扩查两条最可能相关的：
   · #18（论元完整：动词必须带宾语）—— **方向不同**：#18 是宾语**空着**，
     本条是宾语**有、却多架了一个介词**。按 #18 的规则改 ⇒ "把宾语补出来" ⇒
     她本来就有 others ⇒ **给不出正确答案** ⇒ 不同条。
   · #312（search for sth，今天同日新建）—— **方向相反**：#312 是"必须加 for"。
     按 #312 的规则改 ⇒ 得到"给 message 也补个介词" ⇒ **正是她的原句** ⇒ 给不出答案
     ⇒ 不同条。★ 互斥已写死在两条的判据里（防她把两条记混）。
③ 说得出差在哪：#18 差在**缺宾语 vs 多介词**｜#312 差在**要加 vs 不许加** ⇒ **保留新建**
```

**我错在哪**
她的：`… or just **messaging with others**.`　　正确：`… or just **messaging their friends**.`
（档位 ⚠️ 不是 ❌ —— 口语里 messaging with 不是明确的错，但不是母语者的默认说法。）
找法：写完一个"跟人说话／联系"的动词，问一句 —— **这个词是直接跟人，还是要先架个 to？**
message／text／call／email 一律**直接跟人**，⛔ 别被中文的"跟"骗去加 with。

**题面**
"到家了记得给我发个消息。" ／ "他上课的时候一直偷偷跟同学发消息。"（两句的"发消息"都用 **message** 说）

- 2026-08-30 📝 新建 · **她当场指定**（§2③）· 新题 P3 里 ·
  `… scrolling through short videos or just **messaging with others**.` → messaging **their friends**
  ★ **为什么新建行不记 ❌**（四问④档位）：`messaging with others` 在口语里不是明确的错
  （类比 chat with，美式口语有人这么说）⇒ 档位 ⚠️ 不是 ❌ ⇒ 记 📝、不记档位、不进连错。
  ★ **教练犯规留痕**：本篇诊断里教练只判了"others 太泛"（层2 精确度），
    **漏说 `with` 本身多余** —— 更好版里 with 事实上去掉了，理由却没在 diff 里逐处列出
    （§7「❌ 必须给可迁移的理由」的隐性违反）。她读出来了并当场指定建号。
  ⇒ 新建当天不测（§3.1），2026-08-31（R 付息日）a 段起进池
- 2026-08-31 ✅ 付息日 a 段第 1 组
  `I'll message you later.` ／ `she **messaged her friends** all afternoon.`
  第二句是本条真正的考位（中文"**跟**朋友发消息"最易直译成 message **with**）——
  她没有写 with，动词后直接跟人 ⇒ 一字不差命中。建号后首测即中。
- 2026-09-01 ✅ 复习第1组 [5] · 点名直测 · 题面 `我等下发消息给你。／她整个下午都在跟朋友发消息。`
  `I'll **message you** later. / she's been **messaging her friends** all afternoon.`
  考点两句全中：message 后面直接跟人，无 to／with。
  ★ 时态留痕：08-31 写 `she messaged her friends all afternoon`（一般过去），今天写完成进行。
    中文"整个下午都在"两种读法都合法（下午未完 ⇒ 完成进行；下午已过 ⇒ 一般过去），
    句内自洽 ⇒ **不判**，只记差异。
  ⇒ 连对1 → **连对2 ⇒ 毕业**（状态行手写）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 4 题整串，她原话："1-4 直接过"）
- 2026-09-22 ⚡ 自评免测 · 复检第 4 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  两句换新场景，只点名 message（去掉"当动词说"），后面带不带 with／to 留给她

### 314 · economic（经济的）≠ economical（省钱的）
类型 词汇 ｜ 新建 2026-08-31
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-09-03**（连对2 ＝ 09-01 ＋ 09-03；08-31 新建、当天首犯，两次点名直测连翻）｜ 题型 整句

**问题是什么**
**economic**（经济的）≠ **economical**（省钱的）。
判据：
```
economic   ＝ 经济（方面）的 → economic growth ／ economic policy ／ economic crisis ／
                              economic downturn ／ the economic situation
economical ＝ 省钱的、省油的 → an economical car ／ an economical way to get around ／
                              It's more economical to buy in bulk.
★ 一句话：**-ic 的那个是"关于这个领域"，-ical 的那个另有意思。**
★ 同族一起记（同一个后缀对立）：
  historic（有历史意义的）／ historical（历史上的）
  classic（经典的）／ classical（古典的）
  economic（经济的）／ economical（省钱的）
⚠️ ⛔ 别把这条推广成"凡 -ical 都是另一个意思"——**practical／political／physical 没有对立的 -ic 版本**。
   这三对是要整块记住的**有限清单**，不是规则。
```
★ 与 🎓**#255**（vital ≠ virtual）的分工：同样是"形近词选错"，但 §3.2 写死「词汇/搭配按**具体的词**
　一条一号」⇒ 另立；按 #255 的规则改 `economical growth` **给不出 economic**。
★ 与 **#89**（加形容词回到 a）的分工：那条管**冠词**，本条管**选哪个形容词** ⇒ 不同层。

**怎么发现的**
2026-08-31 ❌ 首犯 · 付息日 d 段重答 R9（P3 · Should governments provide financial support to start-ups?）·
她写 `So financial support from governments play a crucial role in **economical growth**.`
★ 判为**选词**不是拼写（§2.1④）：调出来的是**另一个词**，不是同一个词写歪。
★ 反证她不是不会 economy：**同一篇** S2 的 `a diverse economy` 用对 ⇒ 缺的只是**形容词那一格**。
判重结论（§3.1 判重三步，2026-08-31 当天做）：**保留新建**
```
① 目标英文形式 ＝ `economic`
② 全档 grep `economic\|economical`（**范围含已毕业**）⇒ **零命中**
③ 最接近的一条 ＝ 🎓#255（vital ≠ virtual）—— 同样是"形近词选错"，
   但 §3.2 写死「词汇/搭配按**具体的词**一条一号」⇒ 另立
   **决定性证据**：按 #255 的规则去改 `economical growth`，它只管 vital／virtual 这一对，
   **给不出 economic** ⇒ 不是同一条规则 ⇒ 新建
④ 另比对 #89（加形容词回到 a）：那条管**冠词**，本条管**选哪个形容词** ⇒ 不同层
```

**我错在哪**
她的：`play a crucial role in **economical growth**`　　正确：`in **economic** growth`
找法：要说"经济的"就用 **-ic** 那个（economic）；**-ical** 那个是"省钱的"——
这三对（economic/economical · historic/historical · classic/classical）**整块背，不是规则**。

**题面**
"政府今年出台了一系列新的经济政策。"
　　★ 零提示："经济政策"只有 economic policies 一条自然路（policies on the economy 也算对）；她掉过的是 economical growth

- 2026-08-31 ❌ 首犯 · 付息日 d 段重答 R9（P3 · Should governments provide financial support to start-ups?）·
  `So financial support from governments play a crucial role in **economical growth**.`
  ★ 判为**选词**不是拼写（§2.1④）：调出来的是**另一个词**，不是同一个词写歪。
  ★ 反证她不是不会 economy：**同一篇** S2 的 `a diverse economy` 用对 ⇒ 缺的只是**形容词那一格**。
- 2026-09-01 ✅ 复习第1组 [8] · 点名直测 · 题面 `政府的资金支持对经济增长很关键。`
  `Financial support for governments is vital to **economic** growth.`
  考点 **economic**（08-31 首犯写的是 `economical`，今天调对了）。
  ★ 新建（08-31）后首次点名直测即中；按 §3.1「新建当天不测、次日起进池」正好到期。
  ★ 同句另有两处，**标记打在条目上不打在整句上**（§3.3），各自归各自的号：
    ① `support **for** governments` ⇒ 意思反了 ⇒ **新建 #315**（见该条）
    ② `Financial support ... **is** vital` ⇒ 主谓一致做对 ⇒ #10 形态类，只记 ⚪
  ⇒ 连对0 连错1 → **连对1**（差一次毕业）
- 2026-09-03 ✅ 复习第1组 [5] · 点名直测 · 题面 `政府的资金支持对经济增长很关键。`
  `Government financial support is vital to **economic** growth`
  考点 `economic`（经济的）≠ economical（省钱的）—— 词形一字不差。
  ★ 顺带：`vital to` 也对（词是 vital 不是 virtual，介词是 to）⇒ 🎓#255 自发命中，另记一行留痕。
  ⚠️ 同句另一处（**不属本条考点，不判 ❌、不新建号**）：
    `Government financial support` → `Financial support **from** the government` ——
    两层修饰（Government ＋ financial）全叠在名词前面，口语里读着发闷；英语更爱把"谁给的"
    甩到后面用介词说。判据可迁移：**名词前面最多叠一层，第二层往后甩成介词短语。**
    ★ **决定性观察**：同一场第 2 题她写的正是 `financial support **from** governments` ——
      同一件事隔三题一次后置、一次前置 ⇒ **不是不会，是选择不稳定**。
    ⛔ 不建号：英语本来允许名词堆叠（Government financial support 在报告体里到处都是）⇒
      收不成一条"错"的规则（§3.2b）。这是同族第二例（09-01 `a new system version` 是第一例），
      两次同裁 ⚠️ 不建号，记进纵向发现，等第三例看形状能不能收敛。
  ⇒ 连对1 → **连对2，毕业**（状态行手写，见上）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 3 题整串，她原话："1-4 直接过"）
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [2] 打包 · `economic growth`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）· 题型 词组 → 整句
  去掉"econom- 开头"猜谜写法，改零提示整句"经济政策"—— 只有 economic 一条自然路，她掉过的是 economical growth
- 备注 **出题口径（单句，不做合并条）**：本次的缺口是**单向**的 ——
  想说"经济的"调出了 economical；**没有**"想说省钱的却调出 economic"的证据。
  ⇒ 照 🎓#255（vital ≠ virtual）的先例出**单句**，⛔ 不凭空造第二个方向（那是加戏）。
  若日后出现反向，再按 §3.2c③ 摘出来另立。
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 315 · support FROM sb（谁给的）≠ support FOR sb（给谁的）
类型 搭配 ｜ 新建 2026-09-01
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-09-04**（连对2 ＝ 09-03 ＋ 09-04；09-01 新建当天首犯，两次复测 from／for 两个方向各一句全中）｜ 题型 整句

**问题是什么**
**support FROM sb**（谁给的）≠ **support FOR sb**（给谁的）。
判据：
```
support ＋ 介词，这个介词管的是"**谁给**"还是"**给谁**"：
  support **from** ＋ 出钱/出力的一方
      financial support **from** the government ／ support **from** my family ／
      funding **from** investors ／ help **from** a colleague
  support **for** ＋ 受益的一方
      support **for** start-ups ／ support **for** small businesses ／
      support **for** the new policy ／ there's a lot of support **for** this idea
★ 中文陷阱（本条的真考点）：中文一个"的"，英文两种角色 ——
    「政府**的**资金支持」　＝ 政府出钱 ⇒ **出资方** ⇒ from
    「对小企业**的**支持」　＝ 小企业收钱 ⇒ **受益方** ⇒ for
  ⇒ 中文的"的"不带角色信息，英文必须自己判：**先问"谁出的钱"**，再挑介词。
★ 最省事的绕开法：把出资方直接当定语放到前面 ——
  **government funding** ／ **government support**（名词当形容词用，介词就不用挑了）
★ 检查触发：写完 support／help／funding 这一族名词，问一句 ——
  **我说的是"谁给的"还是"给谁的"？** 前者 from，后者 for。
```
★ 与 **#314**（economic ≠ economical，同一句里的另一处）的分工：那条管**形容词选词**，
　按它的规则改**给不出 for→from** ⇒ 不同考点；**题面互斥**：本条题面里根本不出现"经济增长"。
★ 与 **#243**（形容词 ＋ 固定介词整块记）的分工：那条是**形容词带死一个介词**；
　本条是**同一个名词的两个介词各管一个语义角色、两个都对** ⇒ 不同层。
★ 与 🎓**#200**（think FOR oneself ≠ by oneself）的分工：形状最像（一个词两个介词两个意思），
　但 §3.2 写死「搭配按**具体的词**一条一号」⇒ 另立。
★★ **出题口径**：**两句都出**（一句测 from、一句测 for），⛔ 不许只出一句 ——
　只出 from 那一句，她永远测不到"什么时候该用 for"。这不是 §3.2c 的合并条，是**一条规则的两个方向**。

**怎么发现的**
2026-09-01 ❌ 首犯 · 复习第 1 组 [8] 句里（题面 `政府的资金支持对经济增长很关键。`）· 她写
`**Financial support for governments** is vital to economic growth.`
（→ Financial support **from** governments is vital to economic growth.）
❌ 意思反了：她这句英文读出来是"**给**政府的资金支持"，中文说的是"政府**出**的资金支持"。
判重结论（§3.1 判重三步，2026-09-01 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
```
① 目标英文形式 ＝ `support from sb` ／ `support for sb`
② 全档 grep（**范围含已毕业**）：
   `grep "^### .*support"` ⇒ **零命中**
   `grep "support from\|support for\|financial support"` ⇒ 只命中她自己的日志行
     （#10 · 🎓#206 · #314），**一条条目都没有**
   `grep "^### .*介词\|^### .*from\b"` ⇒ #62 #103 #127 #158 #170 #193 #242 #243 #266 #273 #274 #300 #308
     逐条读过，无一管 support 的介词语义角色
③ 三条最接近的，逐条排除：
   · #314（同一句里的另一处）——管**形容词 economic／economical**。
     **决定性证据**：按 #314 的规则去改她这句，只改得出 economical→economic，
     **给不出 for→from** ⇒ 不同考点。
   · #243（形容词 ＋ 固定介词整块记：familiar WITH／interested IN）——那条是**形容词带死一个介词**；
     本条是**同一个名词的两个介词各管一个语义角色、两个都对**。
     **决定性证据**：按 #243 的规则去改（"support 后面固定跟某个介词"）**得不到答案**，
     因为 support from 与 support for 都是标准搭配，选哪个取决于谁出钱 ⇒ 不同层。
   · 🎓#200（think FOR oneself ≠ by oneself）——形状最像（一个词两个介词两个意思），
     但 §3.2 写死「搭配按**具体的词**一条一号」⇒ 另立。
④ **题面互斥**（§3.1③ 硬要求）：
   #314 的题面点名"经济增长那个形容词"；本条题面里**根本不出现"经济增长"**，
   两句换成小公司/小企业的资金支持 ⇒ 两条题面不撞车，日后同组也不冲突。
⑤ 出题口径：**两句都出**（一句测 from、一句测 for），⛔ 不许只出一句 ——
   只出 from 那一句，她永远测不到"什么时候该用 for"。
   ★ 这不是 §3.2c 的"合并条"（成员只有一个词 support），是**一条规则的两个方向**。
```

**我错在哪**
她的：`**Financial support for governments** is vital to economic growth.`（意思反了）
正确：`Financial support **from** governments is vital to economic growth.`
找法：写完 support／help／funding 这一族名词，问一句 —— **我说的是"谁给的"还是"给谁的"？**
前者 **from**，后者 **for**（中文的"的"不带这个信息，必须自己判）。

**题面**
"这个项目能撑下来，全靠我父母的资金支持。" ／ "社会对残疾人的支持还远远不够。"（两句的"支持"都用 **support** 说）

- 2026-09-01 ❌ 首犯 · 复习第1组 [8] 句里（题面 `政府的资金支持对经济增长很关键。`）·
  `**Financial support for governments** is vital to economic growth.`
  → Financial support **from** governments is vital to economic growth.
  ❌ 意思反了：她这句英文读出来是"**给**政府的资金支持"（比如国际援助给政府），
     中文说的是"政府**出**的资金支持"。
  ★ 同句另外两处各归各号（§3.3 标记打在条目上，不打在整句上）：
    `economic growth` ✅ 归 #314（本条不沾）｜ `support ... **is**` 主谓一致做对 ⇒ #10 记 ⚪
- 2026-09-03 ✅ 复习第1组 [2] · 点名直测 · 题面 `这些小公司很需要政府的资金支持。／政府对小企业的支持还不够。`
  `These small companies really need finacial support **from** governments.`
  `Government support **for** small businesses is still lacking.`
  **考点两句全中**：from（谁给的）／ for（给谁的）—— 09-01 首犯写的是 `support **for** governments`
  （把"谁给的"说成了"给谁的"），今天两个方向一次分清 ⇒ 建号第三天首测即翻正。
  ｜`finacial` 按 §2.1 拼写不算错（正确拼法 financial）。
  ⚠️ 同句另一处（**不属本条考点，不判 ❌、不新建号、⛔ 不记 ⚪**）：
    `from governments` → `from the government` —— 主语用了 `These small companies`（特指这一批），
    后面的政府就该跟着特指；`governments` 复数把话拉到"各国政府"那个尺度，前后档位不齐。
    ⛔ **不归 #63 记 ⚪**：⚪ 是给"形态掉了"用的，这里两个形式都合法，不存在"掉"⇒ 只走 diff-2。
  ★ 第二句 `Government support` 一个字不改 —— 那里是**泛指政府这一类支持**，与主语档位一致，是对的。
  ⇒ 连对0 连错1 → **连对1**（差一次毕业）
- 2026-09-04 ✅ 复习 · 第 1 组 · 中译英两句，考点位两个方向一次全对
  `These small companies really need financial support **from** the government.`（谁给的）
  `Government support **for** small businesses is still not enough.`（给谁的）
  ★ 09-01 中译英首犯（写成 support to／方向混）→ 09-03 ✅ → 09-04 ✅ ⇒ 连对 2
  ★ 判前自审留痕：`support of the government` 会反向读成"对政府的支持"，
    `give support to sb` 里的 to 是动词 give 带的、不是名词 support 带的 ⇒ from／for 才是本条的两个出口。
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 4 题整串，她原话："1-4 直接过"）
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [2] 打包（漏答后当场补答）· `Financial support from the government. Government support for small businesses.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  两句换新场景（父母出资 ／ 社会对残疾人），只点名 support，from／for 留给她
- 备注 **本条的诊断价值（反向证据，与她平时的形状相反）**：
```
她 08-31 在 R9 **cold 自由产出**里自己写的是 `financial support **from** governments` ✅
—— support from 她本来就会。今天走**中译英**这条路反而掉了。
⇒ 缺口不在 support 这个词上，在"**从中文的'的'反推英文介词**"这一步：
  中文的"的"默认被翻成 of／for，语义角色那一步被跳过了。
⇒ 她平时的形状是"点名对、自由产出掉"（retrieval-under-pressure）；
  **本条正好反过来** ⇒ 只有中译英题面测得到它，自由产出测不出来。
  ⛔ 因此本条不许靠"自由产出自发命中"毕业，必须点名直测。
```
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 316 · log in（动词，两个词）≠ login（名词，一个词）
类型 词汇 ｜ 新建 2026-09-01
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-09-04**（连对2 ＝ 09-03 ＋ 09-04；题面 09-03 整改过——只钉词根 log 不钉词形，两次测的都是真考点）｜ 退池 ｜ 题型 词组

**问题是什么**
**log in**（动词，两个词）≠ **login**（名词，一个词）。
判据：
```
动词 ＝ **log in**（分开写两个词）
   I can't **log in**. ／ **log into** your account ／ **log out** when you leave ／
   Have you **logged in** yet?
名词/形容词 ＝ **login**（连着写一个词）
   your **login** details ／ the **login** page ／ click the **login** button ／ I forgot my **login**.
⛔ `login in` 不存在 —— 那是把名词当动词用了，然后又补了一个 in。
★ 同族一起记（**动词分开写、名词连着写**，这一族在她的工作场景里高频）：
   log in ／ a login          set up  ／ a setup
   back up ／ a backup        check in ／ a check-in
   sign up ／ a signup        roll out ／ a rollout
★ 检查触发：写完 login／setup／backup 这一族，问一句 ——
  **我这里要的是"动作"还是"东西"？动作 ⇒ 分开写两个词。**
```
★ 与 🎓**#62**（drive past sth：past 是介词，pass 是动词）的分工 —— **形状最像**（同一串字母的
　两种词类被混用），但 §3.2「词汇/搭配按具体的词一条一号」⇒ 另立。
★ 与 🎓**#213**（功能上线 ＝ go live／be released）的分工：同属她的工作场景词，管的是"上线"用哪个动词 ⇒ 无关。
★ **不是形态类**：#56／#63 管单复数与冠词，本条管**词类**（名词 vs 动词短语），
　§3.4 的形态类清单里**没有"词类"** ⇒ 照常记 ❌，⛔ 不走 ⚪。
★★ **出题口径**：两句都出（一句测动词、一句测名词），⛔ 不许只出一句 ——
　这不是 §3.2c 的合并条（成员只有 log in 这一个词），是**一个词的两种词类**。

**怎么发现的**
2026-09-01 ❌ 首犯 · 新题 P3（question_bank.md:490 · What are the rules people should obey at work?）· 她写
`I remember one time users could neither **login in** nor place orders because the developer released a wrong version.`
（→ users could neither **log in** nor place orders）
❌ 把名词 login 整块当成了动词，然后又补了一个 in。英语里没有 `login in` 这个形式。
★ 同句 `neither … nor` 用对 ＝ 🎓#65 的自发命中 ⇒ **她的问题只在 log in 这一个块上**。
判重结论（§3.1 判重三步，2026-09-01 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
```
① 目标英文形式 ＝ `log in`（动词分写）／ `login`（名词连写）
② 全档 grep（**范围含已毕业**）：
   `grep "log in\|login\|log on" problems.md methods.md` ⇒ **零命中**
③ 三条最接近的，逐条排除：
   · 🎓#62（drive past sth：past 是介词，pass 是动词）——**形状最像**：
     同一串字母的两种词类被混用。
     **决定性证据**：按 #62 的规则去改她这句，它只管 past／pass 这一对，**给不出 log in**
     ⇒ 不同条（§3.2「词汇/搭配按具体的词一条一号」）。
   · 🎓#213（功能上线 ＝ go live／be released）——同属她的工作场景词，
     管的是"上线"这个动作用哪个动词，不管 log in 的分写 ⇒ 无关。
     ★ 而且今天她 `released` 用对，正是 #213 的自发命中，两条不冲突、不重叠。
   · #56／#63（形态类）——那两条管单复数与冠词；本条管**词类**（名词 vs 动词短语）。
     §3.4 的形态类清单是「主谓一致·时态标记·单复数/限定词·冠词/指称·比较级·否定标记·
     不规则动词变形」——**里面没有"词类"** ⇒ 本条照常记 ❌，⛔ 不走 ⚪。
④ 是不是拼写（§2.1 不算错）？**不是。**
   §2.1④ 的判据是"她脑子里调的词对不对"——她调出来的是屏幕上看惯的**名词 login**，
   再补了个 in ⇒ 属「选词（调出另一个词）」，照常算。
   ★ 反证：真拼写错长成 `logn in`／`log inn` 那样；**多余的那个 in**
     说明她把 login 整块当动词了，不是手指打歪。
```

**我错在哪**
她的：`users could neither **login in** nor place orders`　　正确：`could neither **log in** nor place orders`
找法：写完 login／setup／backup 这一族，问一句 —— **我这里要的是"动作"还是"东西"？**
动作 ⇒ **分开写两个词**（log in）；东西 ⇒ 连着写（the login page）。

**题面**
**点名**："登不进去" ／ "登录页面"（两句都用 **log** 这个词说；第一句当**动作**，第二句当**东西**）
★ 题面 2026-09-03 整改：加点名"两句的登录都用 **log** 这个词说"，堵掉 `sign in`／`the sign-in page` 这条合法绕道。**只点词根不点词形** —— 分写还是连写仍由她自己判，考位一个字没漏出去（§6"可点目标词，不许整句给答案"）

- 2026-09-01 ❌ 首犯 · 新题 P3（question_bank.md:490 · What are the rules people should obey at work?）·
  `I remember one time users could neither **login in** nor place orders because the developer released a wrong version.`
  → users could neither **log in** nor place orders
  ❌ 把名词 login 整块当成了动词，然后又补了一个 in。英语里没有 `login in` 这个形式。
  ★ 同句里另外两处各归各号（§3.3 标记打在条目上，不打在整句上）：
    `released` ✅ 是 🎓#213 的自发命中 ｜ `a wrong version` → `the wrong version` 归 #63 记 ⚪
  ★ 同句 `neither … nor` 用对 ＝ 🎓#65 的自发命中 ⇒ **她的问题只在 log in 这一个块上**。
- 2026-09-03 📝 题面整改（出题前跑 §6.5 第 7 项"第二译法自查"时发现，⛔ 未测就改，本次不计档位）
  发现 ＝ "登录"有第二个**同样合法**的译法：`sign in` ／ `the sign-in page`。她若写 sign in，
  按 §3.3 得记 ✅（合法即 ✅），但**本条的考点 log in／login 那一格根本没被碰到** ⇒ 白测一次。
  改法 ＝ 题面点名"两句的登录都用 **log** 这个词说"。**只点词根，不点词形** ——
  分写还是连写仍然全部由她自己判，考位一个字没漏出去（§6"可点目标词，不许整句给答案"）。
- 2026-09-03 ✅ 复习第1组 [4] · 点名直测 · 题面 `账号被锁了，我登不进去。／登录页面加载很慢。`
  `the account is locked, and I can't **log in**.` ／ `The **login** page is loading very slowly.`
  **考点两句全中**：动词 `log in` 分开写两个词 ／ 名词 `login` 连着写一个词。
  09-01 首犯写的是 `login in`（名词整块当动词用，后面又补一个 in），今天两种词类都摆对 ⇒ 首测即翻正。
  ｜句首小写 `the` 属打字，§2「打字材料里的句读不构成口语证据」，不算问题。
  ★ 本次用的是**今天改过的题面**（当天出题前改，见本条上一行 📝）：加点名「两句的登录都用 log 说」
    —— 堵掉 `sign in`／`the sign-in page` 这条合法绕道，让考位真被测到。**只点词根不点词形**，
    分写还是连写仍由她判 ⇒ 本次 ✅ 是干净的考位数据。
  ⚠️ 同句另外三处（**都不属本条考点，不判 ❌、不新建号**）：
    · `The account` → `My account`（后半句是"我登不进去"，账号是她自己的；The account 是工单口吻）
    · `and` → `so`（中文是因果不是并列）
    · `is loading` → `loads`（**两个都对**：is loading ＝ 此刻正在；loads ＝ 一直都慢。
      中文属性句「登录页面加载很慢」默认说常态 ⇒ 一般现在时更贴。⛔ 这一处绝不是错，不进任何形态类）
  ⇒ 连对0 连错1 → **连对1**（差一次毕业）
- 2026-09-04 ✅ 复习 · 第 1 组 · 中译英两句，动作位与名词位的词形分得干净
  `The account is locked, so I can't **log in**.`（动词，两个词）
  `The **login** page loads slowly.`（名词/定语，一个词）
  ★ 09-03 出题前按 §6.5 第 7 项整改过题面（只钉词根 log、不钉词形）⇒ 两次测的都是真考点
  ★ 09-03 ✅ → 09-04 ✅ ⇒ 连对 2
  ★ 不判的一处（留痕）：09-03 她用 `and`、今天用 `so` 连接前后两句 —— 两个都合法，
    且中文本就是因果 ⇒ 不判、不提。
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 4 题整串，她原话："1-4 直接过"）
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [2] 打包 · `can't log in / login page`
- 2026-09-29 📝 退池 · ③ 口语里测不出
  log in／login 读音完全一样，只是分写连写（§2.1 拼写层）⇒ 口语线测不出；09-01 那次是书面产出里写成 login in
- 备注 **出题口径（两句，一句测动词一句测名词，⛔ 不许只出一句）**：
  只出动词那一句，她永远测不到"什么时候该连着写"；只出名词那一句，考位根本没碰到。
  ★ 这不是 §3.2c 的"合并条"（成员只有 log in 这一个词），是**一个词的两种词类**。
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 317 · when it comes TO sth（说到／在……这件事上）
类型 词组 ｜ 新建 2026-09-03
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-09-04**（连对2 ＝ 09-04 同日两次独立产出：第 1 组点名中译英 ＋ 新题第 2 道自由产出；§3.3 她 08-23 定"同一天多次产出各记一次"）｜ 题型 整句

**问题是什么**
**when it comes TO sth**（说到／在……这件事上）。
判据：
```
when it comes to X        ＝ 说到 X／在 X 这件事上（**引出话题**，后面接名词/动名词）
   When it comes to money, everyone gets careful.
   When it comes to cooking, I'm useless.
   When it comes to **learning** a language, you just have to keep at it.   ← 接动名词
it (all) comes down to X  ＝ 归根到底就是 X（**把一堆原因收成一个**）        ← 🎓#58
   It all comes down to money.
   When it comes down to **it**, …  ← 这是固定说法，后面那个 it **不能换成话题词**
⛔ 她这次的形状 ＝ 把已经会的 comes down to 塞进了 when it comes to 的槽位：
   `when it comes down to modern lifestyle and trends` 读出来是
   "当[某事]归根到底是现代生活方式时" —— 前面根本没有那个"某事" ⇒ 句子挂空。
★ 一句话记：**话题用 to，收束用 down to；差的就是一个 down。**
★ 检查触发：写完 come 那个块，问一句 ——
  **我这里是"说到"还是"归根到底"？"说到" ⇒ 没有 down。**
```
★ 与 🎓**#58**（it mainly comes down to）的**互斥关系（当场写死）**：#58 题面「说到底就是钱的问题。」
　＝ 收束；本条题面「说到网购和穿搭这些…」＝ 引出话题。中文触发词一个是"说到**底**"、一个是"说到"，
　字面互斥，不会撞车。
★ 与 🎓**#284**（boil down to sth）的分工：与 #58 同族（收束），方向与本条相反 ⇒ 无关。
★★ **出题口径**：只出"说到"那一句，⛔ 不在同一题里混进"说到底"（那归 🎓#58／🎓#284）。

**怎么发现的**
2026-09-03 ❌ 首犯 · 新题 P3（question_bank.md:831 · When would old people ask young people for advice?）· 她写
`On top of that, when it **comes down to** modern lifestyle and trends - like online shopping,
fashion choices or entertainment - older people might ask for recommendations…`
（→ when it **comes to** modern lifestyle and trends）
❌ 她要的是**引出话题**，用的却是**收束**那个块；错点收敛到一个词 `down`。
★ 归因：这个错的来源**不是不会，是太熟** —— `comes down to` 是 🎓#58，她在 08-28／08-29 两次都
在题面完全没提的情况下自己接出来过 ⇒ 熟到自动化的块在压力下会去占相邻槽位。
判重结论（§3.1 判重三步，2026-09-03 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
```
① 目标英文形式 ＝ `when it comes to X`（引出话题）
② 全档 grep（**范围含已毕业**）：
   `grep "comes to\|comes down\|it comes" problems.md methods.md`
     ⇒ 🎓#58（it mainly comes down to）· 🎓#284（boil down to）· #56 附近留痕 ·
       L1717 `if he comes tomorrow`（无关，是条件句）
   中文题面 `grep "说到"` ⇒ 只命中 🎓#58／🎓#284 的"说到**底**"
③ 三条最接近的，逐条排除：
   · 🎓#58（it mainly comes down to ＝ 说到底就是）——**形状最像**，同一个动词块。
     **决定性证据**：按 #58 的规则去改她这句，改出来的还是 `comes down to`
     ⇒ **得不到正确答案** ⇒ 不同考点（§3.1③"只是像、目标形式不同 → 两条"）。
     **互斥关系（当场写死）**：#58 题面「说到底就是钱的问题。」＝ 收束；
       本条题面「说到网购和穿搭这些，老人常会问年轻人。」＝ 引出话题。
       中文触发词一个是"说到**底**"、一个是"说到"，字面互斥，不会撞车。
   · 🎓#284（boil down to sth ＝ 说到底就是）——与 #58 同族（收束），方向与本条相反 ⇒ 无关。
     且 #284 的中文触发词 08-23 已被她当场指定为"说到底就是"专属 ⇒ 更不会撞。
   · #56／#63（形态类）——那两条管单复数与冠词；本条是**固定词组选错**，不是形态 ⇒ 无关。
④ 是不是拼写（§2.1 不算错）？**不是** —— 她调出来的是**另一个词组**（多了一个实词 down），
   属「选词」，§2.1④ 判据"她脑子里调的词对不对" ⇒ 照常算。
⑤ 是不是伞形条目（§3.2b）？**不是** —— 目标形式就一个 `when it comes to`，成员数得出来。
```

**我错在哪**
她的：`when it **comes down to** modern lifestyle and trends`
正确：`when it **comes to** modern lifestyle and trends`
找法：写完 come 那个块，问一句 —— **我这里是"说到"还是"归根到底"？**
"说到" ⇒ **没有 down**。

**题面**
"说到做饭，我老公可比我强多了。"（"说到"用 **come** 说）

- 2026-09-03 ❌ 首犯 · 新题 P3（question_bank.md:831 · When would old people ask young people for advice?）·
  `On top of that, when it **comes down to** modern lifestyle and trends - like online shopping,
  fashion choices or entertainment - older people might ask for recommendations…`
  → when it **comes to** modern lifestyle and trends
  ❌ 她要的是**引出话题**（说到现代生活方式和潮流……），用的却是**收束**那个块。
  ★ **错点收敛到一个词 `down`** ⇒ 考点干净、可复测。
  ★ 归因（写下来，下次复测时要用）：这个错的来源**不是不会，是太熟** ——
    `comes down to` 是 🎓#58，她在 08-28／08-29 两次都**在题面完全没提**的情况下自己接出来过。
    熟到自动化的块在压力下会去占相邻槽位 ⇒ 这类错要靠"问自己要哪个意思"挡，不是靠背。
  ★ 同句其余各归各号（§3.3 标记打在条目上，不打在整句上）：
    `to keep up with … or better understand …` ＝ 🎓#98 自发命中（另记）｜
    `current developments` ＝ 🎓#206 书面登记（另记）｜
    `older people` ＝ 🎓#234 自发命中（另记）
  ★ `modern lifestyle` 单数**未判**（判前自审 [C]）：两个形式都合法，没掉形态 ⇒ 连 ⚪ 都不记。
- 2026-09-04 ✅ 复习 · 第 1 组 · 首次复测，考点位一字不差
  `**When it comes to** online shopping and fashion, older people often ask younger generation for advice.`
  ★ 09-03 首犯写的是 `when it comes **down** to` ⇒ 今天 down 没有再出现 ⇒ ✅，连对 0 → 1
  ★ 判前自审留痕（反向偏见自查）：09-03 刚给它写过长归因（"太熟致错、熟块占相邻槽位"），
    存在"想看她再错一次以证明归因"的倾向 ⇒ 强制只看这一句 ⇒ 干净 ✅。
  ★ 同句第二处 `younger generation` 裸单数 ⇒ 归 #56，形态类只记 ⚪，不影响本条档位
    （§3.3「标记打在条目上，不打在整句上」）。
- 2026-09-04 ✅ 新题第 2 道（自由产出 · bank:549 P3 · Who do young people like to share opinions with?）· **同日第二次产出**
  `especially **when it comes to** modern lifestyle and trends - like fasion choices, entertainment…`
  ✅ 考点位一字不差，没有 down。
  ★ 为什么这一次照算（§3.3 她 08-23 定："同一条同一天被产出多次 ⇒ 每次各记一行、各算一次，
    不挑'以谁为准'"）—— 今天第 1 组是**点名中译英**，这一次是**自由产出**，两次独立。
  ★ 三条自我质疑，逐条答完才落定：
    ① 同一天讲评完再测算不算"假 ✅"？—— §3.1 的"假 ✅"只针对**新建当天**；
       本条 09-03 新建、当天未测，今天首测 ⇒ 不在禁令范围内。
    ② 是不是照抄她自己 09-03 的原句？—— **是**（同样的 modern lifestyle and trends／
       fashion choices／entertainment）。但这恰恰是最干净的证据：**同一个句子框，
       昨天带 down、今天不带** ⇒ 修上了。
    ③ §4① 的"加速通道边界"要不要拦？—— 那条拦的是"命中的是她本来就稳的那一半、
       掉的那一格没被测到"；本次命中的**正是掉的那一格**（down 在不在）⇒ 不适用。
  ⇒ 连对 1 → **2**，达线（毕业状态行手工改，见状态行）。
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 6 组（第 4 题整串，她原话："1-4 直接过"）
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [2] 打包 · `when it comes to online shopping and outfit styling`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 come，when it comes to 里有没有 down 留给她（她掉过的是 comes down to 串槽）；换成做饭场景
- 备注 **出题口径**：只出"说到"那一句，⛔ 不在同一题里混进"说到底"——
  "说到底"归 🎓#58／🎓#284，中文触发词已经分掉了，混着出会让她分不清在测哪一条。
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 318 · one time WHEN ＋ 背景，主句装事件（讲往事的挂接顺序）
类型 结构 ｜ 新建 2026-09-04
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-09-07**（连对2 ＝ 09-05 ＋ 09-07）｜ 题型 整句

**问题是什么**
**one time WHEN ＋ 背景，主句装事件**（讲往事的挂接顺序）。
判据：
```
讲一件往事，句子里有三样东西：
  背景A 有一次／有一天        背景B 那时候他几岁／在哪儿／在干嘛     事件 发生了什么
英语的装法固定：**背景全部塞进 when 从句，主句里只装事件**。
  ✓ I remember one time **when** my son was two years old, **he showed me a picture**.
  ✓ I remember **when** my son was two, he once **showed me a picture**.
  ✗ I remember one time my son was two years old, **when** he showed me a picture.
    （主句变成"有一次我儿子两岁"—— 状态不能"发生一次"；事件被降级成从句 ⇒ 句子挂空）
★ 检查触发：写完 `one time` / `one day` 之后问一句 ——
  **我的主句里装的是"发生了什么"吗？** 不是 ⇒ when 挪位。
```
★ 与 🎓**#59**（嵌进句子里用陈述语序）的分工 —— 形状最像（都是从句）：#59 只管"从句里有没有倒装"，
　按它的规则**改不出 when 的位置** ⇒ 不同考点。
★ **不是伞形条目**（§3.2b）：目标形式收敛成一条可复述的规则（背景进 when，事件进主句）。

**怎么发现的**
2026-09-04 ❌ 首犯 · 新题第 1 道（自由产出 · bank:875 P3 · Why do most children draw more often than adults do?）· 她写
`I remember **one time my son was two years old, when he presented** me a picture and pointed three circle on it…`
（→ I remember **one time when my son was two years old, he showed** me a picture…）
❌ 主从颠倒：两样**背景**（有一次 ／ 他两岁）＋ 一件**事**（他给我看画），原句把"他两岁"当成了
one time 的内容，真正的事件反而被 when 挂成了从句 ⇒ 主句里没有"发生了什么"。
★ 归因：她 09-01 写过 `I remember one time users could neither login…`，**那次结构是对的**
⇒ 今天不是老毛病，是**多了一层背景（几岁）之后不知道往哪儿挂** ⇒ 题面必须**带两层背景**才测得到。
判重结论（§3.1 判重三步，2026-09-04 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
```
① 目标英文形式 ＝ `one time **when** ＋ 背景, ＋ 主句事件`（挂接顺序，不是某个词）
② 全档 grep（**范围含已毕业**）：
   `grep "one time"` ⇒ L916（🎓#59 日志里的 `one time (when) we needed to present`，是命中记录不是条目）
                      · L2305／L5200（sessions 引文）· L5733（🎓#316 日志里她 09-01 的正确句）
   `grep "when 从句\|时间状语从句\|背景.*主句"` ⇒ **零命中**
   ⇒ 全档**没有任何条目**管"从句挂接对象"这件事
③ 最接近的一条逐条排除：
   · 🎓#59（直接疑问 vs 嵌入疑问：嵌进句子里就用陈述语序）——形状最像（都是从句）。
     **决定性证据**：按 #59 的规则去改她这句 ⇒ 只会去检查"从句里有没有倒装"，
     她的从句语序本来就是陈述的 ⇒ **改不出 when 的位置** ⇒ 不同考点。
   · #18（论元完整）／🎓#134（能单独站住的动词）——管的是动词带不带宾语 ⇒ 无关。
④ 是不是拼写（§2.1）？**不是**，是结构。
⑤ 是不是伞形条目（§3.2b）？**不是** —— 目标形式收敛成一条可复述的规则
   （背景进 when，事件进主句），⛔ 不是"结构断裂"那种开放集合。
```

**我错在哪**
她的：`I remember **one time my son was two years old, when he presented** me a picture`
正确：`I remember **one time when my son was two years old, he showed** me a picture`
找法：写完 `one time`／`one day` 之后问一句 —— **我的主句里装的是"发生了什么"吗？**
不是（装的是一段状态）⇒ 把 **when 往前挪一格**，让它领住背景。

**题面**
**点名**："我记得有一次，他两岁的时候，把一张画拿给我看。"（用 **one time** 起头说）

- 2026-09-04 ❌ 首犯 · 新题第 1 道（自由产出 · bank:875 P3 · Why do most children draw more often than adults do?）·
  `I remember **one time my son was two years old, when he presented** me a picture and pointed three circle on it…`
  → I remember **one time when my son was two years old, he showed** me a picture…
  ❌ 主从颠倒：她有两样**背景**（有一次 ／ 他两岁）和一件**事**（他给我看画）。
  原句把"他两岁"当成了 one time 的内容（"有一次我儿子两岁"—— 两岁是一段状态，
  不是能发生"一次"的事），真正的事件反而被 when 挂成了从句 ⇒ 主句里没有"发生了什么"。
  ★ 修法只有一个动作：**把 when 往前挪一格**，让它领住背景，事件回到主句。
  ★ 归因（下次复测要用）：她 09-01 写过 `I remember one time users could neither login…`，
    **那次结构是对的**（one time 后面直接接事件）⇒ 今天不是老毛病，是
    **多了一层背景（几岁）之后不知道往哪儿挂**。⇒ 题面必须**带两层背景**才测得到。
- 2026-09-05 ✅ 在池组 · 第 1 组（付息日 a 段）
  `I remember one time when he was two years old, he showed me a picture.`
  挂接顺序正确：when 领住两层背景（有一次 ＋ 他两岁），主句装事件（he showed me a picture）。
  ★ 09-04 首犯时主句成了"有一次我儿子两岁"（状态当事件），今天 when 挪到了正确的位置。
  ｜ ⚠️ he → my son（第一次提到先给身份）／two years old → two，diff-2 已给，不记 ❌
- 2026-09-07 ✅ 复习 · 在池第 1 组 · `I remember one time when he was two, he shown me a picture.`
  —— one time when ＋ 背景、主句装事件，挂接顺序全对 ⇒ 连对 2，**毕业**
  （shown 是形态类，只记 ⚪ 到 #93，不影响本条）
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 7 组（她原话："5-9 直接过"）
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [8] · `One time, when he was two year old, he brought a drawing over to show me.` —— one time, when ＋ 背景，主句装事件
  ★ two year old 的 -s ⇒ ⚪#150，不属本条
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 319 · present sth TO sb ／ present sb WITH sth（present 不进双宾语那一族）
类型 搭配 ｜ 新建 2026-09-04
状态 连对2 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ 题型 整句 ｜ **回潮 2026-09-11**（09-07 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零；09-05／09-07 两次 ✅ 之后隔 3 个练习日就忘 ⇒ 没长稳）

**问题是什么**
**present sth TO sb ／ present sb WITH sth** —— present 只有这两个框，⛔ 不进双宾语那一族。
判据：
```
present 的两个框（记框，不记单词）：
  present sth **to** sb      The principal presented a medal **to** him.
  present sb **with** sth    The principal presented him **with** a medal.
⛔ present sb sth           ✗ The principal presented him a medal.
★ 语域：present ＝ 颁发／正式呈递（present an award／present a report／present your ID）。
  **日常"给某人看／递给某人"一律 show／give**，⛔ 别升到 present。
  （2026-09-04 的原句就是这个毛病：两岁孩子把画拿给妈妈看 ⇒ 口语只用 show。）
```
判据一句话：这个动词进不进双宾语那一族？present 不进 ⇒ 人在前带 **with**、东西在前带 **to**。
★ 与 🎓#263（双宾语语序：promise／give／tell／show／send 一律"人在前、东西在后"）的分工：
　#263 考的是**族内**五个动词的语序，本条考的是 present 这个**族外**动词的框；
　中文触发词也分开 —— #263 ＝"他答应给儿子买最新款手机／她给了我一本很旧的书"，本条 ＝"校长给他颁了一块奖牌"。
　⇒ 09-04 那次她的**语序是对的**，错在把 #263 的规则过度泛化到不属于那一族的动词上；
　　 这类错⛔不能靠再背一遍双宾语语序来修（越背越往外套），只能靠"这个动词进不进那一族"这一问挡。

**怎么发现的**
2026-09-04 ❌ 首犯 · 新题第 1 道（自由产出 · bank:875 P3）· 她的原话
`he **presented me a picture** and pointed three circle on it`
（→ presented me **with** a picture ／（口语档）**showed** me a picture）。
判重结论（§3.1 判重三步，2026-09-04 当天做，逐条人读）：**保留新建**
```
① 目标英文形式 ＝ `present sb **with** sth`（或 `present sth **to** sb`）
② 全档 grep（**范围含已毕业**）：
   `grep "present"` ⇒ L916（🎓#59 日志里的 `needed to present`，动词"做演示"，无关）
                     · L1615（`the present` ＝ 名词"现在"，无关）⇒ **无条目**
③ 最接近的一条：**🎓#263（双宾语语序：promise／give／tell／show／send 一律【人在前，东西在后】）**
   **决定性证据**：按 #263 的规则去改她这句 ⇒ 她的语序**已经是"人在前、东西在后"**
   ⇒ **改不出 with** ⇒ 得不到正确答案 ⇒ 不同考点（§3.1③"只是像、目标形式不同 → 两条"）。
   **互斥关系（当场写死）**：#263 题面考的是 promise／give／tell／show／send 五个**族内**动词的语序；
     本条题面考的是 present 这个**族外**动词的框。中文触发词也分开：
     #263 ＝"他答应给儿子买最新款手机／她给了我一本很旧的书"；本条 ＝"校长给他颁了一块奖牌"。
   ⇒ #263 只在 09-04 记一行 📝（过度泛化留痕），⛔ 不判回潮。
④ 是不是拼写（§2.1）？**不是**，是动词的框（搭配）。
⑤ 是不是伞形条目（§3.2b）？**不是** —— 就 present 一个动词、两个框，成员数得出来。
```
2026-09-11 付息日 a2 第 7 组复检：她答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**。

**我错在哪**
她的：`he presented me a picture`（09-04 首犯）／ 答"忘了"（09-11 复检）
正确：`presented him with a medal` ／ `presented me with a picture`（日常场景则整个换成 showed me a picture）
找法：写 present 之前先问一句 —— 人在前还是东西在前？人在前补 **with**，东西在前补 **to**；⛔ 中间什么都不加是错的。

**题面**
"公司年会上，老板给她颁了一个最佳员工奖。"（"颁"用 **present** 说）

- 2026-09-04 ❌ 首犯 · 新题第 1 道（自由产出 · bank:875 P3）·
  `he **presented me a picture** and pointed three circle on it`
  → presented me **with** a picture ／（口语档）**showed** me a picture
  ❌ present 只有两个框：`present sth **to** sb` ／ `present sb **with** sth`。
  它**不进** give／show／send／tell／promise 那一族（动词 ＋ 人 ＋ 东西直接上）。
  ★ 归因（下次复测要用）：她的**语序是对的** —— 这是 🎓#263 的规则她执行得没问题；
    错在**把 #263 的规则过度泛化到不属于那一族的动词上**。
    ⇒ 这类错不能靠"再背一遍双宾语语序"修（越背越会往外套），
      只能靠"这个动词进不进那一族"这一问挡。
- 2026-09-05 ✅ 在池组 · 第 1 组（付息日 a 段）
  `The principal presented him with a medal.`
  框选对：present sb **with** sth，⛔ 没有落回 09-04 的 present sb sth（双宾语过度泛化）。
  ★ 她同时主动提出「principal 这个词要背」⇒ 按 §2③／§2.1③ 另建 #321，⛔ 不并进本条
    （本条考动词的框，#321 考这个名词本身）
- 2026-09-07 ✅ 复习 · 在池第 2 组 · `presented him with a medal.`
  —— present sb **with** sth 的框选对，⛔ 没有落回 09-04 的双宾语过度泛化 ⇒ 连对 2，**毕业**
- 2026-09-11 ❌ 复检 · 付息日 a2 第 7 组 · 答"忘了"（§3.3「忘了/不会」＝ ❌）⇒ **回潮**
  最小改 `presented him with a medal`
  ❌ present 不进双宾语那一族（⛔ present him a medal）：人在前带 **with**（present sb with sth），东西在前带 **to**（present sth to sb）。
  ★ 09-04 建号、09-05／09-07 两次 ✅，隔 3 个练习日再测忘了 ⇒ 没长稳
- 2026-09-13 ✅ 学习日 在池第 2 组 · `present him with a medal.`——present sb WITH sth（09-11 回潮后首测）
- 2026-09-15 ✅ 学习日 在池第 2 组 · `present him with a medal.` —— present sb WITH sth → **连对2，毕业**
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"＋ 人在前"结构提示，只点名 present，with／to 怎么挂留给她；换成年会颁奖场景
- 2026-09-30 ✅ 复检 · 付息日 a2 第 4 组 [1] · `the mayor personally presented the trophy to the campion.`
- 备注 **出题口径**：题面必须用 present **真正合适**的场合（颁奖／递交／正式呈上）。
  ⛔ 不出"孩子给妈妈看画"这种日常场景 —— 那种场景的正确答案是 show，出了会**教反**。
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 320 · point AT sth（指着某样东西）
类型 搭配 ｜ 新建 2026-09-04
状态 连对2 连错0 上次2026-09-26 ｜ **🎓 已毕业 2026-09-07**（连对2 ＝ 09-05 ＋ 09-07）｜ 题型 整句

**问题是什么**
**point AT sth**（指着某样东西）。
判据：
```
指着一个目标            point **at** sth        He pointed **at** the photo on the wall.
把某物瞄准某处（及物）   point sth **at** sth    He pointed the camera **at** me.
★ 检查触发：写完 point，问一句 —— **我是在"指"，还是在"把某个东西瞄准"？**
  在"指" ⇒ point 后面必须先出现 **at**。
```
★ 本条考点是"表'指'时 point 后面的**介词不能省**"（point **to** 在物理指认时同样地道，答它算对）。
★ 同一格里的邻居（别串，⛔ 不并进本条）：`point sth **out**` ＝ 指出来／点明 —— **另一个块**，
　意思是"把没人注意到的东西说出来"，不是用手指。
★ 与 🎓**#229**（complain 不及物，带 about）的分工 —— 形状最像（都是"这个动词后面要带介词"），
　但按 #229 的规则只产出 about，**产不出 at** ⇒ 不同考点。
★ 与 **#18**（论元完整）的分工 —— **方向相反**：她**给了**宾语，缺的是介词。

**怎么发现的**
2026-09-04 ❌ 首犯 · 新题第 1 道（自由产出 · bank:875 P3）· 她写
`he presented me a picture and **pointed three circle** on it`（→ **pointed at** three circles on it）
❌ point 表"指"时后面必须带介词：**point at sth**。裸的 `point sth` 只在"把某物瞄准某处"时成立
（point a gun at sb），那时的宾语是**被举起来瞄准的那个东西**，不是"被指的目标"。
判重结论（§3.1 判重三步，2026-09-04 当天做，逐条人读）：**保留新建**
```
① 目标英文形式 ＝ `point **at** sth`
② 全档 grep（**范围含已毕业**）：`grep "point at\|pointed\|point to"` ⇒ **零命中**
③ 最接近的三条逐条排除：
   · 🎓#229（complain 不及物，带 about）——形状最像（都是"这个动词后面要带介词"）。
     **决定性证据**：按 #229 的规则去改她这句 ⇒ 只产出 about，**产不出 at** ⇒ 不同考点。
   · #18（论元完整：中文可单说的动词，英文必须带宾语/补语）——**方向相反**：
     她**给了**宾语（three circle），缺的是介词 ⇒ 无关。
   · 🎓#134（不是所有动词都要宾语·白名单）——那条是"可以不带宾语"，与本次无关。
④ 是不是拼写（§2.1）？**不是**，是缺一个介词。
⑤ 是不是伞形条目（§3.2b）？**不是** —— 目标形式就一个 `point at`；
   ⛔ 没有开成"动词后面要带介词"那种开放集合（那才是伞形）。
```

**我错在哪**
她的：`he presented me a picture and **pointed three circle** on it`
正确：`**pointed at** three circles on it`
找法：写完 point，问一句 —— **我是在"指"，还是在"把某个东西瞄准"？**
在"指" ⇒ point 后面必须先出现 **at**。

**题面**
"孩子指着天上的飞机，兴奋得直叫。"（"指着"用 **point** 说）
★ point at／point to 都算对；她掉过的是 point 后面不带介词（pointed three circles）

- 2026-09-04 ❌ 首犯 · 新题第 1 道（自由产出 · bank:875 P3）·
  `he presented me a picture and **pointed three circle** on it`
  → **pointed at** three circles on it
  ❌ point 表"指"时后面必须带介词：**point at sth**。
  裸的 `point sth` 只在"把某物瞄准某处"时成立（point a gun at sb ／ point the camera at…），
  那时的宾语是**被举起来瞄准的那个东西**，不是"被指的目标"。
  ｜同处 `three circle` → three **circles** 归 #150（形态类，只记 ⚪，不算在本条头上）
- 2026-09-05 ✅ 在池组 · 第 1 组（付息日 a 段）
  `he pointed at the picture on the wall.`
  point **at** sth，介词带上了，⛔ 没有落回 09-04 的裸 `pointed three circle`。
- 2026-09-07 📝 题面补一条排除「⛔ 不许用 to」：point **to** 在物理指认时同样地道 ⇒ 第二译法没被收敛。
  本条考点是"表'指'时 point 后面的介词不能省"（见备注），排除 to 之后考点原样保留、也没给出 at。
- 2026-09-07 ✅ 复习 · 在池第 2 组 · `point at the picture on the wall`
  —— 表"指"时介词没省，⛔ 没有落回 09-04 的裸 `pointed three circle` ⇒ 连对 2，**毕业**
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 7 组（打包串，她原话："除了 3）忘了，其他直接过"）
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [9] · `Pointing at that photo on the wall.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 去负向排除）· 题型 词组 → 整句
  去掉"⛔ to"（point to 同样地道，算对），只点名 point；换成孩子指飞机场景
- 备注 **不当考点的邻居**（写在这里防混，⛔ 不并进本条、不出题）：
  `point sth **out**` ＝ 指出来／点明（She pointed out two mistakes.）——**另一个块**，
  意思是"把没人注意到的东西说出来"，不是用手指。若日后她掉这个，另开号。
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 321 · principal ＝ 校长（≠ principle ＝ 原则）
类型 词汇 ｜ 新建 2026-09-05
状态 连对2 连错0 上次2026-09-27 ｜ **🎓 已毕业 2026-09-10**（连对2 ＝ 09-07 ✅ ＋ 09-10 ✅；09-05 建号后第一次毕业，中途零回潮）｜ 退池 ｜ 题型 词组

**问题是什么**
**principal ＝ 校长**（≠ **principle** ＝ 原则）。
判据：
```
principal   名词 ＝ 校长／形容词 ＝ 主要的      the principal of the school ／ the principal reason
principle   名词 ＝ 原则、准则                  on principle ／ It's a matter of principle.
★ 两个词读音一模一样，靠**位置**分：
  后面能接 of the school、前面能加 the 指一个人 ⇒ principal（校长）
  说"做人的准则／原则问题" ⇒ principle
★ 口语退路（不想背时一样对）：the head teacher（英）／the head of the school
★ 检查触发：写完"校长"，问一句 —— 我指的是**一个人**还是**一条道理**？
  人 ⇒ principal（-pal 结尾，和 pal「伙伴」同尾，人）
```
★ 同一格里的邻居（别串，⛔ 不并进本条、不出题）：形容词 `principal` ＝ 主要的
　（the principal reason／the principal cause）—— 同一个词的另一个词性，本条只出**名词义**。
★ 与 **#319**（present sth to sb ／ present sb with sth）的**互斥关系（当场写死）**：
　#319 考 **present 这个动词的框**（"校长"只是场景、不在产出位置）；本条考 **principal 这个名词本身**
　⇒ 两条题面不撞车。
★ 与 🎓**#227**（clear ≠ clean）／**#255**（vital ≠ virtual）的分工：都是"形近/音近词选错"这一**形状**，
　但各自锁死在自己那一对词上 ⇒ 不同考点；⛔ 也**不能**并成"形近词"伞形条（开放集合，§3.2b 禁止）。

**怎么发现的**
2026-09-05 📝 **她主动提出建号** · 在池组第 1 组（#319 的作答里自标）· 她写
`The principal(这个词要背) presented him with a medal.`
★ 她**拼对了、用对了**，⛔ 不是拼写错 —— 走 §2.1③「她主动说这个要记」这唯一一条例外建号。
判重结论（§3.1 判重三步，2026-09-05 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
```
① 目标英文形式 ＝ 名词 `principal`（＝ 校长）
② 全档 grep（**范围含已毕业**）：
   `grep -n "principal\|principle\|校长" problems.md graduated.md methods.md`
   ⇒ 5 处命中**全部落在 #319 内部**（题面 1 ＋ 判据例句 3 ＋ 判重结论 1）⇒ 全档**无条目**
③ 最接近的一条逐条排除：
   · #319（present sth to sb ／ present sb with sth）——同一句话里出来的，形状最近。
     **决定性证据**：按 #319 的规则去改这一处 ⇒ 只会去检查介词框（with ／ to），
     **产不出"校长这个词怎么说"** ⇒ 得不到目标形式 ⇒ 不同考点（§3.1③ 第三档）。
     **互斥关系（当场写死）**：#319 题面 ＝ "校长给他颁了一块奖牌。"（点名用 present，
     "校长"只是场景、不在产出位置）；本条题面 ＝ "校长在毕业典礼上讲了话。"
     （点名"校长"用一个词说，动词随便）⇒ 两条题面不撞车。
   · 🎓#227（clear ≠ clean）／#255（vital ≠ virtual）——都是"形近/音近词选错"这一**形状**。
     **决定性证据**：它们各自锁死在自己那一对词上（clear/clean · vital/virtual），
     按它们的规则改**产不出 principal** ⇒ 不同考点。
     ⛔ 也**不能**把三条并成"形近词"伞形条 —— 那是开放集合（§3.2b 明令禁止）。
④ 是不是拼写（§2.1）？**不是** —— 她拼对了、用对了，是她**主动要求记**，走 §2.1③ 例外。
⑤ 是不是伞形条目（§3.2b）？**不是** —— 目标形式就一个词 `principal`，
   成员数得出来（一个名词义 ＋ 一个防混邻居），⛔ 没有开成"所有形近词"。
```

**我错在哪**
她这次没有错（`The principal presented him with a medal.` 拼对了、也用对了），
建号理由是 §2③／§2.1③ **她点名要背**（原话写在句子里："这个词要背"）。
找法：写完"校长"，问一句 —— 我指的是**一个人**还是**一条道理**？
人 ⇒ **principal**（-pal 结尾，和 pal「伙伴」同尾，人）；道理 ⇒ principle。

**题面**
**点名**："校长"（用一个词说，⛔ 不用 head teacher · ⛔ 不用 headmaster）
★ 题面 2026-09-07 补一条排除「⛔ 不用 headmaster」：原题面只排除了 head teacher，而 headmaster 同样是"一个词"、且在英式里正是默认词 ⇒ 第二译法没被收敛（§6.5 第 7 项）。补掉它之后 principal／principle 这个真考点一个字都没泄露

- 2026-09-05 📝 她主动提出建号 · 在池组第 1 组（#319 的作答里自标）·
  `The principal(这个词要背) presented him with a medal.`
  ★ 她**拼对了、用对了**，⛔ 不是拼写错 —— 走 §2.1③「她主动说这个要记」这唯一一条例外建号。
  ★ 与 #319 的分工写死：#319 考 **present 这个动词的框**（校长只是场景，不在产出位置上）；
    本条考 **principal 这个名词本身**，题面必须把"校长"摆到要她产出的位置上。
- 2026-09-07 📝 题面补一条排除「⛔ 不用 headmaster」：原题面只排除了 head teacher，
  而 headmaster 同样是"一个词"、且在英式里正是默认词 ⇒ 第二译法没被收敛（§6.5 第 7 项）。
  补掉它之后 principal／principle 这个真考点一个字都没泄露。
- 2026-09-07 ✅ 复习 · 在池第 2 组 · `principal` —— 首测；principal（校长）≠ principle（原则），调对了词
- 2026-09-10 ✅ 复习 · 在池第 1 组 · `principal` —— 一字不差 ⇒ **连对2，毕业**
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 退池 · ③ 口语里测不出
  principal／principle 读音完全一样，两者只差拼写（§2.1 拼写层，口语线不算）；"校长"说 head teacher 也地道 ⇒ 口语里测不出缺口
- 备注 **不当考点的邻居**（写在这里防混，⛔ 不并进本条、不出题）：
  形容词 `principal` ＝ 主要的（the principal reason／the principal cause）——同一个词的另一个词性，
  她掉的是"校长"这个名词义 ⇒ 出题只出名词义。若日后形容词义单独掉，另开号。
- ⇒ **新建当天不测**（§3.1），下一个练习日起进池

### 322 · play WITH sth（玩"东西"一律带 with）
类型 搭配 ｜ 新建 2026-09-07
状态 连对2 连错0 上次2026-09-30 ｜ **回潮 2026-09-28**（09-11 毕业 → 09-28 复检 [5]／[8] 两次漏 with，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-30**（连对2 ＝ 09-29 ＋ 09-30；09-28 回潮后第二次毕业）｜ 题型 整句

**问题是什么**
**play WITH sth**（玩"东西"一律带 with）。
判据：
```
玩"东西"     play **with** sth      play with toys ／ play with the dog ／ play with your phone
玩"项目"     play ＋ 名词（不带 with）play football ／ play the piano ／ play a game ／ play a role
★ 判据一句话：后面是**一个东西** ⇒ 必须有 with；后面是**一项活动** ⇒ 直接接。
★ 检查触发：写完 play，问一句 —— 我后面接的是东西还是活动？
```
★ 与 🎓**#51**（put sth away ＝ 收起来）／🎓**#67**（可分离动词短语的位置）的**互斥关系（当场写死）**：
　那两条的题面都以"收起来"为落点（put away），本条题面以"在玩"为落点（play with）⇒ 不撞车；
　按它们的规则去改她这两句都**产不出 with** ⇒ 不同考点。

**怎么发现的**
2026-09-07 📝 首犯 · 复检第 5 组 [6]（#215 的作答里，**同一题犯了两次**）· 她写
`kids put toys away after **playing them**.` ／ `After kids **played toys**, I put them away.`
（→ playing **with** them ／ played **with** the toys）
★ 建号理由：这条搭配 2026-08-21 只作为 🎓#67 的一行**备注**被提过一次
（「另：away 不变形；玩具搭配是 play with」），**从来没有自己的编号** ⇒ 从来没进过召回队列
⇒ 今天同一题里连犯两次，正是"讲过但没测过"的典型。
判重结论（§3.1 判重三步，2026-09-07 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
```
① 目标英文形式 ＝ `play **with** sth`
② 全档 grep（**范围含已毕业**）：`grep -n "play with\|玩具\|play toys" problems.md graduated.md methods.md`
   ⇒ 4 处命中，逐条读：
   · 🎓#51（put sth away ＝ 收起来）题面"把玩具收回去" —— 只是同一个名词出现，考点是 put away
   · 🎓#67（可分离动词短语的位置）题面里也有玩具 —— 考点是代词必须摆中间
   · 🎓#67 的**备注行**「玩具搭配是 play with」—— ★ 决定性事实：只是备注，**全档无条目**
   · #215（-ing 短语的逻辑主语）题面里有玩具 —— 考点是逻辑主语＝主句主语
③ 最接近的两条逐条排除：
   · 🎓#67 —— 按它的规则去改她这两句 ⇒ 只会检查 them 有没有摆在 put 和 away 中间，
     **产不出 with** ⇒ 不同考点（§3.1③ 第三档）
   · 🎓#51 —— 按它的规则改 ⇒ 只会把 clean up 换成 put away ⇒ 产不出 with ⇒ 不同考点
   **互斥关系（当场写死）**：#51／#67 的题面都以"收起来"为落点（put away），
   本条题面以"在玩"为落点（play with），⛔ 两边题面不撞车。
④ 是不是拼写（§2.1）？**不是**，是缺一个介词。
⑤ 是不是伞形条目（§3.2b）？**不是** —— 目标形式就一个 `play with`，成员数得出来。
```

**我错在哪**
她的：`kids put toys away after **playing them**.` ／ `After kids **played toys**, …`
正确：`after playing **with** them` ／ `After kids played **with** the toys, …`
找法：写完 play，问一句 —— **后面接的是"东西"还是"一项活动"？**
东西 ⇒ 必须有 **with**。

**题面**
"孩子在玩他们的玩具。"（"玩"用 **play** 说）

- 2026-09-07 📝 首犯 · 复检第 5 组 [6]（#215 的作答里，**同一题犯了两次**）·
  `kids put toys away after **playing them**.` ／ `After kids **played toys**, I put them away.`
  → playing **with** them ／ played **with** the toys
  ★ 建号理由：这条搭配 2026-08-21 只作为 🎓#67 的一行**备注**被提过一次
    （「另：away 不变形；玩具搭配是 play with」），**从来没有自己的编号** ⇒ 从来没进过召回队列
    ⇒ 今天同一题里连犯两次，正是"讲过但没测过"的典型。
- 2026-09-09 ⚡ 自评免测 · 在池第 2 组（她原话："前 7 题直接过"）
- 2026-09-11 ⚡ 自评免测 · 付息日 a 段第 1 组（她原话："6. 直接过"）⇒ 连对1 → 连对2 **毕业**（§4③：⚡ 够 2 ＝ 她行使直接指定毕业）
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 2026-09-28 ❌ 复检第 2 组 [5]（#67 那题顺带）· `After playing toys` 漏 with
- 2026-09-28 ❌ 复检第 2 组 [8] · `Children are playing their toys.` 漏 with —— **回潮**
- 2026-09-29 ✅ 在池第 1 组 · `Kids are playing with their toys.`
- 2026-09-30 ✅ 付息日 a 段在池第 1 组 [2] · `My cat can play with a cardboard for an entire afternoon.`（with 到位；a cardboard 另建 #375）⇒ 连对2 **毕业**
- ⇒ **新建当天不测**（§3.1），下一个练习日起进池

### 323 · 嵌入疑问的 wh 词不能吞（know **what** they want）
类型 结构 ｜ 新建 2026-09-07
状态 连对2 连错0 上次2026-09-28 ｜ **🎓 已毕业 2026-09-11**（连对2 ＝ 09-09 ✅ ＋ 09-11 ✅）｜ 题型 整句

**问题是什么**
嵌入疑问的 **wh 词不能吞**（know **what** they want）。
判据：
```
know／tell／wonder／figure out 后面接嵌入成分时，**每一个成分都要有自己的 wh 词领头**：
  know **what** they want ／ know **how** to do it ／ know **why** it matters ／ know **where** to start
并列两个的时候两个 wh 都要出现：know **what** they want and **how** to get there.
★ 这里的 what 是双重身份：既是连接词、又是 want 的**宾语** ⇒ 吞掉它，want 就没宾语了。
★ 检查触发：写完 know／tell／wonder／figure out，数后面有几个成分，每个是不是都有 wh 领头。
```
★ 与 🎓**#59**（嵌进句子里就用陈述语序）的分工 —— 形状最像（都是 wh 从句）：她这句从句里本来就是
　陈述语序，按 #59 的规则去改 **产不出 what** ⇒ 不同考点。
★ 与 **#46**（表语用名词说，不用 what 从句）的**互斥关系（当场写死）**：#46 题面是**表语位置**、⛔ 禁用
　what 从句；本条题面是 know 的**宾语位置**、**必须**用 what ⇒ 方向相反，两条题面不撞车。
★ **不是伞形条目**（§3.2b）：收敛成一条规则（wh 词不能吞），成员是封闭的 wh 词表。

**怎么发现的**
2026-09-07 📝 首犯 · 新题第 1 道（自由产出 · bank:975 P3 · Do you think smart children are happier than other children?）· 她写
`smart enough to know **they actually want** and how to reach their gold`
（→ to know **what** they actually want and how to reach their goals）
❌ want 是及物的，后面必须有宾语，而这里的宾语正是那个 what。
★ 归因：know 后面并列了两个嵌入成分 —— 第二个的 how **她写了**，第一个的 what 吞掉了
⇒ 不是"不知道要用 wh"，是**并列时第一个被跳过**。
判重结论（§3.1 判重三步，2026-09-07 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
```
① 目标英文形式 ＝ `know **what** …` —— 考的是 wh 词的**有无**
② 全档 grep（**范围含已毕业**）：`grep -n "嵌入疑问\|what 从句\|宾语从句\|know what" problems.md graduated.md`
   ⇒ 逐条读：🎓#59（直接疑问 vs 嵌入疑问）· #46（表语用名词，不用 what 从句）· #59 的两条合并备注
③ 最接近的两条逐条排除：
   · 🎓#59（嵌进句子里就用陈述语序）——形状最像（都是 wh 从句）。
     **决定性证据**：她这句从句里本来就是陈述语序（`they actually want`），
     按 #59 的规则去改 ⇒ **产不出 what** ⇒ 得不到目标形式 ⇒ 不同考点（§3.1③ 第三档）。
   · #46（表语用名词说，不用 what 从句）——**方向相反**：那条禁用 what 从句，本条要求别吞。
     **互斥关系（当场写死）**：#46 题面 ＝ "业余爱好是自己挑的事，工作不是。"（表语位置，⛔ what 从句）；
     本条题面 ＝ "聪明到知道自己到底要什么、也知道怎么去够到。"（know 的宾语位置，**必须**用 what）
     ⇒ 两条题面不撞车。
④ 是不是拼写（§2.1）？**不是**，是缺一个功能词。
⑤ 是不是伞形条目（§3.2b）？**不是** —— 收敛成一条规则（wh 词不能吞），成员是封闭的 wh 词表。
```

**我错在哪**
她的：`smart enough to know **they actually want** and how to reach their gold`
正确：`smart enough to know **what** they actually want and how to reach their goals`
找法：写完 know／tell／wonder／figure out，**数一数后面有几个成分** ——
每一个都得有自己的 wh 词领头（并列的第二个写了，别把第一个吞掉）。

**题面**
"他聪明到知道自己到底要什么、也知道怎么去够到。"（用 **know** 起头的一个不定式说）

- 2026-09-07 📝 首犯 · 新题第 1 道（自由产出 · bank:975 P3 · Do you think smart children are happier than other children?）·
  `smart enough to know **they actually want** and how to reach their gold`
  → to know **what** they actually want and how to reach their goals
  ❌ want 是及物的，后面必须有宾语，而这里的宾语正是那个 what。
  ★ 归因（下次复测要用）：know 后面并列了两个嵌入成分 —— 第二个的 how **她写了**，
    第一个的 what 吞掉了 ⇒ 不是"不知道要用 wh"，是并列时第一个被跳过。
- 2026-09-09 ✅ 复习 · 在池第 2 组 · `Smart enough to know exactly what they want and how to get it.`
  —— 嵌入疑问的两个 wh 词（what／how）都没被吞，后面都是陈述语序；"到底" 用 exactly 落位
- 2026-09-11 ✅ 付息日 a 段 · 第 1 组 · `smart enough to know what he wants and how to get it.`
  —— know 后面并列的两个嵌入疑问 what／how 一个没吞 ⇒ 连对2 **毕业**
  ★ 发出时题面缺主语（"聪明到知道…"），她自己补了 he —— 教练的锅，⛔ 不扣分；同日 📝 整改
- 2026-09-11 📝 题面整改：补主语「他」· 她当场点出（原话："整句（翻译）需要完全的句子"）
  旧 "聪明到知道自己到底要什么、也知道怎么去够到。"（用 **know** 起头的一个不定式说）
  新 "他聪明到知道自己到底要什么、也知道怎么去够到。"（用 **know** 起头的一个不定式说）
  ⇒ 考点靠句子现形 ⇒ 整句题 ⇒ §6.5⑥ 要求有主语、能独立成句；旧题面正是那条的反例形状
- 2026-09-18 ⚡ 自评免测 · 复检第 3 组
- 2026-09-28 ✅ 复检第 2 组 · `he's smart enough to know what he really wants and how to reach it.`
- ⇒ **新建当天不测**（§3.1），下一个练习日起进池

### 325 · obstacle course（闯关设施／障碍训练场）
类型 词汇 ｜ 新建 2026-09-09
状态 连对2 连错0 上次2026-09-29 ｜ **🎓 已毕业 2026-09-13** ｜ 题型 词组

**问题是什么**
整套闯关设施 ＝ **an obstacle course**（course 本身就含"一条路线"）；单个项目 ＝ **an obstacle**。
同一格里的邻居（别串）：⛔ 不说 facility（那是"设施/场馆"这种大词，指的是建筑不是项目）。
判据一句话：说的是**一整条路线／一整套关卡** ⇒ obstacle course；只说**其中一个障碍** ⇒ an obstacle。

**怎么发现的**
2026-09-09 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个词我查字典，一开始想写有了设施，但是也不会写"。
判重结论 全档 grep `obstacle` 零命中 ⇒ 保留（⛔ 建号当天不测，次日起进队列）
2026-09-10 ✅ 复习 · 在池第 1 组首测 · `an obstacle course` —— 两个词一字不差。

**我错在哪**
她的：想写"设施"但"也不会写"（2026-09-09 自标不会，⛔ 不是产出错）　　正确：`an obstacle course`
找法：中文想到"设施"先停一下 —— 是一整套闯关路线吗？是就用 obstacle course，⛔ 别去够 facility。

**题面**
"儿童乐园里那条障碍闯关路线"（爬网、过独木桥的一整套关卡）

- 2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个词我查字典，一开始想写有了设施，但是也不会写"
  条目内容：整套闯关设施 ＝ **an obstacle course**（course 本身就含"一条路线"）；单个项目 ＝ **an obstacle**。
  ⛔ 不说 facility（那是"设施/场馆"这种大词，指的是建筑不是项目）。
- 2026-09-10 ✅ 复习 · 在池第 1 组（首测）· `an obstacle course` —— 两个词一字不差
- 2026-09-13 ✅ 学习日 在池第 2 组 · `an obstacle course.`——**连对 2，毕业**
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-28 📝 学习日 新题 bank:915（P2）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）· `I went on an obstacle course with my 5-year-old son`
- 2026-09-29 ✅ 复检第 2 组 · `an obstacle course.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉首字母／词数／排除项，改成中文释义（一整套关卡）；换成儿童乐园场景

### 326 · stamina（耐力）
类型 词汇 ｜ 新建 2026-09-09
状态 连对2 连错0 上次2026-09-29 ｜ **🎓 已毕业 2026-09-13** ｜ 题型 词组

**问题是什么**
**stamina** ＝ 长时间撑下来的耐力（**不可数**，⛔ 无复数）。
同一格里的邻居（别串）：strength ＝ 力气（一下子的力量）· energy ＝ 精力/能量 · stamina ＝ 能撑多久。
判据一句话：说的是"能撑多久"⇒ stamina；"一下子多大劲"⇒ strength；"有没有精神头"⇒ energy。

**怎么发现的**
2026-09-09 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个词需要背下"。
判重结论 全档 grep `stamina` 零命中 ⇒ 保留（⛔ 建号当天不测）
2026-09-10 ✅ 复习 · 在池第 1 组首测 · `stamina` —— 一字不差。

**我错在哪**
她的：自标"这个词需要背下"（2026-09-09；⛔ 不是产出错，是她点名要背的词）　　正确：`stamina`
找法：中文说到"耐力／撑得住"先问一句 —— 是"能撑多久"吗？是就用 stamina，⛔ 别拿 energy／strength 顶。

**题面**
"跑长跑最要紧的那股耐力"（能撑多久的劲儿，不是力气大小）

- 2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个词需要背下"
  条目内容：**stamina** ＝ 长时间撑下来的耐力（**不可数**，⛔ 无复数）。
  同族三个别混：strength ＝ 力气（一下子的力量）· energy ＝ 精力/能量 · stamina ＝ 能撑多久。
- 2026-09-10 ✅ 复习 · 在池第 1 组（首测）· `stamina` —— 一字不差
- 2026-09-13 ✅ 学习日 在池第 2 组 · `stamina`——**连对 2，毕业**
- 2026-09-19 ✅ 复检 · 付息日 a2 复检第 2 组（打包 [2]）· `stamina`
- 2026-09-29 ✅ 复检第 2 组 · `stamina.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉首字母／词数／排除项，改成中文释义（能撑多久，不是力气大小）；endurance 同样算对

### 327 · 踏脚点 ＝ foothold ／ peg
类型 词汇 ｜ 新建 2026-09-09
状态 连对2 连错0 上次2026-10-01 ｜ **回潮 2026-09-29**（09-13 毕业 → 09-29 复检 foothold 答成 footsteps，撤销毕业、连对清零）｜ **🎓 已毕业 2026-10-01**（连对2 ＝ 09-30 ＋ 10-01；09-29 回潮后第二次毕业）｜ 题型 词组

**问题是什么**
脚能踩的那个点 ＝ **a foothold**（通用）；钉在柱子上、只够踩一只脚的小桩 ＝ **a peg**。
同一格里的邻居（别串）：⛔ 不说 a place to step（能懂，但要绕一个从句）。
判据一句话：说的是"能踩脚的那个位置"这个概念 ⇒ foothold；说的是"钉上去的那根小木桩"这个实物 ⇒ peg。

**怎么发现的**
2026-09-09 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个词也是查字典的"。
判重结论 全档 grep `foothold\|peg` 零命中 ⇒ 保留（⛔ 建号当天不测）
2026-09-10 ✅ 复习 · 在池第 2 组首测 · `foothold / peg` —— 两个名词都一字不差。

**我错在哪**
她的：当场查字典才写出来（2026-09-09 自标；⛔ 不是产出错）　　正确：`a foothold` ／ `a peg`
找法：想说"能踩脚的地方"时⛔别去绕 a place to step，先找那个名词 —— foothold；具体那根小木桩就是 peg。

**题面**
"攀岩墙上的落脚点"（凸出来、能把脚踩稳的那一小块） ／ "木栈道栏杆上钉的小木桩"（短短一截、可以挂东西或踩一只脚）

- 2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个词也是查字典的"
  条目内容：脚能踩的那个点 ＝ **a foothold**（通用）；钉在柱子上、只够踩一只脚的小桩 ＝ **a peg**。
  ⛔ 不说 a place to step（能懂，但要绕一个从句）。
- 2026-09-10 ✅ 复习 · 在池第 2 组（首测）· `foothold / peg` —— 两个名词都一字不差
- 2026-09-13 📝 题面整改：第一句补（⛔ 不许用 footing）· 发题前审核（§6.5 第 7 项）
  `footing` 同样 f 开头、同样一个名词、同样合法（get a footing），但它是"站稳的状态"不是"那个点" ⇒ 补排除项
- 2026-09-13 ✅ 学习日 在池第 2 组 · `foodhold. peg.`——foothold（foodhold 是拼写，§2.1 不算）／peg 两个都对 ——**连对 2，毕业**
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组（打包 [2] 里 foothold 当场答对；另一半 peg 请她补答时她说"直接过"）
- 2026-09-29 ❌ 复检第 2 组 · 答成 `footsteps. peg.`（foothold 没调出来，peg 对）—— **回潮**
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉首字母／词数／排除项，括号只留中文释义；换成攀岩墙、木栈道两个新场景
- 2026-09-30 ✅ 付息日 a 段在池第 1 组 [3] · `A foodhold / A peg.`（foodhold 拼写，§2.1 不算）
- 2026-10-01 ✅ 学习日 在池第 1 组 [3] · `foothold. peg.` —— 两个名词都对 ⇒ **连对 2，毕业**

### 328 · 中性尺寸与比较级一律 small（⛔ littler 不存在）
类型 词汇 ｜ 新建 2026-09-09
状态 连对1 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **🎓 已毕业 2026-09-10 · 她指定**（§3.3「她可直接指定」；原话："这个直接毕业吧"。首测 ✅ ＋ 她指定 ⇒ 连对停在 1，⛔ 未凑连对2）

**问题是什么**
中性尺寸与比较级一律 **small**（⛔ **littler** 不存在）。
判据（三格，一起记）：
· **比较级只有 smaller**，⛔ 没有 littler ——「比…小」一律 `smaller than`
· **中性地说尺寸**（a small company／a small room）默认 **small**
· **little** ＝ 尺寸 ＋ 情绪色彩（可爱／微不足道），**只作定语**、⛔ 不作表语（✗ the peg is little）
判据一句话：要**比大小**或**只说尺寸** ⇒ small／smaller；带"就那么一点点"的**语气**且在名词前面 ⇒ little。
★ 她 09-09 写的 `a little peg` **是对的**（定语位 ＋ 带语气）⇒ 本条不是纠她的错，是把边界钉住。

**怎么发现的**
2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· **她自标**："这个 little 我也纠结了很久和 small"
⇒ 走 §2③「她点名要学」建号；她那一句本身没写错。
判重结论：grep `little\|small` 命中 6 处全是别的条目的例句正文（#46 #56 #63 等），
⛔ 无同考点条目 ⇒ 保留新建。

**我错在哪**
她这次没有错（`a little peg` 在定语位、带"就那么一点点"的语气，用法成立），
建号理由是 §2③ **她点名要学**（自标原话："这个 little 我也纠结了很久和 small"）。
找法：要说"小"之前先问一句 —— 我是在**比大小／只报尺寸**吗？
是 ⇒ **small／smaller**（⛔ 没有 littler）；想带"就那么一点点"的语气才用 little，且只能摆在名词前面。

**题面**
"这家公司比那家小。"（"小"用形容词的**比较级**说）

- 2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个 little 我也纠结了很久和 small"
  条目内容：① **比较级只有 smaller**，⛔ 没有 littler；
  ② 中性地说尺寸（a small company／a small room）默认 small；
  ③ little ＝ 尺寸 ＋ 情绪色彩（可爱／微不足道），**只作定语**、⛔ 不作表语（✗ the peg is little）。
  ★ 她这次写的 `a little peg` **是对的**（定语位 ＋ 带"就那么一点点"的语气）⇒ 本条不是纠她的错，是把边界钉住。
- 2026-09-10 ✅ 复习 · 在池第 2 组（首测）· `This company is smaller than that one`
  smaller 用对（⛔ littler 不存在），than that one 的比较对象也对齐了
  ★ 她当场指定毕业（原话："这个直接毕业吧"）⇒ §3.3「她可直接指定」⇒ **🎓·她指定**，连对停在 1
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）

### 329 · terrified ＝ 吓坏了（scared 的顶格版，⛔ 不加 very）
类型 词汇 ｜ 新建 2026-09-09
状态 连对2 连错0 上次2026-09-29 ｜ **🎓 已毕业 2026-09-13** ｜ 题型 整句

**问题是什么**
**terrified ＝ 吓坏了**（scared 的顶格版）：它本身已经是顶格 ⇒ ⛔ 不说 very terrified，
要加程度只能用 **absolutely／completely** terrified。
同一格里的邻居（别串）：scared ＝ 害怕（可加 a bit／very）；
同族顶格词都不加 very —— tired→exhausted · good→brilliant · bad→awful · big→huge。
⇒ 题面直接点名 terrified（她点名要学的词），考的是它前面还加不加 very。
判据一句话：这个形容词本身是不是顶格？是 ⇒ 不加 very，只能加 absolutely／completely。

**怎么发现的**
2026-09-09 新建 · 新题 bank:1091 自由产出（P2）· 她自标"和 scared 的区别，需要学习下"。
★ 她这次用对了（`he was terrified`）⇒ 本条锁的是"顶格词不加 very"这条边界。
判重结论 全档 grep `terrified\|scared` 零命中 ⇒ 保留（⛔ 建号当天不测）
2026-09-10 ✅ 复习 · 在池第 2 组首测 · `he was terrified.` —— 一个词说完，**没加 very**。

**我错在哪**
她的：自标"和 scared 的区别，需要学习下"（2026-09-09；⛔ 不是产出错，她当次用对了）　　正确：`terrified`（⛔ 不加 very）
找法：说"特别害怕"时先挑顶格词 terrified，挑完就**不许**再往前加 very。

**题面**
"草丛里突然窜出一条蛇，我整个人都吓坏了。"（"吓坏了"用 **terrified** 说）

- 2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· 她自标"和 scared 的区别，需要学习下"
  条目内容：scared ＝ 害怕（可加 a bit／very）；**terrified ＝ 吓坏了**，本身已经是顶格 ⇒
  ⛔ 不说 very terrified，要加就用 **absolutely／completely** terrified。
  同族（顶格词都不加 very）：tired→exhausted · good→brilliant · bad→awful · big→huge。
  ★ 她这次用对了（`he was terrified`）⇒ 本条锁的是"顶格词不加 very"这条边界。
- 2026-09-10 📝 题面加提示「**t** 开头」· 在池第 2 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面「"他吓坏了。"（"吓坏"用一个形容词说 · ⛔ 不许用 scared／afraid）」——
  `petrified`／`horrified` 都是一个形容词、都合法、都不在排除项里 ⇒ 题面不唯一可判。
  ⇒ 补首字母提示 `**t** 开头`，把 terrified 框死；⛔ 未泄露"不加 very"这条边界（＝ 考点本身）。
- 2026-09-10 ✅ 复习 · 在池第 2 组（首测）· `he was terrified.` —— 一个词说完，**没加 very**
  ★ 本条锁的那条边界（顶格词不加 very）守住了
- 2026-09-11 📝 付息日 c 段 · 题型回标 词组 ＋ 题面缩块：「他吓坏了。」→「吓坏了」
  考点 terrified 一个形容词就覆盖 ⇒ 词组（§6①）；原题面是带句号的整句 ⇒ 与题型格打架（§6.0 机器闸会报）⇒ 去主语、去句号
- 2026-09-13 ✅ 学习日 在池第 2 组 · `terrified.`——**连对 2，毕业**
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 ✅ 复检第 2 组 · `be terrified.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  她点名要学的词 ⇒ 直接点名 terrified，考的是前面还加不加 very（本条锁的边界）；换成遇到蛇场景

### 330 · set one's mind to sth（下定决心要做的事）
类型 词组 ｜ 新建 2026-09-09
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-18** ｜ 题型 整句

**问题是什么**
**set one's mind to sth** ＝ 铁了心要做成某事（强调持续用力）；
常见形 `do what he set his mind to`（介词 to 留在句尾，后面不再挂东西）。
同一格里的邻居（别串）：make up one's mind（那是"拿定主意"＝ 一次性的选择，做完就结束）；
题面正向点名 mind，set … to 的搭法留给她。
判据一句话：说的是"铁了心一直干下去"⇒ set one's mind to；只是"当场拿定主意"⇒ make up one's mind。

**怎么发现的**
2026-09-09 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个短语也是查字典的"。
判重结论 全档 grep `set his mind\|mind to` 零命中（graduated.md:3810 那条是 many suggestions 的可数性，不同考点）⇒ 保留
2026-09-10 ✅ 复习 · 在池第 2 组首测 · `He did what he set his mind to` —— set his mind to 一字不差，介词 to 留在句尾。

**我错在哪**
她的：当场查字典才写出来（2026-09-09 自标；⛔ 不是产出错）　　正确：`do what he set his mind to`
找法：中文"下定决心要做"先分一刀 —— 是"一直往下干"（set one's mind to），还是"当场拿定主意"（make up one's mind）？

**题面**
"她只要认准了一件事，就一定会干成。"（"认准了"用 **set** 和 **mind** 说）

- 2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个短语也是查字典的"
  条目内容：**set one's mind to sth** ＝ 铁了心要做成某事（强调持续用力）；
  常见形 `do what he set his mind to`（介词 to 留在句尾，后面不再挂东西）。
  ⛔ 不是 make up one's mind（那是"拿定主意"＝ 一次性的选择，做完就结束）。
- 2026-09-10 📝 题面补排除项「／make up」· 在池第 2 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面已排除 decide／determined，但 `the thing he made up his mind to do` **同样用 mind**、
  同样合法 ⇒ 绕开 set one's mind to。条目正文本来就写着「⛔ 不是 make up one's mind」，
  ⇒ 把那条判据搬进题面：排除项补 `／make up`。
- 2026-09-10 ✅ 复习 · 在池第 2 组（首测）· `He did what he set his mind to`
  ★ set his mind to 一字不差，介词 to 留在句尾、后面不再挂东西 —— 与条目正文写的常见形完全一致
- 2026-09-12 📝 题面整改：「做成了他下定决心要做的那件事」→「他下定决心要做的那件事」—— "做成了"（achieved）是考点之外的噪音（§6① 把考点单独摆出来，剩下的全是噪音 ⇒ 缩到块）· 全档题面 review
- 2026-09-13 📝 题面整改：排除项补 `／put` · 发题前审核（§6.5 第 7 项）
  `put his mind to` 同样用 mind、同样合法（专心去做），绕开 set one's mind to ⇒ 补排除项；set … on／to 两个介词都在本条规则内，都判 ✅
- 2026-09-13 ❌ 学习日 在池第 2 组 · `he sets his mind to do that thing`
  最小改 `what he set his mind to`
  ❌ set one's mind **to** 里的 to 是**介词**，后面接名词／-ing 或留在句尾（what he set his mind to），⛔ 不接动词原形 to do；
    题面是名词块"…的那件事"，答成整句也说明 what he set his mind to 这个块形还没长上（09-10 那次 ✅ 正是这个形）
- 2026-09-15 ✅ 学习日 在池第 2 组 · `The thing he set his mind to do.` —— set one's mind to 块出来了；连错1 → 连对1
- 2026-09-18 ✅ 学习日 在池第 1 组 · `the thing he set his mind to`——to 留在块尾 ⇒ **连对 2，毕业**
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉四个排除项，只点名 mind，set … to 与句尾 to 留给她（09-13 掉过）；换成认准了就干成场景
- 2026-10-01 📝 题面补点名「"认准了"用 **set** 和 **mind** 说」· 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  只点 mind 时 make up her mind／put her mind to 同样合法，绕开 set one's mind to ⇒ 点名 set；
  to 和它后面挂什么（09-13 掉的是 to do）仍留给她
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [7] · `Once she sets her mind on something, she always makes it happen.` —— set one's mind on／to 同属本条（09-13 已定），后面挂名词，没落成 to do

### 331 · look straight ahead（往正前方看）≠ look forward to（期待）
类型 词组 ｜ 新建 2026-09-09
状态 连对2 连错0 上次2026-10-01 ｜ **回潮 2026-09-29**（09-13 毕业 → 09-29 复检答成 look forward ahead，撤销毕业、连对清零）｜ **🎓 已毕业 2026-10-01**（连对2 ＝ 09-30 ＋ 10-01；09-29 回潮后第二次毕业）｜ 题型 词组

**问题是什么**
眼睛往正前方看 ＝ **look straight ahead**；
look forward **to** sth ＝ 期待（永远带 to ＋ 名词/-ing，⛔ 与"视线方向"无关）。
同一格里的邻居（别串）：⛔ forward 在"往前看"这个意思上不能替 ahead。
判据一句话：说的是**视线方向** ⇒ ahead；说的是**心里盼着** ⇒ look forward to。
★ 与 graduated.md:1455 那条的分工：那条考的是"不定式后面挂介词"（something to look forward **to**）＝ 结构考点；
　本条考的是**选词**（ahead vs forward）⇒ 目标形式不同，题面互斥（本条题面只讲视线方向，释义里点明不是"盼着"）。

**怎么发现的**
2026-09-09 新建 · 新题 bank:1091 自由产出（P2）· 她自标"本来想写 look forward"。
★ 她这次最终写对了（look straight ahead），但第一冲动是 look forward ⇒ 建号锁住。
判重结论 grep `look forward` 命中 graduated.md:1455 —— 那条考的是"不定式后面挂介词"
（something to look forward **to**）＝ 结构考点；本条考的是**选词**（ahead vs forward）
⇒ 目标形式不同 ⇒ 两条并存，题面互斥（本条题面已排除 forward）⇒ 保留
2026-09-10 ✅ 复习 · 在池第 2 组首测 · `look straight ahead` —— 三个词一字不差。

**我错在哪**
她的：第一冲动是 `look forward`（2026-09-09 自述，最终写对了 look straight ahead）　　正确：`look straight ahead`
找法：要说"往前看"先问一句 —— 是眼睛的方向吗？是就用 ahead，⛔ 别让 look forward 抢跑。

**题面**
"骑车时眼睛直视前方"（视线朝正前面，不是"盼着"的那个"往前看"）

- 2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· 她自标"本来想写 look forward"
  条目内容：眼睛往正前方看 ＝ **look straight ahead**；
  look forward **to** sth ＝ 期待（永远带 to ＋ 名词/-ing，⛔ 与"视线方向"无关）。
  ⛔ forward 在"往前看"这个意思上不能替 ahead。
  ★ 她这次最终写对了（look straight ahead），但第一冲动是 look forward ⇒ 建号锁住。
- 2026-09-10 ✅ 复习 · 在池第 2 组（首测）· `look straight ahead` —— 三个词一字不差
  ★ 09-09 她自述原始冲动是 look forward（＝ 期待），这次没再冒出来
- 2026-09-13 ✅ 学习日 在池第 2 组 · `look straight ahead.`——**连对 2，毕业**
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 ❌ 复检第 2 组 · 答成 `look forward ahead.`（题面 ⛔ forward）—— **回潮**
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉词数与「⛔ forward」，括号改写中文释义（视线方向，不是"盼着"）；换成骑车场景
- 2026-09-30 ✅ 付息日 a 段在池第 1 组 [4] · `For the ID photo, look straight ahead.`
- 2026-10-01 ✅ 学习日 在池第 1 组 [4] · `look straight ahead.` —— ahead 到位，forward 没抢跑 ⇒ **连对 2，毕业**

### 332 · 名词化的"提议/请求"拆回【动词 ＋ when 从句】
类型 结构 ｜ 新建 2026-09-09
状态 连对2 连错0 上次2026-09-29 ｜ **🎓 已毕业 2026-09-13** ｜ 题型 整句

**问题是什么**
中文的"他拒绝了我**回去的提议**"里，"提议"是个名词块；英语默认把它**拆开**：
主句只说他拒绝干什么（`he refused to turn back`），"我提议"降级成一个 **when 从句**（`when I suggested it`）。
同族：他答应了我的请求 → `he agreed to come when I asked him`
　　　我接受了他的邀请 → `I went when he invited me`
同一格里的邻居（别串）：⛔ 不是 my proposal／my suggestion 这种名词块顶在宾语位。
判据一句话：中文宾语位上蹲着一个"提议／请求／邀请"的名词块 ⇒ 把它拆成【动词 ＋ when 从句】。

**怎么发现的**
2026-09-09 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这句话很简单，但是我憋了很久，
第一想法是 He refused my proposal to go back，我好像很难想到这种 when I suggested it"。
★ 她这次**写对了**（全篇最好的一句）⇒ 建号是为了把这条路固定下来，不是纠错。
判重结论 grep `suggest` 命中 2 处（graduated.md:2156 时间轴例句 · 3810 many suggestions 的可数性）
⇒ 都不是本考点 ⇒ 保留
2026-09-10 ✅ 复习 · 在池第 2 组首测 · `he refused to turn back when I suggested it.`

**我错在哪**
她的：第一想法是 `He refused my proposal to go back`（2026-09-09 自述，最终憋出了对的那句）
正确：`he refused to turn back when I suggested it.`
找法：中文里"提议／请求／邀请"蹲在宾语位上时，先把它还原成一个动词，挂进 when 从句里去。

**题面**
"我请他来帮忙搬家，他一口就答应了。"（"我请他"用 **when** 从句说）

- 2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这句话很简单，但是我憋了很久，
  第一想法是 He refused my proposal to go back，我好像很难想到这种 when I suggested it"
  条目内容：中文的"他拒绝了我**回去的提议**"里，"提议"是个名词块；英语默认把它**拆开**：
  主句只说他拒绝干什么（`he refused to turn back`），"我提议"降级成一个 **when 从句**（`when I suggested it`）。
  同族：他答应了我的请求 → `he agreed to come when I asked him`
        我接受了他的邀请 → `I went when he invited me`
  ⛔ 不是 my proposal／my suggestion 这种名词块顶在宾语位。
  ★ 她这次**写对了**（全篇最好的一句）⇒ 建号是为了把这条路固定下来，不是纠错。
- 2026-09-10 ✅ 复习 · 在池第 2 组（首测）· `he refused to turn back when I suggested it.`
  ★ 名词化的"提议"拆回了【动词 suggested ＋ when 从句】，⛔ 没出现 proposal／suggestion。
    这正是她 09-09 憋了很久才憋出来的那一句（原话："我好像很难想到这种 when I suggest it"）⇒ 现在能主动调出来
- 2026-09-13 ✅ 学习日 在池第 3 组 · `he refused to turn back when I suggested it.`——"提议"拆成动词 suggested ＋ when 从句，没用 proposal／suggestion ⇒ **连对 2，毕业**
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-28 📝 学习日 新题 bank:915（P2）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）· `he refused to turn back when I suggested it`
- 2026-09-29 ✅ 复检第 2 组 · `he refused to turn back when I suggested it.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 去负向排除）
  去掉"⛔ proposal／suggestion"，只留正向"用 when 从句说"；换成请人帮忙搬家场景

### 333 · 间接引语里人称一路跟到底（I told him to … **his**）
类型 结构 ｜ 新建 2026-09-09
状态 连对2 连错0 上次2026-09-29 ｜ **🎓 已毕业 2026-09-13** ｜ 题型 整句

**问题是什么**
**间接引语里人称一路跟到底**：`I told him to A, B, C…` 底下并列多少个动作，人称就得跟到底 ——
执行者是他 ⇒ 所有格一律 **his**、宾格一律 **him**。
同一格里的邻居（别串）：⛔ 中途跳回 your／you ＝ 从间接引语滑回直接引语（脑子里已经在对他说话了）。
判据一句话：这一串还挂在 `I told him to …` 底下吗？在 ⇒ 每一个 you／your 都得是 him／his。
★ ⛔ 不判形态类：这不是"漏了个词尾"，是**两种引语混用**（结构层），要靠改写整串才对 ⇒ 照常召回。
★ 与 #92（否定别丢）／#150（限定词与数一致）都不同层。

**怎么发现的**
2026-09-09 新建 · 新题 bank:1091 自由产出（P2）· 触发原话
`I told him to look straight ahead, put one foot first onto the next peg, hug the log, bring **your** other foot over`。
判重结论 全档 grep `间接引语\|转述\|told him to` 零命中；与 #92（否定别丢）#150（限定词与数一致）
都不同层 ⇒ 保留
2026-09-10 ✅ 复习 · 在池第 2 组首测 · `I told him to hug the log and bring his other foot over`。

**我错在哪**
她的：`I told him to …, bring **your** other foot over`　　正确：`… bring **his** other foot over`
找法：写完 `I told him to …`，回头把这一串里每一个 you／your 换成 him／his。

**题面**
"我叫他抱住柱子，把另一只脚挪过来。"（用 **told him to** 起头，一句说完）

- 2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· 触发原话
  `I told him to look straight ahead, put one foot first onto the next peg, hug the log, bring **your** other foot over`
  条目内容：`I told him to A, B, C…` 底下并列多少个动作，人称就得跟到底 ——
  执行者是他 ⇒ 所有格一律 **his**、宾格一律 **him**。
  ⛔ 中途跳回 your／you ＝ 从间接引语滑回直接引语（脑子里已经在对他说话了）。
  ★ 检查触发：写完 `I told him to …`，回头把这一串里每一个 you／your 换成 him／his。
  ★ ⛔ 不判形态类：这不是"漏了个词尾"，是**两种引语混用**（结构层），要靠改写整串才对 ⇒ 照常召回。
- 2026-09-10 ✅ 复习 · 在池第 2 组（首测）· `I told him to hug the log and bring his other foot over`
  ★ **his** other foot —— 间接引语里人称一路跟到底；09-09 掉的正是这里（写成了 your）
  ★ log ⛔ 不判错：题面的"柱子"就是从她 09-09 原文的 `hanging vertical logs` 来的，
    09-09 的最小改与更好版也都保留了 `hug the log`
- 2026-09-13 ✅ 学习日 在池第 3 组 · `I told him to hug the log and pull his other foot over.`——told him to 底下 **his** 跟到底（log 是她 09-09 原话里的那根，照用）⇒ **连对 2，毕业**
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 ✅ 复检第 2 组 · `I told him to hug the log, and pull his other foot over.`

### 334 · the cause OF sth（⛔ cause for）
类型 搭配 ｜ 新建 2026-09-10
状态 连对3 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ 题型 整句

**问题是什么**
**the cause OF sth** ＝ 某事的**起因**（the main cause **of** air pollution ／ the cause **of** the fire）。
`cause for` 是另一个意思 ＝ "…的**理由**"，只配情绪／反应类名词：cause for concern／cause for alarm／cause for celebration。
⇒ 说"某个现象的原因"永远是 **of**。
⚠️ 同族**反向**：reason 配 **for**（the reason **for** the delay）—— cause 与 reason 的介词是反的，
这是最容易互相串的一格；题面正向点名 cause。
判据一句话：后面挂的是"一个现象"⇒ cause **of**；挂的是"担心／庆祝"这类情绪 ⇒ cause **for**。

**怎么发现的**
2026-09-10 新建 · 新题 bank:956 自由产出（P3）· 触发原话
`But generally speaking, they'not the main **cause for** air pollution.`
判重结论 全档 grep `cause of|cause for|the cause` ⇒ 只命中 graduated.md:2359（#173 备注里的
`Because of those two hours…`，考点是评价句的 be 动词槽，与本条无关）⇒ 保留（⛔ 建号当天不测）
2026-09-11 ✅ 付息日 a 段第 1 组首测 · `the main cause of air pollution.` —— cause 配 OF。

**我错在哪**
她的：`they'not the main **cause for** air pollution.`　　正确：`the main cause **of** air pollution`
找法：写完 cause 先问一句 —— 后面跟的是"一个现象"还是"一种情绪"？现象 ⇒ of。

**题面**
"警方还在调查这场火灾的起因。"（"起因"用 **cause** 说）

- 2026-09-10 📝 新建 · 新题 bank:956 自由产出（P3）· 触发原话
  `But generally speaking, they'not the main **cause for** air pollution.`
  条目内容：**cause OF sth** ＝ 某事的**起因** —— the main cause **of** air pollution／the cause **of** the fire。
  `cause for` 是另一个意思 ＝ "…的**理由**"，只配情绪／反应类名词：cause for concern／cause for alarm／
  cause for celebration。⇒ 说"某个现象的原因"永远是 **of**。
  ⚠️ 同族**反向**：reason 配 **for**（the reason **for** the delay）—— cause 与 reason 的介词是反的，
  这是最容易互相串的一格。
- 2026-09-11 ✅ 付息日 a 段 · 第 1 组 · `the main cause of air pollution.` —— cause 配 OF（首测）⇒ 连对1
- 2026-09-15 ✅ 学习日 在池第 2 组 · `The primary cause of air pollution.` —— the cause OF → **连对2，毕业**
  ｜同句 primary ⇒ 🎓#206 书面登记一行 📝
- 2026-09-15 ✅ 新题 bank:1059 自发命中 · `failed to find the cause of the problem` —— the cause OF，介词对
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"⛔ reason／source"，只点名 cause，of 留给她（她掉过的是 cause for）；换成火灾起因场景
- 2026-09-30 ✅ 复检 · 付息日 a2 第 4 组 [4] · `The doctor haven't figured out the cause of his headache yet.`

### 335 · take action（action 在这个块里不可数，⛔ take actions）
类型 语法 ｜ 新建 2026-09-11（从 #261 拆出）
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-18** ｜ 题型 整句

**问题是什么**
**take action** 是固定块，action 在这里**不可数** ⇒ ⛔ 不加 -s、⛔ 不加 an。
同一格里的邻居（别串）：同族的 take **steps**／take **measures** 才有复数（steps／measures 本身可数）
⇒ 题面直接用"采取行动"点名 action，-s 挂不挂留给她。
判据一句话：take 后面挂的是 action 吗？是 ⇒ 尾巴上不许有 s。
★ 与 #261 的分工：本条 2026-09-11 从 #261 拆出（§3.2c③ 顽固成员单独摘出），#261 剩六个成员照常走连击；
　拆出来的子条从 0 起算、⛔ 不继承 #261 的连击。

**怎么发现的**
2026-09-11 新建 · 付息日 c 段 · **从 #261 拆出**。拆号依据（一条一条数的）：#261 七个成员里
**只有 action 掉过两次** —— 08-20 首犯 `they are more willing to take actions`；
09-07 复检 `take actions` 又加 -s（题面完好，判定有效）；09-05 那次是题面缩坏判 ◎，⛔ 不算。
判重结论 全档 grep `take action|actions` ⇒ 只命中 #261 本条（拆源）与 #85（take on risk，不同块）⇒ 保留（⛔ 建号当天不测；次日起进池）

**我错在哪**
她的：`they are more willing to take actions`（08-20 首犯 · 记在 #261）／ `take actions`（09-07 复检）
正确：`take action`
找法：写完 take action，回头看 action 尾巴上有没有多出一个 s。

**题面**
"污染这么严重，政府得马上采取行动。"（"采取行动"用 **action** 说）

- 2026-09-11 📝 新建 · 付息日 c 段 · **从 #261 拆出**（§3.2c③：顽固成员单独摘出，老条目剩六个成员照常走连击）
  拆号依据（一条一条数的）：#261 七个成员里 **只有 action 掉过两次** ——
    08-20 首犯 `they are more willing to take actions`；09-07 复检 `take actions` 又加 -s（题面完好，判定有效）；
    09-05 那次是题面缩坏判 ◎，⛔ 不算。其余六个成员从未掉过（09-10 掉的 feedback 是 a 不是 -s，也只一次）。
  ⇒ 拆出来从 0 起算、⛔ 不继承 #261 的连击（§3.1「拆出来的子条从 0 起算」）。
  条目内容：**take action** 是固定块，action 在这里**不可数** ⇒ ⛔ 不加 -s、⛔ 不加 an。
    同族的 take **steps**／take **measures** 才有复数（steps／measures 本身可数）⇒ 题面已排除，免得白测。
    中文"更愿意干"口语更常走 **more willing to give it a go／to go for it**；take action 偏"采取行动"。
  检查触发：写完 take action，回头看 action 尾巴上有没有多出一个 s。
- 2026-09-13 📝 题面整改：排除项补 `／plunge／chance` · 发题前审核（§6.5 第 7 项）
  take the plunge／take a chance 同样 take＋一个名词、同样能翻"更愿意干"，都绕开 take action ⇒ 补排除项
- 2026-09-13 ✅ 学习日 在池第 3 组 · 首测 · `If risk is lower, people are willing to take action.`——take action 无 -s（09-11 从 #261 拆出后第一次单测）
  ｜⚠️ "更愿意"的"更"丢了（more willing）、risk 前该有 the ⇒ 只进 diff-2，不建号
- 2026-09-18 📝 题面整改：提示「take ＋ 一个名词」→「take ＋ 一个 a 开头的名词」· 发题前审核（§6.5 第 7 项）
  take the leap／take the initiative 同样 take ＋ 一个名词、同样能翻"更愿意干"，排除项一个个补不完 ⇒ 改用首字母收敛；考点 action 不加 -s 没给出
- 2026-09-18 ✅ 学习日 在池第 1 组 · `if risks are lower, people are willing to take action.`——take action 无 -s ⇒ **连对 2，毕业**
  ｜同句 willing（更愿意）⇒ ⚪ #7，不归本条
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"take ＋ a 开头的名词"猜谜与四个排除项，直接用"采取行动"点名 action，-s 挂不挂留给她；换成治污场景
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [8] · `With pollution this severe, the government needs to take swift action.` —— take swift action，action 不带 s

### 336 · get TO ＋ 地点（到达；⛔ get the destination）
类型 搭配 ｜ 新建 2026-09-11
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-18** ｜ 题型 整句

**问题是什么**
**get to** ＋ 地点 ＝ 到达（get 后面挂地点必须有 to）：get to the station ／ get to work ／ get to the destination。
同一格里的邻居（别串）：get **home／here／there**（副词，⛔ 不带 to）·
get 直接带宾语是"拿到／得到"（get a ticket／get the message）—— 漏了 to，句子就成了"拿到那个目的地"。
判据一句话：get 后面是**地点名词**吗？是 ⇒ 补 to；是 home／here／there ⇒ 不补。
★ 与 🎓#81（get TO know sb）分工：那条的 to 是不定式标记，本条是介词 ⇒ 两条规则，各走各的；
　题面互斥（#81"认识陌生人"／本条"到目的地"）。
⚠️ 同一句里 `where to live` 是 🎓#86 后半格（where to STAY）掉了 ⇒ 那条回潮，⛔ 不归本条。

**怎么发现的**
2026-09-11 新建 · 付息日 d 段重答 R10（P3 · How does technology help people make plans?）· 触发原话
`like how to get the destination, where to live, and which restaurants are good.`
判重结论 全档 grep `get to\b|get TO|到达` ⇒ 只命中 🎓#81（get **to** know sb）——那条的 to 是不定式标记、本条是介词，
"get 后面那个 to 不能省"表面同、规则不同 ⇒ 两条并存，题面互斥（#81"认识陌生人"／本条"到目的地"）⇒ 保留（⛔ 建号当天不测）

**我错在哪**
她的：`how to get the destination`　　正确：`how to get **to** the destination`
找法：写完 get ＋ 名词，回头问一句 —— 这个名词是地点吗？是就补 to。

**题面**
"请问去火车站怎么走？"（"去"用 **get** 说）

- 2026-09-11 📝 新建 · 付息日 d 段重答 R10（P3 · How does technology help people make plans?）· 触发原话
  `like how to get the destination, where to live, and which restaurants are good.`
  条目内容：**get to ＋ 地点** ＝ 到达（get to the station／get to work／get to the destination）；
    home／there 是副词，⛔ 不带 to（get home／get there）。
    get 直接带宾语是"拿到／得到"（get a ticket／get the message）—— 漏了 to，句子就成了"拿到那个目的地"。
  ⚠️ 同一句里 `where to live` 是 🎓#86 后半格（where to STAY）掉了 ⇒ 那条回潮，⛔ 不归本条。
  检查触发：写完 get ＋ 一个地点名词，回头看中间有没有 to。
- 2026-09-13 ✅ 学习日 在池第 3 组 · 首测 · `how to get to your destination`——get **to** ＋ 地点（09-11 掉的那个 to 回来了）
- 2026-09-18 ✅ 学习日 在池第 1 组 · `how to get to the destination` ⇒ **连对 2，毕业**
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 get，to 留给她（她掉过的是 get the destination）；换成问路去火车站场景
- 2026-10-01 ✅ 复检 · 学习日 复检第 4 组 [1] · `During peak hour, it takes me a full hour to get to work.` —— get to work（get 后面挂地点，to 在）

### 337 · look up sth（查；⛔ look up for）
类型 词组 ｜ 新建 2026-09-13 ｜ 与 🎓#100 互斥（look for）
状态 连对2 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ 题型 整句

**问题是什么**
**look up** ＋ 查的东西 ＝ 查（查地址／查营业时间／查一个词）：look up where to stay ／ look up the opening hours ／ look it up。
⛔ look up 后面**直接接**被查的东西，中间不加 for。
同一格里的邻居（别串）：**look for** sth ＝ 找（🎓#100）· **search for** sth（🎓#312）—— 那两个的 for 是它们自己的小词，
⛔ 不许搬到 look up 后面；`look up for` ＝ 把两个词组焊在一起，哪个都不是。
判据一句话：是"查"还是"找"？查 ⇒ look up，后面直接接东西；找 ⇒ look for。
★ 与 🎓#100 分工：那条考 find（结果）与 look for（过程）的分工，目标形式是 look for；本条她已经选对 look up、
　错在多挂一个 for ⇒ 目标形式不同 ⇒ 两条并存，题面互斥（#100"在找一份工作"／本条"查一下营业时间"）。

**怎么发现的**
2026-09-13 学习日 在池第 1 组 [4]（#86 那题 · "出去玩之前，先查查住哪儿。"）· 触发原话
`Before going on a trip, you need to first look up for where to stay.`（#86 两个成员都对，look up for 不归那条）
判重三步：
　① 目标形式 look up sth ⇒ dedup "look up" ⇒ 命中 🎓#100（look for ≠ look up）、🎓#312（search for）、#86（历史行）
　　　#100：考点是 find／look for 的过程结果分工、目标形式 look for ⇒ 目标形式不同 ⇒ 否，题面互斥
　　　#312：另一个动词 search ⇒ 否　　#86：只是历史行里出现过 look up，那条考 go on a trip／where to stay ⇒ 否
　② 中文题面 "查" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`look up for where to stay`　　正确：`look up where to stay`
找法：写完 look up，回头看后面紧跟的是不是那个被查的东西；夹了个 for 就删掉。

**题面**
"这个词我不认识，得查一下。"（"查"用 **look** 说）

- 2026-09-13 ❌ 首犯 · 学习日 在池第 1 组 [4]（#86 那题）· `you need to first look up for where to stay`
  最小改 `look up where to stay`
  ❌ look up ＝ 查，后面直接接查的东西，⛔ 不带 for；look for ＝ 找。两个词组各带各的小词，不许拼在一起。
  ★ 判重：dedup "look up" ⇒ 🎓#100（look for，目标形式不同）／🎓#312（search for，另一个动词）⇒ 两条并存，题面互斥
- 2026-09-15 ✅ 学习日 在池第 1 组 [4]（#86 题）自发命中 · `look up where to stay` —— look up 直接带宾语从句，没再加 for（09-13 同题写的是 look up for）；连错1 → 连对1
- 2026-09-15 ✅ 学习日 在池第 2 组 · `look up the open time.` —— look up 直接带宾语、没加 for → **连对2，毕业**（今天第 1 组 [4] 自发命中一次 ＋ 本题一次，§3.3 同日多次各算一次）
  ｜同句 the open time ⇒ 新建 #343（opening hours）
- 2026-09-19 📝 c 段 review · 题面整改：「查一下营业时间」→「查一下这个词」
  旧题面把 🎓#343（opening hours）的考点夹带进来：答 look up the open time 时，掉的其实是 #343 ⇒ 换成不带别的考点的宾语；look up the word／look it up／look the word up 都在本条规则内
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"look 起头的两个词"词数提示，只点名 look，up 后面夹不夹 for 留给她；换成查生词场景
- 2026-09-30 ✅ 复检 · 付息日 a2 第 4 组 [3] · `I have to look it up on my phone.`

### 338 · end up ＋ -ing（⛔ end up to do／end up to -ing）
类型 词组 ｜ 新建 2026-09-13 ｜ 与 🎓#113 互斥（那条考"都要"那一层，本条考 end up 后面的形）
状态 连对2 连错0 上次2026-09-30 ｜ **🎓 已毕业 2026-09-15** ｜ 题型 整句

**问题是什么**
**end up ＋ -ing** ＝ 最后落到（做）某事：end up queuing ／ end up doing it myself ／ end up making a mess。
end up 后面**直接接 -ing**（或名词／介词短语：end up in hospital ／ end up with nothing）；⛔ 中间不加 to。
同一格里的邻居（别串）：🎓#113 考的是"都要／总是"那一层要不要显式说出来（always end up ／ have to），
本条只管 end up 后面那个形 —— 层落地了、形写歪了，两条各判各的。
判据一句话：end up 后面是动词吗？是 ⇒ 直接 -ing，中间什么都不夹。

**怎么发现的**
2026-09-13 学习日 复检第 4 组 [8]（#113 那题 · "我每次去都要排半小时队。"）· 触发原话
`I always end up to queuing for half an hour every time I go.`（"都要"那层落地了，#113 ✅；end up to queuing 不归那条）
判重三步：
　① 目标形式 end up -ing ⇒ dedup "end up" ⇒ 命中 🎓#113（层，不是形）、#49（历史行里带过 end up，考人称）⇒ 都否
　② 中文 "最后…" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）；08-20／09-05 她两次写对过 end up queuing ⇒ 是形没长稳，不是没见过

**我错在哪**
她的：`end up to queuing`　　正确：`end up queuing`
找法：写完 end up，看后面紧跟的是不是 -ing；冒出一个 to 就删掉。

**题面**
"本来想点外卖，结果最后还是自己做了饭。"（"结果最后"用 **end up** 说）

- 2026-09-13 ❌ 首犯 · 学习日 复检第 4 组 [8]（#113 那题）· `I always end up to queuing for half an hour every time I go.`
  最小改 `I always end up queuing for half an hour every time I go.`
  ❌ end up 后面直接接 -ing，⛔ 不加 to；"都要"那层（always end up）落地了，归 #113 ✅
  ★ 判重：dedup "end up" ⇒ 🎓#113（层不是形）／#49（历史行带过）⇒ 两条并存
- 2026-09-15 ✅ 学习日 在池第 2 组 · `I ended up doing it myself.` —— end up ＋ -ing；连错1 → 连对1
- 2026-09-15 ✅ 新题 bank:1059（P2 · cold）自发命中 · `We ended up being classmate for years right until we finished high school.`
  end up ＋ -ing 一字不差（今日第二次 ✅，§3.3 同日多次各记一行各算一次）→ **连对2，毕业**
- 2026-09-20 ⚡ 自评免测 · 复检第 2 组（她答"都直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 end up，后面接 -ing 还是 to 留给她（她掉过的是 end up to queuing）；换成点外卖场景
- 2026-09-30 ✅ 复检 · 付息日 a2 第 4 组 [2] · `we ended up staying at home watching TV all day.`

### 339 · reach sb（联系上；直接带宾语，⛔ get reach sb）
类型 词组 ｜ 新建 2026-09-13 ｜ 与 🎓#130 互斥（那条考 can／be able to，本条考 reach 的形）
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-18** ｜ 题型 整句

**问题是什么**
**reach sb** ＝ 联系上某人（电话／消息打得通）：I couldn't reach him ／ You can reach me at this number。
reach **直接带宾语**，⛔ 前面不套 get。
同一格里的邻居（别串）：get hold of sb ／ get in touch with sb ／ get through to sb —— 这三条才带 get，
`get reach him` ＝ 把 get hold of 的 get 和 reach 焊在一起，哪个都不是。
判据一句话：用 reach 就不要 get；要用 get 就换成 get hold of／get in touch with。

**怎么发现的**
2026-09-13 学习日 复检第 4 组 [9]（#130 那题 · "我一直没能联系上他。"）· 触发原话
`I'v not been able to get reach hime.`（haven't been able to 那一格对，#130 ✅；get reach 不归那条；hime 是拼写）
判重三步：
　① 目标形式 reach sb ⇒ dedup "reach" ⇒ 命中 🎓#267（get sth in front of sb，正文提到 reach 是另一义）、🎓#323（嵌入疑问）⇒ 都否
　　　dedup "get in touch" ⇒ 零命中
　② 中文 "联系上" ⇒ 只在 #130 题面里（那条考 be able to）⇒ 否，题面互斥
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`get reach him`　　正确：`reach him`（或 `get hold of him`）
找法：写完 reach，回头看前面有没有多出一个 get；有就二选一 —— 删 get，或把 reach 换成 hold of。

**题面**
"我打了一下午电话，都没联系上他。"（"联系上"用 **reach** 说）

- 2026-09-13 ❌ 首犯 · 学习日 复检第 4 组 [9]（#130 那题）· `I'v not been able to get reach hime.`
  最小改 `I haven't been able to reach him.`
  ❌ reach 直接带宾语，⛔ 前面不套 get；带 get 的是 get hold of／get in touch with／get through to
  ★ 判重：dedup "reach"／"get in touch" ⇒ 无同考点条目；#130 题面同句但考 be able to ⇒ 互斥并存
- 2026-09-15 ✅ 学习日 在池第 2 组 · `We couldn't reach him during the day.` —— reach 直接带宾语；连错1 → 连对1
- 2026-09-18 ✅ 学习日 在池第 1 组 · `we can't reach her by phone during the day.`——reach her 不套 get ⇒ **连对 2，毕业**
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 reach，前面套不套 get 留给她；换成打一下午电话场景
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [10] · `If anything comes up, you can reach me at this number.` —— reach me 直接带宾语，没套 get
  ｜at this number 她自注「需要学一下，本来想写 through」⇒ 新建 #381（号码前的介词，与本条规则不同）

### 340 · a step up from that（递进到更高一档；⛔ on top of that 是平级追加）
类型 词组 ｜ 新建 2026-09-13 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **🎓 已毕业 2026-09-21**

**问题是什么**
**a step up from that** ／ **going a step further** ＝ "再往上一档"：前一条是底线，这一条比它更高。
同一格里的邻居（别串）：**on top of that ／ plus ／ also** ＝ 平级追加（再加一条，不分高低）——
她自己点出这两个"体现不出来"，对：它们没有"高一档"那层。
⛔ `stepping it up a bit, things like …` 悬空：分词没有逻辑主语（谁在 step up？句子主语是 things）。
判据一句话：新一条比前一条**更高一档**吗？是 ⇒ a step up from that；只是再加一条 ⇒ on top of that。
★ 与 🎓#262（口语转折工具箱 Then again／That said）分工：那条是话锋一转，本条是往上一档；
　与 🎓#283（It's really about A first, and then B）分工：那条排先后收尾，本条升档。

**怎么发现的**
2026-09-13 学习日 新题 bank:238（P3 · What kinds of behavior are considered as good behavior?）· 触发原话
`But stepping it up a bit, things like showing up on time and meeting your deadlines … are totally worth praise.`
她自标："这句要学下，on top of that 或者 plus 体现不出来"（§2③ 她主动提出的）。
判重三步：
　① 目标形式 a step up from that ⇒ dedup "step" ⇒ 🎓#281 step back（另一个块）· 🎓#327 foothold（无关）· #49（历史行）⇒ 都否
　　　🎓#262 转折工具箱 ＝ 转折不是递进 ⇒ 否；🎓#283 A first, and then B ＝ 排先后不是升档 ⇒ 否
　② 中文 "台阶" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`But stepping it up a bit, things like … are …`　　正确：`A step up from that, things like … deserve …`（或 `Going a step further, …`）
找法：写"更进一步"之前先问 —— 是升档还是平级加一条？升档 ⇒ a step up from that；⛔ 别让分词悬着。

**题面**
"准时上班是最基本的；再往上一档，是主动帮同事分担活儿。"（"再往上一档"用 **a step up** 说）

- 2026-09-13 新建 · 新题 bank:238（P3）· 她点名要学 · `But stepping it up a bit, things like showing up on time …`
- 2026-09-15 ✅ 学习日 在池第 2 组 · `a step up from that.` —— 首测一字不差；连对1
- 2026-09-19 📝 题面整改：补「step 当名词用」· 发题前审核（§6.5 第 7 项）
  `step it up` 同样用 step、单看"再往上一档"也说得通（加把劲），但它是动词用法，正是 09-13 触发句 stepping it up 那条路 ⇒ 限定成名词，逼出 a step up／a step further
- 2026-09-19 ❌ 付息日 a 段在池第 1 组 · `a step up for that`
  最小改 `a step up from that`
  ❌ 块内固定的介词是 from（比"那个"再高一档 ＝ 从那一档往上）；for 不在这个块里。a step up 本身对
- 2026-09-20 📝 题面整改：排除项补 `／above` · 发题前审核（§6.5 第 7 项）
  `a step above that` 同样用 step 当名词、也是"高一档"，单看题面完全合法 ⇒ 她答它得判 ✅，而块内那个 from（09-19 掉的正是它）就白测一次 ⇒ 排掉 above，把答案收敛到 a step up from that／going a step further
- 2026-09-20 ✅ 学习日 在池第 1 组 · `a step up from that.` —— 块内固定介词 from（09-19 掉的正是它，写成 for）；本场发题前已把 above 排除
- 2026-09-21 ✅ 学习日 在池第 1 组 [2] · `a step up from that.` —— 逐字命中目标块，step 当名词，没走 on top of／plus／above。连对 1 → 2 ⇒ 🎓
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"step 当名词／⛔ on top of／plus／above"，她点名要学的块 ⇒ 直接点名 a step up，from that 怎么接留给她（09-19 掉过）；换成职场表现场景

### 341 · deserve praise／credit（⛔ worth praise）
类型 搭配 ｜ 新建 2026-09-13
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-18** ｜ 题型 整句

**问题是什么**
"值得表扬／值得认可" ＝ **deserve praise／credit**（或 be worthy of praise ／ be praiseworthy）。
⛔ **worth ＋ praise 不搭**：worth 后面挂的是"值那个价"的东西 —— worth the money ／ worth a try ／ worth the effort ／
worth -ing（worth praising 可以）。
同一格里的邻居（别串）：deserve 管"该得到的"（praise／credit／respect／attention／a break）；worth 管"值不值那个价／那个功夫"。
判据一句话：后面那个名词是"该得到的"吗？是 ⇒ deserve；是"价／功夫"吗 ⇒ worth。

**怎么发现的**
2026-09-13 学习日 新题 bank:238（P3 · What kinds of behavior are considered as good behavior?）· 触发原话
`things like showing up on time and meeting your deadlines … are totally worth praise.`
判重三步：
　① 目标形式 deserve praise ⇒ dedup "deserve"／"praise" ⇒ 零命中；dedup "worth" ⇒ 🎓#173／#264／#275／#14／#262 全是正文里带 worth 字样的别的考点 ⇒ 都否
　② 中文 "值得" ⇒ 🎓#26／#262／#264／#306／#58 均无关 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`are totally worth praise`　　正确：`totally deserve praise` ／ `deserve real credit`
找法：写完 worth，看后面：是 praise／credit／respect 这种"该得到的" ⇒ 换成 deserve。

**题面**
"那个捡到钱包又送回来的小伙子，真值得表扬。"
　　★ 零提示：deserves praise／is worth praising／should be praised 都算对；她掉过的是 worth praise

- 2026-09-13 ❌ 首犯 · 新题 bank:238（P3）· `are totally worth praise`
  最小改 `totally deserve praise`
  ❌ worth 后面挂"值那个价"的东西（worth the money／worth a try／worth praising）；"值得表扬"这种"该得到的"用 deserve
- 2026-09-15 ✅ 学习日 在池第 2 组 · `This approach deserves praise.` —— deserve praise；连错1 → 连对1
- 2026-09-18 📝 题面整改：补（"值得"用一个动词说）· 发题前审核（§6.5 第 7 项）
  `This approach is praiseworthy／commendable.` 合法，但绕开 deserve ⇒ 限定成动词；merit praise 同在规则内，判 ✅
- 2026-09-18 ✅ 学习日 在池第 1 组 · `deserve praise.` ⇒ **连对 2，毕业**
- 2026-09-21 ⚡ 自评免测 · 复检第 2 组（她看完整组回「直接过」）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）· 题型 词组 → 整句
  去掉"一个动词／⛔ worth／should"，改零提示整句（deserve／worth praising／be praised 都算对），逼的是她掉过的 worth praise
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [9] · `That young guy who found the wallet and brought it back really deserves a lot of credit.` —— deserves credit，没落成 worth praise

### 343 · **opening hours**／business hours（营业时间；⛔ open time）
类型 词组 ｜ 新建 2026-09-15
状态 连对0 连错1 上次2026-10-02 未毕业 ｜ **回潮 2026-10-02**（09-19 毕业 → 10-02 复检写成 `The museum's operating time.`，"开放时间"又落在 time 上，撤销毕业、连对清零）｜ 题型 词组

**问题是什么**
"营业时间"是一个固定块：**opening hours**（英式也说 opening times）／ **business hours**；⛔ open time 不是一个块（open 是形容词，time 单数也不对）。
同一格里的邻居（别串）：working hours（工作时间，说人）· office hours（办公时间／答疑时间）· be open（"开着门"：Are they open on Sundays?）。
判据一句话：说"几点开几点关"这件事 ⇒ 用 **hours**（复数）挂在 opening／business 后面；说"开没开门"才用 open。

**怎么发现的**
2026-09-15 学习日 在池第 2 组 [4]（#337 题面"查一下营业时间"）：她写 `look up the open time`。
查重（§3.1 判重三步）：
　① 目标形式 dedup "opening" ⇒ 只命中 #337（look up sth，考"查"不考"营业时间"，题面里带这个词而已）⇒ 否；dedup "business hours"／"open time" ⇒ 零命中
　② 中文 "营业" ⇒ 同样只命中 #337 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）
★ 编号跳过 342：本场教练建过 #342（gotta）又当场撤销，号作废不复用。

**我错在哪**
她的：`the open time`　　正确：`the opening hours`（／ business hours）
找法：写完"营业时间"回头看 —— 是不是 hours 结尾？不是就换成 opening hours。

**题面**
"这家超市的营业时间"（几点开门、几点关门）

- 2026-09-15 ❌ 首犯 · 学习日 在池第 2 组 [4]（#337 题）· `look up the open time`
  最小改 `look up the opening hours`
  ❌ "营业时间"是固定块 opening hours／business hours；open time 不是一个块
- 2026-09-18 ✅ 学习日 在池第 1 组 · `opening hours`（09-15 首犯后首测）
- 2026-09-19 ✅ 付息日 a 段在池第 1 组 · `opening hours` ⇒ **连对 2，毕业**
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉词数与"⛔ time"，改成中文释义（几点开门几点关门）；换成超市场景
- 2026-10-02 ❌ 复检 · 学习日 复检第 4 组 [6] · `The museum's operating time.` —— "开放时间"落在 time 上（与掉过的 open time 同一处）⇒ **回潮**
  最小改 `The museum's operating hours.`　更好版 `The museum's opening hours.`
  ❌ 营业／开放时间是几点到几点这一段 ⇒ hours（opening／business／operating hours），⛔ time

### 344 · drive over／come over（到我这边来；⛔ drive here）
类型 词组 ｜ 新建 2026-09-15 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-09-26 ｜ 题型 整句 ｜ **🎓 已毕业 2026-09-20**

**问题是什么**
"到我这边来"这一层，挂在动词后面的小词是 **over**：drive over ／ come over ／ head over ／ pop over。
over 自己就带着"从他那边挪到我这边"，句子里 ⛔ 不用再说 here。
同一格里的邻居（别串）：**drive here** ＝ 强调"开到我此刻站的这个点"，讲故事时不自然 ·
**go over** ＝ 到他那边去（方向相反）· **come by／drop by** ＝ 顺路来一下（重点在"顺路"）·
**head over** ＝ 动身过去（重点在出发）。
判据一句话：说"来我这儿"⇒ 动词 ＋ **over**；⛔ 不用 here。

**怎么发现的**
2026-09-15 新题 bank:1059（P2 · cold）：她写 `He drove here and started debugging`。
教练在 diff-2 给了 drove over，她点名要学（原话："drove over 和 on his own laptop 可以建，这两个我觉得更地道"）。
查重（§3.1 判重三步）：
　① 目标形式 dedup "drive over"／"come over" ⇒ 零命中；dedup "over" ⇒ 🎓#216（all over the floor）·🎓#186（leave a mess）·🎓#14（well away）等全是别的块 ⇒ 都否
　② 中文 "开过来" ⇒ 零命中；"过来" ⇒ 最近的是 🎓#145（bring／take／fetch）—— 那条分的是**东西**往哪个方向带，本条是**人**往我这边来 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`He drove here`　　正确：`He drove **over**`
找法：写完"来我这儿"这层意思，看句子里有没有 here —— 有就换成 over。

**题面**
"你周末有空就过来坐坐吧。"（"过来"用 **over** 说）

- 2026-09-15 新建 · 新题 bank:1059（P2 · cold）· 触发原话 `He drove here and started debugging using his own device` · ⭐ 她点名要学
- 2026-09-18 📝 题面整改：排除项补 `／up／round` · 发题前审核（§6.5 第 7 项）
  `he drove up`（开到跟前停下）／`he drove round`（英式 ＝ came over）都是"动词 ＋ 一个小词"、都合法，绕开 over ⇒ 补排除项
- 2026-09-18 ✅ 学习日 在池第 2 组 · 首测 · `he drove over.`——drive **over**，没带 here
- 2026-09-20 ✅ 学习日 在池第 1 组 · `he drove over.` —— "过来"＝ 动词后面挂 over；连对2 ⇒ 毕业
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [2] 打包 · `he drove over`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"一个小词挂动词后面 ＋ 四个排除项"猜谜写法，她点名要学的块 ⇒ 直接点名 over，动词挑哪个留给她；换成邀请周末过来场景

### 345 · 在哪台机器上干活 ＝ ON ＋ 机器（on his own laptop／device；⛔ using his device）
类型 搭配 ｜ 新建 2026-09-15 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-09-26 ｜ 题型 整句 ｜ **🎓 已毕业 2026-09-20**

**问题是什么**
在某台机器上做事，介词用 **on** ＋ 那台机器：on his own laptop ／ on his own device ／ on my phone ／ on the office computer。
⛔ 不用 using 起头把机器当工具挂上去（using his own device）—— 口语说"在哪台上干"，走 on。
同一格里的邻居（别串）：软件、平台也走 **on**（on Zoom ／ on Excel）· **in** 用在"在某个系统／应用里面"（in the app）·
**with** 用在手持工具（with a screwdriver）。
判据一句话：机器或平台 ⇒ **on** ＋ 机器；⛔ 不用 using 起头。

**怎么发现的**
2026-09-15 新题 bank:1059（P2 · cold）：她写 `started debugging using his own device`。
教练在 diff-2 给了 on his own laptop，她点名要学（原话同 #344）。
查重（§3.1 判重三步）：
　① 目标形式 dedup "laptop"／"device"／"on my phone" ⇒ laptop 只命中 🎓#74（make do with）与 🎓#302（something breaks），两条都是正文里带 laptop 的例句 ⇒ 否；另两个零命中
　② 中文 "用…电脑" 无对应条目 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`using his own device`　　正确：`**on** his own device`
找法：说"用某台机器干活"之前，先把 using 换成 on —— 机器是干活的地方，不是工具。

**题面**
"我一般在自己的平板上看电子书。"
　　★ 零提示：中文"在…上"自然落 on；她要学的就是 on my tablet 这条（⛔ using my tablet 是她原来的路）

- 2026-09-15 新建 · 新题 bank:1059（P2 · cold）· 触发原话 `started debugging using his own device` · ⭐ 她点名要学
- 2026-09-18 📝 题面整改：排除项补 `／from` · 发题前审核（§6.5 第 7 项）
  `debugged it from his own laptop`（远程）同样一个介词、合法，绕开 on ⇒ 补排除项
- 2026-09-18 ✅ 学习日 在池第 2 组 · 首测 · `he debugged on his own device` ⚠️ **本条已于 2026-09-18 改判为 ✅**
  最小改 `he debugged it on his own laptop`
  ❌ 介词 on 对了；"那台笔记本"又说成统称 device（题面已排除，09-15 触发句掉的也是这一半）⇒ 具体是哪台就说哪台
  ★ 她当场异议："computer 就是 device" ⇒ device 是合法说法，本条考点只有介词 on，她答对了 ⇒ 改判 ✅
- 2026-09-18 📝 规则收回：「⛔ device 这种统称」半条删掉 · 她异议（"computer 就是 device"）
  device 是合法说法，不是错；本条考点只剩介词 on（⛔ using 起头）⇒ 标题／问题是什么／我错在哪同步改，题面排除项去掉 device
- 2026-09-20 ✅ 学习日 在池第 1 组 · `he debugs on his own laptop.` —— 在哪台机器上干活 ＝ on ＋ 机器；连对2 ⇒ 毕业
- 2026-09-26 ✅ 复检 · 付息日 a2 第 2 组 [2] 打包 · `he debugged on his own laptop`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）· 题型 词组 → 整句
  去掉"用一个介词 ＋ 三个排除项"，改零提示整句：中文"在…上"自然落 on；换成平板看电子书场景

### 346 · "…所在" ＝ where X **lies**／is（where 后面那句要有动词）
类型 词组 ｜ 新建 2026-09-19
状态 连对2 连错0 上次2026-09-27 ｜ 题型 整句 ｜ **🎓 已毕业 2026-09-21**

**问题是什么**
中文"…的魅力所在／问题所在／关键所在"，英语落成 **where X lies**（或 where X is／where X comes from）：
that's exactly where the magic of reading lies ／ that's where the problem lies ／ that's where the fun is。
where 引出的是一个句子，**X 后面必须有动词**；"所在"这个"在"就是那个动词。
同一格里的邻居（别串）：🎓#3 That's where … 管的是"就是在这儿"这个块本身（她三次都对）；
本条管 where 后面那句不能只剩一个名词 · 也可以整个不用 where：that's the magic of reading。
判据一句话：说完 where ＋ 一个名词，后面有没有动词？没有 ⇒ 补 lies／is。

**怎么发现的**
2026-09-19 付息日 d 段重答 R13（P3 · What are the differences between reading a book and visiting a museum?）· 触发原话
`there are a thousand Hamlets in a thousand people's eyes, and that's exactly where the magic of reading books.`
判重三步：
　① 目标形式 where X lies ⇒ dedup "lies"／"lie in"／"所在"／"魅力" ⇒ 零命中；"在于" ⇒ 🎓#276（for ages，正文里带"在于"字样）⇒ 否
　② "that's where" ⇒ 🎓#3（That's where 这个块本身，她 08-16／08-19／09-09 三次都对，这次块也用对了）⇒ 本条管 where 后面缺动词，与 #3 互补、两条并存
　　 🎓#275（whether 后面要跟主谓）同是"从句要有谓语"，但那条只管 whether ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`that's exactly where the magic of reading books`　　正确：`that's exactly where the magic of reading lies`
找法：说完 where ＋ 一个名词，回头看后面有没有动词；中文是"所在"就补 lies。

**题面**
"我觉得这就是旅行的意义所在。"
　　★ 零提示：where the meaning of travel lies／is 与 what travel is all about 都算对；她掉过的是 where ＋ 名词后面没动词

- 2026-09-19 ❌ 首犯 · 付息日 d 段重答 R13（P3）· `that's exactly where the magic of reading books.`
  最小改 `that's exactly where the magic of reading books lies.`
  ❌ where 引出的是一个句子，the magic of reading books 后面缺动词；"所在"的"在"就是 lies（或 is）
- 2026-09-20 ✅ 学习日 在池第 1 组 · `that is where the magic of reading lies` —— where 后面那句有动词，"所在"落成句末的 lies；首测一次中
- 2026-09-21 ✅ 学习日 在池第 1 组 [3] · `It's where the magic of reading lies.` —— where 引出的句子挂上了动词 lies，且放在最后。连对 1 → 2 ⇒ 🎓
- 2026-09-27 ⚡ 自评免测 · 复检第 2 组（她原话："2.d 忘了，其他直接过"）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）· 题型 词组 → 整句
  去掉"一个动词、放在最后"形态描述，改零提示整句（where … lies／is 与 what … is all about 都算对），逼的是她掉过的 where ＋ 名词不带动词

### 347 · "对于 X，他们…" ⇒ X 直接当主语（⛔ For office workers, they …）
类型 结构 ｜ 新建 2026-09-19
状态 连对2 连错0 上次2026-09-28 ｜ **🎓 已毕业 2026-09-22** ｜ 题型 整句

**问题是什么**
中文话题句"对于上班族，他们…／对老人来说，他们…"先摆一个话题，再用代词把它重说一遍当主语。
英语一个句子只要一个主语 ⇒ **X 直接当主语**：Office workers usually have no choice but to eat out.
同一格里的邻居（别串）：For X 后面换了**另一个**主语是对的 —— For office workers, eating out is the only option. ／
For me, reading is more relaxing.（主语不是回指 X 的代词）· 🎓#135 管的是"社会／大家"这种中文主语用 there is／被动吃掉，
本条管的是主语说了两遍 ⇒ 两条并存。
判据一句话：For X 后面的主语是不是又指回 X（they／he／it）？是 ⇒ 删掉 For，让 X 直接当主语。

**怎么发现的**
2026-09-19 付息日 d 段重答 R11（P3 · Do people today prefer eating at home or in a restaurant?）· 原话
`For office workers, they usually have no choice but to eat out or order takeout`（diff-2 ⚠️，不是 ❌；她确认按 §3.2b 建号）
判重三步：
　① 目标形式 X 直接当主语 ⇒ dedup "For office"／"对于"／"主语重复"／"双主语" ⇒ 零命中；"当主语" ⇒ 🎓#135（"社会／大家"用 there is／被动吃掉）、
　　 🎓#216（东西不会自己 leave）⇒ 都是"主语选谁"，本条是"主语说了两遍" ⇒ 否
　② 中文 "对于…他们" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`For office workers, they usually have no choice but to eat out`　　更地道：`Office workers usually have no choice but to eat out`
找法：说完 For X，看下一个主语是不是又是指 X 的代词；是就把 For 删掉，X 直接当主语。

**题面**
"对老年人来说，他们还是更喜欢去实体店买东西。"
　　★ 零提示：Older people … ／ For older people, shopping in person … 都算对；她要改掉的是 For X, they … 主语说两遍

- 2026-09-19 新建 · 付息日 d 段重答 R11（P3）· 原话 `For office workers, they usually have no choice but to eat out or order takeout`（⚠️ 更地道的表达，她确认建号）
- 2026-09-20 ✅ 学习日 在池第 1 组 · `office workers have no choice but to grab a quick bite outside.` —— office workers 直接当主语，没有 For office workers, they… 那一层；首测一次中
  ⚠️ diff-2：grab a quick bite outside → eat out or grab something quick（归 🎓#180）· 补 usually
- 2026-09-22 ✅ 学习日 在池第 1 组 [3] · `Office workers have no choice but to grab a quick bite out.` —— Office workers 直接当主语，没有 For office workers, they… 那一层 ⇒ **连对 2，毕业**
  ⚠️ diff-2：漏了"一般"（→ usually，🎓#22 她会，检索滑手）· a quick bite out → a quick bite somewhere（grab a quick bite 自带"在外面"，out 多余）
- 2026-09-28 ✅ 复检第 2 组 · `Office workers usually have no choice but to grab a quick bit outside.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）
  去掉"⛔ option／choice 当主语"，改零提示；换成老年人去实体店场景 —— For X, they … 主语说两遍这条路照旧开着

### 348 · "好吃"挂在吃的东西上：the food tastes better（⛔ cooking is delicious）
类型 搭配 ｜ 新建 2026-09-19
状态 连对2 连错0 上次2026-09-28 ｜ **🎓 已毕业 2026-09-22** ｜ 题型 整句

**问题是什么**
delicious／tasty／tastes good 说的是**吃的东西**。中文"在家做饭更好吃"把动作和做出来的饭说成一件事，
英语要把"好吃"挂到饭上：Home-cooked food tastes way better. ／ …, and the food tastes way better.
同一格里的邻居（别串）：cooking at home is cheaper／healthier／cleaner —— 这些形容词能说动作，照用。
⛔ **tastes more delicious**：delicious 本身已经是"很好吃"，英语不给它再加 more ——
　"更好吃"的口语比较级就是 **tastes better**（加强用 way better／so much better）。
判据一句话：谓语是"好吃"吗？主语就得是吃的东西（the food／home-cooked food），⛔ 不是 cooking／eating out。

**怎么发现的**
2026-09-19 付息日 d 段重答 R11（P3 · Do people today prefer eating at home or in a restaurant?）· 原话
`If you have the time, cooking at home is cleaner and way more delicious.`（diff-2 ⚠️，不是 ❌；她确认按 §3.2b 建号）
判重三步：
　① 目标形式 the food tastes better ⇒ dedup "delicious"／"taste"／"好吃" ⇒ 零命中
　② 中文 "好吃" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`cooking at home is cleaner and way more delicious`　　更地道：`cooking at home is cleaner, and the food tastes way better`
找法：说到"好吃"先看主语是不是吃的东西；是动作（cooking／eating out）就把"好吃"挂到 the food 上。

**题面**
"自己在家烤的蛋糕，比外面买的好吃多了。"（"好吃"用 **taste** 说）

- 2026-09-19 新建 · 付息日 d 段重答 R11（P3）· 原话 `cooking at home is cleaner and way more delicious`（⚠️ 更地道的表达，她确认建号）
- 2026-09-20 ✅ 学习日 在池第 1 组 · `Cooking at is cleaner and the food tastes more delicious.` —— "好吃"挂在 the food 上，没说成 cooking is delicious；首测一次中
  ★ `Cooking at` 掉了 home ＝ 打字掉字（§2.1 同理，不记档位）
  ⚠️ diff-2：tastes more delicious → tastes way better（delicious 已是"很好吃"，不再加 more；"更好吃"的口语比较级就是 better）
  ⇒ §3.3 硬顺序③ 答得合法但不是条目预期 ⇒ 记 ✅ ＋ 当场改题面（补 ⛔ 不许用 delicious／tasty）
- 2026-09-22 ✅ 学习日 在池第 1 组 [4] · `Cooking at home is much cleaner, and the food tastes far better.` —— "好吃"挂在 the food 上、用 taste，没用 delicious／tasty ⇒ **连对 2，毕业**
  ★ 09-20 那次写的是 tastes more delicious，本次比较级自己走到了 better ⇒ 条目里"delicious 不加 more"那一条当场兑现；far better ⛔ 不改（与 way better 同级）
- 2026-09-28 ✅ 复检第 2 组 · `Cooking at home is much cleaner, and the food tastes better.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"⛔ delicious／tasty"，只点名 taste，主语挂哪、比较级怎么说留给她；换成烤蛋糕场景

### 349 · "网上／通过网络" ＝ online（⛔ through the internet）
类型 词组 ｜ 新建 2026-09-19
状态 连对2 连错0 上次2026-09-28 ｜ **🎓 已毕业 2026-09-22** ｜ 题型 词组

**问题是什么**
"网上／通过网络／在网上就能…" 口语就是 **online**，一个副词，挂在句首或动词后面：
You can do pretty much anything online. ／ I booked it online.
同一格里的邻居（别串）：on the internet 也对（介词短语，稍长）· 🎓#8 管的是 in an online group／on a forum 的介词，⛔ 不是这一格 ·
⛔ through the internet 是"通过"直译，能懂但不地道。
判据一句话：中文"网上／通过网络" ⇒ online；想用介词短语就 on the internet，⛔ through。

**怎么发现的**
2026-09-19 付息日 d 段重答 R12（P3 · Why do some people not like using apps?）· 原话
`Through the internet, you can do pretty much anything—order takeout, hail a ride, pay utility bills, you name it.`（diff-2 ⚠️，她确认按 §3.2b 建号）
判重三步：
　① 目标形式 online ⇒ dedup "online" ⇒ 🎓#8（in an online group）、🎓#209（an online pet group 的形容词顺序）、🎓#50、🎓#81 都是正文里带 online 字样的别的考点 ⇒ 否；
　　 dedup "through the internet" ⇒ 零命中
　② 中文 "网上" ⇒ 🎓#8／🎓#262／🎓#312 都是别的考点 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`Through the internet, you can do pretty much anything`　　更地道：`Online, you can do pretty much anything`／`You can do pretty much anything online`
找法：说到"通过网络／在网上"，先落 online。

**题面**
"在网上预约挂号"（手机上直接就能办）

- 2026-09-19 新建 · 付息日 d 段重答 R12（P3）· 原话 `Through the internet, you can do pretty much anything`（⚠️ 更地道的表达，她确认建号）
- 2026-09-20 ✅ 学习日 在池第 1 组 · `you can do pretty much anything online.` —— 一个副词 online 挂句末；首测一次中
- 2026-09-22 ✅ 学习日 在池第 1 组 [5] · `You can do pretty much everything online.` —— 一个副词 online 挂句末，没用 internet／through the internet ⇒ **连对 2，毕业**
- 2026-09-28 ✅ 复检第 2 组 · `You can do petty much everything online.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉"一个词 ＋ ⛔ internet"，改中文释义；换成网上挂号场景

### 350 · let your imagination run wild（让想象力放开跑）
类型 词组 ｜ 新建 2026-09-19
状态 连对2 连错0 上次2026-09-28 ｜ **🎓 已毕业 2026-09-22** ｜ 题型 整句

**问题是什么**
"让想象力自由发挥／放开想" ＝ **let your imagination run wild**（固定说法；run free 同样地道）。
也可以把 imagination 当主人：Reading gives your imagination room to run wild.
同一格里的邻居（别串）：run with sth ＝ 接过一个想法往下做（run with the idea），⛔ 不配 imagination。
判据一句话：说想象力放开 ⇒ imagination ＋ run wild／run free。

**怎么发现的**
2026-09-19 付息日 d 段重答 R13（P3 · What are the differences between reading a book and visiting a museum?）· 原话
`Reading gives you room to run with your imagination, while museums speak to more of your senses.`（diff-2 ⚠️，她确认按 §3.2b 建号）
判重三步：
　① 目标形式 let your imagination run wild ⇒ dedup "run wild" ⇒ 零命中；"imagination" ⇒ 🎓#299、🎓#206 正文里带这个词，别的考点 ⇒ 否
　② 中文 "想象力" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`Reading gives you room to run with your imagination`　　更地道：`Reading gives your imagination room to run wild`
找法：imagination 后面想接"放开／自由发挥" ⇒ run wild。

**题面**
"放假了，就让孩子们的想象力放开了跑吧。"（"放开了跑"用 **run** 说）

- 2026-09-19 新建 · 付息日 d 段重答 R13（P3）· 原话 `Reading gives you room to run with your imagination`（⚠️ 更地道的表达，她确认建号）
- 2026-09-20 ✅ 学习日 在池第 1 组 · `let your imagination run wild.` —— imagination ＋ run wild 整块；首测一次中
- 2026-09-22 ✅ 学习日 在池第 1 组 [6] · `Let your imagination run wild.` —— imagination ＋ run wild 整块，没写成 run with your imagination ⇒ **连对 2，毕业**
- 2026-09-28 ✅ 复检第 2 组 · `let your imagination run wild.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  点名 run，let … imagination … wild 怎么搭留给她；换成孩子放假场景

### 351 · feel ＋ 名词必须加 like（it feels **like** a mini-escape）
类型 语法 ｜ 新建 2026-09-20
状态 连对2 连错0 上次2026-09-28 ｜ **🎓 已毕业 2026-09-22** ｜ 题型 整句

**问题是什么**
**feel 后面挂名词，中间必须有 like**：It feels **like** a mini-escape. ／ It feels **like** home. ／ That felt **like** a waste of time.
同一格里的邻居（别串）：feel ＋ **形容词** ⛔ 不加 like（It feels weird. ／ I feel tired.）；
feel like ＋ **-ing** ＝ 想做某事（🎓#258 whenever they feel like it）—— 那条管"想不想"，本条管"像不像"。
同族的动词一样处理：look／sound／smell／taste ＋ 名词也要 like（It looks **like** a museum. ／ It sounds **like** fun.）。
判据一句话：feel／look／sound 后面跟的是**名词**吗？是 ⇒ 补 like；是形容词 ⇒ 不补。

**怎么发现的**
2026-09-20 学习日 新题 bank:1038（P3 · Why do people like to visit historical sites?）· 触发原话
`Going to a historical site feels a mini-escape.`
判重三步：
　① 目标形式 feel like ⇒ dedup "feel like" ⇒ 命中 🎓#258（at will → whenever they feel like it ＝ feel like ＋ -ing，"想做某事"）⇒ 否，两条规则；
　　　🎓#264（a sense of）· 🎓#206（书面降级）只是正文里出现过这两个词 ⇒ 否
　② 中文题面 dedup "感觉像" ⇒ 零命中
　③ 保留新建

**我错在哪**
她的：`Going to a historical site feels a mini-escape.`　　正确：`Going to a historical site feels **like** a mini-escape.`
找法：说完 feel／look／sound，看后面第一个词 —— 是个名词就补 like。

**题面**
"这家小咖啡馆让人感觉就像在自己家里一样。"
　　★ 零提示：feels like home／feels like being at home 都算对；她掉过的是 feel 直接挂名词、漏了 like

- 2026-09-20 ❌ 首犯 · 新题 bank:1038（P3）· 原话 `Going to a historical site feels a mini-escape.`
- 2026-09-21 ✅ 学习日 在池第 1 组 [4] · `going to ancient sites feels like a mini-escape.` —— feel ＋ 名词把 like 补上了，没用 is／seems（09-20 首犯正在这里）。连错 1 清零、连对 0 → 1
- 2026-09-22 ✅ 学习日 在池第 1 组 [1] · `Going to ancient sites feels like a mini-escape.` —— feel ＋ 名词把 like 补上了，没用 is／seems ⇒ **连对 2，毕业**
- 2026-09-28 ✅ 复检第 2 组 · `Going to ancient sites feels like a mini-escape.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）
  去掉"像那个词不许省 ＋ ⛔ is／seems"，改零提示；换成咖啡馆像家场景 —— feel 直接挂名词这条路照旧开着

### 352 · "亲眼看到真东西" ＝ seeing the real thing（⛔ the real-life feeling）
类型 词组 ｜ 新建 2026-09-20
状态 连对2 连错0 上次2026-09-29 ｜ **🎓 已毕业 2026-09-26** ｜ 题型 整句

**问题是什么**
中文"真实感／实物感"别硬拼成一个名词（the real-life feeling）。英语把它说成**动作**：
**seeing the real thing** ／ **seeing it in real life** ／ **seeing it in person**（🎓 R13 里她自己用过 in person）。
同一格里的邻居（别串）：the real-life **feel** of it 勉强能说，但口语几乎都走 seeing 那条；
⛔ the real-life feeling 是把中文的"感"直译成 feeling。
判据一句话：想说"真实感" ⇒ 换成"亲眼看到真东西"这个动作来说。

**怎么发现的**
2026-09-20 学习日 新题 bank:1038（P3 · Why do people like to visit historical sites?）· 触发原话
`It mainly comes down to two simple things: the real-life feeling and a change of pace.`
判重三步：
　① 目标形式 the real thing ⇒ dedup "the real thing" ⇒ 命中 🎓#306（not just A — it's more B，只是正文里出现过）⇒ 否；
　　　dedup "real life" ／ "in person" ⇒ 零命中
　② 中文题面 dedup "真实" ⇒ 命中 🎓#60 #84 #59 #275 全是"真实条件句／嵌入疑问"⇒ 否，不同考点
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`the real-life feeling`　　正确：`seeing the real thing`（或 `seeing it in real life`）
找法：中文里出现"…感"，先别找名词，先问一句 —— 这个"感"是从哪个**动作**来的？

**题面**
"照片拍得再好，也比不上亲眼看到真东西。"（"真东西"用 **real** 说）

- 2026-09-20 新建 · 新题 bank:1038（P3）· 触发原话 `the real-life feeling`（⚠️ 更地道的表达，§3.2b）
- 2026-09-21 ✅ 学习日 在池第 1 组 [5] · `see the real things.` —— 考点命中：把"真实感"换成**动作**来说、用了 real、没用 feeling ⇒ 符合题面（§3.3 硬顺序①②）。连对 0 → 1
  ★ `the real things` 的 -s ⇒ ⚠️ 不判 ❌：the real thing 恒单数，但题面没点名单数 ⇒ 判定只认题面（§6 ⛔ 不让她猜教练想要什么）⇒ 当场改题面，见同日 📝 行
- 2026-09-21 📝 题面整改（§3.3 硬顺序③）· 原题面 "亲眼看到真东西"（用 **real** 说 · ⛔ 不许用 feeling／feel）
  → 现题面 "亲眼看到真东西"（用 **real** 说 · 是一个**单数**的固定块 · ⛔ 不许用 feeling／feel）
  —— 提示不受粒度限制（§6②），补一句"单数"把 the real thing 变成唯一答案；考点（别把"真实感"名词化，改说动作）一个字没动
- 2026-09-26 ✅ 付息日 a 在池第 1 组 [5] · `See the real thing in person.` —— the real thing 单数固定块，没用 feeling ⇒ **连对 2，毕业**
- 2026-09-29 ✅ 复检第 2 组 · `see the real thing.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"单数固定块 ＋ ⛔ feeling／feel"，只点名 real；换成照片比不上亲眼看场景
- 2026-09-29 📝 补题面（上一批 🎓#352 状态行改了整句、题面节替换没落上，本行补记新场景：照片比不上亲眼看）

### 353 · vibe 是【地方带的】，人不待在 vibe 里（a place with a different vibe）
类型 搭配 ｜ 新建 2026-09-20
状态 连对2 连错0 上次2026-10-01 ｜ **回潮 2026-09-29**（09-26 毕业 → 09-29 复检写成 in a totally different vibe，撤销毕业、连对清零）｜ **🎓 已毕业 2026-10-01**（连对2 ＝ 09-30 ＋ 10-01；09-29 回潮后第二次毕业）｜ 题型 整句

**问题是什么**
**vibe ＝ 一个地方/一件事给人的调子**，它挂在地方上，⛔ 不是人待进去的空间：
`somewhere with a completely different vibe` ／ `the place has a really chill vibe` ／ `soak up a different vibe`。
⛔ chill **in** a different vibe —— in 把 vibe 当成了房间。
同一格里的邻居（别串）：真要说"待在里面"就换个有空间义的名词：in a totally different setting／atmosphere。
判据一句话：vibe 前面想加 in ⇒ 停：改成 with a … vibe 挂在地方上，或者把 vibe 换成 setting。

**怎么发现的**
2026-09-20 学习日 新题 bank:1038（P3 · Why do people like to visit historical sites?）· 触发原话
`you just get to chill in a totally different vibe.`
判重三步：
　① 目标形式 vibe ⇒ dedup "vibe" ⇒ 零命中；dedup "atmosphere" ⇒ 零命中
　② 中文题面 dedup "气氛" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`you just get to chill in a totally different vibe`　　正确：`you get to chill somewhere with a totally different vibe`
找法：写完 vibe，回头看它前面是不是 in —— 是就把它挂回地方上（with a … vibe）。

**题面**
"周末去一个氛围完全不一样的小镇待两天，整个人都放松了。"（"氛围"用 **vibe** 说）

- 2026-09-20 新建 · 新题 bank:1038（P3）· 触发原话 `chill in a totally different vibe`（⚠️ 更地道的表达，§3.2b）
- 2026-09-21 📝 题面整改（发题前，§6.5 第 6 项）· 原题面"能在一个气氛完全不一样的地方待着。"中文省了主语 ⇒ 整句题却可能被答成一个裸词组 ⇒ 补出主语"你"，考点（vibe 挂在地方上）一个字没动
- 2026-09-21 ✅ 学习日 在池第 1 组 [6] · `you can stay somewhere with a completely different vibe.` —— vibe 挂回了地方上（somewhere with a … vibe），前面不是 in。连对 0 → 1
- 2026-09-26 ✅ 付息日 a 在池第 1 组 [6] · `You get to somewhere with a totally different vibe.` —— vibe 挂在地方上（somewhere with a … vibe），前面不是 in ⇒ **连对 2，毕业**
  ★ 同句 get to 后漏动词 ⇒ 不属本条，新建 #360
- 2026-09-29 ❌ 复检第 2 组 · `you get to chill somewhere in a totally different vibe.`（vibe 前用了 in）—— **回潮**
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉「⛔ vibe 前面不许用 in」（那是考点本身），只点名 vibe；换成周末小镇场景
- 2026-09-30 ✅ 付息日 a 段在池第 1 组 [5] · `The cafe has such a great vibe, I go there all the time to read.`
- 2026-10-01 ✅ 学习日 在池第 1 组 [5] · `I prefer working at a small company with a relaxed vibe.` —— vibe 挂在地方上（a small company with a relaxed vibe），前面不是 in ⇒ **连对 2，毕业**

### 354 · as for ＋ 名词（"至于…"；⛔ as far ＋ 名词 —— as far as … goes 才是完整块）
类型 词组 ｜ 新建 2026-09-21 ｜ 与 🎓#317 互斥（见「问题是什么」末行）
状态 连对2 连错0 上次2026-09-29 ｜ **🎓 已毕业 2026-09-26** ｜ 题型 整句

**问题是什么**
**as for ＋ 名词／名词性从句** ＝ "至于…／说到…"，**两个词一组**，后面直接挂名词：
`as for the price` · `as for what's trending right now` · `as for me`。
同一格里的邻居（别串）：**as far as … goes ／ as far as … is concerned** ＝ "就…而言"，它是**四段式**，
后半截（goes／is concerned）⛔ 不能省；**when it comes to ＋ 名词** ＝ "一说到…"，三个词，同义但更长。
⛔ `as far ＋ 名词` ＝ 把上面两个块的前半截拼在一起，英语里不存在这个说法。
判据一句话：写完 as far，回头看后面有没有 `as … goes`？没有 ⇒ 把 far 换成 for。
★ 与 🎓#317（when it comes **TO** sth）分工：那条考 come 那一族的介词，本条考 as for 这个块 ——
　本条零提示（as for／when it comes to 都算对，测的是会不会拼出 as far ＋ 名词），🎓#317 点名 come ⇒ 两边各测各的。

**怎么发现的**
2026-09-21 学习日 新题 bank:1005（P3 · What are the differences between old and young people's music preferences?）· 触发原话
`As far what's trending right now, I'm actually not too sure`。
判重三步：
　① 目标形式 as for ⇒ dedup "as for"／"as far as" ⇒ 命中 🎓#59（直接疑问 vs 嵌入疑问，考的是从句语序）·
　　　🎓#298（have the final say，考的是 say 当名词）—— 两条都只是正文/历史里出现过这个字母串 ⇒ 否，考点不同
　② 中文题面 dedup "至于" ⇒ 命中 🎓#250（that far vs too far，考的是 far 有没有"刚才那句话"可指）⇒ 否，那条管指代、本条管块
　③ 保留新建（⛔ 建号当天不测）
收尾复核（§4⑤1b，同日）：补查 dedup "when it comes to" ⇒ 命中 🎓#317（when it comes **TO** sth）· 🎓#58（it mainly comes down to）
　⇒ 两条的目标形式都是 come 那一族，本条是 as for ⇒ **两条，不并**；按判重三步③ 当场落实**题面互斥**：
　　本条题面点名"两个词的块 · 第一个词是 **as**" ⇒ 排掉 when it comes to；
　　🎓#317 题面点名"用 **come** 说" ⇒ 排掉 as for。两边各自唯一，⛔ 不会撞车。

**我错在哪**
她的：`As far what's trending right now`　　正确：`As for what's trending right now`
找法：写完 as far，回头问一句 —— 后面有没有 as … goes？没有就把 far 换成 for。

**题面**
"工资还行，至于加班多不多，我还不太清楚。"
　　★ 零提示：as for／when it comes to／regarding 都算对；她掉过的是拼出来的 as far ＋ 名词

- 2026-09-21 ❌ 首犯 · 新题 bank:1005（P3）· 原话 `As far what's trending right now, I'm actually not too sure`
- 2026-09-22 ✅ 学习日 在池第 1 组 [2] · `As for what's trending now.` —— as for ＋ 名词性从句，两个词一组，没写成 as far（09-21 首犯正在这里）。连错 1 清零、连对 0 → 1
- 2026-09-26 ✅ 付息日 a 在池第 1 组 [2] · `As for what's trending right now` —— as for ＋ 名词性从句，没写成 as far ⇒ **连对 2，毕业**
- 2026-09-29 ✅ 复检第 2 组 · `as for what's trending now.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）· 题型 词组 → 整句
  去掉"两个词／第一个词是 as ＋ 三个排除项"，改零提示整句（as for／when it comes to／regarding 都算对），逼的是她掉过的 as far ＋ 名词；换成工资加班场景

### 355 · ballad ＝ 抒情慢歌（情歌／民谣那一类）
类型 词汇 ｜ 新建 2026-09-21 ｜ ⭐ 她点名要背
状态 连对2 连错0 上次2026-09-30 ｜ 题型 词组 ｜ **🎓 已毕业 2026-09-27**

**问题是什么**
**ballad** ＝ 节奏慢、以唱情绪为主的歌（情歌、抒情曲）：`a power ballad` · `all sorts of ballads` · `a slow ballad`。
可数，说"这一类歌"时常用复数 ballads。
同一格里的邻居（别串）：**folk music** ＝ 民谣／民间音乐（一个**流派**，不可数）· **pop music** ＝ 流行乐（流派，不可数）·
**a tune** ＝ 一首曲子（中性，指任何一首）。
判据一句话：说的是"慢歌／情歌"这一类**歌曲** ⇒ ballad（可数）；说的是"哪个**流派**" ⇒ pop／folk ＋ music（不可数）。

**怎么发现的**
2026-09-21 学习日 新题 bank:1005（P3）· 她在自己的产出里主动标注 `all sorts of ballads(这个单词要背）`
—— 词**用对了**，是她点名要收进复习（§2③ 她主动提出的）。
判重三步：
　① 目标形式 ballad ⇒ dedup "ballad" ⇒ 零命中
　② 中文题面 dedup "慢歌" ⇒ 零命中（同批查的 "至于" 命中 🎓#250，与本条无关）
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
本条不是她犯的错：她这次写的 `all sorts of ballads` 完全正确，缺的是"下次还调不调得出来"。
找法：想说"抒情慢歌／情歌"，先别拼 slow songs，先问一句 —— 有没有一个 **b** 开头的名词？

**题面**
"我爸最爱听的那种抒情慢歌"（节奏慢、以唱感情为主的歌）

- 2026-09-21 新建 · 新题 bank:1005（P3）· 触发原话 `all sorts of ballads(这个单词要背）`（⭐ 她点名要背，词本身用对了）
- 2026-09-22 ✅ 学习日 在池第 1 组 [7] · `various ballads` —— 一个 b 开头的名词 ballads 调出来了，没退回 slow songs／love songs（建号后首测）。连对 0 → 1
  ⚠️ diff-2：various → all sorts of（书面词降级，走 §7 书面登记记在 🎓#206；她 09-21 自己写的就是 all sorts of ⇒ ⛔ 不另建号）
- 2026-09-27 ✅ 在池第 1 组 · `all sorts of ballads.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉"一个名词、b 开头 ＋ 排除项"猜谜写法，改中文释义；换成"我爸爱听的"场景
- 2026-09-30 ✅ 复检 · 付息日 a2 第 3 组 [2] · `A slow, romantic ballad.`

### 356 · "另一些人" ＝ others（⛔ some ones）
类型 词组 ｜ 新建 2026-09-22 ｜ 与 ⚪#324 分工（见「问题是什么」末行）
状态 连对2 连错0 上次2026-09-30 ｜ 题型 整句 ｜ **🎓 已毕业 2026-09-27**

**问题是什么**
"有些人…，另一些人…" 的第二个"人"，英语用 **others** 一个词顶（others ＝ other people）：
`Some people learn by reading, while others learn by doing.` ／ `Some like it hot, others don't.`
同一格里的邻居（别串）：**ones** 必须先有一个**可指的名词**才站得住（`the cheap ones` ＝ the cheap shoes）——
凭空一个 `some ones` 没有可指的名词 ⇒ 英语里不存在这个说法；`other people` 合法但长，口语默认 others。
判据一句话：说第二拨人时，句子里有没有一个刚提过的名词给 ones 指？没有 ⇒ 用 others。
★ 与 ⚪#324（other 是限定词、others 才是代词）分工：那条的检查触发是"**写完 other**，看后面有没有名词"——
　本句里压根没有 other 可查（她写的是 some ones）⇒ 那条的检查跑不起来、产不出 others ⇒ 两条不同考点。

**怎么发现的**
2026-09-22 学习日 新题 bank:1102（P3 · Do you think some people are better than others at persuading?）· 触发原话
`while some ones speak with so much emotion that they quickly connect at an emotional level`。
判重三步：
　① 目标形式 others ⇒ dedup "others" ⇒ 命中 ⚪#324（other／others 的限定词与代词之分，形态类·不召回）·
　　　🎓#236 · 🎓#313 · 🎓#81（三条只是正文/历史里出现过 others 这个字串，考点分别是不定式目的、message sb、get to know sb）
　　　⇒ #324 逐条读完后否掉：它管"写出来的 other 少了 -s"，本条管"第二拨人该调 others 这个词"——
　　　按 #324 的检查触发扫这一句 ⇒ 句里没有 other ⇒ 检查不触发（与 #324 当初否掉 #150 是同一条判据）
　② 目标形式 dedup "some ones" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`while some ones speak with so much emotion`　　正确：`while others speak with so much emotion`
找法：写完 some people 之后要说第二拨人 —— 先落 others，⛔ 不要把 some 再用一次。

**题面**
"有的孩子喜欢画画，另一些更喜欢踢球。"
　　★ 零提示：others／other kids 都算对；她掉过的是 some ones

- 2026-09-22 ❌ 首犯 · 新题 bank:1102（P3）· 原话 `while some ones speak with so much emotion`
- 2026-09-26 ✅ 付息日 a 在池第 1 组 [3] · `some people persuade you with reason, while others win you over through emotion.` —— 第二拨人用 others 一个词顶。连错 1 清零、连对 0 → 1
- 2026-09-27 ✅ 在池第 1 组 · `Some people persuade you with logic, while others drive you with emotion.` —— others 到位
  ｜drive you with emotion ⚠️ ⇒ 建号 #363（appeal to sb's emotions）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）
  去掉"一个词 ＋ ⛔ some／other people"，改零提示（others／other kids 都算对），逼的是 some ones；换成画画踢球场景
- 2026-09-30 ✅ 复检 · 付息日 a2 第 3 组 [3] · `…, while others prefer to do it at night.`

### 357 · logic 是名词、logical 才是形容词（a strong logical thinker）
类型 词汇 ｜ 新建 2026-09-22
状态 连对2 连错0 上次2026-10-02 ｜ **🎓 已毕业 2026-09-29** ｜ 题型 整句

**问题是什么**
**logic ＝ 名词**（这门学问／这套道理：`the logic behind it`），修饰后面的名词要用形容词 **logical**：
`a strong logical thinker` ／ `a logical explanation` ／ `logical thinking`。
同一格里的邻居（别串 —— 同一条 -ic → -ical 派生规则下的别的词，本条只管 logic 这一对）：
magic→magical · music→musical · practice→practical · politics→political。
判据一句话：这个词后面还挂着一个名词吗？挂着 ⇒ 它得是形容词形（logical），⛔ 不是光秃秃的 logic。
★ 不是拼写（§2.1）：logic 与 logical 是**两个词**（名词 vs 形容词），不是同一个词写歪。

**怎么发现的**
2026-09-22 学习日 新题 bank:1102（P3 · Do you think some people are better than others at persuading?）· 触发原话
`Some people are strong logic thinkers who can persuade others through reason`。
判重三步：
　① 目标形式 logical ⇒ dedup "logical" ⇒ 零命中
　② 中文题面 dedup "逻辑" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`strong logic thinkers`　　正确：`strong logical thinkers`
找法：写完 logic，看后面还有没有名词。有 ⇒ 补 -al。

**题面**
"她是个逻辑特别强的人，跟她吵架从来没赢过。"
　　★ 零提示：a very logical person／she has really strong logic 都算对；她掉过两次的是 logic 直接修饰名词（a strong logic thinker）

- 2026-09-22 ❌ 首犯 · 新题 bank:1102（P3）· 原话 `Some people are strong logic thinkers`
- 2026-09-26 ✅ 付息日 a 在池第 1 组 [4] · `A logical thinker.` —— logic 后面挂名词 ⇒ logical。连错 1 清零、连对 0 → 1
  ★ 漏了"很强"（strong）⇒ diff-2 ⚠️，不建号
- 2026-09-27 ❌ 在池第 1 组 · `A strong logic thinker` —— logic 仍当形容词放在 thinker 前
  最小改 `A strong logical thinker`
- 2026-09-28 ✅ 在池第 1 组 · `a strong logical thinker.`
- 2026-09-29 ✅ 在池第 1 组 · `A strong logical thinker.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）· 题型 词组 → 整句
  去掉"logic 的家族 ＋ 排除项"，改零提示整句，logic 直接修饰名词这条她掉过两次的路照旧开着；换成吵架场景
- 2026-10-02 ✅ 复检 · 学习日 复检第 4 组 [2] · `We need to hire a developer with a solid logical mindset.` —— logical 当形容词修饰名词

### 358 · on a(n) … level（在…层面；⛔ at an emotional level）
类型 搭配 ｜ 新建 2026-09-22
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-28** ｜ 题型 整句

**问题是什么**
"在…层面"有**两个块**，⛔ 不是"on 对 at 错"，分界线是**冠词**：
· **on ＋ a(n) ＋ 形容词 ＋ level** ＝ 从某个**角度**／在某种程度上（不定冠词）：
　`connect with people on an emotional level` ／ `on a personal level` ／ `on a deeper level` ／ `on some level` ／ `on a practical level`
· **at ＋ the ＋ 形容词 ＋ level** ＝ 一套**层级**里的某一层（定冠词，行政／组织／分析的层级，永远能跟另一层并排）：
　`at the national level` ／ `at the local level` ／ `at the individual level` ／ `at the social level` ／ `at the policy level`（也说 `at the level of the individual`）
· **at ＋ 物理高度**（永远 at）：`at eye level` ／ `at sea level` ／ `at street level`
同一格里的邻居（别串）：`emotionally` 说得通，但它是副词，说不了"在某个层面上"这个比喻。
另外 connect 要把人带上：connect **with sb** on a … level（论元完整，同族 🎓#18）。
判据一句话：冠词是 **a/an**、说的是"从某个角度" ⇒ **on**；冠词是 **the**、而且那一层能跟别的层并排（个人层 vs 国家层）⇒ **at**。
★ 她的那句 `connect ___ an emotional level`：冠词是 an、说的是"从情感这个角度跟人连上"（不跟别的层并排）⇒ 走 on，
　且 connect 与 on 本身就是固定搭配（connect with sb **on** a … level）。

**怎么发现的**
2026-09-22 学习日 新题 bank:1102（P3 · Do you think some people are better than others at persuading?）· 触发原话
`they quickly connect at an emotional level`（diff-2 ⚠️，不是 ❌ —— 意思能懂、也偶有人这么说，但地道说法是 on）。
判重三步：
　① 目标形式 on an emotional level ⇒ dedup "on an emotional level"／"level" ⇒ 两次都零命中
　② 中文题面 dedup "层面" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`they quickly connect at an emotional level`　　更地道：`they quickly connect with people on an emotional level`
找法：说到"在…层面"，**先看冠词** —— a/an（从某个角度）⇒ on；the ＋ 能跟别的层并排（国家层／个人层／社会层）⇒ at。

**题面**
"好的广告往往是在情感层面上打动人。"（"在…层面上"用 **level** 说）

- 2026-09-22 新建 · 新题 bank:1102（P3）· 触发原话 `they quickly connect at an emotional level`（⚠️ 更地道的表达 ⇒ §3.2b 建号）
- 2026-09-22 📝 **正文订正（她当场推翻我写窄的判据）**：她问「at the social level 是 at 还是 on」——
  `at the social level` 完全成立（社会这一层 vs 个人那一层 ＝ 层级用法）⇒ 建号时写的"at ＋ level 只用于物理高度"**是错的**，
  当天改成按**冠词**分的两个块（on a/an ＋ 角度 ／ at the ＋ 层级 ／ at ＋ 物理高度）。
  ⛔ 判定口径同步放宽：她若答 `at the … level` 且说的是层级 ⇒ **判 ✅**；本条真正要卡的只有"从某个角度"那一格该用 on。
- 2026-09-26 ✅ 付息日 a 在池第 1 组 [7] · `Connect with people on an emotional level.` —— on ＋ an ＋ 形容词 ＋ level，connect 带上 with people。首测，连对 0 → 1
- 2026-09-28 ✅ 在池第 1 组 · `You connect with others on an emotional level.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"⛔ emotionally"，只点名 level，on／at 与冠词留给她；换成广告打动人场景
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [1] · `This song means a lot to me on a personal level.` —— on a personal level

### 359 · persuasion ＝ 说服（名词；动词 persuade · 形容词 persuasive）
类型 词汇 ｜ 新建 2026-09-22 ｜ ⭐ 她点名要背
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-28** ｜ 题型 词组

**问题是什么**
**persuasion** ＝ "说服"这件事（名词，不可数）：`successful persuasion` ／ `the art of persuasion` ／
`it took a lot of persuasion`。
同一格里的邻居（别串 —— 同一个词根的三个形）：**persuade sb to do sth** ＝ 动词（`she persuaded me to go`）·
**persuasive** ＝ 形容词（`a persuasive argument` ＝ 有说服力的）· **convince sb of sth** ＝ 近义动词（偏"让人信"，
persuade 偏"让人做"）。
判据一句话：句子里这一格要的是**一件事／一个名词**吗？是 ⇒ persuasion；要的是动作 ⇒ persuade；形容一个论点 ⇒ persuasive。

**怎么发现的**
2026-09-22 学习日 新题 bank:1102（P3 · Do you think some people are better than others at persuading?）·
她在自己的产出里主动标注 `successful persuasion(这个单词背一下)`
—— 词**用对了**，是她点名要收进复习（§2③ 她主动提出的）。
判重三步：
　① 目标形式 persuasion ⇒ dedup "persuas" ⇒ 零命中（全档没有这个词根的条目）
　② 中文题面 dedup "说服" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
本条不是她犯的错：她这次写的 `successful persuasion` 完全正确，缺的是"下次还调不调得出来"。
找法：要说"说服"这件事本身（当名词用），先问一句 —— persuade 的名词形是什么？

**题面**
"做销售最要紧的说服能力"（让人被你说动的那种本事）

- 2026-09-22 新建 · 新题 bank:1102（P3）· 触发原话 `successful persuasion(这个单词背一下)`（⭐ 她点名要背，词本身用对了）
- 2026-09-26 ✅ 付息日 a 在池第 1 组 [8] · `successful persuasion. The art of persuasion.` —— 两处都调出名词 persuasion。首测，连对 0 → 1
- 2026-09-28 ✅ 在池第 1 组 · `successful persuasion. the art of persuasion.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉"一个名词、p 开头 ＋ 排除项"，改中文释义；换成销售说服能力场景（09-26 发过的两个块⛔不复用）
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [2a] · `The power of persuasion in a speech.` —— the power of persuasion

### 360 · get to ＋ 动词原形 ＝ 能／有机会做（⛔ get to ＋ somewhere）
类型 语法 ｜ 新建 2026-09-26
状态 连对2 连错0 上次2026-10-01 ｜ **🎓 已毕业 2026-09-28** ｜ 题型 整句

**问题是什么**
"能／有机会做某事"用 **get to** 说时，to 是**不定式**，后面必须接一个**动词原形**：
`you get to chill somewhere` ／ `you get to see the real thing` ／ `you get to meet new people`。
同一格里的邻居（别串）：
· **get to ＋ 地点名词** ＝ 到达（`get to the station`），这里的 to 是介词（🎓#336）
· **get ＋ somewhere／there／home** ＝ 到达，这几个是副词，⛔ 不带 to
· **get to know sb** ＝ "认识"那个固定块（🎓#81）
判据一句话：get to 表示"能／有机会"时，to 后面是不是一个动词？不是 ⇒ 补一个（be／stay／chill／go）。
★ 与 🎓#336 分工：那条的 to 是介词、后面挂地点名词；本条的 to 是不定式、后面挂动词 ⇒ 两条规则。
★ 与 🎓#81 分工：那条考"to 别漏"（get to know），本条考"to 后面要有动词"。

**怎么发现的**
2026-09-26 付息日 a 在池第 1 组 [6]（#353 题面"你能待在一个气氛完全不一样的地方。"）· 她的原话
`You get to somewhere with a totally different vibe.`
（#353 的考点 vibe 挂在地方上是对的，判 ✅；本条是同句另一处）
判重三步：
　① 目标形式 get to ＋ 动词原形 ⇒ dedup "get to" ⇒ 命中 🎓#81（get to know sb：考 to 不能省，⇒ 否，本条考 to 后要有动词）·
　　　🎓#336（get to ＋ 地点名词：to 是介词，⇒ 否，本条的 to 是不定式）· #353（只是历史里出现 get to chill，考 vibe ⇒ 否）·
　　　🎓#50 #86 #98 #206 ⚪#324 #356（只是正文/历史里出现 get to 字串，考点分别是 easier／go on a trip／并列同形／书面降级／others ⇒ 否）
　② dedup "somewhere" ⇒ 命中 #353 🎓#206 🎓#347，都只是历史里出现过这个词 ⇒ 否；中文 dedup "待在" ⇒ 只命中 #353 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`You get to somewhere with a totally different vibe.`　　正确：`You get to be somewhere with a totally different vibe.`
找法：写完 get to，看后面是不是一个动词；不是 ⇒ 补一个（be／stay／chill／go）。

**题面**
"当老师最开心的，就是能看着孩子们一点点长大。"（"能"用 **get to** 说）

- 2026-09-26 ❌ 首犯 · 付息日 a 在池第 1 组 [6]（#353 同句）· 原话 `You get to somewhere with a totally different vibe.`
- 2026-09-27 ✅ 在池第 1 组 · `When you're on vacation, you get to speed the whole day at the beach.` —— get to ＋ 原形到位
  ｜speed ＝ spend 打漏 n，§2.1 拼写不算
- 2026-09-28 ✅ 在池第 1 组 · `When you are on vacation, you get to spend the whole day at the beach.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"⛔ can／be able to"，正向点名 get to，后面接动词原形留给她；换成当老师场景
- 2026-10-01 ✅ 复检 · 学习日 复检第 3 组 [3] · `The best part about being a teaching is getting to watch kids grow up step by step.` —— get to 后面接了动词（getting to watch）｜teaching → teacher 打字，§2.1 不算

### 361 · 准点下班 ＝ get off work on time（⛔ leave work early ＝ 早退）
类型 词组 ｜ 新建 2026-09-26
状态 连对2 连错0 上次2026-10-02 ｜ **🎓 已毕业 2026-09-29** ｜ 题型 整句

**问题是什么**
"准点下班／到点就走" ＝ **get off work on time**（也说 leave work on time）。
同一格里的邻居（别串）：**leave work early** ＝ 早退（下班时间还没到就走）· **work overtime** ＝ 加班 · **get off work** ＝ 下班（不带时间点）。
判据一句话：想说"不加班、到点走"，先问 —— 是"到点"还是"提前"？到点 ⇒ on time。

**怎么发现的**
2026-09-26 付息日 d 段重答 bank:778（R16 · P3 · What kind of job can be called a 'dream job'?）· 触发原话
`If you can leave work early, you have enough time for other things like hobbies, or speeding time with your kid.`
（diff-2 ⚠️：上下文是"不加班的工作"，要说的是到点走，不是早退）
判重三步：
　① 目标形式 get off work on time ⇒ dedup "get off work" ⇒ 零命中；dedup "on time" ⇒ 命中 🎓#92（否定别丢）· 🎓#98（并列同形）·
　　　🎓#206（书面降级）· 🎓#340（a step up）· 🎓#341（deserve praise）· ⚪#63（泛指特指）—— 全是正文/历史里出现过这个字串，考点都不是"准点下班" ⇒ 否
　② 中文题面 dedup "准点" ⇒ 零命中；"下班" ⇒ 命中 🎓#98（题面"下班后有时间做点别的"，考并列同形）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`If you can leave work early`　　更地道：`If you can get off work on time`
找法：说"下班"时先问一句 —— 是到点走还是提前走？到点 ⇒ on time；提前才是 early。

**题面**
"自从换了工作，我终于能准点下班了。"（"下班"用 **get off** 说）

- 2026-09-26 新建 · 付息日 d 段重答 bank:778（R16）· 触发原话 `If you can leave work early`（⚠️ 更地道的表达 ⇒ §3.2b 建号）
- 2026-09-27 ✅ 在池第 1 组 · `You can get off work on time every day.` —— 首测，块一字不差
- 2026-09-29 ✅ 在池第 1 组 · `get off work on time every day.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  去掉"get 起头 ＋ ⛔ early"，只点名 get off，on time 留给她；换成换工作场景
- 2026-10-02 ✅ 复检 · 学习日 复检第 4 组 [3] · `I finally managed to get off work on time today, only to end up stuck in traffic for an hour.` —— get off work on time

### 362 · turn down ＋ 机会（没人会拒绝…；⛔ no one can refuse）
类型 词组 ｜ 新建 2026-09-26
状态 连对2 连错0 上次2026-10-02 ｜ **🎓 已毕业 2026-09-29** ｜ 题型 整句

**问题是什么**
"拒绝一份工作／一个邀请／一个机会"口语用 **turn down**：`turn down a job offer` ／ `turn it down`。
"没人会拒绝"的情态动词用 **would**：`no one would turn that down`（can 是"能不能"，no one can refuse 听着像"谁都没能力拒绝"）。
同一格里的邻居（别串）：**refuse to do sth** ＝ 拒绝做某事（后面接动作）· **say no to sth** ＝ 同义口语说法。
判据一句话：拒绝的是一个机会／邀请 ⇒ turn down；说"会不会拒绝" ⇒ would。

**怎么发现的**
2026-09-26 付息日 d 段重答 bank:778（R16 · P3 · What kind of job can be called a 'dream job'?）· 触发原话
`Overall, no one can refuse a job with reasonable hours and job security.`
判重三步：
　① 目标形式 turn down ⇒ dedup "turn down" ⇒ 零命中
　② 中文题面 dedup "拒绝" ⇒ 命中 🎓#332（名词化的"提议"拆回动词 ＋ when 从句，考结构不考拒绝这个词）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`no one can refuse a job with reasonable hours`　　更地道：`no one would turn down a job with reasonable hours`
找法：说"没人会拒绝"时，情态动词先落 would；拒绝的是机会 ⇒ turn down。

**题面**
"那家公司给我开了很高的工资，我最后还是拒绝了。"（"拒绝"用 **turn** 说）

- 2026-09-26 新建 · 付息日 d 段重答 bank:778（R16）· 触发原话 `no one can refuse a job with reasonable hours and job security`（⚠️ 更地道的表达 ⇒ §3.2b 建号）
- 2026-09-27 ✅ 在池第 1 组 · `No one would turn down a job this good.` —— 首测，turn down 到位
- 2026-09-29 ✅ 在池第 1 组 · `Nobody would turn down a job this good.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉"⛔ refuse／say no"，只点名 turn；换成拒绝高薪场景
- 2026-10-02 ✅ 复检 · 学习日 复检第 4 组 [4] · `The university offered him a position as a professor, but he turned it down.` —— turned it down
