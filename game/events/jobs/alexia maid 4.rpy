init python:
    
    event('mary_event_4', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), depends=('more_with_mary',), group='alexia_maid', run_count=1, priority=pr_npc)
    event('hanging_with_the_maids', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), group='alexia_maid', priority=pr_npc)
    event('I_got_your_back', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), depends=('alexia_and_mary',), group='alexia_maid', run_count=1, priority=pr_npc)
    event('girl_of_ill_repute', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), depends=('more_with_mary',), group='alexia_maid', run_count=1, priority=pr_npc)
    event('alexia_panty_sniffing', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'", "all_actors['alexia'].corruption > 30",), group='alexia_maid', run_count=1, priority=pr_npc)
    event('alexias_break', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'", 'alexiaLiurialFriendly', "all_actors['alexia'].corruption < 61",), group='alexia_maid', run_count=1, priority=pr_npc)

#Mary Event 4

$ maryNakedSeen = True

label mary_event_4:
scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve

"Alexia plodded down the hallway towards the servant’s quarter wiping the sleep from her eyes. Today’s shift was set for quite early in the morning. She was replacing a maid too sick to work. The fact that there were sick days for the servants seemed quite odd."
"Would Jezera really allow that?"
"She was considering that fact all the way until she opened the door to the changing room." 
"When she opened the door she discovered she was not alone."

#Mary’s “Interesting” Body
scene cg399 with fade
pause 3

"Mary was standing near the clothing pile, rifling for a uniform. Her lithe form was entirely naked. Alexia blinked twice in confusion."
"It was not that she had not seen a naked woman before. Or that there was something unusual about seeing a naked female body in the changing room. It was the specific naked female body she was staring at."
"Her body had clearly been heavily modified. Gleaming golden ring piercings hung from each nipple. But, that was just the start of it. There were a string of piercings at her navel as well. But, more shocking still was what was between her legs."
"A single small gold ring was clearly attached to her clit. But, other rings seemed to line each side of Mary’s lower walls. It was like her pussy had been built to be laced up."
"But, there were also all that tattoos. The word “Slave” written right above her privates. The pair of purple handprints etched around her breasts. And the image of two women engaging in...relations...tattooed in intimate detail on her side."
"Alexia just stood in place, shocked. Who would let their body be marked with such filthy...degrading...things. It made her look like such a slut…"
"Alexia brushed a hand over her own right side."

scene bg14 with fade
show alexia 2 necklace shocked at midleft with dissolve
#show mary naked

"Mary didn’t appear to have noticed Alexia’s presence. She was too busy focusing on one of the skimpy maid outfits she liked to wear. When she’d found the one she wanted, she turned her back towards Alexia."
"Alexia still just stood in place as Mary bent over to work the dress up her hips. Of course, there was a pattern on the small of her back. Though, Alexia proved unable to focus on making it out, when her eyes were glued to Mary’s pert backside. Alexia shifted her posture."
"The entire thing was uncomfortable. It was like she’d seen something private. Trying not to make a sound, she hurried out the door. She could change when Mary was done."

scene bg18 with fade
show alexia maid shock at midleft with dissolve
show mary neutral at midright with dissolve

mary "You’re looking at me funny. Is something wrong?"

"Alexia shook her head, perhaps a little too fast."

show alexia maid neutral at midleft with dissolve

al "No, I’m not. You’ve got such an imagination, Mary."

show mary happy at midright with dissolve

"Mary rolled her eyes and giggled. Then she went back to cleaning, though the persistent smirk on her face made Alexia think that Mary didn’t believe her. Alexia ran a hand down her side."
"Had Jezera been the one to do that to her? Had Mary wanted her body marked up that way? If it had been against her will, it sure didn’t seem like she was too unhappy about it." 
"Were the other maids marked up like that too?"

if all_actors['alexia'].corruption < 31:
    "Alexia decided she didn’t want to know. She didn’t want to think about it. There was work to do anyway. Alexia went back to cleaning, and tried her best not to stare at Mary. She was able to stop herself. Mostly."
    
else:
    "Alexia squirmed slightly. As degrading as the thought was, perhaps there was something to the idea of being marked...the permanence of it…"
    "If she kept working as a maid, did that mean that…?"
    "Alexia decided it would be best not to think about it too much. She had work to do. Though, her productivity throughout the day was somewhat limited. Working with Mary was...distracting."

return

######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################

#Hanging with the Maids Event (Repeatable)
label hanging_with_the_maids:
scene bg14 with fade
show alexia maid neutral at midleft with dissolve

"Today, Alexia was working from the kitchens, bringing meals over to some of the higher ups who could not be bothered going down to main hall and getting food for themselves. Naturally, Skorded, Jezera, Cliohna, and Andras were all on her delivery list."

if all_actors['alexia'].flags['andras_influence'] > 5 and all_actors['alexia'].flags['andras_influence'] > all_actors['alexia'].flags['jezera_influence']:
    show alexia maid aroused at midleft with dissolve
    "Naturally, Andras took the opportunity to make her feed him. It was hard to explain to the kitchen staff why it took her so long."
    show alexia maid neutral at midleft with dissolve

elif all_actors['alexia'].flags['jezera_influence'] > 5:
    show alexia maid aroused at midleft with dissolve
    "Jezera had, of course, chosen today to lounge about in strategic nudity. She took the opportunity of Alexia’s presence to have her do a few menial chores. By the time that Alexia returned to the kitchen, her cheeks were tomato red."
    show alexia maid neutral at midleft with dissolve

else:
    pass
    
scene alexia_maid_1 with fade

"However, for the most part the day was mostly monotonous. One did not expect to change the world when assigned to housework, but this was especially mindless work. Eventually settled in with a few other maids to engage in some gossip."
"She was pretty disconnected from the social circles of the servant’s quarter. Unlike them she stayed in the suites and could interact with anyone at any time. But, there was something sweet about their conversations about who was friends with who, and who was sleeping with who."
"It almost reminded her of gossip with the girls back at Arthdale. That reminder made her sad for a second when she remembered them. Almost like Arthdale. But, not Arthdale."
"Alexia came away from it with a greater sense of camaraderie with the serving staff. Bloodmeen was a living thing, and these people and their everyday lives and struggles were the blood flowing in its veins."

return

######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################

#I Got Your Back
label I_got_your_back:
scene bg14 with fade
show alexia maid neutral at midleft with dissolve
show mary neutral at midright with dissolve

"Alexia moved her duster back and forth over the antique vase. It certainly needed it. This segment of the castle hadn’t been occupied since the last war, and it was very much not fit for human habitation."

al "Oh no!"

"While not paying attention, she’d accidentally used a bit too much force. The vase fell over off its pedestal and crashed on the ground."
"Alexia jumped to her hands and knees, trying to grab up all the pieces. Fuck. What was she going to do if anyone found out? Just how valuable was this thing?"

mary "As much fun as you are in that position, you should move out of the way for a second."

"Alexia turned to the side to find Mary, standing there with a broom. With her help, the mess was entirely swept up in seconds."

show mary happy at midright with dissolve

mary "Don’t worry about it. If anyone asks, I’ll just say that it was badly situated on the pedestal. Since no one can flog you, as the general’s wife, everyone will probably just let it go."

"Mary gave Alexia a reassuring wink." 
"It was good to have friends."

return

######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################

#The Girl of Ill Repute

label girl_of_ill_repute:
scene bg14 with fade
show alexia maid neutral at midleft with dissolve

maid "Did you hear about Mary and Agnes?"

"Alexia’s ears perked up. She was one table over from the two maids who were chatting, setting silverware."

omaid "Agnes this time?"

"The first maid chuckled softly."
"Why was she always the voyeur?"

maid "Yup. The little runt must have fucked her way through half of the serving staff by now."

omaid "So what happened?"

maid "Falisiona went to the storeroom, and found Agnes with a strap-on buried in Mary. They didn’t even stop either."

omaid "I bet they were hoping Falisiona would join in. Wouldn’t be Falis’ first go around."

"Was Mary really that sexually active with the other maids? She knew that Mary liked girls, and that she had a flirtatious manner to her. But, Alexia hadn’t expected it to be such a routine occurrence…"
"She briefly even considered going over to the neighboring table and asking for more details."

omaid "So wait, is that why the two of them weren’t in rotation today?"

maid "I can only imagine."
maid "If I’ve heard of it, that means the Mistress has heard about it. And you know that she enjoys little miss cunt-munchers antics."
maid "She probably brought them in for a private viewing."

"The other maid rolled her eyes, but didn’t show much surprise. This probably wasn’t the first time Jezera had called up some of the maids this week."

omaid "So wait? Have you ever…?"

maid "Slept with Mary?"

omaid "Yeah, that."

maid "No way. They told me I didn’t have to fuck anyone when I took this job. I’m cleaning houses, not here to whore around."

"The other maid giggled."

omaid "That must be why the taskmistress assigned you the bad cot."

"The topic turned further away from Mary, and with it so did Alexia. She was mostly thinking about her friend." 
"Of course, it all made sense. It wasn’t like Alexia didn’t know that Mary was a bit of a bitch-in-heat. But, she didn’t know that Mary had that kind of reputation. And there was also the bit about Jezera keeping up with her antics…"

if maryKissLiked == False:
    #show alexia maid concerned at midleft with dissolve
    "The thought brought a pit to Alexia’s stomach. Even if her friend might enjoy it, being the subject of Jazera’s attentions couldn’t be good for Mary. Perhaps Jazera might even be responsible for her current...reputation..."
    return
    
else:
    show alexia maid aroused at midleft with dissolve
    "Did that mean though, that before...when Mary kissed her...that it was because…"
    "Alexia shook her head quietly."
    "Still, the idea of what was no doubt happening to Mary at that exact moment lingered. Being forced to fuck another person as a show for another person..."
    "Having your body, your sexuality, everything private used as a way of entertaining someone else... "
    "Captured by her eyes…"
    "Alexia shook her head again. She had work to do."
    $ change_corruption_actor('alexia', 3)
    return

######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################

label alexia_panty_sniffing:

scene alexia_maid_1:

"The weeks and weeks of work around the castle had taken its toll on Alexia. Endless minutiae mixed with degrading debauchery had left her prone to frequently getting lost in fantasies. The type of fantasy that one might call...improper."
"It was to her great consternation then, that she felt the rough, groping fingers of a hand caress her ass, just as she was bending over to retrieve her dropped feather duster in the castle hall."

scene bg14 with fade
show alexia maid shock at midleft with dissolve
show jezera happy at midright with dissolve

al "{i}Eeep!{/i}"

je "Mmm, my but aren’t you a squirmy one today?"

if midCorHappened == False or midCorFlee == True and alexiaJezObedient == False:
    #alexia maid angry
    show alexia maid neutral at midleft with dissolve
    "Alexia jumped in place and shot Jezera an annoyed look. Such events were a daily occurance working under Jezera. Still, she never seemed to get used to it."
    if midCorHappened == True and midCorFlee == True:
        al "How many times must I tell you not to do that?"
        je "Yes yes. You are not interested. I have heard it all before. But, the odd spot of fun won’t kill you. Besides, I caught you daydreaming."
    else:
        al "Lady Jezera! Must you do this so often?"
        je "‘Must’ is such a strong word. It’s more a question of {i}can{/i}, really."
        je "Besides, I caught you daydreaming. so you can’t claim to be the blushing maiden here, can you?"
        je "Don’t think you can hide it from me."
    al "..."
    al "Was there a reason that you wished to speak to me today, My Lady?"
    "Jezera chuckled to herself, toying softly with her nails."
    je "In fact, there is a reason. I have a task for you, my little dove."

else:
    al "M-mis- "
    #alexia maid angry
    show alexia maid neutral at midleft with dissolve
    al "Jezera!"
    "Despite her feigned anger, Alexia felt an erotic thrill run up her spine at the half-demon’s touch. She had been so titillated by the unexpected ass grope that she had nearly slipped and used a name that she mostly reserved for...private time. "
    je "Hello my little maid. I was just admiring the view."
    if all_actors['alexia'].corruption < 61:
        al "..."
        "Where once she might have snapped in anger at the unsolicited touch of the Demoness, now she found herself lapsing into silence."
    else:
        show alexia maid aroused at midleft with dissolve
        "Alexia licked her lips at Jezera’s horny gaze, her hands unconsciously drifting up and down her body as she put herself on display for the randy Demoness."
    "Jezera laughed at the look on Alexia’s face. She sashayed over to her, brazenly taking her by the hip as she held her close."
    show jezera neutral at midright with dissolve
    je "Sadly, I didn’t come here for fun, or even your juicy posterior. I’ve got a task for you; it’s very simple, all things considered."
    
#alexia maid concerned
show alexia maid neutral at midleft with dissolve

al "What do you want me to do?"

je "You see, in light of your husband’s recent successes, a few Dark Elf nobles have seen fit to come on bended knee to ask for my help."
je "I’m a bit picky with whom I ask to help keep such ‘honored’ guests’ rooms tidy, but…"

"Jezera allowed the implication to hang in the air. Alexia bowed her head."

al "It will be done, my Lady."

if alexiaJezObedient:
    "Jezera brushed a hand along Alexia’s breast through the thin fabric of her maid outfit, sending shivers down her spine."

je "Of course it will. You always know what to say, don’t you Alexia?"

scene bg7 with fade
show alexia maid neutral at midleft with dissolve

"Alexia went about her normal duties of cleaning with a kind of resigned indifference. If she was being totally honest with herself, the mundanities of traditional maid work only made it easier for her mind to drift elsewhere. A touch of a hand. A squeeze. Something more..."

show alexia maid aroused at midleft with dissolve

"As she changed the bedsheets, Alexia found focusing on the task harder and harder. The naughty thoughts were intruding on her work to the extent that she found herself blushing." 
"The Dark Elf may have been a noble, but she was either exceedingly lazy or a slob. A fact confirmed by the presence of used clothing discarded everywhere. Sighing to herself, Alexia set about her task of collecting the laundry to be washed and-"

show alexia maid shock at midleft with dissolve

al "…!"

"Alexia stopped. In her hands was a thin, black pair of panties. The clothing was frilled and silken, of a high quality reserved only for the crafty Elven nobility."
"Alexia hooked her thumbs through the corners of the underwear, stretching it taut to simulate a pair of thighs moving through them. Her eyes were affixed to the center of the crotch, where a slight wet patch could be seen."
"A lewd thought entered her head. A simple curiosity, really:"
"What did they smell like?"
"Glancing around to make sure no one was around, Alexia lifted the panties up to her face. Spreading the interior wide, she planted her nose against the fabric at the very core of the crotch." 
"She took in a stiff inhale, her lungs filling with the thick, feminine scent of an Elven cunt. It lingered in her senses so close that she could almost taste it."

show alexia maid aroused at midleft with dissolve

"Mmm…"

if maryNakedSeen == False:
    "Snapping back to her senses, the momentarily pussy-drunk maid stuffed the panties into her pile of laundry and resumed her cleaning duties. What had come over her?"
    
else:
    show mary happy behind bg7
    mary "Knock knock."
    hide mary
    show mary happy at midright with moveinright
    "Alexia nearly jumped out of her skin, she turned in horror to see her friend leaning casually against the crook of the door, smirking. Her smile widened as their eyes met."
    "Alexia froze, her hands still clutching the used panties. Mary slid into the room with all the grace of a cat."
    "She approached Alexia, her hands reaching out to take the panties from her. Alexia let her, her cheeks burning with shame as she struggled to find some excuse that could save her in this humiliating moment."
    "Mary inspected the panties, turning them around and back, making a great show of examining the lacework and the intricate details sewn into the fabric."
    mary "What do we have here? You know you could get in trouble for sniffing a visiting dignitaries undergarments, don’t you?"
    al "I can expl-"
    "Before Alexia could finish, Mary lifted the panties to her own face and took in a deep, shuddering inhale."
    mary "Aaah!"
    "With a wink and a smile Mary dropped the panties into the pile of laundry that Alexia had already collected and moved to help her clean the rest of the room. Alexia giggled at her friend and moved to help."
    
scene bg7 with fade
show alexia maid neutral at midleft with dissolve

"Alexia was just finishing the last touches on the room when the Dark Elf matron herself returned. The door opened and a regal, statuesque beauty swept into the room."

show alexia maid shock at midleft with dissolve

al "Oh! I beg your pardon!"

darke "You may take your leave, servant. I need to be alone for a time."

show alexia maid neutral at midleft with dissolve

al "Of course, my Lady."

darke "..."
darke "Goodness, this room is spotless! I wish my servants were half as thorough as you are."

show alexia maid happy at midleft with dissolve

al "I take this job very seriously, my Lady."

"She gave the Elf a bright smile."

return

######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################

label alexias_break:

scene alexia_maid_1 with fade

"Alexia was on cleaning duty alone today. A fairly normal task, albeit not an especially exciting one. It mostly meant going to the unused rooms and cleaning them out. Why any given room went from occupied to not was a roulette."
"Sometimes they left to seek out a better room. The castle was quite large, with hundreds of rooms that sat unused due to inability to maintain so much. Other times, it was for less innocent reasons. Especially when the room belonged to an orc."
"She’d actually spent the better part of the last hour hauling a bad mattress away. Her muscles just weren’t built for that."

scene bg7 with fade
show alexia maid neutral at midleft with dissolve

"She rubbed her shoulders as she walked into a recently vacated room. Only to discover that she wasn’t quite as alone as she might have believed."

#liurial shocked
show liurial neutral at midright with dissolve

liur "Eeeek!"

show alexia maid shock at midleft with dissolve

al "W-wait!"

"Alexia froze up, only to loosen up again when she discovered who it was It was just Liurial."

show alexia maid happy at midleft with dissolve

al "Don’t scare me like that, you. What are you even doing out here? This isn’t your room, is it?"

"Liurial took a second to catch her breath."

#liur neutral

liur "M-mistress Alexia. When someone walked in, I had assumed the worst. Thank the sky and the dirt that it’s just you."
liur "I only know this room has no present occupant. That’s why I picked it. There was little in the way of new work to do, so I wished for a quiet place to seclude myself. "
liur "I’m sorry to have surprised you in this way."

al "No no, it’s quite alright."

"She clutched at the amulet that hung dark on her neck."

al "He. I quite understand the feeling of being rather vulnerable in this place. I’m sorry to have disturbed your sense of security that way. If you’d like I could go?"

"Liurial shook her head emphatically."

liur "No! You’re not violating anything Mistress Alexia. I’m worried about those of ill intent. You’re my protector’s wife. I could never refuse your presence."

"Alexia smiled to herself. The fact that her husband was still...with...this woman was a hard thought to push out of her head. But, what would be the point of putting up her guard?"
"If there was one thing that was true about Liurial, she was not a threat."

al "I’m glad you feel that way. If there is anything you ever need, you can always come to me."

show liurial happy at midright with dissolve

liur "I know, Mistress. Thank you."

show liurial neutral at midright with dissolve
show alexia maid neutral at midleft with dissolve

"Liurial returned to her tea, and Alexia got to work bringing the room into more of a presentable state. Removing any trash or remaining belongings. Dusting the floors and counters."
"But, the more she worked, the harder she found it to continue. She’d pause for a few seconds here and there to collect herself. The exhaustion was getting to her. She needed a break. She needed-"
"Alexia paused."

al "Liurial, you consider me to be your Mistress, right? You belong to my husband, after all."

"She gave the waifish blonde a small wink."

al "And we both know from first hand experience that what’s his is mine. He does not mind sharing with me."

show liurial aroused at midright with dissolve

"A blush came to her face. The memory Alexia was hinting towards was not a difficult one to tease out. "

liur "That is all true…"

"Alexia stood tall and walked towards her. She didn’t normally tower over most people, but she could easily overpower Liurial if she so desired."

al "Wouldn’t you call it...rather rude for your Mistress to be doing all the work while her possession lounges around luxury. "

"Liurial nodded slowly. There was a light behind her eyes. A spark of interest."

liur "Of course. It’s my duty to serve you. If it is within my power, it is my responsibility. What would you have me do?"

"Alexia’s smile grew wider."

al "I know just the thing. I bet they have one in your size. Wait right here."

#cg1
scene cg538 with fade
show alexia maid happy behind cg538
show liurial aroused behind cg538

"Half an hour later, it was Alexia sitting at the table sipping slowly from a hot cup of tea. This was her break hour and she was going to make the most of it. Her feather duster remained in hand, but Alexia only idly toyed with it by brushing the table."

al "Under the desk as well."

"Liurial rushed to respond. Liurial fluttered over with a duster in hand. The minuscule skirt that Alexia had picked out for her flared easily. She looked good in a maid outfit. It suited her. If anything, it was a shame that she was mostly tasked with clerical work."

if meetMary == True:
    "The fact that it was one of the skimpier outfits that Mary tended to wear only added to the aesthetic appeal of the situation."
    
"Liurial bent low to clean the floor, inadvertently giving her Mistress a show."

al "Lacey. Very cute. "

"Alexia brushed a hand along Liurial’s rump. The girl shivered at the touch. But, before it could get too far, Alexia drew her hand back."
"That was the game of it. Tease and pull back. Tease and pull back. Cop a feel of Liurial’s exposed breasts then draw her hand back."

if NTR and all_actors['alexia'].corruption > 30:
    "By now, Alexia knew the basics of the art of teasing a girl. She’d learned from experience."
    
"Liurial was naturally the perfect subject for this. Every time Alexia brushed her hand against her, she’d let out a little whimper. She’d lean into touches, like a pet craving affection."

if liurial_orgasm_control_on == True:
    "If Alexia didn’t know any better, she’d suspect that Liurial hadn’t released any sexual tension in weeks. Where was this desperation coming from?"
    
"Liurial subtly waved her rear at Alexia as she cleaned. Pleading with her body. Alexia could smell the need in the air."
"But, she wasn’t going to indulge yet. After all, would she really be doing her duty if she didn’t make sure the maid finished her work? Not that Liurial seemed to be making much headway at all."

al "This floor is still filthy. Look at all that dust! It’s a wonder to believe you’ve really been cleaning this entire time."

liur "I’m sorry, Mistress..."

al "Have you been too busy fantasizing about naughty things to clean?"

liur "..."

"Liurial nodded her head slowly. She looked up to the other woman."

al "And are you here to have dirty thoughts, or are you here to clean?"
al "O-only bad little maids are thinking dirty thoughts when they should be thinking clean thoughts."

"Alexia had to suppress a giggle. The character she was playing was not exactly subtle. Besides, she hadn’t exactly forgotten what she was wearing herself."

liur "Indeed, Mistress. I’m a bad little maid. My mind keeps on going to such filthy filthy places. No place for a maid like me."
liur "Do you wish to punish me, Mistress?"

"She wiggled her rear again." 
"Alexia’s mouth grew dry. She wanted to lean down and feast on the girl here and now. The more she teased Liurial, the more turned on she got. How did Jezera maintain so much self control when going about her perversions?"

al "W-well the only solution to you being a bad little maid is for you to instead be a good little maid. That means you need to do some cleaning."

"Liurial went up to her knees. By now, her face had turned totally red."

liur "What would you have me clean? Surely there is something I could do to show you my obedience?"

"Alexia bit her lip. She’d planned to continue the game of role reversal a little longer. But, how could she resist such a cute face? How could she resist the scent of feminine arousal in the air?"
"Alexia lifted her own maid skirt and brushed her panties to the side."

al "Why don’t you clean this?"

"Liurial giggled softly. Then she leaned in to lick her Mistresses’ slick pussy."

#cg2
show maidcunnianimation1 with fade

al "Ah…"

"Liurial might not have been good at cleaning some things. But this she could do. The movement of Liurial’s tongue proved skillful. Every time it brushed over Alexia’s clit, she let loose a loud groan."
"Alexia gripped the back of Liurial’s head tightly. The silly bonnet Alexia had given her was lost in the chaos."
"The intensity of Alexia’s movements grew and grew. At first, she squirmed and twitched. Soon her back was arched, and her chest rose and fell in deep lustful breaths. Alexia’s eyes fell closed." 
"Liurial just continued her work. She dutifully worked on the task of bringing Alexia pleasure."

al "Filthy filthy little maid."

"She pulled Liurial’s head away for a moment and found the elf’s face covered in juices and a mischievous grin. Some of her hair had fallen in front of her eyes and gotten matted. "

al "What are you grinning at?"

liur "Nothing, Mistress."

"Alexia rolled her eyes."

al "Then get back in there."

liur "Of cou-"

"Before she could even finish her reply, Alexia had gagged her once more with her sex. At once, the lapping of Liurial’s tongue started again. With it, the pleasure."

al "Ahhh. Fuckkkk."

"She bucked her hips, grinding and moving against Liurial’s face. Juices poured down her chin, dripping into the empty spot of the dress afforded for cleavage. Liurial’s borrowed outfit grew damp with hot, sticky liquid."

al "More. More. Keep on going. Keep on going you little Ah."

"Liurial’s tongue sped up. It went from polishing to scrubbing. The effect on Alexia was instantaneous. She went from squirming and groaning to thrashing and moaning. For Alexia, it was the building of pressure. A bubble about to burst."

al "Almost there. Almost there…."

"Her voice turned to a rasp. Her body grew stiff…"

show cg542 with sshake
show cg542 with sshake
show cg543 with flash
pause 3

"...Then it hit."
"Alexia’s fingers dug into Liurial’s hair, forcing her face close. That last extra bit of stimulation as she came, to eek out every last bit of pleasure from Liurial’s tongue."

"Alexia let Liurial fall backward. The elf panted loudly, sucking in every bit of air she could get. She’d been reduced to a filthy pussy stained mess."

if liurial_orgasm_control_on == True:
    "Liurial’s fingers drifted between her legs for a moment. To Alexia, it seemed like she was about to touch herself. A natural response to what had just happened. But, after the first brush, Liurial forced her fingers back up. Like she was forcing herself not to indulge."
    "Alexia would have said something, but she was too busy panting."
else:
    "A hand drifted between Liurial’s legs. Even as Alexia was recovering from her orgasm, Liurial was working towards hers. Good. She deserved it. Her tongue had put in work."

"Alexia closed her eyes. This had been a good break."

scene bg7 with fade
show alexia maid aroused at midleft with dissolve
show liurial naked aroused at midright with dissolve

al "..."
liur "..."

"Liurial stretched her jaw. She’d been doing so off and on for the past few minutes. The remnants of Alexia’s secretions still covered her face."

al "So, both of the uniforms are too much of a mess to return as is..."

"She turned to the table."

al "The floor and the chair are both so stained from cum that they’re actually more filthy than when I first arrived…"

"Then she turned back to the rest of the room."

al "...And you were too distracted by the roleplay to do much actual cleaning at all."

"Alexia ran a hand through her hair. Not only would she still have to clean, despite having already wasted so much time on her break. But, she’d actually need to do more cleaning then she’d have had to do had she never tried to get Liurial to do her work."

al "This place is a nightmare. What exactly are we going to do about this?"

show liurial neutral at midright with dissolve

"She turned to the side, only to find her plaything shimmying back into her normal green dress."

liur "How should I know, Mistress? I’m not a maid."

"Alexia gave her a swat on the ass."

return
