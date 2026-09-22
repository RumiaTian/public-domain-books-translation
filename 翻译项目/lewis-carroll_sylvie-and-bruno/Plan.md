# 翻译计划（《西尔维与布鲁诺》——刘易斯·卡罗尔）

## 本计划信息

- **项目名称**：《西尔维与布鲁诺》（Lewis Carroll, *Sylvie and Bruno*, 1889 / *Sylvie and Bruno Concluded*, 1893，Standard Ebooks 两卷合订本）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

## translation_queue.csv 格式

```
file,size_kb,status
00-volume-1.md,0.3,todo
01-preface-volume-1.md,17.7,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `02-less-bread-more-taxes.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本内容形态为「长篇」，走委派模式，每篇下沉到一次性子代理执行；简报与并发上限（≤3）见 `WORKFLOW.md`「委派模式调度循环」。

## 篇目清单

共 2 卷 × 25 章（罗马数字 I–XXV），另含卷首题辞诗 2 篇（00、27）、两卷作者序 2 篇（01、28）、卷尾尾注 1 篇（54），合计 55 个文件、约 767KB，详见 `translation_queue.csv`。

- 卷一（00–26）：题辞诗、作者序、第 I–XXV 章（Less Bread! More Taxes! → Looking Eastward）
- 卷二（27–53）：题辞诗、作者序、第 I–XXV 章（Bruno's Lessons → Life Out of Death）
- 尾注（54）：Endnotes

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
