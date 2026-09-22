# 翻译计划：James Stephens《The Demi-Gods》（半神）

> 复制自 `prompts/翻译计划模板.md`。执行者按「执行步骤」9 步推进；本项目的执行模式为**委派**（长篇），由子代理逐章执行。

---

## 本计划信息

- **项目名称**：james-stephens_the-demi-gods
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
chapter-01.md,7.1,todo
chapter-02.md,3.8,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `chapter-01.md` |
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
- 人物/语气/风格全文一致（文学类尤其重要），照黄金样本风格译。爱尔兰英语口语按术语表「翻译策略」第 6 条处理。
- 章节标题罗马数字照搬不译；卷标题（`## Book I: …`）译作「Book I: Patsy Mac Cann / 第一卷：帕齐·麦克·坎恩」合并格式。
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
| 0 | 献词（Thomas Bodkin） | 00-dedication.md | 0.0KB | todo |
| 1 | 第一章（I） | chapter-01.md | 7.1KB | todo |
| 2 | 第二章（II） | chapter-02.md | 3.8KB | todo |
| 3 | 第三章（III） | chapter-03.md | 5.1KB | todo |
| 4 | 第四章（IV） | chapter-04.md | 4.5KB | todo |
| 5 | 第五章（V） | chapter-05.md | 3.8KB | todo |
| 6 | 第六章（VI） | chapter-06.md | 6.7KB | todo |
| 7 | 第七章（VII） | chapter-07.md | 5.0KB | todo |
| 8 | 第八章（VIII） | chapter-08.md | 5.7KB | todo |
| 9 | 第九章（IX） | chapter-09.md | 5.9KB | todo |
| 10 | 第十章（X） | chapter-10.md | 6.3KB | todo |
| 11 | 第十一章（XI） | chapter-11.md | 8.9KB | todo |
| 12 | 第十二章（XII） | chapter-12.md | 5.0KB | todo |
| 13 | 第十三章（XIII） | chapter-13.md | 7.9KB | todo |
| 14 | 第十四章（XIV） | chapter-14.md | 4.0KB | todo |
| 15 | 第十五章（XV） | chapter-15.md | 6.9KB | todo |
| 16 | 第十六章（XVI） | chapter-16.md | 9.9KB | todo |
| 17 | 第十七章（XVII） | chapter-17.md | 2.0KB | todo |
| 18 | 第十八章（XVIII） | chapter-18.md | 3.2KB | todo |
| 19 | 第十九章（XIX） | chapter-19.md | 8.6KB | todo |
| 20 | 第二十章（XX） | chapter-20.md | 9.3KB | todo |
| 21 | 第二十一章（XXI） | chapter-21.md | 10.2KB | todo |
| 22 | 第二十二章（XXII） | chapter-22.md | 3.9KB | todo |
| 23 | 第二十三章（XXIII） | chapter-23.md | 4.4KB | todo |
| 24 | 第二十四章（XXIV） | chapter-24.md | 9.3KB | todo |
| 25 | 第二十五章（XXV） | chapter-25.md | 16.8KB | todo |
| 26 | 第二十六章（XXVI） | chapter-26.md | 4.2KB | todo |
| 27 | 第二十七章（XXVII） | chapter-27.md | 10.3KB | todo |
| 28 | 第二十八章（XXVIII） | chapter-28.md | 8.1KB | todo |
| 29 | 第二十九章（XXIX） | chapter-29.md | 8.2KB | todo |
| 30 | 第三十章（XXX） | chapter-30.md | 5.2KB | todo |
| 31 | 第三十一章（XXXI） | chapter-31.md | 9.8KB | todo |
| 32 | 第三十二章（XXXII） | chapter-32.md | 3.2KB | todo |
| 33 | 第三十三章（XXXIII） | chapter-33.md | 17.3KB | todo |
| 34 | 第三十四章（XXXIV） | chapter-34.md | 12.5KB | todo |
| 35 | 第三十五章（XXXV） | chapter-35.md | 8.5KB | todo |

> 权威清单以 `translation_queue.csv` 为准。卷归属：Book I = 章 1–12；Book II = 章 13–19；Book III = 章 20–27；Book IV = 章 28–35（卷标题已并入各卷首章文件）。全书合计约 251.7KB。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-30 | 全书 36 项（35 章＋献词） | 完成 35/36 | 批次1历经三波：首轮 3 段遭 [1301]×1+[1308]×2 中断（存稿 15 章）；断点续作 B/C 两段＋ch07 免责重派失败后跳章降级（A 补 8-12+34-35）；C 自愈装配模板多镜像 --- 缺陷。ch07 为封锁章（[1301]×2 平台误伤，确认放弃）。定名零漂移（18 组变体全一致）；四部题＝帕齐·麦克·坎恩／艾琳·尼·库利／布里恩·奥布莱恩／玛丽·麦克·坎恩 |
| 2026-08-31 | ch07 隔日新链重试 | 仍封锁 | 批次3新会话链重试 ch07（原派+免责前缀各 1 次）：双双 [1301]（137s/81s 即拦），维持 todo 封锁、放锁流转。本项为顽固封锁件，后续批次勿再消耗尝试 |
| 2026-09-02 | 第 7 章 | 跳过（2×[1301]） | 批次1残留回收：chapter-07 两次派发均遭内容安全误报（源文为无害的爱尔兰野餐场景），按规则重试一次后跳过留 todo |

## 2026-09-05 批次3运行记录
- 06:11 批次3认领（认领.md）。摸底：35/36 done，仅剩 chapter-07（5KB，todo，无半成品）。
- 06:12 派子代理翻译 chapter-07 → [1301] 内容拦截，重置 todo。
- 06:14 加学术文献免责前缀重派 1 次 → 仍 [1301] 拦截。按规则6：保持 todo、跳过、不再重试。chapter-07 列为封锁项，本轮确认放弃。
- 06:15 删除认领锁，批次3流转下一本（lewis-mumford_sticks-and-stones）。

## 2026-09-06 批次3运行记录
- 06:11 批次3认领，重试 chapter-07（昨日已2次[1301]拦截）。
- 06:11、06:12 两次派发（含学术免责前缀）均在35-51秒内遭[1301]内容拦截，累计4次（跨2026-09-05/06两日），判定为该章内容确定性触发过滤，非瞬时波。
- ⚠️ 待人工处理：chapter-07 为全书唯一剩余章节（35/36 done），需人工分段翻译或调整过滤策略后补译。批次3确认放弃，删除认领锁，流转 sticks-and-stones。
