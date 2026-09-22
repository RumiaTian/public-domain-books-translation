# 翻译计划（Plan.md）— 《彼得勋爵查看尸体》

## 本计划信息

- **项目名称**：《彼得勋爵查看尸体》（多萝西·L·塞耶斯《Lord Peter Views the Body》）
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
the-abominable-history-of-the-man-with-copper-fingers.md,41.5,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `the-abominable-history-of-the-man-with-copper-fingers.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（委派模式：子代理逐篇执行）

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
- 人物/语气/风格全文一致（文学类尤其重要），保持温西爵爷优雅做作的绅士腔调与塞耶斯的机智冷幽默，照黄金样本风格译。
- 长文（源文 >50KB，如 the-undignified-melodrama-of-the-bone-of-contention 篇 117.6KB）分段处理见通用翻译引擎第七节。

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
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单。

---

## 篇目清单

> 共 12 篇故事 + 2 个附属文件（插图目录、填字游戏答案页），依原书 spine 顺序。附中文篇名供参考，实际文件名以原文目录为准。

| # | 中文篇名 | 源文 | 大小 | 状态 |
|---|----------|------|------|------|
| 1 | 铜指男人的可怖往事 | the-abominable-history-of-the-man-with-copper-fingers.md | 41.5KB | todo |
| 2 | 涉案文章的趣闻 | the-entertaining-episode-of-the-article-in-question.md | 22.5KB | todo |
| 3 | 米利格叔叔遗嘱的迷人难题 | the-fascinating-problem-of-uncle-meleager-s-will.md | 34.1KB | todo |
| 4 | 袋中猫的离奇惨案 | the-fantastic-horror-of-the-cat-in-the-bag.md | 27.4KB | todo |
| 5 | 恶作剧者的无耻勾当 | the-unprincipled-affair-of-the-practical-joker.md | 23.8KB | todo |
| 6 | 争议之骨的失格闹剧 | the-undignified-melodrama-of-the-bone-of-contention.md | 117.6KB | todo |
| 7 | 奔跑足印的复仇故事 | the-vindictive-story-of-the-footsteps-that-ran.md | 33.3KB | todo |
| 8 | 关于品味的酒事 | the-bibulous-business-of-a-matter-of-taste.md | 28.3KB | todo |
| 9 | 龙首的博学冒险 | the-learned-adventure-of-the-dragon-s-head.md | 43.6KB | todo |
| 10 | 失窃胃脏的钓鱼闹剧 | the-piscatorial-farce-of-the-stolen-stomach.md | 42.1KB | todo |
| 11 | 无面人的未解之谜 | the-unsolved-puzzle-of-the-man-with-no-face.md | 58.6KB | todo |
| 12 | 阿里·巴巴洞穴的惊险奇谋 | the-adventurous-exploit-of-the-cave-of-ali-baba.md | 59.3KB | todo |
| 13 | 米利格叔叔遗嘱填字游戏答案 | solution-to-the-crossword-in-uncle-mealager-s-will.md | 0.1KB | todo |
| 14 | 插图目录 | list-of-illustrations.md | 1.1KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
