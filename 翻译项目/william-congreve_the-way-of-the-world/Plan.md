# 翻译计划：如此世道

## 本计划信息

- **项目名称**：william-congreve_the-way-of-the-world
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：连续（中篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。连续模式下由主 agent 直接执行。

## 篇目清单

由 `translation_queue.csv` 管理（12 篇，约 176KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-22 | act-i.md | 完成 | 35 块对照；check_bilingual 退出码 0（无错配）；首译定基调：对白「**角色.** 台词」，脚注编号全角括号（n） |
| 2026-08-22 | act-ii / act-iii | done | 两幕译成（26.3+35.0KB，45/49 对块，均 exit 0、0 可疑，逐行零缺失；歌按 AABB 韵式，脚注号 24-71 内联保留） |
| 2026-08-22 | act-iv / act-v / dedication / commendatory-verses / epigraph / dramatis-personae / prologue / epilogue / endnotes | done | 两代理并行译成（31.3+31.2+6.2+2.4+0.1+0.8+2.0+1.7+13.9KB，均 exit 0、0 可疑；订约一场逐句全译，三首诗分行等数，112 条尾注逐条对照）。全书 12/12（100%）收官 |
