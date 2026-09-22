# -*- coding: utf-8 -*-
"""Build the complete bilingual file. Reads English source, adds Chinese translations."""
import os, re

SRC = r'C:\Users\HanTi\OneDrive\translate\翻译项目\thornton-w-burgess_green-forest-stories\原文\blacky-the-crow.md'
DST = r'C:\Users\HanTi\OneDrive\translate\翻译项目\thornton-w-burgess_green-forest-stories\译文\blacky-the-crow.zh-CN.md'

with open(SRC, 'r', encoding='utf-8') as f:
    src = f.read()

# Split into sections by ## headers
parts = re.split(r'(?=^## )', src, flags=re.MULTILINE)
# parts[0] = empty/header stuff, parts[1] = ## Blacky the Crow, parts[2] = ## I ..., etc.

# Section title translations
CN = {}
CN[1] = "乌鸦布莱基"
CN[2] = "乌鸦布莱基有了新发现"
CN[3] = "布莱基去确认"
CN[4] = "布莱基查明蛋的主人"
CN[5] = "布莱基的诡计"
CN[6] = "布莱基召唤朋友们"
CN[7] = "猫头鹰胡蒂不肯老实待着"
CN[8] = "布莱基换个计划"
CN[9] = "胡蒂赶来帮助胡蒂太太"
CN[10] = "布莱基想到了布朗农夫的儿子"
CN[11] = "布朗农夫的儿子和胡蒂"
CN[12] = "布朗农夫的儿子受到了诱惑"
CN[13] = "树顶之战"
CN[14] = "布莱基回心转意"
CN[15] = "布莱基去拜访"
CN[16] = "布莱基四处查看"
CN[17] = "布莱基发现了其他迹象"
CN[18] = "布莱基看到一件怪事"
CN[19] = "布莱基起了疑心"
CN[20] = "布莱基有了更多发现"
CN[21] = "布莱基给了一句暗示"
CN[22] = "布莱基终于确认了"
CN[23] = "布莱基开心地回家了"
CN[24] = "布莱基叫来了布朗农夫的儿子"
CN[25] = "布朗农夫的儿子想了些事"
CN[26] = "布莱基受到了巨大的打击"
CN[27] = "猎人为什么没打到鸭子"
CN[28] = "猎人放弃了"
CN[29] = "布莱基和黑鸭达斯基谈了谈"
CN[30] = "布莱基发现了一个蛋"
CN[31] = "布莱基鼓起了勇气"
CN[32] = "一个不听话的蛋"
CN[33] = "布莱基拿偷来的蛋怎么办"

# Build output
out = []
out.append("## Blacky the Crow / 乌鸦布莱基\n\n")

for i in range(2, len(parts)):
    sec = parts[i]
    # Get section title (first line)
    lines = sec.strip().split('\n')
    title_line = lines[0]
    # Extract title text after "## "
    title_text = title_line[3:].strip()
    # Get content (everything after first line)
    content = '\n'.join(lines[1:]).strip()

    # Write merged title
    cn_title = CN.get(i, title_text)
    out.append(f"## {title_text} / {cn_title}\n\n")

    # Write English content
    out.append("===Original===\n")
    out.append(content + "\n\n")

    # For Chinese, we need paragraph-by-paragraph translation
    # We'll mark sections that need manual Chinese translation
    out.append("===Chinese===\n")
    out.append(f"[Chinese translation for section {title_text}]\n\n")

# Write output
os.makedirs(os.path.dirname(DST), exist_ok=True)
with open(DST, 'w', encoding='utf-8') as f:
    f.write(''.join(out))

print(f"Template file written: {os.path.getsize(DST)} bytes, {len(out)} blocks")
print("Now we need to fill in Chinese translations for each section.")
