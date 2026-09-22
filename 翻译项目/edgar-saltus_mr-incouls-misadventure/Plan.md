# Plan.md — 因库尔先生的不幸遭遇（Mr. Incoul's Misadventure）

---

## 本计划信息

- **项目名称**：edgar-saltus_mr-incouls-misadventure
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
01-epigraph.md,0.1,todo
02-dedication.md,0.0,todo
03-mr-incoul.md,7.8,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 带两位数字前缀，前缀=阅读顺序 |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> 本项目为**长篇 → 委派模式**：主 agent 调度，每篇下沉到一次性子代理执行以下 9 步（见 `WORKFLOW.md`「委派模式调度循环」与「子代理简报」）。

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

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节（标记成对、标题合并「英文 / 中文」、不跳过不缩写、UTF-8 无 BOM）。

**本流程专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 章标题罗马数字转汉字序数（“I Mr. Incoul” → 「第一章 因库尔先生 / Mr. Incoul」式合并标题）。
- 正文法/德/意语插词保留原文斜体（策略见术语表第四节）。
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
- ② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 那一行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单。

---

## 篇目清单

| # | 篇名 | 源文 | 状态 |
|---|------|------|------|
| 1 | 题记（Epigraph） | 01-epigraph.md | todo |
| 2 | 献词（Dedication） | 02-dedication.md | todo |
| 3 | 第一章 因库尔先生 | 03-mr-incoul.md | todo |
| 4 | 第二章 巴海特小姐同意改姓 | 04-miss-barhyte-agrees-to-change-her-name.md | todo |
| 5 | 第三章 黑暗之后 | 05-after-darkness.md | todo |
| 6 | 第四章 一次晚间来访 | 06-an-evening-call.md | todo |
| 7 | 第五章 一只黄信封 | 07-a-yellow-envelope.md | todo |
| 8 | 第六章 比亚里茨 | 08-biarritz.md | todo |
| 9 | 第七章 包厢里看得见的 | 09-what-may-be-seen-from-a-palco.md | todo |
| 10 | 第八章 一位不速之客 | 10-an-unexpected-guest.md | todo |
| 11 | 第九章 因库尔先生在西班牙晚餐 | 11-mr-incoul-dines-in-spain.md | todo |
| 12 | 第十章 视角 | 12-the-point-of-view.md | todo |
| 13 | 第十一章 蒙梭公园的宅邸 | 13-the-house-in-the-parc-monceau.md | todo |
| 14 | 第十二章 因库尔先生心事重重 | 14-mr-incoul-is-preoccupied.md | todo |
| 15 | 第十三章 后台听得见的 | 15-what-may-be-heard-in-a-greenroom.md | todo |
| 16 | 第十四章 卡尔蓄起了小胡子 | 16-karl-grows-a-moustache.md | todo |
| 17 | 第十五章 梅的规劝 | 17-may-expostulates.md | todo |
| 18 | 第十六章 赤裸的锥子 | 18-the-bare-bodkin.md | todo |
| 19 | 第十七章 玛伊达的婚礼 | 19-maida-s-nuptials.md | todo |
| 20 | 第十八章 因库尔先生核对账目 | 20-mr-incoul-goes-over-the-accounts.md | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-28 | 全书 20 章 | 完成 20/20 | 批次1三段并行（段B 网络故障死前完成5/6章，单章补译收尾）；术语表既有定名硬约束生效，核心人名全书零漂移；epigraph/dedication 实有内容照译 |
