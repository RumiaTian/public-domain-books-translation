# Noel Loomis《Short Science Fiction》翻译计划

本文件是本项目的翻译执行入口。任务清单（篇目 + 状态）在同目录的 `translation_queue.csv`，翻译须知在 `翻译质量保障方案.md` + `术语表.md` + `prompts/` 体系。要推进翻译，读本文件即可，无需手动指定篇名。

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `翻译质量保障方案.md` | 五阶段 QA 流程（预生产→翻译→自审→自动检查→人工验收） | 人工 |
| `术语表.md` | 翻译硬约束层（人物/地名/科幻概念词）。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一篇，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（已从 epub 转换） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 字段说明

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `The-Bryd.md` |
| `size_kb` | 源文大小（KB），>20KB 为长文，按质量保障方案分段处理 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进）

### 1. 读配置（每次翻译前必读）
```
1. 翻译项目/noel-loomis_short-science-fiction/翻译质量保障方案.md
2. 翻译项目/noel-loomis_short-science-fiction/术语表.md
3. prompts/通用翻译引擎.md
4. prompts/领域配置/小说文学.md
5. 翻译项目/noel-loomis_short-science-fiction/译文/Day-s-Work.zh-CN.md  ← 风格黄金样本
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。把它改为 `doing` 并保存 CSV。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译（阶段1）
产出到 `译文/对应文件名去.md加.zh-CN.md`（如 `原文/The-Bryd.md` → `译文/The-Bryd.zh-CN.md`）。

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
- 人物语气全文一致。1940s-50s 通俗科幻腔调，对话口语化。
- 文学性优先，避免翻译腔，像中文创作。
- 罗马数字编号、技术缩写、单位符号照搬不译。
- 不使用 emoji，不加元信息头。
- 长文（>4000词）分 2-3 次译，断点选章节边界或空行，合并后检查衔接。

### 5. 自检（阶段2）
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并。
- 术语一致：抽查 5 个术语词，全文译法统一。
- 不满足则改到满足。

### 6. 自动检查（阶段3）
```
python3 scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```
结构契约满足（标记成对、标题合并格式、可疑错配少）则继续；有违规回步骤4修订。

### 7. 回填状态
检查通过后，把该行 `status` 从 `doing` 改为 `done`，保存 CSV。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。

---

## 一条命令版提示词（可整段复制给 agent）

```
翻译 Noel Loomis 科幻短篇集的下一篇。读 翻译项目/noel-loomis_short-science-fiction/Plan.md，按其中的「执行步骤」推进：读配置 → 从 translation_queue.csv 取第一个 status=todo 的篇目，改 doing → 读源文 → 按 QA 流程翻译产出到译文/ → 自检 → 跑 check_bilingual.py → 通过则改 done → 在 Plan.md 追加运行日志。一次翻译一篇，完成后停下汇报。长文（>4000词）分段处理。严守术语表，新词报回补充。
```

---

## 篇目清单

| # | 篇名 | 源文 | 词数 | 状态 |
|---|------|------|------|------|
| 1 | Day's Work | Day-s-Work.md | 2840 | done（试点，已验证） |
| 2 | Electron Eat Electron | Electron-Eat-Electron.md | 4930 | done |
| 3 | Parking, Unlimited | Parking-Unlimited.md | 3473 | done |
| 4 | The Bryd | The-Bryd.md | 4659 | todo |
| 5 | Remember the 4th! | Remember-the-4th.md | 5142 | todo |
| 6 | You Too Can Be a Millionaire | You-Too-Can-Be-a-Millionaire.md | 5875 | todo |
| 7 | Nine Men in Time | Nine-Men-in-Time.md | 5916 | todo |
| 8 | The Mischievous Typesetter | The-Mischievous-Typesetter.md | 5965 | todo |
| 9 | The Wealth of Echindul | The-Wealth-of-Echindul.md | 7094 | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-02 | Day's Work | 通过 | 试点篇，check_bilingual 退出码0，已生成双语 EPUB |
| 2026-08-02 | Electron Eat Electron | 通过 | 8对块，结构契约满足，3处数字锚点为启发式误报 |
| 2026-08-02 | Parking, Unlimited | 通过 | 8对块，结构契约满足，可疑错配0处；修了1处漏译英文词 |
| 2026-08-03 | The Bryd | 通过 | 19对块，标题合并、结构契约满足；check_bilingual.py 因环境无 Python 无法运行，改用 grep 复刻结构检查（标记成对、标题格式、无截断），通过 |
| 2026-08-03 | Remember the 4th! | 通过 | 24对块，结构契约满足；侦探题材新故事，沿用通用译法，新词首次附原文 |
| 2026-08-03 | You Too Can Be a Millionaire | 通过 | 28对块，结构契约满足；反乌托邦新故事，修了2处中文段内英文残留（bewildered/inevitably）后通过 |
| 2026-08-03 | Nine Men in Time | 通过 | 30对块，结构契约满足；印刷厂科幻新故事，修了3处Chinese标记等号缺失及1处arguments残留后通过 |
| 2026-08-03 | The Mischievous Typesetter | 通过 | 29对块，结构契约满足；高袋琼斯系列，含一段中英对照打油诗（中译4行对应英4行） |
| 2026-08-03 | The Wealth of Echindul | 通过 | 29对块，结构契约满足；金星冒险新故事，修了3处中文段英文残留（largely/bolt×2）后通过；全书9篇全部完成 |
| 2026-08-03 | （环境就绪后补跑）6篇新译文 | 通过 | winget 装好 Python 3.12.10 + 关闭 WindowsApps 别名 + 重启终端后，check_bilingual.py 实跑：6篇退出码全0，结构契约（标记成对/标题合并）全部满足；启发式可疑错配共16处，逐一核对均为数字锚点误报（日期/年份/编号在译文里保留数字，正则在中文语境匹配不到），无真实语义错配 |
