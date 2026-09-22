# 翻译计划（《风仙子》——玛丽·德·摩根）

## 本计划信息

- **项目名称**：《风仙子》（玛丽·德·摩根）
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

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | The Windfairies / 风仙子 | the-windfairies.md | 33.5KB | todo |
| 2 | Vain Kesta / 虚荣的凯斯塔 | vain-kesta.md | 17.3KB | todo |
| 3 | The Pool and the Tree / 池塘与树 | the-pool-and-the-tree.md | 11.4KB | todo |
| 4 | Nanina's Sheep / 纳尼娜的羊 | naninas-sheep.md | 12.0KB | todo |
| 5 | The Gipsy's Cup / 吉普赛人的杯子 | the-gipsys-cup.md | 48.6KB | todo |
| 6 | The Story of a Cat / 一只猫的故事 | the-story-of-a-cat.md | 19.7KB | todo |
| 7 | Dumb Othmar / 失声的奥特玛 | dumb-othmar.md | 45.6KB | todo |
| 8 | The Rain Maiden / 雨中少女 | the-rain-maiden.md | 13.6KB | todo |
| 9 | The Ploughman and the Gnome / 农夫与地精 | the-ploughman-and-the-gnome.md | 27.1KB | todo |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-13 | - | 建项目 | 从 待翻译/mary-de-morgan_the-windfairies.epub 提取 9 篇正文、建术语表初版、生成队列。领域 小说文学，形态 短篇集，模式 委派。 |
| 2026-08-14 | naninas-sheep/the-pool-and-the-tree (12.0+11.4KB) | done ×2 | exit 0 |
| 2026-08-15 | the-rain-maiden (13.6KB) | done | exit 0；20 对块、0 错配；术语照表（雨中少女/灰衣女子/旧城堡），无新词补充 |
| 2026-08-15 | vain-kesta (17.3KB) | done | exit 0；83 对块、0 错配；术语照表（凯斯塔/亚当/管家/公爵/宫殿/兵营），无新词需补入术语表 |
| 2026-08-15 | the-story-of-a-cat | 19.7KB / exit 0 | check_bilingual 49 对全过；无术语新增（波斯猫/暹罗猫/猫展均已在术语表）。 |
| 2026-08-15 | the-ploughman-and-the-gnome | 27.1KB / exit 0 | check_bilingual 90 对块、0 错配；术语照表（地精/橡胶/黑甲虫/仙灵），无新词需补入术语表。 |
| 2026-08-15 | the-windfairies | 33.5KB / 退出码0 | 书名同名主打篇；原文首段“windmill figures like them”处存在源文缺字，按最合理理解补足衔接译出 |
| 2026-08-15 | the-gipsys-cup | 48.6KB | 退出码 0 | 143 对块，0 可疑错配；术语沿用术语表（陶工/吉普赛女郎/陶轮/窑/小棕杯），无新词需补充 |
| 2026-08-15 | dumb-othmar | 45.6KB / 退出码 0 | 104 对块，0 可疑错配；术语照表（奥特玛/胡尔达/矮人/乐师/小个子/傻瓜汤米/渡鸦/镇长），新词补充：bird-boy=鸟孩子入术语表。 |
