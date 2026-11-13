# 翻译计划：幸运的贝拉里翁

## 本计划信息

- **项目名称**：rafael-sabatini_bellarion-the-fortunate
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（50 篇，约 796KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-11-13 | 阶段汇总（19–28/50，共 10 篇） | 完成 | 完成 `the-battle-of-travo.md`、`the-arrest.md`、`the-camisade.md`、`the-champion.md`、`the-commune-of-milan.md`、`the-count-of-pavia.md`、`the-countess-of-biandrate.md`、`the-battle-of-novi.md`（重试一次通过）、`the-fruitless-wooing.md`、`the-door-ajar.md`，全部通过 `check_bilingual.py` 与 `check_coverage.py` 校验，新术语已并入 `术语表.md`。 |
| 2026-11-13 | 阶段汇总（累计 35/50） | 暂停 | 含首轮 17 篇及后续 `the-grey-friar.md`、`the-hostage.md`、`the-inheritance.md`、`the-knight-bellarion.md`、`the-last-fight.md`、`the-lord-bellarion.md`、`the-marquis-theodore.md`、`the-miracle-of-the-dogs.md`（均通过 `check_bilingual.py` 与 `check_coverage.py` 校验），累计完成 35/50（剩余 15 篇）；按指令暂停子代理并同步至 GitHub。 |
