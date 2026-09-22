# Plan.md — wilkie-collins_the-haunted-hotel

## 本计划信息

- **项目名称**：wilkie-collins_the-haunted-hotel（闹鬼的旅馆（Wilkie Collins: The Haunted Hotel, 1879））
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
| `原文/*.md` | 源文（34 文件） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`「执行步骤」9 步推进。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | chapter-1 | chapter-1.md | 9.8KB | todo |
| 2 | part-1 | part-1.md | 0.0KB | todo |
| 3 | chapter-2 | chapter-2.md | 12.8KB | todo |
| 4 | part-2 | part-2.md | 0.0KB | todo |
| 5 | chapter-3 | chapter-3.md | 13.8KB | todo |
| 6 | part-3 | part-3.md | 0.0KB | todo |
| 7 | chapter-4 | chapter-4.md | 15.9KB | todo |
| 8 | part-4 | part-4.md | 0.0KB | todo |
| 9 | chapter-5 | chapter-5.md | 15.9KB | todo |
| 10 | chapter-6 | chapter-6.md | 14.0KB | todo |
| 11 | chapter-7 | chapter-7.md | 5.4KB | todo |
| 12 | chapter-8 | chapter-8.md | 19.4KB | todo |
| 13 | chapter-9 | chapter-9.md | 5.1KB | todo |
| 14 | chapter-10 | chapter-10.md | 10.1KB | todo |
| 15 | chapter-11 | chapter-11.md | 11.1KB | todo |
| 16 | chapter-12 | chapter-12.md | 16.6KB | todo |
| 17 | chapter-13 | chapter-13.md | 12.6KB | todo |
| 18 | chapter-14 | chapter-14.md | 7.8KB | todo |
| 19 | chapter-15 | chapter-15.md | 8.3KB | todo |
| 20 | chapter-16 | chapter-16.md | 4.9KB | todo |
| 21 | chapter-17 | chapter-17.md | 15.6KB | todo |
| 22 | chapter-18 | chapter-18.md | 8.0KB | todo |
| 23 | chapter-19 | chapter-19.md | 15.9KB | todo |
| 24 | chapter-20 | chapter-20.md | 16.6KB | todo |
| 25 | chapter-21 | chapter-21.md | 13.8KB | todo |
| 26 | chapter-22 | chapter-22.md | 13.8KB | todo |
| 27 | chapter-23 | chapter-23.md | 13.6KB | todo |
| 28 | chapter-24 | chapter-24.md | 13.2KB | todo |
| 29 | chapter-25 | chapter-25.md | 13.4KB | todo |
| 30 | chapter-26 | chapter-26.md | 23.7KB | todo |
| 31 | chapter-27 | chapter-27.md | 7.4KB | todo |
| 32 | chapter-28 | chapter-28.md | 10.4KB | todo |
| 33 | dedication | dedication.md | 0.1KB | todo |
| 34 | epilogue | epilogue.md | 4.6KB | todo |

---

## 运行日志

| 日期 | 事件 | 备注 |
|------|------|------|
| 2026-08-17 | 建项目 | epub 提取 34 篇，术语表初版建成 |
| 2026-09-10 | 全书 34 篇（献词+4部分+28章+尾声） | 整书完结 | 批次4委派模式：10 个并发子代理译完（353.6KB 哥特悬疑小说）；34/34 done，check_bilingual 结构契约 0 违规（非零退出码均为年份/时间数字本地化改写型锚点误报）；无 doing 残留、无失败重试；新定名（斯蒂芬·韦斯特威克、布鲁诺医生、女像柱室等）已回填术语表。 |
