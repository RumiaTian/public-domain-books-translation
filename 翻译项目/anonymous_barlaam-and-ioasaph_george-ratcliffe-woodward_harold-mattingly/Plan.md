# 翻译计划：Barlaam and Ioasaph（巴拉阿姆与约阿萨弗）

## 本计划信息

- **项目名称**：anonymous_barlaam-and-ioasaph_george-ratcliffe-woodward_harold-mattingly
- **书名**：*Barlaam and Ioasaph*（《巴拉阿姆与约阿萨弗》，Woodward & Mattingly 英译）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态**：长篇（43 篇）→ 执行模式：委派

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置 | 建项目时定稿 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | 翻译 agent |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done（双写根表） |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | 翻译 agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。委派模式下由子代理逐篇执行，主 agent 调度。

---

## 篇目清单

阅读顺序 = 文件名数字前缀顺序（罗马数字章名已加 00-42 前缀防乱序）。

| # | 篇名 | 源文 |
|---|------|------|
| 1 | Preface（译者序） | 00-preface.md |
| 2 | Introduction（导言） | 01-introduction.md |
| 3 | 章 I | 02-i.md |
| 4 | 章 II | 03-ii.md |
| 5 | 章 III | 04-iii.md |
| 6 | 章 IV | 05-iv.md |
| 7 | 章 V | 06-v.md |
| 8 | 章 VI | 07-vi.md |
| 9 | 章 VII | 08-vii.md |
| 10 | 章 VIII | 09-viii.md |
| 11 | 章 IX | 10-ix.md |
| 12 | 章 X | 11-x.md |
| 13 | 章 XI | 12-xi.md |
| 14 | 章 XII | 13-xii.md |
| 15 | 章 XIII | 14-xiii.md |
| 16 | 章 XIV | 15-xiv.md |
| 17 | 章 XV | 16-xv.md |
| 18 | 章 XVI | 17-xvi.md |
| 19 | 章 XVII | 18-xvii.md |
| 20 | 章 XVIII | 19-xviii.md |
| 21 | 章 XIX | 20-xix.md |
| 22 | 章 XX | 21-xx.md |
| 23 | 章 XXI | 22-xxi.md |
| 24 | 章 XXII | 23-xxii.md |
| 25 | 章 XXIII | 24-xxiii.md |
| 26 | 章 XXIV | 25-xxiv.md |
| 27 | 章 XXV | 26-xxv.md |
| 28 | 章 XXVI | 27-xxvi.md |
| 29 | 章 XXVII | 28-xxvii.md |
| 30 | 章 XXVIII | 29-xxviii.md |
| 31 | 章 XXIX | 30-xxix.md |
| 32 | 章 XXX | 31-xxx.md |
| 33 | 章 XXXI | 32-xxxi.md |
| 34 | 章 XXXII | 33-xxxii.md |
| 35 | 章 XXXIII | 34-xxxiii.md |
| 36 | 章 XXXIV | 35-xxxiv.md |
| 37 | 章 XXXV | 36-xxxv.md |
| 38 | 章 XXXVI | 37-xxxvi.md |
| 39 | 章 XXXVII | 38-xxxvii.md |
| 40 | 章 XXXVIII | 39-xxxviii.md |
| 41 | 章 XXXIX | 40-xxxix.md |
| 42 | 章 XL | 41-xl.md |
| 43 | Endnotes（尾注） | 42-endnotes.md |

（大小与状态以 `translation_queue.csv` 为准）

---

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
