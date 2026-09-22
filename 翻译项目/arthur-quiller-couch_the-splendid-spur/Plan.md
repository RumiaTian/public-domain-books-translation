# Plan（《灿烂的马刺》翻译计划）

> 从 `prompts/翻译计划模板.md` 复制建立。执行步骤、CSV 格式等通用规范见模板，此处为本书实例。

---

## 本计划信息

- **项目名称**：arthur-quiller-couch_the-splendid-spur（《灿烂的马刺》，阿瑟·奎勒-库奇）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

> 执行步骤（读配置→取任务→读源文→翻译→自检→自动检查→回填状态→追加日志→循环）见 `prompts/翻译计划模板.md`「执行步骤」，本文件不重复；完成状态须双写（项目 CSV + 根表）。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 0 | 献词 | 00-dedication.md | 0.8KB | todo |
| 1 | 王冠客栈的滚木球场 | 01-the-bowling-green-of-the-crown.md | 12.8KB | todo |
| 2 | 穿琥珀缎斗篷的年轻人 | 02-the-young-man-in-the-cloak-of-amber-satin.md | 11.6KB | todo |
| 3 | 我卷入酒馆斗殴：险些脱不了身 | 03-i-find-myself-in-a-tavern-brawl-and-barely-escape.md | 21.2KB | todo |
| 4 | 我踏上旅途 | 04-i-take-the-road.md | 20.2KB | todo |
| 5 | 我在「三杯」客栈的奇遇 | 05-my-adventure-at-the-three-cups.md | 21.2KB | todo |
| 6 | 松林里的逃亡 | 06-the-flight-in-the-pine-wood.md | 16.4KB | todo |
| 7 | 我找到一个同伴 | 07-i-find-a-comrade.md | 15.6KB | todo |
| 8 | 我丢了国王的信：被押往布里斯托尔 | 08-i-lose-the-king-s-letter-and-am-carried-to-bristol.md | 21.4KB | todo |
| 9 | 我越狱了 | 09-i-break-out-of-prison.md | 36.2KB | todo |
| 10 | 波特里船长与塞特尔上尉 | 10-captain-pottery-and-captain-settle.md | 20.2KB | todo |
| 11 | 我骑马下行到坦普尔：受到款待 | 11-i-ride-down-into-temple-and-am-well-treated-there.md | 14.8KB | todo |
| 12 | 琼恩如何救了西路军：并目睹布拉多克荒原之战 | 12-how-joan-saved-the-army-of-the-west-and-saw-the-fight-on-braddock-down.md | 15.5KB | todo |
| 13 | 我在博德明集市买镜子：遇见汉尼拔·廷科姆先生 | 13-i-buy-a-looking-glass-at-bodmin-fair-and-meet-with-mr-hannibal-tingcomb.md | 13.7KB | todo |
| 14 | 我在格莱斯宅一无所成 | 14-i-do-no-good-in-the-house-of-gleys.md | 14.2KB | todo |
| 15 | 我告别琼恩，奔赴战场 | 15-i-leave-joan-and-ride-to-the-wars.md | 13.4KB | todo |
| 16 | 斯坦福德荒原之战 | 16-the-battle-of-stamford-heath.md | 20.1KB | todo |
| 17 | 燃绿火而遇欢喜奇缘 | 17-i-meet-with-a-happy-adventure-by-burning-of-a-green-light.md | 23.5KB | todo |
| 18 | 琼恩最后一次帮我 | 18-joan-does-me-her-last-service.md | 21.6KB | todo |
| 19 | 灵车历险 | 19-the-adventure-of-the-hearse.md | 21.1KB | todo |
| 20 | 岩礁历险：以及我如何与同伴握手 | 20-the-adventure-of-the-ledge-and-how-i-shook-hands-with-my-comrade.md | 19.3KB | todo |

共 21 篇（献词 + 20 章），源文合计约 375KB。全书单一第一人称回忆录但章数多、体量大，走委派模式；跨章连贯靠术语表「情节主线」+ 黄金样本 + 前篇末尾补偿。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
