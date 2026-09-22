# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：edgar-wallace_the-three-just-men（《三义士》，埃德加·华莱士）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇，34 章，约 514KB；子代理逐章译，跨章连贯靠术语表+黄金样本+前章末尾补偿）

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

## translation_queue.csv 格式

```
file,size_kb,status
01-the-firm-of-oberzohn.md,18.3,todo
02-the-three-men-of-curzon-street.md,15.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-the-firm-of-oberzohn.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为长篇→委派模式，子代理逐章执行本 9 步；主 agent 只当调度员（并发 ≤3）。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（风格黄金样本；无则跳过，
   风格基准可参照 ../edgar-wallace_the-four-just-men/译文/ 同系列已完成译篇）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物/语气/风格全文一致，照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并（罗马数字照搬，见项目说明备注）。
- 术语一致：抽查 5 个术语词，全文译法统一。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```

### 7. 回填状态（双写）
`status` 从 `doing` 改 `done`，改两处：① 项目 `translation_queue.csv`；② 根 `translation_queue.csv` 对应行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，直到全部 `done`。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | The Firm of Oberzohn | 01-the-firm-of-oberzohn.md | 18.3KB | todo |
| 2 | The Three Men of Curzon Street | 02-the-three-men-of-curzon-street.md | 15.1KB | todo |
| 3 | The Vendetta | 03-the-vendetta.md | 10.1KB | todo |
| 4 | The Snake Strikes | 04-the-snake-strikes.md | 9.6KB | todo |
| 5 | The Golden Woman | 05-the-golden-woman.md | 14.6KB | todo |
| 6 | In Chester Square | 06-in-chester-square.md | 14.1KB | todo |
| 7 | “Moral Suasion” | 07-moral-suasion.md | 12.6KB | todo |
| 8 | The House of Oberzohn | 08-the-house-of-oberzohn.md | 13.6KB | todo |
| 9 | Before the Lights Went Out | 09-before-the-lights-went-out.md | 5.3KB | todo |
| 10 | When the Lights Went Out | 10-when-the-lights-went-out.md | 12.7KB | todo |
| 11 | Gurther | 11-gurther.md | 9.3KB | todo |
| 12 | Leon Theorizes | 12-leon-theorizes.md | 15.5KB | todo |
| 13 | Mirabelle Goes Home | 13-mirabelle-goes-home.md | 14.1KB | todo |
| 14 | The Pedlar | 14-the-pedlar.md | 18.9KB | todo |
| 15 | Two “Accidents” | 15-two-accidents.md | 19.2KB | todo |
| 16 | Rath Hall | 16-rath-hall.md | 33.2KB | todo |
| 17 | Written in Braille | 17-written-in-braille.md | 14.1KB | todo |
| 18 | The Story of Mont d’Or | 18-the-story-of-mont-d-or.md | 13.0KB | todo |
| 19 | At Heavytree Farm | 19-at-heavytree-farm.md | 20.3KB | todo |
| 20 | Gurther Reports | 20-gurther-reports.md | 9.0KB | todo |
| 21 | The Account Book | 21-the-account-book.md | 18.8KB | todo |
| 22 | In the Store Cellar | 22-in-the-store-cellar.md | 12.0KB | todo |
| 23 | The Courier | 23-the-courier.md | 13.2KB | todo |
| 24 | On the Night Mail | 24-on-the-night-mail.md | 15.0KB | todo |
| 25 | Gurther Returns | 25-gurther-returns.md | 10.4KB | todo |
| 26 | In Captivity | 26-in-captivity.md | 15.8KB | todo |
| 27 | Mr. Newton’s Dilemma | 27-mr-newton-s-dilemma.md | 21.0KB | todo |
| 28 | At Frater’s | 28-at-frater-s.md | 8.6KB | todo |
| 29 | Work for Gurther | 29-work-for-gurther.md | 22.2KB | todo |
| 30 | Joan a Prisoner | 30-joan-a-prisoner.md | 20.7KB | todo |
| 31 | The Things in the Box | 31-the-things-in-the-box.md | 15.6KB | todo |
| 32 | The Search | 32-the-search.md | 17.5KB | todo |
| 33 | The Siege | 33-the-siege.md | 28.0KB | todo |
| 34 | The Death Tube | 34-the-death-tube.md | 3.1KB | todo |

> 注：表中大小为建项时快照，权威以 `translation_queue.csv` 为准。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
