# village trade events
init python:

    #They Offer Slaves Instead
    #should be uncommon (todo)
    event('village_trade_offer_slave_instead', triggers='village_trade',  conditions=['not cant_trade_with_villages'], run_count=1, group='village_trade', priority=pr_map_res)
    #Other Trader
    #should be uncommon (todo)
    event('village_trade_other_trader', triggers='village_trade',  conditions=['not cant_trade_with_villages'], run_count=1, group='village_trade', priority=pr_map_res)
    event('rural_stink', triggers='village_trade',  conditions=['not cant_trade_with_villages'], run_count=1, group='village_trade', priority=pr_map_res)


label village_trade_offer_slave_instead:
#They Offer Slaves Instead
#should be uncommon (todo)
scene bg1 with fade

"Rowan scouted the village and found it woefully in need of basics such as food. They had been hanging under the shadow of a famine for years now. It’s people were dressed in rags, and showed the signs of malnutrition in their hollowed cheekbones."
"When he mentioned to local traders his capacity to bring in shipments of essentials in return for village income their eyes lit up. But, there was a problem."
"A farming village without enough food to go around lacks the kind of money needed to afford food shipments."
"The local traders squeaked out promises to somehow pull together the money needed. A few hours later, Rowan discovered the plan they had constructed. A number of the villagers stood in shackles by the side of the road."
"They watched Rowan with weary pathetic eyes."
"The traders explained that when they had posed their lack of resources to the village, some of the men and women whose homesteads had been hit hardest by famine had elected to be sold to the traders in return for food."
"With their sacrifice, the village would both be able to afford more food and would be able to bring in more overall. Rowan scratched his chin."

menu:
    "Accept the Slaves as an Alternative Form of Payment.":
        $ released_fix_rollback()
        "Rowan looked down at the poor wretched souls. Surely if left here, they would die of starvation. Being kept as slaves in Bloodmeen was not a fate Rowan wished on anyone, but perhaps they would have a better life there."
        "And besides, he was too far gone now to quibble about bringing a few human slaves back with him. That was his life now."
        "Rowan signaled his agreement to the village traders, and had the slaves loaded up into his wagons, much as one would do with cattle. Their lips curled in gracious smiles, but their eyes were wide with fear of the unknown."
        "The village would have its food, and that was enough."
        #Reduced income. +prisoners. + guilt.
        # TODO: reduced income
        $ change_prisoners(5)
        $ change_base_stat('g', 2)
        return

    "Refuse to Accept the Sale of the Slaves.":
        $ released_fix_rollback()
        "Rowan looked on the scene with a sigh. These people were in desperate straits, certainly. But, without knowing who his demon masters were or the fates of these men and women, he could hardly take them back to Bloodmeen."
        "He tried not to think of the human prisoners already there because of his own actions."
        "So, with a heavy heart, he refused the offer of the slaves, and insisted that the only thing he would accept in payment was the village’s money. "
        "The traders sadly accepted this deal, exchanging glances at the villagers who had offered themselves as slaves."
        "One little girl grabbed a leg of his horse, beginning him to take her. She claimed that with her sale, her little brother could afford to eat."
        "Rowan simply brushed the girl aside without looking at her."
        #Reduced trade income.
        # TODO: reduced income
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label village_trade_other_trader:
#Other Trader
#should be uncommon (todo)
scene bg1 with fade

"With bright red orchards stretching out in neat rows, this village would make for a bountiful trade partner. However, when Rowan arrived at thes merchant house, he found the officials there skeptical."
"To them he was just another trader trying to suckle from the teat of their wealth. Rowan sat across the table from them, trying his hardest not to tell them that if they rejected his demands, Andras would come and kill them all."
"The cost of their intransigence could only be death."
"n the village square between meetings, Rowan looked out into the streets and found happiness. Small children running around, free from starvation or life without a home."
"Before the meeting started back up, another trader in town came to see Rowan. He was a mysterious man, armored from the world in fine silks."
"The merchant explained that he had heard about the negotiations in progress, and would be more than happy to join in on Rowan’s side. Strangely, he didn’t seem to be asked for any special deal of his own as a result."
"Whoever this man was, he must have motives for trying to help."

"Rowan shook the merchant’s hand. Whatever the man’s intentions and priorities, by helping Rowan establish his deal, he would be helping him on his mission and also saving the lives of the people of this town."
"Besides, the merchant hadn’t asked for anything in return. If he made demands later, Rowan could always stiff him."
"The two returned to the trade guild. Rowan’s new ally apparently knew the village merchants. In between drinks and jokes he steers them away from their hardline position."
"The deal Rowan got as a result was perhaps not as expansive as he might have liked, but it was still quite lucrative."
"Rowan asked the merchant why he had helped on the road out of town. The merchant have him a blood curdling smile. In front of Rowan’s eyes, small horns burst from the merchant’s head."
"The creature simply asked Rowan to extend his well wishes to Lady Jezera. Then, his forehead sucked the horns back in, not leaving a trace."
"The incubus rode away, another village to fleece already visible in the distance."
#Extra income from village.
$ castle.villages_income += 1
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label rural_stink:

scene bg1 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan sat across from the table, growing steadily more and more concerned as the Village chief ran through the potential trading supplies the village could offer." 
"Very little sounded like resources that Bloodmeen could actually benefit from."

if avatar.corruption < 31:
    "Rowan rocked uneasy in his seat. If he could not mark the village down as a trading partner, it’d be slated for a sacking. He had to make a trade compact with them."
    
elif avatar.corruption > 60:
    "Rowan’s eyebrows grew more narrow. If they were not useful as trading partners, they would be slated for a sack instead. Less then ideal, sine the war effort needed consistent tributaries to maintain its finances."

else:
    "Rowan sat uneasily. If he couldn’t mark the village as a trading partner, it’d be slated for a sacking. Not the first, or likely the last, time that would happen. But, something to avoid if at all possible."

ro "Allow me to go for a walk, and I will return with a new proposal."

vilch "Of course. We are eager for a proposal. Food shipments have been slow this year, and it is a worry our stock will dwindle."

"Rowan sat out around the village, inspecting it. The conditions were brutal and dirty. Far more so then Arthdale had ever been in his memory."
"Would the demons even want to sack this place? All they’d get would be substandard sheep."
"A village boy showed him around, pointing out locations. It was the same old haunts you’d get in any other small town. The matchmaker’s house, the supply shed, the village circle. He looked on the grazing areas and they were barren."
"But, fortune struck him, in an unusual form, on his way back to the Chief’s lodge."

ro "Wh-what is that smell? It’s atrocious?"

boy "Oh don’t mind that, no sir. Just the smelly rocks. When it’s all windy out, them smell goes down valley to the village. Been like that mah whole life."

ro "Smelly rocks? Show me."

scene bg31 with fade

"The boy led Rowan to the edgy of a mountain. The closer Rowan got, the more his nostrils was an assault by the pungent scent. He was driven by his suspicion. If this was what he thought it was, then it might solve the problem."
"When they reached the cliff side, he was proven right."

show rowan necklace neutral at midleft with dissolve

ro "Brimstone. "

boy "Hrmmm. What’s that?"

ro "It’s an important substance. Especially useful for incendiary properties."

"Rowan put a hand to his chin."

ro "Take me back to your chief. I have an idea."

$ castle.villages_income += 2
return