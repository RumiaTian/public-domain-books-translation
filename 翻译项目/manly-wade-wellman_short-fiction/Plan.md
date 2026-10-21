# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：manly-wade-wellman_short-fiction
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
第一章.md,12.3,todo
第二章.md,18.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `The-Bryd.md` |
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
| 1 | The Valley Was Still | 01-the-valley-was-still.md | 29.8KB | todo |
| 2 | The Witch's Cat | 02-the-witch-s-cat.md | 34.8KB | todo |
| 3 | The Golgotha Dancers | 03-the-golgotha-dancers.md | 19.8KB | todo |
| 4 | Fearful Rock | 04-fearful-rock.md | 8.2KB | todo |
| 5 | The Hairy Ones Shall Dance | 05-the-hairy-ones-shall-dance.md | 1.4KB | todo |
| 6 | The Black Drama | 06-the-black-drama.md | 1.8KB | todo |
| 7 | Coven | 07-coven.md | 12.3KB | todo |
| 8 | It All Came True in the Woods | 08-it-all-came-true-in-the-woods.md | 17.8KB | todo |
| 9 | The Dreadful Rabbits | 09-the-dreadful-rabbits.md | 25.5KB | todo |
| 10 | The Half-Haunted | 10-the-half-haunted.md | 31.1KB | todo |
| 11 | The Liers in Wait | 11-the-liers-in-wait.md | 30.1KB | todo |
| 12 | Back to the Beast | 12-back-to-the-beast.md | 1.5KB | todo |
| 13 | The Song of the Slaves | 13-the-song-of-the-slaves.md | 25.9KB | todo |
| 14 | Bratton's Idea | 14-bratton-s-idea.md | 52.8KB | todo |
| 15 | The Invading Asteroid | 15-the-invading-asteroid.md | 11.7KB | todo |
| 16 | The Devil's Asteroid | 16-the-devil-s-asteroid.md | 58.2KB | todo |
| 17 | Warrior of Two Worlds | 17-warrior-of-two-worlds.md | 15.7KB | todo |
| 18 | All Were Monsters | 18-all-were-monsters.md | 12.7KB | todo |
| 19 | Half Around Pluto | 19-half-around-pluto.md | 24.3KB | todo |
| 20 | Venus Enslaved | 20-venus-enslaved.md | 98.1KB | todo |

（同时以 `translation_queue.csv` 管理）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-10-15 | 02-the-witch-s-cat.md | done | 42 对块，145 段全译，check_bilingual.py 退出码 0 |
| 2026-10-15 | 04-fearful-rock.md | done | 9 对块，30 段全译，check_bilingual.py 退出码 0 |
| 2026-10-15 | 05-the-hairy-ones-shall-dance.md | done | 1 对块，7 段引用体全译，check_bilingual.py 退出码 0 |
| 2026-10-15 | 03-the-golgotha-dancers.md | done | 18 对块，78 段全译，check_bilingual.py 退出码 0；术语表补 9 条新词 |
| 2026-10-15 | 06-the-black-drama.md | done | 2 对块，序言 6 段全译（引用体保留），check_bilingual.py 退出码 0；术语表补 7 条新词 |
| 2026-10-15 | 07-coven.md | done | 17 对块，71 段全译，check_bilingual.py 退出码 0；术语表补 6 条新词 |
| 2026-10-15 | 08-it-all-came-true-in-the-woods.md | done | 22 对块，96 段全译（含篇首题诗引用体保留），check_bilingual.py 退出码 0；术语表补 7 条新词 |
| 2026-10-15 | 09-the-dreadful-rabbits.md | done | 29 对块，120 行（113 段）全译，check_bilingual.py 退出码 0；术语表补 15 条新词并校正 Morgan Pi→Morgan Pitts |
| 2026-10-15 | 12-back-to-the-beast.md | done | 2 对块，5 段全译（剪报体短文，无标题行），check_bilingual.py 退出码 0；术语表补 9 条新词 |
| 2026-10-15 | 10-the-half-haunted.md | done | 44 对块，194 段全译（篇首题诗引用体保留、7 处场景分隔原位保留），check_bilingual.py 退出码 0；术语表补 10 条新词 |
| 2026-10-15 | 11-the-liers-in-wait.md | done | 42 对块，136 段全译（篇首题诗引用体保留、8 处场景分隔原位保留），check_bilingual.py 退出码 0；术语表补 29 条新词（查理二世出逃史实人物与地名） |
| 2026-10-15 | 15-the-invading-asteroid.md | done | 13 对块，55 段全译（### I 标题合并、2 处场景分隔原位保留），check_bilingual.py 退出码 0；术语表补 9 条新词（科幻篇人名/机构/武器） |
| 2026-10-15 | 13-the-song-of-the-slaves.md | done | 34 对块，130 段全译（书信/朗费罗诗引用体保留、6 处场景分隔原位保留），check_bilingual.py 退出码 0；术语表补 18 条新词 |
| 2026-10-15 | 14-bratton-s-idea.md | done | 48 对块，242 段全译（52.8KB 超大篇，按 7 幕分段翻译后程序化拼合，6 处场景分隔原位保留），check_bilingual.py 退出码 0；术语表补 13 条新词（布拉顿/加斯孔/汤姆-汤姆等） |
| 2026-10-15 | 17-warrior-of-two-worlds.md | done | 20 对块，85 段全译（### I 标题合并、3 处场景分隔原位保留），check_bilingual.py 退出码 0；术语表补 9 条新词（东德罗莫贡/扬德罗/多丽扎/斯波尔等） |
| 2026-10-15 | 16-the-devil-s-asteroid.md | done | 63 对块，302 段全译（58.2KB 全书最大篇，按场景分 5 段翻译后程序化拼合，9 处场景分隔原位保留），check_bilingual.py 退出码 0；术语表补 15 条新词（菲茨休·帕尔/瓦莉娜·彭伯顿/林/鲁珀特等） |
| 2026-10-15 | 18-all-were-monsters.md | done | 19 对块，97 段全译（1 处场景分隔原位保留、原文不可见字符字节级保真），check_bilingual.py 退出码 0；术语表补 4 条新词（普罗沃尔/斯基普/奥斯卡/篇名） |
| 2026-10-15 | 19-half-around-pluto.md | done | 33 对块，全文 6 场景全译（5 处场景分隔原位保留、航行日志引用体保留、数字锚点按位保留），check_bilingual.py 退出码 0；术语表补 6 条新词（沃福思/詹克斯/科贝特/莉娅·斯特罗明格/基地营/篇名） |
| 2026-10-18 | 20-venus-enslaved.md | done | 一次性子代理翻译（98KB 中篇，分段流式落盘），97 对块对照，check_bilingual 通过（退出码 0）。新增定名：戴维·普兰特/迪斯布罗/马克斯/斯凯戈/玛拉/曼莎/莎拉/弗拉/格兰菲尔/霍默森医生/巢窟/泥虫/克劳/格罗尔/火箭基金会/沃尔弗拉姆/《被奴役的金星》 |
| 2026-10-18 | 全书完结 | done | Wellman 短篇集 20/20 全部完成（前 19 篇由兄弟执行流完成，第 20 篇 98KB 中篇《被奴役的金星》由本执行流断点续作：复用 _work20 残留 f1/f2 分段+运行 f3.py+新译 4 段流式落盘，97 对块一次过检），删除认领锁 |
2026-10-18 | 🎉全书完书 | 20/20 done（10-17 本会话开册译至19篇+终篇断点，10-18 晨间他流接力译完98KB终篇20并流转删锁；本会话验收抽查通过）
