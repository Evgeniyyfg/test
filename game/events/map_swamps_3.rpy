init python:
    event('slithering_premonitions', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('caravanner_caught', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"', 'week > 4',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('snakebite_bad', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)

label slithering_premonitions:

scene bg32 with fade

"Rowan stepped carefully through the bogs. This was a dangerous path with all kinds of horrors that could be found. He kept his eyes open for swamp beasts and unusually sized rodents."
"His diligence would prove tiring but well rewarded."
"Near the shambling path that might have been inaccurately called a road, he heard the sound of a disturbance. With a hand on his sword hilt, he went to investigate."
"Rowan found what looked like a pair of female legs being dragged into the swamp. Whatever torso they were connected to had long since been sucked under the bog. Rowan braced himself. Should he try to help her?"
"The thought was banished when he saw three small tendrils rise above the bog’s surface. To an uninformed traveler they might not have seemed so threatening, but Rowan understood their implications. The woman in the bog was well beyond saving by now."
"After that Rowan put even more diligence into every step. Alone in the moss would be a terrible fate."

$ avatar.mp -= 1
return

##################################################################################################
##################################################################################################
##################################################################################################

label caravanner_caught:

scene bg32 with fade

"There was a wagon trapped in the muck ahead of Rowan. Although it certainly was no human's, this one belonged to a goblin caravanner like Cla-Min's group. Perhaps they'd gone through here to avoid the higher traffic roads?"
"The goblin family had a bad run through one of the many streams on this animal trail and now a pair of wheels were down to the axils in mud. Most of the family was trying desperately to lift the vehicle back out, while the children watched over their donkeys."
"Given that they were most often treated with mistrust by the humans of Rosaria, it was not surprising that Rowan was greeted with similar misgivings when he made his presence known."
"Immediately the patriarch confronted him and demanded that he mind his own business. The goblin leader only kept the barest trappings of decency in his speech."

#TODO - deception check - easy
#pass
"However, a shout of surprise from one of the other caravanners who'd recognized Rowan for who he was soon turned things around. These folks were well familiar with the sneaky hero Rowan and his tricks with deception."
"They didn't show quite the same open affection as Cla-Min did at their first meeting, but certainly saw the hero far more favourably now that they knew who he was."
"Also fortunately for them, Rowan was someone very familiar with the logistics of moving wagons through rough terrain from back during the war. He knew there was little chance of them freeing this thing on their own, their short stature didn't give them the leverage they needed."
"Instead of them continuing to push, pull, and lift fruitlessly, Rowan had them unpack their supplies while he looked for a suitably long and sturdy stick. Once he'd found what he needed, he used it to leverage the wagon bit by bit out of the muck while the family kept the wagon from sinking back down."
"Eventually the wheels were high enough that the donkey team could pull it out of the mud. Everyone was very relieved and thanked Rowan profusely for his help. They shared some stories and many were especially curious about his less savoury deeds."
"Rowan deflected these questions, but did tell them some of the goings on elsewhere in Rosaria. In return, they gave Rowan some information about the local area that would speed his exploration up some. The group didn't seem to know or really care about Cla-Min's caravan."
"They parted ways on very favourable terms."
$ avatar.mp += 4
$ add_exp(5)
return

#TODO - Fail
#"Rowan had experience with this sort of thing from back in the war.  He'd been the one who'd had to deal with moving wagons through rough terrain.
#"He knew the group's stature meant that they simply couldn't get the leverage they needed to free their wagon.  However, helping them out unwillingly wasn't exactly something that Rowan would be able to manage."
#"He did offer to give some help and even mentioned Cla-Min's name in the hopes it'd get him somewhere.  No such luck.  The patriarch was firm in his desire that Rowan leave the group alone and now all of them were carefully watching him."
#"Discouraged, Rowan simply observed that they would need to put some leverage and distance into freeing the wagon before heading on his way.  His suggestions were repaid with jeers, insults, and even a few thrown rocks from the children."
#take damage
#$ add_exp(5)
#return

##################################################################################################
##################################################################################################
##################################################################################################

label snakebite_bad:
    
scene bg32 with fade

"Rowan had set up camp in the least moggy place he could find and settled into as good of a sleep as he could. Camping in a bog was always unpleasant between the bugs and the fog, this was no exception."
"However, in the morning he got an especially unpleasant surprise when a sharp pain ran up his leg, jolting him awake. In an instant he had his sword out and scanning for foes and where the creatures from his dream were attacking from."
"After a moment's chance to focus, and remember he wasn't organizing a battle against walking trees, he spotted the creature that had been responsible for waking him. A bright red snake was slithering away from his camp and into the underbrush."
"He examined his wound and sure enough had two holes leaking blood on his shin. A grunt of irritation escaped his lips before he set to work cleaning the wound. At the same time he tried to remember what this particular snake's venom did."

$ temp_res = check_skill(8, 'survival')

if temp_res[0]:
    "There was an old rhyme that dad had taught him. 'Red without black was a lack'? A lack of what? Venom? It had been a very long time since he'd hunted with his parents."
    "Aside from the pain, there didn't seem to be other ill effects. Perhaps this one wasn't dangerous after all? Rowan made a mental note to refresh his memory on snakes at the first opportunity."
    #take minor wound
    $ add_exp(5)

else:
    "Try as he might, Rowan couldn't recall anything about snakes. It had been a very long time since he'd hunted with his parents and they'd surely have taught him about this."
    "He couldn't wait for the effects to present themselves, and cut his leg open with a knife in the hopes of getting some of the venom out."
    "It made the wound worse, but with no idea what he'd need to counteract whatever effect the beast's poison would have on him, if any, this was the lesser of two evils."
    #take moderate wound
    $ add_exp(5)
    
"Thankfully the only thing that he noted through the rest of the day was the pain from the wound itself. Nothing more than favouring his other leg came of it."

return


