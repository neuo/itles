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

### 630 · **two weeks**（"半个月"；⛔ half a month）
类型 词组 ｜ 新建 2026-11-08
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

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
- 2026-11-09 ❌ 学习日 在池第 2 组 [6] · `It took half a month for my delivery to get here.` —— half a month 又出来了 ⇒ two weeks · 连错 1 → 2
- 2026-11-11 ❌ 学习日 在池第 2 组 [1] · `It took me half a month to get over this cold.` —— 半个月又说成 half a month（第三次）⇒ two weeks
- 2026-11-13 ✅ 学习日 在池第 1 组 [1] · `I spent two weeks traveling in Yunnan` —— 连错 3 → 连对 1

### 641 · **grilled sausage**（烤肠）
类型 词汇 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
烤肠 ＝ **a grilled sausage**（复数 grilled sausages）。
街边小吃一族：`lamb skewers`（羊肉串）· `grilled squid`（烤鱿鱼）· `a savory crepe`（煎饼）。
同一格里的邻居（别串）：hot dog（夹在面包里的才叫 hot dog）。
判据一句话：烤肠单吃、不夹面包 ⇒ grilled sausage。
★ 与 🎓#581 grill 分工：那条考"烤"这个词本身，本条考"烤肠"这个食物名 ⇒ #581 换场景时不再用烤肠。
★ 题型判整句："烤肠"能落到 roast sausage／hot dog，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-11 学习日 在池第 1 组 [5]（#624 题面"楼下那家烤肠五块钱一根，学生放学都去买。"）· 原话
`The grilled sausages（背下） downstairs cost five yuan a pop, and all the students buy them after school.`
她写对了 grilled sausages，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "sausage" ⇒ 全档零命中
　② 中文 dedup "烤肠" ⇒ 零命中；🎓#581 grill（烤）⇒ 考的是词 grill，不是"烤肠"这个名字 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `grilled sausages`，但词不在手边（自己标背下）　　目标：同她原句
找法："烤"＋食物 ⇒ grilled ＋ 那个食物。

**题面**
"孩子们放学一出校门就围着小摊买烤肠。"（"烤肠"用 **grilled sausage** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：As soon as the kids get out of school, they crowd around the stall to buy grilled sausages.

- 2026-11-11 ❌ 首犯 · 学习日 在池第 1 组 [5]（#624 题里）· 她标「背下」· 原话 `The grilled sausages（背下） downstairs cost five yuan a pop, and all the students buy them after school.`
- 2026-11-13 ✅ 学习日 在池第 1 组 [10] · `they crowded around the food stall to buy grilled sausages` —— 连错 1 → 连对 1

### 642 · **off ＝ 不对劲、怪怪的**（feel off · something's off · the milk smells off）
类型 词汇 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**off** 当形容词 ＝ 不太对、不对劲，但说不清哪儿：
　`feel off`（感觉别扭；也指身体有点不舒服：I've been feeling a bit off today）
　`something's off`（有点不对劲）· `the milk smells off`（牛奶闻着坏了）· `his timing was off`（没卡准）
同一格里的邻居（别串）：weird（怪，更泛）· not right（不对）。
判据一句话：想说"不对劲／怪怪的／不在状态" ⇒ feel／seem／smell ＋ off。
★ 题型判整句：off 要挂在 feel／smell／seem 后面才现形。

**怎么发现的**
2026-11-11 学习日 在池第 1 组 [6]（#625 题面"我自行车的车把歪了，骑起来总觉得别扭。"）· 原话
`My bike's handlebars are misaligned, which makes riding it feel totally off(这个 off 的用法学下）.`
她写对了 feel totally off，但自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 grep "feel off／something's off／is off" ⇒ 全档零命中
　② dedup "off" 命中 54 条，全是短语动词（get off · pull off · set off · drop off …）⇒ 不是形容词义 off ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `feel totally off`，但用法不在手边（自己标学下）　　目标：同她原句
找法：中文"别扭／不对劲／怪怪的" ⇒ feel／seem／smell ＋ off。

**题面**
"这牛奶闻着有点不对劲，你别喝了。"（"不对劲"用 **off** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：This milk smells a bit off—don't drink it.

- 2026-11-11 ❌ 首犯 · 学习日 在池第 1 组 [6]（#625 题里）· 她标「这个 off 的用法学下」· 原话 `My bike's handlebars are misaligned, which makes riding it feel totally off.`
- 2026-11-13 ✅ 学习日 在池第 2 组 [1] · `This milk smells a bit off` —— 连错 1 → 连对 1

### 643 · **sugary**（太甜、糖放多了：too sugary · sugary drinks）
类型 词汇 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**sugary** ＝ 糖多、甜得过头（偏贬）：`This cake is way too sugary.` · `sugary drinks`（含糖饮料）。
同一格里的邻居（别串）：sweet（甜，中性，夸也能用）· sickly sweet（甜得发腻）。
判据一句话：嫌糖放多了／说含糖饮料 ⇒ sugary；只是说"甜" ⇒ sweet。
★ 题型判整句："太甜"能落到 too sweet 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-11 学习日 在池第 1 组 [8]（#627 题面"这杯奶茶甜度刚刚好，喝着不腻。"）· 原话
`This milk tea's sweetness is just right, so it doesn't feel heavy or too sugary（背下）.`
她写对了 too sugary，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "sugary" ⇒ 全档零命中
　② 中文 dedup "齁" ⇒ 零命中；#627 taste just right（sugary 只在原话里，考点不同）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `too sugary`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"太甜／齁甜" ⇒ too sugary。

**题面**
"这家店的蛋糕太甜了，吃一口就够了。"（"太甜"用 **sugary** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The cakes at this place are way too sugary—one bite is enough.

- 2026-11-11 ❌ 首犯 · 学习日 在池第 1 组 [8]（#627 题里）· 她标「背下」· 原话 `This milk tea's sweetness is just right, so it doesn't feel heavy or too sugary.`
- 2026-11-13 ✅ 学习日 在池第 2 组 [2] · `The cakes at this place are way too sugary` —— 连错 1 → 连对 1

### 644 · **get over ＋ 病／坏事**（缓过来、好了：get over a cold · get over a breakup）
类型 词组 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**get over ＋ 病／打击** ＝ 从里面缓过来、彻底好了：`get over a cold` · `get over the flu` · `get over a breakup`。
常和 It took me … 连用：`It took me two weeks to get over it.`
同一格里的邻居（别串）：#645 shake off（把小病甩掉，常说"甩不掉"）· recover from（更正式）。
判据一句话：说"病好了／从打击里走出来" ⇒ get over ＋ 那件事。
★ 题型判整句：get over 后面要挂上病或那件事，单翻一个块测不出。

**怎么发现的**
2026-11-11 学习日 在池第 2 组 [1]（#630 题面"我这次感冒拖了半个月才好。"）· 原话
`It took me half a month to get over(和 hake off 一起学下) this cold.`
她写对了 get over，但自己标「和 shake off 一起学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "get over"／"got over" ⇒ 只命中 🎓#429 hold a grudge（get over 只在它的邻居里）⇒ 否
　② 中文 dedup "走出来"／"好了" 不是固定中文块，按英文形式判 ⇒ 无同考点
　③ 保留新建（⛔ 建号当天不测）；与 #645 shake off 分工写在上面

**我错在哪**
她的：写对了 `get over this cold`，但想和 shake off 一起巩固（自己标学下）　　目标：同她原句
找法：中文"好了／缓过来／走出来" ⇒ get over ＋ 那件事。

**题面**
"她跟男朋友分手以后，过了大半年才走出来。"（"走出来"用 **get over** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：It took her more than half a year to get over the breakup with her boyfriend.

- 2026-11-11 ❌ 首犯 · 学习日 在池第 2 组 [1]（#630 题里）· 她标「和 shake off 一起学下」· 原话 `It took me half a month to get over this cold.`
- 2026-11-13 ✅ 学习日 在池第 2 组 [3] · `it took her over half a year to finally get over him` —— 连错 1 → 连对 1

### 645 · **shake off ＋ 小病**（甩掉：I can't shake off this cold）
类型 词组 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**shake off ＋ 小病／坏状态** ＝ 把它甩掉，常用否定说"甩不掉"：
　`I can't seem to shake off this cold.`（这感冒老是好不了）· `shake off the jet lag`（倒过时差来）
同一格里的邻居（别串）：#644 get over（已经好了）。
判据一句话：说"老是甩不掉／好不利索" ⇒ can't shake off ＋ 那个病。
★ 题型判整句：常带 can't seem to 的否定框，靠句子才现形。

**怎么发现的**
2026-11-11 学习日 在池第 2 组 [1]（#630 题里）· 她在 get over 后标「和 hake off 一起学下」（hake off ＝ shake off，拼写不算）。
她没在句子里用它，点名要学 ⇒ §2③ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "shake off" ⇒ 全档零命中
　② 与 #644 get over：get over ＝ 好了，shake off ＝ 甩掉／甩不掉 ⇒ 两个词组 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：没用到，点名要学　　目标：`I can't seem to shake off this cold.`
找法：中文"甩不掉／好不利索" ⇒ can't shake off。

**题面**
"这次咳嗽拖了好久，怎么都好不利索。"（"好不利索"用 **shake off** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I've had this cough for ages and I just can't shake it off.
★ 首次出题给整块（§6② 她点名要学 ⇒ 练）。

- 2026-11-11 ❌ 首犯 · 学习日 在池第 2 组 [1]（#630 题里）· 她标「和 hake off 一起学下」· 原话 `It took me half a month to get over this cold.`
- 2026-11-13 ✅ 学习日 在池第 2 组 [4] · `I just can't seem to shake it off` —— 连错 1 → 连对 1

### 646 · **play matchmaker**（当红娘、撮合别人）
类型 词组 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**play matchmaker (for sb)** ＝ 当红娘、帮人牵线：`My aunt loves playing matchmaker.`
同一格里的邻居（别串）：set sb up (with sb)（给人介绍对象：She set me up with her coworker.）。
判据一句话：说"撮合／牵线／当红娘" ⇒ play matchmaker。
★ 题型判整句："当红娘"能落到 set them up 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-11 学习日 在池第 2 组 [2]（#631 题面"她想撮合两个朋友，结果适得其反，现在俩人都不理她了。"）· 原话
`She wanted to play matchmaker(学下这个词） for two friends, which backfired big time; neither of them speaks to her anymore.`
她写对了 play matchmaker，但自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "matchmaker" ⇒ 全档零命中
　② 中文 dedup "撮合" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `play matchmaker`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"撮合／当红娘" ⇒ play matchmaker。

**题面**
"我姑姑最爱给年轻人当红娘，可惜一对都没成。"（"当红娘"用 **matchmaker** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My aunt loves playing matchmaker for young people, but none of her matches has worked out.

- 2026-11-11 ❌ 首犯 · 学习日 在池第 2 组 [2]（#631 题里）· 她标「学下这个词」· 原话 `She wanted to play matchmaker for two friends, which backfired big time; neither of them speaks to her anymore.`
- 2026-11-13 ✅ 学习日 在池第 2 组 [5] · `My aunt loves playing matchmaker for young people` —— 连错 1 → 连对 1

### 647 · **be sick of ＋ 事／人**（受够了、烦透了：I'm sick of waiting）
类型 搭配 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**be sick of ＋ 东西／-ing** ＝ 受够了、烦透了：`I'm sick of his excuses.` · `I'm sick of waiting.`
加强版：`sick and tired of`。
同一格里的邻居（别串）：can't stand ＋ 东西（受不了，意思接近）· can't bear（偏书面，口语少用）。
判据一句话：烦了很久、再也不想忍 ⇒ be sick of ＋ 那件事。
★ 题型判整句：介词 of 和后面的 -ing 要靠句子才现形。

**怎么发现的**
2026-11-11 学习日 在池第 2 组 [9]（#638 题面"他每次开会都拼命夸领导，大家都看不下去了。"）· 原话
`Every single meeting, he's constantly flattering the boss, and everyone is completely sick of（这个短语又忘了，召回下，本来我想用 bear) it.`
她最后写对了 sick of，但说"又忘了、本来想用 bear" ⇒ §2③ 她说不会 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "sick of" ⇒ 🎓#420 burnt out · 🎓#6 情态副词 —— sick of 只在邻居／例句里，不是考点 ⇒ 否
　② dedup "can't stand"／"受不了" ⇒ 只命中 🎓#494 can't bring myself to do（狠不下心，另一个意思）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：一开始调出 bear，查了才写出 `sick of`　　目标：`everyone is completely sick of it`
找法：中文"受够了／烦透了／看不下去" ⇒ be sick of ＋ 那件事。

**题面**
"我真受够了每天挤地铁上班。"（"受够了"用 **sick of** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I'm so sick of cramming onto the subway to get to work every day.

- 2026-11-11 ❌ 首犯 · 学习日 在池第 2 组 [9]（#638 题里）· 她标「这个短语又忘了，召回下，本来我想用 bear」· 原话 `everyone is completely sick of it.`
- 2026-11-13 ✅ 学习日 在池第 2 组 [6] · `I'm so sick of squeezing onto the subway` —— 连错 1 → 连对 1

### 648 · **commit a foul ／ foul sb**（体育比赛里犯规）
类型 搭配 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**foul** ＝ 比赛里的犯规（名词），动词搭配 **commit a foul**：`He committed a foul in the last minute.`
口语也直接当动词：`He fouled the other player.`（对那个球员犯规）；裁判吹犯规：`the referee called a foul`。
同一格里的邻居（别串）：break the rules（违反规则，泛指）。
判据一句话：体育比赛里的"犯规" ⇒ foul（commit a foul ／ foul sb）。
★ 题型判整句："犯规"能落到 break the rules 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-11 学习日 复检第 3 组 [5]（#585 题面"裁判明明看到他犯规了，却故意不管。"）· 原话
`The referee saw him commit the foul(这个词学下), but decided to just look the other way.`
她写对了 commit the foul，但自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "foul" ⇒ 🎓#553 stench · 🎓#592 back up —— foul 在那里是"臭"，只出现在例句里 ⇒ 另一个意思，否
　② 中文 dedup "犯规" ⇒ 命中的都是"教练犯规"留痕行，没有体育犯规的考点 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `commit the foul`，但词不在手边（自己标学下）　　目标：同她原句（泛指时 commit a foul）
找法：中文"犯规" ⇒ commit a foul，或者 foul ＋ 人。

**题面**
"他上半场就犯了三次规，被教练换下去了。"（"犯规"用 **foul** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：He committed three fouls in the first half, so the coach took him out.

- 2026-11-11 ❌ 首犯 · 学习日 复检第 3 组 [5]（#585 题里）· 她标「这个词学下」· 原话 `The referee saw him commit the foul, but decided to just look the other way.`
- 2026-11-13 ✅ 学习日 在池第 2 组 [7] · `He committed three fouls in the first half alone` —— 连错 1 → 连对 1

### 649 · **pirated**（盗版的：pirated books · a pirated copy）
类型 词汇 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**pirated ＋ 东西** ＝ 盗版的：`pirated books` · `pirated DVDs` · `a pirated copy`（一份盗版）。
动词 pirate ＝ 盗版；名词 piracy ＝ 盗版行为（online piracy）。
同一格里的邻居（别串）：fake／knockoff（仿冒的商品，名牌包、鞋那种假货）。
判据一句话：书、电影、软件的"盗版" ⇒ pirated；商品的"假货" ⇒ fake／knockoff。
★ 题型判整句："盗版"能落到 fake 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-11 学习日 复检第 3 组 [10]（#590 题面"他在网上卖盗版书，最后被警察抓了。"）· 原话
`He got busted by the cops in the end for selling pirated(背下) books online.`
她写对了 pirated，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "pirate" ⇒ 全档零命中
　② 中文 dedup "盗版" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `pirated books`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"盗版" ⇒ pirated ＋ 东西。

**题面**
"我小时候家里那些动画片光盘全是盗版的。"（"盗版"用 **pirated** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：All the cartoon DVDs we had at home when I was a kid were pirated.

- 2026-11-11 ❌ 首犯 · 学习日 复检第 3 组 [10]（#590 题里）· 她标「背下」· 原话 `He got busted by the cops in the end for selling pirated books online.`
- 2026-11-13 ✅ 学习日 在池第 2 组 [8] · `All the cartoon DVDs we had at home when I was a kid were pirated.` —— 连错 1 → 连对 1

### 650 · **tucked away** ＋ 地点（藏在不起眼、不好找的地方：a café tucked away in an alley）
类型 词组 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**be tucked away ＋ 地点** ＝ 藏在（偏僻、不显眼的地方），带一点"不好找、但找到了挺惊喜"的味道：
`a little café tucked away in an alley` · `The village is tucked away in the mountains.`
常直接挂在名词后面当修饰：`a guesthouse tucked away in …`
同一格里的邻居（别串）：hidden（藏着，中性，只说看不见）· remote（偏远，只说离得远）。
判据一句话：想说"藏在…里头、不好找的那种小地方" ⇒ tucked away in ＋ 地点。
★ 题型判整句："藏着"能落到 hidden 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-11 学习日 ③ 重答 bank:434（P2 · Describe a home that you like to visit but do not want to live in）S1 · 原话
`I'd like to talk about a guesthouse tucked away（这个词学下） in a super quiet plateau town out in western Sichuan.`
她写对了 tucked away in，但自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "tucked"／"tuck" ⇒ 全档零命中；邻居 dedup "hidden" ⇒ 零命中
　② 中文 dedup "藏在"／"偏僻" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `a guesthouse tucked away in …`，但词不在手边（自己标学下）　　目标：同她原句
找法：说到"藏在"某处的店／房子／村子，先落 tucked away，后面接 in ＋ 地点。

**题面**
"我们学校后面的巷子里藏着一家特别好吃的面馆。"（"藏着"用 **tucked away** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：There's a really good noodle place tucked away in the alley behind our school.

- 2026-11-11 ❌ 首犯 · 学习日 ③ 重答 bank:434 S1 · 她标「这个词学下」· 原话 `I'd like to talk about a guesthouse tucked away in a super quiet plateau town out in western Sichuan.`
- 2026-11-13 ✅ 学习日 在池第 2 组 [9] · `an amazing little noodle shop tucked away in the alley` —— 连错 1 → 连对 1

### 651 · **spotless**（一尘不染、干净得挑不出毛病：The kitchen is spotless.）
类型 词汇 ｜ 新建 2026-11-11 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**spotless** ＝ 干净到一点污渍都没有，比 very clean 强一档：`The kitchen is spotless.` · `keep the place spotless`。
同一格里的邻居（别串）：clean（中性的"干净"）· neat／tidy（整齐，说的是"乱不乱"，不是"脏不脏"）。
判据一句话：夸"一尘不染、干净得发亮" ⇒ spotless；夸"收拾得整齐" ⇒ neat／tidy。
★ 题型判整句："一尘不染"能落到 very clean 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。
★ 与 🎓#227（clear ≠ clean）分工：那条是形容词选词（清澈 vs 干净），本条是"干净"的程度词 ⇒ 两条，各走各的。

**怎么发现的**
2026-11-11 学习日 ③ 重答 bank:434 S4 · 原话
`It definitely has a dated, old-school vibe to it, though everything is spotless（这个词学下） and neat.`
她写对了 spotless，但自己标「这个词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "spotless" ⇒ 全档零命中；邻居 dedup "tidy" ⇒ 🎓#51 put away · 🎓#190 clear the table · 🎓#206（历史字样）⇒ 都否
　② 中文 dedup "一尘不染"／"整洁" ⇒ 零命中；"干净" ⇒ 🎓#227 clear ≠ clean（选词，不是程度）等 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `everything is spotless`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文是"一尘不染／干净得发亮" ⇒ spotless。

**题面**
"我妈每天都要拖两遍地，家里总是一尘不染。"（"一尘不染"用 **spotless** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My mom mops the floor twice a day, so the house is always spotless.

- 2026-11-11 ❌ 首犯 · 学习日 ③ 重答 bank:434 S4 · 她标「这个词学下」· 原话 `It definitely has a dated, old-school vibe to it, though everything is spotless and neat.`
- 2026-11-13 ✅ 学习日 在池第 2 组 [10] · `our house is always spotless` —— 连错 1 → 连对 1

### 652 · **a spoonful of ＋ 东西**（一勺：two spoonfuls of salt）
类型 词汇 ｜ 新建 2026-11-13 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**spoonful** ＝ 一勺的量（spoon ＋ -ful）：`a spoonful of sugar` · `two spoonfuls of salt`。
同族量词：a handful of（一把）· a mouthful of（一口）· a cupful of（一杯的量）。
同一格里的邻居（别串）：spoon 是勺子这个东西（a spoon）；说"几勺 X"要用 spoonful。
判据一句话：说"几勺 X" ⇒ 数字 ＋ spoonful(s) of ＋ X。
★ 题型判整句："一勺"能落到 a spoon of 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 在池第 1 组 [6]（#637 题面"这碗汤一点味道都没有，我又加了两勺盐。"）· 原话
`This bowl of soup was way too bland, so I added two more spoonfuls(背下) of salt.`
她写对了 spoonfuls，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "spoonful" ⇒ 全档零命中
　② 中文 dedup "勺" ⇒ 只命中 🎓#74 make do with（历史行里的字样，考点是"将就"）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `two more spoonfuls of salt`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"几勺" ⇒ 数字 ＋ spoonful(s) of。

**题面**
"我每天早上喝咖啡都要放一勺糖。"（"一勺"用 **spoonful** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I put a spoonful of sugar in my coffee every morning.

- 2026-11-13 ❌ 首犯 · 学习日 在池第 1 组 [6]（#637 题里）· 她标「背下」· 原话 `This bowl of soup was way too bland, so I added two more spoonfuls of salt.`

### 653 · **from ＋ 另一个介词短语**（from across the yard · from behind the door · from under the bed）
类型 结构 ｜ 新建 2026-11-13 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
中文"从 X 那头／后面／底下（过来）" ⇒ **from 后面直接再接一个介词短语**：
　`from across the street`（从街对面）· `from behind the door`（从门后）· `from under the bed`（从床底下）
　`from inside the house`（从屋里）· `from over there`（从那边）
from 管"起点"，后面那个介词管"起点在哪个方位"，两个各干各的，⛔ 不是重复。
判据一句话：中文是"从 ＋ 地方 ＋ 方位词（那头／后面／底下／里面）" ⇒ from ＋ 方位介词 ＋ 地方。
★ 与 🎓#439 comeback 分工：那条邻居里的 come from behind ＝ 落后反超（固定说法），本条是方位介词叠用 ⇒ 两条。
★ 题型判整句：考点是两个介词在句子里挂在一起，单翻一个块测不出。

**怎么发现的**
2026-11-13 学习日 在池第 1 组 [9]（#640 题面"我一喊它的名字，狗就从院子那头跑过来了。"）· 原话
`The second I called its name, the dog came running over from across the yard（这种 双重介词 的用法得学下).`
她写对了 from across the yard，但自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "from across" ⇒ 全档零命中；dedup "from under" ⇒ 零命中
　② dedup "from behind" ⇒ 只命中 🎓#439 comeback（come from behind ＝ 落后反超）⇒ 考点是固定说法，不是介词叠用 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `from across the yard`，但结构不在手边（自己标学下）　　目标：同她原句
找法：中文"从…那头／后面／底下" ⇒ 先说 from，再接那个方位介词。

**题面**
"我听见有人从门后面小声喊我的名字。"（"从门后面"用 **from behind** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I heard someone whispering my name from behind the door.
★ 首次出题给整块（§6② 她点名要学 ⇒ 练），之后换 across／under／inside 等别的方位。

- 2026-11-13 ❌ 首犯 · 学习日 在池第 1 组 [9]（#640 题里）· 她标「这种 双重介词 的用法得学下」· 原话 `The second I called its name, the dog came running over from across the yard.`

### 654 · **more than enough**（够了还有富余、绰绰有余）
类型 词组 ｜ 新建 2026-11-13 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**more than enough** ＝ 不光够，还多出来：`one bite is more than enough` · `We have more than enough food.`
同族：more than happy to（非常乐意）。
同一格里的邻居（别串）：enough 单用 ＝ 刚好够。
判据一句话：中文"绰绰有余／够了还多／一口就够了（语气是嫌多）" ⇒ more than enough。
★ 题型判整句："绰绰有余"能落到 plenty 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 在池第 2 组 [2]（#643 题面"这家店的蛋糕太甜了，吃一口就够了。"）· 原话
`The cakes at this place are way too sugary; one bite is more than enough（这个 more than  + enough 可以学下).`
她写对了 more than enough，但自己标「可以学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "more than enough" ⇒ 全档零命中
　② 中文 dedup "绰绰有余" 未命中任何考点相关条目
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `one bite is more than enough`，但块不在手边（自己标学下）　　目标：同她原句
找法：想说"够了还多" ⇒ 在 enough 前面加 more than。

**题面**
"这些菜我们四个人吃绰绰有余。"（"绰绰有余"用 **more than enough** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：This is more than enough food for the four of us.

- 2026-11-13 ❌ 首犯 · 学习日 在池第 2 组 [2]（#643 题里）· 她标「这个 more than + enough 可以学下」· 原话 `The cakes at this place are way too sugary; one bite is more than enough.`

### 655 · **the better part of ＋ 时间段**（大半年：the better part of a year）
类型 词组 ｜ 新建 2026-11-13
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**the better part of a year** ＝ 一年里的大部分 ＝ 中文"大半年"；同理 the better part of a day（大半天）· the better part of an hour（大半个小时）。
同一格里的邻居（别串）：半年 ⇒ six months（half a year 能懂但少说，同 #630 "半个月 ⇒ two weeks"）。
判据一句话：中文"大半 ＋ 时间段" ⇒ the better part of ＋ 那个时间段。
★ 题型判整句："大半年"能落到 over six months 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 在池第 2 组 [3]（#644 题面"她跟男朋友分手以后，过了大半年才走出来。"）· 原话
`After she broke up with her boyfriend, it took her over half a year to finally get over him.`
⚠️ 不地道：over half a year 能懂，"大半年"英语有现成块 ⇒ §3.2b 能学的表达 ⇒ 建号。
判重三步：
　① 目标形式 dedup "better part" ⇒ 全档零命中
　② 中文 dedup "大半年" ⇒ 只命中 #644 get over 的题面（考点是 get over）⇒ 否；邻居 #630 two weeks 是"半个月"的说法，本条是"大半 ＋ 时间"⇒ 两条
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：it took her over half a year　　更地道：it took her the better part of a year
找法：中文里出现"大半年／大半天" ⇒ 先想 the better part of。

**题面**
"为了考这个证，我花了大半年时间准备。"（"大半年"用 **the better part of** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：I spent the better part of a year preparing for this certificate.

- 2026-11-13 ❌ 首犯 · 学习日 在池第 2 组 [3]（#644 题里）· ⚠️ 不地道 · 原话 `After she broke up with her boyfriend, it took her over half a year to finally get over him.`

### 656 · **a match**（红娘撮合成的一对：none of her matches worked out）
类型 词汇 ｜ 新建 2026-11-13
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

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

### 657 · **take sb off**（比赛里把人换下场；⛔ change sb out）
类型 词组 ｜ 新建 2026-11-13
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**take sb off** ＝ 教练把球员换下场：`The coach took him off at half-time.`
口语也说 sub sb off／sub sb out；换上场 ⇒ put sb on／bring sb on。
同一格里的邻居（别串）：change 不这么用；换衣服是 change out of（🎓#411）。
判据一句话：比赛里"换下去" ⇒ take sb off。
★ 题型判整句：考点是 take 和 off 夹着人挂在一起，单翻一个块测不出。

**怎么发现的**
2026-11-13 学习日 在池第 2 组 [7]（#648 题面"他上半场就犯了三次规，被教练换下去了。"）· 原话
`He committed three fouls in the first half alone, so the coach changed him out.`
⚠️ 不地道：change 在这里搭不上 ⇒ §3.2b 她的词搭不上 ⇒ 建号。
判重三步：
　① 目标形式 dedup "sub"／"subbed"／"take him off" ⇒ 全档零命中
　② 中文 dedup "换下" ⇒ 命中 🎓#411 change out of（换衣服）· 🎓#513 pajamas（换睡衣）· 🎓#633（字样）⇒ 都不是比赛换人 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：the coach changed him out　　更地道：the coach took him off
找法：比赛换人 ⇒ take off（下）／put on（上），⛔ 不用 change。

**题面**
"他第二十分钟就受了伤，教练只好把他换下场。"（"换下场"用 **take off** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：He got injured in the twentieth minute, so the coach had to take him off.

- 2026-11-13 ❌ 首犯 · 学习日 在池第 2 组 [7]（#648 题里）· ⚠️ 不地道 · 原话 `He committed three fouls in the first half alone, so the coach changed him out.`

### 658 · **we／us ＋ 名词**（我们这些…：we students · all of us kids）
类型 结构 ｜ 新建 2026-11-13 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
英语可以把 **we／us 直接放在名词前面**，意思是"我们这些 X"：`we students` · `us kids` · `we office workers`。
主格宾格跟着位置走：当主语 ⇒ **we**（`We kids stopped messing around.`）；在介词／动词后面 ⇒ **us**（`all of us kids` · `for us parents`）。
同一格里的邻居（别串）：those of us who …（我们当中那些…的人）。
判据一句话：中文"我们这些／我们几个 ＋ 身份" ⇒ we／us ＋ 那个名词，主语位用 we、宾语位用 us。
★ 题型判整句：考点是 we／us 跟着句中位置变，单翻一个块测不出。

**怎么发现的**
2026-11-13 学习日 复检第 3 组 [1]（#600 题面"我爷爷严厉地看了我们一眼，我们几个孩子立刻就不闹了。"）· 原话
`My grandpa gave us one stern look, and all of us kids（us + noun. 的用法学下) stopped messing around(这个词组学下) right away.`
她写对了 all of us kids，但自己标「学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "us kids"／"we kids" ⇒ 全档零命中
　② 中文 dedup "我们这些" 未见同考点条目
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `all of us kids`，但结构不在手边（自己标学下）　　目标：同她原句
找法：中文"我们这些 X" ⇒ we／us ＋ X；先看它当主语还是宾语，再定 we 还是 us。

**题面**
"我们这些上班族周末只想在家睡觉。"（"我们这些上班族"用 **we** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：We office workers just want to sleep in on weekends.
★ 换场景时轮换主语位（we）和宾语位（us）。

- 2026-11-13 ❌ 首犯 · 学习日 复检第 3 组 [1]（#600 题里）· 她标「us + noun. 的用法学下」· 原话 `My grandpa gave us one stern look, and all of us kids stopped messing around right away.`

### 659 · **mess around**（瞎闹、胡闹、不干正事瞎玩）
类型 词组 ｜ 新建 2026-11-13 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**mess around** ＝ 不干正事、瞎闹瞎玩：`Stop messing around and do your homework.`
同一格里的邻居（别串）：mess up（搞砸）· make a mess（弄乱）。
判据一句话：中文"瞎闹／胡闹／不干正事瞎玩" ⇒ mess around。
★ 题型判整句："瞎闹"能落到 fool around／play around 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 复检第 3 组 [1]（#600 题面"我爷爷严厉地看了我们一眼，我们几个孩子立刻就不闹了。"）· 原话
`My grandpa gave us one stern look, and all of us kids（us + noun. 的用法学下) stopped messing around(这个词组学下) right away.`
她写对了 messing around，但自己标「这个词组学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "mess around" ⇒ 命中 #12（时态，形态类）· 🎓#206（书面词降级）—— 都只是历史行里的字样，考点无关 ⇒ 否；"messing around" 零命中
　② 中文 dedup "胡闹"／"瞎闹" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `stopped messing around`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"瞎闹／胡闹" ⇒ mess around。

**题面**
"老师一走出教室，后排几个男生就开始瞎闹。"（"瞎闹"用 **mess around** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：As soon as the teacher left the classroom, the boys in the back started messing around.

- 2026-11-13 ❌ 首犯 · 学习日 复检第 3 组 [1]（#600 题里）· 她标「这个词组学下」· 原话 `My grandpa gave us one stern look, and all of us kids stopped messing around right away.`

### 660 · **ache**（隐隐地疼、酸疼：my back aches · left my back aching）
类型 词汇 ｜ 新建 2026-11-13 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**ache** ＝ 持续的、闷闷的疼（动词）：`My back aches.` · `My legs were aching.` · `it left my back aching`。
名词也常用：a headache · a stomachache · a toothache。
同一格里的邻居（别串）：hurt（泛指疼，最通用）· sore（肌肉酸痛：My legs are sore.）。
判据一句话：中文"酸疼／一直隐隐地疼" ⇒ ache。
★ 题型判整句："酸疼"能落到 hurt／sore 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 复检第 3 组 [4]（#603 题面"那辆旧公交车一路上特别颠，坐得我腰都疼了。"）· 原话
`That old bus was super bumpy the whole way—it left my lower back aching(这个词也学下).`
她写对了 aching，但自己标「这个词也学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "aching"／"ache" ⇒ 全档零命中
　② 中文 dedup "酸疼" 未见同考点条目
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `it left my lower back aching`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"酸疼／闷闷地疼" ⇒ ache。

**题面**
"搬了一整天家，第二天我浑身酸疼。"（"酸疼"用 **ache** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：After a whole day of moving, I was aching all over the next day.

- 2026-11-13 ❌ 首犯 · 学习日 复检第 3 组 [4]（#603 题里）· 她标「这个词也学下」· 原话 `That old bus was super bumpy the whole way—it left my lower back aching.`

### 661 · **all over the place**（没规律、乱、变来变去：The weather's been all over the place.）
类型 词组 ｜ 新建 2026-11-13 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**all over the place** 两个意思：① 到处都是（`toys all over the place`）② 没规律、乱、变来变去（`The weather's been all over the place.` · `My sleep schedule is all over the place.`）。
本条考 ②。
同一格里的邻居（别串）：🎓#496 be overrun with（到处都是坏东西，泛滥）。
判据一句话：中文"没个准／没规律／一会儿这样一会儿那样" ⇒ be all over the place。
★ 题型判整句："没规律"能落到 irregular 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 复检第 3 组 [10]（#271 题面②"这阵子天气变化特别大。"）· 原话
`I've been learning how to cook recently. And the weather has been all over the place(这个短语学下) lately.`
她写对了 all over the place，但自己标「这个短语学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "all over the place" ⇒ 命中 🎓#496 be overrun with（邻居里提到"到处都是"可落到 all over the place）· 🎓#585 look the other way（例句字样）⇒ 考点都不是这个块 ⇒ 否
　② 中文 dedup "没规律" 未见同考点条目
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `has been all over the place`，但块不在手边（自己标学下）　　目标：同她原句
找法：说"没个准／乱七八糟" ⇒ be all over the place。

**题面**
"他的作息完全没规律，有时候凌晨三点睡，有时候晚上九点就睡了。"（"完全没规律"用 **all over the place** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：His sleep schedule is all over the place—sometimes he goes to bed at 3 a.m., sometimes at 9 p.m.

- 2026-11-13 ❌ 首犯 · 学习日 复检第 3 组 [10]（#271 题里）· 她标「这个短语学下」· 原话 `I've been learning how to cook recently. And the weather has been all over the place lately.`

### 662 · **take attendance**（上课点名：看一遍谁来了）
类型 词组 ｜ 新建 2026-11-13 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**take attendance** ＝ 课上点名、看谁到了：`The teacher takes attendance at the start of every class.`
英式也说 take the register；口语也说 call roll。
同一格里的邻居（别串）：attend（出席、参加）· be marked absent（被记缺勤）。
判据一句话：中文"上课点名" ⇒ take attendance。
★ 题型判整句："点名"能落到 call names 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 复检第 4 组 [1] 打包 a（#608 题面"开学第一天站在讲台上点名的那位班主任"）· 原话
`the homeroom teacher standing at the stage taking attendance(这个短语学下)  on the first day of school`
她写对了 taking attendance，但自己标「这个短语学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "attendance" ⇒ 全档零命中
　② 中文 dedup "点名" ⇒ 命中的全是题面里的「正向点名」字样（出题术语），不是这个考点 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `taking attendance`，但块不在手边（自己标学下）　　目标：同她原句
找法：中文"上课点名" ⇒ take attendance。

**题面**
"我们教授每节课一开始都要点名，迟到的直接记缺勤。"（"点名"用 **attendance** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Our professor takes attendance at the start of every class, and anyone who's late gets marked absent.

- 2026-11-13 ❌ 首犯 · 学习日 复检第 4 组 [1] 打包 a（#608 题里）· 她标「这个短语学下」· 原话 `the homeroom teacher standing at the stage taking attendance on the first day of school`

### 663 · **at the front of the classroom**（教室里的"讲台上／讲台前"；⛔ at the stage）
类型 搭配 ｜ 新建 2026-11-13
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
教室里的"讲台" ⇒ **the front of the classroom**：`stand at the front of the classroom` · `come up to the front`。
同一格里的邻居（别串）：stage ＝ 剧场、礼堂的舞台（on stage）· podium ＝ 演讲用的讲桌。
判据一句话：教室里说"站在讲台上／上讲台" ⇒ at／to the front of the classroom。
★ 题型判整句："讲台"能落到 platform／podium，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 复检第 4 组 [1] 打包 a（#608 题面"开学第一天站在讲台上点名的那位班主任"）· 原话
`the homeroom teacher standing at the stage taking attendance(这个短语学下)  on the first day of school`
⚠️ 不地道：stage 在教室里搭不上（那是舞台）⇒ §3.2b 她的词搭不上 ⇒ 建号。
判重三步：
　① 目标形式 dedup "front of the classroom" ⇒ 全档零命中；"podium" ⇒ 零命中
　② 中文 dedup "讲台" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：standing at the stage　　更地道：standing at the front of the classroom
找法：教室里的讲台 ⇒ the front of the classroom，⛔ 不用 stage。

**题面**
"老师让我上讲台把这道题写在黑板上。"（"上讲台"用 **front** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：The teacher asked me to come up to the front and write the answer on the board.

- 2026-11-13 ❌ 首犯 · 学习日 复检第 4 组 [1] 打包 a（#608 题里）· ⚠️ 不地道 · 原话 `the homeroom teacher standing at the stage taking attendance on the first day of school`

### 664 · **bestie**（闺蜜、最好的朋友，口语）
类型 词汇 ｜ 新建 2026-11-13 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**bestie** ＝ best friend 的口语说法，朋友之间常用：`my bestie and I`。
同义：best friend · BFF。
判据一句话：中文"闺蜜／最铁的朋友（口语）" ⇒ bestie。
★ 题型判整句："闺蜜"能落到 best friend 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 复检第 4 组 [2]（#609 题面"我闺蜜最近逢人就夸她新找的那家理发店。"）· 原话
`My bestie(背下) hasn't stopped raving about this new hair salon she found to everyone she meets.`
她写对了 bestie，但自己标「背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "bestie" ⇒ 全档零命中；"best friend" ⇒ 只在 🎓#537 put together · 🎓#557 frost 的例句里 ⇒ 否
　② 中文 dedup "闺蜜" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `My bestie`，但词不在手边（自己标背下）　　目标：同她原句
找法：中文"闺蜜" ⇒ bestie。

**题面**
"我跟闺蜜每年都要一起出去旅行一次。"（"闺蜜"用 **bestie** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My bestie and I take a trip together every year.

- 2026-11-13 ❌ 首犯 · 学习日 复检第 4 组 [2]（#609 题里）· 她标「背下」· 原话 `My bestie hasn't stopped raving about this new hair salon she found to everyone she meets.`

### 665 · **side character**（配角；演员层面 ⇒ a supporting role）
类型 词汇 ｜ 新建 2026-11-13 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-11-13 未毕业 ｜ 题型 整句

**问题是什么**
**side character** ＝ 配角（故事里的次要角色）；主角 ⇒ main character／the lead。
演员层面说 a supporting role（演配角：play a supporting role）。
判据一句话：说故事里的"配角" ⇒ side character；说演员演的戏份 ⇒ supporting role。
★ 题型判整句："配角"能落到 minor character 绕开，词组题又不许给英文提示 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-11-13 学习日 复检第 4 组 [10]（#542 题面"那个配角的背景故事比主角的还感人。"）· 原话
`That side character's(配角单词学下) backstory is even more touching than the main character's.`
她写对了 side character，但自己标「配角单词学下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 #634 先例）。
判重三步：
　① 目标形式 dedup "side character" ⇒ 全档零命中；"supporting" ⇒ 只命中 🎓#455 underprivileged（例句字样）⇒ 否
　② 中文 dedup "配角" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 `That side character's backstory`，但词不在手边（自己标学下）　　目标：同她原句
找法：中文"配角" ⇒ side character。

**题面**
"这部动画里我最喜欢的不是主角，是那个话很多的配角。"（"配角"用 **side character** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My favorite character in this cartoon isn't the main character—it's that chatty side character.

- 2026-11-13 ❌ 首犯 · 学习日 复检第 4 组 [10]（#542 题里）· 她标「配角单词学下」· 原话 `That side character's backstory is even more touching than the main character's.`

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

