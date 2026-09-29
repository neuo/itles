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
- 2026-09-29 ⚪ 学习日新题 bank:534（P3）· `career prospect` → career prospects（只记录）
- 2026-09-29 ⚪ 学习日新题 bank:534（P3）· `large-language-model` → large language models（只记录）
- 备注 合并 2026-08-19：#160（泛指一类东西用复数不带冠词）＋ #112（traffic 带不带 the）并入本条 ——
  三条问的是同一个问题；#112 那句"眼前这一份 vs 泛指这件事"正是本条的判据
- 备注 国家形容词 Chinese/Japanese（不是 China's）（原 #160）

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

### 186 · leave a mess（⭐ 她自产）
类型 词组 ｜ 旧号 B97
状态 连对1 连错0 上次2026-09-29 未毕业 ｜ 回潮 2026-09-09（08-17 毕业 → 09-09 复检答"忘了"，撤销毕业、连对清零）｜ **回潮 2026-09-28**（09-11 第二次毕业 → 09-28 复检答成 `mess up the floor`，撤销毕业、连对清零）｜ 题型 整句

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

### 322 · play WITH sth（玩"东西"一律带 with）
类型 搭配 ｜ 新建 2026-09-07
状态 连对1 连错0 上次2026-09-29 未毕业 ｜ **回潮 2026-09-28**（09-11 毕业 → 09-28 复检 [5]／[8] 两次漏 with，撤销毕业、连对清零）｜ 题型 整句

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
- ⇒ **新建当天不测**（§3.1），下一个练习日起进池

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

### 327 · 踏脚点 ＝ foothold ／ peg
类型 词汇 ｜ 新建 2026-09-09
状态 连对0 连错1 上次2026-09-29 未毕业 ｜ **回潮 2026-09-29**（09-13 毕业 → 09-29 复检 foothold 答成 footsteps，撤销毕业、连对清零）｜ 题型 词组

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

### 331 · look straight ahead（往正前方看）≠ look forward to（期待）
类型 词组 ｜ 新建 2026-09-09
状态 连对0 连错1 上次2026-09-29 未毕业 ｜ **回潮 2026-09-29**（09-13 毕业 → 09-29 复检答成 look forward ahead，撤销毕业、连对清零）｜ 题型 词组

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

### 353 · vibe 是【地方带的】，人不待在 vibe 里（a place with a different vibe）
类型 搭配 ｜ 新建 2026-09-20
状态 连对0 连错1 上次2026-09-29 未毕业 ｜ **回潮 2026-09-29**（09-26 毕业 → 09-29 复检写成 in a totally different vibe，撤销毕业、连对清零）｜ 题型 整句

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

### 363 · appeal to sb's emotions（拿情绪打动人；⛔ drive sb with emotion）
类型 搭配 ｜ 新建 2026-09-27
状态 连对1 连错0 上次2026-09-28 未毕业 ｜ 题型 整句

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
"很多广告不讲产品好在哪，只会打感情牌来打动你。"（"打感情牌来打动你"用 **appeal** 说）

- 2026-09-27 新建 · 学习日在池第 1 组 [2] · 触发原话 `while others drive you with emotion.`（⚠️ 更地道的表达 ⇒ §3.2b 建号）
- 2026-09-28 ✅ 在池第 1 组 · `Appeal to your emotions.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  move／play on 都合法，中文块单独映射不回 appeal to ⇒ 改整句、正向点名 appeal，to your emotions 留给她搭；换成广告场景

### 364 · without a doubt（毫无疑问）
类型 词组 ｜ 新建 2026-09-29 ｜ ⭐ 她点名要背
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
**without a doubt** ＝ 毫无疑问，P3 开口亮立场用；放句首、句尾都行（`The tech sector, without a doubt.`）。
同一格里的邻居（别串）：no doubt（更随口，也常表"我猜"）· definitely（一个词版）· undoubtedly（书面）
判据一句话：想说"毫无疑问／肯定是"，三个词 without a doubt。

**怎么发现的**
2026-09-29 学习日 新题 bank:534（P3 · In your country, what industry is it easier to be successful in?）：
她写 `The tech and software sectors, without a doubt(背一下).` —— 她点名要背。
判重三步：
　① 目标形式 dedup "without a doubt" ⇒ 零命中
　② 中文 dedup "毫无疑问" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了，点名要背（⭐ 不是纠错）
找法：P3 要亮立场时，名词短语 ＋ without a doubt 一句就够。

**题面**
"要说在我们这儿哪个行业最好找工作，毫无疑问是医疗。"（"毫无疑问"用 **without a doubt** 说）

- 2026-09-29 新建 · 学习日新题 bank:534 · 她点名要背 · 原话 `The tech and software sectors, without a doubt(背一下).`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  no doubt／definitely 都合法 ⇒ 改整句；她点名要学（§2③）⇒ 首测把整个块写进题面；换成求职行业场景

### 365 · powerhouse（某个领域实力最强的那家：a delivery powerhouse）
类型 词汇 ｜ 新建 2026-09-29 ｜ ⭐ 她点名要背
状态 连对0 连错0 上次— 未毕业 ｜ 题型 词组

**问题是什么**
**powerhouse** ＝ 在某个领域实力强、能打的那家公司／那个国家／那个人：a delivery powerhouse ／ an economic powerhouse。
同一格里的邻居（别串）：giant（体量大）· leader（排第一）· powerhouse（实力强）
★ 与 #367（social media giant）分工：那条考 giant 前面放行业名，本条考 powerhouse 这个词本身。
判据一句话：想说"XX 巨头／XX 强者"又不用 giant ⇒ 行业名 ＋ powerhouse。

**怎么发现的**
2026-09-29 学习日 新题 bank:534：她写 `an instant-delivery powerhouse(背一下) like MeiTuan` —— 她点名要背。
判重三步：
　① dedup "powerhouse" ⇒ 零命中
　② dedup "巨头" ⇒ 零命中
　③ 保留新建

**我错在哪**
她的：用对了，点名要背（⭐ 不是纠错）
找法：说"XX 巨头"时，除了 giant 还有 powerhouse，前面放行业名。

**题面**
"新能源汽车里的实力派"（字面是"发电站"的那个词，比喻一个行业里最能打的那家）

- 2026-09-29 新建 · 学习日新题 bank:534 · 她点名要背 · 原话 `an instant-delivery powerhouse(背一下) like MeiTuan`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉首字母与排除项，括号改中文释义（"发电站"的比喻）；换成新能源汽车场景

### 366 · make bank（赚大钱，口语俚语；make absolute bank ＝ 赚翻了）
类型 词组 ｜ 新建 2026-09-29 ｜ ⭐ 她点名要背
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
**make bank** ＝ 赚很多钱（口语俚语）；加强版 **make absolute bank** ＝ 赚翻了。bank 这里不加冠词。
同一格里的邻居（别串）：make a fortune（发大财，偏正式）· make good money（挣得不错）
判据一句话：口语里说"赚翻了"⇒ making (absolute) bank。

**怎么发现的**
2026-09-29 学习日 新题 bank:534：她写 `people working on large-language-model are making absolute bank(背一下)` —— 她点名要背。
判重三步：
　① dedup "make bank" ⇒ 零命中
　② dedup "赚大钱" ⇒ 零命中
　③ 保留新建

**我错在哪**
她的：用对了，点名要背（⭐ 不是纠错）
找法：想说"赚翻了"，落 making absolute bank（bank 前面不加 a／the）。

**题面**
"今年做直播带货的那几个主播都赚翻了。"（"赚翻了"用 **bank** 说）

- 2026-09-29 新建 · 学习日新题 bank:534 · 她点名要背 · 原话 `people working on large-language-model are making absolute bank(背一下)`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  make a killing／make a fortune 都合法 ⇒ 改整句、点名 bank，make 与不加冠词留给她；换成直播带货场景

### 367 · social media giant（社交巨头；⛔ social giant）
类型 搭配 ｜ 新建 2026-09-29
状态 连对0 连错0 上次— 未毕业 ｜ 题型 词组

**问题是什么**
"XX 巨头" ＝ **行业名 ＋ giant**：a social media giant ／ a tech giant ／ a retail giant。
社交这个行业叫 **social media**；social 单独放在名词前是"爱社交的／社会的"（a social person ＝ 爱社交的人）。
★ 与 #365（powerhouse）分工：本条考 giant 前面的行业名，那条考 powerhouse 这个词。
判据一句话：giant 前面放的是行业名吗？"社交"这个行业 ⇒ social media。

**怎么发现的**
2026-09-29 学习日 新题 bank:534：她写 `Whether you secure a position at a social giant like Tencent`。
判重三步：
　① dedup "giant" ⇒ 命中 🎓#293（one side of it，只是历史行里的字串，考点无关）⇒ 否
　② dedup "social media" ⇒ 命中 🎓#8（群组 in／论坛 on）· 🎓#80（than ever）· 🎓#81（get to know），都只是例句字串 ⇒ 否
　③ 保留新建

**我错在哪**
她的：a social giant　　更地道：a social media giant
找法：说"XX 巨头"先问 giant 前面是不是行业名 —— social 不是行业名，social media 才是。

**题面**
"微博这种社交巨头"（做社交平台的大公司）

- 2026-09-29 新建 · 学习日新题 bank:534 · 触发原话 `at a social giant like Tencent`（⚠️ 更地道的表达 ⇒ §3.2b 建号）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉「两个词 ＋ ⛔ 只用 social」，括号改中文释义；换成微博

### 368 · land a job (at …)（谋到／进了一份工作）
类型 词组 ｜ 新建 2026-09-29
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
**land a job (at 公司)** ＝ 找到／谋到一份（好）工作，口语里"进了腾讯"就说 land a job at Tencent。
同一格里的邻居（别串）：get a job（最普通）· secure a position（招聘启事腔，书面）· find a job（强调找的过程）
判据一句话：嘴上说"进了某家公司／拿到一份好工作"⇒ land a job at …。

**怎么发现的**
2026-09-29 学习日 新题 bank:534：她写 `Whether you secure a position at a social giant like Tencent`。
当场被教练记成「书面登记 🎓#206」、未建号 —— 她追问后查证：session 与档案里**找不到她说过 land a job** ⇒ 对她是新表达 ⇒ 按 §3.2b 补建。
判重三步：
　① dedup "land" ⇒ 零命中
　② dedup "谋" ⇒ 零命中
　③ 保留新建

**我错在哪**
她的：secure a position at　　更地道（口语）：land a job at
找法：想说"进了／谋到一份工作"，口语落 land a job，⛔ 别去够 secure a position。

**题面**
"她毕业没多久就在一家大银行谋到了一份工作。"（"谋到"用 **land** 说）

- 2026-09-29 新建 · 学习日新题 bank:534 · 触发原话 `secure a position at a social giant like Tencent`（⚠️ 更地道的表达；教练初判走书面登记漏建，她追问后补建）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  get／find 都合法 ⇒ 改整句、点名 land；换成银行场景

### 369 · 中文"头衔＋名字"（社交巨头腾讯）⇒ 英文【名字, the 头衔】（Tencent, the social media giant）
类型 结构 ｜ 新建 2026-09-29
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
中文把头衔放在名字**前面**直接连（社交巨头腾讯、短视频巨头字节跳动），中间没有任何连接词；
英语⛔ 不找介词，用同位语：**名字 ＋ 逗号 ＋ the 头衔** —— `Tencent, the social media giant`。
（新闻体也可以把不带冠词的头衔直接放名字前：`social media giant Tencent`，同样合法）
同一格里的邻居（别串）：a social media giant like Tencent ＝"像腾讯这样的社交巨头"（举例，不是指腾讯本身）
★ 与 🎓#1（同位语，一个逗号，⛔ 不用 who／which）分工：#1 考"解释块前面别加 which is"，本条考"中文头衔在前 ⇒ 英文挪到名字后面、补 the、不找介词"。
判据一句话：中文"XX 头衔 ＋ 名字"⇒ 名字, the XX 头衔。

**怎么发现的**
2026-09-29 学习日 新题 bank:534：她写 `a social giant like Tencent`，并自注
"社交巨头腾讯、短视频绝对领先者字节跳动还是即时配送美团，这个 like 其实我不会翻译，还是查了下，我一直在想用什么介词"。
当场教练只在 🎓#1 留了一行 📝、未建号 —— 她追问后按 §2③（她说"不会"）补建。
判重三步：
　① dedup "同位" ⇒ 命中 🎓#1（同位语，考不加 which is）⇒ 否，考点不同（本条考语序＋the、不找介词）；#265 #75 #363 只是字串 ⇒ 否
　② 中文 dedup "巨头" ⇒ 零命中
　③ 保留新建

**我错在哪**
她的：不会把"社交巨头腾讯"直接说出来，一直在找介词（最后用 like 绕开）
正确：`Tencent, the social media giant`
找法：中文头衔贴在名字前面时，先说名字，再逗号 ＋ the ＋ 头衔 —— ⛔ 不找介词。

**题面**
"我表哥在短视频巨头字节跳动上班。"（先说"字节跳动"，"短视频巨头"用 **, the …** 补在后面）

- 2026-09-29 新建 · 学习日新题 bank:534 · 她自注"这个 like 其实我不会翻译…我一直在想用什么介词" · 原话 `a social giant like Tencent`（教练初判只留 📝、漏建，她追问后补建）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉两条负向排除，改成正向点名同位语结构「, the …」；换成表哥在字节跳动

### 370 · create ＋ 结果（造就一批富豪／创造就业：create billionaires；⛔ build billionaires）
类型 搭配 ｜ 新建 2026-09-29
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
"造就／催生出一批（人或结果）"＝ **create**：create billionaires ／ create jobs ／ create wealth。
build 只能搭"建起来的东西"（build a company／a house／a brand），⛔ 搭不上人（build billionaires）。
★ 与 🎓#85（start／set up a business，⛔ create a business）分工：那条是"开公司"不用 create，本条是"造就人／结果"要用 create ⇒ 两个方向，各管各的宾语。
判据一句话：宾语是一批人或一种结果（富豪、就业、财富）⇒ create；宾语是一个实体建起来 ⇒ build／set up。

**怎么发现的**
2026-09-29 学习日 新题 bank:534：她写 `the digital revolution has fueled the rapid rise of Chinese tech businesses, building a bunch of tech giants and billionaires`。
当场被教练记成"同级近义词、不建号"—— 她追问后改判：build 搭不上 billionaires ＝ 搭配问题 ⇒ 补建。
判重三步：
　① dedup "create" ⇒ 命中 🎓#85（开公司不用 create）⇒ 否，宾语方向相反
　② dedup "造就" ⇒ 零命中
　③ 保留新建

**我错在哪**
她的：building a bunch of tech giants and billionaires　　更地道：creating a bunch of tech giants and billionaires
找法：说"造就了一批 XX"，先看宾语是不是人／结果 —— 是就用 create。

**题面**
"这波电商热潮造就了一大批亿万富翁。"（"造就"用 **create** 说）

- 2026-09-29 新建 · 学习日新题 bank:534 · 触发原话 `building a bunch of tech giants and billionaires`（教练初判"同级近义词"漏建，她追问后补建）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  produce／give rise to 都合法 ⇒ 改整句、点名 create；换成电商热潮场景

### 371 · bring your other foot over（把另一只脚挪过来；⛔ pull your foot over）
类型 词组 ｜ 新建 2026-09-29
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
把身体某部位"挪／带"到某个位置 ＝ **bring … over**：bring your other foot over ／ bring your arm up。
pull 是"用力拽"，说脚的话像用手去拽自己的脚。
判据一句话：自己把脚／手挪过去 ⇒ bring … over，⛔ 不用 pull。

**怎么发现的**
2026-09-29 学习日 复检第 2 组 [6]（🎓#333 题面"我叫他抱住柱子，把另一只脚挪过来。"）：
她写 `I told him to hug the log, and pull his other foot over.`（#333 考点 his 判 ✅）。
当场被教练记成"同级近义词、不建号"—— 她追问后改判：pull 在这里意思偏了 ＝ 选词问题 ⇒ 补建。
判重三步：
　① dedup "bring" ⇒ 命中 🎓#145（bring／take／fetch 方向）· #149 #189 #173 #236（字串）⇒ 否，都不是"挪身体部位"
　② dedup "挪过来" ⇒ 命中 🎓#333（同一句题面，考 his 人称）⇒ 否，考点不同；★ 两条题面⛔ 不许用同一句
　③ 保留新建

**我错在哪**
她的：pull his other foot over　　更地道：bring his other foot over
找法：说"把脚挪过去"，动词落 bring，⛔ 别用 pull（那是拽）。

**题面**
"瑜伽老师让我们先站稳一条腿，再把另一只脚慢慢挪过来。"（"挪过来"用 **bring** 说）

- 2026-09-29 新建 · 学习日复检第 2 组 [6] · 触发原话 `I told him to hug the log, and pull his other foot over.`（教练初判"同级近义词"漏建，她追问后补建）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  move 合法 ⇒ 改整句、点名 bring，over 留给她；换成瑜伽课场景（⛔ 与 🎓#333 不同句）

### 372 · get it（把想要的东西弄到手；⛔ reach it —— reach 接目标／地点）
类型 搭配 ｜ 新建 2026-09-29
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
"把想要的东西弄到手"口语就是 **get it**：know what he wants and how to **get it**。
reach 接的是**目标／地点**（reach a goal ／ reach the top），⛔ 不接"想要的东西"。
判据一句话：宾语是"想要的东西"⇒ get；宾语是目标／终点 ⇒ reach。

**怎么发现的**
2026-09-29 学习日 复检第 2 组 [9]（🎓#323 题面"他聪明到知道自己到底要什么、也知道怎么去够到。"）：
她写 `he's smart enough to know what he really wants and how to reach it.`（#323 考点 wh 词判 ✅）。
当场被教练记成"同级近义词、不建号"—— 她追问后改判：reach 搭不上 what he wants ＝ 搭配问题 ⇒ 补建。
判重三步：
　① dedup "get it" ⇒ 命中 🎓#137（I get it ＝ 听懂）· 🎓#323（同一句）⇒ 否，考点不同
　② dedup "弄到手" ⇒ 零命中
　③ 保留新建；★ 题面⛔ 不许与 #323 用同一句

**我错在哪**
她的：how to reach it　　更地道：how to get it
找法：说"弄到手／得到它"，先看宾语是不是"想要的东西"—— 是就用 get。

**题面**
"那双限量球鞋一上架就被抢光了，我到现在也没弄到手。"（"弄到手"用 **get** 说）

- 2026-09-29 新建 · 学习日复检第 2 组 [9] · 触发原话 `how to reach it`（教练初判"同级近义词"漏建，她追问后补建）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  obtain／grab 都合法 ⇒ 改整句、点名 get；换成限量球鞋场景（⛔ 与 🎓#323 不同句）

### 373 · It was when …（"那是在…的时候"：P2 第一句点题后接故事）
类型 句型 ｜ 新建 2026-09-29
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
先用一句话点题，再用 **It was when ＋ 从句** 把具体那件事接上：
`I'd like to talk about a time I felt really proud of my son. It was when we went on an obstacle course together.`
It 指前一句的"那一次"，when 从句说是哪一次（时间／事件）。
同一格里的邻居（别串）：That was when …（强调"就是那时候"）· It happened when …
判据一句话：前一句说了"有一次…"，下一句要交代是哪一次 ⇒ It was when …。

**怎么发现的**
2026-09-28 学习日 新题 bank:915（P2 · Describe a time when you felt proud of a family member）：
她开头 `I'd like to talk about a time I went on an obstacle course with my 5-year-old son.`，proud 到最后一句才出现；
教练的更好版拆成 `… a time I felt really proud of my 5-year-old son. It was when we went on an obstacle course together.`
当时判"P2 开头扣卡的做法、不建号"—— 09-29 她追问后改判：做法本身不是表达，但里面的 It was when … 是能学的句型 ⇒ 补建。
判重三步：
　① dedup "It was when" ⇒ 零命中
　② dedup "那是" ⇒ 命中 28 条，逐条看都是题面／例句里的"那是"字串（#110 #174 #178 #186 #222 …），⛔ 无一条考 It was when ⇒ 否
　③ 保留新建

**我错在哪**
她的：第一句直接讲事件，没先点题　　更好：先点题（felt proud of …），再 It was when … 接事件
找法：P2 第一句说完"有一次我…"，第二句用 It was when … 交代是哪一次。

**题面**
"我想说说我第一次对自己的英语有信心的那一次。那是我在机场帮一个外国人指路的时候。"（第二句用 **It was when** 起头）

- 2026-09-29 新建 · 追补 09-28 新题 bank:915 · 原话 `I'd like to talk about a time I went on an obstacle course with my 5-year-old son.`（教练 09-28 判"做法不建号"漏建，她 09-29 追问后补建）

### 374 · can't be bothered (to do)（懒得…：比 lazy 更口语）
类型 词组 ｜ 新建 2026-09-29 ｜ 从 🎓#15 拆出
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
**can't be bothered (to do sth)** ＝ 懒得（做某事）—— 说的是"这件事不值得我费劲"，比 lazy 更口语。
过去的事用 **couldn't be bothered**：`I couldn't be bothered to cook, so I ordered takeout.`
同一格里的邻居（别串）：I'm too lazy to …（合法，偏"说自己人懒"）· I don't feel like -ing（不太想）
判据一句话：中文"懒得 ＋ 动作"⇒ can't／couldn't be bothered to ＋ 动作。

**怎么发现的**
2026-09-29 从 🎓#15（旧 B37，deep down／It's not that…／can't be bothered 三块捆在一条）拆出（§3.1 一条 ＝ 一个考点）。
来源：08-19 她答 `It's not that I don't want to go. I'm just lazy.`，教练在备注里给了更口语的 can't be bothered，
之后一直挂在捆绑条目里、从没单独出过题，她也从没自己说出过它 ⇒ 对她是新表达（§3.2b）。
判重三步：
　① 目标形式 dedup "bothered" ⇒ 只命中 🎓#15（拆出来的来源）⇒ 否
　② 中文 dedup "懒得" ⇒ 只命中 🎓#15 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`I'm just lazy`（08-19，合法但不是这个块）　　更地道：`I just can't be bothered.`
找法：想说"懒得…"先落 can't be bothered，过去的事换成 couldn't。

**题面**
"周末我懒得做饭，直接点了外卖。"（"懒得"用 **can't be bothered** 说）

- 2026-09-29 新建 · 从 🎓#15 拆出 · 原话 `It's not that I don't want to go. I'm just lazy.`（08-19）· 教练给的更口语版
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）
  去掉负向排除；她不会的句型（§2③）⇒ 首测把 It was when 整个写进题面；换成机场指路场景

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

