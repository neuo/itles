# lab/ · 口语训练数据目录

> **方法唯一真源 ＝ `.claude/skills/fluency-lab/SKILL.md`。**
>
> ⚠️ **本文 ⛔ 不复述任何方法内容** —— 没有周期、没有流程、没有档位、没有条数。
> 两份方法文档 ＝ 两份真源，那正是 v1 审计里最常触发的失败形状。
>
> 2026-09-05 实证：本文上一版把方法抄了一遍，于是整份停在了已经作废的机制上 ——
> D-1/D-3、付息日 a/b 段、📖 四档、连对 3 毕业、「不许连续两个付息日没被测到」、
> 「253 条」（当时真值 303）。**每一条都是被明令废掉的**，而没有任何闸会发现它过期。
> ⇒ 这一版只留【文件是什么】和【数从哪来】，两样都不会随方法变动而过期。

## 文件

```
problems.md    在池条目（未毕业）—— 编号 · 题面 · 状态行 · 日志行
graduated.md   已毕业条目（🎓）—— 格式与 problems.md 完全一致
               ★ 两个文件被脚本当**一个档案**读；搬家由 `lab.py migrate` 做，教练不手搬
methods.md     方法类（操作/方法论）—— ⛔ 不进复习召回，只在诊断里当判据
redo_queue.md  重答队列
cycles.md      每个付息日的合并记录 ＋ 周期小结
sessions/      一天一文件 YYYY-MM-DD.md
drawn.log      出题流水，`lab.py` 自动 append —— ⛔ 禁手工编辑
lab.py         机械工具（唯一入口，子命令见下）
tests/         回归测试台 —— ⛔ 只跑临时副本、不碰真档案
fix_format.py  一次性格式整改（可重跑、幂等）
```

## 任何一个数都从脚本拿

```
python3 speaking-band7/lab/lab.py stats            全档统计 ＋ 召回队列
python3 speaking-band7/lab/lab.py count            按类型数条目（不带 --type 打全表）
```

⛔ **禁用 grep 数条目。** grep 数的是"字符串出现了几次"，脚本数的是"符合口径的条目有几条"。
实证 2026-09-04：`grep -c "^状态.*🎓"` 报 291（真值 290）；据此算出的未毕业报 29（真值 13，**大了 2.2 倍**）。

## 子命令一览（口径与用法一律看 SKILL）

```
pick  used  ｜  list  show  dedup  prompts  ｜  append  migrate  ｜  stats  count  check  deliver  lookback
```

⚠️ 只有 `append` 和 `migrate` 会写内容文件，且都**只碰位置与算术**，⛔ 不产生任何一个字。

## 历史

- 2026-08-18　v2 起用本目录（旧真源 `coach/fluency_lab.md` 转为只读归档）
- 2026-08-29　从写作线移植 `lab.py`；全档格式整改到 `check` ERROR 0
- 2026-09-04　`migrate` 上线，🎓 条目搬进 `graduated.md`
- 2026-09-05　召回梯子上线（毕业条目重新进召回）；本文改成纯指针
