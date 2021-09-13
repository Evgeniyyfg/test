init python:
    
    event('draiths_visitor', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), run_count=1, group='alexia_breeding', priority=pr_npc)
    event('drider_exhibitionism', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'", 'NTR == True', "castle.buildings['pit'].driders >= 1"), run_count=1, group='alexia_breeding', priority=pr_npc)
    event('drider_milking', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'", "all_actors['alexia'].corruption > 30",), run_count=1, group='alexia_breeding', priority=pr_npc)
    event('wild_animals_bite_back', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'", 'emissariesPresent == True',), run_count=1, group='alexia_breeding', priority=pr_npc)
    
label draiths_visitor:

scene bg25 with fade

"Working in the breeding pits wasn’t exactly Alexia’s favourite job. The boy, Draith was nice, and she tried her best to be kind to him, for all that he has been subjected to before he arrived at Castle Bloodmeen, but the work was often hard going."
"Cleaning the cages was a long, and arduous task, and the creatures who lived in them were at best not particularly friendly, and at worst downright scary."

if friskyDrider:
    "She had seen what happened when one of the driders got free, and she wasn’t pleased at the prospect of the same thing happen to her."
    
else:
    "If she had met any of the monsters that Draith loved so much out in the world before coming to the castle, she would have run for her life screaming, and now she had to look after them."
    
"Today though, as it had turned out, had been her lucky day. Draith had a number of errands that needed doing around the castle, and had given her the task of doing them instead of her usual chores."
"When she saw the errand list, she understood why; a visit to Cliohna for books needed for research, Cla-Min for supplies, and delivering a report to Jezera. She knew how the young dark elf felt about women, and was no doubt happy for an excuse not to have to see them himself."
"In the end, the tasks had taken her longer than she had expected. The sorceress was busy, and Alexia ended up having to search for the books herself." 
"When she got to the caravan, later than intended, Cla-Min’s supplies were low, which meant waiting for one of her children to return with more stock." 
"Jezera had been the worst though, she had kept her waiting outside her chambers for almost an hour while she amused herself with the help, and when she was finally able to deliver the report, the demoness nonchalantly waved her off, uninterested in Draith’s research."
"By the time Alexia was finally able to head back to the pits, it was well past noon. She contemplated stopping for lunch, but still had the books and supplies, and felt she had best deliver them first, in case the dark elf needed them."
"As she approached, goods in hand, she heard two voices coming from the research area. At first, she could make out neither, but as she got closer, it became clear who were talking." 
"One voice, as she assumed, belonged to Draith. He would be there still working after all. But the other surprised her - it was Andras. Was what he doing down here?"
"She tiptoed closer, wanting to hear what was being said, but without wanting to intrude in case it was inopportune timing. With what she had seen of Andras’ temper, eavesdropping was the more prudent choice." 
"She stopped near the door and placed the items she had been carrying on the floor, carefully. First, the sounds of heavy breathing, and then the demon spoke."

show andras smirk behind bg25
show draith neutral behind bg25

an "You haven’t forgotten your place, have you?"

dra "No master."

"Place? Were they talking about work?"

dra "My place… my place is…"
dra "To do whatever you want me to, whenever you ask me to."
dra "You be… your fuck toy."

"Alexia went bright red as she realized what she had walked in on. She shouldn’t have been surprised really, Draith was so afraid of women it was obvious he’d prefer the company of men, and Andras was practically a walking erection." 
"She should leave now. This was obviously a private moment, and she didn’t really want to risk getting caught peeping, however…"

if all_actors['alexia'].corruption > 50:
    "She felt her loins grow hot at the thought of what was about to happen. The dark elf was a cutie, and the thought of the larger, muscular demon pounding his little butthole made her wet."
    if all_actors['alexia'].flags['andras_influence'] > 5:
        "And as wrong as it was to feel that way, she felt jealous of Draith."
    else:
        pass
else:
    pass
    
menu:
    "Peek.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +3)
        jump andrasDraithBPSex
        
    "Leave":
        $ released_fix_rollback()
        "No, this was a private moment, and she had no idea what would happen if the demon was to spy her watching, or the type of punishment he would inflict." 
        "Bending over, she picked up the books and supplies from where she had left them. She would return after eating to deliver them, when they had, hopefully, finished."
        return

label andrasDraithBPSex:

#CG1
scene cg358 with fade
show andras smirk behind cg358
show draith neutral behind cg358
pause

"While she had been contemplating what to do in the hallway, Andras had wasted no time putting the dark elf to work. When she peeked around the corner, she saw Draith was now on his knees behind the demon."
"She saw his grey-white hands on the demon’s ass, a strange contrast against his red skin. He spread the cheeks, and leaned forward to bury his face in it."

an "Uhhh.. That’s it, lick it slave."

"Alexia watched as the smaller elf began to tongue her captor’s asshole, licking up and down, and round in circles. It was obvious to her he had done this before, and was clearly enjoying himself. Andras didn’t seem to mind it either."

an "You’ve gotten good at this, haven’t you, my little ass slut?"

"At the use of the term, “ass slut”, the dark elf’s face reddened, not with shame, but with pride. He was getting off on the degradation, perhaps the result of the years he had spent as a slave to the females of his species. "

"He took a moment to move his face back, giving him room to respond."

dra "Yes master. I love the taste of your ass master."

"He really did. He went back to licking it as soon as the words left his mouth, the demon smirked."

an "Why don’t you prove it?"

"Draith didn’t need any more encouragement, he buried his tongue into his master’s hole as far  as it would go. Andras let out and groan, followed by a chuckle, as the elf swirled his tongue as best he could. Alexia wondered how he could breathe."
"As his slave jerked his head back and forth, stabbing his tongue into his butthole, Andras reached down and grabbed his engorged cock, moving his hand up and down in lazy strokes."

an "That’s a good start, slut. Now, assume the position."
     
#CG2
scene cg405 with fade
show andras smirk behind cg405
show draith neutral behind cg405
pause 3

"Draith got up from the floor, and walked over to the desk where he did his research. He pulled down his pants, and then leaned over to offer himself to his master. Andras walked up behind him, and placed a large hand on the elf’s posterior."

an "Now, do you think that performance deserves a reward? Hmmm?"
 
dra "No master."

an "No, what does it deserve then?"

dra "I think I…"

an "Yes?"

dra "I deserve to be punished!"

"The demon let out a chuckle."

an "I think so too, three should do it, don’t you think?"

dra "You are too kind, master."

"Andras smirked at his response."

an "You are right, of course, we’ll make it five."

"*THWACK*"

"His large hard came down in a flash, so fast that Alexia barely saw it. The elf let out a squeal as it met flesh, leaving a large red welt in its wake. It looked painful, but it was clear Draith was getting off on it."

an "That’s one."

"*THWACK*"

"Again the hand came down as the demon spanked him, this time leaving a welt on the other cheek this time."

dra "Unnnn……"

an "Two."

"*THWACK*"

"Once more, the hand met flesh with hard contact, making the cheek even redder. The dark elf shuddered and moaned in response."

an "Three."

dra "Please master…"
dra "No more…"

"This must have been part of the act, the woman surmised, he was clearly enjoying being manhandled by Andras."

an "Be quiet you wimp, and take it like a man."

"*THWACK*"

"The fourth spank fell, both cheeks were practically glowing now. Draith had bitten down on his lip to try and stop himself from crying out, but it hadn’t helped. He had a dazed look on his face, and his cock was twitching with arousal."

an "Four. Just one more."

dra "No no no…"

"*THWACK*"

"The final spank was so hard, the sound reverberated around the room. Draith collapsed on the table in extacy."

dra "Fuckfuckfuckfuck…"

"Andras gentled caressed his small ass with his hand. He then ruffled his hair in an uncharacteristic display of gentleness."

an "Good boy."

scene cg256 with fade
show andras smirk behind cg256 
show draith neutral behind cg256 

"Without a word, Andras flipped his smaller partner over so that his back was on the table, and spread his legs apart. The elf didn’t object, but then, even if he wanted to, he was hardly in a state to do so."
"Andras spit on his hand, and applied a copious amount of it to his dick, before fingering Draith’s asshole to lube it up for good measure. Reaching down he grabbed his cock, and pressed it against his slave’s ass, forcing it inside."

dra "Unnnf!"

"Without waiting on ceremony, the demon began to move his hips back and forth, deep fucking the elf. All the foreplay must have gotten him hot, and he was in no mood to play around any further."
"By this point, Draith was reduced  to a moaning mess. To add to it, Andras reached down and grabbed his cock, and stroked it with the same rhythm as the movement of his hips."
"The sound of thwack thwack thwack filled the room as flesh met flesh, each time the demon bottomed out, again and again. It was joined by the cries of the young elf, which grew louder and louder."

if all_actors['alexia'].corruption > 50 and NTR == True:
    "As if almost by instinct, Alexia slid a hand down into her panties, and began to massage her clit. As she watched the two handsome creatures before her, fucking like animals, she wished one of them was inside her too."
    if all_actors['alexia'].corruption > 75 and NTR == True:
        "Or both of them, she had more than one hole after all, and she knew she would feel so full..."
    else:
        pass
    if all_actors['alexia'].flags['andras_influence'] > 5:
        "She couldn’t stop herself from staring at the demon, so strong and so powerful. She knew it was wrong, and she tried to push the thought away, but all she could imagine was him holding her down, and having his way with her. A wave of orgasmic pleasure shot through her body."
    else:
        pass
else:
    pass

"It didn’t take long before they were both approaching climax. Draith came first, as Andras jerked him hard and fast, spraying cum into the air like a fountain." 

show cg256 with sshake
show cg256 with sshake
show cg257 with flash
pause 3

"With a smirk, the demon forced his cock into the dark elf’s asshole until he was balls deep, and then let out a satisfied grunt as he spunked inside him. Draith smiled as he felt his insides grow warm from his master’s creamy load."

show cg257 with sshake
show cg257 with sshake
show cg258 with flash
pause 3

if all_actors['alexia'].corruption > 50:
    "Alexia came last, greedily fingering her hole as she watched the two males cum. As she climaxed, she had to cover her mouth to avoid being discovered, before sliding to the floor in post orgasmic bliss."
else:
    pass
    
"With the show over, and both of them currently distracted, Alexia saw this as her best chance to slip away. She picked the goods, and the books, up from the floor, and carefully tiptoed away down the hall."
"She would return later to deliver them to the dark elf, and never mentioned what she had seen to anybody."

return

#############################################################################################################################################    
    
label drider_exhibitionism:

scene bg25 with fade

if castle.researches['monster_taming'].completed:
    show alexia breeding happy at midleft with dissolve
    show draith happy at midright with dissolve
    dra "Isn’t he simply adorable?"
    al "Not exactly the word I’d use."
    show draith neutral at midright with dissolve
    dra "Hmm… I guess that much is true."
    show draith happy at midright with dissolve
    dra "“Magnificent” is much more fitting!"
    "Alexia smiled to herself. Draith’s enthusiasm was infectious, even though the object of his adoration was slightly unorthodox."
    "Said object – a large drider they recently finished training – continued to pace restlessly in his cell. They’ve been doing great progress on them, and it was surprising to see these wild beasts act so… Servile."
    
else:
    show alexia breeding concerned at midleft with dissolve
    show draith happy at midright with dissolve
    dra "Isn’t he simply adorable?"
    al "Not exactly the word I’d use."
    show draith neutral at midright with dissolve
    dra "Hmm… I guess that much is true."
    show draith happy at midright with dissolve
    dra "“Magnificent” is much more fitting!"
    "With some concern, Alexia eyed Draith’s object of adoration – a large drider they recently finished training. The beast paced the cell restlessly, and Alexia suspected it wasn’t striking against the bars only because his master was here."
    "They had been making great progress with them, and Alexia had to admire Draith’s skill, but she just couldn’t share his enthusiasm. She couldn’t help but think they’ve been playing with fire here."

show alexia breeding neutral at midleft with dissolve

al "Do you think he’s fit for battle?"

show andras displeased behind bg25

an "He better be."

hide andras
show andras displeased at edgeright with moveinright
show draith neutral at edgeleft with moveoutleft
show alexia breeding shocked at midleft with dissolve

dra "M-Master?"

show alexia breeding concerned at midleft with dissolve
show draith happy at edgeleft with dissolve

dra "What a pleasant surprise! Have you come to inspect the pens?"

an "Yes. I was hoping to make use of our driders next month."

show andras displeased at midright with moveinright

an "So I believe you can imagine my disappointment when I saw the result of your “hard work”."

if castle.buildings['pit'].driders == 1:
    an "I was promised an army of driders, Draith! Is this one, measly bug all you have to show to me?!"
    
elif castle.buildings['pit'].driders == 2 or castle.buildings['pit'].driders == 3:
    an "I was promised an army of driders, Drath! Is a handful of bugs all you can show me?! What am I supposed to conquer with them, a cabbage farm?!"
    
else:
    an "I was promised an army of driders! And all you have here is a mob of half-feral bugs!"
    
dra "Technically they’re arach- gack!"

#draith terrified
show draith neutral at center with moveinleft
show alexia breeding shocked at edgeleft with moveoutleft

"Andras seized the elf by the throat, picking hip with ease, and he weighed nothing to him. And mattered nothing to him."

an "I found you wandering the tunnels like a lost dog, AND THIS IS HOW YOU REPAY ME?!"

show alexia breeding concerned at edgeleft with dissolve

al "Andras, please-"

show andras displeased at midleft with moveoutleft

an "Do not interrupt me woman."

"His low growl was enough to make her shut up, and she shriveled under his fury. His lone arm still choked the elf – Draith put his own hands on it, but made no attempts to break his hold."
"If there was anything both of them had learned already, it was that resisting Andras usually only made the situation worse."
"Even if his initial intent was to kill you."

an "Pathetic."

hide draith with dissolve

"He threw the pen master to the ground – violently. Alexia winced as she heard something crack and prayed it wasn’t anything important."

show draith neutral behind bg25

dra "*cough* M-mas…"

"Draith tried to apologize, but Andras paid no attention to him. He turned to Alexia and the housewife backed away immediately, instinctively. He wouldn’t hurt her, right?"

if alexiaAndrasSex > 2:
    "She’s been obedient, spreading her legs whenever he asked her to. He wouldn’t hurt her for a silly little thing like this, right?"
    "Right?"

else:
    "… Right?"
    
an "This is unacceptable. What are you two even doing here all week? Is this whole project just a massive money sink?"

dra "M-"

an "Shut up."

"Draith whimpered, and did just that."

"The demon turned away from both of them, and peered into the cell. The drider watched the situation unfold in silence, having retreated deep into the corner of his room."
"The beast recognized the presence of an apex predator, but with escape impossible, it could only try to put some distance between himself and red demon." 

an "…But I guess I can’t really blame you."

if castle.buildings['pit'].driders < 4:
    an "It’s not your fault you have no eggs to work with."
    
else:
    an "It’s not your fault you receive sup par eggs or that you don’t have enough staff to train everyone.    "

an "Rowan was supposed to handle this, but I guess I expected too much of him."

if all_actors['andras'].favors > 2:
    an "And to think he was starting to show promise…"
    an "..."

else:
    pass
    
an "Guess I’ll have to discipline him."

show andras displeased at edgeright with moveoutright

"Without another word, he headed for the exit. Alexia felt her heart sink. The threat hanged in the air, spoken so casually, yet carrying terrifying undertones."
"Rowan was not in the castle, but Andras was not one to calm down with time. His fury would only grow, and her husband would meet it head on the moment he steps from the portal."

show andras happy at edgeright with dissolve

al "Wait!"

show andras displeased at edgeright with dissolve

"Miraculously, the demon did just that. He turned his head around, eyes narrowed on her."

show alexia breeding neutral at edgeleft with dissolve

if all_actors['alexia'].relation > 30:
    "Even if things weren’t going so well between her and Rowan, she couldn’t just let Andras hurt him for no reason."
    "Despite everything, a part of her still loved him. She was still his wife – she had to find a way to protect him."

else:
    "She couldn’t just let Andras hurt her husband for no reasons. She was his wife – she had to find a way to protect him."

al "We might not have the army you wanted, but-"

show alexia breeding happy at edgeleft with dissolve

if castle.buildings['pit'].driders == 1:
    al "But we’ve been making great progress training them!"
    
else:
    al "But the ones we have are all well trained!"
    
al "Just look at this one!"

show andras displeased at center with moveinright

"She pointed to the cell. The drider still observed them all without as much as a peep, silent and alert."

if all_actors['alexia'].corruption < 30:
    hide andras with dissolve
    show alexia breeding concerned at edgeleft with dissolve
    "As Andras approached the cell, Alexia took a quick glance to where the demon dropped the pens master."
    hide draith
    show draith neutral at midright with dissolve
    "Draith didn’t look seriously injured, but did not dare to raise up. Alexia offered him a reassuring smile, mouthing “I’ll take care of it”. She then turned back to Andras before the demon noticed she was looking away."
    hide draith with dissolve
    show andras displeased at center with dissolve
    show alexia breeding happy at edgeleft with dissolve
    
else:
    pass
    
al "Strong and vicious in battle, but tame and obedient in the presence of his trainers!"

if castle.buildings['pit'].driders < 4:
    al "Rowan has been delivering some high-quality eggs, so the driders we have all show great potential!"
    
else:
    al "We might be a little bit understaffed, but the people Rowan assigned to us all are excellent trainers!  These driders will surely perform in battle, Master Andras!"
    
"It was straight up lies, but she had to say something. Her mouth was simply running faster than her mind could keep up. She only hoped Andras would buy it."

if castle.buildings['pit'].driders == 1:
    al "We just need some time to breed this one, and-"
    
else:
    al "We just need some time to breed the more promising ones, and-"

show alexia breeding shocked at edgeleft with dissolve

an "Hrm. Breed, you say?"

"She froze. This did not bode well."

show alexia breeding happy at edgeleft with dissolve

al "… Yes?"

show andras happy at midleft with moveoutleft

an "You had plenty of time to breed them before, didn’t you?"

"He placed his arm on her shoulder. She did her best not to shiver, and failed miserably."

an "I’d like to see some proof of your claims."
an "Strip."

show alexia breeding shocked at edgeleft with dissolve

al "What?"

show andras displeased at midleft with dissolve

an "I said strip."
an "You’re going to prove to me how well trained he is."

show andras smirk at midleft with dissolve

an "So, you’re going to strip. Then you’ll walk in there. Slowly."
an "You’re going to tell the drider to stay put."
an "Then, you’re going to spread your legs, and start playing with your pussy."
an "If, by the time you come, the drider does not jump you, then I’ll concede that maybe, just maybe, Rowan and Draith know what the fuck they’re doing here.  "

al "… You can’t be serious."

show andras displeased at midleft with dissolve

"He glared at her, and she stowed further complains. He was very much serious."

show alexia breeding neutral at edgeleft with dissolve

"Her eyes ventured to the drider. In the heat of the moment, she made some very bold statements, on some very shaky grounds. She couldn’t back down from them now, and she couldn’t expect the semi-sentient beast to play ball with her. "
"The drider still kept his distance, but even in the half dark of his cell, she could still see his large body looming menacingly behind the cell bars."

if alexia_ice_shard == True:
    "Was she really going to expose herself to this beast? With nothing to defend herself, except for a low-level magic bolt and faith in Draith’s unfinished training?"
    
else:
    "Was she really going to expose herself to this beast? With nothing to defend her, expect for Draith’s unfinished training?"
    
if all_actors['alexia'].corruption > 30:
    "It was reckless. It was foolish. It was downright insane."
    show alexia breeding aroused at edgeleft with dissolve
    "But Solansia save her, as much as she wanted to deny it, something deep inside of her was thrilled at the perspective of following through with this, thrilled at the prospect of exposing herself like that." 
    "It was wrong. But as much as she tried to suppress her feeling, they refused to leave her."
    
else:
    show alexia breeding concerned at edgeleft with dissolve
    "It was reckless, it was idiotic, and she shivered in fear at the thought of doing so."
    
show alexia breeding neutral at edgeleft with dissolve

"Besides her, Andras was waiting for her decision. He didn’t urge her on, but his mere presence was enough to make her sweat."

$ driderProtectAsk = False

label driderMenu:

menu:
    "Agree to his demands.":
        $ released_fix_rollback()
        "There was no use resisting. She’ll just make the situation worse if she tries to. It was best to just go along with his demands before he adds something even more unreasonable to them."
        if all_actors['alexia'].corruption > 30:
            show alexia breeding aroused at edgeleft with dissolve
        else:
            show alexia breeding concerned at edgeleft with dissolve
        jump driderHarrassSex
        
    "Ask Andras if he’ll protect her if something goes wrong." if driderProtectAsk == False:
        $ released_fix_rollback()
        show alexia breeding concerned at edgeleft with dissolve
        al "Um… Theoretically asking…"
        al "If the drider proves to be more rebellious than we previously anticipated… Will you make sure he doesn’t hurt me?"
        "Andras gave her a hard look, then burst into a loud, mocking laugh."
        show andras happy at midleft with dissolve
        an "Ahahaha, not so confident in your husband’s choices after all, are you?!"
        "He put his arm around her, and hugged her close to his chest. She blushed, feeling his rock hard muscles and heavy musk of his sweat, so characteristic to the demon."
        an "Very well. No harm will come to you. I am not like Rowan. I’d never allow anyone to touch you without my permission."        
        $ driderProtectAsk = True
        $ change_actor_num_flag('alexia', 'andras_influence', 1)
        jump driderMenu
        
        
    "Try to weasel yourself out of this.":
        $ released_fix_rollback()
        if driderProtectAsk == True:
            "Hearing her husband’s name, she felt a surge of guilt overtake her. She pushed herself away from the demon, and stammering, tried to think of an excuse to cut things short before they spiral out of control."
        else:
            pass
        show alexia breeding shocked at edgeleft with dissolve
        show andras displeased at midleft with dissolve
        al "This a little sudden don’t you think?"
        al "The drider is trained, but we haven’t fed him today, and that might make him a bit uppity-"
        an "Alexia."
        an "As much as it amuses me seeing you backtrack from your attempt of covering for Rowan’s mistakes, I am less pleased by the fact you think you can play me and get away with it."
        an "Need I remind you of your place here? Then allow me to rephrase my earlier demand."
        an "You will strip."
        an "You will walk into the cell."
        an "And you will fuck your slut pussy until you cum."
        an "This is an order."
        show alexia breeding neutral at edgeleft with dissolve
        al "…"
        if alexiaWulump == True:
            "Andras already proved he wouldn’t shy away from anything when Alexia got out of the line. And while refusing him here likely wouldn’t be enough to toss her into the dungeons again, she knew she couldn’t keep doing so."
        else:
            "She didn’t think he’d do anything to her from denying him here, but… He wouldn’t tolerate constant disobedience either."
        "Sooner or later, she will suffer the consequences from her continuous resistance."
        
        menu:
            "Submit to his will.":
                $ released_fix_rollback()            
                "Slanting her shoulders, she resigned herself to her fate. What else could she do? He was the Lord of the castle, while she was his prisoner."
                if all_actors['alexia'].corruption > 30:
                    show alexia breeding aroused at midleft with dissolve
                    "Besides… It’s not like she was wholly opposed to the idea…"
                else:
                    pass
                jump driderHarrassSex
                
            "Deny his request.":
                al "Andras, I-"
                show alexia breeding concerned at edgeleft with dissolve
                al "I’m sorry, I shouldn’t have made all these claims about the driders."
                if all_actors['alexia'].relation > 30:
                    al "Please have mercy on my husband-"
                else:
                    al "Please have mercy on me-"
                an "Enough. This is pathetic. I don’t have time for this."
                show andras displeased at edgeright with moveoutright
                an "I don’t have time for this."
                "Andras snapped angrily, stopping her midway, no longer paying attention to her excuses. He walked over to Draith, and Alexia fully expected him to kick the dark elf or punch him or something equally violent."
                an "Draith."
                "Instead, he knelt beside him and grabbed him by the chin, forcing him to look him in the eyes."
                show alexia breeding shocked at edgeleft with dissolve
                an "Do not make me hurt you again."
                an "Have I made myself clear?"
                show draith neutral behind bg25
                dra "Y-yes Master…"
                show alexia breeding neutral at edgeleft with dissolve
                an "Good."
                hide andras with moveoutright
                "He left the room as suddenly as he arrived, leaving behind an oppressive atmosphere."
                hide draith
                show draith neutral at midright with dissolve
                show alexia breeding concerned at edgeleft with dissolve
                al "Draith… "
                dra "… Let’s get back to work."
                al "Right."
                scene black with fade
                "Neither of them wanted to talk about what transpired. They returned to their duties, doing their best to avoid one another for the remainder of the week."
                $ andrasPunishmentCounter += 1
                return


label driderHarrassSex:

al "Alright… I’ll do it."

show andras smirk at midleft with dissolve

an "Good… Good."

show andras displeased at midleft with dissolve

an "Get on with it then, I don’t have all day."

hide draith
show draith neutral at edgeright with dissolve

"With trembling hands, she started to take off the heavy tunic she wore in the pens, and quickly moved on to everything else."

show alexia necklace naked concerned at edgeleft with dissolve

if all_actors['alexia'].corruption < 30:
    al "(Let’s just be done with this…)"
else:
    pass
    
show alexia necklace naked concerned at center with moveinleft
show andras displeased at edgeleft with moveoutleft
show draith neutral at midright with moveinright

"A moment later, she stood naked in front of the cell, Draith by her side with the keys in his hand. He kept rubbing his throat, the red imprinting of Andras hand clearly visible on his dark skin."

if all_actors['alexia'].corruption < 30:
    al "Are you okay Draith?"
    "He nodded solemnly, but didn’t speak up. She could only imagine how much it hurt."
else:
    "She couldn’t help but notice there was a soft blush to his cheeks. Did he like it when Andras treated him roughly?" 
    "Part of her wanted to feel his pants to check it, but this was not the right time."

"He opened the door for her. She took a deep breath, stepped inside."

#cg 1
scene cg263 with fade
show alexia necklace naked concerned behind cg263 
show andras smirk behind cg263 
pause 3

"She never was much of a fighter, but now, she felt more vulnerable than ever. The stone beneath her feet was hard and cold, and the cell had an unpleasant smell to it Alexia tried very hard not to think about."
"And in front of her, the drider watched her approach, slowly raising up to meet his prey."
"Protected by the orcs and separated by metal bars, Alexia sometimes forgot what a dangerous foe they were playing with here. The Drider towered over her easily, his eight black legs supporting a large body that could crush her with ease."
"Four pairs of eyes hid intelligence that rivaled human, while the chitin armor on his lower torso covered something that often surpassed its human equivalent."
"Alexia saw it break many slaves. And if their training was insufficient, she was next on that list."

if all_actors['alexia'].corruption > 30:
    "He would plunge his massive cock into her, ravishing her with abandon. She would scream, she would shout, but would Andras and Draith react? Would they save her, or would they let her be ravished in front of their eyes?"
    "… She only just entered the cell, and already she felt her pussy flare up."
    
else:
    pass
    
"The drider waited, uncertain of the situation. He glanced towards his dark elf master, expecting to see him follow Alexia into the cell, whip in hand."
"But Draith only watched the situation unfold, with a pained expression on his face. He would not intervene, that much was clear to the beast. And this only meant one thing to the drider."
"He smiled hungrily, and took a step forward." 

al "Stay!"

"The drider almost recoiled from the command. He was trained to obey the staff, no matter the circumstances. Draith made sure of it."

if all_actors['alexia'].corruption > 30:
    "And a small, twisted part of Alexia almost resented him for it. Such a glorious beast… Shackled and broken."
    "What a shame it was!"

else:
    "And again, Alexia prayed the training stuck. Overwhelmed with fear, she barely got the command out in time."
    
"She could almost see the invisible tethers of Draith's conditioning bind the drider, hold him in his place. How durable were they?"
"She was about to put them to the test."
    
if all_actors['alexia'].corruption > 30:
    "Giggly with anticipation, she spread her legs slightly. She watched the beast, as her hand slowly slid downwards."
    al "A-ah!"
    "She could not contain her voice. It was twisted, she knew that."
    "But with every passing moment, she cared less for it."

else:
    "Shivering in fear, she spread her legs slightly. She watched the beast while her hand ventured south, fully expecting the drider to pounce at her at any moment."
    
al "Stay."

if all_actors['alexia'].corruption > 30:
    scene cg264 with fade
    show alexia necklace naked aroused behind cg264
    show andras smirk behind cg264
    pause 3
    "It was amazing, watching this massive beast just… Stare, as she spread her pussy lips right in front of him. He could watch, but he could not touch. They lived to breed, and this wonderful soaking pussy was being denied to him."
    al "Stay and watch."
    al "..."
    al "Watch me fuck myself with my fingers."
    "She couldn’t contain her voice, the rush from taunting the drider banishing all reason."
    al "You can watch me, but you can’t fuck me."
    al "Watch my – Mmmh!- fingers!"
    al "Watch me put them inside of me!"
    "She felt a jolt of pleasure shoot up her spine, as she easily thrusted her hand inside of her. The drider’s erect cock swayed in front of her eyes, the sight of it tearing her apart-"
    "What was better? Taunting him, or laying on her back and letting him fuck her?"
    al "Ha… ha-ha!"
    "She had- she had to masturbate, but the more she did, the more remorse she felt Andras didn’t order her to just go and fuck the beast. She wanted- she wanted something bigger than this! Something bigger than her fingers!"
    an "Ahahahaha, panting like a slut already? You really are shameless!"
    "She heard Andras jeer, and could not find it in herself to refute his words. Here she was, naked, fucking herself with her hand in front of a massive drider dick, and all she could think about was how it was not enough for her."
    an "Tell him to watch you! Tell him to stare at your cunt!"
    al "W-watch meeeee fuck my cunt!"
    an "Tell him to stroke himself!"
    al "U-use your hand while yo-u watch!"
    an "Tell him he’s not worthy of breeding with you."
    al "You c-can’t fuu-uck me!"
    al "You caaa-n’t spray your cum inside of m-me!"
    an "Tell him your pussy is for me only."
    
    menu:
        "Obey.":
            $ released_fix_rollback()  
            $ change_actor_num_flag('alexia', 'andras_influence', 3)
            al "My pussy is for M-master Andras aloooone-!"
            
        "Don’t.":
            $ released_fix_rollback()
            "Despite the overwhelming lust, the words froze in her mouth, as the image of her husband flashed before her eyes."
            "She couldn’t do it. She couldn’t betray him like that."
            al "Ah-ah, ah!"
            "Instead, she redoubled her efforts. She had to cum."
            "She had to cum before Andras makes her say something she didn’t want to."
            
    
    if castle.researches['monster_taming'].completed:
        jump alexiaDriderCum
        
    else:
        jump andrasDriderIntervention
            
else:
    scene cg264 with fade
    show alexia necklace naked aroused behind cg264
    show andras smirk behind cg264
    show rowan necklace happy behind cg264
    pause 3
    "She slowly traced her fingers across her slit, but felt no arousal from doing so. What madwoman would? With a half-feral beast waiting to rape her, and with her captor watching her every move?"
    "But Andras wouldn’t let her go unless she orgasmed. Bastard…"
    "Too afraid to take her eyes off the drider, she imagined her husband behind her, and herself leaning her back against his muscular chest."
    "She imagined his arms embrace her, as he leaned in to whisper reassuringly in her ear:"
    ro "Everything will be fine. Just think about me."
    "And she did. Ignoring the drider in front of her, and the demon behind her, and the cold stone beneath her, and the horrid odor around her, she thought of her husband."
    "She thought of his kind smile, of his tender touch. She thought of the warmth of his body, and his gentle voice, firming guiding her movements."
    ro "Everything will be fine. Put your hand between your legs, and think about me."
    al "A-ah…"
    "She slid the first finger in, her eyes never leaving the drider."
    al "Ah-ah!"
    "She thought of the summer festival, three years into their marriage. She promised the Cavins she would help with the pies. Rowan pretended to go patrol around the village, only to sneak in into the bakery when no one was looking."
    "She recalled how he grabbed her from behind, shushing her. She tried to protest quietly, telling him it wasn’t proper, but he paid her no heed."
    "He reached under her skirt, and thrust his finger into her pussy, just as she did now."
    al "Aah! Mm-ah! S-stay!"
    "She saw the drider tense, and again she ordered him to stay. His erect tool swayed in front of her eyes, ready to plunge into her hole."
    "Insane. This was all insane. But she had to keep going."
    "She kept thrusting, with every moment with greater urgency. She tried to think of Rowan, but it was difficult to recall the fantasy again, with the cock reminding her of the danger she was in."
    al "(Why do I have to suffer through this…)"
    "She tried to think what Rowan would say, what comforting words he would offer-"
    an "Looking real nice, slut!"
    al "Nngh?!"
    an "Look how hard you got his dick! He looks like he’ll pounce you at any second!"
    al "S-stop it Andras!"
    "He laughed in response, as always not caring in the slightest for her concerns. No matter. She was getting close. She just had to ignore everyone and think about her-"
    an "It’s actually dripping with pre-cum! Driders must really love you Alexia!"
    al "(Ignore him, don’t-)"
    an "Spread your legs! Keep fucking your pussy!"
    al "Sto-o-op!"
    an "Keep fucking it!"
    al "D-damn it Aaa-Andras!"
    al "(Shut up, shut up, shut up!)"
    an "Keep fucking it right in front of his eyes until you cum, you slut!"
    al "I’m n-nngh-!"
    an "I said cum!"
    if castle.researches['monster_taming'].completed:
        jump alexiaDriderCum
        
    else:
        jump andrasDriderIntervention


label alexiaDriderCum:

al "A-ah, aaah, AAAH!"

"She closed her eyes, threw her head back, and allowed pleasure to overtake her."

scene black with fade

"..."

show alexia necklace naked aroused behind black

al "Nn… Uh?"

scene bg25 with fade
show alexia necklace naked concerned at center with dissolve

"With some fear, she opened her eyes, and looked up at the drider. He still glared at her furiously, cock painfully erect, but he dared not to step forward."
"She heard a slow clap from behind, and saw Andras enter the cell."

show andras smirk at midleft with moveinleft

an "Well done, well done."

"His gaze traveled across her body, but she was too tired to cover herself."

an "They really are well trained."
an "I’ll give you and Rowan a pass this time. Keep up the good work."

al "… Yes, Master Andras."

"She did it. She managed to protect her husband."
"But as she stood there, Andras eyeing her naked body with lust in his eyes, somehow, it did not feel like victory..."

$ change_actor_num_flag('alexia', 'andras_influence', 3)
$ change_corruption_actor('alexia', +3)
return

label andrasDriderIntervention:

scene black with fade

"Suddenly, all hell broke loose."

show black with sshake

"So engrossed she was in the situation, she didn’t notice the drider leap forward, screeching in frustration. She fell back, shouting-"

show black with redflash

"She felt a large arm embrace her, and a crimson energy flooded the cell. "

show black with sshake
show black with redflash

"She watched, as a large, red pentagram fell on the drider, crushing it into the ground, turning him into a red pulp right in front of her eyes. He kept screeching, until his head literally exploded from the pressure, spraying the cell red."

show andras displeased behind black

an "Nobody fucks Alexia without my permission."

scene bg25 with fade
show andras displeased at midleft with dissolve
show alexia necklace naked concerned at center with dissolve


"She looked up, eyes blurry, and saw it was Andras embracing her from behind. His left arm was raised up, glowing menacingly with terrifying power."

if alexia_ice_shard == True:
    "He was younger than her, and she almost never saw him train the library… Just how much innate power did he have at his disposal?"
else:
    pass
    
an "So much for it being well trained."

al "..."

"She couldn’t say anything. She just stayed in his arms, trying to stop her heart from jumping out of her chest."

an "But I guess I’ll let it pass. This one time."

"He broke the spell, and gently ran his fingers over her hair. Alexia did her best to ignore the stench of blood that now filled the room."

an "You did well Alexia. Take the rest of the week off."

"She nodded solemnly. She did it. She protected her husband."

scene black with fade

"Then why was she hugging another man?"

#lose 1 drider
$ change_actor_num_flag('alexia', 'andras_influence', 3)
$ change_corruption_actor('alexia', +3)
return

##########################################################################
##########################################################################
##########################################################################

label drider_milking:

scene alexia_pits_1 with fade

"Alexia often dreaded the prospect of descending into the depths of Bloodmeen Castle to work once in the breeding pits."
"It was dark, dank, engulfed in the collected heat and stench of creatures enslaved to the will of the Twins. The walls were wet, covered in scratch marks and glistening in the dim torchlight like some mouldering vision of eternal imprisonment."
"Alexia would almost pity them… were the monsters themselves not so despicably abhorrent."

scene bg25 with fade
show alexia breeding neutral at midleft with dissolve
show draith happy at midright with dissolve

dra "Good {i}morning{/i}, Alexia!"

show alexia breeding concerned at midleft with dissolve

"...Which made Draith’s eternal, cheery nature all the more jarring."

al "Uh… good morning, Draith?"
al "What are you doing carrying around those buckets?"

"Draith glanced down at the two hefty buckets clenched in each hand at his side. A gleam of mischief entered his eyes."

dra "Oh! I… forgot I had these."

"Draith’s lie was unconvincing, his false smile doubly concerning. Despite their numerous positive interactions since she’d started working with him, the Dark Elf was still somewhat intimidated by Alexia."

dra "It’s a bit complicated."

show alexia breeding shocked at midleft with dissolve

al "Buckets are complicated?"

dra "Uh, no... but the reason why I have them is."

"The Elf gestured with his head in the direction of the occupied breeding pits."

dra "Do you mind tagging along? We’re just about to get started."

show alexia breeding concerned at midleft with dissolve

"Alexia felt her hackles rise as she joined Draith down the long walk towards the Drider cages. Their footsteps echoed in the humid air as they moved through the darkened corridors."

dra "You know how I mentioned in the past about having troubles with maintaining permanent staff down here?"

al "I… can't imagine why."

"Draith laughed, seeming to take her frank comment as a joke."

dra "I know, I know. Taming beasts is not an easy job, it’s even harder when you’re trying to teach a bunch of uncoordinated Orcs to do it."
dra "{i}One{/i} bad mauling in the cage, and suddenly they all turn to puddles on the floor. They wouldn’t have lasted a day in a Dark Elf Menagerie."


#draith annoyed
show draith neutral at midright with dissolve
show alexia breeding shocked at midleft with dissolve

dra "Do you realize how many times I was bitten working in my Mistress’ pits, before I finally figured out how to wrangle a Chalcedon Cobra? I practically developed an immunity to their venom by the end of it!"
dra "Well… almost. It’s actually impossible to develop an immunity, as their venom is magical in nature."

#show alexia breeding angry at midleft with dissolve
show alexia breeding neutral at midleft with dissolve
show draith happy at midright with dissolve

al "Draith, what are we doing? What’s with the buckets?"

"Draith - to his credit - managed to stop himself from rambling more about the intricacies of herpetology. He shot her a sheepish grin, unable to meet Alexia’s eyes as they came to a stop near one of the training pits."

dra "Remember how I said that the Orcs are unreliable? "
dra "Well… one of my normal handlers is no longer available for work, and I was hoping you could help."

show alexia breeding shocked at midleft with dissolve

dra "You see, her unexpected ‘leave of absence’ has gotten me to thinking: I really don’t have a reliable worker down here in the pits… other than you."

"He extended the bucket towards Alexia. The bottom dropped out of her stomach as she realized what he was asking her to do."

#show alexia breeding angry at midleft with dissolve
show alexia breeding neutral at midleft with dissolve

al "N-no way!"

#draith sad
show draith neutral at midright with dissolve

dra "Please, Alexia? I’ve got a training session set up for one of the new Driders. It’s just some simple exercises, and uh… ‘rewarding’ them for their good behavior."
dra "I promise: you won’t be in any danger. I’ll be right there with you, and there’ll be handlers in the cage with us at all times."

al "If you’ve already got handlers, then why not make {i}them{/i} do it?!"

#draith annoyed

dra "Haven’t you been listening? I can’t rely on them! The Orcs are clumsy, boorish, and violent. A deadly combination when dealing with a temperamental Drider."
dra "Besides, have you ever felt an Orc’s grip? No tenderness or subtlety at all. We’ll be lucky if the Drider doesn’t kill them, much less allow one of them to get him off."

if AlexiaOrcSex == True:
    show alexia breeding concerned at midleft with dissolve
    "She had felt an Orc’s grip before, in a much more personal manner than she cared to admit. It was hard to deny that their touch could be… rough."
    #show alexia breeding angry at midleft with dissolve
    show alexia breeding neutral at midleft with dissolve

dra "I’ve seen how you handle these beautiful creatures. You know when to be kind, and when to be firm. They respect you, more than I think you realize."

"Alexia thought back to all the times she’d passed by a Drider’s cage, only for the thing to hiss and grab at her from the other side of the bars. "

al "They have a funny way of showing it!"

dra "{i}Please{/i}, Alexia? You’re the only worker I trust enough to teach how to do this. Between the two of us, we can make a lot of progress in the breeding pits."

"Alexia frowned. Draith was asking her to do something particularly odious: seeing to the ‘needs’ of half human monsters who would sooner fuck her into submission than obey her command."
"She cast a worried glance in the direction of the cage they were standing next to. Deep inside the training pit, the Drider was curled up in a defensive crouch, lurking in the darkest spot it could find. There were so many ways that this could go wrong."
"...Then again, Draith was one of the kinder members of the Twins’ staff, and he had gone out of his way to ask for her help."

if all_actors["alexia"].corruption > 60:
    show alexia breeding aroused at midleft with dissolve
    "..And, after all, wasn’t this an opportunity for a new experience?"

menu:
    "Beg off the request.":
        $ released_fix_rollback()
        show alexia breeding neutral at midleft with dissolve
        al "...No. I’m sorry Draith, but this is just too much."
        #draith sad
        "The Dark Elf deflated, letting out a heavy sigh. She’d increased his workload considerably, and both of them knew it."
        dra "I… I understand. Drider wrangling isn’t for everyone."
        al "It’d be one thing if it was just ‘wrangling’ Draith, but…"
        show draith happy at midright with dissolve
        dra "Say no more, Alexia. I’ll take care of it. I’ll just have to hope the next batch of recruits Andras sends me are more capable."
        dra "In the meantime, you can help the cleaning crew scrub out the empty cages instead!"
        show alexia breeding shocked at midleft with dissolve
        "Alexia stopped dead, her mind alight with the disgusting state of Drider cages after several weeks of occupation."
        al "Oh…"
        show alexia breeding concerned at midleft with dissolve
        al "Wonderful."
        return
        
    "Agree to train and drain the Driders.":
        $ released_fix_rollback()
        #show alexia breeding angry at midleft with dissolve
        show alexia breeding neutral at midleft with dissolve
        al "...Okay, fine. Let’s just get this over with."
        "Alexia accepted the empty bucket from Draith, casting a worried glance in the direction of the training pit."
        "The next hour or so was a slow process of wrangling the unruly beast. Alexia stood by as Draith put the beast through his paces, letting the handlers angle the Drider to his proper positioning while Draith gave him basic commands."
        show alexia breeding neutral at midleft with dissolve
        "The Drider was not happy with the situation, but Draith was a natural, moving with smooth grace across the soft, sandy floor. He moved in tune to the creature’s body language, making sure to always remain within easy vision of the beast’s numerous eyes."
        "Every time the Drider would get distracted, or hiss at one of Draith’s handlers, Draith would raise the whip and snap it backwards. He would then assert a strong stance, holding the whip in an active position as if to menace the Drider with a direct hit against the carapace."
        "Despite his ruthless nature in training the Drider, Alexia was astounded by Draith’s restraint. He only used the whip when he had to, and even then only as a tool of chastisement."
        "She had grown up hearing tall tales of the infamous sadism of the Dark Elves, so it was surprising the tenderness with which he handled the beasts in his care."
        #show draith neutral at midright with dissolve
        dra "Stop!"
        "The beast came to a halt, straightening his humanoid spine and casting a long look at the Dark Elf he dwarfed with his bulk."
        show draith happy at midright with dissolve
        dra "All right, I think he’s ready."
        dra "Alexia? Step forward next to me in the pit. Don’t make eye contact with the Drider, just look at me."
        "Alexia took in a deep breath, then did as she was bid, striding forward with slow purpose next to Draith. He smiled and handed her the whip."
        "The Drider, spotting the bucket in Alexia’s other hand, began to get antsy, letting out a low growl and stepping back and forth as he wiggled his abdomen."
        dra "Okay, when I tell you do, look directly into his eyes. You’re going to give him three commands: walk, turn, and stop."
        "Alexia frowned, nervously fingering the whip in her hand as she raised it up to shoulder height the way Draith had showed her. The Drider stopped dead, freezing in place like a bug on a wall. His stillness was almost disturbing in its totality."
        show alexia breeding concerned at midleft with dissolve
        al "Walk!"
        "The Drider began to move, its skittering feet reaching out as if searching for leverage as it moved about the training pit. Alexia sidestepped like Draith had shown her, keeping herself in front of the Drider at all times."
        "Its multiple eyes were watching her, always watching her. There was a terrifying intelligence in his expression. She suppressed a frightened shudder and raised her hand in the air."
        #show alexia breeding angry at midleft with dissolve
        show alexia breeding neutral at midleft with dissolve
        al "Turn!"
        "The creature turned, its heavy body shifting in place as it adjusted to the slowing momentum. He was beautiful - in a strange, bestial way. The bristles on his spider abdomen swayed gently, keyed to the slightest change in air pressure."
        "Alexia sidestepped again, moving once more to the front of the Drider’s form. She led him in a slow circle around the pit, with Draith and the handlers moving out of the way to allow the Drider free access."
        show alexia breeding concerned at midleft with dissolve
        al "{i}Stop!{/i}"
        "The Drider stopped. It let out a low hiss, its humanoid upper body shuddering in place as the wind worked its way up from his gullet in a loud pronouncement of sound. He stretched, putting his muscles on display as he regarded her with a cool, deferential look."
        show alexia breeding happy at midleft with dissolve
        al "Good boy!"
        "Alexia blurted out the words without intending to, feeling an embarrassed blush rise to her face as she did so. She glanced back in the direction of Draith who gave her an enthusiastic thumbs up." 
        "The Drider pranced excitedly in place. He reared up on his hind legs, exposing his undercarriage and the long, black sheath of his erect cock."
        dra "All right! He’s looking for his reward. Now: slowly approach him."
        #show alexia breeding angry at midleft with dissolve
        show alexia breeding neutral at midleft with dissolve
        al "Stay!"
        "The Drider went stock still. Alexia shuffled forward and clambered under his bulky frame. The Drider let out a low, pleasured coo."
        #cg1
        scene cg717 with fade
        show alexia breeding aroused behind cg717
        show draith happy behind cg717
        pause 3
        "Alexia planted the bucket onto the ground beneath his hovering cock and adopted an awkward stance. She was forced to bend low to reach the turgid shaft, its black carapace coloration providing a lurid bestiality to the whole affair."
        if all_actors["alexia"].corruption > 60:
            al "I think you deserve a reward."
            "Her lurid whisper was undoubtedly lost to everyone around her save the spider, and she somewhat doubted whether he could actually understand her or not."
            "It didn’t matter. The sight of his fat Drider cock caused Alexia’s mouth to moisten with excitement. She licked her lips, her fingers curling about his shaft with the forcefulness of a lover impatient to get started."
        else:
            "While Alexia had certainly… ‘expanded her horizons’ in recent months, she still was a bit mortified at finding herself face to face with a Drider’s imposing dick." 
            "Her fingers reached out with hesitant trepidation, before finally wrapping around the shaft in a gentle, double-handed grip."
        "She stroked him, moving up and down in a slow and steady rhythm. It was marvelous how much heat he gave off. He was a seething aura of sexual energy."
        "The Orcish handlers standing on either side of the Drider watched with amusement as the human handler worked a lather upon the creature’s cock, stroking it at a slow pace. Alexia spared a glance in Draith’s direction, who was watching her efforts with genuine interest."
        dra "Don’t be afraid to go at it a bit harder, Driders love the stimulation!"
        "Resolving to make the most of her compromising situation, and more than a little turned on by the lurid act, Alexia started to work the shaft at a faster pace, her elbows bending to the task as she jerked the creature’s long cock in swifter, shorter bursts."
        "The Orcs began to catcall, which brought a nervous blush to Alexia’s face. She {i}never{/i} imagined that this is where she would have ended up in her life: jerking off a sentient spider-morph in the dungeons of Bloodmeen Castle while a leering crowd watched her do it."
        if all_actors["alexia"].corruption > 60:
            "...Then again, it was almost {i}deliciously{/i} obscene. The sheer taboo of what she was doing brought a pleasant moistness to her nethers, an itching need to fill herself with this big, onyx shaft whose altar she was worshipping at."
        "Alexia wiped the sweat from her brow, her fingers coated in the Spider’s precum as she continued to work it up and down."
        "The Drider grunted and repositioned, raising his torso and legs so that Alexia was shaded by his tall bulk. His cock snapped up, moving almost to smack her in the cheek."
        if all_actors["alexia"].corruption > 60:
            "Alexia, overcome in the moment by the delightful eroticism on display, leaned forward and planted a little kiss upon the shaft. The Drider’s cock had a thick, rubbery texture. She licked her lips, marvelling at the exotic taste on her tongue."
        "Undeterred, Alexia picked up the pace, standing now with the cock level with her face. The Drider thrust its abdomen forward, its sheath bunching as her hands reached his base before jerking forward again."
        "She palmed his cockhead, rubbing the juices across her hands as she heard the hooting calls of the Orcs all around. Draith was shouting encouragements, but she barely heard them. She was focused entirely on the unique experience of this creature in her hands."
        "Her nose hovered perilously close to the Drider’s slick cock, the smell of its sexual juices permeating her nose and filling her with a deep, burning desire in her belly."
        if all_actors["alexia"].corruption > 60:
            "Alexia gripped the black spider dick in her hand in a vice, jerking him in fast, sudden strokes as if to squeeze every bit of the Drider’s milk out."
            al "C’mon you dumb beast: shoot your thick load out onto the floor!"
        else:
            al "{i}Cum{/i}. Cum for me!"
            "Her pace quickened still further, her face flushing red at the sight of the Drider’s bulging cock swell with every stroke. It was nearing completion."
        "The novice Drider handler felt a surge of triumph as the Drider’s cock bloated in her fingers. It’s thick cumvein swelled as it reached its climax."
        "Alexia dimly heard they encouraged shouting of Draith and his Orcish handlers in the background. She was transfixed by the curious beauty of seeing this pristine manhood swell with impregnating potential."
        "Snapping back to reality, she hurriedly pointed the creature’s cock downwards in the direction of the bucket."
        "She was just in time too, as the first surge of cum spurted out like a fountainhead, painting the bottom of the bucket in strings of pearlescent white."
        "She jerked him, coaxing the cum from his cock in long, languid strokes to help facilitate the process of extraction. The Drider hardly needed encouragement: once he began, there was little to stop him."
        "Spurt after spurt of white seed fired forth from his onyx cock, the chitinous cockhead swelling then discharging as Alexia looked on, simultaneously shocked and aroused at this crowning display of virility."
        "The Drider growled and hissed in supreme satisfaction. The bucket roiled with the growing puddle of spunk issuing forth from the creature’s prodigious genitalia. It took almost a minute for the drooling spurts to finally cease."
        scene bg25 with fade
        show alexia breeding aroused at midleft with dissolve
        show draith happy at midright with dissolve
        dra "My goodness! Excellent work Alexia, I’ve never seen a Drider respond so positively to a new handler before!"
        "Alexia clambered out from under the sedate Drider, who basked in his post orgasmic bliss. Her face was burning as she saw the leering grins the Orcs gave her as she walked over to Draith, a slushing bucket of Drider cum in her hands as she handed it to him."
        al "M-my pleasure, Draith."
        dra "You’re a natural, Alexia. I cannot thank you enough!"
        if all_actors["alexia"].corruption > 60:
            "No thanks were needed. If Alexia’s soaking panties were to be believed, it was {i}she{/i} who was now in dire need of a release."
        dra "Now we’ve just got a few more before we’re done for the day."
        show alexia breeding neutral at midleft with dissolve
        al "..."
        show alexia breeding shocked at midleft with dissolve
        al "{i}What?!{/i}"
        $ change_corruption_actor('alexia', +3)
        return

##########################################################################
##########################################################################
##########################################################################

label wild_animals_bite_back:

#catacombs BG
scene black with fade
show alexia breeding neutral at midleft with dissolve

"Alexia went down the long, winding stairs, into the depths of Bloodmeen Castle as per usual. It was a long, dark descent, and she was completely alone for the majority of it. She thought little of it. At this point, this had become a semi-regular occurrence."

#show alexia breeding angry at midleft with dissolve

"It was going to be a long day of cleaning in the Drider pits, Alexia could tell. The recent breedings had left the place a chaotic mess of spilled, unnameable fluids. Alexia was secretly dreading it."
"Her mind was in the clouds, picturing all the things she’d do once the unpleasant work of the day was over. A hot bath was on the top of that list."
"The sound of rustling wind at her back caused her to freeze. She glanced over her shoulder, seeing nothing. They were deep in the dark now, not far from the breeding pits."
"The animal part of Alexia’s brain twitched. Something was wrong. She glanced around, seeing nothing but shadows and the stairs twisting upwards like a harried snake. It was a particularly dim part of the castle, lit only by the distant torches set far apart down the stairs."

show alexia breeding concerned at midleft with dissolve

al "...Hello?"

"No answer. With some trepidation Alexia continued her descent, her steps quickened as she neared the bottom."
"Then, just as she came to the end of the stairwell and reached to the door leading to the pits, it appeared."

show alexia breeding shocked at midleft with dissolve

"The shadow of some massive form slunk from the darkness as if materialized from thin air. It let out a low growl."
"Alexia backpedaled, nearly toppling to the ground as it menaced her. She shrank back, her mind going blank as blind panic set in."

show whitescar neutral at cliohnaright with dissolve

"White fur. A hulking body. Long, black claws thick enough to eviscerate a man with a single swipe. It’s yellow eyes regarded Alexia with a bestial calculation, as if sizing up her prospective threat to him versus her value as a meal."

al "W-what..."

show alexia breeding concerned at midleft with dissolve

al "Who are you?"

"The creature let out a sharp snort. It stared at her with its piercing gaze for a moment longer, before finally blinking. Something about the action made Alexia let go of the tense breath she’d been holding."

whit "There’s a disgusting scent coming from behind this door. I haven’t been able to get it out of my nose since I arrived in Bloodmeen."
whit "I can smell it on {i}you{/i} as well, mortal."

"She was shocked to hear the creature speak intelligibly. Its voice was harsh and deep, its tone crude and belligerent. But Alexia could understand it."

whit "What are the Twins keeping behind this door?"

al "Th-they call it the Breeding Pits. It’s where they cage the beasts they’ve captured. Driders, mostly."

"This revelation seemed to only make the Wolf man mad. His clawed fists clenched as he let out a low growl."

whit "You cage them?"

show alexia breeding shocked at midleft with dissolve

"Words escaped Alexia. She felt a wave of primal terror her when the white wolf looked at her like that. If she had laid eyes on a monster such as him alone in the forest, she’d have run for her life."
"The wolf-man paused, taking a few experimental sniffs of the air. His gaze hardened on her as he let out a huff."

if all_actors["alexia"].relation >= 60:
    whit "You stink of Rowan. His mate, perhaps?"
    if all_actors["alexia"].corruption > 50:
        whit "Then again, you stink of more than a few others, as well."
        
elif all_actors["alexia"].relation < 31:
    whit "You have a whiff of Rowan upon you. Faint… but it’s there."
    if all_actors["alexia"].corruption > 50:
        whit "Strange that I’d pick it out, amongst the dozen or so other scents I smell on you."
        
else:
    whit "Hm. Rowan’s scent. You’ve been intimate with him."
    if all_actors["alexia"].corruption > 50:
        whit "Strange that I’d pick it out, amongst the dozen or so other scents I smell on you."

whit "Who are you?"

show alexia breeding neutral at midleft with dissolve

al "I-I’m Alexia Blackwell. Rowan’s wife."

"The beast regarded her with something approaching confusion. He cast his glance backward towards the closed door then refocused on her."

whit "I am Whitescar, Emissary of the Fae. What are you doing down here?"

show alexia breeding concerned at midleft with dissolve

al "J-just… just working. What are you doing down here?"

whit "Investigating my prospective allies. Who leads the… ‘work’ down here?"

al "That’d be Draith. The Dark Elf beastmaster."

scene bg25 with fade
show alexia breeding neutral at edgeleft with dissolve
show whitescar neutral at cliohnaright with dissolve

whit "{i}Beastmaster{/i}!"

show draith neutral at midleft with dissolve

dra "W-wuh- what?!"

"The white wolf yanked the shocked Elf out of his chair and lifted him bodily into the air. His slender legs dangled feebly as he stared wide-eyed at the beast that had appeared in his office."

whit "I should have known I’d find one of your kind lurking in the muck."
whit "Is what Rowan’s mate told me true? Do you cage these beasts at the Twin’s behest?"

"Alexia shuffled into the room behind Whitescar, casting an apologetic look in Draith’s direction. To her surprise, he didn’t look afraid. Far from it, he looked amazed."

dra "By the Three! So the rumors were true, the true Fae really are here in the castle."
dra "You’re just… you’re beautiful!"

show alexia breeding shocked at edgeleft with dissolve

"Whitescar’s rage faltered. He cast a short, sharp look back at Alexia. He seemed just as confused at Draith’s reaction as Alexia was."
"The Dark Elf, far from being intimidated, reached out and brazenly ran his fingers through the fur on the Fae’s hand."

dra "Gods, it’s so soft!"

"Whitescar snarled, shoving the Dark Elf back onto his desk. He loomed over him, his thick shoulder blades clenching together with rage."

show alexia breeding concerned at edgeleft with dissolve

al "Whitescar, wait!"

"Draith, to Alexia’s shock, began to {i}laugh{/i}. He held his hands up in halfhearted defense."

dra "Sorry, sorry! I should have known better. Maybe proper introductions are in order?"
dra "I’m Draith. And yes, I am the Twins' beastmaster. But you’ve got it all wrong: I’m not abusing the creatures in my care, I’m just training them."

whit "A living thing does not need ‘training’ to know how to live. You’ve enslaved them."

dra "I’d like to think of it as ‘recruited.’"

"The Fae let out a towering roar. He rushed forward, planting himself over the helpless Dark Elf like a predator pinning its prey as he forced him back onto the table. Be bared his teeth, his snout mere inches from his face."

show alexia breeding shocked at edgeleft with dissolve

al "{i}Draith!{/i}"

dra "It’s okay, Alexia. I’ve got this."

show alexia breeding concerned at edgeleft with dissolve

al "But he’s going to-"

dra "Trust me. I know the difference between anger and bloodlust."

"How could he be so calm in a moment like this? Whitescar looked like he was inches away from killing him! But Draith was as serene as a fish in a storm. He smiled at the snarling beast."

dra "You think I’m just like my brothers slaving under the Sisters of Slaughter, don’t you? That I beat and torment animals for the fun of it. You’re wrong, I care for these creatures."

whit "It does not matter if you ‘care’ for them. You cage them all the same."

dra "The animals we capture are hunted mercilessly by the Rosarians. They slaughter them wherever they find them. Rowan himself helps me collect them, to protect them."
dra "Andras promised me that once their conquest was over, they’d all be set free to roam the world once more. If it wasn’t for the Twin’s efforts, these poor creatures would already be dead."

whit "The barbed whip on the table by your hand proves your lie, torturer."
whit "Reach for it. I dare you."

dra "I’d never make it. And it wouldn’t matter if I did, would it? I doubt it’d do much more than anger you."
dra "...You’ve felt its sting before, haven’t you?"

show alexia breeding shocked at edgeleft with dissolve

scene cg718 with fade
pause 2
scene cg719 with fade
pause 2

"Whitescar tensed. His eyes blazed with white fury as he seized the Elf by the neck and smashed him against the wall. It shook with the impact. Draith’s hands went involuntarily towards his closed windpipe, but he let them fall to the side in a meek gesture of submission."

show alexia breeding concerned behind cg719

al "Please, let him go!"

"Whitescar stood still as stone, frozen to the spot, glaring into the eyes of the unintimidated Draith. At last his grip loosened, and the Dark Elf took in a deep breath."

show draith neutral behind cg719 
show whitescar neutral behind cg719

dra "I… don’t know who did this to you. But I offer my life in their place." 

whit "Their sins are not yours. You have nothing to offer me, runt."

dra "Then why are you gripping me so tightly?"

"There was a long silence. Alexia did not fully comprehend the dynamic at play here, but she was catching on to the fact that Draith wasn’t in any real danger. This was less of a threat to his life, so much as a strange struggle for dominance."
"Whitescar growled, dropping Draith to the ground before dragging him once more over to the table. The Elf let out a short gasp, before the beast’s lurid intent became evident."

dra "Ah… Alexia you’re off for the day, okay? D-don’t worry about me, I’ll be fine."

menu:
    "Stay and watch.":
        $ released_fix_rollback()
        #show alexia breeding angry at edgeleft with dissolve
        show alexia breeding neutral at edgeleft with dissolve
        al "N-no, I’m staying here!"
        show alexia breeding concerned at edgeleft with dissolve
        al "I… need to make sure you’re okay. "
        if all_actors["alexia"].corruption > 30:
            show alexia breeding aroused at edgeleft with dissolve
            "In truth, that was just the convenient excuse. There was something terrifyingly arousing in the way Whitescar moved. He had a hunter’s purpose, a sort of ceaseless aggression that spoke to Alexia’s baser urges."
            "She wanted to see the beast in action."
        dra "S-suit yourself, but I’ll warn you: things might get a bit messy from here on out."
        whit "Quit your whimpering, runt."
        "The Fae busied himself with disrobing his erstwhile opponent. His long finger-claws ripped Draith’s leggings down the middle like they were nothing. He yanked them off in one, great tear, leaving him naked."
        dra "Hehe… I’ll only whimper if you ask me to."
        "Whitescar let out a growl and slammed his fist onto the part of the table directly next to Draith’s head. The Dark Elf remained utterly unphased, smirking back at the Fae as if they were playing some strange game with each other."
        dra "You’ll have to do better than that to make me quiver."
        whit "Why don’t I tear your throat out then?"
        dra "But you won’t be able to hear my squeals then!"
        #cg1
        scene cg720 with fade
        show draith neutral behind cg720 
        show whitescar neutral behind cg720
        pause 3
        "Whitescar growled. He seemed more annoyed than angered by Draith’s insolent tone. If anything, he sounded excited. His hips positioned against Draith’s body, the red, pulsing weight of his cock pushing free inch by inch from its sheath."
        dra "What are you waiting for?"
        "Draith’s voice was breathless, airy and whimsical. There was a peculiar kind of grace in the way he shifted beneath Whitescar’s bulk, stretching languidly back onto the table as he displayed his nude body for the white wolf’s purview."
        whit "I’m not waiting, runt. I’m sizing you up."
        dra "Could have fooled me."
        "Alexia was shocked at the ease with which Draith handled Whitescar. The Fae spread the Elf’s legs, exposing his hardening member and the supple curve of his rump upon the table. Draith wiggled his hips back and forth. "
        dra "Come on, I’m already primed and ready for you."
        scene cg721 with fade
        show draith neutral behind cg721 
        show whitescar neutral behind cg721
        pause 3
        whit "Like a bitch in heat."
        dra "Hehe. Guilty as charged!"
        "By now the full length of Whitescar’s red cock was exposed. It was bestial in shape, a long, veiny bulge with the glans ending in a point. It’s base was a bulb of swollen nerves made for knotting their copulation partners."
        "Alexia swallowed as she imagined what such a thing would do to Draith. The Elf was so {i}small{/i} compared to his partner, but evidently that wouldn’t deter him."
        "Whitescar angled his hips in precise, controlled movements. Despite his overwhelming strength, he moved with calm surety. He planted his paws on either side of Draith’s head and leaned forward, commanding his attention with his large furry form."
        "He angled himself towards the Elf’s unspoiled asshole with short, humping movements. This was no tender moment, no kind foreplay or exchange of pleasure. This was a hunt, and Draith was the challenge to be overcome. Thankfully for everyone involved, Draith liked being his prey."
        "He cock brushed against the crack of the Elf’s ass and Draith shivered, settling in and wrapping his arms around Whitescar’s thick neck. The Wolf growled a warning, but the Elf ignored it, humping back against him as the tip drew ever nearer to its terminal destination."
        "Then, without warning, Whitescar thrust forward."
        "The first sign Alexia had of what had just occurred came when she saw Draith’s fingers clench against Whitescars neck."
        scene cg722 with fade
        show draith neutral behind cg722 
        show whitescar neutral behind cg722
        pause 3
        dra "{i}Oooooh{/i}, by the Three that’s deep!"
        scene cg723 with fade
        show draith neutral behind cg723
        show whitescar neutral behind cg723
        pause 3
        "Whitescar did not spend much time in establishing a relentless tempo. He thrust hard against Draith, pinning him hard to the table as he laid his whole form atop him. The Elf was smothered under a layer of white fur."
        "Whitescar’s teeth pulled back on his snout as he humped hard in short, sharp strokes, his legs bending and lifting repeatedly." 
        "Alexia’s face went beet red as she observed the brutal way he treated the Elf. He did not slow or pause his thrusts for an instant. His tail wagged as his shapely flank pulled back before thrusting like an animal against him once again."
        "Draith moaned and gasped beneath the wolf’s form, and Whitescar rewarded him by leaning downwards, licking the sweat off of his chest. He took in a long, deep inhale of his skin near his throat then grunted in appreciation."
        whit "You’ll do. For now."
        dra "C-color {i}ah{/i}! Color me impressed!"
        "The Fae grinned at Draith. Or, more accurately, he bared his teeth at him. But Draith laughed, pulling close to plant a cheeky peck on the beast’s snout. Whitescar growled and seized the Elf’s wrists, pinning him back against the wall as he picked up the pace."
        "Their playful battle of dominance devolved into animalistic fucking rapidly enough. Soon, the table upon which Draith was pinned was smacking repeatedly against the wall. The only thing Alexia could hear rise above it were the increasingly loud cries of Draith himself."
        dra "{i}Ah! Ah! Ah! H-harder{/i}, you beast!"
        "Whitescar obliged him, his hips pistoning hard as his turgid length slid deeper and deeper into the valley of the Elf’s ass. Soon his knot was bumping against his asshole, sending jolts up Draiths’ spine as he tried to maintain some sort of composure."
        "But the White wolf was too much for him. He fell back against the table, shivering and shaking as he let out a shout of pleasure. A thin stream of cum shot forth from Draith’s cock and painted his chest and belly in long lines of white."
        dra "O-oooooh f-{i}fuck{/i}!"
        "But Whitescar did not slow his thrusts for the sake of his spent lover. If anything, it merely emboldened him: a predator proving his ultimate dominance over his lesser prey. The Wolf growled and fell hard against the Elf, mashing his fur against his wet chest."
        "The thrusts grew shorter and shorter, until Alexia was sure that the table itself would give out on them. Whitescar was rutting against Draith so hard that the table legs were banging hard against the stone ground."
        "She’d have been afraid for the Elf’s life… were he not so clearly enjoying every second of it."
        dra "Come on, drain it out in me. I {i}dare{/i} you!"
        show cg724 with sshake
        show cg724 with sshake
        pause 2
        show cg725 with flash
        pause 3
        "Not about to let the masochistic Elf off the hook, Whitescar did. He let out a bellowing howl as his thick wolf cock thrust once, twice, three times, then {i}shoved{/i} his hips forward. His bloating knot pressed, then slipped into Draith’s overworked ass with a loud pop."
        "Draith screamed in a voice that sounded like a curious mixture of pain and pleasure. Whitescar leaned hard against him, his tail wagging back and forth in sharp bursts before puffing out as he released his pent up seed within the hapless Elf’s rectum."
        dra "Oh m-my- {i}guh{/i}!"
        whit "Careful what you wish for, runt."
        "The two held there in place for a long moment, the Wolf’s cock pulsing his sperm directly into Draith’s ass in thick, pumping gouts. A blissful look overtook Draith as he laid back and took it."
        "For all his harsh words, Alexia noticed that the Wolf was letting out cute little yips of pleasure himself. Tied together for the foreseeable future, Whitescar allowed the exhausted Elf to wrap his hands around his back and pull him close."
        dra "That was amazing. Your people are fierce lovers."
        whit "We’re even fiercer warriors."
        dra "Of {i}that{/i}, I have no doubt."
        scene bg25 with fade
        show alexia breeding aroused at edgeleft with dissolve
        show draith happy at midleft with dissolve
        show whitescar neutral at cliohnaright with dissolve
        dra "Uh… Alexia? We’re probably going to be here a while. Mind fetching me a towel?"
        dra "..And maybe a bucket."
        show alexia breeding neutral at edgeleft with dissolve
        "Shocked out of her stupor, Alexia stood to attention."
        al "Uh- yeah! Okay! S-sure!"
        "Her cheeks were aflame as she fled the messy scene. She had initially stayed for the sake of making sure that Draith wasn’t going to be killed by the angry Fae. But such fears had quickly died in the passion of their lovemaking."
        "...So why had she stayed? The question dogged her for several minutes after as she rushed to find something to clean up the wet, animalistic sex off the ground."
        return



    "Leave while you still can.":
        $ released_fix_rollback()
        al "Y-you’re sure you’ll be okay?"
        dra "I’ll be fine. Whitescar and I are just having a… {i}spirited{/i} discussion!"
        dra "Close the door on the way out, will you sweetie?"
        "Alexia shut the door behind her, profoundly confused as to the interaction that had just occurred. Apparently, Draith had… ‘diffused’ the situation? At the very least she didn’t think Whitescar would hurt him."
        "...Best not to ask too many questions."
        return


