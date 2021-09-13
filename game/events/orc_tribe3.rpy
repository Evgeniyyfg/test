init python:

    event('good_defence_is_only_offence', triggers='map_res_13', group='map_res_orc_tribe', run_count=1, priority=pr_map_res)
    event('chieftess_seeks_pretty_boy', triggers='map_res_13', group='map_res_orc_tribe', run_count=1, priority=pr_map_res)
    event('introductions_count_for_something', triggers='map_res_13', group='map_res_orc_tribe', run_count=1, priority=pr_map_res)
    
label good_defence_is_only_offence:

scene bg26 with fade

"Rowan found himself studying the tribe while Andras was occupied with convincing the orcs to join his soldier ranks."
"The place was little more than a camp of skin tents, haphazardly laid out with no apparent plan or regard for utility or defense.  Rowan suspected they'd just pitched them wherever they felt like it."
"The tactician in him couldn't help but criticize how open it left them to attacks.  Though orcs were not exactly a defensively minded race.  He couldn't remember a single time they'd actually tried to hold a defensive position against a siege or prolonged assault."
"There were numerous times when he, his men, or the heroes had come upon a camp not too dissimilar to this one where the orcs had come charging out to meet them head on in combat.  That or they'd fled in all directions, abandoning everything except their weapons and children."
"It had been said that a good defence is a good offense, but left to their own devices orcs forgoed defense entirely."
$ change_recruitment_bonus('barracks', 1)
return

#############################################################################################################
#############################################################################################################
#############################################################################################################

label chieftess_seeks_pretty_boy:

scene bg3 with fade

"There should have been orcs in the area. Frequent large footfalls through this particular stretch of otherwise very dense woods had choked out the plants and left a good path to follow."
"Rowan had been tracking the tribe for several hours now. Well, tracking was hardly necessary at this point. It had started with him finding their hunting grounds and following the trails they'd left since."
"Up ahead, he spotted a group of them. That confirmed what he'd hoped, though left him in an awkward position. There wasn't anywhere to hide on this trail and the forest brush on either side wasn't something he'd be able to make much headway in."
"There was a shout from the approaching group, so Rowan decided it was time to hurry in the only direction open to him. He was a human, prey as far as orcs were concerned until his demon Master arrived to give him safe passage through the tribe."
"A quick word through the amulet was all that was needed to indicate he'd found some orcs to recruit. Now he just needed to get somewhere where he could wait for Andras to make his way here from the nearest portal."
"Ten minutes later, he was cursing his luck. He'd gone around a turn and run straight into another group of orcs heading in the opposite direction."

show wild orc neutral behind bg3
#show femorc

wo "Wat dis? Some silly humie out here on his own?"

"The speaker had a large deer slung over his shoulder and a bloody spear in his other hand. A moment after he spoke, the others fanned out and blocked any chance of running past them. Rowan put his hand on his pummel, sizing them up. Four plus the hunter with his deer."

femorc "Humie! Humie!"

"The other group came around the corner, pinning Rowan in. Now there were over a dozen of them, and he was surrounded."

femorc "Heh, caught you!"

"The green woman swaggered confidently up to Rowan, nodding at the other hunter."

femorc "Gettin extra meat I see."

"Rowan sighed and took his hand off the pommel of his sword. Instead, he undid the scabbard from his belt and let it tumble to the ground."

wo "Dat was fast."

femorc "Humie smart. Knows when he beaten."

"She snatched up his sword then took a close look at Rowan."

femorc "Well, you real pretty one. Silly boy, shouldn't walk all alone in woods, might find strong orcs. Hungry orcs."

"She laughed, then shoved Rowan towards the other group. One of the other hunters grabbed his hands, then tied them up behind his back."

wo "Chief will like him, pretty boys like dis get da blood running."

femorc "Maybe. If not, I get him when hunt over and you can have dis sword."

wo "Done."

"The two groups passed by one another, and Rowan was lead further down the path. At first the group made crude remarks about his appearance and insults to Rowan's abilities and intelligence, though they soon grew bored of it when he didn't react to their antics."

scene bg26 with fade

"Upon returning to the tribe, the group broke up: the lead hunter went off to butcher his kill and most of the others went off to their respective tents. The remaining orc paraded Rowan around the camp to a few scattered cheers."
"The man bore it in stoic silence. He was not so helpless as they might believe."
"Soon the chief came to inspect the capture that had been said to be of interest to them. She towered over Rowan, wrapped in silk scraps and a vest of antlers lashed together. Pale white eyes glowered down at him from a sharp face with one broken fang."

orcc "Hmm, he is pretty humie boy. Got some nerve to him too, no tears or begging. Wonder how long dat will last?"
orcc "No one fucked him, right?"

"Her gaze had a look of great danger to it and there was a certain degree of apprehension when the guard insisted that no, Rowan had not been fucked by any of the other orcs. Yet."
"Her gaze softened and she returned to Rowan, inspecting his body and pulling off some of his clothing to reveal the scars underneath."

orcc "Oh? A warrior dis one. Well, warrior, you tink you can last wid me? I could use a toy dat can last all day."

"At the same time, Rowan was given a chance to observe her as well. More muscular than the typical female orc but not to the same extent as most males. Her breasts would easily fill a human's hand, although they looked about average on her large frame."

orcc "Say, do someden! Ya may be pretty, but ya ain't no fun."

"That was a good sign if he didn’t want to find himself being used as her toy. He couldn’t react. Any sign of weakness would shift the dynamic."

menu:
    "Accidentally meet her eyes.":
        $ released_fix_rollback()
        jump chieftessSexScene
        
    "Continue ignoring the taunting":
        $ released_fix_rollback()
        orcc "Notting? Boy you are bo-ring. We see how you are after a couple days on a post. Den you'll be begging to be a proper toy. If he still stubborn, den da tribe gets him."
        "Rowan had to stop himself from sneering."
        "She waved the two off and Rowan was taken to a set of posts and tied to it. Another human was tied up here as well, a woman. She glanced at Rowan briefly, but didn't try to talk to him." 
        "Soon after, another orc came and took her down. She was lead off without complaints to one of the tents. Well, that was for the best. It meant that Rowan would get less attention."
        scene bg26 with fade
        show rowan necklace neutral at midleft with dissolve
        show andras happy at edgeleft with moveinleft
        "Nearly an hour later, a familiar red demon was sideling up to the post with a satisfied smirk on his face. The cavalry was here."
        an "Well, well, well, what do we have here? Stubbed your toe and suddenly in need of rescue?"
        ro "Hardly."
        show andras displeased at edgeleft with dissolve
        "Rowan effortlessly slipped free of his bonds and stood with a stretch."
        ro "I figured out the ropes within the first hour. I was just waiting until... ah!"
        hide rowan with moveoutright
        show rowan necklace neutral behind bg26
        "Spotting the other hunting group get back, Rowan walked confidently up to the orcish woman who'd 'captured' him. He rolled his shoulder, still stiff from the ropes."
        ro "I believe you have something that belongs to me."
        femorc "Wha dis? Humie out of his ropes?"
        ro "This humi is a demon's agent, and..."
        "The man rushed forward and elbowed the orc in the stomach, then swept her feet out from under her when she tried to hit him back. Before she could recover, Rowan yanked his sword off of her belt and returned it to his own."
        ro "... he'll be taking back his property."
        hide rowan
        show rowan necklace happy at midleft with moveinright
        ro "I'll be returning to exploring now, if that pleases you, Master?"
        show andras happy at edgeleft with dissolve
        an "Ha! Yes, that will be fine."
        #rowan takes a small amount of humiliation damage - TODO
        $ change_recruitment_bonus('barracks', 2)
        return

label chieftessSexScene:
    
orcc "Oh?"

"She grabbed Rowan's face, forced him to look her in the eyes again. She chuckled, then released his head and ruffled his hair."

orcc "I'm keeping you."
orcc "Who brought him? He's worth a double wine prize."

"She accepted the rope from the hunter as he relayed the story of Rowan's capture, then led him off to her tent."

scene bg30 with fade
show rowan necklace neutral at midleft with dissolve

"The interior was dominated by two things: a veritable horde of deer antlers and a large bedmat."

orcc "You real tough out der, may fool my boys and girls, but not fool me."

"She flipped Rowan around and roughly grabbed his jaw, forcing him to meet her gaze again."

orcc "You definitely toy material. I'ma enjoy breaking you in."

"The man squirmed in her grip to try and free himself, but could do nothing against the stronger orc's grip on his bonds. He did succeed in annoying her enough to slap him across the face twice."

orcc "Enough of dat. Wedder you give in, or I have to beat you first, I will get what I want."

ro "Fine."

orcc "He speaks! Well, let's see if ya moan too."

"She roughly ran one of her thick digits over his crotch, then slipped it inside his pants and yanked both them and his undergarments down."

orcc "Hehe, already hard for me too. I knew you wanted me on you."

"Although she wasn't trying to hurt Rowan, her treatment had not grown gentle or caring. It was with the typical orcish brutality that she forced Rowan to kneel down, then shoved him onto his back."
"After planting a foot on his chest and releasing his bindings, the chieftess undid the scraps of fabric covering her loins. Loop after loop came off with significantly more care than had been shown before."
"There was a certain amount of satisfaction on her face at Rowan's reaction to seeing her reveal her sex."

orcc "Dis is your new Master. Betta make it feel good or ya gonna be ravaged by all dem in my tribe and da boys too."

#CG1
scene cg608 with fade
show rowan necklace aroused behind cg608
pause 3

"Without removing her foot, Rowan's legs were hoisted into the air. Both of the man's boots were casually yanked off and tossed into the corner, followed by his pants being roughly jerked and shook off."
"Now she finally took her weight off of him and pressed her new toy's legs firmly against either side of his body. Even if his arms weren't tied and he'd had the strength to overcome this monstrous woman, Rowan couldn't have done anything against her now in such a helpless position."
"The orc knew it too, and it was with some pleasure that she settled herself down on him and guided his member into her sex."

orcc "Like dis pretty boy? I certainly do."

"Rowan let out an involuntary groan, the feeling of her sex clamping down on him followed by rapidly plopping herself up and down on his length was too much to keep his voice back."

orcc "Dat's what I like to hear."

"Being fucked in such a compromising position was surprisingly exotic and exhilarating. It certainly suited this orc chiefess to ride her conquests in such an amazonian way."
"Their eyes locked together while her hips continued to bounce up and down, making an audible smack with each drop that hilted Rowan's member. Rowan couldn't help but groan yet again."

orcc "Yes! Keep making dos nice noises."

ro "(Is it the humiliation...or am I actually enjoying this?)"

"In true orcish fashion, the rough fucking soon reached climax for both of them. The chieftess finally let Rowan catch his breath after he painted her insides white."

orcc "Hehe, good enough for first time, wonder how long you'll last in da next one?"

"She didn't wait for a response. Just let out a couple groans of her own while she stood up and stretched. This gave the man a chance to reposition himself into a much less uncomfortable orientation and finally get his bindings into his hands."
"She walked over to a case in the corner of the tent with her bits still exposed and dripping with a mixture of white and clear. When she returned, she was drinking from a leather flask. After taking a few sips, she pressed the skin to Rowan's lips and let him have a taste of watered down wine."
"While Rowan was not surprised when she plopped herself back down on top of him, her lips suddenly pressing against his own in a deep kiss was. The sudden romantic affection sent blood rushing back into his deflating member."
"She broke the kiss and smiled triumphantly."

orcc "Feels like humie's ready to go again. Lookies like he might be good enough to stay with me after all."

"Once more, she roughly kissed him, then licked Rowan's ear and whispered to him:"

orcc "You belong to me. No one else can touch you."

scene bg30 with fade

"Nearly an hour later and at the end of the fourth round of orcish chainsex, Rowan finally managed to slip the knot on his bindings free. There was no end in sight to this woman's lusts and he knew that Andras would be arriving soon."
"The orc chief was worn out enough that he could finally take her on in a wrestling match, and her surprise at his sudden freedom was enough of an advantage to turn the bonds against his captor."
"Just in time as well, as shortly after things turned to violent wrestling, a familiar red skinned demon opened up the tent flap."

show andras displeased at midleft with moveinleft

an "Oh Rowan? Your mighty Master is here to save you from your incompetence."

"Rowan pulled the rope tight, finishing the process of tying up his former captor. He stood and grabbed his fallen clothing from the floor."

show rowan necklace neutral at midright with moveinright

an "Hmm? Well, I'd expected to find you were in need of rescue, but it seems like everything is well in hand."

ro "That's one way of putting it."

"He looked over his shoulder at Andras as he spoke, then turned back to the bound chief. "

ro "Looks like I don't belong to you anymore."

orcc "Grrr, I didn't like you anyway. Remember dat I will make you pay for taking away my tribe."

ro "Oh, you don't need to worry about what happened here leaving your tent, assuming you do as my demon Master tells you. "

"He stood, stretched, and put his pants back on."

ro "Now, if you'll excuse me, there's one more thing I have to take care of."

hide rowan with moveoutleft

scene bg26 with fade
show rowan necklace neutral at midright with moveinright

"The hero stepped outside the tent and scanned the tribe for the one he was looking for. Conveniently she was at the nearest campfire, admiring exactly what he needed."

ro "I believe you have something of mine."

femorc "Wha dis? Humie out of his ropes?"

ro "This humi is a demon's agent, and..."

"A kick sent the orc over as she tried to stand up, then the man dropped his knee into her stomach to make sure she stayed down."

ro "... he'll be taking back his property."

"He strapped his sword back on his belt and returned to Andras."

scene bg30 with fade
show andras displeased at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "I'll be returning to exploring now, if that pleases you, Master?"

show andras happy at midright with dissolve

an "Ha! Yes, that will be fine."

#rowan takes a small amount of humiliation damage - TODO
$ change_recruitment_bonus('barracks', 2)
return


#############################################################################################################
#############################################################################################################
#############################################################################################################

label introductions_count_for_something:

scene bg26 with fade
show rowan necklace neutral at midleft with dissolve
show andras displeased at edgeleft with dissolve
show wild orc neutral behind bg26

"Shortly after Andras had arrived, he pulled Rowan behind a bush near the tribe and started whispering conspiratorially in the man's ear."

an "Listen Rowan, I want you to introduce me. The way your human nobles get introduced at the start of parties."

ro "What, I'm your crier now?"

an "Make me sound as impressive as you can, doesn't matter if it's real or not. But remember, these are orcs."

ro "You sure you want me for that? Boasting and propaganda aren't exactly my specialty."

"The demon made an exaggerated look around."

an "Hmm, I don't see anyone other than you, so I guess today is your lucky day to try and impress me."

menu:
    "Just do it.":
        $ released_fix_rollback()
        jump orcJustDoIt
    
    "Refuse.":
        $ released_fix_rollback()
        ro "We’re out here negotiating and you want me to stand around in the middle of the camp and shout about how large your cock is?"
        an "I never said anything about my cock, but good suggestion."
        ro "..."
        an "..."
        ro "You’re fucking with me, aren’t you?"
        "Andras didn’t say anything in response. But, he did give Rowan a dark smile. A moment later his face softened a bit and he leaned in closer."
        an "This is a great routine for recruiting orcs, I'm trusting you to back me up. Come on, you aren't doing anything for the next few minutes, are you?"
        menu:
            "Insist on not doing it.":
                $ released_fix_rollback()
                ro "I'm sure I'll screw it up. Getting troops is important. We need it to fight the war. Surely you value your power and the war effort more than that."
                "Andras rolled his eyes."
                an "You and my sister are both such sticks in the mud. Yes, yes, the war effort is important. Do whatever."
                "Andras huffed, but didn’t push the point. As much as he liked to swagger about, he too saw the importance of diplomacy. Rowan got the feeling he wouldn’t always be able to refuse Andras that way. Not if he enjoyed having a head."
                $ change_favor('andras', -1)
                $ change_recruitment_bonus('barracks', 1)
                return
                
            "Don't antagonize him.":
                $ released_fix_rollback()
                jump orcJustDoIt


label orcJustDoIt:

show andras at edgeright with moveoutright

"Then he abruptly stood up and strode straight into the middle of the tribe. Rowan hesitated a second, but having no other choice in the matter, he following after and started calling out."

ro "Uh, introducing Andras, the great demon lord of Bloodmeen!"
ro "Listen up all you orcs, this mighty demon has come to claim this land for his own! To make slaves and servants of the humans, to kill those who don't fall in line!"

"The various members of the tribe were slowly shuffling bleary eyed out of their tents or looking up from their fires in confusion."

$ successCount = 0

#perception test - TO DO
$ res_roll = dice(6)
if res_roll > 3:
    "Rowan noticed that there only seemed to be one human slave in the camp and that there didn't seem to be very much food on the fires. The orcs had a grumpy and underfed look about them."      
    ro "His orcs have scores of slaves to sate their lusts on and feast every day on the bounties of his conquests!"
    ro "Follow him, and you shall never go hungry again!"
    "That certainly got attention, one of the orcs threw down his measly scraps into the fire and stood up with something between a cheer and a roar. Then he seemed to think better of disposing of his meal and his face fell."
    $ successCount += 1
else:
    ro "His orcs are the best warriors in the lands, victors of a hundred battles, and devoted enough to fight a hundred more!"
    "The orcs were listening now, even if they were not the most rapt audience."

#brawn test - TO DO
$ res_roll = dice(6)
if res_roll > 3:
    ro "Behold how might and handsome your new lord is!"
    show andras happy at edgeright with dissolve
    "This got a sudden grin from his master, and Andras immediately played along by flexing his muscles, striking poses, and slowly turning around to show off to the onlookers."
    ro "None is more ferocious or tough! I can attest that this master is both virile and generous in his affections. A single time with him will certainly be the best experience you've ever had!"
    wo "You aint bad neither!"
    "Andras grabbed Rowan around the shoulder and nudged him in the arm, then dragged him into more muscular posing and some rather lewd poses. The orcs jeered in appreciation, yelling out cat calls."
    $ successCount += 1
else:
    ro "Behold how mighty and handsome your new lord is!"
    show andras happy at edgeright with dissolve
    "This got a sudden grin from his master, and Andras immediately played along by flexing his muscles, striking poses, and slowly turning around to show off to the onlookers."
    ro "None is more ferocious or tough!  I can attest that this master is both virile and generous in his affections- "
    wo "Of course you can, ya sissy!"
    wo "“Mighty and handsome”?! Bwahahaha, you always kiss his ass like this before you start sucking his cock?!"
    "A wave of jeering laughter passed over the crowd, making Rowan blush in furious embarrassment. He quickly changed the topic, hoping to win the crowd back. "

#deception test - TO DO
$ res_roll = dice(6)
if res_roll > 3:
    ro "This demon has slain a dozen knights at once in personal combat!"
    "Andras slashed at the air with his fingers faster than the eye could trace. Yielding appreciative calls from the crowd."
    ro "He can hurl a spear further than the mightiest of ogres!"
    "One of the tribesman lost their spear, which soon flew over the treetops and out of sight.  Laughter erupted around the camp."
    ro "He's, uh, even wrestled a dragon to submission?"
    "Now the slightly annoyed tribesman was in the air too, caught, and slammed to the ground. The cheers from the onlookers covered for Rowan's sudden silence as he put his head in his hands."
    ro "(Right... orcs. Sometimes they don't mind rough handling.)"
    $ successCount += 1
else:
    ro "This demon has mastered a dozen combat styles."
    "Andras performed some impressive footwork and flourished a spear he grabbed from a nearby tribesman."
    ro "He knows twice as many ways to kill a man in a single strike!"
    "The spear spun furiously fast, then slashed down. Laughter erupted from the camp as the tribesman started struggling with Andras to recover his lost weapon."
    ro "Uh, he can, uh...."
    "Rowan's voice faltered as the scene unfolded before him. No one was paying any attention to him anymore anyway."
    "Predictably, it ended with the orc face down in the mud with his spear rammed up his ass. The other orcs seemed to find it more amusing than annoying."
    wo "Stuppid. Ya don' fight demon masters!"

"Now the tribe was getting impatient, so the performance had to come to a close."

ro "This demon has come for you! For soldiers to fill the ranks of his invincible armies!"

scene bg26 with fade
show rowan necklace neutral behind bg26

if successCount > 2:
    "The performance had gone over quite well and many new recruits were soon to be travelling to Bloodmeen to begin their training."
    show andras happy at center with dissolve
    an "Well done Rowan. Perhaps I should get you to back me up more often."
    ro "Should I add crier to my list of professional duties in Bloodmeen?"
    $ change_favor('andras', 1)
    $ change_recruitment_bonus('barracks', 2)
    #gain XP - TO DO
    #gain skill exp to one of either perception, brawn, or deception at random - TO DO
    return
    
elif successCount > 1:
    "That hadn't been Rowan's best work.  Even still, he'd managed to keep things from being a disaster.  This camp could be relied on to give their share of recruits."
    $ change_recruitment_bonus('barracks', 1)
    #gain XP - TO DO
    #gain skill exp to two of either perception, brawn, or deception at random - TO DO
    return
    
else:
    show andras displeased at center with dissolve
    an "Rowan, you fool. You bloody fool. Did you really think those lame boasts would really impress orcish warriors. Did you believe they could capture my..."
    show andras happy at center with dissolve
    "Andras couldn’t even finish the sentence before bursting out in laughter."
    an "You’re fucking terrible at boasting, you know that?"
    ro "I tried to tell you that in the first place."
    an "Yes, yes. Get out of here you moron. Gotta find an actual, what did you call it? Crier? Gotta find me a real one."
    "Rowan wasn’t sure if he should be angry about this..."
    $ change_recruitment_bonus('barracks', 0.5)
    #gain XP - TO DO
    #gain skill exp to one of either perception, brawn, or deception at random - TO DO
    return
    
    