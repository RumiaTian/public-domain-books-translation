# 翻译计划（h-beam-piper_murder-in-the-gunroom）

## 本计划信息

- **项目名称**：h-beam-piper_murder-in-the-gunroom（Murder In The Gunroom）
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

共 22 篇，见 `translation_queue.csv`（合计 391KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |

- 2026-09-24 06:14｜批次3直启子代理｜chapter-1.md 完成，check_bilingual 通过
- 2026-09-24 06:21｜批次3直启子代理｜chapter-2.md 完成，check_bilingual 通过
- 2026-09-24 06:26｜批次3直启子代理｜chapter-3.md 完成，check_bilingual 通过
- 2026-09-24 06:31｜批次3直启子代理｜chapter-4.md 完成，check_bilingual 通过
- 2026-09-24 06:38｜批次3直启子代理｜chapter-5.md 完成，check_bilingual 通过
- 2026-09-24 06:42｜批次3直启子代理｜chapter-6.md 完成，check_bilingual 通过
- 2026-09-24 06:49｜批次3直启子代理｜chapter-7.md 完成，check_bilingual 通过
- 2026-09-24 06:54｜批次3直启子代理｜chapter-8.md 完成，check_bilingual 通过
- 2026-09-24 07:07｜批次3直启子代理｜chapter-9.md 完成（[1301]免责重派成功），check_bilingual 通过
- 2026-09-24 07:15｜批次3直启子代理｜chapter-10.md 完成，check_bilingual 通过
- 2026-09-24 07:23｜批次3直启子代理｜chapter-11.md 完成，check_bilingual 通过
- 2026-09-24 07:31｜批次3直启子代理｜chapter-12.md 完成，check_bilingual 通过
- 2026-09-24 11:11｜批次3直启子代理｜chapter-13.md 断点续作完成，check_bilingual 通过
- 2026-09-24 11:22｜批次3直启子代理｜chapter-14.md 完成，check_bilingual 通过
- 2026-09-24 11:29｜批次3直启子代理｜chapter-15.md 完成，check_bilingual 通过
- 2026-09-24 11:37｜批次3直启子代理｜chapter-16.md 完成，check_bilingual 通过
- 2026-09-24 11:46｜批次3直启子代理｜chapter-17.md 完成，check_bilingual 通过
- 2026-09-24 11:53｜批次3直启子代理｜chapter-18.md 完成，check_bilingual 通过
- 2026-09-24 12:00｜批次3直启子代理｜chapter-19.md 完成，check_bilingual 通过
- 2026-09-24 12:10｜批次3直启子代理｜chapter-20.md 完成，check_bilingual 通过
- 2026-09-24 12:21｜批次3直启子代理｜chapter-21.md 完成，check_bilingual 通过

- 2026-09-24 12:22｜批次3直启子代理｜dedication.md 完成，check_bilingual 通过
- 2026-09-24 12:23｜批次3直启｜全书完结流转：22/22 章全部 done（含 [1301] 免责重派 1 章），认领锁已删除，移交审核阶段。
