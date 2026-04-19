# 数字串听写专项训练

> **背景**：S1 数字题反复丢分，且不是听不懂数字本身，是 **4-5 位数字串的短时记忆容量不够**。听到第 8 位时前面的开始模糊，导致位置混淆（9785 → 9685 / 9875 两次错位置不同）。
>
> **目标**：通过每日 5 分钟专项训练，把数字串短时记忆从 4 位扩到 7 位（IELTS 电话号码长度），把常见易混数字（teens vs tens, 7/9, 6/7）的识别从"想一下"压缩到"瞬间反应"。

---

## 训练时长 & 频率

- **每天 5 分钟**（独立于其他听力任务）
- **持续 14 天**为一个完整周期
- 第 7 天和第 14 天对照分数看趋势

---

## 训练流程（每天 5 分钟）

**4/18 起已集成到练习 app**：打开 http://localhost:3456 → 数字听写 Tab → 按今日配比 → 自动播放 + 判分 + 统计

手动版（仅在 app 不可用时用）：
1. **听写 5 句**（每句听 2 遍，第 2 遍间隔 3 秒）— 2 分钟
2. **对照原文，标错位**（哪一位错、错成什么）— 2 分钟
3. **重听错的 1-2 句，跟读数字部分** — 1 分钟

记录：app 会自动存 `sessionStats` 和 `sentenceStats`；下面的训练日志表手动填正确率+错位类型即可。

---

## 易混数字快速识别（训练前必看 30 秒）

### 1. Teens vs Tens（最高频陷阱）

| Teens（重音在后） | Tens（重音在前） |
|------------------|----------------|
| thir**TEEN** /θɜːrˈtiːn/ | **THIR**ty /ˈθɜːrti/ |
| four**TEEN** /fɔːrˈtiːn/ | **FOR**ty /ˈfɔːrti/ |
| fif**TEEN** /fɪfˈtiːn/ | **FIF**ty /ˈfɪfti/ |
| six**TEEN** /sɪksˈtiːn/ | **SIX**ty /ˈsɪksti/ |
| seven**TEEN** /ˌsɛvənˈtiːn/ | **SEV**enty /ˈsɛvənti/ |

**辨别法**：重音在哪个音节 → 确定是 teen 还是 ty。

### 2. 7 vs 9 vs 6（个位数易混）

| 数字 | 发音 | 关键特征 |
|------|------|----------|
| six | /sɪks/ | 短促，结尾 /ks/ |
| seven | /ˈsɛvən/ | 两个音节，/v/ 音 |
| nine | /naɪn/ | 长元音 /aɪ/ |

**注意**：你两次错都涉及 7（一次 7→6，一次 7和8对调）。听到 /ˈsɛvən/ 时立即标记，不要含糊。

### 3. 价格表达

| 写法 | 读法 |
|------|------|
| £1.50 | "one pound fifty" / "one fifty" |
| £2.95 | "two ninety-five" / "two pounds ninety-five" |
| 5p | "five p" /piː/（pence 缩写）|
| £125 | "one hundred and twenty-five" / "a hundred and twenty-five" |

### 4. 时间表达（英式）

| 写法 | 读法 |
|------|------|
| 9:30 | "nine thirty" / "half past nine" |
| 9:15 | "nine fifteen" / "quarter past nine" |
| 8:45 | "eight forty-five" / "quarter to nine" |
| 9-9:30 | "between nine and half past" |

---

## 训练材料库（21 句，分 3 级难度）

### L1 — 4 位数字（年份/编号/PIN）

来源：C14T1S1, C14T2S1 等已精听过的 S1

1. **C14T1S1** "September the tenth, 1992" → 1992
2. **C14T2S1** "Oh, I actually have 1991, I'll just correct that now" → 1991
3. **C5T2S1** "It's £125 per year" → 125
4. **C5T3S1** "a 1.4 should do" → 1.4（小数）
5. **C5T2S1** "5p a sheet for both A4 and A3" → 5 / A4 / A3
6. **C5T4S1** "I'd go up to a hundred" → 100
7. **C14T1S1** "So that was September the tenth" → 10

### L2 — 7 位电话号码 / 邮编（含 chunk 节奏）

来源：C5-C18 各 S1 第一段（personal information 段）

8. **C14T2S1 句10**: "It's 219 442 9785" → 21944**29785**
9. **C5T3S1**: 拨号码（详见 transcript） → 待补
10. **C16T1S1**: 邮编/编号 → 待补
11. **C17T1S1**: 联系电话 → 待补
12. **C18T1S1**: 紧急联系 → 待补

> ⚠️ L2 是核心难度。每天必练 1-2 句。听写时把 7 位拆成 3-3-1 或 3-4 chunks，每 chunk 之间有微停顿。

### L3 — 价格 / 时间范围 / 多数字陷阱句

来源：C5T2S1 / C5T3S1 / C5T4S1 / C14T2S1（数字密集句）

13. **C5T2S1 句24**: "the earliest you can book is forty-eight hours" → 48
14. **C5T2S1**: "The minimum fine is £1.50" → £1.50
15. **C5T4S1 句21**: "I'm planning on staying a year" → 1 year
16. **C5T4S1 句46**: "I'd go up to a hundred" / "£60-80 ... a hundred" → 60/80/100
17. **C5T4S1**: "between 9 and half past" → 9:00-9:30
18. **C14T2S1 句25**: "it's three weeks since I first noticed it" → 3 weeks
19. **C5T2S1 句26**: 5p a sheet 段（A4 and A3 / black and white）→ 数字密集段
20. **C5T3S1**: "1.2 / 1.4 / 1.6" 连续小数段 → 区分相邻小数
21. **C14T2S1 句37**: "running a few times a week, maybe three or four times" → 3 or 4

---

## 每日选题建议

| 周次进度 | 每日 5 句配比 |
|---------|--------------|
| Day 1-3 | L1×3 + L2×1 + L3×1 |
| Day 4-7 | L1×2 + L2×2 + L3×1 |
| Day 8-11 | L1×1 + L2×2 + L3×2 |
| Day 12-14 | L1×1 + L2×1 + L3×3 |

每天随机抽，不要按顺序。录音工具：把 transcripts 里相关句子用任意 TTS（如 ElevenLabs/Mac say 命令）生成音频，或直接用真题音频定位到对应秒数。

**Mac 终端 TTS 示例**：
```bash
say -v Samantha "It's 219 442 9785"
say -v Daniel "The minimum fine is one pound fifty"
```
（Daniel 是英式发音，Samantha 是美式）

---

## 训练日志

| 日期 | Day | 5句正确率 | 错位类型 | 备注 |
|------|-----|----------|---------|------|
| 4/17 | 1 | /5 | | 手动版启动 |
| 4/18 | 2 | /5 | | 切换到 app 版 |
| 4/19 | 3 | /5 | | |
| 4/20 | 4 | /5 | | |
| 4/21 | 5 | /5 | | |
| 4/22 | 6 | /5 | | |
| 4/23 | 7 | /5 | **第一周中检** | |
| 4/24 | 8 | /5 | | |
| 4/25 | 9 | /5 | | |
| 4/26 | 10 | /5 | | |
| 4/27 | 11 | /5 | | |
| 4/28 | 12 | /5 | | |
| 4/29 | 13 | /5 | | |
| 4/30 | 14 | /5 | **毕业测试** | |

**错位类型代号**：
- `D` = 单数字混淆（7→6 等）
- `S` = 顺序错位（9785→9875）
- `T` = teens vs tens 混淆（13/30）
- `M` = 漏一位
- `E` = 多一位
- `F` = 完全错（重听都听不出）

---

## 毕业标准（Day 14）

- L1 全对（4 位数字稳定）
- L2 至少 3/5 对（7 位电话进步明显）
- L3 至少 3/5 对（价格/时间复杂句能抓核心）

如果毕业失败 → 进入 phase 2（材料升级到 C13-C18 难度更大的 S1）

---

## 训练之外的辅助

1. **做 S1 套题时**，听到数字立即在草稿纸上写，不等句子结束（习惯性 trigger）
2. **app「精听卡点词」分类** 增加 "数字" 子分类（待开发）
3. 看英文 YouTube 时遇到电话号码/价格，暂停跟读一遍
