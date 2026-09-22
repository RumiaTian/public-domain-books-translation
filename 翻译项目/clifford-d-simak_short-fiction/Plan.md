# Clifford D. Simak《Short Fiction》翻译计划

本文件是本项目的翻译执行入口。任务清单（篇目 + 状态）在同目录的 `translation_queue.csv`，翻译须知在 `术语表.md` + `prompts/` 体系。要推进翻译，读本文件即可，无需手动指定篇名。

---

## 本计划信息

- **项目名称**：clifford-d-simak_short-fiction
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
| `术语表.md` | 翻译硬约束层（各篇人物/地名/虚构生物植物/科幻概念词）。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一篇，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（已从 epub 转换） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 字段说明

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `message-from-mars.md` |
| `size_kb` | 源文大小（KB），>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，委派模式由子代理逐篇执行）

### 1. 读配置（每次翻译前必读）
```
1. 翻译项目/clifford-d-simak_short-fiction/项目说明.md
2. 翻译项目/clifford-d-simak_short-fiction/术语表.md
3. prompts/通用翻译引擎.md
4. prompts/领域配置/小说文学.md
5. 翻译项目/clifford-d-simak_short-fiction/译文/ 下任意已完成 .zh-CN.md  ← 风格黄金样本（无则跳过）
6. 前一篇末尾 2-3 段原文+译文（衔接上下文；首篇无此项）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：已存在→直接改 `done` 跳到步骤 8；不存在→把该行改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`（如 `原文/message-from-mars.md` → `译文/message-from-mars.zh-CN.md`）。

**格式**：块对照双语。
```
## 英文标题 / 中文标题

===Original===
英文原文段落（可连续数段）

===Chinese===
中文译文段落

===Original===
...
```

**关键约束**：
- 标记 `===Original===` / `===Chinese===` 独占一行，成对出现。
- 标题写成「英文 / 中文」合并一行，**不加块标记**。
- 块对照粒度：按场景或每 3-6 段一组。
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文。
- 人物语气全文一致；保留西马克质朴温厚、田园悲悯的风格。
- 文学性优先，避免翻译腔，像中文创作。
- 科学段落（维度/演化/永生论述）用通行术语，准确不口语化；缩写/编号照搬。
- 报纸/电码体裁保留原文节奏（如火星电码断句）。
- 不使用 emoji，不加元信息头。
- 长文（>50KB，本书《Hellhounds》《Second Childhood》）分 2-3 次译，断点选章节边界或空行，合并后检查衔接。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并。
- 术语一致：抽查 5 个术语词，全文译法统一。
- 不满足则改到满足。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```
结构契约满足（标记成对、标题合并格式、可疑错配少）则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
检查通过后，`status` 从 `doing` 改 `done`，改两处：
- ① 项目 `translation_queue.csv` 该行；
- ② 根 `translation_queue.csv` 中 `clifford-d-simak_short-fiction,<本篇名>` 那一行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。

---

## 篇目清单

篇目清单与进度详见同目录 `translation_queue.csv`（由 `gen_project_files.py` 按 spine 顺序生成）。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-14 | Hellhounds of the Cosmos（宇宙地狱犬） | done | 107.9KB |
| 2026-08-14 | Message from Mars（来自火星的信息） | done | 21.5KB |
| 2026-08-14 | mr-meek-musketeer (15.2KB回填) | done | exit 0; 前次中断遗留、校验通过后回填 |
| 2026-08-14 | mr-meek-plays-polo/project-mastodon/second-childhood/the-call-from-beyond/the-shipshape-miracle (7.7+6.6+35.9+12.8+20.0KB) | done ×5 | exit 0 |
| 2026-08-14 | the-street-that-wasn-t-there/the-world-that-couldn-t-be (32.6+10.4KB) | done ×2 | exit 0 | **全书 10/10 译完** |
