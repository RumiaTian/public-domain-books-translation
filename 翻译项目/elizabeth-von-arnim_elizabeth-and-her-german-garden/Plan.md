# Plan.md

## 本计划信息

- **项目名称**：elizabeth-von-arnim_elizabeth-and-her-german-garden（《伊丽莎白和她的德国花园》）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态/执行模式**：长篇 / 委派（子代理逐篇执行下方 9 步）

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
01-may-7th.md,15.4,todo
02-may-10th.md,5.4,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-may-7th.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> 本书为**委派模式**：主 agent 把每篇的 9 步下沉到一次性子代理执行（子代理简报见 `WORKFLOW.md`「委派模式调度循环」）。

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

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节。此处不重复。

**本流程专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物/语气/风格全文一致（文学类尤其重要），照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节（本书 09-november-11th.md 约 53.8KB）。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并（章题如「May 7th / 5月7日」）。
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
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单（并发 ≤ 3，见 `WORKFLOW.md`）。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | May 7th | 01-may-7th.md | 15.4KB | todo |
| 2 | May 10th | 02-may-10th.md | 5.4KB | todo |
| 3 | May 14th | 03-may-14th.md | 9.7KB | todo |
| 4 | May 15th | 04-may-15th.md | 1.8KB | todo |
| 5 | May 16th | 05-may-16th.md | 9.9KB | todo |
| 6 | June 3rd | 06-june-3rd.md | 9.6KB | todo |
| 7 | July 11th | 07-july-11th.md | 11.3KB | todo |
| 8 | September 15th | 08-september-15th.md | 5.0KB | todo |
| 9 | November 11th | 09-november-11th.md | 53.8KB | todo |
| 10 | November 20th | 10-november-20th.md | 14.9KB | todo |
| 11 | December 7th | 11-december-7th.md | 10.1KB | todo |
| 12 | December 22nd | 12-december-22nd.md | 21.1KB | todo |
| 13 | December 27th | 13-december-27th.md | 12.1KB | todo |
| 14 | January 1st | 14-january-1st.md | 25.5KB | todo |
| 15 | January 15th | 15-january-15th.md | 17.8KB | todo |
| 16 | January 28th | 16-january-28th.md | 28.0KB | todo |
| 17 | April 18th | 17-april-18th.md | 7.6KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-30 | 全书 17 篇 | done 17/17 | 批次2上锁（01:02）后 3 并行子代理 6/6/5 一次跑通，无 [1301]/[1308]；09 篇 53.8KB 巨章分 15 批流式（临时文件追加法）原文块字节级校验一致（含 U+FEFF/U+00A0 保真），另 3 章 >20KB 流式无半块。三段收尾对齐互相纠偏 10+ 处（橡树→栎树、飞燕草/翠雀近缘种区分、香花芥→香紫罗兰、洋槐→刺槐、洋水仙→黄水仙等），花木通名表全书统一。主 agent 复验 16/17 exit 0 + 01 篇仅数字锚点假阳性（cell No. 14→14号小室），CSV 17 done 无残留，变体 grep 零命中 |
