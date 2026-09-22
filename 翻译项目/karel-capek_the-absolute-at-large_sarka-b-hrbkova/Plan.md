# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：karel-capek_the-absolute-at-large_sarka-b-hrbkova（《绝对无处不在》，Karel Čapek, *The Absolute at Large*，Šárka B. Hrbková 英译）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态**：长篇（30 章 + 尾注）→ **执行模式：委派**（子代理逐章执行下方 9 步）

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（01–30 章序号前缀 = 罗马数字 I–XXX，31 为尾注） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
01-the-advertisement.md,8.7,todo
02-the-karburator.md,9.6,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-the-advertisement.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> 本书为**委派模式**：主 agent 按调度循环派单，子代理在独立上下文逐章执行本流程。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
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

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节。此处不重复。

**本书专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：捷克人名/地名译法、The Absolute=「绝对物」、Karburator=「卡布拉托」全书统一，首现附原文。
- 章标题格式「英文 / 中文」，罗马数字章号照搬（如 `## I The Advertisement / 一 广告`）。
- 讽刺语气、人物口癖（如布拉豪什家的"Yes, yes"絮叨）前后一致；照黄金样本风格译。

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
结构契约满足则继续；有违规回步骤 4 修订。

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

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I The Advertisement | 01-the-advertisement.md | ~9KB | todo |
| 2 | II The Karburator | 02-the-karburator.md | ~10KB | todo |
| 3 | III Pantheism | 03-pantheism.md | ~11KB | todo |
| 4 | IV God in the Cellar | 04-god-in-the-cellar.md | ~10KB | todo |
| 5 | V Bishop Linda | 05-bishop-linda.md | ~12KB | todo |
| 6 | VI The Board-Meeting | 06-the-board-meeting.md | ~10KB | todo |
| 7 | VII Developments | 07-developments.md | ~8KB | todo |
| 8 | VIII The Dredge | 08-the-dredge.md | ~14KB | todo |
| 9 | IX The Ceremony | 09-the-ceremony.md | ~11KB | todo |
| 10 | X Saint Ellen | 10-saint-ellen.md | ~9KB | todo |
| 11 | XI The First Blow Struck | 11-the-first-blow-struck.md | ~11KB | todo |
| 12 | XII Doctor Blahous | 12-doctor-blahous.md | ~9KB | todo |
| 13 | XIII The Chronicler's Apology | 13-the-chronicler-s-apology.md | ~9KB | todo |
| 14 | XIV The Land of Plenty | 14-the-land-of-plenty.md | ~13KB | todo |
| 15 | XV Disaster | 15-disaster.md | ~12KB | todo |
| 16 | XVI In the Mountains | 16-in-the-mountains.md | ~10KB | todo |
| 17 | XVII The Hammer and Star | 17-the-hammer-and-star.md | ~8KB | todo |
| 18 | XVIII In the Night Editor's Room | 18-in-the-night-editor-s-room.md | ~10KB | todo |
| 19 | XIX The Process of Canonization | 19-the-process-of-canonization.md | ~8KB | todo |
| 20 | XX St. Kilda | 20-st-kilda.md | ~12KB | todo |
| 21 | XXI The Telegram | 21-the-telegram.md | ~9KB | todo |
| 22 | XXII The Old Patriot | 22-the-old-patriot.md | ~11KB | todo |
| 23 | XXIII The Augsburg Imbroglio | 23-the-augsburg-imbroglio.md | ~12KB | todo |
| 24 | XXIV The Napoleon of the Mountain Brigade | 24-the-napoleon-of-the-mountain-brigade.md | ~8KB | todo |
| 25 | XXV The So-Called Greatest War | 25-the-so-called-greatest-war.md | ~8KB | todo |
| 26 | XXVI The Battle of Hradec Králové | 26-the-battle-of-hradec-kr-lov.md | ~9KB | todo |
| 27 | XXVII A Coral Island in the Pacific | 27-a-coral-island-in-the-pacific.md | ~8KB | todo |
| 28 | XXVIII At Seven Cottages | 28-at-seven-cottages.md | ~7KB | todo |
| 29 | XXIX The Last Battle | 29-the-last-battle.md | ~7KB | todo |
| 30 | XXX The End of Everything | 30-the-end-of-everything.md | ~8KB | todo |
| 31 | Endnotes | 31-endnotes.md | ~0.4KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-02 | 全书 31 件（30 章＋尾注） | 完成 31/31 | 批次1三段并行（103.1/100.8/86.7KB，10+10+11 件全单发）零[1301][1302][1308]；31 件全量过检零告警；漂移10处终验统一（米克萨街/布热夫诺夫/斯捷霍维采/代维采系）；恰佩克讽刺文风一本正经的荒诞；讹词与口误存真（狐狸肥/卡不拉托们）；拉丁语与造词照搬加注 |
