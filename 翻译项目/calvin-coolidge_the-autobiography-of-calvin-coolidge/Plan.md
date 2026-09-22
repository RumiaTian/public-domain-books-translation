# Plan.md

## 本计划信息

- **项目名称**：calvin-coolidge_the-autobiography-of-calvin-coolidge（《卡尔文·柯立芝自传》）
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
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
01-scenes-of-my-childhood.md,32.8,todo
02-seeking-my-education.md,46.3,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-scenes-of-my-childhood.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为中篇 → **连续模式**，主 agent 在自身上下文内逐篇执行 9 步，译完一篇继续下一篇，保有跨章连贯。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（作为风格黄金样本；无则跳过）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节。章节标题保留罗马数字并合并为「英文 / 中文」。

**本项目提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：General Court = 州议会（勿译"最高法院"）；人名地名按表内统一译法。
- 语体平实简净，柯立芝式短句与格言收束，忌夸饰与口语腔。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。

### 5. 自检
完整性 / 块对称 / 标题格式 / 术语一致，不满足则改到满足。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```

### 7. 回填状态（双写）
`status` 从 `doing` 改 `done`，改两处：① 项目 CSV 该行；② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 那一行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I Scenes of My Childhood（我的童年景象） | 01-scenes-of-my-childhood.md | ~33KB | todo |
| 2 | II Seeking My Education（求学） | 02-seeking-my-education.md | ~46KB | todo |
| 3 | III The Law and Politics（法律与政治） | 03-the-law-and-politics.md | ~60KB | todo |
| 4 | IV In National Politics（进入全国政坛） | 04-in-national-politics.md | ~30KB | todo |
| 5 | V On Entering and Leaving the Presidency（就任与离任总统） | 05-on-entering-and-leaving-the-presidency.md | ~22KB | todo |
| 6 | VI Some of the Duties of the President（总统的某些职责） | 06-some-of-the-duties-of-the-president.md | ~45KB | todo |
| 7 | VII Why I Did Not Choose to Run（我为何不再竞选） | 07-why-i-did-not-choose-to-run.md | ~9KB | todo |

---

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-17 | 03 译完 | 法律与政治 59.6KB（34对块，州议会/市议会等政制术语遵表，塔夫特/冈珀斯等新词全章统一，未并发写术语表由主代理回填），exit 0、0 错配。01/02 派发两度模型超时，重派中 |
| 2026-08-17 | 全书译完 7/7 | 01 童年场景（27对块，黄金样本）/ 02 求学（23对块）/ 04 全国政治（16对块）/ 05 入主与卸任（20对块）/ 06 总统的若干职责（17对块）/ 07 我为何不再竞选（12对块，终章），全部 exit 0、0 错配、逐段程序化核验一致；术语表累计补 60+ 条（政制词/人名/白宫厅室）。新英格兰式简洁克制文体全章统一。01/02 首两派模型超时，第三次派发成功 |
