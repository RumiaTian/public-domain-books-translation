# 《失踪者巷》前半卷独立审校报告

- 审校日期：2026-10-23
- 质量等级：A
- 一句话结论：前半卷23篇全量逐段比对通过，无漏译截断与严重硬伤，文风古典考究，仅见极微瑕疵

---

## 一、审校范围与工程基准

- 审校对象：《失踪者巷》前半卷（Part A）
- 篇目清单：共23篇
  - 01-dedication.zh-CN.md
  - 02-preface.zh-CN.md
  - 03-the-knollys-family.zh-CN.md
  - 04-a-visit-from-mr-gryce.zh-CN.md
  - 05-i-am-tempted.zh-CN.md
  - 06-i-succumb.zh-CN.md
  - 07-a-ghostly-interior.zh-CN.md
  - 08-a-strange-household.zh-CN.md
  - 09-a-sombre-evening.zh-CN.md
  - 10-the-first-night.zh-CN.md
  - 11-on-the-stairs.zh-CN.md
  - 12-a-new-acquaintance.zh-CN.md
  - 13-secret-instructions.zh-CN.md
  - 14-men-women-and-ghosts.zh-CN.md
  - 15-the-phantom-coach.zh-CN.md
  - 16-gossip.zh-CN.md
  - 17-i-forget-my-age-or-rather-remember-it.zh-CN.md
  - 18-the-flower-parlor.zh-CN.md
  - 19-lucetta-fulfils-my-expectation-of-her.zh-CN.md
  - 20-loreen.zh-CN.md
  - 21-the-flower-parlor-2.zh-CN.md
  - 22-the-second-night.zh-CN.md
  - 23-a-knot-of-crape.zh-CN.md
- 工作模式：100% 逐块逐段对照通读，严守只读隔离
- 工具验证：check_bilingual.py 校验 23 篇全部通过，块标记与段落结构完整契合

---

## 二、主要缺陷与修改建议

### 发现的问题与建议
- 缺陷定位一：13-secret-instructions.zh-CN.md 第 56 行
  - 原文：tell your sister of this fainting fit
  - 现译：倘若我看不出有什么正当的理由，非得把你这回昏厥告诉你妹妹不可，我自然缄口不言
  - 问题描述：长幼称谓倒置，露塞塔（次女）请求不要告知洛琳（长女/姐姐），阿米莉亚答语中将 sister 误译为「妹妹」
  - 修复建议：将「告诉你妹妹」修正为「告诉你姐姐」

- 缺陷定位二：15-the-phantom-coach.zh-CN.md 第 174-177 行
  - 原文：Mrs. Carter 跨段叙述幽灵马车历史
  - 现译：第 174 行末尾多出闭合后引号「』」」，第 177 行后续内容又以「「人们发现...」开头
  - 问题描述：连续多段引语排版标点欠妥，段落尚未结束即提前闭合后引号
  - 修复建议：按多段引语通用规范，删除第 174 行末尾多余的外层后引号「」」，保留内层套引号「』」，在全段叙述终了的第 177 行末尾统合闭合

- 缺陷定位三：20-loreen.zh-CN.md 第 72 行
  - 原文：That of Lucetta’s namesake... won her lover’s heart away from her
  - 现译：「露塞塔那位同名前辈的传说，」我解释道。「她就是那位连夜骑马追赶女儿的人，那女儿把她情郎的心夺了去
  - 问题描述：长对话末尾遗漏闭合后引号，因英文底本排印遗漏引号导致译文末尾亦缺少后引号，下一段已切换为洛琳发言
  - 修复建议：在第 72 行句末补全闭合后引号「」」

- 缺陷定位四：23-a-knot-of-crape.zh-CN.md 第 14 行
  - 原文：it was also the first time I had seen the three together
  - 现译：这也是头一回，我看见她们姊妹三个聚在一处
  - 问题描述：家庭成员性别指称瑕疵，在场三人为诺利斯小姐、威廉和露塞塔，威廉为兄弟，译文使用「她们姊妹三个」不当
  - 修复建议：修正为「他们兄妹三人」或「他们三人」

- 缺陷定位五：23-a-knot-of-crape.zh-CN.md 第 97 行
  - 原文：the Magnolia grandiflora
  - 现译：学名*Magnolia grandiflora*，广玉兰
  - 问题描述：外文暴露于括号外且主次顺序倒置
  - 修复建议：调整为主从次序并加括号，修正为「广玉兰（学名：*Magnolia grandiflora*）」

---

## 三、综合评审明细

- 完整性：23 篇各章节段落与块标记 100% 完整对应，双语对照结构契约完全符合，无任何漏译、漏段、段落重复或内容截断
- 准确性：准确再现原文叙事逻辑与微言大义，人物情感层层递进，主客体关系分明，无时间线颠倒或严重逻辑反转
- 术语与命名体系：严格遵循术语表硬约束，阿米莉亚·巴特沃斯、格赖斯先生、阿尔西娅·诺利斯、露塞塔、洛琳、特罗姆先生、失踪者巷、花房等关键专有名词及地名统一规范
- 文学质感与古典哥特侦探小说风格：用词典雅克制，准确传达十九世纪末期维多利亚式悬疑小说的典雅文质与从容冷峻的叙事口吻，叙述层次分明
- 格式规范与标点：双语块结构、标题对齐完全符合规范，对话引号使用规范，仅两处标点配对与一处外文括号次序细节建议优化