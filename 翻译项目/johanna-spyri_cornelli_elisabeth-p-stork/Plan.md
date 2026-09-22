# 翻译计划（johanna-spyri_cornelli_elisabeth-p-stork）

## 本计划信息

- **项目名称**：johanna-spyri_cornelli_elisabeth-p-stork（Cornelli）
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

共 10 篇，见 `translation_queue.csv`（合计 269KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-30 | 全书 10 章 | 完成 10/10 | 批次3首译整书（0/10 起步，06:34 上锁）；主 agent 预定核心定名 16 条防并行撞名，10 章委派子代理滚动译毕（终章 41.4KB 分 5 批流式无半块）；全书 10 件终验通过（ch5 一处「11 o'clock→十一点」数字锚点误报判过）；术语表累计 40+ 条（含 Maelinger/Malinger 同人异拼注记） |
