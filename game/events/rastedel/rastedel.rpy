init python:
    
    event('rastedel_introduction', triggers=('map_res_106', 'map_res_107'), group='rastedel', priority=pr_map_res)
    
label rastedel_introduction:

if not goal2_completed:
    "Rowan stopped in his tracks and looked out into the distance. There, sitting on the river, was Rastedel in all of its glory. Stinking, noisy, Rastedel. He knew that heading that way would be dangerous. The arrival of the hero of the previous war in the capital could not be hidden."
    "What would Jezera think if she discovered him there without her knowledge?"
    "Better not to risk it. Rowan turned away."
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

else:
    pass

if rastLocked == True:
    $ push_to_previous_tile()
    return

elif verdoinCounter == 3:
    jump postVerdoin

elif postBattleVisit == True:
    jump rasPostBattleVisit

elif rastCurrentEnd == True:
    scene bg33 with fade
    "More content to come in the future. Stay tuned for the next build."
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

elif rastFirstVisit == False:
    jump rastMenu

else:
    pass

#######################################################################################################################

#First Visit

#rowan's arrival CG
scene cg394 with fade
show doran beardless neutral behind cg394
show rowan necklace neutral behind cg394
pause 3

"There it was. A gust of wind blew over the tall grass on the side of the road. Rowan parked his horse. Seeing this, Duke Reave pulled his to a stop as well. Rowan just wanted to look at it. He had not been back here in so many years."
"Down below them was Rastedel. The capital of Rosaria and home of the nobility. Rowan sighed. A place that held so many memories."
"The first thing he noticed as they approached was the sight of the Grand Codifice in the distance. Its eight towers are the tallest buildings in the city. There, the High Arbitron runs her bi-weekly sermons in the name of Solansia." 
"Now, from the hilltop, he could look at it in all of its glory. He could even see the movement of tiny figures up and down the boulevards. Rastedel was always alive. Always moving and squirming."
"The city itself was on the fork of a river. The north side was entirely taken up by the lower class districts. Endless pathways of bakeries, bars, and brothels. The river separated them from their more well to do brethren."
"The South East side was somewhat more upscale and was the center of industry. The merchant guilds, the granaries, the smiths, and the mining companies that dominated the east were all settled there. It was also where one went when looking for a doctor or other professional."
"And to the South West was the home of the nobles. The smallest part of the city, it was a collection of estates, servants homes, fine stores, and military facilities." 
"But, its most striking feature was the shining shimmering palace where the Baron lived. Its gardens were an unparalleled marvel in all of Rosaria, and its size and splendor was bested only by the Codifice on the other side of the river."
"In the last days of the war, especially after Bloodmeen had fallen, this place had been his home. There was still a fondness for it in his heart. Among other things."

dor "We must get on with it. It is expected of us."

"Rowan turned to the man. Duke Raeve was a hollow shell of his former self. Not only had Jezera taken his beard, but his pride. He now searched around any space he was in with a nervous expression. It was a good thing that so little was expected of him."

ro "Onward then."


scene bg33 with fade
show rowan necklace neutral at midleft with dissolve
show doran beardless neutral at edgeleft with dissolve

"At the gates, the soldiers didn’t even try to stop him. One of the guards moved to approach."

show rosarian knight neutral at midright with dissolve

rkn "Halt travelers. Where are you coming from?"

"The guard blinked twice, surprised at what he saw."

rkn "Rowan Blackwell? Goddess above. Let him through, let him through!"

hide rosarian knight with dissolve

"And just like that, the two riders were allowed entrance into the city."
"Rowan looked around and breathed in the scent. Where else was there like Rastedel?"
"The stink from the garbage and manure from the streets mixed with that of the fish from the river. The lines of buildings, entwined like lovers, stretching for miles. There was always someone on the street, always someone talking, always movement." 
"And the people. Louder and bolder than those of the villages by ten. Some dirt poor and reduced to rags. Other wearing whatever fashion had become common. It was a place built atop itself in so many layers that it had fused into a cohesive and distinct whole. "
"Smelly, massive, hopeful, flawed Rastedel."

cro "Rowan?"

"The guards were not the only ones who swiftly realized who the two newcomers were. A few people who had seen him in the parades of years before started to notice."

cro "Rowan’s here?"

"A murmur went down the street. Rowan rode with his back held high. He may have been accompanying a duke, but no one paid much attention at all to Doran. People pointed and chatted."
"Rowan rode down the long central boulevard. Every stretch saw the streets more and more filled. People opened second and third story windows to look down at him. Before long, the streets were mobbed by a crowd of people. They called out to him from all sides."
"It was like an impromptu celebration."

show rowan necklace happy at midleft with dissolve

"Rowan waved to the people. Being beloved had never been his goal, nor his addiction, but who wouldn’t feel a bit of energy when so many people showed so much affection for him."
"The people looked disturbingly similar to how he’d seen them last. That had been in the immediate aftermath of the war, when easy access to food was just being restored." 
"The hollowness of some of the cheeks he saw was a testament to the famine. Here too, it wreaked havoc in the form of higher bread prices. But, the people still looked in good spirits, and cheered earnestly at his approach."
"Doran bristled softly at all this attention, but didn’t protest as Rowan stopped to be greeted by several veterans. Rowan didn’t know them, of course, but they claimed to have fought by his side. A large matronly woman thrusted a small pastry into his hands."
"But, the ruckus was soon broken up by the arrival of five knights. In gleaming armor and strong horses, they immediately drew attention. But, Rowan’s eyes most lit up at the sight of the neat purple cloaks swept over their armour."
"They were of the Thorns of Solansia, the oldest and most exclusive knightly order in the entirety of Rosaria. The second sons and cousins of Dukes, Earls, and Counts had all pined for a spot in their ranks for generations."

show werden neutral at midright with dissolve

"And at the front of their ranks was a man a much older than the others, with armour a bit more ceremonial as well."

werd "Duke Reave. Rowan Blackwell."

show rowan necklace neutral at midleft with dissolve

"Rowan narrowed his eyes. He knew the man very well. He had commanded the Thorns during much of the last war. Duke Antoine Villele of Werden." 
"Rowan had fought at the side of this man’s brother at Karst. He’d actually fought with him too at Bloodmeen, but that didn’t mean there was much camaraderie between them. Duke Antoine didn’t share camaraderie with commoners."

ro "My lord..."

"The Duke and his entourage rode up to Rowan and Doran. Rowan controlled his emotions and kept a neutral expression. He remembered how frustrating the Duke could be to talk with. He didn’t suffer conversation."

werd "I had not expected you to appear, Lord Raeve. When your keep fell and no word came of your arrival, I assumed you lost."

"Doran clenched his teeth. Duke Antoine turned to Rowan. Rowan made sure to meet his gaze at equal level."

werd "I had not considered all the variables. Rosaria seemingly finds itself in the debt of Rowan Blackwell yet again."

"He put a hand to his chin."

werd "Hmmm."

"Suddenly the older man’s eyes brightened. He turned his steed around and gestured to be followed. The Thorns under his command spaced themselves out to push through the crowd."

werd "Follow. The Baron will need to speak with you immediately. Both of you."

"He was quite insistent on the matter. There was no room for debates. Rowan and Doran moved to follow. Still, Rowan was skeptical. Why was a Duke doing the dirty work of escorting them to the Palace?"

$ rastFirstVisit = False

jump rastMenu

#########################################################################################################################

label rasPostBattleVisit:

$ postBattleVisit = False

#Rowan comes to Rastedel Variant 2
scene cg395 with fade
pause 3

"There it was. A gust of wind blew over the tall grass on the side of the road. Rowan parked his horse. He just wanted to look at it. Despite having been back recently, Rowan was looking at a different Rastedel."
"It still stank. It still stretched out over the riverbed. The bearer of memories, and the home of disappointments."
"But, the city was quiet today. There was no subtle hints of movement down below in the city. There was not the usual clattering of activity. Even from a distance, the bustle of figures would still be visible from here. But, today nothing. Dead quiet."
"Well, at least it still stank. So there was that."
"Rowan spurred his horse onward. The city was waiting for him."

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve

"At the gates, Rowan wasn’t even checked. There were no troops in front of the gate stopping anyone from entering the city. A few guards patrolled the top of the walls though. They had dark circles under their eyes. Probably had been pulling multiple shifts back to back."
"They just let him through. He seemed human enough. Besides, the only people going through the gate was the odd person, here and there, who was leaving the city."
"The path he tread through the city was equally desolate. It wasn’t that there was no one on the street. It was just that there was no life. Everyone out had their head down and was just trying to get somewhere. No crowded boulevards and loud conversations."
"The windows and doors were all closed. A cloud of fear hung over the city."
"The last time he had come, people had thronged the streets to see him. The Hero of Karst in flesh and blood. This time no one came out to greet him." 
"It wasn’t that he was unnoticed. As he went, doors and windows creaked open. Eyes peeked out to see if it was really true. If he was really back. But, no one rushed out to greet him."
"He finally ran into someone with an interested in a longer conversation when he reached the main square. The silent spirals of the Grand Codifice hung like a phantom over the city below."

show rowan necklace happy at midleft with dissolve

ro "Well met, Inquisitors."

"A pair of blue clad guardsmen approached him on foot. Their bright blond hair gleaned in the sunlight. Inquisitorial Guards were Protheans. The direct defenders of the High Arbitron of whichever region they were assigned to. Naturally, they’d been left back from the fighting."

if avatar.corruption > 59:
    ro "Cunts."

inq "Good day, Rowan Blackwell. When Her Beatitude the High Arbitron heard of your arrival, she dispatched us at once. She would most kindly like to bestow a blessing of protection on you."

"Rowan scratched the top of his head. That seemed like a pretext to him."

#if deception high (TODO)
    #"Probably an excuse to get him alone in a room with her."

"He’d intended to visit Ameraine and the ever valiant Duke Raeve first upon arrival. Surely they were waiting for him. But, if Marianne was calling for him, it was probably best not to offend her by blowing her off."

ro "Of course. I will speak to her at the earliest convenience."

"The guards gestured for Rowan to follow them."


menu:
    
    "The Grand Codifice":
        $ released_fix_rollback()
        jump rastCodifice
    
###########################################################################################################################

label postVerdoin:
$ verdoinCounter = 4

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve

if rastAlly == "jacques":
    show jacques happy at edgeleft with dissolve
    "The procession made its way from the gate down the north side heading towards the central plaza and the Grand Codifice. The mercenaries had remained outside of the gates, but whatever landed knights and official soldiers had been part of the force joined them on parade."
    "Of course, Rowan had been placed in the center of the parade. Jacques had positioned himself at his side, with a bright smile and dramatic waves to either side. Hundreds lined the street along the entire procession to cheer."
    "They had been told this was the greatest victory in months. A hundred orcs dead in the process. To the average citizen of the city, there was now something between themselves and doom."
    "Rowan rode with a stoic expression and upright posture. Gloryhounding was for other men. Jacques waved dramatically and shook the hands of common men who approached them. He just wasn’t that kind of showman."
    if avatar.corruption > 30 and society_type == "feudalism":
        show rowan necklace angry at midleft with dissolve
        "He hid a dark sneer underneath his placid external features. Common folk were really so easy to fool. Had he once been like that? The idea seemed so foreign to him."
        show rowan necklace neutral at midleft with dissolve
    "Still, it was Rowan’s name on the lips of the people as they passed. Rowan the hero. Rowan the saviour. Rowan their greatest hope."
    "Likenesses were held aloft in his honor. Children raised mocked swords as though saluting a superior in the military."
    show liliana neutral at edgeright with dissolve
    "As they reached the center square, Rowan found something truly surprising. A great banner hung on the side of one of the buildings depicting him and some other armored men slaying orcs."
    "Near the banner, Liliana was busy directing the men setting it up. This entire parade had been her brain child."
    hide liliana with dissolve
    "Other festivities had been arranged throughout the square. Merchants and businessmen passed out sweets to children. Some of them probably hadn’t had a good meal in weeks."
    "The wealthy of the south-eastern merchant quarters had bankrolled an incredible celebration. A show of force."
    jacq "Marianne wants to make a speech. Naturally, we’re required up on the podium."
    "What do you say? Want to see the face she makes when she has to praise us? "
    if avatar.corruption > 30:
        "Rowan flashed a dark grin. Jacques had a point."
    else:
        "Rowan nodded somberly."
    "But, before they could make it all the way, Rowan and Jacques found themselves face to face with an unexpected well wisher."
    show werden neutral at edgeright with dissolve
    werd "..."
    "A dark smile crept on Jacques face."
    jacq "My lord."
    "He gave a short bow. Rowan couldn’t help but notice the way that even with his head lowered, the horse Jacques was riding still left him higher up then the Duke."
    jacq "You are a military man of great renown. It is a great honor to see you here today. I only hope the tactics that Rowan and I worked up meet your rigorous standards."
    jacq "After all, your victories were legendary..."
    jacq "...In their day."
    "Werden didn’t so much as honor Jacques with a reply. He was facing Rowan."
    werd "This is your role of choice, then?"
    "Rowan stared back intensely. His eyebrows furrowed."
    ro "It is, M’lord."
    werd "Hmmm."
    if werdenTalkFailed == False:
        werd "Disappointing."
    else:
        werd "Predictable."
    hide werden with dissolve
    "Rowan watched as the old man walked off into the crowd. Jacques seemed to be following his departure with an equal intensity."
    show jacques neutral at edgeleft with dissolve
    jacq "Bastard."
    show jacques happy at edgeleft with dissolve
    jacq "Shall we?"
    "The two made their way to the steps of the Codifice and dismounted. The crowd stopped at the edge of the staircase, leaving it as something like an impromptu stage. The Baron and the high arbitron waited at the top."
    #cas happy, mari annoyed
    show casimir neutral at midright with dissolve
    show marianne neutral at edgeright with dissolve
    "At the top of the stairs, Jacques went down on one knee and bowed his head. Rowan hastily followed along his lead."
    jacq "Baron, I would like to formally return the garrison of Verdoin Abbey to you. May this gift do honor to you."
    "The Baron gave a weak smile."
    casi "Rise. Rise. "
    casi "I...uh.."
    casi "I have so much to thank you for, and I don’t know where to begin. You are deserving of..yes...you are deserving of great honour."
    "He looked to Rowan."
    casi "And you, Rowan. You do so much. So so much. How do you find enough hours in the day?"
    ro "I can be a busy man at times, your highness."
    "Rowan and Jacques rose to their feet and walked down towards the crowd hand in hand with The Baron and High Arbitron Marianne. The crowd erupted in a cheer." 
    "As they descended, the High Arbiton leaned over and whispered into Rowan’s ear."
    mari "Do not worry, Child. I will pray for you. Solansia forgives those who do ill to her and her servants."
    "Rowan kept a straight face. Something told him that he’d done a little too much to be forgiven by this point."
    
    jump rastThePlan
    
else:
    show werden neutral at edgeleft with dissolve
    "The procession made its way from the gate down the north side heading towards the central plaza and the Grand Codifice. The Thorns made up the bulk of the parade because Werden’s Levies were not allowed into the city without official permission."
    "But, in their flowing purples and holding aloft colorful banners with their house surcoats, they still made a dramatic show. A stream of color moving like a river down the city boulevards."
    show rowan necklace neutral at midleft with dissolve
    "Of course, Rowan had been placed in the center of the parade. Werden rode at his side, stoic even in triumph. Somehow it was Rowan who was the approachable one. He tried his best to wave and greet the seemingly endless well wishers."
    "Hundreds had lined the streets to cheer. There was no love to the haughty nobles, but few could take issue with what this show demonstrated."
    "They had been told this was the greatest victory in months. A hundred orcs dead in the process. To the average citizen of the city, there was now something between themselves and doom."
    if avatar.corruption > 30 and society_type == "feudalism":
        show rowan necklace angry at midleft with dissolve
        "He hid a dark sneer underneath his placid external features. Common folk were really so easy to fool. Had he once been like that? The idea seemed so foreign to him."
        show rowan necklace neutral at midleft with dissolve
    "It was Rowan’s name on the lips of the people as they passed. Rowan the hero. Rowan the saviour. Rowan their greatest hope."
    "Likenesses were held aloft in his honor. Children raised mocked swords as though saluting a superior in the military."
    show patricia annoyed at edgeright with dissolve
    "As they reached the center square, Rowan found every building nearly covered in silk. 100 Banners hung in a ring, each depicting the sigil of a member of the Thorns. There was, naturally, one person behind this display." 
    "Patricia directed workers with dark shadows under her eyes. It was all well and good to put on a military parade, but it wasn’t like Werden was going to plan something so pedestrian."
    hide patricia with dissolve
    "Strange scenes played out all around him. Highborn knights in shining armor passed out loaves of bread to common folk. Some of whom probably hadn’t had a full meal in weeks." 
    "The entire affair was framed like a gift from on high. A show of force from the blue bloods that their power couldn’t be denied."
    werd "The most important step is to be seen with the Baron. The Baron and his lady should be at the entrance of the Codifice."
    "Rowan almost laughed. The Baron and “his lady”. Had Werden actually told a joke?"
    if jacqConvo == True or copperJacquesMet == True:
        "The idea was so absurd, he didn’t even pay special attention as a specific well wisher approached."
        show jacques happy at midright with dissolve
        jacq "Ah, Rowan. I suppose I must congratulate you on your victory. With the Abbey back in our hands, some of my friends can finally get their caravans moving north. The demand for swords is quite lucrative, I heard."
        "He leaned in close and nudged Rowan in the ribs."
        jacq "Still, don’t you think that this shindig is a bit much for so very few enemies killed?"
        "Rowan kept up a smile."
        ro "Does nothing happen without you catching wind of it?"
        jacq "No no, not at all. For instance, I have no idea what your actual plans are. I’d love to meet with you sometime and learn a little bit about your intentions."
        "Rowan sighed."
        ro "You know that isn’t going to happen at this point, Jacques."
        jacq "I suppose not, but it was worth a shot."
        jacq "For better or worse, all of our fates are in your hands, Rowan. You’ve got a lot of responsibility. I hope you use it wisely."
        "Rowan was left to chew on his words as he vanished into the crowds. "
        hide jacques with dissolve
    "The two made their way to the steps of the Codifice and dismounted. The crowd stopped at the edge of the staircase, leaving it as something like an improptu stage. The Baron and the high arbitron waited at the top."
    #cas happy, mari annoyed
    show casimir neutral at midright with dissolve
    show marianne neutral at edgeright with dissolve
    "Werden gracefully went down to one knee. All of the manners and rituals of power were second nature to him. Rowan hastily followed along his lead."
    werd "My Lord."
    "The Baron gave a weak smile."
    casi "Rise. Rise. "
    casi "How many times have we done this? Rowan Blackwell and Duke Werden coming with victories. It’s like...I’m a younger man..."
    "He looked to Rowan."
    casi "And you, Rowan. You do so much. So so much. How do you find enough hours in the day?"
    ro "I can be a busy man at times, your highness."
    "Rowan and Duke Werden rose to their feet and walked down towards the crowd hand in hand with The Baron and High Arbitron Marianne. The crowd erupted in a cheer. "
    "As they descended, the High Arbiton leaned over and whispered into Rowan’s ear."
    mari "Do not worry, Child. I will pray for you. Solansia forgives those who do ill to her."
    "Rowan kept a straight face. In his case, he rather doubted it…"
    
    jump rastThePlan


label rastThePlan:

scene bg42 with fade
show rowan necklace neutral at midleft with dissolve

"It was late when Rowan finally made his way back through the city to the tavern he was staying at."

if rastAlly != "jacques":
    "There was still a hint of alcohol on his lips."
 
"The room itself appeared empty when Rowan first arrived. Strange, since Ameraine had insisted on shaking him down for what he learned after the meeting."

show ameraine neutral at midright with dissolve

"But, there was something out of the ordinary. One of the windows was open. Rowan approached it slowly and found the woman he was looking for sitting on the ledge, legs dangling out above the city."
"His eyes caught on a detail in particular. Her long black sleeve was visibly torn. Beneath it, though hard to make out, Rowan caught the glimmer of a long gash."
 
ro "You're hurt." 

"She turned back to him slowly, emerging from the window. She stared down at her arm impassively, barely reacting to the news."
"Then she let out a soft tsk and clutched at it."

ro "What were you doing?"

"Ameraine chuckled to herself."

amer "Picking flowers."
amer "You should know by now, my business is my own. Jezera trusts me, and that's all there is to it."

ro "..."
ro "Of course..."

"Ameraine circled around towards the desk, running a hand through her long dark hair. Rowan sat down in the chair."

if rastAlly == "werden":
    amer "So, do we have the details? Did Werden let you into the inner circle? I’ve been waiting for you."
    
else:
    amer "So, do we have the details? Did Jacques let you into the inner circle? I’ve been waiting for you."

"Instead of answering, he took a quill and set of parchment and began to sketch. It was everything he could remember from the meeting. Not every detail was there, but enough to get the general point across. A map of the battle to come."

amer "Excellent. I've been getting allies adjacent for so long. The presence of a plan is obvious, probably even to Marianne as well. But the details? Now, that is a rare treat."

if rastAlly == "werden":
    ro "Werden isn't a pushover. He doesn't trust just anyone."

else:
    ro "Jacques isn't a pushover. He doesn't trust just anyone."
    
if rastAlly == "crevette":
    ro "He doesn't even trust me."
    
"Rowan talked in detail about what he'd learned. The movement of forces, the positioning of allies. Times and dates..."

amer "A lightning strike at the palace to get the Baron and his blushing companion, and then to move fast to take control of the important places in the city. Is that right?"

ro "Essentially, yes."

"She sighed and slithered over to his bed. Rowan kept his eyes on the parchment, while Ameraine languished on the cushions."

amer "Military strategy has never been my area of expertise, I fear. Some studies when I was younger, but your expertise is needed."

"Rowan put a hand to his chin. In truth, internal conflict had never been much his base of knowledge either. He'd always been more focused on battlefields and fortifications. But, he'd been in enough conflict to have a base idea."

ro "A fight like this isn't a battle. You need to move hard and fast because the enemy actually has overwhelming power. It's a problem of division of forces. If they can unify, it will be too late. "
ro "The simplest way to stop the coup from working is just to buy Marianne time to defend herself. Tip her off danger is coming or rescue her. So long as she can still organize, the snake has a head and her forces will be able to unify."

"He paused again to chew on his words further. "

ro "But, that won't work either. At least I don't think so. Our goal isn't to stop the coup. If we just keep Marianne free, she could possibly crush it too easily and still be able to defend the city."
 
if rastAlly == "werden":
    ro "Maybe... the Purples?"
    ro "No. I'd never be able to balance the scales. I could just as easily be handing the city too easily over to Werden instead."

    
else:
    ro "Maybe... the Coppers?"
    ro "No. I'd never be able to balance the scales. I could just as easily be handing the city too easily over to Jacques instead."

"Ameraine yawned softly to herself. A little bit of moonlight filtered into the room. It was silver on Ameraine's skin, just like the night they'd first met."

amer "It seems to me like the best situation if we wished to have some fun would be no one wins. Chaos and bloodshed in the streets and no one in charge."

ro "Something like that. Yes."

"Rowan's eyes scanned the map city over and over again. None of his ideas seemed strong. Simply barging in during the coup would be enough. Something more needed to be done. Another weakness exploited."
"But, what? What was he missing?"

ro "..."
ro "What about the North Side?"

"Ameraine raised an eyebrow."

amer "The peasants quarters?"

ro "Yes. There is to be an effort to take out the bridges, the grand square, and a few garrison points. "
ro "But there are almost no operations planned on that side. There will be a period of time when the segment of the city will be almost entirely unguarded, in between the start of the coup and the settling of the city."

amer "So you want to add a spot of havoc to the mix?"

ro "I wouldn't go that far. There only needs to be a small disturbance. A mob or two. Just enough to pin down whatever guards in the northern quarter aren't swept up in the coup. With a little bit of action from the peasants, the entire area's defenses may be out of action."
ro "Then it's as simple as using the chaos to burn down the gate. Fatally compromise the city's defenses. We know the day of the coup. Simply have the army arrive the following morning when everyone is worn out. Only, with no gate to keep them out of the city. "

"Ameraine chewed on one of her long fingernails. But, there was something unsettling about the way that she was deliberating. Her eyes never left Rowan's."

amer "Why a small mob? Surely the more chaos, the better?"

ro "To take the city? Maybe. But, doing it my way results in the lowest loss of life."

"Rowan coughed."

ro "That means the lowest loss of productive capacity."


amer "Does it now? Shall I put a letter to your Mistress and see if she agrees?"

if avatar.corruption > 60:
    ro "Must my motive be questioned every time? Yes. Burning down the entire city is dumb strategy. Prudence demands we keep our aims limited."
    amer "If you insist."
    "Ameraine didn't appear especially convinced, but at least was suitably chastened to stop talking about it. That was fine. She could believe whatever she wanted."
    
else:
    "Rowan remained silent on that front."

ro "Okay, so that turns the question to the riot itself. How can we set it in motion?"

show ameraine happy at midright with dissolve

"The woman giggled softly at that."

amer "That's a strange thing to hear from the mouth of the most popular man among the lower classes of the city."

"Rowan shook his head emphatically. It always came down to “You're Rowan!”"

ro "I can't be seen creating a disturbance like that. I can hardly remain in a position where I can influence our supposed ally if I'm openly agitating a riot on the day of the plan."

show ameraine neutral at midright with dissolve

"Ameraine sighed and leaned back on the bed. She didn't look at Rowan as she answered."

amer "Then get someone else to do it."
amer "There are figures in positions of influence who'd be perfectly happy to take you into their confidence. You're Rowan."

ro "That could work…"

"She put a single nail down on the makeshift map. It was positioned right where the slums are."

amer "The area is largely controlled by The Northside Bannermen. An ironic name for bands of smugglers. But, they claim nominal obedience to the Baron in return for some limited toleration. That makes them a tough nut to crack, but I have some friends among them."
amer "One of them, Madame Montiel, is a good friend of mine. From what she’s told me, there’s a leader up there that goes by Maud. "

ro "Maud? Who is she?"

amer "Well, that I can’t speak to her motives. But she and her men have been creating quite a stir."
amer "The new captain of the guard has been running around like a headless...chicken trying to deal with them. Alain Alarie. Such a sweet boy. But, that’s what happens when all the higher ranking guards die. He has a base of operations in the barracks."
amer "Either of them would make a suitable ally. You should seek them out."
amer "I’ve also heard some rumblings out of the church."

ro "The church? One would think they-"

amer "Not the Protheans, of course. You think any of them would say a word against The High Arbitron. But, the native priests? The Rosarians?"
amer "You should ask around among them. There may be potential friends in their ranks. The common masses trust their religious leaders. But, not the foreigners. The local church leaders have the power to incite the peasants to action."
amer "I want you to seek out native Rosarian leaders in the church. Someone with a good deal of discontent. They can help us raise the heat in the kettle."

show ameraine happy at midright with dissolve
show rowan necklace concerned at midleft with dissolve

"The woman leaned forward, placing her arms on Rowan’s shoulders and leaving an uncomfortably small amount of distance between them."

amer "And remember, if you are discreet at all, no one will think twice about it. Your ability to spread your influence with the peasants is half of why you're valuable."
amer "You have a few weeks right, Rowan? Just have all your friends in place by then."

if rastAlly == "crevette":
    amer "Naturally, we need Patricia under our thrall by that point as well. You will need to continue working our influence on her."
    "Ameraine whispered it in in his ear in a dark tone. Her voice nearly hissed at the word thrall. Rowan suspected the idea of corrupting a woman this way was not such a novel concept to Ameraine."

elif rastAlly == "jacques":
    amer "Of course, we still need to deal with Duke Werden as well. You need to focus on someone who might be able to give you an opening on him. If he is left free to act, he might screw up the entire plan."
    ro "Of course. Perhaps someone at the lodge…"
    "They'd need to have a good grasp of the layout of the Lodge and the schedules as well. It seemed if Rowan wanted a plan for handling Rowan he'd need to go back to that place."
    if delane_status == "free":
        "Lady Delane, perhaps…? "

amer "Provided you have that, then the rest of the plan should be simple enough to execute."

"Rowan nodded slowly. It was all coming together now."

ro "A few weeks..."

amer "Indeed. Think you'll have all the pieces in place by then?"

ro "It should not be a problem."

"Ameraine giggled softly and backed away."

show ameraine neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve

amer "It's a date, then."

"Rowan stood up from his chair and walked over to the window. Part of the city was visible in the moonlight, but remained shrouded in darkness. But, the last few stragglers from the taverns were still making their way to their sons and daughters through the streets below. "
"Even at night, Rastedel never truly came to a stop."

hide ameraine with dissolve

"Rowan didn't even have to look back to know that Ameraine had left. A slight breeze and swish of lace was all it took. Rowan was alone."

"The city is now more free for Rowan to explore. Just make sure that you've established allies in the city before the coup starts. Note: This segment is not currently complete. The Coup will not activate until a later release."

if rastAlly == "werden" or rastAlly == "crevette":
    $ werdenCoup = True
    
else:
    $ jacquesCoup = True

$ rastActFour = True

$ rastBarracksAccess = True
$ rastLodgeAccess = True
$ rastCopperAccess = True
$ rastAlleysAccess = True

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return


##########################################################################################################################
#Town Menu

label rastMenu:

scene bg33 with fade

menu:
    
    "The Palace.":
        $ released_fix_rollback()
        jump rastPalace
        
    "The Noble Lodge" if rastLodgeAccess == True:
        $ released_fix_rollback()
        jump rastLodge
    
    "The Northside Alleys" if rastAlleysAccess == True and maudAllied == False:
        $ released_fix_rollback()
        jump rastAlleys
    
    "The Grand Codifice" if rastCodificeAccess == True:
        $ released_fix_rollback()
        jump rastCodifice
    
    "The Trade Guild." if rastGuildAccess == True:
        $ released_fix_rollback()
        jump rastGuild
        
    "The Copper Club." if rastCopperAccess == True:
        $ released_fix_rollback()
        jump rastCopper
    
    "The Barracks" if rastBarracksAccess == True:
        $ released_fix_rollback()
        jump rastBarracks
        
    "Rowan's Room at the Inn" if rastActThree == True and rastForkingPaths == False and (copperJacquesMet or lodgeFirstMeetings):
        $ released_fix_rollback()
        jump rastInn
        
    "Capture Verdoin Abbey." if verdoinCounter == 2:
        $ released_fix_rollback()
        jump verdoinAbbeyCapture
        
    "Finish corrupting Patricia." if rastActFour == True and patriciaCorrupted == False and guessWhoSeen == True:
        $ released_fix_rollback()
        jump fall_of_crevette
        
    "Begin the coup." if northsideAlly != "none" or maudAllied == True and (julietKey or patriciaCorrupted or delaneAlly):
        $ released_fix_rollback()
        jump twilight_hour

    "Exit to North Gate":
        $ world.cur_map.pos_id = 272
        return

    "Exit to South Gate":
        $ world.cur_map.pos_id = 352
        return
    
    #"Back to map." if palaceStage !=1:
    #    $ released_fix_rollback()
    #    $ prevent_tile_exploration()
    #    $ push_to_previous_tile()
    #    return
