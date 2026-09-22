# 翻译计划（紫色国土 / The Purple Land）

## 本计划信息

- **项目名称**：w-h-hudson_the-purple-land（《紫色国土》，W. H. 哈德森）
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

## translation_queue.csv 格式

```
file,size_kb,status
00-preface.md,2.0,todo
01-rambles-in-modern-troy.md,21.7,todo
...
```

状态取值：`todo` 待译 / `doing` 翻译中 / `done` 已完成。

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本项目长篇/委派模式，由主 agent 调度、逐篇下沉子代理执行（并发 ≤ 3）。全书 31 篇约 519KB。

## 篇目清单

| # | 章号 | 篇名 | 源文 | 状态 |
|---|------|------|------|------|
| 1 | — | 前言 Preface | 00-preface.md | todo |
| 2 | I | Rambles in Modern Troy 现代特洛伊漫游 | 01-rambles-in-modern-troy.md | todo |
| 3 | II | Peasant Homes and Hearts 农家与农心 | 02-peasant-homes-and-hearts.md | todo |
| 4 | III | Materials for a Pastoral 田园素材 | 03-materials-for-a-pastoral.md | todo |
| 5 | IV | Vagabonds' Rest 流浪者之歇 | 04-vagabonds-rest.md | todo |
| 6 | V | A Colony of English Gentlemen 英国绅士殖民地 | 05-a-colony-of-english-gentlemen.md | todo |
| 7 | VI | The Colony Under a Cloud 蒙阴的殖民地 | 06-the-colony-under-a-cloud.md | todo |
| 8 | VII | Love of the Beautiful 爱美之心 | 07-love-of-the-beautiful.md | todo |
| 9 | VIII | Manuel, Also Called the Fox 曼努埃尔，人称狐狸 | 08-manuel-also-called-the-fox.md | todo |
| 10 | IX | The Botanist and the Simple Native 植物学家与淳朴土人 | 09-the-botanist-and-the-simple-native.md | todo |
| 11 | X | Matters Relating to the Republic 共和国种种 | 10-matters-relating-to-the-republic.md | todo |
| 12 | XI | The Woman and the Serpent 女人与蛇 | 11-the-woman-and-the-serpent.md | todo |
| 13 | XII | Children in the Forest 林中孩童 | 12-children-in-the-forest.md | todo |
| 14 | XIII | Barking Dogs and Shouting Rebels 犬吠与叛众鼓噪 | 13-barking-dogs-and-shouting-rebels.md | todo |
| 15 | XIV | Maids of Fancy: Maids of Yí 想象之女：伊河之女 | 14-maids-of-fancy-maids-of-y.md | todo |
| 16 | XV | When the Trumpet Calls to Battle 号角召战 | 15-when-the-trumpet-calls-to-battle.md | todo |
| 17 | XVI | Romance of the White Flower 白花罗曼史 | 16-romance-of-the-white-flower.md | todo |
| 18 | XVII | Passion Versus Patriotism 激情对爱国 | 17-passion-versus-patriotism.md | todo |
| 19 | XVIII | Rest on Thy Rock, Andromeda! 安睡岩上，安德洛墨达！ | 18-rest-on-thy-rock-andromeda.md | todo |
| 20 | XIX | Tales of the Purple Land 紫色国土故事集 | 19-tales-of-the-purple-land.md | todo |
| 21 | XX | A Ghastly Gift 骇人的赠礼 | 20-a-ghastly-gift.md | todo |
| 22 | XXI | Liberty and Dirt 自由与尘土 | 21-liberty-and-dirt.md | todo |
| 23 | XXII | A Crown of Nettles 荨麻之冠 | 22-a-crown-of-nettles.md | todo |
| 24 | XXIII | The Red Flag of Victory 胜利的红旗 | 23-the-red-flag-of-victory.md | todo |
| 25 | XXIV | Mystery of the Green Butterfly 绿蝶之谜 | 24-mystery-of-the-green-butterfly.md | todo |
| 26 | XXV | Deliver Me from Mine Enemy 救我脱离仇敌 | 25-deliver-me-from-mine-enemy.md | todo |
| 27 | XXVI | Lock and Key and Sinners Three 锁钥与三罪人 | 26-lock-and-key-and-sinners-three.md | todo |
| 28 | XXVII | Night and Flight 黑夜与出逃 | 27-night-and-flight.md | todo |
| 29 | XXVIII | Goodbye to the Purple Land 别了，紫色国土 | 28-goodbye-to-the-purple-land.md | todo |
| 30 | XXIX | Back to Buenos Aires 重返布宜诺斯艾利斯 | 29-back-to-buenos-aires.md | todo |
| 31 | — | 附录：东岸区简史 | 30-appendix-history-of-the-banda-oriental.md | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
