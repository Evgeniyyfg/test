init python:
    
    event('alexia_and_the_drunk', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'", "midCorHappened == True", "midCorFlee == False", "NTR == True"), group='alexia_barmaid', priority=pr_npc)
    event('bards_song_over', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), group='alexia_barmaid', priority=pr_npc)
    event('diplomatic_immunity', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), depends=('jezera_s_alliance_making_skills',), group='alexia_barmaid', priority=pr_npc)


label alexia_and_the_drunk:

scene alexia_tavern_1 with fade

"was often a gruesome, messy affair. On particularly rowdy nights, overturned tables and scattered barstools only added to the chaos." 
"Which was to say nothing of the assorted drunks who, at the end of the evening’s revelry, ended up strewn like slaughtered casualties across the floor and bar countertops. Alexia was, in many ways, more of a corpse-clearer than a barmaid. "
"One such liquor-licker was still sitting slumped at the bar, insistent in his refusal to either leave or lose consciousness."


scene bg21 with fade

drunk "Oi! Wench! More beer, aye?"

show alexia barmaid angry at midleft with dissolve

"This inebriated indigent had been a thorn in Alexia’s side all night, dispensing catcalls, curses and obscene calls for “more ale!” in equal measure." 
"More than once, Alexia had been forced to run the gauntlet of his pinching fingers and groping hands, grimacing every time a glancing touch brushed across her bottom. He was a nuisance, in every sense of the word."
"Now that the tavern was closing, the time had come for him to leave." 
"...But he would not budge."

al "...Sir, it’s well past midnight. Everyone else has gone ho-"

drunk "{i}Fack off{/i}, aye?"

"Exhausted, exasperated, and stressed to the point of anger, Alexia approached Indarah for advice on what to do."

show indarah neutral at edgeleft with dissolve

"Indarah, in a tone that made it clear Alexia should say nothing more, whispered in her ear."

ind "Bar the door, return to your duties. I will handle this."

"Alexia grumbled to herself, but did as she was bid. She had expected Indarah to give the drunken lout a thorough tongue-lashing then and there." 
"But the exotic tavern owner gave no sign that she intended to intervene whatsoever, casually polishing a bar glass as the evening hours wound down. Aside from a brief disappearance into the portal room, she remained aloof."
"As the minutes ticked by it became increasingly obvious to Alexia that he would face no repercussions. She was just about to complain to Indarah again, when a hulking, green brute strode in from the back rooms."

show alexia barmaid shocked at midleft with dissolve

"For a brief, terrible moment Alexia thought that a repeat of Arthdale was about to occur. It was only after she sized up the Orc that she realized he was a veteran from Bloodmeen."

show orc soldier neutral at midright with dissolve

tarek "Wots the trouble?"

"He was large, a beast of a brute. Narrow eyes set upon a heavy brow, with a rough, chiseled jawline. This was no mere Orc, but was a hardened killer."
"Indarah merely pointed at the man, shoving her thumb over her shoulder in dismissive command to remove him. The Orc grunted."

tarek "Waste o’ damn time."

show alexia barmaid neutral at midleft with dissolve

"Despite his grumbling, the Orc shifted his swordbelt and approached the drunk. Alexia was just passing him as he did so, balancing a tray of empty glasses on her hand." 
"She felt his thick, green hand grasp her by the forearm. She stopped short."

tarek "Ey, wots his guff? ‘Dis fool givin’ ya the pinchy treatment?"

"The Orc lifted his free hand and mimed pinching his fingers together. Alexia blushed and nodded. The Orc grinned with cocky pride, looking Alexia up and down."

tarek "Thought so. Had the same thought m’self."

"The Orc bent down. For a brief moment, Alexia thought he was leaning down to kiss her, but instead his lips went to her ear."

tarek "Don’ worry. He won’t give ya no more trouble."

"With a smirk and a grin, the Orc let go of Alexia and trudged up to the drunk. Alexia watched as the Orc smacked his fist onto the countertop directly next to the old drunk’s dozing head."

tarek "{i}Ey{/i}! Wakey wakey!"

"The man’s head snapped up, his eyes going wide at the sight of the hulking figure looming over him."

tarek "If you’s gonna keep the nice ladies up all night, you’d best keep drinkin’."

"The drunk, perhaps finally sensing the danger through his alcohol haze, stammered something inaudible and tried to stand up. The Orc let out a guffaw and planted his heavy hand down onto his shoulder, shoving him back into his stool."

tarek "Ah naw, ya ain’t gettin’ away dat easy, ya cheeky git."
tarek "You’s wanna drink? Fine. Then drink wif me."

"The Orc bent over the countertop and fished a tall bottle out. He planted it with a wet smack onto the Bar."

tarek "‘ere’s the deal from now on: you can come in ‘dis place whenever you like. Night n’ day, rain or shine. Don’t make no difference to me."

"The Orc’s grin was wide and predatory, a long line of sharp fangs that looked ready to take a bite out of the terrified drunk. He popped the cork on the bottle."

tarek "Only rule is: ya gots to tell good ol’Indarah over there yer comin’."

"He lifted the bottle and took a pair of deep, heavy gulps, swallowing well over a third of its contents in the process. He lowered the bottle and smacked his lips."

tarek "{i}Ah{/i}! Dat’s the stuff."
tarek "{i}But...{/i}"

"The Orc turned in his stool to face the drunk. The poor man tried to squirm away but the Orc took him by his chin, staring straight into his eyes."

tarek "Everytime you’s here, I’ll be here too. We’ll be drinkin’ buddies!"
tarek "And fer every drink {i}I{/i} take, you takes the same."

"The Orc’s easy smile disappeared. His face contorted for a moment into a monstrous simulacrum of a dragon’s snarl."

tarek "And if ya can’t keep up…"

"The Orc smashed the bottle against the bar just next to the terrified drunk’s trembling hand. The unfortunate man let out a squeaking yelp as glass and alcohol rained down onto the ground."

tarek "You won’t have to worry ‘bout yo’ tab ever again."

"The threat alone was enough to shatter him. The bedraggled drunk fled from the grinning Orc’s sight, whimpering as he threw open the door and ran from the tavern."
"The Orc started to laugh, though Alexia noticed that he made no move to leave, now that his task was done."

tarek "Ey, where’s my victory bottle?"

"Indarah sighed, as if she had expected this outcome."

ind "Alexia, let him have his pick of whichever bottle he wants. One bottle, and no more. Tarek knows the rules. "

$ tarekName = "Tarek"

hide indarah with dissolve
show alexia barmaid concerned at midleft with dissolve

tarek "...Well? Wot ya waitin’ for?"

"Alexia circled to the back of the bar. The next few minutes were a frustrating guessing game as the Orc patently refused to pick a specific bottle."
"Finally, once he had chosen one he tore open the cork with his teeth, spitting it out onto the floor to settle with the smashed glass of the first bottle. The Orc took a deep slug of the bottle, then held it out for Alexia."

tarek "Have a taste. Gab wif me a minute."

"He swirled the water around in the bottle, his heavy brow arching in mirth. That wide, predatory smile was on his face again."

if alexiaAndrasObedient == True:
    "There was a callous masculinity to the Orc’s brutish demeanor that was strangely… {i}charming{/i} to Alexia. Perhaps it was just in her head, but the Orc in many ways reminded her of Andras."
    "Alexia smiled, sliding smoothly into the seat next to him as she gratefully accepted the bottle from his hands. Her fingers trailed across his as they passed the bottle between them."
    jump tarekSitandTalk

else:
    "The offer was tempting. Alexia had been working on her feet for hours now, and was nearly at the end of her endurance. Despite the brutish company, she dearly coveted a short rest and a little nip of wine."
    "But… was it worth the trouble?"
    menu:
        "Accept the bottle.":
            $ released_fix_rollback()
            "Thirst and weariness won out over caution. Alexia - with more than a few misgivings - took a seat next to the Orc. She felt his wandering eyes roam across her body."
            "The Orc grinned and held out the bottle. She reached out and took it. His thick, green fingers met hers for a brief moment as he handed her the bottle."
            jump tarekSitandTalk
            
        "Decline and go back to cleaning.":
            $ released_fix_rollback()
            "Alexia spared a nervous smile in the direction of her uncouth savior. Though the drink was sorely tempting, and Alexia was in desperate relief from the drudgery of the work, she knew a risky offer when she saw one."
            al "Thank you, Tarek. But I really must clean up this spill."
            "The Orc grunted and downed the bottle, gulping half its contents in one great swallow."
            tarek "Suit yo’self. I ain’t one fer wastin’ good drink."
            "He waved her away dismissively. Alexia - finally able to see a light at the end of the tunnel - redoubled her efforts. For all the toil still to do, she had at least gotten to see the sorry old drunk evicted. The day wasn’t a {i}complete{/i} loss."
            return

label tarekSitandTalk:

tarek "Dat’s a nice lady. Drink up!"

"Alexia lifted the bottle to her lips, taking a swig of the wine. The Orc’s taste was good, it was a fine vintage."
"Tarek grinned, reaching out to tilt the end of the bottle upwards. In a rush, Alexia’s mouth was flooded. Her cheeks wept red tears as her throat overflowed. She coughed and spluttered, not ready for such a sudden deluge."

show alexia barmaid shocked at midleft with dissolve

al "{i}Guh!{/i}"

tarek "Har! Ya hold yer drink {i}worse’n{/i} the drunk!"

"Alexia swallowed the wine still in her mouth and affixed the randy Orc with a glare."

show alexia barmaid angry at midleft with dissolve

al "{i}D-don’t{/i} do that!"

"His insolent grin was answer enough."

tarek "Then drink faster!"

show alexia barmaid neutral at midleft with dissolve

"The Orc began to laugh. Despite her own annoyance, Alexia found herself smiling along with him. He was an uncultured beast, to be sure. But there was an odd sort of charm in his antics. He took the bottle from her hand and took another long swig."

tarek "Wine like ‘dis, ya gotta {i}gulp{/i} it, see?"

al "Why?"

"Tarek smacked his lips and handed the bottle back to Alexia. She took a shallower drink, tasting the warm flavor of the wine. All things considered, it was a pleasant end to the evening’s work."

tarek "Cause it’s pisswater. Wouldn’t want Indarah to waste her best stuff on a lowly head-cracker."

show alexia barmaid happy at midleft with dissolve

al "...Or a lowly barmaid."

"The Orc guffawed, slapping Alexia across her back. She felt his hand linger for a long moment on her, drifting lower before retreating."

tarek "See? You gets it. Peas in a pod, you’n me."
tarek "{i}Neither{/i} o’ us gets the reward they deserve. Just endless toil and a bottle o’ piss-wine to keep each other company."

"Alexia giggled as the bottle was passed back to her. She dwelled on Tarek’s observation for a long moment. It was strange how... prescient it was. More often than not Alexia felt as if her jobs were merely one endless, thankless task after another."
"Perhaps this Orc felt the same. Alexia took a contemplative sip from the half-empty bottle."

al "{i}Everyone{/i} deserves to be rewarded for their hard work."

"Tarek grinned, a naughty twinkle in his eye. He accepted the bottle back from Alexia and finished off the bottle, smacking his lips again."

menu:
    "Thank Tarek for his help.":
        $ released_fix_rollback()
        al "...Thank you,Tarek."
        "The brash Orc guffawed again."
        tarek "Har! ‘Tink nothin’ of it, pretty lady. Bashin’ heads is wot I do. The bottle’s just a bonus."
        "The Orc stood up and stretched, giving Alexia a pat on the bum before standing to leave."
        tarek "Tell ol’Indy I said ‘thanks’ fer the drink. Call me anytime."
        al "I’ll do that Tarek."
        "Alexia watched as the Orc shot her one last sly smirk before departing. Alexia sighed, turning to face the final, arduous push before closing time. At least the Drunk was finally gone. That was a plus."
        return
        
    "“Reward” Tarek for his help.":
        $ released_fix_rollback()
        $ AlexiaOrcSex = True
        "Sod it. She had had a rotten day, and this gruff greenskin had managed - in spite of his abrasive demeanor - to markedly improve it. Perhaps he did deserve a reward for all his efforts."
        show alexia barmaid aroused at midleft with dissolve
        "He was attractive enough… in a bestial, boorish sort of way. In fact, it was {i}that{/i} uncultured vulgarity that drew her to him. His aggressive masculinity was, paradoxically, as intriguing as it was infuriating."
        "Alexia, plied by wine and the pleasant company, inched forward in her chair. She leaned forward, as she reaching beneath the countertop at the same time Tarek lifted the bottle to his lips. He jerked in place when her hand settled on the stiff bulge in his groin."
        al "Oh…"
        tarek "Har! Yer a feisty little fig, ain’t ya?"
        #cg 1
        scene cg657 with fade
        show alexia barmaid aroused behind cg657
        show orc soldier neutral behind cg657
        pause 3
        "Far from being put off by her antics, Tarek grinned. He took another long swig of drink before putting his free hand atop hers, mashing it against his crotch so she could appreciate the full scope of his manhood."
        al "Mmmm…"
        tarek "And here I was, thinkin th’ only friend I’d make tonight was ‘dis bottle."
        "Alexia’s fingers kneaded his growing erection through the thin veneer of his leather loincloth. Her eyes lidded as she felt the heat radiating off of him."
        al "We deserve to be rewarded for our hard work, don’t you think?"
        tarek "Har! Dat we do. Dat we do."
        "Tarek settled his elbows onto the bar top, taking yet another swig off the bottle as Alexia did her dirty work. She shifted position, peeling aside the loincloth to get at the fat green cock bulging beneath."
        "Her fingers wrapped around his length, marveling at the prodigious size she was dealing with. The head of his cock lifted nearly to the roof of the bar top at full erection. She jerked him with slow, steady movements, working up a lather."
        tarek "Easy now, we’s just gettin’ to the good part."
        "The Orc huffed when she began to speed up, using her awkward position to roughly masturbate the Orc beneath the bar."
        "From a casual observer’s perspective, Alexia was merely leaning forward on the bar. Her companion was just taking short hits off the wine bottle."
        "In reality, she was quickening her efforts. Her fingers clenched as she formed a solid grip upon his cock, jacking the well-endowed Orc off at a faster and faster pace."
        "Alexia’s efforts clearly paid off, for Tarek was soon letting out little, squeaking grunts in the pit of his throat. He slid the bottle across the countertop to her, shooting her a naughty smirk."
        tarek "Yer grip’s off. Take a drink."
        "Alexia laughed and did as she was bid, lifting the bottle with her free hand and downing a robust mouthful. She gripped him tighter, tugging at his cock with ever increasing vigor. Her fingers were now slick with his precum."
        "Tarek took the bottle from her and downed the last dregs. Alexia, randy, tipsy and well past the point of common sense, redoubled her efforts. Her rapid, jerking handjob became a blur of motion as Tarek reached his climax."
        "The Orc grunted, hunching forward in his seat. Alexia felt the sudden bulge of his cumvein, a wave of heat and inseminating liquid that rose, peaked to the brim, then fired a thick, white rope against the roof of the bar top’s underside."
        "Alexia giggled as the masculine Orc let out another grunt, reveling in the feeling of working him to completion as she continued to jerk him as strings of cum came spurting from his member. Her fingers were slick with white fluid."
        show cg658 with dissolve
        pause 2
        show cg659 with dissolve
        pause 3
        "Just then, Indarah stepped through the door. Her eyes affixed to Alexia and Tarek sitting together. Her eyes narrowed. Tarek, still in the midst of ejaculation, let out a loud sigh of satisfaction. He planted the empty bottle on the countertop."
        scene bg21 with fade
        show alexia barmaid aroused at midleft with dissolve
        show orc soldier neutral at midright with dissolve
        show indarah neutral at edgeleft with moveinleft
        tarek "{i}Mmm{/i}! Dat’s some damn fine wine, Indy!"
        "The look on Indarah’s face was inscrutable. Alexia couldn't tell if she either enjoyed or despised the Orc’s presence. The Tavern owner allowed a faint smirk to play across her lips."
        ind "..It’s the same brand you guzzle every time, Tarek."
        "Tarek grinned, patting Alexia’s inner thigh with his big hand beneath the countertop."
        tarek "Yeah, but fer some reason, it tastes {i}better{/i} today!"
        show alexia barmaid shocked at midleft with dissolve
        "Alexia panicked. She hastily reached for her hand towel, furiously mopping up the leftover splooge and Orcish cum from her fingers, hands and the bar top’s underside."
        ind "Alexia, have you finished cleaning the bar?"
        show alexia barmaid concerned at midleft with dissolve
        al "N-not yet, Indarah. I was just-"
        "Tarek let out a booming guffaw, clapping Alexia hard on her back."
        tarek "Har! She was just keepin’ me company is all! Ya wouldn’t want to make yer best customer mad, would ya Indy?"
        "Alexia saw something approaching recognition cross Indarah’s face. Alexia hurriedly mopped up what she could from the remainder of Tarek’s eruption, giving him a last, loving jerk with her hand before standing up and stepping nervously away."
        "Indarah gave Alexia a short look, then glanced back at Tarek. She squared her jaw."
        ind "...I suppose I wouldn’t."
        $ change_corruption_actor('alexia', 3)
        return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label bards_song_over:

scene alexia_tavern_1 with fade

"Alexia walked into the front of the bar today ready to work. Two different groups of travelers had come down the road so it was going to be a busy day."
"Only, when she prepared to start her shift, she found Indarah ducked behind the bar counter with her hands over her ears."

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve
show indarah neutral at midright with dissolve

al "Is something happening?"

"Indarah removed her hands from her ears and blinked in confusion. Then, she looked over the bar wearily."

ind "Ah, he must have taken a break?"
ind "I can’t exactly go about advising you stay here right now, Alexia. Best if you back away for a time."

"Alexia looked over to the middle of the room, searching for whatever put Indarah in this state. She mostly found a collection of burly men, each more miserable seeming then the last. They ate with heads down and horror in their eyes."
"But, amidst the gloom, there was a single flash of color. A man in silk stood atop one of the tables with a loot in hand. He had shaggy blond hair and a pronounced nose."
"Before Alexia could react, the man started to sing. Then, she understood the state of the others."

bard "Oh, I hate the dear old lady."
bard "She just won't see me lately."
bard "In fact, she might hate me."
bard "But, she's still nice and dainty!"

"He took a painfully drawn out breath. But, before Alexia had time to recover he jumped back into his musical monstrosity."

bard "When she sees me she's quite irate."
bard "She must think me an ingrate."
bard "For the baby, I long to sire it."
bard "And she may grow to tire of it."

"Alexia’s eyebrows narrowed. As atrocious as his wordplay was, his voice was worse. Arthdale had possessed a good number of singers and musicians, but none like this."

al "That's not a rhyme."

bard "Hrmm?"

al "You said “Sire it” and “Tire of it”. The extra “of” throws off the rhythm."

"The bard blinked twice and then went deep into thought."

bard "Oh yes. Yes."
bard "How about..."
bard "How about..."
bard "For her, I'd be a pirate!"

"Alexia could only recoil as the silken fool rushed over to her and placed an overdramatic kiss on her hand. From up close he even smelled bad."

if all_actors["alexia"].corruption < 31:
    "Alexia sighed to herself. It was distasteful, but what could she do? So, she let the bard give way too many smooches to her wrist."
    "Then, he jumped back to the center of the room and started up on his next masterpiece."
    al "I think...I think I’m going to do inventory."
    ind "That is probably wise, yes."
    scene black with fade
    "In the morning, the bard thankfully departed along with the caravans. But, it was not a morning for much rejoicing."
    "The other customers left scant tips. After all, they had not had a very good stay."
    #TODO - reduce tavern weekly income one off
    return
    
else:
    "Enough was enough."
    "Without a further word, Alexia reached down to the man’s Lute and yanked it from his hands."
    bard "My instrument!"
    if all_actors["alexia"].corruption > 60:
        "Before he could react, Alexia slammed the wooden instrument on his head so hard that he fell to the ground."
    "She marched over to the doorway and threw the lute as far out into the wastes as she could. In the darkness, she lost sight of where it went."
    "Then, she was pushed to the side. The bard went running and yelping into the wastes to collect his instrument."
    "When she turned and walked back, she found the entire bar full of dour men and immediately turned upside down into a glowing party. They cheered her return."
    "In the morning, she found out that they’d received more tips than usual the night before. Though, they hadn’t received any from the bard."
    "What a surprise."
    #TODO - increase tavern weekly income one off
    return

########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################

label diplomatic_immunity:

scene alexia_tavern_1 with fade

"It was a quiet night at the inn aside from the harsh rumble of thunder outside, soon followed by the steady thump of rain on the roof. Alexia watched the small beads splatter and roll down the glass windows and pretended they were racing toward the windowpane's finish line."
"It wasn't as if she had anything better to do; the bar was clean, most of their visitors had checked out for the week, all she had to worry about was refilling the occasional beer for a weary traveller at a nearby table." 
"As Alexia grabbed the pitcher for another refill, three hooded figures scrambled through the front door, their cloaks soaked through from the rain. They dropped their hoods at once, clearly relieved to find shelter from the storm."
"The man in the center was tall with a handsome face and messy curls of damp dark hair. It was only when he stepped into the light that Alexia realized he was a dark elf. Two goblins flanked him on either side and ushered for him to follow as they checked in."
"Alexia watched the curious trio as the goblins led the reluctant elf to their room."

scene bg21 with fade
show indarah neutral at midright with dissolve

ind "You know them?"

show alexia barmaid shocked at midleft with dissolve

"Alexia jumped; she hadn't even heard Indarah approach."

show alexia barmaid neutral at midleft with dissolve

al "No. Do you?"

"Indarah nodded."

ind "The goblins are traders: Ebs and Ras. I see them come in here every few months. They always order the same thing-- two bowls of beef stew and three mugs of beer before they wobble back to their rooms."

al "I guess that makes them easy to remember."
al "What about the third one there?"

"Alexia pointed toward the dark elf just before he disappeared up the stairs. Indarah looked after him and shrugged."

ind "Couldn't say. Never seen him. He looks like a page boy, though, don't you think? I guess they got some extra help."

al "Hm. I suppose so."

"Alexia returned to work, the thoughts of the dark elf and his escorts drifting to the back of her mind."

scene bg21 with fade

"....."

show alexia barmaid angry at midleft with dissolve

al "Ugh, this is disgusting…"

"Alexia pinched her nose as she finished cleaning one of the rooms. Some of these travellers were absolute {i}pigs{/i}."
"She took in a deep breath of fresh air as she stepped out into the hall, eager to close the door behind. If she ever had to scrub vomit from bedding again it would be too soon."
"With a sigh, Alexia knocked onto the door to the next room."

show alexia barmaid neutral at midleft with dissolve

al "Housekeeping."

"There was no answer, so Alexia unlocked the door and stepped in."
"At least this room wasn't so bad; some rumpled sheets, a few balled up pieces of parchment on the floor. She got to work, eager to finish quickly and end her shift for the night."
"As she bent over to pick the parchment up from the floor, something under the bed caught her eye. Alexia reached underneath, surprised to find a satchel."

show alexia barmaid shocked at midleft with dissolve

al "Oh!"

"Something hard and circular fell out of the bag and rolled across the floor. Alexia picked up the rough metal, surprised by how heavy the silver steel was. Purple gems decorated the heavily spiked circle, glinting under the soft lamplight."

show alexia barmaid neutral at midleft with dissolve

al "What is this doing here…?"

rhis "O-Oh… That's..."

"Alexia froze, the strange accessory clutched in her hands as the dark elf opened the door. He stood in the doorway, panic written on his face as he took in the item in her hands."

al " I'm so sorry, it just fell out…"

"Alexia tucked the strange object back into the bag. She shouldn't have been snooping, but what if the bag belonged to another guest? The right thing would have been to return it."

rhis "It's okay… Um…"

"The elf glanced around the hall before ducking inside, making sure to lock the door before dropping his voice down to a whisper."

rhis "I can explain."

al "Did you steal this?"

rhis "No! ...Er, not really. Please, just listen to what I have to say."

"He gestured for Alexia to sit in a nearby chair while he perched himself on the edge of the bed. Alexia did so, her curiosity getting the better of her."
"The dark elf continued to glance around the room as if he was being watched. She had to strain to hear him speak."

$ rhistelName = "Rhistel"

rhis "My name is Rhistel. I promise that heirloom is as much my right as my name. I didn't {i}technically{/i} steal it--it is… was… my mother's."

al "Won't she be upset that it's gone?"

"He ran a hand over his face, his smile bitter and without humour."

rhis "We don't need to worry about that. She's dead."

show alexia barmaid shocked at midleft with dissolve

"Then, upon seeing the look on Alexia's face--"

rhis "I didn't kill her. She… Things are complicated back home. But she's gone and my sister is in charge now."

show alexia barmaid neutral at midleft with dissolve

rhis "How much do you know of Dark Elven politics?"

al "Enough to know you are one."

"Rhistel nodded, and Alexia noticed a flicker of shame in his eyes as he looked away. He picked at a thread on his sleeve, betraying a nervous habit."

rhis "It's common for Dark Elven men of high social standing to be given as pets to secure alliances. My mother adored me and always promised I would be protected… But my sister is in charge now. She's not so merciful."

"Rhistel's eyes met Alexia's then, and she could see the desperation in his gaze as he pleaded with her."

rhis "So please, I'm begging you, do not tell anyone about the heirloom. I just want to leave as far as possible, until no one can recognize me again."

if all_actors["alexia"].corruption > 30:
    "Alexia's lips pressed together in a tight line and, for a brief moment, she considered how advantageous this could be: a dark elven noble trying to escape slavery. She knew plenty of people that would pay plenty for that kind of information, if she didn't take him back to his sister herself."
    if all_actors["alexia"].corruption < 61:
        "She shut the thought down just as quickly as it came. What kind of woman would harm someone in need that way?"
    al "Don't worry, I won't tell anyone. Your secret is safe with me."

else:
    "Alexia nodded and a pitying frown pulled at her face. She could only imagine how scared and alone this poor man was just trying to escape slavery, enforced by his own flesh and blood no less."
    al "Of course I'll keep it a secret. You have nothing to worry about."

"Rhistel's body sagged with relief, a grateful smile brightening his weary face."

rhis "Thank you. You have no idea how much this means to me."

"With that, Alexia hastily finished cleaning the room and stepped back out into the hall."
"She was only a few steps away when another conversation caught her ear."

ebs "We could tell him we're making a stop in town. He doesn't need to know {i}what{/i} town."

"Alexia slowed her pace, her attention drawn to the conversation floating out from the room next door. She pressed her ear against the wood, a nagging feeling twisting in her gut."

ras "That's true. You know, the closer we get to the border, I'm sure the sister's name will pop up. News about runaways with that kinda background tends to go pretty far."

ebs "Exactly. Once we got a name, we just need to draft a ransom note and send it on its way. Then we get the money and boom! We're rich!"

if all_actors["alexia"].corruption < 61:
    "Had they heard her conversation with him, or had they known about this all along? She put a hand to her aching heart; was she responsible for Rhistel's blown identity?"
    
else:
    "Had they eavesdropped on her? Alexia's fists tightened at her sides. What right did they have to listen in on her conversation?"

"She didn't think; she just unlocked and threw open the door, adrenaline rushing through her veins. The goblins both jumped at her sudden intrusion, looking up from their maps on the table."

ebs "We don't need our room clea--"

al "You're going to ransom Rhistel back."

"The goblins' mouths snapped shut. They exchanged a glance, their high spirits immediately taking a sour turn."

ebs "And what's it to ya? Ya shouldn't have been eavesdropping--"

al "You did it first."

"It was a wild guess, but from the look on their faces, Alexia knew she was right. So they had heard her conversation. She swore under her breath. She'd only just made her promise to Rhistel that she would keep his secret and already it was broken."

ras "Listen, girlie. Why don't we cut a deal? We've got gold, and you got a pretty mouth you can keep shut."

"Alexia stared at them, shocked by the offer. She had expected threats or a fight even-- not a bribe."

al "And what would it take for you not to harm him?"

if all_actors["alexia"].corruption > 60:
    "She glared between the two men, her hands balled into fists at her sides. She was furious; if they hadn't eavesdropped on her, she never would have been forced to break her promise in the first place."
    
elif all_actors["alexia"].corruption < 31:
    "She couldn't shake the idea of poor Rhistel bound in chains and forced to act as some dark elf's pet. Alexia just met the man, but his story was so pitiful that the idea of him being forced to go through with it stabbed at her heart like a knife."
    
else:
    "Guilt tugged at her heart. It was her fault that his secret was out now; she had to make it up to him."

"The goblins scoffed, but the merchant eyed her over, his crooked lips curling into an even more crooked smirk."

ebs "Been a while since either of us saw some action, wouldn't you say, Ras? "

"Ras chuckled but nodded. She could feel their gazes piercing through her clothes, taking in every slight curve of her body that her uniform exposed."

menu:
    "Do nothing.":
        $ released_fix_rollback()
        if all_actors["alexia"].corruption < 61:
            "Alexia stared at the men, flustered and stunned. What should she do? {i}Could{/i} she do anything realistically? She wasn't about to have sex with these men in exchange for a stranger's safety, but wasn't there any other way to help him?"
        else:
            "Were they seriously trying to {i}blackmail{/i} her? What kind of woman did they take her for?"
        if all_actors["alexia"].relation > 30:
            "Not to mention the betrayal Rowan would feel if he knew she slept with someone else. How could she ever justify that?"
        "The goblins took her silence as her answer."
        ebs "Now that's a smart woman. Be on your way now."
        "Alexia tried to find something-- anything-- to say, but nothing came to her. She was paralyzed by her own indecision."
        "Without another word, Alexia fled the room."
        "……"
        "When Alexia came to clean their room the next day, the goblins and Rhistel were long gone. Worry pulled at the back of her mind, thoughts of what would become of Rhistel once the goblins' ransom succeeded eating her away." 
        "She should have done something, and yet, here she was."
        "Alexia stepped into the goblins' room with her cleaning supplies, ready to turn over for the next guest." 
        "A large velvet pouch sat on the bed. When she looked inside, shiny gold coins glinted up at her."
        "Well, at least something came of her indecision."
        $ castle.treasury += 50
        return
        
    "Help Rhistel escape.":
        $ released_fix_rollback()
        "They couldn't be serious, right? But from the look in their eyes, Alexia knew they meant every word."
        "She smiled politely, working hard to keep the grimace from her face. The idea of lying in bed with these two scheming lowlifes made her sick, but if she wanted to assist Rhistel, she couldn't risk them thinking she would do anything to upset their plan. She would just need to find another way to help Rhistel."
        al "I'll be quiet. You have my word."
        ebs "Damn. Was hopin' you'd take us up on the other option, but silence works, too."
        "Alexia forced a smile and stepped out of the room, a plan already forming in her mind."
        "….."
        "It was late into the night when Alexia tiptoed through the halls of the inn, the sounds of the storm disguising her footsteps and the creaky floorboards."
        "Rhistel was fast asleep in bed, his hair tousled and knotted over his pillow. Alexia crept up to his side and gently shook his shoulder. He blinked awake, tired and confused."
        rhis "What--"
        "Alexia clamped a hand over his mouth. Rhistel's eyes widened and he stilled."
        al "You need to leave. Now. They know everything."
        "Panic sunk into his face, but he remained silent as Alexia removed her hand and rummaged through his room, tossing his items back into his bag."
        "Rhistel said nothing as Alexia helped dress him up and covered him in his cloak, pulling the hood low over his face." 
        "She escorted him back outside to the stables; she'd already prepared a horse for his escape. Alexia helped attach his luggage to the animal before he climbed up and took the reins."
        "Before he took off, Rhistel gripped Alexia's hand and smiled down at her. His touch was soft, his fingers smooth and free from calluses."
        rhis "...Thank you."
        "She would need to feign being too sick to work tomorrow; the last thing Alexia wanted to see was the goblins when they realized their ransom had disappeared on them. It wouldn't take long for them to figure out who did it."
        $ change_corruption_actor('alexia', -5)
        return

    "Fuck the Goblins in exchange for Rhistel's safety" if all_actors["alexia"].corruption > 30:
        $ released_fix_rollback()
        al "I…"
        "Alexia began to object but stopped herself, the words dying in her throat. Was this all they wanted in exchange for Rhistel's safety? Men were so simple when it came to their desires."
        al "Alright. As long as you can guarantee Rhistel's safety."
        ebs "Oh. You're serious?"
        ras "Don't make her change her mind, Ebs. Opportunities like this don't come round often enough."
        ebs "Right, right. Why don't you get on the bed for us, girlie?"
        "Alexia did as commanded, settling on her knees into the middle of the bed. The goblins wasted no time unbuckling their belts and crawling after her, one on either side of her body." 
        "She felt their hands slide from her thighs to her ass to her breasts, pushing at the fabric to get a better sense of how her body felt underneath. Alexia couldn't help but grin to herself as they removed her uniform, tossing the dress aside to ogle at her bare skin."
        ebs "Fuck, it's been a long time since I've seen tits like these."
        "The goblin squeezed her breasts and shoved his face between them, his tongue and teeth licking and nipping at the soft skin."
        "Ras's hands roamed down her hips from behind, his fingers brushing against her pussy."
        ras "Fuck, she's real wet, Ebs. You think she was hoping for an offer like this? Huh, girlie?"
        "His hot breath tickled her ear as he chuckled. She could feel his erection already pressing hard against her round ass."
        al "Mmm..."
        "A small moan escaped from her throat. Her eyes widened, surprised by her own reaction, but the goblins' grins grew wider."
        ebs "We better give her what she wants."
        "Ebs lifted his head slightly from her breasts, just enough to position his cock against her pussy. He slid in easily, forcing her to take his full amount. Alexia gasped, gripping his shoulders."
        ebs "Oh, you like that, don't you?"
        ras "Think she'll like this, too?"
        "Alexia whimpered as Ras eased into her ass from behind."
        ebs "How do you like the feel of two cocks in you at once, girlie?"
        ras "I think she likes it, Ebs."
        "They took their turns pushing in and out of her, Ebs gripping her hips while Ras toyed with her breasts from behind. Alexia's grip on Ebs's shoulders tightened, a pleasure growing low in her belly." 
        "Alexia's pulse quickened and her breath came out as heavy pants as the two men fucked her. She could feel their cocks moving in and out of her from in front and behind, and just when one would pull out, the other would drive right back in." 
        "They didn't give her time to catch her breath or even truly {i}breathe{/i}-- it was one building sensation after another toward her climax. Her toes curled and she arched toward them, jerking her hips back and forth in an attempt to match their movements."
        al "Oh fuck, oh fuck, oh fuck--"
        "Her voice pitched high with her orgasm and her body spasmed."
        "Ebs came soon after, grunting hard as his cum spurted inside of the wet folds of her pussy. Ras didn't last much longer, filling her ass with enough cum that it slid and dripped down her thighs."
        "The goblins climbed off of her, laughing a little to themselves at the mess they'd made. Even Alexia found it amusing and smiled herself; she may be a maid, but they could clean up this mess on their own."
        al "He'll be safe then?"
        ebs "Yeah, yeah, we'll keep him safe. Don't worry your pretty little head about it."
        ras "But if you ever want to go again, you know where to find us."
        "Ras winked at her. Alexia scrambled to pull her clothes back on before slipping out into the hall."
        "It was out of her hands now; all she could do was hope they kept to their word."
        "….."
        "Alexia stood in the stables beside Ebs and Ras, her hands folded delicately in front of her. A blush colored her cheeks as Ras subtly grabbed her ass, but she worked to hide any physical responses."
        "Rhitel was busy attaching his luggage to a horse the goblins had given him. He didn't seem to notice the sexual atmosphere between his three companions."
        "The goblins had already confessed to Rhitel what they knew about him by the time Alexia had arrived, but true to their promise, they intended to keep him safe from harm. Rhitel seemed skeptical about the ordeal, but was willing to trust them as he had Alexia."
        ebs "Remember, we'll be meeting up at Qerazel at the Blue Bird Inn. If you aren't there in four days, we're leaving without you."
        rhis "Don't worry, I'll be there."
        rhis "Ah, before I forget…"
        "Rhitel reached into his bag and pulled out the accessory. The goblins' eyes widened, immediately attracted to the shiny object. Rhitel passes it over to Ebs."
        rhis "For a ransom; it's preferable if they think I'm dead, but you can say that you came across this beside my corpse. I know my sister will be wanting it back."
        "The goblins stared at the spiked hoop and nodded; it wasn't a dark elf, but the crown itself came pretty damn close."
        "Alexia waved farewell to Rhistel as he rode off, and soon Ebs and Ras were travelling after him."
        $ change_corruption_actor('alexia', +5)
        return

    "Call Jezera." if all_actors["alexia"].flags["jezera_influence"] > 5:
        $ released_fix_rollback()
        "Alexia bit her lip, contemplating her options. She didn't want to have sex with them, but what else could she do to protect Rhistel?"
        if all_actors["alexia"].corruption < 31:
            "She hated the idea of him suffering for her silence."
        else:
            "She was already involved, she wasn’t about to let these chumps get away with it."
        "Ah, but if Jezera were here..."
        if alexiaJezObedient:
            "Alexia smiled to herself and nodded. Jezera was a master at negotiations, and it was probably best that her mistress be informed about the situation with Rhistel anyway. Jezera had plenty of connections to the dark elves; perhaps this could benefit both of them."
        else:
            "Alexia bit her lip and sighed. Jezera was a master at negotiations; there had to be something she could do to help Rhistel."
            "That didn't mean she wanted to ask her, though."
        al "I understand. I'll be quiet."
        "Alexia ducked out of the hotel room, eager to leave the goblins' presence." 
        "Once she was further away from the rooms, Alexia pressed a hand against her sapphire necklace."
        al "Jezera?"
        show jezera neutral behind bg21 
        je " Yes, yes, I hear you. Is something the matter, sweetling?"
        al "Somewhat."
        "Alexia explained the situation with Rhistel, working to keep her voice both low enough that she couldn't be eavesdropped on as well as loud enough that Jezera could hear her over the storm."
        je "I see. Wait just a moment."
        scene bg21 with fade
        show alexia barmaid neutral at midright with dissolve
        "Alexia made her way to the portal and waited. Fifteen minutes passed before Jezera stepped through."
        hide jezera
        show jezera happy at midleft with dissolve
        je "Now, where are these nasty little goblins?"
        al "Ah, right this way."
        "Alexia led her to their room. Jezera smirked and gripped the brass knob."
        je "You stay right here, sweetling. I'll take care of these negotiations."
        if alexiaJezObedient:
            "Alexia nodded, holding back. She was reluctant to trust the twins, but she knew Jezera could get this done."
        else:
            "Alexia nodded, a chill running down her spine. She trusted Jezera to handle this, but her methods… She wasn't sure if she trusted those."
        "A few moments later, Jezera left the room, a satisfied grin on her face."
        je "Those disruptive little goblins and I came to an... understanding. They were quite agreeable after some persuasion."
        je "We'll even bring the little lordling back with us. I'm sure he'll be very comfortable after a short stay in the castle, don't you agree?"
        "Alexia smiled, although she wasn't entirely relieved. A guest? She doubted as much. Still, he was safe."
        al "Thank you so much, Jezera."
        je "Don't worry, little dove. I'm proud of you; you did the right thing coming to me."
        if alexiaJezObedient:
            "Jezera ran her thumb across Alexia's bottom lip, her sensual lips curling into a smile."
            je "Perhaps I'll reward you later."
        "With a little smirk and wave, Jezera returned to the portal and disappeared."
        return
        
#############################################################################################################################################################
            