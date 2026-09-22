# Plan（噩梦隐修院）

---

## 本计划信息

- **项目名称**：thomas-love-peacock_nightmare-abbey（噩梦隐修院，Nightmare Abbey）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态 / 执行模式**：中篇 / 连续（主 agent 逐章直译，见项目说明.md）

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
00-epigraph.md,1.1,todo
chapter-1.md,14.2,todo
...
```

---

## 执行步骤（agent 按此推进，两种模式共用）

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（风格黄金样本；无则跳过）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物口癖全文一致（Toobad 的「魔鬼已来到你们中间」、Raven 的曲意逢迎、Listless 的慵懒腔），照黄金样本风格译。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并（罗马数字照搬）。
- 术语一致：抽查 5 个术语词，全文译法统一。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```

### 7. 回填状态（双写）
`status` 从 `doing` 改 `done`，改两处：① 项目 `translation_queue.csv`；② 根 `translation_queue.csv` 对应行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 0 | 题词 | 00-epigraph.md | 1.1KB | todo |
| 1 | 第一章 | chapter-1.md | 14.2KB | todo |
| 2 | 第二章 | chapter-2.md | 6.1KB | todo |
| 3 | 第三章 | chapter-3.md | 8.8KB | todo |
| 4 | 第四章 | chapter-4.md | 6.9KB | todo |
| 5 | 第五章 | chapter-5.md | 7.3KB | todo |
| 6 | 第六章 | chapter-6.md | 13.3KB | todo |
| 7 | 第七章 | chapter-7.md | 16.3KB | todo |
| 8 | 第八章 | chapter-8.md | 9.3KB | todo |
| 9 | 第九章 | chapter-9.md | 8.4KB | todo |
| 10 | 第十章 | chapter-10.md | 11.7KB | todo |
| 11 | 第十一章 | chapter-11.md | 14.3KB | todo |
| 12 | 第十二章 | chapter-12.md | 9.6KB | todo |
| 13 | 第十三章 | chapter-13.md | 12.9KB | todo |
| 14 | 第十四章 | chapter-14.md | 5.3KB | todo |
| 15 | 第十五章 | chapter-15.md | 5.6KB | todo |
| 16 | 尾注 | endnotes.md | 3.2KB | todo |

---

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-22 | 00-epigraph.md | done | 首译定基调：3 对块，退出码 0。巴特勒诗体讽刺、琼森对白喜剧腔、拉伯雷法语照搬括注；术语按术语表（《人人扫兴》等） |
| 2026-08-22 | chapter-8.md | done | 9.3KB，8 对块，check_bilingual 退出码 0 |
| 2026-08-22 | chapter-9.md | done | 8.4KB，11 对块，check_bilingual 退出码 0 |
| 2026-08-22 | chapter-10.md | done | 11.7KB，8 对块，check_bilingual 退出码 0 |
| 2026-08-22 | chapter-2.md | done | 6.1KB，7 对块，check_bilingual 退出码 0；先验哲学黑话腔、斯克罗普七金灯台独白定式 |
| 2026-08-22 | chapter-3.md | done | 8.8KB，10 对块，check_bilingual 退出码 0；玛丽奥内塔登场（allegro vivace/andante doloroso 音乐术语照搬括注）、斯克罗普混血盟誓名场面、Toobad 撞楼梯 |
| 2026-08-22 | chapter-11.md | done | 14.3KB，20 对块（含两支歌的韵文），check_bilingual 退出码 0 |
| 2026-08-22 | chapter-4.md | done | 6.9KB，10 对块，check_bilingual 退出码 0；父子快问快答、必然性哲学术语混战（unconsentaneous 等意译不留英文）、骷髅盏饮马德拉威胁一幕 |
| 2026-08-22 | chapter-12.md | done | 9.6KB，13 对块，check_bilingual 退出码 0 |
| 2026-08-22 | chapter-5.md | done | 7.3KB，12 对块，check_bilingual 退出码 0；转入「**人物.** 台词」剧本体（粗体保留）；意语唱词 Zitti zitti 照搬括注；书评三连（《魔鬼人》《保罗·琼斯》《唐宁街评论》）按术语表 |
| 2026-08-22 | chapter-13.md | done | 12.9KB，16 对块，check_bilingual 退出码 0 |
| 2026-08-22 | chapter-14.md | done | 5.3KB，11 对块，check_bilingual 退出码 0 |
| 2026-08-22 | chapter-6.md | done | 13.3KB，11 对块，check_bilingual 退出码 0；塞琳达出走引子、但丁/蓝魔清谈、弗洛斯基康德式长篇独白（综合推理/无穷级数）、灰衣修士歌五行体逐行对译 |
| 2026-08-22 | chapter-15.md | done | 5.6KB，7 对块（含两封块引信件），check_bilingual 退出码 0 |
| 2026-08-22 | endnotes.md | done | 3.2KB，7 对块（14 条尾注），check_bilingual 退出码 0 |
| 2026-08-22 | chapter-7.md | done | 16.3KB，18 对块，check_bilingual 退出码 0；阿斯特里亚斯人鱼学考据、法图醉腔法语照搬括注（mermaid/merry maid 双关存音存义）、esse/percipi 论拦腰插诗行 |
