# 翻译计划：一团乱麻

## 本计划信息

- **项目名称**：lewis-carroll_a-tangled-tale
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/学术著作.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（16 篇，约 152KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-22 | a-serpent-with-corners.md | 成功 | 7.2KB，10 对块，check 退出码 0；首篇定基调：对话用「」，Knot→乱结，Balbus→巴尔布斯，Hugh→休，Lambert→兰伯特，数字保留阿拉伯数字，脚注标 [n] |
| 2026-08-22 | appendix.md | 成功 | 81.3KB，74 对块，check 退出码 0；按引擎第七节分 7 段翻译后合并；读者化名中文定名（约 120 个），×/○ 排列图与缺失公式占位照搬，中古英语引诗保留原文附今译 |
| 2026-08-22 | chelsea-buns.md | 成功 | 11.0KB，13 对块，check 退出码 0；百分比保留阿拉伯数字+％，Coleridge《古舟子咏》戏仿引号保留 |
| 2026-08-22 | de-omnibus-rebus.md | 成功 | 5.2KB，6 对块，check 退出码 0；拉丁篇名意译「论万物」，grurmstipths→格鲁姆斯特普斯 |
| 2026-08-22 | eligible-apartments.md | 成功 | 8.0KB，12 对块，check 退出码 0；门牌号保留阿拉伯数字，房东方言口语化处理 |
| 2026-08-22 | endnotes.md | 成功 | 0.2KB，1 对块，check 退出码 0；洋泾浜词 Maskee 保留 |
| 2026-08-22 | epigraph.md | 成功 | 0.0KB，1 对块，check 退出码 0；拉丁题词附今译 |
| 2026-08-22 | excelsior.md | 成功 | 2.6KB，5 对块，check 退出码 0；仿古骑士腔（文白相间），篇名 Excelsior 拉丁语保留附注 |
| 2026-08-22 | her-radiancy.md | 成功 | 8.3KB，10 对块，check 退出码 0；Beaten/Star/Charm/Glory 去字母双关以括注英文保留，洋泾浜题词仿译 |
| 2026-08-22 | mad-mathesis.md | 成功 | 5.7KB，7 对块，check 退出码 0；train（裙裾/列车）双关括注英文，pail/pale 谐音括注 |
| 2026-08-22 | oughts-and-crosses.md | 成功 | 6.8KB，9 对块，check 退出码 0；oughts and crosses 统一「圈圈与叉叉」，与附录一致 |
| 2026-08-22 | list-of-illustrations.md | 成功 | 0.1KB，1 对块，check 退出码 0 |
| 2026-08-22 | petty-cash.md | 成功 | 7.6KB，9 对块，check 退出码 0；账目条目保留斜体，Habeas Corpus 括注 |
| 2026-08-22 | preface.md | 成功 | 0.5KB，1 对块，check 退出码 0 |
| 2026-08-22 | the-dead-reckoning.md | 成功 | 7.2KB，9 对块，check 退出码 0；称重数字与附录统一用阿拉伯数字，船长「我的」大写讽刺用斜体 |
| 2026-08-22 | to-my-pupil.md | 成功 | 0.3KB，1 对块，check 退出码 0；赠诗押韵仿译 |

全部 16 篇完成（152KB → 译文 16 篇，全部 check 退出码 0，状态双写，无 doing 残留）。
