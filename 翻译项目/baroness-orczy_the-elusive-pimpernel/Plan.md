# 翻译计划（baroness-orczy_the-elusive-pimpernel）

## 本计划信息

- **项目名称**：baroness-orczy_the-elusive-pimpernel（The Elusive Pimpernel）
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

共 36 篇，见 `translation_queue.csv`（合计 487KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |

- 2026-10-17 | chapter-2 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-1 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-3 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-5 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-4 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-6 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-7 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-8 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-10 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-9 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-11 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-13 | 直启批次3 子代理完成 | check 通过

- 2026-10-17 | chapter-14 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-12 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-15 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-16 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-17 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-19 | 直启批次3 子代理完成 | check 通过
- 2026-10-17 | chapter-18 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-18 | 直启批次3 主Agent断点验收回填（1308 中断前已完成落盘，check 通过） | check 通过
- 2026-10-18 | chapter-21 | 直启批次3 子代理完成（1308 断点重派） | check 通过
- 2026-10-18 | chapter-22 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-20 | 直启批次3 子代理完成（1308 断点重派） | check 通过
- 2026-10-18 | chapter-24 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-23 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-25 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-27 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-28 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-26 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-29 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-31 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-30 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-32 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-33 | [1301] 内容拦截，免责前缀重派 1 次仍拦截，按规则跳过保持 todo（待换模型重试） | 直启批次3
- 2026-10-18 | chapter-34 | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | dedication | 直启批次3 子代理完成 | check 通过
- 2026-10-18 | chapter-35 | 直启批次3 子代理完成 | check 通过
