# 翻译计划（《漫游者》）

## 本计划信息

- **项目名称**：漫游者（约瑟夫·康拉德）
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

## translation_queue.csv 格式

```
file,size_kb,status
chapter-1.md,15.9,todo
chapter-2.md,22.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `chapter-1.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

## 篇目清单

见 `translation_queue.csv`（16 章，chapter-1.md 至 chapter-16.md）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-12 | chapter-1/2/3 (15.9+22.1+24.4KB) | done ×3 | exit 0; 法语词/地名/航海术语多 |
| 2026-08-12 | chapter-4/5/6 (22.5+23.5+21.4KB) | done ×3 | exit 0; 新词:Vincent/Bolt/Amelia/Nelson/Petite Passe/Passe/Ali-Kassim 等 |
| 2026-08-12 | chapter-7 (80537B,81对块) | done | exit 0; 委派子代理。新词:瓜达富伊角/巴利阿里/巴巴里/桑给巴尔/卡马尼奥勒/con amore/François 弗朗索瓦。法语特色词照录释义(Sacrebleu/ça ira/Vive la République 等)。驼背残疾汉体貌与术语表「马德拉格的残疾汉(无腿骑驴)」略有出入,按现场描写译「残疾汉」 |
| 2026-08-12 | chapter-8 (68093B,53对块) | done | exit 0; 委派子代理。新词:苏库夫先生/撒丁岛/波拿巴/第一执政/海军省长/荣军院/英国囚船 pontoons/阿尔式女帽/帆驳船/小帆桁。法语词照录释义(Tiens! Vous voilà!/Un homme de cœur/Celui-là est un malin 等) |
| 2026-08-12 | chapter-9 (64310B,31对块) | done | exit 0; 委派子代理。新词:Testa Dura 硬脑袋/Poigne-de-Fer 铁拳(佩罗尔绰号)/demijohn 小酒坛/marinero 水手/pied-de-nez 拇指按鼻/Sam 西蒙斯本名。法语照录释义 |
| 2026-08-12 | chapter-10 (72979B,82对块) | done | exit 0; 委派子代理。新词:佩罗丝 Perose/阿尔勒 Arles/欧仁 Eugène(雷亚尔名)/abbé 神父/curé 本堂神父/sacristy 圣器室/nave 中殿/vespers 晚祷/breviary 日课经/confirmation 坚振礼/fichu 三角披肩/platanes 悬铃木。注:pontoon 本章作「浮码头」义,与表内 pontoons=英国囚船不同义项。法语照录释义 |
| 2026-08-12 | chapter-11 (67947B,49对块) | done | exit 0; 委派子代理(子代理自行补术语表)。新词:hein 嗯?/patronne 女主人/ci-devant 前贵族/Voyons 得啦/Allons—du courage 来拿出勇气/Mademoiselle Catherine 凯瑟琳小姐/Saracen 撒拉逊人/the Terror 恐怖统治/La Boyère 拉布瓦耶尔。法语照录释义 |
| 2026-08-12 | chapter-12 (43956B,70对块) | done | exit 0; 委派子代理。新词:Salins 萨兰(耶尔白沙滩)/Petite Passe 小水道(耶尔群岛航道)/ci-devant 前贵族/notre maître 我们的老大/cutter 舰载艇/master's mate 准尉/first lieutenant 大副/sailing master 舵手长。法语照录释义 |
| 2026-08-12 | chapter-13 (32073B,9对块) | done | exit 0; 委派子代理。新词:keelson 内龙骨/boarding pike 接舷长矛/handspike 撬棍/boathook 船钩/cutting-out expeditions 斩缆夺船突击/master-at-arms 纠察长/six bells in the first watch 头更六响钟 |
| 2026-08-12 | chapter-14 (85629B,64对块) | done | exit 0; 委派子代理。新词:Port-Admiral 港务海军上将/Toulon Admiralty 土伦海军部/coxswain 舵手/Nanette 娜奈特(白安哥拉猫)/garde-champêtre 乡间巡守/gendarmes 宪兵。法语照录释义 |
| 2026-08-12 | chapter-15 (115332B,38对块) | done | exit 0; 委派子代理。新词:Petite Passe 小水道/Cape Blanc 布朗角/cuddy 小舱房/Majorité 军港司令部/sabots 木鞋/Jean 让(雷亚尔信中称佩罗尔本名)/Rhône Valley 罗讷河谷/Ceylon 锡兰岛。法语照录释义 |
| 2026-08-12 | chapter-16 (92954B,36对块) | done | exit 1=数字锚点误报(40-ton 跨块),结构契约满足; **全书终章**,译至结尾桑树/海岸兄弟会段落无截断。委派子代理。Keats/Eugène/Jean/Cette/Genoa/Gibraltar/Brest 等遵表 |
| 2026-08-12 | ★全书完 16/16 | — | joseph-conrad_the-rover《漫游者》全部 16 章译完(100%)。本会话委派译 ch7-16 共 10 章 |
