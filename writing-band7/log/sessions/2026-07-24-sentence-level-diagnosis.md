# 2026-07-24 · 写作句子层诊断 + 实练（根因①②）

**形式**：不是写作文，是**对自己 7 月 17 篇实产做句子层解剖 + 单句重写 + 低压抽查**
**语料**：`writing-band7/gemini/corrections_2026-07.md`（Gemini 3 个对话，17 篇原文 = 199 句）
**产出**：`writing-band7/gemini/my_sentence_habits.md`（诊断全文，含第六节规则修订 + 第七节根因②证伪）

---

## 一、诊断（199 句逐句，忽略拼写）

| 指标 | 值 |
|---|---|
| 干净句 | 43/199 = **22%** |
| 短句(<15词)干净率 | 35% → **"写短句"这个药方无效** |
| Gemini 18 次评分 | TR/CC 7.0–7.5 ｜ LR/GRA 6.0–6.5 |
| 时态错误 | **仅 3 句** → 时态是强项，停练 |

**缺陷频次前五**：动词框架 ~75 · 冠词 ~55 · 中文块直译 ~45 · 单复数/一致 ~30 · 词性 ~28

---

## 二、12 句实练（她全程自己改，我只判）

| # | 原句 | 她的产出 | 判 / 补 |
|---|---|---|---|
| 1 | the leaving school time of students is usually before 5pm | （示范） | students usually leave school before 5 pm |
| 2 | rescues for skyscraper are extreme difficult | it is extremely difficult for local governments to rescue residents from skyscrapers | ✅ 找到笼中动词+补施动者。教**三档梯子**：名词→不定式/动名词→谓语 |
| 3 | the maintenance is impossible for governments | governments cannot maintain the facilities if water is free | ✅ 直接到档 2。补：impossible→unaffordable；条件句应虚拟 `If water were...would be` |
| 4 | living in the countrysides means more free and relaxing | living in the countryside offers people more freedom and a relaxing life | ✅ 一次修 3 类（means→offers / adj→n / countrysides→countryside）。补并列同档 + a more relaxed pace of life |
| 5 | before a drop for the next 40 years | 提议 before a drop to xx | ⚠️ 方向对但**介词后默认 -ing**：before dropping to X over... 教：名词化会丢"体" |
| 6 | an aging population means significant burden and overload on society | an aging population puts a significant burden on society | ✅ 4 处一次修完（含主谓一致 -s 自己加的）。升级 impose（她自己写过） |
| 7 | with the percentage of change compared with previous month being over 4% | with the monthly increase being over 4% | ✅ 8 词压成 3 词。补：**being 是 be 的马甲** → with monthly gains exceeding 4% |
| 8 | the number of high income becoming more | the number of high-income households becomes more? | ✅ 半（补了中心词）。`more` 是限定词不是形容词 → more high-income households / rose slightly |
| 9 | the requirement for professionals working in the country where they are trained is just for reward | Professionals should work locally to return the investment by governments | ✅ 20→10 词。补：repay（不是 return）+ **让步段必须带归属标记 many people argue that** |
| 10 | securing them having right to choose where they work is more important | protecting individual freedom is more important | ✅ 9→3 词。她自问"还是 is"→ 给**刹车规则** |
| 11 | the process of how global fashion imposes a influence is... | exerts | ✅ impose(强加/负面) vs exert(中性) |
| 12 | while it is a possible way ... to build high-rises | building high-rises is a possible way to provide more homes in big cities | ✅ 补后半 worth considering |

**不用提示自己修掉的**：countrysides→countryside · population put→puts · burden→a burden · 补中心词 households · Professionals 零冠词复数 · means→offers 并转词性 · **两次直接跳档 2**

---

## 三、24 次低压抽查（本次最重要的发现）

| 轮 | 内容 | 得分 |
|---|---|---|
| 1 | 框架 devote/disagree/compete/help/require/suffer/range/worth | 6/8 |
| 2 | 框架 attend/reach/level off/wait/exert/prefer/spend/expect | 7/8 |
| 3 | 冠词（8 个取自原文的名词短语） | 7/8 |
| | | **20/24 = 83%** |

**同样这 24 个点在 cold 作文里 0%。**

→ **根因②"词条只存意思没存用法包"被证伪**。不是知识缺口，是检索失败，与根因①同源（13 词主语吃光带宽 → 框架冠词第一批被挤掉）。

### 真缺口全清单（只有 5 条要背）
```
require sb TO DO sth · have THE right to do sth · worth+doing ≠ worthy OF+n
prefer A TO B（名/动名）≠ prefer to do A RATHER THAN do B · burn itself OUT
```

---

## 四、本次教的规则（她可直接用）

```
下笔 6 问：
1 真正的动作是什么、谁做的  → 让它当谓语
2 主语几词？≤5 → is 合法收手 ; >8 且谓语是 be → 拆
3 写了 the+抽象名词？兑现得了吗(of… 或上文提过)？不能就删 the
4 见 and/or/than/rather than → 左右同词类同范畴同主语
5 介词(before/after/by/without)后 → -ing
6 这坨内容前面说过吗？说过→this+一个词 ; 没说过→拆主谓宾

be 的马甲：is/are/was/were/being/to be/there is
名词化不许占谓语位（主语可以，宾语更可以，动词槽必须满）
考场：默认档 1，只在论点句/结论句推档 2
让步段结论句必须带归属标记（many people argue that / From this perspective）
```

**自我分诊法**：出错后先单独问自己 → 答得出=检索失败(不背，加检查触发) ; 答不出=真缺口(记下)

---

## 五、下次

- 根因③（并列同形，~10 句）还没过——量最小，可快速收掉
- **验证预测**：cold 写一个 T2 body 段，先写短主语骨架再补细节，数框架/冠词错误率，与 7 月基线对比
- "写一句扫一眼"的扫描内容改为：① 主动词框架对吗 ② 主名词冠词对吗
