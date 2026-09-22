# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：ambrose-bierce_in-the-midst-of-life（安布罗斯·比尔斯《在人生中途》短篇集）
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
00-preface-to-the-first-edition.md,0.3,todo
02-a-horseman-in-the-sky.md,13.5,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 带两位序号前缀，顺序=阅读顺序 |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为短篇集，走**委派模式**，由子代理逐篇执行本 9 步；主 agent 只当调度员。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md（如无则跳过）
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md（项目说明指定）
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
- 罗马数字分节号 I/II/III 照搬不译；军衔按术语表「军语与军衔」统一。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节（本集最长篇约 25KB，无此情况）。

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
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单（见 `WORKFLOW.md`「委派模式调度循环」，并发 ≤3）。

---

## 篇目清单

| # | 篇名 | 源文 | 卷 |
|---|------|------|----|
| 00 | Preface to the First Edition / 初版序 | 00-preface-to-the-first-edition.md | — |
| 01 | Soldiers / 士兵（标题页） | 01-soldiers.md | 上卷 |
| 02 | A Horseman in the Sky / 天空中的骑者 | 02-a-horseman-in-the-sky.md | 上卷 |
| 03 | An Occurrence at Owl Creek Bridge / 鹰溪桥上 | 03-an-occurrence-at-owl-creek-bridge.md | 上卷 |
| 04 | Chickamauga / 奇克莫加 | 04-chickamauga.md | 上卷 |
| 05 | A Son of the Gods / 天神之子 | 05-a-son-of-the-gods.md | 上卷 |
| 06 | One of the Missing / 失踪者之一 | 06-one-of-the-missing.md | 上卷 |
| 07 | Killed at Resaca / 阵亡于雷萨卡 | 07-killed-at-resaca.md | 上卷 |
| 08 | The Affair at Coulter's Notch / 科尔特隘口之战 | 08-the-affair-at-coulters-notch.md | 上卷 |
| 09 | The Coup de Grâce / 致命一击 | 09-the-coup-de-grace.md | 上卷 |
| 10 | Parker Adderson, Philosopher / 哲学家帕克·艾德森 | 10-parker-adderson-philosopher.md | 上卷 |
| 11 | An Affair of Outposts / 前哨事件 | 11-an-affair-of-outposts.md | 上卷 |
| 12 | The Story of a Conscience / 一个良心的故事 | 12-the-story-of-a-conscience.md | 上卷 |
| 13 | One Kind of Officer / 某类军官 | 13-one-kind-of-officer.md | 上卷 |
| 14 | One Officer, One Man / 一官一兵 | 14-one-officer-one-man.md | 上卷 |
| 15 | George Thurston / 乔治·瑟斯顿 | 15-george-thurston.md | 上卷 |
| 16 | The Mockingbird / 反舌鸟 | 16-the-mockingbird.md | 上卷 |
| 17 | Civilians / 平民（标题页） | 17-civilians.md | 下卷 |
| 18 | The Man Out of the Nose / 鼻子里出来的人 | 18-the-man-out-of-the-nose.md | 下卷 |
| 19 | An Adventure at Brownville / 布朗维尔奇遇 | 19-an-adventure-at-brownville.md | 下卷 |
| 20 | The Famous Gilson Bequest / 有名的吉尔森遗赠 | 20-the-famous-gilson-bequest.md | 下卷 |
| 21 | The Applicant / 求职者 | 21-the-applicant.md | 下卷 |
| 22 | A Watcher by the Dead / 与死者为伴的人 | 22-a-watcher-by-the-dead.md | 下卷 |
| 23 | The Man and the Snake / 人与蛇 | 23-the-man-and-the-snake.md | 下卷 |
| 24 | A Holy Terror / 可怕的圣徒 | 24-a-holy-terror.md | 下卷 |
| 25 | The Suitable Surroundings / 合适的环境 | 25-the-suitable-surroundings.md | 下卷 |
| 26 | The Boarded Window / 钉死的窗 | 26-the-boarded-window.md | 下卷 |
| 27 | A Lady from Redhorse / 来自红马镇的女士 | 27-a-lady-from-redhorse.md | 下卷 |
| 28 | The Eyes of the Panther / 黑豹之眼 | 28-the-eyes-of-the-panther.md | 下卷 |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
