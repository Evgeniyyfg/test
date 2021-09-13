init python:

    # Jezera and Shaya have personal time
    # Req Brothel exist.  High priority until change to NPC events or end date is extended.
    event('jezera_and_shaya_personal_time', triggers="week_end", conditions=('castle.buildings["brothel"].lvl >= 1',), depends =('rowans_reward',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Drider egg found (benediction)
    #Requires that the breeding pit exist and have an open space.
    event('drider_egg_found', triggers="week_end", conditions=('castle.buildings["pit"].lvl >= 1', 'castle.buildings["pit"].free_space >= 1', 'week >=4'), group='ruler_event', run_count=1, priority=pr_ruler)
    #Cliohna's Unwanted Results
    #Req:  Cliohna's hero studies
    event('cliohna_s_unwanted_results', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, depends=("cliohna_s_hero_studies",), priority=pr_ruler)
    #Breeding pit's first monster (worldbuilding)
    #Requires that breeding pits have a monster in them.  High priority.
    event('breeding_pit_first_monster', triggers="week_end", conditions=('week >=4', 'castle.buildings["pit"].free_space < castle.buildings["pit"].capacity'), group='ruler_event',
        run_count=1, priority=pr_ruler_high)
    #Drider gets loose (malediction, sex)
    #Requires that there be at least one drider in the breeding pits and four orc soldiers.
    event('drider_gets_loose', triggers="week_end", conditions=('castle.buildings["pit"].driders >= 1', 'castle.buildings["barracks"].troops >= 4', 'week >=4'),
        group='ruler_event', run_count=1, priority=pr_ruler)


label jezera_and_shaya_personal_time:
# Jezera and Shaya have personal time
# Req Brothel exist.  High priority until change to NPC events or end date is extended.

scene bg24 with fade
show alexia 2 necklace neutral at midleft with moveinleft

al "Hello, Shaya?"

"Alexia glanced around the brothel's entrance, looking for the operator and trying to ignore the sounds of the other residents engaged in other activities. A male slave with a particularly well-sculpted chest made this rather difficult."

#al blush
al "Oh, uh, no! I’m looking for Shaya."

"She stepped carefully through the strangely well-maintained building. The scent of the place left the strongest impact. Strong spices and incense almost entirely covered the stink of bodily fluids. The keyword being 'almost'."
"After stepping around the back of the counter, she knocked on the door to the office.  This unintentionally pushed it open. But, Alexia didn’t see anyone inside."

#al confused
al "Is there anyone in here?"

"The woman glanced over her shoulder to see if anyone was watching her, then slipped into the room while closing the door behind her."

#al serious
"The room was dominated by a small private stage with several couches surrounding it. There were two other areas divided by screens: a sleeping area and a dressing area. They were also deserted. A separate locked door went off to the side. Perhaps where she did office work?"
"Shaya's quarters had a similar level of excessive decoration and finery that the rest of the brothel had, but a much more imperial feel. This looked like a place where kings and lords were personally attended."
"Alexia brushed some hair over her ear. Did Shaya design even her personal quarters for the act of entertainment? "
"She sighed and sat down on the bed. She’d come to learn more about the place and its role in the Bloodmeen ecosystem. Was there someone else at the brothel she could ask instead?"

if all_actors["alexia"].corruption < 31:
    "She blushed slightly. Shaya had a reputation as Jezera’s confidant, so talking to her was one thing. On the other hand, asking an actual whore…?"

"But, then came the sudden sound of the door opening behind her. With it a pair of female voices. Without thinking, Alexia rushed towards the sliding screen in the corner."

show alexia 2 necklace concerned at midleft with dissolve
show jezera neutral behind bg24

je "...always short something, so revisions are common."

show alexia 2 necklace concerned at edgeleft with moveoutleft
hide jezera

show jezera happy at midright with moveinright
show shaya neutral at edgeright with moveinright

je "Hrmmm. I don’t recall all of these decorations. I thought I had it exact, but you messed it all up!"

sha "Hush, {i}Jezer’aca{/i}. The original back room was dull. In my version, it will be dressed for the role in the play assigned to it."

"The half-demoness took a seat on one of the couches, directing Shaya to take the spot next to her, as if she were the one who the room belonged to. But, the brothel madam dutifully took the requested position. "

#jez smirk

je "Since we’re in private, regarding what we discussed…"

sha "It’s done, Mistress."

je "And he’s placed the item in her chambers? My marvelous little plan will not work unless it’s exactly where I directed it to be."

sha "...I have been gone too long then. Once, you’d have trusted my word alone. If you plan to start doubting me now…"

show jezera displeased at midright with dissolve

je "Psh. Don’t start with me, girl. Save the crocodile tears for your boy toys."

sha "Just because a thing may not work, does not make it not worth doing, Mistress. On a cold night, the game is its own reward."

#jez smirk
show jezera happy at midright with dissolve
show shaya happy at edgeright with dissolve

je "The game is its own reward? Simply absurd. Madam Amoria taught you to talk like that? Does that poetic nonsense actually work?"

sha "...S-sometimes…"

je "You think too highly of old tutors. If she were half so good as you think, she’d have conquered the empire with her snatch by now."

sha "Y-yet you were the one who...mmmf...paid for it, Mistress."

show jezera neutral at midright with dissolve

"Jezera sighed and let go of Shaya. The freed woman gasped and ran a hand along her chest. Alexia sat transfixed. Another person might have been unnerved by Jezera’s aggressive casual sexuality, but Shaya barely seemed perturbed."

sha "It is a strange thing, however, being lectured on brevity and simplicity by a woman with your history in schemes."

je "What are you implying, girl?"

sha "There is no need to imply anything, Mistress. Half your plots amount to hot air and an orifice stuffed with unpleasant fluids."

"Jezera scoffed."

je "Only the odd little trifle. My true aims have miraculous success rates. Now that you’re here, you’ll see the full weight of my skill again."

sha "So you say."

"Shaya bowed her head. Yet, something didn’t feel especially servile about it. Jezera paced close to Shaya. Close enough to bring their height difference to stark contrast."

je "And not another word about Amoria. Try to remember darling, teachers have their uses. But, there’s only one person in this world you truly need to listen to."

sha "I’ve never forgotten. Never ever."

show jezera happy at midright with dissolve

"A faint smile crept onto Jezera’s face."

je "Let’s get that veil off, shall we. There’s no purpose hiding your face from me. My perfect prize."

sha "Of course…"

"Jezera reached up and tore the veil away. Alexia’s breath caught in her throat at the sight revealed."
"She’d always presumed Shaya would be beautiful beneath the veil. But, the vision beneath was eerie in it’s perfection. Not a blemish. Not a feature too large. Even Jezera’s face almost looked plain by comparison."
"If her entire job was seduction, surely keeping such a thing hidden would be a perplexing misstep..."
"Jezera’s fingernails traced over Shaya’s skin softly, with the carefulness that one holds a precious heirloom."

je "My {i}Shay’aca{/i}…"

sha "Mistress..."

je "My perfect girl...I should have brought you sooner…"
je "The only one I can rely on..."

sha "Always…."

scene cg188 with fade
show jezera happy behind cg188
pause 3

"Jezera took the lead. She took a step forward and drew Shaya’s face to hers. The olive skinned woman exhaled sharply, but dutifully lifted lips. Their bodies intertwined."
"Soft moans emerged from the meeting. This was no chaste affair. Shaya has taken on the passive role, but the surging of her head and subtle gyration of her body made clear she was no disinterested partner. It had the desperation of lovers, long separated."
"Alexia sighed softly. She’d never seen Jezera act intimate with anyone before. Without thinking, her hand brushed against her thigh. From her hidden vantage point, she was forced to watch these two women."
"The effect it was having on her was..."

menu:

    "“...Really arousing.”":
        $ released_fix_rollback()
        $ alexiaTouching = True
        "...Really arousing. For a moment, Alexia forgot where she was and got lost in the sights, sounds, and smells of these beautiful women in the midst of passion."
        "She bit down on her lips. Her fingers had slipped inside her panties. The urge to touch herself had been too strong. Now she was timidly playing with her clit."
        $ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 1)
        $ change_corruption_actor('alexia', 3)


    "“...Not too much to stand.”":
        $ released_fix_rollback()
        $ alexiaTouching = False
        "Not too much to stand. Regardless of what Jezera and her lover were doing, Alexia didn’t lose sight of two critical facts. First, that she was not supposed to be here. Second, what Jezera would do if she caught Alexia eavesdropping."

scene bg24 with fade
show alexia 2 necklace aroused at edgeleft with dissolve
show jezera happy at midright with dissolve
show shaya happy at edgeright with dissolve

"After a small eternity, the kiss broke. Shaya was left half dazed for a moment. The sound she emitted was something akin to a purr. Naturally, Jezera smirked at that."

#jez smirk

je "{i}The game is it’s own reward, huh{/i}? Those were your words?"
je "Well, sweet sister, let’s put that to the test. Let’s pretend I was one of those silly boys coming to call on you."

"Jezera walked over to the large sofa by the wall with her hands on her hips. When she sat down, she made a dramatic show of crossing her legs and spreading her arms out along the back of the furniture."

je "{i}Seduce me.{/i}"

"The kiss must have had quite the effect on Shaya, as she was left on wobbly legs. Alexia had never seen the woman so unsteady. After a few seconds of deliberation, Shaya went down on both knees. Her normally piercing ochre eyes fell to the carpet."

show shaya neutral at edgeright with dissolve

sha "Mff...but it’s you. You know well why I’d find that a troubling task…"

je "Tsk. And here I was expecting more interesting things from you after all of that word poetry. My {i}Shay’aca{/i}, you know what I think of those with mouths to talk and no legs to walk."
je "Here, I’ll make it easier for you."

#jez happy

"Jezera cleared her voice. When she spoke again, it was in the squeaky voice of another woman entirely. None of her usual dulcet tones. She even took on a backwoods Rosarian accent."

je "H-hello, I’m Torinthia. I heard from my husband about this place...he said I could come here for a...good time. You are Shaya, right?"

#jez smirk

"Just as fast as it changed, Jezera’s voice came back. Slithering and powering."

je "{i}Seduce me, pet.{/i}"

#jez happy

"There was a moment of hesitation. Alexia could see the thoughts scrolling over Shaya’s face. Someone who spends most of her hours veiled is often not practiced hiding her feelings from her expressions."

show shaya happy at edgeright with dissolve

"But, slowly, Shaya began to rise to her feet. The change was obvious at once. The cock in her hips. The subtle smile that had formed."

sha "Torinthia, you said? That’s a lovely name. "
sha "And you needn’t worry for a moment, sweet one. You’re in the best of hands with me. Pleasures one could never even explain to their husband can be had here."

"She swished her way over to the couch, swaying with every step. Jezera scrunched up her shoulders and adopted a strangely diminutive pose. An un-Jezera-like pose."
"Meanwhile, Shaya went back to the cabinet to select some kind of tool or implement. Alexia watched with rapt interest."

if alexiaTouching == True:
    "Alexia’s finger idly circled her own outer lips. With the intensity simmered, so had her wanton explorations. But, her digit remained in place, keeping her body teased in case Jezera and Shaya’s game warmed up."

else:
    "For all her curiosity, Alexia was still clear headed enough to notice this was an opportunity. Shaya and Jezera had both moved away from the door. They were also both distracted. If there was a moment to escape, it was now."
    
menu:
    "Escape.":
        $ released_fix_rollback()
        "Alexia sealed her eyes shut. It would be risky. But, would it be riskier than staying and spying on a woman with a reputation for her treatment of enemy spies?"
        "She moved fast and cat-like, crawling to the door. It was not easy to ignore the impulse to look back. But, if she hesitated for a moment between the screen and the door, then it would be little different from simply presenting herself to them."
        scene bg14 with fade
        show alexia 2 necklace concerned at center with moveinright
        "There was no sound of disturbance as the door opened, and no sign of being followed as she slipped from the room."
        "On her way back to Rowan’s room, her breath caught in her mouth. What exactly had she just seen?"
        if alexiaJezObedient == False:
            "Still, other elements of the encounter still stuck with her. In particular, elements of the earlier conversation with Shaya. To her ears, most of it sounded like simple interpersonal gossip."
            "But, sometimes gossip could be of use. Perhaps it might be valuable to Rowan to hear about some of these details?"
            "Though, it might also be wrong of her to violate Jezera’s boundaries by sharing what was surely a personal encounter…"
            menu:
                "Tell Rowan.":
                    $ released_fix_rollback()
                    show alexia 2 necklace neutral at center with dissolve
                    "Alexia narrowed her eyebrows. There was no question about it. When she returned to Rowan this evening, it would be with new details about Jezera and Shaya’s relationship."
                    "She planned to tell him about how Jezera had been the one to arrange for Shaya’s training as a courtesan. She also would give him a sketch of their intimate close relationship."
                    "Hopefully….hopefully it would be of use."
                    $ shayaClue3 = True
                    $ shayaClueScore += 1
                    
                "Keep Jezera’s Secrets":
                    $ released_fix_rollback()
                    "Alexia shook her head. There was no way she could tell Rowan, or even tell anyone about what she’d just seen. It would be...wrong…."
                    $ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 1)
        return      
                    
    "Stay and Watch":
        $ released_fix_rollback()
        "Alexia shook her head softly. They were distracted now, but were they truly so lost in their little game that they would not notice the door creaking open?" 
        "Better to stay and watch...at least a little while longer…."


####################################
label .jezShayaSex:

"Alexia’s patient wait was rewarded when Shaya returned from the closet. She had to cover her mouth to prevent from making an audible gasp. Shaya was standing wearing an unusual golden harness over her pelvis...a harness meant to hold up a gleaming shaft, where a man’s would be."
"A golden strap-on."

sha "Now then, my dear. Shall we begin?"

je "Oh! My word!"

scene cg68 with fade
show jezera naked happy behind cg68
show shaya happy behind cg68
pause 3


"Shaya pressed down softly on Jezera’s back. Her form arched beneath her hand, stretching her ass further out. Jezera’s bare sex brushed ever so softly against the dildo."
"But, Shaya didn’t put it in Jezera’s sex. Instead, the rod slid into her ass."

sha "Hush now, pretty one. Let me take care of you.~"

"Jezera let out a long high pitched moan in the woman’s voice. Her his bucked slightly, pushing the mass into her rear. Shaya held her steady, working inch after inch of the apparatus in. The further in, the more Jezera’s body yielded."

je "M-my husband never…"

sha "Then it is good I am not your husband."

if alexiaTouching == True:
    "Alexia’s fingers sunk deep inside her own pussy. Whatever restraint she had regained in the break in passions was erased in an instant."

"Shaya rolled her hips artfully. Not the hard eager pounding of a man, but the controlled movement of a woman working her art. The golden shaft was visible in the light for a mere moment before plunging softly back inside the other woman."

sha "And I shall not tell him if you don’t. It can be my sweet gift to you. A memory for when you’re in bed with him…"

je "Mfff….harder…"

sha "As you wish."

"Shaya’s nails dug into Jezera’s hips. It was a presage of a change in her pace. There was still the intense rhythm and gyration of Shaya’s carefully controlled hips. But, now it was at a faster pace. Alexia could barely keep up with it."
"Jezera’s eyes widened. There was a delay of a few seconds, as if her body was still processing the new sensation. Then, the high pitched girlish moaning returned. Only louder and more frantic. "
"Alexia faintly wondered if it could be heard outside. Surely not. The room must have had thick walls. A brothel madam would not want to be overheard, either in plotting whispers or passionate whispers."

if alexiaTouching == True:
    "In truth, such thoughts had become near impossible for Alexia to maintain. She was totally overcome by the act of voyeurism. Her fingers cravenly attempting to eke pleasure from her clit had taken on the same rhythm as the pounding of the fake cock inside Jezera."
    "In a strange way, she had become just another participant in the scene."

"Shaya’s lips parted softly and a pant escaped. She was the one in control of the pace. She wasn’t even the one being penetrated. But, the unmistakable signals of lust dominated her features."
"Jezera may have been on bottom, but she was no mere passive receptor here. Her body pumped forward and back to the rhythm set by Shaya. The effect was quite intense. Her ass hitting Shaya’s body made constant slaps ring out through the room."
"She was moving her body hard. And it was forcing the artificial penis deep into her."

je "Ah. Ah. Ah."

"Their entire bodies seemed to participate. Jezera’s head rolled upwards. Her fingers dug into the upholstery. The energy seemed to be spreading everywhere. Shaya was not immune. Her chest shook and her breath had taken on a desperate airless pant."
"At some point, Jezera seemed to have set the pace. Where once Shaya’s practiced gyration had been pounding into Jezera’s body, now it seemed that the demonesses’ wanton backwards thrusting were stronger. "
"It was as though her body were challenging the fake cock to go deeper and deeper inside of her every time. To make it hit places that Alexia could not imagine meeting sensation."

if alexiaTouching == True:
    "Alexia thrust out her hips, rolling them forward and back from her kneeling position. It was too much for her. If this continued, she might actually moan out loud..."

je "Y-you’re enjoying, ah...you’re enjoying this too, right?"

sha "Yes."

je "Mfff. I can’t stand it anymore. I’m going to…"

sha "Y-yes…"

je "I’m going to…"
je "..."
je "Hehehe."

"Alexia saw the moment Jezera flashed an evil grin. But, everything that happened afterwards was a whirlwind of motion."

scene cg124 with fade
show jezera naked happy behind cg124
show shaya happy behind cg124
pause 3

"Jezera had not only pushed the strap-on from her body, but dragged Shaya into her lap. The full grown woman was like a doll to be manhandled."

sha "Mistress, I-"

"Shaya tried to regain her bearings and speak. But, Jezera shoved a breast to her lips silencing her. Alexia was left gasping to herself. In mere moments, Shaya had gone from the top to little more than an infant."
"As if to emphasize it, Shaya timidly opened her mouth and took in Jezera’s nipple. She was suckling it softly."

je "Shhh. No more words from you now."

"Now back in control, Jezera fingers danced their way up Shaya’s thigh. At some point, Shaya’s strap on had been discarded, but it must have been in the midst of Jezera taking back control."
"Now, there was nothing in the way of Jezera’s fingers as they danced along the exterior of Shaya’s sex."

je "Mmm. That’s a good girl. Not a bad start."

sha "Mfff."

"Shaya’s body jerked and squirmed in Jezera’s hands. Little brushes against her clit would have her jerking and hard suckling at Jezera’s teat."

je "Still, not quite enough discipline. By the end, you’d already melted back into a submissive little fucktoy, sweet {i}Shay’aca{/i}."
je "Clearly, you need some more...instruction."

"Gagged as she was, Shaya could merely moan into Jezera’s nipple. Her knees spread slightly, pushing her sex against Jezera’s hand. Any surviving discipline was gone."

je "But, worry not. You’re back with Mistress. {i}We have all the time in the world. I’ll make sure you’re perfect for me{/i}."

"With that, her fingers slid inside of Shaya’s body…"

scene bg24 with fade
if alexiaTouching == True:
    show alexia 2 necklace aroused at edgeleft with dissolve
    "...An action that was served as Alexia’s final straw. Watching Jezera fuck Shaya with her fingers was too much for the already over-stimulated voyeur."
    "Alexia had to bite down hard on her finger so her orgasmic cry wouldn’t be too loud. Her hips jerked slightly, and beneath her a very small puddle had started to form."

else:
    show alexia 2 necklace shocked at edgeleft with dissolve

"Still, even as entranced as Alexia had gotten in her viewing experience, she was not so far gone as to not realize what this moment meant. If Shaya and Jezera had been distracted before, they simply had to be near absent now."

if alexiaTouching == True:
    "Still shaking, Alexia crawled her way slowly to the door. There was no reaction from the two moaning women as she slipped from the room."
    
else:
    "Alexia crawled her way slowly to the door. There was no reaction from the two moaning women as she slipped from the room."
    
scene bg14 with fade
show alexia 2 necklace neutral at center with moveinright

"Her breath came hard as she stomped down the hall. The memory of the illicit passions she’d watched replayed over and over in her head."

if all_actors["alexia"].corruption < 31:
    show alexia 2 necklace concerned at center with dissolve
    "What kind of person would stay and watch something like that?"
    show alexia 2 necklace neutral at center with dissolve
    
if alexiaJezObedient == False:
    "Still, other elements of the encounter still stuck with her. In particular, elements of the earlier conversation with Shaya. To her ears, most of it sounded like simple interpersonal gossip."
    "But, sometimes gossip could be of use. Perhaps it might be valuable to Rowan to hear about some of these details? He would not have to hear about the entire encounter, but some of this information could be useful to him."
    "Though, it might also be wrong of her to violate Jezera’s boundaries by sharing what was surely a personal and intimate encounter…"
    menu:
        "Tell Rowan.":
            $ released_fix_rollback()
            "Alexia narrowed her eyebrows. There was no question about it. When she returned to Rowan this evening, it would be with new details about Jezera and Shaya’s relationship."
            "She planned to tell him about how Jezera had been the one to arrange for Shaya’s training as a courtesan. She also would give him a sketch of their intimate close relationship. Albeit, there was no need to go into specifics."
            "Hopefully….hopefully it would be of use."
            $ shayaClue3 = True
            $ shayaClue4 = True
            $ shayaClueScore += 2
            
        "Keep Jezera’s Secrets.":
            $ released_fix_rollback()
            show alexia 2 necklace aroused at center with dissolve
            "Alexia shook her head. There was no way she could tell Rowan, or even tell anyone about what she’d just seen. It would be...wrong…."
            $ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 1)

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label drider_egg_found:
#Drider egg found (benediction)
#Requires that the breeding pit exist and have an open space.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show draith neutral at midright with moveinright
show skordred neutral at skorright with moveinright

ro "Something to report?"

sk "Aye. Excavashun' team stumbled on an old nest way down in the ruined catacombs ah tha old castles. We found eggs, so I called Draith to take a look."

dra "They're ancient drider eggs, several centuries old."

"Rowan set down his work and straightened up."

ro "But even after all this time they're still viable?"

show draith happy at midright with dissolve

dra "Yes! Well, one at least."

sk "Right, I'll leave ya two to it then."

hide skordred with moveoutright

dra "Drider eggs go into hibernation when they're cold and only hatch in a warm environment. They're human-spider hybrids, but are endothermic so can't survive really cold places."

ro "I know what a drider is, Draith."

show draith neutral at midright with dissolve

dra "Right, sorry sir. Since the excavation teams have breached the chamber, I don't expect these eggs to last in there, so I'd like to hatch what I can now and add them to the pit."
dra "If you can't spare the cage space, I understand."

#player can choose whether they want a drider or not, if pits capacity is full, first option should be greyed out

menu:
    "Gain a drider." if castle.buildings['pit'].free_space >= 1:
        $ released_fix_rollback()
        #line below should display correctly depending if player already has a drider or not
        if castle.buildings["pit"]._driders >= 1:
            ro "Please hatch the egg Draith, we can definitely use another drider."
        else:
            ro "Please hatch the egg Draith, we can definitely use a drider."
        show draith happy at midright with dissolve
        dra "Understood sir! I'll get started right away."
        #Gain a drider and end event
        $ castle.buildings["pit"]._driders += 1
        return

    "Leave the cell open.":
        $ released_fix_rollback()
        ro "Sorry Draith, but I don't want you to hatch that egg."
        #dra sad
        dra "Alright, understood sir."
        #end event
        return
return
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label cliohna_s_unwanted_results:
#Cliohna's Unwanted Results
#Req:  Cliohna's hero studies

$ unwantedResults = True

scene bg12 with fade
show cliohna neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "I got your message, what would you like to talk to me about?"

"The woman put down her work immediately, but didn't turn to speak to Rowan."

ro "Is now a bad time?"

cl "No."

"However, she still didn't turn around or look at the man she'd called here."

ro "Well then... what is it?"

"Finally she looked at him, revealing an expression that Rowan hadn't seen on her face before. In fact, he couldn't remember seeing much of any expression on her face."

show cliohna angry at cliohnaright with dissolve
cl "It is not through any fault of yours, but you have vexed me greatly."

"She looked, annoyed? Frustrated? Maybe even exhausted?"

cl "Since you were gracious enough to provide me with your seed, I have spent nearly all of my personal time attempting to discern what, if any, magical power you have."
cl "Again, and again, and again, all of my efforts have disproved every possible avenue that could conceivably grant you such potential. I can only conclude, with great reluctance, that you truly are an ordinary man."

"Rowan spread his arms wide and gave a big shrug."

ro "Well, I did warn you about that, though it does sounds like you did the most thorough test anyone's done of me."

"The sorcerer broke eye contact and started drumming her fingers on the table for a few seconds."

"Right away Rowan could tell that there was something else she hadn't said yet, some people had these kinds of ticks when they were trying to decide if they should say something or not. Considering it had to do with him, the hero decided it was worth pushing her just a bit."

ro "With all those tests, surely there was something interesting you found out?"

show cliohna neutral at cliohnaright with dissolve

"Cliohna let out a long sigh and stopped rapping her knuckles."

cl "Yes, I did detect what appeared to be faint magical potential within you at first that I couldn't eliminate, but the more I looked the more I realized that it was someone else that you'd been in contact with. There were other auras, but this one I couldn't identify."

ro "Really? Who do you think it was?"

cl "I assume it was someone you met while out travelling, there was no demonic energy to it and I've already tested the major castle staff you work with every day."

ro "I do encounter a great number of people like that, but would they really have rubbed off their aura's onto my seed from such a short visit?"

cl "No sweethearts, no repeatedly visited acquaintances?"

ro "No."

cl "Fascinating, then there must be someone in the castle that I missed. Who have you been sleeping with? Anyone you've spent a significant amount of time in the presence of over the last year?"

ro "Well...."

scene bg12 with fade
show cliohna angry at cliohnaright with dissolve
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral behind bg12

"It was nearly an hour later and Cliohna was just finishing a quick surface test on the most likely person that Rowan thought it could be."

ro "So, what's the results?"

cl "I cannot believe this.  It defies all logic.  How is it you have nothing, YET SHE DOES?!"

show rowan necklace shock at midleft with dissolve

"That was the first time Rowan had ever heard Cliohna raise her voice.  Feeling the air start to crackle with static, the hero wisely started to back off."

al "Uh... should I leave?"

hide alexia
show alexia 2 necklace concerned at edgeleft with moveinleft

"The man hastily mimed to his wife to stay silent while the sorcerer continued to fume.  He took her hand and the two edged away together."

show bg12 with flash

cl "Drast!"

"She almost screamed that while the test tube in her hand exploded with a blast of crackling electricity.  The couple had nearly reached the main hallway for the library."

show bg12 with flash

cl "A FUCKING HOUSEWIFE!"

hide alexia with moveoutleft
hide rowan with moveoutleft

"Another burst of energy flashed around the place where the tube had been once again, then another. At this point, Rowan and Alexia were able to slip around a corner and hurry out of the library, leaving the muffled cries of indignant rage behind them."

scene black with fade

"It would probably be best to wait a time before approaching Cliohna about this subject again. Even so, this revelation was quite a bit to sink in, apparently Alexia had magical potential!"

#end scene
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label breeding_pit_first_monster:
#Breeding pit's first monster (worldbuilding)
#Requires that breeding pits have a monster in them.  High priority.

scene bg25 with fade
show draith neutral at midright with dissolve
show andras displeased at edgeright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "Master, Draith, I understand we have our first monster now?"

show draith happy at midright with dissolve
show andras happy at edgeright with dissolve

an "Ah servant, how wonderful for you to join us for this glorious occasion! Let us enjoy this together."

dra "Then, if you handsome men would follow me?"

"The dark elf lead the small group down the row of cages until they arrived at one where several orc handlers were attempting to either coax or force out the creature that was contained inside."

#if first monster is a drider
# TODO: ignore monster type for now

"Finally a fully grown female drider came skittering out of the cage and pounced onto one of her handlers.  Rowan started to run forwards, but was stopped by a hand from Draith, who simply indicated he should watch."
"Instead of biting the orc with her mandibles, the creature started caressing her breasts and tethering strangely side to side. Two of the other handlers climbed onto her legs and started molesting her at the same time, which the drider seemed to enjoy."
"Once they got closer, Rowan could see now that the creature seemed to be mating with the orc she had tackled earlier and the others had joined in the fun. In-spite of the carnal display, the hero couldn't help but take note of the size of the creature and how quickly it had moved."

dra "Driders are fascinating creatures. No culture or societies and almost impossible to communicate with, but dangle the prospect of sex in front of them and they can be taught to do almost anything."

#rejoin

an "Marvelous. This creature will be of great use in our armies, I'm sure. How soon will be able to breed more?"

dra "Breeding will be out of the question until we can upgrade our facilities, but thanks to Rowan's efforts we'll have no problem completely filling up all our available cells with the site he found."
dra "The limiting factors right now are only space and supply. With the right know how and funding, Skordred will be able to help with the problem of space."
dra "As for supply, If Rowan can find more nests of the same species, we'll be able to accelerate how quickly we can raise them. I'll also be able to raise other creatures if their nests can be found, assuming we have the space for them."

show andras displeased at edgeright with dissolve

an "Very well. Rowan, once we have a few more of these things down here, I hope you can find a nice innocent village I can cut their teeth on."

show andras angry at edgeright with dissolve

an "Then we'll see first hand just how mighty these monsters are!"

#End event
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label drider_gets_loose:
#Drider gets loose (malediction, sex)
#Requires that there be at least one drider in the breeding pits and four orc soldiers.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show draith neutral at midright with moveinright
show orc soldier neutral at edgeright with moveinright

#dra worried
dra "Rowan! Rowan! One of our driders broke away from training and escaped into the tunnels! Now she's on a raping spree and moving towards the outer tunnels!"

ro "What? How did this happen?"

#dra sad
dra "It's my fault, this particular monster was much wilder than most and didn't respond to training well. I mean, she loved having sex as much as any other drider, but she wouldn't obey anyone for it. I should have been more careful with Black Ness."

"The hero strode forward and clapped a hand onto the monster breeder's shoulder."

ro "Everyone makes mistakes and it's too late to change anything about that now."

#dra neutral
dra "Yes sir. Ness will probably escape into the forests soon and we'll never be able to catch her then. What should we do?"

menu:
    "Risk your own body as bait for a trap to recapture the female drider.":
        $ released_fix_rollback()
        jump driderSexScene

    "Send in a squad of orcs to attack and capture it.":
        $ released_fix_rollback()
        ro "Soldier, go gather a squad of orcs and bring them to the outer tunnels. Myself and Draith will go ahead and plan our attack."
        os "Yes boss!"
        scene black with fade
        "The fighting was fierce and cost the lives of several of the orc soldiers, but the escaped drider was back in the pits by the end of the day and Draith started working on devising a new way to train it."
        "The triumph ended up being quite the story among the soldiers and they frequently discussed it among their friends. While this blunder had cost the lives of several of their fellows, the orcs as a whole felt better afterwards."
        #Lose four orc soldiers, gain 3 morale.
        $ castle.buildings["barracks"].troops -= 4
        $ change_morale(3)
        #end event
        return

    "Let it escape.":
        $ released_fix_rollback()
        ro "Let it go, it isn't worth it at this point. Pull everyone out of the drider's path so we can avoid anymore damage."
        os "Wah!? Yous a coward!"
        ro "I gave you an order soldier, carry it out."
        hide orc soldier with moveoutright
        scene black with fade
        "The drider fled through the underground passages until it had stumbled its way out of the castle and into the forests surrounding Bloodmeen."
        "There was no major damage or casualties after its escape, but many of the soldiers were upset afterwards that such a beast had apparently gotten the better of them."
        #lose 1 drider, lose 5 morale.
        $ castle.buildings["pit"]._driders -= 1
        $ change_morale(-5)
        #end event
        return

label driderSexScene:

ro "You said that this drider is still very interested in sex, right?"

dra "Yeah, she's left quite a few dazed orcs in her wake."

"Rowan nodded and turned to the orc soldier that had accompanied the dark elf."

ro "Soldier, go gather a squad of orcs and bring them to the outer tunnels. Myself and Draith will go ahead and set a trap for the drider, then you will capture it."

#dra worried

os "Yes boss!"

hide orc soldier with moveoutright

dra "Wait, what do you have in mind?"

#tunnels bg
scene black with fade
show rowan necklace naked at midleft with dissolve
show draith neutral behind black

ro "Alright beasty, where are you? Hello? Ness?"

"He called out into the tunnels for the drider, trying to draw it into his trap. Surrounding the hero was a squadron of orcs with nets, handling rods, and a very worried dark elf breeder, all nestled into cracks and crevices or behind rocks."
"Rowan was quite pleased with how well he'd hidden everyone, after selecting this spot for the ambush due to how many good hiding places there were. Orcs didn't like sitting still like this, but their discipline held."

ro "Here, drider drider drider!"

dra " Rowan! That's not how you call out to a beast as noble as a drider!"

hide draith
#draith annoyed
show draith neutral at edgeright with moveinright

"The hero turned to the dark elf who'd poked his head out from behind a boulder with a look of annoyance."

ro "I'm afraid that handling monsters properly was never something I needed to learn before now, how would you suggest I proceed?"

dra "First off, stop covering your cock, make sure it's on full display! Then, make a chittering sound like this: Chita chita chit!"

"Suddenly something slapped the back of Rowan's head and he tried to wheel around to face what had attacked him. Unfortunately, this act caused him to become wrapped up in the sticky webbing that had been lobbed onto him."

ro "Oh no."

hide rowan with moveoutleft
show rowan necklace naked behind black

ro "Wahhhhhh!"

show draith neutral at center with moveinleft
show orc soldier neutral at edgeleft with moveinleft

dra "Rowan!"

scene black with fade

"The female drider caught Rowan in mid-flight and fled down the tunnels away from the ambush. He could hear Draith and the orcs calling after them and then launching into pursuit, but his captor soon outpaced them."
"With his upper body completely immobilized by the webbing, he couldn't do anything to get away from its grip, leaving him helpless in its arms as it sought out a refuge of some kind."
"Finally the drider slipped into a tiny side passage and dropped Rowan to the ground.  It darted about the hallway for a moment, then pounced onto his mostly nude body, grinding its softer underbody over his cock."

scene cg121 with fade
show rowan necklace naked behind cg121

"Like all driders, this creature appeared to be a giant spider, but with the torso, arms, and head of a pale skinned human instead of a spider head."
"The upper body wasn't entirely human, mandibles tipped with poison sprouted at the base of their jaw and the point where carapace gave way to skin."
"The lower body was mostly a black exoskeleton with hairs coming off of the legs and abdomen. At the back of said abdomen, which was almost as wide as Rowan was tall, was the drider's spinnerette which the creature had used to make the thread it had captured him with."
"Since he didn't seem the be going anywhere right now, the hero took a moment to study it's (her?) more human features. She looked to have been in her mid to late twenties, with a very fit muscled body."
"Her breasts were about average in size and there was a distinct hint of hips just before the body ended."
"Then there were the eyes, eight pools of black scattered around her head that occasionally peeked out around her soft silky white hair. At least the two main ones where eyes should be were possible to focus on to avoid being unnerved. Then Rowan retracted that thought."
"His attention was brought down to the creature's monstrous body, at the place where it was rubbing his groin. The stimulation had started to make his member grow hard, and now he could see that there was a sort of flap or slit there."

ro "(Her sex?)"

"Sure enough, once the creature realized that he was getting hard, those flaps split open and thick drops of goo started plopping out of it. Rowan only had a moment to look at the thing before the drider lowered itself down to engulf his member inside."

scene cg122 with fade
show rowan necklace naked behind cg122

"The man groaned as he was engulfed by her, sliding into a passage that was a mix of flesh and silk that clamped down onto his shaft."
"Once he was fully inside, the drider closed its eyes and made a soft chittering sound which he interpreted as a sigh of pleasure based on her body language."
"She didn't stop moving when he was completely inside her, immediately going into a steady rhythm of rising and falling on her legs. At the same time, she pressed her human arms down on his chest and leaned back with a look of contented arousal on her face."

ro "(Woah, for a vicious monster she's surprisingly cute like this.)"

"Another groan escaped the man's lips as the drider pressed herself down on him particularly hard in time with her sharply inhaling."

ro "(Did she just cum?  Already?)"

"If the drider had orgasmed, she showed no signs of being done and hardly even slowed her stride. Though now Rowan could feel his own peak approaching, given how strong and insistent her stimulation was, this wasn't surprising."
"Just as he let himself go and sent ropes of jiz into the monster's inhuman vagina, Rowan realized that he could hear the sounds of people nearby. Sensing his chance, he grabbed onto the drider's hands since they were within his reach and called out to his companions."

scene black with fade
show draith neutral behind black

"The drider realized almost immediately that it was in trouble, but was unable to disentangle itself from Rowan before the orcs got into the side passage and threw their nets over her."
"In desperation, she bit into Rowan with her lower mandibles and gave him a dose of poison to make him let go. However, she didn't get far and was subdued shortly afterwards."

dra "Sir? Rowan? Are you alright?!"

"Thankfully for Rowan the poison wasn't too bad and he hadn't gotten a big dose of it. Unfortunately he would still feel its effects for some time, along with the memory of mating with a monster."

#Rowan is injured.
$ take_damage(1)
#End scene.
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
