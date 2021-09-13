
label rastInn:

scene bg40 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan sat down at the sparse desk next to his bed. A sheet of blank parchment and ink sat ready."
"If it was time to make a choice on who to side with, he was to call Ameraine so the two could make plans together."

label innMenu:
"The question was that. Was Rowan ready to choose who to side with?"

menu:
    "Yes.":
       $ released_fix_rollback()
       jump chooseRastFaction
       
    "No.":
        $ released_fix_rollback()
        jump rastMenu
        
        
label chooseRastFaction:

menu:
    "Side with Jacques and the Coppers." if copperJacquesMet:
        "Are you sure?"
        menu:
            "Yes.":
                $ rastAlly = "jacques"
                jump sideWithJacques
                
            "No.":
                jump innMenu
                
    "Side with Chancellor Patricia Crevette." if lodgeFirstMeetings:
        "Are you sure?"
        menu:
            "Yes.":
                $ rastAlly = "crevette"
                jump sideWithCrevette
                
            "No.":
                jump innMenu
                
    "Side with Duke Werden." if werdenConvinced == True:
        "Are you sure?"
        menu:
            "Yes.":
                $ rastAlly = "werden"
                jump sideWithWerden
                
            "No.":
                jump innMenu



label sideWithJacques:
    
"Regardless of the flaws and virtues of the other options, there were two facts about Jacques that stood out above the rest. The first was that he was capable, intelligent, and a natural leader of men."
"The second was that he had very little attachment to the way the Rosarian system currently worked. Rowan rather suspected that if he grew up in demon occupied territory, he’d do rather well for himself."
"But, why select a man with his own will and his own capacity to achieve it over a puppet?"
"Well, that was simple enough. It would be better for everyone if there was an independent human actor in Rastedel when it was all over. One who could exercise some modicum of power. One who was on good terms with Rowan."
"Perhaps he’d even be able to ensure the city went unmolested into the twins fold. A bloodless victory."
"When the letter was complete, Rowan ran it down to the bartender and returned to his room to wait. He didn’t have to wait especially long."

#show ameraine annoyed at midright with dissolve
show ameraine neutral at midright with dissolve


amer "I go through all the trouble of giving you advice, and you don’t listen to me."
amer "It’s as though you don’t enjoy our little friendship."

"Rowan lowered his head at the pale woman’s approach."

ro "Good evening, My Lady."

"Ameraine crossed her arms and stood in the center of the room."

amer "I fear I’m not much in the mood for pleasantries this evening. Why ignore my recommendation?"

"Rowan expected this. It wasn’t as though he would be able to do whatever he wanted without supervision. That was not how working for demons played out."

ro "I took the time to consider your advice, as well as the broader political situation. I believe that Jacques is the superior ally, even to Lady Crevette."
ro "The reason why is simple. If we back anyone besides him, I think we’ll lose."

#show ameraine neutral at midright with dissolve

amer "Oh?"

ro "You’re right. He’s smart. He’s too smart to easily control. "
ro "But, the prospect of bringing down the city from the inside is challenging enough without him as an enemy. Of anyone, he has the greatest chance of successfully launching a coup and setting the city into chaos."
ro "At the end of the day, what matters to my Masters is that the city falls. Any other detail matters less. You may know Rastedel better, but I know Bloodmeen."

"Ameraine put a hand to her chin." 
"In truth, Jezera actually tended to care a great deal about the mechanics of specific schemes, but if Rowan had one advantage in this conversation it was that Ameraine was pretty unfamiliar with her outside correspondence."

ro "If he proves troublesome, we can always do something about him after the city is secure. But, right now our prime responsibility is making sure that when Andras and the army arrive, the city is not prepared to stop him. "
ro "Everything else is secondary."
ro "Thus, Jacques is our man."

#show ameraine annoyed at midright with dissolve

"Ameraine sighed."

amer "I’m not sold, Rowan. I do not respond favorably to my advice being ignored. Not favorably at all. It is a very real possibility that you might find Jacques more willing to fight tooth and nail than Werden even…"

#show ameraine neutral at midright with dissolve

amer "...But, there is a reason I spend so much time with the man. He’s not boring, I’ll give you that."
amer "I will let him know you’re prepared to join him via an intermediary."
amer "When you’re ready, just go down to the Copper Club and pay him a visit. I am sure that you’ll be able to arrange the details amongst yourselves."

show ameraine neutral at edgeright with moveoutright

"Without anything further to say, the woman turned and began to sashay towards the door."

ro "Thank you. For trusting me."

amer "My darling, it’s hardly trust when there are backup plans. I’d rather not use them. Best make sure your efforts are not for nothing."

hide ameraine with dissolve
show rowan necklace happy at midleft with dissolve

if avatar.corruption < 31:
    "Rowan breathed a sigh of relief. She’d bought his rationale. Or at least, bought it enough to not stop him." 
    "For the first time since his return to Rastedel, Rowan felt a bit of weight lift off his chest. Maybe there was a way he could make sure that the city and its people remained safe without openly crossing the twins."
    "There was hope."

else:
    "Rowan smiled to himself. She’d bought his rationale. Or at least, bought it enough not to stop him."
    "This was why it was so important for him to remain in power. Who else was able to examine the situation and find the best solution if not him? The twins were too emotional. The solansian were blind fools."
    "Who else could make the world a better place if not him?"


$ rastForkingPaths = True

$ prevent_tile_exploration()
$ push_to_previous_tile()
return

#################################################################

label sideWithCrevette:
    
"It wasn’t like he hadn’t considered the other options. Ameraine had been right that Patricia was the figure with the most power closest to corruption. He was capable of reading that kind of thing now."

if avatar.corruption < 61:
    "Depressingly capable."

"If anything, that gave Rowan some pause. Should he really do this?" 

if avatar.corruption < 31:
    "She was a person. With hopes and dreams. They wanted to destroy those. Twist them. It wasn’t like this was the first time he’d seen this happen. But, the idea of it still weighed."
    
else:
    "If he tried to corrupt her, there was no way that Jezera and Andras would just allow him to maintain control over her. He’d essentially be handing them more power."
    
"But, at the end of the day, what other option was there? Jacques was snake and Werden was something else entirely."
"If he pushed for another candidate, then the chances of the mission failing. Patricia had to fall."
"When the letter was complete, Rowan ran it down to the bartender and returned to his room to wait. He didn’t have to wait especially long."

show ameraine happy at midright with dissolve

amer "Come around to my point of view, huh?"

"Rowan shrugged."

ro "No one has a better grasp on the city then you do. I wouldn’t have noticed it had you not pointed it out, but when I spoke to her I could feel the hunger coming off her."
ro "With the right bait, it should be possible to bring her around to our side."

"Ameraine chuckled to herself and leaned her slender frame close to the bed."

amer "You don’t need to praise me every few seconds. I’m not such a narcissist. The question that faces us now is how to go about it."
amer "Provided you actually make it into their ranks, of course."

ro "Do any of your sources know what they’d probably ask of me? Duke Raeve?"

"Ameraine shook her head."

amer "We’re just going to have to find out. I’ll have an intermediary put word of your interest back to Crevette."
amer "You’re going to have to go back and speak to her again to find out what she wants. Don’t worry though, you should have less trouble getting into the lodge."

"Rowan sighed. Working with Crevette probably meant having to work with Werden too, if not indirectly. Was he really ready for this?"

amer "I believe that should be everything. Get some rest before you speak to her tomorrow. Gotta have you at tip-top shape for destroying a realm."

hide ameraine with dissolve
show rowan necklace concerned with dissolve

if avatar.corruption < 31:
    "Destroy a realm. The thought made his heart almost stop beating."
    "Perhaps it might have been better had he died a long time ago. Lots of people might not have suffered for his mistakes…"
    "Was there ever going to be an end point?"

else:
    "Rowan sighed. Once he might have found the prospect of destroying the realm more distasteful. But, once felt like a long time ago now."
    "Even the past few days had helped to remove any lingering attachment to the Rosarian system. How had it survived this long ruled by such incompetent leaders?"
    "Maybe...maybe it deserved this. Maybe he was even doing Solansia’s work somehow. Maybe."
    "It deserved this. It truly did."

$ rastForkingPaths = True

$ prevent_tile_exploration()
$ push_to_previous_tile()
return

##################################################################

label sideWithWerden:

"Was he really going to do this?"
"There was so much that Rowan could say about Werden. That he was the most heartless man in the kingdom? That he had no respect whatsoever for the common people? No respect for Rowan?"
"But, he was also the man most capable of pushing back against the twins."

if serveChoice == 1:
    "When he first accepted his servitude, it was to bide his time and do something about them. He would still be limited, even allied with Werden. But, perhaps he could nudge events in a way that would bring about the best result. This was the moment."
    
elif serveChoice == 3:
    "He thought about Alexia. If he used his position to help out Werden, then it might put him and his wife at risk. But, Rowan was...even after all this time...who he’d always been. This was a risk he needed to take. "
    
elif serveChoice == 4:
    "Jezera had promised him, once, that they would make a better world together. Rowan still believed that. But, his heart burned at the prospect of what any plan would require. Maybe...just maybe...the best path laid in between Werden and Jezera."
    "It was something he was gambling a lot on."

else:
    "His heart burned with fear. What would the twins do if they found out that he was selecting Werden to defy them? Images of that dark cell he’d spent so long in came back to his head."
    "He had to do this, though. He was still a hero. Right? Right?"

"When the letter was complete, Rowan ran it down to the bartender and returned to his room to wait. He didn’t have to wait especially long."

#amer annoyed
show ameraine neutral at midright with dissolve

amer "I’d ask what in the six realms you’re doing, but I assume you don’t know yourself."
amer "Werden. Really? Have you lost your damned mind."

"Rowan leaned back in his chair. He expected this. It wasn’t the most obvious choice, by any means."

ro "I’m thinking quite clearly, My Lady."

amer "Then why Werden? The most incorruptible man in the entire realm?"

"Her expression shifted. It was hard to read what she was thinking."

amer "And I thought that you, more than anyone, would appreciate the value of vengeance. Werden has wronged you. You should wish him dead."

show rowan necklace angry at midleft with dissolve

"There was something to the way she said it which gave him chills. Ameraine was no stranger to vengeance, it seemed. Something to make note of for the future."
"Did Rowan wish Werden dead truly?"

if avatar.corruption < 51:
    "In most situations, he’d deny it. Rowan tried to understand his perspective. He did. But, now was not the time for denials."

else:
    "Perhaps Rowan might have answered differently in the past. But, much had changed. He truly did wish Werden dead. It made knowing what he had to do all the more difficult."

ro "Aye, I wish him dead. Of course I do. But, I am here on a mission. Bringing down Rastedel comes before anything. Even making the score with him even."
ro "...Because for better or for worse, there is one man who can bring down Marianne. Jacques can’t do it. If we tried to replace him with Patricia, it would fall apart."
ro "Werden must be the one to take power, because he is the one most likely to pull it off. And the success or failure of the plans depends on the kind of chaos that would create."
ro "Destabilizing the city comes before everything. We can kill him when it’s all over."

"Ameraine tilted her head. Selling people on his hatred for the man was simple when Rowan truly did hate him."

amer "That’s a big if. You risk him taking the city and stabilizing the situation so quickly that it ends our chance to exploit the power vacuum."

show rowan necklace neutral at midleft with dissolve

"Ameraine sighed."

amer "Werden, huh?"
amer "Fine. I’ll get word through Duke Raeve and set up a one on one meeting. He might not even agree to the idea."
amer "You’re responsible for selling the idea up the chain to the pair who hold your leash."
amer "And don’t forget for a moment that I’m watching you. I will not see my plans ruined by anyone. Anyone at all."

ro "I will not forget for a moment, My Lady."

hide ameraine with dissolve
show rowan necklace happy at midleft with dissolve

"Rowan breathed a sigh of relief. None of this would matter though if he couldn’t persuade Werden to allow him into his inner circle. Now the real mission began..."

$ rastForkingPaths = True

$ prevent_tile_exploration()
$ push_to_previous_tile()
return

#################################################################################
#################################################################################
#################################################################################

label postForkCommonEnding:

scene bg40 with fade
show rowan necklace concerned at midleft with dissolve

"When the meeting was over, Rowan retreated back to his room in the inn and laid back on the bed. He was expected to clear out the Abbey, but perhaps he could work his way into their confidence even further by taking it without the heavy casualties they expected."
"If only the orcs actually had been loyal to Bloodmeen. This would be a lot simpler."
"Rowan sighed and brought the amulet that Jezera had given him close to his lips."

ro "This is Rowan, reporting from the capital."

ro "I require your assistance..."

$ rastAllyChosen = True
$ verdoinCounter = 2

#temp - make copper club / lodge unavailable
$ rastCopperAccess = False
$ rastLodgeAccess = False

$ prevent_tile_exploration()
$ push_to_previous_tile()
return

#####################################################################################
#####################################################################################
#####################################################################################

label fall_of_crevette:

$ patriciaCorrupted = True

scene bg40 with fade
show rowan necklace neutral at midleft with dissolve
#ameraine annoyed
show ameraine neutral at midright with dissolve

"Rowan sat on his bed, arms crossed, and counted the seconds as they fled. Lady Patricia was going to be here soon. This was to be the centerpiece of the plan. The moment Patricia was brought aboard." 
"Rowan wasn’t alone in the room. Ameraine stalked back and forth like a cat."

amer "When will she be here? Having my time wasted is not a thing I accept idly."

ro "Soon. Chancellor Patricia received the time and location. But, you needed to be here beforehand. We need to discuss how the meeting will go."

"Ameraine brushed some of her long dark hair over her shoulder."

amer "We’re simply going to tempt her, right? Or is there another element that I am missing?"

"Rowan nodded slowly. He’d been told to wait for the right moment by Jezera. But, that moment was now."
"He reached into a satchel by the bedside and pulled out the box that Jezera had gifted him with. Ameraine slid over and snatched it from his hand. It rattled softly when shaken. There was jewelry inside."

ro "From Mistress Jezera."

show ameraine happy at midright with dissolve

"Without a hint of sentiment, she tore the package open. A jeweled silver choker was revealed inside. In the center, and outlined along the different edges, were glittering sapphires."
"Rowan marveled at the sheer beauty of the thing, but Ameraine seemed more inclined to study it, almost as though she’d opened a page in a book."

amer "Interesting."

ro "You recognize it?"

"She pointed to the side of the choker. Only now did Rowan realize that there was writing on it. Though, there would be no point trying to read it. The script was in some forbidden language."

show ameraine neutral at midright with dissolve

amer "The runes on the edges. Yes. I don’t know the spells off the top of my head. I am not much of an enchanter, I am afraid. But, easy enough to read. This is a fairly powerful charm."
amer "The runes here mean...well it’s hard to put into common tongue, but something like desire or “Soul Want”."

"She pointed to the runes on the other side."

amer "These ones are normal linking terms."
amer "And this one...hm…"

"Rowan waited in silence as Ameraine deciphered the script. This was not his element."

amer "It’s a binding amulet. Simple soul linking. "
amer "Feed in a desire, bind the desire to a pact. Then the subject is left mentally linking the two together in their mind."
amer "A perfect subordinate. Perhaps a bit of a single minded obsessive though. But, that’s the problem with thought magic. Minds are meant to work as discrete wholes."

"Rowan grabbed the charm from her hand. It was so small. Small enough to roll about in his palm even. His other hand went to amulet around his neck."

if avatar.corruption < 31:
    show rowan necklace angry at midleft with dissolve
    "But, there was only so long he could even stand to hold such a thing. The charm went tumbling from his hand to the wooden floor. "
    ro "There’s evil in that thing."
    show ameraine happy at midright with dissolve
    "Ameraine chuckled to herself."
    amer "Of course, there is. Did you think we were going to corrupt her with children’s toys and flowers? A little bit of sex to get her warmed up, couldn’t hurt, but this will help with the heavy lifting."
    ro "..."
    show rowan necklace concerned at midleft with dissolve
    ro "There isn’t another way?"
    "Ameraine shrugged nonchalantly."
    amer "She gave it to you, didn’t she? I doubt she’d much take to the idea of it not being used. Besides, it makes both of our jobs much simpler."
    "Of course, it couldn’t remain on the floor forever. Rowan scooped it up. As he did, his eye was caught on the large sapphire in the center. When it sparkled, he could have sworn there was movement. Something was inside of it. Or was it just his imagination?"
    "Ameraine was looking at him expectantly."
    show ameraine neutral at midright with dissolve
    amer "She never intended for you to be the one to use it, did she?"
    "Was it so easy to tell?"
    ro "I’m supposed to give it to you."
    "She held out her hand."
    amer "That makes it easier. I will handle the hard work. You’ll just help me get her into the right mindset. "
    show ameraine happy at midright with dissolve
    amer "That much you are capable of, yes?"
    "Rowan placed the charm into her hands. Even that relieved him a bit. Now that he knew what it was, even holding it was stressful."
    ro "I’ve done worse before, I suppose..."
    
else:
    ro "So, how would that play out in practice?"
    "Ameraine raised a skeptical eyebrow to him."
    amer "Jezera didn’t tell you?"
    "Rowan kept his face empty. Jezera had told him to give the amulet to her and let her handle it. It wasn’t as though he would break that command. But, something felt off about the idea of just telling her now. Like it would hand her power over the situation."
    ro "She told me that you’d be able to explain its function to me. Jezera is not one for sitting around giving instructions."
    #if low / medium deception TO DO
    "She didn’t seem pleased by that explanation. But, Rowan had the benefit of a closer relationship with the demoness. Still, it left him feeling the need to break the silence."
    #high deception TO DO
        #"It was a good thing Rowan had become such an accomplished liar of late. Ameraine raised an eyebrow skeptically, but hardly seemed to dwell on it."
    "I don’t know. You said it would be simple to operate, right?"
    amer "Well, simple enough."
    "She approached him and pressed one of her long nails to the charm."
    amer "I presume you must get her to put it on voluntarily. The effect requires the subject’s mental participation. Overwhelm her but keep her following along with you. But, once you have her, there’s a magic word trigger."
    "She scooped it up from his hand took a closer look at the runes."
    amer "One moment."
    "It only took a few minutes of study for the mysterious woman to arrive at an answer."
    amer "Aran-Uch-Ah."
    amer "That’s the word. Say it and the effect will come to life. At that point, all that is required is to ask her Soul Want and then to make her an offer for it."
    "Rowan nodded slowly and retook the amulet from her hand. This magic nonsense was beyond him. Yet, he could not fault its efficiency."
    amer "The soul binder should be able to use that information to produce a “deal” so to speak. "
    ro "Aran-Uch-Ah."
    show rowan necklace concerned at midleft with dissolve
    "For just a moment, as he said the words, there was a flicker. It was almost as though there were something inside of the large sapphire at the center. A shiver ran up his spine."
    show rowan necklace neutral at midleft with dissolve
    "Ameraine stood by, waiting to hear the next detail. Rowan’s glance drifted back and forth between her and the charm."
    show rowan necklace angry at midleft with dissolve
    "He’d put so much work into personally corrupting Patrica. It was a perverse thing to even think, but wasn’t this like a wolf handing off his kill to a more senior wolf who’d simply stood at the sidelines?"
    show rowan necklace neutral at midleft with dissolve
    "But, Jezera had told him to give Ameraine the charm. To let her operate it using her superior knowledge of magic. It was certainly a safer choice. Both in terms of the success of the plan…"
    "...and safer if Jezera were to decide to dig deeper into this day’s events..."
    
menu:
    "Give Ameraine the charm.":
        $ released_fix_rollback()
        $ ameraineCharm = True
        $ rowanCharm = False
        "Rowan sighed. There really wasn’t a point in being difficult with so much on the line. Ameraine gave him a quizzical look as Rowan placed the charm into her hand."
        amer "A prudent measure. I wouldn’t dream of trying to pull the wool over her eyes. But, you may stay in the room nonetheless."
        "She flashed a sharp smile."
        #ameraine smirk
        show ameraine happy at midright with dissolve
        amer "Besides, she’ll be much easier to bring to bed with you there to guide her into the proper place."
        amer "You just need to follow my lead."
        "Rowan sat passively on the bed as Ameraine ran him through the plan. It was bold and forward. Not quite what he’d do in this situation. But, he’d spent enough time with Ameraine to trust her sense when it came to intrigue."

            
    "Keep the charm.":
        $ released_fix_rollback()
        "His fingers closed around the charm."
        ro "Very well. I’ll ask you to leave a little before I use it on her. You’ll need to fill me in any other details of its operation before she arrives."
        show ameraine neutral at midright with dissolve
        "Ameraine raised an eyebrow. The woman was an expert at intrigue. It’d take more than that to fool her."
        amer "I’m not to stay for the ritual?"
        #easy deception check - TODO
        ro "I’m not sure my Mistress wants to hand you that kind of power yet. She told me to corrupt Patricia myself. She might be quite displeased."
        ro "Besides, Patricia trusts me, but she doesn’t trust you. You said the process requires the consent of the subject to work properly."
        "Rowan kept his face expressionless. Unlike Ameraine, he had a direct line to Jezera, and Rowan intended to fully exploit that."
        "After a few moments of consideration, Ameraine’s posture slouched. Rowan thought he saw something from the look in her eyes. Disdain perhaps?"
        amer "Fine. Stupid, but fine. Patricia is not of great interest to me either way. Take her. Leave her. Whatever. If you insist on completing the ritual yourself, then be my guest."
        amer "But, you understand that if you screw up, we have to kill her, right? Word cannot spread of Rowan Blackwell trying to corrupt court officials with black magic."
        show rowan necklace happy at midleft with dissolve
        ro "He faked a laugh."
        ro "I’ll kill her myself if it comes to that."
        $ ameraineCharm = False
        $ rowanCharm = True
        #if failed
            #ro "Well, she said I was the one who needed to perform the ritual. I am her agent in the city, after all."
            #"Ameraine paused to consider his words. A bead of nervous sweat formed at his temple. This kind of nervous deception was not Rowan’s natural element."
            #show ameraine happy at midright with dissolve
            #"Then, she started to laugh."
            #amer "That’s cute. You can stay and watch if you like. I’m sure your Mistress would be content with that."
            #amer "But, do you truly expect me to believe that she meant for a human who couldn’t even {i}read{/i} the runes to perform the ritual?"
            #amer "Absurd."
            #"She was right, of course. Rowan was not prepared to use the amulet himself. Why would he be put in charge? Perhaps this had been a bad idea. Still, he had to try."
            #ro "I’m serious."
            #show ameraine neutral at midright with dissolve
            #amer "As am I. I’m not about to knife my ally over such a trivial matter. And should you and your untested abilities screw this up, it could mean tragedy for us both."
            #amer "Hand it over."
            #"With a sigh, Rowan let the gem slip through the gaps of his fingers into Ameraine’s outstretched grasp."
            #$ ameraineCharm = True
            #$ rowanCharm = False

scene black with fade
pause 1
scene bg40 with fade

show rowan necklace neutral at midleft with dissolve

"The sun was now starting to set. Rowan could see it through his window. He was roused by a knocking at the door."

show patricia happy behind bg40

patr "So this is where you’ve been staying, huh? You should have told me you needed a room to stay in. My brother has a nice villa by the riverside in the Noble District that I’ve been using."

"Rowan opened the door slightly to let his guest in."

hide patricia
show patricia happy at midright with moveinright

patr "Now, then. Before we get started with the meeting. I think it’s time that you...made good...on some of those promises you gave me the last time we…"

show ameraine happy at edgeleft with dissolve

amer "Promises, Rowan? Sounds scandalous."

show patricia neutral at midright with dissolve

"Patricia’s eyes shot Ameraine. The pale woman was laying on Rowan’s bed on her side. She looked like a lazy cat."

show patricia annoyed at midright with dissolve

patr "Excuse me, who are you? What are you-"
patr "Wait, I’ve seen you before. You’re part of Lord Mineur’s circle, aren’t you? Who invited you here?"

"Rowan sighed and took a step back. Patricia’s eyes fiercely met Ameraine’s."

ro "Lady Crevette. Meet Lady Ameraine."
ro "Lady Ameraine. Meet Lady Crevette."
ro "Lady Ameraine has been my ally since I first returned to the Capital. She’s an incredibly valuable information broker."

show patricia neutral at midright with dissolve

"Ameraine rose gracefully to a standing position, only to then bow forward respectfully. Lady Patricia took a few seconds to consider how to reply before offering a perfunctory curtsy. But, for a passing moment, Rowan thought he saw Patricia shoot him a nervous glance."

amer "I’ve heard so much about you, My Lady."

patr "I see."

"Patricia turned back to Rowan. He’d spent the entire greeting watching, as though he were introducing a dog to a cat for the first time."

patr "I must admit, I’m curious. Why is she here exactly?"

ro "I decided that she’d be valuable for any plans we might come up with for strategy during the coup. She has inside knowledge that few others can match."

show patricia shocked at midright with dissolve

"Patricia’s eyes went wide as she processed the words coming from his mouth."

show patricia annoyed at midright with dissolve

patr "She knows about the coup!? Did you tell her?"

"Before he could reply, Ameraine interjected."

amer "The reverse, I’m afraid. He went snooping around your little lodge at my suggestion based on the whispers I was hearing. I may well have known about it before you did."
amer "Worry not though. My lips have been sealed shut when spending time with my bald-headed friend. I prefer backing a winner."

"A hush fell. Would Patricia buy that explanation so easily? Ameraine had said it with certainty, but Patricia easily could break into a panic. This was the first real test."

patr "..."

show patricia neutral at midright with dissolve

patr "Fine. She can stay."

"Rowan exhaled."

amer "Do you drink, My Lady? I brought some fine red."

show ameraine neutral at edgeleft with dissolve

"Nobody really needed to answer the question. Now with a cup in her hands, Patricia settled at the little table and the others followed her. Ameraine and Patricia traded hesitant pleasantries. It was enough to help Patricia’s tone start to thaw."
"Then the topic of the meeting came to the fore. The coup. The following hour was spent going back and forth over the minutiae of the plan. The placement of troops, the chance of success. Most of all, where Duke Werden would be for the operation."
"Yet, Rowan couldn’t help but notice Patricia’s posture. Straight back. Formal. She even kept her drinking within moderation. Her guard was still up, even as her familiarity with their strange third wheel grew."

show ameraine happy at edgeleft with dissolve
show rowan necklace shock at midleft with dissolve
show patricia shocked at midright with dissolve

"Not that Ameraine seemed to make it easy for Patricia to warm up. She kept on making jokes that Rowan recognized instantly as flirting. For her part, Patricia seemed to have little idea what to do with it. Every time Ameraine would reference sex, it left Patricia visibly flabbergasted."
"Once she even found an occasion to give Patricia a slap on the ass. Rowan had been as shocked as Patricia. Yet, also surprised that the noblewoman had not protested louder."
"Rowan didn’t quite understand what Ameraine was doing. Was she testing Patricia?"

show ameraine neutral at edgeleft with dissolve
show rowan necklace neutral at midleft with dissolve
show patricia neutral at midright with dissolve

"After a time, it was Ameraine who addressed the spectral presence in the room. What topic of what would come after."

amer "In the case of a power struggle, I would place a good-sized bet that you’d be able to bring Jacques or his successor on your side. Compared to other nobles, you have much more business acumen from years in administration."
amer "Rowan, meanwhile, is still beloved among the professional class. They respect competence and someone who can rise above his station."
amer "Even outside the noble quarter, you’d be their choice of leader, My Lady."

"Rowan jumped in. If there were any hope of persuading Patrica, he’d have to be involved."

ro "Combined with the support I can draw on from the northside, that would represent a sizeable coalition. Larger than any other potential leader of the purples could draw on."

"Patricia’s eyes studied the merchant quarter on the map at the table."

patr "You’re not totally wrong. But, the Coppers wouldn’t just align with me for nothing. You strike me as the type who knows how to whisper in someone’s ear. But, you can’t possibly be so good as to bring them around for free."

show ameraine happy at edgeleft with dissolve

amer "You’d be surprised, My Dear. You haven’t heard me try to whisper to you."

#patricia embarassed

"Patricia rolled her eyes and looked exasperated. She’d been so effective and rebuffing Rowan’s advances for awhile, yet against Ameraine’s wiles she seemed lost. Naturally, Ameraine looked pleased with herself."

show patricia neutral at midright with dissolve

patr "You must tell me the truth. I’d have to give them something, wouldn’t I?"

show ameraine neutral at edgeleft with dissolve

amer "A portion of the council seats that used to go to the priests, probably. An end to the quota system and limits on the internal movement of goods. Offer that and they’re yours."

show patricia annoyed at midright with dissolve

"That only earned an angry scoff from Patricia."

patr "Pah. Those damn spice merchants and profiteers. Every last one of them thinks they can run the state economy more than I can."

show patricia neutral at midright with dissolve

patr "Hrmmm."

"Patricia leaned back in the chair. As the moments dragged on, that turned to furrowed eyebrows and the relaxation her posture had developed went away."

patr "What does it matter?"
patr "You talk as though we will wake up tomorrow and Werden will no longer command the faction. I apologize, My Lady, but that just isn’t how it works."

"She rose from her chair and walked back slightly. She hung between the table and the door. Yet, her eyes hung on Rowan and Ameraine still."

show patricia annoyed at midright with dissolve

patr "The truth remains. You cannot hide it. Would this hypothetical plan of yours require that Duke Werden be taken off the board somehow?"

"Rowan just shrugged his shoulders and drank a bit from his own glass of wine."

ro "Honestly? Probably."

if avatar.corruption < 31:
    show rowan necklace concerned at midleft with dissolve
    "Rowan closed his eyes and breathed inwardly. There was a role he needed to play here."
    
show rowan necklace angry at midleft with dissolve
    
ro "While he is in action he’d be impossible to replace and would never accept the control of another. But, during the chaos of the coup, he can be removed from play. We know when there will be an opportunity. "

#and low deception - TO DO
if avatar.corruption < 31:
    "His voice cracked slightly as he said it. Rowan had to struggle to keep his speech straight else he seem out of his depth."

ro "Once he’s gone, who can challenge you for leadership? His sons lack his obvious fire and authority. None of the other dukes would be able to put together a coalition fast enough."
ro "But, we could have the city guard, the merchants, the normal people, and at least a portion of the nobles aligned behind us before anyone else even realizes what is happening."

show patricia shocked at midright with dissolve

"Patricia froze where she was standing and looked at him with new eyes."

patr "Rowan. You’re openly talking about assassinating Duke Werden. I may not like him, but he’s a duke."

"Ameraine raised an eyebrow."

amer "You’re also talking about overthrowing the right hand of the Baron appointed by the Goddess herself. Surely everything is on the table."

show patricia annoyed at midright with dissolve

patr "No one is considering killing her."

amer "My lady, do you truly believe you will take over the capital and overthrow the existing order without having to kill people?"
amer "I had not believed you to be such an innocent thing."

"Patricia crossed her arms. "

patr "How dare you!?"
patr "This..it’s different. We’re at war and that bitch is losing it. It has to be done."

show rowan necklace concerned at midleft with dissolve

"Rowan rose to his feet and walked over to Patricia. She didn’t recoil at his approach. A good sign. Neither did she object when he placed a hand on her shoulder."

ro "My Lady. I’m not sure Werden being in charge would fix the problem of the war either. "
ro "He is a hard man. Perhaps too hard to really win in a war of this sort. The demons will simply melt back and refuse to do battle with him. Would his men really follow such a strict disciplinarian for long enough to do the hard work of rooting them out?"

show patricia sad at midright with dissolve

"She sighed and looked away."

patr "I don’t want to kill him. I don’t."

"Rowan didn’t give her the comfort of not meeting his eyes. He tilted her chin so they would remain face to face."

show rowan necklace neutral at midleft with dissolve

ro "If we kill him, you can be in charge. The council is yours. The country is yours. You can make the hard choices needed to defeat them."

patr "But, murdering a duke? How could I do such a thing…?"

show ameraine happy at edgeleft with dissolve

"That was when Ameraine broke the moment. After a loud yawn, she interjected into the moment."

amer "Stab him. Poison Him. The same way you murder anyone else, I would say."

show patricia annoyed at midright with dissolve

"Patricia shot her a dark glare."

if ameraineCharm == True:
    patr "You know exactly what I meant."
    #ameriane angry
    show ameraine neutral at edgeleft with dissolve
    show rowan necklace shock at midleft with dissolve
    "Ameraine’s face hardened in a way Rowan hadn’t seen it harden before."
    amer "And you do not appear to know what I meant. I bore of this."
    "Ameraine too left her seat, but rather than joining them, she perched herself atop the table and crossed her legs."
    show patricia shocked at midright with dissolve
    "Rowan and Patricia both took a step back."
    amer "Lady Crevette. Why are you even here?"
    "The accusation left Patricia sputtering."
    patr "Because Rowan-"
    amer "I do not have endless tolerance for games. You are here because you want something. Were you content with your life as it had previously existed, you would not be in a room with Rowan and I discussing such hypotheticals."
    patr "..."
    "Rowan closed the distance back to the table. This hadn’t been in the plan. He didn’t know what Ameraine was doing, but it seemed to be messing up everything. How long could she treat Patricia this way without sending the noblewoman running?"
    show rowan necklace neutral at midleft with dissolve
    if avatar.corruption > 60:
        "Although, it was amusing. He’d give her that much."
    ro "Lady Ameraine, I don’t think that you need to be so direct."
    amer "I think you need to be more direct."
    amer "I enjoy skulking around the point as much as the next woman. But, the truth is in front of us and we may as well put it on the table. "
    "She trained her gaze on Patricia. A direct challenge."
    amer "You are here because there are things you want, Patricia. Things that Rowan and I can give you."
    show patricia annoyed at midright with dissolve
    "Patrica’s hands shook and balled into fists. Now she too marched forward. Even standing up, she still was half a head shorter than the other woman."
    patr "I am a lady. The daughter of the Gordon Crevette. Just because you are some friend of Rowan’s does not mean that-"
    show ameraine happy at edgeleft with dissolve
    "Ameraine giggled playfully, cutting off Patricia’s protestations."
    amer "I will make this more simple still."
    "Without warning, Ameraine dug her hand into Rowan’s shirt and dragged him headfirst into a kiss. Rowan nearly jumped, his fight or flight instincts coming into focus. Ameraine moved her hand so fast, even Rowan’s strong reflexes were left struggling."
    show rowan necklace shock at midleft with dissolve
    "But, once he realized what was happening, he let himself melt into the kiss."
    #patricia aroused
    show patricia neutral at midright with dissolve
    patr "Wait. Hey-"
    "Rowan blinked softly as the kiss broke. Patricia’s face had gone fire red at the sight."
    amer "Did that make you mad, Patricia?"
    show patricia annoyed at midright with dissolve
    patr "Yes. Yes, it did."
    "Patricia answered through her teeth, barely able to able to break a grimace."
    amer "Why?"
    patr "Because I-I.."
    amer "Because you have been waiting to kiss him the entire time?"
    "There was a pause. Patricia seemed to try on different replies, like dresses, at a store, before arriving at the one she knew she had to pick all along."
    patr "...Yes. Yes because I’ve been waiting to do that the entire time."
    amer "Rowan, would you object if Patricia kissed you?"
    "Rowan looked back and forth between them. Ameraine’s switch in plans was started to make more sense to him. Had all of that teasing earlier just been feeling her out?"
    show rowan necklace happy at midleft with dissolve
    ro "Not especially, no."
    amer "So there you have it. Just kiss him."
    #patricia aroused
    "Patricia looked to Rowan and then back to Ameraine, never deciding on whom her eyes should rest. She brought a thumb to her lips and bit it softly."
    patr "Here? In front of you? Weren’t we-"
    amer "This is the Lady Crevette with years of sexual experience? Blushing like a maiden at as chaste suggestion as a kiss?"
    patr "..."
    "That seemed to settle it. Stiffly, as though doing so were a way of giving spite to Ameraine, Patricia marched right up to Rowan. There was a lingering moment with their lips mere inches from each other."
    "Then, Patricia leaned up and planted a long delicate kiss on Rowan’s lips. Rowan placed his hands on her sides. It only broke when Patricia turned to Ameraine with a triumphant expression."
    patr "There. Happy?"
    amer "Progress, but not there yet."
    patr "Excuse me?"
    show ameraine naked neutral at edgeleft with dissolve
    "Without warning, Ameriane’s hands went to dress. Patricia and Rowan gawked as she threw the dress off. Neither of them seemed to notice Patricia slip out of his grasp."
    "Ameraine retook her former position, now stripped down to nothing but black lace underwear and a pair of heels so long and thin that they could probably pierce skin."
    patr "I had not expected..."
    amer "Yes, of course. You had not expected me to undress here and now at the table. There are rules of decorum, after all."
    "She yawned. Ameraine had a strange comfort in her nudity. Not the flaunting Rowan was used to expecting from Jezera, but a humble nonchalance."
    amer "But, I wanted to lose my clothes. So I did."
    "Somehow, that answer didn’t seem to satisfy Patricia. She stood frozen like an animal newly caught in a trap."
    show rowan necklace shock at midleft with dissolve
    "Rowan was left to reflect on this. He was used to more...sexual tactics by now. But, Ameraine had never mentioned using one. After all, as far as they both knew, Patricia was not interested in women."
    "Was Patricia interested in women?"
    amer "Easy right? I’m going to show you something else."
    #cg 1
    scene black with fade
    show ameraine naked neutral behind black
    show patricia neutral behind black
    "Ameraine pushed further. She raised one of her heels and pressed it hard against Patricia’s chest. The supple flesh of the other woman’s breast was indented by the force of the heel." 
    "Yet, Patricia still didn’t run away. She only seeded space to Ameraine, taking a step back. Her face had gone totally white."
    amer "You didn’t just come here to get a kiss from Rowan, did you?"
    patr "We just met one another and you’re just-"
    "Her weak protestations were cut off by a loud tsk."
    amer "No more games. You came to be fucked."
    patr "I-"
    #cg 1 - var 2
    scene black with fade
    show ameraine naked neutral behind black
    show patricia neutral behind black
    show rowan necklace neutral behind black
    "Ameraine slowly lifted herself from the table. Her foot angled downward. The effect was simple. There were only two ways Patricia could go, further away or down. She went down."
    if avatar.corruption < 31:
        "In the span of seconds, she had Patricia lying on the ground, pinned by her heel. Rowan watched in shock."
    elif avatar.corruption > 60:
        "In the span of seconds, she had Patricia lying on the ground, pinned by her heel. Rowan watched in approval."
    else:
        "In the span of seconds, she had Patricia lying on the ground, pinned by her heel. Rowan watched in awe."
    "Patricia winced. The heel was really digging into her breast. The squirming woman on the ground seemed so distant from the sarcastic but proper woman Rowan had come to know."
    "She’d made herself vulnerable for Rowan. And Ameraine was using every inch of that vulnerability."
    patr "Wait. Wait. Please wait. I wasn’t…"
    amer "What do you want?"
    "Patricia whimpered. Ameraine was applying more pressure."
    patr "..."
    patr "I want...I want him to fuck me."
    amer "Indeed. What else."
    "Her shock and confusion had given way to desperate panic. She wriggled helplessly, looking back and forth between the towering forms of Rowan and Ameraine."
    if avatar.corruption > 30:
        "A smirk slowly drifted on his face. Perhaps this could be fun for him as well."
    "It was time to jump in. If Ameraine was to be the pressing heel, Rowan needed to be the open hand."
    ro "Tell us, Patricia. You need to be open about what you want."
    ro "Then we can give you everything that you’re looking for."
    patr "E-everything?"
    amer "Everything."
    "Patricia forced her eyes closed. Her cheeks were flushed. No doubt the humiliation was beginning to mount."
    patr "I want...I want more."
    amer "Of this?"
    patr "Y-yes."
    "Ameraine lifted her heel up, then cruelly brought it back down in the same spot. Patricia cried out so loud that Rowan was worried others in the inn might hear."
    amer "What else?"
    patr "I want more...s-sexually."
    amer "When was the last time you truly felt pleasure?"
    "The dark woman finally let her heel of Patricia’s breast...only to glide it ever so slowly downward, brushing the tip of the heel over Patricia’s chest. Patricia’s eyelashes fluttered, and her right hand went to the side of her neck."
    patr "So long…"
    "She let out a loud groan as the heel reached between her legs."
    amer "Good. And we can provide you with that pleasure. But, only because you were open about what you wanted."
    "Ameraine turned back to Rowan."
    amer "Rowan, do you have any objections to fucking Patricia?"
    show rowan necklace happy behind black
    if avatar.corruption < 31:
        "Rowan faked a smile."
    else:
        "Rowan let out a laugh."
    ro "None whatsoever."
    "He needed no cue. His hand went to the bottom of his shirt and pulled it effortlessly over his head. Next, he moved to his belt."
    "Patricia’s attention was taken, finally, from the woman above her, to watch the show. Ameraine may have her down on the floor, but it was Rowan where her eyes settled."
    "As if in answer, Ameraine pulled her heel back. Patricia let out a groan in answer to its sudden absence."
    amer "What are you waiting for? Weren’t you the one who said you wanted more?"
    scene bg40 with fade
    show ameraine naked neutral at edgeleft with dissolve
    show rowan necklace aroused naked at midleft with dissolve
    #patricia aroused
    show patricia happy at midright with dissolve
    "Rowan could practically sense the heat rising from Patricia. A decade of sexual repression all coming out at once. Yet, she still hesitated. She just laid back, even without Ameraine’s foot keeping her down."
    "Rowan jumped in."
    ro "It’s okay. Really. This is just how Lady Ameraine plays."
    patr "I-I see. Quite aggressive."
    "Patricia laughed to herself."
    amer "I prefer the term interesting."
    #patricia naked
    "Rowan knelt down and helped Patricia with her clothes. Soon her garments graced the floor. Her eyes fell lower towards newly disrobed parts of Rowan. She bit her thumb, glance firmly placed on his cock."
    amer "It truly has been a while, hasn’t it?"
    "Patricia huffed, but otherwise didn’t reply. Instead, she pushed softly on Rowan’s muscular chest. An unmistakable message. Rowan laid back."
    amer "There we go. A little initiative."
    patr "Just because I’m rusty doesn’t make me a virgin."
    amer "Prove it."
    #cg 2
    scene cg583 with fade
    #patricia naked
    show patricia happy behind cg583 
    show rowan necklace aroused naked behind cg583 
    pause 3
    "Patricia moved above Rowan into a kneeling position. Her sex positioned itself mere inches from Rowan’s cock. The proximity alone was enough to make him stiffen. He could feel the heat and wetness even over the inches that still remained apart."
    ro "It’s okay, Patricia. Really."
    "Now, the movement began. Patricia brushed the lips of her pussy against the underside of Rowan’s manhood and began to grind. Nothing fast or frantic. Just the slow rubbing, the slow pressure, of body against body."
    "For Rowan, the sensation was most powerful on the sensitive underside of his cock. He could feel her lower lips and how wet they were. He could even feel the little stubbles of shaven hair from atop her pussy."
    "Patricia groaned out. Apparently, Rowan was not the only one who this felt good for."
    "Rowan rolled his hips. Despite the weight, he was still strong enough to set the rhythm. Patricia moved hers as well, matching his timing."
    "The two were not even yet fucking, and already the sensations began to mount in intensity. Their bodily reactions raised in visibility and in volume."
    "But, Ameraine did not seem quite as much a fan of this. She had retreated to her chair and watched with one hand supporting her chin. She was about to interject when Rowan shot her a look."
    "Her strategy of provocation had worked better than anticipated. But, what Patricia needed right now was time to get worked up."
    "Ameraine would not have to wait too long, however. Soon, Patricia was writhing and grinding. Rowan could feel how far she’d advanced by how lubricated the grinding was making his shaft."
    patr "I’m...I’m ready."
    #cg 2 - var 2
    #scene black with fade
    #patricia naked
    #show patricia happy behind black
    #show rowan necklace aroused naked behind black
    #show ameraine naked happy behind black
    "There was no challenge as Patricia lowered herself again, this time on to his cock. She was so wet that Rowan fit right in. The only challenge was the tightness. It was a pussy that had not been filled like this in a long time."
    "The effect was immediate though. With her sudden feeling of being filled and Rowan feeling cock pushed back upon by tightness, they both let out a low groan at the same time."
    "Patricia worked her hips up and down eagerly. There was some stiffness to her movement. But, she still had the muscle memory for what she had to do."
    "The force of Rowan’s upward thrusting proved strong enough to make her generous breasts flip. The sound of their bouncing joined the chorus of moans that grew from her lips."
    "Rowan grit his teeth. From this position, she controlled much of the pace, but he still threw his energy at working himself up. His chest rose and fell to mirror her body."
    patr "More..."
    "Ameraine watched the affair with dispassionate interest."
    "The movement of hips and bodies built and built. Patricia moaned out for the world to hear. Who cared if there was a pub right below. She had years of pent up energy to work out."
    patr "...More...More...More…"
    "Rowan found himself surprised by her energy. She pressed down on him harder and took him deeper with each new moment. The deeper he went, the more intense the rings of sensation."
    "Rowan’s eyes closed for a second and a groan slipped out. When they opened, the situation had changed."
    amer "Room for one more?"
    #cg 2 - var 3
    scene cg584 with fade
    #patricia naked
    show patricia happy behind cg584 
    show rowan necklace aroused naked behind cg584 
    show ameraine naked happy behind cg584 
    pause 3
    "Ameraine had taken up position kneeling behind Patricia. Her slender fingers roamed the naked woman’s body."
    "Patricia could only wordlessly nod in agreement. But, Ameraine did manage a sound from the other woman a moment later. Patricia squeaked at the top of her lungs when Ameraine’s fingers pinched down on Patricia’s nipples."
    "Now Rowan and Ameraine worked her from two angles. Rowan held her down by the hips and pounded her with every ounce of stamina. Ameraine brought her lips Patricia’s ears and whispered dark and erotic words."
    "The more Ameraine whispered, the more Ameraine toyed with her nipples, the more lost in the pleasure Patricia seemed."
    patr "More. More. More. M-more…"
    "Still, the more turned on Patricia got, the more erratic her movements became. From her position, she applied constant pleasure. Rowan was barely able to focus himself. Everything was swimming."
    "In a way, he became almost a prop in the proceedings. Patricia danced to Ameraine’s whispers."
    amer "You can’t resist dear. Let all your needs out."
    "The room suddenly filled with a long low groan. Even as out of it as he was, Rowan could tell what was happening. The spasming that replaced the thrusting. The juices running down the side of his cock. She was cumming."
    patr "I..fuck. I can’t control...Fuck."
    patr "...More…"
    "Ameraine’s nipples dug harder into Patricia’s nipples, earning a loud squeal. Still shaking, she hadn’t stopped moving her hips. She hadn’t stopped fucking him. The pleasure had reached so high he couldn’t speak."
    amer "No more barriers. No more lies."
    amer "Feeling what you want. Doing what you want. Taking what you want."
    amer "More..."
    patr "...More."
    "The pounding was nearing a pitch. Rowan’s groaning joined Patricia’s frantic sounds. At this pace, he wasn’t sure how much longer he could hold on."
    amer "Rising and rising..."
    patr "Y-yes…"
    "Rowan pumped wildly. His hands dug into Patricia’s hips. A sheen of sweat was forming on his chest."
    "Patricia’s body answered just as wildly. She pumped and bounced. Her body rolled into Ameraine’s."
    amer "One more...Almost there...."
    patr "M-m-more…"
    "Rowan saw white. A barrier was breaking. He couldn’t hold it anymore. He couldn’t hold it anymore."
    amer "And...cum."
    "And then it hit."
    "Patricia came first. This orgasm came even stronger than the one before. She screamed out and slumped forward, hands on Rowan’s chest. The force of it was so strong that it pushed away Ameraine’s hands."
    #cg 2 - var 4
    scene black with fade
    #patricia naked
    show patricia happy behind black
    show rowan necklace aroused naked behind black
    show ameraine naked happy behind black
    "But, Rowan came too hardly a second later. He held to her body for dear life as his cum spurted out. The tension lifted, and with it came a moment of bliss."
    ro "Fuck."
    "He started to soften slowly. The space of it gave room for hot white cum to drip from between her legs."
    "Rowan and Patricia panted in unison. Sweat covered their bodies. In that moment, their drifting eyes crossed paths."
    "Ameraine had already risen back to her feet, in the meantime."
    amer "Oh dear. We’re still not done. I hope you saved some energy. Because now it’s time for you to do something that will please me."
    patr "...Huh?"
    "Patricia’s eyelashes fluttered. Ameraine retreated to the table and returned holding an object familiar to Rowan. The silver and sapphire choker."
    amer "But, first. Would you be a dear and put this on for me?"
    "She placed the amulet into Patricia’s still shaking hand. Rowan himself was struggling to focus, and he knew why Ameraine was doing this. He could only guess at Patricia’s confusion."
    "Yet, the strange gem seemed to transfix the woman."
    patr "I...It’s so pretty…"
    "Eyes still fluttered, she brought the charm to her neck and did the clasp. Rowan almost thought he saw the central sapphire glitter."
    "Ameraine gave a pleased nod."
    amer "Good. Now let’s keep the fun going. I know you’re really going to love this next part."
    
else:
    show rowan necklace angry at midleft with dissolve
    "What was this woman doing? Rowan’s eyes narrowed. Ameraine had agreed to let him sway her. She was going to ruin everything."
    ro "That’s not something you just {i}say{/i}."
    amer "And yet, I did."
    "Rowan quietly balled his hand into a fist. A gesture he made sure the pale woman would note."
    ro "Would you mind excusing us for a time, My Lady?"
    ro "Your contribution has been most valuable, but I think Lady Crevette and I need some time together to discuss the plan. "
    show ameraine neutral at edgeleft with dissolve
    "Ameraine let out a small huff, thin arms crossing over her frame."
    amer "I wouldn’t dare intrude, of course. Fine. I have my own business to attend to. We’ll be seeing each other a good deal in the future, I suspect."
    "The two exchanged a terse goodbye. Patricia didn’t interject, but her eyes trailed Ameraine, all the way to the door."
    hide ameraine with moveoutleft
    "The noblewoman waited a few seconds after the door slammed before speaking."
    show patricia happy at midright with dissolve
    patr "Where did you even find that woman?"
    show rowan necklace neutral at midleft with dissolve
    "Rowan shrugged."
    ro "She was useful when I was setting up back in the capital. At times, she still is."
    show rowan necklace happy at midleft with dissolve
    ro "But, not quite so useful as she thinks she is. Not by a long shot. When dealing with her for an extended timeframe, it’s easy to grow weary."
    patr "Hmph."
    "The Lady went for the bottle of wine. A loud {i}pop{/i} reverberated off the room’s thick walls."
    patr "It’s good that she brought wine. I’d have grown even wearier of her, otherwise."
    "Soon, there were glasses of wine in front of both of their places. But, just as fast, the liquid disappeared into their lips. When it was done, Patricia went to Rowan’s bed to sit. She tested it playfully. No doubt she was used to more ostentatious arrangements."
    patr "Still. Is it true? We’d have to remove Werden ourselves?"
    "Feeling a bit more light headed, Rowan followed her to the bed. His fingers reached out to the strap of her dress and toyed with it."
    show rowan necklace neutral at midleft with dissolve
    ro "It’s not like I’m happy about it either."
    ro "But, you’ve always known that the man is likely to create problems. He’s too inflexible. Some peasant would ask for bread and he’d hang them. His rule would end in disaster."
    patr "-And would ours truly go much better?"
    "Rowan retreated back to the table and poured another pair of wine glasses for them."
    show rowan necklace happy at midleft with dissolve
    ro "I could tell you about it if you like."
    "Patricia nodded and took the offered glass from his hand."
    ro "An able administrator sitting at the helm, ensuring that the coffers are full, and the wheels of government keep turning. No debate, no whining sycophants to tell you no. {i}You{/i} get the last word. A thriving economy, a well run capital."
    ro "-And happy peasants too. They’d know they have a man in court who speaks for them."
    ro "No new demon war, either. I saw the Astarte first hand. I know the mistakes the commanders made. Were I in command, we’d never have lost."
    patr "Oh? Did the farm boy grow an ego all of a sudden?"
    "She took a greedy sip from her drink. Rowan’s eyebrow scrunched."
    show rowan necklace angry at midleft with dissolve
    #if deception is low - TO DO
        #ro "..."
    if avatar.corruption > 59:
        "She was just teasing him, but it was hard not to react with anger. How could anyone be so stupid as to think those preening Rosarian generals were a match for him?"
        "In fact, if the point of comparison was Astarte, he already had already proved it beyond a doubt..."
    ro "It’s the truth, Patricia. If we were in charge, Rosaria would be better run, better defended, and far more prosperous."
    show rowan necklace happy at midleft with dissolve
    ro "The two unthanked saviors of the realm. Its unrewarded savior and marginalized steward. Think what we could do."
    if avatar.corruption > 59:
        show rowan necklace aroused at midleft with dissolve
        #show patricia aroused at midright with dissolve
        "Rowan punctuated his words with a long drawn out kiss. An indication that the time for careful consideration was over."
    else:
        show rowan necklace concerned at midleft with dissolve
        "Rowan had to pause for a moment to collect himself. Patricia was slumped back in her chair, chewing over his words."
        "The impulse to act had come to him. This was the perfect moment to make his move, while she was thinking of the two of them together."
        "Yet, something held Rowan back. A vague sense of a line being crossed. It became almost a physical thing. Like to cross it would take real physical exertion."
        "But, Rowan had long ago settled on his course of action. Such waning scruples did not hold for long."
        show rowan necklace aroused at midleft with dissolve
        #show patricia aroused at midright with dissolve
        "So, right as the lady moved to answer him, Rowan bent low and kissed her."
    "Her lips tasted still of the wine. Rowan was sure his did as well."
    "The noblewoman let out a moan of assent and opened her mouth to give Rowan full access. Soon, their hands were exploring each other’s bodies as eagerly as their tongues were."
    "Rowan pushed her backwards on the bed. She let out a little giggle, but otherwise responded by stretching out on the bed. Miraculously, she held tight to her wine. She didn’t spill a drop."
    #show patricia naked at midright with dissolve
    "Of course, her clothes would have to go. Her giggle turned to a groan as Rowan pulled away her dress."
    patr "You had yet to see me naked."
    ro "A mistake."
    "A single of her short fingers went to his chest and teasingly traced a circle."
    patr "...One that must be answered by punishment?"
    #rowan naked smirk
    show rowan necklace happy at midleft with dissolve
    if avatar.corruption > 59:
        "Rowan flashed a shadowed smirk. A fun idea was coming to him. One he never would have imagined in the past."
        "Who said you couldn’t mix business and pleasure?"
    else:
        "Rowan had to take a second to collect his thoughts. This seduction game often felt like entering a duel with another person’s sword. The balance was all wrong."
        "But, slowly the genesis of an idea came to him."
    ro "Stand up straight for me, Patricia."
    "There was a hint of hesitation. Some searching for a motive behind Rowan’s eyes. But, the curious noblewoman eventually worked her way off the bed. She took up a pose with her hips cocked and her arms crossed over her chest."
    #patricia naked happy
    patr "Like this?"
    "Rowan leaned back, adopting the mannerisms of a self assured patrician. Or at least, as close to it as he could approximate."
    ro "“Like this, M’lord?” Try it like that."
    "Patricia gave a small roll of her eyes."
    patr "Like this, My Lord?"
    ro "Hrm. No, not quite."
    ro "You’ve seen servants your whole life. You can’t truly say you don’t know what it looks like when they stand at attention."
    ro "Back straight, hands to the side, looking straight ahead."
    patr "It is not as though I’ve been taking notes, Rowan."
    "Next, she tried to adopt the pose Rowan described. Certainly, her back straightened out. With the curves of her frame, it had the effect of prominently displaying her large and exposed breasts."
    patr "Do I have it now?"
    ro "Uh uh uh. You’re forgetting something."
    "She rolled her eyes again. But, from the way her lips twisted to a wicked little grin, Rowan suspected she was starting to enjoy this."
    "She called out in a sing-song voice. Almost an approximation of the dainty tone a female servant was often expected to take."
    patr "Do I have it correctly {i}now{/i}, M’lord?"
    "He openly scrolled his gaze up and down her body. To emphasize the point, he even made a show of tilting his head, as though he were an appraiser at the market."
    ro "Better."
    ro "Now then, be a good girl and bring me some wine. A certain greedy guest has been drinking up most of it."
    "Without a word of complaint, she grabbed up both of their goblets and sashayed back to the table. The way she swayed her rear as she walked had unmistakeable connotations."
    "He watched in silence as she poured his goblet full. But, when she tried to top off hers, Rowan interjected."
    ro "What are you doing? Do servants normally drink with the lords when commanded to bring wine?"
    "She blinked twice, as if trying to process words that didn’t make sense. Then came an answer, paired with a sigh of relief."
    patr "Of course not, M’lord."
    ro "If you ask nicely, I might be generous enough to share."
    #cg1
    scene cg700 with fade
    show rowan necklace happy behind cg700
    #patricia naked happy
    show patricia happy behind cg700
    pause 3
    "She returned, posture a little straighter this time, and held out the goblet to him. But, now it was her turn to surprise him. She sank down to her knees, head lowered, and held up the goblet."
    patr "Would M’lord please be so kind as to spare a humble servant some wine?"
    if avatar.corruption > 59:
        ro "Heh."
    else:
        ro "..."
    ro "Just a sip."
    #cg1 - var 2
    scene cg701 with fade
    show rowan necklace happy behind cg701
    #patricia naked happy
    show patricia happy behind cg701
    pause 3
    "Rowan tipped his goblet forward to her, hand still firmly on the base. It was not for her to hold. She brought her head low to the edge of the cup, and sipped from it."
    if avatar.corruption > 59:
        "Naturally, this was too good an opportunity to pass up. A cruel smile framed his face as he suddenly tilted the goblet, sending a surprising amount of wine forward."
        "She coughed from the surprise, red wine trailing down her lips over her bare breasts."
    "But before she could get too greedy, Rowan took it back. Patricia was forced to watch as her lowborn companion drained the only cup of wine."
    scene bg40 with fade
    #rowan smirk
    show rowan necklace happy at midleft with dissolve
    #patricia naked aroused
    show patricia happy at midright with dissolve
    "When he finished, he rose to his feet. Even when she wasn’t on her knees, he towered over her. To emphasize the disparity, he gracefully gripped her chin and tilted it upwards with the slightest touch of force."
    ro "The hair is wrong. Too neat. Servants don’t get their hair dressed up fancy like."
    "His hand rifled through her neatly styled hair and undid the delicate bonds hold it together. Long hair tumbled down her hair in an undignified display."
    ro "Hrmm. I should have prepared a serving girls uniform for you, shouldn’t I?"
    ro "Something to show you off."
    ro "It’s not too late though. I can grab a peasant’s rags from downstairs and send you into town to fetch more proper attire."
    #patricia naked shocked
    show patricia shocked at midright with dissolve
    "That final implication earned a shocked gasp and outraged expression. She reached out and gave him a light smack."
    patr "Rowan! I would be seen! Even as a game, that’s over the line!"
    show rowan necklace angry at midleft with dissolve
    "Rowan laughed to himself. But, inside he was a brooding stormcloud. She’d just shown some defiance. If he didn’t act fast, she might break the scene he was setting."
    "What would Andras do here? For all his faults, that man knew how to project confidence. The answer was obvious, the demon would likely use sudden aggression as a chance to regain control over the situation."
    "That’s what Rowan did. Keeping a silly grin on his face to ensure it came across as playful, he reached down to her exposed bosom and twisted her nipple."
    ro "That’s My Lord to you, still. You gotta remember it."
    #patricia naked aroused
    patr " Mmf."
    "Patricia let out a low sound, halfway between a squeak and a moan. She peered up, over the tangles of her released hair, meeting Rowan’s eyes with an unforeseen intensity."
    patr "How else should I serve you, M’lord?"
    "Her voice came sultry and low. Naturally, to pair with it, came a subtle movement of her tongue against her lips."
    #rowan smirk
    show rowan necklace happy at midleft with dissolve
    "Rowan released her nipple and marched back to the table and his chair. Freed from his hand, she let out a drawn out pant."
    ro "Pour me some more wine...then service me while I eat."
    patr "Service?"
    "Casually, he reached down to his breeches and undid the front."
    ro "Service."
    #cg2
    scene cg702 with fade
    pause 2
    show cg703 with dissolve
    #rowan smirk
    show rowan necklace happy behind cg703
    #patricia naked aroused
    show patricia happy behind cg703
    pause 2
    "Soon, Rowan was leaning back at the table, taking his time to enjoy the fine wine. Patricia was also engaged in a tasting of a different sort."
    "He had her naked, under the table, with one hand and her lips wrapped around his cock. Her tongue slowly danced up and down the sensitive underside. It was the work of an experienced woman, albeit one whose technique had some rust. "
    "She took it slow, drawing out the sensation. Rowan tried his best not to let the sensation eke out a sound from him, although here and there he couldn’t stop himself from grunting."
    "After some time, he used her sweeping undone hair as a handle, and tilted it just enough so that she’d look him straight in the eyes. A perfect vantage point to see her face contort around his manhood."
    ro "Wipe it totally spotless now. What good is a servant who can’t clean?"
    "As much as her posture would allow, she gave an eager nod. But, when she went back to work, the lesson of his prior action had been learned. She kept her eyes up, trained on him. Even as her head started to pump faster, she never broke eye contact."
    patr "Totally clean, M’lord. Every inch…"
    #cg2 - var 2
    show cg704 with dissolve
    #rowan smirk
    show rowan necklace happy behind cg704
    #patricia naked aroused
    show patricia happy behind cg704
    pause 3
    "She broke from the task, but didn’t avert her glance. A mess of her saliva remained as a trail for her lips to his stiff cock."
    patr "Please...more…"
    "In some ways, this was an act of rebellion. He hadn’t told her to stop, after all. Yet, he couldn’t deny it. He wanted more too."
    ro "Such a haughty servant, asking for such things."
    #cg3
    scene cg705 with fade
    #rowan smirk
    show rowan necklace happy behind cg705
    #patricia naked aroused
    show patricia happy behind cg705
    pause 3
    "With a hand in her hair, he pulled her roughly back to her feet. But, she would not remain there for long. Next, he slammed her down, although careful not to truly harm her, against the surface of the table."
    "Patricia’s mouth widened into a long gasp the entire time. Force to the table, she clutched at it with her nails. Almost certainly, the wood was already scratched."
    patr "Ah. You’re right. So haughty. Fuck. Need to be...taught a lesson."
    patr "...Been so long..."
    "His eyes trailed her body. The wiggle of her hips was unmistakable."
    "His own hand trailed back to his cock, fingertips running over the saliva coated length of it. Certainly, if nothing else, he was quite lubricated."
    "It made it much easier when he began to work himself into her ass, tip first."
    patr "There!? But, I haven’t in so-"
    #cg3 - var 2
    scene cg706 with fade
    #rowan smirk
    show rowan necklace happy behind cg706
    #patricia naked aroused
    show patricia happy behind cg706
    pause 3
    "He silenced her with another rough tug of her hair."
    ro "Who said you could complain? "
    ro "Servants do whatever…"
    ro "I…"
    ro "Want."
    "The only answer she could give was a moan. As it finished, she pressed her face down against the table and repositioned to better fit his length."
    show cg706 with sshake
    show patsex1 with fade
    "His cock descended into her slowly. It was as though each segment of his length was its own little struggle. Each time, her asshole would inevitably lose, ceding more and more room to him. The shivering of her body grew and grew."
    "Then, fully submerged, into her, Rowan began to move. He didn’t give her long to adapt before picking up the pace. After all, she was supposed to be the one serving him here, wasn’t she?"
    patr "Fuck. I haven’t felt...Fuck...Solansia above…"
    "Her body slammed forward and back against the table, large breasts being shoved around uncontrollably. The harder he fucked her, the higher the pitch of her voice went."
    ro "Thank...Your...Lord…."
    patr "Th-thank you...M’l-"
    "She threw her head back and howled out a long grown. There was something really reactive to her. Most women were not so animated during sex…"
    "..Though, most of the time it wasn’t their ass being fucked either."
    patr "M’lord…"
    "Rowan grunted. She was tight. So tight that even moving was difficult. But, that just added to the enjoyment. The more her body made him work, the more pleasure he eke’d from her."
    patr "M’lord…"
    "The noblewoman seemed to melt beneath him. Her legs grew so shaky that it was only the table keeping her up. Her face twisted to the side, and Rowan was greeted with wide open eyes, a gasping open mouth, and a face redder than he’d ever seen her with."
    patr "M-M’lord!"
    "Awareness of the situation fluttered in and out. At times, he was so concentrated on the tense growing pleasure that he lost track of what he was doing. That a high noblewoman of the realm was knowingly letting him fuck her ass, roles reversed."
    "When awareness of it returned, it came with a rush. He spontaneously gave her untidy hair another hard tug, just because he could."
    patr "M’LORD!"
    ro "What are you, slut?"
    patr "S-servant. Servant. Ahh."
    show patsex2 with fade
    pause 3
    "He sped up once more. Throwing his hips into it with his considerable strength. In answer, the cries from her lips only grew more desperate. It was as though she were an instrument to be played."
    patr "Fuck fuck. M’LORD! M’LORD! So fast...I can’t...I can’t…"
    #cg3 - var 3
    show cg714 with sshake
    show cg714 with sshake
    show cg715 with flash
    pause 2
    "One final push. He used his largest reserve of energy to speed up still further, pounding with the single minded goal of finishing himself off."
    "It was not not a difficult task. There was but a mere moment before a long grunt fled his lips...and hot white seed fled his manhood."
    "Staggering back, a little bit of cum dripped from Patricia’s rear. The woman was slumped over the table, eyes flicking lightly."
    scene bg40 with fade
    show rowan necklace aroused at midleft with dissolve
    #patricia naked aroused
    show patricia happy at midright with dissolve
    patr "With all that...all that screaming, the people downstairs must think there is actually a lord here."
    "Rowan laughed to himself. His arms clutched at the wall to aid him in the act of catching his breath."
    ro "Perhaps there is. There is a lady, after all."
    "Patricia blinked twice, as if he said something strange. Then her eyes lit up with comprehension."
    patr "Oh yeah!"
    "But, as that reminder came back to Lady Crevette, something different came back to Rowan. His true task."
    "Still staggering, he withdrew back to his satchel and pulled from it an object. A jeweled silver choker lined with glittering blue sapphires."
    patr "You know, as much fun as that was. Said...activity...is not known for bringing ladies their own orgasm."
    ro "You wound me. We’re not exactly done yet."
    "He returned to her, eyes still examining the strange wonder of the choker. Would it really do what Ameraine had said?"
    ro "But, before I continue, would you be so kind as to tilt up your neck?"
    patr "Hm?"
    "He gave her his best confident smirk."
    ro "Your “Lord” has a gift for you."
    scene black with fade
    #patricia naked aroused
    show patricia happy behind black
    patr "It’s lovely..."


#cg 3 
scene cg585 with fade
#patricia naked
show patricia happy behind cg585
show rowan necklace aroused naked behind cg585
show ameraine naked happy behind cg585
pause 3

"It was dark out now. The games had only progressed. Patricia’s form took up the center of the room. Rowan had bound her with rope that kept her wrists and feet. It forced her into an awkward, bent forward position."
"The short woman squirmed helplessly in her bonds. Her mouth was frozen open in a gasp."

patr "It’s really been a long time since I tried something of this sort…"

if ameraineCharm == True:
    "Ameraine giggled playfully. Rowan watched from a nearby chair."
    amer "You’re not new to being tied up?"
    patr "A suitor of mine was quite good at it."
    amer "What a challenge. Still, I think what I have planned next might be a little bit different from anything you may have tried before."
    amer "Aran-Uch-Ah."

else:
    patr "...I don’t think the last guy was quite so good at this. You really know how to tie a knot."
    "She squirmed weakly in her bonds. Though, Rowan had made extra sure there was no chance of escape."
    patr "What do you have planned for me now...M’lord?"
    "He put a hand to his chin."
    ro "I think...I think something a little different."
    ro "Aran-Uch-Ah."

show black with blueflash

"The moment she said it, there was no doubt that the magic had been effective. The room flashed with brilliant blue light. Rowan had to shield his eyes to prevent himself from being blinded."

if ameraineCharm == True:
    ro "You didn’t tell me this would happen."
    amer "Had I known, I would have told you."
    patr "I feel...strange..."
    
else:
    "Rowan grit his teeth. Accursed Ameraine. Had she given him prior warning of this effect, it would have saved his eyes a great deal of strain."
    patr "I feel...strange..."

#CG 3 - var 2
scene black with fade
#patricia naked
show patricia happy behind black
show rowan necklace aroused naked behind black
show ameraine naked happy behind black

"The room dimmed once more to the point where Rowan could see again. Patricia was still in place. But, the charm was emitting bright blue light. But, it wasn’t just the object that was affected. The same strange light now shone from Patricia’s eyes."

if ameraineCharm == True:
    "Rowan and Ameraine exchanged glances. The process appeared to have worked."

else:
    "Rowan nodded slowly to himself. Whatever the process of the amulet was, it appeared to have been effective."
    
ro "Patricia. You said you wanted to be true to your desires right? That’s what you want."
    
patr "Yes…..Yes."

"Rowan narrowed his eyebrows. It was supposed to be as simple as finding this “soul wan”t of hers and employing it."

ro "Why did you come here tonight?"

patr "To fuck you."

"She answered in a strange monotone. Present, yet without thought or crafting to her answers."

if ameraineCharm == True:
    "Ameraine motioned Rowan forward. The indication was clear."

else:
    "This was all uncertain ground, of course. But, considering her answer, some extra stimulation might help along the process. "

#CG 3 - var 3
scene black with fade
#patricia naked
show patricia happy behind black
show rowan necklace aroused naked behind black
show ameraine naked happy behind black

"He stepped behind her and ran his hands up and down her side. One of his fingers brushed over her nipples. Clearly, the charm didn’t block arousal. She let out an involuntary moan at the touch."

if rowanCharm == True:
    "Along the way, he noticed a small bruise formed near her nipple. No doubt the consequence of a bit of manhandling he’d given her body earlier."

ro "Why else?"

patr "Because...because I was curious about what you told me before. A coup within a coup. I wanted to know more."
    
ro "Why did you want to know more?"

"He planted delicate butterfly kisses all along her neck. She tilted to the side to allow him greater access."

patr "Because I want it all. I want what I am owed."

ro "What are you owed?"

"His right hand trailed all the way down, making for the place between her legs. Still quite wet, of course. She was freshly fucked Not even her inner walls offered much resistance."

patr "Power. Respect."

"He took two fingers to pump into her, just as his cock had done earlier. Patricia’s unthinking words were punctuated with intermittent groans and gasps."

patr "I am the smartest. "

"Her leg spasmed. As unreactive as her words were, her body was pliant in his hands."

patr "I am the hardest working."

"His fingers beckoned her forward. A gasp escaped her lips. Then the flood. She let out a soft cry and shook in his hands."
"She sunk into her bonds for only a few seconds. Then her lips started to move again, as though she had not just cum."

patr "I d-deserve to rule and be treated as a ruler. I want more."
patr "I want to be seen as beautiful. I want to be seen as someone to pay heed to."
patr "I want what I am owed."

"Rowan brought his lips to her ear. His hand continued to work her sex. Her body seemed to twitch and shiver with each pump of his fingers."

ro "But, Marianne and the current order will not give you what you are owed?"

patr "They won’t. No."

ro "And Werden won’t give you what you are owed either, will he? Oh, he’ll give you some of it, but if you ask for the rest he won’t listen."

patr "..."

"Rowan waited. This was a key moment. If she admitted this, then her want could perhaps be directed."

patr "Yes. He won’t give me what I’m owed."
patr "I..."

"Before she could continue, another orgasm wrapped through her. It made her head roll back and her knees shake. Only the ropes were keeping her on her feet."

patr "Ah..."

if ameraineCharm == True:
    "Ameraine rushed forward and tilted her head up by her chin. She wanted a turn. Rowan’s ally met the possessed woman, eye to eye."
    amer "But, what if there was someone who could give you what you were owed? Everything you want."
    patr "There is…?"
    "A low groan rolled from her lips. Rowan had set to work once more. Patricia was drowning in pleasure."
    patr "You?"
    "Ameraine smirked."
    amer "No. There are ways we can help you. And will."
    amer "But, a higher power exists. One who wants to see you get everything that you are owed."
    "She brushed the tips of her nails down the side of Patricia’s cheek. Their tips were sharp enough to leave a small cut in their wake."
    amer "With such powerful allies, there is no doubt that you will get what you want. You will have it all and more."
    patr "All and more…"
    "Rowan pulled his hand back and shifted to clit rubbing. Soft flicks that elicited a gasp every time. Her body radiated with heat."
    patr "Who…"
    amer "The Demon Twins. Andras and Jezera."
    patr "Demon twins…"
    "Suddenly, Patricia struggled in her bonds. Rowan pulled his hand back briefly, giving her room to move."
    patr "But...enemy...evil…"
    patr "You...you work for demons. This entire time. You…"
    "Ameraine shushed Patrica with a finger atop her lips."
    amer "Of course, we work for demons, my dear. They give us what we are owed. It’s good to work for people who give you what you are owed, right?"
    patr "..."
    "The struggling stopped. Now that she was back under control, Rowan went back to work teasing her exhausted pussy."
    amer "Do the human lords give you what you are owed? Marianne? Werden?"
    patr "N-no."
    "Even in her dreamlike state, her voice came out shaky. It was like a core pillar of her identity being challenged."
    amer "And you want what you are owed, don’t you? It’s what you want most?"
    patr "Y-yes."
    amer "So why serve them?"
    patr "I…"
    "She groaned loudly and thrust her rear backwards towards Rowan. Once more her words and her body fell totally out of sync."
    patr "Demons are evil."
    amer "Is it evil to want what you are owed?"
    patr "No."
    amer "Are not people who lie and don’t give out fair due evil?"
    patr "Yes."
    amer "So if the human leaders are evil, why is it evil to serve the demons? They give you what you are owed?"
    patr "I don’t know."
    "Rowan felt her movements grow faster once more. Another orgasm was rising. It must have been her tenth in the past few hours alone. It showed in her body. Her skin glistened with sweat, and her legs were so weak that without the rope it looked like she’d fall over."
    amer "This can be very easy, Patricia. Very easy. Agree to the deal. You serve Andras and Jezera...and you get what you are owed."
    "She squirmed slightly once more. Nothing like the way she’d tried to escape her bonds when talking of demons first came up. But, even in this state, there was still a part of her trying to escape the direction everyone saw it heading."
    "Rowan used this chance to jump in once more."

else:
    "Rowan tilted her head back, so he could work in a trial of kissing and nibbling along the sensitive side of her neck."
    ro "Are you owed pleasure?"
    patr "Yesss."
    ro "So there is someone out there who gives you what you’re owed, right?"
    "She remained silent, except soft moans and whimpers. His words had gone through, but in her spacey state, she didn’t seem to have even fully processed them."
    ro "Not only that. Someone who helps you and stands by your side. Someone who gives you good advice."
    ro "Someone who sees you as beautiful."
    "He glided a hand between her legs. He made sure that she could feel the electric tingle of his fingertips brushing over her clit."
    ro "Smart."
    "More and more. Each new way he teased her was bolder than the last."
    ro "Capable."
    patr "Y-yes…"
    "Her voice cracked. Whether the successive pressure of having her body worked or his words, the facade of resistance was crumbling."
    ro "Who?"
    patr "You."
    ro "So there is one person in the world who sees how valuable you really are, and wishes to give you what you’re owed. Someone whose word is the truth."
    "He breathed his words like whispers into her ear. It was a strange act. The kind of silly thing he’d seen Jezera attempt on more than one occasion. Yet, he could see why she favored it. It was shockingly effective."
    patr "Yessss."
    ro "So if I promised you more...If I promised you everything you were owed could come from my hand, then you would trust me?"
    patr "Everything?"
    "Rowan knew what he was going to say. He had not fully considered it. Yet, now that he found himself here, in this moment, there was no need to make a choice at all."
    "He knew who he should transfer her loyalty to..."
    ro "Everything. But, you need to make a promise. You need to swear to serve me. To obey me. To act as I tell you."
    patr "...obey…?"
    "Rowan flashed a dark smirk. Not the twins. Him. A servant of his own, disguised as one of theirs."
    ro "That’s right. Swear to serve me, and you will have everything you’re owed."
    patr "...Everything...How?"
    "The sound rang with the soft wet sound of fingers pumping in and out of a woman. The more intense the moment got, the more intense his ministrations."
    "There was no use holding back anymore. If she wasn’t far enough along now, she never would be ready to be told the truth."
    ro "It’s simple. I’ve made a deal with the demons for control of the city. When all is done, I will ensure that you are made the new governor."
    patr "D-demons!? "
    "She started blinking and lightly squirming in the bonds. As if trying to rebel against his words. Yet, it wasn’t an especially strong escape either."
    patr "...Enemy...Evil…"
    ro "But, am I your enemy?"
    "A pause, and when her answer came it was already noticeably less sure."
    patr "...No…"
    ro "Yes. There are demon twins. You must pretend to serve them. But it is just a farce."
    ro "But, I am not a demon, nor do I trust them. You would serve me. I would ensure you always got what you are owed. And you can trust me, right?"
    "Her answer came this time in a whimper, tinged as much with lust as anything else."
    patr " ..Trust...Rowan..."

ro "It’s easy, Patricia. I’ve made the deal. They give me everything I want."
ro "You just have to say yes."

"To punctuate his words, he gave her clit a series of faster flicks. In her state of intense arousal, more than enough to bring her over."
"There were no more juices when she came this time. Only a series of shivers that ran the entire length of her spine and a soundless cry. When it settled she swayed in place. Her sense of balance was gone. Only Rowan was holding her up."

patr "I...Demons..."

if ameraineCharm == True:
    amer "One more I think."
    "Rowan didn’t argue."

else:
    ro "Demons who think you serve them. But, you don’t truly. You serve me. I give you what you are owed. I give you what you’ve always wanted."
    patr "...Rowan…demons…"
    "Her protestations grew more subdued by the moment. Rowan was winning and he knew it."
    ro "Do the lords of Rosara give you what you are owed? What are you longing for?"
    patr "No. No."
    ro "Only I do. Right?"
    "She nodded slowly."
    ro "You can trust me. It’s so easy. Simply swear to serve me. Demons don’t matter. The nobles don’t matter. Only what you are owed. And who can give you what you are owed."
    patr "...Rowan…"

"His fingers kept at their current pace of attack. In the after-glow of orgasm, it was easy to get her worked up again. Soon, Rowan had extracted another from her."
"Her head hung limply. Her lungs sucked in air, chest rising and falling in large movements."

if ameraineCharm == True:
    amer "Will you serve Andras and Jezera? In return, everything you are owed will be yours."
    patr "..."
    "Rowan readied his fingers. He’d make her cum however times it took."
    patr "Everything?"
    amer "Everything."
    amer "You simply have to say yes."
    patr "..."
    "She took in a breath. Her head still hung low."
    patr "Yes."
    amer "Yes, you’ll serve Andras and Jezera?"
    patr "Yes."
    "Rowan drew his hand back. Without thinking he took a step back. All the energy seemed to leave him. After all this work, they’d done it. They’d brought her over to their side."
    if avatar.corruption < 31:
        "It left a knot in his stomach."
    elif avatar.corruption > 60:
        "Rowan smiled openly. It had been hard work, but well worth it. He’d never corrupted someone this way before."
    else:
        "Was it wrong that he wanted to celebrate?"
    amer "Whatever it is they tell you to do?"
    patr "Anything. Just...more…"
    "Ameraine pulled back and sat down at the table. She crossed both her arms and her legs. She looked happy, of course, but her reaction was not quite as extreme as Rowan’s."
    amer "Swear it. Here and now."
    patr "I swear it. I will...serve Jezera and Andras...if they give me what I am owed."
    amer "Then it’s a deal."
    scene black with blueflash
    "Ameraine snapped. Once more the room filled with blue light. Rowan didn’t have time to prepare and caught a full burst in his eyes. Everything was bright blue."
    "When vision returned to him, Ameraine was back on her feet. But, Patricia wasn’t. Ameraine had cut the rope, and now the smaller woman’s form lay crumpled on the ground."
    "The blue light was gone now. The sun had long since set and the room had gone dark."
    scene bg40 with fade
    show rowan necklace neutral naked at midleft with dissolve
    show ameraine naked happy at edgeleft with dissolve
    #show patricia naked neutral
    show patricia neutral at midright with dissolve
    ro "It’s done?"
    amer "Ask her."

else:
    patr "Serve...Rowan…"
    patr "Rowan...give...owed…"
    "He rolled her head backwards. Her lips came to rest inches from hers. So, between his whispered words, he slipped kiss after kiss on to her hungry lips."
    ro "Then you agree? You will serve me? You will let me give you what you are owed?"
    patr "...Yes…"
    "He planted another long kiss. It left her panting for more."
    ro "You swear?"
    patr "I swear...to serve...you…"
    ro "No matter what? Even if you must pretend to serve the demons? Even if you must do anything that I ask you?"
    "A long shiver ran up her spine, focused at the points of contact between their bodies. Something had changed between them, and it was clear just from the contact of forms."
    patr "..Anything...Demons...Anything…"
    "He closed his eyes."
    if avatar.corruption > 59:
        "Conquest. Sweet conquest. This was a feeling he could get used to…"
    else:
        "He’d done it. He’d corrupted a woman to him through dark magic." 
        "It was all for the greater good, yet Rowan had trouble keeping personal emotions from it. Was it shame he was feeling? The thrill of victory? Or the wickedness of a taboo falling down? If you’d asked him, he wouldn’t be able to answer."
    ro "Then it’s a deal."
    "Rowan snapped his fingers...and once more the room flashed in a bright, all encompassing blue."
    show black with blueflash
    "He staggered backwards, blinded by the brilliant light. His new servant was left to free hang from her bonds." 
    "She was still there even as his vision returned to him. Panting and staring off blankly. Albeit, now with the glow no longer emitting eerily from her eyes. He drew a dagger and gently eased her from her bonds."



"Rowan looked down. Patricia may have been barely able to stay up, but her eyes were open and aware. Rowan knelt down and placed a hand on her shoulder."

ro "Do you understand what just happened?"

if ameraineCharm == True:
    patr "I just swore...to serve the demons…"

else:
    "Patricia slowly rose...only, not to her feet. She paused on her knees, hands spread out in a posture of reverence and head hanging low. She was bowing to him."
    patr "I serve you, Rowan. With all my heart and my soul. I made a deal…"
    "She looked down to her hands, blinking."
    patr "And you are...in league with demons...who I must pretend serve...?"
    "It was a strange sight, watching someone rationalize the irrational. Rowan half expected her to panic or lose her cool, yet Patricia remained mostly calm. Almost as if they’d come to an agreement of a more normal variety."

patr "Were you planning that all along, Rowan…?"

"Rowan nodded softly."

ro "I am sorry that deception was required. It wouldn’t have worked if you hadn’t trusted me. Most are not willing to serve demons."

if ameraineCharm == True:
    "With Rowan’s help, Patricia slowly worked her way back up to her feet. Her arms and legs were still shaking from the aftershocks of so many orgasms. Her eyes trailed a lazy arc between Rowan and Ameraine."

else:
    "With Rowan’s help, Patricia slowly worked her way back up to her feet. Her arms and legs were still shaking from the aftershocks of so many orgasms."

patr "So, we’re killing the Duke and handing the city over to the demons. Do we have a plan…?"

if ameraineCharm == True:
    "Rowan and Ameraine exchanged a look. Patricia had said it so casually."
    "Patricia and Ameraine remained in Rowan’s room until well into the night. Most of it was spent bringing Patricia up to dates on the specifics of the plan. Though, not without breaks for other activities."
    $ change_base_stat('c', 10)
else:
    ro "Indeed we do. And you’re going to be the central star."
    "He tilted up her chin, so she could look him in the eyes. An easy sigh escaped her."
    ro "And when it’s all over, everything you’ve ever dreamed will be in your hands. You will be the ruler of all of Rastedel."
    $ change_base_stat('c', 15)

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return