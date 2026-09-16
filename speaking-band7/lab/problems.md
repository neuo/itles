# 问题总表 · problems.md

> 一条问题一个编号。**状态行紧挨日志行**；状态由日志重放而来，两边不一致时以日志为准。
> 归类粒度：词汇/搭配/词组/拼写 按【具体词组】；语法/结构 按【规则】。
> **连对 2 → 毕业**（她 2026-08-20 定，统一口径；⛔ 头部原来写的"连对 3"是 08-20 之前的旧线，
> 　2026-09-04 更正）：**只把状态行改成「🎓 已毕业 日期」，条目和全部日志行留在原地**，复习不再召回；
> 毕业后再犯 → 在原地把状态行改回未毕业、连对清零，日志接着往下记。
> **本表只装未毕业的**：🎓 条目在 `graduated.md`。
> 　搬迁 ＝ **每天收尾跑 `python3 speaking-band7/lab/lab.py migrate`**（2026-09-04 起，SKILL §3.3 §11）；
> 　教练只在条目原地改状态行，⛔ 不手工搬。脚本把两个文件当**一个档案**读 ⇒ 搬没搬不影响任何一个数。
> 　⚠️ 墓碑/迁出条目（（已并入…）／⛔ 作废）**留在本表**，`migrate` 一律不动它们。
> **数条目一律 `lab.py stats` / `lab.py count`，⛔ 禁 grep**（SKILL §0.1.5）——
> 　grep 会把墓碑也数进去：2026-09-04 实测 🎓 报 291（真值 290）、未毕业报 29（真值 13）。
> 迁移自 `coach/fluency_lab.md` 的 B 表（2026-08-18，手工逐条）。历史日志重放自 9 行 📊（08-09→08-17）。
> ⚠️ 2026-08-09 之前的记录不在事件流里，标「旧账」的条目连击可能偏低。

---

### 7 · 比较级三条（短词 -er／长词 more／much·far·a lot 后必须比较级）
类型 语法 ｜ 旧号 B19
状态 连对0 连错1 上次2026-08-19 未毕业 ｜ **回潮（当天毕业当天回潮）** ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定）｜ 题型 产出验
　　★ 她 2026-08-27 的原话："**标记下就行了，不出题，只记录**" ——
　　　⇒ ① 历史 ❌ **不回扫、不撤销**（连错/累错/顽固标记全部保持原样）
　　　　 ② 本条**永不出题**（不进任何复习组，含付息日 a/b 段）
　　　　 ③ 以后在任何地方掉了 ⇒ **只追加一行 ⚪ 记录**，不判档位、不动状态行

**问题是什么**
比较级三条规则，同一个考点：
· 短词 ＋ **-er**（noisi**er** · cheap**er**）
· 长词 ＋ **more**（**more** fragile · **more** convenient · **more** willing）
· **much／far／a lot** 后面必须跟比较级（much noisi**er** ｜ much **more** fragile；⛔ much convenient）
判据一句话：中文里出现"更／比较／多了／少了"这一层程度 ⇒ 英文必须有 -er 或 more，丢了就只剩原级。
★ 本条是**形态类**（她 2026-08-27 定）：不是不会，是产出时检查没跑 ⇒ 在哪儿掉都只记 ⚪。

**怎么发现的**
旧 B 表迁移（B19，2026-08-18），原始触发句未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 同日第 9 组她写 `much convenient`——much 后面没跟比较级 ⇒ 撤销当天的毕业、连对清零重新入池。
2026-08-19 她定："**比较级那个不用复习了，会，只是会漏，以后重点看就行，和单复数一样**"；
2026-08-27 她再定："**标记下就行了，不出题，只记录**" ⇒ 转形态类、永不出题。

**我错在哪**
她的：much convenient（2026-08-19 第 9 组）　　正确：much **more** convenient
检查触发：写完一个形容词，回头问"它前面有没有 much／far／a lot／than"——
　有就必须是比较级；**长词（convenient／important／expensive）看有没有 more**

**题面**
不出中译英题（题型 产出验 ＋ 形态类·只记录）；挂自由产出抓：形容词前有 much／far／a lot／than 却没变比较级、长词漏 more。
★ 原题面（留档，⛔ 不再发题）："吵多了" ／ "脆弱得多"（两个都译；程度那一层不许省）

- 2026-08-17 ✅ 首次进流
- 2026-08-19 📝 她定：**"比较级那个不用复习了，会，只是会漏，以后重点看就行，和单复数一样"**
  ⇒ 本条转形态类：不进中译英复习组，只在自由产出里判
- 2026-08-19 ✅ `much noisier than it was ten years ago` ＋ `much more fragile`（三条规则全中）→ 当时判毕业
- 2026-08-19 ❌ 同日第 9 组 · `much convenient`——much 后面没跟比较级
  ⇒ 两次都是 cold，按"以最后一次为准" ⇒ **撤销毕业，连对清零重新入池**
- 2026-08-31 📝 付息日 a 段第 2 组 · 她 08-31 临时指令把全部未毕业条目拉出来重测（形态类不推进连对，§3.4②）
  `it's much noisier that it was ten years ago.` ／ `much more fragile`
  考点三条全中：短词 → noisi**er** ｜ 长词 → **more** fragile ｜ much ＋ 比较级。
  ★ `that` → `than` 判**手滑不计错**：本条 08-19 日志里她写对过 `much noisier **than** it was ten years ago`
    ⇒ 不是不知道这个词；且 than 不在本条考点内。
  ⇒ 状态行一个字不动
- 2026-09-10 ⚪ 在池第 1 组 · #261 成员 ① `people are willing to take action`
  中文"更愿意干"的"更"是一整层比较，英文丢了 more 就只剩"愿意"⇒ **more willing**。
  ★ 形态类（本条状态行带 ⚪ 只记录·不出题）⇒ 只记 ⚪，⛔ 不判档位
  检查触发：中文里出现"更／比较／多了／少了"，回头看英文有没有 -er 或 more
- 2026-09-11 ⚪ 付息日 d 段重答 R10 · `a more customized plan` —— 比较级悬空（比谁更定制？），形态类只记号；同篇 pretty much everything 这类程度表达用得准 ⇒ 会，检查没跑
- 备注 分诊：**短词加 -er 她已自动化（noisier／cheaper 都对），长词要加 more 的那一半没装上**
  ⇒ 重新入池后只测长形容词（convenient／important／difficult／expensive）

### 10 · 主谓一致
类型 语法 ｜ 旧号 B27
状态 连对0 连错2 上次2026-08-20 未毕业 ｜ **累错 7** ｜ **形态类·不召回** ｜ **顽固** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定）｜ 题型 产出验
　　★ 她 2026-08-27 的原话："**标记下就行了，不出题，只记录**"（教练问的正是本条那次
　　　`it help me clear my head` 的 ❌ 要不要按 §3.4⑤b 撤销）⇒ **不撤销、不回扫**：
　　　累错 7 和"顽固"标记**原样保留**，它们只当历史读，不再驱动任何出题

**问题是什么**
**主谓一致**：谓语跟着主语的数走 —— 第三人称单数主语 ⇒ 动词加 **-s**。
同一格里的邻居（别串，都是"看着不像单数、其实是单数"的考位）：
· everyone ／ no matter what 里的 what ⇒ 单数（everyone … **is** ｜ no matter what **happens**）
· whether 从句当主语 ⇒ 单数（whether you have help or not **makes** a huge difference）
· attraction：主语后面紧挨着一个复数名词，把动词拽跑（financial support from governments **plays**）
判据一句话：把主语和动词之间的插入语盖住，只看主语的数和动词对不对得上。
★ 本条是**形态类**（她 2026-08-27 定）：低压中译英里对、高压自由产出里掉 ⇒ 缺口在**检查动作**，不在知识
　⇒ 在哪儿掉都只记 ⚪，历史里的累错 7 与"顽固"只当历史读。

**怎么发现的**
旧 B 表迁移（B27，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ❌ 一天内三次
（`the two hours MAKES` ／ `my mom HELP` ／ `he WALK`）。
之后在自由产出里反复掉：2026-08-19 新题 bank:489 `if everyone run red lights`；
2026-08-21 新题 bank:434 `it **help** me clear my head`；
2026-08-31 付息日 d 段重答 R9 `So financial support from governments **play** a crucial role …`。
2026-08-27 她定："**标记下就行了，不出题，只记录**" ⇒ 转形态类、⛔ 不再出题。

**我错在哪**
她的：`it help me clear my head`　　正确：`it **helps** me clear my head`
检查触发：每写完一个谓语，回头看主语是不是第三人称单数（08-19 她定，同比较级）
· 主语和动词中间隔了一长串插入语 ⇒ 把插入语盖住再看（09-10 新增）
· and 后面还有一个动词 ⇒ 看它跟不跟前面那个同主语；同主语就必须同形（keeps … and stay**s**，08-27 新增）
· 带 what／who／whatever 的从句 ⇒ 只看一眼那个从句里的动词有没有跟主语的数对上（09-10 新增）

**题面**
不出中译英题（题型 产出验 ＋ 形态类·只记录）；挂自由产出抓：第三人称单数主语的谓语漏 -s
（含 everyone／whether 从句／no matter what 从句当主语，以及被紧邻复数名词拽跑的 attraction）。
★ 原题面（留档，⛔ 不再发题）："他每天七点起床，从来不迟到。"（一句里两个动词都要加 s）

- 2026-08-11 ❌ 一天内三次（the two hours MAKES／my mom HELP／he WALK）
- 2026-08-12 ❌
- 2026-08-13 ❌
- 2026-08-15 ❌ 自由产出 `the words was`
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ❌ **自由产出**（新题 bank:489）· `if everyone run red lights`——everyone 是单数（runs），
  且主句用了 could be ⇒ 这里还该虚拟（ran）。一句里主谓一致和时态平面一起塌
  ★ **这是"形态类只在自由产出里判"改规则后第一次抓到，正是 §3.4 设计的用法**
- 2026-08-20 ❌ 复习#34 句里 · `the teacher get the students to work in groups`——第三人称单数漏 -s
  ｜同日 #258 那句 `he feels like it` 的 -s 是带上的 ⇒ 仍是"检查跑不跑得起来"的问题，不是不会
- 2026-08-21 ⚪⚪❌ **同一天三次，三次档位不同 —— 这条正好把新规则跑通了**：
　⚪ 复习#59 句里 `what did you **ate** yesterday`（这处其实归 #147，不归本条）
　⚪ 复习#264 句里 `rewards **makes** children feel…`——中译英复习 ⇒ 按她 08-21 定的规则
　　 **只做记号，不记档位、不动状态行**
　❌ **自由产出**（新题 bank:434）· `it's a perfect little escape - it **help** me clear my head`
　　 —— 主语 it 是第三人称单数（helps）⇒ **这一次照常记 ❌**，连错 1→2，累错 7
　★ 三次放在一起看正是 §3.4 的设计：**中译英里她一半对一半错，信息量低；自由产出里才是真掉的地方**
- 2026-08-27 ⚪ **只做记号** · 付息日 a 段 · 复习 #305 句里 ·
  `he always **keeps** his cool and **stay** patient.` → and **stays** patient
  ⇒ **一句之内一对一错**（前半 keeps 加对了、后半 stay 掉了）—— 正是本条"检索失败不是不会"的定义。
    按 §3.4⑤ **只做记号：不记 ❌、状态行不动**
  ★ 检查触发（新增一条，本条专用）：**and 后面还有一个动词时，回头看它跟不跟前面那个同主语**——
    同主语就必须同形（keeps … and stays）
- 2026-08-27 ⚪ **正面观察行（不改状态）** · 付息日 b 段 #280 句里 ·
  `**whether you have help or not** makes a huge difference.`
  ——**whether 从句当主语 ⇒ 谓语用单数 makes**，这是本条里偏难的一档，她一次到位
  ⇒ 与同日 #305 句里那次 ⚪（stay 漏 -s）**同一天一对一错**，再次印证本条 ＝ 检索失败不是不会
- 2026-08-28 ⚪ **正面观察行（不改状态）** · 复习第2组 #280 句里 ·
  `Whether you have help or not **makes** a huge different.`
  ——whether 从句当主语 ⇒ 谓语用单数 makes，**与 08-27 同一档、连续第二次做对**
  （同句 different／difference 那处判的是 #280 ＋ #156，与本条无关）
- 2026-08-29 ⚪ 新题 P2 · **正面记号**（形态类只记号，不动状态行）·
  `which **traps** the sand` ／ `the river **holds** special significance` ／ `it **is** the primary source`
  ——三单 -s 三处全对，一处没漏
- 2026-08-30 ⚪ 新题 P3 · **正面记号**（形态类只记号，不动状态行）·
  `smartphones **are** connected` ／ `People **can**` ／ `everyone … **is** glued` ／
  `they also **take** up` ——四处全对，一处没漏。
  ★ 尤其 **everyone 当单数配 is** —— 这一格是主谓一致里最容易掉的，一次到位。
  ★ 同日第 2 组 [6] 里也对了一次（`whether … makes`），见 #280 行。
- 2026-08-31 📝 付息日 a 段第 2 组 · 她 08-31 临时指令重测（形态类不推进连对）
  `he gets up at 7 every day and never runs late.`
  考点命中：一句里两个动词 get**s** ／ run**s** **都**加了 s ——
  本条（累错 7 · 顽固）在"两个动词同句"这个考位上第一次两处同时中。
  ⇒ 状态行一个字不动
- 2026-08-31 ⚪ 付息日 d 段 · 重答 R9 · **形态类只记 ⚪**（§3.4②：不记 ❌／不动状态行／不计入本篇真错数）
  `So financial support from governments **play** a crucial role …`
  真主语 ＝ financial support（单数），被紧挨着的 governments（复数）拽跑 ＝ 典型 attraction。
  ★ §3.4 执行自查已跑：**同一篇**里 `Start-ups **are**`／`it's`／`people **are**`／`they **take**`
    四处主谓一致全对 ⇒ 不是不会。
  ★★ **本日含金量最高的一条证据**：同一天 a 段第 2 组她把本条的两个动词 -s 同时做对
    （`he **gets** up at 7 every day and never **runs** late.`），**30 分钟后在自由产出里掉了**。
    ⇒ §3.4 判据的教科书级实证：低压答得出 ＋ 产出时掉 ⇒ 缺口在**检查动作**，不在知识。
    ⛔ 不因此把它放回复习池（放回去她只会在组里再做对一次）。
  ⇒ 状态行一个字不动
- 2026-09-01 ⚪ 复习第1组 [8] 句里 · 顺带产出 · 形态类只记录（§3.4②）
  `**Financial support** for governments **is** vital to economic growth.`
  主谓一致做对：真主语 financial support（单数）＋ is。
  ★ 与 08-31 R9 的 `financial support from governments **play** a crucial role` 是
    **同一个主语、同一个位置**：后面紧挨着 governments（复数）。昨天被 attraction 拽跑，今天没有。
  ★ 与 08-31 上午 a 段第 2 组 `he **gets** up at 7 and never **runs** late` ✅ 合起来看，
    形态类的形状是"**低压对、高压掉**"，不是"有时会有时不会"⇒ §3.4 判据继续成立。
  ★ 按 §3.4②：⚪，不记 ✅／❌、不判档位、不动状态行、不进复习池、不计入真错数。
- 2026-09-07 ⚪ 留痕 · 09-05 复核时才看见 · `These letters on the cake **is** written in sweets and biscuits.`
  → The letters ... **are** written。形态类（§3.4②）只记 ⚪。执行自查：她 09-07 同一条题写出
  `The words ... **are** spelled out` ⇒ 会，缺的是产出时的检查。
- 2026-09-10 ⚪ 在池第 1 组 · #238 成员 ② `No matter what happen, the company has to…`
  no matter what 里的 what 是单数主语 ⇒ 动词跟单三：happen → **happens**。
  ★ 同一篇里她多处主谓一致做对（`there is widespread agreement` · `If risk is lower` ·
    `There isn't much research`）⇒ §3.4 执行自查通过 ⇒ 只记 ⚪，⛔ 不记 ❌、⛔ 不动状态行
  检查触发：写完带 what／who／whatever 的从句，回头只看一眼那个从句里的动词有没有跟主语的数对上
- 2026-09-10 ⚪ 新题 bank:956 自由产出（P3）· `car exhaust, especially from older vehicles …, definitely **worsen** air quality`
  主语是 car exhaust（不可数、当单数）⇒ 动词跟单三：worsen → **worsens**。
  ★ 执行自查通过（§3.4）：同一篇里 `industry **is** the primary source` 她自己改对了 ⇒ 会，只是检查没跑
  ⇒ 只记 ⚪，⛔ 不记 ❌、⛔ 不动状态行
  检查触发：主语和动词中间隔了一长串插入语时，回头把插入语盖住、只看主语和动词对不对得上
- 备注 孤立测 100% 会 ⇒ 检索失败，不 drill，只加产出时检查触发
- 备注 ⚠️ **c 段待办（2026-08-27 提出，等她裁，不擅自改）**：本条日志里那次
  `it help me clear my head` 记的是 **❌**（当时的口径是"自由产出照常记 ❌"），
  但她 **08-25 定的 §3.4⑤b** 是"形态类**在哪儿掉都只记 ⚪**、不计入真错数"。两者冲突 ⇒
  那次 ❌ 要不要按新规则一并撤销、累错从 7 降到 6、连错重算？
  ★ 同类可能还有别的条目（#4 #7 #12 等形态类的历史 ❌）⇒ 一并列进 c 段问她
  ★★ **2026-08-31 c 段结案：已被规则回答，答案是"不动"，一个数字都没改。**
    SKILL §3.4⑤ 原文：「★★★ **历史不回扫**：08-25 之前记下的 ❌／连错／累错／"顽固"标记
    **一律原样保留**，不撤销、不重算 —— 只当历史读，不再驱动任何出题」
    ⇒ 本待办问的正是"要不要撤销/重算"，规则答的就是"不撤销、不重算" ⇒ 结案。
    ⛔ 教练**没有替她裁**：执行方向是保守的那一侧（什么都不动），且这个数改不改都不影响出题
      （形态类本来就不进复习组）。她要翻随时翻。
    ★ 今天的旁证：本条在 08-31 a 段第 2 组低压中译英里**两个动词的 -s 同时中**
      ⇒ "累错 7"本来就不是"她不会"的证据，正是 §3.4 说的"产出时检查没跑"。

- 备注 孤立测 100% 会 ⇒ 检索失败，不 drill，只加产出时检查触发
- 备注 2026-08-19 上午 `every one nedd to sign in`——单词拼残，判不出她想写 need 还是 needs
  ⇒ 当时不记档位（假错代价大于漏错）；欠的那一次**在当天新题里补上了**（见上一行）

### 12 · 时态判断触发（看中文时间标记词；过去的习惯用 used to/would）
类型 语法 ｜ 旧号 B34
状态 连对0 连错1 上次2026-08-19 未毕业 ｜ **累错 6** ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 产出验
　　★ 历史 ❌ 不回扫；累错 6 原样保留，只当历史读。以后掉了只追加 ⚪ 一行

**问题是什么**
**时态判断触发**：中文里的时间标记词（了／结果／以前／昨天／上次／那天／Back then）就是"把谓语落到过去"的开关；
**过去的习惯**用 **used to** ／ **would** ＋ 原形（I **used to** go to the gym ｜ we **would** play football）。
同一格里的邻居（别串）：used to／would ＝ 过去反复做的事 · 一次性的过去 ⇒ 直接过去式（gave · hung · enjoyed · rose · waited）。
判据一句话：中文里有没有时间标记？有 ⇒ 这一句的**每一个**谓语都要落到过去，不是只改第一个。
★ 与 #156 的分界（2026-08-28 写明，免得混）：#156 **不是形态类** ⇒ 照常记 ❌／回潮；
　本条 **是形态类** ⇒ 按她 2026-08-27 的裁定只记 ⚪ —— 分界来自她定的规则，不是教练临场判断。

**怎么发现的**
旧 B 表迁移（B34，2026-08-18），原始触发原话未存；最早记录 2026-08-11 ❌（连错五天）。
2026-08-19 一天三次同一形状：复习 #66 句 "全场观众都笑**了**" → `all the audience laugh`（过去式没标）；
`I want to buy a pack of napkins and there is a promotion`（中文"结果…"是已发生）；第 6 组 `sales go up`。
此后同一形状一路数到第 6 次：08-24 `he give me a lot of advice.` ／ 08-26 新题 bank:244 P2
`Back then, we hang out in the computer club and mess around building little program.` ／
08-27 与 08-28 同一道题面连续两天 `I really enjoy my time with him that day.`
2026-08-27 她定："标记下就行了，不出题，只记录" ⇒ 转形态类、⛔ 不再出题。

**我错在哪**
她的：`Back then, we **hang** out … and **mess** around …`　　正确：we **hung** out … and **messed** around …
检查触发：中文里出现"了／结果／以前／昨天／上次"⇒ 英语的谓语必须落在过去
（08-19 一天三次都是这个形状：sales go up ／ audience laugh ／ I want…there is）
· 句首出现 Back then／那时候／以前 ⇒ 回头扫这一句的**每个**谓语，全部落到过去（08-26 沿用）
· 句子里出现 that day／yesterday／last …／当年 ⇒ 回头看动词标没标过去（08-28 复述）

**题面**
不出中译英题（题型 产出验 ＋ 形态类·只记录）；挂自由产出抓：中文时间标记在场、英语谓语却停在现在时；过去的习惯没用 used to／would。
★ 原题面（留档，⛔ 不再发题）："我以前常去健身房。"

- 2026-08-11 ❌
- 2026-08-12 ❌
- 2026-08-13 ❌
- 2026-08-15 ❌
- 2026-08-16 ❌
- 2026-08-17 ✅
- 2026-08-19 ✅ `I used to go to the gym.`（连错五天后连对两次）
- 2026-08-19 ❌ 同日复习#66 句里 · "全场观众都笑**了**" → `all the audience laugh`（过去式没标）
  ｜同日第三次：`I want to buy a pack of napkins and there is a promotion`（中文"结果…"是已发生）
  ⇒ 一天里三次都是"中文有 了／结果，英语停在现在时" —— **次日给本条一次专门的 cold 测**
  ⇒ 按"同一天先对后错、两次都是 cold 以最后一次为准" ⇒ 本日记 ❌，连对清零
  （同日第 6 组 `sales go up` 也是同一类，但那句脱离上下文能当泛述读，只提醒未记）
- 2026-08-24 ⚪ **只做记号** · 复习第1组 #270 句里 · "他给**了**我很多建议" → `he give me a lot of advice.`
  → **He gave me** a lot of advice.
  ⇒ 本条 `形态类·不召回`，按 §3.4⑤／§3.3 **中译英复习里掉了只做记号：不记 ❌、不掉毕业、状态行不动**
  ｜ 同一形状第 4 次（08-19 三次 ＋ 今天）：中文"了"在场、英语谓语停在现在时
- 2026-08-26 ⚪ **只做记号** · 自由产出（新题 bank:244 P2）·
  `**Back then**, we **hang** out in the computer club and **mess** around building little program.`
  → we **hung** out … and **messed** around …
  ⇒ 同一形状第 5 次：**时间标记在场（Back then），英语谓语停在现在时**。
    本条 `形态类·不召回`，按 §3.4⑤b **在哪儿掉都只记 ⚪**：不记 ❌、不掉毕业、不计入当篇真错数
  ★★ **同一篇里一对一错，正反两证齐了**：
    · 对 —— `we **would** play football or just wander around the neighborhood`
      （would 说过去的习惯，正是本条标题的后半"过去的习惯用 used to/would"）
    · 错 —— 上面那句
    ⇒ 不是不会，是产出时检查没跑（§3.4 判据的教科书例子）
  ★ 检查触发（沿用，不新增）：**句首出现 Back then／那时候／以前 ⇒ 回头扫这一句的每个谓语，
    全部落到过去**
- 2026-08-27 ⚪ **只做记号** · 付息日 a 段 · 复习 #301 句里 ·
  "**那天**跟他待着我挺开心的" → `I really **enjoy** my time with him that day.`
  → I really **enjoyed** my time with him that day.
  ⇒ **同一形状第 6 次**：中文时间标记词在场（"那天"），英语谓语停在现在时。
    本条 `形态类·不召回`，按 §3.4⑤（中译英复习里掉了）**只做记号：不记 ❌、不掉毕业、状态行不动**
- 2026-08-28 ⚪ **只做记号** · 复习第3组 #301 句里 · `I really **enjoy** my time with him that day.`
  → enjoyed。**同一道题面、连续两天、同一处漏**（08-27 也是 enjoy ＋ that day）
  ★ 与同日 #156（同根词形"重说退回"判 ❌ ＋ 回潮）的分界，写清楚免得以后自己混：
    #156 **不是形态类** ⇒ 照常记 ❌／回潮 ｜ 本条 **是形态类** ⇒ 按她 2026-08-27 的裁定只记 ⚪。
    分界来自**她定的规则**，不是教练临场判断
  ★ 检查触发（复述）：句子里出现 that day／yesterday／last …／当年 ⇒ 回头看动词标没标过去
- 2026-08-31 📝 付息日 a 段第 2 组 · 她 08-31 临时指令重测（形态类不推进连对）
  `I used to go to the gym.`
  考点命中：过去的习惯 → used to ＋ 原形。⇒ 状态行一个字不动
- 2026-09-09 ⚪ 复检第 4 组 [6] · `I wait for hours`（"我等了很久"）—— 中文时间标记"了"没触发过去式
  ★ 形态类只记不判（§3.4②）：同一篇里她 `was built`／`I walked`／`actually was` 三处过去式都做对了
  ★ 检查触发：写完带时间标记（了/昨天/去年/上次）的句子，回头看一眼动词标没标过去
- 2026-09-10 ⚪ 复检第 3 组 · #24 `sales rise by 20%`
  中文"销量涨了 20%"是已完成的事实 ⇒ 英文该用过去式 **rose by 20%**。
  ★ 形态类（本条状态行带形态类·不召回）⇒ 只记 ⚪，⛔ 不判档位、⛔ 不动状态行
  检查触发：中文里出现"了／过／上个月／去年"这类完成或过去标记，回头看英文动词有没有跟着变过去式

### 56 · visual effects 恒复数；可数名词单数必须带限定词
类型 语法 ｜ 旧号 B79
状态 连对1 连错0 上次2026-08-17 未毕业 ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 产出验
　　★ 历史判定不回扫；以后掉了只追加 ⚪ 一行，不判档位、不动状态行

**问题是什么**
旧号 B79 迁来的捆绑条，两件事焊在一条里（未拆）：
· **visual effects** 恒复数 —— 说"视觉效果"只有复数形（it mainly comes down to visual effect**s**）
· **可数名词单数必须带限定词** —— 单数可数名词左边一定有一个词（a／the／my／this），⛔ 不许光秃秃地用
同一格里的邻居（别串）：泛指裸复数本来就对（older people · These small companies），不要一见复数就改。
⚠️ 与 #63 的分工（09-04 写明）：她**多加了一个 the** ⇒ 归 #63（泛指／特指）；
　**一个限定词都没有** ⇒ 归本条。同一处 ⛔ 不双记。
判据一句话：写完一个单数可数名词，它左边有没有一个词？没有 ⇒ 要么补限定词，要么改成复数。
★ 本条是**形态类**（她 2026-08-27 定）：检查跑了就对（08-28 漏的那个 a，08-29 同一道题自己补上了）⇒ 在哪儿掉都只记 ⚪。

**怎么发现的**
旧 B 表迁移（B79，2026-08-18），原始触发原话未存；最早记录 2026-08-15 ❌；
2026-08-16 ❌ 自由产出 `one of old classmates` ／ `watching event`。
之后同一形状反复出现：08-28 复习第2组 #306 句里 `relaxing in **different environment**`；
09-04 复习第 1 组 `older people often ask **younger generation** for advice`。
2026-08-27 她定："标记下就行了，不出题，只记录" ⇒ 转形态类、⛔ 不再出题。

**我错在哪**
她的：`relaxing in **different environment**` ／ `ask **younger generation** for advice`
正确：in **a** different environment ／ ask **the** younger generation
检查触发：写完可数名词单数，看它前面有没有 a／the／my（同 #150 一起扫）

**题面**
不出中译英题（题型 产出验 ＋ 形态类·只记录）；挂自由产出抓：visual effect 用成单数；单数可数名词左边一个限定词都没有。
★ 原题面（留档，⛔ 不再发题）："主要是看视觉效果。"

- 2026-08-15 ❌
- 2026-08-16 ❌ 自由产出 `one of old classmates`／`watching event`
- 2026-08-17 ✅
- 2026-08-28 ⚪ **只做记号** · 复习第2组 #306 句里 · `relaxing in **different environment**`
- 2026-08-29 ⚪ **正面记号** · 复习第1组 #306 句里 · `relaxing in **a** different environment`
  ——**同一条题、隔一天，08-28 漏的那个 a 今天自己补上了** ⇒ 同 #150，属"检查跑了就对"
  → in **a** different environment。§3.4 执行自查：同一组里 a few key things／a real alternative／
  a bit of practice 全部带限定词 ⇒ 一律 ⚪，不记 ❌、不动状态行
- 2026-08-31 📝 付息日 a 段第 2 组 · 她 08-31 临时指令重测（形态类不推进连对）
  `it mainly comes down to visual effects.`
  考点全中：visual effect**s** 恒复数 ＋ 无裸用的可数单数。
  顺带全对一处：comes down to（"归根到底看…"）。⇒ 状态行一个字不动
- 2026-09-04 ⚪ 复习 · 第 1 组 · 同句第二处（本条只记录·不出题）
  `older people often ask **younger generation** for advice` → **the** younger generation
  ⚪ 形态类（§3.4②）：不记 ❌／不动状态行／不进复习池／不计入本组真错数。
  ★ §3.4 执行自查（落 ❌ 之前必跑）："同一篇里她有没有把同一个形态做对过？"
    **有，四处**：`These small companies`（限定词＋数一致）· `the government`（特指带 the）·
    `The account`／`The login page`（特指带 the）· `older people`（泛指裸复数正确）
    ⇒ 一律 ⚪。
  ★ 挂 #56 不挂 #63 的理由：她不是**多加了一个 the**（那才是 #63 管的泛指/特指），
    是**一个限定词都没有** ⇒ 正对 #56「可数名词单数必须带限定词」。
    若走 #63 路线修，出口是 `younger generations` 复数 —— 也合法，但那是另一条路，
    不是最小修改；同一处 ⛔ 不双记。
  ★ 检查触发（复述给她的那句）：写完一个单数可数名词，回头看它左边有没有一个词
    （the/a/my/this）。没有 ⇒ 要么补限定词，要么改成复数。
- 2026-09-15 ⚪ 新题 bank:1059 · `being classmate` → classmates —— 形态类只记录（§3.4②），同篇 programs／problems／capabilities 都对


### 63 · 泛指 vs 特指：泛指不带 the（可数就用复数），特指才带 the
类型 语法 ｜ 旧号 B86＋B249＋B195
状态 连对0 连错2 上次2026-08-20 未毕业 ｜ **顽固** ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 产出验
　　★ 历史 ❌ 与"顽固"标记原样保留、不回扫；以后掉了只追加 ⚪ 一行

**问题是什么**
**泛指不带 the**（可数就用复数），**特指才带 the**（或 my／their）。
同一格里的邻居（别串）：
· 最高级天然唯一 ＝ 特指 ⇒ 必须带 the（**the** latest iPhone）
· wrong／right 前面几乎永远是 the —— "对的那个"只有一个（the wrong version · the right way）
· **the same** ＝ 特指，必须带 the（share **the** same interests · on **the same** wavelength）
· 物质名词 traffic 带不带 the 都成立（`Traffic was terrible this morning` 母语者照说）⇒ ⛔ 不许拿本条判它错
判据一句话：方向由**指称**定，不由词性定 —— 08-19 那天三处方向各不相同
（`the job` 泛指该去掉 the · `flowers` 她自己养的那些该带 the · `toys` 该带 their），
说明不是规则不会，是产出时"这个名词指哪一个"没检查。
⚠️ 与 #56 的分工（09-04 写明）：**多加了一个 the** ⇒ 本条；**一个限定词都没有** ⇒ #56。同一处 ⛔ 不双记。
★ 本条是**形态类**（她 2026-08-27 定）⇒ 在哪儿掉都只记 ⚪；"顽固"与连错 2 原样保留，只当历史读。

**怎么发现的**
旧 B 表迁移（B86＋B249＋B195，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅（原 #112）。
2026-08-19 ❌ **档位更正**（原记 ⚠️，合并后改判）：一天里三处指称全掉 —— `the job` ／ `flowers` ／ `toys`。
2026-08-20 ❌ 加练新题 bank:927 自由产出 · `a lastest iPhone`——该 **the** latest ⇒ 连错 2。
2026-08-27 她定："标记下就行了，不出题，只记录" ⇒ 转形态类、⛔ 不再出题。

**我错在哪**
她的：`the relationship online is a bit more fragile.` ／ `share same interests` ／ `a lastest iPhone`
正确：online relationships are a bit more fragile ／ share **the** same interests ／ **the** latest iPhone
检查触发：写完名词回头问一句"我说的是**这一个**，还是**这一类**？"
　这一类 → 不带 the（可数就用复数）｜ 这一个 → the／my／their
· 写完 the ＋ 复数名词，问一句"是前面提过的那几个吗？"不是就把 the 去掉（09-10 新增）
· 写完 wrong／right，回头看一眼 —— 前面是 the 吗？（09-01 新增）
· 写完一个"泛泛说一类"的可数名词，回头看一眼旁边那几项是不是复数（09-01 新增）

**题面**
不出中译英题（题型 产出验 ＋ 形态类·只记录）；挂自由产出抓：泛指多带了 the ／ 泛指没用复数 ／ 特指漏了 the。
★ 原题面（留档，⛔ 不再发题）："法规和执行都很重要。" ／ "今天早上路上特别堵。"／"成都的交通一直不好。"

- 2026-08-12 ✅（原 #112）
- 2026-08-16 ✅（原 #112）
- 2026-08-17 ✅ 首次进流 ｜同日原 #160 也 ✅（08-19 回补：迁移时误写"未测过"，📊 08-17 ✅ 里有 B86）
- 2026-08-19 ❌ **档位更正**（原记 ⚠️，合并后改判）：一天里三处指称全掉 ——
  `the job`（泛指工作该不带 the ＝ work）· `flowers`（她自己养的那些，该带 the）·
  `toys`（该带 their）。三处方向不同 ⇒ 不是规则不会，是产出时"这个名词指哪一个"没检查
- 2026-08-20 ❌ **自由产出**（加练新题 bank:927）· `a lastest iPhone`——该 **the** latest
  ⇒ **最高级天然唯一 ＝ 特指**，必须带 the。连错2
- 2026-08-31 📝 付息日 a 段第 2 组 · 她 08-31 临时指令重测（形态类不推进连对）
  `Both regulations and enforment are important.` ／ `Traffic was crazy heavy this morning.` ／
  `Traffic in Chengdu has always been terrible.`
  三句指称考点全中：泛指复数不带 the ｜ 物质名词裸用 ｜ 泛指 ＋ 后置限定不带 the。
  ★ b 句差点误判 ❌（"特指该带 the"），当场自我推翻：traffic 作物质名词带不带 the 都成立
    （`Traffic was terrible this morning` 母语者照说）⇒ 假错代价 > 漏错。
  enforment 属拼写，不计错。⇒ 状态行一个字不动（连错2／顽固 按 §3.4⑤ 原样保留）
- 2026-08-31 ⚪ 付息日 d 段 · 重答 R8 · **形态类只记 ⚪**（§3.4②：不记 ❌／不动状态行／不计入本篇真错数）
  `**the relationship online** is a bit more fragile.`
  泛指所有网上的关系 ⇒ 该用**复数、不带 the**（online relationships are …）——正是本条的判据。
  ★ §3.4 执行自查已跑：同一篇里 `new friends`／`online friends` 两处裸复数都对
    ⇒ 不是不会，是产出时那道检查没跑 ⇒ 确认走 ⚪。
  ⇒ 状态行一个字不动
- 2026-09-01 ⚪ 新题 P3（bank:490 · What are the rules people should obey at work?）· 第 1 记（同篇共两记）
  `There are some common rules, like turning up on time, meeting your **deadline**, and getting along
  with your colleagues.` → meeting your **deadlines**
  形态类（泛指用复数），按 §3.4② 只记 ⚪：不记 ❌／不判档位／不动状态行／不计入本篇真错数。
  ★ §3.4 执行自查已跑：**同一篇里她把同一个形态做对过** ——
    `common rules`／`your colleagues`／`place orders`／`problems` 复数全对，就这一项落单
    ⇒ 硬规则「有 ⇒ 一律 ⚪，不许记 ❌」。
  ★ 检查触发：写完一个"泛泛说一类"的可数名词，回头看一眼旁边那几项是不是复数。
- 2026-09-01 ⚪ 新题 P3（bank:490）· 第 2 记（同篇共两记，§3.3「同一条同一天被产出多次 ⇒ 每次各记一行」）
  `because the developer released **a** wrong version.` → released **the** wrong version
  形态类（特指带 the），按 §3.4② 只记 ⚪：不记 ❌／不判档位／不动状态行／不计入本篇真错数。
  ★ §3.4 执行自查已跑：**同一篇里她把冠词做对过** ——
    `the developer`／`the team` 特指带 the，`a dress code`／`a new system version`／`a big one`
    泛指带 a，全对，就这一处落单 ⇒ 硬规则「有 ⇒ 一律 ⚪，不许记 ❌」。
  ★ 判据：wrong／right 前面几乎永远是 the —— "对的那个"只有一个，"错的那个"是相对它说的：
    the wrong bus ／ the wrong file ／ the wrong version。
    ★ 她**用对过的例子就在昨天那篇里**：08-31 R8 [S8] `you have to use it **the right way**` ✅。
  ★ 检查触发：写完 wrong／right，回头看一眼 —— 前面是 the 吗？
- 2026-09-04 ⚪ 新题第 2 道 · 形态类（本条只记录·不出题）
  `they are on the same wavelength and **share same interests**` → share **the** same interests
  ⚪ 形态类（§3.4②）：不记 ❌／不动状态行／不进复习池／不计入本篇真错数。
  ★ §3.4 执行自查这一次触发得最干净：**同一句里、隔 8 个词**，她刚写对
    `on **the same** wavelength` —— 一模一样的块 ⇒ 一律 ⚪。
  ★ 落本条的理由：`the same` ＝ 特指，必须带 the，正对本条"泛指不带 the，特指才带 the"；
    全档 grep "the same" ⇒ 无专条 ⇒ ⛔ 不新建（形态类新开号 ＝ 开一个永不出题的号）。
- 2026-09-07 ⚪ 留痕 · 复检第 5 组 [6]（#215 句 2）· `After kids played toys` → After **the** kids
  —— 那一次的孩子是特指 ⇒ 带 the。形态类（§3.4②）只记 ⚪。
  执行自查：同一组里她写出 `a job`／`a red light`／`the toys`／`two kinds` 全部正确 ⇒ 会，缺的是产出时的检查。
- 2026-09-10 ⚪ 新题 bank:956 自由产出（P3）· `especially from **the** older vehicles that don't meet emission standards`
  这里说的是"凡是老旧车"这一类（泛指），不是前面提过的某几辆 ⇒ 泛指用复数裸名词：older vehicles。
  ★ 形态类（本条状态行带形态类·不召回）⇒ 只记 ⚪，⛔ 不判档位
  检查触发：写完 the ＋ 复数名词，问一句"是前面提过的那几个吗？"不是就把 the 去掉
- 备注 合并 2026-08-19：#160（泛指一类东西用复数不带冠词）＋ #112（traffic 带不带 the）并入本条 ——
  三条问的是同一个问题；#112 那句"眼前这一份 vs 泛指这件事"正是本条的判据
- 备注 国家形容词 Chinese/Japanese（不是 China's）（原 #160）

### 89 · 加形容词说"哪一种"时回到 a（a diverse economy）
类型 语法 ｜ 旧号 B144
状态 连对0 连错1 上次2026-08-20 未毕业 ｜ **形态类·不召回**（冠词族，同 #63）｜ **回潮 2026-08-20**（08-20 当天毕业当天回潮）｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 产出验
　　★ 历史 ❌ 与回潮记录原样保留、不回扫；以后掉了只追加 ⚪ 一行

**问题是什么**
名词一带形容词、说的是"**哪一种**"，冠词就回到 **a**（the economy → **a** diverse economy）。
同一格里的邻居（别串）：in **a** short time · **a** really wide and long river · **a** small city。
判据一句话：这个名词前面新加了形容词、说的是"哪一种"⇒ 冠词回到 a／an，⛔ 不跟着上一句的 the 走。
★ 与 #63（泛指 vs 特指）的分工：本条是**冠词族里的一个子格**（状态行写明"冠词族，同 #63"）——
　只管"加了形容词 ⇒ 回到 a"这一步；指称到底是这一类还是这一个，归 #63。
★ 本条是**形态类**（她 2026-08-27 定）⇒ 在哪儿掉都只记 ⚪。

**怎么发现的**
旧 B 表迁移（B144，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅ 首次进流。
2026-08-19 ✅ `a diverse economy`——上一句是 the economy，加了形容词就回到 a，没被带跑。
2026-08-20 ❌ 自由产出（新题 bank:187）· `can get good feedback in short time` ⇒ **当天毕业当天回潮**。
2026-08-27 她定："标记下就行了，不出题，只记录" ⇒ 转形态类、⛔ 不再出题。

**我错在哪**
她的：`can get good feedback in short time`　　正确：`get good feedback in **a** short time`
检查触发：写完"形容词＋名词"，回头看前面有没有 a／an

**题面**
不出中译英题（题型 产出验 ＋ 形态类·只记录）；挂自由产出抓：名词带了形容词说"哪一种"，冠词却漏了 a／an。
★ 原题面（留档，⛔ 不再发题）："创业公司对多样化的经济很关键。"

- 2026-08-17 ✅ 首次进流
- 2026-08-19 ✅ `a diverse economy`——上一句是 the economy，加了形容词就回到 a，没被带跑
- 2026-08-20 ❌ **自由产出**（新题 bank:187）· `can get good feedback in short time`——该 in **a** short time
  ⇒ 名词一带形容词就回到 a。形态类，正是"只在自由产出里判"要抓的场景
- 2026-08-29 ⚪ 新题 P2 · **正面记号**（形态类只记号，不动状态行）·
  `**a** really wide and long river` ——加了形容词说"哪一种河"，冠词回到 a，做对了。
  同篇 `a small city` ／ `a hydropower station` ／ `the water` ／ `the sand` ／ `one of the mother rivers`
  全篇冠词一处不漏
- 2026-08-31 📝 付息日 a 段第 2 组 · 她 08-31 临时指令重测（形态类不推进连对）
  `start-ups are vital to a diverse economy.`
  考点命中：加形容词说"哪一种" → 回到 **a** diverse economy。⇒ 状态行一个字不动
- 2026-08-31 📝 付息日 d 段 · 重答 R9 · 本条今天第 2 行（形态类不推进连对，§3.4②）
  `Start-ups are vital to **a diverse economy**` —— 加了形容词说"哪一种" ⇒ 回到 a，考位命中。
  ⚠️ 同 #255：**同日 a 段第 2 组的原句复用**，不是独立证据。
  ★ 照 §3.3「同一天每一次各记一行」照常记，⛔ 不挑"以谁为准"。
  ⇒ 状态行一个字不动
### 93 · 不在那一小撮里的动词必须变形（sit→sat／sing→sang）
类型 语法 ｜ 旧号 B152b
状态 连对0 连错0 上次 — ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 产出验
　　★ 本条建立至今**从未被测过**，按本次裁决**今后也不出题** —— 只在自由产出里追加 ⚪ 记录

**问题是什么**
**不在"原形＝过去式"那一小撮里的动词，过去时必须变形**：sit → **sat** ／ sing → **sang** ／ buy → **bought**。
同一格里的邻居（别串）：过去分词 shown 只活在助动词后面（I haven't **seen**）；单独作过去式要用 **showed**。
判据一句话：这个动词在不在 put／cut／hit 那一小撮里？不在 ⇒ 必须变形。
★ 与 🎓#249（原形＝过去式的一小撮 put／cut／hit）的分工：同一条规则的两面 ——
　2026-08-19 判重结论**不并入 #249**（#249 已毕业不再召回，本条从未被测 ⇒ 并进去等于埋掉），保留、互相引用。
★ 本条是**形态类**（她 2026-08-27 定）⇒ 在哪儿掉都只记 ⚪。

**怎么发现的**
旧 B 表迁移（B152b，2026-08-18），原始触发原话未存；**建号至今从未被判定过**（状态行 上次 ＝ —）。
判重结论（2026-08-19）：不并入 🎓#249 —— 同一条规则的两面，但 #249 已毕业不再召回、本条从未被测，
并进去等于埋掉 ⇒ 保留本条，两边写互相引用。
2026-08-31 付息日 a 段第 2 组她 08-31 临时指令重测（形态类不推进连对）· `he sat on the couch all evening yesterday.` 考点命中。
2026-09-07 ⚪ 在池第 1 组 [10] · `he shown me` —— 本条第一次在自由产出里掉。

**我错在哪**
她的：`he shown me`（2026-09-07 在池第 1 组 [10]）　　正确：`he **showed** me`（shown 只活在助动词后面）
检查触发：过去的事，动词是不是变形了（sit→sat／sing→sang／buy→bought）

**题面**
不出中译英题（题型 产出验 ＋ 形态类·只记录）；挂自由产出抓：过去的事，动词还停在原形，或把过去分词当过去式用。
★ 原题面（留档，⛔ 不再发题）："坐在沙发上"（动词用过去式）

- 2026-08-19 📝 判重结论：**不并入 🎓#249（原形＝过去式的一小撮 put/cut/hit）**。同一条规则的两面，
  但 #249 已毕业不再召回，本条从未被测 ⇒ 并进去等于埋掉。保留，写互相引用
- 2026-08-31 📝 付息日 a 段第 2 组 · 她 08-31 临时指令重测（形态类不推进连对）
  `he sat on the couch all evening yesterday.`
  考点命中：sit → **sat**。★ 本条建号以来第一次被测（此前 上次 ＝ —）。
  ★ `all evening yesterday` 差点误判语序，当场自我推翻：all ＋ 时段 ＋ yesterday 是标准搭配。
  ⇒ 状态行一个字不动
- 2026-09-07 ⚪ 留痕 · 在池第 1 组 [10] · `he shown me` → `he showed me`
  —— shown 只活在助动词后面；同一组里 `he was two`／`I haven't seen` 都做对了 ⇒ §3.4 判形态类


### 147 · 时态只标一次：did/will/should/can/must 一出现，后面动词一律原形
类型 语法 ｜ 旧号 B236
状态 连对0 连错1 上次2026-08-20 未毕业 ｜ **顽固**（08-11/08-16/08-17/08-20 四犯） ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 产出验
　　★ 四犯记录与"顽固"标记原样保留、不回扫；以后掉了只追加 ⚪ 一行

**问题是什么**
**时态只标一次**：did／will／should／can／must 一出现，后面的动词一律**原形**。
同一格里的邻居（别串）：didn't **find** out · children will **lose** interest · couldn't **find** it ·
what did you **eat** yesterday · nor **did he tell**（倒装之后仍然是原形）。
判据一句话：这个谓语前面已经有 did／will／should／can／must 了吗？有 ⇒ 后面那个动词必须是原形。
★ 与 #10（主谓一致）／#54（比较级只标一次）／#92（否定别丢）同属一条元规则：
　**每个语法标记在一个谓语上只能出现一次，而且必须出现一次**。
★ 本条是**形态类**（她 2026-08-27 定）⇒ 在哪儿掉都只记 ⚪；四犯记录与"顽固"只当历史读。

**怎么发现的**
旧 B 表迁移（B236，2026-08-18），原始触发原话未存；最早记录 2026-08-16 ❌
`didn't FOUND out` ／ `children will LOST interest`。
2026-08-17 ❌ 第三次（教练当场讲完二十分钟后又犯）；
2026-08-20 ❌ 复习 #18 句里 `I still couldn't found it`——**第四次**；
2026-08-21 ⚪ 复习 #59 句里 `what did you ate yesterday`——第五次同型（中译英里不计 streak）。
2026-08-27 她定："标记下就行了，不出题，只记录" ⇒ 转形态类、⛔ 不再出题。

**我错在哪**
她的：`didn't FOUND out` ／ `children will LOST interest` ／ `I still couldn't found it`
正确：didn't **find** out ／ children will **lose** interest ／ I still couldn't **find** it
检查触发：句子里已经有 did／will／should／can／must ⇒ 后面的动词一律原形

**题面**
不出中译英题（题型 产出验 ＋ 形态类·只记录）；挂自由产出抓：did／will／should／can／must 后面的动词又变了形。
★ 原题面（留档，⛔ 不再发题）："他昨天没看见我，也没跟我说他要走。"

- 2026-08-16 ❌ `didn't FOUND out`／`children will LOST interest`
- 2026-08-17 ❌ 第三次（教练当场讲完二十分钟后又犯）
- 2026-08-19 ✅ 复习 · `he didn't see me yesterday and didn't say he was going to leave`（两个谓语都是原形）
- 2026-08-20 ❌ 复习#18 句里 · `I still couldn't found it`——**第四次**：could 之后又用了过去式
  ⇒ 印证 §3.4：孤立测她 100% 会，只有在她自己造句时才掉，所以只能在产出里判
- 2026-08-21 ⚪ **只做记号，不记档位**（她 08-21 定：形态类在中译英复习里掉了不记 ❌）
  复习#59 句里 · `what did you **ate** yesterday`——did 已经标了过去，动词该回原形 eat
  ⇒ 状态行不动（仍是 连对0 连错1）。**第五次同型**，但按新规则中译英里的不计入 streak
  ★ 今天新题（bank:434）里她没有 did/will/can 后面接变形的句子 ⇒ 自由产出里本条本日无对象
- 2026-08-31 📝 付息日 a 段第 2 组 · 她 08-31 临时指令重测（形态类不推进连对）
  `He didn't see me yesterday, nor did he tell me he was leaving.`
  考点全中：did**n't** see（原形）· nor **did he tell**（倒装后仍是原形）。
  ★ nor ＋ 倒装属 Band 7 上限结构，与本条考点同时做对。⇒ 状态行一个字不动
- 备注 自我分诊：单独问她"情态动词后面接什么"秒答"原形" ⇒ 不 drill，只加产出时检查触发
- 备注 与 #10 主谓一致／#54 比较级只标一次／#92 否定别丢合成一条元规则：**每个语法标记在一个谓语上只能出现一次，而且必须出现一次**

### 150 · 限定词必须跟后面名词的【数】一致（These statements／a group）
类型 语法 ｜ 旧号 B239
状态 连对0 连错2 上次2026-08-19 未毕业 ｜ **顽固** ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 产出验
　　★ 历史 ❌ 与"顽固"标记原样保留、不回扫；以后掉了只追加 ⚪ 一行

**问题是什么**
**限定词必须跟后面名词的【数】一致**：These statement**s** ／ many commuter**s** ／ three circle**s**（复数限定词配复数）·
**a** team（单数限定词配单数）。
同一格里的邻居（别串）：these／those／many／a lot of／two／three 这一类都是限定词，后面的名词必须跟着变复数。
判据一句话：写完限定词，立刻看后面那个名词的尾巴跟它对不对得上。
⚠️ 与 #56 的分工（09-04 写明）：本次**有**限定词、错在数不一致 ⇒ 本条；
　#56 管的是"单数可数名词裸奔、一个限定词都没有" ⇒ 不适用。
★ 本条是**形态类**（她 2026-08-27 定）：08-28 掉的那个 -s，08-29 同一道题她自己补上了 ⇒ 检查跑了就对。

**怎么发现的**
旧 B 表迁移（B239，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ❌。
2026-08-19 ❌ 复习 #103 句里 · "这些东西" → `the thing`（限定词和数一起塌）⇒ 连错 2。
之后同一形状：08-28 复习第1组 #286 句里 `many commuter will happily leave their cars`；
09-04 新题第 1 道 `pointed at three circle on it`。
2026-08-27 她定："标记下就行了，不出题，只记录" ⇒ 转形态类、⛔ 不再出题。

**我错在哪**
她的：`the thing`（中文"这些东西"）／ `many commuter` ／ `pointed at three circle on it`
正确：these thing**s** ／ many commuter**s** ／ three circle**s**
检查触发：写完 a／an／this／these（**加 many／a lot of／these 这一类**），立刻看后面那个名词的尾巴

**题面**
不出中译英题（题型 产出验 ＋ 形态类·只记录）；挂自由产出抓：限定词与名词的数不一致（these／many／three ＋ 单数名词，或 a ＋ 复数）。
★ 原题面（留档，⛔ 不再发题）："这些句子" ／ "一个队"

- 2026-08-17 ❌
- 2026-08-19 ❌ 复习#103 句里 · "这些东西" → `the thing`（限定词和数一起塌）
- 2026-08-28 ⚪ **只做记号** · 复习第1组 #286 句里 · `many commuter will happily leave their cars`
  → many **commuters**。§3.4 执行自查：同一篇里 their cars／materials／corners／folks 全部复数正确
  ⇒ 一律 ⚪，不记 ❌、不动状态行
- 2026-08-29 ⚪ **正面记号** · 复习第1组 #286 句里 · `many **commuters** will happily leave their cars at home`
  ——**同一条题、隔一天，08-28 掉的那个 -s 今天自己补上了** ⇒ 印证 §3.4 的判据：
    不是不会，是产出时检查没跑；跑了就对
- 2026-08-31 📝 付息日 a 段第 2 组 · 她 08-31 临时指令重测（形态类不推进连对）
  `these sentences are really simple.` ／ `The five of us formed a team.`
  考点全中：These ＋ 复数 sentence**s** ｜ **a** team（单数限定词配单数名词）。
  ⇒ 状态行一个字不动
- 2026-09-04 ⚪ 新题第 1 道 · 同句第二处（本条只记录·不出题）
  `pointed at **three circle** on it` → three **circles**
  ⚪ 形态类（§3.4②）：不记 ❌／不动状态行／不进复习池／不计入本篇真错数。
  ★ §3.4 执行自查："同一篇里她有没有把同一个形态做对过？"
    **有，五处**：`two factors`／`their ideas`／`little ones`／`kids`／`entertainment options`
    ⇒ 一律 ⚪。
  ★ 落本条不落 #56：本次**有**限定词（three），错的是限定词与名词的数不一致 ⇒ 正对本条；
    #56 管的是"单数可数名词裸奔、一个限定词都没有" ⇒ 不适用。
- 2026-09-15 ⚪ 新题 bank:1059 · `These day` → These days —— 形态类只记录（§3.4②）

### 167 · be in a hurry 的主语必须是人；There's no rush.
类型 搭配 ｜ 旧号 B256
状态 连对1 连错0 上次2026-09-15 未毕业 ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-19 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零。★ 今天回标成「题型 整句」才从词组串里单独拎出来 —— 旧口径按「类型 搭配」打包，主语根本不出现、考点永远测不到）

**问题是什么**
**be in a hurry 的主语只能是人**（I'm in a hurry ／ he's in a hurry）—— 事情和时间不会"赶"，
⛔ 不能说 It isn't in a hurry；"这件事不急"要换一个框：**There's no rush.**（＝ There's no hurry.）
一条规则两个落点：主语是人 ⇒ in a hurry ｜ 主语是"这件事" ⇒ There's no rush。
同一格里的邻居（别串）：`Take your time.` 完全合法，但它绕开了 There's no rush ⇒ 题面已把它排除。
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
"不用赶时间。" ／ "我赶时间，先走了。"（第一句用 **There's** 起头 · ⛔ 不许用 take your time）

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
- 备注 同族"块记了一半"：`stood on their feet`（该 be on your feet）

### 238 · move on ≠ move forward
类型 词汇 ｜ **合并条·出题多句覆盖**（§3.2c，2026-09-07 定：只出一句测不到这一对的分工）｜ 旧号 B184
状态 连对0 连错1 上次2026-09-15 未毕业 ｜ 题型 整句 ｜ **合并条·出题多句覆盖** ｜ **回潮 2026-09-15**（09-10 第二次毕业 → 09-15 复检答"忘了"，两个成员都没出来，撤销毕业、连对清零）
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
她的：2026-09-07 复检只给出 `move forward`，`move on` 一次没出现；2026-09-15 复检两句都答"忘了"
正确：`① It's all in the past, just move on. ② No matter what happens, the company still has to move forward.`
找法：先分一刀 —— 放下过去用 move **on**，事情往前推进用 move **forward**。

**题面**
★ 2 句，两个成员各一句 —— 本条考的就是这两个块的分工，只出一个等于没测
　① "都过去了，别老想着了。"（用 **move** 说）
　② "不管出什么事，公司还是得往前推进。"（用 **move** 说，"推进"是往前取得进展 · ⛔ 不许用 ahead）
　　★ 2026-09-07 题面整改（§6「题面必须唯一可判」）：原题面只有一句
　　★ "一直往前走"（用 move 说）—— move on 和 move forward **两个都套得上**，
　　★ 而本条的考点恰恰是这两个的分工 ⇒ 原题面结构上测不到自己的考点。

**成员出题账**
① move on ｜ 09-07 ❌ · 09-10 ✅ · 09-15 ❌
② move forward ｜ 09-07 ✅ · 09-10 ✅ · 09-15 ❌
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

### 282 · take ownership (of sth)（把它当成自己的事，自己扛起来）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对1 连错0 上次2026-09-15 未毕业 ｜ 题型 词组 ｜ **回潮 2026-09-11**（08-28 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零）

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
**点名**："把这事当成自己的事扛起来"（用 **take** ＋ 一个 **o-** 开头的名词说）

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

### 301 · enjoy ＋ 物主代词 ＋ time／stay（不说 enjoy the time）
类型 搭配 ｜ 新建 2026-08-26（**补建**）
状态 连对1 连错0 上次2026-09-15 未毕业 ｜ 题型 词组 ｜ **回潮 2026-09-11**（08-28 毕业 → 09-11 复检写成 `enjoy the time with him`，与 08-26 建号触发句一模一样，撤销毕业、连对清零）

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
**点名**："跟他待着挺开心"（用 **enjoy** 说，后面接"时光" · ⛔ 不许用 spending）

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

### 324 · other 是限定词、others 才是代词（happier than **others**）
类型 语法 ｜ 新建 2026-09-07
状态 连对0 连错0 上次 — 未毕业 ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题** ｜ 题型 产出验

**问题是什么**
**other 是限定词、others 才是代词**（happier than **others**）。
判据：
```
other  ＝ **限定词**，后面必须跟名词：other kids ／ other people ／ the other one
others ＝ **代词**（＝ other people／other ones），单独站着时用它：happier than **others**
★ 同一族：one／ones —— average kids and smart **ones**
★ 检查触发：写完 other，看它后面有没有名词。没有 ⇒ 加 -s。
```
⚠️ 与 #150 的分工：#150 管"限定词与名词的**数**不齐"；本条管"限定词后面**根本没有**名词"——
　按 #150 去改只会去找 other 后面那个名词的尾巴，而这句压根没有那个名词 ⇒ 产不出 others。
★ 本条是**形态类**（新建当天定）⇒ ⛔ 永不出题，在哪儿掉都只记 ⚪。

**怎么发现的**
2026-09-07 新建 · 首次留痕 · 新题第 1 道（自由产出 · bank:975）· 她的原话
`they are definitely happier than **other**`（→ happier than **others**）。
判重结论（§3.1 判重三步，2026-09-07 当天做，逐条人读）：**保留新建**
```
① 目标英文形式 ＝ 裸代词 `others`
② 全档 grep（含已毕业）：`grep -n "others\|than other" problems.md graduated.md methods.md`
   ⇒ 命中全部落在**别的条目的正文举例**里（🎓#106 的 get to know others ／
     另一条的 messaging with others）⇒ **全档无条目**管这一条。
③ 最接近的一条排除：#150（限定词必须跟后面名词的【数】一致，These statements／a group）——
   那条管"限定词与名词的数不齐"；本条管"限定词后面**根本没有**名词"。
   **决定性证据**：按 #150 的规则去改她这句 ⇒ 只会去找 other 后面那个名词的尾巴，
   而这句**压根没有那个名词** ⇒ 产不出 others ⇒ 不同考点。
④ 是不是拼写（§2.1）？不是 —— 少的是一个表"代词化"的 -s，不是把同一个词写歪。
⑤ 是不是伞形条目（§3.2b）？不是 —— 目标形式就一个 `others`。
```

**我错在哪**
她的：`they are definitely happier than other`　　正确：`happier than **others**`
检查触发：写完 other，看它后面有没有名词。没有 ⇒ 加 -s。

**题面**
不出中译英题（题型 产出验 ＋ ⚪ 形态类，不出题）；挂自由产出抓：other 后面没有名词却没加 -s（one／ones 同族一起扫）。

- 2026-09-07 ⚪ 首次留痕 · 新题第 1 道（自由产出 · bank:975）·
  `they are definitely happier than **other**` → happier than **others**
  ★ §3.4 自我分诊（省时版）：同一段里她把 `average kids and smart **ones**` 做对了
    ⇒ 同一个形态（裸代词要带 -s）她会 ⇒ 不是缺口，是产出时检查没跑 ⇒ 只记 ⚪、⛔ 不进召回队列。
- ⇒ 形态类：⛔ 永不出题（§3.4①），以后在任何地方掉了只追加一行 ⚪

### 330 · set one's mind to sth（下定决心要做的事）
类型 词组 ｜ 新建 2026-09-09
状态 连对1 连错0 上次2026-09-15 未毕业 ｜ 题型 词组

**问题是什么**
**set one's mind to sth** ＝ 铁了心要做成某事（强调持续用力）；
常见形 `do what he set his mind to`（介词 to 留在句尾，后面不再挂东西）。
同一格里的邻居（别串）：⛔ 不是 make up one's mind（那是"拿定主意"＝ 一次性的选择，做完就结束）；
题面另外排除 decide／determined。
判据一句话：说的是"铁了心一直干下去"⇒ set one's mind to；只是"当场拿定主意"⇒ make up one's mind。

**怎么发现的**
2026-09-09 新建 · 新题 bank:1091 自由产出（P2）· 她自标"这个短语也是查字典的"。
判重结论 全档 grep `set his mind\|mind to` 零命中（graduated.md:3810 那条是 many suggestions 的可数性，不同考点）⇒ 保留
2026-09-10 ✅ 复习 · 在池第 2 组首测 · `He did what he set his mind to` —— set his mind to 一字不差，介词 to 留在句尾。

**我错在哪**
她的：当场查字典才写出来（2026-09-09 自标；⛔ 不是产出错）　　正确：`do what he set his mind to`
找法：中文"下定决心要做"先分一刀 —— 是"一直往下干"（set one's mind to），还是"当场拿定主意"（make up one's mind）？

**题面**
"他下定决心要做的那件事"（"下定决心要做"用 **mind** 说 · ⛔ 不许用 decide／determined／make up／put）

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

### 335 · take action（action 在这个块里不可数，⛔ take actions）
类型 语法 ｜ 新建 2026-09-11（从 #261 拆出）
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ 题型 整句

**问题是什么**
**take action** 是固定块，action 在这里**不可数** ⇒ ⛔ 不加 -s、⛔ 不加 an。
同一格里的邻居（别串）：同族的 take **steps**／take **measures** 才有复数（steps／measures 本身可数）
⇒ 题面已排除，免得白测；中文"更愿意干"口语更常走 **more willing to give it a go／to go for it**，take action 偏"采取行动"。
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
"风险小了，大家就更愿意干。"（"更愿意干"用 **take ＋ 一个名词** 说 · ⛔ 不许用 steps／measures／plunge／chance）

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

### 336 · get TO ＋ 地点（到达；⛔ get the destination）
类型 搭配 ｜ 新建 2026-09-11
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ 题型 词组

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
"到目的地怎么走"（"到"用 **get** 说）

- 2026-09-11 📝 新建 · 付息日 d 段重答 R10（P3 · How does technology help people make plans?）· 触发原话
  `like how to get the destination, where to live, and which restaurants are good.`
  条目内容：**get to ＋ 地点** ＝ 到达（get to the station／get to work／get to the destination）；
    home／there 是副词，⛔ 不带 to（get home／get there）。
    get 直接带宾语是"拿到／得到"（get a ticket／get the message）—— 漏了 to，句子就成了"拿到那个目的地"。
  ⚠️ 同一句里 `where to live` 是 🎓#86 后半格（where to STAY）掉了 ⇒ 那条回潮，⛔ 不归本条。
  检查触发：写完 get ＋ 一个地点名词，回头看中间有没有 to。
- 2026-09-13 ✅ 学习日 在池第 3 组 · 首测 · `how to get to your destination`——get **to** ＋ 地点（09-11 掉的那个 to 回来了）

### 339 · reach sb（联系上；直接带宾语，⛔ get reach sb）
类型 词组 ｜ 新建 2026-09-13 ｜ 与 🎓#130 互斥（那条考 can／be able to，本条考 reach 的形）
状态 连对1 连错0 上次2026-09-15 未毕业 ｜ 题型 词组

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
"白天电话联系不上她"（"联系上"用 **reach** 说）

- 2026-09-13 ❌ 首犯 · 学习日 复检第 4 组 [9]（#130 那题）· `I'v not been able to get reach hime.`
  最小改 `I haven't been able to reach him.`
  ❌ reach 直接带宾语，⛔ 前面不套 get；带 get 的是 get hold of／get in touch with／get through to
  ★ 判重：dedup "reach"／"get in touch" ⇒ 无同考点条目；#130 题面同句但考 be able to ⇒ 互斥并存
- 2026-09-15 ✅ 学习日 在池第 2 组 · `We couldn't reach him during the day.` —— reach 直接带宾语；连错1 → 连对1

### 340 · a step up from that（递进到更高一档；⛔ on top of that 是平级追加）
类型 词组 ｜ 新建 2026-09-13 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-09-15 未毕业 ｜ 题型 词组

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
"再往上一档"（用 **step** 说 · ⛔ 不许用 on top of／plus）

- 2026-09-13 新建 · 新题 bank:238（P3）· 她点名要学 · `But stepping it up a bit, things like showing up on time …`
- 2026-09-15 ✅ 学习日 在池第 2 组 · `a step up from that.` —— 首测一字不差；连对1

### 341 · deserve praise／credit（⛔ worth praise）
类型 搭配 ｜ 新建 2026-09-13
状态 连对1 连错0 上次2026-09-15 未毕业 ｜ 题型 词组

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
"这种做法值得表扬"（⛔ 不许用 worth／should）

- 2026-09-13 ❌ 首犯 · 新题 bank:238（P3）· `are totally worth praise`
  最小改 `totally deserve praise`
  ❌ worth 后面挂"值那个价"的东西（worth the money／worth a try／worth praising）；"值得表扬"这种"该得到的"用 deserve
- 2026-09-15 ✅ 学习日 在池第 2 组 · `This approach deserves praise.` —— deserve praise；连错1 → 连对1

### 343 · **opening hours**／business hours（营业时间；⛔ open time）
类型 词组 ｜ 新建 2026-09-15
状态 连对0 连错1 上次2026-09-15 未毕业 ｜ 题型 词组

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
"营业时间"（两个词的块 · ⛔ 不许用 time）

- 2026-09-15 ❌ 首犯 · 学习日 在池第 2 组 [4]（#337 题）· `look up the open time`
  最小改 `look up the opening hours`
  ❌ "营业时间"是固定块 opening hours／business hours；open time 不是一个块

### 344 · drive over／come over（到我这边来；⛔ drive here）
类型 词组 ｜ 新建 2026-09-15 ｜ ⭐ 她点名要学
状态 连对0 连错0 上次— 未毕业 ｜ 题型 词组

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
"他开车过来了"（"过来"用一个小词挂在动词后面 · ⛔ 不许用 here／to my place）

- 2026-09-15 新建 · 新题 bank:1059（P2 · cold）· 触发原话 `He drove here and started debugging using his own device` · ⭐ 她点名要学

### 345 · 在哪台机器上干活 ＝ on ＋ 具体机器（on his own laptop；⛔ using his device）
类型 搭配 ｜ 新建 2026-09-15 ｜ ⭐ 她点名要学
状态 连对0 连错0 上次— 未毕业 ｜ 题型 词组

**问题是什么**
在某台机器上做事，介词用 **on** ＋ 那台机器的**具体名字**：on his own laptop ／ on my phone ／ on the office computer。
⛔ 不说 using his device —— device 是书面／技术档，口语只说具体是哪台。
同一格里的邻居（别串）：软件、平台也走 **on**（on Zoom ／ on Excel）· **in** 用在"在某个系统／应用里面"（in the app）·
**with** 用在手持工具（with a screwdriver）。
判据一句话：机器或平台 ⇒ **on** ＋ 具体名字；⛔ 不用 device 这种统称、⛔ 不用 using 起头。

**怎么发现的**
2026-09-15 新题 bank:1059（P2 · cold）：她写 `started debugging using his own device`。
教练在 diff-2 给了 on his own laptop，她点名要学（原话同 #344）。
查重（§3.1 判重三步）：
　① 目标形式 dedup "laptop"／"device"／"on my phone" ⇒ laptop 只命中 🎓#74（make do with）与 🎓#302（something breaks），两条都是正文里带 laptop 的例句 ⇒ 否；另两个零命中
　② 中文 "用…电脑" 无对应条目 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`using his own device`　　正确：`**on** his own laptop`
找法：写完 device／equipment 这类统称，先问"具体是哪台？"换成 laptop／phone／computer，介词用 on。

**题面**
"他用自己那台笔记本调试"（"用…那台机器"用一个介词说 · ⛔ 不许用 using／with／device）

- 2026-09-15 新建 · 新题 bank:1059（P2 · cold）· 触发原话 `started debugging using his own device` · ⭐ 她点名要学

## 迁移说明（2026-08-18）

```
来源      coach/fluency_lab.md 的 B 表 288 行（287 个唯一号）＋ 9 行 📊 事件流（08-09→08-17）
本表      253 条 ＝ 未毕业 164 ＋ 🎓 已毕业 89　｜　methods.md 35 条方法类（不召回）
          ★ 08-19 二次整理：原来分出去的"已毕业"文件（83 条）证明只被读不被用，已删除；
            #173–#253 就是它写回来的 81 条（题面从旧 B 表逐条取回，事件流抄成日志行），
            #54 也从墓碑行还原；G79（同位语·旧账）与 #1 同考点，只在 #1 加了一条备注
拆条      B52（六句补录）按 Q4 拆成 #28–#33；其余一号一条
不迁移    父号 B57/B107/B109/B114/B117/B147/B152/B161/B171/B191/B207/B31（已拆，本身不出题）
          B190/B209（共享判据，不占槽位）· B171※（题面已分给各号）· B105（口语作废，只在写作有效）
          B214（已移入表达库，不出题）
旧账      2026-08-09 之前的记录不在事件流里；标「旧账」的条目连击可能偏低，遇到时按实际重测
```

