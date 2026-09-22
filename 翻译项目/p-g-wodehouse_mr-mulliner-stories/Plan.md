# 翻译计划（Plan.md）— 《穆勒先生故事集》

## 本计划信息

- **项目名称**：《穆勒先生故事集》（P. G. 伍德豪斯《Mr. Mulliner Stories》）
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
the-truth-about-george.md,32.6,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `the-truth-about-george.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：委派模式由子代理逐篇执行本流程；连续模式（中篇）由主 agent 自己执行。无论谁执行，这 9 步不变。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（作为风格黄金样本，照此风格译；无则可参考 p-g-wodehouse_the-small-bachelor 项目的译文风格；均无则跳过）
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
- 本项目专有：口吃、结巴等拟声重复（N-n-n-n-ice d-d-d-day）须以中文结巴语气（例：「今-今-今……今天天……天气」）如实再现，不可省略或简化；穆勒家人物跨篇登场，译名务必对照术语表。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节（本项目最长篇约 47KB，一般无需分段）。

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
| 1 | The Truth About George（乔治的真相） | the-truth-about-george.md | 32.6KB | todo |
| 2 | A Slice of Life（生活的一角） | a-slice-of-life.md | 28.4KB | todo |
| 3 | Mulliner's Buck-U-Uppo（穆勒家的补力剂） | mulliner-s-buck-u-uppo.md | 32.4KB | todo |
| 4 | The Bishop's Move（主教的一着棋） | the-bishop-s-move.md | 33.9KB | todo |
| 5 | Came the Dawn（黎明到来） | came-the-dawn.md | 31.0KB | todo |
| 6 | The Story of William（威廉的故事） | the-story-of-william.md | 30.9KB | todo |
| 7 | Portrait of a Disciplinarian（严师写照） | portrait-of-a-disciplinarian.md | 31.0KB | todo |
| 8 | The Romance of a Bulb-Squeezer（挤灯泡者的罗曼史） | the-romance-of-a-bulb-squeezer.md | 31.3KB | todo |
| 9 | Honeysuckle Cottage（忍冬小屋） | honeysuckle-cottage.md | 47.1KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-16 | a-slice-of-life.md | 28.4KB / 退出码 0 | 本项目首篇，确立风格黄金样本；产品名与 ffinch-ffarrowmere 小写 f 双关等新术语已补入术语表 |
| 2026-08-16 | portrait-of-a-disciplinarian | 31.0KB / 退出码 0（40 对块、段落 279:279 对称、可疑错配 0） | 新术语已补入术语表：滨海宾利、简·奥利芬特、马拉齐恩路、小霍尔姆、软泥谷等 |
| 2026-08-16 | came-the-dawn | 31.0KB | - | 子代理两度触[1301]内容过滤（clean失败无文件），status 保持 doing，留待并行cron重试 |
| 2026-08-16 | mulliner-s-buck-u-uppo | 32.4KB / 退出码 0（28 对块、段落对称、可疑错配 0） | 新术语已补入术语表：米登的下布里斯基特、沃德尔太太、馅饼脸／博科·比克顿、祭披／锦带、七旬主日等；bish 依主教篇术语表统一译「老主教」 |
| 2026-08-16 | the-truth-about-george | 32.6KB / 退出码 0（72 对块、段落 151:151 对称、可疑错配 0） | 口吃拟声以「今-今-今」连字符式全篇再现；新术语已补入术语表：伊普尔顿、灯帚间、阿比西尼亚皇帝、连字符长村名系列（谷中小威格马什等）、《英语同义词词典》等 |
| 2026-08-16 | the-bishop-s-move | 33.9KB / 退出码 0（31 对块、段落 285:285 对称、可疑错配 0） | 篇题定「主教的一着棋」；圣经引文章节号保留阿拉伯数字（数字锚点全过）；新术语已补入术语表：哈彻斯特、猫食（Catsmeat）、布拉德纳夫将军、瓦-纳-巴戈什-巴金戈、斯蒂普尔马默里等；源文“Whats 分配清单”一节原文即缺失（仅存 as follows:/making five in all 两行），照实译出未补造 |
| 2026-08-16 | the-story-of-william | 30.9KB / 退出码 0（34 对块、段落 167:167 对称、可疑错配 0） | 首现数字锚点 1906 加空格通过；新术语已补入术语表：默特尔·班克斯、德斯蒙德·弗兰克林、迈克酒馆、三款酒名（炸药露珠／梦乡特饮／送葬人之乐）、墨菲家的小矮人、约翰·旧金山·地震·穆勒等；订正 Elmer 行备注（系酒馆顾客之兄弟，非穆勒家人） |
| 2026-08-16 | the-romance-of-a-bulb-squeezer | 31.3KB / 退出码 0（52 对块、段落 195:195 对称、可疑错配 0） | 篇题定「挤灯泡者的罗曼史」；Power A–F 以天干「甲乙丙丁戊己」再现「Call it B／Call it Power F」笑点；fly／flee／flea 谐音双关译文附注；新术语已补入术语表：东图廷、比格斯诉穆勒案、约瑟夫·博杰爵士、「负片与显影液」俱乐部、挤灯泡者联合公会、莫妮卡·索斯伯恩小姐、格拉迪斯、半克朗等 |
| 2026-08-16 | honeysuckle-cottage | 47.1KB / 退出码 0（35 对块、段落 293:293 对称、可疑错配 0） | 新术语已补入术语表：罗丝·梅纳德、威廉／托托、麦金农与古奇、普罗德与威格斯、《秘密九人团》、卡特雷特上校（冷钢卡特雷特）、绣线菊枢纽站等；Original 块已按源文逐字对齐重建（弯引号／省略号与源文一致，修正 definitive→definite 一处转写误差） |
| 2026-08-17 | came-the-dawn 重试第 3 次 | 派发子代理再次被 [1301] 敏感内容拦截（202608171820…），无译文落盘。status 保持 doing，留待后续换派单措辞重试 |
