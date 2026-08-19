# skill 模拟评估（实验名，后续用此名重新发起）

目的：在隔离环境里检验 `SKILL_v3.md` 的质量 —— 三个 opus agent 连续模拟 4 天（D1 D2 D3 + 付息日），
不准跳跃，看 skill 在真实执行压力下哪里断。**她确认之前不修改 skill。**

## 角色
- **A（教练）**：唯一依据 = `SKILL_v3.md`。出题、判定、记录、反馈，全按 skill 来。⛔ 不许读 `private-b/`。
- **B（模拟 suzy）**：按 `private-b/playbook.md` 答题、植错、质疑、问问题。A 不知道剧本存在。
- **C（审计）**：每天结束后，对照 skill 逐条核 A 的所有产出与文件；读 playbook 核 A 的捕获率
  （漏了几个植入错、有没有假错、假错测试那句有没有被误判）。产出 `audit/dayN.md`。
  发现【重点问题】（skill 结构性缺陷/A 无法执行的条款）→ 立即上报主线，实验可中停。

## 环境
```
SKILL_v3.md            被测 skill（v3 整合稿定稿）
data/                  A 的工作区：problems.md(空启动) · log.md · bank.md · scoring.md ·
                       anchors.md · pick_question.py · sessions/
legacy/drill/          现有真实数据整理迁入（只读参考，模拟不写它）
private-b/playbook.md  B 剧本（A 禁读）
audit/                 C 的逐日审计报告
```

## 模拟适配（环境限制，C 不据此扣 A 的分）
1. skill 里的"节点 LLM 评审"在模拟中降级为 A 的**书面自查**（逐项写出检查结果）——subagent 不能再生 subagent。
2. 时间不真实流逝：模拟日期 2026-08-19 ~ 08-22；作文"限时 40min"只作标注。
3. daily_log.md / study_hub.md 两处收尾写到 `data/` 内的同名文件，不碰真实文件。

## 真实数据迁移状态
- 现有 drill/ 已全量复制进 legacy/（2026-08-18）。
- 生产环境的新文件夹 + 全库按新格式重编号迁移：**等她确认 skill 后再做**（她定的顺序）。
