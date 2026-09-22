# 翻译计划 — jean-toomer_cane（《甘蔗》）

---

## 本计划信息

- **项目名称**：jean-toomer_cane（《甘蔗》Cane, Jean Toomer）
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
01-dedication.md,0.0,todo
02-epigraph.md,0.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `04-karintha.md` |
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
5. prompts/领域配置/对应领域.md（项目说明指定）
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
- 诗行/歌谣保留分行与引文块结构（见项目说明备注）。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并。
- 术语一致：抽查 5 个术语词，全文译法统一。
- 诗歌分行与源文一致。
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

全书 32 个文件，三部分：
- 南方（佐治亚，第 1–19 篇）：dedication、epigraph、foreword、Karintha 至 Blood-Burning Moon，诗与散文速写交错；
- 北方（华盛顿/芝加哥，第 20–31 篇）：Seventh Street 至 Bona and Paul；
- 剧本（第 32 篇）：Kabnis。

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 献辞 | 01-dedication.md | 0.0KB | todo |
| 2 | 题词 | 02-epigraph.md | 0.1KB | todo |
| 3 | 序言 | 03-foreword.md | 5.5KB | todo |
| 4 | 卡琳莎 | 04-karintha.md | 3.9KB | todo |
| 5 | 收割者（诗） | 05-reapers.md | 0.4KB | todo |
| 6 | 十一月棉花花（诗） | 06-november-cotton-flower.md | 0.7KB | todo |
| 7 | 贝琪 | 07-becky.md | 5.5KB | todo |
| 8 | 脸（诗） | 08-face.md | 0.3KB | todo |
| 9 | 棉花之歌（诗） | 09-cotton-song.md | 0.7KB | todo |
| 10 | 卡玛 | 10-carma.md | 4.4KB | todo |
| 11 | 之子之歌（诗） | 11-song-of-the-son.md | 1.0KB | todo |
| 12 | 佐治亚黄昏（诗） | 12-georgia-dusk.md | 1.3KB | todo |
| 13 | 费恩 | 13-fern.md | 10.5KB | todo |
| 14 | 无效（诗） | 14-nullo.md | 0.2KB | todo |
| 15 | 夜歌（诗） | 15-evening-song.md | 0.4KB | todo |
| 16 | 埃丝特 | 16-esther.md | 4.5KB | todo |
| 17 | 皈依（诗） | 17-conversion.md | 0.2KB | todo |
| 18 | 佐治亚画像（诗） | 18-portrait-in-georgia.md | 0.3KB | todo |
| 19 | 血烧月 | 19-blood-burning-moon.md | 2.7KB | todo |
| 20 | 第七街 | 20-seventh-street.md | 1.4KB | todo |
| 21 | 罗伯特 | 21-rhobert.md | 2.8KB | todo |
| 22 | 艾薇 | 22-avey.md | 13.8KB | todo |
| 23 | 蜂巢（诗） | 23-beehive.md | 0.5KB | todo |
| 24 | 风暴结束（诗） | 24-storm-ending.md | 0.3KB | todo |
| 25 | 剧场 | 25-theater.md | 9.8KB | todo |
| 26 | 她的双唇是铜线（诗） | 26-her-lips-are-copper-wire.md | 0.4KB | todo |
| 27 | 呼唤耶稣（诗） | 27-calling-jesus.md | 1.8KB | todo |
| 28 | 包厢座 | 28-box-seat.md | 12.2KB | todo |
| 29 | 祈祷（诗） | 29-prayer.md | 0.7KB | todo |
| 30 | 收获之歌（诗） | 30-harvest-song.md | 1.7KB | todo |
| 31 | 博娜与保罗 | 31-bona-and-paul.md | 3.3KB | todo |
| 32 | 卡布尼斯（剧本） | 32-kabnis.md | 10.6KB | todo |

（以 `translation_queue.csv` 为准，此表同步维护）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-15 | 01-dedication.md | done | 0.1KB |
| 2026-08-15 | 02-epigraph.md | done | 0.2KB |
| 2026-08-15 | 03-foreword.md | done | 11.2KB | check 通过，8 对块 |
| 2026-08-15 | 04-karintha.md | done | 7.8KB | check 通过，8 对块；歌谣叠句按术语表 |
| 2026-08-15 | 05-reapers.md | done | 0.8KB | check 通过，1 对块 |
| 2026-08-15 | 06-november-cotton-flower.md | done | 1.4KB | check 通过，1 对块 |
| 2026-08-15 | 07-becky.md | done | 11.1KB | check 通过，6 对块 |
| 2026-08-15 | 08-face.md | done | 0.7KB | check 通过，1 对块 |
| 2026-08-15 | 09-cotton-song.md | done | 1.4KB | check 通过，1 对块；叠句重复照原样 |
| 2026-08-15 | 10-carma.md | done | 9.0KB | check 通过，6 对块；中段 corn 变体叠句保留 |
| 2026-08-15 | 11-song-of-the-son.md | done | 2.2KB | check 通过，1 对块 |
| 2026-08-15 | 12-georgia-dusk.md | done | 2.6KB | check 通过，1 对块 |
| 2026-08-15 | 13-fern.md | done | 20.7KB | check 通过，4 对块 |
| 2026-08-15 | 14-nullo.md | done | 0.4KB | check 通过，1 对块 |
| 2026-08-15 | 15-evening-song.md | done | 0.8KB | check 通过，1 对块 |
| 2026-08-15 | 16-esther.md | done | 9.1KB | check 通过，8 对块；源文件仅含第 I 节 |
| 2026-08-15 | 17-conversion.md | done | 0.5KB | check 通过，1 对块 |
| 2026-08-15 | 03-17 第一部分「南方」(15篇) | done ×15 | exit 0×15(主agent代校验); 委派子代理(单代理连译,产出完成后触发[1301]敏感词拦截未能自报,译文完整落盘)。诗歌逐行对应+引文块缩进保留;南方篇抒情浓烈语调 |
| 2026-08-15 | 18-32 第二部分「北方」+诗剧Kabnis(15篇,126302B,72对块) | done ×15 | exit 0×15; 委派子代理(单代理连译)。北方篇碎裂都市节奏;Kabnis 剧本体对话/舞台指示分明;nigger 按语境区分(白人语境保「黑鬼」残酷性/黑人社区内部「黑人」)。新词:卡布尼斯/汉比/莱曼/老彩印婆 等+15篇名译法;eoho=哦吼 |
| 2026-08-15 | ★全书完 32/32 | — | jean-toomer_cane《甘蔗》全部32篇译完(100%)。本会话 2 子代理并行译 30 篇(~102KB源文)。哈莱姆文艺复兴里程碑 |
