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


### 32 · There's no point regretting it now.（比 It's no use 更常用）
类型 结构 ｜ 旧号 B52⑤
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-21 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零）

**问题是什么**
**There's no point ＋ -ing** ＝ 做这件事没意义（比 It's no use 更常用）。
同一格里的邻居（别串）：加 in 也对（There's no point **in** regretting it now.）·
⛔ 不是 There's no point **to do** · ⛔ 不是 It's no use（题面已把它排除掉）。
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
**点名**："现在后悔也没用。"（用 **There's** 起头的那个框说，⛔ 不许用 It's no use · ⛔ 不许用 use）

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

### 34 · in groups（小组）≠ in pairs（两人一组）
类型 词组 ｜ 旧号 B53
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ 题型 词组 ｜ **回潮 2026-09-11**（08-20 毕业 → 09-11 复检写成 `get paired in groups`，把 paired 与 groups 焊在一起 ＝ 正中本条要分开的那两个词，撤销毕业、连对清零）

**问题是什么**
**in groups**（以小组为单位）≠ **in pairs**（两人一组）——
**pair ＝ 两个人配成一对**，**group ＝ 三个人以上的小组**，这一组区分就是本条考点。
同一格里的邻居（别串）：in groups ／ in pairs 都是【介词 ＋ 名词复数】的裸块；
要带动词说 ⇒ get put into groups ／ split into groups；⛔ 题面排除 form groups ／ get into groups。
判据一句话：几个人？两个 ⇒ in pairs；三个以上 ⇒ in groups。

**怎么发现的**
旧 B 表迁移（B53，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ◎（题面没逼出，form groups／get into groups 都合法 → 当天改点名）。
2026-08-19 ✅ `working in groups is better than working alone`；2026-08-20 ✅ 复习 `the teacher get the students to work in groups.` ⇒ 毕业。
2026-09-11 付息日 a2 第 3 组复检：她写 `get paired in groups` —— 把 paired 与 groups 焊在一起 ⇒ **回潮**。

**我错在哪**
她的：`get paired in groups`（字面成了"被两两配对成小组"，自相矛盾）　　正确：`get put in groups`（只译这个块 ⇒ `in groups` 就够）
找法：说"分组"之前先数人数 —— 两个人才是 paired／in pairs，三个人以上一律 in groups。

**题面**
**点名**："以小组为单位"（用【介词＋名词复数】说，⛔ 不许用 form groups／get into groups · ⛔ 不许用 teams）

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

### 49 · 人称一致：一句里、一段里都不能跳（统一 I 或统一 you）
类型 结构 ｜ 旧号 B71＋B78
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-20 毕业 → 09-05 复检 ✅ → 09-11 复检答"忘了"，撤销毕业、连对清零）

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
"喜欢做饭，因为一步步来，最后有东西拿得出手。" ／ "在电影院能完全沉浸进去，还能跟另一半当成约会。"（两句中文都省了主语 —— 自己定人称，一句之内不许跳）

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
- 备注 08-05 一天内跳了 3 次（原 #55）
- 备注 合并 2026-08-19：#55（人称一致·一段里）并入本条 —— 同一条规则，只是范围一句/一段

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

### 86 · go ON a trip / take a trip（不是 go to a trip）＋ where to STAY
类型 搭配 ｜ 旧号 B138
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ **合并条·出题多句覆盖** ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-21 毕业 → 09-05 复检 ✅ → 09-11 付息日重答 R10 自由产出里写成 `where to live`，后半格 where to STAY 掉了 —— 与 08-07 建号触发句一字不差，撤销毕业、连对清零。顽固已断的记号撤回：同一格五周后原样回来）

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
**点名**："出去玩之前，先查查住哪儿。"（"出去玩"用 go ＋ trip 那个说法；"住哪儿"用 **where to ＋ 一个动词** 说）

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

### 152 · the first / last TIME ＋ 完整从句（time 不能省）
类型 结构 ｜ 旧号 B241
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ 题型 词组 ｜ **回潮 2026-09-11**（08-19 毕业 → 09-11 复检写成 `The first I saw it.`，把 time 整个吞掉 ＝ 正中本条考点，撤销毕业、连对清零）

**问题是什么**
**the first ／ last TIME ＋ 完整从句**（time 不能省）：first／last 后面挂整个从句时，
中间必须有一个名词把从句接住，那个名词就是 **time**；⛔ 序数词 first 自己带不了从句。
同族：the last time I saw him ／ every time she calls me。
同一格里的邻居（别串）：⛔ 不许用 when 起头（题面已排除）。
判据一句话：first／last 后面跟的是一整句话吗？是 ⇒ 中间必须补 time。

**怎么发现的**
旧 B 表迁移（B241，2026-08-18），原始触发原话未存；最早记录 2026-08-17 ✅。
2026-08-19 ✅ `the first time I saw it I just stood there`（time 没省，顺带自发用出 #163 的块）⇒ 毕业。
2026-09-11 付息日 a2 第 2 组复检：她写 `The first I saw it.` —— **time 被吞**，而本条考点就是它 ⇒ **回潮**。

**我错在哪**
她的：`The first I saw it.`　　正确：`The first time I saw it.`
找法：中文"我第一次看见它**的时候**"里，"的时候"就是那个 time —— 中译英最容易把它当虚词丢掉。

**题面**
"我第一次看见它的时候"（⛔ 不许用 when 起头）

- 2026-08-17 ✅
- 2026-08-19 ✅ `the first time I saw it I just stood there`（time 没省 ＋ 顺带自发用出 #163 的块）
- 2026-09-11 ❌ 复检 · 付息日 a2 第 2 组 · `The first I saw it.` —— **time 被吞**，而本条考点就是它 ⇒ **回潮**
  最小改 `The first time I saw it.`
  ❌ first／last 后面挂整个从句时，中间必须有一个名词把从句接住，那个名词就是 time；
    ⛔ 序数词 first 自己带不了从句。同族 the last time I saw him／every time she calls me。
  ★ 找法：中文"我第一次看见它**的时候**"里，"的时候"就是那个 time —— 中译英最容易把它当虚词丢掉
- 2026-09-13 ✅ 学习日 在池第 1 组 · `The first time I saw it.`——time 没省、没用 when

### 167 · be in a hurry 的主语必须是人；There's no rush.
类型 搭配 ｜ 旧号 B256
状态 连对0 连错2 上次2026-09-13 未毕业 ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-19 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零。★ 今天回标成「题型 整句」才从词组串里单独拎出来 —— 旧口径按「类型 搭配」打包，主语根本不出现、考点永远测不到）

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
- 备注 同族"块记了一半"：`stood on their feet`（该 be on your feet）

### 273 · fine sb FOR doing sth（罚款的介词是 for，不是 of／on）
类型 搭配 ｜ **从 #25 拆出 2026-08-23**
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ 题型 词组 ｜ **回潮 2026-09-11**（08-27 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零。★ 本条 08-23 才从 #25 拆出来，拆出后只被测过两次 ⇒ 基础本来就薄）

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
**点名**："因为乱停车被罚了款"（用 fine ＋ 一个介词说 · "乱停车"就用 illegal parking）

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

### 279 · get a feel for sth（慢慢摸出感觉／找到手感）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ 题型 词组 ｜ **回潮 2026-09-11**（08-28 毕业 → 09-11 复检写成 `get a feel of time`，介词滑到 of，撤销毕业、连对清零）

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
**点名**："慢慢摸出时间的感觉"（用 get ＋ feel 说）
　　★ 题面 2026-08-27 整句改（§3.3 ③「答得合法但不是条目预期 ⇒ 记 ✅ ＋ 当场改题面」）：
　　★ 旧题面"练几次就找到感觉了"这个语境里，`get **the** feel **of** it` 和 `get **a** feel **for** it`
　　★ **两个都成立** ⇒ 逼不出本条的目标形式（她 08-27 给的就是前者）。
　　★ 新题面把宾语换成**抽象领域**（时间）—— `get the feel of time` 不成立，
　　★ 只有 `get **a** feel **for** time` 通，正是她 08-23 自己产出的那一句

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

### 282 · take ownership (of sth)（把它当成自己的事，自己扛起来）
类型 词组 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对0 连错2 上次2026-09-13 未毕业 ｜ 题型 词组 ｜ **回潮 2026-09-11**（08-28 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零）

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

### 286 · 整句句型：If A, B and C, a lot of X will happily do Y（条件够好 → 人自愿去做）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）｜ 点名 2026-08-28 加结构限定（08-27 她走了 `will be happy to` 这条绕路）
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ 题型 整句 ｜ **回潮 2026-09-11**（08-29 毕业 → 09-11 复检掉了 will：`many commuters happily leave…`，题面点名的 will happily 少了一半；08-27 绕 will be happy to、今天丢 will ⇒ 框没长稳，撤销毕业、连对清零）

**问题是什么**
整句句型：**If A, B and C, a lot of X will happily do Y**（条件够好 → 人就自愿去做）。
骨架：If ＋【主语】＋ are ＋【形1, 形2, and 形3】, ＋【一群人】＋ **will happily** ＋【一个具体动作】.
· 三个形容词必须**同形**（cheap, frequent, reliable；✗ cheap, frequent, and it's reliable）
· 主句是**预测** ⇒ **will 不能掉**；掉了 will 就成了零条件句（句子合法，但不是本条要她产出的那句）
· "乐意做某事"在论证句里走【副词】，⛔ 不走【be ＋ 形容词 ＋ to】：will happily leave ／ will gladly pay ／ would happily do it again
· 收尾动作要**具体可画面**：leave their cars at home ＞ use public transport more
同一格里的邻居（别串）：⛔ be happy to ／ be willing to ／ want to —— 它们正是 will happily 要替掉的那一族，题面已封。
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
**点名**："只要公交又便宜、班次又密、又靠得住，很多通勤的人乐意把车留在家里。"（**一句话**说完：if ＋ **三个并列形容词**，主句用 **will** ＋ 一个 **-ly 副词** ＋ 一个具体动作；⛔ 不许用 be happy to／be willing to）

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

### 301 · enjoy ＋ 物主代词 ＋ time／stay（不说 enjoy the time）
类型 搭配 ｜ 新建 2026-08-26（**补建**）
状态 连对0 连错2 上次2026-09-13 未毕业 ｜ 题型 词组 ｜ **回潮 2026-09-11**（08-28 毕业 → 09-11 复检写成 `enjoy the time with him`，与 08-26 建号触发句一模一样，撤销毕业、连对清零）

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


### 319 · present sth TO sb ／ present sb WITH sth（present 不进双宾语那一族）
类型 搭配 ｜ 新建 2026-09-04
状态 连对1 连错0 上次2026-09-13 未毕业 ｜ 题型 词组 ｜ **回潮 2026-09-11**（09-07 毕业 → 09-11 复检答"忘了"，撤销毕业、连对清零；09-05／09-07 两次 ✅ 之后隔 3 个练习日就忘 ⇒ 没长稳）

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
**点名**："给他颁了一块奖牌"（用 **present** ＋ 人在前说）

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
- 备注 **出题口径**：题面必须用 present **真正合适**的场合（颁奖／递交／正式呈上）。
  ⛔ 不出"孩子给妈妈看画"这种日常场景 —— 那种场景的正确答案是 show，出了会**教反**。
- ⇒ **新建当天不测**（§3.1），下一个学习日起进池

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
状态 连对0 连错1 上次2026-09-13 未毕业 ｜ 题型 词组

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

### 334 · the cause OF sth（⛔ cause for）
类型 搭配 ｜ 新建 2026-09-10
状态 连对1 连错0 上次2026-09-11 未毕业 ｜ 题型 词组

**问题是什么**
**the cause OF sth** ＝ 某事的**起因**（the main cause **of** air pollution ／ the cause **of** the fire）。
`cause for` 是另一个意思 ＝ "…的**理由**"，只配情绪／反应类名词：cause for concern／cause for alarm／cause for celebration。
⇒ 说"某个现象的原因"永远是 **of**。
⚠️ 同族**反向**：reason 配 **for**（the reason **for** the delay）—— cause 与 reason 的介词是反的，
这是最容易互相串的一格；题面另外排除 reason／source。
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
"空气污染的主因"（用 **cause** 说 · ⛔ 不许用 reason／source）

- 2026-09-10 📝 新建 · 新题 bank:956 自由产出（P3）· 触发原话
  `But generally speaking, they'not the main **cause for** air pollution.`
  条目内容：**cause OF sth** ＝ 某事的**起因** —— the main cause **of** air pollution／the cause **of** the fire。
  `cause for` 是另一个意思 ＝ "…的**理由**"，只配情绪／反应类名词：cause for concern／cause for alarm／
  cause for celebration。⇒ 说"某个现象的原因"永远是 **of**。
  ⚠️ 同族**反向**：reason 配 **for**（the reason **for** the delay）—— cause 与 reason 的介词是反的，
  这是最容易互相串的一格。
- 2026-09-11 ✅ 付息日 a 段 · 第 1 组 · `the main cause of air pollution.` —— cause 配 OF（首测）⇒ 连对1

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

### 337 · look up sth（查；⛔ look up for）
类型 词组 ｜ 新建 2026-09-13 ｜ 与 🎓#100 互斥（look for）
状态 连对0 连错1 上次2026-09-13 未毕业 ｜ 题型 词组

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
"查一下营业时间"（"查"用 **look** 起头的两个词说）

- 2026-09-13 ❌ 首犯 · 学习日 在池第 1 组 [4]（#86 那题）· `you need to first look up for where to stay`
  最小改 `look up where to stay`
  ❌ look up ＝ 查，后面直接接查的东西，⛔ 不带 for；look for ＝ 找。两个词组各带各的小词，不许拼在一起。
  ★ 判重：dedup "look up" ⇒ 🎓#100（look for，目标形式不同）／🎓#312（search for，另一个动词）⇒ 两条并存，题面互斥

### 338 · end up ＋ -ing（⛔ end up to do／end up to -ing）
类型 词组 ｜ 新建 2026-09-13 ｜ 与 🎓#113 互斥（那条考"都要"那一层，本条考 end up 后面的形）
状态 连对0 连错1 上次2026-09-13 未毕业 ｜ 题型 词组

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
"最后还是自己干了"（"最后…"用 **end up** 说）

- 2026-09-13 ❌ 首犯 · 学习日 复检第 4 组 [8]（#113 那题）· `I always end up to queuing for half an hour every time I go.`
  最小改 `I always end up queuing for half an hour every time I go.`
  ❌ end up 后面直接接 -ing，⛔ 不加 to；"都要"那层（always end up）落地了，归 #113 ✅
  ★ 判重：dedup "end up" ⇒ 🎓#113（层不是形）／#49（历史行带过）⇒ 两条并存

### 339 · reach sb（联系上；直接带宾语，⛔ get reach sb）
类型 词组 ｜ 新建 2026-09-13 ｜ 与 🎓#130 互斥（那条考 can／be able to，本条考 reach 的形）
状态 连对0 连错1 上次2026-09-13 未毕业 ｜ 题型 词组

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

### 340 · a step up from that（递进到更高一档；⛔ on top of that 是平级追加）
类型 词组 ｜ 新建 2026-09-13 ｜ ⭐ 她点名要学
状态 连对0 连错0 上次— 未毕业 ｜ 题型 词组

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

### 341 · deserve praise／credit（⛔ worth praise）
类型 搭配 ｜ 新建 2026-09-13
状态 连对0 连错1 上次2026-09-13 未毕业 ｜ 题型 词组

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

