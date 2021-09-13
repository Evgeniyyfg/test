
label arzyl_dialogue:

if arzylDialogueStage == 1:
    jump arzyl_first_dialogue

if arzylDialogueStage == 2:
    jump arzyl_nileth

if arzylDialogueStage == 3:
    jump arzyl_isdruel

else:
    jump arzyls_gift


label arzyl_first_dialogue:

scene bg7 with fade

"Rowan stopped at the entrance to Arzyl’s chambers, the sound of low chanting drifting through the doorway. The lyrical tune of her voice carried a strange resonance, and his head buzzed as he pressed onwards through the entryway."
"The pale Elf sat cross-legged in the center of the room, her blank white eyes glowing as her full lips mumbled a haunting chorus low under her breath. She seemed to be almost in a trance, her head bowing low as she huddled forward. "
"At the sound of Rowan’s arrival her head snapped up, her lidless gaze swiveling to focus upon the human intruder. A wide smile spread across her face; Rowan could have sworn her body posture was intended to entice him with her hanging, milky cleavage."

show arzyl neutral at midright with dissolve

arz "Rowan! I was just thinking of you."
                                                                                                                                                                                                                                                               
show rowan necklace neutral at midleft with dissolve

ro "No doubt while chanting a paralyzing spell."

#arz happy

arz "Oh, I don’t think so. I took the lead {i}last time{/i}. Now it’s your turn to prove yourself worthy of me!"

ro "Don’t hold your breath on that."

arz "Why would I? I’d prefer to have you take it away from me."

ro "..."

arz "Oh, don’t give me that look Rowan! Can you honestly say that I was the first being in Solance to try such a maneuver on you?"

show rowan necklace angry at midleft with dissolve

ro "No. But that doesn’t make it right."

#arz neutral

arz "Maybe not, but neither was Whitescar’s attempt to corner you like a wounded animal in that canyon, don’t you think?"

show rowan necklace neutral at midleft with dissolve

ro "How do you know about that?"

arz "I know much more than you might think, Rowan. "
arz "About you. About the Twins. About… "

#arz happy

arz "Your wife."

show rowan necklace angry at midleft with dissolve

ro "Tread lightly with your next words, Arzyl. I don’t respond well to threats."

arz "Oh, sweet Rowan: I would never dream of such a thing!"


"The statuesque Elf stood up from the ground, smiling at the long look Rowan gave to her jiggling mammaries as she rose. She strode with a seductress’ walk over to him, her lips pursed as she slid comfortably to his side."

#arz neutral

arz "Now: what can I do for you?"

$ arzylDialogueCount = 0
$ arzylFirstQ = True

label aryzlDialogueMenu:
show rowan necklace neutral at midleft with dissolve

menu:
    "What is the Midnight Court?":
        $ released_fix_rollback()
        if arzylFirstQ == True:
            $ arzylDialogueCount += 1
            arz "We are the Eternal Heirs of the Outer Spheres, the Imperators of a New Era, Witches and Warlocks of the Third Path."
            arz "We are the Drach’Hyl, the twice-born, and we are the rightful rulers of this world."
            ro "Yeah? And I’m the Baron of Rosaria."
            #arz happy
            arz "Now now, Rowan! There’s no need to be rude."
            #arz neutral
            arz "We are a Cabal of the most powerful of the Fae, those unbound by the rule of that Golden Dragon that the Red Sun Alliance obsequiously worships.  We broke free from his tyranny centuries ago, and now govern ourselves as we see fit."
            arz "We are led by her grace, Queen Kassandra. Firstborn and most beloved of the true Fae. For she alone of the first Fae understands that there is only one thing in this world that truly matters:"
            arz "Power, and the means to acquire more."
            ro "Alliances made purely for the sake of power are rarely worth the paper they’re printed on."
            #arz happy
            arz "A marriage of convenience is preferable to lonely impotence, wouldn’t you agree Rowan? Especially when that marriage comes with so many… ‘convenient’ perks."
            "Rowan’s mouth twisted in distaste as he felt the ageless Fae’s long fingertips slide down his arm, drifting inexorably towards his genitals. He took a purposeful step back, which caused Arzyl to let out a lilting laugh."
            $ arzylFirstQ = False
            menu:
                "What Races are in the Midnight Court?":
                    #arz neutral
                    arz "Only one. The Fae."
                    ro "That’s blatantly untrue. I have seen your servants around the castle: Elves, humans, even a Goblin or two."
                    #arz happy
                    arz "Oh ho! For all your heroic sensibilities, you really can be short sighted in your judgement. Those beings you saw {i}looked{/i} like Humans and Elves, I’ll grant you that."
                    #arz neutral
                    arz "But I can assure you: they are Fae, just as I am."
                    arz "Have you never wondered about the old folk legends? Of entire villages’ slumbering children being abducted from their beds in the middle of the night by spirits of the woods?"
                    ro "They’re children’s tales. Fiction and fantasy."
                    #arz happy
                    arz "Exaggerated, yes. Fantasy, no. The ones we abduct are the {i}Nekarae{/i}, “host vessels.” Unlike the Red Sun Alliance, the Midnight Court chooses to possess sapient beings."
                    #arz neutral
                    arz "The spiritual merge that occurs anchors the Fae to this adopted realm, granting the host unending life, and the Fae spirit a permanent body to reside in. We do not suffer the same ills that the false Fae do."
                    ro "...And the hosts themselves?"
                    #arz happy
                    arz "Is immortality really such a terrible thing? What is the cost spiritual freedom in comparison to eternal life?"
                    ro "So are there no other races in the Midnight Court at all?"
                    #arz neutral
                    arz "We are a single people, and have little use for the lesser races of the world. The Glades of the Midnight Court are our playground, far removed from the mortals of Solanse. "
                    arz "We are visited on occasion by the odd adventurer or ambitious Warlock, seeking knowledge, or power, or simply a test of their skills."
                    #arz happy
                    arz "It does not matter their reasons: to step into the forbidden Glades is to make one’s life forfeit."
                    jump aryzlDialogueMenu
                    
                "Is it true that the Midnight Court mates with demons?":
                    "A deep, menacing smile spreads across the Fae’s face. Her eyes seem to gleam with a malicious light as she fluttered her eyelashes at him."
                    #arz happy
                    arz "My, aren’t {i}you{/i} a curious sort. Is this question a subtle attempt to ask if the Fae will copulate with anyone?"
                    ro "Just answer the question."
                    #arz neutral
                    arz "Very well. The short answer? Yes. We will mate with Demons. We’ll also mate with Elves, Orcs, Minotaurs and even {i}Dragons{/i} - if it suits our needs."
                    ro "Why?"
                    arz "Silly boy, the answer is as obvious as it is self evident. Why does a beautiful Noblewoman have an affair with an Elderly King? Why do the street-walking whores of your squalid cities choose to bed strangers?"
                    arz "To get something out of it. Pleasure can be a purpose unto itself. The Demons have sired many of our progeny in the past, and will doubtless do so again, should this Alliance conclude to our satisfaction."
                    arz "Sex is a tool. A delightful one, to be sure: but a tool nonetheless."
                    jump aryzlDialogueMenu
                    
                "Why is the Midnight Court at odds with the Red Sun Alliance?":
                    #arz angry
                    arz "They are the false Fae, alien spirits of an alternate dimension who abandoned their own customs to follow the clarion call of that Glimmering Lizard and his drooling sycophants."
                    arz "My Queen, her Grace Kassandra herself, was the first of the Realm-born: a Fae spirit born from the loins of another Fae in this reality. She was the first to recognize the Dragon’s tyranny for what it was."
                    #arz neutral
                    arz "She led a revolt, and freed her most loyal followers from the clutches of that beast’s enslavement spell."
                    ro "..the Dragon enslaved you?"
                    arz "Imagine if you will, Rowan: a desperate people, spirits of a dying reality, cast adrift in the currents and eddies of the great void between dimensions."
                    arz "When out of the ether there comes a voice: “I can save you.” it says, “I can give you life, love, happiness and peace. All you need to do is swear fealty to me, and tie your very essence with my own."
                    #arz angry
                    arz "-And now picture the rage we felt when that promise turned out to be a lie."
                    jump aryzlDialogueMenu
                    
        else:
            menu:
                "What Races are in the Midnight Court?":
                    #arz neutral
                    arz "Only one. The Fae."
                    ro "That’s blatantly untrue. I have seen your servants around the castle: Elves, humans, even a Goblin or two."
                    #arz happy
                    arz "Oh ho! For all your heroic sensibilities, you really can be short sighted in your judgement. Those beings you saw {i}looked{/i} like Humans and Elves, I’ll grant you that."
                    #arz neutral
                    arz "But I can assure you: they are Fae, just as I am."
                    arz "Have you never wondered about the old folk legends? Of entire villages’ slumbering children being abducted from their beds in the middle of the night by spirits of the woods?"
                    ro "They’re children’s tales. Fiction and fantasy."
                    #arz happy
                    arz "Exaggerated, yes. Fantasy, no. The ones we abduct are the {i}Nekarae{/i}, “host vessels.” Unlike the Red Sun Alliance, the Midnight Court chooses to possess sapient beings."
                    #arz neutral
                    arz "The spiritual merge that occurs anchors the Fae to this adopted realm, granting the host unending life, and the Fae spirit a permanent body to reside in. We do not suffer the same ills that the false Fae do."
                    ro "...And the hosts themselves?"
                    #arz happy
                    arz "Is immortality really such a terrible thing? What is the cost spiritual freedom in comparison to eternal life?"
                    ro "So are there no other races in the Midnight Court at all?"
                    #arz neutral
                    arz "We are a single people, and have little use for the lesser races of the world. The Glades of the Midnight Court are our playground, far removed from the mortals of Solanse. "
                    arz "We are visited on occasion by the odd adventurer or ambitious Warlock, seeking knowledge, or power, or simply a test of their skills."
                    #arz happy
                    arz "It does not matter their reasons: to step into the forbidden Glades is to make one’s life forfeit."
                    jump aryzlDialogueMenu
                    
                "Is it true that the Midnight Court mates with demons?":
                    "A deep, menacing smile spreads across the Fae’s face. Her eyes seem to gleam with a malicious light as she fluttered her eyelashes at him."
                    #arz happy
                    arz "My, aren’t {i}you{/i} a curious sort. Is this question a subtle attempt to ask if the Fae will copulate with anyone?"
                    ro "Just answer the question."
                    #arz neutral
                    arz "Very well. The short answer? Yes. We will mate with Demons. We’ll also mate with Elves, Orcs, Minotaurs and even {i}Dragons{/i} - if it suits our needs."
                    ro "Why?"
                    arz "Silly boy, the answer is as obvious as it is self evident. Why does a beautiful Noblewoman have an affair with an Elderly King? Why do the street-walking whores of your squalid cities choose to bed strangers?"
                    arz "To get something out of it. Pleasure can be a purpose unto itself. The Demons have sired many of our progeny in the past, and will doubtless do so again, should this Alliance conclude to our satisfaction."
                    arz "Sex is a tool. A delightful one, to be sure: but a tool nonetheless."
                    jump aryzlDialogueMenu
                    
                "Why is the Midnight Court at odds with the Red Sun Alliance?":
                    #arz angry
                    arz "They are the false Fae, alien spirits of an alternate dimension who abandoned their own customs to follow the clarion call of that Glimmering Lizard and his drooling sycophants."
                    arz "My Queen, her Grace Kassandra herself, was the first of the Realm-born: a Fae spirit born from the loins of another Fae in this reality. She was the first to recognize the Dragon’s tyranny for what it was."
                    #arz neutral
                    arz "She led a revolt, and freed her most loyal followers from the clutches of that beast’s enslavement spell."
                    ro "..the Dragon enslaved you?"
                    arz "Imagine if you will, Rowan: a desperate people, spirits of a dying reality, cast adrift in the currents and eddies of the great void between dimensions."
                    arz "When out of the ether there comes a voice: “I can save you.” it says, “I can give you life, love, happiness and peace. All you need to do is swear fealty to me, and tie your very essence with my own."
                    #arz angry
                    arz "-And now picture the rage we felt when that promise turned out to be a lie."
                    jump aryzlDialogueMenu
                
    "What is your role in the Midnight Court?":
        $ released_fix_rollback()
        $ arzylDialogueCount += 1
        "Arzyl laughs, putting a hand over her mouth as if to chastely conceal her humor. Her sultry look puts lie to the act, though. The Fae leaned forward just slightly, her heaving bosom front and center. Rowan felt a stirring in his groin."
        #arz happy
        arz "It is whatever I choose it to be. We are not the hierarchical taskmasters that the Red Sun Alliance is. Each member of the Court is an individual: a singular, unique soul."
        #arz neutral
        arz "I am one of the greatest of the true Fae, the Queen’s most trusted servant. Thus, she asked that I come here as a favor, and represent her interests in this delicate time."
        arz "I have no title, nor any true authority save that which I am willing to stake my life upon. If Queen Kassandra does not like the terms I return with…"
        #arz happy
        arz "Well, let’s just say that everyone has to answer for their actions in the end."
        "Despite the disturbing implication of her words, Arzyl seems jovial about the situation. Rowan quirked an eyebrow as she breezily ran her fingers through her hair, tossing it behind her shoulders."
        arz "We are living beings, Rowan. Not cogs in an infernal machine. The life we make is our own, for better or for worse. I bear no titles, save the ones I give myself."
        ro "Yet you represent the Midnight Court."
        arz "I look after the interests of the Midnight Court - and thus, my own interests as well. Anything beyond that is pedantic and unnecessary. My brothers and sisters can speak for themselves."
        jump aryzlDialogueMenu
            
    "Why did you ambush me with your servants?":
        $ released_fix_rollback()
        $ arzylDialogueCount += 1
        "Arzyl’s eyes brightened considerably. A slow, creeping smile spread across her cheeks."
        #arz happy
        arz "Why? Didn’t you enjoy our time together? If you are so eager to repeat the experience, my servants would be happy to oblige."
        show rowan necklace angry at midleft with dissolve
        ro "That’s not my point and you know it. You attacked me without provocation. Why?"
        #arz neutral
        arz "Mortals are such strange creatures: always seeking answers to questions far beyond the purview of their own ability to comprehend."
        arz "It is as if you are asking me: “Why do the rains come? Why does the storm collapse my hovel, but leave my neighbor’s safe and sound?”"
        arz "Content yourself with the fact that I chose you for a reason, and that the outcome was even better than I expected!"
        #arz happy
        arz "After all: I could have just as easily cut your throat, had I wished to. The fact that you even have the opportunity to demand answers from me should be an answer unto itself."
        jump aryzlDialogueMenu
            
    "Who leads the Midnight Court?":
        $ released_fix_rollback()
        $ arzylDialogueCount += 1
        #arz happy
        arz "Queen Kassandra, her most illustrious Grace. Lady of the Fae, Royarch of Beauty, and Goddess of the Freeborn."
        ro "That’s a lot of titles for a woman I’ve never heard of."
        #arz neutral
        arz "And that’s precisely why she still bears them, after thousands of years of turmoil and strife."
        arz "If the lesser races knew of her beauty, it would cause a war of such titanic proportions that the very firmament of the sky would collapse."
        ro "Bold words for a myth. If she’s anything like her servants, I doubt that ‘beauty’ sinks deeper than the skin."
        #arz happy
        arz "Ha ha! Oh Rowan, if you were in her clutches right now, you would not even have the breath to scream."
        jump aryzlDialogueMenu
            
    "I have no further questions for you." if arzylDialogueCount > 3:
        $ released_fix_rollback()
        arz "You do, you simply lack the knowledge to ask them, yet. All in due time though."
        ro "Just make sure you avoid using that sorcery on me while you’re here, Arzyl."
        #arz happy
        arz "Of course! I have no doubt that your masters would be resentful if I interfered with their favorite toy."
        show rowan necklace angry at midleft with dissolve
        ro "...!"
        ro "At least I am not begging them on bended knee, prostrating myself like a common whore, praying that their ‘toy’ chooses them to be the latest of their easily-discarded allies."
        arz "Oh, Rowan. Now you’re just making me blush."
        arz "I think we’re going to get along just fine."
        $ arzylDialogueStage = 2
        return


#############################################################################################################################################################

label arzyl_nileth:

$ arzylDialogueStage = 3

scene bg9 with fade

"Rowan awoke in the middle of the night to the sight of pale, glowing eyes staring at him in the dark."

show rowan necklace naked concerned behind bg9

ro "{i}Guh!{/i}"

hide rowan
show rowan necklace naked concerned at midleft with dissolve

"He leapt out of bed, his heart pumping as the figure in the darkness snapped her fingers. A purple, flaming light erupted in the palm of her hand, casting her face in the cover of flickering shadows."

show arzyl neutral at midright with dissolve

arz "Rowan. Come. The Midnight Court has need of you."

show rowan necklace naked angry at midleft with dissolve

ro "What the {i}hell{/i} are you doing in my room at this time of night?!"

arz "There is no time. I heard a psychic call upon the wind. My acolyte, Nileth is in trouble."

show rowan necklace naked neutral at midleft with dissolve

ro "What are you talking about?"

arz "I dispatched Nileth to the castle to give him a report on the state of things with the Twins. But it seems he has run into a band of their Orc servants, near the base of the mountain."
arz "He thinks that they intend him harm. If we do not intervene now, there may be severe consequences… for everyone involved."

ro "Then go handle it! Why are you waking me up at Gods-know what time to tell me this?"

#show arzyl happy at midright with dissolve

arz "Oh, Rowan. I thought you’d know me better by now."
arz "If {i}I{/i} go down there, the only thing left in my wake will be bodies. As detestable as the Orcs are as a species, killing the Twins’ servants would not endear them to me much at all."
arz "Don’t you think a ‘softer’ touch is needed here?"

menu:
    "Yes.":
        $ released_fix_rollback()
        jump orcsNileth
        
        
    "No.":
        $ released_fix_rollback()
        ro "Deal with it your damned self, woman. It is the middle of the night."
        "If his anger had any effect on the pale elf, she showed no sign of it. Her lips curled into a smirk that sent a chill down his spine."
        arz "Very well Rowan, but do not come running to me if you do not like the outcome."
        hide arzyl with dissolve
        "With that, the witch disappeared, leaving him stood alone in his chambers. He didn't learn what happened that night, but in the morning he discovered two orcs were missing, neither were ever seen again."
        $ castle.buildings['barracks'].troops -= 2
        return

label orcsNileth:

show rowan necklace naked angry at midleft with dissolve

ro "All right! Damn it! At least let me get some clothes on!"

arz "Oh don’t mind me, Rowan! I’m just admiring the view."

ro "Ugh."

show rowan necklace neutral at midleft with dissolve

"Rowan threw on his travel cloak and shoved his sword into his belt. He kept his eyes upon the shifty Fae and her imperious smile, wondering to himself if this was just another in the long line of the endless mind games she loved to play on him."

#outside bloodmeen BG
scene black with fade

"Rowan followed the nebulous Fae’s instructions, picking his way down high embankments and rock-strewn crevices to reach the base of the mountain upon which the Bloodmeen Castle perched. As he reached at last a bend in the road he overheard the sound of voices."

show orc soldier neutral at midright with dissolve

os "Wots dat sound?"

show wild orc neutral at edgeright with dissolve

wo "Wot sound? You get nogged ur someden? Is just dis coward wimperin! Heh heh."

#nileth scared
show nileth neutral at edgeleft with dissolve

nil "You uncultured swine! S-stay back! I am the acolyte of Arzyl herself!"

os "Acka-who?"

wo "Wots an “Arr-zeal?”"

dag "She’s your worst nightmare, you green skinned gits!"

"Rowan’s eyes were drawn to the small, impish creature caught in the grasp of one of the Orcs. He was tiny, fitting into the palm of the creatures’ hand as he struggled in futility to free himself."

dag "Do as you please with that jizz-swilling toadie - Sol’s Bones, he may even like it! But leave me out of it, or Queen Kassandra will hear of this!"

os "Imp talks too much. {i}*Squeeze*{/i}"

dag "{i}Gak!{/i}"

nil "Please good sirs: I am a diplomatic representative, here to meet with the Midnight Court’s ambassador to the Twins, your mighty rulers."
nil "I only ask that you allow us safe passage, as becoming of a diplomatic mission of such importance."

wo "Hah! It talks more dan ‘da Imp duz!"

nil "...“it?”"

os "Da way ‘e uses his mouth, ‘e’s more girl than boy."

wo "Wot? It not girl? It {i}shaped{/i} like girl!"

dag "He’s got a {i}dick{/i}, you assholes!"

os "Yap, e’s a girl, no mistakin it."

wo "I dunt believe ya."

os "Well, dere’s only wun way ta find out!"

nil "Oh, goodness! I didn’t even lube myself!"

"The two Orcs chuckled, menacing upon the poor, Fae twink. Rowan saw his chance: the Orcs were distracted, too busy pulling aside their loincloths to bother looking in his direction. Rowan watched as Nileth halfheartedly shrinked back from the two of them."
"Rowan could take this opportunity to confront the Orcs and prevent any ‘harm’ from befalling Nileth (though truth be told: it seemed less ‘harmful’ and more sexual. And even Nileth didn’t seem {i}that{/i} frightened.)"
"As the first Orc produced his member, shoving directly in Nileth’s face."

menu:
    "Intervene.":
        $ released_fix_rollback()
        "Rowan gritted his teeth. He couldn’t just sit by and watch this helpless being be menaced by the Twins' lackeys. He stood to his feet, stalking over to the two Orcs as they loomed over the Fae creature."
        show rowan necklace neutral behind black
        ro "Stop!"
        hide rowan
        show rowan necklace neutral at center with moveinleft
        wo "Wot?"
        ro "What is the meaning of this? What are you two guards doing with that man?"
        os "E’s more of a girl than a git, boss."
        show rowan necklace angry at center with dissolve
        ro "I don’t care if he’s a bloody busty succubus! Unhand him immediately!"
        "The two Orcs shared an uncertain look, staring stupidly into one another’s eyes in hopes that the other might take charge and defy Rowan’s order. Seeing that neither was taking the bait, both stepped back from Nileth."
        dag "Finally! Someone with a lick of sense! Thanks, effeminate stranger!"
        "Rowan had to bite his tongue to not strike the impudent imp. Brushing aside the two Orc Guards, he knelt in front of Nileth, offering his hand to pull him to his feet."
        show rowan necklace happy at center with dissolve
        ro "I apologize for my master’s servants. They can be a bit energetic in their efforts to defend our borders."
        nil "Th-that’s quite all right, Sir."
        "Nileth’s face flushed and he glanced away, unable to properly meet Rowan’s eyes. It was vaguely charming. Rowan reached out and took the demon twink by the wrist, pulling him to his feet."
        show rowan necklace neutral at center with dissolve
        ro "I guarantee that you will not be accosted. Do you think you can reach your lady’s chambers from here?"
        nil "Y-yes, I can feel her presence. I uh… I don’t need an escort or anything."
        "Judging from the way he blushed, Rowan wondered if he was more terrified of Rowan’s presence than he was the Orcs'."
        ro "I am sure we will be seeing more of each other in the coming days."
        ro "Guards, I want the two of you to escort Nileth to Arzyl’s chamber and ensure he reaches there with no more… issues."
        "Rowan planted his hand upon the pommel of his sword."
        ro "If I find out that it was anything to the contrary, I will personally make a point of finding and punishing the ones who did it. Am I clear?"
        os "Yes, boss."
        wo "Count on us."
        show rowan necklace angry at center with dissolve
        ro "I don’t. But you {i}can{/i} count on the consequences. Now begone."
        nil "Thank you, Sir."
        show rowan necklace happy at center with dissolve
        ro "It’s Rowan. And it was my pleasure, Nileth."
        dag "Yeah yeah, let's get goin’ you glorified sex toy. Lady Arzyl’s lookin’ for us."
        "Rowan made a point to watch as the Orcs led their former victim back towards the Castle. He caught glimpse of Nileth stealing long glances over his shoulder before disappearing inside. He let out a sigh and resolved to keep a closer eye on the guards from now on."
        return
    
    "Stay hidden and see where this goes.":
        $ released_fix_rollback()
        "Rowan decided to observe the unfolding action, keeping hidden till he felt certain he should intervene. He watched as the two Orcs continued with their plans unmolested. The Orc not holding Daggertongue reached down and roughly fondled the androgynous Fae’s crotch."
        scene cg439 with fade
        show wild orc neutral behind cg439
        show orc soldier neutral behind cg439
        #nileth aroused
        show nileth neutral behind cg439
        pause 3
        nil "{i}Ah!{/i}"
        wo "Hah! Its fer sure a ‘he!’ I felt his lil’ cock!"
        nil "Nnngh!"
        "The Orc continued to fondle the Fae, his leering grin growing as Nileth blushed and looked away. The other Orc let out a boisterous guffaw, holding up Daggertongue face to face with Nileth so that he could see his humiliation."
        os "Imp bitch get to see Fae bitch squeal!"
        dag "I’m gonna make you squeal out your {i}intestines{/i} once I’m done with y- {i}gak!{/i}"
        "As the Imp struggled in his new owner’s grasp, Nileth gasped, his girlish face twisting with repressed lust as the Orc’s hand began to move faster. He squirmed back and forth, but was unable to escape the creature’s thick hand."
        "He pumped him back and forth, his brutish fingers closing about the Fae’s crotch in a vice-like grip as the other Orc loomed over him."
        "Nileth’s pale eyes stared up, his lower lip trembling as the Orc pulled aside his loincloth, revealing the green, pulsating cock beneath. He was already rock hard, his erection jabbing forth to poke Nileth in the cheek. The pale-skinned trap let out a simpering wimper."
        scene cg440 with fade
        show wild orc neutral behind cg440
        show orc soldier neutral behind cg440
        #nileth aroused
        show nileth neutral behind cg440
        pause 3
        os "Time fer sum fun."
        "The Orc took himself in hand, laughing as he began to jerk in front of Nileth’s face. Emboldened by his companion, the second Orc soon followed suit: releasing Nileth’s pitifully small cock as he ripped his own loincloth clean off. Nileth shivered, the air heavy with the musk of superior masculinity." 
        "Nileth’s face was red, his eyes flicking back and forth from dick to dick as he licked his luscious, cocksucking lips. There was a low heat in the air, a sort of erotic tension that made the scene seem less like an inflicted punishment and more a debauched fantasy of domination."
        "Even Nileth was rock hard, his cock pointing straight up from his outfit."
        wo "You like dis, girl?"
        nil "N-no! And I’m a man!"
        os "Mmm, yeah ya do. Lick it, girl."
        "The Orc responded to Nileth’s protestations by rubbing his dribbling cockhead across his face. Nileth grimaced but did not push him away, groaning as the Orc spread precum under his nose."
        show cg441 with dissolve
        show wild orc neutral behind cg441
        show orc soldier neutral behind cg441
        #nileth aroused
        show nileth neutral behind cg441
        pause 3
        "Against his better judgement Nileth took a deep whiff, shuddering as he planted a short, hesitant kiss upon the cock."
        os "Dats right. You like bein held down, dontcha?"
        nil "No… n-no I don’t…"
        wo "She’s a shy one. Wot say we give her wot she wants?"
        show cg441 with sshake
        show cg441 with sshake
        scene cg442 with flash
        show wild orc neutral behind cg442
        show orc soldier neutral behind cg442
        #nileth aroused
        show nileth neutral behind cg442
        pause 3
        nil "Eeek!"
        "Nileth closed an eye as a long string of pearlescent spunk squirted up along his face. The second shot threaded across his nose, his downcast eyes squeezing tight to keep the sloppy load from getting in them."
        "The Orcs grunted, their heavy breathing heralding new jets of cum to come roaring forth. Soon Nileth’s face was caked in the stuff, the shameful residue of stronger males coating him like a lurid christening. He groaned, unintentionally licking his lips and getting some of the creamy cum on his tongue."
        os "She looks good dis way."
        wo "You ever want to come ‘round here again, you just ask."
        nil "I-I… I wont…"
        os "Heh. We heard dat one before."
        "Laughing, the two Orcs unceremoniously dropped the struggling Imp to the ground and left, whistling an off-key tune as they moved on with their patrol."
        "They did not spare so much as a half-glance in the direction of the thoroughly-humiliated Fae, who picked himself up off the ground only after waiting to be sure that they were gone."
        nil "Ugh… mmph. S-stupid Orcs."
        nil "...What’s Arzyl going to say? I couldn’t even take on a pair of brutes!"
        dag "I dunno dick-lips, but you can be damn sure {i}I’m{/i} not getting in trouble with this!"
        "Realizing that his opportunity to intervene had come and gone, Rowan wisely decided to simply fade back into the brush. At this point, it was probably better to tell Arzyl that he simply wasn’t able to find the Fae twink at all, otherwise he doubted she’d take kindly to him in the future for letting it happen."
        return


###############################################################################################################################################################

label arzyl_isdruel:

$ arzylDialogueStage = 4

scene bg13 with fade

"Rowan entered Arzyl’s dank chambers, the dying candles casting the room into a murky darkness like the inside of a witches cauldron. He found the Fae pacing the room, a tense expression across her ageless features."

show rowan necklace neutral at midleft with dissolve

ro "Hello again, Witch."

show arzyl neutral at midright with dissolve

arz "Give me a moment, Rowan. I am just about to receive word."

ro "...Word of what? From who?"

"Before Rowan could inquire further, there was a flash of light. Suddenly, a note was in Arzyl’s hands. It was sealed with blood-red wax, an unintelligible symbol gracing its back that looked vaguely like three moons interlocking with one another."
"With a single, long {i}rip{/i} of her nails, Arzyl broke the seal. A small fount of magical power erupted out from beneath the seal, melting the wax away in a single instant. Arzyl folded open the letter, her glowing eyes skimming across its length as she read."

arz "..."
arz "I have been summoned by her Flawlessness, Queen Kassandra herself. It would appear that it's urgent."

ro "It must be, if she’d dare to send a sealed letter into the Twins’ own fortress."

"Arzyl spared a half smirk in Rowan’s direction before she began to pace the room once more."

arz "I never pass up a chance to meet with my beloved Queen. However, this does complicate matters a bit."
arz "Another member of the Court is headed here to the castle as we speak. I was supposed to meet her at the gate to ensure safe passage… unlike my sweet Nileth."
arz "She is being ‘delivered’ here soon."

ro "...Delivered?"

arz "The Midnight Court boasts many different kinds of Fae within its ranks, Rowan. She just happens to be more - {i}eccentric{/i} than most."

ro "Given what few Fae I’ve met who are a part of the Midnight Court, that’s saying something."

#arzyl happy
arz "Oh Rowan, you should know by now that I’m the most eccentric Fae you’ll ever meet! Isdruel just happens to be far less dignified about it than I."
arz "As a result, the Queen and I decided we needed to use some discretion in getting her here."
arz "But now the Queen wishes to speak to me! And I am quite loathe to deny her wishes. Would you be a dear and meet my sister Fae at the gate when she gets here? "
arz "I shudder at the thought of what she might do if she’s left… unattended."

ro "Well, I-"

arz "Oh! There is my Queen calling now!"

"Before Rowan could respond, a sudden blast of light blinded him. A swirling maelstrom of energy erupted from the ground at Rowan’s feet, a gleaming portal into Gods-know what. With a wink and a wave Arzyl stepped onto its surface, sinking like quicksand as the eldritch energy engulfed her."

arz "I promise I won’t be long, Rowan…"

hide arzyl with dissolve

"Her otherworldly smile stays in Rowan’s mind long after the ground swallowed her into nonexistence. He stood there for a moment in her room, contemplating his options."

menu:
    "Help Arzyl.":
        $ released_fix_rollback()
        jump helpArzyl
        
    "Don’t involve yourself.":
        $ released_fix_rollback()
        "Considering his options, Rowan decided that this was a classic example of ‘none of his business.’"
        "Given the Midnight Court’s disturbing propensity for sadism and cruelty, the thought of helping Arzyl ‘retrieve’ a servant deemed dangerous enough to have to send them in a sealed box set off warning bells in his head."
        "Rowan shrugged to himself, resolving to let the situation work itself out."
        return

label helpArzyl:

"Considering his options, Rowan decided that learning more about the Midnight Court and their baffling ways was worth the potential blowback of whatever Arzyl had just saddled him with. Besides: what’s the worst that could happen?"
"Rowan did his best to ignore the pit in his gut as he considered the actual implications of the question."

scene black with fade

"Hurrying to catch this newcomer before she waltzed in the front door unattended, Rowan reached the front gate of Castle Bloodmeen in record time. What he found waiting for him shocked him."

show rowan necklace shock at midleft with dissolve

ro "W-what the hell is going on?!"

"True to Arzyl’s words, her companion had been ‘delivered’ to the front gate in what appeared to have once been a sealed, runic crate of alien design. Rowan could see the shattered splinters of the thing lying in shards across the ground, its occupant now stood at the entrance, a picture of rage and spite."
"The pair of Orcs guarding the gateway had inadvertently opened the crate without asking permission, freeing the being within from her interminable confinement. Now free from her shackles, the bark-skinned creature had enacted her vengeance upon them."
"She was a creature of wood and vine, leaf and root. Her eyes were the color of sap, her hair like knotted brambles tangled together, her lips a curling, contemptuous oak. Though her body was feminine and curvaceous, she looked more akin to a living growth than a human."
"Her eyes swept across Rowan, a dark grin growing upon her lips. One Orc guard was laid out on the ground, his body splayed back with his eyes rolled into his head. Rowan bent down and checked the brute’s pulse. It was still going, if very faintly."
"The other Orc let out a roar of fear, dangling by the leg from a series of curling vines that emerged from the Dryad-woman’s body. Her cruel smile widened as she dragged a set of brambles across the struggling Orc’s body."

show orc soldier neutral behind black
os "Aaaaugh!"

show isdruel neutral at midright with dissolve

isdr "Yes, {i}yes{/i}! Feel it, you worm! Taste the delectable agony of my vines! "

"The Dryad rose up, floating upon a canopy of vines that bear her up to the high place she’s dangled the helpless Orc. The stupid creature flailed about, helpless in her grasp as she inflicted herself upon him. Her bark-encrusted hands roamed about the Orc’s green skin, pinching and groping at whatever struck her fancy."

isdr "You thought you’d use me, you little tick, didn’t you? First words out of your mouth when you saw me: ‘I’m gon’ fuck dat plant lady’ huh? Well {i}now{/i} who’s fucking who?"

"Her claws raked his back, the Orc twitching in place as he cried out in pain. Rowan winced. He approached the plant woman, whose amber eyes darted over to him as he approached."

isdr "Ah… Rowan. It has been a while."

show rowan necklace neutral at midleft with dissolve

ro "Have we… met?"

isdr "Oh, sweetling, you don’t remember your beloved Isdruel?"
isdr "That gang of villagers… that {i}brute{/i} with the crossbow and his army of lackeys who had stolen my sister’s mushrooms? Surely you’d at least recall the fight. "

if dryad_side == "isdruel":
    isdr "After all, you saved me like a blushing damsel in the fairy tales. You sexy thing."
    isdr "Arzyl really did give me a treat, sending {i}you{/i} of all people to greet me at the door!"

else:
    isdr "After all, you left me to fight those heathens on my own, despite their thieving manner."
    isdr "I did not expect a weakling like you to be the one Arzyl sent to fetch me."

ro "Well, she sent me. What are you doing to these guards?"

isdr "You mean these {i}brutes{/i}?!"

"Isdruel reached out, grasping the Orc’s upturned face by the chin as she leered down at his helpless expression. A dark smile graced her chlorophyllic lips."

isdr "I am teaching them some manners. Care to join in on the fun?"

show rowan necklace angry at midleft with dissolve

ro "I’ll pass."

isdr "A shame. Perhaps another time then. Something tells me that you could indulge in a bit of {i}domination{/i} better than most."

"As if to exemplify this fact, Isdruel let go of the Orc’s chin, her other hand curving around and slapping him hard in the face. The Orc wimpered, and Isdruel went eye to eye with him."

isdr "You. Do {i}not{/i}. Touch me without permission, worm!"

"She slapped him hard across the face again, her brambly vines dragging themselves across his back as the Orc’s face contorted in pain. There was a manic, almost sadistic look in the Dryad’s eyes." 
"Rowan felt a vague stirring in his gut: these were just Orcs, after all. Brutes who themselves had undoubtedly committed whatever atrocities they could in the early days of the Twins’ campaigns. Who was he to judge a bit of comeuppance? Then again, something about the Dryad’s pure malice made him feel…"

$ isdrWatchFailed = False

label isdrMenu:

menu:
    "Disgusted. Put a stop to this now, however you can!":
        $ released_fix_rollback()
        ro "Let the Orcs go Isdruel. {i}Now{/i}."
        isdr "Hehe, why?"
        "Rowan’s knuckles went white from his grip on his blade hilt. His scowl deepened as he saw Isdruel, her eyes matching with his, dragged her sharp fingernails down the Orc’s back in spiteful malevolence. Her smile widened as Rowan drew his sword."
        ro "Because if you don’t, I’ll hack you to pieces and use your bark for kindling."
        isdr "You flirt."
        "There was a long moment of tenseness, the two staring each other down as the Orc dangled in the air, whimpering in a desperate tone. At last Isdruel shrugged, her vines unravelling around the Orcs legs as he collapsed to the ground in a heap. Rowan did not let go of his sword."
        isdr "Funny, Arzyl said you {i}liked{/i} a girl who was into the rough stuff."
        ro "Then Arzyl is sorely mistaken."
        isdr "Or you’re just playing coy."
        isdr "...Fine, lead the way. But I don’t grovel to mortals. Arzyl’s going to get an earful about this."
        ro "I don’t doubt that for a second. Tell her I said she should fix her own messes, next time."
        isdr "If this is how you solve problems for Arzyl, I’m sure she’ll take you up on that offer."
        return
        
        
    "Impatient. Negotiate with the Dryad to let the Orc go.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        ro "Look, Isdruel-"
        isdr "Hold on a moment, Rowan. We’re just getting to the best part."
        os "Gaaaah!"
        ro "I get that these guards acted outside their station, but they are loyal soldiers of the Twins."
        show rowan necklace angry at midleft with dissolve
        ro "And if you think that torturing the servants of your would-be allies is going to secure their friendship, then you’re sorely mistaken."
        "Isdruel’s sap-colored eyes trailed across Rowan’s impassive expression, her smile widening as she winked at him, as if it were all just some perverse game she was playing. She gave her best pout and released the Orc, who collapsed onto the ground in a heap."
        isdr "Fine. I see your point. Arzyl would be quite cross with me if I messed up her little diplomatic excursion."
        "The viney creature sidled up to Rowan, her arms wrapping around his as if he were her escort."
        isdr "Shall we, Rowan? I hope next time we meet you won’t be so adverse to sharing little ‘fun’ between us."
        ro "Something tells me that your definition of ‘fun’ involves inflicting pain."
        isdr "Hehe, only on my inferiors. Who knows? Perhaps we can find someone mutually beneath us."
        return
        
        
    "Intrigued. Watch to see what she does." if isdrWatchFailed == False:
        $ released_fix_rollback()
        if avatar.corruption < 30:
            "Rowan heard the first sound of the Orc’s agony and felt a stirring in his chest. He couldn’t just sit by and watch this happen! He had not yet sunk so low beneath his own morality, that he could sit by and ogle another being’s pain."
            $ isdrWatchFailed = True
            jump isdrMenu
        else:
            "Rowan felt a strange sort of thrill watching Isdruel effortlessly torment the Orc. Despite his own misgivings, he found himself electrified by the sounds of the creature’s distress."              
            "Perhaps it was because of their ghoulish nature, or perhaps Rowan understood Orcs well enough to know that most of them were contemptible swine; either way, he could not bring himself to look away when Isdruel continued her sadistic vexations."
            "The Dryad lowered the Orc, his face level with her waist as she came face to face with his hanging junk. She reached out, her hands grasping the sexual organ with the curiosity of a child playing with a picked dandelion."
            isdr "Hm, so much fuss over so meagre an endowment."
            "Her hands began to roughly jerk him, her free hand reaching up to cup his testicles in a solid, tugging grip."
            isdr "Do you feel this, whelp? This is power. {i}This{/i} is control, not that banal bluster you and your friend were trying with me. That might make a mere mortal cower with fear, but I see it for the ruse that it is."
            "Her fingers clenched, and Rowan saw the Orc’s face contort with pain. She held him for a long moment in her crushing grip, his body trembling at the precariousness of his position. The Orc let out a cry of pain."
            isdr "I could eviscerate you in an instant, you filthy cur. Had I less important business to attend to for my Queen, I’d have likely done so."
            "The Dryad let the terrifying threat hang in the air for another long moment, then released her grip on the Orc, the vines holding up his legs and keeping him suspended in the air unravelling." 
            "The Greenskin let out a yelp of surprise as he toppled to the ground, landing in a heap on top of his fellow Guard. The two collapsed into a pile of pitiful moaning."
            "She turned to face Rowan, a brilliant, emerald smile spreading across her face. Without a word she took him by the arm and ambled forward into the Castle courtyard, humming a low, hypnotic tune as she moved."
            isdr "My apologies for being late, Rowan. I was held up by the Twins’ unruly servants. You know how mongrels can get. The weak and powerless covet that which they cannot have."
            show rowan necklace neutral at midleft with dissolve
            ro "Sure."
            isdr "I see you did not try to stop the theatrics! Could it be I’ve found a kindred spirit amongst the Twins’ misbegotten slaves?"
            show rowan necklace angry at midleft with dissolve
            ro "I am no slave, Dryad."
            isdr "Mmm, no. You’re not. I can tell. You’re something {i}infinitely{/i} more intriguing than that."
            isdr "I would like to discuss this more with you in the days to come. Perhaps next time you can be a more… {i}active participant{/i} in the fun?"
            ro "That depends entirely on where I am in that situation."
            "Rowan felt the Dryad’s grip tighten around him as her eyes held steady to him. Her smile widened."
            isdr "Oh don’t worry sweetling… you won't be the one dangling from my vines."
            return
            


label aryzlDialogueEnd:

$ arzylDialogueAvailable = False
return

#########################################################################################################
#########################################################################################################
#########################################################################################################

label arzyls_gift:

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve

"As Rowan approached the Lady of the Midnight Court’s dank chambers once more, he came upon a truly concerning sight: Jezera standing in front of Arzyl’s closed door, tapping her toe against the ground with barely-restrained annoyance. Her head snapped over to look at him when he turned the corner."

show jezera displeased at midright with dissolve

je "Why is this door locked, my hero?"

ro "Will you ever tire of using that nickname on me?"

show jezera happy at midright with dissolve

je "I will at the exact moment it fails to get a rise from you."

show jezera displeased at midright with dissolve

je "And I believe I asked you a question: {i}why{/i} is this door locked?"

ro "...Because Arzyl wanted some privacy?"

je "Then she was a fool to look for it while living under my roof. More to the point: if that was the case, she should not have invited me into her quarters in the first place."

ro "The Midnight Court has invited you to a personal meeting with their representative?"

show jezera happy at midright with dissolve

je "Oh! Rowan! Is that the telltale hint of {i}jealousy{/i} I hear?"

show rowan necklace angry at midleft with dissolve

ro "Hardly. You made me the arbiter of this alliance negotiation on your behalf, why bother giving me the task if you’re just going to make deals behind my back?"

je "Who said anything about making a deal behind your back?"

ro "Why else would you be here?"

je "Why, for my own selfish interests of course. Did you expect anything less from me?"

show rowan necklace neutral at midleft with dissolve

ro "No."

je "Ha ha! Goodness Rowan, but you are a terrible liar."

"With a smirk and a wink, Jezera waved her hand across the door. Like an obedient servant, the lock popped open."

show jezera displeased at midright with dissolve

je "Enough waiting. Come along, hero."

hide jezera with moveoutright
pause 1
hide rowan with moveoutright

scene black with fade

"The room is dark, murky and damp-smelling. Rowan could barely see in the gloom, his eyes failing to adjust as the heavy door slammed shut behind him."
" There was the sound of a hum, like the noxious buzzing of a hundred whispering voices melding together into a single, incomprehensible mass."
"Rowan felt the bottom drop out of his stomach, his hand reaching instinctively for his blade."

scene bg13 with fade

"One by one, eldritch candles made from black wax flickered to life. They glowed with a sickly, greenish hue, tainted with an almost miamsic glow that hung heavy in the room like a fog. As Rowan’s eyes at last adjusted to the dim coloration, he caught sight of a truly disturbing sight."

show rowan necklace shock at midleft with dissolve

ro "Gah! What in the hells are you doing?!"

show jezera displeased at edgeleft with dissolve

je "My, my, my, what do we have here?"

show arzyl neutral at cliohnaright with moveinright

arz "{i}Abrith’Allach! Sakah nobbek! Gephar’Ykaal!{/i}"

"Stretched across a long table, bound at the wrists and feet, a young elf struggled to free himself from the nightmare in which he found himself. He was naked from the waist up, his slender body straining against his manacles in futility."
"Catching sight of the two newcomers, he let out a keening cry which carried over the ceaseless, droning chant of the hooded and robed figures all around him."
"A humid, pinkish mist hung about him, distorting the murky light. The mist bent and shivered in geometric circles as Arzyl swirled her hands about them, twisting and bending the mist to suit her needs. "
"At each flowing gesture, the elven prisoner’s face twisted and jerked. When she reached into the swirling matrix near his chest and clenched her fingers, he screamed, the carmine smoke diverging from its singular stream into a dozen, trembling tributaries."

show jezera happy at edgeleft with dissolve

je "Fascinating."

show rowan necklace angry at midleft with dissolve

ro "{i}Fascinating?!{/i} She’s torturing that poor elf!"

je "Incorrect. The pain the prisoner is feeling is merely a byproduct of her true intent."
je "Can you not see her subtle brilliance? She is manipulating the very essence of his spirit, the way a butcher tenderizes meat. She’s making a more succulent sacrifice. "

show jezera displeased at edgeleft with dissolve

je "Granted, I do not recall inviting her servants into Castle Bloodmeen for the demonstration; although I suppose now I at least get to see one of these rituals enacted properly, for once."

"Arzyl turned to face the Demon spawn, a curling smile breaking across her angular features like the midnight glimmer of an assassin’s blade."

arz "So you have come."

je "Of course I came! You kept me waiting at the door like a frightened neophyte."

arz "My sincerest apologies, Lady Jezera, but the ritual could not be halted in such a delicate moment. Not even for your sake."

"Arzyl spared Rowan a smirk and a fleeting wink before turning to her prisoner. She gestured towards him, beckoning Jezera forward."

arz "The sacrifice is prepared. We need only conduct the ritual."

show jezera happy at edgeleft with dissolve

je "Good! Then let’s not waste any more time."

show rowan necklace neutral at midleft with dissolve

ro "What are you going to do?"

arz "What does it look like I’m doing?"

show rowan necklace angry at midleft with dissolve

ro "You think {i}this{/i} is going to convince me that the Midnight Court are a better ally than the Red Sun Alliance?"

"At this, Arzyl quirked an eyebrow. A smile built across her face that sent a chill down Rowan’s spine. She walked up to him, her sultry footsteps criss crossing in front of her as she exaggerated the sway of her hips. She came to a halt in front of him."

show arzyl neutral at midright with moveinright

arz "Tell me, Rowan: just what is a soul?"

ro "Don’t try to spin your words with me, witch."

arz "I wouldn’t dream of it. You only need to listen."
arz "When my people arrived in Rosaria from a different plane of existence, we were as infants attempting to comprehend the new reality in which we found ourselves."

"Arzyl’s hands swirled around her, the clinging, pinkish smoke of her ritual building like a fog around her fingertips."

#arz angry

arz "The very air we breathed was an uncomfortable stranger; the ground we walked upon an unfamiliar echo from whence we came. The trees, and the rivers and the mountains a foul parody of our old existence. Not even the sky above us was the same."
arz "But we were Spirits of Nature, we were always meant to adapt or die, to embrace {i}change{/i}…"

"Arzyl clenched her fist around a particularly thick strand of pinkish smoke. The prisoner let out a deafening scream."

#arz happy

arz "-Or face oblivion."

ro "Is that how you justify your atrocities against this poor fool? Survival of the fittest?"

arz "What would you call it? In nature, the strong consume the weak. Ask yourself: why is {i}he{/i} lying on the table, and not another from his village?"
arz "He was the chaff, the weakling; the sickly and decrepit. Does not the Lion hunt the oblivious Gazelle, does not the lizard devour the eggs of an absent Eagle? Morality is the false construct of a deluded animal in search of greater meaning. Strength and will are all that matter. "
arz "Are all that ever mattered."

"Arzyl turned back to face the manacled prisoner, her hands reaching out and grasping the trembling tendrils of smoke above his chest like a rope."

if society_type == 'feudal':
    show jezera displeased at edgeleft with dissolve
    je "Now now, Arzyl, be fair to the poor prisoner: it was chance that saw him captured. Nature is by no means a fair thing, regardless of how you might want to justify it. This boy got unlucky; don't try to claim otherwise."
    arz "Luck plays a part even in nature, my Lady"
    je "But we are not ‘nature,’ my dear. {i}Our{/i} methods are a little more civilized.  We have laws and titles to make things less random."
    je "I don't condone this kind of needless waste of resources. Moving forward, more suitable subjects will be selected for your use during your stay in the Castle: criminals, layabouts and the like."
    show jezera happy at edgeleft with dissolve
    je "It also gives a good incentive to try and earn the favor of my brother and I! "
    
else:
    je "I see we are kindred spirits, Arzyl! He lost because he couldn't stop you; you had the power to choose who in village would be yours, and he could do nothing to prevent himself from being chosen."
    arz "You are not mistaken, my Lady. This wretch’s fate was sealed the moment I laid eyes upon him."
    je "Had he managed to fight you off or even destroy you, then that would have been his right to do; after all, he can hardly be blamed for killing a foe to preserve himself."
    je "But he didn't. So here he is."

ro "You hide behind your words, witch. But I have spoken with the Red Sun Alliance. They believe in Survival of the Fittest as well, and it’s not... "
ro "Whatever the hell this is supposed to be."

"Arzyl let out a contemptuous snort. She turned, her slender shoulders squaring as she looked down her nose at Rowan."

arz "‘Survival of the Fittest.’ What those enslaved beasts practice is Survival of the Favored."
arz "A thousand generations pass, and the weak are allowed to return from death in place of the strong. Only those who have properly prostrated themselves to that would-be messiah, Sol return. The weak-willed, the cowardly and the subservient."

#arz angry

arz "My sister died her last death six centuries ago. She was one of the strongest and fairest of all the Fae. But because she refuses to bow to that Golden Dragon, she remains trapped in limbo, fading away on our old plane of existence. "
arz "Had our realm been this green and verdant place you call Rosaria, she would have been the greatest among us. But instead she fades away, our old plane of existence slowly sapping her of her strength."

"Rowan could swear he could see tears building in the eyes of the ancient Fae sorceress."

arz "{i}That{/i} is what is unnatural. That is what the Red Sun Alliance offers my people, Rowan. Sol has infected us, polluted our very essence by shackling us to his will. He is nature corrupted, tamed to the tyranny of a single being, not for the sake of the natural ecosystem, but for his own, grasping vanity."

show rowan necklace neutral at midleft with dissolve

ro "If what you say is true, why do you toy with other being’s spirits in the same way?"

arz "You are comparing an anthill to a mountain range. This Elf lives a natural life cycle - short and fleeting as it is. He is {i}afforded{/i} the chance to fail."

"Arzyl stared down at the struggling prisoner on the dais with an expression approaching envy."

arz "He is, in many ways, blessed in his rudimentary reality. He does not have to be anything other than what he is: in this case, my prey."
arz "I cannot speak to the confusing morays of your realities or your heavens or your gods, but at least once he dies this creature will go where those that created him intended, be that a comforting paradise, or a black abyss. "
arz "...When we Fae die, our spirits return to our original plane. We cannot pass beyond the veil again without Sol’s blessing. And If we linger too long in that deadened place of ash and memories, we wither."
arz "Sol is the gatekeeper, preventing us from returning, from existing without his overriding control. Life without free will is just a lingering suicide. My people {i}refuse{/i} to be his slaves, and thus, we return once more to the Elf lying upon the table."

#arz happy

arz "He - and many others like him - has provided us with an ‘alternative’ means of survival. Just as Sol perverted our natural life cycles and and forced us to submit, we have twisted the laws this new reality to adapt to his "
arz "This is a ritual to replenish our souls. And the prisoner is the fuel."

show jezera displeased at midleft with moveinleft
show rowan necklace neutral at edgeleft with moveoutleft

je "My, my, what a conundrum this puts me in. As I recall Arzyl, one of your demands for this alliance was to have free access to take whomever you please from our occupied villages."

arz "Only the weak. Only the useless. Your servants and agents will of course be left alone."

je "Nevertheless, you are asking for the right to take people from their beds. {i}My{/i} subjects."
je "On the one hand, this kind of reckless kidnapping and sacrifice would be hell on our population, sowing fear and resentment wherever you go, and leaving me with the task of cleaning up your mess."
je "On the other hand…"

show jezera happy at midleft with dissolve

je "These powers of yours are quite {i}fascinating{/i}."

show rowan necklace angry at edgeleft with dissolve

ro "You can’t be serious."

arz "Doubt my methods if you must Rowan, but do not judge before you understand what it is that you are judging."

je "Hmm… perhaps a demonstration is in order?"

"Another curling smile grew across Arzyl’s face. Her hands swirled again across the unseen plane above the elf’s body where the pink mist hung like lingering, acrid smoke."

arz "If it pleases you, my Lady. I can show Rowan firsthand the raw power of a consumed soul."

#arz aroused

arz "Shall I give it to you, Rowan? Shall I feed you the delectable sweetness of another’s life force? I promise you, you will not regret it.."

menu:
    "Accept Arzyl’s 'gift'.":
        $ released_fix_rollback()
        $ arzylGift = True
        show rowan necklace neutral at edgeleft with dissolve
        ro "...Fine. Since you’re going to kill this poor fool anyway, show me how this senseless death actually could mean something."
        #arz happy
        arz "Oh, Rowan. You are as ravishing as you are wise."
        ro "-On one condition."
        je "Oh, here we go."
        ro "Make it quick. Make it painless. You’ve already condemned that poor Elf to death, the least you can do is minimize his suffering."
        #arz neutral
        arz "That will significantly weaken the effect of the spell. If I try to limit his suffering, I am also hamstringing my ability to manipulate his-"
        ro "Do it my way, or don’t do it at all."
        arz "Hm, you know Rowan I never noticed this about you, before."
        #arz aroused
        arz "You’re so… forceful. I like that."
        "Arzyl turned back to face the half-conscious prisoner. Her hands reached out, fiddling in frenetic movements as her fingernails traced amongst the pink smoke. It swirled around her fingertips, attaching to it like rope tethers to a rising monolith."
        "Her chanting voice began to rise above the dim, her voice growing and growing in strength till it was booming in the low light of the room. The cultists’ calls turned to a gnashing wail as a light appeared."
        "The Prisoner jerked, his mouth gaping as his eyes became lidless husks. They stared up at oblivion. He seemed to scream, though no sound emerged from his voice."
        "In a rush, the pinkish smoke was sucked, as if in a vacuum into Arzyl’s fingertips. The prisoner collapsed against the table, dead. He looked empty, wrinkled and dry, as if he were a corpse worn away by a stinging desert sandstorm."
        arz "S-step forward Rowan. Quickly!"
        show rowan necklace neutral at midleft with moveinleft
        show jezera displeased at edgeleft with moveoutleft
        pause 1
        scene white with fade
        show rowan necklace shock behind white
        "Arzyl’s hands felt cold upon Rowan’s brow as she laid her fingertips upon his head like a crown. There was a blinding flash, and for a moment his vision went white."
        ro "{i}Aaaah!{/i}"
        "Fever dreams of a passing spirit flowed like water through his consciousness. Names, faces, places, events pass beyond his eyes in a confusing mess of contradictions. Rowan felt in an instant the whole of the poor elf’s memories."
        "A lone tear crawled down his cheek. Heat built in his mind as the energy redirected itself, dissipating the confusing jumble of sensations into a warm, soothing bliss."
        "When Rowan opened his eyes, he was on the floor, staring up at the ceiling."
        scene bg13 with fade
        show rowan necklace neutral at midleft with dissolve
        show jezera happy at edgeleft with dissolve
        show arzyl neutral at cliohnaright with dissolve
        je "Jeez, one silly soul-transfer and you go faint on us!"
        arz "The first spirit meld is always the hardest. Thankfully, he enjoyed only a watered down sensation. Many of those non-fae who endure a full spirit meld for the first time do not survive the experience."
        ro "Ugh… what- what happened?"
        arz "You absorbed the prey’s soul. It has revitalized you."
        ro "I feel…"
        #arz happy
        arz "Younger? Stronger? {i}Filled{/i} with energy?"
        show rowan necklace angry at midleft with dissolve
        ro "Dirty."
        je "Ha ha! Oh Rowan, never change."
        show rowan necklace concerned at midleft with dissolve
        ro "I saw his memories. Just for an instant, but-"
        arz "That was his spirit melding with yours, it takes some time before it breaks down into something consumable. I helped the process along as quickly as I could to spare you from..."
        #arz angry
        arz "Hmph. Anyway, your newfound gifts will not last long; the ritual itself was stunted, due to the restrictions you placed upon me."
        je "Even still, most impressive. I can see the strength in Rowan myself!"
        #TODO - temp stat boost
        #TODO - MC rep boost
        $ change_base_stat('c', 3)
        show jezera happy at midleft with moveinleft
        show rowan necklace neutral at edgeleft with moveoutleft
        jump arzylGiftEnding
        
    "Refuse her ‘gift’.":
        $ released_fix_rollback()
        $ arzylGift = False
        ro "No."
        #arz neutral
        arz "...No?"
        ro "I will not be a part of this crime against nature."
        ro "This goes beyond ‘cruel necessity’ Jezera. This is plain cruelty."
        ro "I know you don’t care all that much about the subjects you rule."
        ro "...But by whatever small scrap of humanity you have left, {i}this{/i} is not the way to treat them. You’re trying to build an Empire, not govern over smouldering ashes."
        show jezera displeased at midleft with dissolve
        je "Do not presume to tell {i}me{/i} what to do, Hero."
        show jezera happy at midleft with dissolve
        je "That being said… I’ll be sure to take that into ‘consideration,’ my loyal servant."
        "Arzyl’s eyes were filled with frigid malice. Her lips flattened into a line, her nose curling into a sneer as she let out a huff."
        #arz angry
        arz "I expected better of you Rowan."
        "Rowan heard the scream before he realized what was happening. Arzyl clenched her hands tight around the pinkish smoke, where before she had been content to merely manipulate. Now her knuckles clenched like she was trying to choke the life out of him."
        "...And that’s exactly what appeared to happen. The Elf writhed upon the table, his face reddening as his eyes bulged. The penultimate screech grew and grew, and grew, till Rowan winced and looked away."
        "How was a creature able to scream for so long? He didn’t even pause to breathe."
        arz "{i}Kakh’Khaan!{/i}"
        "Arzyl’s fingers ripped the smoke into pieces like a child tearing apart a fallen leaf.The scream blessedly, mercifully stopped. The Elf collapsed against the table, twitching, his limbs moving in an uncoordinated and jerky fashion."
        "His eyelids fluttered, but his pupils were dilated, dead things that stared at nothing. Rowan felt for a brief, terrible moment that they were staring at him."
        arz "Seeing as no one here has need of this thing’s soul, the demonstration is over."
        show rowan necklace neutral at edgeleft with dissolve
        jump arzylGiftEnding


label arzylGiftEnding:

arz "{i}Now{/i} do you believe me, my lady?"

je "It is indeed a neat trick, my dear. Whether or not it ultimately serves my purposes? Well…"

"Jezera’s predatory smile was like a fistful of razors in her mouth. She stared at Rowan with a long, knowing look."

je "That remains to be seen."

arz "Do not allow another’s words to sway you one way or the other, my Lady. Perhaps next time {i}you{/i} could be the target of such an empowering ritual?"

je "Perhaps. We would - of course - need to take the necessary… ‘precautions.’"
je "After all, you can never be too careful, even with friends."

arz "You need not worry when in my august company, Jezera. I am committed to showing you and your brother that the Midnight Court is the best possible ally you could have."

"Arzyl shot a glance over in Rowan’s direction, her eyebrow quirking. He couldn’t tell if she was flirting with him or glaring at him."

arz "And conversely, no worse enemy."

je "Hm, I will admit, there are a few details about this ritual that I’d like to go over with you… perhaps in private."

#arz happy

arz "Hmm, that sounds positively delightful, my Lady."

je "Rowan, would you give us the room?"
je "Hm… better yet, will you stick around? Perhaps in watching us, you’ll learn something about the nature of magic."

if arzylGift == False:
    "Arzyl’s eyes flashed at Jezera’s offer."
    #arz angry
    arz "No. He does not deserve to see what transpires. Do you reward a dog for going against your commands?"
    je "Oh come now Arzyl, don’t you like an audience?"
    arz "Only those who are worthy to see such a spectacle."
    arz "Perhaps another time, when my tempers have cooled and Rowan has gained the proper perspective."
    "Jezera held eyes with the stoic Fae for a moment, then shrugged."
    je "Sorry Rowan, seems like the deal’s off. On your way, then. Arzyl and I have some ‘business’ to discuss."
    je "Don’t wait up."
    "Rowan took his leave, sliding free from Arzyl’s room and the limp body splayed across the table nearby with a shudder of relief. He might have angered Arzyl, but at least he had maintained his dignity."
    "...For all that was worth at this point. He did his best to put the poor Elf out of his mind, though the memory of his vacant, soulless eyes hovered in his mind for several hours thereafter."
    jump aryzlDialogueEnd
    
"Rowan knew Jezera well enough by now to know precisely what she intended to do with Arzyl. He stood firm for a few moments as Arzyl’s chanting circle of hooded followers slowly filed out of the room."
"The way Jezera’s eyes roamed across Arzyl’s succulent form told to her true motives. The lack of an invitation to ‘join’ in the discussion spelled out the voyueristic purpose of Rown’s presence as well, should he choose to stay."

menu:
    "Stay and watch.":
        $ released_fix_rollback()
        jump jezArzSex
        
    "Leave gracefully.":
        $ released_fix_rollback()
        ro "I shall take my leave."
        je "Why did I have a feeling that would be the case?"
        "Jezera planted a thoughtful finger on her lips and smirked. Rowan did his best to ignore the jab."
        ro "Do you have any more orders for me, my Lady?"
        "Rowan’s Demonic mistress let out a snort."
        je "No. That will be all, my hero. Run along now, I have a competition to win."
        "Deciding that any words he might use in this moment would only give Jezera ammunition for more mockery, Rowan pivoted on his heel and left the room. He heard one last, mocking chuckle emerge from Jezera before the door closed behind him."
        jump aryzlDialogueEnd
    
label jezArzSex:

"Deciding that any words he might use in this moment would only give Jezera ammunition for more mockery, Rowan planted his feet and said nothing. Arzyl’s unearthly eyes began to glow with mirth."

arz "You only want him here as an audience."

je "Of course! Now let’s get that robe off."

#arz naked

"Jezera strode forward, grasping Arzyl’s milky tits in a rough grope. She unceremoniously ripped her slim blue bodice, exposing the Fae’s heaving breasts and pink areolae. Rowan’s eyes trailed across them, his face betraying no expression as Jezera cast a sly gaze over her shoulder in his direction."

je "Time for a ‘demonstration’ of my own!"

"Rowan’s demonic mistress kneaded the Fae’s breasts within her hands, her grin growing as Arzyl’s face struggled to maintain its cold indifference. Jezera, ever the minx, leaned up and planted a wet kiss upon the stoic creature’s lips."

arz "Please: we can do far better than this. Perhaps another demonstration is in order?"

"Arzyl’s slender fingers slid across the bare, purple skin of Jezera’s shoulders, sliding off her crimson dress with an almost effortless grace. Her hands trailed southward, grasping Jezera’s still-covered bottom in her hands. The Demon let out a contented purr."
"Her purr turned into a sudden gasp as Arzyl whispered something under her breath, her fingers hovering over Jezera’s tailbone as they massaged something that only she could see. Jezera shuddered for a moment, pulling back before Arzyl could get a firm grip on her."

je "Naughty little witch! And here I thought we were playing a simple lover’s game."

arz "Why settle for such pale mundanities, my Lady? We are both better than that."

"As if to exemplify that fact, Arzyl reached out and brazenly groped Jezera’s left breast, pulling aside the crimson fabric to tweak her nipple. The Demon let out a pleasured laugh."

je "Hmm, careful what you wish for, my dear. If we go by that particular, juicy metaphor: you are attempting to out-hunt a lioness."

#cg1
scene cg518 with fade
#arz naked
show arzyl neutral behind cg518
show jezera happy behind cg518
show rowan necklace aroused behind cg518

"A whispered breath is all it took, and familiar, tendrils of power erupted from her fingertips. But unlike her normal, eldritch puppeteering, this took a decidedly different turn. "
"For one the ropes were now pinkish, almost purple in coloration. They swept about her like whips before stretching down towards the Fae’s crotch."
"They rubbed against the fabric of her underwear with a pleasing friction, causing the Fae to let out a low, breathless sigh. Her thighs clenched for a moment before she put a hand to Jezera’s wrist. "

arz "{i}Ah!{/i} Yes! You are exactly what I expected, my Lady. Powerful and fearless, delight and danger together as one."
arz "But… why should unleash ourselves upon each other so quickly? Isn’t the kill far more savoury when it has been properly…"

je "‘Stuffed?’"

arz "Hmm, I was more thinking ‘chased down.’"

je "What did you have in mind, my dear?"

arz "A game. A test, if you will. "

je "Of our abilities?"

arz "Of our ability to resist one another."

"The low growl that emerged from Jezera’s throat told Rowan everything he needed to know about the stakes of their unspoken wager. Her eyes practically shined with glee as she began to caress the ancient creature’s chest with her free hand."

je "Mmm, so it is a lover’s game, then. One I fully intend to win."

"It was as if her words were the spell to some sinister ritual, for in the blink of an eye Arzyl and Jezera were in each other’s arms. They ripped at one another’s clothing with the heedless care of two sweethearts on a midnight tryst."
"They were naked, their hands roaming across one another, groping flesh and pinching bottoms."
"Jezera’s used her left hand to touch, and her right hand to cast, her fingers rubbing together to stimulate movement across the hair-thin tendrils under her command. More erupted from her fingertips, swirling about Arzyl’s breasts and forming something approaching breast manacles."
"Arzyl gasped, her body going taut at the same time the ropes did. The very touch of them seemed to stimulate pleasure, and Rowan could see her mouth open wide in a near-orgasmic O. The ropes flashed pink, and Arzyl let out a literal squeal."
"Not to be outdone, Arzyl’s fingers reached out to caress Jezera’s body, her face, her breasts. Everywhere the fingers traced, goosebumps appeared. Rowan watched as Jezera shivered, her concentration wavering as she struggled to keep her knees together."
"Arzyl ran her fingers down Jezera’s spine, leaning forward and planting her thick lips upon Jezera’s extended neck. The Demon laughed at the Fae’s impudence, planting her hand in a rough spank across Arzyl’s ass as her spell-finger continued to grind and twist and pull against the threads upon the ethereal creature’s cunt."

if avatar.corruption < 31:
    "Rowan did his best to keep his face impassive and his gaze faraway as he stood in front of the increasingly-erotic display."
    "Both of the voluptuous women were gasping and panting, the raw heat and stench wafting over his nose and bringing an uncomfortable twinge in his pants. He did his best to ignore the pleasured cries and glances Jezera shot his way every so often."
    
else:
    "Rowan couldn’t help but gawk at the lewd display. Jezera and Arzyl were going at one another like bitches in heat, their bodies slick with sweat as they engaged in their erotic competition to out-tease the other."
    "The hapless spectator found himself reaching down to fondle his growing erection through his pants. Jezera smirked at his arousal."

"The twining torsion of Jezera’s semi-corporeal threads twisted and squirmed against Arzyl’s soaked thighs. She grimaced, her magic fingers leaving a trail of shivering ecstacy across Jezera as she tried to resist her partner’s magics."
"Jezera grunted, leaning forward and taking Arzyl’s right nipple in her mouth. Her casting hand sent out yet more pleasure ropes which wound tight about the other nipple, clenching and constraining like the contractions of her vagina."
"Seeming to almost read Rowan’s thoughts, Arzyl reached down, her fingers curling into a question mark that found its answer at the junction of Jezera’s thighs. She cried out, grasping Arzyl’s arm to steady herself, to keep her own legs from giving out."

je "C-clever... "

"Jezera shifted focus, clenching her fingers as her hand clasped tight to Arzyl’s ass, pulling them together, chest to chest. The Demonic twin clenched her teeth, her brow furrowing with concentration even as her wet sex glistened with every schlicking sound that the Fae witch inflicted with her finger."
"It was an utterly ruthless game of teasing."
"The first sign that the sexual dam had broken came when Arzyl’s pale face reddened to a bright, cherry color. She bit her lower lip, her eyes clenching for a moment. Jezera’s ropy tendrils slid across her mound, dragging with slow, delectable torsion up the length of her womanhood, wrapping tight around her clit."
"Jezera flicked her thumb across her hand, and more ropes emerged. One wrapped itself tight around Arzyl’s luscious lips, sealing whatever spell the ancient Fae had been about to utter. Her body went slack, her fingers slipping bonelessly from Jezera’s drooling snatch as she shuddered in place."

arz "{i}Aaaahn!{/i}"

"Rowan watched as the vaunted Voice of the Fae cried out and orgasmed onto the floor, a flood of feminine fluids squirting forth as Jezera’s relentless ropes pulled tighter and tighter, forcing the Witch to helplessly endure the erotic euporia that radiated out from their touch."
"Jezera, her face as red as her opponent’s, laughed aloud."

je "{i}Mmmmh{/i}, that was a good one! I look forward to giving you many more in the hours to come, my dear."

arz "{i}Hah… haaaah…{/i}"

"Despite Jezera’s bold words, Rowan could see she was nearing her limit. Her spine was taut like a drawn bowstring, and her body all but quivered like one too. She allowed the mystic ropes that bound Arzyl to become incorporeal, and the Fae collapsed back onto her bed, panting."

je "The point has been made. Rowan, give us the room."

ro "...Yes."

"His face bright red with embarrassment, and perhaps more than a bit of arousal, Rowan pivoted on his heel and left the room. He heard one last, mocking chuckle emerge from Jezera before the door closed behind him."

je "Quickly now, best two out of three!"

jump aryzlDialogueEnd