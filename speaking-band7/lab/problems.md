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

### 271 · recently／lately／so far 这一族默认拉完成时（要用一般现在时就换成 these days）
类型 语法 ｜ **合并条·出题多句覆盖**（§3.2c）｜ 新建 2026-08-23
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ **合并条·出题多句覆盖** ｜ 题型 整句 ｜ **回潮 2026-10-10**（08-25 毕业 → 10-10 复检 #21 题里写成 `keeps forgetting his keys recently`，recently 配了一般现在时，撤销毕业、连对清零）

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
① recently ｜ 08-23 ❌（首犯）· 08-24 ✅ · 08-25 ✅ · 09-11 ✅ · 10-04 ✅ · 10-11 ✅
② lately ｜ 08-24 ✅ · 08-25 ✅ · 09-11 ✅ · 10-04 ✅ · 10-11 ✅
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

### 429 · hold a grudge (against sb)（记仇）
类型 词组 ｜ 新建 2026-10-07 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 整句

**问题是什么**
**hold a grudge** ＝ 心里一直记着别人的不好、不肯放下：He never holds a grudge. ／ hold a grudge against sb（记某人的仇）。
同一格里的邻居（别串）：let it go（放下、算了）· forgive and forget（原谅了也不再提）· get over it（过去了、缓过来了）。
判据一句话：说"记仇／一直耿耿于怀" ⇒ hold a grudge (against sb)；说"不记仇／放下了" ⇒ never holds a grudge ／ let it go。
★ 性子 vs 一次：说一个人"特别记仇"（性子）⇒ really holds grudges（复数 ＝ 老这样）；说"对某人记着一笔仇"（一次具体的）⇒ hold a (huge) grudge against sb。
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
- 2026-10-08 ❌ 付息日 a 段在池第 2 组 [8] · 「忘了」—— hold a grudge 没调出来（§3.3 "忘了"也是 ❌）。连错 1 → 2
  最小改 `My sister really holds a grudge — I took a piece of candy from her when we were kids, and she still brings it up.`
  ❌ "记仇" ＝ hold a grudge（动词 hold，grudge 前有 a；记谁 ⇒ against sb）
- 2026-10-09 ✅ 学习日 在池第 1 组 [8] · `My roommate holds a huge grudge—I forgot to pay her back ten bucks, and she nagged(这个词学一下) me about it for a whole month.` —— hold ＋ a ＋ grudge 齐了。连错 2 → 连对 1
  ⚠️ 更好版 `My roommate really holds grudges` —— "特别记仇"是性子 ⇒ 复数 grudges；a huge grudge 是一笔具体的仇（要接 against me）⇒ 问题是什么补了一行
  ｜她标「这个词学一下」⇒ nag 另建 #438
- 2026-10-10 ❌ 学习日 在池第 1 组 [4] · `My coworker holds really grudge—I disagreed with him once in a meeting, and he hasn't spoken to me since.` —— really 插进动词和宾语中间，grudge 没带 a 也没变复数，块没成形。连对 1 → 连错 1
  最小改 `My coworker really holds grudges—I disagreed with him once in a meeting, and he hasn't spoken to me since.`
  ❌ really 修饰动作 ⇒ 放动词前（really holds）；副词不插进动词和宾语中间；grudge 可数，单数带 a，"性子记仇"用复数 grudges
- 2026-10-11 ✅ 学习日 在池第 1 组 [2] · `My neighbor holds a huge grudge; our renovation was noisy for a month, and he still ignores me when he sees me.` —— hold 在前、grudge 带 a，块成形了。连错 1 → 连对 1
  ⚠️ 更好版 `holds a huge grudge against us` —— a huge grudge 是一笔具体的仇 ⇒ 接 against ＋ 人（同 10-09 的 ⚠️，块内的事，不另建号）

### 440 · sentimental（煽情、催泪）≠ dramatic（夸张、戏剧化）
类型 词汇 ｜ 新建 2026-10-09 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 词组

**问题是什么**
**sentimental** ＝ 煽情、感情渲染过头、就想让人哭：`an overly sentimental ending`。
**dramatic** ＝ 戏剧化、起伏大、反应夸张：a dramatic ending（结局反转大、很有冲击力）· overly dramatic（演得太过、大惊小怪）。
同一格里的邻居（别串）：sappy（口语，酸、肉麻）· melodramatic（狗血、苦情那种夸张）。
判据一句话：重点在"催泪、感情泛滥" ⇒ sentimental；重点在"情节起伏、反应夸张" ⇒ dramatic。
★ 题型判词组：中文块"煽情的…"能映射回 sentimental（sappy／tear-jerking 合法照判）；再落到 dramatic ⇒ ❌。

**怎么发现的**
2026-10-09 学习日 复检第 3 组 [7]（#404 题面"我觉得这部电影的结局太煽情了。"）· 原话
`I felt like then ending of the movie was overly dramatic(这个词学下).`
她自己标「这个词学下」⇒ §2③ 建号，判 ❌；"煽情"落到 dramatic 只沾边（dramatic 是夸张、戏剧化，煽情是催泪、感情泛滥）⇒ 目标 sentimental。
判重三步：
　① 目标形式 dedup "sentimental"／"dramatic"／"melodramatic"／"sappy" ⇒ 零命中
　② 中文 dedup "煽情"／"催泪" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`overly dramatic`（她标「这个词学下」）　　更准：`overly sentimental`
找法：说"煽情"之前问一句 —— 是想让人哭（sentimental），还是演得夸张（dramatic）？

**题面**
"电视剧结尾那段特别煽情的告别戏"（故意把感情往上推、就为了让人哭的那种）

- 2026-10-09 ❌ 首犯 · 学习日 复检第 3 组 [7]（#404 题里）· 她标「这个词学下」· 原话 `I felt like then ending of the movie was overly dramatic(这个词学下).`
- 2026-10-10 ❌ 学习日 在池第 2 组 [2] · 「忘了」—— sentimental 没调出来（§3.3 "忘了"也是 ❌）。连错 1 → 2
  最小改 `the really sentimental farewell scene at the end of the TV series`
  ❌ "煽情" ＝ sentimental（催泪、感情泛滥）；⛔ 别落到 dramatic（情节起伏大、反应夸张）
- 2026-10-11 ✅ 学习日 在池第 1 组 [6] · `that super sentimental speech the groom gave at the wedding` —— sentimental。连错 2 → 连对 1

### 441 · shed（猫狗掉毛：a dog that doesn't shed）
类型 词汇 ｜ 新建 2026-10-10 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 整句

**问题是什么**
**shed** ＝ 猫狗掉毛（不及物，主语是动物）：`a dog that doesn't shed` ／ `Our cat sheds like crazy in spring.`
同一格里的邻居（别串）：shed hair／fur（带宾语也行）· lose hair（人掉头发、或病了一块块掉；猫狗正常换毛不说它）· molt（鸟换羽、蛇蜕皮）。
判据一句话：猫狗身上掉毛 ⇒ shed；人掉头发 ⇒ lose hair。
★ 题型判整句："掉毛"也能绕成 lose fur ⇒ 整句 ＋ 正向点名 shed。

**怎么发现的**
2026-10-10 学习日 在池第 1 组 [2]（#96 题面"我想养一只不掉毛、又特别亲人的狗。"）· 原话
`I want to get a dog that doesn't shed（学一下） and is super affectionate（学一下）.`
她写对了 doesn't shed，但自己标「学一下」⇒ §2③ 建号，判 ❌（§3.2b：不会的地方哪怕写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "shed" ⇒ 零命中
　② 中文 dedup "掉毛" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「学一下」（用法本身对）　　目标：`a dog that doesn't shed`
找法：说猫狗"掉毛"，先落 shed，不用带宾语。

**题面**
"我们家哈士奇一换季就疯狂掉毛，地板上到处都是狗毛。"（"掉毛"用 **shed** 说）

- 2026-10-10 ❌ 首犯 · 学习日 在池第 1 组 [2]（#96 题里）· 她标「学一下」· 原话 `I want to get a dog that doesn't shed（学一下） and is super affectionate（学一下）.`
- 2026-10-11 ✅ 学习日 在池第 1 组 [7] · `Our husky sheds like crazy whenever the season changes, so I have to vacuum the floor twice every day.` —— sheds（不及物，主语是狗）。连错 1 → 连对 1
  ⚠️ twice every day → twice a day（频率默认"次数 ＋ a ＋ 时间"；她自己说过 three times a week／twice a year ⇒ 只进 diff-2，不建号）

### 442 · affectionate（宠物／人亲人、爱亲近）
类型 词汇 ｜ 新建 2026-10-10 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 整句

**问题是什么**
**affectionate** ＝ 爱亲近、爱撒娇、主动表达亲热：`a super affectionate dog` ／ `She's very affectionate with her kids.`
同一格里的邻居（别串）：friendly（友好、不怕生，程度弱）· clingy（黏人，常带"烦"的意思）· cuddly（抱起来软乎乎、爱被抱）。
判据一句话：宠物"亲人"、爱蹭爱黏、主动凑过来 ⇒ affectionate；只是不怕生 ⇒ friendly。
★ 题型判整句："亲人"翻成 friendly／clingy 都沾边 ⇒ 整句 ＋ 正向点名 affectionate。
★ 与 #441（shed）同一句里建号：两条是两个词，各走各的。

**怎么发现的**
2026-10-10 学习日 在池第 1 组 [2]（#96 题面"我想养一只不掉毛、又特别亲人的狗。"）· 原话
`I want to get a dog that doesn't shed（学一下） and is super affectionate（学一下）.`
她写对了 super affectionate，但自己标「学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "affectionate" ⇒ 零命中
　② 中文 dedup "亲人" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「学一下」（用法本身对）　　目标：`a super affectionate dog`
找法：说"亲人／爱黏人"，先落 affectionate，对谁亲用 with。

**题面**
"我养的那只猫特别亲人，我一进门它就跑过来蹭我的腿。"（"亲人"用 **affectionate** 说）

- 2026-10-10 ❌ 首犯 · 学习日 在池第 1 组 [2]（#96 题里）· 她标「学一下」· 原话 `I want to get a dog that doesn't shed（学一下） and is super affectionate（学一下）.`
- 2026-10-11 ✅ 学习日 在池第 1 组 [8] · `My three-year-old nephew is super affectionate and wants a hug from everyone he sees.` —— affectionate。连错 1 → 连对 1

### 443 · office ＝ 上班的地方（"公司"指地点 ⇒ office；company 是机构）
类型 词汇 ｜ 新建 2026-10-10
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 整句

**问题是什么**
**office** ＝ 上班的那个地方：`downstairs from our office` ／ `I stayed at the office till ten.`
**company** ＝ 公司这个机构：`I work for a tech company.` ／ `The company laid off 200 people.`
同一格里的邻居（别串）：at work（在上班，不点出地方）· go to work（去上班，⛔ go to the company）· office building（写字楼）。
判据一句话：中文"公司"说的是**一个地方**（楼下、门口、在公司加班）⇒ office；说的是**一个机构**（进了一家公司、公司裁员）⇒ company。
★ 题型判整句：要靠"地方"的语境才现形；零提示（office／at work 都对，只有 company 当地点算掉）。

**怎么发现的**
2026-10-10 学习日 在池第 1 组 [8]（#436 题面"我们公司楼下有一家咖啡店，每天早上都排长队。"）· 原话
`There's a coffee shop downstairs from our company, with a huge line every morning.`
downstairs from 本身对（#436 ✅），diff-2 ⚠️："公司"在这里指地方，company 是机构 ⇒ 更地道是 our office ⇒ §3.2b 能学的表达 ⇒ 建号。
判重三步：
　① 目标形式 dedup "office" ⇒ 🎓#347（For office workers 话题句）· 🎓#343（opening hours）· 🎓#345（on ＋ 机器）· #436（downstairs from）· 🎓#127（especially）· 🎓#302（something breaks）· 🎓#428（be featured in）—— office 只出现在例句／历史里，考点都不是它 ⇒ 否
　　 dedup "company" ⇒ 🎓#423（job insecurity，⛔ company instability：那条考的是"工作不稳定"的说法）· 🎓#214 #238 #328 #370 #419 #129 #271 #353 #368 · #432 · ⛔#10 —— 没有一条考"公司指地点" ⇒ 否
　② 中文 dedup "公司" ⇒ 28 条，全是题面／正文里出现"公司"（social media giant／start a business／land a job／at stake 等），没有一条以"公司 ＝ office"为考点 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`downstairs from our company`　　更地道：`downstairs from our office`
找法：说到"公司"先问一句 —— 我说的是地方，还是机构？地方 ⇒ office。

**题面**
"我今天在公司待到晚上十点才走。"
★ 零提示：office／at work 都算对，只有把 company 当地点说才算掉

- 2026-10-10 ❌ 首犯 · 学习日 在池第 1 组 [8]（#436 题里）· diff-2 ⚠️ · 原话 `There's a coffee shop downstairs from our company, with a huge line every morning.` ⇒ 更好版 downstairs from our office
- 2026-10-11 ✅ 学习日 在池第 1 组 [9] · `I stayed at the office until ten tonight.` —— at the office（"公司"指地方，没落到 company）。连错 1 → 连对 1

### 444 · get caught up in ＋ 事（一门心思扑在…上、陷进去顾不上别的）
类型 词组 ｜ 新建 2026-10-10 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 整句

**问题是什么**
**get (so) caught up in** sth／doing sth ＝ 被一件事卷进去、扑在上面，顾不上别的：`People get so caught up in making money that …` ／ `I got caught up in work and forgot to call her.`
同一格里的邻居（别串）：be busy with（只说忙，没有"卷进去顾不上别的"那层）· 🎓#289 be obsessed with（着迷，程度更重）· get carried away（一时兴奋过了头）。
判据一句话：陷在某件事里、结果把别的忽略了 ⇒ get (so) caught up in ＋ 事。
★ 题型判整句："一忙起来"翻成 be busy with／focus on 都合法 ⇒ 整句 ＋ 正向点名 caught up。

**怎么发现的**
2026-10-10 学习日 复检第 3 组 [1]（#406 题面"很多人一心只顾着赚钱，慢慢就忘了什么才是真正重要的。"）· 原话
`A lot of people get so caught up in(这个词组学一下) making money that they lose sight of what actually matters.`
她写对了 get so caught up in，但自己标「这个词组学一下」⇒ §2③ 建号，判 ❌（§3.2b：不会的地方哪怕写对也照常判 ❌）。
判重三步：
　① 目标形式 dedup "caught up" ⇒ 只命中 🎓#166（see／meet／meet up 选动词，正文里有 catch up）⇒ 否；dedup "obsessed" ⇒ 🎓#289（be obsessed with，邻居、不同块）⇒ 否
　② 中文 dedup "一心"／"顾不上" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」（用法本身对）　　目标：`get so caught up in making money that …`
找法：想说"一忙起来就…／光顾着…"，先落 get caught up in，后面接事或 doing。

**题面**
"我一忙起工作来，就把我妈的生日给忘了。"（"一忙起来"用 **caught up** 说）

- 2026-10-10 ❌ 首犯 · 学习日 复检第 3 组 [1]（#406 题里）· 她标「这个词组学一下」· 原话 `A lot of people get so caught up in(这个词组学一下) making money that they lose sight of what actually matters.`
- 2026-10-11 ✅ 学习日 在池第 1 组 [10] · `Whenever my brother gets so caught up in video games, he even forgets to eat.` —— gets caught up in video games 块对。连错 1 → 连对 1
  ⚠️ so 挂结果没接 that ⇒ 归 🎓#144 记 📝（更好版 `My brother gets so caught up in video games that he even forgets to eat.`）

### 445 · dust（灰：chalk dust／a layer of dust）
类型 词汇 ｜ 新建 2026-10-10 ｜ 她说不会
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 词组

**问题是什么**
**dust** ＝ 落下来、积起来的灰、细粉末（不可数）：`chalk dust`（粉笔灰）· `a layer of dust on the shelf`（一层灰）。
同一格里的邻居（别串）：ash（烧剩的灰：烟灰、骨灰）· powder（磨成的粉）。
判据一句话：落下来、积起来的灰 ⇒ dust；烧剩的 ⇒ ash。
★ 题型判词组：中文"积的灰／粉笔灰"能映射回 dust，只要调出这个词就覆盖考点。

**怎么发现的**
2026-10-10 学习日 复检第 3 组 [2]a（#407 题面"老师袖子上蹭的一片粉笔灰"）· 原话
`不会（灰和袖口)`
她说"灰"不会 ⇒ §2③ 建号，判 ❌。
判重三步：
　① 目标形式 dedup "dust" ⇒ 零命中
　② 中文 dedup "灰" ⇒ 零命中；"一层" ⇒ 只命中正文里的"那一层"（🎓#113 #118 等，别的考点）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`不会（灰和袖口)`　　目标：`the chalk dust on the teacher's sleeve`
找法：说"灰"先问一句 —— 是积的还是烧的？积的 ⇒ dust。

**题面**
"书架顶上积的一层厚厚的灰"（很久没擦、手指一抹就是一道印子的那种）

- 2026-10-10 ❌ 首犯 · 学习日 复检第 3 组 [2]a（#407 题里）· 她说不会 · 原话 `不会（灰和袖口)`
- 2026-10-11 ✅ 学习日 在池第 2 组 [1] · `a thick layer of dust gathered on top of the bookshelf` —— dust（a thick layer of dust）。连错 1 → 连对 1

### 446 · sleeve（袖子）／cuff（袖口）
类型 词汇 ｜ 新建 2026-10-10 ｜ 她说不会
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 词组

**问题是什么**
**sleeve** ＝ 袖子：`on his sleeve` · `roll up your sleeves` · long-sleeved／short-sleeved（长袖／短袖）。
**cuff** ＝ 袖口（袖子最末那一圈）。
同一格里的邻居（别串）：collar（领子）· hem（下摆）。
判据一句话：整条袖子 ⇒ sleeve；末端那一圈 ⇒ cuff。
★ 题型判词组：中文"袖子"只映射回 sleeve。

**怎么发现的**
2026-10-10 学习日 复检第 3 组 [2]a（#407 题面"老师袖子上蹭的一片粉笔灰"）· 原话
`不会（灰和袖口)`
她说"袖口"不会 ⇒ §2③ 建号，判 ❌；题面写的是"袖子" ⇒ 目标 sleeve，袖口 cuff 一起写进本条。
判重三步：
　① 目标形式 dedup "sleeve"／"cuff" ⇒ 零命中
　② 中文 dedup "袖" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`不会（灰和袖口)`　　目标：`on the teacher's sleeve`
找法：说"袖子"先落 sleeve；只说最末那一圈才用 cuff。

**题面**
"这件外套的袖子"（胳膊伸进去的那两截）

- 2026-10-10 ❌ 首犯 · 学习日 复检第 3 组 [2]a（#407 题里）· 她说不会 · 原话 `不会（灰和袖口)`
- 2026-10-11 ✅ 学习日 在池第 2 组 [2] · `the sleeves on this jacket` —— sleeves（on／of 都对）。连错 1 → 连对 1

### 447 · stray（流浪的：a stray cat／stray animals）
类型 词汇 ｜ 新建 2026-10-10 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 词组

**问题是什么**
**stray** ＝ 没主人、在外面流浪的（动物）：`a stray cat` · `stray dogs` · `feed the strays`（名词，流浪猫狗）。
同一格里的邻居（别串）：homeless（说人）· abandoned（被主人遗弃的）· wild（野生的，本来就不是宠物）。
判据一句话：没主人在外面晃的猫狗 ⇒ stray；人 ⇒ homeless。
★ 题型判词组：中文"流浪猫"映射回 stray cat，只要调出 stray 就覆盖考点。

**怎么发现的**
2026-10-10 学习日 复检第 3 组 [2]b（#410 题面"为流浪动物筹款的慈善长跑"）· 原话
`a charity run for stray(学一下) animals`
她写对了 stray animals，但自己标「学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "stray" ⇒ 零命中
　② 中文 dedup "流浪" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「学一下」（用法本身对）　　目标：`stray animals`
找法：说"流浪猫／流浪狗"，先落 stray。

**题面**
"小区楼下那几只流浪猫"（没主人、在外面晃、靠邻居喂的那种）

- 2026-10-10 ❌ 首犯 · 学习日 复检第 3 组 [2]b（#410 题里）· 她标「学一下」· 原话 `a charity run for stray(学一下) animals`
- 2026-10-11 ✅ 学习日 在池第 2 组 [3] · `those stray cats living downstairs in our residential area` —— stray cats。连错 1 → 连对 1
  ⚠️ our residential area → our apartment complex ⇒ 新建 #453

### 448 · elevated highway／expressway（高架路）≠ overpass（跨线桥）
类型 词汇 ｜ 新建 2026-10-10
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 词组

**问题是什么**
中文"高架"（一整条架在半空中的快速路）⇒ **the elevated highway**（或直接 **the expressway**）。
**overpass**（英式 flyover）＝ 一座跨过另一条路的桥，只有一小段。
同一格里的邻居（别串）：ring road（环线）· interchange（立交桥）· footbridge（人行天桥）。
判据一句话：一整条在空中跑很远的路 ⇒ elevated highway／expressway；一座跨过去的桥 ⇒ overpass。
★ 题型判词组：中文块"那段高架"映射回 elevated highway（expressway 合法照判），落到 overpass ⇒ ❌。

**怎么发现的**
2026-10-10 学习日 复检第 3 组 [2]d（#61 题面"早高峰在高架上堵了四十分钟"）· 原话
`being stuck in traffic for forty minutes on the overpass during the morning peak`
diff-2 ⚠️：overpass 是一座桥，"高架"是一整条路 ⇒ 更准是 the elevated highway ⇒ §3.2b 选词偏了 ⇒ 建号。
判重三步：
　① 目标形式 dedup "overpass" ⇒ 零命中
　② 中文 dedup "高架" ⇒ 只命中 🎓#287（flow smoothly，题面里有高架）⇒ 否；"立交" ⇒ 零命中
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`on the overpass`　　更准：`on the elevated highway`
找法：说"高架"先问一句 —— 是一整条路还是一座桥？

**题面**
"每天上班要走的那段高架"（一整条架在半空中、能跑很远的快速路）

- 2026-10-10 ❌ 首犯 · 学习日 复检第 3 组 [2]d（#61 题里）· diff-2 ⚠️ · 原话 `being stuck in traffic for forty minutes on the overpass during the morning peak` ⇒ 更好版 on the elevated highway
- 2026-10-11 ✅ 学习日 在池第 2 组 [4] · `that stretch of the elevated highway I drive on to work every day` —— elevated highway（没落到 overpass）。连错 1 → 连对 1

### 449 · get／be knocked out (of 比赛)（被淘汰）
类型 词组 ｜ 新建 2026-10-10 ｜ ⭐ 她点名要学
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 整句

**问题是什么**
**get／be knocked out** ＝ 比赛里被淘汰：`He got knocked out in the first round.` ／ `They were knocked out of the World Cup.`（被淘汰出某个比赛用 of）。
同一格里的邻居（别串）：be eliminated（更正式）· be voted off（选秀被投票刷掉）· lose in the first round（大白话）。
判据一句话：淘汰赛里出局 ⇒ get knocked out (of 比赛)；靠投票刷掉 ⇒ be voted off。
★ 题型判整句："被淘汰"翻成 be eliminated 也合法 ⇒ 整句 ＋ 正向点名 knocked。

**怎么发现的**
2026-10-10 学习日 复检第 3 组 [3]（#408 题面"选秀节目第一轮他就被淘汰了。"）· 原话
`He was knocked out(这个词组学一下) in the first round of the talent show.`
她写对了 was knocked out，但自己标「这个词组学一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "knocked out"／"eliminated"／"voted off" ⇒ 零命中
　② 中文 dedup "淘汰" ⇒ 只命中 🎓#433（semi-final，题面里有淘汰）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「这个词组学一下」（用法本身对）　　目标：`He was knocked out in the first round`
找法：说"被淘汰"，先落 get knocked out，出哪个比赛用 of。

**题面**
"中国队小组赛就被淘汰了。"（"被淘汰"用 **knocked** 说）

- 2026-10-10 ❌ 首犯 · 学习日 复检第 3 组 [3]（#408 题里）· 她标「这个词组学一下」· 原话 `He was knocked out(这个词组学一下) in the first round of the talent show.`
- 2026-10-11 ✅ 学习日 在池第 2 组 [5] · `The team I root for got knocked out early this season.` —— got knocked out。连错 1 → 连对 1

### 450 · all over ＋ 地方（满…都是、弄得到处都是）
类型 词组 ｜ 新建 2026-10-10 ｜ 她问怎么说
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 整句

**问题是什么**
**all over ＋ 地方** ＝ 满…都是：`left a mess all over the table`（弄得满桌都是）· `There's water all over the floor.` · `paint all over his shirt`。
同一格里的邻居（别串）：everywhere（到处，不点出在哪）· on the table（只说在桌上，没有"满"那层）。
判据一句话：想说"弄得满 X 都是" ⇒ all over the X 挂在后面。
★ 与 🎓#216 分工：那条考"东西当主语用 be（His stuff is all over the floor）"，本条考 all over ＋ 地方这个块本身。
★ 与 🎓#186 分工：那条考 leave a mess，本条考 mess 后面怎么挂地方。
★ 题型判整句：on the floor／everywhere 也能达意 ⇒ 整句 ＋ 正向点名 all over。

**怎么发现的**
2026-10-10 学习日 复检第 3 组 [6]（#186 题面"同事们在会议室开完会，把桌上弄得一团糟就走了。"）· 原话
`My coworkers wrapped up their meeting in the conference room and just left a huge mess.(在桌子上怎么翻译)`
她问"桌上"怎么挂 ⇒ §2③ 她问的地方照常建号，判 ❌。
判重三步：
　① 目标形式 dedup "all over" ⇒ 🎓#216（东西当主语用 be，见上分工）· 🎓#186（leave a mess，见上分工）· 🎓#392 #100 #344（all over 只在例句里）⇒ 否
　② 中文 dedup "满地"／"到处都是" ⇒ 只命中 🎓#272 #314、#441 正文里的字串 ⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`just left a huge mess.(在桌子上怎么翻译)`　　目标：`just left a huge mess all over the table`
找法：说完 a mess／东西，想补"满桌／满地"，接 all over the …。

**题面**
"孩子吃完饭，饭粒掉得满地都是。"（"满地都是"用 **all over** 说）

- 2026-10-10 ❌ 首犯 · 学习日 复检第 3 组 [6]（#186 题里）· 她问「在桌子上怎么翻译」· 原话 `My coworkers wrapped up their meeting in the conference room and just left a huge mess.(在桌子上怎么翻译)`
- 2026-10-11 ✅ 学习日 在池第 2 组 [6] · `The kid finished eating and left rice grains all over the floor.` —— all over the floor（all over ＋ 地方挂在后面）。连错 1 → 连对 1

### 451 · locksmith（开锁师傅）
类型 词汇 ｜ 新建 2026-10-10 ｜ ⭐ 她点名要背
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 词组

**问题是什么**
**locksmith** ＝ 开锁／换锁／配钥匙的师傅：`call a locksmith` · `get a spare key cut at the locksmith's`。
同一格里的邻居（别串）：lock yourself out（把自己锁在门外）· spare key（备用钥匙）。
判据一句话：开锁、换锁、配钥匙的人 ⇒ locksmith。
★ 题型判词组：中文"开锁师傅"只映射回 locksmith。

**怎么发现的**
2026-10-10 学习日 复检第 3 组 [8]（#21 题面"我爸最近经常忘带钥匙，上周已经找了两次开锁师傅。"）· 原话
`My dad keeps forgetting his keys recently, and he's had to call a locksmith（背一下) twice just last week.`
她写对了 locksmith，但自己标「背一下」⇒ §2③ 建号，判 ❌（§3.2b）。
判重三步：
　① 目标形式 dedup "locksmith" ⇒ 零命中
　② 中文 dedup "开锁" ⇒ 零命中；"钥匙" ⇒ 只命中 🎓#100（look for，题面里找钥匙）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：自己标「背一下」（用法本身对）　　目标：`call a locksmith`
找法：说"开锁师傅"，先落 locksmith，动词用 call。

**题面**
"半夜打电话叫来的开锁师傅"（钥匙丢了、进不了家门时找的那种人）

- 2026-10-10 ❌ 首犯 · 学习日 复检第 3 组 [8]（#21 题里）· 她标「背一下」· 原话 `he's had to call a locksmith（背一下) twice just last week.`
- 2026-10-11 ✅ 学习日 在池第 2 组 [7] · `the locksmith we called in the middle of the night` —— locksmith。连错 1 → 连对 1

### 452 · 钉死的过去时间（last week／yesterday／two days ago）⇒ 一般过去时（⛔ have done … last week）
类型 语法 ｜ 新建 2026-10-10
状态 连对1 连错0 上次2026-10-11 未毕业 ｜ 题型 整句

**问题是什么**
句子里有**已经结束、钉死的过去时间**（last week／yesterday／in 2019／two days ago／when I was a kid）⇒ **一般过去时**：`He had to call a locksmith twice last week.`
完成时说的是"到现在为止"，⛔ 不跟钉死的过去时间；还没过完的时间（this week／today／so far）才配完成时。
同一格里的邻居（别串）：🎓#271（recently／lately／so far ⇒ 拉完成时）· 🎓#90（for／since／ever／just／already／yet ⇒ 完成时）—— 那两条是"该用完成时"的触发词，本条是"不能用完成时"的触发词。
判据一句话：句子里有 last …／… ago／yesterday／具体年份 ⇒ 一般过去时。

**怎么发现的**
2026-10-10 学习日 复检第 3 组 [8]（#21 题面"我爸最近经常忘带钥匙，上周已经找了两次开锁师傅。"）· 原话
`My dad keeps forgetting his keys recently, and he's had to call a locksmith（背一下) twice just last week.`
he's had to … last week：完成时撞上钉死的过去时间 ⇒ 时态选择错（不是形态标记漏掉）⇒ 建号。
判重三步：
　① 目标形式 dedup "last week" ⇒ 🎓#302 #166 #369 #397（只在例句里）⇒ 否；dedup "完成时" ⇒ 🎓#259（have 后面用过去分词，形态）· 🎓#141（过去完成时要有更晚参照）· 🎓#148（状态 vs 变化）· 🎓#271（recently 族拉完成时）· 🎓#214（完成进行时的形式）· 🎓#130 #269 #309 #291（别的规则）⇒ 否；dedup "yesterday" ⇒ 🎓#133（this morning 说法）· ⛔#147（时态只标一次）· 🎓#372 ⇒ 否；dedup "ago" ⇒ 🎓#220 #385 ⇒ 否
　② 中文 dedup "过去时间"／"具体时间" ⇒ 零命中／只命中 🎓#148（状态 vs 变化）⇒ 否
　③ 保留新建（⛔ 建号当天不测）

**我错在哪**
她的：`he's had to call a locksmith twice just last week`　　正确：`he had to call a locksmith twice just last week`
找法：写完 have／has done，扫一眼句子里有没有 last／ago／yesterday —— 有就退回过去式。

**题面**
"我前天才把这本书看完。"

- 2026-10-10 ❌ 首犯 · 学习日 复检第 3 组 [8]（#21 题里）· 原话 `he's had to call a locksmith（背一下) twice just last week.`
- 2026-10-11 ✅ 学习日 在池第 2 组 [8] · `I only paid this month's rent the day before yesterday.` —— the day before yesterday ⇒ 一般过去时 paid。连错 1 → 连对 1

### 453 · apartment complex（自己住的"小区"；⛔ our residential area）
类型 词汇 ｜ 新建 2026-10-11
状态 连对0 连错1 上次2026-10-11 未毕业 ｜ 题型 整句

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

### 454 · cut back on ＋ 东西（少吃／少用／少花：cut back on sugar）
类型 词组 ｜ 新建 2026-10-11 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-11 未毕业 ｜ 题型 整句

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

### 455 · underprivileged（家境困难的、条件差的 —— 说"穷"的体面说法）
类型 词汇 ｜ 新建 2026-10-11 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-11 未毕业 ｜ 题型 词组

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

### 456 · crafted（手工／精心做出来的：a manually crafted request · a carefully crafted message）
类型 词汇 ｜ 新建 2026-10-11 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-11 未毕业 ｜ 题型 整句

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

### 457 · build up ＋ 经验／积蓄（一点点攒起来：build up experience）
类型 词组 ｜ 新建 2026-10-11 ｜ ⭐ 她点名要学
状态 连对0 连错1 上次2026-10-11 未毕业 ｜ 题型 整句

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

