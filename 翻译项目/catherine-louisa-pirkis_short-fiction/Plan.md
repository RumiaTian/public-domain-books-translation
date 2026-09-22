# 翻译计划（《凯瑟琳·卢伊莎·皮尔基斯短篇小说集》）

## 本计划信息

- **项目名称**：《凯瑟琳·卢伊莎·皮尔基斯短篇小说集》（Catherine Louisa Pirkis, *Short Fiction*）
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本篇目为短篇集，走委派模式，由子代理逐篇执行。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-14 | At Twelve Tonight / 今夜十二点 | done | 源文 12.5KB，译文 23.8KB；check 通过（18 对块、0 错配） |
| 2026-08-14 | Disappeared from Her Home / 自家中失踪 | done | 源文 7.0KB，译文 14.1KB；check 通过（5 对块、0 错配） |
| 2026-08-14 | drifting(38.2KB回填)/jack(22.0KB)/rhea(26.8KB) | done ×3 | exit 0; drifting 为前次中断遗留、校验通过后回填 |
| 2026-08-14 | trooping-with-crows (17KB) | done | exit 0 | **全书 6/6 译完** |
