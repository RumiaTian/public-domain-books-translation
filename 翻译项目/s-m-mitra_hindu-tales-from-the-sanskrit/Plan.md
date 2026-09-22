# 翻译计划（Plan.md）— 《梵语印度故事》

## 本计划信息

- **项目名称**：s-m-mitra_hindu-tales-from-the-sanskrit（《梵语印度故事》Hindu Tales from the Sanskrit）
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
00-introduction.md,2.2,todo
01-the-magic-pitcher.md,21.7,todo
...
```

---

## 执行步骤（agent 按此推进，委派模式：子代理逐篇执行）

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
结构契约满足则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
`status` 从 `doing` 改 `done`，改两处：① 项目 `translation_queue.csv`；② 根 `translation_queue.csv` 对应行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，直到全部 `done`。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 0 | 导言（Nancy Bell） | 00-introduction.md | 2.2KB | done |
| 1 | 魔罐 | 01-the-magic-pitcher.md | 21.7KB | done |
| 2 | 猫、鼠、蜥蜴和猫头鹰的故事 | 02-the-story-of-a-cat-a-mouse-a-lizard-and-an-owl.md | 12.7KB | done |
| 3 | 皇家捕贼记 | 03-a-royal-thief-catcher.md | 19.6KB | done |
| 4 | 魔鞋与魔杖 | 04-the-magic-shoes-and-staff.md | 28.5KB | done |
| 5 | 宝石箭 | 05-the-jewelled-arrow.md | 42.5KB | done |
| 6 | 甲虫与丝线 | 06-the-beetle-and-the-silken-thread.md | 13.1KB | todo |
| 7 | 乌鸦和他的三个朋友 | 07-a-crow-and-his-three-friends.md | 19.4KB | todo |
| 8 | 聪明的小偷 | 08-a-clever-thief.md | 20.7KB | todo |
| 9 | 隐士之女 | 09-the-hermits-daughter.md | 23.2KB | todo |
| 10 | 尾注 | 10-endnotes.md | 0.3KB | todo |

---

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-18 | 00-introduction.md | done（exit 0，3 对块） | 首译定基调：编辑导言平易书面语，南希·贝尔落款；新词 Mind-Training→心智训练 |
| 2026-08-18 | 06-the-beetle-and-the-silken-thread.md | done | check 退出码 0，13 对块 |
| 2026-08-18 | 01-the-magic-pitcher.md | done（exit 0，14 对块） | 分节罗马数字作「### I / I」合并标题；Original 块与原文逐行一致（含 2 处 U+FEFF） |
| 2026-08-18 | 07-a-crow-and-his-three-friends.md | done | check 退出码 0，24 对块 |
| 2026-08-18 | 02-the-story-of-a-cat-a-mouse-a-lizard-and-an-owl.md | done（exit 0，6 对块） | 动物无名者径称猫/鼠/蜥蜴/猫头鹰；banians→巴尼亚、Vidisa→毗底沙首现附原文 |
| 2026-08-18 | 08-a-clever-thief.md | done | check 退出码 0，17 对块 |
| 2026-08-18 | 09-the-hermits-daughter.md | done | check 退出码 0，18 对块 |
| 2026-08-18 | 10-endnotes.md | done | check 退出码 0，1 对块 | ↩︎ 回链符按术语表删除；Raj-Yoga→拉杰瑜伽（王瑜伽） |
| 2026-08-18 | 03-a-royal-thief-catcher.md | done（exit 0，12 对块） | Benares→贝拿勒斯（今瓦拉纳西）首现括注；nagaballa→那加巴拉 |
| 2026-08-18 | 04-the-magic-shoes-and-staff.md | done（exit 0，17 对块） | Chinchini→钦奇尼；Siva→湿婆、Heaven→天界；Patali-Putra→帕塔利普特拉（华氏城）、Mother Ganga→恒河母亲（Mother Ganga） |
| 2026-08-18 | 05-the-jewelled-arrow.md | done（exit 0，24 对块） | 42.5KB 分两段产出后合并；Dhuma-Pura→杜马普拉（烟城）；Rakshas→罗刹；Marut→马鲁特；Original 块与原文逐行一致（含 6 处 U+FEFF） |
