# 翻译计划（j-s-fletcher_the-talleyrand-maxim）

## 本计划信息

- **项目名称**：j-s-fletcher_the-talleyrand-maxim（The Talleyrand Maxim）
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

共 28 篇，见 `translation_queue.csv`（合计 420KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |

- 2026-09-26 06:38｜批次3直启子代理｜chapter-1.md 完成，check_bilingual 通过
- 2026-09-26 06:44｜批次3直启子代理｜chapter-2.md 完成，check_bilingual 通过
- 2026-09-26 06:53｜批次3直启子代理｜chapter-3.md 完成，check_bilingual 通过
- 2026-09-26 06:58｜批次3直启子代理｜chapter-4.md 完成，check_bilingual 通过
- 2026-09-26 07:05｜批次3直启子代理｜chapter-5.md 完成，check_bilingual 通过
- 2026-09-26 07:09｜批次3直启子代理｜chapter-6.md 完成，check_bilingual 通过
- 2026-09-24 07:13｜批次3直启子代理｜chapter-7.md 完成，check_bilingual 通过
- 2026-09-27 06:10｜批次3直启子代理｜chapter-8.md 完成，check_bilingual 通过
- 2026-09-27 06:14｜批次3直启子代理｜chapter-9.md 完成，check_bilingual 通过
- 2026-09-27 06:22｜批次3直启子代理｜chapter-10.md 完成，check_bilingual 通过
- 2026-09-27 06:27｜批次3直启子代理｜chapter-11.md 完成，check_bilingual 通过
- 2026-09-27 06:32｜批次3直启子代理｜chapter-12.md 完成，check_bilingual 通过
- 2026-09-27 06:37｜批次3直启子代理｜chapter-13.md 完成，check_bilingual 通过
- 2026-09-27 06:42｜批次3直启子代理｜chapter-14.md 完成，check_bilingual 通过
- 2026-09-27 06:48｜批次3直启子代理｜chapter-15.md 完成，check_bilingual 通过
- 2026-09-27 06:53｜批次3直启子代理｜chapter-16.md 完成，check_bilingual 通过
- 2026-09-27 07:00｜批次3直启子代理｜chapter-17.md 完成，check_bilingual 通过
- 2026-09-27 07:07｜批次3直启子代理｜chapter-18.md 完成，check_bilingual 通过
- 2026-09-28 06:16｜批次3直启｜chapter-19.md 断点验收：昨晨[1308]中断，本轮核验译文已完整（空白归一化逐行0缺失，check 退出码0），回填 done（19/28）
- 2026-09-28 06:23｜批次3直启子代理｜chapter-20.md 完成，check_bilingual 通过
- 2026-09-28 06:38｜批次3直启子代理｜chapter-21.md 完成，check_bilingual 通过
- 2026-09-28 06:39｜批次3直启子代理｜chapter-22.md 完成，check_bilingual 通过

- 2026-09-28 06:45｜批次3直启子代理｜chapter-23.md 完成，check_bilingual 通过
- 2026-09-28 06:52｜批次3直启子代理｜chapter-24.md 完成，check_bilingual 通过
- 2026-09-28 06:57｜批次3直启子代理｜chapter-25.md 完成，check_bilingual 通过
- 2026-09-28 07:02｜批次3直启子代理｜chapter-26.md 完成，check_bilingual 通过
- 2026-09-28 07:06｜批次3直启子代理｜chapter-27.md 完成，check_bilingual 通过
- 2026-09-28 07:14｜批次3直启子代理｜chapter-28.md 完成，check_bilingual 通过（全书 28/28 完结）

- 2026-09-28 07:15｜批次3直启｜全书完结流转：28/28 篇全部 done（含 09-27/09-28 两轮接续、ch19 断点验收），认领锁已删除，移交审核阶段。
