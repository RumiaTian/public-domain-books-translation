# 翻译计划（《罗伯特·E·霍华德短篇小说集》）

## 本计划信息

- **项目名称**：《罗伯特·E·霍华德短篇小说集》（Robert E. Howard）
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

> 本集为短篇集，走**委派模式**：主 agent 逐篇派子代理翻译，每个子代理执行单篇 9 步流程。各系列篇目建议按系列归组调度（所罗门·凯恩 6 篇、库尔 3 篇、基罗万—康拉德 3 篇等），便于人物/术语一致。

## 篇目概览（28 篇，按系列）

- **所罗门·凯恩系列**：red-shadows、skulls-in-the-stars、rattle-of-bones、the-moon-of-skulls、the-hills-of-the-dead
- **库尔系列**：the-shadow-kingdom、the-mirrors-of-tuzun-thune（kings-of-the-night 库尔客串）
- **布兰·马克·莫恩**：kings-of-the-night
- **基罗万—康拉德神秘学**：dig-me-no-grave、the-haunter-of-the-ring、the-voice-of-el-lil
- **史蒂夫·克拉尼冒险**：the-fire-of-ashurbanipal
- **柯尔比·巴克纳南方哥特**：black-canaan
- **南方密林恐怖**：black-hound-of-death、the-grisly-horror、the-fearsome-touch-of-death
- **史前/历史冒险与恐怖**：a-tale-of-the-cavemen、the-lost-race、wolfshead、in-the-forest-of-villef-re、sea-curse、gods-of-the-north、the-hyena、the-dream-snake
- **残稿/片断**：after-the-game、sleeping-beauty、weekly-short-story

（详细队列与状态见 `translation_queue.csv`。）

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
