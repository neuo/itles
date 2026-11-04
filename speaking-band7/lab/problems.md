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
- 2026-10-30 ⚪ 学习日 在池第 2 组 [2]（#559 题里）· `long queues for photo` → `for photos` —— 可数名词单数光秃秃；同句 long queues 复数她自己做对 ⇒ 形态类只记录·不出题（检查触发：名词前停一下 —— 可数吗？单数就补 a／the，泛指就变复数）
- 2026-11-02 ⚪ 学习日 在池第 1 组 [8]（#568 题里）· `pitch our tent using flashlight` → using a flashlight —— 可数名词单数光秃秃；同组 a new refrigerator／a street vendor／a business trip 她都带对 ⇒ 形态类只记录·不出题（检查触发：名词前停一下 —— 可数吗？单数就补 a／the，泛指就变复数）


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

### 562 · **the next／past few days**（"这几天"（眼下短期）＝ for the next few days／the past few days；⛔ these days）
类型 词组 ｜ 新建 2026-10-27
状态 连对2 连错0 上次2026-11-03 ｜ **🎓 已毕业 2026-11-03** ｜ 题型 整句

**问题是什么**
中文"这几天"说的是**眼下短短几天**：往后几天 ⇒ **for the next few days**／over the next few days；过去几天 ⇒ **for the past few days**／the last few days（一般配完成时：`It's been raining for the past few days.`）。
同一格里的邻居（别串）：**these days** ＝ 如今、最近这一阵子（长期常态、跟以前对比）：`Kids these days …` · `Everyone's on their phone these days.` · 🎓#271（recently 一族默认拉完成时，要用一般现在时就换成 these days —— 那是 these days 用对的一边）。
判据一句话：一场病、一段天气、一阵忙这种几天就过去的事 ⇒ the next／past few days；现在这个时代、这几年的常态 ⇒ these days。
★ 题型判整句：考点是"这几天"在句子里落成哪一个（短期 vs 长期），孤立翻"这几天"看不出语境 ⇒ 整句 ＋ 正向点名 few days（next／past 与介词留给她）。

**怎么发现的**
2026-10-27 付息日 a2 复检第 4 组 [4]（🎓#465 题面"医生说我发烧这几天得多喝水，别让身体缺水。"）· 原话
`The doctor said I need to drink tons of water while I have a fever these day so I stay hydrated.`
考点 stay hydrated 用对（#465 ✅）；不在考点上的一处：发烧"这几天"落成 these day(s) —— these days 是"如今、这一阵子"的长期说法，发烧那几天说偏了 ⇒ for the next few days ⇒ §3.2b 能学的表达（选词偏了，⛔ 不是同级近义词）⇒ 建号（同 #548 #549 #559 先例：⚠️ 建号记 ❌ 首犯）。these day 漏 s 是形态，只点出。
判重三步：
　① 目标形式 dedup "these days" ⇒ 🎓#271（recently／lately 一族要用一般现在时就换 these days —— 讲的是 these days 该用的地方，本条讲的是不该用的地方，目标形式是 the next／past few days）· 🎓#81 #91 #164（历史字样）⇒ 都否；"few days" ⇒ 🎓#90 #528（历史字样）⇒ 否
　② 中文 dedup "这几天" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`while I have a fever these day`　　更地道：`for the next few days while I have a fever`
找法：中文"这几天"先问一句 —— 是过几天就完的事吗？是 ⇒ the next few days（往后）／the past few days（过去），these days 留给"如今的常态"。

**题面**
"这几天一直下雨，阳台上的衣服都晾不干。"（"这几天"用 **few days** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：It's been raining for the past few days, so the clothes on the balcony just won't dry.

- 2026-10-27 ❌ 首犯 · 付息日 a2 复检第 4 组 [4]（🎓#465 题里）· 不在考点上的一处 · 原话 `The doctor said I need to drink tons of water while I have a fever these day so I stay hydrated.` ⇒ 更好版 for the next few days
- 2026-10-30 ✅ 学习日 在池第 2 组 [5] · `It's rained for a few days straight, and none of the laundry on the balcony will dry.` —— for a few days straight ✓（短期"这几天"没落 these days，配完成时）。连错 1 → 连对 1
- 2026-11-01 ❌ 学习日 在池第 1 组 [5] · `I'm working from home these few days, so feel free to come to grab the keys whenever you feel like it.` —— 往后几天落成 these few days。连对 1 → 清零，连错 1
  最小改 `I'm working from home for the next few days, …`
  ❌ 往后几天 ⇒ for the next few days；these days 是长期常态，these few days 两头都不是
- 2026-11-02 ✅ 学习日 在池第 1 组 [2] · `I've been grinding on my thesis for the past few days, so I've barely gotten any sleep.` —— for the past few days（过去几天配完成进行时）。连错 1 → 连对 1
- 2026-11-03 ✅ 付息日 a 段在池第 1 组 [1] · `I'm out of town on business for the next few days, so just drop me a message on WeChat if you need anything.` —— for the next few days。连对 1 → 2 ⇒ 🎓 毕业

### 564 · **hail**（冰雹，不可数；一场冰雹 ＝ a hailstorm）
类型 词汇 ｜ 新建 2026-10-30 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-11-03 ｜ **🎓 已毕业 2026-11-03** ｜ 题型 整句

**问题是什么**
**hail** ＝ 冰雹（不可数）：`There was hail the size of golf balls.`；一场冰雹 ＝ **a hailstorm**（一个词）；一颗颗冰雹 ＝ hailstones；动词 `It's hailing.` ＝ 正在下冰雹。
同一格里的邻居（别串）：sleet（雨夹雪）· snow · hail a taxi（招手叫车，另一个义项）。
判据一句话：说"冰雹"这东西 ⇒ hail（不加 a）；说"一场冰雹" ⇒ a hailstorm。
★ 题型判整句：考点除了 hail 这个词，还有"一场"落 a hailstorm、不说 a hail ⇒ 要靠句子才现形 ⇒ 整句 ＋ 正向点名 hail（形留给她）。

**怎么发现的**
2026-10-30 学习日 复检第 4 组 [3]（🎓#472 题面"去年一场冰雹把屋顶砸坏了，保险公司赔了三万块。"）· 原话
`A hail(学下这个词) storm damaged our roof last year, and the insurance company paid out thirty grand.(这个词学下)`
她用对了 hail，自己标「学下这个词」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #560 #561 #563 先例）。hail storm 连写 hailstorm 是拼写（§2.1 不算）。
判重三步：
　① 目标形式 dedup "hail" ⇒ 🎓#219 #349（历史字样）⇒ 否
　② 中文 dedup "冰雹" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 `A hail storm damaged our roof`，但词不在手边（自己标学下）　　目标：`A hailstorm damaged our roof`
找法：中文"冰雹"先落 hail；要说"一场"就换 a hailstorm。

**题面**
"下午突然下了一场冰雹，停车场里好几辆车都被砸出了坑。"（"一场冰雹"用 **hail** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：There was a sudden hailstorm this afternoon, and quite a few cars in the parking lot got dented.

- 2026-10-30 ❌ 首犯 · 学习日 复检第 4 组 [3]（🎓#472 题里）· 她标「学下这个词」· 原话 `A hail(学下这个词) storm damaged our roof last year, and the insurance company paid out thirty grand.(这个词学下)`
- 2026-11-01 ❌ 学习日 在池第 1 组 [7] · `A sudden storm of(storm of 可以学下) hail hit this afternoon …` —— 一场冰雹没落到 a hailstorm，她自标「storm of 可以学下」（§3.2b 不在手边照判 ❌）。连错 1 → 2
  最小改 `A sudden hailstorm hit this afternoon …`
  ❌ 天气的"一场 X"是合成词 hailstorm／rainstorm／snowstorm；a storm of ＋ 名词多是比喻（a storm of criticism）
- 2026-11-01 📝 题面整改 · 连错 2 且她自标「storm of 可以学下」⇒ §6② 她说要学的块先练：点名从 hail 改成整块 **hailstorm**；连对 ≥1 之后降回 hail（不可数、不说 a hail 留给她）
- 2026-11-02 ✅ 学习日 在池第 1 组 [4] · `Last night's hailstorm smashed several windows in our apartment complex.` —— last night's hailstorm。连错 2 → 连对 1
- 2026-11-02 📝 题面整改 · 连对 ≥1 ⇒ 点名从整块 hailstorm 降回 hail（§6②：她说要学的块先练，连对 ≥1 后降回 lemma；"一场"落 a hailstorm、⛔ a hail 留给她）
- 2026-11-03 ✅ 付息日 a 段在池第 1 组 [2] · `Last summer, a sudden hailstorm knocked nearly all the apples off the trees in our orchard.` —— a sudden hailstorm（点名只给 hail）。连对 1 → 2 ⇒ 🎓 毕业

### 566 · **street vendor**（路边摊贩：buy／get sth FROM a street vendor；摊子本身 ＝ a street stall）
类型 词汇 ｜ 新建 2026-11-01 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-11-03 ｜ **🎓 已毕业 2026-11-03** ｜ 题型 整句

**问题是什么**
**street vendor** ＝ 在路边摆摊卖东西的人（卖小吃、卖水果的那种）；东西是从人手里买的 ⇒ `buy／get sth from a street vendor`：`I grabbed some dumplings from a street vendor.`
同一格里的邻居（别串）：a street stall／a food stall（摊子本身：`eat at a street stall`）· street food（路边小吃）· 🎓#430 street market（一整片集市）· #563 stall（车熄火，另一个义项）。
判据一句话：说人 ⇒ vendor（前面用 from）；说摊子 ⇒ stall（前面用 at）。
★ 题型判整句："路边摊"能落到 street stall／food stand／street vendor 一串，又要看介词 from 挂在句子里 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 street vendor，连对 ≥1 后降回 vendor。

**怎么发现的**
2026-11-01 学习日 在池第 1 组 [1]（#338 题面"我们找了半天餐厅，最后只好在路边摊随便吃了点。"）· 原话
`We searched for a restaurant forever, and ended up just getting some food at a street vendor（这个单词背下).`
她写出了 street vendor，但自己标「这个单词背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌；同 #560 #561 #563 #564 #565 先例）。同句 at a street vendor ⇒ 更好版 from a street vendor（⚠️）。
判重三步：
　① 目标形式 dedup "vendor" ⇒ 零命中；"street food" ⇒ 零命中；"stall" ⇒ 只命中 #563（车熄火义项，正文提到 market stall 当邻居）⇒ 否，不同义项
　② 中文 dedup "路边摊" ⇒ 零命中；"摊" ⇒ 🎓#430 street market（集市，块不同）· #563（同上）· 🎓#27 #295 #550 #206 #300（分摊／摊开，字面撞）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写出了 `a street vendor`，但词不在手边（自己标背下）；介词用了 at　　目标：`getting some food from a street vendor`
找法：说到"路边摊"先问一句 —— 说的是摆摊的人还是那个摊子？人 ⇒ from a street vendor；摊子 ⇒ at a street stall。

**题面**
"下班路上我常在一个路边摊买煎饼当晚饭。"（"路边摊"用 **vendor** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：On my way home from work, I often buy a jianbing from a street vendor for dinner.

- 2026-11-01 ❌ 首犯 · 学习日 在池第 1 组 [1]（#338 题里）· 她标「这个单词背下」· 原话 `We searched for a restaurant forever, and ended up just getting some food at a street vendor（这个单词背下).`
- 2026-11-02 ✅ 学习日 在池第 1 组 [6] · `I frequently buy dinner from a street vendor on my commute back home.` —— buy dinner from a street vendor（from 挂人）。连错 1 → 连对 1
- 2026-11-02 📝 题面整改 · 连对 ≥1 ⇒ 点名从整块 street vendor 降回 vendor（§6②；介词 from 留给她）
- 2026-11-03 ✅ 付息日 a 段在池第 1 组 [3] · `I grabbed a stick of grilled squid from a local vendor at the night market.` —— from a local vendor（点名只给 vendor）。连对 1 → 2 ⇒ 🎓 毕业；同句新建 #581 #582 #583

### 567 · **make a point of ＋ -ing**（特意、专门去做某事：He made a point of booking a table with a view.）
类型 词组 ｜ 新建 2026-11-01 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-11-03 ｜ **🎓 已毕业 2026-11-03** ｜ 题型 整句

**问题是什么**
**make a point of doing sth** ＝ 特意／专门去做（当成一件要紧事去做，常带"有心、用心"的意思）：
`He made a point of booking a table with a view.` ／ `She makes a point of calling her mom every Sunday.`
结构：of 后面接 -ing（make a point to … 也有人说，但 of ＋ -ing 是最稳的那个）。
同一格里的邻居（别串）：make a point（发言里"提出一个观点"：You make a good point.）· go out of one's way to do（特意费周折去做，更强调"多绕了路、多费了劲"）· 🎓#517 didn't bother to do（压根没费那个事，正好反过来）。
判据一句话：中文"特意／专门（有心地）做…" ⇒ make a point of ＋ -ing。
★ 题型判整句："特意"能落到 specially／deliberately／went out of his way 一串，块里的 of ＋ -ing 要靠句子才现形 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 make a point of，连对 ≥1 后降回 point。

**怎么发现的**
2026-11-01 学习日 复检第 2 组 [5]（🎓#477 题面"第一次约会他特意订了能看到江景的位子，那天晚上一下子就显得很特别。"）· 原话
`He made a point of(这个词组学下) reserving a table with a river view for our first date, so that night just felt so special.`
她写对了 made a point of reserving，但自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌；同 #566 先例）。
判重三步：
　① 目标形式 dedup "make a point" ⇒ 零命中；"point of" ⇒ 🎓#236（历史字样，说人的目的用 to do）⇒ 否；"out of his way"／"go out of" ⇒ 零命中
　② 中文 dedup "特意" ⇒ 🎓#115（a couple of，历史字样）· 🎓#517（didn't bother to do，反义邻居，块不同）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `made a point of reserving`，但块不在手边（自己标学下）　　目标：同她原句
找法：说"特意 X"时先落 made a point of，后面动词换 -ing。

**题面**
"我爸每次出差回来，都特意给我妈带一束花。"（"特意"用 **point** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Every time my dad comes back from a business trip, he makes a point of bringing my mom a bunch of flowers.

- 2026-11-01 ❌ 首犯 · 学习日 复检第 2 组 [5]（🎓#477 题里）· 她标「这个词组学下」· 原话 `He made a point of(这个词组学下) reserving a table with a river view for our first date, so that night just felt so special.`
- 2026-11-02 ✅ 学习日 在池第 1 组 [7] · `Whenever my dad returns from a business trip, he always makes a point of buying flowers for my mom.` —— makes a point of buying（of ＋ -ing）。连错 1 → 连对 1
- 2026-11-02 📝 题面整改 · 连对 ≥1 ⇒ 点名从整块 make a point of 降回 point（§6②；of ＋ -ing 留给她）
- 2026-11-03 ✅ 付息日 a 段在池第 1 组 [4] · `Whenever my grandmother makes dumplings, she always makes a point of making a bigger batch for us to take back.` —— makes a point of making（点名只给 point）。连对 1 → 2 ⇒ 🎓 毕业；同句 take back ⇒ 新建 #584

### 568 · **pitch a tent**（搭帐篷；也说 put up／set up a tent；⛔ build a tent）
类型 词组 ｜ 新建 2026-11-01 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-11-03 ｜ **🎓 已毕业 2026-11-03** ｜ 题型 整句

**问题是什么**
**pitch a tent** ＝ 搭帐篷（露营时最常用的那个动词）：`We pitched our tent by the lake.`
同一格里的邻居（别串）：put up／set up a tent（同义，更中性；屋里给孩子搭的小帐篷常说 set up）· take down a tent（拆帐篷）· 🎓#327 tent pegs（帐篷钉）。
判据一句话：说"搭帐篷" ⇒ pitch／put up／set up a tent；⛔ 不说 build a tent。
★ 题型判整句："搭帐篷"映射得回 pitch／put up／set up 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 pitch a tent，连对 ≥1 后降回 pitch。

**怎么发现的**
2026-11-01 学习日 复检第 3 组 [1]（🎓#186 题面"孩子们在客厅搭帐篷玩了一下午，把地上弄得一团糟就去睡觉了。"）· 原话
`The kids spent the whole afternoon pitching（这个动词学下) a play tent in the living room, and left the floor in a total mess when they went to sleep.`
她写对了 pitching a play tent，但自己标「这个动词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌；同 #566 #567 先例）。
判重三步：
　① 目标形式 dedup "pitch" ⇒ 零命中；"put up" ⇒ 零命中；"tent" ⇒ 🎓#174（as … as it gets，题面字样）· 🎓#327（tent pegs，历史字样，考 peg 不考"搭"）⇒ 都否
　② 中文 dedup "帐篷" ⇒ 🎓#174（同上）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `pitching a play tent`，但动词不在手边（自己标学下）　　目标：同她原句
找法：说到"搭帐篷"先落 pitch a tent。

**题面**
"我们到营地的时候天已经黑了，只能打着手电筒搭帐篷。"（"搭帐篷"用 **pitch** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：By the time we got to the campsite it was already dark, so we had to pitch our tent by flashlight.

- 2026-11-01 ❌ 首犯 · 学习日 复检第 3 组 [1]（🎓#186 题里）· 她标「这个动词学下」· 原话 `The kids spent the whole afternoon pitching（这个动词学下) a play tent in the living room, and left the floor in a total mess when they went to sleep.`
- 2026-11-02 ✅ 学习日 在池第 1 组 [8] · `By the time we got to the camp, night had fallen（这个短语可以学下), and we had no choice but to pitch our tent using flashlight.` —— pitch our tent。连错 1 → 连对 1；同句她标学下 ⇒ 新建 #571；using flashlight ⇒ ⚪ #56
- 2026-11-02 📝 题面整改 · 连对 ≥1 ⇒ 点名从整块 pitch a tent 降回 pitch（§6②）
- 2026-11-03 ✅ 付息日 a 段在池第 1 组 [5] · `We picked a flat patch of ground by the lake and got the tent pitched in thirty minutes.` —— got the tent pitched（点名只给 pitch）。连对 1 → 2 ⇒ 🎓 毕业

### 569 · **here in ＋ 地名**（here in Chengdu；⛔ here, Chengdu）
类型 搭配 ｜ 新建 2026-11-01
状态 连对2 连错0 上次2026-11-03 ｜ **🎓 已毕业 2026-11-03** ｜ 题型 整句

**问题是什么**
说"就在这儿（某城市／某国）" ⇒ **here in ＋ 地名**：`a stadium here in Chengdu` · `here in China` · `back home in Sichuan`。
同一格里的邻居（别串）：over there in ＋ 地名（那边在…：over there in Japan）· in Chengdu（不带 here，也对）。
判据一句话：here 后面要补出具体是哪儿 ⇒ 用 in 挂上；⛔ 逗号直接接地名（here, Chengdu）。
★ 题型判整句：考点是 here 和地名之间那个 in，要靠句子才现形；"我们这儿成都"不点 here 会落成 in Chengdu 绕开 ⇒ 整句 ＋ 正向点名 here。

**怎么发现的**
2026-11-01 学习日 ③ 重答 bank:340（R30 · P2 · Describe a live sports event you watched and liked）[S2] · 原话
`We watched it at a stadium here, Chengdu.`
here 后面丢了 in，逗号直接挂地名 ⇒ ❌（08-16 首答同一处写的是 here in chengdu，这次退步）。
判重三步：
　① 目标形式 dedup "here in" ⇒ 零命中
　② 中文 dedup "成都" ⇒ 🎓#312（search for，题面字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`at a stadium here, Chengdu`　　正确：`at a stadium here in Chengdu`
找法：说完 here 想补地名，先补 in。

**题面**
"我们这儿成都，冬天很少下雪。"（"我们这儿成都"用 **here** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Here in Chengdu, it hardly ever snows in winter.

- 2026-11-01 ❌ 首犯 · 学习日 ③ 重答 bank:340（R30 · P2）[S2] · 原话 `We watched it at a stadium here, Chengdu.`
- 2026-11-02 ✅ 学习日 在池第 1 组 [9] · `It hardly ever snows in the winter here in Chengdu.` —— here in Chengdu。连错 1 → 连对 1
- 2026-11-03 ✅ 付息日 a 段在池第 1 组 [6] · `Subways come every three minutes or so here in Shanghai.` —— here in Shanghai。连对 1 → 2 ⇒ 🎓 毕业

### 570 · **in total**（前前后后／加起来一共；⛔ back and forth ＝ 来来回回）
类型 词组 ｜ 新建 2026-11-02
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
"前前后后花了／一共花了 X" 说的是**总数** ⇒ X **in total**：`It cost us fifty grand in total.`（也说 a total of fifty grand）。
同一格里的邻居（别串）：altogether（同义，口语常用）· all told（同义，稍正式）· 🎓#23 back and forth（来来回回：走来走去、两边跑、反复讨论 `We went back and forth on it.` —— 那条考词序，意思不是"总共"）。
判据一句话：中文"前前后后／加起来／一共"后面跟一个数 ⇒ in total；"来来回回、反复"才是 back and forth。
★ 题型判整句："前前后后"孤立翻能落到 altogether／all told／in total 一串，词组题又不许给英文提示；考点是数字后面挂哪个块 ⇒ 整句 ＋ 正向点名 total（她犯错建的 ⇒ 给 lemma）。

**怎么发现的**
2026-11-02 学习日 在池第 1 组 [5]（#565 题面"他家这次重新装修厨房，前前后后花了差不多五万块。"）· 原话
`They spent nearly fifty grand back and forth just remodeling their kitchen.`
考点 fifty grand 用对（#565 ✅）；不在考点上的一处：前前后后 落成 back and forth —— 选词偏了（back and forth 是来回，不是总数），⛔ 不是同级近义词 ⇒ §3.2b 能学的表达 ⇒ 建号，判 ❌ 首犯。
判重三步：
　① 目标形式 dedup "back and forth" ⇒ 🎓#23（固定词序整块背，考的是 back and forth 的词序）· 🎓#64（forward or back ≠ back and forth，词序）· 🎓#522（字样）⇒ 都否，本条考"总数"怎么说；"in total" ⇒ 🎓#472（历史字样 paid out … in total，那条考 pay out）⇒ 否；"altogether"／"all told" ⇒ 零命中
　② 中文 dedup "前前后后" ⇒ 零命中；"一共" ⇒ 🎓#486 #88（字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`spent nearly fifty grand back and forth`　　正确：`spent nearly fifty grand in total`
找法：说到"前前后后"先问一句 —— 后面跟的是一个总数吗？是 ⇒ 数字 ＋ in total。

**题面**
"这趟旅行连机票带住宿，前前后后花了两万多。"（"前前后后"用 **total** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The whole trip, flights and hotels included, cost us over twenty thousand in total.

- 2026-11-02 ❌ 首犯 · 学习日 在池第 1 组 [5]（#565 题里）· 不在考点上的一处 · 原话 `They spent nearly fifty grand back and forth just remodeling their kitchen.`
- 2026-11-03 ✅ 付息日 a 段在池第 1 组 [7] · `Including flights and accommodation, the whole trip added up to over twenty grand in total.` —— in total。连错 1 → 连对 1

### 571 · **night falls**（天黑了：night had fallen · as night fell；⛔ the night fell）
类型 搭配 ｜ 新建 2026-11-02 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**night falls** ＝ 天黑下来（讲经过、讲故事时最常用，比 it got dark 更有画面感）：`By the time we got there, night had fallen.` · `As night fell, the temperature dropped.`
night 前面不带 the（⛔ the night fell）；名词说法 at nightfall（天黑时分）。
同一格里的邻居（别串）：it got dark（中性同义，也对）· darkness falls（同一个画面）· dusk（黄昏，天快黑那一段）。
判据一句话：叙述里"天黑了／天已经黑了" ⇒ night fell／night had fallen（或 it got dark）。
★ 题型判整句："天黑了"能落到 it got dark 绕开，词组题又不许给英文提示；块里 night 不带 the、fall 的时态要靠句子才现形 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 night falls，连对 ≥1 后降回 fall。

**怎么发现的**
2026-11-02 学习日 在池第 1 组 [8]（#568 题面"我们到营地的时候天已经黑了，只能打着手电筒搭帐篷。"）· 原话
`By the time we got to the camp, night had fallen（这个短语可以学下), and we had no choice but to pitch our tent using flashlight.`
她写对了 night had fallen，但自己标「这个短语可以学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌；同 #563 #566 #567 #568 先例）。同句 using flashlight ⇒ ⚪ #56。
判重三步：
　① 目标形式 dedup "night had fallen"／"night fell" ⇒ 零命中
　② 中文 dedup "天黑" ⇒ 零命中；"天已经黑" ⇒ #568（题面字样，那条考 pitch a tent）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `night had fallen`，但块不在手边（自己标学下）　　目标：同她原句
找法：说到"天黑了"先落 night fell；"到…的时候天已经黑了" ⇒ by the time …, night had fallen。

**题面**
"一到冬天，五点多天就黑了。"（"天就黑了"用 **fall** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：In winter, night falls at around five.

- 2026-11-02 ❌ 首犯 · 学习日 在池第 1 组 [8]（#568 题里）· 她标「这个短语可以学下」· 原话 `By the time we got to the camp, night had fallen（这个短语可以学下), and we had no choice but to pitch our tent using flashlight.`
- 2026-11-03 ✅ 付息日 a 段在池第 1 组 [8] · `In the winter time, night falls around five in the afternoon.` —— night falls。连错 1 → 连对 1
- 2026-11-03 📝 题面整改 · 连对 ≥1 ⇒ 点名从整块 night falls 降回 fall（§6②；night 不带 the 与时态留给她）

### 572 · **pull away**（往后一缩、躲开，不让人碰）
类型 词组 ｜ 新建 2026-11-02 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**pull away** ＝ （人／动物）身子往后一缩、躲开，不让对方碰到：`The cat pulled away when I tried to pet it.` · `She pulled away from his hug.`
同一格里的邻居（别串）：back away（往后退几步）· shy away from（因为害怕／不好意思而回避）· dodge（一下子闪开）· 车起步也叫 pull away（#563 11-01 原话 `stalled right when it pulled away`，另一个义项）。
判据一句话：被人伸手碰时身体往回缩 ⇒ pull away（from sb）。
★ 题型判整句："躲开"能落到 move away／back off／dodge 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 pull away，连对 ≥1 后降回 pull。

**怎么发现的**
2026-11-02 学习日 复检第 2 组 [4]（🎓#544 题面"宠物咖啡馆里那只柯基特别乖，谁去摸它都不躲。"）· 原话
`That Corgi at the pet cafe is so well-behaved that it won't pull away（这个学下） no matter who pets it.`
她写对了 pull away，但自己标「这个学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #563 #566 #567 #568 #571 先例）。
判重三步：
　① 目标形式 dedup "pull away" ⇒ #563（历史字样：车起步的 pulled away，另一个义项）⇒ 否
　② 中文 dedup "躲" ⇒ 🎓#46 #176 #495（字样）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `it won't pull away`，但块不在手边（自己标学下）　　目标：同她原句
找法：说到"一躲／往后一缩"先落 pull away。

**题面**
"我想抱一下邻居家的小孩，他害羞地往后一缩躲开了。"（"往后一缩躲开"用 **pull** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I tried to give the neighbor's kid a hug, but he shyly pulled away.

- 2026-11-02 ❌ 首犯 · 学习日 复检第 2 组 [4]（🎓#544 题里）· 她标「这个学下」· 原话 `That Corgi at the pet cafe is so well-behaved that it won't pull away（这个学下） no matter who pets it.`
- 2026-11-03 ✅ 付息日 a 段在池第 1 组 [9] · `When I tried to hug the kid next door, he got shy and pulled away from me.` —— pulled away from me。连错 1 → 连对 1
- 2026-11-03 📝 题面整改 · 连对 ≥1 ⇒ 点名从整块 pull away 降回 pull（§6②；away 留给她）

### 573 · **settle a score with sb**（找某人算账、报旧仇；对多个人 ⇒ settle scores with …）
类型 词组 ｜ 新建 2026-11-02 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**settle a score (with sb)** ＝ 找某人算账、把旧仇报了：`He came back to settle a score with the man who betrayed him.` · settle old scores（清算旧账）。
同一格里的邻居（别串）：get back at sb（报复某人，更口语）· get even with sb（扯平）· settle the bill（结账，真付钱）· 🎓#126 settle into（适应新环境，另一个块）。
判据一句话：因为过去的仇去找人"算账" ⇒ settle a score with sb；真的付钱结账 ⇒ settle the bill。
★ 题型判整句："找…算账"能落到 get back at／get revenge on 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 settle a score，连对 ≥1 后降回 score。

**怎么发现的**
2026-11-02 学习日 复检第 2 组 [5]f（🎓#498 题面"小说里那个专门私下找贪官算账的义警"）· 原话
`a vigilante in the book who settles scores with(学下这个短语） corrupt officials on the sly(学下这个短语）`
她写对了 settles scores with，但自己标「学下这个短语」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #572 先例；同句 on the sly 另建 #574）。
判重三步：
　① 目标形式 dedup "settle" ⇒ 🎓#126（settle into 适应新环境）· 🎓#308 #414（字样）⇒ 都否
　② 中文 dedup "算账" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `settles scores with corrupt officials`，但块不在手边（自己标学下）　　目标：同她原句
找法：说到"找…算账"先落 settle a score with。

**题面**
"他出狱以后第一件事就是去找当年出卖他的人算账。"（"算账"用 **score** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The first thing he did after getting out of prison was settle a score with the guy who'd sold him out.

- 2026-11-02 ❌ 首犯 · 学习日 复检第 2 组 [5]f（🎓#498 题里）· 她标「学下这个短语」· 原话 `a vigilante in the book who settles scores with(学下这个短语） corrupt officials on the sly(学下这个短语）`
- 2026-11-03 ✅ 付息日 a 段在池第 1 组 [10] · `Once he was released from prison, he went straight to find the person who betrayed him to settle a score.` —— to settle a score。连错 1 → 连对 1
- 2026-11-03 📝 题面整改 · 连对 ≥1 ⇒ 点名从整块 settle a score 降回 score（§6②；settle 与 with 留给她）

### 574 · **on the sly**（偷偷地、背着人）
类型 词组 ｜ 新建 2026-11-02 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**on the sly** ＝ 偷偷地、背着别人（不想让人知道），口语，常放句末：`She's been eating sweets on the sly.` · `He took the job on the sly.`
同一格里的邻居（别串）：secretly（中性）· behind sb's back（背着某人，常带"不地道"）· 🎓#527 in private（私下、关起门来，不一定是瞒着人）。
判据一句话：做的事不想被人发现 ⇒ on the sly；只是不在公共场合 ⇒ in private。
★ 题型判整句："偷偷"能落到 secretly／sneakily 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 on the sly，连对 ≥1 后降回 sly。

**怎么发现的**
2026-11-02 学习日 复检第 2 组 [5]f（🎓#498 题面"小说里那个专门私下找贪官算账的义警"）· 原话
`a vigilante in the book who settles scores with(学下这个短语） corrupt officials on the sly(学下这个短语）`
她写对了 on the sly，但自己标「学下这个短语」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同句 settle scores with 另建 #573）。
判重三步：
　① 目标形式 dedup "on the sly" ⇒ 零命中
　② 中文 dedup "偷偷" ⇒ 🎓#313 #481 #485（字样）⇒ 都否；"私下" ⇒ 🎓#527 in private（私下≠偷偷，块不同）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `on the sly`，但块不在手边（自己标学下）　　目标：同她原句
找法：说到"偷偷（瞒着人）做…"，句末补 on the sly。

**题面**
"我妹妹趁我妈不注意，偷偷吃了好几块巧克力。"（"偷偷"用 **sly** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My sister ate several pieces of chocolate on the sly while my mom wasn't looking.

- 2026-11-02 ❌ 首犯 · 学习日 复检第 2 组 [5]f（🎓#498 题里）· 她标「学下这个短语」· 原话 `a vigilante in the book who settles scores with(学下这个短语） corrupt officials on the sly(学下这个短语）`
- 2026-11-03 ✅ 付息日 a 段在池第 2 组 [1] · `My little sister ate several chocolates on the sly when my mom was looking the other way.` —— on the sly。连错 1 → 连对 1；同句她标学下 ⇒ 新建 #585
- 2026-11-03 📝 题面整改 · 连对 ≥1 ⇒ 点名从整块 on the sly 降回 sly（§6②）

### 575 · **prefer (that) sb do**（更希望某人做…：My mom preferred I stay home；也说 prefer sb to do）
类型 结构 ｜ 新建 2026-11-02 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**prefer (that) sb do sth** ＝ 更希望某人做…，人后面的动词用**原形**：`My mom preferred I rest at home.` · `I'd prefer you not tell anyone.`
同义结构：prefer sb to do sth（`I'd prefer you to stay.`）。
同一格里的邻居（别串）：would rather sb did（`My mom would rather I stayed home.` 口语更常见，后面用过去式）· want sb to do（最中性）。
判据一句话：prefer 后面跟"人 ＋ 动作" ⇒ 人后面接动词原形（或 to do）。
★ 题型判整句：考点是 prefer 后面挂人和动作的那个结构，要靠句子才现形 ⇒ 整句 ＋ 正向点名 prefer。

**怎么发现的**
2026-11-02 学习日 复检第 2 组 [6]（🎓#546 题面"我想周末出去玩，我妈想让我在家休息，最后我们找了个折中：周六出门，周日在家。"）· 原话
`I wanted a weekend outing, but my mom preferred I(prefer sb. do sth. 学下) rest at home, so we eventually found a middle ground …`
她写对了 preferred I rest，但自己标「prefer sb. do sth. 学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #572 先例）。
判重三步：
　① 目标形式 dedup "prefer" ⇒ 🎓#20 #347 #348 #353 #356（字样）⇒ 都否；"would rather" ⇒ 零命中
　② 中文 dedup "更希望"／"希望我" ⇒ 只命中本条自身 ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `my mom preferred I rest at home`，但结构不在手边（自己标学下）　　目标：同她原句
找法：说"（谁）更希望我…"先落 prefer (that) I ＋ 动词原形。

**题面**
"我爸更希望我毕业后回老家工作。"（"更希望我…"用 **prefer** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My dad would prefer (that) I go back to my hometown to work after graduation.／My dad would prefer me to go back …

- 2026-11-02 ❌ 首犯 · 学习日 复检第 2 组 [6]（🎓#546 题里）· 她标「prefer sb. do sth. 学下」· 原话 `I wanted a weekend outing, but my mom preferred I(prefer sb. do sth. 学下) rest at home, so we eventually found a middle ground where we went out on Saturday and chilled at home on Sunday.`
- 2026-11-03 ✅ 付息日 a 段在池第 2 组 [2] · `My dad would prefer that I head back to my hometown to work after I graduate.` —— would prefer that I head back（that ＋ 人 ＋ 原形）。连错 1 → 连对 1

### 576 · **savory crepe**（煎饼：a Chinese savory crepe／jianbing）
类型 词汇 ｜ 新建 2026-11-02 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**savory crepe** ＝ 咸口的薄饼；跟外国人说煎饼 ⇒ a Chinese savory crepe（或直接说 jianbing 再解释一句）。savory ＝ 咸口的（反义 sweet）。
同一格里的邻居（别串）：pancake（厚的、多半甜的松饼）· crepe（薄饼，甜咸都有）· flatbread（饼、烙饼）· #577 fried dough sticks（油条，同一桌早饭）。
判据一句话：薄薄一层、加鸡蛋酱料的咸口早饭 ⇒ savory crepe。
★ 题型判整句："煎饼"能落到 jianbing／pancake 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 savory crepe，连对 ≥1 后降回 crepe。
★ 与 #566 同组时注意：#566 种子题面里有"煎饼" ⇒ 两条同组出题时 #566 换别的小吃（防泄题）。

**怎么发现的**
2026-11-02 学习日 复检第 2 组 [9]（🎓#486 题面"我家楼下有四家早餐店：一家卖包子，另一家卖面条，第三家卖煎饼，最后一家只卖豆浆油条。"）· 原话
`… a third serves savory crepes(这两个单词分别背下), and the last one exclusively sells soy milk and churros.`
她写对了 savory crepes，但自己标「这两个单词分别背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（另一个单词 ⇒ #577）。
判重三步：
　① 目标形式 dedup "crepe" ⇒ 零命中
　② 中文 dedup "煎饼" ⇒ #566（题面字样，那条考 street vendor）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `savory crepes`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"煎饼"先落 a savory crepe。

**题面**
"我最喜欢的早餐是加两个鸡蛋的煎饼。"（"煎饼"用 **crepe** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My favorite breakfast is a savory crepe with two eggs.

- 2026-11-02 ❌ 首犯 · 学习日 复检第 2 组 [9]（🎓#486 题里）· 她标「这两个单词分别背下」· 原话 `Downstairs from my place, there are four breakfast shops: the first sells buns, another sells noodles, a third serves savory crepes(这两个单词分别背下), and the last one exclusively sells soy milk and churros.`
- 2026-11-03 ✅ 付息日 a 段在池第 2 组 [3] · `My favorite breakfast has to be a savory crepe with two eggs inside.` —— a savory crepe。连错 1 → 连对 1
- 2026-11-03 📝 题面整改 · 连对 ≥1 ⇒ 点名从整块 savory crepe 降回 crepe（§6②；savory 留给她）

### 577 · **fried dough sticks**（油条；⛔ 直接说 churros）
类型 词汇 ｜ 新建 2026-11-02 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
油条 ＝ **fried dough sticks**（或 youtiao 再解释一句）：`soy milk and fried dough sticks`（豆浆油条）。
同一格里的邻居（别串）：churros（西班牙／墨西哥那种裹糖、蘸巧克力吃的甜点 —— 解释时可以说 "it's like a Chinese churro"，但直接说 soy milk and churros 对方想的是甜点）· doughnut（甜甜圈）· #576 savory crepe（煎饼）。
判据一句话：说中国早餐里的油条 ⇒ fried dough sticks；churro 只拿来打比方。
★ 题型判整句："油条"能落到 youtiao／churros 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 fried dough stick，连对 ≥1 后降回 dough。

**怎么发现的**
2026-11-02 学习日 复检第 2 组 [9]（🎓#486 题面同 #576）· 原话
`… a third serves savory crepes(这两个单词分别背下), and the last one exclusively sells soy milk and churros.`
她标「这两个单词分别背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌；且 churros 本身选词偏了（调出来的是另一种食物，不是同级近义词，§3.2b）。
判重三步：
　① 目标形式 dedup "churro"／"dough" ⇒ 零命中
　② 中文 dedup "油条" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`soy milk and churros`　　更准确：`soy milk and fried dough sticks`
找法：说到"油条"先落 fried dough sticks；churro 只在打比方时用。

**题面**
"他把油条掰成小段泡在粥里吃。"（"油条"用 **dough** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：He breaks the fried dough sticks into little pieces and soaks them in his congee.

- 2026-11-02 ❌ 首犯 · 学习日 复检第 2 组 [9]（🎓#486 题里）· 她标「这两个单词分别背下」· 原话 `Downstairs from my place, there are four breakfast shops: the first sells buns, another sells noodles, a third serves savory crepes(这两个单词分别背下), and the last one exclusively sells soy milk and churros.`
- 2026-11-03 ✅ 付息日 a 段在池第 2 组 [4] · `He broke the fried dough stick into bitesized chunks to dip in his congee.` —— the fried dough stick。连错 1 → 连对 1
- 2026-11-03 📝 题面整改 · 连对 ≥1 ⇒ 点名从整块 fried dough stick 降回 dough（§6②）

### 578 · **handlebars**（自行车／摩托车的车把，常用复数）
类型 词汇 ｜ 新建 2026-11-02 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**handlebars** ＝ 自行车、摩托车的车把（左右一根横杆，一般说复数）：`grip the handlebars` · `let go of the handlebars`。
同一格里的邻居（别串）：handle（门把手、锅柄这类"把手"）· steering wheel（汽车方向盘）· 自行车别的零件：brakes（刹车）· pedals（脚蹬）。
判据一句话：自行车上手握的那根横杆 ⇒ handlebars；门、杯子、锅上的把手 ⇒ handle。
★ 题型判整句："车把"能落到 handle／the bar 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 handlebars（她说要背 ⇒ 首测给整词）。

**怎么发现的**
2026-11-02 学习日 复检第 3 组 [3]（🎓#492 题面"一只小鸟落在我的自行车把手上，好像一点也不怕人。"）· 原话
`A small bird landed and perched on my bike's handlebars(这个词背下), appearing totally unfazed(这个词学下) by people.`
她写对了 handlebars，但自己标「这个词背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #572–#577 先例；同句 unfazed 另建 #579）。
判重三步：
　① 目标形式 dedup "handlebar" ⇒ 零命中
　② 中文 dedup "把手" ⇒ 🎓#282（字样：take ownership）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `my bike's handlebars`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"车把"先落 the handlebars（带 s）。

**题面**
"他骑车下坡的时候两只手都松开了车把，吓得我直叫。"（"车把"用 **handlebars** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：He let go of the handlebars with both hands while riding downhill, and I screamed.

- 2026-11-02 ❌ 首犯 · 学习日 复检第 3 组 [3]（🎓#492 题里）· 她标「这个词背下」· 原话 `A small bird landed and perched on my bike's handlebars(这个词背下), appearing totally unfazed(这个词学下) by people.`
- 2026-11-03 ✅ 付息日 a 段在池第 2 组 [5] · `When he was riding down the hill, he took both hands off the handlebars and terrified me.` —— the handlebars。连错 1 → 连对 1

### 579 · **unfazed**（淡定、一点不慌、不受影响：be unfazed by sth）
类型 词汇 ｜ 新建 2026-11-02 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**unfazed** ＝ 遇到本该让人慌、怕、乱的事，一点不受影响：`He was totally unfazed by the criticism.` · `The cat seemed unfazed by the noise.`
搭配：be／seem／look unfazed (by sth)；fazed 本身多用在否定里：`It didn't faze him.`（没把他吓着）。
同一格里的邻居（别串）：calm（平静，中性）· not bothered（不在乎）· chill（口语，淡定）· rattled（慌了，反义）。
判据一句话：别人以为会慌、结果一点没受影响 ⇒ unfazed (by sth)。
★ 题型判整句："一点不怕／很淡定"能落到 calm／not scared 一串，词组题又不许给英文提示；by 挂什么要靠句子 ⇒ 整句 ＋ 正向点名 unfazed。

**怎么发现的**
2026-11-02 学习日 复检第 3 组 [3]（🎓#492 题面同 #578）· 原话
`A small bird landed and perched on my bike's handlebars(这个词背下), appearing totally unfazed(这个词学下) by people.`
她写对了 unfazed by，但自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同句 handlebars 另建 #578）。
判重三步：
　① 目标形式 dedup "unfazed"／"fazed" ⇒ 零命中
　② 中文 dedup "不怕人"／"淡定" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `totally unfazed by people`，但词不在手边（自己标学下）　　目标：同她原句
找法：说到"（面对某事）一点不怕、一点不慌"先落 unfazed by。

**题面**
"外面雷打得那么响，我家狗却一点都不怕，照样呼呼大睡。"（"一点都不怕"用 **unfazed** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The thunder was really loud, but my dog was totally unfazed and kept sleeping.

- 2026-11-02 ❌ 首犯 · 学习日 复检第 3 组 [3]（🎓#492 题里）· 她标「这个词学下」· 原话 `A small bird landed and perched on my bike's handlebars(这个词背下), appearing totally unfazed(这个词学下) by people.`
- 2026-11-03 ✅ 付息日 a 段在池第 2 组 [6] · `The thunder outside was crashing so loudly, but our dog stayed totally unfazed and just kept sleeping.` —— stayed totally unfazed。连错 1 → 连对 1；同句她标学下 ⇒ 新建 #586

### 580 · **clothesline**（晾衣绳）
类型 词汇 ｜ 新建 2026-11-02 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**clothesline** ＝ 晾衣服用的绳子（一个词）：`hang the laundry on the clothesline`。
同一格里的邻居（别串）：clothespin（晾衣夹，英式 clothes peg）· drying rack（落地晾衣架）· hanger（衣架，挂衣服的）· 🎓#327 peg（墙上的小木钉）。
判据一句话：两头拴住、把衣服搭上去晒的那根绳子 ⇒ clothesline。
★ 题型判整句："晾衣绳"能落到 washing line／a rope for drying clothes 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 clothesline（她说要背 ⇒ 首测给整词）。

**怎么发现的**
2026-11-02 学习日 复检第 3 组 [7]a（🎓#327 题面"晾衣绳两头钉在墙上的小木钉"）· 原话
`small wooden pegs fixed to the wall holding up the clothesline(背下)`
她写对了 clothesline，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #578 先例）。
判重三步：
　① 目标形式 dedup "clothesline" ⇒ 零命中
　② 中文 dedup "晾衣" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `the clothesline`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"晾衣绳"先落 clothesline。

**题面**
"趁着太阳好，我妈把被子搭在院子里的晾衣绳上晒。"（"晾衣绳"用 **clothesline** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Since it was sunny, my mom hung the quilt over the clothesline in the yard to air it out.

- 2026-11-02 ❌ 首犯 · 学习日 复检第 3 组 [7]a（🎓#327 题里）· 她标「背下」· 原话 `small wooden pegs fixed to the wall holding up the clothesline(背下)`
- 2026-11-03 ✅ 付息日 a 段在池第 2 组 [7] · `My mom put the quilt out on the clothesline in the courtyard to get some sun while it was nice outside.` —— on the clothesline。连错 1 → 连对 1；同句她标背下 ⇒ 新建 #587

### 581 · **grill**（烤：在烤架／炭火／铁板上直接烤 ⇒ grilled squid；⛔ 与 roast 串）
类型 词汇 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
"烤"按做法分三个词：
**grill** ＝ 放在烤架／炭火／铁板上直接对着火烤，多是串、片、块：`grilled squid` · `grilled chicken wings` · `grilled corn`。
roast ＝ 整只或一大块放进烤箱（或架在火上转着）慢慢烤：`roast chicken`（整只烤鸡）· `roast beef` · `roasted sweet potatoes` · `roasted peanuts／coffee beans`。
bake ＝ 面包、蛋糕、饼干这类面点：`bake a cake`。
同一格里的邻居（别串）：barbecue ＝ 户外烧烤这件事（have a barbecue），烤出来的东西也常说 grilled。
判据一句话：小块直接上火烤 ⇒ grill；整只大块进烤箱 ⇒ roast；面点 ⇒ bake。
★ 题型判整句："烤"孤立着翻 grill／roast／bake 都可能，要靠句子里烤的是什么才定 ⇒ 整句 ＋ 正向点名 grill。

**怎么发现的**
2026-11-03 付息日 a 段在池第 1 组 [3]（#566 题面"我在夜市的一个路边摊上买了一串烤鱿鱼。"）· 原话
`I grabbed a stick of grilled(和 roast 的区别是啥，可以学下) squid(背下) from a local vendor at the night market.`
她写对了 grilled，但自己问「和 roast 的区别是啥，可以学下」⇒ §2③ 她主动提出 ⇒ 建号，判 ❌（同 #571–#580 先例；同句 squid 另建 #582、a stick of 另建 #583）。
判重三步：
　① 目标形式 dedup "grill"／"roast"／"barbecue" ⇒ 零命中
　② 中文 dedup "烤" ⇒ 🎓#348（"好吃"挂在吃的东西上，字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `grilled squid`，但分不清 grill 和 roast（自己问）　　目标：同她原句
找法：说到"烤 X"先问一句 —— 是串／片放在火上烤，还是整只进烤箱？前者 grilled，后者 roast(ed)。

**题面**
"海边那家店的烤生蚝特别出名，每天都排长队。"（"烤"用 **grill** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：That place by the beach is famous for its grilled oysters — there's a long line every day.

- 2026-11-03 ❌ 首犯 · 付息日 a 段在池第 1 组 [3]（#566 题里）· 她问「和 roast 的区别是啥，可以学下」· 原话 `I grabbed a stick of grilled(和 roast 的区别是啥，可以学下) squid(背下) from a local vendor at the night market.`

### 582 · **squid**（鱿鱼；复数也是 squid）
类型 词汇 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**squid** ＝ 鱿鱼，单复数同形（some squid · two squid）；当食物吃时不可数：`grilled squid` · `dried squid`（鱿鱼干）。
同一格里的邻居（别串）：calamari（菜单上的炸鱿鱼圈）· octopus（章鱼）· cuttlefish（墨鱼）。
判据一句话：说鱿鱼 ⇒ squid，不加 s。
★ 题型判整句："鱿鱼"孤立翻能落到 squid／calamari，词组题又不许给英文提示；不加 s 要靠句子才现形 ⇒ 整句 ＋ 正向点名 squid（她说要背 ⇒ 首测给整词）。

**怎么发现的**
2026-11-03 付息日 a 段在池第 1 组 [3]（#566 题面同 #581）· 原话
`I grabbed a stick of grilled(和 roast 的区别是啥，可以学下) squid(背下) from a local vendor at the night market.`
她写对了 squid，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "squid" ⇒ 零命中
　② 中文 dedup "鱿鱼" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `grilled squid`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"鱿鱼"先落 squid（不加 s）。

**题面**
"海边的渔民把刚打上来的鱿鱼一排排挂起来晾干。"（"鱿鱼"用 **squid** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The fishermen by the sea hang the freshly caught squid up in rows to dry.

- 2026-11-03 ❌ 首犯 · 付息日 a 段在池第 1 组 [3]（#566 题里）· 她标「背下」· 原话 `I grabbed a stick of grilled(和 roast 的区别是啥，可以学下) squid(背下) from a local vendor at the night market.`

### 583 · **skewer**（一串：a skewer of grilled squid · lamb skewers；⛔ a stick of）
类型 词汇 ｜ 新建 2026-11-03
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**skewer** ＝ 穿食物的签子，也指"一串"烤的东西：`a skewer of grilled squid` · `lamb skewers`（羊肉串）· `chicken skewers`。
同一格里的邻居（别串）：on a stick（插在一根签子上的：corn on a stick）· a stick of ＋ 一根一条的东西（a stick of gum／butter）· kebab（中东式烤肉串）。
判据一句话：烤串的"一串" ⇒ a skewer of X ／ X skewers。
★ 题型判整句："一串"孤立翻能落到 a string of／a bunch of 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 skewer。

**怎么发现的**
2026-11-03 付息日 a 段在池第 1 组 [3]（#566 题面"我在夜市的一个路边摊上买了一串烤鱿鱼。"）· 原话
`I grabbed a stick of grilled squid from a local vendor at the night market.`
考点 from a local vendor 用对（#566 ✅）；不在考点上的一处：一串 落成 a stick of —— a stick of 配一根一条的东西，烤串说 skewer ⇒ §3.2b 能学的表达（搭不上，⛔ 不是同级近义词）⇒ 建号（同 #562 #570 先例：⚠️ 建号记 ❌ 首犯）。
判重三步：
　① 目标形式 dedup "skewer"／"on a stick" ⇒ 零命中
　② 中文 dedup "烤串" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`a stick of grilled squid`　　更地道：`a skewer of grilled squid`
找法：说到烤的"一串 X"先落 a skewer of X。

**题面**
"我们在烧烤摊上一口气点了二十串羊肉串。"（"串"用 **skewer** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：We ordered twenty lamb skewers at the barbecue stall in one go.

- 2026-11-03 ❌ 首犯 · 付息日 a 段在池第 1 组 [3]（#566 题里）· 不在考点上的一处 · 原话 `I grabbed a stick of grilled squid from a local vendor at the night market.` ⇒ 更好版 a skewer of grilled squid

### 584 · **take sth home**（带回家；⛔ take back ＝ 退回／收回）
类型 词组 ｜ 新建 2026-11-03
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
"带回（家）去" ＝ **take sth home**：`Take some dumplings home with you.` · `I took the leftovers home.`
同一格里的邻居（别串）：take sth back ＝ 把东西退回去／收回一句话（take it back to the store · I take that back）· bring sth home（从外面带回到说话人这边的家）。
判据一句话：东西要跟着你回家 ⇒ take sth home；还回去、收回 ⇒ take back。
★ 题型判整句："带回去"孤立翻 take back／take home 都像，要靠句子里"回哪儿"才定 ⇒ 整句 ＋ 正向点名 home。

**怎么发现的**
2026-11-03 付息日 a 段在池第 1 组 [4]（#567 题面"我奶奶每次包饺子都特意多包一些，让我们带回去吃。"）· 原话
`Whenever my grandmother makes dumplings, she always makes a point of making a bigger batch for us to take back.`
考点 makes a point of making 用对（#567 ✅）；不在考点上的一处：带回去 落成 take back —— take back 先读成"退回／收回"，意思偏了 ⇒ §3.2b 能学的表达（⛔ 不是同级近义词）⇒ 建号（⚠️ 建号记 ❌ 首犯）。
判重三步：
　① 目标形式 dedup "take home"／"take back" ⇒ 零命中
　② 中文 dedup "带回" ⇒ 🎓#558（a trip down memory lane，字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`a bigger batch for us to take back`　　更地道：`a bigger batch for us to take home`
找法：说"让我带回去（吃／用）"先落 take … home。

**题面**
"朋友聚会剩下的蛋糕，我分了一半带回家。"（"带回家"用 **home** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I took half of the leftover cake from the party home.

- 2026-11-03 ❌ 首犯 · 付息日 a 段在池第 1 组 [4]（#567 题里）· 不在考点上的一处 · 原话 `Whenever my grandmother makes dumplings, she always makes a point of making a bigger batch for us to take back.` ⇒ 更好版 for us to take home

### 585 · **look the other way**（看向别处；引申：睁一只眼闭一只眼、故意不管）
类型 词组 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**look the other way** 有两层：
字面 ＝ 眼睛看着别处（没在看这边）：`She snuck a cookie while her mom was looking the other way.`
引申 ＝ 明知有问题却故意装没看见、睁一只眼闭一只眼：`The police just looked the other way.`
同一格里的邻居（别串）：when sb isn't looking（趁某人不注意，最常用、最中性）· turn a blind eye (to sth)（故意视而不见，只有引申义）· #574 on the sly（偷偷地）。
判据一句话：趁人没看着 ⇒ when sb isn't looking／while sb is looking the other way；明知不管 ⇒ look the other way／turn a blind eye。
★ 题型判整句："假装没看见"能落到 pretend not to see／ignore 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 look the other way，连对 ≥1 后降回 way。

**怎么发现的**
2026-11-03 付息日 a 段在池第 2 组 [1]（#574 题面"我妹妹趁我妈不注意，偷偷吃了好几块巧克力。"）· 原话
`My little sister ate several chocolates on the sly when my mom was looking the other way.（不注意的这个说法可以学下)`
她写对了 looking the other way（字面义），但自己标「不注意的这个说法可以学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #571–#582 先例）。
判重三步：
　① 目标形式 dedup "look the other way"／"other way" ⇒ 零命中；"not looking" ⇒ 🎓#102（字样）⇒ 否
　② 中文 dedup "不注意" ⇒ #574（题面字样，那条考 on the sly）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `when my mom was looking the other way`，但块不在手边（自己标学下）　　目标：同她原句
找法：说"趁…不注意"先落 when … wasn't looking；想说得更有画面 ⇒ while … was looking the other way。

**题面**
"保安明知道有人插队，却假装没看见。"（"假装没看见"用 **look the other way** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The security guard knew people were cutting in line, but he just looked the other way.

- 2026-11-03 ❌ 首犯 · 付息日 a 段在池第 2 组 [1]（#574 题里）· 她标「不注意的这个说法可以学下」· 原话 `My little sister ate several chocolates on the sly when my mom was looking the other way.（不注意的这个说法可以学下)`

### 586 · **crash**（雷声轰隆：thunder crashed · a crash of thunder）
类型 词汇 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**crash** 说声音 ＝ 巨大的、轰的一声：`thunder crashed overhead`（头顶雷声轰隆）· `a crash of thunder`（一声炸雷）· `the waves crashed against the rocks` · `the plates came crashing down`。
同一格里的邻居（别串）：rumble（雷在远处闷闷地滚：thunder rumbled in the distance）· boom（低沉的轰一声）· crash 的另一个意思：撞车、电脑死机（the car crashed · my laptop crashed）。
判据一句话：近处、炸开的那种响 ⇒ crash；远处闷闷滚过来 ⇒ rumble。
★ 题型判整句："炸雷／雷声轰隆"能落到 loud thunder／thunderclap 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 crash。

**怎么发现的**
2026-11-03 付息日 a 段在池第 2 组 [6]（#579 题面"外面雷打得那么响，我家狗却一点都不怕，照样呼呼大睡。"）· 原话
`The thunder outside was crashing(这个词的用法学下) so loudly, but our dog stayed totally unfazed and just kept sleeping.`
她写对了 thunder was crashing，但自己标「这个词的用法学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "crash" ⇒ 零命中；"thunder" ⇒ 🎓#561（tremble，题面字样）· #579（unfazed，题面字样）⇒ 都否
　② 中文 dedup "雷" ⇒ #579（同上）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `The thunder outside was crashing`，但用法不在手边（自己标学下）　　目标：同她原句
找法：说"雷声轰隆／炸雷"先落 thunder crashed 或 a crash of thunder。

**题面**
"半夜一声炸雷，把全家人都惊醒了。"（"一声炸雷"用 **crash** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：A crash of thunder in the middle of the night woke up the whole family.

- 2026-11-03 ❌ 首犯 · 付息日 a 段在池第 2 组 [6]（#579 题里）· 她标「这个词的用法学下」· 原话 `The thunder outside was crashing(这个词的用法学下) so loudly, but our dog stayed totally unfazed and just kept sleeping.`

### 587 · **quilt**（被子）
类型 词汇 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**quilt** ＝ 被子（尤其是缝起来、有夹层的那种棉被）：`air out the quilt`（晒被子）。
同一格里的邻居（别串）：comforter（美式：厚被子）· duvet（英式：羽绒被、被芯）· blanket（毯子，薄的一层）· bedsheet（床单）· pillowcase（枕套）· #580 clothesline（晒被子搭的那根绳）。
判据一句话：家里盖的那床棉被 ⇒ quilt（美式也常说 comforter）；薄毯子 ⇒ blanket。
★ 题型判整句："被子"能落到 comforter／duvet／blanket 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 quilt（她说要背 ⇒ 首测给整词）。

**怎么发现的**
2026-11-03 付息日 a 段在池第 2 组 [7]（#580 题面"趁着太阳好，我妈把被子搭在院子里的晾衣绳上晒。"）· 原话
`My mom put the quilt(背下) out on the clothesline in the courtyard to get some sun while it was nice outside.`
她写对了 quilt，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "quilt"／"duvet" ⇒ 零命中；"comforter" ⇒ 🎓#526（down jacket 正文字样）⇒ 否
　② 中文 dedup "被子" ⇒ #580（题面字样，那条考 clothesline）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `the quilt`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"被子"先落 quilt。

**题面**
"天一冷，我就把厚被子从柜子里拿出来了。"（"被子"用 **quilt** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：As soon as it got cold, I took the thick quilt out of the closet.

- 2026-11-03 ❌ 首犯 · 付息日 a 段在池第 2 组 [7]（#580 题里）· 她标「背下」· 原话 `My mom put the quilt(背下) out on the clothesline in the courtyard to get some sun while it was nice outside.`

### 588 · **chime**（钟、门铃叮咚地响）
类型 词汇 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**chime** ＝ 钟、门铃发出悦耳的叮咚声：`the clock chimed midnight` · `the doorbell chimed`；名词 wind chimes（风铃）。
同一格里的邻居（别串）：ring（铃响，最中性）· strike（钟敲几点：the clock struck twelve）· buzz（手机、蜂鸣器嗡嗡响）。
判据一句话：好听的、叮咚一声的钟声铃声 ⇒ chime；一般的铃响 ⇒ ring。
★ 题型判整句："叮咚响"能落到 ring／go off 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 chime。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 3 组 [1]（🎓#548 题面"我外婆家客厅里还挂着一台老式摆钟，每到整点就当当响。"）· 原话
`There's still an old-fashioned pendulum clock hanging in my grandma's living room that chimes（ 这个词学下）on the hour（整点的说法学下).`
她写对了 chimes，但自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同句 on the hour 另建 #589）。
判重三步：
　① 目标形式 dedup "chime" ⇒ 零命中
　② 中文 dedup "整点" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `chimes`，但词不在手边（自己标学下）　　目标：同她原句
找法：说到"（钟／门铃）叮咚响"先落 chime。

**题面**
"门铃叮咚一响，我就知道外卖到了。"（"叮咚一响"用 **chime** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：As soon as the doorbell chimed, I knew my takeout was here.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 3 组 [1]（🎓#548 题里）· 她标「这个词学下」· 原话 `There's still an old-fashioned pendulum clock hanging in my grandma's living room that chimes（ 这个词学下）on the hour（整点的说法学下).`

### 589 · **on the hour**（每个整点）
类型 词组 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**on the hour** ＝ 在每个整点：`The bus leaves every hour on the hour.` · `The clock chimes on the hour.`
同一格里的邻居（别串）：on the dot／sharp（某一个点准时：at nine sharp）· every half hour（每半小时）。
判据一句话：说"每到整点" ⇒ on the hour；说"某一个点准时" ⇒ on the dot／sharp。
★ 题型判整句："每到整点"能落到 every hour／at the top of every hour 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 on the hour，连对 ≥1 后降回 hour。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 3 组 [1]（🎓#548 题面同 #588）· 原话
`… that chimes（ 这个词学下）on the hour（整点的说法学下).`
她写对了 on the hour，但自己标「整点的说法学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "on the hour" ⇒ 零命中
　② 中文 dedup "整点" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `on the hour`，但块不在手边（自己标学下）　　目标：同她原句
找法：说到"每到整点"先落 on the hour。

**题面**
"这趟机场大巴每到整点发一班车。"（"每到整点"用 **on the hour** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The airport bus leaves every hour on the hour.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 3 组 [1]（🎓#548 题里）· 她标「整点的说法学下」· 原话 `There's still an old-fashioned pendulum clock hanging in my grandma's living room that chimes（ 这个词学下）on the hour（整点的说法学下).`

### 590 · **bust**（口语：被警察抓、被逮到 ⇒ get busted）
类型 词汇 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**bust** ＝ 口语里的"抓、逮住"（警察抓人，或干坏事被人逮到），常用被动 get busted：`He got busted for drunk driving.` · `I got busted sneaking out.`
同一格里的邻居（别串）：get caught（被抓到，最中性）· get arrested（被正式逮捕）· catch sb red-handed（人赃并获）。
判据一句话：口语说"被抓了／被逮到" ⇒ get busted。
★ 题型判整句："被抓"能落到 get caught／arrested 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 bust。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 3 组 [2]b（🎓#551 题面"警匪片里最后被抓住的那个大反派"）· 原话
`the big villain who gets busted(学下) in the end of the action movie`
她写对了 gets busted，但自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同一处 in the end of 另建 #591）。
判重三步：
　① 目标形式 dedup "bust" ⇒ 零命中
　② 中文 dedup "被抓" ⇒ 只命中本条与 #591 自身 ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `gets busted`，但词不在手边（自己标学下）　　目标：同她原句
找法：说"被抓了个正着／被逮到"先落 got busted。

**题面**
"那个卖假货的店主上周被警察抓了个正着。"（"被抓了个正着"用 **bust** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The shop owner selling knockoffs got busted by the police last week.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 3 组 [2]b（🎓#551 题里）· 她标「学下」· 原话 `the big villain who gets busted(学下) in the end of the action movie`

### 591 · **at the end of ＋ 名词**（在…的结尾／尽头；⛔ in the end of）
类型 搭配 ｜ 新建 2026-11-03
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**at the end of ＋ 名词** ＝ 在某样东西的结尾、尽头：`at the end of the movie` · `at the end of the street` · `at the end of the day`。
in the end ＝ 最后、终于（后面不跟 of）：`In the end, we stayed home.`
同一格里的邻居（别串）：by the end of（到…结束时为止）· at the beginning of（在…开头）。
判据一句话：后面跟 of ＋ 名词 ⇒ at the end of；单独说"最后" ⇒ in the end。
★ 题型判整句：考点是 end 前面那个介词（at／in），要靠句子才现形 ⇒ 整句 ＋ 正向点名 end（介词留给她）。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 3 组 [2]b（🎓#551 题面"警匪片里最后被抓住的那个大反派"）· 原话
`the big villain who gets busted(学下) in the end of the action movie`
考点 villain 用对（#551 ✅）；不在考点上的一处：in the end of the action movie —— in the end 不接 of，"在…的结尾"是 at the end of ⇒ ❌ 首犯（介词搭配）。
判重三步：
　① 目标形式 dedup "at the end" ⇒ 🎓#355 #416 #440（历史字样）⇒ 都否；"in the end" ⇒ 零命中
　② 中文 dedup "尽头" ⇒ 只命中本条自身；"最后" ⇒ 🎓#298 #395 #338 #439 #486 #58 #88 #136 #248 #283 #286 #308（都是"最后"字样，没有一条考 at／in the end）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`in the end of the action movie`　　正确：`at the end of the action movie`
找法：说"在…的最后／尽头"先落 at the end of；只有 of 不出现时才用 in the end。

**题面**
"这条街的尽头有一家很小的面馆。"（"尽头"用 **end** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：There's a tiny noodle shop at the end of this street.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 3 组 [2]b（🎓#551 题里）· 不在考点上的一处 · 原话 `the big villain who gets busted in the end of the action movie`

### 592 · **back up**（下水道、水槽堵住、往回冒：the sewer backed up · the sink is backed up）
类型 词组 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**back up** ＝ 管道堵住、水往回冒：`The kitchen sink is backed up again.` · `The toilet backed up.`
同一格里的邻居（别串）：clogged（堵住了，同义：a clogged drain）· traffic backed up（车流排起长队）· back up a file（备份文件，另一个义项）· 🎓#543 bumper-to-bumper（车堵成长龙）。
判据一句话：管子、水槽、马桶堵了 ⇒ backed up／clogged。
★ 题型判整句："堵了"能落到 blocked／clogged 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 back up，连对 ≥1 后降回 back。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 3 组 [5]（🎓#553 题面"下水道堵了好几天，整条巷子都是一股熏人的味道。"）· 原话
`The sewer had been backed up(这个词组学下) for days, so there was a foul stench all over the alley.`
她写对了 had been backed up，但自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "backed up" ⇒ 🎓#543（bumper-to-bumper，历史字样）⇒ 否；"back up" ⇒ 🎓#316（log in，字样）⇒ 否
　② 中文 dedup "堵" ⇒ 🎓#107 #543 #61（都是堵车）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `The sewer had been backed up`，但块不在手边（自己标学下）　　目标：同她原句
找法：说"（水槽／下水道）堵了"先落 is backed up。

**题面**
"厨房水槽又堵了，水怎么都下不去。"（"堵了"用 **back up** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The kitchen sink is backed up again, and the water just won't drain.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 3 组 [5]（🎓#553 题里）· 她标「这个词组学下」· 原话 `The sewer had been backed up(这个词组学下) for days, so there was a foul stench all over the alley.`

### 593 · **hype up**（大肆宣传、吹得很神：be hyped up to be amazing）
类型 词组 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**hype (up)** ＝ 大肆宣传、吹得很神：`The movie was hyped up as the best of the year.` · `It's overhyped.`（被吹过头了）
同一格里的邻居（别串）：overrated（名不副实，被高估了）· 🎓#556 nothing to write home about（也就一般般）· get hyped（口语：特别兴奋）。
判据一句话：事先被宣传得很神 ⇒ hyped up／overhyped。
★ 题型判整句："被吹得很神"能落到 overrated／praised 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 hype。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 3 组 [7]（🎓#556 题面"那个景点被吹得神乎其神，去了一看也就一般般。"）· 原话
`The place was hyped up(这个词组学下) to be amazing, but once I saw it in person, it was nothing to write home about.`
她写对了 was hyped up，但自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "hype" ⇒ 零命中
　② 中文 dedup "吹" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `was hyped up to be amazing`，但块不在手边（自己标学下）　　目标：同她原句
找法：说"被吹得很神"先落 was hyped up。

**题面**
"这款新手机发布前被吹得特别厉害，结果用起来也就那样。"（"被吹得特别厉害"用 **hype** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The new phone was hyped up like crazy before the launch, but it's just okay to use.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 3 组 [7]（🎓#556 题里）· 她标「这个词组学下」· 原话 `The place was hyped up(这个词组学下) to be amazing, but once I saw it in person, it was nothing to write home about.`

### 594 · **bring up**（在聊天里提起某个话题）
类型 词组 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**bring up** ＝ （在谈话里）提起、说起某事：`Don't bring up his ex.` · `She brought up an interesting point.`
同一格里的邻居（别串）：mention（提到，中性）· bring up a child（把孩子带大，另一个义项）· 🎓#149（bring up 后面别多加 about）。
判据一句话：在聊天里把某个话题抛出来 ⇒ bring up sth。
★ 题型判整句："提"能落到 mention／talk about 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 bring up，连对 ≥1 后降回 bring。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 3 组 [9]（🎓#558 题面"高中同学聚会上大家聊起当年的糗事，一下子都回到了那段日子。"）· 原话
`Bringing up(这个词组学下) our old foolish moments at the class reunion was such a trip down memory lane.`
她写对了 Bringing up，但自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "bring up" ⇒ 🎓#149（动词后面别多加词，bring up 是列举之一，考的是别加 about）⇒ 否
　② 中文 dedup "提起" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `Bringing up our old foolish moments`，但块不在手边（自己标学下）　　目标：同她原句
找法：说"提起／说起（某事）"先落 bring up。

**题面**
"吃饭的时候别提他前女友的事，他会不高兴的。"（"提"用 **bring up** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Don't bring up his ex at dinner — he'll get upset.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 3 组 [9]（🎓#558 题里）· 她标「这个词组学下」· 原话 `Bringing up(这个词组学下) our old foolish moments at the class reunion was such a trip down memory lane.`

### 595 · **choke on**（呛着、噎着、卡住喉咙：choke on water／a fish bone）
类型 词组 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**choke on sth** ＝ 被某样东西呛着、噎着、卡住喉咙：`I choked on my coffee.` · `He choked on a fish bone.`
同一格里的邻居（别串）：swallow water（游泳时喝进水）· cough（咳嗽）· choke up（哽咽，另一个义项）。
判据一句话：东西进了气管、卡在喉咙 ⇒ choke on sth。
★ 题型判整句："呛着／卡住"能落到 get stuck in my throat 一串，词组题又不许给英文提示；on 挂什么要靠句子 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 choke on，连对 ≥1 后降回 choke。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 4 组 [6]（🎓#152 题面"我第一次学游泳的时候，呛了好几口水。"）· 原话
`The first time I learned how to swim, I choked on(学下这个词组） water a bunch of times.`
她写对了 choked on，但自己标「学下这个词组」⇒ §2③ 她说要学 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "choke" ⇒ 零命中
　② 中文 dedup "呛" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `I choked on water`，但块不在手边（自己标学下）　　目标：同她原句
找法：说"呛着／噎着／卡住喉咙"先落 choke on。

**题面**
"他吃鱼的时候不小心被鱼刺卡住了喉咙。"（"被…卡住"用 **choke on** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：He accidentally choked on a fish bone while eating fish.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 4 组 [6]（🎓#152 题里）· 她标「学下这个词组」· 原话 `The first time I learned how to swim, I choked on(学下这个词组） water a bunch of times.`

### 596 · **trailer**（电影预告片）
类型 词汇 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**trailer** ＝ 电影、剧集的预告片：`the official trailer` · `watch the trailer`。
同一格里的邻居（别串）：teaser（更短的先导预告）· preview（预告、试映）· trailer 另一个意思是拖车／房车（a trailer park）。
判据一句话：上映前放出来的那段宣传短片 ⇒ trailer。
★ 题型判整句："预告片"能落到 preview／teaser 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 trailer（她说要背 ⇒ 首测给整词）。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 4 组 [8]（🎓#363 题面"这部电影的预告片一直在打感情牌，就想让观众掉眼泪。"）· 原话
`That movie trailer（背下） constantly appeals to emotion, trying so hard to get people to cry.`
她写对了 trailer，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "trailer" ⇒ 零命中
　② 中文 dedup "预告片" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `That movie trailer`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"预告片"先落 trailer。

**题面**
"这部新片的预告片一出来，网上就炸了。"（"预告片"用 **trailer** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：As soon as the trailer for the new movie dropped, the internet went crazy.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 4 组 [8]（🎓#363 题里）· 她标「背下」· 原话 `That movie trailer（背下） constantly appeals to emotion, trying so hard to get people to cry.`

### 597 · **on a whim**（一时兴起、心血来潮）
类型 词组 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
**on a whim** ＝ 一时兴起、没怎么想就去做：`We booked the trip on a whim.` · `I bought it on a whim.`
同一格里的邻居（别串）：on the spur of the moment（一时冲动，同义）· spontaneously（说走就走，偏正式）· impulse buy（冲动消费）。
判据一句话：没计划、突然想做就做了 ⇒ on a whim。
★ 题型判整句："一时兴起"能落到 suddenly／spontaneously 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名；她说要学 ⇒ 首测给整块 on a whim，连对 ≥1 后降回 whim。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 4 组 [10]（🎓#368 题面"他在网上随手投了几份简历，没想到很快就在一家外企谋到了一个职位。"）· 原话
`After deliverying a few resumes online on a whim(这个词组学下), he unexpectedly landed a position at a multinational company.`
她写对了 on a whim，但自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同句 deliver 另建 #598）。
判重三步：
　① 目标形式 dedup "on a whim"／"whim" ⇒ 零命中
　② 中文 dedup "随手" ⇒ 🎓#407 #541 #560（题面字样）⇒ 都否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `on a whim`，但块不在手边（自己标学下）　　目标：同她原句
找法：说"一时兴起／随手就…"先落 on a whim。

**题面**
"我们一时兴起，周五下班直接买了去海边的车票。"（"一时兴起"用 **on a whim** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：On a whim, we bought train tickets to the beach right after work on Friday.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 4 组 [10]（🎓#368 题里）· 她标「这个词组学下」· 原话 `After deliverying a few resumes online on a whim(这个词组学下), he unexpectedly landed a position at a multinational company.`

### 598 · **send out résumés**（投简历；⛔ deliver）
类型 搭配 ｜ 新建 2026-11-03
状态 连对0 连错1 上次2026-11-03 未毕业 ｜ 题型 整句

**问题是什么**
投简历 ＝ **send out résumés**（一次投好几家）／ send in a résumé ／ apply for a job：`I sent out dozens of résumés.`
同一格里的邻居（别串）：deliver ＝ 把实物送到、递到（deliver a package）· 🎓#501 drop off（顺路送过去）· submit an application（提交申请，偏正式）。
判据一句话：网上、邮件投简历 ⇒ send out；deliver 只说把实物送到。
★ 题型判整句："投简历"能落到 apply／submit 一串，词组题又不许给英文提示；考点是动词选哪个 ⇒ 整句 ＋ 正向点名 send out。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 4 组 [10]（🎓#368 题面同 #597）· 原话
`After deliverying a few resumes online on a whim(这个词组学下), he unexpectedly landed a position at a multinational company.`
考点 landed a position 用对（#368 ✅）；不在考点上的一处：投简历 落成 deliver（deliverying 拼写不算，§2.1）—— 调出来的是另一个词（deliver 是送实物），⛔ 不是同级近义词 ⇒ §3.2b 选词 ⇒ 建号，判 ❌ 首犯。
判重三步：
　① 目标形式 dedup "send out" ⇒ 零命中；"resume" ⇒ 🎓#414（tweak，字样）⇒ 否；"deliver" ⇒ 🎓#501（drop off，送东西）⇒ 否
　② 中文 dedup "简历" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`After delivering a few resumes online`　　更地道：`After sending out a few résumés online`
找法：说"投简历"先落 send out résumés。

**题面**
"毕业前那个月，我每天都要投二三十份简历。"（"投简历"用 **send out** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The month before graduation, I was sending out twenty or thirty résumés a day.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 4 组 [10]（🎓#368 题里）· 不在考点上的一处 · 原话 `After deliverying a few resumes online on a whim, he unexpectedly landed a position at a multinational company.`

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

