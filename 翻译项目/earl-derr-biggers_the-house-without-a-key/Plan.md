# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：earl-derr-biggers_the-house-without-a-key（《没有钥匙的房子》）
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
01-dedication.md,0.1,todo
02-kona-weather.md,27.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `02-kona-weather.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为「长篇」→ **委派模式**，由子代理逐篇执行本流程。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md（如无则跳过）
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
- 人物/语气/风格全文一致（文学类尤其重要），照黄金样本风格译；陈查理对白腔调见项目说明备注。
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

| # | 篇名 | 源文 | 状态 |
|---|------|------|------|
| 1 | 献词 | 01-dedication.md | todo |
| 2 | 一 科纳天气 | 02-kona-weather.md | todo |
| 3 | 二 高顶帽 | 03-the-high-hat.md | todo |
| 4 | 三 俄罗斯山午夜 | 04-midnight-on-russian-hill.md | todo |
| 5 | 四 蒂姆的朋友 | 05-a-friend-of-tim-s.md | todo |
| 6 | 五 温特斯利普家的血 | 06-the-blood-of-the-winterslips.md | todo |
| 7 | 六 竹幕彼端 | 07-beyond-the-bamboo-curtain.md | todo |
| 8 | 七 陈查理登场 | 08-enter-charlie-chan.md | todo |
| 9 | 八 轮船到港日 | 09-steamer-day.md | todo |
| 10 | 九 在礁石棕榈旅馆 | 10-at-the-reef-and-palm.md | todo |
| 11 | 十 愤怒中撕碎的报纸 | 11-a-newspaper-ripped-in-anger.md | todo |
| 12 | 十一 珠宝之树 | 12-the-tree-of-jewels.md | todo |
| 13 | 十二 贩奴者汤姆·布雷德 | 13-tom-brade-the-blackbirder.md | todo |
| 14 | 十三 十九号房间的行李 | 14-the-luggage-in-room-nineteen.md | todo |
| 15 | 十四 考赫拉带来之物 | 15-what-kaohla-carried.md | todo |
| 16 | 十五 印度来客 | 16-the-man-from-india.md | todo |
| 17 | 十六 科佩船长归来 | 17-the-return-of-captain-cope.md | todo |
| 18 | 十七 檀香山夜生活 | 18-night-life-in-honolulu.md | todo |
| 19 | 十八 本土来电 | 19-a-cable-from-the-mainland.md | todo |
| 20 | 十九 「再见，皮特！」 | 20-goodbye-pete.md | todo |
| 21 | 二十 刘何的故事 | 21-the-story-of-lau-ho.md | todo |
| 22 | 二十一 石墙崩塌 | 22-the-stone-walls-crumble.md | todo |
| 23 | 二十二 光透进来 | 23-the-light-streams-through.md | todo |
| 24 | 二十三 十字路口的月光 | 24-moonlight-at-the-crossroads.md | todo |

（状态以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
