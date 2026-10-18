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

### 251 · cost ＋ 钱／take ＋ 时间／spend ＋ 人做主语
类型 搭配 ｜ 旧号 B230
状态 连对0 连错1 上次2026-10-17 未毕业 ｜ 题型 整句 ｜ **回潮 2026-10-17**（08-17 毕业 → 10-17 重答 bank:834 钱配了 take）

**问题是什么**
**cost ＋ 钱 ／ take ＋ 时间 ／ spend ＋ 人做主语**：
`**it takes** two hours to cook a meal.`（时间 ⇒ take）｜ 钱 ⇒ cost ｜ 人当主语 ⇒ spend。
同一格里的邻居（别串）：⚠️ **cost 只配钱**这条边界还没固化（08-19 她在自由句里 takes／costs 两个都列了出来，
首选 takes 是对的 ⇒ 当时不记回潮，再出现一次按回潮处理）。
判据一句话：先看花的是**钱**还是**时间**、主语是**人**还是 it —— 三条路各走各的。

**怎么发现的**
旧 B 表迁移（B230，2026-08-18）；最早记录 2026-08-15 ❌，触发原话未存。
2026-08-16 ✅ ／ 2026-08-17 ✅ ⇒ 毕业。
2026-09-05 复检第 1 组 ✅ `it takes two hours to cook a meal.`——take ＋ 时间。

**我错在哪**
她的：2026-08-15 记过一次 ❌（触发原话未存）；08-19 自由句里写过 `it just takes/costs ten minutes`（两个都列，⛔ 不记回潮）。
找法：说"要花多少"先分一刀 —— 时间用 take、钱用 cost、人当主语用 spend。

**题面**
"这台二手相机花了我三千块，光研究怎么用就又花了我一整个周末。"
　　★ 零提示：钱 ⇒ cost me three thousand、时间 ⇒ took me a whole weekend（spend 以人做主语也对）；两个方向她都掉过（时间配 cost 的苗头 08-19、钱配 take 10-17 回潮）
　　★ 2026-10-17 改：旧种子"从我家开车到机场要一个多小时"只测时间那一半

- 2026-08-15 ❌
- 2026-08-16 ✅
- 2026-08-17 ✅
- 2026-09-05 ✅ 复检组 · 第 1 组 · `it takes two hours to cook a meal.` —— take ＋ 时间
- 2026-09-19 📝 题面整改：补（⛔ 不许用 need）· 复检组发题前审核（§6.5 第 7 项）
  `I need two hours to cook a meal.` 合法，绕开 take ＋ 时间 ⇒ 补排除项；spend 以人做主语在规则内
- 2026-09-19 ⚡ 自评免测 · 复检第 2 组
- 2026-09-19 ✅ 自发命中 · 付息日 d 段重答 R11（P3 · 自由产出）· `my family spends the whole day cooking`——spend 以人做主语
- 2026-09-19 ✅ 自发命中 · 付息日 d 段重答 R12（P3 · 自由产出）· `People spend hours in front of screens every day now.`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 零提示）
  去掉"⛔ need"，改零提示（It takes …／The drive is … 都算对），逼的是时间配 cost 这条她掉过的路；换成开车去机场场景
- 2026-10-17 ❌ 付息日 d 段重答 bank:834（R23 · P2 · 自由产出）S1 · `I'd like to tell you about my 3D printer, which took me about four thousand RMB.` ⇒ 钱配了 take ⇒ 最小改 which cost me about four thousand RMB ⇒ 🎓 回潮
- 2026-10-17 📝 题面整改：种子改成钱＋时间同句（这台二手相机花了我三千块，光研究怎么用就又花了我一整个周末）—— 今天回潮掉的是钱配 take，旧种子只测时间
- 备注 2026-08-19 她在自由句里写 `it just takes/costs ten minutes`（两个都列出来）——
  首选 takes 是对的，不记回潮；但 **cost 只配钱** 这条边界还没固化，再出现一次就按回潮处理

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

### 467 · charge 的主语是收钱的一方（the lot charges you）；事情本身花多少钱 ⇒ cost（parking costs you）
类型 搭配 ｜ 新建 2026-10-12
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 整句

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
找法二（10-16 补）：题面要用 charge、中文里却没出现收钱的一方 ⇒ 自己补一个：泛指的 **They charge you X to do Y**，或让车／店／停车场当主语（Cabs from the airport charge X to get downtown）。

**题面**
"在市中心停车，一小时就要二十块。"（"要二十块"用 **charge** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Parking lots downtown charge twenty yuan an hour.／They charge you twenty yuan an hour to park downtown.（⛔ Parking downtown charges …）

- 2026-10-12 ❌ 首犯 · 付息日 a2 段复检第 7 组 [1]（#288 题里）· diff-2 ⚠️ · 原话 `Once parking charges you twenty bucks an hour, you start asking whether taking the subway is a better deal.` ⇒ 更好版 parking costs you
- 2026-10-13 ❌ 学习日 在池第 2 组 [8] · `Parking in the city center charges twenty bucks an hour.` —— "停车"这件事当了 charge 的主语 ⇒ 最小改 `Parking lots in the city center charge twenty bucks an hour.`（或 Parking … costs …）。连错 1 → 2
- 2026-10-14 ✅ 学习日 在池第 2 组 [3] · `This shop charges two hundred bucks to repair a phone.` —— 收钱的店当 charge 的主语。连错 2 → 连对 1
- 2026-10-16 ❌ 学习日 在池第 1 组 [1] · 题面"从机场打车进市区，要一百五十块。"（点名 charge）· `Taking a cab from the airport to downtown costs a hundred and fifty bucks.`（她问"这不能用 charges 吧"）—— 那件事当主语换 costs 本身合法，但题面点名 charge、中文没给收钱的一方 ⇒ 没补出 they／cabs 当主语 ⇒ 最小改 `They charge you a hundred and fifty bucks to take a cab from the airport to downtown.`。连对 1 → 0，连错 0 → 1
- 2026-10-17 ✅ 付息日 在池第 1 组 [1] · `This barbershop charges eighty bucks for a haircut.`（收钱的一方当主语）。连错 1 → 连对 1

### 481 · **plan a surprise for sb**（给人准备惊喜；throw 只配"办一场活动"：throw sb a surprise party）
类型 搭配 ｜ 新建 2026-10-14
状态 连对1 连错0 上次2026-10-16 未毕业 ｜ 题型 整句

**问题是什么**
"给某人准备一个惊喜"＝ **plan a surprise for sb** ／ put together a little surprise for sb。
同一格里的邻居（别串）：throw ＋ 一场活动 ⇒ throw a party ／ throw sb a surprise party ／ throw a gala（🎓#416 她用对过）—— throw 后面要的是"派对／晚会"这种办出来的活动，不是"惊喜"本身 ·
surprise sb（动词：给人一个惊喜）· give sb a surprise 也能说，但没有 plan 那层"花心思准备"。
判据一句话：后面是派对／晚会 ⇒ throw；后面是惊喜本身 ⇒ plan／put together a surprise for sb。
★ 题型判整句："准备惊喜"能落到 surprise sb／give sb a surprise 一串合法说法，for ＋ 人 的挂法要靠句子现形 ⇒ 整句 ＋ 正向点名 plan。

**怎么发现的**
2026-10-14 学习日 在池第 3 组 [2]（#477 题面"生日那天朋友们给我准备了一个小惊喜，让这一天变得特别不一样。"）· 原话
`My friends threw me a little surprise on my birthday, and it really made the day feel special.`
feel special 本身对（#477 ✅），diff-2 ⚠️（不是 ❌）：throw 不配 surprise；plan a surprise 她没产出过（session 里零命中）⇒ §3.2b 能学的搭配 ⇒ 建号。
判重三步：
　① 目标形式 dedup "surprise" ⇒ 🎓#402 pull off（历史字串）· #477 feel special（今天这句的题面）⇒ 目标形式不同 ⇒ 否；dedup "throw"／"threw" ⇒ 🎓#394 throw a tantrum · 🎓#416 gala（10-08 她写 threw a grand gala，用对的）⇒ 否
　② 中文 dedup "惊喜" ⇒ 只命中 #477 题面 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`My friends threw me a little surprise`　　更地道：`My friends planned a little surprise for me`
找法：说"给人准备了个惊喜"先落 plan a surprise for ＋ 人；想用 throw ⇒ 后面得补 party。

**题面**
"我们几个偷偷给班主任准备了一个惊喜，庆祝她退休。"（"准备了一个惊喜"用 **plan** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：A few of us secretly planned a surprise for our homeroom teacher to celebrate her retirement.

- 2026-10-14 新建 · 学习日 在池第 3 组 [2]（#477 题里）· diff-2 ⚠️ · 原话 `My friends threw me a little surprise on my birthday, and it really made the day feel special.` ⇒ 更好版 planned a little surprise for me
- 2026-10-16 ✅ 学习日 在池第 2 组 [2] · `A few of us secretly planned a surprise for our homeroom teacher to celebrate her retirement.`。首测 ⇒ 连对 1

### 484 · **shipping**（物流、寄运：cross-border shipping · international shipping；⛔ express 单独当名词）
类型 词汇 ｜ 新建 2026-10-14
状态 连对1 连错0 上次2026-10-16 未毕业 ｜ 题型 词组

**问题是什么**
物流／寄运 ⇒ **shipping**（cross-border shipping · free shipping · shipping costs），偏行业的说法 logistics；快递 ⇒ **delivery**（express delivery）／ a courier。
同一格里的邻居（别串）：express 主要当形容词 —— express delivery（加急快递）· an express train · express lane；单独当名词说"快递／物流"是直译。
判据一句话：说东西怎么寄过去 ⇒ shipping；说送件这件事 ⇒ delivery；想说"加急"⇒ express ＋ 名词。
★ 题型判词组：中文块"国际物流的运费"映射回 shipping costs（logistics 合法照判）。

**怎么发现的**
2026-10-14 学习日 复检第 4 组 [2]（🎓#432 题面 ①"跨境物流"）· 原话
`cross-border express`
cross-border 本身对（#432 ✅），diff-2 ⚠️（不是 ❌）：express 单独当名词说"物流"是直译；shipping 她 lab 档案里没产出过 ⇒ §3.2b 能学的表达 ⇒ 建号。
判重三步：
　① 目标形式 dedup "express" ⇒ 🎓#236（字串）⇒ 否；"shipping"／"logistics" ⇒ 零命中
　② 中文 dedup "快递" ⇒ 🎓#375 a cardboard box（题面"快递纸箱"字样）⇒ 否；"物流" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`cross-border express`　　更地道：`cross-border shipping`
找法：想说"物流／快递"别落 express，先落 shipping 或 delivery。

**题面**
"国际物流的运费"（把包裹从国内寄到国外要付的那笔钱）

- 2026-10-14 新建 · 学习日 复检第 4 组 [2]（#432 题里）· diff-2 ⚠️ · 原话 `cross-border express` ⇒ 更好版 cross-border shipping
- 2026-10-16 ✅ 学习日 在池第 2 组 [3] · `international shipping fees`。首测 ⇒ 连对 1

### 486 · 一组里挨个说：**one … another … a third … the last one**（⛔ another 一路用到底）
类型 句型 ｜ 新建 2026-10-14
状态 连对1 连错0 上次2026-10-16 未毕业 ｜ 题型 整句

**问题是什么**
一组几个（三个、四个）挨个说各自干了什么 ⇒ **one … another … a third … and the last one …**。
another ＝"再一个"，第二个用它没问题；第三个起换序数 a third，最后一个用 the last one（或 the fourth），听的人才数得清还剩几个。
同一格里的邻居（别串）：只有两个 ⇒ one … the other … · 剩下的一群 ⇒ the others／the rest · 不知道一共几个 ⇒ some … others …。
判据一句话：知道一共几个 ⇒ 第三个起用序数、最后一个用 the last one；只有两个 ⇒ the other。
★ 题型判整句：列举顺序要靠一串并列分句才现形；正向点名 third，the last one 留给她。

**怎么发现的**
2026-10-14 学习日 ③ 重答 bank:450（P2 · Describe a story/book with animals in it）S5 · 原话
`one tries climbing up, but falls off halfway; another tries crashing into the tree, …; another tries to reach it with his trunk, but comes up short; and one even makes a kite to fly up there, only to drift further and further away.`
diff-2 ⚠️（不是 ❌）：第三只还用 another、第四只又回到 one，听的人数不清 ⇒ §3.2b 能学的句型 ⇒ 建号。
判重三步：
　① 目标形式 dedup "another" ⇒ 🎓#139（every／each／another 后面跟单数，形态）· 🎓#169 #291 #152 #408 #415（字串）⇒ 否；"a third" ⇒ 🎓#19 分数说法（a third ＝ 三分之一）—— 本条的 a third 是"第三个"，不是分数 ⇒ 否；"the last one" ⇒ 零命中
　② 中文 dedup "第三个"／"最后一个" ⇒ 未作判据，以英文形式为准
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`one … another … another … and one even …`　　更地道：`one … another … a third … and the last one even …`
找法：列举到第三个时停一下 —— 还要说 another 吗？换 a third；最后一个用 the last one。

**题面**
"我们宿舍四个人毕业后各奔东西：一个去了北京，另一个出了国，第三个回了老家，最后一个留在学校读研。"（"第三个"用 **third** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：After graduation, the four of us went our separate ways: one moved to Beijing, another went abroad, a third went back to his hometown, and the last one stayed on for a master's.

- 2026-10-14 新建 · 学习日 ③ 重答 bank:450 S5 · diff-2 ⚠️ · 原话 `one tries climbing up, …; another tries crashing into the tree, …; another tries to reach it with his trunk, …; and one even makes a kite to fly up there, …` ⇒ 更好版 a third … the last one
- 2026-10-16 ✅ 学习日 在池第 2 组 [4] · `… one went to Beijing, another went abroad, the third moved back home, and the last one stayed at school for grad school.` —— 第三个换了序数、最后一个用 the last one ⇒ 考点到位；diff-2 ⚠️ the third → a third（四个人没先后，"又一个"用 a third）。首测 ⇒ 连对 1

### 487 · 一群 X ＝ **a bunch of／a group of** X（⛔ a pack of mice —— pack 只配狼、狗）
类型 搭配 ｜ 新建 2026-10-14
状态 连对1 连错0 上次2026-10-16 未毕业 ｜ 题型 词组

**问题是什么**
说"一群老鼠／一群孩子／一群朋友"⇒ **a bunch of**（口语）／ **a group of**；pack 只配成群打猎的动物：a pack of wolves ／ a pack of dogs。
同一格里的邻居（别串）：a herd of elephants／cows（大型食草动物）· a flock of birds／sheep · a swarm of bees · a school of fish ·
pack 的另一个意思是"一包"：a pack of napkins（🎓#78）。
判据一句话：拿不准用哪个量词 ⇒ a bunch of／a group of 永远安全；pack ⇒ 只说狼、狗。
★ 题型判词组：中文块"一群小老鼠"映射回 a bunch／group of mice，考的就是量词那一格。

**怎么发现的**
2026-10-14 学习日 ③ 重答 bank:450（P2）S7 · 原话
`Instead, a pack of mice team up and help each other climb the tree, and they actually manage to get the mango.`
diff-2 ⚠️（不是 ❌）：pack 不配老鼠 ⇒ §3.2b 能学的搭配 ⇒ 建号。
判重三步：
　① 目标形式 dedup "pack" ⇒ 🎓#78 a pack of napkins（"一包"，量词块）—— 本条是"一群"，pack 不配老鼠 ⇒ 否；"bunch" ⇒ 🎓#370 #206（字串）⇒ 否
　② 中文 dedup "一群" ⇒ 🎓#286 #288（题面字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`a pack of mice`　　更地道：`a bunch of mice`／`a group of mice`
找法：说"一群 X"先落 a bunch of／a group of；想用 pack 先问是不是狼或狗。

**题面**
"一群在厨房里偷吃东西的小老鼠"（好几只聚成一伙的那种）

- 2026-10-14 新建 · 学习日 ③ 重答 bank:450 S7 · diff-2 ⚠️ · 原话 `Instead, a pack of mice team up and help each other climb the tree, …` ⇒ 更好版 a bunch of mice
- 2026-10-16 ✅ 学习日 在池第 2 组 [5] · `a group of tiny mice sneaking food in the kitchen`。首测 ⇒ 连对 1

### 488 · **there's strength in numbers**（团结就是力量、人多力量大；⛔ 直译 unity is strength）
类型 词组 ｜ 新建 2026-10-14
状态 连对1 连错0 上次2026-10-16 未毕业 ｜ 题型 整句

**问题是什么**
"团结就是力量／人多力量大"⇒ 口语 **there's strength in numbers**；说故事寓意也常说 teamwork pays off。
unity is strength 是口号式直译，日常口语不这么说。
同一格里的邻居（别串）：two heads are better than one（"三个臭皮匠"，一起想主意）· many hands make light work（人多干活轻松）· united we stand（口号，偏政治）。
判据一句话：人多一起上就更有力量 ⇒ there's strength in numbers；一起想办法 ⇒ two heads are better than one。
★ 题型判整句："人多力量大"能落到 teamwork／unity 一串说法 ⇒ 整句 ＋ 正向点名 numbers。

**怎么发现的**
2026-10-14 学习日 ③ 重答 bank:450（P2）S8 · 原话
`I really love this book, not so much because of the moral—like showing that unity is strength—but because …`
diff-2 ⚠️（不是 ❌）："团结就是力量"口号式直译；there's strength in numbers 她 lab 档案里没产出过 ⇒ §3.2b 能学的表达 ⇒ 建号。
判重三步：
　① 目标形式 dedup "strength" ⇒ 🎓#326 stamina（字串）⇒ 否；"numbers" 未单独作判据（太宽）
　② 中文 dedup "团结" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`like showing that unity is strength`　　更地道：`you know, that there's strength in numbers`
找法：想说"团结就是力量"先落 there's strength in numbers。

**题面**
"小区业主一起去找物业，问题很快就解决了 —— 人多力量大嘛。"（"人多力量大"用 **numbers** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The residents all went to the property management office together, and the problem got sorted out fast — there's strength in numbers.

- 2026-10-14 新建 · 学习日 ③ 重答 bank:450 S8 · diff-2 ⚠️ · 原话 `not so much because of the moral—like showing that unity is strength—but because …` ⇒ 更好版 you know, that there's strength in numbers
- 2026-10-16 ✅ 学习日 在池第 2 组 [6] · `The homeowners went to property management as a group, and the problem was fixed in no time—there's strength in numbers.`（in no time 她标学下 ⇒ 新建 #489）。首测 ⇒ 连对 1

### 489 · **in no time**（很快、没一会儿就…：the problem was fixed in no time；⛔ at no time ＝ 从来没有）
类型 词组 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**in no time** ＝ 没一会儿就、很快就（强调快得出乎意料），挂在句尾修饰整个动作：
`The problem was fixed in no time.` · `You'll pick it up in no time.` · `We got there in no time.`
同一格里的邻居（别串）：right away（马上、立刻 —— 强调"没耽搁、当下就开始"）· quickly（中性的"快"）·
⛔ at no time ＝ 从来没有、任何时候都不（At no time did he apologize.）—— 意思完全不同。
判据一句话：想说"一下子／没一会儿就搞定了" ⇒ 句尾挂 in no time；强调"马上开始" ⇒ right away。
★ 题型判整句："很快就"能落到 quickly／soon／right away 一串合法说法 ⇒ 整句 ＋ 正向点名 no time（in 留给她）。

**怎么发现的**
2026-10-16 学习日 在池第 2 组 [6]（#488 题面"小区业主一起去找物业，问题很快就解决了 —— 人多力量大嘛。"）· 原话
`The homeowners went to property management as a group, and the problem was fixed in no time(这个词组学下)—there's strength in numbers.`
她自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #472 #471 先例）。
判重三步：
　① 目标形式 dedup "in no time" ⇒ 零命中；"no time" ⇒ 🎓#377 not long after（"没多久之后"，说的是先后，不是快）—— 只是正文字串 ⇒ 否
　② 中文 dedup "很快就" ⇒ 只命中 #488（题面字样，考点是 strength in numbers）⇒ 否；"一会儿就" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（块不在手边）　　目标：`the problem was fixed in no time`
找法：说"很快就（办成了）"先问：强调的是"快得意外"⇒ 句尾挂 in no time；强调"马上开始"⇒ right away。

**题面**
"我把电脑送去修，师傅一会儿就弄好了。"（"一会儿就"用 **no time** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I took my laptop in for repair, and the guy fixed it in no time.

- 2026-10-16 ❌ 首犯 · 学习日 在池第 2 组 [6]（#488 题里）· 她标「这个词组学下」· 原话 `The homeowners went to property management as a group, and the problem was fixed in no time(这个词组学下)—there's strength in numbers.`
- 2026-10-17 ✅ 付息日 在池第 1 组 [6] · `… and the guy fixed it in no time.`。连错 1 → 连对 1

### 490 · **stay on**（留下来接着待：同一个学校／单位不走 —— stayed on for grad school）
类型 词组 ｜ 新建 2026-10-16
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**stay on** ＝ 本来可以走（毕业了／合同到了／实习完了），却留在原地接着待、接着干：
`She stayed on for grad school.` · `He stayed on at the company after the internship.` · `I'm staying on for another year.`
同一格里的邻居（别串）：stay at school（英式 ＝ 还在上学、没辍学）· stay in（待在家里不出门）· stay behind（别人走了你留下，偏一时）。
判据一句话：说"留下来（在原来那个学校／单位）继续…" ⇒ stay on；地方要点出来 ⇒ stay on at ＋ 地方。
★ 题型判整句："留下来"能落到 stay／remain 一串合法说法 ⇒ 整句 ＋ 正向点名 stay on。

**怎么发现的**
2026-10-16 学习日 在池第 2 组 [4]（#486 题面"…最后一个留在学校读研。"）· 原话
`The four of us in our dorm went our separate ways after graduating: one went to Beijing, another went abroad, the third moved back home, and the last one stayed at school for grad school.`
diff-2 ⚠️（不是 ❌）：stayed at school 听着像"还在上学"，后面又撞一个 grad school ⇒ stayed on for grad school；stay on 她 lab 档案里没产出过 ⇒ §3.2b 能学的表达 ⇒ 建号。
判重三步：
　① 目标形式 dedup "stay on" ⇒ 零命中；"stayed on" ⇒ 只命中 #486（目标形式字样，考点是 one … another … a third）⇒ 否
　② 中文 dedup "留在学校" ⇒ 只命中 #486（题面字样）⇒ 否；"留下来" ⇒ 零命中；"grad school" ⇒ 🎓#419 🎓#425（历史行字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`the last one stayed at school for grad school`　　更地道：`the last one stayed on for grad school`
找法：说"留校／留在公司"先问：是不是"本来该走、却没走、接着待"？是 ⇒ stay on。

**题面**
"实习结束以后，公司问她愿不愿意留下来，她就留了。"（"留下来"用 **stay on** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：After her internship ended, the company asked if she wanted to stay on, so she did.

- 2026-10-16 新建 · 学习日 在池第 2 组 [4]（#486 题里）· diff-2 ⚠️ · 原话 `… and the last one stayed at school for grad school.` ⇒ 更好版 stayed on for grad school
- 2026-10-17 ✅ 付息日 在池第 2 组 [9] · `… the company asked her if she wanted to stay on, and she said yes.`。首测 ⇒ 连对 1

### 491 · **snap**（细长的硬东西"咔"一下断成两截：the key snapped in the lock）
类型 词汇 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**snap** ＝ 细长、硬的东西（钥匙、树枝、铅笔、筷子、尺子）突然"咔"一声断成两截：
`The key snapped in the lock.` · `The branch snapped under his weight.` · `My pencil snapped in half.`
同一格里的邻居（别串）：break（中性、通用的"坏了／断了"）· crack（裂了一道缝、没断开）· tear／rip（布、纸撕破）。
判据一句话：硬东西一下子断成两截、还带声响 ⇒ snap；只是"坏了" ⇒ break。
★ 题型判整句："断了"能落到 break 一串合法说法 ⇒ 整句 ＋ 正向点名 snap。

**怎么发现的**
2026-10-16 学习日 复检第 3 组 [3]f（🎓#451 题面"钥匙断在锁里以后找来的开锁师傅"）· 原话
`a locksmith called in after the key snapped(背下) inside the lock`
她自己标「背下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 #471 先例）。
判重三步：
　① 目标形式 dedup "snap" ⇒ 🎓#400（历史行字串，考点是 come here just to）⇒ 否；"snapped" ⇒ 零命中
　② 中文 dedup "断在" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「背下」（词不在手边）　　目标：`the key snapped inside the lock`
找法：说"啪地断了／断成两截"先落 snap；要说断在哪 ⇒ snap in ＋ 地方，断成两半 ⇒ snap in half。

**题面**
"我一使劲，筷子就啪地断了。"（"啪地断了"用 **snap** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I pressed a bit too hard and the chopstick snapped.

- 2026-10-16 ❌ 首犯 · 学习日 复检第 3 组 [3]f（🎓#451 题里）· 她标「背下」· 原话 `a locksmith called in after the key snapped(背下) inside the lock`
- 2026-10-17 ✅ 付息日 在池第 1 组 [7] · `The moment I pressed too hard, the chopstick snapped in two.`。连错 1 → 连对 1

### 492 · **perch**（鸟停、落在高处或边沿上：perch on people's shoulders）
类型 词汇 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**perch** ＝ 鸟停在（枝头、肩上、栏杆、电线）上；人坐在高处或边沿上也能说：
`It loves perching on people's shoulders.` · `A crow was perched on the fence.` · `She perched on the edge of the bed.`
同一格里的邻居（别串）：land（飞下来落地那一下，动作）· sit（泛泛地坐／待着）· nest（做窝）。
判据一句话：鸟停在某个高处／细的东西上 ⇒ perch on；说"停着"的状态 ⇒ be perched on。
★ 题型判整句："停着"能落到 sit／stand 一串合法说法 ⇒ 整句 ＋ 正向点名 perch。

**怎么发现的**
2026-10-16 学习日 复检第 3 组 [5]（🎓#442 题面"我朋友家那只鹦鹉特别亲人，总爱站在人肩膀上。"）· 原话
`My friend's parrot is really affectionate; it loves perching(背下) on people's shoulders.`
她自己标「背下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 #471 先例）。
判重三步：
　① 目标形式 dedup "perch" ⇒ 零命中
　② 中文 dedup "肩膀" ⇒ 零命中；"站在" ⇒ 🎓#156 #164 #170 #241 #270（正文里"站在…"之类的字样，考点全不相干）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「背下」（词不在手边）　　目标：`it loves perching on people's shoulders`
找法：说"鸟停在…上"先落 perch，再补 on ＋ 地方。

**题面**
"窗外的电线上停着一排麻雀。"（"停着"用 **perch** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：There's a row of sparrows perched on the power line outside the window.

- 2026-10-16 ❌ 首犯 · 学习日 复检第 3 组 [5]（🎓#442 题里）· 她标「背下」· 原话 `My friend's parrot is really affectionate; it loves perching(背下) on people's shoulders.`
- 2026-10-17 ✅ 付息日 在池第 1 组 [8] · `There was a row of sparrows perching on the power line outside the window.`。连错 1 → 连对 1

### 493 · **citywide**（全市的、全城范围的：a citywide tournament）
类型 词汇 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 词组

**问题是什么**
**citywide** ＝ 整座城市范围的（形容词，放名词前）：`a citywide tournament` · `a citywide blackout` · `a citywide ban on fireworks`。
同一族：nationwide（全国的）· worldwide（全世界的）· statewide（全州的）—— 都是"范围 ＋ wide"一个词，放名词前；也能放句尾当副词（The rule applies citywide.）。
同一格里的邻居（别串）：across the city（介词短语，放名词后或句尾）。
判据一句话：想说"全市的／全城范围的 X" ⇒ a citywide X。
★ 题型判词组：一个固定的词，缺口只是调不调得出来；"全市范围的…"中文块能映射回 citywide（across the city 合法照判）。

**怎么发现的**
2026-10-16 学习日 复检第 4 组 [2]a（🎓#395 题面"全市中学生篮球大赛"）· 原话
`the citywide（学下) high school basketball tournament`
她自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #472 先例）。
判重三步：
　① 目标形式 dedup "citywide"／"city-wide" ⇒ 零命中
　② 中文 dedup "全市" ⇒ 🎓#18（历史行字样，考点是论元完整）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「学下」（词不在手边）　　目标：`the citywide high school basketball tournament`
找法：说"全市／全国／全世界范围的"先想"范围 ＋ wide"：citywide · nationwide · worldwide。

**题面**
"全市范围的垃圾分类新规定"（整座城市都要照着执行的那种）

- 2026-10-16 ❌ 首犯 · 学习日 复检第 4 组 [2]a（🎓#395 题里）· 她标「学下」· 原话 `the citywide（学下) high school basketball tournament`
- 2026-10-17 ✅ 付息日 在池第 1 组 [9] · `citywide waste sorting regulations`（漏了「新」只进 diff-1，不影响考点）。连错 1 → 连对 1

### 494 · **can't bring myself to do**（狠不下心、下不了手去做：I could never bring myself to throw them away）
类型 词组 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**can't／couldn't bring yourself to ＋ 动词原形** ＝ 心里过不去、怎么也下不了决心去做（多用否定）：
`I could never bring myself to throw them away.` · `She couldn't bring herself to tell him.` · `I can't bring myself to delete his number.`
★ to 后面是动词原形（bring myself to throw）—— 这里的 to 是不定式，⛔ 不接 -ing；反身代词跟着主语变（myself／herself／himself）。
同一格里的邻居（别串）：can't bear to（受不了去做）· have the heart to（忍心，也多用否定：I didn't have the heart to tell her）· be reluctant to（不太情愿，偏正式）。
判据一句话：想说"舍不得／狠不下心／下不了手去做" ⇒ can't bring myself to ＋ 动词。
★ 题型判整句：反身代词跟主语、to 后接原形，都要靠句子才现形 ⇒ 整句 ＋ 第一次把整块写进题面（她说要学 ⇒ 练）。

**怎么发现的**
2026-10-16 学习日 复检第 4 组 [6]（🎓#46 题面"这些旧照片都是我怎么也舍不得扔的东西。"）· 原话
`These old photos are things I could never bring myself to(这个词组学下) throw away.`
她自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #472 先例）。
判重三步：
　① 目标形式 dedup "bring myself"／"bring oneself"／"bring herself" ⇒ 零命中
　② 中文 dedup "狠不下心"／"舍不得" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（块不在手边）　　目标：`things I could never bring myself to throw away`
找法：说"怎么也舍不得扔／狠不下心说"先落 can't bring myself to，反身代词跟着主语变。

**题面**
"我爸的旧手机早就不能用了，可我妈就是狠不下心把它扔掉。"（"狠不下心"用 **bring herself to** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My dad's old phone stopped working ages ago, but my mom just can't bring herself to throw it away.

- 2026-10-16 ❌ 首犯 · 学习日 复检第 4 组 [6]（🎓#46 题里）· 她标「这个词组学下」· 原话 `These old photos are things I could never bring myself to(这个词组学下) throw away.`
- 2026-10-17 ✅ 付息日 在池第 1 组 [10] · `… but my mom just can't bring herself to throw it away.`。连错 1 → 连对 1

### 495 · **beat around the bush**（绕弯子、不直说正题：Stop beating around the bush）
类型 词组 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**beat around the bush** ＝ 说话绕来绕去、就是不说正题（故意回避或不好意思直说）：
`Stop beating around the bush and tell me what happened.` · `He beat around the bush for a while before he told the truth.`
同一格里的邻居（别串）：get to the point（说正题）· hem and haw（支支吾吾、吞吞吐吐，偏犹豫不决）· dodge the question（躲开问题）。
判据一句话：想说"绕弯子／拐弯抹角／不直说" ⇒ beat around the bush；"别绕了" ⇒ Stop beating around the bush。
★ 题型判整句："绕弯子"能落到 avoid the point 一串合法说法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-16 学习日 复检第 4 组 [10]（🎓#136 题面"我问他钱花哪儿了，他支支吾吾半天，最后才说了实话。"）· 原话
`I asked him where the money went, and he beat around the bush（这个词组学下) for a while before finally telling the truth.`
她自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #472 先例）。
判重三步：
　① 目标形式 dedup "beat around"／"bush"／"hem and haw" ⇒ 零命中
　② 中文 dedup "绕弯子"／"拐弯抹角"／"支支吾吾" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（块不在手边）　　目标：`he beat around the bush for a while`
找法：说"别绕弯子了"先落 Stop beating around the bush，后面接 and just …。

**题面**
"别绕弯子了，直接告诉我你到底想要什么。"（"绕弯子"用 **beat around the bush** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Stop beating around the bush and just tell me what you actually want.

- 2026-10-16 ❌ 首犯 · 学习日 复检第 4 组 [10]（🎓#136 题里）· 她标「这个词组学下」· 原话 `I asked him where the money went, and he beat around the bush（这个词组学下) for a while before finally telling the truth.`
- 2026-10-17 ✅ 付息日 在池第 2 组 [1] · `Stop beating around the bush and just tell me what you really want.`。连错 1 → 连对 1

### 496 · **be overrun with** ＋ 坏东西（到处都是、泛滥成灾：a city overrun with crime）
类型 词组 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**be overrun with X** ＝ 一个地方被 X 占满了、泛滥成灾（X 多是不想要的东西：老鼠、蟑螂、杂草、游客、犯罪）：
`a city overrun with crime` · `The old house is overrun with rats.` · `The beach gets overrun with tourists every summer.`
介词是 with；放名词后面当修饰（a city overrun with …），或者 be／get overrun with。
同一格里的邻居（别串）：be full of（中性的"满是"）· be packed with（挤满人，常是好事）· be infested with（虫、鼠成灾，更专指害虫）·
🎓#450 all over ＋ 地方（东西撒得满地都是，主语是东西）。
判据一句话：主语是被占满的地方、占满它的是坏东西 ⇒ overrun with；主语是撒出来的东西 ⇒ all over。
★ 题型判整句："到处都是"能落到 all over the place／full of 一串合法说法 ⇒ 整句 ＋ 正向点名 overrun。

**怎么发现的**
2026-10-16 学习日 ③ 重答 bank:1011（P2 · Describe a movie you watched and enjoyed recently）S5 · 原话
`The whole story takes place in Gotham, a fictional city overrun（学一下） with corruption and crime.`
搭配本身用对；她自己标「学一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #472 先例）。
判重三步：
　① 目标形式 dedup "overrun"／"overrun with"／"infested" ⇒ 零命中
　② 中文 dedup "到处都是" ⇒ 🎓#450 all over ＋ 地方（东西撒得满 X 都是，主语是东西）—— 本条主语是被占满的地方、块是 overrun with ⇒ 两个块，题面互斥（#450 ⛔ 不出"老鼠／害虫成灾"）；🎓#272 #441 #485 #314 只是题面／正文字样 ⇒ 否；"泛滥" ⇒ 🎓#440（正文字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「学一下」（块不在手边）　　目标：`a fictional city overrun with corruption and crime`
找法：说"满地都是老鼠／到处都是游客／犯罪泛滥"先落 overrun with，主语放被占满的地方。

**题面**
"那栋老房子空了好几年，现在到处都是老鼠。"（"到处都是"用 **overrun** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：That old house has been empty for years, and now it's overrun with rats.
★ 互斥：与 🎓#450 同组时，#450 题面 ⛔ 不出"老鼠／害虫成灾"。

- 2026-10-16 ❌ 首犯 · 学习日 ③ 重答 bank:1011 S5 · 她标「学一下」· 原话 `The whole story takes place in Gotham, a fictional city overrun（学一下） with corruption and crime.`
- 2026-10-17 ✅ 付息日 在池第 2 组 [2] · `… and now it's completely overrun with rats.`。连错 1 → 连对 1

### 497 · **have ＋ 东西 ＋ done** ＝ 遭遇（had my phone stolen）；人出事 ⇒ watched X get …
类型 结构 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**have ＋ 东西 ＋ 过去分词**，除了"叫人做"（I had my hair cut），还能表示"遭遇了某事"（倒霉、不是自己安排的）：
`I had my phone stolen on the subway.` · `We had our flight cancelled.` · `She had her bag snatched.`
★ 边界：宾语是人、动作是 killed／shot 时，听的人会先想到使役（"他找人干的"）⇒ 人出事别用 had X killed，
说 watched／saw X get killed（亲眼看着）或 lost X（失去）。
同一格里的邻居（别串）：get ＋ 东西 ＋ done（I got my phone stolen，口语也说）· 被动句（My phone was stolen —— 不点出"我"倒霉）。
判据一句话：想说"我被偷了／被取消了／被弄坏了 X" ⇒ I had my X stolen／cancelled／broken。
★ 题型判整句：结构靠句子才现形（have ＋ 宾语 ＋ 过去分词的位置）⇒ 整句 ＋ 正向点名 have。

**怎么发现的**
2026-10-16 学习日 ③ 重答 bank:1011 S6 · 原话
`Bruce Wayne, who becomes Batman, had(被动遭遇 have 的用法学下) his parents shot and killed when he was just a kid.`
她自己标「被动遭遇 have 的用法学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #472 先例）。
同句 diff-2 ⚠️：had his parents shot and killed 能读成使役 ⇒ 更好版 watched his parents get shot and killed（边界写进正文）。
判重三步：
　① 目标形式 dedup "had my"／"have sth done"／"stolen" ⇒ 零命中
　② 中文 dedup "被动遭遇" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「被动遭遇 have 的用法学下」；这次用在"父母被杀"上，能听成"他找人杀的"　　目标：`I had my phone stolen`（东西）／`watched his parents get shot`（人）
找法：说"我被 V 了 X"先落 I had my X ＋ 过去分词；X 是人、事情是被杀被伤 ⇒ 换 watched X get …。

**题面**
"我上个月在地铁上被偷了钱包。"（"被偷了"用 **have** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I had my wallet stolen on the subway last month.

- 2026-10-16 ❌ 首犯 · 学习日 ③ 重答 bank:1011 S6 · 她标「被动遭遇 have 的用法学下」· 原话 `Bruce Wayne, who becomes Batman, had(被动遭遇 have 的用法学下) his parents shot and killed when he was just a kid.` ⇒ 更好版 watched his parents get shot and killed
- 2026-10-17 ✅ 付息日 在池第 2 组 [3] · `I had my wallet stolen on the subway last month.`。连错 1 → 连对 1

### 498 · **vigilante**（不靠警察、私自出手惩治坏人的人；义警）
类型 词汇 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 词组

**问题是什么**
**vigilante** ＝ 没有执法身份、自己动手抓坏人／惩罚坏人的人（Batman 就是最典型的 vigilante）：
`become a vigilante` · `a masked vigilante` · `vigilante justice`（私刑式的"正义"）。
同一格里的邻居（别串）：hero（英雄，泛）· detective（侦探，查案）· bounty hunter（赏金猎人，拿钱抓人）。
判据一句话：不是警察、却自己出手惩治罪犯 ⇒ vigilante。
★ 题型判词组：一个固定的词，缺口只是调不调得出来；中文"私自替天行道的蒙面义警"能映射回 vigilante。

**怎么发现的**
2026-10-16 学习日 ③ 重答 bank:1011 S7 · 原话
`Later on, he decides to clean up the city, and his way of doing that is by becoming a vigilante(背一下), striking fear into the hearts of criminals.`
她自己标「背一下」⇒ §2③ 她说要背 ⇒ 建号，判 ❌（同 #471 先例）。
判重三步：
　① 目标形式 dedup "vigilante" ⇒ 零命中
　② 中文 "义警" ⇒ 未作判据（档案里没有这个中文块），以英文形式为准
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「背一下」（词不在手边）　　目标：`by becoming a vigilante`
找法：说"义警／私自替天行道的人"先落 vigilante。

**题面**
"电影里那种不靠警察、自己出手惩治坏人的蒙面义警"（没有执法身份、私自替天行道的那种人）

- 2026-10-16 ❌ 首犯 · 学习日 ③ 重答 bank:1011 S7 · 她标「背一下」· 原话 `… and his way of doing that is by becoming a vigilante(背一下), striking fear into the hearts of criminals.`
- 2026-10-17 ✅ 付息日 在池第 2 组 [4] · `a masked vigilante in the movie who takes justice into his own hands …`（in the movie → in the movies 只进 diff-2）。连错 1 → 连对 1

### 499 · **Take X —**（拿 X 来说：举一个真实的具体例子起手）
类型 句型 ｜ 新建 2026-10-16
状态 连对1 连错0 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
前面说完一个观点，要举一个具体的、真实的例子 ⇒ **Take X —**／**Take X, for example, …** 起手，后面接完整句：
`Take the Joker in the second movie—his performance was …` · `Take my nephew—he has tutoring until nine every night.`
同一格里的邻居（别串）：🎓#30 Say you …（假设一个情况举例："比方说你…"）· for example／for instance（中性）·
Even X …（"就连 X 都…"，后面直接接 X 的谓语：Even the Joker was more memorable than Batman.）。
判据一句话：举一个真实存在的人／东西当例子 ⇒ Take X —；假设一个情况 ⇒ Say you …。
★ 题型判整句：Take X 后面要接完整句才成立 ⇒ 整句 ＋ 正向点名 take。

**怎么发现的**
2026-10-16 学习日 ③ 重答 bank:1011 S10 · 原话
`Even the Joker in the second movie—his performance was honestly even more memorable and profound than Batman's.`
diff-2 ⚠️（不是 ❌）：Even 起头、破折号后另起主语 his performance，像中文"就连小丑，他的表演…"，前半句没搭上，和后面 even more 也撞了；这里是在举例 ⇒ Take the Joker —；Take X 她 lab 档案里没产出过 ⇒ §3.2b 能学的句型 ⇒ 建号。
判重三步：
　① 目标形式 dedup "Take my"／"Take X" ⇒ 🎓#189（take sb out）· 🎓#87（consider sth）只是字串 ⇒ 否；"for example" ⇒ 🎓#30 Say you …（假设举例，不是拿真实的人举例）⇒ 否，两条，题面互斥
　② "even" 相关 ⇒ 🎓#165（even though）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`Even the Joker in the second movie—his performance was …`　　更地道：`Take the Joker in the second movie—his performance was …`
找法：说"就拿…来说"先落 Take X，破折号后另起完整句；说"就连 X 都…"才用 Even X ＋ 谓语。

**题面**
"现在的孩子压力太大了。就拿我外甥来说，他每天补课补到晚上九点。"（"就拿…来说"用 **take** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Kids these days are under way too much pressure. Take my nephew—he has tutoring until nine every night.
★ 互斥：与 🎓#30 同组时，#30 题面 ⛔ 用真实的人举例（只出假设情况）。

- 2026-10-16 新建 · 学习日 ③ 重答 bank:1011 S10 · diff-2 ⚠️ · 原话 `Even the Joker in the second movie—his performance was honestly even more memorable and profound than Batman's.` ⇒ 更好版 Take the Joker in the second movie—
- 2026-10-17 ✅ 付息日 在池第 2 组 [10] · `Take my nephew, for instance—he has cram school every single night until nine.`。首测 ⇒ 连对 1（同句 cram school 她标要学 ⇒ 新建 #502）

### 500 · **a down payment**（首付：买房／买车时先付的那一笔）
类型 词汇 ｜ 新建 2026-10-17 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-17 未毕业 ｜ 题型 词组

**问题是什么**
**a down payment (on sth)** ＝ 首付，买房／买车时先一次付掉的那一部分，剩下的再贷款或分期：
`save up for a down payment` · `put down a down payment on a flat` · `cover the down payment`。
同一格里的邻居（别串）：deposit（英式也用来说买房首付 a deposit on a house；也是押金、定金）· mortgage（房贷，剩下借的那部分）· installment（分期付的每一期）。
判据一句话：先付的那一大笔、后面还要接着还 ⇒ down payment（英式也可 deposit）。
★ 题型判词组：一个固定名词块，缺口只是调不调得出来；中文"首付"能映射回 down payment。答 deposit 合法且贴题 ⇒ 照判 ✅。

**怎么发现的**
2026-10-17 付息日 a 在池第 1 组 [3]（#482 题里）· 原话
`What we've saved so far is far from enough to cover a down payment.(首付这个词需要学下)`
她自己标「首付这个词需要学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #471 #498 先例）。
判重三步：
　① 目标形式 dedup "down payment" ⇒ 零命中；邻居 dedup "deposit"／"mortgage" ⇒ 零命中
　② 中文 dedup "首付"／"按揭" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「需要学下」（词不在手边）　　目标：`cover a down payment`
找法：说"首付"先落 down payment；说"房贷"是 mortgage，别串。

**题面**
"买车时先交的那笔首付"（先付一大笔，剩下的再分期还的那种）

- 2026-10-17 ❌ 首犯 · 付息日 a 在池第 1 组 [3]（#482 题里）· 她标「首付这个词需要学下」· 原话 `What we've saved so far is far from enough to cover a down payment.(首付这个词需要学下)`

### 501 · **drop off ＋ 东西**（自己顺路送过去、放下就走；⛔ 和 send 串）
类型 词组 ｜ 新建 2026-10-17 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**drop off sth ／ drop sth off** ＝ 自己（多半是顺路）把东西或人带到某处、放下就走：
`drop off the kids at school` · `drop the keys off at my mom's` · `drop off a package at the front desk`。代词放中间：`drop it off`（⛔ drop off it）。
同一格里的邻居（别串）：send ＝ 让邮局／快递／别人送过去，自己不到场（send a parcel · send her flowers）· bring ＝ 带过来（朝说话人这边）· deliver ＝ 送货（多是职业行为）。
判据一句话：自己亲自跑一趟、放下就走 ⇒ drop off；东西过去了、人没去 ⇒ send。
★ 题型判整句：要靠句子才看得出"人去没去"、代词摆在哪儿。

**怎么发现的**
2026-10-17 付息日 a 在池第 2 组 [7]（🎓#478 题里）· 原话
`Every day after work, he makes a detour to the hospital to drop off(和send的区别学下) soup for his grandma in hospital—that's just his way of showing how much he cares.`
她问「和 send 的区别学下」⇒ §2③ 她主动提出 ⇒ 建号，判 ❌（同 #471 #498 #500 先例）。
判重三步：
　① 目标形式 dedup "drop off" ⇒ 零命中；邻居 dedup "send" ⇒ 🎓#263（双宾语语序：人在前东西在后）· 🎓#319（present sth to sb）⇒ 都是介词／语序框架规则，不是"亲自去 vs 寄过去"⇒ 否
　② 中文 dedup "送" ⇒ 命中的全是题面里的"送"字样（送礼、送货），没有一条讲"亲自送 vs 寄"⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 drop off，但不确定和 send 的分界　　目标：`drop off soup for his grandma`（他自己去）
找法：中文「送过去」先问 —— 我自己去吗？去 ⇒ drop off；不去 ⇒ send。

**题面**
"我下班顺路把备用钥匙放到我妈那儿就走了。"（"顺路放下"用 **drop off** 说）

- 2026-10-17 ❌ 首犯 · 付息日 a 在池第 2 组 [7]（#478 题里）· 她问「和 send 的区别学下」· 原话 `… he makes a detour to the hospital to drop off(和send的区别学下) soup for his grandma in hospital …`

### 502 · **cram school**（补习班：为了考试突击补课的校外班）
类型 词汇 ｜ 新建 2026-10-17 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-17 未毕业 ｜ 题型 词组

**问题是什么**
**cram school** ＝ 为了升学考试、放学后／周末去的补习班（亚洲语境最常用）：
`go to cram school` · `have cram school until nine` · `spend weekends at cram school`。动词 **cram** ＝ 考前临时突击：`cram for an exam`。
同一格里的邻居（别串）：tutoring ／ a tutor（一对一或小班辅导，中性）· extra classes（加课）· after-school classes（课后班，不一定是补习）。
判据一句话：为了考试、校外、密集填鸭 ⇒ cram school；一对一请老师 ⇒ tutoring。
★ 题型判词组：一个固定名词块，缺口只是调不调得出来；中文"为了考试突击的补习班"能映射回 cram school。

**怎么发现的**
2026-10-17 付息日 a 在池第 2 组 [10]（#499 题里）· 原话
`Kids are under so much pressure these days. Take my nephew, for instance—he has cram school(这个词组学下) every single night until nine.`
她自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #471 #498 #500 先例）。
判重三步：
　① 目标形式 dedup "cram school" ⇒ 零命中；"cram" ⇒ 只命中 🎓#403 正文字样（挤上车）⇒ 否
　② 中文 dedup "补课"／"tutoring" ⇒ 只命中本条触发题 #499 的题面 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「学下」（词组不在手边）　　目标：`he has cram school every night until nine`
找法：说"补习班／补课班"先落 cram school；说"请家教"是 a private tutor。

**题面**
"（为了中考突击的那种）周末补习班"（放学后、周末去的校外补课班）

- 2026-10-17 ❌ 首犯 · 付息日 a 在池第 2 组 [10]（#499 题里）· 她标「这个词组学下」· 原话 `… Take my nephew, for instance—he has cram school(这个词组学下) every single night until nine.`

### 503 · **over ＋ 名词**（为了／就因为一件事 —— 多是小事：argue over money）
类型 搭配 ｜ 新建 2026-10-17 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**over ＋ 名词** ＝ 为了（某件事）而争、而气、而折腾，常带"就为了这么点事"的口气：
`argue／fight over money` · `get upset over nothing` · `make a fuss over a small mistake` · `rewrite the whole thing over a missing comma`。
同一格里的邻居（别串）：even if ＋ 整句（就算…也…）· because of ＋ 名词（中性的原因）· about（argue about 也行，over 更口语、更带"就为了这个"）。
判据一句话：后面只是一个名词、说的是"为了这点事就…"⇒ over；后面是一整句假设 ⇒ even if。
★ 题型判整句：over 挂在哪个动作后面（argue／get upset／make sb redo）要靠句子现形。

**怎么发现的**
2026-10-17 付息日 a2 复检第 4 组 [1]（🎓#404 题里）· 原话
`My boss is overly strict about details—he'll make me rewrite a whole document just over（这个 over 的用法学下，我本来想写 even if 的) a missing comma.`
她自己标「这个 over 的用法学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #471 #498 #500 先例）。
判重三步：
　① 目标形式 dedup "argue over"／"fight over"／"over a" ⇒ 只命中 🎓#368（land a job，正文字样）⇒ 否
　② 中文 dedup "小事" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 over，但不确定这个用法（本来想写 even if）　　目标：`make me rewrite a whole document over a missing comma`
找法：中文「为了／就因为（一件小事）」先试 over ＋ 名词；要说"就算…"才用 even if ＋ 整句。

**题面**
"他俩为了谁洗碗吵了一晚上。"（"为了"用 **over** 说）

- 2026-10-17 ❌ 首犯 · 付息日 a2 复检第 4 组 [1]（#404 题里）· 她标「这个 over 的用法学下」· 原话 `… he'll make me rewrite a whole document just over（这个 over 的用法学下，我本来想写 even if 的) a missing comma.`

### 504 · **take up ＋ 时间／空间**（占掉）vs **It takes ＋ 时间**（需要多久）
类型 搭配 ｜ 新建 2026-10-17 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**It takes (sb) ＋ 时间 ＋ to do** ＝ 做这件事需要多久：`It took us two hours to get it in.`
**take up ＋ 时间／空间** ＝ 占掉一块（偏"挤占"）：`It takes up a lot of my time.` · `The sofa takes up too much space.`
同一格里的邻居（别串）：take up ＋ 爱好 ＝ 开始学（took up yoga，是"开始"那一下，不配一段时长）· spend ＋ 时间 ＋ doing（人当主语）·
🎓#251 cost ＋ 钱／take ＋ 时间／spend（管的是"钱还是时间"那一刀；本条管 take 还是 take up —— It takes ＋ 时间那一半两条共用，出题别同组撞）。
判据一句话：说"需要多久"⇒ take；说"占地方／占时间"⇒ take up。
★ 题型判整句：take 与 take up 的分工要靠句子才看得出（主语是事、宾语是时间还是空间）。

**怎么发现的**
2026-10-17 付息日 a2 复检第 4 组 [3]（🎓#176 题里）· 原话
`This method of learning words works wonders for me, even though it takes up (take up和 take 的区别) a lot of time.`
她问「take up 和 take 的区别」⇒ §2③ 她主动提出 ⇒ 建号，判 ❌（同 #501 先例）。
判重三步：
　① 目标形式 dedup "take up" ⇒ 只命中 🎓#206（书面词降级，正文字样）⇒ 否
　② 中文 dedup "占地方"／"占时间" ⇒ 未命中可比条目（以英文形式为准）
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 takes up，但分不清和 take 的区别　　目标：`it takes up a lot of time`（占掉）／ `it takes two hours`（需要）
找法：中文「占（地方／时间）」⇒ take up；「花了／要（多久）」⇒ It takes。

**题面**
"这个大沙发太占地方了，光搬进门就花了我们两个小时。"（"占地方"用 **take up** 说，"花了…小时"用 **take** 说）

- 2026-10-17 ❌ 首犯 · 付息日 a2 复检第 4 组 [3]（#176 题里）· 她问「take up 和 take 的区别」· 原话 `… even though it takes up (take up和 take 的区别) a lot of time.`

### 505 · **in a bit**（一会儿、马上）vs **in a while**（过一阵子／好久没）
类型 词组 ｜ 新建 2026-10-17 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-17 未毕业 ｜ 题型 整句

**问题是什么**
**in a bit** ＝ 一会儿、马上（几分钟内，口语）：`I'll call you back in a bit.` · `I'll be there in a bit.`
**in a while** ＝ 过一阵子（时间更长、更含糊）；否定句里 ＝ 好久没：`I haven't seen him in a while.`
同一格里的邻居（别串）：in a minute／in a sec（同 in a bit，更短）· for a while（持续了一阵子，说时长）· after a while（过了一会儿，讲过去的事）·
#489 in no time（没一会儿就搞定了 —— 强调快得意外、多挂在已完成的动作后；in a bit 是"过一会儿再做"，说的是将来）。
判据一句话：马上就会发生 ⇒ in a bit；隔了挺久、或"好久没"⇒ in a while。
★ 题型判整句：两个块的分工要靠句子里的时间关系（将来马上 vs 好久没）才现形。

**怎么发现的**
2026-10-17 付息日 a2 复检第 4 组 [8]（🎓#67 题里）· 原话
`I've finished washing all the winter clothes, so I'm going to put them away in a bit(in a bit / in a while 学下).`
她自己标「in a bit / in a while 学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #471 #498 #500 先例）。
判重三步：
　① 目标形式 dedup "in a bit"／"in a while" ⇒ 零命中
　② 中文 dedup "一会儿"／"好久没" ⇒ 未作判据（以英文形式为准）
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：用对了 in a bit，但不确定和 in a while 的分界　　目标：`put them away in a bit`
找法：中文「一会儿就」⇒ in a bit；「好久没」⇒ haven't … in a while。

**题面**
"我一会儿就到；说起来，我们好久没见了。"（"一会儿"用 **in a bit** 说，"好久没"用 **in a while** 说）

- 2026-10-17 ❌ 首犯 · 付息日 a2 复检第 4 组 [8]（#67 题里）· 她标「in a bit / in a while 学下」· 原话 `… so I'm going to put them away in a bit(in a bit / in a while 学下).`

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

