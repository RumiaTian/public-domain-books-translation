# -*- coding: utf-8 -*-
"""Build the complete bilingual file by reading original English and adding Chinese translations."""
import os, re

SRC = r'C:\Users\HanTi\OneDrive\translate\翻译项目\thornton-w-burgess_green-forest-stories\原文\blacky-the-crow.md'
DST = r'C:\Users\HanTi\OneDrive\translate\翻译项目\thornton-w-burgess_green-forest-stories\译文\blacky-the-crow.zh-CN.md'

with open(SRC, 'r', encoding='utf-8') as f:
    src = f.read()

# Split source into sections by ## headers
sections = re.split(r'(?=^## )', src, flags=re.MULTILINE)
# sections[0] is empty or the main title
# sections[1] is "## Blacky the Crow" (main title)
# sections[2] is "## I Blacky the Crow Makes a Discovery"
# etc.

# Chinese section title translations
CN_TITLES = {
    "Blacky the Crow": "乌鸦布莱基",
    "I Blacky the Crow Makes a Discovery": "乌鸦布莱基有了新发现",
    "II Blacky Makes Sure": "布莱基去确认",
    "III Blacky Finds Out Who Owns the Eggs": "布莱基查明蛋的主人",
    "IV The Cunning of Blacky": "布莱基的诡计",
    "V Blacky Calls His Friends": "布莱基召唤朋友们",
    "VI Hooty the Owl Doesn't Stay Still": "猫头鹰胡蒂不肯老实待着",
    "VII Blacky Tries Another Plan": "布莱基换个计划",
    "VIII Hooty Comes to Mrs. Hooty's Aid": "胡蒂赶来帮助胡蒂太太",
    "IX Blacky Thinks of Farmer Brown's Boy": "布莱基想到了布朗农夫的儿子",
    "X Farmer Brown's Boy and Hooty": "布朗农夫的儿子和胡蒂",
    "XI Farmer Brown's Boy Is Tempted": "布朗农夫的儿子受到了诱惑",
    "XII A Treetop Battle": "树顶之战",
    "XIII Blacky Has a Change of Heart": "布莱基回心转意",
    "XIV Blacky Makes a Call": "布莱基去拜访",
    "XV Blacky Does a Little Looking About": "布莱基四处查看",
    "XVI Blacky Finds Other Signs": "布莱基发现了其他迹象",
    "XVII Blacky Watches a Queer Performance": "布莱基看到一件怪事",
    "XVIII Blacky Becomes Very Suspicious": "布莱基起了疑心",
    "XIX Blacky Makes More Discoveries": "布莱基有了更多发现",
    "XX Blacky Drops a Hint": "布莱基给了一句暗示",
    "XXI At Last Blacky Is Sure": "布莱基终于确认了",
    "XXII Blacky Goes Home Happy": "布莱基开心地回家了",
    "XXIII Blacky Calls Farmer Brown's Boy": "布莱基叫来了布朗农夫的儿子",
    "XXIV Farmer Brown's Boy Does Some Thinking": "布朗农夫的儿子想了些事",
    "XXV Blacky Gets a Dreadful Shock": "布莱基受到了巨大的打击",
    "XXVI Why the Hunter Got No Ducks": "猎人为什么没打到鸭子",
    "XXVII The Hunter Gives Up": "猎人放弃了",
    "XXVIII Blacky Has a Talk with Dusky the Black Duck": "布莱基和黑鸭达斯基谈了谈",
    "XXIX Blacky Discovers an Egg": "布莱基发现了一个蛋",
    "XXX Blacky Screws Up His Courage": "布莱基鼓起了勇气",
    "XXXI An Egg That Wouldn't Behave": "一个不听话的蛋",
    "XXXII What Blacky Did with the Stolen Egg": "布莱基拿偷来的蛋怎么办",
}

# For each section, we need Chinese translations of the content
# We'll store them keyed by section number
# The translations are stored as lists of (english_paragraph, chinese_paragraph) pairs
# For poetry sections, we store (english_poem, chinese_poem)

# Since we can't include all translations in this script (too large),
# we'll create a framework and then fill in translations section by section.

# For now, let's write the structure with placeholders
# and then we'll fill in the actual translations

print(f"Source file has {len(sections)} sections")
for i, sec in enumerate(sections):
    first_line = sec.strip().split('\n')[0][:80]
    print(f"  [{i}] {first_line}")
