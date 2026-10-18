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

### 474 · 交通方便（从这儿出门去别处方便）⇒ convenient for getting around（⛔ a place that's convenient to get around）
类型 搭配 ｜ 新建 2026-10-13
状态 连对1 连错0 上次2026-10-14 未毕业 ｜ 题型 整句

**问题是什么**
说住的地方、酒店**交通方便**（从这儿出门去别处方便）：`The apartment is really convenient for getting around.` · `It's close to public transport.`
⛔ **X is convenient／easy to get around** ＝ 在 X **里面**走动方便（`The city is easy to get around.`）——
挂在一套房子上就成了"在屋里走来走去方便"。
同一格里的邻居（别串）：🎓#50 easy vs convenient（convenient ＝ 方式省事；难度低 ⇒ easy）·
The city is easy to get around（城市本身好逛，主语就是 get around 的地方）。
判据一句话：get around 的是主语本身（城市、景区）⇒ X is easy to get around；从这儿出发去别处（房子、酒店）⇒ convenient for getting around ／ close to public transport。
★ 与 🎓#50 分工：#50 判"难度低该用 easy、不用 convenient"；本条判 get around 的对象挂错了（换成 easy to get around 照样错）⇒ 两条。
★ 题型判整句：考点是 get around 挂在谁身上，要靠句子才现形；零提示（合法说法很多，考的是别落到 the place is convenient to get around）。

**怎么发现的**
2026-10-13 学习日 复检第 4 组 [1]（🎓#96 题面"我想租一套不吵、交通又方便的房子。"）· 原话
`I'm looking to rent a place that's quiet and convenient to get around.`
diff-2 ⚠️（不是 ❌）：意思听得懂，但 a place that's convenient to get around 字面是"在这地方里面走动方便" ⇒ §3.2b 能学的表达 ⇒ 建号。
判重三步：
　① 目标形式 dedup "get around"／"public transport"／"交通" ⇒ 🎓#45 walk to work · 🎓#218 traffic management（题面字样）⇒ 否，无关
　② dedup "convenient" ⇒ 🎓#50 easy vs convenient ⇒ 否：#50 管"难度低用 easy"，本条管 get around 的对象（换 easy 照样错）
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`a place that's quiet and convenient to get around`　　更地道：`a place that's quiet and convenient for getting around`（或 `close to public transport`）
找法：说完 X is convenient／easy to get around，回头问一句 —— 是在 X 里面走，还是从 X 出发？从 X 出发 ⇒ 换 for getting around。

**题面**
"我们住的酒店就在地铁站旁边，出去玩交通特别方便。"
　　★ 零提示：convenient for getting around ／ close to the subway ／ easy to get around from there 都算对；她要改掉的是 the hotel is convenient to get around
★ 目标形式（教练看，⛔ 不进发题稿）：Our hotel is right next to the subway station, so it's really convenient for getting around.

- 2026-10-13 新建 · 学习日 复检第 4 组 [1]（#96 题里）· diff-2 ⚠️ · 原话 `I'm looking to rent a place that's quiet and convenient to get around.` ⇒ 更好版 convenient for getting around
- 2026-10-14 ✅ 学习日 在池第 3 组 [1] · `The hotel we stayed at was right next to the subway station, so it was super easy to get around.` —— "方便"挂在 get around 这件事上（it was super easy to get around），没说成 the hotel is convenient to get around。首测 ⇒ 连对 1

### 477 · make sth feel special（让这一天／这件事显得特别；⛔ elevates the day above ordinary routine）
类型 词组 ｜ 新建 2026-10-13
状态 连对1 连错0 上次2026-10-14 未毕业 ｜ 题型 整句

**问题是什么**
**make ＋ 东西 ＋ feel special** ＝ 让某天／某件事显得特别、跟平常不一样：
`A nice dinner makes the day feel special.` · `Little things like that make birthdays feel special.`
同一格里的邻居（别串）：feel ＋ 形容词（feel special）vs feel like ＋ 名词（🎓#351 it feels like a mini-escape）·
make sb feel special（让人觉得被重视，挂人）。
判据一句话：想说"让 X 不同于平常、有仪式感" ⇒ make X feel special；⛔ 别去够 elevate … above ordinary routine 这类写作块（🎓#206 同族）。
★ 题型判整句："让…变得特别"能落到 make it special／make it memorable 一串合法说法，make ＋ 宾语 ＋ feel 的挂法要靠句子现形 ⇒ 整句 ＋ 正向点名。

**怎么发现的**
2026-10-13 学习日 ③ 新题 bank:1296（P3 · Why are some people willing to spend a lot of money on meals on special days?）S1 · 原话
`… they are purchasing an unforgettable experience and a sense of ritual that elevates the day above ordinary routine.`
diff-2 ⚠️（不是 ❌）：书面块，口语版她没产出过（扫她历年原话：feel special 零命中）⇒ §3.2b 不走书面登记，照常建号。
判重三步：
　① 目标形式 dedup "feel special" ⇒ 零命中
　② 中文 dedup "特别" ⇒ 🎓#289 obsessed · 🎓#429 grudge 等，只是"特别"字样 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`a sense of ritual that elevates the day above ordinary routine`　　更地道（口语）：`a sense of ritual that makes the day feel special`
找法：想说"让…显得特别／不一样"，先落 make it feel special。

**题面**
"生日那天朋友们给我准备了一个小惊喜，让这一天变得特别不一样。"（"变得特别不一样"用 **feel special** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My friends planned a little surprise for my birthday, which made the day feel really special.

- 2026-10-13 新建 · 学习日 ③ 新题 bank:1296 S1 · diff-2 ⚠️ 书面块 · 原话 `… a sense of ritual that elevates the day above ordinary routine.` ⇒ 更好版 makes the day feel special
- 2026-10-14 ✅ 学习日 在池第 3 组 [2] · `My friends threw me a little surprise on my birthday, and it really made the day feel special.` —— made the day feel special。首测 ⇒ 连对 1
  ⚠️ diff-2：threw me a little surprise → planned a little surprise for me ⇒ 新建 #481

### 478 · show how much you care（用行动表心意：It's a way of showing how much you care；⛔ acts as a tangible signal of love）
类型 词组 ｜ 新建 2026-10-13
状态 连对1 连错0 上次2026-10-14 未毕业 ｜ 题型 整句

**问题是什么**
**show (sb) how much you care ／ how much you love them** ＝ 用行动表达心意：
`Cooking for someone is a way of showing how much you care.` · `It shows how much you love them.`
how much 后面用陈述语序（🎓#59）。
同一格里的邻居（别串）：a (tangible) sign of love（名词说法，tangible 搭 sign 不搭 signal）· mean a lot to sb（对某人意义重大）。
判据一句话：说"表达心意／爱" ⇒ show how much you care；⛔ 别去够 acts as a tangible signal of …（🎓#206 同族）。
★ 题型判整句：how much 后面的主语 ＋ 动词要靠句子现形；新表达第一次出题点 show how much。

**怎么发现的**
2026-10-13 学习日 ③ 新题 bank:1296 S2 · 原话
`Plus, Spending generously on a meal acts as a tangible signal of love and appreciation.`
diff-2 ⚠️（不是 ❌）：书面块，口语版她没产出过（扫她历年原话：show how much／a way of showing 零命中）⇒ §3.2b 照常建号。
判重三步：
　① 目标形式 dedup "how much you care" ⇒ 零命中；"how much" ⇒ 🎓#59 嵌入疑问陈述语序（规则，不是这个表达）· 🎓#396 等字样 ⇒ 否
　② 中文 dedup "心意" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`acts as a tangible signal of love and appreciation`　　更地道（口语）：`is a way of showing how much you love and appreciate someone`
找法：想说"表达心意"，先落 show how much ＋ 主语 ＋ care／love。

**题面**
"我妈每次都给我寄一大箱家乡特产，这是她表达心意的方式。"（"表达心意"用 **show how much** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My mom always sends me a huge box of local specialties from home — it's her way of showing how much she cares.

- 2026-10-13 新建 · 学习日 ③ 新题 bank:1296 S2 · diff-2 ⚠️ 书面块 · 原话 `Plus, Spending generously on a meal acts as a tangible signal of love and appreciation.` ⇒ 更好版 is a way of showing how much you love and appreciate someone
- 2026-10-14 ✅ 学习日 在池第 3 组 [3] · `My mom sends me a huge box of specialties from home every time—it's just her way of showing how much she cares.` —— her way of showing how much she cares。首测 ⇒ 连对 1
  ⚠️ diff-2：sends me … every time → always sends me …（偏好，不建号）

### 479 · bring sb closer (together)（拉近感情；⛔ provides a space to deepen their emotional connection）
类型 词组 ｜ 新建 2026-10-13
状态 连对1 连错0 上次2026-10-14 未毕业 ｜ 题型 整句

**问题是什么**
**bring ＋ 人 ＋ closer (together)** ＝ 让人感情更近：`Cooking together brings us closer.` · `The trip really brought the two of them closer together.`
不带宾语：grow closer ／ get closer。
同一格里的邻居（别串）：get everyone together（把人聚齐 —— 她 2026-09-19 说过，是"人到齐"不是"感情近"）· bond (with sb)（培养感情）。
判据一句话：人到齐 ⇒ get everyone together；感情变近 ⇒ bring sb closer。
★ 题型判整句：bring ＋ 人 ＋ closer 的宾语位置要靠句子现形；新表达第一次出题点 closer。

**怎么发现的**
2026-10-13 学习日 ③ 新题 bank:1296 S3 · 原话
`It provides a unique space for family or partners to deepen their emotional connection.`
diff-2 ⚠️（不是 ❌）：书面块（心理学文章腔），口语版她没产出过（扫她历年原话：closer／bond 零命中；getting everyone together 意思不同）⇒ §3.2b 照常建号。
判重三步：
　① 目标形式 dedup "closer"／"together" ⇒ 零命中
　② 中文 dedup "感情" ⇒ 🎓#440 sentimental · 🎓#363 appeal to emotions（"情绪"字样）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`It provides a unique space for family or partners to deepen their emotional connection.`　　更地道（口语）：`A meal like that brings family or partners closer together.`
找法：想说"拉近感情／关系更好了"，先落 bring … closer。

**题面**
"一起照顾那只小狗，让我们一家人感情近了不少。"（"感情近了"用 **closer** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：Taking care of that puppy together really brought our family closer.

- 2026-10-13 新建 · 学习日 ③ 新题 bank:1296 S3 · diff-2 ⚠️ 书面块 · 原话 `It provides a unique space for family or partners to deepen their emotional connection.` ⇒ 更好版 brings family or partners closer together
- 2026-10-14 ✅ 学习日 在池第 3 组 [4] · `Taking care of that little dog together really brought our family closer.` —— brought our family closer。首测 ⇒ 连对 1

### 480 · **change jobs**（换工作：jobs 复数、不带冠词；⛔ change the job／change job）
类型 搭配 ｜ 新建 2026-10-14
状态 连对2 连错0 上次2026-10-17 ｜ **🎓 已毕业 2026-10-17** ｜ 题型 整句

**问题是什么**
"换工作"＝ **change jobs**：从一份工作换到另一份，涉及两份工作 ⇒ jobs 用复数、前面不带 the／my。
同一格里的邻居（别串）：switch jobs（同义，同样复数）· change trains（换乘）· switch schools（转学）· swap seats（换座位）——"从一个换到另一个"这一类都是复数、不带冠词；
change the job／change my job ＝ 把这份工作本身改了（改内容），不是换一份。
判据一句话：说"换 X"指从一个 X 换到另一个 ⇒ change／switch ＋ 复数 X，不带冠词。
★ 题型判整句："换工作"能落到 find a new job／get a new job 一串合法说法 ⇒ 整句 ＋ 正向点名 change；jobs 的复数与有没有 the 要她自己出。

**怎么发现的**
2026-10-14 学习日 在池第 1 组 [9]（#463 题面"换工作之前，我跟我老公坐下来把利弊都好好聊了一遍。"）· 原话
`Before changing the job, my husband and I sat down and talked through the pros and cons.`
talk through 本身对（#463 ✅），changing the job ❌。lab 之前犯过一次：coach/sessions/2026-06-24.md:30 `change job`→change jobs ⇒ 不是手滑，是块没装上。
判重三步：
　① 目标形式 dedup "change jobs"／"changing jobs" ⇒ 零命中
　② 中文 dedup "换工作" ⇒ 🎓#425 make the move（考"迈出那一步"）· 🎓#361 get off work（考"下班"）—— 只是题面／历史里有"换工作"字样，目标形式不同 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`Before changing the job`　　正确：`Before changing jobs`
找法：说"换工作／换学校／换车"先想"从一个换到另一个"⇒ 名词变复数、去掉 the。

**题面**
"我表姐去年换了三次工作，现在终于找到一份自己喜欢的了。"（"换工作"用 **change** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My cousin changed jobs three times last year, and she's finally found one she likes.

- 2026-10-14 ❌ 首犯 · 学习日 在池第 1 组 [9]（#463 题里）· 原话 `Before changing the job, my husband and I sat down and talked through the pros and cons.` ⇒ 最小改 Before changing jobs
- 2026-10-16 ✅ 学习日 在池第 1 组 [7] · `My cousin changed jobs three times last year, and now she's finally landed one she actually likes.`。连错 1 → 连对 1
- 2026-10-17 ✅ 付息日 在池第 1 组 [2] · `My uncle changed jobs quite a few times when he was younger …`。连对 1 → 2 ⇒ 🎓

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

### 482 · **far from** ＋ 形容词／enough（远远不够、远不是：far from enough · far from perfect；⛔ far away from enough）
类型 搭配 ｜ 新建 2026-10-14
状态 连对2 连错0 上次2026-10-17 ｜ **🎓 已毕业 2026-10-17** ｜ 题型 整句

**问题是什么**
**far from ＋ 形容词／enough** ＝ "远远不…／远不是…"：`It's far from enough.` · `The plan is far from perfect.` · `far from easy`。
同一格里的邻居（别串）：far away from ＋ 地点 ＝ 离…很远（说距离：far away from the city）· nowhere near enough（更口语的"差得远"）· not nearly enough（同义）。
判据一句话：说距离 ⇒ far away from ＋ 地方；说程度差得远 ⇒ far from ＋ 形容词（away 不能进来）。
★ 题型判整句："远远不够"能落到 not enough at all／nowhere near enough 一串合法说法，far from 后面直接挂形容词要靠句子现形 ⇒ 整句 ＋ 正向点名 far from。

**怎么发现的**
2026-10-14 学习日 复检第 4 组 [8]（🎓#315 题面"学校对留学生的支持还远远不够。"）· 原话
`The school's support for international students is far away from enough.`
support for 本身对（#315 ✅），far away from enough ❌（把说距离的 far away from 用到了程度上）。
判重三步：
　① 目标形式 dedup "far from" ⇒ 🎓#14 well away（"离马路远远的"，说距离）⇒ 本条是程度、不是距离 ⇒ 否；dedup "far away" ⇒ 🎓#14 · 🎓#203（"离地铁远"题面字样）⇒ 否；"nowhere near" ⇒ 零命中
　② 中文 dedup "远远不够" ⇒ 只命中今天的 #315 题面 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`is far away from enough`　　正确：`is far from enough`
找法：说"远远不够／远不是"先落 far from，后面直接接形容词或 enough —— away 只在说距离时出现。

**题面**
"这点工资养一家人远远不够。"（"远远不够"用 **far from** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：This salary is far from enough to support a family.

- 2026-10-14 ❌ 首犯 · 学习日 复检第 4 组 [8]（#315 题里）· 原话 `The school's support for international students is far away from enough.` ⇒ 最小改 is far from enough
- 2026-10-16 ✅ 学习日 在池第 1 组 [8] · `This pay is far from enough to support a whole family.`。连错 1 → 连对 1
- 2026-10-17 ✅ 付息日 在池第 1 组 [3] · `What we've saved so far is far from enough to cover a down payment.`。连对 1 → 2 ⇒ 🎓（同句「首付」她标要学 ⇒ 新建 #500）

### 483 · **on holidays／on public holidays**（节假日；⛔ on holiday ＝ 在度假）
类型 搭配 ｜ 新建 2026-10-14
状态 连对2 连错0 上次2026-10-17 ｜ **🎓 已毕业 2026-10-17** ｜ 题型 整句

**问题是什么**
节假日（法定放假的那几天）⇒ **on holidays** ／ **on public holidays** ／ during the holidays。
同一格里的邻居（别串）：on holiday ＝ 在度假、休假中（She's on holiday in Spain.）· go on holiday ＝ 去度假 · on weekends（周末，同样复数）。
判据一句话："在那些放假的日子里"⇒ on holidays ／ public holidays；"人在度假"⇒ on holiday。
★ 题型判整句："节假日"挂在什么上（开门、营业）要靠句子现形；正向点名 holidays，带不带 s／加不加 public 留给她。

**怎么发现的**
2026-10-14 学习日 复检第 4 组 [4]b（🎓#343 题面"健身房节假日的营业时间"）· 原话
`the opening hours of the gym on holiday`
opening hours 本身对（#343 ✅），on holiday ❌（说成了"在度假"）。
判重三步：
　① 目标形式 dedup "holiday" ⇒ 🎓#301 enjoy your stay（历史字串）⇒ 否；"public holiday" ⇒ 零命中
　② 中文 dedup "节假日" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`on holiday`（节假日）　　正确：`on holidays` ／ `on public holidays`
找法：说"节假日"先想是不是在说"人去度假"—— 不是 ⇒ holidays 带 s，或说 public holidays。

**题面**
"这家银行节假日不开门。"（"节假日"用 **holidays** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：This bank is closed on public holidays.

- 2026-10-14 ❌ 首犯 · 学习日 复检第 4 组 [4]b（#343 题里）· 原话 `the opening hours of the gym on holiday` ⇒ 最小改 on holidays ／ 更好版 the gym's opening hours on public holidays
- 2026-10-16 ✅ 学习日 在池第 1 组 [9] · `This bank is closed on public holidays.`。连错 1 → 连对 1
- 2026-10-17 ✅ 付息日 在池第 1 组 [4] · `This supermarket is open as usual during the holidays.`（during the holidays 是正文列着的合法说法，没落到 on holiday）。连对 1 → 2 ⇒ 🎓

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

### 485 · **smear**（抹、涂得一塌糊涂：smear lipstick all over her face · smear sth on sth）
类型 词汇 ｜ 新建 2026-10-14 ｜ ⭐ 她点名要学
状态 连对2 连错0 上次2026-10-17 ｜ **🎓 已毕业 2026-10-17** ｜ 题型 整句

**问题是什么**
**smear** ＝ 把又油又黏的东西胡乱抹开、抹得到处都是：`smear lipstick all over her face` · `smear butter on the bread` · `The kid smeared paint on the wall.`
同一格里的邻居（别串）：spread（均匀地抹开，正常地涂：spread butter on toast）· put on（正常化妆：put on lipstick）· rub（揉、搓进去：rub in sunscreen）。
判据一句话：抹得乱七八糟、到处都是 ⇒ smear；正常地涂一层 ⇒ spread ／ put on。
★ 题型判整句："抹得满墙都是"能落到 get … all over／spread 一串说法，smear sth on／all over sth 的挂法要靠句子现形 ⇒ 整句 ＋ 正向点名 smear（她点名要学的新词，连对 ≥1 后照旧点 lemma）。

**怎么发现的**
2026-10-14 学习日 复检第 4 组 [10]（🎓#318 题面"我记得有一次，我女儿五岁的时候，偷偷拿我的口红涂了一脸。"）· 原话
`One time, when my daughter was five, she stole my lipstick and smeared(学下这个词) it all over her face.`
她写对了 smeared … all over，但自己标「学下这个词」⇒ §2③ 她说要学 ⇒ 建号，判 ❌（同 🎓#433 先例）。
判重三步：
　① 目标形式 dedup "smear"／"spread" ⇒ 零命中
　② 中文 dedup "抹" ⇒ 🎓#445 dust（题面"手指一抹"字样）· 🎓#465（字串）；"涂" ⇒ 🎓#293（"涂鸦"字样）⇒ 都不是"抹开"这个动作 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「学下这个词」（词不在手边）　　目标：`smeared it all over her face`
找法：说"抹了一脸／抹得到处都是"先落 smear … all over。

**题面**
"小侄子把巧克力抹得满墙都是。"（"抹得满墙都是"用 **smear** 说）
★ 目标形式（教练看，⛔ 不进发题稿）：My little nephew smeared chocolate all over the wall.

- 2026-10-14 ❌ 首犯 · 学习日 复检第 4 组 [10]（#318 题里）· 她标「学下这个词」· 原话 `One time, when my daughter was five, she stole my lipstick and smeared(学下这个词) it all over her face.`
- 2026-10-16 ✅ 学习日 在池第 1 组 [10] · `My little nephew smeared chocolate all over the wall.`。连错 1 → 连对 1
- 2026-10-17 ✅ 付息日 在池第 1 组 [5] · `After eating skewers, my little brother smeared grease all over the couch.`。连对 1 → 2 ⇒ 🎓

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
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

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
状态 连对0 连错1 上次2026-10-16 未毕业 ｜ 题型 整句

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

### 496 · **be overrun with** ＋ 坏东西（到处都是、泛滥成灾：a city overrun with crime）
类型 词组 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-16 未毕业 ｜ 题型 整句

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

### 497 · **have ＋ 东西 ＋ done** ＝ 遭遇（had my phone stolen）；人出事 ⇒ watched X get …
类型 结构 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-16 未毕业 ｜ 题型 整句

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

### 498 · **vigilante**（不靠警察、私自出手惩治坏人的人；义警）
类型 词汇 ｜ 新建 2026-10-16 ｜ ⭐ 她点名要背
状态 连对0 连错1 上次2026-10-16 未毕业 ｜ 题型 词组

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

### 499 · **Take X —**（拿 X 来说：举一个真实的具体例子起手）
类型 句型 ｜ 新建 2026-10-16
状态 连对0 连错0 上次— 未毕业 ｜ 题型 整句

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

