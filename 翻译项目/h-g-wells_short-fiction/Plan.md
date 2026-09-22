# 翻译计划（H·G·威尔斯短篇小说集）

## 本计划信息

- **项目名称**：H·G·威尔斯短篇小说集
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-10 | - | 建项目 | 从 待翻译/H·G·威尔斯短篇小说集 epub 提取正文、建术语表初版、生成队列 |
| 2026-08-10 | the-stolen-bacillus.md | done | 黄金样本定调。28781 字节，check_bilingual 退出码 0（10 对标记成对、0 错配）。术语：Bacteriologist=细菌学家、cholera=霍乱、bacillus=杆菌、microscope=显微镜；人名 Minnie=明妮、Ravachol=拉瓦肖尔、Vaillant=瓦扬；地名 Haverstock Hill=哈弗斯托克山、Camden Town=卡姆登镇、Havelock Crescent=哈夫洛克新月街、Waterloo Bridge=滑铁卢桥、Wellington Street=惠灵顿街、Great Saint Andrew's Street=大圣安德鲁街、Hampstead=汉普斯特德。 |
| 2026-08-10 | the-jilting-of-jane.md | done | 29861 字节，check_bilingual 退出码 0（10 对标记成对、0 错配）。术语：人名 Jane=简、Euphemia=欧菲米娅、William=威廉、George（叙述者）=乔治、Barnabas Baux=巴纳巴斯·博克斯、Maynard=梅纳德、Mr. Piddingquirk=皮丁柯克；地名 South Kensington=南肯辛顿；the elder Miss Maitland=梅特兰家大小姐；Home for the Dying=临终安养院；Plymouth Brother=普利茅斯兄弟会。 |
