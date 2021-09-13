init python:
    
    event('lady_farquarter', triggers="week_end", conditions=('week > 34', 'society_type == "feudalism"',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('succubi_murder_mystery', triggers="week_end", conditions=('week > 30', "castle.buildings['sanctum'].lvl >= 1",), group='ruler_event', run_count=1, priority=pr_ruler)
    
label lady_farquarter:
    
scene bg6 with fade
show rowan necklace angry at midleft with dissolve
show liurial happy at midright with dissolve

"Liurial hummed to herself as she placed papers atop Rowan’s desk. Watching the stack rise so high made him want to punch someone."

liur "Oh, one more thing, Sir Rowan. There’s a visitor here to speak to you."

show rowan necklace neutral at midleft with dissolve

ro "A visitor?"

liur "From Rosaria. One of the landed knights who agreed to swear fealty in return for protection. Another success of your recent efforts. I have been told that he wishes to speak to the “Lord Quartermaster” to pay him homage."
liur "I was informed his name was a Sir Faunch of Tonio."

show rowan necklace angry at midleft with dissolve

"Rowan groaned. He’d heard of Sir Faunch before, even if the two had never met. Knights in general had a bad tendency of being annoyingly concerned with formalities. Being in the middle of the food chain made the forms and structures of society a comforting blanket."
"But, even for a knight, Sir Faunch had a reputation for being an uptight pain."

ro "Can’t you send him away?"

show liurial neutral at midright with dissolve

"Liurial shook her head."

liur "Most unlikely. Of my experiences with human knights, they have been shown rather tenacious on matters of formality."

show liurial happy at midright with dissolve

"She giggled to herself."

liur "Present company excluded, of course…"

show liurial neutral at midright with dissolve

liur "If you prefer, I can attempt to stall him to give you time to prepare."

"Rowan shook his head. He had a better idea."

show rowan necklace happy at midleft with dissolve

ro "No. How about you just deal with him?"

liur "Meaning…?"

ro "I’ll hide. You tell him that you’re the quartermaster. You’ll tell him you’re a noble here. Then you can just deal with him until you go away."

"She blinked twice."

show liurial sad at midright with dissolve

liur "Sir Rowan. I didn’t exactly run away from home to…"

show rowan necklace neutral at midleft with dissolve

ro "I spend my weeks trekking through entire countrysides, often in the rain and mud. You can handle one conversation."

liur "..."
liur "Please don’t make me do this. I don’t like people. Pleaseeeee."

"She brought her hands together in a begging motion. Rowan found there to be a distinct “puppy dog” quality to it. "

show rowan necklace happy at midleft with dissolve

ro "Denied."

show liurial angry at midright with dissolve

"Liurial huffed."

if liurial_domination_count > 0:
    liur "Sadist."
    "Rowan thought back to some of the recent activities the two of them had engaged in. From her, there was some truth in the moniker…"

else:
    liur "Cruel."

"Just then, there was the sound of approaching footsteps. Loud and self-assured, like they came from a man who owned the world. Rowan brought the papers on his desk together into a miniature fort and hid behind them."

hide rowan with dissolve
show rosarian knight neutral at midleft with moveinleft

faunch  "Greetings!!!"

"Liurial shot Rowan a glare, but rushed over to meet the guest."

show liurial happy at midright with dissolve

faunch "I am Sir Fauch of Tonio and I am looking for the quartermaster of this fine castle."

liur "Well you have found, er, her. I am the Quartermistress! Lady, um, Far...Quarter. Lady Farquarter of Bloodmeen, keeper of the coin. It is a pleasure to meet you."

"The knight went to one knee, oblivious to Liurial’s stumbling speech."

faunch "May I have the honour of kissing your hand?"

"Rowan thought he saw Liurial mouth some words to him, but he couldn’t make out what she was saying, besides none of it being especially happy."

liur "V-very well!"

"The Knight took her hand and placed a kiss on it."

faunch "I come to you today, because I have brought a gift. A token of the new bonds between liege and subject. Connected as though by phantom threads from many rivers and mountains apart."

"The knight reached into his satchel and took out a massive sack. It dropped to the floor with a clink. Inside there must have been a great deal of wealth."

faunch "It is bound in the code of House Faunch that on every tenth year, we are to pay a great tithe to our liege lord. For five hundred years, we have kept faith to this noble oath."
faunch "This is the tithe of a decade past!"

#liur shocked

"Rowan’s eyes near bulged from his socket. That was a great deal of money. Enough to double the week’s income just from the actions of a single landed knight."
"Liurial’s mouth gaped slightly as well. "

faunch "As the new liege of house Faunch, we hope that Bloodmeen accepts this gift as a sign of fealty and eternal connection."

liur "Y-y-yes. Of course. This is a most proper gift. I, Lady Farcourt, accept this gift in honor of castle Bloodmeen."

faunch "My lady? Farcourt? I must protest some confusion. What did my lady say her name was? I had heard Farquarter the first time."

show liurial neutral at midright with dissolve

liur "Oh."
liur "..."

show liurial happy at midright with dissolve

"There was a moment of standing about awkwardly. Liurial looked like a recently caught fish wiggling on the planks of a dock."

show liurial neutral at midright with dissolve

faunch "Now, we must engage in the ritual of the tithe. I will show you the steps. It is an honor I have had the honor of doing but twice in my life. But, my father did it many a time and-"

liur "How, uh, long is this ritual, brave knight?"

"The knight gave her a dramatic sweep of his arms."

faunch "Oh, it should not take more than two hours, Great Quartermistress. It would not befit the honor of the bond between House Faunch and Bloodmeen if it were to be any shorter."
faunch "Indeed, it would be a dishonor to the noble virtue of your ladyship as well."

show liurial happy at midright with dissolve

"Liurial strained her lips into something that could pass for a smile."

liur "Oh yes. My honor. W-wonderful."
liur "Very well. We can begin if you like."

scene black with fade

"It was not often these days that one of Rowan’s plans went better than expected. But, Rowan couldn’t believe just how much his earlier choice had been vindicated."
"Liurial did not end up making it the entire two hours. After the first hour, she managed to stutter out an excuse that got through Sir Faunch’s dense ears."

scene bg6 with fade
show rowan necklace happy at midleft with dissolve
show liurial angry at midright with dissolve

"Liurial sat down on the other side of the desk with a very uncharacteristic glare."

liur "...Why?"

"Rowan chuckled to himself. He’d made wonderful progress on his work in the meantime."

ro "I thought it’d be funny...Lady Farquarter."

"She answered with an angry little squeak."

ro "Did you see how much money he brought?"

show liurial neutral at midright with dissolve

liur "In truth, I couldn’t believe my eyes, Sir Rowan. It is surely a great sum."
liur "..."
liur "I’m assuming I will be required to count all of the gold as well?"

if liurialSex == True or (liurial_domination_count > 0 and liurial_orgasm_control_on == False):
    "Rowan swatted at the air, as though batting the question away."
    ro "Of Course. But, I’ll make sure there’s a reward at the end for you."
    show liurial aroused at midright with dissolve
    if liurial_orgasm_control_on == True:
        liur "There will!?"
        "She nearly jumped from her seat. All of the annoyed lines left her face in an instant."
        liur "You haven’t let me have release in so long! Oh thank you!"
        "Rowan chuckled to himself."
        ro "I never said it would be that."
        ro "But, if you do a good job counting his tithe, I’ll consider it."
        "Liurial ran back towards the sack, so she could start on the work. No doubt it was going to be a long night for her..."
    else:
        "There was no confusion from the glint of his eye what Rowan meant when he said reward. Especially when Liurial gave a bashful smile back. It was going to be a long night for her."
        
else:
    ro "How did you know?"
    "Liurial sighed to herself, but diligently went to start the count. It was going to be a long night for his poor secretary indeed."
    
$ change_treasury(50)
return
    
########################################################################################
########################################################################################
########################################################################################

label succubi_murder_mystery:

scene bg23 with fade
show rowan necklace neutral at midleft with dissolve
show xzaratl neutral at cliohnaright with dissolve

"Rowan stood solemn like one of the innumerable blackstone gargoyles squatting within the blue-tinted pleasurescape of the Dark Sanctum."
"Upon his face he bore a grim expression. A solemn acknowledgement of the two prostrate bodies lying frozen in mid-coitus in front of him."

ro "So, I take it this is the emergency?"

#xzaratl concerned
xz "Yes..."

"Rowan had to suppress a shiver. The amount of blood splattered on the ground prognosticated a particularly gruesome end for the star-crossed pair. The bed was soaked in it, its frilly pillows and silken covers coated in a thick red stain."
"It was hard to look at them. The two naked bodies lay like piled matchsticks atop one another. They had died in a terrible way. Rowan hardened his brow."

show rowan necklace concerned at midleft with dissolve

ro "Who were they?"

xz "The Succubus was named Ishta. "

#xzaratl neutral

xz "She was my second, my enforcer in the Sanctum. Inferior only to myself in both power and prestige. "

"X'zaratl stepped forward, staring down at the body with a thoughtful look. She placed one of her four hands upon the bed, lifting it up to stare at the lifeblood clinging to her fingertips."

xz "I depended upon her to keep the others in line, when the Twin’s duties took me elsewhere."
xz "As for the mortal… I have no idea. Maybe one of her pets. My siblings keep so many these days, I don’t bother to keep track of them all."

"The slave’s lifeless body was draped atop his mistress, his position indicating intense copulation in the immediate moments leading up to his demise."
"He was a distinctive fellow: bald, tan, with piercing green eyes and a handsome -if rugged and wind blown - face."
"Rowan reached out and took the limp hand of the Succubus lying face-up upon the bed." 
"Her eyes were lidless, staring up towards the ceiling, gazing into eternity. A small line of blood trailed from one corner of her full lips, marring her otherwise beautiful features."
"Given the character of the blood stains on the bed, the worst injuries were far lower on her body. They were mercifully covered up by the dead corpse of her lover splayed out atop her."
"She was dead cold. Rowan let go of her hand, and it dropped with boneless weight back onto the bed."

ro "I’ve seen {i}harpies{/i} use more subtle evisceration methods. This was no act of mortal men. "

#xzaratl concerned

xz "An act of ‘mortal’ men, no. But {i}men{/i} are not the only ones capable of such cruelty."

"Her worried frown spoke volumes."

show rowan necklace neutral at midleft with dissolve

ro "So you’re saying it was a crime of passion, then. Some kind of rage killing."

"X'zaratl nodded solemnly."

xz "Lesser Succubi in a brood sometimes suffer from these kinds of internal squabbles."

"The Demoness’ shrug was nonchalant, as if capital murder was just acceptable collateral in the pitiless realm of Kharos."
"...A chill ran down Rowan’s spine as he considered the true implications of the thought. X'zaratl did not seem particularly broken up at her former second’s grisly demise, so much as annoyed at the inconvenience of the event itself. "
"He stood up and brushed himself off, glancing around the room in search of anything odd or out of place."

xz "You see now why I wanted your help in this."

"Rowan’s brow tightened. He felt his hand drift towards the reassuring weight of his sword pommel."

ro "No. {i}Why{/i} have you brought me into all this?"
ro "If what you say is true, then this is a personal matter, one that should be solved amongst the Succubi. "
ro "Why come to me, and not the Twins?"

"X'zaratl’s easy smile fell away. For the first time since Rowan had met her, she looked… troubled. Her four arms curled around herself in a protective cocoon."

xz "I am trying to avoid bringing our masters into this matter. As it might reflect poorly on my perceived ability to keep my kin in line."
xz "My little siblings no doubt all intend to lie through their teeth. Given the circumstances, I do not blame them for doing so. "

#xzaratl angry

xz "But this is unacceptable. It is one thing for a minion to carry out a personal grudge, it is quite another to do so to the {i}detriment{/i} of her mistress’ influence."
xz "Justice must be done."

ro "To whom? You sound like you already know who is to blame."

#xzaratl happy

xz " That is precisely what I’m hoping you’ll help me discover, Rowan. I figure that a mortal’s perspective might shed light upon this mystery in a way that a Demon’s mind might not."

#xzaratl neutral

xz "My brood are now detained in their rooms, denied their harems until the investigation is finished."
xz "Would you do me a kindness, and join me in their interrogation?"

menu:
    "Agree to help.":
        $ released_fix_rollback()
        "Rowan sighed. Of all the odious tasks he had been expected to deal with in Bloodmeen, conducting a murder investigation with a Demon certainly wasn’t one of them."
        ro "Where should we begin?"
        xz "With those who stand the most to gain from Ishta’s death."
        xz "I enforce a strict but informal hierarchy in the brood. I am on top, of course. {i}Always{/i}."
        "X'zaratl’s unsubtle sexual purr was so blatant that Rowan couldn’t help but grow a bemused smile."
        xz "-But beneath me, power comes to those ambitious or deceitful enough to claim it."
        xz "Ishta has been my second for some time now. Few would dare challenge her position openly. But there are those in the brood who hold deep grudges against her."
        #xzaratl angry
        xz "We must suss out the truth. Come, there isn’t much time. Ishta’s body already grows cold."
        jump xzaratlInterrogation1
        
    "I don’t have time for this.":
        $ released_fix_rollback()
        show rowan necklace angry at midleft with dissolve
        ro "X’Zaratl, I am trying to run a war effort. Your brood’s internecine conflicts do not interest me."
        "X’Zaratl’s expression fell as Rowan took a last look at the dead bodies. Demon squabbles were a messy and pointless affair."
        ro "Deal with this problem how you see fit. This is why the Twins brought you in to lead the Dark Sanctum in the first place."
        ro "And next time: don’t bother coming to me about something as trivial as this."
        "Rowan swept from the room in a smooth movement, hustling from the area as if to escape the accusing eyes of the dead slave looking at him."
        return
        
label xzaratlInterrogation1:

scene bg23 with fade
show rowan necklace neutral at midleft with dissolve
show xzaratl neutral at cliohnaright with dissolve

"The two came to the first of the sealed chambers that were the Succubi’s personal quarters. This one was directly next door to Ishta’s abode." 
"It was a large, circular room encircled by mystical curtains. He walked up to them and gave a tug, but nothing happened. So far as Rowan could tell, there was no means of piercing through the seemingly thick fabric."

ro "So who is first?"
        
xz "This is Ahrima, one of my first recruits to the Dark Sanctum. She’s an irritable creature, aggressive and ill-tempered."
xz "...And also a prime suspect in Ishta’s murder."

ro "What makes her your first choice?"

xz "Location and motive. The two {i}hated{/i} each other."
xz "With most broods, alliances and rivalries can shift with the breeze as each competes for position and privilege."
xz "But despite that fact, the two have never worked together. That should speak to the level of enmity we’re dealing with here." 
xz "Expect an icy greeting, she’s been stewing in her room for a while, now."

"X'zaratl pulled aside the silken curtains, their enfolding curves bending aside to reveal the sumptuous bedroom of a Succubus."

hide xzaratl with dissolve
show succubus 2 neutral at midright with dissolve

"Ahrima stood in the corner of the room with her back to Rowan."

ro "{i}Ahem{/i}."

"At the sound of Rowan’s voice, Ahrima turned, her slitted eyes spreading wide as she took in the sight of the male in front of her. The Succubus’ gaze swept across his form before settling on his face." 
"Her eyes darted down to look at Rowan’s sword before meeting his gaze once more. A cold smile spread across her lips."

ahrima "My my, so Lady X'zaratl sees fit to slake my thirst?"
ahrima "You’ll make a scrumptious morsel, little mortal."

ro "You’re Ahrima, yes?"

"Her catspaw smile was wide and curling. She slunk over towards the bed, bending forward to display her feminine curves to him."

ahrima "‘Mistress’ will do."

show rowan necklace angry at midleft with dissolve

ro "I’m here to investigate Ishta’s murder on behalf of the Twins."

ahrima "Oh an ‘agent’ of the Twins, is it?"

"The Succubus moved closer, her bare footsteps across the carpet silent on the approach. Her eyes were fixed to him as she moved to step into his personal space."
"Rowan drew the first inch of his sword free from its scabbard, flashing the Succubus a warning look."

ro "Don’t trifle with me, whore. I’m no more pleased to be here than you are."

"Far from being intimidated, the Demon let out an annoyed huff. She plopped her bare bottom onto the bed and folded her arms together."

ahrima "Figures she sends a prude to waste my time. "
ahrima "What do you want from me then, mortal?"

ro "Answers."

ahrima "Then you stuffed your cock up the wrong hole, honey. I don’t know who killed the bitch."

$ ahrima1aSeen = False
$ ahrima2aSeen = False
$ ahrima3aSeen = False

$ niseiSlaveClue = False
$ ryleaLoverClue = False

label ahrimaQuestions:

show rowan necklace neutral at midleft with dissolve

menu:
    "Where were you when the murder occurred?" if ahrima1aSeen == False:
        $ released_fix_rollback()
        "The demon seemed amused at this particular line of questioning. She rolled over onto her back on the bed, stretching out to display her full, feminine curves to him."
        ahrima "Looking for ways to undermine dearest Ishta, of course. Seems like whoever snuffed her out took a far more… {i}direct{/i} route."
        "Her grin was predatory, her eyes lidding low as if to invite Rowan to celebrate the demon’s grisly demise by joining her on the bed."
        show rowan necklace angry at midleft with dissolve
        ro "I’ll ask again: {i}where were you{/i}?"
        ahrima " I have no alibi, honey. I won’t pretend to peddle false stories to you."
        ahrima "I was in my room, in fact. Trying to listen in on that skank misusing a perfectly good cockslave."
        "The demon shrugged, gesturing with a hand towards the outside."
        ahrima " I got distracted, and was busy fucking the brains out of some of my concubines when X'zaratl burst in and confined us to our rooms."
        ro "Did you see anything suspicious? Did you see anyone enter or leave the area?"
        ahrima "here were several cocks in my face at the time. I saw dick."
        ro "Do you have {i}any{/i} other witnesses who might have seen you in the minutes before the body was discovered?"
        "Ahrima giggled at the mere notion."
        ahrima "None save my own concubines. But, you should know how trustworthy a Succubus’ pet can be!"
        ahrima "So willful, so free spirited! And they’d {i}never{/i} lie for the sake of their mistress, would they?"
        ro "I think I get the point."
        ahrima "Then you know why I don’t bother to give you empty excuses. I was alone, for all intents and purposes."
        ro "How inconvenient for you."
        ahrima "Life is often a series of inconveniences, no?"
        ahrima "Like, how {i}inconvenient{/i} it is for all involved, that X'zaratl managed to pull an outsider into the brood’s private matter."
        ahrima "It’s almost like she has her own motives for doing so, no?"
        $ ahrima1aSeen = True
        jump ahrimaQuestions
        
    "Do you have any idea who could have done this? " if ahrima2aSeen == False:
        $ released_fix_rollback()
        ahrima "Anyone but me."
        show rowan necklace angry at midleft with dissolve
        ro "That’s hardly helpful."
        ahrima "I’m not in the habit of kissing and telling, honey."
        ahrima "Even if I did know who did it, I wouldn’t tell you."
        ro "Why?"
        ahrima "Because to us, there’s nothing worse than a tattletale."
        ro "Mock me again whore, and I’ll tell X'zaratl that {i}you're{/i} the one to blame for all this."
        "The demon let out an impatient sigh. Ahrima muttered something under her breath that sounded suspiciously like {i}‘mortals.’{/i}"
        ahrima "You don’t get it. This is a matter of trust. If I knew, and I told you, and got {i}caught{/i}…"
        ahrima "Well, lets just say it’s not a happy outcome. My sisters would hate a tattler {i}far{/i} more than whoever killed our dear, departed Ishta."
        ahrima "Telling truths about our kin to strangers is a much worse sin than killing one another."
        $ ahrima2aSeen = True
        jump ahrimaQuestions
        
    "Do you know anything about the human victim?" if ahrima3aSeen == False:
        $ released_fix_rollback() 
        ahrima "How should I know? A slave is a slave."
        ahrima "I rarely bother to keep track of the filthy mongrels and scabby sluts my brothers and sisters lay with in their off-hours. Could you describe him?"
        ro "He was tall. Bald, green eyed and tan-skin."
        "Ahrima sighed, perching her leg up onto her knee in bored invitation. She idly tapped the air with her toe, heedless of her exposed genitalia."
        ahrima "Figures you’d leave out his most telling trait."
        "The demon chewed on Rowan’s words for a moment."
        ahrima "Hm… bald, you said?"
        "The more she considered the thought, the more she seemed to deduce something from it. Her furrowed brow lifted as surprise turned to mirth. A malicious gleam came to her eye."
        ahrima "Wait, was it {i}Nisei’s{/i} little favorite?"
        "Ahrima let out a self-satisfied chuckle, leaning back and spreading her legs wide as she idly touched herself."
        ahrima "This little shakeup in the brood hierarchy just got a whole lot juicier."
        ro "Who?"
        ahrima "Nisei captured him in battle, a little while ago. She hasn’t stopped flapping her jism-suckers about him ever since."
        ahrima "She brought him out to play with me once or twice before, when we were on better terms. "
        ahrima "Good, reliable workhorse in the sack. A shame the old stud is gone, I’d have liked to have gotten a ride or two in."
        ahrima "But my, what a way to go, huh? I’m certain Nisei’s just devastated."
        show rowan necklace concerned at midleft with dissolve
        "Ahrima’s mocking laughter made even the stoic and profoundly jaded Rowan feel awkward and uncomfortable."
        $ niseiSlaveClue = True
        $ ahrima3aSeen = True
        jump ahrimaQuestions

    "What can you tell me about Ishta?" if ahrima1aSeen == True:
        $ released_fix_rollback()
        ahrima "How much bile can you stomach at once?"
        ahrima "She was a cheat, a liar, a hypocrite, and - worst of all - an uninspired lover. And I’m glad she’s dead."
        ro "Could she have had any enemies, aside from you?"
        "Ahrima laughed aloud. It was a curious union of attractive, feminine resonance and grating, lilting cackling."
        ahrima "Of {i}course{/i} she did! We’re demons, not a Solansian nunnery."
        ro "How did she treat the other Succubi?"
        "Ahrima smiled, but her eyes were filled with murder."
        ahrima "Does the term ‘imperious’ mean anything to you, mortal?"
        ahrima "The {i}instant{/i} she became X'zaratl’s new second, she lorded it over all the others. Me especially."
        ahrima "It was insufferable. I’m not surprised someone finally saw fit to finish her off."
        ahrima "The only real shock in all this is that {i}I{/i} didn’t do it."
        ro "Your words would seem to imply the exact opposite."
        "Ahrima’s distant shrug showed how little she seemed to care about that fact."
        jump ahrimaQuestions
        
    "What can you tell me about the other Succubi?" if ahrima2aSeen == True:
        $ released_fix_rollback()
        "Ahrima sighed, rolling onto her stomach as she counted them out on her fingers."
        ahrima "Well, there’s Ishta, whom I’m sure you’ve already met."
        "A dark smile grew on the Succubus’ in response to her own, morbid joke. It sent a shiver down Rowan’s spine."
        ahrima "Then there’s Rylea, the cute hunk. Our brood’s only Incubus, at the moment."
        ahrima "Bit of an overpolite sap, but clever enough. He was Ishta’s favorite boy toy while she was Queen of the roost. The two were ‘inseparable.’"
        "The Demon rolled her eyes, reaching up with one clenched fist to mime jerking off an invisible cock."
        ahrima "I wouldn’t doubt he’s in his doldrums right now, thinking about how he’s lost his cozy spot at the top."
        ahrima "-Then there’s Nisei."
        ahrima "{i}She’s{/i} a curious type: tends to bend in the wind to whatever breeze is blowing."
        ro "What do you mean?"
        ahrima "Ishta wasn’t always X'zaratl’s second. There used to be an Incubus in charge, and Nisei was his favorite lover."
        ahrima "Then Ishta subjugated him, and kicked him out of the harem, leaving Nisei swaying in the breeze."
        ahrima "We’ve allied a few times in the past. She’s a fun lay, if a bit too soft for my tastes. The woman can barely keep her wits together when there’s something convenient to sob about."
        ahrima "Between you and me: I see right through her crocodile tears. Just be ready for some waterworks when you go talk to her, huh?"
        "Ahrima sat up on the bed and hummed to herself, her head tilting."
        ahrima "And then, of course, there’s Deandra."
        ahrima "Our ‘little sister.’ Such a dear. If you value your testicles, don’t take your eyes off of her for a second. She wields lies like Andras wields that big, red rod of his."
        ro "They all sound like quite the charmers."
        "She blew a kiss in Rowan’s direction."
        ahrima "Careful whence you tread, mortal. We demons play {i}rough{/i}."
        $ ryleaLoverClue = True
        jump ahrimaQuestions
        
    "What was Ishta doing in the arms of another Succubus’ pet?" if ahrima3aSeen == True:
        $ released_fix_rollback()
        ahrima "Fucking, if I had to guess."
        show rowan necklace angry at midleft with dissolve
        "The Succubus let out a sultry laugh at the sight of Rowan’s unhappy frown."
        ahrima "Oh, lighten up mortal! What did you {i}think{/i} they were doing? Playing at marriage?"
        ro "I’m looking for a possible motive, Succubus."
        ahrima "Well, speaking from experience, Nisei’s pretty tight-cunted with her harem. I’m surprised she was willing to lend out her favorite stud."
        ahrima "Especially given how notorious Ishta was for… "
        ahrima "‘Breaking toys.’"
        "The Succubus, lounged back against the bed, lazily displaying her body for Rowan’s perusal. She winked at him as her hands trailed lower."
        ahrima "Ishta must have offered her something {i}juicy{/i}. Maybe they were looking to form a potential alliance?"
        ahrima "Oh well. Doesn’t matter either way, anymore. Nisei’s back at the bottom of the food chain now, with nothing to show for it."
        jump ahrimaQuestions
        
    "End interrogation." if niseiSlaveClue == True:
        $ released_fix_rollback()
        jump ahrimaInvestigationEnd
        
label ahrimaInvestigationEnd:

ro "...I think I have everything I need from you."

"Ahrima pouted, rolling over onto her stomach and letting her lower lip quiver in a liar’s pantomime of a jilted lover."

ahrima "Are you certain you have {i}everything{/i}, mortal? There isn’t {i}anything{/i} else I can offer?"

show rowan necklace angry at midleft with dissolve

ro "No. Goodbye."
        
hide succubus 2 with dissolve
show xzaratl neutral at cliohnaright with dissolve

"Rowan stepped through the mystical curtains and came face to face with a waiting X’Zaratl."

xz "...Did you learn anything?"

show rowan necklace concerned at midleft with dissolve

ro "Yes. For one thing, the dead slave didn’t belong to the victim. He was the pet of a Succubus named “Nisei.”"

xz "Nisei?"
xz "Hm… it appears this killing is more complicated than I first thought."

ro "We must speak with her immediately."

#xzaratl happy
xz "My thoughts exactly, Rowan."

label xzaratlInterrogation2:

scene bg23 with fade
show rowan necklace neutral at midleft with dissolve
show xzaratl neutral at cliohnaright with dissolve

ro "What can you tell me about Nisei?"

xz "Nisei is one of my more stable servants. She enjoys the politics, but is not as comfortable with the occasional outbreak of violence as the others often are."
xz "She’s... {i}Pach’na{/i}, what is the word?"
xz "She is {i}“Achranis.”{/i} One who prefers a comfortable bottom to a precarious top."

ro "A submissive?"

"X'zaratl giggled, covering her mouth with one of her upper hands to hide her impolite smile."

xz "Forgive me, I know you didn’t intend it as such, but that was a funny joke."
xz "Perhaps you’re looking at it from the wrong perspective. {i}None{/i} of us are ultimately true submissives."
xz "-It’s just that some of us are willing to subjugate ourselves for the sake of expediency."
xz "I know that she and Ishta had grown close the last few weeks… but such power plays are to be expected."

ro "Do you think she could have done it?"

xz "{i}Anyone{/i} in the Sanctum could have done it. But Nisei was more personally involved with Ishta than most."
xz "Don’t be afraid to call her out on her falsity. For all her emotional tendencies, Nisei is a calculating creature."

"X'zaratl pulled aside the silken curtains, their enfolding curves bending aside to reveal the sumptuous bedroom of a Succubus."

hide xzaratl with dissolve
show succubus 3 neutral at midright with dissolve

"Nisei didn’t wait for the curtains to close behind Rowan before she rushed forward, tears in her eyes as she fell at his feet."

nisei "Do you know what’s happened? Who was it? Please, {i}you{/i} have to tell me!"

show rowan necklace concerned at midleft with dissolve

ro "Uh…"

nisei "X'zaratl sent you, didn’t she? Does she know who's to blame? What of my sweet Simon?"

"Her eyes were wide, her expression pleading. But behind the tears and worried tone, Rowan saw a hunger in the creature’s eyes. Nisei was restless, and for more reasons than just the murder."
"Nisei prostrated herself before him, pleading to his beneficence like a sinner to a judging god. Her long tail curled behind her in frenetic outbursts."

nisei "I beg you mortal: give me news of what has happened!"

show rowan necklace neutral at midleft with dissolve

ro "Ishta was found dead in bed with a slave. Both of them murdered. I’m here to figure out what happened."

"At this statement, Nisei’s expression collapsed. She fell to the floor, only just catching herself with her hands as she began to sob."

nisei "Oh, my poor, sweet Simon!"

show rowan necklace shock at midleft with dissolve

"Her ragged wailing shocked Rowan. He had never seen a demon express such grief before. Most of it was for show, almost certainly, but lurking behind the facade was a pale shadow of regret."

show rowan necklace neutral at midleft with dissolve

"At last, after a minute or two of mewling melancholy, the demon seemed to come to her wits. She sat up, wiping at her eyes as she ignored the very un-sexy way she looked in that moment."

nisei "...Simon was my favorite, you know? A real ‘go-getter.’ Never had to be told what to do in the bedroom, always knew how to please."

ro "Simon was the slave who was found alongside Ishta?"

nisei "Nisei nodded, tears flooding into her eyes once more. She let out a low, feminine whine, hanging her head in her hands. She was a wet mess on the floor."

show rowan necklace concerned at midleft with dissolve

ro "I need to ask you some questions Nisei."

"Nisei, without looking up, nodded in assent."

$ nisei1aSeen = False
$ nisei2aSeen = False
$ nisei3aSeen = False

$ simonOddVictim = False
$ ryleaDeandraAffairClue = False
$ ryleaIsthasFavouriteClue = False

label niseiQuestions:

show rowan necklace neutral at midleft with dissolve

menu:
    "Do you have any idea who could have done this?" if nisei1aSeen == False:
        $ released_fix_rollback()
        nisei "No… everyone {i}loved{/i} Simon! He was such a wonderful slave."
        nisei "I practically had to seal him away in his quarters every night. Someone in the brood might’ve snatched him away when I wasn’t looking!"
        nisei "Murdering Ishta is one thing. But… killing a slave? A handsome, virile, {i}beautiful{/i} slave?"
        nisei "Is nothing sacred, anymore?"
        ro "Why would you think that he was the target, and not Ishta? Simon may have simply been in the wrong place at the wrong time."
        "Nisei’s eyes took a hard look. Her brow twisted downward in black hatred."
        nisei "Because those two-faced whores {i}knew{/i} who he was, and who he belonged to. It’s no accident he’s dead too. "
        nisei "They wouldn’t harm Simon just to get to Ishta. Not unless {i}I{/i} was the ultimate target."
        nisei "I mean, sure she had her enemies. But who doesn’t?"
        nisei "Oh my poor, sweet Simon. He must have been so scared!"
        show rowan necklace angry at midleft with dissolve
        ro "What enemies?"
        nisei "I mean… everyone knows how bad she’s been mistreating Ahrima recently. The two nearly came to blows at least three times in the last month."
        ro "Who else?"
        "Nisei’s lips pinched in worry. She gave Rowan a doleful look, her eyes wide and - ostensibly - innocent."
        nisei "I… I don’t want to say. We’re not supposed to talk to outsiders about brood business."
        ro "I’m here to solve your ‘brood business.’"
        "Nisei chewed on her lower lip but said nothing. Rowan let out a tired sigh."
        $ simonOddVictim = True
        $ nisei1aSeen = True
        jump niseiQuestions
        
    "Where were you when the murder occurred?" if nisei2aSeen == False:
        $ released_fix_rollback()
        nisei "Well, the first part of the day I was helping X'zaratl with some…"
        nisei "Personal business."
        "Her horny smile said everything that needed to be said on the matter."
        nisei "After that, I was given some light relief duty with a few of the mercenaries."
        nisei "Nothing special: a half dozen blowjobs, an anal quickie or two. Normal stuff, to keep the officers happy."
        nisei "And after {i}that{/i}, well…"
        nisei "A girl has to keep {i}some{/i} secrets, doesn’t she?"
        "Rowan did not like the menacing glint of her smile."
        show rowan necklace angry at midleft with dissolve
        ro "No, we really don’t. I don’t have time to waste on word games, where were you?"
        nisei "Nothing much. I got into a little scrap I got into with one of my sisters, Deandra."
        nisei "She and I were old allies once, when we were once newcomers to the brood. The older members wanted nothing to do with us."
        nisei "After the last shakeup, when Ishta took power, Deandra suddenly decided I wasn’t good enough. "
        nisei "The slut started sleeping with that winging little pissant Rylea behind Ishta’s back, and left me to fend for myself."
        nisei "She’s been a thorn in my side ever since."
        ro "What was this ‘little scrap’ between you two about?"
        "Nisei’s eyes narrowed. Her tail twisted and contorted behind her like a whip."
        nisei "Ask {i}Rylea{/i} If you’re so eager to learn. I’m sure he’ll tell you."
        $ ryleaDeandraAffairClue = True
        $ nisei2aSeen = True
        jump niseiQuestions
       
    "So you admit that the dead slave belonged to you?" if nisei3aSeen == False:
        $ released_fix_rollback()
        nisei "Of {i}course{/i} I do! Who wouldn’t want to brag about possessing the finest breeder in the whole brood?"
        nisei "Simon was an absolute stud! A {i}beast{/i} in the sheets, but as tame as a lamb."
        nisei "He was a real sweetheart, too: I barely even had to train him after I claimed him."
        nisei "Most former soldiers try to fight it, not wanting to accept their new role. We usually have to put them in their place. But {i}Simon{/i}…"
        "Nisei’s smile became dreamy, as if she were reminiscing on some distant, romantic evening the two had shared, long ago."
        nisei "Kharos claim him, he was like a whiff of manly sweat after a daylong abstinence binge."
        nisei "He cheered me up if I was ever feeling down. I could always count on him to curl my toes."
        nisei "I just can’t believe he’s gone."
        $ nisei3aSeen = True
        jump niseiQuestions
        
    "What are your thoughts on the other Succubi?" if nisei1aSeen == True:
        $ released_fix_rollback()
        nisei "They’re fucking {i}dead{/i} is what they are!"
        "The sudden hatred that rose in her eyes bespoke Nisei’s apocalyptic sincerity. Her fists clenched as she bared her long fangs."
        nisei "One of those walking corpses killed my poor Simon. That insult won’t go unpunished."
        nisei "I swear, when I figure out whoever’s responsible for this, I’ll rip their guts out and burn their intestines on a-"
        show rowan necklace angry at midleft with dissolve
        "Rowan let out a frustrated sigh. It was like he was talking to a delusional, horny wall."
        ro "All right, all right, I get it. Answer the question."
        nisei "Well… Ahrima is the first one that comes to mind. Her and Ishta got along about as well as an amputee at a foot fetish orgy."
        nisei "Then there’s Rylea, catty little moocher that he is. I wouldn’t be surprised if he was responsible for all this."
        ro "Why?"
        nisei "Jealousy. He knew I was moving in on his turf as Ishta’s new number two. He’s been her favorite bottom bitch ever since she took the crown."
        nisei "Then again… he {i}did{/i} love Simon to pieces."
        nisei "I often had to get violent to separate the two, back when we were working together."
        nisei "Hehe… {i}especially{/i} when I told him to shove Simon’s head into the pillow and piledrive is ass deep into the-"
        show rowan necklace concerned at midleft with dissolve
        ro "Kharos take me, {i}I get it{/i}."
        "Nisei giggled at Rowan’s squeamishness."
        show rowan necklace neutral at midleft with dissolve
        ro "What about the last one?"
        "She paused in her revelry, her head tilting as a strange look came to her features. Nisei’s teasing smile faded, her expression blackening with hatred. She let out a low snarl."
        nisei "...You mean Deandra."
        nisei "That fat-winged, tiny assed, gag-reflex inducing, {i}pathetic{/i} excuse for a strumpet!"
        nisei "She could have done it with a smile on her face, oh yes. She’s a lying, thieving, {i}bitch{/i}."
        ro "So you think Deandra’s responsible."
        nisei "She’d definitely do it if she thought she could get away with it."
        nisei "But... she wouldn’t have dared to move against me, not with how isolated she’s been the last few weeks."
        nisei "The weak little tart wouldn’t have been stupid enough to try. She’d know I’d find out."
        "{i}Or so you think{/i}. Was the thought that rolled through Rowan’s mind."
        $ ryleaIsthasFavouriteClue = True
        jump niseiQuestions
        
    "What can you tell me about Ishta?" if nisei2aSeen == True:
        $ released_fix_rollback()
        nisei "She was a dear friend, and a powerful demon."
        ro "I never took Succubi to be particularly interested in ‘friendship.’"
        nisei "Is it {i}really{/i} so hard to believe that we actually liked one another?"
        show rowan necklace angry at midleft with dissolve
        ro "Yes. Impossible, in fact."
        "Nisei tried to let out a huff of indignance, but it was at best a half-hearted attempt. She took one look at Rowan’s empty look and frowned. After a moment’s charade, she dropped the whole act."
        nisei "Everyone’s a means to something, mortal."
        nisei "So what if I’m not in pieces over her {i}oh{/i} so tragic death? Are my own abject circumstances alone not enough to prove my innocence to you?"
        nisei "The worst has already happened: I’ve lost my leverage, {i}and{/i} my favorite pet is dead!"
        ro "What will you do now that she is dead?"
        nisei "Oh, I’m sure I’ll find some way to carry on."
        nisei "I’m used to shake ups like this; all the old rules are out the door at this point, anyway."
        ro "Old rules?"
        nisei "Back in Karnas’ time, a little killing like this wouldn’t even be noticed by a broodmother like X'zaratl."
        nisei "It was just another power play. Any leader worth her harem was ready to kill to keep her spot at any time."
        nisei "Now, with the Twins calling the shots, things are a lot more boring and predictable. A lot of the older Sanctum members chafe under the new rules."
        jump niseiQuestions
        
    "What was your ‘sweet Simon’ doing in Ishta’s room?" if nisei3aSeen == True:
        $ released_fix_rollback()
        "Nisei’s shoulders sagged."
        nisei "I…"
        nisei "I loaned him to her."
        ro "Why?"
        "Nisei made a great show of throwing herself at Rowan's feet."
        nisei "Oh {i}mortal{/i}, must you make me name my shame?"
        show rowan necklace angry at midleft with dissolve
        "Rowan flattened his lips and nodded. Nisei let out an annoyed exhale and picked herself up off the ground."
        nisei "Oh fine, have it your way!"
        nisei "It was a deal, all right? Ishta and I had gotten pretty close recently, and it was starting to look like she wanted to join forces."
        show rowan necklace neutral at midleft with dissolve
        ro "Against your fellow brood?"
        "Nisei’s fragile smile was that of a guilty child who had just learned where the sweets were hidden."
        nisei "Some of them. If it came to that."
        show rowan necklace angry at midleft with dissolve
        ro "This still doesn’t explain Simon’s presence in her room."
        nisei "He was a gift. A loan. A sign of trust, if you will."
        nisei "The Sanctum is a dangerous place. One must make sacrifices to find a proper niche to cling to. My poor Simon was that sacrifice."
        nisei "...M-more than I ever expected him to be!"
        "Nisei covered her face with her hand and intonated a sob. Rowan let out a sigh. His toe tapped impatiently against the ground."
        jump niseiQuestions
        
    "End interrogation." if ryleaDeandraAffairClue == True and ryleaIsthasFavouriteClue == True:
        $ released_fix_rollback()
        jump niseiInvestigationEnd

label niseiInvestigationEnd:

ro "Well Nisei, your testimony was certainly…"
ro "Compelling."
ro "But I think I’ve heard enough."

"As if by magic Nisei’s tears returned as Rowan turned away. Her voice took on the righteous anger of a grieving widower."

nisei "Wait! Mortal, you {i}must{/i} tell me who is to blame once you find the culprit, you simply {i}mus{/i}-"

hide succubus 3 with dissolve
show xzaratl neutral at cliohnaright with dissolve

"The curtains mercifully closed behind the begging Succubus before she could finish her entreaty."

xz "What news?"

ro "The dead slave did indeed belong to Nisei, though she admitted to it outright."
ro "She said a number of other interesting things as well."

if simonOddVictim == True:
    ro "For one thing, she seems baffled as to why the killer would have harmed her slave in the first place."
    xz "It is… rare for a Demon to involve others’ slaves in our internal conflicts. It’s considered a grave insult, a profound disrespect of another’s property."

ro "It would seem Ishta had a number of entanglements in the brood. It seems like no one really liked her, given that even her supposed ‘ally’ seemed unmoved by her death."
ro "Nisei also said that an Incubus called “Rylea” was Ishta’s secret concubine. She claimed she’d brought Simon in to try to woo Ishta away from him."

xz "Then we have our next suspect."

label xzaratlInterrogation3:

scene bg23 with fade
show rowan necklace neutral at midleft with dissolve
show xzaratl neutral at cliohnaright with dissolve

ro "...So who is Rylea?"

xz "Rylea is the coven’s only Incubus. He was one of Bloodmeen’s first recruits, one of the older demons of the brood, from Karnas’ time."

#xzaratl concerned

xz "He is a capricious creature, quick to anger and often petulant. His fellow demons don’t respect him, but he is a survivor through and through."
xz "You must be wary of flattery. Rylea is more than happy to debase himself to those more powerful than him."
xz "If he was indeed Ishta’s pet, then he had a vested interest in remaining in her good graces… but such alliances amongst our kind are always built upon rotten logs."
xz "A stray word, a callous insult… over the centuries, many a great alliance of broods have broken down over the petty politics of pillow talk."

ro "Do you think he is a credible suspect?"

xz "Why wouldn’t he be?"

ro "Innocence? Proof he didn’t do it?"

"X'zaratl returned a blank stare, as if befuddled by the question. She gave him a kindly, If somewhat patronizing smile."

xz "This is the Dark Sanctum, Rowan. ‘Innocence’ has no meaning here."
xz "You must understand this when it comes to my kind: there is no such thing as a neutral party."
xz "{i}All{/i} of us bear some form of guilt in this murder. The crux is finding out who bears the most."

"With that concerning implication left ringing in his ears, X'zaratl pulled aside the silken curtains. Rowan stepped inside, glancing over his shoulder for one last look at her smiling face."

hide xzaratl with dissolve

"He turned his gaze back towards the room just in time to see an Incubus stroking himself furiously on the bed, letting out a horny moan as he did so."

show incubus 1 neutral at midright with dissolve
show rowan necklace shock at midleft with dissolve

rylea "{i}Gh!{/i}"

show rowan necklace angry at midleft with dissolve

ro "Damn it!"

"He had not been expecting to suddenly face such a lurid sight. The Incubus rose to his feet with an apologetic smile. Noticeably, he did not put his erect penis away. It pointed back at Rowan as if in dread accusation."

rylea "Sorry about that. Been stuck in here a while."
rylea "Who are {i}you{/i}, cutie? I wasn’t expecting anyone else other than X’Zaratl to show up."
rylea "Is it too much to hope that you’re here to entertain me?"

ro "I am Rowan Blackwell. I’ve been sent here to investigate the murder of X'zaratl’s second."

"Rylea’s eyes went wide."

rylea "...Wait, what?"
rylea "Ishta’s dead?"
rylea "No… oh by Kharos, {i}no{/i}!"

show rowan necklace shock at midleft with dissolve

"Rylea rushed forward and grabbed Rowan by the shoulders. It happened so quickly that Rowan didn’t even have time to go for his sword."

rylea "What happened? Who did this? Mortal, you must tell me immediately!"

"Rage and fear warred across the Incubus’ features as he shook Rowan back and forth."

rylea "{i}I{/i} was Ishta’s favorite! Do you {i}know{/i} what this means for me?"
rylea "Those fucking whores there will tear me limb from limb!"

show rowan necklace angry at midleft with dissolve

"Rowan took in a deep breath, struggling to contain the rage that rose in his chest."

ro "Let. Go. Of me."
ro "{i}Now.{/i}"

"Rylea paused, his anger subsiding as he saw the danger lurking in Rowan’s eyes. He let out a deep sigh, then stepped back. He had gone flaccid in the interim."

rylea "{i}Damn{/i} it. How did she die?"

ro "Shut up. I’m asking the questions. Touch me like that again, and you’ll lose your head. Both of them."

"At this Rylea’s brow quirked. He let out an effeminate giggle, swaying his narrow hips from side to side."

rylea "Talk dirty to me like that again, mortal, and maybe I’ll suck a different head, instead."

$ deandraPrankClue = False
$ ryleaDeandraAffair2Clue = False

label ryleaQuestions:

menu:
    "What can you tell me about Ishta?":
        $ released_fix_rollback()
        rylea "What is there to say? She was my lover for the last few months, and a damn good one at that."
        rylea "Far more importantly: she was my protection against the rest of the brood."
        rylea "Things have gotten a little tense around here lately, if you haven’t noticed. But I never would have thought someone would snap and go crazy like {i}this{/i}."
        ro "What makes you think someone ‘snapped?’"
        "Rylea‘s brow furrowed. His hands clenched as he seemed to struggle with the new reality he’d found himself in."
        rylea "No one with an ounce of sense or ambition would have gone through with killing Ishta. Not now."
        rylea "X'zaratl likes to keep a quiet brood. She’s trying to impress our new masters. And a killing like this, where there’s seemingly no purpose… well, it makes her look weak."
        rylea "This also puts me in a most depressing predicament. As I’ve just run out of allies."
        ro "Then tell me who did it, and you can be short one rival."
        "Rylea’s predatory pupils widened. A malicious smile came to his face as he contemplated Rowan’s words."
        rylea "My, but aren’t {i}you{/i} a succulent little soldier?"
        rylea "It’s an amusing - and {i}tempting{/i} - offer, but I’m going to have to decline."
        rylea "I don’t know who did it. But even if I did, the blowback isn't worth it. I need to find new allies, not alienate whoever’s left."
        jump ryleaQuestions
        
    "Do you know about a slave of Nisei’s called Simon?":
        $ released_fix_rollback()
        rylea "No. I rarely trifle in the brood’s pet-swapping antics. I find it nauseating."
        show rowan necklace angry at midleft with dissolve
        ro "You’re lying."
        ro "Nisei told me you knew him personally. She said you liked him so much she often had to separate the two of you."
        "Rylea laughed in a high, lilting tone. He lifted his hand to cover his smile."
        rylea " Is {i}that{/i} what she told you? "
        rylea "Let me be frank, mortal: Nisei is a lying narcissist with a desperate need to feel {i}important{/i}."
        rylea "I wouldn’t know who her favorite harem slave was if he flew in here riding a fire-breathing dragon sporting a ten-foot penis. A warm hole is a warm hole."
        ro "Then you’ll be surprised to learn that Simon is dead. He was found in the arms of Ishta."
        rylea "...The killer murdered a slave too?"
        "Rowan had expected some kind of emotional response, but Rylea seemed merely curious. He shrugged."
        rylea "I’ll admit, that’s quite strange. No one kills a slave, not unless they’ve grown too unruly. And even then, only if its their own. Slaves are supposed to be off limits."
        rylea "But this only proves my point: what possible reason would I have to slaughter both my meal-ticket, and my ‘favorite’ slave at once?"
        show rowan necklace neutral at midleft with dissolve
        jump ryleaQuestions
        
    "Where were you when the murder occurred?":
        $ released_fix_rollback()
        rylea "Enduring yet another one of Deandra’s childish pranks."
        rylea "Admittedly, it was a good one. But it was hardly worth my time."
        ro "What prank? Where was this?"
        rylea "It was in Nisei’s room. Deandra and I snuck in this morning during one of Nisei’s cooldown sessions."
        rylea "She has a predictable routine where she calls in a random slave and rides them till they pass out. But this time, Deandra posed as the slave."
        rylea "They got halfway through the fuck-session before Nisei realized that the person railing her ass was Deandra, not her chosen stud."
        rylea "Then Deandra played a charming little game of ‘hold on for dear life,’ using Nisei’s hair as a rope, while Nisei tried to buck her off like a bronco."
        ro "What were you doing there?"
        rylea "Watching, of course! Deandra usually likes to have an audience when she pulls these kinds of things."
        rylea "X'zaratl came barging in not long after, maybe ten minutes or so after that. I scuttled back to my chambers, with no one the wiser to my whereabouts."
        ro "Can anyone corroborate your story?"
        "Rylea shook his head, his tail twisting behind him as he fantasized about the moment."
        rylea "Maybe Deandra, if she’s inclined to tell the truth today. Nisei had no idea I was there, and would never admit it if she did."
        $ deandraPrankClue = True
        jump ryleaQuestions
        
    "Do you have any idea who could have done this?":
        $ released_fix_rollback()
        rylea "Ahrima. No question about it."
        ro "Really? You’re that certain? Everyone else has been a lot more…"
        rylea "Speculative?"
        rylea "That doesn’t surprise me. The others are exploiting the change, jostling for the top spot. They have a reason to accuse anyone and everyone else, hoping to eliminate a future rival."
        rylea "I, on the other hand, harbor no such delusions. {i}Whoever{/i} wins, I will have to either impress them, or submit to them."
        rylea "Nisei - the scheming slut - was trying to snatch my place as Ishta’s bottom out from under me. The last thing she’d want to do is purposefully undercut herself in that endeavor."
        rylea "Deandra is a cute prankster, but {i}hardly{/i} a master of intrigue. To pull off a killing like this, she’d have to be very confident that she wouldn’t get caught. And she has no real reason to try."
        rylea "{i}Ahrima{/i} on the other hand, had both motive and means. Her room’s right next to Ishta’s. At the very least, she’d have heard everything."
        rylea "She hated Ishta more than anyone else. Our options for allies in the brood often boiled down to either one or the other."
        rylea "Now that her rival’s out of the picture, Ahrima has the most to gain."
        ro "I noticed you left {i}yourself{/i} out of your calculations."
        "Rylea smiled with a mouth full of fangs."
        rylea "Yes. And why wouldn’t I? Am I supposed to {i}suggest{/i} to you that I’m guilty?"
        jump ryleaQuestions
        
    "What’s going on between you and Deandra?":
        $ released_fix_rollback()
        rylea "What do you mean?"
        ro "You say that you’re Ishta’s favorite, yet {i}Nisei{/i} says you were carrying on a secret affair with Deandra at the same time behind her back, as well."
        "Rylea let out a soft sigh. He pinched the bridge of his nose, as if annoyed by the inquiry."
        rylea "Have you ever heard of the term “business before pleasure,” Rowan?"
        rylea "Ishta was a relationship of convenience. She knew it, and I knew it."
        rylea "The second someone else caught her eye - someone like {i}Nisei{/i} - my days as her bottom were numbered. It’s a miracle it lasted as long as it did."
        rylea "I’ve tried hopping onto Ahrima’s bandwagon in the past. Let me tell you: it's a quick path to a sore ass and an empty harem."
        rylea "But if Ishta ever got bored of me, I needed insurance."
        ro "And Deandra is that ‘insurance.’"
        "Rylea shrugged, running his hands up and down across his skin as if he were possessed of excessive sensitivity."
        rylea "Better to have a clever underdog as backup than nothing at all. Nisei’s current situation in the brood is living proof of that fact."
        ro "So you admit that she was your secret lover?"
        rylea "Sure. Just ask Deandra, she’ll tell you the tru-"
        "Rylea started to laugh, covering his mouth with his hand as he did so."
        rylea "Dear me, I very nearly finished the sentence without smiling!"
        $ ryleaDeandraAffair2Clue = True
        jump ryleaQuestions
        
    "End interrogation." if ryleaDeandraAffair2Clue == True and deandraPrankClue == True:
        $ released_fix_rollback()
        jump ryleaInvestigationEnd

label ryleaInvestigationEnd:

ro "...Fine. That’s all the questions I’ve got for now."

rylea "You realize X’Zaratl’s using you, yes?"
rylea "You think she couldn’t solve this herself? I’d bet half my harem that she already knows who the culprit is."

"Rowan set his jaw, saying nothing as he stalked out of the demon’s room and threw aside the curtains."

hide incubus 1 with dissolve
#xzaratl happy
show xzaratl neutral at cliohnaright with dissolve

xz "How did it go, Rowan?"

show rowan necklace angry at midleft with dissolve

ro "The same as the others. Nothing but lies, insinuations, and hearsay."

"Rowan let out a sigh and collected himself. Today had been an especially trying day."

show rowan necklace neutral at midleft with dissolve

ro "...It seems Rylea was playing Ishta and Deandra against each other. He was secretly seeing Deandra while acting as Ishta’s ally."

xz "-And all the while, Nisei was doing her best to pull Istha out of his orbit."

ro "Yet no one at all seems interested in allying with Ahrima. Meaning everyone we’ve spoken to so far has at least some reason to want to implicate the others."

xz "There’s only one brood member left, Rowan."

"Rowan gave a grim nod."

ro "Lead the way. Let us be done with this."

label xzaratlInterrogation4:

scene bg23 with fade
show rowan necklace neutral at midleft with dissolve
show xzaratl neutral at cliohnaright with dissolve

ro "Who is this last demon?"

xz "Deandra is the youngest member of the brood. She is new, but has integrated herself quite well into the schemes of the others."
xz "She is a social climber, and will do anything to get to the top. But her relative weakness makes her an unappealing ally for most of her kin."
xz "With time, she could grow into a shrewd and calculating Succubi. But so far, she has remained ambitious, but isolated."

ro "Ambitious and isolated enough to murder your second?"

xz "Hmm… possibly. If there was something to gain from it."
xz "I cannot fathom what that could be, though. She is nowhere near ready to take Ishta’s place in the pecking order."

ro "Maybe she’s just crossing one more name off the list."

"X'zaratl smiled, putting a thoughtful hand to her chin."

xz "I like the way you think, Rowan. And in a way, I hope that it is so. It would mean that Deandra had shown remarkable initiative to defeat a more powerful rival."

#xzaratl angry

xz "But she had best hope that you’re wrong."
xz "Brood politics is one thing. Callous murder for nobody’s benefit is another matter entirely."

#xzaratl neutral

xz "Careful with your words when you’re around her, she likes to play mind games."

show rowan necklace concerned at midleft with dissolve

ro "-As opposed to the rest of them."

hide xzaratl with dissolve

"No sooner had the curtains parted than Rowan was face to face with Deandra’s smiling face."

show rowan necklace shock at midleft with dissolve

ro "Gah!"

show succubus neutral at midright with dissolve

deandra "Greetings, Rowan."
deandra "I was wondering when you’d get here."

"Her smile was welcoming, her body language placid and sedated. Deandra had her arms folded behind her, offering no resistance to him whatsoever."

show rowan necklace angry at midleft with dissolve

ro "How do you know my name?"

deandra "Unlike my brothers and sisters, I make a point of learning the who’s and what’s of Bloodmeen."

if society_type == "feudalism":
    deandra "Sir Rowan Blackwell. Hero of Karst, Steward of the Twins."
    
else:
    deandra "Rowan Blackwell. Hero of Karst, Steward of the Twins."

deandra "So X'zaratl’s pulled you into our little web of intrigue, hm?"
deandra "I suppose it’s to be expected. You have become her favorite little project."

"Deandra smiled, stepping aside and gesturing for him to enter."

deandra "Please, come in. I’m sure you have questions about Ishta’s murder."

show rowan necklace neutral at midleft with dissolve

ro "How do you know about the murder?"

deandra "Come now, Rowan. You think my brothers and sisters weren’t aware of what had happened, before you ever even talked to them?"
deandra "They all may be practiced liars, but none of them would be stupid enough to be caught in the lurch when X'zaratl locks us down like this."

"Rowan gave the smiling demon a careful once over. She was friendly, open, downright {i}happy{/i} to engage with him. That fact alone made the hair on the back of his neck stand on end."
"He fingered the pommel of his blade and stepped inside. Deandra walked over to the bed and sat down. She patted a spot right next to her."

deandra "Come, sit! I don’t bite… unless you want me to."

"Her teasing smirk made Rowan’s jaw clench. He remained standing where he was. Deandra did not seem at all put off at the rejection."

deandra "So, what did you wish to know?"

$ deandra1aSeen = False
$ deandra2aSeen = False
$ deandra3aSeen = False

$ deandraSawSimonClue = False
$ secretTunnelsClue = False

label deandraQuestions:

show rowan necklace neutral at midleft with dissolve

menu:
    "Do you have any idea who could have done this?" if deandra1aSeen == False:
        $ released_fix_rollback()
        deandra "Everyone has their reasons. Some more justified than others."
        "Her smile might have seemed innocent, were her eyes not so obstinately insolent."
        deandra "Well there’s Ahrima, of course. The two got along so poorly, I’m shocked it hadn’t already ended in a blood-duel ages ago."
        deandra "Nisei might have done it. She and Istha have past grievances, due to Ishta kicking her lover out of the brood."
        deandra "Although, if she did do it, she would have struggled to overcome her own, glaring flaws to do so."
        ro "Such as?"
        deandra "Cowardice, for one. No self-respecting demon {i}willingly{/i} subjugates themselves for the sake of a ‘cosy’ position as someone else’s bottom bitch."
        deandra "Hmm… Rylea’s probably innocent. As petty as he can be, he’d have {i}had{/i} to know the consequences of offing his own meal-ticket."
        ro "What about you? What reason would you have to kill Ishta?"
        "Deandra let out a sultry coo. She stretched, making sure Rowan got a good look at her slender curves as she did so."
        deandra "Oh, that’s easy. She is X'zaratl’s second. She’s holding my rightful spot."
        ro "So you admit that you had a motive."
        "Deandra giggled."
        deandra "Yes. But I promise you: I’d have done it a lot {i}better{/i}."
        $ deandra1aSeen = True
        jump deandraQuestions
        
    "What do you actually know about the killing?" if deandra2aSeen == False:
        $ released_fix_rollback()
        "Deandra let out a sumptuous giggle, hiding her mouth with her hand. Her eyelashes fluttered in seductive offering."
        deandra "I know that Ishta is dead, torn apart at the hands of a demon’s claws."
        deandra "I also know that she wasn’t the only victim. She was caught with the body of a dead slave in her arms. Nisei’s little pet, If the rumors are true."
        deandra "Simon? Simeon? His name escapes me."
        show rowan necklace angry at midleft with dissolve
        ro "The other demons all claimed some form of ignorance about the crime."
        deandra "I am not ‘other demons.’ I have no reason to lie to you."
        ro "Other than to prove your innocence."
        "Her curling smile did nothing to reassure Rowan."
        $ deandra2aSeen = True
        jump deandraQuestions
        
    "Where were you when the murder occurred?" if deandra3aSeen == False:
        $ released_fix_rollback()
        deandra "I was busy making a fool of Nisei in her quarters."
        "There was a pitiless humor in the sharp curve of Deandra’s lips, like a lioness greedily licking her chops after a meal."
        deandra "The absent-minded slut forgot to check and see if her slave was actually her slave, and not just a transformed copy."
        deandra "When she failed to figure it out, I strutted in and stuck my dick up her ass."
        "Deandra giggled at the memory, her hands drifting lower on her body at the reminiscence."
        deandra "She didn’t squirm strongly enough to throw me off in time. So now there’s a thick load of my cum sloshing about in her guts."
        ro "Was this done in revenge for something?"
        "Deandra’s eyebrow quirked. She seemed amused by the question."
        deandra "Now, now, Rowan. Must {i}everything{/i} be about petty revenge? I saw an opportunity to humiliate a potential rival, and I took it."
        $ deandra3aSeen = True
        jump deandraQuestions

    "Rylea says that you have been carrying on an affair behind Ishta’s back.":
        $ released_fix_rollback()
        deandra "It’s a bit rich to say ‘behind her back’ when Ishta knew damn well we were fucking."
        ro "So you deny being his secret lover?"
        deandra "Insomuch as I am no one’s ‘lover’ besides my own."
        deandra "Rylea and I have collaborated a lot recently. But I have {i}never{/i} been foolish enough to make a true alliance with him. Or anyone else, for that matter."
        ro "Why?"
        deandra "Because I don’t work well with other demons. The brood’s a bloody business, and when you play this deadly game with partners, you often end up like Istha."
        ro "So you dislike killing?"
        "Deandra covered her lips with her hand to hide her smile."
        deandra "I dislike politics of all kinds. A smart Succubus knows her only real friend is herself. Everyone else is just… "
        deandra "An accessory."
        jump deandraQuestions
        
    "What can you tell me about Ishta?" if deandra1aSeen == True:
        $ released_fix_rollback()  
        deandra "She was a shallow pretender, and a weak second. X'zaratl could have done better with {i}literally{/i} anyone in the brood, even that seething bag of spite Ahrima."
        deandra "She was a pretentious, inattentive tyrant. The worst kind. It’s a mystery of Kharos’ imagination how she lasted as long as she did."
        deandra "Honestly, her murder sounds a lot more like something she would have pulled off, if she were gunning for the top spot."
        ro "What do you mean?"
        deandra "Senseless, messy slaughter. No grace, no subtlety. Just brute force driven by raw emotion."
        deandra "A part of me almost wonders if she’s still, in fact alive. And that this is all just some odd ruse to suss out possible traitors."
        ro "Do you have any proof to back up this claim?"
        "Deandra laughed, covering her mouth to hide the smile."
        deandra "No. But then again: neither do you."
        deandra "If you really wish to find out, poke her corpse and see if she protests."
        jump deandraQuestions
      
    "How do you know about Simon being in the room with Ishta?" if deandra2aSeen == True:
        $ released_fix_rollback()  
        deandra " It wasn’t exactly a secret of Solansia that Nisei was on the hunt for a new ally."
        deandra "She just recently got out of a bad alliance with Ahrima, and needed someone with substance to protect her from people like… well, {i}me{/i}."
        "Deandra flashed Rowan her fangs as her tail curled excitedly in circles behind her."
        deandra "Nisei knew I was courting Rylea, so to avoid becoming isolated she went for the only remaining option."
        deandra "Simon’s a bit of a debutante in the brood. Nisei likes to parade him about sometimes. She talks to him like he’s some beloved child."
        deandra "Loaning off her favorite pet was a good way of showing trust and fidelity to Ishta’s rule."
        deandra "It’s all rather revolting, if you ask me. Food is food."
        show rowan necklace angry at midleft with dissolve
        ro "I didn’t ask ‘why did she do it?'"
        ro "I asked: {i}how do you know{/i}?"
        "Deandra - to her credit - did not bother to look chastened by his words. She merely smiled at him."
        deandra "Because I saw him enter the room with her. Nisei dropped him off before going to her own room. I was disguised as one of her other slaves. I saw it all."
        $ deandraSawSimonClue = True
        jump deandraQuestions

    "Were you alone with Nisei?" if deandra3aSeen == True:
        $ released_fix_rollback()  
        deandra "No. Rylea was there too, lurking about in the tunnels so she wouldn’t know he was there."
        deandra "He likes to jerk off to other people’s power plays sometimes. Bit of a voyeur fetish."
        ro "Tunnels? What tunnels?"
        "Deandra’s eyes glowed with dark amusement."
        deandra "Goodness. No one told you, did they?"
        deandra "The Sanctum is {i}riddled{/i} with hidden passages and secret backways. It’s how we get around without drawing each other’s notice."
        deandra "Aside from a few dead ends leading to X'zaratl’s room, you can get practically anywhere if you know where you’re going."
        "Deandra stood up off the bed and gestured towards the curtains at the back wall. Rowan followed her warily as the demon pulled aside the curtains to reveal a small, cramped corridor to step into."
        show rowan necklace angry at midleft with dissolve
        ro "Why has no one mentioned this before?"
        "Deandra giggled."
        deandra "You never asked! And we demons don’t like to share."
        $ secretTunnelsClue = True
        jump deandraQuestions
        
    "End interrogation." if deandraSawSimonClue == True and secretTunnelsClue == True:
        $ released_fix_rollback()
        jump deandraInvestigationEnd    

label deandraInvestigationEnd:

show rowan necklace neutral at midleft with dissolve

ro "...I think I’m done asking questions."

deandra "Oh, I think you’ve got one more in you."

show rowan necklace angry at midleft with dissolve

ro "Unless you’re volunteering guilt, we have nothing more to say to each other, demon."

"Rowan pivoted on his heel and made for the door. He paused at the curtains at the sultry sound of Deandra chuckling."

deandra "Such an odd thing, Simon’s death. Don’t you think?"

show rowan necklace neutral at midleft with dissolve

ro "What?"

deandra " What a strange aberration he is in all this. A perfectly good cockslave, with all the hallmarks of a beloved stud. Tame as a lamb, and so easy to manipulate."

"Rowan turned in a slow circle to face her."

deandra "Why would anyone kill him? What do they have to gain by killing a slave who bore no loyalty to Ishta?"

ro "...To denigrate Ishta’s memory? To ruin her reputation?"

"Deandra let out a snort, waving the thought away as if it were nothing."

deandra "Ishta’s dead. Her reputation is irrelevant. While it may elicit an extra chuckle or two, it serves no real purpose."
deandra "You must know Rowan: there is nothing that we demons do that isn’t in our best interests."
deandra "So ask yourself: why would someone kill a slave?"

show rowan necklace concerned at midleft with dissolve

"A long silence followed, as the oddly contagious thought rolled through Rowan’s head. The bottom went out of his stomach as his eyes flicked over to the curtains leading to the tunnels. Deandra continued on as if he’d heard nothing."

deandra "You know it’s funny, this reminds me of what Nisei said while I was railing her ass today. She-"

show rowan necklace shock at midleft with dissolve

ro "No… "

"Deandra tilted her head in a mock-quizzical fashion."

deandra "Hm? Did you say something Rowan?"

show rowan necklace angry at midleft with dissolve

ro "Open the way to the tunnels. {i}Now{/i}."

"Deandra practically skipped to the curtains, turning them aside as Rowan stepped through. He hustled down the dank corridor, following his hunch into the dark depths."

#catacombs BG
scene black with fade

"Deandra’s room soon disappeared from view. Rowan soon came to a switchback that led to a long corridor that ran parallel to the Dark Sanctum’s main chambers."
"Acting on his suspicions, he used his natural tracking senses to trace the rough distance of Ishta’s room in his head, then made in that direction."
"Moving through the tunnels, he began to hear a strange sound emanating from the depths. It was almost like… whimpering."
"At last Rowan came to the place he figured to be Ishta’s room. The whimpering grew louder as his footsteps approached, then abruptly fell silent."

show rowan necklace concerned at midleft with dissolve

ro "...Hello?"

"A frightened squeak was the response. Rowan turned the corner, and came face to face with a dead man."

show rowan necklace shock at midleft with dissolve

ro "{i}Simon?!{/i}"

simon "{i}Aaah{/i}! P-please, don’t hurt me!"

"It took Rowan a moment to recover from his shock to comprehend what he was looking at. Rowan put his hand upon the shivering, naked shoulder of the very-much-alive slave."
"The terrified man was covered in cuts and bruises, most of them made by a Succubus’ claws running down his back and chest."
"He was shaking like a leaf, curled up into the fetal position against the wall next to a set of sealed curtains that led presumably into Ishta’s room."

ro "Simon, what are you doing here?"

simon "It- it wasn’t me! Tell Mistress Nisei it wasn’t me! He’d said he’d tell her {i}I{/i} was to blame if I didn’t stay put!"
simon "Please, tell Mistress I’ve been good! I’ve been good, I swear! It wasn’t me!"

"Rowan felt a wave of wretched pity subsume him. He bent down to comfort the crying, blubbering man. But as he did so, a sudden, overwhelming question arose in his mind."
"{i}If this is Simon… then whose body is lying in Ishta’s arms?{/i}"

scene bg23 with fade
show rowan necklace angry at midleft with dissolve

"Rowan swept aside the curtains leading from Simon’s hiding place and stepped into Ishta’s room. His hand clenched in a white-knuckled grip upon his sword."
"The two bodies were right where he’d left them: motionless… but not lifeless."

show rowan necklace neutral at midleft with dissolve

ro "The charade is over. I found the real Simon."

show rowan necklace angry at midleft with dissolve

ro "{i}Whoever{/i} you are, you had best stand up and explain yourself."

"At first, nothing happened. Then, as if by magic, the dead body of Simon began to shrink. It contorted and shifted as a waxy figure came into view."
"He stood up and stretched, letting out an annoyed huff of air as he turned to face Rowan. His true features came to the fore."

show incubus 1 neutral at midright with dissolve

ro "Rylea."

rylea "And just who the hell are you supposed to be?"

ro "The man who’s going to turn you over to X’Zaratl for wasting my time."

"At that Rylea’s eyes went wide. He fell to his knees, clasping his hands together in desperate supplication."

rylea "W-wait, you cannot tell her! You {i}must{/i} not!"
rylea "I-I know I fucked up, okay? Rules are rules and… but I got so {i}mad{/i} at her-"
rylea "She- she deserved it, you know? That bitch deserved {i}it{/i}! "
rylea "She was going to run out on me - on {i}me{/i}, for that idiotic tart Nisei?"

"Rylea crawled on his belly, simpering on hand and knee as he scrabbled at Rowan’s boots."

rylea "I-I had to do it! She was gonna leave me out in the lurch {i}again{/i}! I walked in on her fucking Simon. Sweet, {i}innocent{/i} Simon-"
rylea "S-she was hurting him, you know? I had to protect him!"

"The lies and justifications came out so fast that Rowan didn’t have time to process them. He took a deliberate step back out of the wailing demon’s grasp."

ro "You had best explain yourself immediately, or I’m calling X’Zaratl."

"At this the demon calmed. He let out a frustrated sigh and picked himself up off the ground."

rylea "What a waste. All those hours lying on top of that dumb slut’s corpse, and for what?"

ro "Why did you kill Ishta?"

rylea "Why do you think? She was two-timing me behind my back! "
rylea "I walked in on her playing rough with a slave she {i}knew{/i} I liked. She could have killed Simon!"
rylea "I just… I saw red. I didn’t even realize what was happening till it was all over."

ro "-So instead of killing him, you stashed Simon away to keep for yourself."

rylea "The poor boy’s been brainwashed by Nisei, he would have told her everything!"
rylea "Besides, Nisei doesn’t deserve a sweetheart like Simon. Just look at how she treats him! "

ro "If you’ve been lying here this whole time, then who was the “Rylea” I just talked to a few minutes ago in your room?"

"Rowan saw the lie build in Rylea’s eyes before he ever parted his lips."

ro "Stop. Don’t even bother."
ro "If even a fraction of what your brood has told me is true, then I have ample reason to suspect who your accomplice is."

"{i}The very demon who put me on this path to begin with{/i}. Rowan thought darkly, thinking back to Deandra’s insinuations."

show rowan necklace neutral at midleft with dissolve

ro "You have a lot to answer for, X’Zaratl wants to speak to you."

rylea "Wait, human! Please, you must reconsider."
rylea "There must be {i}something{/i} I can offer you, in exchange for my freedom."

ro "I’m here to name names, demon. The only way you’re getting off the hook now is if I point the finger at someone else."

"The evil glint of Rylea’s smile sent a chill down Rowan’s spine."

rylea "Exactly my thought as well! What if I were to offer you my… {i}personal{/i} services?"

"The demon put himself on display, spreading his arms apart in sensual invitation."

rylea "We form a binding contract. You tell X’Zaratl that someone else was to blame. And in exchange, you mark me as yours. From here on in, I work for {i}you{/i} first before anyone else."

"Rylea’s pleading smile showed how desperate he was. This was his final gambit."
"Rowan considered the idea. It was tempting to have an ally in the Dark Sanctum wholly devoted to Rowan. What’s more, he was pent up from the frustrating chase he’d just undergone. It might be nice to blow off steam with a shapeshifting demon. "
"While finding the killer had been his task, the brood had lied to him repeatedly over the course of the investigation. He had no true loyalty to any of the ostensibly ‘innocent’ demons."

menu:
    "Accept Rylea's offer.":
        $ released_fix_rollback()
        ro "...Fine. I will keep your secret."
        ro "But you must swear personal loyalty to me. You will be my eyes and ears from now on inside the Dark Sanctum."
        rylea "You will not regret this, Rowan."
        "Rowan reached out and struck Rylea with the back of his hand."
        ro "Silence. You have wasted enough of my time. And now I’m left with a mess to clean up, and an underling to mislead."
        ro "X’Zaratl might be willing to tolerate a petulant child as a minion, but {i}I{/i} will not. "
        "Rylea, his cheek burning a bright cherry red, lowered his head in contrition."
        rylea "Yes… master."
        ro "We don’t have much time. We’ll take the tunnels back to your room. You can hide Simon in your harem till this all blows over."
        "At this Rylea perked up, a wide smile spreading across his face."
        rylea "{i}Yes{/i}, master!"
        scene black with fade
        pause 1
        scene bg23 with fade
        show rowan necklace naked at midleft with dissolve
        show incubus 1 neutral at midright with dissolve
        rylea "Are you ready to make the pact, master?"
        rylea "The loyalty ritual requires you to… {i}consecrate{/i} me."
        "Rylea let out an unsubtle giggle. Rowan sighed. They didn’t have much time, X’Zaratl still thought he was interrogating Deandra."
        show rowan necklace angry at midleft with dissolve
        ro "Then down on your knees, whore."
        #cg1
        scene cg665 with fade
        show incubus 1 neutral behind cg665
        show rowan necklace naked behind cg665
        pause 3
        rylea "Mmm, such a delicious looking cock."
        "Rylea, corrupted slut that he was, was already on his knees and peeling off Rowan’s pants by the time Rowan had issued the command."
        "The sultry demon took Rowan’s hardening length in hand and planted a delicate kiss upon the head."
        "A wave of sensitivity passed over Rowan’s shoulders as Rylea took an experimental lick. Whatever else could be said about the canny killer, he knew how to please."
        "Rylea took him in his mouth, suckling upon his cockhead as if savoring a delicious meal. The demons eyes fluttered shut as he let out a happy moan."
        "Rowan’s dick made a pop sound as Rylea pulled it to the corner of his cheek, then allowed it to slip free from his lips. He let out an appreciative gasp as he jerked him from the base."
        rylea "Mmmm, master’s cock."
        scene cg666 with fade
        show incubus 1 neutral behind cg666
        show rowan necklace naked behind cg666
        pause 3
        ro "No talking. If I wanted lip, I’d have sold you out to X’Zaratl."
        "Rylea, far from being deterred, let out a low giggle. He kissed Rowan’s shaft and jerked him more strenuously."
        "Rowan began to tire of the foreplay. He put his hand to the back of Rylea’s head, taking great fistfuls of his silky white hair in hand."
        "With a clench and a pull he forced Rylea down onto his dick. The demons eyes widened, and he mimed choking for a moment. But the ease with which he managed to deepthroat Rowan was telling."
        ro "That’s a proper look for you: choking on my cock like the degenerate, lying slut you are. No wonder Ishta chose Nisei over you."
        "Rylea - caught as he was with a mouthful of Rowan - merely moaned and gagged, his tongue swirling in eccentric circles as he lathered Rowan’s rod with glistening spittle."
        "Rowan reached down and casually slapped the sinful demon, reddening his cheek even as they suctioned tighter than a vice against his shaft."
        "Rowan picked up the pace, thrusting his hips against Rylea’s face so that his midriff bumped against the demon’s wrinkled nose. The sound of wet slapping filled the room."
        ro "Are you satisfied now, you fucking whore? You got everything you ever wanted."
        ro "Ishta’s dead, Simon is yours…"
        ro "And now you’ve got a {i}new{/i} master with a big, fat dick to suck. Things couldn’t have gone better for you, huh?"
        "Rylea shivered in place, his own erection poking pitifully upwards from his obedient kneeling position. He did not answer Rowan’s jeering, he merely tightened his lips and sucked harder."
        "Rowan put both his hands to the back of Rylea’s head, shoving him down to the base. The demon obliged his intrusion, opening his throat so Rowan could jam the whole of his cock down Rylea’s throat."
        "They met eyes: the triumphant human and his submissive demon. Rylea smiled at him through the corners of his mouth, his lips working the shaft even as Rowan felt the wet, slick slide of his tongue against his balls."
        ro "There you go, just keep groveling. Keep sucking that dick, and let your master do all the thinking for you."
        "Rylea fluttered his eyes. He {i}hummed{/i} with Rowan in his mouth, a curious vibration that brought Rowan to the very edge of orgasm."
        "Rowan stopped him with another light slap, pulling free from Rylea’s lips in a single smooth motion. The demon let out a mewling whine, but was silenced with a look."
        ro "Get on the bed, I’m not done with you."
        "Rylea giggled and did as he was told, crawling on all fours as he wiggled his bottom in the air. He slid out of his clothing like a snake shedding its skin, leaving his winking ass exposed to Rowan’s viewing pleasure."
        "Rowan approached, planting a harsh {i}smack{/i} against Rylea’s pert bottom. The demon squealed and lifted his hips, his long tail thrashing about in excitement."
        "Rowan didn’t bother with lube, he didn’t need to. Rylea was already ready and waiting for him. He pressed his dick against the demon’s yielding ass, and pushed."
        #cg2
        scene cg667 with fade
        show incubus 1 neutral behind cg667 
        show rowan necklace naked behind cg667
        pause 3
        rylea "{i}Mmm{/i} yeah, that's the stuff!"
        "Rowan’s cock slid into Rylea’s ass like it belonged there. The demon bit the pillow and suppressed a cry of pleasure. It slid deep into his rectum as Rowan put his weight behind the thrust, shoving Rylea into the mattress."
        "Rowan leaned his weight atop him, straddling Rylea’s ass as he angled himself for proper penetration. Rylea’s erect cock bounced from the momentum of his thrusts, spinning about in helpless, swirling circles as it drooled precum from the tip."
        rylea "{i}Mmm! Mm{/i}, yeah baby, just like that."
        "Such insolence. Rowan would not stand for it. It was bad enough he was covering up a murder for the impulsive creature, now he was dealing with a chatty slave."
        "Rowan spanked him. Hard. He planted the flat of his palm against Rylea’s pale skin at the same time as he thrust, sending the unexpecting demon into a conniption fit of shivers at the action. X’Zaratl had not been lying: he really did like to be dominated."
        ro "I told you to shut up."
        "Rylea giggled and pushed his rump back into Rowan’s hips, eager to bring their relentless mating session to its explosive conclusion."
        "Rowan laid himself atop the demon, shoving his head into the bed and pinning him in place. This was no romantic interaction, no slow buildup or casual mating. This was hate sex, of the most pitiless and callous kind."
        "Rowan laid into Rylea’s ass with all the vigor and strength that he would normally reserve for a foe on a battlefield. He slammed his hips against him again and again, ruthlessly railing his hole the way a barbarian would devour a flank of raw meat."
        "He took him by his throat, his hand clenching to give the illusion of choking. He wanted to dominate Rylea, to put him in his place and never let him live down the humiliation of his circumstances."
        "For Rylea, Rowan was salvation and safety. For Rowan, Rylea was merely a useful means to pleasure and influence. The tables had turned, Rowan had finally begun to play the Game of Demons."
        show cg668 with fade
        pause 3
        "His teeth clenched as he felt the building rise of something deep within him. His cock thickened in Rylea’s ass as he felt his cumvein bulge with all that pent up frustration, anger and spite. It was a tremendous relief of the body as he grunted and spurted and came."
        show cg668 with sshake
        show cg668 with sshake
        show cg669 with flash
        pause 3
        "Rylea, for his part, merely moaned and trembled beneath Rowan’s domineering presence. He yielded entirely to him, relaxing in his arms as Rowan planted his seed deep within him."
        "They held together for a minute for more, each reveling in the sensation of hot cum pouring into Rylea’s ass."
        ro "I’ve ‘concecrated’ you now, whore. The deal is struck."
        "Rowan pulled free, watching with dark glee the white fluid pouring from Rylea’s boneless and insatiate body. He had himself cum in the interim, his weak dribble soaking the bedsheets as he basked in the afterglow of the fuck."
        "Rowan pulled his pants up and made for the curtains without a second glance over his shoulder."
        ro "Remember this day well. I own you, now. You report to {i}me{/i}."
        "The only response Rowan got was a mumbled affirmative. He smirked to himself as he redid his sword belt and left the room."
        $ change_base_stat('c', 3)
        $ ryleaRowanSlave = True
        jump murderMysteryEnd
        
    "Accept Rylea’s offer, but demand he change gender.":
        $ released_fix_rollback()
        ro "...Fine. I will keep your secret."
        ro "But you must swear personal loyalty to me. You will be my eyes and ears from now on inside the Dark Sanctum."
        rylea "You will not regret this, Rowan."
        "Rowan reached out and struck Rylea with the back of his hand."
        ro "Silence. You have wasted enough of my time. And now I’m left with a mess to clean up, and an underling to mislead."
        ro "X’Zaratl might be willing to tolerate a petulant child as a minion, but {i}I{/i} will not. "
        "Rylea, his cheek burning a bright cherry red, lowered his head in contrition."
        rylea "Yes… master."
        ro "-And before we continue, change your form. If I’m going to treat you like a slut, I’d rather fuck a Succubus."
        "A gleam of masochistic glee entered Rylea’s eyes. He smiled, his face and form shifting even as he let out a sultry - and decidedly feminine - giggle."
        hide incubus 1 with dissolve
        show succubus 6 neutral at midright with dissolve
        femrylea "Mmm, {i}gracious{/i} what am I getting myself into?"
        "The now-Succubus Rylea exposed her thicker curves to him, plumping out her ass and quirking an eyebrow as her breasts grew to whorish proportions. Rowan’s eyes widened as he watched her rapid transformation."
        femrylea "First you subjugate me, {i}then{/i} you force me to take on a more pleasing form for your own, cruel amusement?"
        "Rylea chewed on her lip, letting out a sultry moan as she reached down to finger her new, dripping cunt."
        femrylea "Master, where have you been all my life?"
        show rowan necklace angry at midleft with dissolve
        ro "We don’t have much time. We’ll take the tunnels back to your room. You can hide Simon in your harem till this all blows over."
        "At this Rylea perked up, a wide smile spreading across her face."
        femrylea "Yes, master!"
        scene bg23 with fade
        show rowan necklace neutral at midleft with dissolve
        show succubus 6 neutral at midright with dissolve
        femrylea "So are you ready to make the pact, master?"
        femrylea "The loyalty ritual requires you to… {i}consecrate{/i} me."
        "Rylea let out an unsubtle giggle. Rowan sighed. They didn’t have much time, X’Zaratl thought he was still interrogating Deandra."
        show rowan necklace angry at midleft with dissolve
        ro "Then down on your knees, whore."
        #cg1
        scene cg787 with fade
        show rowan necklace neutral behind cg787
        show succubus 6 neutral behind cg787
        pause 3
        "Rowan sat down and spread his legs, inviting her to nuzzle against him like the desperate supplicant she was. He cast a dismissive glare down on her."
        ro "Hurry up, before I change my mind and throw you to X’Zaratl’s mercy."
        "Rylea perked up, rushing forward on her hands and knees to worship at his manly altar."
        femrylea "No! Oh Master, you mustn’t! She won’t punish me {i}nearly{/i} as well as you can!"
        "Rylea, corrupted slut that she was, was already on her knees and peeling off Rowan’s pants. Rowan grunted in annoyance at her exaggerated obsequiousness."
        "The sultry demon took Rowan’s hardening length in hand and planted a delicate kiss upon the head. A wave of sensitivity passed over Rowan’s shoulders as Rylea took an experimental lick." 
        "Whatever else could be said about the canny shapeshifter, she knew how to please."               
        "Rylea leaned her face into his lap, placing herself submissively at his feet took him in his mouth, suckling upon his cockhead as if savoring a delicious meal. The demon's eyes fluttered shut as she let out a happy moan."
        "Rowan’s dick made a {i}pop{/i} sound as Rylea pulled it to the corner of her cheek, then allowed it to slip free from his lips. She let out an appreciative gasp as she jerked him from the base."
        femrylea "Mmmm, master’s cock."
        ro "No talking. If I wanted lip, I’d have sold you out to X’Zaratl."
        "Rylea, far from being deterred, let out a low giggle. She kissed Rowan’s shaft and jerked him more strenuously."
        "Rowan began to tire of the foreplay. He put his hands to either side of Rylea’s face, clutching her for a moment like one would a treasured lover."
        "That all changed when he pulled her down with measured force onto his cock, taking great fistfuls of her silky white hair in hand." 
        "With a clench and a pull she forced Rylea down onto his dick. The demon's eyes widened, and she mimed choking for a moment. But the ease with which she managed to deepthroat Rowan was particularly telling."
        ro "That’s a proper look for you: choking on my cock like the degenerate, lying slut you are. No wonder Ishta chose Nisei over you."
        "Rylea - caught as she was with a mouthful of Rowan - merely moaned and gagged, her tongue swirling in eccentric circles as she lathered Rowan’s rod with glistening spittle."
        "Rowan used her head like it was his plaything, controlling the tempo of the blowjob by lifting and lowering her at his leisure, often at a speed just beyond that which was comfortable."
        "His brow turned downward as he let out a low expulsion of breath; the whore was a pleasing way to blow off steam, if nothing else. Rylea, sensing his increasingly aggressive movements, mimed choking when he pulled her down to the base."
        femrylea "{i}Huk{/i}!"
        "Rowan did not let up, holding her with ruthless aggression against his crotch. To her credit, Rylea merely moaned and suckled, tonguing his balls with her wet and suctioning mouth."
        ro "Are you satisfied now, you fucking whore? You got everything you ever wanted."
        ro "Ishta’s dead, Simon is yours…"
        ro "And now you’ve got a {i}new{/i} master with a big, fat dick to suck. Things couldn’t have gone better for you, huh?"
        "Rylea shivered in place, her hands drifting southwards to fondle her dripping nethers from her obedient kneeling position. She did not answer Rowan’s jeering, she merely tightened her lips and sucked harder."
        ro "There you go, just keep groveling. Keep sucking that dick, and let your new master do all the thinking for you."
        "Rylea fluttered his eyes. She {i}hummed{/i} with Rowan in his mouth, a curious vibration that brought Rowan to the very edge of orgasm."
        "Rowan stopped her, shoving her off his cock in a single, ruthless movement. Rylea came up coughing, wiping at her drool-caked face as she fought to catch her breath."
        ro "Stand up, I’m not done with you."
        "Rylea giggled and did as she was told, rising to her feet before bending at the hip to expose her soaking genitalia. She put her hands to her thighs as she wiggled her ass in the air."
        "Rowan approached, planting a harsh smack against Rylea’s pert bottom. The demon squealed and lifted her hips, her long tail thrashing about in excitement."
        "Rylea was already wet and waiting for him. He pressed his dick against the demon’s yielding cunt, and pushed."
        #cg2
        scene cg788 with fade
        show rowan necklace neutral behind cg788
        show succubus 6 neutral behind cg788
        pause 3
        femrylea "{i}Mmm{/i} yeah, that's the stuff!"
        "Rowan’s cock slid into Rylea’s tight pussy like it belonged there. The demon suppressed a cry of pleasure as he hit her deepest place. His dick slid deep into her as Rowan put his weight behind the thrust, shoving Rylea forward, nearly catching her off balance."
        "Rowan leaned his weight atop her, grabbing her by her wide hips as he angled himself for proper penetration. Rylea’s legs shivered from orgasmic pleasure at the immediate, relentless pounding Rowan delivered to her clenching cunny."
        femrylea "{i}Mmm{/i}! Mm, yeah baby, just like that."
        "Such insolence. Rowan would not stand for it. It was bad enough he was covering up a murder for the impulsive creature, now he was dealing with a chatty slave."
        "Rowan spanked her. Hard. He planted the flat of his palm against Rylea’s pale skin at the same moment as his deepest thrust, sending the unsuspecting demon into a conniption fit of shivers at the action. X’Zaratl had not been lying: she really did like to be dominated."
        ro "I told you to shut up."
        "Rylea giggled and leaned back on her heels, pushing her rump against Rowan’s hips. She was just as eager as he was to bring their relentless mating session to its explosive conclusion."
        "Rowan grabbed her by the wrists and pulled her flush against his back, humping her in rapid thrusts into her deepest core. She tilted her head back to look at him, her eyes ablaze with erotic pleasure."
        "This was no romantic interaction, no slow buildup or casual mating. This was hate sex, of the most pitiless and callous kind."
        "Rowan laid into Rylea with all the vigor and strength that he would normally reserve for a foe on a battlefield. He slammed his hips against her again and again, ruthlessly railing her the way a barbarian would devour a flank of raw meat."
        "He took her by her throat, his hand clenching to give the illusion of choking. He wanted to dominate Rylea, to put her in her place and never let her live down the humiliation of her circumstances."
        "For Rylea, Rowan was salvation and safety. For Rowan, Rylea was merely a useful means to pleasure and influence. The tables had turned, Rowan had finally begun to play the game of demons."
        "His teeth clenched as he felt the building rise of something deep within him. His cock thickened in Rylea’s cunt as he felt his cumvein bulge with all that pent up frustration, anger and spite. It was a tremendous relief of the body as he grunted and spurted and came."
        "Rylea, for her part, merely moaned and trembled beneath Rowan’s domineering presence. She yielded entirely to him, relaxing in his arms as Rowan planted his seed deep within her. They held together for a minute for more, each reveling in the sensation of hot cum pouring into Rylea’s pussy."
        ro "I’ve ‘concecrated’ you now, whore. The deal is struck."
        "Rowan pulled free, watching with dark glee the white fluid dripping from Rylea’s boneless and insatiate body. He shoved her to the bed, and she toppled onto the bed without protest, twitching in place as she endured an explosive orgasm." 
        "Rowan pulled his pants up and made for the curtains without a second glance over his shoulder."
        ro "Remember this day well, whore. I own you now. You report to {i}me{/i}."
        "The only response Rowan got was a mumbled affirmative. He smirked to himself as he redid his sword belt and left the room."
        $ change_base_stat('c', 3)
        $ ryleaRowanSlave = True
        jump murderMysteryEnd

    "Turn Rylea in to X’Zaratl":
        $ released_fix_rollback()
        "Rowan’s expression hardened. He drew his sword in a swift, smooth movement, pointing the tip of it directly in Rylea’s crestfallen face."
        ro "You’re coming with me, worm."
        rylea "Please don’t do this, I beg you!"
        ro "Shut up and follow me. If you try to run, X’Zaratl will be the {i}least{/i} of your problems."
        "The demon cowered before his blade, raising his hands in defeat as he made for the door. Rowan shoved him through, calling out in a loud voice so that all in the Dark Sanctum might hear of what had happened."
        ro " I found him, X’Zaratl! I found the killer!"
        jump murderMysteryEndTurnIn


label murderMysteryEndTurnIn:

scene bg23 with fade
show rowan necklace neutral at midleft with dissolve
#xzaratl happy
show xzaratl neutral at cliohnaright with dissolve

xz "You have done a great thing for me this day, Rowan."

show rowan necklace concerned at midleft with dissolve

ro "And yet, it feels like I’ve wasted my time."

"X’Zaratl smiled, putting a comforting hand on his shoulder as another swept smoothly about his waist. She pulled him tight in a side-hug, allowing him to feel the feminine curve of her hips against him."

show rowan necklace neutral at midleft with dissolve

xz "Don’t think of it like that. Thanks to you, peace - or what passes for it - has returned to the Dark Sanctum. "
xz "I may have lost my second, but I have retained the confidence of my brood, and kept the crisis to a minimum."

"She leaned in, her eyes lidding low as she planted a chaste peck on his cheek. He rubbed at the spot where the lipstick stuck."

xz "Thank you. I won’t forget this."

ro "What is to become of Rylea?"

#xzaratl angry

xz "Luckily for Rylea, he is too valuable an agent to simply dispose of."

#xzaratl happy

xz "But that doesn’t mean he won’t face harsh punishment."
xz "Aside from specific tasks I give him myself, he will not be allowed to leave his room or see his harem."

show rowan necklace angry at midleft with dissolve

ro "{i}That's{/i} it?!"

"X’Zaratl smirked."

xz "Have you ever seen what happens to a Demon who has been denied sexual partners or pleasure for {i}months{/i}?"
xz "Trust me, by the time I finally forgive Rylea of this slight, he will be {i}begging{/i} for the sweet release of death."

"Rowan suppressed an expression of disgust. Demon ‘justice’ was often more cruel and arbitrary than a simple execution. Rylea would certainly survive the ordeal, but he would be none too happy by the end of it."

xz "At least that settles things for now."

show rowan necklace concerned at midleft with dissolve

"{i}Not quite{/i}. Rowan thought. There was still the matter of Rylea’s accomplice."
"While Rylea had ultimately been to blame for the killing, it was obvious that Deandra had helped him try to cover it up… at least, at first. He could still out her, if he so chose to. X’Zaratl would certainly believe him."

show rowan necklace neutral at midleft with dissolve

"Then again, demons did hate tattlers. if Rowan wanted to, he could simply drop the matter and not tell Deandra’s mistress about her double-dealings. She {i}had{/i} helped him solve the murder, after all… in her own, duplicitous way."

menu:
    "“Tattle” on Deandra":
        $ released_fix_rollback()
        show rowan necklace angry at midleft with dissolve
        ro "Things aren’t quite as settled as you think. Rylea had help."
        ro "Deandra posed as Rylea when I went to interrogate him in his room. She tried to cover up the murder."
        #xzaratl neutral
        xz "Did she?"
        show rowan necklace concerned at midleft with dissolve
        ro "Yes. After trying to mislead me, she revealed the tunnels that eventually led me to Simon."
        ro "What confused me, however, is why she fed me the information needed to out Rylea in the first place. Supposedly, they were allies."
        "X’Zaratl let out a humored giggle, one she quickly tried to cover with her hand. Rowan shot her a quizzical look."
        #xzaratl happy
        show rowan necklace neutral at midleft with dissolve
        xz "You must know by now that my siblings’ definition of ‘ally’ is not quite the same as a Solansian’s."
        xz "This is a pleasant surprise. I wouldn’t have expected Deandra to show such calculation and forethought. At least, not for a few years yet."
        show rowan necklace shock at midleft with dissolve
        ro "You’re not… mad at her?"
        xz "Why would I be? She acted {i}exactly{/i} as one should in such circumstances."
        xz "She took advantage of a major shakeup in the brood’s power dynamic, betrayed a weak ally at a key moment for personal gain, and ensured she now sits at or near the top of the pecking order."
        #xzaratl neutral
        xz "-And she did it all while manipulating her superior, ensuring you came to your own conclusions while also pointing you in the right direction."
        xz "She outed Rylea, but avoided the stigma of being called a ‘tattler.’ She diverted blame while accomplishing her goals all at once."
        #xzaratl happy
        xz "If anything, she’s to be {i}commended{/i}. That is the exact kind of intuition and ambition that I’m looking for in a recruit."
        ro "But… she covered up Ishta’s murder!"
        xz "Did she? Rylea would disagree."
        show rowan necklace angry at midleft with dissolve
        ro "So, she deserves no punishment?"
        xz "Deandra is not to blame for Ishta’s death. That fault lies squarely on Rylea’s shoulders. She only did what was right, and took advantage of the situation."
        xz "If anything, this puts her on the shortlist for when I choose my new second in the brood. Such raw talent should be harnessed."
        menu:
            "Not good enough. She needs to be punished.":
                $ released_fix_rollback()
                ro "No. Unacceptable."
                ro "Your underling wasted my time on a wild goose chase, all the while playing me for a fool."
                show rowan necklace neutral at midleft with dissolve
                ro "I don’t deal with false-talkers, and I don’t trust minions who are ready to lie to my face to avoid responsibility."
                #xzaratl concerned
                xz "She is only doing what is expected of her, Rowan."
                show rowan necklace angry at midleft with dissolve
                ro "She is {i}expected{/i} to be loyal to those above her. I don’t care about the petty politics of your brood, I care that my time is being wasted."
                ro "Under no circumstances is she to be rewarded for this. I want you to make an example of her."
                xz " I suppose I could assign her to exclusive Orc relief duty for a few months. Not quite a slap on the hand, but-"
                show rowan necklace neutral at midleft with dissolve
                ro "Do whatever you deem necessary to get the point across. But a word of advice?"
                "Next time, leave me out of your brood politics."
                return
            "I suppose you’re right.":
                $ released_fix_rollback()
                show rowan necklace concerned at midleft with dissolve
                "It was hard to argue that Deandra had played him for a fiddle. As frustrating as it was to be used in that manner, she {i}had{/i} shown herself to be a capable demon. Rowan could harness that."
                show rowan necklace neutral at midleft with dissolve
                ro "Very well, but if you could pass along a message to her for me?"
                #xzaratl neutral
                xz "Of course."
                show rowan necklace angry at midleft with dissolve
                ro "Tell her: “Rowan Blackwell doesn’t give second chances to liars.”"
                #xzaratl happy
                "X’Zaratl’s eyes shined with mirth. She smiled and nodded."
                xz "I’ll be sure to relay that information to her."
                xz "The Dark Sanctum is, as always, at your disposal Rowan."
                return
                
    "Drop the matter.":
        $ released_fix_rollback()
        ro "...Yes."
        show rowan necklace happy at midleft with dissolve
        ro "That settles things."
        "X’Zaratl smiled back at him, genuine warmth in her features as she swept her arm out to encompass the whole of the building."
        xz "The Dark Sanctum is, as always, at your disposal Rowan."
        return

label murderMysteryEnd:

scene bg23 with fade
show rowan necklace neutral at midleft with dissolve
show xzaratl neutral at cliohnaright with dissolve

xz "Ah! Rowan, there you are."

#xzaratl concerned

xz "Deandra said you’d disappeared into the tunnels, and I thought-"

show rowan necklace concerned at midleft with dissolve

ro "I’m fine, I was just investigating a lead."

#xzaratl neutral

xz "Did you find anything conclusive?"

ro "Not exactly."

#xzaratl concerned

xz "This is not good, Rowan. While you were gone I took the time to look in Ishta’s room for more clues that might help the investigation. The slave’s body is gone."

show rowan necklace shock at midleft with dissolve

ro "Gone?"

xz "Gone. Missing. Someone has taken it."

show rowan necklace concerned at midleft with dissolve

xz "This has gotten out of hand. I {i}cannot{/i} report Ishta’s murder to the Twins without having the culprit well in hand. "
xz "If you can't prove who did it, a scapegoat will have to suffice."

show rowan necklace neutral at midleft with dissolve

ro "You’re okay with throwing one of your servants to the wolves?"

#xzaratl neutral

xz "If it means ending this threat to my rule, yes."
xz "The killer may still be at large, but I can at least send a message to the rest of the brood that these kinds of inter-demon squabbles won't be tolerated."

#xzaratl happy

xz "Besides, I won't be choosing blindly."
xz "You have spoken to my kin, who do {i}you{/i} think murdered Ishta?"

show rowan necklace concerned at midleft with dissolve

menu:
    "Ahrima did it.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        ro "Ahrima is the obvious culprit."
        ro "She had plenty of motive, and had the strength to follow through on the threat."
        ro "What’s more, she’s the only demon in the brood whose alibi didn’t have another demon present to corroborate."
        #xzaratl neutral
        xz "She {i}has{/i} chafed for a long time beneath Ishta’s shadow. It makes sense - given the injuries - that she just finally lost her patience."
        xz "Very well."
        
    "Nisei did it.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        ro "I think Nisei did it."
        "X’Zaratl tilted her head in confusion. She seemed surprised by the accusation."
        #xzaratl neutral
        xz "Really? Why?"
        show rowan necklace concerned at midleft with dissolve
        ro "Before Ishta was your second, there was an Incubus in the brood, yes?"
        show rowan necklace neutral at midleft with dissolve
        ro "Nisei was once his pet. When Ishta took over, she kicked him out of the brood and left Nisei alone with no allies."
        ro "My guess is, she harbored a grudge, and waited for a perfect moment to pay Ishta back in kind. Simon wasn’t a gift, he was a ruse."
        xz "If that is the case, then I shudder to think what she’s done with his missing body."
        
    "Deandra did it.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        ro "...Deandra did it."
        ro "She admitted that she saw Ishta as a wrongful pretender to the title of your second."
        ro "Given her proclivities towards shapeshifting and backstabbing, and the lack of struggle on Ishta’s part, she likely caught her unawares and had to kill her quickly."
        xz "An ambitious power move, if true."
        #xzaratl angry
        xz "But also a grave miscalculation, I do not reward senseless slaughter."
        #xzaratl neutral
        
xz "Very well. Then your part in this drama is done, Rowan."
xz "I assign our little scapegoat to the mines for now as a punitive punishment. A few weeks of mindless, menial labor should get the message across well enough."

ro "...For a murder?"

"X’zaratl smiled."

xz "Since I cant ascertain as to the actual guilt of the accused, yes. If nothing else, it tells everyone to knock off the infighting, or there will be consequences."

#xzaratl concerned

xz "An inelegant and imperfect solution, but it is the best I can come up with."

#xzaratl neutral

xz "Thank you, Rowan. I know how frustrating this all must have been for you."

show rowan necklace concerned at midleft with dissolve

"{i}Less than you might think{/i}. Rowan thought to himself, remembering the feel of Rylea’s velvety lips around his cock."

show rowan necklace neutral at midleft with dissolve

ro "Of course, X’Zaratl. But in the future: try to be more discerning with your recruits."

return


