# Plan（《迈克》翻译计划）

> 从 `prompts/翻译计划模板.md` 复制建立。执行步骤、CSV 格式等通用规范见模板，此处为本书实例。

---

## 本计划信息

- **项目名称**：p-g-wodehouse_mike（《迈克》，P. G. 伍德豪斯）
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
| 0 | 献词 | 00-dedication.md | 0.0KB | todo |
| 1 | 迈克 | 01-mike.md | 10.6KB | todo |
| 2 | 南下之旅 | 02-the-journey-down.md | 10.4KB | todo |
| 3 | 迈克遇到一位友善的当地人 | 03-mike-finds-a-friendly-native.md | 10.1KB | todo |
| 4 | 练网 | 04-at-the-nets.md | 9.0KB | todo |
| 5 | 夜宴狂欢 | 05-revelry-by-night.md | 13.8KB | todo |
| 6 | 危局得脱 | 06-in-which-a-tight-corner-is-evaded.md | 8.3KB | todo |
| 7 | 迈克成了话题 | 07-in-which-mike-is-discussed.md | 11.2KB | todo |
| 8 | 与镇上人干了一仗 | 08-a-row-with-the-town.md | 11.8KB | todo |
| 9 | 暴风雨前 | 09-before-the-storm.md | 10.2KB | todo |
| 10 | 大野餐 | 10-the-great-picnic.md | 8.8KB | todo |
| 11 | 野餐收场 | 11-the-conclusion-of-the-picnic.md | 10.1KB | todo |
| 12 | 迈克得到机会 | 12-mike-gets-his-chance.md | 9.5KB | todo |
| 13 | 对马里波恩板球俱乐部一战 | 13-the-m-c-c-match.md | 15.0KB | todo |
| 14 | 一场小小风波 | 14-a-slight-imbroglio.md | 7.1KB | todo |
| 15 | 迈克空出一个位子 | 15-mike-creates-a-vacancy.md | 10.5KB | todo |
| 16 | 行家考核 | 16-an-expert-examination.md | 9.6KB | todo |
| 17 | 又一个空缺 | 17-another-vacancy.md | 9.4KB | todo |
| 18 | 鲍勃有消息要透露 | 18-bob-has-news-to-impart.md | 8.6KB | todo |
| 19 | 迈克又睡着了 | 19-mike-goes-to-sleep-again.md | 11.7KB | todo |
| 20 | 队伍补齐了 | 20-the-team-is-filled-up.md | 8.5KB | todo |
| 21 | 直言不讳的玛乔丽 | 21-marjory-the-frank.md | 10.8KB | todo |
| 22 | 怀亚特想起一个约会 | 22-wyatt-is-reminded-of-an-engagement.md | 8.3KB | todo |
| 23 | 给阿普尔比先生的惊喜 | 23-a-surprise-for-mr-appleby.md | 9.9KB | todo |
| 24 | 被抓住了 | 24-caught.md | 8.3KB | todo |
| 25 | 开拔令 | 25-marching-orders.md | 5.8KB | todo |
| 26 | 余波 | 26-the-aftermath.md | 8.7KB | todo |
| 27 | 对里普顿一战 | 27-the-ripton-match.md | 10.5KB | todo |
| 28 | 迈克赢球回家 | 28-mike-wins-home.md | 20.0KB | todo |
| 29 | 怀亚特再现 | 29-wyatt-again.md | 5.0KB | todo |
| 30 | 杰克逊先生拿定主意 | 30-mr-jackson-makes-up-his-mind.md | 10.6KB | todo |
| 31 | 塞德利 | 31-sedleigh.md | 7.6KB | todo |
| 32 | 皮史密斯 | 32-psmith.md | 7.5KB | todo |
| 33 | 圈占地盘 | 33-staking-out-a-claim.md | 10.9KB | todo |
| 34 | 游击战 | 34-guerilla-warfare.md | 12.0KB | todo |
| 35 | 深夜里的不愉快 | 35-unpleasantness-in-the-small-hours.md | 10.1KB | todo |
| 36 | 阿代尔 | 36-adair.md | 10.2KB | todo |
| 37 | 迈克找到活干 | 37-mike-finds-occupation.md | 10.2KB | todo |
| 38 | 消防队会议 | 38-the-fire-brigade-meeting.md | 12.0KB | todo |
| 39 | 阿喀琉斯走出营帐 | 39-achilles-leaves-his-tent.md | 7.8KB | todo |
| 40 | 对唐宁舍一战 | 40-the-match-with-downing-s.md | 16.0KB | todo |
| 41 | 杰利科的异常举动 | 41-the-singular-behavior-of-jellicoe.md | 8.8KB | todo |
| 42 | 杰利科上了病号名单 | 42-jellicoe-goes-on-the-sick-list.md | 6.9KB | todo |
| 43 | 迈克接到一项委托 | 43-mike-receives-a-commission.md | 8.6KB | todo |
| 44 | 并完成了它 | 44-and-fulfils-it.md | 9.1KB | todo |
| 45 | 追踪 | 45-pursuit.md | 12.0KB | todo |
| 46 | 给萨米上色 | 46-the-decoration-of-sammy.md | 6.2KB | todo |
| 47 | 唐宁先生嗅到线索 | 47-mr-downing-on-the-scent.md | 9.8KB | todo |
| 48 | 警犬 | 48-the-sleuthhound.md | 10.6KB | todo |
| 49 | 挫折 | 49-a-check.md | 11.1KB | todo |
| 50 | 销毁证据者 | 50-the-destroyer-of-evidence.md | 9.8KB | todo |
| 51 | 主要说靴子 | 51-mainly-about-boots.md | 11.5KB | todo |
| 52 | 再度追踪 | 52-on-the-trail-again.md | 5.8KB | todo |
| 53 | 水壶法 | 53-the-kettle-method.md | 10.5KB | todo |
| 54 | 阿代尔与迈克谈谈 | 54-adair-has-a-word-with-mike.md | 8.1KB | todo |
| 55 | 消除隔阂 | 55-clearing-the-air.md | 11.7KB | todo |
| 56 | 议和了 | 56-in-which-peace-is-declared.md | 9.3KB | todo |
| 57 | 唐宁先生行动了 | 57-mr-downing-moves.md | 10.9KB | todo |
| 58 | 画家认领作品 | 58-the-artist-claims-his-work.md | 14.4KB | todo |
| 59 | 塞德利对雷金 | 59-sedleigh-v-wrykyn.md | 9.9KB | todo |

共 60 篇（献词 + 59 章），源文合计约 592KB。全书单一连续叙事（雷金→塞德利两大段），章数多，走委派模式；皮史密斯 XXXII 章登场。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
