# 翻译计划：实用神秘主义

## 本计划信息

- **项目名称**：实用神秘主义（Practical Mysticism，伊夫琳·恩德希尔）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/学术著作.md（概念/引文密集的人文专著，兼顾文学质感；粒度逐段对照）
- **内容形态**：中篇（单一操练弧线，13 文件）→ **执行模式：连续**（主 agent 直译，逐篇接续；上下文将满时按停机判据收尾，续批从 todo 接续）
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（逐段对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
00-dedication.md,0.1,todo
01-preface.md,7.5,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `03-what-is-mysticism.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（按 prompts/翻译计划模板.md 九步推进）

1. **读配置**：本 Plan.md → 项目说明.md → 术语表.md → prompts/通用翻译引擎.md → prompts/领域配置/学术著作.md → 译文/ 下任意已完成 .zh-CN.md（黄金样本；无则跳过）。
2. **取任务**：读 translation_queue.csv 取第一个 `todo`；译文已存在则直接改 `done`；否则改 `doing`。
3. **读源文**：原文/对应文件。
4. **翻译**：产出到 译文/对应文件名去.md加.zh-CN.md。逐段对照，绝不漏译、不合并、不缩写；严守术语表（默想≠默观！）；引文按术语表「引文回译」策略处理；>50KB 分段（本书各章均 <25KB，无需分段）。
5. **自检**：完整性、块对称、标题「英文 / 中文」合并、术语一致（抽查默想/默观/收敛心神/实在/生成世界 5 词）。
6. **自动检查**：`python scripts/check_bilingual.py 译文/<篇名>.zh-CN.md`。
7. **回填状态（双写）**：项目 CSV 改 `done`；根 translation_queue.csv 中 `<本项目名>,<本篇名>` 行改 `done`（根表若尚未收录本项目行，跳过根表改写）。
8. **追加日志**：本文件「运行日志」追加一行。
9. **循环**：回到步骤 2，直至全部 `done`（连续模式由主 agent 逐篇执行）。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 0 | 献词（To the Unseen Future） | 00-dedication.md | ~0KB | todo |
| 1 | 前言（Preface） | 01-preface.md | 7.5KB | todo |
| 2 | 题词（布莱克语） | 02-epigraph.md | 0.2KB | todo |
| 3 | I 何谓神秘主义 | 03-what-is-mysticism.md | 13.0KB | todo |
| 4 | II 实在世界 | 04-the-world-of-reality.md | 16.9KB | todo |
| 5 | III 神秘主义者的准备 | 05-the-preparation-of-the-mystic.md | 18.3KB | todo |
| 6 | IV 默想与收敛心神 | 06-meditation-and-recollection.md | 10.4KB | todo |
| 7 | V 自我调适 | 07-self-adjustment.md | 20.0KB | todo |
| 8 | VI 爱与意志 | 08-love-and-will.md | 14.6KB | todo |
| 9 | VII 默观的第一种形式 | 09-the-first-form-of-contemplation.md | 18.8KB | todo |
| 10 | VIII 默观的第二种形式 | 10-the-second-form-of-contemplation.md | 22.8KB | todo |
| 11 | IX 默观的第三种形式 | 11-the-third-form-of-contemplation.md | 24.1KB | todo |
| 12 | X 神秘主义的人生 | 12-the-mystical-life.md | 23.6KB | todo |

（以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
