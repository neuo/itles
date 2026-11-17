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

### 675 · **alumni**（校友，复数；单数口语 an alum）
类型 词汇 ｜ 新建 2026-11-14 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**alumni** ＝ 校友（复数，最常用）：`Many alumni came back for the anniversary.`
单数 alumnus（男／泛指）· alumna（女），口语里单数常说 an alum；"老校友"直接说 alumni，不用加 old。
同一格里的邻居（别串）：classmate（同班同学）· schoolmate（同校同学，在校期间）。
判据一句话：从这个学校毕业的人 ⇒ alumni。
★ alumni 挂的是**学校**，⛔ 不挂人：alumni **of** my university ／ my university's alumni ／ fellow alumni（同校校友）· ⛔ my alumni（"我的校友"不能这么说）
　"他是我校友" ⇒ We went to the same university. ／ He's a fellow alum.（2026-11-15 第二次掉在这里补）
★ 题型判整句：同 🎓#641 等她点名背的单词先例，整句 ＋ 正向点名。

**怎么发现的**
2026-11-14 付息日 复检第 6 组 [8]（#416 题面"大学校庆那天晚上办了一场盛大的晚会，好多老校友都回来了。"）· 原话
`On the night of the university's anniversary, they threw a big gala, and tons of alumni（这个词背下） came back.`
她写对了 alumni，但自己标「这个词背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "alumn" ⇒ 全档零命中
　② 中文 dedup "校友" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `tons of alumni`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"校友" ⇒ alumni（一个人 ⇒ an alum）；说出口前看一眼 alumni 前面挂的是不是学校（of 学校），⛔ 别挂 my。

**题面**
"我们公司有好几个同事都是我的大学校友。"（"校友"用 **alumni** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Several of my coworkers are alumni of my university.

- 2026-11-14 ❌ 首犯 · 付息日 复检第 6 组 [8]（#416 题里）· 她标「这个词背下」· 原话 `they threw a big gala, and tons of alumni came back.`
- 2026-11-15 ❌ 学习日 在池第 3 组 [4] · `Quite a few coworkers at my company are my alumni from my university.` —— alumni 挂在人身上（my alumni）；校友是"某学校的"⇒ alumni of my university —— 连错 1 → 2
- 2026-11-16 ✅ 学习日 在池第 1 组 [10] · `Quite a few alumni from my school work in Silicon Valley now.` —— alumni from my school（挂学校，没挂人）。连错 2 → 连对 1

### 677 · **can't take it anymore**（实在受不了了、忍不下去了）
类型 词组 ｜ 新建 2026-11-15 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**can't take it anymore** ＝ 实在忍不下去了、撑不住了。it 是固定的，⛔ 不换成具体的事；过去时说 **couldn't take it anymore**。
`I couldn't take it anymore, so I quit.` · `The noise upstairs never stops—I can't take it anymore.`
同一格里的邻居（别串）：be sick of ＋ 事（受够了某件事，要接宾语，🎓#647）· can't stand ＋ 人／事（受不了某个具体对象）。
判据一句话：只说"我撑不住了"、不说受不了"什么" ⇒ can't take it anymore；要说出受不了的那件事 ⇒ sick of ／ can't stand ＋ 那件事。
★ 题型判整句：中文"受不了了"单拎出来有好几种合法说法（can't stand it／have had enough），非点名不可 ⇒ 不是词组题。

**怎么发现的**
2026-11-15 学习日 在池第 1 组 [4]（#655 题面"我在那家公司干了大半年，后来实在受不了就辞职了。"）· 原话
`I worked at that company for the better part of a year before I couldn't take it anymore（take it anymore 学下) and quit.`
她写对了 couldn't take it anymore，但自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #653 #676 先例）。
判重三步：
　① 目标形式 can't take it anymore；dedup "take it" ⇒ #584 take sth home · #49 #206 #282 #340 只是正文或历史里碰巧有 take it，考点无关 ⇒ 否；dedup "anymore" ⇒ #559 #646 只是例句里有 anymore ⇒ 否
　② 中文 dedup "受不了" ⇒ 🎓#647 be sick of（另一个词组，必须接宾语）· 🎓#494 can't bring myself to（狠不下心，意思不同）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `couldn't take it anymore`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"实在受不了了／忍不下去了"后面没有宾语 ⇒ 先调 can't take it anymore，过去的事换 couldn't。

**题面**
"这份工作天天加班到半夜，我实在受不了了。"（"实在受不了了"用 **can't take it anymore** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：This job has me working till midnight every day—I can't take it anymore.
★ 首次出题给整块（§6② 她点名要学 ⇒ 练），连对 ≥1 之后降回 take 点名。

- 2026-11-15 ❌ 首犯 · 学习日 在池第 1 组 [4]（#655 题里）· 她标「take it anymore 学下」· 原话 `I worked at that company for the better part of a year before I couldn't take it anymore and quit.`
- 2026-11-16 ✅ 学习日 在池第 2 组 [2] · `This job has me working overtime until midnight every single day—I just can't take it anymore.` —— can't take it anymore。连错 1 → 连对 1

### 678 · **ask sb what they think**（问…的意见／问…怎么看；⛔ ask for advice ＝ 请教该怎么办）
类型 句型 ｜ 新建 2026-11-15
状态 连对1 连错0 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
中文"问某人的意见／问问他怎么看" ⇒ **ask sb what they think**：中文的名词"意见"在英语里变成一个小从句 what … think。
`My dad never asks my mom what she thinks.` · `I asked my team what they thought about the plan.`
· think 跟着从句主语走：what she thinks ／ what we think ／ what they thought
同一格里的邻居（别串）：ask sb for advice ＝ 遇到事去请教"我该怎么办"（讨主意）· ask (for) sb's opinion 也对，但口语里 what they think 最常用。
判据一句话：问的是"你怎么看" ⇒ ask sb what they think；问的是"我该怎么办" ⇒ ask sb for advice。
★ 题型判整句：考点是从句挂在 ask sb 后面、think 跟主语变形，单翻一个块测不到。

**怎么发现的**
2026-11-15 学习日 在池第 1 组 [7]（#658 题面"老板从来不问我们这些新员工的意见。"）· 原话
`The boss never asks us new employees for our advice.`
#658 考点（us new employees）✅；"意见"在这里是"看法"，她说成 advice（请教怎么办）⇒ 意思偏了 ⇒ ⚠️，更地道的说法 ask sb what they think 是能学的句型 ⇒ §3.2b 建号。
判重三步：
　① 目标形式 ask sb what they think；dedup "what we think／what you think／what they think／what I think" ⇒ 全档零命中
　② dedup "advice" ⇒ 🎓#261（不可数名词规则）· 🎓#270（advice 的量词）· 🎓#304 turn to sb for sth（有事求助）⇒ 规则或词组都不同 ⇒ 否；dedup "opinion／input" ⇒ 零命中
　③ 中文 dedup "意见" ⇒ 🎓#275 whether 后接主谓（正文碰巧有"意见"二字）⇒ 否；"征求" ⇒ 零命中 ⇒ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：never asks us new employees for our advice　　更地道：never asks us new employees **what we think**
找法：说到"问…的意见"，先想人家要的是看法还是主意 —— 看法 ⇒ what … think。

**题面**
"我爸买车之前，一次都没问过我妈的意见。"（"问…的意见"用 **think** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Before buying the car, my dad never once asked my mom what she thought.

- 2026-11-15 新建 · 学习日 在池第 1 组 [7]（#658 题里）· 原话 `The boss never asks us new employees for our advice.`
- 2026-11-16 ✅ 学习日 在池第 2 组 [8] · `Before my dad bought the car, he didn't ask what my mom thought even once.` —— ask what my mom thought（省了被问的人，合法）；更好版 he never once asked my mom what she thought。首测 ⇒ 连对 1

### 679 · **recite**（背诵、当众背出来：recite a poem · recite a text）
类型 词汇 ｜ 新建 2026-11-15 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**recite** ＋ 课文／诗 ＝ 把背熟的东西当众、一字一字背出来：`recite a poem` · `recite a text in front of the class`。
同一格里的邻居（别串）：memorize ＝ 背下来（记进脑子的那个过程）· learn sth by heart ＝ 背熟。
判据一句话：说"背给别人听／背出来" ⇒ recite；说"把它背下来、记住" ⇒ memorize。
★ 题型判整句：同 🎓#641 等她点名背的单词先例，整句 ＋ 正向点名。

**怎么发现的**
2026-11-15 学习日 在池第 2 组 [2]（#663 题面"小时候每次被老师叫到讲台上背课文，我都紧张得要命。"）· 原话
`When I was a kid, every time the teacher called me up to the front to recite（这个词背下) a text, I got super nervous.`
她写对了 recite，但自己标「这个词背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #675 先例）。
判重三步：
　① 目标形式 dedup "recite" ⇒ 全档零命中；dedup "memorize" 的邻居关系另记，不是本条目标形式
　② 中文 dedup "背课文" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `to recite a text`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"背课文／背诗"是背给人听的那种 ⇒ recite。

**题面**
"我侄子才五岁，已经能把整首唐诗背出来了。"（"背出来"用 **recite** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My nephew is only five, and he can already recite a whole Tang poem.

- 2026-11-15 ❌ 首犯 · 学习日 在池第 2 组 [2]（#663 题里）· 她标「这个词背下」· 原话 `every time the teacher called me up to the front to recite a text, I got super nervous.`
- 2026-11-16 ✅ 学习日 在池第 2 组 [3] · `My nephew is only five, and he can already recite a whole Tang poem by heart.` —— recite a whole Tang poem。连错 1 → 连对 1

### 680 · **bridesmaid**（伴娘；伴娘之一 ⇒ one of the bridesmaids）
类型 词汇 ｜ 新建 2026-11-15 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**bridesmaid** ＝ 伴娘（bride ＋ maid）；美式婚礼伴娘常有好几个 ⇒ `I was one of her bridesmaids.`；主伴娘 ＝ the maid of honor。
同一格里的邻居（别串）：groomsman ＝ 伴郎 · best man ＝ 首席伴郎。
判据一句话：婚礼上陪着新娘的女生 ⇒ bridesmaid。
★ 题型判整句：同 🎓#641 等她点名背的单词先例，整句 ＋ 正向点名。

**怎么发现的**
2026-11-15 学习日 在池第 2 组 [3]（#664 题面"我闺蜜结婚的时候，我给她当了伴娘。"）· 原话
`When my bestie got married, I was one of her bridesmaids(背下).`
她写对了 bridesmaids，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #675 先例）。
判重三步：
　① 目标形式 dedup "bridesmaid" ⇒ 全档零命中
　② 中文 dedup "伴娘" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `one of her bridesmaids`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"伴娘" ⇒ bride ＋ maid。

**题面**
"我表姐下个月结婚，叫我去给她当伴娘。"（"伴娘"用 **bridesmaid** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My cousin is getting married next month, and she asked me to be one of her bridesmaids.

- 2026-11-15 ❌ 首犯 · 学习日 在池第 2 组 [3]（#664 题里）· 她标「背下」· 原话 `When my bestie got married, I was one of her bridesmaids.`
- 2026-11-16 ✅ 学习日 在池第 2 组 [4] · `My cousin is getting married next month, and she asked me to be one of her bridesmaids.` —— one of her bridesmaids。连错 1 → 连对 1

### 681 · **time off**（休假、请的假：take time off · approve sb's time off；不可数，不加 a）
类型 词组 ｜ 新建 2026-11-15 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**time off** ＝ 不上班的那段时间（不可数，前面不加 a）：`take some time off` · `I haven't had any time off in months.` · `The boss didn't approve his time off.`
同一格里的邻居（别串）：a day off ＝ 一天假（可数，带数字：take two days off）· leave ＝ 正式的假（sick leave · maternity leave）· vacation ＝ 出去度假的长假。
判据一句话：笼统说"休假／请假"、不带天数 ⇒ time off；带天数 ⇒ X days off。
★ 题型判整句：同 🎓#641 等她点名学的词先例，整句 ＋ 正向点名。

**怎么发现的**
2026-11-15 学习日 复检第 4 组 [3]（#622 题面"我同事到现在还在生老板的气，因为老板没批他的假。"）· 原话
`My coworker is still mad at the boss because he didn't approve his time off（time off 学下).`
她写对了 time off，但自己标「time off 学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #675 #679 先例）。
判重三步：
　① 目标形式 dedup "time off" ⇒ 全档零命中；邻居 "day off" ⇒ 零命中
　② 中文 dedup "请假"／"批假" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `approve his time off`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"请假／休假／批假" ⇒ 先落 time off。

**题面**
"我已经好几个月没休过假了，下个月一定要请几天出去玩。"（"休假"用 **time off** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I haven't had any time off in months—I'm definitely taking a few days off next month to go somewhere.

- 2026-11-15 ❌ 首犯 · 学习日 复检第 4 组 [3]（#622 题里）· 她标「time off 学下」· 原话 `My coworker is still mad at the boss because he didn't approve his time off.`
- 2026-11-16 ✅ 学习日 在池第 2 组 [5] · `I haven't taken any time off in months, so next month I'm definitely taking a few days off to go on a trip.` —— taken any time off · taking a few days off。连错 1 → 连对 1

### 682 · **nail ＋ 事情**（口语：做得很到位、拿下：nail the interview · nailed it）
类型 词汇 ｜ 新建 2026-11-15 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**nail** ＋ 事情 ＝ 把一件事做得正好、做到位（口语）：`She nailed the interview.` · `You nailed it!` · `nail the basics`。
同一格里的邻居（别串）：🎓#620 master ＝ 练很久、彻底掌握一门技能（master a magic trick）· 🎓#402 pull off ＝ 把难事办成。
判据一句话：一次做得漂亮／做到位 ⇒ nail；花很长时间练成 ⇒ master；难事居然办成了 ⇒ pull off。
★ 题型判整句：同 🎓#641 等她点名学的词先例，整句 ＋ 正向点名。

**怎么发现的**
2026-11-15 学习日 复检第 4 组 [7]（#626 题面"学开车得先把基本功练扎实，再上高速。"）· 原话
`When learning to drive, you've got to nail(学下) the basics first before getting on the highway.`
她写对了 nail，但自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #675 #679 先例）。
判重三步：
　① 目标形式 dedup "nail" ⇒ 全档零命中；邻居 "ace" ⇒ 零命中
　② 中文 dedup "练扎实" ⇒ 零命中；"搞定" ⇒ 🎓#402 pull off（办成难事，另一个词）· 🎓#489 in no time · 🎓#505 in a bit（都是时间块，无关）⇒ 否
　③ 保留新建（⛔ 建号当天不测）；与 🎓#620 master 的区别：master 是长期练成，nail 是一次做到位

**我错在哪**
她的：写对了 `nail the basics`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"表现得特别好／一次就做对了／拿下了" ⇒ nail。

**题面**
"她面试前准备了整整一个星期，结果那场面试表现得特别好。"（"表现得特别好"用 **nail** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：She spent a whole week preparing, and she totally nailed the interview.

- 2026-11-15 ❌ 首犯 · 学习日 复检第 4 组 [7]（#626 题里）· 她标「学下」· 原话 `When learning to drive, you've got to nail the basics first before getting on the highway.`
- 2026-11-16 ✅ 学习日 在池第 2 组 [6] · `She prepped for a whole week before the interview, and she ended up totally nailing it.` —— nailing it。连错 1 → 连对 1

### 683 · **beforehand**（事先、提前；副词，放句尾，后面不接东西）
类型 词汇 ｜ 新建 2026-11-15 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**beforehand** ＝ 在那件事之前（副词，单独放在句尾）：`It's best to call beforehand.` · `I had no idea beforehand.`
同一格里的邻居（别串）：in advance ＝ 提前（常配 book／pay／plan in advance）· before ＋ 事件 ＝ 后面必须接东西（before the meeting）。
判据一句话："事先"后面不接事件、落在句尾 ⇒ beforehand；后面要接事件 ⇒ before ＋ 名词。
★ 题型判整句：同 🎓#641 等她点名学的词先例，整句 ＋ 正向点名。

**怎么发现的**
2026-11-15 学习日 复检第 4 组 [9]（#628 题面"这次涨价是几个股东关起门来商量的，员工事先一点都不知道。"）· 原话
`This price hike was discussed behind closed doors by a few shareholders, and the staff had no idea beforehand(这个词学下).`
她写对了 beforehand，但自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #675 #679 先例）。
判重三步：
　① 目标形式 dedup "beforehand" ⇒ 全档零命中；邻居 "in advance"／"ahead of time" ⇒ 零命中
　② 中文 dedup "事先" ⇒ 🎓#431 planned out · 🎓#593 hype up（正文字样，别的块）⇒ 否；"提前" ⇒ 🎓#203 though · 🎓#361 get off work on time · 🎓#73 · 🎓#97（字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `had no idea beforehand`，但词不在手边（自己标学下）　　目标：同她原句
找法：句尾想说"事先／提前"、后面又没东西可接 ⇒ beforehand。

**题面**
"去别人家做客，最好事先打个电话说一声。"（"事先"用 **beforehand** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：If you're visiting someone, it's best to give them a call beforehand.

- 2026-11-15 ❌ 首犯 · 学习日 复检第 4 组 [9]（#628 题里）· 她标「这个词学下」· 原话 `the staff had no idea beforehand.`
- 2026-11-16 ✅ 学习日 在池第 2 组 [7] · `When you're visiting someone's place, it's best to call and let them know beforehand.` —— let them know beforehand。连错 1 → 连对 1

### 684 · **N times in a row**（连着 N 次；⛔ 数次数时不用 in one sitting）
类型 词组 ｜ 新建 2026-11-15
状态 连对1 连错0 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**N times／N days ＋ in a row** ＝ 一次接一次、中间没断：`five times in a row` · `three days in a row`。
同一格里的邻居（别串）：🎓#605 in one sitting ＝ 一次坐下来不停，把一件事做完（看完一部剧、吃完一个披萨），说的是一个连续过程，不数次数 · 🎓#434 for a month straight ＝ 连续一整段时间。
判据一句话：数的是"几次／几场／几天"一个接一个 ⇒ in a row；坐下来一口气把一件事做完 ⇒ in one sitting。
★ 题型判整句："连着"能落到 one after another／back to back 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-15 学习日 复检第 4 组 [5]（#624 题面"游乐园里的碰碰车十块钱玩一次，我儿子一口气玩了五次。"）· 原话
`The bumper cars at the amusement park cost ten yuan a pop, and my son went on them five times in one sitting.`
考点外 ⚠️：碰碰车一轮一轮地玩，数的是次数 ⇒ five times in a row；in one sitting 是一次坐下来做完一件事 ⇒ 用偏了（§3.2b：她的词在这里搭不上 ⇒ 不是同级近义词 ⇒ 建号）。
判重三步：
　① 目标形式 dedup "in a row" ⇒ 🎓#434（正文邻居行；那条考 consecutive 配不配单数）⇒ 否；"back to back" ⇒ 零命中
　② 中文 dedup "一口气"／"in one sitting" ⇒ 🎓#605 in one sitting（一次坐下来做完，不数次数，本条正是它的边界外）· 🎓#390 get through · 🎓#583 skewer（字样）⇒ 否；"连着"／"连续" ⇒ 都是正文字样，考点无关 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）；session 与档案里找不到她自己产出过 in a row

**我错在哪**
她的：`five times in one sitting`　　更好：`five times in a row`
找法：中文"一口气／连着 ＋ 几次" ⇒ 先问是不是在数次数，是 ⇒ in a row。

**题面**
"这家超市的抽奖我连着中了三次，收银员都不敢相信。"（"连着"用 **in a row** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I won the supermarket's prize draw three times in a row—the cashier couldn't believe it.

- 2026-11-15 新建 · 学习日 复检第 4 组 [5]（#624 题里）· 原话 `my son went on them five times in one sitting.`
- 2026-11-16 ✅ 学习日 在池第 2 组 [9] · `I won this supermarket's lucky draw three times in a row—even the cashier couldn't believe it.` —— three times in a row。首测 ⇒ 连对 1

### 685 · **on the sidelines**（在场边：sit on the sidelines and watch · watch from the sidelines）
类型 词组 ｜ 新建 2026-11-16 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**on the sidelines** ＝ 在场边（比赛场地边线外，不上场，只能看）；sidelines 用复数，前面用 on。
常用搭配：sit on the sidelines（坐在场边）· watch from the sidelines（在场边看）；引申 ＝ 没参与、只能旁观：I was stuck on the sidelines.
同一格里的邻居（别串）：on the bench ＝ 替补席（坐板凳）· in the stands ＝ 在看台上（观众坐的地方）。
判据一句话：人在场地边上、没上场 ⇒ on the sidelines；观众席 ⇒ in the stands。
★ 题型判整句：同 🎓#641 等她点名背的单词先例，整句 ＋ 正向点名；首次出题给整块（§6② 她点名要学 ⇒ 练），连对 ≥1 之后降回 sidelines 点名。

**怎么发现的**
2026-11-16 学习日 在池第 1 组 [2]（#667 题面"他第三节还没打完就犯满离场了，只能坐在场边看。"）· 原话
`He fouled out before the third quarter was even over, so he just had to sit on the sidelines(背下) and watch.`
她写对了 on the sidelines，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #675 #634 先例）。
判重三步：
　① 目标形式 dedup "sideline" ⇒ 全档零命中；"bench" ⇒ 零命中
　② 中文 dedup "场边" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `sit on the sidelines`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"在场边／在边上看着" ⇒ on the sidelines（复数 ＋ on）。

**题面**
"我脚崴了，整场比赛只能坐在场边看。"（"在场边"用 **on the sidelines** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I sprained my ankle, so I had to sit on the sidelines for the whole game.

- 2026-11-16 ❌ 首犯 · 学习日 在池第 1 组 [2]（#667 题里）· 她标「背下」· 原话 `so he just had to sit on the sidelines and watch.`

### 686 · **drummer**（鼓手；打鼓 ＝ play the drums）
类型 词汇 ｜ 新建 2026-11-16 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**drummer** ＝ 鼓手（drum ＋ m ＋ er，m 双写）：`He's the drummer in a local band.`；打鼓 ＝ `play the drums`（drums 用复数）。
同一格里的邻居（别串）：guitarist 吉他手 · bassist 贝斯手 · lead singer 主唱 · keyboardist 键盘手。
判据一句话：乐队里打鼓的那个人 ⇒ drummer。
★ 题型判整句：同 #680 等她点名背的单词先例，整句 ＋ 正向点名。

**怎么发现的**
2026-11-16 学习日 复检第 3 组 [4]（#634 题面"我们乐队的鼓手是位打了二十多年的老鼓手，什么场子都镇得住。"）· 原话
`Our band's drummer（背下） is a veteran who's been playing for over twenty years—he can handle any kind of crowd.`
她写对了 drummer，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #680 #685 先例）。
判重三步：
　① 目标形式 dedup "drummer" ⇒ 全档零命中
　② 中文 dedup "鼓手" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `Our band's drummer`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"鼓手" ⇒ drum ＋ -er。

**题面**
"我儿子学了三年架子鼓，现在是学校乐队的鼓手。"（"鼓手"用 **drummer** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My son has been learning the drums for three years, and now he's the drummer in the school band.

- 2026-11-16 ❌ 首犯 · 学习日 复检第 3 组 [4]（#634 题里）· 她标「背下」· 原话 `Our band's drummer is a veteran who's been playing for over twenty years`

### 687 · **compliment sb on sth**（当面夸某人某方面：She complimented me on my haircut.）
类型 词汇 ｜ 新建 2026-11-16 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**compliment** ＝ 当面夸人（衣服、发型、做的菜）：`She complimented me on my haircut.`；夸的东西直接当宾语也行：`He complimented my cooking.`
名词同形：`That's a compliment.`（这是在夸你）· `Thanks for the compliment!`
同一格里的邻居（别串）：🎓#638 flatter ＝ 拍马屁，夸得过头、有目的 · 🎓#609 rave about sth ＝ 逢人就夸一样东西 · praise ＝ 表扬，偏正式、多是上对下。
判据一句话：真心当面夸别人 ⇒ compliment；夸得过头想讨好 ⇒ flatter。
★ 题型判整句："夸"能落到 said … looked nice／praised 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 compliment。

**怎么发现的**
2026-11-16 学习日 复检第 3 组 [8]（#638 题面"新来的实习生特别会拍马屁，天天夸经理的衣服好看。"）· 原话
`The new intern is really good at flattering people—she compliments（这个词学下） the manager's outfits every single day.`
她写对了 compliments，但自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #680 先例）。
判重三步：
　① 目标形式 dedup "compliment" ⇒ 全档零命中
　② 中文 dedup "夸" ⇒ 12 条，逐条否：🎓#609 rave about（逢人就夸）· 🎓#638 flatter（拍马屁）· 🎓#639 win over（拉拢）—— 词都不是 compliment ⇒ 否；🎓#440 #6 #22 #53 #289 #643 #651 #647 #664 是正文碰巧有"夸"（夸张等）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `she compliments the manager's outfits`，但词不在手边（自己标学下）　　目标：同她原句；夸人 ⇒ compliment sb on sth
找法：中文"夸他…好看／做得好"、当着本人说 ⇒ compliment。

**题面**
"我同事今天夸我的新发型好看，我高兴了一整天。"（"夸"用 **compliment** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My coworker complimented me on my new haircut today, and it made my whole day.

- 2026-11-16 ❌ 首犯 · 学习日 复检第 3 组 [8]（#638 题里）· 她标「这个词学下」· 原话 `she compliments the manager's outfits every single day.`

### 688 · **I only meant to ＋ 动词**（本来只打算…；mean to ≠ want to）
类型 句型 ｜ 新建 2026-11-16 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**mean to do** ＝ 当时的打算、本来的意思（说的是"打算"）：`I only meant to stay for a minute.`
**want to do** ＝ 想要（说的是"愿望"）：`I want to stay longer.`
"本来只打算…结果…" ⇒ `I only meant to …, but …`（打算没照着走）。否定最常用：`I didn't mean to.`（我不是故意的）。
同一格里的邻居（别串）：was going to ＝ 本来要（已经定好的计划）· wanted to ＝ 当时想（心里的愿望）· 🎓#338 end up ＋ -ing（"结果"那一半）。
判据一句话：说"本来只打算／本来没想…，结果…" ⇒ meant to；单纯说想要什么 ⇒ want to。
★ 题型判整句：考点是 meant to 跟"结果"那半句搭在一起才现形；"本来只想"能落到 I just wanted to 绕开 ⇒ 整句 ＋ 正向点名 mean。

**怎么发现的**
2026-11-16 学习日 复检第 4 组 [1]（#338 题面"我本来只想眯十分钟，结果最后一觉睡到了天黑。"）· 原话
`I only meant（和 want to 对比学下) to take a quick ten-minute nap, but I ended up sleeping straight through until dark.`
她写对了 meant to，但自己标「和 want to 对比学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #680 先例）。
判重三步：
　① 目标形式 dedup "meant to" ⇒ 零命中；"mean to" ⇒ 🎓#478 只在历史行里碰巧出现（show how much you care）⇒ 否
　② dedup "was going to" ⇒ 🎓#171（tell sb）· 🎓#39（定冠词）只在例句里出现 ⇒ 规则不同 ⇒ 否；中文 dedup "本来只想" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `I only meant to take a quick ten-minute nap`，但分不清它和 want to（自己标学下）　　目标：同她原句
找法：中文"本来只是想…"后面跟着"结果" ⇒ I only meant to。

**题面**
"我本来只想说两句，结果一讲就讲了一个小时。"（"本来只想"用 **mean** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I only meant to say a few words, but I ended up talking for an hour.

- 2026-11-16 ❌ 首犯 · 学习日 复检第 4 组 [1]（#338 题里）· 她标「和 want to 对比学下」· 原话 `I only meant to take a quick ten-minute nap, but I ended up sleeping straight through until dark.`

### 689 · **halfway ＋ up／down／through／there**（走到一半、做到一半：halfway up the mountain）
类型 词组 ｜ 新建 2026-11-16 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**halfway** 后面跟一个小词，说清楚是"往哪走到一半／做什么做到一半"：
`halfway up the mountain`（半山腰，往上爬）· `halfway down the road／the stairs`（路上／楼梯走到一半）
`halfway through the movie／the meeting`（看到一半、开到一半）· `halfway there`（去的路上走了一半）
同一格里的邻居（别串）：🎓#669 twenty pages in（读了多少页）· in the middle of sth（正在做…的当中，不强调"一半"）。
判据一句话：在往上爬 ⇒ up；往下走或沿着路走 ⇒ down；一件事的中间 ⇒ through；去某地的路上 ⇒ there。
★ 题型判整句：小词跟着句子里的动作走（爬山 ⇒ up），单翻一个块看不出方向 ⇒ 整句 ＋ 只点名 halfway，小词留给她。

**怎么发现的**
2026-11-16 学习日 复检第 4 组 [5]（#564 题面"我们去爬山那天，半路上突然下了一场冰雹，砸得头都疼。"）· 原话
`The day we went hiking, it suddenly started to hail halfway up(halfway 后面接 up/down 学下), and the hailstones actually hurt my head.`
她写对了 halfway up，但自己标「halfway 后面接 up/down 学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #680 先例）。
判重三步：
　① 目标形式 dedup "halfway" ⇒ 🎓#215 #384 #144 #486 #506 #668，全是例句或历史里碰巧有 halfway，没有一条讲 halfway 后面接什么 ⇒ 否
　② 中文 dedup "半路" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `halfway up`，但 halfway 后面接哪个小词不确定（自己标学下）　　目标：同她原句
找法：中文"半山腰／半路上／看到一半" ⇒ 先问自己在往哪个方向走，再给 halfway 配小词。

**题面**
"我们才爬到半山腰，我女儿就喊走不动了。"（"半山腰"用 **halfway** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：We were only halfway up the mountain when my daughter said she couldn't walk any farther.

- 2026-11-16 ❌ 首犯 · 学习日 复检第 4 组 [5]（#564 题里）· 她标「halfway 后面接 up/down 学下」· 原话 `it suddenly started to hail halfway up`

### 690 · **go so far as to ＋ 动词**（甚至到了…的地步：He went so far as to quit.）
类型 句型 ｜ 新建 2026-11-16 ｜ ⭐ 她点名要学 ｜ 与 🎓#70 互斥（那条单独一句往回收，本条后面要说出那个说法）
状态 连对0 连错1 上次2026-11-16 未毕业 ｜ 题型 整句

**问题是什么**
**go so far as to ＋ 动词原形** ＝ 甚至做到／说到某个地步：`My boss went so far as to say he'd fire us all.`
否定用来收着说：`I wouldn't go so far as to call it a rip-off.`　同义：`go as far as ＋ -ing`（I wouldn't go as far as calling it a rip-off）。
同一格里的邻居（别串）：🎓#70 I wouldn't go that far, though. ＝ 单独一句往回收，不重复那个说法 · 🎓#250 that far vs too far。
判据一句话：后面要说出那个"过头的说法／做法" ⇒ go so far as to ＋ 动词；只往回收一句 ⇒ I wouldn't go that far。
★ 与 🎓#70 题面互斥：本条的题面必须让后面说出那个说法（甚至说…），#70 的题面是单独一句往回收。

**怎么发现的**
2026-11-16 学习日 复检第 4 组 [10]（#70 题面"这家餐厅是挺贵的，可说它是在抢钱，我倒不会说得那么夸张。"）· 原话
`This restaurant is pretty pricey, sure, though I wouldn't go so far as to(as to 学下) call it a rip-off.`
她写对了 go so far as to call，但自己标「as to 学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #680 先例）。
判重三步：
　① 目标形式 dedup "so far as" ⇒ 零命中
　② dedup "go that far" ⇒ 🎓#70（单独一句往回收的整块）· 🎓#250（that far vs too far）—— 都不带「as to ＋ 动词」这个结构 ⇒ 差在结构上 ⇒ 否；10-24 她在 #70 题里说过 go as far as saying（判 ✅ 未建号）
　③ 保留新建（⛔ 建号当天不测），题面与 #70 互斥

**我错在哪**
她的：写对了 `I wouldn't go so far as to call it a rip-off`，但 as to 这一截不在手边（自己标学下）　　目标：同她原句
找法：中文"甚至说…／至于说…那就过了" ⇒ go so far as to ＋ 动词原形。

**题面**
"我老板甚至说，要是这个项目搞砸了，就把我们全部开除。"（"甚至说"用 **go so far** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My boss went so far as to say that if this project failed, he'd fire all of us.

- 2026-11-16 ❌ 首犯 · 学习日 复检第 4 组 [10]（#70 题里）· 她标「as to 学下」· 原话 `though I wouldn't go so far as to call it a rip-off.`

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

