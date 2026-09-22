# 翻译计划（《女侦探洛芙迪·布鲁克的经历》）

## 本计划信息

- **项目名称**：《女侦探洛芙迪·布鲁克的经历》（凯瑟琳·卢伊莎·皮尔基斯）
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
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本篇目为短篇集，走委派模式，由子代理逐篇执行。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-13 | - | 建项目 | 从 待翻译/catherine-louisa-pirkis_the-experiences-of-loveday-brooke-lady-detective.epub 提取 7 篇正文、建术语表初版、生成队列。领域=小说文学，形态=短篇集，模式=委派，粒度=块对照。 |
| 2026-08-13 | a-princesss-vengeance (83038B,41对块) | done | exit 0; 委派子代理(自行补术语表)。首篇黄金样本,定维多利亚晚期典雅克制推理风格。土耳其公主复仇案。法语 seule sur la terre 等保留释义 |
| 2026-08-13 | drawn-daggers (88772B,60对块) | done | exit 1=数字锚点误报(14→十四),结构满足; 委派子代理。弃职牧师案。新词:Mrs.Hawke/Danvers/Decastro 香港钻石商/Colombo 科伦坡号 等 |
| 2026-08-13 | the-ghost-of-fountain-lane (92399B,47对块) | done | exit 0; 委派子代理。千禧年派讲道者偷支票案。新词:Millenarian 千禧年派/Wesleyan 卫斯理宗/Apollyon 亚玻伦。数字锚点改阿拉伯数字复检 exit 0 |
| 2026-08-13 | the-redhill-sisterhood (98301B,47对块) | done | exit 1=数字锚点误报(11:05),结构满足; 委派子代理。假修女会团伙案。新词:Sister Anna/Arthur Lee 主谋/Portland 监狱 |
| 2026-08-13 | the-black-bag-left-on-a-doorstep (102046B,49对块) | done | exit 1=数字锚点误报(£30000/7:30),结构满足; 委派子代理(自行补术语表)。门阶黑皮包盗窃案。《朗诵者宝库》三篇朗诵篇目为全案关键。注:术语表并发写已重读干净追加 |
| 2026-08-13 | the-murder-at-troytes-hill (107312B,58对块) | done | exit 0; 委派子代理(自行补术语表)。坎伯兰边塞古堡凶杀案。新词:巡回法庭/地质锤/au revoir |
| 2026-08-13 | missing (121924B,62对块) | done | exit 1=数字锚点误报(Age 18→年十八),结构满足; 委派子代理。**全书最长篇61.5KB按§7分3段合并**。富家女失踪案。意语 Mia Madre 保留释义。Florence 佛罗伦萨/Buckingham 白金汉号 |
| 2026-08-13 | ★全书完 7/7 | — | pirkis《女侦探洛芙迪·布鲁克的经历》全 7 篇译完(100%)。本会话委派译全 7 篇(~355KB源文) |
