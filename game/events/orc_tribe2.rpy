init python:

    event('orc_feminist_camp', triggers='map_res_13', group='map_res_orc_tribe', run_count=1, priority=pr_map_res)
    
label orc_feminist_camp:

scene bg26 with fade
show rowan necklace neutral at center with dissolve

"When he saw the female guards at the gates, he didn’t take notice."

show rowan necklace shock at center with dissolve

"When he couldn’t see any male orcs around the village, with the exception of a few kids that couldn’t be older than six, a certain suspicion arose within him."

show rowan necklace neutral at center with dissolve

"And finally, when he was allowed to enter the chief’s tent after a short explanation of his intent, his growing suspicion was fully confirmed."

show rowan necklace happy at center with dissolve

ro "I take it there’s some backstory here?"

orcm2 "Men stoopid. Always fight over human sluts. Think with da dicks, not da brains."

"Rowan thought it an unjust generalization, but with two female warriors pointing their spears at him, he chose to respond with an apologetic smile instead."
"The backstory in question proved to be a simple one. This particular tribe served in the vanguard of Karnas’ army, and used to count its members in thousands. But after going through eleven different tribe leaders-"

show rowan necklace concerned at center with dissolve

"-one of which Rowan had a nagging suspicion he was personally responsible for the demise of, given the recounting of the battle, a fact he decided to keep to himself-"

show rowan necklace neutral at center with dissolve

"-the wife of the first one decided that enough is enough, and it was time to cut their losses and pack home. A decision that did not sit well with the twelfth warchief-"

show rowan necklace happy at center with dissolve

"-and this one Rowan was absolutely certain he was responsible for killing, unless there was more than one orc warleader who chose to “paint male genitalia on his cheeks as a sign of virility”-"

show rowan necklace neutral at center with dissolve


"- and the tribe split up. Most of the women went with the new matron, who now sat before him, while the men stuck with Karnas. Given how the war ended, he had to commend the matron’s foresight."

"… Not it was particularly difficult to foresee how the war would end, given how the same conflict played out numerous times in the past, but orcs weren’t known for learning from past mistakes."
"Regardless, this now led to a difficult conundrum. Given the tribe’s history, he couldn’t really see how he could convince them to join a yet another demon-driven crusade…"
"But at the same time, he could just have Andras wrap the place up, in the usual fashion."

menu:
    "Propose a loose alliance.":
        $ released_fix_rollback()
        "It wasn’t ideal, but it was making the best of a bad situation. Surely there would be no shortage of hotheaded young orcs who’d rather join in on the fight, than waste away in some gods-forsaken valley."
        "His assumption was correct, and the matron looked covertly pleased with the suggestion of taking the village troublemakers away."
        $ change_recruitment_bonus('barracks', 0.3)
        $ castle.villages_income += 0.3
        return
        
    "Convince the orcs with your body.":
        $ released_fix_rollback()
        jump orcfeministSex
        
    "Call in Andras.":
        $ released_fix_rollback()
        $ change_base_stat('c', 5)
        "As amusing as their little community was, it was not Rowan’s job to support local social experiments."
        "Keeping his expression straight, he politely inquired on the matters of the village further. Then, once he was away from prying eyes, he touched his amulet and sent his current location to his demonic overlord."
        "As always, Andras fell upon the village like a plague of locusts, cutting orcs left and right. Against such overwhelming difference of power, the village was quick to surrender."
        "Most agreed to serve. Some, especially the elderly, stated they’d rather die on their feet than live on their knees."
        "Andras applauded the sentiment, then broke a few knees to swiftly uncover the faulty reasoning behind it, and had the remaining opposition collared and sent back to the castle as slaves."
        $ change_recruitment_bonus('barracks', 0.3)
        $ change_prisoners(5)
        return
        
    "Tell them about Tarish." if orciad_ally == "tarish":
        hide rowan with dissolve
        "The village matron was not the first orcess Rowan had met that thought she could do a better job leading them than men."
        "He retold the tale of the conflict between Ulcro and Batri, and how, ultimately, with trickery and guile, it was Tarish who emerged victorious and now led the biggest orc army in Rosaria."
        "Suffice to say, the matron was impressed. She asked to meet Tarish in person, and promised her support in full if the tale proves true."
        "Rowan arranged for the meeting to happen, then went on his way, letting his subordinates handle the rest."
        $ change_recruitment_bonus('barracks', 1)
        return
        

label orcfeministSex:

ro "I understand, and sympathize with your plight. Most of the men I served under where like that as well."
ro "Aggressive, domineering, needlessly violent."
ro "Personally, I prefer a… Softer approach."

"He lowered his voice ever so slightly, adding a seductive undertone to his words. But the matron either remained oblivious to it, or chose to purposely ignore it."
"The two guards by his sides, however, responded more keenly to his attempts. The one on his left eyed his crotch with poorly concealed interest, while the one on his right wiggled her eyebrows at her companion."

orcm2 "Bah, men always the same. Make empty promises, give no guarantees. Heard it a dozen times. Leave me."

"He bowed before the camp leader, and left the tent. It wasn’t long before the two guards approached him, the one leading them flashing him a toothy grin."

grino "Well, well, well… Been a while since we had such a fine male wander here. How long has it been?"

shyo "A year… Methinks?"

grino "Methinks a year too… And to think our good matron was so quick to dismiss him… The old hag forgot the benefits of having a dick around."

show rowan necklace shock at center with dissolve

"Her hand gripped his ass suddenly, making him yelp."

grino "Though personally, I’d like to have a go at THAT, than take in the thing between his legs… And you?"

shyo "Is a real one… Better?"

grino "Oh, SO much BETTER."

show rowan necklace neutral at center with dissolve

"Rowan eyed his newfound supporters. The grinning orcess was tall, muscular, and kept rubbing his butt quite shamelessly. The second one was more lithe, more generously gifted around the chest, but evidently lacking in self-confidence."

ro "I take it you don’t exactly approve of how things are done around here?"

grino "Oh I do approve! It’s just that some of us think that as we sit here, twiddling our thumbs waiting for gods knows what, the world moves on without us."
grino "And in time, it will forget us. Or crush us to dust so we fit whatever new grand design it has for the orcs, without ever asking us for our opinion."
grino "So I tell you what… As long as your demon masters let us keep some male slaves for entertainment, we won’t mind throwing in with you lot… And don’t worry about any… Internal opposition. That’s my problem now, not yours."
grino "Though of course, we would need a… Proof of good intentions, hm?"

"She pushed in direction of one of the tents, and brought out a… Quite imposing strap-on from one of her belt sacks. Rowan didn’t know why she carried it around, though seeing the shy orcess blush at the sight of it, he could make an educated guess."

grino "Get on with it, mister human… I’d like to see this settled by sunrise."

menu:
    "Betray they guards and try diplomacy again.":
        $ released_fix_rollback()
        ro "That’s a bit quick, don’t you think?"
        grino "And what’s the point of waiting?"
        ro "All I can say… I need some time to discuss this with my superiors, alright? I’ll get back at you tomorrow."
        "The orcs grumbled but agreed, with the domineering shooting him unpleasant glances. No matter."
        if check_skill(6, 'diplomacy')[0]:
            hide rowan with dissolve
            "By noon the following day, both of them ended up with their head on pikes, charged with treason. The matron was grateful for his information, not at all surprised there were those who would see her deposed."
            "In the end they agreed to a simple, yet favorable arrangement. The village would pay a considerable weekly tribute and send most of their young to serve in the Bloodmeen army."
            $ change_recruitment_bonus('barracks', 0.5)
            $ castle.villages_income += 0.5
            return
        else:
            hide rowan with dissolve
            "Sadly his attempt at revealing the brewing mutiny proved fruitless, as matron would not believe a single word from Rowan’s mouth."
            "Further negotiations broke down quickly, leaving Rowan with a simple choice: To leave, or to call in Andras and let him sort this place out."
            menu:
                "Subjugate the village by force.":
                    $ released_fix_rollback()
                    "As always, Andras fell upon the village like a plague of locusts, cutting orcs left and right. The matron and her guards were among the first to fall, courtesy of Rowan himself."
                    "After that, the village was quick to surrender. Most agreed to serve. Some, especially the elderly, stated they’d rather die on their feet than live on their knees."
                    "Andras applauded the sentiment, then broke a few knees to swiftly uncover the faulty reasoning behind it, and had the remaining opposition collared and sent back to the castle as slaves."
                    $ change_recruitment_bonus('barracks', 0.3)
                    $ change_prisoners(5)
                    return
                    
                "Just leave them be.":
                    $ released_fix_rollback()
                    $ change_base_stat('c', -3)
                    "Despite the twins’ quotas, it just didn’t feel right to destroy a settlement that for the most part managed to live in peace with the surrounding villages."
                    "With a heavy heart, Rowan bid the orcs goodbye, knowing fully well he’d have to try extra hard to make up for the loss here."
                    return
                    
    "Use your ass for diplomacy.":
        $ released_fix_rollback()
        jump orcfeministSex2


label orcfeministSex2:

show rowan necklace concerned at center with dissolve

ro "If you insist so much…"

grino "Oh I do~"

show rowan necklace shock at center with dissolve

"She shoved him again, making sure Rowan had no false impression on who was going to be the top dog in this relationship. The shy orcess followed after them, fidgeting with every step."

grino "Now get out of that shirt, before I rip it open!"

show rowan necklace naked at center with dissolve

"He didn’t have to be told twice. Taking his shirt off, he flexed his muscular chest, eliciting a surprised gasp from the shy one. She was clearly not accustomed to the sight, and kept avoiding his eyes."
"Her friend, on the other hand, was much more brazen in her ogling."

grino "Damn… That’s one hot piece of ass... Do you like it too?"

shyo "Y-yes…"

"The dominant orcess coiled around her meek partner like a snake ensnaring her prey, whispering sweetly in her ear."
"Whenever the hesitant girl tried to look away, she would gently push her face back in Rowan’s direction, and her eyes would always venture to his chest, or to the bulge in his pants."

grino "Poor girl… Never had it in her to disobey our good matron and venture outside to find herself a nice cock to fuck."
grino "I hope this makes you happy, human…"

"She playful twirled the intimidating strap-on, then slid it between the shy orcess’ thighs, making her moan sweetly."

grino "She’s not a virgin, but I guarantee yours will be the first real dick she’s ever had."

menu:
    "“I consider it an honour.”":
        $ released_fix_rollback()
        pass
        
    "(What is up with people and their fixation on virgins...)":
        $ released_fix_rollback()
        "He simply did not get what the fuss was all about, but after eyeing the strap-on again, wisely decided to keep that thought to himself."
        ro "I consider it an honour."
        
grino "Good. You should."

"Another gasp escaped the meek girl as his cock sprung worth, half erect but growing from the perverse display before his eyes, the domineering orcess still teasing and groping her less experienced friend."
"The shy orcess struggled to escape her friend’s grasp, but did so with no actual strength or real effort in her movements. A futile display, that convinced no-one sans the girl herself."

grino "Come on now, enough playing coy. Touch it."

shyo "It’s so..."

grino "{b}Touch it.{/b}"

"This time her voice was sharp as commanding, and the other orcess almost yelped in surprise. Still shivering, she approached Rowan."
        
show rowan necklace naked aroused at center with dissolve
  
"Her hand touched his cock, first shyly, but with every stroke growing more confident in her caress. She watched, wide-eyed, as it hardened under the slow dance of her delicate fingers."

shyo "… So warm…"

grino "A dildo can be fun, but nothing beats the real deal."

"Rowan blinked, the shy orcess suddenly disappearing from his view, leaving behind her a loud “eep!”. The grinning one shoved her onto the bed, tired of her antics."

grino "Alright slut. Now you strip. And make it quick."

"Reduced to the role of a bystander, Rowan watched the orcess “help” her friend, tearing one piece of clothing after the other, seemingly callously, but the more he looked, the clearer it became she wasn’t destroying anything too valuable…"
"A game they had played several times, it seemed..."

grino "There you go… Open wide."

"Flashing Rowan a cocky grin, the domineering orcess guided her partner’s hands to her crotch. The hesitant fingers wrapped around her pussy lips, and with her legs spread wide, the shy orc presented her honeypot to the hero."

shyo "P-please don’t stare… It’s embarrassing…"

show rowan necklace naked at center with dissolve

grino "“Don’t stare, don’t look, kyaa, it’s embarrassing!” Oh, do you never grow tired of that act?"
grino "I certainly don’t, haha!"

"It would be a lie to say he wasn’t seeing the charm either. The shy orcess had a lithe, slender body, without a hint of fat in it, but not as muscular as to appear amazonian. The modest, but pleasantly rounded breasts added an air of femininity to an otherwise fighter’s body."
"And the shy, reluctant act, so clearly masking fascination and desire, from the way her eyes constantly ventured to his cock, to the heaving of her breasts and way she licked her lips..."

if raeve_keep_rowan_claimed_helayna == True:
    "This must have been what his and Helayn’s first time would look like, if things turned out differently."
    "Maybe without the additional company."
else:
    "Alexia was a lot less bashful during their first time… But this was also nice."
    
grino "What are you waiting for, you dumb hunk? Show my little slut what it means to be with a man!"

"An uncertain smile graced the shy orcess as he climbed atop of her, his hard phallus pressing against her stomach. Voice wavering, she begged him:"

shyo "P-please be gentle?"

grino "Ha! Be anything but!"

menu:
    "Go hard.":
        $ released_fix_rollback()
        ro "I think your mistress knows your body a lot better than you do..."
        scene black with fade
        shyo "E-eh? AAAh!"
        #CG 1
        scene cg401 with fade
        pause 3
        "A pained moan escaped her lips as Rowan pushed into her savagely, having no problem in penetrating her wet pussy. Despite all her halfhearted noes and resultants protests, her lower lips offered no resistance, parting welcomingly before Rowan."
        shyo " Aaa-aaah?!"
        grino "Ahaha! What’s with that perverted moan you slut? You never scream like that under me! Trying to make me jealous?!"
        shyo "N-noo-aah!"
        "Her words of denial drowned under her own moans, and soon conversation proved impossible, the shy orcess responding to his rapid thrust with sweet cries of ecstasy, completely ignoring her friend."
        grino "So quick to forget about the one who first showed her how much fun it is to play with your own pussy… I’m hurt!"
        grino "I think I’ll have to punish you human, for turning her against me."
        "He felt her feel his ass again, a wet finger pushing against his lower entrance. His surprised gasp was quickly silenced when the orcess below threw herself at him, sealing his lips with a passionate kiss."
        grino "So you do you remember where your loyalties lie! Keep him steady for me…"
        
    "Go easy.":
        $ released_fix_rollback()
        scene black with fade
        show rowan necklace naked behind black
        ro "Shh… Relax… I promise it will feel divine."
        #CG 1
        scene cg401 with fade
        show rowan necklace naked behind cg401
        pause 3
        "Rather than take her savagely, he cupped her face gently, caressing her cheek as the tip of his cock teased her entrance. She looked almost confused at the unexpected gesture."
        grino "What are you playing at, human?"
        ro "Nothing… Just making sure she enjoys herself."
        shyo "I-I… Mmmm?!"
        "He silenced her protests with a passionate kiss, his hands exploring her feminine mounds. Slowly, he pushed her lower lips open. There was no need for hurry. He’ll show these women how a hero-"
        ro "?!"
        shyo "Aaa-ah!"
        "Someone slapped him in the ass with full force, the sudden sensation making him jerk violently. He thrust into the orcess, sliding easily, but-"
        grino "Don’t forget why you’re here, human. It’s not to please just her, but also {b}me{/b}."
        grino "I think I’ll have to punish both of you for trying to hog all the fun…"
        "He felt her feel his ass again, a wet finger pushing against his lower entrance. In a surprising reversal, his pained gasps were silenced with a passionate kiss as well, as the orcess under him threw herself into his arms."
        grino "Feeling remorseful now? Ha, fair enough! Keep him steady for me…"
        
"He shuddered as she kept prodding and exploring his insides, spreading some sort oily substance inside his anus. Wet and ready..."

grino "Now, tell me you want it."

ro "I-"

grino "Not you, you dunce. Her!"
grino "Tell me you want me to fuck you through the human on top of you. Tell me you want to feel me thrust his cock right into that slutty pussy of yours!"

shyo "I- I- I-…"

grino "Enough playing coy! Tell me what you want!"

shyo "I-I-"
shyo "I want you to fuck me with a male cock! I want to feel you fuck me, and have a dick inside of me! It just feels so, so..."

"She took the finger out, and soon, he felt something else, something much bigger, replace it."

grino "Treacherous little cunt… I’ll make sure to punish you good for that~"

#shake screen
#cg2
scene cg402 with fade
show rowan necklace naked aroused behind cg402
pause 3

ro "A-ah!"

"He couldn’t stop the pained moan as she brutally forced the stone strap-on into his ass. She showed him only the bare minimum of consideration, just enough to avoid ripping him apart, but not enough to make the process in any way pleasurable."
"As she pushed into him further, the orcess below him embraced him in an almost loving fashion, kissing his lips and his face, whispering sweet nothings into his ear."

shyo "I-I know how it feels… J-just relax, it will soon feel really good~"

"The warmth of her body contrasted with the cold stone up his ass, contrasted with her wet, needy pussy~"

grino "Damn you’re tight! You must not be doing this very often!"

ro "Can you please- aaah!"

show cg403 with dissolve
pause 3

"She shoved it all the way in, pushed him all the way into her lover~"

grino "How does her pussy feel, human?"

ro "G-great~"

grino "Fuck I’m jealous… But I’ll make use of what I have… Now… Start pulling out slowly…"

"What followed Rowan could only describe as several hours of lust driven insanity. The Orcess would not let him rest. Pulling his hair, slapping his ass, she had him follow her bidding, her stone cock in his ass proof of his submission."
"Her artificial dick set the tempo, tempo Rowan had to follow religiously. Whenever he’d feel her pull out, he pulled out as well. When she pushed, he relaxed, his hard dick thrusting into the panting lover under him."

shyo "M-more! Please, mo-ore!"

show cg404 with dissolve
pause 3

"Thrice he came in her. Normally it would be nearing his limit, but with his ass stimulated he would not go soft, the sensation below his waist slowly growing into a mixture of pain and pleasure."
"It was sweet agony, accompanied by grunts of efforts, triumphant laughter, and almost constant cries of ecstasy."

shyo "Y-yes! Fuck me more! Both of you, fuck m-me mooore!"
shyo " I-I never knew a male’s dick would feel so good! Harder, please, harder!"
shyo "Harder! I said harder!"

scene black with fade
shyo "Fuck me harder, damn it!"

"… … ..."
"… …"
"…"

#shake screen

scene bg26 with fade
show rowan necklace naked angry at center with dissolve

"Feeling someone approach him, Rowan sprung up, sword in hand, already aimed at the assailant’s neck."

grino "Holy fuck, you’re jumpy! It’s me, you dunce!"

show rowan necklace naked neutral at center with dissolve

ro "Sorry, it’s just-"

grino "No, no, that’s fair. I admire the reflexes."
grino "Get dressed, human. Time for you to meet our new matron."

show rowan necklace naked angry at center with dissolve

"Grudgingly, Rowan forced himself up, trying to ignore the pain in his ass. He would not be sitting straight for a week… Good luck explaining that to Alexia..."

show rowan necklace neutral at center with dissolve

"Ten minutes later, he was outside, dressed up and looking spry and ready for action, as he always was. Immediately, a pair of unfamiliar guards started to lead him towards the warchief’s tent."

show rowan necklace shock at center with dissolve

"He was greeted by the very orcess that was squealing under his cock the night before, but now she was dressed much more ornamental, in a brightly colored tunic that were reminiscent of the robes of the previous matron."

show rowan necklace neutral at center with dissolve

"She welcomed him with a warm smile, her eyes devouring his body. The look in them made him slightly uneasy, and the way she licked her lips when looking at his crotch did not help."

shyo "Emissary of Castle Bloodmeen. Earlier this morning, the tribe has reconvened to once more discuss your proposal."
shyo "After addressing everyone’s concerns and dealing with the accordingly, we’ve decided to support you and your demonic patrons, in exchange for a fair share in the spoils, expressed in the form of male slaves."
shyo "We will send our warriors by the end of the week."
shyo "Go now."

show rowan necklace shock at center with dissolve

"He got ushered out of the tent instantly. A bit dazed, he looked at the grinning orcess who waited for him outside, uncertain what to say."

grino "Shocked?"

show rowan necklace concerned at center with dissolve

ro "That’s… Quite the change. I thought you would be the new matron?"

show rowan necklace neutral at center with dissolve

grino "Me? Ha, nah. Never had the head for all this management stuff. The previous matron –"
grino "-please pay your respects when leaving, the head is mounted near the entrance, second from the left –"
grino "-she always had us rob or trade for books, saying “Males stoopid, think they know all. You read. You see you know shit. You learn.” Guess I have more of a man in me than just the penchant for being on top, since they never interested me that much."

"She pointed behind her, winking to the hero."

grino "She on the other hand? Devoured everything she could get her hands, can recite half of that stuff from memory. I’m sure she’ll do great, she just has some trouble getting out of her shell. Glad you were around to help with that, stud."

ro "… No problem?"

grino "Oh, don’t be modest, I know how exhausting it must have been for you!"
grino "You know, it’s always the shy ones that are the biggest sluts. Now she won’t shut up about all the things she wants to try… I believe double penetration is first on the list? And I think she wanted to inquire if you have futanari magic at your disposal?"

show rowan necklace concerned at center with dissolve

ro "(Sweet Goddess, what I have I unleashed upon this innocent land.)"

show rowan necklace neutral at center with dissolve

grino "But I’ve wasted enough of your time here. You can go. Please, tell your demonic masters their manwhore performed most admirably."

show rowan necklace shock at center with dissolve

ro "Wha-"

show rowan necklace angry at center with dissolve

ro "Hold on, what exactly do you think my position is in the castle?"

grino "… Male whore, no?"

show rowan necklace concerned at center with dissolve

"The genuine confusion in her voice stung. It really did."

ro "(Maybe that’s for the better… I don’t want them walking around, boasting about fucking the Lord of Castle Bloodmeen.)"

show rowan necklace neutral at center with dissolve

"Choosing to keep what little remained of his pride, he finally bid the orcess, and the strange camp, farewell."

hide rowan with moveoutleft

scene black with fade

"He continued his journey, armed with the knowledge that for all of his troubles, at least he managed to secure another village, without Andras' help to boot."

$ change_recruitment_bonus('barracks', 1)
return
