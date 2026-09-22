# 翻译计划：tanizaki-junichiro_short-fiction_various-translators

## 本计划信息

- **项目名称**：tanizaki-junichiro_short-fiction_various-translators（谷崎润一郎短篇集：刺青／杀阿艳／白狐之汤）
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
00-foreword.md,0.3,todo
01-tattooing.md,17.7,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-tattooing.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> 本项目内容形态为**短篇集**，执行模式为**委派**：主 agent 只当调度员，每篇的 9 步下沉到一次性子代理执行（见 `WORKFLOW.md`「委派模式调度循环」与「子代理简报」）。

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
- 严守术语表：遇表内源词必译为指定译法（专名还原日文汉字）。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物/语气/风格全文一致（文学类尤其重要），照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节：本项目 02-a-springtime-case.md（约 157KB）须分段连续译完单文件，不拆文件、不中途截断。

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
| 1 | 前言（Foreword） | 00-foreword.md | 0.3KB | done |
| 2 | 刺青（Tattooing） | 01-tattooing.md | 17.7KB | done |
| 3 | 杀阿艳（A Springtime Case） | 02-a-springtime-case.md | 157.4KB | done |
| 4 | 白狐之汤（The White Fox） | 03-the-white-fox.md | 42.2KB | done |
| 5 | 尾注（Endnotes） | 04-endnotes.md | 4.0KB | done |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-21 | 00-foreword.md | done | check_bilingual 通过；译者名 Ijichi Sumimasa 按推定作「伊地智巽正」，Iwadō Z. Tamotsu 从术语表作「岩堂全智」 |
| 2026-08-21 | 01-tattooing.md | done | check_bilingual 通过（20 对块）；新词妲己／纣王／《牺牲》／备后表／襦袢／琉球朱／氯仿等已定译，首现附原文；原文中的 Hirakiyo 按术语表统一作「平清」 |
| 2026-08-21 | 02-a-springtime-case.md | done | 断点恢复：在盘完整文件取证回收（157.4KB 源文，123 对块，结构契约满足；check_bilingual 5 处数字锚点为脚注编号假阳性），主代理代校验后双写 done |
| 2026-08-22 | 03-the-white-fox.md | done | check_bilingual 通过（49 对块，退出码 0）；角色名行保留英文原词，舞台指示译作（……）圆括号提示；新词千岁屋（Chitoseya）／阿六（Oroku-san）／中村（Nakamura）裁缝店／凯利公司（Kelly & Co.）已定译，狐狸叫声 Kon, Kon, Kon 拟作「吭、吭、吭」，L.C. 舞台方位术语照搬 |
| 2026-08-22 | 04-endnotes.md | done | check_bilingual 通过（3 对块，退出码 0）；17 条尾注编号与 ↩︎ 回返符原样保留，注 7／12 数字锚点（10 点／9 点／1825）以数字直保留通过启发式校验；术语（町、殿、两、盂兰盆、旗本、清酒、三味线、河东节）按术语表回译。全书 5 篇全部完成 |
