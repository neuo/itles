# 题库 · suzy 练过的题（writing-drill 唯一出题源）

> **规则：只从这里出题，不加新题。** 同题反复写，直到表层错误清零。
> 每题记录：题面逐字 / 她写过几次 / 每次的分和错 / 她原稿在哪 / 下次的靶子。
> `📍` = 她的原稿位置（要对照就去读）。分数标 ⚠️ 的是 **2026-06 未限时且未数错误** 的旧判分，**不作基线**。

> 🔴 **路径约定（2026-08-10 补，F85）**：本文件所有 `📍` / `⚠️` 行里的相对路径，
> **一律以 `writing-band7/` 为根**（原来 11+ 处直接写 `log/sessions/…`，从仓库根打不开）：
> ```
> log/sessions/X            ＝ writing-band7/log/**_pre_drill_sessions**/X   ← 08-11 改：旧 session 全部移到这里
>                              例外：`log/sessions/2026-08-10-drill-T2-18.md` ＝ writing-band7/**drill/sessions**/2026-08-10-drill-T2-18.md
> t1/coach/sessions/X       ＝ writing-band7/t1/coach/sessions/X
> gemini/corrections_2026-07.md ＝ writing-band7/gemini/corrections_2026-07.md
> 裸文件名（如 2026-05-19-ex02-v1.md）＝ writing-band7/log/sessions/ 下的同名文件
> ```
> 写成一条约定而不是改 40 行，是因为约定**可以被一次性核对**，逐行改反而会漏。

---

## 出题优先级（每次 session 按此选题 —— ★ 排序键必须打印进 G1 证据块）

> ⚠️ 本表原来与下方「📌 T2 缺口盘点」冲突：那里写 `P/S 题型（T2-25）从未完整 cold 产出 → **最高优先**`，
> 而本表的第 1 位是"上次有复发错的题"。两条都写着"最高"。⇒ 现合并成**一条全序**，冲突消失。

**排序键 —— 比较顺序 `K1 → K0 → K2 → K3 → K4`（从上往下比，先分出胜负就停）**

> 🔴 **2026-08-10 二修（F55）：K0 从第 0 位降到第 2 位。**
> 原来 K0 是**第一**排序键 ⇒ 任何一道从没写过的题都压过所有练过的题。
> 那**正好反着**本 skill 的立身之本 —— `profile §0`「同题反复写把内容负荷归零」、
> 本表 R3「**同题反复优先于轮换**」。具体后果：D2 会被逼去写一道从没 cold 过的题，
> 而 08-10 刚刚推出来的两个靶子（冠词 / 逗号粘连）当场作废、无题可落。
> ⇒ 降位 **＋** 加一条硬配额 R4（每周期最多 1 篇基线篇），覆盖照补，但不再吃掉反复练。

```
K1  上次有【复发错】的题       ← 「复发」＝ SKILL 定义5，定义见下
    ★★ **K1 有连出上限：同一道题连续 3 个学习日之后强制让位**（F157 六审）
      🔴 病灶：只有写过 ≥2 次限时 cold 的题才可能有「复发」，而全库**只有 T2-18** 满足；
         K1 排在最前、又被 R1 例外豁免 ⇒ **K1 是吸收态，T2-18 会一直赢下去**，
         K0 的覆盖缺口、R4 的基线配额、R2 的 T1 排期全部永远轮不到。
      ⇒ 同题连出 3 个学习日后，第 4 天**跳过 K1**（该题降到 K2 参与排序），
        让 K0 出一篇基线篇 —— **有了新基线，才会有新的题够格进 K1**，吸收态自然打开。
      ★ 打印在 G1 断言 2：`K1 连出检查：<题号> 已连出 <n> 天 · <是否跳过>`
K0  🚩 覆盖缺口（＝【基线篇】候选）
    条件：**该【题】**没有任何一次限时 cold 产出
    ★ 粒度二修（F80）：原写"某个【题组】还没有任何一次限时 cold"，
      可下面的候选清单列的是**逐题**（T2-01 / T2-07 / T2-19 …）—— 条件是组级、清单是题级，
      同一个键有两种读法 ⇒ 排序不唯一。**以【题】为准。**
    理由：没有基线的题连"复发"都无从谈起，K1–K3 对它们全部无定义
    当前命中：见下方两张「📌 缺口盘点」清单
    ★ 受 R4 约束：每周期最多出 1 篇
K2  最近一次【可比分】最低的题 ← 「可比」的定义见下
K3  距上次最久的题（按学习日 D 计，不按日历）
K4  题号升序（兜底，保证全序，不许出现"两题并列所以随便挑"）
```

**★ 「复发」的定义（原来没有，F22）**
```
复发 ＝ 同一个【错误代号】（P1–P12 / W1–W18）在同一道题的【相邻两次限时 cold】里都出现
      ★ 不是"某个具体词又写错了"，是代号级
      ★ 只看限时 cold；untimed / 仿写 / 改后稿不参与判定
「上次这道题的复发清单」＝ 该题最近一次 attempt 行里，代号级复发的那些代号
      → 写在该题的 `🎯 下次靶子` 行里；靶子必须从这一行取（SKILL §4c）
```

**★ 「可比分」的定义（原来没有，F22；2026-08-10 二修补了时间线，F64）**
```
可比    限时 cold、非 (edited)、非 (zh-untimed)、**且判分日期 ≥ 2026-08-10** 的分
不可比  ⚠️ **2026-08-10 之前的分一律标 ⚠️ 不可比**，无论条件多干净。三条理由：
        ① 那批分有的是 Gemini 判的（AI 判分不是交叉验证，`scoring.md §5 第 8 条`）
        ② 有的是教练**校准前**判的 —— 同一批作文教练判 7.0–7.5，实考 5.5，差一整档半
        ③ 那批里还留着 `LR 5.5 / 6.5 / GRA 6.5 / TA 7.5` 这类 **§3.1 明令非法的半档**
        另外照旧不可比：「未判」· 仿写 · 半 cold（教练给骨架）· 未限时
处理    K2 只在【可比分】之间比。当前全库只有 1 条可比分（08-10 T2-18 = 6.0）
        ⇒ K2 目前几乎总是分不出胜负，落到 K3 / K4。**这是实话，不是故障。**
        一道题若一条可比分都没有 → 它在 K2 上不参与比较（不是"排最后"，是"无定义、跳过"）
```

**★ 题型轮换（重写 —— 原写「任何题型不超过 2 周没碰」在算术上不可能，F23）**
```
问题：本库有 13 个题组（T2 六组 A1–A6 ＋ T1 七组 B1–B7），每学习日只写 1 篇。
     2 周就算天天练也只有 ~14 篇，还要留出「同题反复写」的篇数 —— 全覆盖与反复练直接打架。
     而「同题反复写」是本 skill 的立身之本（profile §0：换新题会消耗她不缺的那部分带宽）。
⇒ 轮换只约束【连续】，不承诺【全覆盖周期】：
   R1 连续 3 个学习日不许出同一个题组。**★ 例外（F88）：R1 不适用于 K1 选中的题**
      （＝带着未清【复发】的那道题）—— R1 只在【没有复发】的题之间打破平局。
      理由：按字面读，R1 会在 D2 直接删掉 D1 的 K1 胜者，正好复现 F55 那条 fix 要防的失败
      （靶子刚推出来就无题可落），并与 R3「同题反复优先于轮换」正面打架。**同题反复赢。**
   R2 每个周期（5 学习日）里 T1 ≥ 1 篇（防 T1 整个荒掉）
      ★★ **R2 是【排期槽】不是【删除约束】**（F156 六审 —— 它原来永远不可能生效）：
        🔴 病灶：R1/R4 都能用"删候选"实现，**R2 是个下限，删任何候选都满足不了它**。
           它写在"删掉违反 R1/R2/R4 的候选"这句话里 ⇒ **按构造从不触发。**
        🔴 后果更重：**她的 Writing 总分 = (T1 + 2×T2) / 3**，T1 占三分之一。
           一个从不触发的 R2 = T1 永远不练 = 三分之一的分自生自灭。
        ⇒ 改成排期：**一个周期里如果已经过了 4 个学习日还没写过 T1，第 5 个学习日
          【强制出 T1】，凌驾于 K1–K4 之上**（在 T1 内部再按 K1→K4 排序）。
          写进 G1 断言 2 的证据行：`R2 排期检查：本周期 T1 已写 <n> 篇 · 今日<是/否>强制 T1`
   R3 全库覆盖不设期限 —— **同题反复优先于轮换**
   R4 ★ **每个周期（5 学习日）最多 1 篇 K0 基线篇**（2026-08-10 新增，F55）
      理由：K0 降位只是让它不再压过 K1；还要一条配额，否则"没写过的题"存量太大
      （T2 至少 6 道 + T1 至少 2 道），排序上一旦轮到就会连着好几天全在开新题。
      基线篇本身是必要的（没基线就没有复发可谈），但**一周期一篇够了**。
   ★ R1/R2/R4 是【约束】不是【排序键】：先按 `K1→K0→K2→K3→K4` 排序，
     再删掉违反 R1/R2/R4 的候选，取剩下第一名（**R1 的删除动作跳过 K1 胜者，见上面的例外**）
```

**★ 🎯 行的写法（F98 —— 原来一半的 🎯 行写的是散文，`SKILL §4c` 分支① 读不出代号，靶子被静默丢掉）**
```
🎯 行【必须】以错误代号开头：`P1–P12`（T2）／`W1–W18`（T1），代号后面才跟人话解释
   例：`🎯 下次靶子：①P2 冠词（…）②P7 逗号粘连（…）`
该题 0 次限时 cold ⇒ 写 **【基线篇】** 三个字，并注明"按 §4c 分支③ 不给靶子"
   —— 这一档合法且必须显式写出，不许留空、不许写成散文式的"先补一次 cold"
```

**每题毕业条件**：连续 2 次限时 cold ①总分 ≥ **目标** ②该题历史错误零复发。
> **「目标」＝ 6.5**（她本人定的近期总目标，`profile.md §0 / §7.3`）。原来这个量没有定义。
> ★ 「总分」只认**可比分**（定义见上）⇒ **08-10 之前的分不能用来毕业**（F64）。
>   当前全库可比分只有 1 条，所以现在**没有任何题**够得着题级毕业 —— 这是实话，别拿旧分凑。
> 三套毕业系统（题级 / 模式级 / 条目级）的关系见 `profile.md §5`。

---

# PART A · TASK 2（25 题）

## A1 · DBV 讨论双方（6 题）

### T2-01 学校该教实用学科还是广泛学科 〔非剑桥·教练题〕
> Some people think that schools should teach children academic subjects that will be beneficial to their future careers. Others think it is more important for schools to teach a wide range of subjects, including arts and music. **Discuss both views and give your own opinion.**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 05-17 | 仿写（读完范文再写） | 5.5–6 ⚠️ | 9 个拼写；🚨 `students **with** practical skills ... are difficult to get a stable job`（语义反转）；结论抄了范文 |
| 2 | 05-18 | 仿写二刷 | 6.0–6.5 ⚠️ | `What is the goal of education is`（间接疑问语序）；`I lean towards that`；`A education system`；`would success` |

📍 `log/sessions/2026-05-17-ex01-v1.md:16-34` · `2026-05-18-ex01-v2.md:17-31`
🎯 **下次靶子**：**【基线篇】** —— 该题 0 次限时 cold（只有仿写），按 `SKILL §4c` 分支③ **不给靶子**，先拿真实基线

---

### T2-02 一辈子做同一份工作 vs 换工作 〔非剑桥·教练题〕
> Some people think it is better to spend their whole working life doing the same job, while others believe that changing jobs from time to time is more beneficial. **Discuss both views and give your own opinion.**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 06-02 | 半 cold（教练给 TEEL 骨架） | ~6.5 ⚠️ | `others **argues**`；`is **effective way**`；a/an 缺 ×3；逗号粘连；🚨 `firing old bosses`（想说"离职"）；`his new **leader**`→manager |

📍 `log/sessions/2026-06-02-skeleton-dbv-extra.md:12-20`
🎯 靶子：①**P2 冠词**（a/an 缺 ×3）②**P7 逗号粘连**。★ 条件：无骨架限时 cold（上次是半 cold）

---

### T2-03 竞争 vs 合作 〔剑 19 T1〕
> Some people think that competition at work, at school and in daily life is a good thing. Others believe that we should try to cooperate more, rather than competing against each other. **Discuss both these views and give your own opinion.**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 06-14 | cold **未限时** | ~7 ⚠️ | 仅 3 处搭配：`natural driver **for** progress`→of；`bring **bigger** progress`→lead to greater；`**get** sustainable success`→achieve |

📍 `log/sessions/2026-06-14-dbv-cold.md:21-25`
🎯 靶子：**【基线篇】** —— 该题 0 次限时 cold（06-14 那次未限时），按 `SKILL §4c` 分支③ **不给靶子**。
★ 同题限时 40 分钟重写，看未限时的干净度能保住多少 —— 这是最干净的一次 cold，最适合做"限时代价"实验

---

### T2-04 老龄化社会（讨论双方版）〔剑 18 T4〕
> In many countries, people are now living longer than ever before. Some people say an ageing population causes problems for governments. Others think there are benefits if society has more elderly people. **Discuss both these views and give your own opinion.**
> （剑桥原文用 `creates` / `Other people`）

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 06-15 | cold **未限时** | ~7.5 ⚠️ | 2 处：`delay the retirement age`→raise；`much greater`→far greater。最难的 -s 判断全对 |

📍 `log/sessions/2026-06-15-dbv-ageing.md:15-22`
🔗 **与 T2-18 同话题、不同指令** —— 见那条的对照实验

---

### T2-05 专业人士是否必须在受训国工作 〔剑 17 T3〕
> Some people believe that professionals, such as doctors and engineers, should be required to work in the country where they did their training. Others believe they should be free to work in another country if they wish. **Discuss both these views and give your own opinion.**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-09 | **cold 限时**（她自评"时间不太够，逻辑没写顺，结尾匆匆"） | ~6.5 | 🚨 **两处逻辑断裂**：(a) `Therefore, the requirement ... is just for reward`（国家投资凭什么推出强制？）(b) **Body2 例子反证论点** —— 用中国定向生（本来就被绑定）论证"不该限制自由"；`should be work`；`a engineer`/`a easy thing`；`valueable`；`Nevertherness` |

📍 `gemini/corrections_2026-07.md:119-125` ← **这才是她的原稿**
⚠️ `log/sessions/2026-07-12-t2-cold-dbv-pn.md:14-20` **不是她的原稿**，是 Gemini 改后稿被误当 cold 判了 7 分。该文件结论作废。
🎯 靶子：①**P10 逻辑闭环** —— 写前先检查"我的例子是不是在帮对方说话"

---

### T2-06 大学生该不该学本专业以外的科目 〔剑 18 T2〕
> Some people believe university students should study whatever subject they like; others believe they should only study subjects that are useful for their future qualification/career. **Discuss both views and give your own opinion.**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | **cold 限时** | **6.5**（TR 7.0 / CC 7.0 / LR 6.0 / GRA 6.0） | 拼写 6 个（abount / univerity / energe / knowledage / ablities / import）；`devote all their attention **into**`；`I strong believe`；`improve students' **competition**`（中式）；`the education system **focus**`；`a whole-developed person`；`help student **to learning**`；`beneficial for **find** jobs` |

📍 `gemini/corrections_2026-07.md:472-478`

---

## A2 · AgD 同意与否（6 题）

### T2-07 电脑手机损害年轻人社交能力 〔非剑桥·教练题〕
> Some people believe that the increasing use of computers and mobile phones for communication has had a negative effect on young people's social skills. **To what extent do you agree or disagree?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 05-19 | 仿写 | 6.0 ⚠️ | 🆕 **让步过头**：`Admittedly, heavy reliance ... is hurting our ability to socialize`（把对方论点整个让掉）；`put attention **in**`；`themself`；`These example` |
| 2 | 05-20 | 仿写二刷 | 6.0–6.5 ⚠️ | 只剩 3 处：`to some extend`；`The shows that`；`show noticeably social awkward` |
| 3 | 05-30 | 段落级 cold 重写 | — | 逗号粘连；🆕 P9 缺副词/分词延展（她自己发现） |

📍 `2026-05-19-ex02-v1.md:17-33` · `2026-05-20-ex02-v2.md:16-30` · `2026-05-30-rewrite-drill.md:60`

---

### T2-08 个人对环保作用很小，只能靠政府和大公司 〔非剑桥·教练题〕
> Some people believe that individuals can do very little to protect the environment, and that real change can only come from governments and big companies. **To what extent do you agree or disagree?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 06-01 | 半 cold（教练给骨架） | ~6.5 ⚠️ | `the power ... **are** huge`→is（**attraction**）；`protecting **environment**` ×3；逗号粘连；`companies **achieve** the capacity`→have；`looks like negligible`；`contributions **to protect**`→to protecting；`polices`；`huge` 重复 4 次 |

📍 `log/sessions/2026-06-01-skeleton1.md:12-19`
⚠️ 这是全库唯一**没过 examiner 门**的篇，教练在这篇里把她的 `huge` 升成了 `considerable` —— 唯一一次词汇漂移事故就落在这里

---

### T2-09 音乐能连接不同文化与年龄 〔剑 14 T3〕⭐ 有官方带分样卷
> Some people say that music is a good way of bringing people of different cultures and ages together. **To what extent do you agree or disagree with this opinion?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 06-15 | cold **未限时** | ~7 ⚠️ | 无硬伤。LR 平（very happy / become closer / together ×4）—— 按她定的优先级不计错 |

📍 `log/sessions/2026-06-15-agd-music.md:16-20`
⭐ **对照读**：剑 14 官方同题样卷 = **Band 5.5**，考官评语见 `anchors.md` 锚 A。那篇 TR/CC/段落全达标，就栽在拼写和词选 —— **和她同一个失分结构**

---

### T2-10 科学最重要的目标 〔剑 18 T1〕
> The most important aim of science should be to improve people's lives. **To what extent do you agree or disagree?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-09 | **cold 限时 45 分**（目标 37 分，超时） | ~6.5 | 拼写 7 个（Nowsday / resouces / benifit / thier produects / convient / energe / imporve）；`immerse **themself into** researching`；`compete others`；`I strong believe`；`life quanlity`；**结论只重述论点没有落点**（她自己诊断） |
| 2 | 07-13 | 她自己微改版 | — | Gemini 重写了结论 |

📍 `gemini/corrections_2026-07.md:313-319`（原稿）· `:378-384`（她微改版）
🎯 靶子：①**P5 拼写**（7 个：Nowsday / resouces / benifit / convient / energe / imporve / produects）②**P1 动词框架**（`immerse themself into` · `compete others`）
★ **超时**是这题的独立【条件】问题不是靶子 —— 她"过度解释因果"导致写不完。修法：抽象化/名词化（`for commercial profits` / `for geopolitical advantages`）

---

### T2-11 免费供水是基本人权 〔剑 20 T1〕
> Some people believe that it is the responsibility of governments to provide free water supply to all citizens. **To what extent do you agree or disagree?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | **cold 限时** | **6.5–7.0**（TR 7.5 / CC 7.5 / LR 6.0 / GRA 6.5） | `safty`；`disagree **this** opinion`→with；`It is governments' duties`→the government's duty；`water cleaning factory`→water treatment plants（中式）；`cannot **have** a water supply`→access；`a **faulty** of the local government`；`has **right** to require`；`This demonstrates ___`（漏 that）；`outweighted` |

📍 `gemini/corrections_2026-07.md:922-928`
⭐ 这是她 TR/CC 最高的一篇（7.5/7.5）—— **证明内容层她已经稳在 7.5，全部差距在 LR/GRA**

---

### T2-12 高层公寓是解决住房的最好办法 〔机经·非剑 13-20〕
> Building tall apartment blocks is the best way to provide homes for a growing population. **To what extent do you agree or disagree?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | **cold 限时** | **6.5–7.0**（TR 7.5 / CC 7.5 / LR 6.0 / GRA 6.5） | 拼写 8 个（resousces / skycrapers / demostrates / mainteinance×3 / packet / satety）；`to **houses**`→to house；`more than half ... **are** living`→lives；`metacities`→megacities；`external glasses`→external windows；`rescues for skyscraper are **extreme** difficult`；`worthy thinking about`；`had no ideas except for waiting the fire naturally vanishing`（中式长块） |

📍 `gemini/corrections_2026-07.md:1060-1066`
🎯 靶子：①**P5 拼写**专项（这篇 8 个，全库最多）

---

## A3 · PN 积极还是消极（3 题）

### T2-13 超市能买到全球食品 〔剑 19 T4〕
> In many countries nowadays, consumers can go to a supermarket and buy food produced all over the world. **Do you think this is a positive or a negative development?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 06-15 | cold **未限时** | ~7.5 ⚠️ | 仅 2 处：`food imports produced all over the world`（冗余）；`create pressure **for**`→put pressure on |

📍 `log/sessions/2026-06-15-pn-cold.md:16-20`

---

### T2-14 替代疗法取代看医生 〔剑 17 T4〕
> Nowadays, a growing number of people with health problems are trying alternative medicines and treatments instead of visiting their usual doctor. **Do you think this is a positive or a negative development?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-09 | **cold 限时 40 分**，她自评写不够长 | ~6.5 | `a increasing`→an；`rather than **believing** their usual doctor`→seeing/consulting；`**tread**`→trend（全篇反复）；`treatments which barely **success**`→succeed；`follow the **advices**`→advice。她自己诊断：**调不出简单形容词**（safe/strong/dangerous/wise/qualified）和名词 desire |

| 2 | **08-12** | **cold 限时 40min**（模式 A，中文计时；TR/CC 标 `(zh-coached)`） | **6.0**（TR 6.0 / CC 6.0 / LR **5.0** / GRA **7.0**） | 315 词 · 干净句率 **55.6%**（跨进 GRA 7 档）· 词汇错 **15**，K270 **13** → LR 掉一档。🎯 P7 逗号粘连 **0 处 ✅**（用了破折号 ＋ `where`）／ P2 冠词 **3 处 ❌**（`loss` · `hierarchy diagnosis system` · `scope of doctors`）。❌ 主要错：`In actually`／`they works`／`business tend`／`even` 引导从句缺 if／`guidances` 不可数／`a health urgent`／S18 悬垂分词／`result from experience`／`gambling at`／`recommend patients to`（应 refer） |

📍 08-12 原稿见 `drill/sessions/2026-08-12-drill-T2-14.md`
🎯 **下次靶子**：①**P2 冠词**（本篇 3 处未清零，继续）②**P4 单复数**（P7 本篇 0 处已过，换掉；P4 在 08-10 两处、08-11 两处、本篇 `business tend`，是当前最高频未盯项）
> 📌 推出依据（供 G6 断言 6 复算）：P2 取自本篇**靶子内未清零**；P4 取自本篇**靶子外出现集** `{P4×1, P1×4, P11×5, P12×3, P6×2}`。
> 未取 P11（×5，频次最高）的理由：P11 = 词义/搭配误用，本篇的 5 处**全部来自"为避免重复而换词"**（secure/negative/expenditure），
> 那是一个**策略问题**不是一个可盯的表层模式——已在 drill 里用"代词/上位词/省略"三招直接解决，盯它没有可执行动作。

📍 `gemini/corrections_2026-07.md:181-187` ← 07-09 原稿
⚠️ `log/sessions/2026-07-12-t2-cold-dbv-pn.md:50-56` 是 Gemini 改后稿，非她原稿

---

### T2-15 农村人口迁往城市 〔剑 18 T3〕
> In many countries, people are moving from rural areas to cities. **Do you think this is a positive or a negative development?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | **cold 限时** | **6.5**（TR 7.0 / CC 7.0 / LR 6.0 / GRA 6.0） | `the rural **ares**`；`is **positive** development`→a；`countrysides`（不可数）；`a bunch of kids`（口语register）；`the olderly, most of **who**`→whom；`per **capital**`→capita；`**way** less`→far less；`China government`→the Chinese government；`massive money`；`which exactly makes few people convenient`（中式）；`This **demonstrate**`；`import`；`efficiencey` |

📍 `gemini/corrections_2026-07.md:578-584`

---

## A4 · AD-outweigh 利大于弊（3 题）

### T2-16 无人驾驶车 〔剑 16 T4〕
> In the future, all cars, buses and trucks will be driverless. The only people travelling inside these vehicles will be passengers. **Do you think the advantages of driverless vehicles outweigh the disadvantages?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 06-15 | cold **未限时** | ~7.5 ⚠️（CC 被标为连接标杆） | 仅 1 处：`they are a great technology`（数不一致） |

📍 `log/sessions/2026-06-15-ad-driverless.md:16-20`

---

### T2-17 冒险的利弊 〔剑 17 T1〕
> It is important for people to take risks, both in their professional lives and their personal lives. **Do you think the advantages of taking risks outweigh the disadvantages?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-09 | **cold 限时** | ~7（Gemini 评"结构极其完整"） | `import part`→important；`uneccessary`；`taking a risk actually **make**`→makes；`someone **change** jobs`→changes；`Hark work`→Hard；`neccessary`；`bussiness`；`goverment`；`fit **in** a new environment`→into |

📍 `gemini/corrections_2026-07.md:65-71`
⚠️ `log/sessions/2026-07-11-ad-risk-model.md` 里的英文是**教练范文**，不是她写的（且与 Gemini 改后稿 83% 雷同）

---

### T2-18 老龄化社会（利大于弊版）〔剑 18 T4 变体〕
> In many countries, people are now living longer than ever before. **To what extent do the advantages of having an ageing population outweigh the disadvantages?**
>
> ⚠️ **2026-08-10 补上第一句（F81）**：她 08-10 实际写的那道题**带这句 lead-in**
> （见 `writing-band7/log/sessions/2026-08-10-drill-T2-18.md` 的「题目」行），本条却只存了后半句。
> 而 `SKILL §G1 断言 1` 要求题面与本文件**逐字一致** ⇒ 缺这一句 = 下次出题时那条断言必然 FAIL，
> 或者（更糟）被静默改成"差不多一致"。**题面是逐字对象，不是摘要。**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | **cold 限时** | **5.5** ⚠️不可比（TR 6.0 / CC 6.0 / LR 5.0 / GRA 5.5） | 拼写 7 个（cruial / maintainance / neccessary / goverments / popution / orderly·oderly）；`bring **in** some benefits`；`On the **society** side`→social；`**These** knowledge`；`more clear`；🚩 `the leaving school time of students is usually before 5pm`（**中式旗舰标本**）；`an ageing population **put** massive burden`；`With ages growing`（悬垂）；`long-term ills`；`the youth workplace` |

| 2 | **08-10** | **cold 限时 40min** | **6.0**（TR 6.5 / CC 6.0 / LR 6.0 / GRA 6.0） | 284 词 · 干净句率 **37.5%**（上次 23%）· **拼写 0**（上次 7）· 词汇错 9（上次 14）。🎯两个靶子全中（拼写归零 / 段尾零 `Therefore`）。❌未盯的全复发：冠词×4（As for family level · young workforce · retirement age · the pension）· `makes sb have`×2 · 逗号粘连 `A case in point is China, students…` · `the challenge`(应复数) · `much more early` |

> ⚠️⚠️ **attempt #1 的分 2026-08-10 二修（F64）**：这一行原来写的是 `6.5（TR 7.0/CC 7.0/LR 6.0/GRA 6.0）`，
> 而**同一篇文章**在下面的进度曲线里是 `5.5`、在 `scoring.md §6` 的校准走查里也是 `5.5`。
> **一篇作文三个值**，而 attempt 行正是排序键 K2 和「题级毕业 ≥6.5」实际读的那一行 ——
> 留着它就等于让选题和毕业判定读一个已知错误的数。⇒ 统一为 **5.5（TR 6.0 / CC 6.0 / LR 5.0 / GRA 5.5）**，
> 出处 `scoring.md §6` 的逐项走查：(6+6+5+5.5)/4 = 5.625 → 5.5，且**与实考分一致**。
> 该分仍标 ⚠️ 不可比（08-10 之前，见顶部「可比分」定义）。

📍 本次原稿见 `drill/sessions/2026-08-10-drill-T2-18.md`
🎯 **下次（第 3 次）靶子**：①**P2 冠词**（可数单数前必有限定词；泛指制度性开支用复数无冠词）②**P7 逗号粘连**（逗号两边都能独立成句 → 改句号或加 where/and/which）。拼写（P5）与段尾变化继续保持但不再当靶子。
> 📌 推出依据（补记，供 `G6 断言 6` 复算）：两个代号都取自 08-10 的**靶子外出现**集
> `{P2×4, P1/P3×4, P12×4, P11×2, P4×2, P7×1, P6×1}` ✅
> （P11/P12 是五审新增的代号，此处回填；`{P2,P7} ⊆ 该集` 仍然成立）。
> 其中 P2/P7 **不是** SKILL 定义5 意义上的「复发」（07-14 那次没记这两个代号）——
> 选它们的理由：P2 是当天频次最高的一项（4 处），P7 是她"教过 4 次仍复发"的老账（profile §P7）。
> ★ 定义5 的复发集是 `{P1, P3, P4, P6}`，下一轮若这两个靶子清零，优先回到这个集合。

📍 `gemini/corrections_2026-07.md:695-701`
⭐⭐ **对照实验（全库最有价值的一组）**：与 T2-04 同话题。
- T2-04：**未限时**，2 处小错，判 ~7.5
- T2-18：**限时 40 分**，14+ 处错，判 **5.5**
  > ⚠️ 这一行改过两次，第二次还改错了（八审查出）：
  > 原写 6.5 → 五审改成 6.0 → **八审改成 5.5**。
  > 判据：「14+ 处错」是 **07-14** 那次（`scoring.md:209` 词汇错 14），而 07-14 的分是 **5.5**。
  > 08-10 那次是 9 处错、6.0。五审只看了"判 6.5 不对"就改成 6.0，**没看这句说的是哪一次** ——
  > 于是给同一篇作文造出了**第四个值**，而它正是为了修「一篇作文三个值」才动的那一行。
  > ★ 教训：改一个数之前先确认它在描述哪一次。**四处分值的对账见 `G6 断言 5`。**
→ **限时的代价 = 整整两个档**（7.5 → 5.5）。 这就是为什么所有分必须标 timed/untimed。
→ `scoring.md §6` 用的就是这篇做校准走查。

---

## A5 · 两问题（4 题）

### T2-19 独居增多：为什么 + 好坏 〔非剑桥·教练题〕
> Many people now live alone, both in cities and in rural areas. **Why is this happening? Is this a positive or negative development for society?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 05-26 | 仿写 | ~6.5 ⚠️ | `the **rising** of solo living`；`Regarding **economy**`；`community **bond**`；`These demonstrate ___`（漏 that）；**L 句与内容不符**（说 privacy 但正文没提） |
| 2 | 05-26 | 仿写二刷 | ~6.5–7 ⚠️ | 13 个旧 gap 全修好，但**冒出 5 个新形近词错**：`model careers`→modern；`almost negative`→mostly；`per capital`→capita；`househoulds`；`has founded`→found |

📍 `2026-05-26-ex05-v1.md:38-60` · `2026-05-26-ex05-v2.md:37-51`
🔑 **这题记录了一个关键机制**："修 3 个 gap"和"拼写自检"是**两条独立的注意力通道** —— 盯着改 gap，拼写通道就关了。→ 交前必须**单独**跑一遍拼写扫描

---

### T2-20 自雇：为什么 + 缺点 〔剑 14 T4〕⭐ 有官方带分样卷
> Nowadays, many people choose to be self-employed, rather than to work for a company or organisation. **Why might this be the case? What could be the disadvantages of being self-employed?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 06-15 | cold **未限时** | ~7.5 ⚠️ | 仅 2 处：`becoming self-employed has become`（重复）；`unpredictable **incomes**`→income |

📍 `log/sessions/2026-06-15-2pt-cold.md:18-22`
⭐ **对照读**：剑 14 官方同题样卷 = **Band 7.5**，考官评语见 `anchors.md` 锚 B。**这是她的目标状态的实物样本**

---

### T2-21 孩子长时间用手机：为什么 + 好坏 〔剑 17 T2〕
> Some children spend hours every day on their smartphones. **Why is this the case? Do you think this is a positive or a negative development?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 06-15 | cold **未限时** | ~7–7.5 ⚠️ | 仅 1 处：`damages both their physical **bodies** and their mental focus`→physical health |

📍 `log/sessions/2026-06-15-children-phones.md:15-19`

---

### T2-22 全球时尚：如何形成 + 好坏 〔剑 20 T4〕
> Fashion has become a global phenomenon. **How has this happened? Is this a positive or negative development?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | **cold 限时** | **6.5**（TR 7.0 / CC 7.0 / LR 6.0 / GRA 6.0） | `counties`→countries；`eassy`；`exmaple`；`peopel`；`Toutube`；🚩 `go **rural**`→go **viral**；`a large **amount** of people`→number；`every **T-shirts are**`；`phenomenon **that**`→where；`the preference **are** constantly **effecting**`；`global fashion **play**`；`people **benefits**`；`Looking forwards`；`we can **expected**` |
| 2 | **08-29** | cold 限时（★ 先交中文构思稿并经清单诊断，见 sessions/2026-08-29.md a-3～a-10） | **7.0**（TR **7.0** / CC **7.0** / LR 7.0 / GRA 7.0） | 372 词 · 17 句 · 干净句率 **88.24%**（15/17）· 词汇错 **2**，K270 = **1** · **零拼写错**（07-14 那次 5 处，含 `go rural`→viral）。<br>只有两处：`**Video** created by…`→Videos（GRA 单复数，本篇 R2 唯一命中）· `this trend is **highly positive development**`→a（GRA 冠词，同一个块在结论里写对了）。<br>词汇错两处：`identical information and **materials**`（服装语境指面料，中文要的是"东西"）· `a wave of **follow-up trends**`（follow-up ≠ 跟风）。<br>⚠️ LR 与 GRA 查表本来是 8.0，撞 §2.3d 硬约束② 压回 7.0（**封顶来的，不是挣的**）；**TR 7/7 与 CC 4/4 是实打实查出来的**。<br>🎯 靶子2（介词）**清零**：全篇固定介词零失守；靶子1 守住但**不宣布清零**（Body2 的关键删改出自中文诊断） |

📍 `gemini/corrections_2026-07.md:808-814`
🎯 靶子：①**P4 单复数/主谓**（重灾区，5 处）②**P5 拼写**（5 处）

---

## A6 · 其它题型（3 题）

### T2-23 网购取代实体店：原因 + 对传统零售的影响 〔非剑桥·教练题〕· C/E
> In recent years, more and more people are buying clothes, shoes, and other items online instead of in shops. **What are the reasons for this trend, and what are the effects on traditional retail stores?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 05-24 | 仿写（首次用中文骨架） | ~6.0 高位 ⚠️ | `In terms of **convenient**`；`Amazon, which **have** built`；`challenges, most **is** negative`；`more **consumer** prefer`；`immerse pressure`→immense；🆕 并列谓语错 |
| 2 | 05-24 | 仿写二刷 | ~7.0 ⚠️（她仿写阶段最好成绩） | 0 硬伤 —— ⚠️ 但存的是**清版**不是原始错误版，这个 7.0 是改后文本的分 |

📍 `2026-05-24-ex04-v1.md:53-76` · `2026-05-24-ex04-v2.md:43-66`（清版）

---

### T2-24 儿童肥胖：原因 + 对策 〔非剑桥·教练题〕· C/S
> Obesity is a growing problem worldwide, particularly among children. **What are the causes of this trend, and what can be done to address it?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 05-21 | 仿写 | ~6.0 ⚠️ | 6 个拼写自检漏掉；🆕 悬垂修饰（结论段）；`cause **for**`→of；`leading children ingesting`；`teach kids on` |
| 2 | 05-23 | 仿写二刷 | ~6.0 高位 ⚠️ | 拼写 0（首次），但冒出 5 个新模式：`leading children **to having**`；`**researches** show`；`not caused by X, but Y`（漏第二个 by）；`require **a** clearer nutrition labels` |

📍 `2026-05-21-ex03-v1.md:16-28` · `2026-05-23-ex03-v2.md:16-30`

---

### T2-25 工时过长：问题 + 措施 〔非剑桥·教练题〕· P/S
> In many countries, people are working longer hours than ever before and have very little time for rest or leisure. **What problems does this cause, and what measures could be taken to solve them?**

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 06-04 | ⚠️ 只写了 3 句（其余是教练范文） | — | 🚨 **题型交叉**：`examine the main **reasons** for this shift` —— P/S 题答成 C/E；`The most serious problem ... is massively damaging`（系动词打架） |

📍 `log/sessions/2026-06-04-skeleton2.md:67-69, 90`
🎯 靶子：**【基线篇】** —— 该题 0 次限时 cold（只写过 3 句），按 `SKILL §4c` 分支③ **不给靶子**。
★ P/S 是她唯一没有完整 cold 产出的题型，优先补

---

## 📌 T2 缺口盘点（＝ 排序键 **K0** 的候选清单，逐题列，不是另一套优先级）
> ⚠️ 本节原来写着「最高优先」，与顶部「出题优先级」冲突。现已并入那张全序表的 K0 位（第 2 顺位）。
> ★ K0 的判定单位是**题**不是题组（F80）；一次命中就是一篇【基线篇】，
>   受 R4 约束：**每周期最多出 1 篇**。
- **T2-25**（P/S）—— 只写过 3 句，其余是教练范文 → **0 次限时 cold** → K0 命中
- **T2-01 / T2-07 / T2-19 / T2-23 / T2-24** —— 只有仿写版（读过范文再写，不算真 cold）→ K0 命中
- **T2-02**（半 cold，教练给骨架）· **T2-03 / T2-04 / T2-09 / T2-13 / T2-16 / T2-20 / T2-21**（均为**未限时** cold）
  → 按 K0 的条件（"没有任何一次**限时** cold"）**全部命中**
- **不命中 K0** 的 T2 题（有过限时 cold，走 K1→K2→K3→K4）：
  T2-05 · T2-06 · T2-10 · T2-11 · T2-12 · T2-14 · T2-15 · T2-17 · **T2-18**
  ⚠️ 它们的分**全部** ⚠️ 不可比（08-10 之前），只有 T2-18 attempt#2 是可比分

---

# PART B · TASK 1（20 题）

> T1 重跑不需要原图 —— 下面保留了图上数据。标 ⚠️ 的需要外部找图。
> 所有题面统一补官方结尾：*Summarise the information by selecting and reporting the main features, and make comparisons where relevant.*

## B1 · 柱状图（3 题）

### T1-01 五个欧洲国家家庭互联网接入率 〔**来源未查到**〕
> ⚠️ 2026-08-15 双语搜遍未找到剑桥册号出处，也无可靠机经来源；搜到的全是用户自编变体（三国 2007–2019、五国含 USA/India 等），没有一条是「五个欧洲国家 ＋ 2000/2005/2010」。⇒ 照实留空，不猜。
> The bar chart shows the percentage of households with internet access in five European countries in 2000, 2005, and 2010.

| 国家 | 2000 | 2005 | 2010 |
|---|---|---|---|
| Germany | 30% | 62% | 82% |
| France | 14% | 51% | 74% |
| Spain | 7% | 36% | 65% |
| Italy | 8% | 34% | 53% |
| Poland | 4% | 26% | 59% |

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 04-28 | cold 限时 35 分 | 未判 | `a dramatically growth`（W1+W3）；`lower rate`（W5）；`most largest`（W2）；`By 2020`→2010（W4）；**整个 2005 列漏写**（W3）；overview 语言渗进正文（W7） |

📍 `t1/coach/sessions/2026-04-28.md:20-26`

---

### T1-02 家庭周开销 1968 vs 2018（8 类）⭐ 她 T1 最好一篇 〔**剑 17 Test 3**〕
> ⚠️ **题面更正**：剑桥原文是 how families in **one country** spent their weekly income，**不是「英国」**——「英国」是本库自己加的。八类数据与原题逐条吻合。
> 数据（占周支出 %，各年合计≈100）：Food 35→17 · Housing 10→19 · Fuel & power 6→4 · Clothing 10→5 · Household goods 8→8 · Personal goods 8→4 · Transport 8→14 · Leisure 9→22

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-07 | **cold** | **≈7（摸到 7.5）** | **只有 1 处**：`slightly fell`→fell slightly（W1）。W15 片段首次清零；`specific` 首次清零；W17 时态改对；数据 16/16 全对；8 类全覆盖；overview 两根柱子 + odd-one-out（household goods 持平）都抓到 |

📍 `t1/coach/sessions/2026-07-07.md:136-139`
⭐ **这是她的能力上限证明** —— 说明 T1 达 7 完全可复现，问题只在稳定性

---

### T1-03 美国家庭按年收入 2007/2011/2015（分组柱）〔**剑 18 Test 2**〕
> The chart below shows the number of households in the US by their annual income in 2007, 2011 and 2015.

| 收入档 | 2007 | 2011 | 2015 |
|---|---|---|---|
| < $25k | 25 | 29 | 28 |
| $25k–$49,999 | 27 | 30 | 29 |
| $50k–$74,999 | 21 | 21 | 21 |
| $75k–$99,999 | 14.5 | 14 | 15 |
| $100k+ | 29.5 | 28 | **33** |
（单位：百万户）

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-08 | cold | **≈7**（overview 被评为当时最佳） | `three **specific** years`（反射复发→计数器归零）；`In stark contrast, **The** households`（句中大写）；`The group of`→groups；`through the period`→throughout |
| 2 | 07-14 | cold（交 Gemini） | **6.5**（TA 7.0 / CC 7.0 / LR 6.5 / GRA 6.5） | 🔴 `over **100,000 million** annually`（应为 $100,000 —— 差 100 万倍）；🔴 `ranked first in **2017**`（应为 2007）；`the number of family`；`the Unite State`；`resplectively`；`bellow`；`firstrunner`；`dip **at**`→to |

📍 `t1/coach/sessions/2026-07-08.md:20-23` · `gemini/corrections_2026-07.md:426-432`
⭐ **唯一一道两次都有原稿的 T1**：第 2 次反而更差（两个严重数据错）→ **W9 数据准确是她真正的头号风险**

---

## B2 · 折线图（6 题）

### T1-04 四国人均 CO₂ 排放 1967–2007 〔**剑 11 Test 3**〕
> The graph below shows average carbon dioxide (CO2) emissions per person in the United Kingdom, Sweden, Italy and Portugal between 1967 and 2007.

| Year | UK | Sweden | Italy | Portugal |
|---|---|---|---|---|
| 1967 | 11 | 9 | 4 | 1.5 |
| 1977 | 11 | 10.5 | 6 | 2 |
| 1987 | 10 | 8 | 7 | 4 |
| 1997 | 10 | 6.5 | 7.5 | 5 |
| 2007 | 9 | 5.5 | 8 | 5.5 |
（公吨/人）

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 04-29 | cold（花了 1 小时） | 未判 | `before **fell** significantly`→falling（W8）；`In 1969`→1967（W4）；`a fourfold growth`（W3）；`by the end of period`→the period |

📍 `t1/coach/sessions/2026-04-29-line.md:29-35`

---

### T1-05 关店 vs 开店 2011–2018（双线）〔**剑 17 Test 4**〕
> Closures：6,400 / 5,900 / 7,200(峰) / 6,500 / **600(全图最低)** / 5,200 / 5,000 / 5,200
> Openings：**8,500(全图最高)** / 3,900 / 5,000 / 6,200 / 4,000 / 4,000 / 4,200 / 3,000
> 关键关系：8 年里 6 年关店 > 开店（例外 2011、2015）

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-07 | cold，162 词，**没跑交前自查** | **≈6.5** | 🔴 **W6 零跨线对比**（最大扣分）；`stable for the first four years` 抹掉了 2013 峰值；`Regarding the closures.`（W15 片段）；`specifical`/`fluctated`（W13）；`approximate 4,000`（W1）；`slight reversal` 用在 600→5,200 九倍（**W16**）；`rest of period` 缺 the |

📍 `t1/coach/sessions/2026-07-07.md:15-18`

---

### T1-06 家电普及率 + 家务时长 1920–2019（双图）〔**剑 16 Test 1**〕
> 🔴 **2026-08-15 更正：原记「剑 13 T1」是错的**，双源核实为 **剑 16 Test 1**。按剑 13 去翻会翻空。
> 家电 %（1920/1940/1960/1980/2000/2019）：洗衣机 40/60/70/**64(回落)**/70/75 · 冰箱 2/55/90/100/100/100 · 吸尘器 30/50/70/90/100/100
> 家务小时/周：50/35/20/15/15/12
> 关键：**洗衣机是 odd-one-out —— 唯一没到 100%，且中途跌到 64 再回升**；跨图关系 家电↑ ↔ 家务↓ 才是本题的点

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-07 | cold | **≈6**（当日最差） | `Regarding the X.` 片段第 3 次；`specific` 第 3 次；`all of appliances`（W5）；`rest of period`；**漏 odd-one-out**（写成"levelled off at 70%"）；`inclined to 70%`；`is echoed`→was（W17）；`dramatic` 用在 40→75（W16）；**自查 0** |

📍 `t1/coach/sessions/2026-07-07.md:87-90`
🎯 靶子：①**W11 overview 特征选得弱**（漏 odd-one-out：洗衣机）②**W16 幅度词与数据不符**（`dramatic` 用在 40→75）
★ 这题产生了她的**交前 30 秒 7 点清单**（见 `profile.md §4`）

---

### T1-07 四个亚洲国家城市化率 1970–2040 〔**剑 18 Test 1**〕
> The graph below gives information about the percentage of the population in four Asian countries living in cities from 1970 to 2020, with predictions for 2030 and 2040.
> Malaysia 30%(1970)→~75%(2020)→**~83%(2040)** · Indonesia ~14%→53%→**~64%** · Philippines 略超 30%→1990 略低于 50%→2010 回落 ~42%→~56% · Thailand →**2040 达 50%**（44% 是它 2030 的位置）

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-09 | cold（交 Gemini） | **6.0–6.5**（TA 6.5 / CC 7.0 / LR 6.5 / GRA 6.0） | **数据读错 3 处**（W9）：Malaysia 2040 写成 80（实 83）、Indonesia 60（实 64）、Thailand 44（实 50）；`the dominance will **be** continue`；`the all countries`；`both of two countries`；`reaching **at** approximately`；`growed`→grew；`first runner`（自造词）；**悬垂主语** `the dominance ... hitting a peak of` |

📍 `gemini/corrections_2026-07.md:237-243`

---

### T1-08 三种金属月度价格变化率 2014 〔**剑 18 Test 4**〕
> The graph below shows the average monthly change in the prices of three metals during 2014.
> Y 轴 = 与上月相比的变化率 %。**Nickel**：1、2 月月涨 >4%；3–5 月 ≤+1%；之后下滑，**6 月见底约 −3%**；随后四个月在 −1%~−2% 走平；12 月回升 +1%。**Zinc**：2 月最高约 +3%，其余月份在 −1%~+2%。**Copper**：全年变化率绝对值均 <2%。

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | cold（**超时** —— 一直在想"环比"怎么说） | **6.5**（TA 7.0 / CC 7.0 / LR 6.0 / GRA 6.5） | 拼写 5 个（fluctution / whlie / modertate / occured / aboslute）；`plummeting in **Jane**`→June；`the price **pf**`；比较对象错位（copper/zinc 需 `those of`）；8 词名词块 `with the percentage of change compared with previous month being over 4%`；`-3% decrease`（语义重复）；`leveled off **about**`→at；`changed more **moderate**`→moderately |

📍 `gemini/corrections_2026-07.md:634-640`
🎯 靶子：①**W13 拼写**（5 个：fluctution / whlie / modertate / occured / aboslute）②**W1 副词/形容词位置**（`changed more moderate`）
★ 学到的方法：**照抄图上坐标轴的措辞，别自己造术语**

---

### T1-09 美国四个行业就业人数 1960–2020 〔**剑 21 Test 1**〕
> The graph below gives information about the number of jobs in four sectors of the economy in the US between 1960 and 2020.
> Healthcare ~2m(1960，最低)→略超 **15m**(2020，第一) · Retail ~6m→2020 与 healthcare 齐平(~15m) · Agriculture ~6m→1980 ~2.5m→2020 **~2m(最低)** · Manufacturing 15m(1960)→**1980 峰值 20m**→之后 40 年持续下滑

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | cold（交 Gemini） | **6.5–7.0**（TA 7.5 / CC 7.5 / LR 6.5 / GRA 6.5） | **行业名前多加 the**（the retail / the healthcare / the agriculture）→ 裸行业名不加冠词，配 sector/industry 才加；`expericed`；`agricultrure`；`was the last one in 1960`→the lowest；`the same level **of** the healthcare`→as；`before a drop for the next 40 years`→before dropping over |

📍 `gemini/corrections_2026-07.md:987-993`
📌 这题产出了她要的**排名句库**：`fell to the lowest position` / `ranked last` / `was overtaken by all other sectors` / `dominated the chart` / `were the bottom two sectors` / `held the highest position`

---

## B3 · 饼图（4 题）

### T1-10 六大区域用水结构（6 饼图）〔**剑 11 Test 1**〕
| Region | Industrial | Agricultural | Domestic |
|---|---|---|---|
| North America | 48% | 39% | 13% |
| South America | 19% | 71% | 10% |
| Europe | 53% | 32% | 15% |
| Africa | 9% | 84% | 7% |
| Central Asia | 7% | 88% | 5% |
| South East Asia | 12% | 81% | 7% |

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 04-30 | cold | 未判 | 🔴 **数据读错/标错**（W9 首现）：South America 写成 77%，且工业/生活标签互换；`agriculture **becomes** the primary **source**`→is + use（W10）；`A striking similar`（W1）；`the figure...stay`；拼写 countris/fallowed/remaing；大小写 europe |

📍 `t1/coach/sessions/2026-04-30-pie.md:22-30`
📌 教训："写完留 30 秒回去核数据 —— 数据错是 T1 最致命的扣分项"

---

### T1-11 三种营养素在四餐的分布（3 饼图）〔**剑 14 Test 1**〕（08-15 双源复核，原记正确）
> ⚠️ **题面用词**：剑桥原题是 **sodium（钠）**／saturated fats／added sugars，不是 salt。
> The charts below show the average percentages in typical meals of three types of nutrients, all of which may be unhealthy if eaten too much.

| | Breakfast | Lunch | Dinner | Snacks |
|---|---|---|---|---|
| Sodium | 14% | 29% | **43%** | 14% |
| Saturated fat | 16% | 26% | **37%** | 21% |
| Added sugar | 16% | 19% | 23% | **42%** |

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 05-03 | cold | **Band 7**（她第一个 7） | 只有 2 处：overview 内部逻辑冲突（"all three" vs "exception"）；`an equal 14% each`（冗余） |
| 2 | 07-06 | 框架先行 + 她 v2 自写 | **≈6.5**（结构 7 / 表层 6） | `potiently`/`Sturated`/`accout`（W13×3）；`charts illustrates`（W14）；`Followed by`（W15 片段）；`one of the smallest contribution`（W5）；`added sugar is mostly **digested** by snacks`→comes from；框架阶段 **W11 漏 odd-one-out**（added sugar 最大来源是 snacks 42%，不是 dinner） |

📍 `t1/coach/sessions/2026-05-03-pie.md:19-25` · `2026-07-06.md:154-157`
🔑 **W12 规则诞生于此**：说"最大/最小"前先查并列（breakfast 14 与 snacks 14 并列）
⚠️ 两个月后重做反而降了（7 → 6.5）→ **正是"同题反复练"要解决的问题**

---

### T1-12 英国某大学学生所会外语 2000 vs 2010（2 饼图）〔**剑 11 Test 2**〕
> ⚠️ **题面用词**：剑桥原题是 **proportions**，不是 percentages。
> The charts show the percentages of British students at one university in England who were able to speak other languages in addition to English, in 2000 and 2010.

| 类别 | 2000 | 2010 |
|---|---|---|
| No other language | 20 | 10 |
| French only | 15 | 10 |
| German only | 10 | 10 |
| Spanish only | 30 | **35（最大且上升）** |
| Another language | 15 | 20 |
| Two other languages | 10 | 15 |

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-06 | 框架先行 + 她 v2 自写 | **≈7.0** | v2 **零语法硬伤**。3 处精度问题（非错）：`who spoke foreign languages` 排除了 "No other language" 组 → 用 `what languages, if any`；`stayed completely stable at exactly 10%`（叠加冗余强调词）；`a specific English university`→one university in England。框架阶段 **W11**：两根柱子是同一事实的两面 |

📍 `t1/coach/sessions/2026-07-06.md:74-80`
📌 **本题定下硬规则**：rise/fall 的主语必须是**量**（proportion / percentage / share / figure / number），不能是人。❌ `those who spoke X rose` → ✅ `the figure for X rose`

---

### T1-13 ⚠️ 澳洲家庭能源使用 vs 温室气体排放（2 饼图）
> **图和题面均已丢失**，只有一行登记（`t1/coach/chart_bank.md:11`，05-03，标 Band 7）。**重跑需外部找图。**

---

## B4 · 表格（1 题）

### T1-14 纽约市人口 1800–2000（3 张表）〔**剑 20 Test 1**〕
> The first table below shows changes in the total population of New York City from 1800 to 2000. The second and third tables show changes in the population of the five districts of the city (Manhattan, Brooklyn, Bronx, Queens, Staten Island) over the same period.
> **表1 · 全市总人口**：1800 **79,216** → 1900 **3,437,202** → 2000 **8,009,185**
> **表2 · Manhattan**：1800 **60,515**（76%）→ 1900 **1,850,093**（54%，峰值）→ 2000 **1,538,096**（19%）
> **表3 · 其余四区合计**（Brooklyn/Bronx/Queens/Staten Island）：1800 **18,701**（24%）→ 1900 **1,587,109**（46%）→ 2000 **6,471,089**（81%）
> ⚠️ **2026-08-15 补全**：原来只录了 Manhattan 三个年份 + 其余四区两个年份，**全市总人口整张表和其余四区 1900 都漏了**
>    —— 而题面第一句说的就是"第一张表是全市总人口"。没有总数写不出合格的 overview。
>    数据经网上两个来源交叉核对且自洽：60,515+18,701=79,216 ✅ 1,850,093+1,587,109=3,437,202 ✅ 1,538,096+6,471,089=8,009,185 ✅

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | cold（交 Gemini） | **6.5**（TA 6.5 / CC 7.5 / LR 6.5 / GRA 6.5） | 🔴 **两处数据/年份错**（W9）：1,850,093 写成 1990 年（实 1900）；其余四区 1800 年写成 19,701（实 18,701）→ Gemini 原话"幻视，直接扣 TA"；`rised`→rose；`experienced a massive growth`（不可数）；`the majority of population`→of the population；`in the end of peroid`→at the end of the period |
| 2 | **08-15** | **cold 限时 20min** | **6.5**（TA 6.0 / CC **7.0** / LR **5.0** / GRA **7.0**） | 180 词 · 干净句率 **50.0%**（正踩 [50%,70%) 下边界）· 词汇错 9，K270 **14** → LR 掉进 5 档。🎯 P4单复数❌1处（The tables illustrates，第一句）· P2冠词❌1处。🔴 **拼写回潮 5 处**（popution/Manhatten/droped/alomst/meat，08-10 曾归零）· **W9 数据错 2 处**（75%应76% · 1,587,108应1,587,109）——**与她 07-14 在同一道题上犯的是同一类错**。⭐ CC 7.0：连接词范围好且不机械，`that of the five districts` 指代漂亮 |

🎯 **下次靶子（08-15 定）**：①**主谓搭配**（T1 专用配对表：数字/占比/趋势各能配哪些谓语——本篇三处翻车全在这）②**拼写**（本篇 5 处，08-10 曾归零，属回潮）
> 📌 推出依据：两个都取自本篇**靶子外出现**集 `{P5×5, P12×5, P1×3, P3×2, W9×2}`；
> **换掉 P2 冠词 / P4 单复数**——它们本篇各只错 1 处，已在收口；且按 §2.1b 新规，
> 这类"低压下她会、只是负荷时掉"的点**该设靶子不该 drill**，继续挂着即可。
> ⚠️ **W9 数据错不设靶子**（"回图核一遍"属不可执行反馈），但判分必查。

📍 `gemini/corrections_2026-07.md:873-879`
📌 **表格题是她覆盖最薄的题型（只练过 1 次）**

---

## B5 · 流程图（2 题）

### T1-15 乙醇（生物燃料）生产循环 〔**剑 19 Test 3**〕
> **原题任务句**（2026-08-31 她发来题目截图后补进档案，此前本条只有阶段数据）：
> `The diagram below shows how a biofuel called ethanol is produced. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.`
> 阶段：植物/树木借阳光+CO₂ 生长 → 机械收割 → 预处理、分解出纤维素 → 送往加工厂 → 转化成糖 → 加入微生物 → 产出乙醇 → 驱动车辆（汽车/卡车/飞机）→ 车辆排放 CO₂ → 被新植物吸收 → 循环重启
> ⚠️ 图元校准（2026-08-31）：Processing 那一格画的是**一组设备**（塔柱＋罐／瓶），**⛔ 不是厂房／烟囱**，
> 　 且图上**没有给这一格的动词** ⇒ 只能写「A 变成 B」，⛔ 不许写"送到加工厂／用热和化学品"（T1 三禁）

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-08 | cold | **≈6.5**（方法=7，拼写压到 6.5） | **拼写就是天花板**：deliveried / vehical / **trunks→trucks** / airphanes / entrie / **circle→cycle**；`is convert`→is converted |
| 2 | 08-31 | cold | **6.0**（TA 5.0 / CC 6.5 / LR 6.0 / GRA 7.0） | **字数是唯一变量**：133 词 ⇒ 撞 §3.2 的 T1<150 惩罚，TA 6.0−1＝5.0；拿掉这 −1 就是 6.5。`trunks` 与 `circle` **与 07-08 同题错的是同一对**；CC 丢在 P4 三个中心；TA ④ 漏"CO₂ 被吸收"那一格 |

📍 `drill2/sessions/2026-08-31.md`（判分八步全打印）
📌 **同题隔 54 天，拼写的两个词原样复发**（trunks / circle）；airphanes 这次拼对了
📌 追加练后 133 → 171 词，⛔ 但**不改本篇判分**（§4.8）

📍 `t1/coach/sessions/2026-07-08.md:56-59`
🎓 **W15 句子片段在这篇毕业**（连续 3 篇干净）
⭐ 方法一次就掌握：现在时 + 被动贯穿；序列词；overview 写清"循环/线性 + 阶段数 + 起点终点"

---

### T1-16 竹子 → 布料（9 步）〔**剑 20 Test 4**〕
> ① 春天种竹 ② 秋天成熟，农民收割 ③ 切成条 ④ 机器压碎成液态浆 ⑤ 过滤分离长纤维 ⑥ 加水和氧化胺软化 ⑦ 纺成纱线 ⑧ 织成布 ⑨ 做成成品（T恤、袜子）

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | cold（交 Gemini） | **6.5–7.0**（TA 7.5 / CC 7.5 / LR 6.0 / GRA 6.5）—— 她 Gemini 组最高 TA/CC | `a multi-**stages** process`→multi-stage；`the **plantation** of bamboo`→planting；`automn`；`a process, **where**`→in which；🔴 `a ball of **yam**`→**yarn**（照抄图上错词，yam=山药）；`produced **with** fabric`→from |

📍 `gemini/corrections_2026-07.md:751-757`
📌 **流程图写不够 150 词的解法**（此题教的 4 招）：加状态变化 / 加工具方法（`using…`）/ 加修饰（thin strips, industrial machines）/ 加目的结果（`to turn them into…`）

---

## B6 · 地图（2 题）

### T1-17 农场 1950 vs 今天 〔**剑 20 Test 2** · Beechwood Farm〕
> 北部：大片羊场 → 露营地 + 太阳能板；新增两处停车场（一处在主路以北，一处在东侧）。其余：果树区减半，腾给新农场商店；谷仓南迁到农舍以西，腾地建度假小屋；软果/蔬菜/养鸡区保留（**在西侧**）；小径升级为道路（她漏了）；河流和农舍不变。图上**没有农场名**。

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-08 | cold | **≈7**（方法全对，卡表层） | `a agricultural`→**an**（**W18 诞生于此**，跨技能：口语也犯 a old / a internet）；`comping`→camping；`now **have occupied**`→now occupy；`west of farmhouse`→of **the** farmhouse；`combining farm`→farming；**方位错**（果蔬区在西不是南）；漏"小径→道路"；**自己编了农场名 "Beechwood Farm"** |

📍 `t1/coach/sessions/2026-07-08.md:83-86`

---

### T1-18 公共图书馆平面图 20 年前 vs 现在 〔**剑 18 Test 3**〕
> The diagram below shows the floor plan of a public library 20 years ago and how it looks now.
> 左侧：电脑室占据原阅览室；CD/录像/电脑游戏区 → 更大的儿童区（含沙发 + 讲故事区）；中左原成人小说区 → 全部参考书。右/中：中央的桌椅移除；中右原成人非虚构 → 成人小说 + 咨询台 + **三台自助机**；右上角原儿童书区 → 讲座室；入口旁原问询台 → 新咖啡吧。主入口与整体结构不变。

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-14 | cold（交 Gemini） | **6.0–6.5**（TA 7.0 / CC 6.5 / LR 6.5 / **GRA 5.5** —— 她 GRA 最低记录） | `has **underwent**`→undergone；`all functional rooms were **demolished**`→transformed/renovated（demolish=拆楼）+ "all" 过绝对；`will **found**`→find；`chidren's`/`kis`；`once entering the entrance`（语义重复）；`corridor`→section/room；`stores`→houses；`make room for`→make way for；🔴 **两处主观臆测**（`where people can take a break`）→ **T1 三禁**第①条 |

📍 `gemini/corrections_2026-07.md:531-537`

---

## B7 · 混合多图（2 题）

### T1-19 Little Chalfont 图书馆（饼 + 表 + 柱）〔**剑 20 Test 3**〕
> **饼 · 会员年龄 2016（%）**：儿童 22 · 青少年 13–17 **15** · 成人 18–64 **51** · 65+ 12
> **表 · 借阅类别 2016（%）**：儿童小说 **38** / 儿童非虚构 6 / 儿童 DVD 1（**儿童合计 45**）· 青少年 **2** · 成人小说 **38** / 成人非虚构 13 / 有声书 2（**成人合计 53**）
> **柱 · 总借阅量 2007→2016**：15,700 / 18,900 / 19,000 / 20,600 / 21,000 / 20,700 / **19,600** / 20,700 / 21,200 / 21,600

| # | 日期 | 条件 | 分 | 主要错 |
|---|---|---|---|---|
| 1 | 07-08 | cold | **≈7** | ⚠️ **最大缺口 W6 第 4 次**：没写跨图错配句 —— **青少年占会员 15% 却只占借阅 2%**；**儿童占会员 22% 却占借阅 45%**（这是本题最高分的句子）；`an upward growth`→trend；`through`→**throughout**（第 2 次）；`the groups of 13–17 age`→the 13–17 age group；2013 应为 19,600 不是 19,000 |

📍 `t1/coach/sessions/2026-07-08.md:121-124`
⭐⭐ **拼写 W13 和 a/an W18 首次双双清零**

---

### T1-20 ⚠️ 见 T1-06（家电+家务双图，已列在折线组）

---

## 📌 T1 缺口盘点（同上，＝ K0 候选清单）
- **表格题只练过 1 次**（T1-14）→ 覆盖最薄，K0 命中
- **T1-13 图已丢失**，需外部找图才能重跑
- **W6（跨线/跨图对比）在 4 道多图题上全部失手** → 这是 T1 从 6.5 到 7 的单一最大杠杆
- **W9（数据准确）实际频次 8–10 次**，且 T1-03 第二次比第一次更严重 → 交前核数据必须成为固定动作

---

# 附 · 进度曲线（每次 drill 后手工追加，禁脚本）

> 🔴 **两个干净率的定义在 `scoring.md §2.1`（唯一真源，本表不重述算法）**（F89）
> ```
> 全篇干净率   = 干净句 ÷ 总句数                       → **判分**用
> 靶子外干净率 = (总句数 − 含【靶子外】错的句数) ÷ 总句数 → **趋势**用 ＝ 本表的进步主指标
> ```
> 🔴 **怎么读这张表（F17 —— 不写清楚就会读出假进步）**
> ```
> 「全篇干净率」被【当次靶子选了什么】主导：盯什么什么就干净（08-10 实证，profile §8）。
> 靶子每次轮换 ⇒ 全篇干净率的涨落一大半在量【选题决策】，不在量【能力】。
> ⇒ **进步的主指标是「靶子外干净率」**（没盯的地方有多干净 = 自动化程度）。
>    全篇干净率只当【当次成绩】看，判分照样用它（scoring §2.1 是按全篇算的，别改）。
> ⇒ 两个数每次都要记。只有一列的行 = 那次没算，标 `—`，不许倒推补。
> ⇒ ★ **基线篇写 `n/a`，不是 `—`**（F70）：基线篇按 `SKILL §4c` 不给靶子，
>    **靶子外这个概念对它不成立**，不是"这次忘了算"。两个符号必须分开：
>      `—`  = 本该有，那次没算（可耻，从 D2 起禁止）
>      `n/a` = 结构上不存在（基线篇唯一合法）
>    原文同时写着"基线篇不做靶子内/靶子外分类"和三处"两个干净率都要报"，
>    直接互相矛盾 ⇒ 现在用 `n/a` 把矛盾消掉。
> ```
> **只收【可比分】**：untimed / (edited) / (zh-untimed) / 仿写 / 半 cold 一律不进本表（可写进各题的 attempt 行）。

| 日期 | 题号 | 条件 | 词数 | 总句/干净句 | **全篇干净率** | **靶子外干净率** | 词汇错 K / K270 | TR/TA | CC | LR | GRA | 总分 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **实际考试** | — | 真考 | — | — | — | — | — | — | — | — | — | **5.5 ← ground truth** |
| （基线）07-14 | T2-18 | timed 40min | ~280 | ~15 / 3–4 | **~23%** | — （当时无靶子概念） | 14 / 13 | 6.0 | 6.0 | 5.0 | 5.5 | **5.5** |
| 08-10 | T2-18 | timed 40min | 284 | 16 / 6 | **37.5%** | **37.5%** | 9 / 9 | 6.5 | 6.0 | 6.0 | 6.0 | **6.0** |
| 08-12 | T2-14 | timed 40min | 315 | 18 / 10 | **55.6%** | **55.6%** | 15 / **13** | 6.0⚠️ | 6.0⚠️ | **5.0** | **7.0** | **6.0** |
| 08-15 | T1-14 | timed 20min | 180 | 10 / 5 | **50.0%** | **50.0%** | 9 / **14** | **6.0**(TA) | **7.0** | **5.0** | **7.0** | **6.5** |

> ⚠️ 08-12 那行的 **TR/CC 标 `(zh-coached)`** —— 教练对她的中文构思给过意见，这两项不算 cold。
> LR/GRA 是纯 cold（语言层教练一个词没给），照常计。
> 🔴 **这一行最该读的不是总分，是两只手在互相抵消**：
> 干净句率 37.5% → 55.6%（GRA **6→7**），同时 K270 9 → 13（LR **6→5**），净效果原地。
> 成因是**同一个动作**：她这篇主动去够更难的词以避免重复（secure / negative / expenditure），
> 换错的比换对的多。⇒ 下一篇的可执行动作＝**别换词，用代词/上位词/省略**（drill 已给）。

> ✅ **08-10 的靶子外干净率 2026-08-10 三修补上（F89）：`—` → 37.5%。这是【算】出来的不是【补】出来的。**
> 那天两个靶子（P5 拼写 · CC 段尾槽位）**都是零出现** ⇒ 没有任何一句是"只因靶子内错误而脏"的
> ⇒ 16 个句子里的 10 个脏句**全部**含靶子外错误 ⇒ (16−10)/16 = **37.5%**，与全篇干净率相等。
> 手算全过程见 `scoring.md §2.1` 的「已跑过的一行」。**这不违反"不许倒推补数"** ——
> 倒推补数是拿印象填空；这里两个率的相等是定义的直接推论，输入只有已记录的 16/6 和"靶子零出现"。

> ⚠️ 08-10 那行初版写的是 7/7/6/6 = 6.5，**已按实际考分重判**。教练两次虚高的过程记录在 `scoring.md §6.5`。
> **近期目标 6.5，不是 7。** 三个可数靶子：① 词汇错密度进 LR 6.0 档 ② 干净句率进 GRA 6.0→7.0 档
> ③ 连接词去固定槽位（＝勾上 CC 清单第 3 项）。**具体阈值一律查 `scoring.md §2.1 / §2.2 / §2.3d`，本表不重述。**

> 📒 **每篇的 📊 行另有一份可枚举总账**：`writing-band7/drill/log.md`（`grep "^📊"` 就能全查出来）。
> 本表是人读的曲线，log.md 是机器可复算的流水。**两处都要写，且数字必须一致**（G6 断言 5）。

（第一次 drill session 起逐行追加）
| 08-20 | T2-17 | timed 40min | 371 | 20 / 16 | **80.0%** | **80.0%** | 3 / **2** | **6.0**(TR) | **6.0** | **7.0** | **7.0** | **6.5** |

> 📌 **2026-08-20 T2-17 attempt#2**（07-09 是 attempt#1）。她的 **T2 最高分**。
> 🔴 **本行起不再打 (edited) / (skeleton-seen) / (zh-coached) / (model-seen) / (no-rubric) 任何标记**——
> 她 2026-08-21 定：「你不用关心我的曲线，你如实评分即可」「你是辅助工作，不是 tutor」。
> 收稿闸与"进不进曲线"整套作废（SKILL §4⑤b / §5 / §10-6b 已改）。**每一篇都照常进这张表。**
> ⚠️ GRA 与 LR 两项查表都出 **8.0**，被 §2.3d 硬约束② 压回 7.0 ——**这两个 7.0 是封顶来的，不是挣的。**
> 分丢的地方全在 TR（5/7，丢"论证 WHY 不是 HOW"与"每段段尾 L 句"）与 CC（2/4，丢"每段一个中心"与"指代无歧义"）。
> ⇒ 下一步重点是**段落中心与段尾 L 句**，不是词汇也不是语法。
> ★ 靶子1（#0126 丢限定层）**首次清零**：14 层修饰零丢失。靶子2（数的一致）4 对 2 错，未清零。
> ★ 4 个脏句里 **2 个是标点**（冒号接转折 / 句号后接破折号片段）——只修标点，干净句率 80% → 90%。
