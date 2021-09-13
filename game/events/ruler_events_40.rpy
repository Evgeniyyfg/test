init python:
    
    event('a_caged_mess', triggers="week_end", conditions=('rowan_draith_sex',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('goblin_twin_double', triggers="week_end", conditions=('society_type == "feudalism"',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('demon_bastards', triggers="week_end", conditions=('xzaratlFinaleSeen == False',), depends=('xzaratl_s_advances',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('xzaratl_virility', triggers="week_end", conditions=('abandondedPregnancyAspirations == False',), depends=('demon_bastards', 'alexia_potion_stealing',), group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg23")
    event('dead_orc_lord', triggers="week_end", conditions=('week > 12',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('embezzlement_for_justice', triggers="week_end", conditions=('avatar.corruption < 61','week > 28',), group='ruler_event', run_count=1, priority=pr_ruler)

   
label a_caged_mess:

scene bg25 with fade
show rowan necklace neutral at midleft with moveinleft


"The breeding pits never smelled any better no matter how many times Rowan ventured down into the castle's depths. It was a musty stench; the sour tang invaded his nostrils as Rowan searched through the pits for the small beastmaster."
"He would have to make sure the staff down here was adequate when it came to cleaning the cages. He knew the breeding pits were overwhelmed as it was, and it appeared the cages were suffering for it."
"Knowing Draith, he probably wasn't happy about the state of cleanliness either. He cared for these creatures more than anyone Rowan knew. Seeing them in any state of disarray would no doubt trouble the beastmaster."
"Rowan made a mental note to himself of the state of the pits as he turned the corner, the dark elf coming into view."
"Draith was in the midst of training one of the many beasts, his whip gripped securely in his palm as he circled one of the Driders. It was a new one, smaller than the others Rowan usually brought in. He recognized the runt of the litter, its eyes roving around the cage with fresh panic."
"Rowan was not usually here to witness Draith's training methods, but as he watched the dark elf instruct the Drider, a sense of admiration swelled in his chest. "
"Draith was not cruel to the creature, no matter how new and disobedient it was-- and that was often. Rowan winced as the Drider hissed and made a step to attack the beastmaster, but before Rowan could reach his sword, Draith lashed his whip out in warning."
"It barely caught against the Drider's leg, but it was enough to force it into submission."

ro "Impressive."

#show draith shocked at midright with dissolve
show draith neutral at midright with dissolve

"Draith started at the sound of Rowan's voice. When he glanced back with a smile, the Drider took its opportunity to leap toward him."

dra "Hello, sir--"

"Before Rowan could get a warning past his lips, Draith lashed his whip again, drawing the Drider back. He {i}tsk'd{/i} at the creature with pity."

#show draith neutral at midright with dissolve

dra "You're a stubborn one, aren't you?"

"With a sigh, Draith hooked the whip against his hip and ducked out of the cage. The Drider hissed at him, but once the lock was in place, Rowan felt he could relax."

ro "Are they all like that when you first start?"

show draith happy at midright with dissolve

"Draith gave him a wry smile."

dra "Sometimes. This one is tougher than most… But she has a lot of scars. Whoever caused those caused more damage than physical."

show draith neutral at midright with dissolve

dra "I hate to see them in pain like that…"

"The elf sighed, disheartened. Rowan could see the hurt it caused him to see even a gruesome beast like a Drider suffering."

show draith happy at midright with dissolve

"Just as quickly though, Draith perked up."

dra "Ah, but was there something you came here for, sir?"

"Rowan could see the eagerness on the man's face, and the memory of his last time here in the pits flashed through his mind. Based on the tinge of purple on Draith's face, Rowan assumed the elf was thinking the same thing."
"Alas, that is not why he came here."

ro "Yes, actually. I came to see how much food you need down here for the month. I didn't receive your usual report."

show draith neutral at midright with dissolve

"Recognition and shame colored Draith's face. He grimaced, running a hand through his hair."

dra "Right. The report."
dra "I'm so sorry, sir. I've been so busy, I didn't get a chance…"

"Draith glanced around the cages, and Rowan could tell he was mentally calculating the time it would take to continue training the creatures, clean up the pits, {i}and{/i} come up with everything they needed down here, plus the time it would take to deliver that report back to Rowan's office."
"It was a lot of work for one person to do by themselves."

dra "I'll have it ready by tonight. I'm sorry for the delay."

ro "It's fine. I just need it by tomorrow night, so whenever you get a chance."

"The dark elf smiled shyly up at him and nodded, comforted by his words. Rowan took the moment to admire the plumpness of the man's lips, remembering just how sweet his tongue had tasted against his. How smooth his body felt under his hands…"

dra "Is there anything else I can do for you, sir?"

menu:
    "Have sex.":
        $ released_fix_rollback()
        $ change_base_stat('g', 1)
        $ change_base_stat('c', 3)
        $ change_relation('draith', 3)
        jump cagedMessSex
        
    "Return to work":
       $ released_fix_rollback() 
       $ change_base_stat('g', -1)
       $ change_relation('draith', -3)
       "Briefly, Rowan considered the heated moment of passion he and the dark elf shared last time he wandered down into the pits, but just as quickly pushed the thought away."
       "He wasn't sure what came over him last time. Something about the elf was… pleasurable, both to look at and to have."
       "But if Draith didn't have the time to clean up the pits, he certainly didn't have a free moment for sex."
       ro "...Yes, I would like you to clean up these cages. They reek."
       "Draith frowned, looking back at the empty, unused cages. Disappointment was evident on the young man's face."
       dra "...Oh. Yes, sir."
       "Rowan waved goodbye to the attractive dark elf, glancing once at the pleasant sight of his ass before returning to his office."
       return

label cagedMessSex:

"Well since he was here, Rowan may as well make use of the extra time. He smirked, his eyes roving over the delicious curves of the supple man's pale skin."

ro "I can think of a few things, actually."

"Rowan rested his palms against Draith's slender waist and pulled him flush against his chest. The elf's eyes widened, the blush taking a stronger hold over his face."

ro "When are you going to clean up these cages?"

dra "U-Uh, sometime tonight…"

"Good. Then you won't mind if we use one now."

#cg1
scene black with fade
show rowan necklace happy behind black
#show draith aroused behind black
show draith happy behind black

"Draith shook his head, an eager glint in his eyes. Rowan pressed his lips hard against his, sucking on the soft curve of the elf's bottom lip. Draith moaned, his trembling hands clutching tightly onto Rowan's shirt."
"Memories of their last endeavour poured through Rowan's mind, heat building up in his hardening cock. Draith was so small, so soft, compared to the other men he'd come across." 
"It made him want to tear the elf in two."
"Rowan's hands roamed down, over the curve of his back and planted his palms firmly on Draith's buttocks, giving the soft flesh a squeeze. The elf bit back a whimper, arching toward him."
"One touch and the beastmaster was ready to give it all away."

ro "Go get the oil."

"Draith nodded at once, scurrying off. When he returned, Rowan led him into one of the emptied cages, ignoring the glances of passing orcs as he shoved the elf onto his hands and knees." 
"Draith got into an easy position, his pert ass raised high in the air as he arched downward. Once his cock was free, Draith rested his head in his arms, moaning softly under his breath as Rowan's hands roamed across his ass and thighs."
"Rowan pressed kisses across Draith's back, earning a shudder from the elf when his teeth grazed his hip bone." 
"How could a man be this delightful to touch? Rowan pulled himself out from his own trousers and spread the oil across his erection. Draith glanced back, biting down on his lip when he took in the sight of Rowan's large shaft." 
"Once the oil was thoroughly applied, Rowan leaned forward and humped Draith's buttox, his cock stiff and ready for insertion."
"Draith was not quite ready, however. Rowan delighted in the tightness of the elf's asshole as he ground against it, each movement widening it further."

dra "G-Go slow… Careful, please, sir…"

"Draith panted out the words, his fingers curling against the hard stone floor. Rowan eased Draith's tight hole with a few fingers, pumping in and out until he felt the man was ready for his cock."
"Rowan pushed himself inside slowly, earning a pleased cry from the elf. Rowan further surged inside of him, his cock pressing deeper. Deeper. Deeper."

dra "O-Ooohh…"

"Draith bit down on his arm as he whimpered. Rowan's fingers dug into the slender man's hips as he pushed in and out at a steady rhythm." 
"Draith's reached down to stroke his own cock, occasionally reaching back to touch his own ass or the base of Rowan's shaft. The sight excited Rowan, and he rocked against the elf harder."
"Draith begged and pleaded through his little pants and whimpers, his little cock twitching every time Rowan followed through. Rowan pressed close to bite down along the elf's shoulders and back, enjoying the bloom of purple on his skin wherever the bites left a mark."

"He bit further, up his shoulders, along his neck. Draith leaned his head to the side, giving Rowan better access to his skin." 
"The elf gasped as Rowan pounded inside his taught hole, a stream of white cum pouring out over the stone floor. Rowan continued to hammer away at the twinkish elf's ass."

dra "Puh-Please, sir… Fill me up…!"

"Draith wiggled his ass against him, rubbing against Rowan's balls. Rowan grunted in pleasure, his hips jerking hard against the elf's soft rear."
"He tried to hold it in-- he wanted to keep going, to make Draith cum a second time-- but the sight of Draith panting and whining naked underneath him was too much. Hot cum released from his sac, pouring out into Draith's waiting hole."
"Rowan humped the elf a little further until he was empty. Once finished, he held the slender man against his chest from behind. Draith did not seem to mind-- in fact, he seemed to enjoy the intimate act."

scene bg25 with fade
#show draith aroused behind bg25
show draith happy behind bg25

"After a few moments of silence, Rowan finally stood up and cleaned himself up. Draith remained on the floor, a relaxed smile on his face."

show rowan necklace happy at midleft with dissolve

"Rowan began to leave the cage but stopped, looking back down at the mess they made."

ro "Make sure this is cleaned up the next time I'm here."

"Draith beamed, fully aware of what Rowan's next visit would entail. Rowan saw the elf's cock twitch in anticipation."

dra "Yes, sir!"

return

###############################################################################################################################
###############################################################################################################################
###############################################################################################################################

label goblin_twin_double:

scene bg6 with fade
show rowan necklace neutral at midright with dissolve

"There was a knock at the door."

ro "Enter."

"A maid entered the room, then gave a short curtsey. She was followed by four more, two carrying a trunk, the third a wooden stand, and the final one held a single tall stool."

maid "Mistress has sent us to prepare for the lady's fitting."

ro " In my office?"

maid "Yes, mistress insisted."

"Well it certainly was not unusual for Jezera to impose... frequently. The demoness bastard herself would insist that he stay here while this went on too, not that Rowan really wanted to move everything out to keep working anyway."

if week > 24:
    "Liurial would be gone for most of the day and he had a lot to do in her absence."
    
ro "Very well, get to it."

"They placed their burdens in the center of the room, then extracted a large noblewoman's dress from the trunk. It was a Rosarian style, the sort of attire typically worn by ladies to balls or weddings."
"They put the entire affair on the rack, lined up for a group bow, and took their leave. It had not even been two minutes since the first had entered."

ro "Guess the lady will be by later then."
ro "(I should keep working while I still can.)"

scene black with fade
pause 2

scene bg6 with fade
show rowan necklace neutral at midright with dissolve

"Perhaps an hour later Rowan became aware in the back of his mind that there were a lot of excited women chatting outside his office. It wasn't enough to draw his attention away from his work until the door suddenly opened and Jezera surrounded by three goblin women piled inside."

show jezera happy at midleft with moveinleft
show clamin happy at edgeleft with moveinleft

je "Wonderful, it would seem everything is in order for you. What do you think, my lady?"

"Rowan watched the goblins circle around the dress for a moment before speaking up. Cla-Min was unmistakable, the other two were her sisters Cla-Tre and Cla-Owi. He recognized the twins from the dinner."

ro "After the staff came by I wasn't expecting a business deal like this."

show jezera displeased at midleft with dissolve

je "Rowan! You insult us! This is no deal, it is a gift for our new noble lady Cla-Min."

show rowan necklace shock at midright with dissolve

"He could only stare on incredulously. A dress like that? Evidently he wasn't the only one."

clatre "This is what we have to work with?!"

claowi "Empress, I wouldn't call this a 'little' adjustment."

"However, the one who was receiving the gift had a very different reaction."

cla "Thank you so much your majesty, it's beautiful!"

show jezera happy at midleft with dissolve

"Jezera beamed then surveyed the room with a triumphant grin on her face."

je "I'm so happy to hear, you, like my gift. Please make use of this room for your tailoring needs until you have finished your adjustments. If you need any supplies or tools, do not hesitate to ask Rowan and he'll get what you need."

hide jezera with moveoutleft

"Without another word the half-demon slipped back out the door and closed it behind her."

clatre "This is going to take days! You know how much work we'll lose in that time?"

claowi "Sis, what is wrong with you?"

cla "Don't be like that girls."

hide clamin with dissolve

"Ignoring the other goblins, Cla-Min promptly stripped her clothes off then and there and clambered up onto the stool with an expectant look on her face."

show clamin happy behind bg6

cla "Let's get to work. The sooner you start, the sooner we finish."

"The twins exchanged a double take of the dress, Min on the stool, each other, and finally eyed up Rowan. A few whispers were exchanged before they saddled up to the man. Together they looked up at him, Owi doing her best doe eyes while Tre licked her lips seductively."

show rowan necklace neutral at midright with dissolve

ro "(Uh oh, what do you want with me?)"

clatre "We could really use your help here, big hero."

claowi "Yeah, sis is in one of her moods."

"The two kept their voices low, while they stood on either side of his chair."

clatre "There's no way two short girls like us can work on that dress alone."

claowi "You're a nice tall man who could. And we'd owe you a big favour if you help out."

"The two pressed in against him, while puffing their sizable chests out."

clatre "A big big double double favour!"

claowi "Oh! Yeah, yes. We do the best chestwork."

menu:
    "Take up their offer of a 'favour'":
        $ released_fix_rollback()
        jump goblinDressFitting
        
    "Help them find some stepladders.":
        $ released_fix_rollback()
        ro "I have a better idea."
        scene black with fade
        pause 1
        scene bg6 with fade
        show clamin happy behind bg6
        clatre "Fourteen."
        claowi "Okay, that's half the other side."
        clatre "Good."
        "Rowan mostly tuned them out as he kept working, only occasionally being distracted by the often naked woman receiving measurements and trying out various parts of her new dress in front of him."
        "Her younger sisters fussed about her dutifully on the stepladders that Rowan had found for them. They were slightly disappointed he hadn't decided to help them personally, but Rowan had a lot of work to do and this way he'd get it done even after his office takeover."
        cla "You'd think it wouldn't be so tight when you're half the dress size. Hey Rowan, does this push my breasts up too much?"
        "Get most of the work done anyway."
        return
        
label goblinDressFitting:

"Rowan put his papers down and stood up."

ro "Alright, what do you need me to do?"

"The two squealed slightly in excitement and wrapped their arms around his waist."

clatre "Thank you so much!"
claowi "Yes, thank you!"

cla "What are you two doing, hurry up already!"

claowi "Coming sis!"

"While one sister ran off, the other lingered just a second longer to give a smoldering smile and wink."

clatre "Don't worry big guy, you won't regret this."

"Rowan wasn't sure if he was already regretting this or not."

claowi "Now elbow height. Lift your arm Cla-Min."

clatre "And Rowan you lay that attachment, yes up there. Now put the tape next to it."

ro "Here?"

clatre "No, up a bit."

ro "Right."

"They'd been at it for awhile now.  Measuring and marking all sorts of different parts of the dress so it could be refitted for Cla-Min."
"The routine was first to put the dress on, adjusting the oversized thing to where it would properly fit, then use the measuring tape to figure out how much material needed to be removed. Finally put some pins in to mark things and move on to the next part. There was a lot to do."
"On the other hand, most of the time Cla-Min's chest was totally exposed right in front of his face."

cla "Steady there. Here, lean against me."

"Not only were none of the goblins troubled by the lack of personal space, they actively looked for opportunities to press against Rowan while he worked. By human standards all three sisters were very well endowed."

ro "(How big are goblins on average?)"

show rowan necklace shock at midright with dissolve

"There was a sudden sharp prick in his backside!"
 
ro "Ow!"

"Cla-Tre winked at him and held up one of her long needles, which he took."

clatre "Don't get too distracted, big guy, we do actually want to finish here."

claowi "Five centimeters in from the elbow."

show rowan necklace neutral at midright with dissolve

ro "Okay."

"He put the pin in and Cla-Owi checked the tape one more time."

claowi "Great. Next the cuff."

"Rowan sighed slightly and started messing around with the sleeve with Cla-Min to get the wrist onto her wrist. A pair of mounds that were growing rather familiar pressed right against his groin. Soft whispering came up from the site."

clatre "Hey, remember there's an extra special double double favor coming at the end. We'll get through this."

"She flicked her pink hair over her shoulder and pressed her breasts even harder against his trousers with an eager grin."

cla "Cla-Tre! Stop flirting with Rowan for one damn minute so we can sort out this sleeve!"

"Tre jerked back in surprise and looked over at her older sister impishly, then pointedly took a step away from Rowan. For all the world Cla-Min looked like a schoolteacher reprimanding a misbehaving student."

clatre "Sorry Cla-Min."

"
Just before returning to work, Rowan noticed that the third sister was barely suppressing laughter."

scene black with fade
pause 2
scene bg6 with fade
show rowan necklace neutral at midright with dissolve
show clamin happy at midleft with dissolve

"Ultimately things went fairly smoothly and Rowan hardly noticed the passage of time. He was a bit surprised when Cla-Owi announced that they'd finished."

cla "Thank you so much for your help Rowan. I can't wait until you get to see me in the finished dress."

ro "So you're not going to keep using my office for the tailoring?"

clatre "No, it'll be a lot easier if we take the dress back to our wagon."

claowi "There's a lot more there we'd have to bring in to do the work here."

"It was a few minutes after they'd taken the last measurement. Everything was back on the stand and Cla-Min had put her regular clothes back on."

cla "There won't be any problems, right girls?"

clatre "Mostly no."

cla "Mostly?"

claowi "Well the chest..."

show clamin annoyed at midleft with dissolve

"A dark look crossed the goblin's face."

cla "Yes, the one thing that's way too tight."

claowi "We can take material out no problem but adding it in... not so much."

cla "If only we could move some of that around. Ugh, well if I have to bear it I will."

clatre "Actually we could take the chest out."

ro "Wait, take it out? As in, no chest at all?"

clatre "Totally! Goblins go barechested all the time, it wouldn't be odd at all!"

"On queue, the twins popped their breasts out of their tops and hopped once together."

ro "I don't think that would go over well in most noble parties I've seen."

"Owi blushed a deep green as she fixed her blouse, but Tre remained upbeat and pleased with herself."

cla "Nor is it true. Tell me what you're actually thinking Tre."

"Tre stuck her tongue at her sister, however the matriarch was back and she was not in the mood to put up with nonsense. The troublemaker heaved an exaggerated sigh as she pulled her top back up, then apologized."

clatre "Sorry. I was thinking that we could take the chest out and replace it with material from somewhere else."

claowi "Uh, Tre, none of these cuts are going to be enough for that."

clatre "We're cutting from two sleeves, we can stitch those together without it looking terrible."

claowi "Hmm. Yeah, that might work."

show clamin happy at midleft with dissolve

"Cla-Min clapped her hands together."

cla "Excellent, then problem solved. I believe that's everything we needed here. Thank you very much for letting us use you and your office Rowan. We'll get everything cleaned out and discuss compensation for service and space."

claowi "You shouldn't trouble yourself Cla-Min."

clatre "Yeah, we'll take care of everything, you get back to the caravan. I think... "

"The twins exchanged a look."

claowi "Bow?"

clatre "Yeah, Bow said he wanted you back as soon as you were done."

claowi "We don't need you here anymore, so we'll take care of cleanup and repaying Rowan while you help Bow at the caravan."

"Cla-Min's expression didn't change an inch. Though her next sentence did come far more dragged out."

cla "Very well. I'll leave Rowan in your 'very' capable hands."

hide clamin with moveoutleft

"She nodded once to Rowan and left the room."
"No sooner had Cla-Min left the room and Cla-Tre was straight back to her seductress ways. She threw her arms around Rowan's waist and rubbed her face against him, urging a little excitement."

clatre "Thank you sooo much for your help, you big sneaky sexy man."

"Only a beat behind her sister, Cla-Owi wrapped her arms around Rowan's back and rested her head in the small of his back."

claowi "So good, so nice."

"Both of them pressed their breasts hard against Rowan's legs."

claowi "We promised you a big double double favor, now it's time to pay it! Ready, Owi?"

clatre "Ready, Tre."

scene black with fade
show rowan necklace naked behind black

"Rather than pulling their tops down, the two sisters lifted them up.  Slowly pulling the cloth up and over their heads to let their breasts drop with a satisfying bounce to them."
"Rowan smiled in approval and started working at his belt, only to be stopped by Owi."

claowi "Don't trouble yourself, let us take care of you."

ro "Hmm, well I think I can leave myself in your 'very' capable hands for now."

"Rowan sat back on the dress trunk to let the girls work. They busied themselves first with his shoes, taking them off fast and efficiently. Then giving both feet a firm rub. It was obvious they were good with their fingers."
"Next came the belt and peeling down his pants. It didn't take long, but even if it had Rowan had plenty of entertainment in the form of ogling the two topless women before him."  
"Tre took full advantage of the gawking and pressed herself against him with every opportunity. On the other hand Owi had developed quite the deep blush and squirmed a bit under his gaze. Rowan used a finger to lift her chin and meet his gaze so he could give her a reassuring smile."
"Her eyes darted in all directions, but kept coming back to his."

clatre "Looks like someone's enjoying this."

claowi "Tre, please don't tease me."

"The show was effective. By the time they had fully depantsed Rowan he was rock hard and ready for their attention. Both kneeled down on either side of him and pressed their breasts together with their arms to push them forwards."
"Then they leaned in and wrapped him up in their tit-flesh. It felt amazing having these two around him. Even better when they started rocking forwards and back. As they started to get into it Rowan leaned backwards and relaxed into their motions."

claowi "Hah, yes."

ro "Isn't that my line? Hnn..."

"Owi's blush deepened even more and she bit her lip to stifle further comment. On the other hand Tre was all smiles as she leered at Rowan."

clatre "Cla tits are the best, aren't they? Definitely worth the trouble we put you through, I bet."

ro "Your family certainly is blessed. You've got most human women beat when it comes to size."

"She winked at him and used a finger to draw circles about the glans sticking out of her green flesh."

clatre "Enjoy, you earned it."

claowi "Uh huh."

"Tre was knocked slightly off balance when her sister started pushing forwards harder, but quickly moved to match the movements. The sensations on Rowan's member were doubled and he groaned appreciatively."

ro "Well you two are doing a good job at making it enjoyable. How often do you give double double favors?"

"The two glanced at one another and Rowan realized what he'd just said."

ro "You know what, never-"

claowi "Just you, actually."

clatre " You're special. You're Rowan, the hero!"

claowi "The man who'll join the clan..."

"That again."

ro "I haven't heard of humans joining goblin clans before, are double favors part of the process?"

claowi "Yes!  Yes!  So many double double favors when you join our clan, right Tre?"

"This time it was Tre's turn to be caught off guard."

clatre "Of... course?"

"Rowan was about to say something else, but decided not to and just enjoy the sensation of bouncing and rolling around the bountiful breasts before him. It hadn't been a lie. They really were good at 'chestwork'."
"However, now he was approaching his peak."
"There was no relaxing anymore, no holding back. He put a hand on either shoulder of the twins and started bucking his hips against their movements. The change was obvious to them. Owi rocked harder as Tre planted a wet kiss on his member."

#cum var
scene black with fade
show rowan necklace naked aroused behind black

"A moment later a shudder ran through the sisters as he erupted over their combined tits. Tre pulled her head back but kept her breasts firmly against her sisters."  
"Owi didn't, and got some of Rowan's seed on her head. The rest covered their joined chests, with the shaft kept firmly between."

ro "Hah, amazing. I definitely enjoyed that. Your hands and chests make compelling arguments for giving favours."

claowi "Thank you so much! I practice a lot when I'm... uh..."

"Once more Owi looked away in embarrassment and busied herself with cleaning off her face."

clatre "Good to know. If we need any help with more big jobs, we know just who we can hire with our double double favour!"

ro "Depends on the job."

scene bg6 with fade
show rowan necklace happy at midright with dissolve

"Rowan started redressing himself while the sisters cleaned themselves off.  He stood up and glanced down at the chest he'd been sitting on.  It had taken two human maids to bring that in here."

ro "Do you need a hand with this? It might be a bit big for you two. No favour needed."

claowi "Oh don't trouble yourself, we can-"

clatre "No Owi, we aren't bringing that all the way to the wagon on our own."

claowi "But... but..."

"She stumbled at her words for a moment, but couldn't seem to come up with an actual objection."

scene bg19 with fade

"A few minutes later the three of them had hauled the chest with the dress in it to the goblin wagons. It was quite manageable between the three of them, but Rowan was surprised at how much trouble Owi seemed to be having."
"When they got to the wagon and put the chest in, he saw his answer. While pushing their burden further in, Rowan got a good view of both sister's backsides. Turns out Owi was rather wet downstairs after their double favour."

show rowan necklace neutral at midleft with dissolve

ro "(Well that's interesting.)"

return

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

label demon_bastards:

scene black with fade

if serveChoice == 4:
    "Easier said than done, especially when the people you were working with actively sabotaged your efforts. Be it out of spite or shortsightedness, he couldn’t say." 
    "It didn’t matter. What mattered was that Rowan needed leverage and information on the twins. He already had a subject he needed insight on - and someone he could pry the info from."

else:
    "The vile artifact weighted down Rowan’s neck neck like an anchor, and the hero cursed it a hundredth time today."  
    "But try as he might, there was little he could with it, and little he could do about it. And if he was to be honest with himself - little he could do {i}without{/i} it. It was a mistake to arrive at the castle knowing so little. He would not repeat it." 
    "Gathering information - all kinds of it - was step one. He already had a subject he needed insight on - and someone he could pry the info from."

scene bg14 with fade
show xzaratl happy at midright with dissolve
show rowan necklace neutral at midleft with dissolve


"As discreetly as possible, given he had yet to confirm X’zaratl’s true motives. Luckily for him, a simple stroll around the castle made them witness three ongoing succubi romance, with at least one love triangle. That was enough to get the conversation going."

ro "Is this going to be a problem, X’zaratl? Your cubi seducing everything that walks in a mile’s radius?"

xz "I wondered that myself, once."

"The succubus touched his arm gently, and sent him a dazzling smile."

#xzaratl yellow eye flash

xz "My eye is on you and Alexia only, gallant Rowan. Always will be."
xz "But as far as my sisters go… Ah, well, surely you understand - the castle is just {i}full{/i} of wonderful people! People full of passions and aspirations!   "
xz "Many of my kin love that in a mortal, and would gladly share in their excitement, then see it diminished. So If you’re worried nothing will get done, you should be at ease. "
xz "If anything, I believe that having a friendly demon hanging from your shoulder can be {i}quite{/i} the motivator to many. "

if RowanXzaratlInfluence < 1:
    show rowan necklace angry at midleft with dissolve
    "She had yet to let go of him, and her close proximity made him all too aware of the subtle, sweet scent that always surrounded her. He thought of finding a way to push her off without a fuss, but they had yet to breach the topic that was of actual interest to him."

elif RowanXzaratlInfluence > 4:
    show rowan necklace happy at midleft with dissolve
    "She had yet to let go of him, and her close proximity made him all too aware of the subtle, sweet scent that always surrounded her. He took a deep breath, and took a long moment to relish it."
    
else:
    "She had yet to let go of him, and her close proximity made him all too aware of the subtle, sweet scent that always surrounded her. He ignored it, not wanting to cause a fuss before they breach the topic that was of actual interest to him. "
    
ro "… I suppose. It’s a viewpoint I have not considered before."

xz "You’re welcome. I enjoy expanding your horizons."

show rowan necklace neutral at midleft with dissolve

ro "But what of all the- excuse my bluntness- unprotected sex going around?"

xz "I suppose it might keep the maids a little busy-"

ro "It’s not about that."

show xzaratl neutral at midright with dissolve

ro "X’zaratl, I always try to plan ahead. And I want to know - how concerned should I be  about any new half-demons appearing in the castle? The twins alone are a handful."

show xzaratl concerned at midright with dissolve
show rowan necklace shock at midleft with dissolve

"The cubi mistress grew silent. Rowan eyed her curiously, and was surprised to find an almost pained expression on her face."

show rowan necklace neutral at midleft with dissolve

xz "Oh, Rowan! None, I fear."
xz "You must know all demons are born of Kharos’ will. We do not sire children among each other. And for us to sire a child with a mortal… "

show xzaratl neutral at midright with dissolve

xz "It’s a miracle that happens once a decade, at best, and only to demons of exceptional power. I met one such child in the past, sixty years ago. Heard of maybe a dozen more across centuries."
xz "And never of twins. At least not before Jezzy and Andras."

show rowan necklace happy at midleft with dissolve

"{b}That{/b} was what he was looking for. Anything about the twin’s background was priceless - the demon bastards guarded their secrets too well."

if RowanXzaratlInfluence > 2:
    show rowan necklace concerned at midleft with dissolve
    "But seeing X’zaratl’s pained expression, and hearing the longing in her voice… He felt almost guilty about prodding her of all people for information. But it needed to be done.  "

show rowan necklace neutral at midleft with dissolve

ro "Sixty years ago… So were they also a child of a Demon Lord? "

xz "I believe so. She walked a lonely road Rowan - never found an equal to share her ambitions with. Never found anyone she would deem worthy of standing by her side. She never thought it a problem - and I couldn’t agree with that."

#xzaratl yellow/gold eye flash

xz "It is better to have someone who supports you in all things, someone you can confide in, someone who helps you relax after a hard day, and who never judges you. Life is sweeter with someone like that by your side."

show xzaratl concerned at midright with dissolve

xz "And yet she would never allow anyone this close to her. In the end, hers is a truly sad tale. One I do not enjoy telling. "

ro "… I see."

"He found himself nodding along. That didn’t sound that different from the demon bastards he knew."

ro "So what does it take for a Demon Lord to actually sire a child? Is it only a matter of chance? Or is magic involved?"

show xzaratl aroused at midright with dissolve
show rowan necklace shock at midleft with dissolve

"He felt her touch his arm. When he looked at her again, the small smile returned, as did the sparkle in her eye. His nose tickled. "

show rowan necklace happy at midleft with dissolve

xz "It’s a matter of love."

ro "X’zaratl, I don’t- "

show rowan necklace shock at midleft with dissolve

xz "It is!"

show rowan necklace neutral at midleft with dissolve
show xzaratl concerned at midright with dissolve

xz "Oh, gallant Rowan! Our worlds are so different!"

show xzaratl happy at midright with dissolve

xz "To be allowed to be part of yours - to be here on Solanse, to be allowed to explore it, to enrich it! - opened my eyes in ways you cannot imagine! It was the greatest joy of my life, and I celebrate it with every breath I take."
xz "And I know it in my heart that each and every single one of Karnas lovers thought the same. To be part of his world - to carry his child - to be bred by him! - was a joy like no other."
xz "I guarantee you, gallant Rowan. The day the twin’s mother discovered she was pregnant with the twins was the happiest day of her life. "

"X’zaratl bit her lip, her cheeks flushed, and Rowan couldn’t not notice how her hand crept down to her crotch, even as she talked to him."

xz "Aaaah, one day… Maybe one day, I’ll know that joy myself. But for now…"

show xzaratl aroused at midright with dissolve

xz "I would be content in introducing Alexia to it."

if unlockFertilityTreatment == True:
    show rowan necklace shock at midleft with dissolve
    "Rowan blinked, wondering if the cubi mistress somehow overheard his conversation with Alexia on the matter, or if it was mere coincidence."
    
else:
    show rowan necklace shock at midleft with dissolve
    "Rowan blinked, wondering where did {i}that{/i} come from."

show rowan necklace neutral at midleft with dissolve

ro "I think we’re getting off-topic here, X’zaratl."

xz "Maybe a little. And I know many worries plague your mind gallant Rowan. But you must never forget what you’re working towards to:"
xz "The day you and Alexia are finally free to enjoy yourself.  "

#xzaratl yellow/gold eye flash
show rowan necklace aroused at midleft with dissolve

xz "Breeding your wife can be a pleasure like no other Rowan, and I believe Alexia would enjoy it too. I could help you. I could show you. I could-"

if RowanXzaratlInfluence > 4:
    show rowan necklace shock at midleft with dissolve
    "A moan escaped her lips, and she bit her lip again, drawing back. Suddenly, the world felt awfully empty without her warm body and sweet scent surrounding him."
    
else:
    "A moan escaped her lips, and she bit her lip again, drawing back. As always, the world felt awfully empty without her warm body and sweet scent surrounding him."
    
show xzaratl happy at midright with dissolve
show rowan necklace happy at midleft with dissolve

xz "Aaah, I’m getting ahead of myself. I shouldn’t discuss it without Alexia around. Give it some thought, Rowan."

ro "X’zaratl, there are still things-"

xz "Later, gallant Rowan. All that talk of breeding… I need a moment to myself. Excuse me."

hide xzaratl with moveoutright
show rowan necklace neutral at center with moveinleft

"… She was still rubbing her crotch, and Rowan was left with little choice but to let her leave, lest she started relieving herself right there." 
"He was left to ponder on everything she told him regarding the twins' ancestry." 

scene black with fade

"... And whether or not to accept her proposal."

return

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

label xzaratl_virility:

$ breedingGreeting = False
$ lovingGreeting = False

scene black with fade

"Motherhood… To think of all the problems he had to take care of in the castle, it was Alexia’s long-held dream that now occupied his mind."

if firstTreatment == True:
    "Would Nasim’s treatment be enough to satisfy her? He hoped so, but if not…"
    
elif promisedFertilityTreatment == True:
    "He promised her to look into possible solutions, but it was easier said than done. Nasim was one possible angle. And another…"
    
elif alexiaScolded == True:
    "It was precisely why he didn’t want her bothering him with it. He couldn’t even focus on his gods-damned job now. But perhaps there was a way to appease her with minimal effort…"
    
else:
    "He told her to wait, told her now was not the right time. And it was a wise choice. Still…"
    
scene bg14 with fade

if RowanXzaratlInfluence > 4:
    show rowan necklace aroused at center with dissolve
    "The door to X’zaratl’s lair loomed before him. The demoness offered her help before. And her solutions thus far have been… Enjoyable. What harm was there in consulting her?"
    hide rowan with moveoutright
    scene black with fade
    "Licking his lips, he entered the sanctum, and ordered one of the cubi to lead him to their mistress."
    
else:
    show rowan necklace neutral at center with dissolve
    "The door to X’zaratl’s lair loomed before him. The demoness offered her help, after all. And at times, it felt like he needed all the help he could get."
    hide rowan with moveoutright
    scene black with fade
    "He entered the sanctum, and ordered one of the cubi to lead him to their mistress. "

scene bg23 with fade
show rowan necklace neutral at edgeleft with dissolve
show xzaratl neutral at midright with dissolve

"Immediately upon seeing his expression, X’zaratl flicked her wrist, and just like before, the chamber emptied in a blink of an eye, leaving the two alone."

show xzaratl neutral at center with moveinright

xz "Gallant Rowan, you seem troubled. What’s wrong? How can I help?"

show xzaratl neutral at midright with moveoutright
show rowan necklace neutral at midleft with moveinleft

"She grabbed him by the arm, and led him to the large bed at the center of the room so they could sit down."

ro "Straight to the point. Where do I start… You remember how we talked of demons having children? You spoke of me and Alexia having one, one day."
ro "Truth be told…  It’s been Alexia’s dream for a while now, but we had no luck back in Arthdale, and Castle Bloodmeen hasn’t made it any easier. "
ro "And it’s been weighing on her."

show rowan necklace concerned at midleft with dissolve
show xzaratl concerned at midright with dissolve

ro "More than I realized."

show rowan necklace neutral at midleft with dissolve

"Four arms rested on his shoulders, and X’zaratl hugged him close. He could see the anguish in her eye - almost as intense as the one he saw in Alexia’s."

show xzaratl neutral at midright with dissolve

xz "Tell me everything."

if RowanXzaratlInfluence > 4:
    show rowan necklace concerned at midleft with dissolve
    "And he did. Once he started, he couldn’t stop. He poured his heart out, starting from their first attempts in Arthdale, and ending on Alexia stealing Nasim’s potion, and the fallout of it all."  
    "X’zaratl listened intently, nodding her head, only from time to time interrupting to reassure him he did nothing wrong."
    show rowan necklace happy at midleft with dissolve
    show xzaratl happy at midright with dissolve
    $ change_base_stat('g', -3) 
    "And in the end, he did feel a little better for getting it all off his chest." 
    show rowan necklace neutral at midleft with dissolve

else:
    "X’zaratl listened intently to his every word, nodding her head, only from time to time interrupting to reassure him he did nothing wrong. Mindful of her dubious motives, he told her only what she needed to know - just enough to satisfy her."
    
show xzaratl concerned at midright with dissolve

xz "Ah, Rowan! That is all so dreadful! And I feel for Alexia. I know what it’s like, to be denied that which we so desperately desire." 

show xzaratl neutral at midright with dissolve

xz "But she must not fret, and neither should you. She {b}will{/b} conceive!" 

show xzaratl happy at midright with dissolve

xz " I have seen how much you try for her. Whatever you put your mind to, you always achieve. How can this compare to the monumental tasks you’ve already accomplished in her name?"

ro "That’s very sweet of you. But - well, I was hoping for something more than words of encouragement?"

xz "Of course! You desire my help - and I will grant it."
xz "But first, I must ask. Do you do it often? When you fuck - do you always come inside of her?"

if 'all_actors["alexia"].relation < 50':
    show rowan necklace concerned at midleft with dissolve
    show xzaratl concerned at midright with dissolve
    ro "To be honest, things have been a little rocky between us recently."
    
else:
    if avatar.corrupt < 31 and all_actors["alexia"].corruption < 31:
        show rowan necklace shock at midleft with dissolve
        ro "As often as any couple, I would say?"
    elif avatar.corrupt > 30 and all_actors["alexia"].corruption < 31:
        show rowan necklace angry at midleft with dissolve
        ro "I try, but Alexia isn’t always in the mood."
    elif avatar.corrupt < 31 and all_actors["alexia"].corruption > 30:
        show rowan necklace aroused at midleft with dissolve
        ro "Well… Not often enough, apparently. Feels like Alexia can’t get enough nowadays…"
    else:
        ro "Sometimes, sometimes not. We’ve been trying new things, kind of hard to keep track of it all."
        
show rowan necklace neutral at midleft with dissolve
show xzaratl neutral at midright with dissolve

ro "X’zaratl, I think I know where this is going. I don’t think it’s the frequency of our lovemaking that’s the problem. I was thinking that maybe there’s a spell you could try on her?"

"Surprisingly, he saw X’zaratl shake her head. "

xz "There are no shortcuts in love. I learned that a long time ago, and I know you know it too."

if RowanXzaratlInfluence > 3:
    show rowan necklace angry at midleft with dissolve
    ro "This isn’t a matter of love. It’s a simple biological problem, and it should have a simple magical solution."
    show rowan necklace neutral at midleft with dissolve
    xz "Rowan, please. Hear me out."

xz "You must not think of this in terms of fertility - or virility - alone. It is part of it, yes. But must look at the bigger picture."
xz "You must ask yourself - what does Alexia desire?"

#xz eye flash yellow

show xzaratl happy at midright with dissolve
show rowan necklace aroused at midleft with dissolve

xz "Ask yourself - when you come inside of her - do her eyes not shine with joy? Do the corner of her lips not twist up in delight? Do her moans not grow breathless and satisfied?"

show rowan necklace neutral at midleft with dissolve

ro "I mean…"

xz "If all you said is true, this is no passing fancy, but a dream she carried for years! A desire that has always laid beneath the surface, and now, finally, rises to see the light of day."

if RowanXzaratlInfluence > 5:
    "He was having a hard time disputing her claims - why did it feel like the conversation was running away from him?"
    
else:
    "Her words made him pause. As always, she was shining new light on his problems, and he found himself nodding along, eager for her insight."
    
show xzaratl neutral at midright with dissolve

xz "Gallant Rowan, please, consider what I am about to say."
xz "What Alexia asked for, is to be blessed with your child."

show rowan necklace shock at midleft with dissolve
show xzaratl aroused at midright with dissolve

xz "But what she {i}desires{/i}, is for you to {i}breed{/i} her."

if avatar.corruption < 31:
    show rowan necklace concerned at midleft with dissolve
else:
    show rowan necklace happy at midleft with dissolve

xz "For you to thrust your cock inside of her, as hard as you can, and pump her full of seed. Not once, not twice - but every week, every {i}day{/i}! Whenever you can! Without rest and without restraint, until she’s heavy with your child! "

show xzaratl happy at midright with dissolve

xz "And {i}with that{/i}… I could help. "

show rowan necklace aroused at midleft with dissolve

"She smiled at him. He was so lost in her sparkling eye he almost didn’t notice her bring something up to his face."

show rowan necklace shock at midleft with dissolve

"A dark-red ring, oddly shaped, with delicate, engraved runes. It shimmered in the flickering light of the sanctum’s torches."

show rowan necklace neutral at midleft with dissolve

"It looked too large to fit over his finger - then he realized that wasn’t where it was intended to go."

xz "Let me slip this over your cock, gallant Rowan. Then give it a few hours to work its magic."
xz "I will make Alexia ready for you. You will give her a breeding session she desires so much." 
xz "And afterwards… I can’t guarantee success. But I know both you and her will find the attempt enjoyable. A few weeks of trying, and I’m sure you’ll see results."

"The dark ring beckoned. He had to force himself to look away - only to be once again met with X’zaratl’s radiant smile."

#If JezeraNTRDetoxSex: Yes 
#(Not yet written) 
#show Rowan awkward. 
#Rowan: Isn’t this…   
#X’zaratl: The same ring I gave Alexia before, yes. But don’t worry - it’s a versatile tool, and you will be in control this time. It will behave as you need it to.  
#show Rowan aroused. 
#He licked his lips nervously. For it to keep him on edge… Would be counterproductive. But that was not the main problem. 
#show rowan necklace neutral at midleft with dissolve

ro "X’zaratl, that’s a… Far-reaching conclusion." 

show rowan necklace concerned at midleft with dissolve

ro "And truth be told, I haven’t been looking for an {i}immediate{/i} solution. Not with everything else going on." 
ro "You know how hard it would be to raise a child now."

"He made a vague motion with his hand. Right now, it felt like a lame excuse."

show rowan necklace happy at midleft with dissolve

"Not to X’zaratl. She squeezed his shoulder reassuringly, and nodded her head, sympathy clear in her gaze."

show rowan necklace aroused at midleft with dissolve

"By now, he was all too aware of the pleasant heat of her body, of the sweet scent that always followed her, and even the softness of the bed they both sat upon. He felt he could sink in it. In it all."

show rowan necklace neutral at midleft with dissolve

xz "Oh, Rowan, what a difficult role you have! Both lover and protector, torn between keeping Alexia safe, and making her dreams come true!"
xz "I understand, I really do. And if it’s your wish, gallant Rowan…"

show bg23 with flash

"She trailed a fingernail along the ring’s surface, making it sizzle with small, white flames that quickly died out."

xz "Then I can make it so nothing will come of your encounter whilst the ring is on."
xz "Fair Alexia will get a taste of what she so desperately desires - of what it means to be bred, of how it feels to have your cock thrusting in her without stop or rest, pumping her full of cum."
xz "Just a taste. Just one night, for that is all we can steal for her, with Jezera breathing down our necks. One night without consequence, so that in the future you can breed her for weeks, not days. Just as she deserves."

show rowan necklace aroused at midleft with dissolve

ro "Y-yeah…"

xz "One night, to give her hope for tomorrow."

show rowan necklace neutral at midleft with dissolve

ro "She would love it, for sure."

xz "And yet…"

show rowan necklace aroused at midleft with dissolve
show xzaratl concerned at midright with dissolve

"Her dizzying, sweet fragrance wrapped him like a blanket. She touched his cheek gently, making him focus on her and her alone she continued, another hand placed on his chest."

xz "Gallant Rowan, I know you always try to be sensible. Alexia loves that in you, and so do I."

#xzaratl eye flash yellow

xz "But in matters of love, is it not better to follow your heart? Leave reason and logic at the door, and let yourself be carried away by romance?"

show xzaratl happy at midright with dissolve

xz "Do you not want to try and give your beloved what she so desperately desires?"

show rowan necklace concerned at midleft with dissolve

ro "X’zaratl, the consequences…"

xz "I will be there to help you handle them. She wants this. And I believe you want it to. "

show rowan necklace aroused at midleft with dissolve

"Her lips almost brushed against his, and her hand ventured south, towards his crotch. Her breath was like fire, and she never stopped whispering into his ear. "

show xzaratl neutral at midright with dissolve

xz "Take the ring Rowan."

show xzaratl happy at midright with dissolve

xz "Let it work its magic in full."
xz "Show your wife how it will feel to be bred by your cock."

show xzaratl aroused at midright with dissolve

xz "Make her pregnant with your child."

menu:
    "Follow X’zaratl’s advice in full.":
        $ released_fix_rollback()
        $ RowanXzaratlInfluence += 3
        $ breedingRingAccepted = True
        show xzaratl happy at midright with dissolve
        ro "… A calculated risk"
        "Her eye sparkled in the dark, curious. He swallowed hard, his tongue seemingly possessing a mind of its own."
        show rowan necklace neutral at midleft with dissolve
        ro "Even with the ring on, there’s no guarantee anything will come out of it, right? But at least… It would be an honest attempt… Right?"
        xz "Yes. It would be the honest thing to do. It would be the right thing to do."
        show rowan necklace happy at midleft with dissolve
        ro "Y-yeah. It’s the right thing to do."
        #xzaratl yellow eye flash
        show rowan necklace aroused at midleft with dissolve
        xz "Exactly. Pumping your wife full of your potent, virile cum is the right thing to do."
        ro "And if it doesn’t work… "
        xz "Then you can try again."
        xz "And again, and again, and again, and again."
        "X’zaratl’s seductive tone made it all too easy to picture doing exactly that. When she started to undo his pants, he made no move to stop her."
        jump acceptedRing
        
    "Demand the contraception charm.":
        $ released_fix_rollback()
        $ RowanXzaratlInfluence += 2
        $ contraceptionRingAccepted = True
        show rowan necklace neutral at midleft with dissolve
        show xzaratl happy at midright with dissolve
        "He seized her hand, and met her innocent gaze with his own unrelenting one."
        ro "X’zaratl, we’re not doing anything without the contraception charm. It’s too risky otherwise."
        xz "...Of course, Rowan."
        show bg23 with flash
        "Again, she trailed her fingernail over the dark-red ring, this time over the whole of it as she weaved her spell."
        show rowan necklace concerned at midleft with dissolve
        "… Was it dishonest of him? To fuck his wife under a false pretense?"
        #xzaratl yellow eye flash
        show rowan necklace aroused at midleft with dissolve
        xz "A taste. Of things to come. Until you’re free to breed her as she deserves. She deserves to know it will feel. She deserves to hope again." 
        show rowan necklace neutral at midleft with dissolve
        ro "… Yeah. Exactly."
        "Her finger reached the starting point, and the ring shone white for a moment, as the charm took hold. Still holding it, she reached down again - and this time, he found no reason to stop her."
        jump acceptedRing
        
    "Refuse the ring altogether.":
        $ released_fix_rollback()
        $ RowanXzaratlInfluence -= 1
        show rowan necklace neutral at midleft with dissolve
        show xzaratl concerned at midright with dissolve
        "He seized her by the hand- and pushed her away."
        ro "X’zaratl… No."
        ro "It’s too risky without the contraception charm, and with it… That just defeats the purpose, doesn’t it? It would be done for my sole satisfaction."
        show rowan necklace neutral at edgeleft with moveoutleft
        "He forced himself up - without X’zaratl hanging off his shoulders, the sanctum suddenly felt cold and unpleasant. He didn’t mind it - it served to cool his head, and calm his feverishly beating heart."
        ro "It would be dishonest. Plain and simple."
        show xzaratl happy at midright with dissolve
        xz "Only if you didn’t intend to repeat it without the charm later."
        show rowan necklace angry at edgeleft with dissolve
        ro "That’s a level of mental gymnastics I do not subscribe to."
        "Glaring at the succubus, he dared her to challenge his words - only for X’zaratl to beam at him, smiling from ear to ear."
        xz "I understand. You will make her dreams reality on your own terms."
        show rowan necklace neutral at edgeleft with dissolve
        ro "… Something like that."
        xz "Then you must make haste, and find a way to rescue her as soon as possible."
        "The cubi mistress rose from her bed and escorted him back - her hand touching his arm gently as she did."
        hide rowan with moveoutleft
        hide xzaratl with moveoutleft
        scene bg14 with fade
        show xzaratl neutral at midleft with dissolve
        show rowan necklace neutral at midright with dissolve
        xz " I will ask my cubi to get out of your way today as you work. And if you need anything of me, you need only to ask Rowan."
        xz "Even if it is just someone to talk to."
        ro "I know. And… Thank you, X’zaratl. For hearing me out, and for understanding."
        xz "Of course."
        scene black with fade
        show xzaratl neutral behind black
        xz "Anytime, Rowan."
        return
        
label acceptedRing:

show rowan necklace aroused at midleft with dissolve
show xzaratl aroused at midright with dissolve

"There was a soft gasp, and he saw X’zaratl stare, as if entranced, as his cock stood hard and throbbing. Her delicate hands hovered nearby, and she licked her lips hungrily."

show rowan necklace happy at midleft with dissolve

xz "Ah, Rowan, you truly have the most wonderful cock… Have I ever told you how lucky your wife is to have you?"

menu:
    "Let her touch it.":
        $ released_fix_rollback()
        $ RowanXzaratlInfluence += 1
        ro "You can touch it, if you want."
        show xzaratl happy at midright with dissolve
        xz "You torture me, Rowan. Today, it belongs to your wife alone."
        "She bit her lip, then placed a quick kiss on his cheek, her eye sparkling."
        xz "But thank you for the offer."
        
    "Keep it “professional.”":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        show xzaratl happy at midright with dissolve
        ro "X’zaratl…"
        xz "I know. I wouldn’t dare. Today, this cocks belongs to your wife alone."
        show rowan necklace happy at midleft with dissolve
        xz "But I can at least admire it from a distance, can I not?"
        
show rowan necklace aroused at midleft with dissolve 

"He heard a soft click, and drew a sharp breath himself, when the ring wrapped itself around the base of his cock, the other half extending around his testicles."

show rowan necklace shock at midleft with dissolve 

"He expected… He wasn’t sure what. It was warm, and vibrated gently, almost unnoticeably. It locked itself tight, but not uncomfortably so."

show rowan necklace neutral at midleft with dissolve

xz "There. Give it a few hours, while I make Alexia ready for the evening."

"She redid his pants, and drew away. Exhaling, Rowan repositioned his cock, trying to pay no mind to the strange sensation. A few hours… That didn’t sound that bad."

ro "Fair enough. I still have castle business to take care of. "

xz "Take your time, gallant Rowan."

scene black with fade
show xzaratl happy behind black

xz "And ready yourself for an experience you too won’t forget anytime soon. "

"..."

scene bg14 with fade
show alexia 2 necklace neutral at center with dissolve

al " X’zaratl, you’re skulking around again."

show alexia 2 necklace neutral at midleft with moveoutleft
show xzaratl happy at midright with dissolve

"The demon gave a sheepish laugh - and in a blink of an eye, she was beside her, arms around her, grinning from ear to ear."

xz "Oh, Alexia. I’m sorry! I didn’t want to startle you."

show alexia 2 necklace shocked at midleft with dissolve

al "But I was talking with Rowan, and he- well, he saw fit to let me in on some of your problems." 

show xzaratl happy at center with moveinright
hide alexia
show alexia 2 necklace aroused at midleft with dissolve

"The demon leaned in, whispering in her ear the topic of her earlier discussion with her husband. Alexia sighed, her cheeks turning a light shade of red."

show xzaratl happy at midright with moveoutright
show alexia 2 necklace neutral at midleft with dissolve

al "To have people actually approach me regarding it… It’s a little embarrassing."

xz "It should not be. There is nothing to be ashamed of."
xz "I’ve met many women in my life who had similar problems. Dear Duchess Moress comes to mind, among others."
xz "It is no shame to face adversity, sweet Alexia. I know that as long as you and Rowan work together, there is no hurdle you cannot overcome."

al "I would say that given the nature of the problem, it can only be resolved together."

if promisedFertilityTreatment == False and firstTreatment == False:
    show alexia 2 necklace angry at midleft with dissolve
    al "And given how difficult Rowan is on that particular topic…"
    xz "A thing of the past, I believe."
    
else:
    show alexia 2 necklace shocked at midleft with dissolve
    xz "And resolve it together you shall.  "

show xzaratl happy at edgeright with moveoutright
show alexia 2 necklace aroused at midright with moveoutright

"Both sets of arms grabbed Alexia’s hand, and the demon pulled her gently in the direction of her room, gracing her with a vibrant, friendly smile."  

xz "Come with me, Alexia. Rowan has something planned for you, for the evening. And I am to make you ready for it."

if AlexiaXzaratlInfluence == 0:
    show alexia 2 necklace concerned at midright with dissolve
    "She regarded her warily. It was a lie too easy to disprove, but for him to actually involve her, after everything they’ve discussed…  "

else:
    "Her heart skipped a beat - he actually planned something, and had X’zaratl involved? It would be a lie to say she was not excited, but…"
    
menu:
    "Follow her to your room.":
        $ released_fix_rollback()
        $ AlexiaXzaratlInfluence += 2
        scene black with fade
        show alexia 2 necklace aroused behind black
        al "Well… If it was Rowan’s idea…"
        
    "Absolutely not! Rowan shouldn’t let X’zaratl interfere in their lives like that!":
        $ released_fix_rollback()
        $ AlexiaXzaratlInfluence -= 2
        show alexia 2 necklace angry at midleft with moveoutleft
        show xzaratl shocked at midright with moveoutright
        "She pulled her hands away, and glared at the surprised succubus."
        al "X’zaratl, I don’t know what it is you managed to trick my husband into, but I will have no part in it."
        show xzaratl happy at midright with dissolve
        xz "Making your dreams-"
        show xzaratl shocked at midright with dissolve
        al "Come true? I’m sorry X’zaratl- but I don’t think you’re in them."
        show xzaratl concerned at midright with dissolve
        "The demoness looked almost hurt by her words, but Alexia would not take them back. She turned around and left to find her husband, tell her what she thought of all of this."
        scene black with fade
        "He didn’t look happy either, shifting uncomfortably in his chair. But her decision was final, and she would not discuss it further." 
        $ change_relation('alexia', -5)
        $ virilityTreatmentAlexiaDenied = True
        return
        
scene bg6 with fade
show rowan necklace neutral at midright with dissolve
show clamin happy at midleft with dissolve

cla " ...Aaaaand that’s another thirty gold to the coffers. After my cut, of course."

ro "Mhm."

"Hours have passed since his conversation with X’zaratl. His castle duties were never a fun affair, but today, they were proving exceptionally dreary." 
"The soft vibrations of X’zaratl’s ring never ceased, but neither did they grow in intensity, constantly sending subtle warmth across his crotch." 

show rowan necklace aroused at midright with dissolve
#clamin surprised
        
"He was starting to feel its effect. Like a slight… {i}Churning{/i} in his balls. They felt heavier. Swollen, almost. His cock was half-erect at all times, and it increasingly more difficult to hide it’s outline. "

show rowan necklace happy at midright with dissolve
#clamin happy

"A few more hours. A few more hours, and he would finally put it to good use. Find his wife, bend her over, and-"

cla "Rowan, are you listening? "

ro "Hm? Yes, yes, of course. Thirty gold, after your cut. Sounds fine to me."

cla "Great! So, moving on…"

"He had a gnawing suspicion Cla-Min took advantage of his temporary distraction to pocket a few extra gold coins for herself, but just once, he couldn’t be bothered to call her out on it."

scene black with fade

"Other things occupied his thoughts. Like Alexia’s waiting, wet, empty- "

scene cg930 with fade
pause 3
show xzaratl happy behind cg930
show alexia 2 necklace aroused behind cg930

xz "-{i}Cunt{/i}. Just imagine it overflowing with Rowan seed, his cum dripping down your belly and back, as he keeps pumping into you from above, with limitless vigour!"  

al "A-ah, X’zaratl, that’s-"

"What started as a casual conversation held at Rowan’s desk, with X’zaratl behind her, holding her by the shoulders, soon ended with all four of the demoness hand caressing her body, and the demoness whispering sweetly into her ear."   
"In front of her, laid X’zaratl’s violet, crystal ball. It kept showing her things - figures of two people intertwined, of lovers lost in pleasure." 
"In possibly every position known to man, and then twice that. And X’zaratl insisted one day, she and Rowan would try them all." 

al "… A-ah… Didn’t the last one... Require both of us flying? "

xz "Nothing a little magic can’t fix."

if all_actors["alexia"].corruption < 31:
    "Almost against herself, Alexia’s imagination ran wild. She never thought herself boring in the bedroom - but X’zaratl’s ideas were on a whole other level."
    xz "Don’t worry. You’ll try them all, in time. But for now…"
    
else:
    "She had to admit - the Succubus had {i}quite{/i} the imagination." 
    al "Should we- Ah!- Should we try them all?"
    xz "You {i}will{/i}. I promise. But for now…"

"The image shifted again, and X’zaratl’s fingers pushed her lower lips open, making her squeal in delight."

xz "There. This one. That’s the position you should greet Rowan with, when he comes to breed you today. "

al "H-ha… You keep saying it like that…"

xz "Because that’s what it will be! He will ram his cock inside of you, balls-deep, and keep thrusting with a single goal in his mind: To cum inside, paint your womb white with his semen."

#xzaratl eye flash yellow

xz "What you always desired so desperately, comes true today. Why be embarrassed about it? Is it wrong to rejoice when dreams become reality?"

"She tried to answer, but just right then, X’zaratl hit a sensitive spot with her finger, and she could only moan in response. Several times now, she arrived right at the edge of an orgasm - only to have it denied her every time."

xz "There is no reason to be ashamed anymore, fair Alexia. Revel in tonight."
xz "Just try. I’ll help. I’m always here to help."
xz "So repeat after me -"

scene cg931 with fade
pause 3
show xzaratl aroused behind cg931
show alexia 2 necklace aroused behind cg931

xz "“Ah! I can’t wait to feel my husband’s cock inside of me! ”"

menu:
    "“Ah! I can’t wait to feel my husband’s cock inside of me!”":
        $ released_fix_rollback()
        xz "Such a lucky girl, to have such a wonderful man by her side…"
        show xzaratl happy at center with dissolve
        
    "“Still too embarrassing!”":
        $ released_fix_rollback()
        show xzaratl happy at center with dissolve
        xz "Why? You’re husband and wife. It’s only natural."
        xz "Come now, Alexia. Be honest with yourself. Say what you truly want."
        
xz "Say: “I want him to ram it inside of me, as hard as he possibly can!”"

menu:
    "“I want him to ram it inside of me, as hard as he possibly can!”":
        $ released_fix_rollback()
        xz "Yes, exactly! Now… "
        
    "...":
        $ released_fix_rollback()
        "A quiet moan escaped her lips, as she writhed in X’zaratl’s grasp."
        xz "Don’t try and hold your voice, Alexia. Speak your true desires. Repeat after me:"
        
xz "“I want him to breed me! I want him to impregnate me!”"

menu:
    "“I want him to breed me!”":
        $ released_fix_rollback()
        $ AlexiaXzaratlInfluence += 1
        $ breedingGreeting = True
        "She cried out in pleasure, only to find her lips sealed in a passionate kiss by the demoness. Quivering, she surrendered herself to her, growing limp in her arms."
        xz "There you go! Now, come with me…"
        
    "“I want him to make love to me.” ":
        $ released_fix_rollback()
        $ lovingGreeting = True
        "She glared almost defiantly at the succubus - only to find her pressing her lips against her, locking them in a passionate kiss. And even though X’zaratl had yet to cease her ministrations, they grew more gentle, more loving, after hearing her words."
        xz "Oh, Alexia~~~ You two are made for one another! Don’t worry - he will do just that!"
        xz "That’s enough teasing for now, fair Alexia. Please, come with me…"
        
scene black with fade
show xzaratl happy behind black

xz "Let’s greet your husband properly."

"..."

scene bg14 with fade

show rowan necklace aroused at midleft with dissolve

"Hours. Literal hours of constant vibrations. The hardness of his cock could no longer be concealed, the outline of his throbbing phallus clearly visible to all who could see. "

show rowan necklace happy at midleft with dissolve

"He no longer bothered to hide it. The cubi all eyed it hungrily, but for once, he felt no temptation to waste his lust on such lowly sluts. A single thought occupied his mind, a single desire guided his action."

show rowan necklace aroused at midleft with dissolve

"The need to {i}breed{/i}." 

show rowan necklace happy at midleft with dissolve

"He laughed out loud. Gods, that was stupid! But his balls felt so heavy and swollen, that was all he could think about. Taking his cock out, plunging it into his wife, and fucking her till she’s full of his cum." 
"But his wait was now over. He was already undoing his pants the moment he saw the door to his room. He let his cock sprung free, and opened the door wide." 


scene cg932 with fade
show alexia necklace naked aroused behind cg932
show xzaratl happy behind cg932
pause 3

xz "Hello, Rowan."

al "A-ah, hello dear~~."

"They were ready for him. Alexia laid naked on her back, holding her legs high and spreading them wide, presenting her {i}cunt{/i} for him. It glistened in the evening light, parted welcomingly." 
"He almost didn’t notice X’zaratl. The demon knelt behind her, allowing Alexia’s head to rest on her thighs. One set of arms ran lovingly through her hair. The other - held her legs ups. Kept them spread." 
"Kept his wife ready to be bred. Ready to be impregnated." 
"Mad with desire, he shut the door close and started throwing his clothes off, sending his armor and sword flying. Alexia watched, speechless, her eyes drawn to the throbbing rod between his legs." 

if all_actors["alexia"].corruption > 30:
    "She grinned at the sight of it, and licked her lips. The dark-red ring around the base of his cock made his tool look almost massive. And it was all at the thought of {i}her{/i}."

else:
    "She laughed nervously, then bit her lips. The dark-red ring around the base of his cock made his tool look almost massive. She knew he found her attractive, but this…"
    
scene cg933 with fade
show alexia necklace naked aroused behind cg933
show xzaratl happy behind cg933
pause 3

"He climbed the bed without hesitation. She let her eyes wander up - across his sculpted chest, his toned muscles - and looked into his eyes." 
"They saw no world beyond her." 
"A gentle, feminine hand caressed her cheek as Rowan positioned himself over her, his cock dangling inches away from her soaking cunt." 

xz "What do you say, Alexia?"

al "Ah, Rowan…"

if lovingGreeting:
    al "Make love to me, dear."
    
else:
    al "Breed me, my love." 

"The burning flames of his desire burst forth, twice as strong, and he thrust his hips forward. His throbbing cock parted her overflowing pussy with ease-"

scene cg934 with fade
show alexia necklace naked aroused behind cg934
show xzaratl happy behind cg934
pause 3


ro "Ah!!"

"And his world went white with ecstasy. He threw his head back, almost blind from the overwhelming sensation. Gods, his cock was sensitive, and her cunt squeezed him so tight! Her pussy felt incredible. It- "

"A gentle kiss was placed upon his lips. He blinked, and found himself looking at X’zaratl’s benevolent smile. "


xz "Relax, Gallant Rowan. Breed her properly. Do not rush, but do not hold back either."
xz "And cum with her. Don’t worry, the ring will help."

if all_actors["alexia"].corruption > 30:
    "His wife’s quiet moans reached his ears, he looked down, and looked straight into Alexia's loving, slightly glazed over eyes." 
    "Without a moment of hesitation, he started thrusting again-"

else:
    "His wife’s quiet moans reached his ears, he looked down, and looked straight into Alexia's lust dazed eyes. Without a moment of hesitation, he started thrusting again-"
    
"And again- and again! The searing ecstasy robbed him of all reason. Alexia’s velvet, soft pussy felt like heaven, her wet walls both soothing and driving the raging desire that took hold of his cock."

al "Ha- ha- Aaah, Rowan!"

"And Alexia - she was used to her husband taking her hard- used to him taking the lead- but the desperate, almost primal thrusts were like nothing before." 
"She cried in pleasure again. She could see Rowan looking into her eyes - and X’zaratl too. And she could even see the demoness’ own cock, painfully hard and neglected, pressing against her black robe, leaving a wet, sticky stain from the inside."  
"And at the same time, she saw none of it. She knew no world beyond her husband’s iron-hard cock, splitting her apart with every thrust. His heavy balls hitting her, their slapping noise barely noticeable through Rowan’s grunting and her own moans."  
"How could she hold back? How could she last? Her eyes rolled back -"  

show cg934 with sshake
show cg934 with sshake
show cg935 with flash
show alexia necklace naked aroused behind cg935 
show xzaratl happy behind cg935 
pause 3


al "A-aaah!"

"Just as ecstasy took her, a surge of hotness filled her to the brim. Was this it? The day she waited so long for?!"

al "A-ah… Y-yes! Finally!"

"His hard cock throbbed inside of her, cumming seemingly without end. Gods- if she could only ever remember one moment in her life, she would wish for it to be this one. The feeling of Rowan’s cock cumming inside of her." 
"And he felt it too. Only partially aware of his wife’s happy moans, he kept thrusting, driven by instinct, head thrown back. Lost in his own ecstasy, he didn’t care how the force of his thrust caused his cum to spurt out of her pussy." 
"Gods, it felt amazing - to finally find release. But the ring around still vibrated gently, and he found his need didn’t recede one bit-"    
"He felt X’zaratl’s lips on his own again. A gentle, delicate kiss - as he was still thrusting into his wife. A moment of quiet and clarity, amidst the hurricane of lust."

scene cg934 with fade
show alexia necklace naked aroused behind cg934
show xzaratl happy behind cg934
pause 3

xz "Excellent work, Rowan."
xz "Keep going."

if lovingGreeting:
    al "Y-yes! Keep going! Fuck me, darling!"
    
else:
    al "Y-yes! Keep going! Breed me, darling!"
    
"Alexia didn’t realize - never dreamed - how good it would feel to {i}finally{/i} have Rowan fuck her like this." 
"She giggled, drunk with desire, and made no efforts to hold back her moans as Rowan resumed his feverish thrusts." 

show cg934 with sshake
show cg934 with sshake
show cg935 with flash
show alexia necklace naked aroused behind cg935 
show xzaratl happy behind cg935 
pause 3

"It didn’t take long until Rowan felt himself cum again. He threw his head up again, grunting in pleasure, not even caring how it looked or sounded-"  
"And met X’zaratl’s sweet lips {i}again{/i}. They were like a glass of fine wine, and he drank it without hesitation, his cock still twitching inside of his wife."  
"And each spurt of cum was rewarded with a slow, almost loving kiss."
"Finally, when he was done, she let go of him. He looked into her sparkling eyes, at her crimson red lips-"   
"And saw her smile." 

xz "Excellent work Rowan. You’re the best lover a woman could ask for."
xz "Keep going. Keep fucking your wife. Make her understand what true bliss is."
xz "Make her experience a taste of her happy ending."

"Alexia stirred beneath him, her hard breathing barely noticeable through the maddening beating of his heart. X’zaratl kissed him again, for a brief moment, then pulled away-"

menu:
    "Do not let her pull away!":
        $ released_fix_rollback()
        $ RowanXzaratlInfluence += 2
        scene cg934 with fade
        pause 3
        "He leaned in, forcing her lips open with his tongue, not wanting to let her go." 
        "X’zaratl offered a quiet moan in protest, and tried to pull away again, to no success. He wouldn’t let her - he wanted her just as much as he wanted Alexia." 
        "And when she felt it - felt his passion as his tongue danced with her - X’zaratl returned it a thousandfold, grabbing his head and pressing into his lips." 
        "Only then did he start thrusting again, driven to madness by the constant vibrations around his cock. His world was reduced to Alexia’s tight pussy and X’zaratl’s sweet lips - and he would trade it for no other."  

    "Let her pull away, and focus on Alexia.":
        $ released_fix_rollback()
        "- and Rowan turned his attention back to Alexia. Back to his sweet wife - his sweet,  moaning wife." 
        "He started thrusting again, driven to madness by the constant vibrations around his cock, Alexia’s tight pussy and X’zaratl’s perverted whispers." 

"He thrusted and came, again-"   
"And again-"

scene black with fade

"{i}and again-{/i}"
        
"..."

#new bed var
scene black with fade
show rowan necklace naked behind black
show xzaratl happy behind black

"He didn’t realize when morning caught them. Their session continued well into the night, and at some point, exhaustion must have taken them both, for he did not recall their fucking actually coming to an end." 
"Not that he cared. With a smile, he ran his fingers through Alexia’s hair, a gentle gesture that got him a half-asleep murmur from his exhausted wife. If he could, he would stay like that forever. But the depressing reality…" 

xz "I’ve brought you breakfast, gallant Rowan. And the twins should be still distracted with the impromptu orgy I ordered yesterday. Should buy you an hour more."

"Like a shadow, X’zaratl tiptoed around the room, carrying a silver tray in her hands. Did she stay with them the entire night? That would explain their folded clothes, and opened windows…"

ro "… Thank you, X’zaratl. "

xz "You’re welcome. I should go now, try to buy you more time. Andras can occupy himself, but Jezzy will go hunting for entertainment if left unattended for too long."

"Rowan stifled a laugh, and waved goodbye at the succubus. X’zaratl sent him another vibrant smile, and hurried out of the room." 
"Alexia shifted beside him, and he kissed her head lovingly. To stay like that forever…"

scene black with fade

"Would be bliss."

$ change_base_stat('c', 5)
$ change_corruption_actor('alexia', +5)
$ change_relation('alexia', 5)
$ virilityTreatmentSex = True

if breedingGreeting:
    $ virilityTreatmentBreedingSex = True

if contraceptionRingAccepted:
    $ virilityTreatmentSafeSex = True

return

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

label dead_orc_lord:

scene bg6 with fade
show rowan necklace neutral at midright with dissolve
show skordred neutral at edgeleft with dissolve

"Rowan began his day squirrelled away at his desk, his mountain of paperwork slowly ebbing away with each passing hour, but soon found himself summoned to the throne room by none other than Skordred."
"The dwarf lingered outside of the doorway, his rough face drawn into a serious expression."

sk "I'll be needin' yer assistance. There's been'a discov'ry."

"Rowan looked at his paperwork; there wasn't much left, and if given the time, he'd prefer to knock this out sooner than later."
"But facing Skordred, the look on the dwarf's face told him that no such requests would be honored."

ro "Alright. I'll be right there."

hide skordred with moveoutleft

"Skordred nodded stiffly before leaving Rowan to his work."

scene bg6 with fade
show andras displeased at edgeright with dissolve
show jezera neutral at midright with dissolve
show skordred neutral at midleft with dissolve
show rowan necklace neutral at edgeleft with dissolve

"Rowan followed the summons shortly after and did not bother to hide his surprise at seeing Andras and Jezera waiting in the throne room as well. This must have been a truly impressive find for Skordred to gather all three of them here."
"Once they were seated, Skordred rolled out a metal table with a large canvas sheet covering whatever discovery he had made underneath." 
"Andras showed little patience while the dwarf moved, his arms crossed tightly over his chest and a sneer curled on face, but Jezera eyed the cloth with morbid curiosity, the hint of a smirk on her lips."
"Even Rowan wondered what could be underneath. Something useful, surely, or else Skordred wouldn't have bothered with the twins' presence."
"The dwarf reached up and tore the canvas cloth off, allowing it to settle on the ground as the table revealed the cleaned remnants of bones. Rowan stared at the remains in confusion."
"That is, until he saw the armour and crown accompanying them."

ro "Is that…?"

sk "Aye, 'tis an orcish Lord. Grismar the Mighty, to be exact."

show andras happy at edgeright with dissolve

"Andras let out a loud laugh of recognition, a demonic smile spreading across his face. Rowan too knew exactly who Skordred was talking about. In fact, it was quite hard to forget."

an "I wondered what happened to the old bastard's body."

"Jezera pursed her lips."

je "Hmm… I don't recall him."

an "How could you forget? The beast was a legend!"

sk "He's over two-hundred years old by now. Served under the demon lord at the time."

an "Lord Ulradath! They were a fierce team. Gismar ruled with an iron fist and Ulradath helped pave the way for his takeover."
an  "They were an inspiration to orcs and demons everywhere. They still pass the stories down among our soldiers."

"Rowan stared at Andras in disbelief. It seemed that they had very different recollections of the king and his escapades."

ro "That's not how I remember it…"

"Rowan, even as a young boy, knew about King Gismar and his slaughter. Everyone he grew up with, in fact, were made aware of the atrocities that came from the Orcish people and the demons they allied with."
"King Gismar and his orc army pillaged, raped, and destroyed any kingdom and village they came across, whether the people showed resistance or not. They didn't care if they would be welcomed willingly; they just wanted to see blood."

an " You remember a weaker story."

"Rowan gave Andras a skeptical look but chose not to argue." 
"Jezera eyed up the armor alongside the bones. Rowan could see the wheels turning in her mind as she no doubt thought of some use for the materials."

sk "I can put the bones on display, but what do ye want to do with the rest of it?"

"Skordred gestured toward the materials lying beside the body while Andras and Jezera contemplated their use."

an "Let's split the armour among our stronger troops! It will inspire them on the battlefield and draw them further to our cause."

"Jezera didn't seem so convinced by her brother's suggestion. She tapped her chin in thought, a new idea coming to her."

je "{i}Or{/i} perhaps we could find a better use for these ancient materials. Who knows how useful they'll really be in battle?"
je "I'm sure there are plenty of buyers that would delight in having artifacts like these. They would be more than willing to compensate us."

"Rowan stayed silent as the siblings argued against each other for the armor's better use. Neither seemed willing to back down from their suggestion."
"Skordred sighed, settling his gaze on Rowan."

sk "And what are yer thoughts on the matter?"

menu:
    "Give the orc troops the armour.":
        $ released_fix_rollback()
        $ change_favor('andras', 1)
        $ change_morale(5)
        "As nice as gold was to have, it couldn't compare to the morale they would earn among their troops if they offered the artifacts with such meaning attached to them."
        ro "Let's split the armor among the troops. They'll be grateful for the favour."
        "The twins stopped their bickering at once, a satisfied look settling on Andras's face."
        an "HA! He's not as stupid as I thought. "
        show jezera displeased at midright with dissolve
        "Although Andras was pleased with the matter, Jezera was not. She made a face at Rowan, put out by his decision."
        je "Do you know how much someone would pay for even just a piece of this armor? We're missing out on a valuable opportunity."
        ro "We'll be repaid more than enough in loyalty. Some things are worth more than their weight in gold."
        je "Very well. If that is your decision, then I'll be returning to my room."
        "Jezera gave the men a skeptical look before leaving. Andras waved her off, unconcerned with her dismissive behaviour."
        an "Tch. She knows nothing of running an army."
        an "Clean this metal up and get them split up among the troops. I want them ready by tomorrow."
        "Skordred bowed his head."
        sk "Right away."
        "With the decision settled, Rowan returned to his desk."
        return
        
    "Sell the armour.":
        $ released_fix_rollback()
        $ change_favor('jezera', 1)
        $ change_treasury(50)
        "Although the Orcish troops would no doubt be delighted by the armour split among them, there were too many financial burdens to account for in the castle and the extra gold would be essential to the upkeep of both the castle and their army."
        ro "The armour is old enough as is, which makes me doubt its effectiveness on the battlefield. I would rather our troops be well-armed than inspired by flimsy metal."
        show andras displeased at edgeright with dissolve
        show jezera happy at midright with dissolve
        "The twins stopped their argument at once, but Rowan did not miss the scowl that darkened Andras's face. Jezera, on the other hand, seemed delighted."
        ro "We ought to sell the artifacts instead. The gold we get from this can buy us better armour and weapons which will be of more use to us than a few days of appreciation."
        je "An excellent point, Rowan. We wouldn't want to lose our best troops over some faulty armor, don't you agree, Andras?"
        "Her brother clearly did not agree, but fumed silently at her side, deciding not to throw in his two cents to the matter. With a huff, Andras made his way back to the barracks."
        "Jezera ignored him and beamed at Rowan instead."
        je "I'll contact some buyers that would be interested in these sorts of things. Why don't you get this cleaned up, Skordred, so they're fully polished upon purchase?" 
        "Skordred bowed his head."
        sk "I'll get right on that."
        "Jezera offered Rowan another smile, no doubt pleased with his decision, before returning to her room."
        return
        
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

label embezzlement_for_justice:

scene bg9 with fade
show rowan necklace neutral at midright with dissolve

"Breaks did not seem to exist in Bloodmeen Castle. Every time Rowan tried to bite into his afternoon meal, another messenger came barging in with information that certainly could have waited if they exhibited any ounce of patience."

show liurial neutral at midleft with dissolve

"By the time Liurial came wandering toward his desk, Rowan had only been fortunate enough to make it halfway through his sandwich."

show rowan necklace happy at midright with dissolve
    
"He worked to temper his annoyance with a polite smile."

ro "Hello, Liurial."
    
liur "Sorry to disturb you, but there's something important I found I think we need to discuss."

"The tone of her voice threw Rowan off. Something about the way she shifted, clutching the documents in her hands, nagged at Rowan's suspicion." 
"As much as he wanted to finish his meal, he had a feeling this could not wait."

ro "Alright, shoot. Is everything okay?"

"The elven maiden placed her documents on the desk for Rowan to see: expense reports. What could be so important about those?"

liur "I've been tracking the funding for a little while and I've noticed an irregularity in maintenance going toward the slave pits."

"Liurial's drew a line across the document with a thin finger, tracing just where the changes were made. "

liur "For some reason the funding towards them went up, and there's quite a bit of construction going toward the facilities."

show rowan necklace neutral at midright with dissolve

ro "(Shit.)"

"Rowan knew exactly why there was more funding going toward the slave pits, but that wasn't something he was about to give away to Liurial. Even if she proved to be reliable, they were in Bloodmeen after all. There was no telling where anyone's loyalties truly lay."
"Liurial's eyes met Rowan but he worked to keep his expression blank and neutral. It wouldn't do any good for her to see that he knew exactly what she was talking about."
"Rowan gently brushed the papers to edge of his desk, dismissing them."

ro "I'm sure it's nothing to worry about. I'll have a look at it sometime today."

"He worked to keep his voice casual and light, to dissuade Liurial from sticking her nose in places where it didn't belong."
"Liurial moved the papers back to the center of his desk and gave him a knowing look. She pulled another paper from the stack and placed it on top."

liur "I went looking into the old documents, Rowan. I can see right here where you forged the amount."

"She kept her voice low in case of wandering ears, her finger pressed beside one of the amounts that had clearly been tampered with."

ro "(Shit. Shit, {i}shit, shit{/i}.)"

"Rowan felt sweat brim at the back of his neck but he kept his expression composed. He hadn't expected anyone to go digging into old reports, especially {i}Liurial{/i} of all people." 
"Rowan was given the paperwork for a very good reason: no one else liked to do it. So why did she have to go tampering with things like this?!"

ro "Ah, you see…"

"There was no lying his way out of this. The look on Liurial's face already told Rowan that she knew everything. Even if he chose to deny it, Liurial had enough intelligence and proof that she could go running to the twins with everything."

ro "I think you already know what this means. I've been trying to improve the conditions in the slave pits without anyone knowing. Is that what you want to hear?"

"He couldn't bring himself to answer her kindly, not when she held so much information over his head. What would she do with it? Run to the twins? Blackmail him?"
"The look of surprise on her face told him that it was none of those things."

liur "I… I hadn't expected that."

"Recognition flashes across her face and Liurial quickly shakes her head, a flicker of worry glinting in her eyes."

liur "Please don't misunderstand me, Rowan. I didn't bring this up to expose you. I would never do something like that."

"Now Rowan felt confused. He stared up at her, lost."

ro "Then why bother telling me? Why bring it up at all?"

liur "Well, I was worried. I didn't want anyone else to find them, so I came to let you know that I doctored the documents successfully. No one should be questioning you from now on."

"To prove herself, Liurial slid a few more papers out from the pile and showed him. They looked almost like exact replicas of the old documents, except even Rowan couldn't tell where the forgery had been made. They were perfect."
"Liurial took the original documents and made her way to the fireplace, tossing them inside. The flames ate at the paper greedily, burning them to ash."

liur "Let me know the next time you need help with this. I'll take care of it for you."

"Rowan's chest swelled with warmth at her promise. So she wouldn't be turning him in after all."

show rowan necklace happy at midright with dissolve

ro "...I'll be sure to do that. Thank you."

"Liurial gave him a small smile and nodded before leaving him to finish his lunch."

$ change_treasury(-25)
$ change_base_stat('c', -3)
return
