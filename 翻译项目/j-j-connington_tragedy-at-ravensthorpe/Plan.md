# 翻译计划（j-j-connington_tragedy-at-ravensthorpe）

## 本计划信息

- **项目名称**：j-j-connington_tragedy-at-ravensthorpe（Tragedy At Ravensthorpe）
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

共 15 篇，见 `translation_queue.csv`（合计 404KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-21 | chapter-1.md | done | 批次1直启，check_bilingual PASS（40 对块） |
| 2026-09-21 | chapter-2.md | done | 批次1直启，check_bilingual PASS（33 对块） |
| 2026-09-21 | chapter-3.md | done | 批次1直启，check_bilingual PASS（38 对块） |
| 2026-09-21 | chapter-4.md | done | 批次1直启，check_bilingual PASS（43 对块） |
| 2026-09-21 | chapter-5.md | done | 批次1直启，check_bilingual PASS（36 对块） |
| 2026-09-21 | chapter-6.md | done | 批次1直启，check_bilingual PASS（74 对块） |
| 2026-09-21 | chapter-7.md | done | 批次1直启，check_bilingual PASS（44 对块） |
| 2026-09-21 | chapter-8.md | done | 批次1直启，check_bilingual PASS（51 对块） |
| 2026-09-21 | chapter-9.md | done | 批次1直启，check_bilingual PASS（48 对块） |
| 2026-09-21 | chapter-10.md | done | 批次1直启，check_bilingual PASS（40 对块） |
| 2026-09-21 | chapter-11.md | done | 批次1直启，check_bilingual PASS（38 对块） |
| 2026-09-21 | chapter-12.md | done | 批次1直启，check_bilingual PASS（44 对块） |
| 2026-09-21 | chapter-13.md | done | 批次1直启，check_bilingual PASS（21 对块） |
| 2026-09-21 | chapter-14.md | done | 批次1直启，check_bilingual PASS（51 对块） |
| 2026-09-21 | chapter-15.md | done | 批次1直启，check_bilingual PASS（109 对块） |
