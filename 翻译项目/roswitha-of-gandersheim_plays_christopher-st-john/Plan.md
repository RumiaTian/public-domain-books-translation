# 翻译计划：罗斯维塔戏剧集

## 本计划信息

- **项目名称**：roswitha-of-gandersheim_plays_christopher-st-john
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/历史古籍.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（12 篇，约 189KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-26 | dedication / prefaces / introduction / a-note / endnotes | done | 委派子代理，5 件 check 全过；回填甘德斯海姆等 18 条定名 |
| 2026-08-26 | the-plays-of-roswitha2 / dulcitius / callimachus | done | 委派子代理，check 全过（11+32+39 对块） |
| 2026-08-26 | gallicanus / paphnutius | done | 委派子代理，check 全过（79+81 对块），流式分批 |
| 2026-08-26 | sapientia / abraham | done | 委派子代理，check 全过（54+46 对块） |
| 2026-08-26 | 全书 12/12 done | 完结 | 主代理全书术语归一（泰绮丝/萨皮恩提亚/杜尔基提乌斯等 6 组变体），12 文件 check 全过、CSV 无 doing；refresh_progress 已刷新 |
