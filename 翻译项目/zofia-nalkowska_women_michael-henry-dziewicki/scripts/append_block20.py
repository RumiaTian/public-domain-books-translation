#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

path = r'C:\Users\HanTi\OneDrive\translate\翻译项目\zofia-nalkowska_women_michael-henry-dziewicki\译文\the-garden-of-red-flowers_part1.zh-CN.md'

content = """
===Original===
I went to call upon her today, in the place of Martha, who is constantly unwell. She was by herself; for Wildenhoff, of course, like all husbands of his kind, either was no longer at home, or had not yet come back.

She tried to interest me by talking, as her custom is, about herself.

"My outward appearance, when all is said in its favour that can be said, is insufficient to explain the extraordinary success I have all my life had with men. My only ability\u2014call it an art if you like\u2014consists in influencing men by an appeal to their lower natures. That is the only way to succeed with them: for all of them are mere animals\u2014all!"

She offered me some fruit, taking up the vase containing it with the gesture of a "hetaira" of old days, presenting a goblet of golden wine.

"You see," she said, "I am an epicure. I want to get as much as I can out of life, and I know how to get it. With nothing but champagne and songs and flowers life would pall upon me very soon; so I like now and then to get the atmosphere of an 'At Home': for instance, with the Imszanskis. As to her, I don't know whether she is really purer than the atmosphere of a private supper-room: at all events, her style of corruption is peculiar\u2014more Gothic\u2014and the virus is more skilfully inoculated. I like to take a rest, and spend some quiet evenings in my family circle, teach little Sophy her alphabet, or pass sleepless nights in penance and vigil and sombre meditations. After which, I may perform a sudden 'pirouette,' Paris style, and blow from afar a farewell kiss to husband, Sophy, mamma, grandmamma\u2014and virtue!"

She laughed merrily.

"The future of the nations is not what I am looking forward to. No, I am resolved to get for myself the greatest possible amount of happiness, under the circumstances in which I am placed.\u2026 You will say I am a mere product of environment; well, let it be so. But mind: the way I live harms no one. If I am contented, so is my husband, and so are my admirers as well."

"And their wives too?" I hazarded.

"Well, but is it my fault if they are fools? Now, I'll tell you what. Never have I taken a man from a woman he loved. I am not of those whose sole aim is to make difficult conquests."

She added, after a pause:

"For ever so long (and that you must surely know) Imszanski has been quite indifferent to his wife."

===Chinese===
我今天代替一直生病的玛莎去拜访她。她独自一人；因为维尔登霍夫当然像他那一类的所有丈夫一样，要么已经不在家了，要么还没回来。

她试图以谈论自己（这是她的习惯）来引起我的兴趣。

"我的外表，当所有能说的好话都说完之后，仍然不足以解释我一生中在男人身上取得的非凡成功。我唯一的能力\u2014\u2014你若愿意，可以称之为一种艺术\u2014\u2014在于通过诉诸男人的低等本性来影响他们。这是在他们身上取得成功的唯一途径：因为他们全都是畜生\u2014\u2014全是！"

她给我递了一些水果，以古代"艺妓"手持金杯呈献的姿态端起装水果的花瓶。

"你看，"她说，"我是一个享乐主义者。我想从生活中尽可能多地获取，而且我知道如何获取。如果只有香槟、歌曲和鲜花，生活很快就会让我厌倦；所以我喜欢时不时地感受一下'会客日'的氛围：比如在伊姆尚斯基家。至于她，我不知道她是否真的比私人晚宴的氛围更纯洁：无论如何，她的堕落风格很独特\u2014\u2014更哥特式\u2014\u2014而病毒的接种更为巧妙。我喜欢休息，在我的家庭圈子里度过一些安静的夜晚，教小索菲她的字母表，或者在忏悔、守夜和阴郁的冥想中度过不眠之夜。然后，我可以来一个突然的'旋转'，巴黎式的，从远处向丈夫、索菲、妈妈、外婆\u2014\u2014还有美德\u2014\u2014抛去一个告别的飞吻！"

她愉快地笑了。

"民族的未来并不是我所期待的。不，我决心在自己所处的环境中获取尽可能多的幸福。\u2026 你会说我不过是环境的产物；好吧，就算是吧。但请注意：我的生活方式不伤害任何人。如果我满足了，我的丈夫也满足了，我的崇拜者们也同样如此。"

"他们的妻子也是吗？"我试探性地问道。

"那他们自己愚蠢，能怪我吗？我来告诉你吧。我从来没有从一个女人手中夺走一个她所爱的男人。我不是那种以艰难的征服为唯一目标的人。"

她停顿了一下，补充道：

"已经有很长一段时间了（你一定知道）伊姆尚斯基对他的妻子已经完全无动于衷了。"
"""
with open(path, 'a', encoding='utf-8') as f:
    f.write(content)
print('Block 20 appended')
