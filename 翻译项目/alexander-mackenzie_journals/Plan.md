# 翻译计划：alexander-mackenzie_journals

> 复制自 `prompts/翻译计划模板.md`，按 9 步执行流程推进。

---

## 本计划信息

- **项目名称**：alexander-mackenzie_journals（麦肯齐探险日志：1789 北抵冰洋、1793 西达太平洋）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/历史古籍.md
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

## translation_queue.csv 格式

```
file,size_kb,status
01-introduction.md,3.8,todo
02-preface.md,8.6,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `04-1789-chapter-i.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，委派模式由子代理逐篇执行）

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/历史古籍.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（作为风格黄金样本；无则跳过）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。块对照格式、标记规则、完整性禁令见 `prompts/通用翻译引擎.md` 第五、六节。

### 5. 自检
完整性（无漏段、无截断）、块对称、标题「英文 / 中文」合并、术语一致（对照术语表抽查）。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```

### 7. 回填状态（双写）
`doing` → `done`，改 ① 项目 `translation_queue.csv`；② 根 `translation_queue.csv` 中 `alexander-mackenzie_journals,<本篇名>` 行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2 取下一篇 `todo`。委派模式由主 agent 调度（并发 ≤ 3）。

---

## 篇目清单

| # | 篇名 | 源文 | 状态 |
|---|------|------|------|
| 1 | 引言（Robert Waite） | 01-introduction.md | todo |
| 2 | 自序 | 02-preface.md | todo |
| 3 | 第一部标题页：1789 年赴冰洋 | 03-part-1-frozen-ocean-1789.md | todo |
| 4 | 1789 年日志·第一章 | 04-1789-chapter-i.md | todo |
| 5 | 1789 年日志·第二章 | 05-1789-chapter-ii.md | todo |
| 6 | 1789 年日志·第三章 | 06-1789-chapter-iii.md | todo |
| 7 | 1789 年日志·第四章 | 07-1789-chapter-iv.md | todo |
| 8 | 1789 年日志·第五章 | 08-1789-chapter-v.md | todo |
| 9 | 1789 年日志·第六章 | 09-1789-chapter-vi.md | todo |
| 10 | 1789 年日志·第七章 | 10-1789-chapter-vii.md | todo |
| 11 | 第二部标题页：1793 年赴太平洋 | 11-part-2-pacific-ocean-1793.md | todo |
| 12 | 1793 年日志·第一章 | 12-1793-chapter-i.md | todo |
| 13 | 1793 年日志·第二章 | 13-1793-chapter-ii.md | todo |
| 14 | 1793 年日志·第三章 | 14-1793-chapter-iii.md | todo |
| 15 | 1793 年日志·第四章 | 15-1793-chapter-iv.md | todo |
| 16 | 1793 年日志·第五章 | 16-1793-chapter-v.md | todo |
| 17 | 1793 年日志·第六章 | 17-1793-chapter-vi.md | todo |
| 18 | 1793 年日志·第七章 | 18-1793-chapter-vii.md | todo |
| 19 | 1793 年日志·第八章 | 19-1793-chapter-viii.md | todo |
| 20 | 1793 年日志·第九章 | 20-1793-chapter-ix.md | todo |
| 21 | 1793 年日志·第十章 | 21-1793-chapter-x.md | todo |
| 22 | 1793 年日志·第十一章 | 22-1793-chapter-xi.md | todo |
| 23 | 1793 年日志·第十二章 | 23-1793-chapter-xii.md | todo |
| 24 | 1793 年日志·第十三章 | 24-1793-chapter-xiii.md | todo |
| 25 | 附录（地图目次） | 25-appendix.md | todo |
| 26 | 尾注 | 26-endnotes.md | todo |
| 27 | 插图目录 | 27-list-of-illustrations.md | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
