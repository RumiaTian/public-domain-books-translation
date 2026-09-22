# 翻译计划（Plan.md）

> 从 `prompts/翻译计划模板.md` 复制建立。执行步骤、CSV 格式以模板为准，本文件填入本书信息与篇目清单。

---

## 本计划信息

- **项目名称**：j-j-connington_the-case-with-nine-solutions（《九种解答》，J. J. Connington）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇，19 章，主 agent 调度子代理逐章执行 9 步）

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进：读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → `python scripts/check_bilingual.py` → 双写 done（项目 CSV + 根表）→ 日志。委派模式下由子代理逐章执行，简报见 `WORKFLOW.md`「子代理简报」。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 垂死的人 | 01-the-dying-man.md | ~27KB | todo |
| 2 | 隔壁的宅子 | 02-the-house-next-door.md | ~13KB | todo |
| 3 | 常春藤小屋的克林顿爵士 | 03-sir-clinton-at-ivy-lodge.md | ~29KB | todo |
| 4 | 希瑟菲尔德的罪案 | 04-the-crime-at-heatherfield.md | ~22KB | todo |
| 5 | 平房惨剧 | 05-the-bungalow-tragedy.md | ~34KB | todo |
| 6 | 九种可能的解答 | 06-the-nine-possible-solutions.md | ~23KB | todo |
| 7 | 琥珀中的苍蝇 | 07-the-fly-in-the-amber.md | ~33KB | todo |
| 8 | 哈森丁的日记 | 08-the-hassendean-journal.md | ~18KB | todo |
| 9 | 债主 | 09-the-creditor.md | ~11KB | todo |
| 10 | 情报到手 | 10-information-received.md | ~27KB | todo |
| 11 | 密码广告 | 11-the-code-advertisement.md | ~18KB | todo |
| 12 | 西尔弗代尔的遗嘱 | 12-the-silverdale-wills.md | ~27KB | todo |
| 13 | 告密者之死 | 13-the-murder-of-the-informer.md | ~21KB | todo |
| 14 | 外套 | 14-the-jacket.md | ~16KB | todo |
| 15 | 克林顿爵士的替身 | 15-sir-clinton-s-double.md | ~22KB | todo |
| 16 | 书面证据 | 16-written-evidence.md | ~22KB | todo |
| 17 | “正义”先生 | 17-mr-justice.md | ~19KB | todo |
| 18 | 贯穿的线索 | 18-the-connecting-thread.md | ~18KB | todo |
| 19 | 克林顿爵士笔记本摘录 | 19-excerpts-from-sir-clinton-s-notebook.md | ~23KB | todo |

（权威清单以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
