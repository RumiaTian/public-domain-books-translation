#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

path = r'C:\Users\HanTi\OneDrive\translate\翻译项目\zofia-nalkowska_women_michael-henry-dziewicki\译文\the-garden-of-red-flowers_part1.zh-CN.md'

content = """
===Original===
A smile passed over her face. Then she gave a long shudder and closed her eyes fast.

Starting up on a sudden, she joined her hands behind her bare and shapely neck.

"If you knew, Janka," she whispered, "if you only knew how I love him! If you knew how I am longing for him every moment when he is away! If you knew how fondly, how wildly, how madly I love the exceeding sweetness of his mouth!"

===Chinese===
一丝微笑掠过她的脸。然后她打了一个长长的寒颤，紧紧闭上了眼睛。

她突然坐起身来，将双手合拢在裸露而匀称的颈后。

"你知道吗，扬卡，"她低声说道，"你可知道我有多么爱他！你可知道在他离开的每一个瞬间，我有多么渴望他！你可知道我多么温柔地、多么狂野地、多么疯狂地爱着他那无比甜美的嘴唇！"
"""
with open(path, 'a', encoding='utf-8') as f:
    f.write(content)
print('Block 18 appended')
