# Plan：Bulldog Drummond

## 本计划信息

- **项目名称**：h-c-mcneile_bulldog-drummond
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置 | 人工 |
| `术语表.md` | 翻译硬约束层 | agent / 人工 |
| `translation_queue.csv` | 任务队列（file,size_kb,status） | 翻译前 doing，完成 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出 | 翻译 agent 产出 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置→取 todo→doing→读源文→翻译→自检→check_bilingual.py→双写 done→日志→循环）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
- 2026-09-30 07:47｜批次3直启子代理｜00-prologue.md 完成，check_bilingual 通过
- 2026-09-30 07:50｜批次3直启子代理｜01-in-which-he-takes-tea-at-the-carlton-and-is-surprised.md 完成，check_bilingual 通过
- 2026-09-30 11:21｜批次3直启子代理｜02-in-which-he-journeys-to-godalming-and-the-game-begins.md 完成，check_bilingual 通过
- 2026-10-01 06:50｜批次3直启子代理｜03-in-which-things-happen-in-half-moon-street.md 完成，check_bilingual 通过（[1301]后带免责声明重派成功）
- 2026-10-01 06:55｜批次3直启子代理｜04-in-which-he-spends-a-quiet-night-at-the-elms.md 完成，check_bilingual 通过
- 2026-10-01 07:05｜批次3直启子代理｜05-in-which-there-is-trouble-at-goring.md 完成，check_bilingual 通过
- 2026-10-01 07:20｜批次3直启子代理｜06-in-which-a-very-old-game-takes-place-on-the-hog-s-back.md 完成，check_bilingual 通过
- 2026-10-01 07:40｜批次3直启子代理｜07-in-which-he-spends-an-hour-or-two-on-a-roof.md 完成，check_bilingual 通过
- 2026-10-01 07:45｜批次3直启子代理｜08-in-which-he-goes-to-paris-for-a-night.md 完成，check_bilingual 通过
- 2026-10-01 11:20｜批次3直启子代理｜09-in-which-he-has-a-near-shave.md 完成，check_bilingual 通过
- 2026-10-02 06:32｜批次3直启子代理｜10-in-which-the-hun-nation-decreases-by-one.md 完成，check_bilingual 通过
- 2026-10-02 06:42｜批次3直启子代理｜11-in-which-lakington-plays-his-last-coup.md 完成，check_bilingual 通过
- 2026-10-02 06:50｜批次3直启子代理｜12-in-which-the-last-round-takes-place.md 完成，check_bilingual 通过

- 2026-10-02 07:12｜批次3直启子代理｜13-epilogue.md 完成，check_bilingual 通过（尾声内联完成）

## 完书纪要
- 2026-10-02 07:13｜批次3直启｜全书 14/14 队列项完成（序幕+12章+尾声），check_bilingual 全部通过，锁已删除。第十六章完工。第III章曾 [1301] 拦截一次，免责重派成功。
