# TODO: maybe
init python:

    # Dark Sanctum Event - Triggers at week end when building is purchased
    event('dark_sanctum_purchased', triggers="week_end", conditions=('week >=4', '"sanctum" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    # Forge Event - Triggers at week end when building is purchased
    event('forge_purchased', triggers="week_end", conditions=('week >=4', '"forge" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    # Intro to Indarah and tavern explanation
    #occurs week tavern is built (when purchased actually)
    event('tavern_purchased', triggers="week_end", conditions=('week >=4', '"tavern" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    # Andras opens the arena
    # Event triggered when the arena is built
    event('andras_opens_arena', triggers="week_end", conditions=('week >= 4', '"arena" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    ##### Breeding pit build scene #####
    #Event triggers when breeding pit is built.
    event('breeding_pit_build_scene', triggers="week_end", conditions=('week >= 4', '"pit" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    # Intro to Shaya and brothel tutorial
    # Triggers the week the brothel is built
    event('brothel_purchased', triggers="week_end", conditions=('week >= 4', '"brothel" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    #greyhide meets alexia
    event('greyhide_meets_alexia', triggers="week_end", depends=('drinking_buddies',), group='ruler_event', run_count=1, priority='pr_story')


label dark_sanctum_purchased:
#Dark Sanctum Event - Triggers at week end when building is purchased

$ RowanXzaratlDominantStart = False
$ RowanXzaratlFriendlyStart = False

scene bg14 with fade
show rowan necklace angry at midleft with moveinleft
show incubus 1 neutral at midright with dissolve
show succubus neutral at edgeright with dissolve

succ "Thought he’d be more muscular."

incu "And taller."

succ "Yes, taller. Can’t believe such a wimp helped kill Lord Karnas."

incu "Inconceivable. And {i}infuriating{/i}."

succ "Definitely infuriating."

show rowan necklace concerned at midleft with dissolve

incu "… But I’d {i}still{/i} fuck him."

show rowan necklace neutral at midleft with dissolve

succ "{i}Oh yes{/i}. Especially when he looks at us this way. Such a nice, {i}hateful{/i} look-"

hide succubus with moveoutright
show incubus 1 at edgeright with moveoutright
show jezera happy at midright with moveinright

je "Alright, you had your fun. Now shoo, Rowan and I have business."

hide incubus with moveoutright

"The cubi made a half bow to the castle mistress, one Rowan thought wasn’t particularly respectful. They scurried off, flashing Rowan predatory smiles."

ro "Already, they swarm the castle like flies."

je "As they should. Now come, I’ll introduce you to their mistress. "

hide rowan with moveoutleft
hide jezera with moveoutleft

scene black with fade

"Jezera’s smile couldn’t be wider as they headed for the newly built Dark Sanctum. With proper demons now being incorporated into their army, the twins’ project was looking less like an orc insurrection, and more like a true invasion."  
"Rowan, on the other hand, kept looking behind his shoulder, trying not to frown. His past encounters with demons of all sorts tended to be short - and violent."

scene bg14 with fade
show jezera neutral at midleft with moveinleft
show rowan necklace neutral at edgeleft with moveinleft

ro "Said mistress - is she one of Karnas’ old servants? She might not like me much if that is the case."

je "Consider yourself lucky - she is not."

show jezera neutral at midleft with dissolve

je "But that doesn’t mean you should treat her lightly. Her coven predates Karnas’ reign, and we benefit greatly from making it part of our forces."

ro "No doubt. I experienced firsthand how sharp cubi claws are."

show jezera displeased at midleft with dissolve

je "Men, always thinking with either their swords and their cocks."

show jezera happy at midleft with dissolve

je "Yes, yes, the cubi are fearsome fighters, but don’t use them for battle if you can avoid it. Many possess magical talent, and I expect Cliohna to put it to good use."

if castle.buildings["brothel"].lvl >= 1:
    je "And you already know what wonders they can accomplish under Shaya’s guidance."
    ro "I suppose."
    show rowan necklace shock at edgeleft with dissolve
    show jezera neutral at midleft with dissolve
    ro "… Wait, who even are the cubi working under Shaya?"
    je "Independent contractors."
    show rowan necklace neutral at edgeleft with dissolve
    ro "You’re telling me there’s a market for cubi spies."
    ro "... And now that I said it out loud, it doesn’t sound that unreasonable?"
    show jezera displeased at midleft with dissolve
    je "There’s a market for everything. But I won’t go into details over the many strings I had to pull to get them on board."
    show jezera neutral at midleft with dissolve
    je "Suffice to say, from now on we’ll be recruiting our agents internally."
    show jezera happy at midleft with dissolve
    
elif ('fiendish_diplomacy' in castle.completed_researches):
    je "But that only skims the surface of their abilities. It’s time we apply what Cliohna already discovered. Built the Brothel - and I’ll show you how to break a country without spilling a single drop of blood."
    je "Plus, there’s someone I want to introduce you to."

else:
    je "But that only skims the surface of their abilities. The cubi can deliver Rosaria to us on a silver plate - if we use them right."
    je "All it will take, is the right person to oversee them, and a plan on how to properly apply their... “Fiendish Diplomacy”."
    je "I will provide us with the former. Make sure Cliohna handles the latter, then have Skordred make the necessary adjustments to the castle."
    
je "Aaand here we are. Now, Rowan - don’t embarrass me in front of the demons. It’s an order."

hide rowan with moveoutleft
hide jezera with moveoutleft

scene black with fade

"Rowan shook his head as Jezera swung the doors to the dark sanctum open. Swelling with pride, she strolled into the chamber with a grin."

scene bg23 with fade

"Pale blue light illuminated Skordred’s latest creation, generously decorated with fearsome gargoyles and lavish beds." 
"Already, it was full of cubi, all busy cleaning, decorating and - of course - fucking. In the middle of it all… "

show jezera happy at midleft with moveinleft
show rowan necklace neutral at edgeleft with moveinleft
show xzaratl happy at midright with moveinright

je "X’zaratl! So wonderful for you to finally join us. The castle becomes you and your sisters. "

xz "Little Jezzy! I must admit, being here is a little… {i}Overwhelming{/i}."  

"In the middle of it all, stood the queen bee, greeting them with a bright smile and open arms. Half of which, Rowan assumed, held items of powers. That alone was reason to worry.  "

show rowan necklace concerned at edgeleft with dissolve

"But it wasn’t what made Rowan desperately fight the urge to draw his sword, just to have something - anything - between himself and the demoness."

show rowan necklace neutral at edgeleft with dissolve

xz "Is this the gallant Rowan Blackwell you spoke of?"

"It was the way the demoness looked at him. Her one visible eye - he could swear it sparkled with gold light - was focused on him, and him alone. As if she saw no world beyond him. "

je "In the flesh. Once “hero of the six realms”, now the man who will help us bring them to their knees."

#jez smirk

je "… And it’s {i}mistress Jezera{/i} now, X’zaratl. "

#jez happy

xz "Of course, Mistress Jezera. "

"All around them, the cubi were slowly stopping their tasks to watch their mistress. Some exchanged knowing looks. Some snickered. One rolled her eyes."

show xzaratl happy at edgeright with moveoutright
show succubus4 at midright with moveinright
show rowan necklace shock at edgeleft with dissolve
show jezera displeased at midleft with dissolve

"And another suddenly jumped down from one of the gargoyles she was lazing on, kneeling before X’zaratl for a moment, then springing up with a twirl."

show rowan necklace neutral at edgeleft with dissolve
show jezera happy at midleft with dissolve

second "{i}Mistress{/i} Jezera!  Oh, they grow so fast! "

show jezera displeased at midleft with dissolve

second "It feels like just yesterday you were moaning my name! And that was with just one finger. "
second "Will you be joining us for the welcome orgy? I’ve been waiting to make you squeal again."

show jezera happy at midleft with dissolve

je "And a good morning to you too, Ishta."

show rowan necklace shock at edgeleft with dissolve

je "Rowan, be so nice and acquaintance yourself with X’zaratl. It appears I have a point to make."

hide succubus4 with moveoutright
hide jezera with moveoutright
show rowan necklace angry at midleft with moveinleft
show xzaratl happy at midright with moveinright

"... And just like that, she was gone. He suppressed a groan - sometimes Jezera was all too easy to bait."

show rowan necklace neutral at midleft with dissolve

"X’zaratl had yet to take her eye off him. He wondered why did the succubus hide the other side of her face with a cowl - only to push the thought aside." 
"There would be time to investigate - for now he had to figure out where he stood with the cubi Mistress."  

menu:
    "Keep your head high. She answers before you - not the other way around.":
        $ released_fix_rollback() 
        $ RowanXzaratlDominantStart = True
        ro "A pleasure to make your acquaintance, X’zaratl. I’ll give you some time to settle in. Then, meet in my office in the evening, so we can discuss your duties."
        xz "Whatever you command, gallant Rowan."
        
    "Show her respect. This was her coven after all.":
        $ released_fix_rollback() 
        $ RowanXzaratlFriendlyStart = True
        "He bowed his head, slightly. Enough to show respect - but not subservience."
        show rowan necklace happy at midleft with dissolve
        ro "A pleasure to make your acquaintance, Mistress X’zaratl. Please contact me once your coven settles in. We’ll have to discuss the full extent of your duties."
        xz "Of course. But I beg you - call me X’zaratl."
        show rowan necklace neutral at midleft with dissolve

xz "And the pleasure is {i}all{/i} mine."

show rowan necklace concerned at midleft with dissolve

"A flick of a wrist - that’s all it took for the cubi to vacate the chamber, leaving him alone with their mistress-"

#rowan battle pose
show rowan necklace angry at midleft with dissolve

"Who, in just one step, was right in front of him, biting her lips excitedly, almost giggling. Alarmed, he grabbed his sword - only for X’zaratl to rest her soft hand on its handle, preventing him from drawing it."

xz "Oh, Rowan, there is no need for that. I won’t hurt you."

#flash xzaratl's eyes yellow

show rowan necklace shock at midleft with dissolve

xz "I’d never hurt you. You’re the reason I’m here."

if RowanXzaratlDominantStart == True:
    "Her voice sounded so earnest, and her expression seemed so innocent, that he {i}almost{/i} believed her."
    show rowan necklace angry at midleft with dissolve
    "Keeping his expression unreadable, he  discreetly reached for the dagger tucked behind his back - just in case."
    
else:
    "Her voice sounded so earnest, and her expression seemed so innocent - if it was a trick, he never saw it executed so flawlessly."
    show rowan necklace happy at midleft with dissolve
    "As they were supposed to be allies, he let himself relax, just a little. She didn’t take her hand away - and instead took the opportunity to intertwine her fingers with his, smiling happily."
    
xz "I had Jezzy tell me {b}everything{/b} about you. Twice- thrice even! I almost couldn’t believe my ears!"
xz "Rowan Blackwell. Hero of the six realms. Saviour of Karst. Slayer of the Demon Lord himself. So many titles. So many deeds. So many troubles and tribulations."
xz "And all of them to protect your childhood sweetheart! You travelled to the end of the world just to keep her safe! Faced unimaginable horrors so she would never have to! Oh, Rowan, it’s all so unspeakably incredible! "

show rowan necklace shock at midleft with dissolve

"He blinked, surprised. Is that how some people saw it?"

show rowan necklace neutral at midleft with dissolve

xz "Tell me, how is she called? The redhead maiden of Arthdale?"

ro "… You mean Alexia?"

xz "Alexia. Such a beautiful name. {i}Alexia{/i}. For Alexia. Everything for Alexia."  
xz "For Alexia, you traversed the treacherous Rakshan wastes with only a blade by your side and a cloak on your back. For Alexia, you endured tortures and imprisonment, not once giving in to despair. "

#xz displeased
show xzaratl concerned at midright with dissolve

"Her fingers poked the amulet on his neck. She scowled at it."

xz "For Alexia, you dance with death every day."

show xzaratl happy at midright with dissolve

xz "Such devotion. Such {b}love{/b}." 
xz "It’s people like you that make this world so wonderful! To be part of it all- to just {b}be{/b} here, near you-"

show xzaratl aroused at midright with dissolve
show rowan necklace shock at midleft with dissolve

xz "Oh, Kharos punish me, I’m getting {b}hard{/b} already-"

"Rowan peeked down - and stared right at the considerable tent the demon sorceress was pitching under her robes. So this wasn’t just a figure of speech."

ro "I-"

#xz aroused
show xzaratl aroused at center with moveinright
hide rowan
show rowan necklace aroused at midleft with dissolve

"She placed a finger on his lips, silencing him. "

xz "Please, don’t say a thing. I know this is all new. Maybe a little strange. But don’t worry - I’m a woman down there too."
xz "And it’s not important right now. What {b}is{/b} important is that you to know this-" 

#flash xz eyes gold
xz "The bond between you and Alexia is a wonderful thing, and the only thing that matters to me here. I will do everything in my might to see it grow and blossom."

if RowanXzaratlDominantStart == True:
    "A feeling of warmth spread through him. There was a subtle, sweet scent around the succubus, that made him feel slightly lightheaded. How did he not notice it before?"
    show rowan necklace angry at midleft with dissolve
    "And why did he allow her to get so close?"
    show xzaratl at midright with moveoutright
    "… Suddenly, he was free of it, as the Succubus mistress drew back. She flashed him another radiant smile, and brushed her hand against her crotch, struggling to suppress yet another moan."
    
else:
    "A feeling of warmth spread through him. There was a subtle, sweet scent around the succubus, that made him feel slightly lightheaded. He found himself leaning in, wanting to feel more of it."
    show xzaratl at midright with moveoutright
    show rowan necklace concerned at midleft with dissolve
    "… And just like that, he was suddenly denied it, as the Succubus mistress drew back. She flashed him another radiant smile, and brushed her hand against her crotch, struggling to suppress yet another moan. "

show rowan necklace neutral at midleft with dissolve

xz "But for now, I have to make sure Jezzy and Ishta start getting along. And you should rest. Rest, and gather your strength. And tell fair Alexia to do the same."

scene black with fade
show xzaratl happy behind black

xz "There is just so {b}much{/b} I want to show you."

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label forge_purchased:
#Forge Event - Triggers at week end when building is purchased

scene bg11 with fade
show andras displeased at trueedgeleft with dissolve
show rowan necklace neutral at midleft with dissolve

an "The renovations to the Forge are complete."
an "Just in time, too. My men were getting antsy with these rusty cleavers."

"Rowan didn’t respond. A dark cloud hung heavy over his thoughts."

an "Well? Are you going to say anything, or is gazing at your navel really that fascinating?"

ro "Bloodmeen’s Forges made most of Karnas’ weapons during the war."

show andras happy at trueedgeleft with dissolve

an "-And now the forge is ours. A fitting legacy, I think. Father would be proud."

ro "If you say so."

an "Don’t be such a glum bastard. Come, meet the new forgemaster with me."

ro "Why?"

an "Because you’re my servant and I said so. Do I need to drag you by the ear?"
an"Don't worry, I’m sure you’ll get along fine. The old fool’s almost as much of a glum bastard as you are."

show rowan necklace angry at midleft with dissolve

ro "Hmmh…"

scene bg22 with fade
show andras displeased at trueedgeleft with dissolve
show rowan necklace neutral at midleft with dissolve

"Andras stepped into the heated hell of the forge with the confidence of a man walking through fire."

an "{i}Forgemaster{/i}! Cease your hammering and come meet my castellan."

"The hulking figure at the head of the forge paused in his work. He set down his hammer, wiping at the soot in his fur as he rose to his fulll height."

show greyhide neutral at cliohnaright with dissolve
show rowan necklace shock at midleft with dissolve

an "This is him. This beast will be our forgemaster from here on."

"The great minotaur simply stood there, accepting the insult without any reaction."

an "Sort out your introductions, servants. Then show him the forge."

hide andras with moveoutleft

"And with that perfunctory introduction out of the way, Rowan was left alone with the largest Minotaur he’d ever seen. He studied the large bull in silence."
"There was an aged quality to his features. Not old, exactly, but weathered with experience and a hint of world-weariness."
"He moved with a sort of deliberate care, shoulders slumped and body hunched, as if conscious of the impact his imposing presence had upon others."
"The bull, in turn, took the measure of Rowan. He was surprised when the minotaur broke the awkward silence first."

gh "Human, it is good to meet you."

show rowan necklace concerned at midleft with dissolve

ro "And… you as well."

gh "Will you do me the honor of telling me your name?"

ro "Rowan Blackwell."

"He let out a grunt deep in his gullet. The sound passed through his leathery lips like a rockslide."

gh "The Hero of Rosaria?"

"Rowan nodded. The halting cadence of his voice was oddly soothing to the ear."

gh "Hm. A pleasure. The stories say you are a good man."

ro "I wouldn’t know about all that."

gh "Modest too, it seems."

ro "You're... too kind. Would you do me the honor of telling me {i}your{/i} name?"

"The minotaur blinked, seemingly shocked for a moment by the response."

gh "I... of course. It is Greyhide."

ro "It’s nice to meet you, Greyhide."

"Something in the bull's stance changed.  He seemed to stand up just a little bit straighter."

gh "From now on, I shall turn as much of the iron you supply me into equipment for the brat's soldiers as I'm able. In time, I may forge with other metals as well."

"There was a simple earnestness in Greyhide’s words that made Rowan smile. Despite his size, Rowan felt not the least bit intimidated by him."

gh "Shall I show you around the forge?"

"Please do."

scene black with fade
pause 2

scene bg22 with fade
show greyhide neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with dissolve

"The next half hour passed in pleasant conversation between the two as the Minotaur showed him his workspace. Greyhide knew his work, and Rowan was now confident that he was up to the task."

ro "If you don’t mind me saying, you seem… different from most of the castle staff."

gh "Of course. I am a Minotaur."

"Rowan had to hide his wry smile behind his hand."

ro "Not quite what I meant. I mean you don’t have quite the - uh… ‘temperament’ of most of the Twins’ servants."

"Greyhide was silent for a moment, as if mulling over his words."

gh "The brat has said that I won't have to fight as long as I make his weapons and armor.Greyhide: His cause is not mine. I am just a smith."

ro "Well, either way, I'm looking forward to working with you, Greyhide."

"Greyhide grunted again. Rowan saw the beginnings of a smile tugging at the corner of his lips."

gh "You seem to be an honourable man. Careful: honour is in short supply here. Much like iron."

"Rowan moved to leave, but the bull shifted uneasily on his hooves. After another long silence he spoke up again."

gh "I don't like these bloodthirsty orcs, but maybe you can keep me company some time."

ro "Perhaps we can get a drink together soon and swap stories?"

gh "I’d like that very much."

ro "The Twins are working me to the bone at the moment, but we can work something out when I have some free time."

gh "I look forward to it."

$ activate_event("drinking_buddies")
$ set_event_timer('greyhide_s_first_gift', 'after_forge_purchased', dice(5))
$ greyhideMet = True
$ codex_add('greyhide_starting')
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label tavern_purchased:
# Intro to Indarah and tavern explanation
#occurs week tavern is built

#corridor bg
scene castle hallway with fade
show rowan necklace neutral at midleft with dissolve
show indarah neutral at midright with dissolve

"As Rowan was leaving his quarters and heading down towards the castle kitchens he ran into a dark skinned woman dressed in bright silks. She had a cheerful bounce to her movements, but also had a hard edge to her features."
"She gave a one handed curtsey to the hero before addressing him."

ind "A fine morning to you, hero Rowan. I am Indarah, the one called Jezera instructed me to seek you out and introduce myself."

ro "A fine morning to you as well, woman of the Dragon's Tail."

"As he spoke, he returned her greeting with the customary sweeping bow. As he did so, he noticed that there were some fighting scars on the woman's hands."
"When he returned his gaze to her face, he spotted the barest hint of another scar that she hadn't quite managed to cover up. This girl was a fighter."

ro "So what brings you to Castle Bloodmeen?"

ind "An opportunity I would never get back home, a chance to own a tavern of my own. Your mistress has offered me a property that was recently restored in the Wastes. My experience dealing with pirates, often violently, seemed to have impressed her."

ro "Well, I hope that your service does not prove to be a greater burden than you thought it would be when you agreed to serve Jezera."

"She measured Rowan's words for a moment before responding."

ind "I'm well aware that she is a demoness, as well as what she and her brother seek to do. I don't care what they are if they give me a chance to break free of the chains of my birth."
ro "Very well, Indarah. It was good meeting you, I'll see you around the tavern."

$ set_event_timer('indarah_s_first_gift', 'after_tavern_purchased', dice(5))

$ codex_add('indarah_starting')
#end event
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label andras_opens_arena:
# Andras opens the arena
# Event triggered when the arena is built

scene bg9 with fade
show rowan necklace neutral at edgeleft with dissolve
show alexia necklace neutral at midleft with dissolve
show andras smirk at midright with moveinright

an "In honor of the arena's completion, I would like to personally invite the two of you to see first blood spilled."

show alexia necklace look away at midleft with dissolve

"Alexia shifted uncomfortably and looked away from Andras."

menu:
    # Choice: Try to convince him that Alexia shouldn't have to come"
    "Try to convince him that Alexia shouldn't have to come":
        ro "Thank you for the invitation, but I think that Alexia isn't feeling up to this, so..."

    # Choice: Turn down his invitation"
    "Turn down his invitation":
        ro "I don't think we're all that interested, thank you."

show andras displeased at midright with dissolve
an "I'm sorry, but I must insist that both of you come as my honored guests.  I really won't take no for an answer."

scene bg14 with fade

"Under the demon's fierce gaze, Rowan and Alexia were escorted to the newly completed arena."

# arena bg
scene bg29 with fade
show rowan necklace neutral at edgeleft with dissolve
show alexia 2 necklace concerned at midleft with dissolve
show andras happy at midright with dissolve

"As they approached the entrance to the high seat, the sound of orcish cheering rose louder and louder."
"Rowan and Alexia were directed to sit in the seats surrounding the high seat, which Andras then took."

"He smiled and rubbed his hands in anticipation for a moment, then snapped his fingers causing a thundering crash. Shortly afterwards, several scared men shuffled into the arena followed by a troop of orcs from the other side."
"Alexia gasped in horrible realization at what's about to happen."
"Rowan's breathing stopped for several moments in even deeper horror, as he saw that the men were horribly under equipped compared to the orcs. This wasn't going to be a battle, it was going to be a slaughter."
"Andras only waved his hand, then smiled sadistically as the \"battle\" started."

an "Don't even think about looking away, this show is in the two of you's honor after all. Think of it as a thank you from me for finding the funds for this wonderful place."
an "I assure you that the troops will be much more content with a place like this to cut loose and have fun, especially if you can find me some prisoners for them to play with."

"The rest of his words were drowned out by the incredible noise from the soldiers in the stands as the first drops of blood hit the arena floor."
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label breeding_pit_build_scene:
##### Breeding pit build scene #####
#Event triggers when breeding pit is built.

scene bg14 with fade
show rowan necklace neutral at edgeleft with dissolve
show andras displeased at midleft with moveinright
show draith neutral at cliohnaright with moveinright
show jezera neutral behind bg14

"On his way to the throne room, Rowan found himself face to face with his master holding onto a short violet skinned man dressed in straps and leather pants who was nervously looking around the castle."

an "There you are, servant. I snagged a little dark elf to help us out with the new breeding pit. Found the poor sod wandering around outside their caves, shivering from the cold."

ro "What were you doing there?"

"Rowan addressed the elf, but there was no response. The dark skinned man wouldn't even meet his gaze."

je "Probably running from his mistresses.  Men don't get much in the way of rights in their society."

hide jezera
show jezera happy at edgeright with moveinright
show draith neutral at midright with move

je "What's the matter? I won't bite."

show draith neutral at midleft with move
show andras displeased at midright with move
show jezera neutral at edgeright with dissolve

je "Don't like ladies, hmm? I promise I'd treat you better than my brother will, but suit yourself. Rowan, would you be a dear and give this man a hug?"

ro "Excuse me?"

je "Brother, why have you dressed him like that?"

an "That was how I found him. He begged me to take him away from his home and said he knew how to handle monsters."

je "No wonder he was so cold.  This boytoy didn't have a chance to get any proper clothing for an escape, must have been an opportunity he couldn't pass up or a danger he had to flee. Why are you still standing there hero? Our new breeder needs to knock dicks with someone."

menu:
    "Give the dark elf a hug.":
        $ released_fix_rollback()
        "As instructed, Rowan stepped forward and wrapped his arms around the shorter man. The elf started slightly, but then almost immediately pressed himself into the embrace."
        "He wrapped his arms around the hero in turn, even pressing his waist forward. While Jezera had likely jested when saying their newest servant needed to knock dicks, it seemed that he really did want to do exactly that."

    "Give the dark elf a pat on the back.":
        $ released_fix_rollback()
        "Rowan didn't give the shorter man a full hug, but did clap him on the back and give a reassuring squeeze of the shoulders. That was how he'd always encouraged his male soldiers back during the war."
        "The elf evidently wanted to go a step further, but when the hero pulled back from him he didn't push the matter."

show draith happy at midleft with dissolve

"For the first time, a smile crossed over the dark elf's face and he meet Rowan's gaze for an instant."
"Behind the two of them, the twins continued their discussion. It was rapidly turning into an argument."

dra "Draith. I'm Draith."

ro "Good to meet you Draith, I'm Rowan. So, you're good with monsters?"

show jezera displeased at edgeright with dissolve

dra "Yes! I'm good with them, one of the only guys who managed to not lose a hand to them. If you can give me a place to stay, I'll take care of your monsters."

"He spoke with a mix of excitement and apprehension. The former was likely due to the possibilities of his new life. The later probably had to do with always being afraid of the next beating."

show andras angry at midright with dissolve

ro "Well then, why don't I show you the facilities and you can explain all about handling monsters."

"Talking about things that he liked, or at least was comfortable with, should help overcome that apprehension."

hide rowan with moveoutleft
hide draith with moveoutleft

je "Honestly brother, whatever will I do with you? Yeti hunting? Was that really the best use of your time?"

an "A yeti would have made a fantastic first addition to our pits! Our foes wouldn't know what hit them."

scene black with fade

"They left the two arguing twins behind, heading deeper and deeper into the castle underground."

scene bg25 with fade
show rowan necklace neutral at midleft with dissolve
show draith neutral at midright with dissolve

ro "Here we are."

"The dark elf looked around the cells and facilities for a few moments, then looked at Rowan with a confused expression on his face."

dra "It's empty."

ro "Yeah, well, we just finished building the place. There hasn't been time to actually get any monsters yet."
ro "Speaking of which, would you know what the best way would be to get monsters?"

dra "For small pens like these? Best to use newborns, growth enhanced if we can get the nutrients."

ro "So, stealing eggs or children from nests and bringing them here?"

dra "Exactly. We don't have large enough facilities for anything else, so find any monster nests you can and bring their young back here. I'll take care of the rest, at least I think I'll be able to."

ro "Sounds good. I'll just give you an overview on life here at Bloodmeen, where you can find me, and we'll see about getting you quarters to live in."

$ codex_add('draith_starting')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label brothel_purchased:
# Intro to Shaya and brothel tutorial
# Triggers the week the brothel is built

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with moveinright
show shaya neutral at edgeright with moveinright

"Rowan was distracted from work today by the usual source. Jezera. She came into the throne room, accompanied by an olive skinned woman wearing the attire of a dancer."
"Rowan strained to get a look at her face, but it was hidden behind a silk veil. Still, one could not doubt she was a rare body. Her provocative outfit left little hidden. The difference between it and nudity was perilous."
"He stood up and bowed to them when they arrived at his desk."

ro "Have we met before, my lady?"

je "Haha, you most certainly have not. This is Shaya. And you have to be on your best behavior with her, Rowan. You happen to be in the presence of my oldest friend."
je "Well, oldest living friend. Long story. Not going to get into"

"The half demon turned to her companion."

je "Rowan here is my finest acquisition. I am sure you know of Al-Serah, yes? During his campaign here at Bloodmeen, Rowan was-"

show shaya happy at edgeright with dissolve

sha "One of his most noble companions. I have heard. It is an honor to meet you, Sir Rowan."

"The newcomer dove down into so deep a bow, that she was on all fours with her forehead touching to the ground. Compared to it, Rowan’s bow of greeting seemed quant. No greeting for a commoner."
"He blinked a few times."

je "Yes, well, among the tasks I have assigned to him, is management of castle resources. So you two will be working closely together."

"Her sudden show of affection felt somewhat off to Rowan and he tried to softly pull his hand away from her. The woman only held on tighter, so the hero decided to change tactics."

show rowan necklace happy at midleft with dissolve

ro "So you are to join the castle staff? It’s good to meet you, Shaya."

"He held his hand out to greet her. Upon returning to her feet, she clutched his extended palm with both of hers. She held it like a treasure, hovering only a few inches from her body."

sha "To you as well. I can merely hope that I do not prove a disappointment to you."

"Rowan felt his palm start to sweat. Shaya proved perfectly accommodating when he pulled it back to his side."

ro "So, what will you be doing with us here in Bloodmeen?"

"She turned to look at Jezera for a moment. For a moment, Rowan thought he caught the outline of a smile forming behind the veil."

sha "A fascinating question. Indeed, sweet {i}Jezer’aca{/i} has not been forthcoming enough with that information for me to answer."

#jez shocked
je "Not forthcoming? Do you mean to tell me you weren’t listening when I explained it to you?"

"Shaya let out a faint giggle, hidden by the politeness of a palm over her face."

sha "Forgive me, sister. But, at times your excitement makes your explanations...somewhat difficult to follow."

show jezera displeased at midright with dissolve

je "Ugh. Terrible. "

show jezera happy at midright with dissolve

je "Well then, time to fuck two nuns with one cock. Come along, dear sister, and I’ll show you to your new base. Rowan, join us as well. You both need to be brought up to speed."

if avatar.corruption < 31:
    ro "Two nuns…?"
    "Rowan followed them down the corridor. To avoid staring at the swaying rears in front of him, he tried to collect his thoughts. "

else:
    "Rowan followed them down the corridor. Between strategic glances at the two shapely asses, he collected his thoughts."
    
show rowan necklace neutral at midleft with dissolve

"There was no doubt she and Jezera were close. She walked near arm and arm with the mistress of the castle. What’s more, she called her {i}“Jezer’aca”{/i}. The suffix was a common honorific for a close friend or lover in the Empire of Sand."
"Rowan’s eyes narrowed. What kind of woman would Jezera choose as a close friend?"

scene bg24 with fade
show jezera happy at midleft with dissolve

je "Well, what do you think?"

"Jezera spread her arms in a dramatic sweeping gesture. And sure enough, the sight was impressive. The room was a seemingly endless weave of cushions, gold, and luxury. It was impossible to say how large, since multiple silk dividers sectioned off different areas."

show rowan necklace neutral at midright with moveinright
show shaya neutral at edgeright with moveinright

ro "This is quite, extravagant…"

"Shaya cupped her mouth in her hands. Her eyes visually widened."

sha "It’s perfect. Everything where it should be. As if it were a painting…."

"Shaya walked slowly over to the drapes and ran a delicate nailed hand over it, taking in the sensation."

ro "This is the base of operations for spies, right? The one I approved construction of."

#jez smirk

je "Base? No, this is a sanctuary. To the men, and occasional women, we bring in, it will look and feel like a brothel, among the finest in the six realms. Many of the girls will be hand trained dancers and slaves, who specialize in pleasure."
je "But, behind the curtain will be my finest infiltrators, succubi and incubi. From here, they’ll go forth and spread whispers over the confident. Queens and Aribtrons will be wrapped around their fingers."
je "I finally have an operation befitting my skills as a spymaster. Mark my words, this day will go down in the annals of the craft of deception."
je "Aha-ha-ha."

show rowan necklace happy at midright with dissolve

ro "You’re really excited huh?"

sha "Why wouldn’t she be? Sweet {i}Jezer’aca{/i} has been quite...forward about her desire for such a thing for many years."
sha "Surely, you had to expect a bit of excitement, assuming you’ve worked for her for long?"

"Shaya brushed against his side for a moment with her bare shoulder. An accident when she’d been turning to speak to him."

#show jezera happy at midleft with dissolve

"Jezera, meanwhile, had taken a seat on a large purple cushion with lions decorated on the sides."

je "Now then, that brings matters back to you too. Shaya, you’re better trained and better suited to running this operation than anyone I know. The show we put on here must leave customers speechless, and no one can entertain like you can."

"Shaya bowed her head."

je "Rowan, the spies here will help you on your mission. It will be your job to find tasks for them to undertake.  You'll also need to allocate funds to maximize our possible operations."
je "I'll handle locating spy candidates and transportation, of course.  While they don't have other tasks to accomplish in the field, our spies can join in the fun back here at the brothel. Cubi are quite good at extracting information... among other things."

"The demoness continued to go over the finer points of espionage for some time. In detail far more fine than remotely necessary, of course. At the same time, they went on a tour of the facility, showing off some of the many private rooms and segments."

je "Now, keep in mind that my sublime shadow stalkers will take time to complete their tasks. While brother's armies can conquer villages and towns faster, it will cost you more than if my spies do the task."

"Shaya paused in place, folding her arms behind her back. The posture only made her bust rise into a more prominent position."

sha "May I leave to explore my new home in greater detail, {i}Jezer’aca{/i}? There are things I must acquaint myself with."

je "Of course, beautiful. Do what you need to."

"Then, the newcomer turned back to Rowan and gave him another bow."

sha "And please excuse my rude departure as well, my new friend. I look forward to the many happy memories we will make together in the future."

ro "Y..yes. Of course."

hide shaya with moveoutright

show rowan necklace neutral at midright with dissolve

"Once Shaya left, Rowan returned his focus on the building. His fingers traced the strange glittering beads of one of the dividers."

#Perception Check - Medium Difficulty - TODO
"Something about this encounter hadn’t sat right with him. Shaya’s posture and behaviour had been very fluid and controlled most of the time they spoke. But, when she’d seen this place, she’d shown genuine shock."
scene black with fade
show shaya neutral at center with dissolve
sha "It’s perfect. Everything where it should be. As if it were a painting…"
scene bg24 with fade
show rowan necklace neutral at midright with dissolve
"Rowan looked down at the bed in the room he was exploring. The design was intricate, with a pair of jeweled lions guarding the ends. A very specific design choice. Hard to construct on the fly." 
"...But, perhaps easier to recreate."

$ shayaClue1 = True
$ shayaClueScore += 1

"He turned back to Jezera who was still sitting in a recliner and largely basking in victory."

show jezera happy at midleft with dissolve

ro "Shaya’s quite polite isn’t she?"

je "Politeness can be a weapon, Rowan. But, have no fear. If there’s anyone who can see through her, it’s her sister Jezera. She definitely likes you already."

"Rowan ran a hand through his hair."

menu:
    "”She’s beautiful.”":
        $ released_fix_rollback()
        $ shayaBeautiful = True
        show rowan necklace aroused at midright with dissolve
        ro "..."
        ro "...She’s beautiful…"
        #jez smirk
        "Jezera did not fail to notice that Rowan’s cheeks had turned red. Naturally, she didn’t have the self restraint to avoid giggling at his expense."
        je "Oh, does our little hero have a crush? I’m sure the missus would have some opinions on that."
        je "But, not to worry. If there is one rule in this world, it is that a man’s wife doesn’t need to hear about what happens within the walls of a brothel."
        
    "”You seem close to her.":
        $ released_fix_rollback()
        $ shayaBeautiful = False
        show rowan necklace neutral at midright with dissolve
        ro "You called her “Sister”. You must be pretty close to her."
        je "Why, of course. I grew up with her, basically. She’s one of my oldest friends. In truth, most of the runts I grew up with were quite average. But, I saw the talent in Shaya here very early."
        je "In some ways, she’s my first agent. Being without her here in Bloodmeen has been like if I were missing a hand. Or like if you were missing your cock."
        show rowan necklace happy at midright with dissolve
        ro "I’m not sure that metaphor totally works."
        "Jezera rolled her eyes at him."
        
    "”You must really trust her.”":
        $ released_fix_rollback()
        $ shayaBeautiful = False
        show rowan necklace neutral at midright with dissolve
        ro "When I agreed to construct a spy base, I assumed you’d be running it yourself. The only person you don’t have eight layers of bullshit with is Andras."
        je "Not for lack of trying. He’s just usually too bullheaded to manipulate."
        ro "What I’m saying is, that for you to trust anyone with your spying operations you must really truly trust them."
        je "Trust? Trust!? I will have you know that’s a dirty word for me."
        "Her playful grin revealed her seeming outrage wasn’t quite so serious."
        je "But, if you must know, I have no fear that Shaya will keep faith perfectly. No one has done more to show her dedication to me than she has…"
        "Rowan’s ears peaked up. There was something to the way she’d said it. He mentally filed that as important."
        $ shayaClue2 = True
        $ shayaClueScore += 1
        
"Before Rowan could ask any further questions, Jezera was making her way back to the entrance of the brothel."

je "By the way, please be so kind as to arrange for Shaya's luggage to be brought down here? Chop chop, hero."

scene bg9 with fade
show rowan necklace naked neutral at midleft with dissolve

"That evening, Rowan tossed and turned in bed. Sleep should have already fallen on him, but tonight it just didn’t come. On nights like this, he often found himself reviewing the events of the day in exacting detail."

if rowan_shares_room_with_helayna == True:
    "So it was that Rowan, half-asleep and near-naked, made his way to his desk. There, he drew a large parchment and began to scribble."

else:
    "So it was that Rowan, half-asleep and near-naked, made his way to his desk. He made great care to move silently, so as not to wake Alexia. There, he drew a large parchment and began to scribble."
 
"The page was headed by a single question in large font."
"Who is Shaya?"
"Beneath it, he scribbled all of his observations from the conversation. The silky smooth way she moved. Her polite deferential way of speaking. Most especially her familiar rapport with Jezera."

if shayaClue1 == True:
    "He made special note of her reaction to the design of the new brothel. She’d been reduced to awe. But, it didn’t sound like she was reacting to its opulence. There was something particular about this place."
    "Furthermore, a project of this sort would need more than Skorded’s usual crew of designers. It would need particular artisans, probably of Imperial origin. A task he would have heard of." 
    "Unless... she had designed the entire building herself? unlikely, she must have been going on a pre-existing design.No. This was modeled on a place that already existed. A place that Shaya and Jezera both knew well."
    "Rowan brought the feather of his quill to his lip." 
    "Before he saw her next, he would need to research Qerazel’s architecture in greater detail. Perhaps he could figure out the exact building."
    "{i}What building is the Brothel a replica of?{/i}"

if shayaClue2 == True:
    "When recording Jezera’s reactions during the conversation, he stopped briefly to consider her response when he’d mentioned how much trust Jezera gave her."
    "“No one has done more to show her dedication to me than she has…”"
    "Just what did that mean? For Jezera to say that, Shaya must have rendered quite a service in the past…"
    "{i}What did Shaya do for Jezera?{/i}"

"Whoever this mysterious newcomer was, she was important. She was the first person he’d encountered that had been presented to him as someone who one of the twins considered a  genuinely close confidant." 
"For all the other powerful people he’d met here at the castle. There were almost none so worthy of close scrutiny."
"Perhaps that is why he’d found it so difficult to sleep..."
"When he finished, he carefully folded the notes and hid them in a treatise on magical beasts next to his desk, then stumbled into bed."

if shayaBeautiful == True:
    "But, his efforts to fall back asleep were not easy. His doubts were replaced with something else. A flicker of memory; a sensation." 
    "Two perfect, supple breasts pressed into his arm. It was like a phantom presence. The more he dwelled on it, the more he rocked uncomfortably in bed."


if rowan_shares_room_with_helayna == False:
    "If his wife noticed, she didn’t mention it in the morning."

$ codex_add('shaya_starting')
#end scene
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label greyhide_meets_alexia:

scene bg14 with fade
show alexia 2 necklace concerned at midleft with dissolve

"Alexia hated Castle Bloodmeen. She hated it from the tip of its tallest spire all the way down to its grimy foundations."
"She hated that she was stuck here with no control over her own fate, she hated that the life she’d struggled so hard to make had been destroyed and replaced with this gilded cage."

show orc soldier neutral at edgeleft with moveinleft
show wild orc neutral at edgeright with moveinright

wo "Ey pretty lady, wanna cum play wif us?"

"...But most of all, she hated the things that lived here. "

wo "Oi! You deaf? I says come over ‘ere."

al "U-uh no! I- uh-"

wo "We’s missin’ out on good whores down in tha’ barracks. You look good e’nuff."

"The two Orcs leered at her as she tried to slide past them in the hallway. She’d been hoping, {i}praying{/i} they wouldn’t notice her. No such luck."

al "I-I’m not a-"

wo "Oi, come ‘ere, eh? I just wanna touch ya."

os "Best steer clear of ‘er. She’s da boss’ pet I fink."

wo "Wot? Really? Dis one?"

os "Yea."

"The Orc looked her up and down, as if appraising the age of bad meat."

wo "Fuck it. Fine, ya ain’t worth ‘da trouble anyway."
wo "See ya again, pretty lady."

hide orc soldier with moveoutleft
hide wild orc with moveoutright

"Alexia stood rooted to the spot, a feeling of helpless dread tingling down her spine as the two disappeared down the corridor."

show alexia 2 necklace angry at midleft with dissolve

"…followed shortly thereafter by a rush of impotent rage."

al "Those {i}bastards{/i}!"

"She couldn’t stand it. She couldn’t stand one more second of it."

scene bg57 with fade

"She rushed out of the castle, sparing not even a parting glance for anyone around who might be watching. She marched through the front gate as though she were about to storm it from the inside."

scene bg3 with fade

"It didn’t take long for her angry charge to degenerate into a miserable, meandering hike through the nearby woods."

show alexia 2 necklace neutral at midleft with dissolve

"Her brooding reverie was cut short when she spotted something lurking in the bushes in front of her. She stepped through the creeping foliage, stopping short once she realized she was face to face with a hulking-"

show greyhide neutral at cliohnaright with dissolve

show alexia 2 necklace shocked at midleft with dissolve

"...Minotaur?!"

al "{i}Aaaah!{/i}"

gh "Hm?"

"Alexia fell back on her hands, half crawling, half scampering backward as blind panic set in. The massive beast towered over her, nearly twice her size when standing at full height."
"The two shared a long staredown. The Minotaur’s dull, cowlike eyes gazed back at her with curiosity."

gh "Why do you scream?"

al "...What?"

gh "Why do you scream?"

al "B-because you’re a {i}Minotaur{/i}!"

"The beast looked down at himself, as if appraising the truth of her words. "

gh "So I am."
gh "But why are you shouting?"

al "A-aren't you going to… eat me?"

gh "I am a vegetarian."

al "..."
al "...Oh."

"The absurdity of the situation would have been almost comical were Alexia not so frightened for her life."

al "But- but the stories said-"

gh "Stories are not truth."

al "Oh."

"Another awkward silence. Neither seemed to know quite what to do with the other."

al "I-I had no idea."

"The bull flashed her a glimpse of his smile, pulling back his leathery lips to reveal large, flat teeth. They weren't nearly as menacing as Alexia had expected."

gh "Now you do."

show alexia 2 necklace neutral at midleft with dissolve

"The beast offered her his hand. It was well over twice the size of her own, able to hold hers entirely in its palm. Hesitantly, she took it. He helped her to her feet."

gh "What are you doing out here?"

al "I just… needed some air."
al "Who {i}are{/i} you?"

gh "Greyhide. The castle blacksmith. "
gh "Would you do the honour of granting me your name?"

al "It’s… Alexia Blackwell."

"The bull grinned again, disarming her with his honest smile."

gh "Nice to meet you, Alexia."

al "What… what are you doing out here?"

gh "Feeding the birds."

al "Birds?"

"The bull opened his left hand, revealing the sizable heap of seed sheltered in his palm. With his right he took a pinch of it, tossing it out onto the forest floor like a farmer sowing seeds."

gh "They were here just a few moments ago. You scared them off."

al "Oh! I… I’m sorry."

gh "Do not feel sorry, they are only birds. They will return."

"This conversation was only growing more and more absurd. Alexia watched in a sort of stunned awe as the hulking Minotaur gently tossed another pinch of seed across the ground."

al "So… you’re the castle blacksmith?"

gh "Yes."

al "I had no idea the Twins had a {i}Minotaur{/i} for a blacksmith."

gh "Heh. Now you do."

"There was no scorn in his voice. He spoke to her with a quiet, respectful tone. A wave of shame struck Alexia as she realized how rude she was acting."

al "I’m sorry, I didn’t mean to say it like that."

gh "It was a fair question. My kind are not common in this part of the world."

al "Still, it came off worse than intended."

gh "No harm done."

al "..."

"Alexia watched as the gentle giant tossed another handful of seed upon the ground. Her eyes trailed across his bulky, bestial form."

al "Do you... often do this? Feeding the birds, I mean."

gh "No. This is the first time."

al "What made you want to do it now?"

"The bull paused, seeming to mull over the question. The silence dragged on for several seconds."

gh "{i}Hrmh{/i}. I do not know. A whim, I guess."
gh "The castle can be a hard place to live in. I come here sometimes. It is quiet."

al " Then I've interrupted your solitude... I’m sorry."

gh "Do not apologize. You are not at fault."

"Yet another silence, this one a little less awkward. She was starting to grasp the slow cadence of his voice. He wasn’t slow, just… deliberate."
"Soon, the sound of chirping could be heard in the clearing. Alexia smiled as a pair of thrushes alighted upon the ground and began to peck at the seeds he’d tossed."

al "It’s nice out here."

gh "Yes. It is."
gh "Come, share some seeds with me."

al "W-what?"

gh "It is very calming."

"Alexia shuffled forward, her stomach twinging with uncertainty. Greyhide seemed friendly enough, but…"
"She extended her palms, cupping them together like a bowl. His large hand tipped to one side, pouring the seeds into her grasp."

scene cg860 with fade
pause 2
show cg861 with dissolve
pause 2
show cg862 with dissolve
pause 3
show alexia 2 necklace happy behind cg862
show greyhide neutral behind cg862

"Together, the two began to toss their bounty to the hungry birds. They soon had a small flock hopping and pecking and chirping about them."
"Alexia’s eyes were suddenly drawn to the flutter and flash of crimson wings sweeping through the air."

al "Oh! A robin!"

gh "I have seen him here a few times already. He is hungry, I think. Slim pickings in these woods."

al "He’s beautiful!"

gh "Heh, I guess he is."
gh "It is good to take joy in little things."

al "It… it is."

"Was this really happening? Was she {i}really{/i} standing here, passing idle time with a monster?"
"She had almost completely forgotten about her earlier anger, her frustrations. The world had descended into an almost dreamlike delirium. "

gh "You are Rowan’s mate, are you not?"

al "How did you know that?"

gh "I have seen the two of you in passing. "
gh "He was kind to me when we first met. As are you."

al "Oh, uh… thank you."

gh "No need to thank me. Your kindness is your own doing."

al "I’ve never met a Minotaur before. Are all of them like you?"

"Greyhide’s brow furrowed. He seemed troubled by the question."

gh "...Why do you ask?"

al "Just that-"
al "All my life I’ve heard stories of your kind. None of them particularly pleasant."
al "But you’re nothing like that. You’re so-"

"Alexia paused. She’d been about to say ‘gentle,’ but she didn’t know if he’d take it as an insult."

al "Sweet."

gh "I told you: those stories are not real."

al "I’m not talking about the stories. I’m talking about you."

"Greyhide pondered the question for a long moment, staring down at the birds that gathered at his hooves with a grim expression."

gh "...I do not think anyone is ‘like me.’"
gh "I am me. If any other Minotaur was like me, they would be here."

al "In Bloodmeen?"

gh "Alone."

al "..."

scene bg3 with fade
show alexia 2 necklace happy at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve

"They’d run out of birdseed. Greyhide dusted his hands off and hefted his warhammer onto his shoulder."

gh "Thank you for your kindness. There is not enough of it in this place."
gh "I enjoyed our talk."

al "As did I."

gh "Be well, Alexia."

hide greyhide with moveoutright

"Alexia stared at his retreating back and slumped shoulders, wondering what it was she had said to make him so melancholy."
"He was a strange creature for certain, but at least Alexia was no longer afraid of him."

al "...Be well, Greyhide."

return
