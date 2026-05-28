# Examples 生成进度追踪

> **流程**：one by one（不并行）。每题派 1 个 agent → 生成 P2 → check-static.py → LLM self-eval → 通过写入 examples/ → 更新本表 → 下一题。
> **顺序**：先 P2 全部（先新题 27 + 后老题 27），后 P3。
> **标准**：155-170 词 / 4 段 / Band 7 oral / persona 路由 / 死机机制。3 个 gold sample: p2_old_07 / p2_old_13 / p2_new_12。

---

## P2 新题（27 道）

| # | 题目 | persona | 状态 | 文件 |
|---|------|---------|------|------|
| 1 | 喜欢或不喜欢的高建筑 | 成都 IFS (S7) | ✅ | p2_new_01_tall_building.md |
| 2 | 有趣视频 | speaker 太空纪录片 | ✅ | p2_new_02_interesting_video.md |
| 3 | 去过的无聊地方 | wife 无聊小镇 | ✅ | p2_new_03_boring_place.md |
| 4 | 早起经历 | wife 晨跑 (S1/S8) | ✅ | p2_new_04_got_up_early.md |
| 5 | 喜欢在家/花园种菜的人 | 外公 种菜 (新配角) | ✅ | p2_new_05_plant_grower.md |
| 6 | 想颁布的新法律 | Object/hypo（wife 公务员）| ⬜ | — |
| 7 | 发小 | Person（zhangwei）| ⬜ | — |
| 8 | 想从事医疗行业的人 | Person | ⬜ | — |
| 9 | 拥有成功商业的人 | Person（zhangwei?）| ⬜ | — |
| 10 | 近期改变的计划 | Event/decision（speaker）| ⬜ | — |
| 11 | 在团队中工作 | Event（wife 团队）| ⬜ | — |
| **12** | **重要决定** | **speaker** | ✅ | p2_new_12_important_decision.md |
| 13 | 喜欢的现场体育赛事 | Event | ⬜ | — |
| 14 | 特别场合的食物 | Event（wife 烘焙）| ⬜ | — |
| 15 | 擅长学习和说语言的人 | Person | ⬜ | — |
| 16 | 遇到的科技问题 | Event | ⬜ | — |
| 17 | 名人出演的广告 | Event/Object | ⬜ | — |
| 18 | 推荐旅行过的地方 | Place（京都）| ⬜ | — |
| 19 | 喜欢拜访但不想住的家 | Place（京都）| ⬜ | — |
| 20 | 包含动物的故事或书 | Object | ⬜ | — |
| 21 | 别人帮助解决问题 | Event | ⬜ | — |
| 22 | 保护环境的法律 | Object/hypo（wife）| ⬜ | — |
| 23 | 很久没收到回复的信息 | Event | ⬜ | — |
| 24 | 长久目标/抱负 | Object/decision（speaker）| ⬜ | — |
| 25 | 遇到困难终成功的人 | Person（zhangwei/wife）| ⬜ | — |
| 26 | 改变重要想法 | Event/decision（speaker）| ⬜ | — |
| 27 | 想要颁布的环保法律 | Object/hypo（wife）| ⬜ | — |

## P2 老题（27 道）

| # | 题目 | persona | 状态 | 文件 |
|---|------|---------|------|------|
| 1 | 完美工作 | Event（wife 公务员）| ⬜ | — |
| 2 | 想见的名人 | Person | ⬜ | — |
| 3 | 禁用手机的场合 | Event | ⬜ | — |
| 4 | 给别人建议 | Event（wife）| ⬜ | — |
| 5 | 想拥有的科技产品 | Object | ⬜ | — |
| 6 | 擅长做计划的人 | Person（zhangwei S9c）| ⬜ | — |
| **7** | **喜欢画画的孩子** | **Muye** | ✅ | p2_old_07_child_drawing.md |
| 8 | App/程序 | Object | ⬜ | — |
| 9 | 微笑的场合 | Event（wife/Muye）| ⬜ | — |
| 10 | 为家人骄傲 | Person（wife/Muye）| ⬜ | — |
| 11 | 对家庭重要的东西 | Object | ⬜ | — |
| 12 | 自行车/摩托车/汽车旅行 | Event/Place | ⬜ | — |
| **13** | **机智解决问题的人** | **zhangwei** | ✅ | p2_old_13_smart_problem_solver.md |
| 14 | 朋友自学 | Person（zhangwei S9a）| ⬜ | — |
| 15 | 不享受的音乐活动 | Event | ⬜ | — |
| 16 | 近期看过且享受的电影 | Object | ⬜ | — |
| 17 | 有趣的建筑 | Place | ⬜ | — |
| 18 | 发挥想象力 | Event（Muye 乐高）| ⬜ | — |
| 19 | 乐于助人的人 | Person（wife）| ⬜ | — |
| 20 | 花费超过预期的物品 | Object/Event | ⬜ | — |
| 21 | 鼓励别人做不愿做的事 | Event（wife→speaker S8）| ⬜ | — |
| 22 | 想从事的短期海外工作 | Object/hypo（speaker）| ⬜ | — |
| 23 | 爱护自然之人 | Person | ⬜ | — |
| 24 | 商店 | Place | ⬜ | — |
| 25 | 去过且喜欢的城市 | Place（京都/成都）| ⬜ | — |
| 26 | 安静的地方 | Place（成都公园）| ⬜ | — |
| 27 | 喜欢的电视/网络节目 | Object | ⬜ | — |

---

## 进度统计

- **P2 完成**：8 / 54
- **P2 待生成**：46
- **P3 待生成**：54 题 × ~6 questions ≈ 324（P2 全部完成后）

---

## 状态图例

⬜ 未开始 / 🔄 生成中 / ✅ 通过入库 / ⚠️ revise 中
