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
| 6 | 想颁布的新法律 | speaker 提议+wife 灵感 | ✅ | p2_new_06_new_law.md |
| 7 | 发小 | 童年邻居 Liang (新配角) | ✅ | p2_new_07_childhood_friend.md |
| 8 | 想从事医疗行业的人 | 表妹 Lin (新配角) | ✅ | p2_new_08_medical_career.md |
| 9 | 拥有成功商业的人 | 前同事 Chen 咖啡馆 (新配角) | ✅ | p2_new_09_successful_business.md |
| 10 | 近期改变的计划 | speaker 京都行取消 | ✅ | p2_new_10_changed_plan.md |
| 11 | 在团队中工作 | speaker 工作团队 | ✅ | p2_new_11_group_work.md |
| **12** | **重要决定** | **speaker** | ✅ | p2_new_12_important_decision.md |
| 13 | 喜欢的现场体育赛事 | zhangwei CBA 球赛 | ✅ | p2_new_13_sports_event.md |
| 14 | 特别场合的食物 | wife 生日蛋糕 (S2) | ✅ | p2_new_14_special_food.md |
| 15 | 擅长学习和说语言的人 | **wife 语言（复用，原 Lena 弃）** | ✅ | p2_new_15_language_learner.md |
| 16 | 遇到的科技问题 | speaker 笔记本崩溃 | ✅ | p2_new_16_tech_problem.md |
| 17 | 名人出演的广告 | speaker 刘翔广告 | ✅ | p2_new_17_celebrity_ad.md |
| 18 | 推荐旅行过的地方 | 京都 (S6) | ✅ | p2_new_18_recommend_place.md |
| 19 | 喜欢拜访但不想住的家 | 外公老家 (复用) | ✅ | p2_new_19_visit_not_live.md |
| 20 | 包含动物的故事或书 | Muye 动物绘本 (复用) | ✅ | p2_new_20_animal_book.md |
| 21 | 别人帮助解决问题 | zhangwei 帮修网络 (复用) | ✅ | p2_new_21_helped_solve_problem.md |
| 22 | 保护环境的法律 | wife 垃圾分类法 (复用) | ✅ | p2_new_22_environmental_law.md |
| 23 | 很久没收到回复的信息 | Liang 重联系 (复用) | ✅ | p2_new_23_no_reply_message.md |
| 24 | 长久目标/抱负 | speaker 独立研究梦 | ✅ | p2_new_24_long_term_goal.md |
| 25 | 遇到困难终成功的人 | zhangwei 自学 ML (S9a 复用) | ✅ | p2_new_25_overcame_difficulty.md |
| 26 | 改变重要想法 | speaker 育儿观+Muye (复用) | ✅ | p2_new_26_changed_opinion.md |
| 27 | 想要颁布的环保法律 | speaker+wife 限塑令 (复用) | ✅ | p2_new_27_env_law_introduce.md |

## P2 老题（27 道）

| # | 题目 | persona | 状态 | 文件 |
|---|------|---------|------|------|
| 1 | 完美工作 | speaker 灵活自主工作 | ✅ | p2_old_01_perfect_job.md |
| 2 | 想见的名人 | speaker Nolan (复用 sci-fi) | ✅ | p2_old_02_famous_person.md |
| 3 | 禁用手机的场合 | 京都寺庙 (S6 复用) | ✅ | p2_old_03_phone_not_allowed.md |
| 4 | 给别人建议 | wife 工作压力 (S3) | ✅ | p2_old_04_gave_advice.md |
| 5 | 想拥有的科技产品 | 相机拍 Muye (speaker 爱好) | ✅ | p2_old_05_tech_to_own.md |
| 6 | 擅长做计划的人 | zhangwei Notion (S9c) | ✅ | p2_old_06_good_planner.md |
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

- **P2 完成**：35 / 54（新题 27/27 + 老题 1,2,3,4,5,6,7,13）
- **P2 待生成**：19（老题 8-12, 14-27）
- **P3 待生成**：54 题 × ~6 questions ≈ 324（P2 全部完成后）

---

## 状态图例

⬜ 未开始 / 🔄 生成中 / ✅ 通过入库 / ⚠️ revise 中
