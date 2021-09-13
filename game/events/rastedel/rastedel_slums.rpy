
label rastAlleys:

if slumsIntroSeen == False:
    jump slumsIntro
    
else:
    jump slumsMenu


label slumsIntro:

scene bg45 with fade

"Rowan stood before the northern slums of Rastedel with the air of a man left simultaneously disgusted and in awe of its fetid grandeur."
"The slums were a madman’s jigsaw of winding streets, haphazard hovels and shuddering lean-tos, all mashed together against the northern walls like the heaped accumulation of Rastedel’s architectural offal." 
"It was humanity at its most inhumane: a civilization unto itself of congested urban living, with all the thrills and dangers that such a place could offer." 
"There was no urban planning to speak of: roads ran like snaking rain channels through the mud and refuse, merging and flowing out and into one another with little sense for traffic or coherence." 
"Precious few buildings could claim to have a shingled roof devoid of holes, or lacked a rotted wall thick with rats and other vermin." 
"For most, the entrance was a doorframe, gaping wide the inner goings on of the assorted brothels and gambling halls to the curious and the voyeuristic alike."
"Rowan peered into the first house he came across that didn’t look like a house of ill repute. It held little beside a handful of broken furniture, and lone mother of two."
"Her hand went for the knife the moment she noticed him, desperate to protect what little she had. Rowan shook his head and moved on, before she could do something they’d both regret." 
"Looking around, it was no wonder she took him for a bandit. Crime was rampant here, like a wasting disease it creeped through the very bloodstream of the slums." 
"Already, Rowan had witnessed no less than three robberies, a failed pickpocket attempt, and what he suspected to be a surreptitious gang beating." 
"The Slum-folk lived hard, and they lived desperate, their cruel existence made all the more brutal, more tragic, by the war. The dwellings along the outer walls were gone now. Burned by Werden. Their former occupants crowding the streets added to the misery."

if avatar.corruption < 31:
    "He watched three children run down with dirty feet. They were smiling. Did they know there was a war going on? How horrid their conditions were?"
    "Rowan had tried not to think of the plight of the slums much when he had last spent time in Rastedel. He had believed then that with the last war over, things would improve for the poor."
    "Could he even still pretend that the lords would help when this war was done?"
    
elif avatar.corruption > 60:
    "Not even the sun itself could bear to look upon the foul sight of the slums."
    "The light of day was a sickly grey companion in these streets; the numerous tarps and overhangs of the street merchants sapped what little illumination there was left to find. In short: it was a bleak, noxious, deadly shithole. "
    "And it was the perfect place for Rowan to find the kind of vicious wretches he was looking for... assuming he could flush them out of their nests."
    
else:
    "He watched three children run down with dirty feet. They were smiling. Did they know there was a war going on? How horrid the conditions they lived in were?"
    "How had he thought this was justice? Marianne’s predecessor had once told him that helping the urban poor would be a priority with Karnas defeated."
    "Lies. So many lies. "
    
show rowan hood neutral at center with dissolve

"He took a step aside, avoiding a hulking, drunk brute who made his way through the street, eagerly searching for a fight. His beady eyes turned to Rowan, but the hero had already blended with the crowd, unwilling to find trouble so soon." 
"No man would be stupid enough to pick a fight with the Hero of Karst. But thanks to the simple, threadbare cloak of faded brown, he just another outsider. Before, he had hoped to blend in - but now realized his folly."  
"There was a missing component in his clothing, in his figure, in his walk: hungry desperation. His cheeks were not hollowed, and his step lacked the nervous jerkiness he had seen in almost everybody here." 
"The locals would not trust him easily, of that he was certain. He’d have to use whatever tools he had at his disposal - gold being just one of them - to gather information on Maud. At the moment he didn’t even know how the damn woman looked." 
"He pulled his hood further down. No matter. He was no stranger to tracking a big game. Even if all that would be left for him is searching blindly, he’d find Maud and her people." 
"And the Northside Bannermen would be brought to heel."

$ slumsIntroSeen = True

##############################################################################################################################

label slumsMenu:
    
scene bg45 with fade
show rowan hood neutral at center with dissolve

menu:
    "The hunter becomes the prey." if slumsEvent1Seen == False and maudMet == False:
        $ released_fix_rollback()
        jump slumsEvent1
        
    "Beating around the ambush." if slumsEvent2Seen == False and maudMet == False:
        $ released_fix_rollback()
        jump slumsEvent2
        
    "The beggar." if slumsEvent3Seen == False and maudMet == False:
        $ released_fix_rollback()
        jump slumsEvent3
    
    "Red light, green light." if slumsEvent2Seen == True and slumsEvent4Seen == False and maudMet == False:
        $ released_fix_rollback()
        jump slumsEvent4
        
    "Meeting Maud." if slumsEvent3Seen == True and maudMet == False and northsideAlly != "alain":
        $ released_fix_rollback()
        jump meetMaud
        
    "Visit Maud again." if maudMet == True and maudEvent2Seen == False and northsideAlly != "alain":
        $ released_fix_rollback()
        jump maud_event2
        
    "Help Maud Meet the Baron" if maudEvent2Seen == True and maudEvent3Seen == False and northsideAlly != "alain" and act4BaronMeet == True and clubbingSealSeen == True:
        $ released_fix_rollback()
        jump maud_event3
        
    
    "Leave the slums.":
        $ released_fix_rollback()
        jump rastMenu
        


###############################################################################################################################

label slumsEvent1:

$ slumsEvent1Seen = True

"It was difficult to catch the gaze of anyone in the slums. A stranger approaching was always a sign of trouble, and people scurried away at the sight of him, his cloak doing little to inspire trust."

show rowan hood happy at center with dissolve

"But if there was one thing that made them stop in their tracks, then it was the quiet jingle of the gold coins Rowan held in his pouch. Promise of easy money made deaf men suddenly regain their hearing, and gave Rowan hopes for finding Maud quickly."

show rowan hood neutral at center with dissolve

"At least as long as nobody throws a wrench in his efforts. Gold did attract attention - but often the wrong kind."

show rowan hood neutral at midleft with moveoutleft

"A group of thugs perched upon the crumbling wood of the second-story balcony to his right. They were undoubtedly a part of the local muscle, judging from their only somewhat gaunt appearances, and the mean way they carried themselves."
"Many were missing teeth, or bore ugly scars of survival the way an animal of the jungle might. The only unifying feature any of them shared were the green scarves they tied around their waists or about their necks."

show rowan hood neutral at center with moveinright

"He felt their eyes upon him as he strode onwards, beneath their balcony and on through the thoroughfare. He pretended not to notice, keeping his senses alert to sudden changes in his environment." 
"A moment later, he spared a glance behind him. The balcony was now empty, and it didn’t take a life full of war to know why. Trouble... But perhaps the kind he could use to his advantage."

hide rowan with moveoutleft

"Turning ahead once more, he made his way through the crowd. A street vendor rushed towards him and tried to thrust a half-rotted fish into his hands."

if avatar.corruption < 61:
    "Rowan flipped him a coin and waved the man away. A small catch before his hunt for a much bigger one. A sign of good fortune for sure. "

else:
    "Rowan shoved out of the way. He had his sight on a much bigger fish now, and these people were already straining his patience. "


show rowan hood happy at center with moveinright

"Rowan looked behind again, sighting a flash of green fabric in the crowd. He suppressed a smile and continued onward, weaving between stalls and abandoned carts to confound and delay his pursuers."

hide rowan with moveoutleft

scene black with fade

"He looked one last time, spotting at least two within a dozen feet of him. He quickened his pace, keeping his hand the hilt of his sword, then -  ducked down the first side alley he could find."
"It was a half-tilted crack between a large whorehouse and what was once a grain silo that had sunk into the mud. The building leaned hard to one side, creating a slanted alley that was wider at the bottom and almost nonexistent at the top."
"It was just large enough for a few men to walk abreast through it."

#stealthcheck (to do)
$ res_roll = dice(6)
if res_roll > 3:
    "He pressed his back to the slanted wall, hidden deep within the shadows. The seasoned warrior drew his sword with a smooth, silent rasp of the blade. He held fast, calm like a pond in the stillness."
    "The first two thugs came through the alley with all the blundering aggression of men too-used to the glamour of their ability to intimidate." 
    "They had daggers in their hands, and looked ready to kill. Rowan let them rush past him, keeping silent till their backs were turned."
    menu:
        "Just keep one alive for questioning.":
            $ released_fix_rollback()
            $ slumThugsKilled = True            
            show black with sshake
            show black with redflash
            scene bg45 with fade
            show rowan hood angry at center with dissolve
            "Just as they passed him, Rowan stabbed his sword deep into the nearest man’s side, between the ribs."
            "The first sign the other thug had that things were amiss was the spurt of blood that gushed from his companions mouth as he crumpled to the ground, gurgling."
            show rowan hood angry at midleft with moveoutleft
            show bg45 with redflash
            "The second man, a worm-lipped little mongrel, let out a cry of surprise and backed up, finding himself boxed into the wall."
            "Rowan pulled his blade free from his compatriot’s body and slashed at his throat, blood fountaining out from the gaping wound as he stepped aside to avoid the spray."
            
        "Just knock them out." if avatar.corruption < 51:
            $ released_fix_rollback()
            $ slumThugsKilled = False
            scene bg45 with fade
            show rowan hood neutral at center with dissolve
            "The moment they passed him, Rowan reached out, snatching the nearest thug’s wrist and twisting the blade out his hands." 
            "The socket-eyed man let out a yelp of surprise, followed by a grunt of pain as Rowan smashed the pommel of his sword square in his face. He crumpled to the ground."
            show bg45 with sshake
            "The second man spun around, eyes going wide as he realized too late that his opponent was behind him."
            show rowan hood neutral at midleft with moveoutleft
            show bg45 with sshake
            "Seizing the initiative, Rowan rushed forward, slamming his shoulder into the worm-lipped ruffian and shoving him hard into the wall. The wall itself shuddered from the impact, and the thug slumped to the ground, dazed."
            $ change_base_stat('g', -3)
            
else:
    "Rowan tried to duck into the shadows of the alley, but he was too slow. There was a shout, and in a flash the men were upon him."
    show black with sshake
    scene bg45 with fade
    show rowan hood neutral at midleft with dissolve
    "Rowan turned and swept his blade in front of him, forcing the two thugs who had entered the alley to back off. The difference in reach played to his advantage, which would make smarter men think twice before engaging."
    show rowan hood angry at midleft with dissolve
    thug "Awful kind of place to be gettin’ lost, eh? Dun worry, we’ll show you out. Just gives us all the gold on ye."
    othug "And everything else o’ worth."
    "But his opponents were neither smart, nor particularly skilled. They held their daggers before them with the stiff frame of men who had never been trained to wield them." 
    "It was obvious they were used to robberies and street fights. They had no experience dueling a real swordsman."
    ro "I have a counterproposal. How about you two put your daggers down before you hurt yourself, answer some of my questions, and I’ll let you leave with your pride and limbs intact?"
    show rowan hood happy at midleft with dissolve
    ro "We’ll start with something simple. Who do you work for?"
    show rowan hood angry at midleft with dissolve
    "The two thugs looked at each other, cruel smiles gracing their lips. Sadly, Rowan could almost the cogs move inside their heads."
    "“It’s two on one, and our friends are just around the corner. Who does this idiot think he is to threaten {i}us{/i}?!”"  
    "Two swift strikes were Rowan’s answer, as the first thug feinted forward, while the other rushed him, trying to move past his guard and nullify the warrior’s superior reach."
    ro "If that’s how you wish to play it."
    show rowan hood neutral at edgeleft with moveoutleft
    show bg45 with redflash
    "Rowan danced back and slashed at the thug’s hand. The man screamed and dropped his blade, a deep gash furrowed into the top of his hand."
    menu:
        "Go for the kill.":
            $ released_fix_rollback()
            $ slumThugsKilled = True 
            show rowan hood neutral at center with moveinright
            show bg45 with redflash
            "Rowan finished the man off with a stab directly to his heart. The man gasped and clutched at the blade, collapsing to the ground as he bled out in the alleyway."
            show bg45 with sshake
            "Rowan planted his foot on his chest and pulled, managing with some difficulty to extricate his sword from his person."
            "A split of a second too late. The second thug let out a shout of anger and rushed him, swinging his dagger wildly in an attempt to overwhelm the hero."
            "Realizing he wouldn’t be able to raise his sword in time, Rowan opted for the safer option and dropped it, catching the worm-lipped man’s wrist as he tried to plunge the dagger into his chest."
            show rowan hood shock at center with dissolve
            "A brutal struggle ensued. Rowan caught an elbow to the face that made him momentarily see stars. However, his superior strength and skill won the day, and he managed to wrestle the dagger from his assailant’s hands."
            show rowan hood angry at center with dissolve
            show bg45 with redflash
            "He rewarded the ruffian’s murderous impulse with a dagger to the eye, shoving his lifeless body to the ground and retrieving his sword."
            #Add Damage (light, Face) TO DO
            
        "Just knock them out." if avatar.corruption < 51:
            $ released_fix_rollback()
            $ slumThugsKilled = False
            show rowan hood neutral at center with moveinright
            show bg45 with sshake
            "Rowan followed up on the attack and kicked the man in the chest, knocking the wind out of him. A quick elbow to the face made the man collapse altogether."
            show rowan hood neutral at midright with moveoutright
            "Rowan quickly seized the momentum rushing towards the second thug, whose narrow lips twisted in fear as he tried to back up."
            show rowan hood neutral at midright with dissolve
            "Unexpectedly, out what could only be suicidal desperation, the man leaped forward at the same time Rowan did."
            show rowan hood shock at center with moveinleft
            show bg45 with sshake
            show bg45 with redflash
            "The hero instinctively moved his blade away to avoid skewering the poor bastard, and took a dagger to the shoulder for his kindness."
            "Rowan grimaced and punched the man with his sword still clenched in his grasp, using the extra weight to add girth to the blow."
            show rowan hood angry at center with dissolve
            show bg45 with redflash
            "The thug’s nose crunched from the hit, and he went down, clutching at his face. Rowan yanked the dagger out with a grunt of pain."
            #add Damage (normal, piercing) TO DO
            $ change_base_stat('g', -3)
            
scene bg45 with fade
show rowan hood neutral at center with dissolve

"His first two opponents dispatched, Rowan turned to the front of the alley, where four more men were now standing, shocked at the speed at which he had dispatched their compatriots."
"Whether it was a form of suicidal bravery or some low, slum-borne sense of gangland honor, none of them fled. They advanced upon him, daggers and chains in their hands."

#combat check TODO:
$ res_roll = dice(6)
if res_roll > 3:
    show rowan hood neutral at edgeleft with moveoutleft
    "What followed was a short but brutal fight. Rowan backed up deeper into the alley, using its narrow confines to limit the ease with which his opponents had to encircle him." 
    "So long as he managed to keep them in front of him, he only ever had to fight two at a time."
    if slumThugsKilled == False:
        "It was a tricky business to simultaneously gain the upper hand and avoid unnecessary killing, but Rowan threaded that knife’s edge with seasoned skill." 
        "He was, in the end, facing malnourished vagabonds with more guts than tactical sense."
        "The first two newcomers he dispatched with ease, knocking aside their weapons and inflicting minor wounds to their hands, arms and legs."
        show rowan hood shock at center with moveinleft
        "The second two were trickier, and Rowan nearly lost his blade - and subsequently his life - to the clever grip of one ruffian’s chain when it wrapped around the hilt."
        show rowan hood neutral at center with dissolve
        "However, Rowan had seen this trick before, and managed to extricate the weapon from the trap without losing his grip on the process." 
        "From then on it was just a matter of whittling down their limited fount of stamina and goading them into a mistake."
        "In the end, six men lay injured and groaning, strewn about the alleyway in various states of distress. Rowan let out a soft sigh and walked up to the nearest one."
    else:
        "He readied his sword as the first pair advanced, and quickly went on the offense."
        show rowan hood neutral at center with moveinleft
        "He fought like a man possessed, parrying faltering strikes and responding in a blistering fashion, slashing and stabbing in the cramped confines, dispensing death to anyone foolish enough to challenge him."
        "The men in the front fell within moments, one with his head parted from his body, the other with his gut cut open, staring in shock at spilling innards."
        show rowan hood angry at center with dissolve
        "The second two were trickier, and Rowan nearly lost his blade - and subsequently his life - to the clever grip of one ruffian’s chain when it wrapped around the hilt."
        "However, Rowan had seen this trick before. Instead of resisting the thug’s insistent tug on his blade, he followed with it, stabbing the blade deep into the man’s chest."
        "He turned to face the last man, his dying friend’s body still twitching on his blade."
        "He half expected the man to turn around and run. And he tried just that. He took a step back, then tripped over, his knees giving up underneath him."
        ro "If you want to have any hope at coming out of this alive, don’t get up."
        "The dagger fell to the ground, and the ruffian scrambled to  his knees, his eyes quivering and his mouth babbling for mercies. Rowan approached him, the rush of killing still burning in his eyes."
        
else:
    show rowan hood neutral at edgeleft with moveoutleft
    "Rowan had not been quite ready to fight this many opponents at once. He tried to back up deeper into the alleyway to avoid getting overwhelmed, but his pursuers kept pace."
    show rowan hood shock at midleft with moveinleft
    "With a reckless tumble, one of the thugs managed to get around him, forcing Rowan to fight three of them at a time. What had started out as an ambush had quickly morphed into a very real fight for his life."
    if slumThugsKilled == False:
        "Rowan hadn’t meant it to end up like this. The fight was desperate, and soon he was on the defensive, parrying attacks as he used his quick footwork to avoid letting any one foe to get behind his guard."
        show rowan hood neutral at midleft with dissolve
        show bg45 with sshake
        show bg45 with redflash
        "He felt a dagger pierce the armor beneath his clothing, digging a shallow wound into his rib as he grunted in pain. His instincts kicked in, his sword slashing up to remove the hand of the offending party."
        "The man let out a piteous scream and staggered back, clutching at the bleeding stump."
        show bg45 with redflash
        "Without a moment of respite, Rowan moved to parry a knife thrust into his throat, and quickly followed with a deep stab into his opponent's shoulder blade." 
        "He managed to shove the man away just in time to avoid taking a set of chains to the face, though his sword was now tangled by the impediment."
        show bg45 with redflash
        "He managed to extricate the sword, but not before taking another shallow stab to the arm that he only just managed to avoid turning into a life-ending wound to the chest."
        "Out of options, and unable to prevent more bloodshed, Rowan turned and slashed at the man’s throat. Blood coated Rowan’s face as the man crumpled to the ground dead."
        show rowan hood neutral at center with moveinleft
        "One last man remained, the thug with the chains. Rowan turned his now bloodied sword to him, and the blood of his companion was enough to shatter what little remained of the man’s resolve."
        thug "Yield! I yield!"
        show rowan hood concerned at midleft with dissolve
        "The chain fell to the ground. Rowan spared a long, regretful glance in the direction of the dying man, then focused on the thug in front of him."
        #Add serious damage (Vital/Arm/Piercing) TO DO
        $ change_base_stat('g', 3)
    else:
        show rowan hood angry at midleft with dissolve
        "Rowan fought with a desperation bordering on fury. He lashed out at the thugs all around him with little heed to his own safety, batting aside their numerous attacks and dealing out death in turn."
        show bg45 with sshake
        show bg45 with redflash
        "He felt a dagger jab into his leg, digging a deep if superficial wound into his thigh. He snarled and slashed at the offending enemy, removing his arm up to the elbow as the man began to scream bloody murder."
        show bg45 with redflash
        "He quickly pressed the offensive, parrying a knife thrust at his throat and following with a strike on the next man’s neck."
        "A spray of blood coated his face and momentarily blinded him, allowing the man with the chains to entangle his sword and yank it out of his hands."
        thug "Get ‘im! "
        show rowan hood neutral at midleft with dissolve
        "The second thug threw himself at him, his dagger aimed right into Rowan’s belly. Rowan grabbed his arm, using his superior strength to lock his opponent in place."
        thug "Duck!"
        ro "Oh, no you don’t."
        "He saw the chain coming. A quick elbow to the chin stunned his opponent, and a simple push put him right in the path of the incoming strike."
        show bg45 with sshake
        show rowan hood happy at midleft with dissolve
        "A sickening {i}crack{/i} filled the alley and the man collapsed to the ground, his skull split open by the metal weight that ended the chain."
        "Rowan faced the last man, who gawked at him with his mouth wide open."
        ro "I need one of you alive. Want to be the lucky one, or will I have to check your companions to see who’s still breathing?"
        "The chain rattled as it fell to the ground. The poor bastard was shaking in fear, his hands up in the air.  Rowan walked up to him without hurry, and picked up his sword."
        #Add light damage (leg, piercing) TO DO
        show rowan hood neutral at center with moveinleft
        
show rowan hood angry at center with dissolve

ro "I don’t know who you think you are, but you and your friends made a big mistake trying to tail me."

thug "…P-please sir, mercy?"

ro "Speak! Who sent you?"
ro "No two-bit cutpurses would have bothered with a stunt like that, after seeing what I did to your two friends."

"Rowan could see the cringing fear in the man’s eyes. The thug set his narrow jaw and tried to say nothing, but his chin was quivering."

ro "Was it Maud? Are you working for her?"

thug "Y-yes! Yes, we work for Maud! A-and she’ll be really mad if you hurt me! I’m her right hand, I is! Yeah, yeah!"

"Rowan’s cheek twitched. He was in no mood for such brazen lies."

if slumThugsKilled == False:
    show rowan hood angry at midright with moveoutright
    "He stepped forward and brandished his blade against the thug’s neck."
    ro "You have ten seconds to start telling the truth, or I’m parting you from that lying tongue of yours. "

else:
    show rowan hood angry at midright with moveoutright
    "He stepped forward and brandished his blade against the Thug’s neck. The tip still glistened red with the blood of his defeated compatriots."
    ro "You have ten seconds to start telling the truth, or you’re joining your friends over there."
    
thug "Aaah!"

show rowan hood happy at midright with dissolve

thug "Okay! Okay!"

show rowan hood neutral at center with moveoutright

thug "We ain’t working for Maud, alright?! We- we’s nobodies!"
thug "Me an’ the lads was lookin’ to join up with Maud’s Boys. She’s the big bad bitch o’ dis place."        
thug "We figgured she’d be more liable towards lettin’ us join up if we showed we was good earners."
thug "But her Boys said we’re just common thugs. Said we’d never be part o’ the gang."

ro "And you decided to prove them wrong by robbing people? "

"Rowan brandished the blade against the babbling bandit’s chicken neck again. He let out a frightened sound, like a rat being stepped on."

ro "Not the smartest of the bunch, are you? "

thug "I’m s-sorry! We- We just eyeballed your fat purse and thought it’d be an easy snatch!"
thug "We didn’t know we was fightin’ a damn {i}demon{/i}!"

if avatar.corruption < 31:
    show rowan hood angry at center with dissolve 
    ro "-So if I {i}had{/i} been one of those ‘easy scores,’ what would have been my fate, huh?"
    ro "How many people have you and your friends killed, boy? People left out on the streets just like you, people trying to make whatever life they can in this place?"
    "The saucer-eyed fear in the thug’s eyes told Rowan everything he needed to know. A well of righteous fury filled his chest. It took everything he had to not cut the man’s throat and be done with it."
    
else:
    if serveChoice == 4:
        show rowan hood happy at center with dissolve 
        "Rowan smiled a crooked smile. With his eyes hidden under the hood, it was the only thing the thug could see - and it chilled him to the bone."
        ro "You have no comparison. But I will take the compliment."
    else:
        show rowan hood angry at center with dissolve 
        "He slapped the man with the hilt of his sword. A sharp edge split his brow, and the thug’s scream of pain was cut short by a blow to the stomach."
        ro "Don’t you dare call me that! You have no idea what a real demon is like. But I will gladly give you a taste if you want it so badly!"
        thug "No-o! I’m - ack- sorry! "
        
show rowan hood neutral at center with dissolve

ro "Give me something of use about Maud. {b}Now{/b}."

"He didn’t add “or else”. There was no need. He was certain the thug’s tiny mind had already provided the bastard with a plethora or possible outcomes for that very scenario."

thug "I-I- I- I-"
thug "Calhoun! ‘is name is Calhoun!"
thug "The guy I talked with - he’s got four fingers on his left hand. N-not cut or nuffin, like - like he was born with four! He’s a skinny fuck, always crackin’ jokes!"
thug "He’s Maud’s right hand! Calhoun’s the one who said we’d never get in!"

menu:
    "Knock him out.":
        $ released_fix_rollback()
        $ slumsInterrogatorKilled = False
        ro "Well done..."
        if avatar.corruption < 31:
            ro "Now, if you have anything rattling in that empty head of yours, I’d advise you to rethink your current way of life."
            ro "At least once the headache passes."
        "He cranked his arm back and hit the thug as hard as he could in the jaw. The man collapsed to the ground, knocked senseless by the blow. Rowan bent down for a moment to check that he was still breathing, then sheathed his blade."
        ro "‘...Calhoun.’"
        ro "As good a place to start as any, I suppose."
        hide rowan with moveoutright
        "His work finished, Rowan strode out of the alleyway, picking his way past the bodies strewn about with the carelessness of a man used to walking through a dozen battlefields."
        "He rejoined the main thoroughfare and disappeared into the crowd."

    "No loose ends.":
        $ released_fix_rollback()
        $ slumsInterrogatorKilled = True
        ro "Thank you for your honesty. May Solansia forgive you."
        thug "F-forgive me for w-"
        thug "{i}Uhhhh.{/i}"
        "Rowan’s blade slid across the thug’s throat with the ease of cutting turkey. His eyes went wide as the realization of what Rowan was doing hit home too late."
        "They stared into one another’s eyes as blood filled the man’s mouth. He coughed, spluttered, then gurgled."
        if slumThugsKilled == False:
            ro "It it’s any consolation, your companions will live."
        "Rowan stood to his feet, wiping the blood from his blade on the man’s shirt. He then sheathed his sword, checking to make sure the man was dead."
        ro "‘...Calhoun.’"
        ro "As good a place to start as any, I suppose."
        hide rowan with moveoutright
        "His work finished, Rowan strode out of the alleyway, picking his way past the bodies strewn about with the carelessness of a man used to walking through a dozen battlefields."
        "He rejoined the main thoroughfare and disappeared into the crowd."
        
$ maudClues += 1
$ knowCalhoun = True
$ calhounName = "Calhoun"
$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

##########################################################################################################################
##########################################################################################################################
##########################################################################################################################

label slumsEvent2:

$ slumsEvent2Seen = True

scene bg50 with fade

"Rowan moved like a ghost through the darkness, the way ahead lit only by the flickering torches of passers-by and the odd firelight coming through the yawning door frames of decrepit buildings." 
"Night turned the chaotic, dangerous network of the slums into a terrifying hedgemaze, near impossible to traverse. Here in these narrow spaces, daring to bear a light in the wrong place could be as dangerous as braving the dark alone."
"Rowan did not even bother trying to “find” his way in the crowded gloom. Instead, he followed the sound of raucous laughter and drunken revelry." 
"He reasoned that his best chance to find the elusive Northside Bannermen lay in identifying them amongst the assorted gambling halls and bordellos, alongside all the other debauched sinners."

show rowan hood neutral at center with dissolve

"His instincts led him to the slum equivalent of a red light district: a star-pointed five way junction between streets, where the evening crowds were thickest." 
"Rowan stood shoulder to shoulder with his fellow travelers as perfumed prostitutes dolled in presumptuous faux-finery propositioned the crowd from second-story windows." 
"He watched as the whores waved and cooed to him, fluttering small handkerchiefs and flashing their bare breasts, pale skin the color of milk in the low light as if to entice him."
"Their silhouettes were illuminated by the light emerging from the windows behind them, like bewitching sirens… or cavorting demons."

show rowan hood shock at center with dissolve

"The sound of a drunken brawl breaking out down the street drew Rowan’s attention away from the wayward women of the night, and he continued on through the thoroughfare."

show rowan hood neutral at center with dissolve
"He came to a wide, squat tavern of dubious construction. The gentle trills of lutes and lyres arose beneath the loud roar of humanity inside. "

show rowan hood neutral at edgeleft with moveoutleft

"In front of the door a crowd gathered: more than two dozen men and women - some lacking cloaks, or even shoes - watched two drunken sots as they wrestled like animals in the muck."
"The fight was hardly a fair contest. One man was nearly twice the size of the other: a hulking brute of balding complexion and a lazy eye, who dispensed a merciless beating to the groaning man on the ground, his fists striking flesh with a wet, sickening sound." 
"The onlookers watched in silence or jeered, forgetting for a moment their unfortunate surroundings by this distracting amusement."

show rowan hood concerned at edgeleft with dissolve

"In his younger, more idealistic days Rowan might have stepped in and put a stop to the beating."
"Such inclinations in the past had, after all, been what had spurred Rowan to action in the first place: a sense of justice, a notion of fairness, of seeing the small trampled by the mighty."

if avatar.corruption < 31:
    "Even now, he found his hand going to the sword by his side. He forced it to stop. He couldn’t blow his cover here. "
    show rowan hood neutral at edgeleft with dissolve

else:
    show rowan hood neutral at edgeleft with dissolve
    "...But those days had long since passed into memory. Now, Rowan simply watched."

"His unconscious foe dispensed with, the hulking brute wiped the stray spittle from his face and stood upright, glaring out across the crowd as if daring any other man to cross him. He met Rowan’s eyes for an instant, but made no sign that he noticed him." 
"Grunting, the man turned to a compatriot standing near to the crowd and gestured for his swordbelt. The man tossed it to him, shouting out an indecipherable jest his way."
"The brute made a crude gesture at him and strode away, a half dozen men from the crowd moving to follow." 
"Rowan’s eyes trailed across their persons as they moved in formation: these men were all armed, bearing swords and wearing crude armor of padded gambeson and cloth doublets." 
"It was as good a clue as any. A gathering of such men in the slums could only speak to coherent organization, and the gangs were the only ones capable of such collective force. City Guards and mercenaries knew better than to tread on their turf."

hide rowan with moveoutright

"Pulling his hood tighter over his head, Rowan gave the men a wide berth, then moved to pursue." 
"The party of men, led by their hulking brute of a commander, cut a path through the crowd,  headed with purpose towards some undetermined location. Rowan followed, keeping behind assorted bystanders but always staying in sight of them." 
"The men moved away from the thoroughfare, into a particularly dense part of the shantytown, where dwellings tended to look more like half-collapsed tents of trash than proper buildings." 
"The roads became animal trails, weaving between the walls of habitation like a dried creek bed, the twists and turns coming so quickly that Rowan worried how he would find his way back out again." 
"Now far away from the main street he had started from, the foot traffic died away. Soon Rowan was walking alone in the narrow confines, moving with slow, careful footsteps in the wake of the crowd of men." 
"The twists and turns of the alleys made it hard to keep track of them from afar, and he was forced to close the distance, peeking around corners to spy on the men as they continued onwards into the night."

#stealthcheck (to do)
$ res_roll = dice(6)
if res_roll > 3:
    "He kept to the shadows, darting between the streets with uncanny skill. Rowan had spent many, terrifying days in the Demon War behind enemy lines: tailing enemy forces was but one of his many tasks." 
    "At last, the men arrived at their destination. Their brute of a leader led them to a dimly lit warehouse with a large stone wall encircling the front courtyard. He rapped his fist upon the heavy oak door, glancing around as his men idled in the courtyard." 
    show rowan hood neutral at midleft with moveinleft
    "There was a long pause, and then the sound of a rusted lock being unlatched… and then another. And another. Finally the door swung wide, and a vague silhouette of a man appeared."
    man "Wot's your business?"
    brute "Shut your gob and let us in, Kesser. I’m one o’ the Boys, if ya kinnae tell."
    "Kesser looked at the man, then at his gaggle of friends outside. He shook his head with slow deliberate, turns."
    kesser "Nah. It don’ work that way, friend."
    kesser "Boy or no Boy, you don’ walk in here without showin’ your colors. ‘Specially when you bring your drinkin’ buddies along. You know Maud’s rules for outsiders."
    brute "They’re new recruits."
    kesser "They’re fuckin’ {i}scallywags{/i}, and I won’t have ‘em here. Not until Maud approves of ‘em."
    kesser "Git the gesture right, or fuck off."
    brute "You finna make me mad in front of my lads, Kesser? I’ll gut you in the street and leave you bleeding fo’ the dogs."
    kesser "Oh, you like sayin’ stupid things, ya know that?"
    kesser "I got five bows on the rafters pointin’ down at ye, ready to turn you and your troupe o’ curs into a tailor’s pincushion. Go on, gimme a reason to shut your mouthy cunt-lips for good."
    kesser "Take your stab, but know it’ll be the last {i}stupid fuckin’{/i} thing you do, you miserable wretch."
    kesser "Now tell them fools to fuck off, and gimmie the sign… if ya please."
    "Momentarily, Rowan thought the incident would descend into bloodshed. But this just was another power play. Evidently Kesser had the right of things, as the other man looked around and gestured towards his companions with his head."
    brute "Go on, clear off. We’ll pick this up in the morning."
    "The men filed out of the courtyard. Rowan held fast against the wall he was hiding behind, his eyes staring intently at the brute’s hands."
    show rowan hood happy at midleft with dissolve
    "He watched as the man lowered his open hand, his empty palm facing upwards. Then, he brought it to his chest, clenching it with force, as if trying to squeeze the life out of the air itself."
    show rowan hood neutral at midleft with dissolve
    "That seemed to please Kesser, who nodded and stepped aside, spreading his arm wide as if to welcome his former rival in."
    kesser "After you, ‘Boy.’"
    brute "You’re a rotter, Kesser."
    kesser "Aye, fuck yerself."
    "The door shut behind them with a loud {i}boom{/i}. Content that he had secured what he was looking for, Rowan carefully threaded his way back away from the building and into the night."
    hide rowan with moveoutleft
    scene black with fade
    "It would be several hours before he weaved his way out of the Slum’s hefty interior, but he did so knowing he had found a new avenue to pursue, and a means to get what he wanted."
    $ maudClues += 1
    $ knowHandsign = True
    $ released_fix_rollback()
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

else:
    show rowan hood shock at center with moveinleft
    "As Rowan continued, he noticed a sudden change in the way the men were moving. In a rush they broke off in all directions, heading down different pathways with a speed that implied flight or terror."
    "He froze for a moment, baffled by their unexpected change in pace. It took him a moment to recover himself and consider his options."
    show rowan hood neutral at center with dissolve
    "Such a potential lead was too good to pass up. The ugly balding leader was at that very moment hightailing it down the street with a speed that belied his bulky frame. Behind him followed Rowan."
    hide rowan with moveoutright
    "Rowan followed him for a half mile or more, moving ever deeper into the darkness as fewer and fewer torches lit the way."
    "Soon he was running in the dark, his path illuminated only by the stars above him as his eyes adjusted to the change."
    show rowan hood neutral at midleft with moveinleft
    "At last, Rowan came up short in front of an unusually wide, open thoroughfare. Despite its size, it was deserted, an open path empty of cover for the better part of thirty feet across." 
    "Something seemed off, even more so than before. He couldn’t see where the brute had gone."
    "His hunter’s eyes scanned the ramshackle buildings that surrounded the roadside. He caught the glint of metal in the dark, barely visible in the gloom. There was a feeling here, a low dread that gave Rowan pause."
    show rowan hood angry at midleft with dissolve
    "He did not want walk down that thoroughfare in search of the missing brute. To do so meant facing someone - possibly someones - lying in wait for him."
    hide rowan with moveoutleft
    "With severe reluctance, Rowan pivoted on his heel and retreated back the way he came, making sure to hurry down different corridors than the one’s he’d went down, on the off chance they had attempted to cut off his escape."
    scene black with fade
    "It took several hours of frustrating backpedaling, but Rowan finally found his way back out again, exhausted from the chase and no closer to his quarry than when he’d set out that night."
    $ released_fix_rollback()
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return


#######################################################################################################
#######################################################################################################
#######################################################################################################

label slumsEvent3:

$ slumsEvent3Seen = True

scene bg45 with fade
show rowan hood neutral at center with dissolve

"Beggar’s Row. A long, winding road running through the heart of the Slums like a knotted artery through a heart valve." 
"It was an unusually wide thoroughfare, named so due to the sheer concentration of the Slum’s most unfortunate denizens that packed its edges." 
"There were so many beggars, bums and ragged orphans strewn about that it looked like nothing so much as a glutted, muddy riverbed clogged with flotsam from a storm."

show rowan hood concerned at center with dissolve

"The beggars reached out to him as he passed, their hollow-eyed stares leaving a helpless feeling in Rowan’s gut. During the last war he had seen more than his fair share of refugees and orphans, and had done what he could to alleviate their pain."

show rowan hood neutral at center with dissolve

"But whether he liked the sight of it or not, Rowan was on a quest. These thin-framed and disease-ridden ghosts might be the bottom rung of the Slum’s society, but they were also its eyes and ears." 
"Without gold, without a trade, and without strength, to survive these people sold the one currency they had: gossip, rumors, tales of what they’d seen and what they’d overheard."
"They were the roots of the rumor grapevine: unseen, unnoticed, but nevertheless essential for their propagation and proliferation. For a few scant coins for a meal, Rowan could buy information that was likely priceless elsewhere."
"So down the long, depressing row he walked. He noticed that the passers-by moved at a much faster clip than in other parts of the Slums. Whether that was from a fear of pickpocketing, or simply disgust at the odious scent in the air was an open matter." 
"Deciding that keeping his cover meant necessarily keeping to custom, Rowan did not linger as he moved through the thoroughfare." 
"His eyes were sharp to the potential of one of the multitudes of desperate folk - men, women, young and old - who might have useful news for him regarding the elusive Maud."
"He came to a clog in the artery: the Beggar’s Row narrowed for a stretch, allowing only one man to walk abreast through the ever-shortening streets."
"Panhandlers were packed so tightly together that Rowan found himself almost tripping over the prone bodies and extended legs of those who sat against the walls." 
"It became less a road and more a glorified alley, the sun darkening as the buildings around shielded them from its glare."

beggar "Oi you piss soaked bitch! You fink I as’ed fer yer help?!"

"Rowan’s gaze was drawn upwards, towards a particular beggar lying in a heap on the street." 
"The long-faced and half-blind beggar was clearly in some distress: his ragged clothes were soaked in blood, and he clutched at his stomach with a sharp grimace of pain." 
"Some kind-hearted nun passing by had bent down to try to aid him, but the man would have none of it."

beggar "If ya can’t tell, I need a {i}coffin{/i} not yer coin. "
beggar "Better yet: dangle me bones on strings and use my rottin’ corpse fer a puppet instead, aye? It’s what yer shinin’ cunt of a Goddess would want, anyway."

"The well-meaning nun tried to offer him a gold piece, but the Beggar slapped her hand away."

beggar "{i}Did I fuckin’ stutter{/i}? Piss off! Leave me be! If I din’t wish to be pecked to death by crows, I’d tell ye!"
beggar "Or maybe I’ll just shout into that narrow space ‘tween yer ears and make an echo out o’ it, aye?"

"Dejected, the nun whispered a prayer to the man and bowed his head, turning back up the thoroughfare. The Beggar made a rude gesture towards her back as she walked away, then collapsed onto his back, clutching at his wound."

beggar "F-fuckin’ Solansians. Can't even let a man bleed to death in his own damn street."

"Rowan glanced around, taking care to notice the way the other beggars pointedly ignored this man, despite his grievous wounds. To his surprise, they weren’t even trying to relieve him of whatever meager possessions he might have." 
"He either held their respect - or their fear. And as far as leads were concerned this one was as promising as any. Rowan turned his steps to him."

beggar "Oh fer {i}Kharos’ clingin’ nutsack{/i}, what now? Why couldn’t Beric have just cut my throat and be done with it?"
beggar "Leastways then I wouldn’t have to put up with this {i}perpetual{/i} fuckin’ pesterin’!"

ro "You seem to be in some distress, old man."

beggar "Yeah, eyes of a fuckin’ hawk, this one."

show rowan hood angry at center with dissolve

beggar "D’you mind? Tryin’ to turn into a carcass on the street here with the mildest o’ decency."

"Rowan hunched down on his knees, examining the man’s wound. The beggar let out a huff of anger, but did not try to stop him."

show rowan hood neutral at center with dissolve

"He’d been stabbed in the gut, deep enough that a slow death was his only recourse if he did not seek some sort of healing. The width of the cut indicated something small, likely a knife wound."

ro "I can help you, old man."

beggar "Oh great, another twat wants to make a charity case out o’ me! "

"The beggar tried to push up on his elbows but let out a short gasp of pain. He scowled at Rowan. The hero would have commended him on his stubbornness, if it wasn’t killing him as effectively as the wound in his gut."

show rowan hood angry at center with dissolve

ro "If that’s what you’re concerned with, then you can repay me in information."

show rowan hood neutral at center with dissolve

ro "I’m looking for a woman named Maud."

"The beggar paused, his eyes coloring with some indecipherable thought as he took stock of Rowan for the first time. His lip curled into a sneer and he mimed flicking him away like an annoying bug."

beggar "You want a woman, you should try a whorehouse. Shoo. Shoo! Off with you!"

menu:

    #if Wilderness Survival is high enough - TO DO
    "Treat his wounds.":
        $ released_fix_rollback()
        "The wound was deep, but not impossibly so. Not the worst, compared to some he’d seen on the battlefield, but nonetheless lethal unless the man received immediate help."
        "He resolved himself to the task, leaning down to properly deal with the wound."
        "He felt the Beggar’s hands go about his wrists as Rowan reached for his injury, his stomach contracting as if to spasm away from the warrior’s touch."
        beggar "Didn’t ya hear me, you thrice-damned lecher? {i}Fuck. Off{/i}!"
        show rowan hood angry at center with dissolve
        ro "Would you rather I save your life or preserve your dignity, old man?"
        beggar "I’d rather you leave me be."
        "Rowan stared hard into the old man’s eyes. He could see the animalistic fear lurking behind his caustic bravado. He’d seen it countless times before."
        show rowan hood neutral at center with dissolve
        ro "If you want to curse me, be my guest. But I’m not going to stop just because you’re rude."
        "He reached under his robe, and laid out the first aid tools he carried with him on his travels. It was a good thing he’d thought to take them with him to the slums."
        ro "No one deserves to die like this."
        "The old beggar glanced away, letting out a harumph of air as he settled back against the ground. He let Rowan work, taking care not to look as Rowan cleaned, stitched, dressed, and then bandaged the wound." 
        "To his credit, the beggar made only the occasional light grunt of pain as Rowan worked on the injury. He had a remarkable pain tolerance if nothing else."
        #rowan hood happy
        ro "… And that should do the trick." 
        jump beggarHelpProvided
        
    "Find a doctor to help him.":
        $ released_fix_rollback()
        "The wound was deep, but not impossibly so. Not the worst, compared to some Rowan had seen on the battlefield, but very obviously lethal unless the man received immediate help."
        "Help he himself could not provide."
        ro "Stay here for now, old man. I’ll find you a doctor."
        beggar "Oh, I’ll make sure to tarry a while longer. Tell the crows to wait till I’m dead first to pick my bones, aye?"
        "Rowan brushed off the dying man’s insults and turned away. He walked back up Beggars Row, retracing his steps in search of a small sign he had seen in passing before."
        "Finally, he found it: a shoddily drawn Solansian symbol of healing painted on the front door of a dingy lean-to. A street “healer”, if one was being generous with the term."
        "Not his first pick, but the dying beggar already displayed a distaste for clergy, leaving him with little choice on the matter. He pushed the door open."
        doctor "Greetings sir! {i}Hell{/i}-o sir! how do you do, sir?"
        "Rowan could already tell he did not like the man. His face was mousey, his beady eyes black and filled with avarice."
        ro "A beggar outside needs your help."
        doctor "Ah, if only I were a man of charity sir. {i}Many{/i} beggars need help, but few can afford the kind of quality aid I offer!"
        doctor "Dr. Yaldras at your service! I’m the finest Bonesetter south of the Yael River."
        doctor "If you need a knee or an elbow set, a wound stitched, or - {i}ahem{/i}, “inconvenient materials” disposed of, there you have come to the right place!"
        doctor "A fair warning though, my good sir: my premium services don’t come cheap."
        show rowan hood angry at center with dissolve
        "Rowan was not surprised in the least. No self-respecting doctor would work in these conditions. But he was out of timely options."
        "He fingered his bag of coin, watching as the Doctor’s ears pricked up at their metallic jingle. The universal language."
        ro "The beggar outside has been wounded in the gut with a knife."
        doctor "Oh dear, oh dear."
        "There was no pity in the man’s eyes. He had the kind of soulless expression that a shark would wear when closing on its prey."
        doctor "Well, I suppose I could help him. Does forty gold pieces sound reasonable?"
        show rowan hood shock at center with dissolve
        "Rowan nearly choked on the amount. Forty gold pieces? That was enough to buy a small wagon."
        ro "Are you {i}joking{/i}?"
        doctor "Not in the least, good sir. I did say I was the best Bonesetter south of the Yael, no?"
        doctor "My lifesaving services don’t come cheap. And if the price is too high… Perhaps a priestess from the Cathedral would be willing to help? Maybe one of those Selestine Nuns?"
        show rowan hood angry at center with dissolve
        "He’d never make it, and the Doctor’s oily smile told him that the shifty codger had guessed as much."
        
        menu:
            "Intimidate him.":
                $ released_fix_rollback()
                $ doctorThreatened = True
                "Rowan swept aside one corner of his cloak, revealing the hilt of his sword. He put his palm upon the pommel, his brow pulling down into a scowl."
                ro "Pick a fairer price."
                "The Doctor remained unfazed."
                doctor "Sir, perhaps you are unused to the vagaries of the Slums. You are not the first man to walk into my office with a blade in your hand."
                doctor "Then allow me to provide you with some consultation, free of charge:"
                doctor "I, and every other doctor in the area are under the protection of none other than Sir Edgar Gaugmont, a Northside Knight of a particularly nasty reputation."
                doctor "Even as we speak, eyes are watching us, ensuring no harm comes to me."
                doctor "So please, consider your next steps carefully."
                "Rowan almost groaned. Another Northside Bannerman? He-"
                show rowan hood neutral at center with dissolve
                "No, it didn’t matter. He couldn’t waste his time running around trying to untangle the teeming web of politics that infested the slums."
                ro "And exactly how many pairs of eyes are watching us, doctor? One? Two?"
                show rowan hood angry at center with dissolve
                ro "Are they really going to step in once I move towards more… physical arguments?"
                #brawn check [hard] (to do)
                $ res_roll = dice(6)
                if res_roll > 4:
                    "The doctor’s lips grew thin. His eyes flicked down to stare at Rowan’s weapon, then back up to Rowan. He took careful note of what little of his body the cloak revealed."
                    doctor "You certainly look like a man capable of dramatically increasing demand for my services."
                    "A wide smile blossomed on the doctor’s face. It reminded Rowan of Cla-Min."
                    doctor "As that is the case, I’ll consider staying on your good side an investment for the future."
                    doctor "I ask only for a customary gold coin. As per our agreement with the Church of Solansia, we are forbidden from providing charity. Surely you understand."
                    "Rowan shook his head then tossed the man his coin."
                    ro "Fine. Here. Now bring your tools, I don’t think we can move him."
                    doctor "At once, Sir!"
                    jump doctorIntervention
                else:
                    "The doctor’s lips grew thin. His eyes flicked down to stare at Rowan’s weapon, then back up to Rowan. He took careful note of what little of his body the cloak revealed."
                    doctor "I believe so, yes. And even if they fail to stop you… In the best-case scenario, I’ll escape amidst chaos."
                    doctor "In the worst-case scenario, I’ll likely be dead, meaning I will be unable to provide the kind of medical assistance you came here for."
                    if castle.treasury < 40:
                        $ WoundedSlumsDoctor = True
                        doctor "My advice, good sir? Just-"
                        show bg45 with sshake
                        "His face connected with a nearby table before he could finish the sentence, and a sickening *crack* resounded in the room."
                        if avatar.corruption < 50:
                            "Consequences be damned, lives were on the line here!"
                        ro "In the worst case scenario, I break your legs, deal with whomever storms the place, then drag you with me."
                        ro "So would you like to rethink your position here?"
                        "The injured doctor raised a finger up, asking Rowan to wait. He placed his other hand on his nose, and with a short yelp, set it back in place."
                        doctor "After careful consideration, since a life in indeed in danger, I will offer you my services after all, and almost free of charge!"
                        doctor "I ask only for a customary gold coin. As per our agreement with the Church of Solansia, we are forbidden from providing charity. Surely you understand."
                        "Rowan shook his head then tossed the man his coin."
                        ro "Fine. Here. Now bring your tools, I don’t think we can move him."
                        doctor "At once, Sir!"
                        jump doctorIntervention
                    
                    else:
                        doctor "My advice, good sir? Just pay the price, and let’s have all this nasty business behind us."
                        ro "(Bastard….)"
                        jump payUp
                    
            "Pay up." if castle.treasury > 39:
                $ released_fix_rollback()
                label payUp:
                $ change_treasury(-40)
                ro "Fine. Here."
                doctor "A pleasure, sir. Let me get my implements. Can you bring the vagrant in question here?"
                ro "I wouldn’t risk it. He’s in a bad enough way as it is."
                doctor "Ah, an outcall. Normally I’d charge more for that…"
                "The dangerous look on Rowan’s face gave the Doctor pause."
                doctor "-But for {i}you{/i} sir, I shall make an exception!"
                jump doctorIntervention
                    
label doctorIntervention:

"Rowan led the illicit Doctor back to the Beggar on the street. The wounded wretch looked surprised that Rowan had actually bothered to return."
"His eyes widened to dinner plates when he laid eyes on the Doctor."

show rowan hood neutral at center with dissolve

ro "I’m back old man, like I promised."

beggar "You get that corpse merchant out of here, you hear me? "
beggar "{i}I’m not going on the cart!{/i}"

doctor "I take umbrage at the very implication, sir! This fine gentleman has convinced me to help you."

"Rowan put a hand upon the panicking Beggars shoulder."

show rowan hood happy at center with dissolve

ro "Easy old man, he’s here to staunch the bleeding."

doctor "Yes, and I have plenty more patients to see this afternoon, so if you could please pull aside your... rags?"

"The Beggar hesitated, but Rowan’s firm nod and soft expression made him relax back down on the ground."

beggar "Solansia preserve me."

doctor "Hopefully it won’t come to that. Now hold still."

"The old beggar glanced away, letting out a harumph of air as he settled back against the ground. He let the Doctor work, taking care not to look as he cleaned, stitched, dressed, and then bandaged the wound." 
"To his credit, the beggar made only the occasional light grunt of pain as the Doctor worked on the injury. He had a remarkable pain tolerance, if nothing else."

doctor "And… done! Another task completed, another satisfied patient."

"The Doctor picked up his implements and stuffed them into his satchel, sparing a last glance over his shoulder at Rowan."

show rowan hood angry at center with dissolve

doctor "I take my leave of you, sir. Best of luck with… Whatever it is that’s going on here."

label beggarHelpProvided:

show rowan hood neutral at center with dissolve

"Eyeing the badged wound dubiously, the beggar tried to lift himself up. He managed a full centimeter, before groaning in pain and dropping down on the ground.  "

beggar "Great. Now I can starve to death in the streets, instead."

if avatar.corruption < 31:
    "Halfway through his griping, Rowan stood up and looked around, seeking someone who’d be willing to take care of the man for a few coins."
    ro "Give me a moment. I’ll think of something."
    "Before he could walk off, he felt the beggar’s hands tugging at his cloak. The old man held him firmly, baring his teeth in annoyance."
    beggar "No. No, you… you did enough."
    beggar "A favour for a favour."
    beggar "I’ll tell you what you want to know about Maud, even if I dunno much... Just don’t let on that I’m talking, aye?"
    beggar "What do you want to know?"
    beggar "Whatever you can tell me about her and the Northside Bannermen."
    "The Beggar stroked his scraggly grey beard."
    beggar "Not much to tell; they’re a shifty bunch. They’re split between several gangs, each led by a so-called ‘Knight,’ the vain cunts. But you probably already know that. Maud and Madame Montiel are the biggest fish. "
    beggar "Maud’s not hard to recognize, but good luck spottin’ her most days, she’s not the public type. She dyed her hair green recently. No clue why. She’s daft, if you ask me."
    $ maudLook = True
    jump beggarEnd
    
else:
    ro "I see you’re still quite determined to die, old man. "
    "The beggar glared at him, but quickly stopped once he noticed the cold, indifferent look on Rowan’s face."
    ro "At first I thought you were just being stubborn, or maybe you adhered to some bizarre beggar’s code of honor that made you refuse help from outsiders."
    show rowan hood angry at center with dissolve
    ro "But now I realize you just wanted me and the nun gone, so you could wallow in your self-pity."
    "Fury sparked in the man’s eyes. He clutched his bandaged wound, though his other hand trembled, eager to part Rowan with his front teeth."
    beggar "You got some balls saying that ‘ere, lad."
    ro "Please. I can’t walk ten feet in this cesspool without tripping over a sob story."
    ro "You still have all your limbs intact and you’re not spewing your guts on the street anymore. You’re luckier than most."
    show rowan hood neutral at center with dissolve
    ro "So if you’re done feeling sorry for yourself, you owe me information."
    beggar "...Are you sure it’s Maud you’re looking for?"
    beggar "Other Northside Knights might be more to your liking. Some of whom I think would play more to your thuggish type."
    ro "It’s Maud I’m interested in. But I’ll take whatever else you can tell me."
    beggar "Fine. But afterward, I want you out of my sight."
    beggar "The Northside Bannermen are split between several groups, each led by a Knight, but you probably already know that. Maud and Madame Montiel are the most influential of the bunch."
    beggar "Never seen either of ‘em myself. Couldn’t give you a description, even if I wanted to. People who know what they look like don’t tattle."
    jump beggarEnd

label beggarEnd:

ro "Does she have a headquarters? Some kind of home base?"

"The Beggar burst into laughter, then started wheezing, his face twisted in pain. It took a few moments till he could speak again. "

beggar "You’d think so. But if she’s got one, I never heard of it. They say she’s a girl of the streets. Grew up livin’ from place to place."
beggar "They say she stays with her Boys, or with people she helped in the past. But mostly, she keeps to her home turf."

ro "Where’s that?"

"The Beggar didn’t have a clear answer for that either, but he did give Rowan a set of general directions. Roughly speaking, it narrowed down Rowan’s search to a mere fraction of the slums area."

ro "Any chance you could tell me how to get in touch with them, or with Maud?"

beggar "Sorry stranger, but I dunno. In the end, I’m just a wretch on the street."

if avatar.corruption < 31:
    "Rowan felt a twinge in his gut. He put a hand upon the man’s shoulder. He took a few coins from his purse and pressed them into the man’s hand."
    show rowan hood happy at center with dissolve
    ro "Not today. You earned a few meals, at least. Take care, old man."
    "He bid the beggar farewell, which the man returned with a respectful nod. Rowan pulled his hood deeper over his features, and left the beggar behind, wary of causing a scene or attracting any unwanted attention."
    beggar "Take care… Rowan Blackwell."
    $ beggarLowCorEnd = True
    $ released_fix_rollback()
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

else:
    ro "We all make do with the lot life has given us."
    ro "This will suffice. Consider your debt repaid, old man."
    "A mocking smile came to the beggar’s face."
    beggar "What would ‘ave happened had I told you to just fuck off? I’d have ended up with another hole in my gut, wouldn’t I?"
    "Rowan stared him down with a cold expression."
    ro "... No."
    ro "That would be senselessly cruel. But now that you mention it, I’d appreciate if you kept our little deal to yourself."
    beggar "Yeah, yeah… piss off already."
    "Rowan briefly considered silencing the old fool, just to be safe. But it would attract attention. Regardless of his caustic attitude, the man {i}had{/i} provided him with some answers, even if their quality remained to be seen."
    "In the end, he pulled his hood deeper over his features, and left Beggar’s Row behind him. There was no longer any reason to linger."
    beggar "…Some hero you turned out to be, Rowan Blackwell."
    $ beggarHighCorEnd = True
    $ released_fix_rollback()
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

#######################################################################################################
#######################################################################################################
#######################################################################################################

label slumsEvent4:

$ slumsEvent4Seen = True
$ change_treasury(-40)

"The Slums of Rastedel were impenetrable, a literal wall of humanity that barred passage into its hidden places. Like an insular Goblin tribe, it was impossible to ingratiate oneself into the greater community without being labeled an outsider."
"Rowan needed to find Maud. But Maud clearly didn’t want to be found. You couldn’t beg, borrow, or steal such information. It could only be bought." 
"Who better to try his luck with then, than those who sold their bodies to feed themselves?"
"Rowan returned once more to the Red Light district, to the rows and rows of open windows. To the catcalls and bare chests of hungry women, and more than a few men." 
"Most of the whorehouses in the slums were shantytowns masquerading as houses of pleasure. They projected an image that was as feigned as their occupants’ cheap perfume." 
"Beneath the colorful paint and the red-tinged lamplight, desperation and poverty lurked. But not everywhere." 
"He stopped in front of a particular brothel that looked different from the others. It was sturdy, a three story building built relatively recently. Tall balconies looked out onto the street, supporting the floors above them with wood-carved pillars of curving, feminine contours."
"The place was clean, orderly without excess.  Half a dozen women reached out to him on the balconies above, blowing kisses and fluttering wisp-thin neglige like a banner upon the breeze." 
"If Maud’s officers visited any brothel around here, it would be this one. Rowan pulled his cloak tighter about himself and entered the front door."
"He came to a warm-lit entryway and approached the Madame of the Bordello."

scene bg50 with fade
show rowan hood neutral at center with moveinleft

madame "Welcome to the {i}Sheath and Dagger{/i}, stranger. Take off your cloak, and tarry awhile."

ro "Thank you Miss, but I’d rather retain my anonymity for the moment."

madame "As you wish, sir. But you will have to remove it when you enter the private rooms."
madame "There are no secrets beneath the bedsheets. If you expect my girls to bare everything to you, the least you could do is deign show them your face."
madame "How can I help you?"

ro " I was hoping to talk to you for a moment."

madame "I’m flattered, love. But I’m not for sale."

ro "That’s… not what I meant. I was hoping to ask you some questions."

madame "We don’t trade in information here, sir. We sell cunt. And at a premium. If you have business with one of my girls, you may while away the hours with them as you please."

"Well, that was a futile effort. Rowan nodded at the Madame as his gaze swept the room, eying the score of half-clad women lounging on couches or standing at the windows." 
"He spotted a particularly comely girl, bright-eyed and cheerful looking. Her hair was short, raven black and knotted into thin braids to add an element of exoticness to her appearance." 
"She had a certain, hopeful look in her eyes that told Rowan she hadn’t worked here for long.  And when Rowan looked her way, her cheeks reddened and she glanced away." 
"The girl played the part of blushing maiden well... perhaps a bit {i}too{/i} well." 
"She would do. Rowan gestured towards her."

ro "How much for her?"

madame "Shari? Twenty gold for a shagging. Forty for extra services."

"Rowan pulled the coins from his purse, noting the deliberate look the Madame gave him as he counted out the forty pieces."

madame "-And leave your weapons in the foyer. They will be well looked after."

show rowan hood angry at center with dissolve

"Rowan grunted and removed his sword belt. The Madame took his weapon with the wary eyes of a woman too-used to feints and trickery. She swept her hand out to the imperial staircase leading to the upper floors."

madame "Room Fifteen, Second floor. Shari will join you shortly."

show rowan hood neutral at center with dissolve

"Rowan ascended the stairs, passing by giggling couples and half-drunk patrons. He stepped into the red-lit room and closed the door behind him, letting out a soft sigh. Foregoing the bed, he walked over to the lone window, staring out at the thoroughfare."
"He heard the door softly open behind him. Rowan glanced back in time to see the bright-eyed girl from before give him a tremulous smile and shuffle into the room. She folded her arms behind her back in a submissive, ladylike fashion."

ro "You must be Shari."

shari "Yessir."
shari "If it please you sir, could you take off your hood? Madame says I can’t be alone with you ‘afore I see your face."

"Rowan furrowed his eyebrows. The Madame was far too savvy for his taste, but he supposed that was to be expected."

if avatar.corruption > 50:
    "He gave the whore a once-over again. A fragile girl like her… If worse came to worst, it wouldn’t be hard to intimidate her into silence."
    
else:
    "He gave the woman a once-over again. A delicate girl like her… Even if she did recognize him, surely he’d be able to leverage his reputation to ensure her silence."
    
ro "Very well."

"Rowan pulled back his hood. A flicker of surprise swept across Shari’s face."

shari "Who… "
shari "Y-you’re Rowan Blackwell!"
shari "I saws you at the parade, you was riding a white horse at the front."

"The eagerness in her voice made Rowan unintentionally smile. It was amusing to hear her drop out of her faux-noble accent. Beneath all the pretensions she was still just a slum girl."

show rowan hood happy at center with dissolve

ro "Would you please close the door, Shari?"

shari "Y-yeah o’ course."
shari "I mean... yes of course, sir."

"Shari hurriedly shut the door behind her, her eyes fixed to Rowan’s features as if to memorize them for later. Rowan undid his cloak and tossed it aside onto the bed. She turned to face him, her cheeks glowing a genuine cherry red."

shari "How do you want me, Lord Rowan?"

show rowan hood neutral at center with dissolve

ro "On the bed, preferably. And it’s just Rowan."

"Shari slinked to the bed and sat down on the opposite edge with her back facing him. She pulled off one of the black straps of her frilly dress, exposing a pale shoulder."

shari "Shall I be your blushing maid for the evening, Rowan?"

ro "Not just yet."
ro "First, I’d like to know about some of your other clients."

"The look on Shari’s face told him he’d caught her off guard."

show rowan hood happy at center with dissolve

ro "Call it voyeuristic curiosity."

shari "Oh my."
shari "I never would have thought the Hero of Karst was such a…"
shari "Pervert."

"She breathed out the last word with the whisper of a lover aroused by a secret revealed."

shari "Well, earlier today I-"

show rowan hood neutral at center with dissolve

ro "I was hoping to hear about someone specific, actually."

"Shari’s eyebrow rose. She cocked a leg over one knee, displaying her ankles to him. She kept her back to Rowan, glancing at him out of the corner of her eye."

shari "Who?"

ro "Dangerous people."

shari "There’s lots of dangerous folk in the slums, Rowan."

ro "...Have you ever slept with gang members?"

"Shari laughed, covering her lips demurely with her hand."

shari "Does a dog have fleas?"

ro "One of Maud’s Boys?"

"Shari’s eyebrow danced a dangerous jig atop her head."

shari "Maybe. I’ve had lots of ‘boys,’ Rowan."
shari "Something tells me I haven’t had a man like {i}you{/i} yet, though."

"Rowan circled the bed, leaning in to go face to face with Shari. He noticed her shrink back, her face going beet red as he planted his palms on either side of her on the bed."

ro "Tell me what you know about Maud’s Boys."

"The whore fluttered her eyelids. She seemed to be reveling in the moment. Her voice came out like a quiet exhale."

shari "Make me."

if avatar.corruption > 50:
    "Rowan suppressed a sigh. Of all the women in this whorehouse, why did he have to pick the one that {i}enjoyed{/i} being ravished? Rowan didn't know whether he should praise or curse his luck."
    "Sharli licked her lips, then parted her lips invitingly. If she was that earnest, then he supposed there was no downside in playing along…"

else:
    "Rowan’s lips formed a thin line. Solansia save him, of all the whores in this place, he {i}had{/i} just had to pick the depraved one?" 
    "Sharli licked her lips, then parted her lips invitingly. If the little bitch was this eager, then it wouldn’t be hard to make her squeal..." 

label shariMenu:

menu:
    "Tie her up and give her what she wants.":
        $ released_fix_rollback()
        jump shariTiedSex
        
    "Convince her that they shouldn’t have sex." if ShariNoSexFailed == False:
        $ released_fix_rollback()
        jump shariNoSex
        
    "Explain you’re not really THAT into women." if rowanGaySex > 0:
        $ released_fix_rollback()
        jump shariGay
    
    #TODO - add deception Rank 2 requirement
    "Pretend you’re not really THAT into women." if rowanGaySex == 0:
        $ released_fix_rollback() 
        jump rowanLieJump
        
    "Let it go.":
        $ released_fix_rollback() 
        jump shariLetGo

label shariTiedSex:

ro "Close your eyes. Don’t open them till I tell you to."

shari "Mmmm, are you going to-"

"Rowan put a finger to her cherry-red lips. Shari’s shoulders tensed at his touch. Her eyes widened, but she did not shy away."

ro "Try again."
ro "Close your eyes."

"She closed them, her long eyelashes fluttering shut. She let out a heavy exhale as she settled onto the bed. Her spine was rigid, her body tense. He was exciting to her."
"The mystique of his heroism was once again paying dividends. Rowan gently stroked her lips with his thumb, feeling the rush of heat as she quivered at his touch."

ro "Keep them closed, Shari."

shari "Yes, sir."

scene cg567 with fade
show rowan necklace happy behind cg567
pause 3

"Rowan stood up, leaving a void in her personal space. Her brow furrowed at his disappearance. Ignoring her, he circled the bed in a slow, circuitous manner." 
"His footsteps made loud thuds upon the wooden floor as he came to a halt on the opposite side. Rowan sat down, the threadbare bed creaked under their shared weight."
"He took hold of the upper layer of sheeting and pulled. A loud rip echoed in the room, causing Shari to jump in place. To her credit, she didn’t open her eyes."
"Rowan took the long strand of ripped fabric and approached Shari from behind her. He draped it across her eyes, weaving it around her head before tying it into a tight bow in the back."

ro "Tonight you are mine."

"Shari hesitated. Rowan ran a finger along the curve of her cheek. His warm breath glided across the back of her neck. A thrilling shiver coursed over her."

ro "Say it."

shari "Tonight, I’m yours."

"Rowan marveled at the goosebumps that formed on her neck when he spoke. He took her by the shoulders, peeling off her loose-fitting clothes piece by piece and leaving her naked. She sighed in his grasp."
"Rowan stood up and circled the bed once more, watching as Shari tensed at his approaching footsteps. He stepped into her space again, asserting it as his own." 
"Shari sat with her hands folded over her lap, concealing her womanhood like a maiden at her first bedding. Her face was clenched, waiting with bated breath to see what Rowan would do."

ro "When you’re with me here, tonight, I want you to think about all those dangerous men you’ve slept with."

scene cg568 with fade
show rowan necklace happy behind cg568
pause 3

"Rowan moved without warning, clambering up onto the bed so that his knee was in her crotch and her thigh between his legs. She gasped in surprise, but he put his hands upon her shoulders, steadying her."

ro "Because {i}none{/i} of the men you’ve met are half as dangerous as me."

"Rowan saw a full-body blush trail across her pale skin as she processed the statement. He smiled, reaching out to idly fondle one of her perky breasts."
"He began to grind his knee against her exposed pussy, watching as she squirmed in place. Her legs spread wider to allow him access to her nethers."

ro "Don’t move."

"She listened to his command, letting out a soft moan as he loomed over her."

ro "When I ask a question, you’re going to answer."

shari "{i}Mmmh.{/i}"

"There was a note of strain in her voice. A last, lingering bit of willful resistance. Rowan would snuff it out. He leaned into her, digging his knee hard against her clit. Shari’s back hunched forward as she let out a soft cry."

ro "You’re going to answer. Or I’m going to stop doing this to you."

"He pulled back from the brink, smirking at the trail of feminine goo that coated his knee. Shari whimpered. The whore had a submissive streak. Yet even still, she resisted the natural inclination to give in."
"Rowan had to be relentless on this point. He put his palm upon her chest, his fingers trailing across her neck with the barest hint of sexual threat."

ro "You’re going to answer. Or I’m going to stop."

"She nodded. Rowan could not see her eyes through the blindfold, but he could see the bob of her throat as she swallowed. Her inner thighs were trembling."
"Satisfied that the message had gotten across, Rowan placed his knee against her crotch once more. The friction was enough to force the helpless whore to rub herself raw against his unyielding body."

ro "Let’s start easy. A simple question, one I already know the answer to."
ro "Do you want me?"

shari "More than anything…"

"He dug a little deeper, allowing her to feel the weight of him hovering over her. He ran his fingers through her hair, as if he were about to pull her head down into his lap."

ro "Good girl. Keep going."
ro "Have you slept with one of Maud’s Boys?"

"Shari bit her lip and gave a little nod. She squirmed again, but Rowan punished her by pulling away. She let out a little gasp and went stock still. She was getting better at complying."

ro "Name him."

shari "W-we’s not supposed to kiss n’ tell. Madam said-"

"Rowan pulled his knee away again. Shari let out a whine like a bitch in heat, a small trickle of femcum streaming impotently from her cunt."
"She was so engrossed by the edging that she dropped into her natural slum-slang once more."

ro "Is the Madame here in this room? Is she asking you these questions?"

"Shari blushed and lowered her head. She shook her black locks of hair back and forth, unable to meet Rowan’s eyes, even through a blindfold."

ro "No. I am."
ro "So name him."

shari "H-he’s… his name’s Kesser."

if knowHandsign == True:
    "...Kesser. That was the name of the man who he’d seen guarding the entrance to one of Maud’s warehouses. Shari wasn’t lying."
    ro "Good girl."
    "He tightened his knee, allowing her to grind her crotch back and forth against him. Shari let out an appreciative cry of pleasure."
    
ro "Who is he? What does he do?"

shari "I-I dunno! He just waltzed into the brothel a few days ago… {i}mmmh{/i}! A-and told the Madame he was one o’ Maud’s Boys. "
shari "She let ‘im have the pick o’ the litter! {i}Ahn{/i}!"

ro "And you were the prize, hm?"

"Despite her struggle to remain calm, Shari adopted a fierce expression beneath the blindfold."

shari "I am sir... Why else would {i}you{/i} ‘ave picked me?"

"Spunky girl, this one. Fortunately Rowan knew how to tease the spunk right out of her."

ro "Good. Another easy one:"
ro "How wet are you right now?"

shari "N-not much, sir."

"She was wrong; purposefully so. Rowan let out a huff of air, pulling his leg away again. She shivered in place, her pussy twitching and clenching at the sudden denial."

shari "{i}Mmh{/i}, No!"

ro "Try again."

shari "{i}Please{/i}, Rowan-"

"Rowan made as if to step away from the be entirely. Shari let out a tortured cry of frustration and excitement."

ro "{i}Try. Again.{/i}"

shari "I-I’m wet! I’m wet! I’m soakin’ my own linens wif it, sir!"
shari "Please Rowan, I {i}need{/i} to cum!"

"He had her right where she needed to be. Rowan’s knee returned to its rightful place between her legs, edging her towards the precipice of orgasm once more."

ro "Soon enough, whore. First I need answers."
ro "What’s Maud’s racket in the Brothels? What are her Boys doing here?"

shari "T-they’s here to get their jollies, tha’s all!"

"Rowan slapped her lightly across the cheek. Shari let out a gasp at the unexpected contact."

ro "Stop lying, or you’ll earn a second one."

shari "No! They is! Maud doesn’t handle the whorehouses! Honest!"
shari "Us whores are Madame Montiel’s turf! She’s who runs things!"

"The name was familiar to him. Amaraine mentioned Montiel was also part of the Northside Bannermen. But if that was the case, then he was chasing the wrong dog."

ro "And Maud?"

"Shari’s mouth snapped shut. Despite her desperate need to answer his questions, and even more desperate need to cum, she seemed hesitant to speak of her."

shari "The… the other girls say she’s an angel. Says if’n you find yourself in a bad way, she can… she’ll help you. She’ll help {i}anyone{/i}."

ro "Even you?"

"Shari nodded, lifting her chin as her lower lip quivered. Rowan couldn’t see her eyes, but he saw her brow clenching in desperation."

shari "Even me. Even a whore like me. Please sir, I feel like I’m half-bout to piss myself."

"Rowan nodded, reaching down to finish her off with his nimble fingers. Her honesty had at least earned an orgasm. Shari let out a pleasured scream as his fingertips dove into her sodden twat."

shari "I’m gonna… I’m gonna…"
shari "{i}Aaaahn!{/i}"

"Rowan brought her to the precipice. He frigged her drooling entrance at a frenetic pace, watching with delight as the whore trembled, stiffened, then went rigid."
"He lifted her hood with his thumb, rubbing across her clitoris like he was scrubbing a plate."

shari "Oh {i}Rowan{/i}!"

"She came, fountaining a sizable squirt of femcum from her nethers as her thighs clenched and her body seized up. Shari let out an open-throated cry of feminine elation, her hands leaping to her face to rip the blindfold off of her."
"Rowan watched in satisfaction as she made eye contact with him at the moment of orgasm. Her eyes crossed, her lips opened into an O of pleasure, and her whole body trembled from the seismic convulsions he made inside of her."
"She fell back against the bed, putting a hand to her forehead as she wiped the sweat from her brow. She basked for a moment in the warmth of post-orgasmic bliss."

shari "{i}Aah{/i}, I feel like Marianne after a visit to the royal fuckin’ chambers, I do."
shari "You sure now how to shag a hag, sir."

ro "Please, call me Rowan."

"Shari lifted her hand off of her face and fixed him with a heavy, sexual stare."

shari "Make me cum like that again mister, and I’ll call you whatever you like."

"Rowan chuckled, standing up off the bed and brushing himself off. He saw Shari sit up in confusion."

shari "Wait, where are you goin’? Didn’t you want to…?"

#rowan hood smirk

ro "I think I’ve had my fun for the evening."

"Rowan moved to leave. Shari practically leapt out of bed in a rush to delay him."

shari "B-but tonight I’m {i}yours{/i}, you said so!"
shari "Can’t we just-"
shari "I-I mean, you {i}paid{/i} the coin for a shagging... don’t you want your money’s worth?"

"Pleased that he had played the pretty thing to perfection, Rowan reached out and took her by the chin. Her breath caught in her throat. He planted a shallow kiss on her lips."

ro "I got my money’s worth tonight, Shari."

"The whore went bright red again. A girl this callow had no business being a prostitute. He swept a thumb across her cheek and gifted her with a smile."

ro "You go downstairs after I leave, and you tell your Madame that I had a wonderful time with you. I had such a good time, in fact, that I paid you extra."

"Rowan pushed a few extra coins into her hand. Shari broke out into a wide smile."

ro "Remember what you told me tonight? Good girls don’t kiss and tell. Not a peep about what went on between these bedsheets, you hear?"
ro "Who knows? Maybe I’ll return to finish the job."

shari "I..."
shari "I’d like that, M’lord."

#rowan hood happy

ro "Till we meet again, M’lady."

"Rowan grinned, feigning for a moment as if to kiss her before standing up, pulling up his hood and leaving the room for good."

$ slumWhoreInformation = True
$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

##########################################################

label shariNoSex:

"Rowan took a deep breath. Granted, Shari was attractive, but… It didn’t sit well with him, indulging her fantasies just to get information."

ro "Ah. So that’s how it feels."
ro "Having to please people out of necessity."

#diplo check [easy] (to do)
$ res_roll = dice(6)
if res_roll > 2:
    pass
else:
    shari "Mmmm… And I’m a wicked, {i}wicked{/i} girl for forcing you to do it. {i}Punish me{/i}."
    if avatar.corruption > 50:
        "His eyelid twitched. Oh, the wench was really asking for this…"
    else:
        "Well, it was worth a shot. Not that satisfying a woman this thirsty would be particularly difficult… "
    $ ShariNoSexFailed = True
    jump shariMenu

"Her eyes softened, and she gave him a little pout, arms crossed."

shari "You’re the one who paid for me! Don’t try to make me feel guilty about wanting to do the deed after the fact! "

"...And just like that, the magic of the moment was gone. Rowan uttered a sigh of relief and moved to sit beside her on the bed."

ro "I admit, it’s a mean thing to do, and I apologize for putting you in this situation. But I wouldn’t lead you on like this if it wasn’t important."

"He let her sulk, his hand reaching for her own and squeezing it lightly. After a long moment, she rolled her eyes and shot him a tired look."

shari "I imagine a hero like you wouldn’t be inquiring ‘bout the Knights if there wasn’t some damsel in distress somewhere."

ro "…Yes. Something like that."
ro "If it’s any consolation, you’re the most pleasant informant I had so far."

shari "Ha! Well I’d hope so!"
shari "Fine. Madame is going to be madder than a wet hen in a rainstorm, but… youre Rowan Blackwell."
shari "I suppose you can be my exception. But under one condition!"

"She her lips curled into a devious smile, one that almost made him regret not indulging her after all."

shari "When the bards make an epic tale of Rastedel defense, I want to play a supporting role!"

show rowan hood happy at center with dissolve

ro "I’ll ask the court poets to see what can be done."

"She was a funny girl, this whore. Too quick to smile, too easy to convince."

shari "Yes! Alright, no take backs, because… I don’t really know that much."
shari "At least, not about Maud. Madame Montiel handles the brothels. We don’t see Maud’s men here, unless one of them comes to get their jollies."

ro "Anyone in particular strikes your memory?"

shari "Mmm… There was this one guy… Kesser, I think? Looked really important."

if knowHandsign == True:
    "The man who handled the door from a few nights back. So he wasn’t just any other guard… "
    
shari "I know he’s been handling some of the dirtier stuff, but… It’s not like he’s bad or anything! "
shari "I heard good things about Maud and her boys! My friends - The ones who aren’t lucky enough to work here - they say Maud’s an angel. A real Knight in shining armour!"
shari "They say if you find yourself in a bad way, she can… she’ll help you. She’ll help {i}anyone{/i}."
shari "So if you really want to find her or her men… I think you should simply ask for that. It should work sooner or later. "

if slumsEvent3Seen == True:
    "Was it really that simple? Shari wasn’t the first person he’d met who had a high opinion of Maud and her people."
    
else:
    "Was it really that simple? Shari seemed to think highly of Maud and her people… Though this could be simply a clever ploy on Maud’s part."
    
"But he would find no further answers here. He hugged the girl in gratitude, then pushed a few extra coins into her hand."

ro "Thank you Shari. Go downstairs after I leave, and you tell your Madame that I had a wonderful time with you. I had {i}such{/i} a good time, in fact, that I paid you extra."
ro "And not a word about what we discussed today, alright?"

shari "-At least not until I’ve heard the bards sing it! "

"She broke into a quiet giggle. She could likely guess how her own role would be described. Rowan gifted her a smile as he gathered his things, readying to leave."

scene black with fade

"He didn’t have the heart to tell her if any bards remained after this war, they would not sing praises for the ‘honorable’ Rowan, nor of the kindhearted Shari."
"No, their frightened tongues would sing only of the glories of Andras and Jezera."

$ slumWhoreInformation = True
$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

######################################################

label shariGay:

"Rowan scratched the back of his neck. Here sitting before him like a waiting conquest was a young, incredibly attractive woman. She was all but begging him to fuck her. Most men wouldn’t think twice, but for him…"

label rowanLieJump:
    
ro "Shari, don’t take it the wrong way, but… I picked you because you seemed the type who is very popular with the wealthier clientele." 
ro "If I were to pick someone based on preference… I wouldn’t exactly pick any of the women here."

"Shari stared at him in silence, not understanding. Then, her lips formed a surprised little “o”, only to once again be replaced with an even more confused expression. "

shari "Wait, didn’t you marry a girl after the war?"

ro "Well, yes, but- Let’s just say it’s complicated."

"A devious sparkle entered her eyes. Rowan did not like it one bit."

shari "So who do you think about when you, you know... with your wife?"
shari "Ooooh, is it Valyr? That hero from the south? Ma said he had an arse to {i}die{/i} for! "

ro "Shari, we were quite literally fighting for our lives every day back then."

shari "Did you have your wife wear a beard on your wedding night?"

show rowan hood angry at center with dissolve

ro "Now hold on- do you ask all your clients about their sexual relationship with their wives?"

shari "Oh, oh! have you met the guard captain? Sir Alarie, wasn’t it? Tell me: Hot or not?"

if alainMet == True:
    menu:
        "Hot.":
            $ released_fix_rollback()
            shari "Knew it!"
            
        "Eh.":
            $ released_fix_rollback()
            shari "No way!"
            
else:
    show rowan hood neutral at center with dissolve
    ro "Haven’t have the pleasure yet, I’m afraid."
    shari "That’s a shame."

show rowan hood concerned at center with dissolve

ro "So are you done embarrassing me?"

shari "Depends. Do you know how embarrassing it is for a lil’ slum-girl like me to be picked by the Hero of Rosaria... only to learn he prefers to cross swords, in more ways than one?"

"She stuck her tongue out at him. Rowan wondered how many men in this whorehouse had to deal with a prostitute throwing a fit over being paid to not ply her trade."

ro "Shari, I… I see your point. And I’m sorry for the deception. And even though I could grind my teeth and just bear it, I..."
ro "I think there’s enough false passion in this place. Don’t you agree?"

"Shari’s eyes softened. What he’d said seemed to have struck a chord in the young woman. She put a hand upon his own. She dropped her faux-noble accent completely."

shari "Well what d’you know?"

show rowan hood happy at center with dissolve

shari "Turns out the Hero o’ Karst is just a softie after all."
shari "Fine. Madame is going to be madder n’ a wet hen in a rainstorm, but… you’s Rowan Blackwell. I suppose you can be my exception. But just so you know… I don’t really know much."
shari "At least, not about Maud. Madame Montiel handles the brothels. We don’t see Maud’s men here, ‘cept when one of them barges in to get their jollies."

ro "Anyone in particular strike your memory? "

shari "Mmm… There was this one guy. Kesser, I think? Looked really important."

if knowHandsign == True:
    "The man who handled the door to Maud’s Warehouse from a few nights back. So he wasn’t just any other guard… "

shari "I know he’s been handling some of the dirtier stuff. But it’s not like he’s bad or anything!"
shari "I heard good things about Maud and her boys! My friends - the ones who aren’t lucky enough to work here - they say Maud herself is an angel. A real knight!"
shari "Say if’n you find yourself in a bad way, she can… she’ll help you. She’ll help {i}anyone{/i}."
shari "So if you {i}really{/i} want to find her, I think you should ask for that. It’ll work sooner or later. "

if slumsEvent3Seen == True:
    "Was it really that simple? Shari wasn’t the first person he met who had a high opinion of Maud and her gang."
else:
    "Was it really that simple? Shari seemed to think highly of Maud and her gang… Though this could be simply a clever ploy on Maud’s part."
    
"But he would find no further answers here. He hugged the girl in gratitude, then pushed a few extra coins into her hand."

ro "Thank you Shari. Go downstairs after I leave, and you tell your Madame that I had a wonderful time with you. I had such a good time, in fact, that I paid you extra."

shari "Only if you promise not to come back in later and hire one of the sword-swingers instead, eh? That might put a damper on the whole story."
shari "Course, odds to arseholes you’d give ‘em the ride o’ their lives, yeah?"

"He chuckled as he gathered his things. Her smile was contagious, and in the end, he lingered a couple minutes longer to make the story seem more believable."
"Spending forty gold coins to crack bad jokes with an all-too-willing whore…"

scene black with fade

"Cla-Min would kill him."

$ slumWhoreInformation = True
$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

###################################################

label shariLetGo:

ro "...On second thought, I don’t think I’m in the mood tonight."

"Rowan stood up, pulling his hood back over his head as he made to leave."

shari "Come on, m’lord. I didn’t mean it like that."

show rowan hood angry at center with dissolve

ro "I know you didn’t. But in hindsight, neither did I."

"Rowan pulled out his coinpurse and tossed her a few extra gold. She caught it with a look of surprise."

ro "Here. For your silence. I never took my hood off, you have no idea who I was or what I looked like."

shari "O-okay."

show rowan hood neutral at center with dissolve

ro "Tell your Madame that I got what I came for. Tell her I’m a quick shot, or I just wanted to watch you undress, then left abruptly."
ro "Tell her…"

show rowan hood concerned at center with dissolve

ro "Kharos take me, just tell her whatever you want."

"Rowan stalked out of the room, black stormclouds darkening his mood. Yet another dead end… were the slums truly this impenetrable?"

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

#########################################################################################
#########################################################################################
#########################################################################################

label meetMaud:

$ maudEvent1Seen = True

scene bg45 with fade

"The closer one got to the fire, the higher was the risk of getting burned."

show rowan hood neutral at center with moveinleft

"Rowan pulled his hood further over his eyes, and turned into a narrow alley as he saw a pair of brutish looking men cast him suspicious looks." 
"The beggars’ information narrowed the scope of his search immensely. But now his continuous presence in what he dubbed “Bannermen territory” was starting to draw unwanted attention."

if knowHandsign == True:
    "The suspicious walled warehouse he'd seen a few nights back was his primary target of interest. He spent much of his time observing it from the shadows, trying to determine if Maud might be one of the people staying there."
    show rowan hood angry at center with dissolve
    "Without success - he never saw anyone who he suspected could be the fabled slums leader."
    show rowan hood neutral at center with dissolve
    "But a large man he believed was part of her gang - Kesser, he recalled - seemed to have used the place as his base of operations. Taking a gamble, Rowan trailed him one night."
    hide rowan with moveoutleft
    scene bg50 with fade
    "His suspicion on the man’s allegiance was all but confirmed. He spent enough time in the slums to understand the pecking order within them."  
    "Like a swarm of fish, the poor and the desperate that crowded the streets parted way before the powerful sharks of the slums. But only a handful earned a respectful nod alongside it. Kesser was one of them."
    show rowan hood neutral at edgeleft with dissolve
    "Being as careful as he could be - an ambush was more than likely - Rowan finally followed him to a simple wooden building near the outer walls of the city. Nothing distinguished it from any of the hundred he had just passed on the way there."
    "Except it had a pair of bored thugs at the entrance, who gave Kesser a short nod after being shown the signal, the large man coming in. "
    show rowan hood neutral at center with moveinleft
    "Knowing this was his chance, Rowan waited a moment, then followed suit."
    
else:
    #TO DO - stealth check
    $ temp_res = check_skill(8, 'move_silently')
    if temp_res[0]:
        show rowan hood happy at center with dissolve
        "But while an urban jungle differed vastly from a regular one, it held the same principles. And even if the Bannermen held the turf advantage, it would do them little good against the legendary skill of Rowan Blackwell."
        show rowan hood neutral at center with dissolve
        "Having spent enough time in the slums to grow familiar with its many twists and turns, Rowan navigated the streets with ease, observing Maud’s men from the shadows and making a quick retreat the moment their eyes laid on him."
    else:
        "And an urban jungle differed vastly from a regular one. In his life, Rowan managed to evade countless demons and orcs, brushing against death more times than he could count." 
        "But while the slum thugs had neither the numbers of the orcs, nor the skills of winged succubi, they knew their turf, and had no trouble noticing a hooded figure lurking in the shadows."
        show rowan hood angry at center with dissolve
        "More than once, Rowan was forced to abandon his hiding spot and make a hasty retreat, not wishing to risk a violent encounter with people he wished to turn into allies. "
        "It delayed his search, but did not stop it."
        show rowan hood neutral at center with dissolve
        $ avatar.mp -= 4
        #mental damage TO DO
    "He wasn’t certain what he was looking for - despite his efforts, all he had were vague hints to Maud’s role in the slums, and nothing on her appearance. "
    #TO DO - perception test
    $ temp_res = check_skill(8, 'spot')
    if temp_res[0]:
        scene bg50 with fade
        show rowan hood neutral at center with dissolve
        "But a keen eye, a level head, and at times a little bit of luck could carry a man far. Rowan had no shortage of the first two, and one night blessed him with the third."
    else:
        "One could always be on the lookout for “something suspicious”. But what did that mean in a land where law was as an abstract of a concept as personal hygiene?"  
        "One night he found two groups fighting in the middle of the square, only to discover it was a family quarrel between two brothers, over the hand of a whore that was clearly playing them both." 
        "Another he discovered a well-dressed man with a bright smile trying to sell wonderful cures for all ailments that plagued the “good, proper folk of Rasedel.” He got beaten up within the hour." 
        "And yet another, a wild-looking woman, dagger in hand, was pushing through the streets, a package in her hand, threatening to stab anyone who came near."
        show rowan hood concerned at center with dissolve
        "Rowan followed her home, watching from afar. The package turned out to be stale bread."
        scene bg50 with fade
        show rowan hood neutral at center with dissolve
        "It was only after several wasted nights, that he stumbled upon something that could be of use to him."
        $ avatar.mp -= 4
        #mental damage TO DO

    show rowan hood happy at edgeleft with moveoutleft
    "A pair of thugs dragged a struggling man through the streets, a sack over his head. The one leading had a confident stride and a bright smile on his face, and greeted everyone nonchalantly as he went."
    show rowan hood happy at edgeleft with dissolve
    "And many greeted him back, paying no mind to his captive."  
    hide rowan with moveoutright
    "Making sure to stick to the shadows - the pair paid little attention to what was happening around them, but that was no reason to be careless - Rowan followed them to a simple wooden building near the outer city walls."
    show rowan hood neutral at edgeleft with moveinleft
    "Nothing distinguished it from any of the hundred he had just passed on the way there - except it had a pair of bored thugs at the entrance, who smiled at the man and opened the door for him."  
    "Rowan waited a moment, observing the building from a distance. Another man, this one much larger, soon arrived as well. But after that… Nothing." 
    show rowan hood neutral at center with moveinleft
    "Knowing this was his chance, Rowan made his move." 
    
"He stepped from the shadows, and approached the door. Slowly, with his hands open and on display. The men tensed, their own hands hovering over the handles of their sword."

if knowHandsign == True:
    ro "I’m looking for Maud. It’s important."
    "He recreated the hand sign, as well as he could, and saw the thugs relax. They looked at each other, shrugged, and knocked at the door."
    
else:
    if slumWhoreInformation == True:
        ro "I’m looking for Maud. I need help, and she’s the only one I can turn to."
        "One of them rolled their eyes, while the other gave him a sympathetic look. They didn’t pry, and simply knocked at the door behind them."
    else:
        ro " I’m looking for Maud."
        show rowan hood angry at center with dissolve
        thug "No idea who’s that."
        ro "Look..."
        show rowan hood neutral at center with dissolve
        "He opened his cloak just a little, to show his sword. The men started drawing theirs, but Rowan stopped them by raising his hand in a peaceful gesture."
        ro "If you’re standing guard, then I take it you’re smart enough to realize I’m not just any regular sellsword."
        ro "So let’s cut the part where I have to rough you up, and just let me talk with someone higher ranking than you."
        "Hard logic could knock a sword out of a man’s grip as well as a clever feint, if used at the right moment. The men looked at one another, grumbled, then knocked at the door behind him."
        
if knowHandsign == True:
    "A man opened it wide - a skinny, smiling man, and one Rowan took an immediate dislike to. He was the kind that never took anything seriously, murder included."
        
else:
    "A man opened it wide - a skinny, smiling man, the same he saw earlier, and one Rowan now took an immediate dislike to. He was the kind that never took anything seriously, murder included."
    
if knowCalhoun == True:
    "His left hand had only four fingers in it. So that was Calhoun, Maud’s second in command."
    calh "A guest! Welcome, welcome, come in, make yourself at home!"
else:
    "A guest! Welcome, welcome, come in, make yourself at home!"

if knowHandsign == True:
    "He took a step back and made a lavish bow, though never took his eyes of Rowan. By his side, also watching Rowan with suspicion, stood Kesser, ready to strike at a moment’s notice."
    kesser "Yer’ bein’ too careless, Calhoun. "
else:
    "He took a step back and made a lavish bow, though never took his eyes of Rowan. By his side, also watching Rowan with suspicion, stood a large, burly man, ready to strike at a moment’s notice."
    kesser "Yer’ bein’ too careless, Calhoun."
    $ calhounName = "Calhoun"
    
show rowan hood angry at center with dissolve
    
calh "Oh relaaaaaaaaax, Kesser! Look at that guy! His dress screams “I’m a messenger for a corrupt, shadowy figure, but I’m trying to be inconspicuous about it.” I mean, the cloak! And the hood!"

show rowan hood neutral at center with dissolve

calh "Besides, if he wants to take Maud one on one, fuck, he’s invited to try! Right, Maud?"

show maud neutral behind bg50

maud "… A moment. But let him in."

"The two men parted, Kesser reluctantly, Calhoun spreading his arms far and wide as he showed Rowan their kingdom: a shoddy, poorly lit room, almost empty, sans for a few people in it."

show rowan hood shock at center with dissolve

show maud neutral at edgeright with dissolve

"One of whom was sprawled across the table, near-naked, his mouth gagged, his limbs bound. And over him, her back turned to them, stood Maud."

show bg50 with sshake

"A sickening crack and a muffled scream filled the room as she just broke the man’s arm."

show bg50 with sshake

"And another soon followed, as Maud then bent his elbow in the opposing direction."

show bg50 with sshake

if avatar.corruption < 50:
    show rowan hood concerned at center with dissolve
    "With her brutes surrounding him on both sides, Rowan could only watch in horror as Maud methodically worked her way up the man’s arm, breaking it in several places with frightening ease."
    "Screams turned to howls, but she didn’t stop. Didn’t hesitate for even a second.  "
else:
    show rowan hood neutral at center with dissolve
    "Arching an eyebrow, Rowan watched as Maud methodically worked her way up the man’s arm, breaking it several places with frightening ease. Screams turned to howls, but she didn’t stop. Didn’t hesitate for even a second."
    
calh "Sorry for the wait, but it’s not just a social gathering, you understand? We’re kind of at work here. I mean, Maud is, we’re just here to add gravitas to the situation, you know?"

if avatar.corruption < 50:
    show rowan hood neutral at center with dissolve

"He didn’t even pay attention to whatever Calhoun was saying. It was Maud he was focused on. But it was only after she was finished with the left arm, and moved to the right, that Rowan could get a proper look at the woman who ruled the slums."

show rowan hood neutral at midleft with moveoutleft
show maud neutral at midright with moveinright

"… She didn’t look the part. She was a plain woman, with an unattractive face, marred by a scar on her cheek. Her slightly too long, dyed hair fell on her eyes as she leaned over the table to continue her task."
"She was short, diminutive almost, but obviously had no problem repeatedly breaking one bone after the other. She held more strength than Rowan would suspect of someone on her posture. Perhaps magic was at work?"

maud "… Your turn, doctor."

"Two people that stood by her side, Rowan now realized. An older man in a grey gown, and a young girl with bright eyes and hair dyed green, holding a half-burned notebook close to her chest."   
"The man licked his lips nervously, and approached the table. With a somewhat shaky voice he began explaining how to identify different bone fractures and how to properly set and bind each one. The girl wrote down everything, with commendable diligence."
"And Maud turned her attention to him."

show rowan hood shock at midleft with dissolve

maud "Rowan Blackwell."

show rowan hood neutral at midleft with dissolve

"So much for keeping a low profile. Her words made everyone stop -  well, everyone except one person, who fell off her chair."

#maud happy

calh "Ouch, ouch ouch ouch- wait, you serious?! Rowan Blackwell? Rowan fucking Blackwell?! How-"

maud "There was a parade. You should go out more."

calh "Fuck, hold on, I had something for this… "

#maud neutral

"Maud tilted her head, not paying much attention to her own man. Hands crossed on her chest, she continued to watch the hero."
"Rowan expected to see a sneer. Maybe a glint of interest. A hint of adoration. Hells, even a creeping, lustful smile. The latter was growing more common by the month."

show rowan hood concerned at midleft with dissolve

"But Maud’s cold eyes held nothing. Told him nothing.  She was neither impressed, nor disgusted with the Hero of Karst. Hell, she didn’t seem at all alarmed or concerned by his arrival."

show rowan hood neutral at midleft with dissolve

maud "Continue, doctor."

"The short order broke them all out of their stupor. Calhoun shut up, while the slum doctor slowly resumed his explanation, stuttering, but still." 
"Only the bound man kept staring, desperately trying to push the gag out of his mouth, his hope rekindled by Rowan’s arrival. He was a hero, so surely-"

maud "Don't."

show bg50 with sshake

"She grabbed the man by the hair and slammed his head into the table with a deafening crack. His body went limp in an instant."

ro "Isn’t this a little excessive?"

"Maud tilted her head again, and cast him a bored look. "

maud "Do you care?"

if avatar.corruption < 50:
    ro "I dread the day I no longer will.  "
else:
    ro "… No. I suppose not. This is your territory, and your laws."

maud "Mhm."

"She neither approved nor sneered at his response - merely gave him a short nod of acknowledgment."

maud "Contracted syphilis. Told him to stay away from the whores."
maud "He did not."      
maud "I would kill him. But Lily needed someone to study on."

#maud happy

"The young girl gave Maud a bright smile, and Rowan saw the gang leader return it. It was only a subtle rise of the corner of her lips, so short you could blink and miss it. But it was there."

ro "… Perhaps it would be best if we took this conversation elsewhere?"

maud "Why?"

ro "We’re distracting them. And what I want to discuss is of great importance. It’s not-"

show rowan hood shock at midleft with dissolve

maud "-meant for them. "

#maud angry

"In a blink of an eye, he felt the temperature in the room drop. Her tone was quiet, but the chill in her voice froze him to the bone. Maud dug her fingers into her arms, as if she was just barely restraining herself from grabbing Rowan by the throat and ripping it out."

show rowan hood angry at midleft with dissolve

"He felt someone put a hand over his shoulder. Kesser leaned in, his voice steady, but Rowan felt the tension underneath:"

kesser "If it concerns the people o’ the slums, then surely ye can speak of it in their company, eh? "

calh "Nothing about us without us, you know? It’s just rude - you’d think the hero of Karst would have better manners."

show rowan hood neutral at midleft with dissolve

"On all sides, he was surrounded by murderers and sadists. He saw the hateful sneer creep into Maud’s lips-"

#maud shocked

lily "… And what if the bones stick out of the body? "

doctor "That’s not a good sign, obviously, but…"

#maud neutral

"-and he saw it disappear a moment later. The slums leader closed her eyes and took a deep breath, and when she opened them again, they were as unreadable as before."

maud "Say what you have here."
maud "And make it quick."

"Kesser released his shoulder, and returned to his place near the front door. Calhoun whistled a happy tone as he started to hide the wide collection of daggers Rowan wasn’t sure when he took out." 
"Looks like this was as good of a chance at getting Maud on his side as he was going to get."

menu:
    "An offer she can't refuse." if avatar.corruption > 30:
        $ released_fix_rollback()
        "Rowan stepped up, taking the place by her side as he watched the doctor continue his lesson. Low-level theatrics, all of it. He wouldn’t be intimidated by them."
        ro "Then I’ll cut straight to the point. Between the orc threat and nobles’ squabbling, the situation in Rastedel has become… Volatile, so to speak."
        ro "I need people who will help me put order to this chaos. Who will help me make it so it doesn’t become that way ever again."
        ro "I know the Northside Knights hold considerable influence over the slums. I wish to make use of it."
        maud "And why should I let you?"
        ro "So that you can be part of that new order. An order where the Northside residents are no longer Rastedel outcasts. And order where you don’t have to break bones to prove a point."
        maud "Mmh."
        "Maud gave a short nod. Straight and to the point, he felt Maud wouldn’t be one to appreciate long speeches-"
        
    "Rastedel needs her help." if avatar.corruption < 50 or slumWhoreInformation == True:
        $ released_fix_rollback()
        "Rowan stepped up, keeping his expression neutral as he watched the doctor continue his lecture. Perhaps it was foolish of him to try and appeal to a better nature of someone who broke bones like twigs."
        if slumWhoreInformation == True:
            "But if what he learned in the brothel was worth anything… Then maybe this was the right approach, despite the events he bore witness to."
        ro "I am sure you already suspect my presence here doesn’t foretell anything good."
        maud "Mmh."
        ro "So forgive me the dramatics, but I’ll say it how it is: Rastedel is in grave danger. Between the orc threat and nobles squabbling for power… I need someone who will help me put order to this chaos."
        ro "I know the Northside Knights hold considerable influence over the slums. If we are to survive this crisis… I need you by my side."
        ro "Help me make things right by Rastedel, and I’ll make sure Rastedel makes things right by you."
        maud "Ha."
        "It wasn’t even a dry laugh. It was a shadow of one - an apt reply to a joke one heard a thousand times."
        maud "Alright."
        $ maudFaith += 1
        
show rowan hood shock at midleft with dissolve

maud "The answer is no. The Bannermen don’t take sides."

show maud neutral at edgeright with moveoutright

"She turned away, and that was that."

show rowan hood angry at midleft with dissolve

"It took Rowan a moment to gather his jaw from the floor. He expected her to bargain, or even play hard to get, but nothing like this!"

show rowan hood angry at center with moveinleft

ro "I find that hard to believe, Maud."

"She shrugged as she moved behind the girl to take a look at her notes. The girl - Lily, was it? - offered them with a smile."

maud "Believe what you want."
maud "I don’t play politics. I just keep the peace."

if avatar.corruption > 60:
    "He wasn’t sure what was it that broke the camel’s back. Maybe it was her casual tone. Maybe it was the obvious adoration in the young girl’s eyes. Or maybe the self-righteous attitude. But her words made his blood boil."
    ro "Listen here- "
    #maud annoyed
    "Her eyes shot to him, murder clear as day in them. He heard steel being drawn."
    if julietSex == True:
        #maud shocked
        ro "Oh fuck off, Werden glares twice as hard as you and I still fuck his daughter."
        #maud annoyed
    else:
        ro "Oh fuck off, Werden glares twice as hard as you."
    ro "Listen here, I don’t know, and I don’t care what twisted philosophy or bizarre code of honour you and your Bannermen live by."
    ro "You find the court distasteful? Devoid of honour and so full of filth the slums gutter seem like a pristine spring stream? Fine, I get that."
    ro "But if you really want to keep the peace, you do what I do: Get your hands dirty."
    show rowan hood neutral at center with dissolve

else:
    "Peace? She kept the peace? It took Rowan every ounce of willpower not to look at the door, not too look in the direction of the chaotic, violence-ridden streets of the Rastedel slums."
    if avatar.guilt > 50:
        show rowan hood concerned at center with dissolve
        "Did he sound the same, every time he spoke of his servitude to the twins? He shook his head - now was not the time for that."
    show rowan hood neutral at center with dissolve
    "It sounded like a bad joke, and with Maud’s flat, apathetic tone, it was impossible to guess whether or not it was meant as one. But to one person it wasn’t a joke." 
    "To one person, it was reality. To the young girl, so proud to show Maud the progress she had just made. Perhaps to others as well." 
    "Perhaps it was their faith that allowed Maud to break bones and crush skulls without a moment of hesitation."  
    "He wondered how deep Maud’s delusions ran, and found no answer. But if he had to play into them to accomplish that goal, then so be it." 
    ro "… Then help me keep that peace. "

ro "I didn’t play politics either, and look where it got us." 
ro "I bought Rosaria 8 years of peace, and now things are worse than ever."
ro "Don’t make my mistake."
ro "Don’t let your inaction destroy the things you’re trying to protect."

maud "..."

show rowan hood concerned at center with dissolve

"A long silence followed.  He kept his eyes on Maud. He needed to see something in them. Some hint that his words reached her."

if avatar.guilt > 50:
    show rowan hood happy at center with dissolve
    "And they did - damn it, they did! He saw something stirred inside of her. In those dead eyes, that seemingly knew nothing but violence."
    show rowan hood concerned at center with dissolve
    "It was the same thing he saw every time he stared into his own reflection."
    show rowan hood neutral at center with dissolve
    
else:
    show rowan hood neutral at center with dissolve
    "And they did - damn it, they did! He saw something stirred inside of her. In those dead eyes, that seemingly knew nothing but violence. He just couldn’t tell what."
    
maud "… You remind me of someone."

ro "And who might that be? "

maud "… It doesn’t matter."

show rowan hood neutral at midleft with moveinleft
show maud neutral at midright with moveinright

maud ".. Fine. I’m willing to consider your proposal. If you’re willing to back words with action."
maud "Find me next week. Bring your sword."

ro "Very well. And… Thank you. For listening."

maud "Hmph."

hide maud with moveoutright

"That was his cue. Her two henchmen cleared the way for him, Calhoun doing so with a lavish bow and a wicked smile, while Kesser kept a stone face that did nothing to hide his unease."

calh "Don’t worry about finding us. We’ll find you."

hide rowan with moveoutright
show maud neutral at midright with dissolve

"Rowan turned around for the sole purpose of rolling his eyes at the man. And just as he did, he saw Maud in the back of the room. She was ruffling the girl’s hair affectionately, her dark eyes staring into the distance, lost in some old memory."

scene black with fade

$ maudMet = True
$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

##################################################################################
##################################################################################
##################################################################################

label maud_event2:

$ maudEvent2Seen = True

$ banditLeaderFriend = 0
$ banditLeaderFear = 0

scene bg45 with fade

"No time was wasted upon his return to the slums. A shy, young boy caught his attention early on, and escorted him to where he would be meeting Maud that day."

if knowHandsign == True:
    "It was not the doctor’s house, nor Kesser’s warehouse today. He was led to a ruined building, a burned down stone mansion, that appeared strangely ancient among the continuously rebuilt wooden shacks around it. "
    
else:
    "It was not the doctor’s house today. He was led to a ruined building, a burned down stone mansion, that appeared strangely ancient among the continuously rebuilt wooden shacks around it. "

show rowan hood shock at edgeleft with moveinleft

ro "What is this place… "

"It didn’t take him long to deduce there was some significance to it. Any other building would be long stripped for materials, or built upon, the marbled floor becoming foundation to a yet another whorehouse or illicit gambling den."
"And yet this place remained untouched. Devastated by rain and wind, yes, but not by human hand. Being here, Rowan felt like he was trespassing on some sort of holy ground."

show rowan hood neutral at midleft with moveinleft
show maud neutral at midright with dissolve

maud "Neutral territory."

"Maud appeared not long after him, Kesser and Calhoun by her sides. The larger man had a large ax by his side and came dressed in chainmail, while Calhoun abandoned his hidden daggers for a more straightforward belt full of throwing knives."
"Maud herself looked no different, but then again, she always looked like she was ready to kill." 

ro "I feel like there’s more to the story."

"Maud tilted her head, either knowing not of it, or caring not to share it. Calhoun, on the other hand, was quick to pick up the topic. He spread his arms wide and twirled around as he went past the empty halls."

calh "Of course there is! This, dear Rowan, is a temple to apathy! The grand sign of submission! The gravestone to deviance! The- ouch! "

"Kesser stopped his tirade with a quick jab to the shoulder. Unlike Calhoun’s callous behaviour and Maud’s utter indifference, he seemed to almost cave from the ruin’s heavy atmosphere."

kesser "T’ was home to the cunt who used to rule the slums, ova’ a century ago"
kesser "Stories say he sold his soul to Kharos. Tried to take ova’ Rastedel when the Baron was away, fighting demons."

"Calhoun casually kicked a lone rock. It ricocheted against the walls, the hollow sound resounding across the halls. "

ro "Obviously he failed."

maud "Yes."

show rowan hood shock at midleft with dissolve

maud "And Prothea purged the slums in retribution."

"She added nothing more, and instead drew her blade to inspected the sharpness of it. Unnerved, Rowan took a moment to examine his surroundings."
"Now that he thought of it, while the city itself was built several centuries ago, and many buildings in it have shown the wear of time. But nothing in the slums seemed to be older than a few decades."

show rowan hood concerned at midleft with dissolve

"A cold wind passed by."

ro "Surely they wouldn’t-"

"A sharp sound cut him off while Maud sheathed her sword again."

show rowan hood neutral at midleft with dissolve

maud "You can talk history later. We have business to settle."
maud "You want my help? I promised I’ll listen. But if you want to fix anything, it starts here."
maud "There’s someone causing trouble. We will deal with them today."

show rowan hood angry at midleft with dissolve

ro "So what is this? An execution? "

"His eyes went to the handle of her sword. Maud still held it, and as if only now realizing it, tore her hand away."

maud "No. Not if they’ll submit. They’ll get a chance."
maud "Everybody gets a chance."

hide maud with dissolve
show rowan hood neutral at center with moveinleft

"She turned away, for some reason hiding her expression. Meanwhile, Calhoun wrapped his arm around the hero, his wide smile taking an ugly turn."

calh "You should drop the cape. We don’t really have running water to help clean you up afterwards, and I imagine dripping blood is not in fashion at the palace. "

show rowan necklace angry at center with dissolve

calh "Well, at least not for a couple of weeks yet. I think. Funny, there’s so little we know about orc fashion…."

"Rowan tried not to roll his eyes, doing his best to hide his displeasure, both at Calhoun’s ill-timed remarks, and at the general turn of events. A gang war was the last thing he wanted to involve himself in, but it would be a small price to pay for getting Maud’s ear."

show rowan necklace neutral at center with dissolve

if alainEvent2Seen == True:
    "And even if he decides against using her, it wouldn’t hurt to remove any lingering uncertainties within the slums before Alain raids the place."

"They didn’t have to wait long for the opposing party to arrive. Rowan observed as six men walked into the ruins, led a man in plate armor, his face covered by the heavy helmet."

show rowan necklace neutral at midright with moveoutright
show rosarian knight neutral at midleft with dissolve

"He held his head high and walked with confidence. Something his men did not share."

kesser "Oi, we agreed on four people each."

banditl "Last time we talked I had my arm broken in two places. These people are my insurance."

show rowan necklace shock at edgeright with moveoutright
show rosarian knight neutral at edgeleft with moveoutleft
#maud angry
show maud neutral at center with dissolve

maud "You mauled an innocent girl half dead! You’re lucky I let you keep it!"

show rowan necklace neutral at edgeright with dissolve

"Maud’s hiss was enough to make several men take a step back, hands nervously seeking swords. Their leader was the only one to keep his cool."

banditl "She was a whore and a traitor to us all. She deserved worse."
banditl "… But I imagine present company won’t agree."

if slumThugsKilled == True and slumsInterrogatorKilled == False:
    "Their attention turned to Rowan. One of the men - green ribbon around his arm - leaned in to whisper something to his boss, his eyes full of fear."
    $ banditLeaderFear += 1
    
elif slumsEvent1Seen == True and slumThugsKilled == False:
    "Their attention turned to Rowan. One of the men - green ribbon around his arm - leaned in to whisper something to his boss, his eyes full of concern."
    $ banditLeaderFear += 1
    

elif slumThugsKilled == True and slumsInterrogatorKilled == True:
    $ banditLeaderFear += 1

else:
    pass
    
#maud neutral
show maud neutral at edgeright with moveoutright
show rowan necklace neutral at center with moveinright


banditl "Rowan Blackwell. Finally gracing us with his attention. Have you grown bored of rubbing shoulders with the perfumed elite?"

ro "I was wondering when someone would make a remark of the kind."

show rowan necklace angry at center with dissolve

banditl "Make no mistake, they’re all thinking it. They’re just too afraid to say anything."

show rowan necklace neutral at center with dissolve

kesser "Just as they’re too afraid to find ya waiting for ‘em in a dark alley?"

"That got a reaction from the man - he raised his finger accusingly at Kesser, like a weapon, and his tone took a hostile turn."

banditl "Don’t you try and paint me as some sort of a thug! What I did was right! Sleeping with nobility is treason to the slums!"
banditl "Nobility doesn’t care about us! It’s us against them, always has been that way! And someone who parts her legs for gold and pretty trinkets while we suffer doesn’t deserve compassion!"

"Rowan threw Maud a short look. The diminutive warrior kept clenching and unclenching her right hand, still cautious to keep it away from anything she might kill the man with. "

banditl "You know this Rowan! Don’t pretend it’s otherwise!"

menu:
    "He’s right. They do need to stand together.":
        $ released_fix_rollback()
        ro "... It’s difficult to disagree, with all the outer slums turned to ashes."
        #maud angry
        "Maud shot him a hostile look, and Rowan had to raise his hands in self-defense, lest she murdered him with her bare hands."
        ro "That doesn’t mean I approve of what he’s done. But I told you the situation is difficult. And I’ve long given up on making nobility see reason."
        maud "… Violence breeds violence."
        maud "You’re too quick to it."
        $ banditLeaderFriend += 1
        $ maudFaith -= 1
        
    "He’s not entirely wrong.":
        $ released_fix_rollback()
        ro "… Some nobles do care. Even if many do not."
        show rowan necklace concerned at center with dissolve
        calh "What a sophisticated answer."
        if rastAlly != "jacques":
            ro "What do you want me to say? Werden’s trying to save the city, but step one of that was burning the entire outer slums."
        else:
            "What do you want me to say? Jacques is doing what he can to help out, but I’d be a fool to believe he’s doing it out of the goodness of his heart."
        ro "I can’t rely on the nobility to do what’s right, even if some of them aren’t indifferent."
        ro "But if my future allies are going to be wasting their time beating women as terror tactics, then I can’t rely on them either."
        #diplomacy check 5 - TODO
        #pass
        "At least one man looked away, ashamed. The leader’s reaction remained obscured by the helmet, but Rowan had hoped it struck a nerve."
        $ banditLeaderFriend += 1
        #fail
            #pass
        maud "… Violence breeds violence. And he’s too quick to it."
        show rowan necklace neutral at center with dissolve
        
    "That’s no reason to dish out vigilante justice.":
        ro "Even if that were true, then who made you judge, jury and executioner?"
        show rowan necklace concerned at center with dissolve
        banditl "I do what I must- "
        show rowan necklace concerned at midleft with moveoutleft
        ro "Don’t you fucking dare play the troubled hero. Not when you’re standing before the real deal."
        #diplomacy check 5 - TODO
        #pass
        "The men shuffled around nervously. Their leader remained unmoved, and with the heavy helmet hiding his face, it was impossible to say what his thoughts were."
        $ banditLeaderFear += 1
        #fail
            #pass
        
        show rowan necklace concerned at center with moveinleft
        banditl "... I’m not any worse than Maud."
        maud "There are rules. You’re too quick to violence."
        maud "And violence breeds violence."
        show rowan necklace neutral at center with dissolve
        
#maud angry

"Rowan saw her grit her teeth. The Bandit Leader had to notice it too, as he lowered his hand, bringing it closer to the sword by his side."

maud "She was just trying to save up money. For her kids."
maud "She sold all his gifts."
maud "And you took that gold and bought yourself a suit of armour. "

banditl "It’s poetic justice."

#maud angry
show maud neutral at midright with moveinright
show rowan necklace neutral at edgeright with moveoutright

maud "There’s nothing poetic about her children begging for food on the streets!"

banditl "They’re one of many! No reason for hers to be special!"

maud "No reason for them to suffer either!"

"The situation quickly began to spiral out of control. He saw Maud’s fingers twitch, and knew she was just moments away from killing the man."

menu:
    "Try to defuse the situation using common interests.":
        $ released_fix_rollback()
        $ banditLeaderFriend += 1
        show rowan necklace neutral at center with moveinright
        #maud concerned
        show maud neutral at edgeright with moveoutright
        "Standing between two people ready to slash each other’s throats was never a wise idea, but jumping headfirst into danger was something Rowan had to practice often - even if he never enjoyed it."
        ro "Both of you, remember where you are. This is supposed to be a neutral ground, no?"
        "He turned to the bandit leader. Did that man have a name? He didn’t ask, and it was too late to do so now."
        show rowan necklace neutral at midleft with moveoutleft
        ro "Look, I’ll give you the benefit of the doubt, and assume whatever your intentions are, they’re good ones. But you’re not going to get many allies by hurting the very people you’re trying to protect."
        show rowan necklace neutral at midright with moveoutright
        #bluff check - easy TO DO
        #pass
        ro "And Maud, you know how things look. It’s no surprise people are getting restless, and not all of them share your self-restraint."
        #fail
            #ro "And Maud, you know how things look. It’s no surprise people are getting restless, and not all of them share your… Self-restraint?"
            #"Calhoun coughed in the background, and Rowan thought he heard him mutter “Smooth” under his breath."
        maud "That’s no excuse for what he’s done."
        ro " No, probably not. But soon enough, the situation is going to turn from bad to worse. We’re going to need all the people we can get."
        "Angry silence was all he got from her, but that was a major improvement from the murderous glare before. He turned to the man again."
        show rowan necklace neutral at center with moveinright
        ro "Besides, I could use men with conviction. Our interests align, even if you might not see it yet."
        ro "Do you think you can stomach working under Maud for a while?"
        banditl "..."
        jump maud2Outcome
    
    "Make the bandit realize how precarious the situation is.":
        $ released_fix_rollback()
        $ banditLeaderFear += 1
        show rowan necklace neutral at center with moveinright
        show maud neutral at edgeright with moveoutright
        "He put his hand in front of Maud, hoping she won’t just break it once she decides to just go for the jugular, and addressed the man. He threw first him, then the people around him, a pitying look."
        show rowan necklace concerned at center with dissolve
        ro "Look, I’m going to say what everybody else is too polite to say. If this is the elite “guard” you took to a meeting with Maud, then I dread to think how the rest of your supporters look."
        "Some of them looked outraged at the remark. The rest was smart enough to not show how deep his words cut."
        ro "What the hell are you even thinking? Do you have any idea what forces are at play here? Not just the Bannermen. Even if you somehow manage to kill everyone here, there’s also Alain and his city guard to deal with."
        ro "And Duke Werden. And the High Arbitron. And Solansia knows how many other people who’ve been at this game for years now."
        ro "I’m no stranger to asymmetric warfare, so believe me when I say: you don’t stand a chance. So bend the knee already, before you hurt your cause any further."
        banditl "..."
        jump maud2Outcome
        
    "Let Maud kill him. ":
        $ released_fix_rollback()
        jump maud2Battle
        
label maud2Outcome:

if banditLeaderFear > 2 or banditLeaderFriend > 2:
    show rowan necklace happy at center with dissolve
    #maud neutral
    banditl "… Very well."
    "Kesser breathed a sigh of relief, and he was not the only one to do so, despite the look of disappointment in some."
    if banditLeaderFear > 2:
        banditl "If I and my men are to die, I’d rather we do so fighting orcs. That way once I’m dead I’ll at least get the chance to spit Solansia right in the face."
    else:
        banditl "If you’re here, then it’s obvious something bigger is going on, something I know nothing about. So fine, I’ll work for Maud."
        banditl "But I don’t like it. I don’t approve of it, and like hell am I going to keep doing so once this is all over."
    maud "All I ask of you, is that you don’t take from those who already have next to nothing."
    show rowan necklace neutral at center with dissolve
    maud "And don’t attract unwanted attention from the church and guard."
    ro "And do as ordered when the time is right."
    if banditLeaderFear > 2:
        banditl "Yeah, yeah, I’ll be a good dog. But don’t think this is over Maud."
        calh "How about we all focus on not dying for the time being, eh?"
        hide rosarian knight with moveoutleft
        "The man growled and stormed off without another word. Calhoun and Kesser hurried after him, informing Maud they’d make sure to familiarize them with the order of things."
    else:
        banditl "Yeah, yeah, I’ll be a good dog. Unbelievable…"
        hide rosarian knight with moveoutleft
        "The man threw his hands in the end and turned around, muttering curses as he left with his group. Calhoun and Kesser hurried after him, informing Maud they’d make sure to familiarize them with the order of things."
    $ banditLeaderJoined = True
    jump maud2Ending

if banditLeaderFear == 2 or banditLeaderFriend == 2:
    banditl "… If the choice is to either submit and serve a cause I do not believe in, or to see my men killed because of misplaced pride..."
    "His hands went to the heavy helmet. He took it off, revealing a face far too young to belong to a scoundrel, and tossed it under Maud’s feet."
    banditl "Then I refuse to make a choice."
    banditl "I’ll leave. And leave your hands clean. That’s what you always wanted, no?"
    "For a moment, Rowan thought this wouldn’t be enough - that Maud would pass sentence she had long decided upon."
    "Instead, he saw her looking over the man’s shoulder, staring into seemingly nothing in particular, her expression carefully neutral. If she was displeased by the result, she didn’t show it."
    maud "Be out of town before sunrise. If your men cause any more trouble, I will show them no mercy."
    banditl "Fuck you."
    hide rosarian knight with moveoutleft
    "Those were his parting words, as he and his men began to left. Calhoun and Kesser went with them, to make sure he would follow through with his promise."
    "Leaving Rowan alone with the Bannermen leader. Finally."
    $ banditLeaderExile = True
    jump maud2Ending

else:
    show rowan necklace angry at center with dissolve
    banditl "… Fancy words are no substitute for principles."
    jump maud2Battle
    
label maud2Battle:

$ maud2Battle = True

show maud neutral at center with moveinright
show rowan necklace shock at edgeright with moveoutright

show bg45 with sshake
show bg45 with redflash

"The armored man managed to get his sword halfway out of the scabbard before Maud’s own sung, cutting through the air with a flash. Blood splattered everywhere as she slit the man’s throat open, easily finding the narrow opening between his helmet and the breastplate."

hide rosarian knight with dissolve

show maud neutral at midleft with moveoutleft
show rowan necklace neutral at midright with moveoutright

show bg45 with sshake

"Things moved quickly. Rowan drew his own blade, and embed it in some unfortunate man’s chest. Another fell, right next to him, a knife between his eyes, and yet another had his skull split open with an axe."
"It was not a fight, it was a slaughter. The remaining men all lost their lives before their leader could even hit the floor."

maud "… I warned you."

"The armored man still breathed - or at least tried to. He fell to his knees, his hands desperately wrapped around his throat, trying to stop the bleeding. It was a moot effort. Before the minute would pass, he would lay dead."

maud "You should’ve listened."

#maud sad
show maud neutral at center with moveinleft
show rowan necklace neutral at edgeright with moveoutright

"Maud stepped up and grabbed him by the helmet. She pushed his head forward, and either out of mercy or rage,  forced her blade right into the back of his neck, finishing what her first strike started."

#maud concerned

calh "No use for a moral spine when you lack a literal one, ha!"

"Three sets of eyes threw the four-fingered man an unpleasant look, to which Calhoun shrugged his arms asking “What?”."

maud "… Clean this up."

$ banditLeaderDead = True

label maud2Ending:

#maud concerned
show maud neutral at midright with moveoutright
show rowan necklace neutral at midleft with moveinright

if maud2Battle == True:
    "Exhausted, Maud sat down on a part of a ruined wall, while Kesser and Calhoun dragged the bodies outside. The fight was short and quick, and yet she looked no better than most men after a daylong battle."
else:
    "Exhausted, Maud sat down on a part of a ruined wall. The whole meeting lasted no more than a quarter of an hour, but she like she just fought a battle from dawn till break."
    
show rowan necklace concerned at midleft with dissolve

ro "Are you okay?"

if maud2Battle == True:
    "She stared at the tip of her bloodied sword, her head low. Drops of blood still dripped down from it, further staining the marble floor."
    maud "… He was a good kid."
    maud "Couldn’t let him go around doing as he pleased."
    
else:
    "She didn’t respond at first. She rubbed the pommel of her sword with her thumb, lost in thought before realizing what she’s been doing and tearing her hand away."
    maud "… He’s not a bad kid."
    maud "But there are rules. You’ve got to follow the rules."
    maud "Or else everyone suffers."


show rowan necklace neutral at midleft with dissolve

ro "So what was this all about? You didn’t really need my help, did you? "

if maud2Battle == False:
    #maud happy
    maud "Maybe I did."
    $ maudFaith += 1
    #maud neutral
    maud "Or maybe just I wanted to see what a true hero looks like."
    
else:
    #maud concerned
    maud "No. Not for that."
    maud "Maybe I just wanted to see what a true hero looks like. "

if beggarHighCorEnd == True:
    #maud angry
    maud "Since you didn’t leave a good impression at the start."
    $ maudFaith -= 1

#maud neutral

maud "You did as was requested. I promised I’d listen. "
maud "What do you need, Rowan Blackwell? "

"With everybody gone, she didn’t seem to see the need to raise her voice anymore. She spoke quietly, and didn’t even look at him as she did. Not that her eyes ever told him anything."

ro "… I need someone to take the northern gate for me. It has to be quick and quiet. There’s no room for error. "

maud "Alarie keeps a small contingent there. It will not be a problem. Anything else?"

ro "I will need a distraction. A… District-wide one."
ro "You don’t have to worry about the people here. Nobody’s going to have the time to move against you. And by the time this is all over, you’ll sit at the same table as the victors."

"Along with a man as red as blood and a taste to shed it, and a woman with wicked horns and a wicked smile. But she needn’t know that."

maud "… You ask a lot."

"Maud did not raise her head as she answered." 
"… And the silence that followed after her words grew more deafening by the seconds. "

show rowan necklace shock at midleft with dissolve

maud "You want to destroy the very order that stands between us and the orcs."

show rowan necklace concerned at midleft with dissolve

ro "They can’t save us!"
ro "They can’t protect Rastedel or anybody here-"

show rowan necklace neutral at midleft with dissolve

"He forced himself to calm down. Maud’s remark hit too close to home. For a moment he feared she knew more than she let on. But that couldn’t be the case. Couldn’t."

ro "Maud, you must understand. You don’t know the full extent of the decay there."

maud "So you say."
maud "As did others before you."

#maud happy

"She leaned back, and finally raised her head as she looked to the sky. For a moment, a shadow of a smile danced on her lips. She opened them to say something, only to decide against it at the last moment."

maud "… Ha."

#maud angry

"She snapped her head to him, and just like that all the fury and rage returned, like they were never gone."

show rowan necklace shock at midleft with dissolve

maud "I will see it myself first."

ro "What?"

maud "I said I will see it first." 
maud "I want to talk with the Baron."

show rowan necklace concerned at midleft with dissolve

maud "I want to see that decay firsthand."

ro "Maud, I can’t just-"

maud "You can. And you will. I don’t care how."
maud "There are rules. The Bannermen stay neutral."
maud "I will not risk the slums on a word. Not even yours."

show rowan necklace neutral at midleft with dissolve

maud "See it done. Then I will help you."

hide maud with moveoutleft

"There was no room for negotiations. Maud waited to see if he wished to protest any further, then picked her belongings and left the ruin without another word, leaving Rowan alone with his thoughts." 
"Knowing the Baron, he doubted there was any risk of Maud taking any liking of him. And with Amaraine’s help, it shouldn’t be difficult to set up a random meeting somewhere within the palace." 
"So it was only a matter of if. He did not forget the events he witnessed on their first meeting. Maud was volatile, and while he doubted she would betray him, there was no telling how she’ll behave after the coup."

if alainEvent3Seen == True:
    "Alain was ready to strike. All he needed was the right weather and the “go” from Rowan. He would cover his tracks here and secure his support with one simple sweep. If he wished to." 

elif alainEvent2Seen == True: 
    "Alain was willing to help him out. Even now, he could have his guard strike against Maud. He could cover his tracks here and secure Alain’s support with one simple sweep. If he wished to."

elif alainEvent1Seen == True:
    "Compared to her, Alain was much more amicable. And if Rowan helps him take her down, he could gain a much more reliable ally."
    
else:
    "Perhaps there was still time to meet with the captain of the guard. Maud wasn’t his only option here."

scene black with fade

"Regardless of what he wished to do, he should decide soon. Time was running out."

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

##################################################################################
##################################################################################
##################################################################################

label maud_event3:

$ maudEvent3Seen = True

scene bg33 with fade

show rowan necklace neutral at midleft with dissolve
show casimir neutral at midright with dissolve

"For once, things proceeded exactly as planned. With the help of Ameraine and a “mysterious benefactor”, as she called her friend - likely for no other reason than to annoy him with needless secrecy - Rowan put together a simple plan for Maud." 
"A chance meeting, during the baron’s morning stroll in Marianne’s garden at the codifice rooftop. The very same Juliette showed him not long ago. The baron was known to visit it at the break of dawn, before most guests arrive."

#casimir happy

casi "It’s not often that I have company during these walks, Rowan. It’s a pleasant surprise."

"Nobody questioned Rowan’s desire to accompany the most powerful man in Rosaria. Even the handful of guards discreetly lingering in the background barely paid attention to him, yawning whenever they thought he wasn’t looking."

show rowan necklace happy at midleft with dissolve

ro "I imagine they understand his majesty needs some time to himself to contemplate. Or perhaps they find gardens a poor place for politicking?"

casi "A shame. I always believed flowers soothe even the most violent of tempers. It is a good place to seek compromise."

show rowan necklace neutral at midleft with dissolve

"He stopped by a short tree with indigo flowers Rowan couldn’t recognize. Not far away, a young pair came out of a side alley, hands held. Seeing them, the man scoffed, and quickly turned his lover around."

if avatar.corruption > 50:
    #casimir neutral
    casi "I do not believe flowers would be of much help with what is to come."
    ro "No, I suppose not."
    "A soft sigh escaped the Baron’s lips. Rowan discreetly led them down a different path, so they wouldn’t stumble upon the pair."
    
else:
    ro "Perhaps if we gathered all the discontent nobles here, we might be able to ease the tensions a little."
    casi "Maybe so, maybe so."
    show rowan necklace happy at midleft with dissolve
    ro "Or perhaps all we would accomplish is trample over her Beatitude’s flowers."
    "A soft smile graced the man’s lips. Rowan discreetly led them down a different path, so they wouldn’t stumble upon the pair."
    show rowan necklace neutral at midleft with dissolve
    
"Where the hell was Maud? She said she would meet them here, and that she would arrange for a disguise herself."  
"Knowing her, Rowan imagined she’d handle it with the same efficiency she handled everything else, but quietly hoped it would not involve any bone breaking."

casi "Do tell Rowan, how are the preparations coming along?"

ro "They’re going well, your majesty. I was handling some internal matters recently, in the northern side of the city. Wouldn’t want to be blindsided by them once the orcs arrive."

show rowan necklace shock at midleft with dissolve

casi "Ah, have you by any chance met Captain Alarie? Charming young man. Marianne introduced me to him a while ago. She thought he showed much promise."

if alainEvent1Seen == True:
    show rowan necklace neutral at midleft with dissolve
    ro "I had. He… Leaves quite the impression. I almost went blind from the smile."
    casi "Indeed. She said the guard would need that light. That we all would, one day."
    
else:
    show rowan necklace neutral at midleft with dissolve
    ro "I do not believe so. Perhaps I wasn’t introduced by name?"
    casi "Hmm… Perhaps. He leaves quite the impression though. I think you’d recall if you had met him.  "

"Rowan kept a polite smile, but now he was searching for the slums leader anxiously. He shouldn’t have allowed the conversation to go that way, but the Baron’s usual absentmindedness lowered his guard."

ro "So what convinced Marianne to build this garden? "

#casimir happy

casi "Ah. A good question. Best directed at her, I think."
casi "I know to Protheans, Rastedel can be, hm, crude."
casi "But she never saw it that way."
casi "She used to travel a lot, when she first came here. Around the countryside. "
casi "She’d gather wilting or sickened flowers, and bring them here. So they could bloom again. "
casi "Planted many herself. Later, I helped with some." 

"The baron knelt beside a patch of soft blue hyacinths, currently attended to by a gardener."

casi "These have always been my favourite. I see you’ve been taking good care of them."

show rowan necklace shock at midleft with dissolve

maud "Of course, your majesty."

show rowan necklace shock at edgeleft with moveoutleft
#casimir happy
show casimir neutral at center with moveinright
show maud neutral at edgeright with moveinright

"Rowan felt his heart skip a beat, as Maud lowered her head before the Baron. With her armor and sword gone, and a wide hat to seemingly shield her eyes from the sun, she looked no different than dozens of faceless workers attending the place."

show rowan necklace neutral at edgeleft with dissolve

"Even the violent ambience was gone, the absence of it so striking, Rowan wondered how he could ever think the woman dangerous."

maud "I don’t like them myself. I see them too often. "

casi "Hm? Then are there some that strike your fancy, young miss?" 

maud "… In a way. "

"She took a few steps into the garden, stepping lightly as to not thread on anything delicate. Rowan watched as she knelt by a bed of dozens spectacular, funnel-shaped flowers, each a different colour."

casi "Ah, that’s… Hm, the name escapes me."

#if rowan has wildnerness survival 1 - TO DO
ro "The Gladiolus, your majesty. Also known as the Sword Lily."

#else:
    #maud "Sword Lilies. "

casi "Ah, yes, exactly! Marianne fancies them herself."

maud "… I see."
maud "They’re the first flowers I ever took care of."
maud "A young girl gave them to me. She said they fit me."

"Her hand went to the back of her head, and she touched her green-dyed hair, lost in thought."

maud "We planted many. Couldn’t make mine grow."
maud "But I tried to take care of hers, after she was gone."

"The Baron offered a few compassionate words Rowan didn’t listen to, as he eyed the faraway guards. He hoped whatever it was Maud wished to accomplish here, she would be quick about it."

show maud neutral at midright with moveinright
show casimir shocked at center with dissolve

"A quiet snap caught his attention. Maud picked up a single, red flower, and turned it in her fingers. Then, breaking all protocol, she placed it behind the baron’s sash. "

show maud neutral at edgeright with moveoutright
show casimir neutral at center with dissolve

maud "… I was ten when I came to Rastedel."
maud "The thing I remember most about that day… Was how bright the dresses were."

#maud happy

maud "They looked so light. So beautiful."

#maud neutral

maud "I couldn’t help but envy them. And I thought…" 
maud "“Surely the Baron would be the most majestic of them all?”"

show rowan necklace concerned at edgeleft with dissolve

"Her lip twitched, its corner rising to form a grotesque smile for a split second. Rowan noticed her fingers digging into her own arms, something the Baron remained oblivious to.  "

show rowan necklace neutral at edgeleft with dissolve

maud "I didn’t see his Lordship until much later."
maud "Until the day you came back from the war."

show casimir sad at center with dissolve

maud "Do you remember that day, your majesty? Do you remember the parade?"

casi " …Yes, of course."

"The Baron furrowed his eyebrows, obviously trying to recall the event. With little success."

casi "Weren’t you a part of it too, Rowan? "

ro " Indeed I was. We were marching south with Duke Werden and his knights, and a handful of Prothean priests. I’m afraid I can’t recall the names."

"But he did recall the Baron wasn’t part of the campaign. He joined them on their way back, priests in tow, and led the procession as they entered the city."

ro "People swarmed to the streets, cheering as we went past. I could barely hear my own thoughts."

#baron happy
show casimir neutral at center with dissolve

casi "There were red petals in the air, no? "

ro "I think some of the people threw them from the windows."

maud "Yes. They gave them away at the main square."

"Casimir played with the gifted flower, his gaze as distant as ever. He didn’t notice the burning intensity that hid in Maud’s dark eyes, nor the tension in her voice."

maud "I was watching it from the rooftops. Me and Roderick."

casi "Someone dear to you?"

maud "…Yes. In a way."
maud "We waited all day to see you."
maud "I still remember the golden laurels shining in the sun. The flowing red cape, and the rose etched into the gold-adorned armour." 
maud "I even remember the white horse, so meticulously groomed to look its best."
maud "And I remember you, your Majesty."
maud "And I remember thinking…"

show rowan necklace shock at edgeleft with dissolve
show casimir sad at center with dissolve

maud "“Solansia help me, I’ve never seen a man more defeated.” "

show rowan necklace neutral at edgeleft with dissolve

"Casimir’s fingers froze, and the red flower with them. Any other noble would be outraged, but the Baron seemed to struggle not to turn his head away in shame."

show rowan necklace concerned at edgeleft with dissolve

maud "You looked so tired. Hunched over your horse. You’d rise to wave at the crowd, but could never do so for longer than a few moments." 

show rowan necklace neutral at edgeleft with dissolve

maud "And as you were about to pass me by, I remember thinking, for the first time in years-"
maud "“Maybe it will all turn out okay.” "

#maud happy

"A bright, hopeful smile went past her face, so quickly Rowan wasn’t sure if his eyes didn’t deceive him."

#maud neutral

maud "“Maybe now we’ll have someone who understands how it feels to lose everything.”"
maud "“Maybe now we’ll have someone to look after us.”"
maud "“Maybe now someone will care.”"
maud "“Maybe now….”"
maud "Maybe now..."
maud "..."
maud "What happened, your majesty?"

#maud angry

"She always hid it so well, but now the bitterness in her tone ran so deep, Rowan could only imagine the full depth of it. Even the Baron felt it. He no longer dared to look at the girl, his gaze fixed on the bright flowers around them. "

show rowan necklace concerned at edgeleft with dissolve

"The hero wondered how many were planted for the fallen prince. Too many. Far too many."

show rowan necklace neutral at edgeleft with dissolve

"The silence dragged on, but Maud would not be denied. Her eyes were still fixed on the Baron, and her question hung in the air stubbornly, demanding to be answered."

#maud shocked

casi "… Surely it hasn’t been all that bad, has it?"

#maud neutral

casi "There was… Hmm… Lady Crevette had this… Public works project, I think? A few years back. She was really proud of it, I believe."
casi "And I did approve more funding to the Selestine Sisters, did I not?"

#if rowan dis simone event - TO DO
#"The Baron turned to Rowan for confirmation."
#ro "Simone did mention something of the kind."
#casi "Ah, good, good. "

#else
"The Baron turned to Rowan for confirmation, but the hero shrugged. How could he know? "

casi "And... Hmm… I can’t recall. But there had to be something." 

#maud angry

casi "Maybe I should talk with Marianne about-"

show rowan necklace shock at edgeleft with dissolve
show casimir shocked at center with dissolve

maud "Marianne doesn’t wield the scepter!"

show casimir sad at edgeleft with moveoutleft
show rowan necklace neutral at midright with moveinright

"Casimir recoiled from the hostile hiss. He looked to the guards, and Rowan seized Maud by the arm before the situation could spiral out of control.  "

maud "You’re the Baron! It’s your job-"

ro "Enough!"
ro "I apologize your Majesty. I’ll escort this troubled young woman out and make sure her foot never graces her Beatitude’s garden ever again. Please, try to enjoy your walk."

"Too stunned to answer, the baron gave a short nod as Rowan dragged Maud out."

hide rowan with moveoutright
hide maud with moveoutright
show casimir sad at center with moveinleft

"She did not struggle, but she did keep looking back, her eyes shooting daggers at Lord of the realm."

scene black with fade
"..."

scene bg33 with fade
#maud angry
show maud neutral at midright with dissolve
show rowan necklace angry at midleft with dissolve

ro "What the hell were you thinking!"  

#maud angry
show maud neutral at edgeright with moveoutleft

"Maud wrenched her arm away as soon as they walked out into the main square. She hissed again, and began pushing through the crowd, shoving people away with surprising force."

maud "Getting answers."

ro "And you got them. Satisfied now?"

maud "Yes. No. Fuck, I don’t know. "

"She snarled, making a random merchant jump out of her way. Rowan followed a few steps behind, to make sure she wouldn’t do anything stupid before she could fulfill her end of the deal."

maud "I need to think. I -"

#maud neutral

"She stopped suddenly, then turned right sharply."

"Moving quickly enough to almost force Rowan into a jog, Maud stormed through the northern main road, the same one that led through the slums. But before they could enter her home turf, she took a quick turn to one of the back alleys."

show rowan necklace neutral at midleft with dissolve

maud "He looks no better than eight years ago."

"Her eyes studied the wall on her left, before quickly jumping on crates to her right."

maud "How?"

hide maud with moveoutleft

show rowan necklace neutral at center with moveinleft

"She didn’t expect an answer, and Rowan could give her none that wouldn’t be met with an angry bark. With another jump, she grabbed the edge of the roof, and pulled herself up to it."

hide rowan with moveoutleft

"Grumbling at the unexpected exercise, Rowan followed, using his climbing expertise where agility failed him."
"… The building was not tall, but it was just high enough to allow for an unobstructed view of their city. The surrounding buildings all blended together, their roofs creating a mismatched, brown carpet."   
"Behind them, the Basilica stood, as grand as ever. In front of them, he could see the northern mountains looming in the distance, behind the tall walls that looked so feeble in comparison." 

#maud angry
show maud neutral at edgeleft with dissolve
show rowan necklace angry at edgeright with dissolve

"In the bright afternoon light, and under the crystal blue sky, the view might have been seen as delightful. But it did nothing to soothe Maud’s anger. The short woman had her back to him now, her gaze focused north." 
"Focused on the northern gate, and the long, straight track leading out of it."

maud "… The petals. The cheers. The column of knights."
maud "It was just as you said. I can still see them. "
maud "They made me want to puke."

#maud angry
show maud neutral at midleft with moveinleft

"She took a step back, and started to experimentally tap the wooden tiles that made the slightly steep rooftop. One of them jumped loose suddenly, as if it wasn’t fixed at all."

show rowan necklace concerned at edgeright with dissolve

"Rowan watched her remove a few more, and kneel beside the unexpected compartment, taking something out of it. It took him a few long moments, before his eyes recognized the wooden construction. He swallowed heavily."

#maud neutral

"Ten years ago, it would have been top-grade military equipment. But years of rain turned what once was a heavy crossbow into a rotten mess, almost falling apart in Maud’s arms."

show rowan necklace neutral at edgeright with dissolve

ro "Not just watching the procession, then?"

"Maud didn’t answer. Her fingers ran across the ruined weapon with a tenderness he didn’t suspect she was capable of. All of her anger seemed to vanish into thin air, and when she spoke again, her voice was heavy with long-held anguish."

maud "I lost my brother in the war. Under the walls of Karst."
maud "Nothing you’re responsible for. He died in the first battle, I was told."
maud "For months, I hoped that maybe he was still inside the keep. But news came about Werden breaking the siege and I -"
maud "I didn’t hope for anything afterwards."

"A tale shared by hundreds, if not thousands. Names changed, but the story stayed the same."

#OR guilt is high - TODO
if avatar.corruption < 50:
    show rowan necklace concerned at edgeright with dissolve
    ro "I’m sorry, I-"
    maud "Don’t."
    "She didn’t let him say the words, but for once, her tone had no edge in it."
    show rowan necklace neutral at edgeright with dissolve

else:
    "By now, Rowan had grown numb to them." 

maud "I met Roderick some time later."

"She played with the broken bowstring for a moment, reminiscing."

maud "Roderick lost people too. But he… He had a vision. A dream."

show rowan necklace shock at edgeright with dissolve

maud "A dream of the palace running red with blood. A dream of Rastedel in flames."

show maud neutral at edgeleft with moveoutleft
show rowan necklace neutral at edgeright with dissolve

"She brought the crossbow to her eyes, and pointed it at the streets. The low steep obscured them both, allowing for an easy shot, especially at a lone man atop a massive horse."

ro "Sounds more like a nightmare."

maud "It wasn’t to us."
maud "... So stupid. There was never more than thirty of us. But we wanted blood. And we would have it."
maud "It was supposed to be our grand day. I was Roderick’s right hand. I was given the honor of starting it all." 

#maud sad

ro "But you changed your mind at the last moment. When you saw Casimir."

maud "Yes. There had been enough suffering."
maud "Causing pain is no way to honour the dead."

"She brought the crossbow down, and stared at the slums with a faraway gaze. When she spoke up again, it was in a nearly inaudible whisper."

maud "Not everyone agreed."

"She didn’t elaborate, but she didn’t need to. Rowan could see into the uncovered compartment. An old rusty sword was tucked away inside, next to a simple leather quiver, its lid open wide."
"He counted nineteen bolts inside. "

ro "We all make sacrifices to protect what’s important to us."

"She didn’t answer, still staring at the slums solemnly. Reminiscing, no doubt. About the people lost. About the people she failed to protect. About -"

#maud happy
show rowan necklace shock at edgeright with dissolve

maud "… Hah."

"About something incredibly entertaining, apparently. "

ro "What’s so funny?"

show rowan necklace neutral at edgeright with dissolve

maud "The sign over there. Over that Inn. See it?"

show rowan necklace neutral at midleft with moveinright

"She pointed with the tip of the crossbow, and Rowan had to strain his eyes to make out the image on it. A crude drawing of an angry, mustached man was painted over what once had to be a very intricate depiction of a nubile elf girl."

maud "“The raving prick.” Used to be “Enchanting Nymph.”"
maud "The owner takes in orphans as helpers. Feeds them. Clothes them. Instructs them how to cook, clean and take care of a horse."
maud "Complains a lot, and always throws them out after a year, saying they’re worthless."

ro "After teaching them everything they needed to know."

maud "Yes."
maud "Some angry kids did this to him two years ago."
maud "Never shuts up about it."
maud "Yet he still takes in new ones."

"A soft smile danced on her lips as she held the crossbow close to her heart. It seemed far too heavy for her to carry. For anyone, really."

#maud neutral

maud "… I don’t regret it. It was not wasted time." 

show maud neutral at midright with moveinright 
show rowan necklace shock at midleft with dissolve

"She turned around, looking at the alley behind them. She clutched the crossbow for a little longer, then tossed it off the roof, so casually Rowan couldn’t believe this was a weapon that almost killed the Baron of Rosaria."

maud "And there is no use looking to the past."
maud "It wasn’t perfect. These last few years. But it was better than death. Better than orcs."
maud "... But I can’t keep waiting for someone else to make it better."

if avatar.corruption < 60:
    show rowan necklace happy at midleft with dissolve
    "He smiled, and waited for Maud to finish talking herself into a decision she has already made. He feared her violent tendencies could be a problem, but perhaps he misjudged her."
    show rowan necklace shock at midleft with dissolve
    "And yet it still caught him off guard when her hand cupped his cheek gently."
    
else:
    show rowan necklace happy at midleft with dissolve
    "Finally. He could feel the woman had long ago made her decision, and now only needed to talk herself into it. Even if he was not unsympathetic to her plight, there were bigger things going on than-"
    show rowan necklace shock at midleft with dissolve
    "Her hand cupped his cheek gently, completely catching him off guard. "

maud "Not when we have you."

show rowan necklace concerned at midleft with dissolve

maud "I know the past months have not been easy for you."
maud "I heard of Arthdale. The fact you’re here, doing this for us…"

#maud happy

maud "Thank you, Rowan. For everything."

if avatar.corruption < 60:
    "Her concern sounded so sincere, and her voice so warm, it almost cut his heart into pieces. So this was what Kesser, Calhoun, and everyone else saw in her. The caring older sister, always there to protect them. "

else:
    "He didn’t do this for them. But she really believed he did. And her concern sounded so genuine, her voice was so warm, it almost made him sorry for using her."  
    "So this was what Kesser, Calhoun, and everyone else saw in her. The caring older sister, always there to protect them." 

show rowan necklace happy at midleft with dissolve
#maud shocked

ro "Can’t allow something as minor as heart-shattering personal tragedy stop us from doing what’s right, can we?"

#maud happy

"His poor attempt at humor made her flash him a short, tired smile."

maud "Yes. No looking back. No more."

show rowan necklace neutral at midleft with dissolve
#maud neutral

maud "So after the coup, what awaits us?" 

menu:
    #add below average guilt to second conditional - TO DO
    "A better world. By his and the twins design." if serveChoice == 4 or avatar.corruption > 50 and avatar.guilt < 50:
        $ released_fix_rollback()
        $ promisedMaudBetterWorld = True
        "He touched her hand as she looked into his eyes. He didn’t know what she saw in his, but he recognized that look. Hope. Long gone, now invited again." 
        "It was not misplaced. Despite the twisted road they both walked, it would not be all for naught."
        show rowan necklace happy at midleft with dissolve
        ro "We bring down Marianne. Lock her away, somewhere far away and secure. Then we deal with the Baron, make sure he won’t oppose anything we do. And once all opposition is dealt with, you’ll start to see... Changes. Real changes."
        if rastAlly != "jacques":
            maud "I hope Werden is willing to compromise-"
        else:
            maud "Jacques seems like the type-"
        #maud shocked
        ro "No. He won’t be making the calls."
        #maud happy
        ro "I will."
        ro "There’s far more at play here than you can imagine. But believe me when I say I did not sacrifice almost everything I ever believed in just to change one noble for another."
        ro "We’re going to make things right Maud."
        "It would be a lie to say the look of shock on her usually indifferent face was not a little satisfying. But the way it slowly turned to a slight grin was almost magical."
        maud "Ah, is that so."
        maud "Then consider me in."
        #maud aroused/embarassed
        "Her hand lingered on his cheek for far longer than it should. Realizing that, she tried to pull it away-"
        jump maudSexChoice
        
    "Another chance at making things right.":
        $ released_fix_rollback()
        "He touched her hand as she looked into his eyes. He didn’t know what she saw in his, but he recognized that look. Hope. Long gone, now invited again." 
        "Perhaps it was not misplaced? Despite all the lies, despite the growing weight on his soul as he came to terms with what was about to come, perhaps it would all turn out for the better."
        ro "We bring down Marianne. Lock her away, somewhere far away and secure. Then we deal with the Baron, make sure he won’t oppose anything we do. And once all opposition is dealt with… We’ll fix things."
        ro "Deal with the Orcs. Deal with Protheans interfering. Start to recognize the people who actually deserve it."
        #maud happy
        ro "We won’t sit on the sidelines as others weave our fate for us."
        "That’s right. He could’ve chosen to rot in his cell for all eternity. Whatever the circumstances now, he chose to be here. And even though Maud’s role was to ensure his Rastedel “allies” couldn’t claim a total victory, she and her people didn’t have to be expendable." 
        "This was a chance for her too. And she saw it too, a slow grin creeping on her face."
        show rowan necklace happy at midleft with dissolve
        maud "Consider me in, then."
        #maud aroused/embarassed
        "Still smiling, she let her hand linger for a moment, far longer than it should. Realizing that, she tried to pull it away-"
        jump maudSexChoice

    "Pain and Misery." if avatar.guilt > 50:
        $ released_fix_rollback()
        $ maudFaith += 2
        $ change_base_stat('g', -3)
        $ promisedMaudPainMisery = True
        "He touched her hand as she looked into his eyes. He didn’t know what she saw in his, but he recognized that look. Hope. One he invited it. Nurtured with every well-timed word and honeyed lie."  
        show rowan necklace concerned at midleft with dissolve
        #maud shocked
        ro "… Don’t look at me like that."
        "And now he couldn’t stand it. Maud’s role was to make sure his allies were weakened enough to surrender to the twins. She was nothing more than an unwitting tool of chaos and destruction."
        "Though perhaps this was better than being a witting one."
        #maud neutral
        ro "I can’t promise you a happy ending. Even if everything goes according to plan, we’ll deal with one problem, and probably invite a hundred more."
        ro "It’s always like that. Always."
        #maud happy
        "Her surprise was clear, but short-lived. And he hated the understanding expression that replaced it even more."
        maud "I know."
        maud "Good thing neither of us is going to quit."
        maud "..."
        maud "..."
        show rowan necklace shock at midleft with dissolve
        #maud neutral
        maud "I’m not very good at this."
        show rowan necklace happy at midleft with dissolve
        "She frowned at herself, dissatisfied with her inept attempt at lifting his spirit, and Rowan almost burst out laughing."
        ro "No, no, concise and to the point. It was perfect, Maud."
        "Here he was, agonizing over his unwilling servitude, and the hardships that still laid ahead. And before him was a woman who for eight years had covered Solansia’s ass, making sure the desperate and destitute wouldn’t shower Marianne with stones."
        "How weak was his own resolve, for it to start breaking a mere year in?"
        #maud happy
        ro "You’re right. We can’t leave a job half-finished."
        ro "I’m glad to have you on my side, Maud."
        #maud aroused/embarassed
        "Still flashed him that quick, dazzling smile he knew she only shared with her inner circle. Her hand lingered on his cheek, far longer than it should. Realizing that, she tried to pull it away-"
        jump maudSexChoice

label maudSexChoice:

menu:
    "Hold it.":
        $ released_fix_rollback()
        jump maudSex
        
    "Let it go.":
        $ released_fix_rollback()
        maud "We should go. There’s much to be done. "
        scene black with fade
        "… … ..."
        jump maudEvent3Ending
        
label maudSex:

$ maudSex = True

"He didn’t let her pull away, and instead wrapped her hand with his own, holding it close to her chest. Something the female warrior obviously didn’t expect, as she almost stumbled on her feet."

#maud happy

"But only for a moment. The corners of her lips twitched upwards, and she steadied herself, leaning against his chest as her other hand touched his body, fingers running against his muscles with appreciation."

maud "It isn’t often that I’m the one who gets moved on."

ro "A terrible loss. Your abashed smile is kind of cute."

maud "… Is that so?"

show bg33 with sshake
hide rowan with dissolve
hide maud with dissolve

"His entire world was turned upside down as she pushed him unexpectedly, hooking his leg to make him lose all balance. He hit the roof hard, causing a ruckus that couldn’t have gone unnoticed."

#cg1 - blurred
scene black with fade
show rowan necklace happy behind black
#maud happy
show maud neutral behind black

"Any words of protest he might have had were silenced as she jumped on top of him, sealing his lips in a passionate kiss. She grabbed him by the wrists - not strong enough to lock him in place, but enough to send a clear message: “don’t struggle”."
"Still surprised, he let her enjoy his lips for several long moments, and felt her hips rubbing against his crotch. Despite her aggressive approach - or maybe thanks to it - he knew she felt him growing hard."
"When she finally broke their kiss, there was a victorious smirk on her face, one tempered by playful sparks in her usually distant eyes."

maud "Yours is too."

ro "Maud, is this really-"

maud "Yes."

"She let go of his hands, and removed her vest in one swift movement. He was greeted with a pair of modest breast, bound by a binder. Her body was lithe and full of scars, but she didn’t seem bothered by them." 
"And as he focused on the hungry look in her eyes, he found out neither was he."

maud "Life’s short. You find happiness when and where you can."

ro "How unexpectedly indulgent."

"She flashed him another happy smile, and her hands went under his shirt. She rolled it up, feasting her eyes on the view before her."

maud "Blame yourself."
maud "I don’t meet many men like you."

if promisedMaudPainMisery == True:
    ro "Brooding, troubled heroes?"
else:
    ro "Legendary heroes, inspiring and valiant?"

"A short snort was her response, as she unceremoniously rid him of all his upper garments."

show rowan necklace naked behind black

maud "Clean. Handsome." 

"She wiggled her hips, feeling his length with her inner thighs. Judging by the approving purr she gave him, they weren’t the only things she appreciated about him."

ro "How insulting, to have my many valours reduced so. "

"He placed his hands on her hips, as Maud’s hands went to her binder. Behind her, he could see the Basilica standing silently, basked in the afternoon light. A silent witness to their little illicit adventure. Marianne would get an aneurysm, if she knew."

maud "You’ll live."

"But all thoughts of the High Arbitron went out of his mind as Maud undid her bra, her small, perky breasts looking charmingly feminine on this otherwise boyish woman. Her nipples pointed out excitedly, in testimony to her growing lust."

maud "Don’t just stare."

"She jumped him again, locking lips. Rowan answered with equal enthusiasm, moving his hands upwards, taking his time feeling Maud’s lithe body - despite the woman’s murmurs of disapproval."

ro "Just because I let you be on top doesn’t mean you can bark orders at me."

"His defiance was met with an indigent huff, and Rowan couldn’t help but laugh as he grabbed her tits, his thumbs flicking her erect nipples, hoping to appease the woman."

maud "Ahh, better."

ro "Next time just ask nicely."

"A quiet “hmph” was his response, as she kissed him again, her nimble tongue forcing his mouth open."  
"With a year of service for the twins under his belt, he met no small number of women who were quick to fuck and eager to indulge. But Maud didn’t feel like them. Her passion ran just as deep, but it wasn’t driven by lust alone."
"He could feel her desire for intimacy in every kiss, whenever her fingers traveled across his body. He felt her want to touch him, appreciate him." 
"And beneath it, the slight unease. The unspoken, unacknowledged fear, that in any moment, in a blink of an eye, all of this might be taken away from her."
"Perhaps in the past, it was." 
"He let her rub against body with abandon, as much as she wanted, until his own desires took the better of him, and he reached for her back, his hands greedily grabbing her slender ass, still criminally covered by a pair of dark pants."
"She got the message, and pulled back, her face flushed with desire." 
"Her pants landed by his head, as she stripped with agility even the finest courtesan would envy." 
"Her pretty pink pussy glistened in the sun, and he feasted his eyes on it. It was decorated with a short bush slightly bigger than he preferred, but that was soon obscured by his cock jumping free." 

ro "Not a fan of the razor, I see. "

maud "How demanding."
maud "I might reconsider. If you perform. "

"She raised her hips, placing the tip of his cock against her wet cunt. She took a moment to run her fingers his full length, and purred as she felt its size and hardness. He could get used to that sound."

maud "Shouldn’t be difficult for you."

"He rushed to grab her hips, only for her to intercept his hands, flashing him a triumphant smile. He knew she wanted to appreciate the sight a bit longer. Admire his chiseled chest, his handsome face."
"So he took the moment to admire her too. He let his eyes take in that athletic body, that now buzzed with aggressive sexuality. She always seemed like she was holding back, all that energy gnawing at her, waiting to find an outlet."
"And she finally had one." 

scene cg679 with fade
show rowan necklace naked behind cg679
#maud naked happy
show maud neutral behind cg679
pause 3

"In a last act of restraint, Maud lowered herself on his dick without hurry, inhaling sharply as his cock spread her tight, moist walls. She took him inch by inch, savoring his length." 
"Until the very last moment, when just as she was about to sit down, Rowan thrust his hips upwards, filling her all the way to the base of his cock." 

maud "___ !"

ro "Nn-ngh! Not even a peep?"

"She answered him with a dark chuckle, a playful spark dancing in her eyes as she rolled her hips, getting herself used to his considerable girth. Her walls squeezed at him greedily, refusing to let go of their new conquest."

maud "If you want a contest… "
maud "Let’s make it one."

scene cg680 with fade
show rowan necklace naked behind cg680
#maud naked happy
show maud neutral behind cg680
pause 3

"She pushed herself upwards, and impaled herself on his cock without a moment of hesitation, lust and pride driving her actions. Rowan hissed, if only to stop himself from moaning."

maud "Whoever cums first, loses."

"There was nothing on the line - nothing to gain, except the satisfaction of showing this cocky girl that Rowan Blackwell was more than a pretty face with a slightly embellished hero story."  
"And seeing her temporarily drop that cocky grin to moan in ecstasy, he realized he wanted nothing more than to make her scream her lungs out, their public location be damned. He tried to grab her thighs again, but she refused to let go of his arms." 
"Instead, she held her breath as she continued to rock her hips in a steady rhythm, sweating from the effort. But that just made the obscene, squelching sound her pussy made whenever his dick slid right into her all the more apparent." 

ro "You make such lewd sounds M-Maud. What would everyone think if they saw you like this? "

maud "They’d be gla~aaaa~ad I’m enjoying myself ~~"

"She redoubled her efforts, picking up tempo, her lithe body rising and falling as she let desire guide her movements. Her modest breast jumped with every thrust, the dazzling sight made even more enchanting by the crystal sky behind them." 
"Whatever he might have to say about her outwards appearance, the passion she rode him with would make any woman beautiful." 

maud "Ha…-Aaa!"

"Sensing a moment of weakness, he thrust his cock upwards, turning her lovely sigh into a cry of pleasure."

maud "Ha- how dirty!"

"He allowed her no respite, driving his cock into her with abandon, forcing the smaller woman to jump on his cock in accordance with his tempo, not hers. Despite any protests, her wide smile beamed with joy."

ro "You want chivalry, you should try fucking a knight!"

maud "And what would be - ah!- The fun in that? "

"Her pussy clamped around his cock greedily, testimony to her words. Gods, she was tight, and she-"

scene cg681 with fade
show rowan necklace naked behind cg681
#maud naked happy
show maud neutral behind cg681
pause 3

maud "You can cum in me."

"The words caught him off guard, and the tables turned again, as Maud grabbed his hands and intertwined their fingers together in a romantic gesture that in no way fitted the fervent rocking of her hips."

ro "A- -ah! - a safe day, then?"

maud "I don’t know."

"Her lips curled into a wild smile, and he remembered how he thought her mad when he first saw her. And maybe she really was."

maud "I don’t keep track."
maud "But it’s a new beginning, no?"
maud "Good time to start thinking about the future."
maud "Maybe I’ll start a family."

"She didn’t stop for a moment, and it was increasingly harder to keep himself from painting her insides white. Something he knew she could see and feel."

maud "You wouldn’t make a bad father Rowan."
maud "What do you say?"

"She leaned in to steal a deceptively tender kiss off his lips, and kept his gaze as she pulled away, the deep blush on her face making him doubt what was a trick, and what a shy admission of affection."

maud "Do you want to cum in me, Rowan?"

menu:
    "Do it!":
        $ released_fix_rollback()
        scene cg682 with fade
        show rowan necklace naked behind cg682
        #maud naked happy
        show maud neutral behind cg682
        pause 3
        "The needy undertone in her voice, the delightful warmth of her snatch, and the vision of making this boyish fighter swell with his children all proved too much."  
        "He thrust his hips up again, fulfilling her desire. She threw her head backwards, enjoying as he ejaculated right into her, his cock crammed as deep as he could."
        maud "Aaaaa-a! Aaa-aaaa… "
        "He expected to see a triumphant smile blossom with every cry of ecstasy, but instead, he was greeted by a shy, almost loving expression."
        maud "Aaaaaaah..."
        "One that did not fade, not for as long as he held her gaze."    
        "One he did not want to fade." 
        scene black with fade
        "... ... ..."
        $ maudCreampie = True
        jump maudEvent3Ending
        
    "Pull out.":
        $ released_fix_rollback()
        scene cg682 with fade
        show rowan necklace naked behind cg682
        #maud naked happy
        show maud neutral behind cg682
        pause 3
        if all_actors["alexia"].relation >= 50:
            "He clenched his jaw, refusing to play along. As if he’d let another woman bear his children before Alexia!"
        else:
            "He clenched his jaw, refusing to play along. As if he’d let any other woman tell him what to do!"
        ro "I think you’d -ah! - Look better with a pearl necklace, than a swollen stomach!"
        "If Maud was disappointed by his words, all ill feelings were quickly washed away by the energetic thrust of his hips, that robbed Maud of all desire to toy with him any longer. Finally, she let herself surrendered to his cock."
        maud "Ha! So ~~~ So~~  Stubborn! "
        "Her complaints lost all weight to them, as she arched her back in ecstasy. Making true of his promise, Rowan pulled out, at the edge himself, and a moment later sprayed his cum across her body."
        maud "Aaaah!~~ Aaaah… Ah…."
        maud "Damn it. You got some in my hair."
        "She brought her hand to her face, and tries to brush the sticky bangs away - only to have them stick at an odd angle. It looked so ridiculous, he couldn’t hold back his laugh."
        maud "Hmph."
        "She repaid him back right away, leaning in to steal another kiss. Feeling generous, he let her do just that, holding her close as they enjoyed the last embers of their passion."
        scene black with fade
        "... ... ..."
        jump maudEvent3Ending

label maudEvent3Ending:

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve
show maud neutral at midright with dissolve

"Maud landed by his side, making the jump with grace that even now continued to surprise him." 


if maudSex == True:
    ro "Going as far as to tempt me with coming inside, just to win… You don’t hold anything back, do you? "
    maud "Hm? No. I suppose not. "
    if maudCreampie == True:
        show rowan necklace shock at midleft with dissolve
        maud "I did come halfway. So it was my loss in the end."
        ro "Then all that talk-"
        #maud happy
        show rowan necklace neutral at midleft with dissolve
        "She tilted her head, trying to keep a straight face, but could not keep the spark of amusement from her eyes."
        "… He wondered if it was a risky day after all. Somehow, he had a feeling she wouldn’t answer him, even if he pushed for it."
        #maud neutral
    if maudCreampie == False:   
         maud "Wanted to make you come at least once before I did again."
         maud "You’re a tough nut to crack."
         "Rowan arched his eyebrow as she threw him a resigned sigh. “Again”? She really was stone-faced, at least when she needed to be."
    maud "… Alright. That’s enough entertainment."
    maud "I will make my preparations."
    
maud "Pass any orders through Calhoun. I’ll have to see to some matters personally."

ro "How much time do you need?"

maud "Eight hours."

ro "… I was thinking in terms of days."

maud "I work fast."

show rowan necklace shock at midleft with dissolve
#maud embarrassed/aroused

"She was already halfway to the exit as she said that. But just before leaving, she turned around. A hint of longing entered her eyes- "

show rowan necklace happy at midleft with dissolve
#maud neutral

"And it disappeared in an instant as Maud steeled herself against what was to come. But by now he knew what that usually distant expression held underneath." 
"All that love and passion, desire for a life she never got to live, sacrificed so others could get a chance at it, no matter how slim. "

maud "… Stay alive, Rowan."

ro "You too, Maud. You too. "

scene black with fade

"He could only hope, that once all his deceptions come to light, she’ll understand his sacrifices were no different from hers."
                                                                                                                                
$ maudAllied = True

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return
                                                                                                                                