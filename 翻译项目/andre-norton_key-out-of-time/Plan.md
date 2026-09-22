# 翻译计划（脱离时间的钥匙）

## 本计划信息

- **项目名称**：andre-norton_key-out-of-time
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
01-lotus-world.md,18.3,todo
02-lair-of-mano-nui.md,18.4,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-lotus-world.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本书为长篇，走委派模式，由子代理逐篇执行本流程。无论谁执行，这 9 步不变。

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

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I Lotus World | 01-lotus-world.md | 18.3KB | todo |
| 2 | II Lair of Mano-Nui | 02-lair-of-mano-nui.md | 18.4KB | todo |
| 3 | III The Ancient Mariners | 03-the-ancient-mariners.md | 17.2KB | todo |
| 4 | IV Storm Menace | 04-storm-menace.md | 16.0KB | todo |
| 5 | V Time Wrecked | 05-time-wrecked.md | 16.8KB | todo |
| 6 | VI Loketh the Useless | 06-loketh-the-useless.md | 14.9KB | todo |
| 7 | VII Witches' Meat | 07-witches-meat.md | 16.7KB | todo |
| 8 | VIII The Free Rovers | 08-the-free-rovers.md | 17.7KB | todo |
| 9 | IX Battle Test | 09-battle-test.md | 17.6KB | todo |
| 10 | X Death at Kyn Add | 10-death-at-kyn-add.md | 16.9KB | todo |
| 11 | XI Weapon from the Depths | 11-weapon-from-the-depths.md | 17.1KB | todo |
| 12 | XII Baldies | 12-baldies.md | 18.1KB | todo |
| 13 | XIII The Sea Gate of the Foanna | 13-the-sea-gate-of-the-foanna.md | 17.4KB | todo |
| 14 | XIV The Foanna | 14-the-foanna.md | 16.7KB | todo |
| 15 | XV Return to the Battle | 15-return-to-the-battle.md | 17.9KB | todo |
| 16 | XVI The Opening of the Great Door | 16-the-opening-of-the-great-door.md | 16.7KB | todo |
| 17 | XVII Shades Against Shadow | 17-shades-against-shadow.md | 17.0KB | todo |
| 18 | XVIII World in Doubt? | 18-world-in-doubt.md | 22.1KB | todo |

（以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-05 | 全书 18 章 | done 18/18 | 批次1两段完结：日间会话（13:16 认领）完成 13 章；晚间会话回填 3 个 doing 断点（05/11/18，译文落盘过检补验收）+ 并发 2 子代理译 06/12 章（17+19 对块，check 全过零错配）；术语随章回填（秃头人/萨尔卡/普特卡圣祠等）；删锁流转 |
| 2026-09-06 | 18-world-in-doubt | done 18/18（补全） | 依审核报告修复 A 级截断：第 18 章后半（源文 30-100 行，60 段大结局）断点续作追加 14 块（8→22 对），check rc=0 零错配；全书真实完结，删锁流转 |
