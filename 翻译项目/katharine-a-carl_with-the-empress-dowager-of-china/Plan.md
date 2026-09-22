# 翻译计划（与慈禧太后在一起的日子）

## 本计划信息

- **项目名称**：与慈禧太后在一起的日子
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
| 2026-08-10 | - | 建项目 | 从 待翻译/与慈禧太后在一起的日子 epub 提取正文、建术语表初版、生成队列 |
| 2026-08-10 | introductory.md | done | 18420B，5块对照，check exit=1（仅1903数字锚点误报，数字实存） |
| 2026-08-11 | 本会话续译25篇（return-summer-palace-2 至 the-great-audience-hall） | done | 委派25篇，清宫专名一律中文原名还原。术语表大幅扩充：恭亲王/大公主/袁世凯/梁诚/溥伦/庆亲王/那桐/罗斯福/前门/哈德门/外务部/总理衙门/石舫/昆明湖/柯姑娘(Ker-Gonnia)/美拉/傻子/海洛/老佛爷/老祖宗/李莲英大总管/同治/文宗皇帝(咸丰)/端王/康有为/克林德男爵/瓦德西伯爵/热河/大沽/西安/万佛楼/景泰蓝/西山/正大光明殿/大朝殿/奉先殿/万寿节/抬阁/花盆底鞋/玉如意/庚子拳乱/石(picul)/两(tael)等。各篇check_bilingual exit=0(少数数字锚点误报已核实)。本项目 28/37，剩9篇todo(the-chinese-new-year-official-audience/the-festival-of-the-harvest-moon/the-literary-tastes/the-palace-eunuchs/the-palace-of-the-emperor-s-father/the-steam-launch/the-summer-palace-and-its-grounds/the-winter-palace/the-young-empress-and-ladies-of-the-court) |
| 2026-08-11 | her-majesty-the-empress-dowager（首次）/ return-to-the-summer-palace（首次）/ the-chinese-new-year-official-audience / the-festival-of-the-harvest-moon | 失败（保持 todo） | 多次触发「Network connection failed for the provider request」瞬时网络故障（非内容/限额问题），clean失败无半成品。her-majesty与return-to-the-summer-palace重试成功；the-chinese-new-year-official-audience与the-festival-of-the-harvest-moon留待下次cron重试 |
