init python:
    event('trek_into_the_wild', triggers="week_end", depends=('delf_dipping',), group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg25")
    event('a_noble_fate', triggers="week_end", conditions=('week >=4', "castle.buildings['arena'].lvl >= 1",), group='ruler_event', run_count=1, priority=pr_ruler)
    event('showing_driders_whos_on_top', triggers="week_end", conditions=('week >= 4', 'castle.buildings["pit"].driders >= 2'), group='ruler_event', run_count=1, priority=pr_ruler)
    event('an_iconic_display', triggers="week_end", depends=('password_is_fidelio',),group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg24")
    event('succumbing_to_shaya', triggers="week_end", depends=('an_iconic_display',),group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg24")
    event('jezeraNTRDetox', triggers="week_end", conditions=('all_actors["alexia"].corruption > 30', 'week > 25', 'alexiaWhipRowan', 'AlexiaXzaratlInfluence > 9', 'rowan_shares_room_with_helayna == False', "get_actor_job('alexia')!='maid'",), group='ruler_event', run_count=1, priority=pr_ruler)

label trek_into_the_wild:

#tropical jungle bg
scene black with fade
show rowan necklace neutral at midright with moveinleft
show draith neutral at midleft with moveinleft

"Rowan stepped through the portal, Draith and camping equipment in tow. They were greeted with thick, humid air and the fresh scent of unearthed soil after a storm. Draith squinted against the lush greenery, unused to so much light and vibrancy."

ro "Thanks for coming. I'm not sure I'd be able to track down this beast on my own."

dra "Of course. If you’re doing this for my sake, I should come along too."

"Rowan unattached the machete from his waist and hacked away at the overgrowth in his path."

ro "You still haven't told me what we're using it for exactly. The Khut-- The Khustish--"

dra "The Khustistian."

ro "Right. That. Are you going to train it like the others?"

dra "Rowan, please, I have much bigger plans for the Khusti! Its natural-made armor is nearly impenetrable; if I can pair that with the… with the…"

"Draith trailed off. Odd. Usually he was eager to discuss his plans for the beasts at length, whether anyone was interested in hearing about it or not."
"Rowan glanced back as he maneuvered through the thick jungle, surprised to find the dark elf several feet behind. Draith seemed both fascinated and confused by his surroundings, constantly leaning down to inspect the leaves or examine a multi-legged insect up close."

ro "Draith?"

dra "Hm? Yes, just a moment."

"Draith procured a glass bottle from his bag and scooped the creature up, capturing it with a cork top."

ro "Careful, some of the stuff here could be poisonous."

dra "Yes, yes, I already know that. It's precisely what I'm hoping for…"

"Draith smiled at the little insect before placing the bottle back into his bag. Rowan wasn't sure he wanted to know what experiments Draith had planned for the little creature."
"He wasn't sure he wanted to know what Draith was going to do with the Khusti either."
"Rowan had planned, with Draith's assistance, to track down the beast within two days' time. Draith had reassured him it would be easy with the Khusti's telltale signs of nesting and travel."
"They did not get very far." 
"Every few paces, Draith seemed to find another creature he was eager to add to his collection." 
"After the second day, Rowan could hear the clinking of bottles in Draith's bag, followed by the irritated sound of hissing and wings flapping as his miniscule creatures desperately tried for an escape. There was still no sign of the Khusti."
"At this rate it would take them weeks to track the beast down."

ro "You know you don't have to take every creature we pass by, Draith."

"A rushing coursing stream broke up the monotonous greenery of the jungle. Rowan made his way across a stream with ease but Draith hesitated at the edge of the running water, his leg spread out to cross but never making that final leap."

dra "It's hard to resist; I may never come back here again. I need as many specimens as I can."

"He eyed the water suspiciously before leaping to the first stone. Draith waved his arms frantically at his sides, barely catching his balance in time. There were still three stones to go."

ro "What makes you think you'll never come back here?"

dra "I have a job to do; I can't leave the creatures for long."

"Draith hesitated. He looked around the jungle with such an awestruck longing that Rowan felt a slight tug at his heartstrings. He was used to travel-- heroic deeds required heroic settings, in his experience--but this was the beastmaster's first time ever setting foot on tropical land."

dra "I was lucky enough to come here once. I doubt I'll see it again."

ro "I'm sure we'll need more beasts in the future. It's not as if we're keeping you locked up in the pits, you know."

"Rowan regretted the words as soon as they'd left his mouth. While Draith kept up a light front, the dark elf gripped the straps of his bag a little tighter, his gaze finding interest in anything but Rowan."

dra "You're always welcome to start if you're feeling the temptation. There's plenty of rope, and I'll make any noise you want~"

"Draith smiled at Rowan, but he couldn't tell if the beastmaster meant what he said or if he was simply making light of the situation."
"Rowan elected to ignore the comment and made his way back across the stream, offering his hand out to the dark elf. Draith took the help at once, leaning into Rowan's touch as they leapt over the remaining stones and once again found dry land."
"They started forward, but Draith threw a hand out, halting Rowan in place."

dra "Wait!"

ro "What is it?"

"Draith didn't answer. He crept forward instead, focused on something Rowan couldn't see. He disappeared behind the trees."

ro "Draith?"

dra "Just a moment."

"Rowan waited. The dark elf returned a few moments later with a giddy look on his face."

ro "Did you find another bug for your collection?"

dra "Better than that; I believe I've found footprints."

"Draith waved Rowan forward, pointing out the small stumpy prints in the ground."

dra "They're smaller than I expected, but these are certainly the right prints."

"Draith rummaged through his bag and pulled out a green-covered book that looked like it'd seen better days; the pages were rumpled and worn, with ink marks and small, hurried notes in the columns. He flipped through the book's contents until he landed on a page titled {i}Khustistian{/i}."
"Rowan peered over the beastmaster's shoulder, taking in a drawing of the beast's footprint. It looked much larger than the one Draith was showing him on the ground."

#if low survival skill- TODO
    #ro "Are you sure that's the right footprint?"
    #dra "Well, it's not exactly the same, but you can't blame the artist for trying."
    #ro "They look recent--and there's more over here. Do they travel in a pack?"
    #dra "No. That is unusual… but perhaps there's a nest nearby."
    #ro "Great."
    #"From everything Draith had told Rowan about the Khusti so far, he felt confident in handling one of them, but any more would cause trouble."
    #ro "We'll keep going. If there's a nest ahead, we may need to rethink our strategy."
    #dra "Whatever for? We'll simply take them all back."
    
#else

ro "That doesn't look like one set of tracks, Draith. Look-- you can see the imprint of smaller ones beside it."
dra "That doesn't make sense; Khusti's are solitary creatures."
ro "Then either another animal crossed this path shortly after-- not entirely unlikely, but it would make more sense if they travelled together-- it's being hunted, or--"
dra "Or a nest!"
"Draith beamed at the prospect, and Rowan could see the wheels turning in the dark elf's head; masterful plans of experimentation that left even the bravest men feeling uneasy."
ro "Er, possibly…"
dra "This is better than I ever imagined! We could return home with an entire family of Khusti!"

#rejoin

"Rowan stared at him. Did he not realize how much trouble just one of these beasts was going to be to drag back on their own?" 
"No--there was an excited gleam in Draith's eyes, and Rowan realized the elf was solely focused on the possibility of experimenting on not just one deadly beast, but multiple."

ro "...Let's see if it's a nest first."

dra "Alright."

"To Rowan's relief, Draith seemed far more focused on their task now that there was a hint of the beast ahead. He hardly stopped to collect any other random creatures that were unfortunate enough to meet the elf's path."
"They travelled a little farther before the sun started to set. Despite their desire to get the beast and return home, the men were forced to call it a night and set up camp."

ro "Would you mind starting up the fire tonight? I'm going to take a leak and then hunt us some fish."

"Draith had usually handled the food up until this point, but their two days of rations were gone, and Rowan would be damned if he didn't get something to eat before he dealt with giant insects swarming around his head or deadly animals growling at him from behind bodice-sized leaves."

dra "Sure! It'll be easy."

"Rowan started toward the jungle but stopped. There was something nagging at him, a small voice that cut through his confidence in the dark elf."

ro "Have you ever lit a fire before?"

dra "I've read about it plenty of times, Rowan. I'm sure I can light a simple fire."

"Rowan shrugged, leaving the dark elf to his devices. Draith was well-versed enough in animals, he supposed the elf should be just as studied in their habitats as well."
"Rowan returned just after sundown with a couple of fish and some fallen fruit from the trees he'd collected off the ground. He was eager to settle down by the fire and fill the empty void in his stomach."
"The campsite, however, was shrouded in darkness. Draith grunted from somewhere on the ground, cursing under his breath."

ro "Where's the fire?"

"Draith jumped."

dra "J-Just a moment. Please wait, just a moment..."

"Rowan, his eyes already adjusted to the dark, watched Draith rub the sticks together furiously. The elf's face was pinched with growing agitation and anxiety as he redoubled his efforts."

ro "Where's the flint?"

"The sticks fell from his hands."

dra "The what?"

"Rowan walked past the beastmaster and, after setting his catch of the night down, dug through his own pack. He pulled out a small piece of flint and some flammable material."
"He gently nudged Draith out of the way and set up a proper fire. Draith held his breath at his side, eyes wide as Rowan explained the process. Flames sparked and the fire roared."

dra "Oh. I'm sorry, I'm sorry, I should have known about that..."

ro "It's alright, don't worry yourself about it."

"But he was. Draith kicked a stray stick into the fire dejectedly. The flames licked it up greedily, quick to turn the wood into ash."

ro "There are a few different ways, but this is the best method if you don't already have a source for flame. It's good to carry spare flint and tinder in case you don't find any where you're going."

dra "But we're surrounded by trees. Surely you could've taken some of these leaves or branches."

ro "True, but a lot of these plants are too wet. See? They wouldn't catch fire easily."

"Rowan ran a hand over one oversized leaf; a thick spray of dew clung to his hand."

dra "Oh. Yes, I suppose you're right."

"Even more disappointment. Draith avoided Rowan's gaze, his lips moving but his words too quiet for Rowan to hear. It didn't take a genius to figure out that Draith was blaming himself for the incident."

ro "Do you want to learn how to cook the fish?"

dra "...Sure."

"Rowan picked up the fish and taught Draith the procedures for cleaning and cooking them-- a far cry from the academic study the beastmaster was used to when it came to learning about animals. The elf relaxed as the lesson went on, the tension easing from his face and shoulders."
"Soon their stomachs were full and the fire was dimming. Draith chewed at the last remaining pieces of his fish with a thoughtful expression on his face."
"Rowan observed him from the corner of his eye."

ro "What are you thinking about?"

dra "I'm wondering how to use  some of the smaller creatures I've acquired. I never imagined I'd come across so many all at once; it's almost overwhelming. The possibilities are truly endless…"

ro "Hm."

dra "What?"

ro "Oh, nothing. I was just thinking… You have more knowledge about beasts than most men have about themselves. I don't think I could name half the creatures you captured in your bag, let alone what else is in this jungle."
ro "Do you have a favorite?"

dra "A favorite beast from the jungle?"

ro "Any beast from anywhere."

"Draith tapped his chin in thought."

dra "There's a lot that comes to mind… But I guess it would have to be the Pearl Solandis."

ro "I've never heard of that before."

dra "They're a type of mammalian creature that live in the tundra. Their white fur blends right into the snow, and they have a pearlescent eye color, so the only way to really see them is when their jaws are open and you can see their black teeth."
dra "They're not all that strong, but they're very fast. Pearl Solandises are very good at outrunning their prey, or outswimming them if need be. They're truly outstanding creatures."

"A blush colored Draith's cheeks. He looked away and poked the dying flames with his stick if only for something to do."

dra "Sorry, I must be boring you. I can cease talking now."

if avatar.corruption < 31:
    ro "You don't have to do that. I don't mind hearing about it."
    "Draith looked at him skeptically. He didn't look like he knew what to do with that information, choosing to wring his hands together instead."
    dra "It's alright. I know I can be a bit much sometimes."
    "He laughed awkwardly, but the tension in his body was clear."
    
else:
    ro "That would be preferred. You have a tendency to ramble."
    dra "Right… Sorry."
    "Draith smiled awkwardly before redirecting his attention back to the fire. Only a small flame sparked now, diminishing into embers."
    "There was something to Draith's movements that nagged at him, and despite himself, Rowan felt a little guilty for shutting him down."

ro "You're used to people telling you to be quiet."

"It wasn't a question. Rowan could see it in the dark elf's face; his presence was to be seen, not heard. At least, that must have been how it was in his former kingdom. Draith bit his lip." 
"Rowan knew Draith's experience in the dark kingdom left much to be desired, but Draith rarely-- if ever-- spoke the details of his abuse. It was there in the way he talked about his interests as if he couldn't get the words out fast enough, the way he flinched when something minor went wrong."
"Rowan had seen the same reactions in his own soldiers after battle, the haunted look in their eyes and the way they would laugh as if that could erase the horrors they'd seen. The horrors they'd endured."
"Draith was the same way; his cheeky grin didn't match the sadness in his eyes. But he smirked at Rowan anyway, dragging his gaze over the hero's body."

dra "They'd have to find ways to shut me up. Sometimes I was just so loud~"

"The elf slid closer to Rowan. Draith tilted his head back to look up at him, his long eyelashes casting shadows over his pale cheeks."

dra "Do you want to shut me up, too?"

menu:
    '"Shut up" Draith effectively.':
        $ released_fix_rollback()
        $ change_relation('draith', 5)
        "Rowan's gaze dropped to Draith's lips: soft, supple. He could feel the dark elf's breath against his, the heat of Draith's body intoxicating him. Pulling him closer."
        dra "Well? I-- Mmph!"
        "Rowan gripped the back of his head and yanked him forward, lips mashing against his. Draith's words melted into a satisfied moan, his slender arms finding their way around Rowan's neck."
        "Rowan dug his tongue into the elf's mouth, pulling the whimpers from Draith's throat. His hands fell to the elf's waist, then his hips, his ass, and back around again." 
        "He pulled away just as roughly, earning a dazed smile from the beastmaster."
        ro "You really don't know when to stop talking."
        dra "Heh. It's a gift."
        "Their lips found each other again. The men stumbled toward their tent-- a canvas pitched together to provide the bare minimum of protection from tropical storms-- and collapsed into a pile of limbs and violent kisses."
        "A lantern burned low in the corner of the tent, casting stark shadows across the men's bodies. Draith was all too eager to slip out of his clothes, exposing every inch of that indulgent flesh that left Rowan's mind addled and his cock hard."
        "Fuck, there was something delicious about the curve of Draith's slender waist and the round flesh of his pert ass that drove Rowan crazy."
        "Draith knew it, too; he arched his body toward the larger man, precum dripping from the tip of his stiff cock. Rowan was tempted to lick the juices right off."
        "The hero removed his own clothes instead, peeling the leather and fabric off until they were discarded throughout the tent. Draith's cock twitched, his gaze dropping from Rowan's wide muscles and onto the erection poking out in his direction."
        "Rowan pressed the beastmaster against the ground and hiked Draith's legs up against his chest. The elf bit back a smirk as his legs were forced apart and his asshole exposed."
        dra "This isn't convincing me to be quiet, Rowan."
        ro "Then it's a good thing no one can hear you."
        "Draith opened his mouth to make another remark, but the words were lost as Rowan drove himself fully into his ass. A strangled cry of pain and pleasure echoed through the jungle."
        "Rowan's cock dived in and out of the beastmaster. His hands wrapped around Draith's legs and held them tightly in place, digging into the elf's soft flesh as he admired the bounce of his pale cock with each violent thrust."
        "Precum dribbled from the tip, flying onto the elf's stomach every time Rowan pounded deeper into him. Draith tossed his head back, incoherent words slipping together until they came out as nothing but pleasured moans."
        "Draith's ass clenched. Rowan's breath grew heavy, and the sight of cum pouring from the elf's cock pushed him over the edge."
        "He slipped out of Draith's ass, barely giving himself enough time to blow his load across the elf's chest and belly. A low hum erupted from Draith's lips, utterly content."
        "Rowan took a moment to admire his work; Draith was covered, his body a strange canvas for their mixture of cum. The elf dragged a finger across the mess and pressed it between his lips, licking off the semen." 
        "Rowan's body gave a slight shudder, and if he wasn't so tired from their expedition across the jungle, he would have been tempted to fuck him again."
        ro "We should rest; there's still a lot of ground to cover tomorrow. I want to be ready to capture the Khusti and go home."
        "Draith reached for a spare cloth and wiped at his chest."
        dra "Of course. I don't think I could stay awake any longer if I tried."
        
    "Suggest you both go to bed.":
        $ released_fix_rollback()
        ro "We should rest; there's still a lot of ground to cover tomorrow. I want to be ready to capture the Khusti and go home."
        "Draith frowned, clearly disappointed with the direction Rowan had gone."
        dra "Yes, I suppose so."
        
"The men finished cleaning up the campsite and climbed into their cots, worn out from their trek thus far. It didn't take very long for them to succumb to their exhaustion."

"……"

"Draith seemed more energetic after the night's rest, his excitement to see the Khusti's nest obvious as he searched out clues and tracks with enthusiasm. Rowan quietly wished he'd had this focus when they first arrived; then perhaps it wouldn't have taken three days to track down."

dra "Ah, Typhon Berries!"

"The beastmaster ran towards a tropical bush covered in vibrant violet berries. Rowan had never seen food such an unnatural color, but then again, he didn't tend to go galavanting this deep in the jungle." 
"Draith plucked one of the berries from the bush and squeezed it between his thumb and forefinger; bizarrely enough, a green juice oozed out from it. The elf's excitement increased tenfold."

ro "What's so special about the berries?"

dra "They're a staple of an early Khustistian diet; these berries contain the nutrients their young need to develop their armor properly. A nest must be closeby."

"Rowan struggled to keep up with Draith as the elf wandered through the jungle, always three steps ahead and constantly disappearing behind the thick leaves. It was a far cry from their earlier journey; perhaps Draith had lost interest in collecting the smaller creatures now that he was so close to his goal."
"Draith reached the nest first and held up a hand for Rowan to slow his steps and remain quiet. They peered through a break in the trees."

dra "An infant; isn't it beautiful?"

"Beautiful wasn't the word Rowan would use to describe the creature. The baby Khustistian had a small beak and large, oversized eyes that were halfway covered by patches of rough natural armor, and thick limbs that looked too big for its tiny body. It was perhaps one of the strangest creatures Rowan had ever seen."
"But Draith stared at the baby Khusti with all of the love and admiration of a parent overseeing their newborn. The elf glanced around, his expression falling at once with a soft gasp."
"A few feet away, a fallen tree had crushed the head of the mother, stopping her just short of protecting her baby. While the armor around the Khusti's face and body may be impenetrable, their exposed neck wasn't. "

ro "It must have happened before we got here; the tree looks like it was struck by lightning."

"Draith frowned at the burnt tree, then at the mother, and finally at the Khusti baby. They'd been lucky enough to avoid any rainstorms since they arrived, but it seemed they had been even luckier to avoid a real storm."

dra "Well, this will have to do."

"Draith stepped over the overgrowth and approached the hissing baby. It snapped its beak at Draith, but the elf was undeterred, easily picking it up like a disgruntled toddler."

dra "Now, now, there's no reason to be so feisty. I'm not going to hurt you."

ro "Is a baby going to work? I thought we came here so you could experiment on an adult."

dra "It should be fine, we'll still take the mother back. It may even have worked out better with her dying; there's less risk when one of the subjects can't feel pain."

"The baby Khusti wriggled in his arms, its limbs frantically swiping the air as if it could escape on its own. The sight was almost cute."

dra "As for this little one, it won't be able to survive in the wild. I'll just need to raise it myself, won't I?"

"Draith smiled down at the feisty infant. It gave him the stink eye in return, and Rowan nearly laughed."

dra "We should take one of those berry plants back with us as well; we'll need plenty if we want the baby to grow up big and strong."

ro "I'll have someone get on that."

"There was no way they'd be able to haul all of this by themselves, so Rowan would have to send some orcs to bring the adult Khusti and the berry plants back."
"Draith seemed satisfied with the plan, and they both began their trek back to the portal, one ill-spirited baby in tow. Draith reassured him that the baby would relax and grow used to being handled by them once it had some time to adjust; Rowan hoped the elf was right."

return

########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################

label a_noble_fate:
    
scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan found himself in the throne room in the early dawn, just an hour before the sun would break out over the horizon. He rubbed the sleep from his eyes, the air miserably chilly compared to the warmth of his bed."

ro "You called, Jezera?"

"He didn't hide the annoyance in his tone; her voice had loudly woken him up through the sapphire necklace just minutes before, insisting that he was to make his way to the throne room immediately."

show jezera happy at midright with dissolve
 
"Jezera smiled at him from atop her throne, well aware of the disturbance she caused him. Andras sat at her side, arms crossed and annoyed."

je "Yes; I've recently acquired a little treasure that I simply can't decide what to do with. Perhaps you'll be of some advice."

"A treasure? Rowan scowled. Couldn't this have waited until the morning?"
"He watched Jezera flick her wrist, and two orc guards dragged out her so-called treasure."
"It was a man-- a slave from the looks of it-- with broad muscles and dark hair that was bleached lighter by the sun. His hands were bound by iron shackles, and even with his strong figure, the orcs easily brought him down to his knees with a swift kick behind his calves."

je "Rowan, meet Dasius-- a runaway slave from Qerazel."

"Rowan took Dasius in, recognizing the bronze armor and symbols carved into it: one marking him as a slave,  another signifying which house he belonged to. {i}He's a gladiator{/i}."

je "It appears the poor thing wants to disappear. I say we give him the opportunity, don't you?"
je "But how should we do it, hmm? So many options… Personally, I like the idea of placing him in the brothel. He would make a most excellent little whore, don't you think?"

das "I am not some sex puppet for you to tote around!"

"Although the only outburst were his words, the orcs yanked on his chains, earning a small hiss of pain from the slave."

je "Not with that attitude."
je "Be careful, little slave. You do know who is deciding your fate, don't you?"

"Dasius turned to Rowan, recognition and dread crossing his features."

das "I was there at Deadman's Pass when he stormed it--"

show andras displeased at edgeright with dissolve

"Andras slammed his fist against his chair's arm, drawing their attention."

an "The man is a {i}gladiator{/i}; he was born to fight!"
an "I say we let him fight {i}to the death{/i}." 

show andras smirk at edgeright with dissolve

"Andras flashed a sharp, sadistic smile in Dasius's direction. The gladiator glared but didn't object."

if avatar.corruption < 61:
    "Rowan shifted uncomfortably in his place."
    ro "Surely there is something more useful we can do with him. Add him to the army, perhaps?"
    an "Shove off, worm. You hand him a sword and strip his chains and he’d probably try to slice your throat in your sleep. Gladiator or Bedwarmer. You’re not getting out of picking this time."
    je "He’s quite right, dear. One or the other."
    "Rowan sighed."
    
menu:
    "Make him a manwhore for the brothel.":
        $ released_fix_rollback()
        $ change_prisoners(1)
        $ change_favor('jezera', 1)
        "There was always a shortage of male whores among the brothel, and Dasius had the kind of physique that fit the role perfectly."
        if avatar.corruption > 30:
            "He would no doubt bring in plenty of money for Bloodmeen at the expense of a few thrusts."
        ro "I say we put him in the brothel."
        an "Tch.Boring."
        je "I knew you would see reason, Rowan. We'll have him prepared right away."
        "The demon flicked her wrist again, dismissing the orcs and their prisoner. Rowan didn't miss the harsh glare Dasius cast in his direction as he was dragged away."
        hide andras with dissolve
        "Andras got up and left, Jezera smirked down at Rowan, a knowing look in her eyes."
        je "Why don't you take the first swing at breaking him in? If you're into that sort of thing, of course."
        menu:
            '"Teach" Dasius how to be a whore.':
                $ released_fix_rollback()
                "Rowan picked up on her meaning easily."
                ro "That's a great idea."
                "....."
                "Rowan found Dasius in the brothel a few hours later, his armor replaced with thin trousers and a leather mask around his eyes. His lips curled into a sneer as Rowan entered and gestured for the slave to follow him." 
                "Dasius hesitated, but upon seeing the weapon strapped to Rowan's side, he followed until they came to a spare bedroom."
                das "I thought you were supposed to be a {i}hero{/i}."
                if avatar.corruption > 30:
                    ro "I would say ensuring you don't die is pretty heroic, don't you think? I even came all this way to make sure you got some training for your new job."
                    "Rowan licked his lips, admiring how little Dasius's pants hid his slight erection."
                    ro "On your knees. Now."
                else:
                    ro "I thought so, too. Things are more complicated than that, though…"
                    "Rowan looked down at Dasius's pants, noticing his slight erection through the thin fabric."
                    ro "Have you ever blown a guy?"
                "Dasius didn't respond; he lowered onto his knees obediently, aware of where this was going. Rowan unbuckled his pants and pressed the tip of his cock to the gladiator's lips."
                "His behavior spoke for himself-- Dasius took Rowan's cock into his mouth and down his throat with ease, an expertise that spoke from experience."
                "Rowan's fingers pressed into the back of Dasius's head as he fucked his mouth and throat, his thrusts growing more fervent the deeper Dasius's took him." 
                "The gladiator seemed to be enjoying himself, closing his eyes as his tongue ran up and down Rowan's shaft."
                ro "Fuck, fuck--"
                "His cock twitched, cum spurting down deep into the gladiator's throat. Dasius's swallowed it all, his tongue still tracing against Rowan's tip as they pulled away."
                "Rowan tucked himself back into his pants, a small smirk playing at the edge of his lips. Dasius just watched him, his expression unreadable."
                ro "Looks like you'll have no trouble fitting in here."
                "Rowan patted his shoulder once before making his way out of the brothel. Yes, this had been a good decision."
                $ change_base_stat('c', 5) 
                return
                
            "Leave it to the twins.":
                $ released_fix_rollback()
                ro "I'm sure you two have it handled."
                je "Hm. Suit yourself."
                ro "Is that all you needed?"
                je "Yes, yes, you're free to go."
                "Rowan nodded, eager to return to the comfort of his bed."
                return
                
    "Make him a gladiator.":
        $ released_fix_rollback()
        $ change_favor('andras', 1)
        "They could always use more soldiers, especially experienced ones. If he managed to survive Andras's show to the death, he could be incredibly valuable to their army."
        "He said as much to Andras and Jezera, earning a pout from the female while Andras grinned maliciously."
        an "{i}If{/i} he survives."
        "Rowan had a feeling Andras had no intention of letting the gladiator succeed, but at least he could try."
        "….."
        "The turnout for Dasius's fight was larger than Rowan had ever expected; the arena's stands were filled with orcs and various other castle staff, their fists and feet pounding against the stone chairs and floor in a steady, dooming rhythm."
        ro "You'd think he advertised this fight to half the realm…"
        "The arena itself was empty, although Rowan could hear snarling and growling from the other side behind a solid row of iron bars. Whatever Dasius was about to fight was either angry or hungry-- or both."
        "The gladiator and Rowan stood on the other side of the arena, staring at the empty space with a sense of foreboding."
        das "I didn't expect {i}you{/i} to visit me before the show."
        ro "I thought I'd see a fellow warrior off before battle."
        "Dasius narrowed his gaze, a thousand questions behind his dark eyes. Rowan couldn't tell if he was grateful for the long pause of silence that followed or guilty for the position he'd put the gladiator in."
        das "May I make a request?"
        ro "Of course."
        "Dasius's gaze fell to the sword by Rowan's hip."
        das "If I'm to die, I wish to die a noble death."
        menu:
            "Let him borrow the sword.":
                $ released_fix_rollback()
                "Rowan unhooked the sword from his side and passed it into Dasius's hands. The gladiator's fingers curled tightly around the sheathed sword until his knuckles were white; this was his last chance, a final lifeline."
                "An announcement echoed throughout the arena: the fight was about to begin."
                ro "Good luck."
                "The seats were uncomfortable, but Rowan was more concerned about the gladiator as he stepped out into the arena. A large frog-like beast Rowan didn't recognize-- Draith must have either created this monstrosity or found it-- croaked and snarled through thick fangs before diving at Dasius."
                "Dasius managed to dodge and block one of the blows with his sword. A few orcs boo'd."
                "As the battle continued, Rowan realized the orcs were hoping for a quick round of bloodshed. Instead, they got an actual show and they were disappointed."
                "Harsh words and angry boo's nearly drowned out the announcer's voice as he tried to keep up with the battle. Rowan felt a surge of relief; he had rescued this man. If he were to die, at least it would be noble."
                "But the gladiator did not die. Dasius fought hard, and Rowan could tell that the man had years of training as he dodged and sliced at the beast with expert precision."
                "The frog-creature's corpse rolled over onto its back, its long purple tongue swollen and missing a piece that had been strewn out somewhere in the arena."
                "Dasius raised his arms up in triumph. The crowd boo'd. The slave didn't care; he was alive. At least for one more day. One did not live long in the gladiator pits, after all."
                "He clapped quietly before leaving the arena. Morale may be down, but Rowan's mood certainly wasn't."
                $ change_base_stat('g', -5) 
                return
                    
            "Fend for himself.":
                $ released_fix_rollback()
                "Rowan shook his head; that was not the show Andras wanted to put on, and the orcs were eager for bloodshed. If Dasius was any kind of skilled gladiator, he would find a way to handle this by himself."
                ro "I can't."
                "Dasius's expression slipped and Rowan caught a hint of betrayal on his face. Of course he would see it this way; a hero leaving him up to his own devices, refusing to help the very people he had sworn to protect."
                "But this was Dasius's fight, not Rowan's."
                "Rowan clapped his hand against Dasius's shoulder. The gladiator tensed and swallowed hard, a new panic in his eyes as he looked back out over the arena."
                ro "Good luck out there."
                "Dasius didn't respond. He stood there, still and shocked, while Rowan left to find his seat."
                "The excitement was contagious; Rowan felt himself getting hyped up in the orc's audience, almost as eager for the bloodshed as they were."
                "The announcer yelled over the arena for the fight to begin. The crowd cried out in response."
                "The gates opened. Dasius stumbled out, empty-handed and barely armored. He stared ahead and raised his chin in an attempt to look intimidating, but Rowan could see the weak bend of his legs and the tight fists clenched at his sides."
                "The gladiator was terrified."
                "On the other side, a large frog-like beast Rowan didn't recognize croaked and snarled through thick fangs before diving at Dasius."
                if castle.buildings["pit"].lvl >= 1:
                    "Draith must have either found this creature or created it."
                "The frog spit something at Dasius's arm. The gladiator screamed."
                "The gladiator fell easily, one limb burned off from a strange purple acid emitting from the frog. The rest of the match went quick; without a weapon, Dasius was defenceless."
                "The orcs didn't care, though. They cheered and whooped with each splash of gore and acid in the arena, many even jumping up to their feet as they took in the bloodshed."
                "The announcer mocked Dasius, his voice echoing throughout the chamber until the gladiator's dying breath."
                "The whole affair was humiliating. Rowan stared down at Dasius's corpse-- rather, what was left of it. The gladiator hadn't stood a chance."
                "Excited chaos erupted throughout the arena as the announcer declared the beast the winner, and the audience craned their necks and pushed past each other to get a good view of the frog consuming the gladiator's remains."
                "Rowan grimaced; he felt bad leaving Dasius without a weapon, especially after seeing how poorly it had gone, but what's done was done. At least the soldiers were happier, and that would be just as useful as an extra hand on deck."
                $ change_morale(3)
                return

########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################

label showing_driders_whos_on_top:

scene bg25 with fade

"There was always an unpleasant smell to the beast pits, not from lack of care, but from the animals themselves. It was lucky for Rowan that he had come across plenty of miserable scents in his lifetime, or he might have felt inclined to pinch his nose to block it out."
"How Draith could stand it, Rowan never knew."
"He found the dark elf in a heated discussion with a pair of orcs near the drider cages, his face pinched in irritation. The orcs stalked off, leaving an annoyed Draith behind."

show rowan necklace neutral at midleft with dissolve
show draith neutral at midright with dissolve

ro "What was that about?"

dra "Yes?!"

"Draith jumped, eyes wide and alarmed, until he saw who it was behind him. He pressed a hand to his heart."

dra "Oh, you can't scare me like that! My nerves are shot as it is."

ro "What's going on?"

dra "One of our driders has been a little feisty out on the fields. Neswin--"

"Draith gestured toward one of the cages where a female drider rested, her large body rising and falling with heavy sleep."

dra "--has been bullying the orcs when they go out to fight. She's usually pretty obedient, but she's been relentless out on the fields, constantly picking fights with the orcs."

ro "Has she been hurt?"

"Draith laughed, shaking his head."

dra "They {i}wish{/i} they could lay a hand on her. Oh, it was quite the bloodbath, I hear…"
dra "But she's developed a bit of an attitude, and now the other driders are picking it up, too."

"Another one of the driders in a nearby caged perked up, as if he knew he was being spoken about. Draith gave him a warning glance before turning back to Neswin."

dra "Something needs to be done. The orcs are furious, but what do I do? What do I do?"

"Draith pressed his hands over the lover half of his face, repeating the nervous mantra to himself."

ro "You could always punish her. If she's killing off soldiers, that's enough reason to teach her a lesson."

"Draith looked torn, as if the idea of holding her properly accountable physically hurt him."

dra "I don't want to punish her; it's not her fault she's like this. "

ro "It's not?"

dra "No. It's her first breeding season, after all; she can't help it. She wants a strong male, but none of our driders fit the role. Female driders can be immensely competitive, actually."
dra "Once they reach about two years old, they begin a long search for a partner, and the longer they go without finding one, they become insatiable. It's actually..."

"Rowan tuned out a little at Draith's eager explanation on the inner workings of the female driders' sex drives. The male drider in the cage perked up, almost appearing offended by Draith's claims, but the dark elf ignored him."

dra "--but since no one here fits, she's been looking for substitutes. Unfortunately she picked the orcs, but none of them have been able to live up to the task."

"Rowan nodded to himself and peered between the cages of driders. Violent, nasty beasts they were, but they had an alluring quality to them as well. They couldn't resist their base urges, no matter the problems it caused for others."

ro "But if we don't do something, the orcs aren't going to want to go out at all with them. They might even hurt or kill the Driders while they're out before the beasts attack first."

dra "Ugh, Rowan, I haven't been able to stop thinking about it. Believe me, I know."

"Draith stared at Neswin with a troubled look on his face. Rowan felt for him; punishment of the beasts for misbehavior was one thing, but it was another entirely when the beast was following a natural instinct."

dra "I don't know what to do. She's so good otherwise, but when she's with the orcs, she's practically uncontrollable."

ro "Well, it may not be that she's uncontrollable, but that the orcs don't know how to handle her."

"The dark elf shot a glare in the direction the orcs had left."

dra "You could say that again. I could have fed them to the driders for dinner! They didn't show any care when they brought her back here-- the poor girl was practically dragged into the pits! "

ro "I don't think they're used to having a beast overpower them. The orcs are used to using their physical prowess in fights; they don't know how to peacefully handle a creature that is stronger than them. They just want to fight it more and show their superiority."

"Draith's nose wrinkled in distaste but he nodded, understanding."

dra "They've made that abundantly clear."

ro "Neswin doesn't seem all that powerful-- she isn't bigger than most of the other driders-- so we just need to approach this differently."

dra "Well, don't keep it to yourself. What did you have in mind?"

#If 2 Heavy Armored Orcs in Rowan's Retinue / Battle Prowess Rank 2 - TODO
"Rowan rubbed his chin in thought. Then--"
ro "Bring her to the arena. Make sure she's still a little tired; we don't want her putting up a full fight."
"Draith raised an eyebrow but didn't object. Rowan was glad the beastmaster trusted him; it definitely made his job easier."
"Now he just hoped his plan would work."
"….."
"Rowan met Draith back in the arena, a tired Neswin beside him. She fidgeted, slowly growing more alert as Rowan stepped in. Draith held his whip tightly in case she lost control."
"Two armoured orcs flanked either side of Rowan, chains and shackles held in their arms. They eyed the drider like a challenge, their sharp teeth protruding with their smiles."
dra "So, not that I'm one to doubt you or anything, Rowan, but what is your plan exactly?"
ro "We're going to make sure she doesn't bother the orcs anymore. Would you mind providing a distraction?"
dra "I suppose."
dra "Neswin! Over here, girl. That's it, come forward."
"Neswin followed Draith through the arena slowly, her speed picking up as she grew more awake. Rowan watched her, waiting for a perfect opening."
ro "Now."
"The orcs descended upon the beast, clamping on their shackles around her legs and wrists before yanking the chains to pull her away." 
"Neswin gave out a startled yell, suddenly alert. She snarled and attempted to attack the orcs, but the chains trapped her to the ground." 
"The orcs waited as Neswin thrashed about, failing to free herself from the shackles. She paced the short length the chains allowed, eyeing the group of men with malice."
"But after a few tense minutes, to Rowan's surprise, Neswin sat down. She continued to eye the men, but she didn't bite or fight for her freedom. She seemed to be… waiting."
"Rowan turned to Draith, proud of his work."
ro "I would say she's submissive now, wouldn't you?"
dra "Hm, not quite. She still needs to breed with someone or else it'll be the same situation all over again."
menu:
    "Let the orcs fuck her.":
        $ released_fix_rollback()
        ro "Would it be so bad for the orcs to have a go at her, then?"
        "Draith considered the idea, slowly nodding in agreement."
        dra "Yes, I think that could work. Really, it has to; it's our only option. Until we find a proper drider for her, she'll just keep acting up unless she's properly satisfied."
        "The orcs grinned, having overheard the suggestion."
        ro "Have at it, boys."
        "They wasted no time, quick to slip out of their pants and press themselves on either side of the trapped drider. Her hisses turned to moans as they thrust inside."
        dra "Hm. Yes, perhaps this could work after all! Thank you, Rowan."
        ro "No trouble. Come see me if you need anything else."
        dra "Of course."
        
    "Fuck her yourself.":
        $ released_fix_rollback()
        ro "Let me handle it. I'll make sure she learns her place."
        "Draith watched with interest as Rowan stepped toward the beast and unbuckled his pants. Neswin regarded him curiously, her initial anger subsiding as she took in the length of his cock."
        "Rowan settled behind her. Neswin started as he placed his hands on her waist and shoved her down, hiking the opening of her pussy up toward him. It wasn't hard to do considering her bulbous rear made the opening easy to find."
        ro "You've caused a lot of trouble, you know? "
        "She whipped her head back and hissed, but the sound changed into a whimper as Rowan thrust inside of her with the entirety of his length. Fuck, she was so {i}open{/i}. His fingers dug deeper into her sides."
        "Neswin squirmed, at first trying to pull away, but then pushing Rowan's cock deeper. Neswin jerked her body back and forth in an attempt to ride him, to overpower him, but Rowan held her still."
        ro "Easy there."
        "As Rowan picked up the pace, she slowly fell into submission. Her body jerked with each thrust. Rowan felt his own pleasure build as he felt her wet folds welcome him, her desire obvious."
        "The orcs cheered him on from the sidelines, and even Draith watched Rowan's movements with fascination. There was a small thrill in succeeding where they had failed, especially when he felt just how much the drider wanted his cock driven inside of her."
        "Neswin let out a small cry as her body spasmed with her climax, her legs trembling before they collapsed onto the ground. Rowan pulled out and finished outside of her, his cum stark white as it landed against her black bodice."
        "Rowan strode across the arena back to Draith, tucking himself back in his clothes."
        ro "Let me know if there are any more problems with her. I'll take care of it."
        dra "Mm, I'm sure you will. I'll keep that in mind."
        "With a satisfied grin, Draith ordered the orcs to take Neswin back to the pits. Rowan left them behind, his mind already drifting to the mountain of paperwork he still had to complete."
        
"....."
"Rowan visited the pits once more a few days later. Draith sat in his office but perked up with Rowan's entrance."
ro "Hey. I was just coming to see how everything worked out with Neswin."
dra "Oh, she's getting along just {i}fine{/i}. It's become a sort of game between her and the orcs, really."
ro "A game?"
dra "Yes! The orcs will set traps for her while out on duty, then subdue and fuck her. I was a little worried at first, but she seems to be enjoying the game immensely, even purposefully falling into the traps."
"That was the {i}last{/i} thing Rowan had expected to hear, but it was better than the news that Neswin had slaughtered a whole new branch of orcs. "
ro "Oh. Huh. Well, I'm glad to see it all worked out."
dra "Indeed. Now to stop Neswin from influencing the other driders to fall in traps on purpose as well…"
"Draith mused a little more to himself before jumping back into his paperwork."
return

#Else - TODO
#ro "I'm not really sure. I guess we could try to keep her off of the fields for now."
#dra "Yeah, I suppose that's all we can do for now."
#"Draith sighed in disappointment, then returned to his office."
#"Rowan watched him go. He felt a little bad for not having a better idea, but what else could he do? It wasn't like he could pull a dominant drider out of thin air to please her."
#"With a sigh, he too returned back upstairs to his own waiting pile of paperwork. "
#return

###################################################################################################################################
###################################################################################################################################
###################################################################################################################################

label an_iconic_display:

scene bg24 with fade
show rowan necklace happy at midleft with dissolve
show shaya neutral at midright with dissolve

"Rowan lounged on the cushions in Shaya’s private room in the brothel. She sat across the small table from him, daintily bringing olives to her mouth beneath the veil. His bowl of olives sat untouched. The unfamiliar, Imperial fruit was a stranger to his tongue."

if shayaClueScore < 7:
    "In truth, he was simply enjoying the company, after yet another hard week in the field. Shaya was a patient listener and always engaged herself in relevant topics."
else:
    "He’d considered going with the purpose of information collection, but this visit had proved fruitless in that regard. He’d decided to settle on the simple joy of conversation."

if week > 61:
    sha "I had thought of taking a trip back to Qerazel soon. The big city was always a home to me. The castle is lovely, for its unfortunate location at least, but rather austere."
    sha "Though, I suspect you’ve visited a major city more recently than I have. I’ve never been to Rastedel. Tales speak of it’s industry."
    "Rowan frowned."
    ro "I don’t know what you’re talking about."
    sha "Come now. It’s my job to know things. Your secret is safe with me. Always."

elif week < 61 and orciad_state == 2:
    sha "So many orcs visiting the castle of late. Their dignitaries are giving my boys and girls a hard time indeed. A human’s orifices are not designed for taking so many large...organs in succession."
    sha "Whatever happened must have been a success."
    if delane_status == "free":
        sha "Although...I’ve heard tell of an incident at the orc camp. An escaped prisoner. Orcs like to talk, you see."
        sha "You ought to have kept a closer eye on her. Surely, by now, you see the value of a hostage."
        "Rowan huffed and threw an olive into her cleavage. His hostess giggled."
    else:
        sha "You’ve proven yourself quite the diplomat, Rowan. I’d claim I was impressed...but when it comes to you my eyes are clear. I had no doubts of your success."
        
elif week < 61 and helayna_escaped == True:
    sha "The castle is all abuzz still about that escaped knight. One sweet, and financially well-endowed, frequent customer was suggesting she had dug a tunnel beneath the walls. Another friend of mine was wondering if she’d convinced a cubi to hoist her over the walls."
    if rowanBlameAlexia:
        sha "But, of course, you and I know the truth. One must suppose your subsequent actions explain why you’re down here spending time with a humble servant such as myself."
        "Rowan’s expression remained stone-like."
    else:
        sha "I’d ask you more, but I’m sure her absence has you distraught. You were close, yes?"
        ro "You could say that."
        
else:
    sha "I’ve heard much about the fall of your little castle. So much fighting and bloodshed. I can never stand such things. That is why the fighting is best left to...strapping...young men."
    ro "I’m not so young."
    sha "Perhaps. But, you make up for it in the strapping realm."
        
"After some further relaxation, Rowan stood to leave. Involuntarily, he broke into a stretch. His muscles had grown stiff from the time spent in uncharacteristic relaxation."

ro "I think that should be all for the day. If I’m down here too long, people might start to wonder about my absence."

show rowan necklace neutral at midleft with dissolve

"But, as Shaya accompanied him to the front hall, something struck his eye down the side corridor. He turned to inspect it."

sha "Sir Rowan?"

scene black with fade
show rowan necklace neutral behind black
show shaya neutral behind black

"What he found was a display of what seemed like an art piece. If one could call a human being an art piece, that is."
"It was a naked woman standing in perfect posture in the center of the hall. Her arms were folded behind her back and her stance kept her legs spread wide. But, it was impossible to see her face." 
"A large ornate mask in the shape of a woman’s face covered her head. It was hewn from a shining material that was perhaps gold. Writing in Imperial script lined the head, along with an artistic molding in the shape of a halo."
"Rowan approached the woman close and studied her. There were small air holes at the top of the mask, but otherwise it was totally closed."

sha "Curious? One imagines this is a custom you’re unfamiliar with."

"The Brothel Madam appeared at his side. Her arms wrapped daintily around his chest."

sha "In Qerazel, among the elite of courtesans, the training regiment must be equally elite. And the punishments for failure are severe. This was a training method shown to me by my former Madam. Called, The {i}Epipala{/i}."

"She ran a hand along the cheek of the mask, as if caressing another human being."

sha "The Priestesses of Solansia in Qerazel hew great works of art to The Lady’s honor from gold. They are called {i}Ikons{/i}. It is said they are blessed by the power of the goddess themselves. They are her pride and majesty."
sha "I was never a religious girl, but gold has a power on it’s own."
sha "But, a courtesan is a servant of her duty. Confidence is vital, but pride is a sin."

"Her hand drifted lower, to the collarbone of the girl. The moment she touched skin, the girl shivered. But, just as quickly returned to statue-esque posture."

sha "This girl attempted to solicit customers after I had forbade it. She believed herself too good for a lengthy training period. And she spoke back to her madam when I scolded her."
sha "The {i}Ikon{/i} Mask blocks her words, her ears, her eyes. She must remain in place, unspeaking, unmoving, regardless of what the customers do to her. In that time, she is to be art. A week with no name will serve her well."

"Shaya drew herself from Rowan and circled the girl. She traced the tip of her fingernail around the girl’s hips. It left a slight indentation in its wake for a moment after."

menu:
    "Sounds kinky.":
        $ released_fix_rollback()
        "Encouraged by Shaya’s handsy approach, Rowan couldn’t resist placing a hand on the girl’s thighs."
        if avatar.corruption < 31:
            ro "Sounds kinky. She’s basically on display this way. I suppose...I could see how some people could be into having a girl this way."
        else:
            ro "Sounds kinky. You’ve got this slut out here as basically a decoration. Tempting people to touch her exposed body…very kinky indeed."
            "He gave an evil grin and brushed his hand further up the girl’s thigh."
        ro "Probably a nice attraction for a brothel too. A nice warm up for the rest of the business. How do I know you didn’t make up the whole punishment story just to make the display sound kinkier."
        "Shaya circled back around, placing her hand atop Rowan’s."
        sha "If it soothes you, there is nothing stopping it from being both a spectacle and a punishment. Shame and humiliation is a powerful motivation, but also a source of profit. Why not make use of the tools you have?"
        
    "Sounds Like a grueling ordeal.":
        $ released_fix_rollback()
        "Rowan eyed Shaya skeptically."
        ro "A week standing at attention as a glorified sex toy? Sounds like a taxing punishment for a single instance of back talk."
        sha "I take no joy in it. But, the purpose of a punishment is to modify behaviour. She will learn from it."
        "Shaya’s eyes still trailed the still courtesan. Rowan’s glance faded from them down to the veil over her face, and the absent expression that was surely beneath it."
        ro "..."
        ro "When you were studying how to be a Courtesan in Qerazel, I have to imagine that you were subjected to the same kinds of punishments."
        "Shaya sighed inwardly."
        sha "On many occasions. There was a time I was...haughty. My Madam broke me of that a long time ago."
        "She flashed him a seductive glance and pulled closer to him."
        sha "Or were you asking for the purpose of roleplay? I do have another mask should you wish..."
        ro "No no, I just meant that it sounded like a grueling ordeal."    
        "She sighed and pulled back from him."
        sha "It was. But, I understand why it was necessary. That is sufficient."

"Rowan’s eyes wandered over the girl’s body. She was pretty. Shapely smooth breasts, toned arms and legs, skin of a dark cream."

menu:
    "Indulge.":
        $ released_fix_rollback()
        "Rowan openly stared, mouth parting slightly. Shaya was there to witness him. But, what would she care?"
        
    "Shy away.":
        $ released_fix_rollback()
        "Rowan tried to pull his eyes away from her. He was not alone in the room. She was not the sort to judge, but it still felt wrong."

sha "It’s quite alright for you to partake. This place, and all of it’s pleasures, are spread open for you."

"Her voice turned to a hoarse whisper."

sha "You may do whatever you wish to her."
sha "I would draw the curtains for you. Let you loose your desires in private. Not even the girl would know."
sha "Perhaps you’d even like to engage in more...unconventional pleasures. There’s a chest full of clamps by the wall for that very purpose. All forms of indulgence are welcome here."

"Rowan clenched his fist."

menu:
    "Use the clamps.":
        $ released_fix_rollback()
        "Without a further word, he trailed over to the aforementioned chest. It was no surprise that it was gold lined with a velvet interior. The clamps inside were equally a work of excess. They were shaped like river crocodiles and hewn from bronze."
        "Rowan held one up. Then, he smiled darkly."
        sha "It seems you’ve decided."
        ro "It seems I have."
        "He grabbed an armful of the clamps from the chest and returned to his unaware victim. There was no creation to his approach."
        "Even with senses dulled by the mask, she was aware of his presence from the touches. But she was disciplined enough already to keep as still as a statue."
        "He was going to have to change that."
        "To test their strength, he placed one of the clamps on his finger. At once, he pulled it off with a wince. These things stung."
        ro "You’re sure it won’t leave a mark?"
        sha "We have tested them. Extensively."
        ro "Hmm."
        "Without a further word, he went up to the girl’s breast and clamped her nipple. For a split second, he detected movement. As if she had bounced on her heels. But, on second glance she was holding with perfect discpline."
        "Still, if there remained any doubt she was aware what was happening…"
        "Rowan placed a second clamp to her other nipple to match the first. It would have been wrong to take the symmetry from a piece of art like this. Still, this one had even less of an effect. She didn’t even flinch. Evidently, it would be be harder when surprise isn’t a factor."
        "So, Rowan kept on adding clamp after clamp. Each must have become a hotspot of pain, radiating out. Certainly they were digging into her breasts with enough of a bite that the skin was pulled. But, sure enough, she held firm."
        sha "If I may be so bold as to make a suggestion. There are other places for you to clamp."
        "Rowan turned back to Shaya."
        ro "“Bold as to suggest”. You really want me to torture this girl’s crotch, huh?"
        sha "...My want is irrelevant here."
        "The statement gave him an idea. He took two clamps and tossed them to the madam."
        ro "I’m not doing this for your amusement, you know? How about you put these on your nipples too. A reminder not to overstep."
        sha "mfff."
        "In the same gesture that she caught the clamps, the first was already placed on her body. It dug into the soft fabric of her top. Soon, it’s twin would find a similar spot."
        sha "If this will please you."
        "Rowan turned back to his primary target. Shaya’s prior suggestion still stuck with him. It may have been vengeful, but that didn’t mean it wasn’t cruelly effective in it’s own way."
        "He started slow. One clamp on each lip of her labia. At once, the effect was visible. A slight twitch. A crack in her armor. Rowan smirked. He was going to break through. He just needed one more step."
        "So, he leaned down, final clamp in hand. He had to prod her sex to find it’s destination. The nub of her clit was but a bump in his hands...but it was more then solid enough to serve as a handle. A moment later, the final clamp bit into her clit."
        "The reaction was instantaneous. A shiver that ran up her leg. This time, there was a fit of squirming before she regained her pose. Regardless of her duty, this was clearly no easy task for her."
        "Rowan returned to Shaya’s side to admire his handiwork. There was a strange beauty to it. The glimmer of gold and bronze. The unchanging face of the goddess looking back at him. He sighed softly."
        sha "May I remove the clamps now, Rowan? I believe you’ve made your point."
        ro "I suppose."
        "His attention was trained solely on the girl. The clamps on her breasts had been in place for a few minutes now. More than enough time for the cumulative strain to go from painful to excruciating. Every moment tortured by the clamps would grow more intense."
        "It was showing in the girl’s posture. What had been a few breaks had turned into the occasional squirm. That, in turn, had descended to full on wiggling." 
        "He leaned in closer. Any moment now." 
        "Then, it came. A soft scream, muffled by metal. The limits of the girl’s endurance. She fell down to one knee, chest rising and falling. It made a funny sight. The bronze of the clamps seemed to dance in the air to the movement of her body."
        "It was only then he had mercy. With Shaya’s help he removed the clamps one by one. This proved a final torture for the poor girl. Each time a clamp was removed, her arm shook. The sudden absence of the pain could be more intense then the initial bite."
        "It was only when the final piercing was removed, the clit clamp, that the girl finally rose to her feet."
        "Shaya shot him a knowing glance."
        sha "I had not known you to be a sadist of this calibre. Perhaps in the future, I can plan in advance something to scratch that itch."
        
    "Jerk off on her.":
        $ released_fix_rollback()
        "Rowan stared at the naked form of the courtesan with a dry mouth. Naked, wearing the mask, there was a strange serenity to her. She was more like a marble sculpture then a person. Too perfect to be real."
        "His hands quietly fumbled with his belts. Shaya watched with a cat’s curiosity."
        "She was too perfect. He had to spoil her."
        "There was a clattering as his trousers landed on the floor of the brothel. Rowan drew closer, so close that his erect mass nearly touched the girl." 
        "Then, his hands joined in the action. They pumped back and forth in a pattern familiar to him since adolescent, stroking the surface of his cock."
        "As he did, his hand nearly brushed over her skin. As the friction grew, he started to groan. It wasn’t a long and slow effort. He was working himself as fast as he could, for one purpose. To defile her."
        "Of course, the subject of his glance didn’t move. Had it not been for the earlier touch, she may not have even realized she was not alone. Still, she held pose, with the tiny movement of her chest even showing she was alive." 
        "He blinked softly. What had Shaya told him before? That she had been made to endure this for being haughty? In his mind, he imagined her as an ice queen. Someone so rigid that she deserved this treatment." 
        "Shaya circled closer, brushing a hand over Rowan’s back. It brought a shiver down his spine. He felt the brush of her veil along the tip of his ear."
        sha "My assistance might prove valuable here, Rowan. You need only give permission."
        "The intent could not be more obvious."
        menu:
            "Let Shaya assist.":
                $ released_fix_rollback()
                "Shaya’s slender arm gradually wrapped itself around his waist. She took her time to allow him plenty of opportunity to stop her. But, Rowan didn’t stop her. Instead, a soft sigh escaped his lips the moment her hand wrapped itself around his cock."
                "Slowly, his hands drifted down to the side. Instead, Shaya’s delicate fingers took up the work stroking him off. The shape of her hands and the pace she set were practiced. Tight enough a grip to feel almost as if he were engaging in penetration, but loose enough to be comfortable."
                "He sighed and leaned back into her. The tips of her nipples gave a tantalizing brush against his back." 
                "Yet, his eyes never left their true focus. The creamy skin of the woman in front of him. As the pressure mounted and his eyes fluttered, the thought of despoiling her was what consumed him."
                "It made it inevitable that he wouldn’t last long. His cock twitched. Shaya aimed it square at the girl’s belly."

            "Finish without her.":
                $ released_fix_rollback()
                "She slid a slender arm around his waist. But, before her hand could reach his cock, he brushed it away. Wordlessly, she drew back to a less obtrusive distance."
                "This was a task he wanted to finish at his own pace."
                "He focused with his full attention on the girl. Her perfect posture and creamy skin begged for despoilment. The mask of the goddess stared back at him. Holy and unfeeling. In a sense, it was almost like cumming on Solansia herself."
                "His pace picked up to frantic stroking. He was rushing towards his inevitable climax at his fastest possible speed. His eyes slammed shut."
                
        "Then, in a flash of white, he let loose."
        "In his wake, he left the girl stained by his cum. A streak of white ran from the underside of her breast all the way down to her hips. Smaller globs were splattered in a rough pattern around the line."
        "He staggered back panting. The orgasm felt good, of course. But, it was for this sight that it had all been worth it."
        "Shaya took to his side and looked on with equal fascination."
        sha "A fine painting job, sir. I couldn’t have done a better job myself."
        ro "At least not without the right tools."
        "She giggled softly into her veil."
        
    "Decline politely.":
        $ released_fix_rollback()
        "A beat passed. Rowan could picture the feel of her nipple between her fingers. The splatted of his seed over her belly."
        ro "...No..."
        "He pulled his glance away from the girl and her plight. This was a temptation that would not snatch him."
        "Shaya pulled to the side and stoically bowed."
        sha "Of course, Sir Rowan. I apologize for overstepping in suggesting something so inappropriate."
        "He shook his head slightly."
        ro "No. No. It’s your job. You’re alright..."
        
"Rowan went silent for a time, contemplating the faceless figure before him. He’d almost missed it before, but there was something about her…"

ro "This girl. What’s her name?"

sha "Sweet Rowan. It would defeat the purpose of the punishment to reattach a label to her. For now, she is just a girl."

ro "...Does she frequently work the attendant desk, though?"

"There was a twinkle in Shaya’s eyes, but the veil hid if it spread to the rest of her face."

sha "I will simply say that she is not authorized to interact with a client, absent my permission. No matter how much she professes her beauty is “wasted”."

"She shook her head slightly."

sha "Beauty is wasted on the beautiful. This is where pride ought to lead."

menu:
    "Agree.":
        $ released_fix_rollback()
        ro "With how strong your hold on the girls here are, she must have expected it wouldn’t go well. Compared to dealing with a succubus, a bratty attendant is nothing."
        sha "I cannot speak for the girl. But, she cannot speak for herself presently, either."
        
    "Flirt.":
        $ released_fix_rollback()
        "Perhaps, Rowan might have taken those words seriously if they’d come from someone else. He gave Shaya a nudge in the side and shot her a bemused look."
        ro "Don’t give me that. With looks like yours, you were probably a menace in your youth too. Maybe Jezera will tell me some time."
        "Shaya chuckled softly."
        sha "...Perhaps."
        
"Rowan turned to finally leave, when one final idea came to him."

if liaAttitude == "flirt":
    "He turned back to the girl and gave her a sudden and intense smack on the rear. She jumped slightly before returning to her prior position." 
    "It gave Rowan a soft grin."

else:
    "Rowan drew a coin from his belt and snuck it into the girl’s hand. When she realized what it was, her grip tightened around it."
    ro "{i}Here’s something for your trouble.{/i}"

return

###################################################################################################################################
###################################################################################################################################
###################################################################################################################################

label succumbing_to_shaya:

scene bg12 with fade
show rowan necklace neutral at midleft with dissolve

"There was always a strange calm in the library. The rest of the castle could often be a storm of trouble, but it seemed like nothing could truly break its silent serenity. Perhaps that peculiar quality helped to explain how it survived all the sacks of the castle."
"Thus, when something did disturb the normal energy of the library, he was able to tell immediately. It was a scent. Beautiful and calming, like a field fresh of flowers. Rowan returned a book to the shelf and followed where his nose took him."
"The place it led was the front desk, where someone he had become well acquainted with was signing out an armful of books."

show shaya neutral at midright with dissolve

"He only got a chance to watch her for a few fleeting moments before she noticed his presence."

sha "It appears I have a voyeur. You don’t have to gawk, Rowan."

menu:
    "Respond confidently.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "You’re not complaining about a little staring, are you?"
        sha "Noting, not complaining. One gets used to being seen."
        
    "Respond in surprise.":
        $ released_fix_rollback()
        show rowan necklace shock at midleft with dissolve
        "He blinked twice. When dealing with Shaya, he frequently had to mentally ready himself lest he be tripped up in her flirtations. But, seeing her in an unexpected place left him flat footed."
        ro "Uh… hmmm..."
        sha "Tongue-tied? A form of flattery, to a woman of my profession. And here I had come to believe that you had found a way to keep your wits about me."
        
"Beneath her veil, a hint of a smile could almost be divined. The longer Rowan spent with her, the more second nature reading her veiled expressions became."

sha "It is good fortune that we happened to cross each other's paths today. You've been in my thoughts, Rowan."

ro "Have I?"

show shaya happy at midright with dissolve

sha "I had an inkling of perhaps… inviting you back for another special session. This time, no party. Just you and me."
sha "If I wasn't too disappointed in our prior engagements, that is. "

show bg12 with smallshake
show rowan necklace neutral at midleft with dissolve

"Before he could respond to what she said, there was an interruption. A loud clattering noise like books toppling from the shelf. His ears perked up."
"Was someone else here?"

ro "Hrmm."
sha "Ah, I appear to have lost your interest…"

show rowan necklace happy at midleft with dissolve

ro "No… no. Of course not."

sha "Then it is settled. You simply must come back down soon. I've been preparing a surprise for you! Something that will make our session from the party look meek by comparison. Something you won’t ever forget."
sha "Can you be there tomorrow?"

ro "Tomorrow. So soon?"

sha "What can I say? You have caught me at the height of my anticipation. If one is putting in great effort to ensure every detail is perfect, is it so wrong to be eager?"

menu:
    "A polite response.":
        $ released_fix_rollback()
        $ shayaResponse = "polite"
        if avatar.corruption < 61:
            "Rowan gave her a warm smile."
        else:
            #ro smirk
            "Rowan gave her a low smirk."
        ro "Well if you’re so excited by it, then who am I to disappoint you? I’ll be down to see you tomorrow."
        
    "An eager response.":
        $ released_fix_rollback()
        $ shayaResponse = "eager"
        ro "More impressive than that dance at the party?"
        sha "Far more."
        "He chuckled softly."
        if avatar.corruption < 31:
            ro "Well I suppose I can’t complain about that. You do like your promises."
            ro "You can count on my presence."
        else:
            #ro smirk
            ro "I’ll hold you to that, Shaya. That sky dance was something else entirely. You must have something good cooked up."
            ro "Tomorrow, you said?"
            "Shaya nodded softly."
            sha "You can most certainly expect me."
 
show rowan necklace aroused at midleft with dissolve           

"The brothel madam drew closer and placed her lips to his cheek. The soft sensation was blunted only by the layer of fabric perpetually in the way."

sha "Truly then, it was my fortune that we ran into each other."
sha "I will see you tomorrow, Sir Rowan. But, even that short a wait will leave me in anxious anticipation. Please don’t be late."
        
"With a final, soft smile she departed, cradling a pair of books under her arm. Rowan sighed. As she left, the smell of flowers from her perfume drew fainter and fainter. As if a fading memory of her presence in this section of the castle."

hide shaya with moveoutright
show rowan necklace neutral at midleft with dissolve

#and NasimGrandDisplay = False - TODO
if nasimAvailable == True:
    "But, once he was sure she was gone, his eyebrows narrowed. He turned to march towards the segment of the library where he’d heard the clattering of books."
    show nasim angry at midright with dissolve
    "And there, he found the source of the noise. Sprawled out on the ground, with a small pile of books that had fallen from the shelf...was Nasim."
    ro "It’s unlike you to hide like this, Nasim."
    "With a shaky start, Nasim worked his way back on two legs. The man tensed for a moment, then took off his hood, and regarded Rowan with a carefully crafted, indifferent look."
    nas "To the contrary, Lord Blackwell. I’ve long since learned intellectual prowess is in low supply in Castle Bloodmeen, and every random passerby seems to have a list of lifelong issues only you can fix."
    nas "It’s simply better to keep your distance, more often than not."
    ro "Ah yes, because you of all people would find it difficult to tell them to sod off."
    nas "And in the eyes of some people that would make me the asshole, as if bothering others with personal problems was a virtue we should all share."
    "Insults and misdirections. Nasim’s chatter was amusing at the best of days, and infuriating at any other. Normally he would be inclined to indulge it. But right now… What attracted his attention was the topic Nasim seemed desperate to avoid."
    ro "You were trying to hide from Shaya in particular, weren’t you? Why? Aren’t you both from Qerazel? I’d think you’d get along better with your countrymen than that?"
    nas "You assume we’re from the same place because we have the same skin color? How offensive… Not to mention, naive to think national identities mean much here in Bloodmeen."
    ro "You’re stalling, Nasim."
    "Nasim’s lips formed a thin line, and his eyes darted to the exit. It made his blood boil. Why was the man always so damn difficult to deal with?"
    $ shayaNasResponse = ""
    
    menu:
        "Appeal to his best interest." if nasimAttitude > -1:
            $ released_fix_rollback()
            $ shayaNasResponse = "best interest"
            ro "Be honest with me. Why the hesitation?"
            nas "Is it really that difficult to believe I simply wish to avoid even the risk of antagonizing an avowed spy Mistress?"
            ro "Perhaps not. But whatever you say stays between us. I have nothing to gain by selling you out."
            nas "… And I have much to lose by antagonizing {i}you{/i}."
            ro "I didn’t want to say it out loud. But yes. Exactly that."
            nas "Charming. Very well, I will indulge you. But you’ll be disappointed to learn I know little."
            jump shayaQuestioningNasim
            
        "Pressure him into compliance." if nasimAttitude < 0:
            $ released_fix_rollback()
            $ shayaNasResponse = "pressure"
            ro "Are you afraid of her, Nasim? "
            nas "I lived long enough to understand the risks of antagonizing an avowed spy Mistress. A wise man knows when to stick to the shadows."
            ro "Well put. But there are no shadows for you to hide now."
            "He grabbed Nasim by the edge of his robe and shoved him into the bookshelf. A single rune flared up - but Nasim made a swift motion with his hand, and it went out as quickly as it appeared."
            ro "Wise choice. Now listen well - you want to stay out of Shaya’s sight? Fine. But you don’t have that luxury with me. I can make your life very difficult, Nasim."
            ro "So start talking."
            "… For a moment, only the quiet wobbling of the shoved books could be heard. Rowan had to commend the wizard on keeping his cool - that icy glare would make even Cliohna jealous."
            nas "… Fine. But you’ll be disappointed to learn I know little of her."
            jump shayaQuestioningNasim
            
        "Forget about it. More time to focus on Tomorrow.":
            $ released_fix_rollback()
            ro "You know what? Fine. Have it your way."
            "Almost throwing his hands in the air, he left the wizard alone. There were a million things that needed his attention - and he needed to get them out of his way so he could focus on Shaya properly."
            if shayaClueScore < 7:
                "He would hate for someone to interrupt them in the middle of his surprise… "
            else:
                "His investigation would finally bear fruit - and he needn’t bother with other men for it."
            hide nasim with moveoutright
            jump shayaPostNasim
            
        "… There were enough men vying for Shaya’s attention." if lirioConfront:
            $ released_fix_rollback()
            "Briefly, he wondered - what exactly was he trying to accomplish by adding {i}yet another man{/i} to Shaya’s seemingly never ending circle of clients and suitors?" 
            "Was what little information Nasim could offer worth sharing everything he had learned about the woman." 
            "His thoughts briefly returned to Lirio, and that fat bastard putting his hands on Shaya. If he had to handle Nasim as well on their next orgy-"
            ro "… You know what? Fine. Keep your secrets."
            "He let the man go - before he talked himself into punching him in the face. Just because."
            hide nasim with moveoutright
            jump shayaPostNasim

    label shayaQuestioningNasim:
    nas "I have heard she’s apparently skilled enough to handle demons on a daily basis. I have heard she has a reputation for placing eyes and ears where they don’t belong. But, most importantly, that she’s been personally handpicked by Mistress Jezera."
    nas "The latter is reason enough to avoid her. I try not to step on the Mistress’ toes - as should you. "
    "Rowan leaned back against the bookshelf and crossed his arms over his chest." 
    "Perhaps, then, there was something else he wasn’t saying. He might have been a person she would have recognized? Though, knowing Nasim, almost certainly not someone close. Still, that was all guesswork..."
    ro "Is she as popular as I suspect? "    
    nas "You ask the wrong man. My duties seldom lead me to the castle brothel. Nor had I frequented them before I came here. If it were otherwise, I’d be in a very different profession."
    ro "Hrm… Suppose then I’m not asking you for first hand experience. Just what you’d suspect with a background from Qerazel."
    nas "I still never said I was from Qerazel."
    ro "Less bullshit."
    nas "…Fine."
    nas "If I am being forced to speculate, I would be surprised if she were not popular. Women in such professions often get to high places. I have seen it first hand. Mistress Shaya is the embodiment of sensual perfection."
    nas "And in Qerazel everything {i}must{/i} be perfect. Beauty is power. A woman’s status is proportional to her obsession with fashion and frivolities. And men by the aesthetic excellence of their companions. For most, appearances are the only thing that matters."
    ro "Still...sounds like an environment where Shaya’s looks would prove a valuable asset."
    $ shayaClue13 = True
    $ shayaClueScore += 1        
    nas "If one was able to back such looks with skills and guile… They would no doubt thrive. But I cannot assess either on Mistress Shaya’s part."
    if shayaResponse == "eager":
        nas "You, however, seem to have firsthand experience? Sky dancing perhaps…?"
        "Rowan tried not to blush. If embarrassing him was Nasim’s subtle form of revenge for being involved in all of this, he succeeded."
    nas "That’s all I have to offer, Lord Blackwell. If you desire more in depth knowledge about the social and cultural workings of the empire, there are better sources of it than myself."
    ro "Hm… I suppose."
    if shayaClue12 == False:
        "Nasim brushed his hands over his robes and straightened a few of the books that fell to the floor."
        nas "Now then, if you’ll excuse me. I have important business to attend to. Business you're nosing about has given an unsightly delay too."
        "Rowan moved to the side and let him pass. There was little else he wanted with the wizard. And much on his mind to otherwise distract him…"
        hide nasim with moveoutright
    else:
        "But, before he let Nasim out of the conversation, something else came to the surface. A topic that had been rattling around at the back of Rowan’s mind since the night of the party at the brothel."
        ro "Actually, there’s something else I’m wondering. Totally unrelated to Shaya."
        nas "Unrelated to her? Very well."
        ro "Your chamber. Suppose I had a scar that I disliked. Could it be used to, say, remove that scar?"
        if castle.buildings["nasim_chamber"].lvl > 0:
            "Nasim rolled his eyes, as if a toddler had asked him a simple math question."
            nas "There is little it cannot do. Chaos magic has no concept of boundaries or limitations. It can change a man into a thing he would entirely not recognize."
            if avatar.corruption < 31:
                ro "Everytime we discuss this topic I’m reminded just how questionable your research is."
                nas "Yes, yes, fire and brimstone await me. "
            nas "So the answer is affirmative."
            nas "That said, scars tend to present something of a unique problem. I believe I spoke at length of how Solansia’s mandate ensures ontological inertia. The more a thing or a person identifies with its own shape, the harder it will be to modify it in a lasting manner."
            nas "In that regard, a scar might seem like a simple, small thing. But… "
            nas "You understand it best, I imagine. A scar is not just a simple injury of the flesh. It’s a symbol of your struggles. History engraved into your very body. It’s part of you more so than even your arm or your leg."
            nas "For transformation magic, it’s physical size wouldn’t matter nearly as much as the emotional weight it carries. The greater it is, the harder it would be to remove."
            nas "In most cases, only the most powerful of magical means could permanently remove even a simple scar."
            ro "How hard would it be?"
            nas "If I had to, once more, speculate? The scars you received in the war would be near impossible to be rid of. For it, only the chamber and the magics buried within would suffice."
            nas "So unless your desire to remove the scar is of the highest order, I would suggest a simpler and less drastic solution. Perhaps some type of illusion charm to mask it. Though, it might not conceal it up close."
            $ shayaClue14 = True
            $ shayaClueScore += 1
            "Rowan went silent, considering his words. If that were the case, Shaya could not have simply gone to Jezera and had her scar removed…"
            nas "Do you require help drawing up such a charm?"
            ro "No, no. I was just curious."
            nas "Then, can you be curious somewhere else? I believe I have answered your question to a satisfactory extent."
            hide nasim with moveoutright
        else:
            nas "A fascinating question. One I would be more willing to indulge, if the matter wasn’t still buried beneath our feet." 
            if shayaNasResponse == "best interest":
                "Rowan’s mouth made a thin line, and he avoided Nasim’s glare. He should consider himself lucky that the man even bothered to indulge his earlier questions."
            else:
                "Rowan’s mouth made a thin line, and he briefly considered taking his threats one step further."                 
                "But this was not worth making an enemy of the man… He would have to be content with what he learned up till now."
            ro "I see."
            nas "Now then, I believe you have nothing further to waste my time with. I have duties I must attend to."
            hide nasim with moveoutright

else:
    pass

label shayaPostNasim:

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve

"In the hallway, Rowan’s thoughts were still on his encounter with Shaya’s proposed session for tomorrow."

show jezera happy at midright with dissolve

je "Feeling pensive, Hero? Surely I haven’t made you do anything too awful."
je "...Today."

"He glanced to the side and found the demoness was walking beside him. Her arms were stretched out, and every few seconds she let out an easy-going yawn."

ro "It’s nothing."

je "I see. Well, if you are otherwise free, then you simply must join me. I was going down to the brothel for another tea session for Shaya. Surely you must be eager for another session with her."

"He smiled politely."

ro "No need to see her so soon.  I just ran into her in the library. We have a visit together planned for tomorrow."

"Jezera raised an eyebrow."

je "In the library? Did she say what she was there for?"

ro "Actually, I don’t think she did."

"Rowan tilted his head."

if shayaClue7:
    "What books had she been there for, anyway? He hadn’t gotten a good look at them before she’d walked out. Had he been so distracted?"
    "But, perhaps she hadn’t come for books at all? It had struck him as quite the coincidence that she’d come at the same time as him - and with a proposal for the following day she was eager to tell him, no less."

je "Fascinating. I’m sure I can extract the rationale from her over tea. "

"Jezera affected a careless shrug."

je "A shame you won’t be joining us, but such is life, hero."

scene bg9 with fade
show rowan necklace naked neutral at midleft with dissolve

"Once Rowan arrived in his room, he went right to his desk and pulled out a book. There, hidden in the pages, was his roll of parchment with the question written at the top. {i}Who is Shaya?{/i}"
"In the time since he’d first written that question, he could have considered the question answered." 
"She was skilled, dutiful, polite, and gentle. She was eager to please her clients, but loyal to her “best friend.” He’d heard her sing, seen her dance, and even gotten fleeting chances to speak to her about her life."
"Yet, he dwelled on that segment of parchment, the more it felt like he hadn’t come closer to answering that question at all. She hid much."

if shayaClueScore < 7:
    "The longer he stared at the document, the heavier it felt in his hands. In stark contrast, the more clearly he noticed just how little he’d written in it. So much of the parchment remained blank."
    "He put a hand to his chin and studied it closer."
    "Had he really spent so little of his time with Shaya delving into her past? He searched his memory for instances where he’d dug for more information, but he found so few instances. It seemed impossible. And yet..."
    "There had been all those times he’d come just to see her dance. Or to spend time in conversation with her. Or else simply to fuck her."
    if shayaClue15 == False:
        "His eyes scanned the segment of the page where he’d written his observation after the first time he’d seen her dance."
        "{i}Shaya is… radiant.{/i}"
    if shayaClue1 == False and shayaClue5 == False and shayaClue6 == False:
        "On one stretch of the page, there was a crude drawing in the shape of a nude woman. The barely remembered result of a mind blowing night? Rowan smirked at its vulgar curves."
    "The strength from his hands died. The parchment tumbled limply to the floor. He let out a final sigh."
    "The truth was staring him in the face. There was no denying it now."    
    show rowan necklace naked aroused at midleft with dissolve
    "He’d stopped going down to the brothel to investigate Shaya a long time ago. He’d been lying to himself to justify it. The reason he went now was... to be with her. To be inside her. Or even just to be in the same {i}vicinity{/i} as her."
    if avatar.corruption > 31:
        "Even thinking about her sent his heart into uncomfortable fluttering. The faint remnant of the smell of flowers still hung in his nostrils. It was like an addiction. He knew it was wrong… but it was too late now."
    elif avatar.corruption > 60:
        #ro smirk
        "He wanted her. He wanted to fuck her. He wanted to be around her. He wanted to make her his and only his. He wanted to {i}despoil{/i} her."
        "He wanted her desperately."
    else:
        "His cock always seemed to stiffen at the thought of her. How many times had he dreamed of her? The effect she had on him was intoxicating. He swore under his breath at how low he’d fallen."
    "And so, that night, when Rowan went to sleep, it was Shaya that was in his thoughts. In his dreams."
    "But the parchment he’d used to investigate her lay in a crumpled heap among his discarded trash..."
    jump shayaSuccumbing
    
else:
    "It was this sense of absence, of something missing, that drove him closer and closer to the roll of parchment in front of him. Long segments of notes and text packed the page." 
    "He was so close. If the thought had a physical shape, he could almost touch it. Just what was he missing?"
    scene black with fade
    "Rowan spent that night reviewing his notes and reflecting on them. Making connections between the questions, and tracking the paths they made." 
    "Rowan had once heard that the truth was a type of story. To find it, first one must find little threads of detail and fact. Only afterwards, do you bind it all together. And if done well, the story it tells will resemble the real world."
    "It was many hours later when he had finally finished the story. Amidst the details of his notes, he had pieced together some hint to the secrets Shaya was hiding."
    scene bg9 with fade
    show rowan necklace naked neutral at midleft with dissolve
    "Rowan’s quill went to the space directly beneath his initial question, and there he wrote an answer."
    "{i}Who is Shaya?{/i}"
    "{i}Whoever Jezera wants her to be.{/i}"
    "He leaned back in his seat, running a hand through his hair. There were still doubts in Rowan’s mind, but he believed he had a theory about Shaya and her secrets."
    "It would explain where she came from, her relationship with Jezera, and the strange air of mystery to her. Not only that, but it offered a chance to get a leg up on Jezera for once. Knowledge was power, after all."
    "But, it also meant there was little else to be gained from his pleasant...or occasionally rather more than pleasant...visits down to the brothel."
    "The best course of action now would be to take what he knew to Shaya and confront her with it directly."
    "Even if she denied it, one of two situations would occur. Either, she’d be put in a state of disadvantage where he could trip her up in lies. Or else she might genuinely disprove it, but in so doing leave him with even more information. Valuable reactions either way."
    scene black with fade
    show shaya neutral at center with dissolve
    "The only problem was, he did not know how Shaya would take to him for the encounter. Would she be impressed by his deductive skills? Upset at his efforts to pry into her life?"
    "If he wasn’t careful, in the process of confirming the information, he could reshape the budding dynamic between the two. And Rowan wasn’t sure if it would be in a way that would bring them closer.."
    "One of the two would have to be more important. The truth and the advantageous knowing it would bring...or his ability to indulge himself in Shaya’s company?"
    sha "Rowan..."
    label shayaFinaleMenu:
    menu:
        'Confront Shaya with the "Truth".':
            "Are you sure?"
            menu:
                "Yes.":
                    $ released_fix_rollback()
                    jump shayaConfront
                    
                "No.":
                    $ released_fix_rollback()
                    jump shayaFinaleMenu
                
        'Forget about it and follow what Shaya wants.':
            "Are you sure?"
            menu:
                "Yes.":
                    $ released_fix_rollback()
                    jump shayaFollow
                    
                "No.":
                    $ released_fix_rollback()
                    jump shayaFinaleMenu

label shayaFollow:

scene bg9 with fade
show rowan necklace naked neutral at midleft with dissolve

"Rowan closed his eyes. He could burst into the brothel tomorrow and confront Shaya with his suspicions. Perhaps she would still allow him to return to the brothel, perhaps she’d laugh at his absurd notions… and he’d believe her."
"His hand tightened around the fragile sheet. It felt like it weighed its mass in steel." 
"Or perhaps there was another path…"

show rowan necklace naked concerned at midleft with dissolve

"...He could just bury what he knew. Let Shaya go ahead with whatever exciting plans she had for tomorrow. Perhaps even wait for another moment to confront her with what he believed."
"That way, he could continue to see her. He wouldn’t have to risk ruining a good thing, simply because of his suspicions…"

jump shayaSuccumbing
        
#############################################

label shayaConfront:

scene bg9 with fade
show rowan necklace naked neutral at midleft with dissolve

"Rowan shook his head. The entire notion was insane. He couldn’t just forget what he knew. And since when was he too much of a coward to confront a tense situation head on?"
"This had been the entire reason he’d been going to the brothel so often, after all, if he’d finally gotten a piece of information that he could use regarding her relationship with Jezera, then it would have all been for naught."
"And if there was a risk that it would make Shaya upset…"

menu:
    "It was a regrettable necessity.":
        $ released_fix_rollback()
        show rowan necklace naked concerned at midleft with dissolve
        "...It would just have to be worth it. Sometimes it was very easy to forget his mission in the moment when spending time with Shaya." 
        "But, pleasure and good company alone would not deter him from his real goals. It was a risk worth taking."
        show rowan necklace naked neutral at midleft with dissolve
        
    "It didn’t concern him":
        $ released_fix_rollback()
        "...That didn’t matter much, did it? She might be fun to talk to, fun to fuck even...but that didn’t change what he was trying to do. It was a risk he’d take without a second thought."
        
if shayaClue7:
    "Still, there was one other issue that bothered Rowan." 
    "It wasn’t just Shaya’s identity that had bedevilled him, but also her intentions." 
    "Why did she spend so much time and energy lavishing him with attention? Why had Jezera rewarded him with unlimited access to Shaya in the first place? It was as if she didn’t care if Rowan investigated her own spymaster."
    "It was this suspicion that drove Rowan to continue to pour over his notes, long after he should have settled in for sleep."
    scene bg6 with fade
    "The search eventually led him to his work desk and the cabinet he normally used to store important papers."
    "Papers like Shaya’s invitation to the party at the brothel, as well as the original document he’d been given by the cloaked man were soon scattered about it."
    "Tomorrow, he was going to come with real evidence..."
else:
    "Rowan sighed and snuck the parchment back in its hiding place. He was going to need some sleep for tomorrow..."
        
jump shayaUnveiling

###############################################

label shayaSuccumbing:

scene bg24 with fade
show rowan necklace concerned at midleft with dissolve

"Rowan arrived in the morning at the entryway to the brothel. He stopped at its precipice, letting out a heavy sigh. Then he pushed his way into the building."
"The entryway was empty on this particular occasion. There was no attendant at the desk. Yet, Rowan did not have to wait long. The madam herself emerged from behind a curtain of beads."

show shaya neutral at midright with dissolve

sha "Finally, {i}ashallan{/i}, I have been in a state of dread. I had worried you would not come."



"Rowan laughed nervously and ran a hand through the back of his hair. "

ro "I don’t think you had to worry about that. How could I resist?"

"She sashayed close and took his right hand into both of hers. She pulled him along lightly, but with purpose. It amazed him how soft her grip was. Surely such an acrobatic woman would have more arm strength."

ro "Lia isn’t at the desk today?"

sha "There was no need. I waited for you myself."

"She led him, hand in hand, through the familiar back corridor of the brothel. He had anticipated she would turn into her personal room. Instead, she led him all the way back to the door at the end of the hallway."
"The door which was secured with a pair of large, imposing locks."

sha "This is a special room, for sessions of a unique nature. Not just anyone is allowed down here."

ro "I had wondered…"

"She pulled forth a large key ring and pulled out a key as large as her hand. With a shuddering clank, the huge lock fell to the floor. Then she started on the second."
"The moment gave Rowan the briefest chance to reflect. Whatever it was she was planning must have been more special than he could have antici-"
"Shaya gave him a firm nudge to bring his focus back. Then she retreated to the side of the open doorway. It opened to a darkened staircase that descended deeper into the castle."

sha "After you, Rowan."

"Rowan took a deep breath. He’d just have to go along with this. Knowing Shaya, whatever she had planned would blow his mind."
"He stepped into the darkened stairwell."

"The room Shaya took him to could have been mistaken for many in the brothel. It was designed with the same mix of silks and ornate finery. Because it was so deep underground, it was lit mostly by a series of lamps shaped like flowers that bloomed from the wall."
"Three details defined the room. The first was the large pile of cushions in the place of any kind of couch or bed. The second was the large water basin that lined one of the side walls."
"But, most spectacularly, an enormous golden thurible hung like a chandelier from the ceiling, bound by jewel encrusted chains." 
"From small holes along the sides, Rowan could vaguely make out a bundle of herbs in the center. But, he could not determine what type, despite his wilderness knowledge."
"Rowan had seen similar devices for the burning of incense among the rituals of the Imperials when he’d been on campaign with them, but never one so massive."

sha "Very good. If you would please be so kind, would you lay back on the cushions for me? I must prepare everything perfectly for you."

"He was slow to comply with her gentle request. Part of him was curious what she meant by preparing." 
"In this case, it meant opening the hatch of the great thurible and dropping the smallest of flames inside. A small puff of smoke streamed out the sides. It would take time for it to settle down to the air close to the floor."
"From there, she went to the basin and filled a bucket with a silver handle filled with strange pink hewed water. By then, Rowan had finally reclined where she’d directed."
"Next, she drew a chalice from a cabinet next to the walls and poured a mixture of drinks into it. Rowan turned his head to see, but from his seated vantage point, strained to see detail."

show rowan necklace aroused at midleft with dissolve
#shaya naked with veil

"The Brothel Madam shot her head back over her shoulder and gave him a playful wink. Then, her hands pulled her silken top up over her chest. She made a play of a short little dance. But, there was little delay before her remaining clothes lay discarded."

if avatar.corruption > 30:
    "Rowan watched, near salivating. If there was one thing Shaya knew, it was how to be appropriately captivating. Why hadn’t there been anyone like {i}her{/i} back in Arthdale?"
else:
    "Rowan ducked his head away. His cheeks felt like they were on fire. Goddess fend, what was this woman doing to him…."
    
menu:
    "Ask about the room.":
        $ released_fix_rollback()
        "Rowan groaned and shook his head. As much as he wanted to just get lost in the movement of Shaya’s curves, there were still questions that pressed on him."
        ro "What is this place exactly? You didn’t tell me when we were coming down. It looks almost like a lounge…"
        "Shaya half crawled back to him, holding the chalice of liquid in one hand. "
        sha "A ritual chamber. Designed by myself for the sake of a special kind of sensual ceremony. It is said that it was passed down from the ancient Rakhsan’s themselves. But, few know it’s practice."
        "She giggled ever so softly."
        sha "I am one of those few."
        sha "Its intent is comfort of an unparalleled nature. A place where a man can slow his thoughts and utterly escape the tribulations of the waking world. A poet might call it a sanctuary."
        ro "Slow my thoughts? You don’t know how much I have to deal with on a daily basis. I’d be pretty surprised if you could actually do that."
        sha "I must strive to exceed expectations, then."
        "His eyes briefly scanned back to the thurible overhead. More smoke slowly drifted low from it. From its center, the burning incense gave the entire apparatus an eerie glow."
        "Shaya took a kneeling position in front of him, like a servant bowing before a king. With her head lowered, she raised the chalice to him with both hands. Rowan eyed it skeptically."

        
    "Stare in naked lust":
        $ released_fix_rollback()
        "Taking the chalice in hand, Shaya softly crawled the length of the room back to him. Rowan watched every ripple of her muscles. Every jiggle of her well proportioned curves. It was enough to make a man dumb."
        ro "..."
        "When she arrived at the cushions, she lowered her head into the nape of his neck and planted a single gentle kiss. Rowan groaned as she withdrew."
        sha "It warms my heart to see you getting into the spirit of things so fast. And I have not yet even {i}started{/i}."
        "His eyes briefly scanned back to the thurible overhead. More smoke slowly drifted low from it. From its center, the burning incense gave the entire apparatus an eerie glow."
        "Shaya took a kneeling position in front of him, like a servant bowing before a king. With her head lowered, she raised the chalice to him with both hands. /Rowan eyed it with burgeoning curiosity."

sha "For you, Rowan."

menu:
    "Take the chalice.":
        $ released_fix_rollback()
        pass
        
    "Question it":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        ro "I don’t normally like to drink something whose origin I don’t know. Is it wine?"
        "Shaya kept her head bowed low in subservience."
        sha "Not wine, no. It is an elixir of ancient origin. It is vital to the process."
        "Rowan shifted slightly amidst the cushions."
        ro "Are you planning to drink any?"
        sha "I would not dishonour you, that way. I am but the hostess. The {i}Heirophtantessa{/i}. It is not for me to partake."
        menu:
            "Just go along with it.":
                $ released_fix_rollback()
                show rowan necklace aroused at midleft with dissolve
                pass
            
            "Waver further.":
                $ released_fix_rollback()
                "Rowan frowned. He could already sense her disappointment, and it left him on edge. But, so did the knot in his stomach when he looked at its reflective surface."
                ro "You didn’t tell me about any of this. The room. The chalice. I don’t even know what’s in it. How can I just drink it?"
                sha "It is a vital part of the ceremony. All of this, even the mystery, is simply to aid in your pleasure. You have my humble word."
                ro "..."
                sha "Please."
                sha "I would never harm you. Don’t you trust me?"
                "Rowan sighed. The truth was, for all of his confusion, he did trust her. She could’ve poisoned him a dozen times by now. So if she promised him that this was all for his pleasure..."
                show rowan necklace aroused at midleft with dissolve

"Rowan reached out and pulled the chalice from his hands. After inspecting it for a moment, he drained the entire contents in a single gulp. It had a strange bitter taste. Upon his finishing, Shaya dutifully collected it from his grasp."

ro "What now?"

"Shaya crawled away from him, but only so far as to reach the bucket of pink water that she had drawn from the basin at the side."

sha "Undress, please. For the bathing. Fresh spring water treated with herbs and citrus. What is relaxation without a massage?"

if avatar.corruption > 60:
    ro "We could just skip this bullshit and get right to the real fun."
    "The darkness of her room made her expression even harder to read through the veil than normal. But, he had to imagine her smiling."
    sha "Rest assured. We will progress to such delights. But, this is one case where the wait will be worthwhile."
    ro "If you insist. "

show rowan necklace naked aroused at midleft with dissolve

"Under her watching ochre eyes, Rowan pulled his belts away and worked off his clothing. He noted with some amusement just how little different he felt so far. Whatever was in that chalice, it must not have packed much of a punch."
"Finally, he lay back in the cushions naked. Or at least, naked save for the amulet around his neck." 
"He lay back on his hands and glanced once again to the soft glow of the thurible over head. By now, more of the smoke was starting to pool in the lower part of the room. It had an oddly pungent scent for incense. Almost like being in a forest."
"As he pondered it, Shaya crawled back to him. In one hand she carried the ornate bucket of rosewater. In the other a soft towel."

sha "Now, it’s time for the relaxation to begin. Do not worry about what part you must play, Rowan. I will happily guide you."

"Rowan tensed up as she drew closer. Then the moment the wet towel made contact with the skin of his arm, he let out an involuntary sigh. He hadn’t expected it to be so warm..."

sha "It feels good, yes? There is something you can do for me, sweet Rowan. When you feel the warm touch, I wish for you to simply try to breathe. As deep as you can. Can you try for me, Rowan?"

ro "I suppose."

"Shaya purred gently."

sha "Thank you."
sha "But you must remember. Large breaths. Feel the touch of your skin. Then take in air. Hold it, hold it, hold it. Until you are at the crescendo. Then let it all out."
sha "Very simple, yes?"

ro "Yeah."

"Then she moved the towel to his chest and started there. Her movements carried a precise amount of force. Firm enough he could really feel the cloth digging in. But, smooth and gentle as though handling something delicate."
"Rowan opened his mouth. It would feel good to do what she said. He let the air swim into his lungs. Then, when he was ready, he exhaled. His chest rose and fell, even as she washed it."

sha "Very good. Most uncomplicated. Just letting the air in...and letting the air out. Is it not simple and pleasing?"
sha "You needn’t worry about holding yourself up. Let Shaya take care of you. All you must do is breathe. Air comes in. Air goes out."

"For the briefest of moments, her elbow brushed against his manhood. Only the slightest teasing of contacts. It made a long low groan escape his lips."

show rowan necklace naked concerned at midleft with dissolve

ro "Mpph."

"He blinked twice and sank ever so slightly into the cushions. The air around him was getting saturated with incense now. He could almost see particular whisps dancing about him."

sha "It sounds like you found my touch pleasing. Very good. I want to be pleasing to you Rowan. And the best way to do so is to help you relax. To help you to breathe."
sha "In fact...tell me your favorite bird?"

ro "My favorite bird?"

"He groaned. For some reason, when he tried to think about it, it took a second longer than he’d expected. All of this relaxation and care really had been slowing his thoughts. So, he went with the first one that came to mind."

ro "A blackbird, I suppose."

sha "Perfect. It’s exactly like a blackbird. With every new breath in. It is like a blackbird taking flight. With every breath out, it is like a bird floating through the air."

"His chest rose and fell."

sha "Doesn’t that sound so peaceful, Rowan? Just floating through the air. You can almost picture it, can’t you?"

ro "Mhm."

sha "Perhaps as you breathe, you might find yourself feeling more and more like that blackbird. Every time air comes in, soaring higher. Every time air comes out, gliding more serenely. The more you breathe, the more you feel it."

ro "Mhm."

"His eyes fluttered slightly. He really could imagine it. The shape of the feathers, the way it moved over a background of clouds. Almost like he was a teenager again bird watching on a hunt." 
"She’d moved across his pectorals and down his arms, tenderly making sure that there was no spot she missed. With her right hand, she worked the tension from his muscles. With her left, she caressed his skin with the rosewater."
"He groaned slightly and his head rolled. Only now did he realize how much the room had changed. Smoke had been pouring out from the thurible for so long that it now hung in a deep cloud over the room. Even as close to him as she was, Shaya was slightly obscured."

ro "The air is kind of...smokey…"

"Her hands dipped lower, and briefly the cloth touched close to his crotch. All there was between her dexterous hands and his most sensitive of places was a thin line of wet fabric."

sha "All to help you relax, sweet Rowan. You needn’t trouble yourself about such things. I promise it will help you feel good. And you trust me, don’t you Rowan?"

ro "I suppose."

sha "Just focus on the blackbird. Breathing in. Flying through the air. Breathing out. Soaring free through the air. It’s so hard to feel tension when you’re in the air."
sha "And so easy to feel...pleasure..."

"Finally, her hands slipped low. Her left hand brushed down and used the towel along the length of his inner thigh. But, her right hand? It ever so gently, ever so carefully, wrapped around his manhood. He grunted softly."
"He lazily stared at the way her fingers manipulated themselves around him. But, he found focus somewhat difficult. Maybe it was because he was so relaxed, but his vision seemed to rock rhythmically, as if he were on a ship. Nothing stayed still."

ro "It feels…"

sha "Does it feel good, Rowan?"

ro "Yeah…"

sha "Perhaps the reason my caress against your body feels so good is how perfectly relaxed you are beginning to feel. How relaxed every breath makes you feel."
sha "Breathing deeply. A blackbird in flight. And each breath melting into {i}pleasure{/i}."

ro "Mmmhmm."

"Her fingers dragged along the surface of his foreskin. The gentlest of half-strokes. As if the more conversative her movements, the more he felt every change."

sha "More and more. Is it not such an easy thing to just breathe? To feel the air coming out of your lungs. To feel the air coming in?"
sha "Is it not so easy to soar higher and higher with each repetition? To let it turn each breath into ecstasy."
sha "Breathing in. Floating high. So relaxed."

"He opened his mouth to take in air when she reminded him to do so. Each breath grew deeper, as if searching for the limit of how deep his breath could get. The smokey air filled his lungs." 
"With one eye, he peered towards Shaya, through the mist her hand was slowly rising and falling as it worked the length of his shaft. The cloth had been discarded at the side, and her left hand was slowly working its way back up his thigh."
"But, he could only look for a few seconds before it overwhelmed him. His head was swimming, and he couldn’t keep a straight glance."
"His head rolled up slightly, aiming right towards the thurible above. It was funny. He hadn’t realized how colorful its glow had been. It took on a reddish tint...then greenish...then more yellow…"

scene black with fade
show rowan necklace naked concerned behind black
#shaya naked veil
show shaya neutral behind black

ro "My head feels funny…"
ro "Uh..."

sha "But, there’s nothing wrong with that, is there? It is simply the feeling of relaxation overtaking you. Like a blackbird in flight. "
sha "Doesn’t it feel so good?"

"The sound of skin against skin rang in his ears. Shaya’s skillful hands had made an instrument of his cock, and every stroke...every careful touch...was its own elation. The sensation made him float."

sha "And as you breathe in. As you feel so good. It would be natural for you to start to think of a person. A person who is making you feel good?"
sha "A person you desire {i}utterly{/i} at this moment?"

"The words were punctuated by a slight speed up of her movements. But in his overstimulated state, the sensation alone was enough to make him roll his head back and sputter out a groan."

sha "It would be kind of you to say who this person is, blackbird. The one making you feel so good?"

"He opened his eyes again. But the world around him had only grown more strange. Shapes seemed to bleed their edges over. One moment Shaya’s veil was red. The next it was a shade of purple."
"But, through the distortion, he was still able to train his eyes straight on her. Straight on Shaya."

ro "Yes..."

"He breathed deeply."

sha "I’m the one making you feel {i}so{/i} good?"

ro "Uh..."

sha "If that’s the case, I wouldn’t doubt it if you thought of me often. A blackbird flying to my door. I might even be a person who frequently makes you feel that way."

ro "Mmm."

"He let his eyes slip close again and rolled his head back. The distortions were just too much. Nothing was straight or simple. All that remained consistent was the pleasure. The constant sparking waves coming from his crotch. He melted into her touch."
"{i}So good.{/i}"

sha "Perhaps even being in my presence makes you feel calm. Relaxed. Excited. {i}Hungry{/i}. Like a blackbird settling soft and safe into my hands."
sha "You needn’t feel shame from such things. They’re our personal secret. I don’t mind you feeling good. Your pleasure intoxicates me. It makes me feel…"

"She brought her lips close to his ear and let out a coarse moan. It punctuated her own desire."

sha "Mmmm."
sha "So calm. Feeling so so good. A blackbird in flight. A blackbird coming home to me."

"His pleasure was held in her hands. With both hands, she set a steady beat of touches. One cascading into the next. His hips danced to this sweet music."

sha "Mmm. You can barely stand it, can you? I must be making you feel..."
sha "..So...Much...Pleasure..."

"He let himself stare up to the ceiling, his mouth hanging open in rolling guttural sounds. Everywhere there was smoke. So much that he could barely even see the thurible anymore. Amidst it all, he thought he saw a woman’s face. But, whose face was it? "
"But, now it danced in so many colours. As though there were a rainbow of hues assaulting the edges of his vision. All of it spinning around and around in a circle. A cacophony of sights and sensory explosions."

ro "Mmmm…"

sha "I could scarcely imagine how it must feel. A blackbird whose only wish is to settle deep into my arms. Wanting so badly..."
sha "To {i}pine{/i} for me so badly. {i}Ache{/i} for me so badly. Yearn for me so badly. Perhaps even to taste me."

"His hips bucked wildly in desperation. The moment she’d said it, he felt something soft and wet running along the sensitive underside of his shaft. But, when he looked down, her face was still full veiled. Or at least it seemed that way amidst the visual distortions overwhelming him."
"Whatever had happened, he wanted to feel it again."

ro "Fuck…"

sha "There are words that must be said aloud. You know how I am making you feel, sweet Rowan. It’s okay to say it."

ro "Ugh...good…"

"It was all so much. So much colour. So much smoke. So much spinning. And the pleasure...How could a man think like this? How could a man do anything but surrender to the total and overwhelming pleasure? To descend into a spasming doll in her hands."

sha "Mmm. If I’m making you feel so good, you must want me. Want me so badly…"

ro "Yes...want…"

sha "You must feel more comfortable, more at ease, when I’m near. I would understand so completely if being with me put me at ease…"

ro "At ease…"

"His words were punctured by hyperventilating pants. For a moment, he glanced down and it almost seemed as if she had three hands on his cock, all stroking and teasing him."

sha "And if being with someone so beautiful...who you wanted so badly...who made you feel so good...made you feel safe."

ro "Mmm…"

sha "Almost as if it would be so easy to just trust me. To let me do anything to you. Always safe...Always with Shaya…"

"Her words struck like thunderbolts. So seductive and powerful, he could not process them."

sha "Beautiful Shaya...Desirable Shaya...Trusted Shaya…"
sha "...The woman you’d do {i}anything{/i} for..."

ro "What…"

"His eyes strained slightly. Everything was still in an unnatural haze. But, something about the way she’d said that had put a crack in the effect." 
"Was she a woman he’d do anything for? What did she mean by that?"
"Now too, came flooding with it a flicker of emotion. Didn’t it seem odd that everything had become so distorted and colorful? This...this wasn’t normal?"

ro "What are you…"
ro "What are you...doing to me?"

sha "Wha-."

"For a moment, he thought he saw her without the veil...and with a frown on her face. But, he blinked again and her emotions were cloaked again."

sha "You don’t have to worry about anything, Rowan. So relaxed. Feeling so good. Like a blackbird flying to me…"

"He groaned and shifted uncomfortably in the cushions. Something was wrong...something felt wrong..."

ro "Ugh…"
ro "My head...you’re in my head…"

sha "..."

"Suddenly her hands sped up their motion. With her effortless skill and total control over his cock, she soon had it straining and pulsing. Perhaps seconds from release. At once the words from his mouth collapsed into a series of unintelligible groans."

sha "And it would be so natural for you to want that, right? For me to be in your head. Making you feel good. Making you feel calm. Safe in my bosom."

"Suddenly, her hands withdrew. Rowan couldn’t see it amidst the visual distortions, but he felt the sudden and overpowering absence. He whined and bucked his hips, but to no avail. An orgasm that had been seconds away had collapsed."
"But, before he could start to move again, her fingers had refound their place and resumed their commanding strokes."

ro "W-wait…"
ro "No..doing something…"

"He panted and groaned. The spiral was coming back. It was surrounding him. Everything was spinning. But, he didn’t know if he wanted it to be spinning this way. His world was a confusion that he could not put into words."

sha "Interesting."
sha "But, whatever I’m doing is making you feel {i}so much{/i} pleasure, isn’t it? So much pleasure you can’t even stand it."


"Her words were punctured by another withdrawal of her hands. Yet again, Rowan had been seconds from orgasm. And yet again he had been cruelly denied. His eyes shot open, taking in more and more of the swirling technicolour smoke."
"His gaze was drawn into Shaya, and he couldn’t look away. Her body captured him. Even amidst the visual chaos, she was the sole anchor."

ro "Uhh…"

sha "Shh. You know you can’t deny it. The more you try, the more and more good you might even start to feel. Until you’re totally lost in the pleasure. Until you want me to give you more…"
sha "..Until you’re my little blackbird. Totally relaxed. Totally overwhelmed by pleasure. Totally in need of me. Totally trusting me..."

ro "Uhh.."

"His eyes began to flutter again. The last clear thing he saw was Shaya. Everything from her curves to the way her hair shined was perfect..."

ro "Feels good…"
ro "Yes…"

"And so, all of the chaos seemed to sink back away. Everything was still a swirl of colors and smoke. But that was okay. Shaya was here for him. And he trusted her…"
"As if to reward him, he felt the touch of her hand again. Like a frozen land taking in the first spring sun. Her touch was soft and tender. None of the frantic pace of the prior moments. "

sha " And it feels so easy to trust me, doesn’t it?"

ro "Ye..s…"

sha "And you know that the more you trust me, the more good you will feel."

ro "Mmm..."

sha "Very good. Very good. My Rowan. Let me show you just how much pleasure I can make you feel…"

"The pillows made the sound of greater weight being placed on them. Shaya was crawling forward. Momentarily, Rowan too was the subject of greater weight. Unless his eyes were playing tricks on him, Shaya must have been crawling on top of him."
"Her nails pressed down on his chest, digging into his skin. Sweat poured down his neck."

ro "Mmm..."

sha "You know what’s about to happen, don’t you? You can’t hide your need from me. You want to say yes."

ro "Ye.yes…"

"His obedience was rewarded with another flood of pleasure. Shaya took her sweet time lowering herself atop his painfully erect mast. She pushed down and down until his entire cock was buried in her folds. Until her sex was squeezing him from all angles."
"He cried out and bucked his hips in mindless desire. Shaya, meanwhile, answered with a purr of delight."

sha "Ah. That is what you’ve been waiting for, isn’t it? You needed to feel yourself inside me. Mmm. All you wanted..."

"Her hips rolled, but with a teasingly slow pace. It was as if she were making a game of drawing out his need further and further, beyond what he could take."
"Beneath her, Rowan was a sputtering mess. He couldn’t even see her straight. The face behind the veil kept shifting. But always the eyes remained the same. A piercing ochre. They shined at him through the cloud of smoke."

sha "Mmm. Isn’t it so easy to give in to the pleasure? To simply float along like a good little black bird. To feel good with me. To feel safe with me. In your safe little bird cage. So eager for more…"

ro "Uhhhh…."

"He strained, pushing his hips upwards in a desperate pathetic attempt to bring himself to climax. But, sensing his attempt, her movements ground to a complete halt. She even used her body weight to press him down. He was left groaning and panting, but unable to tip himself over."

ro "mu..uhhh."

sha "Soft and Calm. Like a blackbird in flight. Letting me guide you. Letting me control you. Letting me take you to a place where you can be truly happy."
sha "As you listen to my words, you might find yourself floating away to a safe place. A place you’d only go with someone you completely {i}trusted{/i}."
sha "Picture it…"

"When said the words, as if on command, the gears of Rowan’s mind turned into action. He blinked. And when his eyes opened again..it almost like he wasn’t in a smoky room."

scene bg31 with fade
show rowan necklace naked concerned behind bg31
#shaya naked veil
show shaya neutral behind bg31

"He was on a rolling grassy hillside. A forest of pine trees dotted the horizon. Just like in Arthdale."
"And with him, in this safe space, was Shaya...making him feel good..."

ro "Uhhhh…."

sha "Shh. You don’t need to speak, sweet bird."

"She held a finger to his lip."

sha "You might even find that if you try to speak, it would just make you soar even higher into a state of mindless, safe relaxation. Mindless, safe pleasure."

ro "..."

"Rowan settled back into the cushions. He couldn’t speak. He couldn’t think. He could barely even move. The sights and sounds of Arthdale grew clearer with each passing moment. As though he were fading off into its open sky."
"Now that Rowan was fully pacified, Shaya began to ride him anew. Now, even as totally consumed by his need as he was, he did not even attempt to control the pace. She ground down into his straining cock, and his body spasmed beneath her."

sha "So good. Mmm."
sha "All you have to do is {i}trust{/i} me. All you have to do is let go. I will do all the work for you."
sha "You know that all I want is for you to feel good. Ahh!"

"His lips half formed a smile. He tried to speak, but no words came out. That didn’t bother him. He trusted Shaya. She’d make him feel good."

sha "Floating away and floating away. A happy little blackbird Just for me. Mmm."
sha "Breathing deeply."
sha "Every breath, ah, more relaxing."
sha "The more relaxed, the more pleasure. Mmm."

"Even this state was only held by a tether. Shaya gyrating and moaning atop him barely phased him. The Rosarian sun aligned behind her, covering her in golden light."

sha "So much pleasure."
sha "And the more pleasure I make you feel...ah...the more hopelessly eagerly...enthralled by me…"
sha "The more you trust me. The more you {i}need{/i} me."

"The sensation was all that held him down. The stoked fire of his need was his only physical sensation. Shaya was his tether to the ground. And that tether was mere moments from..."

ro "..."

"From..."

sha "Coming together. All at once. About to...to…"
sha "Ahhh!"

"Shaya let out a high pitched scream. In that same moment, the entire world seemed to tighten around Rowan. By now, he was nothing but a subject to the sensation. His straining body could not resist."

ro "...!"

"And suddenly, everything was spinning. Colours were everywhere. He was flying through the sky. His breath turned to hyper ventilated panting. And then, through it all he heard a word."

sha "{i}Blank.{/i}"

scene black with fade

"…"
"…"

#shayas eyes
scene cg953 with fade
show rowan necklace naked concerned behind cg953
#shaya naked veil
show shaya neutral behind cg953
pause 3

"In the center of the sky, a single eye opened. It was tall and its gaze swept over everything. Rowan was inexorably drawn into its shimmering pupil. An ochre eye."
"Then, another ochre eye opened to its right. An equal appeared to its left. Eyes opened everywhere. They formed a kaleidoscope around him from every angle."
"They saw everything. Nothing could be hidden. "

sha "It seems we might be much closer from now on. My black bird. My {i}Row’aca{/i}. "
sha "But, you don’t have to worry about that. You don’t have to worry about anything with me anymore, {i}Row’aca{/i}. You’re going to find it {i}very easy{/i} to trust me from now on."

"His ears rang with a noise almost like a giggle."

sha "And to think you were so close to making an escape. In truth, you’ve almost impressed me. No man has ever awoken once I started. You’re truly amazing."
sha "But, it’s no matter. I’m not going to give you another chance to fly free. In fact..."
sha "You might find the little cocktail of drugs that you just experienced a little...addicting. You needn’t worry much on that account. Your {i}Shay’aca{/i} will always be ready with another dose, when you crave more. "
sha "And you can always trust me to give you more."

"The eyes drilled into him from all sides. For some reason, there was a voice telling him he should be worried. But, it just made him angry. Why should he listen to this liar?"

sha "Mmm."
sha "Don’t you think we should put this new trust between us to the test, {i}Row’aca{/i}?"
sha "Oh! I have it. "
sha "I know about that fascinating parchment you’ve been keeping about me. You don’t have to worry about offending one such as myself, {i}Row’aca{/i}. I know you meant it as flattery."
sha "But, you can show me how much you trust me by telling me {i}everything{/i} you believe you uncovered in your espionage."

"Rowan’s mouth opened. He was struck, in the moment, with one overwhelming desire. He needed to tell her everything. Maybe if he did, she’d be happy with him.."

if shayaClueScore < 7:
    ro "I know….I know nothing…"
    sha "Nothing? Truly?"
    "Her voice sounded almost disappointed. Rowan’s heart sank."
    ro "I’m sorry, Shaya. I...I tried to learn more. But, you were too beautiful. I always just...uh...I lost myself around you…"
    sha "Oh, Row’aca. Flattery will get you {i}everything{/i}."
    sha "But, this is all the better. In Rosaria, do they not say that “ignorance is bliss”?"

else:
    ro "I believe I know that...that you were made?"
    sha "Made?"
    "He strained slightly under the field of eyes, all looking at him expectantly. It was hard to access his memories. He recalled vaguely sitting at his desk for hours the prior night. But, it all seemed so far in the past..."
    ro "The reason you hide your face...Jezera did something to you with her magic….changed you…"
    ro "That’s why...you wear...veil..."
    ro "Wasn’t sure if true...wanted to find out…"
    sha "..."
    "Rowan waited in eager silence. Was that the information that Shaya had wanted to know? Would she be happy with him if he said that? Or did he need to say more?"
    sha "You wished to know? Well, the simplest way to know would just be to ask? After all, you trust my answer, don’t you?"
    ro "Trust…"
    ro "Of course."
    sha "Well, speaking as someone who would know. It’s quite a silly idea, isn’t it? Wouldn’t it be embarrassing to tell another person you believed something so strange?"
    ro "Yes."
    sha "In fact, it might even be better if you forget you ever had such a silly little notion. Don’t you agree?"
    ro "Forget…"
    sha "Good. Such nonsense doesn’t deserve space in your thoughts. Not when there are much more...{i}pleasurable{/i} things you could be thinking about."
    
"Rowan smiled to himself. If that’s what Shaya thought, then it was probably a good point. He trusted her, after all."
"She started speaking more words, but the longer she droned on, the more comprehension seemed to flee Rowan. In truth, he just liked hearing the sound of her voice."
"It really was relaxing…"
"..."

scene bg24 with fade
show rowan necklace naked at midleft with dissolve
#shaya naked veil
show shaya neutral at midright with dissolve

"Rowan awoke with a start. His eyes scanned around the surroundings frantically. For the briefest of moments, he’d believed something crazy. That he was back in Rosaria...his village." 
"He shook his head. Memory was returning to him in pieces. He was in the brothel. He’d come to see Shaya for her surprise. And she had...she had...what had she done exactly?"
"He looked down at the sheets. The location was familiar. The soft and comfortable bed in Shaya’s private room. He turned to the side and spotted another figure lying in bed next to him. It was Shaya, naked save for her veil."
"He smiled. Shaya was beautiful when she slept. Even looking at her was making a quiet calm set over him."

sha "Mmmm. My {i}Row’aca{/i}. You’re awake."

ro "Yeah. The divines alone know how long I was out for. I should probably make my way upstairs soon, lest my absence be missed."

"Shaya smiled at him softly through her veil."

sha "That’s alright. I’m certain that you’ll be back for another visit with me."

#shayas eyes
scene cg953 with fade
#shaya naked veil
show shaya happy behind cg953
pause 3

sha "Very soon…"

"{i}Shaya’s Story Will Continue in Act 2 of Seeds of Chaos.{/i}"

$ shayaTruth = False
$ change_base_stat('c', 10)
return

##############################################################################

label shayaUnveiling:

scene bg24 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan arrived in the morning at the entryway to the brothel. He stopped at the precipice, letting out a heavy sigh. Then he pushed his way into the building."
"The entryway was empty on this particular occasion. There was no attendant at the desk. Yet, Rowan did not have to wait long. The madam herself emerged from behind a curtain of beads."

show shaya happy at midright with dissolve

sha "Finally, {i}ashallan{/i}, I have been in a state of dread. I had worried you would not come."

show rowan necklace concerned at midleft with dissolve

"Rowan laughed nervously and ran a hand through the back of his hair."

ro "I don’t think you had to worry about that. You’ve been on my mind."

sha "There was no need. I waited for you myself."

"Yet, Shaya had not pulled him far before Rowan dug in heels and stopped. After an eager but failed tug, she turned back with questioning eyes."
"She sashayed close and took his right hand into both of hers. She pulled him along lightly, but with purpose. It amazed him how soft her grip was. Surely such an acrobatic woman would have more arm strength."

ro "No Lia today at the desk?"

sha "Rowan?"

show rowan necklace neutral at midleft with dissolve

ro "Shaya. There is something I need to discuss with you. It’s of great importance."

"She smiled softly at him from behind the veil and attempted again, in vain, to playfully nudge him onward. Rowan didn’t budge."

sha "Surely whatever the concern, it is not so pressing as to come before today’s session. I confess that all the time spent in preparation has left me rather...eager."
sha "You wouldn’t desire to deny a working girl her meager pleasures, Rowan. Would you?"

"He shook his head."

ro "Would your back room be a private place for us to talk?"

"Shaya drew her arms back and crossed them behind her back. For the first time since he met her, he saw a moment of pensive hesitation. Such a break from her smooth demeanor."

#shaya angry
show shaya neutral at midright with dissolve

sha "One supposes…"

"Rowan marched with Shaya to her back room. It was to the brothel keeper’s credit that she wasn’t openly pouting. Though, for once, Rowan could sense the frustration from her. "

if avatar.corruption < 61:
    "It almost made him feel bad about interrupting whatever she had planned. Almost."
    
"Upon arrival, she made straight for a small table of refreshments in the corner."

sha "May I get you anything? Fruit? Wine?"

ro "No, thank you."

sha "Then I hope you won’t think less of me for a minor indulgence."

"She returned with a plate of almonds from the east, and sprawled out over one of the fine couches that flanked her low table. Rowan had to hand it to her. She had a talent for picking the most sexually provocative poses to relax in."
"He took a seat across the table from her and began his line of thought."

ro "Shaya, I’ve been fascinated by you. "

show shaya happy at midright with dissolve

sha "I’ve been known to have that effect on people. I pray you don’t hold it against me."

ro "No see: I mean as a puzzle, of sorts."
ro "I don’t normally meet someone and instantly start rushing to investigate them. But, you’re not some normal person. A woman of your background and your predilection for being mysterious was likely to arouse my fascination."
ro "There’s so much you’re holding back at any one moment. Talking to you can become a guessing game. What is the real motive behind your words? How much of the bullshit that spews out of your mouth do you really mean?"

"She lazily snuck an almond beneath her veil."

sha "It’s only proper for me to make myself interesting, don’t you-"

ro "There it is. More bullshit."

"That got her attention. He felt a slight satisfaction at the sight of her eyebrow raised."

#shaya angry
show shaya neutral at midright with dissolve

sha "Careful now, Rowan. I aim to be accommodating in all things, but I prefer to leave the harsher tones for play time. A woman could grow upset."

ro "Alright."

"He sighed and reclined back in his seat."

ro "I’ll get to the point. I think I’ve figured you out. Or at least, I have most of the pieces for it."

sha "Handsomest of heroes, surely you’d find what I have for you more pleasurable than these kinds of word games? A bit of intrigue {i}can{/i} spice the mood, but with what I have prepared-"

"Rowan held up his hand to silence her."

ro "Just let me finish."

sha "..."

"Slowly, Shaya’s eyes relit with their normal fire. In this atmosphere, her response came as half a purr and half a taunt."

sha "I do live to serve. What’s a small indulgence to whet the appetite? We will have {i}so much{/i} time together afterwards to make up for it."
sha "So then, Rowan: what revelation have you come to that’s so {i}pressing{/i}?"

if shayaClue7:
    ro "Two things."
    "He held up a corresponding number of fingers."
    ro "First, the veil you wear. Whenever we’ve met up in the past, it stuck out to me. Why do you refuse to take it off, even in bed together?"

else:
    ro "The veil you wear. Whenever we’ve met up in the past, it stuck out to me. Why do you refuse to take it off, even in bed together?"

ro "I think… I think I’ve figured it out."

"Rowan made out the upturn of her lips into a smirk beneath her veil."

sha "Oh? You wouldn’t be the first man to hazard a guess."

ro "None of the men you’ve been with would have been able to put it together.  Let’s call it an advantage of my unique position."

"He straightened up in his seat and settled his gaze on her. He wanted to have a better view for her reaction."

scene black with fade
#jez smirk
show jezera happy at center with dissolve

ro "You wear it because of Jezera."

scene bg24 with fade
show rowan necklace neutral at midleft with dissolve
show shaya neutral at midright with dissolve

ro "At some point, back in Qerazel, Jezera did something to your face. And whatever she did must have had a profound impact on you."
ro "One of my vaguer notions is that she might have even {i}made{/i} you somehow. With Jezera, you never know for sure."

"Shaya’s reaction didn’t disappoint. Her eyebrow arched upwards and didn’t return to normal."

if shayaClue7:
    ro "The second thing I determined is this. I don’t think you’re telling me the real reason you’ve been having me visit. It’s {i}certainly{/i} not because you like me, specifically."
    ro "I think Jezera ordered you to get close to me. She wanted you to seduce me. To what end, I’m not entirely sure."
    ro "But, what I do know for sure, is that almost all of our meetings have been set up in advance for purposes besides the stated ones. You’ve been manipulating me."
    "In a dainty gesture, she brought her knuckle to the front of her veil and giggled into it."
    sha "I’m not sure which of your theories is more fanciful, Rowan! "

else:
    "In a dainty gesture, she brought her knuckle to the front of her veil and giggled into it."
    sha "And what would give a man of your deductive reasoning such a fanciful idea?"

#sha neutral

sha "Come now. {i}Jezera made me{/i}? Were she my mother, she’d have to be a little older. No?"

"Rowan let her statement hang in the air between them. He eased back into his chair. Her reaction was expected thus far. Nothing that would shake his confidence in his conclusion."

ro "Would you like to hear my reasoning? "

"A lull descended over the conversation. Nonplused by his lack of reaction, Shaya reached out and grabbed another almond. Then, rather than eat it. She tossed it back on the plate and rose to her feet."

sha "This may require wine. Continue, then."

#shaya angry

if shayaClue7:
    sha "Start with your mistrust of my intentions, if you would. I’m eager to hear what schemes this imagined version of myself is engaged in. She sounds like a fascinating character."
    "As she spoke, she poured herself a drink from a pitcher into an ornate goblet."
    sha "Though, in one sense, you are not far off from the truth. You were given our sessions as a reward for your service. "
    sha "I was ordered to please you. Surely you’re not mistaking the relationship between whore and client for something more sinister?"
    sha "But, that doesn’t make our rendezvous insincere. There was no obligation for me to seek out your company, after all."
    "Rowan shook his head forcefully in response. "
    ro "I've mistaken nothing. What you’ve described to me is but a cover."
    ro "All of these sessions have been about making me into a returning customer."
    ro "After all, seduction is your expertise. Your work is getting yourself or your agents close to valuable targets. Then to use that proximity to gather information and manipulate their behaviour."
    ro "I’m the steward of the castle. A valuable asset to Jezera, but one who must be controlled. It makes sense that she’d want to keep close tabs on me. Perhaps to get more leverage."
    "Rowan reached across the table and took one of Shaya’s discarded almonds, popping it into his mouth. He winced slightly; he’d never had an almond before. He’d expected it to be sweeter."
    ro "In fact, it’s fascinating you’d bring up that reward of service. I wasn’t truly the one who discovered the plot. A cloaked stranger came to visit me in the middle of the night and handed me the information that led to Jezera gifting me these sessions."
    "He studied her face to see if it would break with surprise, but her attention remained steady. Did that mean that she already knew? Or merely that she was disciplined?"
    ro "But, you knew that fact already, didn’t you?"
    ro "At the time, I’d thought they’d come to me because Jezera wouldn’t trust them. At the time, I’d asked myself “who would want Jezera to know about the plot, but not to inform her themselves?”"
    ro "But that was the wrong question. Because the person who gave me that information...was you."
    ro "Last night, I cross checked that letter of information with the invitation you’d given me to your party. You told me that the invitation was written in your own hand."
    ro "It was the same hand that wrote both. There were some slight variations to throw off an eyeball analysis, but many of the letters had uncannily similar shapes."
    ro "I think {i}you{/i} were the one who visited me that night."
    ro "And I think the reason you did it was because Jezera wanted an excuse to send me to you for further sessions, but needed a cover so I wouldn’t know the true reason."
    "Shaya tilted her head and took a sip from her wine."
    sha "A fascinating story. Misdirection. Seduction. {i}Betrayal{/i}. Should I be upset that you think me so treacherous, or flattered that you believe me so skilled?"
    ro "Is that a denial?"
    sha "But of course."
    sha "In your charming little tale, you gave no reason to suggest {i}Jezer’aca{/i} was behind it. What should I make of this slander?"
    "Rowan chuckled."
    ro "Well that brings us back to my other accusation, doesn’t it?"
    
ro "I will admit, I’ve been noting down some of what you told me about your life in Qerazel. Some of my other observations as well."
ro "Here is what I pieced together from it."

"By now, Shaya had returned to her repose on the couch. With her free hand, she used an eastern paper fan to cool herself.  Her ochre eyes were trained intensely on her companion."

$ shayaMenuCount = 0
$ shayaJezeraTrust = False
$ shayaJezeraTraining = False
$ shayaVeilStrange = False
$ shayaBodyPerfection = False
$ shayaAppearanceChange = False
$ shayaDebut = False

label shayaEvidenceMenu:

menu:
    "Jezera’s trust in her." if shayaJezeraTrust == False:
        $ released_fix_rollback()
        $ shayaMenuCount += 1
        $ shayaJezeraTrust = True
        ro "Jezera seems to trust you, and that’s very unusual in and of itself. She barely trusts her own {i}brother{/i}. This was what first drew my interest in you."
        if shayaClue2:
            ro "On the first day we met, She went so far as to tell me that you’re the one person she considers trustworthy beyond doubt. An incredibly strong statement of support."
            "She waved her free hand dismissively."
            sha "Surely the cause of your mistrust isn’t that a woman is close to her childhood friend?"
            ro "Jezera doesn’t trust anyone. Certainly not her other childhood friends. So... why does she trust you?"
        if shayaClue4:
            ro "Though, the way you continue to portray your relation with her… that’s not quite true, is it? It’d be more apt to call you lovers in private."
            ro "Or perhaps… a Mistress and her Slave."
            ro "She has her talons in you pretty deep, doesn’t she?"
            "Her eyebrows narrowed slightly."
            sha "A bold thing for a man to make claims about what goes on in private between two people whom he has not seen alone together. One must wonder the {i}source{/i} of such a claim."
            ro "One must."
        ro "You’ve certainly gone pretty far out of your way for her sake. Done things no ordinary person would do for her. Probably some that common standards would call evil."
        ro "Is it so strange for me to think that she’d have tested your loyalty somehow? And that the result of the test was a solidification of her trust in you?"
        ro "But, that’s just the context."
        jump shayaEvidenceMenu
        
    "Jezera’s role in her training." if shayaJezeraTraining == False and shayaClue3 == True: 
        $ released_fix_rollback()
        $ shayaMenuCount += 1
        $ shayaJezeraTraining = True
        ro "There’s the matter of your training as a courtesan. If I did my due diligence correctly, you were trained at the {i}Empress of Waters{/i} brothel in Qerazel."
        if shayaClue1:
            ro "The very building we’re sitting in is a testament to your training. Jezera designed it as an {i}identical{/i} replica of the original building."
        "Shaya took another, careful sip from her drink."
        sha "A fact that I have done nothing to hide."
        ro "Indeed, but I also know how you ended up there. Jezera, who’d been your friend at the time, had arranged it."
        ro "She convinced you to start, she got the assent of the madame. She even paid out of pocket for your training."
        if shayaClue5:
            ro "Though, you didn’t much like your training, did you? You don’t show much hesitation now, but there was a period where you were half being forced into it, weren’t you?"
            sha "Where did you get that silly notion?"
            ro "The way you talked about your apprenticeship; when we were discussing that training song you used. It sounded quite traumatic. "
            sha "You assume much."
            ro "Maybe, but if the methods that were employed on you are half as serious as those you use here... it must have been a trying experience."
        sha "This is all a fascinating stroll through my past. But to what end?"
        ro "Not much. Simply… there was a period of your life when Jezera was {i}very{/i} invested in shaping you for her own aims."
        if shayaClue5:
            ro "...And you weren’t always entirely a willing participant."
        ro "It’s almost enough to make me wonder if you were the one who wanted to be a courtesan in the first place."
        jump shayaEvidenceMenu
        
    "The strangeness of the veil." if shayaVeilStrange == False:
        $ released_fix_rollback()
        $ shayaMenuCount += 1
        $ shayaVeilStrange = True
        ro "Of course, there is the veil. It’s quite a fascinating touch. It gives you an air of mystique; makes you hard to read. I can see why you like it, as an accessory."
        ro "But, you don’t take it off, even in a situation that would warrant it. You’re pretty dedicated to not showing your face."
        ro "I’m sure most men think you’re hiding something under there. Some kind of scar or imperfection? Perhaps you’re hiding features that might be recognized in some way."
        if shayaClue4:
            ro "But, that certainly isn’t true. I happen to know someone who caught a glimpse of you without the veil. And they told me that you’re just as beautiful with the veil gone."
            ro "If that’s the case, why would you still keep your appearance hidden? A beautiful face would actually help you draw in customers."
            "Perhaps unconsciously, her palm went to her cheek. The delicate tips of her fingers pressed gently against the soft material of the veil. "
            sha "{i}If{/i} that’s the case, either I’ve been more lax than I’ve intended. Or perhaps this spy of yours is a liar or was prone to exaggeration? Do you truly believe they would tell you the truth?"
            "Rowan’s eyes narrowed on her."
            ro "With my life."
            ro "Still, I find it fascinating that Jezera is the only one you would purposefully show your face to. "
            "Shaya responded with a very atypical dismissive snort."
            sha "Some ‘mystery.’ I love {i}Jezera’aca{/i} as a sister."
            ro "Most people don’t sleep with their sisters."
        if shayaClue11:
            ro "I, of course, wondered if it was just a custom among whores in the Empire. Or perhaps in the particular brothel where you were trained."
            ro "But, no one I spoke to knew anything about such a tradition in Qerazel. Your refusal to show your face is as strange to them as it is to me."
            "She sighed."
            sha "I could have told you that myself, my friend. Still, what does any of this prove?"
        ro "I think that the veil is there to hide a particular discomfort. It’s not a general or traditional object."
        ro "You’re hiding something. Something you don’t feel totally comfortable with. And you’re hiding it from {i}everyone{/i}."
        if shayaClue16:
            ro "In fact, you’re so uncomfortable, you might even dislike mirrors because of what they show."
        jump shayaEvidenceMenu
        
    "Her bodily perfection." if shayaBodyPerfection == False:
        $ released_fix_rollback()
        $ shayaMenuCount += 1
        $ shayaBodyPerfection = True
        ro "There’s another matter that drew my thinking in this direction."
        ro "At the party, you told Magistors Lirio about a boating accident that left you with a scar on your back. Afterwards, I asked you about the truth of the story. You claimed you hadn’t made it up."
        "She squinted him with lidded eyes."
        sha "Did I? I barely recall."
        ro "You did. But the scar isn’t there, is it Shaya? That night, I looked for it."
        ro "So either you were lying to me at the time, or it had once been there, but is now gone somehow."
        sha "Surely then, by your logic, I must have been lying."
        ro "And yet… it’s more than that."
        ro "You don’t have a single scar, do you? For that matter, not even freckles or birthmarks."
        ro "Your body lacks imperfections. Anything you might have picked up from day to day living. No pox marks, nothing from childhood."
        if shayaClue16:
            ro "No wonder you’re so confident you can prepare for performances with only a slight hint of makeup. There’s nothing to cover."
        sha "Surely this delightful investigation wasn’t just an excuse to compliment my appearance? Although, it is appreciated."
        ro "It’s not natural. Some things, you can hide with makeup and good care. But, it’s almost as if your body is only a few years old."
        "That earned Rowan another laugh from his hostess."
        sha "Your most outlandish accusation yet."
        ro "Not so outlandish when speaking to the closest confidant to one of the most powerful mages I know."
        if shayaClue10:
            ro "A woman who has herself admitted to being used as Jezera’s magic guinea pig in her youth."
        if shayaClue12:
            ro "And whatever the cause, it can’t have been a simple spell either."
            ro "I’m no expert on magic nonsense myself, but I know enough to realize that the kind of power you’d need to make a change like that would be a complex and dangerous force to dabble with."
            ro "It must have been a very intense and invasive process."
        ro "It’d be pretty stupid of me not to draw the straight line from that towards the veil you wear, don’t you think?"
        sha "..."
        "For once, she didn’t have an immediate retort. Rowan caught on to the hesitation immediately."
        jump shayaEvidenceMenu
        
    "A change in appearance" if shayaAppearanceChange == False and (shayaClue8 or shayaClue9):
        $ released_fix_rollback()
        $ shayaMenuCount += 1
        $ shayaAppearanceChange = True
        ro "But, why would Jezera have changed to your appearance? It seems drastic, but the motive is obvious."
        ro "And some things I’ve picked up suggest you had a major makeover at some point."
        if shayaClue13:
            ro "Qerazel is very concerned with matters of that sort, no? I’ve heard that the nobility there prize beauty above all else. Someone who wanted to advance there has good reason to pay close attention to their looks."
        if shayaClue8:
            ro "Consider what you told me about your family. I remember what you said about your family, that they would not even recognize you if they saw you. You meant it {i}literally{/i}, didn’t you?"
            sha "Must you nitpick every word I spoke to you prior?"
            ro "What can I say? You’ve done a good job getting my attention."
        jump shayaEvidenceMenu
        
    "Her debut." if shayaDebut == False and (shayaClue9 or shayaClue17):
        $ released_fix_rollback()
        $ shayaMenuCount += 1
        $ shayaDebut = True
        ro "There’s another incident that’s drawn my interest. At several points, I heard talk of your debut as a courtesan. I think that event was important."
        sha "My debut? What do you know of that?"
        if shayaClue9:
            ro "You told me about it yourself, remember? During my visit over tea time."
            "She retreated from him slightly and reached for her goblet for another drink."
            sha "Ah. I had forgotten."
        else:
            ro "Just what I heard from gossip during the party. You really should have known better than to just let me wander around talking to your customers."
            sha "Evidently."
        sha "So?"
        ro "Just that, if the other conclusions I’ve drawn are true, then there’s a connection. Whenever this change to you happened, it probably happened just beforehand."
        ro "Your debut is an important event for your marketability as a courtesan in Qerazel. One where appearance matters most."
        if shayaClue9:
            ro "Jezera was involved in the process. You said so yourself. She must have been very invested in making sure it went well."
        if shayaClue17:
            ro "But, there’s something about the event itself that was very unusual."
            ro "Most debuts normally happen for a courtesan with years of training and reputation already developed. But, you had your start with nothing. As if you just… {i}appeared{/i} out of nowhere."
            if shayaClue15:
                ro "Your records certainly bear that out. How many clients did you have more than three years ago? I saw almost none."
                sha "Ah, so you’ve snooped through my client records as well? A bold admission. A more spiteful woman might find that upsetting."
                ro "You’re a spymistress aren’t you? Isn’t subterfuge part of the job?"
                "Shaya rolled her eyes."
        sha "This proves even less than your other wild conjectures."
        jump shayaEvidenceMenu
        
    "That's all." if shayaMenuCount > 3:
        $ released_fix_rollback()
        pass
        
"Shaya had let him go on, with only the occasional retort in between. But, now it was time for him to get to the point."

ro "My picture of the specifics is incomplete. But, this is what I {i}do{/i} know."
ro "You’re loyal to Jezera. {i}Very loyal{/i}, to the point you’d do anything for her. Jezera, being Jezera, saw this as an opportunity. Why let the blind loyalty of a subordinate go to waste?"
ro "So she did something to you. And when it was done, you were the ideal agent. Beautiful, seductive, manipulative."

if shayaClue12:
    ro "Whatever she did to you, or made you do, it left your body different from how it had been before. Changed."
    
if (shayaClue8 or shayaClue9) and shayaClue12 == False:
    ro "And when it was done, you were someone else"
    
ro "And whatever this change was, it is connected to why you never remove your veil. "
 
"When Rowan finished his pronouncement he studied the reaction of his counterpart. Shaya merely watched Rowan in silence. The silent pause filled the entire room, leaving the two to simply look into each other’s eyes." 
"So much of Shaya’s thoughts were always hidden behind the veil. Like a wall erected between her and others." 
"Then, Shaya began to speak. Her words came out with the odd pause, punctuated by her soft speaking tone. It was even softer than usual. Guarded perhaps?"
 
sha "-And you believe this tale is truly more plausible than the simple truth that I am a private woman when it comes to intimacy with clients?"

ro "Look around you, Shaya. In this castle, the strange is the mundane."

"She placed her goblet of wine down on the table and straightened up to a proper sitting position. For the first time, their pose mirrored each other."

sha "What if I told you that your mind has wandered in the wrong direction entirely? That perhaps there is a true reason I wear the veil."
sha "...And the reason is that I’m someone {i}quite rightfully{/i} in fear of being recognized."
sha "What if, one day, sweet {i}Jezer’aca{/i} approached a girl whom she had no business befriending? Someone {i}important{/i}. And from that day onward, that girl devoted herself in service to her new blood sister. "
sha "But, every day since then she must hide her identity, lest word of who she was get to the wrong people. Perhaps even her family."

"Rowan studied her closely. The notion would be plausible, in theory, yet something didn’t sit right about it."

ro "I’d wonder, then, why this girl doesn’t take her veil off when she’s alone with me. If it’s a matter of security, then there would be no issue at all. After all, this woman and I would both be on the same side."

sha "..."
sha "Perhaps this woman might wonder if we {i}truly{/i} are on the same side."

"Another silence overcame the room. Shaya stared at Rowan. Rowan stared at Shaya. "
"Was what she had said true? It wouldn’t be out of character for Jezera to bring along a noble girl or some other girl of high standing. And such a rationale might explain all the secrecy about her…"

if shayaClue12:
    "Rowan frowned. No, that couldn’t be the case. After all, it didn’t address the matter of the scar… or lack thereof. What was the nature of her near-supernatural beauty? Simply being someone important wouldn’t explain that."
    
"But, as Rowan considered the matter, Shaya suddenly rose to her feet and gave him a curt bow. Compared to her normal, flowing body language, it was almost rude."

sha "Please be so kind as to excuse me for a moment, Rowan. I had expected our session to be well under way by now, so this conversation is testing slightly."
sha "Once I freshen up, I will gladly return to continue to reassure you."

ro "Of cours-"

hide shaya with moveoutright

"But, Rowan didn’t even have time to finish his reply before the woman was making for the door. Before he could fully process it, Rowan was left alone."

ro "Interesting."

"Two things struck Rowan immediately."
"The first was that her sudden departure meant he had evidently struck a nerve. If she felt compelled to leave so abruptly, then what he’d said to her wasn’t so absurd after all." 
"The second was that she needed time to compose herself. That would not do."
"Rowan stood up out of his seat and started down the hallway after her. As it turned out, finding where she’d gone didn’t prove especially difficult."

show bg24 with sshake

"{b}SMASH{/b}" 
"Rowan stopped at the entrance to the back dressing room. That was where the sound had come from."

#shaya angry
show shaya neutral at midright with dissolve
show rowan necklace shock at midleft with dissolve

"Shaya stood alone, surrounded by shards of glass. One of the tall mirrors that lined the walls of the dressing room lay half-shattered on the floor. She stood there, trembling at attention, arms at her sides as her chest rose and fell."

ro "Shaya..."

"Shaya turned to face him. There was something totally different about her eyes. Their usual serene calm had turned into an intense storm. They bore into him with something approaching hatred."

sha "Get out."

ro "I-"
      
sha "Do you not understand this is a dressing room, Rowan? Isn’t there any type of privacy you know how to respect?"      

"Rowan took a step backwards. Where had this come from? He’d seen brief flickers of emotion back during the conversation, but this was another matter entirely."
"Shaya went to an open chest, pulled out a handcarved string instrument, and flung it at him. It went sailing in a sharp arc through the air. Rowan easily ducked out of the way. The instrument shattered against another of the mirrors and clattered to the floor, leaving a crack behind it."

show rowan necklace concerned at midleft with dissolve

ro "Shaya. Stop. This isn’t like you."

sha "Is it, Rowan? {i}Is it{/i}?"

"He took a step closer. She hunched her back and raised her arms to defend himself. But, he didn’t draw any closer. The question of whether Shaya could fight was a mystery that he had not yet properly answered."

ro "Shaya. {i}Stop{/i}."

sha "I-I said-"

ro "Stop now."

if avatar.corruption < 61:
    ro "Look, I understand you’re upset. I probably would be too in this situation. But, you’re not going to suddenly disprove my theories by breaking your changing room. So how about we just talk about this? You and me."
    
else:
    show rowan necklace angry at midleft with dissolve
    ro "Do you really think you’re going to make me forget everything I learned by throwing a childish tantrum? Frankly, I’m disappointed in you. Stop and think for a second."

sha "..."

"From the corner of her eye, she looked into a segment of the destroyed mirror. Its jagged edges there was a reflection of her, showing her at her most erratic. Her breath rose and fell."

sha "Fine."

"She settled backwards against the mirror. But, her pose was unlike any he’d seen her adopt. Arms crossed over her bosom and one leg over the other. It screamed defiance. She had closed herself off."

show rowan necklace neutral at midleft with dissolve

ro "I have to admit, you caught me by surprise there. That outburst was totally unlike you. I thought you were a calm person."

sha "You have a great deal of thoughts about me. Not all are true. I am - normally - a {i}controlled{/i} person. But I have never been a calm person."
sha "..."

"She brought two fingers to a wide crack in the mirror and traced it along its course. Her eyes followed the polished nails as they slid down along the edges."

sha "Not everything you suggested before was correct…"

ro "Hmmmm?"

show shaya neutral at center with moveinright
show rowan necklace neutral at edgeleft with moveoutleft

if shayaClue7:
    sha "Mistress Jezera didn’t order me to seduce you. I’ve reported your actions to her, as always, but I refrained from mentioning my full role."
    show rowan necklace shock at edgeleft with dissolve
    ro "What-"
    "She turned her head from him, so that their eyes couldn’t meet."
    sha "I decided to bring you to my bed of my own initiative. You stood out as particularly important from the moment of my arrival. So I immediately set to work on a plan to expand my influence with you."
    sha "When I visited you that night in secret, Mistress was unaware of my actions. The evidence had come to me from some of my girls who provide me with regular intelligence reports."
    sha "Afterwards, I had gone to Mistress and pretended to have been unaware of what you’d done. When she asked for my suggestion for a reward, I was the one to propose unrestricted access to my services."
    "She turned her face back to him. Her eyes blazed with a fire he’d never seen from her. Pride. Surety. All things she’d seemed to lack in the past."
    sha "You presume to understand our relationship, but you are as ignorant as a child."
    sha "Mistress doesn’t need to order me to seduce you. If it will make her happy, I will do it of my own will. Without a second thought."
    show rowan necklace neutral at edgeleft with dissolve
    "Rowan took a step back. The bluntness of her words had an impact all on their own. For all of the time and effort he’d put into considering Shaya as a puzzle, had he ever truly seen her as a force onto herself?"
    sha "Now. You want to know about my face, yes? I will tell you about my face."
    
sha "To start with, you should know that what I’ve told you in the past is true. I merely decided there were certain details that were not for you. I really was born to middle-class merchants. I really was in a group of girls of a similar background. And Jezera really did join us."

"She glanced wistfully into the mirror, as if searching for something that wasn’t really there."

sha "There was Ismena, the fashionable one. There was Aysun, the pretty one. There was Makbule, the one who always knew the right thing to say to boys."
sha "And then there was me."
sha "To my face they said I was the clever one. But, I always knew the truth. I was the ugly one. Or at least, ugly by their standards."

"Rowan tilted his head slightly."

ro "That drastic?"

sha "Your little theory would not make much sense had I already been beautiful, no?"
sha "Our dynamic changed when Mistress joined. To us, it was like living in the dark and seeing the sun for the first time. We all loved her. We all worshipped her. Within weeks of joining, there was no dispute that she was our leader."

"Her voice took on a tone he’d never heard from her when she spoke about Jezera. It was loving and reverent. It reminded him most of the way that the high priests spoke of Solansia herself."

sha "But, the others could not see her radiance the way I could. They were always competing. Always seeking their own advantage. And as much as they wished to serve Mistress Jezera, they also wished to use her."
sha "Over time they began to drift away. They had ambitions of their own. Mistress remains in contact with Ismena and Makbule. They remain her agents. But, they have their own lives."
sha "But not me. I told Mistress that I would always serve her. That I would be whoever she wanted me to be. {i}Whatever{/i} she wanted me to be."

ro "So she wanted you to be a whore. But, it didn't turn out well, did it?"

"She sighed."

sha "We were young. We didn’t understand what a truly merciless environment elite brothels are."
sha "I failed her. I could grasp the lessons. But everything was limited by my appearance."
sha "There are things one can learn to give themselves an advantage. How to dress, how to wear makeup, how to do your hair. But, one cannot make the highest quality art without the highest quality materials."
sha "So, Jezera showed me a way to change that."

"Shaya paused to catch her words. She turned from the mirror back to Rowan."

sha "The following is a secret of the highest order. Not merely the truth of the matter, but also that we are aware of it. Were you not already Jezera’s agent, even telling you this would be unthinkable."

"He ran a hand through his hair. A promise to Shaya to keep a secret carried with it more potential dangers than he’d have liked. But, at the moment, there wasn’t a good alternative."

ro "I understand."

"Rowan gave her a reassuring nod."

sha "Perhaps you have heard that the High Lords of Qerazel are renowned for their bodily perfection? "
sha "They would have their subjects believe that it is their superior blood. That they are a higher race, and that this radiance descends through their generations. Perhaps they even imply that Solansia herself had blessed them with her special favour."
sha "Lies. What they hoard for themselves and keep closely secret is magic."

#transformation cg
scene black with fade
show shaya neutral behind black

sha "Beneath Qerazel is a vast reservoir in a secret underground labyrinth. It’s so large it could be called a small lake. I am unsure of the origin, but it must have existed since Rakshan times. And from the waters there is a great white mist that wafts across the chambers."
sha "On the walls there were...it is hard to describe. Jezera called them magic runes. But, they were golden and they lined the exterior like a vast ring."
sha "Those who descend into it are changed. There is a picture of themselves in their head, and they emerge to match it. "

scene bg24 with fade
show rowan necklace shock at edgeleft with dissolve
show shaya neutral at center with dissolve

#IF Seen: NasimGranDisplay. (nasim finale, not yet written) 
#ro "I think I know where this is going…" 
#"Rowan shifted uncomfortably in place, cold sweat running down his neck. Nasim played with fire and got burned for it. If the cursed chamber beneath the castle and the one Solansian Elites were using were in any way, shape or form similar… "
#"Solansia protect them all. He banished the sight of Nasim’s transformed body from his mind, and focused on Shaya again, hoping her answer would prove him wrong. But knowing that likely wouldn’t be the case. "

#else
"Rowan shifted uncomfortably in place. Learning that Jezera was dabbling in dangerous chaos magic would hardly have shifted his worldview. But, the idea that it was the Solansian Elites doing it..."

if aboutTransSeen:
    ro "Wait- “A picture of themselves in their head”..."
    ro "How much do you know about Nasim and his project?"
    sha "Enough to understand the intent behind your question. Your thought has been the same as mine. I’ve ensured he’s under proper surveillance to determine if there are indeed similarities."
    sha "But in terms of the magical arts, my only knowledge is what Jezera has taught me. I am afraid that his work is simply beyond me."
    if castle.buildings["nasim_chamber"].lvl > 0:
        "A lake extolling mist surrounded in golden runes…The similarities to Nasim’s chamber were limited, but the principle sounded almost the same." 
        "But the castle’s resident dark wizard was clear on the chamber’s ties to Kharos’ and his chaos magic. Just what on earth was the Qerazel nobility doing?!"
    else:
        "More questions… Perhaps once they excavate the chamber in the castle’s lower levels, they’ll understand more. This all couldn’t be a coincidence. "
elif aboutTransSeen == False and castle.buildings["nasim_chamber"].lvl > 0:
    "A chamber capable of changing the human body… Why did it sound so unnervingly similar to what Nasim had him uncover in the castle’s lower levels? "
ro "Continue please..."

#transformation cg
scene black with fade
show shaya neutral behind black

sha "It’s unlikely I shall forget that night. We slipped past the guards of the external entrance and through the tunnels. How Mistress learned of this entrance, or even the labyrinth itself, I cannot speak to."
sha "I remember being told how I should picture myself. Jezera had meticulously composed for me the perfect form. One whom men would lose every coin they had to spend time with. With her guidance in mind, I descended into the waters."
sha "And when I emerged…"

scene bg24 with fade
show rowan necklace neutral at midleft with dissolve
show shaya happy at midright with dissolve

"Shaya brought a hand to her forehead and slowly dragged it down the length of her body, all the way to her feet. It was a mockery of a display gesture a hostess might engage in. Her voice raised to a sing-song tone."

sha "Am I to your liking, M’Lord?"
sha "Hehe."
sha "An interesting thing about the transformation: I had not fully considered what my speaking voice would be in this shape. "
sha "But, in my mind, I pictured myself as the perfect courtesan. It is as if the water itself knew what I would consider the voice of the perfect seductress to sound like."
sha "The process was more comprehensive than I could have imagined."

ro "Seems like I’d pieced together most of the story."

"Rowan exhaled sharply. He’d come in reasonably confident about his interpretations. But, to have them vindicated, for the most part, was still a relief."

ro "That new body must have been quite a change for you? Did you resent Jezera for making you go through with it?"

#shaya angry
show shaya neutral at midright with dissolve

"She shot him a dark glare. Her voice immediately went back lower."

sha "Never. And I never shall."
sha "A human body is but flesh and blood. I serve a higher purpose than such things. In this form, I have access to power and influence beyond what I could have {i}dreamed{/i} of in my youth."
sha "Yet, even that pales in comparison to knowing the service I can render her. Who would complain about being made perfect?"

"Rowan went silent now. That he had extracted so much already was a gift. But, perhaps one worth looking at critically. While her words rang true, there was still room for misdirection. Shaya seemed to be off her balance. But, she was still a practiced manipulator."

ro "You’re feeling a lot more talkative all of a sudden. What am I to make of that?"

"She crossed her arms over her chest."

sha "Do not confuse my being upset with turning stupid. You saw what you saw, and learned what you learned. "
sha "I could continue to lie and you would continue to not believe it. Or I could confess and confide. A risky choice, in some ways, but one with great potential upside."
sha "Is it not the common strategy of you military men to cut your losses in a dire situation?"

ro "And what losses would those be?"

sha "A position of friendship to one of the most important men in the castle. One that took months of work to foster."

if shayaClue7:
    ro "If you can be said to be friends with someone who was your mark."
    sha "And yet, in a sense, {i}I{/i} was your mark too. Were that not the case, we would be having a very different conversation right now, Rowan."
    
"She shrugged."

show shaya happy at midright with dissolve

sha "For what’s it worth, I’ve found myself forced to focus on far less appealing targets. You’re not a boring man, Rowan. Nor are you an ugly one. I was not suffering."

"She shot him a weak smile. Even in a situation such as this, her instinct remained to flirt. But she didn't have much of her confident aura. Indeed, for once, she seemed quite frail."
"A hush fell over the dressing room. Shaya's silence seemed driven by vulnerability. Rowan's by indecision."

if avatar.corruption < 61:
    "He was trying to learn about her, and through her learn about Jezera. But it wasn't like he wanted to hurt her."
    
else:
    "Rowan knew an opportunity when he saw one. And Shaya's present state definitely fit that bill. The question was how to capitalize on it."

#CGs will start here
scene black with fade
show rowan necklace happy behind black
show shaya happy behind black

"But, Shaya quickly drew her attention away from Rowan. It was the mirror that gained her interest. The mirror she stared into When she looked at herself, what did she see?"
"Rowan slowly approached Shaya from behind. Without saying a word, he wrapped one arm around her slender waist. The other he brushed against the side of her cheek. The courtesan sighed and leaned into the touch."

ro "There’s still one thing about your story that doesn't track for me. One part I don't think was true."

sha "Are you saying you don't believe me?"

ro "No, no. It's just when you said that you didn't mind the change."
ro "Yet, if you’re so comfortable with your new form. Why the veil? Your face was made to be perfectly appealing to men, wasn’t it?"

"Her eyes flickered between Rowan's reflection and her own."

sha "It was. My new face is...quite beautiful…"
sha "When Jezera constructed how I would look afterwards, she had many ideas for what I could do with it to be more desirable."

"She murmured softly and placed a delicate hand on Rowan's arm. "

sha "But, the end result is...well, I admit that it’s the single aspect I struggle with the most…"

ro "What do you dislike about it?"

sha "Dislike is the wrong word. It’s just…"

"She tilted her head softly away from him. It was the smallest of gaps that could be formed amidst such close contact."

sha "Mmr. You really are a demanding man. Haven’t you already made me speak of too many topics I had intended to remain silent about?"

"Rowan laughed for a moment. Then he got an evil glint in his eye."

ro "Oh I definitely have a demanding side. In fact..."
ro "But, if that’s your answer, you’re going to have to show it to me."

"She blinked."

ro "I want to see your face without the veil. If you've spoken so much about what's beneath. Now I have to see it for myself. "

sha "My face without the veil…"

"For a moment, she paused. Within the narrow confines of his grasp, she swayed back and forth. Her hair brushed against his neck. Finally, she answered him in a quiet voice."

sha "If it will please you."

"Her hand went up to her face. With the quick undoing of two clasps, the thin piece of fabric went drifting to the ground."

ro "..."
ro "You’re beautiful."

"There was little doubt about it. Shaya’s face in the mirror was striking, with its inhumanly perfect proportions, pleasing olive complexion, and soft, slightly parted lips. In a way, it was almost too beautiful."
"Rowan’s hand slid along her cheek, for the first time touching it without any intermediaries. She sighed and leaned into the touch. Yet, her eyes darted away from her own reflection."

sha "...So you say…"

"Slowly, her eyes worked their way back up until she could see herself. She leaned in ever so slightly, staring deeply into the face on the other side. Rowan felt a shiver go down her spine."

sha "You asked why I do not like it."

ro "I did."

sha "It is not that it is ugly. Or that I disagree with my mistress on its merits."
sha "It is simply that it is not me."
sha "Even years later, when I look into a mirror, the woman I see looking back at me is a stranger."

"Rowan brushed his thumb over her lips. They parted slightly to accommodate his touch. "

ro "And yet, it’s your own face."

"She sighed once more. Her head began to lean away again, but this time Rowan held her in place. This way, she wouldn’t be able to escape her own reflection."

if avatar.corruption > 60:
    ro "Look at it."

else:
    ro "You shouldn’t look away, Shaya."

"The moment continued to linger. He felt her lean back into his arms. A motion he responded to by gripping her tighter. Of course, in the process, he felt her backside rubbing very close to his trousers."

sha "I thought you might like to know. You are the first man I've ever willingly allowed to see my face. The second person, in general, after {i}Jezer’aca{/i}."
sha "In a way, it’s almost like being naked."
sha "Though, considering I disrobe around clients so frequently, this is more naked than if I had actually lost my clothes."

"She shivered softly, her cheek brushing up and down against his firm hand."

ro "Would you forgive me if I told you that I don’t mind you being naked {i}in either{/i} way, with me."

"Suddenly, he felt a thud against his ribs. She’d elbowed him, albeit not especially hard."

sha "Men are all alike."

"Though, Rowan had little doubt how she meant it. Had she really been so perturbed by his joke, she wouldn’t still have been pressing herself so close to his body."
"Rowan felt her breath starting to grow hotter. In fact, he could even see the spot of mirror directly closest to her mouth fog up slightly. So, he decided to make the next move."
"With the hand on her cheek, Rowan forced her face towards his. Her eyes and his met. From this vantage point, he could even see the little way she bit her lip. Funny, had she always done that when she was turned on?" 
"It made him want to just lean down and kiss her. So he did."

sha "Mmm…"

"But, the moment the kiss broke, he forced Shaya’s head back forwards. She softly yielded to his touch, letting him guide her body. As expected, when faced with the mirror again, her eyes trained back on her face."
"It left his other hand free to roam her body. He broke his grip on her waist to brush over her belly, her outer thigh, wherever he wished to feel. Shaya responded merely by leaning in wherever he touched."
"All of this was starting to make his own breath come out harder."

sha "Rowan…"

"He broke contact with all but his hand holding her head in place. With the rest, he worked himself free of his belt and trousers. His cock rapidly stiffening from the sensation of pressing to her soft skin."
"Finally, Shaya took matters into her own hands. She worked herself free of her bra, followed in turn by the provocative skirt she wore. But, rather than stop there, she also went to her head piece and the multitudes of armbands she was never seen without."
"It seemed that this time, she was serious about being truly naked."

ro "Are you ready?"

"Shaya turned around within his grasp, wrapping her arms around his neck. Their faces pressed so close that their noses touched. His lips were so close to hears they could feel each breath, each pant, from the other’s lips."
"Then, she jumped into his arms. Her agile legs wrapped themselves around his waist. Rowan stepped forward, pushing her into the mirror behind them."
"Then, Rowan positioned his cock to her entrance. He found it warm and ready for him. There was no challenge slipping it into her. A long sigh slipped out. That too was something new. He’d never properly seen her moan before."
"This time there was little artifice of technique. No elaborate dances or acrobatics. It was merely a man face to face with a woman. A man pressing a woman to a mirror and fucking her senseless."
"At first, the roll of her hips and his forward thrusts were sloppy and sporadic. But the longer he fucked Shaya, the closer their timing got. It was not long before they were in sync. He would drive into her, and she would respond with a moment in turn."
"Their lips pressed together. Rowan invaded her mouth with his tongue just as frantically as his cock invaded her body. The shaking from their frantic liaison was strong enough that it invertebrates down her tongue, into his."
"Without warning, he spun around, driving into the mirror on the opposite side. There was a brief thud as her back hit the wall. But, moments later they were back in the process of furious movement. In the process, they’d overturned another chest and a small stool."
"One hand dug into his hair. The other clawed at his upper back. Rowan winced through the pain, barely even processing it. What was one more sensation amidst the others?"
"She pushed off from the wall, and they fell backwards to the floor. For a moment, Shaya was even on top. She took the opportunity to shift postures, rising to a riding position."
"But, the effort was premature. Rowan immediately shifted his weight, rolling her onto her back. From this position, he was able to press down, slamming the length of his cock as deep as he could. A moment later, her mouth contorted into a wide moan."
"For a moment, he caught sight of the second mirror. There too was a slight crack from the impact. Although, it was far less dramatic than the damage she’d wrought during her earlier rage. Another changing stool lay overturned from their rolling about on the ground. "
"It wasn’t as if the brothel’s madam was about to complain. She was too busy taking his cock. Her hips rolled frantically, and her body seemed to arch and dance beneath him."
"But, that small respite to look around left him with an idea."
"He suddenly pulled himself free from her. Cock strained against the open air, suddenly no longer receiving the constant stimulation. But, that would only be a temporary state of affairs."
"He grabbed Shaya, still sighing and moaning, from the floor and leg her back towards the wall. At first hesitant, his hand in her hair acted like a lead to draw her forward. She slowly began to crawl after him. "

sha "Wait. The mirror."

"Rowan aligned her in front of the mirror. Her face was so close that it nearly touched the surface. Every detail of it would stare back at her the entire time. She tried to squirm out of place, but his hands held her by the hips."

if avatar.corruption > 60:
    "The image was only broken up by a single crack running across the shattered panel. It split Rowan and Shaya’s forms in two."
    ro "Don’t look away. Not for a second."
    
else:
    ro "I want you to look. For my sake."

"Slowly, and with little relish, she brought her face back to level. Her bangs hid one, but the other glanced shyly at her own form. All the while, Rowan settled behind her. He was still more than hard enough to resettle his cock between her legs."
"He let her wait in anticipation for a moment. Her own need was exemplified by the sensation of her juices dripping on him. A bodily plea for him to continue."
"So, Rowan slammed his cock back into Shaya. He held her hips in a strong grip, ensuring that her poor cunt would take every ounce of force."
"Her eyes widened in shock. That was followed by an uncontrolled moan breaking coming from her lips. They both saw every detail of her reaction clearly in the mirror. From her desperate glance to the swell of redness on her normally olive cheeks."

if avatar.corruption > 60:
    ro "Don’t look away."
    "His voice came out in a growl."
    
else:
    ro "Keep looking. I want you to keep looking."
    
"Suddenly, he felt her grow even tighter. Her body clamping down on his mast, as if trying to squeeze out everything inside. Her eyes lost focus, as if they were off in the middle distance."
"To further punctuate the point, he even felt warm liquid...her juices, running down the leg. She’d just cum, but she was still going."
"Still, the reaction of her body had its effect on Rowan. If before, his cock was straining, now it felt on the precipice of explosion. He dug his hand into her hips and used her body for every ounce of pleasure he could."
"All the while, growing closer...and closer...until…"

ro "Shaya…"

"By just a hair, he managed to pull out in time. Instead, a spurt of sticky cum shot into the air. Some of it landed on her back. The rest, however, left a huge stain on the mirror."
"Now, finally satisfied, they both settled down on the floor. Shaya’s hand left a smudge where she’d placed it."

scene bg24 with fade
show rowan necklace naked aroused at midleft with dissolve
#shaya naked happy with no veil
show shaya happy at midleft with dissolve

"And what a result their encounter had left in its wake. As Rowan and Shaya snuggled closer together on the floor, they were left in a swirl of broken mirrors, destroyed stools, overturned personal effects chests, cum puddles, and mirror stains."
"This point was further driven home once they had calmed enough to take back in their surroundings. Still panting, Shaya raised her hand to show Rowan the results of their session."

#shaya naked neutral
show shaya neutral at midright with dissolve

sha "Tsch. In the future, I really must be more careful."

"There was a nasty cut on the back of her palm, running much of its length. Instinctively, Rowan leaned down and kissed it."

ro "Perhaps it will leave a scar?"

"Just, then, Rowan heard approaching footsteps."

#shaya naked with veil

"Shaya scrambled over to her pile of discarded clothes. But, rather than make herself modest, she simply threw her veil back on."
"A moment later, the door opened and two of Shaya’s courtesans entered. But, they stopped in their tracks when they saw the utter devastation that remained of the changing room."

sha "Ahh, girls right on time. My guest and I were right about to vacate the room. Though, we may have made a slight mess. So, please be so kind as to go to the supply closet and retrieve a broom…"
sha "...And a mop…"
sha "And some bandages…"

show rowan necklace happy at midleft with dissolve
show shaya happy at midright with dissolve

"Once Rowan and his host were done recovering their wits and re-adorning their clothes, Shaya moved to escort him back to the entrance of the brothel."

sha "Will you still be returning to visit? I fear you might have fewer mysteries to uncover in future trips."

ro "I still have the reward, don’t I? Free visits to the brothel in reward for my valuable contribution to the castle?"

"She bowed deeply."

sha "Then it appears I will be at your service for a long time to come…"

"But, mid-bow shot a teasing glance upwards."

ro "...{i}Row’aca{/i}."

"Upon arriving at the exit, Rowan hesitated for a moment and turned around. Shaya had already begun to saunter back to her room. She had a comb in hand and was working the tangled strands of her hair."

show rowan necklace neutral at midleft with dissolve

ro "One last thing. It’s something I noticed back in the changing room."

"She turned her head over her shoulder."

sha "Yes?"

ro "I think your discomfort with your new face gives you a lot of pain. But, what I really think hurts you is this."
ro "I think the fact that you’re uncomfortable with it at all, hurts even worse. Because if you were really as perfect a slave for Jezera as you wish you were, you wouldn’t be so negatively impacted by the choice she made for you. And I suspect you {i}really{/i} don’t like thinking about that."

hide rowan with moveoutleft

"Shaya raised her eyebrow. But, by the time she could formulate a response, though, Rowan was already gone."

"{i}Shaya’s Story Will Continue in Act 2 of Seeds of Chaos{/i}."

$ shayaTruth = True
return

###################################################################################################################################
###################################################################################################################################
###################################################################################################################################

label jezeraNTRDetox:

scene bg23 with fade
show xzaratl happy at center with dissolve
show alexia 2 necklace happy at edgeleft with dissolve
show jezera happy at edgeright with dissolve

$ alexiaXzaratlDomTraining = True

al "X’zaratl~~~"

show alexia 2 necklace shocked at edgeleft with dissolve
show jezera displeased at edgeright with dissolve

al "Oh! Jezera, I- "

show alexia 2 necklace concerned at edgeleft with dissolve

je "Is it such a surprise to see me visiting my fellow cubi servants? "

al "No, of course not- "

xz "But it might be surprising to find all of us still clothed. "
xz "I think dear Ulmira still hasn’t found her panties after your last visit, Mistress. "

#jez smirk
show jezera happy at edgeright with dissolve

je "I did do a number on her, didn’t I? "

show alexia 2 necklace happy at edgeleft with dissolve

"The cubi mistress flashed Alexia a quick smile. Jezera was always on edge whenever X’zaratl and her inner circle was involved - but the cubi mistress seemed to know how to appease her - if only for a moment."

show alexia 2 necklace neutral at edgeleft with dissolve
show xzaratl neutral at center with dissolve
show jezera neutral at edgeright with dissolve

je "Oh well, since you’re already here… Alexia, how about you help us with a matter most pressing. Tell me:"

show jezera happy at center with moveinright
show xzaratl neutral at edgeright with moveoutright

je "Red, or black?"

"Reaching into a nearby chest, Jezera brought out a pair of outfits, and held it for Alexia to see. "

al "Are these… Bondage uniforms? "

"There was no mistaking the shiny material and leather straps. Far too skimpy to be anything but fetish outfits, the high heeled boots and tight corset gave them a rather aggressive feel. Alexia wouldn’t be surprised to see a dominatrix in one."

je "Oh, no, no. They’re maid uniforms, for some of X’zaratl’s succubi who agreed to serve me, and will from now on work as the castle’s senior maids. "
je "I thought they deserved suitable outfits, to commemorate their new promotion."

al "They appear to be missing frills. And aprons? "

je "It's a work in progress. But they do have a duster!"

xz "That would be a whip, Mistress."

je "It’s for dirty people, not furniture. "

#al smirk
show alexia 2 necklace happy at edgeleft with dissolve
show xzaratl happy at edgeright with dissolve

je "And I’ll make sure your succubi will make plenty of use of it, X’zaratl. "
xz "I’m sure they’ll enjoy it a great deal, Mistress. They always had a thing for frilly dresses and bondage."

show jezera neutral at center with dissolve

je "And a hint of sensibility I don’t usually see in your coven. Don’t worry - they’ll spread their wings wide under {i}my{/i} tutelage."

show alexia 2 necklace angry at edgeleft with dissolve

"X’zaratl bowed her head in deference. Alexia narrowed her eyes. Shouldn’t she be at least a little angry at Jezera stealing her subordinates from under her? "

if alexiaJezObedient == False:
    show alexia 2 necklace happy at edgeleft with dissolve
    "Then she noticed the small smile X’zaratl was giving her. Perhaps this wasn’t as big of a victory as Jezera thought it was? "

show alexia 2 necklace neutral at edgeleft with dissolve

"Regardless, it didn’t seem like she was going to oppose the idea, and that alone made the castle mistress happy."

show jezera happy at center with dissolve

"Then Jezera raised the two outfits again, looking at Alexia expectedly, and she remembered her earlier question- "


###############################################################

#xzaratl route

"She noticed X’zaratl pointing to the red one, and instantly followed along."

show alexia 2 necklace happy at edgeleft with dissolve

al "Maybe… The red one?"
al "I think X’zaratl’s cubi would appreciate wearing your colours. "

#jez smirk

je "Quite the idea. I like it. I like it {i}very{/i} much."

#jez smirk
show jezera happy at edgeleft with moveoutleft
show alexia 2 necklace happy at midleft with moveinleft

"Pleased with herself, Jezera tossed the black one away, leaving it hanging over the open chest. She headed for the exit - but as she was about to leave, turned around to face them."

je "You know, I think I’ll order them in bulk. There was this one cubi… Sarases? I think she’ll like the heels."

xz "I’ll make sure she is not otherwise preoccupied. I hope the two of you will have a pleasant time, Mistress."

je "Oh, we will. Ta ta! "

hide jezera with moveoutleft
show xzaratl happy at midright with moveinright

"Instantly, she had the other girl in a tight hug, kissing both of her cheeks. Alexia blushed slightly, and after a moment of hesitation, reciprocated."

xz "Alexia, how wonderful for you to visit! Can I help you in any way?"

show alexia 2 necklace concerned at midleft with dissolve

al "I- Shouldn’t you be concerned about… Whatever it is Jezera is scheming? "

xz "Hmm… Should I now?"

"X’zaratl kept her smile wide, but seeing Alexia’s worried expression, it slowly faded away - to a small, enigmatic smirk. "

xz "Sweet Alexia, for bringing the three of us together - you, me and Rowan - I owe Jezzy a debt I cannot repay. If she wishes to recruit some members of my coven for her own goals, and they agree to it, I will not stop either."
xz "Many of these girls have served me faithfully for years, but I understand they have ambitions that cannot be realized whilst staying by my side. I knew one day they would want to leave."

al "Yes, but… For Jezera, of all people?"

xz "If that is their choice, I cannot stop them."

show alexia 2 necklace happy at midleft with dissolve

xz "… But if they change their mind and wish to return at a later date, I will welcome them with a smile and open arms."

"Alexia blinked, then did it again, as she felt tears gather in her eyes. It was such an honest, almost maternal understanding. She didn’t expect to find it anywhere in Castle Bloodmeen."

xz "-And a full month in chastity belts."

al "I think they wouldn’t have it any other way."
al "Your cubi are lucky to have you, X’zaratl."

xz "Oh, Alexia, you’re making me blush. It’s no big deal."

#xzaratl eye flash

show alexia 2 necklace aroused at midleft with dissolve

xz "I always offer love and unconditional support to those who are dear to me."

"Alexia nodded her head, feeling slightly lightheaded the sweet fragrance that always followed the cubi suddenly grew far more noticeable. They were {i}really{/i} lucky to have her… "

show alexia 2 necklace happy at midleft with dissolve

xz "But enough about me. You came here for a reason, did you not?"

show alexia 2 necklace shocked at midleft with dissolve

al "Ah! Well, it’s, um…"

show alexia 2 necklace aroused at midleft with dissolve

al "Ha… A little embarrassing really. "
al "I thought we could… Maybe… Discuss what happened back then…"
al "With the…  Whip? "

"The words barely made their way through Alexia’s lips. Truth be told, she’s done some… Slightly outrageous things in the last few months." 
"But almost getting off to whipping her husband, after he came to her looking for penance,  might be the one that took the cake."

show alexia 2 necklace concerned at midleft with dissolve

al "X’zaratl…?"

"She expected the demoness to say something, but the cubi mistress simply stared at her with an enigmatic smile. Hearing her confused voice, she took a step forward, and grabbed her by the hands."

xz "Yes, sweet Alexia?"

al "Aren’t you going to say anything?"

xz "Only after you tell me one more thing."
xz "You’re here because you want to feel that way again, yes? "

"She blushed, at a loss of words. To be confronted so directly!"

show xzaratl happy at center with moveinright
show alexia 2 necklace aroused at midleft with dissolve

"And the demoness wasn’t finished. She took another step forward, her thumbs gently massaging the back of her hands, and kept talking, her soothing voice as always helping Alexia relax."

xz "Recall that sensation, sweet Alexia. Remember how you felt back then."
xz "Remember how your whip struck Rowan’s body."

#show greyed out whip CG

"{i}Remember how his pained gasps turned to moans of pleasure, how his body trembled with pleasure… Remember how hard his cock grew with every strike, all from the sweet torture you delivered unto him...{/i}"

#show greyed out whip indulgence

"{i}Remember the blazing desire in your veins… The rush of blood… Remember the sensation of power and control that took your body by storm… {/i}"

#return to room
#xzaratl happy center
#al aroused midleft

xz "And tell me - do you want to feel that way again?"

menu:
    "Yes.":
        $ released_fix_rollback()
        pass
        
"There was only one answer. Almost entranced, she found herself nodding along, breathing heavily as all the memories rushed into her mind again. It all felt so good… "
    
show alexia 2 necklace concerned at midleft with dissolve

al "But Rowan… "

"She couldn’t find the courage to finish. The fact she enjoyed herself this much…"

show xzaratl happy at midright with moveoutright

al "… I feel horrible… Taking advantage of his request, and letting myself indulge in such desires. "
al "I cannot phantom asking him for something like that again."
al "Besides, I’m not sure he would be interested. He was always the one taking the initiative in our relationship. Hero of men, and all."

xz "It’s difficult to say no to a man of such renown."

al "It’s the way he carries himself, you know? Like he always has the best solution to every problem, and everybody else could as well be running around with pants on their heads."

xz "All of that is true. But Alexia, my sweetest - you underestimate yourself."

show alexia 2 necklace happy at midleft with dissolve

xz "You are the sun that parts Rowan’s darkness, his hope, his happiness, his reason to go on."
xz "He trusts you - and allows himself to be vulnerable around you in ways he could never be around another. "

al "You say so, but… "

show xzaratl neutral at midright with dissolve
show alexia 2 necklace neutral at midleft with dissolve

al "I know Rowan. He will never relinquish control. Not in full."

xz "Perhaps not now. Perhaps not in the way you want him. But a journey starts with a singular step. Even if Rowan never stops being a hero - even if he never stops struggling and fighting  - there are still things you can try."

show xzaratl happy at midright with dissolve

xz "In the quiet of your bedroom, in the dark of the night… When nobody is watching. Who says you shouldn’t take on slightly different roles, than the ones they all know you by?"

show alexia 2 necklace concerned at midleft with dissolve

al "You make it sound so easy…"

"She looked down, to the chest left by Jezera. She reached to pick up the black uniform - to once examine this bizarre, fetishistic costume." 
"Its material felt slick and cold to the touch. Even if she wore something like this…" 

al "… As if all it would take is to dress up, and ask him to kneel."

show alexia 2 necklace shocked at midleft with dissolve

"Unexpectedly, X’zaratl placed her hands over hers, and made her put the uniform down, shaking her head."

show alexia 2 necklace neutral at midleft with dissolve

xz "The cloth would not convince him. What I believe Rowan needs… Is most of all, to hear you say what you want of him."
xz "If you want to take control... If you want Rowan to submit. If you want him to kneel, you must ask him to do so. Voice your desires Alexia. Have your heart reach his. Is that not what love is all about?"

#else
show alexia 2 necklace happy at midleft with dissolve
al "Do you think this will work?"
xz "It will. If you dread that you might be taking advantage of him… Then all you need to do is make the experience unforgettable for him as well."

xz "I have something that will help. "

"From between her robes, X’zaratl took something out - a small trinket. A ring, Alexia realized.  Dark-red and oddly shaped, with delicate, engraved runes. It shimmered in the flickering light of the sanctum’s torches." 
"It looked too large to fit over her finger - then she realized that wasn’t where it was intended to go." 

if virilityTreatmentSex:
    "Has she seen it before…?"
    
xz "Surprise him tonight. Ask him to strip before you. See him grow hard just from the sight of you, and the orders you give him."
xz "Then, slip it over his cock."

show alexia 2 necklace shocked at midleft with dissolve

"X’zaratl took her hand, and ran her fingertip over the ring’s surface. She felt a rush of energy through her body  - and saw the runes sizzle with small, white flames that quickly died out. "

show alexia 2 necklace concerned at midleft with dissolve

xz "It will increase his sensitivity threefold, and place his manhood in your complete control. He will experience ecstasy like no other - and find no release until you allow it."

al "Threefold... Do you want me to drive him insane with pleasure?"

xz "We only have one night before Rowan must depart again. If we had a full week, then maybe..."

show alexia 2 necklace neutral at midleft with dissolve

"She couldn’t say if X’zaratl was joking or not. The demoness now laid the ring in Alexia’s open palm - holding the back of her hand, as if helping Alexia bear the weight of it. "

show xzaratl happy at center with moveinright
show alexia 2 necklace aroused at midleft with dissolve

"And using it as an excuse to wrap the remaining three hands around her body, hugging her close as she whispered in her ear."

xz "Do you not want to try it, Alexia? "

##if Alexia Indulged during the X’zaratl Guilt solution. AND NOT Jezera NTR
xz "You know how good it felt, making him submit with a whip. Do you not want to do the same with your hands and words alone?"

if virilityTreatmentSex:
    al "The ring… "
    xz "Rowan wore it before, once, as its master. Back then… Were you not pleased with the results, when he impregnated your pussy, time and time again?"
    "She drew a sharp breath. So {i}that’s{/i} where she saw it!"
    if alexiaFuta:
        xz "And if you want, we can have you wear it later as well…"
        
"X’zaratl kept whispering in her ear, stroking her body as the dizzying fragrance that always followed her made it difficult to focus on words alone."

show alexia 2 necklace concerned at midleft with dissolve


"It was such a small thing. Could it really hold so much power over a man?" 
"… Did she want to know?" 
"And did she want to use it on Rowan?"

menu:
    "Dominate Rowan with the ring’s help.":
        $ released_fix_rollback()
        $ AlexiaXzaratlInfluence += 2
        "She closed her fingers around the dark ring, taking in the sensation of its warmth seeping into her skin. Was just touching it having an effect on her as well…?"
        show alexia 2 necklace neutral at midleft with dissolve
        al "… How do we do it, X’zaratl?"
        xz "There is still some time till Rowan is done with his duties. We’ll present him with a nice little surprise once the sun sets."
        scene black with fade
        show xzaratl happy behind black
        xz "But if you do not mind, I do have some pointers to offer…"
        jump detoxWithRowan
        
    "Refuse - you don’t want to take advantage of Rowan’s vulnerable state." if alexiaJezObedient == False:
        $ released_fix_rollback()
        #xzaratl concerned
        show xzaratl neutral at midright with moveoutright
        "With a heavy heart, she gave the ring away."
        al "I’m grateful for the offer, but… "
        al "It still feels like taking advantage of that one moment of weakness he allowed himself in my company."
        al "I can’t. I’m sorry, X’zaratl. "
        show xzaratl happy at center with moveinright
        "The demoness hugged her close, planting a loving kiss on her forehead."
        show xzaratl happy at midright with moveoutright
        show alexia 2 necklace happy at midleft with dissolve
        xz "Why apologize? For loving a man so much you’re willing to sacrifice your own desires for his sake?"
        xz "And people always praise Rowan’s nobility… If only they knew what a golden heart his wife has."
        show alexia 2 necklace aroused at midleft with dissolve
        "She seized her by the chin, and made her look up. The noise of the sanctum seemed to have faded into the background, so only X’zaratl’s eye and voice remained. "
        xz "Can you promise me that if I find a way that lets you indulge such fantasies without feeling like you’re taking advantage of Rowan…  You will consider doing so?"
        "How many times has she found herself in this spot, X’zaratl holding her in her arms, teasing new pleasure for Rowan and her to enjoy? Even if this one crossed the line…If there was a way to do it safely…"
        al "Yes… Of course…"
        xz "That is all I ask of you.  For you to be willing to experience new heights of pleasure with him... "
        scene black with fade
        show xzaratl happy behind black
        xz "And me."
        return
        
label detoxWithRowan:

scene bg14 with fade
show rowan necklace concerned at center with dissolve

"Stifling a yawn, Rowan headed back to his room. His work never seemed to end - but there was no helping it."

show rowan at edgeright with moveoutright

"Finally reaching the end of the corridor, he opened the door gently-"

scene bg9 with fade
show xzaratl happy at edgeright with dissolve
show rowan necklace shock at edgeleft with dissolve
show alexia white neutral at center with dissolve

if RowanXzaratlInfluence > 5:
    show rowan necklace neutral at edgeleft with dissolve
    "… And closed it behind him."
    ro "Continue. "
    "Once, he would be shocked to be greeted with such a display. But he learned to give the demoness the benefit of the doubt, so he waited to hear what she had to say." 
    "But it wasn’t X’zaratl who spoke up."  
    show rowan necklace shock at edgeleft with dissolve
    al "So I have your attention. Good. "

else:
    show rowan necklace angry at edgeleft with dissolve
    ro "I hope there is a good explanation for this, X’zaratl."
    show rowan necklace shock at edgeleft with dissolve
    al "Would you not have me speak for myself, husband?"
    show rowan necklace angry at edgeleft with dissolve
    "He glanced at his wife - then glared again, twice as hard, at X’zaratl. Now he knew the succubus was scheming something - and has already managed to convince his wife to participate in it."
    al "Not everything is a ploy, Rowan. "

show rowan necklace concerned at edgeleft with dissolve

al "We’ll do something different today. Something you’ll agree to, without knowing the full details of."

show rowan necklace neutral at edgeleft with dissolve

ro "And may I know why? "

al "Because it’s something that I want."

ro "That’s all the explanation you’re going to give me?"

show alexia white concerned at center with dissolve

"She shifted her weight from one leg to another. He could see her whole body was tense. Before, he considered the possibility that maybe she was under the effect of some sort of spell - some compulsion that made her say the words."
"But he has seen this expression before. Whenever his wife had to breach a subject she knew he wouldn’t approve of - but still felt the need to do so."

al "Because… I want this. Because it’s important to me. And because you’re the only man I want to do it with."

ro "I appreciate it, but… You’re still dancing around the subject."

show alexia white neutral at center with dissolve
show rowan necklace concerned at edgeleft with dissolve

ro "… This is going to be a painful experience for me, is it not? "

xz "Perhaps a little - and perhaps a little scary too. Maybe improper, in the eyes of some."
xz "But all of it will be done for the sake of love."  

show rowan necklace neutral at edgeleft with dissolve

xz "All Alexia needs from you, Rowan, is for you to be gallant a little while longer. The rewards for doing so… Might be greater than you can imagine. "

if RowanXzaratlInfluence > 5:
    show rowan necklace aroused at edgeleft with dissolve
    "X’zaratl’s one eye was almost glowing from excitement. She stayed behind, appearing strangely subdued. But her pleasant smile and soft words brought a strange sense of comfort. With her here, things could not go wrong."

else:
    show rowan necklace aroused at edgeleft with dissolve
    "X’zaratl’s one eye was almost glowing from excitement. She stayed behind, appearing strangely subdued. But her pleasant smile and soft words brought a strange sense of comfort. "

show rowan necklace neutral at edgeleft with dissolve

al "Rowan, what I’m about to do… I think you will enjoy it very, very much."

"Alexia’s low, serious tone sent shivers down his spine, and not necessarily unpleasant ones. It wasn’t often that she was this determined. If she was pouring all her heart and soul into this…."
"Just what awaited him?"

show rowan necklace concerned at edgeleft with dissolve

ro "Alexia, sweetheart…"

al "We’ve talked enough, dear."
al "Now - strip."

menu:
    "Obey.":
        $ released_fix_rollback()
        $ RowanXzaratlInfluence += 1
        $ change_relation('alexia', 10)
        $ alexiaDomCockringSex = True
        jump detoxXzaratlSex
        
    "Refuse - you’re not going to let yourself be ordered around by your wife.":
        $ released_fix_rollback()
        #xzaratl concerned
        show xzaratl neutral at edgeright with dissolve
        show rowan necklace neutral at edgeleft with dissolve
        "He didn’t move one inch. And every second that went past, made it clear he had no intention of doing so."
        #xzaratl branch
        $ change_relation('alexia', -3)
        show alexia white concerned at center with dissolve
        "Slowly, his wife lost her confidence, fidgeting a little in her spot."
        al "Ah… Hm…"
        show rowan necklace concerned at edgeleft with dissolve
        ro "I’m sorry. I know this was important for you, but-"
        al "I know, I know. Just… "
        show rowan necklace shock at edgeleft with dissolve
        al "Maybe I should’ve worn the outfit after all? And use the whip, maybe…"
        show rowan necklace aroused at edgeleft with dissolve
        "Rowan coughed, blushing ever so slightly. So that was what this was all about."
        show rowan necklace neutral at edgeleft with dissolve
        ro "A one-time thing, I’m afraid. One I am grateful for, but- "
        al "I really was hoping it wouldn’t be one, you know- "
        al "I mean, you were really into it-"
        ro "I know. I know. Look, it’s- it’s a little complicated."
        al "Oh yes, definitely- "
        al "…But still- Really hoping we would repeat it. Not with the whip- at least it wasn’t planned-"
        ro "Y-yeah, I did notice the absence of it."
        al "Unless you requested it?"
        ro "Maybe, but, really- It was a one-time thing I’m afraid."
        ro "… … … Sorry."
        "… … … An uncomfortable silence befell them. X’zaratl coughed in the background, looking slightly embarrassed herself."
        menu:
            "No hard feelings. Invite X’zaratl over for tea.":
                $ released_fix_rollback()
                ro "Well then, now that we have that cleared."
                show xzaratl happy at edgeright with dissolve
                show rowan necklace happy at edgeleft with dissolve
                ro "Tea, X’zaratl?"
                show xzaratl happy at midleft with moveinright
                "Alexia buried her hands in her face, burning with embarrassment. X’zaratl hugged her close, cooing reassuringly."
                xz "Don’t worry… We’ll try to soften him up to the idea. Let’s try again in a year."
                "Alexia nodded her head. Maybe a year from now she won’t recall this humiliation."
                scene black with fade
                show xzaratl happy behind black
                xz "And yes, that would be lovely, Rowan."
                $ RowanXzaratlInfluence += 1
                return
                
            "Ask X’zaratl to leave. This was awkward enough.":
                $ released_fix_rollback()
                #xzaratl neutral
                ro "X’zaratl, if you would be so kind…"
                xz "Of course. I’m going."
                show xzaratl happy at midleft with moveinright
                "Alexia buried her hands in her face, burning with embarrassment. X’zaratl hugged her one last time, before leaving."
                xz "Don’t worry… We’ll try to soften him up to the idea. Let’s try again in a year."
                hide xzaratl with moveoutleft
                "Alexia nodded her head, and watched her leave."
                scene black with fade
                "Maybe a year from now she will no longer recall this humiliation…."
                return
                
label detoxXzaratlSex:

show rowan necklace aroused at edgeleft with dissolve

"The moment of hesitation seemed to stretch into infinity. Finally, slowly, as if his hands were made of lead, he reached for his pants and unbuckled his sword."

show rowan necklace aroused at midleft with moveinleft
show alexia white happy at midright with moveoutright

"Pieces of his armour followed. He made his way to the desk, and placed them at their usual place. Behind him, he could hear excited whispers. He glanced behind."  
"Pressing her body against Alexia, X’zaratl had all four of her hands around his wife. Both giggled at something the demoness had said, and Alexia turned her attention to him again."

#al smirk

"Gone was the hint of nervousness. Her lips parted in a wicked smile. With his permission, she could truly enjoy herself."

show rowan necklace naked aroused at midleft with dissolve

"He was down to his pants by then."

al "So hesitant at first… Now would you look at the sight."

"He knew what she was referring to - the prominent outline of his cock, clearly visible through his underwear. Blushing, he tried to keep what little remained of his dignity."

ro "When you’re that forward about your desires-"

al "It makes you hard after all, doesn’t it, dear? This domineering side of me~~~"
al "X’zaratl, I think my husband might be a bit of a pervert. "

xz "Do not be hard on him, sweet Alexia. What man could stay apathetic, when the love of his life teases such exquisite sexual torture to him?"

al " I haven’t teased anything yet. But I have every intention of doing so."

show alexia white happy at center with moveinright

"She approached him, and trailed her finger over the outline of his cock, still hidden by his underwear. He grabbed the edge of the desk, taking a sharp breath."

al "Remove your underwear, husband."

"He did as ordered - his cock sprung forth, straight into Alexia’s fingers. She brushed it lazily, admiring its hardness - then grabbed it firmly. He stifled a moan, and Alexia chuckled at his reaction."

al "I wasn’t sure if you’d agree. You keep surprising me, Rowan. "

menu:
    "It sounded like a pleasant idea… ":
        $ released_fix_rollback()
        ro "I mean, what man doesn’t enjoy his lover being active in the bedroom…?"
        "His halfhearted attempt at hiding his own excitement earned him a delighted laugh from his wife, who turned to X’zaratl with a wide smile."
        #NTR OFF
        al "Looks like you were right after all. Thank you."
        "X’zaratl lowered her head again, this time in appreciation. With twinkles in her eyes, Alexia pressed her lips into his, locking them in a long, passionate kiss."
        al "Do not worry, my love. You’ll get your wish."
        
    "You don’t mind - and you’re more than willing to do it for her.":
        $ released_fix_rollback()
        ro "I’d slay Kharos himself for you. How could I deny you something so simple?"
        #alexia white shocked
        ro "Not that it’s particularly unpleasant thus far…"
        #NTR OFF
        #alexia white happy
        "She laughed, and her mask of dominance cracked for a moment, revealing a warm, loving smile. Her lips touched his again, in a short, chaste kiss."
        al "It’s not meant to be unpleasant. Not entirely."
        #al smirk
        al "You’ll see soon enough. "
        
show alexia white neutral at midright with moveoutright        
show rowan necklace naked neutral at midleft with dissolve

al "X’zaratl - prepare him."

hide xzaratl
show xzaratl happy at midright with moveinright
show alexia white neutral at edgeright with moveoutright

xz "As you command."

"He saw the succubus reach into her clothes, taking out a long, black rope."

if alexiaWhipRowan:
    "Instantly, he recognized the enchanted whip from before. This time, when the cubi mistress ran her hands through it, the enchanted material started to grow thinner, and even longer. More suited for restraints."
    
else:
    "The cubi mistress ran her hands through, and he saw it grow thinner, and longer. More suited for restraints."
    
xz "Do not worry, gallant Rowan."

scene black with fade
show xzaratl happy behind black

xz "I have… Ample experience."

"..."

scene bg9 with fade
show alexia white happy at center with dissolve

"Alexia played with the ring in her hand, as X’zaratl tied her husband to their bed. A black blindfold was placed over his eyes - and at Alexia’s own initiative, he was gagged with her own panties."   
"She felt giddy. It was… Easy. Almost too easy. Is that all it took? A little push?"
"Had this castle made them all slaves to their lust?"

hide alexia
show xzaratl happy at midright with dissolve
show alexia white happy at center with dissolve

xz "He is ready for you, Mistress."

al "No more “ sweet Alexia”?"

xz "It didn’t seem proper, given the circumstances. Do you mind? "

al "Ha! No… Not really. But a title like that… Must be earned, doesn’t it, dear husband?" 

hide xzaratl with moveoutright
hide alexia with moveoutright

#cg1 - blurred
scene black with fade
show xzaratl happy behind black
show alexia white happy behind black

"Without hurry, she took her place by Rowan’s side. She trailed her hand up his leg, making him shiver as every inch took her closer to the part of his body that demanded her attention most."  
"Standing proud, with a flared tip, his cock twitched like crazy. She wondered if the ring was even needed."  
"X’zaratl must have thought so too, because before she took her own place by his side, she placed a red handkerchief in his right hand, and leaned over to run her fingers through his hair."

xz "Release this if the sensation proves too much."

al "Ha… How considerate of you."

xz "This is all for his sake as well as yours, after all."

#cg1
scene black with fade
show xzaratl happy behind black
show alexia white happy behind black
show rowan necklace naked aroused behind black

"With that, she joined her by Rowan’s other side, lowering her head demurely, as if awaiting orders. Everything was in its place. Everything was as it should be." 
"And she would take her time enjoying herself." 
"Alexia leaned over to blow at the tip of Rowan’s cock, then ran her fingers up it - from the base, to the top. Then again - from the flared, twitching tip, to the base, teasing the spot between his cock and his balls."  
"Then again - this time, wrapping her fingers around it. Rowan moaned, his words muffled by her panties."

al "Still so hard ~~~ I guess getting tied up by X’zaratl was more of a turn-on than not?"

"Another muffled response, and the demoness by her side blushed at being praised. Grinning, she kept stroking his cock. A drop of precum formed at the top, and she wondered…"

menu:
    "Tease him, then use his precum as lubricant.":
        $ released_fix_rollback()
        al "What a pleasant sight… Don’t mind if I make use of it, dear~~"
        "She scooped that lonely drop, and spread it across the taunt skin of his cock. She massaged the base of his cock gently, toyed with his balls - put to use every trick known to her." 
        "More precum formed at the head. She scooped it again, admiring how it stretched between her fingers."

    "Have X’zaratl spit on his cock, then keep stroking.":
        $ released_fix_rollback()
        al "X’zaratl… I wouldn’t want to be rough with his cock for {i}no{/i} reason... Would you mind giving me some lubrication here?" 
        xz "As you wish, mistress."
        "The demoness leaned over his cock, and opened her mouth wide to extend her tongue. Alexia watched, wide-eyed, as saliva dripped from the tip of it, in obscenely copious amounts, coating both her hand and Rowan’s cock."
        al "Literally salivating at the sight of my husband’s cock, X’zaratl? And in such a lewd way, no less…"
        al "Not that I disapprove."
        "The corner of X’zaratl’s mouth twitched, as the demoness tried to smile while keeping her tongue extended. Alexia chuckled to herself, and decided to put that effort to good use."
        
"Running her hand up and down Rowan’s cock, it didn’t take long for it to become slippery and wet, glistening in the evening light.  She wondered how much more could her husband take - and judging by his pained groans, not much."

xz "I think it’s time, Mistress."

al "Oh, I agree ~~"

"Rowan couldn’t see, couldn’t even suspect what his wife had in store. He felt Alexia’s soft hand being taken away-"
"Suddenly, something cold snapped around the base of his cock." 

ro "Mmmh?!"

"Said coldness swiftly gave way to unnatural warmth that filled his manhood, and he shivered as he suddenly felt his cock grow unexpectedly sensitive." 
"His body became numb - every other sensation paled to the sudden pleasure that overtook his cock. He felt everything- every light breeze of air-"    
"Delicate fingers wrapped around his cock again."
"He bucked his hips again, pushing into that soft, wonderful embrace. Ecstasy mounted in his balls, and he found himself chasing the ever-mounting release, moaning and drooling as he was just about to come-" 
"… And not being able to do so."

ro "Mmm-mmmh?!"

"Someone touched his face, and the blindfold was taken off his eyes. For the first time, he could see the source of his torment-"

if virilityTreatmentSex:
    "The black-red ring from before, once more wrapped around the base of his pulsating dick."
    
else:
    "A black-red ring, wrapped tightly around the base of his pulsating cock."
    
"But he could stare for only a moment, as Alexia ran her hand up and down his phallus, and he found his eyes rolling up, overtaken by pleasure. The sensation was incredible - both painful and intoxicating - and it didn’t seem to abate one bit."

al "Ha... He might actually go crazy, X’zaratl."

xz "Not yet. Not from your hand alone, mistress."

al "Almost sounds like a challenge."

"Alexia grinned, still stroking Rowan’s cock, savouring how even the slightest of her touch made him trash in ecstasy." 
"And most of all, enjoying how his fingers desperately clutched the handkerchief. “More, more, more!”, the simple act screamed at her."

al "Since you want it so badly.."

#cg2
scene black with fade
show xzaratl happy behind black
show alexia white happy behind black
show rowan necklace naked aroused behind black

"She pushed herself up, climbing atop of him. Her outer lips brushed the tip of his cock - and she gasped at the pleasant tingle that spread across her body. Surprised, she traced a finger across her lower slits. It was dripping wet."

al "… Wonderful. "

xz "I concur, Mistress."

"She almost forgot about the cubi mistress. With a knowing smile and flushed cheeks, X’zaratl took her place by the bed’s side, watching the situation unfold with glee."
"Alexia could see the demoness’ own cock peek from under the dark dress, waiting to be touched, and saw traces of her pussy juices trailing down X’zaratl’s inner thighs."  
"… And like an obedient little servant, X’zaratl kept all four of her hands placed behind her back, even though she was struggling to keep them from reaching for her privates."  

al "… Is there something you want to say, X’zaratl? Something you, maybe, want to ask permission for?  "

"Alexia tilted her head, trying to sound casual, disinterested at the cubi’s lustful moans. But just that one moment of attention seemed to be more than enough for X’zaratl. The demoness beamed at her, delighted to no end."

xz "I would never dare to impose mistress ~~~ But if you would be so kind…. Can I stroke my cock, as you ride your husbands? Can I finger my cunt, as his manhood parts yours?"

menu:
    "You have a better idea - have Rowan attend to her with his mouth.":
        $ released_fix_rollback()
        $ AlexiaXzaratlInfluence += 1
        al "And leave you out of the fun? No… I don’t think so."
        "She lowered her hips, and her outer lips once more brushed against the tip of her husband’s cock. He shuddered in response. He couldn’t refuse her now. She could ask anything of him."
        al "Rowan, dear…"
        menu:
            "Rowan agrees to suck X’zaratl’s cock.":
                $ released_fix_rollback() 
                $ xzaratlCockSucking = True
                $ RowanXzaratlInfluence += 1
                al "… I know how hard it is for you to just lay down and take it. You’re a man of action. That’s one of the things I love about you."
                al "So how about you show X’zaratl’s {i}cock{/i} some action for a change?"
                "He was nodding his head before he even realized it. His cock kept pulsating, begging for release. His balls felt like they were about to explode - he’d do anything to cum!"
                al "There you go, X’zaratl. Enjoy yourself."
                xz "A-ah~~ Mistress Alexia~~!"
                #cg2 - var 1
                scene black with fade
                show xzaratl happy behind black
                show alexia white happy behind black
                show rowan necklace naked aroused behind black
                "The cubi giggled with delight, and in a moment, Rowan’s vision was dominated by X’zaratl smiling visage. The demoness straddled his head, one hand grabbing him by the hair - another pulling at Alexia’s panties still stuck in his mouth."
                ro "G-ah! A-aaaa-mmm!"
                "He didn’t get to call out Alexia’s name as X’zaratl’s cock was pushed into his mouth. Driven by desire, he started sucking without a thought, rolling his tongue around the tip, lust guiding his actions."
                xz "H-ha, Gallant Rowan! So enthusiastic! You’ll make me cum in no time!"
                al "A-a, I’d advise against that."
                jump detoxRidingHisCock
                
            "Rowan agrees to lick X’zaratl’s pussy.":
                $ released_fix_rollback()
                $ xzaratlPussyLicking = True
                $ RowanXzaratlInfluence += 1
                al "… I know how hard it is for you to just lay down and take it. You’re a man of action. That’s one of the things I love about you."
                al "So how about you show X’zaratl’s {i}pussy{/i} some action for a change?"
                "He was nodding his head before he even realized it. His cock kept pulsating, begging for release. His balls felt like they were about to explode - he’d do anything to cum!"
                al "There you go, X’zaratl. Enjoy yourself."
                xz "A-ah~~ Mistress Alexia~~!"
                #cg2 - var 2
                scene black with fade
                show xzaratl happy behind black
                show alexia white happy behind black
                show rowan necklace naked aroused behind black
                "The cubi giggled with delight, and in a moment, Rowan’s vision was dominated by X’zaratl’s cock. The demoness straddled his head, one hand grabbing him by the hair - another pulling at Alexia’s panties still stuck in his mouth."
                ro "G-ah! A-aaaa-mmm!"
                "He didn’t get to call out Alexia’s name as X’zaratl’s wet slit was pushed into his mouth. Driven by desire, he started lapping at it without thought, parting them with tongue, drilling into it, lust guiding his actions. "
                xz "H-ha, Gallant Rowan! So enthusiastic! You’ll make me cum in no time!"
                al "A-a, I’d advise against that."
                jump detoxRidingHisCock
                
            "Permission granted - if she asks properly.":
                $ released_fix_rollback()
                $ detoxXzaratlSolo = True
                al "What a naughty succubus you are… It makes me suspect this is what you’ve been after all along."
                xz "Not at all, mistress Alexia~~ "
                al "Hm… Maybe if you ask properly…"
                #cg2 - var 3
                scene black with fade
                show xzaratl happy behind black
                show alexia white happy behind black
                show rowan necklace naked aroused behind black
                "X’zaratl’s knees hit the ground before she even finished talking, and the lust drunk succubus looked up to her, pleading as all four of her hands gripped the bedsheets."
                xz "Please, let me touch myself! Please let me pleasure myself as I watch you dominate your husband, Mistress Alexia!"
                "Alexia laughed in delight. How natural it felt, to have succubi begging at her feet!"
                al "If you really can’t help it ~~~ Then fine, permission granted."
                xz "Thank you, mistress~~~! "
                al "Don’t thank me yet-"
                jump detoxRidingHisCock

label detoxRidingHisCock:

al "If you climax before him, you have to leave. And I’m never inviting you here again."

"Alexia rocked her hips slowly, rubbing her outer pussylips against Rowan’s erection. X’zaratl surprised, fearful moan was a most wonderful reaction, and she felt herself grin wickedly."

al "You’re a succubus, after all. What demon are you, if you aren’t able to control your own lust?"

if detoxXzaratlSolo:
    xz "A-aaah, a very happy one, Mistress!"

else:
    xz "A-aaah, ah- a- a very ha-aaa-aappy one, mistress!"

"She turned to look at her, and despite everything, X’zaratl looked almost proud at her. She wondered if she shouldn’t have picked a harsher command after all…" 
"Rowan pushed his hips out, and the enlarged tip of his erect cock almost parted her outer lips." 

al "A-ah! So impatient… Maybe I should torture you some more…"
al "Ah well~~~ This will be your punishment and reward in one. "

"Her own desires making themselves known, she waited no longer. She pushed her hips down, enveloping Rowan’s cock with her womanly lips-" 
"And to Rowan himself, it was as if the gates of heaven had parted. Pleasure radiated through his whole body, making him let out a muffled moan."

if detoxXzaratlSolo:
    xz "A-ah… His expression, mistress… He’s loving it so much~~~"
    
else:
    xz "H-ha, your tongue is going crazy, R-rowan!"
    
"Gasping softly, Alexia took her time rolling her hips, taking his cock deep inside of her. She let herself enjoy the moment, for once seeing no reason to hurry." 
"For once, she felt no sense of urgency. With Rowan’s cock in her complete control, she could take her time enjoying herself in full." 
"Quickening and slowing her pace as she desired, unconcerned with anything and anyone else, she commenced her husband’s wonderful torture…" 

al "Haaaa… Haaa… Ha-ah?!"

"Once more, desire overtook her, and another orgasm rocked her body. Like a wave, it started rising, and rising, until it swallowed her whole."

al "Haaaa… Haaa..."

"Smiling contently, she opened her eyes, and took a moment to again appreciate the lovely sight that accompanied her through the evening."

if detoxXzaratlSolo:
    "X’zaratl still had her hand wrapped around her cock, pumping slowly as precum leaked to the floor, almost forming a small puddle by now."
    
elif xzaratlPussyLicking:
    "X’zaratl rolled her hips gently,  enjoying her husband’s attention, her hands fondling her own body. Alexia leaned to the side - and saw no splash of cum on the wall in front of them."
    "She was abiding by her orders. Good, good…" 

else:
    "X’zaratl rolled her hips gently, thrusting her cock into Rowan’s mouth, her hands fondling her own body. Alexia couldn’t know if she didn’t sneakily cum down her husband's throat… But she had a suspicion the demoness wouldn’t dare to risk it.  "

"As for Rowan himself…" 
"His cock never softened, and as promised by X’zartl, found no release. Her hand reached for his balls, and she held them tenderly. They felt heavy to the touch, aching for release."

if alexiaFuta:
    "She knew how incredible a cock could feel… If what Rowan was going through was even greater than that… It must have been as X’zaratl promised - hell and heaven combined."
    
else:
    "She could only imagine what he was going through… But if what X’zaratl told her was true, it must have been like hell and heaven combined.  "

"And it was. The last few hours felt like an eternity to the man."
"His original reason for agreeing to this has been long gone, washed away by the neverending desire to finally find release. A hundred times, he was tempted to drop the handkerchief in his hand." 
"And every time, he stopped himself, thinking, wondering- how good will it feel, if he just endures a {i}little while longer{/i}." 
"In the end, his patience would be rewarded - it had to be!"

al "What a wonderful picture this is Rowan… If keeping you on edge till the morning sun would let me immortalize it, I could do just that. "

if detoxXzaratlSolo:
    "He trashed in protest, making X’zaratl pull away in surprise. Alexia laughed, and gently squeezed his balls to calm him. "

else:
    "He trashed in protest, making X’zaratl squeal in surprise. Alexia laughed, and gently squeezed his balls to calm him."

al "Just kidding, dear. You’ve been such a good boy, I would be a very cruel mistress to deny you know."
al "I know how much you want to cum - how much that aching balls yearn for release, how much your erect cock wishes to shower me in cum - inside and out."
al "But first…"

menu:
    "Tell him he can climax only if he agrees to impregnate you." if alexiaPotionStolen and promisedFertilityTreatment == False:
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', 5)
        al "I want you to ask yourself… Where would you rather come- into the cold, evening air, or… "
        "-She rolled her hips, and pushed them down, taking his cock all the way inside of her-"
        al "Into my hot, wet pussy?"
        al "Do you not want to paint its walls white?"
        al "Do you not want to fill your wife with your cum, not caring about the consequences?"
        al "Do you not want to give me a baby?"
        "The unexpected words temporarily pulled him out of the lust-filled haze. For this topic to return, right here, right now-!"
        al "Don’t worry about a thing, dear. You just have to hold that handkerchief, while I count down to one, and make you know pleasure like you never imagined."
        al "It’s that easy… Just relax and listen… "
        al "Five…"
        "-She picked up the pace, suddenly filled with newfound vigour-"
        al "Four..."
        "-Her pussy making lewd sploshing sounds, each time she thrust her hips down-"
        al "Three..."
        "-The sounds of X’zaratl exciting gasps reaching his ears-"
        al "Two..."
        menu:
            "Drop the handkerchief.":
                $ released_fix_rollback()
                "… Rowan kept his eyes closed, as Alexia suddenly stopped her thrusting motions. Even the pleasant sensation in his cock couldn’t stop the impending sense of doom."
                if detoxXzaratlSolo:
                    "Alexia was still processing the unexpected betrayal, when X’zaratl climbed the bed, and suddenly pressed his lips against hers, locking them in a passionate kiss."
                else:
                    "Alexia was still processing the unexpected betrayal, when X’zaratl suddenly leaned back and reached for her, pulling her in and locking their lips in a passionate kiss."
                xz "Do not be angered, Alexia. You will conceive. You will bear a dozen of Rowan’s children. This is but the first attempt of many."
                xz "Do not let a temporary setback ruin all you’ve accomplished tonight."
                "Her head felt dizzy, and all that outrage seemed to evaporate in an instant. Suddenly, she could no longer remember what was it that angered her so, and she simply dazed in agreement."
                al "Ha… You’re right, X’zaratl… "
                if detoxXzaratlSolo:
                    "The demoness sunk back to the floor, once more enveloping her cock with her hands- "
                else:
                    "The demoness pulled away, once more giving herself to Rowan’s loving tongue -"
                "Making Rowan wonder if his wife really was so easy to appease. But that thought quickly vanished, when Alexia resumed her thrusts once again."
                $ RowanXzaratlInfluence -= 2
                jump detoxCummingOutside
                
            "Hold it.":
                $ released_fix_rollback()
                al "One."
                jump detoxCummingInside
                
            "Give X’zaratl the privilege." if detoxXzaratlSolo == False:
                $ released_fix_rollback()
                $ RowanXzaratlInfluence += 2
                $ AlexiaXzaratlInfluence += 1
                al "X’zaratl… Since you’ve been so helpful… "
                al "I’ll let you decide when the two of you can cum ~~"
                xz "A-ah! Mistress! You’re too kind!"
                "Alexia chuckled, gently rocking her hips. Maybe she was… But this was all thanks to X’zaratl. She deserved a little reward for it…"
                "She expected the demoness to jump at the chance of finally finding release. But the demoness waited still, enjoying Rowan’s tongue, and cupping his face lovingly as they rushed towards climax."
                xz "Gallant Rowan… Wonderful Rowan… "
                "She whispered tenderly, her hands guiding him to look up into her eye. It seemed to shine in the dark of the room, drawing him in."
                xz "As we both reach ecstasy… I want you to know-"
                xz "I love you. I want you to be happy. I will do everything to make you know joy."
                xz "Find true bliss in this moment."
                xz "Let us cum, Mistress."
                "Alexia grinned, and released the spell holding him." 
                if promisedFertilityTreatment == False:
                    jump detoxCummingOutside
                else:
                    jump detoxCummingInside
             
    "He has to promise to try even more perverted stuff with her.":
        $ released_fix_rollback()
        $ change_base_stat('c', 10)
        al "I want to know… This doesn’t end here…"
        "She kept rocking her hips, suddenly finding in herself a new source of vigour. That’s right… This was just the first night of many… She needed to give him a proper send-off… "
        al "We have so little time together… I want to use it to the fullest! We don’t know what will happen tomorrow, so…"
        al "Let’s do more~~ Messed up stuff like this, my love~~!!"
        "Drunk on ecstasy, she kept running her finger over the hard ring around Rowan’s cock. She knew it could do so much more than keep him on edge… But X’zaratl made her promise not to take it too far~~"
        "Well, a little more {i}pleasure{/i} wouldn’t hurt~~"
        ro "Mmmm~~!!!!!!!! "
        "Violent ecstasy shook Rowan’s body, making him arch his back. This wasn’t- this shouldn’t be- How could his cock feel even better?!"
        al "We’ll try even more perverted stuff together, alright?"
        if detoxXzaratlSolo:
            "He wanted to scream he’ll do anything, but with her panties still in his mouth-"
        elif xzaratlPussyLicking:
            "He wanted to scream he’ll do anything, but with X’zaratl’s cunt pressing against mouth-"
        else:
            "He wanted to scream he’ll do anything, but with X’zaratl’s cock still in his mouth-"
        al "Ah… Right…"
        al "Oh well~~~ I’ll just have to hope I made enough of an impression, love."
        "And with that, she released the spell holding him."
        if promisedFertilityTreatment == False or abandondedPregnancyAspirations:
            jump detoxCummingOutside
        else:
            jump detoxCummingInside
                
    "Thank him for everything - he earned his release. ":
        $ released_fix_rollback()
        $ change_relation('alexia', 10)
        al "I want you to know… That I love you."
        "Gently, she resumed rocking her hips."
        #no NTR
        al "For you to agree… To such a selfish desire of mine… I love you so goddamn much!"
        al "I just hope… This has been a pleasant distraction… For you as well…"
        "And with that, she released the spell holding him."
        if promisedFertilityTreatment == False or abandondedPregnancyAspirations:
            jump detoxCummingOutside
        else:
            jump detoxCummingInside

###################################
label detoxCummingInside:

"The white runes around the ring flared up and fizzled out, and suddenly, he was free again." 
"Alexia pushed herself down, and he exploded inside of her, pouring immeasurable amounts of cum inside of her. Alexia gasped as she felt it spill out of her, barely able to handle the sheer volume of it." 
"It was incredible - all too incredible. Rowan felt his eyes roll up, and he could swear he could see stars. All that pressure - all that tension - suddenly leaving him."
"Drained, and exhausted, he felt himself deflate-"

jump detoxConclusion

####################################
label detoxCummingOutside:

"The white runes around the ring flared up and fizzled out, and suddenly, he was free again." 
"Alexia pulled herself off him, and he exploded all over her, showering her body and dress in milky white cum. The sensation was so incredibly intense, his eyes rolled up, and he could swear he could see stars." 
"All that pressure - all that tension - suddenly leaving him. Drained, and exhausted, he felt himself deflate-" 

jump detoxConclusion

####################################
label detoxConclusion:
    
if detoxXzaratlSolo:
    "Besides him, X’zaratl was finally free to reach her own orgasm. Jerking her cock frantically, she came on the floor, moaning without any sense of shame or reservation."
    "He smiled, just a little. Good. She deserved it too. "
    scene black with fade
    "It was the final thing that crossed his mind, as darkness took him."
    
elif xzaratlPussyLicking:
    "Only to be greeted by a spray of X’zaratl’s pussy juices, and the overbearing stench of cum, as she too climaxed, staining the wall in front of her."
    "He almost chuckled, giving her one last lick, as he thought how the hell were they going to explain that to the maids. "
    scene black with fade
    "… And with that, darkness took him."

else:
    "Only to be rewarded with a cumshot of his own, as X’zaratl came inside his mouth, making him choke on her cum. With the last vestiges of his strength, he sucked it all down, wondering when would this madness end."
    scene black with fade
    ".. The answer proved to be “now,” as right after, exhaustion claimed his body, and darkness took him. "

#rowan eyes closed, alexia eyes open var - TODO
scene cg31 with fade
show rowan necklace naked behind cg31
show alexia necklace naked behind cg31
show xzaratl happy behind cg31
pause 3

"…. Once everything was over, Alexia found herself laying by her husband’s side, running her fingers through his hair, watching him sleep. She couldn’t remember when was the last time he looked so peaceful - she doubted the end of the world could wake him up right now."
"Behind her, X’zaratl was cleaning up the room. The demoness didn’t say a word - didn’t want to disrupt her peace of mind."  

al "… Do you think he’ll ever let this be a regular thing? "

xz "Perhaps. Who knows what the future holds? "
xz "I never thought I’d set my foot in castle Bloodmeen. And yet here I am - helping the two most wonderful people in the world find happiness."

al "Fate can be a twisted thing." 

xz "Indeed."

al "..."
al "I wouldn’t mind… If it was a regular thing." 

"She heard the soft rustling of X’zaratls robes. The demoness grabbed her by the cheek, and gently turned her to look at her. "

xz "Sweet Alexia, you and Rowan are one of a kind. Like gems that shine different colours in sunlight and in the moonlight. Beautiful, unique - ever surprising."
xz "Gallant Rowan is a hero at heart. A part of him will always seek to take the initiative."
xz "But perhaps… From time to time… Another could come to light."

"The gentle hands stroked her face. Despite the role she played today… It didn’t feel bad to be cared for like this…"

xz "And as long as you let me stay by your side. I will do everything to help you discover all those beautiful shades of yourself."

"Her red lips looked so inviting… "

menu:
    "Kiss her.":
        $ released_fix_rollback()
        $ AlexiaXzaratlInfluence += 1
        "She pulled X’zaratl in, kissing her with passion. The cubi was surprised for only a moment, and quickly moved to reciprocate, hungrily tasting Alexia’s lips. "
        xz "I’ll take that as a “yes.”"
        al "Y-yeah..."
        "The demoness offered Alexia one last kiss on the forehead, then left her to rest. "

    "Nod your head.":
        $ released_fix_rollback()
        al "Y-yeah..."
        "She gave her a shy nod. The demoness offered Alexia one last kiss on the forehead, then left her to rest. "
        
scene black with fade

"...Leaving Alexia alone with memories of Rowan’s cock inside of her, and X’zaratl's sweet fragrance still filling the room."

return
