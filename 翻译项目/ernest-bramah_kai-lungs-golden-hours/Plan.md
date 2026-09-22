# Plan.md — ernest-bramah_kai-lungs-golden-hours

## 本计划信息

- **项目名称**：ernest-bramah_kai-lungs-golden-hours（《凯龙的黄金时光》）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态／执行模式**：中篇／连续（主 agent 直译，逐篇推进）

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
00-preface.md,8.0,todo
01-the-encountering-of-six-within-a-wood.md,15.2,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-the-encountering-of-six-within-a-wood.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

## 执行步骤（agent 按此推进）

> 本项目为**连续模式**：主 agent 在自身上下文内逐篇执行以下 9 步，译完一篇继续下一篇，保跨章连贯。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（作为风格黄金样本，照此风格译；无则跳过）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节（标记成对、标题合并「英文 / 中文」、不跳过不缩写、UTF-8 无 BOM）。

**本项目专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断（第 12 章为全书结局）。
- 严守术语表；表外人名地名按「汉字还原＋首现附原文」策略，全书统一。
- 保留佯装典雅的敬谦夸饰与格言腔（浅文言），这是全书风格命脉；人名语气前后一致。
- 超过 50KB 的章（03/08/09/10/12）按通用翻译引擎第七节分段处理。

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
结构契约满足则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
`status` 从 `doing` 改 `done`，改两处：
- ① 项目 `translation_queue.csv` 该行；
- ② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 那一行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done` 或上下文将满。

## 篇目清单

| # | 篇名 | 大小 | 状态 |
|---|------|------|------|
| 0 | Preface（贝洛克序） | 8.0KB | todo |
| 1 | I. The Encountering of Six Within a Wood | 15.2KB | todo |
| 2 | II. The Inexorable Justice of the Mandarin Shan Tien | 45.2KB | todo |
| 3 | III. The Degraded Persistence of the Effete Ming-Shu | 53.6KB | todo |
| 4 | IV. The Inopportune Behaviour of the Covetous Li-Loe | 16.1KB | todo |
| 5 | V. The Timely Intervention of the Mandarin Shan Tien's Lucky Day | 36.4KB | todo |
| 6 | VI. The High-Minded Strategy of the Amiable Hwa-Mei | 33.4KB | todo |
| 7 | VII. Not Concerned with Any Particular Attribute of Those Who Are Involved | 37.6KB | todo |
| 8 | VIII. The Timely Disputation Among Those of an Inner Chamber of Yu-Ping | 54.0KB | todo |
| 9 | IX. The Propitious Dissension Between Two Whose General Attributes… | 52.7KB | todo |
| 10 | X. The Incredible Obtuseness of Those Who Had Opposed the Virtuous Kai Lung | 58.2KB | todo |
| 11 | XI. Of Which It Is Written: "In Shallow Water Dragons…" | 10.8KB | todo |
| 12 | XII. The Out-Passing Into a State of Assured Felicity of the Much-Enduring Two… | 59.2KB | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
