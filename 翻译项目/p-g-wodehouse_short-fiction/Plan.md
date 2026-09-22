# Plan.md — p-g-wodehouse_short-fiction

## 本计划信息

- **项目名称**：p-g-wodehouse_short-fiction（伍德豪斯短篇集（P. G. Wodehouse: Short Fiction））
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
| `原文/*.md` | 源文（40 文件） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`「执行步骤」9 步推进。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | a-sea-of-troubles | a-sea-of-troubles.md | 23.9KB | todo |
| 2 | absent-treatment | absent-treatment.md | 26.7KB | todo |
| 3 | ahead-of-schedule | ahead-of-schedule.md | 27.6KB | todo |
| 4 | at-geisenheimers | at-geisenheimers.md | 32.7KB | todo |
| 5 | bill-the-bloodhound | bill-the-bloodhound.md | 31.7KB | todo |
| 6 | black-for-luck | black-for-luck.md | 32.1KB | todo |
| 7 | by-advice-of-counsel | by-advice-of-counsel.md | 23.0KB | todo |
| 8 | concealed-art | concealed-art.md | 25.8KB | todo |
| 9 | crowned-heads | crowned-heads.md | 30.2KB | todo |
| 10 | death-at-the-excelsior | death-at-the-excelsior.md | 43.4KB | todo |
| 11 | deep-waters | deep-waters.md | 34.9KB | todo |
| 12 | disentangling-old-duggie | disentangling-old-duggie.md | 32.2KB | todo |
| 13 | in-alcala | in-alcala.md | 43.2KB | todo |
| 14 | lord-emsworth-acts-for-the-best | lord-emsworth-acts-for-the-best.md | 36.7KB | todo |
| 15 | mister-potter-takes-a-rest-cure | mister-potter-takes-a-rest-cure.md | 39.9KB | todo |
| 16 | misunderstood | misunderstood.md | 15.6KB | todo |
| 17 | one-touch-of-nature | one-touch-of-nature.md | 22.8KB | todo |
| 18 | out-of-school | out-of-school.md | 22.9KB | todo |
| 19 | pots-o-money | pots-o-money.md | 31.7KB | todo |
| 20 | rough-hew-them-how-we-will | rough-hew-them-how-we-will.md | 25.6KB | todo |
| 21 | ruth-in-exile | ruth-in-exile.md | 31.9KB | todo |
| 22 | sir-agravaine | sir-agravaine.md | 30.2KB | todo |
| 23 | something-to-worry-about | something-to-worry-about.md | 31.8KB | todo |
| 24 | the-best-sauce | the-best-sauce.md | 29.6KB | todo |
| 25 | the-goalkeeper-and-the-plutocrat | the-goalkeeper-and-the-plutocrat.md | 25.7KB | todo |
| 26 | the-good-angel | the-good-angel.md | 29.2KB | todo |
| 27 | the-making-of-macs | the-making-of-macs.md | 30.2KB | todo |
| 28 | the-man-the-maid-and-the-miasma | the-man-the-maid-and-the-miasma.md | 26.0KB | todo |
| 29 | the-man-upstairs | the-man-upstairs.md | 31.9KB | todo |
| 30 | the-man-who-disliked-cats | the-man-who-disliked-cats.md | 30.6KB | todo |
| 31 | the-man-with-two-left-feet | the-man-with-two-left-feet.md | 36.2KB | todo |
| 32 | the-mixer | the-mixer.md | 57.0KB | todo |
| 33 | the-romance-of-an-ugly-policeman | the-romance-of-an-ugly-policeman.md | 26.5KB | todo |
| 34 | the-test-case | the-test-case.md | 25.3KB | todo |
| 35 | the-tuppenny-millionaire | the-tuppenny-millionaire.md | 29.7KB | todo |
| 36 | three-from-dunsterville | three-from-dunsterville.md | 29.9KB | todo |
| 37 | tom-dick-and-harry | tom-dick-and-harry.md | 16.2KB | todo |
| 38 | when-doctors-disagree | when-doctors-disagree.md | 32.8KB | todo |
| 39 | when-papa-swore-in-hindustani | when-papa-swore-in-hindustani.md | 11.0KB | todo |
| 40 | wiltons-holiday | wiltons-holiday.md | 26.7KB | todo |

---

## 运行日志

| 日期 | 事件 | 备注 |
|------|------|------|
| 2026-08-17 | 建项目 | epub 提取 40 篇，术语表初版建成 |
