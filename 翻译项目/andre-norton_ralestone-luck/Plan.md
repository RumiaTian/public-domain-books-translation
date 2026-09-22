# Plan.md

---

## 本计划信息

- **项目名称**：andre-norton_ralestone-luck（《雷尔斯通的运气》Ralestone Luck，Andre Norton，1939）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇，20 篇，约 332KB；每篇由子代理按「翻译计划模板执行步骤」9 步完成）

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
01-dedication.md,0.1,todo
03-the-ralestones-come-home.md,21.4,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `03-the-ralestones-come-home.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，委派模式下由子代理逐篇执行）

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

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节（标记成对、标题合并「英文 / 中文」、不跳过不缩写、UTF-8 无 BOM）。此处不重复。

**本流程专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物/语气/风格全文一致（文学类尤其重要），照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。

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
- ② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 那一行（`WORKFLOW.md`「双写状态」）。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单（见 `WORKFLOW.md`「委派模式调度循环」）。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 献词 | 01-dedication.md | 0.1KB | todo |
| 2 | 题词 | 02-epigraph.md | 0.3KB | todo |
| 3 | 第一章 雷尔斯通姐弟返乡 | 03-the-ralestones-come-home.md | 21.4KB | todo |
| 4 | 第二章 洛恩领主们的家运 | 04-the-luck-of-the-lords-of-lorne.md | 20.0KB | todo |
| 5 | 第三章 雷尔斯通家宴客，来客不显眼 | 05-the-ralestones-entertain-an-unobtrusive-visitor.md | 21.5KB | todo |
| 6 | 第四章 双人用枪，一人喝咖啡 | 06-pistols-for-two-coffee-for-one.md | 20.2KB | todo |
| 7 | 第五章 房客发现雷尔斯通一家 | 07-their-tenant-discovers-the-ralestones.md | 19.9KB | todo |
| 8 | 第六章 撒旦出猎，闲人得活 | 08-satan-goes-a-hunting-and-finds-work-for-idle-hands.md | 19.1KB | todo |
| 9 | 第七章 凭我家运 | 09-by-our-luck.md | 19.0KB | todo |
| 10 | 第八章 里克老叔祖行走长厅 | 10-great-uncle-rick-walks-the-hall.md | 19.1KB | todo |
| 11 | 第九章 一位女士与一位绅士的画像 | 11-portrait-of-a-lady-and-a-gentleman.md | 18.9KB | todo |
| 12 | 第十章 深入沼泽 | 12-into-the-swamp.md | 17.8KB | todo |
| 13 | 第十一章 雷尔斯通全家救援 | 13-ralestones-to-the-rescue.md | 18.3KB | todo |
| 14 | 第十二章 雷尔斯通家带回不情愿的客人 | 14-the-ralestones-bring-home-a-reluctant-guest.md | 16.6KB | todo |
| 15 | 第十三章 在这样一个夜晚 | 15-on-such-a-night-as-this.md | 20.1KB | todo |
| 16 | 第十四章 海盗的路是隐秘的路 | 16-pirate-ways-are-hidden-ways.md | 19.4KB | todo |
| 17 | 第十五章 八里亚尔银币——雷尔斯通的命运 | 17-pieces-of-eight-ralestones-fate.md | 13.0KB | todo |
| 18 | 第十六章 雷尔斯通一家同心协力 | 18-ralestones-stand-together.md | 19.5KB | todo |
| 19 | 第十七章 里克·雷尔斯通归来 | 19-the-return-of-rick-ralestone.md | 18.6KB | todo |
| 20 | 第十八章 鲁珀特带回他的侯爵夫人 | 20-rupert-brings-home-his-marchioness.md | 8.7KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
