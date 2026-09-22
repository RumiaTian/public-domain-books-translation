# 翻译计划（Plan.md）——民主与社会伦理

> 复制自 `prompts/翻译计划模板.md`，按本项目信息填写。执行流程见模板说明及 `WORKFLOW.md`。

---

## 本计划信息

- **项目名称**：民主与社会伦理（jane-addams_democracy-and-social-ethics）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/学术著作.md
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
| `译文/*.zh-CN.md` | 译文产出（逐段对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
3-charitable-effort.md,56.0,todo
4-filial-relations.md,29.2,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `3-charitable-effort.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为长篇 / 委派模式，由子代理逐篇执行本流程。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/学术著作.md
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
- 逐段对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 术语、概念、语气全文一致（学术著作尤其重要），照黄金样本风格译。
- 长文（源文 >50KB，本书 3、8 两章）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并；罗马数字章号照搬。
- 术语一致：抽查 5 个术语词（如 social ethics、settlement、benefactor），全文译法统一。
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
| 0 | 献词 | 0-dedication.md | 0.0KB | todo |
| 1 | 序言 | 1-prefatory-note.md | 0.6KB | todo |
| 2 | 导言 | 2-introduction.md | 10.7KB | todo |
| 3 | 慈善活动 | 3-charitable-effort.md | 56.0KB | todo |
| 4 | 代际关系 | 4-filial-relations.md | 29.2KB | todo |
| 5 | 家务调适 | 5-household-adjustment.md | 34.1KB | todo |
| 6 | 产业改良 | 6-industrial-amelioration.md | 39.1KB | todo |
| 7 | 教育方法 | 7-educational-methods.md | 41.5KB | todo |
| 8 | 政治改革 | 8-political-reform.md | 54.7KB | todo |

（以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-18 | 4-filial-relations.md（III Filial Relations 孝亲关系，29.2KB） | 完成；check_bilingual.py 退出码 0（29 对块，0 可疑错配） | 续用前一会话 .4-part1.tmp 已译 1–16 段，续译 17–29 段；术语表新增 Cordelia（考狄利娅）、St. Francis（圣方济各）、Assisi（阿西西） |
| 2026-08-18 | 5-household-adjustment.md（IV Household Adjustment 家务调适，34.1KB） | 完成；check_bilingual.py 退出码 0（45 对块，0 可疑错配，Original 块与源文逐段全等校验通过） | 三段写入后合并；术语表新增家务劳动章术语（家务劳动者／家务雇主／人身侍奉／廉租公寓／寄宿俱乐部／团体精神／癔症球／「无意识的奴役」） |
| 2026-08-18 | 6-industrial-amelioration.md（V Industrial Amelioration 产业改良，39.1KB） | 完成；check_bilingual.py 退出码 0（48 对块，0 可疑错配，Original 块由源文逐段直接拼装、全等校验通过） | 三段临时文件合并生成；术语表新增产业改良章术语（联合努力／模范城镇／非工会工厂／同情罢工／仲裁／公众信托／互济会／工厂立法／童工法／「产业改善」／公民投票）及林肯、苏黎世、俄亥俄 |
| 2026-08-18 | 7-educational-methods.md（VI Educational Methods 教育方法，41.5KB） | 完成；check_bilingual.py 退出码 0（41 对块，0 可疑错配，Original 块由源文逐段直接拼装、全等校验通过） | 三段临时文件合并生成；术语表新增教育方法章术语（包工头／雅典娜馆／机械工人讲习所／产业教育／立体幻灯／师范学校／妇女俱乐部）及代顿、君士坦丁堡、柏林、罗马、那不勒斯、卡拉布里亚、西西里等地名 |
| 2026-08-18 | 8-political-reform.md（VII Political Reform 政治改革，54.7KB） | 完成；check_bilingual.py 退出码 0（56 对块，0 可疑错配，Original 块由源文逐段直接拼装、全等校验通过） | 全书最长章，按引擎第七节四段临时文件合并生成；术语表新增政改章术语（文官制度／政治机器／改革运动／选民／特许权／市议会／贪贿者／「骗子街」／掷骰子／帮伙／老虎机／少年禁酒队／「大经验」）及密尔、查普曼；至此全书 9 篇全部完成，项目收官 |
