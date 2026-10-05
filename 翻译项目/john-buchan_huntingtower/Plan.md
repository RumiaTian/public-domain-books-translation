# 翻译计划（john-buchan_huntingtower）

## 本计划信息

- **项目名称**：john-buchan_huntingtower（Huntingtower）
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

共 19 篇，见 `translation_queue.csv`（合计 439KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
- 2026-10-04 05:10｜批次3直启｜chapter-1.md 完成，check_bilingual 通过（[1308] 断点核验回填，中断前已完成）

- 2026-10-04 05:19｜批次3直启子代理｜chapter-2.md 完成，check_bilingual 通过
- 2026-10-04 05:31｜批次3直启子代理｜chapter-3.md 完成，check_bilingual 通过
- 2026-10-04 05:40｜批次3直启子代理｜chapter-4.md 完成，check_bilingual 通过
- 2026-10-04 05:53｜批次3直启子代理｜chapter-5.md 完成，check_bilingual 通过
- 2026-10-04 06:03｜批次3直启子代理｜chapter-6.md 完成，check_bilingual 通过
- 2026-10-04 06:12｜批次3直启子代理｜chapter-7.md 完成，check_bilingual 通过
- 2026-10-04 06:21｜批次3直启子代理｜chapter-8.md 完成，check_bilingual 通过
- 2026-10-04 06:32｜批次3直启子代理｜chapter-9.md 完成，check_bilingual 通过
- 2026-10-04 06:45｜批次3直启子代理｜chapter-10.md 完成，check_bilingual 通过
- 2026-10-05 05:23｜批次3直启子代理｜chapter-11.md 完成，check_bilingual 通过
- 2026-10-05 05:32｜批次3直启子代理｜chapter-12.md 完成，check_bilingual 通过
- 2026-10-05 05:40｜批次3直启子代理｜chapter-13.md 完成，check_bilingual 通过
- 2026-10-05 05:57｜批次3直启子代理｜chapter-14.md 完成，check_bilingual 通过
- 2026-10-05 06:09｜批次3直启子代理｜chapter-15.md 完成，check_bilingual 通过
- 2026-10-05 06:10｜批次3直启｜endnotes.md 完成，check_bilingual 通过
- 2026-10-05 06:10｜批次3直启｜dedication.md 完成，check_bilingual 通过

- 2026-10-05 06:19｜批次3直启子代理｜chapter-16.md 完成，check_bilingual 通过
- 2026-10-05 06:23｜批次3直启子代理｜prologue.md 完成，check_bilingual 通过

## 完书纪要
- 2026-10-05 06:24｜批次3直启｜全书 19/19 项完成（序章+16 章+题献+尾注），check_bilingual 全部通过，锁已删除。第二十二本完工。

