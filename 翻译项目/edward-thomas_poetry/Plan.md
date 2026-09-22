# 翻译计划（edward-thomas_poetry）

## 本计划信息

- **项目名称**：edward-thomas_poetry（Poetry）
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

共 2 篇，见 `translation_queue.csv`（合计 162KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-23 | poetry / endnotes | done | 一代理批译（162.0+0.1KB，138 首诗逐首对照、行数与分节程序化校验 138/138 通过，§7 分 14 段合并，均 exit 0）。全书 2/2（100%）收官 |
| 2026-08-24 | poetry / endnotes | done（复核） | 派单快照过期（称 2 篇 todo，实际已 done）。本次仅复核未重译：check_bilingual 均 exit 0（138 对 + 1 对）；138 首标题全覆盖、逐行对齐、分节空行同位、末尾无截断；「March the Third¹」上标锚点差异为核对脚本误报，非缺失 |
