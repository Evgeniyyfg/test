# random map events that happen on plains
init python:

    #Brigand Slavers
    #Requires: After first warning of famine sweeping area, after Castle Raeve assault at least
    # TODO: probably switch dependence to rumor of famine
    event('brigand_slavers', triggers='map_expl', conditions=('world.cur_tile_type == "plains" or world.cur_tile_type == "road"',), run_count=1, depends=('famine_looms', 'raeve_keep_visit_goal2'),
        group='map_expl', priority=pr_map_rnd)
    #Tower Ruin
    event('tower_ruin', triggers='map_expl', conditions=('world.cur_tile_type == "plains" or world.cur_tile_type == "road"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('impure_visions', triggers='map_expl', conditions=('world.cur_tile_type == "plains" or world.cur_tile_type == "road"', 'week > 21', 'castle.buildings["brothel"].lvl >= 1',), run_count=1, group='map_expl', priority=pr_map_rnd)
    

label brigand_slavers:
#Brigand Slavers
#Requires: After first warning of famine sweeping area, after Castle Raeve assault at least
scene bg31 with fade

"Rowan heard the group long before they came into view."
"Many feet, marching out of time; Rough laughter and swearing asides; the rattle and clink of chains. Half a dozen men, armed with knives, swords and crossbows, marching twenty souls in rags, bound together at the wrists."
"When he saw Rowan on the road ahead, the leader called a halt with a sharp jerk of his hand."

if avatar.infamy < 10:
#infamy low to medium
    brig "'ere, I know you. The big peasant hero from the last war, ain't it? Reagan, or summat. I've worked with lads who marched under you, once upon a time."
    "He gave the train behind him a lazy eye. A couple of the other brigands looked away, bitterness on their lean, dirty faces."
    brig "Well, hero lad, we ain't got no quarrel with you. These are different times, when ordinary jacks got to do some hard things in order to stay alive."
    brig "Reckon a real man of the people would see that, and go about his business, and let us go about ours. That sound about right?"
    "The other bandits watched Rowan carefully, hands close to their weapons. The slaves at the head of the train looked at Rowan, hollow-eyed and helpless."
    jump .brigmenu
#else
else:
    brig "'Ere, I know you. The big peasant hero from the last war, ain't it? Reagan, or summat. Sounds as if you've been changing your stripes, though. Sad state of this world, eh?"
    ro "What are you doing?"
    brig "Getting by. Ordinary jacks got to set their hands to some hard things to do that, these days. But I reckon a pragmatic gentleman such as yourself can appreciate that. Perhaps you'd be interested in buying some of our stock?"
    brig "They'll be cheap - can't afford to feed 'em all, that being the truth. Gonna have to get rid of some, ‘tween here and the pits."
    "The other bandits watched Rowan carefully, hands close to their weapons. The slaves at the head of the train looked at Rowan helplessly."
    jump .brigmenu

label .brigmenu:

menu:

    "Let them go.":
        $ released_fix_rollback()
        ro "I have no interest in any of this. Get out of my sight."
        "The brigand leader smirked, and his compatriots relaxed."
        brig "I'm glad you've got some sense about you, at least. A pleasant day, Sir Robert, or whatever it was."
        "He jerked his hand brusquely, and the other brigands shoved the slave train back into motion. The sound of chains and shuffling of feet took a while to fade entirely out of range of Rowan's ears."
        #gain a small amount of infamy
        $ change_base_stat('f', 1)

    #low corruption only
    "Demand they release the slaves." if avatar.corruption < 10:
        $ released_fix_rollback()
        ro "You will release those people this instant, or I'll kill you where you stand, blaggard."
        brig "Shame. I was led to believe you were smart."
        "One of the other men suddenly raised his crossbow and fired."

        #dodge check DC12
        $ event_tmp['dodge check'] = check_skill(12, 'dodge')
        if not event_tmp['dodge check'][0]:
        #fail
            "Rowan jerked to one side, but could not stop the bolt thudding with numbing force into his armor."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Rowan acrobatically flung himself to one side, and the bolt whistled past his shoulder. Then the brigand leader was upon him, foul-smelling and fierce, trying to bear hug him into the point of his dirk."

        $ event_tmp['strength check'] = check_stat(10, 'strength')
        #strength check DC10
        if not event_tmp['strength check'][0]:
        #fail
            "Rowan struggled hard and managed to pull away enough to stop the blade piercing his innards, but still received a vicious slice across his ribs."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Rowan struggled like a wolverine, landing an uppercut on the man's unshaven chin and making him swing the vicious blade into empty air."

        if not event_tmp['strength check'][0] and not event_tmp['dodge check'][0]:
        #Failed both checks
            "Doubled up in shock from his wounds, Rowan could not stop the brute punching him in the gut and sending him sprawling into the roadside ditch."
            "Jeering laughter and cheers from the other bandits, interspersed with aghast groans from the slaves, accompanied his fall."
            brig "This world ain't got a place for your type anymore, hero lad. Learn that, or die."
            "He jerked his hand brusquely, and the other brigands shoved the slave train back into motion. The sound of chains and shuffling of feet took a while to fade entirely out of range of Rowan's ears."
            return
        else:
        #passed one check    # or two
            "Rowan pulled away long enough to pull out his own blade, and swung it hard and true across his assailant's unguarded throat. With a wet choke, he collapsed into the dirt."
            ro "Run, or face me, cowards."
            "The other brigands' eyes flicked between the body of their leader and Rowan, then first one then the rest turned and fled. Rowan searched the corpse's pockets, and duly found a key that fitted the shackles of the slaves."
            slave "I - I don't know what we'll do, truth be told, master. We were fleeing south from the famine when they jumped us. They took what little we had. But... anything is better than being at the mercy of men like that."
            slave "We'll think of something. Thank you so much, Sir Rowan - for as long as I live, I will tell anyone that cares to listen that you are the last truly honourable man in Rosaria."
            "Rowan watched them depart, aglow with chivalric pride."
            #gain 25 xp, lose some infamy and guilt
            $ add_exp(25)
            $ change_base_stat('f', -1)
            $ change_base_stat('g', -1)
            return

    "Buy Slaves.":
        $ released_fix_rollback()

        ro "They're offering these prisoners for cheaper than what I could probably ransom them for. And even being at the whim of Andras and Jezera is better than being marched to their deaths by this lot..."
        ro "Alright. I'll take some."
        brig "How many?"

        menu:
            "Can't afford any.":
                $ released_fix_rollback()
                ro "On second thoughts..."
                brig "Humph. Just as well we didn't try to rob you. What a waste of time."
                "He jerked his hand brusquely, and the other brigands shoved the slave train back into motion. The sound of chains and shuffling of feet took a while to fade entirely out of range of Rowan's ears."
                #small infamy boost
                $ change_base_stat('f', 1)
                return

            #allow extra choices to buy [5], [10], [15], or [20] slaves with the following outcome
            # TODO: check for free space for prisoners?
            'Buy 5' if castle.treasury >= 5 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 5
            'Buy 10' if castle.treasury >= 10 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 10
            'Buy 15' if castle.treasury >= 15 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 15
            'Buy 20' if castle.treasury >= 20 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 20
        $ released_fix_rollback()
        "Keeping a watchful eye on the other brigands, Rowan handed the gold over."
        #if not 20
        if event_tmp['buy slaves'] < 20:
            "The leader produced a key, and snapped clear the number of ragged souls Rowan had just purchased."
        #else
        else:
            "The brigands shoved forward the full score of ragged souls Rowan had just purchased."
        slave "You- you have no right to do this! We are just ordinary men, like you-"
        brig "Quit yer yapping, dog! A pleasure doing business with you, Sir Redmond. I only hope we get to do so again."
        "With the crystal, it only took Rowan a few minutes to call in a squad of orcs, who roughly led the ragged chattel away."
        "Watching them go, Rowan could almost convince himself he'd more or less rescued these people from being either marched to death, or sold to even worse masters. Almost."
        #minus gold (5 gold per prisoner) and gain prisoners equal to the number of slaves purchased, medium guilt and infamy gains
        $ change_treasury(-5 * event_tmp['buy slaves'])
        $ change_prisoners(event_tmp['buy slaves'])
        $ change_base_stat('g', 3)
        $ change_base_stat('f', 3)
        return

    #High corruption only
    "Kill Them, Take the Slaves For Yourself." if avatar.corruption >= 10:
        $ released_fix_rollback()
        ro "Filth like you don't deserve slaves. I believe I'll kill you, and take them as my own."
        brig "You will, will you?"
        "One of the other men suddenly raised his crossbow and fired."

        #dodge check DC12
        $ event_tmp['dodge check'] = check_skill(12, 'dodge')
        if not event_tmp['dodge check'][0]:
        #fail
            "Rowan jerked to one side, but could not stop the bolt thudding with numbing force into his armor."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Rowan acrobatically flung himself to one side, and the bolt whistled past his shoulder. Then the brigand leader was upon him, foul-smelling and fierce, trying to bear hug him into the point of his dirk."

        $ event_tmp['strength check'] = check_stat(10, 'strength')
        #strength check DC10
        if not event_tmp['strength check'][0]:
        #fail
            "Rowan struggled hard and managed to pull away enough to stop the blade piercing his innards, but still received a vicious slice across his ribs."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Rowan struggled like a wolverine, landing an uppercut on the man's unshaven chin and making him swing the vicious blade into empty air."

        if not event_tmp['strength check'][0] and not event_tmp['dodge check'][0]:
        #failed both checks
            "Doubled up in shock from his wounds, Rowan could not stop the brute punching him in the gut and sending him sprawling into the roadside ditch. Jeering laughter and cheers from the other bandits accompanied his fall."
            brig "Those were some big words for an absolute streak of piss. Keep them to yourself next time."
            "He jerked his hand brusquely, and the other brigands shoved the slave train back into motion. The sound of chains and shuffling of feet took a while to fade entirely out of range of Rowan's ears."
            return
        else:
        #succeeded one or more
            "Rowan pulled away long enough to pull out his own blade, and swung it hard and true across his assailant's unguarded throat. With a wet choke, he collapsed into the dirt."
            "Rowan advanced upon the other brigands, face alive and terrible with blood lust. Before he'd even reached the first, though, they had fled, unnerved and aghast at this living embodiment of chaos they'd been unfortunate to happen upon."
            "The slaves drew back from him and the corpse twitching in the dirt, ashen terror chalked on their gaunt faces."
            ro "Do exactly as I say and you won't share the fate of that fool."
            "With the crystal, it only took Rowan a few minutes to call in a squad of orcs, who roughly led the ragged chattel away. Rowan watched them go, thoroughly satisfied with his catch and the manner in which it was gained."
            #gain 20 prisoners, gain 25 xp, gain a large amount of infamy
            $ change_prisoners(20)
            $ add_exp(25)
            $ change_base_stat('f', 5)
            return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label tower_ruin:
#Tower Ruin
#No requirements
scene bg31 with fade

"Stood on top of a nearby hill was the ruin of an old watchtower - a solitary finger of stone crumbling off into nothing thirty feet off the ground, a remnant from a different age of man."
"It would be the den of ne'er-do-wells, or haunted, Rowan guessed. In the lowlands, unguarded finished stone was rarely left for long before it was appropriated by peasantry. He had to consider whether it was worth the risk and time to explore the ruin."

menu:
    "Search.":
        $ released_fix_rollback()
        "Rowan made his way up the rubble-strewn hill and entered the tower through a gap in the wall. There was bad taste to the air inside, a feeling of malignity and despair seemingly baked into the stone itself, confirming his suspicion that the place was haunted."
        #stealth check DC12
        if not check_skill(12, 'move_silently')[0]:
        #fail
            "Rowan tried to remain as quiet as possible as he picked his way through the stone and rotting furniture inside, searching for anything that might be valuable, but the black atmosphere compressed around him until it felt like he was suffocating, body and mind."
            "It was like drowning at the bottom of a deep, deep well. Down which {i}things{/i} were whispering terrible things..."
            "Rowan's nerve failed, and he stumbled desperately back to the gap in the wall and collapsed out of it, heaving down great lungfuls of air once he was back outside."
            "He recovered his breath after a few moments - but the feeling of being tainted, black words and thoughts insinuated into his mind, remained."
            #lose 1 move point, gain a small amount of corruption
            $ change_mp(-1)
            $ change_base_stat('c', 1)
            return
        else:
        #pass
            "Rowan kept as quiet as possible as he picked his way through the stone and rotting furniture inside, searching for anything that might be valuable.The ominous oppressiveness of the tower remained, but Rowan kept his thoughts as innocuous and quiet as his footstep, and this way it seemed he avoided disturbing the unsleeping shades that lurked within it."
            "The ominous oppressiveness of the tower remained, but Rowan kept his thoughts as innocuous and quiet as his footstep, and this way it seemed he avoided disturbing the unsleeping shades that lurked within it."
            #lose one move point
            $ change_mp(-1)

        #loot rolls
        $ event_tmp['loot rolls'] = dice(4)
        $ released_fix_rollback()

        if event_tmp['loot rolls'] == 1:
        #1/4 chance - nothing
            "Unfortunately, there was nothing of interest in the tower. The ghosts here guarded nothing but bitter memories of their own demise, it seemed. Disappointed, Rowan crept carefully back out of the ruin and continued on his way."
            #gain 20 xp
            $ add_exp(20)
            return
        elif event_tmp['loot rolls'] == 2:
        #1/4 chance - random piece of armour
            "Halfway up the stairway that wound around the inside of the tower Rowan found skeletal remains, an arrow running through its leering skull."
            "Clutched in its hands was a piece of armor - something the warrior had failed to pull on in time, perhaps. Guarded from the elements, it still looked in good condition."
            "Rowan carefully retrieved it from the bony, moldering hands of its former owner and then retraced his steps, glad to make his way back down the hill with his prize and leave the ruin far behind."
            #gain one random piece of armour, gain 20 xp
            $ add_exp(20)
            $ get_rnd_item(0, 500, 'armour')
            return
        elif event_tmp['loot rolls'] == 3:
        #1/4 chance - money
            "In the tower's lower level, Rowan found a storage area, which looked like it had already been ransacked - and within which a large number of people had met unpleasant ends, going off the number of skeletons he had to toe his way around."
            "In a small depression by the far wall, he found a small chest filled with thick coins. Ancient denomination, but gleaming softly with gold."
            "The chest wasn't hidden. Why hadn't it been taken? Cursed? Nothing bad seemed to happen when Rowan gingerly fingered the coins, then transferred them to his own pouch, then retraced his steps back out of the tower."
            "Happy with his prize and even happier to leave the haunted ruin behind him, he headed back down the hill and continued on his way."
            #gain one hundred gold for the treasury, gain 20 xp
            $ change_treasury(100)
            $ add_exp(20)
            return
        else:
            #1/4 chance military information
            "There was nothing of material value in the tower, all of it lost to whatever catastrophe had befallen the place when it had known living occupants. However - in the main chamber, Rowan found a large map nailed to the wall, crumbling but still well preserved."
            "It showed mountains, rivers, fortresses and arsenals, troop movements, terrain bottlenecks, where stores would be kept in times of war."
            "It was clearly outdated, but from his own knowledge Rowan could discern that it was a map of Rosaria, its main settlements and granaries unchanged."
            "He thought this information may well allow him to guess how and where the Baron's forces were likely to line up, maybe even get the jump on them should it come to a straight fight."
            "He carefully copied the map's details down, then retraced his steps out of the tower, happy to leave the cursed place behind."
            #todo - Rosaria loses military points
            #gain 20 xp
            $ add_exp(20)
            return

    "Leave it alone.":
        $ released_fix_rollback()
        "Let sleeping towers lie, Rowan decided. He continued on his way, quickly leaving the ruin behind."
        return

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

label impure_visions:
    
scene bg31 with fade

"Through what felt like endless plains and open fields, Rowan came across a dirt road that wound past an abandoned church and stretched onward into the distance, disappearing through the trees."
"It was not the road that caught Rowan's eye, however, but the modestly dressed nun walking along it."
"The nun held herself in a dignified manner, her nose turned up in distaste as she passed the church. She looked insulted by its clear abandonment, as though she too were forgotten in this empty field."

show rowan necklace neutral at midleft with dissolve

sisgw "Well met traveler. May I have your name."

ro "To you as well, sister. I am Rowan."

"She smiled, her footsteps slowing to a stop in front of him. Rowan halted as well, giving the woman a modest smile in return."
"Now that she was close enough, he could see just how young this nun was: barely past her youth but no less a woman, all of her feminine shame hidden behind thick layers of black robes." 
"Rowan saw her eyes light up with recognition."

sisgw "You are not {i}the Rowan{/i}, are you?"

ro "Oh...I’m afraid I am."

"The nun bowed, and Rowan recognized the look of admiration in her eyes."

sisgw "It is an honour to meet you, Hero. The people cannot thank you enough for your service."

ro "The pleasure is all mine, but please, just leave it as Rowan. And whom do I have the pleasure of meeting out here?"

"The nun held herself upright, ever the prim and proper lady."

$ gwenName = "Sister Gwen"

sisgw "Sister Gwendoline Mathy at your service, sir… Rowan."

"She smiled a little to herself as she spoke his name."

sisgw "But everyone calls me Sister Gwen for short."

ro "Sister Gwen it shall be then. Ah, since I have you here, could you tell me where the next town is? I have to replenish some of my supplies."

"Sister Gwen gestured further down the road, opposite the way she came."

sisgw "The nearest town is just a little ways down this path here. Would you allow me to accompany you?"

if avatar.corruption > 30:
    "Rowan shot her body an occasional glance as he walked. A shame it was hidden by those dowdy religious robes. Nuns were no fun."

"Sister Gwen held herself a little taller and walked alongside Rowan toward the next town. As sunset settled over the horizon, Rowan wondered what a nun as young and unarmed as Sister Gwen was doing out here alone."

ro "So, if you don't mind me asking, what are you doing out here? It's dangerous to be crossing between towns at night."

sisgw "It's not technically night yet though, is it, Rowan?"
sisgw "I am here on behalf of the Torsend Abbey. There have been rumors, you see, of… well, rather strange occurrences happening in Rosaria, so I've been asked to look into them."

ro "Strange occurrences?"

"He already had a pretty good idea as to what Gwen was referring to-- the changes he had been participating in were not exactly meant to be kept a secret-- but knowing how quickly word travelled left him feeling unsettled. "
"His involvement with Bloodmeen was only growing, and there was only so much time before everyone knew what became of their dear Hero."
"Sister Gwen appeared reluctant to relay the information, but Rowan could sense the trust in her eyes as she looked over the great Hero of Karst, and decided he was worthy of such tales."

sisgw "Oh, absurd things: demons, incubi, orcs, what have you. All ridiculous nonsense, if you ask me, but the faith will not hesitate to ease the minds of the people here."

ro "Ridiculous, you say?"

sisgw "Of course. The only people that can claim to see an incubus or succubus are people of impure thoughts. A true sighting would be a rare thing indeed. Only a truly impure woman would imagine such a creature visiting her in the night."

"Sister Gwen shook her head in disgust, {i}tsk{/i}'ing quietly to herself."

sisgw "What these people need is to pray for forgiveness and cast out the impurity in their hearts. Nothing more."

"Sister Gwen seemed so certain and confident in her speech that, if Rowan hadn't seen the dangers himself firsthand, he may have been inclined to believe her."

menu:
    "Tell her to take the threat seriously.":
        $ released_fix_rollback()
        $ change_base_stat('g', -3)
        $ change_base_stat('c', -5)
        if avatar.corruption < 31:
            "It was bad enough that Sister Gwen felt she could wander between towns alone, but to not even take the threats her own abbess gave her seriously… It worried him more than Rowan cared to admit."
        else:
            "Surely this maiden was heading to a disaster. To disbelieve even the warnings of her own abbess." 
            "Perhaps it would be karma to see her taken and exposed to the true dangers that lurked out there. But, some small part of Rowan could not let that happen."
        "Not wanting to drive her away from his warning, Rowan decided to be careful with how he approached the topic." 
        "He needed to warn her, but if he even gave the slightest hint away of his own allegiance with Andras and Jezera, Sister Gwen would never take him seriously. In fact, she may even condemn him entirely…"
        ro "You know, Sister Gwen, I've faced many beasts since my time in the war. The demon lord may be dead, but those that followed him are not."
        sisgw "Is that so?"
        "Sister Gwen did not seem to believe him. She spoke as though entertaining a child's story. Did she really see no threat here? He had to make her understand somehow."
        ro "I worry for the villages here, Sister Gwen. I pray they do not get taken in by the creatures wandering these woods."
        "Her laughter was not something Rowan had expected."
        sisgw "You mean to pull my leg. Just because you are a hero does not mean I will fall for these gags. We all know such problems were taken care of long ago."
        sisgw "Karnas is dead. There won’t be another demon war for a lifetime."
        "She dismissed his warning with a wave of her slim hand. Rowan could not help but realize just how small Sister Gwen was: naively brave and new to the world." 
        "She had likely spent much of her life up until this point in a convent, sheltered from the travesties that unravelled throughout Rosaria." 
        ro "I am not joking, sister."
        "Sister Gwen raised an eyebrow, but after seeing the grave look on his face, he noticed how her body stiffened and she seemed to actually take a glance at her surroundings, searching between the trees and across the plains for one of the horrendous beasts her church spoke of."
        sisgw "You believe in these rumors then, Rowan?"
        ro "I believe that times are changing, sister, and there are more things that stalk the land than just wild animals."
        "Sister Gwen drew silent, and the sun dipped lower over the horizon, stretching the shadows of the nearby forest across the fields like clawed hands. There was a chill in the air, a foreboding that could not be ignored."
        sisgw "Could you say you have seen this firsthand, Rowan? The demonic activity?"
        "Her gaze was searching, and he knew she was putting her trust in him as a hero to tell the truth. While she kept her expression indifferent, Rowan noticed how her hands were clenched tightly in front of her and that she stepped a little quicker down the road."
        ro "...Yes. I have."
        "The nun's lips pressed together in a tight line. She did not want to believe in it, but hearing it come from a man who had fought these very creatures firsthand, it was hard to ignore."
        ro "You should be careful, Sister Gwen. These monsters are nothing to take lightly, and if you do, they will have you in their trap before you realize it."
        "The weight of the amulet suddenly felt very heavy around Rowan's neck, but he tried not to draw attention to it. Sister Gwen's face paled and she nodded, her body moving a little closer to Rowan as they continued their journey to town."
        sisgw "...I see."
        "Although she did not make any such promises, Rowan felt that he had gotten through to her, and that was enough."
        "They reached the outskirts of a local village shortly after, and Rowan bid the nun farewell. There wasn't much in his power he could do, but every little warning counted."
        return
        
    "Teach her a kinky lesson." if avatar.corruption > 30:
        $ released_fix_rollback()
        $ change_base_stat('c', 5)
        $ change_favor('jezera', 1)
        jump gwenSex
        
label gwenSex:

"The nun's air of haughtiness and superiority rubbed Rowan the wrong way. He had seen firsthand what these monsters could do, and somehow this woman thought she was above it all; immune to the effects of every other village around her."
"A little further down the road, an idea popped into his mind, and Rowan knew precisely how to make Sister Gwen take the threat seriously."

ro "It's getting dark; we should set up camp for the night."
         
"Sister Gwen raised a brow and glanced back down the road."

sisgw "We are not that far off from the village. Surely we can reach it if we pick up the pace."
        
ro "I would rather not risk the journey. It should be nightfall by the time we arrive, and the road will be difficult to see in the dark. I would rather not risk getting lost."

sisgw "No doubt, you’re the expert. Very well. Allow us to rest for the night; I'm sure the demons can wait another night."

"She smirked at her own joke and helped Rowan set up camp, handling the meal prep while Rowan fetched wood and established a fire."
"When he was a little ways off from their campsite, one arm full of sticks and broken logs, Rowan spoke into his amulet."

ro "Jezera?"

show jezera neutral behind bg31

je "Yes? Is there a problem?"

"Although usually somewhat patient with him, Rowan briefly wondered if he had interrupted something. From the small moans he heard in the background, he was certain the answer was yes."

ro "I need you to send me an incubus. Tell him to go along with what I say."

je "An incubus? Really, Rowan, if you needed sex, I'm sure you could--"

ro "It's not for me, Jezera. Can you send him or not?"

je "Very well. It should take him a few hours to get to you from the portal. I'm curious about what you plan to do to him, though, so I'll have him relay everything when he returns."

"He didn't really care what Jezera did with the incubus afterwards, as long as he followed Rowan's lead."
"After a few hours, the sun dipped low over the horizon, basking the fields in twilight, and the fire was raging high. Rowan dumped the rest of the sticks and logs into the center while Sister Gwen served up some sandwiches she made in his absence."

ro "So, what made you decide to go into the convent, sister?"

sisgw "Oh, following the Goddess's words were always my calling. When I was a child, I-- A-Aaaahhh!!"

show incubus 2 neutral at edgeright with dissolve

"Sister Gwen let out a shriek as an incubus appeared beside the fire in a grand display of fog and smoke, as though he were stepping out of thin air. Rowan was careful not to look at the incubus, keeping his gaze focused on Sister Gwen."

ro "What is it, sister? Are you alright?"

"Rowan glanced back at the smirking incubus, then further across the plains around him, pretending to see nothing."

ro "What is it?"

"Sister Gwen gaped at him, just as quickly diverting her gaze back to the incubus standing proudly beside the fire. The incubus's hips swayed as he walked closer to the nun. She scooted away."

sisgw "Don't you see him?! You must! He's right there!"

"She thrust a hand out towards the incubus, who quickly snatched her palm and gave her finger a little suckle. She yanked her hand away and clutched it to her chest, her face blossoming in a bright red."
"Rowan tried not to laugh or even smile. It was no easy task, especially considering how flustered the nun was."

ro "I don't see anything, Sister. There's nothing there."

"The incubus' eyes sparkled as he picked up on Rowan's intentions. There was little keeping him clothed in the first place, but the demon removed the thin cloth wrapped around his waist, dropping it into a pile beside the campfire."

ro "What are you seeing, Sister?"

"Sister Gwen stammered out a response, desperately working to shield her eyes from the disrobing demon, but he was difficult to ignore."

sisgw "A-A-An… I-Incubus…"

"She could barely get the word out, the pallor of her skin turning an even brighter red as she caught a glimpse of the incubus removing his pants. Rowan looked in the same direction as her, toward the incubus, but played dubious."

ro "An incubus? I don't see anything, sister."

scene cg904 with fade
pause 2
scene cg905 with dissolve
pause 3
show rowan necklace neutral behind cg905

"The lustful demon wrapped a strong hand around his cock and pumped, earning another frightened squeak of the nun. She did not glance away this time, however; her gaze was frozen on the steady movements of the incubus as he pleasured himself right beside her."

sisgw "B-But it's right the--"

ro "Are you sure you see it? You aren't having… impure thoughts, are you, sister?"

"Rowan cocked his head to the side and looked at her politely, but inside he was laughing away, enjoying the sight of the nun squirming uncomfortably on the ground."
"This was what she deserved, after all, for insisting there was no danger here."

sisgw "N-No, of course not… Forgive me, I must have been mistaken."

"But she looked at the incubus deadon, her youthful curiosity getting the better of her as she watched the incubus dance around her, his cock growing with each flick of the wrist. His one visible eye roamed across her body, seeming to pierce through each layer of her dress."
"Something changed in the nun's expression, and Rowan saw her haughtiness subside into a natural desire as her eyes traced every sway of the demon's hips, the broad expanse of his chest, and the hard erection poking out from his crotch."
"It was likely she had never seen an exposed man before, and even more likely that she never felt the desire of one pressed against her body." 
"Rowan stood up, and while the incubus spy did not falter in his self pleasure, Sister Gwen jumped, certainly haven forgotten that the Hero of Karst was even there. She looked away in shame."

ro "Well, since you're so worried, I'll go make sure there are no demons in the area."

sisgw "W-What? No, you needn't do that…"

"She reached out to stop him, but her fingers paused in the air. Rowan could see she was afraid, but it was not what the incubus would do if she was left alone with him that scared her; it was what she might do."

ro "({i}Perhaps she shouldn't have such impure thoughts{/i}.)"

#ro smirk
"Rowan smirked."

"Oh, don't worry. I won't be gone long. I think it will give us both some peace of mind."

hide rowan with moveoutleft

"Ignoring her stammering objections, Rowan gave the nun a little wave and walked off into the woods."

scene cg906 with fade
pause 3
show incubus 2 behind cg906


"Just out of sight behind the forest foliage, Rowan leaned against the bark of a tree and watched with a mischievous gaze."

traz "Sister, huh? A little nun~ Now that's just too cute. My name is Trazear. Remember that when you're screaming with pleasure."

"He winked at her. Despite the sweetness in his tone, the incubus's voice was husky as he bent down to her eye level." 
"Rowan chuckled as the nun had trouble keeping eye contact with the incubus as he continued the steady movements on his cock. "

traz "Don't be so shy. Here, you can touch it."

"Sister Gwen let out a small gasp as the incubus took her hands and wrapped it around his cock. She sat still, her body unmoving."

sisgw "You're not real… Y-You're just a figment of my imagination…"

traz "Oh, then you must have a pretty dirty imagination."

"She flushed to the tips of her ears and looked away, but she did not remove her hands."

traz " Here~ It must be your first time. Let me help you."

"The incubus knelt down in front of her and placed his hands over hers, moving them up and down his shaft." 
"Sister Gwen tried to avert her gaze, but soon she could not resist her own curiosity and she stared in amazement as Trazear's cock twitched and throbbed beneath her palms. "
"Rowan had to bite back an audible laugh as he watched the nun's curiosity take hold of her. It was too easy for her to drop decorum and give in to her base instincts."
"After a few moments, the incubus released his hold on her hands and moved them to her thighs, pushing the fabric of her dress up as she worked on him by herself. She didn't even seem to notice him removing her dress, her focus solely on the smooth curve of his shaft."

traz "Is it what you thought it would be?"

sisgw "I-It… It's smooth."

traz "Why don't you taste it?"

"Sister Gwen lowered her head and timidly licked the slit of his tip. Trazear stroked her hair with one hand while the other pinched and pulled at her nipples, giving each one an equal amount of attention in turn."

traz "Oh, aren't you lovely."

scene cg907 with fade
pause 3
show incubus 2 behind cg907

"The compliment urged her on, and Sister Gwen opened her mouth, allowing the tip to move past her lips." 
"There was no doubt she was inexperienced, but Trazear was patient and allowed her to explore different techniques on his cock, thrusting deeper inside of her mouth with each pleasant touch until she was gagging."
"Trazear pulled out of her mouth, earning a disappointed whimper from the nun. He smirked down at her and nudged her down onto her back." 

scene cg908 with fade
pause 3
show incubus 2 behind cg908

"Rowan could see the embarrassment on her face as Trazear forced her legs apart and settled between her gaping thighs. "

traz "My oh my~ Is this all for me? What a {i}dirty{/i} little nun."

"Trazear ran a finger along her slit and pressed it into his mouth, licking the juices clean off. Her body shuddered, her hips involuntarily jerking toward him."

traz "Simply delightful."

"Wasting no more time, the incubus shoved himself fully into her at once, earning a pained cry from the nun."

traz "Oh right! You're a virgin. I should have taken that slowly, right?"

"Trazear thrusted in and out of her with a little more care, and with each movement, the pain inside of Sister Gwen seemed to ease into a needy pleasure instead."
"Rowan didn't expect Sister Gwen to know what to do, but it seemed Trazear was happy to take on a more dominant role as he fucked the nun's open cunt, each thrust and clench of her pussy pushing them close to the edge. "
"Sister Gwen dug her nails into the ground and hooked her legs around his waist as Trazear grabbed her breasts for leverage. Rowan grinned at the sight of her bouncing chest as Trazear rocked her body against the ground. "
"Her soft moans turned into cries, and she seemed no longer able to contain herself as he pounded into her body harder--"
"Harder--"
"Harder--"

sisgw "G-Goddess…!!"

show cg908 with sshake
show cg908 with sshake
scene cg909 with flash
pause 3

"Her back arched toward him as she met her climax, her body convulsing uncontrollably as Trazear continued to fuck her senseless."
"Amidst the moans of the nun's climax, Rowan heard Jezera's voice come through his amulet. He quickly stepped further into the wood so that the passionate couple would not overhear."

scene bg3 with fade
show jezera happy behind bg3
show rowan necklace neutral at midleft with dissolve

je "Well, that was quite the plan, Rowan! You should tell me next time you organize something like this; I'd love to be there and see it."

ro "It was more impromptu than a plan, but thanks for sending your spy over."

je "Oh, no trouble at all. He's already back, and he's brought that pleasant little girl for me to play with."

"She'd left already?"
"Now that he listened carefully, Rowan realized he could no longer hear the nun's cries of pleasure. He peeked through the foliage, surprised to see the two of them gone."
"Mistaking his silence, Jezera hurried to reassure him."

je "Don't worry, I didn't kidnap her; she agreed to come to the castle willingly. And let me tell you, we're having a {i}splendid{/i} time, aren't we, sister~?"

"Rowan could hear the nun's familiar cries of ecstasy through the amulet and chuckled to himself. Somehow, it was Jezera that won in the end."

return
