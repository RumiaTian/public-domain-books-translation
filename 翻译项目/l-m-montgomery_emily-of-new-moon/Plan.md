# 翻译计划（新月庄园的艾米丽）

## 本计划信息

- **项目名称**：新月庄园的艾米丽（Emily of New Moon，L. M. 蒙哥马利）
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本项目为「长篇／委派模式」，由子代理逐章译，主 agent 统管术语与风格连贯。

## 篇目清单

> 全书 31 章，罗马数字 I–XXXI，章名原为纯文字无编号，已为各章文件加 `chapter-N-` 前缀以保证自然排序与阅读顺序一致。合计约 626.1KB。

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 一　谷中小屋 | chapter-1-the-house-in-the-hollow.md | 13.7KB | todo |
| 2 | 二　守夜 | chapter-2-a-watch-in-the-night.md | 20.5KB | todo |
| 3 | 三　非亲非故 | chapter-3-a-hop-out-of-kin.md | 24.2KB | todo |
| 4 | 四　家庭会议 | chapter-4-a-family-conclave.md | 18.5KB | todo |
| 5 | 五　棋逢对手 | chapter-5-diamond-cut-diamond.md | 14.2KB | todo |
| 6 | 六　新月庄园 | chapter-6-new-moon.md | 19.6KB | todo |
| 7 | 七　昨日之书 | chapter-7-the-book-of-yesterday.md | 28.4KB | todo |
| 8 | 八　火的考验 | chapter-8-trial-by-fire.md | 21.2KB | todo |
| 9 | 九　特别的眷顾 | chapter-9-a-special-providence.md | 25.4KB | todo |
| 10 | 十　成长的烦恼 | chapter-10-growing-pains.md | 14.5KB | todo |
| 11 | 十一　伊尔丝 | chapter-11-ilse.md | 15.5KB | todo |
| 12 | 十二　艾菊丛 | chapter-12-the-tansy-patch.md | 27.0KB | todo |
| 13 | 十三　夏娃之女 | chapter-13-daughter-of-eve.md | 17.6KB | todo |
| 14 | 十四　锦衣玉食 | chapter-14-fancy-fed.md | 12.4KB | todo |
| 15 | 十五　种种悲剧 | chapter-15-various-tragedies.md | 22.2KB | todo |
| 16 | 十六　查办布朗内尔小姐 | chapter-16-check-for-miss-brownell.md | 24.8KB | todo |
| 17 | 十七　活的信件 | chapter-17-living-epistles.md | 23.9KB | todo |
| 18 | 十八　卡西迪神父 | chapter-18-father-cassidy.md | 32.5KB | todo |
| 19 | 十九　重归于好 | chapter-19-friends-again.md | 7.4KB | todo |
| 20 | 二十　航空邮件 | chapter-20-by-aerial-post.md | 20.1KB | todo |
| 21 | 二十一　浪漫而不舒适 | chapter-21-romantic-but-not-comfortable.md | 20.2KB | todo |
| 22 | 二十二　威瑟农庄 | chapter-22-wyther-grange.md | 14.5KB | todo |
| 23 | 二十三　与鬼打交道 | chapter-23-deals-with-ghosts.md | 18.7KB | todo |
| 24 | 二十四　另一种幸福 | chapter-24-a-different-kind-of-happiness.md | 13.0KB | todo |
| 25 | 二十五　她不可能干出这事 | chapter-25-she-couldn-t-have-done-it.md | 11.3KB | todo |
| 26 | 二十六　在海湾边 | chapter-26-on-the-bay-shore.md | 21.2KB | todo |
| 27 | 二十七　艾米丽的誓言 | chapter-27-the-vow-of-emily.md | 35.3KB | todo |
| 28 | 二十八　织梦者 | chapter-28-a-weaver-of-dreams.md | 23.8KB | todo |
| 29 | 二十九　亵渎 | chapter-29-sacrilege.md | 20.1KB | todo |
| 30 | 三十　当帷幕升起 | chapter-30-when-the-curtain-lifted.md | 24.8KB | todo |
| 31 | 三十一　艾米丽的伟大时刻 | chapter-31-emily-s-great-moment.md | 19.6KB | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
