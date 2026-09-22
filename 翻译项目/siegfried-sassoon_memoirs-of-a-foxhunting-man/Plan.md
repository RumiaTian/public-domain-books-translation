# Plan.md — siegfried-sassoon_memoirs-of-a-foxhunting-man

## 本计划信息

- **项目名称**：siegfried-sassoon_memoirs-of-a-foxhunting-man（《一个猎狐人的回忆》）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（10 章） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 篇目清单

| # | 章名 | 源文 | 大小 | 长文分段 | 状态 |
|---|------|------|------|----------|------|
| 1 | I — Early Days | chapter-1.md | 75.2KB | 分 2-3 段 | todo |
| 2 | II — The Flower Show Match | chapter-2.md | 44.5KB | - | todo |
| 3 | III — A Fresh Start | chapter-3.md | 71.4KB | 分 2-3 段 | todo |
| 4 | IV — A Day with the Potford | chapter-4.md | 30.1KB | - | todo |
| 5 | V — At the Rectory | chapter-5.md | 52.5KB | 分 2 段 | todo |
| 6 | VI — The Colonel's Cup | chapter-6.md | 61.0KB | 分 2 段 | todo |
| 7 | VII — Denis Milden as Master | chapter-7.md | 52.7KB | 分 2 段 | todo |
| 8 | VIII — Migration to the Midlands | chapter-8.md | 36.4KB | - | todo |
| 9 | IX — In the Army | chapter-9.md | 52.2KB | 分 2 段 | todo |
| 10 | X — At the Front | chapter-10.md | 78.9KB | 分 2-3 段 | todo |

> 第 1、3、5、6、7、9、10 章超 50KB，翻译时按通用翻译引擎第七节分 2-3 段（断点选 `###` 小节边界或 `---` 分隔线），用 sed -n 切分到临时文件分别翻译，最后 cat 合并，检查衔接处完整。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-13 | 建项目 | — | 10 章提取完成，领域=小说文学，内容形态=中篇（10 章单一回忆录弧）→ 执行模式=连续；术语表初版约 100 词条（猎狐/马术域词 + 舍尔斯顿三部曲共享人物地名军语 + 第十章一战术语），与姊妹篇《一个步兵军官的回忆》严格对齐译名 |
