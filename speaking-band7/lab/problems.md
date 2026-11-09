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

### 610 · **drain ≠ sewer ≠ drainage**（下水口／排水管 · 城市下水道 · 排水）
类型 词汇 ｜ 新建 2026-11-06 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-07 未毕业 ｜ 题型 词组 ｜ 合并条·出题多句覆盖

**问题是什么**
三个"下水"名词的分工：
　① **drain** ＝ 排水口和连着它的管子（水槽、浴缸、地漏、路边雨水口）：the sink drain · a floor drain · a blocked drain；一栋房子里的排水管道统称 **the drains**
　② **sewer** ＝ 街道底下的污水总管（城市下水道，大到人能钻进去）：the city sewers · the sewer system
　③ **drainage** ＝ 排水（不可数：排得好不好、这套系统）：poor drainage · the drainage system
同一格里的邻居（别串）：#592 back up（管道往回冒，动词块；主语可以是 the drains／the sewer／the sink）· clogged（堵住了）。
判据一句话：一个口子／房子里的管子 ⇒ drain(s)；街道底下的大管道 ⇒ sewer；排水这件事、排水能力或系统 ⇒ drainage。

**怎么发现的**
2026-11-06 学习日 在池第 2 组 [4]（#592 题面"这栋楼的下水道一下大雨就往上返水。"）· 原话
`The drains（和 sewer 的区别学下，还有 drainage) in this building back up whenever we get heavy rain.`
the drains 在这里用对了；她点名要学三个词的区别 ⇒ §2③ 建号（📝 新建，不判档，同 🎓#432 cross-border／transnational 对比条先例）。
三个成员是有限集合、同一个考点（分工）⇒ §3.2c 合并条。
判重三步：
　① 目标形式 dedup "drain" ⇒ 只命中 #592（back up，正文举例 a clogged drain）⇒ 否：那条考动词块 back up；dedup "sewer" ⇒ #592（触发句）· 🎓#553（stench，题面字样）⇒ 否
　② 中文 dedup "下水" ⇒ 只命中 #592 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：the drains 用对了，但三个词的分工不清（自己点名要学）　　目标：drain／sewer／drainage 各就各位
找法：先问自己说的是"一个口、一根管"，还是"整座城市的管网"，还是"排水这件事"。

**题面**
★ 3 句，三个成员各一句 —— 本条考的就是三个词的分工，只出一个等于没测
　① "浴室的地漏"（地上那个出水口）
　② "城市街道底下的下水道"（大管子，全城的污水都流进去）
　③ "这个小区的排水"（下雨积不积水、水排得快不快）
★ 目标形式（教练看，⛔ 不进发题稿）：① the floor drain in the bathroom ② the sewers under the city streets ③ the drainage in this neighborhood
★ ② 答 sewer system 也判 ✅；③ 答 the drainage system 也判 ✅

**成员出题账**
① drain ｜ 11-07 ✅
② sewer ｜ 11-07 ✅
③ drainage ｜ 11-07 ✅

- 2026-11-06 📝 新建 · 学习日 在池第 2 组 [4]（#592 题里）· 她要求学三个词的区别 · 原话 `The drains（和 sewer 的区别学下，还有 drainage) in this building back up whenever we get heavy rain.`
- 2026-11-07 ✅ 学习日 在池第 2 组 [8] · `① the shower/bathroom floor drain ／ ② the city sewer system ／ ③ the neighborhood drainage` —— 三个成员各就各位 ⇒ 成员出题账三行补 11-07 ✅。首测 ⇒ 连对 1

### 615 · **palm**（手掌、手心：my palms were sweating · sweaty palms）
类型 词汇 ｜ 新建 2026-11-07 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**palm** ＝ 手掌、手心（手里面那一面）。手心出汗：`My palms were sweating.` · `I had sweaty palms.` · `It made my palms sweat.`
同一格里的邻居（别串）：the back of my hand（手背）· fist（拳头）· wrist（手腕）。
判据一句话：中文说"手心／手掌"⇒ palm；紧张得手心冒汗 ⇒ sweaty palms／my palms were sweating。
★ 题型判整句："手心出汗"能落到 my hands were sweating 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 palm。

**怎么发现的**
2026-11-07 学习日 在池第 1 组 [4]（#600 题面"面试我的那个经理从头到尾都很严肃，我紧张得手心全是汗。"）· 原话
`The hiring manager who interviewed me stayed totally stern the whole time, making my palms(背一下) sweat like crazy.`
她写对了 palms，但自己标「背一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #601 #609 先例）。
判重三步：
　① 目标形式 dedup "palm" ⇒ 零命中
　② 中文 dedup "手心" ⇒ 零命中；"sweat" ⇒ 🎓#238 move on（历史行字样）⇒ 否：那条考 move on／move forward
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `making my palms sweat`，但词不在手边（自己标背一下）　　目标：同她原句
找法：说到"手心／手掌"先落 palm。

**题面**
"我第一次上台演讲，手心全是汗。"（"手心"用 **palm** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The first time I gave a speech on stage, my palms were sweating like crazy.

- 2026-11-07 ❌ 首犯 · 学习日 在池第 1 组 [4]（#600 题里）· 她标「背一下」· 原话 `The hiring manager who interviewed me stayed totally stern the whole time, making my palms(背一下) sweat like crazy.`
- 2026-11-08 ✅ 付息日 在池第 1 组 [9] · `When I gave a presentation on stage for the first time, my palms were completely soaked in sweat.` —— 连错 1 → 连对 1

### 616 · **movers**（搬家公司、搬家工人：hire movers）
类型 词汇 ｜ 新建 2026-11-07
状态 连对1 连错0 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**movers** ＝ 搬家公司／搬家工人，口语里一律复数：`We hired movers.`（请了搬家公司）· `The movers showed up at eight.`
英式也说 a removal company；正式一点 a moving company。"请"用 **hire**。
同一格里的邻居（别串）：🎓#425 make the move（下决心迈出那一步，不是搬家）· move（动词：搬家）· the move（名词：这次搬家）。
判据一句话：中文是"搬家公司／搬家师傅"⇒ movers；动词配 hire。
★ 题型判整句："搬家公司"能落到 a moving company 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 movers。

**怎么发现的**
2026-11-07 学习日 在池第 1 组 [1]（#251 题面"这次搬家，请搬家公司花了我两千块，光打包东西又花了我整整三天。"）· 原话
`Moving this time cost me two thousand yuan, plus it took me three full days just to pack my stuff up.`
题面花钱的主语是"请搬家公司"，她没译出来（落成 Moving this time）⇒ 更好版补 Hiring movers，是能学的表达 ⇒ §3.2b 建号，判 ❌。
判重三步：
　① 目标形式 dedup "movers" ⇒ 零命中；"hire" ⇒ 🎓#357 logic／logical（历史行字样）⇒ 否
　② 中文 dedup "搬家公司" ⇒ 零命中；"搬家" ⇒ 🎓#332（名词化提议拆回 when 从句）· 🎓#425 make the move ⇒ 否：都不是"搬家公司"这个词
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：Moving this time cost me two thousand yuan　　更好：Hiring movers this time cost me two thousand yuan
找法：中文里出现"搬家公司／搬家师傅"⇒ 落 movers，"请"用 hire。

**题面**
"我们请了搬家公司，一上午就把东西全搬完了。"（"搬家公司"用 **movers** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：We hired movers, and they had everything moved in one morning.

- 2026-11-07 ❌ 首犯 · 学习日 在池第 1 组 [1]（#251 题里）· ⚠️ 题面"请搬家公司"漏译 · 原话 `Moving this time cost me two thousand yuan, plus it took me three full days just to pack my stuff up.`
- 2026-11-08 ✅ 付息日 在池第 1 组 [10] · `We called in some movers, and they finished moving all our stuff in a single morning.` —— 连错 1 → 连对 1

### 617 · **wrap one's head around sth**（想明白、理解得了：can't wrap my head around it）
类型 词组 ｜ 新建 2026-11-07 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**wrap your head around sth** ＝ 把一件难懂／难接受的事想明白：`I can't wrap my head around it.` · `It took me a while to wrap my head around the idea.`
head 跟主语人称走：they can't wrap **their heads** around …；后面可接名词或 why／how 从句。
同一格里的邻居（别串）：get it（听懂）· make sense of（理出头绪）· figure out（琢磨出来）。
判据一句话：中文是"想不通／脑子转不过来"⇒ can't wrap my head around。
★ 题型判整句："想不通"能落到 can't understand 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 wrap。

**怎么发现的**
2026-11-07 学习日 ③ 重答 bank:187 S2 · 原话
`You tell kids that studying hard gives them more career options, but when it's something 10 or 20 years down the road, they just can't wrap their heads around（这句话学下) why it matters.`
她写对了 wrap their heads around，但自己标「这句话学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #601 #609 #615 先例）。
判重三步：
　① 目标形式 dedup "wrap"／"head around" ⇒ 零命中
　② 邻居 get it ⇒ 🎓#137（know／tell／get 的分工，已退池）⇒ 否：那条考 get ＝ 听懂，不是这个词组
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `can't wrap their heads around why it matters`，但词组不在手边（自己标学下）　　目标：同她原句
找法：说到"想不通／理解不了"先落 wrap my head around，head 跟主语人称走。

**题面**
"我到现在还是想不通，他怎么会为了一只猫辞掉那么好的工作。"（"想不通"用 **wrap** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I still can't wrap my head around why he'd quit such a good job over a cat.

- 2026-11-07 ❌ 首犯 · 学习日 ③ 重答 bank:187 S2 · 她标「这句话学下」· 原话 `…they just can't wrap their heads around（这句话学下) why it matters.`
- 2026-11-08 ✅ 付息日 在池第 2 组 [1] · `Even now, I just can't wrap my head around how he could walk away from such a great job all because of a cat.` —— 连错 1 → 连对 1

### 618 · **discouraging**（让人泄气、打击人；⛔ negative reinforcement 是心理学术语"负强化"）
类型 词汇 ｜ 新建 2026-11-07
状态 连对1 连错0 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**discouraging** ＝ 让人泄气的、打击人的：`It's really discouraging.` · `a discouraging result`；人泄了气 ⇒ `I felt discouraged.`
negative reinforcement（负强化）＝ 拿掉一个难受的东西来鼓励某个行为 —— 跟"一直受打击"不是一回事，⛔ 借来说"打击人"意思就偏了。
同一格里的邻居（别串）：frustrating（让人抓狂、使不上劲）· demotivating（让人没动力）。
判据一句话：事情让人泄气 ⇒ discouraging；人泄气 ⇒ discouraged。
★ 题型判整句："打击人"能落到 frustrating 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 discouraging。

**怎么发现的**
2026-11-07 学习日 ③ 重答 bank:187 S3 · 原话
`Especially for kids who just aren't school-smart, it's basically pure negative reinforcement—no matter how hard they try, they just don't get it, and the more they try, the more frustrated they get.`
想说"一直受打击、让人泄气"，借了心理学术语 negative reinforcement，词义偏了 ⇒ 更好版 really discouraging 是能学的表达 ⇒ §3.2b 建号，判 ❌。
判重三步：
　① 目标形式 dedup "discouraging"／"reinforcement" ⇒ 零命中
　② 中文 dedup "泄气"／"打击" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：it's basically pure negative reinforcement　　更好：it's basically really discouraging
找法：想说"打击人／让人泄气"时落 discouraging，⛔ 不借术语。

**题面**
"我练了三个月口语，分数一点没涨，真的挺打击人的。"（"打击人"用 **discouraging** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I've been practicing speaking for three months and my score hasn't gone up at all—it's really discouraging.

- 2026-11-07 ❌ 首犯 · 学习日 ③ 重答 bank:187 S3 · ⚠️ 选词偏 · 原话 `Especially for kids who just aren't school-smart, it's basically pure negative reinforcement—…`
- 2026-11-08 ✅ 付息日 在池第 2 组 [2] · `After working on my speaking for three months with zero score improvement, it's pretty discouraging, to be honest.` —— 连错 1 → 连对 1（同句 ⚠️ After 分词挂不上主语／名词块压缩 ⇒ 只进 diff-2）

### 619 · **book-smart**（会读书的；对照 street-smart 会混社会）
类型 词汇 ｜ 新建 2026-11-07
状态 连对1 连错0 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**book-smart** ＝ 读书这块灵光、学习好；**street-smart** ＝ 社会经验足、会来事：`He's book-smart but not very street-smart.`
同一格里的邻居（别串）：academic（偏书面：academic kids）· good at school（大白话）。
判据一句话：中文是"会读书／不是读书的料"⇒ (not) book-smart；⛔ 不自造 school-smart。
★ 题型判整句："不是读书的料"能落到 not good at school 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 book-smart。

**怎么发现的**
2026-11-07 学习日 ③ 重答 bank:187 S3 · 原话
`Especially for kids who just aren't school-smart, it's basically pure negative reinforcement—…`
school-smart 能懂，但"会读书"的现成说法是 book-smart ⇒ 更地道的说法是能学的表达 ⇒ §3.2b 建号，判 ❌。
判重三步：
　① 目标形式 dedup "book smart"／"book-smart"／"school-smart" ⇒ 零命中
　② 中文"读书的料" ⇒ 无相关条目
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：kids who just aren't school-smart　　更地道：kids who just aren't book-smart
找法：说到"会不会读书"先落 book-smart。

**题面**
"我表弟不是读书的料，但特别会跟人打交道。"（"不是读书的料"用 **book-smart** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My cousin isn't very book-smart, but he's really good with people.

- 2026-11-07 ❌ 首犯 · 学习日 ③ 重答 bank:187 S3 · ⚠️ 不地道 · 原话 `Especially for kids who just aren't school-smart, …`
- 2026-11-08 ✅ 付息日 在池第 2 组 [3] · `My cousin is hardly book-smart, but he sure knows how to deal with people.` —— 连错 1 → 连对 1

### 620 · **master ＋ 技能／曲子**（练熟、彻底掌握；及物，直接接宾语）
类型 词汇 ｜ 新建 2026-11-08 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**master ＋ 东西** ＝ 把一项技能／一首曲子／一门语言练到完全拿得下，比 learn 重：
`master a song` · `master a language` · `master the basics` · `It took me two months to master the first piece.`
master 是及物动词，直接接宾语，⛔ 不加介词（⛔ master in／master at）。
同一格里的邻居（别串）：🎓#528 get the hang of sth（刚摸到窍门、上手了，比 master 浅）· get sth down（口语：I finally got the song down）· be good at sth（形容词才带 at）。
判据一句话：想说"把 X 练熟／彻底掌握 X"⇒ master X，后面直接跟东西。
★ 题型判整句："练熟"能落到 learn／get good at 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 master。

**怎么发现的**
2026-11-08 付息日 在池第 1 组 [1]（#251 题面"报这个吉他班花了我五千块，光把第一首曲子练熟就花了我两个多月。"）· 原话
`Enrolling in this guitar class cost me five grand, and it took me more than two months just to master(这个动词的用法学下) the first piece.`
她写对了 master，但自己标「这个动词的用法学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #609 #615 先例）。
判重三步：
　① 目标形式 dedup "master" ⇒ 🎓#486 #489（只在历史行出现，考点是 one…another／in no time）⇒ 否
　② 中文 dedup "掌握" ⇒ 🎓#137 know／tell／get（知道、分辨）⇒ 否；🎓#279 get a feel for（摸出门道）⇒ 否；"练熟" ⇒ 零命中
　　 🎓#528 get the hang of（上手）⇒ 否：差在程度（刚上手 vs 练熟），写成邻居
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `just to master the first piece`，但用法不在手边（自己标学下）　　目标：同她原句
找法：说到"练熟／掌握"先落 master，宾语直接跟上，不补 at／in。

**题面**
"她花了半年才把这门语言的发音练熟。"（"练熟"用 **master** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：It took her half a year to master the pronunciation of the language.

- 2026-11-08 ❌ 首犯 · 付息日 在池第 1 组 [1]（#251 题里）· 她标「这个动词的用法学下」· 原话 `Enrolling in this guitar class cost me five grand, and it took me more than two months just to master(这个动词的用法学下) the first piece.`

### 621 · **We've had ＋ 人 ＋ 原形**（"我们这儿来了／走了几个人"：经历义的 have sb do）
类型 结构 ｜ 新建 2026-11-08 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**have ＋ 人 ＋ 动词原形**，除了"让某人做"（I had him fix my car），还能表示"我们这边出了这么个事、来了／走了这么些人"——
主语是"我们"这个地方或团体，事情是别人做的：
`We've had three people quit this month.`（这个月走了三个人）· `We had a guy knock on our door at midnight.`（半夜有人来敲门）· `We've had a lot of tourists come by lately.`
动词用原形，⛔ 不加 to（同 🎓#16 的规则）。
同一格里的邻居（别串）：🎓#16 have sb do ＝ 让某人做（使役）· 🎓#497 have ＋ 东西 ＋ done ＝ 遭遇（had my phone stolen）· 直接说 Three people have quit（不点出"我们"）。
判据一句话：中文是"我们这儿来了／走了／有人…"⇒ We('ve) had ＋ 人 ＋ 原形。
★ 题型判整句：结构靠句子才现形（have ＋ 人 ＋ 原形的位置）⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-08 付息日 在池第 1 组 [2]（#271② 题面"这阵子我们公司来了好几个新同事。"）· 原话
`We've had a bunch of new coworkers join (have sbd. do sth. 的句型学下) our team lately.`
她写对了，但自己标「have sbd. do sth. 的句型学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #609 #615 先例）。
判重三步：
　① 目标形式 dedup "have sb do"／"had .* join" ⇒ 零命中
　② dedup "sb do" ⇒ 🎓#16（让某人做四件套）⇒ 否：原形不带 to 的规则相同，但 #16 考"让"（使役，选 get／have／make 及带不带 to），本条考"来了／走了"（经历义，意思层）；🎓#575 prefer that sb do ⇒ 否
　　 dedup "have sth done" ⇒ 🎓#497 遭遇（宾语是东西 ＋ 过去分词）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `We've had a bunch of new coworkers join our team`，但句型不在手边（自己标学下）　　目标：同她原句
找法：说"我们这儿来了／走了几个人"先落 We've had ＋ 人，后面动词原形。

**题面**
"这个月我们小区已经有三户人家搬走了。"（用 **We've had** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：We've had three families move out of our neighborhood this month.
★ 首次出题给整块（§6② 她点名要学 ⇒ 练），连对 ≥1 之后降回 lemma（用 **have** 说）。

- 2026-11-08 ❌ 首犯 · 付息日 在池第 1 组 [2]（#271② 题里）· 她标「have sbd. do sth. 的句型学下」· 原话 `We've had a bunch of new coworkers join (have sbd. do sth. 的句型学下) our team lately.`

### 622 · **be mad at sb**（生某人的气；为某事生气 ⇒ mad about sth）
类型 搭配 ｜ 新建 2026-11-08 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**mad at ＋ 人** ＝ 生某人的气（口语最常用）：`She's mad at me.` · `Are you still mad at me?`
为某件事生气 ⇒ **mad about ＋ 事**：`He's still mad about the scratch on his car.`
同一格里的邻居（别串）：angry with／at sb（略正式）· upset with sb（难过＋不满，语气轻）· 单说 be mad 也可以（美式口语＝生气）· ⛔ mad to sb。
判据一句话：生"人"的气 ⇒ at；生"事"的气 ⇒ about。
★ 题型判整句：介词靠宾语现形（人 ⇒ at，事 ⇒ about），"生气"能落到 angry 绕开 ⇒ 整句 ＋ 正向点名 mad。

**怎么发现的**
2026-11-08 付息日 在池第 1 组 [6]（#612 题面"她明摆着是在生你的气，你还看不出来吗？"）· 原话
`It's plain as day that she's mad at(这个词组学下) you—can't you even tell?`
她写对了，但自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #609 #615 先例）。
判重三步：
　① 目标形式 dedup "mad at"／"angry with"／"upset with" ⇒ 零命中
　② 中文 dedup "生.*的气" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `she's mad at you`，但词组不在手边（自己标学下）　　目标：同她原句
找法：说"生某人的气"先落 mad at ＋ 人；后面是事情就换 about。

**题面**
"我妈还在生我的气，因为我忘了她的生日。"（"生我的气"用 **mad** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My mom's still mad at me because I forgot her birthday.

- 2026-11-08 ❌ 首犯 · 付息日 在池第 1 组 [6]（#612 题里）· 她标「这个词组学下」· 原话 `It's plain as day that she's mad at(这个词组学下) you—can't you even tell?`

### 623 · **dodge ＋ 东西**（一闪躲开；引申 dodge the question 回避问题）
类型 词汇 ｜ 新建 2026-11-08 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**dodge ＋ 东西** ＝ 身子一闪，躲开迎面来的东西：`dodge a ball` · `dodge a punch` · `dodge my hand`；
引申：躲着不面对 —— `dodge the question`（回避问题）· `dodge a bullet`（躲过一劫）。及物，直接接宾语。
同一格里的邻居（别串）：🎓#572 pull away（往后一缩，不让人碰，不及物）· avoid（避开，泛指，没有"闪身"的画面）· duck（低头一躲）。
判据一句话：有东西冲你来、你一闪 ⇒ dodge ＋ 那个东西；只是往后缩 ⇒ pull away。
★ 题型判整句："躲开"能落到 avoid／got out of the way 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 dodge。

**怎么发现的**
2026-11-08 付息日 复检第 3 组 [3]（🎓#572 题面"我伸手想摸那只流浪猫，它一下子往后一缩躲开了。"）· 原话
`I reached out to pet the stray cat, but it pulled away to dodge(这个词学下) my hand.`
她写对了 dodge，但自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #609 #615 先例）。
判重三步：
　① 目标形式 dedup "dodge" ⇒ 🎓#572 pull away（dodge 只在它的历史行里当绕开词出现）⇒ 否：pull away 不及物、往后缩，dodge 及物、闪身躲开，写成邻居；🎓#495 beat around the bush（历史行字样）⇒ 否
　② 中文 dedup "躲" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `to dodge my hand`，但词不在手边（自己标学下）　　目标：同她原句
找法：说"一闪躲开 X／回避 X"先落 dodge ＋ X，直接接宾语。

**题面**
"他头一偏，躲开了飞过来的篮球。"（"躲开"用 **dodge** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：He tilted his head and dodged the basketball flying at him.

- 2026-11-08 ❌ 首犯 · 付息日 复检第 3 组 [3]（🎓#572 题里）· 她标「这个词学下」· 原话 `I reached out to pet the stray cat, but it pulled away to dodge(这个词学下) my hand.`

### 624 · **价钱 ＋ a pop**（口语：一个／一次多少钱 —— five bucks a pop）
类型 词组 ｜ 新建 2026-11-08 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**价钱 ＋ a pop** ＝ "一个多少钱／一次多少钱"，挂在价钱后面，非常口语：
`They're five bucks a pop.` · `Tickets are 200 a pop.` · `He charges fifty dollars a pop.`
同一格里的邻居（别串）：each（中性：five yuan each）· apiece（略正式）· per（书面：per item）。
判据一句话：说"一个／一次多少钱"，口语里把 a pop 挂在价钱后面。
★ 题型判整句："一个"能落到 each 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 a pop。

**怎么发现的**
2026-11-08 付息日 复检第 3 组 [7]（🎓#576 题面"我们学校门口有个大爷摆摊卖煎饼，一个五块钱。"）· 原话
`There's an old guy outside our school gate who runs a stall selling savory crepes for five bucks a pop(a pop 的用法学下).`
她写对了，但自己标「a pop 的用法学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #609 #615 先例）。
判重三步：
　① 目标形式 dedup "a pop" ⇒ 🎓#430 street market（只是历史行字样）⇒ 否
　② dedup "apiece／each" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `for five bucks a pop`，但用法不在手边（自己标学下）　　目标：同她原句
找法：报了价钱、想补"一个／一次"⇒ 价钱后面直接接 a pop。

**题面**
"那家网红店的冰淇淋要四十块一个，排队的人还特别多。"（"一个"用 **a pop** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The ice cream at that trendy shop is forty yuan a pop, and the line is still really long.

- 2026-11-08 ❌ 首犯 · 付息日 复检第 3 组 [7]（🎓#576 题里）· 她标「a pop 的用法学下」· 原话 `There's an old guy outside our school gate who runs a stall selling savory crepes for five bucks a pop(a pop 的用法学下).`

### 625 · **misaligned**（没对正、歪了：the handlebars are misaligned）
类型 词汇 ｜ 新建 2026-11-08 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**misaligned** ＝ 本该对齐／对正的东西没对上（车把、轮子、牙齿、画框）：
`The handlebars are misaligned.` · `My car's wheels are misaligned, so it pulls to the right.`
同一格里的邻居（别串）：crooked（歪的，最日常：a crooked picture）· bent（弯了、变形）· off-center（偏了，没在正中）。
判据一句话：本该对正却没对正 ⇒ misaligned；只说"看着歪"⇒ crooked。
★ 题型判整句："没对正"能落到 crooked／not straight 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 misaligned。

**怎么发现的**
2026-11-08 付息日 复检第 3 组 [9]（🎓#578 题面"这辆共享单车的车把是歪的，骑起来特别费劲。"）· 原话
`The handlebars on this shared bike are completely misaligned(背下这个词), so it takes a ton of effort to ride.`
她写对了，但自己标「背下这个词」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #609 #615 先例）。
判重三步：
　① 目标形式 dedup "misalign"／"crooked" ⇒ 零命中
　② 中文 dedup "歪" ⇒ 14 条全是"读歪／写歪"字样（#215 #280 #338 #357 #17 #28 #161 #193 #268 #310 #314 #316 等），考点无一相关 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `are completely misaligned`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"（车把／轮子／牙）没对正"先落 misaligned。

**题面**
"我的车四轮没对正，开起来总往右偏。"（"没对正"用 **misaligned** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My car's wheels are misaligned, so it keeps pulling to the right.

- 2026-11-08 ❌ 首犯 · 付息日 复检第 3 组 [9]（🎓#578 题里）· 她标「背下这个词」· 原话 `The handlebars on this shared bike are completely misaligned(背下这个词), so it takes a ton of effort to ride.`

### 626 · **the basics**（基本功、最基本的那一层；固定带 the、固定复数）
类型 词组 ｜ 新建 2026-11-08
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**the basics** ＝ 最基本的那些东西／基本功，固定带 the、固定复数：
`Cooking food until it's done is just the basics.` · `Let's start with the basics.` · `get the basics right`
同一格里的邻居（别串）：a basic skill（一项基本技能，可数单数要带 a）· fundamentals（略正式）· basic（形容词：That's pretty basic.）。
判据一句话：中文"基本功／这只是最基本的"⇒ (just) the basics。
★ 题型判整句："基本功"能落到 a basic skill 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 basics。

**怎么发现的**
2026-11-08 付息日 复检第 4 组 [2]（🎓#340 题面"能把菜做熟只是基本功；再往上一档，是能把每道菜的味道调对。"）· 原话
`Just cooking food until it's done is basic skills—a step up from that is making every dish taste fine.`
is basic skills 的单复数 ⇒ ⚪ #56；"基本功"的口语现成说法是 the basics ⇒ 更地道的说法是能学的表达 ⇒ §3.2b 建号，判 ❌。
判重三步：
　① 目标形式 dedup "basic skill"／"the basics" ⇒ 零命中
　② 🎓#340 a step up from that（同句的另一个块）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`is basic skills`　　更地道：`is the basics`（最小改 is a basic skill）
找法：说"只是基本功"先落 It's just the basics。

**题面**
"会用电脑打字只是基本功，会做表格才算真本事。"（"基本功"用 **basics** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Typing on a computer is just the basics—being able to make spreadsheets is the real skill.

- 2026-11-08 ❌ 首犯 · 付息日 复检第 4 组 [2]（🎓#340 题里）· ⚠️ 不地道 · 原话 `Just cooking food until it's done is basic skills—a step up from that is making every dish taste fine.`

### 627 · **taste just right**（味道调得正好；⛔ taste fine ＝ 还行）
类型 搭配 ｜ 新建 2026-11-08
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**taste just right** ＝ 味道刚刚好、调对了：`The soup tastes just right.` · `get every dish to taste just right`
⛔ taste fine ＝ 味道还行、过得去（不难吃而已），不是"调对"。
同一格里的邻居（别串）：taste good（好吃）· taste off（味道不对劲）· get the seasoning right（调味调对）。
判据一句话：想说"调得正好" ⇒ just right；只是"还行" ⇒ fine。
★ 题型判整句："刚刚好"能落到 perfect／great 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 just right。

**怎么发现的**
2026-11-08 付息日 复检第 4 组 [2]（🎓#340 题里）· 原话
`… a step up from that is making every dish taste fine.`
"再往上一档"要说的是味道调得正好，fine 只是"还行"，意思偏了（⛔ 不是同级近义词）⇒ §3.2b 建号，判 ❌。
判重三步：
　① 目标形式 dedup "taste right"／"get .* right" ⇒ 零命中
　② 中文 dedup "调对／味道" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`making every dish taste fine`　　更地道：`making every dish taste just right`
找法：说"味道调对／刚好"先落 taste just right；fine 只在"还行"时用。

**题面**
"我妈炖的汤咸淡刚刚好。"（"刚刚好"用 **just right** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The soup my mom makes tastes just right—not too salty, not too bland.

- 2026-11-08 ❌ 首犯 · 付息日 复检第 4 组 [2]（🎓#340 题里）· ⚠️ 意思偏了 · 原话 `… a step up from that is making every dish taste fine.`

### 628 · **behind closed doors**（关起门来、私下里）
类型 词组 ｜ 新建 2026-11-08 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**behind closed doors** ＝ 关起门来、不当着外人（私下处理、私下谈）：
`They sort out their problems behind closed doors.` · `The deal was made behind closed doors.`
同一格里的邻居（别串）：🎓#527 in public（当着外人）的反面 · in private（私下，中性）· 🎓#574 on the sly（偷偷，带"背着人"）。
判据一句话：想说"关起门来自己解决、不让外人看见"⇒ behind closed doors。
★ 题型判整句："私下"能落到 in private 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 closed doors。

**怎么发现的**
2026-11-08 付息日 复检第 4 组 [5]（🎓#527 题面"他们俩在公共场合从来不吵架，有矛盾都关起门来解决。"）· 原话
`They never fight in public—if there's any disagreement, they always resolve it behind closed doors（这个私下解决可以学下).`
她写对了，但自己标「这个私下解决可以学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #609 #615 先例）。
判重三步：
　① 目标形式 dedup "behind closed doors" ⇒ 零命中
　② 中文 dedup "私下" ⇒ 🎓#527 in public · 🎓#574 on the sly · 🎓#573 settle a score（字样）⇒ 全否，前两条写成邻居
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `resolve it behind closed doors`，但块不在手边（自己标学下）　　目标：同她原句
找法：说"关起门来／私下解决"先落 behind closed doors。

**题面**
"公司裁员的事都是高层关起门来定的。"（"关起门来"用 **closed doors** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The layoffs were all decided by the top bosses behind closed doors.

- 2026-11-08 ❌ 首犯 · 付息日 复检第 4 组 [5]（🎓#527 题里）· 她标「这个私下解决可以学下」· 原话 `They never fight in public—if there's any disagreement, they always resolve it behind closed doors（这个私下解决可以学下).`

### 629 · **take a tumble**（摔一跤）
类型 词组 ｜ 新建 2026-11-08 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**take a tumble** ＝ 摔一跤（口语，偏轻松）：`I took a nasty tumble on the ice.` · `kept taking tumbles`
同一格里的邻居（别串）：fall (over／off)（最中性：fell off my bike）· trip（被绊倒）· slip（滑倒）。
判据一句话：想说"摔了一跤"又带点轻松口气 ⇒ take a tumble。
★ 题型判整句："摔一跤"能落到 fell 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 tumble。

**怎么发现的**
2026-11-08 付息日 复检第 4 组 [6]（🎓#528 题面"我刚开始学滑板老摔，练了半个月才摸到窍门。"）· 原话
`I kept taking tumbles(背下） when I began skateboarding and only got the hang of it after half a month.`
她写对了，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #609 #615 先例）。
判重三步：
　① 目标形式 dedup "tumble" ⇒ 零命中
　② 中文 dedup "摔" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `kept taking tumbles`，但块不在手边（自己标背下）　　目标：同她原句
找法：说"摔一跤"先落 took a tumble。

**题面**
"我奶奶上周在楼梯上摔了一跤，还好没伤着骨头。"（"摔了一跤"用 **tumble** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My grandma took a tumble on the stairs last week, but luckily she didn't break anything.

- 2026-11-08 ❌ 首犯 · 付息日 复检第 4 组 [6]（🎓#528 题里）· 她标「背下」· 原话 `I kept taking tumbles(背下） when I began skateboarding and only got the hang of it after half a month.`

### 630 · **two weeks**（"半个月"；⛔ half a month）
类型 词组 ｜ 新建 2026-11-08
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
中文"半个月"英语说 **two weeks**（口语也说 a couple of weeks），不按月切半：`It took me two weeks.` · `I'll be away for two weeks.`
同一格里的邻居（别串）：a fortnight（英式）· half a year（"半年"英语照说，没问题）。
判据一句话："半个月"⇒ two weeks；"半年"⇒ half a year／six months。
★ 题型判整句：零提示——"半个月"任何地道译法都得落到 two weeks／a couple of weeks，避不开（§6② 绕开测试翻不出）⇒ 整句、不点名。

**怎么发现的**
2026-11-08 付息日 复检第 4 组 [6]（🎓#528 题里）· 原话
`… and only got the hang of it after half a month.`
half a month 能懂，但英语说"半个月"用 two weeks ⇒ 更地道的说法是能学的表达 ⇒ §3.2b 建号，判 ❌。
判重三步：
　① 目标形式 dedup "half a month" ⇒ 零命中
　② 中文 dedup "半个月" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`after half a month`　　更地道：`after two weeks`
找法：说到"半个月"直接换成 two weeks。

**题面**
"我等了半个月，快递才到。"
★ 目标形式（教练看，⛔ 不进发题稿）：I waited two weeks for my package to arrive.

- 2026-11-08 ❌ 首犯 · 付息日 复检第 4 组 [6]（🎓#528 题里）· ⚠️ 不地道 · 原话 `… and only got the hang of it after half a month.`

### 631 · **backfire**（适得其反、弄巧成拙：It can totally backfire.）
类型 词汇 ｜ 新建 2026-11-08 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**backfire** ＝ 本想有好结果，反倒招来坏结果（适得其反、弄巧成拙）。
不及物：`The plan backfired.` · `It can totally backfire.` · 要说害到谁 ⇒ **backfire on sb**（`It backfired on him.`）；⛔ 不接宾语（⛔ backfire the plan）。
同一格里的邻居（别串）：go wrong（只是出岔子，没有"反过来"那层）· do more harm than good（弊大于利）。
判据一句话：中文是"适得其反／反倒害了自己" ⇒ backfire。
★ 题型判整句："适得其反"能落到 had the opposite effect 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 backfire。

**怎么发现的**
2026-11-08 付息日 d 段重答 bank:927 S5 · 原话
`Leaning too heavily on them can totally backfire（这个词学下).`
她写对了 can totally backfire，但自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #609 #615 #617 先例）。
判重三步：
　① 目标形式 dedup "backfire" ⇒ 全档零命中
　② 中文题面 "适得其反"／"反噬"／"弄巧成拙" ⇒ 零命中；邻居 "harm than good" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `can totally backfire`，但词不在手边（自己标学下）　　目标：同她原句
找法：说到"适得其反／反倒害了自己"先落 backfire，后面要说害到谁就接 on sb。

**题面**
"他想靠送礼讨好领导，结果适得其反。"（"适得其反"用 **backfire** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：He tried to win his boss over with gifts, but it backfired.

- 2026-11-08 ❌ 首犯 · 付息日 d 段重答 bank:927 S5 · 她标「这个词学下」· 原话 `Leaning too heavily on them can totally backfire（这个词学下).`

### 632 · **a means to an end, not an end in itself**（只是手段，不是目的本身）
类型 词组 ｜ 新建 2026-11-08
状态 连对0 连错1 上次2026-11-08 未毕业 ｜ 题型 整句

**问题是什么**
**an end in itself** ＝ 目的本身（end 在这里是"目的"）。常跟 **a means to an end**（手段）成对：
`X is just a means to an end, not an end in itself.` —— 两个 end 前后呼应。
也能单用：`For some people, money is an end in itself.`
同一格里的邻居（别串）：the end goal（最终要达到的那个结果）—— 能懂，但跟 a means to an end 成对时母语者说 an end in itself。
判据一句话：中文是"只是手段，不是目的（本身）" ⇒ a means to an end, not an end in itself。
★ 题型判整句：块要挂在"X 只是……"的句子里才现形，且"目的本身"可绕成 the goal itself ⇒ 整句 ＋ 正向点名 end。

**怎么发现的**
2026-11-08 付息日 d 段重答 bank:927 S4 · 原话
`Mind you, rewards are just a means to an end, not the end goal itself.`
a means to an end 用对；后半句 the end goal itself 能懂，但成对的固定说法是 an end in itself ⇒ §3.2b ⚠️ 更地道的表达是能学的块 ⇒ 建号，判 ❌（同 #618 #630 先例）。
判重三步：
　① 目标形式 dedup "in itself"／"means to an end"／"end goal" ⇒ 全档零命中
　② 中文题面 "目的本身"／"不是目的"／"手段" ⇒ 零命中（graduated.md 一处"不是目的"在 🎓#236 正文里，那条考"目的用 to do"，不是这个块 ⇒ 否）
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：a means to an end, not **the end goal itself**　　正确：a means to an end, not **an end in itself**
找法：说出 a means to an end，后半句直接接 not an end in itself —— 两个 end 对上。

**题面**
"对他来说，赚钱只是手段，不是目的本身。"（"目的本身"用 **end** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：For him, making money is just a means to an end, not an end in itself.

- 2026-11-08 ❌ 首犯 · 付息日 d 段重答 bank:927 S4 · ⚠️ 不地道 · 原话 `Mind you, rewards are just a means to an end, not the end goal itself.`

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

