
label bedroom_window:

$ julietSexAvailable = False


scene black with fade
show juliet neutral behind black

"In her bed, Juliet was stirring. There was a tapping at her window. Something small was striking against it."

juli "Mmm…"

"She groaned and rose. Nothing was there from her first glance. She approached the window slowly and pushed it open. Her left hand was at her eyes, wiping the sleep dust from them."
"That was when Rowan climbed high enough to come into view."

#cg1
scene black with fade
show juliet neutral behind black
show rowan necklace happy behind black

ro "Good evening, Juliet."

show juliet shocked behind black

#if agility is low - TOD
    #Rowan took a moment to catch his breath. It had been an easy climb, but even so, that kind of acrobatics were clearly not his specialty.
    
"She fell back in surprise with both hands over her mouth. He hadn’t been able to make it out before, but she was dressed in a silky white night dress that showed much of her form. If anything, it reminded him of the one Alexia liked to wear."
"Rowan rose to a sitting position on top of the windowsill." 
"He kept his posture unobtrusive. There was a fine line of decorum in a situation like this. The acceptability depended entirely on how much Juliet wanted him to be there."

ro "I’m sorry to have startled you. If my presence is unwelcome, I can-"

show juliet neutral behind black

juli "W-wait!"

#cg1 - var 2
scene cg596 with fade
show juliet neutral behind cg596
show rowan necklace happy behind cg596
pause 3

"Juliet brushed herself off and rose to her feet. She walked towards him. Slow. Cautious. It was less about him as about making a sound."

juli "I don’t mind. Just... don't be loud. This is my brother's house. He cannot know there is another person in the room."

"Rowan nodded softly. Of course, Rowan knew to come when she was here. At other times she stayed at her father’s smaller quarters in the city or even the lodge. Both had heavily armed guards. A much riskier approach."

juli "Why visit me, though? Why at this hour? "

ro "What do you mean? I wanted to see you."

"Juliet’s cheeks flushed. She turned her head from him, in a bashful girlish way."
"Ameraine had confirmed that she heard rumors of a secret passageway in and out of the lodge. One that people associated with Werden and his children. Sometimes they’d leave and no one would see their departure."
"Meanwhile, Juliet loved her stories. The entire purpose of sneaking in through the window like a thief in the night. To her, it would be more like the knight and his ladylove."

juli "...I wanted to see you again too…"

if avatar.corruption > 60:
    "Exactly."

"Rowan reached down and plucked up her chin. He used it to guide her head higher."

ro "Look here. In my eyes."

#cg1 - var 3
scene black with fade
show juliet neutral behind black
show rowan necklace happy behind black

"Rowan kissed her on the lips. It was a lingering meeting of lips on lips. He didn’t indulge in too much tongue. It was meant to simulate a loving kiss. Juliet, of course, was very bad at it. Her mouth didn’t open enough. Rowan wouldn’t have been surprised if this were her first kiss."

if avatar.corruption < 31:
    "It was charming. Mostly."
else:
    "Rowan didn’t think much of the kiss. He’d been with people who actually knew what they were doing."

"On the other hand, Juliet was having the time of her life. Her eyes were sealed shut, and she rose from his lips every few seconds for heavy breaths. When their lips met again, her body shuddered."

if rastAlly != "werden":
    #cg1 - var 2
    scene cg596 with fade
    show juliet neutral behind cg596
    show rowan necklace neutral behind cg596
    pause 3
    "Then, in a sudden rush, the kiss broke. Juliet pushed herself backwards. Her eyes flew open. Something was wrong."
    juli "Wait. I-"
    juli "I really shouldn't be doing this. It would be wrong. Disrespectful. Impious."
    "Rowan remained in place. His muscles tensed, but he couldn’t show it. He had to keep his voice soft and his posture open."
    ro "My Lady?"
    juli "Wait. Just wait."
    "She sucked in air. She still could not go more than a second without shooting him glances. It was a confusing mix of expressions So much so that Rowan didn’t quite grasp what feelings she was trying to convey."
    juli "I cannot do this, Rowan. I cannot. What would people say? What if people knew? In stories, the noblewoman elopes with a commoner. But, they're stories. They don't have families. Fathers. Honour to consider."
    juli "In the storybooks, it's not complicated."
    "Rowan nodded slowly. This was a delicate situation. He had to pick his words carefully. She took a step closer."
    ro "It doesn't have to be more complicated than you make it. It's just you and me. Here. In this room."
    #cg1 - var 3
    scene black with fade
    show juliet neutral behind black
    show rowan necklace neutral behind black
    "Rowan leaned down and placed a little peck on her lips. Juliet certainly didn’t refuse the kiss."
    #cg1 - var 2
    scene cg596 with fade
    show juliet neutral behind cg596
    show rowan necklace neutral behind cg596
    pause 3
    #Conditional in sentence based on deception skill. - TODO
        #ro "No one will know. We won't do anything outwardly to show our (Love/...Love). We're safe from all eyes. Every vulture who might see otherwise. "
    ro "We can have our storybook. You can have your storybook. Exactly like you’ve always wanted."
    "Juliet went very quiet. Her eyes closed softly."
    juli "Right here. In this room. Our storybook."
    juli "If we do this...promise me you'll stay with me when the fighting is done."
    juli "I've heard you are married. I know it's wrong. But, when you've defeated the demons again, you will set your peasant wife aside and come be with me. By then, your own lordship is surely guaranteed."
    if society_type == "feudalism":
        "Rowan thought about the way politics had developed back at Bloodmeen."
        ro "My lordship would be guaranteed by then...yes…"
    juli "So promise me. Promise me that I would be your woman, and you would be my man."
    "Rowan looked down into her eyes. They shone with a fierce determination right now, but they were still so soft and round."
    "She would not have made a bad wife. She was pretty and intelligent and came from good stock. Most of all, she loved him."
    "Or at least she loved a story of him."
    menu:
        "Make the promise." if rastAlly != "crevette" or (rastAlly == "crevette" and avatar.corruption > 60):
            $ released_fix_rollback()
            "Rowan looked deep into her shining eyes."
            ro "I promise you. You’re the woman for me. It doesn’t matter who I’m with until the end of the war. It doesn’t matter who I married."
            ro "When the fighting is done, I will return to Rastedel and make you my wife."
            if avatar.corruption < 31:
                "Rowan thought about Alexia. She was waiting for him back at the castle." 
                "But, Alexia’s safety depended on his ability to get results for the twins. That, in turn, meant he needed Juliet’s absolute trust."
                "Lying burned. But, he had to do it. For her."
                if all_actors["alexia"].relation < 30:
                    "Even if she never truly appreciated him for it."
            elif avatar.corruption > 60:
                "Such an easy lie. How would she even have survived in life with so little sense? If Rowan had not come along surely someone else would have played with her heart."
            else:
                "Lying this way was...distasteful, of course. But, there was no getting around it. Rowan needed a way to take out Werden surgically during the fighting. This was the only way it could be done."
            "Juliet took in his words with a near blank expression. Like she couldn’t even process them fully."
            #if deception is high - TODO
                #"When he finished, Juliet’s smile instantly stretched wide. The moment she’d processed his words, her expression had instantly dropped all worries, all concern."
            #else:
            "For a lingering moment after he finished, there remained touches of doubt. A furrowed eyebrow. Pursed lips."
            "Her expression only softened a little bit after he was done. A lingering trace of doubt remained. But, just a trace."
            #rejoin
            "I shall gladly be your lady tonight, my hero."
            jump julietPreSex
            
            
        "Don't make the promise." if rastAlly != "jacques":
            $ released_fix_rollback()
            ro "..."
            "Rowan’s expression darkened."
            ro "I can’t do that, Juliet. I’m not going to leave my wife when the war is over. You and I have only just met."
            juli "I-"
            "Rowan shook his head again before she could speak. Juliet’s entire posture deflated before his eyes."
            ro "We can have this moment here and now. But, it won’t last forever. I can’t promise anything more than that."
            #cg1
            scene black with fade
            show juliet neutral behind black
            show rowan necklace neutral behind black
            "Juliet turned away from him and walked towards her bed. Rowan could only see the back of her head. Yet, her thoughts were painfully clear to him."
            juli "I see."
            juli "Thank you for your honesty. I...I appreciate that."
            juli "..."
            "Rowan heard a small sniffle. The sound of someone trying to hold together that which is coming apart. His face sank."
            juli "Please leave."
            "The next time Juliet would look back, Rowan would not be there. He would already be making his way down the wall and far away. He left Juliet to construct her own story of what had happened."
            "As he made his way down, he heard a sound from her room that could only be sobbing."
            $ released_fix_rollback()
            $ prevent_tile_exploration()
            $ push_to_previous_tile()
            return

else:
    #cg1 - var 2
    scene cg596 with fade
    show juliet neutral behind cg596
    show rowan necklace happy behind cg596
    pause 3
    "Juliet slowly broke the kiss. But, only so far as needed to speak. Her body remained pressed close to him."
    juli "I don’t know how father will feel about this…"
    "Rowan smiled softly to reassure her."
    ro "Do you think I came through the window in the dead of night if I planned to tell your father?"
    ro "Still, he and I are allies. You saw us standing together at the parade. Before this is done, I’m likely to be a lord. You understand that."
    ro "To tell the truth, I’ve come to see him as something of a father figure here over the last few weeks."
    ro "Do you really believe he’d find me the most unsuitable of liaisons?"
    "Juliet went silent. There was not much to this. Sure, the two cavorting around would be a scandal if discovered. But, as far as Juliet and her father were both aware, Rowan planned to remain in the capital as an ally for months or even years to come."
    ro "To me, the real question is simply. Is this what you want? This liaison is entirely your choice, my lady."
    "She nodded slowly, hiding her face. Rowan could have sworn he saw a sparkle from her cheek."
    juli "…I’ve heard it whispered by some that you are secretly a divine. I don’t know."
    juli "But this, right here, is…is the thing I’ve wanted most since I first saw you."
    jump julietPreSex


label julietPreSex:

#cg1
scene black with fade
show juliet neutral behind black
show rowan necklace happy behind black

"Juliet marched back from the window, away from Rowan, once more. Her arms hugged right around her waist. Rowan leaned forward, eyes trained entirely on her. Yet, he did not rise from his perch. He wanted to give her a little bit of room."

ro "Lady Juliet?"

juli "A moment."

"Juliet reached an old and quite ornate dresser and fumbled her way inside. From it, she drew a large candelabra. Rowan silently watched as she lit it and set it in place on the dresser. Afterm she rushed to another part of the room and pulled out another source of light."
"The entire time she was nearly vibrating with energy. Her lips softly hummed a sweet little bird’s song. He was surprised her small frame could contain all of her excitement."
"Soon, several candles burned around the room, giving the place a warm glow. She giggled to herself softly. "

show juliet happy behind black

juli "Well, um…this is my first time. I want it to be perfect."

if rastAlly == "jacques":
    "Rowan kicked his feet. Did he really have to go all the way? Perhaps there was a way that did not involve going that far."
    menu:
        "Take her to bed.":
            $ released_fix_rollback()
            jump julietSex
            
        "Get cold feet.":
            $ released_fix_rollback()
            show juliet neutral behind black
            ro "Wait!"
            "Juliet tilted her head to the side. She held an unlit candelabra in hand."
            ro "You misunderstood me, My Lady."
            ro "I had not meant to take things quite as far as that."
            "Juliet’s face turned scarlet."
            juli "Oh."
            ro "What I had intended instead, at least for tonight, was to simply lay with you. To kiss you. To feel your heartbeat close to mine."
            "Rowan struggled to find the right words to say. He had to figure out how not to sound disinterested. He could not tell her how little he actually wanted to fuck her."
            "Juliet looked down at her feet. Was she disappointed? Relieved? Rowan could not say with anything approaching certainty."
            ro "It is meant as a promise, my lady. For what is to come when the fighting is done."
            "That solidified it. She nodded stoically. The lady waiting for her lover to return from the war. That was a role she understood."
            "So it was that Rowan took Juliet to bed. The two curled close under the covers, lips firmly locked together. It was difficult to tell how long it was that they kissed, but certainly the time was in hours rather than minutes."
            "By the time it was done, Juliet stared at him with totally captured eyes. She’d do what he wanted."
            jump julietSexEnd
        
else:
    pass
    
label julietSex:
show juliet neutral behind black

$ julietSex = True

"With the room properly lit, she next went for a stick of incense. As it burned, the room quickly started to fill with a smoky aroma. Even the scent had to be perfect."
"Rowan continued to wait. This was her mental preparations for a momentous event. Any effort to rush her would be stupid."

if avatar.corruption < 61:
    "Not to mention cruel."

"Now, illuminated by candle light, she turned back to him. Her eyes trailed the floor. Moments later, her nightgown would as well. With shaky hands, she went to her shoulders and worked the silk fabric off. It silently fluttered to the ground, leaving her body totally exposed to him."

juli "I’m ready."

"Rowan’s eyes trailed her near unearthly pale body. He found a single freckle near her crotch. Something he was sure no man save a relative had ever seen before." 
"She stood in an uneven stance, gripping her forearms. This was her first time being seen, totally and completely seen, by a lover."

juli "What should I do, Rowan? "

#cg2
scene cg597 with fade
show juliet neutral behind cg597
show rowan necklace happy behind cg597

"Rowan advanced into Juliet’s room. Her body shivered to the vibrations of his steps. So soft. So supply Not a hard muscle to be felt. It was so easy to guide her to the bed and mold her into position. He laid her back with her hands gripping the bedframe and her legs properly spread."
"Juliet grunted and whimpered at the feel of his touch. But, she followed along with the lead of his hands."

juli "Like this?"

if avatar.corruption < 31:
    ro "Mhm. That’s right. (You’re doing well)"
    
"Rowan ran a hand down from her collar bone over her belly slowly. He trailed his fingers between her breasts, all the way down her belly. Again, she shivered under his touch. The feel of his hand highlighted for her present state. Exposed."

juli "Are you g-going to-"

ro "Not yet. You’re not ready yet. You’re almost certainly way too dry for that."
ro "You’ve touched yourself before, right?"

juli "Well-"

"To illustrate the point, Rowan’s hand finally made its way between her legs. It took half a second of exploration to find her clit hidden beneath her folds. Rowan nodded knowingly. Not wet enough. He’d need to do something about that."
"For her part, Juliet reacted as he had planned. Her eyes fluttered and her lips formed an open gasp."

#juliet aroused

juli "Ah…"

"Rowan had to be careful. Too much stimulation would overwhelm her. So, he set about working her up as needed. Brushing her clit in a steady rhythm. Touching over and over. Each time, Juliet would wiggle or let out gasps. The feedback to tell him it was working."
"Rowan controlled the pace. He brought the flow of tension higher and higher. All it took was steadily working at her clit. She might not have experience, but her body was responding."

ro "You’re enjoying yourself, aren’t you?"

juli "Mff."

"She buried her face in her hands. But, her ability to hide her growing arousal was fading. Now the wetness of her sex and the spasms and shaking of her body told Rowan how effective his touch was."
"He buried a hand into his pants to work his cock stiff. Not so difficult with the visual encouragement he was getting."

if avatar.corruption < 61:
    "Eventually, he shifted from rubbing her clit to pumping fingers inside of her. First, a single finger, but then up to two. It wasn’t as effective a teasing method, but it would give her body a bit more experience with penetration."
    "For all of his goals in this room, actually causing pain was not one of them. She should enjoy herself too."

"The dynamic of the situation could not be more clear. Rowan knew how to please a woman from intimate experience. Even without directly topping, he was the one guiding her."

juli "R...Rowan…"

"She was getting closer. The movement of his fingers  were having the intended effect. Her breath was growing shallow and fast. Cheeks bright red, eyes out of focus. The unmistakable signs of a body in the throes of need."

juli "I’m feeling really...uh...hot..yeah…"

ro "You want the real thing now, huh?"

"She nodded weakly."

juli "Please...yes..."
juli "Just...gentle. Okay?"

"Rowan pulled his hand back slowly and put it to his nose. Her scent hung on his finger tips. Her body wiggled eagerly beneath him."

ro "Okay. Gentle. I can do that."

"Rowan worked his cock out of his pants. Juliet glanced out towards it with a mixed expression. Wide eyes and hungry parted lips."

ro "Gentle."

#cg3
scene cg598 with fade
#juliet aroused
show juliet neutral behind cg598
show rowan necklace happy behind cg598
pause 3

"That was how he entered her. No rough movement. Just slow and gentle. He couldn’t have gone fast or rough if he tried. Her hole was just too tight. Rowan had to work harder and harder the deeper he penetrated."
"Juliet whimpered and groaned with each inch that he sunk into her. Not all of those groans were pleasure." 
"Rowan looked down and saw red on his cock. Just a small bit, but enough to tell him what had happened. He’d taken her virginity."

ro "My Lady...Juliet...Do you wish for me to keep going?"

"She bit her lip and nodded. She was beyond words now."
"Rowan tested it slowly. Rocking his hips back and forth in a light pattern. The tightness of her pussy was more than enough to stimulate him, even with that small motion. Her insides clung to him, developing the experience of being shaped from his cock."
"There was something erotic to it all. Rowan didn’t truly want her. But, the animal part of his mind swelled with pride at the sight of the small amount of blood on his cock."
"Juliet let loose an increasingly loud torrent of noises. The whimpers started to slow as the pain from her cherry being popped started to parse down. Every new sound was more similar to a moan."
"Rowan groaned. His pace picked up slightly. But his moves were still small and soft thrusts. He was not so much railing her as rubbing her insides with his cock. The tight squeezing drove him closer and closer to orgasm by the second. Every texture of her body was his to feel."

juli "Today is...Today is safe…"

"The fact that she was even able to speak at all was to her credit. Even now, she was only growing more overwhelmed by sensation. Her head buried even further into his shoulder. It was her tether to the ground."
"The smell of the room stank of sex. Not even the incense could clear it out. All of her perfect preparation couldn’t match the smell of real sex."
"He pulled out slightly. The mixture of her juices, his precum, and the blood left his cock coated in a glistening layer of fluid. He breathed in once. And then he entered her again. Now her pussy was more ready. No longer was he just rubbing. He was going to fuck her like he meant it."
"From there, the pleasure only built. So too did her movements. The muffled whimpers from her lips grew harder to control. All of it was building towards a fever pitch. A climax."
"Rowan bucked hard. Already he could feel the vibrations running through his shaft. He was almost there."

#cg3 var 2
scene black with fade
#juliet aroused
show juliet neutral behind black
show rowan necklace happy behind black

ro "There. Fuck. There. Mm."

"Rowan groaned out. That was all he could take. There was a small sputter and then he let loose. Juliet’s pussy overflowed with white hot semen."
"He leaned back, panting. Juliet curled up closer to him, still whimpering. No doubt, as his movements slowed and his cock began to soften, the pleasure began to fade. The pain would still linger."

juli "I…"

show juliet happy behind black

juli "I didn’t hate that."

"She sighed weakly."

juli "I could get used to that…"
juli "Was I good? Did I please you?"

"Rowan strokes her hair softly. Her face was still buried in his shoulder. For once, he could tell the full truth."

ro "You did, Juliet. You did."

label julietSexEnd:

scene bg9 with fade

if avatar.corruption < 61:
    show rowan necklace concerned at midleft with dissolve
    
else:
    show rowan necklace neutral at midleft with dissolve
    
"Rowan arrived back at his room and sealed the door behind him. After the visit, he’d needed to return home quickly. Going to her room had always been risky. What would have been required had he actually been caught by her father?"

if julietSex == True:
    "After they slept together, Rowan had stayed for hours to cuddle her and listen to her feelings. If she regretted it, she certainly hadn’t shown anything of the sort while Rowan had been there."
    
"She’d been sad to see him leave so soon, of course. He’d promised her they’d meet up again in a few weeks. There were big events happening in the city and he’d see her again when things were more stable."
"Of course, when things actually would be more stable, either he’d be dead or the city would be under new management. But, she believed him all the same."

if avatar.corruption < 31:
    "Juliet was a sweet girl. Well bred. Intelligent and curious. Rowan could not blame her for this. More hardened and world weary people had been hoodwinked by his ruse. What chance had a sheltered and romantic young woman had?"
    "Rowan was not quite sure who to blame for any of this."

elif avatar.corruption > 60:
    "Simply too easy. Juliet had practically been dropping her undergarments for him from the moment of meeting. Was it really so wrong of him to oblige her by shoving his cock in? She did want this, after all."
    "And besides, it let him get what he really wanted. Werden had taken so much from him. So it would only be justice if Rowan got to take something of his."

else:
    "Rowan sighed. That had been easy. It constantly amazed him the way people would let him into their halls of power and homes."
    "He was not so incredible a liar as to fool everyone. Indeed, when he was unrecognized, his schemes were much harder to pull off."
    "It actually made him angry. How dare she make it so easy for him? How could she be so stupid as to not try to figure out if the real Rowan matched his reputation? It was her own fault, really."
    
if rastAlly == "jacques":
    $ julietKey = True
    "Rowan pulled out a balled up handkerchief from his belt. A token of her favour was what she had called it. Like all the lords and ladies give to each other. In truth, it mattered much less than what it was wrapping around."
    "Rowan had asked her if she knew of a secret way into the Lodge. A way to see her without the guards knowing he was there. As a member of the Werden family, she was more likely to have such a means than anyone."
    "The handkerchief he held was wrapped around a key. A key to a tunnel leading into the lodge. With it, he could get in or out without running into the normal guards."
    "Juliet had given him a way in. A way to meet her Father."
    "Rowan closed his fingers around the key."
    
if julietSex == True:
    $ change_base_stat('c', +5)
    
$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

#####################################################################################
#####################################################################################
#####################################################################################

label guess_whos_coming:

$ guessWhoSeen = True

scene bg33 with fade
show rowan hood neutral at midleft with dissolve

"It was not yet mid-day as Rowan crossed the central boulevard. Since retaking the abbey, some life had returned. A few more vendors returning to their normal spaces. More food and crafts being sold. But, it still lacked its usual energy."
"Rowan didn’t stop to stare. He had a date."

show mystery neutral at midright with dissolve

"As he passed one stall, a head turned."

myst "The Noble District today..."

#if lower perception (TO DO)
    #"Rowan kept on walking, oblivious to the fact he was being tracked. After all, he was hooded and the place was near empty."

#else (TO DO)
"The man turned and started to follow Rowan. He walked with a cat-like grace. But, at the first turn, even he was left blinking. Rowan was nowhere to be seen."

myst "Where exactly are you going."

"The man turned around...and Rowan was right behind him."

show rowan necklace angry at midleft with dissolve
#show mystery shocked

ro "You’ve been following me a good deal, haven’t you?"

"The man took a step back and blinked. Rowan looked around. They were right in front of the bridge now. Unfortunately, still on a well lit and populated pedestrian street. Certainly, he couldn’t draw his sword."

myst "Excuse me. I don’t believe we know each other."

ro "Yes we do. You helped me get into the Grand Camelia Lodge. I checked your name after, but none of the guards knew it."

"Rowan took a step forward. The man took a step back. The fading sun cast their shadows together on the ground."

myst "Ah. I do recall that."

ro "No one knew who you were either. You just used your signet ring to get the guards to open up for you."

show rowan necklace neutral at midleft with dissolve

"Rowan crossed his arms over his chest. The man must have been nearly a foot smaller than him. Certainly no match in a fight."

ro "Who are you?"

#mystery neutral

myst "An excellent question."

"He hooked his hands together behind his back and leaned forward a few times. A strange thought ritual."

myst "I suppose you could call me Sir Alek. Though, I never actually got the knighthood. Yes, that is my name."

"Valuable, perhaps. But, not an answer to the question."

ro "Sir Aleksi. Hrmm. And who do you work for?"

#mystery happy

$ mystery_name = "Aleksi"

myst "Myself, mostly."

show rowan necklace angry at midleft with dissolve

"That was enough of that. Rowan rushed forward, grabbing him by the collar of his fine shirt and lifting him up to his toes."

myst "Uh uh. I’m sure you’d love to throw me in one of those alleys and just have your way with me."
myst "But, we’re in a public place. "

"Sir Aleksi gestured around. Already a man and woman had stopped to stare. That wasn’t good. The cloak would not save him from identification with greater scrutiny."

myst "Even the great Rowan can’t go around attacking random citizens in the middle of crowded areas."

show rowan necklace neutral at midleft with dissolve

"Rowan scroled and released him. Sir Aleksi managed to land gracefully back on the heels of his feet."

ro "You know what I really want to know. Why are you following me? What are your intentions?"

"Sir Aleksi chuckled softly to himself."

#mystery neutral

myst "If you must know. I’m on your side. I am praying for your successful fortune. No one wants to see the {i}humans{/i} get what they deserve more than I."
myst "Besides, do you have a more serious grievance with me then simply that I helped you deal with an obstacle? I had not known lending a hand to be a grave offense."

show rowan necklace angry at midleft with dissolve

ro "..."

"Rowan sighed slowly."

ro "I suppose not. But, I do not take well to being followed. If you really do want to help me, you should stop skulking and tell me what you want so we can make a deal."

#mystery happy

myst "If ever I need your aid, I will be sure to approach you for it directly. You’ve proven a favor from your hand to be a most valuable commodity."

"Aleksi bent his hands back and forth in exaggerated movements as he spoke."

myst "In the meantime, however. Don’t you have...places...to be? People to meet? Unless you’d prefer to stay around and keep little old me company."

"Rowan scowled to himself. He was smart enough to know when someone was trying to play him."

ro "Next time I see you, I will not be quite so busy. I will force you to spill everything."

#mystery neutral

myst "To be sure."

show rowan hood neutral at midleft with dissolve

"Rowan turned on his heels and began the trek down the bridge to the Noble’s Quarter. Even with his eyes facing away, he still tracked the movements of Sir Aleksi to ensure that he didn’t continue to follow.
"

hide rowan with moveoutleft

"Sir Aleksi remained in place until Rowan was out of sight. Once the coast was clear, he made a dramatic show of burying his face in his hands."

myst "Tsk tsk. So many questions."
myst "I suppose that is why he was useful enough to make a pawn in the first place. The cost of doing business."


#rejoin

scene bg36 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan walked into the hall of the Crevette manor. It belonged to Lady Patricia’s brother, of course, but for all practical purposes, it was her home."
"Servants were rushing in and out of a room to the side. Their trays were laden with food and decorations."

ro "I apologize for my lateness."

show patricia happy at midright with dissolve

"A figure walked out from the room. Lady Patricia had her hair done up a bit neater today, and he could tell she put more effort into her appearance than usual."

patr "Rowan. Come in. Come in. We were just getting the last touches ready."

"Inside the room was a long table covered in a delicate tablecloth and all manner of food. A roast ham sat at the center. But, other dishes of meat, soups and salads, fruits and breads, sat waiting for them. A single servant stood with his head lowered."

show rowan necklace shock at midleft with dissolve

"Patricia moved to sit, but Rowan was still jaw agape. All this food in the middle of a famine?"

patr "Oh come now, Rowan. This isn’t your first dinner with a noble. Is there really a need for all the gawking? You must have expected this."

show rowan necklace neutral at midleft with dissolve

ro "Expect it maybe. Never used to it."

"Feasts like this had hardly been uncommon from Jezera and Andras. But, expecting restraint from either of them was a beginner's mistake."

patr "Well, based on how you dress to functions, I have no choice but to accept your answer. No one can draw the peasant out of you, can they?"

show rowan necklace happy at midleft with dissolve

ro "Don’t be too critical, My Lady. Appearances are everything. I’m a dirt general, so I have to dress like one."
ro "If I started bursting through doors in silks, I wouldn’t really be “the Rowan” anymore."

if avatar.corruption < 61:
    "In truth, it was mostly a matter of comfort. But, he’d been advised since back after the war to put his choice in terms that the high born would understand."
    
"Rowan settled down for the meal, and soon had appetizers on his plate. One of the servants came around and helped stuff a napkin over his vest. "

if avatar.corruption < 31:
    "Rowan silently told himself that he’d make sure the leftovers, at least, made their way up to the northside slums."

"Considering his dining companion, it was no surprise when Patricia raised her glass in a toast. Rowan toasted her back."

patr "To our friendship. With your reputation and my standing, we’ll accomplish what neither could have managed alone."

ro "To our friendship."

"He leaned the cup back. The wine was sweet and tasted good. But, Rowan truthfully didn’t have much ability to distinguish between wines. He only drank so much as to be polite. He had to remain sober today."

ro "Has the situation changed on the council since my recent intervention?"

"She nodded eagerly, but before answering took another large gulp from her goblet."

patr "Oh, the world hasn't turned upside down. But, my {i}esteemed{/i} colleagues have been respecting my proposals much more now that they know you're working with me."

patr "You browbeat that stuffed shirt knight so badly, he's hardly said a word to me since."

"They both gave a laugh."

patr "Only Marianne has still been getting in my way. It's really quite the change."
patr "I might even call the feeling intoxicating."

"Rowan took a bite from a strange cabbage roll in front of him. It was stuffed with some kind of bean that he didn’t recognize. But, he forced his smile to freeze, if only to be polite."

ro "Are you sure that’s not the wine."

"Patricia rolled her eyes."

patr "Don’t be a lightweight. I’ve barely started drinking."

show rowan necklace neutral at midleft with dissolve
show patricia neutral at midright with dissolve

"She bit down into her food greedily. Rowan waited for her to settle it down before he took the opportunity. Tonight, he needed to take their alliance further."

#if low diplomacy (TO DO)
    #"Ameraine had even been coaching him in preparation. He was more of a fighter than a talker, after all."
    
ro "I only see one problem with the situation…"

patr "Hrm?"

"He let a beat pass."

ro "What happens when Werden wins?"

"Patricia looked at him as though he were gibbering nonsense. She didn’t even stop taking bites of ham from her plate."

patr "What do you mean? When Werden wins I shall be done with that self-important princess Marianne forever and I can run the council as I see fit."

"Rowan made a show of continuing to wolf down his food. Best not to break the spell of casual conversation just yet."

#if low diplomacy (TO DO)
    #"Though in the process, he swallowed a piece of pork so fast he had to beat his chest to prevent hiccups from setting in."
    
ro "Yes yes, but Werden will be taking her place at the table’s head. "
ro "Marianne’s priests will likely be replaced with Werden’s favorites. All of the advisors who’d been denied council seats in the past because of association with him."

"That got her attention. She poured more wine into her goblet slowly, not taking her eyes from him."

patr "That’s nonsense. I worked out more favourable terms then that when I first negotiated my way into the faction. The administration of the state is my purview."
patr "Do you take me to be a fool?"

"Rowan shook his head hard."

ro "No. Of course not."

"He lowered his face so as to duck under her gaze. Still, he could feel it intensifying on him."

ro "Only, based on experience, I can tell you my name will be worthless again the moment the capital has a sizeable standing army again. You’re going to have fewer allies."
ro "...And the question stands. Does Werden treat you like an ally that he needs for your abilities? Or like someone he gives power to because he wanted a power player on the present council?"

"She kept her eyes him, only taking breaks to work at her goblet. But, he could have sworn he saw her shift slightly in her seat."

patr "Werden is honourable. He probably never kissed anyone until he married. If he promised me the council, he’s going to follow through. He is not one to renege simply because of a power shift."

show rowan necklace happy at midleft with dissolve

"Rowan leaned back in his chair."

#if low diplomacy (TO DO)
    #"Ameraine had predicted this line of conversation as well."

ro "Ah, but is he especially generous?"
ro "He’ll give you exactly what he specified, but not one shred more. Not even his continued friendship."
ro "Did he promise you control of the government itself...or just control of the council?"

"She grimaced softly. That had been enough to break her stare."

patr "I don’t much like this conversation topic, Rowan."

#if higher deception (TO DO)
show rowan necklace neutral at midleft with dissolve

"Rowan bowed his head softly. To press too hard and too fast would be a grave mistake."

ro "Of course, My Lady. Apologies for overstepping."

"She sighed and gave a wave of her hand."

patr "It’s fine."

#else (TODO)
    #ro "I am simply saying that-"
    #show patricia annoyed at midright with dissolve
    #"She held out her hand. Her eyebrows narrowed slightly."
    #patr "Enough."
    #show rowan necklace concerned at midleft with dissolve
    #"That got the message across. Rowan went silent. He had already pushed further than he should have."
    #ro "My apologies."
    #show patricia neutral at midright with dissolve
    #patr "No no. You’re alright, Rowan..."
    
show rowan necklace happy at midleft with dissolve
show patricia happy at midright with dissolve

"The topic on the dinner table moved past Rowan’s true aims. Rowan let himself get caught up in the flow of the conversation. Patricia, of course, was a skilled host and regaled him with all sorts of stories from years past."
"Rowan interjected here and there but largely focused on making sure the food on his plate was not put to waste."

patr "...In truth, I probably should have married him. But, he wanted me to stop working and simply be the lady of his castle."

ro "I take it that isn’t your style."

"She let out a tiny burp after a swig of wine. They both chuckled at it lightly."

patr "Wasn’t then. Probably still isn’t now. If anything, I’d rather be the one with my husband managing the house. If I didn’t love my brother, I’d resent him for getting our holdings."
patr "Of course, I told the man no. Flat out."

"She sighed softly and looked to the side. The servant had long since left them alone together."

show patricia sad at midright with dissolve

patr "Gave up the best sex I will ever have for this stupid job."

"Rowan raised an eyebrow."

ro "The best sex? Really?"

show patricia happy at midright with dissolve

patr "Oh yes. He was a beast. When he got the hunger for it, he’d just go on and take me right there on the spot. Didn’t matter if it was in the bedroom or the common room."
patr "Once, the villagers by the family keep were holding a celebration for my family mere inches away, and we were making love in a hut inches away."

"She smirked darkly."

patr "Thin walls too."

"Rowan cracked his knuckles and leaned back in his chair. Opportunity always had a certain smell to it."

ro "Must have been a pretty good lover then. Though, I’m not sure about “best sex you’ll ever have”. There may still be opportunities to come."

"She rolled her eyes."

patr "More flirting? I’m ten years older than you are, Rowan. Well past my prime in the looks department too."
patr "Besides, aren’t you married?"

if all_actors["alexia"].relation >= 30:
    "That was a question he’d stopped to ask very frequently. Still, so long as this was all necessary for their mutual survival, it was still okay."
    
else:
    "When had that ever stopped him?"

ro "Would I be the first married man you slept with?"

"She shot him an accusatory glance. Yet, Rowan couldn’t help but notice that she hadn’t quite denied it."

patr "Besides the point. Why bother?"

"She leaned forward, flashing Rowan a teasing hint of cleavage."

patr "Is it a political game? Trying to seal our alliance with a bit of the ‘ol diplomacy in the sheets?"

"Rowan kept his composure and took a slight sip from his wine."

ro "You’re intelligent and ambitious. What’s not to want?"
ro "You underestimate yourself. You’re still quite a catch. If you truly wanted a husband, it would be no real difficulty for you to find one."

"She answered back with a far larger gulp from her goblet. If she kept going at this rate, there was a chance she might not even remember the night."

ro "If you’re not interested, I can always stop. I’m more than happy with the working relationship we’ve already established."

patr "I didn’t tell you to do that."

"The two stared at each other from across the table. It was almost a contest to see who’d break first. A contest he won."

show rowan necklace neutral at midleft with dissolve

"More time passed before they returned to a topic of substance. By then, a significant dent had been made in the piles of food. Thankfully, Patricia had eased off the wine ever so slightly. She’d reached the limit of what she could drink before impairment set in."

patr "About you spoke about earlier…"

ro "Werden’s willingness to cede power?"

"She nodded slowly."

patr "What do you propose that I do about it? If I find myself without a power base after the coup is over, how would I even go about avoiding being sent back to my home keep?"

"Rowan sighed."

ro "I don’t know. I’m not sure if there's anything at all you could do to reverse course if you found yourself in that situation."

show patricia neutral at midright with dissolve

patr "Then why bring it up?"

ro "So you don’t find yourself in that situation."

"Patricia slowly inched her goblet away. Rowan took in a deep breath. He had to put his words together just right."

patr "Make your damn pitch already. "

ro "Well, you won’t have power once things settle. But, after the coup starts, there will be a brief window of chaos when anything can happen. If you move fast, you can secure yourself a power base and a stronger position by the time the carrion crows arrive."
ro "Werden might not need you once Marianne is safely in chains. But, would you actually need him?"

"When Rowan was done, he expected serious consideration. Instead, he got a laugh."

show patricia happy at midright with dissolve

patr "A coup within a coup. You’re crazy."

show rowan necklace happy at midleft with dissolve

"He shrugged his shoulders. If she was treating it with a veneer of comedy, why stop her? It might make the topic easier to broach."

ro "You asked how you would go about dealing with the problem. I'm not actually suggesting you do it."

patr "Uh-huh."

ro "All of this fighting, here and in the countryside, could actually benefit you."

"Her finger lazily pointed across the long table towards him."

patr "Benefit me...and you too, I assume?"

ro "Possibly. If you were crazy enough to do something like that, you might need a partner to rely on."

"It would be best to pretend he did have a more selfish motive. She’d be looking for one anyway, and minor personal gain was an easier pitch then slavery to demon lords."

patr "I wouldn't be in this mess if I didn't have to rely on other people."

ro "Even friends?"

patr "The only reason we're discussing this treasonous hypothetical is because of your earlier reminder that trust without leverage is nonsense."

show rowan necklace neutral at midleft with dissolve

"Rowan sighed. Already he could see the blush from her cheeks start to fade. She was starting to sharpen up once more."

ro "Well, I could never take over for Werden myself. I'm a commoner. It doesn’t matter if I was ennobled. To the lords, I would always be a commoner."
ro "No one would ever put me in charge of anything. That just won’t happen for me."

"He picked up his goblet and sloshed it around. The wine swirled and danced."

ro "You're a well-respected administrator. And the sister to a lord of the west. You're not Werden, but the nobility would still bite their tongue and listen to you."

show patricia neutral at midright with dissolve

"Now it was her turn to recoil slightly. He could see her brain working in real time."

patr "So what you are saying, even if the Duke just happened to retire one day, you'd never be able to take any power at all without my help?"

ro "That is the essence of it."

patr "It's an interesting idea."
patr "As a fantasy."

"She looked slightly off to the side, as though not truly speaking to him."

patr "Still, I should be thinking about what to do if that bastard tries to double-cross me though. It’s prudent advice."

ro "Mhm. He does have a way of doing that, doesn't he? I would know."

patr "So I've heard."

scene black with fade

"This time it was Rowan who drank from his goblet, and Patricia who only took a cursory sip. Her eyes were still vacant. Shadowboxing the conversation they’d just had instead of paying attention to the present."
"They’d both sobered more still by the time dessert was brought out. The servants wheeled out a large, multi-layered cake. To join it were several dishes of fruit."
"The servants departed once more once places were finally found for the new additions on the table. Rowan and Patricia both stared. There had already been so much food that much of it would go to waste. The prospect of more just baffled him."
"Patricia, at least this time, seemed to agree."

scene bg36 with fade
show rowan necklace neutral at midleft with dissolve
show patricia neutral at midright with dissolve

patr "Hrmm. Perhaps I should have instructed them not to prepare so much. I had hoped you’d be a bigger eater."

ro "Perhaps, dessert can be skipped?"

"Rowan stood from his chair and started to move around towards the front of the table. Much progress had been made tonight. After another few meetings, he was sure that-"

patr "Wait!"

"Rowan froze in place. Patricia rose slowly from her chair and glided closer to him. He was honestly surprised she was able to walk perfectly straight again."

show patricia happy at midright with dissolve

patr "Considering all that smooth talk earlier, I’m surprised you haven’t asked for a goodnight kiss."

"She now stood only a few inches away from him. So close that he could smell the faint trace of wine still on her lips."
"He knew the way she was looking at him. He’d seen that face on Alexia before."

show rowan necklace happy at midleft with dissolve

ro "I did not know it was an option on the table."

patr "Why of course? I don’t recall saying it was..."

"She brought her thumb to her lips and bit it softly."
"The intention of her words couldn’t be clearer. Rowan could, of course, decide to indulge here. Or simply leaving her wanting and let her come back another night."
"One of the two options offered more...immediate upsides."

menu:
    "Give her what she’s been missing.":
        $ released_fix_rollback()
        jump patriciaSex1
        
    "Hold chaste...at least for tonight.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        "Yet, try as Rowan might, he couldn’t bring himself to take the next step. Maybe it really would be smarter simply to keep her strung out and eager for more."
        ro "Well, if you haven't said it's on the table, then clearly my choice not to ask was the right one."
        "She rolled her eyes but didn’t back away."
        patr "Clearly."
        "So, Rowan took the chance to lean down. His lips went to her ear. His voice came out heavy but quiet."
        show rowan necklace happy at midleft with dissolve
        ro "But the next time we meet..."
        ro "Well...next time anything can happen."
        "Patricia brought her thumb to her lip and softly bit it."
        patr "Is that a promise?"
        ro "It is."
        "Her eyebrow kept perched in challenge."
        patr "I’ve heard my share of promises from pretty boys. I will be very disappointed if you do not follow through."
        ro "I want nothing less than to see you disappointed, My Lady?."
        "Rowan lifted back to a standing position. He didn’t speak immediately. It was best to let Patricia stew on what he said until it was etched in."
        ro "Shall we call it a night?"
        "She looped his arm in his and together they made their way from the table. Rowan remembered the food a little bit too late to ask for the leftovers to be sent north. For some reason, that was the thing he felt most guilty about."
        $ released_fix_rollback()
        $ prevent_tile_exploration()
        $ push_to_previous_tile()
        return

label patriciaSex1:

"Rowan looked down at the table. It was still covered in food, many of the dishes merely tried, but mostly uneaten. It was a reminder of all of the food being wasted."
"With so much to eat, why not indulge a little bit?"

ro "You know, now that I have a closer look at it, perhaps I will have that dessert after all. "

patr "What-"

#cg1
scene cg799 with fade
show rowan necklace happy behind cg799
show patricia happy behind cg799
pause 3

"Patricia didn’t even have time to react to Rowan’s declaration before his hand was on her stomach. In a few moments, he pushed her hard enough to send her on the table." 
"A fish and bread-based dish plummeted to the floor. Rowan’s near-empty goblet of wine fell over, staining both the white table cloth and Patricia’s dress."
"If Patricia was mad about it, then it didn’t register on her face immediately. She froze up, still processing what he was doing. Then, a dark smile formed on her lips."
"Her hands went down to the hem of her dress and hiked it all the way up. Beneath were a pair of lacy blue panties. His pride was stoked by the small dark spot that had formed at the front."

ro "You invited a commoner and wanted to waste food?"

"Rowan moved to join her. He raised himself up by a knee so he could hang above the table. Patricia’s fingernails dug into the table cloth, ripping it slightly."

ro "You had to know I wouldn't like that, Patricia."

patr "What should we do about it, then?"

"She batted her eyelashes to him."
"Rowan scooped down a dish from one of the dessert trays. It was an apple dipped in a strange red sauce with the consistency of honey."

ro "Feast."

#cg1 - var 2
#scene black with fade
#show rowan necklace happy behind black
#show patricia aroused
#show patricia happy behind black

"He brought the apple down so that it was hanging mere inches from her face. The message was clear. With closed eyes, she took a bite."
"She groaned out through the material, as though she were gagged."
"Rowan leaned down to join her. His teeth dug into the other side of the apple. The taste of it was sweet. Sickeningly sweet. His lips stained red with juices."
"They let out their bite at the same time. The apple rolled away, leaving both of their faces a red mess. "

ro "Delicious. "

"His clean hand slipped between her legs. The soft lace gave way, and soon his fingers were softly working at her clit. Both of her lips were stained with juices now."

patr "More. More than that."

"At that cue, he pushed inward. Not merely content to rub, his fingers worked their way into her folds. He pushed them in and out. In and out."

patr "Ah. Yes. Mfph. Yes."

"Her eyes fluttered harder. The dishes continued to clatter, as she clutched the tablecloth hard enough to pull the creases out."
"All the while, the pumping of Rowan’s fingers picked up in pace. They slammed into her folds as hard as any cock."
"Yet, even as he did this, Rowan’s eyes kept on roving. There needed to be something more." 
"He found it in the nearby cake. Whoever had made it had no doubt spent hours getting all of the icing and cream just right. Rowan roughly dragged it over with his honey-covered hand."
"The force of movement almost knocked the cake over then and there."

#cg1 - var 3
#scene black with fade
#show rowan necklace happy behind black
#show patricia aroused
#show patricia happy behind black

"Then, using two fingers he roughly scooped up icing from the cake. Patricia’s eyes fluttered open to them dangling above her lips."
"She opened her mouth."
"Rowan dipped his fingers down into her mouth. A groan escaped her lips. In moments, his fingers were pumping in and out of her lips at only a slightly slower pace then the fingers working her pussy."
"Rowan couldn’t help feeling affected by the sight of her, wiggling and moaning in his hands. It was like he was fucking her from both ends at once."
"Only when he could feel all of the icing gone did he pull his fingers back from her mouth. A trail of sugary saliva drifted off."

patr "More..m…"

"If the lady insisted. Rowan scooped up more of the icing from the cake and resumed the process of pounding her from both sides. Her tongue swirled around his fingers, searching for as much of the cream as she could take."
"As that hand withdrew, his efforts to work her pussy only sped up. Soon the room rang with the sounds of lubricated contact."

patr "M-more. I want more."

"Soon a rhythm had been found. Her mouth invaded by icing. Her sex invaded by his fingers. Every time she finished lapping up the food, Rowan plunged his hand in to collect the next batch."

patr "More."

"This time, when he pushed the icing in, she opened her mouth so wide that his thumb accidentally went in. She suckled on that too, icing or no icing. Her hips rolled with his hands."
"It was to the point where she was more humping his fingers then being masturbated."
"In the frantic movement, One of her arms shot out and smacked against the cake. It went tumbling over the side on to the floor below."

patr "Don’t just...just use your fingers. More. More. M...more."

"Rowan backed up slightly. Both of his hands withdrew to his side. She was right. He needed to take this a step further still."

ro "Hmmm."

#cg2
scene cg798 with fade
#show patricia aroused
show patricia happy behind cg798
show rowan necklace happy behind cg798
pause 3

"Rowan eased himself from the table. Worked up to the point where her body was electrified, Patricia groaned and squirmed in his absence. More dishes of food clattered on the floor."
"The napkin he had been given earlier was still hanging beneath his chin. Rowan pulled it out and used it to wipe his mouth clean of the red honey sauce. Then, he slowly went down to his knees and placed his face between the noblewoman’s legs."
"Patricia’s hips bucked eagerly. The closer he got to them, the more they surged forward. They were seeking him."

#cg2 - var 2
#scene black with fade
#show rowan necklace happy behind black
#show patricia aroused
#show patricia happy behind black

"Of course, it would be rude to keep a noblewoman waiting when it was time for dessert. So, Rowan plunged his face into her cunt and started to eat away."
"A gasp rang out from atop the table, and another dish clattered to his side. All the while, his tongue plunged deeper into her folds."

patr "Rowan. Fuck. Rowan. More. More."

"Rowan’s tongue was a demon. It slithered in places no man had tasted in a long time. It made her feel sensations that Patricia would have ached for ages."
"Rowan was no stranger to this task. He darted it back and forth from her clit to her folds. Never so long as to be numbing. Always finding a new avenue of attack."
"Patricia’s body shook under him. Her voice came out cracked and broken."

patr "Rowan. Fuck. More. More. Ah."

"That was only proof he should pick up the pace. The process went on and on, each step Patricia’s movements only grew more frantic. Her voice only came out in higher pitches. With all the buildup, a reckoning was about to cum."
"Rowan first noticed it as an increase in the liquid at his mouth. Enough of the copper taste of pussy to overcome whatever flavors remained from dinner. But, it was just a prelude to spasms from the woman above him so intense it could only be an orgasm."
"Rowan rose to his feet slowly. He was feeling a bit on edge himself, from all the play. But, not so much so that he couldn’t keep his pants on."
"Patricia, meanwhile, was laying limp on the table. The only breathing that escaped her lips were rasping pants. Without Rowan there to hold up her weight, she even began to slip. He even had to help her down."

#cg2 - var 3
#scene black with fade
#show rowan necklace happy behind black
#show patricia aroused
#show patricia happy behind black

"Yet, even as he helped Patricia away from the table, he couldn’t help making one last sweeping glance at it."
"The tablecloth was in tatters. The cake and many of the dishes, including the remains of the pork, were splattered on the floor. Knocked over wine spilled slowly from some of the sides." 
"It was like the ruins of a town after a dragon attack."
"He settled Patricia softly near the wall and went back to grab a strawberry from a fruit dish that had survived. The sweet taste masked the remnants of Patricia’s personal flavor."

patr "Well...I haven’t done anything like that in...a long time."

"She groaned and worked herself up to her feet."

ro "I merely hope you found it to your tastes."

"The pun earned him a dirty look from her. But, also the hint of a smile."

patr "...Indeed."

scene bg36 with fade
show rowan necklace neutral at midleft with dissolve
#show patricia aroused
show patricia happy at midright with dissolve

"She brushed a segment of cake that still stuck to her dress off. The entire outfit was such a hopeless mess that the prospects of washing it clean seemed dim."

patr "Next time, I’m not going to be satisfied with merely fingers and tongues. I hope you understand what you’re getting into."

"Rowan had to suppress a chuckle. How much of the past year of his life had been driven by getting into things he didn’t understand?"

ro "I promise you, my lady. The next time we meet up, I will show you delights you have not experienced in a long time. Perhaps not ever."

"She scoffed, but Rowan didn’t sense half as much skepticism as the last time he’d been boasting to her."

patr "Promises promises. They can be such pointless things, can’t they?"

"Rowan looked back at the mess they’d made once more. There wasn’t much in the way of leftovers now."

ro "I wonder what the servants will think…"

#patricia happy

"She just laughed."

patr "Oh, they’re all my brother’s bannermen. Any noble worth their salt only brings the most discreet of house staff."
patr "Now then. Shall we?"

"With a smile, Rowan locked arms with her. This was still just the beginning."

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return


