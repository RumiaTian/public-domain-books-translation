# 《失踪者巷》后半卷独立审校报告

- 审校日期：2026-10-23
- 质量等级：A
- 一句话结论：后半卷24篇全量逐段对照通读完毕，无漏译截断与重大逻辑反转，古典文风典雅洗练，发现两处局部缺陷并提供精准行号与修复建议

---

## 一、审校范围与工程基准

- 审校对象：《失踪者巷》后半卷（Part B）
- 篇目清单：共24篇
  - 24-questions.zh-CN.md
  - 25-mother-jane.zh-CN.md
  - 26-the-third-night.zh-CN.md
  - 27-forward-and-back.zh-CN.md
  - 28-room-3-hotel-carter.zh-CN.md
  - 29-the-enigma-of-numbers.zh-CN.md
  - 30-trifles-but-not-trifling.zh-CN.md
  - 31-a-point-gained.zh-CN.md
  - 32-the-text-witnesseth.zh-CN.md
  - 33-an-intrusion.zh-CN.md
  - 34-in-the-cellar.zh-CN.md
  - 35-investigation.zh-CN.md
  - 36-strategy.zh-CN.md
  - 37-relief.zh-CN.md
  - 38-the-birds-of-the-air.zh-CN.md
  - 39-lucetta.zh-CN.md
  - 40-conditions.zh-CN.md
  - 41-the-dove.zh-CN.md
  - 42-an-hour-of-startling-experiences.zh-CN.md
  - 43-i-astonish-mr-gryce-and-he-astonishes-me.zh-CN.md
  - 44-a-few-words.zh-CN.md
  - 45-under-a-crimson-sky.zh-CN.md
  - 46-explanations.zh-CN.md
  - 47-epilogue.zh-CN.md
- 工作模式：100% 逐块逐段对照通读，严守只读隔离
- 工具验证：check_bilingual.py 校验 24 篇全部通过，块标记完整成对，段落对应整齐

---

## 二、主要缺陷与修改建议

### 发现的问题与建议

- 缺陷定位（一）：44-a-few-words.zh-CN.md 第 17 行
  - 原文：His usual lodging was with the family, but when the search was instituted, I suggested that he should remove himself to that eyrie back of the hay where you were sharp enough to detect him today.
  - 现译：他往常寄宿在诺利斯家，但搜查着手之后，我提议他挪到干草后头那处鹰巢似的高阁上去——今天您眼力够尖，正好在那儿把他识破了
  - 问题描述：主客体与事实指涉错误；前文已明确交代奥斯特兰德先生这一周一直寄宿在斯皮尔执事家（Mr. Ostrander, madam, has been spending the week with Deacon Spear），此处 with the family 承前指执事一家人；全书中诺利斯姐妹一直以为奥斯特兰德先生已失踪罹难，若寄宿在诺利斯家则与全书核心情节严重冲突
  - 修复建议：将「寄宿在诺利斯家」修正为「寄宿在执事家里」或「寄宿在斯皮尔执事家」

- 缺陷定位（二）：46-explanations.zh-CN.md 第 81-91 行
  - 原文：格赖斯先生跨越三段的长篇直接引语解说（第 76、84、86 行分别以英文双引号开头，第 86 行末尾闭合）
  - 现译：第 81 行段首有开引号「，第 89 行与第 91 行段首无开引号，第 91 行末尾遗漏闭合后引号「」」
  - 问题描述：长对话末尾遗漏闭合后引号，引语未正常闭合；且跨段长篇对话未补全各段段首开引号
  - 修复建议：在第 91 行句末补齐闭合后引号「」」；依多段连续引语排版规范，第 89 行与第 91 行段首亦可补充开引号「

- 缺陷定位（三）：46-explanations.zh-CN.md 第 23 行
  - 原文：信末署名包含双星号 Amelia Butterworth
  - 现译：信末署名包含双星号 阿米莉亚·巴特沃斯
  - 问题描述：信件落款处残留双星号粗体标记，格式规范宜保持一致性
  - 修复建议：建议清除该处署名的双星号标记，保持纯正文本格式

---

## 三、综合评审明细

- 完整性：24 篇各章节段落与块标记 100% 完整对应，双语对照结构契约完全符合，无任何漏译、漏段、段落重复或内容截断
- 准确性：准确再现十九世纪末侦探小说的复杂推演与心理博弈，叙事逻辑严密，伏笔收束得当；仅见一处代词所指主客体笔误
- 术语与命名体系：严格遵循术语表硬约束，阿米莉亚·巴特沃斯、格赖斯先生、简大妈、特罗姆先生、斯皮尔执事、奥斯特兰德先生、萨拉森、花房等关键专有名词及地名统一规范，前后一致
- 文学质感与古典哥特侦探小说风格：用词典雅，句式凝练稳重，译笔传神刻画出巴特沃斯小姐傲娇敏锐的独身女侦探口吻与特罗姆先生的阴鸷狂乱，文学质感上乘
- 格式规范与标点：双语块结构、标题对齐完全符合工程规范，仅一处长对话末尾遗漏引号及一处签名格式细节需微调优化
