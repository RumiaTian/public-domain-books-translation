# Plan（《交给皮史密斯吧》翻译计划）

> 从 `prompts/翻译计划模板.md` 复制建立。执行步骤、CSV 格式等通用规范见模板，此处为本书实例。

---

## 本计划信息

- **项目名称**：p-g-wodehouse_leave-it-to-psmith（《交给皮史密斯吧》，P. G. 伍德豪斯）
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

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 布兰丁斯城堡密谋 | 01-dark-plottings-at-blandings-castle.md | 47.2KB | todo |
| 2 | 皮史密斯登场 | 02-enter-psmith.md | 32.0KB | todo |
| 3 | 伊芙借伞 | 03-eve-borrows-an-umbrella.md | 10.3KB | todo |
| 4 | 蜂子俱乐部的难堪一幕 | 04-painful-scene-at-the-drones-club.md | 6.1KB | todo |
| 5 | 皮史密斯求职 | 05-psmith-applies-for-employment.md | 14.0KB | todo |
| 6 | 埃姆斯沃思勋爵会见诗人 | 06-lord-emsworth-meets-a-poet.md | 51.3KB | todo |
| 7 | 巴克斯特起疑 | 07-baxter-suspects.md | 35.9KB | todo |
| 8 | 湖上谈心 | 08-confidences-on-the-lake.md | 50.5KB | todo |
| 9 | 皮史密斯雇男仆 | 09-psmith-engages-a-valet.md | 61.1KB | todo |
| 10 | 诗歌朗诵会上的轰动事件 | 10-sensational-occurrence-at-a-poetry-reading.md | 53.6KB | todo |
| 11 | 几乎全与花盆有关 | 11-almost-entirely-about-flowerpots.md | 48.7KB | todo |
| 12 | 花盆话题再谈 | 12-more-on-the-flowerpot-theme.md | 19.0KB | todo |
| 13 | 皮史密斯会客 | 13-psmith-receives-guests.md | 48.3KB | todo |
| 14 | 皮史密斯就任新职 | 14-psmith-accepts-employment.md | 22.4KB | todo |

> 共 14 章，约 500KB。各章 >50KB 者（06/08/09/10）按通用翻译引擎第七节分段处理。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-10-19 | 04-painful-scene-at-the-drones-club.md | done | 6.1KB 短章；36 对块逐段对照，check_bilingual 退出码 0（无错配）；术语按表（蜂子俱乐部/皮史密斯/沃尔德威克），新增词已补术语表；隐形字符（U+FEFF/U+00A0/U+200A）字节级保真 |
| 2026-10-19 | 03-eve-borrows-an-umbrella.md（伊芙借伞） | done | 10.3KB→约22KB，42 对块对照；check_bilingual 退出码 0（结构/标题/语义全过） |
| 2026-10-19 | 05-psmith-applies-for-employment.md（皮史密斯求职） | done | 14.0KB→约21KB，29 对块对照（104 段对称）；check_bilingual 退出码 0；术语按表（Psmith/P-smith 不发音、同志、《名誉攸关》、蜂子俱乐部），英文段落含 U+FEFF×26/U+00A0×4 字节级保真 |
| 2026-10-19 | 02-enter-psmith.md（皮史密斯登场） | done | 32.0KB→约71KB，206 对块逐段对照；check_bilingual 退出码 0（结构/标题/语义全过）；章内小节号循 `### I / I` 体例；术语按表（Psmith/P-smith 不发音、同志、康斯坦丝姑妈、小克拉克），新增词（晨邮报/体育快报/罗洛·芒特福德等）已补术语表；原文 U+FEFF×65/U+00A0×9/U+200A×23 经脚本字节级保真 |
| 2026-10-19 | 01-dark-plottings-at-blandings-castle.md（布兰丁斯城堡密谋） | done | 47.2KB→约100KB，277 对块逐段对照（章首广告块引 15 行结构保真）；check_bilingual 退出码 0（结构/标题/语义全过，无锚点误报）；章内小节号循 `### I / I` 体例；术语按表（布兰丁斯/埃姆斯沃思/能干的巴克斯特/康斯坦丝/麦克托德/皮维），广告口号定名「把这事交给皮史密斯吧！」，新增词（拉特兰郡/什鲁斯伯里/园艺艺术论/单身汉舞会/报端赛马行家）已补术语表；原文 U+FEFF×120/U+00A0×59/U+200A×48 经拼装脚本字节级保真 |
| 2026-10-19 | 06-lord-emsworth-meets-a-poet.md（埃姆斯沃思勋爵会见诗人） | done | 51.3KB→约107KB，244 对块逐段对照（超 50KB 大章，5 批译文 JSON 落盘、脚本拼装）；check_bilingual 结构/标题全过，仅 1 处数字锚点误报（源文 '78 译作 1878 年）；章内小节号循 `### I / I` 体例（与 01/02 章一致）；术语按表（埃姆斯沃思勋爵/麦克托德/麦卡利斯特/弗雷迪/资深保守俱乐部），接头切口「明天诺森伯兰有雨。」「于庄稼有益。」定名；新增词条（皮卡迪利宫殿酒店/资深保守俱乐部/紫杉幽径/蜀葵/《鱼贩公报》/《多宝鱼赫伯特》等）已补术语表；原文 U+FEFF×74/U+00A0×37/U+200A×23 经拼装脚本字节级保真 |
| 2026-10-20 | 07-baxter-suspects.md | 主模型直译 | 200行/190对块 | check_bilingual 退出码0，0错配 | done |
| 2026-10-20 | 08-confidences-on-the-lake.md | 主模型直译 | 311行/304对块 | check_bilingual 退出码0，0错配 | done |
| 2026-10-20 | 09-psmith-engages-a-valet.md | 主模型直译 | 361行/354对块 | check_bilingual 退出码0，0错配 | done |
| 2026-10-20 | 10-sensational-occurrence-at-a-poetry-reading.md | 主模型直译 | 281行/274对块 | check_bilingual 退出码0，0错配 | done |
| 2026-10-20 | 11-almost-entirely-about-flowerpots.md | 主模型直译 | 221行/210对块 | check_bilingual 退出码0，0错配 | done |
| 2026-10-20 | 12-more-on-the-flowerpot-theme.md | 主模型直译 | 83行/82对块 | check_bilingual 退出码0，0错配 | done |
| 2026-10-20 | 13-psmith-receives-guests.md | 主模型直译 | 314行/308对块 | check_bilingual 退出码0，0错配 | done |
| 2026-10-20 | 14-psmith-accepts-employment.md | 主模型直译 | 156行/155对块 | check_bilingual 退出码0，0错配 | done |
