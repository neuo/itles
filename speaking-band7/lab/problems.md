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
- 2026-09-30 ⚪ 付息日 a2 第 4 组 [4] · `The doctor haven't` → hasn't（同组 rent is／neighborhood is 都对 ⇒ 形态类，只记录）
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
- 2026-10-01 ⚪ 学习日 复检第 4 组 [5]（🎓#35 题里）· `Nobody tell me a thing about it.` → told（"谁也没告诉我"＝过去；同组 got／stood／played／bought 都标了过去 ⇒ 形态类，只记录）
- 2026-10-01 ⚪ 学习日 新题 bank:1156（P2）[S7] · `The river lazily meanders along` → meandered（前面 I was completely immersed 已在过去，同一场景的景物描写跳回现在；同篇 couldn't get／was／stayed／took 都标了过去 ⇒ 形态类，只记录）
- 2026-10-08 ⚪ 付息日 a 段在池第 1 组 [7]（#418 题里）· `She was sitting on the idea for this novel for ten years` —— 后面挂着 for ten years ⇒ had been sitting；形态类只记录

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
- 2026-09-30 ⚪ 付息日 a 段在池第 2 组 [5] · `The limited-edition sneaker sold out the second they dropped` → sneakers（同句 they／them 复数 ⇒ 形态类，只记录）
- 2026-10-04 ⚪ 付息日 a 段在池第 1 组 [2]（#372 题里）· `my friends pulled three all-nighter before he …` → my friend（题面"我朋友"一个人，后面也用了 he；同句 Concert tickets 复数标对 ⇒ 形态类，只记录）
- 2026-10-04 ⚪ 付息日 a 段在池第 1 组 [2]（#372 题里）· `got his hand on a pair` → his hands（get one's hands on 固定两只手；10-03 她写对过 got my hands on it ⇒ 形态类，只记录）


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
- 2026-10-02 ⚪ 学习日 新题 bank:1203（P3）[S2] · `Take BBC’s Wonders of the Solar System, for example` —— the BBC 是"这一个"机构，漏了 the（字母念的机构缩写都带 the：the BBC／the UN；拼读的 NASA 不带）；同篇 the habits／the wild／the information 都标对 ⇒ 形态类只记录
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
- 2026-09-30 ⚪ 付息日 d 段重答 bank:911 [S4] · `which helps reduces conflicts` → helps reduce（同篇 makes you smile 原形对 ⇒ 形态类，只记录）
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
- 2026-09-30 ⚪ 付息日 a 段在池第 1 组 [6] · `That films constantly tries …` → That film（同句 tries 单数 ⇒ 形态类，只记录）
- 2026-09-30 ⚪ 付息日 a 段在池第 1 组 [9] · `This living shopping hosts …` → These（同组 [8]／[10] 限定词全对 ⇒ 形态类，只记录）
- 2026-10-04 ⚪ 付息日 a 段在池第 1 组 [2]（#372 题里）· `pulled three all-nighter` → three all-nighters（同句 tickets 复数标对 ⇒ 形态类，只记录）

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

### 340 · a step up from that（递进到更高一档；⛔ on top of that 是平级追加）
类型 词组 ｜ 新建 2026-09-13 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 整句 ｜ **回潮 2026-10-22**（09-21 毕业 → 10-22 复检第 5 组 [5] `taking it a step up is being able to …`：没落到块 a step up from that、退回动词的路，撤销毕业、连对清零）

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
- 2026-10-04 ✅ 复检 · 付息日 a2 复检第 3 组 [4] · `Knowing how to cook is one thing; a step up from that is pulling off a proper New Year's Eve feast.` —— a step up from that
- 2026-10-22 ❌ 复检 · 付息日 a2 段复检第 5 组 [5] · `Knowing how to drive is one thing; taking it a step up is being able to drive steadily in a blizzard.` —— "再往上一档"没落到块 a step up from that，退回动词的路（take it a step further 与 take it up a notch 混搭）⇒ 最小改 a step up from that is being able to … ⇒ 🎓 回潮
- 2026-10-24 ✅ 学习日 在池第 1 组 [1] · `Being polite is just the baseline for hotel staff; a step up from that is actually remembering a regular guest's personal preferences.` —— a step up from that（step 当名词、from 在；没退回 10-22 taking it a step up 的动词路）。连错 1 → 连对 1

### 525 · **on the doorstep**（家门口：东西放在某户人家门外那一小块；⛔ at the entrance）
类型 词组 ｜ 新建 2026-10-22
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 整句

**问题是什么**
**on the doorstep** ＝ 家门口（门外紧挨着门的那一小块地方）：`left the package on my doorstep` · `found a bag of oranges on the doorstep`。
同一格里的邻居（别串）：at the door／outside the door（门口，泛说）· on the porch（独栋房子的门廊）· **entrance**（入口，多指楼、商场、场馆的大门：the building entrance）· 比喻义 right on our doorstep ＝ 就在家门口、离得很近（范文里见过，考点不是它）。
判据一句话：东西放在某户人家门外 ⇒ on the doorstep／at the door；楼、场馆的大门 ⇒ entrance。
★ 题型判整句："门口"能落到 at the door／outside the door 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 doorstep。

**怎么发现的**
2026-10-22 付息日 a 段在池第 1 组 [8]（#517 题面"快递员连门都没敲，直接把包裹扔在了门口。"）· 原话
`The delivery guy didn't even bother knocking on the door—he just dropped the package at the entrance.`
考点 bother 用对（#517 ✅）；diff-2 ⚠️："门口"落成 at the entrance —— entrance 多指楼或场馆的入口，敲门的那扇门外面 ⇒ on the doorstep ⇒ §3.2b 能学的表达 ⇒ 建号（同 🎓#443 先例：diff-2 ⚠️ 建号记 ❌ 首犯）。
判重三步：
　① 目标形式 dedup "doorstep" ⇒ 零命中（她自己没产出过；只在 examples 范文里出现过比喻义 on our doorstep）
　　 dedup "entrance" ⇒ 🎓#375（cardboard box）· #436（downstairs from）· 🎓#502（cram school）· #519（run errands）—— 只是历史行里带 entrance 字样 ⇒ 否
　② 中文 dedup "门口" ⇒ 🎓#453（apartment complex，考"小区"）· 🎓#16（get sb to do）· 🎓#428（be featured in）· 🎓#443（office）· 🎓#473（楼外街上经过 past／by my building）· #436（downstairs from）—— 都只是题面／正文里带"门口"二字，没有一条以"家门口 ＝ doorstep"为考点 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`dropped the package at the entrance`　　更地道：`dropped the package on the doorstep`
找法：说"放在（谁家）门口"先落 on the doorstep；entrance 留给楼、商场、场馆的大门。

**题面**
"早上一开门，发现门口放着一袋邻居送来的橘子。"（"门口"用 **doorstep** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：When I opened the door this morning, I found a bag of oranges from my neighbor on the doorstep.

- 2026-10-22 ❌ 首犯 · 付息日 a 段在池第 1 组 [8]（#517 题里）· diff-2 ⚠️ · 原话 `The delivery guy didn't even bother knocking on the door—he just dropped the package at the entrance.` ⇒ 更好版 on the doorstep
- 2026-10-24 ✅ 学习日 在池第 1 组 [10] · `I opened my door this morning to find a bag of oranges left on my doorstep by a neighbor.` —— on my doorstep。连错 1 → 连对 1

### 526 · **down jacket**（羽绒服；也说 puffer jacket）
类型 词汇 ｜ 新建 2026-10-22 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 词组

**问题是什么**
**down jacket** ＝ 羽绒服（里面填鸭绒／鹅绒的冬衣）：`a long down jacket` · `a lightweight down jacket`；口语也常说 `puffer jacket`（鼓鼓的那种）。
同一格里的邻居（别串）：down ＝ 羽绒（a down comforter 羽绒被）· padded jacket（棉服，填的是棉／化纤）· parka（带帽子的长款厚外套）。
判据一句话：填羽绒的冬衣 ⇒ down jacket／puffer jacket；填棉的 ⇒ padded jacket。
★ 题型判词组：一个名词块，缺口只是调不调得出来；"羽绒服"映射回 down jacket（答 puffer jacket 合法且贴题面 ⇒ 照判 ✅）。

**怎么发现的**
2026-10-22 付息日 a2 段复检第 3 组 [1]（🎓#467 题面"这家洗衣店洗一件羽绒服要六十块。"）· 原话
`This dry cleaner charges sixty bucks to clean a down jacket（背下）.`
她用对了 down jacket，但自己标「背下」⇒ §2③ 她说要背 ⇒ 建号（同 #519–#524 先例：标背下建号记 ❌ 首犯）。
判重三步：
　① 目标形式 dedup "down jacket" ⇒ 零命中
　② 中文 dedup "羽绒服" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `a down jacket`，但词不在手边（自己标背下）　　目标：同她原句
找法：说"羽绒服"先落 down jacket（down 就是羽绒）。

**题面**
"冬天去哈尔滨要带的那件长款羽绒服"（里面填满鸭绒、鼓鼓囊囊的那种冬衣）
★ 目标形式（教练看，⛔ 不进发题稿）：the long down jacket you need to bring to Harbin in winter

- 2026-10-22 ❌ 首犯 · 付息日 a2 段复检第 3 组 [1]（#467 题里）· 她标「背下」· 原话 `This dry cleaner charges sixty bucks to clean a down jacket（背下）.`
- 2026-10-24 ✅ 学习日 在池第 2 组 [1] · `that long down jacket you've gotta take for a winter trip to Harbin` —— down jacket。连错 1 → 连对 1

### 527 · **in public**（在公共场合、当着外人的面；反义 in private）
类型 词组 ｜ 新建 2026-10-22 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 整句

**问题是什么**
**in public** ＝ 在公共场合、当着外人的面：`Don't argue in public.` · `She never cries in public.` · `beat up a thief in public`；反义 **in private**（私下）。块里⛔不带 the。
同一格里的邻居（别串）：publicly（副词，偏正式：publicly apologize）· in front of everyone（当着所有人）· in broad daylight（光天化日之下）· in the street（在大街上）。
判据一句话：有外人看得见的场合 ⇒ in public；关起门来 ⇒ in private。
★ 题型判整句："当众／当着别人的面"能落到 in front of everyone／publicly 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 in public。

**怎么发现的**
2026-10-22 付息日 a2 段复检第 3 组 [3]d（🎓#498 题面"新闻里那个当街暴打小偷、后来被警察带走的义警"）· 原话
`that vigilante in the news who beat up a thief in public（背下) and was taken away by the police`
她用对了 in public，但自己标「背下」⇒ §2③ 她说要背 ⇒ 建号（同 #519–#524 先例）。
判重三步：
　① 目标形式 dedup "in public" ⇒ 零命中
　② 中文 dedup "当街" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `in public`，但块不在手边（自己标背下）　　目标：同她原句
找法：说"当众／当着外人的面／在公共场合"先落 in public（⛔ 不带 the）。

**题面**
"我妈从来不在外面当着别人的面骂我，都是回家再说。"（"在外面当着别人的面"用 **in public** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My mom never scolded me in public — she always waited until we got home.

- 2026-10-22 ❌ 首犯 · 付息日 a2 段复检第 3 组 [3]d（#498 题里）· 她标「背下」· 原话 `that vigilante in the news who beat up a thief in public（背下) and was taken away by the police`
- 2026-10-24 ✅ 学习日 在池第 2 组 [2] · `My mom never scolds me in public—she always saves it for when we get back home.` —— in public。连错 1 → 连对 1

### 528 · **get the hang of sth**（摸到窍门、上手了：got the hang of it）
类型 词组 ｜ 新建 2026-10-22 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 整句

**问题是什么**
**get the hang of sth** ＝ 摸到窍门、上手（一件要动手的事，刚开始不会，慢慢会了）：`It took me a week to get the hang of the new software.` · `Once you get the hang of it, it's easy.` · `she got the hang of it in no time`。hang 前面固定是 the。
同一格里的邻居（别串）：🎓#279 get a feel for sth（对一个领域摸出感觉，偏体感）· get used to sth（习惯，偏适应）· pick up（学会，偏学得快）。
判据一句话：一件"手上的活"从不会到会 ⇒ get the hang of；对一个领域生出直觉 ⇒ get a feel for。
★ 与 🎓#279 分工：那条考 a feel for／the feel of 的冠词＋介词，本条是 hang 这个块 ⇒ 两个块，各走各的。
★ 题型判整句："上手／摸到窍门"能落到 figure it out／pick it up／get used to it 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 hang。

**怎么发现的**
2026-10-22 付息日 a2 段复检第 3 组 [6]（🎓#489 题面"我妹妹学游泳特别快，没几天就会了。"）· 原话
`My little sister learned to swim remarkably fast—she got the hang of it（这个短语背下) in no time.`
她用对了 got the hang of it，但自己标「这个短语背下」⇒ §2③ 她说要背 ⇒ 建号（同 #519–#524 先例）。
判重三步：
　① 目标形式 dedup "hang of" ⇒ 🎓#279（正文把 get the hang of 列为同族邻居，考点是 a feel for／the feel of）· 🎓#206（历史行里教练给过的口语版 get the hang of managing their own time）⇒ 都否：hang ≠ feel，两个块；#206 是书面词降级的登记条，不考这个块
　② 中文 dedup "上手" ⇒ 🎓#279 · 🎓#510（ins and outs）· 🎓#291（Let me …）—— 只是正文／历史带"上手"二字 ⇒ 全否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `got the hang of it`，但块不在手边（自己标背下）　　目标：同她原句
找法：说"上手了／摸到窍门了"先落 get the hang of it（hang 前面有 the）。

**题面**
"这台新咖啡机按钮太多了，我用了一个星期才摸到窍门。"（"摸到窍门"用 **hang** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：This new coffee machine has way too many buttons — it took me a week to get the hang of it.

- 2026-10-22 ❌ 首犯 · 付息日 a2 段复检第 3 组 [6]（#489 题里）· 她标「这个短语背下」· 原话 `My little sister learned to swim remarkably fast—she got the hang of it（这个短语背下) in no time.`
- 2026-10-24 ✅ 学习日 在池第 2 组 [3] · `There are way too many buttons on this new coffee maker; it took me a week to finally get the hang of it.` —— get the hang of it。连错 1 → 连对 1

### 529 · **smash sth in**（把窗户／门砸破、砸进去：had my car window smashed in）
类型 词组 ｜ 新建 2026-10-22 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 整句

**问题是什么**
**smash sth in** ＝ 用力把窗、门、玻璃砸破，砸得往里塌：`Someone smashed in my car window.` · `I had my car window smashed in.`；宾语是代词时放中间：`smash it in`。
同一格里的邻居（别串）：smash ＝ 砸碎（smash a plate）· break into a car（撬车、闯进车里偷东西）· shatter（玻璃自己碎成渣）· 🎓#497 have ＋ 东西 ＋ done（遭遇：had my window smashed in 用的就是那个结构）。
判据一句话：有人用力把窗／门砸破 ⇒ smash in；只说东西碎了 ⇒ smash／break；闯进去偷 ⇒ break into。
★ 题型判整句："砸破／被砸了"能落到 broke／smashed 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 smash in。

**怎么发现的**
2026-10-22 付息日 a2 段复检第 4 组 [2]（🎓#497 题面"我停在路边的车被人砸了车窗。"）· 原话
`I had my car window smashed in（这个词组背下） while parked on the street.`
她用对了 smashed in，但自己标「这个词组背下」⇒ §2③ 她说要背 ⇒ 建号（同 #519–#524 先例：标背下建号记 ❌ 首犯）。
判重三步：
　① 目标形式 dedup "smash" ⇒ 零命中
　② 中文 dedup "砸" ⇒ 🎓#398（be on the line：标题里"搞砸"的字样）⇒ 否；🎓#497 是她这次答题的条目，考 have ＋ 东西 ＋ done 结构，不考 smash in ⇒ 否（★ 建号时这一步漏跑、写了「未单独跑」，收尾 1b 补跑后改写）
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `smashed in`，但块不在手边（自己标背下）　　目标：同她原句
找法：说"（窗户／门）被砸了"先落 smash in。

**题面**
"小偷砸破了店里的玻璃门，把收银机偷走了。"（"砸破"用 **smash in** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The thieves smashed in the shop's glass door and stole the cash register.

- 2026-10-22 ❌ 首犯 · 付息日 a2 段复检第 4 组 [2]（#497 题里）· 她标「这个词组背下」· 原话 `I had my car window smashed in（这个词组背下） while parked on the street.`
- 2026-10-24 ✅ 学习日 在池第 2 组 [7] · `The thief smashed in the store's glass door and made off with the cashiet.` —— smashed in the store's glass door。连错 1 → 连对 1
  ｜ 同句 cashier（收银员）≠ 收银机 ⇒ 另建 #539

### 530 · **come top (of sth)**（拿第一：came top of her grade；⛔ came the top of）
类型 搭配 ｜ 新建 2026-10-22
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 整句

**问题是什么**
**come top (of the class／of her grade／in the exam)** ＝ 考第一、排第一，**top 前不加 the**。也说 **come first in** ＋ 范围（came first in her grade）。
同一格里的邻居（别串）：be (at) the top of the class（在班里排第一的那个位置 —— 这里有 the）· rank first（排名第一，偏正式）· 🎓#434 two years straight（连续两年）。
判据一句话：动词是 come ⇒ come top（无 the）／come first；动词是 be ⇒ be (at) the top of。
★ 题型判整句：考点是 come 后面 top 带不带 the，靠句子才现形；类型 搭配、缺口不是"调不调得出来" ⇒ 整句 ＋ 正向点名 come top。

**怎么发现的**
2026-10-22 付息日 a2 段复检第 4 组 [5]（🎓#434 题面"她连续两年拿了全年级第一。"）· 原话
`She came the top of the grade for two straight years.`
#434 的 straight 对（✅）；"拿第一"落成 came the top of —— 把 come top of 与 be the top of 两个块混了 ⇒ ❌ 真错（搭配：块内的冠词是块的一部分，⛔ 不是形态类：同一篇没有她做对过的同一形态）。
判重三步：
　① 目标形式 dedup "came top" ⇒ 零命中；dedup "top of" ⇒ 🎓#340（a step up from that，⛔ on top of that）· ⛔#56 · 🎓#81 #98 #206 #254 #317 #422 #445（历史行字样）⇒ 全否
　② 中文 dedup "第一名" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`came the top of the grade`　　正确：`came top of her grade` ／ `came first in her grade`
找法：说"拿了第一"先落 came top of ／ came first in —— 动词是 come，top 前面就不加 the。

**题面**
"我表弟这次期末考试考了全班第一。"（"考了第一"用 **come top** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My cousin came top of his class in the final exams this term.

- 2026-10-22 ❌ 首犯 · 付息日 a2 段复检第 4 组 [5]（#434 题里）· 原话 `She came the top of the grade for two straight years.` ⇒ 最小改 came top of the grade（更好版 came top of her grade）
- 2026-10-24 ✅ 学习日 在池第 2 组 [5] · `My cousin came top of his class in this semester's finals.` —— came top of his class（不带 the）。连错 1 → 连对 1

### 531 · **pass out**（晕倒、昏过去）
类型 词组 ｜ 新建 2026-10-22 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 整句

**问题是什么**
**pass out** ＝ 晕倒、失去知觉（口语最常用）：`He passed out from the heat.` · `I nearly passed out.` · `An old man passed out on the subway.`
同一格里的邻居（别串）：faint（晕倒，偏书面一点）· black out（眼前一黑、断片）· collapse（突然倒下，不一定昏过去）· come to／come around（醒过来）。
判据一句话：说"晕倒、昏过去"口语先 pass out；醒过来 ⇒ come to。
★ 题型判整句："晕倒"能落到 faint／collapse 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 pass out。

**怎么发现的**
2026-10-22 付息日 a2 段复检第 4 组 [7]（🎓#335 题面"有个老人在地铁上晕倒了，周围的人都愣住了，只有他马上采取了行动。"）· 原话
`An old man passed out（这个词组学下） on the subway and people around just froze, but he was the only one who took action right away.`
她用对了 passed out，但自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号（同 #519–#524 先例）。
判重三步：
　① 目标形式 dedup "pass out"／"passed out" ⇒ 零命中
　② 中文 dedup "晕倒" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `passed out`，但块不在手边（自己标学下）　　目标：同她原句
找法：说"晕倒了"先落 passed out。

**题面**
"天太热了，好几个军训的学生站着站着就晕倒了。"（"晕倒"用 **pass out** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：It was so hot that several students passed out while standing at military training.

- 2026-10-22 ❌ 首犯 · 付息日 a2 段复检第 4 组 [7]（#335 题里）· 她标「这个词组学下」· 原话 `An old man passed out（这个词组学下） on the subway and people around just froze, but he was the only one who took action right away.`
- 2026-10-24 ✅ 学习日 在池第 2 组 [4] · `It was so hot that a few students passed out right while standing during military training.` —— passed out。连错 1 → 连对 1
  ｜ ⚠️ right while standing → right where they stood ⇒ 另建 #538

### 532 · **credit**（功劳、认可）不可数：deserve credit · give sb credit（⛔ credits）
类型 词汇 ｜ 新建 2026-10-22
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 整句

**问题是什么**
**credit** 当"功劳、认可"讲**不可数**：`deserve credit` · `give sb credit for sth` · `take (the) credit for sth` · `get all the credit`；要加量用 a lot of／most of the credit。
加了 s 的 **credits** 是另一个意思：学分（earn 30 credits）、片尾字幕（the credits）。
同一格里的邻居（别串）：🎓#341 deserve vs worth（那条管动词，本条管名词可数性）· praise 同样不可数（deserve praise）。
判据一句话：说"功劳／认可" ⇒ credit 不加 s；说学分、字幕 ⇒ credits。
★ 与 🎓#261 分工：#261 正文写明「具体某个词的可数性各留各条」⇒ 本条单列，⛔ 不往已毕业的合并条里塞成员。
★ 题型判整句：可数性靠句子才现形；类型 词汇但考点是"加不加 s"，孤立翻"功劳"测不到 ⇒ 整句 ＋ 正向点名 credit。

**怎么发现的**
2026-10-22 付息日 a2 段复检第 4 组 [10]（🎓#341 题面"这次运动会办得这么顺利，那些志愿者真值得表扬。"）· 原话
`Since the sports event went so smoothly, those volunteers truly deserve credits.`
#341 的 deserve 对（✅，没落成 worth praise）；credit 加了 s ⇒ ❌（credits ＝ 学分／字幕，换了词义 ⇒ 选词层面，⛔ 不是形态类）。
★ 如实记：2026-10-01 复检 #341 她写过 `deserves a lot of credit`（对）—— 不在同一篇，§3.4 执行自查口径是"同一篇"⇒ 不按形态类 ⚪ 处理；若下次单独测稳，就照常两次毕业。
判重三步：
　① 目标形式 dedup "credit" ⇒ 🎓#341（deserve praise／credit：考 deserve vs worth）· 🎓#27（the credit gets shared：考 get-passive，已退池）⇒ 都否
　② 规则层：🎓#261（这一小撮抽象名词不可数）⇒ 同类规则，但该条正文写明具体词的可数性各留各条 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`deserve credits`　　正确：`deserve credit`
找法：写完 credit 回头看一眼：说的是功劳吗？是 ⇒ 去掉 s。

**题面**
"这个项目能做成，小王的功劳最大。"（"功劳"用 **credit** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Xiao Wang deserves most of the credit for getting this project done.

- 2026-10-22 ❌ 首犯 · 付息日 a2 段复检第 4 组 [10]（#341 题里）· 原话 `Since the sports event went so smoothly, those volunteers truly deserve credits.` ⇒ 最小改 deserve credit
- 2026-10-24 ✅ 学习日 在池第 2 组 [6] · `Xiao Wang deserves the most credit for getting this project off the ground.` —— the most credit（不可数，没加 s）。连错 1 → 连对 1

### 533 · **wreath**（花环、花圈：a Christmas wreath）
类型 词汇 ｜ 新建 2026-10-22 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 词组

**问题是什么**
**wreath** ＝ 编成一圈的花环／花圈：`a Christmas wreath`（圣诞节挂在门上的那种）· `lay a wreath`（献花圈）。
同一格里的邻居（别串）：garland（一长条的花环、彩带，挂着或戴着）· bouquet（一束花）· 🎓#98（她在那题里说 This wreath is made from …，考点是并列同形）。
判据一句话：编成圆圈的 ⇒ wreath；一长串的 ⇒ garland；一把 ⇒ bouquet。
★ 题型判词组：一个名词，缺口只是调不调得出来；"花环／花圈"映射回 wreath，唯一可判。

**怎么发现的**
2026-10-22 付息日 a2 段复检第 5 组 [4]②（🎓#98 题面"这个花环是用松果和丝带做的。"）· 原话
`This wreath（背下) is made from pinecones（背下) and ribbons（背下).`
她用对了 wreath，但自己标「背下」⇒ §2③ 她说要背 ⇒ 建号（一词一条，§3.2；同 #519–#524 先例）。
判重三步：
　① 目标形式 dedup "wreath" ⇒ 零命中
　② 中文 dedup "花环" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `wreath`，但词不在手边（自己标背下）　　目标：同她原句
找法：说"花环／花圈"先落 wreath。

**题面**
"圣诞节挂在大门上的那个花环"（用常青树枝编成一圈的那种装饰）
★ 目标形式（教练看，⛔ 不进发题稿）：the Christmas wreath hanging on the front door

- 2026-10-22 ❌ 首犯 · 付息日 a2 段复检第 5 组 [4]②（#98 题里）· 她标「背下」· 原话 `This wreath（背下) is made from pinecones（背下) and ribbons（背下).`
- 2026-10-24 ✅ 学习日 在池第 2 组 [8] · `that christmas wreath hanging over the fireplace` —— wreath。连错 1 → 连对 1

### 534 · **pinecone**（松果；也写 pine cone）
类型 词汇 ｜ 新建 2026-10-22 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 词组

**问题是什么**
**pinecone** ＝ 松果（松树结的、一片片鳞片的那种）：`collect pinecones` · `a squirrel nibbling on a pinecone`；也写 pine cone。
同一格里的邻居（别串）：pine（松树）· pine needles（松针）· acorn（橡子）· pine nuts（松子，吃的那种）。
判据一句话：松树结的那个"球" ⇒ pinecone；里面能吃的仁 ⇒ pine nuts。
★ 题型判词组：一个名词，缺口只是调不调得出来；"松果"映射回 pinecone，唯一可判。

**怎么发现的**
2026-10-22 付息日 a2 段复检第 5 组 [4]②（🎓#98 题面"这个花环是用松果和丝带做的。"）· 原话
`This wreath（背下) is made from pinecones（背下) and ribbons（背下).`
她用对了 pinecones，但自己标「背下」⇒ §2③ 她说要背 ⇒ 建号（一词一条，§3.2）。
判重三步：
　① 目标形式 dedup "pinecone"／"pine cone" ⇒ 零命中
　② 中文 dedup "松果" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `pinecones`，但词不在手边（自己标背下）　　目标：同她原句
找法：说"松果"先落 pinecone（pine ＋ cone）。

**题面**
"松鼠抱着啃的那颗松果"（松树上结的、一片片鳞片的那种）
★ 目标形式（教练看，⛔ 不进发题稿）：the pinecone the squirrel is gnawing on

- 2026-10-22 ❌ 首犯 · 付息日 a2 段复检第 5 组 [4]②（#98 题里）· 她标「背下」· 原话 `This wreath（背下) is made from pinecones（背下) and ribbons（背下).`
- 2026-10-24 ✅ 学习日 在池第 2 组 [9] · `that pinecone the squirrel was munching on(这个词组学下)` —— pinecone。连错 1 → 连对 1
  ｜ 她标 munching on「这个词组学下」⇒ §2③ 另建 #540

### 535 · **ribbon**（丝带、缎带：tie a ribbon · cut the ribbon）
类型 词汇 ｜ 新建 2026-10-22 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-24 未毕业 ｜ 题型 词组

**问题是什么**
**ribbon** ＝ 丝带、缎带：`tie a ribbon around the box` · `a red ribbon` · `cut the ribbon`（剪彩）。
同一格里的邻居（别串）：bow（蝴蝶结，丝带打成的结）· string（细绳）· lace（蕾丝、鞋带）。
判据一句话：扎礼物、扎头发的那种带子 ⇒ ribbon；打成的结 ⇒ bow。
★ 题型判词组：一个名词，缺口只是调不调得出来；"丝带"映射回 ribbon，唯一可判。

**怎么发现的**
2026-10-22 付息日 a2 段复检第 5 组 [4]②（🎓#98 题面"这个花环是用松果和丝带做的。"）· 原话
`This wreath（背下) is made from pinecones（背下) and ribbons（背下).`
她用对了 ribbons，但自己标「背下」⇒ §2③ 她说要背 ⇒ 建号（一词一条，§3.2）。
判重三步：
　① 目标形式 dedup "ribbon" ⇒ 零命中
　② 中文 dedup "丝带" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `ribbons`，但词不在手边（自己标背下）　　目标：同她原句
找法：说"丝带／彩带"先落 ribbon。

**题面**
"礼物盒上系的那条红丝带"（打成蝴蝶结的那种带子）
★ 目标形式（教练看，⛔ 不进发题稿）：the red ribbon tied around the gift box

- 2026-10-22 ❌ 首犯 · 付息日 a2 段复检第 5 组 [4]②（#98 题里）· 她标「背下」· 原话 `This wreath（背下) is made from pinecones（背下) and ribbons（背下).`
- 2026-10-24 ✅ 学习日 在池第 2 组 [10] · `that red ribbon tied in a bow on the gift box` —— ribbon。连错 1 → 连对 1

### 537 · **put together ＋ 东西**（自己挑选、拼排出一整份：put together an itinerary／a menu／a playlist）
类型 词组 ｜ 新建 2026-10-24 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-24 未毕业 ｜ 题型 整句

**问题是什么**
**put together ＋ 东西** ＝ 把零散的几样挑出来、排好，组合成一整份（行程、菜单、歌单、PPT、一支队伍）：
`I put together a three-day itinerary myself.` · `She put together the menu for the party.` · `put together a playlist／a presentation／a team`
宾语是代词时夹在中间：`put it together`。
同一格里的邻居（别串）：plan（只说"打算"，没有"一样样拼起来"那层）· 🎓#431 well planned out（规划得好、布局合理）· 🎓#456 carefully crafted（精心打磨，偏"做工"）· throw together（仓促凑出来，带"随便"）· 🎓#481 plan a surprise for sb（那条管 throw 只配活动，本条管 put together 这个块本身）。
判据一句话：东西是一样样挑、一样样排出来的一整份 ⇒ put together；只是"打算" ⇒ plan。
★ 题型判整句："排／搭／张罗出来"能落到 plan／make／arrange 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 put together。

**怎么发现的**
2026-10-24 学习日 在池第 1 组 [9]（#524 题面"我自己排的三天东京行程"）· 原话
`that three-day Tokyo itinerary I put together(这个词组学下) myself`
她用对了、自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #506 #518 #519 #522 先例）。
判重三步：
　① 目标形式 dedup "put together" ⇒ 🎓#456（crafted，正文邻居里提了一句 put together 拼凑）· 🎓#481（plan a surprise，正文里 put together a surprise 是备选说法）⇒ 两条的考点都不是 put together 这个块本身 ⇒ 否；"put it together"／"throw together"／"compile"／"map out" ⇒ 零命中
　② 中文 dedup "安排" ⇒ #524 itinerary（名词"行程"，本条是动词块）· 🎓#431 well planned out（另一个块）· 🎓#53 organized · 🎓#464 tactics 等只是正文／题面字样 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `the itinerary I put together myself`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"排了一份／搭了一份／张罗出一份（计划、菜单、歌单）"，先试 put together ＋ 那份东西。

**题面**
"生日聚会的菜单是我朋友一个人张罗着搭出来的。"（"搭出来"用 **put together** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My friend put together the whole menu for the birthday party on her own.

- 2026-10-24 ❌ 首犯 · 学习日 在池第 1 组 [9]（#524 题里）· 她标「这个词组学下」· 原话 `that three-day Tokyo itinerary I put together(这个词组学下) myself`

### 538 · **right where sb stood／was**（就在原地：站着站着就倒下、原地不动；⛔ right while standing）
类型 词组 ｜ 新建 2026-10-24
状态 连对0 连错1 上次2026-10-24 未毕业 ｜ 题型 整句

**问题是什么**
**right where ＋ 人 ＋ stood／was standing／was** ＝ 就在（他）原来站着／待着的那个地方：
`passed out right where they stood` · `He collapsed right where he stood.` · `Stay right where you are.`
同一格里的邻居（别串）：on the spot（当场，偏"时间上立刻"）· right there（就在那儿，泛指）· 🎓#163 I just stood there（愣住了，说的是反应，不是地点）。
判据一句话：说"就倒在原地／就在原地没动" ⇒ right where ＋ 人 ＋ stood／was；说"当场立刻" ⇒ on the spot。
★ right 后面通常接一个**时间点**（right as／right after／right before）；standing 是一段持续的状态，挂上 right while 读着别扭。
★ 题型判整句："原地"能落到 on the spot／right there 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-24 学习日 在池第 2 组 [4]（#531 题面"天太热了，好几个军训的学生站着站着就晕倒了。"）· 原话
`It was so hot that a few students passed out right while standing during military training.`
考点 pass out 用对（#531 ✅）；diff-2 ⚠️："站着站着就倒下"落成 right while standing，生硬 ⇒ right where they stood ⇒ §3.2b 能学的表达 ⇒ 建号（同 #525 先例：diff-2 ⚠️ 建号记 ❌ 首犯）。
判重三步：
　① 目标形式 dedup "where they stood"／"where he"／"keel" ⇒ 零命中；"on the spot" ⇒ 🎓#517（历史行字样）⇒ 否；"stood" ⇒ 🎓#163（I just stood there ＝ 愣住，另一个块）· 🎓#212 #16 #152 #167 #12（历史／正文字样）⇒ 否
　② 中文 dedup "原地" ⇒ 🎓#490（stay on 正文字样）⇒ 否；"站着" ⇒ 🎓#270 #324（正文字样）· #531（本题题面）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`passed out right while standing during military training`　　更地道：`passed out right where they stood during military training`
找法：中文"站着站着就…／就在原地…"，先落 right where ＋ 人 ＋ stood。

**题面**
"他跑完马拉松，一过终点线就在原地瘫倒了。"（"就在原地"用 **right where** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：He finished the marathon and collapsed right where he stood the moment he crossed the finish line.

- 2026-10-24 ❌ 首犯 · 学习日 在池第 2 组 [4]（#531 题里）· diff-2 ⚠️ · 原话 `It was so hot that a few students passed out right while standing during military training.` ⇒ 更好版 right where they stood

### 539 · **cash register**（收银机；⛔ cashier ＝ 收银员，是人）
类型 词汇 ｜ 新建 2026-10-24
状态 连对0 连错1 上次2026-10-24 未毕业 ｜ 题型 词组

**问题是什么**
**cash register** ＝ 收银机（口语常省成 the register；英式 the till）：`made off with the cash register` · `open the register`。
同一格里的邻居（别串）：**cashier**（收银员，人）· checkout（结账台、收银台那个位置）· receipt（小票）。
判据一句话：说的是机器 ⇒ cash register；说的是人 ⇒ cashier；说的是排队结账的那个位置 ⇒ checkout。
★ 题型判词组：一个名词块，缺口只是调不调得出来；"收银机"＋括号"那台机器"映射回 cash register，唯一可判。

**怎么发现的**
2026-10-24 学习日 在池第 2 组 [7]（#529 题面"小偷砸破了店里的玻璃门，把收银机偷走了。"）· 原话
`The thief smashed in the store's glass door and made off with the cashiet.`
考点 smash in 用对（#529 ✅）；"收银机"调成了 cashier（收银员）⇒ 选词错（§2.1：她调的是另一个词，照常算；cashiet 的 t 属拼写不算）⇒ 建号。
判重三步：
　① 目标形式 dedup "cash register" ⇒ #529（历史行里的目标形式字样）⇒ 否；"cashier" ⇒ 零命中
　② 中文 dedup "收银" ⇒ #529（题面字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`made off with the cashiet`（＝ cashier）　　正确：`made off with the cash register`
找法：说"收银…"先问一句 —— 是那台机器、那个人，还是那个台子？

**题面**
"超市结账台上那台收银机"（收钱、打小票、抽屉里放现金的那台机器）
★ 目标形式（教练看，⛔ 不进发题稿）：the cash register at the supermarket checkout

- 2026-10-24 ❌ 首犯 · 学习日 在池第 2 组 [7]（#529 题里）· 原话 `The thief smashed in the store's glass door and made off with the cashiet.`

### 540 · **munch on sth**（大口地嚼、咔嚓咔嚓地啃：munch on chips／an apple）
类型 词组 ｜ 新建 2026-10-24 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-24 未毕业 ｜ 题型 整句

**问题是什么**
**munch on ＋ 吃的** ＝ 一口一口地嚼（吃得香、有声音，多说零食、水果）：`munching on chips` · `munch on an apple` · `the squirrel was munching on a pinecone`。
同一格里的邻居（别串）：chew（嚼，最泛）· gnaw on（啃硬东西：狗啃骨头）· nibble on（小口小口地啃）· snack on（吃零食，说的是吃什么）。
判据一句话：吃得香、嘎吱嘎吱嚼 ⇒ munch on；啃硬的、费劲 ⇒ gnaw on；小口小口 ⇒ nibble on。
★ 题型判整句："嚼／啃"能落到 chew／gnaw／nibble 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 munch on。

**怎么发现的**
2026-10-24 学习日 在池第 2 组 [9]（#534 题面"松鼠抱着啃的那颗松果"）· 原话
`that pinecone the squirrel was munching on(这个词组学下)`
她用对了、自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #518 #522 #537 先例）。
判重三步：
　① 目标形式 dedup "munch" ⇒ 零命中
　② 中文 dedup "啃" ⇒ 🎓#390（get through，啃完书，比喻）· 🎓#512（finish，"吃完"）· 🎓#415（历史字样）· #534（本题题面）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `the squirrel was munching on`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"嘎吱嘎吱地嚼／抱着啃（零食、苹果）"先试 munch on。

**题面**
"我弟弟一边看电影，一边抱着一大袋薯片嘎吱嘎吱地嚼。"（"嘎吱嘎吱地嚼"用 **munch on** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My brother was munching on a big bag of chips while watching the movie.

- 2026-10-24 ❌ 首犯 · 学习日 在池第 2 组 [9]（#534 题里）· 她标「这个词组学下」· 原话 `that pinecone the squirrel was munching on(这个词组学下)`

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

