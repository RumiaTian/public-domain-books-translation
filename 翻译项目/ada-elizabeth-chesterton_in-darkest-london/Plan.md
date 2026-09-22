# 翻译计划（最黑暗的伦敦）

## 本计划信息

- **项目名称**：最黑暗的伦敦（In Darkest London，阿达·伊丽莎白·切斯特顿）
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
00-foreword.md,1.0,todo
01-i-walked-with-other-souls-in-pain.md,25.3,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `04-the-house-in-kennedy-court.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为**中篇 → 连续模式**，主 agent 自身逐篇执行以下 9 步，译完一篇继续下一篇。

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
- 标题格式：全部「英文 / 中文」合并；罗马数字章号照搬。
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
回到步骤 2，取下一篇 `todo`，直到全部 `done`。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 0 | 作者前言 | 00-foreword.md | 1.0KB | todo |
| 1 | 一、「我与别的受苦人同行……」 | 01-i-walked-with-other-souls-in-pain.md | 25.3KB | todo |
| 2 | 二、找工作的搏斗 | 02-the-fight-to-work.md | 15.2KB | todo |
| 3 | 三、慈善广场的硬心肠女人 | 03-the-hard-faced-woman-of-charity-square.md | 16.6KB | todo |
| 4 | 四、肯尼迪大院 | 04-the-house-in-kennedy-court.md | 24.2KB | todo |
| 5 | 五、一张床的价钱 | 05-the-price-of-a-bed.md | 12.2KB | todo |
| 6 | 六、黑长毛绒外套 | 06-the-black-plush-coat.md | 27.6KB | todo |
| 7 | 七、敲门 | 07-knocking-at-the-gate.md | 19.1KB | todo |
| 8 | 八、门把手的可怕营生 | 08-the-awful-business-of-the-door-handle.md | 30.4KB | todo |
| 9 | 九、基蒂与下药的寡妇 | 09-kitty-and-the-widow-who-drugged.md | 12.2KB | todo |
| 10 | 十、一位非常豪侠的绅士 | 10-a-very-gallant-gentleman.md | 29.6KB | todo |
| 11 | 十一、绝境中的女性 | 11-womanhood-in-extremis.md | 27.6KB | todo |
| 12 | 十二、给吃饱者的几句话 | 12-a-word-to-the-well-fed.md | 15.2KB | todo |
| 13 | 十三、收容机构的陷阱 | 13-the-trap-of-the-institution.md | 19.3KB | todo |
| 14 | 十四、在圣克里斯平 | 14-at-st-crispin-s.md | 13.1KB | todo |
| 15 | 十五、全书的结论 | 15-the-whole-conclusion-of-the-matter.md | 14.7KB | todo |
| 16 | 尾注 | 16-endnotes.md | 2.4KB | todo |

（权威源为 `translation_queue.csv`，此表为快照）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-19 | 00-foreword.md | done | 连续模式主 agent 直译；check 通过 |
| 2026-08-19 | 01-i-walked-with-other-souls-in-pain.md | done | 连续模式直译；救世军首夜，20 对块对照；check 通过（一处 9:20 数字锚点按原样保留后通过） |
| 2026-08-19 | 02-the-fight-to-work.md | done | 连续模式直译；收容站运作+长信引文，11 对块对照；check 通过 |
| 2026-08-19 | 03-the-hard-faced-woman-of-charity-square.md | done | 连续模式直译；擦台阶与卖火柴，13 对块对照；check 通过 |
| 2026-08-20 | 04-the-house-in-kennedy-court.md | done | 连续模式直译；肯尼迪院之夜，15 对块对照 |
| 2026-08-20 | 05-the-price-of-a-bed.md | done | 连续模式直译；一张床的价钱，6 对块对照 |
| 2026-08-24 | 06-the-black-plush-coat.md | done | 连续模式主agent直译，17对块/71段，exit0、0错配；术语补6条（洛克哈特/新街市/猫皮/乌尔斯特/血汗裁缝铺/长毛绒大衣夫人） |
| 2026-08-24 | 07-knocking-at-the-gate.md | done | 连续模式主agent直译，11对块/27段，exit0、0错配；术语补4条（宿夜所/汉伯利街收容所/圣克里斯平宿舍/拿撒勒修女院） |
| 2026-08-24 | 08-the-awful-business-of-the-door-handle.md | done | 连续模式直译；check_bilingual 43 对 0 可疑；114/114 段程序化核验一致 |
| 2026-08-24 | 09-kitty-and-the-widow-who-drugged.md | done | 连续模式直译；check_bilingual 0 可疑；21/21 段程序化核验一致 |
| 2026-08-24 | 10-a-very-gallant-gentleman.md | done | 连续模式直译；116/116 段程序化核验一致；check_bilingual 0 可疑（时间数字改用阿拉伯数字对齐锚点） |
| 2026-08-25 | 11-womanhood-in-extremis.md | done | 27.6KB，主agent连续模式直译，23块/74段，check通过0错配 |
| 2026-08-25 | 12-a-word-to-the-well-fed.md | done | 15.2KB，主agent连续模式直译，8块/25段，check通过0错配 |
| 2026-08-25 | 13-the-trap-of-the-institution.md | done | 19.3KB，主agent连续模式直译，11块/37段（含3处引语块），check通过0错配 |
| 2026-08-25 | 14-at-st-crispin-s.md | done | 13.1KB，主agent连续模式直译，8块/25段，check通过0错配 |
| 2026-08-25 | 15-the-whole-conclusion-of-the-matter.md | done | 14.7KB，主agent连续模式直译，10块/29段（含收支账表1块、尾节---分隔），check通过0错配 |
| 2026-08-25 | 16-endnotes.md | done | 2.4KB，尾注+2统计表，3块/10单元，check通过0错配；本书16/16全完成 |
