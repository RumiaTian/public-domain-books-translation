# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：anna-katharine-green_a-strange-disappearance《离奇失踪案》
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇，20 章约 328KB，子代理逐篇译）

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
01-a-novel-case.md,10.8,todo
02-a-few-points.md,17.6,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-a-novel-case.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：委派模式由子代理逐篇执行本流程；连续模式（中篇）由主 agent 自己执行。无论谁执行，这 9 步不变。

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

| # | 篇名（原文章节） | 源文 | 状态 |
|---|------|------|------|
| 1 | I A Novel Case 一桩新奇案件 | 01-a-novel-case.md | todo |
| 2 | II A Few Points 几处疑点 | 02-a-few-points.md | todo |
| 3 | III The Contents of a Bureau Drawer 写字柜抽屉里的东西 | 03-the-contents-of-a-bureau-drawer.md | todo |
| 4 | IV Thompson's Story 汤普森的故事 | 04-thompson-s-story.md | todo |
| 5 | V A New York Belle 纽约名媛 | 05-a-new-york-belle.md | todo |
| 6 | VI A Bit of Calico 一块印花布 | 06-a-bit-of-calico.md | todo |
| 7 | VII The House at the Granby Cross Roads 格兰比十字路口的宅子 | 07-the-house-at-the-granby-cross-roads.md | todo |
| 8 | VIII A Word Overheard 偶闻一言 | 08-a-word-overheard.md | todo |
| 9 | IX A Few Golden Hairs 几根金发 | 09-a-few-golden-hairs.md | todo |
| 10 | X The Secret of Mr. Blake's Studio 布莱克书房之秘 | 10-the-secret-of-mr-blake-s-studio.md | todo |
| 11 | XI Luttra 卢特拉 | 11-luttra.md | todo |
| 12 | XII A Woman's Love 女人的爱 | 12-a-woman-s-love.md | todo |
| 13 | XIII A Man's Heart 男人的心 | 13-a-man-s-heart.md | todo |
| 14 | XIV Mrs. Daniels 丹尼尔斯太太 | 14-mrs-daniels.md | todo |
| 15 | XV A Confab 一席密谈 | 15-a-confab.md | todo |
| 16 | XVI The Mark of the Red Cross 红十字记号 | 16-the-mark-of-the-red-cross.md | todo |
| 17 | XVII The Capture 擒获 | 17-the-capture.md | todo |
| 18 | XVIII Love and Duty 爱与责任 | 18-love-and-duty.md | todo |
| 19 | XIX Explanations 解谜 | 19-explanations.md | todo |
| 20 | XX The Bond That Unites 结缡之盟 | 20-the-bond-that-unites.md | todo |

（精确大小与状态以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-31 | 全书 20 章（I–XX） | 完成 20/20 | 批次1三段并行（91.9/91.4/90.8KB）零[1301]零[1308]；20 件全量过检零告警；07/10/11/12 四章流式分批落盘；漂移3处终验统一（伊芙琳、布卢姆街、舍恩马克父子）；种子勘误2处（Blake 实名 Holman 非 Everett、Schoenmakers 实为父子非兄弟——代理以源文为准自行纠正）；ch12 源文引号瑕疵镜像；ch17 法文引语双语并陈 |
