# 翻译计划（r-a-lafferty_short-fiction）

## 本计划信息

- **项目名称**：r-a-lafferty_short-fiction（Short Fiction）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置 | 人工 |
| `术语表.md` | 翻译硬约束层，每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列（file,size_kb,status） | 翻译前改 doing，完成后改 done（双写根表） |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`（9 步：读配置→取 todo→doing→读源文→翻译→自检→check_bilingual→双写 done→日志）。

## 篇目清单

共 10 篇，见 `translation_queue.csv`（合计 212KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-24 | all-the-people.md | done | 21KB，30 块，check 退出码 0；定基调篇：受限人/过滤中心/锡人托尼/辉光等定名入术语表 |
| 2026-08-24 | aloys.md | done | 15KB，18 块，check 退出码 0；阿卢瓦·福尔考-奥格/威利·麦吉利/残骸镇/假镍币酒吧等定名 |
| 2026-08-24 | dream-world.md | done | 13KB，19 块，check 退出码 0；巴斯科姆·斯威斯古德/特蕾莎·亚拿尼亚/阿格尼丝/绿雨/疣人梦等定名 |
| 2026-08-24 | in-the-garden.md | done | 19KB，30 块，check 退出码 0；哈阿达玛/哈瓦/小探针号/艾佩尔/蛇油山姆等定名；51% 数字锚点误报已修正为阿拉伯数字 |
| 2026-08-24 | mcgonigals-worm.md | done | 16KB，20 块，check 退出码 0；麦戈尼格尔虫/麦虫/希克尔氏病/新生不能（adynatogenesis）等定名 |
| 2026-08-24 | seven-day-terror.md | done | 13KB，21 块，check 退出码 0；威洛比家七娃/消隐器/假镍币酒吧（沿用）/威利·麦吉利（沿用）等定名 |
| 2026-08-24 | sodom-and-gomorrah-texas.md | done | 14KB，27 块，check 退出码 0；曼努埃尔/穆拉/圣马格达莱纳/新达那厄/小人儿等定名；西语词 italic 保留附注 |
| 2026-08-24 | the-polite-people-of-pudibundia.md | done | 19KB，27 块，check 退出码 0；马洛/普迪人/小于马洛一百万倍的马洛（百万小马洛）/恭敬球/米茨等定名 |
| 2026-08-24 | the-six-fingers-of-time.md | done | 52KB，57 块，check 退出码 0；查尔斯·文森特/梅森医生/祖巴林·希姆/深坑/无面人/加速状态等定名；泥板引文两处破折号留白依原文分别处理 |
| 2026-08-24 | the-weirdest-world.md | done | 31KB，42 块，check 退出码 0；软团（blob）/大蛆/乔治·艾伯特·勒罗伊·埃勒里·麦金托什/通讯球/弹射迫击炮/银河漂流带/太空无能症/欢腾会等定名；全书 10 篇收官 |
