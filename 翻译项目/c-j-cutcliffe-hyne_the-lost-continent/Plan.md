# 翻译计划（c-j-cutcliffe-hyne_the-lost-continent）

## 本计划信息

- **项目名称**：c-j-cutcliffe-hyne_the-lost-continent（The Lost Continent）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置 | 人工 |
| `术语表.md` | 翻译硬约束层，每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列（file,size_kb,status） | 翻译前改 doing，完成后改 done（双写根表） |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`（9 步：读配置→取 todo→doing→读源文→翻译→自检→check_bilingual→双写 done→日志）。

## 篇目清单

共 22 篇，见 `translation_queue.csv`（合计 516KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
- 2026-10-08 06:27｜批次3直启子代理｜chapter-1.md 完成，check_bilingual 通过
- 2026-10-08 06:36｜批次3直启子代理｜chapter-2.md 完成，check_bilingual 通过
- 2026-10-08 06:44｜批次3直启子代理｜chapter-3.md 完成，check_bilingual 通过
- 2026-10-08 06:55｜批次3直启子代理｜chapter-4.md 完成，check_bilingual 通过
- 2026-10-08 07:08｜批次3直启子代理｜chapter-5.md 完成，check_bilingual 通过
- 2026-10-08 07:19｜批次3直启子代理｜chapter-6.md 完成，check_bilingual 通过
- 2026-10-08 07:28｜批次3直启子代理｜chapter-7.md 完成，check_bilingual 通过
- 2026-10-09 06:19｜批次3直启子代理｜chapter-8.md 完成，check_bilingual 通过
- 2026-10-09 06:27｜批次3直启子代理｜chapter-9.md 完成，check_bilingual 通过
- 2026-10-09 06:37｜批次3直启子代理｜chapter-10.md 完成，check_bilingual 通过
- 2026-10-09 06:45｜批次3直启子代理｜chapter-11.md 完成，check_bilingual 通过
- 2026-10-09 06:54｜批次3直启子代理｜chapter-12.md 完成，check_bilingual 通过
- 2026-10-09 07:02｜批次3直启子代理｜chapter-13.md 完成，check_bilingual 通过
- 2026-10-09 07:11｜批次3直启子代理｜chapter-14.md 完成，check_bilingual 通过
- 2026-10-09 07:18｜批次3直启子代理｜chapter-15.md 完成，check_bilingual 通过
- 2026-10-10 06:19｜批次3直启子代理｜chapter-16.md 完成，check_bilingual 通过
- 2026-10-11 06:19｜批次3直启子代理｜chapter-17.md 完成，check_bilingual 通过
- 2026-10-11 06:27｜批次3直启子代理｜chapter-18.md 完成，check_bilingual 通过
- 2026-10-11 06:34｜批次3直启子代理｜chapter-19.md 完成，check_bilingual 通过
- 2026-10-11 06:39｜批次3直启子代理｜chapter-20.md 完成，check_bilingual 通过
- 2026-10-11 06:45｜批次3直启主代理｜endnotes.md 完成，check_bilingual 通过（内联翻译）
- 2026-10-11 06:48｜批次3直启子代理｜prologue.md 完成，check_bilingual 通过

## 完书纪要（2026-10-11）
《The Lost Continent》全书竣工：22/22（20 章 + 序言 Prefatory + 尾注；endnotes 由主代理内联翻译，ch8/ch16/ch17 曾额度中断重派后完成）。终项 prologue.md（20.1KB，60 对块）check_bilingual exit 0，德乌卡利翁手稿叙事框架收束于加那利群岛线。CSV 行数=输出文件数=22，零缺失。亚特兰蒂斯神权-海权定名体系完整（福伦尼刻/祭司氏族/奥秘的方舟/太阳神主等逾 150 条）。认领锁已删除。全书第 29 本完工。
