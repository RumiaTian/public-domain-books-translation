#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

path = r'C:\Users\HanTi\OneDrive\translate\翻译项目\zofia-nalkowska_women_michael-henry-dziewicki\译文\the-garden-of-red-flowers_part1.zh-CN.md'

content = """
===Original===
Quite aware that I am doing wrong, I let Martha look back into her past; and I even question her myself so as to bring before her eyes the long dismal perspective of her wounded love, I listen in the manner she likes best, calmly and without any show of compassion. Nor have I any for her, any more than for a fish that must needs live in cold water, or for a bat that cannot bear the sunlight. Martha likes to suffer, and\u2014perhaps for this very reason\u2014she is compelled to suffer. Indeed, she is something of a Sybarite in her almost abnormal sensitiveness to pain. She is fond of telling me all the petty foolish troubles of an injured wife; and this procures her an odd sense of what may be called a sort of enjoyment.

"But, all the same, there was a time once when he loved you, did he not?"

"Oh, Witold declares that up to now he has loved none but me!"

"Well, well; but then at what time did *this*\u2014the present phase begin? For some time at least, he must have been faithful to you."

"Oh, yes, for a few months. Quite at the beginning. Though I myself was never happy.\u2026 First of all, during the six weeks before our wedding, I was constantly a prey to such mystic terrors that I came near losing my senses. You know that I do not admit any of those hackneyed maxims of morality\u2014and yet I continually felt that some evil thing was afoot, and a day of reckoning close at hand. And besides, how intolerable then was the thought that now I *had* to marry him, however averse I might feel to the act; that now I had more at stake upon my side than he on his!"

"And afterwards, by the seaside?"

"Oh, then it was entrancing! I almost felt happy. But it lasted so short a time! Shortly after our arrival I fell sick, and grew unwieldy and weakly and plain. And then, if you can believe me, surrounded with all those marvels of nature and of art, I was always longing for Klosow, my own place!"

===Chinese===
我清楚地知道自己在做错事，但我还是让玛莎回顾她的过去；我甚至亲自询问她，以便将她受伤之爱的漫长惨淡前景呈现在她眼前。我以她最喜欢的方式倾听——冷静地，不露丝毫同情。我对她也确实没有同情，正如我对一条只能生活在冷水中的鱼、或一只不能忍受阳光的蝙蝠没有同情一样。玛莎喜欢受苦，而且——也许正因为如此——她被迫受苦。诚然，在她对痛苦近乎异常的敏感中，她有些像一个享乐主义者。她喜欢向我倾诉一个受伤妻子的所有琐碎愚昧的烦恼；这为她带来了一种奇异的享受感。

"可是，不管怎样，他曾经爱过你的，不是吗？"

"哦，维托尔德声称直到如今他只爱过我一个人！"

"好吧，好吧；那么*这种*状况——当前这个阶段——是从什么时候开始的呢？至少在一段时间里，他一定是忠于你的。"

"哦，是的，有几个月。就在最初的那段日子。虽然我自己从未幸福过。\u2026 首先，在我们婚礼前的六个星期里，我不断被种种神秘的恐惧所折磨，以至于差点失去理智。你知道我不接受那些陈腐的道德格言——但我一直感觉到某种邪恶的事物正在酝酿，清算的日子迫在眉睫。而且，现在想到我*不得不*嫁给他，无论我对这桩婚事有多反感，这想法是多么令人难以忍受；现在我这边押上的赌注比他那边要多得多！"

"后来呢，在海边？"

"哦，那时候真是迷人极了！我几乎感觉到了幸福。但它持续的时间太短了！到那里不久我就病了，变得笨重、虚弱、丑陋。而且，如果你愿意相信我，尽管周围有那么多自然与艺术的奇观，我却一直渴望着克洛索夫，我自己的地方！"
"""
with open(path, 'a', encoding='utf-8') as f:
    f.write(content)
print('Block 14 appended')
