# Plan（新自由）

---

## 本计划信息

- **项目名称**：woodrow-wilson_the-new-freedom（新自由，The New Freedom）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/学术著作.md
- **术语表**：术语表.md
- **内容形态 / 执行模式**：短篇集 / 委派（子代理逐篇译，见项目说明.md）

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（逐段对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
00-dedication.md,0.2,todo
01-preface.md,1.5,todo
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
5. prompts/领域配置/学术著作.md
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

- 逐段对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 演说排比与设问的节奏、口语化插入语全书一致，照黄金样本风格译。

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
| 0 | 献词 | 00-dedication.md | 0.2KB | todo |
| 1 | 自序 | 01-preface.md | 1.5KB | todo |
| 2 | 一、旧秩序在改变 | 02-the-old-order-changeth.md | 30.2KB | todo |
| 3 | 二、何谓进步 | 03-what-is-progress.md | 22.8KB | todo |
| 4 | 三、自由人无需监护人 | 04-freemen-need-no-guardians.md | 24.7KB | todo |
| 5 | 四、生命来自土壤 | 05-life-comes-from-the-soil.md | 10.7KB | todo |
| 6 | 五、人民的议会 | 06-the-parliament-of-the-people.md | 21.0KB | todo |
| 7 | 六、要有光 | 07-let-there-be-light.md | 25.1KB | todo |
| 8 | 七、关税：保护还是特权 | 08-the-tariff-protection-or-special-privilege.md | 27.7KB | todo |
| 9 | 八、垄断还是机会 | 09-monopoly-or-opportunity.md | 30.1KB | todo |
| 10 | 九、仁慈还是正义 | 10-benevolence-or-justice.md | 31.8KB | todo |
| 11 | 十、恢复之路在于恢复 | 11-the-way-to-resume-is-to-resume.md | 34.8KB | todo |
| 12 | 十一、企业的解放 | 12-the-emancipation-of-business.md | 20.5KB | todo |
| 13 | 十二、解放一个民族的活力 | 13-the-liberation-of-a-people-s-vital-energies.md | 18.6KB | todo |

> 篇目清单中的章名中译仅供识别，各篇标题以译文内「英文 / 中文」合并格式为准，跨章保持一致。

---

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
