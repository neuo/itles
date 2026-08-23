# problems.md

> 迁自旧档案 `_archive/profile.md`（旧号 E-001~E-323）。按族分段，族内按编号升序。
> **2026-08-19 做过一次全档逐条互比**：合并 25 条、撤销 1 条假错、8 条改族。
> 编号只增不复用，所以号段里有空号，那是被合并掉的。
>
> **迁移条目的历史记录只有日期、符号、场合三项** —— 旧档案里就没记内容。
> 从下一场起按 SKILL §3.1 写全。每条底部的「原始行」是旧表逐字，任何字段有疑问回那里核。
>
> **2026-08-23：🎓 条目已全部搬到 `graduated.md`（111 条，逐字搬运）。**
> 搬运由 **suzy 手动**做；教练只在本文件里**原地**把状态行改成 🎓，⛔ 不搬文件。
> 下面「族目录」的「条数」是**两个文件合计**（本文件 ＋ graduated.md）。

## 全档状态

```
★ 下面这一块 **2026-08-23 收尾时由 `drill.py stats` 产出**，⛔ 不许口算、不许沿用旧值（SKILL §0.4）

总数   **309 条**　＝ 本文件 198 ＋ `graduated.md` 111
在池   **169 条**（全在本文件）
🎓     **138 条（占 44.7%）**　＝ `graduated.md` 111 ＋ **本文件 27 条（08-23 毕业，等她搬）**
       本文件里等搬的 27 条：
       #0045 #0239 #0269 #0277 #0278 #0281 #0285 #0288 #0290 #0291 #0294 #0295 #0296 #0298
       #0299 #0300 #0301 #0304 #0305 #0306 #0308 #0311 #0313 #0314 #0315 #0319 #0320
退池   1 条（#0058）　并入 1 条（#0325 → #0059）
毕业线 **全档一律 2**（全档统一）
在池里 连对 1 的 **60 条** · 连对 0 的 **109 条**　（60 ＋ 109 ＝ 169 ✔ 脚本逐条实数）
　　　 校验：169 ＋ 27 ＋ 1 ＋ 1 ＝ 198 ✔　198 ＋ 111 ＝ 309 ✔
REVIEW 池 **10 条**：#0011 #0256 #0259 #0268 #0278 #0299 #0305 #0308 #0309 #0314
　　　 （脚本已核 ✔ 与 `review_pool.md` 一一对应）
题面待补 **0 条**（口径＝在池 ＋ 中文触发点标着「待补」）
最后一次全量校验 **2026-08-23 D1 收尾**：`drill.py check --all`
　　　　　　　　⇒ **ERROR 0 · WARN 0**（存量提示 252 处，全部是 2026-08-24 分界之前写下的行，不报错）
　　　　　　　　`drill.py stats` ⇒ 状态行 vs 历史重数 **零不符**，上次 vs 最后判定行 **零不符**
　　　　　　　　审计口径已同步的规则：
　　　　　　　　① 同日只推进一次、当天有 ❌ 就记 ❌
　　　　　　　　② **靠 ◎✅ 达到毕业线的照常毕业**，只是同时进 REVIEW 池（◎✅ 与 ✅ 同权）
　　　　　　　　③ 词表型未覆盖的成员**不扣毕业**，由 REVIEW 池存档题面承接（§3.5 第3.5步①）

🔴 **2026-08-22 她定的 5 条（本日第二批）**
　① #0325 并入 #0059（不可数名词一族）
　② **词表型条目出题不许只考一个词** —— 一道题必须让两个以上成员同时落地
　③ **靠 ◎✅ 凑到毕业线的：照常毕业，直接进 REVIEW 池** ——
　　 她的原话：「毕业，直接进入 review 池，避免反复出题，我会定期 review 的，你不用 care。」
　　 ⇒ #0011 #0256 #0259 保持 🎓，状态行下打 `⚠️🔍 **REVIEW 池**` 标记，清单写进 `review_pool.md`
　　 ⇒ ⛔ 教练不再出题、不追不催不复测
　④ 词表型条目里**顽固的成员单独摘出来新建条目，老条目照常毕业**
　⑤ 新建 3 条：#0326 impact 一族 · #0327 established practice 一族 · #0328 enrolment 一族
　（①②④ 已写进 SKILL §3.5 第 3.5 步；③ 写进 §3.3；出题纪律写进 §6）
2026-08-22 组1 增量：毕业 #0047 #0181 #0253 · 新建 0 条（#0322 建号当天被她撤销，见 F05 末尾墓碑）
2026-08-22 组2 增量：毕业 #0110 #0008 #0109 #0261 · 新建 #0323 #0324
2026-08-22 组3 增量：毕业 #0262 · 新建 0 条 · #0126 当天净结果翻转为 ❌（连对 1 → 0）
2026-08-22 组4 增量：毕业 #0018 #0250 #0251 #0252 · 新建 #0325 · ⚠️🔍 标记 +1（#0251）
2026-08-22 组5 增量：毕业 #0001 #0263 #0091 · 新建 0 条 · #0080 降级（连对 1 → 0）
2026-08-22 组6 增量：毕业 #0014 #0096 #0124 #0194 · 新建 0 条 · #0267 连对 1 → 0
2026-08-22 组7 增量：毕业 #0255 #0042 #0248 #0260 #0163 #0254（单组最高）· 新建 0 条 · 顺带用错 0 条
2026-08-22 组8 增量：毕业 #0257 #0103 #0176 · 新建 0 条 · **考点命中 10/10（本场唯一满分）**
　　　　　　　　　　★ 积压① 首次整改成功：#0059 双半题面一次通过（两个考点同句都落地）
2026-08-22 组9 增量：毕业 #0256（带 ⚠️🔍）· 新建 0 条
　　　　　　　　　　⚠️ §4.7 改判 3 处（同日口径未执行）：#0325 #0095 #0249 全部回退
　　　　　　　　　　⚠️🔍 标记累计 3 条：#0011 #0256 #0259（#0251 的标记随毕业撤销而撤销）
2026-08-23 组1 增量：毕业 **4 条** #0192 #0287 #0282 #0309（#0309 带 ⚠️🔍 进 REVIEW 池）
　　　　　　　　　　新建 **3 条** #0329 · #0331 时间所有格 · #0332 bear 一族（后两条是她点名要学）
　　　　　　　　　　#0126 连错 4 → 5 · △ #0221 拿到第一个实例并从 F11 迁入 F08
2026-08-23 组2 增量：毕业 **6 条** #0275 #0272 #0302 #0310 #0268（带 ⚠️🔍）#0284（顺带自发 ✅）
　　　　　　　　　　❌ #0303（连错 1）· #0074（连错 2）
　　　　　　　　　　⚠️ **#0095 同日口径翻转**：组1 ✅（patients/parents）／ 组2 ❌（works/workers，
　　　　　　　　　　　 08-11 犯过的同一对原样复发）⇒ 当天净结果 ❌，连对 1 → 0
　　　　　　　　　　◎− #0273（题面出错：情态 dare 只活在否定与疑问里，肯定句逼不出）
　　　　　　　　　　◎✅ #0267（教练 ❌ 被她当场推翻，连对 1）
　　　　　　　　　　⚠️ #0059 组2 的 ❌ **已撤销**（那是 workers 的打错，与不可数性无关），当天回到 ✅
🔴 **2026-08-23 她定的第三批 2 条（组2 判定发出后给的，全部已执行）**
　⑩ **#0267 第 7 题算对** —— 原话「第 7 题就是，你就是说我除了 the 不太对，其他翻译的对不对」
　　 ⇒ `quite challenging` / `a bit heavy` 都是正确英语、意思也送到 ⇒ 改判 ◎✅（§4.7 更正块已写）
　　 ⇒ 连带定下本条的**测量边界**：语域那一半中译英单点题测不了，只能挂作文验（SKILL §6 已加）
　⑪ **第 9 题是 workers 的打错，而且 `replace jobs` 别扭** —— 原话「9 我是打错了，明显应该用
　　 workers，你用 jobs，replace jobs 不觉得奇怪么」
　　 ⇒ #0059 的判定撤销、改归 #0095（work/worker 那一对原样复发）
　　 ⇒ `replace jobs` 造得出三个母语者反例 ⇒ 不判错；但**是我的中文题面「取代大量岗位」
　　 　 把她推向次优搭配** ⇒ SKILL §6 新增：中文题面发出前自己先直译一遍，确认落点是自然搭配
🔴 **2026-08-23 她定的第二批 3 条（组2 之后给的，全部已执行）**
　⑦ **题面提示直接给英文词** —— 原话「我觉得你废话那么多，不如直接点名你要什么词，
　　 把 skill 所有要隐藏题面或者说避免泄漏信息的都删掉」⇒ SKILL §6 §3.5 已删旧条款、写新纪律
　⑧ **不需要提示的题一个字都不给** —— 原话「很多不需要提示的你也提示那么多，也挺邪门的，
　　 比如这题，需要提示么？」⇒ 判据写死：**条目连对 ≥1 ⇒ 只给中文句，零提示**
　⑨ **#0268 的考点设计有问题** —— 原话「我不想用 believe，我觉得你的考点好奇怪」⇒ 异议成立，
　　 题面把 believe in 塞进了它不该在的宾语（老店手艺的自然动词是 trust）；已改题面到自然语境

🔴 **2026-08-23 她定的 6 条裁定（全部已执行）**
　① **#0330 不建，忽略** ⇒ 编号作废留墓碑（F10 段末）；第 1 题 `more than half` 回退为不判错，
　　 本组一字未改率由 60.0% 重算为 **80.0%**
　② **新建时间所有格条目** —— 原话「时间所有格，我不会主动用，可以新建一个条目练习下」⇒ #0331
　③ **新建 bear 条目** —— 原话「bear 我不会用，可以建个条目练习下」⇒ #0332
　④ **#0309 按规则毕业** ＋ **新出题纪律**：原话「**你出题的时候直接点名需要什么，
　　 不然那么多用法永远毕业不来**（写到 skill 里面，如何记录题面以及如何出题）」
　　 ⇒ §3.5① 的"两个成员"从**毕业闸**降级为**出题纪律**；条目里必须记「成员出题账」
　⑤ **第 3 题算对** ⇒ #0286 按 §3.2「她当场推翻 ⇒ 记 ✅」改判，§4.7 更正块已写；
　　 收紧后的判据：**题面括号里的结构点名是出题引导，不是判错的门**
　⑥ **归族按教练裁定** ⇒ #0221 F11 → F08（F10 族名维持不变，因为 #0330 不建了）
2026-08-23 组3 增量：毕业 **7 条** #0295 #0288 #0320 #0319 #0269 ＋ #0299 #0278（后两条带 ⚠️🔍 进 REVIEW 池）
　　　　　　　　　　❌ **1 条** #0318（连对 1 → 0，连错 1；`because of that` 缺 this ＋ `for the very reason` 缺 this）
　　　　　　　　　　✅ 建号后第一次答对：#0307（连对 1）· #0080（连对 1，两个考点自 08-18 以来第一次同时命中）
　　　　　　　　　　新建 **1 条** #0333 in-house 一族（她点名要学）
　　　　　　　　　　她另点名两处，**查重后不建号**：「扎根」＝ #0295 成员③ rooted in ·
　　　　　　　　　　「be limited to」＝ #0269 第三条路的成员 —— 两个都在本组当场落地了
　　　　　　　　　　R2 命中 1 处（`the child throw up`）· R1 R3 零命中
　　　　　　　　　　⚠️ 教练侧：**零提示 × 词表型 ⇒ 合法绕过 ⇒ ◎✅ 毕业**本场第 2、3 次
　　　　　　　　　　　（#0299 #0278），当日累计 5 次（#0309 #0268 #0267 #0299 #0278）
2026-08-23 组4 增量：毕业 **6 条** #0291 #0294 #0296 #0300 ＋ #0308 #0314（后两条带 ⚠️🔍 进 REVIEW 池）
　　　　　　　　　　◎− **1 条** #0276（教练题面把两个未知数塞进一道题，两边都不动，题面已改死）
　　　　　　　　　　❌ 顺带 1 条 #0048（`house … are` 少一个 s，连对 1 → 0）
　　　　　　　　　　✅ 但同日口径不推进：#0074 #0126（两条今天都在前面的组里记过 ❌）
　　　　　　　　　　新建 **2 条** #0334 weigh/balance A against B（她说不会）· #0335 not…until 一族（她点名）
　　　　　　　　　　R2 命中 1 处（与 #0048 同一实例）· R1 R3 零命中
2026-08-23 组5 增量：毕业 **9 条（全组）** #0315 #0304 #0301 #0290 #0285 #0281 #0313 #0045 #0239
　　　　　　　　　　★ **一字未改 100%、考点命中 100%、白测 0、R1R2R3 全零命中 —— 本线第一个零事故组**
　　　　　　　　　　新建 **1 条** #0336 所谓／so-called 的贬义陷阱（她点名要学）
　　　　　　　　　　★ #0313 是 08-22 被 `It is … that` 强调句白测掉的那条，本次真正行使
　　　　　　　　　　★ 更好版进入产出的第一个证据：#0285 她自发写出 08-22 给的 `comes down to`
2026-08-23 组6 增量：毕业 **5 条** #0298 #0306 #0277 #0311 ＋ #0305（带 ⚠️🔍 进 REVIEW 池）
　　　　　　　　　　✅ 建号后第一次答对：#0297（连对 1）· #0317（连对 1，08-22 整条绕开过）
　　　　　　　　　　❌ 顺带 1 条 #0095（`than` ← `that`，真词串台不豁免；同日口径只留证据）
　　　　　　　　　　新建 **1 条** #0337 at all times ／ at times 反义陷阱（她点名要学）
　　　　　　　　　　⚠️ 教练侧：#0297 后半题面缺陷（"一部分"逼不出可数复数）—— **她当场指出，成立**
　　　　　　　　　　R1 R2 R3 全部零命中（连续两组）
2026-08-22 组10 增量：毕业 #0177 #0258 #0259 #0264 · **降级 #0251（🎓 后复发，当天毕业当天塌）**
　　　　　　　　　　★ 本轮 102 条全部出完（§8② 完成）⇒ 下一步 §8③ 回看 ＋ §8④ 全档 review
　　　　　　　　　　⚠️ #0248 #0254 两条毕业时当日已重度预激，条目里已注明下周期换语境重测
```

> 🔴 **2026-08-20 规则变更（她定）：毕业线全部改成 2，「错一次抬到 3」整条作废。**
> 当天把 14 条毕业线 3 的全部改回 2：
> `#0001 #0014 #0018 #0025 #0045 #0048 #0055 #0074 #0095 #0124 #0126 #0128 #0163 #0192`
> 改完复算：这 14 条里连对 ≥2 的有 **0 条** ⇒ 没有人因此立刻毕业，只是门槛降下来了。
> 其中 **#0025 #0128 连对已经是 1，再对一次就 🎓**。
> 各条历史记录里写过的「毕业线抬到 3 / 保持 3」按 §4.7 留痕不删，一律以本行为准。
> SKILL §3.1 §3.3 §3.5A4 §4③d §8④c 已同步改完。

## 族目录

| 族 | 号段 | 条数 | 是什么 |
|---|---|---|---|
| **F01** 动词框架/论元 | #0001–#0329 | 27 | 动词后面接什么、及物性、论元完整 |
| **F02** 冠词/限定 | #0021–#0276 | 20 | a/an/the 的有无与选择、泛指定指、零冠词 |
| **F03** 中式块/硬编 | #0039–#0265 | 14 | 自己拼出来的名词块、中文直译块 |
| **F04** 单复数/主谓一致 | #0048–#0325 | 26 | 含长主语后谓语被拉走、不可数名词 |
| **F05** 拼写/形近词 | #0083–#0096 | 12 | 含构形规则、拼成另一个真词的串台 |
| **F06** 词类混用/位置 | #0097–#0278 | 20 | 形容词副词互换、比较级构形、修饰语位置 |
| **F07** 句法/逗号/并列 | #0049–#0288 | 48 | 逗号粘连、并列同形、语序倒装、从句、指代、大小写 |
| **F08** 词义/近义辨析 | #0090–#0332 | 69 | 选错词、近义词边界（含 #0221 同义重复，2026-08-23 自 F11 迁入） |
| **F09** 时态/体 | #0190–#0324 | 10 | 时态选择、时间状语与时态的配对、体的平行 |
| **F10** 语义缺失(中文丢一层) | #0126–#0331 | 2 | 语法全对但中文明写的一层没送到（＋#0331 时间所有格） |
| **F11** T1 数据/图表 | #0203–#0220 | 18 | 数据抄写、峰值占比、跨线对比、overview 特征选择、倍数（#0221 已迁 F08） |
| **F12** 任务层/篇章层 | #0222–#0312 | 4 | 只能挂作文验的 |
| **F14** 衔接/连接词 | #0223–#0319 | 13 | 连接词选择与位置、转折的搭法 |
| **F15** 语域/正式度 | #0229–#0321 | 14 | 口语词进书面、缩写、对冲词 |
| **F17** T1 整句仿写 | #0241–#0244 | 4 | 整句级改写 |
| **F18** T2 整句仿写 | #0245–#0247 | 3 | 整句级改写 |

---

# F01 动词框架/论元

> 动词后面接什么、及物性、论元完整

## #0002 which deteriorates the situation → which worsens the situation
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F01

**问题是什么**
P1 动词框架（deteriorate 多不及物）　R · 挂代号 P1

**怎么发现的**
2026-08-16　复习日 C1·组5

**我错在哪**
她的：which **deteriorates** the situation
正确：which **worsens** the situation

**中文触发点**
这让政府面临的处境更糟（08-16 题面加死：**这一政策进一步恶化了政府的处境** —— 原题面「更糟」是形容词比较级，最省力译法 makes the situation worse 完全正确、及物性考点整块消失；「恶化**了**＋宾语」把单动词＋宾语变成默认路线，且"恶化"正是 deteriorate 的中文对等词，她若还有 deteriorates+宾语 的习惯会直接浮出来）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组5

<details><summary>原始行（旧表逐字，旧号 E-014）</summary>

`这让政府面临的处境更糟（08-16 题面加死：**这一政策进一步恶化了政府的处境** —— 原题面「更糟」是形容词比较级，最省力译法 makes the situation worse 完全正确、及物性考点整块消失；「恶化**了**＋宾语」把单动词＋宾语变成默认路线，且"恶化"正是 deteriorate 的中文对等词，她若还有 deteriorates+宾语 的习惯会直接浮出来）|which **deteriorates** the situation|which **worsens** the situation|P1 动词框架（deteriorate 多不及物）|R · 挂代号 **P1**|0/3 篇|`

</details>

## #0004 worth + doing ≠ worthy of + n. → P1 动词框架
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F01

**问题是什么**
K（常驻·§3 实测缺口）　0/3 抽查

**怎么发现的**
2026-08-16　复习日 C1·组3

**我错在哪**
她的：`worth + doing` ≠ `worthy **of** + n.`
正确：P1 动词框架

**中文触发点**
这个提议值得考虑

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组3

<details><summary>原始行（旧表逐字，旧号 E-031）</summary>

`这个提议值得考虑|`worth + doing` ≠ `worthy **of** + n.`|P1 动词框架|**K**（常驻·§3 实测缺口）|0/3 抽查|`

</details>

## #0005 比起开车我更喜欢坐地铁 → 08-16 改题面：比起茶我更喜欢咖啡
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F01

**问题是什么**
K（常驻·§3 实测缺口） 08-16 改判 R：新题面下一次写对 I prefer coffee to tea ⇒ 从来不是知识缺口，此前 0/3 全是题面逼不出（E-276）　1/3（08-16 首次有效读数 ✅）

**怎么发现的**
2026-08-16　复习日 C1·组3

**我错在哪**
她的：`prefer A **to** B` ≠ `prefer to do A **rather than** do B`
正确：P1 动词框架

**中文触发点**
~~比起开车我更喜欢坐地铁~~ → **08-16 改题面：比起茶我更喜欢咖啡**（原题面动词对动词，天然可走 I'd rather…than，prefer 框架被整块绕过，记 ◎；名词对名词才逼得出 prefer A to B。详见 E-210）

### 历史记录
- 2026-08-16 ◎ 复习日 C1·组3（当日 2 次，取最后一次）

<details><summary>原始行（旧表逐字，旧号 E-032）</summary>

`~~比起开车我更喜欢坐地铁~~ → **08-16 改题面：比起茶我更喜欢咖啡**（原题面动词对动词，天然可走 I'd rather…than，prefer 框架被整块绕过，记 ◎；名词对名词才逼得出 prefer A to B。详见 E-210）|`prefer A **to** B` ≠ `prefer to do A **rather than** do B`|P1 动词框架|~~K（常驻·§3 实测缺口）~~ **08-16 改判 R**：新题面下**一次写对** `I prefer coffee to tea` ⇒ 从来不是知识缺口，此前 0/3 全是题面逼不出（E-276）|1/3（08-16 首次有效读数 ✅）|`

</details>

## #0006 burn itself out → P1 搭配
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F01

**问题是什么**
K（常驻·§3 实测缺口）　0/3 抽查

**怎么发现的**
2026-08-16　复习日 C1·组3

**我错在哪**
她的：`burn itself **out**`
正确：P1 搭配

**中文触发点**
他们只能等大火自己烧完

### 历史记录
- 2026-08-16 ❌ 复习日 C1·组3

<details><summary>原始行（旧表逐字，旧号 E-033）</summary>

`他们只能等大火自己烧完|`burn itself **out**`|P1 搭配|**K**（常驻·§3 实测缺口）|0/3 抽查|`

</details>

## #0015 每个孩子受教育的权利
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F01

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：guarantee children the right to education
正确：guarantee **every child's right to education**（"每个孩子"更贴，还省掉双宾）

**中文触发点**
每个孩子受教育的权利

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-189）</summary>

`每个孩子受教育的权利|guarantee children the right to education|guarantee **every child's right to education**（"每个孩子"更贴，还省掉双宾）|待排序|U（待定）|`

</details>

## #0016 「第二个是我不会」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F01

**问题是什么**
K（她点名）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：他建议我们早点出发
正确：★ `suggesting **we leave** early` 里嵌的 `(that) we leave early` **才是从句**，动词**用原形**：<br>　✅ suggesting we **leave** early　❌ we **leaves** ❌ we **left**<br>　原因：**suggest 后的 that 从句用虚拟语气**（完整形 `should leave`，英式常省 should）<br>★ 同族一律如此：`recommend / propose / insist / demand that sb **do**`<br>★ 与她已练过的另一条路并列（同一动词两条路）：<br>　✅ suggest **taking** another route（＋doing）<br>　✅ suggest **that we take** another route（＋that 从句，原形）<br>　❌ suggest **us to take**（suggest 不接 sb to do）

**中文触发点**
委员会建议这项计划推迟到明年再启动。（★ 用 recommend ＋ that 从句）
（旧留痕：「第二个是我不会」—— 08-16 建号时她点名 suggest + that 从句的虚拟语气）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-253）</summary>

`「第二个是我不会」（suggest + that 从句的虚拟语气）|他建议我们早点出发|★ `suggesting **we leave** early` 里嵌的 `(that) we leave early` **才是从句**，动词**用原形**：<br>　✅ suggesting we **leave** early　❌ we **leaves** ❌ we **left**<br>　原因：**suggest 后的 that 从句用虚拟语气**（完整形 `should leave`，英式常省 should）<br>★ 同族一律如此：`recommend / propose / insist / demand that sb **do**`<br>★ 与她已练过的另一条路并列（同一动词两条路）：<br>　✅ suggest **taking** another route（＋doing）<br>　✅ suggest **that we take** another route（＋that 从句，原形）<br>　❌ suggest **us to take**（suggest 不接 sb to do）|**K**（她点名）|`

</details>

## #0026 have the right to do sth → P1 + P2 冠词
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F01

**问题是什么**
K（常驻·§3 实测缺口）　0/3 抽查

**怎么发现的**
2026-08-16　复习日 C1·组5

**我错在哪**
她的：`have **the** right **to do** sth`
正确：P1 + P2 冠词

**中文触发点**
每个人都有受教育的权利

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组5

<details><summary>原始行（旧表逐字，旧号 E-030）</summary>

`每个人都有受教育的权利|`have **the** right **to do** sth`|P1 + P2 冠词|**K**（常驻·§3 实测缺口）|0/3 抽查|`

</details>

## #0266 「花多少时间」：take 的主语是事情或 it，人做主语要用 spend
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F01

**问题是什么**
中文一句「要花两天」，英文有**三个框架**，区别只在**谁当主语**：
　① **事情**当主语：`sth **takes** (sb) + 时间`
　　　`The process **takes** two days.` · `The repair **took** us a week.` · `Building it **will take** years.`
　② **it** 当形式主语：`It **takes** (sb) + 时间 + **to do** sth`
　　　`It **takes** two days **to process** an application.` · `It **took** her three years **to finish**.`
　③ **人**当主语：`sb **spends** + 时间 + **on** sth ／ **doing** sth`
　　　`Students **spend** two hours a day **on** homework.` · `She **spends** her evenings **reading**.`
三条硬边（作文里最容易踩的）：
　⛔ **时间直接当宾语，不加介词**：`takes two days` ✅　`~~takes **for** two days~~` ❌
　⛔ **人不配 take**：想说"人花了多少时间"用 spend；`He takes two hours to read it` 语法成立，
　　　但意思变成"他需要两小时"（讲能力/速度），跟"他花了两小时"不是一回事
　⛔ **②里的 to do 不能换成 doing**：`It takes time **to learn**` ✅　`~~It takes time learning~~` ❌
搭配副词：`takes **about / roughly / at least / no more than** two days`
**找法**：先定主语 —— 主语是"这件事"或 it ⇒ take；主语是人 ⇒ spend。

**怎么发现的**
2026-08-20　D3 学习日 C2·组1 第 7 题，她答对之后当场点名要学（§2③）：
「这个 take 的用法建一个条目，如果没有」。

**我错在哪**
她这次**没有错** —— `the process only **takes** two days` 走的正是框架①，一次到位。
建号理由是 §2③（她点名要学），不是她犯了错。
她真正缺的是**另外两个框架**：档案里从来没有她用 `It takes … to do` 或 `spend … on` 的记录，
说明这三条路她目前只走通了最短的那一条。

**中文触发点**
办完这些手续，一般人要花上一个星期。（用 it 开头那个说法）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）D3 学习日 C2·组1 第 7 题
  查重（§3.5 B0）：grep 了 `take`、`takes`、`It takes`、`spend`，全档命中四处，逐条比对：
  · #0018 的 `advises us **taking**` —— 讲的是 advise 的框架，take 只是恰好出现在例句里
  · #0143 附近的 `suggest **taking** another route` —— 同上，讲 suggest
  · #0257 正文里的 `can I **take** a message` —— 例句，不是考点
  · #0033 的 `time **taken away** from` —— 讲的是 the 加不加，被动分词
  四处没有一条讲 take 的**时间框架**，问 2 全部不成立（要另起一句话才讲得清）⇒ 新建。
  又查了 F09 族（时态/体）确认不是时态问题：本条管的是**论元结构**（谁当主语、时间放哪），
  与 #0252（瞬间动词配不了时段）相邻但不同 —— 那条问"这个动词能不能带时段"，
  本条问"带时段的时候主语该是谁"，问 1 不成立（一个换动词、一个换主语）⇒ 两条。
  建号时无对错，连对连错都是 0，毕业线 2。
- 2026-08-22 ❌ D4 复习日 C2·组2 第 8 题（顺带）　**建号后第一次被测就塌**
  她写 `he spent a whole summer **to adapt** to the environment there`。
  正确：`spent a whole summer **adapting** to…`
  ★ 正中本条框架③的形状：`sb **spends** ＋ 时间 ＋ **doing** sth`，后面是**动名词不是不定式**。
  ★ 建号那天（08-20）的判词写着：「她真正缺的是另外两个框架，档案里从来没有她用
  　 `It takes … to do` 或 `spend … on` 的记录」—— 今天她第一次用 spend，就用错了框架。
  　 **预测被验证了**：她只走通了框架①（sth takes 时间）。
  ⚠️ 两个框架的不定式／动名词恰好相反，容易互相污染，一起记：
  　`It **takes** time **to learn**` ✅（框架②要 to do）　`He **spends** time **learning**` ✅（框架③要 doing）
- 2026-08-22 ✅ D4 复习日 C2·组9 第 1 题　**判 ✅ 但不推进 streak（同日口径）**
  题面「他每天花两个小时在通勤上。（★ 主语是人，注意动词和它后面接什么）」
  ——★ **定点补测**：新写触发点，主语必须是人，专打她空着的框架③。
  她写 `he **spends** two house **commuting** every day`。
  ★★ **框架③一次到位**：主语是人 ⇒ spend，后面接**动名词**不是不定式。
  　 组 2 她写的是 `spent a whole summer **to adapt**`，同一天下午补上了。
  ⚠️ 按 §3.2「当天出现过 ❌ 就记 ❌」，本条今天的净结果已由组 2 定下 ⇒ **本行只留证据**，
  　 连对 0／连错 1 维持不变。
  ★★ **本条今天被按框架逐格测了一遍，写法值得复用**：
  ```
  组2  spent a whole summer **to adapt**   ❌ 框架③
  组4  usually **take** … **to process**    ✅ 框架①
  组8  **it takes** … time                  ✅ 框架②
  组9  he **spends** two hours **commuting** ✅ 框架③  ← 空着的那一格补上了
  ```
  📋 顺带用错：`two **house**` → `two **hours**`，拼成另一个真词 ⇒ 记 #0095。
- 2026-08-23 ✅ D1 学习日 C3·组1 第 2 题
  题面「这套流程走完要一个星期；光是材料费，她就花了将近两千块。
  （★ 前半用「事情 ＋ 动词 ＋ 时间」；★ 后半主语是人，"在…上花了多少钱"用另一个动词 ＋ 一个介词）」
  ——★ 出题设计留痕：**刻意不放框架②**（It takes … **to do**），因为同组第 3 题考的是
  　 「形容词 ＋ to ＋ 主动不定式」，放进来会互相提示（§6 考点层）。
  她写 `this process **took** a week. she **spent** nearly two thousand yuan **on** materials.`
  ★ 框架① `sth takes 时间` ＋ 框架④ `sb spends 钱 **on** sth` **两格同时落地** ⇒ 命中，连对 1。
  ★ 至此四个框架全部有过正面记录：
  ```
  框架①  sth **takes** 时间                08-22 组4 ✅ · 08-23 组1 ✅
  框架②  **It takes** sb 时间 **to do**    08-22 组8 ✅
  框架③  sb **spends** 时间 **doing**      08-22 组9 ✅（组2 先错过一次）
  框架④  sb **spends** 钱 **on** sth       08-23 组1 ✅  ← 最后一格补上
  ```
  ⚠️ `took` 用过去时**不判错**：中文「走完要一个星期」可读成"（那次）走完花了一个星期"，
  　 而且后半「她花了」明确是过去 ⇒ 母语者会写 `The whole process took a week; …` ⇒ 按 §0.8 不判。
  ⚠️ 同句一处不属于本条：`on materials` 丢了「**光是**」⇒ 记 #0126 ❌。
  📋 更好：`The whole process **took** a week, and she spent nearly 2,000 yuan **on materials alone**.`

## #0273 dare 作情态动词：dare not do，不加 to 也不加 s
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F01
🔴 **2026-08-23 补一条硬边（教练题面出错换来的）：情态 dare 只在【否定与疑问】里活着。**
　 肯定陈述句里没有情态 dare 的位置 ⇒ 那种语境只能走实义动词 `dares to do`。
　 ⛔ 教练出题时**不许把"敢做…"这种肯定句当本条的题面**（详见 2026-08-23 那行）。

**问题是什么**
`dare` 有两个身份，作文里两条路别串：
```
情态动词 dare   后面直接跟原形，**不加 to**；否定直接加 not；三单**不加 s**
  ✅ `what others **dare not** do`　✅ `He **dare not** speak.`　✅ `**Dare** she ask?`
实义动词 dare   照常变形，后面跟 to do（口语里 to 常省）
  ✅ `He **doesn't dare to** speak.`　✅ `She **dared** to ask.`
```
**判据**：句子里有没有别的助动词。没有助动词、直接 `dare not` ⇒ 情态；
用了 do/does/did ⇒ 实义，后面接 to do。
⛔ 别写混：`~~doesn't dare not speak~~` · `~~dares not to speak~~`
★ 作文里最好用的就是 `what others dare not do` 这个块 —— 六个词说完"别人不敢做的事"。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错** —— 这一处是她自己主动够出来的新表达，用法成立。
建号理由是 §2③（她点名要学），不是记她的错。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
很多人心里想换工作，但真正敢辞职的没几个。（"敢"用情态动词那条路）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `dare`，全档只命中今天作文的记录，零条目 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组2 第 5 题　**建号后第一次被测**
  题面「敢说真话的人在会上其实并不多」，她写 `People who **dare speak** truth are rare at the meeting`。
  情态那条路：后面直接跟原形、不加 to、主语是复数所以也不存在 -s ⇒ 命中，连对 1。
  ★ 教练这次**没有把存档触发点里的结构点名带过来**（原句带「"敢"用情态动词那条路」），
  　 她仍然自己走对了 —— 零提示的证据更硬。
  ⚠️ 同句一处不属于本条：`speak **truth**` 该是 `speak **the** truth`（固定块里的 the）
  　 ⇒ 挂 reminders.md **R3**，不建条目。
  📋 `at the meeting`：中文「会上」两读都成立（#0257），不判，只进更好版 `in meetings`。
  📋 更好：`**Few people** dare speak the truth in meetings.`（比 People who … are rare 直接）
- 2026-08-23 ◎− D1 学习日 C3·组2 第 2 题　**两边都不动，题面是我出错的**
  题面「真正的高手，敢做别人不敢做的决定。（★ 两个"敢/不敢"都必须用 dare 作情态动词那条路：
  后面直接跟原形，不加 to、不加 s）」
  她写 `A ture master is someone who **dares make** decisions that others **dare not make**`。
  ```
  后半 `others **dare not** make`     ✅ 情态路完全正确：not 直接加、无 to、无 s
  前半 `someone who **dares make**`   ✘ 混形：加了 s（走实义路）却没跟 to
  ```
  ★★ **但这一处是我的题面逼出来的，不是她的账 ⇒ 判 ◎−（两边都不动）。**
  ```
  语言事实（我出题时没想到）：情态 dare 基本只活在【否定】与【疑问】里 ——
    ✅ He **dare not** speak.        （否定）
    ✅ **Dare** she ask?  How **dare** he say that?  （疑问 / 感叹）
    ✅ Nobody **dare** move.  Few people **dare** speak.  （准否定的 nobody / few）
    ⚠️ 肯定陈述句里没有情态 dare 的位置 —— `someone who dare make` 读着就是坏的。
  ⇒ 我的题面前半是**肯定陈述句**（"敢做…的决定"），却要求走情态路 ⇒ 这条路根本走不通。
  ⇒ 她被夹在两条都不合法的路之间，写出混形 `dares make` 是题面诱发的。
  ```
  ⇒ 按 §3.2「◎− ＝ 她的答案有错，但错是题面诱发的 ⇒ 两边都不动」，连对 1／连错 0 维持。
  ⇒ 本条正文已加一条硬边（见状态行下方），并**改题面**：
  　 **存好的新题面（下次用）**：**他不敢把实情告诉老板；这种话，谁敢当着他的面说？**
  　 （★ 两处都用 **dare**：第一处否定 —— 直接加 not、不加 to、不加 s；第二处疑问 —— 主语提到 dare 后面）
  ⚠️ 拼写 `ture` → `true`：**ture 不是真词** ⇒ §3.2 复习组手滑豁免，不记 #0095。
  📋 最小修改（走她那条实义路，最省事）：
  　`A true master is someone who **dares to make** decisions that others dare not make.`

## #0274 分离式短语动词：drive sth down ／ drive up sth，宾语短放中间、长放后面
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F01

**问题是什么**
`drive down` 这类**动词＋副词**的短语动词可以被宾语劈开，放哪边由**宾语长短**决定：
```
宾语短（代词或两三个词）→ 放中间     `drive **costs** down` · `drive **them** down`
宾语长（一串修饰）      → 放后面     `drive down **the cost of renewable energy**`
⛔ 代词只能放中间：`drive **it** down` ✅　`~~drive down it~~` ❌
```
同族（作文高频，成套记）：
```
drive down / drive up      压低 / 推高（价格、成本、需求）
push up / push down        同上，更口语
bring down                 降下来（bring down unemployment）
cut back on                削减（不可分离，on 后面必须跟宾语）
carry out                  实施（carry out a policy / carry it out）
```
**找法**：写完短语动词，看宾语有几个词 —— 三个词以内塞中间，长了放后面，代词一律中间。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错** —— 这一处是她自己主动够出来的新表达，用法成立。
建号理由是 §2③（她点名要学），不是记她的错。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
新技术把这些设备的成本压低了将近一半。（"压低"用 drive 那个短语动词）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `drive` `push up` `短语动词`，全档零命中；与 #0007 #0008（动词配介词）不同 —— 那两条管介词，本条管**副词小品词的位置**，问 1 不成立 ⇒ 新建。
- 2026-08-22 ❌ D4 复习日 C2·组2 第 7 题　**建号后第一次被测就塌**
  题面「政府打算把这条线路的票价压下来」，她写
  `The government plans to push **the price of this line** down`。
  ★ **位置规则失守**：宾语 `the price of this line` 是五个词，按本条判据（三个词以内塞中间、
  　长了放后面）应写 `push **down** the price of this line`。
  　小品词 down 被推到句尾、和动词隔了五个词，读的人要等到最后才知道是"压低"还是别的。
  ⛔ 选 push 不选 drive **不扣分** —— `push down` 就写在本条同族表里，是合法成员。
  ⚠️ 教练侧：本条存档触发点里带一句结构点名「"压低"用 drive 那个短语动词」，
  　 我重写题面时把它丢了（§6 违规）。但**位置规则与选哪个动词无关**，这一处失守是她的。
  ⚠️ 同句一处不属于本条：`the **price** of this line` 票价应是 `**fares**` ⇒ 记 #0249（归入待确认）。
  📋 更好：`The government plans to **bring down fares on this line**.`（政策语境默认搭配 bring down）
- 2026-08-23 ✅ D1 学习日 C3·组2 第 5 题　**08-22 的失守修好了，连错归零**
  题面「连续三年的干旱把主要粮食作物的价格推高了将近四成。（★ "推高"必须用 drive 那个短语动词；
  ★ 宾语是"主要粮食作物的价格"这样一长串，注意它该放在副词的哪一边）」
  ——★ 上次的教练犯规（我重写题面时把「用 drive」那句点名弄丢了）**这次逐字带回来了**。
  她写 `a three-year drought **has driven up the prices of major grain crops** by nearly 40 percent`。
  ★ 宾语 `the prices of major grain crops` 六个词 ⇒ 按本条判据放在 **up 后面** ⇒ 位置正确，
  　 动词也选了 drive ⇒ 命中，连对 1、连错归 0。
  📋 顺带用对（三处，都不属于本条）：
  　· `a **three-year** drought` —— 连字符作定语、year **不加 s** ⇒ **reminders.md R3 第三条的正面命中**
  　　（08-22 她在 `5 years working experience` 上掉过这个零件，今天反方向的那一半写对了）
  　· `by nearly 40 percent` —— 「将近」落地（#0126 的正面半边）
  　· `a three-year drought **has**` —— 主谓单数一致（#0055 一族）
  📋 更好：`Three consecutive years of drought **have driven up the price of staple grains**
  　by nearly 40 **per cent**.`
  　（`staple grains` 比 `major grain crops` 紧一格；英式作文 `per cent` 分写更常见；
  　 `the price of X` 单数更像在说"某类东西的价格水平"）

## #0329 「在这件事上做／没做点什么」＝ do sth **about** sth，不是 on
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F01

**问题是什么**
中文的「在…上」「对…」是同一个字，英文按**动词**分成两条线：

```
do something / anything / nothing ／ a lot   ＋ **about** ＋ 那件事
  `The government has done **nothing about** the housing shortage.`
  `There is little we can do **about** it.`
  `We must do something **about** rising costs.`

take action ／ act ／ decide ／ a report ／ data  ＋ **on** ＋ 那件事
  `The council finally **took action on** illegal parking.`
  `Ministers must **act on** the findings.`
  `a report **on** youth unemployment`
```
**判据（一句话）**：动词是 **do** ⇒ 介词一定是 **about**；要说"采取行动"才走 **on**（配 act / take action）。
★ 同族「对…」的固定介词，一起记：
```
do sth **about** sth        对…做点什么
act **on** sth              按…行动／对…采取行动
have an effect **on** sth   对…有影响
be responsible **for** sth  对…负责
complain **about** sth      抱怨…
```
⚠️ 与 #0007（effective **in** cases）#0008（gamble **on** sth）不同：那两条各管一个词的介词，
　 本条管的是**同一个中文"在…上"分裂成 about / on 两条路**，判据是"动词是不是 do"。

**怎么发现的**
2026-08-23　D1 学习日 C3·组1 第 4 题（顺带）。主考点 #0279 命中，介词失守。

**我错在哪**
她的：`the government did nothing **on** it`
正确：`the government did nothing **about** it`
找法：**写完 do ＋ nothing/something，回头看介词——只能是 about。**

**中文触发点**
这些年物价一直在涨，可地方政府在这件事上什么都没做。
（★ "在这件事上什么都没做"里的介词；★ "什么都没做"仍要写成「主语 ＋ 动词 ＋ 一个宾语」三个词）

### 历史记录
- 2026-08-23 ❌ D1 学习日 C3·组1 第 4 题（顺带）　建号
  查重（§3.5 B0）：grep 了 `about` `介词` `搭配`，全档命中 10 条介词类条目 ——
  · #0007（effective **in** some cases）· #0008（gambling **on** these therapies）·
    #0204（reached **to** a peak）· #0208（peaked at … **in** 1900）：
    都是"某一个词配某一个介词"的单点，改正动作是换那个词的介词；
    本条的改正动作是**先判动词是不是 do、再定 about**，规则是一句分岔判据 ⇒ 问 1、问 2 都不成立。
  · #0253（conditions 用 under / cases 用 in）· #0257（at the meeting / in a meeting）：
    这两条的判据是"介词跟着后面那个**名词**走"；本条的判据是"介词跟着前面那个**动词**走"，
    方向正相反 ⇒ 问 2 不成立。
  · #0011（tell sb **about** ＋ 名词）：同一个介词 about，但那条管的是 tell 的第二个论元必须是信息，
    改正动作是"把 that 从句换成 about ＋ 名词"；本条是"把 on 换成 about" ⇒ 问 1 不成立。
  反向验（§3.5 1.3）：举得出"一个对一个错"的句子 ——
    `effective **in** some cases` 写对、同一句里 `do nothing **on** it` 写错，两者可独立取值。
  ⇒ 新建。

## #0334 把 A 和 B 放在一起权衡：weigh / balance A **against** B
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F01

**问题是什么**
中文的「把 A 和 B 放在一起权衡 / 拿 A 和 B 比着看」，英文**不是** `weigh A and B together`，
而是一个**固定的三件套**：动词 ＋ A ＋ **against** ＋ B。介词只能是 against。
```
✅ `We must **weigh** the benefits **against** the costs.`
✅ `The rights of the individual must be **balanced against** the interests of society.`
✅ `You have to **set** the risk **against** the possible return.`（set … against 同款）
⛔ `~~weigh the benefits and the costs together~~`　⛔ `~~balance A with B~~`
```
**三个动词的分工**
```
weigh A against B     **掂量**哪一边重（还没有结论，正在比）      ★ 议论文正文最常用
balance A against B   **求平衡**（两边都要照顾，不是二选一）      ★ 常用被动 be balanced against
set A against B       **摆在一起对照**（最中性，只是并排看）
outweigh              ⚠️ 这是**结论**：A 大过 B（见 #0299 #0312）——
                      weigh…against 是"在比"，outweigh 是"比完了"，别串
```
**被动是这一族在作文里的默认形状**（主语是被权衡的那个东西，不是人）：
`These gains **must be weighed against** the environmental damage they cause.`

**怎么发现的**
2026-08-23　D1 学习日 C3·组4 第 2 题。题面「一个人的权利，必须和整个社会的利益放在一起权衡」，
她整句答不出来，原话：**「A 和 B 一起权衡不会」**（§2③ 她主动说不会）。
查重（§3.5 B0）
```
① 词面查  dedup "weigh" "balance" "against"   ⇒ 命中 #0276 #0299 #0312 #0292 #0293 #0307
② 规则查  dedup "权衡" "对举" "两者比较"        ⇒ 命中 #0276 #0278 #0293 #0268
逐条否掉
  #0276  它是"泛指一个人怎么说"（someone/a person/an individual/one），命中只因为**正文例句里
         恰好有 balanced against 这几个字母** —— 那正是把她堵死的那句。问 1 改正动作完全不同 ⇒ 否
  #0299  exceed/outweigh/surpass/outstrip 四个"超过" —— 那是**结论**（A 已经大过 B），
         本条是**过程**（正在把 A 和 B 比）。问 3：会用 outweigh 完全不保证造得出 weigh…against ⇒ 否
  #0312  引言立场句的整段骨架（让步; however, I believe X outweigh Y），篇章层 ⇒ 问 1 不成立 ⇒ 否
  #0292 #0293 #0307 #0278 #0268  只是词面里带 weigh／对举二字，考点毫无关系 ⇒ 否
```

**我错在哪**
她的：（整句没写出来 —— 不是写错，是这个框架不在手上）
正确：`The rights of **the individual** must be **weighed against** the interests of society.`
**找法**：中文出现「把 A 和 B 放在一起…／拿 A 跟 B 比…／A 和 B 之间要取舍」——
　　　　立刻想 **against**，不要想 and／with／together。

**中文触发点**
修一条新路带来的好处，必须和它对这片湿地的破坏放在一起权衡。

### 历史记录
- 2026-08-23 ③ 建号（她说不会，§2③）D1 学习日 C3·组4 第 2 题
  题面「一个人的权利，必须和整个社会的利益放在一起权衡。」（主考点是 #0276）
  她答：「A 和 B 一起权衡不会」。⇒ 主考点 #0276 记 ◎−（题面把她堵死了，两边都不动），
  她说不会的这个框架按 §2③ 单独建号 ＝ 本条。两条交叉引用。
  ⚠️ 本条的**中文触发点已换场景**（湿地/修路），⛔ 不许拿组4 那句原题回来测（§6）。

---

# F02 冠词/限定

> a/an/the 的有无与选择、泛指定指、零冠词

## #0021 As for family level → At the family level
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F02

**问题是什么**
P2 冠词/搭配　R · 挂代号 P2

**怎么发现的**
2026-08-16　复习日 C1·组3

**我错在哪**
她的：**As for family level**
正确：**At the family level**

**中文触发点**
在家庭层面，祖父母能帮上忙（08-11 改题面：原「在家庭层面」是光杆短语，答成 `family level` 也说不清对错）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组3

<details><summary>原始行（旧表逐字，旧号 E-004）</summary>

`在家庭层面，祖父母能帮上忙（08-11 改题面：原「在家庭层面」是光杆短语，答成 `family level` 也说不清对错）|**As for family level**|**At the family level**|P2 冠词/搭配|R · 挂代号 **P2**|0/3 篇|`

</details>

## #0023 young workforce keeps dropping → the young workforce keeps dropping
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F02

**问题是什么**
P2 冠词　R · 挂代号 P2

**怎么发现的**
2026-08-16　复习日 C1·组3

**我错在哪**
她的：**young workforce** keeps dropping
正确：**the young workforce** keeps dropping

**中文触发点**
年轻劳动力持续下降

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组3

<details><summary>原始行（旧表逐字，旧号 E-012）</summary>

`年轻劳动力持续下降|**young workforce** keeps dropping|**the young workforce** keeps dropping|P2 冠词|R · 挂代号 **P2**|0/3 篇|`

</details>

## #0028 lead to loss in money and time → lead to a loss of money and time
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F02

**问题是什么**
P2 冠词/可数性＋介词（挂主错＝冠词）　R · P2

**怎么发现的**
2026-08-16　复习日 C1·组3

**我错在哪**
她的：lead to **loss in** money and time
正确：lead to **a loss of** money and time

**中文触发点**
会导致金钱和时间上的损失（08-16 题面补主语：这会导致金钱和时间上的损失）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组3

<details><summary>原始行（旧表逐字，旧号 E-070）</summary>

`会导致金钱和时间上的损失（08-16 题面补主语：这会导致金钱和时间上的损失）|lead to **loss in** money and time|lead to **a loss of** money and time|P2 冠词/可数性＋介词（挂主错＝冠词）|R · **P2**|0/3|`

</details>

## #0029 hierarchy diagnosis system → the hierarchical diagnosis system
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F02

**问题是什么**
P11 词形＋P2 冠词（挂主错＝词形）　R · P11

**怎么发现的**
2026-08-16　复习日 C1·组3

**我错在哪**
她的：**hierarchy** diagnosis system
正确：**the hierarchical** diagnosis system

**中文触发点**
分级诊疗体系（08-16 题面补主句：中国建立了分级诊疗体系 —— 原为光杆名词短语，没有动词逼不出限定词与词形）<br>★★ **读数规则先写死**：本条主错是**词形**，而中文「分级」有 tiered／graded／multi-level／hierarchical 四条等概率合法译法，只有一条带考点 ⇒ **只有 hierarchy 词族的答案算有效测试事件**；她写 tiered/graded 等＝正确但**无效读数**，记 ◎ 保持悬空，**绝不因为写对 tiered 就记 ✅**（比照 E-054）

### 历史记录
- 2026-08-16 ◎ 复习日 C1·组3（当日 2 次，取最后一次）

<details><summary>原始行（旧表逐字，旧号 E-073）</summary>

`分级诊疗体系（08-16 题面补主句：中国建立了分级诊疗体系 —— 原为光杆名词短语，没有动词逼不出限定词与词形）<br>★★ **读数规则先写死**：本条主错是**词形**，而中文「分级」有 tiered／graded／multi-level／hierarchical 四条等概率合法译法，只有一条带考点 ⇒ **只有 hierarchy 词族的答案算有效测试事件**；她写 tiered/graded 等＝正确但**无效读数**，记 ◎ 保持悬空，**绝不因为写对 tiered 就记 ✅**（比照 E-054）|**hierarchy** diagnosis system|**the hierarchical** diagnosis system|P11 词形＋P2 冠词（挂主错＝词形）|R · **P11**|0/3|`

</details>

## #0032 ⭐「但是加了是不是也对」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F02

**问题是什么**
（旧档案未单列，见下方「我错在哪」与原始行）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：**她对，教练说过头了。** 两个都成立：零冠词＝**分类**（说它是什么性质的时间）／加 the ＝**同一**（说它就是那一段），而本句里加 the 反而更有力（句式：`The time you spend on X is the time you don't spend on Y`）。**教练"加 the 会凭空暗示"的说法已撤销。**<br>判据不变、只是要用足：**the 要求「缩完只剩一个」＋「听者能确定是哪一个」**。反例 `This is money well spent` ✅／`the money well spent` ❌——缩完还剩无数笔。<br>★ 这条与她口语线自己抓出的 **「限定 ≠ 定指」** 是同一条规则的两张皮
正确：**K**（冠词判据，正是本周靶子）

**中文触发点**
花在应付考试上的时间，正是没能花在真正学习上的时间。（★ 两处"时间"都用 the）
（旧留痕：⭐「但是加了是不是也对」—— 指 `is time taken away…` 要不要 the。她对，两个都成立；
　这个题面锁"同一段时间"那个读法，the 是更有力的那一版）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-135）</summary>

`⭐**「但是加了是不是也对」**（指 `is time taken away…` 要不要 the）|**她对，教练说过头了。** 两个都成立：零冠词＝**分类**（说它是什么性质的时间）／加 the ＝**同一**（说它就是那一段），而本句里加 the 反而更有力（句式：`The time you spend on X is the time you don't spend on Y`）。**教练"加 the 会凭空暗示"的说法已撤销。**<br>判据不变、只是要用足：**the 要求「缩完只剩一个」＋「听者能确定是哪一个」**。反例 `This is money well spent` ✅／`the money well spent` ❌——缩完还剩无数笔。<br>★ 这条与她口语线自己抓出的 **「限定 ≠ 定指」** 是同一条规则的两张皮|**K**（冠词判据，正是本周靶子）|`

</details>

## #0033 花在这些疗法上的时间，就是从正规治疗那里挪走的时间
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F02

**问题是什么**
待排序　U（待定）

**怎么发现的**
2026-08-16　复习日 C1·组7

**我错在哪**
她的：**the time lost to alternative therapies** is **the time delayed for** proper treatment
正确：**the time spent on them** is **time taken away from** proper treatment（① spent on 比 lost to 自然 ② time taken away from＝挪走，比 the time delayed for 准）<br>★★ **这一句她 08-13 专门追问过"第二个 time 加不加 the"** —— 两个都对：零冠词＝分类，the＝同一（同一段时间），本句加 the 反而更有力

**中文触发点**
花在这些疗法上的时间，就是从正规治疗那里挪走的时间

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组7

<details><summary>原始行（旧表逐字，旧号 E-151）</summary>

`花在这些疗法上的时间，就是从正规治疗那里挪走的时间|**the time lost to alternative therapies** is **the time delayed for** proper treatment|**the time spent on them** is **time taken away from** proper treatment（① spent on 比 lost to 自然 ② time taken away from＝挪走，比 the time delayed for 准）<br>★★ **这一句她 08-13 专门追问过"第二个 time 加不加 the"** —— 两个都对：零冠词＝分类，the＝同一（同一段时间），本句加 the 反而更有力|待排序|U（待定）|0/2|`

</details>

## #0034 the percentage of ___ total population → the percentage of the total population
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F02

**问题是什么**
P2 冠词 ← 靶子内　R · P2

**怎么发现的**
2026-08-16　复习日 C1·组8

**我错在哪**
她的：the percentage of **___** total population
正确：the percentage of **the** total population

**中文触发点**
住在曼哈顿的人口**占总人口**的比例

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组8

<details><summary>原始行（旧表逐字，旧号 E-154）</summary>

`住在曼哈顿的人口**占总人口**的比例|the percentage of **___** total population|the percentage of **the** total population|P2 冠词 ← **靶子内**|R · **P2**|`

</details>

## #0035 「其实我在想要不要用 an」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F02

**问题是什么**
K

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：老年人口的增加是主要原因
正确：**本句 the 对。**判据仍是她自己那条【限定 ≠ 定指】：`the increase **in older people**` 被 in 短语缩到只剩一个、且 `is the main reason` 已把它定死 ⇒ 定指 → the。**an** 用在【首次引入、未定死】的场合：`An increase in fuel prices would hurt exports`（假设某一次增长）。★ 同族判据：`a rise in X` 常见于首次提及，`the rise in X` 用于回指

**中文触发点**
燃料价格一旦出现一次上涨，出口就会跟着受影响。（★ 用 an increase in… 开头）
（旧留痕：「其实我在想要不要用 an」—— 老题面「老年人口的增加是主要原因」那句 the 是对的；
　这个新题面落在"首次引入、还没定死"的那一侧，才逼得出 an）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-194）</summary>

`「其实我在想要不要用 **an**」（the increase vs an increase）|老年人口的增加是主要原因|**本句 the 对。**判据仍是她自己那条【限定 ≠ 定指】：`the increase **in older people**` 被 in 短语缩到只剩一个、且 `is the main reason` 已把它定死 ⇒ 定指 → the。**an** 用在【首次引入、未定死】的场合：`An increase in fuel prices would hurt exports`（假设某一次增长）。★ 同族判据：`a rise in X` 常见于首次提及，`the rise in X` 用于回指|**K**|`

</details>

## #0036 「这个 the 可以省掉么」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F02

**问题是什么**
K

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：学校应该保障学生每天的休息时间
正确：**能省，两个都对**：`guarantee students **daily rest time**`（零冠词＝分类泛指）／`guarantee **the** daily rest time **of students**`（被 of students 限定死 → 定指）<br>★ 判据仍是她自己那条 **「限定 ≠ 定指」**；与她 08-15 问的 E-135（`is time taken away from` 加不加 the）**是同一题**<br>⚠️ `rest time` 稍生硬 → `a daily rest **period**` ／ daily rest 更自然

**中文触发点**
公司应当保障员工每天的休息时间。（★ 走零冠词那条路：动词 ＋ 名词块，不加 the）
（旧留痕：「这个 the 可以省掉么」—— 能省，两条都对；这个题面锁"分类泛指"那一侧）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-259）</summary>

`「这个 the 可以省掉么」|学校应该保障学生每天的休息时间|**能省，两个都对**：`guarantee students **daily rest time**`（零冠词＝分类泛指）／`guarantee **the** daily rest time **of students**`（被 of students 限定死 → 定指）<br>★ 判据仍是她自己那条 **「限定 ≠ 定指」**；与她 08-15 问的 E-135（`is time taken away from` 加不加 the）**是同一题**<br>⚠️ `rest time` 稍生硬 → `a daily rest **period**` ／ daily rest 更自然|**K**|`

</details>

## #0038 政府开支去年上升了 20%
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F02

**问题是什么**
⚠️ 不地道　U · 待排序

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`**the** government spending went up by 20%`
正确：`**Government spending** rose by 20% last year.`（泛指的复合名词不带 the；要定指就整体带："**The government's** spending rose…"）<br>★ 与她刚问的冠词问题同一处：冠词管**整个块**，跟着定指性走；这句是泛指 ⇒ 不加

**中文触发点**
**政府开支去年上升了 20%**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-305）</summary>

`**政府开支去年上升了 20%**|`**the** government spending went up by 20%`|`**Government spending** rose by 20% last year.`（泛指的复合名词不带 the；要定指就整体带："**The government's** spending rose…"）<br>★ 与她刚问的冠词问题同一处：冠词管**整个块**，跟着定指性走；这句是泛指 ⇒ 不加|⚠️ 不地道|U · 待排序|0/2|`

</details>

## #0276 泛指"一个人"的四个梯度：someone / a person / an individual / one
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F02

**问题是什么**
同样是"一个人"，四个词的语域和用法差得远：
```
someone       最自然，主语宾语都好用          `**Someone** who changes jobs may struggle to adapt.`
a person      中性，但在学术文里略平           `a **person**'s life`
an individual 正式、略笨重。★ **只在需要和 group / society / the state 对举时才值得用**
              `The rights of **the individual** must be balanced against those of society.`
one           最正式，也最容易过头；`one's` 作所有格倒是很常用
              `**one's** experience` ✅　`**One** should always…` ⚠️ 偏老派
```
**判据**：这句里"一个人"是**和集体对着说**的吗？
　是 ⇒ an individual／the individual；不是 ⇒ 直接用 someone，最省也最自然。
★ 一篇之内**只用一套**：选了 one's 就不要中途跳成 your（这正是 T2-17 里丢 CC 那一项的原因）。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错** —— 这一处是她自己主动够出来的新表达，用法成立。
建号理由是 §2③（她点名要学），不是记她的错。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
- 2026-08-23（**第三版，下次用**）　在这类案子里，法律保护的是一个人，不是某个群体。
  ★ 为什么改：08-23 组4 用的第二版「一个人的权利，必须和整个社会的利益放在一起权衡」
  　 里塞了 `weigh A against B` 这个她**根本没有的结构** ⇒ 她整句答不出来，
  　 本条考点一次都没出场（记 ◎−）。第三版把"个体 ↔ 群体"的对举留下，
  　 把那个动词框架整个拿掉，只剩一个 `protect`。
- 2026-08-23（已作废，教练的账）　一个人的权利，必须和整个社会的利益放在一起权衡。
- 2026-08-22（已用过，08-23 组4 用的就是它的改写版）　一个人一旦换了工作，往往要花好几个月才缓过来。
  （★ 主语必须是**单数**的"一个人"；⛔ 不许用 people ／ those ／ anyone who）
- 2026-08-22（已作废）　换工作的人常常低估适应新环境要花的力气。（"换工作的人"用最自然的那个词）
  ★ 缺陷：提示写成了"最自然"，而最自然的恰恰是 people who ⇒ 把她推离考点，记 ◎✅

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `individual`，8 处命中全是 individual investors / individual experience（#0169 #0008 的内容），没有一条讲"泛指一个人怎么说" ⇒ 新建。
- 2026-08-22 **◎✅** D4 复习日 C2·组4 第 2 题　**算对，连对 1**（题面缺陷，不是她的问题）
  题面「换工作的人常常低估适应新环境要花的力气。（★「换工作的人」用最自然的那个词）」，她写
  `**people who** change jobs often underestimate the effort required to adapt to a new environment`。
  ★ 整句完全成立，复数泛指也完全符合题面 ⇒ 判 ◎✅，连对 +1。
  ⚠️ 但本条要的**单数泛指四梯度**一个都没出场。
  ★★ **这条题面是我写坏的，而且坏得很典型**：我加的提示是「用**最自然**的那个词」——
  　 最自然的恰恰是 `people who`，提示把她推**离**了考点。
  　 ⇒ 纪律（本日新增）：题面点名要点**结构**，不点"最自然／最地道"。
  　 　「最自然」是让她自由发挥的信号，与「必须走这条路」正好相反。
  ⇒ 题面已改死，见下方中文触发点 2026-08-22 那行。
  📋 顺带用对：`the effort **required** to adapt`（#0284 后置定语）· `adapt to a new environment`（#0305）。
- 2026-08-23 ◎− D1 学习日 C3·组4 第 2 题　**两边都不动，是教练的题面把她堵死的**
  题面「一个人的权利，必须和整个社会的利益放在一起权衡。」，她答：**「A 和 B 一起权衡不会」**。
  ★ 按 §3.2 的分诊问句（"你是整句出不来，还是卡在别的地方没走到这个考点？"）——
  　 **她已经自己答了**：卡住的是「权衡」这个动词框架，不是「一个人」这个考点。
  　 ⇒ 一律 ◎ 并当场改题面。她没有产出可判 ⇒ 落 **◎−**（不是 ◎✅），连对连错都不动。
  ⛔ **教练犯规**：本条正文里的例句就是 `The rights of **the individual** must be
  　 **balanced against** those of society.` —— 我照着例句写中文，把 `weigh/balance A against B`
  　 这个**从没测过、她也没有的**结构，塞进了一道考"泛指怎么说"的题里。
  　 一道题只能有一个未知数；这道题有两个，前面那个先炸了，后面那个就永远测不到。
  ⇒ 新触发点已写死（见上方 2026-08-23 第三版）。
  ⇒ 她说"不会"的那个结构按 §2③ 单独建号 ⇒ **#0334**，两条交叉引用。

---

# F03 中式块/硬编

> 自己拼出来的名词块、中文直译块

## #0045 the number of the population → the number of people ／ the population（二选一，不能叠）
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F03

**问题是什么**
P3 硬编名词块　R · P3

**怎么发现的**
2026-08-16　复习日 C1·组7

**我错在哪**
她的：**the number of the population**
正确：**the number of people** ／ the population（二选一，不能叠）

**中文触发点**
- 2026-08-19　这个城市六十岁以上的人口数量在过去十年翻了一番。（★ 题面重写：08-19 原题面「人数…超过两成」自相矛盾——人数是绝对数、两成是比例，她写 proportion 反而更准，考点整块绕过，记 ◎。新题面用绝对数并保留"人口"二字，叠词陷阱才在场）
- 2026-08-22　**08-19 存下的那条题面今天首次实际使用**（08-19 当天用的是被作废的旧题面）⇒ 下次必须换新的。
- （更早）住在曼哈顿的人数（08-16 题面加死补谓语：**住在曼哈顿的人数持续上升** —— 原为光杆 NP）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组7
- 2026-08-18 ❌ D1 学习日 C2·组6
- 2026-08-19 ◎ D2 学习日 C2·组3 第 6 题（**教练出题错误**，不是她的问题）
  教练出的题面是「城市里六十岁以上的**人数**今年首次超过了**两成**」——
  ★ **这个中文自相矛盾**：「人数」是绝对数，「两成」是比例，两者不能是同一个东西。
  她写 `the **proportion** of people aged 60 and over … is over 20%`，
  **她的处理比题面更准确**（比例配百分比）。本条考点（the number of + population 叠词）根本没出场
  ⇒ 记 ◎，streak 不动。
  📋 顺带用对：`aged 60 and over` 是标准写法，很地道。
  📋 `is over 20% for the first time this year` 成立；更好 `has passed the 20% mark for the first time`
  （"首次超过"是事件，完成时更准）。
  ⇒ 题面已重写（见下方中文触发点 2026-08-19 那行），改成绝对人数并保留"人口"这个词，
  这样 `the number of the population` 的陷阱才在场。
- 2026-08-22 ✅ D4 复习日 C2·组1 第 2 题　**08-19 存下来的新题面首次实际使用**
  题面「这个城市六十岁以上的人口数量在过去十年翻了一番」，她写
  `**the population** aged 60 and over has double over the past decade`。
  ★ 两条路里选了 `the population`，**没有叠成 the number of the population** ⇒ 考点命中，连对 1、连错归 0。
  📋 顺带用对：`aged 60 and over` 标准写法 · `over the past decade` 与完成时配对准确 ·
  　`the population … has` 主谓数对（#0055 一族）。
  📋 同句两处教练当天判过、当天被她推翻的（**留痕**）：
  　`has **double**` → `has **doubled**`：原拟新建 #0322，**她当场撤销**
  　　（「这类和单复数一样，重复练习没有用，关键在于你需要不断提醒」）
  　　⇒ 不建条目、不进复习池，改挂教练侧常驻提醒 `reminders.md` **R1**
  　`**the** population` → `**the city's** population`：原判 #0126 ❌，**她当场改判为对**
  　　⇒ 名词前的语境限定语不算丢层，详见 #0126 的更正块
- 2026-08-23 ✅ D1 学习日 C3·组5 第 8 题　**连对 2 ⇒ 🎓 毕业**
  题面（零提示，换新触发点）「这座城市的人口数量已经连续三年下降。」，她写
  `the population of this city has dropped for three consecutive years`。
  ★ 中文里「人口数量」四个字同时在场（叠词陷阱在场），她仍然只取了 `the population` 一条路，
  　 **没有叠成 the number of the population** ⇒ 考点命中，连对 2。
  ★ 这也是 08-22 那次的原样重现，但换了句子（那次是"六十岁以上的人口数量翻了一番"）
  　 ⇒ 不是记忆复现，是同一个陷阱在新句子里没踩。
  📋 顺带用对：`the population … **has** dropped`（不可数集合名词配单数谓语）·
  　 `**for** three consecutive years` 与现在完成时配对准确（#0325 一族）·
  　 `**this city**` 这次没丢（08-22 那次丢了"这个城市"，当时她自己裁定不算丢层）。
  📋 更好：`The population of this city **has fallen** for three consecutive years.`
  　（fall 比 drop 书面，T1 图表叙述里 fall/decline 是默认词）

<details><summary>原始行（旧表逐字，旧号 E-158）</summary>

`住在曼哈顿的人数（08-16 题面加死补谓语：**住在曼哈顿的人数持续上升** —— 原为光杆 NP）|**the number of the population**|**the number of people** ／ the population（二选一，不能叠）|P3 硬编名词块|R · **P3**|`

</details>

## #0051 （无 floor —— 这是个检查动作不是表达） → 名词块「存在性测试」：这个块我是见过的，还是刚拼的？见过→用；刚拼→拆回主谓大白话
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-12 ｜ 族 F03

**问题是什么**
🔴 高　U · 在池（= §9 的 G1）

**怎么发现的**
2026-08-12　D2 作文

**我错在哪**
她的：（无 floor —— 这是个**检查动作**不是表达）
正确：**名词块「存在性测试」**：这个块我是见过的，还是刚拼的？见过→用；刚拼→拆回主谓大白话

**中文触发点**
写出一个名词块时先问自己

### 历史记录
- 2026-08-12 ❌ D2 作文

<details><summary>原始行（旧表逐字，旧号 E-039）</summary>

`写出一个名词块时先问自己|（无 floor —— 这是个**检查动作**不是表达）|**名词块「存在性测试」**：这个块我是见过的，还是刚拼的？见过→用；刚拼→拆回主谓大白话|🔴 高|**U · 在池**（= §9 的 G1）|0/2|`

</details>

## #0249 中文的"费"不等于 fee —— 水电这类定期账单用 bill
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F03

**问题是什么**
中文一个"费"字对应英文三个不同的词，直接映射成 fee 就错。
　**bill**　定期缴的账单：`the electricity bill` · `water and electricity bills` · `utility bills`（水电煤总称）
　**fee**　 为某项服务／资格付的钱：`tuition fees`（学费）· `an entrance fee` · `a membership fee`
　**cost**　做一件事总共花的钱：`the cost of the project` · `transport costs`
　**fare**　 交通票价：`bus / train / air **fares**` · `**fare** increases` · `a single **fare**`（2026-08-22 补）
**找法**：问一次"这钱是按月寄来的单子、还是为某项服务付的、还是做事的总花销"。
★ **一个词收掉水电煤：`utility bills`** —— 作文里不必写 water and electricity bills，
　`Once **utility bills** are included…` 一个词管住整类（她 08-19 点名要这个块）。
⚠️ 与 #0184（cost / price / spending 的边界）相邻但不同：#0184 分的是
"卖方要价 / 我付出的 / 一段时间总量"三分法，bill 与 fee 不在那三分法里，是另一组词。

**怎么发现的**
2026-08-19　D2 学习日 C2·组1 第 8 题

**我错在哪**
她的：`with **water and electric fee** added`
正确：`with **water and electricity bills** included` ／ `once **utility bills** are included`
注意还有一处数：两项东西（水＋电）配单数 fee 对不上，bills 要复数。
（`electric` 本身不算错 —— 美式 `the electric bill` 是常说的；真正错的是 fee。）

**中文触发点**
房租不含水电费，得另外交。

### 历史记录
- 2026-08-19 ❌ D2 学习日 C2·组1 第 8 题（顺带）
  查重（§3.5 B0）：grep 了 `fee` `bill` `utility` `electric`，全档零命中；
  又查了 F08 的 #0184（cost/price/spending）与 F06 的 #0107（transport expending → transport costs）。
  #0184 的规则句是三分法（卖方要价／我付出的／一段时间总量），bill 与 fee 都不在里面，
  要另起一句话才讲得清 ⇒ 问 2 不成立；#0107 讲的是 expend 没有 expending 这个名词形，是词形不是选词
  ⇒ 问 1 不成立。都不是同一条 ⇒ 新建。
- 2026-08-20 ✅ D3 学习日 C2·组1 第 4 题
  题面「房租不含水电费，得另外交」，她写 `the house rent doesn't include **ultility bill**`。
  选词命中：走的是 bill 不是 fee，而且自己调出了 utility 这个块（08-19 才教的）⇒ ✅，连对 1。
  同句两处不属于本条：
  · `bill` 该是复数 `bills`（泛指一类账单）—— 记在 #0048
  · `ultility` 拼写 —— 非真词，按 §3.2 复习组手滑豁免，不记；⚠️ 作文里出现照记
  · `the house rent` → 英式只说 `the rent`；`house rent` 是印度英语用法，不地道但不判错
  · 「得」译成 should 弱了一格，`you have to pay them separately` 更贴（不改变事实，不记 #0126）
- 2026-08-22 ❌ D4 复习日 C2·组2 第 7 题（顺带）　~~归入待确认~~ → **已于当日 §8④a 结清，见本块末**
  题面「政府打算把这条线路的**票价**压下来」，她写 `the **price** of this line`。
  正确：`the **fares** on this line` ／ `fares on this line`。
  ★ 中文一个「费／价」通向好几个英文词，本条的规则句是**按场合挑**：
  　bill（定期账单）· fee（服务／资格）· cost（总花销）· **fare（交通票价）** ← 今天补进正文。
  　`the price of this line` 不成立：line 是一条线路，它没有 price；有 price 的是票（ticket）。
  ⚠️ **归入待确认的理由**（§3.5 误判3，拿不准时先归入）：
  　问 1（改正动作＝按场合挑对那个钱词）成立、问 2（一句话覆盖）成立，
  　但**问 3 存疑** —— 内化了"按场合挑"这个动作，未必就知道 fare 这个词本身，那是词汇量不是规则。
  ★★ **2026-08-22 复习日 §8④a 结清：维持归入，「归入待确认」撤销 —— 但改用新的毕业口径。**
  　 复查证据：**同一天她 fee 那一处命中（组8 tuition fees）、fare 那一处失手（组7 the price of this line）**
  　 ⇒ 两个成员可以独立取值 ⇒ 严格按问 3 该拆。
  　 但拆出来会得到一个只讲 fare 一个词的薄条目，没有练的价值。
  ⇒ **改判为"词表型条目"，另立毕业口径（2026-08-22 教练提出，等她定）**：
  ```
  词表型条目 ＝ 正文是一张"N 选一"的词表（本条 bill/fee/cost/fare；同类还有
  　#0293 四个回报 · #0299 四个超过 · #0305 四个适应 · #0308 四个衡量 · #0323 四个稳
  　#0325 不可数清单 · #0307 职场名词块 · #0270 工资一族 · #0269 范围四条路）
  毕业口径：连对 2 次**必须落在不同成员上**，同一个成员对两次不算毕业。
  理由：这类条目的规则只有一句（按场合挑），真正的缺口是**成员覆盖**，
  　　　只测一个成员就毕业＝拿一个词的会，换掉整族的会。
  ```
  　 本条已有的两次 ✅ 分别是 bill（08-20 utility bills）与 fee（08-22 tuition fees）——
  　 **成员不同 ✓**，若不是同日还有 fare 那次 ❌，本可按新口径毕业。
  ⚠️ 归入的代价已记在账上：本条 08-20 刚拿的连对 1 因此归零。
- 2026-08-22 ✅ D4 复习日 C2·组8 第 2 题　**同日先错后对**
  题面「这学期的学费比去年涨了两成」（新写触发点），她写 `**tuition fees** for this semester are…`。
  「学费」＝为某项服务／资格付的钱 ⇒ **fee**，正是本条判据第二行的那一类 ⇒ 命中，连对 1、连错归 0。
  ★ 同一条今天上午在 fare 那一处失手（组 7 第 7 题 `the price of this line`），下午在 fee 这一处命中
  　 ⇒ **她掌握的是"按场合挑"这个动作，缺的是具体某个词（fare）** —— 与归入时问 3 的存疑判断吻合。
  　 收尾复查时按这条证据结清「归入待确认」。

  ### ★ 更正块（§4.7，2026-08-22 当天改判）
  **原判**：组 8 判 ✅ 之后写成 连对 1 ／ 连错 0。
  **新判**：**连对 0 ／ 连错 1**。
  **理由**：组 7（❌ `the price of this line`，fare 那一处）与组 8（✅ tuition fees）**是同一天**，
  　按 §3.2 同日口径 ⇒ 当天净结果是 ❌。教练原来只按最后一次结算，判宽了。
  **这个数住在哪几处**：本条状态行 ／ 本条历史（组 8 那行 ✅ 留痕不删 ＋ 本更正块）／
  　sessions/2026-08-22.md 组 7 与组 8 战报。
  📋 留痕不判：`higher **than last year**` 比较对象不对等（费用比年份），
  　 但 `Sales/Prices/Temperatures are higher than last year.` 三个母语者句造得出 ⇒ §0.8 不判错。
  　 严谨版进更好版：`than **those of** last year`。

## #0265 两个同义说法不要焊在一起
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F03

**问题是什么**
英语里同一个意思常有两个说法，各自都完整。**记混之后取一半拼一半，两边都不成立。**
　❌ `over **than** three days`　　✅ `**over** three days` ／ `**more than** three days`
　❌ `In **actually**`　　　　　　✅ `**in fact**` ／ `**actually**`（这一处记在 #0044）
　❌ `prefer A **than** B`　　　　✅ `prefer A **to** B` ／ `would rather A **than** B`
　❌ `the reason is **because**`　✅ `the reason is **that**` ／ `**because** …`
　❌ `despite **of**`　　　　　　 ✅ `**despite**` ／ `**in spite of**`
**找法**：写出来之后把它拆开看 —— 这半句能不能自己站住？两半各自都站得住，才不是焊接件。
　`over three days` ✅ 站得住　`than three days` ❌ 站不住 ⇒ `over than` 是焊的。
⚠️ **与 #0044 的关系**（2026-08-19 判过，没合并）：
　#0044 讲的是 in fact ＋ actually 这**一对**；本条讲的是"焊接"这个**机制**。
　按 §3.5 三问，问 3 不成立 —— 掌握了 in fact 不会自动让人知道 over 和 more than 是同义的。
　⇒ 暂不合并，两条都留着。**复习日（§8④a）全档 review 时再看**：
　　如果那时已经攒到第三个焊接实例，就把 #0044 并进本条。

**怎么发现的**
2026-08-19　D2 学习日 C2·组3 第 10 题

**我错在哪**
她的：`children who has a fever **for over than three days**`
正确：`for **more than** three days` ／ `for **over** three days`

**中文触发点**
- 2026-08-20 **题面加死**：这个项目拖了不止半年，可能快一年了。
这个项目拖了不止半年。

### 历史记录
- 2026-08-19 ❌ D2 学习日 C2·组3 第 10 题（顺带）
  查重（§3.5 B0）：grep 了 `more than`、`over than`、「超过」，命中 #0246（倍数 -fold）——
  那条讲的是倍数表达的歧义，不是焊接，问 1、问 2 都不成立。
  与 #0044（In actually → In fact）的三问逐条写在上面「问题是什么」里：问 3 不成立 ⇒ 暂不合并。
- 2026-08-20 ◎− D3 学习日 C2·组2 第 7 题　**题面不够死，两边都不动**
  题面「这个项目拖了不止半年」，她写 `the project has been delayed **for half a year**`。
  「不止」这一层整块没进英文 ⇒ 本条要抓的 `over than` / `more than` 根本没机会出场。
  判 ◎− 不判 ◎✅：她的答案**不符合题面**（漏了「不止」），所以拿不到"算对"；
  但也不记 ❌ —— 本条的错（把两个同义说法焊在一起）她一次都没犯。两边都不动。
  丢「不止」那一层按 #0126 记（★靶子1）。
  ★ 题面的毛病：「不止」是个轻声的修饰词，丢掉之后句子照样通顺，
  　 所以它不构成"绕不过去"的约束。⇒ 加死成
  　 「**这个项目拖了不止半年，可能快一年了。**」—— 后半句让"半年"这个数字站不住，
  　 不写 more than 整句就自相矛盾。
  `half a year` 本身不判错，但英文更常说 `six months` ⇒ 进更好版。
- 2026-08-22 ✅ D4 复习日 C2·组9 第 2 题
  题面「参加这次培训的人超过两百。（★「超过」只能用一个说法，别把两个焊在一起）」（新写触发点），
  她写 `**Over** two hundred people are attending this training`。
  over 单用，没有焊成 `over than` ⇒ 命中，连对 1、连错归 0。
  📋 更好：`**More than** two hundred people are **taking part in** this training.`
  　（两个都对，但书面文里 more than 更常见；attend 偏"出席"，参加培训用 take part in）

---

# F04 单复数/主谓一致

> 含长主语后谓语被拉走、不可数名词

## #0048 该用复数的名词写成了单数
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F04

**问题是什么**
泛指、或中文明说"那些/大多数/很多"时，英文名词要用复数。
她漏的不是规则本身（低压孤立测能产出复数），是写的时候没顾上。

**怎么发现的**
2026-08-11　迷你复习

**我错在哪**
累计实例：
· `the **challenge** caused by` → `the challenges`
· `most employees or **worker**` → `workers`
· `**grandparent** / **young parent**` → `grandparents / young parents`
· `their **business** tend to be` → `their businesses tend to be`
**找法**：中文有"那些/很多/大多数/们"的地方，英文名词先默认复数。

**中文触发点**
- 2026-08-20　房租不含水电费，得另外交。
- 2026-08-19　大多数小企业都撑不过头三年。
- （更早）**老龄化带来的那些挑战不容忽视**（08-18 题面补完整句：原「老龄化带来的那些挑战」是光杆 NP，她必须自己补谓语才能答 —— 她 08-18 定「我是根据题面回答问题」，残题面逼她造句、造出来的部分又不是考点，两头不讨好）

### 历史记录
- 2026-08-11 ✅ 迷你复习
- 2026-08-13 ✅ 迷你复习
- 2026-08-15 ✅ D5 学习日
- 2026-08-16 ✅ 复习日 C1·组9　（当日 4 条，按最后一次记）
- 2026-08-18 ❌ D1 学习日 C2·组2　（当日 2 条，按最后一次记）
  ⚠️ 已并入 #0050 #0052 #0054 的历史
- 2026-08-19 ✅ D2 学习日 C2·组1 第 5 题　★靶子2
  题面换成「大多数小企业都撑不过头三年」，她写 `most small **corporations**`。
  中文「大多数」→ 英文名词复数，一次到位。⇒ 连对 1（毕业线仍 3，08-18 那次 ❌ 已经把线抬到 3）。
  同句另三处，都不属于本条：
  · `corporations` → 更好 `businesses / firms`（见 #0258）
  · `cannot live` → `do not survive`（见 #0250）
  · 丢了「头」first（记在 #0126）
  ★ 值得记一笔：08-18 判 ❌ 的当天她在同一组里也有写对的，今天单点又对了 ——
  这一条低压几乎必对，真正的检验只能在限时作文里（与 #0068 的诊断一致）。
- 2026-08-20 ❌ D3 学习日 C2·组1　（当日 2 次：第 2 题 △ → 第 4 题 ❌，按最后一次记）　★靶子2
  **第 4 题 ❌**：`doesn't include **ultility bill**` —— 泛指一类账单要用复数 `utility **bills**`。
  光杆可数单数，前面既没有冠词也没有 -s。#0249 的正文里已经写死了这一句
  「两项东西（水＋电）配单数对不上，bills 要复数」，08-19 教过，隔一天原样漏。
  **第 2 题 △**：`focuses on **the low-income household**` —— 中文「低收入家庭」是泛指一类，
  英文自然写法是 `low-income **households**`（零冠词＋复数）。
  但 `the low-income household` 作为社科文体的"类指单数"能造出母语者句子（§0.8）
  ⇒ 按 §5 四问自审第 ④ 问判为 **⚠️不地道，不是真错**，记 △ 不推进 streak。
  ⇒ 连对归 0、连错 1，毕业线保持 3。
- 2026-08-20 　作文 T2-17　**留痕，不重复推进**
  作文里与"数"有关的失手只有一处：S17 `these **cost**`，已按主错记在 #0055（限定词与名词数不一致）。
  本条的考点（泛指该用复数的名词写成单数）在这篇里**零出现**：
  `losses` `costs` `risks` `rewards` `problems` `choices` `jobs` 全部正确使用复数。
  ⇒ 不重复计，不推进 streak（本条今天的净结果已由组1 第 4 题的 ❌ 定下）。
- 2026-08-22 ✅ D4 复习日 C2·组3 第 8 题
  题面「这两种做法各有各的代价，只是代价出现的时间不一样」，她写
  `both methods have their own cost是, but **those costs** show up at different times`。
  第二处 `costs` 无歧义地用了复数；第一处 `cost是` 是中文输入法误触（非词）⇒ 手滑豁免，
  从上下文看她要的就是 costs ⇒ 判命中，连对 1、连错归 0。
  📋 顺带用对：`both methods **have**` · `those costs **show**` 两处主谓也对。
  📋 更好：`Both **approaches carry a cost**; the difference is **when** that cost shows up.`
  　（carry ＋ 抽象名词 ＝ #0292；后半改成 when 从句，免掉第二次说 costs）
- 2026-08-23 ❌ D1 学习日 C3·组4 第 7 题（顺带）　连对 1 → 0、连错 1
  主考点是 #0314。她写 `… while **house** in small county towns **are** becoming increasingly difficult to sell`。
  中文「小县城的房子」泛指一类 ⇒ 英文必须复数 `**houses**`；而且她自己的谓语写的是 **are**，
  ⇒ **她心里想的就是复数，落到纸上少了一个 s** ——这正是本条 08-11 起反复出现的形状。
  正确：`**houses** in small county towns are becoming …`。
  ★ 与今天同一句里的另一处对照：`rents … goes up` 的 **rent** 是不可数，她没有乱加 s ⇒ 那一处是对的。
  　 ⇒ 不是"名词一律加 s"式的乱猜，是**该加的那个漏了**。
  ⚠️ 同一处也在 `reminders.md` **R2**（名词与主谓的 -s）的扫描范围内 ——
  　 本行与 R2 记的是**同一个实例**，不重复计两次（#0048 是否该按 #0322 移出复习池，
  　 08-22 她说"先不动"，教练不自行处置）。
  📋 更好：`**Rents** in big cities rise year after year, while **houses** in small county towns
  　 are becoming harder and harder to sell.`（`house rent` 不是英式主流说法，`rents` 一个词就够）
<details><summary>原始行（旧表逐字，旧号 E-002）</summary>

`**老龄化带来的那些挑战不容忽视**（08-18 题面补完整句：原「老龄化带来的那些挑战」是光杆 NP，她必须自己补谓语才能答 —— 她 08-18 定「我是根据题面回答问题」，残题面逼她造句、造出来的部分又不是考点，两头不讨好）|the **challenge** caused by|the **challenges** caused by|P4 单复数|**R（08-11 探针实测坐实）**：低压孤立答 `an aging population brings these challenges` —— 复数产得出 ⇒ 检索失败不是知识缺口 · 挂代号 **P4**|**1/3 · ✅D—迷你复习**|`

</details>

## #0053 「no 后面可以接复数么」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
K　0/3 抽查

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：—（08-13 改判**留痕**：`have no X` 与 `don't have X` 是自由变体，中文无法区分 ⇒ 没有哪句中文能逼出 `no`。她问的是**用法知识**不是**产出考点**。08-15 回写文件）
正确：能，单/复/不可数都合法，看语义：预期本来只有一个→单数（`no husband`）；预期本来有多个→复数（`no children`）。★ 但 `no choice but to` 是**固定块，永远单数**

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— 08-13 已改判留痕：`have no X` 与 `don't have X`
是自由变体，**没有哪句中文能逼出 no**。她问的是用法知识，不是产出考点。
（旧留痕：「no 后面可以接复数么」—— 能，单/复/不可数都合法看语义；但 `no choice but to` 永远单数）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-053）</summary>

`「no 后面可以接复数么」|—（08-13 改判**留痕**：`have no X` 与 `don't have X` 是自由变体，中文无法区分 ⇒ 没有哪句中文能逼出 `no`。她问的是**用法知识**不是**产出考点**。08-15 回写文件）|能，单/复/不可数都合法，看语义：预期本来只有一个→单数（`no husband`）；预期本来有多个→复数（`no children`）。★ 但 `no choice but to` 是**固定块，永远单数**|**K**|0/3 抽查|`

</details>

## #0055 主语与谓语的数不一致（主语紧挨谓语）
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F04

**问题是什么**
谓语没跟着主语的数走。**主语就在谓语旁边、不隔长短语**的那一类。
她低压下能做对，压力下不稳定 —— 08-16 同一天里同一个结构先对后错过。
⚠️ 与「长主语被中间的名词拉走」不是同一条：那一类举得出"简单主谓对了、长主语错了"的实例，可独立取值。

**怎么发现的**
2026-08-13　迷你复习

**我错在哪**
累计实例：
· `why they **works**` → `why they work`（复数主语配了单数动词）
· `an aging population **put**` → `puts`（三单漏 s）
· `some patients **hasn't**` → `haven't`
· `These data **shows**` → `These data show` ／ `This data shows`（不能混）
· `The tables **illustrates**` → `The tables illustrate`
· `China **build**` → `China **has built**`（三单 ＋ 中文"了"要完成时，两层叠在一个光杆原形上）
**找法**：每个谓语都问一次"它的主语是谁、是单还是复"。

**中文触发点**
- 2026-08-19　这家公司这些年建了三座新工厂。
- （更早）没人说得清它们为什么偶尔管用

### 历史记录
- 2026-08-13 ✅ 迷你复习
- 2026-08-16 ✅ 复习日 C1·组7　（当日 2 条，按最后一次记）
- 2026-08-18 ❌ D1 学习日 C2·组8　（当日 3 条，按最后一次记）
  ⚠️ 已并入 #0063 #0066 #0067 #0081 #0240 的历史
- 2026-08-19 ❌ D2 学习日 C2　★靶子2　（当日 2 次：组2 ✅ → 组3 ❌，按 §3.2 只按最后一次记）
  ★★ **本条今天拿到了全天最有诊断价值的一组对照，两次写在下面：**
  【组3 第 10 题 ❌ ← 净结果】「孩子发烧超过三天就该送医院」
  　她写 `**children who has** a fever…`。先行词 children 是复数，从句谓语跟着写了 has。
  　正确：`children who **have** a fever` ／ 更省：`a child with a fever lasting more than three days`。
  【组2 第 1 题 ✅】「这家公司这些年建了三座新工厂」
  　她写 `the company **has built** three factories in recent years` ——
  　三单 ＋ 完成时两层同时对，这是本条累计实例里最难的形状（对应 `China build → China has built`）。
  ⇒ **单点、句子短的时候必对；句子一长（先行词 + 关系从句 + 时间状语）就掉线。**
  这与 #0068 的诊断完全一致：不是知识缺口，是注意力被别的东西占住时基础项掉线。
  ⇒ 结论同 #0068：**这一条不该再做单点 drill**，只能在限时作文里验。
  📋 组2 那次的留痕（漏掉「新」、`complany` 手滑）见 #0126 与 §3.2 手滑豁免，判定不受影响。
  题面「这家公司这些年建了三座新工厂」——**故意把三单和"了"叠在一个动词上**
  （对应累计实例里的 `China build → China has built`）。
  她写 `the company **has built** three factories in recent years`：三单 ✅、完成时 ✅，两层同时对。
  ⇒ 连对 1（毕业线仍 3）。
  📋 留痕：她漏掉了「新」（three factories 而不是 three new factories）。
  **判定：不算 #0126。** 判据 —— #0126 记的是"删掉那一层意思就变了"的修饰；
  `build a factory` 本身已含新建义，`three factories` 与 `three new factories` 传达的事实相同。
  这条边界已写进 #0126：**删掉后意思变了才算丢，删掉后意思不变的冗余修饰不算。**
  📋 `complany` 按 §3.2 手滑豁免（拼成的不是另一个真词）。
- 2026-08-20 ◎ D3 学习日 C2·组1 第 2 题　★靶子2　**教练出题错误，不是她的问题**
  `the report **focus** on` 缺三单 -s，本来要按本条记 ❌。
  但同一处的成因是教练把词元 `focus` 写进了括号、她照搬（详见 #0096 的 08-20 记录，她当场裁定"不算错"）
  ⇒ 与 #0096 一起判 ◎，不记 ❌，不推进 streak。
  ★ 同组另有两处**顺带用对**（列出，按本场口径不推进 streak）：
  　第 4 题 `the house rent **doesn't** include` · 第 7 题 `the process only **takes**`
  　两处都是主语紧挨谓语的最短形状，三单都对。
  ⇒ 今天本条**没有可判的真数据**：唯一一次"错"是题面造成的，两次"对"是顺带。
  　 按 §7，靶子2 只能在限时 cold 作文里清零 —— 今天的作文才是它第一次真正上称。
- 2026-08-20 ✅ D3 学习日 C2·组3 第 7 题　★★★ 靶子2 在最难的形状上守住了
  新题面故意做成**长主语**：「这些工厂每年排放的废水总量仍在上升」。
  她写 `the total **amout** of waste discharged from these factories **is** still growing`。
  中心词 `amount` 是单数、被一整串修饰隔开、紧挨谓语的是复数 `factories` ——
  这正是 08-19 诊断说她"句子一长就掉线"的那个形状，**她没被拉走，写了 is** ⇒ 考点命中，连对 1。
  ★ 08-19 的假设（不是知识缺口，是句子一长就掉线）**今天被证伪了一半**：
  　 长句她守住了，短句（组1 第 2 题 `the report focus`）反而掉了 —— 但那次已判定为教练题面诱发（◎−）。
  　 ⇒ 现有证据不支持"长句必掉"。真正的检验仍然是限时作文（§7）。
  同句两处不属于本条：`waste` 丢了"水"、缺「每年」，都记在 #0126；`amout` 拼写非真词，手滑豁免。
- 2026-08-20 ❌ 作文 T2-17（当日第 2 处出现，与上一行合并为当天一次净结果）　★靶子2
  ⚠️ **上一行组3 记的 ✅ 不撤销、不删**（按 2026-08-21 她定的"两个都记下来"）；
  　 但按同日 streak 口径「当天只要出现过 ❌ 就记 ❌」，**本条今天的净结果是 ❌**：
  　 连对由 1 归 0。
  　 ⚠️ **连错 2026-08-20 收尾 C1 校验时更正为 3**（原写 1，是错判）：
  　 　 08-18 ❌ · 08-19 ❌ · 08-20 净 ❌ ⇒ **连续三天都是错，连错 3**。
  　 　 原来写 1 的理由是"组3 刚 ✅ 过所以从头数"，但组3 那次 ✅ 与作文这次 ❌ **同属 08-20 一天**，
  　 　 按 2026-08-21 她定的同日口径当天只算一次、且有 ❌ 就记 ❌ ⇒ 不存在"中间断过"。
  作文里 4 处对、2 处错：
  　✅ S10 `a certificate that anyone can get **offers** no real advantage`（名词＋关系从句＋三单，全档最难形状）
  　✅ S9 `walking it **yields**` ／ S15 `what **pushes**` ／ S1 `Whether… **has** long been`
  　❌ S2 `the **reward** it yields **are** far greater` —— 单数主语配复数动词
  　❌ S17 `drive these **cost** down` —— 限定词 these 与单数名词不一致
  ★★ **08-19 的假设今天被彻底证伪，而且是反过来的**：
  　 当时的结论是"句子一长就掉线"。作文里**四处对的全是长主语/复杂结构**，
  　 **两处错的全是主谓中间只隔一两个词的短句**。
  　 ⇒ 真实机制不是"长了就掉"，是 **长句她会警觉、会盯；短句她不设防。**
  　 ⇒ 下一篇的装备要改成"短句也要盯"，不是"长主语要盖住 of 短语"。
  ⇒ 按 §7 靶子2 **未清零**，继续挂到下一篇。
- 2026-08-22 ❌ D4 复习日 C2·组2 第 3 题（顺带）　连错 4
  她写 `these therapies only **works** occasionally`。主语复数、谓语就紧挨在后面，还是掉了。
  ★★ **今天两组合看的形状很清楚**：
  ```
  组1  三处主谓全对，其中两处是难的     the population aged 60 and over **has**
                                        Whether to allow … to school **has**
                                        these choices **push**
  组2  三处对（has dropped / gambled / want），错的是【最短的那个从句】：
       these therapies only works —— 主语和谓语中间一个词都没有
  ```
  ⇒ 与 08-20 作文的结论完全一致：**长主语她会盯，短的不设防。**
  ⇒ 已同步挂进 reminders.md **R2**（她 08-22 说这一类靠提醒不靠重复练）。
  ⚠️ 本条是否也比照 #0322 移出复习池，等她定（reminders.md R2 里写了甲／乙两条路）。
- 2026-08-22 ✅ D4 复习日 C2·组7 第 3 题　**判 ✅ 但不推进 streak**
  题面「这几条规定只适用于新员工」，她写 `these rules **only apply** to new staff`。
  ★★ **正是组 2 失手的那个形状**（`these therapies only works` —— 主语复数、谓语紧挨、中间夹一个 only），
  　 今天原样修好，而且 `new staff` 也没写成 staffs（#0325）。
  ⚠️ 按 §3.2 同日口径「当天只推进一次、出现过 ❌ 就记 ❌」：
  　 本条今天的净结果已由组 2 的 ❌ 定下 ⇒ **本行只留证据，连对 0／连错 4 维持不变**。
  ★ 但这条证据本身有价值：同一天里 ❌ → ✅，说明**当场讲过就能改**，
  　 缺的是压力下的自动化，不是规则。这与 reminders.md R2 的判断一致。
- 2026-08-23 ✅ D1 学习日 C3·组2 第 1 题　**连错 4 归零，本条第一次拿到干净的正面测量**
  题面「这项新出台的政府补贴每年为几十万农户省下一大笔开支。（★ 谓语的数必须跟住主语 ——
  写完回头数一次）」——★ 陷阱设计：主语 `this new government subsidy` 是**单数**，
  但它前面挂了三个修饰词、后面紧跟的宾语 `hundreds of thousands of farmers` 是**复数**，
  最容易被后面那串复数拉走。
  她写 `this new government subsidy **saves** hundreds of thousands of farmers a large amount
  of money each year`。
  ★ 三单 -s 在、没被后面的复数宾语拉走 ⇒ 命中，连对 1、**连错 4 归 0**。
  ★★ 本条的连错 4 是全档并列最高（与 #0126 并列）。它第一次转正，靶子2 拿到关键证据。
  ⚠️ 但按 §7 口径：**复习组答对不算清零**，靶子2 仍要在一篇限时 cold 作文里零失守才摘。
  📋 更好：`This new government subsidy saves hundreds of thousands of farmers **a large sum**
  　every year.`（`a large amount of money` 五个词 → `a large sum` 三个词，书面更紧）
<details><summary>原始行（旧表逐字，旧号 E-068）</summary>

`没人说得清它们为什么偶尔管用|why they **works**|why they **work**|P4 主谓一致（复数主语配单数动词）|R · **P4**|0/3|`

</details>

## #0057 without a fluent language … find jobs → the language barrier … finding a job
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F04

**问题是什么**
P11 硬编＋P4 数 → P11 硬编（08-16 更正：合并组里 P4「find jobs」那一半是教练假错，已随 E-130 撤销；本条真错只有 without a fluent language→the language barrier）　R · P11

**怎么发现的**
2026-08-16　复习日 C1·组5

**我错在哪**
她的：**without a fluent language** … find **jobs**
正确：the **language barrier** … **finding a job**

**中文触发点**
加上语言障碍，找工作更难

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组5

<details><summary>原始行（旧表逐字，旧号 E-086）</summary>

`加上语言障碍，找工作更难|**without a fluent language** … find **jobs**|the **language barrier** … **finding a job**|~~P11 硬编＋P4 数~~ → **P11 硬编（08-16 更正：合并组里 P4「find jobs」那一半是教练假错，已随 E-130 撤销；本条真错只有 `without a fluent language`→`the language barrier`）**|R · **P11**|0/3|`

</details>

## #0058 「strain 是可数还是不可数」
状态：退池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04
📤 2026-08-22 复习日 §8④a 退池：本条自己在 08-16 就重判为「两种都成立 ⇒ 第②类，不再出题」，
　 留在池里只会占一个永远抽不到的位置。规则本身留档（#0103 的冠词判词已按它订正）。

**问题是什么**
第②类　不再出题

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：这给医疗系统造成很大压力
正确：**08-16 重判为「两种都成立」⇒ 第②类，不再出题**：`put **a** strain on X` 与 `put strain on X`（不可数）**都是标准英语**——教练自己在 E-087 的目标版里写的就是 `put **further strain** on`，无冠词。原记法"默认带 a"**过度指定，会生产假错**。<br>仍成立的部分：加 further/more 时 a 掉 ／ `under strain` 零冠词 ／ `the strains of modern life`＝多种压力 ／ 判据「光杆抽象名词看有没有'一份/一次'的意思」<br>⛔ **08-16 拟记的"顺带 ✅"已撤销**（评审指出：不能靠一个本身可能错的规则发毕业证。注：来源已核，`puts a financial strain on` 确为**她**第 3 组的产出，非教练示范；撤销的理由是规则过度指定，不是来源问题）

**中文触发点**
**「strain 是可数还是不可数」**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-102）</summary>

`**「strain 是可数还是不可数」**|这给医疗系统造成很大压力|**08-16 重判为「两种都成立」⇒ 第②类，不再出题**：`put **a** strain on X` 与 `put strain on X`（不可数）**都是标准英语**——教练自己在 E-087 的目标版里写的就是 `put **further strain** on`，无冠词。原记法"默认带 a"**过度指定，会生产假错**。<br>仍成立的部分：加 further/more 时 a 掉 ／ `under strain` 零冠词 ／ `the strains of modern life`＝多种压力 ／ 判据「光杆抽象名词看有没有'一份/一次'的意思」<br>⛔ **08-16 拟记的"顺带 ✅"已撤销**（评审指出：不能靠一个本身可能错的规则发毕业证。注：来源已核，`puts a financial strain on` 确为**她**第 3 组的产出，非教练示范；撤销的理由是规则过度指定，不是来源问题）|第②类|不再出题|`

</details>

## #0059 不可数名词一族：不加 -s、不加 a、配单数谓语（含 advice ↔ advise 的名词/动词分工）
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F04
🔗 2026-08-22 **#0325 已并入本条**（她定：「#0325 可以合并」）
⚠️ 2026-08-23 教练一度把组2 的 `works` 判进本条并翻转当天结果 ——
　 **她指出那是 `workers` 的打错 ⇒ 与不可数性无关 ⇒ 该判定已撤销**，当天结果回到 ✅（见历史）。

**问题是什么**
这一批名词在中文里都能说"一条／几条"，在英语里**一律不可数**：
```
advice        建议    `he **advises** us` ／ `**some advice**` ⛔ ~~three advice~~ ~~advices~~
evidence      证据    `The **evidence is** overwhelming.` ⛔ ~~evidences~~ ~~an evidence~~
information   信息    `for further **information**`
research      研究    `**research shows** that…` ⛔ ~~researches~~
equipment 设备 · knowledge 知识 · progress 进展 · feedback 反馈 · furniture 家具
staff 员工（集合，英式配复数；`staff members` 才可数）
work          工作    `**work** is scarce` ⛔ ~~three works~~（works ＝ 作品／工程）
              ⇒ 要说可数的"一份工作／岗位"必须换词：**a job** ／ **jobs** ／ **positions**
              ⚠️ 2026-08-23 补入，但**暂无她的实例**（那天的 `works` 是 `workers` 的打错，
                 已按她的指正撤销 ⇒ 见本条 08-23 的更正块）。规则保留，等真实例。
```
**要说"一条／几条" ⇒ 用量词把它变可数**：
```
a **piece of** advice / evidence / information ／ **three pieces of** advice
a **piece of** research ／ 换可数的 **a study**　·　**an item of** furniture
**a great deal of / a large amount of** ＋ 不可数　⛔ 不能用 many / a number of / 数词
```
**同一个概念的名词↔动词分工**（本条原始来源）：
```
名词 advice（不可数）  ↔  动词 advise（拼写是 s 不是 c）
名词 practice          ↔  动词 practise（英式）
名词 licence           ↔  动词 license（英式）
```
**判据**：写完一个抽象名词，问「能不能说 **one X**」——
不能说 one advice / one evidence ⇒ 不加 -s、不加 a、不配数词、谓语用单数。
⚠️ 最容易串的三组：evidence↔a fact · research↔a study · advice↔a suggestion（选词见 #0181）

★★ **出题纪律（2026-08-22 她定，SKILL §6 已同步写死）**
```
⛔ **不许出只考一个词的句子。** 一道题必须让**两个以上成员**同时落地。
理由（她的原话）：「注意每次出题不要出一个单词，避免错的是另一个，还在反复考同一个。」
⇒ 本条历史已经吃过这个亏：08-15／08-16／08-18 三次全在测 advise（动词半边），
　 08-20 第一次把数词逼到 advice 前面，名词半边立刻塌 —— 之前的 🎓 是虚的。
```

**怎么发现的**
2026-08-15　D5 学习日

**我错在哪**
她的：he **advices** us
正确：he **advises** us（advice 名词不可数／advise 动词）

**中文触发点**
- 2026-08-22（合并后的多成员题面，下次用）　警方掌握的**证据**不多，但他们给了我们几条**建议**，
  并且**建议**我们先别对外说。（★ 一句里三处：证据不可数 · "几条建议"要量词 · 第二个"建议"是动词）
- 2026-08-20　他在会上提出了三条建议。（★ 这次是**名词**半边翻的车：「三条建议」逼出数词＋advice）
他建议我们…（08-16 题面**二次**加死：**他给了我们一些建议，劝我们早点出发**。★ 只写「他建议我们早点出发」不够——「建议」同时通向 advise/suggest/recommend，她写 He suggested we leave earlier 完全正确、advice/advise 的区分**一次都没被行使**；而本条是全库唯一"被清零"条目（08-13、08-15 两次都错），不能把命押在她碰巧选哪个词上。新题面前半「**一些建议**」强制不可数名词、后半「**劝…做某事**」把动词推向 advise ⇒ 即使动词半边被 suggest 逃掉，名词半边仍必然落地）

### 历史记录
- 2026-08-15 ❌ D5 学习日
- 2026-08-16 ✅ 复习日 C1·组10（当日 2 次，取最后一次）
- 2026-08-18 ✅ D1 学习日 C2·组5
- 2026-08-20 ❌ D3 学习日 C2·组3 第 2 题（顺带）　**🎓 复发，回池**
  她写 `he proposed **three advice** at the meeting`。
  advice 不可数，数不了 ⇒ `three **pieces of** advice` ／ 直接换可数词 `three **suggestions**`。
  ★ 这条 08-18 刚 🎓（连对 2），隔一个学习日复发。按 §3.3：状态改回在池、连对归零、毕业线仍是 2。
  ★ 值得注意的是**翻车的是名词半边**：08-16 那次题面加死时就写过
  　「前半"一些建议"强制不可数名词、后半"劝…做某事"把动词推向 advise」——
  　 之前两次 ✅ 都是动词半边（advise/advices），名词半边一次都没被真正测到。
  　 今天「三条建议」第一次把数词逼到 advice 前面，名词半边立刻塌了。
  　 ⇒ 这条以前的两次 ✅ 是**半个考点的 ✅**，档案里的 🎓 是虚的。

### ★ 合并块（§3.5 C4，2026-08-22 她定「#0325 可以合并」）

```
被并编号  #0325（英语里不可数的那批常见名词，2026-08-22 建号）
保留编号  #0059（更早）
历史处置  #0325 的三行 08-22 记录已按日期插进本条历史，逐字保留
streak 重算（合并后按 §3.2 同日口径逐日算）
  08-15 ❌ → 连错 1
  08-16 ✅ → 连对 1
  08-18 ✅ → 连对 2
  08-20 ❌ → 连错 1
  08-22 当天：#0059 ✅ ＋ #0325 建号 ❌ ＋ #0325 ✅ ⇒ **有 ❌ ⇒ 当天记 ❌** → 连错 2
⇒ 合并后状态：**在池 ｜ 连对 0 ｜ 连错 2**
⚠️ 合并的代价已记在账上：合并前 #0059 是 连对 1、#0325 是 连错 1；
　 合并后 08-22 这一天因为含 #0325 的建号 ❌ 而整体记 ❌，所以 #0059 的连对 1 归零。
　 这是同日口径的必然结果，不是判宽或判严。
```
  ⇒ 新触发点记在上面：「他在会上提出了三条建议」，专打名词半边。
- 2026-08-22 ❌ D4 复习日 C2·组4 第 10 题（顺带）　〔原 #0325 建号行，2026-08-22 并入〕
  她写 `even though the **evidents are** solid` ⇒ 要的是 `the **evidence is** solid`。
  evidence 不可数：① 不加 -s（而且 evidents 根本不是词）② 谓语配单数 is。
- 2026-08-22 ✅ D4 复习日 C2·组6 第 2 题　〔原 #0325 行，2026-08-22 并入〕
  她写 `The police have abundent **evidence**, but **none of it points** directly to him`——
  不加 -s ✅ ／ 回指用 it ✅ ／ 谓语单数 points ✅，三层全对。
  ⚠️ 但当天上午刚讲过，属"刚教完就测"，成色要打折。
- 2026-08-22 ✅ D4 复习日 C2·组9 第 10 题（原 #0325 顺带用对，不推进）
  `data found online is not necessarily reliable` —— data 那一处按 §0.8 不判，此行只留痕。
- 2026-08-22 ✅ D4 复习日 C2·组8 第 3 题　**★ 积压① 的第一条整改，一次通过**
  新题面（**双半式**）「医生给的建议不多，但他建议我们再观察几天。
  　（★ 前半的「建议」是名词、后半的是动词；名词那个不可数）」，她写
  `the doctor gave **little advice**, but he **advised us to** observe the situation for a few more days`。
  ★★ **两个考点在同一句里都落地**：
  ```
  名词半边  `little advice` —— 不可数量词，没写成 a few advices / three advices
  动词半边  `advised us to do` —— 拼写与框架都对，没退回 advice 也没被 suggest 逃掉
  ```
  ⇒ 命中，连对 1、连错归 0。**这是本条 08-13 被清零以来第一次两半同时行使。**
  ★★ 出题写法留档（可套用到其余"一条挂两个考点"的条目）：
  　 **把两个考点写成中文句子的两个半句，各自加一句结构点名**，一句里都得落地，不能只对一半过关。
  　 待照此整改的：#0080（数 ＋ 机构零冠词）· #0278（proactive ＋ reactive）· #0251（this kind of 两个方向）。
  📋 顺带用对 #0125：`a **few more** days` —— 组 4 她写的是 `another days`，
  　 我当时给的更好版正是 `a few more days`，**同一天下午原样用上了**。
- 2026-08-23 ✅ D1 学习日 C3·组1 第 5 题　**用的是 08-22 存好的「下次用」多成员题面**
  题面「警方掌握的证据不多，但他们给了我们几条建议，并且建议我们先别对外说。
  （★ 一句里三处都要落地：证据 · "几条建议" · 第二个"建议"是动词）」
  她写 `the police **have little evidence**, but they gave us **some advice**（原文手滑写作 adivce）
  and **advised** us to keep it quiet for now`。
  ★ 三处逐格核对：
  ```
  evidence   不加 -s、配不可数限定词 little        ✅
  advice     不加 -s、不加 a、不配数词             ✅
  advise     动词，拼 s 不拼 c，过去式 advised      ✅
  ```
  ⇒ 三个成员同时落地（§3.5 词表型出题要求满足）⇒ 命中，连对 1、连错 2 归 0。
  ⚠️ `adivce` 是**非词**（字母顺序颠倒），按 §3.2 复习组手滑豁免 **不记**；
  　 本条真正要防的 `advices` / `three advice` / 名词写成 advise 一个都没出现。
  ⚠️ **子考点仍未被行使**：「几条」她用 `some` 绕过去了，量词 `pieces of` 一次都没出场。
  　 §6 处置 ⇒ **当场改题面**，把「几条」换成**明确数词**（some 挡不住数词）：
  　 **存好的新题面**：**警方只掌握两条证据，但他们给了我们三条建议，并且建议我们先别对外说。**
  　 （★ 三处都要落地：「两条证据」· 「三条建议」· 第二个"建议"是动词。
  　 　 ⇒ 数词直接压在不可数名词前面，必须用量词才写得出来）
  📋 顺带用对：`the police **have**`（police 是集合名词，配复数谓语，正确）·
  　 `keep it quiet for now` 很地道。
- 2026-08-23 ❌ D1 学习日 C3·组2 第 9 题（顺带）　⚠️ **本条已于 2026-08-23 当天撤销，见下方更正块**
  主考点是 #0303。她写 `whether AI would replace **a large number of works**`。
  ★ 中文是"**岗位**"。两层错叠在一起：
  ```
  ① work 表"工作"是**不可数** ⇒ 不能加 -s、不能配 a large number of
  ② works（复数）是另一个词：**作品／工程**（the complete works of Shakespeare / public works）
  ⇒ 想说可数的"岗位"必须换词：**jobs** ／ **positions**
  ```
  ⇒ 正是本条正文的机制（"这批名词中文能说'几个'，英语一律不可数；要可数就换词"，
  　 与 `research → a study` 同一条路）⇒ 成员表已补入 **work**。
  ⚠️ **同日结算（§3.2）**：本条今天组1 第 5 题判 ✅（evidence / advice / advised 三处全对），
  　 组2 第 9 题判 ❌ ⇒ **当天只要出现过 ❌ 就记 ❌** ⇒ 当天净结果 ❌，
  　 **连对 1 → 0、连错 0 → 1**。组1 那行 ✅ 留痕不删。
  ★★ 这次是**主动跑同日口径**跑出来的：08-22 教练在这一条上漏跑过 3 处（当天 §4.7 改判 3 次），
  　 今天在同一条目上第一次当场接住。
  ★ 读出来的一件事：组1 测的三个成员（evidence / advice / advise）她全对，
  　 组2 一个**没在成员表里**的 work 立刻塌 ⇒ **词表型条目的真实水平由"没测过的成员"决定**，
  　 这正是她 08-23 定"出题直接点名成员 ＋ 记成员出题账"的理由。
  📋 最小修改：`whether AI will replace a large number of **jobs**`

  ### ★ 更正块（§4.7，2026-08-23 当天撤销）
  **她的原话**：「**9 我是打错了，明显应该用 workers**」
  **原判**：把 `works` 读成"她把不可数的 work 可数化了" ⇒ 判本条 ❌，
  　并按同日口径把本条当天的净结果从 ✅ 翻转为 ❌（连对 1 → 0）。
  **新判**：**该判定整条撤销。本条当天净结果回到 ✅，连对 1 ／ 连错 0。**
  **判据哪里套宽了**：我在两个可能的读法里**挑了对她更不利的那个，而且没问她**。
  ```
  读法A（我用的）  works ＝ work（不可数）被加了 -s  ⇒ 归 #0059
  读法B（她说的）  works ＝ workers 漏打了 er        ⇒ 与不可数性完全无关
  ★ 读法B 明显更合理，我自己本来就有证据：#0095 的累计实例表里**第四行就写着**
    「· `**works**` → `workers`」—— 08-11 她犯过一模一样的一对。
    我在建立本条判定时**没有回头查 #0095 的实例表**。
  ⇒ §3.2 有一条现成的处置我没用：「❌ 与 ◎ 分不清时**当场问她**。⛔ 不许猜。」
    读法歧义同理 —— 拿不准她写的是哪个词，应该问，不许替她选一个更差的。
  ```
  ⇒ 本条 08-23 只剩组1 第 5 题那一次 ✅（evidence / advice / advised 三处全落地），
  　 当天净结果 ✅，连对 1。**成员表里补入的 work 那一行保留** —— 规则本身是对的，
  　 只是今天没有实例支撑它，标注为"暂无实例"。
  📋 那个 `works` 的正确归属见 **#0095**（拼成另一个真词，work/worker 那一对原样复发）。
<details><summary>原始行（旧表逐字，旧号 E-128）</summary>

`他建议我们…（08-16 题面**二次**加死：**他给了我们一些建议，劝我们早点出发**。★ 只写「他建议我们早点出发」不够——「建议」同时通向 advise/suggest/recommend，她写 He suggested we leave earlier 完全正确、advice/advise 的区分**一次都没被行使**；而本条是全库唯一"被清零"条目（08-13、08-15 两次都错），不能把命押在她碰巧选哪个词上。新题面前半「**一些建议**」强制不可数名词、后半「**劝…做某事**」把动词推向 advise ⇒ 即使动词半边被 suggest 逃掉，名词半边仍必然落地）|he **advices** us|he **advises** us（advice 名词不可数／advise 动词）|P11 词形|R · **P11**|`

</details>

## #0060 the patient … larger hospitals → … a larger hospital（单数病人配单数医院；轻度——数的一致性）
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F04

**问题是什么**
P4 数　R · P4

**怎么发现的**
2026-08-16　复习日 C1·组9

**我错在哪**
她的：the patient … **larger hospitals**
正确：… **a larger hospital**（单数病人配单数医院；轻度——数的一致性）

**中文触发点**
病情严重的话，病人会被转到更大的医院

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组9

<details><summary>原始行（旧表逐字，旧号 E-187）</summary>

`病情严重的话，病人会被转到更大的医院|the patient … **larger hospitals**|… **a larger hospital**（单数病人配单数医院；轻度——数的一致性）|P4 数|R · **P4**|`

</details>

## #0061 「其实我觉得用 the growing number of 更安全」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
K（判据；表达侧记 ✅+ 她的）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：老年人口的增加是主要原因
正确：**✅+ 她比教练的条目原版更准，理由可推广**：`increase in` 后面接的应该是**量**，不是**人**。`increase in older people` 严格说是"老年人自身在变大"。两条严谨写法：**the growing number of older people** ／ **the increase in the number of older people**。★★ 这正是 08-15 那张 **T1 主谓配对表** 的同一条规则（数字/量 vs 人 不能混）在名词块侧的样子——她自己迁移过来的

**中文触发点**
老年人口数量的增加是主要原因。（★ 让 increase 后面接的是"量"，不是"人"）
（旧留痕：「其实我觉得用 the growing number of 更安全」—— 她比教练原版更准，
　两条严谨写法：the growing number of older people ／ the increase in the number of older people）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-195）</summary>

`「其实我觉得用 **the growing number of** 更安全」|老年人口的增加是主要原因|**✅+ 她比教练的条目原版更准，理由可推广**：`increase in` 后面接的应该是**量**，不是**人**。`increase in older people` 严格说是"老年人自身在变大"。两条严谨写法：**the growing number of older people** ／ **the increase in the number of older people**。★★ 这正是 08-15 那张 **T1 主谓配对表** 的同一条规则（数字/量 vs 人 不能混）在名词块侧的样子——她自己迁移过来的|**K**（判据；表达侧记 ✅+ 她的）|`

</details>

## #0064 雇主和员工的利益并不总是一致
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：employers' **interest** … **that of** employees
正确：employers' **interests** … **those of** employees（"利益"英文默认复数 interests；单数 interest 偏"兴趣/关切"。回指词随之变复数）<br>★ **`that of` 这个回指手法是她自发用出来的，Band 7 档，记她名下** ✅+

**中文触发点**
雇主和员工的利益并不总是一致

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-208）</summary>

`雇主和员工的利益并不总是一致|employers' **interest** … **that of** employees|employers' **interests** … **those of** employees（"利益"英文默认复数 interests；单数 interest 偏"兴趣/关切"。回指词随之变复数）<br>★ **`that of` 这个回指手法是她自发用出来的，Band 7 档，记她名下** ✅+|待排序|U（待定）|`

</details>

## #0065 「decline…我要学」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
mark a peak」过宽已撤销——The trend reached its peak ✅ 完全自然，趋势和数值都能 reach/peak；只有 mark 不行（详见 E-242）　K（她点名）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：下降（趋势/数量）
正确：**下降动词四个，按"主语是什么"分**（★ 这是 08-15 T1 主谓配对表的延伸）：<br>`decline` 最通用，正式，量与趋势都能接：the number/proportion/workforce **declined**<br>`fall / drop` 中性，配具体数字最顺：**fell to** 19% ／ **dropped by** 5%（drop 略口语，T1 可用）<br>`shrink` 只配**有体量的整体**：the workforce/population/economy **shrank**（★ 不配 proportion/percentage）<br>`decrease` 正式但偏平，能不用就不用<br>★ 三个搭配一起记：`decline **to** X`（降到）· `decline **by** X`（降了多少）· `a **steady** decline **in** X`（X 的持续下降）<br>★ ⛔ 她 08-15 犯过的反面：趋势不能 `**mark** a peak`（E-165）；数字类主语不能带人当宾语（E-162）<br>🔴 **08-16 更正**：本行原写「趋势不能 reach\

**中文触发点**
这家工厂的用工规模连年缩水，产量也从三万件降到了两万件。（★ "缩水"和"降到"各用一个不同的动词）
（旧留痕：「decline…我要学」—— 本条是词表型，一题必须让 ≥2 个成员落地）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-213）</summary>

`「decline…我要学」|下降（趋势/数量）|**下降动词四个，按"主语是什么"分**（★ 这是 08-15 T1 主谓配对表的延伸）：<br>`decline` 最通用，正式，量与趋势都能接：the number/proportion/workforce **declined**<br>`fall / drop` 中性，配具体数字最顺：**fell to** 19% ／ **dropped by** 5%（drop 略口语，T1 可用）<br>`shrink` 只配**有体量的整体**：the workforce/population/economy **shrank**（★ 不配 proportion/percentage）<br>`decrease` 正式但偏平，能不用就不用<br>★ 三个搭配一起记：`decline **to** X`（降到）· `decline **by** X`（降了多少）· `a **steady** decline **in** X`（X 的持续下降）<br>★ ⛔ 她 08-15 犯过的反面：趋势不能 `**mark** a peak`（E-165）；数字类主语不能带人当宾语（E-162）<br>🔴 **08-16 更正**：本行原写「趋势不能 reach\|mark a peak」**过宽已撤销**——`The trend reached its peak` ✅ 完全自然，趋势和数值都能 reach/peak；**只有 mark 不行**（详见 E-242）|**K**（她点名）|`

</details>

## #0068 ⭐⭐ 注意力单通道，第一次拿到干净数据：本组考点 6/6 全中，同一批句子里考点外错
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
（旧档案未单列，见下方「我错在哪」与原始行）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：留痕（诊断）
正确：

**中文触发点**
⭐⭐ **注意力单通道，第一次拿到干净数据**：本组**考点 6/6 全中**（further＋already 两层 · 现在完成时 · "反而"＋"更好的" · 比较级不用最高级 · 原错 all the world 未复现 · does work 实指语气），**同一批句子里考点外错 5 处，一字未改率 1/6（全天最低：6/10 → 7/8 → 6/10 → 9/10 → 8/10 → **1/6**）**。<br>★★ 最硬的证据：`an aging population **puts**` 在第 3 组写对、`an aging population **put**` 在第 6 组写错，**同一天、同一结构、同一主语** ⇒ **不是知识缺口，是注意力被考点占满时基础项掉线**。<br>★ 这与 CLAUDE.md 的核心诊断（retrieval-under-pressure，非 knowledge gap）完全吻合，也印证 2026-08-11/13 两次"单点测通过 ≠ 装上了"。<br>⇒ **推论（下一个学习日执行）**：单复数/主谓一致**不该再做单点 drill**（她低压必对），只能靠**在真篇里重复到自动化**；而本组这种"多考点同时在场"的题恰好是最接近作文的压力环境，比单点抽查更有诊断价值

⛔ **不出单点题（2026-08-24 定）** —— 本条正文是一段**教练侧的流程观察/统计发现**，
按 §2「教练的流程观察、统计发现、犯规记录不进 problems.md」本来就不该是条目。
迁移进来的存量，**留档不删、不召回**；要不要退池等她定。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-236）</summary>

`⭐⭐ **注意力单通道，第一次拿到干净数据**：本组**考点 6/6 全中**（further＋already 两层 · 现在完成时 · "反而"＋"更好的" · 比较级不用最高级 · 原错 all the world 未复现 · does work 实指语气），**同一批句子里考点外错 5 处，一字未改率 1/6（全天最低：6/10 → 7/8 → 6/10 → 9/10 → 8/10 → **1/6**）**。<br>★★ 最硬的证据：`an aging population **puts**` 在第 3 组写对、`an aging population **put**` 在第 6 组写错，**同一天、同一结构、同一主语** ⇒ **不是知识缺口，是注意力被考点占满时基础项掉线**。<br>★ 这与 CLAUDE.md 的核心诊断（retrieval-under-pressure，非 knowledge gap）完全吻合，也印证 2026-08-11/13 两次"单点测通过 ≠ 装上了"。<br>⇒ **推论（下一个学习日执行）**：单复数/主谓一致**不该再做单点 drill**（她低压必对），只能靠**在真篇里重复到自动化**；而本组这种"多考点同时在场"的题恰好是最接近作文的压力环境，比单点抽查更有诊断价值|留痕（诊断）|`

</details>

## #0071 「有点不太会怎么接句子，早点出发憋了一个 leave early」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
K

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：他给了我们一些建议，劝我们早点出发
正确：★ **这是衔接问题不是词汇问题**（她的核心缺口之一）。三条路，从省到全：<br>① `He **advised** us to leave early.`（一个动词全包，最省）<br>② `He gave us some advice **and urged** us to leave early.`（and 并列两个动作）<br>③ `He gave us some advice, **suggesting** we leave early.`（分词接第二层）<br>★ 她「憋」出的 **leave early 完全正确**（＝set off early／start early）<br>★ 顺带把 advice 用法钉死：**advice 永远不可数**（没有 advices）· `some advice` · `a **piece of** advice` · `advise sb **to do**`

**中文触发点**
老师给了我们一些建议，劝我们提前动手。（★ 两个动作要接起来，不许写成两句）
（旧留痕：「有点不太会怎么接句子，早点出发憋了一个 leave early」—— 这是衔接问题不是词汇问题；
　三条路：一个动词全包 advised sb to do ／ and 并列 ／ 分词接第二层）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-249）</summary>

`「**有点不太会怎么接句子**，早点出发憋了一个 leave early」|他给了我们一些建议，劝我们早点出发|★ **这是衔接问题不是词汇问题**（她的核心缺口之一）。三条路，从省到全：<br>① `He **advised** us to leave early.`（一个动词全包，最省）<br>② `He gave us some advice **and urged** us to leave early.`（and 并列两个动作）<br>③ `He gave us some advice, **suggesting** we leave early.`（分词接第二层）<br>★ 她「憋」出的 **leave early 完全正确**（＝set off early／start early）<br>★ 顺带把 advice 用法钉死：**advice 永远不可数**（没有 advices）· `some advice` · `a **piece of** advice` · `advise sb **to do**`|**K**|`

</details>

## #0072 📋 本组悬空备案：第 5 题她走 share 未走 proportion、第 8 题
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
（旧档案未单列，见下方「我错在哪」与原始行）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：留痕（口径备案＋她的资产）
正确：

**中文触发点**
📋 **本组悬空备案（出题前预声明的规则首次生效，两次）**：第 5 题她走 `share` 未走 proportion、第 8 题她走 `suggestions` 未走 advice —— **两个都完全正确**，故不记 ❌；但考点未被行使，**也不记 ✅**，E-172 / E-128 原样进下一组。<br>★ 顺带 ✅ 两条（出处均为她的产出）：第 2 题 `1.85 million` 写法对 ⇒ **E-168** ✅；第 7 题 `of **the** total population` 冠词在 ⇒ **E-154** ✅<br>✅+ **她自发产出/自主纠正**：`people who stay patient` **不加逗号**（组 5 刚犯的非限定从句错，本组自己修回 ⇒ **E-222 回潮修复**）· 用 people 避开 patient 撞词形（08-15 她自己提出的解法，今天自主用上）· `subsequently`（选词是升级）· `steadily rose`（今天教的，第二次自主调出）· `everyone **lives**`（主谓一致本组也对）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-251）</summary>

`📋 **本组悬空备案（出题前预声明的规则首次生效，两次）**：第 5 题她走 `share` 未走 proportion、第 8 题她走 `suggestions` 未走 advice —— **两个都完全正确**，故不记 ❌；但考点未被行使，**也不记 ✅**，E-172 / E-128 原样进下一组。<br>★ 顺带 ✅ 两条（出处均为她的产出）：第 2 题 `1.85 million` 写法对 ⇒ **E-168** ✅；第 7 题 `of **the** total population` 冠词在 ⇒ **E-154** ✅<br>✅+ **她自发产出/自主纠正**：`people who stay patient` **不加逗号**（组 5 刚犯的非限定从句错，本组自己修回 ⇒ **E-222 回潮修复**）· 用 people 避开 patient 撞词形（08-15 她自己提出的解法，今天自主用上）· `subsequently`（选词是升级）· `steadily rose`（今天教的，第二次自主调出）· `everyone **lives**`（主谓一致本组也对）|留痕（口径备案＋她的资产）|`

</details>

## #0073 ⭐⭐「这里我想泛指，应该怎么写。因为想说如果哪一个病情加重，就说那个，后面特指」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
✅+ 她的判据

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：病情严重的话，病人会被转到更大的医院
正确：★★ **她自己把英语冠词的核心机制推出来了，而且写的就是标准解法**：<br>　`**a** patient` ＝引入（首次提及、泛指某一个）→ `**the** patient` ＝回指（就是刚说的那一个）<br>　**a 引入 · the 回指** —— 这条比任何冠词规则都管用，且她是**从"我想表达什么"倒推出来的，不是背来的**<br>★ 备用两条：`If **patients' conditions** worsen, **they** will be transferred…`（复数泛指，最省）／`**Patients whose** condition worsens are transferred…`（定语从句）<br>★ 与 E-135「限定≠定指」、E-194「the vs an increase」构成她自建的冠词判据三件套

**中文触发点**
如果哪个学生跟不上，老师就会给那个学生单独补课。（★ 第一次提到和回指要用不同的冠词）
（旧留痕：⭐⭐「这里我想泛指…如果哪一个病情加重，就说那个，后面特指」—— 她自己推出了
　**a 引入 · the 回指**；换场景重测，原场景是病人转院）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-260）</summary>

`⭐⭐「这里我想泛指，应该怎么写。因为想说如果**哪一个**病情加重，就说**那个**，后面特指」|病情严重的话，病人会被转到更大的医院|★★ **她自己把英语冠词的核心机制推出来了，而且写的就是标准解法**：<br>　`**a** patient` ＝引入（首次提及、泛指某一个）→ `**the** patient` ＝回指（就是刚说的那一个）<br>　**a 引入 · the 回指** —— 这条比任何冠词规则都管用，且她是**从"我想表达什么"倒推出来的，不是背来的**<br>★ 备用两条：`If **patients' conditions** worsen, **they** will be transferred…`（复数泛指，最省）／`**Patients whose** condition worsens are transferred…`（定语从句）<br>★ 与 E-135「限定≠定指」、E-194「the vs an increase」构成她自建的冠词判据三件套|✅+ **她的判据**|`

</details>

## #0074 学校应该保证学生每天有休息时间
状态：在池 ｜ 连对 0 ｜ 连错 2 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F04

**问题是什么**
K

**怎么发现的**
2026-08-18　D1 学习日 C2·组8

**我错在哪**
她的：学校应该保障学生每天的休息时间
正确：★ **不是这个位置要用 a，是 `period` 这个词要求 a —— 冠词跟着名词的可数性走**：<br>　不可数（**rest / time / sleep**）→ 零冠词：`daily rest` ✅ `daily rest time` ✅<br>　可数（**period / break / session**）→ 必须 a/the/复数：`**a** daily rest period` ✅ `daily rest **periods**` ✅ `~~daily rest period~~` ❌<br>★★ 通则：**可数单数名词在英语里永远不能光着**，哪怕泛指<br>★ 用 a 不用 the，因为这里泛指（随便哪一段）不是特指 ⇒ 与她自己推出的 **a 引入 / the 回指**（E-260）同一条

**中文触发点**
- 2026-08-20　这家医院必须保证每位夜班护士一段完整的休息（"休息"用 period 这个词；用「保证【谁】【什么】」的双宾语说法，别用所有格）
**学校应该保证学生每天有休息时间（用「保证【谁】【什么】」这个双宾语说法，别用所有格）**（08-18 题面点名：她走 `students' daily rest time` 所有格，语法成立、但双宾语结构不出现，`a` 的考点整块绕过 ⇒ 记 ◎。原触发点是她的问句「为什么 `Schools should guarantee students **a** daily rest period` 是 a」）

### 历史记录
- 2026-08-18 ◎ D1 学习日 C2·组8
- 2026-08-20 ❌ D3 学习日 C2·组1　（当日 2 次：第 1 题 ✅ → 第 8 题 ❌，按 §3.2 只按最后一次记）
  **第 1 题（本条的正题）✅**：她写 `the hospital must guarantee every night-shift nurse **a reset period**`。
  双宾语 `guarantee sb sth` 一次到位，没有退回所有格；`period` 前面的 **a** 也在 ⇒ 本条考点命中。
  **第 8 题（顺带）❌**：`opposed constructing **waste treatment plant** here` —— 可数单数光着，该是 `**a** waste treatment plant`。
  ★ 同一天同一条规则，**被点名时对、没被点名时漏**：
  　第 1 题题面里我写了「"休息"用 period 这个词」，等于把注意力按在那个名词上；
  　第 8 题没有任何提示，冠词整个不见。⇒ 不是不知道规则，是这条规则**不会自己启动**。
  　这与 #0126、#0055 的机制一模一样（认知带宽被主考点占满，剩下的层掉线）。
  同句另两处不属于本条：`reset`→`rest` 记在 #0095；丢「完整」记在 #0126。
  ⇒ 连对归 0、连错 1，毕业线按 §3.5 A4 抬到 **3**（这是建号后第一次在复习中错）。
- 2026-08-20 　作文 T2-17　**高压 ✅ 留痕，不推进 streak**
  全篇 16 处可数单数**无一光杆**：a subject of debate · an individual · a higher title ·
  a new line manager · a dislike · A guaranteed path · a certificate · a choice · a new city ·
  a new relationship · a person's life · a minimum · any chance · the new environment ·
  their original role · its set path。
  ★ 与今天组1 第 8 题的失手（`constructing waste treatment plant` 光着）构成直接对照：
  　 **复习组失守、作文里 16 处零失守** ⇒ 那次不是知识缺口。
  ⚠️ 不推进 streak：本条今天的净结果已由组1 的 ❌ 定下（当天出现过 ❌ 就记 ❌）。
- 2026-08-23 ❌ D1 学习日 C3·组2 第 7 题（顺带）　连错 2
  主考点是 #0267。她写 `this course is quite challenging, and **workload** is a bit heavy`。
  `workload` 是**可数单数**，光着不行 ⇒ `**the** workload`（前文已把这门课限定住 ⇒ 定指）。
  ★ 与本条 08-20 的失手同一个形状（`constructing waste treatment plant` 光着）——
  　 都是**并列结构里的第二个名词**：第一个分句她给了限定词（`this course`），
  　 到第二个分句就掉了。
  ⇒ **找法加一条**：并列句写完，把 and 后面那个名词单独拎出来问一句"它前面有没有限定词"。
  📋 最小修改：`… and **the** workload is somewhat heavy.`
- 2026-08-23 ✅ D1 学习日 C3·组4 第 9 题　**连错 2 之后第一次答对，连对 1**
  题面「新的规定必须保证每个实习生一段固定的午休。（★ 用 guarantee，走「保证【谁】【什么】」的
  双宾语；★「午休」用 break 这个词）」（连对 0 ⇒ 按 §6 必须给英文词），她写
  `the new regulation must guarantee every intern a fixed lunch break`。
  ★ **两层同时到位**：① 双宾语 `guarantee sb sth` 没退回所有格 ② 可数单数 `**a** fixed lunch break`
  　 的冠词在（这正是 08-20 组1 第 8 题 `waste treatment plant` 光着的那一层）。
  ⚠️ **证据分量说清楚**：题面把 `guarantee` 和 `break` 两个词都点名了 ⇒ 注意力被按在名词上。
  　 本条 08-20 记过的机制就是"**被点名时对、没被点名时漏**"，所以这次的 ✅ 证明的是
  　 「知道 break 可数」，不证明「不被点名也会自己启动」。后者只能在作文里验（§7）。
  📋 顺带：`the new regulation` 单数可数、冠词在 ✔ · `every intern` 单数 ✔。
  ⚠️⚠️ **streak 不推进（§3.2 同日口径）**：本条今天在组2 第 7 题（顺带）已经记过一次 ❌
  　（`and workload is a bit heavy` 光杆可数单数）⇒ **当天只要出现过 ❌ 就记 ❌**
  　⇒ 今天的净结果仍是 ❌，**连对 0 ／ 连错 2 维持不变**，本行只留证据。
  ★ 而这一正一负恰好把本条的机制又演了一遍：**被点名（题面给了 break）时冠词在，
  　 没被点名（workload）时冠词掉**。这不是"会不会"的问题，是"会不会自己启动"的问题。
<details><summary>原始行（旧表逐字，旧号 E-264）</summary>

`**学校应该保证学生每天有休息时间（用「保证【谁】【什么】」这个双宾语说法，别用所有格）**（08-18 题面点名：她走 `students' daily rest time` 所有格，语法成立、但双宾语结构不出现，`a` 的考点整块绕过 ⇒ 记 ◎。原触发点是她的问句「为什么 `Schools should guarantee students **a** daily rest period` 是 a」）|学校应该保障学生每天的休息时间|★ **不是这个位置要用 a，是 `period` 这个词要求 a —— 冠词跟着名词的可数性走**：<br>　不可数（**rest / time / sleep**）→ 零冠词：`daily rest` ✅ `daily rest time` ✅<br>　可数（**period / break / session**）→ 必须 a/the/复数：`**a** daily rest period` ✅ `daily rest **periods**` ✅ `~~daily rest period~~` ❌<br>★★ 通则：**可数单数名词在英语里永远不能光着**，哪怕泛指<br>★ 用 a 不用 the，因为这里泛指（随便哪一段）不是特指 ⇒ 与她自己推出的 **a 引入 / the 回指**（E-260）同一条|**K**|`

</details>

## #0075 祖父母或多或少会帮年轻父母带孩子
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
① P11 漏词 ② P4 单复数 ← 靶子　R · P4（挂主错）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：**parents**（漏 grand-）… young **parent**（单数）
正确：**Grandparents** … young **parents** … their children<br>🔴 `young parent` 单数是 **E-044 隔一组回潮**（组 9 刚写对 many young parents）

**中文触发点**
**祖父母**或多或少会帮**年轻父母**带孩子

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-267）</summary>

`**祖父母**或多或少会帮**年轻父母**带孩子|**parents**（漏 grand-）… young **parent**（单数）|**Grandparents** … young **parents** … their children<br>🔴 `young parent` 单数是 **E-044 隔一组回潮**（组 9 刚写对 many young parents）|① P11 漏词 ② P4 单复数 ← 靶子|R · **P4**（挂主错）|`

</details>

## #0076 ⭐ 两条"读数无效"欠账还清，双双一次命中，且都印证同一件事：不是她不会，是题面的问
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
（旧档案未单列，见下方「我错在哪」与原始行）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：留痕（方法二次验证）
正确：

**中文触发点**
⭐ **两条"读数无效"欠账还清，双双一次命中，且都印证同一件事：不是她不会，是题面的问题**<br>· **E-032**（prefer A to B）：08-10 建条目起挂"K 常驻缺口 · 0/3 抽查"，但那三次**全是题面逼不出**（「比起开车我更喜欢坐地铁」动词对动词，她走 `I'd rather…than` 完全正确）。改成**名词对名词**（比起茶我更喜欢咖啡）后 **一次写对 `I prefer coffee to tea`** ⇒ **该条从来不是知识缺口，应从 K 改判 R**<br>· **E-073**（hierarchy→hierarchical）：组 3 她写 tiered（正确但按预设读数规则记 ◎）。本组**按她 08-16 的裁决直接点名词族**（"用 hierarchy 那个词族，别用 tiered"）→ `hierarchical` 一次命中<br>　★ 顺带：`China **has built**` —— 组 3 的 `China build`（主谓＋时态两层错）**当场修好** ⇒ **E-205 回潮修复**<br>★★ **「题面点名」策略第 2 次验证成功**（第 1 次是 E-172 proportion）。两次的形状完全一样：**她的产出正确 → 教练判无效 → 点名后一次命中**。⇒ 与 E-275 合并成结论：**今天全部 5 处"题面逼不出考点"（E-071/073/111/128/170）都该用点名解决，不该靠绕着改题面**

⛔ **不出单点题（2026-08-24 定）** —— 本条正文是一段**教练侧的流程观察**（"读数无效欠账还清"），
按 §2 不该是条目。迁移存量，留档不删、不召回；要不要退池等她定。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-276）</summary>

`⭐ **两条"读数无效"欠账还清，双双一次命中，且都印证同一件事：不是她不会，是题面的问题**<br>· **E-032**（prefer A to B）：08-10 建条目起挂"K 常驻缺口 · 0/3 抽查"，但那三次**全是题面逼不出**（「比起开车我更喜欢坐地铁」动词对动词，她走 `I'd rather…than` 完全正确）。改成**名词对名词**（比起茶我更喜欢咖啡）后 **一次写对 `I prefer coffee to tea`** ⇒ **该条从来不是知识缺口，应从 K 改判 R**<br>· **E-073**（hierarchy→hierarchical）：组 3 她写 tiered（正确但按预设读数规则记 ◎）。本组**按她 08-16 的裁决直接点名词族**（"用 hierarchy 那个词族，别用 tiered"）→ `hierarchical` 一次命中<br>　★ 顺带：`China **has built**` —— 组 3 的 `China build`（主谓＋时态两层错）**当场修好** ⇒ **E-205 回潮修复**<br>★★ **「题面点名」策略第 2 次验证成功**（第 1 次是 E-172 proportion）。两次的形状完全一样：**她的产出正确 → 教练判无效 → 点名后一次命中**。⇒ 与 E-275 合并成结论：**今天全部 5 处"题面逼不出考点"（E-071/073/111/128/170）都该用点名解决，不该靠绕着改题面**|留痕（方法二次验证）|`

</details>

## #0077 这些材料的价格
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
U · 待排序　0/2

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：「如果 of 后面是复数，前面 price 可以是单数么」
正确：✅ **可以，但意思不同**：<br>· `the **price** of these materials`＝把它们当一个整体算，**一个价**<br>· `the **prices** of these materials`＝各材料各自的价，**多个价**<br>两个都合法，选哪个看你说的是一个价还是多个价。谈"材料涨价"通常是多种 → 复数<br>★ 另一层（她这句真正的问题）：**泛指材料不加 the** —— `the price of **the** materials` 里第二个 the 把范围缩成"那批特定材料"。泛指写 `material prices` 或 `the price of materials`

**中文触发点**
**这些材料的价格**（单复数与冠词）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-286）</summary>

`**这些材料的价格**（单复数与冠词）|「如果 of 后面是复数，前面 price 可以是单数么」|✅ **可以，但意思不同**：<br>· `the **price** of these materials`＝把它们当一个整体算，**一个价**<br>· `the **prices** of these materials`＝各材料各自的价，**多个价**<br>两个都合法，选哪个看你说的是一个价还是多个价。谈"材料涨价"通常是多种 → 复数<br>★ 另一层（她这句真正的问题）：**泛指材料不加 the** —— `the price of **the** materials` 里第二个 the 把范围缩成"那批特定材料"。泛指写 `material prices` 或 `the price of materials`|U · 待排序|0/2|`

</details>

## #0078 如果医生治不了这个病，就会把病人转给专科医生
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F04

**问题是什么**
⚠️ 不地道（她那句语法成立）　U · 待排序

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`if **the doctor** cannot treat the disease, **he or she** will refer **the patient**…`
正确：★ **泛指一律用复数，不用 the ＋ 单数，更不用 he or she**：<br>✅ `If **doctors** cannot treat a disease, **they refer patients** to a specialist.`<br>理由：`he or she` 语法没错但啰嗦，正式写作里普遍改用复数回避性别；复数泛指同时省掉冠词麻烦。<br>★ 与 [[E-196]]（`Schools require students to…` 泛指零冠词复数）是同一条规则的两次出现

**中文触发点**
**如果医生治不了这个病，就会把病人转给专科医生**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-297）</summary>

`**如果医生治不了这个病，就会把病人转给专科医生**|`if **the doctor** cannot treat the disease, **he or she** will refer **the patient**…`|★ **泛指一律用复数，不用 the ＋ 单数，更不用 he or she**：<br>✅ `If **doctors** cannot treat a disease, **they refer patients** to a specialist.`<br>理由：`he or she` 语法没错但啰嗦，正式写作里普遍改用复数回避性别；复数泛指同时省掉冠词麻烦。<br>★ 与 [[E-196]]（`Schools require students to…` 泛指零冠词复数）是同一条规则的两次出现|⚠️ 不地道（她那句语法成立）|U · 待排序|0/2|`

</details>

## #0080 病人的病情如果加重，就要立刻送医院
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F04

**问题是什么**
P4 单复数 ← 靶子　R · P4

**怎么发现的**
2026-08-18　D1 学习日 C2·组8

**我错在哪**
她的：`send them to **hospitals**`
正确：`send them to **hospital**`（英式，机构义零冠词）／ `send them to **a hospital**`（美式）<br>★ **机构名词的零冠词用法** —— 表示"去做那件事"而不是"去那栋建筑"时，英式一律零冠词：<br>　`go to **hospital**`（就医）· `go to **school**`（上学）· `go to **university**` · `be in **prison**` · `go to **church**`<br>　对照：`go to **the** hospital`（去医院那栋楼，比如探病）<br>🔴 她这里错的是**数**：主语 the patient 单数、送去一家医院，复数 hospitals 对不上

**中文触发点**
- 2026-08-19　孩子发烧超过三天就该送医院。
- （更早）**病人的病情如果加重，就要立刻送医院**

### 历史记录
- 2026-08-18 ❌ D1 学习日 C2·组8
- 2026-08-19 ✅ D2 学习日 C2·组3 第 10 题
  题面换成「孩子发烧超过三天就该送医院」，她写 `should be taken **to hospital**` ——
  英式机构义零冠词单数，没有回到 to hospitals ⇒ ✅，连对 1（08-18 建号那次是 ❌）。
  📋 顺带用对：`be taken to`（被动）比原句的 `send them to` 更自然；`a fever` 冠词也对。
  📋 同句两处不属于本条：
  · `children who **has**` 主谓不一致 → 记在 #0055
  · `for **over than** three days` → 记在 #0265
- 2026-08-22 ❌ D4 复习日 C2·组5 第 4 题
  题面「老人要是在家里摔伤了，必须马上送医院」，她写
  `they must **be got to the hospital** immediately`。
  ★ **两处都塌，只有数那一半修对了**：
  ```
  ✅ 数     hospital 单数（08-18 那次写的是 hospitals，这一半修好了）
  ❌ 动词   `be got to` 不是英文 —— get 没有这个被动用法，要 `be **taken** to`（或 be **rushed** to）
  ❌ 冠词   就医语境英式**零冠词**：`be taken to **hospital**`
           `to **the** hospital` ＝ 去医院那栋楼（探病、送东西），本条正文写死了这一条
  ```
  ⇒ 本条正文同时挂着「数」与「机构零冠词」两个考点，只对一半不算命中 ⇒ 记 ❌，连对 1 → 0。
  ⚠️ **收进 §8④ 积压①**：本条是典型的"一条挂两个考点"，
  　 08-18 到今天题面只逼得到数那一半，冠词那一半一直没被单独测过。
  　 改法：题面里加一句「（★ 送去接受治疗，不是去医院那栋楼）」，把零冠词逼出来。
  📋 更好：`If an elderly person **has a fall** at home, they must be taken to hospital **straight away**.`
  　（has a fall 是英式固定块，一个名词收掉 falls and gets hurt 两个动词）
- 2026-08-23 ✅ D1 学习日 C3·组3 第 6 题　**两个考点第一次同时命中，连对 1**
  题面「这个孩子要是再吐一次，就必须马上送医院。
  　　（★ 用 hospital；送去接受治疗，不是去医院那栋楼探病）」
  ——★ 本条连对 0 ⇒ 按 08-23 新规则**把目标英文词写进括号**；同时按 08-22 §8④ 积压①
  　 补上「接受治疗 ≠ 那栋楼」这句语境限定，专门把**零冠词**那一半逼出来。
  她写 `if the child throw up once more, he must **be taken to hospital** immediately`。
  ★ **本条挂着的两个考点这次都对**（08-18 只对了零冠词一半、08-22 只对了数一半）：
  ```
  数      `hospital` 单数 ✅（08-18 写的是 hospitals）
  零冠词  `to hospital` 不加 the ✅（08-22 写的是 to **the** hospital）
  动词    `be **taken** to` ✅（08-22 写的是 `be **got** to`，get 没有这个被动用法）
  ```
  ⇒ 三处全对 ⇒ 命中，连对 1。**这是本条自 08-18 建号以来第一次完整答对。**
  ⚠️ 同句一处**不属于本条、也不建号**：`the child **throw** up` → `**throws** up`
  　 三单 -s 掉词尾 ⇒ 按 §2⑤ 挂 `reminders.md` **R2**，教练当场点名，不占编号、不进复习池。
  📋 更好：`If the child **vomits** once more, he must be taken to hospital immediately.`
  　（`throw up` 是口语说法；单点题里不判 —— 语域按 §6 新规则一律挂作文验）

<details><summary>原始行（旧表逐字，旧号 E-319）</summary>

`**病人的病情如果加重，就要立刻送医院**|`send them to **hospitals**`|`send them to **hospital**`（英式，机构义零冠词）／ `send them to **a hospital**`（美式）<br>★ **机构名词的零冠词用法** —— 表示"去做那件事"而不是"去那栋建筑"时，英式一律零冠词：<br>　`go to **hospital**`（就医）· `go to **school**`（上学）· `go to **university**` · `be in **prison**` · `go to **church**`<br>　对照：`go to **the** hospital`（去医院那栋楼，比如探病）<br>🔴 她这里错的是**数**：主语 the patient 单数、送去一家医院，复数 hospitals 对不上|P4 单复数 ← **靶子**|R · **P4**|0/3|`

</details>

## #0251 this kind of 后面接单数，these kinds of 后面才接复数
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F04

**问题是什么**
`kind / type / sort` 本身是可数名词，前面的指示词和后面的名词都要跟着它的数走，三个位置必须一致：
　✅ `**this** kind **of** complaint`　（单数一路到底）
　✅ `**these** kinds **of** complaints`（复数一路到底）
　❌ `this kind of complaint**s**`　❌ `these kind of complaints`
最省事的躲法：**别用 kind of，改成 such / of this kind**
　✅ `**such** complaints` ／ `complaints **of this kind**`
⚠️ 与 #0048 不是一条：#0048 是"该复数写成了单数"，改正动作是**加 s**；
本条是"该单数写成了复数"，改正动作是**去掉 s**（或整块换掉）。方向相反。

**怎么发现的**
2026-08-19　D2 学习日 C2·组1 第 10 题

**我错在哪**
她的：`there are a few of **that kind of complaints** every year`
正确：`there are only a few **complaints of this kind** each year`
　　／`only a handful of **such complaints** are filed each year`
还有一处结构：`a few **of**` 后面要接定指（a few of these complaints）；
泛指时不能带 of，直接 `a few complaints`。

**中文触发点**
- 2026-08-22（改死后的新题面，人工 review 时用）　这种事故在冬天多，那几种机械故障则一年到头都有。
  （★ 两个半句都必须用 this kind of ／ these kinds of 那个说法，注意两边名词的单复数不一样）
- 2026-08-22（已作废）　这类投诉一般三天之内就能处理完。
  ★ 缺陷：中文「这类 X」有 of this nature / of this kind / such 好几条现成的路，逼不出本条结构 ⇒ ◎✅
- （更早）这种事故在冬天比较常见。（08-20 用过）

### 历史记录
- 2026-08-19 ❌ D2 学习日 C2·组1 第 10 题（顺带）
  查重（§3.5 B0）：grep 了 `kind of` `type of` `sort of` `这类` `这种`，
  命中的都是别的条目的题面用字（#0018 #0079 #0068），没有一条讲 kind of 的数。
  又逐条看了 F04 现有 24 条，最近的是 #0048（该复数写成单数）与 #0060（单数病人配单数医院）。
  #0048 改正动作是加 s、本条是去 s，问 1 不成立；#0060 讲的是句内两个名词的数要照应，
  不涉及 kind of 这个结构本身，问 2 不成立 ⇒ 新建。
- 2026-08-20 ✅ D3 学习日 C2·组2 第 1 题
  题面「这种事故在冬天比较常见」，她写 `**this kind of accident** is fairly common in the winter`。
  this kind of ＋ 单数，一次到位 ⇒ 考点命中，连对 1。整句零改动。
  `in the winter` 也成立（美式常带 the，英式多写 in winter），不判。
  ★ 她在本题当场点名要学 `fairly` 的各种用法（§2③）⇒ 见新建 #0267。
- 2026-08-22 **◎✅** D4 复习日 C2·组4 第 4 题　**算对，连对 2 ⇒ 🎓（带 ⚠️🔍 标记）**
  题面「这类投诉一般三天之内就能处理完」，她写
  `**complaints of this nature** usually take less than three days to process`。
  ★ `complaints of this nature` 是很地道的英文，也完全符合题面 ⇒ 判 ◎✅，连对 2 ⇒ 毕业。
  ⚠️⚠️ **但本条的考点（this kind of ＋ 单数 / these kinds of ＋ 复数）从建号到毕业一次都没被行使。**
  　 08-20 那次她写 `this kind of accident is fairly common`（单数对了，但那题的主考点是 #0267）；
  　 今天这次直接绕过了整个结构。⇒ 按 §3.3 打 `⚠️🔍 待人工 review：考点未行使的毕业`。
  ★ 题面的毛病：中文「这类 X」在英文里有一堆现成的路
  　（of this nature ／ of this kind ／ such ／ this sort of），this kind of 不是必经之路。
  ⇒ 改好的新题面已存进下方中文触发点，供人工 review 时取用。
  📋 顺带用对 **#0266 框架①**：`usually **take** less than three days **to process**` ——
  　 与组 2 的 `spent a whole summer to adapt`（框架③写错）形成同日对照。
- 2026-08-22 ❌ D4 复习日 C2·组10 第 10 题（顺带）　**★ 当天毕业当天塌**
  她写 `**this kind of investments** yield returns only after several years`。
  this kind of 后面用了**复数** —— 正是本条的考点，原样复发。
  正确：`this kind of **investment** … yields` ／ `**investments of this kind** … yield`。

  ### ★ 更正块（§4.7，2026-08-22 当天改判）
  **原判**：组 4 判 ◎✅ ⇒ 连对 2 ⇒ 🎓（带 ⚠️🔍 标记）。
  **新判**：**在池 ｜ 连对 0 ｜ 连错 1**，⚠️🔍 标记随之撤销（已经不是毕业）。
  **本条今天全天**：
  ```
  组4  ◎✅（毕业）　组5/6/7/8 顺带用对 ×4　组10 ❌
  ⇒ 按 §3.2「当天只要出现过 ❌ 就记 ❌」⇒ 当天净结果 ＝ ❌ ⇒ 本来就不该毕业
  ⇒ 今天之前是 连对 1／连错 0 ⇒ 当天净 ❌ ⇒ 连对 0／连错 1
  ```
  **这个数住在哪几处**：本条状态行 ／ 本条历史（组 4 那行 ◎✅ 与四行顺带用对全部留痕不删 ＋ 本更正块）
  　／ sessions/2026-08-22.md 组 4、组 5、组 6、组 7、组 8、组 10 战报。
  ★★ **⚠️🔍 这个机制在本条上被完整验证了一遍**：
  　 上午靠 ◎✅ 凑到毕业线、考点一次都没被行使 ⇒ 打标记；
  　 下午在完全没有提示的一题里，同一个考点原样塌掉 ⇒ 毕业撤销。
  　 **没有这个标记，它会带着一个假毕业出池、再也抽不到。**
  ⇒ 建议（等她定）：**靠 ◎✅ 凑到毕业线的条目，在当日结算前不算最终毕业。**
- 2026-08-22 📋 D4 复习日 C2·组5 第 10 题（顺带用对，🎓 状态不变）
  她在 #0315 那题里自发写出 `**this kind of method** carries risks` —— **this kind of ＋ 单数**。
  ★★ 这是本条**考点第一次被真正行使**：上午靠 ◎✅ 凑到毕业线时，考点一次都没出场，
  　 所以打了 `⚠️🔍`；下午她在完全没有提示的句子里把它写对了。
  ⇒ **⚠️🔍 标记先留着**（撤不撤由她定），但支持证据已经记在这里。
  ⇒ 这也说明 ⚠️🔍 这个机制是有用的：它把"不确定的毕业"标出来，而不是硬判对或硬判错。
- 2026-08-23 📋 D1 学习日 C3·组6 第 7 题（顺带用对，状态不变／不推进）
  主考点是 #0311。她写 `**this kind of** concern is completely understandable` —— this kind of ＋ **单数**。
  ★ 这是本条**第二次正面证据**，而且和 08-22 那次一样是"完全没提示的句子里自发写对"。
  ⚠️ 按复习组口径，顺带用对只列出、不推进 streak（连对仍为 0）——
  　 本条要真正翻身，得在**它自己作主考点**的题里对两次。
  ⇒ 记在这里，等它下次被抽到时作为背景。

---

## #0325 【已并入 #0059】英语里不可数的那批常见名词
状态：并入 #0059 ｜ 连对 — ｜ 连错 — ｜ 毕业线 — ｜ 上次 2026-08-22 ｜ 族 F04

> 🔗 **2026-08-22 她定「#0325 可以合并」⇒ 整条并入 #0059**（留最早的编号，§3.5 C4）。
> 编号不复用、不删除。正文与三行历史已全部搬进 #0059，本处只留指向。
> **不进复习池、不占在池条数、不参与毕业统计。**
> 合并同时带来一条出题纪律（写在 #0059 与 SKILL §6）：
> **⛔ 词表型条目不许出只考一个词的句子，一道题必须让两个以上成员同时落地。**

<details><summary>原正文（并入前逐字留存）</summary>

**问题是什么**
这一批名词在中文里都能说"一条／几条"，在英语里**一律不可数**：
```
evidence      证据      `The **evidence is** overwhelming.`   ⛔ ~~evidences~~ ~~an evidence~~
advice        建议      （见 #0059）
information   信息      `for further **information**`
research      研究      `**research shows** that…`            ⛔ ~~researches~~
equipment     设备      `the **equipment was** replaced`
knowledge     知识      `**knowledge is** power`
progress      进展      `**progress has been** slow`
feedback      反馈      `we received **feedback**`
furniture     家具      `the **furniture is** new`
staff         员工（集合）`the **staff are**…` 英式配复数，`staff members` 才可数
```
**要说"一条／几条"怎么办 —— 用量词把它变可数**：
```
a **piece of** evidence / advice / information ／ **two pieces of** evidence
a **piece of** research ／ **a study**（研究项目用 study，可数）
a **piece of** equipment ／ **an item of** furniture
**a great deal of / a large amount of** ＋ 不可数　⛔ 不能用 many / a number of
```
**判据**：写完一个抽象名词，先问「它能不能说 one X」——
不能说 `one evidence` ⇒ 它就不加 -s、不加 a、配单数谓语。
⚠️ 反过来也要记，最容易串的三组可数／不可数对：
```
不可数 evidence  ↔ 可数 **a fact / facts**
不可数 research  ↔ 可数 **a study / studies**
不可数 advice    ↔ 可数 **a suggestion / suggestions**（#0181 那条讲的就是这一对里的选词）
```

**怎么发现的**
2026-08-22　D4 复习日 C2·组4 第 10 题（顺带）。主考点是 #0317。

**我错在哪**
她的：`even though the **evidents are** solid`
正确：`the **evidence is** solid`
两处一个根：evidence 不可数 ⇒ ① 不加 -s（而且 `evidents` 根本不是词）② 谓语配单数 is。

**中文触发点**
警方掌握的证据非常充分，但没有一条能直接指向他。

### 历史记录
- 2026-08-22 ❌ 建号　D4 复习日 C2·组4 第 10 题（顺带）
  查重（§3.5 B0）：grep 了 `不可数` `evidence` `information` `research`，全档命中三条，逐条比对：
  · **#0059**（advice 不可数／advise 是动词）：问 1（去掉不可数名词上的 -s）与问 2（一句话能讲）都成立，
    但 **问 3 不成立** —— 掌握 advice 不可数**不会**自动让人知道 evidence 也不可数，
    这是**词表**不是**规则**。⇒ 不合并，两条交叉引用。
  · **#0058**（strain 是可数还是不可数）：那条是**单个词的可数性判定**，
    本条是**一批词的清单**，问 2 不成立。
  · **#0275**（三项并列的不可数抽象名词零冠词）：那条管**冠词**，本条管**加不加 -s 与谓语的数**，
    问 1 不成立。
  · **#0048**（该用复数的名词写成单数）：方向正好相反（那条是该复数写成单数，本条是不可数加了 -s），
    问 1 不成立。
  ⇒ 新建。**建这一条的另一个作用是收口** —— 可数性问题此前散在 #0058 #0059 #0094 三处，
  　 以后这一类一律归本条，不再零星建号。
  ⚠️ 不适用 SKILL §2 排除项⑤：这是**词表知识**不是构形，她写 `evidents` 说明根本不知道它不可数。
- 2026-08-22 ✅ D4 复习日 C2·组6 第 2 题　**同日建号、同日被测、同日修对**
  题面「警方掌握的证据非常充分，但没有一条能直接指向他」，她写
  `The police have abundent **evidence**, but **none of it points** directly to him`。
  ★ **三层全对**：① evidence 不加 -s ② 回指用 **it** 不是 them ③ 谓语 **points** 单数。
  　 上午组 4 她写的是 `the evidents are`，下午同一条规则三层全中 ⇒ 连对 1、连错归 0。
  ⚠️ 但要看清成色：**本条上午刚讲过**，间隔只有几小时，属于"刚教完就测"。
  　 真正的证据要等下一个周期换语境再测（§3.3 提示关系查两层里"跨 session 必须换语境"那条）。
  📋 `abundent` → `abundant` 是非词拼写，§3.2 复习组豁免；作文里照记。
  📋 顺带：`The police **have**` —— police 配复数，对。

  ### ★ 更正块（§4.7，2026-08-22 当天改判）
  **原判**：连对 1 ／ 连错 0。**新判**：连对 0 ／ 连错 1。
  **理由**：本条**建号那行就是 ❌**（组 4 `the evidents are`），组 6 的 ✅ 与它同一天。
  　按 §3.2 同日口径「当天只要出现过 ❌ 就记 ❌」⇒ 当天净结果是 ❌，不是 ✅。
  　教练原来只按最后一次结算，等于**让新建条目在建号当天就往前走一格** ——
  　这正是她 08-20 定这条口径时要防的（「不逐次推进：那样同一天答对两次就能毕业，间隔被压没了」）。
  **这个数住在哪几处**：本条状态行 ／ 本条历史（本更正块）／ sessions/2026-08-22.md 组 6 与组 9 战报。
  ⇒ 组 6 那行 ✅ **留痕不删**，只是不再推进 streak。

</details>

---

# F05 拼写/形近词

> 含构形规则、拼成另一个真词的串台

## #0083 demend · hurn → demand · hurt
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F05

**问题是什么**
P5 拼写　留痕·手机输入（不进 P5 计数；作文里的照常算）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`demend` · `hurn`
正确：`demand` · `hurt`

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— `demend`／`hurn` 都**不是真词**，
按 §3.2 属于复习组的手滑豁免范围，单点题里判不了对错；只有作文里才照记。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-051）</summary>

`（手滑）|`demend` · `hurn`|`demand` · `hurt`|P5 拼写|**留痕·手机输入**（不进 P5 计数；作文里的照常算）|—|`

</details>

## #0084 goverments → governments
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F05

**问题是什么**
P5 拼写　留痕·手机输入（不进 P5 计数；作文里的照常算）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`goverments`
正确：`governments`

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— `goverments` 不是真词，
按 §3.2 属于复习组的手滑豁免范围；只有作文里才照记。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-089）</summary>

`（手滑）|`goverments`|`governments`|P5 拼写|留痕·手机输入（不进 P5 计数；作文里的照常算）|—|`

</details>

## #0086 Manhatten → Manhattan
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F05

**问题是什么**
P5 拼写 08-16 改判：地名不进 P5，不出题（T1 图表上印着地名，考场照抄即可，不是要背的东西——她的判断，见 E-243）　留痕 · 不出题

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`Manhatten`
正确：`Manhattan`

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— `Manhatten` 不是真词，属手滑豁免；
而且专有名词的拼写 T1 图上就印着，中译英测不出东西。作文/T1 里照记。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-156）</summary>

`曼哈顿|`Manhatten`|`Manhattan`|~~P5 拼写~~ **08-16 改判：地名不进 P5，不出题**（T1 图表上印着地名，考场照抄即可，不是要背的东西——她的判断，见 E-243）|留痕 · 不出题|`

</details>

## #0093 ✅+ 她自发产出 / 自主纠正：the parents of the patient
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F05

**问题是什么**
（旧档案未单列，见下方「我错在哪」与原始行）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：留痕（她的资产＋备案）
正确：

**中文触发点**
✅+ **她自发产出 / 自主纠正**：`the parents of the patients` —— **形近串台没有发生**（累计 3 次的老错：08-11 employers/employees · 08-15 两次 patients/parents），本题故意让两个词同句出现，她抓对了 ⇒ **E-041 家族回潮修复**<br>· `guidance` 不可数用对（组 4 刚学）· `account for`（08-15 教的，自主调出）· `hand in their homework`（今早补记里给过，当场用上）· `finish work late in the evening`（今早给的 do not finish work until late 的变体，自己改造）<br>📋 **判定备案**：`patiens`／`dailly`／`tbe`／`order`(＝older) 四处按规则 C 手滑归一化，不计入 P5；第 8 题她用 `older **people**` 而非档案的 `the older population`，**两个都对**，考点（old→older 比较级形式）已行使 ⇒ 记 ✅

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-262）</summary>

`✅+ **她自发产出 / 自主纠正**：`the parents of the patients` —— **形近串台没有发生**（累计 3 次的老错：08-11 employers/employees · 08-15 两次 patients/parents），本题故意让两个词同句出现，她抓对了 ⇒ **E-041 家族回潮修复**<br>· `guidance` 不可数用对（组 4 刚学）· `account for`（08-15 教的，自主调出）· `hand in their homework`（今早补记里给过，当场用上）· `finish work late in the evening`（今早给的 do not finish work until late 的变体，自己改造）<br>📋 **判定备案**：`patiens`／`dailly`／`tbe`／`order`(＝older) 四处按规则 C 手滑归一化，不计入 P5；第 8 题她用 `older **people**` 而非档案的 `the older population`，**两个都对**，考点（old→older 比较级形式）已行使 ⇒ 记 ✅|留痕（她的资产＋备案）|`

</details>

## #0094 📋 本组备案 ＋ 她的资产：some advice 不可数用对 ⇒ E-128 悬空
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F05

**问题是什么**
（旧档案未单列，见下方「我错在哪」与原始行）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：留痕（备案＋资产）
正确：

**中文触发点**
📋 **本组备案 ＋ 她的资产**：`some advice` 不可数用对 ⇒ **E-128 悬空还清、连击重启**；`challenges` 复数 · `allows parents to` · `China, where` · `much earlier` 四条 → **连对 2**；`more or less help` 语序修复（原错 help more or less youth parents）；`help sb do sth` 框架用对；`before 4pm` 简洁。<br>★ 第 4 题她走 `young people` 而非档案的 `the young`——**两个都对**，原错 the younger 未复现 ⇒ 考点已行使记 ✅<br>★ `then`(＝the) 按规则 C 手滑归一化不计

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-271）</summary>

`📋 **本组备案 ＋ 她的资产**：`some advice` 不可数用对 ⇒ **E-128 悬空还清、连击重启**；`challenges` 复数 · `allows parents to` · `China, where` · `much earlier` 四条 → **连对 2**；`more or less help` 语序修复（原错 help more or less youth parents）；`help sb do sth` 框架用对；`before 4pm` 简洁。<br>★ 第 4 题她走 `young people` 而非档案的 `the young`——**两个都对**，原错 the younger 未复现 ⇒ 考点已行使记 ✅<br>★ `then`(＝the) 按规则 C 手滑归一化不计|留痕（备案＋资产）|`

</details>

## #0095 拼成了另一个真词（形近或同音），自己扫不出来
状态：在池 ｜ 连对 0 ｜ 连错 4 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F05
⚠️ 2026-08-23 **当天净结果由 ✅ 翻转为 ❌**（组1 ✅ patients/parents ／ 组2 ❌ works/workers，
　 §3.2「当天只要出现过 ❌ 就记 ❌」）。组1 那行 ✅ 留痕不删。

**问题是什么**
**与普通拼写错不是一回事**：拼成非词（`goverment`）自己一眼能发现；
拼成另一个真词，句子仍然"读得下去"，考场上扫多少遍都发现不了。

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
累计实例：
· `**order** people` → `older people`
· `**employers**` → `employees`（employer 雇主 / employee 员工）
· `**patients**` → `parents`
· `**works**` → `workers`
· `**there** clinics` → `their clinics`
高危对：order/older · employer/employee · patient/parent · work/worker · there/their/they're
· though/thought · quite/quiet · form/from · lose/loose
**判定口径**：这一类**不适用手滑豁免**，一律记。

**中文触发点**
**随着老年人口增长，医疗支出也在上升**

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组3（当日 2 次，取最后一次）
- 2026-08-18 ✅ D1 学习日 C2·组4
  ⚠️ 已并入 #0082 的历史
- 2026-08-19 ❌ D2 学习日 C2·组1 第 1 题（顺带）　（当日 2 次，按最后一次记）
  ★ **同日第 2 次**：组 3 第 3 题她写 `since the **beginner** of last year` → `the **beginning**`。
  beginner（初学者）／beginning（开端）又是一对形近真词，句子照样读得下去。
  ⇒ **一天之内犯两次、两次都是本条的机制**，高危对表里补上：**beginner/beginning**。
  「这类培训只对已经入职一段时间的**员工**才真正有用」，她写 `for **employers**`。
  ★ 这个词对（employer 雇主 / employee 员工）**在上面的累计实例里已经有了**，08-11 犯过一次，
  今天原样复发。句子读起来完全通顺，所以自己扫不出来 —— 正是本条描述的机制。
  按 §3.3，🎓 之后再犯 ⇒ 状态改回在池、连对归零、毕业线定为 3。
  找法（写进滚动表）：**凡是 -er / -ee 成对的词，写完回头问一次"我说的是给活的还是干活的"**：
  employer/employee · trainer/trainee · interviewer/interviewee · payer/payee。
- 2026-08-20 ❌ D3 学习日 C2·组1 第 1 题（顺带）
  她写 `a **reset** period`，要的是 `a **rest** period`。多打一个 e，落在一个真词上
  （reset＝重置），`a reset period` 在技术语境里甚至是个成立的搭配 ⇒ 整句读得通，自己扫不出来。
  ⇒ 正是本条的机制，按本条「不适用手滑豁免，一律记」的口径判 ❌。连错 2。
  高危对表补上：**rest / reset**。
  ⚠️ 同组另两处拼写**不记**，口径要分清（§3.2）：
  　`ultility`（第 4 题）、`trainning`（第 10 题）都**不是真词**，句子读起来会绊一下，
  　属于复习组手滑豁免的范围。本条只管"拼成另一个真词"这一类。
  ★ **同日第 2 次**（组2 第 4 题）：`small businesses to **complete** with big companies`
  　 → `**compete**`。complete/compete 又是一对形近真词，而且 `complete with` 本身是个成立的搭配
  　 （＝配备有），句子读起来毫无阻碍 ⇒ 正是本条机制。
  　 按 §3.2 同日只按最后一次记一次，本行合并为一次 ❌。高危对表再补：**compete / complete**。
  ★ **同日第 3 次**（组3 第 6 题）：`**the critic** is not completely unreasonable`
  　 → `**this criticism**`。critic（批评家，人）／criticism（批评，言论）又是一对形近真词，
  　 而且"那位批评家不是完全不讲理"整句读得通，照样扫不出来。高危对表再补：**critic / criticism**。
  ★ **一天之内三次，三对都不同**（rest/reset · compete/complete · critic/criticism）
  　 ⇒ 不是某几个词没记牢，是**这个机制本身**没有防线：她的自检读一遍句子觉得通顺就过。
  ⇒ 行动：这条不适合再出单点题（题面一点名她就会警觉），**改为只在作文里验**，
  　 并在交卷前清单里挂一条"逐词看形近真词"（装备候选，不占今天的名额）。
- 2026-08-22 ✅ D4 复习日 C2·组4 第 5 题　**本条第一次拿到干净的正面测量**
  题面「这些补贴是发给员工的，不是发给雇主的」（新写触发点，把最高危的那一对直接摆上），她写
  `These subsidies are intended for **employees**, not **employers**`。
  ★ 两个词**对比着**用，一个都没串 —— 这正是 08-11、08-19 两次犯过的那一对。
  ⇒ 连对 1、连错 2 归 0。
  ★ 出题方法留痕：**把高危对的两个词同时逼进一句**，比只考其中一个更能测出她分不分得清。
  　 下次换 patient/parent 或 trainer/trainee 用同样的写法。
- 2026-08-22 ❌ D4 复习日 C2·组9 第 1 题（顺带）
  她写 `he spends two **house** commuting every day`。要的是 `two **hours**`。
  ★ `house` 是**另一个真词**，按本条「不适用手滑豁免，一律记」的口径判 ❌。
  高危对表补上：**hours / house**（与 rest/reset、beginner/beginning 同一机制 —— 差一两个字母落在真词上）。

  ### ★ 更正块（§4.7，2026-08-22 当天改判）
  **原判**：组 5 判 ✅ 之后写成 连对 1 ／ 连错 0。
  **新判**：**连对 0 ／ 连错 3**（今天之前是 连对 0 ／ 连错 2，当天净结果 ❌ ⇒ 连错 +1）。
  **理由**：组 5（✅ employees/employers）与组 9（❌ house/hours）**是同一天**，
  　按 §3.2「当天只要出现过 ❌ 就记 ❌」⇒ 当天净结果是 ❌。教练原来只按最后一次结算，判宽了。
  **这个数住在哪几处**：本条状态行 ／ 本条历史（组 5 那行 ✅ 留痕不删 ＋ 本更正块）／
  　sessions/2026-08-22.md 组 5 与组 9 战报。
- 2026-08-23 ✅ D1 学习日 C3·组1 第 1 题
  题面「这家诊所今天的病人里，有一半是带孩子来的家长。（★ 必须同时出现"病人"和"家长"两个词）」
  ——★ 按本条 08-22 留下的出题方法（**把高危对的两个词同时逼进一句**）换了下一对：
  　 08-22 用 employee/employer，今天用 **patient/parent**。
  她写 `**parents** bringing children account for more than half of the **patients** at the clinic today`。
  两个词都拼对、都用对，一个都没串 ⇒ 命中，连对 1、连错 3 归 0。
  ⚠️ 同句一处曾拟另记 #0330（`more than half` ← 中文是「有一半」）——
  　 **她 2026-08-23 当场裁定「不用建，忽略」⇒ 该处不判错、编号作废**（墓碑见 F10 段末）。
  ★ 下一对候选（同法出题）：**work / worker** 或 **there / their**。
  ★ 她点名要学的两条从本题的更好版里长出来（§2③）：
  　 `**today's** patients` ⇒ 新建 **#0331**（时间名词的所有格）。
  📋 更好：`**Half of** today's patients at the clinic are parents who **came with** their children.`
  　（`bringing children` 的分词像在说"正在带孩子进来"；`came with` 更贴"带孩子来看病"这个事实）
- 2026-08-23 ❌ D1 学习日 C3·组2 第 9 题（顺带）　**work/worker 这一对原样复发，当天净结果翻转**
  主考点是 #0303。她写 `whether AI would replace a large number of **works**`，
  要的是 `**workers**`。她自己指出来的：「9 我是打错了，明显应该用 workers」。
  ★ **判 ❌ 不判豁免的理由，就是本条正文写死的那一句**：
  ```
  「拼成非词（goverment）自己一眼能发现；拼成另一个真词，句子仍然"读得下去"，
    考场上扫多少遍都发现不了。」
  ⇒ `works` 是真词（作品／工程），`a large number of works` 语法完全通、扫不出来。
  ⇒ 本条判定口径：**这一类不适用手滑豁免，一律记。**
  ```
  ★★ **而且这一对在本条的累计实例表里排第四行 —— 08-11 犯过一模一样的一次**：
  　 `· **works** → workers`。**原样复发，间隔 12 天。**
  ⇒ 与组1 的 ✅（patients/parents 对比着用，一个没串）合看，当天净结果按 §3.2 记 ❌，
  　 ~~连对 1 → 0、连错 1~~ ⚠️ **这个数写错了，已于 2026-08-24 更正为 连对 0 ／ 连错 4，见下方更正块**。

  ### ★ 更正块（§4.7，2026-08-24 由 `drill.py check` 查出）
  **原判**：连对 0 ／ **连错 1**。
  **新判**：连对 0 ／ **连错 4**。
  **判据哪里套宽了**：把当天的两次**分两次结算**了 ——
  　先用组1 的 ✅ 把连错清零（3 → 0），再让组2 的 ❌ 从 0 起加，得出 1。
  　但 §3.2 写死「当天只推进一次，当天只要出现过 ❌ 就记 ❌」⇒
  　**当天整体只有一个结果 ❌**，它作用在 08-22 收盘的 连错 3 上 ⇒ 连错 4、连对 0。
  **逐个数重算**（同日只结算一次，改判／撤销行不参与）：
  ```
  08-16 ✅ ⇒ 连对 1
  08-18 ✅ ⇒ 连对 2      （当时毕业线是 3，未毕业）
  08-19 ❌ ⇒ 连错 1
  08-20 ❌ ⇒ 连错 2
  08-22 组4 ✅ ＋ 组9 ❌ ⇒ 当天净 ❌ ⇒ 连错 3   （08-22 更正块已按此写死）
  08-23 组1 ✅ ＋ 组2 ❌ ⇒ 当天净 ❌ ⇒ 连错 4   ← 本次更正的就是这一步
  ```
  ★ **同一个错误 08-22 犯过一次、08-23 又犯了一次** —— 都是"同日先结算 ✅ 再结算 ❌"。
  　 08-22 那次是人工发现的，这次是脚本查出来的 ⇒ 这正是 `drill.py check` 要挡的那一类。
  **这个数住在哪几处**：本条状态行 ／ 本行（原文划线留痕）／ 本更正块 ／
  　`sessions/2026-08-23.md` 组2 战报那一行。四处已逐处同步。
  ★ 读出来的一件事：**她能分清"意思相反的一对"（employee/employer、patient/parent），
  　 栽的是"同一个词根、差一个后缀"的那一类**（work/works/workers、beginner/beginning）。
  　 前者靠语义就能分，后者只能靠**逐字看词尾** ⇒ 找法要分成两条：
  ```
  意思相反的一对   → 写完问"我说的是给活的还是干活的"（employer/employee、trainer/trainee）
  同词根差后缀     → 写完**逐字看最后三个字母**（work / works / workers · begin / beginner / beginning）
                    ★ 尤其是名词位置上的 -s：它到底是"复数"还是"另一个词"？
  ```
  ⚠️ 教练侧留痕：我一开始把这个 `works` 判进了 #0059（不可数名词被可数化），**判错了**，
  　 而正确答案就在本条自己的实例表里。⇒ §3.5 第 1 步的 grep 我漏了 `works` 这个词面。
  　 #0059 那边的误判已按 §4.7 撤销。
- 2026-08-23 ❌ D1 学习日 C3·组6 第 6 题（顺带）　**只留证据，不推进 streak（同日口径）**
  主考点是 #0277。她写 `a commission **than** depends on luck` → 应为 `**that** depends on luck`。
  ★ than 是**真词** ⇒ §3.2「拼成另一个真词的不豁免」，照记。
  ★ 这一处比普通形近串台多一层：她前半写的是 `prefer X **over** Y`（正确），
  　 而中式高频错搭正是 "prefer X **than** Y" ⇒ 很可能是**那个错误框架反过来污染了关系代词**。
  　 ⇒ 本条的高危对表补一对：`than / that`（尤其在 prefer / rather 这类比较语境里）。
  ⚠️ 按 §3.2 同日口径，本条今天的净结果已由组2 的 ❌ 定下（今天组1 ✅ → 组2 ❌），
  　 **连对 0 ／ 连错 4 维持不变**，本行只留证据。
<details><summary>原始行（旧表逐字，旧号 E-292）</summary>

`**随着老年人口增长，医疗支出也在上升**|`as the number of **order** people is growing`|`**older** people`　★ **这不是普通手滑**：order 和 older 都是真词，拼错之后句子仍然"读得下去"，考场上自己扫不出来。同类高危对：`order/older` · `though/thought` · `quite/quiet` · `form/from` · `lose/loose`|P11 形近真词串台（**区别于 P5 拼写**：拼成非词能被自己发现，拼成真词发现不了）|R · **P11**|0/3|`

</details>

> 🗑 **#0322 已撤销 —— 编号作废，不复用、不占条目数。**
> 2026-08-22 建号当天，她当场撤销：
> 「**322 不建，这类（和单复数一样）重复练习没有用，关键在于你需要不断提醒。**」
> 原拟内容：完成时里 have/has 后面必须是过去分词（`has double` → `has doubled`）。
> ⇒ 这一类「规则本来就会、只在压力下掉」的构形问题**不进复习池**（重复出题无效），
> 　 改挂教练侧常驻提醒清单 `reminders.md` **R1**：每组判定必扫，反馈里当场点名。
> ⇒ 同类已知成员：单复数 -s、三单 -s、-ed 词尾、冠词。见 SKILL §2 排除项⑤。

---

# F06 词类混用/位置

> 形容词副词互换、比较级构形、修饰语位置

## #0102 「youth 是什么时候能用」
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F06

**问题是什么**
K（用法边界，她主动报不会）　0/3 抽查

**怎么发现的**
2026-08-16　复习日 C1·组5

**我错在哪**
她的：青年失业是个严重问题（08-12 定题面：原格里塞了两个题面，违反"一题一个考点"；这句唯一路径是固定块 `youth unemployment`）
正确：`young`＝形容词（描述年龄）；`youth`＝名词（青年群体/时期），只在固定块里当定语：youth unemployment · youth hostel · youth club · youth culture。❌ `youth parents`

**中文触发点**
青年失业已经成了一个严重的问题。（★ "青年失业"用 youth 那个固定块）
（旧留痕：「youth 是什么时候能用」—— young 是形容词，youth 只在固定块里当定语）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组5

<details><summary>原始行（旧表逐字，旧号 E-052）</summary>

`「youth 是什么时候能用」|青年失业是个严重问题（08-12 定题面：原格里塞了两个题面，违反"一题一个考点"；这句唯一路径是固定块 `youth unemployment`）|`young`＝形容词（描述年龄）；`youth`＝名词（青年群体/时期），只在固定块里当定语：youth unemployment · youth hostel · youth club · youth culture。❌ `youth parents`|**K**（用法边界，她主动报不会）|0/3 抽查|`

</details>

## #0105 a health urgent → an urgent health problem
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F06

**问题是什么**
P11 词形（urgent 是形容词不能作名词）　R · P11

**怎么发现的**
2026-08-16　复习日 C1·组4

**我错在哪**
她的：**a health urgent**
正确：**an urgent health problem**

**中文触发点**
紧急的健康问题

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组4

<details><summary>原始行（旧表逐字，旧号 E-077）</summary>

`紧急的健康问题|**a health urgent**|**an urgent health problem**|P11 词形（urgent 是形容词不能作名词）|R · **P11**|0/3|`

</details>

## #0106 更安全也更快
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F06

**问题是什么**
待排序　U（待定）

**怎么发现的**
2026-08-16　复习日 C1·组6

**我错在哪**
她的：is the safest and most effective way
正确：Of the two, this one is **both safer and faster**（**只有两个选项时用比较级，不用最高级**）

**中文触发点**
更安全也更快（**08-16 题面加死：「在这两种办法之间，这一种最安全、也最快」**——原题面里**没有"只有两个选项"这个前提**，而考点恰恰建立在它上面；中文「更…也更…」还直接把比较级送到她手上 ⇒ 原错不可能复现、答对零信息。新题面照汉语习惯用「最」，英文必须写 Of the two…，选择点才回到题面里）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组6

<details><summary>原始行（旧表逐字，旧号 E-111）</summary>

`更安全也更快（**08-16 题面加死：「在这两种办法之间，这一种最安全、也最快」**——原题面里**没有"只有两个选项"这个前提**，而考点恰恰建立在它上面；中文「更…也更…」还直接把比较级送到她手上 ⇒ 原错不可能复现、答对零信息。新题面照汉语习惯用「最」，英文必须写 Of the two…，选择点才回到题面里）|is the safest and most effective way|Of the two, this one is **both safer and faster**（**只有两个选项时用比较级，不用最高级**）|待排序|U（待定）|0/2|`

</details>

## #0108 「这个副词可以放 is 后面么」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F06

**问题是什么**
（旧档案未单列，见下方「我错在哪」与原始行）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：两处都对。**方式/程度副词**（rapidly/sharply）两处都行；**频率副词**（always/often/never）必须放中间
正确：**K**

**中文触发点**
这项政策的效果显现得很慢，而且这类项目往往一拖就是几年。（★ "很慢"和"往往"两个副词，各自放对位置）
（旧留痕：「这个副词可以放 is 后面么」—— 方式/程度副词两处都行，频率副词必须放中间）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-132）</summary>

`「这个副词可以放 is 后面么」|两处都对。**方式/程度副词**（rapidly/sharply）两处都行；**频率副词**（always/often/never）必须放中间|**K**|`

</details>

## #0111 "可以理解 ≠ 明智" 这个命题怎么说
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F06

**问题是什么**
中文断言的是**两个属性不等价**。她的写法把它变成了"某物同时具备/不具备两个属性"，命题变了。
⚠️ 教练最初给的 `understandable is not the same as sensible` **本身不地道，已撤销**
（她说"感觉怪怪的"，成立：`X is not the same as Y` 两端要名词或动名词，光杆形容词做主语是边缘用法）。

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`is something understandable but not sensible`（命题变了）
三个自然版：
· `Understandable does **not mean** sensible.`（最省）
· `**Just because** something is understandable **doesn't mean** it is sensible.`
· `It is understandable, **but that does not make it** sensible.`
★ 她自己后来找到的解法也对：**不换词，加转折** —— `understandable **but not** sensible`。

**中文触发点**
可以理解并不等于合理。（★ 用 mean 那个说法）
（旧留痕：⭐「understandable is not the same as sensible（感觉怪怪的）」—— 她说得对，
　光杆形容词做 is not the same as 的主语是边缘用法，教练那版已撤销）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组4
  ⚠️ 已并入 #0201 #0225 的历史

<details><summary>原始行（旧表逐字，旧号 E-217）</summary>

`⭐「understandable is not the same as sensible（**感觉怪怪的**）」|可以理解不等于明智|★★ **她对，教练给的目标形式本身不地道，撤销**：`X is not the same as Y` 的两端要**名词或动名词**，光杆形容词做主语是边缘用法。<br>✅ 三个自然版：`Understandable does **not mean** sensible.`（形容词＋does not mean＋形容词，最省）／`**Being** understandable is not the same as **being** sensible.`（补动名词）／`**Just because** something is understandable **doesn't mean** it is sensible.`（最自然，口语书面都行）|**K**（判据；教练版已撤销）|`

</details>

## #0112 「severe issue / problem 这两个有什么区别」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F06

**问题是什么**
K

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：青年失业是个严重问题
正确：**problem** ＝麻烦，明确是坏事、要解决 ← 本句用这个最贴<br>**issue** ＝议题/待处理事项，中性偏正式，常含"有争议"（Whether to ban cars is a controversial **issue**）<br>★ 形容词搭配：`a **serious** problem` 是最标准的组合；`severe` 多配具体的坏东西（severe weather / pain / shortage），配 problem 能用但不如 serious 常见 ⇒ **推荐 a serious problem**

**中文触发点**
交通拥堵在很多大城市都是个严重的问题。（★ 用 serious ＋ problem）
（旧留痕：「severe issue / problem 这两个有什么区别」—— problem＝要解决的麻烦，
　issue＝中性偏正式的议题；serious 配 problem 最标准，severe 多配具体的坏东西）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-225）</summary>

`「severe issue / problem 这两个有什么区别」|青年失业是个严重问题|**problem** ＝麻烦，明确是坏事、要解决 ← 本句用这个最贴<br>**issue** ＝议题/待处理事项，中性偏正式，常含"有争议"（Whether to ban cars is a controversial **issue**）<br>★ 形容词搭配：`a **serious** problem` 是最标准的组合；`severe` 多配具体的坏东西（severe weather / pain / shortage），配 problem 能用但不如 serious 常见 ⇒ **推荐 a serious problem**|**K**|`

</details>

## #0113 曼哈顿在总人口中所占的份额降到了 19%
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F06

**问题是什么**
⚠️ 不地道（她那句读得懂）　U · 待排序

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`Manhattan's share … **shrunk** to 19%`
正确：① **动词形态**：shrink – **shrank** – shrunk。作过去式标准形是 `shrank`（词典虽列 shrunk 为次选，正式写作一律 shrank）<br>② **更标准的搭配**：份额/比例下降用 `**fell / dropped / declined** to 19%`；`shrink` 配的是"体积/规模变小"（the workforce shrank）而不是"降到某个数值"<br>　✅ `Manhattan's share of the total population **fell to** 19%.`

**中文触发点**
**曼哈顿在总人口中所占的份额降到了 19%**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-310）</summary>

`**曼哈顿在总人口中所占的份额降到了 19%**|`Manhattan's share … **shrunk** to 19%`|① **动词形态**：shrink – **shrank** – shrunk。作过去式标准形是 `shrank`（词典虽列 shrunk 为次选，正式写作一律 shrank）<br>② **更标准的搭配**：份额/比例下降用 `**fell / dropped / declined** to 19%`；`shrink` 配的是"体积/规模变小"（the workforce shrank）而不是"降到某个数值"<br>　✅ `Manhattan's share of the total population **fell to** 19%.`|⚠️ 不地道（她那句读得懂）|U · 待排序|0/2|`

</details>

## #0269 「在小范围／在一定范围内」怎么说 —— 按你限定的是什么分四条路
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F06

**成员出题账**
```
① on a … scale（规模）        2026-08-22 组5 题面「这个做法在小范围里行得通」⇒ ✅
② in … cases（情形）          2026-08-23 组3 题面「只在少数几种情况下管用」⇒ ✅
③ be limited to / confined to（边界）2026-08-23 组3 题面「目前还只限于两个试点城市」⇒ ✅
④ within a range of（幅度区间）未出过
⇒ 2026-08-23 她当场点名「be limited to 建一个条目练习」——
　 be limited to 就是本条第三条路的成员，已在本条落地，⛔ 不重复建号（§3.5 防重复）。
　 另与 #0294（be reserved for 一族）交叉引用，那条也列了 be limited to / be confined to。
```

**问题是什么**
中文一个"范围"，英文分四条路，**选哪条取决于你限定的是什么**：

```
限定"多大摊子"（规模）      on a … scale
  `on a **small** scale` · `on a **large** scale` · `on a **limited** scale`
  `The method works well **on a small scale**, but not nationwide.`

限定"在哪些情形下"（条件）  in … cases ／ under … conditions
  `It works **in a limited number of cases**.` · `**in certain cases**` · `**in most cases**`
  `**under laboratory conditions**` · `**under certain conditions**`　（介词见 #0253）

限定"管到哪为止"（边界）    the scope of ／ be limited to ／ be confined to
  `This is **beyond the scope of** a single article.`　（固定块见 #0030）
  `The trial was **limited to** three hospitals.` · `**confined to** a few regions.`

限定"多少范围内"（幅度区间）within a range of ／ within …
  `Prices stayed **within a narrow range**.` · `**within a 5% margin**`
```

**三条硬边**
```
① scale 说的是**规模大小**，不是"情形多少"。
   ✅ `works on a small scale`（小打小闹时管用）
   ⚠️ `works within a limited scope` 语法成立，但 scope 更常指"职责/讨论的边界"，
      说"只在少数情况下管用"不如直接写 `in a limited number of cases`
② scale 前面必须有冠词：`on **a** small scale` ✅　`~~on small scale~~` ❌（可数单数不能光着，#0074）
③ 作文里最好用的两个，先把这两个背熟：
   `**on a small scale**`（规模）· `**in a limited number of cases**`（情形）
```

**T2 里的现成句**
```
This approach works **on a small scale**, but it is unlikely to succeed **nationwide**.
The policy has been effective **in a limited number of cases**, not as a general solution.
Such measures are usually **confined to** large cities.
```
⚠️ 与 #0030（`beyond the scope of a doctor`）不合并：那条管的是**这一个固定块的冠词与介词**
　（out of scope of → beyond the scope of a…），改正动作是修那个块；
　本条管的是**四条路怎么选**，改正动作是先判断你限定的是什么。问 1、问 2 都不成立。
⚠️ 与 #0253（conditions 用 under / cases 用 in）不合并：那条管**介词跟哪个名词走**，
　本条管**先挑哪一族名词**。本条选完 cases 或 conditions 之后，介词才轮到 #0253 管。

**怎么发现的**
2026-08-20　D3 学习日 C2·组3 第 9 题。她写
`is only effective **within a limited scope** ／ **under a narrow range of conditions**`，
两个都成立，然后当场点名：「这个在小范围需要新建一个条目学习」（§2③）。

**我错在哪**
她这次没有错，两个说法都造得出母语者句子。
建号理由是 §2③。她缺的是**分工**：她一口气给了两个，说明是在"哪个听起来像"里挑，
不是按"我限定的是规模还是情形"来选。四条路一分开，选择就变成一步判断。

**中文触发点**
这个做法在小范围里行得通，推到全国就未必。

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）D3 学习日 C2·组3 第 9 题
  查重（§3.5 B0）：grep 了 `scope` `scale` `范围`，全档命中两处，逐条比对：
  · #0030（out of scope of doctors → beyond the scope of a doctor，🎓）—— 管的是那**一个固定块**
    的介词与冠词，改正动作是修块；本条管的是四族说法怎么选 ⇒ 问 1 不成立
  · #0169（rest on individual experience rather than large-scale trials）—— large-scale 只是
    例句里出现的一个词，那条的规则是"个案经验 vs 大规模试验"这个对比块 ⇒ 问 2 不成立
  又比对了 #0253（conditions 用 under / cases 用 in）：那条管介词，本条管选哪族名词，
  两条串联使用而不是同一条 ⇒ 不合并。
  ⇒ 新建。建号时无对错，连对连错都是 0。
- 2026-08-22 ✅ D4 复习日 C2·组5 第 6 题　**建号后第一次被测**
  题面「这个做法在小范围里行得通，推到全国就未必」，她写
  `the method is only effective **on a small scale**, but it may not necessarily work when applied across the country`。
  四条路里挑对了**规模**那一条（中文说的正是"多大摊子"）⇒ 命中，连对 1。
  📋 `may not necessarily` 不判错（母语者常用）。
  ⚠️ 同句里 #0109（已 🎓）走了 `is only effective` 那条路 —— **判为不复发、不降级**：
  　 本题是本条的题面，没有点名"用一个动词"，而 #0109 08-20 的判词已经写死
  　「中文『管用』同时通向 work 和 be effective，光靠中文永远逼不出」⇒ 属 ◎ 情形。
  　 但留痕：她**同一句里前半 be effective、后半 work**，两条路各走一次 ——
  　 会走，没有"优先用动词"的偏好 ⇒ #0109 的毕业成色可疑，收进 §8④ 积压②。
  📋 更好：`The method **works** on a small scale, but it may not work once it is **rolled out nationwide**.`
- 2026-08-23 ✅ D1 学习日 C3·组3 第 10 题　**连对 2 ⇒ 🎓**
  题面（**零提示**）「这种疗法只在少数几种情况下管用，目前还只限于两个试点城市在用。」她写
  `this therapy only works **in a few specific cases** and **is limited to** two pilot cities`。
  ★ **一题两条路同时落地，而且两条都挑对了**：
  ```
  前半「在少数几种情况下」＝ 限定的是**情形** ⇒ **in … cases** ✅
      （不是 scale —— 中文说的不是"多大摊子"；这正是本条硬边①要分的那一刀）
  后半「只限于两个试点城市」＝ 限定的是**边界** ⇒ **be limited to** ✅
      （本条第三条路，正文里写着的成员）
  ⇒ 一句话里"情形"和"边界"分得清清楚楚 ⇒ 命中，连对 2。
  ```
  📋 `speficic` → `specific`，非词拼写，§3.2 复习组豁免（⚠️ 作文里照记）。
  📋 更好：`is **currently** limited to two pilot cities`——中文「**目前还**只限于」带一层时间边界。
  　 ⚠️ 这一处**不记 #0126**：`is limited to two pilot cities` 与"目前如此、以后可能扩大"
  　 　 并不矛盾，只是少了一层时间标记；而 08-22 的「几乎总是」写成 invariably 是**命题被改写**
  　 　（允许例外 → 无一例外）。按她 08-22 收紧的判据（删掉后命题被改写才判），本处落在不判那一侧。
  📋 句末缺句号，复习组标点手滑豁免。
- 2026-08-23 📋 D1 学习日 C3·组4 第 10 题（顺带用对）　**🎓 状态不变，不推进 streak**
  主考点是 #0126。她写 `this fee applies only during the peak season and **is limited to** a few
  main roads in the city center`。
  「仅限市中心的几条主干道」＝ 限定的是**边界** ⇒ 第三条路 `be limited to` 又一次自发用对，
  而且是**毕业后第一次在没有任何提示的语境里复现**（同一天内第二次，上一次是组3 的主考点）。
  ⇒ 留痕，不推进（§3.2 留痕符号）。

## #0277 guaranteed / proven / established 这类过去分词当前置定语
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F06

**问题是什么**
过去分词可以直接放到名词前面当形容词用，一个词顶一个从句：
```
a **guaranteed** path      ＝ a path that is guaranteed to work
**proven** methods         ＝ methods that have been proven
**established** practice   ＝ practice that has been established
**qualified** teachers · **skilled** workers · **written** evidence · **spoken** English
```
**判据**：这个分词描述的是**名词的状态**（被…过的）⇒ 前置；
描述的是**正在进行的动作** ⇒ 用 -ing（`a growing problem` · `rising costs`）。
★ 作文里最好用的一批：guaranteed · proven · established · qualified · skilled ·
　accepted（accepted wisdom 公认的看法）· so-called · long-term / short-term。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错** —— 这一处是她自己主动够出来的新表达，用法成立。
建号理由是 §2③（她点名要学）。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
公认的做法是先做小规模试点。（"公认的"用一个过去分词直接放名词前面）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `guaranteed` `过去分词` `前置定语`，F06 现有 18 条（#0097–#0113 等）全是形容词副词互换与比较级构形，没有一条讲分词作定语 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组4 第 6 题　**建号后第一次被测**
  题面「公认的做法是先做小规模试点」，她写 `the **acknowledged** method is to do it on a small scale`。
  ★ **结构命中**：过去分词直接坐在名词前面，没有退回 `the method that everyone acknowledges` 这类从句。
  ⚠️ 词选偏了一格（不在本条扣分，本条管的是结构）：
  　`acknowledged` 多用于**人**（the acknowledged expert / the acknowledged leader）；
  　「公认的做法」的默认搭配是 `the **established** practice` ／ `the **accepted** approach`。
  📋 `to do it` 的 it 在单句里无所指 —— 复习组允许，作文里会记。
  📋 更好：`The **established practice** is to start with a **small-scale pilot**.`
  ★★ 同日对照（很重要）：本题是**前置**分词定语、同组 Q2 `the effort **required** to adapt` 是**后置**分词定语，
  　 两个位置同一天都对 ⇒ **分词作定语这一族她其实是通的**，缺的是**选哪个分词**（词汇，不是句法）。
- 2026-08-23 ✅ D1 学习日 C3·组6 第 6 题　**连对 2 ⇒ 🎓 毕业。这次连"选哪个分词"也对了**
  题面（零提示，换场景）「大多数人更想要一份有保障的收入，而不是看运气的提成。」，她写
  `most people prefer **a guaranteed income** over a commission than depends on luck`。
  ★ 结构命中：过去分词直接坐在名词前，没退回 `an income that is guaranteed` 这类从句 ⇒ 连对 2。
  ★★ 与 08-22 的差别值得记：那次结构对、**词选偏了一格**（acknowledged 多用于人）；
  　 今天 `guaranteed income` 是这个位上的**标准搭配**（guaranteed income / guaranteed minimum wage）
  　 ⇒ 上次判词里写的"缺的是选哪个分词"，这一次没有再犯。
  ❌ 同句一处顺带用错，不在本条扣分：`a commission **than** depends on luck` → `**that** depends on luck`
  　 ⇒ 记 #0095（拼成另一个真词、自己扫不出来）。**⛔ 不豁免** ——
  　 §3.2 写死"拼成另一个真词的不豁免"，than 是真词。
  　 ⚠️ 这一处还带一层机制：她前面写的是 `prefer X **over** Y`（正确），
  　 而"prefer … than"是中式高频错搭 ⇒ 很可能是**那个错误框架反过来污染了关系代词**。
  📋 顺带用对：`prefer X over Y` 介词正确（不是 prefer X than Y）。
  📋 更好：`Most people would rather have **a guaranteed income** than **commission that depends
  　 on luck**.`（would rather A than B 是这句中文的对称结构；commission 作"提成"时通常不可数）

## #0278 proactive / reactive 这一对，以及"主动地"的四个词
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F06
⚠️🔍 **REVIEW 池**（靠 ◎✅ 到线；**reactive 从建号到毕业一次都没出场**，两次都被从句绕过）

**成员出题账**
```
① proactive     2026-08-22 组6 题面「与其等问题出了再补救，不如提前介入」⇒ ✅
② reactive      2026-08-22 组6 ⇒ 未落地（她走 `fixing problems after they arise`）
                2026-08-23 组3 ⇒ 未落地（她走 `who only react after things go wrong`）
                ★ 两次都被关系从句绕开 —— 这一对的"负面那半边"是真正没练到的
③ proactively / actively / deliberately / consciously　四个副词一个都没出过
```

**问题是什么**
```
proactive   提前动手、不等问题发生     `a **proactive** approach` · `act **proactively**`
reactive    出了事才反应              `a **reactive** policy`（含贬义）
★ 这一对是 T2 里非常好用的对举：`Governments tend to be reactive rather than proactive.`
```
"主动地"四个词，别混：
```
proactively   提前地、防患于未然（时间维度）  `**proactively** take risks` ＝ 不等被逼就先冒险
actively      积极地、投入地（力度维度）      `**actively** seek new opportunities`
deliberately  有意地、故意（意图维度）        `**deliberately** avoid the topic`
consciously   自觉地、清醒地（意识维度）      `**consciously** limit screen time`
```
**判据**：你要强调的是**时间早**（proactively）、**用力大**（actively）、
**是故意的**（deliberately）、还是**心里清楚**（consciously）？四选一，不能互换。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错** —— 这一处是她自己主动够出来的新表达，用法成立。
建号理由是 §2③（她点名要学）。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
政府应该提前介入，而不是等问题出现了再来补救。（"提前介入"用 proactive 那个词族）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `proactiv`，全档零命中；与 #0267（程度副词强度刻度）不同 —— 那条按强弱排，本条按**语义维度**分，问 2 不成立 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组6 第 4 题　**建号后第一次被测**
  题面「与其等问题出了再补救，不如提前介入。（★「提前介入的」和「出了事才反应的」是一对形容词，用那一对）」
  ——★ **改写过的题面**：存档那条括号里直接写着「用 proactive 那个词族」，等于给答案，已去掉。
  她写 `Rather than fixing problems after they arise, it is better to take a **proactive** approach`。
  ★ 零提示下调出了这一对里**难的那个** ⇒ 命中，连对 1。
  ⚠️ 另一半 `reactive` 没出场（她用 `fixing problems after they arise` 从句绕过）——
  　 句子完全成立、不是错，但这一对只行使了一半 ⇒ **收进 §8④ 积压①**。
  　 下次题面改成两半对举：「…的做法叫【 】，…的做法叫【 】」，逼出正对照。
  📋 更好：`Rather than **reacting to** problems after they arise, …`（两个词形成正对照）
- 2026-08-23 **◎✅** D1 学习日 C3·组3 第 7 题　**算对，连对 2 ⇒ 🎓 ＋ 进 REVIEW 池**
  题面（**零提示**，本条连对 1 ⇒ 按新规则不给任何提示）
  「出了事才反应的家长，比不上那些提前动手的家长。」她写
  `parents **who only react after things go wrong** cannot match those **who take action in advance**`。
  ★ **为什么算对**：句子完全成立、完全符合题面 —— `cannot match` ＝ 比不上，母语者句造得出三个
  　（`Their squad cannot match ours.` / `No copy can match the original.` / `Few firms can match
  　 their delivery times.`）；中文的两半意思都送到了 ⇒ §3.2 的两个 ❌ 理由都不成立。
  ⚠️ **没被行使的**：`reactive` 与 `proactive` 这一对形容词一个都没出场 —— **连着两次**。
  ★★ **教练侧的账（题面缺陷，本条第二次栽在同一个地方）**：
  ```
  08-22 的题面「出了事再补救 / 提前介入」是**动词短语**形状 ⇒ 她照着写从句
  08-23 的题面「出了事才反应的家长」是**关系从句**形状 ⇒ 她更是直接写从句
  ⇒ 中文只要写成"…的人"，英文最省事的路永远是 who 从句，形容词那条路可以整个绕开。
  ⇒ 改法：中文必须把这两个词写成**贴在名词前的标签**，让从句无路可走。
  ```
  ⇒ 存档新题面见下方 REVIEW 池条目与 `review_pool.md`。
  📋 顺带用对 **#0301**（in advance / beforehand / in anticipation）：`take action **in advance**`
  　 用得准（📋 留痕不推进 —— 她是自发用出来的，按 §6 自发块挂作文验）。

**★ REVIEW 池存档题面（她 review 时用这条）**
```
提前动手的做法叫【 】，出了事才反应的做法叫【 】；后一种迟早要吃亏。
（★ 两个空都必须填一个**形容词**，⛔ 不许改写成 who／that 从句，⛔ 不许用动词短语）
另一条没练过的：四个"主动地"——
备用题面：他不是被逼的，是**有意**回避这个话题；而她只是**积极**争取机会，两回事。
（★ 前一个用 deliberately，后一个用 actively）
```

---

## #0333 in-house 一族：自己做 vs 外包，形容词与副词同形
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F06

**问题是什么**
`in-house` 一个词同时是**形容词**和**副词**，两个位置都带连字符：
```
形容词（贴在名词前）  `an **in-house** team` · `**in-house** training` · `**in-house** counsel`
副词（贴在动词后）    `they hire **in-house**` · `we do it **in-house**` · `stopped recruiting **in-house**`
⛔ `~~in house~~` 分写 · ⛔ `~~inhouse~~` 连写 —— 只有带连字符这一种写法
⛔ 副词位置不能加介词：`~~hire in in-house~~` `~~do it by in-house~~`
```
**这一族（自己做 ↔ 外包，成对背最省）**
```
自己做   in-house              `keep it **in-house**` ＝ 不外包，自己内部消化
         internally            `handled **internally**`（最中性，不带连字符）
外包     outsource（动词）      `**outsource** the work to a supplier` ★ 及物，配 to
         outsourcing（名词）    `the **outsourcing** market` · `**outsourcing** costs`
         outsourced（形容词）   `an **outsourced** service`
第三方   third-party（形容词）  `a **third-party** supplier`　⛔ 只作定语，不作副词
         a third party（名词）  `handled by **a third party**`（作名词时不带连字符）
自由职业 freelance             形容词与副词同形，同 in-house：`work **freelance**`
```
**判据**：说"这件事在公司内部做"⇒ 副词 in-house；修饰后面的名词 ⇒ 形容词 in-house；
说"交出去做"⇒ 动词 outsource；说"外包这件事本身"⇒ 名词 outsourcing。
⚠️ **连字符的通则**（这一族最容易掉的零件）：
```
third-party supplier ✅（定语位，连字符）　／　a third party ✅（名词位，无连字符）
full-time job ✅　／　works full time ⚠️（副词位英式常无连字符，美式 full-time 也可）
★ in-house 是例外：形容词位、副词位**都要**连字符。记这一个例外就够。
```

**怎么发现的**
2026-08-23　D1 学习日 C3·组3 第 8 题（主考点 #0318）。她写
`many companies have simply stopped hiring **in-house**` —— 用法完全正确，
然后当场点名：「**这个 in-house 可以建个条目练习下**」（§2③）。

**我错在哪**
她这次**没有错**，`hiring in-house` 副词用法、连字符都对。
建号理由是 §2③（她点名要学）。缺口在于**这一族的其余成员**和**形容词/副词两个位置的分工**。
查重（§3.5 B0）：全档（problems.md ＋ graduated.md）grep 了 `in-house` `in house` `outsourc`
`third-party` `freelance`，**零条目命中**（唯一一处出现是 #0318 更好版里的 `recruiting in house`）。
又逐条比对了 F06 里最近的两条：#0277（guaranteed/proven/established 过去分词作前置定语）——
那条管的是**过去分词能不能当定语**，本条管的是**同一个词兼形容词与副词**，问 2 不成立；
#0278（proactive/reactive）—— 那条是一对反义形容词的语义分工，本条是一个词的两个词类位置，
问 1 不成立 ⇒ **新建**。

**中文触发点**
这家公司的培训一直是自己做的，只有法务外包给了第三方。

**成员出题账**
```
① in-house（副词）    2026-08-23 组3 自发用对（📋 不推进）—— 按 §6「自发块挂作文验」，
　                    单点题优先测其他成员
② in-house（形容词）  未出过
③ outsource（动词）   未出过
④ outsourcing（名词） 2026-08-23 组3 自发用对（📋 不推进）
⑤ third-party         未出过
⑥ internally          未出过
```

### 历史记录
- 2026-08-23 ③ 建号（她点名要学）D1 学习日 C3·组3 第 8 题
  她自发写出 `stopped hiring **in-house**`（副词位 ＋ 连字符，全对）、
  同句还写对了 `the **outsourcing** market`（名词位）。
  ⇒ 建号时无对错，连对连错都是 0。
  ★ 出题纪律：本条是**词表型**，一题必须让 ≥2 个成员落地（§3.5 第 3.5 步）。
  ⇒ 成员出题账已挪到上方条目正文（2026-08-24 格式统一，内容一字未改）。

---

# F07 句法/逗号/并列

> 逗号粘连、并列同形、语序倒装、从句、指代、大小写

## #0089 这意味着大多数人住在曼哈顿以外
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F07

**问题是什么**
P12 句法＋P5 拼写（挂主错 P12）　R · P12

**怎么发现的**
2026-08-16　复习日 C1·组7

**我错在哪**
她的：which **meat the majority of people living** outside
正确：which **meant that** the majority of people **lived** outside（原句缺谓语，闭合不了）

**中文触发点**
这意味着大多数人住在曼哈顿以外

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组7

<details><summary>原始行（旧表逐字，旧号 E-164）</summary>

`这意味着大多数人住在曼哈顿以外|which **meat the majority of people living** outside|which **meant that** the majority of people **lived** outside（原句缺谓语，闭合不了）|P12 句法＋P5 拼写（挂主错 P12）|R · **P12**|`

</details>

## #0117 In Conclusion → In conclusion
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-11 ｜ 族 F07

**问题是什么**
GRA 大小写（★ 只进 GRA 桶，不进 LR，见 scoring §2.0）　R · 挂代号 P12

**怎么发现的**
2026-08-11　迷你复习

**我错在哪**
她的：**In Conclusion**
正确：**In conclusion**

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— 考点是句中首字母大小写（In Conclusion → In conclusion），
中译英答案里的大小写按 §3.2 一律豁免 ⇒ 只有作文里才判得了。

### 历史记录
- 2026-08-11 ✅ 迷你复习

<details><summary>原始行（旧表逐字，旧号 E-018）</summary>

`总而言之|**In Conclusion**|**In conclusion**|GRA 大小写（★ 只进 GRA 桶，不进 LR，见 scoring §2.0）|R · 挂代号 **P12**|**1/3 · ✅D—迷你复习**|`

</details>

## #0118 it 直接回指上一句 → this demand —— 用名词回指，不用光杆 it
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-11 ｜ 族 F07

**问题是什么**
🟡 留痕　留痕

**怎么发现的**
2026-08-11　迷你复习

**我错在哪**
她的：`it` 直接回指上一句
正确：`this demand` —— **用名词回指，不用光杆 it**

**中文触发点**
更多人开始租房，这种需求推高了房价（08-11 改题面：原题面把考点「避免 it 指代不明」直接写在括号里＝提前公布）

### 历史记录
- 2026-08-11 ✅ 迷你复习

<details><summary>原始行（旧表逐字，旧号 E-035）</summary>

`更多人开始租房，这种需求推高了房价（08-11 改题面：原题面把考点「避免 it 指代不明」直接写在括号里＝提前公布）|`it` 直接回指上一句|`this demand` —— **用名词回指，不用光杆 it**|**🟡 留痕**|留痕|**1/2 · ✅D—迷你复习**|`

</details>

## #0121 what you should do next → what patients should do next
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
P12 人称一致（全篇第三人称里跳出 you）　R · P12

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：what **you** should do next
正确：what **patients** should do next

**中文触发点**
病人下一步该怎么做（★ 08-16 归类更正：考点是「**不要**在第三人称全篇里跳出 you」＝**第③类减法型**，中译英逼不出"不产出某形式" ⇒ 挂作文里验，不进中译英组。这与她 08-16「不移除、加限定」的裁决不冲突：那条针对的是题面逼不紧，本条是减法型本身没法用中译英测）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-072）</summary>

`病人下一步该怎么做（★ 08-16 归类更正：考点是「**不要**在第三人称全篇里跳出 you」＝**第③类减法型**，中译英逼不出"不产出某形式" ⇒ 挂作文里验，不进中译英组。这与她 08-16「不移除、加限定」的裁决不冲突：那条针对的是题面逼不紧，本条是减法型本身没法用中译英测）|what **you** should do next|what **patients** should do next|P12 人称一致（全篇第三人称里跳出 you）|R · **P12**|0/3|`

</details>

## #0122 保持耐心、不去赌，就更可能治好
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F07

**问题是什么**
P12 悬垂分词（本篇唯一回读句）　R · P12

**怎么发现的**
2026-08-16　复习日 C1·组5

**我错在哪**
她的：**Keeping patient…, there are** more chances
正确：**If patients stay patient…, they have** more chances

**中文触发点**
保持耐心、不去赌，就更可能治好

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组5

<details><summary>原始行（旧表逐字，旧号 E-078）</summary>

`保持耐心、不去赌，就更可能治好|**Keeping patient…, there are** more chances|**If patients stay patient…, they have** more chances|P12 悬垂分词（本篇唯一回读句）|R · **P12**|0/3|`

</details>

## #0123 doctors would provide → doctors will provide
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F07

**问题是什么**
P12 情态（would＝虚拟/委婉）　R · P12

**怎么发现的**
2026-08-16　复习日 C1·组4

**我错在哪**
她的：doctors **would** provide
正确：doctors **will** provide

**中文触发点**
医生会给出指引（事实陈述）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组4

<details><summary>原始行（旧表逐字，旧号 E-079）</summary>

`医生会给出指引（事实陈述）|doctors **would** provide|doctors **will** provide|P12 情态（would＝虚拟/委婉）|R · **P12**|0/3|`

</details>

## #0125 rest for a more week → rest for another week
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F07

**问题是什么**
P12（"再多一个 X"＝another X / one more X）　R · P12

**怎么发现的**
2026-08-16　复习日 C1·组4

**我错在哪**
她的：rest for **a more week**
正确：rest for **another week**
★ 2026-08-22 扩写（她今天写出 `another **days** off`，把规则的第二半暴露出来）：
```
another ＋ **单数名词**            `another week` ✅ `another day` ✅
another ＋ **数词 ＋ 复数**        `another two days` ✅ `another five years` ✅
another ＋ **few ＋ 复数**         `another few days` ✅
⛔ another ＋ 光杆复数             `~~another days~~` ❌
最省事的一条路：**a few more days** ／ **two more days** —— 用 more 就不必记 another 的例外
```
**找法**：写完 another，看它后面那个名词 —— 是单数吗？不是的话，中间必须有数词或 few。

**中文触发点**
医生说他还得再休息一周，之后可能还要再多两天。（★ 两处"再"都用 another）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组4
- 2026-08-22 ❌ D4 复习日 C2·组4 第 1 题（顺带）　~~归入待确认~~ → **已于当日 §8④a 结清，见本块末**
  题面「医生建议他多休息几天」（主考点 #0018），她写 `to take **another days** off`。
  正确：`another **few** days off` ／ `**a few more** days off`。
  ⚠️ **归入待确认的理由**（§3.5 误判3）：本条原错是 `a more week`（该用 another 时用了 a more），
  　 今天是 `another days`（用对了 another 但后面配错了数）。
  　 问 1（改正动作＝把"再多 N 个 X"写成合法形状）与问 2（一句话能覆盖）成立，
  　 **问 3 存疑** —— 知道 `another week` 未必知道 `another days` 不合法。
  ★★ **2026-08-22 复习日 §8④a 结清：确认归入本条，「归入待确认」撤销。**
  　 复查过程：问 3 重判为**成立** —— 本条的规则句是「another 后面只能是**单数**，
  　 或者数词／few ＋ 复数」，真内化了这一句，看到 `days` 就知道中间必须补东西。
  　 反向验（§3.5 1.3）：**举不出**"`another week` 对、`another days` 也对"的句子
  　 （`another days` 在任何语境下都不合法）⇒ 两者不能独立取值 ⇒ 同一条，不拆。
  ★ 反向证据：档案里记过她自发写对 `take another **week** off`（迁移时登记为她的资产）
  　 ⇒ **单数那一半是稳的，复数那一半是空的**。

<details><summary>原始行（旧表逐字，旧号 E-082）</summary>

`再休息一周|rest for **a more week**|rest for **another week**|P12（"再多一个 X"＝another X / one more X）|R · **P12**|0/3|`

</details>

## #0127 现代医学有局限
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
第②类　不出中译英，作文里验

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：there are some limitations in modern medicine（**成立**）
正确：**modern medicine has its limits**（差别只是存现句→实义主语的紧致度，纯风格）<br>⇒ **08-16 改判第②类，移出中译英组** —— 中译英里产不出 ❌，只能产出假错或无意义的 ✅

**中文触发点**
现代医学有局限

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-104）</summary>

`现代医学有局限|there are some limitations in modern medicine（**成立**）|**modern medicine has its limits**（差别只是存现句→实义主语的紧致度，纯风格）<br>⇒ **08-16 改判第②类，移出中译英组** —— 中译英里产不出 ❌，只能产出假错或无意义的 ✅|第②类|不出中译英，作文里验|`

</details>

## #0132 有些中医宣称能治高血压和糖尿病，生意还很好
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F07

**问题是什么**
待排序　U（待定）

**怎么发现的**
2026-08-16　复习日 C1·组7

**我错在哪**
她的：some Chinese traditional medicine **doctors claim that they are able to cure** … their **businesses tend to be really prosperous**
正确：some traditional Chinese medicine **practitioners claim to cure** … their **clinics do very well**（① claim to do 省一个从句 ② practitioners 比 doctors 准 ③ clinics do very well 比 businesses…prosperous 自然）

**中文触发点**
有些中医宣称能治高血压和糖尿病，生意还很好

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组7

<details><summary>原始行（旧表逐字，旧号 E-148）</summary>

`有些中医宣称能治高血压和糖尿病，生意还很好|some Chinese traditional medicine **doctors claim that they are able to cure** … their **businesses tend to be really prosperous**|some traditional Chinese medicine **practitioners claim to cure** … their **clinics do very well**（① claim to do 省一个从句 ② practitioners 比 doctors 准 ③ clinics do very well 比 businesses…prosperous 自然）|待排序|U（待定）|0/2|`

</details>

## #0133 from then on（句首小写） → From then on
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
P12 大小写（08-16 归类：聊天答题里按规则 C 大小写不计 ⇒ 中译英测不出，属第③类，只在作文里验）　第③类 · 挂作文验

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`from then on`（句首小写）
正确：`From then on`

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— 考点是句首大写（from then on → From then on），
中译英答案里的大小写按 §3.2 一律豁免 ⇒ 只有作文里才判得了。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-160）</summary>

`从那以后|`from then on`（句首小写）|`From then on`|P12 大小写（**08-16 归类：聊天答题里按规则 C 大小写不计 ⇒ 中译英测不出，属第③类，只在作文里验**）|第③类 · 挂作文验|`

</details>

## #0134 1,850 thousand → 1.85 million（thousand 前面的数不过 999）
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F07

**问题是什么**
P12 数字写法　R · P12

**怎么发现的**
2026-08-16　复习日 C1·组8

**我错在哪**
她的：**1,850 thousand**
正确：**1.85 million**（thousand 前面的数不过 999）

**中文触发点**
到 1900 年，这个数字达到了 185 万。（★ 用 million 写这个数）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组8

<details><summary>原始行（旧表逐字，旧号 E-168）</summary>

`185 万|**1,850 thousand**|**1.85 million**（thousand 前面的数不过 999）|P12 数字写法|R · **P12**|`

</details>

## #0135 到 1900 年为止，这个数字已经增长到 158 万
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：The population had risen to 1.58 million by 1900
正确：**By 1900,** the population had risen to 1.58 million（T1 里时间状语前置是常态：先给时间轴再给数；**纯语序选择，第②类不进中译英组**）

**中文触发点**
到 1900 年为止，这个数字已经增长到 158 万

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-200）</summary>

`到 1900 年为止，这个数字已经增长到 158 万|The population had risen to 1.58 million by 1900|**By 1900,** the population had risen to 1.58 million（T1 里时间状语前置是常态：先给时间轴再给数；**纯语序选择，第②类不进中译英组**）|待排序|U（待定）|`

</details>

## #0136 雇主和员工的利益并不总是一致
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
P12 语序（GRA 桶）　R · P12

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：does **always not** align
正确：does **not always** align（★ `not always`＝并不总是，是固定次序，always 永远在 not 后面；`always not` 不成立）

**中文触发点**
雇主和员工的利益并不总是一致

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-204）</summary>

`雇主和员工的利益并不总是一致|does **always not** align|does **not always** align（★ `not always`＝并不总是，是固定次序，always 永远在 not 后面；`always not` 不成立）|P12 语序（GRA 桶）|R · **P12**|`

</details>

## #0140 ⭐⭐「本来想用 it is harder，但是前面用了 with 发现主语就对不上了
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
K（高价值）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：加上语言障碍，找工作更难
正确：★★ **这是误判，而且是今天最值钱的一条**：`With a language barrier, **it is even harder** to find a job.` **完全正确**，主语根本不需要对上。<br>**判据（两类前置状语，规则相反）**：<br>· **分词短语**（Combined with X, ／ Facing X, ／ Having done X,）→ **要求**主句主语＝分词的逻辑主语，否则悬垂<br>· **介词短语**（**With** X, ／ In X, ／ Despite X, ／ After X,）→ **不要求**，主句爱用什么主语就用什么，`it` 形式主语完全没问题<br>⇒ 她把分词的悬垂规则**过度泛化**到了介词短语上，因此主动放弃了正确写法、绕道 struggle，还把"更"丢了。**一个假规则造成了两处损失。**

**中文触发点**
有了语言障碍，找工作就更难了。（★ 用 With 开头，主句用 it 作形式主语）
（旧留痕：⭐⭐「本来想用 it is harder，但是前面用了 with 发现主语就对不上了」——
　她把分词的悬垂规则过度泛化到介词短语上了。介词短语前置状语**不要求**主句主语一致）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-224）</summary>

`⭐⭐「本来想用 it is harder，但是前面用了 with 发现**主语就对不上了**，就憋了一个 struggle 出来」|加上语言障碍，找工作更难|★★ **这是误判，而且是今天最值钱的一条**：`With a language barrier, **it is even harder** to find a job.` **完全正确**，主语根本不需要对上。<br>**判据（两类前置状语，规则相反）**：<br>· **分词短语**（Combined with X, ／ Facing X, ／ Having done X,）→ **要求**主句主语＝分词的逻辑主语，否则悬垂<br>· **介词短语**（**With** X, ／ In X, ／ Despite X, ／ After X,）→ **不要求**，主句爱用什么主语就用什么，`it` 形式主语完全没问题<br>⇒ 她把分词的悬垂规则**过度泛化**到了介词短语上，因此主动放弃了正确写法、绕道 struggle，还把"更"丢了。**一个假规则造成了两处损失。**|**K**（高价值）|`

</details>

## #0141 在这两种办法之间，这一种最安全、也最快
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
P12 语序（降档：❌→⚠️，介词部分撤销）　R · P12

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：safer and quicker **between the two**（**句末**）
正确：★★ **08-16 当场改判（她质疑"between 也能用吧"，成立）：错的是【位置】不是【介词】。**<br>✅ `**Between the two,** this one is safer and quicker.`（她的介词，移到句首即可）<br>✅ `**Of the two,** this one is safer and quicker.`（偏书面）<br>✅ `This one is **the safer and quicker of the two**.`（★ 这个固定结构里只能用 of）<br>❌ 只有把 `between the two` 挂句末当状语不成立<br>★ 语域差：of the two 偏书面；between the two 稍口语、强调"在两者间做选择"，常配 choose/pick/prefer<br>⛔ 教练原判据「比较范围用 of 不用 between」**过度概括，已撤销**

**中文触发点**
在这两种办法之间，这一种最安全、也最快

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-233）</summary>

`在这两种办法之间，这一种最安全、也最快|safer and quicker **between the two**（**句末**）|★★ **08-16 当场改判（她质疑"between 也能用吧"，成立）：错的是【位置】不是【介词】。**<br>✅ `**Between the two,** this one is safer and quicker.`（她的介词，移到句首即可）<br>✅ `**Of the two,** this one is safer and quicker.`（偏书面）<br>✅ `This one is **the safer and quicker of the two**.`（★ 这个固定结构里只能用 of）<br>❌ 只有把 `between the two` 挂句末当状语不成立<br>★ 语域差：of the two 偏书面；between the two 稍口语、强调"在两者间做选择"，常配 choose/pick/prefer<br>⛔ 教练原判据「比较范围用 of 不用 between」**过度概括，已撤销**|P12 语序（**降档：❌→⚠️，介词部分撤销**）|R · **P12**|`

</details>

## #0144 ⭐⭐「as 也是学的重点，老想不到；第二句也很少想到，实义动词推动；第三个也是没想到
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
K（她点名，高价值）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：材料涨价后，总成本就上去了（＝一切"因为…所以…"）
正确：★★ **这是「因果/伴随」的四条路，她的默认是最长最绕的那条**：<br>　默认　`The total cost goes up **because** materials are more expensive.` (11 词)<br>　① `**As** material prices rise, the total cost goes up.` (9)<br>　② `Higher material prices **push up** the total cost.` (8) ← **最紧**<br>　③ `**With** material prices rising, the total cost goes up.` (9)<br>**① as ＝「随着」＋「因为」两层一起**，比 because 省一半、更书面。同族：when（条件）· once（一旦）· the moment（一…就）。<br>　T2 直接能用：`**As the population ages**, …` · `As incomes rise, demand grows.`<br>**② 实义动词推动 ＝ 把原因做成主语，Band 7→8 的分水岭**（不用从句，一个动词扛起因果）。<br>　六个动词：**push up / drive up**（推高）· **cut / reduce**（削减）· **trigger**（引发）· **fuel**（助长）· **ease**（缓解）· **offset**（抵消）<br>　例：`An ageing population **drives up** healthcare spending.` · `Better public transport **eases** traffic congestion.`<br>**③ with ＋ doing** ＝ 她今天刚自查出的 E-224（介词短语**不**要求主语一致，主句可用 it）。<br>★ 她自评"③句型会、没想到 rise" ⇒ **不是结构缺口是动词没调出来**，与 E-212/E-213（steadily/decline）同池：`prices **rise/climb/soar**` · `prices **fall/drop/slide**`

**中文触发点**
原材料价格一涨，总成本就跟着上去。（★ 用 As 开头那条路，一个词把"随着"和"因为"两层一起送到）
（旧留痕：⭐⭐「as 也是学的重点，老想不到…实义动词推动…没想到 rise」——
　因果四条路里她默认走最长的 because，这题只测 as 那条）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-263）</summary>

`⭐⭐「as 也是学的重点，**老想不到**；第二句也**很少想到**，实义动词推动；第三个也是**没想到 rise**，句型是会的」|材料涨价后，总成本就上去了（＝一切"因为…所以…"）|★★ **这是「因果/伴随」的四条路，她的默认是最长最绕的那条**：<br>　默认　`The total cost goes up **because** materials are more expensive.` (11 词)<br>　① `**As** material prices rise, the total cost goes up.` (9)<br>　② `Higher material prices **push up** the total cost.` (8) ← **最紧**<br>　③ `**With** material prices rising, the total cost goes up.` (9)<br>**① as ＝「随着」＋「因为」两层一起**，比 because 省一半、更书面。同族：when（条件）· once（一旦）· the moment（一…就）。<br>　T2 直接能用：`**As the population ages**, …` · `As incomes rise, demand grows.`<br>**② 实义动词推动 ＝ 把原因做成主语，Band 7→8 的分水岭**（不用从句，一个动词扛起因果）。<br>　六个动词：**push up / drive up**（推高）· **cut / reduce**（削减）· **trigger**（引发）· **fuel**（助长）· **ease**（缓解）· **offset**（抵消）<br>　例：`An ageing population **drives up** healthcare spending.` · `Better public transport **eases** traffic congestion.`<br>**③ with ＋ doing** ＝ 她今天刚自查出的 E-224（介词短语**不**要求主语一致，主句可用 it）。<br>★ 她自评"③句型会、没想到 rise" ⇒ **不是结构缺口是动词没调出来**，与 E-212/E-213（steadily/decline）同池：`prices **rise/climb/soar**` · `prices **fall/drop/slide**`|**K**（她点名，高价值）|`

</details>

## #0147 ① 随着老年人口增长 ② 几个月正规治疗仍没好转
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：① as **the population of older people is growing** ② **haven't seen any** improvement
正确：① as **the older population grows**（名词块更紧；as 从句表持续趋势用一般现在时更常见）② **have shown no** improvement（show 在此搭配里比 see 常见；她的成立）

**中文触发点**
① 随着老年人口增长 ② 几个月正规治疗仍没好转

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-274）</summary>

`① 随着老年人口增长 ② 几个月正规治疗仍没好转|① as **the population of older people is growing** ② **haven't seen any** improvement|① as **the older population grows**（名词块更紧；as 从句表持续趋势用一般现在时更常见）② **have shown no** improvement（show 在此搭配里比 see 常见；她的成立）|待排序|U（待定）|`

</details>

## #0148 长期治疗没有带来明显的改善
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
🟢 她写得出（brings/shows 都在她词汇内，缺的是"把无生命名词放主语"这一步）　U · 待排序

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`there isn't any significant improvement after long-term treatment`
正确：`Long-term treatment **brings** no significant improvement.` ／ `Patients **show** no significant improvement even after long-term treatment.`

**中文触发点**
**长期治疗没有带来明显的改善**（08-18 新建；与 E-062 同语义但换主语位——E-062 测"别硬编 fail to get positive effects"，本条测**别用 there-be 起句**）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-277）</summary>

`**长期治疗没有带来明显的改善**（08-18 新建；与 E-062 同语义但换主语位——E-062 测"别硬编 fail to get positive effects"，本条测**别用 there-be 起句**）|`there isn't any significant improvement after long-term treatment`|`Long-term treatment **brings** no significant improvement.` ／ `Patients **show** no significant improvement even after long-term treatment.`|🟢 她写得出（brings/shows 都在她词汇内，缺的是"把无生命名词放主语"这一步）|U · 待排序|0/2|`

</details>

## #0149 ⭐⭐ 「把无生命名词放主语位」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
K → drill（08-18 当场上）　0/2

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：**「把无生命名词放主语位 这个特别缺，和实义动词一样经常想不到」**
正确：她自己把两件事并成一件：**无生命主语 ＋ 实义动词推动 ＝ 同一个动作的两半**。中文默认「人/机构 做主语」，英语议论文默认「事物/原因 做主语 ＋ 一个实义动词推动」。<br>· 与 [[E-263]]（08-16 她说"实义动词推动**很少想到**"）**是同一条缺口的两个号** ⇒ 合并成一个 drill 点<br>· 也是 E-277（there-be 起句 → `Long-term treatment brings no…`）的上位规则<br>· ★ 判定为 §2.1b 的**第①类「底层的」＋第③类「知识缺失」** ⇒ **该 drill**（不是靶子）：一条规则管很多句，且她低压孤立也调不出<br>· ⚠️ **不许滑成 P3 硬编**：转主语 ≠ 造名词块。`The leaving-school time of students causes…` 是老病复发

**中文触发点**
这项新规定把不少小公司挤出了市场。（★ 让"这项新规定"直接作主语，配一个实义动词推动）
（旧留痕：⭐⭐「把无生命名词放主语位」08-18 她主动点名 —— 与"实义动词推动"是同一条缺口的两半。
　⚠️ 不许滑成造名词块：转主语 ≠ 硬编 P3 名词块）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-280）</summary>

`⭐⭐ **「把无生命名词放主语位」**（08-18 她主动点名）|**「把无生命名词放主语位 这个特别缺，和实义动词一样经常想不到」**|她自己把两件事并成一件：**无生命主语 ＋ 实义动词推动 ＝ 同一个动作的两半**。中文默认「人/机构 做主语」，英语议论文默认「事物/原因 做主语 ＋ 一个实义动词推动」。<br>· 与 [[E-263]]（08-16 她说"实义动词推动**很少想到**"）**是同一条缺口的两个号** ⇒ 合并成一个 drill 点<br>· 也是 E-277（there-be 起句 → `Long-term treatment brings no…`）的上位规则<br>· ★ 判定为 §2.1b 的**第①类「底层的」＋第③类「知识缺失」** ⇒ **该 drill**（不是靶子）：一条规则管很多句，且她低压孤立也调不出<br>· ⚠️ **不许滑成 P3 硬编**：转主语 ≠ 造名词块。`The leaving-school time of students causes…` 是老病复发|**K → drill（08-18 当场上）**|0/2|`

</details>

## #0150 有些病人已经好几年没有任何好转
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
P12 句法（否定只放一处）　R · P12

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：have not showed / seen **no** improvement
正确：两条路各自成立，**不能拼在一起**：<br>✅ `have not shown **any** improvement`（否定在助动词上 → 后面用 any）<br>✅ `have **seen no** improvement`（否定在名词上 → 助动词不带 not）<br>❌ `have **not** shown **no** improvement`＝双重否定，意思反了

**中文触发点**
**有些病人已经好几年没有任何好转**（同一句里两条路不许混）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-283）</summary>

`**有些病人已经好几年没有任何好转**（同一句里两条路不许混）|have not showed / seen **no** improvement|两条路各自成立，**不能拼在一起**：<br>✅ `have not shown **any** improvement`（否定在助动词上 → 后面用 any）<br>✅ `have **seen no** improvement`（否定在名词上 → 助动词不带 not）<br>❌ `have **not** shown **no** improvement`＝双重否定，意思反了|P12 句法（否定只放一处）|R · **P12**|0/3|`

</details>

## #0151 随着老年人口增长，医疗支出也在上升
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
⚠️ 不地道（她那句语法成立）　U · 待排序

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`as the number of older people **is growing**, medical spending **rises**`
正确：**体要平行** —— 一个从句用进行、一个主句用一般现在，读起来时间轴晃：<br>✅ `As the older population **grows**, medical spending **rises**.`（都一般现在，讲通则，议论文默认）<br>✅ `As the older population **is growing**, medical spending **is rising**.`（都进行，讲眼下）<br>★ 另附：`the number of older people` → `the older population` 更简（少一层 of 结构）

**中文触发点**
**随着老年人口增长，医疗支出也在上升**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-293）</summary>

`**随着老年人口增长，医疗支出也在上升**|`as the number of older people **is growing**, medical spending **rises**`|**体要平行** —— 一个从句用进行、一个主句用一般现在，读起来时间轴晃：<br>✅ `As the older population **grows**, medical spending **rises**.`（都一般现在，讲通则，议论文默认）<br>✅ `As the older population **is growing**, medical spending **is rising**.`（都进行，讲眼下）<br>★ 另附：`the number of older people` → `the older population` 更简（少一层 of 结构）|⚠️ 不地道（她那句语法成立）|U · 待排序|0/2|`

</details>

## #0153 这些疗法不仅浪费时间，还有实际的危害
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
⚠️ 不地道　U · 待排序

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`not only **a waste of time**（名词短语）but also **actively damaging**（形容词短语）`
正确：★ **not only … but also … 两边要同形**：<br>✅ 形＋形：`not only **wasteful** but also actively damaging`<br>✅ 名＋名：`not only **a waste of time** but also **a real danger**`<br>⚠️ 她那句 be 动词后名词/形容词都接得上，**语法站得住**，只是不齐 —— IELTS 的 GRA 看这个<br>★ 与 [[E-003]]（`and be` 那条）同族：**并列结构两边同形**。E-003 判她冗余不算错，本条同理判 ⚠️ 不判 ❌

**中文触发点**
**这些疗法不仅浪费时间，还有实际的危害**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-300）</summary>

`**这些疗法不仅浪费时间，还有实际的危害**|`not only **a waste of time**（名词短语）but also **actively damaging**（形容词短语）`|★ **not only … but also … 两边要同形**：<br>✅ 形＋形：`not only **wasteful** but also actively damaging`<br>✅ 名＋名：`not only **a waste of time** but also **a real danger**`<br>⚠️ 她那句 be 动词后名词/形容词都接得上，**语法站得住**，只是不齐 —— IELTS 的 GRA 看这个<br>★ 与 [[E-003]]（`and be` 那条）同族：**并列结构两边同形**。E-003 判她冗余不算错，本条同理判 ⚠️ 不判 ❌|⚠️ 不地道|U · 待排序|0/2|`

</details>

## #0155 星期五之前把报告交上来
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F07

**问题是什么**
U · 待排序　0/2

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：「(before friday) **要不要加个 this**」（08-16 提的，今天出题结算）
正确：**不用加。默认就指最近的那个周五。**<br>　✅ `Hand in the report **by Friday**.`<br>　· `this Friday` 只在**需要跟别的周五对比**时用（"是这周五不是下周五"）<br>　· 平铺直叙时加 this 反而显得在强调，读者会去找被对比的那一个<br>★ 顺带两层（她这次的写法带出来的）：<br>　① **by ＞ before**：`by Friday`＝不迟于周五（含周五）· `before Friday`＝周五之前（不含）。"之前交上来"的实际意思几乎总是 by<br>　② **星期几、月份、专有名词必须大写**：Friday / Monday / March（本场记 `friday`，按规则 C 聊天大小写豁免，但**作文里计入 GRA**）

**中文触发点**
**星期五之前把报告交上来**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-323）</summary>

`**星期五之前把报告交上来**|「(before friday) **要不要加个 this**」（08-16 提的，今天出题结算）|**不用加。默认就指最近的那个周五。**<br>　✅ `Hand in the report **by Friday**.`<br>　· `this Friday` 只在**需要跟别的周五对比**时用（"是这周五不是下周五"）<br>　· 平铺直叙时加 this 反而显得在强调，读者会去找被对比的那一个<br>★ 顺带两层（她这次的写法带出来的）：<br>　① **by ＞ before**：`by Friday`＝不迟于周五（含周五）· `before Friday`＝周五之前（不含）。"之前交上来"的实际意思几乎总是 by<br>　② **星期几、月份、专有名词必须大写**：Friday / Monday / March（本场记 `friday`，按规则 C 聊天大小写豁免，但**作文里计入 GRA**）|U · 待排序|0/2|`

</details>

## #0279 把否定放到宾语上，比放到谓语上紧
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F07

**问题是什么**
同一个意思两种写法，**否定挂在宾语上的那种更短更有力**，是书面英语的默认：
```
✅ `walking it **yields no more than** what others gain`
⚠️ `walking it **does not yield more than** what others gain`（长、软）
✅ `a certificate that anyone can get **offers no real advantage**`
⚠️ `a certificate that anyone can get **does not offer any** real advantage`
```
常用的否定宾语块：`no advantage` · `no evidence` · `no guarantee` · `no real difference` ·
`little effect` · `few options` · `no more than X` · `nothing but X`
**判据**：句子里出现 `not … any` 时，试着把 not 和 any 合成 no 挪到宾语位置。
⛔ 一句里只能否定一次：`~~does not offer no advantage~~`（双重否定，意思反了 —— 见 #0192 附近那条）

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③（她点名要学）。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
这类培训对老员工没有任何实际帮助。（把"没有"挂在宾语上，别用 does not… any）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `否定` `no more than`，全档只有一条讲双重否定（否定只放一处），改正动作是**删掉一个否定**；本条是**把否定挪位置**，问 1 不成立 ⇒ 新建。
- 2026-08-22 ❌ D4 复习日 C2·组2 第 10 题　**答不出（整句没写出来，不是写错）**
  题面「换句话说，如果你什么都不做，情况只会更糟」，她的回答是「**不会**」。
  目标句：`**In other words, if you do nothing, things will only get worse.**`
  ★ 本条的考点只在 `do nothing` 这三个字母的位置上：
  　✅ `if you **do nothing**`（否定挂在宾语上，三个词）
  　⚠️ `if you **don't do anything**`（否定挂在谓语上，四个词，软）
  ★ 建号时她自己把这一处标了「新」，说明**看得懂**；今天要她产出整句时整句都没出来
  　 ⇒ 和 #0286 今天的表现同一个形状：**recognition 有、retrieval 没有**。
  ⚠️ 这一句只有十个词、三个成分（In other words ／ if 从句 ／ 主句），她说"不会"⇒
  　 下次要把这条拆成半句题（只给「你什么都不做」四个字）先测最小单位，再合回整句。
- 2026-08-23 ✅ D1 学习日 C3·组1 第 4 题　**按上一行的处置拆成最小单位，一次就出来了**
  题面「政府在这件事上什么都没做。（★ "什么都没做"必须写成「主语 ＋ 动词 ＋ 一个宾语」三个词，
  把"没有"这一层放进宾语那个词里）」
  她写 `the government **did nothing** on it`。
  ★ `did nothing` —— 三个词，否定挂在宾语上 ⇒ 考点命中，连对 1、连错归 0。
  ★★ **08-22 的结论被推翻了一半**：当时判「整句答不出」，读作 retrieval 失败；
  　 今天把同一个成分单独拿出来，她**零犹豫写对**。
  　 ⇒ 真正卡住她的不是 `do nothing` 这三个词，是 08-22 那道题的**整句装配**
  　 　（In other words ／ if 从句 ／ 主句 三段同时要）。
  　 ⇒ 处置：本条按最小单位已经过关；**整句装配另算**，等它自己长出证据再决定要不要建号。
  ★ 第 7 题她还**自发**用了一次同一形状：`has seen **no growth**`（否定挂宾语）——
  　 一组之内点名一次、自发一次，两条通路都通了。
  ⚠️ 同句一处不属于本条：`did nothing **on** it` 介词错 ⇒ 应 `**about** it`，另记 #0329（新建）。
  📋 更好：`The government **has done nothing about it**.`
  　（「什么都没做」默认是到现在为止仍未做 ⇒ 现在完成时更贴；但她的一般过去时也成立，不判错）

## #0280 `the cost / price / value of + X` —— of 结构做主语
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F07

**问题是什么**
抽象名词 ＋ of ＋ 名词，是学术写作里最常用的主语形状，比所有格正式：
```
✅ `**the cost of** risk` · `**the price of** taking risks` · `**the value of** experience`
⚠️ `risk's cost`（所有格给无生命名词，偏口语）
```
**of 后面能接什么**：
```
名词        the cost **of** the project
动名词      the price **of** taking risks · the cost **of** playing it safe　★ 不能用不定式
⛔ `~~the price of to take risks~~`
```
★ 这个结构的**主谓一致**：谓语跟 of **前面**那个中心词走（cost is / costs are），
　与 #0055 是同一条规则的应用场景 —— 你 08-20 作文里 `the cost of risk **is**` 就是对的。
★ 同族中心词（作文成套用）：cost · price · value · benefit · impact · role · scale ·
　extent · proportion · number · amount。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③（她点名要学）。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
求稳的代价是放弃一切超出平均水平的可能。（"求稳的代价"用 of 结构做主语）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `the cost of` `of 结构`，命中的是 #0184 #0249（cost/price/bill 选词）与 #0033（time 加不加 the），都是**选词或冠词**，本条是**句法结构**，问 1 不成立 ⇒ 新建。
- 2026-08-22 ❌ D4 复习日 C2·组3 第 2 题　**建号后第一次被测就塌**
  题面「这项技术的成本在过去十年里几乎没变」，她写 `the technology has remained stagnant…`。
  ★ 她**把主语整个换掉了** —— `the cost of + X` 这个形状一次都没出场，
  　 而且换完之后说的已经是另一件事（技术停滞 ≠ 成本没变）。
  正确：`**The cost of this technology** has barely changed over the past decade.`
  ★ 这条的价值就在这里：中文「这项技术的成本」是个偏正短语，直译成英文最省事的路
  　 是把中心词丢掉只留修饰语。**of 结构做主语要求你把中心词放在最前面**，正好逆着这个惯性。
  ⚠️ 同一处也记 #0126（丢掉中心词 ⇒ 命题被改写）。两条判的是不同层：
  　 本条判**句法形状没出场**，#0126 判**语义少了一块**。
  📋 更好：`has **barely changed**`（"几乎没变"）比 `remained stagnant`（停滞不前）准 ——
  　 stagnant 带贬义，说的是"该动没动"，成本不变未必是坏事。
  　 ⚠️ `stagnant` 这个词本身**不判错**（7/7 教练误判过一次、当时已收回）。
- 2026-08-23 ✅ D1 学习日 C3·组4 第 1 题　**塌过一次之后第一次答对，连对 1**
  题面「这项改革的真正价值，要等很久以后才看得出来。（★ 主语必须用 `the value of …` 这个 of 结构）」
  （连对 0 ⇒ 按 §6 必须把英文词原样写进括号），她写
  `the true value of this reform will not become clear util long into the future`。
  ★ **中心词在最前面**（the true value of …），08-22 那次"把中心词丢掉只留修饰语"的惯性没有复现 ⇒ 命中。
  ★ 主谓一致也对：`the value … will`（谓语跟 of **前面**那个词走）。
  📋 `util` 是非词 ⇒ §3.2 复习组手滑豁免，不记。
  📋 她当场点名要建条目的 `until long into the future` ⇒ 已查重后另建 **#0335**（不是本条的账）。
  📋 更好：`The true value of this reform **will not become apparent for many years**.`
  　（`for + 时段` 比 `until long into the future` 更省；apparent 比 clear 在这个位上更书面）

## #0281 what 从句：一个从句顶一个名词
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F07

**问题是什么**
`what` ＝ the thing(s) that，自带先行词，后面直接跟从句，整块当名词用：
```
作宾语      `yields no more than **what others gain**`
作介词宾语  `reserved only for **what others dare not do**`
作动词宾语  `understanding **what you want**`
作主语      `**What matters most** is consistency.`
```
**判据**：想说"…的东西／…的事"而又懒得先造一个名词时，用 what。
⛔ what 后面**不能再有先行词**：`~~the things what others gain~~`（要么 what，要么 that/which）
⛔ what ≠ which：which 有先行词，what 没有。
★ 高频块：`what matters` · `what really counts` · `what others dare not do` ·
　`what is often overlooked` · `what the data suggest`。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③（她点名要学）。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
真正重要的是能不能坚持下去。（用 what 开头那个说法）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `what 从句` `名词性从句`，F07 现有 38 条里讲从句的是 #0128（Only if 倒装）#0131（tell sb what to do）等，没有一条讲 what 自带先行词这个机制 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组2 第 6 题　**建号后第一次被测**
  题面「换工作之前，先弄清楚自己到底想要什么」，她写
  `You should think about **what you want** first before you change jobs`。
  what 从句整块当宾语，没有写成 `the thing what` 也没有换成 which ⇒ 命中，连对 1。
  📋 更好：`**Before you change jobs, work out what you actually want.**`
  　（时间从句提前、主句改祈使，与中文语序一致且短两个词；
  　 `think about`→`work out` —— 中文「弄清楚」要的是有结论，think about 只是"想一想"）
- 2026-08-23 ✅ D1 学习日 C3·组5 第 6 题　**连对 2 ⇒ 🎓 毕业。这次行使的是没测过的那一半：what 作主语**
  题面（零提示）「真正拉开差距的，是他们处理麻烦的方式。」，她写
  `what really **maks** the difference is their approach to dealing with trouble`。
  ★ 08-22 那次 what 作的是**宾语**（think about what you want），今天作的是**主语**
  　（What … is …）—— 正文列的四种用法里，这是另一种，**覆盖面比上次宽** ⇒ 命中，连对 2。
  ★ 没有写成 `the thing that` 也没有串成 which ⇒ 本条两条禁令都守住。
  ★ 题面设计留一笔：中文「真正拉开差距的」后面**故意不放名词**，让 what 成为最短的一条路
  　 —— 这是组3 那条修法的"结构留白"版本，今天在本条和 #0239 上各用了一次，两次都奏效。
  📋 `maks` 是非词 ⇒ §3.2 复习组手滑豁免，不记。
  📋 顺带用对 #0291 一族：`their **approach to** dealing with trouble` —— 这一族介词全是 to，
  　 而且 to 后面接**动名词**（dealing）也对，正是 #0291 毕业时存档说她两次都绕开的那个形状。
  　 ⇒ 隔一题就自发用对了一次，值得记。
  📋 更好：`What really **sets them apart** is **the way they handle** trouble.`
  　（sets them apart 比 makes the difference 更具体；the way they handle 比 approach to dealing 短三个词）

## #0283 动名词作主语
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F07

**问题是什么**
把一个动作变成主语，最省的办法是直接 -ing：
```
✅ `**Walking it** yields no more than what others gain.`
✅ `**Raising** the minimum wage would lift many families above the poverty line.`
⚠️ `**If you walk it**, you gain no more than…`（多一个从句、多一个 you）
⛔ `~~To walk it yields…~~` —— 不定式作主语在书面里很少这么用，通常要 `It is … to do`
```
**主谓一致**：动名词短语无论多长，**永远算单数** ⇒ 谓语用三单。
　`**Learning** a new language **takes** years.` ✅（不是 take）
★ 与 #0266 配套：`It takes years to learn a language` 是形式主语那条路，
　`Learning a language takes years` 是动名词那条路，**两条都对，按重心挑**：
　想强调"这件事"⇒ 动名词作主语；想强调"要多久"⇒ It takes。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③（她点名要学）。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
把工作换掉往往意味着从头再来。（用动名词作主语那条路）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `动名词` `作主语`，命中 #0266（take 的时间框架）里提过 It takes 那条路，但那条管的是 take/spend 的主语选择，本条管的是**动名词能不能当主语、算单数还是复数**，问 2 不成立 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组3 第 6 题　**建号后第一次被测**
  题面「承认自己不懂，往往比装懂更有用」，她写
  `**admitting** what you don't know **is** often far more helpful than **pretending** to understand`。
  ★ 三样一起到位：① 动名词当主语 ② 谓语配**单数** is ③ 后半的 `pretending` 与前面**平行**。
  ⇒ 命中，连对 1。
  📋 顺带用对：`what you don't know`（#0281）· `**far** more helpful`（#0248，far ＋ 比较级）。
  📋 没有更好的版本。
  ★ 值得记：本组 11 处主谓全对，其中就包括这个**动名词主语**（最容易被误判成复数的形状之一）。

## #0285 破折号后面接三个平行 -ing，把抽象概念摊开
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F07

**★ 2026-08-23 毕业时存下的：那个破折号两次都没真正出现过**
两次命中，三个平行 -ing 都对，但**标点两次都不是破折号**：
08-22 写成 ` - `（连字符加空格）· 08-23 写成 `:`（冒号）。
冒号本身完全合法（枚举），所以不判错；但正文写的这个结构是 `抽象说法 **—** 三个动作`，
破折号那一件从建号到毕业没被行使过。
⛔ 本条已毕业、不再出题（§3.3）；下面这条只是**存着**，她自己 review 时要用：
```
备用题面　这份工作最耗人的不是加班——是随时可能被打断、被改需求、被推翻重来。
　　　　　（★ 中间必须用**破折号**，⛔ 不许用冒号／句号；★ 后面三项全用 -ing）
★ 顺带：英文的破折号是 — 或 –，不是 -（连字符）。作文里写 - 会被当成标点错。
```

**问题是什么**
```
✅ `It is a choice shaped by experience, knowledge, and judgement — **understanding** what you
   want, **anticipating** potential problems, and **accepting** the leftover uncertainty.`
```
结构：`抽象说法 — 具体动作①, 具体动作②, and 具体动作③`
**三条硬边**
```
① 三项必须**同形**：全部 -ing，或全部名词，不能混
   ⛔ `understanding what you want, **anticipation** of problems, and to accept uncertainty`
② 三项要**同层级**：都是并列的动作，不能一个大两个小
③ 破折号前面**不能先打句号**（见 #0272）
```
★ 这个结构的作用是**把一个抽象名词变成看得见的三个动作**，是把论点写实的最快方式。
⚠️ 位置有讲究：它展开的是"怎么做"（HOW）。放在 T2 的**论证段**里会丢 TR 第 4 项
　（论证必须回答 WHY）—— 你 08-20 那篇就是这么丢的。想用它，放在**定义段或例子段**。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③（她点名要学）。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
好的准备无非三件事——弄清目标、预判风险、留出余地。（破折号后面三个动作，形式要一致）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `平行` `并列同形` `破折号`，F07 里有"并列同形"的条目讲的是 and 两边词性一致，本条是**破折号后三项展开**这个整块结构（含位置规则），问 2 不成立 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组10 第 1 题　**建号后第一次被测**
  题面「好的准备无非三件事——弄清目标、预判风险、留出余地」，她写
  `- **clarifying** goals, **anticipating** risks, and **leaving** room for error`。
  三个 -ing 形式完全一致、最后一个前面有 and ⇒ 命中，连对 1。
  📋 顺带用对 #0296：`**anticipating** risks` —— 组 4 她写的是 `anticipate … **in advance**`（冗余），
  　 这次没有再加，正是那条新补硬边要的效果。
  📋 破折号写成了 ` - `（连字符加空格）—— 复习组不判，**作文里要写 `—` 或 `–`**。
  📋 更好：`comes down to three things`（中文「无非」是**归结为**，stems from ＝源于，方向不同）。
- 2026-08-23 ✅ D1 学习日 C3·组5 第 5 题　**连对 2 ⇒ 🎓 毕业**
  题面（零提示，换场景）「所谓带团队，说白了就是三件事——把话说清楚、把人放对位置、把功劳分出去。」，她写
  `Leading a team **comes down to** three things: **communicating** clearly, **putting** the
  right person in the right role, and **sharing** the credit.`
  ★ 三条硬边逐条核：① 三项全是 -ing、**同形** ✅ ② 三项同层级（都是并列动作）✅
  　 ③ 前面没有先打句号 ✅ ⇒ 命中，连对 2。
  ★★ **她把 08-22 的更好版收进去了**：那次我给的是 `comes down to three things`（她当时写的是
  　 stems from），今天她**自发用了 comes down to** —— 更好版进入产出，这是本档案里少见的直接证据。
  ⚠️ 但标点是**冒号**不是破折号（见上方毕业存档）。冒号枚举完全合法 ⇒ 不判错。
  📋 顺带用对：`putting the right person in the right **role**` —— 两个冠词都在（R3 扫描通过）。
  📋 她当场点名要学「所谓」怎么说 ⇒ 查重后另建 **#0336**（不是本条的账）。
  📋 更好：`Leading a team comes down to three things **—** communicating clearly, putting the
  　 right people in the right roles, and sharing the credit.`
  　（把冒号换成破折号 ＝ 行使本条正文写的那个形状；person/role 改复数与 team 的规模对齐）

## #0286 `X is impossible to do` —— 主语其实是那个动作的宾语
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F07

**问题是什么**
```
✅ `these costs are **impossible to calculate**`   ＝ 算不出这些代价（costs 是 calculate 的宾语）
✅ `the effect is **hard to measure**` · `this point is **easy to overlook**`
⛔ 后面**不要再补宾语**：`~~these costs are impossible to calculate them~~`
```
能进这个结构的形容词是**闭集**，背下来就够用：
```
easy · hard · difficult · impossible · simple · tough · convenient · dangerous
＋ pleasant · comfortable
```
**判据**：`It is impossible to calculate these costs` 与 `These costs are impossible to calculate`
两句意思一样，**换主语就是换重心** —— 想让读者盯住"这些代价"，就把它提到主语位。
⛔ `important / necessary / essential` **不能**这样用：
　`~~This point is important to remember~~` ⚠️ 有歧义 ⇒ 写 `It is important to remember this point`。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③（她点名要学）。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
这项政策的长期影响很难衡量。（把"影响"放到主语位置那种写法）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `impossible to` `easy to` `逻辑宾语`，全档零命中 ⇒ 新建。
- 2026-08-22 ❌ D4 复习日 C2·组1 第 7 题（顺带）　**建号后第一次被测就塌**
  题面（主考点是 #0308）「这项政策的社会影响很难用数字衡量」，
  她写 `the effect of the policy is difficult **to be quantified**`。
  正确：`is difficult **to quantify**`。
  ★ 机制正是本条正文写的那一句：**主语就是那个动作的宾语**，所以不定式一律用主动。
  　中文「影响…很难被衡量」有个"被"字，直译过来就成了 to be done —— 这个结构恰恰不许跟着中文走。
  ★ 一句话记：`the effect is hard **to measure**` ✅／`~~hard to be measured~~` ❌。
  　同族全都一样：easy to overlook · impossible to calculate · difficult to quantify。
  ⚠️ 08-20 建号时她自己把这处标了「新」，说明她认得这个形状；今天第一次要她**产出**就走回了被动
  　 ⇒ 典型的 recognition 有、retrieval 没有。连错 1。
- 2026-08-22 ✅ D4 复习日 C2·组3 第 5 题　**同日第二次，用对了**
  题面「这套方案听上去不错，但落实起来非常麻烦」，她写
  `it will be quite troublesome **to put into practice**`。
  主语是动作的宾语、不定式**主动**、后面**不补宾语** —— 三条硬边全对。
  ⚠️ 按 §3.2 同日口径，本条今天的净结果已由组 1 的 ❌ 定下，**本行不推进 streak**。
  ★★ **同日一错一对，是全场最有信息量的一对对照**：
  ```
  组1  the effect … is difficult **to be quantified**   ❌ 走了被动
  组3  it will be quite troublesome **to put into practice**  ✅ 走了主动
  两句结构完全相同，差别只在动词：
    quantify        单个拉丁词根正式动词 ⇒ 她本能地配被动
    put into practice  短语块 ⇒ 她整块塞进去，根本没机会插 be
  ```
  ⇒ **假设：她的多余被动是「单个正式动词」触发的，不是这个句法结构触发的。**
  　 下次出题拿 implement / assess / measure 这类单词动词去验，若复发则假设成立，
  　 找法就要改成"**看到正式动词先问一句：主语是不是它的宾语**"。
- 2026-08-23 ❌ D1 学习日 C3·组1 第 3 题　⚠️ **本条已于 2026-08-23 当天改判为 ✅，见下方更正块**
  题面「这些说法现在已经没办法核实了。（★ 必须写成「主语 ＋ be ＋ 形容词 ＋ to ＋ 动词」这个形状，
  主语就是"这些说法"）」——★ 按上一行的假设设计：verify 是**单个正式动词**，专门用来验它。
  她写 `these claims **can no longer be verified** now`。
  目标句：`These claims **are now impossible to verify**.`
  ★★ **假设被验证了**：题面已经把形状点死（be ＋ 形容词 ＋ to ＋ 动词），她仍然走了**被动**
  　 —— 只是这次的被动是合法的 `can be verified`，不是 08-22 那个不合法的 `to be quantified`。
  　 两次的共同点是**同一个动作：把"核实/衡量"这个正式动词摆成被动**。
  　 ⇒ 找法定稿：**看到 verify / quantify / measure / assess / implement 这类单词正式动词，
  　 　 先问一句「主语是不是它的宾语」——是，就用「形容词 ＋ to ＋ 主动」，不要 be done。**
  ⚠️ 判 ❌ 不判 ◎✅ 的理由（§3.2）：◎✅ 的条件是「答案本身成立**且符合题面**」。
  　 她的英语成立，但题面**已经把结构点死**，她的句子不符合那个结构 ⇒ 不是题面的问题。
  ⚠️ 待她回答的一句（写在反馈里）：是**看到提示但调不出** `impossible to verify`，
  　 还是**没按提示走**？前者是 retrieval，后者是流程，处置不同。
  📋 顺带 △（不判错）：`no longer … **now**` 冗余 —— no longer 已含"到现在不再"⇒ 记 #0221 △。
- 2026-08-23 ✅ D1 学习日 C3·组1 第 3 题　**她当场推翻教练的 ❌（原话「第三题算对」）⇒ 按 §3.2 记 ✅**

  ### ★ 更正块（§4.7，2026-08-23 当天改判）
  **原判**：❌，理由是"题面已把结构点死（be ＋ 形容词 ＋ to ＋ 动词），她没照做 ⇒ 不符合题面"，
  　记 连对 0 ／ 连错 2。
  **新判**：**✅，连对 1 ／ 连错 0**。
  **判据哪里套宽了**：我把「题面括号里的结构点名」当成了**判错的依据**。它不是。
  ```
  收紧后的判据（写进本条正文，并已同步 SKILL §3.2 §6）：
    判 ❌ 只有两个理由 —— ① 她的句子本身有错　② 中文的意思没送到。
    题面括号里的结构点名是**出题的引导**，不是判分的门。
    她用另一个合法结构把同一个意思送到了 ⇒ 算对。
    考点没被行使 ⇒ 那是**我的题面没写好**（该走 ◎ 那条路、当场改题面），不是她的账。
  ```
  ⇒ 本条这次她写的 `these claims **can no longer be verified**`：英语成立、中文意思完整送到
  　（"没办法核实了"），而且**没有犯本条要防的那个错**（`~~impossible to be verified~~` 的
  　多余被动一次都没出现）⇒ 命中。
  ⚠️ **08-22 那条假设要跟着降级**：原写「单个正式动词触发多余被动，今天被验证」——
  　 现在看，她这次用的 `can be verified` 是**情态被动，本身完全合法**，与 08-22 那个
  　 `difficult **to be** quantified` 的不合法被动不是一回事。
  　 ⇒ 假设**证据不足，回到待验状态**：下次仍拿 implement / assess / measure 出题，
  　 　 但题面要把"必须用形容词 ＋ to"写成**正向必须项**，且判分只看她有没有写出
  　 　 `~~to be done~~` 这个错，不看她选了哪条合法路。
  **这个数住在哪几处**：本条状态行 ／ 本条历史（原 ❌ 那行留痕不删 ＋ 本更正块）／
  　sessions/2026-08-23.md 的判定表、diff 表A、战报（三处已同步重算）。
  📋 本条要练的那句仍然存着，下次出题用：`These claims are now **impossible to verify**.`

## #0288 最高级 + 抽象名词作主语
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F07

**问题是什么**
```
✅ `**the safest choice** usually carries **the lowest payoff**`
✅ `**the biggest obstacle** is not money but time`
✅ `**the most likely outcome** is that nothing changes`
```
**三条硬边**
```
① 最高级前面**必须有 the**：`**the** safest choice` ✅　`~~safest choice~~` ❌
② 三个音节以上用 most，不加 -est：`the most likely` ✅　`~~the likeliest~~` ⚠️ 少用
③ 与 #0106 的分界：只有两个选项时用**比较级**不用最高级
   `the **better** of the two` ✅　`~~the best of the two~~` ❌
```
★ 这个形状的价值在于**它自带论点**：一说"最安全的选择"，读者就在等你说它的代价 ——
　等于用主语先把悬念立起来，比 `If a choice is safe, it usually…` 有力得多。
★ 常用中心词：choice · option · obstacle · outcome · risk · advantage · concern · argument。

**怎么发现的**
2026-08-20　作文 T2-17。她在原稿里把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③（她点名要学）。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
最省事的办法往往效果最差。（用"最…的＋名词"当主语）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `最高级`，命中 #0106（两个选项时用比较级不用最高级）与 #0031（比较级前泛指用 a），两条都管**选级别**，本条管**最高级名词块当主语这个句法位置**，问 2 不成立 ⇒ 新建，并与 #0106 交叉引用。
- 2026-08-22 ✅ D4 复习日 C2·组1 第 8 题　**建号后第一次被测**
  题面「最省事的办法往往效果最差」，她写 `**the easiest method** is usually **the least effective** choice`。
  最高级名词块坐在主语位、`the` 没漏（硬边①）⇒ 命中，连对 1；表语也用了最高级，等于一句里用了两次。
  📋 更好：删掉 `choice` —— method 与 choice 指同一样东西，重复一次；最高级后面可以直接收尾：
  　`The easiest method is usually **the least effective**.`
- 2026-08-23 ✅ D1 学习日 C3·组3 第 3 题　**连对 2 ⇒ 🎓**
  题面（**零提示**）「最贵的那套方案不一定是最合适的。」她写
  `**the most expensive** project is not necessarily **the most suitable**`。
  ★ 本条考的是**句法位置**，三条硬边全守住：
  ```
  ① the 没漏：`**the** most expensive project` ✅
  ② 三音节以上用 most 不加 -est：`the most expensive` / `the most suitable` ✅
  ③ 不是两选一的场合，用最高级而非比较级（#0106 的分界）✅
  ```
  ⇒ 最高级名词块坐主语位、表语也收在最高级、`suitable` 后面直接断句（08-22 那次多写的 `choice`
  　 这次没有再出现）⇒ 命中，连对 2。
  ⚠️ 同句一处**不属于本条**：中文是「那套**方案**」，她写 `project`。
  　 `project` ＝ 项目（一件要做的事），`方案` ＝ 一套做法／一个可选项 ⇒ 指的不是同一样东西。
  　 正确：`the most expensive **option**`（或 plan／proposal）。
  　 ⇒ 记在**顺带用错**（词义，LR 桶）。全档 grep 了 `方案` `proposal` `scheme` `option`，
  　 　 只有 #0181（proposal ≠ advice，🎓）沾边，改正动作不同（那条是 advice 串台）⇒ 本次**不建号**，
  　 　 按"再犯一次就建"处理，留在本行备查。

---

# F08 词义/近义辨析

> 选错词、近义词边界

## #0090 学生必须在周五前交作业
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F08

**问题是什么**
P11 词义　R · P11

**怎么发现的**
2026-08-16　复习日 C1·组9

**我错在哪**
她的：advised us to **commit** homework
正确：**hand in** ／ **submit** ／ turn in homework（commit＝承诺/犯罪/提交代码，程序员词汇串台）

**中文触发点**
学生必须在周五前交作业

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组9

<details><summary>原始行（旧表逐字，旧号 E-183）</summary>

`学生必须在周五前交作业|advised us to **commit** homework|**hand in** ／ **submit** ／ turn in homework（commit＝承诺/犯罪/提交代码，程序员词汇串台）|P11 词义|R · **P11**|`

</details>

## #0157 老龄化正在让政府财政吃紧
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F08

**问题是什么**
0/3 抽查 · ◎📖 08-11

**怎么发现的**
2026-08-16　复习日 C1·组3

**我错在哪**
她的：→ **`strain`**（`put a strain on government finances`）。她已用 burdens，正好错开
正确：**路径仍未判定（08-11 两次都不算数，理由见下）**

**中文触发点**
老龄化正在让政府财政吃紧

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组3

<details><summary>原始行（旧表逐字，旧号 E-021）</summary>

`老龄化正在让政府财政吃紧|→ **`strain`**（`put a strain on government finances`）。她已用 burdens，正好错开|**路径仍未判定（08-11 两次都不算数，理由见下）**|0/3 抽查 · ◎📖 08-11|`

</details>

## #0159 delays the retirement age → raised the retirement age
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-11 ｜ 族 F08

**问题是什么**
🟡 留痕（08-11 排序：搭配值得记，但只在老龄化话题用得上，覆盖面窄）　留痕

**怎么发现的**
2026-08-11　迷你复习

**我错在哪**
她的：delays the retirement age
正确：**raised** the retirement age

**中文触发点**
政策把退休年龄从 60 提到 65

### 历史记录
- 2026-08-11 ✅ 迷你复习

<details><summary>原始行（旧表逐字，旧号 E-028）</summary>

`政策把退休年龄从 60 提到 65|delays the retirement age|**raised** the retirement age|**🟡 留痕**（08-11 排序：搭配值得记，但只在老龄化话题用得上，覆盖面窄）|留痕|**1/2 · ✅D—迷你复习**（顺带判：第 6 题她自发写出 `raised`）|`

</details>

## #0161 choose to rent houses → choose to rent / rent a place（不必点明 houses）
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F08

**问题是什么**
⚪ 劝退（floor 完全够用）　留痕

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`choose to rent houses`
正确：`choose to rent` / `rent a place`（不必点明 houses）

**中文触发点**
越来越多人选择租房

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-057）</summary>

`越来越多人选择租房|`choose to rent houses`|`choose to rent` / `rent a place`（不必点明 houses）|⚪ 劝退（floor 完全够用）|留痕|—|`

</details>

## #0165 recommend patients to specialists → refer patients to specialists
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F08

**问题是什么**
P11 词义（转诊的行话是 refer）　R · P11

**怎么发现的**
2026-08-16　复习日 C1·组4

**我错在哪**
她的：**recommend** patients to specialists
正确：**refer** patients to specialists

**中文触发点**
医生会把病人转给专科

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组4

<details><summary>原始行（旧表逐字，旧号 E-075）</summary>

`医生会把病人转给专科|**recommend** patients to specialists|**refer** patients to specialists|P11 词义（转诊的行话是 refer）|R · **P11**|0/3|`

</details>

## #0167 changing a road → taking a different route
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F08

**问题是什么**
P11 词义（change a road＝改造道路）　R · P11

**怎么发现的**
2026-08-16　复习日 C1·组5

**我错在哪**
她的：changing **a road**
正确：taking **a different route**

**中文触发点**
他建议换一条路走

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组5

<details><summary>原始行（旧表逐字，旧号 E-084）</summary>

`他建议换一条路走|changing **a road**|taking **a different route**|P11 词义（change a road＝改造道路）|R · **P11**|0/3|`

</details>

## #0168 the epidemic → the pandemic
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F08

**问题是什么**
P11 词义（epidemic＝局部流行）　R · P11

**怎么发现的**
2026-08-16　复习日 C1·组4

**我错在哪**
她的：the **epidemic**
正确：the **pandemic**

**中文触发点**
这场全球性的大流行改变了很多人的工作方式。（★ "大流行"用 pandemic）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组4

<details><summary>原始行（旧表逐字，旧号 E-088）</summary>

`疫情（大流行）|the **epidemic**|the **pandemic**|P11 词义（epidemic＝局部流行）|R · **P11**|0/3|`

</details>

## #0170 can lead to a loss of money and time → costs money and time
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F08

**问题是什么**
她已会 · 撤出装备池（08-13：无提示复现，且她当场指出"costs 那个我给了呀"——教练把她自己的产出当升级递回去，撤销）　留痕

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：can lead to a loss of money and time
正确：**costs money and time**

**中文触发点**
盲目押注要花钱花时间

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-108）</summary>

`盲目押注要花钱花时间|can lead to a loss of money and time|**costs money and time**|**她已会 · 撤出装备池**（08-13：无提示复现，且她当场指出"costs 那个我给了呀"——教练把她自己的产出当升级递回去，撤销）|留痕|✅08-13|`

</details>

## #0172 工会要求加薪
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F08

**问题是什么**
第②类　不出中译英

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：demanded higher wages（**完全标准，新闻英语里比 a pay rise 还常见**）
正确：~~a pay rise~~ **08-16 改判第②类**：目标版只是同级说法不是升级，判 ❌ 就是假错

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— 08-16 已改判第②类：她的 `demanded higher wages`
完全标准，目标版 `a pay rise` 只是同级说法不是升级，**再出就是制造假错**。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-115）</summary>

`工会要求加薪|demanded higher wages（**完全标准，新闻英语里比 a pay rise 还常见**）|~~a pay rise~~ **08-16 改判第②类**：目标版只是同级说法不是升级，判 ❌ 就是假错|第②类|不出中译英|`

</details>

## #0179 材料涨价后，总成本就上去了
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F08

**问题是什么**
P11 词义　R · P11

**怎么发现的**
2026-08-16　复习日 C1·组9

**我错在哪**
她的：the total **adds up**
正确：the total **goes up** ／ rises（add up＝说得通/对得上；doesn't add up＝不划算——E-099/E-116 块的义项边界，迁移时反了）

**中文触发点**
材料涨价后，总成本就上去了

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组9

<details><summary>原始行（旧表逐字，旧号 E-185）</summary>

`材料涨价后，总成本就上去了|the total **adds up**|the total **goes up** ／ rises（add up＝说得通/对得上；doesn't add up＝不划算——E-099/E-116 块的义项边界，迁移时反了）|P11 词义|R · **P11**|`

</details>

## #0180 提前↔ 赶在截止日期之前
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F08

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：in advance（她的，成立）
正确：**ahead of the deadline**（强调赶在截止前）／ **early**（最省）／ ahead of time · beforehand（08-16 复习日她主动问"提前还有哪些说法"，同一块；08-16 二审评审指出漏建后补）

**中文触发点**
提前（交/完成）↔ 赶在截止日期之前

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-192）</summary>

`提前（交/完成）↔ 赶在截止日期之前|in advance（她的，成立）|**ahead of the deadline**（强调赶在截止前）／ **early**（最省）／ ahead of time · beforehand（08-16 复习日她主动问"提前还有哪些说法"，同一块；08-16 二审评审指出漏建后补）|待排序|U（待定）|`

</details>

## #0185 「走投无路不会」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F08

**问题是什么**
K

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：尽管走投无路和别的压力把病人推向替代疗法
正确：**desperation**（名词，走投无路/绝望）<br>同族一起背：`out of desperation`（出于走投无路）· `in desperation`（情急之下）· `a desperate attempt`（孤注一掷的尝试）· `desperate for X`（急need X）<br>★ 本题她另外两处**都中了**：`other pressures` ✅（不是 reasons）· `drive patients towards` ✅（drive sb towards 比目标版的 push 还地道）

**中文触发点**
很多人是出于走投无路才去试这些偏方的。（★ "出于走投无路"用 desperation 那个块）
（旧留痕：「走投无路不会」—— 同族一起背：out of desperation ／ in desperation ／
　a desperate attempt ／ desperate for X）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-239）</summary>

`「**走投无路不会**」|尽管走投无路和别的压力把病人推向替代疗法|**desperation**（名词，走投无路/绝望）<br>同族一起背：`out of desperation`（出于走投无路）· `in desperation`（情急之下）· `a desperate attempt`（孤注一掷的尝试）· `desperate for X`（急need X）<br>★ 本题她另外两处**都中了**：`other pressures` ✅（不是 reasons）· `drive patients towards` ✅（drive sb towards 比目标版的 push 还地道）|**K**|`

</details>

## #0189 这个城市的人口在快速增长
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F08

**问题是什么**
⚠️ 不地道　U · 待排序

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`the population **in** this city`
正确：`the population **of** this city` ／ `this city's population`<br>★ 判据：**population 的所属关系用 of**（the population of Manhattan · the world's population）。`in` 不是错，但把"人口"说成"在城市里的那些人"，比 of 松一档

**中文触发点**
**这个城市的人口在快速增长**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-311）</summary>

`**这个城市的人口在快速增长**|`the population **in** this city`|`the population **of** this city` ／ `this city's population`<br>★ 判据：**population 的所属关系用 of**（the population of Manhattan · the world's population）。`in` 不是错，但把"人口"说成"在城市里的那些人"，比 of 松一档|⚠️ 不地道|U · 待排序|0/2|`

</details>

## #0195 政府计划提高退休年龄
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F08

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：The government is planning to raise
正确：The government **plans to** raise（一般现在时说政策更简洁；**纯风格选择——不进中译英组，作文里验**）

**中文触发点**
政府计划提高退休年龄（时态选择）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-191）</summary>

`政府计划提高退休年龄（时态选择）|The government is planning to raise|The government **plans to** raise（一般现在时说政策更简洁；**纯风格选择——不进中译英组，作文里验**）|待排序|U（待定）|`

</details>

## #0221 一个词里已经含了的那一层，别再用另一个词说一遍（同义重复）
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08
🔀 2026-08-23 从 F11 迁入 F08（她定：「归属按照你裁定来」）。原标题「此后再没回到峰值」，
　 是旧档案的题面式命名，一并改成规则式命名。

**问题是什么**
有些词的**词义里已经含了一个方向或一个时间点**，再加一个副词/介词说同一件事就是重复。
```
return **back**      ⛔  return 已含"回"           ✅ return to that peak
repeat **again**     ⛔  repeat 已含"再一次"        ✅ repeat the experiment
revert **back**      ⛔                            ✅ revert to the old system
reduce **down**      ⛔  reduce 已含"往下"          ✅ reduce the cost
no longer … **now**  ⛔  no longer 已含"到现在不再"  ✅ can no longer be verified
anticipate … **in advance** ⛔ 见 #0296            ✅ anticipate the problems
combine **together** ⛔ · **future** plans ⛔ · **past** history ⛔
```
**判据（一句话）**：把那个副词/形容词删掉，句子的意思**有没有变**？没变 ⇒ 它是重复的，删掉。
★ 「再没…」这一层用 **never** 一个词就够，比 `not … again` 更紧：
　`**never returned to** that peak` ＞ `did not return to that peak again`
⚠️ **档位是 △ 不是 ❌**：这几个搭配在口语里都听得到（`I can no longer help you now.` 这类
　 母语者句子造得出三个以上）⇒ 按 §10 禁令9 与 §0.8 **不判错**。
　 但**书面写作里删掉更有力**，作文判分时按冗余提出来（不进 GRA/LR 桶，只进更好版）。

**怎么发现的**
旧档案建号时未记来源（旧号 E-317）；2026-08-23 组1 第 3 题拿到第一个真实例。

**我错在哪**
她的：`did not return to the peak **again**` ／ `can no longer be verified **now**`
正确：`**never returned to** that peak` ／ `can **no longer** be verified`
找法：**写完一个带方向或带时间的动词，回头看它后面那个小词是不是在重复它。**

**中文触发点**
这个数字在 2010 年见顶，此后再没回到那个水平；到今天也已经没人再提它了。
（★ 两处：「再没回到」用一个词说完；「到今天也已经没人再提」里不要出现两个表示"现在"的词）

### 历史记录
- 2026-08-23 △ D1 学习日 C3·组1 第 3 题（顺带）　**本条第一次拿到实例**
  她写 `these claims can **no longer** be verified **now**`（主考点是 #0286）。
  `no longer` 已经含"到现在不再"这一层，后面再加 `now` 是同义重复 ⇒ 与 `return … again`
  同一个机制。
  ⚠️ **判 △ 不判 ❌**：`I can no longer help you now.` / `We can no longer afford it now.` /
  　 `He is no longer with us now.` 三个母语者句子造得出 ⇒ 按 §10 禁令9 与 §0.8 不许判错。
  ⇒ △ 两边都不动（连对 0 / 连错 0 维持）。
  ★ 同族冗余表补上：**no longer … now**。
  ★ 本条同日完成两件结构性整理：① 从 F11 迁到 F08 ② 标题从题面式改成规则式。

<details><summary>原始行（旧表逐字，旧号 E-317）</summary>

`**此后再没回到峰值**|`did not return to the peak **again**`|`**never returned to** that peak` ／ `did not return to that peak`<br>★ **return 本身已含"回"这一层，again 冗余** —— 同族冗余：`repeat again` · `return back` · `revert back` · `reduce down`<br>★ "再没…"这层用 **never** 一个词就够，比 not…again 更紧|⚠️ 冗余（她那句语法成立）|U · 待排序|0/2|`

</details>

## #0270 工资／收入这一族：先分清"谁的钱、按什么发"，再挑词
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
中文一个"工资／收入"，英文按**按什么周期发、给谁、算不算全部进账**分开：

```
wage(s)      按小时／按天／按周发的，蓝领与计时工
             `hourly **wages**` · `low-**wage** workers` · `**wage** growth has stalled`
salary       按月／按年发的固定薪，白领
             `an annual **salary** of £30,000` · `a **salaried** employee`
pay          最中性、最通用，两边都能盖，还能作动词
             `equal **pay**` · `a **pay** rise`（英）／`a **pay** raise`（美）· `**pay** gap`
income       一个人或一户**所有**进账（工资＋租金＋利息＋补贴）
             `household **income**` · `low-**income** families` · `disposable **income**`（可支配收入）
earnings     从劳动或投资里**挣到**的钱，正式、常用于统计
             `average **earnings** rose by 3%` · `lifetime **earnings**`
```

**★ 她点名的那个块**
```
the minimum wage        最低工资（**必须带 the**，因为全国只有这一个 → 定指）
  `The reform raised **the minimum wage** to £12 an hour.`
  `Workers on **the minimum wage** cannot afford to rent in the city.`
  ⛔ ~~a minimum wage~~（除非在说"设立一条最低工资线"这个抽象制度：`introduce a minimum wage`）
  ⛔ ~~minimum salary~~ —— 最低工资是按小时算的，固定搭配就是 wage
同一批固定块（作文里成套用）：
  `**the living wage**` living wage 生活工资　`**the poverty line**` 贫困线
  `**the pay gap**` 薪酬差距　　`**the retirement age**` 退休年龄（同 #0025，也必须带 the）
  ⇒ 共同点：**全国只有一条线／一个数 ⇒ 定指 ⇒ 带 the**
```

**T2 里的现成句**
```
Raising **the minimum wage** would lift many families above **the poverty line**.
**Wage growth** has failed to keep pace with **the cost of living**.
Households on **low incomes** spend a far larger share of their **income** on essentials.
```
**找法**：先问三句 —— 按小时还是按月？（wage/salary）只算劳动所得还是全部进账？（earnings/income）
是不是全国唯一那条线？（是 ⇒ 带 the）

**怎么发现的**
2026-08-20　D3 学习日 C2·组5 第 2 题。她写 `the reform significantly raises the minimunm wage`，
两个考点全中，然后当场点名：「最低工资建一个条目」（§2③）。

**我错在哪**
她这次没有错 —— `the minimum wage` 连冠词都对。
建号理由是 §2③。她缺的是**这一族的分工**：档案里她只用过 wage 一个词（#0172 `higher wages`），
income / earnings / pay 一次都没出现过，说明谈钱的时候她只有一个词可用。

**中文触发点**
低收入家庭把收入里很大一部分花在了日常必需品上。（"收入"这个词出现两次，两处该用同一个词吗）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）D3 学习日 C2·组5 第 2 题
  查重（§3.5 B0）：grep 了 `wage` `salary` `income` `minimum` `工资` `收入`，全档命中两处：
  · #0172（工会要求加薪 → demanded higher wages）—— 08-16 已改判为**第②类·不出中译英**，
    内容是"她的版本本来就标准、判 ❌ 是假错"的留痕，**没有规则**，谈不上同一条 ⇒ 问 2 不成立
  · #0048 与今天组1 记录里的 `low-income household` —— 那是**数**（泛指该用复数），不是选词 ⇒ 问 1 不成立
  又比对了 #0184（cost / price / spending 三分法）与 #0249（bill / fee / cost）：
  那两条分的是"花出去的钱"，本条分的是"挣进来的钱"，两套词零重叠 ⇒ 不合并。
  ⇒ 新建。建号时无对错，连对连错都是 0。
- 2026-08-20 ✅ 作文 T2-17　**高压 ✅**（建号当天就在作文里用对）
  S5 `an individual who changes jobs for better **pay** or a higher title`。
  按周期发的钱这个位置她选了最通用的 pay，没有误用 wage（按小时/蓝领）或 salary（按月/白领）
  ⇒ 考点命中。当天净结果 ✅（建号那行是 ③，不推进 streak）⇒ 连对 1。
- 2026-08-22 ❌ D4 复习日 C2·组9 第 3 题
  题面「他跳槽主要是为了更高的底薪，不是为了奖金。（★「底薪」和「奖金」各用一个准确的词）」，
  她写 `he changed jobs mainly for a higher **base**, not for the bonus`。
  ★ 「奖金」→ `bonus` ✅ 对；**「底薪」→ `base` ❌ 不成立** ——
  　 base 单独当名词只在口语 HR 里省略着用（"his base is 80k"），书面必须写全：
  ```
  base salary   底薪（月／年固定的那部分）      basic pay   同义，英式更常见
  bonus         奖金（额外发的）               commission  提成（按业绩比例）
  overtime pay  加班费                        allowance   津贴（交通／住房）
  package       整体薪酬（底薪＋奖金＋福利）
  ```
  ⇒ 本条考的就是这一族挑词，一半不算命中 ⇒ ❌，连对 1 → 0。
  📋 更好：`… for a higher base salary **rather than for** the bonus.`
  　（`not for` → `rather than for`，书面对比更明确）
- 2026-08-23 ✅ D1 学习日 C3·组1 第 6 题　**08-22 塌的那个词今天原样修好了**
  题面「她的底薪并不高，大部分进账靠的是提成和加班费。（★ 三处各用一个准确的词：底薪 · 提成 · 加班费）」
  她写 `her **base salary** is not high; most of the income comes from **commission** and **overtime pay**`。
  ★ 三个成员逐格核对：
  ```
  底薪    base salary    ✅  ← 08-22 她写的是光一个 `base`，今天写全了
  提成    commission     ✅
  加班费  overtime pay   ✅
  ```
  ⇒ 三个成员同时落地（§3.5 词表型出题要求满足）⇒ 命中，连对 1、连错归 0。
  ⚠️ §3.5① 毕业条件核对：本条至今覆盖过的成员 —— `pay`（08-20 作文）· `base salary`
  　 `commission` `overtime pay`（08-23）⇒ **已覆盖 ≥2 个不同成员**，下次再对一次即可毕业。
  📋 顺带用对 #0272：分号连两个独立分句，两句语义紧挨 ⇒ 用得准。
  📋 △ 不判错：`most of **the** income` —— 说的是她的进账，`most of **her** income` 更贴；
  　 但前一分句已经出现 `her base salary`，`the income` 回指得过去 ⇒ 按 §0.8 不判错，只给更好版。
  📋 更好：`Her base salary is modest; most of **her** income comes from commission and overtime pay.`
  　（`not high` → `modest`，书面一格）

## #0289 yield ＝ 产出、带来（不是"屈服"那个意思）
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F08

**问题是什么**
`yield` 在书面英语里最常用的意思是**产出、带来**，主语是"投入的东西"：
```
✅ `the reward it **yields**` · `walking it **yields** no more than…`
✅ `The trial **yielded** promising results.` · `This approach **yields** a higher return.`
搭配：yield **results / a return / benefits / data / insights / no more than X**
```
同族三个，按主语挑：
```
yield     强调"产出多少"，主语是方法、投资、土地   `The method yields consistent results.`
produce   最通用、最中性                        `The policy produced an unexpected effect.`
generate  强调"从无到有造出来"，主语常是系统/活动  `Tourism generates jobs.`
```
⚠️ `yield` 的另一个意思是"让步、屈服"（`yield to pressure`），作文里两个意思都会用到，
　 靠**后面接不接 to** 分：`yield sth`（产出）／`yield **to** sth`（屈服）。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
这种做法带来的回报远远超过投入。（"带来"用 yield 那个词）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `yield`，全档只命中今天作文的记录，零条目 ⇒ 新建。
- 2026-08-22 ❌ D4 复习日 C2·组7 第 7 题　**建号后第一次被测就塌**
  题面「这套训练带来的效果要几个月才看得出来。（★「带来」用一个动词，那个词也用来说"农作物产量"）」
  ——★ **改写过的题面**：存档那条括号里直接写着「用 yield 那个词」，等于给答案，已去掉。
  她写 `**the results of** this training won't show until a few months later`。
  ★ yield **一次都没出场** —— 她把"带来"整个换成了名词块 `the results of`。
  ⚠️⚠️ 而且这个词**她自己在 08-20 作文 S2 里用过**：`the reward it **yields**`。
  　 与今天 #0297（作文写对 accompanied **by**、复习组写成 with）**完全同一个形状**。
  ⇒ 结论：作文里那次很可能是**当场够出来的一次性产出**，没有进入可检索状态。
  ⇒ **出题纪律（本日新增）：从她作文里建的条目，第一次复习要比别的条目更早、更密** ——
  　「作文里写对过」是最容易被高估的证据。
  📋 同句两处留痕：`won't` 缩写（#0236 不出中译英，不判）·
  　`until a few months later` —— not…until 后面接的是**时间点**，不是"…之后"，
  　 该写 `for several months` ／ `until several months later`。
  📋 更好：`**What this training yields** will not become visible for several months.`

## #0290 be accessible to sb ＝ 对某人开放／够得着
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
```
✅ `A guaranteed path to success is **accessible to** anyone.`
✅ `Higher education should be **accessible to** students from all backgrounds.`
搭配：accessible **to** sb（对谁开放）· accessible **by** 交通工具（怎么到达）
```
同族按"障碍在哪"分：
```
accessible to    没有门槛，谁都能用／能到      `accessible to everyone`
available to     有存货、有名额，能拿到        `The scheme is available to first-time buyers.`
open to          制度上允许（也指"愿意接受"）  `open to the public` · `open to criticism`
within reach of  够得着（常指经济上）          `within reach of ordinary families`
affordable to    买得起                       `affordable to low-income households`
```
**判据**：障碍是**通路**（accessible）、**数量**（available）、**规则**（open）还是**钱**（affordable）？

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
优质教育资源应该让所有家庭都够得着。（"够得着"用 accessible 那个说法）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `accessible` `available to`，全档零命中 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组6 第 6 题　**建号后第一次被测**
  题面「优质教育资源应该让所有家庭都够得着。（★「够得着」用一个形容词 ＋ to，别用 can get）」
  ——★ **改写过的题面**：存档那条括号里写着「用 accessible 那个说法」，等于给答案，已去掉。
  她写 `Quality educational resources should be **accessible to** all families`。
  零提示下调出来了，介词 to 也对 ⇒ 命中，连对 1。
  📋 顺带：`Quality educational resources` —— 名词作定语（quality）用得地道。
- 2026-08-23 ✅ D1 学习日 C3·组5 第 4 题　**连对 2 ⇒ 🎓 毕业**
  题面（零提示，换场景）「这条步道重修之后，坐轮椅的人也上得去了。」，她写
  `the trail **is accessible to** wheelchair users since it was rebuilt`。
  ★ 形容词 ＋ to 一次到位，介词没写成 for／by ⇒ 命中，连对 2。
  ★ 中文换成「坐**轮椅**的人上得去」之后，本条判据里的四条路只剩一条能走：
  　 障碍是**通路**（accessible）⇒ available（数量）／open（规则）／affordable（钱）全部不成立。
  　 ⇒ 组3 那条修法今天第四次奏效。
  📋 「**也**上得去」的「也」没进英文，⛔ 不判 #0126：也是加合语气词，删掉后命题
  　（这条步道对坐轮椅的人开放）没有被改写 ⇒ 落在 08-22 收紧判据的不判那一侧。
  📋 `is accessible … **since** it was rebuilt` 时态不判错：现在时 ＋ since 从句造得出母语者句子
  　（`The area is much safer since the police station opened.` / `She's much happier since she
  　 changed jobs.` / `Traffic is far worse since they closed the bridge.` 三条，§0.8）⇒ 只进更好版。
  📋 更好：`Since it was rebuilt, the trail **has been** accessible to wheelchair users **as well**.`
  　（since 从句配现在完成时是默认搭配；as well 把「也」那一层补回去）

## #0291 a path / route / road to + 名词 ＝ 通往…的路
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**★ 2026-08-23 毕业时存下的：`the key to` 这条支路没被行使过**
两次命中（08-22 stepping stone to · 08-23 path to）落地的都是**名词 ＋ to ＋ 名词**，
而同族里 `**the key to ＋ 动名词**` 那条路她两次都绕开了（08-23 写成 `the key that unlocked…`）。
⛔ 本条已毕业、不再出题（§3.3）；下面这条题面只是**存着**，她自己 review 时要用：
```
备用题面　愿不愿意改，往往才是把这件事做成的关键。
　　　　　（★ 必须用 `the key to` ＋ **动名词**；⛔ 不许用 the key that … / the key which …）
```

**问题是什么**
```
✅ `a **path to** success` · `the **route to** promotion` · `the **road to** recovery`
⛔ 介词只能是 to：`~~a path of success~~` · `~~a path for success~~`
```
三个词的分工：
```
path    抽象、个人的路径（最通用，作文首选）  `a path to success` · `a career path`
route   有具体路线感，常配 the                `the fastest route to market`
road    最有画面、也最俗套，慎用              `the road to recovery`（经济复苏常用）
```
同族抽象"路"的块（成套用）：
```
a stepping stone to    通向…的踏脚石       a shortcut to        捷径
a barrier to           通往…的障碍         the key to           …的关键（也配 to！）
an obstacle to         阻碍                a gateway to         门户
```
★ 注意上面这一族**介词全是 to**：`the key **to** success` ✅ `~~the key of success~~` ❌

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
语言只是通往这份工作的一块踏脚石。（"通往…的"这类块，介词别写错）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `path to` `the key to` `route`，全档零命中 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组8 第 7 题　**建号后第一次被测**
  题面「语言只是通往这份工作的一块踏脚石」，她写 `Language is only a stepping stone **to** the job`。
  「通往…的」这类块配 **to** 不配 for／of ⇒ 命中，连对 1。
  ★ 而且她自己够出了 `stepping stone` 这个块（本条正文里没有列过）—— 同族的现成成员。
  📋 「**这份**工作」→ the job：指示词属语境限定语，按 08-22 收紧判据不判。
- 2026-08-23 ✅ D1 学习日 C3·组4 第 4 题　**连对 2 ⇒ 🎓 毕业**
  题面（零提示）「教育曾经是通往更好生活的最可靠的一条路；而语言，往往是打开那扇门的钥匙。」，她写
  `education used to be the most reliable **path to** a better life, and language was often
  the key **that unlocked** that door`。
  ★ 前半 `path **to** a better life` —— 介词就是 to，没写成 of／for ⇒ **本条考点命中**，连对 2。
  ⚠️ 后半的第二个成员 `the key **to**` 被 `the key that unlocked` 绕开了。
  　 按 §3.2「判 ❌ 只有两个理由」：关系从句本身完全成立、意思也送到 ⇒ **不判错**，
  　 但这个成员从建号到毕业一次都没出场 ⇒ 备用题面已存进正文（见上）。
  📋 `was often` 时态留痕不判：中文「往往是」是习惯性的现在，她跟着前半的 `used to be`
  　 把整句锁进过去框，读得通 ⇒ §5 四问自审第 ④ 问判为"有更好的"，进更好版。
  📋 更好：`Education used to be the most reliable path to a better life, and language **is**
  　 often **the key to opening** that door.`（`the key to ＋ 动名词` 是这一族的标准形状）

## #0292 carry ＋ 抽象名词 ＝ "自带、附带"（不是"搬"）
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F08

**问题是什么**
`carry` 后面接抽象名词时，意思是**这件事本身自带某种性质**：
```
✅ `the safest choice usually **carries** the lowest payoff`
✅ `Every investment **carries** a risk.` · `His words **carry** weight.`
✅ `The offence **carries** a heavy penalty.` · `This role **carries** great responsibility.`
```
常见宾语（背这一串就够）：
```
carry **a risk / weight / a penalty / responsibility / consequences / implications /
       a payoff / a price / authority / conviction**
```
**判据**：想说"这件事**本身就带着**某种后果或分量" ⇒ carry；
想说"造成、导致" ⇒ 用 cause / lead to / bring about（那是**因果**，不是**自带**）。
⚠️ 一个细分：`carry a risk`（风险是内在的）≠ `pose a risk`（对别人构成威胁）
　 `Smoking **carries** health risks.`（吸烟这件事自带风险）
　 `The dam **poses** a risk to nearby villages.`（水坝对村子构成威胁）

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
每一项投资本身都带着风险。（"带着"用 carry 那个说法）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `carry`，全档零命中；与 #0184（cost/price/spending 三分法）不同 —— 那条分名词，本条讲**动词 carry 能带哪些抽象宾语**，问 1 不成立 ⇒ 新建。
- 2026-08-22 ❌ D4 复习日 C2·组9 第 6 题　**建号后第一次被测就塌**
  题面「每一项投资本身都带着风险。（★「带着」用一个动词，那个词**本义是"搬运"**）」
  ——★ **改写过的题面**：存档那条括号里直接写着「用 carry 那个说法」，等于给答案，已去掉，
  　 改成点**词的本义**（搬运）——指向仍然很死。
  她写 `every investment **is accompanied by** risks`。句子成立，但 carry 一次都没出场 ⇒ ❌。
  ⚠️⚠️ **最值得记的一点：她组 5 第 10 题自发写过 `this kind of method **carries** risks`。**
  　 也就是说**这个块她会**，被点名要它的时候反而绕开了。
  ★★ 与 #0297 正好互补，两条放在一起读：
  ```
  #0297（accompanied by）  组6 被点名时写错 with  →  组9 自发用对 by
  #0292（carry ＋ 抽象名词）组5 自发用对 carries  →  组9 被点名时绕开
  ```
  ⇒ **她的"自发产出"和"被点名产出"是两条不同的通路**：
  　 被点名时她会去猜"教练要哪个词"，反而丢掉本来会用的那个。
  ⇒ 出题启示：这类"她其实会"的块，**挂作文验比单点题更准**（§6 末条）。
  📋 更好：`Every investment carries **a degree of risk**.`
  　（中文「都带着风险」说的是"或多或少有"，不是"有好几种风险"）

## #0293 payoff / return / reward / gain 四个"回报"怎么分
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F08

**问题是什么**
```
payoff   投入之后**最终换来的那个结果**，略口语但书面可用，常配 low / high / big
         `the lowest **payoff**` · `The payoff came years later.`
return   **金融和投资**的标准词，可数，常配 on
         `a high **return on** investment` · `diminishing **returns**`
reward   偏"值得"的那层价值判断，常与 risk 对举 ★ T2 里最常用
         `the **rewards** of taking risks outweigh the risks`
gain     **净增加的量**，常复数，也常与 loss 对举
         `the **gains** outweigh the **losses**` · `financial **gains**`
benefit  最中性最通用，说"好处"用它最安全
         `the **benefits** of exercise`
```
**判据**：讲**钱** ⇒ return／gain；讲**值不值** ⇒ reward；讲**最后换来什么** ⇒ payoff；
拿不准 ⇒ benefit（永远不出错）。
★ 与 #0270（wage / salary / pay / income / earnings）配套：那条分"挣进来的钱"，
　本条分"投入换来的回报"，两套词不重叠。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
这类投入的回报往往要等好几年才看得见。（"回报"这里该用哪个词）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `payoff` `return` `reward`，全档零命中；与 #0270（工资收入一族）分的是不同的钱，问 1 不成立 ⇒ 新建。
- 2026-08-22 ❌ D4 复习日 C2·组5 第 8 题（顺带）　**建号后第一次被测就塌**
  题面「这笔投资的**收益**最终会超过投入的成本」（主考点 #0299），她写 `the **profit of** the investment`。
  正确：`the **return on** this investment`。
  ★ 两层都错，而且是同一个根：
  ```
  选词  「收益」讲的是钱 ⇒ **return／gain**（本条判据第一行）。
        profit ＝ **利润**，本身已经是减掉成本之后的数
        ⇒「利润超过成本」在逻辑上打架，说的不是她想说的意思
  介词  return 配 **on**：`a high return **on** investment` 是固定块（ROI 就是它）
        profit 也不配 of：`profit **on/from** the investment`
  ```
  ⚠️ 与 #0270（wage/salary/pay/income/earnings）的分界再记一次：那条管**人挣的钱**，本条管**投入换来的钱**。
  📋 顺带用对：`the … **of the investment**` 这个主语形状本身是对的（#0280）。
- 2026-08-22 ✅ D4 复习日 C2·组10 第 10 题　**判 ✅ 但不推进 streak（同日口径）**
  题面「这类投入的回报往往要等好几年才看得见」，她写 `this kind of investments **yield returns** only after several years`。
  ★ 「回报」讲的是**钱** ⇒ returns，挑对了（组 5 她写的是 profit）⇒ 考点命中。
  ⚠️ 按 §3.2 同日口径，本条今天的净结果已由组 5 的 ❌ 定下 ⇒ 本行只留证据，连对 0／连错 1 不变。
  ★★ 顺带用对 **#0289**：`**yield** returns` —— **组 7 被点名要 yield 时她调不出来（❌），这里自发用出来了。**
  　 与 #0292（carry）#0297（accompanied by）完全同一个形状，**今天第三次验证"自发 ≠ 被点名"**。
  ⚠️ 同句两处不属于本条：`this kind of **investments**` ⇒ 记 #0251（🎓 后复发，回池）·
  　 丢「**往往**」⇒ 记 #0126。

## #0294 be reserved for ＝ 只留给（不是"预订"）
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
```
✅ `real rewards are **reserved for** what others dare not do`
✅ `The top jobs are **reserved for** those with experience.`
✅ `This lane is **reserved for** buses.`
```
**判据**：想说"这东西**只给某一类人／某一种情况**，别人没份" ⇒ be reserved for。
它自带一层**排他**的意思，比 `are only given to` 有力。
同族（按"给不给得到"排）：
```
be reserved for   只留给某一类（排他最强）    be confined to      局限在…范围内
be limited to     被限制在…以内              be restricted to    被规定只能…
be open to        对…开放（相反方向）        be available to     对…可得
```
⚠️ 别和 `reserve a table / a seat`（预订）混 —— 那是 reserve 的及物动词用法，
　 靠**被动 + for** 认出这个意思：`be reserved **for**` ⇒ 只留给。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
- 2026-08-22（改死后的新题面，下次用）　这几个名额是**专门留给**新员工的，别人一律没份。
  （★ 用 be ___ for 那个自带"别人没份"的动词；⛔ 不许用 only for ／ just for ／ is for）
- 2026-08-22（教练当天实际用的，已作废）　这份工作留给有五年以上经验的人。
  ★ 缺陷：教练重写题面时**把括号里的结构点名整句丢了**（§6 违规），
  　 中文「留给」最自然的英文就是 is for，排他那一层逼不出来 ⇒ 记 ◎✅，是教练的账。
- （建号时）　最好的机会往往只留给敢先动手的人。（"只留给"用被动那个说法）
  ⚠️ 这条不能和 #0273（dare 作情态动词）放同一组 —— 「敢」是那条的考点词，构成提示关系。

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `reserved` `confined to` `limited to`，命中 #0269（在小范围四条路）里列过 be limited to / be confined to —— 那条管的是**「范围」这个概念怎么说**，本条管的是 **reserved for 的排他语义**，问 2 不成立 ⇒ 新建，并与 #0269 交叉引用。
- 2026-08-22 **◎✅** D4 复习日 C2·组2 第 9 题　**算对，连对 1**（题面缺陷，不是她的问题）
  题面「这份工作留给有五年以上经验的人」，她写
  `this job **is just for** those who have more than 5 years working experience`。
  ★ 句子成立、也完全符合题面 —— 中文「留给」最自然的英文就是 is for ⇒ 按 §3.2 判 ◎✅，连对 +1。
  ⚠️ 但 `be reserved for` 自带的那层**排他**（别人一律没份）一次都没出场 ⇒ **是我的题面没点名，我的账**。
  ⇒ 题面已改死（见下方中文触发点 2026-08-22 那行）。
  📋 顺带用对：`those who`（#0239，今天第三次自发出现，组 1 刚测过）。
  ⚠️ 同句两处不属于本条：`**working** experience` → `**work** experience` ⇒ 记 #0307（归入待确认）·
  　 `5 years` 缺所有格撇号 → `five years'` ⇒ 挂 reminders.md **R3**。
  📋 更好（行使考点）：`This post **is reserved for** those **with** more than five years' experience.`
- 2026-08-23 ✅ D1 学习日 C3·组4 第 5 题　**连对 2 ⇒ 🎓 毕业。08-22 白测的那个考点这次真的行使了**
  题面（零提示）「前排座位是专门留给行动不便的乘客的，其他人不能坐。」，她写
  `the front seats **are reserved only for** passengers with reduced mobility, and others are
  not allowed to sit there`。
  ★ **零提示下自己调出了 `be reserved for`** —— 08-22 那次同一个考点她走的是 `is just for`
  　（题面没点名，是我的账）。这一次中文里没有任何英文词，她仍然落到了这个块上 ⇒ 命中，连对 2。
  ★ 教练侧记一笔（这是组3 那条修法第二次奏效）：中文换成「**座位**＋专门留给」之后，
  　 `reserved` 成了这个搭配的默认落点（`seats are reserved for` 是固定搭配），
  　 `is just for` 那条路自己就不自然了 ⇒ **不是靠提示逼出来的，是靠语境把别的路堵住的**。
  📋 顺带用对：`passengers with **reduced mobility**` —— 这是英式公共交通的标准说法（PRM），
  　 比我题面直译的 limited mobility 更准，**她的比我的好**。
  📋 `reserved **only** for` 的 only 位置对（修饰 for 短语）；不判、也不必改。
  📋 更好：`The front seats are reserved for passengers with reduced mobility; **no one else may use them**.`
  　（分号比 and 紧；`may use` 比 `are not allowed to sit there` 短一半）

## #0295 shaped by / grounded in / based on / rooted in ＝ "建立在…之上"
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**成员出题账**
```
① based on     2026-08-23 组3 题面「这项新政策是依据大量实地调查定出来的」⇒ ✅
② grounded in  2026-08-22 组10 题面「这套做法是建立在多年一线经验之上的」⇒ ✅
③ rooted in    2026-08-23 组3 题面「这种偏见深深扎根在当地的传统里」⇒ ✅
④ shaped by    未出过
⇒ 三个成员已落地，毕业时唯一没测过的是 shaped by。
　 2026-08-23 她当场点名「这个扎根可以新建个条目练习下」—— rooted in 就是本条成员③，
　 已在本条落地，⛔ 不重复建号（§3.5 防重复）。是否按 §3.5 第3.5步② 把它单独摘出来，待她定。
```

**问题是什么**
四个都翻成"基于／建立在…上"，但**比喻来源不同，搭的东西也不同**：
```
based on      最通用、最安全，什么都能接        `a decision **based on** evidence`
grounded in   ★ 强调"有扎实依据"，接理论/研究/现实  `**grounded in** research` · `grounded in reality`
rooted in     强调"源头在那儿、长出来的"，接文化/历史/传统 `**rooted in** tradition`
shaped by     强调"被塑造成现在这样"，接经验/环境/力量   `a choice **shaped by** experience`
```
**判据**：你要说的是**依据**（based on / grounded in）、**源头**（rooted in）、
还是**成因**（shaped by）？
★ 语域顺序：based on（中性）＜ shaped by ＜ grounded in ／ rooted in（最正式）。
⚠️ 介词固定，不能换：`grounded **in**` ✅ `~~grounded on~~` ❌　`rooted **in**` ✅ `~~rooted from~~` ❌
⚠️ 与 #0284（过去分词作后置定语）配套用：这四个块最常见的位置就是名词后面
　（`a choice **shaped by** experience`），那是句法，本条是选词。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
这套做法是建立在多年一线经验之上的。（"建立在…之上"用一个比"based on"更实的词）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `based on` `grounded` `rooted`，命中 #0169（rest on individual experience）—— 那条是**一个整块**（靠个案经验而非大规模试验），本条是**四个近义块的分工**，问 2 不成立 ⇒ 新建，并与 #0169 交叉引用（rest on 也属这一族）。
- 2026-08-22 ✅ D4 复习日 C2·组10 第 7 题　**建号后第一次被测**
  题面「这套做法是建立在多年一线经验之上的。（★「建立在…之上」用一个比 based on 更实的词）」，她写
  `this approach is **gounded in** years of hands-on experience`。
  挑对了 grounded in（比 based on 更实）⇒ 命中，连对 1。
  📋 `gounded` → `grounded` 非词拼写，复习组豁免。
  📋 顺带：`hands-on experience` 是她自己够出来的复合形容词，用得很准。
- 2026-08-23 ✅ D1 学习日 C3·组3 第 2 题　**连对 2 ⇒ 🎓**
  题面（**零提示**）「这种偏见深深扎根在当地的传统里；而这项新政策是依据大量实地调查定出来的。」她写
  `this prejudice is deeply **rooted in** the local tradition, whereas the new policy is **based on**
  extensive field research`。
  ★ **一题两个成员，两个都按判据挑对了**：
  ```
  前半「深深扎根」＝ 源头在那儿、长出来的 ⇒ **rooted in**（本条判据第二行），
       而且介词守住了 in（正文硬边：`~~rooted from~~` ❌）
  后半「依据…定出来的」＝ 依据 ⇒ **based on**（最通用那一档），语域也对：
       政策文件配 based on 正好，不必往 grounded in 上冲
  ```
  ⇒ 词表型条目要求的"一题 ≥2 个成员落地"这次真正做到了 ⇒ 命中，连对 2。
  📋 更好：`rooted in **local tradition**`（去掉 the）—— tradition 作抽象概念时零冠词更常见；
  　 加 the 之后读者会等一个具体的"哪一条传统"。她的写法不判错，只进更好版。
  📋 顺带用对：`whereas` 引对比从句，位置与逗号都对（#0317 一族，📋 留痕不推进）。

## #0296 anticipate ＝ 预判并提前应对（不只是"预料"）
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
```
✅ `**anticipating** potential problems` · `**anticipate** demand / objections / criticism`
✅ `far higher than **anticipated**`（作过去分词用，见 #0304）
```
`anticipate` 比 expect 多一层**"因此提前做了准备"**：
```
expect      单纯地"以为会发生"        `I expect prices to rise.`
anticipate  预料到 **并且据此行动**    `The company anticipated the shortage and stockpiled.`
foresee     看得到（常用于否定）      `No one could have foreseen this.`
predict     做出预测（常有依据/模型）  `The model predicts a 3% rise.`
```
**判据**：这句里有没有"因此提前做了什么"的意思？有 ⇒ anticipate；没有 ⇒ expect。
⚠️ 语法陷阱：`anticipate` 后面接**动名词或名词**，不接不定式：
　`anticipate **facing** difficulties` ✅　`~~anticipate to face~~` ❌
　（expect 相反：`expect **to face**` ✅）
⛔ **冗余陷阱（2026-08-22 她写出来之后补的）**：`anticipate` 后面**不要再加 in advance / beforehand**。
　`~~anticipate potential problems **in advance**~~` ⚠️　`**anticipate** potential problems` ✅
　理由：anticipate ＝ 预料 ＋ **提前应对**，"提前"这一层已经在词里了，再说一遍是同义重复。
　同族的冗余陷阱一起记：`~~return **back**~~` · `~~repeat **again**~~` · `~~plan **ahead** in advance~~` ·
　`~~combine **together**~~` · `~~future **plans**~~`
　（要单说"事先"用 in advance / beforehand，那是 #0301 那一族，配的是别的动词）

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
有经验的人会提前把可能出的问题想到并准备好。（"提前想到并准备"用 anticipate）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `anticipate` `expect` `predict`，全档零命中 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组4 第 8 题　**建号后第一次被测**
  题面「有经验的人会提前把可能出的问题想到，并先准备好对策」
  （★ 改写触发点：存档那条把英文单词 anticipate 直接写在题面里了，等于给答案，已去掉），她写
  `those with experience **anticipate** potential problems in advance and prepare solutions for them`。
  ★ 在零提示的情况下调出了 anticipate ⇒ 选词命中，连对 1。
  ⚠️ **但后面又加了 `in advance`，是冗余** —— anticipate 本身已经含"提前"这一层。
  　 不另记错（她选词是对的，缺的是"这个词含多少"），改成给本条补一条硬边（见上方正文）。
  ⚠️ 查过 #0265（两个同义说法不要焊在一起）：**不是同一条**。
  　 那条的找法是"把两半拆开看能不能各自站住"，而 anticipate 与 in advance **各自都站得住**，
  　 那个找法抓不到这一处 ⇒ 问 2 不成立，不归入。
  📋 顺带用对：`**those with** experience`（#0239 的第三种形状：those ＋ 介词短语，今天第四次自发出现）。
  📋 更好：`… and **have a response ready**`（4 个词，且不必再指回 them）。
- 2026-08-23 ✅ D1 学习日 C3·组4 第 6 题　**连对 2 ⇒ 🎓 毕业。08-22 补进正文的那条冗余硬边，这次守住了**
  题面（零提示）「好的调度员会预判到哪些环节可能出问题，并提前把备用方案准备好。」，她写
  `a good dispatcher will **anticipate where things might go wrong** and **have backup plans
  ready in advance**`。
  ★ 两件事同时成立：
  ```
  ① 零提示下调出 anticipate（中文写的是"预判"，没有出现任何英文词）        ⇒ 选词命中
  ② `anticipate` 后面**没有再挂 in advance** —— 08-22 她正是在这里冗余的，
     今天 in advance 挪到了后半句 `have backup plans ready in advance`，
     配的是 have…ready，**位置完全正确**                                  ⇒ 硬边守住
  ```
  ⇒ 连对 2，毕业。
  📋 `anticipate` 后接 **where 从句** 成立（anticipate ＋ 名词/动名词/wh 从句都行，
  　 禁的只有不定式 `~~anticipate to face~~`）⇒ 不判。
  📋 「哪些**环节**」→ `where` 不判 #0126：`where things might go wrong` 与
  　 `which stages might go wrong` 命题相同（"哪里会出问题"），按 08-22 收紧判据
  　 「删掉后命题被改写才判」，这一处命题没被改写 ⇒ **不判丢层**。
  📋 更好：`A good dispatcher **anticipates which stages are likely to fail** and **keeps a
  　 backup plan ready**.`（一般现在时说职业习性比 will 更稳；单数 a backup plan 与"备用方案"对齐）

## #0297 uncertainty 这个词怎么用：搭什么动词、加不加冠词
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
```
✅ `accepting the leftover **uncertainty**` · `**Uncertainty** is inevitable.`
✅ `Risk is invariably accompanied by **uncertainty**.`
```
**冠词与数**（最容易错的一层）：
```
不可数（泛指"不确定性"这个概念）—— 零冠词  `**Uncertainty** discourages investment.`
可数（具体的某一处不确定）—— 加冠词/复数    `There are still **a few uncertainties** about the timeline.`
```
常配的动词与形容词：
```
动词  **accept / live with / reduce / remove / cope with** uncertainty
形容词 **considerable / genuine / residual / lingering** uncertainty
      ⚠️ `leftover uncertainty` 能懂但偏口语，书面写 **residual / remaining**
```
★ 与 #0269（在小范围）里 `within a narrow range` 是同一个话题域（不确定与幅度），
　 但那条管"范围"，本条管"不确定性"这个名词本身。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
- 2026-08-23（**改死后的新题面，下次用**）　时间表上还剩两三处说不准的地方，年底应该能定下来。
  （★ 必须用 uncertainty 的**可数复数**形式；⛔ 不许改写成 be subject to change ／ be uncertain）
  ★ 为什么改：08-23 组6 的题面后半写成「时间表上还有**一部分**说不准」——
  　「一部分」在中文里是**不可数的量**，最自然的英文就是 `part of the schedule is subject to change`，
  　 可数的 uncertainties 那条路根本不占优。**她当场指出「第二个没必要强行用 uncertainty」，成立。**
  　 改法：中文必须写成**能数出个数的"几处"**（两三处 / 剩下三处），可数复数才有落脚点。
- 2026-08-23（已作废，教练的账）　这个行业的不确定性太大，很多人不敢投钱；不过时间表上还有一部分说不准，年底应该能定下来。
- （建号时）　再周密的计划也留着一部分说不准的地方。（"说不准的地方"用 uncertainty，注意冠词）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `uncertainty`，全档只命中今天作文的记录，零条目 ⇒ 新建。
- 2026-08-22 ❌ D4 复习日 C2·组6 第 9 题（顺带）　**建号后第一次被测就塌**
  她写 `it is always accompanied **with** uncertainty`。正确：`accompanied **by** uncertainty`。
  ★★ **她自己写对过**：08-20 作文 S4 就是 `It is invariably accompanied **by** uncertainty` ——
  　 本条正文里那一行例句就是从她那句抄下来的。今天在**低压的单句里反而退回去了**。
  ⇒ 这说明作文里对的东西**不等于装上了**（那次可能是刚看过范文或当场查过）。
  　 判词纪律：以后不要拿"作文里写对过"当"已掌握"的证据，只当"见过"。
  📋 顺带：「总是」→ always 成立；作文里 `invariably` 更重（#0320 的刻度）。
- 2026-08-23 ✅ D1 学习日 C3·组6 第 4 题　**建号后第一次答对，连对 1**
  题面「这个行业的不确定性太大，很多人不敢投钱；不过时间表上还有一部分说不准，年底应该能定下来。
  （★ 两处都用 uncertainty）」（连对 0 ⇒ 按 §6 给英文词），她写
  `there is **too much uncertainty** in this industry, so many people hesitate to invest.
  However, part of the schedule is still subject to change and should be finalized by the end
  of the year.` 并附一句：**「第二个没必要强行用 uncertainty」**。
  ★ **前半命中考点**：`too much uncertainty` —— **不可数、零冠词**，正是本条"冠词与数"那一层的
  　 上半边；而且 much（不是 many）也证明她把它当不可数处理 ⇒ 连对 1、连错归 0。
  ★★ **她的异议成立，是我的题面出坏了**（§0.8 先当她是对的，复核后确认）：
  ```
  我写的中文是「时间表上还有**一部分**说不准」——「一部分」在中文里是个**不可数的量**，
  忠实直译的落点就是 `part of the schedule is subject to change`，
  而 `a few uncertainties` 要求的是**能数出个数的几处**。
  ⇒ 中文根本没给可数复数留位置，硬要她用就是"为了考点造语境"（§6 明令禁止的那件事）。
  ⇒ 而且她给的 `be subject to change` 是这个中文最自然的英文，比我预设的答案好。
  ```
  ⇒ 题面已改死（见上方 2026-08-23 那行）：改成「还剩**两三处**说不准的地方」。
  ⚠️ 所以本条真正被行使的只有**不可数那一半**；可数复数（a few uncertainties）仍未出场，
  　 但这不是她的账，也不进 REVIEW 池（本条还在池里，下次用新题面正常测）。
  📋 顺带用对：`hesitate to invest`（不定式，正确）· `be subject to change` 是商务/项目语域的地道块 ·
  　 `finalized by the end of the year` 时间介词正确 · `However,` 句首带逗号（＝ #0317 的规矩，对）。
  📋 更好：`Uncertainty in this industry is such that many are reluctant to invest;
  　 two or three points on the timeline **remain uncertain**, though they should be settled
  　 by the end of the year.`（`hesitate to` 偏"犹豫要不要"，中文「不敢」更接近 be reluctant to）

## #0298 keep / reduce sth to a minimum ＝ 把…压到最低
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
```
✅ `they can certainly be **kept to a minimum**`
✅ `**Keep** interruptions **to a minimum**.` · `**reduce** waste **to a minimum**`
⛔ 冠词不能丢：`to **a** minimum` ✅　`~~to minimum~~` ❌（可数单数不能光着，#0074）
```
同族"最低/最大"块（成套记，冠词都要）：
```
keep sth **to a minimum**       压到最低        make the most **of** sth   充分利用
reduce sth **to a minimum**     同上            at **a** minimum          至少
bring sth **to an end**         结束            to **a** large extent     很大程度上
take sth **to an extreme**      走极端          at **the** very least     退一万步说
```
**判据**：这一族都是「to ＋ 冠词 ＋ 名词」的固定形，**冠词是块的一部分，不是可选项**。
★ 写完这类块，回头数一眼冠词在不在 —— 这是它们唯一的高频错法。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
排班的时候要把加班时间压到最低。（"压到最低"那个固定块，别丢冠词）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `minimum` `to a large extent`，全档零命中 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组6 第 7 题　**建号后第一次被测**
  题面「排班的时候要把加班时间压到最低。（★「压到最低」是个固定块，别丢冠词）」，她写
  `When scheduling shifts, overtime hours should be **kept to a minimum**`。
  固定块完整、冠词 **a** 没丢 ⇒ 命中，连对 1。
  ⚠️ 同句一处**按 §0.8 不判错，但要留痕**：`When scheduling shifts, overtime hours should be kept…`
  　 是**悬垂结构** —— 分词的逻辑主语是"排班的人"，主句主语却是 overtime hours。
  　 `When making a claim, evidence should be provided.` 这类在正式书面语里极常见，
  　 母语者例句造得出三个以上 ⇒ 不判错。
  　 **但作文里这算 GRA 桶的悬垂，会吃掉一个干净句。** 已列为条目候选，建不建等她定。
  📋 更好：`When scheduling shifts, **managers** should keep overtime to a minimum.`
- 2026-08-23 ✅ D1 学习日 C3·组6 第 1 题　**连对 2 ⇒ 🎓 毕业**
  题面（零提示，换场景）「施工期间，扬尘必须一直控制在最低。」，她写
  `Dust must be **kept to a minimum** at all times during construction`。
  ★ 固定块完整、冠词 **a** 没丢 ⇒ 命中，连对 2。两次都是被动 `be kept to a minimum`，
  　 08-22 那次带悬垂结构，这次主语直接是 Dust ⇒ **句法比上次干净**。
  📋 顺带用对 #0126：「**一直**」→ `at all times`，修饰层主动落地（而且用的不是 always 这种最省的词）。
  📋 她当场点名要学 `at all times` ⇒ 查重后另建 **#0337**（不是本条的账）。
  📋 更好：〔没有更好的版本〕

## #0299 exceed / outweigh / surpass / outstrip 四个"超过"
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08
⚠️🔍 **REVIEW 池**（靠 ◎✅ 到线；outstrip／surpass 从建号到毕业一次没出场，两次都落在 exceed）

**成员出题账**
```
① exceed    2026-08-22 组5 题面「这笔投资的收益最终会超过投入的成本」⇒ ✅
            2026-08-23 组3 题面「近几年需求已经甩开了供给」⇒ ◎✅（我想要 outstrip）
② outweigh  未出过
③ surpass   2026-08-23 组3 题面「今年的销量则超过了去年创下的纪录」⇒ 未落地（她走 break the record）
④ outstrip  未出过（08-23 那题本想逼它，中文「甩开」没锁住）
```

**问题是什么**
```
exceed     数量上**超出某个界限或数字**（最常用，最安全）
           `the gains **exceed** the losses` · `**exceed** expectations / the limit / 30%`
outweigh   ★ **分量上压过**，专用于"利弊比较"——雅思大作文的核心动词
           `the advantages **outweigh** the disadvantages`
surpass    **超越（某人/某个纪录/某个水平）**，带竞争感
           `**surpass** last year's record` · `**surpass** the average`
outstrip   增长速度上**甩开**，主语常是需求/成本/人口
           `Demand has **outstripped** supply.`
```
**判据**：比的是**数**（exceed）、**分量／利弊**（outweigh）、**名次／水平**（surpass）、
还是**增速**（outstrip）？
★★ 雅思 advantages/disadvantages 题**必须用 outweigh** —— 那是题目本身的词，
　 用它就是在用题目的话回答题目（这正是 #0271 那条规则要的动作）。
⚠️ 四个都是**及物动词**，后面直接跟宾语：`~~exceed than~~` ❌ `~~outweigh over~~` ❌

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
收益最终会超过投入的成本。（"超过"用一个讲数量的词，不是讲利弊的那个）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `exceed` `outweigh` `surpass`，命中的是今天作文与 #0271 的记录，零条目 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组5 第 8 题　**建号后第一次被测**
  题面「这笔投资的收益最终会超过投入的成本。（★「超过」用讲数量的那个词，不是讲利弊的那个）」，
  她写 `the profit of the investment will finally **exceed** the total cost`。
  挑对了讲数量的 exceed，没有走 outweigh ⇒ 命中，连对 1。
  ⚠️ 同句一处不属于本条：`the **profit of** the investment` ⇒ 记 #0293。
  📋 顺带用对 #0280：`the … of the investment` 这个**主语形状**是对的（of 结构做主语）——
  　 组 3 她在 #0280 上失手，同一天在这里自发用对。
  📋 `finally` → `eventually` 更贴"最终"（finally 偏"最后一件事"），但 finally 造得出母语者句 ⇒ 不判。
- 2026-08-23 **◎✅** D1 学习日 C3·组3 第 1 题　**算对，连对 2 ⇒ 🎓 ＋ 进 REVIEW 池**
  题面（**零提示**，本条连对 1 ⇒ 按她 08-23 定的新规则一个提示都不给）
  「近几年需求已经甩开了供给；今年的销量则超过了去年创下的纪录。」她写
  `in recent years, demand has **exceeded** supply, and sales this year have **broken the record** set last year`。
  ★ **为什么算对**（§3.2 判 ❌ 只有两个理由，这两条都不成立）：
  ```
  前半  `demand has exceeded supply` 是标准英语，而且判据第一行"比的是数"正好对上
        （需求与供给就是数量比较）—— 母语者句：`Demand has exceeded supply for months.` /
        `When demand exceeds supply, prices rise.` / `Demand exceeded supply at launch.`
  后半  `break the record` 是"超过纪录"最地道的说法，比 surpass 还常见
        母语者句：`Sales have broken last year's record.` / `She broke the world record.`
  ⇒ 句子本身无错、中文意思全送到 ⇒ 不许判 ❌
  ```
  ⚠️ **没被行使的**：我瞄准的 **outstrip**（增速甩开）与 **surpass**（超越纪录）一个都没出场；
  　 两次被测（08-22、08-23）落地的都是**同一个成员 exceed** ⇒ 正是 REVIEW 池要接的那种情况。
  ★★ **教练侧的账（题面缺陷，不是她的账）**：
  　 中文「甩开」在她的语感里通向"超出"，不通向"增速拉开距离"；「超过纪录」天然通向 break。
  　 而本条连对 1 ⇒ 按新规则**零提示**，我没有任何合法手段把 outstrip／surpass 点出来。
  　 ⇒ 这是「零提示 × 词表型」的结构性后果，本场第 2 次（另一次是 #0278），
  　 　 已连同 #0309 #0268 #0267 一起写进当日 session 的教练侧。
  📋 顺带用对：`sales **this year**`（#0331 时间所有格的替代形状之一，合法）· `the record **set** last year`
  　（后置分词定语，#0284 一族，她今天第二次自发用出来）。

## #0300 play it safe ／ 求稳与冒险这一族习语
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
```
✅ `the cost of **playing it safe**` ＝ 求稳、不冒险的代价
✅ `**play it safe** and stick to what you know`
```
同族（作文里成对用，力量最大）：
```
求稳这边   **play it safe** · **err on the side of caution**（宁可保守）
          · **stay in one's comfort zone** · **take the safe option**
冒险那边   **take a chance / take a gamble** · **stick one's neck out**（出头冒险）
          · **step out of one's comfort zone** · **bet on** sth
```
**语域提醒**：这一族是**习语**，比中性词生动但也更口语。T2 里**一篇用一到两个就够**，
放在**段尾或结论**最合适（那是允许有力度的位置）；正文论证段还是用中性说法
（`avoid risk` · `take a calculated risk`）。
⚠️ `play it safe` 里的 **it 不能换、不能省**，是习语的固定件：`~~play safe~~` ⚠️ 英式口语有，书面写全。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
一味求稳本身也是有代价的。（"求稳"用那个带 it 的习语）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `play it safe` `comfort zone` `take a chance`，全档零命中 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组7 第 8 题　**建号后第一次被测**
  题面「与其冒险，他们宁可求稳。（★「求稳」用一个固定习语）」，她写
  `rather than taking risks, they **play it safe**`。固定习语一次到位 ⇒ 命中，连对 1。
  📋 更好：`they **prefer to** play it safe` —— 中文「**宁可**」是一层取舍，
  　 play it safe 单独用只说了做法、没说这是个选择。
- 2026-08-23 ✅ D1 学习日 C3·组4 第 8 题　**连对 2 ⇒ 🎓 毕业。一题落两个成员，两个都到位**
  题面（零提示）「他这些年一直求稳，从没想过走出自己的舒适区。」，她写
  `he has **played it safe** over the years and has never thought about **stepping out of his
  comfort zone**`。
  ★ 两个成员同时落地：`play it **it** 没丢`（习语的固定件）＋ `step out of one's comfort zone`
  　（同族"冒险那边"的成员，本条正文里列过）⇒ 命中，连对 2。
  ★ 时态也对：`has played … over the years` —— 「这些年一直」配现在完成时，
  　 而且后半 `has never thought` 与它平行。
  📋 顺带用对：`thought **about** stepping`（think about ＋ 动名词，介词与形式都对）。
  📋 这一句是本组唯一一处**零提示、零改动、还带对了第二个成员**的答案。
  📋 更好：〔没有更好的版本〕

## #0301 in advance / beforehand / in anticipation 三个"事先"
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
```
in advance       最通用、最书面      `cannot be quantified **in advance**` · `book **in advance**`
                 也可以带具体时长：`two weeks **in advance**`
beforehand       偏口语，位置更灵活   `We should have checked **beforehand**.`
in anticipation of ＋名词  因为预料到某事而提前做  `stockpiled **in anticipation of** shortages`
prior to ＋名词  正式的"在…之前"     `**prior to** the meeting`（＝ before，但更正式）
```
**判据**：只是"提前" ⇒ in advance；口语场合 ⇒ beforehand；
"因为预料到某事所以提前" ⇒ in anticipation of（这一层 in advance 表达不出来）。
⚠️ 位置：`in advance` 一般放**句末**；放句首要加逗号。
⚠️ `in advance of` ＋ 名词 ＝ 在…之前（`in advance of the deadline`），与 in anticipation of 不同：
　 前者只讲**时间先后**，后者讲**因果加时间**。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
这类代价事先根本算不清楚。（"事先"用最书面的那个）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `in advance` `beforehand` `prior to`，全档零命中 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组9 第 7 题　**建号后第一次被测（成色打折，见下）**
  题面「这类代价事先根本算不清楚。（★「事先」用最书面的那个）」，她写
  `such costs cannot be quantified **in advance**`。挑对了 ⇒ 命中，连对 1。
  📋 顺带用对 #0308：`cannot be **quantified**` —— 组 1 那题她选词就对，这次结构也没出问题。
  ⚠️⚠️ **成色严重打折，是教练的题面出坏了**：
  　 这句几乎就是她作文 S7 的原句（`Such costs cannot be easily quantified in advance`）——
  　 我从她作文里建的条目，出题时又把原句拿回去测，**测的是记忆不是产出**。
  ⇒ **纪律第五条（本日新增）：从作文里建的条目，题面必须换场景。**
  ⇒ 下个周期换语境重测（例如「订票要提前多久」这种完全无关的场景）才算实。
- 2026-08-23 ✅ D1 学习日 C3·组5 第 3 题　**连对 2 ⇒ 🎓 毕业。上一行说的那个"换语境重测"，就是这次**
  题面（零提示）「这家餐厅的位子要提前两周订。」，她写
  `reservations at this restaurant must be made **two weeks in advance**`。
  ★ 与 08-22 那次的关键差别：那次的题面几乎是她作文 S7 的原句（测的是记忆），
  　 **今天换成了订位这个完全无关的场景**，她照样落到 in advance ⇒ 成色补实了，连对 2。
  ★ 而且这次的中文带了具体时长「提前**两周**」—— 本条正文写死 in advance 可以带时长，
  　 而 beforehand 不能（`~~two weeks beforehand~~` 不自然）⇒ **中文本身把目标词锁死了**，
  　 这是组3 那条修法（放一个只有目标能覆盖的语义特征）今天第三次奏效。
  📋 顺带用对：`reservations … must be made` —— 被动 ＋ 复数主语 ＋ 情态，三样都对；
  　 而且 `make a reservation` 比我题面直译的 `book a table` 更书面。**她的比我的好。**
  📋 更好：〔没有更好的版本〕

## #0303 引言里"一直有争论"的一族块
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**成员出题账**
```
📒 2026-08-23 她定的新纪律：出一次补一行
X is debated                     —— 未出过
X is a matter of ongoing debate  —— 未出过
X has long been a subject of debate —— 2026-08-22 ⇒ ✅（整句一字未改）
X has sparked considerable debate —— 2026-08-23 ⇒ ❌（她退回 is a subject of debate，
                                     "引发了"与"相当大的"两层都没送到）
Opinion is divided on X          —— 未出过
There is no consensus on X       —— 未出过
⇒ 下次直接把词写进题面：「★ 用 has sparked」（她 08-23 定）
```

**问题是什么**
```
按长度／重量排（都放在引言第一句）：
`X **is debated**.`                              最短，直接当谓语
`X **is a matter of ongoing debate**.`            中等
`X **has long been a subject of debate**.`        ★ 你用的这个，最稳
`X **has sparked considerable debate**.`          强调"引发了"，主语是那件事
`**Opinion is divided on** X.`                    换个角度：强调两派对立
`**There is no consensus on** X.`                 强调"没定论"
```
**判据**：想说"这事一直在争" ⇒ has long been a subject of debate；
想说"这事**引发了**争论" ⇒ has sparked debate；想说"**两派对立**" ⇒ opinion is divided on。
⚠️ 长度是有代价的：`has long been a subject of debate` 是 8 个词，
　 引言只有两三句，用了它就没预算再铺垫 ⇒ **要么用它，要么直接写 `is debated`，别两个都上**。
★ 与 #0271 配套：引言这一句只负责"这事有争议"，**立场必须另起一句**（见 #0312）。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
要不要让学生带手机进校园，一直有争论。（"一直有争论"用最稳的那个块）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `debate` `consensus` `opinion is divided`，命中的是今天的记录，零条目 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组1 第 6 题　**建号后第一次被测**
  题面「要不要让学生带手机进校园，一直有争论」，她写
  `Whether to allow students to bring their phones to school **has long been a subject of debate**`。
  ★ **整句一字未改** —— 最稳的那个块直接调出来了，长度也控住了（没有再叠第二个争论块）。
  📋 顺带用对：`Whether to allow … **has**`（动名词式长主语配单数，#0055 一族）。
  📋 没有更好的版本。
- 2026-08-23 ❌ D1 学习日 C3·组2 第 9 题　**换成员一测就退回上一次那个块**
  题面「近几年，人工智能会不会取代大量岗位，引发了相当大的争论。
  （★ 必须用"这件事**引发了**争论"那个说法，主语就是那件事本身）」
  她写 `These days, whether AI would replace a large number of works **is a subject of debate**`。
  ★ 判 ❌ 的理由（按她 08-23 定的新判据，只看这两条）：
  ```
  ② 中文的意思没送到 —— 两层都丢了：
     「**引发了**」（这件事把争论**引出来**）→ 她写 is a subject（静态的"是一个话题"）
     「**相当大的**」（considerable）      → 完全消失
     ⇒ 命题从"这件事引爆了很大的争论"退回成"这是个有争议的话题"
  ⛔ 不是因为"没照提示走"才判错 —— 那条今天已经作废（§3.2 新判据）。
  ```
  ⇒ 连对 1 → 0，连错 1。
  ⚠️ **同句一处不属于本条，但更贵**：`a large number of **works**` ——
  　 中文是"**岗位**"，`works` 是"作品／工程"，且 work 表"工作"时**不可数**
  　 ⇒ 想说可数的"岗位"必须换词 **jobs** ⇒ 记 **#0059** ❌（成员表已补 work）。
  📋 △ 不判错：`would replace` —— `Whether AI **would** replace human workers is a subject of debate.`
  　 这类母语者句子造得出三个以上（would 表假设性）⇒ 按 §10 禁令9 不判。更好版用 will。
  📋 △ 不判错：`These days` —— 中文「近几年」更贴 `In recent years`；these days ≈ 如今，
  　 命题没被改写 ⇒ 不判丢层。
  📋 最小修改：`In recent years, whether AI will replace a large number of **jobs**
  　**has sparked considerable debate**.`
  📋 更好：`Whether AI will replace large numbers of **workers** has sparked considerable debate
  　in recent years.`
  ⚠️ **更好版已于当天改过一次（她指出）**：原写的是 `displace large numbers of **jobs**`。
  ```
  她的原话：「你用 jobs，replace jobs 不觉得奇怪么」
  复核：`replace jobs` **不是错**——三个母语者句子造得出：
    "AI could replace 300 million jobs worldwide." /
    "Automation is expected to replace many low-skilled jobs." /
    "These machines will replace the jobs of thousands of workers."
    ⇒ 按 §10 禁令9，不许说它不能这样用。
  但她的语感是对的：**replace 的默认宾语是被顶替掉的那个实体（人），不是那个位置。**
    `replace workers` 远比 `replace jobs` 常见、也更直接。
  ★ 真正的病根在**我的中文题面**：我写的是「取代大量**岗位**」，
    忠实直译只能落到 jobs ⇒ **是我的中文把她推向了一个次优搭配**。
    写「取代大量**工人**」就没这回事。
  ⇒ 新出题纪律（已写进 SKILL §6）：**中文题面发出去之前，自己先直译一遍，
    确认它的直译落点是自然英文搭配**；落点别扭 ⇒ 换中文，不是等她翻出别扭的英文再判她。
  ```

## #0304 than expected / than anticipated —— than 后面省掉主谓
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
```
✅ `far higher **than anticipated**`　＝ than it was anticipated to be（省掉了主谓）
✅ `The results were better **than expected**.` · `sooner **than forecast**`
⛔ 别补全：`~~higher than what was anticipated~~` ⚠️ 语法对但笨重
```
一族（按语域排）：
```
than expected      最通用           than anticipated   更正式 ★ 你用的这个
than forecast      经济/天气语境     than previously thought  强调"以前的看法被推翻"
than usual         比平常            than average       比平均水平
```
**判据**：这一族的共同点是 **than ＋ 过去分词/名词，中间什么都不加**。
★ T1 里非常好用：`The figure rose faster **than forecast**.`
⚠️ 与比较级本身分开记：比较级构形是 #0248（much ＋ 比较级），
　 本条管的是 **than 后面那半截怎么省**，两条互补。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
实际花的时间比预想的长得多。（"比预想的"用 than 后面省掉主谓那个写法）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `than expected` `than anticipated`，全档零命中；与 #0248（much/far ＋ 比较级）互补——那条管 than **前面**，本条管 than **后面**，问 2 不成立 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组8 第 8 题　**建号后第一次被测**
  题面「实际花的时间比预想的长得多」，她写 `it takes a far longer time **than anticipated**`。
  than 后面直接接过去分词、主谓全省 ⇒ 命中，连对 1。
  📋 顺带用对：`**it takes** … time`（#0266 的框架①／②）——
  　 组 2 她在框架③（spend ＋ doing）上失手，这里换了个框架用对 ·`**far** longer`（#0248）。
  📋 更好：`**It took far longer** than anticipated.`
  　（删 `a … time` —— far longer 本身就是时间；`takes`→`took`，中文「实际花的」是已经发生的事）
- 2026-08-23 ✅ D1 学习日 C3·组5 第 2 题　**连对 2 ⇒ 🎓 毕业**
  题面（零提示，换场景）「这次搬迁的花费比原先估计的高出不少。」，她写
  `this relocation cost is much **higher than anticipated**`。
  ★ than 后面**主谓全省**，直接接过去分词 ⇒ 命中，连对 2。两次落地的成员都是 anticipated。
  ⚠️ 与 08-22 那次的差别要说清楚：08-22 的题面是「实际花的时间比预想的长得多」，
  　 和她作文 S4 `far higher than anticipated` 语境接近；今天换成搬迁费用，
  　 **是新语境下的产出**，成色比上次实。
  📋 「原先」没进英文，⛔ **不判 #0126**：`than anticipated` 本身就含"先前估计的"这一层，
  　 删掉「原先」命题没被改写 ⇒ 落在 08-22 收紧判据的不判那一侧。
  📋 更好：`The cost of this relocation **came out** considerably higher than **originally estimated**.`
  　（`the cost of X` 比 `this relocation cost` 少一层名词堆；came out 比 is 更贴"最后算下来"）

## #0305 adapt to / adjust to / get used to / acclimatise to（她自己点名要对比）
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08
⚠️🔍 **REVIEW 池**

**问题是什么**
```
adapt to        ★ **主动改变自己**去适应新环境，最正式、作文首选
                `**adapt to** the new environment` · `Firms must **adapt to** changing demand.`
adjust to       **微调**，幅度比 adapt 小
                `**adjust to** a new schedule`
get used to     **被动地习惯了**，口语；强调"从不习惯到习惯"这个过程
                `It took him months to **get used to** the noise.`
acclimatise to  专指**气候/海拔/环境**的生理适应（英式拼写；美式 acclimate）
```
**三条硬边**
```
① 四个后面都跟**名词或动名词**，不跟不定式
   `get used to **working** nights` ✅　`~~get used to work nights~~` ❌
② `used to do`（过去常做）和 `be/get used to doing`（习惯了）**完全是两回事**
   `He **used to work** nights.`（以前常上夜班）≠ `He **is used to working** nights.`（习惯了上夜班）
③ 作文里默认用 adapt to；get used to 偏口语，除非要强调"熬过来了"
```
★ `struggle to do` 这个框架顺带记：**努力去做但吃力** —— `**struggle to** adapt` ＝ 适应得很吃力，
　比 `find it hard to adapt` 短。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
- 2026-08-23　新的作息只是往前挪了一小时，大部分人两三天就适应了；但上夜班这件事，他花了好几个月才习惯。
- 2026-08-22　他花了整整一个夏天才适应这里的气候。
- （建号时）　刚换城市的人往往要花很久才适应当地的节奏。（"适应"用最正式那个，并注意后面接什么形式）

**成员出题账**
```
① adapt to        —— 2026-08-22 组2 题面「花了整整一个夏天才适应这里的气候」⇒ ✅
                     2026-08-23 组6 前半她又用了一次（intransitive `most people adapted`）
② get used to     —— 2026-08-23 组6 后半题面「上夜班这件事他花了好几个月才习惯」⇒ ✅
                     且宾语是动名词 `working the night shift`，硬边①在场
③ adjust to       —— 未出过（08-23 中文写"只挪一小时、两三天就适应"想逼它，她仍用 adapt
                     ⇒ 见 REVIEW 池题面）
④ acclimatise to  —— 未出过
```

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `adapt` `get used to` `adjust`，全档零命中 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组2 第 8 题　**建号后第一次被测**
  题面「他花了整整一个夏天才适应这里的气候」，她写
  `he spent a whole summer to **adapt to** the environment there`。
  四个里挑了作文首选的 adapt to、后面接名词（硬边①满足）⇒ 命中，连对 1。
  ⚠️ 同句一处不属于本条：`spent a whole summer **to adapt**` ⇒ 记 #0266（spend ＋ 时间 ＋ doing）。
  📋 顺带用对：「**整整**一个夏天」→ `a **whole** summer`，修饰层主动落地（#0126 一族）。
- 2026-08-23 ✅ D1 学习日 C3·组6 第 2 题　**连对 2 ⇒ 🎓 毕业 ＋ 进 REVIEW 池（adjust to 未行使）**
  题面（零提示，一题点两个成员）「新的作息只是往前挪了一小时，大部分人两三天就适应了；
  但上夜班这件事，他花了好几个月才习惯。」，她写
  `the new schedule was only moved up by an hour, and most people **adapted** in just two or
  three days. **working the night shift**, however, took him months to **get used to**.`
  ★ **后半是本条最有价值的一处**：`get used to` 这个成员**从建号到今天第一次出场**，
  　 而且宾语是**动名词** `working the night shift` ⇒ **硬边①（不跟不定式）被行使了**。
  　 她还把动名词整块前置作主语（`Working … took him months to get used to.`）——
  　 这是 `This book took me months to get through.` 那类合法结构，不判错。
  ⇒ 一句里两个成员落地（adapt ＋ get used to）⇒ 命中，连对 2。
  ⚠️ **我瞄的 adjust to 没出来**：中文写了"只往前挪一小时、两三天就适应"（＝微调），
  　 想靠幅度把 adjust 逼出来，她仍然用 adapt。按 §3.2「判 ❌ 只有两个理由」——
  　 `most people adapted in two or three days` 句子成立、意思也送到 ⇒ **不判错**。
  ⇒ 本条真正没被行使的是**判据那一层（按幅度挑 adapt / adjust）**，
  　 按 §3.5 第 3.5 步①「没练过的成员由 REVIEW 池的存档题面承接」⇒ 照常毕业 ＋ 打 ⚠️🔍。
  ★ 教练侧：中文的「适应」对这四个词是**一对多**，光靠幅度形容词（"只挪一小时"）分不开 ——
  　 因为 adapt 在中文里也能说小事。要逼出 adjust 得靠**它专属的宾语**
  　（adjust to a new schedule / adjust the seat）而不是靠幅度副词。修法已写进 REVIEW 题面。
  📋 顺带用对：「只」→ `only`、「就」→ `just`（#0126 两层都落地）·
  　 `moved up by an hour` 用 by 表差额，正确。
  📋 `hour ,` 逗号前多一个空格、两处句首小写 ⇒ §3.2 手滑豁免。
  📋 更好：`The new schedule was moved forward by only an hour, and most people **adjusted** within
  　 two or three days; **working nights**, however, took him months to get used to.`
  　（brought/moved forward 是英式默认；only 挪到 an hour 前面，修饰的才是"一小时"这个量；
  　 分号连两个对比分句比句号紧）
  📋 更好：`the **climate** there`（中文说的是气候；environment 太宽，本条正文里 acclimatise 那一行讲的就是这个分界）。

## #0306 take a dislike / a liking to sb ＝ 莫名地开始不喜欢／喜欢
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
```
✅ `a new line manager simply **takes a dislike to** them`
✅ `She **took a liking to** him at once.`
```
这个块比 `dislike sb` 多两层意思：
```
① **开始**（从中性变成不喜欢，是个转折点）
② **没什么道理**（常和 simply / for no reason 连用）
⇒ `He simply **took a dislike to** her.` ＝ 他就是莫名其妙看她不顺眼
   `He **disliked** her.` ＝ 他不喜欢她（只说状态，不说来由）
```
同族 `take ＋ a ＋ 名词 ＋ 介词`（成套记，冠词都不能丢）：
```
take **a dislike to** sb      take **an interest in** sth     take **offence at** sth（因…生气）
take **a liking to** sb       take **pride in** sth（无冠词）  take **advantage of** sth（无冠词）
```
⚠️ 冠词是块的一部分：`take **a** dislike to` ✅ `~~take dislike to~~` ❌；
　 但 `take pride in` / `take advantage of` **不带冠词** —— 这一族不统一，只能一个个记。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
新来的主管不知为什么就是看他不顺眼。（"看不顺眼"用 take 那个块）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `take a dislike` `take an interest`，全档零命中 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组9 第 8 题　**建号后第一次被测**
  题面「新来的主管不知为什么就是看他不顺眼」，她写
  `for some reason, the new line manager **takes a dislike to** him`。固定块一次到位 ⇒ 命中，连对 1。
  📋 顺带用对 #0307：`the new **line manager**`（职场名词块）。
  📋 时态留痕不判：这个块讲的是**开始不喜欢**那个转折点，常用 `took` ／ `has taken`；
  　 中文「就是看他不顺眼」是已经形成的状态 ⇒ `**has taken** a dislike to him` 更准。
  　 一般现在时表习性也读得通 ⇒ 不判错，只进更好版。
- 2026-08-23 ✅ D1 学习日 C3·组6 第 3 题　**连对 2 ⇒ 🎓 毕业。两个成员跨两次全部覆盖**
  题面（零提示，换场景）「老太太第一眼就喜欢上了这个小护士，倒是对她儿子请的护工怎么都看不上。」，她写
  `the erlerly lady **took an immediate liking to** the young nurse, but she simply could not
  warm up to the caregiver her son had hired`。
  ★ `take **a** liking to` 命中，而且她**在冠词和名词之间插了形容词**（`took an immediate liking to`）——
  　 冠词跟着变成 an，这一步做对说明她是把这个块**当活的结构**在用，不是背死的字符串 ⇒ 命中，连对 2。
  ★ 成员覆盖：08-22 落地的是 `take a dislike to`，今天落地的是 `take a liking to`
  　 ⇒ **两个主成员跨两次全部行使过**，本条不进 REVIEW 池。
  📋 后半 `could not warm up to` 不判错：`warm to / warm up to sb` 成立
  　（`I never really warmed to him.` / `She's starting to warm up to the idea.` /
  　 `The crowd soon warmed to her.` 三条，§0.8）⇒ 意思送到，只是没走 take a dislike to 那条路。
  📋 `erlerly` 是非词（elderly）⇒ §3.2 复习组手滑豁免。
  📋 顺带用对：`the caregiver her son had hired` —— 关系代词省略 ＋ 过去完成时（请在先）两样都对。
  📋 更好：`The elderly lady took an immediate liking to the young nurse, but she simply
  　 **took a dislike to** the carer her son had hired.`
  　（后半改成本条的对举成员，一句里两个块并排，读起来才是"一喜一厌"的对称）

## #0307 职场名词块一族：career progression 及同族
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**成员出题账**
```
① career progression  未出过（08-20 作文里她**自发**用过 ⇒ §6 挂作文验，不出单点题）
② work experience     2026-08-22 组2 顺带 ⇒ ❌（写成 working experience）
③ job security        2026-08-23 组3 题面「这份工作的好处是稳定」⇒ ✅
④ workload            2026-08-23 组3 题面「但工作量确实不小」⇒ ✅
⑤ line manager        08-22 组8/9 顺带用对（📋 不推进），未单独出过
⑥ promotion prospects ／ career path ／ turnover ／ work-life balance　未出过
```

**问题是什么**
```
career progression   晋升通道、职业发展（英式常用）★ 你用的这个
career advancement   同上，美式更常见
promotion prospects  升职前景（复数）
career path          职业路径（一条走法）
job security         工作稳定性（不可数）
workload             工作量（不可数）
work-life balance    工作生活平衡
line manager         直属主管（英式）★ 你这篇也用了
turnover             人员流动率（不可数，`a high staff turnover`）
work experience      工作经验（不可数，⛔ 不是 working experience）（2026-08-22 补）
years' experience    几年经验，注意撇号：`five **years'** experience`
```
**这一族的共同陷阱是【数与冠词】**：
```
不可数、零冠词   job security · workload · career progression（作抽象概念时）
可数、要冠词     a career path · a line manager · a promotion
复数固定         promotion prospects · working conditions · employment opportunities
```
★ T2 工作类题（work / career / employment）几乎每篇都要用其中三四个，成套背最划算。
⚠️ 与 #0270（wage / salary / pay / income / earnings）配套：那条管**钱**，本条管**职位与发展**。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
这家公司的晋升通道很窄，工作量却很大。（两个职场名词块，注意冠词和数）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `career` `progression` `job security`，全档零命中；与 #0270 分的是不同话题域（钱 vs 职位），问 1 不成立 ⇒ 新建。
- 2026-08-22 ❌ D4 复习日 C2·组2 第 9 题（顺带）　~~归入待确认~~ → **已于当日 §8④a 结清，见本块末**
  她写 `more than 5 years **working** experience`。正确：`more than five **years' work** experience`。
  两处：① 块名是 `work experience`，不是按中文「工作经验」拼出来的 working experience
  　　　② 「几年的经验」要所有格撇号：`five years' experience`（＝ experience of five years）
  ⇒ ① 归入本条（职场名词块是固定的，不能自己拼）并把 work experience 补进正文；
  　 ② 是撇号，属于"块记住了、块里的小零件掉了"，挂 reminders.md **R3**，不建条目。
  ⚠️ **归入待确认的理由**：本条建号时列的是 career progression 一族，问 3 存疑 ——
  　 掌握 career progression 未必自动带出 work experience。
  ★★ **2026-08-22 复习日 §8④a 结清：维持归入，「归入待确认」撤销。**
  　 理由与 #0249 相同 —— 本条也是**词表型条目**（正文就是一张职场名词块清单），
  　 问 3 在词表型条目上本来就不该成立，那是这类条目的性质而不是归错。
  ⇒ 按新口径：本条毕业需要**两次连对落在不同成员上**（career progression ／ work experience ／
  　 line manager ／ job security ／ promotion prospects …）。
  　 已有的记录：08-22 组 2 ❌（working experience）· 08-22 组 8/9 顺带用对 line manager（不推进）。
- 2026-08-23 ✅ D1 学习日 C3·组3 第 5 题　**建号后第一次答对，连对 1**
  题面「这份工作的好处是稳定，但工作量确实不小。（★ 用 job security；★ 用 workload）」
  ——★ 本条连对 0 ⇒ 按她 08-23 定的新规则**把目标英文词原样写进括号**，不再绕。
  她写 `the advantage of this job is **its job security**, but **the workload** is rather heavy`。
  ★ 本条真正的陷阱是**数与冠词**，两处都守住了：
  ```
  job security  不可数 ⇒ 不能写 `~~a job security~~` / `~~job securities~~`
                她写 `**its** job security`，物主限定词合法且比裸名词更自然
                （母语者句：`The company is known for **its job security**.`）
  workload      不可数 ⇒ `**the** workload`（特指这份工作的）✅，不是 `~~workloads~~`
  ```
  ⇒ 两个成员同时落地、冠词与数都对 ⇒ 命中，连对 1。
  📋 更好：`the workload is **genuinely heavy**`（或 `is indeed considerable`）——
  　 中文「**确实**不小」是确认语气，`rather` 是程度词，把"确实"这一层换成了"相当"。
  　 ⚠️ 这一处**不记 #0126**：删掉「确实」之后命题不变（工作量大还是工作量大），
  　 　 与 08-22 的「几乎」「往往」不同（那两个删掉会把"允许例外"变成"绝对"，是命题被改写）。
  📋 顺带：`rather heavy` 本身是正确英语；它只在**作文语域**里才有问题（口语对冲词进书面），
  　 而语域按 §6 新规则**一律挂作文验**，中译英单点题不判（同 08-23 组2 的 `a bit heavy` 裁定）。

## #0308 quantify / measure / assess / gauge 四个"衡量"
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08
⚠️🔍 **REVIEW 池**

**问题是什么**
```
quantify  **换算成数字**（最强，强调"给出具体的量"）
          `Such costs cannot be **quantified** in advance.` · `hard to **quantify**`
measure   **测量**，可以是数字也可以是标准
          `**measure** performance / progress / success`
assess    **评估**（综合判断，不一定出数字）★ 学术写作最常用
          `**assess** the impact / the risks / the damage`
gauge     **估摸、摸清**（凭观察，最不精确）
          `**gauge** public opinion / the mood`
evaluate  **评价好坏**（带价值判断）
          `**evaluate** the effectiveness of the policy`
```
**判据**：要不要出**具体数字**？要 ⇒ quantify／measure；不要 ⇒ assess／evaluate；
只是"摸个大概" ⇒ gauge。
★ 作文里最好用的搭配：`difficult to **quantify**` · `**assess** the impact of X` ·
　`**measure** the success of X`。
⚠️ `quantify` 是及物动词，后面必须有宾语：`~~It is hard to quantify.~~` ⚠️ 要补 `quantify **it**`。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
- 2026-08-23　这套流程的效果要先评估一遍；至于员工怎么想，目前只能靠一份问卷大致摸个底。
- 2026-08-22　这项政策的社会影响很难用数字衡量。（"用数字衡量"用最精确的那个词）

**成员出题账**
```
① quantify  —— 2026-08-22 组1 题面「这项政策的社会影响很难用数字衡量」⇒ ✅
② assess    —— 2026-08-23 组4 题面前半「这套流程的效果要先评估一遍」⇒ 她落 **evaluate**（同表成员，判据用对）
③ evaluate  —— 2026-08-23 组4 同上 ⇒ ✅（她自己挑的）
④ gauge     —— 未出过（08-23 中文里点了"大致摸个底"，她用 `get a rough idea` 绕开 ⇒ 见 REVIEW 池题面）
⑤ measure   —— 未出过
```

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `quantif` `assess` `measure` `gauge`，全档零命中 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组1 第 7 题　**建号后第一次被测**
  题面「这项政策的社会影响很难用数字衡量」，她写 `the effect of the policy is difficult to be **quantified**`。
  四个词里挑对了 quantify（＝换算成数字那一个）⇒ **本条考点命中**，连对 1。
  ❌ 同句一处顺带用错（不在本条扣分）：
  　`difficult **to be quantified**` → `difficult **to quantify**` ⇒ 记 #0286
  📋 `the **effect**` → `the **social impact**`：原判 #0126 ❌，**她当场改判为对**
  　（名词前的语境限定语不算丢层，详见 #0126 的更正块）。只作为更好版留痕。
  ⚠️ 教练侧：本题题面与 #0286 的存档触发点「这项政策的长期影响很难衡量」几乎同形，
  　 一道题同时挂了两个考点 ⇒ 收进 §8④ 积压①。
- 2026-08-23 ✅ D1 学习日 C3·组4 第 3 题　**连对 2 ⇒ 🎓 毕业 ＋ 进 REVIEW 池（gauge 未行使）**
  题面（零提示，一题点两个成员）「这套流程的效果要先评估一遍；至于员工怎么想，目前只能靠
  一份问卷大致摸个底。」，她写
  `the effectiveness of this process **needs to be evaluated** first. as for how staff feel,
  we can currently only **get a rough idea** through a survey.`
  ★ **前半命中**：中文"评估一遍"**不出数字** ⇒ 按本条判据该落在 assess／evaluate 那一侧，
  　 她选的 `evaluate` 正在这一侧，而且 `evaluate the effectiveness` 是这个位上的标准搭配
  　 ⇒ 四个词里挑对了那一侧 ⇒ **考点命中**，连对 2。
  ⚠️ **后半的 gauge 没出场**：她用 `get a rough idea` 把它整个绕开了。
  　 按 §3.2「判 ❌ 只有两个理由」：`get a rough idea of what staff think` 完全成立、意思也送到
  　 ⇒ **不判错**。但这是本条第 2 次毕业级判定，`gauge` 与 `measure` 从建号到毕业一次没出过。
  ⇒ 按 §3.5 第 3.5 步①「没练过的成员由 REVIEW 池的存档题面承接，不把条目扣在池里」
  　 ⇒ 照常毕业 ＋ 打 ⚠️🔍 标记 ＋ `review_pool.md` 存题面。
  ★ 教练侧（组3 那条修法的检验）：我在中文里放了"大致摸个底"想把 gauge 逼出来 ——
  　 **没逼出来**。原因是"摸个底"在中文里本身就是**口语的模糊说法**，它对应的英文默认是
  　 `get a rough idea`（一个同样模糊的短语），而不是 `gauge` 这个单词动词。
  　 ⇒ 修法要再加一条：**目标是单词动词时，中文那半句必须写成"书面的动宾"**
  　 （"摸清民意" / "估摸出这批人的态度"），不能写成口语短语，否则英文会照着口语那条路走。
  📋 顺带用对：`the effectiveness of this process **needs**`（长主语的主谓一致，中心词是 of 前面
  　 那个 ⇒ #0048／#0055 一族）· `as for …`（话题转换的正确用法）· `staff **feel**`（不可数集合名词配复数谓语）。
  📋 句首小写两处按 §3.2 手滑豁免。
  📋 更好：`The effectiveness of this process **must be assessed** first; as for **what the staff
  　 think**, at this stage we can only **gauge it** through a questionnaire.`
  　（分号连两个相关分句比句号紧；`what the staff think` 比 `how staff feel` 更书面；
  　 `gauge` 一个词顶掉 `get a rough idea` 四个词）

---

## #0323 reliable / stable / steady / consistent —— 四个"稳"分工不同
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F08

**问题是什么**
中文一个"稳"字通向四个词，**问的问题不一样**：
```
reliable    **靠得住**（能不能指望它） ★ 中文"可靠"永远是这个
            `a **reliable** source` · `**reliable** data` · `The method is not **reliable**.`
stable      **不波动**（会不会变） —— 讲的是数值、局势、状态
            `prices remained **stable**` · `a **stable** job` · `**stable** growth`
steady      **匀速持续**（有没有节奏） —— 常配变化
            `a **steady** rise` · `hold **steady**` · `**steady** progress`
consistent  **前后一致**（这次和上次一样吗）
            `**consistent** results` · `**consistent** with the data`
dependable  ＝ reliable，偏口语，作文不用
```
**判据**：问一句"我说的是**靠不靠得住**，还是**变不变**？"
　靠不靠得住 ⇒ reliable　｜　变不变 ⇒ stable（不动）／ steady（匀速动）／ consistent（次次一样）
⚠️ 最容易串的一对：`not stable`（时好时坏、在波动）≠ `not reliable`（指望不上）。
　 `These therapies are not stable` ＝ 疗法本身在变；`not reliable` ＝ 不能指望它管用。
★ 反过来的说法（写议论文常用）：`can hardly be called reliable` ／ `is far from reliable`
　—— 比 `is not reliable` 更贴中文的"谈不上可靠"。

**怎么发现的**
2026-08-22　D4 复习日 C2·组2 第 3 题（顺带）。主考点是 #0109。

**我错在哪**
她的：`these therapies only work occasionally but are not **stable**`
正确：`… but are not **reliable**` ／ `… and **can hardly be called reliable**`
题面写的是「谈不上**可靠**」——"可靠"问的是能不能指望，不是会不会波动。

**中文触发点**
网上查到的数据不一定可靠，最好回原始报告核一遍。

### 历史记录
- 2026-08-22 ❌ 建号　D4 复习日 C2·组2 第 3 题（顺带）
  查重（§3.5 B0）：grep 了 `reliable` `stable` `steady` `consistent`，全档命中两处，逐条比对：
  · #0? 的 `kept stable` → `remained stable`（F01 动词框架）：改正动作是**换动词**（keep→remain），
    本条是**换形容词**（stable→reliable），问 1 不成立
  · #0110（steadily 一族）：那条排的是**副词的幅度刻度**，本条分的是**形容词问的问题不同**，
    问 2 不成立（要另起一句话讲）
  又查了 F08 里现成的四个"辨析组"条目 #0299（四个"超过"）#0308（四个"衡量"）
  #0305（四个"适应"）#0295（"建立在…之上"），都是别的词族 ⇒ 新建。
  ⚠️ 不适用 SKILL §2 排除项⑤：本条是**选词知识**不是构形，她没有"低压写对过两次"的记录。
- 2026-08-22 ✅ D4 复习日 C2·组9 第 10 题　**判 ✅ 但不推进 streak（同日口径）**
  题面「网上查到的数据不一定可靠，最好回原始报告核一遍」，她写
  `data found online is not necessarily **reliable**`。
  ★ 挑对了 —— 「可靠」问的是**靠不靠得住** ⇒ reliable，没有再写 stable ⇒ 考点命中。
  ⚠️ 但**本条今天上午才建号（组 2，符号 ❌）**，按 §3.2 同日口径当天净结果仍是 ❌
  　 ⇒ 本行只留证据，连对 0／连错 1 维持不变。
  　 真正的证据要等下个周期换语境再测（"刚教完就测"不算）。
  📋 顺带用对 #0284：`data **found** online`（后置分词定语）。
  📋 `data … **is**` 留痕不判：学术写作传统上 data 配复数（`data **are**`），
  　 但 `The data is clear.` 母语者例句造得出三个以上 ⇒ §0.8 不判错，更好版按 are 写。

---

## #0326 impact / effect / influence / consequence 四个"影响"
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F08

**问题是什么**
```
impact       **冲击力大、后果明显**，可数，★ 议论文里最常用
             `the **social impact of** this policy` · `have a **major impact on** X`
             `the environmental / economic / long-term **impact**`
effect       **中性的结果**，最通用；可数也可不可数
             `the **effect of** X **on** Y` · `have a **positive effect on**` · `side effects`
influence    **潜移默化的作用**（改变的是想法、风气、选择，不是数字）
             `parental **influence on** children` · `**influence** public opinion`
consequence  **后果**，几乎总是**负面**、且是"因此带来的"
             `the **consequences of** inaction` · `**serious consequences**`
implication  **隐含的后续影响**（政策/研究常配）　`the policy **implications**`
```
**判据（一句话）**：
　冲击大不大 ⇒ **impact**　｜　只是结果 ⇒ **effect**
　改变的是人的想法 ⇒ **influence**　｜　是负面的后果 ⇒ **consequence**
**三条硬边**
```
① 介词写死：**impact / effect / influence ON** X，⛔ 不是 to／for
   `a major impact **on** the industry` ✅　`~~impact to the industry~~` ❌
② impact 作**动词**时是及物的，不加介词：`This will **impact** sales.`（美式常见，英式偏好 affect）
   ⚠️ 作文里名词用 impact、动词用 affect，最稳
③ 前面挂形容词是这一族的主要产出方式，成套记：
   social / economic / environmental / long-term / lasting / far-reaching / devastating ＋ impact
```
★ 与 #0308（quantify 一族）配套：`It is difficult to **assess the impact of** X` 是作文最好用的一整块。

**怎么发现的**
2026-08-22　D4 复习日 C2·组1 第 7 题。她写 `the **effect** of the policy`，
中文是「这项政策的**社会影响**」——**她当场裁定这不算丢层**（名词前的语境限定语不判，见 #0126），
但她同时点名：**impact 这个词建个新条目**（§2③）。

**我错在哪**
她这次**不算错** —— `the effect of the policy` 本身成立。
建号理由是 §2③（她点名要学）。缺口在于**这一族的分工与那个介词 on**。

**中文触发点**
这项改革对小企业的冲击比谁都大。（★「冲击」用讲后果大小的那个名词，注意它配哪个介词）

### 历史记录
- 2026-08-22 ③ 建号（她点名要学）D4 复习日 C2·组1 第 7 题
  查重（§3.5 B0）：grep 了 `impact` `effect` `influence` `consequence` `影响`，全档命中四处，逐条比对：
  · #0007（effective **in** some cases）· #0042（are rarely effective）· #0174（not only ineffective…）
    —— 三条都讲 **effective 这个形容词**的用法，不是"影响"这个名词族，问 1 不成立
  · #0199（影响了全世界 —— affects → has affected）：讲的是**时态**，问 1 不成立
  · #0308 正文里出现过 `assess the impact`，但那条管的是"衡量"那四个动词，impact 只是宾语，问 2 不成立
  ⇒ 全档零条目讲这一族 ⇒ 新建，与 #0308 交叉引用。

---

## #0327 established practice ／「公认的做法」一族
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F08

**问题是什么**
"大家都这么做／公认的做法"在英文里是几个**固定名词块**，不是临时拼的：
```
established practice   **已经定下来的做法**（最常用，正式）　`It is established practice to…`
accepted approach      **被接受的路子**（强调没人反对）
standard procedure     **标准流程**（有明文的那种）　`standard operating procedure`
common practice        **普遍做法**（不一定正规，只是大家都这么干）
best practice          **最佳实践**（行业推荐的做法，不可数）　`follow best practice`
conventional wisdom     **通行的看法**（常用来引出你要反驳的观点）★ 议论文很好用
```
**判据**：说的是**做法** ⇒ practice／approach／procedure；说的是**看法** ⇒ conventional wisdom。
　正规程度：best practice ＞ standard procedure ＞ established practice ＞ common practice。
**两条硬边**
```
① ⛔ `acknowledged` 多用于**人或身份**，不修饰做法：
   `the **acknowledged** expert / leader` ✅　`~~the acknowledged method~~` ⚠️
② practice（名词）↔ practise（动词，英式）拼写别串 —— 见 #0059
   `It is established **practice**` ✅（名词）　`They **practise** it daily` ✅（动词）
```
★ 议论文里的用法：`**Conventional wisdom** holds that X; in practice, however, …`
　—— 先立一个通行看法再推翻，是最省的一种展开方式。

**怎么发现的**
2026-08-22　D4 复习日 C2·组6 第 6 题。题面「公认的做法是先做小规模试点」，
她写 `the **acknowledged method**` —— 结构（过去分词作前置定语）是对的、命中 #0277，
但词选偏了一格。**她当场点名：这个块建个条目**（§2③）。

**我错在哪**
她的：`the **acknowledged method** is to do it on a small scale`
正确：`The **established practice** is to start with a small-scale pilot.`
★ 结构不算错（#0277 已判命中），错的是**挑哪个词** —— acknowledged 修饰人不修饰做法。

**中文触发点**
业内公认的做法是先在一个城市试点，跑通了再推开。（★「公认的做法」用一个固定名词块，⛔ 不许用 acknowledged）

### 历史记录
- 2026-08-22 ③ 建号（她点名要学）D4 复习日 C2·组6 第 6 题
  查重（§3.5 B0）：grep 了 `established practice` `accepted approach` `common practice`
  `conventional wisdom`，全档**零命中**（只有当日 session 里我给的更好版）⇒ 新建。
  又比对 #0277（过去分词当前置定语）：那条管**句法位置**（分词能不能坐在名词前），
  本条管**挑哪个分词/名词块**，问 1 不成立 ⇒ 两条配套但不合并，交叉引用。

---

## #0332 bear ＋ 抽象名词：承担／带有／经得起（不是"熊"，也不是"忍受"）
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08
🔵 §2③ 她点名要学（2026-08-23，原话：「**bear little relation. 这里 bear 我不会用，可以建个条目练习下**」）

**问题是什么**
`bear` 在书面英语里是一个**高频的正式动词**，后面跟一小批固定的抽象名词。
她现在只认识"忍受"那个义项，所以整条路用不出来。**按意思分四组：**
```
① 有／带有某种关系或相似  ★ 就是她点名的这个
   bear **little relation to** sth      和…没什么关联（比 has nothing to do with 正式）
   bear **no relation to** sth          和…毫无关系
   bear **a resemblance to** sb/sth     和…有相似之处
   bear **a close relationship to** sth 和…关系密切

② 承担（责任、成本、后果）—— T2 高频
   bear **the cost** of sth             承担…的成本
   bear **responsibility** for sth      对…负责
   bear **the brunt** of sth            首当其冲承受…（最常配 the poorest / low-income families）
   bear **the burden** of sth           背负…的负担

③ 经得起（检验、推敲）
   bear **scrutiny**                    经得起细看          `The claim does not bear scrutiny.`
   bear **comparison with** sth         比得上…
   ★ 常用否定：`will not bear close examination`

④ 记在心里 / 结果实
   bear **in mind** that…               记住…（写作里常用 `It should be borne in mind that…`）
   bear **fruit**                       见成效（比 yield results 更像成语）
```
**变形要记住**：bear – **bore** – **borne**（不是 beared，也不是 born）。
```
✅ The cost was **borne** by the government.
⛔ ~~was beared~~　⛔ ~~was born~~（born 只用于"出生"）
```
**判据**：想说的是「**有关系／承担／经得起**」这三件事之一 ⇒ bear 那一族；
　　　　只是「忍受得了」的日常口语 ⇒ 用 stand / put up with，别用 bear。
★ 与她已有条目的分工：
```
#0292 carry ＋ 抽象名词 ＝ 自带、附带（`carries the lowest payoff`）
#0332 bear ＋ 抽象名词 ＝ 承担、有关系、经得起
两个都是"抽象名词配一个具体动词"，但 carry 是**自身带着**，bear 是**扛下来／对得上**。
```

**怎么发现的**
2026-08-23　D1 学习日 C3·组1 第 8 题的更好版 `the figures **bear little relation to** the conclusion`。
她看到后当场点名要学（§2③）。

**我错在哪**
她这次**没有错**（她写的 `hardly connects with` 成立）。建号理由是 §2③ ——
**她主动说"这里 bear 我不会用"**。缺口是整个 bear 族在她的产出里零出现。
找法：**要写"承担成本／负主要责任／和…没什么关系／经不起推敲"时，先想一次 bear。**

**中文触发点**
这两组数据其实没什么关联；而不管结论怎么定，成本最后还是由低收入家庭承担。
（★ 两处都必须用**同一个动词**的不同搭配：「没什么关联」· 「承担成本」）

**成员出题账**
```
① bear little / no relation to               —— 未出过
② bear the cost / responsibility / the brunt —— 未出过
③ bear scrutiny / comparison                 —— 未出过
④ bear in mind / bear fruit                  —— 未出过
```

### 历史记录
- 2026-08-23 ③ 建号（她点名要学）D1 学习日 C3·组1 第 8 题的更好版
  查重（§3.5 B0）：grep 了 `bear` `承担` `responsibility` `burden` `resemblance`，全档命中两处 ——
  · **#0292**（carry ＋ 抽象名词 ＝ 自带、附带）：同为"抽象名词配具体动词"，但语义不同
    （carry ＝ 自身带着 / bear ＝ 扛下来、对得上），改正动作也不同 ⇒ 问 1、问 2 都不成立。
  · **#0309**（irrelevant to / unrelated to / has nothing to do with）：`bear little relation to`
    与它同义，但 #0309 已于今天毕业进 REVIEW 池，而且那条管的是**形容词那条路**；
    本条管的是 **bear 这个动词的整族搭配**（承担／经得起／记住三组与"关系"无关）
    ⇒ 问 3 不成立（会用 irrelevant to 不会让人自动会用 bear the brunt of）。
    ⚠️ 两条交叉引用：#0309 的"更好版"里出现的 bear little relation to 就是本条的成员。
  反向验（§3.5 1.3）：她 08-22、08-23 两次都写对 `irrelevant to`（#0309），
    而 bear 一族一次没出现过 ⇒ 可独立取值 ⇒ 不合并。
  ⇒ 新建。建号时无对错，连对连错都是 0。
  ⚠️ 本条是**词表型**（§3.5）：出题必须**直接点名要哪一组／哪一个搭配**
  　（她 2026-08-23 定的新出题纪律），并逐条记下"哪个成员用过哪个题面"。
  ⇒ 成员出题账已挪到上方条目正文（2026-08-24 格式统一，内容一字未改）。

## #0328 enrolment ／「报名与在册人数」名词块一族
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F08

**问题是什么**
```
enrolment    **在册／报名人数**（英式；美式 enrollment）—— ★ 讲"多少人报了名"用它，不可数
             `**Enrolment on** this course has risen sharply.` · `**enrolment figures**`
             `university **enrolment**` · `a sharp fall in **enrolment**`
registration **注册这个动作／手续**，可数也可不可数
             `**Registration** closes on Friday.` · `complete your **registration**`
admission    **准入／录取**（能不能进得来）　`university **admissions**` · `**admission** requirements`
intake       **一次招进来的那一批人**（英式）　`this year's **intake**` · `student **intake**`
attendance   **实际到场／出勤**（报了名不等于来了）　`**attendance** at lectures`
```
**判据**：
　多少人**报了名／在册** ⇒ **enrolment**　｜　报名这个**手续／窗口** ⇒ **registration**
　能不能**被录取** ⇒ **admission**　｜　招进来的**那一批** ⇒ **intake**　｜　实际**来了几个** ⇒ **attendance**
**三条硬边**
```
① 介词写死：`enrolment **on** a course`（英式）／ `enrolment **in** a programme`（美式）
② ⛔ 别用 `the number of registrations` 这种长块 —— `enrolment` 一个词就够（2 词顶 6 词）
③ 这一族配的动词是图表语域那一套：`enrolment has **risen / fallen / remained stable**`（见 #0110）
```
★ 与 #0264（sign up ／ sign in）分工：那条管**动词短语**（报名这个动作怎么说），
　本条管**名词块**（报名的人数／手续怎么说）。作文里几乎只用得到名词块。

**怎么发现的**
2026-08-22　D4 复习日 C2·组6 第 8 题。她写
`the number of registrations for this kind of class has grown rapidly`，
整句正确、#0194 的时态考点也命中，我在更好版里给了 `Enrolment on courses of this kind has risen sharply`。
**她当场点名：enrolment 建个条目**（§2③）。

**我错在哪**
她这次**不算错** —— `the number of registrations for…` 完全成立。
建号理由是 §2③（她点名要学）。缺口在于**这一族的名词块与它们的分工**，
以及"6 个词的长块能压成 2 个词"这个产出方式。

**中文触发点**
这门课这两年的报名人数掉得很快，到课率也不如从前。（★「报名人数」和「到课率」各用一个名词块）

### 历史记录
- 2026-08-22 ③ 建号（她点名要学）D4 复习日 C2·组6 第 8 题
  查重（§3.5 B0）：grep 了 `enrol` `registration` `admission` `intake`，命中两处：
  · **#0264**（sign up／sign in）正文里提过 `register / enrol` 与 `Registration closes on Friday`
    —— 但那是那条的**顺带补充**，它的考点是"动词换小品词就是另一件事"，
    改正动作是**挑对小品词**，本条是**挑对名词块**，问 1 不成立 ⇒ 不合并，交叉引用。
  · #0307（职场名词块一族）：话题域不同（职位与发展 vs 报名与在册），问 1 不成立。
  ⇒ 新建。
  ⚠️ 本条是**词表型条目**（§3.5）：出题必须一句里覆盖两个以上成员，
  　 且毕业前要覆盖过至少两个不同成员（她 2026-08-22 定的口径）。

## #0335 「要过很久才…」一族：not … until ／ not … for ＋ 时段
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
中文「**要等到很久以后才**看得出来」，英文的骨架是**否定 ＋ until／for**，不是"等到…才"逐字翻。
```
✅ `The results **will not become apparent for many years**.`        ← 最省，作文首选
✅ `The results **will not become apparent until much later**.`
✅ `It **was not until** 2015 **that** the policy took effect.`       ← 强调句，正式
```
**三条路怎么挑**
```
not … for ＋ 时段     说的是**要花多久**       will not pay off **for a decade**
not … until ＋ 时点   说的是**要到哪个时候**   will not be clear **until the next census**
not until … that      同上，但**句首强调**     It was not until last year that …
```
**「很久以后」这个位上的几个说法（按语域排）**
```
for many years / for years to come   最省、最书面 ★ 首选
until much later                     中性
well into the future                 可以，`well` 是这个块里的默认副词
long into the future                 ⚠️ 存在（`the debate will continue long into the future`），
                                     但它更常配**持续性动词**（continue / last / go on）；
                                     配 become clear 这种**变化点**动词就别扭
far into the future                  多用于 plan / look（`plan far into the future`）
```
**判据**：动词是**变化点**（become clear / take effect / pay off）⇒ 用 `not … for ＋ 时段`；
动词是**持续**（continue / remain / last）⇒ 才轮到 long / well into the future。
⚠️ 与 #0324（真实条件句）无关；与 #0234（口语块换书面块）也不是一条 —— 那条管语域，本条管**结构**。

**怎么发现的**
2026-08-23　D1 学习日 C3·组4 第 1 题（主考点是 #0280）。她写
`the true value of this reform will not become clear util long into the future`，
并当场点名：**「until long into the future 新建条目」**（§2③ 她点名要学）。
查重（§3.5 B0）
```
① 词面查  dedup "until" "not until"        ⇒ 命中 #0234 #0324 #0093 #0289
② 规则查  dedup "直到" "才" "时间状语"       ⇒ 命中 #0220 #0016 #0018 #0062 #0087 #0128
逐条否掉
  #0234  语域条目（口语块→书面版），until 只出现在它的更好版 `do not finish work until late` 里。
         问 1：那条的改正动作是"把口语词换成书面词"，本条是"用否定 ＋ until/for 搭时间落点" ⇒ 否
  #0324  真实条件句（从句现在时、主句带 will），until 只是例句里顺带出现 ⇒ 问 1 不成立 ⇒ 否
  #0093 #0289  until 命中在触发点／历史记录的正文里，与考点无关 ⇒ 否
  #0220  T1 的"此后再没回到峰值"，管的是**图表叙述的时间参照**，不是这个句法框架 ⇒ 否
  #0016 #0018 #0062 #0087 #0128  只因中文"才"字命中，考点毫无关系 ⇒ 否
```

**我错在哪**
她的：`will not become clear **until long into the future**`
正确：`will not become apparent **for many years**` ／ `**until much later**`
　　　（她的不算错 —— `not … until` 的骨架她已经有了；缺口是**"很久以后"这个位上有哪几个词、
　　　　哪个配变化点动词**。这是 §2③ 建号，不是记她的错。）
**找法**：写完「要过很久才…」这一句，回头看动词 ——
　　　　是"某一刻发生的变化"就换成 `not … for ＋ 时段`，最短也最稳。

**中文触发点**
这批树苗要过十来年才成材，现在看不出什么。

### 历史记录
- 2026-08-23 ③ 建号（她点名要学）D1 学习日 C3·组4 第 1 题
  她写出 `will not become clear until long into the future` 并说「这个新建条目练习下」。
  ★ 她的骨架（not … until）是对的，值得先说清楚：**这一族她已经有一半**。
  　 建号收的是另一半 —— "很久以后"那个位上的成员表 ＋ 怎么按动词类型挑。
  ⚠️ 触发点已换场景（树苗），⛔ 不许拿组4 那句"改革的价值"回来测（§6）。

## #0336 「所谓 X，说白了就是 Y」怎么说 —— ⚠️ so-called 在英语里几乎总带贬义
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
中文的「所谓」是**中性的**（＝"人们说的那个 X"）；英文的 `so-called` **几乎总是带贬义**，
意思是"号称是、其实不配"。直接对译会把语气整个改掉。
```
⛔ `**so-called** experts`        ＝ 那帮所谓的专家（＝我不认为他们是专家）
⛔ `the **so-called** reform`     ＝ 那个所谓的改革（＝我认为它不算改革）
⇒ 只有当你**确实想表达质疑**时才用 so-called。中性的"所谓"要换别的说法。
```
**中性的"所谓 X"，三条路**
```
① what is known as ＋ 名词     `**what is known as** the gig economy`     ★ 最中性、最书面
② what people call ＋ 名词     `**what people call** work-life balance`   略口语，好用
③ what we mean by ＋ 名词      `**what we mean by** a good school`        用于下定义
④ the term X refers to …       `**The term** burnout **refers to** …`     最正式，学术定义句
```
**「所谓 X，说白了就是 Y」这个整句，最省的是把"所谓"直接吃掉**
```
✅ `**Leading a team comes down to** three things: …`        ← 你 08-23 写的就是这个，完全成立
✅ `**What leading a team really comes down to is** …`       ← 想保留"所谓…说白了"的对举语气
✅ `**Stripped of the jargon,** leadership is simply …`      ← 带一点"别绕弯子"的口气
⇒ 中文的「所谓…说白了就是…」是**一个语气**（先把大词摆出来、再拆穿它），
　 英文不靠一个词承担，靠 `really / actually / simply / comes down to` 这类词。
```
**判据**：这句里的「所谓」是**中性转述**还是**带质疑**？
　中性 ⇒ what is known as／直接吃掉；带质疑 ⇒ so-called（而且要有下文说明你为什么质疑）。

**怎么发现的**
2026-08-23　D1 学习日 C3·组5 第 5 题（主考点是 #0285）。题面「**所谓**带团队，说白了就是三件事」，
她写 `Leading a team comes down to three things: …`（把"所谓"整个吃掉，完全成立），
并当场点名：**「（所谓可以建个条目专门练习下）」**（§2③ 她点名要学）。
查重（§3.5 B0）
```
① 词面查  dedup "so-called" "known as" "in essence"  ⇒ 命中 #0277
② 规则查  dedup "所谓" "说白了" "贬义"                ⇒ 命中 #0278 #0280（都只是正文里出现"贬义"二字）
逐条否掉
  #0277  guaranteed/proven/established 过去分词作前置定语 —— so-called 只是它词表末尾的一个成员，
         那条的改正动作是"把'公认的'用一个过去分词直接放名词前"，本条是
         "中文'所谓'该不该译成 so-called、不译又怎么说"。问 1、问 2 都不成立 ⇒ 否，两条交叉引用
  #0278  proactive/reactive —— 只因正文里有"贬义"二字命中，考点无关 ⇒ 否
  #0280  the cost of ＋ X —— 只因历史记录里评 stagnant 时写过"贬义"⇒ 否
```

**我错在哪**
她这次**没有错** —— 她把"所谓"吃掉的处理完全成立、而且是英文里最省的一条路。
建号理由是 §2③（她点名要学）。缺口在于：**中性的"所谓"有哪几种说法，以及 so-called 的贬义陷阱**。
**找法**：中文写着「所谓」，先问一句"**我是不是在质疑它**"——
　　　　不是 ⇒ ⛔ 别写 so-called；要么用 what is known as，要么整个吃掉。

**中文触发点**
所谓弹性工作，说白了就是把加班挪到了家里。

### 历史记录
- 2026-08-23 ③ 建号（她点名要学）D1 学习日 C3·组5 第 5 题
  她自己写的 `Leading a team comes down to three things` 已经是这一族里最省的解法，
  ⇒ 本条收的不是"她不会"，是**so-called 这个陷阱 ＋ 中性说法的成员表**。
  ⚠️ 触发点已换场景（弹性工作），⛔ 不许拿组5 那句"带团队"回来测（§6）。

## #0337 `at all times` ＝ 任何时候都（规定语域）—— ⚠️ 和 `at times` 只差一个 all，意思正相反
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F08

**问题是什么**
```
✅ `Dust must be kept to a minimum **at all times**.`（＝任何时刻都不许有例外）
✅ `Hard hats must be worn **at all times**.` · `Staff must remain contactable **at all times**.`
⚠️⚠️ `**at times**` ＝ **有时候、偶尔** —— 只差一个 all，意思正相反：
　　`The road is **at times** impassable.` ＝ 这条路偶尔不通
　　`The road is **at all times** impassable.` ＝ 这条路任何时候都不通
★ 这是本条最值钱的一行：写完 at all times，回头确认那个 **all** 在不在。
```
**语域**：at all times 是**规章、告示、安全守则**的默认块，常配 must / should / be required to。
学术议论文里用得少；T2 里适合放"规定/义务"这类句子。

**同族"始终／一直"的块，按语境分**
```
at all times        任何时刻都不许有例外（规定）      ★ 配 must / should
throughout          贯穿某一整段时间                 `throughout the project` · `throughout the year`
consistently        表现一贯（＝#0320 的刻度表）      `consistently good`
constantly          不停地，**常带负面**             `constantly interrupted`
continuously        不间断（时间上连着）              ⚠️ 与 continually（反复地，中间有断）不是一个词
round the clock     24 小时轮着                      偏口语／新闻
on an ongoing basis 持续地                           商务书面
```
**判据**：说的是"**任何一刻都不许有例外**"（规定） ⇒ at all times；
　"整段时间里都" ⇒ throughout；"表现一贯" ⇒ consistently（#0320）；"不停地、烦人地" ⇒ constantly。
⚠️ 位置：at all times 一般放**句末**；放句首要加逗号。

**怎么发现的**
2026-08-23　D1 学习日 C3·组6 第 1 题（主考点是 #0298）。她写
`Dust must be kept to a minimum **at all times** during construction`，
并当场点名：**「这个 at all times 可以加一个条目」**（§2③ 她点名要学）。
查重（§3.5 B0）
```
① 词面查  dedup "at all times" "at times" "always"  ⇒ 命中 #0320 #0108 #0136 #0276 #0297
② 规则查  dedup "频率" "始终" "一直"                 ⇒ 命中 #0320 #0108 #0226 #0303 #0253
逐条否掉
  #0320  频率副词的刻度 always/invariably/consistently/rarely/seldom（已 🎓）——
         三问：问1 改正动作？那条是**在五个副词里挑对刻度**，本条是**一个介词短语块**该不该用、
         别和 at times 串台 ⇒ 否。问3 会挑 invariably 完全不保证会用 at all times ⇒ 否。
         ⇒ 不合并，**交叉引用**（"表现一贯"那一格指向 #0320）
  #0108  「这个副词可以放 is 后面么」—— 管的是**副词位置**，本条管**选哪个块** ⇒ 问 1 不成立 ⇒ 否
  #0136 #0276 #0297 #0226 #0303 #0253  只因正文里出现 always／一直／频率等字命中，考点无关 ⇒ 否
```

**我错在哪**
她这次**没有错** —— `at all times` 用得完全正确，位置（句末前）也对。
建号理由是 §2③（她点名要学）。缺口在于：**at times 这个陷阱** ＋ **同族其余成员的分工**。
**找法**：写完「一直／任何时候」这一层，问两句 ——
　　　　① 我说的是"不许有例外"还是"偶尔"？② 那个 **all** 在不在？

**中文触发点**
实验室里任何时候都必须戴护目镜；走廊那台老机器倒是只偶尔响一下，不用管。

### 历史记录
- 2026-08-23 ③ 建号（她点名要学）D1 学习日 C3·组6 第 1 题
  她自己写出 `at all times` 并说「这个可以加一个条目」。
  ⇒ 本条收的不是"她不会"，是 **at times 的反义陷阱 ＋ 同族分工**。
  ⚠️ 触发点已换场景（实验室），⛔ 不许拿组6 那句"施工扬尘"回来测（§6）。

---

# F09 时态/体

> 时态选择、时间状语与时态的配对、体的平行

## #0190 「这里可以换成 might 么」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F09

**问题是什么**
K　0/3

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：在某些情况下**可能**有效
正确：may／might 近等价（might 更弱）；此处 `can be effective in…` 最准（客观上存在这种情况）

**中文触发点**
这种疗法在某些情况下确实是有效的。（★ 说的是"客观上存在这种可能"，用 can）
（旧留痕：「这里可以换成 might 么」—— may／might 近等价、might 更弱；
　但本句要的是客观可能性，can 最准）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-092）</summary>

`「这里可以换成 might 么」|在某些情况下**可能**有效|may／might 近等价（might 更弱）；此处 `can be effective in…` 最准（客观上存在这种情况）|**K**|0/3|`

</details>

## #0191 越来越多人转向替代疗法
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F09

**问题是什么**
第②类　不出中译英

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：the trend towards trying… is growing rapidly（**内容全送到了**：趋势在增长＝越来越多人转向）
正确：**08-16 改判第②类**：差别只是名词化 vs 直陈 SVO；且 more and more people **turn** to（一般现在时）同样成立，连时态都抓不出错 ⇒ 判不出 ❌

**中文触发点**
越来越多人转向替代疗法

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-103）</summary>

`越来越多人转向替代疗法|the trend towards trying… is growing rapidly（**内容全送到了**：趋势在增长＝越来越多人转向）|**08-16 改判第②类**：差别只是名词化 vs 直陈 SVO；且 more and more people **turn** to（一般现在时）同样成立，连时态都抓不出错 ⇒ 判不出 ❌|第②类|不出中译英|`

</details>

## #0196 这项政策大幅推迟了退休年龄，从 60 岁到 65 岁
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F09

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：This policy significantly raises…
正确：This policy **has significantly raised** …（中文"推迟**了**"＝已完成并延续到现在 → 完成时；**纯时态选择，第②类不进中译英组，作文里验**）

**中文触发点**
这项政策大幅推迟了退休年龄，从 60 岁到 65 岁

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-197）</summary>

`这项政策大幅推迟了退休年龄，从 60 岁到 65 岁|This policy significantly raises…|This policy **has significantly raised** …（中文"推迟**了**"＝已完成并延续到现在 → 完成时；**纯时态选择，第②类不进中译英组，作文里验**）|待排序|U（待定）|`

</details>

## #0198 「这个 will 要不要」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F09

**问题是什么**
K（判据）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：医生会给出关于下一步该怎么做的指引
正确：**两个都对，看你在说什么**：`Doctors **provide** guidance…`＝陈述职责/一般规律（T2 里说"医生的角色"用这个）；`Doctors **will** provide…`＝具体情境里将会发生（"如果病人问，医生会…"）。<br>⛔ 真正错的是第三个：`would` ＝虚拟/委婉（E-079 的原错），事实陈述里不能用<br>★ 你这次自发用 will 没用 would ⇒ **E-079 顺带判 ✅**

**中文触发点**
医生会就下一步怎么办给出指引。（★ 说的是医生的一般职责，不是某一次具体情境）
（旧留痕：「这个 will 要不要」—— 两个都对：一般规律用一般现在时，具体情境才用 will。
　⛔ 真正错的是 would，事实陈述里不能用）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-216）</summary>

`「这个 **will** 要不要」|医生会给出关于下一步该怎么做的指引|**两个都对，看你在说什么**：`Doctors **provide** guidance…`＝陈述职责/一般规律（T2 里说"医生的角色"用这个）；`Doctors **will** provide…`＝具体情境里将会发生（"如果病人问，医生会…"）。<br>⛔ 真正错的是第三个：`would` ＝虚拟/委婉（E-079 的原错），事实陈述里不能用<br>★ 你这次自发用 will 没用 would ⇒ **E-079 顺带判 ✅**|**K**（判据）|`

</details>

## #0199 影响了全世界
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F09

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：**affects** the whole world
正确：**has affected** the whole world（中文"影响**了**"是完成；一般现在时说"现在影响着"也成立，她的不算错）

**中文触发点**
影响了全世界（时态）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-235）</summary>

`影响了全世界（时态）|**affects** the whole world|**has affected** the whole world（中文"影响**了**"是完成；一般现在时说"现在影响着"也成立，她的不算错）|待排序|U（待定）|`

</details>

---

## #0324 真实条件句：从句用现在时，**主句必须带 will**
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F09

**问题是什么**
说的是**将来可能发生**的事（第一类条件句）：
```
✅ `**If** it **rains** tomorrow, the match **will** be postponed.`
✅ `**Even if** it **rains** next week, the match **will** still go ahead.`
✅ `**Unless** the policy **changes**, costs **will** keep rising.`
⛔ `~~If it rains tomorrow, the match is postponed.~~`   主句缺 will
⛔ `~~If it will rain tomorrow, …~~`                      从句多了 will
```
**一句话记：will 只出现在主句，从句用现在时顶替将来。**
适用的从句引导词（都一样）：`if · even if · unless · as long as · provided that ·
when · before · after · until · once · as soon as`
```
✅ `**When** you **finish**, I **will** call you.`　✅ `**Once** they **arrive**, we **will** start.`
```
**什么时候主句可以不带 will**（别拿这个当借口）：
```
零类条件句 ＝ 讲恒常规律，两边都用现在时
  `If you **heat** water to 100°C, it **boils**.` · `If it **rains**, the match **goes** ahead.`（＝这是队里的规矩）
判据：句子里有没有**具体的时间点**。有「明天／下周」这种 ⇒ 说的是一次具体的事 ⇒ 主句必须 will。
```
**找法**
写完 if／even if／unless 从句，**回头看主句的谓语** —— 它讲的是将来吗？是就把 will 补上。

**怎么发现的**
2026-08-22　D4 复习日 C2·组2 第 4 题（顺带）。主考点是 #0261。

**我错在哪**
她的：`even if it rains **next week**, the match still **goes** as planned`
正确：`even if it rains next week, the match **will** still **go ahead** as planned`
题面里写着「**下周**」⇒ 说的是一次具体的将来事件，不是队规 ⇒ 主句必须带 will。
★ 同一句里从句 `rains` 是对的 —— **她知道从句不加 will，缺的是主句要加**。

**中文触发点**
如果下个月油价再涨，这条线路就得停运。

### 历史记录
- 2026-08-22 ❌ 建号　D4 复习日 C2·组2 第 4 题（顺带）
  查重（§3.5 B0）：grep 了 `will` `条件句` `主句`，全档命中两条，逐条比对：
  · #0123（doctors **would** provide → **will** provide）：改正动作是**去掉虚拟语气**
    （would→will），本条是**把一般现在时补成 will**，问 1 不成立
  · #0198（「这个 will 要不要」）：那条的判词是"两个都对，看你在说什么"
    （陈述职责用现在时／具体情境用 will），是**语义选择**；本条是条件句里的**硬性配对**，
    没有选择余地，问 2 不成立
  又查了 F09 的 #0192 #0194 #0252：#0192 管现在完成时、#0194 管时段配时态、
  #0252 管瞬间动词配不了时段，都不是条件句 ⇒ 新建。
  ★ 反向证据（说明这是真缺口不是手滑）：08-19 组2 第 4 题她写
  　`Even though the price has dropped, **sales don't go up**` —— 主句时态同样掉线。
  　两次都是**从句写对、主句掉**，同一个形状 ⇒ 建条目成立。
  ⚠️ 不适用 SKILL §2 排除项⑤：她没有"低压写对过两次"的记录，两次记录都是错的。

---

# F10 语义缺失(中文丢一层)

> 语法全对但中文明写的一层没送到

## #0126 中文里明写的修饰层，写英文时丢掉
状态：在池 ｜ 连对 0 ｜ 连错 5 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F10

**问题是什么**
**这是全库出现次数最多的一条，累计 8 次以上。**
她的句子语法完全正确、读起来也通顺，问题是**中文里明写的某一层意思没进英文**。
丢掉的都是修饰层：程度（更/进一步）、范围（全/只有）、时间（周末）、性质（正规）、
情态（本可以）、使役（A 让 B 不得不）。
机制：cold 产出时认知带宽只够搭骨架，修饰层最先被压掉 —— 不是不会，是压力下丢。

**怎么发现的**
2026-08-16　复习日 C1·组6

**我错在哪**
累计实例（每一条都是同一个机制）：
· already/further　`put a strain on scarce resources` → `put **further** strain on **already** scarce resources`
· 进一步　　　　　`has worsened the situation` → `has **further** worsened…`（题面写了"进一步"就要加）
· 周末　　　　　　`to work overtime` → `to work overtime **at weekends**`
· 更（难）　　　　`he struggles to find a job` → `it is **even harder** to find a job`
· 全（世界）　　　`affects the world` → `the **whole** world ／ people **all over** the world`
· 更（有经验）　　`tend to be experienced` → `tend to be **more** experienced`
· 本可以　　　　　`is the time taken away from` → `**could have been used** on`（could have + 过去分词）
· 使役层　　　　　`the government has no choice but to…` → `**This policy leaves** the government with no choice but to…`
**找法**：翻译前先在中文里把修饰词圈出来，翻完逐个回查有没有落地。

**中文触发点**
- 2026-08-20　这家医院必须保证每位夜班护士一段完整的休息
- 2026-08-19　这类培训只对已经入职一段时间的员工才真正有用。
- （更早）让**本来就**紧张的资源**更加**紧张（08-16 题面加死补主语：**老龄化让本来就紧张的医疗资源更加紧张** —— 原为光杆片段；避开 E-117 的"疫情"以免两条撞车）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组6
- 2026-08-18 ❌ D1 学习日 C2·组8　（当日 3 条，按最后一次记）
  ⚠️ 已并入 #0139 #0142 #0145 #0152 #0154 #0200 #0202 的历史
- 2026-08-19 ❌ D2 学习日 C2　（当日 4 条，按最后一次记 —— 组1 第 1、5、10 题，组3 第 1 题）
  第 1 题「这类培训**只**对已经入职一段时间的员工**才**真正有用」
  她写 `this kind of training is truly useful for employers who…`
  ——「真正」truly ✅ 落地、「已经」用完成时试过 ✅，**丢的是「只…才」这一层范围限定**。
  正确：`is **only** really useful for employees who…`
  第 5 题「大多数小企业都撑不过**头**三年」
  她写 `cannot live for 3 years` ——「头」（first）丢了。正确：`do not survive their **first** three years`。
  第 10 题「这类投诉每年**只**有几起」
  她写 `there are a few of that kind of complaints` ——「只」丢了，`a few` 是"有几个"（肯定），
  中文强调的是少。正确：`there are **only** a few complaints of this kind each year`。
  ★★ 三次丢的都是**范围限定词**（only / first / only），全是中文里明写出来的字。
  同一组里 Q8「明显」significantly ✅ 落地、Q1「真正」truly ✅ 落地
  ⇒ 8 次以来第一次能把"丢一层"收窄：**丢的是"限定范围"那一类**（only / just / first / at least），
  形容词副词类（程度、方式）反而站得住。
  **组3 第 1 题**「这项政策去年出台，**彻底**改变了这个行业的招聘方式」
  她写 `changing how the industry hires` ——「彻底」丢了。
  正确：`**completely** changing…` ／ `**transforming** how the industry hires`（一个词把"彻底"含进去）。
  ⇒ 这一处不是范围限定词，是**程度词**，但删掉后"改变的程度"变了 ⇒ 按下面的边界判据，算丢。
  ★ **边界（2026-08-19 组 2 第 1 题补定）**：删掉那一层**意思会变**才算丢。
  同日组 2 她把「三座**新**工厂」写成 `three factories`，但 `build a factory` 本身已含新建义，
  两句传达的事实相同 ⇒ **冗余修饰不算丢**，不记本条。
- 2026-08-20 ❌ D3 学习日 C2·组1 第 1 题（顺带）　★靶子1
  题面「一段**完整的**休息」，她写 `a rest period` —— 「完整」这一层没进英文。
  按 08-19 定死的判据（**删掉后会改变事实的那一层才必须落地**）：
  `a rest period` 五分钟也算，`a **proper / full / uninterrupted** rest period` 才是题面要求的东西
  ⇒ 事实被改弱了 ⇒ 记 ❌。连错 3。
  ★ 但今天这一条只犯了 **1 次**（08-19 是 4 次）。同组另外五处修饰层全部落地，都是主动送到的：
  　第 3 题「现在」→ 用 `is … than it was` 的时态对比承载（不必再加 now）
  　第 5 题「只」→ `only survived`　　第 8 题「强烈」→ `strongly`
  　第 6 题「已经」→ `has been … for`　第 10 题「想参加培训的」→ `who want to join the training`
  　第 9 题「还是」→ `Even though` 已经把转折扛住，按判据不记
  ⇒ 判据收窄之后，这条第一次出现「只漏最不显眼的那一层」而不是成片漏。
  ★ **同日第 2 次**（组2 第 7 题）：题面「这个项目拖了**不止**半年」，她写 `for half a year`，
  　「不止」整块丢掉。按判据：删掉之后"半年"从下限变成确数 ⇒ **事实变了** ⇒ 记。
  　 按 §3.2 同日只按最后一次记，本行合并为一次 ❌（当日 2 处：组1 第 1 题丢「完整」、组2 第 7 题丢「不止」）。
  ★ 两处是同一个形状：**丢掉的都是"下限／程度"那一层**（完整、不止）。
  　 两次都不是实词，都是修饰词，都在句子里最轻的位置 —— 与本条正文的机制描述完全吻合。
  ★ **同日第 3～5 处**（组3）：
  　 第 7 题「废**水**」→ 她写 `waste`（废弃物），少了"水"这一层，排放的东西变了 ⇒ 记
  　 第 7 题「**每年**排放的」→ 整块没写，年排放量变成了累计总量 ⇒ 记
  　 第 8 题「**将近**八成」→ `by 80%`，下限变确数 ⇒ 记（T1 里这一层直接进数据错）
  　 按 §3.2 同日只按最后一次记，本行合并为一次 ❌（当日共 5 处）。
  ★ **五处的形状高度一致**：完整／不止／水／每年／将近 —— 全是**限定与程度**那一层，
  　 全都删掉后句子照样通顺，全都在她认知带宽的最外圈。
  ★ 但也要看另一面：今天同样有 8 处修饰层是**她主动送到的**
  　（只/强烈/已经/仍/更/早点/现在/想参加培训的）⇒ 不是全丢，是丢最轻的那几个。
  ★★ **同日第 6～7 处（组4），一正一反，是全天最有信息量的一对对照**：
  　 第 1 题（本条的正题）**✅ 四层全落地**：题面「这项**临时**措施**只**在**工作日的**早高峰才执行」，
  　　她写 `the **temporary** measure is **only** enforced during the **morning** rush hour **on workdays**`
  　　—— 临时／只／早／工作日，一层不落。这是本条自 08-16 建号以来**第一次全中**。
  　 第 5 题（顺带）**❌**：题面「运输成本占了产品售价的**三分之一**」，
  　　她写 `accounts for **the total price**` —— 「三分之一」整块没了，
  　　句子从"占三分之一"变成"占了全部"，**事实彻底反了**，是全天最严重的一处丢层。
  ★ 对照读出来的东西：**修饰层被做成考点时她全接住，修饰层只是句子里一个零件时她照丢。**
  　 第 1 题四个修饰词明晃晃排在那儿，她知道我在测什么；第 5 题「三分之一」混在数量表达里就没了。
  　 ⇒ 真实缺口不是"看不见修饰词"，是**没有一个固定的自检动作**逐层核对中文。
  　 ⇒ 装备候选（下次作文用）：写完一句，回中文逐个词点过去，指到哪个词就在英文里找它落在哪。
  ★ **同日第 8 处（组6 第 1 题）**：题面「干净**饮用**水」，她写 `clean water` ——
  　「饮用」没进英文。clean water（洗用的也算）与 clean **drinking** water（能喝的）不是一个东西，
  　 主张的权利范围变了 ⇒ 记。与组3 第 7 题「废**水**」写成 `waste` 是**同一个形状**：
  　 中心名词写了，限定它的那个字丢了。
  ⇒ 按 2026-08-20 她定的新口径（历史逐处全记、streak 当天只推进一次、只要出现过 ❌ 就记 ❌）：
  　 **当日共 8 处 —— 1 处全中（组4 Q1 四层）、7 处丢层，净结果记一次 ❌，连错 3。**
  　（原写法"按最后一次记"已按她 08-20 的裁定作废，本行改为逐处全记。）
- 2026-08-20 ✅ 作文 T2-17　★★ **靶子1 第一次在限时作文里清零**
  ⚠️ 按同日 streak 口径（当天出现过 ❌ 就记 ❌），**本条今天的 streak 结果仍是 ❌**（复习组 7 处丢层）。
  　 **清零与 streak 是两回事**：清零看的是这一篇作文，streak 看的是这一天全部判定。
  作文里逐条对着她的中文构思核，**14 层修饰全部落地，一层未丢**：
  　额外的→extra ／ 实际→actual ／ 有时→sometimes ／ 高得多→far higher ／ 往往→usually
  　任何优势→no real advantage ／ 只有…才→only ／ 毫无关系→completely irrelevant
  　正是→exactly ／ 既定的→set ／ 同样真实→so is ／ 一切…可能→any chance
  　确实→genuinely ／ 前提是→provided that
  ★ 装备「每写完一句问一次是不是把话说满了」**第一次上场就一次到位**，证据就是这 14 层。
  ⇒ 按 §7 **靶子1 清零，下一篇换靶子**。本条留在池里照常复习。
- 2026-08-22 ❌ D4 复习日 C2·组1 第 7 题（顺带）　**本条已于 2026-08-22 改判，见下方更正块**
  题面「这项政策的**社会**影响很难用数字衡量」，她写 `the **effect** of the policy`。
  「社会」这一层没进英文。按 08-19 定死的判据（**删掉后事实会变才算丢**）：
  `the effect of the policy` 可以是财政影响、环境影响、任何影响，范围被放宽 ⇒ 事实变了 ⇒ 记。
  正确：`the **social impact** of this policy`。
- 2026-08-22 ❌ D4 复习日 C2·组1 第 2 题（顺带）　**本条已于 2026-08-22 改判，见下方更正块**
  题面「**这个城市**六十岁以上的人口数量在过去十年翻了一番」，她写 `**the** population aged 60 and over`。
  「这个城市」整块没进英文，读者无从知道是哪一个人口 ⇒ 范围限定层丢失 ⇒ 记。
  正确：`**the city's** population aged 60 and over`。

- 2026-08-22 ✅ D4 复习日 C2·组1（第 2 题＋第 7 题）　**她当场推翻教练的两个 ❌，原话：「126 算对」**

  ### ★ 更正块（§4.7）

  **原判**：两处都判 ❌（丢「社会」、丢「这个城市」），当日净结果记一次 ❌，连错 3 → 4。
  **新判**：两处**都不是丢层** ⇒ 本条今天记 **✅**，连对 0 → 1、连错 3 → **0**。
  **改判理由**（她对，教练判宽了）：
  ```
  08-19 定下的判据是「删掉那一层，意思会变才算丢」。教练今天把它套到了
  【名词前的语境限定语】上，套错了 —— 这两处删掉之后，命题本身没有变：
    · 「这项政策的社会影响很难用数字衡量」→ the effect of the policy is difficult to quantify
      主张仍然是「这项政策的影响很难量化」。social 只是把影响的类型说细，不改变主张。
    · 「这个城市六十岁以上的人口翻了一番」→ the population aged 60 and over has doubled
      主张仍然是「60+ 人口翻番」。哪个城市是【上下文承担】的信息，
      在真实作文里前文已经交代过，单句中译英里它本来就悬空。
  ⇒ 与 08-19 那三处（only / first / only）不是一回事：那三处删掉之后
     「只对 X 有用」变成「对 X 有用」、「头三年」变成「三年」，**命题被改写了**。
  ```
  ★★ **判据从今天起收紧（她 2026-08-22 定）**：
  ```
  ✅ 判丢层：删掉后【命题被改写】的那一层
     范围副词 only / just / first ｜ 程度下限 不止 / 将近 ｜ 数量 三分之一
     性质区分 饮用水 vs 水 / 废水 vs 废弃物 ｜ 情态 本可以 ｜ 使役 A 让 B 不得不
  ⛔ 不判丢层：名词前的【语境限定语】—— 这个城市的 / 这项政策的 / 社会的 / 他的
     这类信息在真实作文里由上下文承担，单句中译英逼不出来，判它等于罚她没写废话
  ```
  ⇒ 这条收紧同时解释了本条为什么一直毕不了业：**分母里混进了不该算的**。

- 2026-08-22 ✅ D4 复习日 C2·组3 第 1 题（主考点）
  题面「老龄化让本来就紧张的医疗资源更加紧张」，她写
  `an aging population imposes **a further** strain on **already** scarce medical resources`。
  「本来就」already ✅、「更加」further ✅，两层都落地。
  ⚠️ **证据分量要打折**：这句是本条 08-16 就教过、并**逐字写死在触发点里**的原句，
  　 教练今天原样拿出来用（§6 违规）⇒ 这是**复现**，不是新语境下的产出。
  　 同组真正有分量的是 Q7「**将近**三成」→ `almost a third`，那是新语境、她自己送到的。
  📋 顺带用对 #0103：`imposes **a further strain** on` —— 冠词＋形容词＋单数 strain 三样齐全。

- 2026-08-22 ❌ D4 复习日 C2·组3 第 2 题（顺带）
  题面「这项技术的**成本**在过去十年里几乎没变」，她写
  `**the technology** has remained stagnant over the past decade`。
  「成本」这个**中心词整块没进英文** —— 句子从「成本没变」变成「技术停滞」，**两个不同的主张**。
  按 2026-08-22 收紧后的判据：这一处落在「✅ 判」那一侧（命题被改写），与组 1 那两处
  （名词前的语境限定语）**不是一回事**，她的裁定不适用于此。
  正确：`The **cost of** this technology has barely changed over the past decade.`
  ⚠️ 同一处也让 #0280 的考点整块落空 ⇒ 那条记 ❌。

  ### ★ 当天 streak 结算（§3.2 同日口径）
  ```
  组1 第 2/7 题  ❌ → 她当场改判为 ✅
  组3 第 1 题    ✅
  组3 第 2 题    ❌   ← 命题被改写，收紧后的判据照判
  ⇒ 当天出现过 ❌ ⇒ **当天净结果记 ❌**，连对 1 → 0、连错 3 → 4
  ```
  ⚠️ 这不是推翻她 08-22 的裁定 —— 她裁的是"名词前的语境限定语不算丢层"，那条**继续有效**；
  　 今天 Q2 丢的是中心词，两者落在收紧判据的两侧。若她认为 Q2 也该算对，本行按 §4.7 再改判。
  ⚠️ 复习日无作文 ⇒ 本条今天不涉及靶子清零（§7 清零只认限时 cold 作文）。

- 2026-08-22 ❌ D4 复习日 C2·组8 第 5 题（顺带）
  题面「这项技术已经成熟。成本**还是**下不来。」，她写 `we **failed to** drive the cost down`。
  「还是」这一层没落地，而且主语从"成本"换成了"我们"、体从**持续**变成**完成**
  ⇒ 句子从"成本仍然降不下来"变成"我们（过去）没能把成本降下来"，**命题被改写** ⇒ 判丢层。
  正确：`the cost **still** cannot be brought down` ／ `costs **remain** stubbornly high`。
- 2026-08-22 ❌ D4 复习日 C2·组8 第 10 题（顺带）
  题面「这类项目**几乎**总是超预算」，她写 `projects of this nature **invariably** exceed their budget`。
  invariably ＝ **无一例外**；「几乎」删掉之后主张从"允许例外"变成"绝对" ⇒ 命题被改写 ⇒ 判丢层。
  正确：`**almost invariably**`。
  ⇒ 按 §3.2 同日口径，本条今天的净结果已由组 3 的 ❌ 定下，**这两行只留证据，不再推进**。
  ★★ **今天四处丢层，收紧判据之后剩下的形状高度一致**：
  ```
  组3 Q2  丢中心词「成本」        ← 命题整个换了
  组8 Q5  丢「还是」＋换主语        ← 持续 → 完成
  组8 Q10 丢「几乎」               ← 允许例外 → 绝对
  （组1 那两处"社会／这个城市"已按她 08-22 的裁定不判）
  ```
  ⇒ **真正的缺口是中文里那个"留余地/定范围"的字**：只／头／不止／将近／还是／几乎。
  　 这与 08-19 那三处（only / first / only）完全同族，判据收紧之后**噪音被滤掉，形状反而清楚了**。
  ⇒ 下一篇作文的装备候选：**写完一句，回中文找那个"留余地"的字，问它落在英文哪个词上。**
- 2026-08-22 ❌ D4 复习日 C2·组10 第 10 题（顺带）
  题面「这类投入的回报**往往**要等好几年才看得见」，她写 `yield returns **only after** several years`。
  「往往」没落地 ⇒ 主张从"通常要等好几年"变成"一律要等好几年" ⇒ 命题被改写 ⇒ 判丢层。
  正确：`**often** yield returns only after several years`。
  ⇒ 今天第五处，仍然是同一个形状：**中文里那个"留余地"的字**（只／头／不止／将近／还是／几乎／往往）。
  ⚠️ streak 不再推进（当天净结果已由组 3 定下）。
- 2026-08-23 ❌ D1 学习日 C3·组1 第 2 题（顺带）　**装备第一次上称就漏了一处**
  题面「这套流程走完要一个星期，**光是**材料费，她就花了将近两千块」（主考点是 #0266）。
  她写 `she spent nearly two thousand yuan **on materials**`。
  「**光是**」没落地 ⇒ 命题从"材料一项就两千（总额还更多）"变成"她在材料上花了两千" ⇒
  按 08-22 收紧后的判据「删掉后**命题被改写**才判」⇒ 判丢层，连错 5。
  正确：`on materials **alone**` ／ `**just** on materials`。
  ★★ **「光是」正是今天装备点名的那一族**：只／头／不止／将近／还是／几乎／往往／光是。
  　 装备是「写完一句，回中文找那个留余地的字，问它落在英文哪个词上」——
  　 这句里有**两个**这样的字：「光是」和「将近」。
  ```
  将近两千块  →  nearly two thousand   ✅ 送到了
  光是材料费  →  on materials          ❌ 丢了
  ```
  ⇒ 不是"不认识 alone"，是**一句里有两个留余地的字时，她只逮住了一个**。
  　 装备要改成**数数**：先数中文这句里有几个这样的字，再逐个对英文点名。
  📋 更好：`…, and she spent nearly 2,000 yuan **on materials alone**.`
- 2026-08-23 ❌ D1 学习日 C3·组2 第 9 题（顺带）　**只留证据，不推进 streak（同日口径）**
  题面「人工智能会不会取代大量岗位，引发了**相当大的**争论」（主考点是 #0303）。
  她写 `… is a subject of debate` —— 「**相当大的**」（considerable）这一层没落地。
  ⇒ 与本条今天组1 的「光是」是同一个机制：**中文里那个限定程度的字丢在半路**。
  ⚠️ 按 §3.2 当天只推进一次，本条今天的净结果已由组1 定下 ⇒
  　 **连对 0／连错 5 维持不变**，本行只留证据。
  ★ 今天两处丢层的对照，形状完全一致：
  ```
  组1 第 2 题   光是材料费   →  on materials          （丢 alone）
  组2 第 9 题   相当大的争论 →  is a subject of debate （丢 considerable，连"引发了"一起丢）
  ⇒ 两处都是**句子的骨架送到了、修饰那一层掉了**，与装备要抓的完全同一件事。
  ```
- 2026-08-23 ✅ D1 学习日 C3·组4 第 10 题（**主考点**）　**本条建号以来第一次作为主考点被测就命中**
  题面「这项收费只在旺季执行，而且仅限市中心的几条主干道。（★ 用 only；★ 用 a few）」，她写
  `this fee applies only during the peak season and is limited to a few main roads in the city center`。
  ```
  只在旺季      →  only during the peak season   ✅
  仅限          →  is limited to                 ✅
  几条（不是全部）→  a few main roads             ✅
  ```
  **一句里三个"留余地/定范围"的字，三个全部落地** —— 与今天组1 那次（两个字只逮住一个）
  正好构成对照。⇒ 连对 1、连错 5 → 0。
  ⚠️ **证据分量打折**：题面点名给了 `only` 和 `a few` 两个英文词（连对 0 ⇒ §6 要求给）。
  　 所以这次证明的是"**给了词她放得进正确位置**"，不是"**没人提醒她自己会数**"。
  　 后者只能靠装备在作文里验（装备＝写完一句先数中文里有几个这样的字，再逐个对英文点名）。
  📋 顺带用对 #0269：`**is limited to**`（"限制在…范围内"，#0269 的第三条路，🎓 不推进）。
  📋 更好：`This charge applies only in the peak season, and only to a few main roads in the city centre.`
  　（`in the peak season` 是季节的默认介词；后半用第二个 only 与前半平行，比换成 be limited to 更紧）
  ⚠️⚠️ **streak 不推进（§3.2 同日口径）**：本条今天已经在组1 第 2 题（丢「光是」）记过 ❌
  　⇒ **当天只要出现过 ❌ 就记 ❌** ⇒ 今天净结果仍是 ❌，**连对 0 ／ 连错 5 维持不变**。
  ⇒ 本行是本条**建号以来第一次作为主考点被测**的证据，留着；streak 等下一个练习日再算。
  ★ 教练侧留一句：如果按"最后一次"记，本条今天就该记 ✅ —— 那正是 §3.2 明令禁止的口径
  　（结果会被出题顺序左右）。今天组1 在前、组4 在后，纯属我排组的先后，不该改变结论。
<details><summary>原始行（旧表逐字，旧号 E-087）</summary>

`让**本来就**紧张的资源**更加**紧张（08-16 题面加死补主语：**老龄化让本来就紧张的医疗资源更加紧张** —— 原为光杆片段；避开 E-117 的"疫情"以免两条撞车）|put a strain on scarce resources|put **further** strain on **already** scarce resources|P12（中文一个词两层，英文要两个词分别接；08-15 新语境「情况**进一步**恶化」丢 further，同模式第 3 次）|R · **P12**|0/3|`

</details>

> 🗑 **#0330 已撤销 —— 编号作废，不复用、不占条目数。**
> 2026-08-23 建号当天，她当场撤销：「**(#0330) 不用建，忽略。**」
> 原拟内容：中文没写的那一层，英文里不要加上去（`有一半` 写成 `more than half`）——
> 　 定位为 #0126 的镜像（#0126 管"少送一层"，它管"多送一层"）。
> ⇒ 连带回退：第 1 题 `more than half` **不再判为错**，本组一字未改率由 60.0% 重算为 **80.0%**，
> 　 #0095 那行历史里的相关注记已改写。F10 族名维持「语义缺失(中文丢一层)」不改。
> ⇒ 教练侧留痕（为什么原判站不住）：中文「有一半」到英文的刻度偏移，
> 　 在**翻译练习**里是偏移，但她要的是**作文里的可执行动作**；
> 　 而 #0126 的装备（「回中文找那个留余地的字」）已经覆盖了同一个动作的另一半，
> 　 再建一条只是把同一个检查动作拆成两个编号 ⇒ 她的判断成立。

<details><summary>原拟正文（撤销前逐字，留档不用）</summary>

翻译／作文里，英文送出去的信息量必须**和中文一样，不多不少**。#0126 管"少了"，本条管"多了"。
最常出事的是**程度词与范围词**——中文写的是一个刻度，英文写成了另一个：

```
中文        只能是                    ⛔ 不能写成
有一半      half                      more than half（＝过半，51%+）
将近三成    nearly / almost 30%       over 30% ／ about a third（后者把 28% 也放进来了）
好几年      several years             many years ／ years and years
不少        quite a few / a good many  most（"不少"没说过半）
大多数      most                      almost all
基本上没有  hardly any                none（"基本上没有"留了余地）
```
**判据（一句话）**：英文那个词**框住的范围**，和中文那个词框住的**是不是同一块**？
不是 ⇒ 命题被改写 ⇒ 判本条。
★ T1 里这一条最贵：**它直接算数据错**，走 §5 第 4 步、进 TA 清单、触发硬顶行。
★ 与 #0126 合起来是一个动作：**写完一句，把中文那句的"量"和英文那句的"量"并排读一遍——
　 少送一层是 #0126，多送一层是本条。**

**怎么发现的**
2026-08-23　D1 学习日 C3·组1 第 1 题（顺带）。主考点 #0095 命中，语义层多送了一格。

**我错在哪**
她的：`parents … account for **more than half** of the patients`
正确：`parents … account for **half** of the patients`（中文是「有一半」，不是「一半多」）
找法：**中文里的数量词，逐个抄到草稿边上，写完英文回来一个个对刻度。**

**中文触发点**
这家超市的顾客里有一半是附近的居民，将近三成是学生。
（★ 两个数量词各只能对应一个英文刻度，多一格少一格都不行）

### 历史记录
- 2026-08-23 ❌ D1 学习日 C3·组1 第 1 题（顺带）　建号
  查重（§3.5 B0）：grep 了 `无中生有` `多加一层` `加了一层` `中文没有的`，全档零命中；
  又逐条比对了语义层现有的两条：
  · **#0126**（中文里明写的修饰层丢掉）—— 三问：
    问1 改正动作？#0126 是**补上**中文有的那层，本条是**删掉**中文没有的那层 ⇒ **否**
    问2 一句话规则？「英文的信息量要和中文一样」能同时覆盖两者 ⇒ 是
    问3 掌握一个另一个跟着对？⇒ **否**（两个方向独立）
    ⇒ 三问不全是"是" ⇒ 不是同一条。
    反向验（§3.5 1.3）：**同一组里就有现成的一对** ——
      第 2 题她**丢了**「光是」（#0126 ❌），第 1 题她**加了** more than（本条 ❌）。
      一丢一加同时发生 ⇒ 可独立取值 ⇒ 不合并，确凿。
  · **#0221**（return … again 冗余）—— 那条是"同一个意思说两遍"，句子的信息量没变；
    本条是"信息量被改了" ⇒ 问 1 不成立。
  · **F11 的数据类条目**（#0203–#0221）—— 那些管的是"数字抄错／看错图"，
    本条管的是"数字没抄错、但**刻度词**换了一格" ⇒ 问 1 不成立。
    ⚠️ 但本条在 T1 里的**后果**与数据错相同，正文已写明。
  ⇒ 新建，归 F10（与 #0126 同族，互为镜像）。

</details>

## #0331 时间名词也能带所有格：today's patients / this year's figures
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F10
🔵 §2③ 她点名要学（2026-08-23，原话：「**时间所有格，我不会主动用，可以新建一个条目练习下**」）

**问题是什么**
中文的「今天的病人」「去年的数据」，英文有两条路，**她只用第二条**：
```
✅ 所有格（她缺的这条）     **today's** patients · **this year's** figures · **last month's** report
                          **yesterday's** meeting · **next week's** deadline · **the 1990s'** boom
⚠️ of 结构（她默认走的）    the patients **of today** · the figures **of this year**
                          —— 语法对，但**书面里明显更笨**，而且 of 结构还容易把主语拖长
```
**为什么值得练**：所有格把一个 of 短语压成一个撇号，**句子的主语立刻变短** ——
而她的数的一致失守（靶子2）几乎全发生在**主语被 of 短语拖长**的时候。
⇒ 这一条同时在替靶子2 减压。
```
The production **of this factory** has seen no growth.   （主语 6 个词）
**This factory's** output has been flat.                  （主语 3 个词）
```
**哪些名词能带 's**（不只是人）
```
时间   today's / this year's / a day's work / five years' experience（见 reminders R3）
机构   the government's policy · the company's revenue · the university's intake
国家地区 China's economy · the city's population
⛔ 一般的无生命物不带：`~~the table's leg~~` → the leg of the table
```
**判据**：这个名词是**时间、机构、国家、或人**吗？是 ⇒ 可以用 's；不是 ⇒ 走 of。

**怎么发现的**
2026-08-23　D1 学习日 C3·组1 第 1 题的更好版 `Half of **today's** patients at the clinic…`。
她看到后当场点名要学（§2③）。

**我错在哪**
她这次**没有错**（她写的是 `at the clinic today`，完全成立）。
建号理由是 §2③ ——**她主动说"我不会主动用"**。缺口是这条路根本没在她的产出里出现过。
找法：**写完 `the X of 时间/机构/国家`，回头问一句"能不能改成 撇号 s"。**

**中文触发点**
今天的病人比昨天少了将近一半，而这个月的总量还是高于去年同期。
（★ 三处时间限定都必须用**所有格**，不许用 of 结构：今天的病人 · 这个月的总量 · 去年同期）

### 历史记录
- 2026-08-23 ③ 建号（她点名要学）D1 学习日 C3·组1 第 1 题的更好版
  查重（§3.5 B0）：grep 了 `所有格` `撇号` `'s` `years'`，全档命中两处 ——
  · **reminders.md R3**（`five **years'** experience` 的撇号）：那是"块里那个小零件掉了"，
    她**知道这个块**、只是压力下掉零件 ⇒ 与本条正相反（本条是**这条路她从来没走过**）
    ⇒ 问 1、问 3 都不成立。⚠️ 两者要一起看：R3 管"写了但掉撇号"，本条管"根本没想到用"。
  · **#0025 / #0270**（the retirement age / the minimum wage 必须带 the）：那是冠词，不是所有格
    ⇒ 问 1 不成立。
  反向验（§3.5 1.3）：举得出"一个对一个错"——08-22 她 `5 years working experience` 掉了撇号（R3），
    而她从来没写过 `today's` 这类（本条）⇒ 可独立取值 ⇒ 不合并。
  ⇒ 新建。建号时无对错，连对连错都是 0。

---

# F11 T1 数据/图表

> 数据抄写、峰值占比、跨线对比、overview 特征选择、倍数

## #0205 这一时期结束时只剩 19% 的人住在曼哈顿
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F11

**问题是什么**
P12 主谓搭配　R · P12

**怎么发现的**
2026-08-16　复习日 C1

**我错在哪**
她的：the absolute value **finished the period with only 19% of people**
正确：**the period ended with** only 19% of people…（★ 数字类主语不能带人当宾语）

**中文触发点**
这一时期结束时只剩 19% 的人住在曼哈顿（08-16 中译英题面：这一时期结束时，只剩五分之一的人住在那里 —— 无图语境，五分之一是内容本身，不违反 E-182「T1 题面禁约数」）

### 历史记录
- 2026-08-16 ✅ 复习日 C1

<details><summary>原始行（旧表逐字，旧号 E-162）</summary>

`这一时期结束时只剩 19% 的人住在曼哈顿（08-16 中译英题面：这一时期结束时，只剩五分之一的人住在那里 —— 无图语境，五分之一是内容本身，不违反 E-182「T1 题面禁约数」）|the absolute value **finished the period with only 19% of people**|**the period ended with** only 19% of people…（★ 数字类主语不能带人当宾语）|P12 主谓搭配|R · **P12**|`

</details>

## #0206 上升趋势达到 647 万的峰值
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F11

**问题是什么**
P12 主谓搭配　R · P12

**怎么发现的**
2026-08-16　复习日 C1·组7

**我错在哪**
她的：the upward trend **marked the peak of**
正确：the upward trend continued and **reached a peak of**（★ 趋势不能 mark a peak）

**中文触发点**
上升趋势达到 647 万的峰值

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组7

<details><summary>原始行（旧表逐字，旧号 E-165）</summary>

`上升趋势达到 647 万的峰值|the upward trend **marked the peak of**|the upward trend continued and **reached a peak of**（★ 趋势不能 mark a peak）|P12 主谓搭配|R · **P12**|`

</details>

## #0207 75% → 76%
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F11

**问题是什么**
W9 数据错（T1 最致命）　R · W9

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`75%`
正确：`76%`

**中文触发点**
⛔ **挂作文验（T1），不出单点题**（2026-08-24 定）—— 考点是"数据抄错"（75% 写成 76%），
错不错只能**回图核**才知道，中译英题面里没有图 ⇒ 判分第 4 步的数据核对表管这一条。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-166）</summary>

`占总数的 76%|`75%`|`76%`|**W9 数据错**（T1 最致命）|R · **W9**|`

</details>

## #0208 peaked at … by 1900 → peaked at … in 1900
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F11

**问题是什么**
P1 介词　R · P1

**怎么发现的**
2026-08-16　复习日 C1·组9

**我错在哪**
她的：peaked at … **by** 1900
正确：peaked at … **in** 1900

**中文触发点**
这个数字在 1900 年达到峰值

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组9

<details><summary>原始行（旧表逐字，旧号 E-169）</summary>

`这个数字在 1900 年达到峰值|peaked at … **by** 1900|peaked at … **in** 1900|P1 介词|R · **P1**|`

</details>

## #0210 proportation → proportion
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F11

**问题是什么**
P5 拼写　R · P5

**怎么发现的**
2026-08-16　复习日 C1·组11

**我错在哪**
她的：`proportation`
正确：`proportion`

**中文触发点**
比例（08-16 题面加死：**这个比例只有五分之一**）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组11（当日 3 次，取最后一次）

<details><summary>原始行（旧表逐字，旧号 E-172）</summary>

`比例（08-16 题面加死：**这个比例只有五分之一**）|`proportation`|`proportion`|P5 拼写|R · **P5**|`

</details>

## #0211 from 1900 and 2000 → from 1900 to 2000 ／ between 1900 and 2000
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F11

**问题是什么**
P1 搭配　R · P1

**怎么发现的**
2026-08-16　复习日 C1·组8

**我错在哪**
她的：from 1900 **and** 2000
正确：from 1900 **to** 2000 ／ **between** 1900 **and** 2000

**中文触发点**
从 1900 年到 2000 年（08-16 题面加死：**从 1900 年到 2000 年，人口持续增长** —— 刻意**不用"翻了四倍"**：汉语倍数表达 ×4/×5 歧义，全库倍数类清完之前不出，见 E-178）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组8

<details><summary>原始行（旧表逐字，旧号 E-173）</summary>

`从 1900 年到 2000 年（08-16 题面加死：**从 1900 年到 2000 年，人口持续增长** —— 刻意**不用"翻了四倍"**：汉语倍数表达 ×4/×5 歧义，全库倍数类清完之前不出，见 E-178）|from 1900 **and** 2000|from 1900 **to** 2000 ／ **between** 1900 **and** 2000|P1 搭配|R · **P1**|`

</details>

## #0212 「by 和 in 啥区别，我感觉 T1 基本可以互换」
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F11

**问题是什么**
K

**怎么发现的**
2026-08-16　复习日 C1

**我错在哪**
她的：这个数字在 1900 年达到峰值 ／ 到 1900 年为止已增长到 158 万（08-16 题面：到 1900 年为止，这个数字已经增长到 158 万）
正确：**不能互换**。**in ＝ 动作发生在那一年**（peaked at X **in** 1900）；**by ＝ 结果累积到那一年为止**（**By** 1900, the figure **had** reached X，常配完成时）。★ 她作文 S9 的 `to 1,587,109 **by** 1900` 是**对的**（增长是累积过程）

**中文触发点**
这个数字在 1900 年达到峰值；而到 1950 年为止，它已经翻了一番。（★ 两处时间分别用 in 和 by，注意各自配的时态）
（旧留痕：「by 和 in 啥区别，我感觉 T1 基本可以互换」—— 不能互换：
　in ＝动作发生在那一年；by ＝结果累积到那一年为止，常配完成时）

### 历史记录
- 2026-08-16 ✅ 复习日 C1

<details><summary>原始行（旧表逐字，旧号 E-174）</summary>

`「by 和 in 啥区别，我感觉 T1 基本可以互换」|这个数字在 1900 年达到峰值 ／ 到 1900 年为止已增长到 158 万（08-16 题面：到 1900 年为止，这个数字已经增长到 158 万）|**不能互换**。**in ＝ 动作发生在那一年**（peaked at X **in** 1900）；**by ＝ 结果累积到那一年为止**（**By** 1900, the figure **had** reached X，常配完成时）。★ 她作文 S9 的 `to 1,587,109 **by** 1900` 是**对的**（增长是累积过程）|**K**|`

</details>

## #0213 这个数字随后涨了近百倍，1900 年达到 158 万
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F11

**问题是什么**
第②类 · 数学未定　不出中译英

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：The figure increased sharply, by almost 100 times, to 1,587,109 by 1900（**内容全送到了**：「涨了近百倍」＝increased by ~100 times；sharply 是多给的不是漏的）
正确：~~rose almost a hundredfold~~ ⛔ **08-16 移出中译英池，两个理由**：① **第②类**——她的 floor 判不出 ❌，最多 ⚠️ ② **更糟：目标版与题面在数学上不是同一个数** —— 汉语「涨了近百倍」＝**增量**约 100 倍（末值≈101 倍），`a hundredfold` ＝**末值**≈100 倍，差一个基数，而档案里没有确定源数据支持哪一个。拿它判她错＝判教练自己没算清的账。<br>⇒ 降为 T1 词池里的 ⚠️ 级更好版；要恢复成真错条目，先回图用起止数确认「近百倍」是 by 还是 to<br>🔴 **系统性欠定义**：「翻了四倍」（×4 还是 ×5）同样歧义 ⇒ **倍数表达全库需单独清一遍**，清完之前不出倍数类题

**中文触发点**
这个数字随后涨了近百倍，1900 年达到 158 万

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-178）</summary>

`这个数字随后涨了近百倍，1900 年达到 158 万|The figure increased sharply, by almost 100 times, to 1,587,109 by 1900（**内容全送到了**：「涨了近百倍」＝increased by ~100 times；sharply 是多给的不是漏的）|~~rose almost a hundredfold~~ ⛔ **08-16 移出中译英池，两个理由**：① **第②类**——她的 floor 判不出 ❌，最多 ⚠️ ② **更糟：目标版与题面在数学上不是同一个数** —— 汉语「涨了近百倍」＝**增量**约 100 倍（末值≈101 倍），`a hundredfold` ＝**末值**≈100 倍，差一个基数，而档案里没有确定源数据支持哪一个。拿它判她错＝判教练自己没算清的账。<br>⇒ 降为 T1 词池里的 ⚠️ 级更好版；要恢复成真错条目，先回图用起止数确认「近百倍」是 by 还是 to<br>🔴 **系统性欠定义**：「翻了四倍」（×4 还是 ×5）同样歧义 ⇒ **倍数表达全库需单独清一遍**，清完之前不出倍数类题|第②类 · 数学未定|不出中译英|`

</details>

## #0214 ⛔ 教练 drill 题面出错两处：第 4 题中文写「四分之一的人口住在曼哈顿以外」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F11

**问题是什么**
（旧档案未单列，见下方「我错在哪」与原始行）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：留痕（教练犯规）
正确：

**中文触发点**
⛔ **教练 drill 题面出错两处**：第 4 题中文写「四分之一的人口住在曼哈顿以外」，实际数据是 **81%（五分之四）**——她按事实写 `four fifths` 是对的，记 ◎ 不记错；第 5 题中文用约数「五分之一」会诱导写 20%，而图上是 19%。★ **T1 的题面不许用约数**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-182）</summary>

`⛔ **教练 drill 题面出错两处**：第 4 题中文写「四分之一的人口住在曼哈顿以外」，实际数据是 **81%（五分之四）**——她按事实写 `four fifths` 是对的，记 ◎ 不记错；第 5 题中文用约数「五分之一」会诱导写 20%，而图上是 19%。★ **T1 的题面不许用约数**|留痕（教练犯规）|`

</details>

## #0215 这一时期结束时，只剩五分之一的人住在那里
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F11

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：only one fifth of **people** lived there
正确：only one fifth of **the population** lived there（分数 of 后面接**定指的整体**；of people 泛指在新闻标题里成立，但这里整体是明确的全市人口）

**中文触发点**
这一时期结束时，只剩五分之一的人住在那里

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-199）</summary>

`这一时期结束时，只剩五分之一的人住在那里|only one fifth of **people** lived there|only one fifth of **the population** lived there（分数 of 后面接**定指的整体**；of people 泛指在新闻标题里成立，但这里整体是明确的全市人口）|待排序|U（待定）|`

</details>

## #0216 「可以写 one fifth 么」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F11

**问题是什么**
K（口径）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：这个比例只有五分之一
正确：**能**，`The share is one fifth.` ✅ 与 20% 等价。<br>⛔ 但 T1 里有硬规矩：**图上给什么写什么**——图给 19% 就写 19%，不许自己转成"五分之一"（教练 08-15 出 drill 题时犯过这个错：用约数诱导她写 20%，见 E-182）

**中文触发点**
⛔ **挂作文验（T1），不出单点题**（2026-08-24 定）—— 答案是"能写"，本身没有缺口；
真正要管的是 T1 硬规矩「**图上给什么写什么**」，而那要有图才成立。
（旧留痕：「可以写 one fifth 么」—— 能，`The share is one fifth.` 与 20% 等价；
　但图给 19% 就写 19%，不许自己转成"五分之一"）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-248）</summary>

`「可以写 one fifth 么」|这个比例只有五分之一|**能**，`The share is one fifth.` ✅ 与 20% 等价。<br>⛔ 但 T1 里有硬规矩：**图上给什么写什么**——图给 19% 就写 19%，不许自己转成"五分之一"（教练 08-15 出 drill 题时犯过这个错：用约数诱导她写 20%，见 E-182）|**K**（口径）|`

</details>

## #0217 涨到原来的一百倍
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F11

**问题是什么**
🔴 进池（她点名）　K

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：increased by almost 100 times
正确：★ **她 08-16 点名要学**（「hundredfold 我觉得是可以学，如果确实更好」）：<br>`-fold` ＝ **末值是初值的 N 倍**，不是"增加了 N 倍"：`rose **tenfold**` ＝变成 10 倍 · `a **hundredfold** increase`<br>⛔ **中文「涨了近百倍」本身歧义**（严格＝增加100倍/末值101倍；日常常当"变成100倍"）⇒ 教练无法据此判她错，见 E-178<br>✅ **T1 最安全的三条路**：① `rose **from** 60,000 **to** 1.58 million`（直接给起止数，零歧义，**T1 首选**）② `nearly **doubled** / more than **tripled**`（2、3 倍）③ `rose more than **twentyfold**`（大倍数才用 -fold）

**中文触发点**
涨到原来的一百倍（T1 倍数表达）

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-250）</summary>

`涨到原来的一百倍（T1 倍数表达）|increased by almost 100 times|★ **她 08-16 点名要学**（「hundredfold 我觉得是可以学，如果确实更好」）：<br>`-fold` ＝ **末值是初值的 N 倍**，不是"增加了 N 倍"：`rose **tenfold**` ＝变成 10 倍 · `a **hundredfold** increase`<br>⛔ **中文「涨了近百倍」本身歧义**（严格＝增加100倍/末值101倍；日常常当"变成100倍"）⇒ 教练无法据此判她错，见 E-178<br>✅ **T1 最安全的三条路**：① `rose **from** 60,000 **to** 1.58 million`（直接给起止数，零歧义，**T1 首选**）② `nearly **doubled** / more than **tripled**`（2、3 倍）③ `rose more than **twentyfold**`（大倍数才用 -fold）|🔴 进池（她点名）|**K**|`

</details>

## #0218 这个比例只有五分之一
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F11

**问题是什么**
第②类（测法不适用）　E-172 改挂作文

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：this **share**（第 **2** 次走 share，未产出 proportion）
正确：★★ **08-16 改判：E-172 的拼写考点用中译英测不到** —— 她默认词就是 share（两次悬空实证），根本不产出 proportion。<br>✅ 但她 **08-15 T1 作文里写过 `proportation`** ⇒ **她在 T1 里会用这个词**，只是聊天中译英不走它。<br>⇒ **E-172 改挂作文验**（T1 作文必然出现 proportion），不再出中译英；本条记录改判依据

**中文触发点**
这个比例只有五分之一

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-268）</summary>

`这个比例只有五分之一|this **share**（第 **2** 次走 share，未产出 proportion）|★★ **08-16 改判：E-172 的拼写考点用中译英测不到** —— 她默认词就是 share（两次悬空实证），根本不产出 proportion。<br>✅ 但她 **08-15 T1 作文里写过 `proportation`** ⇒ **她在 T1 里会用这个词**，只是聊天中译英不走它。<br>⇒ **E-172 改挂作文验**（T1 作文必然出现 proportion），不再出中译英；本条记录改判依据|第②类（测法不适用）|E-172 改挂作文|`

</details>

## #0219 ⭐⭐ 「题面点名」策略首次验证成功，且验证得很干净：<br> 组 8「这个比例只有五
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F11

**问题是什么**
（旧档案未单列，见下方「我错在哪」与原始行）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：留痕（方法验证＋资产）
正确：

**中文触发点**
⭐⭐ **「题面点名」策略首次验证成功，且验证得很干净**：<br>　组 8「这个比例只有五分之一」→ 她写 **share**，悬空<br>　组 10 同一题面 → 又写 **share**，第 2 次悬空<br>　组 11 题面点名「用 pro- 开头那个表示比例的正式词，不是 share」→ **proportion，且拼写正确** ✅<br>★★ 关键在于**拼写仍然是她的**：只给了词元描述、没给拼写，她 08-15 T1 作文里写的是 `proportation`，今天对了 ⇒ **点名词元 ≠ 泄漏拼写**，这条方法成立。<br>★ 直接证明她 08-16 的裁决：**「你如果有想要 X，你就在题面直接说，我猜不到的，你说了我自然就写了」** ⇒ 已写进 SKILL §2.3。<br>★ 推论：今天反复出现的"题面逼不出考点"（E-071 词性 · E-073 词元 · E-111 前提 · E-128 同义词 · E-170 块方向）**大半可以用点名解决**，不必再靠改写题面绕。<br>✅+ **她的资产**：`as` 当场调出（两小时前才点名说"老想不到"）· `the public interest`（组 5 写过，今天复用）· `deeply unpopular`（搭配好）· `he or she` 指代唯一 · `months of proper treatment` 全中 · `pension spending` 不可数用对

⛔ **不出单点题（2026-08-24 定）** —— 本条正文是一段**教练侧的方法验证记录**（"题面点名策略首次验证成功"），
按 §2 不该是条目。迁移存量，留档不删、不召回；要不要退池等她定。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-275）</summary>

`⭐⭐ **「题面点名」策略首次验证成功，且验证得很干净**：<br>　组 8「这个比例只有五分之一」→ 她写 **share**，悬空<br>　组 10 同一题面 → 又写 **share**，第 2 次悬空<br>　组 11 题面点名「用 pro- 开头那个表示比例的正式词，不是 share」→ **proportion，且拼写正确** ✅<br>★★ 关键在于**拼写仍然是她的**：只给了词元描述、没给拼写，她 08-15 T1 作文里写的是 `proportation`，今天对了 ⇒ **点名词元 ≠ 泄漏拼写**，这条方法成立。<br>★ 直接证明她 08-16 的裁决：**「你如果有想要 X，你就在题面直接说，我猜不到的，你说了我自然就写了」** ⇒ 已写进 SKILL §2.3。<br>★ 推论：今天反复出现的"题面逼不出考点"（E-071 词性 · E-073 词元 · E-111 前提 · E-128 同义词 · E-170 块方向）**大半可以用点名解决**，不必再靠改写题面绕。<br>✅+ **她的资产**：`as` 当场调出（两小时前才点名说"老想不到"）· `the public interest`（组 5 写过，今天复用）· `deeply unpopular`（搭配好）· `he or she` 指代唯一 · `months of proper treatment` 全中 · `pension spending` 不可数用对|留痕（方法验证＋资产）|`

</details>

## #0220 这个数字随后下降了，此后再没回到峰值
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F11

**问题是什么**
U · 待排序　0/2

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：「**总感觉完成时是不是更好**」
正确：★ **在 T1 里不是——你的直觉对，但用错了场合。判据是【图表时间轴到哪儿为止】**：<br>　· 时间轴**结束在过去**（1900–2000 这种）→ **全程一般过去时**：`the figure dropped and never returned to that peak`<br>　· 时间轴**延续到现在**（… to the present／未标终点）→ 才用完成时：`has never returned to that peak since`<br>　· 判据一句话：**完成时＝"到【现在】为止"**。图表的"现在"在哪一年，就以那年为准；1900–2000 的图，"此后"指的是 2000 年之前，不是今天<br>★ 与 [[E-198]]（in recent years 必须配完成时）互为反面：**时间状语决定时态，两边都要对上**

**中文触发点**
**这个数字随后下降了，此后再没回到峰值**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-316）</summary>

`**这个数字随后下降了，此后再没回到峰值**|「**总感觉完成时是不是更好**」|★ **在 T1 里不是——你的直觉对，但用错了场合。判据是【图表时间轴到哪儿为止】**：<br>　· 时间轴**结束在过去**（1900–2000 这种）→ **全程一般过去时**：`the figure dropped and never returned to that peak`<br>　· 时间轴**延续到现在**（… to the present／未标终点）→ 才用完成时：`has never returned to that peak since`<br>　· 判据一句话：**完成时＝"到【现在】为止"**。图表的"现在"在哪一年，就以那年为准；1900–2000 的图，"此后"指的是 2000 年之前，不是今天<br>★ 与 [[E-198]]（in recent years 必须配完成时）互为反面：**时间状语决定时态，两边都要对上**|U · 待排序|0/2|`

</details>

> 🔀 **#0221 已于 2026-08-23 从 F11 迁到 F08**（她定：「归属按照你裁定来」）。
> 理由：本条讲的是**同义重复／一个词里已经含了的那一层不要再说一遍**，与 T1 图表无关；
> 判据落在"这个词的语义边界到哪"⇒ 属 F08 词义/近义辨析。原位置留此行指路，条目正文在 F08 段内。

---

# F12 任务层/篇章层

> 只能挂作文验的

## #0222 他们学新技术比较慢 → 是。学术写作换 somewhat，或者直接删 —— 对冲词会把 Task 2 的立场说软
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F12

**问题是什么**
留痕（她判断准确，无缺口可测）　—

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：他们学新技术比较慢
正确：是。学术写作换 `somewhat`，**或者直接删** —— 对冲词会把 Task 2 的立场说软

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— 条目正文自己写着「留痕（她判断准确，无缺口可测）」。
而且语域这一层**孤立中文句里不存在**（§6 实证 #0267：`a bit heavy` 在单句里是完全正确的英语）。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-055）</summary>

`「a bit 是不是有点口语了」|他们学新技术比较慢|是。学术写作换 `somewhat`，**或者直接删** —— 对冲词会把 Task 2 的立场说软|留痕（她判断准确，无缺口可测）|—|`

</details>

## #0271 结论段必须用题目的话重述答案，⛔ 不许把问题重新定义
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-20 ｜ 族 F12

**问题是什么**
中文议论文里，结尾把问题往上拔一层（"真正的问题不是甲，而是乙"）是**加分**手段，显得有洞见。
**雅思大作文里这是减分手段。** 判分员在结论段只查一件事：
**你有没有用题目问的那个说法，把你的答案再说一遍。**
把问题换掉 ＝ 你没有回答被问的那个问题。

```
题目问        好处是不是超过坏处
安全的结论    "好处确实超过坏处，因为……"          ← 用题目的词，答案没跑
危险的结论    "关键不在于要不要冒险，而在于怎么冒"  ← 把问题换成了另一个问题
             判分员读到的是：他没回答我问的那个。
```

**判据（判分清单里的原话）**
`scoring.md §2.3a` TR 清单第 7 项写死：**「结论重述立场 ＋ 理由，不引入新内容」**。
"把问题重新定义"同时踩两条：**没有重述立场** ＋ **引入了新内容**。
再往下一档，官方 6 分描述符正是 **"the conclusions drawn may be unclear, unjustified or repetitive"**
⇒ 结论不清会把任务回应这一项直接压在 6 分。

**那这个洞见就不能写了吗 —— 能，但要换位置和换语法**
```
⛔ 不能做主句、不能做最后一句
✅ 做**从属成分**挂在重述后面：
     "……好处确实超过它的代价，**前提是**这种风险建立在经验和判断之上，而不是盲目的赌博。"
     （主句仍然是题目要的那个答案，洞见退成一个条件状语）
✅ 或者放进**正文段的段尾**当过渡，但那一句仍然要落回"好处/坏处"这根轴上：
     "这类代价可以被经验和判断压低 —— 正因为压得低，好处才盖得过它。"
⇒ 通则：**洞见永远只能当定语和状语，不能当谓语。**
```

**怎么发现的**
2026-08-20　T2-17 中文构思阶段。教练给的改写版把结论写成
「关键不在于要不要承担风险，而在于用经验和判断去挑选值得承担的那一类」，
**她当场质疑**：「我确认下，在"雅思"作文的评判标准中，这种不会觉得偏题吧」。

**我错在哪**
**这次错的是教练，不是她。** 她的质疑成立，改写版已按此修正两处（结论段 ＋ 第 2 段段尾）。
她自己的原稿结论「我认为冒风险对于人的发展至关重要」**反而没有踩这个坑** ——
原稿是直接重述立场的，是教练的改写版把它带偏了。
⇒ 本条建号是为了让这条规则进档案（她问的，§2③），不是记她的错。

**中文触发点**
（这一条挂作文验，不出单点题。每篇作文判分时对着 `scoring.md §2.3a` 第 7 项逐句核结论段。）

### 历史记录
- 2026-08-20 ③ 建号（她质疑教练的改写版，§2③）T2-17 中文构思阶段
  查重（§3.5 B0）：grep 了 `结论` `立场` `回扣` `重新定义` `偏题` `题干`，
  全档 F12 只有一条 #0222（对冲词会把立场说软）。
  与 #0222 不合并：那条讲**单个词的强度**会不会削弱立场（词汇层，改正动作是换词或删词），
  本条讲**结论段整段的功能**（篇章层，改正动作是把问题换回来）。
  问 1、问 2 都不成立 ⇒ 新建。
  ⇒ 本条属 §2④「只能挂作文验的」，不出中译英单点题，连对连错只在作文判分时推进。
- 2026-08-20 ✅ 作文 T2-17　**高压 ✅**（她质疑教练当天建号，同一天就在作文里守住）
  结论段 S20 `I firmly believe the rewards of taking risks genuinely **outweigh** its costs,
  **provided that** such risks are built on experience and judgement rather than blind gambling.`
  ⇒ 用题目的词（outweigh）重述了答案，洞见退成 provided that 引导的条件状语，
  　 主句留给题目要的那个答案 ⇒ 完全符合本条 ⇒ 连对 1。
  ⚠️ 但**同一个毛病出现在 Body1 的段尾**：S8 `Yet this is precisely why the real question is
  　 not whether to take risks, but how to manage them intelligently.` —— 把题目换掉了。
  　 本条管的是结论段，所以不判错；但这说明**换问题这个习惯不只出现在结尾**。
  ⇒ 本条说明补一句：段尾的 L 句同样不许换问题（TR 清单第 5 项就丢在这里）。

## #0311 段首短断言句：主语 ＋ be ＋ 一个形容词，五个词收尾
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F12

**问题是什么**
```
✅ `**The cost of risk is very real.**`（段首）
✅ `**The evidence is mixed.**` · `**This argument is flawed.**` · `**The trend is clear.**`
```
**作用**：段落一开头先用一句极短的话把中心钉死，读者立刻知道这段要说什么，
后面所有句子都是在展开它。这是 CC 清单第 2 项（每段一个中心，topic sentence 单独读能站住）
最容易达成的做法。
**三条硬边**
```
① 短。五到八个词，一个从句都不要。长了就不是钉子了
② 形容词要有**判断**：real / clear / flawed / mixed / limited / misleading
   ⛔ 别用没信息量的：`The situation is complicated.` 等于没说
③ 一段只钉一次。第二句起就要展开，不要连着写两句断言
```
★ 与 #0312 分工：本条是**正文段**的开头，#0312 是**引言**里的立场句。两个位置不同。
⚠️ 反面：段首直接举例（`For example, …`）是最常见的失分写法 —— 读者要读到段中才知道你在论证什么。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
（挂作文验为主。出单点题时用两句式题面：「代价是真实的。它总是伴随着不确定性。」——逼出段首那句极短的断言。）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `topic sentence` `段首`，F12 现有 2 条（#0222 对冲词说软立场 / #0271 结论段不许换问题），都不管段首 ⇒ 新建。
- 2026-08-22 ✅ D4 复习日 C2·组6 第 9 题　**建号后第一次被测**
  两句式题面「代价是真实的。它总是伴随着不确定性。（★ 第一句要短到五个词以内）」，她写
  `**the cost is very real.** it is always accompanied with uncertainty.`
  第一句五个词、形状对（主语 ＋ be ＋ 一个形容词）⇒ 本条命中，连对 1。
  ⚠️ 同句两处不属于本条，各记各的：
  　`is **very** real` ⇒ 记 #0321（中文题面根本没有"很"，very 是她加的 —— **原样复发**）
  　`accompanied **with**` ⇒ 记 #0297（应为 accompanied **by**）
  📋 句首小写两处按 §3.2 手滑豁免。
- 2026-08-23 ✅ D1 学习日 C3·组6 第 7 题　**连对 2 ⇒ 🎓 毕业**
  两句式题面（零提示，换场景）「这类担心是有道理的。过去两年确实出过三次一模一样的事故。」，她写
  `this kind of concern **is completely understandable**. There have been three similar
  accidents over the past two years.`
  ★ 三条硬边逐条核：① 第一句 7 个词，**一个从句都没有** ✅
  　 ② 形容词带判断（understandable，不是 complicated 那种没信息量的）✅
  　 ③ 第二句立刻展开、没有连着写两句断言 ✅ ⇒ 命中，连对 2。
  ★ 出题时特意避开了本条正文里现成的例句（`The evidence is mixed.` `This argument is flawed.`）——
  　 那些拿回去测的是记忆（§6）。她在**没见过的语境**里自己搭出了这个形状。
  📋 顺带用对 #0251：`**this kind of** concern`（this kind of ＋ **单数**）——
  　 #0251 08-22 当天毕业当天塌、现在连对 0，今天在完全没提示的句子里又对了一次。
  　 ⇒ 按复习组口径**顺带用对只列出、不推进 streak**，但这是它的第二次正面证据。
  📋 「一模一样」→ `similar`　⛔ **不判 #0126**：判据是「删掉后**命题被改写**才判」——
  　 本句的主张是"过去两年发生过三次同类事故"，similar 已经把"同类"送到；
  　 「一模一样」加强的是相似度，不改变这个主张。⚠️ 教练有过度判 #0126 的前科（08-22 被她推翻两处），
  　 按 §5 四问自审第 ④ 问归到"有更好的"，进更好版。
  📋 「确实」→ 未出现，同上不判（强调语气词，删掉命题不变）。
  📋 更好：`This kind of concern is entirely legitimate. Over the past two years there have
  　 **indeed** been three accidents of **exactly the same kind**.`
  　（legitimate 比 understandable 更承认"这担心站得住"，而不只是"可以理解"；
  　 indeed 把「确实」送出去；of exactly the same kind 把「一模一样」送出去）

## #0312 引言立场句的骨架：让步 ; however, I believe X outweigh(s) Y
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-20 ｜ 族 F12

**问题是什么**
```
✅ `Risk-taking certainly carries costs; **however, I believe** its rewards **clearly outweigh** them.`
✅ `It must be acknowledged that…; **however, I believe** the rewards **are far greater**.`
```
骨架三件：
```
① 前半让步   承认对方有理（一句就够，别展开 —— 展开留给正文段）
② 转折符号   分号 ＋ however ／ 或句号 ＋ However（见 #0272，⛔ 不能用冒号或逗号）
③ 后半立场   **I believe ＋ 题目里那个动词**
```
★★ **最关键的一条：立场句必须用题目问的那个动词。**
　 题目问 `Do the advantages outweigh the disadvantages?` ⇒ 立场句就要出现 **outweigh**。
　 这与 #0271（结论段必须用题目的话重述答案）是**同一条规则的两端**：
　 引言用它开局，结论用它收口，中间不管怎么绕，判分员两头都能看到你在回答他问的那个问题。
⚠️ 立场句里**不要塞理由** —— 理由是正文段的活。塞进来会让引言超过三句，挤掉正文预算。
⚠️ `I believe` 之后的从句里，**主谓一致要小心**（你这次写成 `the reward … are`，见 #0055）。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— 引言立场句是**篇章层**的东西，
孤立中文句里不存在"引言"，单点题逼不出。判分时对着 `scoring.md §2.3a` TR 清单
第 2 项「立场在引言明确写出」逐句核。
（08-23 组4、组5 两次都因同一理由被弃，⇒ 直接挂死，不再进复习池）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `立场` `引言`，命中 #0271（结论段）与 #0222（对冲词）—— #0271 管结论、本条管引言，是同一规则的两端但位置与动作都不同（一个是"收口时重述"，一个是"开局时宣告"），问 1 不成立 ⇒ 新建，两条互相交叉引用。

---

# F14 衔接/连接词

> 连接词选择与位置、转折的搭法

## #0223 At the same time → On the other hand
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-11 ｜ 族 F14

**问题是什么**
🟡 留痕（08-11 排序：配对意识问题，不是词汇缺口，不占装备位）　留痕

**怎么发现的**
2026-08-11　迷你复习

**我错在哪**
她的：At the same time
正确：**On the other hand**

**中文触发点**
一方面，老年人经验丰富；另一方面，他们学新技术比较慢（08-11 改题面：原题面把答案的前半句写在括号里＝提前公布考点）

### 历史记录
- 2026-08-11 ✅ 迷你复习

<details><summary>原始行（旧表逐字，旧号 E-027）</summary>

`一方面，老年人经验丰富；另一方面，他们学新技术比较慢（08-11 改题面：原题面把答案的前半句写在括号里＝提前公布考点）|At the same time|**On the other hand**|**🟡 留痕**（08-11 排序：配对意识问题，不是词汇缺口，不占装备位）|留痕|**1/2 · ✅D—迷你复习**|`

</details>

## #0224 「First 我觉得有点普通了」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F14

**问题是什么**
留痕（判断性焦虑，非缺口）　—

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：（连接词焦虑）
正确：不普通，**该用就用**。CC 扣的是"机械"不是"简单"。想换：To begin with／On top of that／There is also the fact that

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— 条目正文自己写着「留痕（判断性焦虑，非缺口）」：
First 该用就用，CC 扣的是"机械"不是"简单"。这里没有可测的产出缺口。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-091）</summary>

`「First 我觉得有点普通了」|（连接词焦虑）|不普通，**该用就用**。CC 扣的是"机械"不是"简单"。想换：To begin with／On top of that／There is also the fact that|留痕（判断性焦虑，非缺口）|—|`

</details>

## #0226 「我一直不太知道怎么才能避免反复提同一个单词」
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F14

**问题是什么**
K（策略，需在下一篇作文里验）　0/3

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：（策略性问题，全场最有价值）
正确：**❌ 不是找同义词**（找错反而扣 LR —— 本篇 secure／negative／expenditure 正是这么来的）**✅ 三招**：①代词/指示词 ②上位词 ③直接省略主语。★ **重复关键词在雅思不扣分，题面词尤其**

**中文触发点**
**「我一直不太知道怎么才能避免反复提同一个单词」**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-097）</summary>

`**「我一直不太知道怎么才能避免反复提同一个单词」**|（策略性问题，全场最有价值）|**❌ 不是找同义词**（找错反而扣 LR —— 本篇 secure／negative／expenditure 正是这么来的）**✅ 三招**：①代词/指示词 ②上位词 ③直接省略主语。★ **重复关键词在雅思不扣分，题面词尤其**|**K**（策略，需在下一篇作文里验）|0/3|`

</details>

## #0227 医生反而会指给你更好的
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F14

**问题是什么**
待排序　U（待定）

**怎么发现的**
2026-08-16　复习日 C1·组6

**我错在哪**
她的：doctors will provide guidance on what patients should do
正确：doctors, **by contrast**, will **point patients to something better**

**中文触发点**
医生反而会指给你更好的

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组6

<details><summary>原始行（旧表逐字，旧号 E-109）</summary>

`医生反而会指给你更好的|doctors will provide guidance on what patients should do|doctors, **by contrast**, will **point patients to something better**|待排序|U（待定）|0/2|`

</details>

## #0228 必须承认，这个趋势并非无法理解
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F14

**问题是什么**
第②类 · 教练改写　不出中译英

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：Admittedly, this trend is **not completely unreasonable**
正确：~~not hard to understand~~ ⛔ **08-16 改判：这是教练改了她的意思，不是她的错误**。她说的是 **not completely unreasonable**（并非完全不合理），目标说的是 **not hard to understand**（并非无法理解）——**两个不是同一个命题**，而中文触发点是照教练版写的。拿它去考她＝测"能不能复现教练的改写"。⇒ **第②类，移出中译英组**；档案标注为「教练改写，非她的错误」

**中文触发点**
必须承认，这个趋势并非无法理解

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-146）</summary>

`必须承认，这个趋势并非无法理解|Admittedly, this trend is **not completely unreasonable**|~~not hard to understand~~ ⛔ **08-16 改判：这是教练改了她的意思，不是她的错误**。她说的是 **not completely unreasonable**（并非完全不合理），目标说的是 **not hard to understand**（并非无法理解）——**两个不是同一个命题**，而中文触发点是照教练版写的。拿它去考她＝测"能不能复现教练的改写"。⇒ **第②类，移出中译英组**；档案标注为「教练改写，非她的错误」|第②类 · 教练改写|不出中译英|`

</details>

## #0313 precisely because ＋ 从句 前置 —— 段尾 L 句的骨架
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F14

**问题是什么**
```
✅ `**And precisely because** experience and judgement can drive these costs down,
   the gains can finally exceed the losses.`
结构：precisely because ＋ 原因从句, ＋ 主句结论
```
**为什么它适合放段尾**：把整段讲过的东西压缩成一个原因，然后当场给结论 ——
这正是 TR 清单第 5 项要的「L 句：把论点接回题目」。
同族（都能前置作原因）：
```
precisely because…     正因为…（最有力，强调"就是这个原因"）
It is because… that…   强调句，更重
Since / As…            中性，最轻
Given that…            "考虑到…"，常配数据或事实
```
**三条硬边**
```
① 前置的原因从句后面**必须有逗号**
② 主句要给的是**结论**，不是又一个事实 —— 否则读者不知道你为什么说这段
③ ⛔ 主句里不要再出现 so / therefore（因果已经由 because 承担了，不能双计）
```
★ 与 #0271 #0312 串起来用：引言宣告立场 → 每段段尾用本条把论点接回那根轴 → 结论重述。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
- 2026-08-22（改死后的新题面，下次用）　正因为经验和判断能把成本压下来，收益最后才盖得过损失。
  （★ 必须以「正因为…」的**从句**起句、后面加逗号；⛔ 不许用 It is … that 强调句；⛔ 主句里不许出现 so／therefore）
- 2026-08-22（已作废）　正因为这项技术还不成熟，公司才决定再等一年。（★ 原因从句前置，主句里不要再出现 so／therefore）
  ★ 缺陷：`It is … that` 强调句同样满足"原因在前、无 so"，考点被合法绕过 ⇒ 记 ◎✅
- （建号时）　正因为这些代价可以被经验压低，好处最终才盖得过它。

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `precisely` `because`，F14 现有 6 条讲的是对比词、First 的替代、避免重复等，没有一条讲原因从句前置 ⇒ 新建。
- 2026-08-22 **◎✅** D4 复习日 C2·组1 第 10 题　**算对，连对 1**（题面缺陷，不是她的问题）
  题面「正因为这项技术还不成熟，公司才决定再等一年。（★ 原因从句前置，主句里不要再出现 so／therefore）」
  她写 `**it is precisely because** the technology is not yet mature **that** the company has decided to wait another year`。
  ★ **句子完全成立、也符合题面**：原因在前、结论在后、主句里没有 so／therefore，
  　而且 `It is because… that…` 本来就写在本条正文的同族表里 ⇒ 按 §3.2 ◎✅ 判**算对**，连对 +1。
  ⚠️ 但本条真正的考点「**原因从句前置 ＋ 后面加逗号**」（硬边①）**一次都没被行使** ——
  　 强调句不需要那个逗号。⇒ **这是我的题面没堵住同族的另一条路，是我的账。**
  ⇒ 题面已改死（见下方中文触发点 2026-08-22 那行）：明写不许用 It is … that。
  📋 更好（考点想要的那条路）：
  　`**Precisely because** the technology is not yet mature**,** the company has decided to wait another year.`
  　（同时短两个词）
- 2026-08-23 ✅ D1 学习日 C3·组5 第 7 题　**连对 2 ⇒ 🎓 毕业。08-22 白测掉的那个考点，这次真的行使了**
  题面（**零提示**）「正因为这批数据是志愿者自己填的，我们不能拿它代表全体。」，她写
  `**Precisely because** this data is self-reported by volunteers**,** we cannot use it to
  represent the whole population`。
  ★ 三条硬边逐条核：① 原因从句**前置 ＋ 后面有逗号** ✅（08-22 白测掉的就是这一条）
  　 ② 主句给的是结论（不能拿来代表全体）✅ ③ 主句里**没有 so／therefore** ✅ ⇒ 命中，连对 2。
  ★★ **教练侧要认的一件事**：出题前我在 session 里明写"本条有已知漏洞，零提示排除不掉
  　 `It is because … that` 强调句，她若走那条路算对、账记我头上"。**结果她没走**，
  　 而且走的正是 08-22 被强调句绕开的那条。⇒ 我预判的风险没有发生，这次是实打实的。
  📋 `this data **is**` 不判：data 作不可数集合名词配单数谓语在现代英语里是主流用法之一，
  　 尤其配 this（`this data is`）⇒ §0.8 造得出母语者句子，不判错。
  📋 顺带用对：`self-reported` —— 中文「自己填的」一个词到位，比 filled in by themselves 紧得多。
  　 `the whole population` 在统计语境里正是"总体"的术语，用得准。
  📋 更好：`Precisely because these data **are** self-reported, we cannot treat them as
  　 representative of the population **as a whole**.`
  　（`self-reported` 已含"由本人填"⇒ by volunteers 冗余可删；
  　 `treat X as representative of` 是这个意思的固定搭配，比 use it to represent 更学术）

## #0314 While ＋ 从句 前置：它有让步和对比两个身份
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F14
⚠️🔍 **REVIEW 池**

**问题是什么**
```
让步（＝ although）  `**While** these costs are impossible to calculate, they can be kept to a minimum.`
                     ＝ 虽然算不出来，但压得低
对比（＝ whereas）   `**While** the price of taking risks is real, so is the cost of playing it safe.`
                     ＝ 冒险有代价，求稳也一样（两边并列，没有谁让谁）
```
**判据**：后半句是**推翻**前半句（让步），还是**并列**着说另一面（对比）？
两种都合法，但读者要靠后半句才能分清 ⇒ **后半句必须写得让关系一眼看出来**。
**三条硬边**
```
① 前置的 While 从句后面**必须有逗号**；后置时不加
② ⛔ 主句里不能再有 but：`~~While A, but B~~`（中文"虽然…但是"的直译，最常见的中式错）
③ While 还有第三个意思"当…的时候"（时间）—— 一句里同时能读成时间和让步就要换词
```
同族（按强度）：`While` ＜ `Although` ＜ `Even though`（最强，事实已成立，见 #0261）
＜ `Despite / In spite of` ＋ **名词**（不能接从句）。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
虽然这些代价事先算不清楚，但它们是可以被压低的。（用 While 前置，注意主句里别再放 but）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `While` `Although` `让步`，命中 #0261（even if / even though）—— 那条管的是**假设 vs 事实**的分工，本条管的是 **While 的让步/对比两个身份 ＋ 前置逗号 ＋ 不能配 but**，问 2 不成立 ⇒ 新建，与 #0261 交叉引用。
- 2026-08-22 ✅ D4 复习日 C2·组9 第 9 题　**建号后第一次被测**
  题面「虽然这套系统还在测试，公司已经开始让新人上手了。（★ 用 While 前置，主句里别再放 but）」
  （新写触发点 —— 存档那条与 #0301 的"事先算不清"撞词），她写
  `**While** the system is still in testing**,** the company has started having new staff use it`。
  ★ **三条硬边全对**：① While 前置 ② 后面有逗号 ③ **主句里没有 but**（中式"虽然…但是…"没有复现）。
  ⇒ 命中，连对 1。
  📋 顺带用对 #0325：`new **staff**`（不可数，没写成 staffs）。
  📋 更好：`While the system is still **being tested**, the company has **already put new staff on it**.`
  　（in testing 偏技术语域；`started having … use it` 五个词的使役结构 → `put … on it` 三个词）
- 2026-08-23 ◎✅ D1 学习日 C3·组4 第 7 题　**算对，连对 2 ⇒ 🎓 毕业 ＋ 进 REVIEW 池**
  题面（零提示）「城市里的房租一年比一年高，小县城的房子却越来越难卖出去。」，她写
  `house rent in big cities goes up year after year, **while** house in small county towns are
  becoming increasingly difficult to sell`。
  ★ **她走的是后置 while**（逗号在 while 前面），不是本条标题里的**前置**。
  　 按 §3.2「判 ❌ 只有两个理由」：`A, while B` 的对比用法是标准英语、意思也全送到 ⇒ **算对**。
  ★ 而且本条的**另一半考点确实被行使了**：她用的是 while 的**对比身份**（＝ whereas），
  　 不是让步；主句里也**没有 but**（中式"虽然…但是"没复现）⇒ 硬边②守住。
  ⚠️ 没被行使的是**前置 ＋ 后面那个逗号**（硬边①）。
  　 教练侧：题面里两个分句是**对等的两件事**，中文用「却」连接 ——
  　 这种形状最自然的英文本来就是后置 while，我没有任何合法手段（零提示）把它翻到句首。
  ⇒ 按 §3.3 照常毕业 ＋ 打 ⚠️🔍 标记，改好的题面存进 `review_pool.md`。
  ❌ 同句一处顺带用错，不在本条扣分：`**house** in small county towns **are**` → `**houses**` ⇒ 记 #0048。
  📋 顺带：`year after year` 译"一年比一年"很准 · `increasingly difficult to sell` 结构正确。
  📋 更好：`**While** rents in big cities **rise** year after year, houses in small county towns
  　 are becoming **harder and harder** to sell.`（把 while 翻到句首＝行使本条的前置那一半；
  　 `rents` 一个词顶掉 `house rent`；`harder and harder` 比 increasingly difficult 更口语顺、也更短）

## #0315 让步开场一族：It must be acknowledged that ／ Admittedly
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F14

**问题是什么**
```
按长度排（意思几乎一样，差别在重量和位置）：
`**Admittedly**, …`                    最短，最灵活 ★ 日常首选
`**It is true that** …`                中性
`**There is no denying that** …`       强调"无法否认"
`**It must be acknowledged that** …`   最正式最长（8 个词）★ 你用的这个
```
**★★ 位置规则（比选词更重要）**
```
✅ 用在**让步段的开头**   —— 这段就是要承认对方，用它开场名正言顺
⛔ 用在**引言里紧接着题面转述之后** —— 那个位置读者刚知道话题，还没有"对方观点"可承认，
   这句话就是空转。你 08-20 那篇就是这样，所以我在更好版里把它删了
   —— **删它不是因为块不好，是因为位置不对。**
```
**让步开场的铁律（与 #0271 同源）**：承认完**必须转回来**，段尾要落回自己的立场。
只承认不转，读者会以为你改了主意 —— 这正是 08-19 那篇丢 TR 的原因。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
（挂作文验为主。出单点题时用两句式题面：「必须承认，这种做法确实有风险；但风险是可以控制的。」）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `Admittedly` `acknowledg` `必须承认`，命中 #0228「必须承认，这个趋势并非无法理解」—— 那条已于 08-16 改判为**第②类·不出中译英**的留痕（内容是"教练改写，非她的错误"），**没有规则**，谈不上同一条 ⇒ 新建，并交叉引用 #0228。
- 2026-08-22 ✅ D4 复习日 C2·组5 第 10 题　**建号后第一次被测**
  题面「必须承认，这种做法确实有风险；但风险是可以控制的」，她写
  `**It must be acknowledged that** this kind of method carries risks; however, these risks are manageable`。
  让步开场块一字不差 ⇒ 命中，连对 1。
  📋 顺带用对（一句里四条）：
  　`**this kind of** method`（单数！＝ #0251 的考点，那条今天上午靠 ◎✅ 毕业、考点没被行使）
  　`**carries** risks`（#0292 carry ＋ 抽象名词）
  　`risks**;** **however,**`（#0272 分号 ＋ #0317 however 后面的逗号，两条都对）
  ★★ 与组 4 #0317 的 ❌ 对照：**她手里有 however，没有 Yet。**
  　 缺口是具体的一个词能不能句首、后面要不要逗号，不是"转折"这个功能。
  📋 更好：`… **does carry** risks; however, **those** risks are manageable.`
  　（does carry 把中文「确实」送进去；those 指前半句提过的，比 these 自然）
- 2026-08-23 ✅ D1 学习日 C3·组5 第 1 题　**连对 2 ⇒ 🎓 毕业**
  题面（零提示，两句式）「必须承认，网课确实省下了大量通勤时间；但学生之间的交流也被砍掉了大半。」，她写
  `it must be acknowledged that online courses **indeed** save people a lot of commute time,
  but student interaction has also been cut by more than half`。
  ★ 让步开场块一字不差，而且这次是**换了场景**（网课，不是 08-22 的"这种做法有风险"）⇒ 命中，连对 2。
  ★ 位置也对：本条正文写死「用在让步段的开头」，两句式题面里她放的正是这个位置。
  📋 顺带用对 #0126（三层全部落地）：
  ```
  确实 → indeed ✅ ｜ 大量 → a lot of ✅ ｜ 大半 → more than half ✅
  ```
  ★★ 「大半 → more than half」值得单独记一笔：这正是 08-23 上午撤销的 #0330 想管的那个刻度
  　（当时她把"有一半"写成 more than half）。今天中文写的是"大半"，more than half **完全正确** ——
  　 说明那次不是刻度感缺失，是单次偏移。她 08-23 撤销 #0330 的判断，今天被证据支持。
  📋 `commute time` 不判错：`the average commute time` 造得出母语者句子（§0.8）⇒ 只进更好版。
  📋 更好：`It must be acknowledged that online courses **do** save people a great deal of
  　 **commuting** time; **however**, contact between students has been cut by more than half.`
  　（`do save` 比 `indeed save` 送"确实"更自然；commuting time 是英式默认；
  　 两个独立分句之间用分号 ＋ however 比 comma ＋ but 书面）

## #0316 Alternatively ＝ 换一种情形，不是"另一方面"
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F14

**问题是什么**
```
✅ `**Alternatively**, if a new line manager simply takes a dislike to them, …`
   ＝ 或者换一种情况：如果是主管不喜欢他呢
```
四个最容易串的，按**它们连接的是什么关系**分：
```
Alternatively      **同一件事的另一种可能／另一条路**（并列的两个选项）
On the other hand  **对立的另一面**（前后必须真的对立，而且前面通常要有 On the one hand）
By contrast        **拿两个东西对照**，差别明显
Equally            **同等重要的另一点**（不是对立，是并排加一条）
```
**判据**：后面这句和前面是**换一条路**（Alternatively）、**唱反调**（On the other hand）、
**做对比**（By contrast）、还是**再加一条同分量的**（Equally）？
⚠️ `On the other hand` 的高频错法：**前面没有 On the one hand 就单独用**。
　 单独用不算错，但一旦用了 On the one hand，就**必须**有下文（这正是 #0223 记的那个坑）。
★ 这四个都放**句首 ＋ 逗号**。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
或者换一种情况：如果是客户临时改了要求呢。（"或者换一种情况"用一个词开头）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `Alternatively` `On the other hand`，命中 #0223（At the same time → On the other hand）—— 那条的改正动作是**把选错的对比词换掉**，本条是**四个功能不同的连接词怎么挑**，问 2 不成立 ⇒ 新建，与 #0223 交叉引用。
- 2026-08-22 ✅ D4 复习日 C2·组7 第 9 题　**建号后第一次被测**
  题面「或者换一种情况：如果是客户临时改了要求呢」，她写
  `**Alternatively,** what happend if the client modifies the requirements at the last minute`。
  用一个词开头、位置和后面的逗号都对 ⇒ 命中，连对 1。
  📋 顺带：`at the last minute` 译"临时"很准。
  📋 两处不判但留痕：
  　`happend` 是非词 ⇒ §3.2 复习组豁免。⚠️ 但它藏着歧义 —— 若她要的是 `happened`，
  　 时态就错了（if 从句用 modifies 现在时 ⇒ 主句该是 **happens**）。更好版按 happens 写死。
  　 句末缺问号（中文的"呢"是疑问）⇒ 复习组按标点手滑不判，**作文里照记**。

## #0317 转折四兄弟：But ＜ Yet ＜ However ＜ Nevertheless
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F14

**问题是什么**
```
But           最轻、最口语。⚠️ 书面里**不要句首用**，放句中连接两个分句
              `Costs are real, **but** they can be contained.`
Yet           书面、有力。★ **可以句首直接用，后面不加逗号**
              `**Yet** this is precisely why…`
However       最通用。句首、句中、句末都行，**位置不同要有逗号隔开**
              `**However**, I believe…` · `I believe, **however**, that…`
Nevertheless  最重，带"尽管如此还是"的让步味，一篇用一次就够
              `**Nevertheless**, the gains outweigh the losses.`
```
**三条硬边**
```
① Yet 句首**不加**逗号；However 句首**必须加**逗号 —— 这一条最容易错
② 转折词前面接的是**上一句的句号或分号**，⛔ 不能是逗号（逗号粘连）也不能是冒号（见 #0272）
③ 一段里**只转一次**。连着两个转折词读者会跟丢
```
★ 语域梯度记法：说话用 but，写作用 however，想让句子有劲用 Yet，让步收束用 Nevertheless。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
成本确实降了，销量却没起来。（"却"用一个可以句首直接接、不加逗号的词）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `Yet` `However` `Nevertheless`，全档零条目（只有今天作文的记录）；与 #0272（分句之间用哪个符号）互补 —— 那条管**符号**，本条管**词**，两条配套 ⇒ 新建。
- 2026-08-22 ❌ D4 复习日 C2·组4 第 10 题　**建号后第一次被测就塌**
  题面「证据很充分，法官却做出了相反的判决。
  　（★「却」用一个能放**句首**、后面**不加逗号**的转折词）」——点名已经很死，指向 Yet／But。
  她写 `**even though** the evidents are solid, the judge made a decision to the contrary`。
  ★ 她换成了**让步从句**：本条四兄弟一个都没出场，而且 even though 前置**必须加逗号**，
  　 恰恰是题面明写不要的那种。⇒ **题面无缺陷，这一处记她的**，连错 1。
  ⚠️ 判 ❌ 不判 ◎ 的理由：◎ 的条件是"她的答案符合题面"。
  　 题面点名了"句首 ＋ 不加逗号 ＋ 转折词"三个条件，她的答案一个都不满足 ⇒ 不构成 ◎。
  ★ 这条暴露的很可能是：**她不知道 Yet 可以直接放句首**（She 手里只有 although/even though 这条让步路）。
  　 正确：`The evidence was solid, **yet** the judge ruled the other way.`
  　 四兄弟的分工再记一次：`But`（最轻，句中）＜ `Yet`（句首不加逗号）＜ `However,`（句首**要**逗号）
  　 ＜ `Nevertheless,`（最重，句首要逗号）。**只有 But 和 Yet 后面不加逗号。**
  ⚠️ 同句一处不属于本条：`the **evidents are**` ⇒ **新建 #0325**（不可数名词）。
- 2026-08-23 ✅ D1 学习日 C3·组6 第 5 题　**建号后第一次答对，连对 1、连错归 0**
  题面「这几年培训做了不少，一线的差错率却没怎么降。（★ 用 Yet）」（连对 0 ⇒ 按 §6 给英文词），她写
  `Significant training has been provided over the past years, **yet** the frontline error rate
  has shown litte decline`。
  ★ **给了词之后仍然有东西可测，而且她测到了**：本条的规矩是
  　「**只有 But 和 Yet 后面不加逗号**」—— 她写的是 `, yet the frontline…`，**yet 后面没有逗号** ✅。
  　 上一次（08-22）她整条绕开、退回 even though 让步从句；这次 yet 用起来了 ⇒ 命中。
  ⚠️ 她用的是**句中的并列连词**位置（`A, yet B`），不是句首。两种都合法
  　（`A, yet B` 是标准并列；`Yet B.` 是句首副词用法）⇒ **不判错**，句首那个位置留给下次。
  📋 `litte` 是非词（little）⇒ §3.2 复习组手滑豁免。
  📋 `over the past **years**` ⚠️ 不地道不判错：英文默认是 `over the past **few** years` ／
  　 `in recent years`；光 the past years 读得懂但少一个限定词 ⇒ 按 §5 四问自审第 ④ 问
  　 判为「有更好的」，进更好版，⛔ 不记错。
  📋 顺带用对：`has been provided` 现在完成时被动，与「这几年」配对正确 ·
  　 `has shown little decline` 用名词化说"没怎么降"，比 didn't decline much 书面。
  📋 更好：`A great deal of training has been provided **in recent years**, yet the error rate
  　 **on the front line** has barely fallen.`
  　（`Significant training` 略生硬；`frontline error rate` 三个名词叠 → 拆成介词短语；
  　 `has barely fallen` 比 has shown little decline 少两个词）

## #0318 「正因为如此」一族：this is precisely why ／ For this very reason
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F14

**★ 2026-08-23 补进正文：这一族真正会塌的地方是【指示词 this】**
```
这一族每个成员里都有一个**指着前面那句话**的词，那个词一掉，块就不成立：
  This is precisely why …          ← this 就是主语，掉了整句没主语
  For **this** very reason, …      ← 掉了 this ⇒ `~~For the very reason,~~` 不是英语
  It is for **this** reason **that** … ← 强调句：this 和 that 少一个都散架
  which is exactly why …           ← which 指前一整句
  That is why …                    ← that 指前一整句
⛔ `~~It is precisely because of that many companies have…~~`
   —— `because of` 后面要一个名词性成分：`because of **this**`；
      而且强调句 `It is … **that** …` 的 that 也不能省。
   两条合法的路，二选一：
   ✅ `It is precisely **because of this that** many companies have…`（强调句，最重）
   ✅ `**This is precisely why** many companies have…`（最省、最有力）
★ 找法：写完这一族的块，回头找那个指着上文的词（this / that / which）在不在。在，块才成立。
```

**问题是什么**
```
✅ `Yet **this is precisely why** the real question is…`
✅ `**For this very reason**, the safest choice usually carries the lowest payoff.`
```
一族（都把**前一整句**变成后一句的原因，比 So / Therefore 有力得多）：
```
`**This is precisely why** …`      最口语化也最有力，主语 this 指前面整句
`**For this very reason**, …`      正式，very 在这里是"正是这个"不是"很"
`**which is exactly why** …`       接在前句后面，不另起句
`**That is why** …`                最中性
`**It is for this reason that** …`  强调句，最重，一篇一次
```
**判据**：`So` 和 `Therefore` 只是"所以"，**不强调是哪个原因**；
这一族强调"**就是前面那件事**导致的"，用在你刚说完一个关键事实、要立刻推结论时最合适。
⚠️ `For this very reason` 里的 **very 不能删** —— 删了就变成普通的 for this reason，力度掉一半。
⚠️ 这一族**不能和 so / therefore 叠用**：`~~This is precisely why therefore…~~`

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
- 2026-08-22（改死后的新题面，下次用）　正因为如此，很多公司干脆不再自己招人了。
  （★「正因为如此」用**带 very 的那个块**；⛔ 不许只写 For this reason，⛔ 也不许用 Therefore／That is why）
- 2026-08-22（教练当天实际用的，已作废）　正因为如此，很多公司干脆不再自己招人了。
  （★「正因为如此」用一个能放句首的块）
  ★ 缺陷：教练重写题面时把括号里"用带 very 的那个块"整句丢了 ⇒ For this reason 合法绕过，记 ◎✅
- （建号时）　正因为如此，最省事的办法往往回报最低。（"正因为如此"用带 very 的那个块）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `precisely why` `For this reason` `That is why`，全档零条目；与 #0313（precisely because 前置）不同 —— 那条把**原因写在从句里**，本条把**原因指回前一整句**，问 1 不成立 ⇒ 新建，两条交叉引用。
- 2026-08-22 **◎✅** D4 复习日 C2·组8 第 9 题　**算对，连对 1**（题面缺陷，不是她的问题）
  题面「正因为如此，很多公司干脆不再自己招人了。（★「正因为如此」用一个能放句首的块）」，她写
  `**For this reason,** many companies have completely stopped hiring directly`。
  ★ 这个块成立、位置对、逗号也对，**完全符合我写的题面** ⇒ 判 ◎✅，连对 +1。
  ⚠️⚠️ 但本条要的是**带 very 的那个**（`For this **very** reason`）——
  　 **存档触发点的括号里原本写着「用带 very 的那个块」，我重写题面时把这句 pin 整个丢了。**
  　 这是今天第五次因为提示写坏／丢失而白测一条（#0313 #0294 #0276 #0251 #0318）。**我的账。**
  ⇒ 题面已改死，见下方中文触发点 2026-08-22 那行。
  📋 更好：`For this **very** reason, many companies have **simply stopped recruiting in house**.`
  　（`completely`→`simply`：中文「干脆」是"索性"不是"彻底"）
- 2026-08-23 ❌ D1 学习日 C3·组3 第 8 题　**连对 1 → 0，连错 1**
  题面（**零提示**，本条连对 1 ⇒ 新规则不给提示）
  「正是因为这一点，很多公司干脆不再自己招人了；也正是出于这个原因，外包市场才涨得这么快。」她写
  `**It is precisely because of that** many companies have simply stopped hiring in-house;
  **for the very reason**, the outsourcing market has grown so rapidly`。
  ★ **两半都塌，而且是同一个零件：指着上文的 this 掉了。**
  ```
  前半  `It is precisely because of that many companies have…`
        ① `because of` 后面缺名词性成分 ⇒ 要 `because of **this**`
        ② 强调句 `It is … that …` 的 that 也没有 ⇒ 整句没有主句连接
        ⇒ 不是"不地道"，是**句子本身不成立**（§3.2 判 ❌ 理由①）
        正确：`It is precisely **because of this that** many companies have…`
        　　　或 `**This is precisely why** many companies have…`
  后半  `for the very reason,` → `**For this very reason**,`
        固定块是 `For **this** very reason`，掉了 this 就只剩 `for the very reason`，
        而 `the very reason` 在英语里要接下文：`for the very reason **that** it is cheap`。
        句首孤零零一个 `For the very reason,` 不是英语。
  ```
  ★★ 08-22 那次白测的是 **very**（我把提示丢了，她写 For this reason ⇒ ◎✅）；
  　 这次她**把 very 记住了、却把 this 丢了** —— 说明块是按"听起来像"存的，不是按结构存的。
  　 ⇒ 已把「指示词 this 是这一族的命门」写进本条正文（见上方 2026-08-23 补进正文那一段）。
  ⚠️ 机制上同 `reminders.md` **R3**（固定块里那个小零件掉了），
  　 但本块**有编号**且这就是本条的考点 ⇒ 判在本条，不另记 R3。
  📋 顺带用对：`simply stopped hiring **in-house**`（副词用法与连字符都对）·
  　 `the outsourcing market has grown so rapidly`（现在完成时对）。
  　 她当场点名「这个 in-house 可以建个条目练习下」⇒ 全档 grep `in-house` `in house` 零条目 ⇒ 新建 **#0333**。

## #0319 条件连接词四档：if ＜ as long as ＜ provided that ＜ on condition that
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F14

**成员出题账**
```
① if                 未单独出过（最中性，不必测）
② as long as         2026-08-23 组3 题面「只要大家按时交材料，进度就不会拖」⇒ ✅
③ provided (that)    2026-08-23 组3 题面「我认为这条路走得通，前提是预算足够」⇒ ✅
④ on condition that  未出过
⑤ unless             2026-08-22 组3 题面「除非明年拿到新的资金，这个项目就得停」⇒ ✅
```

**问题是什么**
```
if                最中性，什么场合都行
as long as        口语，强调"只要…就"          `**as long as** you plan ahead`
provided (that)   ★ 正式，强调这是**必要条件**   `**provided that** such risks rest on judgement`
on condition that 最硬，常用于协议、规定        `released **on condition that** he reports weekly`
unless            ＝ if not（反向）             `**unless** the policy changes`
```
**三条硬边**
```
① provided 后面的 that **可以省**：`provided such risks rest on judgement` ✅
② 这一族引导的条件从句里**用现在时表将来**：`provided that prices **rise**` ✅ `~~will rise~~` ❌
③ ⛔ unless 后面**不能再加否定**：`~~unless you don't go~~`（意思会反）
```
★★ **作文里最值钱的用法**：把一个洞见退成条件状语挂在立场后面 ——
　 `…the rewards outweigh the costs, **provided that** such risks rest on experience.`
　 主句仍然回答题目，洞见退到从句里。这正是 #0271 那条规则要的动作，**你已经做对了一次**。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
我认为这个办法可行，前提是预算足够。（"前提是"用最正式的那个条件词）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `provided` `as long as` `unless`，7 处 `provided` 全是动词 provide（#0014 的内容），零条目讲条件连接词 ⇒ 新建，与 #0271 交叉引用。
- 2026-08-22 ✅ D4 复习日 C2·组3 第 3 题　**建号后第一次被测**
  题面「除非明年拿到新的资金，这个项目就得停」，她写
  `**unless** there is new funding next year, the project will stop`。
  unless 挑对；硬边③（unless 后面不许再加否定）也守住了，没有写成 `unless there isn't…` ⇒ 命中，连对 1。
  📋 顺带用对 **#0324**（今天刚建）：从句 `there **is**` 用现在时、主句 `**will** stop` 带 will ——
  　 建号后 40 分钟就用对了。
  📋 更好：`Unless new funding **is secured** next year, the project **will have to be shelved**.`
  　（"拿到"是个动作 ⇒ secure；"就**得**停"的强制层用 have to 补回来）
  📋 「得」译弱不判 —— 沿用 08-20 #0249 的先例。
- 2026-08-23 ✅ D1 学习日 C3·组3 第 9 题　**连对 2 ⇒ 🎓**
  题面（**零提示**）「我认为这条路走得通，前提是预算足够；只要大家按时交材料，进度就不会拖。」她写
  `I believe this approach is viable, **provided that** the budget is sufficient; **as long as**
  everyone submits their materials on time, the schedule will not be delayed`。
  ★ **一题两个成员，选词、语域、时态全对**：
  ```
  选词  「前提是」＝ 必要条件、书面 ⇒ **provided that** ✅（没有退回最中性的 if）
        「只要…就」⇒ **as long as** ✅
  语域  正式那一档给了 provided that，口语那一档给了 as long as，两个各就各位
  硬边② 条件从句用现在时表将来：`the budget **is** sufficient` ✅ `everyone **submits**` ✅
        主句带 will：`will not be delayed` ✅　⛔ 没有写成 `~~will be sufficient~~`
  ```
  ⇒ 命中，连对 2。
  📋 顺带用对：`viable`（"走得通"用一个词收掉，比 workable 更书面）· `submit their materials
  　 **on time**`（#0301 一族的时间块，📋 留痕不推进）。

---

# F15 语域/正式度

> 口语词进书面、缩写、对冲词

## #0229 7pm → 7 pm（数字与 am/pm 之间留空格）
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F15

**问题是什么**
⚪ 劝退（排版细节，不扣分）✅ 08-11 她自己就写对了 before 4 pm　留痕

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`7pm`
正确：`7 pm`（数字与 am/pm 之间留空格）

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— 考点是 `7pm` → `7 pm` 的空格，
排版层面的手滑，中译英判不了；T1 里才照记。

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-034）</summary>

`晚上七点|`7pm`|`7 pm`（数字与 am/pm 之间留空格）|**⚪ 劝退**（排版细节，不扣分）✅ 08-11 她自己就写对了 `before 4 pm`|留痕|—|`

</details>

## #0230 is a bit expensive → is no longer worth it
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F15

**问题是什么**
P11 词义＋对冲词 a bit（今天第 2 次）　R · P11

**怎么发现的**
2026-08-16　复习日 C1·组4

**我错在哪**
她的：is **a bit expensive**
正确：is **no longer worth it**

**中文触发点**
这个方案就不划算了

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组4

<details><summary>原始行（旧表逐字，旧号 E-085）</summary>

`这个方案就不划算了|is **a bit expensive**|is **no longer worth it**|P11 词义＋对冲词 a bit（今天第 2 次）|R · **P11**|0/3|`

</details>

## #0231 「本来想用 don't know，但是感觉太不正式了」
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F15

**问题是什么**
K　0/3

**怎么发现的**
2026-08-16　复习日 C1·组4

**我错在哪**
她的：**08-16 题面加死限定：这些疗法为什么偶尔管用，没人解释得清**（"解释得清"锁 explain；原题面「说得清」逼不出）
正确：`No one knows why…` **也成立**（原判「两个都不对」是过度判定，撤销）；目标块 = `No one can **explain** why…`（explain 比 know 更贴"解释得清"，且比 don't know 正式）<br>★ 08-16 她定：**这条要学，不移出题组，用加死题面的方式测**

**中文触发点**
这些疗法为什么偶尔管用，没人解释得清。（★ "解释得清"锁一个正式动词）
（旧留痕：「本来想用 don't know，但是感觉太不正式了」—— 08-16 她定：这条要学，
　用加死题面的方式测。`No one knows why…` 也成立，目标块是 `No one can explain why…`）

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组4

<details><summary>原始行（旧表逐字，旧号 E-095）</summary>

`「本来想用 don't know，但是感觉太不正式了」|**08-16 题面加死限定：这些疗法为什么偶尔管用，没人解释得清**（"解释得清"锁 explain；原题面「说得清」逼不出）|`No one knows why…` **也成立**（原判「两个都不对」是过度判定，撤销）；目标块 = `No one can **explain** why…`（explain 比 know 更贴"解释得清"，且比 don't know 正式）<br>★ 08-16 她定：**这条要学，不移出题组，用加死题面的方式测**|**K**|0/3|`

</details>

## #0233 政府保障权利 ↔ 争取权利
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F15

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：secure？make sure？（她 08-15 问）
正确：**guarantee ／ safeguard ／ uphold** a right（已有权利的保障）；**secure**＝争取到尚未拥有的（secure the right to vote）；make sure 口语→书面 **ensure**

**中文触发点**
政府保障（已有的）权利 ↔ 争取（未有的）权利

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-188）</summary>

`政府保障（已有的）权利 ↔ 争取（未有的）权利|secure？make sure？（她 08-15 问）|**guarantee ／ safeguard ／ uphold** a right（已有权利的保障）；**secure**＝争取到尚未拥有的（secure the right to vote）；make sure 口语→书面 **ensure**|待排序|U（待定）|`

</details>

## #0234 很多年轻家长下班很晚
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F15

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：get off work really late
正确：**do not finish work until late**（get off work／really 偏口语；她的成立）

**中文触发点**
- 2026-08-20　体育用品这一行现在竞争非常激烈。（书面版）
很多年轻家长下班很晚（书面版）

### 历史记录
- （从未被判定过）
- 2026-08-20 ❌ D3 学习日 C2·组3 第 3 题（顺带）　本条第一次被判定
  她写 `is **really** fierce **right now**`。两个都是口语词，作文里要换：
  　`really` → `extremely / particularly / very`　（程度这一族见 #0267）
  　`right now` → `currently / at present / at the moment`
  书面版：`Competition in the sporting goods sector is **currently extremely fierce**.`
  同族一起记（本条的滚动表）：
  　`a lot of` → `a great deal of / considerable`　`kids` → `children`　`get` → `obtain / receive`
  　`big` → `large / substantial`　`things` → `factors / aspects`　`nowadays` → `in recent years`
  ⇒ 连错 1。
- 2026-08-20 ❌ 作文 T2-17（当日第 2 处，与上一行合并为当天一次净结果）
  S14 `It works **the exact same** way in daily life` —— 口语结构进书面。
  书面版：`The same holds outside work` ／ `in exactly the same way`。
  ⇒ 当日两处（组3 的 `really` `right now` ＋ 本处），同一个机制：**说话的语气直接写进了作文**。
- 2026-08-22 ✅ D4 复习日 C2·组5 第 9 题
  题面「很多年轻家长下班很晚。（★ 写成书面语，不要用口语块）」，她写
  `many young parents **finish** their workday very late`。
  没有退回口语块 `get off work really late`，动词换成了 finish、`really` 也换掉了 ⇒ 命中，
  连对 1、连错归 0。
  📋 `very` 不判（中文明写「很晚」），但作文里按 #0321 通常删掉更有力。
  📋 更好（档案里存的目标块）：`Many young parents **do not finish work until late**.`
  　（not … until 比 very late 书面，同时把 very 去掉）
<details><summary>原始行（旧表逐字，旧号 E-190）</summary>

`很多年轻家长下班很晚（书面版）|get off work really late|**do not finish work until late**（get off work／really 偏口语；她的成立）|待排序|U（待定）|`

</details>

## #0235 这一政策进一步恶化了政府的处境
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F15

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：has worsened the government's situation **further**
正确：has **further worsened** the government's situation（正式书面里 further 更常挂在动词前；句末也对，她的成立）

**中文触发点**
这一政策进一步恶化了政府的处境

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-227）</summary>

`这一政策进一步恶化了政府的处境|has worsened the government's situation **further**|has **further worsened** the government's situation（正式书面里 further 更常挂在动词前；句末也对，她的成立）|待排序|U（待定）|`

</details>

## #0236 there isn't any significant improvement → there is not any…（更好是整句换成 E-277 的实义主语版）
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F15

**问题是什么**
⚠️ 语域，不是语法错（她那句语法完全正确）　第③类 · 挂作文当场抓，不出中译英

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：`there **isn't** any significant improvement`
正确：`there **is not** any…`（更好是整句换成 E-277 的实义主语版）

**中文触发点**
⚠️ **减法型（第③类）**：正式书面语不用缩写 —— `isn't / don't / can't` 一律写全 `is not / do not / cannot`

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-278）</summary>

`⚠️ **减法型（第③类）**：正式书面语不用缩写 —— `isn't / don't / can't` 一律写全 `is not / do not / cannot`|`there **isn't** any significant improvement`|`there **is not** any…`（更好是整句换成 E-277 的实义主语版）|⚠️ 语域，不是语法错（她那句语法完全正确）|**第③类 · 挂作文当场抓**，不出中译英|–|`

</details>

## #0237 有些病人好几年没有好转了
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F15

**问题是什么**
⚠️ 不地道（不是硬错）　U · 待排序

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：have **showed**
正确：have **shown**（show 的过去分词标准形是 shown；showed 只作过去式。词典虽列 showed 为次选分词，正式写作一律 shown）

**中文触发点**
**有些病人好几年没有好转了**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-282）</summary>

`**有些病人好几年没有好转了**|have **showed**|have **shown**（show 的过去分词标准形是 shown；showed 只作过去式。词典虽列 showed 为次选分词，正式写作一律 shown）|⚠️ 不地道（不是硬错）|U · 待排序|0/2|`

</details>

## #0238 这个数字随后下降了
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F15

**问题是什么**
U · 待排序　0/2

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：「the figure dropped（**能用 drop 么**）」
正确：✅ **能，而且是标准 T1 写法**。她这个疑问来自我组 2 说过 `workforce drops` 不好——那句话的边界是**主语**，不是 drop 这个词：<br>　✅ **drop 配【数字/量/比率/价格】**：the figure dropped · the number dropped · prices dropped<br>　⚠️ **不配【人的集合体】**：~~the workforce drops~~ → the workforce **shrinks / declines**<br>**T1 下降四兄弟的分工**（够用，别再扩）：<br>　`fall` 最中性最常用 · `drop` 同义，暗示快一点/明显一点 · `decline` 稍正式，配长期趋势 · `decrease` 正式，与 increase 配对<br>★ 教训归教练：我组 2 那句话说得太宽，她当场记住了边界并回来核对 —— **元模式「教练规则写太宽」今天第 1 次**（08-16 已记 6 次，LESSONS §1.2e）

**中文触发点**
**这个数字随后下降了**

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-299）</summary>

`**这个数字随后下降了**|「the figure dropped（**能用 drop 么**）」|✅ **能，而且是标准 T1 写法**。她这个疑问来自我组 2 说过 `workforce drops` 不好——那句话的边界是**主语**，不是 drop 这个词：<br>　✅ **drop 配【数字/量/比率/价格】**：the figure dropped · the number dropped · prices dropped<br>　⚠️ **不配【人的集合体】**：~~the workforce drops~~ → the workforce **shrinks / declines**<br>**T1 下降四兄弟的分工**（够用，别再扩）：<br>　`fall` 最中性最常用 · `drop` 同义，暗示快一点/明显一点 · `decline` 稍正式，配长期趋势 · `decrease` 正式，与 increase 配对<br>★ 教训归教练：我组 2 那句话说得太宽，她当场记住了边界并回来核对 —— **元模式「教练规则写太宽」今天第 1 次**（08-16 已记 6 次，LESSONS §1.2e）|U · 待排序|0/2|`

</details>

## #0239 保持耐心、不去赌的病人更可能康复
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F15

**问题是什么**
U · 待排序　0/2

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：「Patients who stay patient（**怎么避免和前面重复**）」
正确：★ **最标准的解法：用 `Those who…` 顶掉重复的名词**<br>　✅ `**Those who** stay patient and avoid gambling stand a far better chance of getting well.`<br>　`those who` ＝ "那些…的人"，是议论文里替代 `people who / patients who` 的通用块，**同时省掉一个名词、避开重复**<br>★ 另两条路（都成立，按语境挑）：<br>　✅ 换动词：`Patients who **are willing to wait** and avoid gambling…`<br>　✅ 换名词：`Patients who **persevere** and avoid gambling…`<br>★ 顺带：`don't gamble` → `avoid gambling`（正式书面不用缩写，见 [[E-278]]）

★★ **2026-08-20 扩写（她当场点名要学，§2③；只是把适用范围说清，按 §3.5 A 连对连错不动）**
她的原话：「这个 those 用来代替 people，非指代的用法，老是想不起来」。
她说得准 —— 这里的 `those` **不回指前文任何东西**，它本身就等于 "the people"：
　`**Those who** want to join the training must sign up by Friday.`（＝ the people who…）
　`**Those** living in rural areas have fewer options.`（后面接分词，不必用 who）
　`**Those** on low incomes are hit hardest.`（后面接介词短语）
判据：`those` 后面**必须紧跟一个限定成分**（who 从句 / -ing / -ed / 介词短语），
　　　光一个 `those` 就是回指用法（"那些（前面提过的）东西"），两种别串。
为什么值得抢着用：一个词顶掉 `people who` 两个词，还避开跟前文重名 —— 议论文里最省的人称块。
同族两个：`**many of those who** …`（那些…的人里有不少）· `**those of us who** …`（我们当中…的人）
⚠️ 与 #0034（`the percentage of ___ total population`）里的 `that of` 不是一条：
　`that of / those of` 是**替代名词避免重复**（指代用法），本条是 `those who` **等于 people**（非指代）。
　问 2 不成立 —— 一个讲替代前文名词，一个讲这个词自带"人"的意思，要分两句讲。

**中文触发点**
**保持耐心、不去赌的病人更可能康复**

### 历史记录
- （从未被判定过）
- 2026-08-20 　D3 学习日 C2·组1 第 10 题　**顺带用对，不推进 streak**
  她写 `**Those who** want to join the training must sign up by Friday.` —— 一次到位。
  这是本条建号以来第一次出现在她的产出里，而且她同时说「老是想不起来」⇒
  说明这个块处在"低压能调出、她自己没把握"的位置。
  ⚠️ 不记 ✅：本题的主考点是 #0264（sign up），本条只是顺带用对。
  按本场口径（见当日 session 教练侧）：**复习组的顺带用对只列出、不推进 streak**，
  顺带用错才记 ❌。理由 —— 复习题是为主考点设的陷阱，顺带对上不构成压力下的证据；
  §4⑤d 的"高压 ✅ 扫描"只对作文开口，正是这个道理。
  ⇒ 下次要给本条单独出题，让它成为主考点，才能真正推进。
- 2026-08-22 ✅ D4 复习日 C2·组1 第 1 题　**首次作为主考点出题**
  题面「保持耐心、不去赌的病人更可能康复」，她写
  `**thoes who** keep patient and don't blindly gamble stand a far better chance of recovery`。
  `those who` 一次到位，没有回到 `patients who` ⇒ 考点命中，连对 1。
  `thoes` 是非词 ⇒ 按 §3.2 手滑豁免，不记。
  📋 顺带用对：限定从句**不加逗号**（＝ #0138 的考点，08-16 起就是靠加逗号错的，今天原样正确）·
  　`blindly gamble`（#0300 那族的 blind gambling）· `stand a chance of` 搭配准确。
  📋 更好：`stay patient`（keep ＋ 形容词是活的构式 keep calm / keep quiet / keep busy，
  　按 §0.8 造得出母语者句子 ⇒ 不判错，但 stay 是这个位上的默认）· `avoid blind gambling` 免掉缩写 don't（#0236）。
  ⚠️ 本条的中文触发点与 #0138 是**同一句**（#0138 ＝ 限定从句不加逗号，已 🎓）⇒
  　 收进 §8④ 积压①「一条题面挂两个考点」清单。
- 2026-08-23 ✅ D1 学习日 C3·组5 第 9 题　**连对 2 ⇒ 🎓 毕业**
  题面（零提示，换新场景）「病人之间的差别很大：沉得住气、不乱换方子的，恢复得明显更快。」，她写
  `patients vary widely: **those who** remain calm and stick to their treatment plan recover
  noticeably faster`。
  ★ 题面设计说明：中文第二个分句里**整个不出现"病人"**（"沉得住气…的"后面是空的）——
  　 前面已经说过 patients，英文再写一遍就是重复 ⇒ `those who` 成为最短也最自然的一条路。
  　 这是组3 修法的"结构留白"版本，与同组 #0281 是同一招。⇒ 命中，连对 2。
  ★ 这次是**非指代用法**（those ＝ the people），与 08-22 那次同一个机制，但换了句子结构
  　（那次 those who 在句首作主语，这次挂在冒号后面）⇒ 不是记忆复现。
  📋 顺带用对：`patients **vary** widely`（比我题面直译的"差别很大"更紧，**她的比我的好**）·
  　 限定从句**不加逗号** ✅（＝ #0138 的考点，与 08-22 一样正确）·
  　 `those who remain … **recover**` 复数谓语与 those 一致（R2 通过）。
  📋 `stick to their treatment plan` 送到了「不乱换方子」这一层（不判 #0126）。
  📋 更好：`Patients vary widely: those who **stay** calm and **do not keep switching treatments**
  　 recover noticeably faster.`
  　（stay 是这个位上的默认；do not keep switching 把中文的「**乱换**」那层动作感补回来）
<details><summary>原始行（旧表逐字，旧号 E-315）</summary>

`**保持耐心、不去赌的病人更可能康复**|「Patients who stay patient（**怎么避免和前面重复**）」|★ **最标准的解法：用 `Those who…` 顶掉重复的名词**<br>　✅ `**Those who** stay patient and avoid gambling stand a far better chance of getting well.`<br>　`those who` ＝ "那些…的人"，是议论文里替代 `people who / patients who` 的通用块，**同时省掉一个名词、避开重复**<br>★ 另两条路（都成立，按语境挑）：<br>　✅ 换动词：`Patients who **are willing to wait** and avoid gambling…`<br>　✅ 换名词：`Patients who **persevere** and avoid gambling…`<br>★ 顺带：`don't gamble` → `avoid gambling`（正式书面不用缩写，见 [[E-278]]）|U · 待排序|0/2|`

</details>

## #0267 fairly 一族：程度副词的强度刻度与语域
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F15
🔴 **2026-08-23 她推翻教练的 ❌，异议成立 ⇒ 改判 ◎✅**（详见历史记录里的 §4.7 更正块）
　 连带定下本条的**测量边界**：
```
本条其实是两半，只有一半能用中译英单点题测：
  ① 强度刻度（slightly ＜ somewhat ＜ fairly ＜ rather ＜ quite ＜ very ＜ considerably）
     ⇒ 可以测：中文的刻度对不对得上英文的刻度。08-22 `remarkably solid` 冲到顶端，判 ❌ 成立。
  ② 语域（a bit / pretty 是口语，作文不用）
     ⇒ ⛔ **中译英单点题测不了** —— 一个孤立的中文句子没有语域语境，
       `a bit heavy` 在这个句子里是完全正确的英语。**这一半只能挂作文验。**
⇒ 出题纪律：本条只出**刻度**题，且按 08-23 新规**直接把词写进题面**；语域那一半不出单点题。
```
**成员出题账**
```
📒 2026-08-23 她定的新纪律：出一次补一行
slightly       —— 未出过
somewhat       —— 2026-08-22 题面「稍微差了一些」⇒ ✅（她写 somewhat，弱档挑得准）
                  2026-08-23 题面「稍微大了一点」⇒ ◎✅（她写 a bit，正确英语，语域问题不在这测）
fairly         —— 未出过
rather         —— 2026-08-23 题面「相当难」⇒ ◎✅（她写 quite challenging，完全成立）
quite          —— 她默认就用这个，**而且在可分级形容词前它是对的**，不需要改
considerably   —— 未出过
remarkably     —— 2026-08-22 ⇒ ❌ 冲到刻度顶端（这次的 ❌ 站得住，不改判）
⇒ 下次直接把词写进题面：「★ 用 rather」「★ 用 somewhat」（她 08-23 定）
```

**问题是什么**
这一族词都翻成中文的"比较／挺／相当"，但**强度不同、语域不同**，作文里不能互换。
按强度从弱到强排（配形容词/副词）：

```
slightly      轻微地          最弱，只配可量化的差别    slightly higher · slightly more likely
somewhat      稍微／有几分    正式，学术写作的默认对冲   somewhat slower · somewhat different
fairly        比较／还算      中性偏弱，带一点"还行"的味  fairly common · fairly clear
rather        相当            比 fairly 强，常带负面色彩  rather expensive · rather disappointing
quite         相当／挺        英式歧义大，见下           quite common
pretty        挺              ⛔ 口语，作文不用          pretty good
very          很              强，但太素，能换更准的词就换
considerably  相当大幅度      只配比较级／变化量         considerably higher · rose considerably
```

**三条硬边**
```
① fairly 只配"好的一面"：fairly easy ✅ / fairly good ✅　　fairly difficult ⚠️ 别扭
   想说负面的"相当"用 rather：rather difficult ✅ rather slow ✅
② quite 在英式英语里有两个意思，作文里避开：
   quite ＋ **可分级**形容词 ＝ 相当（quite common ＝ 比较常见）
   quite ＋ **不可分级**形容词 ＝ 完全（quite impossible ＝ 根本不可能 · quite right ＝ 完全正确）
   ⇒ 想说"比较"就写 fairly / somewhat，别用 quite
③ 这一族**只修饰形容词和副词，不修饰动词**：
   ❌ `The number fairly increased`　✅ `The number increased **somewhat**` ／ `a **fairly** small increase`
```

**作文里怎么用**
```
T1 描述数据      slightly / somewhat / considerably（可量化）
T2 陈述立场      能删就删。写 `This is fairly important` 不如写 `This matters`
                 ★ 与 #0222 同向：对冲词会把 Task 2 的立场说软
T2 承认对方      somewhat 最好用：`This argument is somewhat convincing, but…`
```
⚠️ 与 #0108（副词能不能放 is 后面）不是一条：那条管**位置**，本条管**选哪一个**。
　 问 1 不成立 —— 一个是挪位置，一个是换词。
⚠️ 与 #0222（a bit 太口语／对冲词说软立场）相邻不合并：#0222 讲的是"要不要用对冲词"这个
　 篇章层决定，本条讲的是"决定要用之后，这一族里挑哪个"。要分两句话讲 ⇒ 问 2 不成立。

**怎么发现的**
2026-08-20　D3 学习日 C2·组2 第 1 题。她写 `is fairly common` 用得完全正确，
当场点名：「fairly 这个词新建条目，练习它的各种用法」（§2③）。

**我错在哪**
她这次没有错 —— `fairly common` 是这个词最标准的搭配之一。
建号理由是 §2③。她缺的是**这一族其余成员**：档案里从来没有她用过
somewhat / rather / considerably 的记录，说明她表示程度时只有 fairly 和 very 两档。

**中文触发点**
这项政策的效果比预期稍微差了一些。（"稍微…一些"用一个正式的程度副词，别用 a little）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）D3 学习日 C2·组2 第 1 题
  查重（§3.5 B0）：grep 了 `fairly` `quite` `rather` `程度副词` `对冲`，全档命中两处，逐条比对：
  · #0108「这个副词可以放 is 后面么」—— 管的是**位置**（方式/程度副词两处都行、频率副词必须放中间），
    改正动作是挪位置；本条是**在同义的一族里挑哪个**，改正动作是换词 ⇒ 问 1 不成立
  · #0222「a bit 是不是有点口语了」—— 管的是**要不要用对冲词**（T2 立场会被说软），是篇章层决定；
    本条管的是**决定用了之后挑哪个**，是词汇层 ⇒ 问 2 不成立，要分两句话讲
  两条都不是同一条 ⇒ 新建。建号时无对错，连对连错都是 0。
- 2026-08-20 ✅ 作文 T2-17　**高压 ✅**（建号当天就在作文里用对）
  全篇 10 个程度/方式副词**无一误用**：invariably · usually · sometimes · severely ·
  completely · certainly · genuinely · simply · ultimately · precisely。
  而且**一个 very 都没滥用**（只有 S3 的 `very real` 一处，是刻意强调）
  ⇒ 考点命中，连对 1。
  ⚠️ 唯一没做到的是"能删就删"那一层：`very real`（S3）在学术文里可以直接写 `real`。留痕不判错。
- 2026-08-22 ❌ D4 复习日 C2·组6 第 10 题
  题面「这份报告写得相当扎实，只是结论略显仓促。（★「相当」和「略显」各用一个正式的程度副词，别用 very / a little）」，
  她写 `the report is **remarkably** solid, though the conclusion feles **somewhat** rushed`。
  ★ **一半对一半错，错的那半正是本条的考点 —— 刻度**：
  ```
  ✅ 「略显」→ somewhat        位置正确（弱档），没有写 a little
  ❌ 「相当」→ **remarkably**   冲到了刻度顶端
     中文「相当」＝ 中等偏上 ⇒ fairly / quite / reasonably
     remarkably ＝ 惊人地、显著地 ⇒ 与 extremely / exceptionally 同档
  ```
  ⇒ 本条考的就是刻度，冲过头即失守 ⇒ ❌，连对 1 → 0。
  ★ 值得注意的方向性：她**弱档挑得准、强档冲过头**。
  　 与 08-20 那次「very real 该删没删」合看，形状一致 —— **她倾向于把语气往上加**。
  　 ⇒ 下次出题把两端同时摆上（一个"相当"一个"极其"），看她能不能拉开距离。
  📋 `feles` → `feels` 非词拼写，复习组豁免。
  📋 更好：`The report is **reasonably** solid, though **its** conclusion feels somewhat rushed.`
- 2026-08-23 ❌ D1 学习日 C3·组2 第 7 题　⚠️ **本条已于 2026-08-23 当天改判为 ◎✅，见下方更正块**
  题面「这门课相当难，而且作业量也稍微大了一点。（★ 两处用**两个不同**的程度副词：
  第一处是配**负面**形容词的那个"相当"；第二处是学术写作里默认的那个**对冲词**；
  ★ 两个词都只修饰形容词，不修饰动词）」
  她写 `this course is **quite** challenging, and workload is **a bit** heavy`。
  ```
  「相当难」（负面）→ 目标 **rather** difficult ／ rather challenging
                    她写 quite ⇒ 正是本条硬边② 要避开的那个词（英式歧义：
                    quite challenging 可以读成"相当难"也可以读成"完全够呛"）
  「稍微…一点」    → 目标 **somewhat**
                    她写 a bit ⇒ **口语词进书面**，正是本条正文里 pretty / a bit 那一格
                    ★ 08-22 同一个位置她写的是 `a little`，今天写 `a bit` —— **同一个成员连栽两次**
  ```
  ⇒ 两个成员都没落地 ⇒ ❌，连错 2。
  ★★ **这一题是她当场给出新纪律的直接触发点**，她的原话：
  　「**我觉得你废话那么多，不如直接点名你要什么词，把 skill 所有要隐藏题面
  　　或者说避免泄漏信息的都删掉。**」
  　 ⇒ 证据链完整：题面写了两行语义边界（"配负面形容词的那个"／"学术默认对冲词"），
  　 　 她仍然调不出 rather / somewhat —— **她缺的是这两个词本身，不是判据**。
  　 　 用语义描述去逼一个她根本没存进去的词，只能测出"她没有"，测不出任何新东西。
  　 ⇒ SKILL §6 与 §3.5 已按此改写：**要提示就直接写英文词**。
  ⚠️ 同句一处不属于本条：`**workload** is a bit heavy` —— 可数单数名词光着，
  　 应 `**the** workload` ⇒ 记 #0074 ❌。
  📋 最小修改：`This course is **rather** challenging, and **the** workload is **somewhat** heavy.`
  📋 更好：`This course is rather demanding, and the workload is somewhat heavier than usual.`
- 2026-08-23 ◎✅ D1 学习日 C3·组2 第 7 题　**她当场推翻教练的 ❌，异议成立**

  ### ★ 更正块（§4.7，2026-08-23 当天改判）
  **她的原话**：「**第 7 题就是，你就是说我除了 the 不太对，其他翻译的对不对**」
  **原判**：❌，理由是"目标词 rather / somewhat 都没落地"，记 连对 0 ／ 连错 2。
  **新判**：**◎✅（算对），连对 1 ／ 连错 0。**
  **判据哪里套宽了**：我又一次拿"没写出我想要的那个词"当判错的理由 ——
  　 而这正是她**同一天上午刚刚废掉**的做法（§3.2「判 ❌ 只有两个理由」）。
  　 犯规加重：新判据是我自己当天写进 SKILL 的，下午出题判分时没有执行。
  **逐条复核她那两个词**（按新判据的两条走）：
  ```
  `quite challenging`  中文「相当难」
    ① 句子本身有错吗？没有。`This course is quite challenging.` /
       `The exam was quite difficult.` / `It's quite hard to say.` —— 母语者句子造得出三个以上。
    ② 中文意思送到了吗？送到了。quite ＝ 相当，与「相当」精确对齐。
    ★ 而且本条硬边② 的那个歧义**在这里根本不适用**：
      quite 的歧义只发生在**不可分级形容词**前（quite impossible ＝ 完全不可能）；
      challenging 是**可分级**的 ⇒ `quite challenging` 只能读成"相当难"，零歧义。
    ⇒ 我拿一条不适用的硬边去判她，双重套宽。
  `a bit heavy`        中文「稍微大了一点」
    ① 句子本身有错吗？没有。`The workload is a bit heavy.` / `It's a bit expensive.` /
       `I'm a bit tired.` —— 造得出三个以上。
    ② 中文意思送到了吗？送到了，而且比 somewhat 更贴「一点」。
    ★ 它唯一的问题是**语域**（口语），而语域**在一个孤立的中译英句子里根本不存在**——
      没有上下文，就没有"这里该不该用口语"这回事。
    ⇒ **本条的语域那一半，中译英单点题测不了，只能挂作文验。**（已写进状态行下方的测量边界）
  ```
  ⇒ 判 ◎✅ 而不是 ✅：她的答案成立、也符合题面，但**刻度考点确实没被行使**
  　（题面没给词 ⇒ 是我的题面问题）⇒ 按 §3.2 算对 ＋ 当场改题面。
  ⇒ **改后的题面（下次用，直接给词）**：
  　 **这门课「相当」难，作业量也「稍微」大了一点。（★ 前一个"相当"用 rather；★ 后一个"稍微"用 somewhat）**
  ⚠️ 08-22 那次的 ❌ **不改判**：那次她写 `remarkably solid` 对应中文「相当」——
  　 remarkably 与 extremely 同档，**刻度冲过头 ⇒ 中文意思没送到** ⇒ 判据②成立，❌ 站得住。
  　 ⇒ 两次的差别正好划出本条的可测边界：**刻度错得判，语域错在这里不判。**
  **这个数住在哪几处**：本条状态行 ／ 成员出题账 ／ 本条历史（原 ❌ 那行留痕不删 ＋ 本更正块）／
  　sessions/2026-08-23.md 组2 的判定表、diff 表A、战报（三处已同步重算）。
  ⚠️ **同句 `workload` 缺冠词那一处仍然是错的**（#0074 ❌，与本条无关，不受本次改判影响）——
  　 这也正是她那句话的意思：「除了 the 不太对，其他翻译的对」。她自己划的边界是准的。

## #0320 频率副词的刻度：always ／ invariably ／ consistently ／ rarely ／ seldom
状态：🎓 ｜ 连对 2 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-23 ｜ 族 F15

**成员出题账**
```
① always        未单独出过（最通用，不必测）
② invariably    2026-08-22 组8 题面「这类项目几乎总是超预算」⇒ ✅
③ consistently  2026-08-23 组3 题面「他这两年的表现一贯很好」⇒ ✅
④ rarely        2026-08-23 组3 题面「出错的时候很少」⇒ ✅
⑤ seldom        未出过（倒装形状 `Seldom does…` 也没测过 ⇒ 挂作文验）
```

**问题是什么**
```
按频率从高到低（配形容词/动词，讲"多久发生一次"）：
always        总是                  最通用
invariably    ★ 无一例外地           **书面版的 always**，比 always 正式且更绝对
                                     `Risk is **invariably** accompanied by uncertainty.`
consistently  一贯地、稳定地         强调"每次都这样"，常配数据
                                     `Their results have **consistently** improved.`
frequently    经常                  正式版的 often
occasionally  偶尔                  （见 #0091）
rarely / seldom  很少               seldom 更正式；⚠️ 置句首要**倒装**：`**Seldom does** a policy…`
hardly ever   几乎从不              偏口语
```
**★ 位置规则（这一族和程度副词不一样）**
```
be 动词后      `Risk **is invariably** accompanied by…` ✅
实义动词前     `They **consistently** underestimate the cost.` ✅
助动词后       `has **always** been` ✅
⛔ 不能放句末：`~~accompanied by uncertainty invariably~~`
```
⚠️ 与 #0267（slightly / fairly / rather 那一族）分清：**那条管"多强"，本条管"多常"。**
　 反向验：fairly 用对 ≠ invariably 用对，两条可独立取值。
⚠️ 与 #0108（副词能不能放 is 后面）分清：那条管位置的**合法性**，本条管**选哪个词**。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
风险总是伴随着不确定性。（"总是"用一个比 always 更书面的词）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `invariably` `频率副词`，命中 #0108 的正文（讲频率副词必须放中间，是**位置**）与 #0267（**程度**副词刻度），两条问 2 都不成立 ⇒ 新建，双向交叉引用。
- 2026-08-22 ✅ D4 复习日 C2·组8 第 10 题　**建号后第一次被测**
  题面（**改写过** —— 存档那条「风险总是伴随着不确定性」正是 #0297 今天写错的那一句，会撞车）
  「这类项目几乎总是超预算。（★「总是」用一个比 always 更书面的词）」，她写
  `projects of this nature **invariably** exceed their budget`。
  挑对了刻度顶端那个书面词 ⇒ 命中，连对 1。
  ⚠️ 同句一处不属于本条：中文是「**几乎**总是」，invariably ＝ 无一例外，
  　「几乎」删掉之后从"允许例外"变成"绝对" ⇒ 记 #0126。正确：`**almost invariably**`。
  📋 顺带用对：`projects **of this nature**`（#0251 今天第四次）· `**exceed** their budget`（#0299）。
  ★ 与同组第 10 题的对照放在一起看：她**能挑到刻度顶端的词，但挑完之后不再回头看中文有没有留余地**。
  　 这与组 6 的 `remarkably solid`（往上冲）是同一个方向。
- 2026-08-23 ✅ D1 学习日 C3·组3 第 4 题　**连对 2 ⇒ 🎓**
  题面（**零提示**）「他这两年的表现一贯很好，出错的时候很少。」她写
  `his performance has been **consistently** good over the past two years, and he **rarely** makes mistakes`。
  ★ **一题两个成员，选词与位置全对**：
  ```
  选词  「一贯」＝ 每次都这样、稳定地 ⇒ **consistently**（不是 always，也没往 invariably 上冲）
        「很少」⇒ **rarely** ✅
  位置  `has been **consistently** good` —— be 动词后 ✅（本条位置规则第一行）
        `he **rarely** makes mistakes` —— 实义动词前 ✅（第二行）
        ⛔ 两处都没有掉到句末
  ```
  ⇒ 命中，连对 2。
  ★★ 与 08-22 那次对照：那次她挑对了刻度顶端的 invariably，却**没回头看中文的"几乎"**（记 #0126）；
  　 这次「一贯」和「很少」两个刻度都挑准了，而且中文里没有留余地的字要接 —— **刻度这一项现在是稳的**。

## #0321 very / really / extremely —— 学术写作里 very 通常删掉更有力
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-22 ｜ 族 F15

**问题是什么**
```
她这次写的：`The cost of risk **is very real**.`
更有力的：  `The cost of risk **is real**.`
```
**为什么删掉更有力**：`very` 不带任何新信息，它只是在给一个已经成立的判断"加音量"。
读者对 very 已经完全免疫；把它删掉，那个形容词反而站得更直。
```
处理办法三选一：
① 直接删            very real → real ｜ very important → important
② 换一个更强的形容词  very big → **substantial** ｜ very bad → **damaging**
                     very hard → **daunting** ｜ very good → **compelling**
③ 换一个有信息量的副词 very common → **increasingly** common ｜ very high → **disproportionately** high
```
**语域梯度**（口语 → 书面）：
```
really（⛔ 作文不用，见 #0234）＜ very（可用但最弱）＜ extremely / particularly（可用）
＜ 换掉形容词本身（最好）
```
⚠️ 例外：`very` 在 `the very first / this very reason / at the very least` 这类固定块里
　 意思是"正是那个"，**不是程度词，不能删**（见 #0318）。

**怎么发现的**
2026-08-20　作文 T2-17。她把这一处标了（新），并当场定「标记的都新建条目学习」（§2③）。

**我错在哪**
她这次**没有错**。建号理由是 §2③。缺口在于**这一族的其余成员和挑选判据**。

**中文触发点**
⛔ **挂作文验，不出单点题**（2026-08-24 定）—— 这是**语域**判断（学术写作里 very 通常删掉更有力），
孤立中文句里 `very` 不是错，§6 实证过（#0267 那条）。每篇判分时扫一遍全文的
very / really，逐个问"删掉会不会更有力"。
（08-23 组4、组5 两次都因「纯语域挂作文验」被弃 ⇒ 直接挂死，不再进复习池）

### 历史记录
- 2026-08-20 ③ 建号（她点名要学）作文 T2-17
  查重（§3.5 B0）：grep 了 `very` `really`，命中 #0234（really / right now 口语词进书面）—— 那条管的是**口语词不该进作文**（really 是错的），本条管的是 **very 虽然合法但删掉更好**（不是错，是可优化），问 1 不成立（一个换词、一个删词）⇒ 新建，与 #0234 交叉引用。
- 2026-08-22 ❌ D4 复习日 C2·组6 第 9 题（顺带）　**建号后第一次被测就原样复发**
  题面「代价是真实的。」—— **中文里根本没有"很"**，她写成 `the cost is **very** real`。
  ★★ 本条就是从她这一句建的号：08-20 作文 S3 `The cost of risk is **very** real`。
  　 今天题面把"很"拿掉了，她还是把 very 加了回去 ⇒ **不是理解问题，是习惯**。
  ⇒ 处理方向已定，但**先不动**：本条目前只有这一次记录，等它攒到两次以上再判要不要
  　 比照 #0322 转成 reminders.md 的 R 项（"会但压力下冒出来"那一类）。
  📋 与同组第 10 题合看：她 `remarkably solid` 也是往上加（#0267 ❌）。
  　 **同一天两处，方向一致：语气往上加。** 这比单看任何一条都有信息量。

---

# F17 T1 整句仿写

> 整句级改写

## #0241 这几张表说明纽约市及其五个区的人口在 1800–2000 的变化
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F17

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：The tables illustrate how the total population of NYC, as well as that of the five districts (…), changed over a two-century period from 1800 to 2000
正确：The tables **show** how the population of New York City **and of its five districts** changed **between 1800 and 2000**（T1 的 intro 只要改写题面；34 词太长，五个区名照抄占字数）

**中文触发点**
这几张表说明纽约市及其五个区的人口在 1800–2000 的变化

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-175）</summary>

`这几张表说明纽约市及其五个区的人口在 1800–2000 的变化|The tables illustrate how the total population of NYC, as well as that of the five districts (…), changed over a two-century period from 1800 to 2000|The tables **show** how the population of New York City **and of its five districts** changed **between 1800 and 2000**（T1 的 intro 只要改写题面；34 词太长，五个区名照抄占字数）|待排序|U（待定）|`

</details>

## #0242 一百年后曼哈顿人口见顶 185 万，占比降到 54%
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F17

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：A hundred years later, the number of people living in Manhattan reached a peak of 1,850,093, while the proportion shrank to 54%
正确：**A century later, Manhattan's population peaked at** 1,850,093, **though its share had fallen to** 54%（peak 作动词省掉整个名词块）

**中文触发点**
一百年后曼哈顿人口见顶 185 万，占比降到 54%

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-176）</summary>

`一百年后曼哈顿人口见顶 185 万，占比降到 54%|A hundred years later, the number of people living in Manhattan reached a peak of 1,850,093, while the proportion shrank to 54%|**A century later, Manhattan's population peaked at** 1,850,093, **though its share had fallen to** 54%（peak 作动词省掉整个名词块）|待排序|U（待定）|`

</details>

## #0243 此后下降，到期末只剩全市的 19%
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F17

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：From then on, the figure dropped, and the period ended with only 19% of people living in Manhattan
正确：**It then declined, ending the period at just 19% of the city's total**（it 回指避免重复；分词并句）

**中文触发点**
此后下降，到期末只剩全市的 19%

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-177）</summary>

`此后下降，到期末只剩全市的 19%|From then on, the figure dropped, and the period ended with only 19% of people living in Manhattan|**It then declined, ending the period at just 19% of the city's total**（it 回指避免重复；分词并句）|待排序|U（待定）|`

</details>

## #0244 上升势头持续，2000 年见顶 647 万，此时五分之四的纽约人住在曼哈顿以外
状态：在池 ｜ 连对 0 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 — ｜ 族 F17

**问题是什么**
待排序　U（待定）

**怎么发现的**
旧档案建号时未记来源

**我错在哪**
她的：…continued and reached a peak of 6,471,089 in 2000, which meant that the majority of people lived outside Manhattan
正确：The upward trend continued, **peaking at** 6,471,089 in 2000, **by which point four fifths of New Yorkers lived outside** Manhattan（用上 81% 这个数，比 the majority 具体）

**中文触发点**
上升势头持续，2000 年见顶 647 万，此时五分之四的纽约人住在曼哈顿以外

### 历史记录
- （从未被判定过）

<details><summary>原始行（旧表逐字，旧号 E-179）</summary>

`上升势头持续，2000 年见顶 647 万，此时五分之四的纽约人住在曼哈顿以外|…continued and reached a peak of 6,471,089 in 2000, which meant that the majority of people lived outside Manhattan|The upward trend continued, **peaking at** 6,471,089 in 2000, **by which point four fifths of New Yorkers lived outside** Manhattan（用上 81% 这个数，比 the majority 具体）|待排序|U（待定）|`

</details>

---

# F18 T2 整句仿写

> 整句级改写

## #0245 传统医学在某些情况下确实有点用
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F18

**问题是什么**
待排序　U（待定）

**怎么发现的**
2026-08-16　复习日 C1·组6

**我错在哪**
她的：Alternative medicines, **like a variety of** traditional medicines in different countries, **may be effective in some specific cases**
正确：Traditional medicines, **of the kind found in** many countries, **can genuinely help in certain cases**（genuinely help 比 be effective 有力；of the kind found in 比 like a variety of 紧）

**中文触发点**
传统医学在某些情况下确实有点用

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组6

<details><summary>原始行（旧表逐字，旧号 E-147）</summary>

`传统医学在某些情况下确实有点用|Alternative medicines, **like a variety of** traditional medicines in different countries, **may be effective in some specific cases**|Traditional medicines, **of the kind found in** many countries, **can genuinely help in certain cases**（genuinely help 比 be effective 有力；of the kind found in 比 like a variety of 紧）|待排序|U（待定）|0/2|`

</details>

## #0246 这些疗法不仅没用，还有实际危害
状态：在池 ｜ 连对 1 ｜ 连错 0 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F18

**问题是什么**
待排序　U（待定）

**怎么发现的**
2026-08-16　复习日 C1·组7

**我错在哪**
她的：this trend **can be harmful to patients —** alternative therapies can be **not only ineffective but also damaging**
正确：the trend **harms patients:** these therapies are **not only useless but actively damaging**（① 实义动词 harms 代替 can be harmful ② 冒号引出解释比破折号紧 ③ actively damaging 有力度）

**中文触发点**
这些疗法不仅没用，还有实际危害

### 历史记录
- 2026-08-16 ✅ 复习日 C1·组7

<details><summary>原始行（旧表逐字，旧号 E-149）</summary>

`这些疗法不仅没用，还有实际危害|this trend **can be harmful to patients —** alternative therapies can be **not only ineffective but also damaging**|the trend **harms patients:** these therapies are **not only useless but actively damaging**（① 实义动词 harms 代替 can be harmful ② 冒号引出解释比破折号紧 ③ actively damaging 有力度）|待排序|U（待定）|0/2|`

</details>

## #0247 尽管走投无路和别的压力把病人推向替代疗法
状态：在池 ｜ 连对 0 ｜ 连错 1 ｜ 毕业线 2 ｜ 上次 2026-08-16 ｜ 族 F18

**问题是什么**
待排序　U（待定）

**怎么发现的**
2026-08-16　复习日 C1·组7

**我错在哪**
她的：while **an urgent health problem and other reasons push patients to try** alternative medicines
正确：although **desperation and other pressures push patients towards** alternative medicines（① desperation 一个词说完"走投无路" ② push sb **towards** sth 比 push sb to try sth 紧）

**中文触发点**
尽管走投无路和别的压力把病人推向替代疗法

### 历史记录
- 2026-08-16 ❌ 复习日 C1·组7

<details><summary>原始行（旧表逐字，旧号 E-152）</summary>

`尽管走投无路和别的压力把病人推向替代疗法|while **an urgent health problem and other reasons push patients to try** alternative medicines|although **desperation and other pressures push patients towards** alternative medicines（① desperation 一个词说完"走投无路" ② push sb **towards** sth 比 push sb to try sth 紧）|待排序|U（待定）|0/2|`

</details>
