#!/usr/bin/env python3
"""Write translation blocks to the output file."""
import os

PATH = r'C:\Users\HanTi\OneDrive\translate\翻译项目\clara-reeve_the-old-english-baron\译文\the-old-english-baron_part1.zh-CN.md'

def write_block(text):
    with open(PATH, 'a', encoding='utf-8') as f:
        f.write(text)

# Block 2: Sir Philip meets peasant / learns news
write_block("""
===Original===
The youths returned to their sports, and Sir Philip mounted his horse and proceeded to the castle; he entered it with a deep sigh, and melancholy recollections. The baron received him with the utmost respect and courtesy. He gave a brief account of the principal events that had happened in the family of Lovel during his absence; he spoke of the late Lord Lovel with respect, of the present with the affection of a brother. Sir Philip, in return, gave a brief recital of his own adventures abroad, and of the disagreeable circumstances he had met with since his return home; he pathetically lamented the loss of all his friends, not forgetting that of his faithful servant on the way; saying he could be contented to give up the world, and retire to a religious house, but that he was withheld by the consideration, that some who depended entirely upon him, would want his presence and assistance; and, beside that, he thought he might be of service to many others. The baron agreed with him in opinion, that a man was of much more service to the world who continued in it, than one who retired from it, and gave his fortune to the church, whose servants did not always make the best use of it. Sir Philip then turned the conversation, and congratulated the baron on his hopeful family; he praised their persons and address, and warmly applauded the care he bestowed on their education. The baron listened with pleasure to the honest approbation of a worthy heart, and enjoyed the true happiness of a parent.

===Chinese===
青年们返回了他们的游戏，菲利普爵士翻身上马，径往城堡而去；他怀着一声深叹和满腔惆怅的记忆步入城堡。勋爵以最崇高的敬意和礼遇接待了他。勋爵简述了菲利普爵士离家期间洛弗尔家族发生的主要事件；他以敬重之情谈及已故的洛弗尔勋爵，以手足之情谈及现任的勋爵。菲利普爵士则回报以自己海外冒险经历的简要叙述，以及归国后所遭遇的种种不如意；他悲切地哀叹失去了所有的朋友，亦不忘提及途中忠仆之殒命；他说自己本可心甘情愿地放弃尘世、遁入修道院，但考虑到有些人完全仰赖于他，不能没有他的在场和援助；此外，他觉得自己还能为许多其他人效力。勋爵与他看法一致，认为一个留在尘世、为世人效力的人，远比一个隐遁出世、将财产捐给教会——其仆人未必总能善加运用——的人更为有用。菲利普爵士随后将话题转向，祝贺勋爵有如此可期的家庭；他夸赞了孩子们的容貌与举止，并热烈称许勋爵为他们教育所倾注的心血。勋爵欣然倾听一位赤诚之人的由衷赞许，享受着为人父母的真正幸福。

===Original===
Sir Philip then made further enquiry concerning Edmund, whose appearance had struck him with an impression in his favour.

"That boy," said the baron, "is the son of a cottager in this neighbourhood; his uncommon merit, and gentleness of manners, distinguish him from those of his own class; from his childhood he attracted the notice and affection of all that knew him; he was beloved everywhere but at his father's house, and there it should seem that his merits were his crimes; for the peasant, his father, hated him, treated him severely, and at length threatened to turn him out of doors; he used to run here and there on errands for my people, and at length they obliged me to take notice of him; my sons earnestly desired I would take him into my family; I did so about two years ago, intending to make him their servant; but his extraordinary genius and disposition have obliged me to look upon him in a superior light; perhaps I may incur the censure of many people, by giving him so many advantages, and treating him as the companion of my children; his merit must justify or condemn my partiality for him; however, I trust that I have secured to my children a faithful servant of the upper kind, and a useful friend to my family."

Sir Philip warmly applauded his generous host, and wished to be a sharer in his bounty to that fine youth, whose appearance indicated all the qualities that had endeared him to his companions.

===Chinese===
菲利普爵士随后进一步询问了关于埃德蒙的情况——这少年的外表给他留下了深刻的好感。

"那个孩子，"勋爵说，"是附近一个佃户的儿子；他非同寻常的才德和温文尔雅的举止使他脱颖而出，迥异于同等出身之人；他自幼便吸引了所有认识他的人的关注和喜爱；除了他的父亲家中，他在哪里都受人爱戴，而在家中，他的优点似乎反倒成了他的罪过——那个农夫，他的父亲，憎恶他，虐待他，最后竟威胁要将他赶出家门；他常替我的人跑腿办差，久而久之他们不得不引起了我的注意；我的儿子们恳切请求我将他收入家中；大约两年前我照做了，本想让他做孩子们的仆从；但他非凡的天资和品性迫使我不得不以更高的眼光看待他；或许我会因此招来许多人的非议——给他这许多优待，将他当作孩子们的同伴；他的品行必将为我对他的偏爱作出辩护或定罪；无论如何，我相信我为我的孩子们确保了一个忠诚的、上等的仆人，也为我的家族赢得了一位有益的朋友。"

菲利普爵士热情赞许了这位慷慨的东道主，并希望能参与他对这优秀少年的恩泽——那少年的外表表明，他身上汇聚了令同伴们珍爱的一切美德。

===Original===
At the hour of dinner the young men presented themselves before their Lord, and his guest. Sir Philip addressed himself to Edmund; he asked him many questions, and received modest and intelligent answers, and he grew every minute more pleased with him. After dinner the youths withdrew with their tutor to pursue their studies. Sir Philip sat for some time wrapt up in meditation. After some minutes, the baron asked him, "If he might not be favoured with the fruits of his contemplations?"

"You shall, my Lord," answered he, "for you have a right to them. I was thinking, that when many blessings are lost, we should cherish those that remain, and even endeavour to replace the others. My Lord, I have taken a strong liking to that youth whom you call Edmund Twyford; I have neither children nor relations to claim my fortune, nor share my affections; your Lordship has many demands upon your generosity: I can provide for this promising youth without doing injustice to anyone; will you give him to me?"

"He is a fortunate boy," said the baron, "to gain your favour so soon."

===Chinese===
到了用膳的时辰，年轻人们前来拜见勋爵及其客人。菲利普爵士主动与埃德蒙攀谈；他问了许多问题，得到的回答谦逊而睿智，他对那少年的好感每分每增。膳后，年轻人们随导师退下继续学业。菲利普爵士独坐沉思了良久。过了一会儿，勋爵问他："不知是否可以分享阁下冥想的成果？"

"当然可以，勋爵大人，"他答道，"您有权知晓。我在想，当许多祝福已逝，我们应当珍惜尚存的一切，甚至尽力弥补失去的。勋爵大人，我对您所说的埃德蒙·特怀福德那少年心生了强烈的好感；我无儿无女，亦无亲人来继承我的产业、分担我的感情；您对我的慷慨有许多需求之处：我可以在不亏欠任何人的情况下为这有为的少年提供出路；您肯将他让给我吗？"

"他真是个幸运的孩子，"勋爵说，"这么快就赢得了您的青睐。"

===Original===
"My Lord," said the knight, "I will confess to you, that the first thing that touched my heart in his favour, is a strong resemblance he bears to a certain dear friend I once had, and his manner resembles him as much as his person; his qualities deserve that he should be placed in a higher rank; I will adopt him for my son, and introduce him into the world as my relation, if you will resign him to me; What say you?"

"Sir," said the baron, "you have made a noble offer, and I am too much the young man's friend to be a hindrance to his preferment. It is true that I intended to provide for him in my own family; but I cannot do it so effectually as by giving him to you, whose generous affection being unlimited by other ties, may in time prefer him to a higher station as he shall deserve it. I have only one condition to make; that the lad shall have his option; for I would not oblige him to leave my service against his inclination."

"You say well," replied Sir Philip; "nor would I take him upon other terms."

"Agreed then," said the baron; "let us send for Edmund hither."

A servant was sent to fetch him; he came immediately, and his lord thus bespoke him.

"Edmund, you owe eternal obligations to this gentleman, who, perceiving in you a certain resemblance to a friend of his, and liking your behaviour, has taken a great affection for you, insomuch that he desires to receive you into his family: I cannot better provide for you than by disposing of you to him; and, if you have no objection, you shall return home with him when he goes from hence."

===Chinese===
"勋爵大人，"骑士说，"我向您坦白，最初打动我心的，是他与我一位故友极为相似——其举止风度亦与其容貌一般无二；他的才德值得他跻身更高的阶层；我愿收他为义子，将他作为我的亲属引荐于世，只要您肯将他让给我；您意下如何？"

"先生，"勋爵说，"您提出了一个高贵的提议，我作为这少年的朋友，不能阻碍他的前程。诚然我本有意在我的家族中为他谋一个位置；但我无法做得比将他托付给您更好——您的慷慨之情不受其他亲情羁绊所限，日后自会按照他的才德将他提升到更高的位置。我只有一个条件：须让这孩子自行选择；我不愿违其本意而强迫他离开我的身边。"

"您说得好，"菲利普爵士答道；"我也不会在其他条件下接纳他。"

"那就这么定了，"勋爵说，"让我们唤埃德蒙来。"

一个仆人被派去叫他；他立刻就来了，勋爵对他说道——

"埃德蒙，你当永远感恩这位先生，他察觉你与他一位故友颇为相似，又欣赏你的品行，对你心生了深厚的情谊，因此希望将你收入他的家族：我将你托付于他，便是对你最好的安排；如果你没有异议，等他离去时，你便随他回家去吧。"
""")

print("Block 2 done")
