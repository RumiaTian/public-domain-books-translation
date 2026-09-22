# 翻译计划（phillis-wheatley_poems-on-various-subjects-religious-and-moral）

## 本计划信息

- **项目名称**：phillis-wheatley_poems-on-various-subjects-religious-and-moral（Poems On Various Subjects Religious And Moral）
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

共 5 篇，见 `translation_queue.csv`（合计 102KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-22 | 全部 5 篇 | done | 一代理批译（0.3+0.9+1.0+99.8+0.4KB，诗集主体 99.8KB 按 §7 分 10 段合并，39 首诗 1770 行逐行对照零缺失，均 exit 0）。全书 5/5（100%）收官 |
