# 翻译计划（达摩克利斯之剑）

## 本计划信息

- **项目名称**：达摩克利斯之剑
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-10 | - | 建项目 | 从 待翻译/达摩克利斯之剑 epub 提取正文、建术语表初版、生成队列 |
| 2026-08-10 | searchings.md | done | 四「寻觅」译完；39064 字节，check_bilingual.py exit=0，0 处错配；新增人名 Farrar=法拉尔、Preston=普雷斯顿、Forsyth=福赛斯，地名 Albemarle=阿尔伯马尔、Baltimore=巴尔的摩、Worth monument=沃斯纪念碑 |
| 2026-08-10 | a-day-at-the-bank.md | done | 十四「银行里的一天」译完；约 12.2KB 源文，19 对 Original/Chinese，check_bilingual.py exit=0，0 处错配；新增人名 Hopgood=霍普古德（表内已定）、Wheelock=威洛克、Folger=福尔杰，地名 Pearl Street=珍珠街，机构 Madison Bank=麦迪逊银行；Hamlet 题词「有一种神明塑造我们的结局，不论我们如何粗凿，终归徒然。」 |
| 2026-08-10 | from-a-to-z-2.md | done | 三十九「从甲到乙」译完；约 46.2KB 源文（爱德华·西尔维斯特致宝拉的长篇自白书），53 对 Original/Chinese，check_bilingual.py exit=0，0 处错配；新增人名 Edward Sylvester=爱德华·西尔维斯特、Ona Delafield=奥娜·迪拉菲尔德、Jacob Delafield=雅各布·迪拉菲尔德、Colonel Japha=杰法上校、Jacqueline Japha=雅克琳·杰法、Geraldine=杰拉尔丁、Cicely=西塞莉、Dr. Burton=伯顿医生，地名 Grotewell=格罗特韦尔、Colorado=科罗拉多、San Francisco=旧金山、Wall Street=华尔街、New York=纽约，机构 Government bonds=公债 |
| 2026-08-11 | the-poem.md | done | 二十三「诗」译完；约 17.7KB 源文（宝拉回村、贝琳达查问、村中游艺会朗诵长 ballad《新娘的护卫》、神秘老妇玛乔丽·哈姆林约谈），10 对 Original/Chinese（含 1 块为完整 ballad 原文/中译），check_bilingual.py exit=0，0 处错配；新增人名 Squire=乡绅及 ballad 内虚构人名 Beaufort=博福尔、Germain=日耳曼、Hugh=休、Enguerrand=昂盖兰、Sassard=萨萨尔、Raoul=拉乌尔、Maurice=莫里斯、Clement=克莱门、Jaspar=雅斯帕、Clarence=克拉伦斯、Sessamine=塞萨敏、Henri=亨利、Stephen=司蒂文，地名 Morency=莫朗西，作品 The Defence of the Bride=《新娘的护卫》、ballad=歌谣/民谣 |
