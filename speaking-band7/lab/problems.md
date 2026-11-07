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

### 251 · cost ＋ 钱／take ＋ 时间／spend ＋ 人做主语
类型 搭配 ｜ 旧号 B230
状态 连对0 连错1 上次2026-11-06 未毕业 ｜ **回潮 2026-11-06**（10-20 第二次毕业 → 11-06 复检 #372 题里写成 `I spent a week to finally get one`，spend ＋ 时间 ＋ to do，撤销毕业、连对清零；更早一次回潮 10-17 见历史行）｜ 题型 整句

**问题是什么**
**cost ＋ 钱 ／ take ＋ 时间 ／ spend ＋ 人做主语**：
`**it takes** two hours to cook a meal.`（时间 ⇒ take）｜ 钱 ⇒ cost ｜ 人当主语 ⇒ spend。
人当主语那条路的完整句型 ＝ **人 ＋ spend ＋ 时间 ＋ doing**（`I spent a week trying to get one.`）—— ⛔ spend ＋ 时间 ＋ to do；要用 to do 就换 take 那条路（`it took me a week to get one`）。
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
"这台二手相机花了我三千块，光研究怎么用就又花了我一整个周末。"（两个"花了我"一个用 **cost** 说，一个用 **take** 说）
　　★ 两个都点名、由她自己分配：钱 ⇒ cost me three thousand、时间 ⇒ took me a whole weekend；两个方向她都掉过（时间配 cost 的苗头 08-19、钱配 take 10-17 回潮）
　　★ 2026-10-17 改：旧种子"从我家开车到机场要一个多小时"只测时间那一半
　　★ 2026-10-19 改：零提示／只点 me 时，她用 set me back（paid 也行）就绕开了 cost ⇒ 改成 cost／take 双点名

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
- 2026-10-19 ✅ 学习日 在池第 1 组 [1] · 题面"这台二手相机花了我三千块，光研究怎么用就又花了我一整个周末。"（两个"花了我"都用 me 说）· `This second-hand camera set me back three thousand RMB, and just figuring out how to use it took me another whole weekend.` —— 钱用 set me back（＝ cost me，合法且贴题面）、时间 took me ✓。连错 1 → 连对 1
- 2026-10-19 📝 题面整改（§3.3 硬顺序③）：她用 set me back 绕开了 cost ⇒ 种子点名改成 cost／take 两个都点、由她自己分配给钱和时间（二选一仍是考点，又不给答案）
- 2026-10-20 ✅ 学习日 在池第 1 组 [1] · `The materials cost me eighty thousand RMB for this renovation, and overseeing the workers took me two whole months.` —— 钱 cost me、时间 took me，两处自己分配都对。连对 1 → 2 ⇒ 🎓 毕业（10-17 回潮后重新毕业）
- 2026-10-24 ✅ 复检 · 学习日 复检第 4 组 [1] · `This trip to Japan cost me six grand just for the flights, and taking care of the visa took me another two weeks.` —— cost me（钱）／ took me（时间）分配都对
- 2026-10-26 ✅ 学习日 ③ 重答 bank:1286 S2（自由产出自发命中）· `She spent the whole day baking the sponge and frosting（这个词的用法学下) it with cream and chocolate.` —— spent the whole day baking（人做主语 ＋ doing；首答 08-15 这里掉过 spent a whole afternoon to bake）。🎓 只推 rc
- 2026-11-06 ❌ 学习日 复检第 4 组 [10]（🎓#372 题里）· `That collab thermos was so hard to get my hands on—I spent a week to finally get one.` —— spend ＋ 时间 ＋ to do（同条 08-15 掉过 spent a whole afternoon to bake）⇒ 最小改 `I spent a week trying to get one`／更好版 `it took me a whole week to finally get one` ⇒ 🎓 回潮
- 备注 2026-08-19 她在自由句里写 `it just takes/costs ten minutes`（两个都列出来）——
  首选 takes 是对的，不记回潮；但 **cost 只配钱** 这条边界还没固化，再出现一次就按回潮处理

### 271 · recently／lately／so far 这一族默认拉完成时（要用一般现在时就换成 these days）
类型 语法 ｜ **合并条·出题多句覆盖**（§3.2c）｜ 新建 2026-08-23
状态 连对0 连错1 上次2026-11-06 未毕业 ｜ **合并条·出题多句覆盖** ｜ 题型 整句 ｜ **回潮 2026-11-06**（10-12 第二次毕业 → 11-06 复检 #392 打包块里写成 `my daughter is obsessed with recently`，recently 配了一般现在时，撤销毕业、连对清零；更早一次回潮 10-10 见历史行）

**问题是什么**
**recently ／ lately ／ so far** 这一族默认**拉完成时**（要用一般现在时就换成 **these days**）。
判据：
```
recently ／ lately ／ so far ／ up to now ＝ "**到现在为止的一段**" ⇒ **拉完成时**
   ✅ I haven't had much time recently.      ✅ Things have got busier lately.
   ✅ We've done three so far.                ✅ It hasn't rained up to now.
想用一般现在时 ⇒ 换成**指现在这个阶段**的副词：
   these days ／ at the moment ／ right now ／ nowadays
   ✅ I don't have much time these days.
★ 判据一句话：**这个副词说的是"一段"还是"此刻"？** 一段 → 完成时；此刻 → 现在时
★ 例外（不用改）：recently ＋ **过去时**说一个具体的点也成立 —— I saw him recently.（那次见面是个点）
```
★ 与 🎓**#90** 的分工写死（见下方备注）：**#90 ＝ for/since · ever/never/before · just/already/yet**
　｜ **本条 ＝ recently／lately／so far／up to now**。两条题面互斥，各走各的连击。
★ 与 **#259**（have 后面用过去分词）的分工：#259 管 have 后面动词**变什么形**（形态），
　本条管"**要不要用完成时**" ⇒ 不同层。
★ 与 **#269** 的分工（互斥写死，2026-09-05 定）：**带"最近/这阵子" ⇒ 本条（时态）；
　不带时间副词 ⇒ #269（否定 ＋ much）**。

**怎么发现的**
2026-08-23 新建 · 付息日 a 段 · 复习 #269 句里 · 她写 `I don't have much time **recently**.`
（→ I **haven't had** much time recently.）—— 副词是"一段"，动词却停在一般现在时。
★ **从 🎓#90 摘出**（§3.2c ③：合并条里冒出没覆盖到的成员就单独摘出来，老的不动）
判重（当天新建复核，§4④1b）：
　① 目标英文形式 ＝ `haven't had much time recently`（recently ⇒ 完成时）
　② grep "完成时"／"recently"／"lately"／"these days" 全库（含已毕业）→
　　 命中 **🎓#90**（完成时的三个触发：for/since · ever/never/before · just/already/yet）
　　 · #259（have 后面用过去分词）· 🎓#130（can vs be able to）
　③ 逐条读：**#90** 列的是"**哪些词触发完成时**"—— recently 是同一条规则的**第四组成员，
　　 但它从来没被写进 #90**。按 §3.2c ③ 摘出成新条；**#90 已毕业、连对3，不动、不回潮**
　　（她不能为一条从没写进条目里的成员被判退步）。
　　 **#259** 管 have 后面动词**变什么形**（形态），不是"要不要用完成时" ⇒ 不同层。
　　 **🎓#130** 管 can／be able to 的选择 ⇒ 无关
　⇒ 保留新建。

**我错在哪**
她的：`I don't have much time **recently**.`　　正确：`I **haven't had** much time recently.`
找法：句子里蹦出 recently／lately／so far 时，回头看动词 —— **have/has ＋ 过去分词 在不在？**
不在 ⇒ 要么把动词拉成完成时，要么把副词换成 these days。

**题面**
★ 2 句，一句测"副词拉完成时"、一句测"换副词保现在时"
　① **点名**："我最近没什么时间。"（用 **recently** 说）
　② **点名**："这阵子东西贵了不少。"（用 **lately** 说）
　　★ 目标形式（教练看，⛔ 不进发题稿）：① I haven't had much time recently. ② Things have got a lot pricier lately.

**成员出题账**
① recently ｜ 08-23 ❌（首犯）· 08-24 ✅ · 08-25 ✅ · 09-11 ✅ · 10-04 ✅ · 10-11 ✅ · 10-12 ✅ · 10-16 ✅ · 10-25 ✅
② lately ｜ 08-24 ✅ · 08-25 ✅ · 09-11 ✅ · 10-04 ✅ · 10-11 ✅ · 10-12 ✅ · 10-16 ✅ · 10-25 ✅
★ 题面外的两次**自发命中**（不出题、只留痕）：08-25 `over the past year`（拉完成时）·
　08-26 `These days he's doing really well.`（判据的另一半，走现在时）⇒ 她调的是判据不是那几个词。

- 2026-08-23 新建 · 付息日 a 段 · 复习#269 句里 · `I don't have much time **recently**.`
  → I **haven't had** much time recently.
- 2026-08-24 ✅ 复习第1组 · **合并条 2 句整组首测，2/2 全对**（§3.2c）：
  ① `I haven't had much time recently.`（与目标形式一字不差）
  ② `Things have become a lot more expensive lately.`
  ⇒ **连错 1 → 0（清零），连对 0 → 1（差一次毕业）**
  ★ ② 条目预期是 `have got a lot pricier`，她答的 `have become a lot more expensive`
    **完全合法且正中考点**（现在完成时 ＋ lately）⇒ 按 §3.3 记 ✅，不记 ◎
  ★ 教练自审：想把 `have become` 标 ⚠️ 降级成 have got／have gone up。试造母语句推翻自己 ——
    `Things have become a lot more expensive lately.` 母语者说得毫无问题、不书面 ⇒ 档位不成立，
    写「无更好版本」，不标
- 2026-08-25 ✅ 复习第1组 · **合并条 2 句整组，2/2 全对**（§3.2c）：
  ① `I haven't had much time recently.`　② `Things have become a lot more expensive lately.`
  ⇒ **连对 1 → 2 ⇒ 毕业**
  ★ 教练自审留痕（§7 四问②）：② 的条目预期是 `have got a lot pricier`；08-24 已就
    `have become a lot more expensive` 自审过一次并判**档位不成立**（母语者照说）。
    今天无任何新证据 ⇒ **不翻案**，照记 ✅ ＋ 无更好版本
- 2026-08-25 ✅ **自发命中**（毕业当天下午，本条未被出题，不改状态）· 加练新题 bank:1043 P2 ·
  `**Over the past year**, I've bought him a lot of Lego sets.`
  ——`over the past year` ＝ "到现在为止的一段" ⇒ 拉现在完成时，她自己拉对了
  ★★ **一次真迁移**：本条今天上午刚毕业（中译英两句全对），下午在**没有中文题面**的自由产出里
     换了一个从没测过的成员（over the past year，不在本条的四个成员里）照样拉对
     ⇒ 说明她调的是**判据**（一段 vs 此刻），不是背下来的那四个词
- 2026-08-26 ✅ **自发命中·第二次真迁移**（本条未被出题，不改已毕业状态）· 自由产出（新题 bank:244 P2）·
  `**These days** he's doing really well.`
  ——本条判据的**另一半**（"要用一般现在时就换成 these days，别用 recently 拉完成时"）
  这次是正向用：想说"现在这阵子"⇒ 直接上 these days ＋ 现在进行，没去写 recently he is…
  ★ 两天两次、两个不同成员、两个方向（08-25 over the past year 拉完成时 ／
    今天 these days 走现在时）⇒ 判据本身已经在手，不是背词
- 2026-09-11 ✅ 复检 · 付息日 a2 第 7 组 · 合并条 2 句：① `I haven't had much time recently.` ② `Things have got to a lot more expensive lately.` —— 两句都拉出完成时，考点 2/2
  ⚠️ ② `have got **to** a lot more expensive` 多了 to（get ＋ 形容词中间⛔不加 to），一次性滑手，⛔ 不落本条、不建号
- 2026-10-04 ✅ 复检 · 付息日 a2 复检第 4 组 [3] · `I haven't been sleeping too well recently.` ／ `We've been working way more overtime lately at our company.` —— recently ／ lately 两个成员都拉完成（进行）时
- 2026-10-10 ❌ 学习日 复检第 3 组 [8]（#21 题里 · 自由产出掉）· `My dad keeps forgetting his keys recently, …` —— recently 配了一般现在时 keeps forgetting ⇒ **回潮**
  最小改 `My dad keeps forgetting his keys these days, and he had to call a locksmith twice just last week.`
  ❌ recently ＝ 到现在为止的一段 ⇒ 拉完成时（he's been forgetting his keys a lot recently）；想用一般现在时 ⇒ 换 these days
- 2026-10-11 ✅ 学习日 在池第 1 组 [3] · 合并条 2 句：① `I haven't really been working out much recently.` ② `I haven't stayed in touch with my old classmates as much lately.` —— recently／lately 两个成员都拉完成（进行）时。连错 1 → 连对 1
- 2026-10-11 📝 学习日 ③ 新题 bank:963 S14 · **自发用对判据，只留痕** · `Over the years, he's done really well in his career.` —— over the years ＝ 到现在为止的一段 ⇒ 自己拉了完成时
  ★ over the years 不是本条四个成员之一 ⇒ ⛔ 不算一次被测、不推进连对（同 08-25 over the past year 的留痕口径）
- 2026-10-12 ✅ 付息日 a 段在池第 1 组 [1] · **合并条 2 句，2/2 全对**（§3.2c）：
  ① `I haven't really read much recently.`　② `Lately, I've been drinking way more coffee than I used to.`
  —— recently ＋ haven't read、lately ＋ I've been drinking，两个副词都拉了完成时。连对 1 → 2 ⇒ **毕业**（10-10 回潮后第二次毕业）
- 2026-10-16 ✅ 复检 · 学习日 复检第 3 组 [1] · `① I haven't really seen my friends much recently. ／ ② Rent has gone up quite a lot lately.` —— recently／lately 都拉了现在完成时。🎓 rc0 → rc1
- 2026-10-25 ✅ 复检 · 学习日 复检第 3 组 [6] · `① I've been helping my sister put together her wedding recently. ／ ② Lately, a few new bubble tea shops have opened up near my house.` —— recently／lately 都拉了现在完成（进行）时 ⇒ 成员出题账两行补 10-25 ✅（顺手补上漏记的 10-16 ✅）
- 2026-11-06 ❌ 学习日 复检第 4 组 [4f]（🎓#392 打包块里）· `the fitness influencer my daughter is obsessed with recently` —— recently 配了一般现在时 ⇒ 最小改 `has been obsessed with recently`／更好版 `is obsessed with these days` ⇒ 🎓 回潮
- 备注 与 🎓#90 的分工写死：**#90 ＝ for/since · ever/never/before · just/already/yet**
  ｜ **本条 ＝ recently／lately／so far／up to now**。两条题面互斥，各走各的连击

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

### 556 · **nothing to write home about**（一般般、不值一提：it's nothing to write home about）
类型 词组 ｜ 新建 2026-10-26 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-06 未毕业 ｜ 题型 整句

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
- 2026-10-27 ✅ 付息日 在池第 2 组 [6] · `We waited in line for an hour at that famous restaurant, but the food was honestly nothing to write home about.` —— nothing to write home about ✓（famous ⇒ 新建 #559）。连错 1 → 连对 1
- 2026-10-30 ✅ 学习日 在池第 1 组 [9] · `Everyone said that movie was amazing, but I watched it and found it to be nothing to write home about.` —— 点名只给 write home，nothing to write home about 自己补全 ✓。连对 1 → 2 ⇒ 🎓 毕业
- 2026-11-03 ✅ 付息日 a2 段复检第 3 组 [7] · `The place was hyped up to be amazing, but once I saw it in person, it was nothing to write home about.` —— nothing to write home about；同句她标学下 ⇒ 新建 #593
- 2026-11-04 ❌ 学习日 在池第 3 组 [4]（#593 题里）· `That new phone got hyped up like crazy before it came out, but it turned out to be nothing to write about home.` —— 固定块词序掉了：write about home ⇒ 最小改 nothing to write home about ⇒ 🎓 回潮
- 2026-11-06 ✅ 在池第 1 组 [2] · `…but I went there and found it was nothing to write home about.`（raving 背下 另建 #609）

### 600 · **stern**（严厉的、板着脸的：a stern look · a stern teacher）
类型 词汇 ｜ 新建 2026-11-03 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**stern** ＝ 严厉、不苟言笑（脸色、语气、人）：`a stern look` · `a stern voice` · `Our teacher was really stern.`
同一格里的邻居（别串）：strict（规矩严、要求高 —— 说管得严）· serious（严肃，最中性）· harsh（严厉到刻薄）。
判据一句话：脸色、语气让人发怵 ⇒ stern；规矩多、管得严 ⇒ strict。
★ 题型判整句："严肃／严厉"能落到 strict／serious 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 stern。

**怎么发现的**
2026-11-03 付息日 a2 段复检第 5 组 [6]d（🎓#380 题面"小说里描写老国王威严面容的那一句"）· 原话
`the sentence describing the old king's stern(背下) look`
她写对了 stern，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "stern" ⇒ 零命中
　② 中文 dedup "威严" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `the old king's stern look`，但词不在手边（自己标背下）　　目标：同她原句
找法：说"板着脸／很严厉的样子"先落 stern。

**题面**
"我们班主任平时很严肃，一瞪眼全班都不敢说话。"（"严肃"用 **stern** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Our homeroom teacher is usually really stern — one look from her and the whole class goes quiet.

- 2026-11-03 ❌ 首犯 · 付息日 a2 段复检第 5 组 [6]d（🎓#380 题里）· 她标「背下」· 原话 `the sentence describing the old king's stern(背下) look`
- 2026-11-06 ✅ 在池第 1 组 [1] · `Our head teacher is normally really stern—the second he glares at us, nobody dares to utter a word.`（head teacher 另建 #608）

### 601 · **syringe**（注射器；针头 ⇒ needle）
类型 词汇 ｜ 新建 2026-11-04 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**syringe** ＝ 注射器（整支针筒）：`The nurse filled the syringe.` · `a disposable syringe`（一次性注射器）
同一格里的邻居（别串）：needle（针头；口语里"打针的那根针"多半直接说 needle：I'm scared of needles.）· get a shot／an injection（打针这件事）。
判据一句话：说那支针筒 ⇒ syringe；说怕扎针、针头 ⇒ needle；说打针这个动作 ⇒ get a shot。
★ 题型判整句："注射器"能落到 needle 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 syringe。

**怎么发现的**
2026-11-04 学习日 在池第 1 组 [3]（#572 题面"护士拿着针走过来，我儿子吓得往后一缩。"）· 原话
`As the nurse approached with the syringe(背一下), my boy panicked and pulled away.`
她写对了 syringe，但自己标「背一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b，同 #571 #599 #600 先例）。
判重三步：
　① 目标形式 dedup "syringe"／"needle" ⇒ 零命中
　② 中文 dedup "打针" ⇒ 零命中；"针" ⇒ 🎓#534 #92 #317 #464（都是历史行字样，那几条考 pinecone／否定／when it comes to／tactics）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `with the syringe`，但词不在手边（自己标背一下）　　目标：同她原句
找法：说到"注射器／针筒"先落 syringe。

**题面**
"我去献血的时候，护士特意拆了一支新的注射器。"（"注射器"用 **syringe** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：When I went to give blood, the nurse made a point of opening a brand-new syringe.

- 2026-11-04 ❌ 首犯 · 学习日 在池第 1 组 [3]（#572 题里）· 她标「背一下」· 原话 `As the nurse approached with the syringe(背一下), my boy panicked and pulled away.`
- 2026-11-06 ✅ 在池第 3 组 [2] · `When I was donating blood, the nurse made sure to open a fresh syringe right in front of me.`

### 602 · **soy milk**（豆浆；⛔ 优先于 soybean milk）
类型 词汇 ｜ 新建 2026-11-04 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
豆浆 ＝ **soy milk**（最常用；soybean milk 也听得懂，但菜单、包装上基本都写 soy milk）：`soy milk and fried dough sticks`（豆浆油条）· `a soy milk maker`（豆浆机）
同一格里的邻居（别串）：soybean（黄豆这种豆子本身）· tofu（豆腐）· #577 fried dough sticks（油条）。
判据一句话：说喝的豆浆 ⇒ soy milk；说豆子 ⇒ soybeans。
★ 题型判整句："豆浆"能落到 soybean milk 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 soy。

**怎么发现的**
2026-11-04 学习日 在池第 1 组 [8]（#577 题面"在我们老家，大家早上都喝豆浆配油条。"）· 原话
`Where I'm from, people usually have soybean(背下) milk with fried dough sticks in the morning.`
她自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "soy" ⇒ #576 #577（历史与正文字样：豆浆油条的场合，那两条考 savory crepe／fried dough sticks）⇒ 否
　② 中文 dedup "豆浆" ⇒ 同上 #576 #577 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`soybean milk`（听得懂，但不是最常用的说法；自己标背下）　　目标：`soy milk`
找法：说到"豆浆"先落 soy milk。

**题面**
"他每天早上用豆浆机给自己打一杯豆浆。"（"豆浆"用 **soy** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Every morning he makes himself a glass of soy milk with his soy milk maker.

- 2026-11-04 ❌ 首犯 · 学习日 在池第 1 组 [8]（#577 题里）· 她标「背下」· 原话 `Where I'm from, people usually have soybean(背下) milk with fried dough sticks in the morning.`
- 2026-11-06 ✅ 在池第 3 组 [3] · `He makes himself a fresh cup of soy milk every morning using a soy milk maker.`

### 603 · **bumpy**（颠簸：a bumpy flight／ride／road）
类型 词汇 ｜ 新建 2026-11-04 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**bumpy** ＝ 坑坑洼洼、一路颠：`a bumpy road` · `a bumpy ride` · `The flight got really bumpy.`
同一格里的邻居（别串）：turbulence（飞机遇到的气流，名词：We hit some turbulence.）· rough（同义，偏"颠得难受"：a rough flight）· 🎓#543 bumper-to-bumper（堵车，一辆挨一辆）。
判据一句话：路、车、飞机"颠" ⇒ bumpy；说气流本身 ⇒ turbulence。
★ 题型判整句："颠"能落到 rough／shaky 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 bumpy。

**怎么发现的**
2026-11-04 学习日 在池第 1 组 [10]（#579 题面"飞机颠得很厉害，旁边那位大叔却一点都不慌，接着看他的报纸。"）· 原话
`The flight got super bumpy(背下), but the guy sitting beside me stayed totally unfazed and just carried on reading his paper.`
她写对了 bumpy，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "bumpy"／"turbulence" ⇒ 零命中
　② 中文 dedup "颠" ⇒ 🎓#318（历史行字样，那条考 one time when）⇒ 否；🎓#543 bumper-to-bumper 字形相近、词义不同（堵车）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `The flight got super bumpy`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"颠／颠得厉害"先落 bumpy。

**题面**
"去山里那段土路特别颠，我差点吐了。"（"颠"用 **bumpy** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The dirt road up into the mountains was so bumpy that I almost threw up.

- 2026-11-04 ❌ 首犯 · 学习日 在池第 1 组 [10]（#579 题里）· 她标「背下」· 原话 `The flight got super bumpy(背下), but the guy sitting beside me stayed totally unfazed and just carried on reading his paper.`
- 2026-11-06 ✅ 在池第 3 组 [4] · `The dirt road up into the mountains was so bumpy that I nearly threw up.`

### 604 · **oyster**（生蚝、牡蛎；常用复数 oysters）
类型 词汇 ｜ 新建 2026-11-04 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**oyster** ＝ 生蚝／牡蛎：`grilled oysters`（烤生蚝）· `raw oysters`（生吃的生蚝）· `an oyster bar`
同一格里的邻居（别串）：clam（蛤蜊）· scallop（扇贝）· mussel（青口）· shellfish（贝类总称）。
判据一句话：说"生蚝／牡蛎" ⇒ oysters；说一大类贝壳海鲜 ⇒ shellfish。
★ 题型判整句："生蚝"能落到 shellfish 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 oyster。

**怎么发现的**
2026-11-04 学习日 在池第 2 组 [2]（#581 题面"海边那家店的烤生蚝特别出名，每天都排长队。"）· 原话
`That place near the beach is super famous for grilled oysters(背下)—the queue is out the door every day.`
她写对了 oysters，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "oyster" ⇒ 零命中
　② 中文 dedup "生蚝" ⇒ #581（题面字样，那条考 grill）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `grilled oysters`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"生蚝"先落 oysters。

**题面**
"我第一次吃生蚝是在青岛，蘸了点柠檬汁就直接吞了。"（"生蚝"用 **oyster** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The first time I had oysters was in Qingdao — I just squeezed some lemon on them and swallowed them whole.

- 2026-11-04 ❌ 首犯 · 学习日 在池第 2 组 [2]（#581 题里）· 她标「背下」· 原话 `That place near the beach is super famous for grilled oysters(背下)—the queue is out the door every day.`
- 2026-11-06 ✅ 在池第 3 组 [5] · `I ate my first raw oyster in Qingdao—just squeezed some lemon juice over it and downed it.`

### 605 · **in one sitting**（一口气、一次坐下来就吃完／看完／读完）
类型 词组 ｜ 新建 2026-11-04 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**in one sitting** ＝ 一次坐下来没停就（吃完／看完／做完）：`I finished the whole series in one sitting.` · `He ate a whole pizza in one sitting.`
同一格里的邻居（别串）：in one go（一口气，范围更宽，不一定坐着）· 🎓#390 get through（读完、啃完一堆）· binge-watch（一口气刷剧）。
判据一句话："一口气吃完／看完／读完" ⇒ … in one sitting（或 in one go）。
★ 题型判整句："一口气"能落到 in one go／without stopping 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 sitting。

**怎么发现的**
2026-11-04 学习日 在池第 2 组 [4]（#583 题面"夜市上我一口气吃了十串羊肉串。"）· 原话
`I ate ten lamb skewers at the night market in one sitting(这个短语学下).`
她写对了 in one sitting，但自己标「这个短语学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "sitting" ⇒ 🎓#418 #425 #426 #435 #548 #554 #579（都是 sitting room／sitting on 之类的字样，考别的词）⇒ 否；"in one go" ⇒ #583（目标形式字样）⇒ 否
　② 中文 dedup "一口气" ⇒ 🎓#390（get through，邻居不同块）· #583（题面字样）· 🎓#105（字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `in one sitting`，但块不在手边（自己标学下）　　目标：同她原句
找法：说到"一口气（吃／看／读）完"先落 in one sitting。

**题面**
"那本小说太好看了，我一口气从头看到尾。"（"一口气"用 **sitting** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The novel was so good that I read it cover to cover in one sitting.

- 2026-11-04 ❌ 首犯 · 学习日 在池第 2 组 [4]（#583 题里）· 她标「这个短语学下」· 原话 `I ate ten lamb skewers at the night market in one sitting(这个短语学下).`
- 2026-11-06 ✅ 在池第 3 组 [6] · `That book was an absolute page-turner; I read the whole thing in one sitting.`

### 606 · **railing**（栏杆；扶手 ⇒ handrail／banister）
类型 词汇 ｜ 新建 2026-11-04 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**railing** ＝ 栏杆（阳台、桥边、楼梯边那一排）：`hold on to the railing` · `lean on the railing`
同一格里的邻居（别串）：handrail（扶手，专门给手扶的那根）· banister（楼梯扶手）· fence（围栏、篱笆，围一块地的）。
判据一句话：一排拦着、可以扶可以靠的 ⇒ railing；楼梯上专门扶手的 ⇒ handrail／banister；围地的 ⇒ fence。
★ 题型判整句："栏杆"能落到 fence／handrail 一串，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 railing。

**怎么发现的**
2026-11-04 学习日 复检第 4 组 [3]（🎓#561 题面"那位老人扶着栏杆，两条腿一直在发抖。"）· 原话
`Holding on to the railing（背下), the elderly man had legs that were trembling.`
她写对了 railing，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "railing" ⇒ 🎓#492（历史字样：鸟停在栏杆上，那条考 perch）⇒ 否
　② 中文 dedup "栏杆" ⇒ 🎓#327（foothold）· 🎓#492（同上）⇒ 否；"扶手" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `Holding on to the railing`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"栏杆"先落 railing。

**题面**
"我们靠在桥边的栏杆上看了好一会儿日落。"（"栏杆"用 **railing** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：We leaned on the railing by the bridge and watched the sunset for a while.

- 2026-11-04 ❌ 首犯 · 学习日 复检第 4 组 [3]（🎓#561 题里）· 她标「背下」· 原话 `Holding on to the railing（背下), the elderly man had legs that were trembling.`
- 2026-11-06 ✅ 在池第 3 组 [7] · `We leaned on the bridge railing and watched the sunset for a good while.`

### 607 · **with ＋ 身体部位 ＋ -ing**（伴随状态描写人：stood there with his legs trembling；⛔ had legs that were trembling）
类型 句型 ｜ 新建 2026-11-04
状态 连对1 连错0 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
主句说人在干什么，句尾挂 **with ＋ 身体部位 ＋ -ing** 描写他当时的样子：
　`The old man stood there with his legs trembling.` · `She ran in with her hair still dripping.` · `He sat there with his hands shaking.`
　（with 也可省：…, his legs trembling）
同一格里的邻居（别串）：🎓#470 with its siren blaring（同一个结构的固定块，那条考警笛 siren／blare 选词）· 直接说 His legs were trembling.（单说可以；但前面挂了 Holding… 分词时主语必须是人 —— 分词逻辑主语＝主句主语）。
判据一句话：一句里既要说人在做什么、又要说他身上某处的状态 ⇒ 人当主语 ＋ with his X -ing；⛔ 别写 had X that were -ing。
★ 题型判整句：结构只在句子里现形；"头发还在滴水"能落到 her hair was still dripping 绕开 ⇒ 正向点名 with。

**怎么发现的**
2026-11-04 学习日 复检第 4 组 [3]（🎓#561 题面"那位老人扶着栏杆，两条腿一直在发抖。"）· 原话
`Holding on to the railing（背下), the elderly man had legs that were trembling.`
the elderly man had legs that were trembling 语法能过，但没人这么说（⚠️ 不地道）；直接改成 his legs were trembling 又会让前面的 Holding 悬空 ⇒ 地道说法 ＝ stood there with his legs trembling ⇒ 能学的句型 ⇒ §3.2b 建号，判 ❌。
判重三步：
　① 目标形式 dedup "with his"／"with ＋" ⇒ 🎓#470（同结构的固定块 with its siren blaring，判据是 siren vs honk 选词）· #458 #486 #602 #383 #88 #338（字样）⇒ 否：本条考"描写人的身体状态时用这个结构"，与 #470 差在考点（结构 vs 警笛选词）
　② 中文 dedup "独立主格" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：the elderly man had legs that were trembling　　更地道：the elderly man stood there with his legs trembling
找法：写出 "had ＋ 身体部位 ＋ that was／were -ing" 时，回头换成 with his X -ing。

**题面**
"她从雨里跑进来，头发还在往下滴水。"（"头发还在滴水"用 **with** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：She ran in from the rain with her hair still dripping.

- 2026-11-04 ❌ 首犯 · 学习日 复检第 4 组 [3]（🎓#561 题里）· ⚠️ 不地道 · 原话 `Holding on to the railing（背下), the elderly man had legs that were trembling.`
- 2026-11-06 ✅ 在池第 3 组 [8] · `She ran in from the rain with water still dripping from her hair.` —— with ＋ 名词 ＋ -ing 挂在句尾描写状态，与目标 with her hair still dripping 同一结构

### 608 · **homeroom teacher**（班主任；⛔ head teacher ＝ 校长）
类型 词组 ｜ 新建 2026-11-06
状态 连对0 连错1 上次2026-11-06 未毕业 ｜ 题型 词组

**问题是什么**
**homeroom teacher** ＝ 班主任（管一个班的日常、开家长会的那位老师）；英式也说 **form teacher**／form tutor。
同一格里的邻居（别串）：**head teacher**／headteacher（英式）＝ 一所学校的校长，同 🎓#321 的 **principal** · class teacher（英式，小学里带一个班的老师）。
判据一句话：管的是"一个班"⇒ homeroom teacher；管的是"整个学校"⇒ principal／head teacher。
★ 题型判词组："班主任"三个字配上中文释义只映射回 homeroom teacher（或英式 form teacher，两个都判 ✅），不需要句子才现形。

**怎么发现的**
2026-11-06 学习日 在池第 1 组 [1]（#600 题面"我们班主任平时很严肃，一瞪眼全班都不敢说话。"）· 原话
`Our head teacher is normally really stern—the second he glares at us, nobody dares to utter a word.`
stern 对了，但"班主任"译成 head teacher ⇒ 母语者听到的是"校长" ⇒ 选词 ❌，建号。
判重三步：
　① 目标形式 dedup "homeroom" ⇒ 🎓#481（题面里的"班主任"，考 plan a surprise）· #600（本题，考 stern）⇒ 否，都只是场景里出现"班主任"
　② dedup "head teacher" ⇒ 🎓#321（principal ≠ principle：考"校长"那个词）⇒ 否：本条考"班主任"，差在词（homeroom teacher vs principal）
　③ 中文 dedup "班主任" ⇒ 同 ① 两条 ⇒ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：Our head teacher is …　　正确：Our homeroom teacher is …
找法：中文是"班主任"时先落 homeroom，别顺手把"班＋主任"译成 head。

**题面**
"班主任"（管一个班的日常、开家长会的那位老师）
★ 目标形式（教练看，⛔ 不进发题稿）：homeroom teacher（form teacher 也判 ✅）

- 2026-11-06 ❌ 首犯 · 学习日 在池第 1 组 [1]（#600 题里）· 原话 `Our head teacher is normally really stern—the second he glares at us, nobody dares to utter a word.`

### 609 · **rave about sth**（逢人就夸、夸个不停）
类型 词组 ｜ 新建 2026-11-06 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**rave about sth** ＝ 特别热情地夸、到处说它有多好：`She keeps raving about that new café.` · `Everyone's been raving about the show.`
常和 always／keep -ing 连用：was always raving about · keeps raving about。介词固定 **about**。
同一格里的邻居（别串）：praise（正式地表扬）· say good things about（一般地说好话）· speak highly of（书面一点）· 🎓#341 deserve praise（值得表扬，考 deserve 搭配）。
判据一句话：中文是"一直夸／逢人就夸／夸得不行"⇒ rave about。
★ 题型判整句："夸"能落到 praise 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 rave。

**怎么发现的**
2026-11-06 学习日 在池第 1 组 [2]（#556 题面"我同事一直夸他老家那个古镇，我去玩了一趟，觉得也就一般般。"）· 原话
`My colleague was always raving(背下) about the ancient town back in his hometown, but I went there and found it was nothing to write home about.`
她写对了 raving about，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #601 #602 #603 先例）。
判重三步：
　① 目标形式 dedup "rave" ⇒ 零命中
　② 中文 dedup "夸" ⇒ 🎓#341 deserve praise · #532 credit · #289 obsessed · #440 sentimental · #6 #22 #53 #340 #361（历史行字样）⇒ 否：都不是"夸个不停"这个词组
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `was always raving about`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"一直夸／逢人就夸"时先落 rave about，介词用 about。

**题面**
"我妈这阵子逢人就夸楼下新开的那家面包店。"（"逢人就夸"用 **rave** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My mom has been raving about the new bakery downstairs to everyone lately.

- 2026-11-06 ❌ 首犯 · 学习日 在池第 1 组 [2]（#556 题里）· 她标「背下」· 原话 `My colleague was always raving(背下) about the ancient town back in his hometown, but I went there and found it was nothing to write home about.`

### 610 · **drain ≠ sewer ≠ drainage**（下水口／排水管 · 城市下水道 · 排水）
类型 词汇 ｜ 新建 2026-11-06 ｜ ⭐ 她点名要学
状态 连对0 连错0 上次— 未毕业 ｜ 题型 词组 ｜ 合并条·出题多句覆盖

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
① drain ｜ 未出过
② sewer ｜ 未出过
③ drainage ｜ 未出过

- 2026-11-06 📝 新建 · 学习日 在池第 2 组 [4]（#592 题里）· 她要求学三个词的区别 · 原话 `The drains（和 sewer 的区别学下，还有 drainage) in this building back up whenever we get heavy rain.`

### 611 · **hear back (from sb)**（收到回音；⛔ without any responses）
类型 词组 ｜ 新建 2026-11-06
状态 连对0 连错1 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**hear back (from sb)** ＝ 你在等的人／公司给你回话：`I haven't heard back from them yet.` · `I applied last week and I'm still waiting to hear back.`
用在投简历、面试、发邮件、报名之后"有没有回音／有消息了没"。
同一格里的邻居（别串）：hear from sb（收到某人的消息，不一定是"回复"）· get a reply（书面一点）· without any responses（能懂，但像在报数据）。
判据一句话：等回复的场景说"没回音／没消息"⇒ haven't heard back (from …)。
★ 题型判整句："收到回音"能落到 get a reply／response 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 hear back。

**怎么发现的**
2026-11-06 学习日 在池第 2 组 [10]（#598 题面"我表姐辞职以后，在网上投了五十多份简历，一个回音都没有。"）· 原话
`Ever since my cousin quit her job, she's sent out more than fifty resumes online without any responses.`
send out 对了；"一个回音都没有"说成 without any responses ⇒ 能懂但不地道（⚠️），更地道的 hasn't heard back from any of them 是能学的表达 ⇒ §3.2b 建号，判 ❌。
判重三步：
　① 目标形式 dedup "hear back" ⇒ 零命中
　② 中文 dedup "回音" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：she's sent out more than fifty resumes online without any responses　　更地道：… and hasn't heard back from any of them
找法：说"一直没回音／没消息"时，先落 haven't heard back。

**题面**
"我上周面试完，到现在还没收到那家公司的回音。"（"收到回音"用 **hear back** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I had an interview last week, and I still haven't heard back from the company.

- 2026-11-06 ❌ 首犯 · 学习日 在池第 2 组 [10]（#598 题里）· ⚠️ 不地道 · 原话 `Ever since my cousin quit her job, she's sent out more than fifty resumes online without any responses.`

### 612 · **plain as day**（一目了然、明摆着；⛔ 不是"长得普通"）
类型 词组 ｜ 新建 2026-11-06
状态 连对0 连错1 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**plain as day** ＝ 明明白白、一眼就看得出来：`It was plain as day that he was lying.` · `The answer was right there, plain as day.`
同一格里的邻居（别串）：**plain** 单用 ＝ 朴素、不起眼（a plain white T-shirt · it looks pretty plain）· ordinary（普通）· obvious（明显，同义但不是习语）。
判据一句话：想说"很明显、明摆着"⇒ plain as day；想说"很普通、不起眼"⇒ plain／ordinary 单用，⛔ 后面别挂 as day。

**怎么发现的**
2026-11-06 学习日 复检第 4 组 [3]（🎓#565 题面"她那块手表看着普普通通，其实值两万块。"）· 原话
`That watch of hers looks plain as day, but it actually cost like twenty grand.`
grand 对了；"看着普普通通"写成 looks plain as day ⇒ 习语意思用反（变成"一眼就看得出来"）⇒ 选词 ❌，建号。
判重三步：
　① 目标形式 dedup "plain" ⇒ 零命中
　② 中文 dedup "普通" ⇒ 🎓#368 #456 #470 #18（历史行字样，考 land a job／crafted／siren／论元完整）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：That watch of hers looks plain as day　　正确：That watch of hers looks pretty plain（／pretty ordinary）
找法：写出 plain as day 时问一句：我是想说"明显"，还是"普通"？

**题面**
"他明摆着就是不想去，还一直找借口。"（"明摆着"用 **plain as day** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：It's plain as day that he doesn't want to go, but he keeps making excuses.

- 2026-11-06 ❌ 首犯 · 学习日 复检第 4 组 [3]（🎓#565 题里）· 原话 `That watch of hers looks plain as day, but it actually cost like twenty grand.`

### 613 · **thermos**（保温杯、保温瓶）
类型 词汇 ｜ 新建 2026-11-06 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**thermos** ＝ 保温杯／保温瓶（让水几个小时都保持热或冷）：`a thermos of hot tea` · `I always bring a thermos to work.`
同一格里的邻居（别串）：water bottle（普通水瓶）· travel mug（带盖的随行咖啡杯）· insulated（保温的，形容词：an insulated bottle）。
判据一句话：中文"保温杯"⇒ thermos。
★ 题型判整句："保温杯"能落到 insulated cup／bottle 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名 thermos。

**怎么发现的**
2026-11-06 学习日 复检第 4 组 [10]（🎓#372 题面"那款联名的保温杯特别难买，我蹲了一个星期才弄到手。"）· 原话
`That collab thermos(背下) was so hard to get my hands on—I spent a week to finally get one.`
她写对了 thermos，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #601 #602 #609 先例）。
判重三步：
　① 目标形式 dedup "thermos" ⇒ 零命中
　② 中文 dedup "保温" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `That collab thermos`，但词不在手边（自己标背下）　　目标：同她原句
找法：说到"保温杯"先落 thermos。

**题面**
"我妈每天出门都要带一个装满热水的保温杯。"（"保温杯"用 **thermos** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My mom takes a thermos full of hot water with her every time she goes out.

- 2026-11-06 ❌ 首犯 · 学习日 复检第 4 组 [10]（🎓#372 题里）· 她标「背下」· 原话 `That collab thermos(背下) was so hard to get my hands on—I spent a week to finally get one.`

### 614 · **monkey see, monkey do**（有样学样；独立成句当评语，⛔ 当动词接在 gonna 后面）
类型 词组 ｜ 新建 2026-11-06
状态 连对0 连错1 上次2026-11-06 未毕业 ｜ 题型 整句

**问题是什么**
**monkey see, monkey do** ＝ "有样学样嘛"，是一句**独立的评语**，挂在主句后面单独说：`Kids copy everything their parents do—monkey see, monkey do.`
⛔ 不接在 gonna／will 后面当动词用；主句里要动词就用 **copy (them)**。
同一格里的邻居（别串）：like father, like son（有其父必有其子）· kids learn by example · 🎓#257 lead by example（大人这边：以身作则）。
判据一句话：想说"孩子会学"⇒ 主句用 copy them；想加一句"有样学样嘛"⇒ 句尾单独挂 monkey see, monkey do。
★ 题型判整句：习语挂在哪儿（句尾独立 vs 当谓语）只在句子里现形；"有样学样"能落到 copy 绕开 ⇒ 正向点名整块。

**怎么发现的**
2026-11-06 学习日 ③ 重答 bank:489 S6 · 原话
`I mean, if parents are constantly cutting the line, kids are obviously gonna monkey see, monkey do.`
习语本身调对了，但当成动词接在 gonna 后面 ⇒ 不地道（⚠️），更地道的 gonna copy them—monkey see, monkey do 是能学的表达 ⇒ §3.2b 建号，判 ❌。
判重三步：
　① 目标形式 dedup "monkey" ⇒ 零命中
　② dedup "lead by example" ⇒ 🎓#257（以身作则，大人那一侧的块）⇒ 否：本条考"有样学样"这个习语的用法
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：kids are obviously gonna monkey see, monkey do　　更地道：kids are obviously gonna copy them—monkey see, monkey do
找法：monkey see, monkey do 前面出现 gonna／will ⇒ 换成 copy them，再把它挂到句尾。

**题面**
"你天天在孩子面前玩手机，他当然也天天玩手机，有样学样嘛。"（"有样学样"用 **monkey see, monkey do** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：If you're on your phone all day in front of your kid, of course he'll be on his phone all day too—monkey see, monkey do.

- 2026-11-06 ❌ 首犯 · 学习日 ③ 重答 bank:489 S6 · ⚠️ 不地道 · 原话 `I mean, if parents are constantly cutting the line, kids are obviously gonna monkey see, monkey do.`

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

