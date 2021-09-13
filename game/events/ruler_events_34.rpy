init python:
    
    event('spider_be_reborn', triggers="week_end", conditions=('castle.buildings["pit"].lvl >= 1', 'arzylDialogueStage > 1', 'castle.buildings["pit"].driders >= 2',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('spanks_for_the_memories', triggers="week_end", conditions=('liurial_orgasm_control_on == True',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('dream_of_wolves', triggers="week_end", conditions=('HSDreamSex',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('rowan_and_the_escaped_slave', triggers="week_end", conditions=('week > 50', 'avatar.corruption < 31',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('mutual_elven_fear', triggers="week_end", conditions=('week > 25', 'castle.buildings["pit"].lvl >= 1',), group='ruler_event', run_count=1, priority=pr_ruler)

label spider_be_reborn:

scene bg25 with fade

"As Rowan made the arduous trek down to the breeding pits, he came across a most unexpected sight. A tall, elegant being towered over Draith, who languished beneath her withering glare."

show draith neutral at edgeright with dissolve
show arzyl neutral at midright with dissolve

arz "..."
arz "{i}You{/i} are the castle’s beastmaster?"

dra "I-I am, ma’am."

#arz angry

arz "-And just how do you plan to subdue the creatures in this pit? You look so weak I doubt you could subdue a pork roast."

"Draith was speechless, his mouth hanging open as he tried to find something to say. He gabbled out a string of nonsense words before managing to actually answer her question."

dra "N-no, Ma’am! "

"Deciding that prolonging the torture would likely see the fragile beastmaster dissolve into a useless puddle of nerves, Rowan stepped forward to save the terrified Elf."

show rowan necklace angry at edgeleft with dissolve

ro "Arzyl, I would appreciate it if you did not amuse yourself at the expense of the castle staff. Don’t distract our beastmaster from his duties. "

"Arzyl let out a dismissive breath of air, her cold eyes trailing across Rowan’s form as he descended the steps into the breeding pits. Draith cowered from her gaze, sidling behind his unexpected savior like a shield to wall off the lady of the Midnight Court."

show rowan necklace angry at midleft with moveinleft

show draith at edgeleft with moveoutleft

arz "A being who would seek to dominate others requires a will of iron and a merciless attitude. Yet the Twins see fit to make a mockery of their own bestiary by having this frail specimen take up the whip and bridle."

ro "Draith is more skilled than anyone at the castle when it comes to beasts and monsters, Fae included.  He’s the perfect man for the job."

arz "That I doubt. But so be it: let him prove his worth to me."

show rowan necklace neutral at midleft with dissolve

ro "What do you mean?"

arz "You have captured a number of the {i}Drach’anili{/i} in your recent adventures, yes?"

ro "...The what?"

arz "The web-biters. The spider-folk of the deep forests."

ro "You mean the Driders? What of them?"

arz "It just so happens that one of my Handmaidens is nearing the end of her host body’s lifecycle. The traditional rituals and sacrifices are no longer enough to sustain her."

ro "I fail to see what this has to do with you bullying our beastmaster."

#arz happy

arz "She was looking to acquire a new host, one with a more… shall we say, “deadly complexion?”"
arz "She mentioned the web-biters by name. I had almost given up hope of finding one myself, and was going to simply implant her into an inferior specimen."

ro "And you want us to give you one of the Driders to use as a new host?"

#arz neutral

arz "Why not? They are strong - if willful and stupid - creatures. They make wonderful predators, ideal hosts for the Fae."

dra "They’re not exactly stupid, rather-"

arz "Think of it as a cultural exchange between newfound allies. In return, I am willing to give you a rare glimpse into the Fae’s methods of soul transference."

ro "..."
ro "I’ll have to think about it."

#arz annoyed

arz "The time for careful contemplation is gone: my Handmaiden will not last much longer in her current form. If you will not acquiesce to my request now, I will be forced to locate a lesser host for her immediately."

"The look of danger in her eyes told Rowan that she would not be pleased with this particular outcome. He glanced over his shoulder at Draith, who was shaking like a leaf, using Rowan’s larger bulk as a bulwark against the matron who so terrified him."

ro "Give me a moment to talk it over with the beastmaster."

"Arzyl made a dismissive gesture with her hand. Rowan took the terrified Elf by the hand and lead him off to one side of the breeding pit."

#show arz annoyed at edgeright
show arzyl neutral at edgeright with moveoutright

ro "So, what do you think?"

dra "She scares me more than Jezera does."

show rowan necklace angry at midleft with dissolve

ro "No not her, the offer she made us."

dra "Oh… about the Driders? Well it’s…"

"Rowan watched has an eager grin spread across the Elf’s face."

show draith happy at edgeleft with dissolve

dra "It’s amazing! I definitely think we should do it."

show rowan necklace shock at midleft with dissolve

ro "Really? You realize that this ritual will kill the Drider, right?"

dra "I mean… yes, and it’s unfortunate to have to lose a creature as majestic as Dirklaw or Antaweb. But…"
dra "Rowan, This is a once-in-a-lifetime opportunity!"
dra "Can you imagine: merging two being’s life forces together to create a brand new creature?"
dra "I have heard of a human alchemist attempting to make such chimeras, but stories claim he never managed to refine the process beyond creating mindless beasts!"
dra "But to make an actual thinking, feeling hybrid! Gods, if my people possessed such an ability, just think of the beasts we could create!  "

if avatar.corruption > 60:
    show rowan necklace neutral at midleft with dissolve
    "Rowan imagined for a moment what kind of twisted terrors might lurk in the energetic mind of the little Elf. If one set aside the blasphemous notion of playing God, the military application of such custom-created chimeras could not be ignored. "
    ro "Something to consider in the future, perhaps. For now… "
    "He turned to face Arzyl, who stood impatiently tapping her toe against the ground. Her glowing eyes swiveled to him as he came to a decision."
    
else:
    "Rowan imagined for a moment what kind of twisted terrors might lurk in the energetic mind of the little Elf. He mentally shuddered."
    show rowan necklace concerned at midleft with dissolve
    ro " ...I’d rather not."
    "Sighing to himself, the warrior turned to face Arzyl, who stood impatiently tapping her toe against the ground. Her glowing eyes swiveled to him as he came to a decision."
    show rowan necklace neutral at midleft with dissolve

label driderMenu2:

menu:
    "Ask if the Fae has a gender preference.":
        $ released_fix_rollback()
        ro "Does your Handmaiden care about the gender of the Drider she possesses?"
        arz "Not in the slightest. "
        arz "A Handmaiden is a Handmaiden, we Fae make no distinctions on the particulars of our host’s genitalia."
        ro "Does that apply to you, as well?"
        "Arzyl swayed her hips as she sashayed up to Rowan, her ripe breasts wobbling as she smirked at him."
        #arz happy
        arz "I have taken a male host in the past, if that is what you are asking. The Fae are not bound by the dualistic reality of a mortal’s reproductive organs."
        arz "And in the case of my Handmaiden: I am already granting her a great boon by asking an ally for a gift on her behalf. It is only fair that you get to choose the manner of gift that is given."
        jump driderMenu2
        
    "Bring her the Female Drider.":
        $ released_fix_rollback()
        $ driderSex = "female"
        ro "Very well, Arzyl. I will have Draith bring you the female Drider to use as the host."
        jump driderTransformation

    "Bring her the Male Drider":
        $ released_fix_rollback()
        $ driderSex = "male"
        ro "I will grant you your request, Arzyl. Draith will bring you the male Drider to become the new host."
        
    "Deny the Request":
        $ released_fix_rollback()
        "Rowan shook his head. No matter how he tried to square it in his head, he did not like the idea of allowing Arzyl to use one of his Driders in such a manner."
        ro "No. I’m sorry Arzyl, but we cannot spare a Drider. Your Handmaiden will have to find a different host body."
        "Arzyl’s glare could have melted stone. Rowan felt the shadow of Draith‘ form cower behind him as if sheltering from a storm."
        #arz angry
        arz "No indeed, you obviously need these witless creatures for the far greater purpose of allowing your incompetent little beastmaster to poke and prod at them like a blundering child."
        arz "Very well, it is of no concern to me. But the Midnight Court will remember this the next time you come seeking our aid."
        "There was a danger in her eyes. Rowan felt his hand reach in caution towards the hilt of his sword, though the Fae did not make a move. She turned, striding with quick steps out of the breeding pit."
        arz "If you will excuse me, I have arrangements to make with my Handmaiden."
        hide arzyl with moveoutright
        "Rowan watched the Fae enchantress as she left, his hand never leaving his sword hilt till she was gone from view. He breathed out a low sigh of relief."
        dra "She was not happy."
        ro "She’s trouble. How much trouble she is for us though remains to be seen."
        dra "Well, at least I get to keep Dirklaw and Antaweb. Despite the whole… aggression thing, I’ve grown quite fond of the two of them."
        #todo - lose MC relationship
        return
        
label driderTransformation:

arz "Excellent Rowan! You will not regret your generosity."
arz "And worry not, I shall bring my Handmaiden here, we shall perform the ritual within the Drider’s cage itself."

"Arzyl whispered a low incantation and snapped her fingers. At the apex of her chant, a blinding blue light filled the room. Rowan only just managed to shield his eyes from the glare in time to avoid being stunned."
"Through the glimmering fog a pale, emaciated figure stepped into reality."
"What appeared before his eyes was an ancient, decrepit human. Her face was a mess of wrinkles, like the bleak furrows of a volcano’s pyroclastic flow caught mid-eruption. "
"She might’ve been beautiful once, but now she was a hunched figure: bent backed and knobby kneed, with a toothless, gaping maw of a mouth and a whispy, white tuft of fuzz atop her head, like baby hair."
"Rowan gaped for a long moment at the wizened figure who shuffled through the break in reality. The only thing about her that seemed even vaguely alive were her eyes: dark, piercing green, the color of a forest canopy in heavy shadow."

show rowan necklace shock at midleft with dissolve

ro " ...{i}This{/i} is your Handmaiden?!"

arz "It is, indeed. You see now why I said it was pressing that we find her a suitable host. "
arz "Her original body has already lived long past its natural lifecycle, and nothing short of a complete migration will be sufficient to save her."
arz "We must act quickly. Come, my dear: Rowan has procured the form you sought."

"Rowan watched as Arzyl gently took her Handmaiden’s trembling, arthritic hand in hers and led her towards the Drider cage, where Draith was overseeing his Orcish worker’s efforts to chain up the creature. Draith did his best to calm the worked up monster."

if driderSex == "female":
    dra "Shh, easy girl. No Orc treats today, we have something special for you instead."
    "The female Drider’s eyes burned with anger at her restraints, her chitinous body shifting and twisting this way and that in a vain attempt to free herself from her bonds. She let out an angry hiss, but Draith simply patted her spider-bottom in pity."

else:
    dra "Cool it boy, it isn’t feeding time anymore… or I guess, ever again. There’s someone here who wants to meet you."
    "If the male Drider was aware of what Draith was saying to him, he showed no sign of it. He attempted to lurch forward in his restraints, snarling as he parted his maw wide and displayed his poisonous mandibles. He let out a hiss, but Draith simply patted his spider-bottom in pity."
    
"The gate opened, and Arzyl, the Handmaiden and Rowan stepped into the cage."
"The old crone broke out into a wide, toothless grin as she caught sight of the struggling Drider, letting out a wheezing groan of joy. Smiling from ear to ear, she leaned up and whispered something in Arzyl’s ear, cupping her hands as if to capture its faint tone."

arz "My Handmaiden wishes to thank you for your generous gift. In ages past she was born into a form much like this one. "
arz "I cannot begin to tell you how long she has pined for the chance to live as one of them! Let us tarry no longer:"
arz "Beastmaster, step away from the {i}Drach’anili{/i}!"

if driderSex == "female":
    dra "So long girl."

else:
    dra "So long, buddy."
    
arz "{i}Uns-Alach ma dorr{/i}."    

"Arzyl’s hands crackled with arcane energy. The tingling tendrils ran up both the wizened woman and the bound Drider’s bodies. They began to shiver and jolt in place."

arz "{i}As kalah mach bo. Heen yala yidor.{/i}"

"The room and the cage flashed a bright, electric blue. The walls flickered and shivered, as if reality itself were unraveling at the eldritch shimmer of Arzyl’s incantation."
"Rowan watched in stonefaced silence as the wizened Fae’s eyes rolled into her head. Her tremors became seizures, and from her gaping, lipless mouth emerged a dark mist, like onyx droplets issuing forth from a waterspout."

if driderSex == "female":
    "The Drider let out a keening screech, her multiple eyes blinking in arrhythmic disharmony with one another."
    "Her humanoid half shuddered, and her limbs went taut. More violent still was her spider half, whose eight limbs twitched and jolted like an insect in its final death throes."
    arz "{i}Drall’Acha{/i}!"
    "With a dramatic flourish Arzyl directed the channel of spiritual energy issuing forth from the Handmaiden’s old host into its new one, the mist filling the Drider’s nostrils as her mouth opened to scream. But no sound issued forth."

else:
    "The Drider let out a booming roar, his multiple eyes blinking in arrhythmic disharmony with one another."
    "His humanoid half shuddered, his muscled abs clenching as his limbs went taut. More dramatic still was his spider half, whose eight limbs twitched and jolted like an insect in its final death throes."
    arz "{i}Drall’Hekar{/i}"
    "With a dramatic flourish Arzyl directed the channel of spiritual energy issuing forth from the Handmaiden’s old host into its new one, the mist filling the Drider’s nostrils as his mouth opened to scream. But no sound issued forth."

"The concentrated energy in Arzyl’s hands dissipated away, the room returning to its natural color. The old woman who had once been the Fae’s host crumpled to the ground, dead."
"The Drider stood stock still, as if calcified into marble. It stood in a locked position, its eyes slowly opening to stare blearily at the world around it."

ro "Is it… done?"

arz " Not quite. Witness the transformation."

if driderSex == "female":
    "Rowan watched as the Drider let out a low, stomach-churning gurgle, her throat clenching as the changes took hold."
    dra "{i}Oh{/i}!"
    "The terrifying changes spread: the black, chitinous armor of the former-Drider’s spider body flowing across her skin, forming clothing-like coverage to her shifting physique."
    "A pair of humanoid legs sprouted out from beneath her former thorax. They were long and lissome pale, like her humanoid half. In place of feet, black tips like a spider’s legs grew at the end."
    "Her arms became more angular, her fingers long claws of black chitin. The Drider’s white hair shrank into her scalp, becoming stained with streaks of deep green."
    "The Drider’s former legs were absorbed into her humanoid body, becoming long, scuttling blades attached to the shoulders and back."
    "They stretched outward, growing nearly three meters in length, sharpening to a razor’s edge before curling behind her like the pinions of a huge, featherless bird."
    "The changes even reached her genitalia: the Drider’s juicy breasts ballooning in size even as they were enveloped in a black, chitinous coating."
    "Her hips widened, her ass plumped out, and her spider-pussy repositioned itself to the nexus of her crotch, growing a small but noticeable clit where none before existed."

else:
    "Rowan watched as the Drider let out a low, stomach-churning gurgle, his throat clenching as the changes took hold."
    dra "{i}Oh{/i}!"
    "The Drider’s features began to warp. His numerous eyes reshaped themselves, merging into a single, angular pair larger than a human’s eyes. His spider abdomen contorted, shrinking like a deflating balloon into his body as his legs shrank into their sockets."
    "The terrifying changes spread across his body: the black, chitinous armor of the former-Drider’s spider body spread across his skin, forming clothing-like coverage to his shifting physique."
    "A pair of humanoid legs appeared, thick and muscled, but in place of feet were black tips at the end like the spider’s former legs."
    "His arms became more angular, his fingers long claws of black chitin. The Drider’s white hair shrank into his scalp, becoming stained with streaks of deep green."
    "The Drider’s former legs were absorbed into his humanoid body, becoming long, scuttling blades attached to the shoulders and back."
    "They stretched outward, growing nearly three meters in length, sharpening to a razor’s edge before curling behind him like the pinions of a huge, featherless bird."
    "The changes even reached his genitalia: the curving barb that was his spider cock repositioning itself to his humanoid groin, growing an inch or two longer in the interim."
    "A set of chitinous testes formed beneath his sheath, creating a hardened sac for his gonads to reside."

"At last the changes ceased. The thing that had once been a Drider opened its eyes, revealing that same, canopy green shade that had inhabited the now-dead body lying on the ground. It smiled, and Rowan was struck by how similar it was to the old woman’s toothless grin."

arz "Beloved Handmaiden, you have returned!"

hand "Yes, Mistress. And stronger than ever!"
hand "Thank you my lady, for this priceless gift."

arz "Do not thank me dear, thank Rowan. It is he who has gifted you your new and improved form."

if driderSex == "female":
    "The Handmaiden bowed her head low, exposing her long back as her leg-claws swayed in a strangely seductive manner. They reached out and touched the ground, steadying her frame as she bent at a ninety degree angle."

else:
    "The Handmaiden bowed her - or rather, his - head low, exposing his rippling back as his leg-claws swayed in a strangely seductive manner. They reached out and touched the ground, steadying his frame as he bent at a ninety degree angle."

hand "Thank you, Master Rowan. You have granted me my deepest abiding wish."

ro "Don't mention it."

arz "How do you feel, my dear?"

if driderSex == "female":
    "The Fae lifted her hand, gazing in fascination at her new, supple arachnid body. The former Drider’s hands roamed up and down her feminine curves, pausing to grope at her hefty breasts. She licked her lips."
    hand "...Horny. I can feel the Drider’s spirit raging within me now: She is frustrated. Pent up. Ready to fuck."
    arz "I don’t doubt it, sister. You have been kept waiting for a long time."
    dra "By the twisting taint of Kharos! Look at her!"
    "The beastmaster marveled at the transformed Fae, despite her feminine features, it appeared that he still saw her more as a creature than a woman."
    "As he fearlessly approached her flank and began to poke and prod at her new legs, dragging his fingertips across the black armor before knocking his knuckles against them."
    dra "She’s amazing! The chitin has solidified to almost twice a Drider’s density, you could use a boar-spear and still struggle to pierce her armor now! Yet it does not seem to weigh much at all!"
    "The Fae seemed almost amused by the fawning adoration Draith was showering on her. She smiled, extending her leg-claws out as she stretched, letting out a Drider-like hiss of satisfaction."
    "Draith, caught up in the moment as he was, took hold of one of the legs and ran a finger across its edge. He drew back, staring in fascination at the blood that beaded from his fingertip."
    dra "-And the legs. Look Rowan: you see the muscles at the joints? Each of these claws are strong enough to cut a man in half! Not even a normal Drider has that kind of body strength!"
    "The Fae laughed, giving one of her aforementioned legs an experimental slice. Rowan was shocked at the reach that they had, extending almost to the other side of the pen in a single swipe."
    "The former Drider let out a low growl of satisfaction. Draith continued his excited inspection, leaning down and brazenly sliding a finger across her spider-cunny."
    dra "Hmm, I wonder if she’s sexually compatible with normal Driders. If we could breed her-"
    "The Fae snarled and slapped Draith’s hand away. The Elf let out a startled yelp and leapt back, reminded once more that this thing that stood before him was no longer the Drider he had once known."
    "She affixed him with a dark glare, and he shrank back, huddling once more behind Rowan."
    hand "Insolent whelp! I am no beast, to mate like a brood mare for your amusement!"
    hand "If I am to fuck something, it shall be on my terms. And I have far bigger prey in mind."
    #arz happy
    arz "Do you now? And… who might you have in mind, my dear?"
    "Rowan did not like the tone in Arzyl’s voice. She spoke with a certain humored quality, as if she already knew the answer to her own question. He felt the two Fae’s gazes swivel to him. There was a hunger in the Handmaiden’s eyes."
    hand "...My ‘saviour’ is a tasty morsel."
    arz "He is indeed, my dear."
    arz "Perhaps you’d like to… pluck him?"
    "The former Drider let out a low, menacing growl, before Rowan knew what was happening she rushed forward, moving with almost blinding speed, surging across the room with the help of her back-claws, pinning him to the wall."
    "Despite himself Rowan felt a thread of panic run down his spine."
    show rowan necklace angry at midleft with dissolve
    ro "{i}Arzyl{/i}! Control her!"
    arz "Now, now Rowan: I thought you would be pleased! It is a great boon for a Fae to bestow upon a mere mortal the honor of testing out her newest form. "
    arz "We Fae can get {i}really{/i} pent up when we switch between bodies; count yourself lucky she merely wishes to copulate with you, and not test her blades."
    "The Handmaiden flashed her fangs at him and leaned in for a kiss."
    
else:
    "The Fae lifted his hand, gazing in fascination at his new, muscular arachnid body. His hands trailed southwards, reaching down to give his large, onyx dick a few experimental strokes. The former Drider licked his lips."
    hand "..Horny. I can feel the Drider’s spirit raging within me now: He is pent up. Fuck hungry. Ready to rut."
    arz "I don’t doubt it, brother. You have been kept waiting for a long time."
    dra "By the twisting taint of Kharos! Look at him!"
    "The beastmaster marveled at the transformed Fae. He began to poke and prod at his new legs, dragging his fingertips across the black armor that covered them. Rowan spotted Draith making a few casual gropes of his rock-hard abs as well."
    dra "He’s {i}amazing{/i}! The chitin has solidified to almost twice a Drider’s density, you could use a boar-spear and still struggle to pierce his armor now!  Yet it does not seem to weigh much at all!"
    "The Fae seemed almost amused by the fawning adoration Draith was showering upon him. He grinned, extending his leg-claws out as she stretched, letting out a Drider-like hiss of satisfaction."
    "Draith, caught up in the moment as he was, took hold of one of the legs and ran a finger across its edge. He drew back, staring in fascination at the blood that beaded from his fingertip."
    dra "-And the legs. Look Rowan: you see the muscles at the joints? Each of these claws are strong enough to cut a man in half! A normal Drider has nowhere near that kind of strength!"
    "The Fae laughed, giving one of his aforementioned legs an experimental slice. Rowan was shocked at the reach that they had, extending almost to the other side of the pen in a single swipe."
    "The former Drider let out a low growl of satisfaction. Draith continued his excited inspection, leaning down and brazenly taking hold of his spider-cock. There was a slight, reddish tinge to his cheeks."
    dra "O-oh, and he’s grown, too!"
    dra "I wonder if he’s still sexually compatible with normal Driders. If we could breed him with-"
    "The Fae snarled and slapped Draith’s hand away. The Elf let out a startled yelp and leapt back, reminded once more that this thing that stood before him was no longer the Drider he had once known."
    "He affixed him with a dark glare, and Draith shrank back, huddling once more behind Rowan."
    hand "Insolent whelp! I am no beast, to mate like a breeding stud for your amusement!"
    hand "If I am to fuck something, it shall be on my terms. And I have far bigger prey in mind."
    #arz happy
    arz "Do you now? And… who might you have in mind, my dear?"
    "Rowan did not like the tone in Arzyl’s voice. She spoke with a certain humored quality, as if she already knew the answer to her own question. He felt the two Fae’s gazes swivel to him. There was a hunger in the Handmaiden’s eyes."
    hand "...My ‘saviour’ is a tasty morsel."
    arz "He is indeed, my dear."
    arz "Perhaps you’d like to… pluck him?"
    "The former Drider let out a low, menacing growl, before Rowan knew what was happening she rushed forward, moving with almost blinding speed, surging across the room with the help of her back-claws, pinning him to the wall."
    "Despite himself Rowan felt a thread of panic run down his spine."
    show rowan necklace angry at midleft with dissolve
    ro "{i}Arzyl{/i}! Control her!"
    arz "Now, now Rowan: I thought you would be pleased! It is a great boon for a Fae to bestow upon a mere mortal the honor of testing out her newest form. "
    arz "We Fae can get {i}really{/i} pent up when we switch between bodies; count yourself lucky he merely wishes to copulate with you, and not test her blades."
    "The Handmaiden flashed his fangs at him and leaned in for a kiss."
    
menu:
    "Is this really necessary?":
        $ released_fix_rollback()
        "Rowan grimaced under the unsubtle touch of the assertive Fae. Even as he spoke he could feel grasping claws casually groping his genitals."
        ro "Is.. {i}urgh{/i} - is this really necessary for your Handmaiden to do?"
        arz "Yes. The transference often leaves the host body physically pent-up and frustrated. The best means of dealing with that extra energy and combing the spirit is to get out that aggression, one way or another."
        show rowan necklace angry at midleft with dissolve
        ro "So why me?"
        arz "Why not? You should be flattered that you are my Handmaiden’s preferred choice."
        ro "And if I don’t wish to be?"
        if driderSex == "female":
            arz "She seems quite set on the idea… perhaps you just require a bit more incentive?"
        else:
            arz "He seems quite set on the idea… perhaps you just require a bit more incentive?"
        arz "I'll tell you what: if you allow my dearest Handmaiden to ravish you in a manner that only the Fae are truly capable of…"
        arz "I will allow your frail little servant to do whatever tests he wishes with my Handmaiden and the remaining Drider."
        dra "Deal!"
        ro "Damn it, Draith!"
        arz "So… what will it be? Shall my Handmaiden show you the sensual pleasures of a Trueborn?"
        jump driderSexMenu
        
    "Reprimand Arzyl.":
        $ released_fix_rollback()
        ro "Is this how you repay me for my kindness, witch? Siccing your minion on me? "
        arz "Calm yourself, my sweet. She is just trying to show her appreciation."
        ro "Regardless of whether or not I want it in the first place?"
        "The Fae let out an appreciative growl, gripping tightly to Rowan’s shoulders with its finger claws. The former Drider seemed to be waiting for Arzyl’s command… or her permission."
        arz "I'll tell you what: if you allow my dearest Handmaiden to {i}ravish{/i} you in a manner that only the Fae are truly capable of…"
        arz "I will allow your frail little servant to do whatever tests he wishes with my Handmaiden and the remaining Drider."
        dra "Deal!"
        show rowan necklace angry at midleft with dissolve
        ro "Damn it, Draith!"
        arz "So… what will it be? Shall my Handmaiden show you the sensual pleasures of a Trueborn?"
        jump driderSexMenu

    "Threaten the Handmaiden":
        $ released_fix_rollback()
        "Rowan realized that if he was going to stop the randy Fae, he’d have to put his foot down. His hand reached down to grasp the hilt of his sword, drawing the blade so as to ward off the aggressive creature."
        ro "Let me go. {i}Now{/i}."
        hand "I love it when prey squirms."
        ro "Lay your hands on me again, and you’re going to need another new host body before the day is through."
        if driderSex == "female":
            "The Handmaiden grinned, but Rowan could see the uncertainty grow in her forest green eyes. She turned, casting her gaze in the direction of her mistress, as if seeking Arzyl’s permission to continue. The Sorceress shrugged."
            "The Handmaiden let out a growl, but with some reluctance released her hold on Rowan, stepping away with a huff as she withdrew her shoulder-claws."
            "The warrior watched the creature with wary eyes, sheathing his blade but keeping his hand on his sword hilt. The Fae made a great show of stretching her body, plumping out her breasts and swaying her wide hips in a suggestive manner towards him."
        else:
            "The Handmaiden grinned, but Rowan could see the uncertainty grow in his forest green eyes. He turned, casting his gaze in the direction of his mistress, as if seeking Arzyl’s permission. The Sorceress shrugged."
            "The Handmaiden let out a growl, but with some reluctance released his hold on Rowan, stepping away with a huff as he withdrew his shoulder-claws."
            "The warrior watched the creature with wary eyes, sheathing his blade but keeping his hand on his sword hilt. The Fae made a great show of flexing his muscles and thrusting his hips in a suggestive manner towards him."
        hand "You missed out, Rowan. I was looking forward to having fun with you."
        show rowan necklace angry at midleft with dissolve
        ro "No doubt you were."
        #arz happy
        arz "There’s no accounting for taste, my beloved Handmaiden."
        arz "For what it’s worth: I cannot {i}wait{/i} to see what wonders you can perform for me in the bedroom."
        "The Fae cast a long, contemptuous glance back in Rowan’s direction."
        hand "-And I cannot wait to show you, my Lady."
        menu:
            "Demand the Handmaiden remain to be studied.":
                $ released_fix_rollback()
                ro "And just where do you think you are going?"
                jump handmaidenThreatened
                
            "Let them go.":
               $ released_fix_rollback()
               jump handmaidenEnding



label driderSexMenu:

show rowan necklace neutral at midleft with dissolve

menu:
    "Allow the sex to occur.":
        $ released_fix_rollback()
        show rowan necklace aroused at midleft with dissolve
        ro "...Fine."
        arz "You have chosen well, dear Rowan."
        jump driderTransformSex
        
    "Decline the offer":
        $ released_fix_rollback()
        ro "...No. Not interested."
        #arz annoyed
        arz "A pity."
        #arz neutral
        arz "Release him, my dear. Rowan does not seem interested in such playthings at the moment."
        "The Handmaiden hesitated, finger claws curling about Rowan’s chin as his brow tightened at the intrusion into his personal space."
        hand "B-but my lady! The Drider wants me to-"
        #arz angry
        arz "I said:"
        arz "{i}Release him.{/i}"
        if driderSex == "female":
            "Chastened, the former Drider stepped back, her back claws pulling away as she stretched to her full height. She cast a frustrated look down at Rowan, predatory eyes shining with hunger before she turned away in a huff."
        else:
            "Chastened, the former Drider stepped back, his back claws pulling away as he stretched to his full height. He cast a frustrated look down at Rowan, predatory eyes shining with hunger before he turned away in a huff."
        hand "As you wish, my Lady."
        arz "You have already been granted a great gift by this man, do not anger me any further by giving into your baser instincts like a pathetic mortal."
        #arz happy
        arz "Thank you Rowan for your help in this endeavor. The Midnight Court will remember the gift you have given us."
        menu:
            "This is not a gift. The Handmaiden will remain here to be studied.":
                $ released_fix_rollback()
                ro "Arzyl, I do not believe we are on the same page here."
                jump handmaidenThreatened
                
            "It was no trouble.":
                $ released_fix_rollback()
                jump handmaidenEnding
                
label driderTransformSex:

if driderSex == "female":
    jump driderFemaleVersion

else:
    jump driderMaleVersion

label driderFemaleVersion:
    
"The Handmaiden’s forest green eyes lit up at the sound of Rowan’s acceptance, glimmering with a ravenous need. She smiled, revealing a mouth of half-human, half fanged teeth. "

hand "You have made the correct choice, Rowan. "

"She stepped into his arms, her body moving with a spider’s slow grace as her foot-claws skittered forward."
"The Fae wrapped her arms around him, pulling him tight against her chest as her breasts squashed into him. The feeling of the hard chitin against his chest made a strange but pleasing dichotomy with the squishy texture of her large breasts."

hand "Mmm, you have no idea how long it’s been since I’ve had another hold me like this."

"Her clawed hands reached out, taking Rowan’s with surprising gentleness and guiding them to her hindquarters. He felt the curve of her plump ass, squeezing at the tender flesh that had grown in place of a spider abdomen." 
"The black armor coating formed a sort of seal upon her rump, only revealing the skin beneath as Rowan applied erotic pressure."
"The Handmaiden sighed as Rowan pulled aside her plating, his probing fingers finding purchase in the wet delta of her snatch as they squirmed their way inside."

hand "Yes… let me show you what my new form is capable of!"

scene cg611 with fade
show arzyl neutral behind cg611
show draith happy behind cg611
show rowan necklace aroused behind cg611
pause 3

"The Handmaiden’s hands reached down to cup Rowan’s ass, her finger-claws curling posessively around them before reaching around to grab at his crotch beneath his outfit. Rowan let out a low grunt as the spider’s sneaking fingers jerked him off through his clothing."

dra "She is showing immense restraint; the Drider would have mounted Rowan by now."

arz "A Fae can be just as bestial as any being, little beastmaster. But we are in control of our hosts. We choose when to let loose."

"The Handmaiden giggled as her claws tore a hole in Rowan’s crotch, allowing her grasping digits to take hold of him in the warmth of her palm. She stroked him, moaning as Rowan fingered her pussy with his hand."

if avatar.corruption > 60:
    "He felt an animalistic need rise up in his chest, and he reached around with his free hand to plant a loud spank against her fat rear. The Fae let out a cry of pleasure, and he repeated the action."
    
hand "Mmm, do you hear that, lover? Our audience is getting impatient with us. I wouldn’t want my mistress to leave disappointed."

"The Handmaiden smiled, showing her rows of fangs. Rowan lifted his hand, displaying for all to see the wet, glistening juices now flowing freely from her spider cunt."
"She put her hands to his chest, shoving Rowan to the ground before clambering over him as she let out a Drider-like hiss of satisfaction."
"The Handmaiden planted herself atop him, her fat bottom resting hard upon his crotch as she grinded up and down atop him. Her grasping, spiderlike limbs encircled them both like a cage, trapping Rowan in place as the Fae eagerly humped atop him."

hand "I can feel it: she wanted to take you herself."

ro "W-who?"

hand "My host. Her thirst is almost as unquenchable as mine - as unquenchable as ours is for you."

"The Handmaiden’s lips pressed against Rowan, a rough kiss of animalistic passion mixed with predatory hunger. She all but assaulted Rowan’s mouth, biting on his lower lip and eliciting a sharp yelp from him when her fangs poked into his skin. "

hand "I want to rip your clothing to pieces and mount you like a mare."

"Her spider claws tore at his clothing, ripping aside his paltry leggings to reach the juicy cock beneath. Her chitinous hand grasped Rowan’s prick, stroking it to full hardness as a wicked grin grew across her face."

hand "Can you feel it? My rejuvenated power?"

"Rowan could feel it… and it was more than just her touch, her fingertips spun threads of mystic power around and across his penis, the sensitive nerves of his dick responding to her flexes and pronations like a puppet to pulled strings."
"She toyed with him for a moment, manipulating his cock till Rowan thought he was about to burst."

scene cg612 with fade
show arzyl neutral behind cg612
show draith happy behind cg612
pause 3

"And just like that, the sensation spilled away. She took his rock-hard dick in hand and aligned it with her folds, her knife cut smile growing as he slipped between her insides. The spider matron settled her hips down onto his waist, letting out a low, rumbling coo as she bottomed out on him."

dra "{i}Amazing{/i}! She even moves like a Drider, despite the changes!"

arz "Have you heard that trite human saying: “you are what you eat,” little beastmaster?"
arz "For the Fae, the term takes on a far more spiritual meaning."

"The dark elf and Fae ambassador watched as Rowan groaned under the weight of the Handmaiden’s pounding hips." 
"Her chitinous black ass slapped against him, creating a rough sexual tempo that matched the hammering of his heart. She twerked and twisted in place, finding new and exciting angles to hump him as she eagerly mounted his manhood."
"The Handmaiden let out a deep growl, her grin widening across her cheeks as she flashed her fangs at her half-lover, half-prey. She picked up the pace, her black carapace bouncing against Rowan’s thighs as her body shivered and shuddered."
"The pace quickened, the two lovers from different dimensions gasped and groaned as the Drider-cunt swallowed his cock whole before pulling back, her lips clinging to his head before plunging back down again."
"Rowan let out a grunt, his balls tightening as his cock thickened within the Spider woman. The Fae let out a keening screech, half Drider and half something else in tone. She lifted her head skyward, her mouth going slack as her pussy clenched around the cock jammed within it."
"Rowan came, shooting his seed deep within the Fae’s newfound spider-pussy. Arzyl watched, her hand drifting beneath her robes to rub at herself as she bit her lip. Draith looked excited."
"The Fae panted above Rowan for a moment, then lifted herself off of him on her powerful legs, a string of white seed leaking out of her used fuckhole as she walked over to Arzyl."

scene bg25 with fade
show draith happy at edgeright with dissolve
show arzyl neutral at midright with dissolve

arz "Well done my Handmaiden. I see your new body has done nothing to dampen your sex drive."

hand "It was my pleasure, Mistress. This new body is far more vigorous and resilient than my previous one."

show rowan necklace aroused at midleft with dissolve

"Rowan picked himself up off the ground at the same time as Arzyl led her rejuvenated Handmaiden back through the portal she had created. The half-Drider being gave him a naughty wink as she left."

dra "Wow, now wasn’t that something?"

#Add a small increase to drider power and Draith relationship - TODO
#Relationship with Arzyl/MC, Lose a Drider - TODO
return

#############################################################

label driderMaleVersion:

"The Handmaiden turned, his forest green eyes burning with a ravenous need. He grinned, revealing a mouth of half-human, half fanged teeth."
"He strode towards Rowan with an arachnid’s confidence, taking the warrior by the wrist and pulling him roughly into his arms. He was graceful, forceful in his movements. As the Fae wrapped his arms around him, Rowan felt the breath stealing from his lungs. "
"The pale skin of the former Drider gleamed like a mirror’s sheen in the torchlight of the breeding pits. The feeling of the hard chitin against Rowan’s chest made his heartbeat quicken."

hand "Mmm, you have no idea how long it’s been since I’ve had someone in my arms like this."

"His clawed hands reached out, sliding across Rowan’s ass, kneading at his hindquarters as he let out a contented growl." 
"Rowan felt the tickling curve of his clawed fingers drag possessively across his cheeks, plump ass, squeezing at the tender flesh as the bulge of his spider cock grew thicker between them. "
"A similar bulge was building in Rowan’s pants, his hands sliding across the Fae’s sweaty skin as they traced the thick muscles of his bare chest." 
"His eyes were upon Rowan’s, a hungry smile growing as the former Drider made an experimental hump, frotting with Rowan through the covering of his leggings."

hand "Yes… let me show you what my new form is capable of!"

"The Handmaiden’s hands reached down to cup Rowan’s ass again, his finger-claws curling posessively around them before reaching around to grab at his crotch beneath his outfit. Rowan let out a low grunt as the spider’s sneaking fingers jerked him off through his clothing."

dra "Wow... he’s uh… q-quite spirited!"

arz "Do try to contain your pathetic libido, beastmaster. I can see you squirming from here. You look like a wine bottle about to pop its cork."

dra "Y-yes ma’am! I j-just wasn’t expecting him to be still so… ah, aggressive?"

arz "A Fae can be just as aggressive as any creature. But we are in control of our hosts. We choose when to let loose."

"The Handmaiden cackled as his claws tore a hole in Rowan’s crotch, allowing his grasping digits to take hold of him in the warmth of his palm."
"He stroked him, moaning as Rowan’s hands wrapped around his onyx dick, marveling at its superior size. The air grew thick with the scent of masculine arousal."

hand "Mmm, do you hear that, lover? Our audience is getting impatient with us. I wouldn’t want my mistress to leave disappointed."

"The Handmaiden smiled, displaying his rows of fangs. He thumbed Rowan’s cock, coating his black fingertips in precum so that they glistened. He lifted his hand displaying the sticky juices as they stretched between his fingertips."
"The Handmaiden put his hands to Rowan’s chest, shoving the warrior to the ground before clambering on top of him as the Fae let out a Drider-like hiss of satisfaction."

hand "Hmm, what have we here? A tasty morsel, barely even a snack."

"The Drider pinned Rowan’s hands above his head, flopping his turgid black spider cock on top of Rowan’s, dwarfing his size and asserting his dominance. Rowan squirmed in place, but could do little to free himself from the creature’s iron grasp."

hand "I can feel it: he wanted to take you himself."

ro "W-who?"

hand "My host. His hunger is almost as unquenchable as mine - as unquenchable as ours is for you."

"The Handmaiden’s lips pressed against Rowan, a rough kiss of animalistic passion mixed with predatory hunger. He all but assaulted Rowan’s mouth, biting on his lower lip and eliciting a sharp yelp from him when the Fae’s fangs poked into his skin. "

hand "I want to rip your clothing to pieces and fuck you like a cheap whore."

dra "O-oh, wait! Hold on, before you begin!"

"The Fae let out an annoyed growl as Draith rushed over to the two, pulling a small vial of clear liquid from his belt. Rowan watched from his compromised position beneath the former Drider’s bulk as the waifish Elf squeezed in on one side."
"He spread Rowan’s bare buttcheeks as he popped the vial’s lid and applied a small stream of the liquid to his fingertip. Draith dabbed the finger against Rowan’s twitching asshole, sending a shiver of sensitivity up the hero’s spine at the warm, wet feel of it."

ro "What the hell are you doing?"

dra "Applying lube. Trust me: from personal experience, you’ll thank me later."

scene cg528 with fade
show arzyl neutral behind cg528
show draith happy behind cg528

"Comprehension dawned on Rowan as he realized what was about to happen. The Handmaiden dragged his long, black cock up across Rowan’s own smaller length before sliding back again to align himself to the recently-lubed hole." 
"Draith stared at the entrance, squinting one eye as if he were an artist inspecting their latest work. He clapped his hands and stepped away, a noticeable blush in his cheeks and stiffness in his groin." 
"A wicked grin grew across the Fae’s face as the tip of his cock touched the entrance to Rowan’s backside."

hand "Can you feel it pressing against you? Sliding in like-"

"Rowan stared up at the Fae, whose forest green eyes gazed back at him with erotic authority. Though Rowan would never admit it,  laid out on the ground with his legs spread and his ass getting reamed, he felt a submissive thrill of pleasure run through his body."
"The Fae began to move, sliding his big, black spider dick in and out of the wet hole he had claimed as his own. Rowan grunted, his erect cock flopping against his stomach with every thrust." 
"His stomach clenched around it, and he found himself leaning into the abuse as the former Drider’s clawed hands ran up and down his chest, tweaking his nipples and scraping across his pecs."

dra "{i}Amazing{/i}! He even moves like a Drider, despite the changes!"

arz "Have you heard that trite human saying: “you are what you eat,” little beastmaster?"
arz "For the Fae, the term takes on a far more spiritual meaning."

"Rowan’s face burned with humiliation as the two voyeurs watched him get fucked on the breeding room floor. The Fae, seeming to sense his trepidation, picked up the pace, driving more and more of his slick cock deeper into his rectum."
"The pale-skinned creature laughed, tossing his red-tinged hair around as he adopted a fast, frenetic humping pace. Rowan could do little but brace himself against the floor as the Fae took him for a ride."
"The Handmaiden let out a deep growl, his grin widening across his cheeks as his flashed his fangs at his half-lover, half-prey. He picked up speed, his black carapace cock bouncing against Rowan’s thighs as draped his legs over his shoulders and laid into his ass."
"The pace quickened, the two lovers from different dimensions gasped and groaned as the Drider dick pressed deep enough to poke Rowan’s prostate before pulling back, his ass clenching against the cockhead before it plunged back in again."
"Rowan let out a cry of pleasure, his balls tightening as he orgasmed from the repeated stimulation of his g-spot. "
"Cum spurted from his tip and shot across his stomach, some of it even landing as high as his chest."
"The Fae let out a growl, half Drider and half something else in tone. He lifted his head skyward, roaring as his dick thickened within Rowan and unloaded its deposit of seed deep within Rowan’s rectum. He kept thrusting through the orgasm, grunting and groaning as his hands molested Rowan’s sides, chest and shoulders."
"Arzyl watched, her hand drifting beneath her robes to rub at herself as she bit her lip. Draith looked excited, his cheeks beet red and his eyes alight with erotic tension."
"The Fae panted above Rowan for a moment, then pulled himself free, jerking his cock over Rowan in a display of dominance. Content that he had dribled out the last drops of cum onto Rowan’s stomach, he walked over to Arzyl."

scene bg25 with fade
show draith neutral at edgeright with dissolve
show arzyl neutral at midright with dissolve


arz "Well done my Handmaiden, I see your new body has done nothing to dampen your sex drive." 

hand "It was my pleasure, Mistress. This new body is far more vigorous and resilient than my previous one."

"Rowan, exhausted and covered in two people’s cum, picked himself up off the ground at the same time as Arzyl led her rejuvenated Handmaiden back through the portal she had created. The half-Drider being gave him a naughty wink as she left."

dra "By the Plane of Chaos... Rowan, do you know when he'll be back?  I think I'll have to take a turn to test his body before we move onto the Drider!"

#Add a small increase to drider power and Draith relationship - TODO
#Relationship with Arzyl/MC, Lose a Drider - TODO
return

label handmaidenEnding:

if driderSex == "female":
    "The now-transformed Fae scuttled with a Drider’s rapid gait over to her mistress. Arzyl pulled her into a kiss, and for a short moment the two roughly made out."
    
else:
    "The now-transformed Fae scuttled with a Drider’s rapid gait over to her mistress. Arzyl pulled him into a kiss, and for a short moment the two roughly made out."

arz "{i}Mwah{/i}!"
arz "Mmmm, I think I’m going to like this new you, my dear."
arz "Very well, if there is nothing more you wish of us then, Rowan? I believe I am going to test my loyal servant’s new body out myself."

#Relationship with Arzyl/MC, Lose a Drider - TODO
return

label handmaidenThreatened:

ro "You said you would let us study the methods of the soul transfer."
ro "You showed us the ritual, but that is not enough. I expect your Handmaiden to return later, so Draith can examine her further. "

"Arzyl’s let out a contemptuous sniff."

arz "I said I would allow you a glimpse. And I have kept my word. "

ro "Don’t play word games with me, Arzyl. That’s {i}my{/i} Drider your Handmaiden is occupying, so far as I’m concerned, she’s half mine now."

#arz angry

arz "You would {i}dare{/i}-"

ro "But we’re not here to bicker, are we? Allies, gifts, and all that."
ro "I have granted you your wish. The least you can do is to abide by my beastmaster’s request, and let him study your Handmaiden."

arz "..."

#arz neutral

arz "Very well."

hand "M-mistress!"

"The Fae Ambassador silenced her minion with a rough kiss, reminding everyone in the room that despite whatever physical might the now-reborn handmaiden possessed, she was still just a servant."

arz "Shh, do not worry my dear. I will make sure to thoroughly examine your body first. You’d like that, don’t you? "

"A hungry moan was all the confirmation she needed. Arzyl answered Rowan with a respectful nod."

arz "You drive a hard bargain Rowan, but as allies-to-be, I will acknowledge your words. My Handmaiden will be at your filthy Elf’s disposal… for a time. "

ro "I expect the handmaiden to behave. If I hear they are bullying Draith, I will return for my half. "

arz "For a beastmaster to require a caretaker of his own… how pathetic."

ro "Arzyl..."

arz "She will behave. Now, if you do not mind, I must break my lovely Handmaiden in. {i}Again{/i}."

if driderSex == "female":
    "The Fae left with her giggling Handmaiden in tow. Draith gave Rowan a shy thumbs up, pleased by the end result, if slightly terrified of the prospect of upcoming evenings with the Drider hybrid."
    
else:
    "The Fae left with her giggling Handmaiden in tow. Draith gave Rowan a shy thumbs up, pleased by the outcome.  "

##Add a small increase to drider power and Draith relationship - TODO
#Relationship with Arzyl/MC (but lower than what you get otherwise), Lose a Drider. - TODO
return

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

label spanks_for_the_memories:
    
scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show liurial aroused at midright with dissolve

"Something was getting in the way of the normal paperwork routine. It was subtle, but ever since he’d joined her in their little corner of the throne room, Liurial hadn’t stopped giving him side glances. It was as though she were giving him one every few minutes."
"Rowan took a deep breath and set the ledger down."

ro "Is there something you wish to say to me?"

"Liurial paused as if she’d been caught sneaking food from the pantry. But, to her credit, she didn’t try to ignore the question. She slowly rose to her feet and took a position standing straight in front of his desk."

liur "There is. Yes."

"Rowan leaned back in his chair, keeping his eyes trained on her."

liur "You told me that I shouldn’t have any orgasms without your express permission…"

ro "Yes."

liur "Last night, I was…"

"Rowan raised an eyebrow. It was not hard to see where this was heading."

ro "You broke the order?"

liur "..."

"She blushed softly and looked to the side, no longer capable of meeting his eyes."

liur "I did."

"Rowan didn’t speak. His mind was whirring at lightning speeds. But, it left the nervous elf standing, still at attention, growing increasingly more unsteady the longer he went without reacting."

liur "The entire time we were working, it made me feel so guilty because you told me not to. I could not refrain from telling you much longer. I wanted to tell you when you first arrived, but it was too difficult."

"Rowan sighed. He’d told her not to cum without his assent. The entire purpose was to maintain control over her. No matter what, he couldn’t simply let her go without some kind of correction."
"The question was...how?"

menu:
    "Chastize her.":
        $ released_fix_rollback()
        "Clearly, if there was one thing that she needed here, it was a bit of discipline. Rowan had been through army life. It would not be hard to channel."
        "Rowan rose from his chair, standing tall enough over Liurial that she would be forced to look up if she wanted to meet his eye. Not that she would meet his eye."
        ro "Did I give you permission to cum?"
        liur "No..."
        ro "And you understand the nature of our dynamic, right? If I tell you not to do something, you obey. It doesn’t matter how much you want to cum."
        liur "But…"
        "Rowan glared and put his hands on the table."
        ro "This will not happen again. Do you understand me?"
        "Liurial nodded softly."
        ro "You have been disobedient. I am not happy about that. Not at all."
        ro "And do you want me disappointed or pleased?"
        liur "Pleased…"
        "Her eyes were now firmly pointed at her feet. When you dress down someone this way, they tend to take on the demeanor of a punished child."
        ro "So, will this happen again?"
        "She shook her head."
        ro "Good. Get back to work."
        liur "Yes, my lord."
        "Rowan’s words had served their purpose. Liurial did hurried work throughout the day, running through even more of the work than normal. Rowan had to stop himself from smiling as he saw her stack of finished papers grow."
        "Every so often, she’d send Rowan a little glance. No longer one of guilt, but a search for approval. Rowan wasn’t going to give her any such thing today, not when she was still being punished." 
        "But, if she was still uncertain in the future, Rowan wasn’t going to hold it out. She normally tried her best, and that was what mattered."
        return
        
    "Spank her.":
        $ released_fix_rollback()
        jump liurialSpank
        
label liurialSpank:
    
if week < 60:
    "Rowan froze. Clearly, he was meant to discipline her. Perhaps that was even what she wanted. Liurial was looking at him expectantly. He’d already been commanding with her. That was just the role to be played..."
    
"Rowan slowly rose from his chair and walked around the desk. He was now standing within arm’s reach of her. Liurial’s eyes rose enough to see what he was doing."

liur "My lord?"

#cg var 1
scene black with fade
show rowan necklace neutral behind black
show liurial aroused behind black

"Then, Rowan pounced. His hand twisted into her long blond hair, and he used his superior strength and size to force her down against the wooden table. The sound of her surprised shriek was overcome by the bang of her body against the wooden surface."
"In all of the chaos, that strange elven hat she wore fell to the ground."

ro "You have been a disobedient girl. Disobedient girls get punished, Liurial. You have to know that by now."

"Liurial gasped and squirmed under the force of his body. Yet, she wasn’t trying to break free."

liur "Y-yes. They do…"

if week < 60:
    "Rowan breathed inwards, collecting the energy needed to do this right."
    
else:
    "Rowan’s eyebrows remained furrowed. Living here for so long made a man accustomed to the concept of sexual discipline."
    
ro "Are you ready?"

"Liurial let out a loud gulp. She tried to give an energetic nod too, but Rowan’s grip on her hair made it rather difficult. Still, her assent had been signaled."

if avatar.corruption < 31:
    "That assent was important. The difference between him and the monsters..."

#cg var 2
scene cg557 with fade
show rowan necklace neutral behind cg557
show liurial aroused behind cg557

"Rowan drew his hand back slowly. The time it took would only add to the effect. Like the uncertainty of slow movement in battle. Waiting and waiting for the strike."
"Then his hand rushed forward, striking the left side of Liurial’s ass. The force of it ran through her entire body, leaving her still shaking and squirming moments later."

liur "Ahhh!"

"A bright red hand was left on her rear. The first step towards the kind of bruises that would make it hurt for her to sit down."
"Before Liurial could steady herself, Rowan brought his hand down for a second and third time. A long involuntary groan slipped from her lips and she responded to each strike by wriggling beneath him." 
"Her involuntary process was flight like a small animal. But, the look on her face revealed all of her thoughts."
"Liurial was whimpering and gasping. Desperate sounds were being drawn from her lips with every strike. Another expression of mind numbing arousal and pain."
"The spankings continued, one after another. Rowan was always alternating position, always ensuring that a different spot felt the stinging pain. Liurial’s cheeks slowly drifted into a dark shade of red. Both her ass and her face."
"There was no escape from her. He had a duelist’s hands. Too strong to wrench free from his grasp. Too precise and skilled not to feel what he wanted her to feel. Stinging pain."
"A strike produces a gasp. A slap a long moan. She was his instrument."

if helAlexiaWhip == True:
    "Rowan wasn’t totally able to enjoy the moment. There was a memory in the way. His own wife naked. Rowan lashing at her with a whip while the demons watched."
    "Liurial’s moans and groans were much lighter and more obviously interspaced with arousal. But, the memory lingered...the one thing getting in the way..."
    
"Liurial was left gasping by this point. Barely even able to string together coherent sentences. "

liur "I’ll be a good girl….Please...It was wrong of me to cum without permission. I...I won’t disobey again. Please…"

"Rowan relented for a moment, hand still hanging in the air ready to strike out again."

ro "You swear?"

liur "Yes, please….I swear it. I swear. I won’t cum without your permission...Please…."

"Rowan’s hand still hung in the air. It really did seem as though she had learned her lesson. A quick glance at her backside revealed the extent of the punishment. She was already starting to bruise. It also revealed something else..."

ro "You’re wet."

"Her panties were easily exposed from this position. The dark, damp patch on them couldn’t be hidden from view. Her body was practically crying out in need."
"Liurial whimpered."

#cg var 3
scene cg662 with fade
pause 3

"Rowan brushed his fingers along her lower lips through the soaking fabric of her panties. There was no mistaking it. Liurial’s body shivered at the touch, or at the very least from the residual pain from the spanking."
"Perhaps he could discipline her better with a bit of pleasure to go along with the pain."
"He brushed her panties to the side. Then two of his fingers worked their way into her pussy and started pumping." 
"She immediately was moaning and rocking her body. Fucking his fingers as eagerly as though it were his cock. But, with his hand in her hair, he still controlled her body."
"She moved as much as he would allow."
"Liurial’s eyes looked glazed over, as though she were spaced out in entirety. She was moaning and moving and responding to each thrust. But, the stimulation had passed the point her brain could keep up. "

scene cg663 with fade
show rowan necklace neutral behind cg663
show liurial aroused behind cg663
pause 3


ro "I understand. I understand."
ro "You liked the spanking, didn’t you? You were crying and pleading, but you were enjoying yourself the entire time."

"Liurial responded only with gasping moans that were themselves half stifled by the desk."
"Rowan toyed with her cunt as relentlessly as he’d spanked her before. A constant steady source of sensation that she could not escape from. Liurial was a toy in his hands."
"Through gasping breaths, she forced out words or at least sounds that resembled words close enough to be understood."

liur "If you...if you keep this up, going to…going to..."

menu:
    "Let her cum.":
        $ released_fix_rollback()
        ro "Ask me nicely, Liurial. After all, you have to ask, don’t you?"
        "He suddenly pulled his fingers out. Leaving Liurial panting, squirming, even dripping all over the desk."
        liur "Ah. Ah. Please. Please let me cum."
        ro "Much better. You can cum."
        show cg664 with flash
        pause 3
        "He plunged his fingers back inside of her, eliciting a loud cry. It only took seconds after that. He pumped his fingers inside of her with so much power that she was bucking and cumming in seconds."
        scene bg6 with fade
        #rowan smirk
        show rowan necklace neutral at midleft with dissolve
        show liurial aroused at midright with dissolve
        liur "Ah..."
        liur "Thank you…"
        "Liurial’s eyes drifted open and shut slowly. Rowan withdrew his hand and slowly made his way to the other side of the table. But, his hand never left her entirely. The back of his hand stayed at her cheek, acting as an anchor for her."
        ro "So you’ll ask next time, won’t you?"
        "A groan rose from her lips. That meant yes."
        "Rowan let her stay like that, even as he went back to his seat. He picked documents from his stack and worked to read them."
        "Still, he kept the back of his hand pressed to Liurial’s cheek. Every so often she’d nuzzle into it and let out a happy sound."
        "Rowan waited until she seemed more functional and present before withdrawing the hand." 
        ro "Okay. You had your fun. Now it’s time to get back to work."
        "Liurial groaned, but by now she was back to basic mental functions."
        liur "Yes, my lord."
        "She practically skipped back to her desk, first pausing to retrieve her hat and her panties. Rowan glanced, with great admiration, at his handiwork. A series of black and blue bruises on her rear that would remind her of the importance of obedience."
        "Not that she seemed to broken up about it. Whenever Rowan looked over her direction, she had a big goofy grin on her face as she worked."
        "It made Rowan smile too."
        return
        
    "She doesn't deserve to cum.":
        $ released_fix_rollback()
        "Rowan didn’t even need to consider it. The moment she started to talk of orgasm, his hand flew back."
        scene bg6 with fade
        show rowan necklace neutral at midleft with dissolve
        show liurial aroused at midright with dissolve
        liur "..."
        liur "...huh?"
        "Rowan waited, hand still in her hair, for her mental process to return to the level that she could process what he was saying."
        ro "Do think that I’d just let you cum when I’m punishing you for cumming without permission?"
        "A moment of silence. Then an answer in a sad little voice."
        liur "...No."
        ro "So, in a moment, you’re going to go back to work. You’re definitely not going to touch again today. Especially not if you don’t want to see what a worse punishment would look like."
        "Liurial pouted, but there was little she could do when confronted with such a fitting punishment. Still, Rowan let her curl up on the desk, still squirming and letting out the odd whimper for the next half hour."
        "He was punishing her, but being cold wasn't his intent."
        "Still, there was work that needed to be done. When Liurial finally seemed to be back in something normally resembling her state of mind, he sent her back to her desk."
        "Rowan took a special joy in the odd gasps from her mouth or the way that she constantly shifted positions. It was though she had an itch that she could not scratch."
        "But, whenever she looked to him, Rowan couldn’t help but see a soft smile beneath her pout. It made him want to smile too."
        return


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

label dream_of_wolves:

scene bg3 with fade
show rowan necklace neutral at center with dissolve

"The hidden forest trail stretched onwards into the distance like an emerald eternity." 
"There was something primal about this place, something virgin and unspoiled. Rowan could feel the life force of the whole world flowing through the earth beneath his feet, in the coiling roots between his toes." 
"He was at peace here, one with nature and the mother-forest that sheltered him in her protective embrace. Rowan lifted his nose and breathed in the moist forest air." 
"He paused. The scent of prey tickled his nostrils, leading like an unseen blood trail into the distance." 
"Rowan smiled to himself. His pack would eat well tonight."
"He took off into the brush, making sure to stay downwind of his prey. The quick-witted Wolf-kin followed the scent for over a mile, his heart pumping in his chest as he leapt over fallen trees and sprinted between the gaps of thorn bushes."
"Rowan stopped dead. The scent of prey was all around him. He tensed himself to strike, watching like a hawk for any change in scenery."
"Then, a movement: a flash of tan fur amidst the sea of green foliage. The chase was on."
"A predatory instinct Rowan could neither define nor control compelled him to pursuit. His legs moved with the blinding speed of a beast on the hunt, his mind fixed to the target in front of him: his prey, his meal."
"The Deer stood no chance. It had spotted him far too late. It’s fight-or-flight instincts were useless against a being as deadly as Rowan."
"His claws were like scimitars, his teeth like ripping daggers. He was faster, stronger, {i}smarter{/i} than his prey. This was the logical state of being: the strong survived, the weak served to strengthen and feed. And Rowan was indeed strong."
"He closed the distance in seconds as the Buck leapt high to escape his snapping jaws. Rowan was so close, he was nipping at its back legs-"
"A white blur descended from an unseen angle in the forest canopy above. Rowan skidded to a stop, his honed instincts warning him of imminent danger."
"A second predator entered the fray. The white blur leapt from the branches above and pounced on the blindsided Buck. Rowan’s mind caught up with his instincts, recognizing the white-furred predator to be a Wolf-kin like him." 
"The interloper tackled the Buck, using her weight and momentum to bring it crashing to the ground. The Buck let out a cry, blood fountaining into the air as the White Wolf latched her teeth around its neck and tore its throat out. A few shakes and a second bite, and the Deer lay motionless upon the ground."

menu:
    "Another predator. Observe her cautiously.":
        $ released_fix_rollback()
        "Rowan bared his teeth, circling the uninvited assailant with caution.  She was not of his pack, her markings and her foreign scent made that clear."
        "But Rowan had not been raised to leap headlong into danger. He first had to determine if this was a fight worth having."
        
    "She took HIS kill! Attack!":
        $ released_fix_rollback()
        "Rowan snarled at this intruder, who was she to deny him his prey? She was not of his pack, her markings and her foreign scent made that clear." 
        "She was a rival huntress, and she had {i}stolen his kill{/i}."

"The intruder wolf’s yellow eyes focused upon him, baring her fangs to ward off her competitor. Rowan let out a threatening roar, and she responded in kind, snarling at him. The two circled each other, the dead Buck separating the two rivals as they prepared to fight for the right of the kill."
"Rowan charged at the same time she did, meeting somewhere in the middle as they became an indistinguishable pile of gnashing teeth and flared fur."
"The contest was fierce: when he slashed at her stomach, she bit him on the shoulder. When Rowan attacked her from the side, the White Wolf snapped at his hind legs."
"The two fought like animals caught in a death spiral: neither willing to return to their pack empty handed. Both ready to fight to the death rather than cede dominance to the other."
"The battle went on and on, far longer than bestial logic or survival instinct would normally allow in such a contest."
"At last, Rowan used his superior weight and size to leap atop her, pinning her to the ground with his arms as she nipped and roared and snarled at him. Despite his wounds, he had gotten the better of her. Yet still she struggled."

menu:
    "Pacify her.":
        $ released_fix_rollback()
        "The White Wolf tried to squirm free from beneath his weight, but a bellowing roar into her face chastened her at last. Exhausted, she stopped struggling and collapsed against the ground, defeated."
        "Rowan growled at her, flashing his eyes and making sure in no uncertain terms she knew who had won. The White Wolf let out a whine and bared her neck to him, a sign of utter submission. Her yellow eyes never left his as they both panted from the exertion."

    "Humiliate her.":
        $ released_fix_rollback()
        "Rowan wouldn’t let the insult stand. He took hold of the White Wolf’s face, grinding her cheek into the earth as she growled and yelped in pain. She squirmed and writhed beneath him, but it was useless: he was stronger than she was. He wanted her to {i}know{/i}."
        "After a last, frantic effort to free herself she collapsed against the ground, unable to maintain her feeble resistance. Rowan reveled in the feeling of putting his rival in her proper place: helpless, terror-stricken, unable to resist his might." 
        "Rowan ran a claw across her cheek as she shuddered, powerless to stop him. The White Wolf let out a whine and bared her neck to him, a sign of utter submission. Her yellow eyes never left his as they both panted from the exertion."

"Rowan snapped his jaws in her face as a final warning and then withdrew, moving to secure his hard-fought kill." 
"The moment he was off of her, the White Wolf moved to bolt into the underbrush. He let out a low growl of warning. She gave a second, longer whine and sat back on her haunches."
"The White Wolf watched in submissive silence as he took hold of the dead deer between his jaws and began to drag it towards his family’s den." 
"Rowan cast a long look over his shoulder at the conquered Huntress, letting out a commanding growl between his teeth. He gestured with his head in the direction he was headed, then disappeared into the underbrush."

show rowan at edgeleft with moveoutleft
show heartsong neutral at center with dissolve

"He felt more than heard her soft footsteps behind him as she followed him back to his den."

scene bg3 with fade
show rowan necklace neutral at midleft with dissolve

"Time passed. There was no way of quantifying the changing of seasons to his kind. Only a vague, instinctive appreciation of the shifting nature of the hunt as the weather cooled, the leaves changed color, and game became more scarce."
"Rowan had outgrown his original family, separating from his birth pack and his Alpha father when it became clear he was no longer welcome."

show heartsong neutral at midright with dissolve

"The time had come for him to set out on his own in search of new territory to hunt. When he left the pack, the White Wolf followed along after him, silent and watchful as always." 
"She had become his faithful companion: traveling with him, hunting with him, sharing the warmth of their body heat in the depths of the night. He had come to rely on her, and she in turn had learned to share her meals."
"Their pecking order had been clearly established by that first, intense encounter: he led, and she followed. They protected each other. Such was the way of things. They had become quite the pair."
"One day, late in the afternoon as they coaxed a hare away from its burrow in tandem, Rowan caught wind of a scent that he had never smelled before."
"Just as he flushed the floppy-eared prey from cover, he sniffed something sweet upon the wind. His head snapped around, craning his neck to stare at the White Wolf. Her rump was turned towards him, her tail held high as she chased after the tiny creature, catching it in her jaws. "
"The White Wolf grinned in excitement through the meat in her teeth. She loped over to him and spat the hare out at his feet, her eyes alight with joy at having brought him the kill."

menu:
    "She is… beautiful.":
        $ released_fix_rollback()
        "Rowan looked at his companion for the first time in a new way. She was strong, yes: a loyal pack mate and an excellent hunting partner. But… this feeling about her was different. Intangible. Instinctive."
        "Rowan circled her, and the White Wolf froze, paralyzed by his gaze. The two stared at each other, exchanging words without words as their eyelids lowered and their tongues grew heavy in their mouths."
        show rowan necklace aroused at midleft with dissolve

    "She is mine.":
        $ released_fix_rollback()
        show rowan necklace aroused at midleft with dissolve
        "Rowan stared hungrily at the White Wolf, feeling a gnawing need build in his gut. He had conquered her: submitted her will to him as the superior specimen all those months ago. And now she did as her Alpha bid, following where his whims took them."
        "Rowan prowled around her, his tongue hanging out of his mouth as he felt heat build in his loins. Taken aback by her partner’s sudden aggression the White Wolf froze, paralyzed by his hungry gaze. He lifted his head and took a deep inhale, sensing her tense back."

scene cg677 with fade
pause 3

"He circled her a second time, pausing this time to stare at her ripe breasts and juicy hindquarters, noting that the scent was coming strongest from her rear. She stood stock still in place, as if she were prey readying to bolt, but the White Wolf did not move an inch without his permission."
"He approached her from behind, sniffing, sniffing at the sweet scent she gave off. He put his nose against her pink slit and inhaled deeply, his nostrils flaring at the erotic scent. The White Wolf whimpered at the feel of his breath against her genitals."
"Rowan felt a rush of adrenaline, his nose burying itself into her rump as he breathed in the intoxicating scent coming from her cunny. He gave an experimental lick, marveling at the sweet nectar that leaked from her femininity."
"The White Wolf let out a moan, hiking up her ass so that Rowan might have easier access to her nethers. It seemed she liked his touch."
"Rowan began to lick and slide his tongue up and down her lower lips, his mind awash with primal urges as his cock grew painfully erect beneath him."
"Her pheromones were unbearable, like a fire burning from the inside that had caught the dry brush of Rowan’s mind ablaze in its destructive path."
"He buried his face in her pussy, licking with wild abandon as he growled and nipped and bit at her plush butt. Far from being angry, the White Wolf mewled with hungry need, forgetting entirely the hare and their meal in place of this new, wonderful thing they had discovered."
"Rowan spread her ass, slathering her with kisses and licks until her crotch was soaked and she was crying out with pleasure. The noise rebounded across the forest clearing with a loud, cacophonous echo. They’d likely scared away the game for miles around; Rowan couldn’t care less."
"The White Wolf’s upper body went to the ground, her arms clinging to the uneven forest floor as Rowan lapped again and again at her sweltering honeypot."
"Rowan was getting dizzy, pussy-drunk on the scent of the pheromones she exuded from her muff. He was rock hard, dribbling precum from his cockhead and humping the air in desperation for release."

scene cg678 with fade
pause 3

"Flush with animal need, he mounted her, pistoning his hips at such a frantic pace that Rowan slipped and missed on his first stroke, the topside of his cock slathering across her slick slit and coating it in her feminine juices."
"The White Wolf gasped, her body tensing with anticipation at their impending mating. She humped back against him, as eager to quench her heat as he was to fill her. It only complicated the delicate biological process as he slipped and slid his turgid length across her hot, wet snatch."
"Frustrated in a way only a rutting male could be, Rowan drew back his hips, let loose a bellowing roar, and speared her entrance with his cock. The White Wolf’s head lifted from the ground, her ears standing on end as she let out a cry of half-pain, half-ecstasy."
"Rowan adjusted his weight, reveling in the warm, wet conquest of his pack mate. She whimpered beneath him, her pussy tightening, squeezing his cock like a vice. The pleasing sensation urged him onwards, and before Rowan’s conscious mind had time to process he was thrusting into her depths."
"They moved as one, rolling their hips together in a hypnotic rhythm that was not borne of experience, but basic instinct. The White Wolf let out a gasp, her arms going out from under her as she lifted her ass in the air to further facilitate Rowan’s rough fucking." 
"There was a wet {i}squelch{/i} every time he hilted within her. Each time he hit that particular depth she let out a scream of orgiastic approval. They mated like beasts beneath the boughs, thrusting and bucking against one another with little subtlety and less restraint." 
"Rowan picked up the pace, his hands reaching around her to grope at her chest and her hanging teats. The White Wolf groaned, helpless to the sensation of being roughly taken like a bitch in heat." 
"Rowan laid himself atop her, smothering her with his weight, claiming her as his own. She submitted to him, bucking her hips back against him in tune to his aggressive thrusts." 
"The two fell into a natural sync, their bodies molding together in a manner reminiscent of their conflict, months before. Only this time, the growls and yips were of an altogether different nature."
"She spread her legs apart and lifted her tail higher in a show of submissiveness. Rowan responded by taking hold of her shoulder firmly but gently with his teeth, holding her in tight place as he slapped his hips hard against her ass."
"He felt the swelling of his base grow and grow, his knot thickening with blood as he bottomed out within her. His knot bumped against her pussy lips, the engorged meat {i}squeezing{/i} tight between the narrow gap of her pussy. Rowan let out a growl, building to a roar. His knot slid into her folds with a loud {i}pop{/i}."
"{i}She is mine{/i}. That was the thought that repeated like a mantra in Rowan’s head as he hilted and came."
"He felt a rush of feminine fluids coat his crotch as the White Wolf orgasmed in tune to his own climax. There was a triumphant thrill of conquest as he ejaculated, a sense of biological accomplishment. His hot cum squirted deep into her pussy, filling her fertile womb with his impregnating seed."
"They had created a new life in that moment, Rowan felt it in the depths of his soul. The very wind in the trees changed their direction to tell him so."

menu:
    "I love her.":
        $ released_fix_rollback()
        $ heartsongLove = True
        "Despite his initial release, his knot did not go down. Whether she had intended it or not, the White Wolf had inflamed Rowan to his very core. They were now irrevocably tied together: his cock letting loose further spurts inside her womanhood as her pussy gently massaged more cum from his balls."
        "Still tied at the groin, the two collapsed together against the earth. Rowan was more exhausted now than he’d been after their first, contentious encounter. The White Wolf huddled into his arms, sharing her warmth with him in the heady afterglow."
        "Again, the yellow eyes. They were the strangest thing about her. More than her strength, or even her beauty, her contemplative gaze was what fascinated Rowan the most. She stared at him with something approaching contentment, and perhaps even a little bit of possessive pride."
        "{i}I am hers{/i}. He realized at last, his heart pumping faster. "

    "I own her.":
        $ released_fix_rollback()
        $ heartsongLove = False
        "Rowan roared and came, reveling in this final, total conquest of his onetime competitor. He had marked her womb as his territory: a claim staked upon her very inheritance." 
        "None save Rowan could mate with her now, and she was at his beck and call. He felt his knot swell still further within the whimpering woman at this supremely masculine thought."
        "As his balls pulsed and his knot swelled Rowan imagined his virile seed working its way into her, filling her with his cubs. The White Wolf was his, now and forever."
        "He laid atop her, pinning her to the ground for hours on end until his knot popped free from her dribbling pussy. She glanced up at him, letting out a submissive gasp as her yellow eyes fluttered and her ears pulled back against her head."
        "{i}She is mine{/i}. He thought again, growling in her ear as he breathed in the intoxicating scent of her hair."

scene bg3 with fade

"The seasons changed again. New life sprang into being as the cold of winter gave way to the bliss of spring. The White Wolf’s belly swelled, her breasts grew heavy with milk, and for a time Rowan hunted alone through the woods to feed the both of them."
"She soon gave birth to a trio of daughters: all white haired, with hazel eyes the color of their father’s. Rowan was overjoyed."
"Weeks passed; months; years. Seasons came and seasons went. Rowan’s pack grew and grew, his cubs growing and multiplying as he and his White Wolf hunted and mated and lived their lives as all Wolf-kin should: free and happy beneath the sheltering boughs of the mother-forest."
"Rowan looked on with pride as his sons and daughters matured and split off from the pack, embarking on the same journey of discovery that he and his love had once taken together, so very long ago." 
"More time passed, and the mighty patriarch grew old and grey, his claws dulling and his speed slowing. His old strength failed him, and for the first time since he was a pup, he found himself unable to keep up with the pack."
"Yet beyond all natural logic, the White Wolf still followed him. Even when he grew too weak to lead, and handed down leadership to his eldest remaining son."
"Then, one day, he could hunt no more. On an old family trail, the very same trail where he once had tried to pursue a fleeing Buck, Rowan collapsed to the ground, his breath going faint and his eyes fading."
"He looked up from his dazed stupor, and there was the White Wolf, bent over him, loyal as always. There was a soft expression in her yellow eyes. She stroked his face, her claws running through his hair and scratching behind his ear, just like he loved it."

wwolf "Rowan…"

"Rowan’s heart caught in his throat; she had never once said his name. Names were a foreign idea, an unnecessary categorization of someone who meant more to you than words."
"The White Wolf smiled at him, leaning in to kiss him gently on the lips one last time before whispering in his ear."

wwolf "Wake up."

scene bg9 with fade
show rowan necklace shock at midleft with dissolve

ro "{i}Guh!{/i}"
ro "W-what?! Where the hell am I? Where is-"

show rowan necklace concerned at midleft with dissolve

ro "..."
ro "By the Goddess."

"Rowan put his head in his hands, shaking it back and forth as he tried to clear the fog of the dream. He had to remind himself where he was - {i}who{/i} he was. It had all been so real: a lifetime lived in the space of a few hours."

show rowan necklace neutral at midleft with dissolve

ro "Heartsong."

"Why was she doing this? What did she want from him? It had all been so…" 
"Sudden." 
"Rowan got out of bed, feeling as weary as if he hadn’t slept at all."

return

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

label rowan_and_the_escaped_slave:

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

"There was a knock at Rowan’s door."
"He looked up from his desk, which was covered in piles of assorted maps he had been using to plan out the latest troop movements. It was later in the afternoon - he wasn’t expecting a visitor." 
"Perhaps one of the Twins had come to jaw at him about some new issue with the castle staff… or subject him to another odious humiliation. He set his quill aside and folded his hands together."

ro "Come in."

"But the emaciated man who stepped through the doorway was nothing like Rowan had imagined: gaunt, thin faced and hollow-eyed; he shuffled into the room with a hesitant, almost terror-stricken slowness."

quest "Rowan? Savior of Karst?"

ro "Who are you?"

"Rowan felt his hand moving to the hilt of his blade beneath the table."

quest "By the Goddess, it {i}is{/i} you! I-I’d heard rumors, but-"

"Rowan stood to his feet, putting his other hand on his scabbard, readying to draw steel. Something about the man’s demeanor told him he wasn’t supposed to be here."

show rowan necklace angry at midleft with dissolve

ro "Tell me who you are, right now."

"The knobby-kneed fellow was dressed in rags, his body was thin - far, far too thin for his frame. His feet were bare, his skin pale as if sunlight were a foreign concept to him."

quest "Forgive me, Lord! I meant no offense!"
quest "I am Boras, of Bowerstead."

show rowan necklace neutral at midleft with dissolve

ro "...Bowerstead? That village is only a few miles from Arthdale."

boras "It is indeed, my Lord."
boras "We were neighbors once… of a sort, I suppose."

"The nature of who Boras was and what he was doing in Rowan’s chambers became more and more obvious to him. He released his grip on his hilt and circled the table. The slave shrank back from him."

ro "How did you get here, Boras?"

boras "I… I am sorry my Lord, I could not take it anymore."

ro "Could not take what?"

boras "The work, the - the beatings. Okrem denies us food, chains us to the wall like {i}animals{/i}, he-"

ro "Who is Okrem?"

boras "The Orcish overseer. I work in the Mines, my Lord."

ro "I am no Lord, Boras."

if society_type == "feudalism":
    ro "At least not at present."

boras "Of- of course, sir."
boras "I am not asking for my freedom. I don’t expect I shall ever leave this place."
boras "-But I {i}had{/i} to come to you. You are the Hero of Karst: the only person in this Castle who treats the slaves fairly."

show rowan necklace concerned at midleft with dissolve

ro "..."

"‘Treats the slaves fairly?’ In truth he didn’t often interact with the captives… was that the rumor that was circulating?"

show rowan necklace neutral at midleft with dissolve

ro "What do you want from me, Boras?"

"Despite his rickety frame, the slave got down on his knees in front of Rowan. He clasped his hands together as if in prayer."

boras "{i}Anything{/i}, my Lord. Whatever kindness I can beg of you."
boras "I don’t want special treatment, but…"
boras "Ogrem is {i}cruel{/i}, my Lord, and the slaves he has a particular dislike for suffer the most. I left work detail to see you, if he finds out I am here..."

"The blubbering man broke down into tears, his eyes only managing to produce a few, dehydrated drops as he shivered and shook in place. Rowan felt a stirring in his chest, a sense of injustice welling like a rising tide of anger."
"He couldn’t risk everything for this man - he was already risking everything for the chance that Alexia might still be saved. But maybe..."

menu:
    "Pull some strings.":
        $ released_fix_rollback()
        "Rowan frowned. There was little he could do to help the poor man out of his predicament. The man was a slave, that was the simple fact of the situation. Rowan could not afford to spend his dearly-earned influence attempting to save every person who came to him expecting him to right the wrongs of his masters."
        "Slavery was a fact of the Twins’ regime: their very power rested on the need for a workforce that provided them effort for a minimum of cost… but that didn’t mean he couldn’t at least help the poor man out. Who knows what Ogrem would do if he just sent him back."
        "Rowan put a hand on the crying slave’s shoulder."
        ro "Let me see what I can do, Boras. I can’t give you your freedom, but I can at least spare you from a brute like Ogrem."
        "Boras lifted his head, his eyes filling with hope."
        show rowan necklace happy at midleft with dissolve
        ro "Let me make a few inquiries. I’m pretty sure Tywin could use some extra hands in the Kitchens. The work is tedious, but-"
        boras "Thank you, my Lord! I won’t let you down."
        show rowan necklace neutral at midleft with dissolve
        ro "You don’t need to worry on that account, Boras. You have already shown immense courage coming here."
        ro "-And it’s just Rowan."
        boras "I cannot thank you enough Rowan, you have saved my life."
        ro "My pleasure Boras."
        "Rowan went back to work with a small smile on his face. That was a rare thing. He didn’t get to smile often."
        $ change_base_stat('c', -3)
        return
        
        
    "Tell him there is nothing you can do.":
        $ released_fix_rollback()
        "Rowan’s heart sank. There was no way to help the poor slave out of his predicament. His relationship with the Twins was tenuous enough; he could not afford to spend his dearly-earned influence helping every worker that came to him begging for mercy."
        "Slavery was a fact of the Twins’ regime: their very power rested on the need for a workforce that provided them effort for a minimum of cost. To play favorites and move mountains for the sake of metaphorical molehills was a waste of resources, and a dangerous misuse of what power he had."
        "Rowan shook his head, reaching down to put a hand on the crying slave’s shoulder."
        show rowan necklace concerned at midleft with dissolve
        ro "I am sorry, Boras. You were assigned to the Mines. That is where you’re supposed to work. And until Ogrem gets reassigned-"
        "Boras’ head lowered, his pitiful tears dripping down onto the stone floor below."
        show rowan necklace neutral at midleft with dissolve
        ro "I will send you back with a personally-signed letter, informing Ogrem that I called you to my chambers to talk to you myself. That should absolve you of any and all guilt in the matter."
        boras "But, what should I tell him we talked about?"
        ro "Tell him that I asked you pointedly about the conditions in the Mines. And how Ogrem was faring as an overseer."
        ro "If you tell him you gave me a glowing report, he’ll likely be pleased, and not in the mood to punish you."
        "Boras stood to his feet, sniffling as he rubbed at his teary eyes."
        boras "Th-Thank you my Lord."
        ro "Please, sit for a moment. You have earned that at the very least. Let me compose the letter."
        boras "You’re a good man, Rowan."
        "Rowan’s mouth twisted with disgust. Was this what a “good man” did? The bare minimum? The longer he served the Twins the more he felt removed from the man he once was. He was sacrificing his morals for the sake of the woman he loved."
        "...He had to believe it was worth it."
        $ change_base_stat('g', 3)
        return

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

label mutual_elven_fear:

scene bg6 with fade
#show draith / liurial afraid
show draith neutral at midright with dissolve
show liurial neutral at edgeright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "Liurial, take a note that-"

show rowan necklace shock at midleft with dissolve

"He stopped at the sight of a stare-off between his secretary and the castle beastmaster.  Both of them were frozen to the spot, staring one another down.  A moment passed, but before Rowan could speak again Liurial let out a sudden shriek!"

liur "Eeey!"

"The noise drove Draith to cover his ears and yell her down."

dra "Stop it!  NO!"

ro "What's going on here?!"

liur "Th-this creature stepped in and-"

dra "Don't punish me!  Don't-"

show rowan necklace neutral at midleft with dissolve

ro "Hey!  There's no need for yelling."

"He stepped between the two with his arms outstretched.  Liurial didn't seem to hear Rowan, cowering behind him now that he'd separated the two of them. All the while continuing to yell out vague accusations."

liur "D-d-dark elf! Monster! Murderer!"

ro "Liurial, pull yourself together girl."

"Draith wasn't doing much better, as he'd also taken to cowering behind Rowan, covering his face with his hands and muttering to himself."

dra "Don't hurt me...  Please...  I'll be good..."

ro "Draith, seriously?  Jezera is far scarier and you don't break down like this."

"At least Liurial had quieted down."

ro "Glad to have you... back?"

show liurial sad at edgeright with dissolve

"The elven woman wasn't responding to Rowan at all now.  She was staring off at nothing with tears in her eyes.  There wasn't even a whimper escaping her lips."
"Draith was still muttering to himself with an occasional outburst."

#draith angry

dra "It wasn't my fault... please give me another chance.  Don't touch me!"

#draith sad
show rowan necklace concerned at midleft with dissolve

"This was ridiculous.  Two adults cowering behind the same person, driven to abject terror by one another.  It would be comical, if Rowan wasn't the one caught in between them."

show rowan necklace neutral at midleft with dissolve

ro "Okay, that's enough!"

"He took each of them by the shoulder with a firm, confident grip.  That got their attention."

show liurial neutral at edgeright with dissolve
#draith neutral

ro "Liurial.  Liurial, look at me."

"Finally her gaze focused on his and at last she seemed to relax.  One of her soft hands went over his and she seemed to take comfort in his familiar touch.  That was good enough for Rowan."

ro "Draith, no one is going to hurt you.  You're safe."

"The beastmaster nodded, evidently getting his wits about him once more.  He took a steady breath, smiled nervously, then nodded again.  At least some confidence had been instilled in the dark elf."

ro "Liurial, this is Draith.  He is the castle beastmaster and serves the twins.  He isn't your enemy, he isn't going to hurt you."

"Rowan waited for her to blink back her tears and respond."

liur "Okay, I trust you."

"Then he turned his attention back to Draith."

ro "Draith, this is Liurial, she's my secretary now.  She answers to me.  I won't let her order you around or try to punish you."

dra "If you say so."

"Satisfied that the situation was resolved, at least for now, Rowan released the two elves.  They glanced at one another somewhat nervously, but showed no further signs of fear."

ro "Okay.  Right.  Draith, may I ask what brings you to my office?"

dra "Uh, oh!  I thought that since you were here that maybe I'd deliver my report in person?"

"Draith fidgeted with a parchment before looking sidelong at Liurial.  He started taking an instinctive step backwards but managed to put his foot back down.  That was progress, but Rowan wasn't satisfied with the answer."

ro "Is there anything in particular about this report you needed to bring up?"

#draith aroused
dra "No... I thought that maybe we could enjoy one another's company?"

ro "Another time.  Thank you for your report Draith."

"He motioned to Liurial."

ro "Give your reports to Liurial.  Like I said, she's my secretary and handles most of my paperwork."

#draith neutral

"Neither of them moved.  Rowan groaned inwardly, the two were acting like children. He motioned once more and Draith reluctantly placed his report in Liurial's hands."

if rowanGaySex > 0:
    #draith angry
    "As the dark elf stepped back, something flashed in his eyes.  Was that a spark of anger?  No, jealousy?"
    ro "(Just wonderful.)"
    
#draith concerned

dra "It was, uh, good to meet you.  I hope you don't mind if I go back to sending my beast handlers up instead of in person, r-right?"

liur "Yes that will be fine, preferable even."

ro "Good, then you're dismissed Draith."

hide draith with moveoutright
#liurial concerned
show rowan necklace angry at midleft with dissolve

"A small barely perceptible smile graced Rowan's lips as the dark elf managed to keep his cool and calmly walk to the door.  However, it faded the moment Draith got outside and broke into a run.  He didn't even bother to close the door before he flew down the hallway."
"This was unusual even for him, was it because Liurial was an elf?  Rowan let out an exhausted sigh.  He would check on him later, for now he turned to his assistant."

ro "Liurial, how can that man scare you so much?  You saw him!  He was just afraid of you as you were of him."

show liurial sad at edgeright with dissolve

ro "Rowan... look... sorry.  I'm sorry."

"The elven woman looked like she would break back into tears."

show rowan necklace neutral at midleft with dissolve

ro "It's fine, please just tell me why?"

show liurial neutral at edgeright with dissolve

"She took a deep breath to steady herself and finally seemed to get her wits back around her."

liur "It’s hard to forget the fear born from years of stride. Our races have been in conflict since the demon wars began.  Dread of the dark elves. Of being killed or captured is a constant aspect of our lives."
liur "They used raid us in the night without warning. I remember hiding in the shelters and hearing the fighting. I’ve heard of whole villages just...vanishing. Peace is a joke in the deep woods."
liur "He could be the most harmless Dark Elf in the world. It is not a fear easily unlearned."

show liurial happy at edgeright with dissolve

"She shook herself, then put on a brave face."

if liurialSex == True:
    liur "As long as you don't want him to join us for...you know... I'll try my best to be civil."
    ro "I don't think you'll need to worry about Draith. He has made it clear he doesn't want women anywhere near him."
    liur "Thank you."
    
else:
    liur "For your sake, I'll try."
    ro "Thank you."

return
