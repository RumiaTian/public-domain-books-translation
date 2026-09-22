# 翻译计划（E·F·本森幽灵故事集）

## 本计划信息

- **项目名称**：E·F·本森幽灵故事集
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
| 2026-08-10 | - | 建项目 | 从 待翻译/E·F·本森幽灵故事集 epub 提取正文、建术语表初版、生成队列 |
| 2026-08-10 | the-dust-cloud.md | done | 58642 字节，check_bilingual 退出码 1（仅 1 处数字锚点误报：1:45 p.m.→一点四十五分，译文已含数字，可忽略；11 对标记成对、0 真实错配，逐块段落数核对一致）。注意：原指令误将该篇归入 h-g-wells_short-fiction，实际属 e-f-benson_ghost-stories，经用户确认后按本森项目翻译。术语补充：人名 Harry Combe-Martin=哈里·康伯-马丁、Guy Elphinstone=盖伊·埃尔芬斯通、Mrs. Morrison=莫里森太太、Jack（司机）=杰克；地名 Hunstanton=亨斯坦顿、Bircham=伯彻姆、Norwich=诺里奇、Dunwich=邓维奇、King's Lynn=金斯林、Suffolk=萨福克、the Norfolk Broads=诺福克湖区；车名 Napier=纳皮尔、Amédée=阿梅代。 |
| 2026-08-10 | and-the-dead-spake / at-abdul-ali-s-grave / at-the-farmhouse | done | 委派批1。dead-spake 41.6KB exit0（霍顿爵士/加布里埃尔太太/纽瑟姆台地/言语中枢/死者留声机）；abdul-ali 26.3KB exit0（阿卜杜勒·阿里/艾哈迈德黑巫术/卢克索/心灵研究学会）；farmhouse 35.4KB exit0（艾尔斯福德/乔纳斯·特雷纳黑巫术/马雷斯/煤油） |
| 2026-08-10 | between-the-lights / caterpillars | done | 委派批2。between-lights 24.9KB exit0（钱德勒/萨瑟兰郡/格伦卡伦/第二视觉）；caterpillars 18.5KB exit0（卡斯卡纳别墅/塞斯特里·莱万泰/英格利斯氏癌虫 Cancer 双关） |
| 2026-08-10 | gavon-s-eve | 失败（保持 doing） | 子代理中途触发 [1301] 内容安全过滤（非速率限额）。已写 47KB 半成品且 check_bilingual 结构通过(18对)，但无法确认未被截断，按容错规则删半成品、status 保持 doing、跳过续译，留待下次重试 |
| 2026-08-10 | how-fear-departed / in-the-tube / inscrutable-decrees | done | 委派批3。how-fear-departed 31.9KB exit0（佩弗里尔/蓝衣夫人/达尔林普尔）；in-the-tube 30.4KB exit0（卡林/佩尔爵士/星质体/布朗普顿）；inscrutable-decrees 61.0KB exit0（罗克家族/林科特/降神会/皮克牌） |
| 2026-08-10 | machaon / mr-tilly-s-s-ance / mrs-amworth | done | 委派批4。machaon 36KB exit0（圣詹姆斯医院/金凤蝶马卡翁/控制灵）；mr-tillys-seance 33.1KB exit0（提利先生/灵界向导/降神会/布拉瓦茨基夫人）；mrs-amworth 36KB exit0（阿姆沃斯太太/吸血鬼/厄克姆/马克斯利） |
| 2026-08-10 | negotium-perambulans / outside-the-door / roderick-s-story | done | 委派批5。negotium 64.6KB exit0（波拉恩/博利索/西勒诺斯/隐多珥交鬼妇人）；outside-the-door 16.5KB exit0（奥尔德威奇/丹尼森/转桌术）；rodericks-story 23KB exit0（卡杜/奥尔顿/元素精灵） |
| 2026-08-10 | the-bus-conductor / the-cat / the-confession-of-charles-linkworth | done | 委派批6。bus-conductor 18KB exit0（格兰杰/奥斯伯顿/见鬼/渡过去）；the-cat 30KB exit0（阿林厄姆/默里克/提香/玫瑰品种）；linkworth 32.3KB exit0（蒂斯代尔医生/林克沃斯/狱卒/赦罪） |
| 2026-08-10 | the-gardener / the-horror-horn / the-house-with-the-brickkiln | done | 委派批7。the-gardener 28.7KB exit0（格兰杰/通灵板/贝德兰姆）；horror-horn 55.5KB exit0（英格拉姆/翁盖莫霍恩峰/阿尔胡贝尔/恩加丁）；brickkiln 24KB exit0（特雷弗·梅杰/辛格尔顿/弗兰克林/刘易斯/干蝇钓） |
| 2026-08-10 | the-man-who-went-too-far / the-other-bed / the-outcast | done | 委派批8。man-too-far 45.5KB exit0（哈尔顿/达西/潘/新林）；other-bed 43.8KB exit0（美景酒店/休谟/兰伯特）；outcast 37.1KB exit0（阿克斯/阿灵顿/斯昆石/盎格鲁以色列派） |
| 2026-08-10 | the-shootings-of-achnaleish / the-terror-by-night / the-thing-in-the-hall | done | 委派批9（末批）。achnaleish 62.2KB exit1（仅2处数字锚点跨块误报，契约通过；阿赫纳利什/萨瑟兰郡/桑迪·罗斯/盖尔语）；terror-by-night 15.9KB exit0（洛里默/恩德利医生/达沃斯）；thing-in-the-hall 50.5KB exit0（阿什顿医生/菲尔德/沙尔科/催眠术/元素精）。本项目：28 done / 1 doing(gavon-s-eve 待重试) / 0 todo |
| 2026-08-11 | gavon-s-eve.md | done | 重试（上次 [1301] 中断）。主代理直译 23.1KB 66 对块，exit0，3 处数字锚点误报（14/128/15）均已在译文中正确呈现。术语补充：人名 Hugh Graham=休·格雷厄姆、Sandy=桑迪、Catrine Gordon=卡特琳·戈登、Mrs. Macpherson=麦克弗森太太；地名 Gavon=加文、Sutherland=萨瑟兰郡、Gavon Loch=加文湖、Brora=布罗拉、Inverness=因弗内斯、Picts' pool=皮克特人潭、Pict castle=皮克特人城堡、Gavon Lodge=加文钓屋；专名 Adonis=阿多尼、Gavon's Eve=加文之夜、《Superstitions of Sutherlandshire》=《萨瑟兰郡迷信志》。**本项目全部 29/29 done，100% 完成** ✅ |
