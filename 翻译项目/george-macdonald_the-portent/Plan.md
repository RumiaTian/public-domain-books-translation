# 翻译计划（《预兆》——乔治·麦克唐纳）

## 本计划信息

- **项目名称**：《预兆》（George MacDonald, *The Portent*, 1864）
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

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本内容形态为「长篇」，走委派模式，每篇下沉到一次性子代理执行。

## 篇目清单

共 27 章，按 spine 顺序（罗马数字 I–XXVII）。详见 `translation_queue.csv`。

| # | 章 | 源文 | 大小 | 状态 |
|---|----|------|------|------|
| I | My Boyhood | chapter-1.md | 7.9KB | todo |
| II | The Second Hearing | chapter-2.md | 6.5KB | todo |
| III | My Old Nurses Story | chapter-3.md | 26.8KB | todo |
| IV | Hilton Hall | chapter-4.md | 6.4KB | todo |
| V | Lady Alice | chapter-5.md | 5.9KB | todo |
| VI | My Quarters | chapter-6.md | 5.5KB | todo |
| VII | The Library | chapter-7.md | 5.7KB | todo |
| VIII | The Somnambulist | chapter-8.md | 4.7KB | todo |
| IX | The First Waking | chapter-9.md | 6.4KB | todo |
| X | Love and Power | chapter-10.md | 11.3KB | todo |
| XI | A New Pupil | chapter-11.md | 7.6KB | todo |
| XII | Confession | chapter-12.md | 6.2KB | todo |
| XIII | Questioning | chapter-13.md | 3.7KB | todo |
| XIV | Jealousy | chapter-14.md | 3.6KB | todo |
| XV | The Chamber of Ghosts | chapter-15.md | 8.8KB | todo |
| XVI | The Clanking Shoe | chapter-16.md | 12.2KB | todo |
| XVII | The Physician | chapter-17.md | 7.6KB | todo |
| XVIII | Old Friends | chapter-18.md | 3.9KB | todo |
| XIX | Old Constancy | chapter-19.md | 4.6KB | todo |
| XX | Margaret | chapter-20.md | 20.3KB | todo |
| XXI | Hilton | chapter-21.md | 6.6KB | todo |
| XXII | The Sleeper | chapter-22.md | 8.0KB | todo |
| XXIII | My Old Room | chapter-23.md | 8.0KB | todo |
| XXIV | Prison-Breaking | chapter-24.md | 6.4KB | todo |
| XXV | New Entrenchments | chapter-25.md | 7.2KB | todo |
| XXVI | Escape | chapter-26.md | 7.6KB | todo |
| XXVII | Freedom | chapter-27.md | 3.3KB | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-12 | chapter-1/2/3 (7.9+6.5+26.8KB) | done ×3 | check_bilingual exit 0; 新词待补:Elsie/Novalis/fere/blaeberry 等 |
| 2026-08-12 | chapter-4/5/6 (6.4+5.9+5.5KB) | done ×3 | exit 0; 新词:Dryad=德律阿得斯, Mrs.Wilson=威尔逊太太 |
| 2026-08-12 | chapter-7/8/9 (5.7+4.7+6.4KB) | done ×3 | exit 0; 新词:Chaucer/George Herbert/somnambulist=梦游者/plaid=格子呢披肩 |
| 2026-08-12 | chapter-10/11/12 (11.3+7.6+6.2KB) | done ×3 | exit 0; 新词:Euclid/Spenser/Annie/Lochroyan/Love Gregory |
| 2026-08-12 | chapter-13/14/15 (3.7+3.6+8.8KB) | done ×3 | exit 0 |
| 2026-08-12 | chapter-16/17/18 (12.2+7.6+3.9KB) | done ×3 | exit 0 |
| 2026-08-12 | chapter-19/20/21 (4.6+20.3+6.6KB) | done ×3 | exit 0 |
| 2026-08-12 | chapter-22/23/24 (8.0+8.0+6.4KB) | done ×3 | exit 0 |
| 2026-08-12 | chapter-25/26/27 (7.2+7.6+3.3KB) | done ×3 | exit 0 | **全书 27/27 译完** |
