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
状态 连对0 连错1 上次2026-08-19 未毕业 ｜ **回潮（当天毕业当天回潮）** ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定）｜ 题型 整句
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
- 2026-09-13 ⚪ 学习日 在池第 3 组 [3]（#335 题）· `If risk is lower, people are willing to take action.`——"更愿意"的"更"丢了；同句 `lower` 比较级做对 ⇒ 形态类只记号
  ★ 09-18 补记：09-13 当天只在 diff-2 给了 ⚠️、漏记本行（§3.4② 在哪儿掉都记 ⚪）
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）
- 2026-09-18 ⚪ 学习日 在池第 1 组 [9]（#335 题）· `people are willing to take action`——"更愿意"的"更"丢了；同句 `lower` 比较级做对 ⇒ 形态类只记号
  检查触发：中文里有"更"，回头看英文里有没有 -er／more
- 备注 分诊：**短词加 -er 她已自动化（noisier／cheaper 都对），长词要加 more 的那一半没装上**
  ⇒ 重新入池后只测长形容词（convenient／important／difficult／expensive）

### 10 · 主谓一致
类型 语法 ｜ 旧号 B27
状态 连对0 连错2 上次2026-08-20 未毕业 ｜ **累错 7** ｜ **形态类·不召回** ｜ **顽固** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定）｜ 题型 整句
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
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）
- 2026-09-21 ⚪ 留痕 · 学习日 在池第 1 组 [1] · `The letters on the cake is spelled out` → `are spelled out`
  —— 主语 The letters 复数，中间隔了 on the cake，动词被就近的 cake 带跑。§3.4 执行自查：同一篇里 `you have`／`going to ancient sites feels`／`the magic of reading lies` 三处都对 ⇒ 是产出时检查没跑，不是不会 ⇒ 只记 ⚪
- 2026-09-21 ⚪ 留痕 · 新题 bank:1005（P3）[S1] · `what are popular` → `what was popular`
  —— what 引出的主语从句动词用单数，且后半句 `when each generation was young` 已把时间钉在过去 ⇒ was。§3.4 执行自查：同一篇里 `the 1990s was`／`teenagers were`／`it was`／`preferences get` 四处都对 ⇒ 产出时检查没跑，不是不会 ⇒ 只记 ⚪（时态那一面同族 #12，同一处 ⛔ 不双记）
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
状态 连对0 连错1 上次2026-08-19 未毕业 ｜ **累错 6** ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 整句
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
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）

### 56 · visual effects 恒复数；可数名词单数必须带限定词
类型 语法 ｜ 旧号 B79
状态 连对1 连错0 上次2026-08-17 未毕业 ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 整句
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
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）
- 2026-09-20 ⚪ 学习日 在池第 1 组（#98 句2）· `The letters on top of cake are …` ⇒ on top of **the** cake —— 形态类只记录·不判档
  检查触发：说完一个单数可数名词，回头看它前面有没有限定词
- 2026-09-27 ⚪ 新题 bank:1339（P3）[S3] · `Without river network watering` → a river network —— 单数可数名词左边没有限定词；同句 a country 写对 ⇒ 只记录


### 63 · 泛指 vs 特指：泛指不带 the（可数就用复数），特指才带 the
类型 语法 ｜ 旧号 B86＋B249＋B195
状态 连对0 连错2 上次2026-08-20 未毕业 ｜ **顽固** ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 整句
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
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）
- 2026-09-27 ⚪ 新题 bank:1339（P3）[S2] · `rivers provide the essential irrigation for crops` → essential irrigation —— 泛指带了 the；同篇 for crops／food shortages 泛指都没带 the ⇒ 检查没跑，只记录
- 2026-09-27 ⚪ 新题 bank:1339（P3）[S3] · `watering the field` → the fields —— 所有农田是一类 ⇒ 复数；同篇 crops／lakes／weekends 复数都对 ⇒ 只记录
- 备注 合并 2026-08-19：#160（泛指一类东西用复数不带冠词）＋ #112（traffic 带不带 the）并入本条 ——
  三条问的是同一个问题；#112 那句"眼前这一份 vs 泛指这件事"正是本条的判据
- 备注 国家形容词 Chinese/Japanese（不是 China's）（原 #160）

### 88 · get on with it（不废话，埋头干下去）
类型 词组 ｜ 旧号 B141
状态 连对0 连错1 上次2026-09-27 未毕业 ｜ 回潮已断（08-11 曾毕业）｜ 回潮 2026-09-05（08-21 毕业 → 09-05 复检写成 `go on with it`）｜ **回潮 2026-09-27**（09-10 第二次毕业 → 09-27 复检答"忘了"，撤销毕业、连对清零）｜ 题型 词组

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
- 2026-09-15 ⚡ 自评免测 · 复检第 3 组（她原话："除了 7 全都直接过"）
- 2026-09-27 ❌ 复检组 · 第 2 组 · **回潮** · 她答"忘了"
  最小改 `Get on with it.`

### 89 · 加形容词说"哪一种"时回到 a（a diverse economy）
类型 语法 ｜ 旧号 B144
状态 连对0 连错1 上次2026-08-20 未毕业 ｜ **形态类·不召回**（冠词族，同 #63）｜ **回潮 2026-08-20**（08-20 当天毕业当天回潮）｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 整句
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
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）
### 93 · 不在那一小撮里的动词必须变形（sit→sat／sing→sang）
类型 语法 ｜ 旧号 B152b
状态 连对0 连错0 上次 — ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 整句
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
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）


### 147 · 时态只标一次：did/will/should/can/must 一出现，后面动词一律原形
类型 语法 ｜ 旧号 B236
状态 连对0 连错1 上次2026-08-20 未毕业 ｜ **顽固**（08-11/08-16/08-17/08-20 四犯） ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 整句
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
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）
- 备注 自我分诊：单独问她"情态动词后面接什么"秒答"原形" ⇒ 不 drill，只加产出时检查触发
- 备注 与 #10 主谓一致／#54 比较级只标一次／#92 否定别丢合成一条元规则：**每个语法标记在一个谓语上只能出现一次，而且必须出现一次**

### 150 · 限定词必须跟后面名词的【数】一致（These statements／a group）
类型 语法 ｜ 旧号 B239
状态 连对0 连错2 上次2026-08-19 未毕业 ｜ **顽固** ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题**（她 2026-08-27 定："标记下就行了，不出题，只记录"）｜ 题型 整句
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
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）
- 2026-09-26 ⚪ 复检第 2 组 [8]（#318 题里）· `when he was two year old` —— 数词 two 后面 year 没变复数；她 #318 历史里写对过 two years old ⇒ 检查没跑，只记录

### 324 · other 是限定词、others 才是代词（happier than **others**）
类型 语法 ｜ 新建 2026-09-07
状态 连对0 连错0 上次 — 未毕业 ｜ **形态类·不召回** ｜ ⚪ **只记录·不出题** ｜ 题型 整句

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
- 2026-09-15 📝 产出验机制取消 ⇒ 题型格回默认「整句」；形态类标记与状态行其余各格一律不动，仍⛔不进召回队列（行为零变化）
- ⇒ 形态类：⛔ 永不出题（§3.4①），以后在任何地方掉了只追加一行 ⚪

### 357 · logic 是名词、logical 才是形容词（a strong logical thinker）
类型 词汇 ｜ 新建 2026-09-22
状态 连对0 连错1 上次2026-09-27 未毕业 ｜ 题型 词组

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
"一个逻辑很强的人"（用 **logic** 那个词的家族说 · ⛔ 不许用 rational／reasonable／smart）

- 2026-09-22 ❌ 首犯 · 新题 bank:1102（P3）· 原话 `Some people are strong logic thinkers`
- 2026-09-26 ✅ 付息日 a 在池第 1 组 [4] · `A logical thinker.` —— logic 后面挂名词 ⇒ logical。连错 1 清零、连对 0 → 1
  ★ 漏了"很强"（strong）⇒ diff-2 ⚠️，不建号
- 2026-09-27 ❌ 在池第 1 组 · `A strong logic thinker` —— logic 仍当形容词放在 thinker 前
  最小改 `A strong logical thinker`

### 358 · on a(n) … level（在…层面；⛔ at an emotional level）
类型 搭配 ｜ 新建 2026-09-22
状态 连对1 连错0 上次2026-09-26 未毕业 ｜ 题型 词组

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
"在情感层面上跟人连起来"（"在…层面上"用 **level** 那个名词说 · ⛔ 不许用 emotionally）

- 2026-09-22 新建 · 新题 bank:1102（P3）· 触发原话 `they quickly connect at an emotional level`（⚠️ 更地道的表达 ⇒ §3.2b 建号）
- 2026-09-22 📝 **正文订正（她当场推翻我写窄的判据）**：她问「at the social level 是 at 还是 on」——
  `at the social level` 完全成立（社会这一层 vs 个人那一层 ＝ 层级用法）⇒ 建号时写的"at ＋ level 只用于物理高度"**是错的**，
  当天改成按**冠词**分的两个块（on a/an ＋ 角度 ／ at the ＋ 层级 ／ at ＋ 物理高度）。
  ⛔ 判定口径同步放宽：她若答 `at the … level` 且说的是层级 ⇒ **判 ✅**；本条真正要卡的只有"从某个角度"那一格该用 on。
- 2026-09-26 ✅ 付息日 a 在池第 1 组 [7] · `Connect with people on an emotional level.` —— on ＋ an ＋ 形容词 ＋ level，connect 带上 with people。首测，连对 0 → 1

### 359 · persuasion ＝ 说服（名词；动词 persuade · 形容词 persuasive）
类型 词汇 ｜ 新建 2026-09-22 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-09-26 未毕业 ｜ 题型 词组

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
"成功的说服" ／ "说服的艺术"（"说服"两处都用**一个名词**说，**p** 开头 · ⛔ 不许用 persuading）

- 2026-09-22 新建 · 新题 bank:1102（P3）· 触发原话 `successful persuasion(这个单词背一下)`（⭐ 她点名要背，词本身用对了）
- 2026-09-26 ✅ 付息日 a 在池第 1 组 [8] · `successful persuasion. The art of persuasion.` —— 两处都调出名词 persuasion。首测，连对 0 → 1

### 360 · get to ＋ 动词原形 ＝ 能／有机会做（⛔ get to ＋ somewhere）
类型 语法 ｜ 新建 2026-09-26
状态 连对1 连错0 上次2026-09-27 未毕业 ｜ 题型 整句

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
"度假的时候，你能在海边待上一整天。"（"能"用 **get** 说 · ⛔ 不许用 can／be able to）

- 2026-09-26 ❌ 首犯 · 付息日 a 在池第 1 组 [6]（#353 同句）· 原话 `You get to somewhere with a totally different vibe.`
- 2026-09-27 ✅ 在池第 1 组 · `When you're on vacation, you get to speed the whole day at the beach.` —— get to ＋ 原形到位
  ｜speed ＝ spend 打漏 n，§2.1 拼写不算

### 361 · 准点下班 ＝ get off work on time（⛔ leave work early ＝ 早退）
类型 词组 ｜ 新建 2026-09-26
状态 连对1 连错0 上次2026-09-27 未毕业 ｜ 题型 词组

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
"每天都能准点下班"（"准点下班"用 **get** 起头说 · ⛔ 不许用 early）

- 2026-09-26 新建 · 付息日 d 段重答 bank:778（R16）· 触发原话 `If you can leave work early`（⚠️ 更地道的表达 ⇒ §3.2b 建号）
- 2026-09-27 ✅ 在池第 1 组 · `You can get off work on time every day.` —— 首测，块一字不差

### 362 · turn down ＋ 机会（没人会拒绝…；⛔ no one can refuse）
类型 词组 ｜ 新建 2026-09-26
状态 连对1 连错0 上次2026-09-27 未毕业 ｜ 题型 整句

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
"这么好的工作，没人会拒绝。"（"拒绝"用 **turn** 说 · ⛔ 不许用 refuse／say no）

- 2026-09-26 新建 · 付息日 d 段重答 bank:778（R16）· 触发原话 `no one can refuse a job with reasonable hours and job security`（⚠️ 更地道的表达 ⇒ §3.2b 建号）
- 2026-09-27 ✅ 在池第 1 组 · `No one would turn down a job this good.` —— 首测，turn down 到位

### 363 · appeal to sb's emotions（拿情绪打动人；⛔ drive sb with emotion）
类型 搭配 ｜ 新建 2026-09-27
状态 连对0 连错0 上次— 未毕业 ｜ 题型 词组

**问题是什么**
靠情绪去打动／说服别人 ＝ **appeal to sb's emotions**（appeal 后面接 to；emotions 用复数）。
`Some people persuade you with logic, while others appeal to your emotions.`
同一格里的邻居（别串）：drive sb ＝ 驱使、逼着（drive me crazy）· move sb ＝ 让人感动（没有"说服"那层）
判据一句话：要说"用情绪去说服／打动别人"⇒ appeal to their emotions。

**怎么发现的**
2026-09-27 学习日 在池第 1 组 [2]（#356 题面"…另一些人靠情绪带动你。"）· 触发原话
`Some people persuade you with logic, while others drive you with emotion.`
判重三步：
　① 目标形式 appeal to ⇒ dedup "appeal to" ⇒ 零命中
　② dedup "emotion" ⇒ 只命中 #356（考 others 一个词，与本条无关）；dedup "情绪" ⇒ 命中 #356 · #355 · 🎓#328 · 🎓#334，
　　　后三条只是历史／正文里出现过这个字串（ballad／small 比较级／the cause of），考点无关 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`others drive you with emotion`　　更地道：`others appeal to your emotions`
找法：想说"打情感牌／靠情绪打动"时，先落 appeal to。

**题面**
"拿情绪去打动你"（用 **appeal** 说 · ⛔ 不许用 drive／move）

- 2026-09-27 新建 · 学习日在池第 1 组 [2] · 触发原话 `while others drive you with emotion.`（⚠️ 更地道的表达 ⇒ §3.2b 建号）

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

