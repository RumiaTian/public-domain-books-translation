# -*- coding: utf-8 -*-
"""Build bilingual translation file by reading the original and adding Chinese translations.
This approach avoids re-typing all the English text."""
import os, re

SRC = r'C:\Users\HanTi\OneDrive\translate\翻译项目\thornton-w-burgess_green-forest-stories\原文\blacky-the-crow.md'
DST = r'C:\Users\HanTi\OneDrive\translate\翻译项目\thornton-w-burgess_green-forest-stories\译文\blacky-the-crow.zh-CN.md'

# Read the original file
with open(SRC, 'r', encoding='utf-8') as f:
    src_text = f.read()

# Split into sections by ## headers
# The original has sections like:
# ## Blacky the Crow
# ## I Blacky the Crow Makes a Discovery
# ## II Blacky Makes Sure
# etc.

# Chinese translations for section titles
TITLE_MAP = {
    "Blacky the Crow": "乌鸦布莱基",
    "I Blacky the Crow Makes a Discovery": "I 乌鸦布莱基有了新发现",
    "II Blacky Makes Sure": "II 布莱基去确认",
    "III Blacky Finds Out Who Owns the Eggs": "III 布莱基查明蛋的主人",
    "IV The Cunning of Blacky": "IV 布莱基的诡计",
    "V Blacky Calls His Friends": "V 布莱基召唤朋友们",
    "VI Hooty the Owl Doesn't Stay Still": "VI 猫头鹰胡蒂不肯老实待着",
    "VII Blacky Tries Another Plan": "VII 布莱基换个计划",
    "VIII Hooty Comes to Mrs. Hooty's Aid": "VIII 胡蒂赶来帮助胡蒂太太",
    "IX Blacky Thinks of Farmer Brown's Boy": "IX 布莱基想到了布朗农夫的儿子",
    "X Farmer Brown's Boy and Hooty": "X 布朗农夫的儿子和胡蒂",
    "XI Farmer Brown's Boy Is Tempted": "XI 布朗农夫的儿子受到了诱惑",
    "XII A Treetop Battle": "XII 树顶之战",
    "XIII Blacky Has a Change of Heart": "XIII 布莱基回心转意",
    "XIV Blacky Makes a Call": "XIV 布莱基去拜访",
    "XV Blacky Does a Little Looking About": "XV 布莱基四处查看",
    "XVI Blacky Finds Other Signs": "XVI 布莱基发现了其他迹象",
    "XVII Blacky Watches a Queer Performance": "XVII 布莱基看到一件怪事",
    "XVIII Blacky Becomes Very Suspicious": "XVIII 布莱基起了疑心",
    "XIX Blacky Makes More Discoveries": "XIX 布莱基有了更多发现",
    "XX Blacky Drops a Hint": "XX 布莱基给了一句暗示",
    "XXI At Last Blacky Is Sure": "XXI 布莱基终于确认了",
    "XXII Blacky Goes Home Happy": "XXII 布莱基开心地回家了",
    "XXIII Blacky Calls Farmer Brown's Boy": "XXIII 布莱基叫来了布朗农夫的儿子",
    "XXIV Farmer Brown's Boy Does Some Thinking": "XXIV 布朗农夫的儿子想了些事",
    "XXV Blacky Gets a Dreadful Shock": "XXV 布莱基受到了巨大的打击",
    "XXVI Why the Hunter Got No Ducks": "XXVI 猎人为什么没打到鸭子",
    "XXVII The Hunter Gives Up": "XXVII 猎人放弃了",
    "XXVIII Blacky Has a Talk with Dusky the Black Duck": "XXVIII 布莱基和黑鸭达斯基谈了谈",
    "XXIX Blacky Discovers an Egg": "XXIX 布莱基发现了一个蛋",
    "XXX Blacky Screws Up His Courage": "XXX 布莱基鼓起了勇气",
    "XXXI An Egg That Wouldn't Behave": "XXXI 一个不听话的蛋",
    "XXXII What Blacky Did with the Stolen Egg": "XXXII 布莱基拿偷来的蛋怎么办",
}

# Print section titles found in source
print("Sections found in source:")
for line in src_text.split('\n'):
    if line.startswith('## '):
        print(f"  {line}")

print("\nDone analyzing. This script provides the framework for bilingual assembly.")
print("Full translation content will be added in subsequent steps.")
