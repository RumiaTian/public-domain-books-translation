# Plan.md — honore-de-balzac_shorts-from-scenes-from-private-life_various-translators

## 本计划信息

- **项目名称**：honore-de-balzac_shorts-from-scenes-from-private-life_various-translators（巴尔扎克《私人生活场景》短篇集 / Balzac: Shorts from Scenes from Private Life）
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
| `原文/*.md` | 源文（22 文件：前言 + 20 篇 + 尾注） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`「执行步骤」9 步推进；本篇目为短篇集，执行模式为**委派**（见 WORKFLOW.md）。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 人间喜剧前言 | introduction.md | 29.0KB | todo |
| 2 | 猫打球商店 | at-the-sign-of-the-cat-and-racket.md | 119.5KB | todo |
| 3 | 苏城舞会 | the-ball-at-sceaux.md | 121.7KB | todo |
| 4 | 钱袋 | the-purse.md | 66.0KB | todo |
| 5 | 死冤家 | the-vendetta.md | 139.6KB | todo |
| 6 | 费尔米安尼夫人 | madame-firmiani.md | 43.5KB | todo |
| 7 | 两个家庭 | a-second-home.md | 145.3KB | todo |
| 8 | 夫唱妇随 | domestic-peace.md | 74.9KB | todo |
| 9 | 假情妇 | the-imaginary-mistress.md | 107.0KB | todo |
| 10 | 一个女人的侧影 | a-study-of-woman.md | 18.7KB | todo |
| 11 | 另一个女人的侧影 | another-study-of-woman.md | 82.6KB | todo |
| 12 | 大布雷泰什 | la-grande-bret-che.md | 43.7KB | todo |
| 13 | 遭遗弃的女人 | the-deserted-woman.md | 92.6KB | todo |
| 14 | 掷弹兵 | la-grenadi-re.md | 50.6KB | todo |
| 15 | 委托 | the-message.md | 28.1KB | todo |
| 16 | 高利贷者 | gobseck.md | 124.9KB | todo |
| 17 | 奥诺丽纳 | honorine.md | 165.9KB | todo |
| 18 | 夏倍上校 | colonel-chabert.md | 132.4KB | todo |
| 19 | 无神论者做弥撒 | the-atheist-s-mass.md | 36.6KB | todo |
| 20 | 禁治产 | the-commission-in-lunacy.md | 156.5KB | todo |
| 21 | 比埃尔·格拉苏 | pierre-grassou.md | 44.2KB | todo |
| 22 | 尾注 | endnotes.md | 0.1KB | todo |

共 22 篇，约 1823KB 源文；多篇 >50KB，按通用翻译引擎第七节分段处理。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
