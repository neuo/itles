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

### 541 · **put one's hair in a ponytail**（把头发扎成马尾；ponytail ＝ 马尾辫）
类型 词组 ｜ 新建 2026-10-25 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**ponytail** ＝ 马尾辫（脑后扎起来的那一束）；扎马尾 ＝ **put one's hair (up) in a ponytail**：`She put her hair in a ponytail.` · `put it up in a ponytail` · `wear her hair in a ponytail`（平时梳着马尾）。
同一格里的邻居（别串）：tie one's hair back（把头发往后扎，不说扎成什么）· braid（辫子／编辫子）· bun（丸子头：put her hair up in a bun）· pigtails（两边各一束的双马尾）。
判据一句话：说"扎成马尾"⇒ put … in a ponytail（介词 in，⛔ 不是 into）；说"平时梳着马尾"⇒ wear … in a ponytail。
★ 词和块一个号：她要学的是词 ponytail 和块 put her hair in a ponytail；词嵌在块里，产出块就必须调出这个词 ⇒ 不另开号（另开会和本条题面互相泄题）。
★ 题型判整句："扎马尾"能落到 tie it back／wear a ponytail 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。首测给整块（§6②：她说要学的 ⇒ 先练）；连对 1 之后只点名 put，ponytail 留给她自己调。

**怎么发现的**
2026-10-25 学习日 在池第 2 组 [2]（#535 题面"女儿扎马尾用的那根粉色丝带"）· 原话
`that pink ribbon my daughter uses to put her hair in a ponytail(这个词和词组都学下)`
她用对了、自己标「这个词和词组都学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #537 #540 先例）。
判重三步：
　① 目标形式 dedup "ponytail"／"put her hair"／"hair in" ⇒ 零命中
　② 中文 dedup "马尾" ⇒ 零命中；"头发"／"扎" ⇒ #535（ribbon，另一个词 ⇒ 题面互斥：本条题面不带丝带）· 🎓#104（bury，"扎进"是比喻）· 🎓#441（shed，掉毛）· 🎓#51（put away，put 的另一个块）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `to put her hair in a ponytail`，但词和块都不在手边（自己标学下）　　目标：同她原句
找法：中文"扎（个）马尾"先落 put ＋ 头发 ＋ in a ponytail。

**题面**
"她早上来不及洗头，就随手把头发扎了个马尾出门了。"（"扎了个马尾"用 **put … in a ponytail** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：She didn't have time to wash her hair this morning, so she just put it in a ponytail and headed out.
★ 连对 1 之后点名降到只给 **put**（ponytail 留给她调）

- 2026-10-25 ❌ 首犯 · 学习日 在池第 2 组 [2]（#535 题里）· 她标「这个词和词组都学下」· 原话 `that pink ribbon my daughter uses to put her hair in a ponytail(这个词和词组都学下)`
- 2026-10-26 ✅ 学习日 在池第 1 组 [4] · `She was running too late to wash her hair this morning, so she just put her hair in a ponytail and left.` —— put her hair in a ponytail ✓。连错 1 → 连对 1

### 542 · **backstory**（背景故事：一个人／角色在眼下这件事之前的经历；⛔ background story）
类型 词汇 ｜ 新建 2026-10-25
状态 连对1 连错0 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**backstory** ＝ 一个人、一个角色"之前发生过什么"的那段经历（一个词）：`the villain's backstory` · `Every contestant has a sad backstory.` · `The show spends ages on their backstories.`
同一格里的邻居（别串）：background（出身、学历、家庭条件：her family background）· history（过往记录：medical history）· sob story（博同情的苦情故事，带贬义）。
判据一句话：讲的是"一段经历、一个故事"⇒ backstory；讲的是出身、学历、家庭条件 ⇒ background。
★ 题型判整句：零提示时她会再落 background story（能懂、不算错）⇒ 词组题判不出缺口 ⇒ 整句 ＋ 正向点名 backstory。

**怎么发现的**
2026-10-25 学习日 复检第 3 组 [9]a（🎓#440 题面"选秀节目里那段特别煽情的选手背景故事"）· 原话
`a sentimental background story on a talent show`
background story 能懂，但"背景故事"英语有现成的一个词 backstory ⇒ diff-2 ⚠️ ⇒ §3.2b 能学的表达 ⇒ 建号（同 #525 先例：⚠️ 建号记 ❌ 首犯）。
判重三步：
　① 目标形式 dedup "backstory"／"background" ⇒ 零命中
　② 中文 dedup "背景" ⇒ 🎓#318（one time when ＋ 背景，讲往事的句子结构，正文字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：a sentimental background story　　更好：a sentimental backstory
找法：中文"背景故事／他之前的经历"先落 backstory（一个词）；background 留给出身、学历、家庭条件。

**题面**
"这部电影花了整整半个小时交代反派的背景故事。"（"背景故事"用 **backstory** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The movie spends a whole half hour on the villain's backstory.

- 2026-10-25 ❌ 首犯 · 学习日 复检第 3 组 [9]a（#440 题里）· diff-2 ⚠️ · 原话 `a sentimental background story on a talent show` ⇒ 更好版 a sentimental backstory
- 2026-10-26 ✅ 学习日 在池第 1 组 [5] · `The film took over half an hour just to lay out(这个词组学下) the villain's(这个词背下) backstory.` —— the villain's backstory ✓。连错 1 → 连对 1 ｜ 她标学下 ⇒ 新建 #550 #551

### 543 · **bumper-to-bumper**（车一辆挨一辆、堵成长龙：The traffic was bumper-to-bumper.）
类型 词组 ｜ 新建 2026-10-25 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**bumper-to-bumper** ＝ 前车保险杠贴着后车保险杠，形容路上堵得一辆挨一辆：`The traffic was bumper-to-bumper.` · `The highway is bumper-to-bumper during rush hour.` · `bumper-to-bumper traffic`（放名词前）。
同一格里的邻居（别串）：🎓#107 jammed／gridlocked（堵死、一动不动）· 🎓#61 get stuck in traffic（人被堵在路上）· backed up（车排成长队往后压）。
判据一句话：说路／车流一辆挨一辆 ⇒ be bumper-to-bumper；说人被堵 ⇒ get stuck in traffic。
★ 题型判整句："堵"能落到 jammed／gridlocked／backed up 一串合法说法 ⇒ 整句 ＋ 正向点名；挂在名词后面当修饰语要带 that's（the expressway that's bumper-to-bumper）。

**怎么发现的**
2026-10-25 学习日 复检第 3 组 [9]e（🎓#448 题面"早高峰堵得一动不动的那段高架"）· 原话
`that elevated expressway bumper-to-bumper(背下) in the morning rush`
她自己标「背下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 #526 #540 先例）。
判重三步：
　① 目标形式 dedup "bumper" ⇒ 🎓#107（jammed／gridlocked，另一个词；已退池不出题）⇒ 否；"gridlock" ⇒ 零命中
　② 中文 dedup "堵" ⇒ 🎓#107（同上）· 🎓#61（get stuck in traffic，另一个块）· 🎓#287（flow smoothly）· 🎓#108（packed，人多）及其余正文字样 ⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 bumper-to-bumper，但块不在手边（自己标背下）；挂在名词后面少了 that's　　目标：`that elevated expressway that's bumper-to-bumper during the morning rush`
找法：中文"车一辆挨一辆／排成长龙"先落 bumper-to-bumper，前面要有 be（The road is bumper-to-bumper）。

**题面**
"国庆节出城的高速上，车一辆挨一辆，堵了整整五个小时。"（"车一辆挨一辆"用 **bumper-to-bumper** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：On National Day, the highway out of the city was bumper-to-bumper for five whole hours.

- 2026-10-25 ❌ 首犯 · 学习日 复检第 3 组 [9]e（#448 题里）· 她标「背下」· 原话 `that elevated expressway bumper-to-bumper(背下) in the morning rush`
- 2026-10-26 ✅ 学习日 在池第 1 组 [6] · `The expressway out of the city was bumper-to-bumper for five solid hours over the National Day holiday.` —— was bumper-to-bumper ✓。连错 1 → 连对 1

### 544 · **pet**（动词：摸、撸小动物：pet the dog · get petted）
类型 词汇 ｜ 新建 2026-10-25 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**pet** 当动词 ＝ 用手一下一下地摸（猫狗等小动物，带亲昵）：`pet the dog` · `Can I pet your cat?` · `The dog loves getting petted.`
**get petted** ＝ 被人摸（狗凑过来"让人摸摸"）。
同一格里的邻居（别串）：stroke（顺着毛抚摸，偏书面）· pat（轻拍：pat the dog on the head）· cuddle（抱着搂着）· touch（碰，最泛、不带亲昵）。
判据一句话：用手摸小动物、表示亲昵 ⇒ pet；轻轻拍两下 ⇒ pat；抱在怀里 ⇒ cuddle。
★ 题型判整句："摸"能落到 stroke／pat／touch 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 pet。

**怎么发现的**
2026-10-25 学习日 复检第 4 组 [1]（🎓#442 题面"我们楼下那只金毛特别亲人，谁路过都要凑上去让人摸摸。"）· 原话
`The Golden Retriever downstairs is exceptionally affectionate; he runs up to anyone walking past just to get petted(这个词学下).`
她用对了 get petted，自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #537 #540 先例）。
判重三步：
　① 目标形式 dedup "petted"／"pet the" ⇒ 零命中
　② 中文 dedup "摸" ⇒ 🎓#279（get a feel for，摸出手感）· 🎓#528（get the hang of，摸到窍门，比喻）· 🎓#45 #68 #133 #510（正文字样）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `just to get petted`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"摸摸（猫狗）／撸猫"先落 pet；"让人摸"⇒ get petted。

**题面**
"我侄女一见到小猫就蹲下来摸个不停。"（"摸"用 **pet** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Whenever my niece sees a kitten, she crouches down and keeps petting it.

- 2026-10-25 ❌ 首犯 · 学习日 复检第 4 组 [1]（#442 题里）· 她标「这个词学下」· 原话 `he runs up to anyone walking past just to get petted(这个词学下).`
- 2026-10-26 ✅ 学习日 在池第 1 组 [7] · `As soon as my niece spotted the kitten, she crouched down(这个词组学下) and couldn't stop petting it.` —— petting it ✓。连错 1 → 连对 1 ｜ 她标学下 ⇒ 新建 #552

### 545 · **quarter-final**（四分之一决赛：八强赛；the quarter-finals）
类型 词汇 ｜ 新建 2026-10-25 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-26 未毕业 ｜ 题型 词组

**问题是什么**
**quarter-final** ＝ 四分之一决赛（还剩八个队／八个人的那一轮，中文常说八强赛）；那一轮有四场 ⇒ 常用复数 **the quarter-finals**（也写 quarterfinals）：`knocked out in the quarter-finals` · `make it to the quarter-finals`。
同一格里的邻居（别串）：🎓#433 semi-final（半决赛，再往后一轮）· the final（决赛，一场，单数）· the knockout stage（淘汰赛阶段）。
判据一句话：决赛往前数第一轮 ⇒ semi-final；第二轮 ⇒ quarter-final。
★ 在哪一轮被淘汰，最常说 in：knocked out in the quarter-finals（during 也能懂，不算错）。
★ 题型判词组：一个名词块，"八强赛"映射回 the quarter-finals；答 the last eight 合法且贴题面 ⇒ 照判 ✅。

**怎么发现的**
2026-10-25 学习日 复检第 4 组 [5]（🎓#449 题面"我们学校的辩论队在八强赛就被淘汰了。"）· 原话
`Our school's debate team was knocked out during the quarter-finals(学下).`
她写对了 quarter-finals，自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #433 先例）。
判重三步：
　① 目标形式 dedup "quarter" ⇒ 🎓#433（semi-final，另一个词；正文把 quarter-final 列为邻居 ⇒ 题面互斥：本条题面不带"半决赛"）· 🎓#19（分数 a quarter）⇒ 都否；"semifinal" ⇒ 🎓#433（同上）
　② 中文 dedup "八强" ⇒ 零命中；"决赛"／"轮" ⇒ 🎓#415（make it through to）· 🎓#395（tournament）· 🎓#408（a round of）· 🎓#475 及其余正文字样 ⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `the quarter-finals`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"八强（赛）"先落 the quarter-finals。

**题面**
"世界杯八强赛"（还剩八支队伍、再赢两轮就进决赛的那一轮）
★ 目标形式（教练看，⛔ 不进发题稿）：the World Cup quarter-finals

- 2026-10-25 ❌ 首犯 · 学习日 复检第 4 组 [5]（#449 题里）· 她标「学下」· 原话 `Our school's debate team was knocked out during the quarter-finals(学下).`
- 2026-10-26 ✅ 学习日 在池第 1 组 [8] · `the World Cup quarter-finals` —— quarter-finals ✓。连错 1 → 连对 1

### 546 · **find a middle ground**（找个折中、两头之间取中间；strike 常配 a balance／a happy medium）
类型 搭配 ｜ 新建 2026-10-25 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**middle ground** ＝ 两头之间的中间地带、折中：`find a middle ground` · `There's no middle ground.`（没有折中的余地）；口语里最简单的同义说法 `something in between`。
同一格里的邻居（别串）：strike a balance (between A and B)（在两者之间取平衡）· strike a happy medium（找到两全的折中）· meet in the middle（双方各让一步）。
判据一句话：middle ground 前面的动词用 **find**；想用 strike ⇒ 后面接 a balance 或 a happy medium。
★ 题型判整句："折中"能落到 compromise／something in between／meet in the middle 一串合法说法 ⇒ 整句 ＋ 正向点名；首测给整块（她说要学 ⇒ 先练），连对 1 之后只点名 middle ground，动词留给她。

**怎么发现的**
2026-10-25 学习日 ③ 重答 bank:349（R27 · P3 · Where do people normally watch sports events?）S4 · 原话
`If you want to strike a middle ground（这个词组学下), going to a bar works too.`
她自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌；strike a middle ground 也有人说，但 middle ground 最常配 find ⇒ diff-2 ⚠️ 给 find a middle ground。
判重三步：
　① 目标形式 dedup "middle ground"／"happy medium"／"strike a"／"in between" ⇒ 零命中；"balance" ⇒ 🎓#194（balance A and／with B，screen time 那条，另一个块）⇒ 否
　② 中文 dedup "折中" ⇒ 零命中；"中间" ⇒ 🎓#67 #155 #306 #36 #74 #87（全是"放中间"的正文字样）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：strike a middle ground（自己标学下）　　更好：find a middle ground
找法：中文"折中一下／取个中间"先落 find a middle ground（或 something in between）；说出 strike 就接 a balance。

**题面**
"我想要大城市的工作机会，我老公想要小镇的安静，最后我们找了个折中，搬到了郊区。"（"找了个折中"用 **find a middle ground** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I wanted the job opportunities of a big city and my husband wanted the quiet of a small town, so we found a middle ground and moved to the suburbs.
★ 连对 1 之后点名降到只给 **middle ground**（动词 find 留给她）

- 2026-10-25 ❌ 首犯 · 学习日 ③ 重答 bank:349 S4 · 她标「这个词组学下」· diff-2 ⚠️ · 原话 `If you want to strike a middle ground（这个词组学下), going to a bar works too.` ⇒ 更好版 find a middle ground
- 2026-10-26 ✅ 学习日 在池第 1 组 [9] · `I was after big-city career opportunities and my husband wanted small-town quiet, so we eventually found a middle ground and settled in the suburbs.` —— found a middle ground ✓。连错 1 → 连对 1

### 547 · **like-minded**（志同道合的、想法爱好一样的：like-minded people）
类型 词汇 ｜ 新建 2026-10-25 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-26 未毕业 ｜ 题型 词组

**问题是什么**
**like-minded** ＝ 兴趣、想法、立场一样的（放在人前面）：`like-minded people` · `meet like-minded friends` · `a group of like-minded fans`。
同一格里的邻居（别串）：share the same interests（有共同爱好，动词说法）· have a lot in common（共同点多）· on the same page（对一件事看法一致）。
判据一句话：说"一群志同道合的人"⇒ like-minded people；说"我们俩爱好一样"⇒ we share the same interests／have a lot in common。
★ 题型判词组：一个形容词 ＋ 人，"志同道合的"映射回 like-minded，唯一可判。

**怎么发现的**
2026-10-25 学习日 ③ 重答 bank:349（R27 · P3）S5 · 原话
`You're surrounded by like-minded(学下) people, plus it's way cheaper and less time-consuming than actually going to the venue.`
她用对了 like-minded，自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #526 #540 先例）。
判重三步：
　① 目标形式 dedup "like-minded"／"same interests"／"share the same" ⇒ 零命中
　② 中文 dedup "志同道合" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `surrounded by like-minded people`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"志同道合的（人）／同好"先落 like-minded ＋ 人。

**题面**
"读书会里那群志同道合的书友"（都爱看同一类书、一聊就停不下来的那种人）
★ 目标形式（教练看，⛔ 不进发题稿）：the like-minded people in my book club

- 2026-10-25 ❌ 首犯 · 学习日 ③ 重答 bank:349 S5 · 她标「学下」· 原话 `You're surrounded by like-minded(学下) people, plus it's way cheaper and less time-consuming than actually going to the venue.`
- 2026-10-26 ✅ 学习日 在池第 1 组 [10] · `those like-minded bookworms in the book club` —— like-minded ✓。连错 1 → 连对 1

### 548 · **old-fashioned**（老式的、旧款的：an old-fashioned cash register；⛔ legacy）
类型 词汇 ｜ 新建 2026-10-26
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**old-fashioned** ＝ 老式的、旧款的（东西是早年那种样式／做法）：`an old-fashioned cash register` · `an old-fashioned sewing machine` · `old-fashioned values`；口语也常说 **old-school**（带点怀旧、复古的味道）。
同一格里的邻居（别串）：legacy（IT／公司行话：legacy system ＝ 公司里还在跑的旧系统、旧软件，⛔ 不拿来说一台老机器）· outdated（过时了、跟不上了，带贬义）· vintage（有年代感、值得收藏）。
判据一句话：说一样东西"老式的" ⇒ old-fashioned／old-school；legacy 只留给公司里还在跑的旧系统、旧软件。
★ 题型判整句："老式的"能落到 old／old-school／vintage 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-26 学习日 在池第 1 组 [2]（#539 题面"街角小卖部柜台上那台老式收银机"）· 原话
`that legacy cash register on the counter of the corner shop`
考点 cash register 用对（#539 ✅）；diff-2 ⚠️："老式"落成 legacy —— IT／公司行话，说一台老机器偏了 ⇒ old-fashioned ⇒ §3.2b 能学的表达（session／档案里找不到她产出过 old-fashioned ⇒ 不走书面登记）⇒ 建号（同 #538 先例：diff-2 ⚠️ 建号记 ❌ 首犯）。
判重三步：
　① 目标形式 dedup "old-fashioned"／"legacy"／"outdated" ⇒ 零命中；"old" ⇒ 命中全是 old man／older 一类正文字样（🎓#234 older people ＝ 老人 · 🎓#74 make do with 旧电脑题面 · 🎓#531 等），无一以"老式"为考点 ⇒ 否
　② 中文 dedup "老式"／"过时" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`that legacy cash register`　　更地道：`that old-fashioned cash register`
找法：中文"老式的（机器、东西）"先落 old-fashioned；冒出 legacy 先问一句 —— 说的是公司里的旧系统吗？不是就换。

**题面**
"我奶奶到现在还在用那台老式缝纫机给我们改衣服。"（"老式"用 **old-fashioned** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My grandma still uses that old-fashioned sewing machine to alter our clothes.

- 2026-10-26 ❌ 首犯 · 学习日 在池第 1 组 [2]（#539 题里）· diff-2 ⚠️ · 原话 `that legacy cash register on the counter of the corner shop` ⇒ 更好版 old-fashioned

### 549 · **at one's desk**（办公室的"工位" ＝ desk：sat at her desk；⛔ station）
类型 词汇 ｜ 新建 2026-10-26
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 词组

**问题是什么**
办公室里的"工位" ＝ **desk**（每人一张的那张办公桌）：`sit at my desk` · `eat lunch at my desk` · `She's not at her desk.`（她不在工位上）。
同一格里的邻居（别串）：workstation（工位，偏正式、行政口吻）· cubicle（带隔板的格子间）· station（岗位：nurses' station 护士站、餐厅后厨、流水线上的一个位置 —— ⛔ 不说办公室工位）。
判据一句话：办公室里说"在工位上" ⇒ at one's desk；有隔板的格子间才说 cubicle。
★ 题型判词组：一个名词块，"工位"映射回 desk；答 workstation 合法也贴题面 ⇒ 记 ✅（§3.3），只盯她不再落 station。

**怎么发现的**
2026-10-26 学习日 在池第 1 组 [3]（#540 题面"午休的时候，我同事坐在工位上，抱着一包饼干咔嚓咔嚓地啃。"）· 原话
`During lunch break, my coworker sat at her station munching on a pack of biscuits.`
考点 munch on 用对（#540 ✅）；diff-2 ⚠️："工位"落成 station —— station 是护士站、后厨、流水线那种岗位，办公室工位说偏了 ⇒ at her desk ⇒ §3.2b（选词偏了，⛔ 不是同级近义词）⇒ 建号（同 #538 先例：diff-2 ⚠️ 建号记 ❌ 首犯）。
判重三步：
　① 目标形式 dedup "at her desk"／"desk" ⇒ 🎓#289（历史字样：她 10-12 说过 `she's right at her desk drawing`，孩子在家的书桌）· 🎓#435（题面"办公桌上"）· 🎓#501 #74 #158（历史／正文字样）⇒ 都否 —— 她会 desk 这个词，缺的是"工位 → desk"这一步；"workstation"／"cubicle" ⇒ 零命中；"station" ⇒ 🎓#336 #360 #287（火车站等字样）· #89（历史字样）⇒ 否
　② 中文 dedup "工位" ⇒ 零命中；"办公桌" ⇒ 🎓#435（succulent 题面）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`sat at her station`　　更地道：`sat at her desk`
找法：中文"工位"先落 desk；说出 station 先问一句 —— 这是护士站／后厨／流水线吗？不是就换 desk。

**题面**
"开放式办公室里我那个靠窗的工位"（每人一张桌子、一台电脑，上班就坐在那儿的位置）
★ 目标形式（教练看，⛔ 不进发题稿）：my desk by the window in the open-plan office

- 2026-10-26 ❌ 首犯 · 学习日 在池第 1 组 [3]（#540 题里）· diff-2 ⚠️ · 原话 `During lunch break, my coworker sat at her station munching on a pack of biscuits.` ⇒ 更好版 at her desk

### 550 · **lay out ＋ 一套东西**（把计划／来龙去脉一条条摆出来讲清楚：lay out the backstory）
类型 词组 ｜ 新建 2026-10-26 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**lay out** ＝ 把一套东西（计划、理由、事实、来龙去脉）有条理地摆出来、讲清楚：`lay out the plan` · `lay out the facts` · `The film took half an hour to lay out the villain's backstory.`；本义是"摊开摆好"（lay out the clothes on the bed）。
同一格里的邻居（别串）：spell out（一字一句说明白）· go through（一项一项过一遍）· explain（最泛）· 🎓#431 邻居栏里的 well laid out（布局好，说空间，另一个义项）。
判据一句话：把一整套东西从头到尾摆出来讲 ⇒ lay out；怕对方没听懂、要说得一清二楚 ⇒ spell out。
★ 题型判整句："讲清楚／交代"能落到 explain／go through 一串合法说法 ⇒ 整句 ＋ 正向点名；首测给整块（她说要学 ⇒ 先练），连对 1 之后点名降到只给 **lay**（out 留给她）。

**怎么发现的**
2026-10-26 学习日 在池第 1 组 [5]（#542 题面"这部电影花了半个多小时交代反派的背景故事。"）· 原话
`The film took over half an hour just to lay out(这个词组学下) the villain's(这个词背下) backstory.`
她用对了 lay out，自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #540 #541 先例）。
判重三步：
　① 目标形式 dedup "lay out" ⇒ 零命中；"laid out" ⇒ 🎓#431（well planned out；邻居栏 well laid out ＝ 布局，说空间）⇒ 否，另一个义项；"spell out" ⇒ 🎓#162（历史字样）⇒ 否；"set out" ⇒ 🎓#509（set off，历史字样）⇒ 否
　② 中文 dedup "交代" ⇒ 🎓#373 #388 #347（正文"交代背景／时间"字样）· #542（本题题面）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `just to lay out the villain's backstory`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"交代清楚／把…一条条讲出来"先试 lay out。

**题面**
"开会的时候，经理先花了十分钟把明年的计划一条条讲清楚。"（"一条条讲清楚"用 **lay out** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：At the meeting, the manager spent ten minutes laying out next year's plan.

- 2026-10-26 ❌ 首犯 · 学习日 在池第 1 组 [5]（#542 题里）· 她标「这个词组学下」· 原话 `The film took over half an hour just to lay out(这个词组学下) the villain's(这个词背下) backstory.`

### 551 · **villain**（反派、坏人角色：play the villain）
类型 词汇 ｜ 新建 2026-10-26 ｜ ⭐ 她点名要背
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 词组

**问题是什么**
**villain** ＝ 故事里跟主角作对的坏人、反派：`the villain of the movie` · `He always plays the villain.` · `the villain's backstory`。
同一格里的邻居（别串）：bad guy（口语，坏人）· antagonist（对手角色，偏影评、文学评论）· hero／protagonist（主角）。
判据一句话：说电影／小说／剧里的"反派" ⇒ villain（口语也说 the bad guy）。
★ 题型判词组：一个名词，"反派"映射回 villain；答 the bad guy 合法也贴题面 ⇒ 记 ✅（§3.3），下次把语境写具体。

**怎么发现的**
2026-10-26 学习日 在池第 1 组 [5]（#542 题面"这部电影花了半个多小时交代反派的背景故事。"）· 原话
`The film took over half an hour just to lay out(这个词组学下) the villain's(这个词背下) backstory.`
她用对了 villain，自己标「这个词背下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 #543 先例）。
判重三步：
　① 目标形式 dedup "villain" ⇒ #542（正文／历史字样：the villain's backstory）⇒ 否，那条考 backstory；"bad guy" ⇒ 零命中
　② 中文 dedup "反派" ⇒ #542（题面）⇒ 否 ⇒ 题面互斥：本条题面不带"背景故事"
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `the villain's backstory`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"反派／大坏蛋（角色）"先落 villain。

**题面**
"这部剧里演反派的那个演员"（专门跟主角作对、观众恨得牙痒痒的那个坏角色）
★ 目标形式（教练看，⛔ 不进发题稿）：the actor who plays the villain in this show

- 2026-10-26 ❌ 首犯 · 学习日 在池第 1 组 [5]（#542 题里）· 她标「这个词背下」· 原话 `The film took over half an hour just to lay out(这个词组学下) the villain's(这个词背下) backstory.`

### 552 · **crouch down**（蹲下：crouch down to tie my shoelaces）
类型 词组 ｜ 新建 2026-10-26 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**crouch (down)** ＝ 弯腿把身子蹲低（多是一下子蹲下去，去够、去看、去摸）：`crouch down to tie my shoelaces` · `She crouched down and petted the kitten.` · `crouch behind the car`。
同一格里的邻居（别串）：squat (down)（蹲，也指一直蹲着；健身里的深蹲）· kneel (down)（跪下，膝盖着地）· bend down（弯腰，腿不一定弯）。
判据一句话：说"蹲下来（够／看／摸）" ⇒ crouch down；一直蹲着／深蹲 ⇒ squat；膝盖着地 ⇒ kneel。
★ 题型判整句："蹲下"能落到 squat down 等合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；首测给整块（她说要学 ⇒ 先练）。

**怎么发现的**
2026-10-26 学习日 在池第 1 组 [7]（#544 题面"我侄女一见到小猫就蹲下来摸个不停。"）· 原话
`As soon as my niece spotted the kitten, she crouched down(这个词组学下) and couldn't stop petting it.`
她用对了 crouched down，自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #540 #541 先例）。
判重三步：
　① 目标形式 dedup "crouch"／"squat"／"kneel"／"bend down" ⇒ 零命中
　② 中文 dedup "蹲" ⇒ 🎓#332（正文字样）· #544（本题题面）⇒ 都否 ⇒ 题面互斥：本条题面不带"摸小动物"
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `she crouched down`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"蹲下来…"先落 crouch down。

**题面**
"我蹲下来帮女儿系鞋带。"（"蹲下来"用 **crouch down** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I crouched down to tie my daughter's shoelaces.

- 2026-10-26 ❌ 首犯 · 学习日 在池第 1 组 [7]（#544 题里）· 她标「这个词组学下」· 原话 `As soon as my niece spotted the kitten, she crouched down(这个词组学下) and couldn't stop petting it.`

### 553 · **stench**（一股恶臭、熏人的臭味：a nasty stench）
类型 词汇 ｜ 新建 2026-10-26 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**stench** ＝ 一股恶臭、熏人的臭味（名词，比 smell 强烈得多）：`a nasty stench` · `the stench of rotting garbage` · `The stench hit me as soon as I opened the door.`
同一格里的邻居（别串）：smell（味道，中性，加形容词才分好坏：a bad smell）· odor（气味，偏正式）· stink（臭味，口语，也能当动词：It stinks!）· #554 smelly（形容词：臭的）。
判据一句话：说"一股熏人的臭味" ⇒ a stench；说"东西是臭的" ⇒ smelly。
★ 题型判整句："恶臭"能落到 a bad smell／a horrible smell／a stink 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；首测给整词（她说要学 ⇒ 先练）。

**怎么发现的**
2026-10-26 学习日 复检第 2 组 [1]（🎓#215 题面"我一打开行李箱，一股臭鞋味就冲了出来。"）· 原话
`On opening my suitcase, a nasty stench（这个词学下) of smelly（这个词学下)  shoes hit me right in the face.`
她用对了 stench，自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #550 #552 先例）；同句 -ing 主语悬空归 🎓#215（❌ 回潮），与本条无关。
判重三步：
　① 目标形式 dedup "stench"／"stink"／"odor" ⇒ 零命中；"smell" ⇒ 🎓#351（feels like，正文字样）⇒ 否
　② 中文 dedup "臭" ⇒ 🎓#488（strength in numbers，正文字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）；与 #554 同一句建号 ⇒ 题面互斥：本条题面不带"臭袜子／臭鞋"

**我错在哪**
她的：用对了 `a nasty stench of smelly shoes`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"一股恶臭／臭味熏人"先落 a stench (of …)。

**题面**
"垃圾好几天没倒，一进厨房就是一股恶臭。"（"恶臭"用 **stench** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The trash hadn't been taken out for days, so there was a horrible stench as soon as you walked into the kitchen.

- 2026-10-26 ❌ 首犯 · 学习日 复检第 2 组 [1]（🎓#215 题里）· 她标「这个词学下」· 原话 `On opening my suitcase, a nasty stench（这个词学下) of smelly（这个词学下)  shoes hit me right in the face.`

### 554 · **smelly**（臭的：smelly shoes · smelly socks）
类型 词汇 ｜ 新建 2026-10-26 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 词组

**问题是什么**
**smelly** ＝ 有臭味的、臭的（形容词，放东西前面）：`smelly shoes` · `smelly socks` · `smelly cheese`。
同一格里的邻居（别串）：stinky（口语，更随意、带点孩子气）· #553 stench（名词：一股臭味）· smell（名词／动词：It smells bad.）。
判据一句话：说"东西是臭的" ⇒ smelly／stinky；说"一股臭味" ⇒ a stench／a bad smell。
★ 题型判词组：一个形容词 ＋ 东西，"臭袜子"映射回 smelly socks；答 stinky 合法也贴题面 ⇒ 记 ✅（§3.3）。

**怎么发现的**
2026-10-26 学习日 复检第 2 组 [1]（🎓#215 题面"我一打开行李箱，一股臭鞋味就冲了出来。"）· 原话
`On opening my suitcase, a nasty stench（这个词学下) of smelly（这个词学下)  shoes hit me right in the face.`
她用对了 smelly，自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #550 #552 先例）。
判重三步：
　① 目标形式 dedup "smelly"／"stinky" ⇒ 零命中
　② 中文 dedup "臭" ⇒ 🎓#488（正文字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）；与 #553 同一句建号 ⇒ 题面互斥：本条题面不带"一股恶臭"

**我错在哪**
她的：用对了 `smelly shoes`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"臭（袜子／鞋／垃圾）"先落 smelly。

**题面**
"儿子踢完球扔在门口的那双臭袜子"（脱下来一股味儿、谁都不想碰的那种）
★ 目标形式（教练看，⛔ 不进发题稿）：the smelly socks my son tossed by the door after soccer

- 2026-10-26 ❌ 首犯 · 学习日 复检第 2 组 [1]（🎓#215 题里）· 她标「这个词学下」· 原话 `On opening my suitcase, a nasty stench（这个词学下) of smelly（这个词学下)  shoes hit me right in the face.`

### 555 · **right down to ＋ 最细的那一处**（连…都一样、细到…：beautifully crafted, right down to the presentation）
类型 词组 ｜ 新建 2026-10-26 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**right down to ＋ 最小的细节** ＝ 一直细到（连最小的那一处也是这样），放在句末补一刀：`Every dish is beautifully crafted, right down to the presentation.` · `She planned everything right down to the last detail.` · `He copied her look right down to the shoes.`
同一格里的邻居（别串）：🎓#58 it comes down to · 🎓#284 boil down to（都是"说到底／归结为"，不是"细到"）· even（"连…都"，最泛）。
判据一句话：前面说了"全部／每一个都…"，句末补"连最细的 X 也是" ⇒ , right down to X。
★ 题型判整句：考点是块在句末的挂接位置，单拎一个块测不出 ⇒ 整句 ＋ 正向点名；首测给整块（她说要学 ⇒ 先练）。

**怎么发现的**
2026-10-26 学习日 复检第 2 组 [7]（🎓#456 题面"这位厨师的每一道菜都是精心做出来的，连摆盘都很讲究。"）· 原话
`Every single dish from this chef is beautifully crafted, right down to(这个词组的用法可以学下) the presentation.`
她用对了 right down to，自己标「这个词组的用法可以学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #550 #552 先例）。
判重三步：
　① 目标形式 dedup "right down to"／"last detail" ⇒ 零命中；"down to" ⇒ 🎓#58 comes down to · 🎓#284 boil down to（另一个块：归结）· #552 crouch down · ⛔#56 · 🎓#218 #277 #283 等（正文／历史字样）⇒ 都否
　② 中文 dedup "细节" ⇒ 🎓#510 ins and outs · 🎓#463 talk sth through（正文字样）⇒ 否；"讲究" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `beautifully crafted, right down to the presentation`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"连…都很讲究／细到…"先试句末补 right down to。

**题面**
"我妹妹婚礼的每个细节都是她亲手安排的，连桌上的名牌都是她自己写的。"（"连…都"用 **right down to** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My sister planned every detail of her wedding herself, right down to the name cards on the tables.

- 2026-10-26 ❌ 首犯 · 学习日 复检第 2 组 [7]（🎓#456 题里）· 她标「这个词组的用法可以学下」· 原话 `Every single dish from this chef is beautifully crafted, right down to(这个词组的用法可以学下) the presentation.`

### 556 · **nothing to write home about**（一般般、不值一提：it's nothing to write home about）
类型 词组 ｜ 新建 2026-10-26 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**be nothing to write home about** ＝ 一般般、没什么值得说的（不算差，就是不出彩）：`The food was nothing to write home about.` · `The hotel was clean, but nothing to write home about.`
同一格里的邻居（别串）：so-so（一般般，最短）· nothing special（没什么特别的）· not all it's cracked up to be（没传说的那么好）· mediocre（平庸，偏书面、偏贬）。
判据一句话：说某样东西"一般般、不值一提"（不是差）⇒ nothing to write home about。
★ 题型判整句："一般般"能落到 so-so／nothing special 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；首测给整块（她说要学 ⇒ 先练）。

**怎么发现的**
2026-10-26 学习日 复检第 2 组 [9]（🎓#354 题面"这款手机拍照挺不错的，至于电池嘛，就一般般了。"）· 原话
`This phone takes pretty decent photos; as for the battery, though, it's nothing to write home about(这个词组学下).`
她用对了 nothing to write home about，自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #550 #552 先例）。
判重三步：
　① 目标形式 dedup "write home"／"so-so"／"mediocre"／"nothing special"／"cracked up" ⇒ 零命中
　② 中文 dedup "一般般" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `it's nothing to write home about`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"也就一般般／没什么好说的"先试 nothing to write home about。

**题面**
"那家网红餐厅排了一个小时队，结果菜也就一般般。"（"一般般"用 **nothing to write home about** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：We waited in line for an hour at that trendy restaurant, and the food turned out to be nothing to write home about.

- 2026-10-26 ❌ 首犯 · 学习日 复检第 2 组 [9]（🎓#354 题里）· 她标「这个词组学下」· 原话 `This phone takes pretty decent photos; as for the battery, though, it's nothing to write home about(这个词组学下).`

### 557 · **frost**（给蛋糕抹奶油／糖霜：frost the cake with cream）
类型 词汇 ｜ 新建 2026-10-26 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**frost** 当动词 ＝ 给蛋糕外面抹一层奶油／糖霜：`frost the cake with cream` · `She frosted it with chocolate.` · `frost the cupcakes`；名词 **frosting** ＝ 抹在外面的那一层（美式；英式多说 icing，动词 ice a cake）。
同一格里的邻居（别串）：ice a cake（英式，同义）· spread（抹开：spread butter on toast）· 🎓#485 smear（抹得一塌糊涂，带贬义）· decorate（装饰，最泛）。
判据一句话：给蛋糕外面抹一层奶油／糖霜 ⇒ frost (it) with …；抹黄油、果酱在面包上 ⇒ spread。
★ 题型判整句："抹奶油"能落到 spread／cover／ice 一串合法说法，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；首测给整词（她说要学 ⇒ 先练）。

**怎么发现的**
2026-10-26 学习日 ③ 重答 bank:1286（R28 · P2 · Describe a special cake you received from others）S2 · 原话
`She spent the whole day baking the sponge and frosting（这个词的用法学下) it with cream and chocolate.`
她用对了 frosting … with，自己标「这个词的用法学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #550 #552 先例）。
判重三步：
　① 目标形式 dedup "frost"／"icing" ⇒ 零命中
　② 中文 dedup "糖霜" ⇒ 零命中；"抹" ⇒ 🎓#485 smear（抹得一塌糊涂，另一个词）· 🎓#445 #465 #495（正文／题面字样）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `frosting it with cream and chocolate`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"给蛋糕抹奶油／抹一层霜"先落 frost。

**题面**
"烘焙课上，老师教我们怎么给杯子蛋糕抹奶油霜。"（"抹奶油霜"用 **frost** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：In the baking class, the teacher showed us how to frost cupcakes.

- 2026-10-26 ❌ 首犯 · 学习日 ③ 重答 bank:1286 S2 · 她标「这个词的用法学下」· 原话 `She spent the whole day baking the sponge and frosting（这个词的用法学下) it with cream and chocolate.`

### 558 · **a trip down memory lane**（一下子回到从前、勾起一串回忆：It was a real trip down memory lane.）
类型 词组 ｜ 新建 2026-10-26 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-26 未毕业 ｜ 题型 整句

**问题是什么**
**a trip down memory lane** ＝ 一样东西／一个场景把人带回过去一整段时光（带怀旧的暖意）：`It was a real trip down memory lane.` · `Looking at those old photos took me on a trip down memory lane.`
同一格里的邻居（别串）：bring back memories（勾起回忆，最常用）· nostalgic（怀旧的，形容词）· remind me of（让我想起某一件事）。
判据一句话：把你带回过去一整段时光 ⇒ a trip down memory lane；只是想起某一件事 ⇒ remind me of。
★ 题型判整句："一下子回到那段日子"能落到 brought back memories 等合法说法 ⇒ 整句 ＋ 正向点名；首测给整块（她说要学 ⇒ 先练）。

**怎么发现的**
2026-10-26 学习日 ③ 重答 bank:1286（R28 · P2）S8 · 原话
`To me, it wasn't just a slice of dessert—it was a real trip down memory lane(这个词组学下), representing all those years of my youth.`
她用对了 a trip down memory lane，自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #550 #552 先例）。
判重三步：
　① 目标形式 dedup "memory lane"／"nostalg" ⇒ 零命中
　② 中文 dedup "回忆" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `it was a real trip down memory lane`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"一下子回到了那段日子／满满的回忆"先试 a trip down memory lane。

**题面**
"翻到大学时的旧照片，我一下子回到了那段日子。"（"一下子回到了那段日子"用 **a trip down memory lane** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Flipping through my old college photos was a real trip down memory lane.

- 2026-10-26 ❌ 首犯 · 学习日 ③ 重答 bank:1286 S8 · 她标「这个词组学下」· 原话 `To me, it wasn't just a slice of dessert—it was a real trip down memory lane(这个词组学下), representing all those years of my youth.`

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

