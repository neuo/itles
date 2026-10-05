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

### 343 · **opening hours**／business hours（营业时间；⛔ open time）
类型 词组 ｜ 新建 2026-09-15
状态 连对2 连错0 上次2026-10-04 ｜ **回潮 2026-10-02**（09-19 毕业 → 10-02 复检写成 `The museum's operating time.`，"开放时间"又落在 time 上，撤销毕业、连对清零）｜ **🎓 已毕业 2026-10-04**（连对2 ＝ 10-03 ＋ 10-04；10-02 回潮后第二次毕业）｜ 题型 词组

**问题是什么**
"营业时间"是一个固定块：**opening hours**（英式也说 opening times）／ **business hours**；⛔ open time 不是一个块（open 是形容词，time 单数也不对）。
同一格里的邻居（别串）：working hours（工作时间，说人）· office hours（办公时间／答疑时间）· be open（"开着门"：Are they open on Sundays?）。
判据一句话：说"几点开几点关"这件事 ⇒ 用 **hours**（复数）挂在 opening／business 后面；说"开没开门"才用 open。

**怎么发现的**
2026-09-15 学习日 在池第 2 组 [4]（#337 题面"查一下营业时间"）：她写 `look up the open time`。
查重（§3.1 判重三步）：
　① 目标形式 dedup "opening" ⇒ 只命中 #337（look up sth，考"查"不考"营业时间"，题面里带这个词而已）⇒ 否；dedup "business hours"／"open time" ⇒ 零命中
　② 中文 "营业" ⇒ 同样只命中 #337 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）
★ 编号跳过 342：本场教练建过 #342（gotta）又当场撤销，号作废不复用。

**我错在哪**
她的：`the open time`　　正确：`the opening hours`（／ business hours）
找法：写完"营业时间"回头看 —— 是不是 hours 结尾？不是就换成 opening hours。

**题面**
"这家超市的营业时间"（几点开门、几点关门）

- 2026-09-15 ❌ 首犯 · 学习日 在池第 2 组 [4]（#337 题）· `look up the open time`
  最小改 `look up the opening hours`
  ❌ "营业时间"是固定块 opening hours／business hours；open time 不是一个块
- 2026-09-18 ✅ 学习日 在池第 1 组 · `opening hours`（09-15 首犯后首测）
- 2026-09-19 ✅ 付息日 a 段在池第 1 组 · `opening hours` ⇒ **连对 2，毕业**
- 2026-09-22 ⚡ 自评免测 · 复检第 2 组
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 词组题零英文提示）
  去掉词数与"⛔ time"，改成中文释义（几点开门几点关门）；换成超市场景
- 2026-10-02 ❌ 复检 · 学习日 复检第 4 组 [6] · `The museum's operating time.` —— "开放时间"落在 time 上（与掉过的 open time 同一处）⇒ **回潮**
  最小改 `The museum's operating hours.`　更好版 `The museum's opening hours.`
  ❌ 营业／开放时间是几点到几点这一段 ⇒ hours（opening／business／operating hours），⛔ time
- 2026-10-03 ✅ 学习日 在池第 1 组 [1] · `The bank's weekend opening hours.` —— opening hours，hours 不是 time。连错 1 → 连对 1
- 2026-10-04 ✅ 付息日 a 段在池第 1 组 [1] · `The pharmacy 's opening hours posted on the front wall.` —— opening hours，hours 不是 time。连对 1 → 2 ⇒ **毕业**

### 372 · get it（把想要的东西弄到手；⛔ reach it —— reach 接目标／地点）
类型 搭配 ｜ 新建 2026-09-29
状态 连对2 连错0 上次2026-10-04 ｜ **🎓 已毕业 2026-10-04**（连对2 ＝ 10-03 ＋ 10-04）｜ 题型 整句

**问题是什么**
"把想要的东西弄到手"口语就是 **get it**：know what he wants and how to **get it**。
reach 接的是**目标／地点**（reach a goal ／ reach the top），⛔ 不接"想要的东西"。
判据一句话：宾语是"想要的东西"⇒ get；宾语是目标／终点 ⇒ reach。

**怎么发现的**
2026-09-29 学习日 复检第 2 组 [9]（🎓#323 题面"他聪明到知道自己到底要什么、也知道怎么去够到。"）：
她写 `he's smart enough to know what he really wants and how to reach it.`（#323 考点 wh 词判 ✅）。
当场被教练记成"同级近义词、不建号"—— 她追问后改判：reach 搭不上 what he wants ＝ 搭配问题 ⇒ 补建。
判重三步：
　① dedup "get it" ⇒ 命中 🎓#137（I get it ＝ 听懂）· 🎓#323（同一句）⇒ 否，考点不同
　② dedup "弄到手" ⇒ 零命中
　③ 保留新建；★ 题面⛔ 不许与 #323 用同一句

**我错在哪**
她的：how to reach it　　更地道：how to get it
找法：说"弄到手／得到它"，先看宾语是不是"想要的东西"—— 是就用 get。

**题面**
"那双限量球鞋一上架就被抢光了，我到现在也没弄到手。"（"弄到手"用 **get** 说）

- 2026-09-29 新建 · 学习日复检第 2 组 [9] · 触发原话 `how to reach it`（教练初判"同级近义词"漏建，她追问后补建）
- 2026-09-29 📝 题面整改（§6 换场景 ＋ 正向点名）· 题型 词组 → 整句
  obtain／grab 都合法 ⇒ 改整句、点名 get；换成限量球鞋场景（⛔ 与 🎓#323 不同句）
- 2026-09-30 ✅ 付息日 a 段在池第 2 组 [5] · `… and I still have yet to get my hands on them.`
- 2026-10-02 ❌ 学习日 在池第 3 组 [5] · 「忘了，而且绝版也不会」—— 弄到手 ＝ get it 没调出来（§3.3 "忘了"也是 ❌）。连对 1 → 清零，连错 1
  最小改 `I'd been looking for that out-of-print book for years, and last month I finally got it at a second-hand bookstore.`
  ❌ 宾语是"想要的东西" ⇒ get it（get hold of it 也对）；⛔ reach it（reach 接目标／地点）
  ｜「绝版也不会」⇒ out of print 另建 #393
- 2026-10-03 ✅ 学习日 在池第 1 组 [2] · `I waited six months for this new phone and finally got my hands on it yesterday.` —— got my hands on it（get one's hands on ＝ 弄到手），get 带出来了、没用 reach。连错 1 → 连对 1
- 2026-10-04 ✅ 付息日 a 段在池第 1 组 [2] · `… before he finally got his hand on a pair.` —— "弄到手"用 get（get one's hands on），没用 reach。连对 1 → 2 ⇒ **毕业**
  ★ hand → hands（固定块两只手；10-03 她写对过 got my hands on it）⇒ ⚪#56 只记录，不算本条

### 387 · meander（河弯弯曲曲、慢悠悠地流；人慢悠悠地闲逛）
类型 词汇 ｜ 新建 2026-10-01 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-04 ｜ **🎓 已毕业 2026-10-04**（连对2 ＝ 10-03 ＋ 10-04）｜ 题型 词组

**问题是什么**
**meander** ＝ 河／路弯弯曲曲、慢悠悠地往前：`The river meanders along／through the town.`
也能说人慢悠悠地闲逛：`We meandered around the old town.`
同一格里的邻居（别串）：wind／wind its way（🎓#311，弯弯曲曲，不强调慢）· wander（人闲逛，不说河）· flow（只说流，不带弯和慢）。
判据一句话：又弯又慢 ⇒ meander；只说弯 ⇒ wind；人随便逛 ⇒ wander（meander 也行）。

**怎么发现的**
2026-10-01 学习日 新题 bank:1156（P2）[S7] · 原话 `The river lazily meanders along(这个词组学一下), with a few scattered ducks drifting across the water, …`
她写对了 meanders along，但自己标「这个词组学一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "meander" ⇒ 零命中
　② 中文 dedup "蜿蜒" ⇒ 只命中 🎓#311（V ＋ its way ＋ 方向，是结构，不是 meander 这个词）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」（词不在手边）　　目标：`meander (along)`
找法：描写小河慢悠悠拐来拐去，先落 meander。

**题面**
"一条小河弯弯曲曲、慢悠悠地流过村子"（河道拐来拐去、水流得很慢）

- 2026-10-01 ❌ 首犯 · 学习日 新题 bank:1156（P2）[S7] · 她标「这个词组学一下」· 原话 `The river lazily meanders along(这个词组学一下)`
- 2026-10-02 ❌ 学习日 在池第 2 组 [6] · 「忘了」—— meander 没调出来（§3.3 "忘了"也是 ❌）。连错 1 → 2
  最小改 `a little river meandering through the village`
  ❌ 河又弯又慢地往前流 ＝ meander（一个词自带"拐来拐去＋慢悠悠"）；别串 wind（只弯）· wander（人闲逛）· flow（只说流）
- 2026-10-03 ✅ 学习日 在池第 1 组 [9] · `A small stream lazily meanders through the valley.` —— meanders through（10-02 忘了，今天调出来了）。连错 2 → 连对 1
- 2026-10-04 ✅ 付息日 a 段在池第 1 组 [3] · `A massive river lazily meanders across the plains, drifting slowly to the east.` —— meanders across。连对 1 → 2 ⇒ **毕业**
  ⚠️ 更好版 `A massive river lazily meanders east across the plains.`（meander 自带慢，drifting 一般说漂在水上的东西 ⇒ 只进 diff-2）

### 388 · as the sun was going down（太阳落山的时候；⛔ 书面诗化 the lingering glow of dusk）
类型 词组 ｜ 新建 2026-10-01
状态 连对2 连错0 上次2026-10-04 ｜ **🎓 已毕业 2026-10-04**（连对2 ＝ 10-02 ＋ 10-04）｜ 题型 词组

**问题是什么**
口语讲故事讲到黄昏、夕阳西下 ＝ **as the sun was going down**（when the sun was setting／at sunset 也对）。
`the lingering glow of dusk` 这一类是书面／诗歌里的写法，嘴上说出来像在背稿。
同一格里的邻居（别串）：as the sun was coming up（日出的时候）。
判据一句话：讲到黄昏 ⇒ 用"太阳在下山"这个大白话，不用"暮色余晖"。
★ 词组题判法：when the sun was setting／at sunset 等大白话都算 ✅；只有书面诗化的说法算 ❌。

**怎么发现的**
2026-10-01 学习日 新题 bank:1156（P2）[S7] · 原话 `…, with a few scattered ducks drifting across the water, melting into the lingering glow of dusk.`
⚠️ 不是错，是书面诗化 ⇒ 更好版换成 as the sun was going down（§3.2b 能学的表达 ⇒ 建号）。
书面登记前提核查（§3.2b）：lab/sessions 全部她的产出里没出现过 sunset／the sun went down ⇒ 口语版对她算新表达 ⇒ ⛔ 不走 🎓#206，照常建号。
判重三步：
　① 目标形式 dedup "go down"／"sunset"／"dusk"／"glow" ⇒ 零命中
　② 中文 dedup "落山"／"黄昏"／"夕阳" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`melting into the lingering glow of dusk`（书面诗化）　　更地道：`as the sun was going down`
找法：想写"余晖／暮色"时，换成 as the sun was going down。

**题面**
"太阳快落山的时候"（讲故事时交代时间：天快黑、太阳在往下沉）

- 2026-10-01 📝 新建 · 学习日 新题 bank:1156（P2）[S7] · 触发原话 `melting into the lingering glow of dusk`（⚠️ 书面诗化 ⇒ 更地道的表达，§3.2b 建号）
- 2026-10-02 ✅ 学习日 在池第 3 组 [8] · `As the sun was setting` —— 大白话交代时间，没用书面诗化的暮色余晖（as the sun was setting 是条目列明的合法说法）。首测 ⇒ 连对 1
- 2026-10-04 ✅ 付息日 a 段在池第 2 组 [1] · `It was right around dusk, when we were standing by the beach watching the sun slowly dip below the horizon.` —— 大白话交代黄昏（around dusk ／ watching the sun dip below the horizon），没用书面诗化的暮色余晖；as the sun was going down 没出，条目判法大白话都算对。连对 1 → 2 ⇒ **毕业**

### 390 · get through ＋ 书／一堆活儿（读完、啃完）
类型 词组 ｜ 新建 2026-10-02 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-04 ｜ **🎓 已毕业 2026-10-04**（连对2 ＝ 10-03 ＋ 10-04）｜ 题型 整句

**问题是什么**
**get through** ＋ 一本书／一堆东西 ＝ 从头到尾读完、啃完（口语，带一点"花了劲才弄完"的味道）：
`I got through the whole book in a weekend.` ／ `I still have 200 emails to get through.`
同一格里的邻居（别串）：finish（中性的"读完"）· read through（从头到尾过一遍，偏仔细看）·
get through to sb（打通电话／让对方听进去，另一个意思，🎓#339 正文里列过）。
判据一句话：要说"把一本书／一堆活儿啃完" ⇒ get through ＋ 那个东西；只说中性的"读完了" ⇒ finish 也行。
★ 题型判整句：中文"看完／读完"映射得回 finish，非点名 get through 不可 ⇒ 整句 ＋ 正向点名；
　§6② 她说要学的块第一次出题整块点名（get through），连对 ≥1 之后降回 lemma（through）。

**怎么发现的**
2026-10-02 学习日 在池第 2 组 [5]（#386 题面"这本书我大概三四天就能看完。"）· 原话
`I can get through(读完学习下) this book in about three or four days.`
她写对了 get through，但自己标「读完学习下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "get through" ⇒ 只命中 🎓#339 reach sb（正文邻居列了 get through to sb ＝ 打通电话）⇒ 否：那是另一个意思，考点是 reach 不套 get
　② 中文 dedup "读完" ⇒ 🎓#311 #206 #288 #356，都只是历史行里出现这两个字，考点无关 ⇒ 否；
　　 dedup "finish" ⇒ 🎓#28（get more done）· 🎓#16（get sb to do 四件套），历史行字串，考点无关 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「读完学习下」（块不在手边）　　目标：`get through this book`
找法：说"啃完／看完一本书""把一堆活儿干完"时，先想到 get through。

**题面**
"假期我一口气啃完了三本小说。"（"啃完"用 **get through** 说）

- 2026-10-02 ❌ 首犯 · 学习日 在池第 2 组 [5]（#386 题里）· 她标「读完学习下」· 原话 `I can get through(读完学习下) this book in about three or four days.`
- 2026-10-03 ✅ 学习日 在池第 1 组 [10] · `I got through three novels over the break.` —— got through three novels。连错 1 → 连对 1
- 2026-10-04 ✅ 付息日 a 段在池第 1 组 [4] · `I've got to get through this massive stack of emails this week.` —— get through ＋ 一堆活儿。连对 1 → 2 ⇒ **毕业**

### 391 · up-and-coming（新贵／正在冒头的：an up-and-coming team）
类型 词汇 ｜ 新建 2026-10-02 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-04 ｜ **🎓 已毕业 2026-10-04**（连对2 ＝ 10-03 ＋ 10-04）｜ 题型 整句

**问题是什么**
**up-and-coming** ＝ 正在冒头、越来越厉害的（新贵、后起之秀），放在名词前：
`an up-and-coming team` ／ `an up-and-coming actor` ／ `an up-and-coming neighborhood`
跟 🎓#365 powerhouse 正好一对：a traditional powerhouse vs. an up-and-coming side。
同一格里的邻居（别串）：a rising star（后起之秀，说人）· new money（刚发财的"新贵"，说人）·
upstart（带贬义：不知天高地厚的新贵）。
判据一句话：说一支队／一个人／一个地方"正在冒头" ⇒ up-and-coming；说"刚发财的新贵（人）" ⇒ new money。
★ 题型判整句：中文"新贵"映射得回 rising star／emerging 等一串，非点名 up-and-coming 不可 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-02 学习日 在池第 2 组 [8]（#365 题面"足球界的老牌豪强"）· 她答完 `A traditional powerhouse in European football / A football powerhouse`
后问「一个问题，新贵怎么说」⇒ §2③ 她主动提出 ＋ §3.2b 她不会 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "up-and-coming"／"rising"／"upstart"／"new money" ⇒ 零命中
　② 中文 dedup "新贵"／"冒头" ⇒ 零命中
　③ 最接近的是 🎓#365 powerhouse（老牌强队）⇒ 否：那条考"强"，本条考"新冒头"，两个词
　⇒ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：问「新贵怎么说」（词不在手边）　　目标：`an up-and-coming team`
找法：想说"新贵／后起之秀／正在冒头的" ⇒ up-and-coming 放在名词前。

**题面**
"他是乒乓球界的新贵，今年连赢了好几场大赛。"（"新贵"用 **up-and-coming** 说）

- 2026-10-02 ❌ 首犯 · 学习日 在池第 2 组 [8]（#365 题里）· 她问「一个问题，新贵怎么说」
- 2026-10-03 ✅ 学习日 在池第 2 组 [1] · `He's an up-and-coming table tennis player who has won several major tournaments(这个背一下) this year.` —— up-and-coming 放在名词前。连错 1 → 连对 1
  ｜她自注「这个背一下」⇒ tournament 另建 #395
- 2026-10-04 ✅ 付息日 a 段在池第 1 组 [5] · `The head chef here is an up-and-coming young talent, …` —— up-and-coming。连对 1 → 2 ⇒ **毕业**
  ★ 同句后半 `people here just to try his food` 漏 come ⇒ 新建 #400，不算本条
- 备注 编号：#389 曾被当天撤销的 Singles' Day 条目占用，按 §3.1「作废的号也不复用」，本日新建从 #390 起

### 392 · influencer（网红）
类型 词汇 ｜ 新建 2026-10-02 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-04 ｜ **🎓 已毕业 2026-10-04**（连对2 ＝ 10-03 ＋ 10-04）｜ 题型 词组

**问题是什么**
**influencer** ＝ 网红（在社交媒体上有影响力、能带货的那种人）。
网红店／网红景点 ⇒ 换说法：an Instagrammable spot ／ a trendy place that's all over social media（⛔ 不说 influencer place）。
同一格里的邻居（别串）：celebrity（传统意义上的明星）· content creator（做内容的博主，中性）· go viral（一条内容爆火）。
判据一句话：说"网红（这个人）" ⇒ influencer；说"网红店／网红景点" ⇒ 换说法，不硬套 influencer。

**怎么发现的**
2026-10-02 学习日 在池第 3 组 [3]（#370 题面"短视频平台造就了一大批网红。"）· 原话
`Short-video platforms have created a whole wave of influencers.(网红这个词背一下)`
她写对了 influencers，但自己标「网红这个词背一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "influencer" ⇒ 零命中
　② 中文 dedup "网红" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「网红这个词背一下」（词不在手边）　　目标：`influencers`
找法：说到"网红"这个人，先落 influencer。

**题面**
"一个有几百万粉丝的美妆网红"（在社交平台上推荐化妆品、带货的那种人）

- 2026-10-02 ❌ 首犯 · 学习日 在池第 3 组 [3]（#370 题里）· 她标「网红这个词背一下」· 原话 `Short-video platforms have created a whole wave of influencers.(网红这个词背一下)`
- 2026-10-03 ✅ 学习日 在池第 2 组 [2] · `A beauty influencer with millions of followers.` —— influencer。连错 1 → 连对 1
- 2026-10-04 ✅ 付息日 a 段在池第 1 组 [6] · `travel influencer` —— influencer。连对 1 → 2 ⇒ **毕业**

### 393 · out of print（绝版；an out-of-print book）
类型 词组 ｜ 新建 2026-10-02 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-04 ｜ **🎓 已毕业 2026-10-04**（连对2 ＝ 10-03 ＋ 10-04）｜ 题型 词组

**问题是什么**
书／唱片"绝版了" ＝ **out of print**：`The book is out of print.` ／ `an out-of-print book`（放名词前加连字符）。
同一格里的邻居（别串）：discontinued（商品停产）· sold out（卖光了，以后还会补货）· limited edition（限量版）。
判据一句话：书／唱片不再印 ⇒ out of print；商品不再生产 ⇒ discontinued。

**怎么发现的**
2026-10-02 学习日 在池第 3 组 [5]（#372 题面"那本绝版书我找了好几年，上个月终于在一家旧书店弄到手了。"）· 原话
`忘了，而且绝版也不会`
⇒ §3.2b 她说不会的地方照常建号 ⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "out of print"／"out-of-print"／"discontinued" ⇒ 零命中
　② 中文 dedup "绝版"／"停产" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：「绝版也不会」（词不在手边）　　目标：`that out-of-print book`
找法：说"绝版的书／唱片"，先落 out of print。

**题面**
"一张早就绝版的老唱片"（唱片公司不再压制、市面上买不到新的那种）

- 2026-10-02 ❌ 首犯 · 学习日 在池第 3 组 [5]（#372 题里）· 她说「忘了，而且绝版也不会」
- 2026-10-03 ✅ 学习日 在池第 2 组 [3] · `A classic record that's long been out of print.` —— out of print，"早就"也落成 long been。连错 1 → 连对 1
- 2026-10-04 ✅ 付息日 a 段在池第 1 组 [7] · `That manga series I used to read as a kid that's now completely out of print.` —— out of print。连对 1 → 2 ⇒ **毕业**

### 394 · throw a tantrum（哭闹撒泼、大发脾气）
类型 词组 ｜ 新建 2026-10-03 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-04 未毕业 ｜ 题型 整句

**问题是什么**
**throw a tantrum** ＝ 又哭又闹、撒泼发脾气（多说小孩，也能说大人耍性子）：
`My son threw a tantrum in the supermarket.` ／ `She's throwing a tantrum because she can't have ice cream.`
动词用 **throw**（have a tantrum 也对）。
同一格里的邻居（别串）：have a meltdown（情绪彻底崩溃、大哭大闹）· throw a fit（同义，更随意）· lose one's temper（发火，多说大人）。
判据一句话：小孩又哭又闹、撒泼打滚 ⇒ throw a tantrum；大人发火 ⇒ lose one's temper。
★ 题型判整句：中文"哭闹／撒泼"映射得回 cry and scream／have a meltdown 一串，非点名 tantrum 不可 ⇒ 整句 ＋ 正向点名；
　§6② 她说要学的块第一次出题整块点名（throw a tantrum），连对 ≥1 之后降回 lemma（tantrum），throw 留给她。

**怎么发现的**
2026-10-03 学习日 在池第 1 组 [5]（#383 题面"孩子哭闹的时候，你根本没法跟他讲道理。"）· 原话
`When a kid is throwing a tantrum(这个词背一下), you just can't reason with them.`
她写对了 throwing a tantrum，但自己标「这个词背一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "tantrum" ⇒ 零命中
　② 中文 dedup "哭闹"／"发脾气" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词背一下」（块不在手边）　　目标：`throwing a tantrum`
找法：说"孩子哭闹／撒泼"，先落 throw a tantrum。

**题面**
"我侄子没买到玩具，就在商场里躺地上撒泼打滚。"（"撒泼打滚"用 **throw a tantrum** 说）

- 2026-10-03 ❌ 首犯 · 学习日 在池第 1 组 [5]（#383 题里）· 她标「这个词背一下」· 原话 `When a kid is throwing a tantrum(这个词背一下), you just can't reason with them.`
- 2026-10-04 ✅ 付息日 a 段在池第 1 组 [8] · `… so he threw a huge tantrum on the mall floor.` —— threw a tantrum（首次出题整块点名）。连错 1 → 连对 1；下次点名降回 tantrum

### 395 · tournament（锦标赛／大赛：要打好几轮、最后决出冠军的那种赛事）
类型 词汇 ｜ 新建 2026-10-03 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-04 未毕业 ｜ 题型 词组

**问题是什么**
**tournament** ＝ 一整个赛事，好几支队伍／好几个人打好几轮，最后决出冠军（网球、乒乓球、电竞、象棋常用）：
`win a tournament` ／ `a major tournament` ／ `enter a tournament`
同一格里的邻居（别串）：match（其中一场，两方对打）· game（一局／一场，球类常说）· competition（比赛的总称）·
contest（评比类：a singing contest）· championship（冠军赛，常做赛事名字）。
判据一句话：一整个赛事、打好几轮决出冠军 ⇒ tournament；其中一场 ⇒ match。

**怎么发现的**
2026-10-03 学习日 在池第 2 组 [1]（#391 题面"他是乒乓球界的新贵，今年连赢了好几场大赛。"）· 原话
`He's an up-and-coming table tennis player who has won several major tournaments(这个背一下) this year.`
她写对了 tournaments，但自己标「这个背一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：不会的地方哪怕查到写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "tournament"／"championship"／"competition" ⇒ 零命中
　② 中文 dedup "锦标赛" ⇒ 零命中；"大赛" ⇒ 只命中 #391（今天的题面字串）⇒ 否；"比赛" ⇒ 🎓#378 trophy · 🎓#256 even if（题面字串，考点无关）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个背一下」（词不在手边）　　目标：`several major tournaments`
找法：说"大赛／锦标赛"这种整个赛事，先落 tournament。

**题面**
"今年夏天的电竞大赛"（好几支队伍打好几轮、最后决出冠军的那种赛事）

- 2026-10-03 ❌ 首犯 · 学习日 在池第 2 组 [1]（#391 题里）· 她标「这个背一下」· 原话 `He's an up-and-coming table tennis player who has won several major tournaments(这个背一下) this year.`
- 2026-10-04 ✅ 付息日 a 段在池第 1 组 [9] · `This summer's esports tournament.` —— tournament。连错 1 → 连对 1

### 396 · at stake（押在那儿、利害攸关：how much is at stake）
类型 词组 ｜ 新建 2026-10-03 ｜ ⭐ 她点名要学 ｜ 与 #398 互斥（各自正向点名 at stake／on the line）
状态 连对1 连错0 上次2026-10-04 未毕业 ｜ 题型 整句

**问题是什么**
**at stake** ＝ 可能会输掉／受影响的东西"押在那儿"；它是**表语短语**，前面一定有 be：
`There's a lot at stake.` ／ `How much is at stake?` ／ `Our reputation is at stake.`
⛔ 不能直接放名词前，也不能接在 how much 后面再另挂别的谓语（how much at stake it feels ✗）。
同一格里的邻居（别串）：the stakes are high（stakes 当名词，"赌注很大"）· high-stakes（放名词前当形容词：a high-stakes exam）。
判据一句话：用 at stake ⇒ 前面补 is／are；要放名词前 ⇒ 改用 high-stakes。
★ 题型判整句：考点是 at stake 在句子里的位置（be 后面），孤立翻一个块永远对 ⇒ 整句 ＋ 正向点名 at stake。

**怎么发现的**
2026-10-03 学习日 新题 bank:504（P3 · What would you do if you did not receive a reply after sending out a message?）[S3] · 原话
`It all comes down to how much at stake it feels.(at stake 要学下)`
at stake 位置用错（缺 be、后面又挂 it feels）＋ 她自己标「at stake 要学下」⇒ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "at stake"／"stakes" ⇒ 零命中
　② 中文 dedup "利害"／"关系重大" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`how much at stake it feels`　　正确：`how much is at stake`（想留"感觉上" ⇒ how high the stakes feel）
找法：说出 at stake 之前，先确认前面有 is／are。

**题面**
"这次谈判关系重大，公司的未来都押在上面了。"（"押在上面"用 **at stake** 说）

- 2026-10-03 ❌ 首犯 · 学习日 新题 bank:504（P3）[S3] · 她标「at stake 要学下」· 原话 `It all comes down to how much at stake it feels.(at stake 要学下)`
- 2026-10-04 ✅ 付息日 a 段在池第 1 组 [10] · `There's so much at stack in this negotiate; …` —— so much at stake，前面有 there's（stack 是拼写，§2.1 不算）。连错 1 → 连对 1
  ★ 同句 negotiate 当名词 ⇒ 新建 #399；她标学 on the line ⇒ 新建 #398；均不算本条

### 397 · pull an all-nighter（熬通宵）
类型 词组 ｜ 新建 2026-10-04 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-04 未毕业 ｜ 题型 整句

**问题是什么**
**pull an all-nighter** ＝ 熬一整个通宵（复习、赶活、玩到天亮）；几次就 `pull three all-nighters`。
同一格里的邻居（别串）：stay up late（熬夜，睡得晚，不一定到天亮）· stay up all night（同义大白话）。
判据一句话：一整夜没睡 ⇒ pull an all-nighter；只是睡得晚 ⇒ stay up late。
★ 题型判整句：stay up all night 也合法，中文块映射不回唯一的英文块 ⇒ 不能出词组题，整句 ＋ 正向点名。

**怎么发现的**
2026-10-04 付息日 a 段在池第 1 组 [2]（#372 题"演唱会的票太难抢了，我朋友熬夜抢了三次才弄到手"）· 原话
`my friends pulled three all-nighter(这个词组学一下) before he finally got his hand on a pair.`
她自己标「这个词组学一下」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（§3.2b：说要学的地方哪怕写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "all-nighter" ⇒ 零命中
　② 中文 dedup "通宵" ⇒ 零命中；"熬夜" ⇒ 只命中 🎓#265（考点 good for／bad for，题面碰巧有"熬夜"）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」（块不在手边）　　目标：`pull an all-nighter`
找法：想说"熬了个通宵"，先落 pull an all-nighter。

**题面**
"考试前一晚我熬了个通宵复习。"（"熬了个通宵"用 **pull an all-nighter** 说）
★ 她说要学的块：第一次出题整块点名；连对 ≥1 之后降回 all-nighter（pull／an 留给她）

- 2026-10-04 ❌ 首犯 · 付息日 a 段在池第 1 组 [2]（#372 题里）· 她标「这个词组学一下」· 原话 `my friends pulled three all-nighter(这个词组学一下)`

### 398 · be on the line（押上了、搞砸就没了：My job is on the line.）
类型 词组 ｜ 新建 2026-10-04 ｜ ⭐ 她点名要学 ｜ 与 #396 互斥（各自正向点名 on the line／at stake）
状态 连对0 连错1 上次2026-10-04 未毕业 ｜ 题型 整句

**问题是什么**
**X is on the line** ＝ X 押在这儿了，结果不好 X 就没了（工作、名声、钱、公司的未来）：`My job is on the line.`
同一格里的邻居（别串）：at stake（#396，There's a lot at stake：利害攸关）· at risk（有风险）。
判据一句话：让被押的东西当主语 ＋ is on the line。
★ 与 #396（at stake）分工：两个块意思相近、都对 ⇒ 题面各自正向点名自己的词，互不串（互斥）。

**怎么发现的**
2026-10-04 付息日 a 段在池第 1 组 [10]（#396 题"这次谈判关系重大，公司的未来都押在上面了"）· 原话
`There's so much at stack in this negotiate; the entire future of the company is on the line（这个词组学一下） .`
她自己标「这个词组学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "on the line" ⇒ 零命中
　② 中文 dedup "押"／"风险" ⇒ 命中 #396（at stake，另一个块 ⇒ 两条，题面互斥）· 🎓#85（take on risk，冒风险，另一个块）· 🎓#134 #261（只是正文里带"风险"字样）⇒ 全否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」（块不在手边）　　目标：`X is on the line`
找法：想说"…押上了／饭碗保不住"，让被押的东西当主语 ＋ is on the line。

**题面**
"这场比赛要是输了，教练的饭碗就保不住了。"（"饭碗保不住"用 **on the line** 说）

- 2026-10-04 ❌ 首犯 · 付息日 a 段在池第 1 组 [10]（#396 题里）· 她标「这个词组学一下」· 原话 `the entire future of the company is on the line（这个词组学一下）`

### 399 · negotiation（谈判，名词）／negotiate（动词）
类型 词汇 ｜ 新建 2026-10-04
状态 连对0 连错1 上次2026-10-04 未毕业 ｜ 题型 整句

**问题是什么**
**negotiate** 是动词（`We negotiated for hours.`）；**negotiation** 是名词（`this negotiation` · `rounds of negotiations` · `salary negotiations`）。
同一格里的邻居（别串）：talks（口语常说 trade talks／peace talks，也是名词）。
判据一句话：前面有 this／the／a、或者要当主语／宾语 ⇒ 名词 negotiation。
★ 题型判整句：考点是词性落在哪个位置，孤立翻"谈判"永远是名词 ⇒ 整句，让名词位置在句子里现形。

**怎么发现的**
2026-10-04 付息日 a 段在池第 1 组 [10]（#396 题"这次谈判关系重大，公司的未来都押在上面了"）· 原话
`There's so much at stack in this negotiate; …`
this 后面放了动词 negotiate ⇒ ❌（词性，不在 §3.4 形态类清单里，按 🎓#357 logic／logical 先例建号）。
判重三步：
　① 目标形式 dedup "negotiat" ⇒ 零命中
　② 中文 dedup "谈判" ⇒ 只命中 #396（题面场景，考点 at stake）⇒ 否
　③ 词性同类 🎓#357（logic／logical）· 🎓#232（honest／honesty）—— 都是别的词 ⇒ 否 ⇒ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`in this negotiate`　　正确：`in this negotiation`
找法："谈判"前面挂了 this／the，就落名词 negotiation。

**题面**
"经过好几轮谈判，双方终于在价格上达成了一致。"（"谈判"用 **negotiate** 这个词说）
★ 点名给 lemma negotiate，名词形式留给她（"好几轮谈判"逼出 rounds of negotiations）

- 2026-10-04 ❌ 首犯 · 付息日 a 段在池第 1 组 [10]（#396 题里）· 原话 `There's so much at stack in this negotiate`
  最小改 `There's so much at stake in this negotiation`
  ❌ negotiate 是动词；this 后面要名词 negotiation

### 400 · come here just to ＋ 动词（专门来做某事；⛔ people here just to …漏了 come）
类型 结构 ｜ 新建 2026-10-04
状态 连对0 连错1 上次2026-10-04 未毕业 ｜ 题型 整句

**问题是什么**
"很多人专门为他来（吃饭）" ＝ `People come here just to try his food.`（大老远专门来：`come all the way here just to …`）
中文的"来／去"很轻、容易被吞；英语这半句必须有动词 come／go，just to ＋ 动词挂在后面说目的。
同一格里的邻居（别串）：🎓#43 come to your city（巡演到某地的块）。
判据一句话：说"专门来…"，句子里有没有 come？没有 ⇒ 这半句没谓语。

**怎么发现的**
2026-10-04 付息日 a 段在池第 1 组 [5]（#391 题"这家店的主厨是个正在冒头的年轻厨师，很多人专门为他来吃饭"）· 原话
`The head chef here is an up-and-coming young talent, and people here just to try his food.`
后半句漏了 come，整句没有谓语 ⇒ ❌（按 #385「漏 was 整句没谓语」先例，落到具体句型建号）。
判重三步：
　① 目标形式 dedup "just to"／"come here"／"come all the way" ⇒ 命中 🎓#43（come to your city：巡演到某地，另一个块）· 🎓#363（只是历史里出现 just to 字串，考点 appeal to）⇒ 否
　② 中文 dedup "专门" ⇒ 命中 🎓#57（date night，题面里有"专门"二字）· #12（形态类·时态，正文带"专门"）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`people here just to try his food`　　正确：`people come here just to try his food`
找法：说"专门来…"，先落 come，再接 just to ＋ 动词。

**题面**
"很多游客专门来这条老街拍照。"（"专门来"用 **just to** 说）

- 2026-10-04 ❌ 首犯 · 付息日 a 段在池第 1 组 [5]（#391 题里）· 原话 `people here just to try his food`
  最小改 `people come here just to try his food`
  ❌ "专门为他来"的"来"被吞了 ⇒ 这半句没有动词

### 401 · fruit platter（果盘／水果拼盘）
类型 词汇 ｜ 新建 2026-10-04 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-04 未毕业 ｜ 题型 词组

**问题是什么**
**fruit platter** ＝ 切好摆在大浅盘里的水果拼盘（派对、饭后端上来的那种）；platter ＝ 拼盘用的大浅盘：a cheese platter ／ a seafood platter。
同一格里的邻居（别串）：a plate of fruit（一盘水果，大白话也对）· tray（托盘）。
判据一句话：一大盘拼好摆好的 ⇒ platter；就是一盘 ⇒ a plate of。
★ 词组题判法：a plate of fruit 合法且贴题 ⇒ 照判 ✅；中文写"拼盘"把语境压向 platter。

**怎么发现的**
2026-10-04 付息日 a2 复检第 3 组 [3]（#98 题"这个果盘是用苹果和葡萄摆出来的"）· 原话
`This fruit platter(这个词组背一下) is spelt out in apples and grapes.`
她自己标「这个词组背一下」⇒ §2③ 建号，判 ❌（§3.2b：说要学的地方哪怕写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "platter" ⇒ 零命中
　② 中文 dedup "果盘" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组背一下」（词不在手边）　　目标：`a fruit platter`
找法：说"果盘／拼盘"，先落 platter。

**题面**
"生日派对上端出来的一大盘水果拼盘"（切好摆在大浅盘里、五颜六色的那种）

- 2026-10-04 ❌ 首犯 · 付息日 a2 复检第 3 组 [3]（#98 题里）· 她标「这个词组背一下」· 原话 `This fruit platter(这个词组背一下) is spelt out in apples and grapes.`

### 402 · pull off ＋ 难事（办成、搞定）
类型 词组 ｜ 新建 2026-10-04 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-04 未毕业 ｜ 题型 整句

**问题是什么**
**pull sth off** ＝ 把一件难办的事办成了（婚礼、演出、惊喜派对、一桌大菜）：`They pulled it off.` ／ `pull off a surprise party`。
同一格里的邻居（别串）：manage to do（大白话"设法做成"）· carry out（执行计划，偏正式）。
判据一句话：强调"这事挺难、居然办成了" ⇒ pull off；宾语是代词放中间 pull it off。
★ 题型判整句：manage to 也合法，中文块映射不回唯一的英文块 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-04 付息日 a2 复检第 3 组 [4]（#340 题"会做饭是一回事；再往上一档，是能张罗出一桌像样的年夜饭"）· 原话
`Knowing how to cook is one thing; a step up from that is pulling off(这个词组学一下) a proper New Year's Eve feast.`
她自己标「这个词组学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "pull off" ⇒ 零命中
　② 中文 dedup "搞定" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」（块不在手边）　　目标：`pull off ＋ 难事`
找法：说"居然办成了／搞定了"，先落 pull off。

**题面**
"只有一周时间准备，他们居然把这场婚礼办成了。"（"办成"用 **pull off** 说）
★ 她说要学的块：第一次出题整块点名；连对 ≥1 之后降回 pull（off 留给她）

- 2026-10-04 ❌ 首犯 · 付息日 a2 复检第 3 组 [4]（#340 题里）· 她标「这个词组学一下」· 原话 `a step up from that is pulling off(这个词组学一下) a proper New Year's Eve feast`

### 403 · squeeze on(to) ＋ 车（挤上车）
类型 词组 ｜ 新建 2026-10-04 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-04 未毕业 ｜ 题型 词组

**问题是什么**
**squeeze on** ／ **squeeze onto the train** ＝ 人多、硬挤上车；挤进去 ＝ squeeze in ／ squeeze into a car。
同一格里的邻居（别串）：🎓#108 packed（车厢人多的状态）· get on（上车，不带"挤"）。
判据一句话：说"挤上去"这个动作 ⇒ squeeze on(to)；说"车厢很挤"的状态 ⇒ packed。
★ 词组题判法：cram onto 合法且贴题 ⇒ 照判 ✅。

**怎么发现的**
2026-10-04 付息日 a2 复检第 3 组 [9]（#60 题"早高峰坐地铁的话，基本都挤不上去"）· 原话
`If you take the subway during peak morning hours, you can barely squeeze on.(这个词组学一下)`
她把「这个词组学一下」标在句末 squeeze on 后面 ⇒ 按 squeeze on 建号，§2③ 判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "squeeze" ⇒ 零命中
　② 中文 dedup "挤" ⇒ 命中 🎓#108 packed（状态，不是动作）· 🎓#107 jammed（车堵）· 🎓#311（V one's way ＋ 方向的结构）· 🎓#212（压缩形容词出口）⇒ 都不是"挤上车"这个块 ⇒ 全否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」（块不在手边）　　目标：`squeeze on(to) ＋ 车`
找法："挤上／挤进"先落 squeeze。

**题面**
"晚高峰好不容易才挤上公交"（人太多，侧着身子硬塞进车厢）

- 2026-10-04 ❌ 首犯 · 付息日 a2 复检第 3 组 [9]（#60 题里）· 她标「这个词组学一下」· 原话 `you can barely squeeze on.(这个词组学一下)`

### 404 · overly ＋ 形容词（过度…、过于…）
类型 词汇 ｜ 新建 2026-10-04 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-04 未毕业 ｜ 题型 整句

**问题是什么**
**overly** ＋ 形容词 ＝ 过度、过于（说"超出合适的那个度"）：overly ambitious ／ overly cautious ／ overly protective。
同一格里的邻居（别串）：too ＋ 形容词（太…，口语最常用）· over- 前缀拼成一个词的（overprotective ／ overworked）。
判据一句话：说"过度／过于 X" ⇒ overly X（或 too X）；已经拼成一个词的那几个用 over-。
★ 题型判整句：too X ／ overprotective 都合法，中文块映射不回唯一的英文块 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-04 付息日 d 段重答 bank:521（R19 · P3 · Is it good for a person to be ambitious?）[S3] · 原话
`But being overly（过度学一下) ambitious can make you lose sight of things …`
她自己标「过度学一下」⇒ §2③ 建号，判 ❌（§3.2b：说要学的地方哪怕写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "overly"／"too ambitious"／"ambitious" ⇒ 零命中
　② 中文 dedup "过于" ⇒ 零命中；"过度" ⇒ 命中 🎓#50 #134 #148 #263 #319 #9 #265（都只是正文里写着"过度泛化"，考点不是这个词）⇒ 全否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「过度学一下」（词不在手边）　　目标：`overly ＋ 形容词`
找法：想说"过度／过于…"，先落 overly ＋ 形容词。

**题面**
"有些家长对孩子保护过度，什么都不让他们自己做。"（"保护过度"用 **overly** 说）

- 2026-10-04 ❌ 首犯 · 付息日 d 段重答 bank:521 [S3] · 她标「过度学一下」· 原话 `But being overly（过度学一下) ambitious`

### 405 · just as X, if not more so（同样 X，甚至更 X）
类型 词组 ｜ 新建 2026-10-04 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-04 未毕业 ｜ 题型 整句

**问题是什么**
比较时先说"一样…"，再补"甚至更…"：`Family is just as important as work, if not more so.` —— so 指回前面的形容词。
同一格里的邻居（别串）：as good as, if not better than（"不比…差，甚至更好"）· even more ＋ 形容词（直接说"更…"）。
判据一句话：前面是 as ＋ 形容词 ⇒ 补 if not more so；口语里光说 if not more 也能听到（不算错）。
★ 题型判整句：块要挂在 just as X 后面才现形 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-04 付息日 d 段重答 bank:521（R19 · P3）[S3] · 原话
`… lose sight of things that are just as precious, if not more（这个词组学一下)—like everyday interactions …`
她自己标「这个词组学一下」⇒ §2③ 建号，判 ❌（§3.2b）；更好版补成 if not more so（⚠️，不算错）。
判重三步：
　① 目标形式 dedup "if not"／"more so" ⇒ 零命中
　② 中文 dedup "甚至更" ⇒ 只命中 🎓#290（收尾块 for totally different reasons，正文里带"甚至更"字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`just as precious, if not more`（自己标学）　　目标：`just as precious, if not more so`
找法："一样…甚至更…"，先说 just as X，再补 if not more so。

**题面**
"陪孩子的时间跟赚钱一样重要，甚至更重要。"（"甚至更重要"用 **if not more so** 说）
★ 她说要学的块：第一次出题整块点名；连对 ≥1 之后降回 if not（more so 留给她）

- 2026-10-04 ❌ 首犯 · 付息日 d 段重答 bank:521 [S3] · 她标「这个词组学一下」· 原话 `just as precious, if not more（这个词组学一下)`

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

