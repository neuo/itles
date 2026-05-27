# Speaking Band 7 — 入口 + 导航

> **2026-05-27 重起炉灶**——参考 [[writing/t2-band7/]] 同款架构，把 P2/P3 训练系统化（错误追踪 + Phrase 积累 + sessions + 毕业 path）。
>
> 旧材料（v7 手册 / v6 模板 / p2_my_path.md）**降级为参考库**，不再作为训练主线。

---

## 现状 snapshot

| 维度 | 状态 |
|------|------|
| **当前评分预估** | Band 5.5-6（P2 死机风险 + P3 cold production 卡顿）|
| **目标** | Band 6.5-7（首考 6/20，二考 7 月）|
| **核心瓶颈** | 主动输出 gap（input >> output）+ P2 60 秒思考时间认知爆掉 |
| **训练时长** | 4 周（5/28 → 6/19），每天 20-30 min |

---

## 文档导航

| # | 文件 | 用途 | 长度 |
|---|------|------|------|
| 1 | **01_my_situation.md** | P2/P3 现状诊断 + 输出 gap | 短 |
| 2 | **02_band7_target.md** | Band 7 评分细则（FC+LR+GRA+PRO）+ 14 项自查清单 | 长 |
| 3 | **03_question_types.md** | P2 4 类（人/地/事/物）+ P3 5 类（compare/cause/agree/hypothetical/predict）骨架 | 长 |
| 4 | **04_toolkit.md** | 衔接词 / 起手 / 过渡 / 收尾 / opener / 升级词 / 复杂句 | 长 |
| 5 | **05_path.md** | 4 周训练路径（W1 高 → W2 中 → W3 低脚手架 → W4 模考）| 长 |
| — | **personas.md** | 8 个 S 存货详细库（wife / Muye / 京都 / 成都 / 一起健身）| 中 |
| — | **question-bank-raw.md** | 2026 5-8 月 大陆题库原文（P1 38 题 + P2 54 题）| 长 |

---

## 训练机制（mirror T2）

```
examples/        ← Band 7 标杆答案（通过 orchestrator 验证才入库）
log/sessions/    ← 每次练习记录
log/error_trace  ← 实时错误流水
log/errors.md    ← 错误模式归类 + 毕业追踪（S2-X 系列）
log/active_phrases.md ← Phrase 池 + D+ 复检
tools/           ← orchestrator（静态检查 + LLM 检查 联合）
```

**错误命名**：T2 用 W2-X 系列，Speaking 用 **S2-X 系列**（避免混淆）。

**关键差异 vs T2**：
- 评分维度：FC + LR + GRA + **PRO**（替代 TR）
- 自检方式：**录音回听**（替代倒读）
- 训练单位：**P2 = 2 min 独白 ~ T2 = 250 词 essay**；**P3 = 30-45 秒/题 ~ T2 句子级**
- v1→v2 模式：v1 cold + v2 reformulated（不是重写，是 reformulation drill）

---

## 关联文件

- [[t2-band7/]] — 写作 Band 7 系统（已成熟）
- [[CLAUDE.md]] — 项目主旨
- 旧材料（仅参考）：
    - `speaking/ielts_p2p3_备考手册v7.md`（56 题完整范文，**水平 OK 但结构散乱**）
    - `speaking/ielts_p2p3_泛化模板体系v6.md`（5 种题型骨架）
    - `speaking/p2_my_path.md`（死机急救——核心思路融入 05_path）
    - `speaking/coach/`（旧 error_log + inventory + sessions——4/27 + 4/29 历史保留）
