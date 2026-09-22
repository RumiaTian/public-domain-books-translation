#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

path = r'C:\Users\HanTi\OneDrive\translate\翻译项目\zofia-nalkowska_women_michael-henry-dziewicki\译文\the-garden-of-red-flowers_part1.zh-CN.md'

content = """
===Original===
"A few weeks before George\u2019s birth, Witold for the first time spent the night away from home. I sat up all the time, and looked out through the window over the sea. Ah, that night!

"The servants had gone to bed long before. There was a great storm, with boisterous gusts of wind: and I gave ear to the never-ceasing roar of the waves. You know what a visionary I am. I at once fancied Witold must have been sailing in a boat to the farther shore of the bay, and gone down to the bottom of the sea. I was horribly alarmed for his sake; and for a time, not an inkling of the truth flashed upon my mind. The horror of my fancy came over me so strongly that I quite forgot all about his past.\u2026 For I believed with faith unbounded in his immense love for me, and should have scouted, as a ridiculous notion, the idea of his possibly being unfaithful. I was out of my mind with terror. I counted the hours that went by, in agonized expectation, surrounded with the dark cloudy night, and hearing the terrific howling and rolling of the winds and waves.\u2026 Ah, that night!

"In the morning he came in.

"With the mien of a youthful page, he doffed his hat to the ground in a courtly bow, and stood motionless in my presence, humble, clasping his hands: then, in a soft sweet voice somewhat broken by emotion, he said, in an accent of dismay:

"\u2018Ah! my lady, I am afraid, greatly afraid!\u2019

"I did not rush to welcome him, nor did I cry out aloud: I felt too weak for any display of joy. But at that first instant, in the sole knowledge that he was living, an infinite intensity of quiet and fathomless and endless bliss flooded my heart: and I was minded to exclaim, like Mary Magdalene at the Sepulchre, \u2018Rabboni: which is to say, Master!\u2019

"And then up rose the sun!

"He had never before appeared so admirable to me, as in that attitude of a page of Medieval times, and with the playful humility of his bright smile; he had never yet been so loved by me, so dear beyond all measure. No, I had never been so glad in all my life as in this one short instant of consolation!

"And yet they say that women have intuitive minds!

"I was as it were caught and suspended in an aerial cobweb that stretched over an abyss of waters; and there I gazed upon the golden glitter of the morning landscape now that the tempest was over\u2014gazed into the blue and shimmering stillness. Beneath me, under the bridge of hanging gossamer, rolled the sombre sea of dread and death; before me rose the sea of life, crimson and bloodred in hue. But I\u2014I saw nothing there, save the dawn and the sunshine."

===Chinese===
"在乔治出生前几周，维托尔德第一次在外过夜。我整夜坐着，透过窗户望着大海。啊，那个夜晚！

"仆人们早就上床了。一场大风暴，裹挟着猛烈的狂风呼啸而来：我倾听着海浪永不停息的咆哮。你知道我是个多么爱幻想的人。我立刻想象维托尔德一定是乘着小船驶向海湾的对岸，沉入了海底。我为他惊恐万分；有一段时间，真相的丝毫暗示都没有闪过我的脑海。我的幻想带来的恐惧如此强烈，以至于我完全忘记了他过去的种种。\u2026 因为我毫无保留地相信他对我深沉的爱，若说他可能不忠，我本会视之为荒谬的念头而嗤之以鼻。我因恐惧而发狂。我在黑暗多云的夜色中，在可怕的狂风怒涛的咆哮翻滚声中，痛苦地数着流逝的每一个小时。\u2026 啊，那个夜晚！

"早晨他回来了。

"带着一个年轻侍从的姿态，他以宫廷式的鞠躬将帽子低垂至地面，然后在我面前一动不动地站定，谦卑地合着双手：然后，用一个略带激动的柔软甜美声音，以一种惊惶的语调说道：

"'啊！夫人，我很害怕，非常害怕！'

"我没有冲上去迎接他，也没有大声叫喊：我太虚弱了，无力表达任何喜悦。但在那一瞬间，仅仅知道他还活着，一种无限深沉的、无底的、无尽的幸福便淹没了我的心：我真想像抹大拉的马利亚在坟墓前那样呼喊：'拉波尼！就是说，夫子！'

"然后太阳升起了！

"他从未像那时那样令我觉得可爱——以那中世纪侍从的姿态，以他明朗微笑中顽皮的谦逊；他也从未被我那样地爱过，那样无可估量地珍贵。不，我一生中从未像在这短暂的安慰瞬间中那样快乐！

"然而人们却说女人有直觉的心灵！

"我仿佛被一张悬在深渊之上的空中蛛网捕捉和悬吊在那里；我在那里凝望着风暴过后晨景的金色辉光\u2014\u2014凝望着蓝色的、闪烁的宁静。在我脚下，在悬挂的游丝之桥下，翻滚着恐惧与死亡的阴沉大海；在我面前升起的是生命之海，殷红如血色。但我\u2014\u2014我在那里什么也没看见，只看见了黎明和阳光。"
"""
with open(path, 'a', encoding='utf-8') as f:
    f.write(content)
print('Block 16 appended')
