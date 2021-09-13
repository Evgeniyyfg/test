init python:
    
    event('nothing_safe_disease', triggers='private_winery_raid', run_count=1, group='map_res_private_winery', priority=pr_map_res)
    event('orc_frat_party', triggers='private_winery_raid', run_count=1, group='map_res_private_winery', priority=pr_map_res)
    event('rosarias_own_mendel', triggers='private_winery_raid', run_count=1, group='map_res_private_winery', priority=pr_map_res)
    

label nothing_safe_disease:
    
scene bg48 with fade

"A man walked between the vines, or rather what remained of them on the stakes and cages."
"The blight which had claimed the surrounding fields had spread to this place as well."
"In a sense, this was a blessing. Bloodmeen had little use for unfermented wine. The level of devastation meant that there were no workers needed here and only a single soul had stood watch over the treasure trove of alcohol from previous years still held here."
"Evidently grapevines were not immune to this flora plague. It made one wonder what, if anything, was?"
"A mystery that wasn't going to be solved by remaining here. It was time to move on."

$ change_morale(5)
return

######################################################################################
######################################################################################
######################################################################################

label orc_frat_party:

scene bg48 with fade

"Everything went off without a hitch. The workers were busy mashing the grapes when the orcs set upon them and didn't make it very far barefoot." 
"This was incredibly entertaining for Bloodmeen's soldiers, who set the 'dirty foots' back to stopping while they watched and sampled the cellar's stores. As they grew drunker, the orcs moved onto other activities, including joining in and tormenting the unfortunate humans."
"Keeping a semblance of order at this point was impossible, if it ever was when orcs were handling alcohol. Now it could only be called a party for troublemakers and teenage nobles."
"Rowan would have to stay the night before he sent anyone back. There was no way they'd keep their prisoners in this state."
"He swept his eyes over a pair of orcs that were cheering as another was drinking down as much wine as he could. Another group was laughing at one of the bleary worker's attempts to balance on one foot with an egg in his mouth. This was going to be a long night."
"Rowan sighed and grabbed a bottle of his own."

$ change_morale(9)
$ avatar.mp -= 2
$ change_prisoners(3)
return

######################################################################################
######################################################################################
######################################################################################

label rosarias_own_mendel:

scene bg48 with fade

"There was an unusually large and well-equipped guard at this winery. Rowan didn't like it, as valuable as the wine was, it wasn't something that a couple of knights in full armour stood watch over."
"By the time that the detachment he'd summoned from Bloodmeen arrived he'd worked out that there had to either be something odd going on or someone important was here. They had enough numbers to take these forces on, so he saw no reason to delay any longer."
"Rowan took advantage of the main attack as a diversion to let him slip into one of the side passages. A bundle of hastily assembled scrolls and books in the arms of a young noblewoman and a middle-aged priest awaited the hero on the other side of the door."
"The two cursed and fled down a staircase.  After giving a moment for his eyes to adjust to the darker interior, Rowan chased after them.  It wasn't that difficult a trail. There were scrolls and parchments scattered all along the cellar."
"The hero found them arguing over their fallen work. Now the priest was desperately imploring his lady to hurry along and leave the scrolls behind, while she insisted on saving their research."
"Loud crunching from above announced that the battle outside had been decided and orcs were now pouring into the structure. Rowan announced his presence and implored the two of them to give up. They still had a chance to save both their lives and their research."

if castle.researches['history_of_rosaria'].completed:
    "While he had no idea who the priest was, Rowan did recognize the woman's crest and called her by family name."
    #TO DO diplomacy test - 4
    #pass
    "His words seemed to have an affect on her, as she made known her surrender.  The priest was shocked at this, but also agreed to fall in line now that his lady had given up."
    "After giving clear orders that the two prisoners were not to be harmed, Rowan ordered the orcs to take them back to Bloodmeen along with the wine.  Perhaps Cliohna could make use of them."
    "This vine growing many vines that most of their research seemed to focus on was far beyond his understanding."
    $ castle.rp += 5
    $ change_morale(5)
    return
    
    #fail
    #pass

"While the woman froze up, the priest stepped in front of her and told her to flee.  Before Rowan could react, the holy man summoned the power of Solansia and sent a shockwave into the wall."
"The result was likely not what had been intended, as the whole section of dirt, wood, and bottles collapsed inward on top of the man!  Rowan was forced to flee lest a part of the wall fall on him as well."

#TO DO agility test - 3
#pass
"He retraced his steps, leaping past the collapsing walls and managing to keep his footing in the muck that formed after a wine bottle broke. Eventually finding his way up to the surface floor when the ground finally stopped shifting."
"With the immediate danger passed it was time to turn attention back to the matter of the girl. Obviously there was another way out of the cellar, so if she'd survived the priest's sacrifice she might very well be making her escape now."
"Rowan sent the orcs fanning out around the building to catch her. Luck was on his side, as they soon caught her trying to pile her scrolls onto a horse at a hidden exit. Her dedication to knowledge was admirable and Rowan hoped that Cliohna would find a use for her."
"This vine growing many vines that most of their research seemed to focus on was far beyond his understanding."
$ castle.rp += 5
$ change_morale(4)
return

#fail
#"He retraced his steps, leaping past the collapsing walls, but stepped into a pool of mud from one of the broken bottles. It sent him tumbling down and soon Rowan's legs were buried in dirt."
#"Thankfully the ground stopped shifting and the immediate danger passed. It took Rowan several minutes to free himself from the earth and the rough fall was something he'd be feeling in the morning."
#"By the time he'd returned to the upper floor, the noblewoman was long gone."
#"A shame, she and the priest might have been of use to Cliohna's research. This vine growing many vines that the few scrolls he'd recovered depicted was far beyond Rowan's understanding."
# gain minor wound
#$ change_morale(4)
#return