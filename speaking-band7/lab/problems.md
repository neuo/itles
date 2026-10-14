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

### 126 · get used to ／ settle into（适应新环境）
类型 词组 ｜ 旧号 B211
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 整句 ｜ **回潮 2026-10-12**（08-19 毕业 → 10-12 她在 #283 题里标「getting used to(学下)」点名要学 ⇒ 判 ❌、连对清零；09-29 停出与 10-12 恢复见历史行）

**问题是什么**
**get used to ／ settle into（settle in）** ＝ 适应新环境：
`new staff need time to **settle in**.` ／ `get used to the new environment`。
同一格里的邻居（别串）：adapt／adjust 也能说"适应"，但绕开这两个口语块 ⇒ 题面已排除。
判据一句话："适应"在口语里走 get used to 或 settle in／into。
★ get used to 的 to 是**介词** ⇒ 后面接名词或 -ing：`get used to the controls` ／ `get used to driving on the left`；
　⛔ 别跟 used to do（过去常常：I used to drive to work.）串 —— 一个是"习惯了／适应了"，一个是"以前常常"。
★ 题型 2026-10-12 由词组改整句：to 后面接名词还是 -ing 要靠句子才现形；题面改正向点名。

**怎么发现的**
旧 B 表迁移（B211，2026-08-18），原始触发原话未存；最早记录 2026-08-12 ✅。
2026-10-12 付息日 a2 段复检第 6 组 [7]（🎓#283 题里）她写 `getting used to(学下) the basic controls first`，自己标「学下」⇒ §3.6 她点名要学 ⛔ 不退 ⇒ 撤销退池、判 ❌、回潮。
2026-08-19 ✅ `new staff need time to settle in.`（settle in 用对）⇒ 毕业。
2026-09-10 复检第 4 组（打包）✅ `get used to the new environment`。

**我错在哪**
她的：本条历史里没有掉过（判定全是 ✅），触发原话未存。
找法：说"适应"时先在 get used to 和 settle in 里挑一个，⛔ 别先去够 adapt／adjust。

**题面**
"我搬到南方两年了，还是没习惯这边又湿又热的天气。"（"习惯"用 **get used to** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I've been in the south for two years, and I still haven't gotten used to the hot, humid weather.

- 2026-08-12 ✅
- 2026-08-16 ✅
- 2026-08-19 ✅ `new staff need time to settle in.`（settle in 用对；句中的 staff 因教练刚给过，不计 #129）
- 2026-09-10 ✅ 复检 · 第 4 组（打包）· `get used to the new environment`
- 2026-09-21 ⚡ 自评免测 · 复检第 3 组（她看完整组回「直接过」）
- 2026-09-29 📝 退池 · ① 同级说法
  "适应新环境"说 adapt to／adjust to 同样成立，get used to／settle in 只是口语偏好（旧题面靠排除项硬框）⇒ 中译英里产不出 ❌；历史零 ❌
- 2026-10-12 📝 撤销退池 · 付息日 a2 段复检第 6 组 [7]（#283 题里）她写 `getting used to(学下)` —— 她点名要学 ⇒ §3.6 ⛔ 不退 ⇒ 删掉状态行的退池；题面改正向点名整句（旧题面靠排除项 ⛔ 不许用 adapt／adjust 硬框，§6② 禁），题型 词组 → 整句
- 2026-10-12 ❌ 付息日 a2 段复检第 6 组 [7]（#283 题里）· 她标「学下」· 原话 `When learning to drive, it's really about getting used to(学下) the basic controls first, and then slowly taking it out on the road.` —— get used to 用法本身对（to 是介词，后面接名词），她点名要学 ⇒ 判 ❌（同 🎓#433 先例）⇒ **回潮**


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

### 290 · 收尾块：… for totally different reasons depending on who you ask（同一个现象，不同的人理由完全不一样）
类型 结构 ｜ 新建 2026-08-23（**她当场指定**）
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 整句 ｜ **回潮 2026-10-12**（08-28 毕业 → 10-12 复检第 7 组写成 `everyone has a different reason, depending.`，on who you ask 没出来，撤销毕业、连对清零）

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
- 2026-10-12 ❌ 付息日 a2 段复检第 7 组 [3] · `A lot of young people are moving back to their hometowns for work these days, and everyone has a different reason, depending.` —— depending 后面断了，on who you ask 没出来，收尾块没成形 ⇒ **回潮**
  最小改 `…, and everyone has a different reason, depending on who you ask.`
  更好版 `…these days, just for totally different reasons depending on who you ask.`（everyone 与 who you ask 说了两遍）

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
状态 连对0 连错2 上次2026-10-12 未毕业 ｜ 题型 整句 ｜ **回潮 2026-10-12**（09-22 毕业 → 10-12 复检 #277／#284 题里两次写成 `Planning a family trip, it's …`／`Whether a relationship can last long, it …`，话题后再用 it 回指，撤销毕业、连对清零）

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

### 453 · apartment complex（自己住的"小区"；⛔ our residential area）
类型 词汇 ｜ 新建 2026-10-11
状态 连对1 连错0 上次2026-10-12 未毕业 ｜ 题型 整句

**问题是什么**
**apartment complex** ＝ 自己住的那片楼（几栋楼围在一起、有大门／物业）：`the stray cats in our apartment complex` ／ `There's a gym in our complex.`（熟了直接说 our complex）
同一格里的邻居（别串）：neighborhood（住的这一带，范围更松，说"我们这片"也对）· residential area（城市里"一片住宅区"，跟商业区、工业区并列：`It's a quiet residential area.`）· building（一栋楼）。
判据一句话：说"**我住的**小区" ⇒ apartment complex（或 neighborhood）；描述城市里一整片住宅区 ⇒ residential area。
★ 题型判整句：要靠"我们小区门口／楼下"这种"自己住的地方"的语境，residential area 才会露馅；孤立的"小区"两个字两边都能落。
★ 与 🎓#431（well planned out）分工：那条 10-08 的原话 `This new residential area is really well planned out` 是在描述一整片新开发的住宅区 ⇒ residential area 在那里成立，不回头改判。

**怎么发现的**
2026-10-11 学习日 在池第 2 组 [3]（#447 题面"小区楼下那几只流浪猫"）· 原话
`those stray cats living downstairs in our residential area`
stray 本身对（#447 ✅），diff-2 ⚠️：说的是自己住的小区 ⇒ 更地道是 our apartment complex ⇒ §3.2b 能学的表达 ⇒ 建号。
判重三步：
　① 目标形式 dedup "residential" ⇒ 🎓#18（历史行原话 residential and industrial use，考论元完整）· 🎓#431（10-08 原话 new residential area，考 well planned out）⇒ 否；dedup "complex" ⇒ 🎓#219（complicated vs complex，形容词）⇒ 否；dedup "apartment complex" ⇒ 零命中
　② 中文 dedup "小区" ⇒ 🎓#428（be featured in）· 🎓#431（well planned out）· #447（stray）—— 只在题面里出现，没有一条考"小区怎么说" ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`in our residential area`　　更地道：`in our apartment complex`
找法：说到"小区"先问一句 —— 是我住的那片楼，还是城市里的一个区？我住的 ⇒ apartment complex。

**题面**
"我们小区门口新开了一家水果店。"（"小区"用 **complex** 说）

- 2026-10-11 ❌ 首犯 · 学习日 在池第 2 组 [3]（#447 题里）· diff-2 ⚠️ · 原话 `those stray cats living downstairs in our residential area` ⇒ 更好版 in our apartment complex
- 2026-10-12 ✅ 付息日 a 段在池第 2 组 [6] · `A new fruit store just opened up right outside our apartment complex.` —— our apartment complex（没落到 residential area）。连错 1 → 连对 1

### 454 · cut back on ＋ 东西（少吃／少用／少花：cut back on sugar）
类型 词组 ｜ 新建 2026-10-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-12 未毕业 ｜ 题型 整句

**问题是什么**
**cut back on sth** ＝ 把某样东西的量减下来（少吃、少用、少花）：`cut back on the sugar` ／ `I'm trying to cut back on coffee.` ／ `We need to cut back on spending.`
同一格里的邻居（别串）：cut down on（意思几乎一样，常说吃喝抽的量）· cut out（彻底戒掉、一点都不碰）· reduce（书面）。
判据一句话：想说"少放点／少吃点／少花点"某样东西 ⇒ cut back on ＋ 那样东西（on 不能丢）。
★ 题型判整句：中文"少吃点"单拎出来，eat less 也完全合法、收不拢 ⇒ 要靠句子 ＋ 正向点名才逼得出这个块；on 的挂接留给她。

**怎么发现的**
2026-10-11 学习日 复检第 3 组 [3]（#414 题面"这个菜谱我照着做了几次，自己稍微调了调，少放了点糖。"）· 原话
`I've cooked this recipe a few times, but I tweaked it a little by cutting back（这个短语学下) on the sugar.`
她写对了 cutting back on the sugar，但自己标「这个短语学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "cut back"／"cut down"／"cutting back" ⇒ 零命中
　② 中文 dedup "少放"／"少吃"／"减少" ⇒ 🎓#265（good for you，题面里有"少吃"）· 🎓#285（give sb alternatives，题面里有"少吃"）—— 考点都不是"减量"这个块 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个短语学下」（用法本身对）　　目标：`cut back on the sugar`
找法：说"少…点 X"，先落 cut back on X。

**题面**
"医生让我爸少吃点盐。"（"少吃点"用 **cut back on** 说）
★ 她点名要学的块：第一次出题整块点名；连对 ≥1 之后降回 cut back（on 留给她）

- 2026-10-11 ❌ 首犯 · 学习日 复检第 3 组 [3]（#414 题里）· 她标「这个短语学下」· 原话 `I've cooked this recipe a few times, but I tweaked it a little by cutting back（这个短语学下) on the sugar.`
- 2026-10-12 ✅ 付息日 a 段在池第 2 组 [7] · `The doctor told my dad to cut back on salt.` —— cut back on salt。连错 1 → 连对 1

### 455 · underprivileged（家境困难的、条件差的 —— 说"穷"的体面说法）
类型 词汇 ｜ 新建 2026-10-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-12 未毕业 ｜ 题型 词组

**问题是什么**
**underprivileged** ＝ 家境困难、缺少基本条件的（说人，比 poor 体面，慈善、公益场合常用）：`underprivileged kids` ／ `underprivileged families` ／ `underprivileged communities`
同一格里的邻居（别串）：poor（直白）· disadvantaged（几乎同义，略正式）· low-income（只说收入低）。
判据一句话：慈善、公益、帮扶的语境里说"穷人家的／条件不好的" ⇒ underprivileged ＋ 人。
★ 题型判词组：中文释义点明"说得体面一点、公益场合用的那个词"⇒ 收拢到 underprivileged；答 disadvantaged 也合法照判 ✅，答 poor ⇒ 没贴释义。

**怎么发现的**
2026-10-11 学习日 复检第 3 组 [5]（#416 题面"这家医院每年都办一场盛大的慈善晚会，给穷人家的孩子筹钱。"）· 原话
`This hospital holds a grand charity gala every year to raise money for underprivileged(这个词学下) kids.`
她写对了 underprivileged kids，但自己标「这个词学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "underprivileged"／"poor families"／"disadvantaged" ⇒ 零命中
　② 中文 dedup "贫困"／"穷人" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词学下」（用法本身对）　　目标：`underprivileged kids`
找法：要说"贫困孩子／困难家庭"又不想直接说 poor，先落 underprivileged。

**题面**
"山区那些家境困难的孩子"（说得体面一点的"穷"，慈善、公益场合常用的那个词）

- 2026-10-11 ❌ 首犯 · 学习日 复检第 3 组 [5]（#416 题里）· 她标「这个词学下」· 原话 `This hospital holds a grand charity gala every year to raise money for underprivileged(这个词学下) kids.`
- 2026-10-12 ✅ 付息日 a 段在池第 2 组 [8] · `underprivileged kids living in the mountain areas` —— underprivileged。连错 1 → 连对 1

### 456 · crafted（手工／精心做出来的：a manually crafted request · a carefully crafted message）
类型 词汇 ｜ 新建 2026-10-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-12 未毕业 ｜ 题型 整句

**问题是什么**
**craft** ＝ 花心思、一点点手工做出来；过去分词当形容词最常用：`a manually crafted network request`（手工构造的请求）· `a carefully crafted message`（精心写的一段话）· `hand-crafted furniture`（手工做的家具）。
同一格里的邻居（别串）：make／write（普通的"做／写"，没有"花心思"那层）· handmade（说实物手工做的）· put together（拼凑出来）。
判据一句话：想强调"不是现成的，是专门花心思一点点做出来的" ⇒ crafted（前面常挂 carefully／manually／hand-）。
★ 题型判整句：中文"精心准备的"单拎出来 prepare／write 都合法、收不拢 ⇒ 要靠句子 ＋ 正向点名才逼得出这个词。

**怎么发现的**
2026-10-11 学习日 ③ 新题 bank:963（P2 · Describe a person who solved a problem in a smart way）S8 · 原话
`he managed to inject a manually crafted(这个词学下) network request and started tracking it across the node logs.`
她写对了 manually crafted，但自己标「这个词学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "craft" ⇒ 零命中
　② 中文 dedup "手工" ⇒ 🎓#161 #313 #317 —— 只在历史行"手工逐条记账"的字样里，考点都不是这个词 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词学下」（用法本身对）　　目标：`a manually crafted network request`
找法：想说"专门手工做的／精心准备的"，先落 crafted，前面挂 carefully／manually。

**题面**
"他精心准备了一段生日祝福，吃饭时念给他妈妈听。"（"精心准备了"用 **carefully crafted** 说）
★ 她点名要学的块：第一次出题整块点名；连对 ≥1 之后降回 crafted（carefully 留给她）

- 2026-10-11 ❌ 首犯 · 学习日 ③ 新题 bank:963 S8 · 她标「这个词学下」· 原话 `he managed to inject a manually crafted(这个词学下) network request and started tracking it across the node logs.`
- 2026-10-12 ✅ 付息日 a 段在池第 2 组 [9] · `He carefully crafted a birthday message and read it to his mom during dinner.` —— carefully crafted a birthday message。连错 1 → 连对 1

### 457 · build up ＋ 经验／积蓄（一点点攒起来：build up experience）
类型 词组 ｜ 新建 2026-10-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-12 未毕业 ｜ 题型 整句

**问题是什么**
**build up ＋ 东西** ＝ 在时间里一点点攒起来：`how much experience he'd built up` · `build up some savings` · `build up your stamina`（练出体力）· `build up trust`。
同一格里的邻居（别串）：gain experience（获得经验，不强调慢慢攒）· accumulate（书面）· pile up（越堆越多，多说活儿、垃圾这类坏事：work piling up）· save up（专说攒钱：save up for a car）。
判据一句话：时间里慢慢攒出来的好东西（经验、积蓄、体力、信任）⇒ build up ＋ 东西。
★ 题型判整句：中文"攒了／积累了"单拎出来 gain／save／get 都合法、收不拢 ⇒ 要靠句子 ＋ 正向点名。

**怎么发现的**
2026-10-11 学习日 ③ 新题 bank:963（P2）S13 · 原话
`Plus, his debugging setup was really handy, which showed how much experience he'd built up(这个词组学下).`
她写对了 he'd built up，但自己标「这个词组学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "build up"／"built up" ⇒ 零命中
　② 中文 dedup "积累" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（用法本身对）　　目标：`how much experience he'd built up`
找法：想说"攒了／积累了"经验、积蓄、体力，先落 build up。

**题面**
"这几年我慢慢攒了一点积蓄。"（"攒了"用 **build up** 说）
★ 她点名要学的块：第一次出题整块点名；连对 ≥1 之后降回 build（up 留给她）

- 2026-10-11 ❌ 首犯 · 学习日 ③ 新题 bank:963 S13 · 她标「这个词组学下」· 原话 `Plus, his debugging setup was really handy, which showed how much experience he'd built up(这个词组学下).`
- 2026-10-12 ✅ 付息日 a 段在池第 2 组 [10] · `I've slowly built up a bit of savings over the past few years.` —— built up … savings。连错 1 → 连对 1

### 458 · snuggle up（舒服地贴着／窝着：snuggle up to sb · on／in ＋ 地方）
类型 词组 ｜ 新建 2026-10-12 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 整句

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

### 459 · in sb's arms（怀里）≠ in sb's lap（腿上）
类型 词组 ｜ 新建 2026-10-12 ｜ 她说不会
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 词组

**问题是什么**
**in sb's arms** ＝ 在某人怀里（被两条胳膊搂在胸前）：`a baby asleep in her arms` · `hold sb in your arms` · `snuggle into sb's arms`（钻进怀里）。
**in sb's lap** ＝ 在某人腿上（坐着时大腿上面那块）：`The cat curled up in my lap.` · `sit on／in sb's lap`。
同一格里的邻居（别串）：hug（抱一下，是动作）· on sb's shoulder（趴在肩上）。
判据一句话：被胳膊搂着、贴在胸前 ⇒ arms；坐着的人腿上 ⇒ lap。中文"怀里"默认 ⇒ in sb's arms。
★ 题型判词组：中文块"怀里"＋"被胳膊搂在胸前"的语境只映射回 in sb's arms。

**怎么发现的**
2026-10-12 付息日 a 段在池第 1 组 [5]（#442 题面"我奶奶养的那只兔子特别亲人，总爱往人怀里钻。"）· 原话
`My grandma's rabbit is super affectionate and loves snuggling up（这个词组学下) into people's laps(怀里怎么说，不会).`
她标「怀里怎么说，不会」⇒ §2③ 建号，判 ❌；她落到的 laps ＝ 腿上，"往人怀里钻" ⇒ arms。
判重三步：
　① 目标形式 dedup "arms"／"lap" ⇒ 零命中
　② 中文 dedup "怀里"／"腿上" ⇒ 零命中；dedup "怀" ⇒ #429 🎓#280 🎓#294 —— 只是正文／历史行字串，考点不是它 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）；与 #458（snuggle up）是两个考点，见 #458 分工

**我错在哪**
她的：`into people's laps`（标「怀里怎么说，不会」）　　正确：`into people's arms`
找法：说"怀里"先落 arms；只有"坐在腿上"才用 lap。

**题面**
"睡在妈妈怀里的小婴儿"（被两条胳膊搂在胸前的那个位置，不是坐在腿上）

- 2026-10-12 ❌ 首犯 · 付息日 a 段在池第 1 组 [5]（#442 题里）· 她说不会 · 原话 `… loves snuggling up（这个词组学下) into people's laps(怀里怎么说，不会).` ⇒ 最小改 into people's arms

### 460 · internship（实习）／intern（实习生）
类型 词汇 ｜ 新建 2026-10-12 ｜ ⭐ 她点名要背
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 词组

**问题是什么**
**internship** ＝ 实习（那段经历）：`do an internship at a hospital` · `finish my internship` · `a summer internship`。
**intern** ＝ 实习生（人），也能当动词：`She interned at Google.`
同一格里的邻居（别串）：trainee（培训生）· work experience（英式，学生的短期实习）· placement（英式，实习岗位）。
判据一句话：说"那段实习" ⇒ internship；说"实习的人" ⇒ intern。
★ 题型判词组：中文块"那段实习"只映射回 internship。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 4 组 [1]（🎓#368 题面"我表妹实习结束后，直接在那家医院谋到了一份正式工作。"）· 原话
`After my cousin finished her internship（这个背一下), she landed a permanent job at that hospital.`
她写对了 internship，但自己标「这个背一下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 🎓#433 先例）。
判重三步：
　① 目标形式 dedup "intern" ⇒ 零命中
　② 中文 dedup "实习" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个背一下」（词不在手边）　　目标：`finished her internship`
找法：说"实习"先落 internship；说"实习生"⇒ intern。

**题面**
"大三暑假在一家广告公司做的那段实习"（边学边干、还没正式入职的那段经历）

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 4 组 [1]（#368 题里）· 她标「这个背一下」· 原话 `After my cousin finished her internship（这个背一下), she landed a permanent job at that hospital.`

### 461 · a boom in sth／the X boom（热潮、一下子火起来；⛔ the boom of sth）
类型 搭配 ｜ 新建 2026-10-12
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 整句

**问题是什么**
**boom** 说"某样东西一下子火起来"，两种挂法：`the bike-sharing boom`（东西放在 boom 前面）· `a boom in shared bikes`（后面接 **in**）。
⛔ the boom of sth：boom 后面的介词是 in，跟 a rise in／an increase in 同一格。
同一格里的邻居（别串）：the rise of sth（兴起，这里才是 of）· take off（动词"火起来"：Bike-sharing really took off.）。
判据一句话：boom 后面挂东西 ⇒ in；或者把东西直接放到 boom 前面。
★ 题型判整句：介词 in 要靠句子里"boom 后面挂东西"才现形。
★ 与 🎓#370（create ＋ 结果）分工：#370 考动词 create，本条考名词 boom 的挂法 ⇒ 两条。
　09-30 #370 历史里她写过 `This e-commence boom`（前置用法对）⇒ 本条缺口在"后面接 in"那一半。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 4 组 [3]（🎓#370 题面"共享单车的兴起造就了一个全新的行业。"）· 原话
`The boom of shared bikes created a completely new industry.`
create 本身对（#370 ✅），diff-2 ⚠️：boom 后面挂东西用 in（或把东西前置），⛔ of ⇒ §3.2b 能学的搭配 ⇒ 建号。
判重三步：
　① 目标形式 dedup "boom" ⇒ 只命中 🎓#370 历史行（09-30 她写的 This e-commence boom，考点是 create）⇒ 否；dedup "rise of" ⇒ 🎓#370 历史字串 ⇒ 否
　② 中文 dedup "热潮" ⇒ 🎓#370 题面（考点"造就"）⇒ 否；"兴起" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`The boom of shared bikes`　　更地道：`The boom in shared bikes`／`The bike-sharing boom`
找法：说完 boom 想往后挂东西 ⇒ 用 in，或者干脆把东西提到 boom 前面。

**题面**
"这几年露营突然火了起来。"（"火了起来"用 **boom** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：There's been a real boom in camping over the past few years. ／ the camping boom

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 4 组 [3]（#370 题里）· diff-2 ⚠️ · 原话 `The boom of shared bikes created a completely new industry.` ⇒ 更好版 The boom in shared bikes

### 462 · blackout（停电）
类型 词汇 ｜ 新建 2026-10-12 ｜ ⭐ 她点名要背
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 词组

**问题是什么**
**blackout** ＝ 停电（一片区域整个断电）：`during the blackout` · `There was a blackout last night.`
同一格里的邻居（别串）：power cut（英式，同义）· power outage（美式偏正式，新闻里常见）· The power went out.（口语动词说法："电停了"）。
判据一句话：说"停电"这件事 ⇒ a blackout／a power cut；说"电停了"这个动作 ⇒ the power went out。
★ 题型判词组：中文块"停电的那两个小时"映射回 the blackout（power cut／power outage 合法照判）。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 5 组 [1]（🎓#236 题面"这次停电倒给了我们一家人一个放下手机聊天的理由。"）· 原话
`The blackout(这个单词背下) actually gave our family an excuse to put our phones down and just talk to each other.`
她写对了 blackout，但自己标「这个单词背下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 🎓#433 先例）。
判重三步：
　① 目标形式 dedup "blackout"／"power cut"／"outage" ⇒ 零命中
　② 中文 dedup "停电" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个单词背下」（词不在手边）　　目标：`The blackout`
找法：说"停电"先落 blackout；说"电停了"⇒ the power went out。

**题面**
"昨晚小区突然停电的那两个小时"（整片楼一下子全黑了的那种）

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 5 组 [1]（#236 题里）· 她标「这个单词背下」· 原话 `The blackout(这个单词背下) actually gave our family an excuse to put our phones down and just talk to each other.`

### 463 · talk sth through（一起把一件事一步一步聊透、商量清楚）
类型 词组 ｜ 新建 2026-10-12 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 整句

**问题是什么**
**talk through sth ／ talk sth through** ＝ 一起把一件事从头到尾过一遍、商量清楚：`talk through their tactics` · `Let's talk it through.`（宾语是代词 ⇒ 放中间）。
同一格里的邻居（别串）：talk things out（把矛盾说开，偏化解分歧）· think sth through（自己想透）· go over sth（过一遍）。
判据一句话：一起把细节过一遍 ⇒ talk through；把矛盾说开 ⇒ talk out；自己想清楚 ⇒ think through。
★ 题型判整句："商量一遍"能落到 discuss／go over 一串合法说法，代词位置也要靠句子现形 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 6 组 [6]（🎓#281 题面"球队训练时，教练有时候会退一步，让队员自己商量战术。"）· 原话
`During practice, the coach sometimes takes a step back and lets the team talk through(这个词组学下) their own tactics(背下).`
她写对了 talk through，但自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 🎓#433 先例）。
判重三步：
　① 目标形式 dedup "talk through"／"talk it through"／"think things through" ⇒ 零命中
　② 中文 dedup "商量" ⇒ 只命中本条与 #464 自己（同一句建的号）⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）；同句 tactics 另建 #464

**我错在哪**
她的：自己标「这个词组学下」（块不在手边）　　目标：`talk through their own tactics`
找法：想说"商量／聊一遍"，先落 talk through；宾语是代词 ⇒ talk it through。

**题面**
"签合同之前，我们俩坐下来把每一条都商量了一遍。"（"商量了一遍"用 **talk through** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Before signing the contract, we sat down and talked through every clause.

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 6 组 [6]（#281 题里）· 她标「这个词组学下」· 原话 `During practice, the coach sometimes takes a step back and lets the team talk through(这个词组学下) their own tactics(背下).`

### 464 · tactics（战术）
类型 词汇 ｜ 新建 2026-10-12 ｜ ⭐ 她点名要背
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 词组

**问题是什么**
**tactics** ＝ 战术（比赛／打仗里具体怎么打）：`the team's tactics` · `change tactics at half-time`，常用复数。
同一格里的邻居（别串）：strategy（战略、整体大方向，偏长远）· game plan（口语，这场比赛的整体打法）。
判据一句话：具体一招一式 ⇒ tactics；整体大方向 ⇒ strategy。
★ 题型判词组：中文块"临时换的战术"映射回 tactics。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 6 组 [6]（🎓#281 题面"球队训练时，教练有时候会退一步，让队员自己商量战术。"）· 原话
`During practice, the coach sometimes takes a step back and lets the team talk through(这个词组学下) their own tactics(背下).`
她写对了 tactics，但自己标「背下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 🎓#433 先例）。
判重三步：
　① 目标形式 dedup "tactic"／"strategy" ⇒ 除本条自己外零命中
　② 中文 dedup "战术" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「背下」（词不在手边）　　目标：`their own tactics`
找法：说"战术"先落 tactics（带 s）。

**题面**
"教练中场休息时临时换的战术"（具体怎么打、怎么跑位的那种安排）

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 6 组 [6]（#281 题里）· 她标「背下」· 原话 `During practice, the coach sometimes takes a step back and lets the team talk through(这个词组学下) their own tactics(背下).`

### 465 · hydrated（水分够的、不缺水的：keep your skin hydrated · stay hydrated）
类型 词汇 ｜ 新建 2026-10-12 ｜ ⭐ 她点名要背
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 整句

**问题是什么**
**hydrated** ＝ 身体／皮肤里水分够、不缺水：`keep your skin hydrated` · `stay hydrated`（多喝水、别缺水）。
同一格里的邻居（别串）：moisturized（皮肤抹了保湿霜）· dehydrated（脱水、缺水）· hydrate（动词，补水）。
判据一句话：水分够、不缺水 ⇒ hydrated；用护肤品保湿 ⇒ moisturized。
★ 题型判整句："补水／别缺水"能落到 drink enough water 一串合法说法 ⇒ 词组题零英文提示收不拢 ⇒ 整句 ＋ 正向点名（她说要背 ⇒ 第一次整块点名）。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 7 组 [6]（🎓#297 题面"多喝水能让皮肤水水润润的。"）· 原话
`Drinking lots of water helps keep your skin hydrated（背一下).`
她写对了 hydrated，但自己标「背一下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 🎓#433 先例）。
判重三步：
　① 目标形式 dedup "hydrat" ⇒ 零命中
　② 中文 dedup "水润" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「背一下」（词不在手边）　　目标：`keep your skin hydrated`
找法：说"补水／别缺水"先落 stay hydrated；说皮肤水润 ⇒ keep your skin hydrated。

**题面**
"天热出去跑步，一定要多喝水，别让身体缺水。"（"别让身体缺水"用 **hydrated** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：When it's hot and you go out for a run, make sure you drink plenty of water and stay hydrated.

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 7 组 [6]（#297 题里）· 她标「背一下」· 原话 `Drinking lots of water helps keep your skin hydrated（背一下).`

### 466 · sign off (on sth)（签字确认、批准放行）
类型 词组 ｜ 新建 2026-10-12 ｜ ⭐ 她点名要背
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 整句

**问题是什么**
**sign off (on sth)** ＝ 签字确认、批准放行：`The manager has to sign off on the budget.` · `sign off at every stage`。
同一格里的邻居（别串）：sign（签名这个动作本身）· approve（批准，偏正式）· sign up（报名）。
判据一句话：签字 ＝ 批准放行 ⇒ sign off (on)；只是写个名字 ⇒ sign；报名 ⇒ sign up。
★ 题型判整句："签字确认"能落到 sign／approve 一串合法说法，on 的挂法也要靠句子现形 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 7 组 [9]（🎓#300 题面"这个项目每个阶段都得有人签字确认。"）· 原话
`Someone needs to sign off(这个词组背一下) at every stage of this project.`
她写对了 sign off，但自己标「这个词组背一下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 🎓#433 先例）。
判重三步：
　① 目标形式 dedup "sign off" ⇒ 零命中
　② 中文 dedup "签字" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组背一下」（块不在手边）　　目标：`sign off at every stage`
找法：说"签字确认／批了"先落 sign off，后面挂东西用 on。

**题面**
"报销单得先让部门经理签字，财务才会打钱。"（"签字"用 **sign off** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Your department manager has to sign off on the expense report before finance pays you back.

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 7 组 [9]（#300 题里）· 她标「这个词组背一下」· 原话 `Someone needs to sign off(这个词组背一下) at every stage of this project.`

### 467 · charge 的主语是收钱的一方（the lot charges you）；事情本身花多少钱 ⇒ cost（parking costs you）
类型 搭配 ｜ 新建 2026-10-12
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 整句

**问题是什么**
**charge** ＝ 收钱，主语是**收钱的人／机构**：`The parking lot charges twenty bucks an hour.` · `They charge you for the bags.`
**cost** ＝ 花掉多少钱，主语是**那件事／那样东西**：`Parking costs twenty bucks an hour.` · `That trip cost me a fortune.`
同一格里的邻居（别串）：fee（收的那笔钱）· pay（付钱的人当主语：I paid twenty bucks）。
判据一句话：主语是"收钱的那一方" ⇒ charge；主语是"那件事／东西" ⇒ cost。
★ 题型判整句：主语和动词的搭配要靠句子才现形。
★ 与 🎓#288（once X costs you something 机制句型）分工：#288 考整句机制框架，本条考 charge／cost 跟主语怎么配 ⇒ 两条。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 7 组 [1]（🎓#288 题面"一旦停车每小时要收二十块，你就会开始琢磨是不是坐地铁更划算。"）· 原话
`Once parking charges you twenty bucks an hour, you start asking whether taking the subway is a better deal.`
#288 机制框架本身对（✅），diff-2 ⚠️：parking（事情）当主语却配了 charge ⇒ costs ⇒ §3.2b 能学的搭配 ⇒ 建号。
判重三步：
　① 目标形式 dedup "charge" ⇒ 🎓#110 🎓#282 只是历史行字串（in charge 等），考点不是它 ⇒ 否；dedup "costs you" ⇒ 🎓#288（机制句型里的 costs you，考点是 once 框架）⇒ 否
　② 中文 dedup "收" 太宽、未作为判据；以英文形式为准
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`Once parking charges you twenty bucks an hour`　　更地道：`Once parking costs you twenty bucks an hour`
找法：用 charge 之前看一眼主语 —— 它会伸手收钱吗？不会 ⇒ 换 cost。

**题面**
"在市中心停车，一小时就要二十块。"（"要二十块"用 **charge** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Parking lots downtown charge twenty yuan an hour.／They charge you twenty yuan an hour to park downtown.（⛔ Parking downtown charges …）

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 7 组 [1]（#288 题里）· diff-2 ⚠️ · 原话 `Once parking charges you twenty bucks an hour, you start asking whether taking the subway is a better deal.` ⇒ 更好版 parking costs you

### 468 · reservoir（水库）
类型 词汇 ｜ 新建 2026-10-12 ｜ ⭐ 她点名要背
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 词组

**问题是什么**
**reservoir** ＝ 水库（人工蓄水、供水用的那种）：`the reservoir east of the village` · `The reservoir supplies water to the whole city.`
同一格里的邻居（别串）：lake（天然的湖）· pond（池塘）· dam（大坝，拦水的那道墙）。
判据一句话：人工蓄水 ⇒ reservoir；天然的 ⇒ lake；拦水的墙 ⇒ dam。
★ 题型判词组：中文块"给全城供水的那座水库"只映射回 reservoir。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 8 组 [1]（🎓#308 题面"这条小溪最后流进了村子东边的水库。"）· 原话
`This stream eventually empties into the reservoir(背下) east(to east 对不对) of the village.`
她写对了 reservoir，但自己标「背下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 🎓#433 先例）。
判重三步：
　① 目标形式 dedup "reservoir" ⇒ 零命中
　② 中文 dedup "水库" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）；同句的 east of 另建 #469

**我错在哪**
她的：自己标「背下」（词不在手边）　　目标：`the reservoir`
找法：说"水库"先落 reservoir。

**题面**
"给全城供水的那座水库"（山里修坝拦起来、专门蓄水的那种）

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 8 组 [1]（#308 题里）· 她标「背下」· 原话 `This stream eventually empties into the reservoir(背下) east(to east 对不对) of the village.`

### 469 · east of X ＝ to the east of X（在 X 的东边；⛔ to east of X）
类型 搭配 ｜ 新建 2026-10-12 ｜ 她问
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

**问题是什么**
说"在 X 的东边"两种说法都对：**east of the village**（east 直接当方位词，不带 to、不带 the）· **to the east of the village**（要用 to 就得带 the）。
⛔ to east of the village（to 有了、the 丢了）。north／south／west 同理：north of the city ＝ to the north of the city。
同一格里的邻居（别串）：🎓#310 all the way east（往东一路走，east 当方向副词）· in the east of China（在境内的东部，用 in）。
判据一句话：要 to 就带 the；不要 to 就连 the 一起不要；在境内 ⇒ in the east of。
★ 题型判整句：to／the 有没有要靠句子才现形；零提示（north of／to the north of 都对）。
★ 与 🎓#310 分工：#310 考 all the way 后面接方向（正文写着"要用 to 必须连冠词加名词"），本条考"在…东边"的方位说法 ⇒ 两条共用"要 to 就带 the"这一小判据，目标形式不同。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 8 组 [1]（🎓#308 题面"这条小溪最后流进了村子东边的水库。"）· 原话
`This stream eventually empties into the reservoir(背下) east(to east 对不对) of the village.`
她写的 east of the village 本身对，但自己问「to east 对不对」⇒ §2③ 她主动提出 ⇒ 建号；她没写错 ⇒ 建号行记 📝、不判档位（同 🎓#310 08-30 先例）。
判重三步：
　① 目标形式 dedup "east of" ⇒ 零命中；dedup "to the east" ⇒ 🎓#310（all the way 判据里的 all the way to the east coast）· 🎓#387（历史行字串 drifting slowly to the east）⇒ 考点不同，否
　② 中文 dedup "东边" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`east of the village`（对）＋ 她问「to east 对不对」　　答：⛔ to east of；✅ east of ／ to the east of
找法：说完 to 看后面有没有 the；没有 ⇒ 要么补 the，要么把 to 也去掉。

**题面**
"那个新机场在城市北边四十公里。"
★ 零提示：forty kilometers north of the city ／ to the north of the city 都算对；只有 to north of 算掉

- 2026-10-12 📝 新建 · 付息日 a2 段复检第 8 组 [1]（#308 题里）· 她问 · 原话 `… the reservoir(背下) east(to east 对不对) of the village.` —— 她写的 east of 本身对，不判档位

### 470 · with its siren blaring（鸣着笛；警笛 siren · 刺耳地响 blare）
类型 词组 ｜ 新建 2026-10-12 ｜ 她说不会
状态 连对0 连错1 上次2026-10-12 未毕业 ｜ 题型 整句

**问题是什么**
**with ＋ 名词 ＋ -ing** ＝ 伴随状态："鸣着笛" ⇒ `with its siren blaring`（好几辆 ⇒ `with sirens blaring`）。
**siren** ＝ 警笛（救护车／警车／消防车上的）；**blare** ＝ 声音很大、刺耳地响。
同一格里的邻居（别串）：honk (the horn)（普通车按喇叭）· beep（短促地嘀一声）· sound the alarm（拉警报）。
判据一句话：救护车／警车／消防车 ⇒ siren blaring；普通车 ⇒ honk。
★ 题型判整句："鸣着笛"能落到 sounding its siren／with the siren on 一串合法说法 ⇒ 整句 ＋ 正向点名（她说不会 ⇒ 第一次点 siren）。

**怎么发现的**
2026-10-12 付息日 a2 段复检第 8 组 [9]（🎓#311 题面"救护车一路鸣着笛，从车流里穿了过去。"）· 原话
`With its siren blaring（鸣笛怎么说，学下）, the ambulance wove its way through the heavy traffic.`
她标「鸣笛怎么说，学下」⇒ §2③ 她说不会 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "siren"／"blaring" ⇒ 零命中
　② 中文 dedup "鸣笛"／"警笛" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`With its siren blaring（鸣笛怎么说，学下）`（她标不会）　　目标：`with its siren blaring`
找法：说"鸣笛"先分车 —— 特种车 ⇒ siren，普通车 ⇒ honk。

**题面**
"半夜一辆消防车鸣着笛从我家楼下开过去。"（"鸣着笛"用 **siren** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：In the middle of the night, a fire truck drove past my building with its siren blaring.

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 8 组 [9]（#311 题里）· 她说不会 · 原话 `With its siren blaring（鸣笛怎么说，学下）, the ambulance wove its way through the heavy traffic.`

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

