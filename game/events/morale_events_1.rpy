init python:
    
    event('plundered_ally', triggers="week_end", conditions=('castle.morale < 45', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    
    #TODO - add condition - captured one orc village
    event('word_gets_around', triggers="week_end", conditions=('castle.morale < 45', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    
    event('unauthorized_party', triggers="week_end", conditions=('castle.morale < 40', 'castle.buildings["tavern"].lvl > 0', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    event('keeping_the_numbers_up', triggers="week_end", conditions=('castle.morale < 40', 'week > 16', 'week < 20', 'castle.buildings["barracks"].troops > 4', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    
    #TODO - add condition - weekly iron equal or greater than one regular mine income
    event('bad_upkeep', triggers="week_end", conditions=('castle.morale < 35', 'castle.buildings["forge"].lvl > 0', 'moraleEventsActive', 'castle.iron_per_week > 1'), group='ruler_event', priority=pr_ruler)
    
    event('you_raided_yourself', triggers="week_end", conditions=('castle.morale < 30', 'castle.treasury > 74', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    event('intellectual_interference', triggers="week_end", conditions=('castle.morale < 30', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    event('bloody_traitors', triggers="week_end", conditions=('castle.morale < 30', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    event('broken_beasts', triggers="week_end", conditions=('castle.morale < 25', 'castle.buildings["pit"].driders >= 2', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    event('a_commanders_responsibility', triggers="week_end", conditions=('castle.morale < 25', 'avatar.corruption < 60', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    event('massacre_in_the_pits', triggers="week_end", conditions=('castle.morale < 20', 'Dungeon.prisoners > 4', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    event('pacification_operation', triggers="week_end", conditions=('castle.morale < 20',), group='ruler_event', priority=pr_ruler)
    event('calling_in_andras', triggers="week_end", conditions=('castle.morale < 15', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)
    event('calling_in_jezera', triggers="week_end", conditions=('castle.morale < 15', 'moraleEventsActive',), group='ruler_event', priority=pr_ruler)


label plundered_ally:

scene bg6 with fade
show rowan necklace concerned at midright with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan rubbed his temples. He did his best to focus on the words of his visitor, but the shrill tone didn’t help his rapidly growing headache."

show clamin angry at midleft with dissolve

cla "If you think I would take a violation of the terms of our agreement like this lying down, you are sorely mistaken. The back of the cart was totally ransacked. Wares gone. Your integrity is broken."
cla "Here in my hands I have the entire terms of the contract I negotiated with those runts who run the place."

"She waved around a stack of papers so large it could have convincingly made for a novel."

cla "Segment 2361 clearly deals with “violations of non-combatant status or acts in assumption of misinformed identity."

if week > 25:
    show liurial neutral at edgeright with dissolve
    "To his side, Liurial hummed to herself as she scribbled down notes from the meeting. He was tempted to tell her to shut up, if only to forestall the onset of his headache."

"The issue was that one of her trade caravans had been utterly ransacked while stationed at the castle. Finding the culprits hadn't been much of a challenge either. Reports had filtered to him nearly immediately in orcs battering away the stolen goods."

ro "Look...how much money do you need for this to go away?"

"With some further haggling, Rowan arranged for reparations to be paid to Cla-Min from the week's income. It turned out that Cla-Min was much less angry once a promise of repayment had been established." 
"But, she’d also wanted a promise that the incident wouldn’t be repeated. Thinking of the increasingly uncontrollable nature of the orcs under his command, it was a promise Rowan wasn’t sure he could give."

$ moraleEvents += 1
$ castle.treasury -= 40
#Reduce Village trade income by 20% for 3 weeks - TODO
$ income_reduced_for = 2
$ original_income = castle.villages_income
$ castle.villages_income /= 1.2
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label word_gets_around:

scene bg6 with fade
show rowan necklace concerned at midright with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan nearly spilled the drink on his desk when he saw the week’s headcount table. He had to catch it before it slipped off his desk."

if week > 25:
    show liurial neutral at edgeright with dissolve
    "Liurial frowned."
    liur "Please sir, you need to be more careful!"

"It took some more digging, including an interview with the orcish officer in charge of recruitment, to figure out what had happened." 
"When visiting the war camps to collect new levies, some of the Bloodmeen soldiers had fraternized with the tribal populations. And they had done a very poor job of selling the castle. Not enough plunder, not enough excitement, not enough pussy."
"When it came time to muster the new recruits, many hadn't even shown up. Apparently, the reputation of life in the castle was that bad."

if week > 25:
    liur "Will we be able to make do with such a small number, Sir?"


"In the end, Rowan was forced to accept this setback. There just wouldn't be enough recruits this week. And if something wasn't done about the morale of the orcs, this might not be the last time he faced problems like this."

$ moraleEvents += 1
#Reduce Orc recruitment by -1 village for 4 weeks. - TODO
$ castle.recruitment_bonuses["barracks"] -= 1
$ reduced_orc_recruitment = 4
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label unauthorized_party:

scene bg14 with fade
show rowan necklace concerned at midleft with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan pulled his foot back the moment he realized that he had stepped in a puddle of wine. Bits of broken glass pooled next to his boot."
"He was in the cellar of the castle, surveying the scene of a recent incident. Casks and bottles littered the stone floor, along with their ruined contents." 
"A few of the perpetrators had also remained to be caught. Leaning against the walls were several Orcish soldiers so hungover they could barely move."
"He kicked one of the broken bottles away and cursed under his breath. How could he run a war if his soldiers looted and pillaged their own castle with impunity?"
"The woman who’d come with him re-appeared by his side."


#show indarah angry at midright with dissolve
show indarah neutral at midright with dissolve

ind "Rowan, this was everything for the week. For weeks after too. You know I can strike some kinda deal with Cla-Min, but that might take some time."
ind "What am I supposed to sell the travelers? How do you think they’re going to react when they arrive at the first rest stop in days and there isn’t anything to drink?"

"Rowan didn’t have an answer for her."

$ moraleEvents += 1
#No tavern income this week, -50% tavern income for 2 weeks afterwards. - TODO
$ castle.buildings["tavern"].income = 0
$ reduce_tavern_income = 2
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label keeping_the_numbers_up:

scene bg6 with fade
show rowan necklace concerned at midright with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan looked down at the document in front of him and then back at the orc who’d given it to him."

ro "Deserters?"

show orc soldier neutral at midleft

os "Yea. A big n bunch o dem. Dey followed Mukmuk out da portal."

"The sheet in front of him was the notes from roll call. The number of missing orcs was far larger than disease or casualties from battle would have predicted."

os "Dey be say dat der is no food. And we follow pussy humies who say no killin. But, if youz in a war band der best be enough killin."
os "Plunder too. Dem demons and youz be takin all da shiny stuff."

"Rowan closed his eyes and put two fingers to his temple. The new recruits from the conscripts would be enough to replace the losses. But he’d planned to have more soldiers available than this."

ro "(Goddess fend…)"

$ moraleEvents += 1
$ castle.buildings['barracks'].troops -= 5
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label bad_upkeep:

scene bg22 with fade
show rowan necklace concerned at midleft with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan examined the large crate marked “replacements”. The fires of the nearby forge furnaces softly illuminated his face. It was always too hot here."

ro "I don’t understand, though. We shouldn’t need so much replacement gear so soon. Aren’t there higher priorities?"

show greyhide neutral at cliohnaright with dissolve

"Greyhide shrugged and brought the hammer down on the sword he was working on. Even with Rowan’s visit, he didn’t pull himself from the labour. There was too much to do."

gh "Bad upkeep. They tell the orcs how to handle their shit. But, they don’t."

"Rowan grunted and leaned slightly against the crate."

ro "The lady damn them. I’ve gone down myself and shown proper weapons maintenance. The officers should be teaching it too."

gh "Should. But, they don’t."
gh "Gotta hammer it in."

"He struck the metal, but the shape proved hard to mold. So he struck it again. Rowan watched for a time, cursing under his breath."

$ moraleEvents += 1
$ castle.iron_per_week -= 2
$ iron_reduced_for = 4
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label you_raided_yourself:

scene bg14 with fade
show rowan necklace concerned at midright with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan picked up a coin from the ground. In the thieves’ haste to escape the scene of the crime, they’d left remnants of the stash scattered on the ground. He shook his head."
"The storage room had been one of the secret treasury caches hidden throughout the castle. The remnants of the destroyed lock and reinforced door were the first things Rowan had discovered on his examination of the wreck."

ro "Just how much was taken?"

if week > 25:
    show liurial neutral at edgeright with dissolve
    liur "...A great deal, Sir. I’m still attempting to find the prior accounting document."
else:
    show orc soldier neutral at midleft with dissolve
    os "...Alot."
    
"Rowan grit his teeth. An investigation would need to be held. But, in all likelihood it was the orcs who’d done the deed. Of late, more and more acts of looting and theft of castle property had come from their own men."
"In the meantime, all this meant was another brutal dent in the castle treasury. In the middle of running a war."

$ moraleEvents += 1
$ castle.treasury -= 75
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label intellectual_interference:

scene bg6 with fade
show rowan necklace concerned at midleft with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."

show cliohna neutral at cliohnaright

"Cliohna stiffly approached Rowan’s desk. After hearing of some kind of disturbance, he’d expected to be greeted by her at some point over the day."

cl "Are you aware of what those brutes you call soldiers have been engaging in?"

ro "Not as much as I’d like. No."

"He reclined in his chair, preparing for whatever she was going to say. Were times like these the reason his commanders back in the war would keep brandy in their desks?"

cl "A cohort of your men attempted to kidnap one of my students and extort a ransom from me for his safe release. You are very fortunate that they did not harm him, else I’d be even more cross than I am presently."

ro "I presume you handled them?"

cl "Indeed. There will be no further questions of the erstwhile kidnapper’s obedience. I have ensured it. Permanently."
cl "But, this episode cost me valuable research time. I do not take kindly to distractions of this ilk."
cl "Handle your soldiers. Do not make this a repeat occurrence."

"It took quite a few assurances from Rowan to get her to return to the library. He was left to his lonesome to figure out how he’d back up any of those promises."

$ moraleEvents += 1
# -80% research this week only. - TODO
$ original_research = castle.tech
$ castle.tech *= 0.2
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label bloody_traitors:

scene bg14 with dissolve
show rowan necklace angry at midleft with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."

ro "Ach!"

show orc soldier neutral at edgeright with dissolve
show wild orc neutral at midright with dissolve

"Rowan fell to the ground clutching his shoulder. The first trickling of blood emerged from beneath the gaps in his fingers. He looked at the red stain it left then back at his assailants."
"The group of orcs he’d been arguing with took a step back. The confidence that they’d had mere moments before vanished."

ro "You just assaulted your commander. Did you think I was going to take that lying down?"

"The most confident among them stepped forward. He’d been the one who struck Rowan with his axe."

wo "Yah, humie. I did. We ain’t got no beer. No slaves. No nutin. How aboutta we put dis to a fight?"

"Rowan straightened his back. Orcs respected one thing, strength. If he backed down here, they’d take it as a signal they could walk all over him."

ro "Put it to a fight? Some fight. You struck me while we were speaking around the table. A cowards’ way to fight. If you were a real man you would have challenged me properly."
ro "Or were you afraid to fight me at my full strength? I don’t fight with cowards."

"The orc growled and took a step towards him. But, the others turned to look at him, and in their eyes was something less than respect. After a moment’s hesitation, he stepped back into line grumbling."

scene black with fade

"Afterwards, Rowan went about calming the mob of soldiers. The one who’d struck him would be disciplined, of course." 
"But, as Rowan went to the infirmary to have the wound properly bandaged, he reflected on the incident. The next time his soldiers were mad at him, would he be able to talk them down with words alone?"

$ moraleEvents += 1
#Add damage: Arm (serious) - TO DO AFTER MECHANICS UPDATE IS READY (not now)
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label broken_beasts:

scene bg6 with fade
show rowan necklace concerned at midright with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."

#draith concerned
show draith neutral at midleft with dissolve

dra "Rowan, please, you have to do something about it. I can’t control them…"

"Rowan sat on the other end of the desk from the dark elf listening to his plea of woah. A band of orcish soldiers, clearly starved for pussy or entertainment, had stormed into the breeding pits and unleashed havoc for their own entertainment."
"Draith’s voice had been unsteady as he recounted the way they’d tortured one of his drider’s for hours. All while he’d been forced to watch."
"By the time the vandals had moved on, they left the building in a state of disarray. The unfortunate drider had to be put out of her misery by the end of it. A loss of a valuable resource."

dra "Rowan, you’re the only one who can do something about it. I just don’t…"
dra "..."
dra "I raised her by hand. I called Zytradtsy. When she was growing bigger she’d made this little coo when she walked…."
dra "You have to stop them, Rowan. You have to."

"The dark elf broke into sobs. Rowan didn’t know what to tell him…"

$ moraleEvents += 1
$ castle.buildings["pit"]._driders -= 2
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label a_commanders_responsibility:

scene bg9 with fade
show rowan necklace concerned at midright with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan trudged back into his room and threw himself on the bed. The morning had been spent on an exhausting mission tracking down several orcish soldiers who’d engaged in unauthorized acts of looting."
"Tales of what one of them had done had gotten to him. A boy as young as four slaughtered in front of his parents." 
"It was of no great harm to the war effort. But, Rowan had explicitly given orders against the wholesale slaughter of children."
"As he settled into bed, an unpleasant memory came back to him."
"He heard the sound of screaming and saw the lick of fire move from house to house. The unit under his command had been sent out to track a rampaging orc band."
"He remembered going from house to house to look for survivors. He remembered the bloated face of a young boy left behind amidst the carnage."
"At the time, he wondered what kind of sadist would order such horrors. But, lying in his bed in Bloodmeen, Rowan thought he knew the truth. Whoever had been in charge must not have been in control of their own men."
"Rowan stared unblinking at the ceiling. It was getting dark."

$ moraleEvents += 1
$ change_base_stat('g', 15)
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label massacre_in_the_pits:

scene bg8 with fade
show rowan necklace concerned at midleft with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan examined the blood stain on the wall. Evidence of the orcish mob that had run rampant here. With a heaving sigh, he turned back to the survivor."

ro "Tell me what happened."

slave "It was just after the work period had ended. Normally our overseas take us back to our barracks. The new one had been getting into the habit of giving us more sleep time. "

ro "I’m aware. I was the one who picked him."

slave "O-oh."
slave "Well, we put our equipment down and waited to be returned to the cells. But, suddenly a whole lot of orcs started coming in. With the shackles, there was no way to defend ourselves…"
slave "The overseer tried to argue with them, but one big one socked him hard in the jaw and he went down all bloody."

ro "And that’s when they started killing the others."

slave "Slow and cruel. Like it was a sport. There was so much screaming…"

"Rowan nodded slowly. The shackled man took his time stumbling over his words. The memories he was recounting had left him traumatized."

slave "They didn’t kill all of us. The women they took back with them. After they were...they were done with them. You might find some of them back at the orc barracks."

"Rowan didn’t answer the poor man. Of course, he’d already come from there. But, by the time he arrived the kidnapped slaves had been killed."

show rowan necklace angry at midleft with dissolve

"Of course, a single incident wasn’t enough to deplete the castle’s entire slave population. But, still, with all the work Rowan had put into improving conditions down in the pits, learning of this latest act of Orcish Barbarism was enough to ball his hand into a fist."

$ moraleEvents += 1
$ change_prisoners(-5)
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label pacification_operation:

scene bg10 with fade
show rowan necklace concerned at midleft with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan tightened his sword belt and slung his bag over his shoulder. The mercenaries he was taking with him were scattered about the throne room making their preparations."
"Of course, what Rowan should have been getting ready for was his weekly return to the field. But, he would be late to his normal operations this time. Something had happened."
"There’d been a mutiny by orcs at one of the critical outposts at the edge of the wastes."
"Taking it back wouldn’t be so difficult, of course. With any luck, negotiations to bring the orcs back in line would be challenging but likely to succeed. And if they resisted, he was more than prepared to just storm it."
"Still, dealing with mutinous orcs wasn’t going to cost him a critical resource that he could not get back. Time. If he didn’t want to spend the hours he needed to devote to missions to keep the orcs in line, he was going to need to find a way to prevent the next mutiny before it started."
"Rowan turned back to the assembled mercenaries."

ro "Alright, men. Let’s move out."

$ moraleEvents += 1
#Movement points - 50% next week. - TODO
$ original_mp = avatar._mp
$ avatar._mp_penalty = int(avatar._mp * 0.5)
$ movement_points_penalised = True
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label calling_in_andras:

scene bg14 with fade
show rowan necklace concerned at midleft with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan stared out a low castle window at the assembled mob in the Bloodmeen courtyard. Orcs of all shapes and sizes held torches and weapons. Their laughing and snarling filtered up to him."

#courtyard BG
scene black with fade

show wild orc neutral at midleft with dissolve
show orc soldier neutral at midright with dissolve

"And in the center was one orc of great height named Torlar. He led off with a dramatic, though not exactly eloquent, speech about all of the plunder being denied to them."

torl "...dats why I say, enough…"
torl "...dats why I say we gon kill dat pink skin hummie, and show da whole castle who really runnin tings!"

"All of a sudden, his speech was cut off by a dark clapping. Another figure emerged from the shadows, mouth twisted into a menacing smirk."

hide orc soldier with dissolve
show andras smirk at center with dissolve

an "Show everyone who's really running things, eh? We can do that."

"Andras boldly strolled forward, shoving a few orcs standing in his way. The others opened up a path for him."

an "You’ve got a real set of brass balls if you think you’re going to be insubordinate in my castle. Rowan is my servant. And an attack on my servant is an attack on me…"

"Rowan didn’t see what happened next so well, but there was a sickening crack sound. Torlar, the rebellious orc, was on his knees before Andras with his leg twisted in an unnatural shape."

an "Hard to be “really running” things, with your leg in that shape, isn’t it?"

torl "I..I yield. Master. I yield."

scene bg14 with fade
show rowan necklace concerned at midleft with dissolve

"Rowan drew away from the window. He’d seen enough."

scene bg6 with fade
show rowan necklace concerned at midright with dissolve
show andras displeased at midleft with dissolve

"Later, he stood in attention before Andras in the throne room."

an "It’s your job to run shit."
an "So why the fuck am I using my valuable time to do your fucking job for you?"
an "I put a stop to the orcs and their muting this once. But, it’s your job to figure out what the fuck to do about them. You’re supposed to be some genius commander of armies, right?"
an "Command my fucking army." 

ro "It won’t happen again."

an "Good. If you can’t get control of them, I will do it myself. And you’re not going to like my methods, boy."

"Rowan made his way from the chamber, snarling under his breath. How had things gone so bad that he’d needed to use some of his precious influence on Andras on something so small?"

$ callingInAndrasSeen = True
$ moraleEvents += 1
$ change_favor('andras', -1)
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label calling_in_jezera:

scene bg6 with fade
show rowan necklace concerned at midleft with dissolve

"If you raise an army with no discipline, you assemble a mob against yourself."
"Rowan was surprised when he came to his desk in the morning and found it occupied by the lady of the castle herself."

show jezera displeased at midright with dissolve

je "Finally. Could you make your way here any slower? You humans and your incessant need to sleep. It’s a fine luxury, to be sure. But, one must tut-tut when there are things to do."

if week > 25:
    "She looked around."
    je "Isn’t that little tart you call a secretary here yet either?"
    
ro "The sun hasn’t even risen yet. I was about to start the day."

"She rolled her eyes."

je "Well, it’s only right for me to question your work ethic. After all, I’ve been the one having to do your damn job for you. Naughty naughty."

show rowan necklace shock at midleft with dissolve

ro "Excuse me?"

"She laid back on the desk, as if it was a bed. In the process, a stack of documents went tumbling to the floor."

je "Managing brother’s stupid brutes is your job, yes? Making sure when he says “jump”, they say “how high”. Yet, I have to do your job for you."
je "My spies have picked up a revolt being planned up in their ranks. Sweet hero, if it weren’t for me tomorrow night you’d be waking up to a cleaver in your belly."

ro "The orcs wish to assassinate me…?"

show jezera happy at midright with dissolve

"She giggled to herself."

je "Do you blame them? I’m sure your head would make a lovely trophy. Still, the fact that you’ve let the situation with their morale get so bad is simply intolerable."

"She leapt from the desk and sashayed towards the exit."

je " I’ve despatched a few of my spies to put a stop to this little plan of theirs. Consider it a favour from me."

#jez smirk

"As she passed Rowan, she stopped to put her lips to his ear."

je "But, if you don’t get your shit together, perhaps next time I’ll just let them kill you. "

hide jezera with moveoutright

"And with that, she departed. In the process, leaving Rowan with more questions than answers."

if week > 25:
    show liurial neutral at edgeleft with dissolve
    liur "Was that Lady Jezera!? Did she have a job for us?"
    "Rowan blinked."

$ moraleEvents += 1
$ change_favor('jezera', -1)
jump moraleFollowUp

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label moraleFollowUp:

if moraleEvents < 5:
    jump normalMoraleFollowUp
    
else:
    jump alternativeMoraleFollowUp

################################################

label normalMoraleFollowUp:

scene bg6 with fade
show rowan necklace concerned at midleft with dissolve

"Later, Rowan was pacing by the side of his desk. Had someone walked in, he'd hardly have noticed their arrival. All his focus was on the pressing issue."
"The morale of the castle's Orc retinue had fallen dangerously low. Unless he did something to change things, his men would continue to act out. He needed an army, not a mob."
"But, how to improve castle morale?"

label moraleMenu:

menu:
    "Use castle resources.":
        $ released_fix_rollback()
        menu:
            "Use your spies to discreetly remove orc malcontents." if get_spies('idle'):
                $ released_fix_rollback()
                #brothel bg blurred
                scene bg24 with fade
                $ moraleSpies = True
                "An idea could be a dangerous thing. If the orcs were putting words to their discontent, it could cause problems."
                "The simplest solution was simply to silence those who advocated for acts of disobedience." 
                "Bloodmeen's Spies went out and handled those who were identified as troublemakers." 
                "Some were vanished. Others threatened into obedience. A few plied with pussy until they were less likely to raise a fuss." 
                "Such an approach handled the symptom, not the root problem. But, it would forestall trouble for the moment."
                #Make 1 spy unavailable for 4 weeks. - TODO
                $ menu_res = renpy.display_menu([(spy.name, spy.uid) for spy in get_spies('idle')])
                $ assign_mission(spy_uid=menu_res, type='infiltration', loc=('rosaria_map', tuple([0, 0])), started=week, duration=4)
                $ change_morale(3)
                return
                
            "Bribe them with trinkets." if castle.treasury > 49:
                $ released_fix_rollback()
                #caravan bg blurred
                scene bg19 with fade
                $ moraleTrinkets = True
                "Throwing money at a problem until it went away was a time-tested strategy - and one twice as effective with a savvy goblin merchant by your side." 
                "Gold medals, expensive alcohols, and trinkets of all sorts were distributed to reward the loyal and placate the discontent." 
                "The novelty of the approach would wear off quickly - but the problem was abated - for now." 
                $ castle.treasury -= 50
                $ change_morale(5)
                return
                
            "Use slaves as sexual relief." if Dungeon.prisoners > 4:
                $ released_fix_rollback()
                #dungeon bg blurred
                scene bg8 with fade
                $ moraleSlaves = True
                "Among the demands of the orcs was more access to the human spoils of war."
                "It was distasteful, to be sure. But, represented one of the fastest ways to bring the tension with the orcs down to a simmer."
                "Rowan justified the choice by telling himself that the women they'd send would suffer less with supervision than had the orcs continued to rampage. That thought mostly worked."
                "Regardless, this would quiet the rage of the orcs. At least, for the moment."
                $ change_morale(5)
                $ change_prisoners(-2)
                $ change_base_stat('c', 3)
                $ change_base_stat('g', 5)
                return
                
            "Back.":
                $ released_fix_rollback()
                jump moraleMenu
                    
    "Employ help.":
        $ released_fix_rollback()
        menu:
            "X’zaratl suggestions." if RowanXzaratlInfluence > 2:
                #dark sanctum bg blurred
                scene bg23 with fade
                $ moraleXzaratl = True
                "X’zaratl was ecstatic to see him ask her for help, and she provided it in spades, without a moment of hesitation." 
                "“Flatter him.” “Scare her.” “Promote him.” All day, she followed him as he reviewed his forces, whispering advice as she hanged off his shoulder." 
                "By the end of it, he saw his men look at him with some degree of respect. But he couldn’t say what convinced them - X’zaratl suggestion, or the sight of a powerful succubus following his every step."
                $ RowanXzaratlInfluence +=1
                $ change_morale(5)
                return
                
            "Shaya manipulation." if shayaMenuCount > 0:
                $ released_fix_rollback()
                #brothel bg blurred
                scene bg24 with fade
                $ shayaMorale = True
                "When Rowan approached Shaya about his problems, he found her all too pleased to be of service." 
                "All she'd asked in return was a promise he'd remember her willingness to help him, the next time he needed someone to confide in."
                "At her command, the brothel allowed in far more orcs than usual and at a discount. Shaya's girls would not be pleased with the change in customer base. But he trusted the spy mistress to keep them safe."
                "Soon, he found reports of orc misbehaviour had lightened. All their...exertions...were going another direction. But, such a distraction would not last forever…"
                #Add -10% to all spy efficiency - TODO AFTER MECHANICS CHANGES (not now)
                if Dungeon.prisoners > 20:
                    $ change_morale(4)
                elif Dungeon.prisoners > 10:
                    $ change_morale(5)
                else:
                    $ change_morale(6)
                return
          
            "Back.":
                $ released_fix_rollback()
                jump moraleMenu      
                
    "Leave it be.":
        $ released_fix_rollback()
        return
        
################################################

label alternativeMoraleFollowUp:

scene bg9 with fade
show rowan necklace concerned at midright with dissolve

"Rowan returned to his room, mind racing with competing ideas. The problem of morale among the orcs had gone too far out of hand. His prior efforts had pacified them for a time, but it was still a vexing challenge."
"He was so lost in his head that he hadn’t noticed he wasn’t alone."
                
show andras angry at midleft with dissolve

an "Servant."
                
ro "Lord Andras?"

if callingInAndrasSeen == True:
    ro "Is this about the situation with the orcs?"
    an "At least you have brains enough to figure that out. I’ve come to tell you that I’ve put an end to it. "

else:
    an "I’ve had enough of the trouble with orcs. Ransacking, rioting, mutinying at will. I’m here to tell you that I’ve put an end to it."
    
"Rowan paced in place, eyeing the demon carefully. He didn’t much care for the cryptic tone, nor Andras’ intervention."

ro "You solved it? How?"

an "By dividing the skin while the bear still lives, something I took excessive care not to do before."

show andras smirk at midleft with dissolve

an "But I can’t stay mad. Not when it allows me to do what you denied my father at Karst. When we finally break Solansia’s hold over the region, I’ll give your homeland a taste of a true demon invasion."

show rowan necklace angry at midright with dissolve

ro "This isn’t what we agreed to."

an "You should’ve thought of that before you decided to neglect your duties. But who knows - if you start trying, maybe you can still save your precious countrymen from the worst of it."

show andras smirk at edgeleft with moveoutleft

an "Oh, and Rowan. I know Cla-Min keeps trying to convince you to trade with the villages. {b}Don’t{/b}. I want to see Rosaria burn."

hide andras with moveoutleft

"The demon briskly stormed out of the room with a laugh on his lips. Rowan gritted his teeth - he failed, and there was no undoing that fact."  
"At the very least, if Andras was to be believed, morale would be less of an issue in the future…"

$ moraleEventsActive = False
$ castle.morale = 30
# Can no longer trade with villages - TODO
$ cant_trade_with_villages = True
$ andrasLootPromise = True
$ sack1Count += 1
$ sack2Count += 1
$ sack3Count += 1
return