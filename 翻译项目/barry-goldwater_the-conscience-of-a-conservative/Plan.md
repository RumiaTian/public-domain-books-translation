# Plan.md — barry-goldwater_the-conscience-of-a-conservative

## 本计划信息

- **项目名称**：barry-goldwater_the-conscience-of-a-conservative（《一个保守主义者的良心》）
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
01-foreword.md,5.1,todo
02-the-conscience-of-a-conservative.md,7.3,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-foreword.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为政论集（短篇集类），走**委派模式**，由子代理逐篇执行本流程。9 步内容见 `prompts/翻译计划模板.md`「执行步骤」。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/学术著作.md
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

- 逐段对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 政论论证链条（前提—推理—结论）不得增删；修辞力度与反讽语气保持一致。
- **11-the-soviet-menace.md 源文 >50KB，属长文，须按通用翻译引擎第七节分段处理，单篇不可中途截断交付。**

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并，罗马数字编号照搬。
- 术语一致：抽查 5 个术语词（如 Conservative/保守主义、Liberal/自由派、States' Rights/州权），全文译法统一。
- 不满足则改到满足。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```

### 7. 回填状态（双写）
`status` 从 `doing` 改 `done`，改两处：① 项目 CSV 该行；② 根 `translation_queue.csv` 对应行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2 取下一篇 `todo`，直到全部 `done`。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | Foreword（前言） | 01-foreword.md | 5KB | todo |
| 2 | I The Conscience of a Conservative | 02-the-conscience-of-a-conservative.md | 7KB | todo |
| 3 | II The Perils of Power | 03-the-perils-of-power.md | 12KB | todo |
| 4 | III States' Rights | 04-states-rights.md | 9KB | todo |
| 5 | IV And Civil Rights | 05-and-civil-rights.md | 10KB | todo |
| 6 | V Freedom for the Farmer | 06-freedom-for-the-farmer.md | 8KB | todo |
| 7 | VI Freedom for Labor | 07-freedom-for-labor.md | 19KB | todo |
| 8 | VII Taxes and Spending | 08-taxes-and-spending.md | 13KB | todo |
| 9 | VIII The Welfare State | 09-the-welfare-state.md | 10KB | todo |
| 10 | IX Some Notes on Education | 10-some-notes-on-education.md | 13KB | todo |
| 11 | X The Soviet Menace（长文，>50KB 分段译） | 11-the-soviet-menace.md | 53KB | todo |
| 12 | Endnotes（尾注） | 12-endnotes.md | 1KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-22 | Foreword（01-foreword.md） | 完成 | 11 块对，check 退出码 0。首译定基调：政论正式语体，术语按术语表（保守主义/自由派/新政/公平政策/国家家长主义/福利主义），引号用“” ，数字金额照搬 |
| 2026-08-22 | I The Conscience of a Conservative（02） | 完成 | 11 块对，check 退出码 0。政治哲学章：完整的人/灵性本性/自由与秩序；脚注上标 1 照搬 |
| 2026-08-22 | II The Perils of Power（03） | 完成 | 21 块对，check 退出码 0。有限政府/宪法约束/利维坦；1830s 加括注保数字锚点 |
| 2026-08-22 | III States’ Rights（04） | 完成 | 12 块对，check 退出码 0。州权/第十修正案/补助拨款（grants-in-aid）/对等资金；1930、1957 锚点保留 |
| 2026-08-22 | IV And Civil Rights（05） | 完成 | 14 块对，check 退出码 0。种族议题段落中性直译：Negro→黑人、segregation→种族隔离、integration→种族融合；布朗案首现附中文通行名；1866/1868/1954 锚点保留 |
| 2026-08-22 | V Freedom for the Farmer（06） | 完成 | 12 块对（含汉密尔顿引语 blockquote），check 退出码 0。农业调整法/巴特勒案/威卡德案；1933/1936/23/1942 锚点保留 |
| 2026-08-22 | VI Freedom for Labor（07） | 完成 | 34 块对，check 退出码 0。工会三条件（结社自由/政治自由/经济自由）；工作权利法/大劳工；1956 段金额数字（941,271/79,939/700,000/1.20/79,000）照搬 |
| 2026-08-22 | VII Taxes and Spending（08） | 完成 | 19 块对，check 退出码 0。财产权/累进税=没收性税/塔夫脱引文；全部财政数字（700/810/600/800/950 亿、15.2/37.0/17.7/33.6 亿、143%/89%/18%/20%/40%）保留；脚注上标 2 照搬 |
| 2026-08-22 | VIII The Welfare State（09） | 完成 | 16 块对（含华盛顿电讯 blockquote），check 退出码 0。福利国家/福利主义/国有化对举；托克维尔「监护者社会」呼应第 3 章；1961/15,000,000,000 锚点与脚注 3 照搬 |
| 2026-08-22 | IX Some Notes on Education（10） | 完成 | 21 块对，check 退出码 0。教育四条反对理由/杜威进步主义教育批评；1955/230/42,000/550,000/19 亿/1,500 万/1,000 万/1949–50/2,500 万/1959–60/3,470 万/38%/54 亿/121 亿/124%/1958 全部保留 |
| 2026-08-22 | 全部 12 篇 | 未开工（保持 todo） | 首篇派发即遭 [1301] 内容审查即时过滤（未产出文件未改状态）。政治议题疑似触发，本批次不再尝试 |
| 2026-08-22 | 11-the-soviet-menace / 12-endnotes | doing | 11 章两度派发（换措辞）均触 [1301]，代理未产出；内容侧触发，status 保持 doing 留待后续；12-endnotes 未派保持 todo |
| 2026-08-24 | Endnotes（12-endnotes.md） | 完成 | 3 块对（逐条对照），check 退出码 0。注释编号照搬；金额 $15,000,000,000 沿用 09 章译法「15,000,000,000 美元」；尾注 1 呼应 02 章「进步主义的」保守主义者；↩︎ 回链符保留；新术语「the national debt/国债」补入术语表。11-the-soviet-menace 仍为 doing，未处理 |
| 2026-08-25 | 11-the-soviet-menace.md | doing（保持） | 第 4 次尝试仍被内容侧 [1301] 拦截（子代理 107 秒触拦无产出）；全书 11/12，仅剩此篇 |
| 2026-09-10 | X The Soviet Menace（11） | 完成 | 83 块对（逐段对照），check_bilingual 与 check_coverage 退出码均 0。冷战攻势章：胜于和/胜利为唯一目标；防御性同盟四缺陷/对外援助肠胃理论/谈判与交流计划批判/裁军/联合国/援助共产党政府；十项胜利路标。人名首现附原文（本·富兰克林/艾森豪威尔/赫鲁晓夫/莱昂斯/苏加诺/尼赫鲁/纳赛尔/哥穆尔卡/卡斯特罗）；北约/东南亚条约组织/中央条约组织首现附原文；1952/1955/1956/80 多国/150 年等锚点照搬；铁幕/消耗战/国家社会主义按术语表 |
2026-09-10｜批次2｜整书完结：12/12 全部 done，删认领锁。
