# 翻译计划（Plan.md）

## 本计划信息

- **项目名称**：活人（Manalive）—— G.K.切斯特顿
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
01-part-i-the-enigmas-of-innocent-smith.md,0.0,todo
02-how-the-great-wind-came-to-beacon-house.md,25.3,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `02-how-the-great-wind-came-to-beacon-house.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为「中篇 / 连续模式」，由主 agent 自己执行；若改委派模式则由子代理逐篇执行。无论谁执行，这 9 步不变。

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
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物/语气/风格全文一致（文学类尤其重要），照黄金样本风格译。
- 本书特别注意：Innocent 双关、颜色姓氏、人物声口（古尔德土腔 / 皮姆美式省音 / 玛丽直白 / 穆恩讥诮 / 史密斯喘语碎句），细则见术语表「翻译策略」。
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
回到步骤 2，取下一篇 `todo`，直到全部 `done`。连续模式下主 agent 译完一篇继续下一篇；跨书连译时每本书之间做一次 compact。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | Part I. The Enigmas of Innocent Smith（部题页：第一部 英诺森特·史密斯之谜） | 01-part-i-the-enigmas-of-innocent-smith.md | 0.0KB | todo |
| 2 | I How the Great Wind Came to Beacon House（大风如何来到灯塔屋） | 02-how-the-great-wind-came-to-beacon-house.md | 25.3KB | todo |
| 3 | II The Luggage of an Optimist（乐观主义者的行李） | 03-the-luggage-of-an-optimist.md | 23.2KB | todo |
| 4 | III The Banner of Beacon（灯塔之旗） | 04-the-banner-of-beacon.md | 23.5KB | todo |
| 5 | IV The Garden of the God（神的花园） | 05-the-garden-of-the-god.md | 25.0KB | todo |
| 6 | V The Allegorical Practical Joker（寓言式的恶作剧者） | 06-the-allegorical-practical-joker.md | 43.6KB | todo |
| 7 | Part II. The Explanations of Innocent Smith（部题页：第二部 英诺森特·史密斯的解释） | 07-part-ii-the-explanations-of-innocent-smith.md | 0.0KB | todo |
| 8 | I The Eye of Death; or, the Murder Charge（死亡之眼；或曰谋杀罪） | 08-the-eye-of-death-or-the-murder-charge.md | 48.7KB | todo |
| 9 | II The Two Curates; or, the Burglary Charge（两位牧师；或曰入室行窃罪） | 09-the-two-curates-or-the-burglary-charge.md | 54.4KB | todo |
| 10 | III The Round Road; or, the Desertion Charge（环球之路；或曰遗弃罪） | 10-the-round-road-or-the-desertion-charge.md | 42.1KB | todo |
| 11 | IV The Wild Weddings; or, the Polygamy Charge（狂野的婚礼；或曰多妻罪） | 11-the-wild-weddings-or-the-polygamy-charge.md | 31.8KB | todo |
| 12 | V How the Great Wind Went from Beacon House（大风如何离开灯塔屋） | 12-how-the-great-wind-went-from-beacon-house.md | 6.3KB | todo |

合计 12 篇，约 323.9KB。部题页（#1、#7）仅一行标题，可与相邻章合并处理或单独成文。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-06 | 01-part-i-the-enigmas-of-innocent-smith.md | done | 部题页单行标题，check 退出码 0，无新增术语 |
| 2026-09-06 | 07-part-ii-the-explanations-of-innocent-smith.md | done | 部题页单行标题，check 退出码 0，无新增术语（段B） |
| 2026-09-06 | 08-the-eye-of-death-or-the-murder-charge.md | done | 15 批流式落盘 99 对块，check 退出码 0；新增术语 14 条（段B） |
| 2026-09-06 | 02-how-the-great-wind-came-to-beacon-house.md | done | 流式 4 批；18 对块，check 退出码 0；术语补充 5 条；文风基准章（段A） |
| 2026-09-06 | 09-the-two-curates-or-the-burglary-charge.md | done | 14 批流式落盘 85 对块，check 退出码 0；新增术语 17 条（段B） |
| 2026-09-06 | 03-the-luggage-of-an-optimist.md | done | 流式 5 批；21 对块，check 退出码 0；术语补充 8 条（段A） |
| 2026-09-06 | 10-the-round-road-or-the-desertion-charge.md | done | 11 批流式落盘 53 对块，check 退出码 0；新增术语 19 条（段B） |
| 2026-09-06 | 04-the-banner-of-beacon.md | done | 流式 6 批；23 对块，check 退出码 0；术语补充 11 条（段A） |
| 2026-09-06 | 11-the-wild-weddings-or-the-polygamy-charge.md | done | 8 批流式落盘 56 对块，check 退出码 0；新增术语 11 条；第二部四罪审理毕（段B） |
| 2026-09-06 | 05-the-garden-of-the-god.md | done | 流式 6 批；21 对块，check 退出码 0；术语补充 8 条（段A） |
| 2026-09-06 | 06-the-allegorical-practical-joker.md | done | 流式 12 批；42 对块，check 退出码 0；术语补充 17 条；manalive 双关章（段A） |
| 2026-09-06 | 12-how-the-great-wind-went-from-beacon-house.md | done | 单次直出；8 对块，check 退出码 0；术语补充 2 条；尾章「活人（Manalive）」双关落定（段A） |
| 2026-09-06 | 整书完结（批次2第19本） | 12/12 done | manalive《活人》：项目说明标连续模式，按批次规则改两段委派（第一部+尾章7件/第二部5件），首次执行并发上限2；9个20KB+章全流式（54KB巨章14批）零半块；Manalive双关/颜色姓氏化名/皮姆省音/古尔德土腔按145行成熟术语表统一；写后核验+段末对账12/12一致；主代理全量复验12件exit 0零可疑零数字锚点误报，术语补充区+112条，CSV零残留 |
