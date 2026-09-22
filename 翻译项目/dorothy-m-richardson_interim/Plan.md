# 翻译计划（过渡 / Interim）

## 本计划信息

- **项目名称**：《过渡》（多萝西·米勒·理查森）/ Interim (Dorothy M. Richardson)
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本作品判定为中篇 → 连续模式，由主 agent 在自身上下文内逐章执行 9 步；单批受上下文限制时可分批续译。

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 第一章（I） | chapter-1.md | 58.7KB | todo |
| 2 | 第二章（II） | chapter-2.md | 34.8KB | todo |
| 3 | 第三章（III） | chapter-3.md | 18.6KB | todo |
| 4 | 第四章（IV） | chapter-4.md | 43.8KB | todo |
| 5 | 第五章（V） | chapter-5.md | 17.5KB | todo |
| 6 | 第六章（VI） | chapter-6.md | 45.5KB | todo |
| 7 | 第七章（VII） | chapter-7.md | 9.4KB | todo |
| 8 | 第八章（VIII） | chapter-8.md | 53.6KB | todo |
| 9 | 第九章（IX） | chapter-9.md | 32.1KB | todo |
| 10 | 第十章（X） | chapter-10.md | 15.9KB | todo |
| 11 | 第十一章（XI） | chapter-11.md | 1.8KB | todo |

合计 11 章，约 331.6KB / 5.6 万英文词。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-08 | chapter-1.md | done | 11 块 / 17 段，check 退出码 0；新定名：昂温家（the Unwins）、米斯特·贝尔（Meester Bell）、萨摩瓷器（Satsuma）、乔治叔叔（Uncle George）、黛西（Daisy，玩偶）、斯特鲁德威克（Strudwick's）、麦秆凉帽（leghorn hats） |
| 2026-09-08 | chapter-2.md | done | 6 块 / 9 段，check 退出码 0；新定名：《皮科拉》（Piccola）、《山中之王》（Le Roi des Montagnes）、萨拉托加衣箱（Saratoga trunk）、马德拉斯细纱（Madras muslin）、乌得勒支天鹅绒（Utrecht velvet）、螺形腿靠墙小桌（console table）、黑木小橱（chiffonier）、什物架（whatnots）、阿尔玛（Alma） |
| 2026-09-08 | chapter-3.md | done | 5 块 / 16 段，check 退出码 0；新定名：世界都会（Cosmopolis）、贝尔纳·门迪萨尔（Bernard Mendizabal）、门迪萨布尔（Mendizabble 误读括注）、波莉·贝利（Polly Bailey）、海德公园（Hyde Park）、阿姆斯特丹（Amsterdam）、埃米尔（Emile，男仆）、救世军乐队 |
| 2026-09-08 | chapter-4.md | done | 8 块 / 14 段，check 退出码 0；新定名：女王大厅管弦乐团、安托万·鲍登（Antoine Bowdoin）、《特里尔比》（Trilby）、女帮办（lady-help）、格林家（the Greens）、威尔特郡、勒罗伊夫人（Madame Leroy）、布鲁顿街、女子圣经协会、纽兰兹（Newlands）、贝阿特丽切、普雷德街、尤斯顿路、贝克街、多尼采蒂兄弟（餐馆）、施韦普斯（Schweppe's）、《伦敦新闻画报》、特拉法尔加广场、冯·黑贝尔（von Heber）、联合考试（the Conjoint）、维克托·霍斯利、巴克医生、大都会铁路、金合欢（mimosa） |
| 2026-09-08 | chapter-5.md | done | 4 块 / 5 段，check 退出码 0；新定名：法灵登路（Farringdon Road）、比林斯门（Billingsgate）、波希米亚（Bohemia）、舰队街（Fleet Street）、罗杰斯小姐（Miss Rogers）、帕德雷夫斯基（Paderewski）、兰厄姆坊（Langham Place）、坎伯韦尔（Camberwell）、《汤豪舍》（Tannhäuser）、德文郡（Devonshire，郡） |
2026-09-06 | chapter-6.md | 11 块 | check 退出码 0 | done
2026-09-06 | chapter-7.md | 6 块 | check 退出码 0 | done
2026-09-06 | chapter-8.md | 37 块 | check 退出码 0（261 段全覆盖核验） | done
2026-09-06 | chapter-9.md | 26 块 | check 退出码 0（102 段全覆盖核验） | done
2026-09-06 | chapter-10.md | 18 块 | check 退出码 0 | done
2026-09-06 | chapter-11.md | 1 块 | check 退出码 0 | done（终章）
2026-09-06 | 段末对齐 | - | - | 按段A回填定名统一：冯·赫伯→冯·黑贝尔、格林一家→格林家、青年女子圣经协会→女子圣经协会、贝雅特丽齐→贝阿特丽切、多尼采蒂（歌剧）→多尼采蒂餐馆、含羞草树→金合欢树；复检 6 章 check 全部退出码 0
| 2026-09-08 | 【整书完结】11/11 done | 批次2；首译：07:20上锁；段A（1-5章，源文程序化回填+段数奇偶校验）+段B（6-11章，段级零漏核验）并发2；全量验收11文件exit 0全过；跨段定名对齐约40处（冯·黑贝尔/多尼采蒂餐馆/金合欢树等）；术语表段A+40条、段B+百余条；系列第5卷，与尖顶屋/backwater/honeycomb风格对齐；删锁流转 |
