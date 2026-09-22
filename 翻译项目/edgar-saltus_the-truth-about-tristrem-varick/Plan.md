# 翻译计划（edgar-saltus_the-truth-about-tristrem-varick）

## 本计划信息

- **项目名称**：edgar-saltus_the-truth-about-tristrem-varick（The Truth About Tristrem Varick）
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

共 19 篇，见 `translation_queue.csv`（合计 237KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-29 | 全书 19 项（17 章＋献词＋题词） | 完成 19/19 | 批次1三段并行（A/B/C 按体量均衡 76/84/76KB）一次通过，零[1301]零[1308]；收尾统一 10 处定名漂移（范诺登/罗亚尔/雅典娜俱乐部/蒂凡尼/蓓尔美尔/纽波特/「字母表」琼斯等，旧变体清零）；歌谣制表符缩进、管家吞音、U+FEFF/U+00A0/U+200A 逐字保真 |
