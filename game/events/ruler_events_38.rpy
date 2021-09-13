init python:
    
    event('conors_fate', triggers="week_end", conditions=('week > 30', 'avatar.corruption < 31',"castle.buildings['sanctum'].lvl >= 1",), group='ruler_event', run_count=1, priority=pr_ruler)
    event('why_karnas_failed', triggers="week_end", conditions=("castle.buildings['sanctum'].lvl >= 1",), group='ruler_event', run_count=1, priority=pr_ruler)
    event('rowans_dominance_display', triggers="week_end", conditions=("castle.buildings['sanctum'].lvl >= 1", 'all_actors["alexia"].corruption < 31',), depends=('xzaratl_s_advances',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('cliohnas_domination', triggers="week_end", conditions=('cliohnaResistance >= 2',), depends=('another_visit_to_Cliohna',), group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="images/Backgrounds/library.jpg")
    event('shaya_capital', triggers="week_end", conditions=("castle.buildings['brothel'].lvl >= 1",), group='ruler_event', run_count=1, priority=pr_ruler)
    
label conors_fate:

scene bg6 with fade
show rowan necklace concerned at midleft with dissolve

"Rowan sat alone at his desk, his head buried in his hands. He had spared himself this brief moment of weakness, a quiet admission of the unbearable weight of responsibility that lay upon his shoulders."
"The moment he’d returned from a grueling week of travels, he was confronted with a swarm of paperwork and emergency missives. Liurial was gone, off attending to some minutiae elsewhere, and he was left alone to handle the mess."

show rowan necklace angry at midleft with dissolve

"It was an endless ordeal. And it never got easier. The lists and lists of names - of villages burned and the loot taken at their expense - only deepened his guilt."
"The fall of Raeve keep had been a boon to the Twin’s cause… and ruination to those stuck under their bootheels. Rowan let out an angry sigh. The challenge of serving as the Twins’ unwilling lackey had finally, for a brief moment, overwhelmed him."
"What was he even {i}doing{/i} here, anymore?"

#courtyard bg
scene black with fade
show rowan necklace neutral at midleft with dissolve

"The light was dying in the western sky when he finally escaped from the carefully collated piles of human misery that littered his desk."
"Rowan walked with a slump-shouldered gait, his eyes to the ground and his mind in some low place in his chest. The sun was a fading disc of orange and red that hung like a drooping eyelid over the ugly wrinkles of the world."
"A trickling stream of newly-arrived slaves were flowing in from the front gate, driven forward by a phalanx of Orcish guards. They shouted and shoved when one fell out of line, yanking them up by the scruff of the neck when they failed to rise from the ground quick enough."

show andras displeased at midright with dissolve

an "Hey, servant. Come here."

"Rowan’s eyes snapped up. Andras. Not the person he was hoping to see today. The Demon was standing next to the castle’s main gate, leaning against the wall as if bored with the ongoing spectacle. Rowan did his best to hide the angry scowl that threatened to break out across his face."

show rowan necklace angry at midleft with dissolve

ro "What is it... ‘Master?’"

show andras angry at midright with dissolve

an "Drop that insolent tone, whelp. I just gave you an order."

"Rowan noticed that a small group of them had been separated from the rest, cowering behind the looming bulk of Andras. They were manacled together in a chain-gang, six of them on their knees, as if awaiting execution."
"...Maybe they were. Rowan heaved a sigh and sidled up next to him."

show rowan necklace neutral at midleft with dissolve

ro "What do you wish of me?"

show andras displeased at midright with dissolve

an "This prisoner claims to know you. Is he lying?"

"Andras gestured in the direction of the hollow-eyed spectre kneeling at the front of the chain gang. When he lifted his head, Rowan’s blood ran cold."

show rowan necklace shock at midleft with dissolve

ro "...Conor?"

conor "{i}Rowan?! {/i}"
conor "Solansia, preserve me, I-I thought you were dead!"

"Rowan felt the bottom go out of his stomach. It was another survivor of Arthdale. Rowan recognized that curly mop of brown hair and wiry frame from anywhere."
"It was Conor, the Baker. Rowan had grown up just down the street from the young man. They’d known each other for years. Gods above, what was he doing here?"

show andras smirk at midright with dissolve

an "And here I thought I’d get to cut out a liar’s waggling tongue. Shame."

"Andras laughed aloud. Judging from the paralyzing fear that filled Conor’s eyes, he was already well acquainted with the Demon’s cruel particularities. "

show rowan necklace angry at midleft with dissolve

ro "What is he doing in chains?"

an "What do you think the rest of the prisoners are wearing, fool?"

"Rowan bit back an angry retort. He had to stay in control. For the sake of salvaging whatever could be salvaged from the situation, he needed to keep a level head. His hand was white-knuckled upon the pommel of his blade as he turned to face Conor."

show rowan necklace concerned at midleft with dissolve

ro "...How did you get here, Conor?"

conor "I… I managed to flee the carnage just as the Orcs attacked. M-my wife, she… she-"

"Tears built up in the exhausted man’s eyes. Rowan could do little but look on in pity. The prisoner took a moment to compose himself. His shirt was scruffed and bloody. He looked like he had taken a beating before capture."

conor "I fled to a nearby village, where some distant relatives were staying. I’d been scraping together whatever I could, making ends meet ever since."

show rowan necklace neutral at midleft with dissolve

"And now, Rowan had brought doom upon this poor man’s head for a second time. Guilt wormed its way into the center of his chest like a burning needle through his heart."

conor "…We thought you were dead, Rowan. Everyone assumed you’d been killed in the initial attack. So when he said you were here I-I-"

an "He got mouthy. He said that if the one of the Six Heroes were here, I’d have a sword shoved in my belly."

show andras displeased at midright with dissolve

an "Brave, but stupid. Very stupid."

"Andras strode up to the man, taking him by the back of the head. He lifted him by the roots of his hair so that he and Rowan were forced to look at each other."

an "So, Rowan, fancy your chances?"

show andras angry at midright with dissolve

an "{i}Do you see a sword in my belly, slave?{/i}"

"Andras’ inhumanly strong fingers clenched against the back of the man’s head. Conor screamed."

menu:
    "Demand he be set free.":
        $ released_fix_rollback()
        show rowan necklace angry at midleft with dissolve
        ro "..Let him go."
        show andras displeased at midright with dissolve
        an "What did you just say to me?"
        ro "I said let him go! What is he to you? The last raid brought you dozens of slaves."
        conor "R-rowan?"
        "Andras’ expression darkened. He shoved Conor forward, toppling him to the ground. He smashed face-first into the dirt. The Demon put his boot upon the back of the man’s head, trapping him in place."
        an "What is he to me?"
        "It took only the tiniest bit of pressure as he leaned into him with his leg, but Conor’s tortured cry of pain sent shivers down Rowan’s spine."
        an "Less than nothing. But it looks like he means something to {i}you{/i}."
        
    "Reason with Andras.":
        $ released_fix_rollback()
        "Rowan could do little but tremble in place, enraged beyond words. If he intervened now, Conor was a dead man. The only hope he had was to talk Andras down."
        show rowan necklace angry at midleft with dissolve
        ro "Master, we have only just begun our conquest of Rosaria. Until we complete that task, the slaves I’ve acquired for you remain a valuable commodity."
        show andras smirk at midright with dissolve
        if society_type == "feudalism":
           an "Heh. Not so valuable as to excuse your Lord getting insulted."
        else:
            an "Perhaps the slave should have thought about that before he insulted me."
        ro "That may be the case, but we can’t afford to make an example of every slave with a loose tongue."
        "Andras’ smile was cruel and pitiless. He strengthened his grip on the poor man’s head, eliciting an even louder cry of pain than the one before."

"Rowan’s eye was drawn to a sudden flash of green above Andras’ head. He looked up to see a forlorn figure standing upon the parapets, overlooking the proceedings."

ro "Alexia…"

"She saw them. She’d seen everything. Her eyes were glued to the back of Conor’s head. The two made brief eye contact, and Rowan saw the glimmer of dread reflected back at him."
"Swallowing down the shame that built in his chest, he redirected his attention once more to the threat in front of him. He couldn’t get distracted, not if he wanted to spare Conor from a terrible fate."

ro "Gods above, he’s learned his lesson! Conor, if you could, would you take back your words?"

conor "Y-yes! Kharos take me, yes!"

"Rowan looked to Andras and affected a careless shrug. It took everything in his power not to draw his sword and prove Conor’s harmless threat true."

ro "You have proved your point. He won’t make the same mistake again."

"There was something frightening in Andras’ eyes as they turned to regard Rowan. It reminded him of that terrible day when he’d been forced to decide the old Elder’s fate."

an "So it seems."

show andras happy at midright with dissolve

an "Fine. I’ll leave it up to you what we do with him."

show rowan necklace concerned at midleft with dissolve

"Andras threw his hand in a careless gesture towards the five men chained together. They cringed when he indicated him, huddling into a nondescript pile in an attempt to avoid being singled out."

an "This lot were headed to the lower reaches of the castle for menial work, but it looks like there’s been a change of plans."
an "Letting a slave insult me is something that cannot go unpunished. Someone {i}else{/i} might try something a bit bolder next time."
an "So {i}one{/i} of them is going to be headed to the mines instead: either your slave friend, or his companions."

show rowan necklace neutral at midleft with dissolve

"The mines were a death sentence, especially for the battered and broken bodies kneeling before him. They wouldn’t last a month in those conditions. Rowan cast a short glance up towards the spot on the wall where Alexia was standing. Her hands were over her mouth."
"Rowan made his face an empty mask. If he were to show the slightest bit of the emotion raging inside his chest, Andras would know that he had won." 
"Condemning a person he’d known since childhood to a merciless fate for the crime of spitting out a careless, toothless insult… or condemning five innocent men for a harmless action they hadn’t even committed."

show rowan necklace angry at midleft with dissolve

ro "..Just how long do you plan to keep doing this to me?"

show andras angry at midright with dissolve

an "Until you learn your place."
an "Decide."

menu:
    "Send Conor to work the mines.":
        $ released_fix_rollback()
        $ conorJob = "mines"
        "Rowan tried to get the words out, but they choked in his throat. He took a moment to compose himself, letting out a weary sigh."
        show rowan necklace concerned at midleft with dissolve
        ro "Send Conor to the mines. He’s the one who…"
        show rowan necklace angry at midleft with dissolve
        ro "‘Offended’ you."
        show andras displeased at midright with dissolve
        an "Boring. I was hoping you’d surprise me for once."
        "Andras stepped back, releasing the slave from his prone position. Conor lifted his head to stare imploringly into his old friend’s eyes."
        conor "Rowan… {i}please{/i}…"
        "From an outsider’s perspective, Rowan was expressionless. But internally, his heart felt like it was about to burst from his chest."
        conor "Gods, don’t let them do this to me!"
        "Instead of responding to his emotional entreaty, Rowan gestured to a few Orc guards standing watch nearby. They seized Conor by his arms and lifted him bodily off the ground, all but dragging him to his grim fate."
        conor " No! Please! I didn’t know! {i}I didn’t know!{/i}"
        "Rowan stared at the wretched form of Arthdale’s baker as he receded into the distance, unable to tear his gaze away from the horror of what he’d just done."
        an "Send the rest of them to their original work detail. Let them know the mercy of my leniency."
        "{i}Mercy is a word you are incapable of comprehending{/i}. Spoke a dark, hateful voice in the back of Rowan’s mind. He no longer knew if the thought was directed at Andras, or himself."
        
    "Send Conor to work in the kitchens.":
        $ released_fix_rollback()
        $ conorJob = "kitchens"
        "He couldn’t do it. He couldn’t bring himself to doom a man he’d known for so long to such an awful fate. It took everything he had to look the five men in the eyes, he owed them that much at least."
        show rowan necklace concerned at midleft with dissolve
        ro "Conor is a- "
        ro "H-he’s a talented baker. He’d be more useful to you serving in the castle kitchens."
        "A malicious grin spread across Andras’ face as he sneered at Rowan. The merciless creature seemed to revel in the way it made him squirm. Andras  gestured once again towards the five men huddled together in chains."
        show andras smirk at midright with dissolve
        an "And what should we do with the others, then?"
        ro "You know what we should do."
        show andras displeased at midright with dissolve
        an "I want to hear you say it."
        ro "...Send them to the mines."
        "The five damned souls let out piteous moans of anguish. Andras, delighted, made a sharp gesture with his hand. The Orc guards who had been standing by rushed forward, seizing the men and hustling them to their feet."
        "They were herded - backs bent and heads bowed - towards their new destination: the black pit where they would spend the rest of their miserable days in toil and suffering. Some cursed Rowan, others begged for mercy. One, the oldest, merely wept."
        "Andras released his grip on Conor and laughed."
        show andras happy at midright with dissolve
        an "He can work the kitchens, if he can keep his mouth shut."
        an "Thank your ‘Hero’ for your life, slave. He may not have run a sword through me, but he at least managed to spare you."
        "Conor babbled out a hushed {i}thank you{/i} as he was led away to the kitchens. Rowan couldn’t even look him in the eye."
        show andras displeased at midright with dissolve
        
an "That’s enough fun for the day, I think."
an "I have a banquet with Jezera, any more trouble from your ‘old friend’ will be on your head, servant."

show rowan necklace neutral at midleft with dissolve

ro "Understood, Lord Andras."

an "Good. I’d hate to have to repeat myself."

hide andras with moveoutright

"Content that he had gotten his pointless lesson across, the Demon turned and left. Six lives destroyed, all in the space of a few minutes, and yet he had somehow grown bored with the travesty."

show rowan necklace angry at midleft with dissolve

"Rowan stared at Andras’ retreating back as the Demon stomped away, off to commit some new barbarity or vulgarity. He felt his hand drift once more to the sword at his side, his fingers clenching against the pommel."

ro "...I’m going to kill you one day. And when I do, I’ll make sure to split your belly open first."

"The words were spoken with a whisper, but they had the strength of iron behind them. Rowan looked up at the empty spot on the wall where Alexia had been standing. He sighed."

show rowan necklace concerned at midleft with dissolve

ro "I guess I should go talk to her."

scene cg743 with fade
show alexia 2 necklace neutral behind cg743
show rowan necklace neutral behind cg743
pause 3

"Night was coming. The final rays of light were fading away to nothing in the coming gloom. There, sitting alone with her back to him, Alexia sat upon a crenellation of the wall."
"Her body was silhouetted by the setting sun, hunched forward as she stared out across the empty wastes beyond the castle."

ro "Alexia? What are you doing up here?"

"She didn’t respond. Rowan let out a sigh and walked over to her. She didn’t so much as glance in his direction as he sat down on the crenellation next to her. Her face was expressionless, her eyes dull."

scene cg744 with fade
pause 3

if all_actors["alexia"].relation >= 60:
    "Rowan reached out and took her hand. His fingers threaded through her slender grasp and squeezed. Alexia looked at him, her glimmering green eyes holding to his for a long moment. He flashed a sympathetic smile."

    
elif all_actors["alexia"].relation <= 30:
    "In the past, in a life now far removed from the one they now lived, Rowan would have wrapped his arm around his beloved wife and asked her what was wrong. Now, the tender words of worry dribbled out his mouth as a mechanical afterthought."
    
else:
    "In normal circumstances, Rowan would have rushed to comfort her. But there was a distance between them now, a hesitation in their interactions that made such attempts at empathy feel almost… hollow."


scene bg57 with fade
show alexia 2 necklace neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve

ro "Something on your mind, love?"

al "...Don’t do that. Don’t pretend like I didn’t see what just happened."

"Rowan’s shoulders slumped. He swallowed down the painful lump in his throat and nodded."

ro "I’m sorry. Andras put me on the spot. I… I didn’t have a choice."

"The look of condemnation in her eyes said otherwise, but to her credit she didn’t offer any real retort. She turned her gaze once more to the setting sun."

al "...Conor was my dad’s apprentice once, you know? He took over the bakery after he died. I knew him since we were children."

ro "I… I know."

al "He was always such a loudmouth, but he had a good heart. We used to sneak spare bread loaves from the ovens and sit together in the alley behind the bakery at lunchtime. "
al "Sometimes… birds would come, and we’d feed them together. Crows mostly, though sometimes we’d see the odd wood thrush, or even a robin. "
al "Once, a nightingale landed on top of his head, chittering away at him in its beautiful little voice. It was the boldest bird I’d ever seen."
al "I laughed so hard when Conor started shouting and capering about, waving his arms about like a loon to get it off his head."
al "He was {i}scared{/i} of it. Can you believe it? Such a little thing, and all it was doing was sitting on his head."
al "But still… he was..."

if all_actors["alexia"].corruption < 31:
    show alexia 2 necklace concerned at midright with dissolve
    "Alexia’s eyes filled with tears."
    show rowan necklace concerned at midleft with dissolve
    ro "...Alexia?"
    al "I-I can’t..."
    al "I can’t {i}do{/i} this anymore, Rowan!"
    "She buried her face in her hands, her shoulders shuddering as she sobbed. Overcome with emotion, she vented her sorrow towards the uncaring horizon."
    al "These people… this {i}place{/i}… it just never stops!"
    al "Every day it gets worse. Every day it feels like we’re just spiraling down deeper and deeper into a pit we can’t escape."
    al "I… j-just can’t take it a-any m-{i}muh{/i}-"
    "Alexia’s voice broke as tears streamed in tortured lines down her face. Her expression collapsed, revealing a frightened woman in its wake."
    if all_actors["alexia"].relation >= 60:
        show rowan necklace neutral at midleft with dissolve
        ro "Hey. Come here."
        show cg745 with fade
        show rowan necklace neutral behind cg745
        show alexia 2 necklace concerned behind cg745
        pause 3
        "She shivered as Rowan’s arms went around her shoulders and pulled her to his breast." 
        "Despite her painful hesitation, once she leaned into him Alexia’s body melded against his like a lifeline. She threw her arms around him, burying her face in his chest as she wept."
        al "What are we doing here, Rowan? What did we ever do to deserve this?"
        show rowan necklace concerned behind cg745
        al "All these people suffering... all our friends in Arthdale…"
        al "We lost everything, the life we built together… for {i}this{/i}?"
        "Rowan’s jaw clenched as he pulled her close and let her vent. He said nothing. What answer could he even give at this point?"
        al "I try so hard to stay strong… I-I really do!"
        al "I know how difficult it is for you. I kn-know how painful it must be... to look into the eyes of those {i}monsters{/i} every day and do their bidding."
        al "But I just can’t… I can’t keep pretending like…"
        al "L-like everything’s still okay!"
        ro "Alexia…"
        al "You’re the only real thing in this world that I have left, Rowan. You’re the {i}only{/i} person who- w-who remembers what it was like, before-"
        "Rowan felt something wet and warm fill the corners of his eyes. His throat constricted. He couldn’t afford to show weakness, neither of them could. But it was just so hard to hold it all in."
        ro "We’ll get it back. We’ll save them all. I swear to you, beloved: we will return there one day."
        "Alexia didn’t answer him. She simply cried. She knew Rowan too well to not recognize the bittersweet sound of an empty promise."
        "They stayed like that for several minutes, Alexia huddled against his chest as he held her close. Rowan gently stroked her hair, whispering quiet nothings into her ear."
        "At last, the storm subsided. Alexia let out a pained chuckle, wiping at her eyes as she tried to hide the misery that painted a sombre brush across her face." 
        scene bg57 with fade
        show alexia 2 necklace happy at midright with dissolve
        show rowan necklace concerned at midleft with dissolve
        al "I-I’m sorry, my love. I just…"
        show alexia 2 necklace concerned at midright with dissolve
        al "I don’t know what to do, anymore."
        ro "Neither do I."
        ro "If there was any way, I would have saved Conor. Set him free to let him find a life far away from this place."
        ro "But… I can’t risk it, not while you’re stuck in this mess with me."
        ro "Andras will be watching him now, to be sure he doesn’t suddenly ‘disappear’ from his job. The same goes for the other prisoners, I’d expect."
        ro "The Twins don’t trust me, and every little rebellion against their will only hardens their hearts against us. I’m sorry my love, but you’re my primary concern."
        show rowan necklace neutral at midleft with dissolve
        ro "Maybe, in the end, there’s nothing we {i}can{/i} do."
        show rowan necklace happy at midleft with dissolve
        ro "But I’m here for you. By all the Gods and all the Realms, I won’t let them hurt you Alexia."
        al "They’ve already hurt me, Rowan. They’ve hurt us both."
        show rowan necklace neutral at midleft with dissolve
        show alexia 2 necklace happy at midright with dissolve
        al "But least I’ve got you, as terrible as this place is. I..."
        al " I don’t know what I’d do without you by my side, Rowan Blackwell. I’d go mad, or-"
        show rowan necklace happy at midleft with dissolve
        ro "Become a spinster?"
        "Alexia returned a blank stare. Rowan’s face grew a knowing smirk. Then, at last, the aura of melancholy broke, and she choked out a laugh."
        al "Y-you {i}beast{/i} of a man!"
        "Alexia slapped his shoulder pad in sharp rebuke, her arms going about his shoulders as she clung tight to him."
        al "Don’t even joke about something like that!"
        ro "What? I think you’d look comely in black."
        show alexia 2 necklace angry at midright with dissolve
        al "One more morbid word out of you, and I’ll shove you off this wall myself!"
        show alexia 2 necklace happy at midright with dissolve
        "Rowan laughed, and Alexia laughed along with him. It was good to see her smile again."
        jump conorLowCorEnd
     
    #to do 
    #elif all_actors["alexia"].corruption > 60:
    
   
    else:
        al "What kind of life is this? What kind of people are we becoming?"
        al "All those innocent victims... everyone who died in Arthdale…"
        al "We gave up our lives, everything we’ve ever known… for {i}this{/i}?"
        "Rowan’s fists clenched against the crenellated rock. He stared out at the bloody sunset, searching for the unanswerable solution to her question in the fading purples of the evening."
        show cg745 with fade
        show rowan necklace neutral behind cg745
        show alexia 2 necklace concerned behind cg745
        pause 3
        "Rowan felt her arms go around his side, pulling tight against him as she searched for some semblance of warmth in the madness." 
        "After a moment’s hesitation, Rowan put his arm around her, leaning his head against her shoulder." 
        al "I try so hard to stay strong. I… I really do."
        al "I… I know what the Twins tell you to do. I know the cruelty they ask you to commit in their name."
        al "But… you don’t do it, do you? You wouldn’t just enslave people the same way they’ve enslaved us?"
        "Rowan very nearly managed to feed her a pleasing lie. But her searching gaze made his heart ache. He sighed and looked away."
        ro "...I do what I can to mitigate their worst impulses. I can only do so much."
        "She looked down at the ground, her tears staining his lap."
        al "W-why does it feel like everything we touch just turns to ashes in our hands?"
        ro "Alexia…"
        "She didn’t answer him. After a time she pulled away from the uncomfortable embrace, wiping at the corners of her eyes. Rowan could do little but watch in sympathy."
        al "...I don’t know what to do anymore."
        ro "Neither do I."
        al "It feels like we’re living in a nightmare. And I don’t know how to wake up."
        ro "Maybe we don’t. Maybe there’s nothing we {i}can{/i} do."
        ro "If there was, I would have saved Conor, set him free to find a life far away from this place."
        ro "But… I can’t risk it, not while you’re stuck here in this mess."
        ro "The Twins don’t trust me, and every little rebellion against their will only hardens their hearts against us."
        "Rowan took her hand in his. He mustered the most convincing smile he could manage."
        scene bg57 with dissolve
        show rowan necklace happy at midleft with dissolve
        show alexia 2 necklace concerned at midright with dissolve
        ro "But I’m here for you, Alexia. I swear: I won’t let them hurt you."
        show alexia 2 necklace neutral at midright with dissolve
        al "I… wish I could believe you, Rowan."
        show alexia 2 necklace concerned at midright with dissolve
        al "But we both know that’s a promise you can’t keep."
        show rowan necklace concerned at midleft with dissolve
        "She wiped at the tears that ran down her face, granting him a soft smile. It was so rare to see her smile these days."
        show alexia 2 necklace happy at midright with dissolve
        al "Solansia forgive me, when did things get so complicated?"
        show rowan necklace neutral at midleft with dissolve
        ro "Things were always this complicated, love. This is just the first time we’ve had to see it up close and personal."
        al "It shouldn’t have to be. We shouldn’t have to compromise who we are for the ‘privilege’ of living in this gilded cage."
        "Rowan had no real answer to that. Neither of them did. Fate had put them into this position, and it was largely fate that would decide how they’d escape it… if they’d escape it."
        jump conorLowCorEnd
        

elif all_actors["alexia"].corruption > 60:    
    #cg5
    show alexia 2 necklace angry at midright with dissolve
    "A terrifying shadow crossed her face. Her beautiful features twisted with sudden fury, her teeth gritting in anger."
    al "He didn’t deserve this!"
    "She rounded on him, her eyes ablaze, tears streaming down her face."
    al "H-how could you let this happen? Conor was our {i}friend{/i}!"
    ro "What was I supposed to do, Alexia? "
    al "Set him free! Tell Andras to let him go!"
    ro "Andras would have killed them all if I did that. You know how he is, I didn’t have a choice."
    al "Then stop him! Stand up to him! {i}I don’t know{/i}!"
    ro "Alexia…"
    al "Maybe we deserve this, maybe it was always our fate to end up here, but Conor did nothing wrong!"
    ro "There was nothing I could do."
    al "{i}Stop saying there was nothing you could do{/i}!"
    "Alexia shoved him. Hard. Rowan toppled off the crenellation, nearly plunging to his death in the process." 
    "He only just managed to throw his weight backwards, landing hard on the stone of the parapet with a loud thud."
    al "Be a man for {i}once{/i} in your damned life!"
    if all_actors["alexia"].relation > 30:
        "Her cruel words broke the spell of madness that had seized her. Alexia froze, her face going rigid with shock." 
        "They stared at one another, mutual expressions of dismay etched across their faces. A dreadful silence stilled the air."
        al "I..."
        al "Rowan, oh Gods, I- I’m so sor-"
        "Her mouth gaped as she tried to babble out an apology. Her choked voice faded away into feeble nothingness." 
        "Rowan picked himself off the ground and brushed himself off, dazed at her harsh words and the sudden shock of violence. They stared at one another in bewilderment, their silhouettes dark shadows amidst the setting sun’s rays."
        ro " ...Why?"
        "It was an innocent question, a childlike inquiry, filled with hurt and confusion. Alexia opened her mouth to speak, but words escaped her."
        al " I… I don’t know what came over me, I-"
        ro "What’s happening to you, Alexia? "
        "She shuffled up to him, trembling hands reaching out to touch his tensed shoulders."
        al "R-rowan, {i}please{/i}, I didn’t mean to-"
        
        menu:
            "Pull away from her.":
                $ released_fix_rollback()
                "Rowan stumbled backwards out of her grasp, tripping over himself to get away from the thing that had so wounded him. Alexia froze for a second time, horrified at his abrupt withdrawal."
                "His heart twinged with pain as he saw the despondent look that crossed her features in the aftermath. But he could not go to her, not after what she’d just done."
                al "Rowan I-I’m-"
                "Rowan’s hands grew clammy as an emotion that he couldn’t describe - an ugly mixture of impotent rage and utter despair - rose up within his gullet to choke the words from his throat."
                "He didn’t say a word to her. He couldn’t, lest the floodgates open and the tears come spilling out like so much useless rainwater on the ground. He just turned and walked away."
                "A muffled sob behind him told him all he needed to know. He’d hurt her, just like she’d hurt them. They were even now, he supposed. Not that it did much good for either of them in the end."
                "So much for the ‘Hero of the Six Realms.’ Rowan couldn’t even manage to save his own wife. He angrily wiped the tears from his face as he all but fled from the castle wall."
                $ change_relation('alexia', -15)
                return
                
            "Hug her.":
                $ released_fix_rollback()
                "How did things get so difficult?"
                "Rowan let Alexia step forward into his chest, wrapping his arms around her as she threw herself against him."
                al "I-I’m so {i}sorry{/i}! Please, forgive me beloved!"
                "Rowan didn’t know what to say, he just held her while she cried. It was like he was moving underwater. His mind was a detached spectator as his body moved on automation."
                "Hug her. Hold her. Stroke her hair. Whisper in her ear meaningless reassurances that things will be all right. This is what it takes to calm her down, to bring her to a normal level."
                "{i}This is what empathy looks like{/i}. A cold, distant voice in his head reassured him. {i}This is what a relationship should be{/i}." 
                "{i}Nothing made sense to him anymore{/i}."
                al "I didn’t mean to do it, I swear! I don’t know what came over me!"
                ro "It’s okay, Alexia. It’s all going to be okay."
                "All he could offer at this point were flavorless platitudes."
                al "Please, Rowan. I… I can’t do this without you."
                ro "I know."
                al "I {i}need{/i} you."
                ro "I know."
                al "Let me- let me make it up to you… please?"
                "She leaned forward hesitantly to kiss him, her searching eyes begging for his permission."
                
                menu:
                    "Kiss her.":
                        $ released_fix_rollback()
                        "In the end, he couldn’t resist her. He never could. Only Alexia could hurt him so and still bring him crawling back."
                        "She was his panacea - or, alternatively: his poison. The lines between them were so blurred and toxic that he didn’t know what she meant to him anymore."
                        "Rowan nodded, and she kissed him, their lips connecting with something approaching desperation."
                        jump conorSexScene
                        
                    "Not like this.":
                        $ released_fix_rollback()
                        "Rowan pulled away, and Alexia’s tears flowed anew. He put a finger to her lips and gently {i}shushed{/i} her."
                        ro "It’s okay, it’s okay. I’m just… not in the mood."
                        al "I-I understand."
                        ro "You don’t have to apologize."
                        al "I don’t deserve you."
                        "{i}No one deserves anything{/i}. Rowan thought as he hugged her close and let her bitter tears stain his shirt."
                        return
                        
            "Confront her.":
                $ released_fix_rollback()
                ro "Why would you do that to me, Alexia? Why would you even say those things?"
                al "I didn’t mean it, Rowan. I-I just- I wasn’t thinking, I was mad."
                ro "At me?"
                al "N-no! About… about Conor..."
                ro "You told me to ‘act like a man.’"
                "Alexia's eyes widened. She opened her mouth to speak, but no words came out. After a pathetic attempt to excuse herself, she lapsed into a miserable silence."
                ro "What do you want me to do, Alexia?"
                ro "The Twins have us trapped here, chained to their will by the necklaces around our necks."
                ro "It would be one thing if I was the only one stuck in this hell… but I have {i}you{/i} to think about as well."
                ro "I want nothing more than to protect these people, but you’ve seen what the Twins are capable of."
                ro "If I push too hard, arouse too much suspicion, we both die. And I can’t let that happen. Call it selfishness: but you’re my primary concern."
                "Alexia huddled into herself. She looked like she was on the verge of tears."
                ro "You’ve changed, Alexia. And I don’t think it's for the better."
                ro "Bloodmeen Castle’s corruption warps everything it touches. At first I thought we were immune to it."
                ro "...I guess I was wrong."
                al "Rowan, I-"
                ro "Don’t say anything. There’s nothing to say. It is what it is."
                ro "I guess we’ll just have to live with the consequences."
                al "Please Rowan, can you ever forgive me?"
                "Rowan stared into her teary eyes, guilt chipping away at his heart."
                ro "…I can only try, Alexia."
                "Her expression broke, her lip quivering as she threw her arms around him. Rowan reluctantly held her close, his heart hammering in his chest."
                al "I love you, I love you, I love you! I swear that I do! I’m {i}so sorry{/i}!"
                "She leaned forward hesitantly to kiss him, her searching eyes all but begging for his permission."
                
                menu:
                    "Kiss her.":
                        $ released_fix_rollback()
                        "Rowan kissed her. What else could he do? For all she had done to him, she was still his wife."
                        "No one else could make him feel this way: this destructive blend of affection and suffering rolled into one."
                        "She was his panacea - or, alternatively: his poison. The lines between them were so blurred and toxic that he didn’t know which was which anymore."
                        jump conorSexScene
                        
                    "Not like this.":
                        $ released_fix_rollback()
                        "Rowan pulled away, and Alexia’s tears flowed anew. He tilted her chin up to look at him."
                        ro "Not like this, Alexia. Not right now, not after what just happened."
                        al "I-I understand Rowan."
                        ro "Then you know why I’m saying no."
                        ro "Please just… let me take some time to process this? I need to think about things."
                        al "I don’t deserve you."
                        "Rowan winced. For all her faults, Alexia still knew how to tug at his heartstrings. He pulled her into a chaste hug."
                        ro "It’s going to be alright."
                        al "No… it won’t be. Not after what I’ve done."
                        "Rowan tried to spit out a denial, but the words got blocked in his throat."
                        return
                        
    else:
        "Rowan froze in place. His eyes went wide as he stared into the seething pit of anger that was the woman he thought he’d loved."
        "There was no apology in her eyes, no sign that she even recognized the gravity of what she’d just done. She leapt off of her seat and rushed forward, looming over him like a raging thundercloud."
        "He saw the look in her eyes. She… she {i}hated{/i} him at that moment. The stinging realization was like a splash of icy seawater to a gaping wound. Rowan was left speechless."
        al "Look at you. You don’t even have the good sense to be angry at me."
        if alexiaJezObedient == True:
            al "What happened, Rowan? Does Jezera keep your balls in a little box somewhere?"
        if alexiaAndrasObedient == True:
            al "What happened, Rowan? Did Andras break you in nice and hard?"
        al "You keep pretending like the world abides by your ridiculous moral code. Yet here you are: dancing like a puppet to the Twin’s strings!"
        al "Do you think you’re {i}better{/i} than me? Is that it?"
        al "Look around you, Rowan. Look at everything you’ve done. Do you think your ‘integrity’ or your ‘morals’ have saved anyone?"
        al "Raeve Keep has burned. Arthdale is {i}gone{/i}. Solansia only knows what you’ve got in store for us next!"
        al "You disgust me. For all your purity, for all your ‘principles,’ you’re just a weak-kneed coward."
        "Rowan stared at this merciless creature, unable to discern her human features. Who was this woman? What had she done with Alexia?"
        "But… the longer Rowan looked, the more despondent he became. In a way, it would have been easier had she been simply telling the truth."
        "For all her bold words, Rowan could see the tears in her eyes."
        al "{i}Well{/i}? Aren’t you going to say anything? All we ever seem to do anymore is argue, so I guess it’s your turn."
        al "So come on! Say it! Get mad at me!"
        al "{i}Do something{/i}!"
        
        menu:
            "Are you quite finished?":
                $ released_fix_rollback()
                "Rowan picked himself up off the ground and dusted himself off. He stared with cold impassivity into his wife’s angry eyes."
                ro "...Are you done?"
                "His empty tone only seemed to make her angrier. She slapped him. Hard. Rowan accepted it, turning his face to one side to lessen the stinging impact."
                al "Gods {i}damn{/i} you!"
                "Rowan allowed a humorless smile to spread across his cheeks."
                ro "They already have. You’re just the insult to the injury, at this point."
                al "You don’t care about me at all, do you?"
                ro "I care, Alexia. More than you can possibly know. It’s why I let you do this to me. You’re the only one who ever could."
                ro "You’re the only one who ever will."
                al "I don’t give a damn about your hollow pity, Rowan."
                "Rowan shrugged, a perfunctory rise and fall of his shoulders."
                ro "You don’t have to. It’s not my pity that’s keeping you alive."
                "Alexia’s glare could have melted stone. It was a good thing then that Rowan had long since hardened his heart to her."
                "He turned away without saying a word. It was just as well, she didn’t really have anything left to say, anyway."
                "So much for good intentions."
                $ change_relation('alexia', -5)
                return
                
            "Walk away":
                $ released_fix_rollback()
                "Rowan didn’t say a word as he stood up. He just looked at her. He searched for some sign of the woman he once knew, but could find nothing."
                "He turned away in a slow circle, moving with deliberate steps in the direction of the stairs. It had been a long day, and he was exhausted."
                al "Where are you going? Get {i}back{/i} here and yell at me!"
                "Rowan didn’t turn around, didn’t address her tortured voice. To acknowledge her now would be to give her the power she sought over him."
                al "{i}Rowan!{/i}"
                "Desperation colored her voice, the sort of hopeless panic a drowning man might have when lost at sea. Rowan could not be her rope to cling to, not this time. She had finally crossed a line."
                al "You bastard, you were {i}everything{/i} to me!"
                "Rowan stopped. He didn’t turn around, but she had - admittedly - managed to unnerve him."
                ro "...No."
                "Empty words. Like all the rest. How many platitudes had slithered past their mouths these last few months? Rowan was so tired of the lies."
                "He walked the final distance to the stairs in silence, dogged by the increasingly hysterical ranting of his wife at his back."
                $ change_relation('alexia', -15)
                return

            "Throw her words back in her face":
                $ released_fix_rollback()
                ro "You’ve got a lot of nerve treating me this way, you know that?"
                ro "You call me a coward, but when you went missing, {i}I{/i} was the only one who cared enough to look for you."
                ro "I {i}came back{/i} for you. I willingly fell into the Twin’s trap for you! I could have just abandoned you. The Elder himself told me to leave you to your fate!"
                ro "But I couldn’t do it, because the thought of you dying alone in this miserable place turned my stomach."
                ro "Every day, I blacken my soul for your sake. I’ve betrayed my oaths, killed my friends, stomped everything I ever believed in into the dirt."
                ro "And this is the gratitude I get?!"
                al "Oh, don’t get so high and mighty with me, Rowan Blackwell!"
                al "You think I don’t see the way you strut around the castle like a peacock preening his feathers?"
                al "For all your ‘selfless sacrifice,’ you sure love to put on airs. Deep down, you always wanted power."
                al " I saw how sullen you got when you returned from the Capital after the War. You {i}hated{/i} that you had to run back to your poor, little nobody wife in a podunk town in the middle of nowhere."
                ro "Is that what you think this is about? You think I give a damn about the trappings of authority?"
                ro "Just who the hell do you think I am, you heartless bitch?"
                al "{i}Fuck you{/i}, Rowan!"
                ro "I would, but I have standards."
                "Rowan caught her wrist long before the intended slap could land. Alexia struggled with him for a moment, shoving at him and punching his chest."
                al "L-let {i}go{/i} of me!"
                ro "With pleasure."
                "Rowan let go of her wrist and stepped back, taking care to avoid a second strike. Alexia’s eyes were narrow pinpricks of hatred that glared at him in the dying light."
                ro "I don’t know where we went wrong-"
                al "When I married you!"
                ro "...But I’m not going to stop being who I am. Love me, hate me, {i}damn{/i} me for all I care. I came back for you. I {i}protected{/i} you."
                "Alexia spat at his feet."
                al "I don’t need your ‘protection.’"
                ro "Maybe you don’t. But I do know this: I’m the best chance you’ve got of leaving this castle with even a shred of your soul intact."
                ro "Think on that Alexia, the next time you try to push me off a castle wall."
                "Rowan half expected her to rush him when he turned away, but instead he was greeted with silence." 
                "He paused at the top of the stairs to look back at her. She was standing alone, facing the sunset with a grim expression." 
                "Rowan let out an exhausted sigh, and descended into the Bowels of Bloodmeen once more."
                $ change_relation('alexia', -15)
                return

else:
    "Alexia trailed off. She turned away from him, staring out at the vast expanse of emptiness that were the Rakshan wastes. Her expression was… desolate."
    show rowan necklace concerned at midleft with dissolve
    ro "Alexia?"
    al "Hm?"
    ro "Are you okay?"
    if all_actors["alexia"].relation >= 60:
        "She turned to look at him, the evening sunlight gleaming in her emerald eyes. The wind blew a gentle breeze across her soft features."
        "Alexia shook her head, shifting her gaze towards the tall mountains in the distance once again." 
        show alexia 2 necklace neutral at midright with dissolve
        al "No."
        al "I’m not okay."
        al "I don’t think I’ve been okay for a long time, Rowan. Not since Arthdale burned."
        ro "That wasn’t our fault, Alexia."
        show alexia 2 necklace angry at midright with dissolve
        if alexiaJezObedient == True:
            al "Wasn’t it? Lady Jezera played us like a lyre. We fell right into her trap."
        else:
            al "Wasn’t it? We were fools to trust that girl."
        ro "How could we have possibly known who she was at the time?"
        "Her gaze sharpened. She turned to glare at him, a righteous anger filling her eyes. For a brief moment, it looked like Alexia wanted to hit him."
        "Then, just as quickly, the hatred dissipated. Alexia let out a tired sigh, unable to meet his sympathetic gaze." 
        show alexia 2 necklace neutral at midright with dissolve
        al "I’m losing myself, Rowan."
        al "I can feel it. Something’s changed."
        al "Maybe it’s this castle, maybe it's the shock of what happened at Arthdale."
        show alexia 2 necklace angry at midright with dissolve
        al "Or maybe I’ve {i}always{/i} been this way, and I was just too blind to see it."
        show alexia 2 necklace neutral at midright with dissolve
        al "But with every day that passes, I feel less and less like the girl you once knew."
        
        menu:
            "That’s not true.":
                $ released_fix_rollback()
                "Rowan took her hand in his. Alexia turned to meet his earnest expression."
                ro "You’re still the woman I fell in love with, Alexia."
                al "I don’t think I am. I don’t know {i}who{/i} I am, anymore."
                ro "{i}I{/i} know who you are. And that’s all that matters."
                show alexia 2 necklace happy at midright with dissolve
                al "Hehe. You… really are a silly man sometimes, Rowan."
            
            "Why do you think you feel this way?":
                $ released_fix_rollback()
                "Alexia’s smile trembled, as if she were but inches away from tears. She took a deep inhale and let out a sigh."
                al "I don’t know."
                al "Or, I guess I do. But I don’t know how I can explain it to you in a way you’d understand. I just... can’t resist it."
                al "Before, I would have been horrified about what happened to Conor. Now though, I just feel empty."
                ro "It’s a coping mechanism, Alexia."
                ro "Sometimes, the worst experiences take a bit of willful delusion on our part to survive. It’s easier on our hearts to just duck our heads down and cover our ears."
            
            "What’s happening to you?":
                $ released_fix_rollback()
                al "I don’t know… I don’t know if I even understand it myself."
                al "I know how I should react, how I {i}would{/i} have reacted had I been exposed to these things back in Arthdale/"
                al "But now, when I find myself confronted with what’s going on around here I just…"
                "She trailed off, nibbling on her lip in worry."
                al "M-maybe I’m just overthinking things, huh?"
                "Her nervous laughter and unconvincing smile belied the strained tone in her voice."
            
        show alexia 2 necklace concerned at midright with dissolve
        al "I wish I could be as strong as you. I admire you for that, truly I do. But..."
        "She opened her mouth to say something more, but then seemed to think better of it. She looked away from him. A pained expression crossed her face."
        ro "But... what?"
        al "Nothing. I’m talking nonsense, now."
        al " I… I’m sorry, Rowan."
        ro "Sorry for what?"
        al "For bringing you to this place. For making you suffer like this."
        al "Conor deserved better. {i}You{/i} deserve better."
        ro "Alexia..."
        al "You shouldn’t have tried to rescue me. You should have just left me to rot. The world would’ve been a better place if you’d just forgotten about me."
        show rowan necklace angry at midleft with dissolve
        ro "W-what-"
        "An anger Rowan couldn't describe bubbled up inside his chest at her words. All of the repressed feelings and burning resentments he’d been storing up since Arthdale rose like bile from his throat."
        ro "What are you {i}talking{/i} about?! Stop saying things like that!"
        "He seized the shocked Alexia by the shoulders, shaking her from her mournful stupor. His eyes were ablaze, his hands were trembling with an indescribable fury that he could no longer keep in check."
        ro "Why do you think I’m here right now? Why do you think this gods-forsaken necklace is wrapped around my neck?"
        ro "Do you think I like helping them? Do you think I {i}enjoy{/i} serving them?!"
        ro "I did this all for you! I am damning myself for {i}you{/i}, Alexia!"
        al "R-rowan-"
        ro "Don’t you dare give up on me now, not after everything we’ve gone through. We’re going to get through this. {i}Together{/i}."
        "She didn’t know how to respond. Tears filled her eyes. Alexia embraced him, and Rowan did the same. They clung to one another like survivors in a storm."
        "Nearly an hour passed. The sun sank beneath the horizon, filling the world with effervescent gloom. Alexia sat next to him, staring into the distance with that long-eyed look again." 
        "They hadn’t said anything to each other in all that time. Something was weighing on her thoughts. At last, she turned to look at him."
        al "...Rowan."
        al "You don’t know how much you mean to me."
        "He felt her arms go around him, her body sidling close as he kept his gaze trained towards the blue mountains in the distance."
        al "I… I want to be with you. Tonight. In your bed. As husband and wife."
        
        menu:
            "Kiss her.":
                $ released_fix_rollback()
                "How could he ever say no to her? As the sun sank into darkness Rowan captured her lips with a kiss."
                "So much had changed about them and their relationship, yet this singular experience was the same as it had been on their wedding day." 
                "She pulled close, holding him tight as if frightened that he would leave. But Rowan wouldn’t do that, he couldn’t. Perhaps he was doomed, perhaps they both were."
                "But for Alexia’s sake, he was willing to risk the void."
                jump conorSexScene
                
            "Beg off.":
                $ released_fix_rollback()
                "Rowan was more tired than he thought. The mental exhaustion of the day and the week preceding it had taken so much from him. The last thing on his mind was sex."
                ro "I’m sorry Alexia, there’s just… a lot on my mind right now."
                "Alexia’s crestfallen face almost made him reconsider, but her gaze hardened as she nodded earnestly at him."
                al "I understand. It was… a selfish thought of mine."
                al "I’ve been having more and more of those, of late."
                al "Would it… is it okay if I was selfish in a different way then?"
                al "Could we just... stay here for a little longer like this?"
                "Rowan smiled, wrapping his arm around her shoulder. She got close to him and snuggled against his chest. He kissed the top of her head."
                ro "Of course my love."
                "They sat there together, staring at the ever-changing orbit of stars. Time ceased to have any meaning as the world seemed to go by in an ever changing cycle."
                $ change_relation('alexia', 5)
                return
    else:
        "She didn’t even bother to look at him. Alexia closed her eyes, letting out a long sigh."
        al "...Yes. I’m fine. I’m just tired."
        ro "It’s been a long day for both of us, I think."
        al "So it has."
        "An awkward silence fell. It was painful to see just how disconnected they’d become from one another."
        "There were a hundred things he wished he could tell her, to confide in her, but the words wouldn’t come. Rowan no longer knew how to cross that unbridgeable gulf."
        ro "I’m doing the best that I can, Alexia."
        "Alexia snorted. Her empty eyes turned to look at him in the growing dark."
        al "In the end, what does it really matter? You play out your little act, and the Twins do what they will regardless."
        ro "I can’t control their impulses. The best that I can do for now is to try to diminish the scale of their atrocities."
        al "Hm."
        al "And how is that going for you?"
        "Rowan had to bite his tongue not snap back with an angry retort. Alexia’s expression softened. She looked away."
        al "I wish I could be as strong as you are, Rowan. I admire you for keeping up with the fantasy, no matter how often reality stares you in the face."
        al "It was… nice while it lasted, our life in Arthdale."
        al "What a pleasant dream it was too: the nobody girl from a nowhere place, falling in love with the hero of the Six Realms."
        al "...None of it ever really meant anything, did it?"
        
        menu:
            "I still love you, Alexia.":
                $ released_fix_rollback()
                "Alexia giggled. She seemed more amused than impressed by his earnest proclamation."
                al "You always knew how to make me smile, Rowan."
                al "I don’t know how much you really believe what you’re saying to me... but I appreciate the thought."
                ro "What will it take to convince you?"
                al "I don’t know. I’m even sure that I {i}know{/i} what I want, anymore."
                al "You don’t need to try so hard, Rowan"
                
            "It meant something to me.":
                $ released_fix_rollback()
                "She let out a frustrated sigh. Her eyes opened, and she looked at him with something approaching pity."
                al "I’d like to think it meant something to me, as well."
                al "But words are empty comforts now. Maybe we could have had a happy life together, had we stayed in Arthdale."
                al "-Or maybe it was always going to end up this way, and the Twins’ intervention just sped up the process."
                ro "I had nothing but good intentions when I first married you, Alexia."
                "She smiled at him, but the warmth did not enter her eyes."
                al "Maybe. But ‘good intentions’ aren’t the same thing as love."
                ro "I do love you."
                al "And I want to believe you."
                
            "Say nothing.":
                $ released_fix_rollback()
                "Rowan didn’t know how to respond. He didn’t even know what it was he was feeling. There was a numbness to his thoughts, as if his whole world were just shades of intermittent grey."
                "Alexia turned away from him again, staring with a wistful expression towards the sunset."
                al "...Perhaps it’s easier this way. Better to live with the painful truth than a fanciful illusion."
                al " It’s not like anything will change either way."
                
        "Alexia hopped off the crenellation, landing smoothly on the cold stone of the castle wall. She turned away towards the stairs, walking with calm steps towards the staircase."
        "She turned back to look at Rowan. The wind blew a gentle gust across her face, ruffling her hair. She smiled at him, that gentle curve of the lips she had once reserved only for him."
        "Here though, it almost felt like a mournful goodbye."
        al "Thanks for being here, Rowan. For what it’s worth: you were always a great listener."
        hide alexia with moveoutright
        "Rowan watched her descend the steps to the ground like a man witnessing an execution. He stayed there on the wall, staring at the horizon till night fell and the world around was covered in darkness."
        "It matched his bleak outlook for the future."
        return


label conorLowCorEnd:

"After the tears had dried, the couple sat together and watched the sunset. More than an hour passed as they waited in silence, the brooding purples giving way to the wintry passage of the stars across the darkening sky."
"Rowan felt Alexia’s fingers interlace with his own, and she rested her head on his shoulder."

al "Rowan."
al "I... don’t want to be alone tonight."

menu:
    "Kiss her.":
        $ released_fix_rollback()
        "Gently, Rowan tilted her head to face him. Her emerald eyes glimmered back at him in the starlight. Tears still glistened in the corners."
        "He leaned down and captured his lips with her own. She sighed into his mouth, melding against his body with a sense of utter peace and contentment."
        ro "...You don’t have to be."
        jump conorSexScene
        
    "Let’s watch the stars a little while longer.":
        $ released_fix_rollback()
        "She giggled, tilting her head skyward and rubbing at her eyes."
        al "Not the worst way to get shut down, I suppose."
        ro "It’s not that, Alexia. It’s just- "
        ro "Sometimes… being near you is enough."
        "She giggled again."
        al "You silly romantic."
        "For all her teasing, she didn’t seem to mind. Alexia cuddled up against him and stared at the horizon, the warmth of her body bringing a small glow to his chest."
        "They sat there together, hand in hand, husband and wife, watching the stars go by into infinity. It would be hours yet before they went inside."
        $ change_relation('alexia', 5)
        return


label conorSexScene:

scene bg9 with fade

if all_actors["alexia"].corruption < 31:
    "Rowan took her by the hand. She smiled at him and squeezed it. He led her down the long walk to his bedroom, heedless of anyone who passed. He only had eyes for her." 
    "Alexia never wavered, never faltered or hesitated. She trusted him completely. Rowan could not put into words what that faithful love meant to him. It was the only thing that kept him going."
    "At last they reached their destination. Alexia entered first, her footsteps light and breezy as she swept into his bedroom. Rowan closed the door behind him and turned to face her."
    "There she was, the picture of feminine beauty, standing before him. Her eyes beckoned him onwards, a subtle promise of forbidden pleasures." 
    "She smiled at him, a shy, delicate thing. It never failed to amaze Rowan just how strong she was. Despite everything, she was still the gentle, loving woman she’d been back in Arthdale. Not even the Twins could steal her innocence."
    "Rowan embraced her, their lips forming a connection that went beyond mere physical attraction. Her lips brushed his, softly, delicately, like butterfly wings, just long enough that he could inhale her breath, feel the warmth of her skin."
    "They peeled the clothing off of one another, mere trappings that concealed their true selves. There were to be no secrets between them. Soon they were naked, standing together like ghostly spirits beneath the light of the stars coming from the window."
    "She was enchanting: pale white skin topped with a shock of fiery red hair, with warm green eyes that glimmered in the dark. She drove him wild."

elif all_actors["alexia"].corruption > 60:
    "Rowan took her by the hand. She looked up at him, her uncertain expression filled with pain and regret. Rowan could not look her directly in the eye as he led her down the long walk to his bedroom."
    "But Alexia’s footsteps were slow and hesitant to follow. It was as if she did not seem to trust herself. It hurt Rowan to see how much their trust had been damaged - even if it was only temporary."
    "...Rowan could only hope that it was temporary."
    "He led the way, his body tense, his footsteps stilted and mechanical. Alexia followed behind him, quiet and forlorn. When they at last reached their destination, Rowan let her walk inside herself, then shut the door behind them."
    "Rowan turned to face her, staring at her features like an artist appraising a work of his he had not seen in years. There she was, the picture of feminine beauty, the woman he loved. Alexia."
    "Why couldn’t he recognize her?"
    "Her eyes might have been hesitant, but her body was not. She walked into his arms, planting them firmly around her waist as she leaned hard into his face."
    "Her lips mashed against his, as if trying to flatten and destroy his mouth. Her mouth opened, tongue pushing past his clenched teeth to the moist space within."
    "She worked her mouth against his, their tongues battling back and forth like wrestlers, each trying to pin the other. Rowan didn’t know how their little, loving game had warped so suddenly into a vicious competition." 
    "They peeled off their clothing in a rush, discarding it in a useless heap on the floor. She was enchanting: pale white skin topped with a shock of fiery red hair. She drove him wild, she was a hellion who all but threw herself at him. "
    "Her body moved with a sensual bend all its own, accentuating her curves. She had an almost preternatural ability to arouse him, a fact driven home as she reached down to roughly grope his hardening erection."

else:
    "Rowan took her by the hand. She smiled at him and squeezed it. He led her down the long walk to his bedroom, heedless of anyone who passed. He only had eyes for her."
    "But Alexia’s footsteps were slow and hesitant to follow. It was as if she did not seem to trust herself. It hurt Rowan to see how much her own self-image had been damaged. It was as if she didn’t even trust herself anymore."
    "When they at last reached their destination, Rowan led the way into the room. Alexia followed behind, her fingers interlocked tight with his own as if to cling to his strength. The door closed behind them and Rowan turned to face her."
    "There she was, standing before him. The picture of feminine beauty. It was a shame that her eyes were uncertain pools of distress, unable to look him directly in the eye." 
    "There was a depth to her features that she have never worn before. He couldn’t tell if she wanted to kiss him, or break down into tears… maybe it was both?"
    "Alexia did her best to smile. But it was strained, her body language was that of helpless indecision. It was as if she didn’t really believe she deserved to be in his presence."
    "Rowan’s heart ached. How could he explain to her how much she mattered to him? The Hero of Rosaria would give up the whole world - the Gods, the afterlife and everything else - just to see her true smile again."
    "He kissed her like she wanted to be kissed, soft and moist and hot and fierce. The heat rose in her cheeks as her tongue touched his own, quick and electric and delicious." 
    "They intertwined in passionate revery, seeking to chase down that elusive feeling that had first brought them together.He had to show her. He had to show her how much she meant to him."
    "They peeled off their clothing, discarding it in a heap on the floor. She was enchanting: pale white skin topped with a shock of fiery red hair. She drove him wild."

#cg1
scene cg746 with fade
show alexia necklace naked aroused behind cg746
show rowan necklace naked aroused behind cg746
pause 3

"Breathless, she took his face in hand, staring deep into his eyes with an expression of heated arousal."

al "Here Rowan, let me…"

"Her fingers clenched against his chest, a silent entreaty for him to comply. She pushed him, a gentle nudge to get him moving. Rowan backpedaled to the foot of the bed. His ankles caught the mattress, and he sat down."

"Alexia knelt in the space between his legs, settling into place with her knees together, like a nun at her prayers. Rowan watched the curve of her spine as she leaned towards, her face hovering near his groin."
"She took his stiffening cock in hand, stroking it in long, slow motions. She watched his reaction as her head bent down and she took him in her mouth."

ro "A-alexia…"

if all_actors["alexia"].corruption < 31:
    "Alexia paused in her sensual movements, her eyes flicking up to look at him with the head of his cock between her lips. There was an innocent expression on her face, she almost seemed to be asking him: {i}“is it okay?”{/i}"
    "Rowan felt a swelling in his heart… one to match the swelling of his groin. Gods, he loved this woman. Even in her most awkward moments, she was adorable."
    "He ran his fingers through her hair and nodded, letting out a soft moan of encouragement. Alexia, emboldened, bent herself to the task, kissing and licking his cock before taking it once more in her mouth."
    "She moved slowly, lifting and lowering her head in gentle strokes, her eyes fixed to Rowan’s face. Her lips quirked up into a smile when she saw him stare back, and a fresh wave of arousal shot up the back of his spine."
    "She was perfect. There was a wordless symmetry between them, a pure-hearted comprehension of their partner’s needs that even something so simple as this became a heated encounter." 
    "Alexia stroked him slowly, bobbing her head up and down, up and down in careful movements. Rowan felt goose bumps roll up his thighs as her fingernails dragged a gentle line across his sensitive skin."
    "Her lips puckered, and she sucked down as far as she could, roughly halfway down his length. It was more than enough, his breath caught in his throat as he felt that warm, wet place settle around it with pleasing tension."
    "In a rush he felt his stomach tighten. Rowan let out a tortured grunt of pleasure and put his hands on her shoulders, his fingers clenching as he did everything in his power to hold back from orgasm."
    "She was too much, he couldn’t hold back against her."
    "He pulled her off of him, breathless, his heart hammering in his chest. Alexia stared back at him, wordless, her eyes smouldering with the kind of aching need peculiar to one in the throes of passionate love."
    "She wanted him. She wanted her mate. And Rowan wanted her, more than anything."
    ro "Alexia… get on the bed."
    "Alexia smiled. She nodded, rising up to crawl onto the bed next to him. She was already wet, but she took the time to hug him close, planting a gentle kiss on his lips."
    al "I love you, Rowan."
    
elif all_actors["alexia"].corruption > 60:
    "She did not hesitate. In the space of a breath she was already bumping her nose against the base of his groin. Rowan let in a startled gasp as his wife began an immediate, intense deepthroat session."
    "There was no subtlety in her actions, no blushing vacillation or chaste misgivings. She took to sucking him off with the ardour of a specialty whore plying her trade. In seconds she was bobbing up and down, asserting his crotch as her own personal living space."
    "Her hands interlaced around his waist, pulling her still closer, still deeper into the oral embrace. Rowan couldn’t even see her face anymore, only the back of her head and the flash of red hair as she bobbed up and down in a merciless, pounding rhythm."
    "Rowan marveled at the sight of his wife’s face buried in his groin. She was so confident, so sure of her movements, a femme fatale with no qualms or concerns about pleasing her man to the fullest."
    "How much had changed since those blushing days in the aftermath of their wedding, when she had seemed almost bashful at the sight of his nakedness. Rowan had once joked that she was the most bashful woman in all of the Six Realms."
    "...But {i}now{/i} look at her. How much time and the events of their lives had changed them. It was almost startling how confident she’d become."
    "As if sensing his surprise, Alexia lifted her head, allowing her lips to drag upwards in a single, long, languid motion. His dick pulled free from her lips like a sword emerging from its sheath, the tip catching at the end as she suckled on the cockhead for a moment before letting it pop noisily from her lips."
    "Alexia cast a naughty eye in his direction, her eyes aflame with the heat of the moment. In a rush he felt his stomach tighten."
    "It was everything Rowan could do to plant his hands upon her shoulders to keep her at bay. If he let her continue, he’d blow his load straight down her throat without so much as a hint of foreplay on her end."
    "He pulled her off of him, breathless, his heart hammering in his chest. Alexia stared back at him, wordless, her eyes smouldering with horny need. She wanted him to {i}fuck{/i} her. And Rowan would give it to her."
    ro "Alexia… get on the bed."
    "She giggled at his assertiveness, hiding her lustful with a coquettish turn of the hand."
    al "Why, whatever for, husband of mine?"
    "She stood up in front of him, tilting her hips so Rowan could see the full effect of her efforts to him. She was practically drooling down there. With a smirk and an unsubtle purr she clambered into bed next to him."

else:
    "She let out a tiny {i}hum{/i}, acknowledging his response with quiet passion. Determined, she pushed forward, her mouth engulfing his cockhead as her tongue worked in small circles against its underside." 
    "There was little Rowan could do but settle in and endure it. Rowan leaned back on his hands, watching in silence as Alexia lifted and lowered her head on his dick. Her ardent efforts earned her a moan, and Rowan closed his eyes."
    ro "Gods, you’re amazing Alexia."
    "She {i}hummed{/i} again, this time causing sensual vibrations to run down the length of his engorged cock. Rowan groaned, putting his hand on the back of her head to guide her deeper."
    "She obliged him, going far deeper than before to take as much of his length down her throat as she could. There was a determined look in her eye, an erotic intensity that simmered just under the surface. It almost felt like she was holding herself back."
    "Her mouth pulled free of him with a pop, letting out a short gasp of air. Alexia leaned forward, planting her chin on his groin, lifting his cock vertically so as to run parallel to her face. She slapped it against her cheek, a dangerous little smile growing across her face."
    "Rowan chuckled, his voice deepening with sexual arousal. She began to stroke him, the glistening lubricant she’d left behind aiding in her endeavour as Alexia took him once more in her mouth."
    "She was perfect. There was a wordless splendor in the way she moved, the way she looked at him. Alexia inflamed his senses in a way that no one else could, she… {i}completed{/i} him."
    "All romantic notions fled from Rowan’s head when she shoved herself down as far as she could on his cock, taking almost the whole of him in her mouth. He felt his breath steal away from him as he found himself lodged in that wonderful, warm place in the pit of her throat."
    "In a rush he felt his stomach tighten. Rowan let out a tortured grunt of pleasure and put his hands on her shoulders, his fingers clenching as he did everything in his power to hold back from orgasm."
    "She was too much, he couldn’t hold back against her."
    "He pulled her off of him, breathless, his heart hammering in his chest. Alexia stared back at him, wordless, her eyes smouldering with the kind of aching need peculiar to one in the throes of intense passion."
    "She wanted him. And Rowan wanted her, more than anything."
    ro "Alexia… get on the bed."
    "Her lips spread wide into a deep, sexual smile. She nodded, rising up to crawl onto the bed next to him. She was already sopping wet down there. Her voice was soft and submissive as she spoke."
    al "As you wish, Rowan."

ro "Alexia…"

"His fevered whisper in her ear was heated, full of longing. She was everything he’d ever wanted in a woman. It was almost painful to look at her."
"He kissed her neck, his hands molesting her body with almost manic ardour. He caressed her breasts, his fingers finding lodging around the firm buds of her nipples."
"He leaned down and kissed one of them. Alexia let out a sharp gasp, her fingers curling though his hair as she held his head hard against her."

if all_actors["alexia"].corruption < 31:
    al "Take me, Rowan…"
    "Her voice was silent, barely a whisper. He was all but compelled to grant her deepest desire."
    
elif all_actors["alexia"].corruption > 60:
    "Alexia licked her lips like a greedy glutton appraising a meal. She yanked his mouth against his, exploring his mouth with the taste of him still on her tongue."
    "He pulled away gasping, empty of breath. She let out a hellcat’s growl."
    al "Make me {i}scream{/i}, you fucking beast."

else:
    al "Fuck me, Rowan…"
    "Her voice was randy, her tone seductive. She had progressed beyond mere ‘affection’ into outright horniness."

scene cg747 with fade
show alexia necklace naked aroused behind cg747
show rowan necklace naked aroused behind cg747
pause 3

"Rowan moved to climb on top of her, but she put a hand against his bare, sweaty chest."

al "No… allow me."

"He fell back against the covers, watching with a dry tongue as this figure of feminine beauty clambered on top of him, straddling him with her waist and ample ass."
"Her hand went inexorably to his wettened cock, angling it upward like a stabbing spear. She rolled her hips against him several times, allowing him to feel the maddening promise of her wet interior."
"Then, she lifted her hips. Alexia pointed his dick in a perfect angle. He was aligned. There was nothing left to do but inhale and gird himself for the imminent plunge."

scene cg749 with fade
show alexia necklace naked aroused behind cg749
show rowan necklace naked aroused behind cg749
pause 3

"She lowered herself down. Rowan felt the tight, clinging warmth of her pussy clamping down on him. And just like that, they were making love."

if all_actors["alexia"].corruption < 31:
    "Rowan’s hands found her hips as Alexia moved in slow, rolling motions above him. They took it slow, reveling in the simple joy of one another’s company."
    "Alexia let out a deep sigh, as if the act of sex itself were removing months of care and worry from her body."
    "...Perhaps it was. She seemed lighter now than she’d been just hours earlier. There was a simple grace to her movements, a carefree pleasure as she bounced atop Rowan."
    al "Oh Gods, Rowan you feel so {i}good{/i}…"
    "They picked up the pace, the gentle lovemaking proceeding into a faster, more intense fuck. Alexia gasped in tune to his thrusts, and Rowan let out grunts of pleasure."
    scene roxal_batt_sex2 with fade
    pause 3
    "Overcome with emotion, Rowan sat up, wrapping his arms around his beloved wife and holding her close. She giggled and reciprocated the gesture, leaning into a deep kiss."
    "She was his everything. He lived for these moments. Rowan thrust hard against Alexia’s flank, the delightful jiggle of her bottom slapping against his hips only spurring him on more."
    show cg764 with sshake
    show cg764 with sshake
    pause 1
    show cg765 with flash
    pause 2
    show cg766 with fade
    pause 3
    "She began to let out short, sharp yelps of pleasure, their bodies kicking into overdrive as they neared their mutual climax." 
    "Rowan groaned as he reached his limit, clinging tightly to her as his wife let loose a cry of joy and came."
    "Her pussy clenched, causing Rowan to erupt. He let out heavy exhales from his nose as his cock thickened, pulsed, and came."

elif all_actors["alexia"].corruption > 60:
    "Though, that was a charitable term. In reality, Alexia made little pretense of  romantic trivialities. There was no time for it: for she had fucking to do." 
    "Her hips smacked hard against Rowan’s own in a rough staccato as she made a mess atop him. The loud schlick of her wet hole devouring his cock in an up-down, up-down motion became a near blur."
    "She was insatiable, humping atop him with the practiced ease of one well suited to the sexual arts. She was a whore in all but name, battering Rowan back against the bed as she held fast to his shoulders."
    al "Ah! Ah! Ah! {i}Aaaah{/i}!"
    "Her loud cries of pleasure were ecstatic and unrestrained. Alexia allowed her facial expression to blossom into that of pure bliss, her eyes lidding as she bit her lip."
    al "{i}Mmmm{/i}, yeah, come on Rowan. {i}Fuck me{/i}!"
    "Rowan did his best to keep up, but in truth he was just along for the ride. Alexia was beyond anything he was used to. She was hornier than a Goblin in heat, more depraved than a Demon with a love fetish."
    "He had never seen her like this before. She was beyond anything that his mind could coherently compare to. They weren’t having just sex, they were {i}mating{/i} like animals, and she was the conquering lioness."
    scene roxal_batt_sex2 with fade
    pause 3
    "Alexia fell atop him, her fingernails scratching long lines down his back as she clung fast. Rowan let out a snarl of half-pain, half-pleasure as he felt her scorching fingernails dig furrows into his skin."
    "Alexia, heedless, redoubled her efforts against him. Her ass slapped hard down against his groin, rolling in hard circles, working him in and around her deepest places. She seemed intent upon introducing him to every nook and cranny of her packed pussy."
    "Rowan groaned, overwhelmed by her unrelenting assault. Rowan had been expecting tender lovemaking, but instead had found conditions more akin to a battlefield. Every inch - {i}quite literally{/i} - was being fought over."
    "He bucked and thrusted as best as he could, but Alexia was on another level entirely, all but pounding him into the bed as she worked a heated lather against his overworked groin."
    "She gasped and cried and came more times than he could count, arriving at a state somewhere between ecstasy and tranquility. For Rowan, it was everything he could do to hold fast to her hips and cling for dear life."
    show cg764 with sshake
    show cg764 with sshake
    pause 1
    show cg765 with flash
    pause 2
    show cg766 with fade
    pause 3
    "Finally, the penultimate moment arrived. Alexia’s spine trembled, her body going rigid as her claws dug hard into his shoulderblades." 
    "She screamed his name in a single, incoherent cry of joy in the same moment his cock thickened and came."
    "Rowan erupted, his balls draining in a massive orgasm that made him lightheaded from the sheer force of it." 
    "He gasped and panted, pulsing jets of cum into her love tunnel with every inhale. His heart was in his throat, his head was in the clouds and his cock was balls-deep within her."

else:
    "Or… “fucking,” as the case may be. Alexia wasted little time in preemption. Her hips began a heavy tempo that drove Rowan back into the bedsheets." 
    "Content that she had Rowan right where she wanted him, she planted her palms down upon his pectorals and adjusted her weight, allowing an ideal penetration for a minimum of effort."
    "With everything in place, she began to move, bouncing up and down in sudden, sharp gales that only receded once her breathing shortened."
    "She fucked him hard against the mattress, planting her hips down onto his and rolling back and forth, allowing him to feel every inch of her interior before rising once more to expose his wet cock to the glistening air."
    "She repeated this process over and over, changing the speed and vigor of her strokes to ensure that he never grew too comfortable with the sex."
    "She’d gotten damn good at this, that much was for certain. Compared to their quiet, romantic evenings on lazy summer afternoons in Arthdale this was a whirlwind."
    "Alexia took Rowan’s hands and guided them to her ample ass, gasping in pleasure when he kneaded her cheeks and planted a light spank on her rump."
    al "{i}Harder{/i}."
    scene roxal_batt_sex2 with fade
    pause 3
    "Her hands then guided him towards her clit as she picked up the pace. Rowan shot her a surprised look, but Alexia merely quirked a naughty eyebrow."
    "Rowan rubbed her there, his thumb working the clit as she now rode him like a stallion."
    "She laughed and cried out, her body tensing every so often with tiny little orgasms that made her shiver with dirty pleasure."
    "Rowan bit his lip and moaned, unable to contain the rush of sensation radiating from his cock at the hands of his wife’s unsubtle attentions."
    "He began to thrust back at her, his hips working like a pivot point against her own as they pulled back, then met in the middle. Over and over and over until-"
    show cg764 with sshake
    show cg764 with sshake
    pause 1
    show cg765 with flash
    pause 2
    show cg766 with fade
    pause 3
    show alexia necklace naked aroused behind cg766
    al "Oh! Ah! {i}O-ooooooh{/i}!"
    "Her pleasured cry became a banshee’s scream as Alexia went rigid. Her pussy clamped down tight on Rowan’s dick as it milked him of his very essence."
    "Rowan tried to resist as long as he could, but it was a lost cause. With a roar of masculine conquest he thrust into her deepest place, planting his seed deep within her as his cock pulsed and spurted inside her. "

scene bg9 with fade
show rowan necklace naked at midleft with dissolve
show alexia necklace naked aroused at midright with dissolve

"Rowan fell back against the bed, unable to catch his breath. His eyes danced circles in his head, and his body thrummed with the masculine sensation of completion." 
"He felt a wave of relief pass over his body. He looked into Alexia’s eyes and, still inside her, planted a gentle kiss onto her lips."

ro "Solansia preserved me, that was… wonderful."

"Alexia let out a chuckle, her finger tracing small circles on his chest. She looked almost shy in the aftermath, as if the intensity of the sex had forced all her assertiveness out of her."

al "I’m… glad you enjoyed it."

"She rolled off of him, settling happily against his side as Rowan put the back of his arm against his forehead. He still couldn’t quite process what had just happened." 
"Rowan turned to look at her, noticing with a twinge in his chest that despite her happy words, her facial expression was once more troubled."

ro "Alexia did you… not enjoy it?"

if all_actors["alexia"].corruption < 31:
    al "Of course I did, love. That’s not the problem. It’s…"
    ro "Conor."
    
elif all_actors["alexia"].corruption > 60:
    al "N-no! Of course not! You were... great."
    al "I’ve just got a lot on my mind."
    ro "Thinking about Conor?"
    if conorJob == "kitchens":
        "Alexia’s expression hardened. Rowan saw the distant look in her eyes, reflected in the dim starlight flowing into the room."
        al "He’s working in the castle now, it's very likely that we’ll bump into each other at some point."
        al "I don’t know if I have the courage to face him, Rowan. To look him in the eyes and-"
    else:
        "Alexia’s face fell. There was a pain in her expression, one she could not dispel with a simple night of passion."
        al "He’s… I’m never going to see him again."
        al "Of course, maybe I {i}never{/i} was. But… knowing what’s happened to him..."
    
else:
    "Alexia let out a soft sigh. But when she turned to him, she was smiling. She ran her fingers gently across Rowan’s cheek."
    al "You were wonderful, love. It’s... not you."
    ro "You were thinking about Conor."
    
ro "We can only take things one day at a time, Alexia."    

"Rowan would have given anything in that moment to find a way to heal the hurt in Alexia’s eyes when he said that. She rolled to face him, huddling up against his warmth as she wrapped her arms around him and settled her head in his chest."

al "Why does every day seem to get worse, Rowan?"

"Rowan didn’t have an answer for her. He could only pull her close and hope that she felt a modicum of comfort from his presence." 
"The Hero of Rosaria might not have been able to save his village, or his kingdom, or his friends and loved ones."
"...But at least he could try to keep this delicate thing in his arms safe. For a little while. Just for a little while, at least."

$ change_relation('alexia', 10)
return


############################################################################
############################################################################
############################################################################

label why_karnas_failed:

scene bg14 with fade
show xzaratl neutral at midleft with dissolve
show skordred angry at midright with dissolve

xz "You’re taking this altogether too personally, Skordred."

sk "Oh aye? You think so, ya indolent sloth?"
sk "Nine years Karnas warred against the combined armies of tha Six Realms, fightin’ tooth and nail fer the glory of Kharos."
sk "And where were ye? A mighty sorceress who mighta turned tha tide o’ his great and noble conquest?"
sk "Ya skulked about like a viper in a rats nest, playing matchmaker with mortals while tha Herald of Kharos himself fought against the might of all creation."

xz "As I’ve told you before dearest Skordred: the Demon Wars were none of my concern."

show skordred neutral at midright with dissolve

sk "How can ya say that? You, a full blooded demon?"

xz "Kharos’ will flows in countless contradictory directions. The Demon Lords and their conflicts are but one aspect of his ambitions."
xz "Hehe… just as I am but another!"

sk "T’was fickle fools like ye what caused his downfall. Imagine what Karnas coulda accomplished with yar help! You and all tha other brittle backbones who abandoned him!"

#skor sad

sk "Karnas was the mightest Demon Lord who ever was, or ever shall be."

show skordred angry at midright with dissolve

sk "He burned the moving city of Frae’Volaith in Eaolen Forest, he smashed an army {i}twenty{/i} times tha size o’ his own at the Battle of Deadman’s Pass. He raised the bloody banner of Kharos before tha very gates of Prothea itself!"


xz "And where is mighty Karnas now, Skordred?"

#skordred shocked
show skordred angry at midright with dissolve

"It was such a simple question, spoken without malice, but it left the Dwarf aghast."

sk "Y-you dare to mock tha greatest Demon Lord that ever was?"

xz " I do. And there’s nothing he can do about it."
xz "Because he is dead, and I am not. That is the clearest answer I can give. "

show rowan necklace neutral at edgeleft with moveinleft

ro "What are you two arguing about?"

show skordred angry at midright with dissolve

sk "This mad witch thinks joining Karnas’ war was a waste o’ time. She stayed on the sidelines while tha fate of Solanse was at stake!"

show rowan necklace shock at edgeleft with dissolve

ro "...Wait, you didn’t fight in the last Demon War?"

xz "Come now Rowan, do you really take me to be the kind of person who is interested in petty conquest?"

sk "Nah, he just dinnae take ya fer a {i}coward{/i}. "

show rowan necklace concerned at edgeleft with dissolve
#xzaratl annoyed

"X’Zaratl’s eyes narrowed. A sudden, murderous electricity filled the room. Rowan felt the hair on the back of his neck stand on end. His hand went instinctively to the hilt of his sword. "
"But just as quickly as it came, the shadow over X’Zaratl’s eyes had passed."

#xz neutral

xz "Silly Dwarf. Only a fool joins a cause she knows is doomed from the start."
xz "Your master made the same mistake that every Demon Lord has done before him: he let his hubris override his common sense."
xz "Karnas fought the war according to rules the Solansians invented. They wanted a grand enemy to struggle against, a mighty foe worthy of song to unite the realms against, and he gave them one."
xz "A Demon Lord has so few friends already, yet Karnas did not adapt his strategy to counter that of his foes. He played into it. "
xz "That is not the mark of a true minion of Chaos. He was never going to win, it was obvious from the onset. What did I stand to gain from joining him?"

sk "Only tha final victory of Chaos. The reforging of this pox-ridden reality into a realm ruled by tha {i}true{/i} servants of Kharos."

xz "Such a delightful image! But a dead dream in the hands of your fallen master."

sk "Tha’s lead boulders and ya know it! Rowan, you know tha truth of things."
sk "Was Karnas not a mighty foe? Could anyone have bested him had all tha servants of Kharos rallied to his banner?"

"Not wishing to be drawn into their heated quarrel, Rowan did his best to dodge the question."

ro "It has been a long time since I last thought about the war."

sk "ye, but it was yer crownin’ moment, as much as it was mine. Why do you think he lost?"

menu:
    "Karnas underestimated his enemies.":
        $ released_fix_rollback()
        show rowan necklace neutral at edgeleft with dissolve
        ro "...Karnas had both the talent and capability of conquering Solanse."
        sk "Har! Ya see X’Zaratl? Even his greatest foes knew his strength!"
        show rowan necklace angry at edgeleft with dissolve
        ro "...But he utterly miscalculated the kind of sacrifices Solansians were willing to make to stop him."
        show rowan necklace neutral at edgeleft with dissolve
        ro "The crushing victories Karnas won early in the war only made him arrogant. He assumed we were too weak, too close minded to adapt."
        ro "He never really recovered from that self-assured delusion."
        ro "He got sloppy, and once Deanara took command of the war effort, it was too late to recover."
        xz "Pride is a deadly disease, one the Twins should take care to avoid if they wish to learn from their father’s mistakes."
        
    "Demons by their very nature cannot win.":
        $ released_fix_rollback()
        ro "Karnas lost not because of what he did, but because of who he was."
        #xzaratl annoyed
        ro "A Demon - for all its strength - is a predictable enemy."
        ro "When he came to Solanse, Karnas’ armies were legion, his power overwhelming."
        ro "...At least at first. But an army of Chaos is temperamentally incapable of maintaining cohesion for long."
        ro "Once the initial shock of the invasion had passed, it was just a matter of buying enough time for his army to fracture."
        xz "{i}Hmph{/i}, I hardly think that’s a fair assessment of Demons, Rowan. My kin can be quite dangerous."
        ro "I didn’t say Demons weren’t dangerous, X’Zaratl. I said they were predictable. And in war, predictability is death."
        ro "Karnas was doomed from the moment he set foot onto Solanse. A Demon Lord could never hope to adapt to new circumstances the way a mortal can."
        xz "A shame then, that Kharos has never deigned to make a mortal his champion."
        
    "Karnas was a bad leader.":
        $ released_fix_rollback()
        ro "Karnas was a mighty Demon Lord, but an incompetent leader."
        sk "How can ya possibly say that? He came {i}this{/i} close to smashing tha Six Realms to pieces!"
        ro "He really didn’t. Karnas had a massive handicap at the start of the war: he spent {i}years{/i} building up his forces, and the Solansians were divided in their initial response."
        ro "He ignored the growing power of his enemies and permitted too much dissension in his own ranks. I can't tell you how many detachments we encircled in our march on Bloodmeen alone, all because Karnas couldn’t keep his soldiers in line. "
        sk "Ya have no idea what yar talkin’ about, lad. Karnas was betrayed by grifters and weak-kneed sellouts. Every battle we won in that war was ‘cause of his genius."
        ro "Karnas had a certain, low cunning, I’ll give you that. It was how he managed to catch the Rosarian Thorns off guard at Deadman’s pass."
        ro "But Karnas was a warlord, not a strategist. Strength was all that mattered to him."
        xz "Like father, like son it would seem."
        ro "Karnas’ leadership ensured obedience when he was winning, and faithlessness when he suffered setbacks."
        ro "Greed may buy men’s hearts for a time, but he failed to instill the kind of loyalty that would have won him the war."
        sk "Ha! Ya know nothing about what yar talkin’ about. I’m livin’ proof of the lie of yar words."
        ro "I’m sorry to say Skordred, but you’re mistaken. You’re the exception that proves the rule."
        
    "Chaos could not form a united front.":
        $ released_fix_rollback()
        ro "Karnas came closer than any Demon Lord in history to conquering the Six Realms. Had he managed to pull some of the other chaotic races into his coalition, maybe he would have succeeded."
        sk "When Karnas first revealed himself, he sent emissaries to all tha great races touched by Kharos."
        sk "They refused his generous offer. Ya cannot blame him fer the foolishness of his allies."
        ro "-His ‘generous’ demand for submission, you mean. Demon Lords don’t make alliances, Skordred. And that’s precisely my point."
        ro "The Orcish tribes of the south, the Goblin tribes of Rosaria, the Dark Elves of the Bloody Spines, {i}all{/i} of them failed to rally to his banner."
        ro "Added together, they likely outnumbered the whole of the armies of the Solansian nations. And they could attack us almost anywhere."
        ro "But Karnas was so high-handed with his potential allies that he alienated most of them. So while the Six Realms rallied and were united in purpose, our enemies remained fragmented."
        xz "A Demon Lord would sooner lose his head than recognize another as his equal."
        ro "That failure to humble himself is what doomed his cause."
        ro "The chaotic races took advantage of the war to settle local scores with their enemies, but they never coordinated with Karnas himself."
        ro "And now look at their situation."
        
    "The Six Heroes defeated Karnas.":
        $ released_fix_rollback()
        ro "Karnas could never have won the war, but it wasn’t for lack of talent. Had it been any other era in history, I don’t think the Six Realms could have withstood him."
        ro "-But he was facing the combined might of the Six Heroes. The greatest spellcasters, generals, warriors and champions the Realms had ever seen."
        "X’Zaratl let out a teasing giggle."
        xz "...Including you, Rowan!"
        if avatar.corruption < 31:
            show rowan necklace concerned at edgeleft with dissolve
            ro "Trust me: I was the least of them by far."
        else:
            show rowan necklace happy at edgeleft with dissolve
            ro "Yes. Including me. Why else do you think the Twins went to such great lengths to recruit me?"
        show rowan necklace neutral at edgeleft with dissolve
        ro "Deanara alone might have been enough to doom the Demon Lord."
        ro " I was there at the Battle of the Burning Pit, when she turned an army of frightened conscripts into a golden legion that would have made Kharos himself tremble on his morphing throne."
        ro "I still dream about that final charge across the open field, strewn with flickering blue balefire. "
        #skor sad
        show skordred neutral at midright with dissolve
        ro "We slaughtered the last of Karnas’ Chaos Dragons like it was a stag hunt."

    "I won the war.":
        $ released_fix_rollback()
        show rowan necklace happy at edgeleft with dissolve
        ro "Karnas never stood a chance, not while I was his enemy."
        xz "It’s moments like these that remind me why I like mortals so much."
        show rowan necklace neutral at edgeleft with dissolve
        ro "Karnas’ great offensive hinged on the fact that he could take Karst and prevent the Rosarian army from uniting with the Protheans when he marched on their capital."
        ro "I stopped him. Myself. With the blood, sweat and tears of our defenders. His dreams of conquest died at the foot of Karst’s walls."
        sk "One untaken castle don’t make a war, boy."
        ro "No, it doesn’t. But that wasn’t the extent of my contribution to the war effort."
        xz "Oh, do tell."
        ro "I was in the war councils with Deanara. It was {i}my{/i} word, my tactics and strategies that turned the tide in our favor."
        ro "For all the might and valiance of the other Six Heroes, they would have never succeeded without my help."
        sk "That glowing witch of Solansia led the charge against Karnas, not ye."
        show rowan necklace angry at edgeleft with dissolve
        ro "And how do you think she fed that army, Skordred? How do you think she kept cohesion in all those battles, facing the odds we did? How did she manage to march a force of its size across the Rakshan Wastes, to the very gates of Bloodmeen?"
        ro "An army is like a body. It marches on its stomach, it sees with its scouts, and it deceives its enemies with its mind. {i}My{/i} mind. Deanara was the figurehead, I was the architect of victory."
        show rowan necklace happy at edgeleft with dissolve
        ro "Karnas never had a chance. I was simply better than him."
        $ change_base_stat('c', 3)

xz "Hm… I must say Rowan, your perspective is certainly enlightening."

"The Demon’s four hands began to drift across her body in slow, sensual circles, as if they had a sentience of their own and had grown bored of the conversation. Her eyes turned to Skordred."

xz "I hope you realize dear Dwarf, that this only helps to {i}reinforce{/i} my reasons for not joining Karnas’ doomed war."

"Skordred made a sound deep in his throat like a grumbling rockslide. Even he seemed chastened by Rowan’s words."

sk "If such be tha state o’ things, why do ya serve tha Twins? If the greatest Demon Lord who ever was weren’t good enough for ye, why follow his halfbred kin?"

"Rowan saw X’Zaratl’s eyes flick over in his direction for the barest instant. There was a teasing glimmer in her eyes. She let out a low giggle."

xz "Simple. They have something interesting that I want. "
xz "...And they aren't losing a war."

return

############################################################################
############################################################################
############################################################################

label rowans_dominance_display:

scene bg14 with fade
show rowan necklace shock at midleft with dissolve
show alexia 2 necklace neutral at midright with dissolve

ro "… Mute Qerazel acrobats? And Andras did what?"

al "Kept practicing with the troupe. Even did the whole act with himself as the main lead."

ro "I’m having difficulty imagining Andras doing hoops."

show rowan necklace concerned at midleft with dissolve
show alexia 2 necklace happy at midright with dissolve

al "Honestly? It had an odd charm to it. Sort of like watching a bull do ballet."

"Rowan groaned, and Alexia chuckled at his pained expression. "

show rowan necklace happy at midleft with dissolve

"Casual strolls, full of talking nonsense. One of the few, small pleasures they could still enjoy in castle Bloodmeen."

show rowan necklace angry at midleft with dissolve
show alexia 2 necklace concerned at midright with dissolve

"At least when they weren’t interrupted."

al "Dear… Am I seeing things, or are we being followed?"

show rowan necklace concerned at midleft with dissolve
show alexia 2 necklace angry at midright with dissolve

al "Again?"

show rowan necklace neutral at edgeleft with moveoutleft
show alexia 2 necklace neutral at midleft with moveoutleft
show succubus 2 neutral at edgeright with dissolve

"Rowan followed his wife’s gaze as she glanced behind them. Three horned heads peered from behind a corner - soon four, as another angry one pushed her compatriot down, gawking at Alexia with a hateful expression."

ro "We are, and we have been for a while now. They’re not exactly subtle about it."

show alexia 2 necklace concerned at midleft with dissolve

if xzaratl_s_advances_rowan_sex:
    al "Given what happened last time… Should I be concerned?"
    
else:
    al "Should I be concerned?"

hide succubus 2 with moveoutright

"The angry succubus vanished from view as someone pulled her back by the horns, something that was instantly followed by a string of obscenities and high pitched screeching."

show rowan necklace concerned at midleft with moveinleft
show alexia 2 necklace neutral at midright with moveoutright

ro "No, I don’t think so. I’ve seen them before, and judging by their behaviour, they’re all low-rank succubi. They wouldn’t dare hurt you."
ro "And I believe it’s me they’re after. "

if avatar.corruption < 31:
    show rowan necklace aroused at midleft with dissolve
    "Alexia arched an eyebrow at him. He turned away and coughed awkwardly."
    ro "Two of them already tried to seduce me. It was rather obscene."
    show alexia 2 necklace aroused at midright with dissolve
    al "Do I even want to know?"
    show rowan necklace happy at midleft with dissolve
    ro "I’ll spare you the details."
    show rowan necklace neutral at midleft with dissolve

elif avatar.corruption > 60:
    show rowan necklace neutral at midleft with dissolve
    show alexia 2 necklace shocked at midright with dissolve
    ro "They’ve climbed my desk and spread their cunts like a pair of cats in heat. One dripped and drooled so hard she almost-- "
    show alexia 2 necklace angry at midright with dissolve
    al "Rowan!"
    show alexia 2 necklace neutral at midright with dissolve
    al "You can spare me the details."
    
else:
    show rowan necklace neutral at midleft with dissolve
    "Alexia arched an eyebrow at him. He rolled his eyes, then explained."
    show alexia 2 necklace shocked at midright with dissolve
    ro "They tried to get me to fuck them, in a rather vulgar manner. The castle maid was afraid she wouldn’t get the stain out of the desk afterward. "
    show alexia 2 necklace neutral at midright with dissolve
    "Alexia’s lips opened for a moment, then closed, the silent question forever unvoiced. She didn’t want to know."

show alexia 2 necklace concerned at midright with dissolve

"Again, Rowan glanced behind him. He watched as one of the succubi opened her mouth and pretended to stroke an invisible cock in front of her face."

show rowan necklace angry at midleft with dissolve

"He gently pulled Alexia to one of the corridors that lead back to [his/their] room. The mood was ruined anyway."

ro "It’s one option. "

show alexia 2 necklace neutral at midright with dissolve

al "You don’t sound pleased with it."

ro "I’m not. But the alternative would be, as Skordred explained to me: “To arrange a decadent display of virility and sexual prowess the castle has not seen since the reign of Gerdruth the Towering!”"

show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace shocked at midright with dissolve

ro "Who, apparently, once killed a knight by ejaculating at him hard enough. Knocked the head straight off his shoulders."

"Alexia skipped a step, and Rowan was ready to steady her. Behind them, another argument blew up, this time about the exact length of Rowan’s manhood."

show alexia 2 necklace neutral at midright with dissolve

al "I…  I would never guess this is what ruling Castle Bloodmeen is like."

if avatar.corruption < 31:
    ro "It’s usually not. But succubi like them… I don’t want to generalize, but I don’t think they comprehend much beyond sexual promiscuity and domination. "
    hide alexia with moveoutright
    show rowan necklace angry at center with moveinleft
    "Reaching the room, he opened the door for his wife, and ushered her inside. For a moment, he watched the quartet of hungry succubi with disdain. Like hell he’ll give them what they want."

elif avatar.corruption > 60:
    ro "They’re demons, of the lowest sort. All they care for is riding the biggest cock in the room, with themselves on the top. And the latter is optional."
    hide alexia with moveoutright
    show rowan necklace angry at center with moveinleft
    "Reaching the room, he opened the door for his wife, and ushered her inside. He stayed to watch the quartet of hungry succubi with annoyance."
    "Part of him wanted to just screw their brains out and be done with the problem. But the question of fidelity aside, he didn’t want to establish a precedence of indulging every common slut that pestered him long enough."

else:
    ro "They’re demons. The only thing they care for is sex and being on top. And the former is usually what they’re forced to settle on."
    hide alexia with moveoutright
    show rowan necklace angry at center with moveinleft
    "Reaching the room, he opened the door for his wife, and ushered her inside. For a moment, he watched the quartet of hungry succubi bicker."
    "Back in the war, his men told stories of lone soldiers being ravished by groups like this one, and they always blurred the boundary between cautionary tales and personal fantasies."
    "Having seen some of what Castle Bloodmeen had to offer… He didn’t see the appeal anymore."

show alexia 2 necklace neutral behind bg14

al "Do you think there might be a... A less “Bloodmeen” way of doing it? "

show rowan necklace happy at center with dissolve

"He couldn’t help but smile at the concern in her voice. A lesser man might think it stemmed from some deeply rooted fear for their marriage. But he knew she simply wanted to help. Always thinking of both of them."
"Compared to her… The succubi truly were lowly creatures. If he could only make them see- "

if avatar.corruption < 31:
    show rowan necklace neutral at center with dissolve 
    "His mouth ran dry, as the thought wormed itself inside of his mind. He {b}could{/b} make them see." 
    "… Skodred said he’d need to give them a display of sexual prowess. He never said the cubi had to be targets of it."   
    "He looked inside the room. They never tried anything like that, but… His wife might not be necessarily opposed to the idea… "

elif avatar.corruption > 60:
    show rowan necklace happy at center with dissolve 
    "He couldn’t stop a smirk. Oh, he could - he could make them see. What hollow, basic bitches they were compared to his wife. He’d show them in great detail. He didn’t need any dumb public display for that." 
    "A private show would be enough. He would simply have to leave the door ajar…"
    show rowan necklace neutral at center with dissolve 
    
else:
    show rowan necklace neutral at center with dissolve 
    "His mouth ran dry, as the thought wormed itself inside of his mind." 
    "He {i}could{/i} make them see… He could make them stay, and {i}watch{/i}. Make them realize how they stood no chance against Alexia. Make them realize now things would be done {i}his{/i} way."  
    "Good reasons, both of them. But despite that, he struggled to focus on them, as he fought back the intoxicating thrill that came with the idea." 
    "He and Alexia never discussed something like that, but they’ve been in the castle for a while now. One would have to be blind not to see all the wanton debauchery on display, so maybe she wouldn’t mind trying it…" 

menu:
    "Close the door, and have a quiet, non eventful evening with Alexia.":
        $ released_fix_rollback()
        "He shook his head, clearing his mind. The castle was getting to him. Fucking his way out of a problem was something the twins would both do, and want him to do. He had to be better."
        show rowan necklace happy at center with dissolve 
        ro "Don’t worry about it, dear. I’ll think of something."
        hide rowan with moveoutright
        "He closed the door behind, and retired for the evening, trying to pay no attention to the scratching sound at his doors."
        $ change_relation('alexia', 5)
        return

    "Leave the door open, and embrace Alexia.":
        $ released_fix_rollback()
        scene bg9 with fade
        show alexia 2 necklace shocked at center with dissolve
        show rowan necklace happy at edgeleft with dissolve
        "He saw her confused expression as he pushed the door further, and noticed it grow as he seized her hand and turned her around, pulling her to the bed."
        show rowan necklace happy at edgeright with moveinright
        show alexia 2 shocked at midright with moveoutright
        al "Rowan- "
        show alexia 2 aroused at midright with dissolve
        "He silenced her with a passionate kiss. She shared it, for a moment, then tried to glance at the door. He cupped her cheek, gently, but firmly."
        ro "You know… There might indeed be a less “Bloodmeen” way to do it."
        "He wrapped his arm around her waist, and pressed her hips close to his body." 
        "She felt his cock press against her, and drew a sharp breath. That was a sound he would never grow tired of."  
        al "You can’t be serious."
        "His lips brushed against her neck. He kissed her ear, and revealed his intentions with a sensual whisper."
        if avatar.corruption < 61:
            ro "They want me to show them what a stud I am, and I want to show them you’re the only one I care about. What better way is there than with a little demonstration?"
        else:
            ro "They want me fuck them, and I want to show how you’re the only one who’ll be taking my cock. What better way is there than to give them a small demonstration?"
        "She tried to pull herself away, but he held her close, and it wasn’t as if she was putting any real spirit into it."
        al "That’s- "
        ro "Unconventional, I know. But that doesn’t mean it won’t be fun."
        al "That’s beside the point!"
        show rowan necklace shock at edgeright with dissolve    
        show alexia 2 necklace angry at midright with dissolve
        "- until she slapped his hand away, and shot him a disapproving look."
        al "Tomorrow, you’ll leave for Rosaria."
        show rowan necklace neutral at edgeright with dissolve    
        show alexia 2 concerned at midright with dissolve
        ro "And I will stay, as I always do. And I’ll be forced to deal with people snickering behind my back at every corner."
        if avatar.corruption < 61:
            "A valid concern. Still…"
            show rowan necklace angry at edgeright with dissolve
            "He looked up, and locked eyes with the succubi. They all shied away, as if expecting to be thrown out."
        else:
            "He barely stopped himself from rolling his eyes. With X’zaratl around, an amputee orgy was yesterday's news before it even ended. Alexia was spending too much time cooped up in her room."
            show rowan necklace angry at edgeright with dissolve
            "But being a loving husband, he kept that thought to himself. He looked up, and locked eyes with the succubi. They all shied away, as if expecting to be thrown out."
        ro "You won’t say a word, will you? I know you all want to take her spot. But if I hear a word of this when I come back… "
        "He let his hand brush against the handle of his sword."
        ro "I won’t be looking for the guilty party. You’ll all take collective punishment."
        show rowan necklace happy at edgeright with dissolve
        "He watched, with great satisfaction, as they all nodded their heads fervently. He kissed Alexia again, whispering she needed to worry about rumours."
        show alexia 2 necklace aroused at midright with dissolve
        "She wasn’t convinced, not in full. But she didn’t try to pull away anymore, and he could swear the redness of her cheeks didn’t come just from embarrassment anymore."
        al "… This isn’t some long held male fantasy you never told me about, is it?"
        "He let go of the sword, and ran his hand up her back. He felt her shiver in his arms, full of nervous anticipation."
        ro "To shun a quartet of sex demons and make them watch as I make gentle love to my wife? "
        show rowan necklace neutral at edgeright with dissolve    
        show alexia 2 angry at midright with dissolve
        ro "I would like to exercise my right to remain silent."
        show rowan necklace happy at edgeright with dissolve
        al "Unbelievable."
        "She brushed her hair away, agitated. He moved his hand to untie her dress, and finally pull her to the bed, only for her to grasp it, this time firmly."
        show rowan necklace neutral at edgeright with dissolve 
        al "I’m not going to let a bunch of demons ogle my naked body, Rowan."
        show rowan necklace happy at edgeright with dissolve    
        show alexia 2 aroused at midright with dissolve
        "She hesitated for a moment, then rested her hands on his chest, and kissed him, deeply. She let herself be lost in the moment, her hands roaming his body, fingers dancing across his sculpted muscles."
        "Starting from the top, she slowly made her way down."
        al "But if it is going to help you… I guess we could try something."
        "And halfway, she began to lower herself too."
        al "I hope you appreciate everything I’m doing for you here, dear."
        ro "As if you weren’t enjoying it, at least a little."
        "He brushed a stray hair away from her eyes, and smiled down on her. A defiant pout was her only response."
        "He didn’t hurry her. There was no need. He ran his fingers through her hair, caressing her affectionately. Her hand brushed against the tip of his cock-"
        show succubus 1 behind bg9
        succubus1 "Aaaaaaah, what is she doing? I want to see, I want to see!"
        "Alexia’s ears turned red, but she pretended she didn’t hear the succubus. She knelt on the floor, and with a swift move of her hand, released his cock. It sprung forth, towering over her."
        succubus2 "My, my, it looks like I guessed right. Such pleasant size and shape… And what alluring smell! A perfect male specimen indeed."
        al "… I hope you don’t expect me to sing you such praises."
        ro "No… But I wouldn’t stop you either."
        "He traced a finger across her cheek, and settled it on her lower lip. He gently pushed it in, forcing her mouth open."
        ro "You know what to do."
        "His wife took a deep breath. They’ve done this so many times, but now, with the succubi watching… Even if she couldn’t see them, she heard them talk, heard them giggle, and comment. It made her heart beat faster."
        #CG1 
        scene cg800 with fade
        pause 1
        show cg801 with dissolve
        pause 1
        show cg802 with dissolve
        pause 1
        show cg803 with dissolve
        pause 1
        show cg804 with dissolve
        pause 1
        show cg805 with dissolve
        pause 2
        show succubus 1 behind cg805
        show succubus 2 behind cg805
        show succubus 3 behind cg805
        show succubus 4 behind cg805
        show succubus 5 behind cg805
        show succubus 6 behind cg805
        show rowan necklace happy behind cg805
        show alexia 2 necklace aroused behind cg805
        "Not wishing to prolong this confusing torture, she ran her tongue up his shaft, from the base to the very tip. She rolled it over the head, making him take a sharp breath - and then took it all in." 
        "The familiar wetness of her mouth felt fantastic, and the thrill of having her usual blowjob witness elevated this usually mundane experience to new heights. He moaned quietly, as Alexia started to bob her head in an unsteady rhythm."
        "She felt it too - the eyes of the succubi watching her every move. Every lick of her tongue, every kiss of her lips - now had a feeling of nervous urgency to it."
        rudesuccubus "Ha! Rushing to the finish already! What is this, amateur hour?!"
        "Alexia almost slid off his cock at the humiliating remark, and it was only his guiding hand that kept her in place. He threw the succubus a murderous glare, and the damn bitch smirked at him."
        $ rowanAggression = 0
        menu:
            "Praise Alexia’s eagerness.":
                $ released_fix_rollback()
                $ rowanAggression += 1
                ro "And how can I blame her? She waits for me all week, having only her fingers and memories for comfort… "
                ro "I, for one, love it when she takes my cock so greedily."
                "He never stopped his loving stroking, but as he ran his fingers across her hair, he did pull her head in, just a little."
                ro "When she sucks it, licks it, with such affection."
                "Slowly, Alexia resumed her nervous blowjob, bobbing her head gently, her tongue caressing him with devotion. She looked up to him, through half-lidded eyes."
                ro "You’re such a great cocksucker Alexia. These demon sluts wish they had even a quarter of your skills. The way you tease it with the tip of your tongue. Ah!"
                "He moaned, and he heard the frame of his doorway crack. Gritting her teeth in frustration, the impertinent succubus held on so tight, ran her fingernails through it. Rude."
                
            "Ignore the succubus. What do demons know of love?":
                $ released_fix_rollback()
                ro "You will not speak again. Or else you might find yourself without a tongue. "
                "He never stopped his loving stroking. Having made his point, he looked down, and simply smiled as Alexia gathered herself again."
                ro "Focus on me, Alexia. Pay them no heed."
                "She closed her eyes, and rolled the tip of her tongue over his head. He took a sharp breath, not holding in the needy moan, as Alexia resumed to bob her head gently, worshipping his cock with utmost attention."
                
        succubus1 "Aaaaaaw, it’s no fair!"
        "Another succubus complained. Eyes transfixed at the back of Alexia’s head, this one had her tongue rolled out, drooling to the floor like some sort of cockhungry animal."
        salivatingsuccubus "Aaaah, I’m so jealous, I’m so jealous! It smells so goooooood! And it looked so tasty!"
        salivatingsuccubus "Why is she having such a nice cock all to herself! I want it too! I want to taste it, lick it, worship it, suck it dry! I want to ram it down my throat! I want to gag on it!"
        salivatingsuccubus "You should use me instead! You should use my throat instead!  Fuck my throat!  Use it as your personal cocksleeve, fill my stomach with your cum! Do it! Do it! {i}Do it{/i}!"
        menu:
            "Shove your cock down *Alexia’s* throat.":
                $ released_fix_rollback()
                $ rowanAggression += 1
                ro "You mean like… {b}This{/b}?"
                "He grabbed Alexia’s head and shoved his cock all the way in, making it hit the back of her throat. He heard her gag, but after a moment of surprise, she relaxed her throat, and let him set the tempo."
                "The whine that followed was music to his ears. The salivating succubus thrashed and complained, how it should be her instead, how much better her throat feels, how she loves-"
                if rowanAggression > 0:
                    succubus2 "Please be quiet, dear. Running your mouth like that won’t make master Rowan plug it with his cock."
                else:
                    rudesuccubus "Shut your fucking mouth. It’s not getting any cock either way."
                "Rowan chuckled as he saw her obey. For a moment, the lone sound any of them heard was the obscene, gagging sound his wife made."
                "Having made his point, he let Alexia go. She gasped for air, her unfocused eyes shining with unshed tears."
                al "Haaa… Haaaa…"
                "She looked up. Seeing him grin, she swallowed heavily, and opened her lips again, enveloping his cock lovingly."
                
            "How Obscene. Your wife is not some hole to use.":
                 $ released_fix_rollback()
                 "He said nothing of the Succubus remark. He kept his hand possessively on Alexia’s head, and let her continue to worship his cock at her own pace. For a moment, she slid off his cock."
                 al "Haaaaa… It really… Does taste good."
                 "The Succubus whined in protest. Rowan chuckled, and Alexia resumed her caress without another word."
                 
        succubus2 "My, my… Who would have thought."
        succubus2 "So nice. So willing. So {i}servile{/i}."
        "Again one of the succubi spoke up. This one had a laugh that grated his ears, and a condescending smile Jezera would be jealous of. Tall and proud, there was no mistaking the alpha of the group."
        haughtysuccubus "You want obedient toys, Rowan, we can be them too."
        "Her lips parted in a wicked smile. She reached behind her, and Rowan heard something snap."
        "She pulled out a skimpy, red thong, and held it high for him to see. Thoroughly soaking with her juices, it made a wet splash as it hit the floor."
        haughtysuccubus "See how happy you make us, master Rowan? Why avoid us? We could be your perfect little cocksluts."
        haughtysuccubus "We would obey your every order. Fulfill every perversion. Realise {b}every{/b} fantasy."
        haughtysuccubus "And we’d {b}love{/b} every minute of it. I bet *she* isn’t even masturbating."
        menu:
            "She is.":
                $ released_fix_rollback()
                $ rowanAggression += 1
                "Alexia’s tongue stopped it’s feverish dance, and she looked up, the expression in her eyes unreadable, even to him."
                ro "This is just foreplay after all. I know she has her hand snuck under her dress."
                ro "I know she’s tracing her fingers across her sodden pussy, waiting to take my cock."
                ro "Pushing against the thin material, imagining how I’ll throw her on the bed and thrust in her!"
                al "Mmmmff!"
                "The muted cry of pleasure was one of the sweetest sounds Rowan ever heard. She followed every one of his orders, her hand disappearing from his view." 
                "Smiling, he pushed his hips forward, urging Alexia to resume her work. They were putting on a show, after all."
                
            "She doesn’t have to. You’ll repay the favour later.":
                $ released_fix_rollback()
                ro "I think she’s enjoying herself plenty. I’ll be sure to inspect it."
                ro "Throw her to the bed, spread her legs, and see with my very eyes, up close, just how much my wife is happy to see me."
                ro "Maybe even repay the favour. How does that sound, Alexia?"
                "Alexia slid off his cock for a split moment, and gave the tip a quick kiss, the corners of her lips turned up in an embarrassed smile."
                salivatingsuccubus " Eeeeeh?! That’s no fair! Orcs never do that to us!"
                haughtysuccubus "They’re not supposed to!"
                
        "Alexia picked up the pace, her slurping sounds dominating the room. He was getting close now. He looked to the Succubi with a cocky grin - and found himself inspecting the one who had yet to speak up."
        ro "Nothing to say? Don’t hold yourself back. Your friends are plenty talkative."
        "With a long fringe that almost covered her eyes, the succubus had to brush her hair aside to look him in the eyes. They were vibrant green, and they studied him with innocent curiosity."
        "Her fingers traced her lower lip, slowly, almost nervously. There was the same hungry look on her face he saw in the other succubi, but it was nowhere near as obscene as in the rest."
        quietsuccubus "Are her lips soft?"
        quietsuccubus "I want to know. Please." 
        "Her question threw him off - and just right then, he felt himself being pushed over the edge."
        if rowanAggression > 1:
            "Driven by lust, he pushed his hips forward, forcing his cock down Alexia’s throat, given her no choice but to swallow."
        else:
            "He clenched his jaw, fighting back the natural instinct to push his cock down her throat. There was no need - Alexia sealed her lips around his crown, and slowly sucked him dry."
        salivatingsuccubus "No fair no fair no fair no fair!!! It should be meeeeeeeeeeeee!"
        haughtysuccubus "Hmph."
        scene black with fade
        "He let out a satisfied sigh, releasing Alexia from his grip. When he looked up, the quiet succubus was no longer there."
        scene bg9 with fade
        show rowan necklace happy at center with dissolve
        show alexia 2 necklace aroused at edgeright with dissolve
        al "Alright, show’s over. And remember what I said - not a word."
        "He shut the door straight in their faces, much to the cubi chagrin. He turned around, and watched as Alexia rose up to meet him, dusting her dress."
        if rowanAggression > 1:
            al "That was… More intense than I imagined."
            show rowan necklace happy at midright with dissolve
            "She brushed aside her disheveled hair, and wiped the saliva off her chin. Minor things, to make herself look presentable."
            "All of which failed to hide the excited blush on her cheeks, and the slight outline of her nipples, poing through her dress."
            "Laughing, he wrapped his arms around her, and kissed her on the forehead. Holding her close, he could now feel how hard her heart was hammering."
            ro "Sorry, I got a bit caught up in the moment."
            show alexia 2 necklace angry at edgeright with dissolve
            al "Oh, believe me, I noticed."
            show alexia 2 necklace aroused at edgeright with dissolve
            ro "Then… How about I repay the favour?"
            al "She narrowed her eyes at him. He grinned."
            hide rowan with moveoutright
            show alexia 2 necklace happy at edgeright with dissolve
            show bg9 with sshake
            "Then he found himself being jokingly pushed to the bed. Alexia towered over him, not even hiding her excitement anymore."
            show alexia 2 necklace aroused at edgeright with dissolve
            al "Oh, you will. You most definitely will."
            scene black with fade
            "The evening was only starting, after all…"
            $ change_corruption_actor('alexia', +6)
            return
            
        else:
            al "That was… I don’t think that was what they were expecting to see."
            show rowan necklace happy at midright with dissolve
            "She brushed aside her slightly disheveled hair, and wiped the saliva off her chin. Minor things, to make herself look presentable."
            "All of which failed to hide the excited blush on her cheeks, and the slight outline of her nipples, poking through her dress."
            "He wrapped his arms around her, and kissed her on the forehead. Holding her close, he could now feel how hard her heart was hammering."
            ro "I have no intention of playing by their rules all the time."
            show alexia 2 necklace happy at edgeright with dissolve
            show rowan necklace shock at midright with dissolve
            al "Mhm. But now I’m starting to think the whole idea was just an excuse to show me off to some of the castle staff."
            show rowan necklace happy at midright with dissolve
            "She narrowed her eyes at him. He grinned."
            ro "… Maybe a little?"
            hide rowan with moveoutright
            show bg9 with sshake
            "Suddenly he found himself being jokingly pushed to the bed. Alexia towered over him, a mischievous smirk dancing on her lips."
            al "Then I believe apologies are in order, dear."
            hide alexia with moveoutright
            show alexia 2 necklace happy behind bg9
            al "We’ll start with repaying the favour."
            scene black with fade
            "The evening was only starting, after all."
            $ change_corruption_actor('alexia', +3)
            $ change_relation('alexia', 5)
            return

############################################################################
############################################################################
############################################################################

label cliohnas_domination:

scene bg9 with fade
show rowan necklace naked at midleft with dissolve

"Staring at his naked body in the mirror, he ran his hand across his chest. The wound from Cliohna’s lightning healed without a trace, but he could still recall the searing pain it brought." 
"It’s been some time since their “experiment” together. Cliohna kept to her word, keeping things professional. So had he. But the matter laid unresolved between them."

show rowan necklace neutral at midleft with dissolve

if serveChoice == 4:
    "He couldn’t leave it that way. Cliohna was an important cog in the Bloodmeen mechanism, and he needed her support if he was ever to do any good here."
    
else:
    "He couldn’t leave it that way. For all her faults, it didn’t seem like Cliohna had any ambitions for world domination. He needed her support if he was ever to strike back at them. "

scene bg9 with fade
show rowan necklace neutral at midleft with dissolve

ro "Inform Cliohna I will be seeing her this evening, after the sun sets, to discuss the results of our experiments."
 
"A castle maid bowed her head and hurried away. He’d given Cliohna enough time to ponder. It was high time he moved into offense himself." 

scene black with fade

"… That being said, he soon regretted having Cliohna wait for him. The remainder of the day dragged on, reports and various complaints all coming to him as if through a fog." 
"He felt the blood rush in his veins, his senses sharpened, his mind tuning out all it deemed pointless and unnecessary. His body readied itself for battle. That’s what his meetings with Cliohna turned into - endless struggles for supremacy."

scene bg12 with fade
#cliohna shocked
show cliohna neutral at center with dissolve

"She felt it too. He saw it in the way her whole body tensed as he walked into the library, in the guarded look in her eyes. For a moment, he thought she’d greet him with another lightning bolt."

show cliohna neutral at cliohnaright with moveoutright
show rowan necklace angry at midleft with dissolve

"Instead, she turned her gaze away, closing the ancient book she held in her hands."

show rowan necklace neutral at midleft with dissolve

cl "Rowan. On time, as always. Please, have a seat."  

"He held back a cutting remark. He couldn’t lose sight of his goal. He had to mend their relationship, not reignite their conflict without reason. He took a seat in front of her desk, as did Cliohna behind it."

ro "I see you’ve sent away your students. Should I be worried? "

show rowan necklace angry at midleft with dissolve

"She kept her expression neutral. Indifferent. Subdued, even?"

show rowan necklace neutral at midleft with dissolve

cl "… No. Your concern is not unwarranted, but I assure you, Rowan, regardless of what happened before, you are at no risk here."
cl "Before, I have allowed my emotions to get the better of me. I broke the terms of our arrangement, harming you and damaging the trust between us."

show rowan necklace shock at midleft with dissolve

cl "For that, you have my sincerest apologies. I am willing to talk compensation, in terms of magical items, additional allocated research, or favours."

show rowan necklace neutral at midleft with dissolve

"She put her hands together, watching him closely. A motion that served only to accent the considerable gaps in her clothing. But at the moment, he paid them no mind." 
"He was at a loss of words. Just like that? An apology and compensation? Delivered to him on a gold plate?" 

show rowan necklace angry at midleft with dissolve

"Was this a trap? An elaborate scheme, to lower his guard?"

show rowan necklace neutral at midleft with dissolve
show cliohna angry at cliohnaright with dissolve

ro "… And what of our research? What did you discover?"

"He asked to buy himself time to think, and he saw her hand tremble. A moment of silence went past, before she slid a stack of papers to him."

show cliohna neutral at cliohnaright with dissolve

cl "The experiment proved to be a resounding failure. You, Rowan Blackwell, are a perfectly normal human being."
cl "You possess no magical abilities, no affinity for the craft, no innate power, nothing. You have no magical protections on you, no magical items, no hidden runes that activate if sufficient magical pressure is detected. "
cl "You have no nonhumanoid ancestry, and no humanoid non-human ancestry. There is not a drop of dragon, demon, celestial or fae blood in you, that could manifest as latent defensive powers."

show rowan necklace happy at midleft with dissolve
show cliohna angry at cliohnaright with dissolve

cl "Neither do you share a subterranean ancestor with Skordred, despite displaying common dwarven traits, such as their famed stubbornness."

show rowan necklace neutral at midleft with dissolve
show cliohna neutral at cliohnaright with dissolve

cl "There is neither holy nor unholy protection on you. At least none I could detect, which rules out most Gods."
cl "As far as I’m concerned, you are the perfect sample of a regular, incredibly magically inept, if unexpectedly resilient, but still - normal human being."

"He could not miss the strained tone of her voice. He shifted through the files as she spoke, and while could make no sense of the esoteric magical lingo they were written in, he could see what their experiments did to {i}her{/i}."

cl "Does the answer satisfy you Rowan?"

"What started as a factual record of her tests, soon turned to something else. The neatly written, straight lines gave way to hectic, chaotic notes, written down in haste, scribbled on the sides and corners of every page."
"“Ancient prophecy involved? \nRackshan? Prothean? Dragon? Elven? Dwarven? Goblin? \nNone of these. Other?”"  
"“Driven by: Fear? Hero complex? Raw determination? Sexual desire to dominate?”"

show rowan necklace angry at midleft with dissolve

ro "… “Brutish simplicity?”"

cl "Uncalled for, I acknowledge that. As you’ve no doubt noticed, I allowed myself to become more invested in the project than it was healthy."
cl "And I recognize because of that, my actions have put us at odds with one another, when we should not be. "

show rowan necklace neutral at midleft with dissolve

"There was an almost unnoticeable pause that followed, and he knew the words that followed were both carefully picked, and practiced many, many times."

cl "Rowan. I acknowledge your skill, and contribution to castle Bloodmeen. There is no reason for us to be enemies, not when we have so much to gain by being allies."
cl "Again, I apologize for what has happened, and to make it up for you, I offer not only my vast magical expertise, but also the influence I can exert over the twins."
cl "Within reason, of course."

"Her eyes briefly went to the amulet at his neck. Not that he held any hopes in that regard. Things were never that easy."

cl "And in return, I ask only that you hold no ill will for my previous… Outburst, and review my future projects based on their merit, and not personal feelings."
cl "Does this sound acceptable, Rowan? "

"That was as much of an apology as he could honestly hope for here. He suspected it took every inch of her self control not to sound exasperated. She kept his gaze, careful not to look at the notes he still held in his hands." 
"Somehow, he had the feeling it was only her integrity as a researcher that didn’t allow her to burn this shameful proof of her defeat." 
"He still felt the blood rush in his veins. He expected to fight her, and here she was, offering him all he could ask for, if not more."   

show rowan necklace angry at midleft with dissolve

"… Yet somehow, this victory felt hollow to him."


label cliohnaDomMenu:

menu:
    "Did she really learn her lesson?":
        $ released_fix_rollback()
        if hypnosis2SubEnding == True:
            ro "You know… Calling a very conscious effort to mindbreak me an “outburst” is underselling it a little, wouldn’t you say?"
            ro "There was also lightning involved? And I believe my body was used to shatter some of the library furniture. A chair, to be precise."
        else:
            ro "Cliohna, “outburst” is a very light term for sending me across the room with a lightning bolt, right at one of your chairs."
        "The destruction of which, I feel inclined to mention, was noted in the monthly damage report. Do you want to know what Skordred wrote as the direct cause of damage?"
        "He narrowed his eyes, not trying to hide the displeasure from his voice. Cliohna withstood his withering look, seemingly unrepentant - though she did close her eyes for a moment to gather herself, before answering."
        cl "I believe we’ve learned the dangers associated with reckless pursuit of knowledge, which seems to be a recurring theme among practitioners of the arcane. For once, I will choose to remain ignorant."
        ro "Very amusing."
        show cliohna angry at cliohnaright with dissolve
        ro "How do I know this won’t happen again? That I won’t find myself be the direct cause for the library renovation?"
        cl "If you doubt my character, then trust my self-interest."
        cl "I assure you, indulging the twin’s various requests is tiring enough. I don’t need another person to appease constantly, simply because I allow myself to be caught in the moment."
        cl "A one-time outburst entails a one-time compensation. After that, we shall return to business as usual."
        show cliohna neutral at cliohnaright with dissolve
        "“Business as usual.” So her treating him with politeness that bordered on condescension. The thought made his blood boil."
        jump cliohnaDomMenu
        
    "How can he know it’s not a trap?":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        ro "Let’s assume I’m satisfied with this. How do I know this isn’t just a trick to lower my guard? How do I know you won’t whack me in the back of my head with “the magical equivalent of a sledgehammer”, the moment an opportunity arises?"
        show rowan necklace shock at midleft with dissolve
        cl "Because I like to look my enemies in the eyes when I break them."
        show rowan necklace neutral at midleft with dissolve
        "He expected her to continue. She didn’t. She simply continued to watch him, with those grey, ancient eyes of her."
        "If he thought her cowed before, he didn’t now. He knew the sorceress was old, but how old exactly? How many mages did she break with her mind control, how many warriors did she reduce to dust with her lightning?"
        show rowan necklace angry at midleft with dissolve
        "Who was he, to challenge her, who stood on a pile of bodies built over centuries?"
        "He looked down, and turned another page of her research."
        ro "“Secret Prothean Mageslaying training?” I’ve never even heard of anything like that, Cliohna."
        show rowan necklace neutral at midleft with dissolve
        cl "I theorize it exists. Arcane magic surpasses divine gifts, and the Prothean Church has long proved it tolerates no competition."
        cl "But that’s a discussion for another time."
        "He nodded his head slowly. He didn’t mention the comment underneath. {u}“Likely.”{/u} Twice underscored." 
        "How many dark warlords has he slain leading the armies of Rosaria, and then with Daenara and the heroes of the six realms by his side?"
        "Cliohna wasn’t the only person in this room standing atop a mountain of bodies."
        show rowan necklace angry at midleft with dissolve
        "And yet she still looked down on him."
        jump cliohnaDomMenu
        
    "What if her offer didn’t satisfy him?":
       $ released_fix_rollback() 
       show rowan necklace neutral at midleft with dissolve
       "He kept turning the notes in his hands. Pages upon pages of frustration, struggle and ultimately - defeat. An experience that ought to humble her, at least a little."
       "And yet here she was, trying to sell him a bunch of garbage favours just to get him out of her sight. It made his skin itch."
       show cliohna angry at cliohnaright with dissolve
       ro "One could think there would be some reward to beating you in a contest of wills." 
       show rowan necklace angry at midleft with dissolve
       "She rolled her eyes at him. Actually rolled her eyes! Impudent witch."
       show cliohna neutral at cliohnaright with dissolve
       cl "This was no contest Rowan, but an experiment. We were not in it for entertainment, but to further the cause of magic."
       show rowan necklace shock at midleft with dissolve
       cl "… And you didn’t “beat” me."
       ro "Excuse me?"
       show rowan necklace angry at midleft with dissolve
       cl "You persisted in a series of tests, with predetermined boundaries in which we tested the extent of your mental resilience."
       cl "*That* is all you did."
       show rowan necklace neutral at midleft with dissolve
       cl "… Which, as I have confessed, is nevertheless admirable in itself. Hence the offered compensation."
       show cliohna angry at cliohnaright with dissolve
       cl "Which, again, I am more than willing to discuss, as soon as you stop playing on my nerves!"
       "The last word was almost a hiss. She didn’t accept her defeat. Didn’t acknowledge her faults, not in full. And both gnawed at her, he {i}saw{/i} that!" 
       show rowan necklace happy at midleft with dissolve
       "He saw the crack in her armor, a weakness for him to exploit-"
       menu:
           "Strike it!":
               $ released_fix_rollback() 
               jump cliohnaProdding 

           "Don't. Cliohna is not your enemy. Accept her terms, and return to status quo.":
               $ released_fix_rollback() 
               show rowan necklace neutral at midleft with dissolve
               "His hand trembled, and the notes in his hands rustled softly. Tangible proof of what chasing victory could to someone." 
               "He took a deep breath, and forced himself to calm down... He was letting his pride talk, he knew that. He couldn’t make the same mistake Cliohna did." 
               #cliohna shocked
               ro "… You’re right. I let my frustration get the better of me."
               "He laid the notes down. Cliohna eyed them like one would eye a venomous viper, then slowly took them away."
               show cliohna happy at cliohnaright with dissolve
               show rowan necklace happy at midleft with dissolve
               cl "I would offer a snide remark, were I not sharing the sentiment."
               ro "A recurring theme as well, this time between us."
               "He chuckled, and he saw Cliohna answer with a shadow of a smile. Right, this was better. Smarter."
               jump cliohnaStatusQuo
                
label cliohnaProdding:

show rowan necklace neutral at midleft with dissolve
show cliohna angry at cliohnaright with dissolve

"- And he went for it. He rose to his feet, no longer able to sit still."

cl "Rowan, I am trying to be patient here!"

show rowan necklace angry at midleft with dissolve

"She rose to meet him, leaning across the table with barely contained fury, and he swore he could see lightning run down the strands of her hair."

ro "Well, that makes two of us. But despite beating you fair and square, {b}on your own terms{/b}, I still can’t get any gods damn respect!"

"Prod her, poke her, test her pride. He knew the look in her eyes. Saw it all so often in the war."

cl "I find it difficult to respect a man who would rather argue petty details than try and see the bigger picture for a minute!"

"The look of a woman who would sooner damn herself than to admit defeat."

menu:
    "“Just admit you weren’t skilled enough to beat me.”":
        $ released_fix_rollback() 
        jump cliohnaSkilledEnough
        
    "Don’t. Take what was offered before this spirals out of control.":
        $ released_fix_rollback() 
        show rowan necklace neutral at midleft with dissolve
        "He felt the blood rush in his veins, and felt its taste in his mouth. He had to bite himself in the tongue to avoid saying words that could not be taken back."
        show rowan necklace shock at midleft with dissolve
        "What was he even trying to do here? Cliohna was no enemy of his. Did he really want to beat her so much? So much he’d-"
        show rowan necklace happy at midleft with dissolve
        ro "… Ah."
        #cliohna shocked
        "He chuckled, and Cliohna narrowed her eyes at him, a confused look behind them."
        #show cliohna angry at cliohnaright with dissolve
        cl "Do you find this funny, Rowan?"
        ro "Maybe a little. Do you know this saying, what happens when an unstoppable force meets an immovable object?"
        cl "A whole lot of frustration it seems."
        ro "Precisely."
        #cliohna shocked
        "He slid the notes over. Cliohna eyed them like one would eye a venomous viper, then slowly took them away."
        show rowan necklace neutral at midleft with dissolve
        show cliohna neutral at cliohnaright with dissolve
        ro "I apologize. I suppose I’ve grown somewhat… Exhausted, with the treatment I tend to receive here."
        "Her expression softened, and she sat down with a sigh."
        cl "Understandable. I… I apologize too. I’ve treated you poorly, yet I expected more patience than I was willing to offer myself."
        show rowan necklace happy at midleft with dissolve
        show cliohna happy at cliohnaright with dissolve
        cl "Rowan. You’ve performed admirably. I’m sorry this has all ended in such a distasteful manner. Shall you accept my offer of peace?"
        ro "I shall."
        cl "Most excellent."
        jump cliohnaStatusQuo
        
label cliohnaSkilledEnough:

show rowan necklace neutral at midleft with dissolve

"His words hung in the air, impossible to ignore. He saw a crackle of lightning dance between her fingers. If he was wrong about her, he was seconds away from being splashed across the castle walls. But if he was right..."

show cliohna angry at center with moveinright

"Like a tiger on the prowl, she left her desk, and slowly made her way to him."

show cliohna neutral at center with dissolve

cl "… Who do you think you are, Rowan Blackwell?"

show cliohna neutral at edgeleft with moveoutleft

"Her eyes never left his, a pair of shining gems, flashing pink, burning holes in his skull."

cl "What exactly are you trying to accomplish here?"

show cliohna neutral at center with moveinleft

cl "If you think I’ll lose my cool again and you survive the following outburst to elicit even more favours out of me, then you are both suicidal, and very, {b}very{/b} much mistaken."  

show cliohna happy at center with dissolve

"He’d swear he felt the heat of her half-naked body as she leaned in to whisper in his ear. He took no step back."

cl "Or do you, perhaps, honestly think you’ve actually beaten me? {b}Me{/b}? "

show cliohna happy at cliohnaright with moveoutright

cl "I expected such arrogance from the twins. They at least have the magical potential capable of contesting my own, even if they lack the intellectual capacity to ever rise beyond being a petty dark wizard."

show cliohna angry at cliohnaright with dissolve

cl "But you…"

"She ran a finger across his chest, across one of the many scars that made it."

show cliohna neutral at cliohnaright with dissolve

cl "You are just human. Of some intellect, though I am starting to think I overestimated the full extent of it."

show cliohna happy at cliohnaright with dissolve

"Her lips twitched. She smiled. That self-served, confident smile. Pride was one hell of a drug."

cl "Or do you think that maybe, just maybe, that you were chosen by history to accomplish great things?"
cl "Once champion to Solansia, savior of the world. Now champion to Kharos, bringing it to its knees."
cl "Perhaps your imprisonment drove you insane after all, “champion”."

"She chuckled at him, actually chuckled at him! He made no move, letting Cliohna circle him, eying him like a prized prey."

show cliohna angry at cliohnaright with dissolve

ro "Or perhaps you overestimate your own ability. Books offer no resistance, and present no challenge. "

"The thunder he heard might have been just in his mind, but the outrage in her eyes was more than real. She wanted to beat him so bad. And as long as he dangled the possibility in front of her eyes…"

menu:
    "Give her another shot. You will triumph again regardless.":
        $ released_fix_rollback()
        cl "If you had any idea of the things I could do-"
        show rowan necklace happy at midleft with dissolve
        #cliohna shocked
        ro "They won’t help. But I invite you to try."
        "That threw her off. He opened his arms invitingly, and he couldn’t help but smile himself. Fuck, maybe he was going mad after all. But {b}this{/b} was his leverage! The one thing no other man in the castle could give the sorceress!"
        "The promise of the sweet taste of victory." 
        show cliohna neutral at cliohnaright with dissolve
        ro "Your offer is not enough. So let’s double down. Three more chances, for double the favours. Sounds fair?"
        if (cliohnaResistance >= 2 and hypnosis2SubEnding) or cliohnaResistance == 3:
            "“To continue would be not research, but personal indulgence.” Weren’t those her words?"
            "But it was one thing to see the bait, another to deny it."
        else:
            "She said it herself, that she suspected he was toying with her, pushing and yielding seemingly at random, to keep her on her toes. She saw the danger."
            "But did she think it a threat?"
        "And as he watched the subtle flush of her cheeks he knew the answer already."
        cl "...People sometimes forget, but I am not only a librarian. I am also a teacher."
        show bg12 with pinkflash
        "The pink flame erupted over her fingers, casting a dark shadow across her face, across the small smile that now decorated her expression oh so charmingly. He couldn’t look away - a familiar warmth spread across his body, burning him from the inside."
        cl "I hope you will find this lesson- "
        show cliohna angry at cliohnaright with dissolve
        show rowan necklace neutral at midleft with dissolve
        ro "No."
        "His limbs felt as if he was swimming in tar, and his tongue as it had a mind of its own, rushing to sing praises for the sorceress. Old tricks - but he wouldn’t let Cliohna start with the new ones yet."
        show cliohna happy at cliohnaright with dissolve
        cl "Oh, Rowan-"
        show cliohna angry at cliohnaright with dissolve
        ro "I said {b}no{/b}."
        ro "Not yet."
        "The pink flame surged on, burning even brighter, burning as strong as the sorceress wounded ego."
        ro "Cliohna… {i}Don’t{/i}."
        "For a moment, he felt the Sorceress wouldn’t let go - and he readied himself for a repeat of their last session."
        cl "Unbelievable."
        "The flame disappeared, replaced by a searing gaze that nevertheless held no magic in itself."
        cl "I’m beginning to think you are guided solely by a pure, undiluted desire to {i}infuriate{/i} me."
        ro "Hardly. You only get three more shots, remember?"
        ro "Make them count. And there are things I need to take care of as well."
        ro "I will send for you when the time is right."
        "He tried to steady his hammering heart, did his best to keep the excitement from his voice. Cliohna hasn’t moved one inch. An unconquered monolith. Slowly, {i}oh so painfully slowly{/i}, bending to his will." 
        #cliohna shocked
        show rowan necklace happy at midleft with dissolve
        cl "Simply unbelievable."
        #cliohna angry
        show rowan necklace neutral at midleft with dissolve
        "She took a step back, then another, each costing her a great degree of effort as she tore herself away from him, until she finally turned around to return to her desk."
        cl "But if that is the case, then I will take the liberty and spend some of the promised capital to garner some favour with the twins for you."
        show cliohna neutral at cliohnaright with dissolve
        cl "Otherwise, given your attitude, I dread Andras will kill you by the end of the year."
        "He voiced no opposition. If it made her feel any better, then it was of no difference to him. He got what he wanted. He would make her wait. He would make her want conquering him more than anything in the world."
        show rowan necklace happy at midleft with dissolve
        "He will make her his."
        cl "… And I suspect even if I were to animate your rotting corpse, your dead body would still refuse to do as I command."
        ro "You flatter me."
        cl "Not my intention. Now, is there anything else you wanted to add, Rowan?"
        show rowan necklace neutral at midleft with dissolve        
        ro "No. For the time being, let’s return to business as usual." 
        "The deadpan stare was her sole answer. He lowered his head respectfully, and headed for the exit -"
        "Notes still in his hands." 
        "He couldn’t help himself. He turned around - and seeing Cliohna’s continued death glare, wisely decided to place them in front of her without another word."
        scene black with fade 
        "All in due time."
        $ breakingCliohna = True
        $ change_favor('andras', 3)
        $ change_favor('jezera', 3)
        return


label cliohnaStatusQuo:

$ researchNotPicked = True
$ jezFavourNotPicked = True
$ AndrasFavourNotPicked = True
$ EquipmentNotPicked = True
$ DriderConditioningNotPicked = True

show cliohna neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with dissolve

cl "State your demands Rowan, and I will accommodate them to the best of my ability."

$ cliohnaBoon = 0

label boonCount2:
if cliohnaBoon == 2:
    jump postBoon2
elif cliohnaBoon == 1:
    cl "Anything else?"
    jump boonMenu2
else:
    jump boonMenu2

label boonMenu2:

menu:
    "More research." if researchNotPicked:
        $ released_fix_rollback()
        $ researchNotPicked = False
        cl "An apt demand, given I had taken your own time for this catastrophe.  "
        cl "Consider it done."
        $ change_research_bonus(3)
        $ cliohnaBoon += 1
        jump boonCount2
        
    "Favour with Jezera." if jezFavourNotPicked:
        $ released_fix_rollback()
        $ jezFavourNotPicked = False
        show cliohna angry at cliohnaright with dissolve
        cl "She has been pestering me for information on the Sea Naga… Very well. I shall provide it to her, and explain it was your arguments that convinced me it was something worth pursuing."
        show rowan necklace shock at midleft with dissolve
        ro "Why does Jezera need information on Sea Nagas?"
        show rowan necklace neutral at midleft with dissolve
        show cliohna neutral at cliohnaright with dissolve
        cl "I imagine for the same reason she needed data on any of the dozen minor racial groups she asked me about in the past."
        cl "Whatever it is, is anybody’s guess. Jezera as always tries to be enticingly mysterious, which is one of the primary reasons why she’s so obnoxious to work with."
        $ change_favor('jezera', 3)
        $ cliohnaBoon += 1
        jump boonCount2
        
    "Favour with Andras." if AndrasFavourNotPicked:
        $ released_fix_rollback()
        $ AndrasFavourNotPicked = False
        cl "He did wish to have detailed information on Qerazel needle traps… I will provide it to him, explain it was your insight that helped create an operational prototype."
        ro "Should I know what that is, in case he asks about them?"
        cl "There is no need. I will simply relay the information to him soon after you depart from Castle Bloodmeen. By the time you return, he will have moved to a different project, as he always does."
        $ change_favor('andras', 3)
        $ cliohnaBoon += 1
        jump boonCount2
        
    "Magic equipment for the orcs." if EquipmentNotPicked:
        $ released_fix_rollback()
        $ EquipmentNotPicked = False
        cl "..."
        show rowan necklace happy at midleft with dissolve
        ro "Is this a complaint I am about to hear?"
        cl "We have a deal. I will abide by it." 
        show rowan necklace neutral at midleft with dissolve
        cl "I will place some basic enhancement on their equipment, though the psychological impact of doing so is likely to exceed the actual increase in power."
        ro "As long as they fight harder, that’s all I care for. "
        #Increase the basic fighting value of a single orc a little - TODO (more orcs for now)
        $ castle.buildings['barracks'].troops += 5
        $ cliohnaBoon += 1
        jump boonCount2
        
    "Drider conditioning." if castle.buildings["pit"].lvl >= 1 and DriderConditioningNotPicked:
        $ released_fix_rollback()
        $ DriderConditioningNotPicked = False
        show cliohna angry at cliohnaright with dissolve
        cl "… If Draith manages to hold a conversation with me for longer than ten minutes without running away, I could arrange for something of the sort." 
        show cliohna neutral at cliohnaright with dissolve
        cl "Driders are simple creatures, easy to manipulate. Increased suggestibility during their formative years should do wonders for their training."
        #Increase drider power - TODO (more driders for now)
        $ castle.buildings['pit']._driders += 3
        $ cliohnaBoon += 1
        jump boonCount2
        
    "Decide later.":
        $ released_fix_rollback()
        if cliohnaBoon > 0:
            ro "What if nothing else comes to mind at the moment?"
        else:
            ro "What if nothing comes to mind at the moment?"
        cl "Then I am afraid I will have to insist on you picking the first you can think of."
        cl "This… Debacle is proving detrimental to our working relationship. It will be best we resolve it here and now."
        "With a sigh, he nodded in agreement. He could only imagine what continued arguments would do to them."
        jump boonCount2
        
label postBoon2:
    
show cliohna happy at cliohnaright with dissolve

cl "And that, I believe, is a suitable compensation for your troubles."

show rowan necklace concerned at midleft with dissolve

ro "I suppose. I’ve gone through harsher trials for less."

show rowan necklace happy at midleft with dissolve

cl "And more await on the horizon. If it’s any consolation, I expect our working relations to be less turbulent from now on. "

ro "Back to “business as usual”."

show rowan necklace concerned at midleft with dissolve

ro "… Which is a strange thing to say about conquering the world."

show rowan necklace happy at midleft with dissolve

"She flashed him a small smile, and for a moment, he wondered about what could’ve been."

scene black with fade

"Then he bid her farewell, and turned his mind to the thousand things that always needed his attention."

$ change_relation('cliohna', 5)
$ cliohnaRomance = False
return

################################################################################################################
################################################################################################################
################################################################################################################

label shaya_capital:

scene bg6 with fade
show rowan necklace neutral at midright with dissolve

"Rowan stopped not far from his desk. Normally, when he got to the office, he didn’t expect to find a woman at his desk." 
"...Especially not one who normally was at work in the brothel."

show shaya neutral at midleft with dissolve

sha "Rowan, you honour me with your presence."

"She gave a small bow, sweeping her arms to the side. Rowan approached cautiously."

if shayaSex == True:
    "Rowan stood to the side of the desk and relaxed into a playful smile."
    ro "You’re the one doing me an honor. My desk is two thirds more lovely for your presence."
    "Rowan thought he saw her smile beneath her veil. But, with Shaya he could never be quite sure."
    
else:
    "Rowan stood to the side of the desk and crossed his arms. While it was rare for any to speak a bad word against her, that didn’t mean he could trust Shaya. She was Jezera’s creature and everyone knew it."
    
ro "So why have you come to visit me? Surely my kingdom of paperwork is a bit dull for a woman used to the silks of your establishment."   

"She cocked her head to the side. From the corner of his eye, he thought he saw her finger tracing one of the documents on his desk."

sha "Boring? You’re too modest. This is the nerve centre of an empire. "
sha "My training in words and numbers were somewhat minimal compared to more practical arts. But, my managerial position has given me new appreciation of the kind of work you do."
sha "You are quite the man, Lord Rowan."

"Rowan nodded. Her words were...exaggerated, perhaps. But, he’d never really thought of Shaya as an administrator before. But, it wasn’t like managing the budgets and schedules of a brothel was an easy task. "

ro "Surely you didn’t come here just to waste your day sweet talk me though?"

sha "It would be no waste of a day, Rowan. But, you are correct. I have actually come to bring an opportunity to your attention."
sha "A frequent customer of ours is a businessman from the east. Between the silks, many secrets come out. And my girls have informed me that he’s in desperate need for investors in a particular merchant project."
sha "A good boy. A bit dull in the sack, so I’ve heard. But, he has an excellent reputation for business management in the city."
sha "He’s been struggling to raise capital in Qerazel for the trade route, because they doubt his ability to bring in the needed materials. It is one thing to run a business, and another to bring goods from one end of the continent to the other safely."

"Rowan scratched his chin. The moment the conversation shifted to business, it was as though there was a little click in his head."

ro "But, it’d be a surefire investment if he had access to our trade network?"

sha "My dealings with the goblin matron have been limited, but surely she could be persuaded to participate if offered a cut."

ro "Cla-Min? Yeah, so long as she got her cut."
ro "So, you’re telling me that you want us to take on the role as principal investor, but ensure it works by using our portal network."
ro "This would take spending some of the treasury though."

"Shaya bowed her head."

sha "If you believe it wise, Lord steward."
sha "From the estimations I received, the cost of a buy in would be 100G. A cut would return to the castle weekly from there. We could continue to collect dividends for a further 20 weeks. A profit of double the initial cost."

"Rowan paced softly behind the desk. If Shaya could be trusted on this account, then there would be valuable potential windfall. And whatever else was uncertain about the woman, her loyalty to Jezera was not."
"Still, it would require forgoing a portion of the castle’s current funds. Not always the wisest prospect in wartime..."

menu:
    "Invest in Shaya's customer." if castle.treasury > 100: 
        $ released_fix_rollback()
        ro "Very well. I will have to review our finances and your contact’s plan for the operation. But, provided everything is in order, you can expect the money."
        "Shaya rose from Rowan's seat and gave a larger bow, arms spread to her side. For a moment, Rowan was left to stare. Even the simple gesture has a catlike grace to it. Someone had taught her how to bow once, no doubt…"
        sha "You needn’t worry. I will ensure everything goes smoothly...and that our new business partner understands the risks associated with a lack of repayment."
        sha "I shall draw up the papers for review."
        "Rowan took back his seat and gathered his papers. Shaya was still here, but he was already in the process of considering the present state of the ledger."
        sha "Tell me Rowan, are you the type who desires a goodbye kiss?"
        "Her eyelashes fluttered."
        ro "I do not think that will be necessary at this moment. Thank you for bringing this to my attention though, Shaya. You’ve been a great help."
        sha "I live to serve."
        hide shaya with moveoutleft
        "The brothel keeper gathered her silks to her and slowly made her way from Rowan’s workplace. For a moment, Rowan’s eyes were drawn to the sway of her hips as she walked."
        "Rowan sighed and leaned back into his chair."
        #lose 100 gold - TO DO
        #gain +10 gold a week for 20 weeks
        return

    "Decline her offer.":
        $ released_fix_rollback()
        ro "I can’t spare the expenses, Shaya. I’m going to have to refuse my seal of approval on this one."
        ro "We’re in the middle of a war. Investments of that sort are the luxury of idle income."
        if castle.treasury < 100: 
            "Shaya studied him closely with her dark eyes. She rose from the chair slowly."
            sha "You cannot afford it. Can you?"
            ro "Am I really so easy to read?"
            sha "You’re a man. Of course, you are."
            "Rowan retook his seat and sighed. Had he actually tipped her off? Internally he reviewed what he’d said prior."
            ro "The point is moot though. We can’t pay for it. So my answer stands."
        "Shaya lowered her head slightly."
        sha "Of course, Lord steward. If that is what you believe best."
        hide shaya with moveoutleft
        "She didn’t stay or try to argue for her idea any further. With the grace of a woman used to rejection, she gave Rowan a respectful bow and then departed the room."
        "Rowan gathered up the papers on his desk. Work still needed to be done."
        return
        
