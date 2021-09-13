#Orc wants to lead
#Can trigger on either choosing to capture, or destroy a village

#randomly determine type of orc:
#flag 1 - Competent orc
#flag 2 - Foolish orc

init python:
    event('orc_wants_to_lead', triggers=('map_res_3', 'map_res_4', 'map_res_5',), run_count=1, group='village', priority=pr_map_res)
    event('old_hero_destroy', triggers=('map_res_3', 'map_res_4', 'map_res_5',), conditions=("week >= 4",'old_hero_event==False'), run_count=1, group='village', priority=pr_map_res)
    event('old_hero_occupy', triggers=('map_res_3', 'map_res_4', 'map_res_5',), conditions=("week >= 4", 'old_hero_event==False'), run_count=1, group='village', priority=pr_map_res)
    event('old_hero_trade', triggers=('map_res_3', 'map_res_4', 'map_res_5',), conditions=("week >= 4", 'old_hero_event==False', 'not cant_trade_with_villages'), run_count=1, group='village', priority=pr_map_res)
    event('the_dragons_path', triggers=('map_res_3', 'map_res_4', 'map_res_5',), run_count=1, group='village', priority=pr_map_res)
    #event('a_cheating_elder', triggers=('map_res_3', 'map_res_4', 'map_res_5',), run_count=1, group='village', priority=pr_map_res)
    event('village_spoils', triggers='village_destroy',  run_count=1, group='village_destroy', priority=pr_map_res)

label orc_wants_to_lead:
scene bg31 with fade
show rowan necklace neutral at midleft with dissolve

if renpy.random.randint(0,10) > 5:
    $ competent_orc = True
    $ foolish_orc = False
else:
    $ competent_orc = False
    $ foolish_orc = True

"As always, the strike force arrived incredibly quickly."

show rowan necklace shock at midleft with dissolve

"... So quickly in fact, that Rowan sometimes wondered if Jezera could actually open portals everywhere, but had him use predetermined sites just to mess with him."
"On one hand, it would be both incredibly petty to do, and so short sighted and enormously harmful to their overall efforts that only a power-tripping teenage girl could consider it a good idea."

show rowan necklace neutral at midleft with dissolve

"On the other hand… It would indeed be both incredibly petty to do, and so short sighted and enormously harmful to their overall efforts that only a power-tripping teenage girl could consider it a good idea."
"Rowan rubbed his temples and decided that maybe it was better not to think about it."

"Regardless of whatever space bending abilities his orcs possessed, they were now present, ready to receive their orders – but before Rowan could give them out, one of the orcs stepped forward and interrupted him quite rudely."
"The orc demanded an opportunity for him and his people to prove themselves to their demon overlords. Rather than follow Rowan's lead, he alone wanted to command the group, to show the twins they didn’t need Rowan to babysit them."
"Usually, while he rarely took to the field himself, it fell to Rowan to devise the “battle plan” when attacking keeps and villages. In case of the villages, the term had to be used quite loosely."
"Rosaria’s settlements consisted almost exclusively of peasants (as one would expect) and had next to no serious fortifications."

if avatar.corruption > 74:
    show rowan necklace angry at midleft with dissolve
    "A prospect that was growing increasingly tempting by the moment."
    "Why, exactly, was it his bloody responsibility to make sure the orcs didn’t burn anything of worth, or allow the villagers to escape?"
    "Why was he walking around the entire bloody realm, locating settlements that anyone with a functional eyesight could easily locate on a Goddess damned map?"
    "The twin’s told him they needed him to help them manage the castle, so why exactly was he overseeing every single, no matter how fucking minor task, instead of focusing on stuff that’s actually important?!"
    "Oh, that’s right."
    "Because Andras was too fucking busy trying to fuck his wife to train his fucking troops properly, while Jezera’s concept of leadership consisted of a) Fucking the people she likes, and b) Stabbing the people she doesn’t like."

    if serveChoice == 4:
        "Rowan couldn’t believe he actually allowed himself to be convinced by two amateurs who think they’re hot shit just because their father was the literal fucking avatar of destruction."

    else:
        "He should probably be happy at how completely inept the twin’s were, but the moment the only emotion he could feel was his growing desire to smack the orc in front of him with something heavy, preferably a war-hammer."

    ro "“(...)”"

    show rowan necklace happy at midleft with dissolve
    ro "You know what? I have a better idea."
    "Smiling pleasantly, Rowan addressed the now confused orc."
    ro "How about you all charge into the village straight away, alright?"
    "For every piece of equipment damaged in battle, I’m cutting 5 fingers. Chosen out random. For every villager you kill, I’m sending you for 2 months of excavation works. For every five villagers dead, I’m executing one of you randomly."
    ro "Everything clear? Alright, go charge."
    "The orcs stared at him, dumbstruck."
    show rowan necklace angry at midleft with dissolve
    ro "I SAID CHARGE YOU DIMWITS!"
    show rowan necklace happy at midleft with dissolve
    "That did the trick. The orcs raised a couple of careful war cries, then rushed in the direction of the village."
    "..."
    show rowan necklace concerned at midleft with dissolve
    "..."
    show rowan necklace shock at midleft with dissolve
    ro "(Oh Goddess, what have I done?)"
    "Rowan watched, terrified, as the village descended into the usual chaotic infighting. Even from where he stood, a fair distance away from the settlement, he could hear the shouts and cries coming from the both sides."
    "It shouldn’t be happening like this… It shouldn’t..."
    show rowan necklace concerned at midleft with dissolve
    ro "..."
    "This shouldn’t have happened. He’d never… Let himself lose control like that. It wasn’t like him to let himself slip."
    "He was spending too much time with the twins. Their casual cruelty and disregard for others was starting to rub off on him."
    "How much longer till outburst like that become a common occurrence?"
    show rowan necklace neutral at midleft with dissolve
    "He couldn’t allow that. He had to get a hold of himself."
    "… Not that committing atrocities with a steady heart was any better."
    "Before Rowan could spiral into self-deprecation any further, he noticed an orc in the front signaling him the village was secured."
    "Self loathing could wait. It was time to assess the damage."

    scene bg1 with fade
    "The attack went… Well."
    "His makeshift threat worked. There were far less casualties among the villagers than usual."
    "But also far more peasants managed to escape. And his orcs… Looked beaten up, and thoroughly displeased with the outcome."
    "Rowan didn’t allow his inner conflict to show, and started giving up orders to clean up the whole mess."
    "He would ponder on his outburst later."
    $ change_base_stat('g', 5)
    $ change_base_stat('c', -3)
    $ castle.morale -= 10
    #village is captured or destroyed based on player choice
    return

else:
    if avatar.corruption > 49:
        "However, letting the orcs do as they pleased usually resulted in unnecessary damage and pointless loss of life. As annoying as it was to micromanage-"
        "-which is to say, pretty annoying-"
        "-doing so ensured the best possible result for every raid, loot wise."

    else:
        "However, letting the undisciplined orcs do as they wanted usually resulted in pointless deaths. Even if he had to do some despicable acts in the service of the twins, he could at least ensure innocent people wouldn’t die needlessly."

    "So Rowan wasn’t all too keen on letting some orc he knew nothing about lead the raid without his supervision. But giving the orcs a chance would no doubt improve the orc morale…"
    "And if the orc leading them proved to be competent, he could be a valuable asset to their army"

    menu:
        "Let him lead.":
            $ released_fix_rollback()
            "Without much enthusiasm, Rowan allowed the orc to proceed with whatever it was that he had planned."

            #if flag = competent orc
            if competent_orc:
                "Much to Rowan’s surprise, the attack went swimmingly. The orc split their forces into two groups and hit the settlement from both sides, preventing the villagers from getting away."
                show rowan necklace neutral at midleft with dissolve
                "It was more or less what Rowan planned as well, and by itself it was hardly impressive."
                "The fact neither group scattered in search of a fight when they entered the village proved the ambitious orc commanded enough respect within this particular strike force to maintain basic discipline."
                "Which usually meant he was chieftain material."
                show rowan necklace happy at midleft with dissolve
                "Orc commander standards weren’t particularly high."
                "Once the battle was over and Rowan inspected the end result, he offered some sparse word of praise to the orc, and made a mental note to promote him as soon he returns to the castle."
                "This should help keep the orcs in check."
                $ castle.morale += 5
                #village is captured or destroyed based on player choice
                return

            #if flag = foolish orc
            else:
                "The attack went about as well as Rowan expected – with the orcs rushing into battle without any plan whatsoever."
                show rowan necklace angry at midleft with dissolve
                "Why he believed even for second that this would go any other way, was beyond him."
                "Rowan covered his face with the hood of his cape, and quickly rode into the village to salvage the situation."
                hide rowan with dissolve
                "..."
                show rowan necklace concerned at midleft with dissolve
                "Some damage was already done, but somehow he managed prevent the chaos from spreading."
                "Half an hour later, the village was subjugated, and the orc he allowed to lead the charge knelt before him."
                show rowan necklace angry at midleft with dissolve
                "Rowan looked down on him, jaw clenched."
                if avatar.corruption > 49:
                    ro "Cut his head off."
                    "The orc stared in disbelief, eyes wide. He lunged forward – only to be stopped by his companions."
                    "Nobody wanted to be the one who told the twins their precious slave was killed by one of their own."
                    "Rowan turned around, and let the other soldiers carry out his order. His business here was done."
                else:
                    ro "Mine duty for three months."
                    "The orc grunted, displeased, but said nothing else. Rowan’s word was law."
                    "With the matter settled, Rowan turned around, and left the village. His business here was done, the orcs knew what they had to do."
                    #village is captured or destroyed based on player choice
                    #village drops in size if possible (TO DO LATER)
                    return

        "Stick to your plan.":
            $ released_fix_rollback()
            show rowan necklace angry at midleft with dissolve
            "But Rowan had no intention of gambling with human life. Coldly, he told the orcs they will stick to the original plan and if any of them even think about disobeying him, there will be consequences."
            "His soldiers grumbled in response, displeased, but nobody dared to voice further opposition."
            "Rowan gave them all their orders and, when the time was right, commenced the attack."
            "And as expected, everything went swimmingly, with minimal losses on both sides."
            "The only thing that really suffered was the orcs' morale, but that was a problem Rowan would deal with another day."
            $ castle.morale -= 5
            #village is captured or destroyed based on player choice
            return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Old Hero.
#Requirement: Week: 20+

#show normal village menu at first, then, split into two branches.
#branch 1 - if the player chooses to capture or destroy the village
#branch 2 - if the player chooses to trade with the village

#branch 1 - capture / destroy
label old_hero_destroy:
scene bg31 with fade
show rowan necklace neutral at midleft with dissolve

$ old_her_event = True
if avatar.corruption > 74:
    "Impatient to bring another village under the twins thrall, Rowan decided that this time he would deviate from the usual procedure and oversee the attack personally."
    "Quickly bringing order to the orc detachment that arrived from castle Bloodmeen, Rowan split his forces into three groups, surrounding the village and closing the usual escape routes."
    "At dusk, he ordered a simultaneous attack from all sides."
    "As always, the village could only offer a token resistance. Caught by surprise, a few men tried to fight back – only to be struck down."
    "It all went according to plan – until Rowan heard sounds of an actual fight going on near the center of the village. Displeased by the prospect of unforeseen complications, Rowan hurried his horse forward."
    "There, he saw a man in an old, battered armor, aided by a handful of young men, engaging his orcs."
    "Despite being vastly outnumbered and clearly fighting a lost battle, the villagers seemed determined to protect their village to the end."
    "Normally, Rowan would applaud such a display of heroism, except this time it was working against him. Without a second thought, he galloped forward and readied his sword."
    "The old man saw him coming – and at the last second turned in his direction, raising his own sword to parry the incoming blow. Too slow – years of peasant life must have dulled his reflexes."
    "Rowan’s blade made its way past his guard and struck the man right in the neck."
    "A young boy shouted in horror. Rowan slowed down, and turned around to observe how the last stand of the village defenders fell apart."
    "Without the old man shouting orders and encouragements, the remaining peasants quickly lost their spirit. Some turned around to flee, others threw their weapons down and begged for their life."
    "Others yet decided to give their life with their hero."
    "And they would do precisely that."
    "Soon, the battle was over."

    #if player chose to destroy village
    "Their defenders beaten down, the orcs scattered across the village, capturing people and grabbing anything that was of any worth to the Twins."

    #rejoin
    "Meanwhile Rowan inspected the now dead hero – the man who dared to oppose his forces, against all odds."
    "The wound was fatal – as Rowan intended it to be. The man bled out to death, red blood staining his clothes and armour."
    "His breastplate bore the insignia of Rosaria military."
    "Once, Rowan wore a similar armour."
    "Felt like it was an eternity ago."

    if avatar.guilt > 50:
        "Slowly, Rowan knelt besides the man. He said a silent prayer in his name, and closed his unseeing eyes."
        "… He lingered for a while, uncertain of his own feeling at the moment. But there was no use in regretting his actions now. Rowan stood up, and turned around without another word."

    else:
        "Rowan stared at the body for a short while, then turned around without a word."

    "This village was done with. It was time to move on."
    #capture or destroy the village based on player choice
    #lose 5 orcs
    $ castle.buildings['barracks'].troops -= 5
    return

else:
    "As always not so keen on seeing the result of his choices, Rowan ordered his orcs to attack without him. He would observe from a safe distance, only intervening if the situation called for it."
    "… The fighting went on a bit longer than usual and Rowan was slowly starting to worry something indeed went wrong."
    "He checked his equipment, still unwilling to participate in the attack – but as he lingered, he finally saw the one of his grunts exiting the village."
    "The orc signaled the village was pacified, and Rowan could safely take stock of the situation."
    "Apparently the village elder was some sort of war veteran, who managed to organize a makeshift defense force at the center of the village. He was dead now, but because of his interference they lost more soldiers than usual."
    "An unpleasant surprise, but these things happened. Rowan nodded to the orc and told him to proceed with the rest of the plan."
    "Another day, another village at the mercy of the Twins."
    #capture or destroy the village based on player choice
    #lose 10 orcs
    $ castle.buildings['barracks'].troops -= 10
    return

label old_hero_occupy:
scene bg31 with fade
show rowan necklace neutral at midleft with dissolve
$ old_her_event = True
if avatar.corruption > 74:
    "Impatient to bring another village under the twins thrall, Rowan decided that this time he would deviate from the usual procedure and oversee the attack personally."
    "Quickly bringing order to the orc detachment that arrived from castle Bloodmeen, Rowan split his forces into three groups, surrounding the village and closing the usual escape routes."
    "At dusk, he ordered a simultaneous attack from all sides."
    "As always, the village could only offer a token resistance. Caught by surprise, a few men tried to fight back – only to be struck down."
    "It all went according to plan – until Rowan heard sounds of an actual fight going on near the center of the village. Displeased by the prospect of unforeseen complications, Rowan hurried his horse forward."
    "There, he saw a man in an old, battered armor, aided by a handful of young men, engaging his orcs."
    "Despite being vastly outnumbered and clearly fighting a lost battle, the villagers seemed determined to protect their village to the end."
    "Normally, Rowan would applaud such a display of heroism, except this time it was working against him. Without a second thought, he galloped forward and readied his sword."
    "The old man saw him coming – and at the last second turned in his direction, raising his own sword to parry the incoming blow. Too slow – years of peasant life must have dulled his reflexes."
    "Rowan’s blade made its way past his guard and struck the man right in the neck."
    "A young boy shouted in horror. Rowan slowed down, and turned around to observe how the last stand of the village defenders fell apart."
    "Without the old man shouting orders and encouragements, the remaining peasants quickly lost their spirit. Some turned around to flee, others threw their weapons down and begged for their life."
    "Others yet decided to give their life with their hero."
    "And they would do precisely that."
    "Soon, the battle was over."

    #if player chose to capture village
    "Their defenders beaten down, the orcs lined the remaining villagers and started explaining them how they served Castle Bloodmeen now."

    #rejoin
    "Meanwhile Rowan inspected the now dead hero – the man who dared to oppose his forces, against all odds."
    "The wound was fatal – as Rowan intended it to be. The man bled out to death, red blood staining his clothes and armour."
    "His breastplate bore the insignia of Rosaria military."
    "Once, Rowan wore a similar armour."
    "Felt like it was an eternity ago."

    if avatar.guilt > 50:
        "Slowly, Rowan knelt besides the man. He said a silent prayer in his name, and closed his unseeing eyes."
        "… He lingered for a while, uncertain of his own feeling at the moment. But there was no use in regretting his actions now. Rowan stood up, and turned around without another word."

    else:
        "Rowan stared at the body for a short while, then turned around without a word."

    "This village was done with. It was time to move on."
    #capture or destroy the village based on player choice
    #lose 5 orcs
    $ castle.buildings['barracks'].troops -= 5
    return

else:
    "As always not so keen on seeing the result of his choices, Rowan ordered his orcs to attack without him. He would observe from a safe distance, only intervening if the situation called for it."
    "… The fighting went on a bit longer than usual and Rowan was slowly starting to worry something indeed went wrong."
    "He checked his equipment, still unwilling to participate in the attack – but as he lingered, he finally saw the one of his grunts exiting the village."
    "The orc signaled the village was pacified, and Rowan could safely take stock of the situation."
    "Apparently the village elder was some sort of war veteran, who managed to organize a makeshift defense force at the center of the village. He was dead now, but because of his interference they lost more soldiers than usual."
    "An unpleasant surprise, but these things happened. Rowan nodded to the orc and told him to proceed with the rest of the plan."
    "Another day, another village at the mercy of the Twins."
    #capture or destroy the village based on player choice
    #lose 5 orcs
    $ castle.buildings['barracks'].troops -= 10
    return

label old_hero_trade:
#branch 2 - trade
scene bg31 with fade
show rowan necklace neutral at midleft with dissolve
$ old_her_event = True
$ temp3 = human_villages_defs[eventHex[6]][2]
"The village elder was an energetic man in his forties, with a short beard, tanned skin and, as it happened, military background."
"Upon seeing Rowan, he squinted his eyes, as if uncertain if they’ve been deceiving him. Then, realization crossed his face - he straightened his back, and saluted the approaching hero."
"”General Blackwell”, the elder called him."
"When Karnas invaded the six realms, it was obvious they would need every living man, from peasant to noble, involved in the war. Not that many people were willing to join – but they didn’t exactly had a choice in that regard."
"The entire countryside was full of veterans. Rowan expected more of them to assume the position of village elders."
"At least those would not end up bandits, mercenaries, or broken men."
"War usually brought out the worst in people. He was glad to see someone who didn’t end up finding himself on that path."
"Rowan returned the salute, then extended his hand. The elder grabbed it with a smile."
"The village elder –  Gregory, as Rowan soon learned, invited the hero to his home, serving beer and bread to his guest. The two exchanged pleasantries and, much to Rowan’s dissatisfaction, the subject of his adventures after the war came up."
"Rowan delivered a handful of noncommittal answers, as always not so keen on sharing his current predicament."
"He tried to power through the conversation as quickly as possible, so he could raise the matter of a potential trade agreement – but the elder had something different planned."
"He revealed to Rowan, voice grave, that he knew of orc activity in the region. Mines were taken, villages were plundered, but the nobles weren’t doing anything about it. He feared, that if nothing was done, in time his own village might be in danger."
"Rowan’s arrival must have been a sign of Solania’s favor, for he was about to take a handful of strong, young lads, and scout the nearby territory for signs of the greenskin."
"The hero's tracking abilities were a thing of legend – with him leading the expedition, they could quickly find any nearby  orc encampments and put an end to this menace before it could threaten his hometown."
"To Rowan, that was obviously not an option, for he had no time to run around Rosaria chasing orcs that quite literally did his bidding."
"And he had a far better solution available to him."
"Having already decided the village would not be a target for an orc raiding party, Rowan explained to the elder he was already working on the problem. He had “allies” who were attempting to contain the orc threat."
"But they could not count on the noble’s backing – the aristocracy cared not for the countryside (a fact that allowed the twins to slowly take over the region in the first place), so they had to take care of the financing themselves."
"Which is what brought Rowan to the village in the first place – he explained he was attempting to secure more funding by signing trade agreement with numerous Rosaria settlements."
"The elder nodded slowly, a soft scowl on his face. For a man of action like himself, sitting around and letting others deal with the problem was clearly frustrating."
"But if Rowan believed this was the best course of action, he would follow suit without a word of complaint."
"He only needed to know what was expected of him."

if avatar.corruption > 74:
    menu:
        "Sign a normal trade agreement.":
            $ released_fix_rollback()
            "Rowan presented him with the usual deal, one that was generally considered acceptable to both sides. And as he expected, the elder agreed to it quickly, stating the terms were indeed reasonable."
            "Satisfied with the result, Rowan warned him not to go Orc hunting on his own. Regardless of what happens in Rosaria, he and the villagers should just sit tight, while Rowan and his “allies” deal with the problem."
            "The elder proposed Rowan should stay the night, as it was getting late, and the prospect of getting a good night of sleep on a proper bed was simply too good to pass."
            #gain 2 move points due to good rest
            $ avatar.mp += 2
            #gain standard village trade income
            return

        "Use your reputation to sign a more lucrative agreement.":
            $ released_fix_rollback()
            "Rowan presented him with a slightly harsher deal than usual, unbeknownst to the elder."
            "The man listened to the terms carefully, and 15 minutes later, after a long consideration, agreed to them without any even attempting to bargain."
            "He said that if Rowan needed the money so badly, the village would provide it. Everything for the hero of Karst."
            "Feeling a bit guilty for using his reputation like that, but nevertheless grateful the elder didn’t pry on the circumstances, the two signed the deal."
            "Rowan warned the elder once more not to go hunting the orcs on his own, and to sit tight no matter what happens in Rosaria. He and his “allies” would deal with the issue."
            "The elder proposed Rowan should stay the night, as it was getting late, but knowing he was already exploiting the elder for his own gain, Rowan decided to pass on the offer and resumed his travels immediately."
            #gain 1.5 times the usual village trade income
            $ castle.villages_income += int(temp3 * ( (dice(25) + 25)/50.0 ))
            return

        #only available if rowan's corruption is greater than 74
        "Make him give the twins almost everything.":
            $ released_fix_rollback()
            "Voice heavy, Rowan explained to the man he and his allies had very limited resources available to them. They really couldn’t afford to spread themselves over the entire region."
            "Only places deemed “strategically important” ended up protected."
            "Rowan could see how the realization dawned on the man. Slowly, the elder asked what would it take for his village to be considered “strategically important”."
            "Quietly, Rowan listed the amount of goods they would have to contribute in order to ensure  his “allies” deal with the orc problem."
            "It was far beyond what he usually demanded during trade agreements. Even though Castle Bloodmeen would provide some token payment for the goods, at this point the village would be better off simply being conquered."
            "The elder didn’t answer at first. He sat there, motionless, fists clenched."
            "Finally, he swallowed heavily and answered that, if that’s what was necessary to protect the village from the orcs, he would agree to it."
            "Trying not to think how just basically forced a village into poverty to fuel the Twins war machine, Rowan explained the details of their arrangement."
            "He reminded the elder not to go hunting orcs on his own, and to sit tight no matter what happens in Rosaria. He and his “allies” would take care of everything –"
            "- as long as he sticks to his side of the deal."
            #gain 2 times the usual village trade income
            $ change_base_stat('g', 3)
            $ change_base_stat('c', 3)
            $ castle.villages_income += int(temp3 * ( (dice(25) + 25)))
            return
else:
    menu:
        "Sign a normal trade agreement.":
            $ released_fix_rollback()
            "Rowan presented him with the usual deal, one that was generally considered acceptable to both sides. And as he expected, the elder agreed to it quickly, stating the terms were indeed reasonable."
            "Satisfied with the result, Rowan warned him not to go Orc hunting on his own. Regardless of what happens in Rosaria, he and the villagers should just sit tight, while Rowan and his “allies” deal with the problem."
            "The elder proposed Rowan should stay the night, as it was getting late, and the prospect of getting a good night of sleep on a proper bed was simply too good to pass."
            #gain 2 move points due to good rest
            $ avatar.mp += 2
            #gain standard village trade income
            return

        "Use your reputation to sign a more lucrative agreement.":
            $ released_fix_rollback()
            "Rowan presented him with a slightly harsher deal than usual, unbeknownst to the elder."
            "The man listened to the terms carefully, and 15 minutes later, after a long consideration, agreed to them without any even attempting to bargain."
            "He said that if Rowan needed the money so badly, the village would provide it. Everything for the hero of Karst."
            "Feeling a bit guilty for using his reputation like that, but nevertheless grateful the elder didn’t pry on the circumstances, the two signed the deal."
            "Rowan warned the elder once more not to go hunting the orcs on his own, and to sit tight no matter what happens in Rosaria. He and his “allies” would deal with the issue."
            "The elder proposed Rowan should stay the night, as it was getting late, but knowing he was already exploiting the elder for his own gain, Rowan decided to pass on the offer and resumed his travels immediately."
            #gain 1.5 times the usual village trade income
            $ castle.villages_income += int(temp3 * ( (dice(25) + 25)/50.0 ))
            return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#A cheating Elder:
#No requirement.

label a_cheating_elder:
scene bg1 with fade

"Rowan walked through the village, taking stock of their defenses. This particular village wasn’t too well defended. It would be an target for his orcs – if he choose to send them in."

#Give normal village menu. Then, split:

#branch one - capture or destroy:
"Rowan expected the attack to go well, but not this well."
"After his forces arrived at the village, the elder instantly surrendered, without as much as a stone cast at his soldiers. His orcs quickly scattered across the village, rounding up villagers, while the elder was brought before him."
"He was a scrawny old fellow, terrified out of his wits, as Rowan quickly after looking at his pats. He prostrated himself before him and with shaking voice asked Rowan to spare the village and himself."

#if player chose to destroy the village
"From beneath his hood, Rowan nodded slowly. He quietly informed the man who his new masters were, and what was expected of them."
"To drive the point home, he ordered all the gathered villagers to kneel along the elder."
"If anyone hesitated, one his orcs would strike them in the back, forcing them down. It was a crude method, but he needed to make sure the villagers wouldn’t be causing any troubles in the future."
"He took another look at the village elder, who was still shaking in  fear. With this man at the helm… He doubted they would."
#village is destroyed as normal
return

#if player chose to capture the village
"Rowan looked down on the man with pity. If only he knew..."
"He turned to the orc besides him and spoke."
show rowan necklace neutral behind bg1
ro "You know your orders."
"The elder looked up confused – only to be knocked out by a blow straight between the eyes."
"Some of the gathered villagers tried to resist, but the orcs subjugated them quickly. Nobody had any weapons to really be a threat, so his soldiers managed to do so without killing anyone."
"Once the people were tied up and ready for transportation, his orcs would then scatter across the village, pillaging food, gold, and valuable tools."
"It was nice to see things go so well for a change."
#village is captured as normal
#gain ten slaves
return

#branch two - trade
"Rowan headed to the center of the village, to meet the elder. He found him quickly – he was a scrawny old fellow, polite and pleasant, who reacted to Rowan’s proposal with great enthusiasm."
"As usual, after a long series of negotiations, Rowan managed to strike a deal that more or less satisfied both sides."
"However, this time things did not go as smoothly as he expected."
"A few days after departing from the village, Rowan received a message from the castle. Apparently, the goods provided by the elder were not what they’d been expecting. The quality was simply below below the usual standard."
"However, the elder still expected to be paid the agreed amount, and wouldn’t listen to his emissaries at all. Castle Bloodmeen was to either pay and take the goods or the deal was off."
"As the trade still benefited the Twins, their representatives reluctantly agreed, much to the elder’s satisfaction. But they were now asking how to proceed from here on. If the matter was left as it stood, the village would provide only half of the usual income."
"Rowan did not have the time to chase after every elder who tried to scam him, as tempting as it was."
"He had to rely on what resources he had to deal with the issue."

menu:
    "Leave the village alone – accept the subpar goods.":
        $ released_fix_rollback()
        "Gritting his teeth, Rowan told the castle staff to leave the village alone. He couldn’t punish the whole village for the actions of one dishonest elder."
        "They would have to accept the deal as it was."
        $ change_base_stat('c', -3)
        #village provides half the usual gold from trade
        return

    "Send the orcs to conquer the village.":
        $ released_fix_rollback()
        "Trading with Rosaria villages was already less profitable than simply conquering them. If Rowan wanted to remain in the Twin’s favor, he couldn’t afford being deceived like that."
        "He told the staff to send an orc detachment to deal the elder, and bring the village under the twin’s control. He knew it was as little defended as most villages were, so he foresaw light casualties at best."
        #lose 3 orcs
        #apply the usual reward from destroying the village
        return

    "Send the orcs to occupy the village.":
        $ released_fix_rollback()
        "Rowan gritted his teeth. Trading with Rosaria villages was already considerably less profitable than some of the other options he had at his disposal. He was protecting them from the twins, and this was how they repaid the favor?!"
        show rowan necklace neutral behind bg1
        ro "…"
        ro "Send the orcs in. The village is scarcely defended, so you don’t need a big group."
        ro "Enslave everyone, take anything of value, then burn down what remains."
        ro "And have this done by the end of the week."
        "That, and no less, was the price the elder and his people would pay for their dishonesty."
        #lose 3 orcs
        #apply the usual reward from capturing the village
        return

    #only available if the brothel is built, and the player has at least one unassigned spy
    "Send a demonic spy to convinces the elder to change his mind.":
       $ released_fix_rollback()
       "Rowan groaned in annoyance. To think he would have to deal with mundane problems like this one…"
       "Luckily for him, he had just the right tool for the job. "
       #give player a choice of available spies, chosen spy becomes unavailable for two weeks
       "He ordered the staff to have one of his agents visit the village and show the elder the error of his ways. It should take a while… But he doubted the demon would have any difficulties with the task."
       #gain standard village trading income
       return
       
       
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

label the_dragons_path:

scene bg5 with fade

"By the time Rowan arrived, pillars of smoke were already rising over the hills. The maps had said there would be a village here. Perhaps if he had arrived sooner there might have been."
"The town was a mix of burned out houses, destroyed roads, and ash. Ash everywhere. He walked through the husks of the buildings, but never found another living soul. If anyone had survived this, they wouldn’t have stayed around."
"At first he had assumed it was a band of orcish raiders. But, then he started finding valuables in the houses. Swords, valuable silks, fine ivory. No one had looted this place. It hadn’t been orcs."
"What had happened here?"
"It was better not to think much on the matter. The people were already dead. There was nothing he could for for them. He sent men in to free the ruined homes of their valuables. But, he also assigned to grumbling orcs to bring the charred bodies together for proper burial."
"It would be some weeks before the mystery of the village would be resolved. Rumor swirled that a dragon from the southern mountains had ventured up into the Rosarian valley on an excursion. "

if avatar.corruption < 31:
    "When he learned that, Rowan said a small prayer. Perhaps it would not run into any other villages. Perhaps."
    
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label village_spoils:

scene bg5 with fade
show rowan necklace neutral at midleft with dissolve

"Destruction surrounded Rowan. It wasn’t surprising. What could the small settlement do against the butchery of a legion of orcs?"
"Once all resistance had faded, the former hero found himself strolling through the village proper. On either side of Rowan, houses burned while others looked like little more than charred husks."
"The Orcs always enjoyed a good sacking. His soldiers were busy looting what remained from the rubble, laughing with cruel malice as they stepped over the broken and defeated corpses of the few who’d tried to resist."

if avatar.corruption < 31:
    "Rowan felt disgusted and appalled by the butchery. While on the outside, he looked resolved and indifferent, beneath his skin he felt a swirling and bitter rage. Even though he had played his role, Rowan knew that he was simply a blade that the Twins had plunged through the heart of the village."
    
elif avatar.corruption > 60:
    "It was their way. And in some respects, Rowan couldn’t fault them for it. They had fought and bled to take the village, and now they enjoyed their spoils, as easily taken as they were."

else:
    "It was easily one of the smoothest conquests he’d yet played a role in. A grin formed on his face as he enjoyed the inspiring sense of power broiling through him after bringing the village under  the twins’ domain. Sure they had suffered, but in time, Rowan knew that those that survived would enjoy the new world he was helping to build."

"His ears alighted to the sound of jeering barking, coming from one group of orcs in front of him. He watched from afar as they rounded up the survivors to bring back as slaves."
"The villagers were all in chains, bound and ready to be either enjoyed or dispatched to their new work. It was a typical raiding party, nothing out of the ordinary."
"But then the warrior stopped, his eyes settling upon a peculiarly entrancing sight. There was a young woman amongst the haggard prisoners. Even covered in soot and grime as she was, the maiden stood out. Perhaps it was her beauty, or merely the defiant look in her eye." 

show orc soldier neutral at midright with dissolve
show wild orc neutral at edgeright with dissolve

os "Alright boys. Get’em moving!"

ro "Stop!"

"The leader of the Orc squad turned his head and bared his tusks slightly at Rowan."

os "Wot?"

"Rowan raised a hand and pointed out the rare jewel that had caught his eye. She looked up at him with tired, resigned eyes. Though a spark remained, it had faded to a pale indifference."

ro "Pull that one from the line."

os "Aww… Boss man, no! Dat’s da best one!"

ro "I’m not here to listen to your whining."

"The two orcs looked back and forth from their treasure to Rowan. Then the main one barked out new orders in his low, guttural tone." 
"The chains around the woman’s feet that attached her to the line were removed. With a grunt of annoyance, the thick-shouldered greenskin shoved her towards the warrior."

wo "Dis is no fair."

"Rowan grabbed the girl by the arm, leading her slowly but surely away from the rest of the prisoners."

os "Was got inta you Boss? Youse is usually a great big stick in da mud!"

hide orc solider with dissolve
hide wild orc with dissolve

"Rowan gave them no reply.  He left the gang of pillagers with his new acquisition glumly in tow. He was certain they’d find their amusements with the other slaves they had nabbed from the ruined village."

"Rowan’s grip remained like a steel trap around the girl’s arm as he escorted her back to his command tent. He spared a glance in her direction, it was hard not to enjoy her beauty, given the wide and shocked pools of her eyes."

gret "Please, let me go."

if avatar.corruption < 31:
    "As he looked at her, the shock seemed to wear off, turning into a stubborn expression. She didn’t lack for spirit, and he hoped that the spark would serve her well as the world rapidly changed for her."
    
elif avatar.corruption > 60:
    "A spark of courage remained in her. It amused Rowan, until she started trying to drag her heels into the bloody and muddy ground around them."

else:
    "While Rowan looked at her, he found himself forgetting about the smoking huts and the metallic stench of blood. Something about her comeliness called out to him, demanding his attention and he quickly had to look away to make sure he didn’t drip over a discarded sword left on the battlefield."

"He turned on the heel of his boot and squared her shoulders with both hands so that she faced him directly."

menu:
    '"Shhh. Quit struggling. I’m trying to help."':
        $ released_fix_rollback()
        "The girl pulled her hand back but he kept his grip firm and tight around her skin."
        "She looked at him, uncertain that she’d even heard his words correctly. Rowan fixed her with a strong look, indicating with his eyes." 
        "Wary, she nodded at him. She didn’t bog them down any further for the rest of the trip. After all, what choice did she have?"

    '"This reckless behavior will only make it worse for you."':
        $ released_fix_rollback()
        if avatar.corruption < 31:
            "He eyed a pair of orcs paying attention to him and his prisoner. Steeling his resolve, he shook her shoulders again to ensure he had her attention."
            ro "I said be {i}quiet{/i}!"
            "She was clearly unprepared for the edge in his voice. Rowan prayed that she’d manage to keep her lips shut as they continued to the tent. He had to maintain the facade of an overlord dragging his concubine to his tent for some after-battle entertainment."
        else:
            "Rowan’s words smacked some sense into her. She looked at him and then at the pair of orcs around, before finally giving him a nod. As they continued walking, Rowan no longer had to drag the girl he had liberated from his warriors."

scene bg30 with fade
show rowan necklace neutral at midleft with dissolve

"Upon returning to his tent, Rowan released his grip on the girl. She fell down to her knees, as the former hero began to brusquely pace back and forth about the tent."

gret "Y-you… you have my thanks, m’lord…"

"The poor woman’s body straightened up. Her shoulders trembled as she glanced back to the tent’s entrance. She was clearly worried the orcs might return while she wasn’t looking."

ro "What is your name? "

$ gretchaName = "Gretcha"

gret "G-Gretcha… and w-who are you?"

"The warrior didn’t answer the question. His eyes dropped from her features after a moment, still abuzz from the rush of battle. As he slowly calmed down, Rowan took a moment to sniff at his armor. His armor had been caked in a layer of grime and viscera. He felt soiled. He needed a bath."

gret "M’lord… why… why did you save me?"

"Rowan glanced at her for a moment and then shifted his eyes away."

menu:
    '"Because I could."':
        $ released_fix_rollback()
        if avatar.corruption < 31:
            "Rowan turned back to face the trembling girl."
            ro "Do I need a reason to spare someone’s life?"
            "She looked at him with blank confusion. Her eyes filled with emotion as they boiled up into rage."
            gret "So why didn’t you save the others? My {i}whole village{/i} was-"
            "Rowan felt his chest constrict. He let out a heavy sigh, unable to look her directly in the eyes."
            ro "Because I can’t save everyone, the Orcs would not allow it. I had to choose, and I chose you."
            ro "At least they died with sword in hand."
            gret "You… you’re just like them..."
            "Gretcha glared at him, obviously not eager to believe his words or trust what he had to say to her."
            gret "So… what happens now?"
        elif avatar.corruption > 60:
            "Rowan fixed the pretty lass with a warm smile."
            ro "You know, I haven’t quite decided yet. But I’m sure we’ll have a lovely evening together."
            "Her eyes were uncertain, her lips flattening down to a fine line. She let out an exhausted sigh."
            gret "Hmmmph. So, if the orcs were going to take me like common wolves, what do you intend to do to me?"
        else:
            ro "I didn’t come here to salt the earth."
            "Rowan’s voice came out as a low growl. He did his best not to look her in the eye."
            ro "I spared you. Isn’t that enough?"
            "The woman looked away from him; her silence was an implicit condemnation. The only thing that could be heard throughout the tent was her soft, laboured breathing."
            gret "But… not the others."
            "Hatred, frustration and pain spilled out of her voice in equal measure. Her fingers knotted into fists."
            gret "Where is your mercy for {i}them{/i}?"
            ro "Count yourself fortunate there was any at all."
            "The girl glared at him. For a time, the only sound was the scribbling of Rowan’s quill and the grunts and whooping of the orcs outside the tent. Finally, the peasant girl spoke up."
            gret "So… I’m to be {i}your{/i} plaything tonight instead, is that it?" 
            
    '"You suffered enough."':
        $ released_fix_rollback() 
        if avatar.corruption < 31:
            ro "I could not stand by and leave you to the Orcs."
            ro "You’ve suffered enough."
            "She looked at him incredulously, half-expecting a seastorm to rise up and sweep through her already ravaged village. Finally, she found the courage to speak."
            gret "T-Thank you, my lord. But… I don’t understand. What do you want from me?"
        elif avatar.corruption > 60:
            ro "It’s simple."
            "The warrior stroked the villager’s chin and then ran a hand down her back. She shivered at the touch, goosebumps rolling down her spine at the sensitivity."
            ro "If I left you to the orcs, they would have done terrible things to you. I don't want that for you... "
            ro "And I don't think you want that, either."
            "The beautiful woman blinked, her eyes slowly shutting as Rowan ran a finger across the upper breadth of her lips."
            gret "As you say… but {i}my lord{/i}…"
            "The two last words were spoken with equal parts frustration, concern, and curiosity."
            gret "What is it you want of me?"
        else:
            ro "Would you rather I toss you back out there with the orcs?"
            "He blazed with rage at the question and its impudence. This girl knew {i}nothing{/i} of true suffering. She didn’t understand what he was doing for her."
            gret "I... No… please."
            "She sniffled and whimpered, shrinking down into herself. His harsh tone had put her in her proper place."
            gret "Anything but that…"
            ro "Then keep your questions to yourself."
            gret "But… I don’t understand. What do you want from me?"
    
    '"I don’t know."':
        $ released_fix_rollback() 
        if avatar.corruption < 31:
            ro "I… I don’t know why I did it."
            "Rowan sat down and slumped into his chair, depressed and full of malice without direction."
            ro "I just saw you, and I..."
            "His eyes fell on the girl, and he gave her a sad, faltering smile."
            ro "I couldn’t let them take you."
            gret "You… you could have helped the others."
            "Rowan’s brow lowered, his low mood only worsening."
            ro "Maybe. But I didn’t."
            "The village girl said nothing. She looked at him, eyes wide and frightened."
            gret "...You helped me instead."
            ro "Yes."
            gret "Why me? What do you want from me?"
        elif avatar.corruption > 60:
            ro "I don’t know. A whim, I guess?"
            ro "You’re beautiful, that much is plain."
            "Gretcha blushed and turned away, her hands reaching up to cover up her breasts."
            ro "Maybe I just wanted to see you a little longer."
            "Rowan stroked his chin while mulling over his thoughts on the matter."
            ro "Perhaps you remind me of someone? I’m not sure, the heart can be a foolish creature sometimes."
            gret "I-I… I think I know what you want."
        else:
            ro "It was a mistake, a foolish decision. I should just send you back."
            gret "{i}Please{/i}, my Lord. Let me stay with you!"
            "The woman cried out while tears welled within her oaken eyes. She knew as well as he did that a return to the orcs was a worse fate, regardless of his intent."
            gret "It’s not like… there is anything for me to go back to. Whatever you want from me, just ask. I have nothing left…"

    '"I want you tonight."':
        $ released_fix_rollback() 
        label gretOrcProtect:
        if avatar.corruption < 61:
            "The poor girl stiffened at her captor’s quiet smile."
            ro "Why are you afraid? I saved you from those Orcs, didn’t I?"
            "Rowan crouched in front of her, gently cupping her trembling chin."
            ro "I’m not going to hurt you."
            gret "P-Please. Don’t send me away."
            "A faint edge formed at the corner of Rowan’s smile."
            ro "I wouldn’t dream of it."
        else:
            ro "You are a rare beauty, Gretcha. But I did not bring you here to be my slave."
            "Rowan turned to look at the quiet peasant girl."
            ro "Stay with me this evening, enjoy a quiet bath, and tomorrow I will ensure you go free and safe."
            "Gretcha looked at him, her eyes two stormy pools of darkened oak."
            gret "And why should I trust you?"
            ro "My masters already have enough prisoners as is. One missing peasant girl won’t be a significant loss to them."
            ro "Really, what have you got to lose?"
            "Gretcha looked around the tent for a long moment, and then let out a sigh. She nodded towards her captor."
            gret "As you wish…" 
        jump GretchaBath
            
menu:
    "Offer her a path to freedom.":
        $ released_fix_rollback() 
        if avatar.corruption < 31:
            ro "For now,  just rest. You’ll be safe here for tonight."
            "Rowan resisted the urge to laugh. The idea of anyone being {i}truly{/i} safe, with the Twin’s armies marching through Rosaria was ludicrous. But she didn’t need to hear that."
            ro "Tomorrow, I will make certain your escape seems like an ‘accident.’"
            "He gave her a sad smile, one she did not return. Her eyes watched him warily, her expression guarded."
            "She must hate him; she wasn’t wrong to do so. If their roles were reversed, Rowan would have been hard-pressed to trust her word himself."
            ro "Please, take some time. Have something to eat. You’ll need your strength."
            "The young woman, seeming to finally realize he was serious, and that she really was safe, struggled to fight back tears. She looked away, responding only with a faint nod. "
        elif avatar.corruption > 60:    
            ro "I don’t want anything from you, I want you to get out of here. Come tomorrow, you will ‘escape’ this camp. With any luck, you will never see me again."
            gret "Why… why would you do that?"
            "Rowan’s brow furrowed, and he turned from his desk and glared at the girl."
            ro "Why do you care? I’m offering you a chance that no one else in your village has gotten. If you’d prefer, I can send you back to the orcs."
            "Gretcha quickly shook her head back and forth. To the peasant girl’s credit, she did not wilt when he returned her curious gaze with a withering glare."
            gret "Y-You really mean to free me?"
            ro "Those were my words, correct?"
            "Rowan proceeded to ignore her for the next few hours. Not a word was shared between them as he focused on his work, looking over the new dispatches and reports of the day."
            "Gretcha watched him for a long while before finally sitting down. Her dark-brown eyes slowly sliding shut as the exhaustion of the day overcame her." 
            "She fell asleep on the ground, curling up to stay warm in the chill air. Rowan worked through the night, his gaze only briefly wavering in her direction every so often."
        else:
            ro "Best you keep quiet."
            "Rowan swept by her to make sure the flaps of his tent were closed. He peered beyond the stiff leather, his eyes hardening as he saw a train of captives being led off not far from the entrance."
            ro "Orcs are dull, but their ears still work. Sometimes better than our own."
            "The girl let out a small yelp and nodded, holding her hands close to her body. Rowan almost moved to comfort her, but decided against it. He kept his back to her."
            ro "Get some rest, if you can. Tomorrow, I will help you escape."
            gret "Truly?"
            ro "Yes."
            "That settled things. The strange, twinging feeling in Rowan’s gut seemed to retreat." 
            "Rowan turned from the tent entrance and moved to small work bench in the corner. Without a word, he began to look over the new dispatches and reports of the day."
            gret "I… I still don’t understand. Why are you helping me?"
            "Rowan paused. He set down the report, affixing her with a short, sharp look."
            ro "Does it matter?"
            "He returned to his work. She sat for some time in the center of his tent, huddled into herself." 
            "Eventually, the peasant girl fell asleep on the ground. Rowan, as if it were an afterthought, draped a spare blanket over her shivering body before retiring to his cot."
        return
                
    "Offer the girl protection from the orcs if she spends the evening.":
        $ released_fix_rollback() 
        jump gretOrcProtect   
           
label GretchaBath:

scene black with fade
show rowan necklace naked behind black

"Time passed. That evening, Rowan had Gretcha draw them both a bath. The warrior was eager to cleanse himself of the soot and grime leftover from a hard days struggle."
"Gretcha played her part as a servant girl well, first filling the tub with warm water and then lathering her captor’s body with a brush and soapy hands."

gret "I didn’t think I’d meet someone who traveled with their own tub. Much less bathing some strange man in one…"

"As she spoke, her nipples occasionally brushed against his shoulders and back. It was a pleasing, ticklish sensation."

ro "These are strange times."

gret "Terrible ones, if you ask me."

"She was a pleasant enough distraction: shy, demure, with a spark of resistance in her. Rowan settled down happily into the tub as she worked the kinks out of his shoulders."

#cg #1
scene black with fade
show rowan necklace naked behind black

if avatar.corruption < 61:
    "Gretcha seemed to be slowly coming around as well. She squished her chest against his back as her fingers ran down his chest, her breathing deepening to a low, sensual coo."
    "Naturally, under the pleasant touch of a beautiful woman like her, his budding arousal soon revealed itself."
    ro "Excuse me."
    "The warrior spoke with faux-modesty as he reached down to shield his wet cock from her. Gretcha’s hand moved over his, pausing his progress."
    gret "You asked for a bath, my lord. That means I need to wash all of you."
    "Her eager tone surprised Rowan. Before he could say anything, a groan slipped from his lips as Gretcha’s slender hand peeled his fingers away."
    "Without another word, she changed positions, pulling herself up out of the back and moving around to the lip of the bath. She kneeled in front of him, covered in suds."
    "Then the peasant girl took hold of his warm, wet length, leaned forward, and engulfed it with her mouth."
    
else:
    "Relaxing in the bath, Rowan felt flickers of warmth rising in his body as Gretcha ran her hands across his body, sliding slowly downward, ever lower."
    "He felt her cute tiny nipples harden against his back, which in turn sent a spell down to his groin."  
    "Soon, the tip of his cock breached the surface, sticking conspicuously out above the water."
    gret "I guess I should attend that as well?"
    ro "I didn’t say anything."
    "The girl let out a wry chuckle."
    gret "Your eyes say it all, my lord…"
    "Without another word, she changed positions, pulling herself up out of the back and moving around to the lip of the bath. She kneeled in front of him, covered in suds."
    "As Gretcha bent her body forward, Rowan watched as she closed her eyes and began licking the tip of his spear."  
    "Her tongue fluttered and licked along the edge of his cock, stoking the fire of Rowan’s lust."
    "It became immediately clear to the warrior that it was not the first time Gretcha had done something like this."
    
gret "Mrmmm…"

"Gretcha moaned out as her head bobbed up and down on the warrior’s cock, moving with urgency and focus."
"While her lips hugged his cock, the girl’s fingers trailed lower, fondling his balls with her palm."
"Partially submerged as they were, her fingers created little splashing noises as she massaged him. The warm water blanketed Rowan’s balls in intoxicating pleasure."

gret "Ahhuhah… It’s getting… bigger…"

"Rowan’s hand reached out, grasped her by the back of the head, and pushed down. The warrior buried his captive’s mouth back down upon his throbbing shaft."
"He led her in an intense throat fucking, pulling her head up and down on his shaft in a relentless tempo. After a moment, Gretcha’s lips tightened; her movements felt more eager and intense than before."
"The slut was {i}enjoying{/i} herself!"

gret "Ahuhaah… Mrrmm… Glllrp… glrrrpp… glruph!"

#cg #1 - var 1
scene black with fade
show rowan necklace naked behind black

"The slurping wet noises of her whorish lips only bolstered the evening treat. Rowan’s balls began to churn as the hot water and the continuous touch of his servant girl’s hands and lips combined to bring him to orgasm."
"With one more hardy grunt, Rowan’s back hunched forward in the bath as fire flourished through his body. It lanced up, firing free from his cock, charting a path directly into Gretcha’s quivering throat."
"He held her there for several seconds. Finally, Gretcha managed to pull back once Rowan released his grip. Ribbons of his nectar and her spittle fired off across her face, hair and breasts."
"They coated the villager’s luscious lips, giving her a pearlescent sheen of cum. Even as the last drops were still spurting out, he did her best to scoop them up like a good girl."
"She coughed a few times as she struggled to gulp down the last remnant of Rowan’s seed. Rowan leaned back, spent but pleased. Gretcha stared expectantly at him, kneeling in front of the bath."

ro "Go… Fetch yourself some water."

"She nodded standing up and idly wiping at the cum on her breasts, as Rowan finished washing himself up."
"Later he and Gretcha shared a quaint meal together. Thereafter, the warrior offered the girl his bed, a kindness she warily indulged in."
"She didn’t end up trying anything more, but she did settle into his arms and attempted to sleep. It had been, after all, a strenuous day for her."

if avatar.corruption < 61:
    "Looking at the beautiful girl who had been his evenings entertainment, Rowan wondered for a moment if it would be better to keep her."
    ro "The odds are high that she’ll be plucked up by a patrol before walking two miles from the camp."
    "Still, he shook his head and returned his thoughts to more important matters. It wasn’t about whether or not she would actually escape into that wide world beyond."
    "He had kept his promise to her, and that was enough."

else:
    "Watching the alluring woman squirm and twist in his arms gave rise to frustration inside of Rowan. He couldn’t help himself and felt his cock stirring anew, even after he’d quenched his lust with Gretcha’s throat."
    "For a moment, he nearly indulged in the urge  to spread her legs apart, but some part of him locked up. Eventually, he settled back down into his chair"
    ro "She’s not worth it."
    "It was true. As pleasant as the distraction had been, that was all she was: a distraction. He’d promised her freedom, and she had returned with affection."
    "His lust sated, his conscience cleared, he turned his thoughts back to more important matters." 
    "After all, what was one peasant girl’s life to another? There were countless other innocents suffering on all sides. If anything, he had {i}spared{/i} her of the worst of it."

scene bg5 with fade
show rowan necklace angry at midleft with dissolve

"Come the morning, Rowan marched out from his tent. With the sun rising above the ruined village, the warrior found the same group of orcs from the day before. The lazy brutes were asleep at their posts."
"He delivered a swift kick to the chest of their leader."

show orc soldier neutral at midright with dissolve

ro "She’s gone."

os "Ah, can’t  we sleep a bit more, Boss? All dis raiding… got me hankered."

"Rowan delivered a sharp kick to the Orc’s groin, sending him rolling on the floor, howling in pain. The rest of the party leapt to their feet."

ro "I said {i}she’s gone{/i}."

os "Who? Who’s she?"

"Rowan glared at them, playing the part of the stern overseer scolding his incompetent servants."

ro "Who do you think, you lazy fiends? The girl! She’s escaped!"

os "Da’ milkmaid? The one wit them huge tits?"

ro "I should gut you where you lie. What good are a bunch of slumbering half-wits if you can’t even guard my tent?"

os "Buh… sorry Boss. Wez jus resting our eyes."

ro "Not any longer, you’re not. Her tracks lead north. Find her, and bring her to me at once."

"The Orcs looked back and forth at one another, their eyes full of fear. The one Orc was still hunched on the ground, cupping his groin as he whimpered in pain."

os "Y-yes, Boss."
os "You ‘eard him, boys. Gather up your blades and clubs, we’s goin huntin’!"

"The other orcs shook off the sluggishness of sleep and began barking and whooping excitedly while they went for their weapons."
"Their leader smacked Rowan on his shoulder."

os "Don’t worry, we’ll catch da pretty Humi for you, boss."

"Rowan said nothing, returning the Orc’s smile with a cold glare. The Orc shrank back, gesturing meekly towards the ground."

os "Ah, don’t worry, we won’t do nuffin to her… come on, boys!"

"Rowan suppressed a smile as the troop headed off on their grand, fruitless hunt. The hero had naturally told the young girl to head due south, and the empty headed Orcs were so stirred up by his sudden hostility that they didn’t even look properly for the tracks. "
"Now, with the warriors searching in the wrong direction, he had followed through on his end of the deal. The rest was up to her; he just hoped she wouldn’t run into other raiding parties."

return


