# 翻译计划（walter-s-masterman_the-wrong-letter）

## 本计划信息

- **项目名称**：walter-s-masterman_the-wrong-letter（The Wrong Letter）
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

共 18 篇，见 `translation_queue.csv`（合计 229KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-28 | 批次3整书完结（18/18） | +16 | 起自 2/18（批次1中断处）；委派子代理译完余 16 件（含 ch3/15/16 三个 20KB+ 超长章流式落盘、切斯特顿序），全书 18 文件 check 通过（ch3/preface 各 1 处数字锚点误报），术语表 40+ 条 |
