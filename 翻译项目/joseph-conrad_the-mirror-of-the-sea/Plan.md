# 翻译计划（海之镜）

## 本计划信息

- **项目名称**：海之镜（The Mirror of the Sea，约瑟夫·康拉德）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（68 个文件，已加 01—68 数字前缀保阅读序） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

## 篇目结构

> 原书为四十九篇以罗马数字（I—XLIX）标号的独立沉思，分归十五个主题部分（part）。原文文件名前缀 01—68 即 spine 阅读顺序：01—04 卷首（题献 / 作者札记 / 两段铭文），随后每个主题部分的标题文件（仅一行 `## 标题`）与该部分所含罗马数字篇章交替排列。完整逐文件清单见 `translation_queue.csv`。

| 部分 | 主题（英文 / 中文） | 所含文件（前缀） | 罗马数字篇 |
|------|---------------------|------------------|-----------|
| 卷首 | 题献 / 作者札记 / 铭文 | 01—04 | — |
| 1 | Landfalls and Departures / 抵港与启航 | 05—08 | I—III |
| 2 | Emblems of Hope / 希望之徽 | 09—12 | IV—VI |
| 3 | The Fine Art / 这门行当 | 13—16 | VII—IX |
| 4 | Cobwebs and Gossamer / 蛛丝与轻纱 | 17—20 | X—XII |
| 5 | The Weight of the Burden / 重负之重 | 21—24 | XIII—XV |
| 6 | Overdue and Missing / 逾期与失踪 | 25—29 | XVI—XIX |
| 7 | The Grip of the Land / 陆地的钳制 | 30—32 | XX—XXI |
| 8 | The Character of the Foe / 敌手的品性 | 33—36 | XXII—XXIV |
| 9 | Rulers of East and West / 东西方的统治者 | 37—42 | XXV—XXIX |
| 10 | The Faithful River / 忠实的河流 | 43—46 | XXX—XXXII |
| 11 | In Captivity / 囚困之中 | 47—49 | XXXIII—XXXIV |
| 12 | Initiation / 入门 | 50—52 | XXXV—XXXVI |
| 13 | The Nursery of the Craft / 这门行当的苗圃 | 53—56 | XXXVII—XXXIX |
| 14 | The Tremolino / 特雷莫利诺号 | 57—63 | XL—XLV |
| 15 | The Heroic Age / 英雄时代 | 64—68 | XLVI—XLIX |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

委派模式下，各子代理以较早完成的译文（尤以 06-chapter-1 第一篇为沉思体基调范本）为风格黄金样本，保持全书第一人称散文声口一致。罗马数字章号（I—XLIX）照搬不译；主题部分标题文件译为「英文 / 中文」合并标题。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-10 | 全书 68 文件（题献+作者札记+铭文+49篇+主题扉页） | 整书完结 | 批次4委派模式：10 个并发子代理译完（337.6KB 航海散文）；68/68 done，check_bilingual 结构契约 0 违规（非零退出码均为数字本地化改写型锚点误报）；组2/5/8 共 17 个文件命名带 .md 后缀笔误，主 agent 统一重命名修正；无 doing 残留、无失败。术语表硬约束全程生效（抵港/离港定位/航海术语/罗曼语照搬加注）。 |
