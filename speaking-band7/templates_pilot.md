# P2/P3 模版 + 展开方法论（Pilot v2，待 suzy 拍板 4 个 ruling）

> 6/20 pilot 产物（11 agent：抽模块→独立打分→改→再打分→破模版→方法论）。
> **验证逻辑（suzy 的信任条件）**：模版不是断言好，是 (a) 拿真实答案 decompile 出来 + (b) 拿没见过的测试题打分（适应力 1-5 + 覆盖率），propose→score→modify 迭代。
> **状态**：v2。4 个 ruling 待定（见末尾），定了再大规模迭代。

---

## 一、P2 模版（1 个骨架covers所有类型，体部是菜单不是清单）

**OPENER → [ANGLE] → [BACKGROUND 和/或 PICTURE] → CLOSE**

| 模块 | 必/选 | 干什么 | 实时思考 |
|------|-------|--------|----------|
| **OPENER** | 必 | 一口气说出"是什么"+ 1 个锚点事实(谁/哪/何时/是啥) | 先把名词说出来(名词就是开头,别找花哨开场)，再扣 1 个锚 |
| **ANGLE** | 选(人/抽象题 ON) | 种下全篇要兑现的**那一个**评判(最…的一个特质/这事的 stake) — **专治你"说完3点就 done"的死机**：它是一张body必须兑付的欠条 | 这题有没有诚实的一句话评判？人→挑**一个**特质(不是三个)；抽象→stake |
| **BACKGROUND** | 选 | 让后面画面落地的背景/铺垫，**用题目要求的任意时态**(过去习惯 / 来历 / 未来计划 = 一个动作三个时态) | "背景是什么" — 别把过去习惯/来历/未来计划当三个吓人的不同动作 |
| **PICTURE** | 选 | 唯一的"让它可见"动作(ONE-MOMENT 和 ZOOM 合并了，永远只需一个) | 这题给我一个可replay的**场景**(人/事)，还是一个能拆开的**笼统词**(物/地)？挑它给的那个 |
| **CLOSE** | 必 | 固定收尾：感受+意义，回扣 OPENER/ANGLE(兑付欠条)，让答案**落地不拖尾** | 现在我怎么**感觉**？为什么**重要**？两句大白话回扣开头 |

**类型只是体部权重不同，不是不同模版**：人/事→BACKGROUND+PICTURE(叙事脊)；物/地→PICTURE(拆词)+对比(描述脊，常无故事)；抽象(决定/目标)→BACKGROUND 改成"权衡/计划"+用反事实代替故事。

---

## 二、P3 模版（4 块脊 + 按题型查表加 1 块）

**STANCE → REASON(because链) → INSTANCE(落具体) → [型强制额外块] → RECAP**

| 模块 | 必/选 | 干什么 | 实时思考 |
|------|-------|--------|----------|
| **STANCE** 3 味 | 必 | 第一句，定调，锁定要取哪几颗珠子 | 先看**疑问词**：why/should/opinion→一句评判；compare→说**一个轴**；pros-cons→"两面都有" |
| **REASON** | 必 | 因果引擎，**不是"because it's good"，是机制**(because X, SO Y) | 问"为什么这是真的"，禁懒答，逼出一条链：claim→so→真实结果 |
| **INSTANCE** | 必 | 最便宜的拖时间：抽象话后立刻落 2-3 个大白话具体例 `like…, that kind of thing` | 刚说了抽象词→立刻报 2-3 个看得见的东西 |
| **CONTRAST** | 型强制 | compare/pros-cons 才 ON：给对面那项/另一面 | 只在 compare/pros-cons(STANCE 时就预载)，`X is different —`/`but on the other hand` |
| **CONCESSION/反事实** | 型强制+万能 | ①反事实(任意题正面枯了用)："没它会咋样"(你 6/18 自己发现的破死机器) ②让步(should/opinion/pros-cons/prediction 强制)：半句认对面再拉回 | 正面枯→翻成"没它会糟"；该让步的题型→认半句再回 |
| **RECAP** | 必 | 压缩收尾(别重列)，给个 top-down 收口 | 一句拉拢：why/should=单评判；compare=对称一对 |

**按题型查表(开口前就知道额外开哪块，封住 live 负荷)**：
- why/importance → 只脊（正面枯了加反事实）
- reasons("为什么有些人…") → 只脊
- compare → +CONTRAST（REASON×2，RECAP 对称）
- pros-cons → +CONTRAST（让步由 CONTRAST 兼了，**不再额外强制 CONCESSION**）
- should/opinion → +CONCESSION
- prediction → forecast 味 STANCE + 趋势 REASON + 未来场景 INSTANCE + CONCESSION（**最重，没真实 cold 样本，先单练**）

---

## 三、方法论（核心 —— 你要的"指导性"）

### ⭐ P2 vs P3 是相反方向的认知动作（confuse 这个 = 你 younger-vs-older 死机的真因）
- **P2 = 叙事解压**：展开问题永远是「**能不能让它可见？**」→ **降高度往感官走**(一个记得的瞬间 / 感官特写 / 具体时间地点)。取出的单位是**画面**，靠具体+不断地赢，只在最后 CLOSE 爬回高度一次。
- **P3 = 分析解压**：展开问题永远是「**为什么这是真的 / 机制是什么？**」→ **搭逻辑链**(because X, SO Y)，只在 INSTANCE 短暂降到具体例(5 秒拖时间)，再爬回评判(RECAP)。取出的单位是**理由**，靠因果链+认两面赢，**高度上下震荡**。
- 一句话：P2 的"加细节" = 加**场景/感官**；P3 的"加细节" = 加**原因/另一面**。
- 你之前把 P3 瞄成 P2 那种生动书面散文 → 锁死。解药 = 知道 P3 是逻辑+震荡，P2 是感官+下降。

### 关键 per-module 思考（最难的两个）
- **P2-PICTURE**(最赚分也最容易卡)：先判**形态** —— A 故事(人/事:setup→发生→一句payoff) or B 拆词(物/地:一个笼统词→2-3 具体)。永远只选一个，不要both。
- **P3-REASON**(最赚分)：拿到 claim 问"为什么真"，**禁止答"because it's good"**，逼出 `because X happens, SO Y`(真实机制)。

---

## 四、验证结果（诚实，含还不行的地方）

| | v1 | v2 | 说明 |
|---|----|----|----|
| **P2** | avgFit 4.14 / 覆盖 86% | avgFit 4.0 / 覆盖 86% | 均分微降是因为 v2 诚实把 book 题降到 3(合并丢了"复述剧情"功能，已标修)；但修好了 v1 三个根问题(SCENE 一名两用 / 未来题盲区 / ANGLE 不该全强制)，模块 7→5 |
| **P3** | avgFit 4.33 / 覆盖 83% | avgFit 4.5 / 覆盖 **100%** | 真涨：prediction 3→4(专门 recipe)，pros-cons 开头不再假装选边，全局必/选换成按型查表 |

**诚实 caveat（别当全验证）**：
- P3 100% 里 **prediction 是靠设计覆盖、没有任何真实 cold 样本** → 先单练再信。
- P2 几道 **future 题是靠"拼两个范文的模式"成立(re-derivation)，不是某一篇完整范文** → 先 cold 试。
- 真正**铁验证的核心**：P3 4 块脊+compare = 你 6/18 两篇零错 cold 的字面骨架；P2 人/决定/物 = 真 trace 到 新07/新12/老11。
- **生硬风险**：防死机的固定件(ANGLE 欠条 / `On top of that` / hedge / 固定收尾 / 固定开场)，**每篇都用就是 examiner 认出"背模板"的头号信号**。解法=每槽留 1 个默认+2-3 个轮换形，但轮换又在"选择=死机"的轴上加了 live 选择 → 这个赌注**没验证过**，是最该先盯的。

---

## 五、4 个 ruling（✅ suzy 6/20 已拍板，锁定）

1. **P2 = 诚实 6 模块**：OPENER / ANGLE(条件) / BACKGROUND / PICTURE(3 形:故事/拆词/**复述**, +future 用 imagined) / **PROBLEM**(process/团队题:problem→做了啥→结果) / CLOSE。体部=按 type 挑 2-3 个 {BACKGROUND, PICTURE, PROBLEM}。
2. **-s/冠词 扫描 = 答后复盘，不实时**（你两次零错 cold 都是没扫的纯组装；实时并行扫=双任务负荷=死机源）。⚠️ **覆盖 CLAUDE.md 的"产出后1秒自查"→明确为「整段说完再扫」，不在说的过程中扫。**
3. **P2 固定件图稳（不轮换）/ P3 建变化库**。suzy 关键洞察：P2 考场是**一题答一次**，零跨答案重复=无 tell；P3 是**一串 follow-up 连答**，同一 chunk 连用 5-6 次才是 examiner tell → 只 P3 需多备词组 + 结构/词汇变化。
4. **cold 过关线 = 到 ~2min 不死机 且 答案落地不拖尾**（production-gap 信号）；scorecard(FC/LR/GRA~7) 只抽查，不每篇追分（避免完美主义→死机）。

---

## 六、大规模迭代方案（拍板后跑，落 full_pass.md）
- **Phase 0 验赌注**(先于扩量，2-3 session)：cold 跑 5 张承载所有未决风险的题 —— 新11 团队[验 PROBLEM]、新20 书[验复述形]、老20 超支[验因果链体]、1 道 P3 prediction、1 道 future P2(老05 VR/老22 日本)。活下来=收敛；否则先补。顺带测轮换 vs 死机(3 道 P3 连背)。
- **Phase 1 给全 bank 打 type 标→体部 recipe**(离线不开口)：54 题分桶(人/物/地/事/process/media/决定目标/future-policy/future-experience)，每桶定死体部模块 → "用哪些模块"从 live 决策变查表。
- **Phase 2 做珠子卡(非整篇)**(离线创造，你低压主场)：每题填 recipe 要的 3-5 槽，复用范文措辞当原料。按 type 批量,让 recipe 在一个 type 内成反射再换。
- **Phase 3 cold campaign**(≥30% cold,其余 cold 水平范文,全 log)：按 type 簇,易先难后(P3 why/reasons/compare→P2 人/决定→硬尾)。每篇 log 1 个真错,追踪指标=「到 2min 不死机 且 落地不拖尾」。
- **Phase 4 收敛+去生硬审计**：每簇后扫重复 surface chunk(出现 3+ 次强制轮换);整类破才重推模版。每次更 study_hub + 写 session(硬规则)。
