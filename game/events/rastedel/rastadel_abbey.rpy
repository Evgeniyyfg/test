



label verdoinAbbeyCapture:


if verdoinCounter == 0:
    scene bg31 with fade
    "Rowan kept his distance from the large abbey that overlooked the road pass. Even from a distance he could see the royal banners flying outside. This was a royal garrison."
    "He made note it on his map and continued on. Rowan scratched his head. What base was this? Regardless, it was smart not to contest such a well defended position if he didn’t have to."
    $ verdoinFirstVisit = False
    $ released_fix_rollback()
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return
    
elif verdoinCounter == 1:
    scene bg31 with fade
    "Rowan approached the large abbey overlooking the nearby road. From it’s strategic position it controlled the entire stretch of open land. He couldn’t help but notice that torn Rosarian banners cut up and hanging from the building. This had been a royal garrison once."
    if verdoinFirstVisit == False:
        "Rowan raised an eyebrow. When last he’d been here those banners had been pristine. It didn’t seem the new occupants were too friendly to the duke."
    "Whatever the cause was, Rowan was not going to discover it any time soon. As he approached the building, an arrow shot out from the ramparts and struck the ground not far from him. It seemed he was an unwelcome visitor."
    "Best to leave whoever the new occupants were to themselves."
    $ released_fix_rollback()
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return
    
else:
    pass

  
scene bg38 with fade
show rowan necklace concerned at midleft with dissolve

"Rowan brought his horse to a halt near the beginning of the winding path up to Verdoin Abbey. He was alone. He’d done a check-in with the troops he’d been sent to rendezvous with. The plan was actually to storm the fortress the following day."
"Which is why he had to skulk around in the night."

quest "Finally, finally. Ya make lil ol me do all da work and den finally show ya face dis late in da da’k."

"Rowan dismounted and looked to the person who’d come to greet him."

#tarish annoyed
show tarish neutral at midright with dissolve

ro "Good evening, Lady Tarish. I trust that the mission has gone well so far?"

"Tarish had her arms crossed, but her expression was hard to make out with what little light was available to him."

tar "Yes ‘n no"
tar "When dealin’ wit hostile chiefs is a gamble no matta what. Some ‘o ‘em want heads. Some want golds. Some don’t want none of what you sellin."

if tarishBetrayed:
    #tarish angry
    "Tarish took a step closer to him. Now her expression was easier to make out. Cold disdain."
    tar "Maybe, I shoulda let ya come up wit out no talkin. See how long before ya guts be boiled. Hehe."
    "Rowan sighed. The fact that hadn’t happened meant that she was just messing with him. They might not like each other, but shared utility made for unusual compromises."
    
show rowan necklace neutral at midleft with dissolve

ro  "What about the chief of the tribe here? What does he want?"

"The orcs who’d taken the abbey were not from those pledged to the twins, but that had not been the end of discussion. Naturally, Tarish was the diplomat best suited to speak to them. She’d been sent as soon as Rowan had gotten word back to the castle."
"Together, they walked up the winding road to the abbey. It stood, clearly visible, above the wide dirt road that acted as one of the main arteries of Rosarian trade."

tar "Lotto things. Me for starts. Been tryin to get on me good side. No luck for ‘im do. I been tryin to talk him inta a deal, but only managed ta get part of da way. Dis is a good spot here, no orc gonna give dat up without sumtin good."
tar  "Do we really need ta move him all dat bad?"

if tarishBetrayed:
    tar "Ya just want da glory of handin dis place over. Don’t think I don’t know, hummie. Don’t think I don’t."
    "Rowan shook his head. Tarish could believe what she wanted to."

elif avatar.corruption < 30:
    show rowan necklace concerned at midleft with dissolve 
    ro "..."
    show rowan necklace neutral at midleft with dissolve
    
else:
    ro "Yes. This position is very valuable to us too. I need it."

"They stopped outside the door of the abbey. On the rampart, he saw a big grey orc holding a bow twice as large as any he’d seen a human use. The strength to wield it must have been intense." 
"With archers like that and a good high ground, they could control vast tracts of land. Many men would die trying to dislodge them."

tar "I done all my part now. Talked ‘is damn ear off. Ya think it easy to getta damn hummie in da door?"
tar "Even did da dirty work bringing da gift up."

ro "Gift?"

"Rowan raised an eyebrow. He hadn’t mentioned anything to Jezera about a gift. That sounded like an improvisation on the part of the twins."

#tarish smirk
tar "A real tasty snack. No warchief gonna say nah to it. "
tar "Captives. Pretty little things for da raiders."
tar "If ya got da stomach for it, we can stop before meetin da chief for a look see."

menu:
    "Take the detour.":
        $ released_fix_rollback()
        jump verdoinDetour
        
    "No need.":
        $ released_fix_rollback()
        if avatar.corruption < 30:
            show rowan necklace angry at midleft with dissolve
            ro "I think I can guess what’s going on. I don’t think I need to see that at the moment."
        else:
            ro "No need. I have every confidence that the orcs enjoyed the gift. Andras’ idea I assume. "
        #tarish neutral
        "Tarish shrugged."
        tar "Suit ya self"
        jump verdoinMeeting


label verdoinDetour:

"Rowan scratched his chin. If this was an important part of the diplomacy effort, then it would probably be wise to see what had been given."

ro "Lead the way, my lady."

"Tarish formed a slight smirk that exposed one of her small tusks."

tar "Wanted a peak, eh hummie? Well okay den. After me."

#abbey BG
scene bg47 with fade

"The building was an old construction. It had just been a nunnery in the early days of Rosaria. Isolated from the capital or major cities, they’d built their own extensive defensive works. In time those had come to dominate the building’s role."
"But, buried into the mountain, the original monastic cells remained. Though they had been refurbished with locks and restraints to act as more of a dungeon."
"Rowan studied the walls as he went deeper and deeper into the abbey’s underbelly. Moans were rising up from the staircase. They grew more overpowering, along with the scent of sex the further down he and Tarish went."

#cg1
scene cg476 with fade
show rowan necklace neutral behind cg476
show tarish neutral behind cg476
pause 3 

"The building was an old construction. It had just been a nunnery in the early days of Rosaria. Isolated from the capital or major cities, they’d built their own extensive defensive works. In time those had come to dominate the building’s role."
"But, buried into the mountain, the original monastic cells remained. Though they had been refurbished with locks and restraints to act as more of a dungeon."
"Rowan studied the walls as he went deeper and deeper into the abbey’s underbelly. Moans were rising up from the staircase. They grew more overpowering, along with the scent of sex the further down he and Tarish went."

if avatar.corruption < 30:
    "Rowan found it hard to watch the scene in front of him. These had once been the daughters and wives of western Rosaria. Once they may have practiced dancing for festivals or had romances with the local boys."
    ro "..."
    
else:
    "Rowan honestly didn’t pay the proceedings much mind. This was hardly the first orcish gangbang he’d seen by this point. It probably would not be the last."
    ro "Hmmm."
    
ro "The sound is different from back at your camp. The captives your people held weren’t this willing?"

"Rowan craned his neck around." 
"The closer he looked, the more it was apparent that none of these women seemed to be dreading the degrading treatment they were getting. Even held by iron leashes, they still moaned and moved like willing participants."

tar "Ya, is why it we gave ‘em some ‘o yours. Orc men be stupid. The just fuck and fuck. So da hummie captives get all worn out real fastlike."
tar "But, ya have dem sex demons up at the keep. Makes ‘em nice and randy. Andras said he picked ‘em because they all liked it with the orc troops."
tar "Here, let me show ya."

#cg2
scene cg529 with fade
show rowan necklace neutral behind cg529
show tarish neutral behind cg529
pause 3

"She strode up to one of the slaves who wasn’t in use, a petite blond, and gripped her by the chin so she’d be forced to look up. She was a ragged thing with cum caked on her chest and the edges of her lips."
"Rowan walked forward to join them. His eyes met with slavegirl."

tar "You’re a good girl, ain’t ya? Wanna tell da hummie here what your favorite hole is?"

"The girl has no hesitation."

slave "Anal. Butt. Please. It’s my favorite. I love it."

"Now Rowan noticed that there was also traces of cum on the back of her leg. If that was her favorite hole, certainly it was getting plenty of attention."

tar "What ya think of orc cock? Ya like it?"

"The slave girl nodded fast."

slave "Please. More."

tar "Ya sound like a real slut, ya know dat?"

"The slave girl nodded again."

slave "A total slut. Please. I want more. My pussy hasn’t been fucked yet today. I wanna cummm."

"Tarish paused for a second, trying to form the words to what she wanted to ask next. Rowan could tell she was enjoying this. Her face dripped with sadism."

tar "Ya mouth been fucked recently?"

"The girl nodded fast."

tar "Wanna give us a good look? Say ahh."

scene cg530 with fade
show rowan necklace neutral behind cg530
show tarish neutral behind cg530
pause 3

"It was no lie. There was still pools of creamy white liquid in her mouth. She opened her mouth as wide as possible to give as good a look at the frothy liquid as possible."
"Tarish smirked."

tar "Your boys know how to pick ‘em."

"She drew her hand back from the slave girl, sending her sputtering to the ground. But, she barely even seemed to register the abuse."

tar "Needa see anymore?"

ro "I believe you’ve made your point. We should visit the chief."

"Rowan looked over his shoulder as they started to go back up the staircase. The slave girl was already back to waving her rear to a pair of orcs who’d just descended the staircase from the other side."
"She seemed happy. Perhaps."


label verdoinMeeting:

#abbey BG
scene bg47 with fade
show rowan necklace neutral at midleft with dissolve
show tarish neutral at edgeleft with dissolve
show wild orc neutral at midright with dissolve

"Rowan had been speaking to the chief of the tribe for some time before he decided that he rather liked him. Oh, he was still an orc. Violent, dismissive of humans, and totally lacking in manners. But, he listened to Rowan’s proposal earnestly."

wo "Big big want. Ya got a big big want."

"He reached down to a massive tankard filled with some of the watery beer he’d offered Rowan earlier."

wo "See, issa smart one. Coulda waita till ya show ya face den kill ya."

"He turned back to another orc in the corner."

wo "Who da hummie who dun walked in? Wha he say ‘is name was?"

orc2 "Sor Bancock, ya mighty."

wo "Heh. Cock."
wo "Ye, said he be wantin to talk terms. We say. Okay. So he come up da way. Den boom. Now I got me sum pretty pretty armor."
wo "So why I not be doin dat? Ya brought my hungry boys sum good pussy. Ya did. But me peepin dat belt ‘o yours. Nice sword. A pretty sword perhaps. "
wo "What ya say, hummie? Should I kill ya and take it?"

show rowan necklace happy at midleft with dissolve

"Rowan rolled his eyes. The orc chief was threatening him, but the big dumb grin on his face undermined the effect somewhat. This was a negotiating ploy."

ro "You probably could. Now, you might die in the process. You already know what friends I have."
ro "But, wouldn’t you rather hear about what you get if you accept my proposal?"

"The chief looked from Rowan to Tarish and then back."

tar "Ya already seen what we had to offer. You and all of ya boys get fed more when ya got us for friends."

wo "We done finally gettin to da good part. Da broad been teasing me along, but not given up da goods."

#tarish annoyed
"Tarish spat on the ground, eliciting a deep belly laugh from the chief."

wo "No good flirtin wit ‘er. Been tryin fo days. But, go on wit it before maggots get ta me."

"Rowan had spent the time leading up to meeting considering what the core of his offer would be. He felt he had a good answer."

show rowan necklace neutral at midleft with dissolve

"The tribe here was medium sized. A few dozen fighting men and women. The old fart acted dumb but he was quite shrewd. He’d noticed that the building was unoccupied shortly after Astarte and took it quickly."
"The easiest offer would be to evacuate the abbey in return for a portion of the spoils from Rastedel after it’s taken."  
"It offered the benefit of not requiring an immediate payment, but Rowan was naturally quite squeamish about any other party in the conquest who might push for a more hardline attack."
"The other option would be a more immediate offer. Fighting men or gold and treasure. It would have to come from Bloodmeen’s own war efforts. But, if it bought Rowan extra influence then it could be a worthwhile investment."

menu:
    "Pay with troops." if castle.buildings['barracks'].troops > 10:
        $ released_fix_rollback()
        $ castle.buildings['barracks'].troops -= 10
        "Rowan and sat out the payment structure he’d use to bribe the tribe. It would be painful. No general wanted to deplete their resources in return for a position that another occupied by good luck."
        "But, this was the simplest and cleanest method to ensure that the abbey fall into their hands."
        "The negotiations went on to the night with lots of drinking, mostly by the chief and his entourage, and a whole bunch of threats of violence."
        "But, an arrangement was struck long before dawn. The orcs quietly filed out of the abbey, to be replaced with a far smaller and weaker unit...weak and mortally wounded from the Bloodmeen allied tribes…"

        
    "Pay with gold." if castle.treasury > 100:
        $ released_fix_rollback()
        $ castle.treasury -= 100
        "Rowan and sat out the payment structure he’d use to bribe the tribe. It would be painful. No general wanted to deplete their resources in return for a position that another occupied by good luck."
        "But, this was the simplest and cleanest method to ensure that the abbey fall into their hands."
        "The negotiations went on to the night with lots of drinking, mostly by the chief and his entourage, and a whole bunch of threats of violence."
        "But, an arrangement was struck long before dawn. The orcs quietly filed out of the abbey, to be replaced with a far smaller and weaker unit...weak and mortally wounded from the Bloodmeen allied tribes…"
        
        
    "Pay with Rastedel’s wealth":
        $ released_fix_rollback()
        $ rastCrime += 1
        "Rowan’s face remained impassive as he detailed what the plan would consist of."
        "In lieu of up front payment, the chief and his tribe would instead join the force attacking the city in the upcoming assault, and keep a portion of the spoils from the south east merchant district."
        if avatar.corruption < 30:
            show rowan necklace concerned at midleft with dissolve
            "He had to stop at a few points to collect himself. It was hard to keep the words coming out of his mouth in context. He had to keep the mindset of a general."
            show rowan necklace neutral at midleft with dissolve
            $ change_base_stat('c', 3)
        "This line of persuasion wouldn’t have worked if he couldn’t point to the battle before. Tarish insisted that Rowan had come up with the plan for Astarte Plain himself. Of course, it would work."
        "The negotiations went on to the night with lots of drinking, mostly by the chief and his entourage, and a whole bunch of threats of violence."
        "But, an arrangement was struck long before dawn. The orcs quietly filed out of the abbey, to be replaced with a far smaller and weaker unit...weak and mortally wounded from the Bloodmeen allied tribes…"

#goblin recruit (TODO)

show bg31 with fade
show rowan necklace neutral at midleft with dissolve
#show different knights depending on alliance - TODO
show rosarian knight neutral at edgeleft with dissolve

"In the first morning light, hundreds of men came streaming down the road. Rowan was at their head. They moved from the south, the route with smaller exposure to enemy fire. Still, as they came roaring up the arrows started to fly."

if rastAlly == "jacques":
    "To Rowan’s side were a few men in steel, bust mostly troops in leather. A combination of levies from smaller estates, landed knights, and mercenaries. A ragtag army, but a large and powerful one nonetheless."
    
else:
    "To Rowan’s side were steel knights in purple surcoats and peasant soldiers fighting under the Duke’s banner. Together they made up the most powerful fighting force presently in the kingdom."

"In a lightning charge they made it to the walls of the abbey. Arrows struck here and there but casualties were light. Their aim was atrocious and supplies of arrows were low."
"The attackers came prepared with ladders rams. While a core of shielded men struck at the main door, the rest of the attackers went over the top. Rowan led them himself with no hesitation. His performance was flawless."

#abbey BG
scene black with fade

"The initial fighting on the rampart went swiftly. There were only five orcs to defend the position and they were swiftly swamped by the attackers numbers."
"Though, Rowan did get a chance to go one on one with one of the orcs. A  large, one armed fighter who’d been slinging stones from the battlements. "
"There was a flash of recognition as Rowan approached. But, he made a good show of it, swinging and charging like a creature possessed. Rowan cut him down easily."

show rowan necklace neutral at midleft with dissolve

ro "Fan out and find the remaining defenders. No survivors. Leave no survivors."

"Not that there were many that needed execution. Wherever they went, they found few orcs, mostly older fighters and those missing limbs."
"Standing over the body of a huge one-armed brute who’d been easily dispatched by ten fighters, one of the other commanders approached him."

#show different knights depending on alliance - TODO
show rosarian knight neutral at edgeleft with moveinleft

rkn "The right wing of the abbey has been totally secured. We found ten of ‘em, but we’d been preparing for fifty."

ro "I’ve noticed the same thing. There’s only a skeleton crew here."

"Rowan leaned close and whispered into the man’s ear."

#rowan smirk


if rastAlly == "jacques":
    ro "I think it will play better in the city without that bit of information. I’m sure your Boss would agree. "

else:
    ro "I think it will play better in the city without that bit of information. I’m sure the Duke would agree." 

"The commander nodded in agreement. Everyone would benefit from a more dramatic triumph."
"So it was that the humans had won their first great victory since the Battle of Astarte. And what a victory it was. Now all that was left was to return to the city and celebrate…"

$ verdoinCounter = 3

$ prevent_tile_exploration()
$ push_to_previous_tile()
return
return

