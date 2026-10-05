# 翻译计划（will-james_smoky-the-cowhorse）

## 本计划信息

- **项目名称**：will-james_smoky-the-cowhorse（Smoky The Cowhorse）
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

共 16 篇，见 `translation_queue.csv`（合计 416KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |

- 2026-10-01 07:35｜批次3直启子代理｜chapter-1.md 完成，check_bilingual 通过
- 2026-10-01 07:45｜批次3直启子代理｜chapter-2.md 完成，check_bilingual 通过
- 2026-10-01 07:50｜批次3直启子代理｜chapter-3.md 完成，check_bilingual 通过
- 2026-10-01 11:20｜批次3直启子代理｜chapter-4.md 完成，check_bilingual 通过
- 2026-10-02 06:30｜批次3直启子代理｜chapter-5.md 完成，check_bilingual 通过
- 2026-10-02 06:40｜批次3直启子代理｜chapter-6.md 完成，check_bilingual 通过
- 2026-10-02 06:48｜批次3直启子代理｜chapter-7.md 完成，check_bilingual 通过
- 2026-10-02 07:05｜批次3直启子代理｜chapter-8.md 完成，check_bilingual 通过
- 2026-10-02 07:15｜批次3直启子代理｜chapter-9.md 完成，check_bilingual 通过
- 2026-10-02 07:30｜批次3直启子代理｜chapter-10.md 完成，check_bilingual 通过

- 2026-10-02 09:02｜批次3直启子代理｜chapter-11.md 完成，check_bilingual 通过（[1308]中断后三分支审计：分支①回填，覆盖率 0 缺失）
- 2026-10-02 11:20｜批次3直启子代理｜chapter-12.md 完成，check_bilingual 通过
- 2026-10-02 11:35｜批次3直启子代理｜chapter-13.md 完成，check_bilingual 通过
- 2026-10-02 11:45｜批次3直启子代理｜chapter-14.md 完成，check_bilingual 通过

- 2026-10-02 11:55｜批次3直启子代理｜endnotes.md 完成，check_bilingual 通过（内联）

- 2026-10-02 11:56｜批次3直启子代理｜preface.md 完成，check_bilingual 通过（内联）

## 完书纪要
- 2026-10-02 11:57｜批次3直启｜全书 16/16 队列项完成（14 章+序言+尾注），check_bilingual 全部通过，锁已删除。第十七本完工。
