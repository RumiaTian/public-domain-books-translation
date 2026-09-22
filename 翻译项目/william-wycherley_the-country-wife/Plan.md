# 翻译计划：乡村妻子

## 本计划信息

- **项目名称**：william-wycherley_the-country-wife
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：连续（中篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。连续模式下由主 agent 直接执行。

## 篇目清单

由 `translation_queue.csv` 管理（10 篇，约 186KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-22 | act-i.md | done | 24.7KB，46 对块，check_bilingual 退出码 0；首篇定基调（对白「**角色.**」格式，人名定名见术语表） |
| 2026-08-22 | act-ii.md | done | 29.8KB，43 对块，check_bilingual 退出码 0 |
| 2026-08-22 | act-iii.md | done | 36.0KB，50 对块，check_bilingual 退出码 0 |
| 2026-08-22 | act-iv.md | done | 断点重派译成（46.2KB，82 对块，exit 0、0 可疑，775 行逐行零缺失；「瓷器一场」双关等效再现）。术语表追加 16 条 |
| 2026-08-22 | act-v / introduction / prologue / epilogue / epigraph / endnotes | done | 一批译成（38.9+4.3+1.2+1.5+0.2+3.7KB，58/3/4/4/1/17 对块，均 exit 0、0 可疑，逐行零缺失；收场诗/饮酒歌按行对应，双关等效）。全书 10/10（100%）收官 |
