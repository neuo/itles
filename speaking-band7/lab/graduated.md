# 已毕业档 · graduated.md

> **🎓 条目的归宿**（2026-08-29 从写作线移植的机制）。
>
> ```
> 毕业当天：教练**只在 problems.md 原地把状态行改成 🎓 已毕业 YYYY-MM-DD**，
>           条目和全部日志行一个字不动、不搬家。
> 搬家：    **她手动做**（把整条从 problems.md 剪到本文件）。
>           ⛔ 教练不搬文件、不建清单、不留墓碑行 —— 她 2026-08-19 驳回过一次，规矩没变。
> 脚本口径：lab.py 把 problems.md ＋ graduated.md **当成一个档案**读，
>           所以搬不搬都不影响 stats / pick / dedup / check 的任何一个数。
>           `lab.py stats` 会报「其中 N 条仍在 problems.md，待她手动搬」。
> 回潮：    已搬进本文件的条目再犯 ⇒ **先把整条搬回 problems.md**，再改状态行、记日志。
>           ⛔ `lab.py append` 拒绝往 graduated.md 里写判定行。
> ```
>
> 格式与 problems.md 完全一致（§3.1 机器契约），`lab.py check` 两个文件一起查。

---
