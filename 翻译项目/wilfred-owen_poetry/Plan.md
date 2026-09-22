# 翻译计划（wilfred-owen_poetry）

## 本计划信息

- **项目名称**：wilfred-owen_poetry（Poetry）
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

共 4 篇，见 `translation_queue.csv`（合计 46KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-23 | endnotes.md | done | 3 条尾注一区块，退出码 0；定名：Wilfred Owen=威尔弗雷德·欧文 |
| 2026-08-23 | introduction.md | done | 8 块（萨松引言散文），退出码 0；定名：Siegfried Sassoon=西格弗里德·萨松、Strange Meeting=《奇异的会面》、Apologia Pro Poemate Meo=《为我诗作一辩》、Greater Love=《更大的爱》 |
| 2026-08-23 | poetry.md | done | 31 块（25 首诗逐首成块，共 752 诗行/110 诗节，逐行对应、空行同位），结构契约全过，退出码 1 仅 3 处数字锚点误报（篇末日期按诗集体例作中文数字：November 1917／5th December 1917／23rd September 1918）；Original 831 行与源文（清洗制表符/零宽字符后）逐字符一致；定名：A Terre=《入土》、Anthem for Doomed Youth=《命定青年的颂歌》、S.I.W.=《自伤》、Exposure=《暴露》、Disabled=《伤残》等 24 个诗题及军语（crump=重炮弹、Tommy=大兵）回填术语表 |
| 2026-08-23 | preface.md | done | 1 块（12 行箴言体自序，逐行对应、空行同位），退出码 0；标题「Preface1」之 1 为尾注锚点，按数字照搬原则保留于英文侧；定名：Prussia=普鲁士、Flanders=弗兰德斯。全书 4 篇全部完成 |
