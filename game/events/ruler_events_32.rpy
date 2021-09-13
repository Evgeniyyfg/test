init python:

    event('greyhide_coal_shipment', triggers="week_end", conditions=('week >=30', 'castle.buildings["forge"].lvl < 3', 'castle.iron_per_week >= 5'), group='ruler_event', run_count=1, priority=pr_ruler)
    event('handle_with_care', triggers="week_end", conditions=('avatar.corruption > 30','all_actors["alexia"].corruption > 30',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('rowans_reward', triggers="week_end", conditions=('castle.buildings["brothel"].lvl > 0',), group='ruler_event', run_count=1, priority=pr_ruler)
    

label greyhide_coal_shipment:

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show liurial neutral at edgeleft with dissolve

"Rowan was stuck with attending an unending mountain of paperwork. Reports of logistics, scouts, the maintenance of the castle grounds… droll and soul crushing work that wore on his fortitude."
"To his left, his assistant diligently tackled her own stack. Their expressions were a study of contrast. Rowan was dull out of his mind, but she looked content. She even hummed softly as she worked."
"The silence broke when the door thunderously cracked against the wall. The man had long grew accustomed to orcs slamming his door wide open with no sense of manners."

ro "What is it?"

show orc soldier neutral at midright with dissolve

os "Bull man. Needs you down in tha’ forge."

ro "Why?"

os "Dunno, seemed upset tho."

hide orc soldier with dissolve

"He dismissed the orc with a wave of his hand, and sat back into his chair to ponder for a moment. Greyhide wasn’t one to need much looking over. Something may have gone wrong."

scene bg22 with fade
show rowan necklace neutral at midleft with dissolve

"It was oddly tepid in the forge when the man entered. The musical rhythm of metal was absent. A knot started deep within his stomach. He turned to meet Greyhides stoic gaze. Grey fur was stained pitch black from his hands to elbows."

show greyhide neutral at cliohnaright with dissolve

"Greyhide bowed his head low. Rowan attempted to wave away the formality, but the hulking man stared solemnly the palms of his hands."

ro "What is it?"

gh "I’m sorry, but... "

"With no effort, the minotaur crumbled handfuls of coal within his palms. He looked up to the man with a look of trepidation. His voice rumbled low with melancholy. Rowan gave him the time to explain the situation."

gh "The forge has been tainted with this."

"The minotaur threw the coal dust into a crate full of the rock. He languished for a moment. His massive form shrunk as he looked deep into the black rocks."

ro "Coal?"

gh "It’s too soft, the orcs who fed the furnace wouldn’t have known the difference between coking coal and this..."

ro "Then what does this mean? No one even uses coal like that back where I’m from."

gh "The forge won’t be able to smelt iron. What’s left within the firepot has to be cleaned. I then will need a shipment of true coking coal, until then I cannot bring the fires hot enough to smelt iron."

"Rowan’s gut feeling was the assume the worst. But it was hard to imagine that any in the castle would risk sabotaging the twins."

ro "I guess there’s no way around it then. How could this have happened?"

gh "To the untrained eye it would be nigh impossible to tell one from the other. Coking coal has a lustre to it when you remove the dust. It is also far harder than this…"
gh "The failure is mine… I should have inspected it upon arrival."

show rowan necklace happy at midleft with dissolve

ro "You’re not to blame for this. It’d bet that we were taken advantage of… I’ll warn Cla-min and tell her you need more."

show rowan necklace neutral at midleft with dissolve

ro "How long do you think it’ll take?"

"Greyhide cupped his chin with a hand, staining the grey fur within soot. Rowan stifled a chuckle at the elder minotaur’s blackened face."

gh "If you will permit me an aide who can fit within the forge, I need only two days. However, we will lose those days of production."

ro "Best we get to it. Thank you, Greyhide."

gh "Of course, until next time."

"With a polite nod exchanged between the two, Rowan set off to give Cla-min the bad news. The goblin would certainly have a deluge of choice words with whomever tried to pull this one over on her. In the meantime it would seem armour production would briefly stop."

$ castle._iron -= 5
return

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

label handle_with_care:
    
scene bg6 with fade
show rowan necklace neutral at midright with dissolve

"The longer Rowan looked at the document, the more tired he got. Scouting reports on the movement of Knights near the border of The Tundra and Rosaria were important. But, it was getting late and his ability to focus had been dulled from hours of grinding work already."

if week > 24:
    "Liurial had left for the night an hour before. Rowan hadn’t minded since she was actually on top of her work for the month. She was probably the only one. "
    
quest "Rowan?"

show alexia 2 necklace concerned at midleft with dissolve

"Rowan looked up. His wife was standing in the doorway closest to the administrative desks."

al "I was waiting up for you, but you never came back to bed."

"Rowan shook his head. Didn’t she understand how important his work was? This woman could be so needy sometimes."

ro "There was still work that needed to be done over here. I’m basically the only one holding this castle up."

"Alexia averted her gaze so as not to meet him eye to eye."
"Moments like this were no longer a rarity. Rowan loved his wife. He really did. But, the longer he stayed here, the less he felt he understood her. The less he felt she understood him."

al "If you wanted, maybe I could help?"

"Rowan waved her away."

ro "I’m alright on secretarial work. What I’m working on is picking out between-"

"Now it was Alexia’s turn to dismiss him. She strutted closer, swaying her hips side to side."

show alexia 2 necklace aroused at midleft with dissolve

al "That’s not what I’m talking about."

"She sat down on his desk, legs hanging to the side and cleavage hanging down near his face. He could smell the scent from her. The musky combination of perfume and desire."

al "It’s alright. You can keep working. I just want to do something to ease your tension...Give you a bit of relaxation."

"Rowan tilted his head." 
"There was something quaint about the effort. Innocent flirtation between husband and wife. It wasn’t the kind of sexuality that Bloodmeen was historically known for."

menu:
    "Let her approach.":
        $ released_fix_rollback()
        jump handleCareSex
        
    "Send her off.":
        $ released_fix_rollback()
        "Rowan shook his head. A noble effort on his wife’s part, but not what he was looking for tonight."
        ro "Not tonight. Lives depend on me doing this work. If I screw up it can cost us entire fighting forces. I can’t distract myself. No matter how enticing the distraction."
        if avatar.corruption > 60 and all_actors['alexia'].corruption < 31:
            "He didn’t mention his feelings towards her or the seduction effort in general. Maybe it was just too tame…"
        show alexia 2 necklace concerned at midleft with dissolve
        al "...Oh."
        "Alexia recoiled backwards, until she was sitting straight up. Her eyes returned downcast, where they couldn’t meet Rowan’s. It made them feel further apart than they actually were…"
        if NTR == True:
            $ change_relation('alexia', -5)
        return
        
label handleCareSex:

"Rowan looked up and down at his expectant wife. She was watching at him closely now. Her eyes took on a doe-like softness. Seeking approval and validation."
"Rowan put his document down. She was making all this effort. What would be the harm in a bit of indulgence? It wasn’t like Rowan didn’t feel pent up."

ro "Alright, I think there is a desk work position for you available."

show alexia 2 necklace happy at midleft with dissolve

ro "I’m still going to be focusing on my work though. You’re just here to give me a little bit of stress relief, alright?"

"Alexia nodded along with him."
 
ro "One more thing…"

"He reached down into a nearby cabinet and grabbed a small piece of string."

ro "You should put your hair up. It will make it easier."

if all_actors['alexia'].corruption < 31:
    "Alexia blinked twice. It took her a second to process his meaning. "
    
"His wife made a show of swaying her body and batting her eyelashes at him as she worked her hair into a ponytail. Rowan watched with a soft smile."

if all_actors['alexia'].corruption < 31:
    "She was fumbling a little bit, but it was cute."
    
else:
    "Rowan knew enough by now to gauge a partner’s skill. Alexia’s movements were smooth and catlike, but he was able to catch the odd slip up here and there. Not bad, but yet..."
    
al "There we are. Shall I get started?"

#cg1
scene cg445 with fade
show rowan necklace happy behind cg445
pause 3

"Alexia slipped under the desk. Shortly, Rowan's pants had been worked down to the floor, and his wife’s lips were wrapped around his manhood. He let out a soft groan in response to the sensation but otherwise went back to the document."
"He did still have work to do."

show cg446 with dissolve
pause 2

"Alexia bobbed her head along softly. Back and forth in a steady rhythm. The sounds of slurping emanated out to the rest of the room. If someone walked in, it would be hard to miss what was happening."
"But, Rowan continued to focus on his work. He jotted down notes. He looked over the latest production reports coming from the occupied territory."

if liurialSex == True:
    "Spending his work days in the castle with a certain elf had improved his ability to focus on work in a great many circumstances."

show cg447 with dissolve
pause 2

"But, there was only so much buildup that he could feel before it drew his attention. Alexia was bobbing her head in a steady rhythmic pattern. Up and down. It made her ponytail flip around in chaos."

if all_actors['alexia'].corruption > 31:
    "She even put her tongue into the work. It was positioned low in her mouth right where it would run right along the sensitive underside of his cock. She definitely hadn’t known that technique back in Arthdale."
    
"It all felt good. Only...not quite good enough."

show cg448 with dissolve
pause 2

"It didn’t take him long to notice that he wanted more. This was fun, but it was drawn out. Almost boring."

if avatar.corruption > 60:
    "Besides, wouldn’t it be a bit more fun to hear her choke a bit?"

"Rowan gripped her ponytail at the base and held it loosely as she bobbed her head up and down. This wasn’t unusual by any stretch of the imagination. But, that was just the first step."

ro "I think it’s time to pick up the pace."

#cg1 var 2
scene cg449 with fade
show rowan necklace happy behind cg449 
show alexia 2 necklace aroused behind cg449 
pause 3

"Alexia only had a second to react before Rowan added force to grip. He forced her head down and then back up with his hand. Her hair became a handle to control her head. She gasped in surprise, but the sound was muffled by his cock."
"Now Rowan was completely in control of the pace. Her mouth was just like any other hole, and he felt her teeth brush softly against himself every time he forced her cock deeper into her throat."
"Alexia sputtered, gasped and squirmed. This was not a way that they commonly played. It was harder, more forceful. She could breathe during a blowjob reasonably well, but throat fucking wasn’t something they did together very often."
"Yet, she didn’t try to stop him nor even protest too strongly. She was going along with it."
"Rowan closed his eyes and just let himself enjoy the sensation. Alexia wriggled underneath him, but obediently acted as a good fuck hole."

show cg450 with dissolve
pause 2

"Each stroke he tried to push deeper, harder. Her mouth was warm and wet. He sought pleasure in its depths."

al "Mmm! Mmm!"

"Alexia whined but still continued not to resist his hand. A passive doll moving as directed. The odd cough here and there joined the loud wet slapping sounds of penetration."

al "Mmmmmm!"

ro "Just relax. I’m almost…"
ro "Almost…"

"He tensed his back. He was right there. The early waves of pleasure already touched him, beckoning onward. But, it was still frustratingly far away. Rowan groaned out, but his orgasm didn’t arrive any faster."
"That is why Rowan sped up his hand. He forced Alexia’s head up and down at a dizzying pace. It resembled the rapid hand movements from when he’d stroke his own cock. "

show cg450 with dissolve
pause 1

al "Mmmm! Mmmm!"

ro "There…"

#cg1 var 3
show cg451 with dissolve
pause 2

"Rowan’s eyes fluttered and a stream of hot white cum shot down his wife’s throat. With a final groan, he let go off his grip on Alexia’s hair."
"She fell to her hands and knees sputtering and groaning. Rowan barely noticed as he let himself get lost in the post-orgasmic bliss."
"He let himself glide that way for a few seconds. But, he returned to normal all too fast. His eyes opened."

show cg451 with sshake
show cg451 with sshake
scene cg452 with flash
show rowan necklace happy behind cg452 
show alexia 2 necklace aroused behind cg452 

"Alexia was still sputtering on the ground. Her face had become an absolute mess. Tears strolled down her cheeks. Spit and cum drooled from her coughing lips. Her nose even leaked a little bit of snot. "
"There was even some cum in her hair. She’d pulled back a bit as he came."
"She was a mess."

if avatar.corruption < 61:
    "Without thinking, Rowan grabbed a small handkerchief that he kept around and passed it down to her."
    al "Th..Thank you."

"Rowan backed his chair out, to let her free. But, it still took her a minute of sputtering and recovering to return to basic functionality."

al "That was...intense…"

scene bg6 with fade
show rowan necklace happy at midright with dissolve
show alexia 2 necklace concerned at midleft with dissolve

"Rowan chuckled softly to himself."

ro "You’re kind of cute like that. "

al "If you...say so..."

"Alexia sighed. She was keeping her eyes low. She was avoiding his gaze all the more now. But, there was a lot of hesitation in the way she moved and spoke. Her brain was still processing what happened. Either that or she needed more air."

al "..."

al "I didn’t hate it…"

"Rowan tilted his head slightly."

al "If you want to do it like that again...I wouldn’t hate it…"

"There was another silence that fell on the room. Rowan looked to the work on the desk. There was still much to do, but he had made good progress today."

scene black with fade

"Rowan led her first to some water and then back to his room. He couldn’t get over the contrast of her crying face to her innocent expression earlier. Rowan couldn’t help but feel like she learned something tonight..."

$ change_corruption_actor('alexia', 5)
return

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

label rowans_reward:

scene bg9 with fade

"Soft footsteps disturbed the night time dark of Rowan’s room. Someone was awake and moving. Step step step. As they approached the bed, there was a sudden flash of activity."

#rowan necklace naked angry
show rowan necklace naked neutral at midleft with dissolve

"In a single swift movement, Rowan had drawn his sword and pointed it at the newcomer. His eyes were still sluggish with sleep, but his eyebrows narrowed."

ro "You’ve made a huge mistake tonight, intruder."

"There was a figure in a long black cloak standing in the centre of the room. With Rowan’s sword pointed towards him, he pulled backwards towards the door."

quest "Be easy, Hero Rowan. I am here on friendly business."

ro "In the middle of the night?"

quest "The best time. Fewer eyes on you."

"Rowan lowered his sword slightly. Whoever this was didn’t seem hostile just yet. Best to hear what his reasoning for such a late visit was."

#rowan necklace naked neutral

ro "Why won’t you show yourself then, friend?"

quest "I’m not anyone of concern. It’s what I know that matters."
quest "One of the sellswords in the castle has been pilfering artifacts. He has an entire sack of inexpensive relics hidden beneath his sleep quarters. Should be going by the name of Z’rathil. I have left further details and evidence on your desk."

"Rowan raised an eyebrow."

quest "I hope that Jezera finds the information useful."

"Rowan rolled his free arm and then shifted his sword to the other arm to continue stretching. It was late, so he wasn’t at his most rational. Still, something was clearly off here."

ro "You could simply deliver this to Jezera yourself, you know? Why am I the middle man?"

"The figure remained still."

quest "Perhaps having you be the one to tell her is the point? There are some people in the castle she trusts, and some whom she does not."
quest "I take my leave now. I hope this is the beginning of a productive relationship."

"The figure gave a short bow and made slowly towards the door. The wheels of Rowan’s brain turned. If he rushed forward, he could probably stop his departure. But, whoever his visitor was, it seemed that he genuinely wished Rowan no harm."
"When he departed, Rowan locked the door behind him. Better to make sure that was locked more often now. On the desk, there was a letter just as his guest had mentioned."

if week > 61:
    "Rowan stroked his chin. Of late his skills at intrigue had been improving, if only from more opportunity to practice. Whoever this was, he benefited from Rowan being the one in possession of the information."
    "Still, Rowan couldn’t deny that it wasn’t exactly bad for him to give off the impression of being more effective..."

if alexiaSeparateRoom == False:
    show alexia necklace neutral at midright with dissolve
    al "...Huh?"
    "In bed, his wife was stirring. Too much commotion in the middle of the night tended to do that."
    ro "Go back to bed, Alexia. I’ll be there in a moment."
    "Rowan looked again at the letter on the desk. There would be time for it in the morning."
    
scene bg18 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with dissolve

"That afternoon, Rowan was at Jezera’s desk handing over all the information he’d gathered. He wasn’t about to leave things to the letter, although it did contain a great deal of information. Rowan had wanted further proof."
"Now he was sharing the results of this small investigation with the letter's true recipient."

je "This is a great deal of evidence."

ro "The benefit of being the one doing the paperwork. You can fool a man, but you can’t fool the numbers. If something goes missing they won’t add up."

show jezera neutral at midright with dissolve

"She looked him up and down, before returning her glance to the papers."

je "Uh huh."

"She leaned back in her chair, holding her morning goblet of wine. She picked one of the documents and lazily ran her gaze over the text."

je "The total amount stolen here is no mere trifle. Had he taken all of this, it would have been a notable impediment to our capacities."
je "But, the real threat would be the sudden appearance of items of Bloodmeen origin in the marketplace. I don’t think you know much about black markets, do you?"

"Rowan shook his head."

ro "I’m afraid not."

je "They’re fascinating places. I’ll take you to one someday."
je "But, it wouldn’t do for word to spread about what’s going on here at this stage. Catching him has been of great service."

"Rowan bowed his head slightly."

ro "I am your humble servant."

if avatar.corruption < 31:
    show rowan necklace concerned at midleft with dissolve
    ro "My only request is that nothing too bad happen to him. He is just an opportunist, not something worse."
    ro "May I have your word that you won’t kill him?"
    show jezera happy at midright with dissolve
    "Jezera rolled her eyes."
    je "After all the men you’ve dispatched or helped dispatch, you are concerned about some common thief?"
    ro "..."
    "Rowan sighed."
    ro "Killing with necessity and killing without it are two different things."
    "Jezera giggled to herself."
    je "You’re an insatiable heroism slut. You know that? One of these days I’m going to break you of that."
    ro "..."
    je "Fine fine, I’ll just send him to the dungeons until he learns his lesson. That should make us both happy, no?"
    "Rowan nodded. It was about as good of a result for the man as could be expected. It wouldn’t be pleasant. Rowan could attest to that from first-hand experience. But, he had tried to rob demon lords, so it wasn’t like he shouldn’t have expected consequences."
    show jezera neutral at midright with dissolve

"Jezera put the paper down and stretched out."

je "You will receive some sort of special compensation. Service above what is required deserves reward above what is standard."

if society_type == "feudalism":
    je "It’s the proper duty of a liege to her subjects, no?"
    
if avatar.corruption > 60:
    ro "Oh?"
    "This entire little information exchange was working out rather nicely for him."
    
else:
    "For a moment, Rowan almost said he didn’t deserve it. But, he managed to stop himself in time. Best not to make Jezera question where the information came from any further."
    
je "I will think of something. You may leave, my hero."

scene black with fade

"Rowan nodded and took his leave from Jezera. He didn’t quite know what she meant by a reward, but he would just have to find out in time."
"As he left, he thought about the cloaked figure from before. Would this be the last time he got information from that source?"

#training yard bg
scene black with fade
show rowan necklace neutral at midleft with dissolve

"Rowan struck at the training dummy set up in the yard over from different angles. It was less about learning some new techniques as just to keep his skills fresh. His mind whirred with the different patterns to reinforce in his muscle memory."

show jezera happy at midright with dissolve

je "You could make this more of a show for me. I mean, do you truly require a shirt for this kind of training?"

ro "Good day, Mistress."

"Rowan lowered his sword and went down to one knee. Internally though, he was less than pleased about having his training regiment disturbed."

je "Don’t make such a big fuss about it. I’m only stopping in for the moment."
je "An excellent idea for a reward just came to me, and I wanted to give you the good news."

"Rowan raised an eyebrow. Jezera’s excellent ideas had a mixed track record."

je "After giving it some consideration, I decided that you are in need of some good, old fashioned relaxation. I do work you so hard, don’t I?"
je "For that reason, I’ve instructed Shaya that should you ever go to the brothel complex, you are expected to receive personal service. No charge or restrictions."
je "She was just telling me the other day that you’d stopped by to see one of her shows. Now you can have the real deal instead."

if rowanGaySex > 0 or raeve_keep_rowan_claimed_helayna == True or eleanorCaveSex == True or avatar.corruption > 31:
    "Jezera giggled to herself in a girlish tone."
    je "You may not be lacking for sexual escapades, but how often do you have a chance to spend the night with a trained courtesan of Qerazel?"
    
if avatar.corruption < 31:
    "Rowan gave a loud sigh. Of course, that was her idea for a reward. "
    ro "I am a married man, Mistress."
    "She faked a yawn."
    je "Are you now? I forget sometimes."
    je "It’s not that you’d be the first man with a ring on his finger to fuck a whore."
    "As she walked, she kept on circling around, arriving at a sword rack. She toyed softly with the pommel of one of the weapons as she spoke."
    je "Do it or don’t do it. It’s your reward. But, you have only to visit Shaya and she will take proper care of you. Got it?"
    "Rowan bowed his head. It wasn’t like she was forcing him to visit Shaya. Antagonizing Jezera was a luxury that he could only indulge in so often."
    ro "Very well. Thank you."
    
else:
    "It wasn’t like he’d never thought of the courtesan since she’d first arrived. Still, he’d never thought to ask for something like visitation rights..."
    je "Shaya is quite the prize, I assure you. I’ve tasted her on more than one occasion. When I say this is a reward, I mean this is a reward."
    ro "She does seem quite experienced…"
    "Jezera gave a dark smile."
    je "Indeed. If you want to indulge, simply go down to the brothel and pay her a visit. I’m sure she’ll enjoy it as well. "
    
je "Now then, I believe that should just about cover it. I will leave you to your male nonsense. Ta ta."

hide jezera with moveoutright

"Rowan panted softly and let his sword fall from his grip. He thought of the reward he’d been offered. "
"Since his last visit down to Shaya, the investigation parchment he’d drawn up had laid untouched. He was a busy man, and as fascinating as Jezera’s strange friend was, she was not a priority."

if shayaClueScore > 1:
    "But, a further visit might shed more light on her. Especially if such a visit entailed a longer one on one session."
    
"Still, if he went this time, it wouldn’t just be to watch, would it? It would be to actually fuck her."

ro "..."

menu:
    "A reason for pause.":
        $ released_fix_rollback()
        show rowan necklace concerned at midleft with dissolve
        "His lips tightened. Visiting her to watch a show was one thing. But, actually sleeping with a courtesan was something else entirely. Could any information he gained from such an excursion truly be worth it? Perhaps it would be better to leave this “gift” in its box."

    "A necessary evil." if shayaClueScore > 1:
        $ released_fix_rollback()
        "He put a hand to his chin. It would still be worthwhile, if only just to make progress on his little investigation of the brothel keeper. The mysterious woman and Jezera had a past together. This just provided a deeper opportunity to figure it out."
        
    "An exciting prospect.":
        $ released_fix_rollback()
        show rowan necklace aroused at midleft with dissolve
        "He smiled softly. He still had vivid memory of the way the Qerazely courtesan had danced upon the obsidian cock statue. If that’s what she could do to an inanimate object, what could she do with the real thing?"
        $ change_base_stat('c', 5)

$ shayaPrivateShow = True

return

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

label a_private_dance:

$ privateDanceSeen = True

scene bg24 with fade
show succubus neutral at midright with dissolve


"In the rose scented rooms of the brothel, two Succubi giggled together. It seemed that the latest guest had attracted some attention."

succ1 "Did the general himself come down to pay us a visit? Awe, how sweet! Gotta inspire the troops."

hide succubus neutral with dissolve
show succubus 2 neutral at midright with dissolve

succ2 "Well, since he came all the way down, I think that we should show him some of our famous hospitality. "
succ2 "And by we, I mean me."

show rowan necklace neutral at midleft with dissolve

"Rowan leaned against the wall by the entrance hallway wall with his arms crossed. But he smiled gently at the antics of the two demons. It was like a child’s game for them."
"Even as he listened to them babble, his eyes scanned the room, looking for something worth observing."

hide succubus 2 neutral with dissolve
show succubus neutral at midright with dissolve

succ1 "You!? I don’t see why he’d want to spend his time with you when I’m around. Not that you’re bad, of course. But, you’re maybe...the tenth most attractive woman here. Cute in your own way, but not in my league."

hide succubus neutral with dissolve
show succubus 2 neutral at midright with dissolve

succ2 "You tell such silly jokes, sister. It shows what a great personality you have. A good thing too, because it helps you make up for..."

"The playful back and forth came to an abrupt end when a fourth person joined them. "

show shaya happy at edgeleft with dissolve

sha "I fear, my sweet girls, that he’s not here to see either of you."

hide succubus 2 neutral with dissolve
show succubus neutral at midright with dissolve

succ1 "Madam!"

hide succubus neutral with dissolve
show succubus 2 neutral at midright with dissolve

succ2 "Madam!"

sha "I heard there are some very vigorous orcish men waiting to spend time in your company. Do you really want to keep them waiting?"

"The two demonesses gave each other a smile and then rushed off to the other end of the facility. They were probably never going to be allowed to sleep with Rowan, no point in pretending otherwise. "

hide succubus 2 with dissolve

"Shaya approached Rowan and made a motion halfway between a bow and curtsey. Rowan respectfully nodded back in turn."
"From beneath her veil, he he could make out olive skin and perfect cheekbones. Her eyes, bright and attentive like a pair of green jewels went uncovered."

sha "Rowan. It is good of you to come and visit. I had heard from Mistress Jezera to expect your return, but I had waved it away as an enticing but unlikely prospect."

if avatar.corruption < 31:
    show rowan necklace concerned at midleft with dissolve
    "Rowan shuffled slightly in place. How could he explain a whim like this?"
    ro "I hadn’t expected to grace you either. But, I am here nonetheless."
    "Shaya’s face remained difficult to read behind her veil. It definitely seemed like she was smiling though."
    sha "Well, what truly matters is what happened, not why. Now that you have come to visit me, Rowan, I will surely have to convince you it was worth doing. A whim needn’t be a bad thing. Not with the right person."
    "She tilted her near-bare hips to the side. Rowan had to marvel at how flawless her features were. She was like a sculpture"
    
else:
    show rowan necklace happy at midleft with dissolve
    "Rowan smirked to himself."
    ro "Now, why would you think that? I was promised a reward, was I not? It would be rude to Jezera not to take her up on her hospitality?"
    "He reached around her body and gave her ass a squeeze. It was soft and supple. Just the right size too. Shaya had a body from a dream."
    sha "Now now. There are private rooms for that, Rowan."
    
"She took him by the hand and playfully led him past elegant sofas and glimmering statues deeper into the building. Around him, there were the odd sounds of moans and sighs. It seemed like a quiet day here to him."

ro "By the way, didn’t you have an attendant? Nia or something?"

sha "Lia. She isn’t on duty today, I fear. The girl has yet to develop a proper work ethic for the profession."

show rowan necklace neutral at midleft with dissolve

"She led him to a small room. It held little more than a lavish bed and a side table with a pair of chairs and some fruit on the table. The small space felt more close and intimate than claustrophobic. It smelled of exotic flowers."

if avatar.corruption < 31:
    "Rowan stood around, awkward from lack of experience with such a high class escort. When she saw that, she helped him down into one of the seats."
    
else:
    "Rowan selected one of the chairs for a seat. And took a position with his arms crossed over his chest and his eyes trained square on the beautiful brothel madam."

ro "So...where do you normally begin?"

"Shaya put a finger to her lip as though she didn’t know what to do next. Her voice came out soft and sweet."

sha "I have found that men like it when I set the mood for them. Is that how you would like me to begin, Sir Rowan?"

if avatar.corruption < 31:
    "Rowan nodded softly, unsure how else to respond."

else:
    ro "I think I like the sound of that. Go ahead."

show rowan necklace aroused at midleft with dissolve

"Rowan watched in rapt attention as Shaya started to dance. Not a belly dancer’s gyrations, but slow flowing movements where the momentum of each movement went into the next. Her hips moved from one side to the other like sloshing water in a cup."
"Up and peak and down. She added spinning to this simple motion, turning and rocking her hips. With her back to him, she bent lower. Almost a squat. Her shapely rear stuck out to him. Beckoning him forward."
"Rowan leaned slightly forward in his seat."
"Still dancing, she moved towards him, first circling the small area behind his chair. Her hands resting on his chest, massaging him through the fabric of his clothes. "

#cg 1
scene cg580 with fade
show rowan necklace aroused behind cg580
show shaya happy behind cg580
pause 3

"His breathing picked up pace. Now she was in front of him, body pressed closer. She broke into the same dance as before. Flowing and turning. The flowing shake of her hips and rear. Only, now she was practically on Rowan’s lap."
"Every time she pressed against him it was a little closer and a little closer. A bit more skin. A bit more sensation. He could feel her body through his pants. It rubbed against him."
"He reached out without thinking and ran a hand along her thigh. He marveled at the feeling of it. No bumps. No imperfections. Just soft and smooth. Shaya let out a soft sigh. She was not unaffected by the touch."

if avatar.corruption > 31:
    "Rowan smirked to himself."
    
"She recoiled soon after the touch began, drawing herself just outside of groping range. Though she hardly seemed offended. In fact, rather than admonishing him she instead reached behind her back. To grasp at the knot that held her top up."

#cg1 - var 1
#scene cg580 with fade
#pause 3

"Her back was turned to Rowan, so he couldn’t see it fall free. But, a moment later she turned back to him, now holding her breasts in her hands. Still covered, if only, by her fingers. Even as she gave him more, she still held back."
"Now she resumed her sensual dance, only with her hands trained on her breasts instead. Rowan still felt the push and touch of her body close to him. Only now he was starting to get painfully stiff. "
"Rowan groaned. He wanted more. He wanted to fuck her."

if avatar.corruption < 31:
    ro "Please, stop with all the teasing. This is too much."
    
else:
    ro "Get on with it already. I’m waiting."

"Shaya bowed her head and answered in a soft voice."

sha "Of course, Rowan. As you say."

#cg2
scene cg581 with fade
show rowan necklace aroused behind cg581
show shaya happy behind cg581
pause 3

"The teasing was over. Her hands drew back, revealing the fullness of her bosom to Rowan. Was there a part of her body that was not perfection? She was unreal. He marveled at them even as she sunk down to her knees."
"From her new position, there was one action, one mission, that she set her sights on. His cock. Her fingers dexterously worked his stiff cock free from his pants, and started on the task of working it. Rowan’s eyes closed and he leaned his head back in his seat."
"She was slow and delicate. Every motion was practiced. Not unsure, but instead continuing to move into the next action like the turning of a wheel. This woman knew how to work a cock."
"Her other hand searched for his prostate and began to work it as well. Her eyes, those jewels, were transfixed. Every movement, every ounce of her attention, every potential avenue of pleasure. It was all focused."
"Rowan gave a low grunt and sputtered slightly. This wasn’t the most intense sexual high he’d ever felt. There was something lacking. An emotional connection. But, who could match this woman in terms of pure skill?"

if rowanJezSex > 0:
    "Even Jezera, with all of her sexual skills, lacked this degree of precision."

"There was one rising frustration. She wasn’t going fast enough. He wanted more."

if avatar.corruption < 31:
    ro "Faster. Fuck. You have to go faster than that. You have to...you have to..."

else:
    ro "I said stop playing around. Stop teasing me. Put your all in it!"
    
sha "Whatever you desire. My body is here for your pleasure. In fact…"

#cg3
scene cg582 with fade
show shaya happy behind cg582
pause 3

"Her hands went to her breasts once more. But, not to cover them. No, it was to lift them together like an offering to him. Held aloft with just enough spacing for a small gap between them."

sha "Use me. Please, Sir. Use me."

scene shayatitjob 
show shaya happy behind shayatitjob
pause 3

$ shayaSex = True

"In seconds, he’d thrust his cock forward into the gap. Her body was there for his pleasure. She pressed them together. Now they engulfed him. The moaning and grunting started up again. He was thrusting forward and she was rocking her body in response."
"She let him fuck her as though she were dancing. The flowing movements and steady precision. It all was there. Her body rocked and gyrated. "
"It all made him groan out uncontrollably. His senses had been overwhelmed beyond his capacity to rationally process it."
"But, Shaya made a sound too. Just not one Rowan had expected to hear. She sang. A small quiet hymn in a steady rhythm. Almost a lullaby. It was framed by the strange scales of Qerazel, and she used it to time the sway of her breasts. "

sha "He left me crying down by the shore. The weep of the lily."

"Rowan was almost out of the chair. Each thrust met by the countering force of Shaya’s movements. Like the tide striking and receding from the shoreline."

sha "The soft dreams of a whore. Loved when I’m pretty."

"Her eyes closed. Her body was acting on instinct and the unseen force of their bodies in unison. The dance continued."

sha "The smile will slowly return to my face. A courtesan’s special charm."

"Rowan groaned out loudly. There wasn’t much longer he could hold it in. He was about to..."

sha "For there are others who want a taste. A customer cannot harm."

show cg647 with sshake
show cg647 with sshake
show cg648 with flash
pause 2

"....White cum shot in an incoherent splatter over Shaya’s breasts. Rowan sputtered and grunted, before sinking back into his chair." 
"Shaya didn’t pull back. She milked his cock for the very last drops before sinking backwards. The cum was already drying on her breasts. "

scene bg24 with fade
show rowan necklace aroused at midleft with dissolve
show shaya neutral at midright with dissolve

"A short time later, Shaya had cleaned off her breasts and robed back up. She selected the other open chair to sit in. Rowan was already mostly recovered from his adventure. Still, his breath came out in ragged rasps."

ro "Has anyone ever told you that you’re very good at this?"

sha "From time to time.  The appreciation is...welcome."

"She grabbed an apple from the table and stared at it. Its shiny surface offered her a reflection of her own veiled face. She could only look at it for a few seconds before offering it to Rowan. "

if avatar.corruption < 31:
    "He accepted it from her hands and took a bite."

show rowan necklace happy at midleft with dissolve

ro "How did you learn all of this? The Dancing? The sexual techniques?"

sha "There is a place called {i}The Empress of the Waters{/i}, in Qerazel. A brothel. It’s quite a marvelous place. {i}Jezer’aca{/i} called it her favorite place in the world once. As children, we’d look at its marble exterior in awe. The techniques they practice are esoteric...and effective."

if shayaClue1:
    ro "Is that the building this place is based on? You suggested when we met that this was not an original design."
    "Shaya blinked softly."
    sha "...Yes. An exact replica. {i}Jezer’aca{/i} likes it when things are perfect. So why not copy the best?"

show shaya happy at midright with dissolve

"She smiled softly to herself. Her hand slowly ran down the bare side of her body. Rowan’s eyes kept coming back to her perfect curves."

sha "The song from before was a...training aid from back then..."
sha "Sister knows magic and intrigue. But, my arts are beauty and grace. Pleasure, too. I serve them as a sculptor serves his art or a singer serves hers."
sha "I’m good at it. I make people happy. Who would not enjoy making people happy?"

#diplomacy check - very easy - TODO
"Rowan’s mind was still, however, on the song that she had carried even while in the midst of pleasuring him."
ro "The song was beautiful. But, it wasn't very happy, was it?"
show shaya neutral at midright with dissolve
sha "The best songs seldom are."
ro "The impression I get from it is...that the courtesan training they give you isn’t very pleasant, is it?"
"Shaya nudged his shoulder gently."
sha "Not all the girls come entirely willing. But, we needn’t discuss such things. What man truly wishes to think of such things in the bed of a beautiful woman?"
sha "When one eats a fine cake, they ought to consider the splendid flavor. Not the apprenticeship experiences of the baker."

menu:
    "Agree.":
        $ released_fix_rollback()
        ro "You’re right, I suppose. It’s not something a normal man concerns himself with here, is it?"
        ro "But, you never know. Maybe I have a strange fetish for empathy. Surely you’ve encountered rarer kinks than that?"
        "Shaya giggled."
        sha "Then empathy? My word. You’re scandalizing me. Are you about to suggest something so unchaste as holding hands next?"
        
    "Disagree.":
        $ released_fix_rollback()
        ro "Maybe. But, when I eat a cake, I’m not eating a person. Maybe if it was a person, I’d care a lot more about how it came to my plate."
        "Shaya’s bangles rang slightly. She brought her wrist to the front of her veil and sniffed at her own hand."
        sha "A strange sentiment. Who is to say that a cake isn’t alive? That it doesn’t feel it every time you bite into it? Were that it could, would you know?"
        sha "Further, who is to say that I am not a cake? I’ve been told I’m quite delicious by men who’ve been with me in the past. You could have a taste for yourself if you’d like, Rowan."
        "She giggled into her hand."
        sha "You do me an undeserved honour with your concern. But, it is appreciated nonetheless. You’re a kind man."


"He let himself go back in the conversation and considered her question from before. Who wouldn’t enjoy making people happy?"

show shaya happy at midright with dissolve
$ shayaClue5 = True
$ shayaClueScore += 1

"The question had been rhetorical, but Rowan couldn’t help but think of an answer to it."

ro "But, Jezera…"

sha "...Is my best friend. She’s the entire world to me, and has been my entire life. If I can ply my trade for her benefit, that’s all the better."

"Rowan raised an eyebrow. He had rarely even heard anything pertaining to Shaya outside the context of Jezera. Just what was the friendship between the two of them?"

if shayaClue4:
    "The only thing he had to go on was what Alexia had told him…"

ro "You really love her, don’t you?"

#shaya annnoyed 
show shaya neutral at midright with dissolve

sha "It is bad form to accuse a courtesan of loving anyone, Sir Rowan. A whore in love is a failed whore."

#shaya neutral

sha "..."

#shaya sad

sha "But, yes. I love her with all my heart."

"She giggled to herself in a low tone."

sha "Perhaps I am not quite so good at this as you’d have me believe."

"Rowan laughed."

ro "I wouldn’t say that at all. Not at all."

show shaya happy at midright with dissolve

"They sat and chatted for a little longer. For all of her meek and deferential demeanor, Shaya was a surprisingly excellent conversationalist. Witty and capable of speaking on a wide range of topics."
"Rowan’s mind started to fixate on one particular thing though…"

show rowan necklace neutral at midleft with dissolve
show shaya neutral at midright with dissolve

ro "Why the veil? I had thought it a part of the costume at first. But, I do not believe I’ve seen you without it."

sha "A question I field often when around a customer for long enough. I’ve heard that it catches the eye."
sha "I like to think about the meaning behind objects. When I’m not working, of course. To a courtesan, a veil is a barrier. Feelings and the Art. Behind it is the truth. In front is the performance. But, men and women do not seek me out for the truth, do they?"

"Rowan’s eyebrows narrowed."

ro "So you never service customers without it? None of them ever see your face?"

sha "There would be no point to it. No man has ever chosen to forgo pleasure with me on account of such a mere trifling. "

menu:
    "Ask to see her face.":
        $ released_fix_rollback()
        label shayaSeeFace:
        ro "What if I was the first?"
        ro "I’m not just some thrill seeker visiting the brothel. You’re someone who I have to rely on, and someone who has to rely on me."
        if avatar.corruption < 31:
            ro "I want to know the person I’m trusting. I want to see your face."
        else:
            ro "If there’s a secret to learn, I want to be the one to learn it. Especially one being held by so beautiful a woman."
            ro "Show me your face."
        "Shaya brought the back of her slender hand to her mouth and used it to hide a soft giggle. She gave a lazily stretch, arching her back away from the chair. Rowan’s eyes were briefly caught on her breasts."
        sha "More flirtation? I must have had quite a profound effect on you, hrmmm?"
        ro "That’s not an answer to my question."
        sha "..."
        sha "No, one must suppose it isn’t."
        sha "But, I must refuse. I will never allow you...anyone...that privilege. This one thing is private to me. Would you not forgive a woman who sells her body the right to keep one thing for herself?"
        if avatar.corruption < 31:
            ro "I hadn’t realized it was so important to you. I’m sorry."
        else:
            ro "Sounds like there’s no way to convince you, huh?"
            sha "There is not. But..."
        "A faint smile was visible beneath the veil. She reached out and put a supportive hand on his knee."
        sha " I appreciate the intent, at the very least. At the end of the day, the concern of most men goes as far as a warm hole to do their business."
        show shaya happy at midright with dissolve
        sha "What you want...well that’s a thing I will need to learn for myself, hmm?"
        $ shayaClue6 = True
        $ shayaClueScore += 1
    
    "Let the topic drop.":
        $ released_fix_rollback()
        "Rowan bit his tongue softly. Shaya certainly seemed to be implying that it was private to her. But, still...the curiosity remained."
        menu:
            "Remain silent.":
                $ released_fix_rollback()
                pass
            "Ask to see her face.":
                $ released_fix_rollback()
                jump shayaSeeFace
                

"Shaya slowly rose from her seat and stretched her arms and legs. She was like a fighter preparing for a battle."

sha "Let us put a page mark here, shall we? You are too important a man to waste your hours in the afterglow with one such as myself..."

"She leaned over his chair and nuzzled against his cheek. It was almost a kiss. The smell of her perfume hit his nostrils hard."

sha "...But, {i}Jezer’aca{/i} has put me at your service whenever it is what you desire. This will not be our last opportunity to speak, w" 

show rowan necklace happy at midleft with dissolve

"Rowan sighed."

ro "You make a good point, Shaya. I’m sure that I’ll have more questions about your...operations to take me back here."

sha "And I shall be open and eager for said questions. My operations are yours to explore."

show shaya happy at midright with dissolve

"Rowan thought he saw her smile as he departed, but with the veil obscuring his view it was hard to be sure."

scene bg9 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan found himself at his desk again that night. In his hands was the familiar piece of parchment with that one central question at the top."
"{i}Who is Shaya?{/i}"

if shayaClue1 == True or shayaClue6 == True or shayaClue7 == True:
    "As he thought back over the encounter, now with the benefit of greater scrutiny, the quill in his hand started to move."
    if shayaClue1 == True:
        "For the first time, Rowan cleared out one of his prior questions and wrote in an answer."
        "Beneath {i}“What place is the Brothel a replica of?”{/i} Rowan put down an answer. {i}“The Empress of Waters. The Brothel she was trained at.”{/i}"
    if shayaClue5 == True:
        "One of the key discussions that stood out to him centered on her training. She had tried to hide it, but whatever had happened to her must have been grueling. Perhaps even traumatic. The song she’d sung had been almost a lament."
        if shayaClue2 == True:
            "Rowan scratched his chin. Was that the reason Jezera considered her trustworthiness beyond reproach? Surely not…"
        "Still, it left him with a new question to add to the page."
        "{i}What happened to Shaya during her training as a courtesan?{/i}"
    if shayaClue6 == True:
        "There was the matter of her veil. Her response to his request to remove it had seemed reasonable. But, how adamant her refusal was stunned him."
        "His eyebrows furrowed."
        if shayaClue4 == True:
            "Yet, he’d heard Alexia tell him that she’d actually seen Shaya’s face before and found her to be a beautiful woman."
            "Why wouldn’t a trained and practicing seductress want to flaunt that element of herself? It was madness. Yet, perhaps that proved that her stated rationale was actually true?"
        else:
            "His mind was left to run rampant speculation on the nature of Shaya’s face. Why else might she refuse to show her face?"
            "Was she ugly? Did she have a scar? Was her face recognizable somehow? Just what was she trying to hide?"
            "Somehow, Rowan felt he’d know so much more about the woman if he could just see her face clearly."
        "He wrote another question on a blank stretch of parchment."
        "{i}Why does Shaya wear a veil?{/i}"
    
    "When he was finished, he slumped back into his chair. His arms hung loosely at his sides. This was progress, but his curiosity still burned. He’d just have to pay her more visits in the future."
    if avatar.corruption > 30:
        "What a {i}horrible ordeal{/i} to have to go through to get information."

else:
    "Yet, every time he put quilt to parchment, he could think of nothing to write. Had he really learned nothing of substance from the entire excursion?"
    "What had he even been doing that entire-"
    show cg647 with fade
    pause 2
    "Right."
    scene bg9 with fade
    show rowan necklace aroused at midleft with dissolve
    "Instead of continuing his futile efforts to write, Rowan just went deeper into his imagination. Picturing her dance again but this time totally naked. Picturing her those soft supple breasts bouncing this time as she rode his cock."
    "He could almost hear her call out his name in that sing song voice of hers."
    scene black with fade
    show shaya happy at center with dissolve
    sha "{i}Rowan.{/i}"
    scene bg9 with fade
    show rowan necklace aroused at midleft with dissolve
    "Rowan blinked twice."
    "Today had been a bust, so to speak. But, he’d have to go back and visit her again soon. He wasn’t done investigating her, after all!"
    $ change_base_stat('c', 5)


$ shayaPrivateShow = False
$ shayaSilkAvailable = True 
return
