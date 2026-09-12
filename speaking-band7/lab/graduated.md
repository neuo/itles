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
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

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
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-19**（复习不再召回；再犯就把状态行改回未毕业，连对清零）｜ 题型 整句

**问题是什么**
**That's where …** ＝ 高复用块，用来点"就是在这儿／这就是…的地方"：`That's where the Yangtze River starts.`
同一格里的邻居（别串）：⛔ It starts here ／ This is the place —— 两个都合法，但都绕开这个块 ⇒ 题面已排除。
判据一句话：中文说"就从这里／就是在那儿"⇒ 先落 **That's where**，再把句子接下去。

**怎么发现的**
旧 B 表迁移（B3，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ✅。
2026-08-15 ◎ 题面没逼出 ⇒ 当天改点名；2026-08-19 ✅ 点名 · `That's where the Yangtze river starts.` ⇒ 毕业。
2026-09-09 复检第 4 组 ✅ `That's where the Yangtze River begins.`

**我错在哪**
她的：本条历史里没有掉过（2026-08-15 那次是 ◎ ＝ 题面没逼出，⛔ 不是她错），触发原话未存。
找法：中文出现"就是从这儿／这就是…的地方"⇒ 张口先给 **That's where**，别现造句子。

**题面**
**点名**："长江就从这里开始。"（用 **That's** 起头说一遍，⛔ 不许用 It starts here／This is the place）

- 2026-08-11 ✅
- 2026-08-15 ◎ 题面没逼出
- 2026-08-16 ✅
- 2026-08-19 ✅ 点名 · `That's where the Yangtze river starts.`
- 2026-09-09 ✅ 复检 · 第 4 组 · `That's where the Yangtze River begins.`

### 4 · 空评价骨架可丢（不说 famous，直接给事实）
类型 减法型 ｜ 旧号 B4
状态 连对2 连错0 上次2026-08-29 ｜ **🎓 已毕业 2026-08-29**（连对2）｜ **⛔ 复习组停出** ｜ 题型 产出验

**问题是什么**
**空评价骨架可丢**：不说 famous／important／good 这一层，**直接给事实**。
（类型标"减法型"＝ 要她**少说**一层，不是多学一个块。）
同一格里的邻居（别串）：评价词**后面跟了事实**就不算掉 ——
`a really wide and long river` → spanning China from west to east ｜ `super cloudy` → it must have been full of sand ｜
`the primary source for Yibin` → supplying … residential and industrial use across the city。
判据一句话：这个评价词后面有没有跟着一条具体事实？没有 ⇒ 整个删掉。

**怎么发现的**
旧 B 表迁移（B4，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-29 新题 P2（Describe an important river/lake）＝ 本条题面写死的判定场，逐处核过、一处空评价都没有 ⇒ 连对 2，毕业。
★ 2026-08-17 她指出旧题面自相矛盾（题面里有"出名"却要求不译）⇒ 改成挂自由产出抓。

**我错在哪**
她的：本条**历史零 ❌**、从没掉过任何一格（§4① 加速通道边界自查当天写明），触发原话未存。
找法：说完 famous／important／good，回头看下一句给没给事实；没给就把那个评价词删掉。

**题面**
不出中译英题；**挂当日自由产出抓**（出现 famous/important/good 而后面没跟事实 → ❌）

- 2026-08-17 ✅ 首次进流
- 2026-08-29 ✅ 新题 P2（Describe an important river/lake）· **本条题面写死"挂当日自由产出抓"，今天这篇就是它的判定场**
  逐处核过，**每一个评价词后面都跟了事实**，一处空评价都没有：
  `a really wide and long river` → spanning China from west to east, emptying into the East China Sea
  `super cloudy` → it must have been full of sand
  `the primary source for Yibin` → supplying … residential and industrial use across the city
  `holds special significance` → considered one of the mother rivers, along with the Yellow River
  ⇒ 连对1 → **连对2，毕业**
  ★ 加速通道边界自查（§4①）：本条**历史零 ❌**、从没掉过任何一格 ⇒ 不存在"掉的那一格没被测到"
    的情况 ⇒ 边界不适用，照常推进连对
- ⚠️ 08-17 她指出题面自相矛盾（题面里有"出名"却要求不译），已改成挂自由产出

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
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 整句

**问题是什么**
**预制块里的情态／副词是功能核心**（could／never／really 这一层不能省）：`I **could** eat hotpot every day.`
同一格里的邻居（别串）：⛔ can —— could 那层是"我天天吃都愿意"（表达喜欢），can 是"有能力"，两者不是一回事；题面已排除 can。
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
**点名**："我能天天吃火锅。"（"能"那一层不许省 · ⛔ 不许用 can）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ◎ 她答 `I can eat hotpot every day` 完全合法（"我有能力天天吃"）
  ⇒ 中文两种译法都成立，题面的锅 → 当天加点名"用 could 说"，次日再测
- 2026-08-20 ✅ 复习（点名题面首测）· `I could eat hotpot every day.`——could 出来了
- 2026-09-11 ✅ 复检 · 付息日 a2 第 2 组 · `I could eat hotpot pretty much every day` —— could 没被吞（pretty much 是她自己加的口语缓冲）
- 2026-09-12 📝 题面整改：点名「用 could 说一遍」→「"能"那一层不许省 · ⛔ 不许用 can」—— 原点名把考点（could 不能省）直接交出去（§6② 红线一），排除 can 之后 could 要她自己调 · 全档题面 review
- 备注 could 那层是"我天天吃都愿意"（表达喜欢），can 是"有能力"，两者不是一回事

### 8 · 群组用 in，论坛用 on（in an online group／on a forum）
类型 搭配 ｜ 旧号 B20＋B130
状态 连对2 连错0 上次2026-09-11 ｜ **回潮 2026-08-31**（08-20 毕业 → 08-31 在 R8 重答里再犯 `on an online pet group`，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-03**（连对2 ＝ 09-01 ＋ 09-03；08-31 回潮后第二次毕业）｜ 题型 词组
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
- 备注 合并 2026-08-19：#82（群组用 in，论坛用 on）并入本条 —— 同一条介词规则
  ★ 不走零 ❌ 线：备注里明写它"改过又犯"过，只是那次发生在事件流之前 ⇒ 按有 ❌ 处理，仍需连对 3
- 备注 曾"改过又犯"（轮94 改、轮95 又犯）

### 9 · 换谓语升级：is+形容词 → 实义动词（只在说"对人的作用"时换）
类型 结构 ｜ 旧号 B22
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个也毕业"）｜ 题型 整句

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

### 11 · no questions asked ＋ for any reason（单数）
类型 词组 ｜ 旧号 B32＋B100
状态 连对2 连错0 上次2026-09-09 ｜ **回潮 2026-09-05**（08-20 她指定毕业 → 09-05 复检两个成员只到一个：no questions asked 有、for any reason 没调出来，撤销毕业、连对清零。★ 2026-09-07 补：这一判定 09-05 当天写进了 session 却漏了 `append`，回潮同步迟到两天） ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）｜ 题型 词组
**问题是什么**
"无理由退货"的两个固定块 —— 一条规则下的两个成员：
· **no questions asked**（questions 是被问的一方 ⇒ 过去分词 **asked**；整块背，⛔ 不拆开想时态）
· **for any reason**（reason 用**单数**）
同一格里的邻居（别串）：⛔ without a reason（题面已排除）。
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
**点名**："无理由退货"（"无理由"用一个固定块说，不要 without a reason；**两个说法都要**——一个带 questions，一个带 reason）

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
- 备注 整块背：questions 是被问的一方 ⇒ 过去分词 asked（＝ with no questions being asked），不拆开想时态
- 备注 合并 2026-08-19：#188（for any reason ＋ no questions asked）并入本条，**同题面同块**

### 13 · 共享主语减 I（一个 I 带两个动词）
类型 结构 ｜ 旧号 B35
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

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

### 14 · well away（程度旋钮：不换词只加精度）
类型 词组 ｜ 旧号 B36
状态 连对1 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20 · 她指定** ｜ 题型 词组
　　（原话："我觉得这道题不好，我不喜欢用 well，用 far 没啥问题，这道题毕业"）
　　⇒ 判定：**这是可选升级块，不是缺口** —— `far away from the road` 本身完全正确，
　　　 well away 只是另一个说法。她已有正确产出且明确不想用这个块 ⇒ 停止召回

**问题是什么**
**well away**（程度旋钮：不换词，只加精度）—— "离马路远远的" ＝ well **away** from the road。
同一格里的邻居（别串）：`far away from the road` 本身完全正确，well away 只是另一个说法；
⛔ 标准英语 well 不叠 far（`well far` 只在英式口语俚语里出现 ＝ very far，考场语域不搭）⇒ 题面已排除 far。
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
**点名**："离马路远远的"（"远远的"用 well ＋ 一个词，**那个词不是 far**）
　　★ 题面 2026-08-20 改：原点名只说"well ＋ 一个词"，`well far` 就是合法执行 ⇒ 排除法补一句

- 2026-08-17 ◎ 题面没逼出（far away 也合法）→ 08-17 改点名
- 2026-08-19 ❌ `well far from the traffic`——点名生效（她确实产出 well ＋ 一个词），但词选错
- 2026-08-20 ✅ `he lives well far away from the road`
  ⛔ **教练先判 ❌、她质疑后撤销**：题面只说"well ＋ 一个词"，`well far` 是**照着点名执行**的合法产出
  ⇒ 按 08-20 新规则【符合题面就算对 ＋ 改题面】，本次记 ✅，题面已加"那个词不是 far"
  ⚠️ 语言点仍成立、只是不计分：标准英语 well 不叠 far（well away／far away 各自成立；
     `well far` 只在英式口语俚语里出现＝ very far，考场语域不搭）
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· well away from（well ＋ away，⛔ 不是 far）
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 备注 更高一档的说法（房子离马路退得远）：`His house is set well back from the road.`
- 备注 well 当程度旋钮只配固定那几个：well away／well worth／well past／well over／well aware／well ahead
- 备注 08-19 她问"the road 哪个好" → the road 对（马路这条路）；the traffic 是路上的车流

### 15 · deep down ／ It's not that A, it's just B ／ can't be bothered
类型 词组 ｜ 旧号 B37
状态 连对2 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

**问题是什么**
同一条目下的三个块：
· **deep down** ＝ 内心深处（**副词块**，⛔ 不用 heart／inside）
· **It's not that A, it's just B** ＝ 不是…，只是…
· **can't be bothered** ＝ 懒得动（比 lazy 更口语；题面把 lazy 排除，逼的就是它）
同一格里的邻居（别串）：lazy 是**说人**的 —— `I'm just lazy` 对、`It's just lazy` 不对（08-19 她当场自己纠过）。
判据一句话："内心深处"想到名词（心／里面）就走错了，它是个副词块；"懒得动"别停在 lazy。

**怎么发现的**
旧 B 表迁移（B37，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `deep down, I know I should go to bed early. It's not that I don't want to go. I'm just lazy.`
⭐ 她自纠：先写 `It's just lazy`，当场改成 `I'm just lazy`（lazy 说人）。
2026-09-09 复检第 4 组 ✅ 两个考点块都在位（deep down ⛔ 没用 heart／inside ＋ It's not that A, it's just B）。

**我错在哪**
她的：`It's just lazy`（08-19 当场自纠）／ `It's not that I don't go`（09-09 复检，"想"那层漏译，⛔ 不判档位、不建条目）
正确：`I'm just lazy` ／ `It's not that I don't want to go, I'm just lazy.`
找法：说"内心深处"直接找副词块 deep down，⛔ 别去够 heart／inside；说"懒得动"往 can't be bothered 上引。

**题面**
"内心深处"（副词块 · ⛔ 不许用 heart／inside） ／ "不是不想去，只是懒得动"（⛔ 不许用 lazy）

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
- 备注 第三个块 can't be bothered（懒得动）比 lazy 更口语，下次可以往这上引

### 16 · 让某人做某事四件套（get sb TO do 只有它带 to；have/make/let/watch/see sb DO）
类型 搭配 ｜ 旧号 B39
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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
"让学生自己试"（"让"用 **get** 说）

- 2026-08-11 ❌ 同族 `watch the machine BUILDS it`
- 2026-08-12 ✅
- 2026-08-16 ✅

- 2026-08-19 ✅ `teachers should get students to try it themselve`（get sb TO do 选对）
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· `let students ... try`（原形，⛔ 没多加 to）
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `get students to try it themselves`（get sb TO do，四件套里只有 get 带 to）
- ⚠️ 与已毕业的 #143（哪些动词后面要带 to）是同一条规则的两个角度 —— 付息日 c 段处理

### 17 · talk AT sb（单向灌输）vs talk TO sb
类型 搭配 ｜ 旧号 B40
状态 连对2 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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
"对着你讲一小时"（单向灌输那种"讲" · 用 **talk** ＋ 一个介词说）

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

### 18 · 论元完整（中文可单说的动词，英文必须带宾语/补语）
类型 结构 ｜ 旧号 B41
状态 连对2 连错0 上次2026-09-11 ｜ **累错 7** ｜ **🎓 已毕业 2026-09-01**（连对2 ＝ 08-31 ＋ 09-01；08-29 回潮后第二次毕业）｜ 题型 整句
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
- 备注 primed 8/8 但 20 分钟后 cold 即掉 ⇒ 产出时掉，修法只有块化
- ⚠️ **必须和 #134 一起读**（08-19 判重发现两条会互相带偏）：本条说"英文动词必须带宾语"，
  #134 说"decide/choose/help/manage/win 这些能单独站住"。**先查这个动词在不在 #134 的白名单里**，
  不在名单里才补宾语 —— 否则修一处带偏隔壁（#134 的备注里已经记过这个教训）

### 19 · 分数说法（a half / a third / a quarter / two thirds）
类型 词组 ｜ 旧号 B42
状态 连对2 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

**问题是什么**
**often ＝ 经常**（频次高）。位置：主语后、实义动词前 —— `my friend **often** goes to that shop.`
同一格里的邻居（别串）：usually ＝ 通常情况下（＝ #22，两条**题面互斥**）；
frequently／a lot 也是"频次高"、也合法 ⇒ 2026-09-10 题面补了首字母提示「**o** 开头」才把 often 框死。
判据一句话：说的是**次数多** ⇒ often；说的是**一般情况下** ⇒ usually。

**怎么发现的**
旧 B 表迁移（B44，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `my friend often goes to that shop.`（often 位置对 ＋ goes 的 -s 没掉）⇒ 毕业。
2026-09-10 复检第 3 组（打包）✅ —— 新题面（补了「**o** 开头」）下首测即命中。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅，🎓 零 ❌ 线），触发原话未存。
找法：中文"经常"先分一刀 —— 讲的是次数（often）还是常态（usually）？

**题面**
"经常"（副词，频次高 · **o** 开头 · ⛔ 不许用 usually）
★ 与 #22 题面互斥（原写在元信息行；元信息行留"题面"二字会被 check 当成第二处题面 ⇒ 移到本节）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `my friend often goes to that shop.`（often 位置对 ＋ goes 的 -s 没掉）
- 2026-09-10 📝 题面补首字母提示「**o** 开头」· 复检第 3 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面只排除了 usually，但 `frequently`／`a lot` 同样是"频次高"的副词、同样不在排除项里
  ⇒ 题面不唯一可判。补 `**o** 开头` 把 often 框死。
- 2026-09-10 ✅ 复检 · 第 3 组（打包）· `often` —— 新题面（补了「**o** 开头」）下首测即命中

### 22 · usually ＝ 通常情况下
类型 词汇 ｜ 旧号 B188
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

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
- 备注 她误用 usually 三次；always ＋ 习惯动词是常见夸张，不算错

### 23 · 固定词序整块背（back and forth · now and then · sooner or later · more or less）
类型 词组 ｜ 旧号 B45
状态 连对2 连错0 上次2026-09-09 ｜ **回潮 2026-09-05**（08-19 毕业 → 09-05 复检答"忘了"、在 forward／forth 之间不确定，撤销毕业、连对清零） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）｜ 题型 词组
**问题是什么**
**固定词序整块背**：back and forth · now and then · sooner or later · more or less ·
give or take · sick and tired · safe and sound —— 词序焊死（back and forth ✅ ／ forth and back ❌）。
同一格里的邻居（别串）：forth 今天几乎只活在 back and forth ／ and so forth 里 ⇒ **只按块记、⛔ 不当单词记**；
`to and fro` 也满足"三个词 ＋ and ＋ 词序不许倒"⇒ 2026-09-07 补首字母提示「**b 开头**」才把它排掉。
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
"来回"（副词块 · 三个词、中间用 and 连 · **b 开头** · ⛔ 词序不许倒）

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

### 24 · 搭配三件（work FROM home · handle orders · sales 恒复数不带 the）
类型 搭配 ｜ 旧号 B47
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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

### 25 · It's no use doing sth（做某事没用）
类型 搭配 ｜ 旧号 B48
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 整句

**问题是什么**
**It's no use doing sth** ＝ 做某事没用（固定框，后面挂 **-ing**）：`it's no use fining people for littering`。
同一格里的邻居（别串）：#32 记的是"There's no point 比 It's no use 更常用"——两条**不矛盾**（都成立，只是常用度不同）
⇒ **她用 It's no use ⛔ 不许判错**；只有她问"哪个更常听"时才提 There's no point。题面已把 There's no point 排除。
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
"罚款对乱扔垃圾没什么用。"（"没什么用"用 **use** 那个词的固定框说，⛔ 不许用 There's no point）

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
- ⚠️ **捆绑条目**：本次只验了 It's no use doing 一块；litter 不可数／fine sb FOR doing 两块未再验
  ⇒ 付息日按"一条＝一个考点"拆号时，那两块各自从 0 起算重建
- ⚠️ 与 #32 的关系（付息日 c 段要写进两条备注）：#32 记的是"There's no point 比 It's no use 更常用"，
  两条**不矛盾**（都成立，只是常用度不同），别把她用 It's no use 判成错

### 26 · 比较题必须说出另一边（prefer A ＝ 比 B，B 一次不出现 ＝ 逻辑缺口）
类型 结构 ｜ 旧号 B49
⛔ **复习组停出**（她 2026-08-20 定："后面不要出这种题了，在新题中自然会考"）—— 本条只在新题/重答的自由产出里判
状态 连对2 连错0 上次2026-08-27 ｜ 顽固已断 ｜ **🎓 已毕业 2026-08-27**（她 2026-08-29 裁定：连对已到 2，算毕业；日期回填到凑满连对 2 那天）｜ **⛔ 复习组停出** ｜ 题型 产出验

**问题是什么**
**比较题必须说出另一边**：prefer A ＝ 比 B 好 —— B 一次都不出现 ＝ 逻辑缺口。
判据一句话：这一答里 B 那一边出现了吗？没出现 ⇒ 论证是空的。
★ 接法（08-27 那次最值得记的）：第一句先立一根**共同的尺子**
（`the differences mainly depend on how much effort you put in`），后面两段各站一端 ＝ methods **M5**。
★ 本条 ⛔ 复习组停出（她 2026-08-20 定）⇒ 只在新题／重答的自由产出里判档位，⛔ 不出中译英题。

**怎么发现的**
旧 B 表迁移（B49，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ❌、2026-08-17 ❌。
2026-08-19 ⛔ 教练把题面发成一句英文问句、没说要做什么，她问"没懂" ⇒ 本次作废，题面当天改成自带交付方式。
2026-08-20 ✅ 复习 · `On the other hand, working in a group requires more time and energy for communication`——B 那一边明确说出来了。
2026-08-27 ✅ **自发命中** · 付息日 d 段重答 R5（everyday food vs festival food）· 两边都说出来、各占一段。
2026-08-29 她裁定"连对已到 2，算毕业"，毕业日回填到 08-27。

**我错在哪**
她的：08-11／08-17 两次只说了 A 那一边（触发原话未存）；08-06 首答 R5 那次没有那根共同的尺子。
找法：说完 prefer A 立刻问自己一句 —— B 呢？B 不出现就还没答完。

**题面**
不出中译英题（题型 产出验 ＋ ⛔ 复习组停出）；挂新题／重答的自由产出抓：比较题里 B 那一边出现没有、有没有一根共同的尺子。
★ 原题面（留档，⛔ 不再发题）：【这题不是翻译。用英文答 3–4 句，题目：Why do some people prefer working alone?】

- 2026-08-11 ❌
- 2026-08-17 ❌
- 2026-08-19 ⛔ 教练把题面发成一句英文问句、没说要做什么，她问"没懂" ⇒ 本次作废不计档位；
  题面已改成自带交付方式（这题不是翻译／答几句／题目原文），当天重出
- 2026-08-20 ✅ 复习 · `On the other hand, working in a group requires more time and energy for communication`
  ——B 那一边明确说出来了，顽固断在这一次
- 2026-08-27 ✅ **自发命中**（本条 `⛔ 复习组停出`，只在自由产出里判 —— 今天正是这样判的）·
  付息日 d 段重答（R5 everyday food vs festival food）·
  **两边都说出来了、各占一段**：everyday food（just for getting fed／grab a meal／ten minutes）
  ／ festival food（takes more time and energy／a whole day／a big meal）
  ★ 更值得记的是**她怎么把两边接起来的**：第一句先立一根共同的尺子
    （`the differences mainly depend on how much effort you put in`），后面两段各站一端
    ⇒ ＝ methods **M5**（差异题不是找相似点，是找一根尺子说两边各在哪一端）。
    08-06 首答那次没有这根尺子
- 2026-08-29 📝 **她裁定：连对已到 2，算毕业**（2026-08-29）· 毕业日按惯例回填到凑满连对 2 的那一天
  ＝ **2026-08-27**（付息日 d 段重答 R5 的那次自发命中）。
  ★ 本条是 `⛔ 复习组停出`，两次 ✅ 都来自自由产出 —— §4① 的「加速通道」在它身上走通了整条路：
    复习组一次没出过，靠自发命中攒满连对 2。
- 2026-09-11 📝 题型回标 `产出验` ＋ 把「⛔ 复习组停出」补进**状态行** · 付息日 a2 第 2 组发题前（§6.0 上线当天）
  ⛔ **本条 2026-08-20 就被她裁掉了**（原话："后面不要出这种题了，在新题中自然会考"），
    但那句 `⛔ 复习组停出` 当时只写在**正文行**、没写进状态行 ⇒ 脚本读的是状态行 ⇒
    它在召回队列里躺了 3 周还在被抽（今天又被抽中，`used --dropped` 弃掉）。
  ⇒ 今天补进状态行 ＋ 标 `题型 产出验`，自动离队；本次⛔不出题、⛔不记档位。
  ★ 全档复查：`grep 复习组停出` 12 处命中里只有本条是「正文有、状态行没有」，
    其余 5 条（#67 #206 #207 #252 #253）都写在状态行上 ⇒ **只此一例**，⛔ 不是系统性漏洞

### 27 · the credit gets shared（团队里功劳被分摊）
类型 词组 ｜ 旧号 B50
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 词组

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
- 备注 口语默认走 get-passive：`the credit just gets shared`（不必补 by everyone）

### 28 · You just get more done at home.（用画面替掉 more efficient）
类型 词组 ｜ 旧号 B52①
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-24** ｜ 题型 词组

**问题是什么**
**get more done** ＝ 干得更多（用画面替掉 more efficient）：`I get more done when I work from home.`
同一格里的邻居（别串）：⛔ do more／finish more（题面已排除）；
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
**点名**："干得更多"（用 **get** 那个动词说，⛔ 不许用 do／finish more）

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
- （B52 六句补录，迁移时按 Q4 拆成 #28–#33 六条）
- 备注 2026-08-25 · **反向留痕（不改状态、不回潮）**：自由产出（新题 bank:987 P3）里她写的是
  `your output at work will be less than your coworkers'` —— 语法全对、比较也对齐，
  但口语走法就是本条这个块：**you just won't get as much done as your coworkers**。
  ⇒ 昨天在中译英里调出来了、今天在自由产出里没调出来。
  **不判回潮**（本条的考点是"会不会用这个块"，她会；掉的是 retrieval，不是知识），
  但这是"知识在、检索没跑"最干净的一个实例，记在这里备查

### 29 · You don't have to sit in meetings all day.
类型 词组 ｜ 旧号 B52②
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-24 · 她指定** ｜ 题型 词组

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
- 备注 **#28–#33 这六条全部是"用块替掉平铺说法"型 ⇒ 天生第②类，出题一律点名**

### 30 · Say you fix something …（Say you… ＝ 举例起手，替 For example）
类型 词组 ｜ 旧号 B52③
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 整句

**问题是什么**
**Say you …** ＝ 举例起手（一个词替掉 For example），后面直接接完整从句：
`Say you fix a problem that the entire team got stuck on`。
同一格里的邻居（别串）：⛔ for example／for instance／suppose／imagine／let's —— 都合法，但都绕开这个词 ⇒ 题面已排除。
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
**点名**："比方说你解决了一个全组都卡住的问题。"（"比方说"用**一个词**起头 · ⛔ 不许用 for example／for instance／suppose／imagine／let's）

- 2026-08-19 ✅ 首次进池 · 点名 · `Say you solve a problem the whole team was stuck on`
  ⭐ 同句还自发用对三个已毕业点：关系代词省略 ＋ 介词留末尾 ＋ stuck ON
- 2026-08-20 ✅ 复习 · `Say you solve a problem that the whole team is stuck with.`——Say you 起手对
  ｜同句 `stuck with`（该 stuck on）归 🎓#248 回潮 —— **同一道题昨天写的是 stuck on，一天之内从对变错**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `Say you fix a problem that the entire team got stuck on` —— Say 起头 ＋ 后接完整从句
  ⚠️ 顺带（不计档位）：entire → whole（口语默认）· got stuck → is stuck（现在还卡着 ⇒ 现在时）
- 2026-09-12 📝 题面整改：点名「用 Say 起头」→「用一个词起头 · ⛔ 不许用 for example／for instance／suppose／imagine／let's」—— 原点名把考点 Say 本身交出去（§6② 红线一）· 全档题面 review

### 31 · explain YOURSELF to anyone（解释自己的行为）
类型 搭配 ｜ 旧号 B52④
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ ⚠️ 状态行 08-21 按日志重算（08-20 的 ✅ 当天漏回写）｜ 题型 词组

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
**点名**："跟任何人解释自己"（用 explain 说）

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
- 备注 同族块：explain yourself／behave yourself／enjoy yourself／help yourself —— 反身代词是块的一部分

### 33 · on a clear day（替 if it's clear）
类型 词组 ｜ 旧号 B52⑥
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-24** ｜ 题型 词组

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

### 35 · 禁双重否定：否定 → no- 词，动词一律肯定（Nobody knows.）
类型 语法 ｜ 旧号 B54＋B207c
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（她 08-20 定：连对 2 即毕业，不论历史有无 ❌）｜ 题型 整句

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
- 备注 合并 2026-08-19：#124（否定 → no- 词，且动词不再否定）并入本条 —— 同一条规则
  ⚠️ **本条 08-19 曾按"零 ❌ 线"判毕业，合并后撤销**：并入 #124 的日志后 08-16 有一个 ❌，
     零 ❌ 线不适用，连对只有 2 ⇒ 回到未毕业，还差一次

### 36 · all morning / all day / all night 不带 the
类型 搭配 ｜ 旧号 B55
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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
"一上午"（用 all ＋ 一个名词说）

- 2026-08-11 ✅
- 2026-08-15 ❌
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ✅ `he played games all night`（all night 不带 the）
  ★ 教练一度按"零 ❌ 线"判它毕业 —— **判错了**，本条 08-15/08-16 两个 ❌ 就在日志里，
    零 ❌ 线不适用；已撤销，仍需连对 3
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· all morning（⛔ 不带 the）
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `all morning`（⛔ 没落进 the whole morning）

### 37 · everyday（形容词）≠ every day（副词短语）
类型 语法 ｜ 旧号 B56
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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

### 38 · feel the energy in the room
类型 词组 ｜ 旧号 B57b
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-20**（08-20 全库回扫漏网，08-21 按日志重放补记）｜ 题型 词组

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
**点名**："感觉不到现场那种气氛"（"那种气氛"用 energy 那个词说）

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

### 39 · 惯用定冠词：the TV / the radio / the cinema / on the screen
类型 语法 ｜ 旧号 B58
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

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

### 40 · 删掉自我对冲的 a bit（对比句要给足）
类型 结构 ｜ 旧号 B59
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

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
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

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

### 43 · come to your city / come to town（乐队巡演到某地）
类型 词组 ｜ 旧号 B62
状态 连对1 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个题毕业了，不要再考了"）｜ 题型 整句

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

### 44 · good AT doing ／ 升级版 He cooks well.
类型 搭配 ｜ 旧号 B66
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

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

### 45 · walk to work（by 后面只接交通工具）
类型 搭配 ｜ 旧号 B67
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 46 · 主语复数，表语也要复数（hobbies are things you choose）
类型 语法 ｜ 旧号 B68
状态 连对2 连错0 上次2026-09-09 ｜ **回潮 2026-09-05**（08-20 毕业 → 09-05 复检用了 what 从句，题面点名的"表语用名词"没测到，撤销毕业、连对清零。★ 2026-09-07 补：这一判定 09-05 当天写进了 session 却漏了 `append`，回潮同步迟到两天） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）｜ 题型 整句

**问题是什么**
**主语复数，表语也要复数**：hobbies **are things** you choose —— 表语用**名词**说。
同一格里的邻居（别串）：`hobbies are what you choose` 完全合法，但它把表语换成了 what 从句、绕开考点
⇒ 题面点名"表语用名词说，不用 what 从句"。
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
**点名**："业余爱好是自己挑的事，工作不是。"（表语用名词说，不用 what 从句）

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

### 47 · 反差句两边都要说完（连接词用 but/whereas，不用 and）
类型 结构 ｜ 旧号 B69
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

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

### 48 · work 不可数 ＝ 活儿（说"这份工作"用 my job）
类型 语法 ｜ 旧号 B70
状态 连对2 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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

### 50 · "好找/好用/好记"用 easier，不用 more convenient（convenient ＝ 方式省事）
类型 搭配 ｜ 旧号 B73
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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
- 备注 ★ 本条就是她 08-21「直译要 case by case 建」那条规则的**正面样本**：
  `more convenient to find` 这个具体 case 早在 08-11 就有自己的号（本条），
  却又被 08-16 复制进伞形条目 #157 的日志里 ⇒ **同一个 case 占两个号、走两条 streak**，
  #157 那条永远清零、她被反复问。#157 已于 08-21 迁出 methods.md，本条保留。

### 51 · put sth away ＝ 收起来（clean up ＝ 打扫脏东西）
类型 词组 ｜ 旧号 B74
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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

### 52 · 去掉 "X is important" 的壳（把动作提上来当谓语）
类型 减法型 ｜ 旧号 B75
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

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

### 53 · organized（说人）＝ 有条理会安排，不是守规矩
类型 词汇 ｜ 旧号 B76
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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

### 54 · 比较级只标一次（more easier ❌）
类型 语法 ｜ 旧号 B77
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

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
- 备注 与 #10 主谓一致／#147 时态只标一次／#92 否定别丢同属一条元规则：
  **每个语法标记在一个谓语上只能出现一次，而且必须出现一次**

### 57 · date night（约会之夜）
类型 词组 ｜ 旧号 B80
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

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
**点名**："约会"（用【date ＋ 一个名词】说）

- 2026-08-17 ✅ 首次进流
- 2026-08-21 ✅ 复习（点名题面首测）· `for us, going to the cinema feels like date night.`——date night 一字不差 → **连对2，毕业**

- 2026-08-23 📝 c 段 **降为备注，不拆号**：`make an evening of it` 从未测过，也不是她犯的错，
  是迁移时带进来的目标块、频率偏低 ⇒ **不单独建条目**，留作备注：
  make an evening of it ＝ 把一晚上过得像回事（We usually make an evening of it — dinner first, then a film.）
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `date night`

### 58 · it mainly comes down to …（说到底就是……）
类型 词组 ｜ 旧号 B81 ｜ ⭐ 她自产
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

**问题是什么**
**it mainly comes down to …** ＝ 说到底就是……（把一堆原因收成一个点）。
同一格里的邻居（别串）：⛔ boil down to（题面已排除 boil）；
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
"说到底就是钱的问题"（"说到底"用 **come** 那个说法，⛔ 不许用 boil）

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
⇒ 2026-08-20 按【算她对 ＋ 改题面】把题面改成逼 if；**主句放 will 是另一回事**
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
**点名**："设计有问题，你每次走那条路都会堵。"（用 if 说，别用 every time · 当一般规律说，⛔ 不用 will／would）
　　★ 题面 2026-08-20 改：她走 `every time ＋ 现在时` 完全合法，但那样测不到"if 从句里不放 may/will"
　　★ 这一层 ⇒ 按 08-20 新规则【算她对 ＋ 改题面】

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

### 61 · run a red light ／ get stuck in traffic
类型 词组 ｜ 旧号 B84
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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
"闯红灯"

- 2026-08-17 ✅ 首次进流（08-19 回补：迁移时误写"未测过"，📊 08-17 ✅ 里有 B84）
- 2026-08-19 ✅ **自由产出里自发用对**（新题 bank:489）：`if everyone run red lights at will`
  —— 这个块今天没在任何讲评里出现过，是干净的 cold 数据
- 2026-09-10 ⚡ 自评免测 · 复检第 3 组（她原话："9. 10 都直接过"）

### 62 · drive past sth／drive down that road（past 是介词，pass 是动词）
类型 搭配 ｜ 旧号 B85＋B99
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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
- 备注 合并 2026-08-19：#187 并入本条（同一个词组 drive past）。题面取 #187 那句——
  原 #62 的题面"我每次开过那条路都堵。"里的"堵"会串到 #61／#68，弃用

### 64 · forward or back ≠ back and forth（固定词序）
类型 词组 ｜ 旧号 B87
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个也毕业了"）｜ 题型 词组

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
- ⚠️ 拆号待办：标题里"whether 后面要跟主谓"那一半**本题面测不到** ⇒ 付息日另立一条，从 0 起算
  ★ **2026-08-31 c 段结案：已兑现，属陈账。** 见本条上方 08-23 那行 —— 已拆出 **#275
    （whether 后面要跟主谓）**，从 0 起算并进池，条目现存于档案。⛔ 本条的 🎓 与任何数字未动。

### 65 · neither … NOR（不能 neither … or）
类型 语法 ｜ 旧号 B89
状态 连对2 连错0 上次2026-09-05 ｜ 旧账 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

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

### 67 · 可分离动词短语的位置（代词必须放中间：put it away）
类型 结构 ｜ 旧号 B95
状态 连对1 连错0 上次2026-08-21 ｜ **🎓 已毕业 2026-08-21 · 她指定**（"这个也是"）｜ **⛔ 复习组停出**（中译英测不到本条考点，见下）｜ 题型 产出验

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
不出中译英题（题型 产出验 ＋ ⛔ 复习组停出）；挂自由产出抓：put away **it**／turn off **it**／pick up **her** 这种把代词甩到后面的。
★ 原题面（留档，⛔ 不再发题）：**点名**："玩具玩完了就把它们收起来。"（用 put … away 说 —— 考点是"它们"摆在哪儿）
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
- 备注 唯一硬规则：**代词只能放中间** —— put **them** away ✅ ／ put away **them** ✗
  同族：turn it off ／ pick her up ／ throw it away ／ work it out ／ give it back
  名词则两边都行：put the toys away ＝ put away the toys
- 备注 另：away 不变形；玩具搭配是 play with

### 68 · IN/DURING the morning rush hour（早高峰）
类型 搭配 ｜ 旧号 B98＋B96
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-15**（合并后重算）｜ 题型 词组

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

### 69 · pay attention TO sth（同族：listen TO／focus ON／concentrate ON）
类型 搭配 ｜ 旧号 B107b
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 70 · I wouldn't go THAT far, though.（软化自己刚说的话）
类型 词组 ｜ 旧号 B109a
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

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
- 备注 08-11 教练自纠：块本身写错过（go too far → go that far）

### 71 · It's not that A — it's about B.（把矛头从对象转到程度）
类型 词组 ｜ 旧号 B109c
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

**问题是什么**
**It's not that A — it's about B.** ＝ 把矛头从**对象**转到**程度**：
`it's not that the game itself is bad — it's about how long you play.`
同一格里的邻居（别串）：`It's not the game itself; it's how long you play.` 英文没问题、也符合旧题面，
但本条的目标框一次都不出现 ⇒ 2026-09-05 题面补了框限定并排除 It's not the game itself。
判据一句话：起手必须是 **It's not that ＋ 一个完整从句**，后半用 it's about … 接。

**怎么发现的**
旧 B 表迁移（B109c，2026-08-18），原始触发原话未存；最早记录 2026-08-11 📖。
2026-08-12 ✅ ／ 2026-08-16 ✅ ⇒ 2026-08-20 毕业。
2026-09-05 复检第 1 组（打包）✅ `it's not that the game itself is bad - it's about how long to play.` 框整块调出。
2026-09-11 ⚡ 自评免测。

**我错在哪**
她的：2026-08-11 那次"给了答案才会"（📖），触发原话未存；此后没有掉过。
找法：要把话从"这东西不好"转到"多少的问题"时，起手先落 It's not that …，后半接 it's about …。

**题面**
**点名**："不是游戏本身不好，是看玩多久。"（用 **It's not that …** 起手的那个框说，后半自己接；⛔ 不许用 It's not the game itself）

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

### 72 · in moderation（适度）
类型 词组 ｜ 旧号 B109d
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

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
**点名**："适度"（用【in ＋ 一个名词】说）

- 2026-08-11 📖
- 2026-08-17 ✅
- 2026-08-21 ✅ 复习（点名题面首测）· `everything in moderation`——in moderation 一字不差 → **连对2，毕业**
  ★ `Everything in moderation` 本身是英语现成的省略式谚语，不按"悬空片段"判（§7 禁用书面标准评口语）；
    完整版是 `Everything's fine in moderation.`
- 2026-09-05 ✅ 复检组 · 第 4 组（打包）· in moderation

### 73 · stuck WITH ＝ 被迫接受甩不掉
类型 词组 ｜ 旧号 B117c
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-19 · 她指定** ｜ 题型 词组

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
"跟他一组，甩都甩不掉"（"甩不掉"用 **stuck** 说）

- 2026-08-11 📖
- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-15 ❌
- 2026-08-16 ✅
- 2026-08-19 ✅ `every time we got put in pairs, i got stuck with him`
  🎓·她指定（"没错的都赶紧毕业了，不知道回答多少次了"）—— 连对 2 提前出池
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· get stuck with
- 2026-09-07 ✅ 复检 · 第 3 组（打包）· `get stuck with`（介词 with 对）

### 74 · make do with（将就）／整块 I'll have to make do with …
类型 词组 ｜ 旧号 B121＋B171a
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

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

- 备注 合并 2026-08-19：#99（make do with）并入本条 —— 同一个词组，#74 只是多带一个 have to
- 备注 备用题面（原 #99）："没有筷子，我就拿勺子凑合了一下。"

### 75 · other than（除了）≠ rather than（与其/而不是）
类型 搭配 ｜ 旧号 B122
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 词组

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
- 备注 rather than 的两条形态规则在 🎓#245（两边同形）／🎓#246（领独立短语用 -ing），本条只管词义辨析

### 76 · 比较里的泛指不加 the（cheaper than new ones）
类型 语法 ｜ 旧号 B124
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

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

### 77 · 平台用 on，实体店用 at（on Amazon／at Walmart）
类型 搭配 ｜ 旧号 B125
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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

### 78 · a pack of napkins（量词块）
类型 词组 ｜ 旧号 B126
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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
- 备注 本条是捆绑条目（a pack of ＋ the product page），下个付息日按"一条＝一个考点"拆开

### 79 · 名词壳（别用"最重要的是…"这种起手）
类型 减法型 ｜ 旧号 B127
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 整句

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
- 备注 08-17 她指出"拆壳"是术语看不懂，指令已改成大白话

### 80 · than ever 必须紧跟比较级
类型 结构 ｜ 旧号 B128
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-21** ｜ ⚠️ 状态行 08-21 按日志重算（08-20 的 ✅ 当天漏回写）｜ 题型 整句

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
- 备注 中文"比以前…多了"里的"比以前" ＝ **than ever**，且必须**紧跟比较级**：
  more convenient than ever／easier than ever；口语里 easier 比 convenient 常用得多

### 81 · get TO know sb（to 不能省）
类型 搭配 ｜ 旧号 B129
状态 连对2 连错0 上次2026-09-11 ｜ **回潮 2026-08-31**（08-21 毕业 → 08-31 在 R8 重答里再犯 `know new friends`，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-03**（连对2 ＝ 09-01 ＋ 09-03；08-31 回潮后第二次毕业）｜ 题型 词组
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
**点名**："认识陌生人"（"认识"这个**动作**用 get ＋ know 说）

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

### 83 · 形容词不加复数（crucial 不是 crucials）；crucial TO
类型 语法 ｜ 旧号 B131
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

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

### 84 · 条件句别纠结（every time/whenever 在场 → 现在时；说将来 → will）
类型 语法 ｜ 旧号 B132
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 整句

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

### 85 · start / set up a business（不用 create）＋ take on risk
类型 搭配 ｜ 旧号 B135
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-20**（连对2） ｜ **合并条·出题多句覆盖** ｜ 题型 词组

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
"创业"（用动词短语说，不要名词） ／ "承担风险"（"承担"用 **take** 说）

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

### 87 · consider sth（及物，不带 about）
类型 搭配 ｜ 旧号 B139
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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
- 备注 更地道的说法是 take X into account／factor X in（"考虑**进去**"那一层）

### 88 · get on with it（不废话，埋头干下去）
类型 词组 ｜ 旧号 B141
状态 连对2 连错0 上次2026-09-10 ｜ 回潮已断（08-11 曾毕业）｜ **回潮 2026-09-05**（08-21 毕业 → 09-05 复检写成 `go on with it`，get 被 go 顶掉，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-10**（连对2 ＝ 09-09 ⚡ 自评免测 ＋ 09-10 ✅；09-05 回潮后第二次毕业）｜ 题型 词组

**问题是什么**
**get on with it** ＝ 不废话、埋头干下去（催促）。
同一格里的邻居（别串 —— 都合法，全靠题面排除）：
· **go** on with it ＝ 接着往下讲／往下做（让他继续）—— 09-05 就是被它顶掉的
· get moving／get cracking／get going／**get a move on** —— 同样 get 起头、同样"赶紧"
⇒ 题面靠「get 起头 ＋ 一共四个词 ＋ ⛔ 不是 go ＋ ⛔ 不是 get a move on」三层把它框死。
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
**点名**："赶紧干吧"（用 **get** 起头的那个词组说，⛔ 不是 go · ⛔ 不是 get a move on · **一共四个词**）

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
状态 连对2 连错0 上次2026-08-26 ｜ **🎓 已毕业 2026-08-24 · 她指定** ｜ 题型 整句

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

### 92 · 否定别丢（嵌套否定：中文两个否定，英语常是一个肯定句）
类型 语法 ｜ 旧号 B148
状态 连对2 连错0 上次2026-08-19 ｜ 旧账 ｜ **累错 4** ｜ **形态类·不召回** ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 产出验

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


### 95 · be after ＝ 图个（追求想要的东西）
类型 词组 ｜ 旧号 B162
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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
"就想图个清静"（"图"用 **after** 说）

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

### 96 · 否定辖域陷阱（with no overtime and stability 会被读反）
类型 结构 ｜ 旧号 B163
状态 连对1 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个也问了很多很多次了，毕业了"）｜ 旧账 ｜ 题型 整句

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
- 备注 分诊（与 #7 同型）：**上午单句测对、下午在长句里掉** ——
  单句时她会主动拆；句子一长、and 后面跟的是动词时，辖域检查就不跑了
  ⇒ **检查触发**：句子里出现 `not … and …`，把 and 后面那半单独接回否定念一遍
- 备注 解法A 换正面名词（reasonable hours and job security）／解法B 拆两句

### 97 · 关系词 where（先行词是 job/situation/case/kind 这类抽象"场所"）
类型 结构 ｜ 旧号 B164
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

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

### 98 · 并列两边必须同形（语法功能相同 ＋ 可数性/单复数要齐）
类型 结构 ｜ 旧号 B168＋B240
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ **2026-09-07 撤销回潮**（09-05 那次 ❌ 已按 §3.1⑩ 改判为 ✅ —— 它反用了 08-20 明文锁死的判据，是假错；毕业日与连击数字原样不动）｜ 题型 整句

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
- 备注 自测法：把两边分别接回前面那个词念一遍
- 备注 合并 2026-08-19：#151（并列两边可数性/单复数要齐）并入本条 —— 同一条规则的两个面，
  题面保留两句，一句测"功能相同"、一句测"数要齐"

### 100 · look for sth（≠ look up ＝ 查资料）
类型 词组 ｜ 旧号 B171f
状态 连对2 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-25 · 连对2 ＋ 她当场指定**（"不问了，直接毕业"）｜ 题型 词组

**问题是什么**
**look for sth**（找 ＝ **过程**）≠ **look up**（查资料）≠ **find**（找到 ＝ **结果**）。
判据：**find ＝ 找到（结果）／look for ＝ 找（过程）**。中文一个"找"字盖两件事，英语必须分开。
· 补一层（08-23）：**进行时 ＋ find** 只在"正在（一点点）发现"时成立（I'm finding it harder…）；
　"找工作／找房子／找钥匙"这种**过程**一律 look for。
同一格里的邻居（别串）：searching for ／ trying to find 都合法、也都完全绕开考点 ⇒ 题面点名"用 look 打头"。
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
**点名**："在找一份工作"（"在找"用 **look** 打头的那个词组说）
　　★ 题面 2026-08-24 加点名（§6.5 审核项 7）：原题面不点名时 `searching for`／`trying to find`
　　★ 都合法且完全绕开考点，而她两次掉的正是 find ⇒ 必须把 look 逼出来；
　　★ 点 look 不泄答案 —— look for ／ look up 的分辨才是本条考点

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

### 101 · get by（应付得来）
类型 词组 ｜ 旧号 B171g
状态 连对2 连错0 上次2026-09-09 ｜ 题型 词组 ｜ **回潮 2026-09-05**（08-19 毕业 → 09-05 复检答"忘了"，撤销毕业、连对清零。★ 2026-09-07 补：这一判定 09-05 当天写进了 session 却漏了 `append`，回潮同步迟到两天） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
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
"日常应付得来"（用 get 打头的那个词组说）

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

### 102 · without ＝ with no，不能叠（without no ❌）
类型 语法 ｜ 旧号 B173
状态 连对2 连错0 上次2026-09-05 ｜ 旧账 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

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
"我没法一天不看手机。"

- 2026-08-10 ◎
- 2026-08-11 ❌
- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `I can't go a day without wacthing my phone.` —— without ⛔ 未叠否定
  ｜ ⚠️ 顺带：watching my phone → looking at／checking my phone（不落号，⭐ 再犯一次就建号，见 session 顺带②）
  ｜ wacthing → watching（拼写，不算错）

### 103 · 不定式后置修饰，介词默认留在末尾（a box to put these things IN）
类型 结构 ｜ 旧号 B175
状态 连对1 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-23 · 她指定**（"这条毕业"）｜ 旧账 ｜ 题型 词组

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
**点名**："一个装这些东西的盒子"（用 `a box to …` 那种不定式说，不用 for）

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

### 104 · bury yourself in sth（比喻义只配 in，不配 into）
类型 搭配 ｜ 旧号 B181 ｜ ⭐ 她自产
状态 连对2 连错0 上次2026-09-09 ｜ 题型 词组 ｜ **回潮 2026-09-05**（08-20 毕业 → 09-05 复检写成 bury **into**，正是本条守的那个错，撤销毕业、连对清零。★ 2026-09-07 补：这一判定 09-05 当天写进了 session 却漏了 `append`，回潮同步迟到两天） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
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
**点名**："一头扎进语法书里"（"扎进"用 bury 说）

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
- 备注 教练连续两天判 ❌ 却没给理由 ⇒ 她只能背不能学；in 标状态、into 标轨迹

### 105 · "兼顾未来和现在"三说法（keep one eye on the future…）
类型 词组 ｜ 旧号 B186
状态 连对2 连错0 上次2026-09-07 ｜ 旧账 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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
"同时看着未来和当下"（用一个带 **eye** 的说法说）

- 2026-08-10 ❌
- 2026-08-11 ✅
- 2026-08-15 ❌
- 2026-08-16 ❌
- 2026-08-17 ✅（教练当天用表里没写的标准判过她一次，已撤销）
- 2026-08-19 ✅ `Keep one eye on the futher, and one on the present.`（整句块调出来了；futher 是打字滑）
- 2026-09-05 ✅ 复检 · a2 第 2 组（09-05 判定 · 09-07 补记入档）· keep one eye on the future and one on the present
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 2026-09-12 📝 题面整改：「得同时看着未来和当下。」→「同时看着未来和当下」—— 原句无主语却带句号（§6.5 第 6 项 ✗ 例），缩成块、回标词组 · 全档题面 review

### 106 · kind of / sort of / type of ＋ 单数名词，不带冠词
类型 语法 ｜ 旧号 B187
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 107 · jammed / gridlocked（车堵到一动不动）
类型 词汇 ｜ 旧号 B191a
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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
"堵死了，一动不动"（一个形容词）

- 2026-08-11 ✅
- 2026-08-12 ✅（📊 记 B191a／B191b 分号后）
- 2026-08-16 ✅
- 2026-09-07 ✅ 复检 · 第 5 组（打包）· `jammed`（形容词槽位，一个词到位）

### 108 · packed（人多：a packed train）
类型 词汇 ｜ 旧号 B191b
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 109 · enough X to go round（够分）
类型 词组 ｜ 旧号 B192
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

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

### 110 · "没有 X" 的三种说法（口语默认走 I didn't have any…, so…）
类型 结构 ｜ 旧号 B193
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

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

### 113 · "都要/总是"那一层（always end up -ing／have to／it always takes）
类型 结构 ｜ 旧号 B197
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 整句

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

### 114 · It's less about X AND more about Y（配对词是 and，不是 but）
类型 词组 ｜ 旧号 B198 ｜ ⭐ 她自产
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

**问题是什么**
**It's less about X AND more about Y** —— 配对词是 **and**，⛔ 不是 but：
`it is less about the machine itself **and** more about the time spent with kids`。
同一格里的邻居（别串）：not … but … 完全合法（08-17 她答的就是它），但绕开这个块 ⇒ 当天改点名。
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
**点名**："这事儿重点不是机器本身，是陪孩子的时间。"（用 less about … more about … 说一遍）

- 2026-08-12 ✅
- 2026-08-15 ✅
- 2026-08-17 ◎ 她答 not…but… 完全合法 → 改点名
- 2026-08-19 ✅ 点名 · `it is less about the machine itself and more about the time spent with kids`
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `It's less about the machine itself **and** more about the time you spend with your kids.`
  配对词是 and，⛔ 不是 but（⭐ 本条是她自产的块）
- 备注 这个块她在自由产出里已自发用对四次（08-11/13/15/16 四篇 P2 结尾）

### 115 · a couple of ＝ 两个（精确）；"几个"用 a few
类型 词汇 ｜ 旧号 B199
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19**（08-20 的回潮已撤销，见下）｜ 题型 词组

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

### 116 · colourful X（不是 color X）
类型 词汇 ｜ 旧号 B200
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 117 · watch（盯着看一个过程）vs see（看到结果/一瞬间）
类型 词汇 ｜ 旧号 B201
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 118 · 只有…才（ONLY ＋ 动词／It's only … that/when）
类型 结构 ｜ 旧号 B203
状态 连对2 连错0 上次2026-09-09 ｜ 题型 整句 ｜ **回潮 2026-09-05**（08-20 她指定毕业 → 09-05 复检 only 那一层整个没出来，★ 与 08-19 掉的那次逐字相同，撤销毕业、连对清零。★ 2026-09-07 补：这一判定 09-05 当天写进了 session 却漏了 `append`，回潮同步迟到两天） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
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
"只有到现场才有那种感觉。"

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
- 备注 2026-08-19 她问"这条怎么还没毕业，考了十次了吧" ⇒ 查记录只有 **3 次**（08-12 ❌ 08-13 ✅ 08-16 ✅），
  真正的原因是**题面与 #38 撞车**（两条题面几乎同一句、考点却不同）：她每次答中一条，另一条就记不上
  ⇒ 08-19 已把 #38 的题面换掉，两条从此互斥
- 备注 两个落点：① only ＋ 动词　② It's only … that/when …

### 119 · when（一定会发生/每次都这样）vs if（不确定）
类型 语法 ｜ 旧号 B204
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

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
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 122 · 肯定·随便哪个 → any-（Anything's fine.）
类型 语法 ｜ 旧号 B207a
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 123 · 肯定·全部 → every-（Everything's gone up.）
类型 语法 ｜ 旧号 B207b
状态 连对2 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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

### 125 · employer（给工作的）／employee（拿工作的）
类型 词汇 ｜ 旧号 B210
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 126 · get used to ／ settle into（适应新环境）
类型 词组 ｜ 旧号 B211
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 127 · especially 不带来介词：句子本来要什么介词就用什么
类型 结构 ｜ 旧号 B213
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

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
- 备注 她真正的错是"挂空"：介词短语后面另起完整句 ⇒ 悬空。万能式 `This is especially true for…`
- 备注 08-19 她问"省一个 for 可以么" → 可以：前面已有 for everyone，后面省略式母语者常用；
  写成 especially for working people 也对

### 128 · 坐飞机 ＝ fly／be on a plane／take a plane（❌ take the airplane）
类型 搭配 ｜ 旧号 B215
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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

### 129 · staff 是集合名词，没有复数 staffs（the staff ARE friendly）
类型 语法 ｜ 旧号 B216
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21**（08-23 撤销 08-21 的误判后按日志重放补记；她 08-23 也当场指定）｜ 题型 词组

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

### 130 · can 才是默认，be able to 是备用（只在完成时/不定式/情态后才必须换）
类型 语法 ｜ 旧号 B217
状态 连对2 连错0 上次2026-09-05 ｜ **累错 4** ｜ **🎓 已毕业 2026-08-21** ｜ 题型 整句

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

### 131 · go ＝ 在程度轴上移动（go too far／How far are you willing to go?）
类型 词组 ｜ 旧号 B218
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

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
- 备注 同族整块背：go too far ／ go all the way ／ How far would you go? —— far 的搭档永远是 go

### 132 · 环路 ＝ ring road（❌ round road）
类型 词汇 ｜ 旧号 B219
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 133 · this morning / last night（❌ today morning／yesterday night）
类型 搭配 ｜ 旧号 B220
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 词组

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

### 134 · 不是所有动词都要宾语（decide/choose/help/manage/win 能单独站住）
类型 语法 ｜ 旧号 B221
状态 连对2 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

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
- 备注 过度泛化警报：修一处，隔壁被带偏（教练纠了两次"缺宾语"，她给不及物动词也硬加）
- ⚠️ **必须和 #18 一起读**（08-19 判重发现）：#18 是"英文动词必须带宾语"，本条是它的白名单。
  两条不冲突但会互相带偏 ⇒ 判之前先查白名单

### 135 · 中文的"社会/大家/人们"→ 英语常用 there is 或被动吃掉
类型 结构 ｜ 旧号 B222
状态 连对2 连错0 上次2026-09-11 ｜ 题型 整句 ｜ **回潮 2026-09-09**（08-20 毕业 → 09-09 复检答"忘了"：题面当天补上排除项、考位才露出来，there is ／ 被动两条路都没调出来，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-11**（连对2 ＝ 09-10 ✅ ＋ 09-11 ✅；09-09 回潮后第二次毕业）
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
"社会对年轻人期待太高。" ／ "大家都觉得这样不对。"（两句都 ⛔ 不许用 society／everyone／people 当主语）

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

### 136 · tell ＋ 有内容的东西（a joke／a story／the truth）
类型 搭配 ｜ 旧号 B223
状态 连对2 连错0 上次2026-09-10 ｜ 题型 整句 ｜ **回潮 2026-09-07**（08-20 毕业 → 09-07 复检答 `to be honest`，题面已是完整句、主语与"终于"都在，插入语挂不上去 ⇒ 真掉，撤销毕业、连对清零。★ 09-05 那次答的也是 to be honest，但当时题面被粒度整改截断成裸块「说了实话」与 🎓#232 撞车 ⇒ 判 ◎ 作废，⛔ 不计连击）｜ **🎓 已毕业 2026-09-10**（连对2 ＝ 09-09 ⚡ 自评免测 ＋ 09-10 ✅；09-07 回潮后第二次毕业）
**问题是什么**
**tell ＋ 有内容的东西**：a joke ／ a story ／ **the truth** —— `He finally **told the truth**.`
同一格里的邻居（别串）：confess／admit／**come clean** 都合法、都绕开这个搭配 ⇒ 题面把三个都排除；
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
"他终于说了实话。"（⛔ 不许用 confess／admit／come clean）

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

### 137 · know（掌握信息）／tell（分辨得出）／get（听懂，只说 I get it）
类型 词汇 ｜ 旧号 B224
状态 连对2 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20**（新规则：连对2 即毕业）｜ 题型 整句

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

### 138 · a / an 看【读音】不看拼写（an hour／a university）
类型 语法 ｜ 旧号 B225
状态 连对2 连错0 上次2026-08-16 ｜ **形态类·不召回**（2026-08-25 她定）｜ **🎓 已毕业 2026-08-20** ｜ 题型 产出验

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
- 备注 2026-08-25 标 `形态类·不召回`（§3.4）：冠词在 §3.4 的形态类清单里（"单复数/限定词 · 冠词/指称"），
  自我分诊判据也成立 —— 08-13／08-16 两次中译英复习她都答对，08-24 掉的是**自由产出里检查没跑**。
  ⇒ ① **不进中译英复习组**（孤立测她会，信息量为零）
     ② **自由产出里掉了也只记 ⚪**，不记 ❌／不掉毕业（她 2026-08-25 定，见上条日志）
     ③ 教练的动作只剩一个：**点出来 ＋ 复述检查触发**

### 139 · every / each / another / any(单指) 后面永远跟单数
类型 语法 ｜ 旧号 B226＋B115
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-15**（合并后重算）｜ 题型 词组

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
- 备注 合并 2026-08-19：#199（any ＋ 单数 ＝ 任何一个）并入本条 —— 本条是全集
  （every/each/another/any 后面永远跟单数），#199 只是其中的 any 那一格

### 140 · I'd love（现在的意愿）≠ I love（长期喜好）
类型 语法 ｜ 旧号 B227
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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

### 141 · 过去完成时必须有另一个更晚的过去事件当参照
类型 语法 ｜ 旧号 B228
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

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
- 备注 参照词 ✅ before/by the time/when/until/after ｜ ❌ and（并列，同一时间平面）
- 备注 08-13 教练用这条判错一次，她当场推翻（until 本身就是参照点），成立

### 142 · 中文"连…都没/都不" → 否定放助动词上，even 跟在后面
类型 结构 ｜ 旧号 B231
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 整句

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

### 143 · 哪些动词后面要带 to（need to/want to/manage to；情态和 make/let/watch 不带）
类型 语法 ｜ 旧号 B232
状态 连对2 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-24**（08-19 曾毕业 → 08-24 回潮 → 同日两次 ✅ 重新毕业）｜ 题型 整句

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

### 144 · so … that ／ too … to ／ very 的分工（too…that 不存在）
类型 语法 ｜ 旧号 B233
状态 连对1 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这句话不要考了，直接毕业"）｜ 题型 整句

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

### 145 · bring（到我这儿）／take（从这儿到别处）／fetch（去拿了再回来）
类型 词汇 ｜ 旧号 B234
状态 连对3 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19** ｜ 题型 词组

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
**点名**："我是从新闻上知道这事的。" ／ "我后来才发现他早就走了。"（两句里"知道/发现"这个**动作**都不许用 know 说）

- 2026-08-16 ❌
- 2026-08-17 ❌
- 2026-08-19 ✅ 复习 · `I found out about it from the news` ＋ `I found he had gone`（两句都没用 know）
- 2026-08-20 ✅ 复习 · `I found out the thing from the news` ＋ `I only realised later that he'd left`
  ——两句都用动作动词（found out／realised），know 一次没出现 ⇒ 连对2 毕业
  ｜同句 `the thing` 归新建 #260（中文"这事"直译），不算本条头上
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· found out about this ／ realized later
  —— 两句都避开了 know 表"得知"
- 2026-09-07 ⚡ 自评免测 · 复检第 3 组（她逐题写「直接过」）
- 备注 the news 要带 the（on/from/in the news）—— 08-19 她自发带了 the；08-20 仍带对

### 148 · 状态用简单时，变化用完成时（He isn't familiar with it yet.）
类型 语法 ｜ 旧号 B237
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

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

- 备注 08-16 她质疑并修正了教练的过度概括（always 不强制完成时），成立；真正强制的只有 for＋时长／since＋时点

### 149 · 动词后面别多加词（celebrate sth／discuss sth／marry sb／bring sb up）
类型 搭配 ｜ 旧号 B238
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

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

### 153 · work AT（下功夫）／work ON（做某项目）／work IN（领域）；"干这行"＝ I've been doing this
类型 搭配 ｜ 旧号 B242
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

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

### 154 · 法律/政策配的动词不是 happen（came in／was introduced）
类型 搭配 ｜ 旧号 B243
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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

### 155 · as … as 中间只能放原级；few（可数）／little（不可数）
类型 语法 ｜ 旧号 B244
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

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
- 备注 `as less as possible` ❌ —— as…as 本身就是比较结构，里面再放比较级 ＝ 标两遍

### 156 · 同根词：位置决定名词形还是形容词形（the difference／different ways）
类型 语法 ｜ 旧号 B245
状态 连对2 连错0 上次2026-08-30 ｜ **🎓 已毕业 2026-08-23**（连对2 · 08-20 回潮后走完两次）｜ 题型 整句
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
- 备注 08-16 实证：原答案写对，重说时反而退成 different

### 158 · 场所介词 on（面）／in（有边界的空间）；on the balcony／on the bus
类型 搭配 ｜ 旧号 B247
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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

### 159 · "…的时刻/地方/原因 是…" → 表语用 when／where／that 引导
类型 结构 ｜ 旧号 B248
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

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
- 备注 连带：讲过去的事，主句系动词也要过去时（is → was）

### 161 · (the) N of us —— 加 the ＝ 全体，不加 ＝ 一部分
类型 语法 ｜ 旧号 B250
状态 连对2 连错0 上次2026-09-11 ｜ 题型 词组 ｜ **回潮 2026-09-04**（08-19 毕业·零 ❌ 线 → 09-04 新题里写成 `the three of my family`，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-07**（连对2 ＝ 09-05 ＋ 09-07；09-04 回潮后第二次毕业）

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
"我们仨" ／ "我们当中有两个" ／ **"我们一家三口"（也用 the ＋ 数字 ＋ of 说）**

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
- 备注 person 的复数口语一律 people

### 162 · made OF ／ OUT OF ＋ 材料；写画出来的 ＋ IN（written in pencil）
类型 搭配 ｜ 旧号 B251
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这题毕业了"） ｜ **合并条·出题多句覆盖** ｜ 题型 词组

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
"用铅笔写的" ／ "木头做的"

**成员出题账**
① 写／画出来的 ＋ in（written／spelt in） ｜ 08-17 ❌ · 08-19 ✅ · 08-20 ✅ · 09-05 ✅
② 材料 ＋ made of／out of ｜ 08-19 ✅ · 08-20 ✅ · 09-05 ✅
★ 08-17 那一次只测到成员 ①。

- 2026-08-17 ❌ `spelt out OF sweets`（把 spell out 和 made out of 串台）
- 2026-08-19 ✅ `written in pen（该 pencil，但介词对）` ＋ `made of wood`——两个介词都中
- 2026-08-20 ✅ `the letter was written in pencil. the box is made of wood.`——两个介词都对，pencil 也对了
- 2026-09-05 ✅ 复检 · a2 第 3 组（09-05 判定 · 09-07 补记入档）· in pencil（写画出来的用 in）／made of wood（材料用 of）
  —— 两个成员都对

### 163 · "愣住了／说不出话"（I just stood there.／I froze.）
类型 词组 ｜ 旧号 B252
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-20**（连对2）｜ 题型 词组

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
- 备注 08-15 给过、当天重说对了，08-16 再问已经不会 ⇒ "当场重说对 ≠ 装上了"

### 164 · 一句话里时态只能有一个平面
类型 语法 ｜ 旧号 B253
状态 连对2 连错0 上次2026-08-26 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 整句

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
- 备注 与 #12 分工：#12 管"该用哪个时态"，本条管"一句里别换档"

### 165 · even（修饰一个词）／even though（已经发生的事实）
类型 语法 ｜ 旧号 B254
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-19 · 她指定** ｜ 题型 整句

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
- 备注 08-16 当天纠、隔一道题她在全新语境里自发用对 ⇒ 迁移窗口很短但很实

### 166 · see sb（见面）／meet（初次认识）／meet up（约着碰头）—— 选哪个动词
类型 词汇 ｜ 旧号 B255
状态 连对2 连错0 上次2026-09-05 ｜ 顽固已断 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

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
**点名**："上周跟他见了一面" ／ "大学认识的"（两句用**不同的动词**说）

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
- 备注 `hadn't MET FOR LONG` 意思反了；说"很久"这个量一律 for ages／for a long time，
  for long 只在"没持续多久"里出现（I didn't stay for long.）
- 备注 **捆绑条目**（see／meet／meet up ＋ for ages）：08-19 出现"块的一半对一半错" ⇒
  下个付息日按"一条＝一个考点"拆开，否则她要为已经会的 meet 陪着 for ages 一起重测

### 168 · tick things off a list（打卡式旅游）
类型 词组 ｜ 旧号 B257 ｜ ⭐ 她想说卡住、📖 给的
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 词组

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
- 备注 完整块是 tick things off **a list**（清单单数）；并列时 taking a photo and moving on 更齐

### 169 · 不带 if 的条件句：[量/程度短语] ＋ and ＋ [结果]
类型 结构 ｜ 旧号 B258
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-19 · 零 ❌ 线** ｜ 题型 整句

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
- 备注 and 前面只能放比较级或量（ten minutes EARLIER）；would（假设）vs will（真打算）；and 是关节，不能用逗号代替

### 170 · 并列人称在介词后/宾语位置一律用宾格 me
类型 语法 ｜ 旧号 B259
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个也毕业了"）｜ 题型 整句

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
- 备注 建号后隔一题她就用对了（迁移窗口）

### 171 · 要把"跟谁说"说出来就得用 tell sb（say 后面不接人）
类型 搭配 ｜ 新建 2026-08-19
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 词组

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
**点名**："没跟我说一声"（用 tell 说）

- 2026-08-19 新建 · 复习#147 句里 · "也没跟我说他要走" → `didn't say he was going to leave`（漏掉"我"）
- 2026-08-21 ✅ 复习（点名题面首测）· `he didn't tell me before he left.`——tell ＋ 人、语序对、两分句时态平面一致
- 2026-08-23 ✅ 付息日 a 段 · `he didn't tell me before leaving.`——tell ＋ 人一字不差；
  `before leaving` 的分词逻辑主语 ＝ 主句主语 he，挂对了 → **连对2，毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `didn't tell me` —— 要把"跟谁说"说出来就得用 tell sb
- 备注 say 后面直接接人不成立（say me ✗）；要出现人就换 tell sb sth／say sth TO sb

### 172 · 机会用 get：get the chance to do（不用 have a chance）
类型 搭配 ｜ 新建 2026-08-19
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

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
- 备注 have a chance 更多用在"有可能性"（There's a chance it'll rain）；"有机会做某事"默认 get

### 173 · X makes me …（实义动词盖住整个评价槽，不用 is）
类型 结构 ｜ 旧号 B12
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 174 · as … as it gets（用原级避开比较级形态）
类型 词组 ｜ 旧号 B25
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

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
**点名**："简单到不能再简单"（用 **as … as** 那个块说，⛔ 不用比较级）

- 2026-08-12 ❌ 回潮：写成 `as simple as it got`（这个块不随句子变过去式）
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-05 📝 题面整改 · 复检组第 1 组发题前审核（§6.5 第 7 项 · 硬阻断）
  原题面 "跑步简单到不能再简单。" 可以译成 `Running couldn't be simpler.`（合法，比较级）——
  而本条的立身之本正是**用原级避开比较级形态** ⇒ 绕开就测不到。
  ⇒ 点名到 as … as 那个块 ＋ 明写 ⛔ 不用比较级，⛔ 未给出 as simple as it gets。
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· `running is as simple as it gets` 原级，⛔ 没落进比较级
- 备注 边界：as…as it gets ＝"已经是最…的了"，不等于"尽量…"（那是 as…as possible）

### 175 · grow vs grow up（grow up 只用于人长大成人）
类型 词汇 ｜ 旧号 B31a
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

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

### 176 · efficient（省时间人力）vs effective（达到效果）
类型 词汇 ｜ 旧号 B46
状态 连对2 连错0 上次2026-09-09 ｜ 题型 词组 ｜ **回潮 2026-09-05**（08-17 毕业 → 09-05 复检用 works well 绕开形容词槽位，形容词一次没出现，撤销毕业、连对清零） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
**问题是什么**
**efficient（省时间人力）vs effective（达到效果）**：
判据：effective ＝ 达到效果（有没有用）／ efficient ＝ 省时间省人力（快不快、省不省）。
`The drug is pretty **effective**.`
同一格里的邻居（别串）：`works well` 完全合法，但它**绕开形容词槽位** —— 09-05 掉的正是这一点
（不是分不清这一对，是压力下用 works well 躲开了）；题面另排除 useful／helpful。
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
"管用"（形容词，⛔ 不许用 useful／helpful）

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

### 177 · 名词表语（a waste of time／a must／a plus）
类型 结构 ｜ 旧号 B51
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 178 · only／all／最高级后面用 that 不用 which
类型 语法 ｜ 旧号 B64
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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
"那是唯一真正属于你自己的部分。"

- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `That's the only part that truly belongs to you.` —— only 后面用 that，⛔ 没用 which

### 179 · that ＋ 形容词 ＝ "那么…"
类型 语法 ｜ 旧号 B65
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

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
"没那么简单" ／ "其实没那么难"

- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `It's not that simple. It's actually not that hard.` —— that ＋ 形容词，两句都对

### 180 · eat out ＝ 出去下馆子
类型 词组 ｜ 旧号 B72
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

**问题是什么**
**eat out ＝ 出去下馆子**（两个词，⛔ 不绕 go to a restaurant）。
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

### 181 · every time／whenever 引导的从句 → 主句用现在时
类型 语法 ｜ 旧号 B90
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 182 · by ＋ -ing ＝ 通过做某事达成结果
类型 结构 ｜ 旧号 B91
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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

### 183 · save sb money／sth（带间接宾语）
类型 搭配 ｜ 旧号 B92
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-11** ｜ 题型 词组

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

### 184 · every time／each time 是连词，后面跟完整从句
类型 结构 ｜ 旧号 B94
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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
"他每次来都带点吃的。"

- 2026-08-12 ❌
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-17 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `he brings something to eat every time he comes.` —— every time ＋ 完整从句

### 186 · leave a mess（⭐ 她自产）
类型 词组 ｜ 旧号 B97
状态 连对2 连错0 上次2026-09-11 ｜ **回潮 2026-09-09**（08-17 毕业 → 09-09 复检答"忘了"，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-11**（连对2 ＝ 09-10 ✅ ＋ 09-11 ✅；09-09 回潮后第二次毕业）｜ 题型 词组

**问题是什么**
**leave a mess**（⭐ 她自产的块，三个词）＝ 东西乱丢一地。
同一格里的邻居（别串 —— 都合法、全靠题面排除）：
`He **makes** a mess.` · `He **throws** stuff around.` · `leave stuff lying around` · everywhere／all over
⇒ 题面靠「三个词的块 ＋ ⛔ everywhere／all over／make／throw」把 leave a mess 框死
　（⛔ 未点名 leave、⛔ 未点名 mess —— 那是考点本身）。
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
"东西乱丢一地"（用**三个词**的块说 · ⛔ 不许用 everywhere／all over／make／throw）

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

### 189 · take sb out ≠ bring sb along；outdoors 是副词
类型 词汇 ｜ 旧号 B101
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 190 · clear the table ≠ clean the table
类型 词汇 ｜ 旧号 B103
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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
"把桌上收拾了"

- 2026-08-09 ❌
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· clear（⛔ 没落进 clean）

### 191 · 集合名词单复数都合法（family／audience／team）
类型 语法 ｜ 旧号 B104＋B93
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-11** ｜ 题型 整句

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
"我们家过年会做一整天的菜。"

- 2026-08-09 ✅
- 2026-08-10 ✅
- 2026-08-11 ✅
- 2026-08-17 ◎（原 #66，题面撞车作废）
- 2026-08-19 ◎（原 #66）她答 `all the audience laugh` —— **按本条是对的**（英式复数成立，美式偏单数）
- 2026-09-05 ✅ 复检组 · 第 4 组 · `My family **spend** a whole day cooking a big meal.`（集合名词配复数谓语，合法的那一边）
- 备注 合并 2026-08-19：#66（audience 作整体时配单数动词）并入本条 ——
  #66 是一条**写错了的绝对化规则**，与本条直接矛盾，已撤销
- 备注 与 #129（staff 没有复数形式 staffs）不冲突：那条管**词形**，本条管**动词一致**

### 192 · make sb ＋ 形容词（cause 不能这么用）
类型 搭配 ｜ 旧号 B106
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 193 · lose interest IN sth（介词是 in）
类型 搭配 ｜ 旧号 B107a
状态 连对2 连错0 上次2026-09-09 ｜ 题型 词组 ｜ **回潮 2026-09-05**（08-17 毕业 → 09-05 复检写成 lose interest **to**，她自己标注"这个介词不确定"，撤销毕业、连对清零） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
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
"对学业失去兴趣"（用 **interest** 说）

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

### 194 · screen time（⭐ 她自产）；balance A and／with B
类型 搭配 ｜ 旧号 B108
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 195 · An hour a day is completely fine.（给具体量当让步）
类型 结构 ｜ 旧号 B109b
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 196 · singular they（someone → they／their）
类型 语法 ｜ 旧号 B110
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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
"喜欢拍照的人，Photoshop 是他们的最爱。"（主语用 **someone** 起头说，后面的代词跟着它走）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `For **someone** who … **their** favourite` —— singular they 命中
  ｜ ⚪ `Photoshop are` → is（主谓一致，归 #10 形态类）：同场 [4] 的 `screen time makes` 就是对的

### 197 · addictive ≠ interesting
类型 词汇 ｜ 旧号 B112
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15**（08-20 的回潮已撤销，见下）｜ 题型 词组

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
"上瘾"（形容词）
　　★ 题面 2026-08-20 改：原题面"游戏太上瘾，有的孩子一天不出门。"与 #144 的题面撞车，两条互相盖

- 2026-08-09 ❌
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-08-19 📝 拼成 `additive`（判打字滑，未建号、未记档位）
- 2026-08-20 ⛔ 教练一度按"同词反复错拼"记 ❌ 并让本条回潮 —— **当天她裁决后撤销**：
  「单词打错不算错（除非我主动说需要记录）」⇒ 本条恢复 🎓，08-20 不计任何档位
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· addictive

### 198 · the 的唯一功能 ＝ 双方都知道是哪一个
类型 语法 ｜ 旧号 B113
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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
"就两类，好玩的和有用的。"（两类各用一个名词短语说，⛔ 不许只说 fun and useful）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `**the** funny ones and **the** useful ones` —— 冠词两边都带上了
  ｜ ⚪ `Two kind of things` → kinds ｜ ⚠️ funny → **fun**（好玩的 ＝ fun／搞笑的 ＝ funny），⛔ 未落号，交回她判
- 2026-09-12 📝 题面整改：点名「冠词是考点…」→「两类各用一个名词短语说，⛔ 不许只说 fun and useful」（§10 禁令 5 禁预告测试点；与 #231 同句同改，两条各判各的格：本条判 the、#231 判 ones）· 全档题面 review
- 备注 与 #231（the fun ONES）共用这句中文 —— 两条都已毕业，若回潮需先把题面改成互斥

### 200 · think FOR oneself ≠ by oneself
类型 搭配 ｜ 旧号 B116
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 201 · "全信" ＝ trust it completely／take its word for it
类型 词组 ｜ 旧号 B118
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 202 · 副词修饰动作：speak English well（不是 speak good）
类型 语法 ｜ 旧号 B119
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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
"英语说得挺好"

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `speak English pretty **well**`（⛔ 没写 good）

### 203 · …, though.（挂句尾，唯一不用提前预判的转折标记）
类型 结构 ｜ 旧号 B120
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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

### 204 · 中文无主语句 → 先想被动或 they
类型 结构 ｜ 旧号 B123
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 205 · the market／the economy 这类系统性名词带 the
类型 语法 ｜ 旧号 B133
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 206 · 书面词降级（有口语版就用口语版）
类型 减法型 ｜ 旧号 B136
状态 连对2 连错0 上次2026-08-25 ｜ `⛔ 复习组停出` ｜ **🎓 已毕业 2026-08-24**（08-17 曾毕业 → 08-23 回潮 → 08-24 两篇自由产出连过）｜ 题型 产出验

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
状态 连对3 连错0 上次2026-09-05 ｜ ⛔ 复习组停出 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 产出验

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
不出中译英题（题型 产出验 ＋ ⛔ 复习组停出 · ⛔ 条目内容待补）；挂自由产出抓：抛观点时有没有用 I'd say 起头。
★ 原题面（留档，内容补回来之前 ⛔ 不发题）："我觉得主要就是……"（用 **I'd say** 起头说）

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ◎ 复检组 · 第 5 组（打包）· **题面不可执行，本次作废**（⛔ 不动连击）
  她的原话："我不懂 4 种说法什么意思"。
  ★ 查证属实：题面写着「（四种说法各说一次）」，而**那四种说法在档案里根本不存在** ——
    本条正文只有标题，**零判据块**，四条路径一个字都没有 ⇒ 任何人都答不出来。
  ⇒ 题面已改成只考 I'd say；元信息标 `⛔ 条目内容待补`，状态行加 `⛔ 复习组停出`，
    内容补回来之前不再出题。

### 208 · some people ≠ somebody
类型 词汇 ｜ 旧号 B142
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 209 · 形容词顺序（口语版）
类型 结构 ｜ 旧号 B143
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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
"一个线上的养宠物的群"

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组 · `an online pet group`（形容词顺序）｜ gourp 是拼写，⛔ 不算错
  ★ 她当场点评本条："反而这个才应该是词组" —— **她说得对**，本条正是粒度合格的样子。

### 210 · there was A PROMOTION（要名词，不能塞形容词/动词）
类型 结构 ｜ 旧号 B145
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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

### 212 · 压缩出来的形容词两个出口（表语最省）
类型 结构 ｜ 旧号 B149
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

**问题是什么**
**压缩出来的形容词两个出口，表语最省**：把中文"…得…不…"这种程度补语压成**一个形容词**放表语位 ——
主语 ＋ be ＋ 一个形容词（`the road is … **jammed**`）。
同一格里的邻居（别串）：⚠️ 修饰形容词要用副词形（`complete jammed` → **completely** jammed，归 🎓#202 同族）。
⚠️ 与 🎓#107（jammed／gridlocked）互斥写死（2026-09-05 c 段裁决）：
　**堵车那个形容词 ⇒ #107（词汇）／ 把"…得…不…"压成表语形容词 ⇒ 本条（结构）。**
　沿革：本条题面撞过两次（先撞 #108 packed、再撞 #107），现已换成"他气得说不出话。"
判据一句话：中文那一长串补语能不能压成一个形容词？能就放到 be 后面。

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
- 备注 原题面还有"地铁里人挤人"，与 #108（packed）撞车 ⇒ 本条只留"路上堵得一动不动"

### 213 · 功能上线 ＝ go live／be released
类型 词组 ｜ 旧号 B150
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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
"这个功能上线"

- 2026-08-09 ❌
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-01 📝 新题 P3（bank:490）· 自发命中留痕（🎓 冻结，只留痕、不推进数字）
  `because the developer **released** a wrong version.` —— "上线/发版"这个动作的动词选对。
  ★ 同句里另有 ❌（`login in`，新建 #316）与 ⚪（`a wrong` → `the wrong`，归本档 #63），
    三处各归各号（§3.3 标记打在条目上，不打在整句上）。
- 2026-09-05 ✅ 复检组 · 第 1 组（打包）· be released

### 214 · 完成进行时 ＝ have been ＋ -ing
类型 语法 ｜ 旧号 B151
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-11** ｜ 题型 整句

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

### 215 · -ing 短语省主语的硬条件（逻辑主语＝主句主语）
类型 结构 ｜ 旧号 B153
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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

### 216 · 东西不会自己 leave（His things ARE all over the floor）
类型 结构 ｜ 旧号 B154
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 217 · and 接第二个谓语时，否定必须带助动词
类型 语法 ｜ 旧号 B155
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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
"有人闯红灯还不用罚款。"（用 **and** 连两个谓语说）

- 2026-08-09 ◎ 题面没逼出
- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 📝 题面补点名「用 and 连两个谓语说」：原题面可合法译成 without being fined，
  只剩一个谓语 ⇒ 考点（and 接第二个谓语时否定必须带助动词）没有落点。
- 2026-09-07 ✅ 复检 · 第 5 组 · `Someone ran a red light and didn't get fined.`
  —— and 接第二个谓语时否定带住了助动词（**didn't** get fined），⛔ 没写成 and not get fined
  ｜ ⚠️ Someone ran → Some people run（中文"还不用罚款"说的是常态，不是一次具体事件）；考点不受影响

### 218 · working people；traffic management 不带 the
类型 语法 ｜ 旧号 B156
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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
"上班族最需要这个。" ／ "交通管理主要看两件事。"

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 ✅ 复检 · 第 5 组 · `working people.` ／ `traffic management mainly comes down to two things.`
  —— 两处泛指都是裸的（⛔ 无 the）；comes down to 是很地道的选择
- 2026-09-12 📝 题面整改：「上班族」→「上班族最需要这个。」—— 两句统一成整句题（§6.0 一条一种形式；"不带 the"这一格只在句子里才现形，裸词组谁都不会加 the）· 全档题面 review

### 219 · 口语选词 complicated／takeaway
类型 词汇 ｜ 旧号 B158
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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
"太复杂了"（形容词，⛔ 不用 complex） ／ "点个外卖"

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `too complicated`（⛔ 没用 complex）／`order takeaway`

### 220 · actually 的位置
类型 结构 ｜ 旧号 B159
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 221 · 肯定句里的 much → a lot of
类型 语法 ｜ 旧号 B161a
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 222 · 肯定句里的 for long → a long time
类型 语法 ｜ 旧号 B161b
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 223 · 肯定句里的 far → a long way
类型 语法 ｜ 旧号 B161c
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 224 · discrimination AGAINST sb；age discrimination 不可数
类型 搭配 ｜ 旧号 B165
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

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

### 225 · 限定 ≠ 定指（她自己抓到的区别）
类型 语法 ｜ 旧号 B166
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 整句

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

### 226 · 关系代词做宾语可省、做主语不可省
类型 结构 ｜ 旧号 B169
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 227 · clear ≠ clean（形容词层面）
类型 词汇 ｜ 旧号 B170
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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
"空气干净。" ／ "天很晴。"

- 2026-08-09 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-05 ✅ 复检组 · 第 5 组（打包）· `air is **clean**` ／ `it's **clear**`（形容词层面的分工）

### 228 · look after sb（照顾）
类型 词组 ｜ 旧号 B171d
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

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

### 229 · complain 不及物（complaining about it）
类型 搭配 ｜ 旧号 B172
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 230 · "什么样的" ＝ what kind of；"适合住" ＝ good to live in
类型 结构 ｜ 旧号 B174
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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
"什么样的城市适合住？"（⛔ 不许用 What makes … 起头）

- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 📝 题面补「⛔ 不许用 What makes … 起头」：What makes a city a good place to live? 完全合法，
  但 what kind of 与 good to live in 两个考位一个都不出现。排除它不泄露任何一个考位。
- 2026-09-07 ✅ 复检 · 第 5 组 · `What kind of city is good to live in.`（what kind of ＋ good to live **in**，介词没丢）

### 231 · 说"两类/三类"时每类要用复数（the fun ONES）
类型 语法 ｜ 旧号 B176
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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
"就两类，好玩的和有用的。"（两类各用一个名词短语说，⛔ 不许只说 fun and useful）

- 2026-08-10 ✅
- 2026-08-13 ✅
- 2026-08-15 ✅
- 2026-09-07 ✅ 复检 · 第 5 组 · `Just two kinds: fun ones and useful ones.`（两类各自都用复数 ones）
- 2026-09-12 📝 题面整改：点名「单复数是考点…」→「两类各用一个名词短语说，⛔ 不许只说 fun and useful」（§10 禁令 5 禁预告测试点；与 #198 同句同改，本条判 ones、#198 判 the）· 全档题面 review
- 备注 与 #198（the 的唯一功能）共用这句中文，回潮时先改成互斥题面

### 232 · to be HONEST（不是 honesty）
类型 词组 ｜ 旧号 B177
状态 连对3 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 233 · either way ＋ you might as well
类型 词组 ｜ 旧号 B178
状态 连对2 连错0 上次2026-09-09 ｜ 题型 词组 ｜ **回潮 2026-09-05**（08-15 毕业 → 09-05 复检把 might as well 拆成 might … as well，撤销毕业、连对清零） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
**问题是什么**
两个块：**either way**（横竖都一样）＋ **you might as well**（那还不如）。
· 本条真正的考位是 **might as well 的内部词序** —— **as well 必须在动词前**
　（09-05 她写成 `might smile as well`，as well 退回本义"也"，"那还不如"整层丢失）
同一格里的邻居（别串）：整句意译 `Either way it's a day, so just smile.` 完全合法，
但两个目标块一个都不出现 ⇒ 题面点名（2026-09-12 起只给首字母与词数，⛔ 不再把块整个交出去）。
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
**点名**："横竖都一样"（两个词 · **e** 开头） ／ "那还不如笑笑"（"还不如"用 **might** 起头的三词块说 · ⛔ 不许用 better／rather）

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

### 234 · older people／the elderly
类型 词汇 ｜ 旧号 B179
状态 连对2 连错0 上次2026-09-09 ｜ 题型 词组 ｜ **回潮 2026-09-05**（08-15 毕业 → 09-05 复检答"忘了"，撤销毕业、连对清零；★ 09-03 自由产出里刚有过自发命中留痕 ⇒ 认得出 ≠ 产得出） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
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

### 235 · All you need to do is ＋ 原形
类型 结构 ｜ 旧号 B180
状态 连对3 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 整句

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

### 236 · 说人的目的用不定式 to do；for ＋ -ing 是物品用途
类型 结构 ｜ 旧号 B182
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-29**（连对2 · 回潮后走完两次）｜ **回潮 2026-08-27**（08-15 毕业 → 08-27 首犯 → 08-28 拿回第一次 → 08-29 换句复测拿回第二次）｜ 题型 整句

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
"学语言就是为了表达自己、听懂别人。"（"为了"那一格 ⛔ 不许用 about／so that） ／ **点名**："过年给了大家一个聚在一起的**理由**。"（"理由"后面那个动词用**不定式**挂上去）
　　★ 题面 2026-08-27 加第二句（回潮当天补）：原题面只测**状语位**的"为了做某事"，
　　★ 测不到她今天掉的那一格 —— **名词后面挂目的**（a reason ___ bring…）。补一句专测它
　　★ 题面 2026-08-29 换句（旧稿"过年**更多的是**给全家一个聚一聚的理由"与 #306 的题面共用"更多的是"这个触发短语 ＝ §6.5 ⑧撞车；且与 08-28 一字不差重出 ＝ 测的是昨天的记忆不是规则。新句仍打在同一格上：**名词 ＋ to do**（a reason to get together））

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

### 237 · a mixed bag（⭐ 她自产）
类型 词组 ｜ 旧号 B183
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-15** ｜ 题型 词组

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

### 238 · move on ≠ move forward
类型 词汇 ｜ **合并条·出题多句覆盖**（§3.2c，2026-09-07 定：只出一句测不到这一对的分工）｜ 旧号 B184
状态 连对2 连错0 上次2026-09-10 ｜ 题型 整句 ｜ **合并条·出题多句覆盖** ｜ **回潮 2026-09-07**（08-15 毕业 → 09-07 复检两个成员只到一个：只给了 move forward，move on 没出来，撤销毕业、连对清零。★ 08-10／08-13／08-15 那三次 ✅ 是在旧题面下拿到的，而旧题面 move on／move forward 两个都套得上 ⇒ 那三次证明不了她分得清；今天是新题面第一次上场）｜ **🎓 已毕业 2026-09-10**（连对2 ＝ 09-09 ⚡ 自评免测 ＋ 09-10 ✅ 两个成员都到；09-07 回潮后第二次毕业，且是**新题面下**第一次走完连对2）
**问题是什么**
**move on ≠ move forward** —— 一道题面两个成员，本条考的就是这两个块的分工：
· **move on** ＝ 翻篇、别老想着了（`It's in the past, just **move on**.`）
· **move forward** ＝ 继续往前推进（`the company has to keep **moving forward**.`）
同一格里的邻居（别串）：`move ahead` 同样是 move 起头、同样地道，但成员 ② 的目标形式必须是 move forward
⇒ 2026-09-10 题面 ② 补了 ⛔ ahead。
判据一句话：放下过去 ⇒ move **on**；事情继续推进 ⇒ move **forward**。
★ 08-10／08-13／08-15 那三次 ✅ 是在旧题面（"一直往前走"）下拿到的，**两个块都套得上** ⇒ 证明不了她分得清。

**怎么发现的**
旧 B 表迁移（B184，2026-08-18），原始触发原话未存；最早记录 2026-08-10 ✅（旧题面下的三次 ✅ ＝ 白测）。
2026-09-07 📝 题面整改 ＋ 转合并条；同日 ❌ 复检第 5 组（加练）· 两个成员只到一个 ——
只给了 `move forward`，第 ① 句要的 **move on** 没出来 ⇒ **回潮**（新题面第一次上场就抓到了这一格）。
2026-09-09 ⚡ 自评免测 ／ 2026-09-10 ✅ 两个成员都到 ⇒ 连对 2，第二次毕业（**新题面下**第一次走完连对 2）。

**我错在哪**
她的：2026-09-07 复检只给出 `move forward`，`move on` 一次没出现
正确：`① Just move on. ② The company still has to move forward.`
找法：先分一刀 —— 放下过去用 move **on**，事情往前推进用 move **forward**。

**题面**
★ 2 句，两个成员各一句 —— 本条考的就是这两个块的分工，只出一个等于没测
　① "都过去了，别老想着了。"（用 **move** 说）
　② "不管出什么事，公司还是得往前推进。"（用 **move** 说 · ⛔ 不许用 ahead）
　　★ 2026-09-07 题面整改（§6「题面必须唯一可判」）：原题面只有一句
　　★ "一直往前走"（用 move 说）—— move on 和 move forward **两个都套得上**，
　　★ 而本条的考点恰恰是这两个的分工 ⇒ 原题面结构上测不到自己的考点。

**成员出题账**
① move on ｜ 09-07 ❌ · 09-10 ✅
② move forward ｜ 09-07 ✅ · 09-10 ✅
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

### 239 · miss out on sth
类型 词组 ｜ 旧号 B185
状态 连对2 连错0 上次2026-09-10 ｜ 题型 词组 ｜ **回潮 2026-09-07**（08-15 毕业 → 09-07 复检写成 `miss something like friendship`，**out on 整个丢了**，撤销毕业、连对清零）｜ **🎓 已毕业 2026-09-10**（连对2 ＝ 09-09 ⚡ 自评免测 ＋ 09-10 ✅；09-07 回潮后第二次毕业）
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
"错过友情这类东西"（用 **miss** 说）

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

### 240 · keep an eye ON sth
类型 搭配 ｜ 旧号 B189
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

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

### 241 · half 放在冠词前面（half an hour）
类型 语法 ｜ 旧号 B196
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

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

### 242 · 介词＋抽象名词的方式块（in moderation／on purpose）
类型 词组 ｜ 旧号 B208
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

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

### 243 · 形容词 ＋ 固定介词整块记（familiar WITH／interested IN）
类型 搭配 ｜ 旧号 B212
状态 连对3 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17** ｜ 题型 词组

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

### 244 · sing along
类型 词组 ｜ 旧号 B57a
状态 连对1 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-11（08-17 复查通过）** ｜ 题型 词组

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

### 245 · rather than 两边同形（helps…rather than replaces）
类型 结构 ｜ 旧号 B114a
状态 连对1 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-11（08-17 复查通过）** ｜ 题型 整句

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

### 246 · rather than 领独立短语时用 -ing
类型 结构 ｜ 旧号 B114b
状态 连对1 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-11（08-17 复查通过）** ｜ 题型 整句

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

### 247 · stuck IN ＝ 被困在环境/容器里
类型 搭配 ｜ 旧号 B117a
状态 连对1 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-11（08-17 复查通过）** ｜ 题型 词组

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

### 248 · stuck ON ＝ 卡在具体的点上
类型 搭配 ｜ 旧号 B117b
状态 连对2 连错0 上次2026-09-05 ｜ 回潮已断（08-20 回潮）｜ **🎓 已毕业 2026-08-23** ｜ 题型 词组

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
**点名**："在第三题上卡住了"（用 stuck 说）

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
- 备注 三条一族，判据放在一起记：stuck **ON** ＝ 卡在具体的点上（a problem／question 3）｜
  stuck **WITH** ＝ 被迫接受甩不掉（🎓#73）｜ stuck **IN** ＝ 被困在环境/容器里（🎓#247）

### 249 · 原形＝过去式的一小撮动词（put／cut／hit／let／cost）
类型 语法 ｜ 旧号 B152a
状态 连对1 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-11（08-17 复查通过）** ｜ 题型 整句

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

### 250 · that far vs too far（有没有"刚才那句话"可指）
类型 词组 ｜ 旧号 B229
状态 连对0 连错0 上次2026-09-09 ｜ **🎓 已毕业 2026-08-17 · 她指定**（"这句毕业了，别问了"）｜ 题型 整句

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
"别太过分了。" ／ （对方说完一句极端的话）"我倒不至于这么说。"（两句都用 **far** 说）

- 2026-08-17 📝 🎓·她指定
- 2026-09-09 📝 状态行从旧账写法 `状态 —` 补成三个字段（连对/连错冻结在毕业日 ＝ 0/0，因为她指定毕业时从没数过连击）
  —— 09-09 复检第一次真测到它，`append` 要写「上次」而旧写法没有这个字段 ⇒ 自查报错、整批回滚（§3.1③ 允许旧账，但一旦被测就得补齐）
- 2026-09-09 ✅ 复检 · 第 4 组 · `don't go too far.` ／ `I wouldn't go that far.` —— too far 与 that far 分工对

### 251 · cost ＋ 钱／take ＋ 时间／spend ＋ 人做主语
类型 搭配 ｜ 旧号 B230
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-17**（记录里明确判定毕业）｜ 题型 整句

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
"做一顿饭要两小时。"

- 2026-08-15 ❌
- 2026-08-16 ✅
- 2026-08-17 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `it takes two hours to cook a meal.` —— take ＋ 时间
- 备注 2026-08-19 她在自由句里写 `it just takes/costs ten minutes`（两个都列出来）——
  首选 takes 是对的，不记回潮；但 **cost 只配钱** 这条边界还没固化，再出现一次就按回潮处理

### 252 · 三个 no 堆反差 ＋ 收一个 yes
类型 结构 ｜ 旧号 B28
状态 连对0 连错0 上次— ｜ **⛔ 复习组停出** ｜ **🎓 已毕业 2026-08-09 · 旧账（08-09 之前，事件流无记录）** ｜ 题型 产出验

- 旧账 事件流无记录；08-09 前已毕业

**问题是什么**
**三个 no 堆反差 ＋ 收一个 yes** —— 先连着说三个"没有…"，最后收一个肯定的落点。
判据一句话：要立"在家更好"这类观点时，先用三个否定把对面拆掉，再给一个正面的收口。
★ 本条 `⛔ 复习组停出` ⇒ 只在自由产出里看她用不用得上这个结构。

**怎么发现的**
旧账：**2026-08-09 之前已毕业，事件流无记录**（旧 B 表 B28，2026-08-18 迁入），触发原话未存。

**我错在哪**
她的：旧账条目，档案里没有任何判定记录，触发原话未存。
找法：说"为什么喜欢在家…"时，先连甩三个"没有…"，最后补一句肯定的收口。

**题面**
不出中译英题（题型 产出验 ＋ ⛔ 复习组停出）；挂自由产出抓：立观点时有没有"三个 no ＋ 一个 yes"这个结构。
★ 原题面（留档，⛔ 不再发题）：【回答这个问题】"为什么有人喜欢在家看电影/跑步？"（答里先连着说三个"没有…"，最后收一个肯定的）

### 253 · 禁 it ＋ I 当逃避载体
类型 减法型 ｜ 旧号 B5
状态 连对0 连错0 上次— ｜ **⛔ 复习组停出** ｜ **🎓 已毕业 2026-08-09 · 旧账（08-09 之前，事件流无记录）** ｜ 题型 产出验

- 旧账 事件流无记录；08-09 前已毕业

**问题是什么**
**禁 it ＋ I 当逃避载体** —— 类型"减法型"：不许拿 it／I 当万能主语顶掉具体内容。
同一格里的邻居（别串）：🎓#135（用 there is ／ 被动吃掉"社会／大家"）是同一个动作的另一条出口。
判据一句话：这个主语能不能换成一个**具体的东西或人**？能就别让 it／I 顶上。
★ 本条 `⛔ 复习组停出` ⇒ 只在自由产出里扫。

**怎么发现的**
旧账：**2026-08-09 之前已毕业，事件流无记录**（旧 B 表 B5，2026-08-18 迁入），触发原话未存。

**我错在哪**
她的：旧账条目，档案里没有任何判定记录，触发原话未存。
找法：开口前先找一个具体主语 —— 找得到就别让 it／I 顶上。

**题面**
不出中译英题（题型 产出验 ＋ ⛔ 复习组停出）；挂自由产出抓：一段里 it／I 当主语顶掉了具体内容。
★ 原题面（留档，⛔ 不再发题）："任给一个话题，说 2 句，一个 it、一个 I 都不许出现。"

### 254 · 主语位置的动词必须变成 -ing（Putting things back makes…）
类型 语法 ｜ 新建 2026-08-19
状态 连对2 连错0 上次2026-08-23 ｜ **形态类·不召回**（2026-08-25 她定）｜ **🎓 已毕业 2026-08-23** ｜ 题型 产出验

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

### 255 · vital（至关重要）≠ virtual（虚拟的）
类型 词汇 ｜ 新建 2026-08-19
状态 连对1 连错0 上次2026-09-07 ｜ **🎓 已毕业 2026-08-20 · 她指定**（"这个也毕业了"）｜ 题型 词组

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

### 256 · even if ＝ 还没发生的假设（"就算…"）
类型 语法 ｜ 新建 2026-08-19（从 #165 拆出）
状态 连对2 连错0 上次2026-09-05 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 整句

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
**点名**："就算下雨我也去。"（"就算"用 even ＋ 一个词说）

- 2026-08-19 ❌ 首犯 · `Even though it is rainy, I will go`——把假设写成了事实
- 2026-08-20 ✅ 复习 · `even if it rains, I will go`——even if ＋ 一般现在时，选对了场合
- 2026-08-21 ✅ 复习（点名题面首测）· `Even if it rains, I'll go`——even if ＋ 一般现在时 ＋ 主句 will
  → **连对2，毕业**（08-19 那次写成 Even though ＝ 把假设写成事实，这次分清了）
- 2026-09-05 ✅ 复检组 · 第 4 组 · `Even **if** it rains, I will go.`（还没发生的假设）
- 备注 她当天问"要用虚拟语气么" → **不用**：even if ＋ 一般现在时（Even if it rains, I'll go）；
  虚拟只在"跟事实相反"时上（Even if it were sunny, I'd still stay in ＝ 其实是阴天）。
  同日第 4 题她的 `if it were a bit more expensive` 正是正确的虚拟用法 ⇒ **两种都会，只是选错场合**

### 257 · 以身作则 ＝ lead by example／practise what you preach
类型 词组 ｜ 新建 2026-08-19
状态 连对2 连错0 上次2026-09-09 ｜ 题型 词组 ｜ **回潮 2026-09-05**（08-21 毕业 → 09-05 复检写成 `lead by yourself`，by 后面塞了人，撤销毕业、连对清零） ｜ **🎓 已毕业 2026-09-09**（连对2 ＝ 09-07 ✅ ＋ 09-09 ⚡ 自评免测）
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
**点名**："以身作则"（用 lead 说）

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
- 备注 来源有意思：这个块是同日第 9 组讲 explain yourself 时顺带列的同族（behave/enjoy/help yourself），
  她当场抓来用了 ⇒ **迁移意识对，但块的使用对象没跟着记** —— 以后给同族清单时要连"对谁用"一起给

### 258 · at will（书面）→ whenever they feel like it
类型 词组 ｜ 新建 2026-08-19（她指定要学）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-21** ｜ 题型 词组

**问题是什么**
**at will** 是书面词，口语版是 **whenever they feel like it**（"想什么时候…就什么时候…"）。
同一格里的邻居（别串 —— 同一条「书面 → 口语」降级规则下的别的词对，本条只管 at will 这一对）：
in order to → to · utilize → use · numerous → a lot of · purchase → buy · commence → start
判据一句话：这个词我是在书上见的还是在嘴上说的？书面 ⇒ 换成 whenever sb feel(s) like it。
★ 与 🎓#206（书面词降级·减法型，挂自由产出抓）的分工：#206 是**总规则**（只在自由产出里判），
　本条是**一个具体的词对**（可以出中译英题）⇒ 两条各走各的。

**怎么发现的**
2026-08-19 新建 · 自由产出（新题 bank:489）· 她写 `if everyone ran red lights **at will**`
—— 语法没错，是**她指定要学**的降级（§2③），教练给的口语版是 whenever they feel like it。
判重：与 🎓#206（书面词降级总规则）比对 —— #206 只在自由产出里判、管的是整条规则，
本条是一个具体词对、可以出中译英题 ⇒ 不重复，**判重通过**（见下方备注）。

**我错在哪**
她的：`if everyone ran red lights **at will**`　　正确：`if everyone ran red lights **whenever they felt like it**`
找法：一个词要出口之前先问 —— 这是我在书上见的，还是嘴上说的？书上见的 ⇒ 换口语版。

**题面**
**点名**："想什么时候来就什么时候来"（用 feel like 说一遍）

- 2026-08-19 新建 · 自由产出（新题 bank:489）· 她写 `if everyone ran red lights **at will**`
  ⇒ 语法没错，但 at will 是书面词，口语版是 **whenever they feel like it**
- 2026-08-20 ✅ 复习（新建后首测）· `He comes here whenever he feels like it.`——目标块一字不差
  ｜附带 feels 的第三人称 -s 也带上了
- 2026-08-21 ✅ 复习 · `he comes here whenever he feels like it.`——一字不差，feels 的 -s 也对
  → **连对2，毕业**
- 2026-09-11 ✅ 复检 · 付息日 a2 第 3 组 · `You can come whenever you feel like it`
- 备注 整句范例（她指定要背的那句）：
  **Parents can show kids how jammed the roads would get if everyone ran red lights whenever they felt like it.**
  —— 注意 felt 跟着虚拟条件走（主句 would get ⇒ 从句 ran／felt 都是过去式形态）
- 备注 同族降级（口语版在右边）：at will → whenever they feel like it ｜ in order to → to ｜
  utilize → use ｜ numerous → a lot of ｜ purchase → buy ｜ commence → start
- 备注 与 🎓#206（书面词降级·减法型，挂自由产出抓）的分工：#206 是**总规则**（只在自由产出里判），
  本条是**一个具体的词对**（可以出中译英题）⇒ 不重复，判重通过

### 259 · 完成时：have/has/had 之后一律用【过去分词】（I've never BEEN able to）
类型 语法 ｜ 新建 2026-08-20
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

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
- ⚠️ **必须和 #147 一起读，两条互斥**（同 #18／#134 那一对的教训）：
  **#147** ＝ did／will／can／should／must 之后 → **原形**（couldn't **find**）
  **本条** ＝ have／has／had 之后 → **过去分词**（I've **been**／he's **gone**／I've **done**）
  ⇒ 她两次掉的都在"助动词后面动词变什么形"这个决策点上，只是方向不同 ⇒ **不许同组出题**
- 备注 高频不规则：be→been ｜ go→gone ｜ do→done ｜ see→seen ｜ take→taken ｜ get→got(ten)

### 260 · 中文的"这事／这个东西"→ it／this／about it（不要 the thing）
类型 词汇 ｜ 新建 2026-08-20
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 词组

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
"知道这事"（"这事"不许用 the thing 说）

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
- 备注 常配的介词：find out **about** it ／ know **about** it ／ hear **about** it ／ talk **about** it

### 262 · 口语转折工具箱（Then again／That said／Having said that／On the flip side／Mind you）
类型 词组 ｜ **合并条·出题必须整组出**（§3.2c，她 2026-08-23 定：只出一句 ＝ 违规）｜ 新建 2026-08-20（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-23** ｜ 题型 整句

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
★ 5 句，五个转折标记各一句 —— 只出 Then again 会永远测不到另外四个
　① "话说回来，奖励也会把孩子的动机带偏。"（转折标记用 **T** 开头的**两个词**起头）
　② "话虽如此，我还是觉得值得试一次。"（转折标记用 **T** 开头的**两个词**起头，与 ① 不同 · ⛔ 不许用 though）
　③ "话说回来，也不是每个人都合适。"（转折标记用 **H** 开头的**三个词**起头）
　④ "反过来说，网上买也有网上买的麻烦。"（转折标记用带 **flip** 的块起头）
　⑤ "不过话说回来，他也没做错什么。"（转折标记用 **M** 开头的**两个词**起头）
　　★ 目标形式（教练看，⛔ 不进发题稿）：① Then again ② That said ③ Having said that ④ On the flip side ⑤ Mind you

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
★ 4 句，覆盖这一族的不同动词 —— 只出 promise 一句会漏掉她在 give/show/send 上的语序
　① "他答应给他儿子买最新那款手机。"（用 **promise** ＋ 两个宾语说，不用 to）
　② "她给了我一本很旧的书。"（用 **give** ＋ 两个宾语说，不用 to）
　③ "他把照片给我看了。"（用 **show** ＋ 两个宾语说，不用 to）
　④ "我给她寄了张明信片。"（用 **send** ＋ 两个宾语说，不用 to）

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


### 264 · a sense of ＋ 只跟固定那几个抽象名词（achievement／purpose／belonging／control）
类型 搭配 ｜ 新建 2026-08-20（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-23** ｜ 题型 词组

**问题是什么**
**a sense of** ＋ 只跟固定那几个抽象名词（achievement／purpose／belonging／control）。
判据：**a sense of 是个半封闭的框**，后面只跟少数几个固定抽象名词：
```
✅ a sense of achievement（成就感）｜ a sense of purpose（目标感）
   a sense of belonging（归属感）｜ a sense of control（掌控感）｜ a sense of direction
❌ a sense of payoff／a sense of reward／a sense of result —— 这些词不进这个框
★ 想说"有奔头/值得"，走别的说法，不要硬塞进 a sense of：
   something to work towards（有个目标可奔）
   make the effort feel worth it（让努力显得值）
   feel like it's paying off（感觉有回报了）—— payoff 的动词形式反而好用
```
一句话规则：**框架是背来的，不是造的**。看到 a sense of 就只从上面五个里选；
说不出来就换整个说法，别在框里填新词。
★ 与 🎓**#206**（书面词降级）的分工：那条管"这个词太书面，换口语版"；
　本条管"这个**框架**只收哪几个词" ⇒ 不同层，不重复。

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
找法：a sense of 一出口就问 —— 后面那个名词在那五个里吗？不在 ⇒ ⛔ 别硬塞，换整句说法。

**题面**
**点名**："努力有奔头"（用 **a sense of** ＋ 一个固定搭配的名词说，⛔ 不许自己造词、⛔ 不许用 pay off）

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

### 265 · 对身体好 ＝ good for you／good for your health（health 前面不能光秃秃）
类型 搭配 ｜ **合并条·出题必须整组出**（§3.2c，她 2026-08-23 定：只出一句 ＝ 违规）｜ 新建 2026-08-21
状态 连对2 连错0 上次2026-09-11 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-23**（连对达线 ＋ 她当场指定"这条毕业"）｜ 题型 词组

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
★ 3 句，覆盖 good/bad for ＋ 不同的身体/心智属性 —— 只出一句会漏掉别的搭配位
　① "对身体好"（用 **good for** 说）
　② "对记忆力不好"（用 **bad for** ＋ 那个名词说）
　③ "对心脏好"（用 **good for** ＋ 那个名词说）
　　★ 目标形式（教练看，⛔ 不进发题稿）：① good for you ② bad for your memory ③ good for your heart
　　★ 题面 2026-08-23 改（付息日 c 段·题面撞车）：原题面"早睡早起对身体好。"与 #254 的题面"早点睡对身体好。"
　　　几乎同一句，而 #254 的考点在**主语位 -ing**、本条的考点在 **good for 后面的限定词** ——
　　　两条落在句子不同位置，本来能分别记档；但两条**同时在池子里**时会互相提示 ⇒ 换成不带动名词主语的句子

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
状态 连对2 连错0 上次2026-09-11 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-24** ｜ 题型 词组

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
★ 3 句，三个成员各一句 —— 只出 apart from 会漏掉她在别的成员上的缺口
　① "除了我妈"（"除了"用**两个词** · **a** 开头 · ⛔ 不许用 aside）
　② "除了我哥"（"除了"用**两个词** · **o** 开头）
　③ "除了周末"（"除了"用**一个词** · **e** 开头 · ⛔ 不许用 excluding）
　　★ 目标形式（教练看，⛔ 不进发题稿）：① apart from my mum ② other than my brother ③ except (at) weekends
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
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-24** ｜ 题型 词组

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
**点名**："让人看见你的产品"（用 **get** 起头说，⛔ 不许用 see／show／notice）

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
状态 连对2 连错0 上次2026-09-11 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-24** ｜ 题型 整句

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

### 269 · "不太了解／知道得少" 口语走 don't know much about it（不用 know little／only know little）
类型 结构 ｜ **合并条·出题必须整组出**（§3.2c，她 2026-08-23 定：只出一句 ＝ 违规）｜ 新建 2026-08-21（**她当场指定**）
状态 连对1 连错0 上次2026-09-11 ｜ **合并条·出题多句覆盖** ｜ **🎓 已毕业 2026-08-23 · 她指定**（"这条毕业"）｜ 题型 整句

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
　① "大家对这个牌子不太了解。"（"不太了解"用 **don't** 起头说 · ⛔ 不许用 well／little）
　② "我没多少钱。"（"没多少钱"用 **don't** 起头说）
　③ "那儿没什么可玩的。"（"没什么可玩的"用 **there isn't** 起头说）
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
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-25** ｜ 题型 词组

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
**点名**："很多建议"（"建议"用 **advice** 说，⛔ 不许用 many） ／ **点名**："一条建议"（"建议"用 **advice** 说，"一条"要用一个**量词块**说）

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
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-27**（连对2）｜ 题型 词组

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
**点名**："乱扔垃圾"（用 **litter** 那个词说）
★ 题面 2026-08-27 整句改（§6.5 审核项 8 题面撞车）：原题面"乱扔垃圾**罚**得挺重"里的"罚"会把她逼向 `you get **fined for** littering` —— 那正是 **#273（fine sb FOR doing）的考点**，两条同一天出会互相泄题。新题面去掉"罚"字，只留 litter 这一格

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
- 备注 与 #261（抽象名词不可数：action／feedback／…）的分工：那条管**抽象名词**那一小撮，
  本条管 **litter 这个具体的词**（且它还有动词用法）⇒ 按 §3.2 词汇按具体词一条一号，不并

### 274 · prepare FOR class（备课／备考，介词是 for；prepare sth ＝ 把东西准备好）
类型 搭配 ｜ **从 #41 拆出 2026-08-23**
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-27**（连对2）｜ 题型 词组

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
**点名**："备课"（用 prepare ＋ 一个介词说）

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

### 275 · whether 后面要跟【主谓】，不能只跟名词或形容词
类型 结构 ｜ **从 #64 拆出 2026-08-23**
状态 连对3 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-27**（同日两次产出各算一次，§3.3）｜ 题型 整句

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


### 276 · for ages ／ in ages ＝ "很久"（for long 只用在"没持续多久"里）
类型 词汇 ｜ **从 #166 拆出 2026-08-23**
状态 连对2 连错0 上次2026-09-11 ｜ 题型 整句 ｜ **回潮 2026-09-05**（08-21 毕业 → 09-05 复检里**同日两次产出**：不点名那次写成 `for long` ❌ ⇒ 撤销毕业、连对清零；点名那次写出 `in ages` ✅ ⇒ 连对回到 1。★ `for long` 这个错 08-19 已犯过一次，今天是**第三次**）｜ **🎓 已毕业 2026-09-07**（连对2 ＝ 09-05 ＋ 09-07；09-05 回潮后第二次毕业）

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

### 277 · 双面立论句型：It's mainly about A while B-ing（一句话同时给"要做的"和"要放的"）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）
　　※ 状态与日志见下（2026-08-27 首测通过）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

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
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 词组

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
**点名**："给孩子自己安排的空间"（"空间"用 **r-** 开头的那个名词说，⛔ 不用 space／freedom）

- 2026-08-23 新建 · **她主动提出**（§2③）· d 段重答 R1 第二版 · `giving kids room to manage themselves`
- 2026-08-27 ✅ 付息日 b 段（**本条从建立起第一次被测到**）·
  `you should give kids **room to** manage their own time.`
  ——**room**（不是 space）＋ 后面挂不定式 to do ⇒ 一字不差，**连对 0 → 1（差一次毕业）**
  ★ `manage their own time` 是她自己补的（题面只说"自己安排"）—— 落到具体的东西上，加分
  ★ 今天改 #277 题面的收益：#277 旧题面里带着"空间"两个字，会把本条答案先泄出去；改后独立命中
- 2026-08-28 ✅ 复习第2组 · `you need to give kids room to manage their own time.`
  ——room 不带冠词，正是这个块的形状 ⇒ 连对2，**毕业**
- 2026-09-11 ⚡ 自评免测 · 付息日 a2 第 4 组（打包串里，她原话："其他的直接过"）

### 280 · make a huge difference（差别很大／很管用）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-08-30 ｜ **🎓 已毕业 2026-08-29**（连对2 ＝ 08-27 ＋ 08-29）｜ 题型 词组
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
**点名**："差别很大"（用 **make** 说 · ⛔ 不许用 different）

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


### 281 · step back（往后退一步，不插手）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 词组

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
**点名**："往后退一步"（用 step 说）

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

### 283 · 收尾句型：It's really about A first, and then B（把前面几点排成先后，收成一条线）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

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
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 词组

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
**点名**："说到底就是几样东西凑一块儿"（"说到底就是"用 **boil** 那个说法）

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


### 285 · give sb (real) alternatives to sth／doing sth（给人别的选择，而不是只能……）
类型 搭配 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 词组

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
**点名**："真正能替代开车的选择"（用 **alternative** 说，别用 choice）

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

### 287 · flow smoothly ／ keep sth flowing（车流顺畅／让它一路走得顺）
类型 搭配 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ **keep 族·一组最多 2 条**（c 段 2026-08-27 加）｜ 题型 词组

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
**点名**："让剩下那些车一路走得顺"（用 **flow** 说）

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

### 288 · 机制句型：once X costs you something, you start asking whether …（把政策翻译成人的心理反应）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-29**（连对2）｜ 题型 整句

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
**点名**："一旦每次出门都要花点钱，你自然会掂量这趟是不是真有必要。"（用 **once** 起头，后半句用 **start asking whether** 说；⛔ 动词就用 asking，不许换成 think／wonder）
★ 点名 2026-08-28 加结构限定（08-27 她走了 `start thinking whether` 这条绕路）

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
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 词组

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
**点名**："特别迷这个"（用 **obsessed** 说）

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

### 290 · 收尾块：… for totally different reasons depending on who you ask（同一个现象，不同的人理由完全不一样）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

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
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-26**（连对2）｜ 题型 整句

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
**点名**："我先给你看个东西。"（**不用 want／going to** 说）
★ 不点目标形式：`Let me show you something first.` 与 `I'll show you something first.` **两个都命中考点**；要逼掉的错路是 `I show you something first.`
★ 题面 2026-08-25 加点名（§6.5 审核项 7）：不点名时 `I want to show you something first.`／`I'm going to show you something first.` 两条都合法、都不是一般现在时 ⇒ **合法绕开考点**；点掉这两条路不泄答案 —— 错路 `I show you something first.` 照样开着，两个目标形式（Let me／I'll）也一个都没说出来

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
- 备注 题面互斥（§3.1 第三档）：**#270** 的题面是"我就给你一条建议。"（考点 ＝ a piece of advice），
  本条题面另起一句"我先给你看个东西。" ⇒ 两条永不撞车

### 293 · "其中的一侧／一头／一角" ＝ one side of it ／ one of its sides（不说 its one side）
类型 结构 ｜ 新建 2026-08-24
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-26**（连对2）｜ 题型 词组

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
"楼的一侧"（用 **of** 说）

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

### 295 · "做某事的目的" ＝ the purpose OF doing sth（口语直接说 why they do it）
类型 搭配 ｜ 新建 2026-08-24
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-08-26**（连对2）｜ 题型 词组

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
**点名**："做事的目的"（用 **purpose** 说）

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

### 296 · cut corners（偷工减料／图省事把该做的步骤跳掉）
类型 词组 ｜ 新建 2026-08-24（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 词组

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
**点名**："在材料上偷工减料"（"偷工减料"用 **cut** ＋ 一个名词说）

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


### 297 · keep your mind active（"保持…活跃"用 keep ＋ 宾语 ＋ 形容词，不用 make sth stay adj）
类型 搭配 ｜ 新建 2026-08-25
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-27**（连对2）｜ **keep 族·一组最多 2 条**（c 段 2026-08-27 加）｜ 题型 词组

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
**点名**："让脑子保持活跃"（用 **keep** 说）

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

- 备注 ★ **这不是句型缺口，是一个具体搭配没调出来**：她已经会 keep ＋ 宾语 ＋ 补语 ——
  08-23 R3 `keeps cars moving`、08-23 R1 `keeps things simple` 两处都自发用对。
  ⇒ 出题只出这一个搭配，别扩成"keep 句型"整片（§3.2b：考点必须能收敛成一个词组）

### 298 · have the final say（拍板／最后说了算）
类型 词组 ｜ 新建 2026-08-25（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 词组

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
**点名**："最后拍板"（"拍板"用 **say** 那个词说 —— 它在这儿是名词）
★ 题面 2026-08-27 改点名（§6.5 审核项 7）：原点名写 **final**，但 `my mum made the **final** decision` 既合法又含 final ⇒ **合法绕开考点**（考点是 the final **say** 这个块，不是 final 这个词）。改成点 **say**：封掉 final decision／it was her call，而 the final say 这个搭配她仍要自己凑出来

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


### 299 · not much of a/an ＋ 名词（"算不上一个…／没多少…"）
类型 词组 ｜ 新建 2026-08-25（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 词组

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
**点名**："算不上个厨师"（"算不上"用 **much of** 说）

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


### 300 · stage 前面的介词是 at（at every stage／at this stage，不用 in）
类型 搭配 ｜ 新建 2026-08-26（**补建**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 词组

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
**点名**："在人生的每个阶段"（用 **stage** 说）
★ 题面 2026-08-27 删掉点名里的"注意介词"四个字（§10 禁令 5 禁预告测试点）：点名的合法范围是**点目标词/句型/块**，"注意介词"点的是**考的是哪一类**，等于预告测试点。只留 stage 就够：不点 stage 时 `at every point in your life`／`throughout your life` 两条合法绕路都不测本条；点掉之后介词那一格仍然空着 ⇒ 考点存活

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


### 302 · something breaks（东西坏了／出故障，break 当不及物动词，不用 be broken）
类型 搭配 ｜ 新建 2026-08-26（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 整句

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
**点名**："要是有什么东西坏了，给我打个电话就行。"（"坏了"用 **break** 说，不用 broken）
★ 题面 2026-08-27 整句改（§6.5 审核项 8 题面撞车）：原题面"…大家都**去找他**"里的"去找"正是 **#304（turn to sb）的考点**，两条同组出 ⇒ 她答本条时会顺手把 #304 的答案先写出来。新题面取判据里的原型句 `If anything breaks, just call me.`，与 #303／#304 零重叠

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


### 303 · sb is the kind of person ＋ 关系从句（形容一个人是"那种人"）
类型 结构 ｜ 新建 2026-08-26（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2 · **主语位和宾语位两半都验过**）｜ 题型 整句

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


### 304 · turn to sb (for sth)（有事去找某人／求助）
类型 词组 ｜ 新建 2026-08-26（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ 题型 词组

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
**点名**："遇到麻烦的时候去找他"（用 **turn** 说）
★ 题面 2026-08-27 微改（§6.5 审核项 8）："出问题的时候"可能被译成 `when something breaks`，那是 **#302 的考点**；换成"遇到麻烦的时候"（in trouble／when there's a problem）后零重叠
★ 2026-08-28 后记：题面这一层隔开了，**但同场 priming 没隔开** —— #302 排在第 1 组、本条排在第 3 组，她仍然把 `If something breaks` 搬了过来

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


### 305 · stay patient（keep ＋ 形容词只跟一小撮词，patient 不在里面）
类型 搭配 ｜ 新建 2026-08-26
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-28**（连对2）｜ **keep 族·一组最多 2 条**（c 段 2026-08-27 加）｜ 题型 词组

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
**点名**："一直很有耐心"（用【**一个动词 ＋ patient**】说，不用 is／be）
★ 题面 2026-08-27 改点名（§6.5 审核项 7，同 #294 08-25 那次的毛病）：原点名直接写 **stay** ＝ 把考点（keep 还是 stay）整个交出去，测了信息量为零。改成点**结构**（一个动词 ＋ patient，不用 be 动词）—— 封掉 `he is always patient`／`he's very patient` 两条合法绕路，同时把她掉过的那条错路 `keeps patient` 留着开着 ⇒ 考点存活
★ 边界（判档位时用）：`remains patient` 也对（判据里列了）⇒ 她若这么写按 ✅ 记 —— 本条真正要的是"**没走 keep**"，不是"必须写 stay"

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


### 306 · not just A — it's more B（"不只是A，更多的是B"：中间不能用 and）
类型 结构 ｜ 新建 2026-08-27
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-29**（连对2）｜ 题型 整句

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

### 307 · That's how ＋ 主谓（"这样一来他们才会…／就是这么来的"）
类型 结构 ｜ 新建 2026-08-28（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-30**（连对2 · **毕业那次已换句**）｜ 题型 整句

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

### 308 · empty into ＋ 海／湖（河流"注入"某处的介词）
类型 搭配 ｜ 新建 2026-08-29
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-31**（连对2 ＝ 08-30 ＋ 08-31）｜ 题型 词组

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
**点名**："流进东海"（用 **empty** 说）

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

### 309 · 推测过去 ＝ must have ＋ 过去分词
类型 语法 ｜ 新建 2026-08-29
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-08-31**（连对2 ＝ 08-30 ＋ 08-31）｜ 题型 整句

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

### 310 · all the way ＋ 方向／终点（"一路…"／"大老远…"）
类型 词组 ｜ 新建 2026-08-30（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-01**（连对2 ＝ 08-31 ＋ 09-01）｜ 题型 词组
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
**点名**："一路走回家" ／ "大老远从北京跑过来"（两句都用 **all the way** 说）

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

### 311 · 动词 ＋ its／his／my way ＋ 方向（"一路…着过去"）
类型 结构 ｜ 新建 2026-08-30（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-01**（连对2 ＝ 08-31 ＋ 09-01）｜ 题型 整句

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

### 312 · search for sth（search 找"东西"必须带 for）
类型 搭配 ｜ 题面 **点名**："找一份兼职"（用 **search** 说） ｜ 新建 2026-08-30
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-01**（连对2 ＝ 08-31 ＋ 09-01）｜ 题型 词组
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
- 备注 判据：
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
- 备注 判重（新建当天复核，§4④1b ⛔ 严禁脚本批量判 —— dedup 只捞候选，判断逐条人读）：
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

### 313 · message sb（发消息给某人，后面直接跟人）
类型 搭配 ｜ 题面 **点名**："发消息给你" ／ "跟朋友发消息"（两句的"发消息"都用 **message** 当**动词**说） ｜ 新建 2026-08-30（**她当场指定**）
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-01**（连对2 ＝ 08-31 ＋ 09-01）｜ 题型 词组
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
- 备注 判据：
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
- 备注 判重（新建当天复核，§4④1b ⛔ 严禁脚本批量判）：
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

### 314 · economic（经济的）≠ economical（省钱的）
类型 词汇 ｜ 题面 **点名**："经济增长"（那个形容词用 econom- 开头的词说） ｜ 新建 2026-08-31
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-03**（连对2 ＝ 09-01 ＋ 09-03；08-31 新建、当天首犯，两次点名直测连翻）｜ 题型 词组
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
- 备注 判据：
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
- 备注 **出题口径（单句，不做合并条）**：本次的缺口是**单向**的 ——
  想说"经济的"调出了 economical；**没有**"想说省钱的却调出 economic"的证据。
  ⇒ 照 🎓#255（vital ≠ virtual）的先例出**单句**，⛔ 不凭空造第二个方向（那是加戏）。
  若日后出现反向，再按 §3.2c③ 摘出来另立。
- 判重结论（§3.1 判重三步，2026-08-31 当天做）：**保留新建**
```
① 目标英文形式 ＝ `economic`
② 全档 grep `economic\|economical`（**范围含已毕业**）⇒ **零命中**
③ 最接近的一条 ＝ 🎓#255（vital ≠ virtual）—— 同样是"形近词选错"，
   但 §3.2 写死「词汇/搭配按**具体的词**一条一号」⇒ 另立
   **决定性证据**：按 #255 的规则去改 `economical growth`，它只管 vital／virtual 这一对，
   **给不出 economic** ⇒ 不是同一条规则 ⇒ 新建
④ 另比对 #89（加形容词回到 a）：那条管**冠词**，本条管**选哪个形容词** ⇒ 不同层
```
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 315 · support FROM sb（谁给的）≠ support FOR sb（给谁的）
类型 搭配 ｜ 题面 **点名**："政府的资金支持" ／ "政府对小企业的支持"（两句的"支持"都用**名词 support ＋ 介词**说） ｜ 新建 2026-09-01
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-04**（连对2 ＝ 09-03 ＋ 09-04；09-01 新建当天首犯，两次复测 from／for 两个方向各一句全中）｜ 题型 词组
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
- 备注 判据：
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
- 判重结论（§3.1 判重三步，2026-09-01 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
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
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 316 · log in（动词，两个词）≠ login（名词，一个词）
类型 词汇 ｜ 题面 **点名**："登不进去" ／ "登录页面"（两句都用 **log** 这个词说；第一句当**动作**，第二句当**东西**） ｜ 新建 2026-09-01
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-04**（连对2 ＝ 09-03 ＋ 09-04；题面 09-03 整改过——只钉词根 log 不钉词形，两次测的都是真考点）｜ 题型 词组
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
- 备注 判据：
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
- 备注 **出题口径（两句，一句测动词一句测名词，⛔ 不许只出一句）**：
  只出动词那一句，她永远测不到"什么时候该连着写"；只出名词那一句，考位根本没碰到。
  ★ 这不是 §3.2c 的"合并条"（成员只有 log in 这一个词），是**一个词的两种词类**。
- 判重结论（§3.1 判重三步，2026-09-01 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
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
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 317 · when it comes TO sth（说到／在……这件事上）
类型 词组 ｜ 题面 **点名**："说到网购和穿搭这些"（用 **come** 说） ｜ 新建 2026-09-03
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-04**（连对2 ＝ 09-04 同日两次独立产出：第 1 组点名中译英 ＋ 新题第 2 道自由产出；§3.3 她 08-23 定"同一天多次产出各记一次"）｜ 题型 词组
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
- 备注 判据：
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
- 备注 **出题口径**：只出"说到"那一句，⛔ 不在同一题里混进"说到底"——
  "说到底"归 🎓#58／🎓#284，中文触发词已经分掉了，混着出会让她分不清在测哪一条。
- 判重结论（§3.1 判重三步，2026-09-03 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
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
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 318 · one time WHEN ＋ 背景，主句装事件（讲往事的挂接顺序）
类型 结构 ｜ 题面 **点名**："我记得有一次，他两岁的时候，把一张画拿给我看。"（用 **one time** 起头说） ｜ 新建 2026-09-04
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-07**（连对2 ＝ 09-05 ＋ 09-07）｜ 题型 整句
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
- 备注 判据：
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
- 判重结论（§3.1 判重三步，2026-09-04 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
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
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 320 · point AT sth（指着某样东西）
类型 搭配 ｜ 题面 **点名**："指着墙上那张照片"（用 **point** 说，⛔ 不许用 to） ｜ 新建 2026-09-04
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-07**（连对2 ＝ 09-05 ＋ 09-07）｜ 题型 词组
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
- 备注 判据：
```
指着一个目标            point **at** sth        He pointed **at** the photo on the wall.
把某物瞄准某处（及物）   point sth **at** sth    He pointed the camera **at** me.
★ 检查触发：写完 point，问一句 —— **我是在"指"，还是在"把某个东西瞄准"？**
  在"指" ⇒ point 后面必须先出现 **at**。
```
- 备注 **不当考点的邻居**（写在这里防混，⛔ 不并进本条、不出题）：
  `point sth **out**` ＝ 指出来／点明（She pointed out two mistakes.）——**另一个块**，
  意思是"把没人注意到的东西说出来"，不是用手指。若日后她掉这个，另开号。
- 判重结论（§3.1 判重三步，2026-09-04 当天做，逐条人读）：**保留新建**
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
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

### 321 · principal ＝ 校长（≠ principle ＝ 原则）
类型 词汇 ｜ 题面 **点名**："校长"（用一个词说，⛔ 不用 head teacher · ⛔ 不用 headmaster） ｜ 新建 2026-09-05
状态 连对2 连错0 上次2026-09-10 ｜ **🎓 已毕业 2026-09-10**（连对2 ＝ 09-07 ✅ ＋ 09-10 ✅；09-05 建号后第一次毕业，中途零回潮）｜ 题型 词组
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
- 备注 判据：
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
- 备注 **不当考点的邻居**（写在这里防混，⛔ 不并进本条、不出题）：
  形容词 `principal` ＝ 主要的（the principal reason／the principal cause）——同一个词的另一个词性，
  她掉的是"校长"这个名词义 ⇒ 出题只出名词义。若日后形容词义单独掉，另开号。
- 判重结论（§3.1 判重三步，2026-09-05 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
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
- ⇒ **新建当天不测**（§3.1），下一个练习日起进池

### 322 · play WITH sth（玩"东西"一律带 with）
类型 搭配 ｜ 题面 "孩子在玩他们的玩具。"（"玩"用 **play** 说） ｜ 新建 2026-09-07
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-11**（连对2 ＝ 09-09 ✅ ＋ 09-11 ⚡ 自评免测；§4③ ⚡ 够 2 ＝ 她行使直接指定毕业）｜ 题型 整句
- 2026-09-07 📝 首犯 · 复检第 5 组 [6]（#215 的作答里，**同一题犯了两次**）·
  `kids put toys away after **playing them**.` ／ `After kids **played toys**, I put them away.`
  → playing **with** them ／ played **with** the toys
  ★ 建号理由：这条搭配 2026-08-21 只作为 🎓#67 的一行**备注**被提过一次
    （「另：away 不变形；玩具搭配是 play with」），**从来没有自己的编号** ⇒ 从来没进过召回队列
    ⇒ 今天同一题里连犯两次，正是"讲过但没测过"的典型。
- 2026-09-09 ⚡ 自评免测 · 在池第 2 组（她原话："前 7 题直接过"）
- 2026-09-11 ⚡ 自评免测 · 付息日 a 段第 1 组（她原话："6. 直接过"）⇒ 连对1 → 连对2 **毕业**（§4③：⚡ 够 2 ＝ 她行使直接指定毕业）
- 备注 判据：
```
玩"东西"     play **with** sth      play with toys ／ play with the dog ／ play with your phone
玩"项目"     play ＋ 名词（不带 with）play football ／ play the piano ／ play a game ／ play a role
★ 判据一句话：后面是**一个东西** ⇒ 必须有 with；后面是**一项活动** ⇒ 直接接。
★ 检查触发：写完 play，问一句 —— 我后面接的是东西还是活动？
```
- 判重结论（§3.1 判重三步，2026-09-07 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
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
- ⇒ **新建当天不测**（§3.1），下一个练习日起进池

### 323 · 嵌入疑问的 wh 词不能吞（know **what** they want）
类型 结构 ｜ 题面 "他聪明到知道自己到底要什么、也知道怎么去够到。"（用 **know** 起头的一个不定式说） ｜ 新建 2026-09-07
状态 连对2 连错0 上次2026-09-11 ｜ **🎓 已毕业 2026-09-11**（连对2 ＝ 09-09 ✅ ＋ 09-11 ✅）｜ 题型 整句
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
- 备注 判据：
```
know／tell／wonder／figure out 后面接嵌入成分时，**每一个成分都要有自己的 wh 词领头**：
  know **what** they want ／ know **how** to do it ／ know **why** it matters ／ know **where** to start
并列两个的时候两个 wh 都要出现：know **what** they want and **how** to get there.
★ 这里的 what 是双重身份：既是连接词、又是 want 的**宾语** ⇒ 吞掉它，want 就没宾语了。
★ 检查触发：写完 know／tell／wonder／figure out，数后面有几个成分，每个是不是都有 wh 领头。
```
- 判重结论（§3.1 判重三步，2026-09-07 当天做，⛔ 严禁脚本批量判，逐条人读）：**保留新建**
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
- ⇒ **新建当天不测**（§3.1），下一个练习日起进池

### 328 · 中性尺寸与比较级一律 small（⛔ littler 不存在）
类型 词汇 ｜ 题面 "这家公司比那家小。"（"小"用形容词的**比较级**说） ｜ 新建 2026-09-09
状态 连对1 连错0 上次2026-09-10 ｜ 题型 整句 ｜ **🎓 已毕业 2026-09-10 · 她指定**（§3.3「她可直接指定」；原话："这个直接毕业吧"。首测 ✅ ＋ 她指定 ⇒ 连对停在 1，⛔ 未凑连对2）
- 2026-09-09 📝 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个 little 我也纠结了很久和 small"
  条目内容：① **比较级只有 smaller**，⛔ 没有 littler；
  ② 中性地说尺寸（a small company／a small room）默认 small；
  ③ little ＝ 尺寸 ＋ 情绪色彩（可爱／微不足道），**只作定语**、⛔ 不作表语（✗ the peg is little）。
  ★ 她这次写的 `a little peg` **是对的**（定语位 ＋ 带"就那么一点点"的语气）⇒ 本条不是纠她的错，是把边界钉住。
- 2026-09-10 ✅ 复习 · 在池第 2 组（首测）· `This company is smaller than that one`
  smaller 用对（⛔ littler 不存在），than that one 的比较对象也对齐了
  ★ 她当场指定毕业（原话："这个直接毕业吧"）⇒ §3.3「她可直接指定」⇒ **🎓·她指定**，连对停在 1
- 判重结论 grep `little\|small` 命中 6 处全是别的条目的例句正文（#46 #56 #63 等），⛔ 无同考点条目 ⇒ 保留
