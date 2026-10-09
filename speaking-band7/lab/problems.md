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

### 366 · make bank（赚大钱，口语俚语；make absolute bank ＝ 赚翻了）
类型 词组 ｜ 新建 2026-09-29 ｜ ⭐ 她点名要背
状态 连对2 连错0 上次2026-10-08 ｜ **回潮 2026-10-05**（10-02 毕业 → 10-05 复检写成 `made a bank`，bank 前面加了冠词，撤销毕业、连对清零）｜ **🎓 已毕业 2026-10-08**（连对2 ＝ 10-07 ＋ 10-08；10-05 回潮后第二次毕业）｜ 题型 整句

**问题是什么**
**make bank** ＝ 赚很多钱（口语俚语）；加强版 **make absolute bank** ＝ 赚翻了。bank 这里不加冠词。
同一格里的邻居（别串）：make a fortune（发大财，偏正式）· make good money（挣得不错）
判据一句话：口语里说"赚翻了"⇒ making (absolute) bank。

**怎么发现的**
2026-09-29 学习日 新题 bank:534：她写 `people working on large-language-model are making absolute bank(背一下)` —— 她点名要背。
判重三步：
　① dedup "make bank" ⇒ 零命中
　② dedup "赚大钱" ⇒ 零命中
　③ 保留新建

**我错在哪**
她的：用对了，点名要背（⭐ 不是纠错）
找法：想说"赚翻了"，落 making absolute bank（bank 前面不加 a／the）。
★ 10-05、10-06 两次都写成 `made a bank`：带 absolute 的两次从没加过 a，光秃秃一个 bank 时才冒出 a。
　找法补一句：这里的 bank ＝ money，made money 不说 made a money ⇒ bank 前面也不放 a。

**题面**
"今年做直播带货的那几个主播都赚翻了。"（"赚翻了"用 **bank** 说）

- 2026-09-29 新建 · 学习日新题 bank:534 · 她点名要背 · 原话 `people working on large-language-model are making absolute bank(背一下)`
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  make a killing／make a fortune 都合法 ⇒ 改整句、点名 bank，make 与不加冠词留给她；换成直播带货场景
- 2026-09-30 ✅ 付息日 a 段在池第 1 组 [9] · `This living shopping hosts are making absolute bank this year.`（living 另建 #376）
- 2026-10-02 ✅ 学习日 在池第 2 组 [9] · `That boba shop right outside the school gate makes absolute bank every summer.` —— makes absolute bank，bank 前不加冠词。连对 1 → 2 ⇒ **毕业**
- 2026-10-05 ❌ 学习日 复检第 3 组 [6]（题面"那家网红餐厅开业第一个月就赚翻了"）· `That viral restaurant made a bank in its very first month.` —— make bank 的 bank 前面加了 a ⇒ **回潮**
  最小改 `That viral restaurant made bank in its very first month.`　更好版 `… made absolute bank …`
  ❌ make bank 里的 bank 是俚语"一大笔钱"，不加冠词；加了 a 像"开了一家银行"
- 2026-10-06 ❌ 学习日 在池第 1 组 [2]（题面"他靠倒卖二手球鞋赚翻了"）· `He made a bank reselling second-hand sneakers.` —— bank 前面又加了 a（10-05 同一个错）。连错 1 → 2
  最小改 `He made bank reselling second-hand sneakers.`　更好版 `He made absolute bank reselling second-hand sneakers.`
  ❌ 这里的 bank ＝ 钱，跟 money 一样不可数（made money 不说 made a money）；带 absolute 的两次都没加 a，光秃秃一个 bank 时才冒出 a
- 2026-10-07 ✅ 学习日 在池第 1 组 [1]（题面"我表姐开宠物美容店，这两年赚了大钱"）· `My cousin runs a pet grooming shop, and she's made bank over the last two years.` —— 光秃秃的 bank，前面没加 a。连错 2 → 连对 1
- 2026-10-08 ✅ 付息日 a 段在池第 1 组 [1] · `My friend got into cross-border（加入 transnational 的条目做对比） e-commerce last year and made bank.` —— made bank，bank 前面没加 a。连对 1 → 2 ⇒ **毕业**（10-05 回潮后第二次毕业）
  ｜她要求「加入 transnational 的条目做对比」⇒ 新建 #432

### 413 · on the house（店家请客、不收钱）
类型 词组 ｜ 新建 2026-10-06 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-08 ｜ **🎓 已毕业 2026-10-08**（连对2 ＝ 10-07 ＋ 10-08）｜ 题型 整句

**问题是什么**
**on the house** ＝ 店家请的、免费送的（饭店／酒吧／咖啡店）：The drinks are on the house. ／ a dessert on the house。
同一格里的邻居（别串）：free（大白话"免费"）· complimentary（酒店、航空那种正式的"赠送"）· It's on me.（我请客 —— 个人请客用 on me，店家请客才用 on the house）。
判据一句话：说"店家送的、不收钱" ⇒ on the house；它自己就是"免费"，⛔ 前面不再加 free。
★ 题型判整句：中文"店家送的"翻成 free／complimentary 都合法，孤立翻块映射不回唯一的 on the house ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 在池第 1 组 [7]（#401 题"吃完饭饭店免费送的一份果盘"）· 原话
`a free fruit platter on the house（这个词组学一下) after dinner.`
她自己标「这个词组学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "on the house"／"on me"／"complimentary" ⇒ 零命中
　② 中文 dedup "请客"／"免费" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」；同一块里 free 和 on the house 叠用（意思说了两遍）　　目标：`a fruit platter on the house`
找法：说"店家请的"，落 on the house，回头看前面有没有多出一个 free。

**题面**
"这杯咖啡是老板请的，不用给钱。"（"老板请的"用 **on the house** 说）
★ 她说要学的块：第一次出题整块点名；连对 ≥1 之后降回 house（on the 留给她）

- 2026-10-06 ❌ 首犯 · 学习日 在池第 1 组 [7]（#401 题里）· 她标「这个词组学一下」· 原话 `a free fruit platter on the house（这个词组学一下) after dinner.`
- 2026-10-07 ✅ 学习日 在池第 1 组 [8] · `This coffee is on the house, so don't worry about paying.` —— 前面没再叠 free。连错 1 → 连对 1（下次点名降回 house）
- 2026-10-08 ✅ 付息日 a 段在池第 1 组 [2] · `We waited for an hour at that restaurant, so the manager gave us a dessert on the house.` —— 点名降到 house，on the 自己补上、前面没加 free。连对 1 → 2 ⇒ **毕业**

### 414 · tweak（小改、微调）
类型 词汇 ｜ 新建 2026-10-06 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-08 ｜ **🎓 已毕业 2026-10-08**（连对2 ＝ 10-07 ＋ 10-08）｜ 题型 整句

**问题是什么**
**tweak** ＝ 在已经差不多的东西上动一点点：tweak the recipe ／ tweak it a bit ／ make a few tweaks（名词：几处小改动）。
同一格里的邻居（别串）：change（泛泛地改）· revise（改文稿，偏书面）· adjust（调数值、位置）· fine-tune（精调）· redo（推倒重来）。
判据一句话：大体已经可以、只动一点点 ⇒ tweak；整个推翻重来 ⇒ redo。
★ 题型判整句："稍微改改"翻成 change a little／adjust 都合法，孤立翻块映射不回唯一的 tweak ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 在池第 1 组 [10]（#404 题"他对自己的作品太苛刻了，怎么改都不满意"）· 原话
`He is overly critical of his own work and never satisfied no matter how much he tweaks(这个词学下） it.`
她自己标「这个词学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "tweak"／"fine-tune"／"revise" ⇒ 零命中；dedup "adjust" ⇒ 命中 🎓#126（get used to／settle into 适应新环境，adjust 只出现在它的排除项里）⇒ 不是同一个词，否
　② 中文 dedup "微调" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词学下」（词不在手边）　　目标：`tweak`
找法："稍微改改／再调一调"，先落 tweak。

**题面**
"方案大体不错，开会前再稍微改改就行。"（"稍微改改"用 **tweak** 说）

- 2026-10-06 ❌ 首犯 · 学习日 在池第 1 组 [10]（#404 题里）· 她标「这个词学下」· 原话 `no matter how much he tweaks(这个词学下） it.`
- 2026-10-07 ✅ 学习日 在池第 1 组 [9] · `The plan is solid for the most part; we just need to tweak it a bit before the meeting.` —— tweak it a bit。连错 1 → 连对 1
- 2026-10-08 ✅ 付息日 a 段在池第 1 组 [3] · `This photo turned out great—I just tweaked the colors a little bit.` —— tweaked the colors。连对 1 → 2 ⇒ **毕业**

### 415 · make it through to ＋ 下一轮／决赛（闯进、晋级）
类型 词组 ｜ 新建 2026-10-06 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-08 ｜ **🎓 已毕业 2026-10-08**（连对2 ＝ 10-07 ＋ 10-08）｜ 题型 整句

**问题是什么**
**make it through to** ＋ 那一轮 ＝ 前面几关都过了、闯进下一轮：make it through to the final ／ the next round ／ the second round of interviews。
同一格里的邻居（别串）：make it to（到了、赶上：make it to the final 也能说，不强调"一关关过"）· get through（过了某一轮：I got through the first round）· go through to（英式体育报道：go through to the semi-finals）。
判据一句话：说"闯进／晋级到哪一轮" ⇒ make it through to ＋ 那一轮；只说"过了这一关" ⇒ get through ＋ 这一轮。
★ 题型判整句："闯进决赛"翻成 reached／got into the final 都合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 在池第 2 组 [3]（#408 题"我进了第二轮面试，下周还要再面一次"）· 原话
`I made it through to（这个词组学一下) the second round of interviews, so I've got another one coming up next week.`
她自己标「这个词组学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "make it"／"made it" ⇒ 命中 🎓#80（than ever）· 🎓#288（once 句型）· 🎓#299（not much of）—— 只是历史句里带这两个词 ⇒ 否；dedup "through to" ⇒ 命中 🎓#339（reach sb，正文邻居 get through to sb ＝ 打通电话）· 🎓#390（get through ＋ 书 ＝ 啃完）—— 都不是"晋级" ⇒ 否
　② 中文 dedup "晋级" ⇒ 零命中；"进了" ⇒ 命中 🎓#368 land a job 等，正文带"进了"二字的别的考点 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」　　目标：`make it through to the second round`
找法："进了下一轮／闯进决赛"，先落 make it through to。

**题面**
"我们队一路闯进了决赛。"（"闯进"用 **make it through to** 说）
★ 她说要学的块：第一次出题整块点名；连对 ≥1 之后降回 make it through（to 留给她）
　10-08 只点 make it 时她答 made it to（合法，判 ✅），through 没逼出来 ⇒ 降级只降到 make it through，⛔ 不再只点 make it

- 2026-10-06 ❌ 首犯 · 学习日 在池第 2 组 [3]（#408 题里）· 她标「这个词组学一下」· 原话 `I made it through to（这个词组学一下) the second round of interviews`
- 2026-10-07 ✅ 学习日 在池第 1 组 [10] · `Our team made it through to the finals.` —— made it through to the finals。连错 1 → 连对 1（下次点名降回 make it）
- 2026-10-08 ✅ 付息日 a 段在池第 1 组 [4] · `She made it to the semifinals(这个词背下) the first time she entered a singing competition.` —— 题面只点 make it，make it to 是条目列明的合法说法 ⇒ ✅；through 没逼出来 ⇒ 种子题面★改为连对后降回 make it through。连对 1 → 2 ⇒ **毕业**
  ｜她自注「这个词背下」⇒ semi-final 另建 #433

### 416 · gala（盛大的晚会／晚宴）
类型 词汇 ｜ 新建 2026-10-06 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-08 ｜ **🎓 已毕业 2026-10-08**（连对2 ＝ 10-07 ＋ 10-08）｜ 题型 整句

**问题是什么**
**gala** ＝ 正式、隆重、要穿礼服的那种晚会或晚宴，常常是为了筹款：a charity gala ／ a gala dinner ／ the annual gala。
同一格里的邻居（别串）：party（泛泛的聚会）· banquet（宴会，重点在吃）· ceremony（仪式、典礼）· fundraiser（筹款活动，不一定是晚会）。
判据一句话：隆重、穿礼服、常带筹款的晚会 ⇒ gala；朋友聚一聚 ⇒ party。
★ 题型判整句："盛大的晚会"翻成 a big party／banquet 也合法，孤立翻块映射不回唯一的 gala ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 在池第 2 组 [5]（#410 题"公司年底办的慈善晚会"）· 原话
`The company's year-end charity gala(这个词学一下).`
她自己标「这个词学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "gala" ⇒ 零命中
　② 中文 dedup "晚会" ⇒ 只命中 #410（charity 的题面带"晚会"二字，考点是 charity 不是 gala）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词学一下」（词不在手边）　　目标：`gala`
找法："盛大的晚会／慈善晚宴"，先落 gala。

**题面**
"博物馆每年都办一场盛大的晚会，来的人都穿着礼服。"（"盛大的晚会"用 **gala** 说）

- 2026-10-06 ❌ 首犯 · 学习日 在池第 2 组 [5]（#410 题里）· 她标「这个词学一下」· 原话 `The company's year-end charity gala(这个词学一下).`
- 2026-10-07 ✅ 学习日 在池第 2 组 [1] · `The museum hosts a grand gala every year, with everyone dressed in formal wear.` —— a grand gala。连错 1 → 连对 1
- 2026-10-08 ✅ 付息日 a 段在池第 1 组 [5] · `The company threw a grand gala at the end of the year and invited a few celebrities to perform.` —— threw a grand gala。连对 1 → 2 ⇒ **毕业**

### 417 · carve out time (for sth)（挤出／抽出时间）
类型 词组 ｜ 新建 2026-10-06 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-08 ｜ **🎓 已毕业 2026-10-08**（连对2 ＝ 10-07 ＋ 10-08）｜ 题型 整句

**问题是什么**
**carve out time** ＝ 从满满的日程里硬挤出一段时间：carve out time for the gym ／ carve out some time to read ／ carve out an hour a day。
同一格里的邻居（别串）：find time（找时间，大白话）· make time for（专门为某事留时间）· squeeze in（把一件事硬塞进日程：squeeze in a workout）。
判据一句话：说"挤出／抽出时间做某事" ⇒ carve out time for ＋ 名词 ／ to ＋ 动词。
★ 题型判整句："挤出时间"翻成 find time／make time 都合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 复检第 4 组 [4]（#130 题"我不会游泳；这几个月我一直没能抽出时间去健身房"）· 原话
`I can't swim; over the past few months, I haven't been able to carve out(这个词组学下) time for the gym.`
她自己标「这个词组学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "carve"／"make time"／"find time" ⇒ 零命中
　② 中文 dedup "抽出时间"／"挤出时间"／"抽时间" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」　　目标：`carve out time for the gym`
找法："抽出时间／挤出时间"，先落 carve out time，后面接 for ＋ 名词或 to ＋ 动词。

**题面**
"工作再忙，我每周也会挤出一个晚上陪我爸妈吃饭。"（"挤出"用 **carve out** 说）

- 2026-10-06 ❌ 首犯 · 学习日 复检第 4 组 [4]（#130 题里）· 她标「这个词组学下」· 原话 `I haven't been able to carve out(这个词组学下) time for the gym.`
- 2026-10-07 ✅ 学习日 在池第 2 组 [2] · `No matter how busy I get, I still carve out one evening a week to have dinner with my parents.` —— carve out ＋ 时间 ＋ to do。连错 1 → 连对 1
- 2026-10-08 ✅ 付息日 a 段在池第 1 组 [6] · `After the baby came along, I could only carve out half an hour a day for working out.` —— carve out half an hour。连对 1 → 2 ⇒ **毕业**

### 418 · sit on ＋ 想法／计划（攥着迟迟没动手）
类型 词组 ｜ 新建 2026-10-06 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-08 ｜ **🎓 已毕业 2026-10-08**（连对2 ＝ 10-07 ＋ 10-08）｜ 题型 整句

**问题是什么**
**sit on sth** ＝ 手里攥着一个想法／计划／消息，一直没动手或没公开：I've been sitting on this idea for years. ／ They sat on the news for a week.
同一格里的邻居（别串）：toy with an idea（脑子里琢磨着玩，没当真）· have sth in mind（心里有个打算）· act on sth（付诸行动，sit on 的反面）。
判据一句话：有想法但还没真的迈出那一步 ⇒ sit on；已经在朝它走 ⇒ work toward。
★ 题型判整句："憋着没动手"翻成 haven't acted on／kept putting off 都合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 新题 bank:510（P2 · Describe a long-term goal/ambition you would like to achieve）[S2] · 原话
`I'm a software engineer, and I've been sitting on（这个词组学下) this idea for a few years now.`
她自己标「这个词组学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "sit on"／"sitting on" ⇒ 零命中
　② 中文 dedup "憋" ⇒ 命中 🎓#136（tell the truth，题面"他憋了好几天"只是场景，考点是 tell）⇒ 否；"没动手" ⇒ 零命中（只命中本条）
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（用法本身对：她还没辞职单干，想法攥在手里）　　目标：`sit on this idea`
找法："这个想法憋了好几年／一直没动手"，先落 sit on。

**题面**
"开咖啡店这个想法他憋了好几年，一直没敢真干。"（"憋着没动手"用 **sit on** 说）

- 2026-10-06 ❌ 首犯 · 学习日 新题 bank:510 [S2] · 她标「这个词组学下」· 原话 `I've been sitting on（这个词组学下) this idea for a few years now.`
- 2026-10-07 ✅ 学习日 在池第 2 组 [3] · `He's been sitting on the idea of opening a coffee shop for years, never quite making the move(这个词组学一下).` —— sitting on the idea of ＋ -ing。连错 1 → 连对 1（她标学 making the move ⇒ 另建 #425）
- 2026-10-08 ✅ 付息日 a 段在池第 1 组 [7] · `She was sitting on the idea for this novel for ten years, never actually writing it down.` —— sitting on the idea。连对 1 → 2 ⇒ **毕业**（was sitting … for ten years 的时态 ⇒ ⚪#12 另记）

### 419 · grind away (at sth)（埋头苦熬、机械地干）
类型 词组 ｜ 新建 2026-10-06 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-08 ｜ **🎓 已毕业 2026-10-08**（连对2 ＝ 10-07 ＋ 10-08）｜ 题型 整句

**问题是什么**
**grind away** ＝ 长时间、枯燥地埋头干，带"熬"的味道：grind away at the same job ／ grinding away for a company ／ grind away at a thesis。
同一格里的邻居（别串）：work hard（中性，不带"熬"）· slog away（同义，英式）· the daily grind（名词：每天上班那套磨人的日常）。
判据一句话：辛苦 ＋ 重复 ＋ 没意思 ⇒ grind away；只是努力 ⇒ work hard。
★ 题型判整句："埋头苦干"翻成 work hard 也合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 新题 bank:510 [S3] · 原话
`Basically, it's about building things of my own, rather than just grinding away（这个词组学下) for a company.`
她自己标「这个词组学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "grind" ⇒ 零命中
　② 中文 dedup "埋头" ⇒ 命中 🎓#88（get on with it：别磨蹭、接着干下去 —— 说的是"开始／继续干"，不带"熬"）⇒ 不是同一个词组，否；"苦熬" ⇒ 零命中（只命中本条）
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（用法本身对）　　目标：`grinding away for a company`
找法："埋头苦熬／给公司当牛马"，先落 grind away。

**题面**
"他在工厂流水线上埋头苦干了十年。"（"埋头苦干"用 **grind away** 说）

- 2026-10-06 ❌ 首犯 · 学习日 新题 bank:510 [S3] · 她标「这个词组学下」· 原话 `rather than just grinding away（这个词组学下) for a company.`
- 2026-10-07 ✅ 学习日 在池第 2 组 [4] · `He spent ten years grinding away on the assembly line in a factory.` —— grinding away on the assembly line。连错 1 → 连对 1
- 2026-10-08 ✅ 付息日 a 段在池第 1 组 [8] · `He spent an entire year grinding away in the library for grad school exams.` —— grinding away。连对 1 → 2 ⇒ **毕业**

### 420 · be burnt out (on sth)（被耗干、倦怠）
类型 词组 ｜ 新建 2026-10-06 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-08 ｜ **🎓 已毕业 2026-10-08**（连对2 ＝ 10-07 ＋ 10-08）｜ 题型 整句

**问题是什么**
**burnt out** ＝ 长期透支、身心被掏空、提不起劲：I'm burnt out on overtime. ／ completely burnt out ／ burnout（名词：职业倦怠）。
同一格里的邻居（别串）：exhausted（就是累，睡一觉能缓过来）· fed up with ／ sick of（烦透了，偏情绪）。
判据一句话：长期透支、累到不想干 ⇒ burnt out (on ＋ 让你耗干的东西)；累了一天 ⇒ exhausted。
★ 题型判整句："被耗干了"翻成 exhausted／worn out 都合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 新题 bank:510 [S5] · 原话
`After 14 years in the industry, I'm pretty burnt out on（这个词组学下)  constant overtime and company instability.`
她自己标「这个词组学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "burn"／"burnt out" ⇒ 零命中
　② 中文 dedup "耗干"／"倦怠"／"累垮" ⇒ 零命中（只命中本条）
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（用法本身对）　　目标：`burnt out on constant overtime`
找法："被耗干了／彻底倦怠"，先落 burnt out。

**题面**
"连着上了三个月夜班，那几个护士都被耗干了。"（"被耗干了"用 **burnt out** 说）

- 2026-10-06 ❌ 首犯 · 学习日 新题 bank:510 [S5] · 她标「这个词组学下」· 原话 `I'm pretty burnt out on（这个词组学下)  constant overtime`
- 2026-10-07 ✅ 学习日 在池第 2 组 [6] · `Working night shifts for three consecutive months left those nurses totally burnt out.` —— left … totally burnt out。连错 1 → 连对 1
- 2026-10-08 ✅ 付息日 a 段在池第 1 组 [10] · `Working overtime for a consecutive month left me totally burnt out.` —— left me totally burnt out。连对 1 → 2 ⇒ **毕业**
  ｜for a consecutive month ❌ ⇒ 另建 #434

### 421 · support yourself（养活自己；sustain yourself 偏正式）
类型 搭配 ｜ 新建 2026-10-06 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-08 ｜ **🎓 已毕业 2026-10-08**（连对2 ＝ 10-07 ＋ 10-08）｜ 题型 整句

**问题是什么**
**support yourself** ＝ 自己挣钱养活自己：support myself ／ support yourself financially ／ support a family（养家）。
同一格里的邻居（别串）：sustain yourself（也能说，偏正式，更常说维持体力、生命）· make a living（谋生，说"靠什么吃饭"）· 🎓#101 get by（勉强够用）。
判据一句话：说"养活自己／养家" ⇒ support；说"靠什么谋生" ⇒ make a living as／from。
★ 题型判整句："养活自己"翻成 make a living／pay my own way 都合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 新题 bank:510 [S6] · 原话
`If I could sustain myself（这个词组学下)  without a traditional 9-to-5, I’d feel so much freer.`
她自己标「这个词组学下」⇒ §2③ 建号，判 ❌（§3.2b）；同一处更好版 sustain myself → support myself（⚠️ 偏正式 → 口语默认）也装进本条（同一个格）。
判重三步：
　① 目标形式 dedup "sustain"／"support myself"／"support yourself" ⇒ 零命中
　② 中文 dedup "养活" ⇒ 零命中
　③ 书面登记前提核查：lab/sessions 全部产出里没出现过 support myself／herself ⇒ 口语版对她是新表达 ⇒ ⛔ 不走 🎓#206，保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`sustain myself`（她标学；能说，但偏正式）　　更好：`support myself`
找法："养活自己"，先落 support myself。

**题面**
"她上大学的时候靠做家教养活自己。"（"养活自己"用 **support** 说）

- 2026-10-06 ❌ 首犯 · 学习日 新题 bank:510 [S6] · 她标「这个词组学下」· 原话 `If I could sustain myself（这个词组学下)  without a traditional 9-to-5` ⇒ 更好版 support myself
- 2026-10-07 ✅ 学习日 在池第 2 组 [5] · `She supported herself as a tutor back in college.` —— supported herself。连错 1 → 连对 1
- 2026-10-08 ✅ 付息日 a 段在池第 1 组 [9] · `He started working to support himself when he was just eighteen.` —— support himself。连对 1 → 2 ⇒ **毕业**

### 422 · day in, day out（日复一日、天天如此）
类型 词组 ｜ 新建 2026-10-06 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-07 未毕业 ｜ 题型 整句

**问题是什么**
**day in, day out**（也说 day in and day out）＝ 每天都一个样、没完没了，常带"单调"的味道，放句尾：do the same thing day in, day out。
同一格里的邻居（别串）：day after day（中性）· every single day · on a daily basis（偏书面）。
判据一句话：强调"天天一个样、没完没了" ⇒ day in, day out。
★ 题型判整句："日复一日"翻成 day after day 也合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 新题 bank:510 [S7] · 原话
`On top of that, this whole thing keeps me learning instead of just repeating company busywork day in and day out（这个搭配学下) .`
她自己标「这个搭配学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "day in" ⇒ 零命中
　② 中文 dedup "日复一日" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个搭配学下」（用法本身对）　　目标：`day in and day out`
找法："日复一日／天天都是这样"，先落 day in, day out，放在句尾。

**题面**
"他日复一日地守着那家小面馆，一干就是二十年。"（"日复一日"用 **day in, day out** 说）
★ 她说要学的块：第一次出题整块点名；连对 ≥1 之后降回 day in（day out 留给她）

- 2026-10-06 ❌ 首犯 · 学习日 新题 bank:510 [S7] · 她标「这个搭配学下」· 原话 `repeating company busywork day in and day out（这个搭配学下) .`
- 2026-10-07 ✅ 学习日 在池第 2 组 [8] · `My cat sits on the exact same windowsill(这个单词背一下) soaking up(这个词组学一下) the sun, day in, day out.` —— day in, day out 放句尾。连错 1 → 连对 1（下次点名降回 day in；她标背 windowsill ⇒ 另建 #426，标学 soaking up ⇒ 另建 #427）

### 423 · job insecurity（工作没保障、不稳定；⛔ company instability）
类型 搭配 ｜ 新建 2026-10-06
状态 连对1 连错0 上次2026-10-07 未毕业 ｜ 题型 整句

**问题是什么**
**job insecurity** ＝ 工作没保障、随时可能被裁的那种不稳定（job security 的反面）。
同一格里的邻居（别串）：job security（工作有保障，她 09-26 自己用过）· an unstable job（一份不稳定的工作，挂在某一份工作上）· layoffs（裁员）。
判据一句话：说"工作不稳定"这种状态或担忧 ⇒ job insecurity；company instability 听起来是"公司本身经营不稳"。
★ 题型判整句："工作不稳定"翻成 unstable jobs 也合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-06 学习日 新题 bank:510 [S5] · 原话
`After 14 years in the industry, I'm pretty burnt out on（这个词组学下)  constant overtime and company instability.`
diff-2 ⚠️：company instability 能懂，但"工作没保障"英语固定说 job insecurity ⇒ 能学的表达 ⇒ §3.2b 建号。
判重三步：
　① 目标形式 dedup "insecurity" ⇒ 零命中
　② 中文 dedup "不稳定" ⇒ 命中 🎓#96（否定辖域陷阱，解法里带 job security，考点是 no … and … 的辖域）· 🎓#314（economic ≠ economical，只是历史句带"不稳定"）⇒ 都不是这个块，否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`company instability`（中文"公司不稳定"直译）　　更好：`job insecurity`
找法："工作不稳定"，从 job security 翻一面 ⇒ job insecurity。

**题面**
"对很多年轻人来说，工作不稳定是最大的压力来源。"（"工作不稳定"用 **job insecurity** 说）

- 2026-10-06 ❌ 首犯 · 学习日 新题 bank:510 [S5] · diff-2 ⚠️ · 原话 `burnt out on constant overtime and company instability.` ⇒ 更好版 job insecurity
- 2026-10-07 ✅ 学习日 在池第 2 组 [7] · `For a lot of young people, job insecurity is their biggest source of stress.` —— job insecurity。连错 1 → 连对 1

### 424 · set aside ＋ 钱／时间（专门留出一部分）
类型 词组 ｜ 新建 2026-10-07 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-07 未毕业 ｜ 题型 整句

**问题是什么**
**set aside** ＝ 从总量里专门划出一部分、留着做某件事：set aside part of my paycheck ／ set aside some money for a trip ／ set aside an hour every evening。
同一格里的邻居（别串）：save（存钱，泛泛地攒）· put aside（同义，更口语）· #417 carve out time（从满满的日程里硬挤出时间 —— 强调"挤"；set aside 强调"划出来留着"）。
判据一句话：把一部分钱／时间划出来、专门留给某件事 ⇒ set aside ＋ 那一部分 ＋ for ／ to do。
★ 题型判整句："留出一笔钱"翻成 save some money 也合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-07 学习日 在池第 1 组 [5]（#410 题"每个月拿出一部分工资捐给慈善机构"）· 原话
`setting aside（这个词组学下) part of my paycheck every month to donate to charity`
她自己标「这个词组学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "set aside"／"setting aside"／"put aside" ⇒ 零命中；"aside" ⇒ 命中 🎓#281（step back，正文邻居 step aside ＝ 让开）⇒ 不是同一个词组，否
　② 中文 dedup "留出" ⇒ 命中 🎓#57（date night，题面带"专门留出来的那一晚"，考点是 date night）⇒ 否；"存下"／"攒" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（用法本身对）　　目标：`set aside part of my paycheck`
找法："拿出一部分／专门留出"，先落 set aside。

**题面**
"我每个月都留出一笔钱，专门用来旅行。"（"留出"用 **set aside** 说）

- 2026-10-07 ❌ 首犯 · 学习日 在池第 1 组 [5]（#410 题里）· 她标「这个词组学下」· 原话 `setting aside（这个词组学下) part of my paycheck every month to donate to charity`

### 425 · make the move（真的迈出那一步、付诸行动）
类型 词组 ｜ 新建 2026-10-07 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-07 未毕业 ｜ 题型 整句

**问题是什么**
**make the move** ＝ 下决心真的去做、迈出那一步（常指换工作、搬家、转行这种大决定）：finally make the move ／ make the move to freelancing ／ make the move to London。
同一格里的邻居（别串）：#418 sit on（攥着想法没动手 —— 正好是 make the move 的前一个阶段）· take the plunge（豁出去下决心，更带"跳下去"的冒险味）· make a move（动身、该走了；也指采取行动）。
判据一句话：说"终于真干了／迈出了那一步" ⇒ make the move；还憋着没动 ⇒ sit on。
★ 题型判整句："迈出那一步"翻成 finally did it／went for it 都合法 ⇒ 整句 ＋ 正向点名。
★ 与 #418 分工：#418 考"攥着没动手"（sit on），本条考"真的动手了"（make the move）—— 一前一后两个块，各走各的。

**怎么发现的**
2026-10-07 学习日 在池第 2 组 [3]（#418 题"开咖啡店这个想法他憋了好几年，一直没敢真干"）· 原话
`He's been sitting on the idea of opening a coffee shop for years, never quite making the move(这个词组学一下).`
她自己标「这个词组学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "make the move"／"make a move" ⇒ 零命中；"plunge" ⇒ 只命中 🎓#335 历史句（take action），不是这个块 ⇒ 否
　② 中文 dedup "迈出" ⇒ 命中 #418（sit on 正文"还没真的迈出那一步"，是本条的前一个阶段，目标形式不同）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」（用法本身对）　　目标：`never quite making the move`
找法："终于下决心真干了"，先落 make the move（要说转去做什么就接 to ＋ 名词）。

**题面**
"她考虑辞职去考研考虑了两年，今年终于真的迈出了那一步。"（"迈出那一步"用 **make the move** 说）

- 2026-10-07 ❌ 首犯 · 学习日 在池第 2 组 [3]（#418 题里）· 她标「这个词组学一下」· 原话 `never quite making the move(这个词组学一下).`

### 426 · windowsill（窗台）
类型 词汇 ｜ 新建 2026-10-07 ｜ ⭐ 她点名要背
状态 连对0 连错1 上次2026-10-07 未毕业 ｜ 题型 词组

**问题是什么**
**windowsill** ＝ 窗台（窗户下沿那条可以放东西、猫能趴的平台）：on the windowsill ／ a plant on the windowsill。
同一格里的邻居（别串）：window（窗户本身）· ledge（凸出来的窄台子，泛指）· balcony（阳台）。
判据一句话：窗户下面那条平台 ⇒ windowsill，介词用 on。
★ 题型判词组："窗台"只映射回 windowsill（window ledge 合法照判），一个块就覆盖考点 ⇒ 词组题、零英文提示。

**怎么发现的**
2026-10-07 学习日 在池第 2 组 [8]（#422 题"我家的猫日复一日地趴在同一个窗台上晒太阳"）· 原话
`My cat sits on the exact same windowsill(这个单词背一下) soaking up(这个词组学一下) the sun, day in, day out.`
她自己标「这个单词背一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "windowsill"／"sill" ⇒ 零命中
　② 中文 dedup "窗台" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个单词背一下」（词不在手边）　　目标：`windowsill`
找法：说"窗台"，先落 windowsill。

**题面**
"窗台上摆着的几盆小多肉"（窗户下沿那条能放东西的平台）

- 2026-10-07 ❌ 首犯 · 学习日 在池第 2 组 [8]（#422 题里）· 她标「这个单词背一下」· 原话 `My cat sits on the exact same windowsill(这个单词背一下)`

### 427 · soak up ＋ the sun／the atmosphere（尽情享受、吸收）
类型 词组 ｜ 新建 2026-10-07 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-07 未毕业 ｜ 题型 整句

**问题是什么**
**soak up** ＝ 像海绵吸水一样，把阳光／氛围／景色尽情吸收进来：soak up the sun ／ soak up the atmosphere ／ soak up the view。
同一格里的邻居（别串）：🎓#353（vibe 挂在地方上 —— 正文例句 soak up a different vibe，考点在 vibe 不在 soak up）· enjoy（泛泛地享受）· bask in the sun（晒太阳，偏书面）。
判据一句话：说"晒太阳／尽情感受那个氛围" ⇒ soak up ＋ the sun／the atmosphere。
★ 题型判整句："晒太阳"翻成 sunbathe／lie in the sun 都合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-07 学习日 在池第 2 组 [8]（#422 题"我家的猫日复一日地趴在同一个窗台上晒太阳"）· 原话
`My cat sits on the exact same windowsill(这个单词背一下) soaking up(这个词组学一下) the sun, day in, day out.`
她自己标「这个词组学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "soak" ⇒ 命中 🎓#353（正文例句 soak up a different vibe；那条考的是 vibe 挂在地方上、人不待在 vibe 里）⇒ 不是同一个考点，否
　② 中文 dedup "晒太阳" ⇒ 零命中；"sunbath" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」（用法本身对）　　目标：`soaking up the sun`
找法："晒太阳／感受一下气氛"，先落 soak up。

**题面**
"周末我们就躺在沙滩上晒了一下午太阳。"（"晒太阳"用 **soak up** 说）

- 2026-10-07 ❌ 首犯 · 学习日 在池第 2 组 [8]（#422 题里）· 她标「这个词组学一下」· 原话 `soaking up(这个词组学一下) the sun, day in, day out.`

### 428 · be featured in ＋ 杂志／节目（被刊登、上了…）
类型 词组 ｜ 新建 2026-10-07 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-07 未毕业 ｜ 题型 整句

**问题是什么**
**be featured in** ＝ 作为重点内容出现在杂志／报纸／节目／展览里（"上了杂志、上了节目"）：Her work has been featured in several magazines. ／ The café was featured in a travel show.
同一格里的邻居（别串）：appear in（出现在…里，泛泛）· be published in（发表在…上，偏文章、论文）· be on TV（上电视，大白话）。
判据一句话：说"上了杂志／上了节目／被重点介绍" ⇒ be featured in；说"发表论文" ⇒ be published in。
★ 题型判整句："上过节目"翻成 was on a show／appeared on 都合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-07 学习日 复检第 3 组 [3]（#391 题"她是设计圈里正在冒头的新人，作品已经上了好几本杂志"）· 原话
`She's an up-and-coming talent in design circles, with her work featured in(这个词组学下) multiple magazines.`
她自己标「这个词组学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "featured" ⇒ 零命中；"feature" ⇒ 只命中 🎓#213（go live，历史句里的 feature ＝ 功能）⇒ 不是同一个词义，否
　② 中文 dedup "刊登" ⇒ 零命中；"上了" ⇒ 命中 34 条，都是正文带"上了"二字的别的考点（🎓#398 on the line · 🎓#234 the elderly 等）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（用法本身对）　　目标：`with her work featured in multiple magazines`
找法："上了好几本杂志／上了节目"，先落 be featured in。

**题面**
"我们小区门口那家面馆上过一档美食节目。"（"上过"用 **featured** 说）

- 2026-10-07 ❌ 首犯 · 学习日 复检第 3 组 [3]（#391 题里）· 她标「这个词组学下」· 原话 `with her work featured in(这个词组学下) multiple magazines.`

### 429 · hold a grudge (against sb)（记仇）
类型 词组 ｜ 新建 2026-10-07 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-07 未毕业 ｜ 题型 整句

**问题是什么**
**hold a grudge** ＝ 心里一直记着别人的不好、不肯放下：He never holds a grudge. ／ hold a grudge against sb（记某人的仇）。
同一格里的邻居（别串）：let it go（放下、算了）· forgive and forget（原谅了也不再提）· get over it（过去了、缓过来了）。
判据一句话：说"记仇／一直耿耿于怀" ⇒ hold a grudge (against sb)；说"不记仇／放下了" ⇒ never holds a grudge ／ let it go。
★ 题型判整句："记仇"翻成 never forgets／holds it against me 都合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-07 学习日 复检第 3 组 [10]⑤（#262 题"他脾气是不太好——不过他从来不记仇"）· 原话
`He's got a bad temper—mind you, he never holds a grudge(这个词组学一下).`
她自己标「这个词组学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "grudge" ⇒ 零命中
　② 中文 dedup "记仇" ⇒ 只命中 🎓#262 的题面⑤（那条考的是 mind you 这个转折标记）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」（用法本身对）　　目标：`he never holds a grudge`
找法："记仇"，先落 hold a grudge，记谁的仇用 against 接。

**题面**
"我妹妹特别记仇，小时候我抢了她一块糖，她到现在还提。"（"记仇"用 **grudge** 说）

- 2026-10-07 ❌ 首犯 · 学习日 复检第 3 组 [10]⑤（#262 题里）· 她标「这个词组学一下」· 原话 `mind you, he never holds a grudge(这个词组学一下).`

### 430 · street market（街头集市、露天摊位市场）≠ shopping street（商业街）
类型 词汇 ｜ 新建 2026-10-07
状态 连对0 连错1 上次2026-10-07 未毕业 ｜ 题型 词组

**问题是什么**
**street market** ＝ 街头集市、露天市场：一排排摊位，卖菜、小吃、旧货；介词用 at（at a street market）。
同一格里的邻居（别串）：shopping street（商业街，两边是正经店面，介词 on）· open-air market（露天市场）· night market（夜市）· flea market（跳蚤市场）。
判据一句话：一排排摊位 ⇒ market（at）；两边是店面 ⇒ shopping street（on）。
★ 题型判词组："露天摆摊的集市"只映射回 street market／open-air market（两个都算对），一个块就覆盖考点 ⇒ 词组题、零英文提示。

**怎么发现的**
2026-10-07 学习日 新题 bank:1151（P3 · What are the differences between shopping in street markets and big shopping malls?）[S3] · 原话
`Shopping streets, on the other hand, are pretty messy or don't really have any layout at all.`
题目问的是 street markets（集市），她通篇答成 shopping streets（商业街）⇒ 层4 切题 ⚠️；street market 是能学的表达 ⇒ §3.2b 建号。
判重三步：
　① 目标形式 dedup "street market"／"stall" ⇒ 零命中；"market" ⇒ 命中 🎓#205（the market／the economy 这类系统性名词带 the）· 🎓#279（get a feel for，历史句带 market）⇒ 都不是这个词，否
　② 中文 dedup "集市" ⇒ 零命中；"摊" ⇒ 命中 🎓#27（功劳分摊）· 🎓#295 · 🎓#206，都是正文带"摊"字的别的考点 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：把题目里的 street markets 当成了 shopping streets（商业街）　　正确：street market ＝ 摆摊的集市
找法：听到 street market，脑子里先出"摆摊的集市"，不是步行街。

**题面**
"周末在停车场里临时摆起来的露天集市"（一排排摊位，卖菜、卖小吃、卖旧货的那种）

- 2026-10-07 ❌ 首犯 · 学习日 新题 bank:1151 [S3] · 层4 切题 ⚠️ · 原话 `Shopping streets, on the other hand, are pretty messy …` ⇒ 更好版 Street markets

### 431 · well planned out（规划得好、布局合理）
类型 词组 ｜ 新建 2026-10-07 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-07 未毕业 ｜ 题型 整句

**问题是什么**
**be (well) planned out** ＝ 事先规划、布局安排得好：The mall is well planned out. ／ way better planned out ／ a poorly planned-out city。
同一格里的邻居（别串）：well laid out（布局好，偏空间）· well organized（安排得有条理）· layout（名词：布局）。
判据一句话：说一个地方／一件事"规划得好／安排得周到" ⇒ well planned out。
★ 题型判整句："规划得好"翻成 well designed／well organized 都合法 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-07 学习日 新题 bank:1151 [S2] · 原话
`Malls are usually way better planned out（这个词组学下)—different kinds of shops are organized into different areas, …`
她自己标「这个词组学下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "planned out"／"plan out"／"layout" ⇒ 零命中
　② 中文 dedup "规划" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学下」（用法本身对）　　目标：`way better planned out`
找法："规划得好／布局合理"，先落 well planned out。

**题面**
"这个新小区规划得特别好，学校、超市走路十分钟都能到。"（"规划得好"用 **planned out** 说）

- 2026-10-07 ❌ 首犯 · 学习日 新题 bank:1151 [S2] · 她标「这个词组学下」· 原话 `Malls are usually way better planned out（这个词组学下)`

### 432 · cross-border ≠ transnational（跨境 vs 跨国）
类型 词汇 ｜ 新建 2026-10-08 ｜ ⭐ 她点名要学
状态 连对0 连错0 上次— 未毕业 ｜ 题型 词组 ｜ 合并条·出题多句覆盖

**问题是什么**
两个"跨"分工不同：
· **cross-border** ＝ 跨越边境的 —— 东西／钱／人从一个国家过到另一个国家：cross-border e-commerce ／ cross-border payments ／ cross-border travel
· **transnational** ＝ 横跨好几个国家同时运作的 —— 说组织、网络（偏书面、新闻）：transnational crime ／ transnational organizations
同一格里的邻居（别串）：multinational（日常说"跨国公司"就是 a multinational company，比 transnational 常用得多）· international（国际的，最宽泛）· overseas（海外的）。
判据一句话：东西／钱"过境" ⇒ cross-border；一个组织"横跨多国运作" ⇒ transnational（公司日常说 multinational）。
★ 题型判词组：两个成员的中文块都能唯一映射回去（跨境支付 ⇒ cross-border payments；跨国犯罪 ⇒ transnational crime，⛔ 不落"跨国公司"——那个 multinational 也合法、收不拢）。

**怎么发现的**
2026-10-08 付息日 a 段在池第 1 组 [1]（#366 题面"我朋友去年做跨境电商，赚翻了。"）· 原话
`My friend got into cross-border（加入 transnational 的条目做对比） e-commerce last year and made bank.`
她写对了 cross-border，并要求「加入 transnational 的条目做对比」⇒ §2③ 她主动提出 ⇒ 建号（合并条：一对词的分工，成员数有限 ＝ 2，§3.2c⑤）。
判重三步：
　① 目标形式 dedup "cross-border"／"transnational"／"multinational" ⇒ 零命中
　② 中文 dedup "跨境"／"跨国" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：写对了 cross-border，要求把 transnational 放进来对比（两个"跨"分不清用哪个）　　目标：cross-border payments ／ transnational crime
找法：先问"是东西在过境，还是一个组织在好几个国家同时干？"

**题面**
★ 2 句，两个成员各一句 —— 本条考的就是这两个词的分工，只出一个等于没测
　① "跨境支付"（钱从一个国家转到另一个国家）
　② "跨国犯罪集团"（在好几个国家同时作案的犯罪组织）

**成员出题账**
① cross-border ｜ 未出过
② transnational ｜ 未出过

- 2026-10-08 📝 新建 · 付息日 a 段在池第 1 组 [1]（#366 题里）· 她要求「加入 transnational 的条目做对比」· 原话 `My friend got into cross-border（加入 transnational 的条目做对比） e-commerce last year and made bank.`

### 433 · semi-final（半决赛）
类型 词汇 ｜ 新建 2026-10-08 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-08 未毕业 ｜ 题型 词组

**问题是什么**
**semi-final** ＝ 半决赛（也写 semifinal）；the semi-finals ＝ 半决赛那一轮（有两场，所以常用复数）。
同一格里的邻居（别串）：quarter-final（四分之一决赛）· the final（决赛，一场，单数）· the knockout stage（淘汰赛阶段）。
判据一句话：决赛前一轮 ⇒ semi-final；再前一轮 ⇒ quarter-final。

**怎么发现的**
2026-10-08 付息日 a 段在池第 1 组 [4]（#415 题面"她第一次参加歌唱比赛，就闯进了半决赛。"）· 原话
`She made it to the semifinals(这个词背下) the first time she entered a singing competition.`
她写对了 semifinals，但自己标「这个词背下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "semi" ⇒ 只命中 #415（正文举例 semi-finals，考点是 make it through to）⇒ 否
　② 中文 dedup "半决赛" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词背下」（词不在手边）　　目标：`the semifinals`
找法：说"半决赛"，先落 semi-final。

**题面**
"世界杯半决赛"（决赛前一轮，四支队伍打两场）

- 2026-10-08 ❌ 首犯 · 付息日 a 段在池第 1 组 [4]（#415 题里）· 她标「这个词背下」· 原话 `She made it to the semifinals(这个词背下) the first time she entered a singing competition.`

### 434 · for a whole month／a month straight（连续一个月；⛔ for a consecutive month）
类型 搭配 ｜ 新建 2026-10-08
状态 连对0 连错1 上次2026-10-08 未毕业 ｜ 题型 整句

**问题是什么**
**consecutive** ＝"一个接一个"，至少两个单位才连得起来：three consecutive days ／ for the third consecutive year。
只有**一个**单位时：**for a whole month**（整整一个月）／ **for a month straight**（straight 放在时间后面 ＝ 连续不断）。
同一格里的邻居（别串）：in a row（three days in a row，同 consecutive，也要两个以上）· on end（for hours on end，一连好几个小时）。
判据一句话：数字 ≥ 2 ⇒ X consecutive days／X days in a row；只有"一个月" ⇒ a whole month／a month straight。
★ 题型判整句：考点是 consecutive 配不配单数，孤立翻"连续一个月"会直接落 for a month ⇒ 整句 ＋ 正向点名 straight。

**怎么发现的**
2026-10-08 付息日 a 段在池第 1 组 [10]（#420 题面"连续加了一个月的班，我整个人都被耗干了。"）· 原话
`Working overtime for a consecutive month left me totally burnt out.`
判重三步：
　① 目标形式 dedup "consecutive" ⇒ 只命中 #420（10-07 历史行里她写对的 three consecutive months）⇒ 否：那条考 burnt out；
　　 dedup "straight" ⇒ 🎓#331 look straight ahead（另一个意思）· 🎓#13 #333（历史行字串）⇒ 否
　② 中文 dedup "连续" ⇒ 命中的都只是历史行字串，考点无关 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`for a consecutive month`　　正确：`for a whole month`／`for a month straight`
找法：说"连续"之前先数一下有几个单位 —— 只有一个就别用 consecutive。

**题面**
"他连续一个星期每天只睡四个小时。"（"连续一个星期"用 **straight** 说）

- 2026-10-08 ❌ 首犯 · 付息日 a 段在池第 1 组 [10]（#420 题里）· 原话 `Working overtime for a consecutive month left me totally burnt out.`

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

