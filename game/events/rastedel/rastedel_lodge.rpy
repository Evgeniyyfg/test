label rastLodge:

if lodgeFirstVisit == True and eleaConvo == False and juliConvo == True:
    scene bg33 with fade
    show rowan necklace neutral at midleft with dissolve
    "Rowan approached the front gate of the Grand Camellia Lodge cautiously. The tall stone structure stood in the Southwest of town, not far from the palace. It was a popular hangout spot for nobles. A place where many of the important decisions of the realm were made."
    "A place he’d normally never be welcome."
    "He looked on at the gates with a hand to his chin. It would be valuable place to gather information, but the guards at the gate didn’t seem inclined to let just anyone through. It seemed that the entire effort had been wasted."
    "Only, as he turned to leave, a familiar face passed him by."
    show juliet shocked at midright with dissolve
    juli "Rowan!"
    show juliet neutral at midright with dissolve
    juli "I had not expected to see you in the capital again so soon. I heard news of your departure."
    "Rowan smiled softly. The moment she caught his eyes, her gaze averted. It seemed not much had changed since the ball."
    show rowan necklace happy at midleft with dissolve
    ro "Quite reasonable, my lady. I only returned for the day just to look about. I’ll be back in the field soon."
    juli "You will?"
    juli "Everyone here speaks of you and your resolve. Your name gives solace whenever the topic of the conflict in the south comes up."
    juli "I will add a private prayer at weekly services for your return unharmed."
    "Rowan nodded somberly."
    ro "That’s quite kind of you, My Lady. Even knowing there are people here who wish for my safe return will make sure I don’t risk too much."
    ro "Apparently Rastedel isn’t done with my ugly face."
    juli "I wouldn’t call it ugly…"
    #show juliet confused
    juli "I suppose you’re here to get into the lodge? You’d need entry papers or a house signet ring to do that. Perhaps I could…"
    "Rowan’s heart briefly rose. Perhaps he would get some valuable information after all…"
    juli "No no. Father will know if I bring someone in. It would be best for him not to get any wrong impressions…"
    #show juli sad/embarassed
    "From what Rowan had heard, there was nothing the nobles loved to do more than talk. Even speaking together in front of the building would no doubt would have some kind of social ramifications."
    ro "I understand. If you’re worried about displeasing your father, then you can only imagine how I feel."
    "He chuckled."
    ro "I wouldn’t belong in there anyway. It’s above my station. I’ll let you go on with your day my lady."
    juli "Of course. I will no doubt see you soon."
    "An interesting conversation. It was good to have friends in the capital. The daughter of the Duke of Werden himself no less. Still, he’d probably have to break it to her that he was a married man soon."
    $ lodgeFirstVisit = False
    jump rastMenu
    
elif lodgeFirstVisit == True and eleaConvo == True:
    jump delaneLodgeSex

elif werdenCoup == True and werdenCoupTalk == False:
    jump werdenCoup

elif rastAlly == "werden" and werdenAbbeyPlan == False:
    jump lodgePostPathWerden
    
elif rastAlly == "crevette" and patriciaAbbeyPlan == False:
    jump lodgePostPathPatricia

elif rastActFour == True:
    jump act4Menu

elif lodgeFirstMeetings == True and rastForkingPaths == False:
    jump lodgeRepeatVisit

elif rastActThree == True:
    jump lodgeVisit


else:
    scene bg33 with fade
    show rowan necklace neutral at midleft with dissolve
    "Rowan approached the front gate of the Grand Camellia Lodge cautiously. The tall stone structure stood in the Southwest of town, not far from the palace. It was a popular hangout spot for nobles. A place where many of the important decisions of the realm were made."
    "A place he’d normally never be welcome."
    "Rowan’s short visit didn’t last long. He hadn’t been allowed in last time, and he wouldn’t be allowed in this time either. His only hope was that Duke Raeve was gathering useful intelligence there."
    jump rastMenu
    
    
label delaneLodgeSex:

"Rowan approached the front gate of the Grand Camellia Lodge cautiously. The tall stone structure stood in the Southwest of town, not far from the palace. It was a popular hangout spot for nobles. A place where many of the important decisions of the realm were made."
"A place he’d normally never be welcome."
"He approached the outside, where a pair of men-at-arms whose surcoats displayed noble sigils manned the doors."

show rosarian knight neutral behind bg33

rkn "Got a permit of entry? Got a sigil ring?"

"Rowan frowned softly. That might be a problem. He didn’t have either."

show eleanor dress neutral behind bg33

ele "No. But, he’s a guest."

hide eleanor
show eleanor dress happy at midright with dissolve

"Rowan turned around to see Lady Delane standing behind him, arms folded behind her back elegantly. There was something immediately different about her." 
"In an orcish cage, everything from her poise to her aura was off. But, here she was a natural fit with the nobles strolling around the gardens."

ele "I am Lady Eleanor of House Delane. This is my signet ring."

"She flashed a ring that Rowan had never seen on her fingers before."

ele "Rowan Blackwell is my honoured guest. He has my pass of entry, and will be my responsibility."

rkn "...Rowan Blackwell…"
rkn "Yes Ma’am. Welcome back."

"The guards rushed to the sides of the gate, raising their pikes to allow Rowan and Delane through."

#show lodge bg
scene bg36 with fade

"Rowan and Delane walked briskly together through the lodge. Rowan had to pause every so often though to marvel at the interior. Magnificent pelts hung on the walls. Much of the furniture as well was made from all manner of deer and fox skin."
"It was as though the entire building was a testament to the history of luxury that the members experienced."
"The place was not too populated at this hour. But, every so often, someone would look up as they moved. No one paid too much mind though. His proximity to Lady Delane made him appear like just another guest."

show rowan necklace neutral at midleft with dissolve
show eleanor dress neutral at midright with dissolve

ele "I had little to worry about with my family. They all made it out just in time. Much of the house staff is gone, of course. "

show eleanor dress concerned at midright with dissolve

ele "Some of them I’d known my entire life."

show eleanor dress happy at midright with dissolve

ele "But, my parents and siblings all made it to the capital without too much incident. Indeed, I was the only one who was in real trouble."

"She gave him a soft smile."

ele "One cannot always expect swashbuckling heroes to rescue them from a sentence of death or worse. I got lucky, I suppose."

ro "With all due respect, my lady."

show eleanor dress happy at midright with dissolve

ro "If you could call yourself lucky, I don’t believe we would have first encountered one another in a secret Orcish prison cell."

"Delane chuckled at that. He knew from experience that the best way to keep her engaged was to stimulate her brain. She liked a verbal sparring partner."

ele "Now that I’m no longer concerned with the threat of a truly undesirable marriage, among other things, one does have to wonder…"
ele "What was the hero of Karst doing exactly at the centre of one of the largest orc tribal confederations, exactly?"

show rowan necklace neutral at midleft with dissolve

"Rowan laughed softly. Better to treat it as just a joke for the moment. He didn’t much think that she’d be too appreciative if his answer was to ally them to demon lords."

show eleanor dress neutral at midright with dissolve

"Delane paused suddenly right outside one of the doors in a long passage."

ele "This is a private room. My family has a long standing reservation on it. We will not be disturbed or overhead in here."

"Once they were inside, Delane sealed the door behind them. Rowan gave a sigh of relief."

if eleanorCaveSex == True:
    "This had been the first time they had been alone together since their escape. The first time they’d been able to enjoy each other’s company since their...encounter in the cave."
    
ele "While our chat outside was riveting, there is another reason I called you here."

show eleanor dress concerned at midright with dissolve

ele "Please be so kind as to excuse me for a moment. I’ll be in the side room."

hide eleanor with moveoutright

"Delane slipped hastily through another door at the side, leaving Rowan alone to explore the room."
"It was like anywhere else in the lodge no doubt. It was filled with tokens from the history of house Delane, some going back centuries. A medal awarded to Sir Duncan Delane by the Baron two hundred years before held the place of honour."
"But, there was only so much exploring he could do before Delane returned."

show eleanor naked aroused at midright with moveinright
show rowan necklace shock at midleft with dissolve

"She was standing in the doorway of the side room, naked as the day she was born."

ele "One must reward those who do them a kindness. It is only the polite thing to do."

"She had hungry eyes as she slinked towards Rowan. Her shapely hips rolled with each delicate step. The distance between them was closing fast."

ele "A life debt requires quite the reward. I may never be done doing so."

if eleanorCaveSex == True:
    ele "You did seem to so enjoy your first taste of it, after all."
    
menu:
    "A hero’s reward.":
        $ released_fix_rollback()
        jump DelaneLodgeSexScene
    
    "Turn her down gently.":
        $ delaneReject = True
        $ released_fix_rollback()
        show rowan necklace concerned at midleft with dissolve
        "Rowan averted his gaze from her body quickly. As he looked at her naked body, a single thought had struck him like a hammer. Alexia."
        ro "My lady. I beg your forgiveness. I do. But, I can’t accept this. I’m a married man." 
        "No matter what else had happened since he’d first gone to Bloodmeen, that fact remained true."
        if eleanorCaveSex == True:
            "Delane shrunk in rejection. Her arms wrapped themselves over her bare chest. But, she still looked at Rowan with a powerful expression. Only now it showed skepticism."
            ele "Interesting. Were you mysteriously less married back in that dark cave? Or perhaps you are a newlywed?"
            "Rowan shook his head. How did he know that was how she was going to reply."
            ro "My Lady. That was a mistake. It was a stressful moment. I never should have indulged in that way. It was wrong of me. To her. And to you."
            ele "Hrmmph."
            "Having accepted his rejection less than gracefully, Delane slinked back into the side room to get dressed once more. She wasn’t about to remain naked."
        else:
            ele "I suppose this is what a lady gets for daring to hope. "
            "Rowan wanted to rise to his feet to comfort her but decided in this context it wasn’t appropriate."
            ele "Alas, you will simply have to continue to bear my efforts, even if I am willing to chalk today up as a defeat."
            ele "I will have you know that the last man I took to bed was married as well. It did not take me one try, I will assure you of that."
            ele "You underestimate me, good sir."
            show rowan necklace happy at midleft with dissolve
            "Rowan exhaled. It seemed that she had taken the rejection in stride. That was well. In a city of vipers, he needed Delane’s help."
            "Having accepted his rejection gracefully, Delane slinked back into the side room to get dressed once more. She wasn’t about to remain naked."
        show rowan necklace neutral at midleft with dissolve
        show eleanor dress neutral at midright with dissolve
        jump delaneLodgePostSex
    

label DelaneLodgeSexScene:

$ delaneLodgeSex = True

show rowan necklace aroused at midleft with dissolve

"Rowan watched her body in motion. She was so close now, almost pressing her naked skin against his chest. He stirred softly."

ro "It would be my honor to receive whatever favour you desire to give me."

ele "Hrmmm…"

"Their lips met. Both of their eyes closed. For a long lingering moment, he enjoyed the feeling. She was so soft. Young, beautiful, and blessed with an air of nobility that radiated from her."
"She broke the kiss, moving close enough to his ear that he could feel her warm breath."

ele "One choice. Whatever you want to do with me. Here and now."
ele "Whatever you want…"

"Rowan blinked twice. Anything he wanted. Anything he wanted. It was hard to think with their proximity. He was already riding on instinct."

ro "Have you ever been taken from the rear?"

"Delane’s eyes fluttered softly."

ele "...Never."

ro "...And you said that you would do whatever?"

ele "…"
ele "There should be some olive oil in the dresser."

scene cg519 with fade
show eleanor naked aroused behind cg519
show rowan naked aroused behind cg519
pause 3

"Moments later, Rowan’s clothes were discarded on the floor, and he was sitting naked on the large couch. Delane had taken a position on her knees right in front of him. Her eyes were drawn, like a moth to flame, by his erect manhood."
"She stared at it with raw lust."

ele "...Incredible."

"She reached down to the jar at her feet, and wet her hands with olive oil. Rowan found out that the contents were rather cold. He could feel it when her fingers brushed over his cock. It brought a shiver up his spine."

ro "Mmh.."

"Delane giggled. She brushed her hand up and down his shaft carefully, rubbing hard to make sure that it was well coated with oil. Among other reasons."

ele "Someone is sensitive, huh? This is what you asked for. It’s rare to expect the one to balk at such an encounter to be the man."

ro "Keep going."

ele "If you insist."

"Her hands traveled up and down his length, making sure to cover every inch of his length with the oil. A droplet dripped down his balls."

ro "You can stop now."

ele "Another moment. You’re not the one who will experience a half done job the most."

ro "And I would know what a poor job is better than you would. You’re fine, My Lady. Really."

"Delane blushed softly."

ele "So you say."

scene cg520 with fade
show eleanor naked aroused behind cg520
show rowan naked aroused behind cg520
pause 3

"Rowan stood up slowly. It made room for his companion to get up on the furniture, positioning herself backwards towards him with her rear raised high up in the air and one hand clutching the top of the couch."
"The other hand shot between her legs. She was already working her clit."

ro "You couldn’t wait?"

ele "Do you really believe for a moment that I don’t want to cum from this as well?"

scene cg521 with fade
show eleanor naked aroused behind cg521
show rowan naked aroused behind cg521
pause 3

"Rowan responded by plunging his well lubed cock towards her sphincter. It spread slowly as he worked himself inside of her."

ele "Ah!"

"Rowan grunted out too. Her rear was tight. Getting his cock even another inch in took work. But, it also meant that the sensation of her inner walls pressing on him was more intoxicating. There was something oddly beautiful about using a hole for the first time. It was like taking it for himself."
"One hand dug into her hips, holding her in place. The other found a convenient handle in her long dark hair. That way she’d be steady as she took the full force of his thrusts. His breath grew heavier."
"The sounds emitted in the process were rather loud. Rowan hoped that the room blocked sound well. After all, between the moaning, the grunting, and the sound of Delane’s fingers hungrily working her clit, there was much to overhear."

ele "This is….ah...this is...different."

show delsexanimation1 with fade

"Rowan slammed himself into her with all of his strength."

ele "Ah!"

ro "Bad different?"

ele "Fuck no. More. Harder. Fuck."

ro "If you insist…"

"He took the lock of her hair that he had in hand and twisted it, Using it as a grip to slam even harder. It made the friction, already more intense from the less lubricated hole he was using, all the more overpowering."
"The effect this was all having on his partner was hard to overstate. Delane was groaning, moving, squeaking. Her finger against her clit moved with frantic abandon. This was her first time being fucked this way, and she certainly seemed to enjoy it."

ele "Oh fuck. Oh fuck."

"Her back went straight suddenly and a long groan slipped out of her lips. A moment later, her hand fell away from between her legs. She was spasming in abject pleasure."

ele "I...Oh…"

"Rowan kept up his movement. After all, just because she’d already cum didn’t mean that she wasn’t enjoying it. Besides, he was too far gone by that point. Lost in the movement of hips, the rolling of sweat, and the overwhelming tightness of her virgin passage."
"If anything he sped up the pace. No holding back for her inexperience any longer. He wanted to cum inside of her rear."

ele "Ah. Fuck. Ah."

show cg526 with sshake
show cg526 with sshake
show cg527 with flash
pause 2

"It did not take long for the effect to bloom. Fast moving thrusts, Delane’s tight rear, and his own lust worked in tandem. After some minutes that felt like hours, Rowan felt the little twinge of his cock that warned him what was about to happen."
"Then he let loose a load of his cum. Bliss ate his senses. He slumped over on top of her. They were both panting hard. The rise and fall of their chests almost seemed to work in tandem with one another."

#lodge bg
scene bg36 with fade
show rowan necklace naked aroused at midleft with dissolve
show eleanor naked aroused at midright with dissolve

ele "Well, my sister did tell me that it hurts."

"She groaned and chuckled."

ele "I fear you’ve left me bow legged for the foreseeable future. Such rudeness."

ro "You did say I could have whatever rewards I wanted."

ele "Which is proof you have no idea what you’re doing. Because, if you did, you’d know that I have no idea what I myself am doing."

"They both laughed and settled down on the couch, closer to how it was intended to be used. His arms were wrapped tight around her naked form. As they relaxed, a question came to his mind."

ro "If your goal was to fuck me. Why go to a building full of gossips?"

ele "Do you propose I try to bring you to my parent’s residence instead?"
ele "I have a cover story for your visit. You did save my life after all. Better to leave it as rumours then risk something worse."

ro "You are the expert."

ele "I am. Which is why you should ignore my most recent statement about not knowing what I am doing, and listen to me intently."

show rowan necklace neutral at midleft with dissolve
show eleanor dress neutral at midright with dissolve

"Some time later, they had cleaned up and gotten dressed again. As enjoyable as spending the rest of the evening naked in each other’s embrace might have been, there was a limit to how long the two could stay in the same room together with watching eyes around."

label delaneLodgePostSex:

ele "How long do you intend to stay in the capital for this time?"

"Rowan shook his head."

ro "Not long. Too much trouble awaits me in the field still. The situation, especially with the northern orcish tribes is still quite grim."

show eleanor dress concerned at midright with dissolve

ele "Oh."
ele "I had heard as much. The lives of many who have sworn loyalty to my family are at stake. I suppose I cannot fault you for your diligence."
ele "Still, you could remain in the capital if you like. No one would be shocked to see you hired as a noblewoman’s bodyguard."

if delaneReject == True:
    ele "You could even bring your wife if you so chose."

show rowan necklace concerned at midleft with dissolve

"It wasn’t like the idea wasn’t tempting. Say adieu to everything he struggled with and simply live out in Rastedel as a well paid retainer. But, the concept was absurd. Even more so considering all of the aspects of his situation she was not aware of."

ro "Would that I could, my lady. But, there are people who need. There is no escape for me."

ele "Very well."
ele "..."
ele "But, the next time you are here, we will speak further. We still have much to discuss. Much indeed. You have no choice in the matter. It’s a noble decree."

"Rowan chuckled to himself. It was an absurd proposition, especially since he wasn’t even her vassal."

ro "Yes, Ma'am."

hide eleanor with dissolve

"Rowan left the lodge shortly afterwards. True to what Delane had suggested, there was an odd glance at him, but not the kind of attention one would expect if people had been able to hear what they were up to." 
"Rowan thought of the conversation they had. Soon, he would be back here. There was no way that Jezera was finished with this place. Would he be capable of tricking Delane into aiding him? Would he be capable of convincing himself to trick her?"

if avatar.corruption < 31:
    "The concept seemed repugnant. But yet, here he was."

elif avatar.corruption > 31 and avatar.corruption < 61:
    "Rowan didn’t know the answer."
    
else:
    "The answer he suspected, to both questions, was yes."

$ lodgeFirstVisit = False
jump rastMenu


label lodgeVisit:

if firstLodgeVisitPostBattle == True:
    $ firstLodgeVisitPostBattle = False
    $ lodgeWerdenAvailable = True
    $ lodgeCrevetteAvailable = True
    scene bg33 with fade
    show rowan necklace neutral at midleft with dissolve
    "Rowan paused just outside the Grand Camilla Lodge. If he was going to inquire about an an alliance with the purple faction, this was the place to do it."
    "There was just one problem. Peasants couldn’t get into the Lodge."
    "He stood outside the gates wondering what to do about this dilemma for a short time. Perhaps he’d need Ameraine’s help getting in. But, Ameraine was associated with the Coppers. Would it be dangerous for her to be the one vouching for him?"
    "Thankfully, he did not need to ponder a solution for long."
    #mys happy
    show mystery neutral at midright with dissolve
    myst "You’re Rowan, are you not?"
    "Rowan tilted his head. He didn’t recognize this man, though his fine clothes suggested he might have seen him at court. It took him a moment, to realize where he’d seen him before."
    "He’d been in the inn while he waited for Ameraine."
    ro "...Yes."
    ro "...And you are, My Lord?"
    "The man smiled at him. His face was impossible to read."
    myst "Here to help. You want to get inside right?"
    "Rowan didn’t even get a chance to answer. He strode boldly up to the guards and whispered something to them. Rowan couldn’t hear what. What did this man want? Was he really an ally?"
    myst "It should be fine now. Come on in."
    "Rowan hesitantly approached the guards, and they didn’t stop his entrance this time. The man had already rushed along ahead, and had gone through the door. Rowan sighed. Whoever he was, he distinctly didn’t want to stay and chat."
    scene bg36 with fade
    show rowan necklace neutral at midleft with dissolve
    "Inside, Rowan found the lodge filled with nobles going about their daily indulgences. Chatting, drinking tea, playing the odd game with one another. There was some glancing and muttering in his general direction, but not a distracting amount."
    if delaneLodgeSex == True:
        "Certainly the lodge was more subdued today then when he’d last been inside. The whispers were a bit more hushed, and the expressions on the faces betrayed worried."
        "They came here for a distraction."
    "The halls of the interior were a maze of passages and rooms. Some were set aside for specific families and dynasties. In some way or another, much of the noble history of Rosaria was built into these walls."
    "Duke Werden would almost certainly be somewhere in here. This was where he made his base of operations. Ameraine didn’t think he would be the best candidate to use to bring down the city. Chancellor Crevette would be somewhere in here as well."
    "The question was, who was he trying to meet with?"
    $ lodgePersonVisit = 0
    jump lodgeVisitMenu
        
else:
    pass
    
label lodgeVisitMenu:

scene bg36 with fade
show rowan necklace neutral at midleft with dissolve

if lodgeCrevetteAvailable == False and lodgeWerdenAvailable == False:
    jump lodgeJuliet

elif lodgePersonVisit == 1 and delane_status == "free":

    "Rowan made his way back to the Grand Camelia Lodge, and discovered that the guards had been informed to let him in. Perhaps they had been warned in advance."
    "This time, he was stopped, briefly, by a southern noble eager to hear about the situation in his lands. He was a vassal of Duke Raeve, and had an estate not far from where Arthdale had once stood."
    "Rowan didn’t have the heart to tell him that the entire area had been destroyed in the fighting. After a small discussion he moved on."
    "The center of the lodge was still curiously depopulated. It seemed every day that another person of high birth decided that it was best to wait out the conflict in their own lands. Rowan had to stop himself from sighing. Didn’t they realize that dispersing made them easier to pick off?"
    "He wanted to shout out at them."
    "Alas, he was here with a job to do. He needed to focus."

else:
    pass


menu:
    "Visit Werden." if lodgeWerdenAvailable:
        $ released_fix_rollback()
        $ lodgePersonVisit += 1
        jump lodgeWerdenVisit
        
    "Visit Crevette." if lodgeCrevetteAvailable:
        $ released_fix_rollback()
        $ lodgePersonVisit += 1
        jump lodgeCrevetteVisit



label lodgeWerdenVisit:

"Duke Werden was not hard to find. Few of the nobles were willing to engage in any long conversations, but he did get one to point in the right direction. When he found the room with two guards outside, both clad in the purple of Solansia’s Thorns. This was the place."

ro "Excuse me, My Lords. I was hoping to perhaps get an audience with the Duke?"

"The two guards exchanged glances, and one ducked into the room. Rowan stood awkwardly in the hallway, waiting on the decision. The guard returned and gave a slight nod."

show rosarian knight neutral behind bg36

rkn "Come in."

"The inside of the room looked like a war room. There was a grand oak table with lords and ladies, many in sterling silver armor, gathered around. There even was a map of the city on the table."

show werden neutral at midright with dissolve
show doran beardless neutral at edgeright with dissolve

"Duke Werden sat at the head of the table. Duke Raeve sat nearby him. That fact gave Rowan some hope. He had an ally in the room. It also explained, partially, how Ameraine knew about Werden’s plans."

ro "Werden."

"Rowan went down to one knee and lowered his head. This was the place to show a peasant’s humility."

show rowan necklace happy at midleft with dissolve

ro "My Lord, it warms my heart see you in good health."

werd "On with it."

"The Duke was feeling curt today. That did not bode well."

ro "I was hoping to help with the defence of the city. As I understand it, you are the one doing the most to-"

werd "A position in command will be arranged for you among the new levies. You are an experienced commander. That has value for training."

show rowan necklace concerned at midleft with dissolve

ro "..."

"Werden never changed. A mere training position was a slap in the face to someone called “the hero” of the country, and everyone knew it. A few lords glanced sideways."

ro "I do not speak of the city’s official defence, if you understand. I have been hearing much of the affairs of the city, lately. You are-"

werd "Not interested."

"A purple cloaked commander spoke up, looking with exasperation back and forth between the kneeling Rowan and the unflinching Werden."

rnb "But, My Lord, he is-"

werd "A commoner."

"There it was."

ro "I only wish to help you. The realm is as much yours as mine."

"Now it was Duke Raeve’s turn to speak up."

dor "Perhaps, we could come to…"

werd "No."

"He turned to his fellow duke. Raeve gasped at the insult. Even Werden couldn’t brush off a fellow duke so easily."

werd "He has operated on the edge of a disaster for more than a year. Appearing and disappearing in the face of tragedy. No supervision. Perhaps he is the cause of disaster. Mayhaps he is helping. Save for your word, there is no proof. "
werd "Most trust him, simply because he was of great use once. I am not most."

"He turned back to Rowan with his arms crossed over his chest. His gaze was cold. It tore through Rowan."

werd "You are acting above your station, Rowan. I won’t accept demands made of me."



if delane_status != "free":
    ro "But, your brother…"
    #werd angry
    werd "Is not here anymore."
    "There were a few quiet gasps around the table, but no one said anything to challenge Werden. No one would stick their neck out for him."
    ro "..."
    werd "Do you have anything further to add Rowan?"
    "He didn’t."
    "Rowan walked back out into the hallway, and once out of sight of the guards, put his head in his hands. The entire meeting had been a disaster. Werden didn’t seem inclined to budge at all. The entire ordeal had taken mere minutes."
    "Now it seemed that the only possible route towards an alliance with the Purples might be through Patricia. If she vouched for him then he might overcome the duke’s reluctance. But, he still heard what Ameraine said about her ringing in his ears."
    "Was there no way to protect the kingdom from his vantage point?"
    $ lodgeWerdenAvailable = False
    $ werdenTalkFailed = True
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return
    
else:
    "Before another word could be said, there was an interruption from outside. Someone was being told to leave by the guards. But, whoever it was didn’t seem inclined to accept that. Werden craned his head softly to the side to see who was the cause of the disturbance."
    "Then she marched in."
    show eleanor dress happy at edgeleft with moveinleft
    show rowan necklace shock at midleft with dissolve
    ele "You have Rowan here and I wasn’t informed on the matter!? My word, is a messenger so hard to send off?"
    werd "Rowan was just about to leave."
    "Lady Delane looked to the side at Rowan and nearly leaned in to give him a hug."
    show eleanor dress neutral at edgeleft with dissolve
    ele "Was he now? What’s going on?"
    "Werden sighed."
    show rowan necklace neutral at midleft with dissolve
    ro "My lady it is-"
    werd "Enough."
    werd "This isn’t a matter of concern for you, Lady Delane. This audience is at an end. Speak with him if it pleases you. Rowan had some demands that were improper for a commoner, but I-"
    "Delane crossed her arms over her chest."
    show eleanor dress angry at edgeleft with dissolve
    ele "Improper? Improper how? My lord, Rowan is the hero of the realm. He could demand a statue made of gold and a knight to sprinkle fresh roses everywhere he walks and he would be within his rights."
    "Rowan remained silent, but was prepared to jump in when needed. Perhaps she could do what the meeker Duke couldn’t."
    #werd angry
    werd "Do not forget who your leige lord is. Friendship with Juliet is no excuse for impudence. You speak out of place."
    ele "Only one man in this room has saved my life. It wasn’t you. Who infiltrated a camp with thousands of orcs to bring me to safety? In the process wreaking chaos in their ranks?"
    ele "I’d be a poor vassal to let such behaviour go without comment, and you a poor liege to demand my silence."
    "The assembled lords squirmed all the more in his chair now. They’d been uncomfortable with Werden’s tone towards Rowan, but this was different. She was breaking protocol."
    werd "Saving you was an act of heroism, aye. But, Rowan came to demand a place at my war table. That hardly warrants-"
    "Lady Eleanor shook her head furiously."
    ele "You do not understand what you are saying, my liege."
    ele "I was captured by orcs...on your soil. In your lands. By a band in the thousands marching in your territory while you were concerned with these stupid power games. Rowan rescued me. He created infighting that shattered the confederation by doing so."
    ele "Your response was slow. His was not. He saved your people. What right do you have to criticize him? You owe Rowan a great debt for his actions."
    "The room went dead silent. Her words were left stinging in the air. Then, when they had landed, it erupted into furious debate. Lords considering how to respond in scandalized tones."
    show rowan necklace happy at midleft with dissolve
    ro "My Lady, maybe it would be best if I simply-"
    "Delane waved Rowan off as well."
    ele "I won’t stand for this injustice. I won’t. He can’t treat you this way."
    dor "We should calm down. High tempers will not-"
    "Duke Werden raised his hand to call for silence."
    #werd neutral
    werd "..."
    werd "Yes."
    werd "Yes, you have the right of it."
    "Werden turned towards Rowan, features softening ever so slightly."
    werd "You did me a service in rescuing my vassal’s daughter. Though, perhaps you didn’t have to rescue her tongue with the rest of her."
    werd "You also did me a service in helping protect my lands for me. I owe you my gratitude."
    werd "I will consider your request further. But, I swear no oath that you will get a positive reply. Merely a fair consideration."
    werd "If I were to accept, there would be strings attached. You understand this, yes?"
    "Rowan nodded softly."
    werd "Good. Go. Both of you."
    scene bg36 with fade
    show rowan necklace happy at midleft with dissolve
    show eleanor dress happy at midright with dissolve
    "Rowan sat across from Delane in a chair in one of the main parlors. They were both a bit breathless. Delane giggled to herself madly."
    ele "I’m going to regret leaving our orcish friends when my father discovers what I just did."
    "She took a sip from a goblet of wine."
    ro "That was not a burden that you had to bear. You put your reputation on the line for me. How did you even know that he could be persuaded?"
    ele "I’m a lady-in-waiting for his daughter. One learns a great deal about a lord from a long term friendship with the one person he actually dotes on. He’s stubborn but not unreasonable."
    ele "Your mistake was too much deference. It seems no amount of war glory can take the commoner out of you. Some lords may rage when they hear sound disagreement. But for all his faults, ignoring negative council is not one of them."
    "Rowan scratched his chin. He had been quite differential in that meeting. Had so much time as a commoner gotten in the way of his mission?"
    ro "Do you believe he’ll come around?"
    ele "Maybe? You’re definitely going to have to press him a bit more though. When he said he wasn’t sure, he meant it."
    "Rowan sighed. Delane, for her part, seemed rather done with the topic."
    ele "I can’t believe you’re still wearing that travesty, even in the city. Must you advertise your lack of class wherever you go? I can find you a tailor."
    ro "They call me a dirt general. What would a dirt general be without his dirt?"
    "They both shared a laugh. Rowan’s mind was far away. Should he side himself with Werden or not? Would he be able to sell the idea to Ameraine and Jezera if he tried?"
    "Rowan didn’t know."
    $ lodgeWerdenAvailable = False
    $ werdenTalkFailed = False
    $ werdenConvinced = True
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

    
label lodgeCrevetteVisit:

$ lodgeCrevetteAvailable = False

"It took some time to even find Chancellor Crevette’s side room. The Crevettes were not a family of the same caliber as the Werdens. Many didn’t even know where it was. So, it was no surprise that when Rowan arrived, he found it mostly empty."
"Except, that is, for the woman he wanted to see."

show patricia annoyed at midright with dissolve

ro "Lady Crevette?"

"The short stubby woman looked up from her desk. It was covered in scrolls and maps of different shapes and sizes. Some were quite old. Rowan took a step inside the darkened room."
"Like the others, it was still filled with regalia, trophies, and banners of the centuries. But, this place had been fashioned into some more alike a makeshift office then a lounge."

patr "Is the fact that I’m working really so hard for you lot to grasp? I..."

#patricia surprised

patr "Wait...Rowan Blackwell?"

ro "In the flesh."
ro "I only just returned to the capital a short while ago. When I was last here, you tried to help me and my people. I owe you my gratitude."

show patricia neutral at midright with dissolve

"Crevette’s brow narrowed."

patr "Hrmm."
patr "..."
patr "Would you be so kind as to sit down?"

ro "Certainly."

"When he sat at the table, he got a good view of what she had looking at. Supply ledgers, census information, maps of the walls."

ro "This is for…?"

patr "The defence of the city. Yes. Marianne insisted that planning stayed within the ministry. It’s not like I haven’t been getting help from The Duke, but for the most part it’s my job."

"Rowan stared at the documents. In truth, it mostly reminded him of his own work back at castle Bloodmeen."

ro "Are you trying to raise a new army?"

"Patricia snorted angrily."

patr "Something like that. More like snap and make a new army appear out of thin air."

show patricia sad at midright with dissolve

patr "I shouldn’t really be telling you this...but you are Rowan...so fuck it. Maybe you can help me a bit."

show patricia neutral at midright with dissolve

"She stretched back and sighed."

patr "We didn’t just lose men out in Astarte. We lost a generation of training from the royal academy and an entire army’s worth of equipment. We can’t just buy more training, especially with all the instructors who went out on the sortie. "
patr "We can’t buy that many weapons either. You can’t just stroll down to Rou De La Ferronn and pick up five thousand swords and helms from blacksmiths. They need to be made. We have every shop in the Ferronn at work. I calculate that…"

"Rowan’s eyes glazed over slightly as Crevette raddled of long strings of numbers off the top of her head. Some of it was so complex that Rowan had trouble keeping track. "

patr "You see the nonsense I have to work with. Don’t you?"

"Much of the next hour was spent at her desk with her answering questions. When it came to the numbers and foodstuffs she was a genius. But, she peppered Rowan with questions about different types of gear and their effectiveness."
"The people requisitioning the equipment hadn’t fought a single battle in the last war. How would they know what type of helmet to buy?"
"Rowan picked up a document off her desk and studied it."

show rowan necklace concerned at midleft with dissolve

ro "Why are the recruitment numbers so low? Not even at one thousand in a city of more than fifty thousand. If the levies are being raised, there should be more men then this taken from the capital without crippling functionality."

"She just sighed and snatched the document out of his hands."

show patricia sad at midright with dissolve

patr "Who knows? I sort the numbers, I don’t do the counting myself. Part of it is deserters. Anywhere from a quarter to a third of the city have sought a less glaring target or “gone on vacation”."
patr "I did try to run the question up to the Duke. He said that it was probably the morale. So many of the small folk have fled the city already. Many more are avoiding the draft."
patr "Solansia be good."

"Rowan’s ears perked up at the mention of Werden. Perhaps this was an opening to discuss what he really wanted to talk about."

ro "As much as I enjoy being of service, the logistical element was never completely my specialty. Isn’t Duke Werden just down the hall? He handled more of that during the war then I ever did."

show patricia neutral at midright with dissolve

"That seemed to strike a chord. She shrunk slightly into her chair."

patr "He has been helpful, but the Duke has many other priorities to detail. He runs a sixth of the realm, you know."

"Rowan paused to consider his options."
"Clearly, this was a solid line of discussion to press. But, there was that constant thread hanging over all of this. The line of deniability that pretended that she wasn’t actively plotting Marianne’s downfall."
"Rowan really wasn’t built for all of this noble backstabbing. It was time to dispense with the pretenses."

show rowan necklace neutral at midleft with dissolve

ro "My Lady. I understand that the Duke and his loyalists do not plan to sit quietly by while demons threaten the capital. You don’t have to hide it from me."

#patricia surprised

patr "Do..do you now?"

show patricia happy at midright with dissolve

ro "I came here to help. Really. Or at least I’m trying to. It’s not easy for a commoner to be accepted as an ally here."

if werdenTalkFailed == True:
    ro "I tried. I was waved away like a servant."
    
else:
    ro "I tried. It didn’t go horribly, but his armor impossible to so much as crack."
    
"Crevette leaned forward slightly. It was a good first tactic, from what little he knew of intrigue. If she felt put upon, it would establish a critical solidarity between them."

patr "I suppose it wouldn’t be. But, I’m surprised that Werden would be inflexible about that kind of thing. Yes, he insists on proper decorum, but you are useful."

show rowan necklace concerned at midleft with dissolve

"Rowan lowered his head. He didn’t need to do much acting to find feelings about Werden. That came naturally."

ro "We don’t have the best history together. You know that. It means that when I want to help him save the realm, I’m kept on the outside."

"Crevette shook her head."

patr "Do other people know about what’s happening? I’d be pretty fucking horrified to learn that the back rooms of the Lodge have become common knowledge."

ro "Not as far as I know, My Lady. I am blessed to have a few of the right friends in a few places who put it into my ear. I doubt Marianne knows anything specific."

"He looked down at the table, and picked up a document. It had a progress report on the repairs to a segment of the walls."

ro "In fact, I don’t even know anything specific. I was rather hoping that by coming here, I could figure out a way to help."

"She gave him an appreciative look. It was a reminder that it was just the two of them alone in this dark room."

patr "Well you’ve already helped. The Duke holds me in high esteem, but he thinks little of the official plans for the city’s defence. After all, this work all becomes moot if we can get the Baron to agree to take in Werden’s troop levies."

show patricia annoyed at midright with dissolve

patr "So both the Duke and the High Arbitron have left it to little old me to do the actual planning."

"Patricia snorted."

patr "Some days I am one of the highest officials in the realm. Other days I am a glorified flunky. The latter feel far more common than the former."

"All of that only made subverting her an even juicier target. Both as a political leader and as a way to weaken the city’s defences. Ameraine had a keen eye."

ro "What is it the Duke wants, besides defeating the demons?"

patr "That’s a hard question. The only one who really knows the answer to that is Werden. But, it’s not hard to get an idea for it. That’s why so many great lords stand behind him. Duke Mortimer stands with him. As now does your own liege."

show patricia happy at midright with dissolve

patr "Not that Raeve exactly has much in the way of levies or income at the moment."

show patricia neutral at midright with dissolve

patr "Werden is not just mad that the demons are on the march. He even predicted it would happen years ago."
patr "I’ve never met a fucker as pious as Werden is. He puts the actual priests to shame. To him, Solansia’s order is coming apart. The people originally put into power have given up their responsibilities. "
patr "The nobles don’t fight. The Prothean priests act like dictators."
patr "Werden is an old fashioned kind of man. He imagines a line of Solansia’s Thorns crashing into the demon hordes and throwing them back like in centuries past. I almost think he’d be more at home down in the Tundra than here."

"All of this sounded in line with what Rowan knew about the Duke. In a way, the Duke was a revolutionary. But, in other ways he was the least revolutionary man in the kingdom."

ro "So what do you think of it all? Why are you helping him?"

show patricia happy at midright with dissolve

patr "I think the day Marianne is sent back to Prothea will be the finest day of my life. That’s what I think."

show patricia neutral at midright with dissolve

patr "Besides, my brother likes him. A lot of lords do, I suppose. My brother is head of my house, and if my house likes him then so do I."

"Well, that made things slightly more complicated. It would be easier if it was just confluence of interests, rather than a matter of family loyalty."

ro "But, Werden doesn’t put you in a position of power?"

show patricia annoyed at midright with dissolve

patr "You’re pushy for a commoner, you know that? "

show patricia neutral at midright with dissolve

"Rowan’s posture shrunk slightly. He’d over extended his position just a bit. If he pushed much further he might find any respect he’d gained from her lost."

patr "I have power and respect. I’m the highest native born member of the ministry. But, my family is of middle caliber. And I am not a military leader. Thus…"

ro "Desk work?"

patr "Desk work."

"She looked down at the map, and at once her expression shifted back to the studious intensity that she’d had when he first arrived."

patr "Help me with this here. The commanders are telling me they want me to put moats here, here, and..."

"Rowan helped the woman with her work once more. At times he struggled to keep up, but it was imperative for him to seem helpful."

show patricia sad at midright with dissolve
show rowan necklace neutral at midleft with dissolve

patr "Look…"
patr "I’m loyal to the Duke, but that doesn’t meant we always see eye to eye on everything. He’s as inflexible as lead. Not the best quality in politics."

ro "So I’ve noticed…"

patr "So I’ll make you a deal. I can bring you into the fold under my personal protection. There is always use for smart and well regarded commoners, no matter what Werden says."
patr "But, don’t think it’s going to come easy. My vouching will only get your foot in the door. You’re still going to need to prove your value to the cause."
patr "And afterwards, you’re still going to owe me a favor. Don’t mistake this for generosity. I help you and you help me."

"Rowan nodded to himself. Just what he wanted to hear. The hardest part would be keeping a straight face."

ro "I’d have to think about it."

show patricia annoyed at midright with dissolve

patr "Sure, it’s not like a teleporting demon army could appear outside our gates any moment."

show rowan necklace happy at midleft with dissolve

ro "I never said think about it for especially long."

"Rowan kept on helping her for a short time longer. At one point her questions shifted to the demon army. What was it like fighting orcs? Just how bad was it in the field?"
"To the residents of the city, Crevette included, the walls had become a prison and the outside a great unknown. Rowan helped her for a time longer, but was soon moving again. He made an excuse just good enough to get him out the door."
"There was still much to do."

if avatar.corruption > 31:
    "When he’d spoken to her, he was almost able to feel the longing coming off of her. He’d seen so many people be corrupted now. Sometimes, even with his own aid. Was it strange that he could recognize the seeds now?"

$ lodgeFirstMeetings = True
$ lodgeCrevetteAvailable = False
$ prevent_tile_exploration()
$ push_to_previous_tile()
return


label lodgeJuliet:
    
"As he was leaving the building, Rowan ran into a familiar face, if only for a moment."

show juliet neutral at midright with dissolve

if juliConvo == True:
    "Duke Werden’s pretty blond daughter passed by him in the entrance hallway. The moment that she caught sight of him, her cheeks turned a shade of scarlet."
    "It seemed her crush had not faded since his last visit."
    "She gave him a hurried wave, and then sped up. Her footsteps made a pitter patter on the marble floor. No doubt she was here to see her father."
    show rowan necklace concerned at midleft with dissolve
    ro "..."
    "Rowan sighed. If there was one man in this world to pine for, none brought worse luck than him."
    
else:
    "It was the blond noblegirl. The one who’d been making moon eyes at him for most of the ball. They crossed paths in the entrance hallway, and the moment she saw him, her cheeks turned a shade of scarlet."
    juli "H-hello…"
    "Before, Rowan could even get a word in, she rushed off. Her footsteps made a pitter patter on the marble floor."
    show rowan necklace shock at midleft with dissolve
    ro "..."
    "Just who exactly was she?"


$ prevent_tile_exploration()
$ push_to_previous_tile()
return


###############################################################################################################
###############################################################################################################
###############################################################################################################

label lodgeRepeatVisit:

scene bg36 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan had decided to come back to the Grand Camelia Lodge and find out more about the Purples and their plans. The effort proved a fool’s errand. This time, the guards didn’t seem much inclined towards letting the intrepid commoner in."
"No one came to collect him either. It seemed that the stars had chosen today as a day he would not enter the lodge. After an hour of failed efforts, Rowan turned away. There were other productive things he could do."

jump rastMenu

###############################################################################################################
###############################################################################################################
###############################################################################################################

label lodgePostPathWerden:

scene bg36 with fade
show rowan necklace concerned at midleft with dissolve

"Rowan stepped into the Duke’s meeting room in the lodge. He tried not to show how nervous he was. He had to present the image of a partner worth negotiating with, now that it was the two of them alone in a room together."

show werden neutral at midright with dissolve

"He found Werden alone, save for a few Thorns who were acting as guards."

werd "Rowan. I was about to go on an inspection."

ro "I will happily go with you, My Lord."

werd "Hrmph."

scene bg31 with fade
show werden neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve

"A short time later, the two of them were riding together along the outskirts of the city, examining the walls. There were sparse pockets of armored men going along to all of the structures built outside the walls. A few were burning. More would be burning later."

#werd unhappy

werd "I told them to have those buildings down days ago. Slow."

show rowan necklace concerned at midleft with dissolve

"Rowan slowed his horse slightly to get a better look. They were ramshackle huts, but people had lived in them once. The overflow of the city."

ro "The outskirt housing? Are there people still living there?"

werd "Not many."

"No matter where the troops went, the buildings were empty. With all the refugees from the city, there were many new vacancies for squatters to take up. Anyone else had already left. When the orcs came, if the orcs came, who wanted to be outside the city walls?"

werd "Impractical for a siege to have around. Enemies can hide in them close to the walls."
werd "They should have lived elsewhere. In the city or elsewhere in the villages."

"Rowan gritted his teeth. He was supposed to be here getting on Werden’s good side. The urge to argue was hard to squash."

ro "The price of the city is often too high for small folk. It’s all many could afford if they wanted to live in Rastedel."

werd "Perhaps too many people wanted to live in Rastedel."

show rowan necklace angry at midleft with dissolve

"Rowan wondered if he meant anyone in particular by that."
"But, Rowan managed to stop himself from doing anything...undiplomatic. A little bit later, Werden finally turned to the topic that Rowan had come to discuss."

#werd neutral

werd "Delane was right. The realm needs you once more. Now is not the time to ignore someone useful."
werd "The capital is in crisis. I have power, but I am not loved."

ro "I hadn’t noticed."

werd "Hrmph."
werd "We must have someone who understands the common man. Someone the common man will accept."

#werd sad
show rowan necklace shock at midleft with dissolve

werd "People think that I am blind. People think I live in a tower with my ideals. But, I see the trap I am walking into. To the small folk, I must seem little different from a demon."

#werd neutral

werd "I don’t trust you."
werd "But, perhaps I need you."

ro "..."

show rowan necklace neutral at midleft with dissolve

"Rowan didn’t quite know what to say. Did Werden truly understand what he was doing? Rowan had to be sure. At this point, he wasn’t even really thinking about his mission."

ro "I’ve saved the realm before. You were there the last time it happened. I never got a reward for it…"

#werd angry

werd "Are you asking for compensation? You came to offer your aid of your own volition."

ro "No. I speak about that tower of yours. That trap."
ro "If order and justice is to be maintained in the world, how can someone who has saved so many people on many occasions be justly sent back to a burned farm? "
ro "I am merely musing to myself. I will join your cause regardless of the answer."
ro "But, can you not forgive me for wondering, My Lord?"

#werd sad

"Werden didn’t answer the question. But, he didn’t dismiss the question either. His head lowered, and a shadow was cast by the mid-day sun over his eyes. Their horses came to a stop."

#werd neutral

"When he raised his head again, it was the normal Werden who he was riding with."

werd "The point is moot. I have not accepted an alliance yet."
werd "There is something I must have before that is possible."

"Rowan nodded. The mission. He was here for a purpose. He had to remember that."

ro "Name it and you will receive it."

werd "Verdoin Abbey."

"He pointed out in the distance towards the rolling hills."

werd "It stands near the road to the North East of the city. In Lord Custer’s domain. Strategically Important. It overlooks the main passthrough to the east."

"They passed a straw hut burning next to the gate. Troops stood around with water to ensure it was a controlled blaze."

ro "We have a garrison there, yes?"

#werd angry

werd "Had."

#werd neutral

werd "Marianne pulled the troops out after Astarte. We were spread too thin, and the position was expendable. Disaster could have come any day. It still could."
werd "But, it proved a mistake. Some of the Demons’ forces have occupied the building. A band of orcs. We must take it back swiftly to ensure the movement of supplies."

"Rowan had to stop himself from freezing up. Orcs taking the abbey? He would have heard of that if they were sworn to the twins."
"No doubt it was another, entirely independent, orcish band."

werd "Is something the matter?"

show rowan necklace concerned at midleft with dissolve

"Had it been so obvious? Best not to let him dwell on it."

ro "I shouldn’t have been surprised you had a task like this in mind. But, is your only goal the strategic picture of the realm?"

werd "I suppose my motive is not entirely pure. We must take the abbey before Marianne can. We will have shown ourselves the best defenders of the realm."
werd "The holdouts must come to see that only the Thorns can protect Rastedel. Having you as a living standard aids in that."

"They brought their horses to a halt in front of the gate."

werd "I have a force of my own levies and Thorns waiting nearby the building. You will link up with them and personally lead the assault on the abbey. That way, when it is done, I can have you ride beside me at the return to the city."

show rowan necklace happy at midleft with dissolve

"Rowan let himself smile."

ro "I am to be a standard for you to wave, huh? I can’t be surprised."

werd "Or a casket to ride besides. Verdoin Abbey was adopted as a defensive position for a reason. Many may die in the process of taking it."

show rowan necklace neutral at midleft with dissolve

"Rowan sighed."

ro "But, in return, I am to receive a spot at your war table?"

"Werden nodded softly. It wasn’t a strong assent, but it was one worth trusting. Werden was more likely to stab you in the front then a back."

ro "Then I’ll do it. As it is, the kingdom is heading to disaster. You’ve been right this entire time. If it’s what it takes to stop the worst from coming to past, then I will ride with you."

"Werden looked to the side. His praise went unanswered."
"Afterwards, they rode back into the city together. Werden did not talk much for the ride, but Rowan felt a less threatened in his presence, if only a little. But, if he knew what Rowan were truly up to..."

$ werdenAbbeyPlan = True

jump postForkCommonEnding                                                                                                                                                          
                                                                                                                                                           

################################################################################################################
################################################################################################################
################################################################################################################

label lodgePostPathPatricia:

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan woke up bright and early to meet with Patricia. Today was the planned meeting with Duke Werden. So after getting dressed he made his way towards the lodge."
"Now, Rowan was used to taking a little bit longer to get places by foot in the capital. When people recognized him, they always seemed to want to stop and talk. But, he didn’t expect the person who was waiting for him on the north side main street, just outside the codifice."

show patricia annoyed at midright with dissolve

ro "My lady? I had expected to meet at the lodge."

patr "And meet with the Duke without a debriefing first? No no no. "

"When Rowan spotted her, she moved beside him. There was a strangeness to her gait. Her short legs and her tendency to always be scribbling on a piece of parchment gave her movement a loud shuffling noise."

patr "Let me tell you how this is going to go."
patr "The important thing is that you must allow me to do the speaking. It will be unavoidable if he asks you a question, but otherwise you need to keep your mouth shut."

"Rowan raised his eyebrows."

ro "I like to think my skills at the intrigue arts have been on the rise. Surely I could help persuade-"

"Before he could even finish, she had a small hand up towards his face and was shaking her head."

patr "You’ve got a certain baseborn wit to you, I’ll admit. But, that’s of no value with Werden. He doesn’t trust anyone, and he cares greatly who is the one speaking."
patr "You’re a peasant soldier. I’m a lady in the ministry. I will do the speaking when Werden is involved."

"Rowan considered his prior experiences with trying to persuade Werden to do anything. It normally did not end particularly well."

if werdenTalkFailed == True:
    "This was something that he had been reminded of quite recently, in fact."
    
show rowan necklace happy at midleft with dissolve

ro "Alright, you do the talking."

"Patricia made a grumbling noise to herself."

patr "Just remember this isn’t charity."

ro "Of course, I will make sure that you are rewarded for your help here. Greatly."

"Patricia crossed her arms, but did not seem especially taken aback by Rowan’s comment."

patr "Hmpph."

scene bg36 with fade
show rowan necklace shock at edgeleft with dissolve
#patricia shocked
show patricia neutral at midleft with dissolve
show werden neutral at midright with dissolve

werd "No."

"Everyone around the table blinked in surprise. Patricia had barely started laying out her pitch for Rowan’s inclusion in the inner circle of the Purples before Werden had interrupted."
"They were standing alone with him in the large conference room he used as a base. Purple shawled Thorns stood at the doorway, they eyed anyone who approached."

patr "Come again, my lord?"

werd "You wish to foist Rowan on me. My answer is no."

#patricia angry
show patricia annoyed at midleft with dissolve

"Patricia leaned back on her heels as though she were just slapped. She had at least expected to get out her full case."

if werdenTalkFailed == True:
    werd "I considered making common cause with him last he was here. But, his usefulness has passed."
    show rowan necklace angry at edgeleft with dissolve
    werd "You attempted this before. I said no. Do you believe me so forgetful?"
    show rowan necklace neutral at edgeleft with dissolve
    
else:
    werd "I had put Rowan into consideration before. If he wished to work with me, he should have waited for my decision, rather then seeking out new allies to persuade me."
    "He rapped the table with his fist."
    werd "When I say maybe, I mean maybe."
    show rowan necklace neutral at edgeleft with dissolve

show patricia neutral at midleft with dissolve

"Patricia cleared her throat loudly, but there was something different around her when interacting with Werden. Her voice sounded an octave more quiet."

patr "And yet, my lord, you have no hand in city governance. Should the government cede us greater control, I will need an ally by my side in the ministry. Someone to ensure the low folk feel accounted for."
patr "Do you know how hard it is to rule over ingrates?"

werd "I learn more everyday."

"Patricia made a noise like steam was coming out of her mouth. Rowan remained standing to her side. Perhaps letting her do all the talking wasn’t quite working."

patr "Rowan has been a great help to me, already. You need to let him work with us. "

"Werden fixed his gaze on Rowan."

werd "Helping."
werd "Curious."

"Patricia was about to form another answer when Rowan jumped in."

ro "This realm is on fire. I want to do everything I can to make things right. Surely, you see that all of our interests are united here. "
ro "I-"
ro "Hrmm."

"Rowan paused. Werden had not ended the meeting despite his stark refusals. Rowan also knew him to be a shrewer man then he often had credit for. Perhaps another tact might work."

ro "What could I do for you to show my usefulness?"
ro "Lady Crevette insists I’d be useful your cause and to her. Let me prove it to you. Please, My Lord."

"Werden slowly moved backwards towards his chair, and slid down. His eyes didn’t leave Rowan once."

werd "This is exhausting."
werd "You truly vouch for Rowan, My Lady?"

patr "Would I be here if I did not?"

"Another silence as Werden chewed it over. Experience had taught him and Patricia not to disrupt it."

werd "Verdoin Abbey."

"Werden returned to activity, pushing aside one of the maps on the table and pulling out a larger map more focused on the immediate Rastedel area."

werd "It stands near the road to the North East of the city. In Lord Custer’s domain. Strategically important. It overlooks the main pass through to the east."

"Rowan leaned close. He’d never actually done any fighting in the capital region, but he knew most of the major outposts from experience. His military mind came to the fore as he read the different positions and numbers. The map came alive in his mind."

ro "I know it. We have a garrison there, yes?"

werd "Had."

"Werden grabbed a dagger and crossed a delicate X into the map over where the position was marked."

werd "Marianne pulled the troops out after the massacre. We were spread too thin, and the position was expendable. Disaster could have come any day. It still could."
werd "But, it proved a mistake. Some of the Demons’ forces have occupied the building. A band of orcs. We must take it back swiftly to ensure the movement of supplies."

"Rowan mentally noted that he’d have heard if it was the twins forces."

ro "Demons? I hadn’t heard of them on the move that far east…"

"Rowan had to stop himself from speaking further. Best not to give away his inside knowledge on demon plans."
"Still, one thing was for sure. Whoever had taken the abbey did not serve the twins. Perhaps an unattached Orcish tribe?"

werd "Your having heard it matters little. The demon army has a garrison there now and every day they are in place they strangle the city."

"Rowan nodded."

ro "A grievous state of affairs, then."
ro "But, I have to believe there is a secondary motive to it too? A benefit…?"

"Patricia was standing to the side listening, but she was squinting and holding herself in a position with her arms over her chest. This was not her field of expertise."

werd "I must take the abbey before Marianne can."
werd "The holdouts must come to see that only the Thorns can protect Rastedel. If you can be placed front and centre? Even better."
werd "I have a force of my own levies and Thorns waiting nearby the building. Should you prove willing, you will link up with them and personally lead the assault on the abbey."
werd "If you live, I will put you to my side at the parade. The common folk will like that."
werd "But, I might have your casket as a riding partner instead. Verdoin Abbey was adopted as a defensive position for a reason. Many may die in the process of taking it."

"Patricia’s face suddenly went white."

patr "Wait-"

ro "That is what I must do to prove my loyalty?"

"Rowan didn’t hesitate. He had a mission to complete and this was necessary to do it. Besides, Rowan was blessed and cursed with more tools in this scenario than the average man."

ro "Then, I’ll do it. I’ll capture the abbey for you."

"Werden gave a terse nod, then made to roll up the map. Patricia remained frozen in place, still processing what had just happened."

werd "I will inform my commanders to wait for your arrival. "
werd "..."
werd "That should be all."

"Rowan looked to Patricia. She was still stuck in place trying to put words to what had happened. Not that it mattered. Werden had said his piece."

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve
show patricia annoyed at midright with dissolve

"They were back on the north side of the bridge now. The clack-sound of Patricia’s shuffling walk only grew louder to match her frustration."

patr "That fucking..fucking...ahhh."

ro "My lady?"

patr "He knew! He knew you were going to ask to prove yourself! He was always planning to send you to take the abbey for himself! Why do you think he already had a plan for what to do the moment you asked!?"

"Rowan nodded along. Of course, it really could have been an improvisation, knowing Werden. But, best not to say that here and now. Holding his tongue was another skill he’d learned a great about over the past year."

patr "The bastard. You’re no good to me dead. But, he gets as much from you as a martyr as he does a living ally."

show rowan necklace happy at midleft with dissolve

"Rowan chuckled to himself."

ro "I’ll just have to be sure to survive then."

show patricia happy at midright with dissolve

"His companion laughed too, if only lacking a bit of Rowan’s surety."

patr "You better. If I have to plan a war without help, I will personally make sure that your soul never gets an ounce of rest."

$ patriciaAbbeyPlan = True

jump postForkCommonEnding                                                                                                                                                          
                              
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

label werdenCoup:

$ werdenCoupTalk = True

scene bg36 with fade
show rowan necklace concerned at midleft with dissolve

if avatar.corruption < 61:
    "Just outside the door to Duke Werden's personal meeting room, Rowan had to stop himself. He felt woozy. He closed his eyes and let himself lean against the wall. Something felt wrong."
    "He had to slow down his breathing. Breathe in. Breathe out. One step at a time, he regained his composure."
    #show thorn knight
    show rosarian knight neutral at midright with dissolve
    rkn "Is there an issue, Mr. Blackwell?"
    show rowan necklace neutral at midleft with dissolve
    ro "No no. I'm alright. Just had to stop for a second."
    hide rosarian knight with dissolve
    "He mustered the strength to push on into the room."

else:
    "Rowan walked boldly down the hallway down to the room where Werden had been encamped before. Only now, he was an invited guest."
    
show werden neutral at midright with dissolve
show patricia happy at edgeright with dissolve

werd "Good of you to join us. Let's get started."

if rastAlly == "crevette":
    "From her corner of the room, a few seats away from Werden, Patricia gave Rowan an encouraging smile."
    
"Numerous nobles and military men took positions around the table. Many were listening to Werden, but some quietly whispered amongst themselves, sometimes pointing at the massive map on the table."
"Rowan had to note who was not in the room, however. No Duke Raeve."
"It was that same map that held Rowan's attention. A massive reproduction of the city labeled down to individual boulevards and roads. The north side held the commoner districts, the trade districts, the Codifice, and the slums."
"The South East the merchant districts, the artisan districts, and the professional buildings. The South West, meanwhile, held the noble quarter, the gardens, and the large estates. "
"This segment of the map was covered in smaller notes and markings. Most of them centered on a specific building."

show rowan necklace shock at midleft with dissolve

ro "...The palace."

"Rowan brushed his hand over the map."

werd "Yes, the subject of our current meeting."

"Werden turned back to the table as a whole."

werd "The parade proved a good opportunity. Lord Liftford was so impressed by the display he's expressed a desire to participate. He provided us with new details about the guard schedule."
werd "With this latest development, all of the lords involved in the palace's defense has been turned. However, the commoners and clerical figures involved are..."

ro "Participate? Participate in what?"

werd "The Coup."

"Rowan nodded slowly. He'd known that Werden was considering some way to take power. But, hearing him, in his own words, admit that he was planning a coup still felt wrong."
"Rowan looked down at the map. These plans were detailed. The product of weeks of work. Definitely not recent enough to have been started after the Battle of Astarte Plain. How long had Werden been waiting for this?"

if avatar.corruption < 31:
    "...The end of the world. Or at least, a world."

patr "Marianne rules through the Baron and her monopoly of the council of state. But, many of us lords have been in agreement for some time that she had no business controlling so much."
patr "But, we didn't use to have anywhere near as much support for the idea of removing her. Then she went off and got the entire city's defenses killed."
patr "Even now, she refuses to take Werden's levies because she knows it would be the end of her power. Her greed is putting the entire region at risk. Killing her would risk open conflict with the holy city, but she must be taken into custody."

show rowan necklace neutral at midleft with dissolve

"Rowan rubbed his chin. The chaos of a coup like this could be the opportunity that the demons had waited for. Still..."

ro "What about the Baron? He's innocent in all of this."

show patricia annoyed at edgeright with dissolve

"Lady Crevette opened her mouth to answer when Werden cut her off. She was left to scowl silently."

werd "He can stay. His heirs are in our orbit. But, replacing Marianne at his side with one of us is a cleaner cut. The common people still love their liege lord."

"Rowan's eyes drifted to the south east. All the bridges in and out of the district, as well as the gates and guard posts had all been labeled as strong points that needed to be seized. They were treating Jacques' stomping grounds as enemy territory to be occupied."

werd "You wished for a seat at the table and a role in future discussions. This is the table you are sitting at. This is what we are discussing."
werd "The current system cannot survive much longer. There must be a rebirth of order."

if avatar.corruption < 61:
    "Rowan took a deep breath. This was what was required of him."
    if serveChoice == 4:
        "And if it meant the destruction of a corrupt regime in the process, that wasn't the worst outcome."
        
ro "Yes...Of course. What is my involvement in the coup to be?"

werd "The spearhead. You will aid me in the assault on the palace itself. There is no more able man for the task."

"Rowan leaned back in the chair. If he was in the spear head, it would mean he'd have to confront Marianne himself."
"It was not a thought Rowan relished. Priests of Solansia were no helpless victims. They could empower their retinue to incredible feats and even alter space itself. Rowan could still remember the holy stones, boulders larger than men, being flung towards the demon army."
"If Marianne put herself at the head of the counter coup faction, the streets would become littered in corpses."

werd "Now then..."

show patricia neutral at edgeright with dissolve

"The idea was to take control of the capital as fast as possible. A quick strike into the palace at a time where the Baron and The High Arbitron were there. Catching Marianne fast, and without her full retinue, were imperative. If she remained to organize a resistance, the coup would fail."
"The second stage would be to put friendly troops at all of the strong points, bridges, garrisons, and major roads. The flow of people to the South Western Noble Quarter needed to be suppressed. If they moved fast, they'd catch Marianne, The City Guard, and the Coppers with their pants down."
"The final stage would involve the movement of an army from the land of the Duke and other armies into the city. They’d move fast and be in the city within days. Soon enough to secure it and ensure it was well defended."
"A good plan. But, Rowan saw the exploitable problem instantly. The main resistance that Werden assumed was Jacques. There was nothing accounting for a sudden strike by the demons."
"The others around the table debated the nuances of specific segments of the plan. Most of them were sword nobles. Military men who could be counted on. The softer sort, like Raeve, were clearly not privy to the details."
"That Lady Crevette was here suggested she'd be taking over government function immediately after the coup was launched. Or perhaps she was quarter-mastering it. Rowan wasn't sure."
"Rowan simply focused on the map for most of the meeting though. Where each troop detachment was going to go. He didn't have the luxury of documents. He needed to memorize all of it if he wanted to bring it back to the twins."

if rastAlly == "crevette":
    "He was so focused on the map, he didn't notice a small scrap of paper being pushed into his hand. A note from Patricia to meet her after the business of the meeting was done."

werd "We have reached the end of our business. Remember, you have a few weeks until the plan goes into effect. Any later and we will risk Prothean Reinforcements arriving. You will all be ready in time."
werd "The meeting is adjourned."

"Rowan rose to leave the room. Patricia was already shuffling out, amidst the crowd of well dressed men."

hide patricia with moveoutright

werd "Rowan. Wait."

"Rowan turned back."

ro "My Lord?"

if rastAlly == "crevette":
    #werd angry
    werd "Men who are too talkative do not have long lives. Are we clear?"
    ro "Yes, My Lord."
    #werd neutral
    "Werden judged him critically for a minute. They were on the same side, at least in theory. But, the tension couldn't hide their true relationship. Finally, Werden waved him off."
    werd "Go."
    
else:
    #werd empathetic
    werd "I am putting my faith in you. That is rare. Do not abuse it."
    hide werden with moveoutright
    
if rastAlly == "crevette":
    jump postCoupPatricia
    
else:
    jump postCoupWerden
    
label postCoupPatricia:

scene bg36 with fade
show rowan necklace neutral at midleft with dissolve
show patricia happy at midright with dissolve

"Back in Patricia's office, he found her where he expected roughly. Popping the cork off a bottle of wine. There was a glass waiting for him on the other side of the table."

patr "There you are. You had me worried when you didn't follow me out."

"He gave a short bow."

ro "Pardon, My Lady. Werden wanted to talk to me."

patr "Oh? What did the old man want to say?"

ro "He just wanted to remind me that it would be my death if word got out."

show patricia annoyed at midright with dissolve

"Patricia swished down her drink and then set to pour another glass."

patr "That's just like him. The most in-demand hero in all of the realm gloriously retakes a key strong point from the Orcs in his name, and the only congratulations he can muster is a death threat."

"Rowan grabbed his glass of wine from the table."

show rowan necklace happy at midleft with dissolve

ro "Is that what this is then? A congratulations?"

patr "Yes, you idiot now drink with me."

show patricia happy at midright with dissolve

"About an hour and two thirds of the bottle later, things had loosened up some. Rowan was significantly less drunk then his companion, however."

ro "I know there is bad blood between you and the High Arbitron, but how do-"

"Patricia waved her hand dramatically in his face, nearly knocking the glass straight out of his hand."

patr "No no no. Work talk is over for the day. It'd be near treason to let alcohol this expensive get wasted on that nonsense."

"Rowan backed up slightly and looked down in the glass. Rowan could tell the tracks of a fawn from a buck. But, telling the difference between expensive wine and cheap wine was beyond him. It was all red and made your head fuzzy."

ro "Just how expensive are we talking about?"

patr "Give or take a small village. Drink up."

"Rowan wasn't totally sure if she was joking. He finished his glass regardless."

if rastPerformanceReview == True:
    show rowan necklace neutral at midleft with dissolve
    "Rowan had to struggle not to think about the unopened parcel waiting for him back in his room."
    "For all of her oddities, she was fun to be around while drunk. It revealed an edge that she normally had to hide. Would she keep it even after Jezera's magical object “changed” her?"
    "It was not a pleasant thought."
    show rowan necklace happy at midleft with dissolve
    
ro "How about this then."
ro "Have you ever been married before? It's hard not to notice that you still go by your father's name. You have an older sibling too, as I recall, so you're not the owner of your own estate."

"She slumped back in her chair with an overwrought sigh."

patr "Almost. Three times, in fact. But, that was some years ago."

"Rowan raised an eyebrow. This sounded like the start of useful information."

ro "Oh? Why almost?"

patr "Because they were all idiots."
patr "I was quite the little morsel back in the day, believe or not. All the boys wanted a bite, but I was picky."
patr "Perhaps a bit too picky."

"Rowan offered a warm smile."

ro "You speak in the past tense, My Lady. You're still quite the morsel."

"Suffice to say, the response Rowan expected was not for Lady Crevette to throw a pen at him. Granted, Rowan was easily able to dodge the slow moving projectile."

patr "Hush you."

"Rowan laughed again, perhaps with a slight assist from the alcohol."

ro "I'm not kidding. You've gained a few pounds, I'm sure, but your features are still beautiful. You should have a battalion of suitors even now."

patr "The only thing I'd do if I had a battalion would be shore up the city's defenses. Good battalions are hard to find these days, apparently."

show patricia sad at midright with dissolve

"The Lady looked to the side. A slight shadow fell over her features."

patr "What about you? You're trying to charm a drunk old lady, but you have a wife yourself I assume?"

"Rowan took another sip from his glass. The less he spoke of Alexia here, the better."

ro "She lives still, but not in the realm anymore. It would take many weeks ride to reach her. The war did this. She's not safe, so she's not in Rosaria anymore."

"Patricia nodded along as he spoke."

ro "It makes me think about who I was all that time ago. I've lost a lot."

patr "I didn't take you to be a mopey drunk. Think about what might happen after we win. No more Marianne lording about because she's fucking the Baron. You'll get to command the city garrison. Maybe then you can even bring your wife back. Who knows."

"Without warning, she grabbed her drink and hoisted into the air. A little bit of wine splashed on the table."

patr "To who we used to be."
patr "And who we'll be when all this is over."

"Rowan slowly raised his glass, and clinked it against hers."

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

label postCoupWerden:

scene bg36 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan wasn't able to return right to Ameraine after the meeting. Someone wanted to speak to him."

quest "Wait!"

show rowan necklace shock at midleft with dissolve
show juliet happy at midright with moveinright

"Rowan turned away in the main room to find Juliet, Werden's daughter approaching. Rowan raised an eyebrow. She'd never outright approached him before."

juli "Sir Rowan. I had to speak to you before you left again for the front."

show rowan necklace neutral at midleft with dissolve

"Rowan bowed softly. If Rowan wished to remain in Werden's good graces, rudeness to his daughter was not the way. Besides, she had an earnestness to her that it would be far too rude to crush."

ro "My lady. You can rest easy on that account. I am staying to participate in the city's defense for the foreseeable future."

#juliet embarassed
juli " Oh...I See."

"An awkward second passed as she straightened her dress and then her back."

show juliet neutral at midright with dissolve

juli "I simply wanted to explain to you that...that what you do is simply incredible. I was with Father when he got the news. I hadn't seen him so happy in a long time…"

show rowan necklace shock at midleft with dissolve

"He hadn't expected that answer. Duke Werden, happy? As far as Rowan knew, the man had taken the news of Bloodmeen's fall without so much as cracking a smile."

ro "I doubt that. I've never seen your father smile in my entire-"

"Juliet shook her head emphatically. The most forceful display she'd ever put on in front of him."

juli "Father is a hard man. He's lived a hard life. Some of my handmaids and friends speak of him as though he is made of stone."

#juliet sad
juli "But, he gets happy. He gets sad. He simply does not like the...help...of others."

"Rowan had to shake the shock from his face. That was new. He had to pull back his composure to continue the conversation. A crack in his performance."

show rowan necklace neutral at midleft with dissolve

ro "You must have a unique vantage point, my lady."

juli "I suppose I do."
juli "Still."

show juliet happy at midright with dissolve

juli "Your support has truly brightened his mood. For that, I thank you."

"Rowan bowed once more."

ro "I take your thanks humbly."

juli "Lady Delane speaks of you often. I have heard that her rescue was quite the feat of cunning."

show rowan necklace happy at midleft with dissolve

"Rowan laughed to himself."

ro "I don't know about that. Outsmarting orcs is not a sign of brilliance, my lady."

juli "You speak of it as though it were routine."

ro "I wouldn't go that far."

"Her face brightened into an excited smile. Her hands clasped together into a prayer. It was as though she were begging him."

juli "But, you must have incredible stories then, right? Other feats of valor of that you've accomplished?"

"A shadow crossed Rowan's face, but he kept on smiling. Juliet seemed none the wiser."

ro "Feats of valour. Heh."
ro "I suppose I do."

"A lull set into the conversation. Juliet looked like she had something she wanted to say, but was struggling to get it out. So Rowan helped her."

ro "Would you like me to tell you a few stories at some future time? It wouldn't be any trouble."

juli "I'd like that."

"Juliet beamed at him with eyes alight. Rowan ran a hand through his hair. It wasn't like he could refuse. More to the point, she knew more about her father than anyone." 
"If Rowan wanted to manipulate events, having Juliet on his side feeding information would be invaluable."

if avatar.corruption < 31:
    "And what was one more sin on his conscious at this point?"
    
elif avatar.corruption > 31 and avatar.corruption < 61:
    "It was regrettable, but perhaps unavoidable."
    
else:
    "Rowan wasn’t about to give up a single advantage anymore. And the ear of Juliet was an advantage."

"This is the end of the current Rastedel content."

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

label act4Menu:
    
scene bg36 with fade

menu:
    "Visit Lady Delane" if eleaConvo == True and delMeet2Seen == False:
        $ released_fix_rollback()
        jump delaneMeeting2
        
    "Visit Juliet." if clubbingSealSeen == False:
        $ released_fix_rollback()
        jump clubbingSeal
        
    "Visit Juliet again." if julietSexAvailable == True:
        $ released_fix_rollback()
        jump bedroom_window
        
    "Visit Patricia" if rastAlly == "crevette" and sternCouncilSeen == False:
        jump sternCouncil
        
    "Visit Patricia again." if sternCouncilSeen == True and guessWhoSeen == False:
        jump guess_whos_coming
        
    "Leave.":
        $ released_fix_rollback()
        jump rastMenu

##################################################################################################################################

label delaneMeeting2:

$ delMeet2Seen = True

show rowan necklace concerned at midleft with dissolve

"Rowan quietly asked around the lodge if Lady Delane had been around recently. It would not be good for him to seem too eager. But, the fact they knew each other, at least, was common enough knowledge. So it could not be that much of a mistake."

nobwom "Lady Eleanor?"
nobwom "You know, I don’t think she’s here at the moment. Eleanor can be rather elusive at times. Never know where she is. Haha."

"Rowan was left to walk away dejected. Delane was the one he was here to see. There was something important that he had to tell her."

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan left the lodge, hoping to return to the northside to make something of the day. Even if he couldn’t find Lady Delane, he still had too much work for idleness."
"But, it became apparent rather swiftly that something was off. At first, it was merely a lingering unease. Rowan’s sense of danger going off."

show rowan necklace angry at midleft with dissolve

"Someone was following him. It took him a few streets to work it out. But, there was a short figure shrouded by a cloak who was keeping a few paces behind him. Rowan narrowed his eyebrows. Whoever this was, they were not subtle enough." 
"Rowan turned into an alley. The stalker followed him."
"Then, Rowan pounced."

stalk "Wait. Ah. Stop. Stop."

"Rowan narrowed his eyebrows and pinned them towards the wall with a single hand. He didn’t want to hurt anyone. If he didn’t have to."

ro "Why are you following me?"

stalk "You can be quite the fool sometimes. We cannot be seen together too often. You know that Even your asking around has consequences, you know. "
stalk "Now, would you be so kind as to remove your oafish hand?"

show rowan necklace shock at midleft with dissolve

"Rowan drew his hand back. The figure lowered her hood just enough for him to see the waterfalling black hair beneath."

show eleanor dress neutral at midright with dissolve

ele "Really now. You’re certainly more adept then you were in the past, but you must be more careful."

show rowan necklace happy at midleft with dissolve

"Rowan sighed. He hadn’t recognized her before because of the heavy cloth cloak she wore over her clothes. Indeed, even up close, he couldn’t tell what she was wearing underneath. The hood had also been large enough to obscure her features."

if rastAlly == "werden":
    ro "We’ve met in public before, My Lady. Are such dramatics really necessary?"
    "She rolled her eyes."
    ele "It’s not the presence or absence of meetings. It’s the frequency of it. I’ve already been asked about how close we are on a few occasions. The theatrics in your plea to the Duke did not help."
    
ro "..."
ro "Truly, it’s good to see you, My Lady."

show eleanor dress happy at midright with dissolve

"Lady Eleanor smirked and gave a tiny curtsey."

ele "Likewise!"
ele "Now then, shall we? Best not to talk here. If someone were to walk past, it could be an issue. If the optics of a meeting at the lodge are bad, surely you can imagine the optics of being seen cavorting secretly in a dirty alley."
ele "I had planned to follow you to wherever it is you’ve been staying."

"Rowan chuckled to himself."

ro "Are you sure? It’s not so much the type of place that many high born ladies, such as yourself, tend to visit."

"Delane groaned and made a gesture with her hands urging him onwards. The sleeves of her cloak were so long that the ends still hung down even with her arms fully outstretched."

ele "Have you forgotten where we met already? I assure you, I can handle whatever filthy tavern you select, provided there aren’t any orcs around."

"Rowan could not argue with that logic."
"Rowan and his companion made their way steadily north towards the inn that Ameraine had selected for him. Lady Delane stayed far enough back to not obviously connect the two together, but not so far that Rowan couldn’t reach her if needed."

scene bg40 with fade
show eleanor dress happy at midright with dissolve
show rowan necklace happy at midleft with dissolve

"At last, they made their way back where Rowan was staying. Delane went straight to the window and looked out at the city’s backroads stretching towards the river."

ele "A nice place, I suppose."

ro "That’s a lie,"

ele "It is. But, do you expect me to call it a filthy hovel? I assume being out of the way is what you sought after. A bit of mystery, perhaps."

"Rowan nodded softly."

ro "I rather like my privacy, you know. I was in the army. I slept on dirt for years. "

"He turned away to undo the straps of his sword belt. He wouldn’t need it if he was just alone with Elanor. But, when he turned back to her, he found that Delane had already worked her way out of her cloak."

#cg 1
scene cg767 with fade
show eleanor dress happy behind cg767
show rowan necklace happy behind cg767
pause 3

ro "..."

"Delane stood in front of the window, clad in brilliant blue silk. It hugged her curves and danced nearly to the floor. The outfit was so see-through that her body was on full display behind its billowing material." 
"The mere hint of it behind the veil made it all the more attractive. Much like how a single drop makes you want a drink more for the single taste."

if delaneLodgeSex == True or eleanorCaveSex == True:
    "Rowan stirred."

scene cg768 with fade
show eleanor dress happy behind cg768
show rowan necklace happy behind cg768
pause 3

"He took a step closer."

ele "The view here is so fascinating. The only sights I normally receive here are the mansions of the others in the South-West Districts. This is so chaotic and dirty."
ele "But, not unpleasant either. Fascinating, like from a storybook about paupers or nobles in disguise. Today, I’m the disguised noble."

"She turned back to him with the slightest of smiles. Then she noticed how Rowan was looking at her. Her smile wasn’t so slight after that."

ele "You like it?"

"She did a little curtsey."

ro "You’re stunning…"

scene cg769 with fade
show eleanor dress happy behind cg769
show rowan necklace happy behind cg769
pause 3

"Lady Delane blushed softly."

ele "...Thank you…"
ele "I wanted something special...for when I saw you…"

"She wrapped her arms around her chest, hugging her sides. The city stretched out behind her in the window."

if delaneLodgeSex == False and eleanorCaveSex == False:
    ele "This isn’t the first time I’ve tried to bring you to bed. I decided...I decided that if I wanted you, I needed to put in efforts of a greater caliber. "
    ele "Anything less would not do."
    ele "So...will you do me the honor, Rowan? "
    "She moved her hands behind her back. A posture that conveniently left her breasts pushed forward. A natural spot for Rowan’s eyes to fall on."
    ele "Rowan Blackwell. Will you fuck me?"

else:
    ele "I understand what is expected of me. That I am to find a noble husband and to work with him. That the good of our family depends on it. I am not the first born, after all."
    ele "You are a commoner...and yet, you saved me. You challenge me."
    ele " I want you again. I think about it often. As stated before, you were the motivation for this particular purchase."
    "She did a little twirl in place, showing off the luxurious style of the dress...and beneath her own luscious curves. She was eager for him. He could see it from her body language. He could even smell it in the air."
    ele "I don’t know what day it won’t be possible for us to meet anymore. You are a busy man. A married man. "
    #if rowan had a date with juliet: #to do
        #"She looked to the side. Her face flushed with something. Not arousal. Something else."
        # ele " ...you are the crush of, my lady. The one who I owe loyalty towards. The very liaison is a small treason."
    ele "Someday, I will not be able to meet with you."
    ele "ut, not today. Stay with me today. Let’s spend the entire day in bed together."
    "She reached out a hand to brush his face. "
 
menu:
    "Take Delane to bed.":
        $ released_fix_rollback()
        $ delaneSex2Refuse = False
        jump delaneSex2
        
    "Refuse.":
        $ released_fix_rollback()
        $ delaneSex2Refuse = True
        jump delaneSex2Refuse

label delaneSex2:

scene cg770 with fade
show eleanor dress happy behind cg770
show rowan necklace happy behind cg770
pause 3

"Rowan took a step forward and kissed her. A passionate possessive kiss. Eleanor’s eyes fluttered closed, and she eagerly opened her lips for him to explore. She was as active and as eager a participant as he was."
"When the kiss broke, she let out the smallest of gasps. Her eyes burned into him."

ro "Ladies first."

scene bg40 with fade
show eleanor dress happy behind bg40
show rowan necklace happy behind bg40

"Rowan swept her up into his arms and deposited her on the bed. She squealed lightly and kicked her feet, but Rowan didn’t give her playful struggle any mind. She looked up at him expectantly from the mattress. He hovered above her. So little distance between them."
"Her face asked a silent question over and over. When are you going to do it? When are you going to fuck me?"
"But, Rowan froze in place for a moment. There was something important he was supposed to do. Something he needed to tell her..."

ele "Rowan? Is there something amiss?"

"Rowan put on a smile to reassure her. "

ro "Nothing at all."

scene cg771 with fade
pause 3

"Rowan put his hands on her body, and his cock inside of her. Delane let out the softest of gasps. Then she grasped on to him. Their bodies were connected in more ways than one now. They gasped at the same time. Connected."

scene roxdel_lodge2 with fade
show eleanor dress aroused behind roxdel_lodge2
show rowan necklace happy behind roxdel_lodge2
pause 3

"Sunlight streamed into the room. It illuminated their bodies in movement. The city overlooked them."
"Rowan’s hands roamed the soft silky fabric of Delane’s dress. It was beauty over beauty. He tracked the way she squirmed when he thrust his cock. He’d speed up or slow down to acquaint himself with the different reactions."
"The small movements. The way her mouth would open to gasp. The little whimpers from her lips. It made him groan too."

if eleanorCaveSex == True:
    "Once they’d fucked one another, sweaty and exhausted, in a damp cave. This was different. The woman he was with now was so fine. All his life he’d been told the nobles were above him. She was a being of grace and perfection. Flawless."
    "And he got to fuck her…"

ele "Rowan…"

"She groaned out and grabbed back at him. He responded with a loud grunt and by pistoning his hips as hard as he could. He rolled and thrusted with every well of strength he had."

ele "Rowan...Rowan…."

"Her cries grew higher pitched. A symphony for his ears. Just for him. It drove him to fuck her harder. It was single minded desire. He wanted her. This sweet, perfect woman whose body met his. He wanted her."

ele "Rowan...ahhh. Fuck. Rowan. Fuck."

"He set the pace. The sight of her in all of her perfection drove him to greater extremes. He’d pull her hair, and her lips would form a perfect O. He’d drive his cock as deep inside of her as he could, and her body would act as the perfect foil. Pleasurable resistance."

scene roxdel_lodge2_2 with fade
show eleanor dress aroused behind roxdel_lodge2_2
show rowan necklace happy behind roxdel_lodge2_2
pause 3

"And as it went on. As they both moved steadily closer and closer and closer to that building pressure. Rowan smiled. It was not on purpose. A natural response to the situation. But, he smiled nonetheless."

ele "Rowan. I...I...Rowan...Inside me. Please...Rowan…"

"Her body twisted and shuddered. She threw herself at him in a desperate desire to eke out every last undiscovered sensation. She was so wanton. So needy. There was something bottled up that was being let out."
"It took on an unbroken rhythm. The moment broke down to its smallest components."
"He moved and she moved. He moved and she moved. Over and over. Sublime. Like the rush of water over a waterfall. He moved and she moved." 
"He asked and she answered."

"Flawless. Moaning and thrusting. Flawless. Squealing and slapping and moving. Flawless. The dirtiness of sweat and flesh and cum. The clean of a freshly tailored dress. Flawless."
"Moving and moving and moving. Faster and faster and faster."
"He smiled. Even as he approached the peak, he smiled. She had reached her heated edge. He was hurtling down the waterfall. He just needed to...let go."

#cg 2 var 2
show cg785 with sshake
show cg785 with sshake
pause 1
show cg786 with flash
pause 3

"Rowan came inside of Delane. Her body spasmed the entire time. Their forms were connected, and so too their orgasms."
"His hands gripped the pristine dress with everything they had. He heard a ripping sound, but his brain was too far bathed in white to process it. Everything was in white."

scene cg770 with fade
show eleanor dress happy behind cg770
show rowan necklace happy behind cg770
pause 3

"They groaned in unison. All strength had been sapped from Rowan’s body. He lowered himself, as slowly as he could, down on top of her. Their lips were mere inches from each other."
"Every time she exhaled, he felt the warmth of her breath against his cheek." 
"She was soft and delicate, intertwined in his arms. It was a moment of indeterminate length. As long and as short as it needed to be."

ele " Rowan…"

"Her eyelashes fluttered. His chest expanded and contracted. He too needed air. The exertion had left him winded. It didn’t normally do that."

ele "Rowan…"

ro "Yes…"

ele "...You ripped my damn dress."

"Rowan looked down. There was a noticeable tear running through it. Before it had been so totally smooth and perfect. He let out a grunt. That was, in a strange way, kind of sad. He’d never again be able to see it like he had before. Even repaired, the stitches would remain."

ro "Sorry."

ele "Impudent bastard."

"She brought her lips to his for a kiss."
"They remained together for a time. Just enough to get their breath back. Rowan held her in his arms. Their position shifted slowly until they sat side by side."

scene bg40 with fade
show rowan necklace concerned at midleft  with dissolve
show eleanor dress happy at midright with dissolve

jump postDelane2Sex

label delaneSex2Refuse:

"Rowan watched passively, drinking in her form. It was all such a provocation. A perfect enticement. From her flowing hair all the way down."
"That was why Rowan had to refuse."

if delaneLodgeSex == False and eleanorCaveSex == False:
    ro "My Lady. This is not the first time you’ve attempted to seduce me. I’m afraid you will find little success on this occasion as well."
    "She crossed her arms."
    ele "Really now, have I become so unattractive that I cannot even tempt you?"
    ro "I wouldn’t say that…"
    "She huffed slightly...then without warning, her hands went to the hem of the dress and pulled it up. Rowan could only gawk as the woman in front of him now."
    show eleanor dress neutral at midright with dissolve
    "From there, she slowly walked over to the bed, grabbing Rowan’s hands and leading him to a seated position at her side. So close he could smell her perfume. Beneath that, her feminine musk."
    show rowan necklace concerned at midleft with dissolve
    ele "You’ve made me give up pretenses to subtlety. I pride myself in my ability to seduce without resorting to such extreme measures. But, you are a defiant man."
    "Rowan closed his eyes. Not, to avoid looking at her, but instead to draw the strength to say what needed to be said."
    
else:
    ro "My Lady, I cannot do it. Not today."
    "She raised an eyebrow."
    ele "Really?"
    ele "I know you find me attractive, Rowan. And I even came all dolled up for you. Surely, I can persuade you to change your mind. Somehow."
    "Without warning, her hands went to the hem of the dress and pulled it up. Rowan could only gawk as the woman in front of him now."
    show eleanor dress neutral at midright with dissolve
    "From there, she slowly walked over to the bed, grabbing Rowan’s hands and leading him to a seated position at her side. So close he could smell her perfume. Beneath that, her feminine musk."
    show rowan necklace concerned at midleft with dissolve
    ele "Do you wish for me to go to my knees and beg? Some men enjoy that."
    "Rowan had to force his eyes away. He couldn’t let himself indulge."

label postDelane2Sex:

ro "My Lady...there is something I must tell you."

show eleanor dress concerned at midright with dissolve

"She tilted her head slightly."

ro "I wasn’t looking to meet with you today because I wanted a liaison."

if delaneSex2Refuse == True:
    show eleanor dress neutral at midright with dissolve
    ele "Clearly."

else:
    show eleanor dress happy at midright with dissolve
    ele "You could have fooled me."
    "She giggled playfully."
    ele "But, why did you seek me out then?"
    
"Rowan breathed in. He’d been preparing for this moment. But, none of his preparations felt real. This felt real."
         
ro "I wanted to see you, so I could tell you to leave the city. It is no longer safe for you in Rastedel."

show eleanor dress concerned at midright with dissolve

"She blinked twice."

ele "The city…?"

ro "Is no longer safe for you. Yes."
ro "It’s time for you and your family to decamp for the countryside. If you have holdings or the capacity to acquire holdings on the other side of the mountains, that would be best. Closer to Prothea."

ele "..."

"She drew back from him slightly, and curled her arms around her knees in a ball position. He could see her intellect whirring to life beneath her."

show eleanor dress neutral at midright with dissolve

ele "You’re involved in the city’s defenses…"

if rastAlly == "jacques":
    ele "The Coppers as well..."

else:
    ele "The Purples as well..."

ele "If you’re telling me that I need to leave the city, that means something is about to happen, doesn’t it? You know about something that you don’t want to talk about."

"Rowan lowered his head. He couldn’t meet her eyes right now. It might give away too much."

ro "I gave everything I had to get you free from the orcs. After everything that happened, I cannot risk you falling back into their hands. It would take away too much that I worked for."
ro "Rastedel isn’t safe. You need to go."

show eleanor dress angry at midright with dissolve

"Delane’s eyebrows furrowed. Her movements turned sharp."

ele "Yet, you still don’t answer me. You know something. You can’t hide it." 
ele "..."
ele "Why were you at that orc encampment?"

"Rowan felt a tingle down his spine. That was the exact right question to ask. Which made it the exact wrong question to ask."

ele "I have not heard of any reconnaissance effort during that time. It was lands adjacent to my family, and we are held in esteem by the Duke. It wasn’t for him. Nor was it for anyone here. Why were you even there?"

"She rose to her feet, but her glare never left him. She soon was pacing the room, barely aware of her own nudity."

ele "And before the Astarte tragedy...you were trouncing around Raeve territory doing what exactly? No one can account for your whereabouts. I’ve even spoken with Duke Raeve about-"

show rowan necklace neutral at midleft with dissolve

ro "You need to leave Rastedel, My Lady. I really cannot say more than that."
ro "I am trying to help you. This is the only way."

"Lady Delane went to his table and grabbed the paper from it. She tried to throw it at him, but the paper mostly scattered to the wind."

ele "No. You listen here. You saved me. I care about you. But, do you really think you can just tell me to run away without evidence? To convince my own father to uproot and travel to the other side of the country?"
ele "I’m not stupid, Rowan. I’m not."
ele "You’re hiding something important. Tell me what’s really going on."

"Rowan balled his hand into a fist. He could see how close she was to figuring it out. There really was so little he could do to account for what he’d been doing ever since the conflict began. But, he needed to do something now. Something to head this off."
"The man closed his eyes and took a breath. Then he stood up."

ro "You want the truth?"

ele "Yes. "

ro "Okay."
ro "..."
ro "I am a double agent."

show eleanor dress concerned at midright with dissolve

"Delane froze in place."

ro "For a little more than a year, I have been going back and forth between the lines. I have met the demons who run the other side personally. As far as they are aware, I am on their side."

ele "Are you?"

if avatar.corruption < 31:
    ro "Never."

else:
    ro "No. I am not."

ro "I was at Raeve Keep when it fell because I was with the attacking forces. That is how I got the Duke out."
ro "I was at the Orc Camps because the demons were there to make an alliance with them. That’s how I learned about you. I knew I could not let them do what they wanted with you. I risked everything to save you."

"She gasped softly."

ro "I am doing everything I can to put a bottle on this monster. But, no matter what I do, it always gets out. All I can do is mitigate it here and there. All my efforts just make the situation worse."

"Rowan paused to gather his breath. Lies always went down easier when taken with truth."

ro "That is why I am telling you that you need to leave this city."
ro "I have seen how it is defended. I had heard about the state of the in-fighting, but I had refused to believe it. Everyone is so busy trying to slit each other’s throats that none of them have a damn clue how to save this entire country."
ro "I have seen every stupid choice. I was at Astarte. The reason it was such a disaster was that all of the selfish noble power brokers were too busy fighting each other to focus on the real enemy."

if serveChoice ==4:
    show rowan necklace angry at midleft with dissolve
    ro "This entire society is rotten and dying. I don’t know what should replace it. Not yet. But, it cannot and will not survive this war."
    show rowan necklace neutral at midleft with dissolve

ro "I cannot stop what is happening. There are going to be orcs inside these walls. My bet is that it’s going to happen soon."
ro "You need to leave."

show rowan necklace concerned at midleft with dissolve

ro "Please…"

show rowan necklace neutral at midleft with dissolve

"A hush fell over the room. The shadow of the Codifice, standing tall in the distance, darkened the room. Rowan was left face to face with Eleanor."

show eleanor dress neutral at midright with dissolve

ele "And if I stay, they’ll take me…"

ro "That’s right."

ele "..."

if rastAlly != "werden":
    "Rowan saw something he hadn’t seen in a long time. Not since the Orc Camp. A tear rolled down Lady Delane’s cheek."
    ele "This explains a great deal. I will admit, I had even considered the possibility before. But, to hear it from the mouth of the demon himself."
    show rowan necklace angry at midleft with dissolve
    "Rowan furrowed his eyebrows."
    ro "I’m no demon."
    ele "Correct, you are no demon."
    ele "But, you don’t have a shred of hope for victory left in you. You want to pack your cart and run rather than stand and fight."
    ele "What you are is a coward."
    if avatar.corruption < 31:
        show rowan necklace concerned at midleft with dissolve
        "Rowan’s eyes fell towards the ground, almost instinctively. Delane had always been cuttingly direct. But, to lay it out like this…"
        "A coward…"
        ro "You’re right. I am."
    else:
        "Rowan felt a flash of something hot boiling inside of him. He imagined giving Delane the back of his hand."
        ro "Me? A Coward?"
        ro "Do you have any idea what I have done to get where I am? The sacrifices I’ve had to make? Every step of my path to this room has been over ashes. Can you even imagine what I have done for the greater good?"
        "Delane, though, stood her ground even as his voice went higher and higher."
        ele "I don’t have the slightest idea what you have done to get here."
        ro "And you remember what I did for you? I risked everything. Everything. Just to save you?"
        show eleanor dress concerned at midright with dissolve
        ele "I remember. I still think about that night in my dreams. I probably will for the rest of my life. It was the most heroic thing I’d ever seen a man do."
        show eleanor dress neutral at midright with dissolve
        ele "But, you’re still a coward."
        "Rowan balled his fists up. Not even the twins normally drew this from him. Why? Why was he feeling this way from the words of some powerless spoiled noblegirl?"
        "He exhaled. It all went with his breath."

    show rowan necklace neutral at midleft with dissolve
    "Rowan staggered back to the bed and sat back down with his head in his hands."
    ro "Hmphh."
    show eleanor dress concerned at midright with dissolve
    "Eleanor approached him slowly. She stepped towards him on the tips of her toes. When Rowan raised his head once more, her arms were around him. So delicate. She had hands with no calluses. Just smooth."
    ele "I’m sorry. I really am. I must seem like the most ungrateful woman in the whole world."
    "Eleanor looked to the side."
    ele "I really do owe you so much. "
    ele "..."
    ele "So they’re really going to be here, aren’t they? If I stay in Rastedel, I’ll fall into their hands."   
    ro "Yes."
    ele "I suppose they might even remember me. A chilling thought indeed."
    show eleanor dress neutral at midright with dissolve
    "She withdrew her arms. A source of warmth gone away. Rowan watched the way that her long dark hair swayed as she made her way back to the window. The city stood watch over them."
    ele "If you believe that Rastedel is no longer a place of safety, then it would be foolish of me not to listen to your council."
    ele "On the morrow, I will persuade my father to begin preparations for a move east. We have family in that territory. They will not be pleased to have to support us, but they will not turn us down either."
    "She walked stiffly to that beautiful sheer dress and the cloaked she had left on the ground. Rowan drank in her naked form while he still could. Delane’s tone made it clear he would not be seeing it again in any immediate future."
    show eleanor dress concerned at midright with dissolve
    ele "You don’t have to bear this by yourself, Rowan."
    show rowan necklace concerned at midleft with dissolve
    ro "Yes, Lady Delane. I do."
    ele "So you say."
    "She pulled on her cloak and walked from the room. Rowan got up from the bed to watch her descend the staircase."
    hide eleanor with dissolve
    "The following day, he received a note saying that Lord Delane and his family had decamped the capital. They had not even been charged the Sword Aid in light of the losses they’d already suffered in the conflict. Rowan traced the ink on the parchment with his fingers."
    $ eleaLeft = True
    $ released_fix_rollback()
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

else:
    "Lady Delane’s voice lowered to a mumble."
    ele "This explains a great deal. I will admit, I had even considered the possibility before."
    "But, before she let herself be drawn to deep in thought, she stopped. Instead, she shook her head at Rowan. Her eyes steadied themselves on him."
    ele "No."
    ro "No?"
    ele "I understand your intention. You simply wish to keep me safe."
    ele "But, such a thing cannot be allowed. I, and my family, will remain in the city for as long as it is feasible to do so. This is not a subject of negotiation."
    show rowan necklace angry at midleft with dissolve
    "Rowan shook his head and loudly slammed his hands on the table. The rumble of it made her flinch."
    ro "Do you expect me to simply accept that? Do you not understand the stakes here? I just told you all that I’ve been through. Especially what I went through for the sake of your life…"
    "She restored her composure and shook her head."
    show eleanor dress concerned at midright with dissolve
    ele "So you did. I believe every word. I cannot imagine the hardship it entailed. Truly."
    show eleanor dress neutral at midright with dissolve
    ele "But, tell me something, Rowan. Do you plan to leave the city as well?"
    ele "You ask for me to pack up and travel East. Away from the danger. But, forgive me for not seeing your packed bags. You plan to stay in the city and try to protect it until the last possible second."
    ele "So, why should I?"
    "Rowan felt what little was keeping him from shouting slipping away the longer the conversation continued. His hands twitched."
    ro "Because, My Lady, if the city falls and I am inside, nothing happens to me. As far as the demon forces know, I am on their side. But, if the city falls and you are still inside, you will…"
    show eleanor dress angry at midright with dissolve
    ele "...Be raped?"
    "She spat to the side."
    show eleanor dress neutral at midright with dissolve
    ele "Oh, you needn’t spare me the modesty. I spent months in an orc encampment as a prize to be tossed around. Do not think me such a blushing flower."
    ro "Yes. That. They’ll do bad things to you, My Lady. The common folk will probably be fine. For the most part, at least. But, the Demons are not going to just let an entire class of people wander around taxing their new subjects. Every noble is at risk. "
    ele "If I leave, who would help you?"
    ele "This is why I remain so insistent, Rowan. You remember your meeting with Duke Werden, after all. You are a commoner and the only people who can aid you are not."
    ele "As I understand it, you need me. "
    ele "You need a partner who can shout on your behalf when some high born puffycoat wishes to get in your way. That invertebrate, Duke Raeve, certainly will do nothing of the sort."
    "Delane flashed a smirk. She was winning and she knew it. She strode closer, this time not as a seduction tactic."
    ele "Rowan, you need me."
    show rowan necklace concerned at midleft with dissolve
    "Rowan slowly walked back to the bed and put his head in his hands. This was not going well at all. Delane was as stubborn as a mule. Not even the threat of renewed captivity with the orcs could deter her."
    "Delane walked over and brushed her smooth fingertips on his shoulder."
    show eleanor dress concerned at midright with dissolve
    ele "You’ve borne such a burden for so long, Rowan. Let me help you."
    ele "You can continue with your cloak and dagger espionage. Play the demons like an instrument. But, if you need help in the human lands. Rastedel. Wherever. I can be there. A steadfast and politically savvy ally to ensure you achieve your objectives."
    show eleanor dress happy at midright with dissolve
    ele "A generous deal, no?"
    "There was something sweet about it. There was always Alexia in the castle. But, most of Rowan’s life, these days, didn’t happen in the castle. Otherwise, he was alone."
    "Still."
    ro "Perhaps. But, I can’t accept that. You know that if you…"
    show eleanor dress neutral at midright with dissolve
    ele "Nope. No way. Not a chance. I have made up my mind already. I will not hear a word to the contrary. Simply inform me where you will be working, and I will go there and start making connections on the ground."
    ele "I had always wanted to do a bit more traveling. A dirty orc cage is entirely unsuitable to be my sole adventure."
    "She extended a hand to shake."
    show eleanor dress happy at midright with dissolve
    ele "So. Do we have a deal?"
    "Rowan sighed and looked to her. Her eyes were shimmering bright. She had not even seemed this excited back on the street."
    ro "Do I even have a choice in the matter at this point?"
    "Delane just giggled at him."
    show rowan necklace neutral at midleft with dissolve
    "Rowan slowly took her hand."
    ro "Alright. Partners then."
    ro "But, from now on, you do what I tell you to do. If you want to involve yourself in espionage and war, you can’t treat it like some kind of adventure novel."
    ro "Be ready to evacuate Rastedel at a moment’s notice. Just because I’m agreeing to your help does not mean that the city is safe all of a sudden."
    show eleanor dress neutral at midright with dissolve
    "She gave a firm nod, like a soldier responding to an order."
    ele "Got it. I’ll have travel provisions and valuables ready to for a moment’s notice."
    show eleanor dress happy at midright with dissolve
    "Rowan scrutinized her closely. She was smiling again. How could he put into words how unhappy he was with this arrangement? She wasn’t stupid. She didn’t even have much cause to be naive. Did his words have no effect?"
    "Perhaps, then, the best move would be simply to fill her in on the last little bit of the truth. The fact that his true goal was to, above all, save Alexia. Saving the realm was one thing, but would she risk her life to save his wife?"
    "Rowan didn’t tell her about that though."
    if delaneSex2Refuse == True:
        "Instead, he pushed her down on the bed and took her again. His body was ready once more, and he found her just as eager as she had been earlier. How many hours were spent like that, bodies in motion, it was hard to say."
    else:
        "Rowan and Delane talked a while longer. The conversation was bright and snappy, and Delane always seemed to have a snappy answer to whatever Rowan said. It was relaxing."
    "Eventually, the shadow from the codifice moved on, and sun streamed into the room once more. With it, sparkling light reflected from the nearby river."
    $ delaneAlly = True
    $ released_fix_rollback()
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

########################################################################################################################
########################################################################################################################
########################################################################################################################

label sternCouncil:

$ sternCouncilSeen = True

show rowan necklace neutral at midleft with dissolve
show patricia annoyed at midright with dissolve

"When Patricia walked in for the scheduled meeting, Rowan could tell something was off immediately. Her fists were clenched in balls, and her eyebrows were clearly furrowed. Small package or no, she looked ready to commit a murder."
"She sat in her chair so strongly and with such force that Rowan was worried it might break."

ro "Is something amiss?"

patr "Not something you need to be the one to deal with."
patr "Some asshole on the council has been trying to block some of the defensive measures you mentioned to me. Sir Alois Tranche, the Minister of Military Affairs."

"She spat to the side."

patr "From his self-importance, you’d think that when you knight a man that his cock grows three inches longer."

ro "Whose he sided with?"

"If he was a noble, was there a chance that he was aligned with the purples?"

patr "He’s still with Marianne. Werden has been trying to tempt him over, though. He hasn’t got the memo that none of the rest of 'em have a support base anymore. All he does is make the procedure to get things done more difficult."

"Rowan ran a hair through his hair slowly, letting the individual strands glide through his fingertips. There was an opportunity here."

ro "You know, my lady. Perhaps this is a situation that I may actually be able to help with."

show patricia neutral at midright with dissolve

"Lady Patricia's expression perked up."

scene bg34 with fade
show patricia neutral at midleft with dissolve

"The following day, Patricia was back in the council room. It was positioned in the heart of the Palace. Only a short walk from the Baron. Around the table were an eclectic collection of well dressed nobles, robed priests, and even a man in full armour."
"A priestess sat at the head of the table in Marianne's place. She was likely back at the Codifice today. A proper noble page boy stood at his side."

page "The Chair recognizes High Chancellor Crevette."

"Patricia rose to her feet and looked around the table to a mix of appreciative and disinterested faces. A battlefield over the large oak table."

patr "The new garrison holding Verdoin Abbey needs supplies. I’ve earmarked the new weapons coming from these two forges to be transported north. That will help ensure we can hold it in the future."
patr "We will also need to build a stockpile of rations there to ensure that it can withstand a siege. This is a depressingly likely eventuality."

"Patricia spent the better part of the next half hour running over the details of the plan. It didn't merely involve Verdoin. Instead, it identified key fortifications all along central Rosaria that might help hold back a marching demon army. All locations Rowan had identified."

patr "Any objections, my lords?"

show rosarian knight neutral at midright with dissolve
show patricia annoyed at midleft with dissolve

"The lord who'd come in full combat armour slammed a hand on the table. Patricia winced to herself."

alois "Yes. One from me."

page "The Chair recognizes Minister for Military Affairs, Sir Alois Tranche."

alois "As the head of military affairs, deciding what garrisons need requisitions is my department, My Lady. You may be responsible for requisitions, but all diversions of supplies must have my approval."

"Someone watching would be able to see Patricia's expression grow hotter. She could have pounced on him from across the table."

patr "I am the one proposing this because I am the one the garrisons got in touch with. Do you plan to hold up the needed supplies?"

alois "Hmm."
alois "One has to wonder why move supplies and arms from the capital to this side theater. One whose soldiers are not under our control. Why not let your friend, Werden, supply his own men?"

patr "It’s not that simple-"

"Before she could even reply, the knight rose his voice so loud that she couldn't talk over him. Patricia's nails dug into the table."

alois "It seems to me that he would be perfectly capable of that. Had he not wanted to do the hard work of keeping the garrison in fighting shape, he should have thought about that before he moved. Without the authority of I or any of the generals, may I add."
alois "Procedure must be followed, Chancellor. You know that."

show rowan necklace happy at edgeright with dissolve

"Rowan decided that he had waited long enough outside the door. Someone had to shut this buffoon down. He threw open the doors and strode into the room. There were audible gasps. Even a few half-formed questions of who was entering, before they saw who their guest was."

ro "Apologies for my interruption. I had been invited to visit the council during one of its sessions by the chancellor. This is not improper, is it?"
       
show patricia happy at midleft with dissolve

"Patricia's expressions softened, and she bid Rowan closer."

patr "I wanted one of the actual field generals involved in the discussions. Rowan is set to be one of the commanders if the city is attacked."

"The room was left sputtering. It went against Sir Alois' precious procedure, but Rowan's role in the city's defense and his status as national hero were not subjects of debate."
"To his credit, it was Sir Alois himself who finally responded to this interruption. Marianne's proxy was still stunned."

alois "No man would dare tell the hero of the realm he couldn’t sit in. So long as there were no pretensions to a council seat, of course."

"Slowly, a chorus of agreement went out around the table."
"Rowan walked over to the empty seat next to Patricia and grabbed the back of the chair."

ro "Excellent. I will take whatever oaths of secrecy as is necessary. That said,I’m privy to most of the details of the defense by now, so if need be we can dispense with that."

ro "Mind if I sit down?"

"He and Patricia exchanged a brief knowing glance. Rowan took his seat at her right hand."
"Sir Alois let out a loud cough."

alois "As I was saying."
alois "The purpose of the royal stores is to serve the royal forces themselves. The capital must be secured before we can worry about the positions of vassals."
alois "You also mentioned an effort to repair damages to fort-"

"Rowan didn't even let him finish. Now it was the knight's turn to be interrupted."

ro "Apologies, but may I interject?"

"Sir Alois looked struck. The rest of the table glanced around, unsure. The Purple ministers all nodded, while the remaining blue ministers mostly remained silent or just gave way from their own confusion."

page "The Chair now recognizes General Rowan Blackwell."

"Rowan rose to speak."

if avatar.corruption > 30 and avatar.corruption < 61:
    "A smirk formed on his face, despite his best intentions."
    
elif avatar.corruption > 60:
    "Rowan smirked darkly. He was about to enjoy this."
    
else:
    pass
    
ro "Naturally, I understand your reluctance to trust High Chancellor Crevette's advice on military affairs. She's not a soldier."
ro "That's why I had actually been the one advising Chancellor Patricia on the military situation when she constructed the plans. All of her ideas were run by me first."

"Patricia jumped in, seeing the blood in the water."

patr "Do you believe I would be so foolish as to propose military strategy without first asking a general who’d been on the ground?"

alois "I-I see."

"Sir Alois lowered himself back into his chair. In effec,t he had ceded the entire floor to Rowan. Rowan started to pace behind his chair as he spoke. He took on the posture of an instructor in front of a class."

ro "I had advised her that our forward defenses should be built up. Whatever costs to the city’s defenses moving resources to front line positions would incur can be paid back with interest by the time they had fallen."

"That is, unless the demons were planning to bypass the fortifications entirely to strike when the city was undefended. But, not even Patricia knew about that wrinkle to it."

ro "Surely, you remember the intense suffering that we all felt before the road north was opened up again with Verdoin’s recapture. Before I opened the road again. We have yet to even begin to recover from the damages of it, and you wish to leave our defenses there weak?"

if avatar.corruption > 30:
    "He put extra emphasis on the word “I” just to rub it in. "
    
"Sir Alois had spent the entire verbal assault shrinking in his seat. Still, he didn't give up immediately."

alois "..."
alois "It remains improper for Duke Werden to hold a garrison in Crown Lands with his own personal levies. That should rightfully be under the command of the royal army."

ro "What troops? Where are you going to pull the men to garrison it from?"
ro "The Royal Army, as an organized regional fighting force, does not exist. We have whatever men can still hold the capital, some troops caught on the far west of the country, mostly holding ports and keeps, and our standing forces over the eastern mountains."
ro "None can be moved. None are even presently sufficient to defend themselves."
ro "I ask again, Sir. What troops would the royal army even garrison Verdoin Abbey with?"

"Sir Alois didn't have an answer to that question."

ro "That is what I thought."

"The table was silent. Sir Alois certainly didn't want to speak. The other nobles were thoroughly cowed. The only other person standing up was Patricia."

show rowan necklace neutral at edgeleft with dissolve

"Rowan turned to her and bowed."

ro "Apologies for interrupting you, My Lady."

"Patricia smiled and bowed back at him respectfully. A show for their present audience. Rowan was passing the torch back to her. He sat back down into his chair."

patr "Not at all, my friend. That was most illuminating."

show patricia neutral at midleft with dissolve

patr "Now that we have resolved that business, let’s move on. I have much more business to run through..."

"No one interrupted Patricia for the remainder of her report. When it came time for the voting process after all of the issues were settled, almost all of Patricia's proposals had easily passed."

hide rosarian knight with dissolve

"After the business was done, the powerful men and women of the city filed out of the palace. Among them, a humbled Alois."

show rowan necklace happy at edgeleft with dissolve
show patricia happy at midleft with dissolve

"Rowan waited in the hallway until Patricia left the room. She was always the last one out. When she arrived, everything she had been holding in after her presentation flowed out. She smiled ear to ear and nearly hopped in place."

patr "Fucking tits, right there. Fucking tits."

"Rowan chuckled to himself. He'd never seen her so...unambiguously happy."

patr "That asshole has been making my life miserable for years. Years. All of them have. But, you shut him right up. He looked like a dog that had been kicked to the curb."
patr "Wonderful. Just wonderful."

"Rowan bowed slightly, feigning humility. The goal wasn't to take credit for what happened."

ro "I would never have even gotten into the room without you. You did all of the work. I just helped out in a few places."

"If Patricia noticed what he said, she didn't show it. She just kept on talking."

patr "...And the rest of them too. They sat there and listened. I haven’t had a council meeting go so completely my way in a long time."

"Rowan and Patricia started walking for the exit. She laughed to herself. Had Rowan not known how much frustration she'd been keeping bottled up, he might have thought her a mad woman."

patr "We make a good team, Rowan."

"She was looking ahead, not even meeting back his look. Rowan looked ahead too."

ro "I like to think so too."

patr "Together, we’re going to make this city our bitch."

"Together, Rowan and Patricia walked out of the palace."

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

##################################################################################################################
##################################################################################################################
##################################################################################################################

label clubbingSeal:
    
$ clubbingSealSeen = True
$ julietSexAvailable = True

show rowan necklace neutral at midleft with dissolve

"This time, when Rowan was let into the Lodge by the guards, he was looking for someone. Juliet. But, he didn’t have to ask many people before realizing that she wasn’t there. Many of the more devout nobles were gone. Today was the weekly services at the Grand Codifice."

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve

"Within the hour, he’d crossed back to the north side of the river. A large crowd had gathered in front of the temple, waiting for the doors to open."

show juliet neutral at midright with dissolve

"Along the edges, near the market stalls, Rowan found Juliet. She was talking with an apple merchant. Rowan waited for her to finish. When she turned from him, newly purchased apple in hand, Rowan saw a handkerchief fall from her basket."

if avatar.corruption > 30:
    "A perfect opportunity to strike."

else:
    "Rowan sighed inwardly. He would not enjoy this."
    
show rowan necklace happy at midleft with dissolve

ro "You must be more careful with your things, My Lady. I won’t always be there to pick them up."

show juliet shocked at midright with dissolve

"Juliet turned around to see him, handkerchief extended. She half-jumped."

juli "R-rowan! What are you doing here?"

if rastAlly == "werden":
    ro "Well, I still owe you stories, don’t I? I made you a promise. It would be wrong of me to ignore a debt."
    ro "I heard you were going to services so I went to pay you a visit."
    show juliet happy at midright with dissolve
    "She clapped her hands together. Her whole posture changed, as though someone had run a current of energy through her."
    juli "You wanted to go with me?"
    show juliet neutral at midright with dissolve
    
else:
    ro "I was actually just on my way to services. The sermon of the High Arbitron isn’t a thing most peasant folk get to hear very often. A perk of my present situation."
    ro "Were you as well?"
    show juliet neutral at midright with dissolve
    "Juliet kicked her feet. Her eyes had lowered the moment she saw him, but every few seconds she’d peek up at him. Her arms were crossed over her chest."
    juli "Indeed."
    juli "..."
    "Rowan stepped closer. She was fighting herself about something."
    ro "Is something amiss?"
    juli "Father warned me I shouldn’t speak with you."
    "Rowan nodded. Of course. He’d noticed how she’d been looking at him in the past. Surely he realized the danger in his daughter’s crush."
    "It took Rowan a few seconds to construct a plan. He was not experienced in this kind of subversion. But, when he spoke again, it was with purpose."
    ro "As well he should. You don’t know me. Do you?"
    "She nodded slowly, now eyes firmly meeting his."
    ro "It’s only right that you take precautions with strangers. Even heroes of the realm. He’s showing wisdom."
    ro "Not that your father needs instruction on not trusting people. He’s quite skilled already on that front."
    "Juliet looked behind her. Then back to him. She was searching for something. A reason to agree."
    juli "You’re not really a stranger though. Are you? "
    if avatar.corruption < 31:
        "Rowan cringed inwardly."
    juli "My brothers and father served alongside you in the war. And my departed uncle as well. You’re a friend of the family."
    "Rowan shrugged. He still needed to present himself as the voice of wisdom. He couldn’t be too eager to accept her rationalization."
    ro "Still, we haven’t spoken much personally. If you’d like we can sit together during services. Perhaps change that."
    "Juliet slowly uncrossed her arms."
    
juli "We would have to be quiet though. Services are no right place for story time. We could disrupt the other worshipers."

"She nodded sagely."

ro "Of course."
ro "And I doubt Marianne would much enjoy being interrupted."

"In the distance, Rowan saw the door of the Grand Codifice opening. The crowd was starting to funnel in." 
"Juliet put a finger in his face and wagged it."

juli "Her Beatitude, the High Arbitron. Father is the same way. I remind him to say the full title all the time, but he never does."

show juliet happy at midright with dissolve

"She sighed to herself. Then she knelt down into a proper curtsy."

juli "Very well. It would be a great honor to attend services side by side with the savior of the realm."

scene bg37 with fade
show rowan necklace neutral at edgeleft with dissolve
show juliet neutral at midleft with dissolve

"The pews of the Grand Codifice rang out with the whispered prayers of the people of Rastedel. Some prayed for safety. Some for strength. Some for a stealthy getaway. At the head of the congregation, framed by floating pillars of water, was the High Arbitron."

show marianne neutral at midright with dissolve

mari "She is the shield of our heart and protector of our minds. Let her guide us to wisdom, clarity of vision, and purity. We are travelers and she is the way."

cong "She is the shield of our heart and protector of our minds. Let her guide us to wisdom, clarity of vision, and purity. We are travelers and she is the way..."

"Rowan leaned over to Juliet in the seat next to his and whispered something in her ears. They sat near the front, close enough to see the High Arbitron up close."
"Juliet giggled softly to herself but managed to go quiet and return to a proper worshipful posture."

juli "Shhh."

"Rowan felt a few cold looks. It had wound up loud enough for a few nearby people to hear. Marianne glanced vaguely in their direction but had to move on to the next prayer mere moment after."
"The services dragged on."

show rowan necklace happy at edgeleft with dissolve
show juliet happy at midleft with dissolve

"Soon, Juliet had given up even pretending to focus on praying. She and Rowan were whispering incessantly to each other throughout the service. An older noblewoman shushed at them periodically throughout the service, but Rowan and Juliet just kept on talking."

scene bg33 with fade
show rowan necklace happy at midleft with dissolve
show juliet happy at midright with dissolve

"Later, when the services were done, Juliet tugged on his sleeve."

juli "I know of a garden by the side of the Codifice. Her Beatitude’s personal. They have such lovely irises there. We can speak there, Rowan. "
juli "That is, if you wish to."

"Rowan gave a soft bow."

ro "It would be my most sincere honour."

"Juliet led him past a winding path through a gate up to the roof of one of the Codifice’s side buildings. Atop it, Rowan was struck by the sight of a vast rooftop garden. Soil taken from the countryside was watered by the flowing currents runnings from the Codifice itself."
"As he stared, Juliet looped her arm in his. With a little nudge, she got him walking."
"They strolled through the garden, over green grass as fresh on the hillsides outside the city. Together they looked like a painting or an illustration in a story book. They spoke on a wide range of topics together. Juliet would ask a question and Rowan would build an answer."

ro "Some stories say Orcs unskilled fighters or brutes. In truth, they can be quite clever and practiced. They are an entire culture devoted to war. The average Orcish soldier has more combat experience and training then even most knights."

juli "Then how are our brave soldiers able to defeat them in battle?"

show juliet neutral at midright with dissolve

"Juliet tilted her head."

ro "Strategy and Logistics."
ro "Good commanders and discipline maximize fighting effectiveness. We rarely go into battle with worse armors, arms, or provisions then them. And we almost always face them with greater numbers."
ro "Steel, terrain, food. The secret of war is that battles are rarely truly won on the battlefield itself. The bravery of individuals rarely changes wars."

show rowan necklace neutral at midleft with dissolve

ro "I was the exception, I suppose..."

"The conversation moved on to other topics. The topic was mostly war stories. Though, Juliet did chime in with a small bit about a book she read. A story about a knight returning from war who snuck in through the window of his lady love, so as to avoid her parents."

show rowan necklace happy at midleft with dissolve
show juliet happy at midright with dissolve

"Together, they arrived at a river stream. The main bulk of the water flowing from the codifice. A quaint little rope bridge had been built on top of it. It must have been quite old because it seemed rickety. Rowan went first and extended his hand to Juliet."

ro "Take my hand, my lady. "

"Without a second’s hesitation, she grabbed it." 
"On the other side of the river, she looked around as though she spotted something."

show rowan necklace neutral at midleft with dissolve
show juliet neutral at midright with dissolve

juli "Perhaps we should continue going a bit further, sir. I feel watched..."

"Rowan nodded. He felt watched too. Together they made off, moving faster until they arrived together at a small clearing. Here it would be hard for someone to sneak up on them."

juli "There had been a question I wondered above all. Something closer to my heart."

ro "Your uncle?"

"Rowan hadn’t had to guess. No doubt she had spoken too few others who had been there the day of the battle of Karst. The same battle that had preceded the siege where he had earned his fame."
"She nodded softly and took a polite seat on a stone. Rowan had the center of the clearing...and her undivided attention."

show rowan necklace concerned at midleft with dissolve

ro "..."

show rowan necklace neutral at midleft with dissolve

ro "Well, I didn’t know him that well. Back when he died, I was no one. No random soldier, especially from another lord’s levy, gets face to face time with the army’s commander."
ro "I’d been called up only weeks before. In Prothea, the Holy Lord Zerias had changed sides and pledged fealty to Karnas. You were young back then, right? Do you remember what happened?"

juli "Mother took me and Edmond east. Father and my brothers were already in Prothea, but Uncle David wanted to go to Karst."

"Rowan sighed. He still remembered the day of his mustering. Alexia watching him march off in formation with the other men of Arthdale. It had been the start of his long war."

show rowan necklace concerned at midleft with dissolve

ro "The entire mission was doomed."

show rowan necklace neutral at midleft with dissolve

ro "Zerias was going south, so they only thought they needed to put together an army strong enough to face a human duke."
ro "But, Karnas put a second, secret, army into his hands. Orcs armed with well-forged arms, led by lesser demons, and fully provisioned."
ro "I was part of Raeve’s force, on the wing, during the battle. Your uncle, the former Duke Werden, in the front. Zerias met us on the road up to Karst."

show juliet happy at midright with dissolve

juli "Did you see what happened to him?"

"Rowan held up his hand. Juliet was leaning forward. Overeager."

ro "We’re getting there. Hold."
ro "Your uncle and his men were the point of the spear. Thick in the fighting. On the far right flank, we mostly held against their counter attacks."
ro "I saw his standard holding high. It was even still making headway down the road."

juli "So what happened?"

"She bit her nails."

ro "The second army. More than a thousand orcs in steel armor charged out of nowhere and struck the other flank. Suddenly, everyone further back was running. But, the orcs were behind the vanguard. Behind your uncle."

show rowan necklace concerned at midleft with dissolve

ro "They were all trapped. Lambs for the slaughter."

#juliet sad
show juliet neutral at midright with dissolve

juli "Uncle David..."

ro "He tried to break out. Aim for a segment of the line where the enemy were weakest. But, no one made it out of the trap."

juli "I’d heard from my older brother that he and cousin Gilbert had been surrounded together and left many dead at their feet before being brought down. The rest, I hadn’t been told."

ro "Perhaps. All I saw was their stand go down. I was one of the closest men to the tragedy, but making out what happened was nearly impossible. None of them made it out alive, and I’ve never heard of an orc survivor of the war who can claim to have seen his final moments. "

"Rowan decided perhaps it would be best to leave a key detail out of the story." 
"He might not have known how the former Duke of Werden died. But, every man who’d been besieged in Karst after the battle had clear memory of what had been done to his head."

show juliet shocked at midright with dissolve

juli "You were closest? Goddess Fend…how did you make it back?"

show rowan necklace neutral at midleft with dissolve

ro "It wasn’t easy. We had to run on foot. My unit were among the last back to Karst."

show juliet neutral at midright with dissolve

"Juliet put her hand to her mouth."

juli "I cannot imagine how someone could be so brave as to stay and fight in that situation. I’d be terrified."

"Rowan nodded stoically. Here too the story was more complicated. It was simply his unit got stuck in a blocking position. But, the story worked better this way."

ro "It had to be done, my lady. All there was to it. It had to be done."

juli "Truly…"

#juliet concerned

"Storytime, however, was to be interrupted. Before they could continue, they heard voices in the distance. People coming. Had that been the presence they had felt earlier?"
"He turned back to Juliet. In moments her expression had shifted radically. She had pleading eyes."

ro "You don’t want to be seen alone with a man in public, my lady? "

"She nodded softly."
"Rowan had to think fast. There wasn’t a good way out from here that didn’t involve first approaching the voices." 
"No, they had to hide."

show juliet shocked at midright with dissolve

"Without saying anything, he grabbed Juliet by the shoulder, and jumped into the bushes. Her squeak of surprise was muffled by Rowan’s hand."

#juliet concerned

"Still, she made no effort to wriggle free from his grasp. At first, she was stiff. The addition of nearby voices. A group of young men and ladies speaking in proper tones. Juliet may well have known some of them."

#juliet aroused
show juliet neutral at midright with dissolve

"But, once she’d gotten used to their place of hiding, her posture shifted. She leaned in more to his embrace. Rowan felt her supple bosom press into his chest. Her head buried into his chest."
"It was only once the voices had passed, so far as to make being in sight range impossible, that Rowan and Juliet emerged from the bushes together."

ro "Apologies for that. It was unseemly."

"Juliet couldn’t meet his eyes. Her cheeks were burning."

juli "No. Thank you. You were quite quick thinking. It’s just I..."

ro "I assume that you’re not much used to close contact with the male sort. Or even with male company in general. One can only imagine life growing up under someone as strict as your father."

#juliet neutral

"To his surprise, Juliet shook her head emphatically. Had he said something wrong?"

juli "Father was never strict with me."

ro "I had not meant to insult him. Merely to say that…"

"Her voice grew bolder then he had yet heard from her."

show rowan necklace shock at midleft with dissolve

juli "He can be protective at times. He’s made it quite clear that my interactions with the opposite sex are to be viewed skeptically. But, father has always been understanding and supportive."
juli "He’s never scolded me or said a word in anger. If he doesn’t like something I’m doing, he tells me he’s worried. It’s mother whose always been the strict one. "
juli "In truth, He- Can you keep a secret?"

"She glanced to the side."

show rowan necklace neutral at midleft with dissolve

ro "I should hope so by now."

juli "Father would actually sometimes help me sneak out of lessons. We’d go riding together in the countryside. Especially in the years after the war ended."
juli "He’s always been the kindest of the kind."

"Rowan simply stared at her, dumbfounded. Did she have some entirely different father he didn’t know about?"

ro "The kindest of the kind. Indeed."

show rowan necklace happy at midleft with dissolve
show juliet happy at midright with dissolve

"After, they departed from the clearing. Best not to linger too much longer. A short time later, they were at the gate leading from the garden."

ro "I’ll leave first. You can stay in the garden for a time longer. That should throw off any watching eyes."

#juliet aroused

"He leaned over and brushed her cheek ever so softly with his finger tips. Only a touch. It would leave her eager for more. Juliet giggled at the touch."

ro "Don’t miss me, Juliet. I’ll see you soon."

"Rowan left the garden, and the Codifice complex, with a bright smile on his face. He was certain that Juliet had watched him go with forlorn eyes. His plans had come to fruition."

hide juliet with dissolve

if avatar.corruption > 30:
    show rowan necklace neutral at midleft with dissolve
    "That had all been almost too easy. Had he not known of Juliet’s crush, he might have thought this was a trap. Playing with the feelings of others had become strangely easy."
    if avatar.corruption > 60:
        "He liked it."
    
else:
    show rowan necklace concerned at midleft with dissolve
    "The entire time, Rowan had half-wanted to shout at her to stay away from him."

"Rowan only had to walk a little bit longer until the person who had been stalking them started walking at his side."

show ameraine happy at midright with dissolve

amer "I don’t think anyone else was paying attention to you. You’re in the clear."

ro "Did you actually go into the Codifice with us?"

"Ameraine was smirking quietly. He had not asked her to join them. But, figuring out who’d been watching them had been all too easy. It was good that Rowan had nothing to hide."

amer "The entire time, Rowan. She was laughing and leaning close to you the entire time. You could have told her to roll over like a cur and she’d have done it."

if rastAlly == "jacques":
    amer "So, when are you going to seal the deal? Her information is too valuable for you to dawdle."
    show rowan necklace angry at midleft with dissolve
    "Rowan gave her a hard look."
    ro "I understand my mission. There will be no failures or delays."
    hide rowan with moveoutleft
    "Rowan sped on, leaving her standing in the street alone. After doing what he had to today, he didn’t much want to speak to her."
    if avatar.corruption < 60:
        "Ameraine sighed to herself. Rowan was rapidly retreating into the distance from her."
        amer "So touchy. All he’s doing is stomping on an innocent kitten. You’d think he’d be used to that by now. Tsk tsk."
        $ released_fix_rollback()
        $ prevent_tile_exploration()
        $ push_to_previous_tile()
        return
    
else:
    amer "One has to wonder what you’re doing with the poor girl. Oh, she’s pretty. And she wants you in her bed. But, why take the time on it?"
    amer "Is it her looks? Or something else?"
    if avatar.corruption < 60:
        hide rowan with moveoutleft
        "Rowan kept on walking, not even looking at her. It was a question he didn’t much want to answer."
    else:
        show rowan necklace angry at midleft with dissolve
        "Rowan glared at her darkly."
        ro "You know why I’m doing this, Ameraine."
        "Ameraine smiled wide and dark."
        amer "There is still fun in asking."
        amer "The point is moot. Be careful and be smart. I’m not about to begrudge a man a spot of petty vengeance, but every step you take makes the plan more complicated. I will not have my designs ruined."
        "Rowan didn’t look at her. This was not a line of question he took kindly too. His vengeance was his business."
        ro "They won’t be."
        hide rowan with moveoutleft
        "Rowan sped up, so he didn’t have to continue speaking to her."
        
$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return