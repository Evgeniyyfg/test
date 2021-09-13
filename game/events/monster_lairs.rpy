# events for various monster lairs (drider nests etc.)
init python:
    # Drider nest: No breeding pit
    event('drider_nest_no_breeding_pit', triggers='map_res_9', conditions=("castle.buildings['pit'].lvl < 1",), group='lair', priority=pr_map_res)
    # Drider nest: Have breeding pit
    event('drider_nest_with_breeding_pit', triggers='map_res_9', conditions=("castle.buildings['pit'].lvl >= 1",), group='lair', run_count=1, priority=pr_map_res)
    # Hunting Party
    event('hunting_party', triggers='map_res_9', group='lair', run_count=1, priority=pr_map_res)
    #The Spider’s Prey
    #requires breeding pits
    event('spider_s_prey', triggers='map_res_9', conditions=("castle.buildings['pit'].lvl >= 1",), group='lair', run_count=1, priority=pr_map_res)
    event('affectionate_driders', triggers='map_res_9', conditions=("castle.buildings['pit'].lvl >= 1",), group='lair', run_count=1, priority=pr_map_res)
    event('lucky_day_or_not', triggers='map_res_9', conditions=("castle.buildings['pit'].lvl >= 1",), group='lair', run_count=1, priority=pr_map_res)


label drider_nest_no_breeding_pit:
# No breeding pit
# If the player has no breeding pit, they cannot capture the resource site.

scene bg44 with fade

"Rowan had discovered a breeding nest for the fearsome drider, one of the most common monsters in Rosaria. However, he had no reason to approach any closer. All he'd be able to get here was drider eggs."
"Once a proper place to hold monsters was constructed at the castle, then he would be able to return here and use the nest to get stock for breeding driders to use in the twin's armies."
#End scene, do not mark the drider nest as explored, move back to previous space.
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

#############################################


label drider_nest_with_breeding_pit:
# Have breeding pit
# Capturing this resource increases drider recruitment by 0.5 each week.  Currently the breeding pits will be only able to have driders, so the pits should slowly fill up with driders once you capture a nest..
$ world.cur_map.resources[world.cur_map.pos].capture()

scene bg44 with fade

#Choose one of the following options at random, it may change the outcome slightly.
$ event_tmp['variant'] = dice(3)

#1 - no effect
if event_tmp['variant'] == 1:
    scene bg3 with fade

    "In a secluded part of the forest, Rowan discovered several massive cocoons of spider silk. He checked them more closely and discovered that they were filled with large eggs. Each was at least twice the size of his head!"
    "That could only mean one thing, this was a drider nest! Something had obviously drawn the creatures to lay their eggs here, and it was likely that they'd keep doing so if the nests were left undisturbed."
    "He sent a message to his masters and relayed the location of the site. This was then passed on to Draith who confirmed that this would be an excellent site to collect eggs from to use for drider stock. He'd start as soon as possible."

    # No effect, end event
    return

#2 - lose orcs.
elif event_tmp['variant'] == 2:
    scene bg3 with fade

    "After avoiding the adults who were hunting nearby, Rowan found a nest of drider eggs and reported both its location and how to avoid the potentially vengeful parents nearby."
    "Unfortunately, the orcs who were dispatched later to collect the eggs were much less proficient at avoiding the driders than the hero had been. Eventually a few of them proved capable of completing the task so that the rate of collection was not reduced."
    "There were, however, several casualties before this point."

    # Lose 3 orc soldiers, end event
    $ castle.buildings['barracks'].troops -= 3
    return

#3 - gain money.
else:
    scene bg3 with fade

    "After spending several hours following the signs of driders, Rowan was fortunate enough to locate their nest, nearby the desiccated remains of what had certainly been a meal for the parent."
    "He sent a message to his masters, detailing the location and confirming that this would be a suitable source of drider eggs to use in the breeding pits."
    "Then he rifled through the bones and scraps of clothing nearby to see if there was anything of value there. He found a pouch of coins, which he pocketed as a small bonus to himself for this find."

    # Gain 20 coins for Rowan's personal money, end event
    $ change_personal_gold(20)
    return


label hunting_party:
#Hunting Party
#can occur if Rowan does or does not have breeding pits

scene bg44 with fade

"As Rowan approached the nest, he was met by three heavily armoured men, carrying a burlap sack."

mhunter "Hail, sir Rowan. Came here to take care of the nest, did ye?"

"The man flashed him a grin and dropped the sack to the ground in front of him."

mhunter "‘Fraid you’re a bit late, me and the lads will be getting the reward for this job."

"Dead eyes looked out from the sack up at Rowan from the severed head of a female drider, and judging from the size of the bag, it wasn’t the only one in there."

mhunter "Hope you weren’t looking forward to getting a few yerself, we took care of ‘em all, even the little ones."

"Rowan looked around the nest and could see fragments of eggs scattered across the forest’s floor, he wouldn’t be taking anything back to the castle from this excursion."
"He exchanged pleasantries with the hunters for a while before they left with their bounty, already laughing about the ways in which they would spend the money coming their way."
"Rowan on the other hand, would be leaving this nest empty handed."

#Nest is explored, but no resource is gained
# TODO: probably mark nest as captured, but avoiding "on_capture" (or maybe it is better to remove nest from map)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label spider_s_prey:
#The Spider’s Prey
#requires breeding pits

scene bg44 with fade

"A man’s scream cut through the peaceful quiet of the forest. Running toward the sound of distress, Rowan saw the poor soul who had cried out for help."
"The man was trapped beneath a female drider, who had bound his upper body and lower legs with its webbing, ensuring that it was impossible for him to escape."
"Something sharp had torn away the lower half of the man’s clothing, and it now had pinned him down with its pedipalps as it positioned itself above him to milk him of his seed."
"If Rowan was going to help him, he’d have to act fast."

menu:
    "Get the drider’s attention.":
        $ released_fix_rollback()
        "Rowan yelled out at the creature, and it turned to look at him quizzically."
        "Drawing his sword from its sheath, he advanced toward the drider as it, sensing the harm the hero intended toward it, readied itself to strike."
        #combat check DC12
        if check_combat(12)[0]:
        #pass
            "The monster struck out at Rowan with its front legs, but the human brought his sword to bear, cutting deep into the drider’s flesh."
            "It roared in pain, and lunged forward to bite at Rowan with its mandibles, but the hero deftly stepped backwards to avoid it, and slashed downward at the creature’s exposed neck."
            "It wasn’t enough to sever the head, but it was certainly a mortal blow, and the drider collapsed, writhing in pain. While it was in its death throes, Rowan went to the man and cut him free of the webbing."
            "He was rather shocked but unharmed by the assault, and after thanking Rowan profusely for saving him, headed off in search of pants"
            "Now free of any prying eyes, he signalled the orcs to come and collect any eggs that may have been left behind."
            #gain 20xp, lose a little guilt
            $ add_exp(20)
            $ change_base_stat('g', -1)
        else:
        #fail
            "The creature lunged forward with its front legs as Rowan brought his sword up to block, barely pushing them wide enough to avoid piercing his chest."
            "Down came the drider’s jaw as it buried its mandibles into the hero’s shoulder. Gritting his teeth against the pain, he brought his sword up, driving it through the monster’s chest."
            "It slumped backwards under the weight of the mortal blow, writhing in pain. While it was in its death throes, Rowan went to the man and cut him free of the webbing."
            "He was rather shocked but unharmed by the assault, and after thanking Rowan profusely for saving him, headed off in search of pants."
            "Now free of any prying eyes, he signalled the orcs to come and collect any eggs that may have been left behind."
            #gain 10xp, lose a little guilt, gain one wound
            $ add_exp(10)
            $ change_base_stat('g', -1)
            $ take_damage(1)
    "Watch what happens.":
        $ released_fix_rollback()
        "Deciding it would be too risky to get involved, Rowan watched as the monster lowered itself onto the man’s cock."
        "It was clearly enjoying the act, toying with its prey and it rose and fell on top of him. The man, for his part, had stopped yelling for help and was grunting and groaning as the drider rode him."
        "It wasn’t too long before he was completely spent, and the creature got off him. Weaving more strands of webbing around him to further enforce his captivity, it dragged him off in the opposite direction, away from the hero, by its spinneret."
        "With the coast now clear, the human contacted the orcs to come and collect  any eggs that may have been left behind."
        #gain a little guilt
        $ change_base_stat('g', 1)

$ world.cur_map.resources[world.cur_map.pos].capture()
return


##########################################################################
##########################################################################
##########################################################################

label affectionate_driders:

scene bg44 with fade
show rowan necklace neutral behind bg44

"There were driders here alright, an awful lot of them for one place at that.  Rowan had seen at least a dozen of them moving over the ground and through the trees.  Two had been feasting on fresh kills."
"It was no wonder, prolific was hardly enough to describe the sheer amount of life that thrived in this particular neck of the woods.  It was a veritable cornucopia of game, many hunters could make a very good living here."
"Evidently the driders had moved in, taken the role of apex predator for the region, and were positively thriving.  That boded quite well for Bloodmeen once Rowan found the local nests."
"It was inevitable that he'd have a confrontation with at least one of the driders.  Only his skills as an outdoorsman had allowed him to avoid as many as he had."
"Now he was faced with a male that definitely knew he was here.  However, it wasn't with aggression that the spider man showed Rowan.  No, it was a very erect member and a smug saunter with which this creature approached.  It even mimed getting a blowjob."

ro "(Horny bastard.)"

"As Rowan drew his sword the drider elicited a chuckle, at least he thought those clicks were a chuckle.  The sight of metal alone wasn't going to be enough to dissuade this beast, though it still remained in its confident saunter, an overconfident saunter."
"Casually it pulled a long silk thread from under its body and looped it together, then flung it in Rowan's direction, which he easily avoided.  It seemed to shrug in response, then abruptly lept forwards.  However that too Rowan had seen coming and was able to avoid without difficulty."
"A flicker of surprise danced over the drider's face when it turned back around and it tried the same trick again.  This time however the veteran warrior used one of his best tricks for such large creatures to turn the beast's size against it."
"He stepped slightly to the side, bent his leg, leveraged his sword, and send the spider man into an unintended cartwheel.  It skidded over the grass and flipped over a large exposed root before finally getting those many feet back under its body."
"There was no mistaking the look of dismayed anger on the drider's face now.  Though it seemed that it wasn't going to be giving up this hunt just yet.  All traces of the previously casual flair were gone as it studied Rowan carefully."
"The two started circling one another and occasionally made probing attacks against the other's defenses.  The long legs gave the drider the advantage of reach, but even then it was it that showed first blood."
"Rowan feinted left, swept around right and left a long line of red over the beast's torso that it only barely managed to pull back from.  Then nearly took a leg off when he abruptly broke the pattern he'd been intentionally showing his opponent."
"It was a common tactic, one he'd used especially often when training students in swordsmanship.  The move had also put the drider hard on the defense, it was now being excessively cautious against further tricks."
"After a few more probes, Rowan noted to himself that the same tricks didn't seem to work twice on the drider.  It adapted fast to his attacks, covering previous openings better each time he was able to get close to doing more damage."
"A smile touched the beast's lips, but not one of confidence.  Suddenly another loop of web came out, which turned out to be a feint for a follow up attack that Rowan just barely managed to parry.  The creature hadn't done a feint before, was it learning from him?"
"It jumped back and the two returned to studying one another's movements.  There was definitely something different now.  Movements which were a little stuttered, like the beast was a student focusing too hard on his footwork."
"The man did a double take, was that a smile of genuine joy on the drider's face?"

menu:
    "Allow yourself to be distracted.":
        $ released_fix_rollback()
        $ affectionateDriderBJ = True
        jump affectionateDriderSex
        
    "This is no time to get distracted.":
        $ released_fix_rollback()
        $ affectionateDriderBJ = False
        ro "So, you think this is a game?  Well, time to teach you a lesson then."
        jump postAffectionateDriderSex
        
label affectionateDriderSex:

"That momentary distraction was all it took for Rowan to put his foot into one of the loops of webbing that the drider had thrown at him earlier.  It stuck to his boat, causing a stumble, then a tumble, and in a moment Rowan was well and truly trapped in one of the nearby webs."
"He tried to get free, but the drider was already on top of him.  A few quick movements and a few more applications of webbing made certain that fight was over."
"His captor heaved a large sigh, seemingly disappointed with how the fight had ended.  Nevertheless it ran its hands up and down the man's body as its inhuman member reemerged.  The touch was not harsh or forceful, but rather appreciative and showed no restraint in what it touched."
"As soon as the beast found Rowan's member, it paid special attention to that.  The creature fondled him until it got an erection to match its own, but made no effort to remove or free Rowan from his clothing."

#cg1
scene cg606 with fade
pause 3

"Instead it stepped up onto the webs, positioned its member in front of Rowan's face, and tried to jab it into the man's mouth!  He recoiled from the strange black cock, but no wasn't an answer the drider would take."
"One of its spider legs pushed painfully against his cheek, drawing a small trickle of blood.  With no way to fight back, Rowan obliged the creature and opened his mouth to accept its cock."
"The first thrust was not gentle, eliciting a gag on the sudden intrusion of the strange chitin covered thing when it went down his throat.  No chance was given to adjust or respond, as the beast simply used him for its own pleasure.  It paid no attention to its partner's comfort or needs."
"Instead the creature simply humped his face again and again, running those interlocking plates over his tongue over and over.  It had a somewhat dusty taste, mixed with dirt.  You certainly wouldn't want it in your mouth, but it wasn't revolting."
"This continued for nearly a minute, with the creature's movements steadily increasing in ferocity as Rowan tried to get what lungs of air he could between the beast's intrusions."
"Eventually it peaked and the man beast thrust his length all the way to the hilt again, forcing Rowan's head back so it could get down.  Rowan had no choice but to swallow the cum that went straight down his throat, then coughed and sputtered as it withdrew from him."

scene bg44 with fade
show rowan necklace neutral behind bg44

"Once Rowan recovered, he was surprised to see that the drider was still there, just looking at him with a strange restless expression on its face.  Abruptly it sliced apart the webs, freeing him."
"Then it scurred over to where Rowan had dropped his sword, picked it up, and almost forcibly put it into his hand!"

ro "What do you want now?"

"Obviously he didn't get a coherent answer.  What was given was a return to the beast's battle stance with that same joyful smile on its face."

ro "Fighting?"

"Taking his stance again, Rowan gritted his teeth in annoyance."

ro "This isn't a game.  Time to teach you a lesson."

label postAffectionateDriderSex:

"The drider charged, going for the feint tactic again. If it was going to copy him, that meant that it was unwittingly playing into Rowan's hands. Rowan had trained enough prospective swordsman that he could see what was coming a mile away."
"He didn't move, causing his opponent to hesitate at the lack of reaction.  That screwed up the charge, putting it out of place.  Rowan then swept his sword down in a wide arc, nearly cutting off both of the beast's front legs."
"It screeched in pain, reeling from the blow and dancing backwards.  Ichor dripped from its wounds and its expression had become one of fear.  Rowan brandished his sword for his own charge, but it seemed that the game was over."
"After staggering in place for a moment, the creature dipped its head in a sort of bow or admission of defeat before running away."

if affectionateDriderBJ == True:
    "After watching for a moment to see if it came back, Rowan stood up straight and wiped a trail of cum from his mouth."
    "That wasn't as bad as it could have gone.  He just wished the encounter hadn't left him so hard."

"Rowan kept his sword out until after he'd found the nest and left the driders' territory, but was thankfully not accausted again."

$ world.cur_map.resources[world.cur_map.pos].capture()
return

##########################################################################
##########################################################################
##########################################################################

label lucky_day_or_not:

scene bg44 with fade

"While he navigated the webstrune trees, Rowan was surprised to come upon the remains of a campsite."
"The fire was still smoldering, so they hadn't left that long ago.  However the fact that belongings were strewn about with signs of a struggle suggested it hadn't been a willing departure."
"Exactly who had been oblivious or insane enough to shelter so close to a drider nest?"
"Rowan quickened his pace into the woods.  There was a chance they'd still be alive."
"It turned out that was the case.  He'd been able to locate a small group of people helplessly strung up in the trees.  They had hoped to avoid what they felt were the lesser of two evils, between bandits and driders."
"Well, this was either their lucky day or an especially unlucky day, depending on how you looked at it.  After all, a hero had found them quickly enough after being captured by driders they were still alive.  On the other hand, that hero now was working for demons who took slaves."

menu:
    "Free the refugees.":
        $ released_fix_rollback()
        "Lucky day it was.  Rowan climbed up the tree and cut them down from their bindings."
        "They were very grateful for the help and were even more grateful for a quick primer on how to avoid being made a meal and toy by giant spider folk."
        "One was able to retrieve a small pouch of coins from the campsite that he passed to Rowan to repay his kindness.  A rare gift for altruism these days, but one that Rowan had no second thoughts against accepting."
        $ change_base_stat('c', -3)
        $ change_base_stat('g', -3)
        $ change_personal_gold(10)
        
    "Take them as slaves to Bloodmeen.":
        $ released_fix_rollback()
        "Things would soon be going from bad to worse for these people.  Their location was reported to Bloodmeen, and a group of orcs would soon come by to collect them along with the nearby eggs."
        "Their loss would be Bloodmeen's, and to a lesser extent Rowan's, gain."
        $ change_base_stat('g', 3)
        $ change_prisoners(3)

$ world.cur_map.resources[world.cur_map.pos].capture()
return                                                                                                                                                                                                                             
