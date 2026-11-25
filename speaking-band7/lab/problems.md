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
- 2026-11-06 ⚪ 学习日 ③ 重答 bank:489 S4 · `If cars just run red lights whenever they feel like it, the intersection gets totally jammed up and nobody could move.` —— 一般规律真实条件，gets 用对、could 滑（→ can）；同句做对过现在时 ⇒ §3.4 只记 ⚪

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
- 2026-10-30 ⚪ 学习日 在池第 2 组 [2]（#559 题里）· `long queues for photo` → `for photos` —— 可数名词单数光秃秃；同句 long queues 复数她自己做对 ⇒ 形态类只记录·不出题（检查触发：名词前停一下 —— 可数吗？单数就补 a／the，泛指就变复数）
- 2026-11-02 ⚪ 学习日 在池第 1 组 [8]（#568 题里）· `pitch our tent using flashlight` → using a flashlight —— 可数名词单数光秃秃；同组 a new refrigerator／a street vendor／a business trip 她都带对 ⇒ 形态类只记录·不出题（检查触发：名词前停一下 —— 可数吗？单数就补 a／the，泛指就变复数）
- 2026-11-08 ⚪ 付息日 复检第 4 组 [2]（🎓#340 题里）· `is basic skills` → is a basic skill —— 主语是一件事，表语该是单数 a basic skill；同组 a knee-length down coat／a pinecone／a large fruit platter 她都带对 ⇒ 形态类只记录·不出题（检查触发：名词前停一下 —— 可数吗？单数就补 a／the，泛指就变复数）


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
- 2026-10-27 ⚪ 付息日 d 段重答 bank:478 S4 · `we learned from TV news that …` → `from the TV news` —— 特指那一条新闻 ⇒ 带 the；形态类只记录·不出题（检查触发：名词前停一下 —— 指的是"那一个"吗？是 ⇒ the）
- 2026-10-30 ⚪ 学习日 复检第 4 组 [1]（🎓#469 题里）· `south of the downtown` → `south of downtown` —— downtown 当名词不带 the（多加了一个 the）；形态类只记录·不出题（检查触发：名词前停一下 —— 这个 the 是在指"那一个"吗？不是就删）
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

### 347 · "对于 X，他们…" ⇒ X 直接当主语（⛔ For office workers, they …）
类型 结构 ｜ 新建 2026-09-19
状态 连对0 连错1 上次2026-11-25 未毕业 ｜ 题型 整句 ｜ **回潮 2026-11-25**（10-14 第二次毕业 → 11-25 学习日重答 bank:1027 写成 `Even for someone like me who's …, I still can't help …`，For X 后再用 I 指回 X，撤销毕业、连对清零）｜ **回潮 2026-10-12**（09-22 毕业 → 10-12 复检 #277／#284 题里两次写成 `Planning a family trip, it's …`／`Whether a relationship can last long, it …`，话题后再用 it 回指，撤销毕业、连对清零）

**问题是什么**
中文话题句"对于上班族，他们…／对老人来说，他们…"先摆一个话题，再用代词把它重说一遍当主语。
★ 话题不止 For X：**动名词短语**（Planning a family trip, it's …）、**whether 从句**（Whether it lasts, it …）摆在句首再用 it 回指，同属本条 ——
　动名词短语／whether 从句本身就能当主语（Planning a family trip is mainly about …）；想保留"先摆话题"⇒ 用 When it comes to X, it's …（🎓#317）把话题包起来。
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
- 2026-10-05 ✅ 复检 · 学习日 复检第 4 组 [5] · `What young people lack the most is real-world experience.` —— 没有 For X, they 主语说两遍
- 2026-10-12 ❌ 付息日 a2 段复检第 6 组 [3]（#277 题里）· `Planning a family trip, it's mainly about setting a budget while giving everyone the freedom to pick their own spot.` —— 动名词短语当话题摆在句首、再用 it 重说一遍当主语 ⇒ 主语说两遍（同 For X, they … 一条规则）⇒ **回潮**
  最小改 `Planning a family trip is mainly about setting a budget while giving everyone the freedom to pick their own spot.`
  更好版 `When it comes to planning a family trip, it's mainly about …`（保留"先摆话题"就用 🎓#317 when it comes to 包起来）
  ★ 判据扩写：话题不止 For X —— 动名词短语／whether 从句摆在句首再用 it 回指，同属本条（问题是什么节补 ★ 行）
- 2026-10-12 ❌ 付息日 a2 段复检第 6 组 [8]（#284 题里）· `Whether a relationship can last long, it really boils down to whether both people are willing to talk things out.` —— whether 从句当话题摆在句首、再用 it 重说一遍当主语 ⇒ 主语说两遍（同一天第 2 行，§3.3 各记一次）
  最小改 `Whether a relationship can last long really boils down to whether both people are willing to talk things out.`
- 2026-10-13 ✅ 学习日 在池第 1 组 [3] · `For college freshmen, their biggest headache is usually figuring out how to get along with their roommates.` —— For X 后面换了另一个主语（their biggest headache），不是回指的 they。连错 2 → 连对 1
  ⚠️ diff-2：their biggest headache → the biggest headache（For X 已交代"谁的"，删回指词）
- 2026-10-14 ✅ 学习日 在池第 1 组 [3] · `For people living on their own, what scares them most is getting sick in the middle of the night with nobody around to take care of them.` —— For X 后面换了另一个主语（what scares them most），不是回指的 they。连对 1 → 2 ⇒ **🎓 毕业**（10-12 回潮后第二次毕业）
- 2026-10-19 ✅ 复检 · 学习日 复检第 4 组 [3] · `For many elementary school kids, summer break is the thing they look forward to the most` —— For X 之后换了主语 summer break，没有主语说两遍（她标 the most 要学 ⇒ 新建 #508）
- 2026-10-27 ✅ 复检 · 付息日 复检第 3 组 [9] · `For a lot of new mothers, what they lack the most is sleep.` —— 主句主语 what they lack the most（they 在主语从句里，⛔ 不是 For X, they … 主语说两遍）
- 2026-11-23 ✅ 付息日 复检第 5 组 [7] · `For a lot of international students, the hardest part is not being able to go home for Chinese New Year.` —— For X 后面没再用 they
- 2026-11-25 ❌ 学习日 重答 bank:1027（P2 · Describe an interesting building）[S10] · `Even for someone like me who's completely used to seeing it, I still can't help taking a second look whenever I walk by, simply because it's just so cute.` —— For X（someone like me）后面主语又用 I 指回 X ⇒ 主语说两遍 ⇒ **回潮**
  最小改 `Even someone like me who's completely used to seeing it still can't help taking a second look whenever I walk by, simply because it's just so cute.`
  更好版 `Even though I'm completely used to seeing it, I still can't help taking a second look whenever I walk by, simply because it's so cute.`（说自己就用 Even though I'm …，一个 I 到底）

### 440 · sentimental（煽情、催泪）≠ dramatic（夸张、戏剧化）
类型 词汇 ｜ 新建 2026-10-09 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 词组

**问题是什么**
**sentimental** ＝ 煽情、感情渲染过头、就想让人哭：`an overly sentimental ending`。
**dramatic** ＝ 戏剧化、起伏大、反应夸张：a dramatic ending（结局反转大、很有冲击力）· overly dramatic（演得太过、大惊小怪）。
同一格里的邻居（别串）：sappy（口语，酸、肉麻）· melodramatic（狗血、苦情那种夸张）。
判据一句话：重点在"催泪、感情泛滥" ⇒ sentimental；重点在"情节起伏、反应夸张" ⇒ dramatic。
★ 题型判词组：中文块"煽情的…"能映射回 sentimental（sappy／tear-jerking 合法照判）；再落到 dramatic ⇒ ❌。

**怎么发现的**
2026-10-09 学习日 复检第 3 组 [7]（#404 题面"我觉得这部电影的结局太煽情了。"）· 原话
`I felt like then ending of the movie was overly dramatic(这个词学下).`
她自己标「这个词学下」⇒ §2③ 建号，判 ❌；"煽情"落到 dramatic 只沾边（dramatic 是夸张、戏剧化，煽情是催泪、感情泛滥）⇒ 目标 sentimental。
判重三步：
　① 目标形式 dedup "sentimental"／"dramatic"／"melodramatic"／"sappy" ⇒ 零命中
　② 中文 dedup "煽情"／"催泪" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`overly dramatic`（她标「这个词学下」）　　更准：`overly sentimental`
找法：说"煽情"之前问一句 —— 是想让人哭（sentimental），还是演得夸张（dramatic）？

**题面**
"电视剧结尾那段特别煽情的告别戏"（故意把感情往上推、就为了让人哭的那种）

- 2026-10-09 ❌ 首犯 · 学习日 复检第 3 组 [7]（#404 题里）· 她标「这个词学下」· 原话 `I felt like then ending of the movie was overly dramatic(这个词学下).`
- 2026-10-10 ❌ 学习日 在池第 2 组 [2] · 「忘了」—— sentimental 没调出来（§3.3 "忘了"也是 ❌）。连错 1 → 2
  最小改 `the really sentimental farewell scene at the end of the TV series`
  ❌ "煽情" ＝ sentimental（催泪、感情泛滥）；⛔ 别落到 dramatic（情节起伏大、反应夸张）
- 2026-10-11 ✅ 学习日 在池第 1 组 [6] · `that super sentimental speech the groom gave at the wedding` —— sentimental。连错 2 → 连对 1
- 2026-10-12 ✅ 付息日 a 段在池第 1 组 [3] · `those super sentimental scenes in Mother's Day commercials` —— sentimental（没落到 dramatic）。连对 1 → 2 ⇒ **毕业**
- 2026-10-16 ✅ 复检 · 学习日 复检第 3 组 [3]a · `the principal's sentimental speech at graduation` —— sentimental。🎓 rc0 → rc1
- 2026-10-25 ✅ 复检 · 学习日 复检第 3 组 [9]a（打包）· `a sentimental background story on a talent show` —— sentimental（background story ⚠️ ⇒ 新建 #542 backstory）
- 2026-11-23 ❌ 付息日 复检第 3 组 [9] 打包 b · 忘了（动画片结尾那首特别煽情的主题曲）—— 目标 the overly sentimental theme song ⇒ 回潮
- 2026-11-25 ✅ 学习日 在池第 1 组 [1] · `that super sentimental background music in the wedding video`

### 458 · snuggle up（舒服地贴着／窝着：snuggle up to sb · on／in ＋ 地方）
类型 词组 ｜ 新建 2026-10-12 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**snuggle up** ＝ 舒舒服服地蜷着、贴着：`snuggle up to sb`（贴着某人）· `snuggle up on the couch`／`snuggle up in bed`（窝在沙发上／被窝里）· `snuggle up with a book`。
不带 up 时常跟 into：`snuggle into sb's arms`（钻进某人怀里）。
同一格里的邻居（别串）：cuddle（搂着、抱抱，偏"互相抱"）· curl up（蜷成一团，不一定贴着人）· nestle（偎依，偏书面）。
判据一句话：想说"贴着／窝着、很舒服" ⇒ snuggle up；后面是人 ⇒ to sb，是地方 ⇒ on／in ＋ 地方。
★ 题型判整句："依偎""窝着"能映射到 cuddle／curl up／nestle 一串合法说法 ⇒ 词组题零英文提示收不拢 ⇒ 整句 ＋ 正向点名。
★ 与 #459（in sb's arms）分工：本条考动词块 snuggle up，#459 考名词 arms／lap ⇒ 两个考点；本条题面 ⛔ 不出"怀里"（互斥）。

**怎么发现的**
2026-10-12 付息日 a 段在池第 1 组 [5]（#442 题面"我奶奶养的那只兔子特别亲人，总爱往人怀里钻。"）· 原话
`My grandma's rabbit is super affectionate and loves snuggling up（这个词组学下) into people's laps(怀里怎么说，不会).`
她写出了 snuggling up，但自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 🎓#433 先例：她标要学的块写对了也照判 ❌）。
判重三步：
　① 目标形式 dedup "snuggle"／"cuddl"／"nestle"／"curl up" ⇒ 零命中；dedup "hug" ⇒ 🎓#333 🎓#371 #442 —— 都只是历史行字串，考点不是它 ⇒ 否
　② 中文 dedup "依偎"／"钻" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（块不在手边）　　目标：`snuggling up into people's arms`／`snuggle up to sb`
找法：想说"贴着／窝着、很舒服"⇒ 先落 snuggle up，再看后面挂的是人（to）还是地方（on／in）。

**题面**
"下雨天我就想窝在沙发上，跟我女儿依偎在一起看电影。"（"依偎在一起"用 **snuggle up** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：On rainy days, I just want to snuggle up on the couch with my daughter and watch a movie.

- 2026-10-12 ❌ 首犯 · 付息日 a 段在池第 1 组 [5]（#442 题里）· 她标「这个词组学下」· 原话 `My grandma's rabbit is super affectionate and loves snuggling up（这个词组学下) into people's laps(怀里怎么说，不会).`
- 2026-10-13 ✅ 学习日 在池第 1 组 [9] · `On rainy days, I just like lounging(背一下) on the couch and snuggling up with my daughter to watch a movie.` —— snuggling up with ＋ 人。连错 1 → 连对 1 ｜ lounging 她标「背一下」⇒ 新建 #471
- 2026-10-14 ✅ 学习日 在池第 1 组 [4] · `On winter nights when we're watching TV, our cat loves to come over and snuggle up with me.` —— snuggle up with ＋ 人。连对 1 → 2 ⇒ **🎓 毕业**
- 2026-10-19 ✅ 复检 · 学习日 复检第 4 组 [4] · `It was a freezing night, and the two puppies snuggled up together to keep warm.`
- 2026-10-27 ✅ 复检 · 付息日 复检第 3 组 [10] · `My nephew needs to snuggle up with his huge teddy bear every night just to fall asleep.` —— snuggle up with
- 2026-11-23 ❌ 付息日 复检第 4 组 [8] 打包 c（#459 题里）· 她标「这个短语学下」· `the little granddaughter snuggled up in her grandma's arms watching TV` —— 写对了但她说要学（§3.2b 她说不会的地方照常判 ❌）⇒ 回潮
- 2026-11-25 ✅ 学习日 在池第 1 组 [2] · `she always loves to snuggle up in my arms`

### 656 · **a match**（红娘撮合成的一对：none of her matches worked out）
类型 词汇 ｜ 新建 2026-11-13
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**match**（名词）＝ 撮合／配对成的一对：`none of her matches have worked out` · `They're a perfect match.`
同一格里的邻居（别串）：pair ＝ 成对的东西（a pair of socks）· couple ＝ 已经在一起的一对 · set sb up（给人介绍对象）。
判据一句话：说"撮合／配成的那一对" ⇒ match。
★ 与 #646 play matchmaker 分工：那条考"当红娘"这个动作，本条考名词 match ⇒ 两条。
★ 题型判整句："撮合成的一对"能落到 couple 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 在池第 2 组 [5]（#646 题面"我姑姑最爱给年轻人当红娘，可惜一对都没成。"）· 原话
`My aunt loves playing matchmaker for young people, though sadly none of the pairs have worked out.`
⚠️ 不地道：pairs 用在撮合出来的人身上像在说成对的物件 ⇒ §3.2b 她的词搭不上 ⇒ 建号。
判重三步：
　① 目标形式 dedup "matches" ⇒ 只命中 #646（目标版里的字样）⇒ 考点不同（动作 vs 名词）⇒ 否
　② 中文 dedup "撮合" ⇒ 只命中 #646 ⇒ 同上否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：none of the pairs have worked out　　更地道：none of her matches have worked out
找法：说"配成的一对" ⇒ match，⛔ 不用 pair。

**题面**
"他们俩是我介绍认识的，算是我撮合成的第一对。"（"撮合成的一对"用 **match** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I introduced them to each other—they were my first successful match.

- 2026-11-13 ❌ 首犯 · 学习日 在池第 2 组 [5]（#646 题里）· ⚠️ 不地道 · 原话 `My aunt loves playing matchmaker for young people, though sadly none of the pairs have worked out.`
- 2026-11-14 ✅ 付息日 在池第 2 组 [7] · `they're pretty much my first successful match` —— 连错 1 → 连对 1
- 2026-11-15 ✅ 学习日 在池第 1 组 [5] · `Out of all the matches my aunt tried to make, not a single one worked out in the end.` —— 连对 1 → 2 ⇒ 🎓
- 2026-11-23 ❌ 付息日 复检第 2 组 [5] · `The couple our team leader made a match for is getting married next month.` —— make a match for ＋ 人 ＝ 给这人找对象，挂在 the couple 上意思偏了；最小改 matched up，更好版 One of our team leader's matches ⇒ 回潮
- 2026-11-25 ✅ 学习日 在池第 1 组 [3] · `Out of the matches she made last year, two couples have already gotten married.`

### 692 · **brighten up ＋ 地方**（植物、花、装饰让屋子好看、有生气：Plants really brighten up a room.）
类型 词组 ｜ 新建 2026-11-22
状态 连对1 连错0 上次2026-11-23 未毕业 ｜ 题型 整句

**问题是什么**
**brighten up** ＋ 地方 ＝ 让一个地方看着更亮堂、更有生气（植物、花、颜色、装饰）：`A few plants can really brighten up your place.` · `Fresh flowers brighten up the kitchen.`；也能说心情：`Her call brightened up my day.`
同一格里的邻居（别串）：light up ＝ 照亮（灯照亮屋子）· sb lights up the room ＝ 某人一来场面就热闹了（主语是人）· make sth look nice ＝ 让它好看（她 08-23 旧答用过，意思对、更平）。
判据一句话：主语是植物／花／装饰，让屋子好看有生气 ⇒ brighten up；真的是光 ⇒ light up。

**怎么发现的**
2026-11-22 学习日 ③ 重答 bank:220（P3 · Do many people grow vegetables or flowers at home in your country?）· 原话
`Young people grow plants too, mostly to light up their place, and they tend to go for potted plants since they're way less hassle.`
diff-2 ⚠️：light up their place 读起来像"照亮"，植物让家里好看的固定说法是 brighten up ⇒ §3.2b 能学的表达 ⇒ 建号。
判重三步：
　① 目标形式 dedup "brighten" ⇒ 全档零命中；"light up"／"spruce" ⇒ 零命中
　② 中文 dedup "装点"／"亮堂" ⇒ 零命中；"好看" ⇒ #687 compliment · 🎓#144 so…that · 🎓#605 in one sitting —— 正文碰巧有"好看"，词都不是 brighten ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`mostly to light up their place`　　更地道：`mostly to brighten up their place`
找法：说"让家里好看、有生气"时，主语是植物／花／装饰 ⇒ brighten up；light up 留给灯和光。

**题面**
"我妈在客厅窗台上摆了几盆花，整个屋子一下子亮堂多了。"（"亮堂多了"用 **brighten up** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My mom put a few pots of flowers on the living room windowsill, and they really brightened up the whole place.

- 2026-11-22 新建 · 学习日 ③ 重答 bank:220 [S4]（⚠️ 更地道的表达，§3.2b）· 原话 `Young people grow plants too, mostly to light up their place, and they tend to go for potted plants since they're way less hassle.`
- 2026-11-23 ✅ 付息日 在池第 1 组 [10] · `it instantly brightened up the whole room` —— 首测 ⇒ 连对 1

### 693 · **be short ＋ 人／东西**（还缺一个…：We're short a drummer.）
类型 词组 ｜ 新建 2026-11-23 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**be short ＋ 名词** ＝ 还缺一个／少几个（人手、东西没凑齐）：`We're short a player.` · `The kitchen is short two chefs tonight.`
数量提前的说法：`We're one person short.` · `We're two chairs short.`
钱、时间不够：**be short of** ＋ 东西（short of cash · short of time）；口语也常说 be short on time。
同一格里的邻居（别串）：lack ＝ 缺乏（书面、偏抽象）· be missing ＝ 少了（本来有、现在不见了）。
判据一句话：一个队伍／一套东西没凑齐、还差几个 ⇒ be short ＋ 缺的那个。

**怎么发现的**
2026-11-23 付息日 在池第 1 组 [2]（#686 题面"我们公司年会的乐队缺一个鼓手，我老公自告奋勇上去了。"）· 原话
`The band for our company's annual party was short(这个短语学下) a drummer, so my husband volunteered to step in.`
她写对了 was short a drummer，但自己标「这个短语学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #666 #691 先例）。
判重三步：
　① 目标形式 dedup "short of"／"short a"／"be short" ⇒ 全档零命中
　② 中文 dedup "缺一个" ⇒ 🎓#103 #272 #320 #322 #323 #465 #662 —— 正文碰巧有"缺一个"，词都不是 short ⇒ 否；"缺" ⇒ 🎓#286 #526 #21 #78 #134 #493 等，同样只是正文碰巧有字，词都不是 short ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `was short a drummer`，但词组不在手边（自己标学下）　　目标：同她原句
找法：中文"还缺一个…／差一个人"、队伍或东西没凑齐 ⇒ 主语 ＋ be short ＋ 缺的那个。

**题面**
"我们周末踢球还缺一个守门员，你能来吗？"（"缺"用 **be short** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：We're short a goalkeeper for our game this weekend—can you come?
★ 首次出题给整块（§6② 她点名要学 ⇒ 练），连对 ≥1 之后降回 short 点名。

- 2026-11-23 ❌ 首犯 · 付息日 在池第 1 组 [2]（#686 题里）· 她标「这个短语学下」· 原话 `The band for our company's annual party was short a drummer, so my husband volunteered to step in.`
- 2026-11-25 ✅ 学习日 在池第 1 组 [5] · `We're still short one person for mahjong—do you want in?`

### 694 · **pop into ＋ 地方**（顺路进去一下、进去待一小会儿：I popped into the supermarket.）
类型 词组 ｜ 新建 2026-11-23 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**pop into** ＋ 地方 ＝ 顺便／很快地进去一下，待不久就出来：`I popped into the supermarket on my way home.`
同族：pop in ＝ 进来坐一下（`Feel free to pop in anytime.`）· pop out ＝ 出去一下（`I'm just popping out for coffee.`）· pop over ＝ 顺道过来。
同一格里的邻居（别串）：stop by／drop by ＝ 顺路去一趟（多指去别人那儿）· go into ＝ 中性的"进去"，没有"一下就走"的意思。
判据一句话：进去很快、顺路、待一会儿就出来 ⇒ pop into。

**怎么发现的**
2026-11-23 付息日 在池第 1 组 [4]（#688 题面"我本来只想进店看一眼，结果拎着三件衣服出来了。"）· 原话
`I only meant to pop into(这个短语学一下) the store for a quick look, but I ended up walking out with three pieces of clothing.`
她写对了 pop into，但自己标「这个短语学一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #693 先例）。
判重三步：
　① 目标形式 dedup "pop into"／"drop in" ⇒ 全档零命中；"pop in" ⇒ 🎓#338 end up（历史行里碰巧有 pop in，条目的词是 end up）⇒ 否
　② "stop by" ⇒ 🎓#463 talk sth through · 🎓#509 set off（历史行里碰巧有）⇒ 词都不是 pop ⇒ 否；中文 dedup "进去看一眼" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `pop into the store`，但词组不在手边（自己标学下）　　目标：同她原句
找法：中文"顺便进去一下／进去看一眼"、进去很快就出来 ⇒ pop into ＋ 地方。

**题面**
"下班路上我顺便进超市买了瓶牛奶。"（"顺便进"用 **pop into** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：On my way home from work, I popped into the supermarket to grab a bottle of milk.
★ 首次出题给整块（§6② 她点名要学 ⇒ 练），连对 ≥1 之后降回 pop 点名。

- 2026-11-23 ❌ 首犯 · 付息日 在池第 1 组 [4]（#688 题里）· 她标「这个短语学一下」· 原话 `I only meant to pop into the store for a quick look, but I ended up walking out with three pieces of clothing.`
- 2026-11-25 ✅ 学习日 在池第 1 组 [6] · `I popped into the supermarket to grab a bottle of milk`

### 695 · **follow sb's tour ／ follow sb on tour**（追巡演、一站站跟着看）
类型 搭配 ｜ 新建 2026-11-23
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**follow sb's tour** ／ **follow sb on tour** ＝ 粉丝跟着歌手、乐队的巡演一站站去看：`She followed the band's tour all over Europe.` · `He followed them on tour for a whole summer.`
同一格里的邻居（别串）：🎓#43 come to town ＝ 乐队巡演到我们这儿（主语是乐队）· go on tour ＝ 歌手自己去巡演 · travel with sb's tour ＝ 跟着巡演队伍一起走（多是工作人员）。
判据一句话：主语是粉丝、追着看 ⇒ follow；主语是歌手 ⇒ go on tour。

**怎么发现的**
2026-11-23 付息日 在池第 1 组 [6]（#690 题面"我朋友为了追那个歌手，甚至把工作辞了，跟着她全国跑。"）· 原话
`To follow that singer, my friend even went so far as to quit her job and travel all over the country with her tour.`
diff-2 ⚠️：travel … with her tour 读起来像她是巡演队伍里的人；粉丝追着看的固定说法是 follow sb's tour ⇒ §3.2b 能学的表达 ⇒ 建号。
判重三步：
　① 目标形式 dedup "follow.*tour" ⇒ 全档零命中；"on tour" ⇒ 🎓#43 come to your city／come to town（巡演到某地，词是 come、主语是乐队）⇒ 否
　② 中文 dedup "巡演" ⇒ 🎓#43 同上 · 🎓#400 come here just to（正文碰巧有）⇒ 否；"全国" ⇒ 🎓#49 #388 #415 #669 等，正文碰巧有字 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`travel all over the country with her tour`　　更地道：`follow her tour all over the country`
找法：说"追巡演／跟着去看"、主语是粉丝 ⇒ follow ＋ 谁的 tour。

**题面**
"她追了那个乐队的巡演整整三年，去了二十多个城市。"（"追…的巡演"用 **follow** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：She followed that band's tour for three whole years and went to more than twenty cities.

- 2026-11-23 新建 · 付息日 在池第 1 组 [6]（#690 题里，⚠️ 更地道的表达，§3.2b）· 原话 `To follow that singer, my friend even went so far as to quit her job and travel all over the country with her tour.`
- 2026-11-25 ✅ 学习日 在池第 2 组 [5] · `She followed that band's tour for three years straight`

### 696 · **porridge**（粥：a bowl of porridge · make porridge）
类型 词汇 ｜ 新建 2026-11-23 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**porridge** ＝ 粥（米粥、燕麦粥都行，不可数）：`a bowl of porridge` · `My grandma makes porridge every morning.`
同一格里的邻居（别串）：congee ＝ 中式米粥（尤其广式白粥）· oatmeal ＝ 燕麦粥（美式常用）· 🎓#577 fried dough sticks ＝ 油条（常跟粥一起说）。
判据一句话：说"粥／稀饭" ⇒ porridge；特指中式白米粥也可以说 congee。

**怎么发现的**
2026-11-23 付息日 复检第 2 组 [1]（#652 题面"我奶奶煮粥的时候总会放一勺红糖。"）· 原话
`Whenever my grandma makes porridge（背一下）, she always adds a spoonful of brown sugar.`
她写对了 porridge，但自己标「背一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #693 #694 先例）。
判重三步：
　① 目标形式 dedup "porridge" ⇒ 全档零命中
　② dedup "粥"／"congee" ⇒ 🎓#577 fried dough sticks（正文提到粥，条目的词是油条）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `makes porridge`，但词不在手边（自己标背一下）　　目标：同她原句
找法：中文"粥／稀饭" ⇒ porridge，一碗 ＝ a bowl of porridge。

**题面**
"我生病的时候，我妈总会给我煮一锅白粥。"（"粥"用 **porridge** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Whenever I'm sick, my mom always makes me a pot of plain rice porridge.

- 2026-11-23 ❌ 首犯 · 付息日 复检第 2 组 [1]（#652 题里）· 她标「背一下」· 原话 `Whenever my grandma makes porridge, she always adds a spoonful of brown sugar.`
- 2026-11-25 ✅ 学习日 在池第 1 组 [7] · `my mom always makes me a pot of plain porridge`（diff-2：plain rice porridge）

### 697 · **let in ＋ 球**（丢球、被对方进球：He let in three goals.）
类型 词组 ｜ 新建 2026-11-23 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**let in** ＋ 几个 goals ＝ （守门员／球队）让对方进了球、丢球：`The goalkeeper let in three goals.` · `They didn't let in a single goal all game.`
同一格里的邻居（别串）：concede a goal ＝ 丢球（解说、新闻常用）· keep a clean sheet ＝ 一个球没丢 · score ＝ 自己这边进球。
判据一句话：说"丢了几个球"、主语是守门员或球队 ⇒ let in ＋ 数字 ＋ goals。

**怎么发现的**
2026-11-23 付息日 复检第 2 组 [6]（#657 题面"那个守门员上半场连丢三个球，教练中场就把他换下去了。"）· 原话
`That goalkeeper let in（这个短语学下) three goals in the first half, so the coach took him off at halftime.`
她写对了 let in，但自己标「这个短语学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #696 先例）。
判重三步：
　① 目标形式 dedup "let in"／"concede" ⇒ 全档零命中
　② 中文 dedup "丢球" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `let in three goals`，但词组不在手边（自己标学下）　　目标：同她原句
找法：中文"丢球／被进了几个" ⇒ let in ＋ 数字 ＋ goals。

**题面**
"我们队守门员今天一个球都没丢。"（"丢球"用 **let in** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Our goalkeeper didn't let in a single goal today.
★ 首次出题给整块（§6② 她点名要学 ⇒ 练），连对 ≥1 之后降回 let 点名。

- 2026-11-23 ❌ 首犯 · 付息日 复检第 2 组 [6]（#657 题里）· 她标「这个短语学下」· 原话 `That goalkeeper let in three goals in the first half, so the coach took him off at halftime.`
- 2026-11-25 ✅ 学习日 在池第 1 组 [8] · `our team let in three goals in the first half alone`

### 698 · **dread ＋ 名词／-ing**（一想到就发怵、很怕某件要来的事）
类型 词汇 ｜ 新建 2026-11-23 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**dread** ＋ 名词／-ing ＝ 很怕一件迟早要来的事，一想到就发怵：`I dread Monday mornings.` · `I'm dreading going back to work.`
常用句型：`What I dread most is …` · `I dread to think …`
同一格里的邻居（别串）：be afraid of ＝ 害怕（危险、东西）· hate ＝ 讨厌 · be nervous about ＝ 紧张。
判据一句话：怕的是一件要来的事、一想到就难受 ⇒ dread。

**怎么发现的**
2026-11-23 付息日 复检第 2 组 [7]（#658 题面"我们这些当妈的，最怕孩子半夜发烧。"）· 原话
`what we moms dread(这个词学下) the most is our kids getting a fever in the middle of the night.`
她写对了 dread，但自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #696 先例）。
判重三步：
　① 目标形式 dedup "dread" ⇒ 全档零命中
　② 中文 dedup "最怕" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `what we moms dread the most`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"最怕…／一想到…就发怵" ⇒ dread ＋ 那件事。

**题面**
"我最怕的就是周一早上开会。"（"最怕"用 **dread** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：What I dread most is Monday morning meetings.

- 2026-11-23 ❌ 首犯 · 付息日 复检第 2 组 [7]（#658 题里）· 她标「这个词学下」· 原话 `what we moms dread the most is our kids getting a fever in the middle of the night.`
- 2026-11-25 ✅ 学习日 在池第 1 组 [9] · `What I dread the most is having meetings on Monday mornings.`

### 699 · **动词 ＋ like crazy**（疯狂地、特别厉害地：The cat sheds like crazy.）
类型 词组 ｜ 新建 2026-11-23 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
动词 ＋ **like crazy** ＝ 一个动作做得特别猛、"疯狂地…"（口语）：`The cat sheds like crazy.` · `It's been raining like crazy.` · `The phone got hyped up like crazy.`
位置：挂在动词／动词短语后面；⛔ 不放在形容词前（⛔ like crazy busy ⇒ crazy busy）。
同一格里的邻居（别串）：a lot（中性）· crazy ＋ 形容词（crazy busy／crazy expensive）· like mad（同义，偏英式）。
判据一句话：修饰的是一个动作、而且特别猛 ⇒ 动词后面挂 like crazy。

**怎么发现的**
2026-11-23 付息日 复检第 4 组 [2]（#441 题面"我同事家的猫掉毛特别厉害，她每天来上班外套上都沾着猫毛。"）· 原话
`My coworker's cat sheds like crazy(like crazy 又忘了，再学下), so she comes to work with cat hair all over her coat every day.`
她写对了 like crazy，但自己标「又忘了，再学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #696 先例）。
判重三步：
　① 目标形式 dedup "like crazy" ⇒ 🎓#441 shed（例句与 10-11 历史行里用过）· 🎓#593 hype up（11-04 历史行她用过）· 🎓#556 #600 #615 #638（历史行碰巧有）—— 都是别的词组，like crazy 没有自己的号 ⇒ 否
　② 中文 dedup "疯狂地" ⇒ 不单列（同 ① 的命中）
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `sheds like crazy`，但词组不在手边（自己标又忘了）　　目标：同她原句
找法：中文"疯狂地…／…得特别厉害"、修饰的是动作 ⇒ 动词 ＋ like crazy。

**题面**
"双十一那几天，我们仓库的订单疯狂地往上涨。"（"疯狂地"用 **like crazy** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：During Singles' Day, orders at our warehouse were going up like crazy.
★ 首次出题给整块（§6② 她点名要学 ⇒ 练），连对 ≥1 之后降回 crazy 点名。

- 2026-11-23 ❌ 首犯 · 付息日 复检第 4 组 [2]（#441 题里）· 她标「like crazy 又忘了，再学下」· 原话 `My coworker's cat sheds like crazy, so she comes to work with cat hair all over her coat every day.`
- 2026-11-25 ✅ 学习日 在池第 1 组 [10] · `orders at our warehouse shot up like crazy`

### 700 · **wag its tail**（狗摇尾巴：wag its tail at sb）
类型 词汇 ｜ 新建 2026-11-23 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**wag** ＝ 狗（猫）摇尾巴：`The dog wagged its tail.` · `wag its tail at sb` ＝ 冲某人摇尾巴；也能单用：`The dog's tail was wagging.`
同一格里的邻居（别串）：shake ＝ 甩（甩头、抖身上的水）· wave ＝ 人挥手。
判据一句话：尾巴左右摆 ⇒ wag。

**怎么发现的**
2026-11-23 付息日 复检第 4 组 [3]（#442 题面"我外婆家那只老狗特别亲人，生人来了也冲人摇尾巴。"）· 原话
`That old dog at my grandma's place is super affectionate—he even wags（背下) his tail at strangers.`
她写对了 wags his tail，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #696 先例）。
判重三步：
　① 目标形式 dedup "wag" ⇒ 全档零命中
　② 中文 dedup "摇尾巴" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `wags his tail`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"摇尾巴" ⇒ wag ＋ its／his tail。

**题面**
"我一拿出零食，我家狗就拼命摇尾巴。"（"摇尾巴"用 **wag** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：As soon as I take out a treat, my dog starts wagging its tail like mad.

- 2026-11-23 ❌ 首犯 · 付息日 复检第 4 组 [3]（#442 题里）· 她标「背下」· 原话 `That old dog at my grandma's place is super affectionate—he even wags his tail at strangers.`
- 2026-11-25 ✅ 学习日 在池第 2 组 [1] · `my dog starts wagging his tail like crazy`

### 701 · **a base of ＋ 一群人**（一批稳定的…：a base of regular customers）
类型 词组 ｜ 新建 2026-11-23 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**a base of ＋ 人** ＝ 一批固定的、撑着你的人：`a base of regular customers` · `a loyal fan base` · `a customer base`。
常跟 build up／grow 连用：`build up a base of regular customers`。
同一格里的邻居（别串）：a bunch of（随便一堆，不强调固定）· regulars（单说"老顾客"）。
判据一句话：中文"一批老顾客／一批粉丝"，强调稳定、撑得住 ⇒ a base of ＋ 人（或 a 名词 base）。
★ 与 🎓#457（build up）分工：那条是动词块"慢慢攒"，本条是名词块"一批固定的人" ⇒ 两个表达，各走各的。
★ 题型判整句：中文"一批"单拎出来 a group of／a lot of 都合法、收不拢 ⇒ 要靠句子 ＋ 正向点名。

**怎么发现的**
2026-11-23 付息日 复检第 5 组 [4]（#457 题面"她开网店三年，慢慢积累了一批老顾客。"）· 原话
`After running an online store for three years, she has slowly built up a base of( a base of 学一下) regular customers.`
她写对了 a base of regular customers，但自己标「学一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #696 #700 先例）。
判重三步：
　① 目标形式 dedup "a base of"／"customer base"／"regular customers"／"regulars" ⇒ 全档零命中
　② 中文 dedup "老顾客" ⇒ 零命中
　③ 最接近的是 🎓#457 build up ⇒ 否，那条是动词块、本条是名词块 ⇒ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `a base of regular customers`，但块不在手边（自己标学一下）　　目标：同她原句
找法：中文"一批（固定的）顾客／粉丝／用户" ⇒ a base of ＋ 人。

**题面**
"他做美食博主两年，攒下了一批铁粉。"（"一批"用 **base** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：After two years as a food blogger, he's built up a base of loyal fans.

- 2026-11-23 ❌ 首犯 · 付息日 复检第 5 组 [4]（#457 题里）· 她标「学一下」· 原话 `After running an online store for three years, she has slowly built up a base of regular customers.`
- 2026-11-25 ✅ 学习日 在池第 2 组 [2] · `he has built up a solid base of loyal fans`

### 702 · **from the cold**（冻得…：结果 ＋ from the cold）
类型 词组 ｜ 新建 2026-11-23 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**结果 ＋ from the cold** ＝ 因为冷而…：`My hands turned purple from the cold.` · `She was shaking from the cold.`
同一套 from ＋ 原因：tired from the trip · sore from running · red from crying。
同一格里的邻居（别串）：because of the cold（合法，但长）· with cold（偏书面：shivering with cold）。
判据一句话：中文"冻得…" ⇒ 先说结果，后面挂 from the cold。
★ 题型判整句：块挂在结果后面才现形，单拎"冻得"收不拢 ⇒ 要靠句子 ＋ 正向点名。

**怎么发现的**
2026-11-23 付息日 复检第 7 组 [4]（#60 题面"冬天不戴手套骑车的话，手会冻得发紫。"）· 原话
`If you ride a bike in the winter without gloves, your hands will turn purple from the cold（from the cold 学下）.`
她写对了 from the cold，但自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #696 #700 #701 先例）。
判重三步：
　① 目标形式 dedup "from the cold" ⇒ 全档零命中
　② 中文 dedup "冻得" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `turn purple from the cold`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"冻得发抖／冻得发紫／冻得通红" ⇒ 结果 ＋ from the cold。

**题面**
"等公交等了半个小时，我冻得直发抖。"（"冻得"用 **from the cold** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：After waiting half an hour for the bus, I was shaking from the cold.

- 2026-11-23 ❌ 首犯 · 付息日 复检第 7 组 [4]（#60 题里）· 她标「学下」· 原话 `If you ride a bike in the winter without gloves, your hands will turn purple from the cold.`
- 2026-11-25 ✅ 学习日 在池第 2 组 [3] · `I was shaking from the cold`

### 703 · **sit around**（闲坐着、什么都不干；⛔ sit tight ＝ 原地等着）
类型 词组 ｜ 新建 2026-11-23
状态 连对1 连错0 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**sit around** ＝ 闲坐着、啥也不干（常跟 and do nothing／doing nothing 连用）：`They'd rather sit around and do nothing.` · `He just sits around all day.`
同一格里的邻居（别串）：sit tight ＝ 原地别动、耐心等着（`Sit tight, I'll be right back.`）· lie around（躺着不动）· hang around（在某处闲逛、待着）。
判据一句话：说的是"懒得动、闲着" ⇒ sit around；说的是"先别动、等着" ⇒ sit tight。
★ 题型判整句："闲着"单拎出来 do nothing／stay idle 都合法、收不拢 ⇒ 要靠句子 ＋ 正向点名。

**怎么发现的**
2026-11-23 付息日 d 段重答 bank:924（P3 · Should parents reward children? Why and how?）S5 · 原话
`Too many rewards can shift their focus away from the real goal and make them dependent on them, to the point where without a reward, they'd rather just sit tight and do nothing at all.`
sit tight 的意思是"原地等着"，她要说的是"闲着不干" ⇒ 选词错（§2.1④：调出来的是另一个词组）。
判重三步：
　① 目标形式 dedup "sit around"／"sit tight" ⇒ 全档零命中
　② 中文 dedup "躺平"／"闲着"／"lie flat" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`they'd rather just sit tight and do nothing at all`　　正确：`they'd rather just sit around and do nothing at all`
找法：想说"闲着／干坐着什么都不干"，先落 sit around；sit tight 只在"别动、等一下"时用。

**题面**
"放暑假了，我儿子整天在家闲着，什么都不干。"（"闲着"用 **sit** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Now that it's summer break, my son just sits around at home all day doing nothing.

- 2026-11-23 ❌ 首犯 · 付息日 d 段重答 bank:924 S5 · 原话 `they'd rather just sit tight and do nothing at all`
- 2026-11-25 ✅ 学习日 在池第 2 组 [4] · `my son just sits around at home all day doing nothing`

### 704 · **around ＋ 节日／时间点**（那段时间前后：around Christmas · around Double Eleven）
类型 搭配 ｜ 新建 2026-11-25
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
**around ＋ 节日／时间点** ＝ 那个节日（时间点）前后那几天：`Around Christmas, the malls are packed.` · `Prices always go up around Chinese New Year.`
同一格里的邻居（别串）：🎓#562 the next／past few days（"这几天"＝相对现在的短期，不挂节日）· during ＋ 节日（节日期间之内，也对，但说"前后那几天"用 around 更贴）。
判据一句话：中文是"X 那几天／X 前后"、X 是节日或时间点 ⇒ around X，⛔ 不把"那几天"译成 those … days。
★ 题型判整句：around 是个小介词，单拎出来没法判，要靠句子 ＋ 正向点名。

**怎么发现的**
2026-11-25 学习日 在池第 1 组 [10]（#699 题面"双十一那几天，我们仓库的订单疯狂地往上涨。"）· 原话
`During those Double Eleven days, orders at our warehouse shot up like crazy.`
能懂，但"那几天"被直译成 those … days；英语直接说 Around Double Eleven ⇒ §3.2b 能学的表达 ⇒ 建号（⚠️ 档）。
判重三步：
　① 目标形式 dedup "around Christmas" ⇒ 零命中；grep 条目头含 around 的 ⇒ #703 sit around · 🎓#471 lounge around · 🎓#474 get around · 🎓#495 beat around the bush · 🎓#617 wrap one's head around · 🎓#659 mess around · 🎓#672 形容词＋around＋人 ⇒ 全是 around 作副词／"在某人面前"，差在不是"时间前后" ⇒ 否
　② 中文 dedup "那几天" ⇒ #699（本题自己的条目，考点 like crazy）⇒ 否；🎓#562 the next／past few days ⇒ 差在"相对现在的这几天"，不挂节日 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）
★ 🎓#385 的历史里她 11-06 说过 `back around Chinese New Year` ⇒ 她见过这个用法，缺口是这次没调出来。

**我错在哪**
她的：`During those Double Eleven days, …`　　更地道：`Around Double Eleven, …`
找法：中文冒出"X 那几天／X 前后"、X 是节日 ⇒ 先落 around X。

**题面**
"每年中秋节前后，月饼的价格都会涨。"（"前后"用 **around** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Mooncake prices go up every year around the Mid-Autumn Festival.

- 2026-11-25 新建 · 学习日 在池第 1 组 [10]（#699 题里）· 原话 `During those Double Eleven days, orders at our warehouse shot up like crazy.`

### 705 · **to the point where ＋ 句子**（到了…的地步：nervous, to the point where I stutter）
类型 句型 ｜ 新建 2026-11-25 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**…, to the point where ＋ 完整句** ＝ 程度深到出现了后面那个结果（"…到了…的地步"）：`I get so nervous around my boss, to the point where I stutter.` · `He was exhausted, to the point where he fell asleep at his desk.`
where 后面接**完整句**（有主语有谓语）；也可以说 to the point of ＋ -ing（`to the point of stuttering`）。
同一格里的邻居（别串）：🎓#690 go so far as to ＋ 动词（某人**主动做出**极端的事："甚至说／甚至去做"）· so … that …（"太…以至于"，更平）。
判据一句话：前面说一个状态、后面说它严重到产生的结果 ⇒ , to the point where ＋ 句子；说某人居然去做了某件过分的事 ⇒ go so far as to。

**怎么发现的**
2026-11-25 学习日 复检第 3 组 [7]（#672 题面"我在领导面前总是很紧张，说话都结巴。"）· 原话
`I always get super nervous around my boss, to the point where(这个短语学下) I even stutter when I talk.`
她用对了，但自己标「这个短语学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #693 #694 #696 先例）。
判重三步：
　① 目标形式 dedup "to the point" ⇒ 🎓#495 beat around the bush（命中的是 get to the point ＝ 说正题，另一个词组）⇒ 否；#703 sit around（命中的是历史行里她 11-23 的原话）⇒ 否
　② 中文 dedup "以至于"／"到了…的地步"／"甚至到" ⇒ 🎓#690 go so far as to（差在：那条是某人主动做出的极端行为，本条是状态严重到出现的结果）⇒ 否
　③ 保留新建（⛔ 建号当天不测）
★ #703 历史里她 11-23 已经用过一次 `to the point where without a reward, they'd rather …` ⇒ 她会用，要的是把它固定下来。

**我错在哪**
她的：用对了 `to the point where I even stutter`，但块不在手边（自己标学下）　　目标：同她原句
找法：想说"…到了…的地步／严重到…" ⇒ 先落 , to the point where ＋ 完整句。

**题面**
"他最近工作压力特别大，大到晚上都睡不着觉。"（"大到…"用 **to the point where** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：He's been under so much pressure at work lately, to the point where he can't sleep at night.

- 2026-11-25 ❌ 首犯 · 学习日 复检第 3 组 [7]（#672 题里）· 她标「这个短语学下」· 原话 `I always get super nervous around my boss, to the point where I even stutter when I talk.`

### 706 · **slack off**（偷懒、摸鱼：slack off on the job · slack off at work）
类型 词组 ｜ 新建 2026-11-25 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-25 未毕业 ｜ 题型 整句

**问题是什么**
**slack off** ＝ 该干活的时候不好好干、偷懒（"摸鱼"）：`Some employees slack off when the boss isn't around.` · `Don't slack off on your studies.`
常跟 on the job／at work／on ＋ 事情 连用。
同一格里的邻居（别串）：goof off（瞎玩不干正事，更口语）· 🎓#659 mess around（瞎闹、胡闹）· #703 sit around（闲坐着什么都不干，不一定是在该干活的时候）。
判据一句话：该干活的场合里磨洋工 ⇒ slack off；纯粹闲着没事 ⇒ sit around。
★ 题型判整句："偷懒"单拎出来 be lazy／goof off 都合法、收不拢 ⇒ 要靠句子 ＋ 正向点名。

**怎么发现的**
2026-11-25 学习日 复检第 4 组 [6]（#585 题面"店长明知道有员工上班摸鱼，却假装没看见。"）· 原话
`The store manager knew full well some employees were slacking off（这个短语学下) on the job, yet he just looked the other way.`
她用对了，但自己标「这个短语学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #693 #694 #696 #705 先例）。
判重三步：
　① 目标形式 dedup "slack"／"goof off" ⇒ 全档零命中
　② 中文 dedup "摸鱼"／"偷懒" ⇒ 零命中；近邻 🎓#659 mess around（瞎闹，不限干活场合）、#703 sit around（闲坐着）⇒ 差在不是"该干活时偷懒" ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `were slacking off on the job`，但块不在手边（自己标学下）　　目标：同她原句
找法：想说"上班摸鱼／偷懒／磨洋工" ⇒ slack off (on the job)。

**题面**
"期末考试快到了，你可别再偷懒了。"（"偷懒"用 **slack off** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Finals are coming up—you really can't slack off anymore.

- 2026-11-25 ❌ 首犯 · 学习日 复检第 4 组 [6]（#585 题里）· 她标「这个短语学下」· 原话 `some employees were slacking off on the job`

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

