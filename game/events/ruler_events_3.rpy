init python:

    # X'zaratl's advances
    # Can trigger three weeks after Dark Sanctum is built, can happen 1 week earlier and is high priority if Rowan was friendly with X'zaratl.
    event('xzaratl_s_advances', triggers="week_end", conditions=("castle.buildings['sanctum'].lvl >= 1", 'week >=4'), group='ruler_event', run_count=1,
        priority=pr_ruler, weekend_auto=False, weekend_room="bg23")
    # A Trip to the Library
    # Requires post week 8, priority after week 11.
    event('trip_to_library', triggers="week_end", conditions=('week >= 8',), group='ruler_event', run_count=1, priority='pr_ruler_high if week > 11 else pr_ruler')
    # Goblin family dinner
    #Requires that Rowan have talked to Cla-Min about goblins.
    event('goblin_family_dinner', triggers="week_end", conditions=('week >= 4',), group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg19")
    # Problem squad
    # Req at least 10 orc soldiers and morale less than 70%.
    event('problem_squad', triggers="week_end", conditions=('week >= 4', "castle.morale < 70", "castle.buildings['barracks'].troops >= 10"), group='ruler_event', run_count=1, priority=pr_ruler)
    # Poisoned
    event('poisoned', triggers="week_end", conditions=('week >= 4',), group='ruler_event', run_count=1, priority=pr_ruler)
    # Salvaged supplies
    # Requires pre-end of first year.
    event('salvaged_supplies', triggers="week_end", conditions=('44 <= week <= 48',), group='ruler_event', run_count=1, priority=pr_ruler)


label xzaratl_s_advances:
# X'zaratl's advances
# Can trigger three weeks after Dark Sanctum is built, can happen 1 week earlier and is high priority if Rowan was friendly with X'zaratl.

$ XzaratlSeenRowanAlexiaRoom = False

scene bg9 with fade
show rowan necklace angry at midleft with dissolve
show alexia 2 necklace neutral at edgeright with dissolve

"Rowan kept tapping his foot, trying to gather his thoughts after his recent encounter with the new cubi mistress." 
"Not wanting to interrupt him, Alexia stared out of the window, watching the newly settled demons explore the castle’s outer walls." 
"… She squinted her eyes, unsure if they were playing tricks on her."

al "Rowan, one of the succubi is jumping up and down, waving at me. "

show alexia 2 necklace shocked at edgeright with dissolve

al "And I think she’s shouting my name?"

show alexia 2 necklace neutral at edgeright with dissolve

ro "Four arms? Asymmetrical horns? "

al "I think so."

ro "That would be X’zaratl. It’s her coven that joined us recently."

al "I believe I’ve seen her before, watching me from afar. Never introduced herself, though."

show rowan necklace concerned at midleft with dissolve
show alexia 2 necklace shocked at edgeright with dissolve

al "… She’s {b}still{/b} waving at me."

show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace happy at edgeright with dissolve

al "She’s quite lively, isn’t she?"

ro "That’s one way to put it."

show alexia 2 necklace neutral at edgeright with dissolve

al "… And now she’s walking to the front gates. I think she’s planning to visit us." 

show alexia 2 necklace neutral at midright with moveinright

"Rowan sighed, and pinched the bridge of his nose. Alexia walked up to him, and placed a hand on his shoulder."

show alexia 2 necklace concerned at midright with dissolve

al "Should I be worried Rowan? Are we in danger?"

if RowanXzaratlDominantStart == True:
    ro "I don’t know. Maybe? I tried to set some boundaries when we first met. She broke through them like a battering ram." 
    al "Not the type to take “no” for an answer?"
    ro "Exactly. She acts friendly, but… I don’t know."
    
else:
    ro "I don’t think so? She seemed… Amicable, when I first met her. At the same time, she doesn’t strike me like the type that takes “no” for an answer."

show alexia 2 necklace neutral at midright with dissolve

al "So how do we handle her?"

ro "That’s what I’m trying to figure out."

"He never encountered a demon like that. Never one that seemed so…. Honest."

show rowan necklace angry at midleft with dissolve

"If it was a trick, it was the best gods damn act he had ever witnessed. And it {i}had{/i} to be a trick. It would be unreal for it {i}not{/i} to be a trick. "

show rowan necklace concerned at midleft with dissolve

"Then why didn’t it feel like one?"

show rowan necklace neutral at midleft with dissolve

ro "… I don’t want to antagonize her. But I don’t know what her motives are, and what she’s truly capable of. I won’t pretend I’m not at a disadvantage here - avoiding her would be the safest choice."

show alexia 2 necklace happy at midright with dissolve

al "You never were one to pick the “safest” route."

show rowan necklace happy at midleft with dissolve

"He grabbed her hand, and smiled sadly. “Calculated risk” - that’s how he liked to think of his strategies. But not every risk was worth taking."

show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at midright with dissolve

ro "She’s interested in you too. I don’t want to put you in danger."
ro "… More so than you already are. "

show alexia 2 necklace happy at midright with dissolve

"A soft knock interrupted them. Alexia glanced at the door, then smiled at him."

al "Occupational hazard. Wife to a hero of the six realms, and all."

show alexia 2 necklace neutral at midright with dissolve

al "Whatever you decide, I’ll do my best to support you."

if alexiaJezObedient or alexiaAndrasObedient or all_actors["alexia"].relation < 30:
    show rowan necklace concerned at midleft with dissolve
    "… She didn’t sound honest. Not in full. Like she was reciting the words from memory, hoping that giving them form will somehow make them true." 
    "He pretended not to notice. For the tenth time today, he wondered if the bond X’zaratl spoke of still existed."  
    show rowan necklace neutral at midleft with dissolve

show alexia 2 necklace neutral at midright with dissolve

ro "Thank you, Alexia." 

show rowan necklace neutral at edgeleft with moveoutleft

"He stood up, and headed for the door-"

menu:
    "Invite X’zaratl in. Play her game - whatever it is.":
        $ released_fix_rollback() 
        ro "Put on your best smile, then. And keep in mind X’zaratl gets a little... Intense." 
        show rowan necklace happy at edgeleft with dissolve
        show alexia 2 necklace shocked at midright with dissolve
        ro "Also, she might have a dick."
        show rowan necklace happy at midleft with moveinleft
        show xzaratl happy at edgeleft with moveinleft
        show alexia 2 necklace happy at midright with dissolve
        ro "X’zaratl! What a pleasant surprise. Have you met my wife, Alexia?"
        "Met with Rowan’s welcoming smile, the demoness took several moments to register what just happened. She stood in the middle of the wide open door, frozen in place."
        "Alexia waved at her."
        show rowan necklace happy at edgeright with moveoutright
        show xzaratl happy at midleft with moveinleft
        xz "Only a thousand times in my dreams."
        show alexia 2 necklace shocked at midright with dissolve
        xz "Oh Alexia, how wonderful to finally meet you! You are just as I imagined!"
        show alexia 2 necklace aroused at midright with dissolve
        xz "Fiery red locks, so full of spirit! Green eyes, wise and compassionate! And a body-"
        xz "Ah, I shouldn’t say. I bet Rowan praises it often enough."
        if all_actors["alexia"].corruption > 30:
            show alexia 2 necklace happy at midright with dissolve
            al "He could do it more."
        al "That’s- ah, t-thank you."
        "Already, X’zaratl was holding her hands, grinning from ear to ear. Alexia threw Rowan a short glance. “Intense” was an understatement."
        show alexia 2 necklace happy at midright with dissolve
        al "I’m also glad to have finally met you. It isn’t often that I see a friendly face here."
        show xzaratl neutral at midleft with dissolve
        xz "I know! Oh, Fair Alexia- I know.."
        show alexia 2 necklace shocked at midright with dissolve
        show rowan necklace shock at edgeright with dissolve
        xz "Stuck in a cage, pawn in a game played by cruel gods and their heartless servants, helplessly watching as the wheel of history threatens to crush you in its cogs-"
        show xzaratl happy at midleft with dissolve
        show alexia 2 necklace neutral at midright with dissolve
        show rowan necklace concerned at edgeright with dissolve
        xz "And yet you remain strong. Like the swordmaiden of Astolde - Unbent and unbroken!"
        #xzaratl eye flash gold
        show alexia 2 necklace happy at midright with dissolve
        xz "You are as resolute as you are lovely, Alexia, and I love you for it."
        "Rowan felt a sting in his heart, and he saw Alexia blink away the tears, struggling to keep up her smile. Everything X’zaratl said, always sounded like it came straight from the heart."
        "It {b}had{/b} to be a trick. Why didn’t it feel like one?" 
        show alexia 2 necklace neutral at midright with dissolve
        show rowan necklace neutral at edgeright with dissolve
        al "That’s very kind of you to say."
        xz "It’s nothing, fair Alexia. I know the walls of Castle Bloodmeen can be cold and suffocating. This place has not seen much love - and very rarely one as strong as yours."
        xz "Yet you mustn't despair, fair Alexia - and you too, gallant Rowan. You must remember what you are fighting for."
        jump letHerIn
        
    "Keep X’zaratl at a distance. You can’t trust her. ":
        $ released_fix_rollback() 
        ro "Stay back, and put on your best poker face. X’zaratl gets a little intense."
        show alexia 2 necklace shocked at midright with dissolve
        ro "Also, she might have a dick."
        scene bg14 with fade
        show rowan necklace neutral at edgeright with moveinright
        show xzaratl happy at midleft with dissolve
        ro "X’zaratl. Good day to you. What can I do for you?"
        "He opened the door for her, but barred her entry, standing at the entrance. That didn’t seem to bother the demoness at all, as she bestowed him with the most radiant of smiles."
        show xzaratl happy at edgeleft with moveoutleft
        show rowan necklace neutral at midright with moveinright
        "Then, discreetly, leaned to the side, trying to peek inside. Rowan took a step to his left, blocking her view."
        show rowan necklace neutral at edgeright with moveoutright
        show xzaratl happy at midleft with moveinleft
        xz "Gallant Rowan! It’s been too long."
        xz "I apologize for the sudden intrusion, but I thought that maybe, just maybe- you could introduce me to your wife?"
        "He drummed on the door frame. Already, she was stalking her. He could deny her, but there was no guarantee she would leave her alone when he was away." 
        "Better now, when he was present. With a sigh, he moved aside, and urged Alexia to come forward." 
        show rowan necklace neutral at midright with moveinright
        show alexia 2 necklace neutral at edgeright with moveinright
        xz "X’zaratl, my wife, Alexia. Alexia, X’zaratl, mistress of the castle cubi."
        al "Good afternoon."
        "As he asked, Alexia kept herself composed - cold, even."
        show xzaratl aroused at midleft with dissolve
        "… And again, that didn’t seem to bother X’zaratl at all. The demoness’ face flushed red, and she visibly struggled not to rush in and embrace her. Her eyes sparkled, as she admired the woman before her."
        xz "Oh Alexia. You are just as I imagined!"
        show xzaratl happy at midleft with dissolve
        show alexia 2 necklace shocked at edgeright with dissolve
        xz "Fiery red locks, so full of spirit! Green eyes, wise and compassionate! And a body-"
        xz "Ah, I shouldn’t say. I bet Rowan praises it often enough."
        show alexia 2 necklace neutral at edgeright with dissolve
        al "That’s very nice, but I hardly compare with some of the succubi from your coven."
        xz "To the contrary. Fair Alexia, you outclass each and every single one of them."
        show xzaratl neutral at midleft with dissolve
        xz "My sisters do not capture hearts of mortal heroes as you do. None would ever have the strength to endure the same hardships as you do almost every single day."
        show alexia 2 necklace concerned at edgeright with dissolve
        xz "Stuck in a cage, pawn in a game played by cruel gods and their heartless servants, helplessly watching as the wheel of history threatens to crush you in its cogs-"
        show xzaratl happy at midleft with dissolve
        show alexia 2 necklace shocked at edgeright with dissolve
        show rowan necklace angry at midright with dissolve
        xz "And yet you remain strong! And yet here you stand, proud and regal! Like the swordmaiden of Astolde - Unbent and unbroken!"
        #xz eyes flash gold
        show alexia 2 necklace concerned at edgeright with dissolve
        xz "You are as resolute as you are lovely, Alexia, and I love you for it."
        "Alexia felt a sting in her heart, and had to blink away the tears. So that’s what Rowan meant by “Intense”. Everything X’zaratl just said, sounded like it came straight from the heart." 
        "Words she didn’t know she needed to hear. How could this be a trick?"  
        show alexia 2 necklace happy at edgeright with dissolve
        show rowan necklace concerned at midright with dissolve
        "She felt Rowan’s hand around her shoulder. She blinked again, and smiled at him."
        al "I’m fine. I’m fine."
        show rowan necklace angry at midright with dissolve
        ro "X’zaratl, please watch your words."
        al "I’m fine, really. That was… Nice. If somewhat unexpected."
        show rowan necklace neutral at midright with dissolve
        xz "Perhaps I spoke out of place - and for that, I apologize. I am still a stranger to you both."
        xz "But it doesn’t have to be that way. Gallant Rowan, fair Alexia - I know the walls of Castle Bloodmeen can be cold and suffocating. Sometimes it might seem that only despair dwells in them."
        show alexia 2 necklace neutral at edgeright with dissolve
        xz "That is not the case, and you are proof of it. Your love for each other is a  beacon of joy, and that shines brightly even here. To think this accursed place could house such a couple-"
        "The demoness bit her lips, and peered into their room again. When she spoke again, her tone was almost pleading."
        xz "Gallant Rowan, fair Alexia, would you- would you allow me to see your love nest? Just this once."
        ro "I assure you it doesn’t compare to the Dark Sanctum."
        xz " I can say no ill of the Master Builder’s skills."
        show xzaratl neutral at midleft with dissolve
        xz "But the Sanctum he made us is just rooms and walls, as any other in this castle. Cold stone, sculpted to perfection by a lonely hand. It’s no home. They have no warmth in them."
        #xz yellow eye flash
        xz "But you - you take your warmth with you, wherever you go. Even here, at the end of the world, I have no doubt you’ve managed to keep the hearth burning, creating a home in the most unlikely of places."
        xz "Just this once. Please?"
        "… Rowan tapped the door frame. He felt both of their eyes on him. Alexia didn’t say a word, but he felt she wouldn’t mind talking with X’zaratl some more."
        show rowan necklace shock at midright with dissolve
        "And he himself couldn’t think of a reason to deny the request. Which was odd - he could swear he had one before. But X’zaratl really seemed mostly harmless, so…"
        menu:
            "Invite X’zaratl in.":
                $ released_fix_rollback() 
                show rowan necklace concerned at midright with dissolve
                show alexia 2 necklace happy at edgeright with dissolve
                ro "Well… Fine."
                show rowan necklace neutral at midright with dissolve
                "X’zaratl’s eye sparkled again, and she giggled like a teenage girl."
                show xzaratl happy at midleft with dissolve
                xz "Oh, thank you Rowan! And I mean it. I really do."
                xz "I know you must be on your guard. But I mean both of you no harm. Not everything is a fight."
                xz "And when it is - you must remember what you are fighting for."
                jump letHerIn
                
            "Stick to the plan. There was no such thing as {i}mostly{/i} harmless. ":
                $ released_fix_rollback() 
                show rowan necklace neutral at midright with dissolve
                "His lips drew a thin line. Something nagged at him - he just couldn’t say what it was. It felt like a light tugging at the back of his head." 
                "He honed his instinct through years of warfare. He knew when to follow it." 
                show xzaratl concerned at midleft with dissolve
                ro "With all due respect… I would like to spend some time with my wife. Alone."
                show xzaratl happy at midleft with dissolve
                xz "Of course! I would never dream to impose. I just hope it’s not because of… Ah, this- "
                show rowan necklace happy at midright with dissolve
                "Her hand brushed against her crotch. Rowan smiled, and very actively didn’t look down."
                show rowan necklace neutral at midright with dissolve
                ro "I feel like that’s a conversation for a whole other day."
                xz "Of course, of course. If you’re busy, just let me reiterate…"
                #xz yellow eye flash
                xz "Alexia, what you share with Rowan… The bond of love between you, hardened through everything that happened, made stronger - I admire it. I think it’s special. Unique."
                xz "I will do what I can to see it grow. If any of you ever need my help, I will do my best to grant it."
                al "That’s very generous of you, X’zaratl. Thank you."
                xz "It’s nothing, really. Now… Do enjoy yourself!"
                hide xzaratl with moveoutleft
                hide alexia with moveoutright
                hide rowan with moveoutright
                scene bg9 with fade
                show rowan necklace neutral at midleft with dissolve
                show alexia 2 necklace neutral at midright with dissolve
                "Rowan locked the door, taking a moment to gather his wits. Something… He couldn’t say what, but something - something felt {i}off{/i}."
                al "That was…"
                ro "Yeah."
                jump xzaratlAdvancesEarlyEnding
                
label letHerIn:

$ XzaratlSeenRowanAlexiaRoom = True

scene bg9 with fade
show alexia 2 necklace neutral at edgeleft with dissolve
show xzaratl happy at midright with dissolve
show rowan necklace neutral at midleft with dissolve


"Caressing both of their cheeks, X’zaratl strolled to the center of the room. Her step light, she turned around, soaking the place in, like a kid in a toy shop." 

xz "And what is it we’re fighting for, in your eyes? "
                
"She turned to them again, eye sparkling, gracing them both with a wide smile. Somewhat, the room felt brighter with her in it. As if it wasn’t complete without her before."

xz "For each other. And for your happy ending, of course."
xz "All of your struggles - every fight, every parting, every humiliation - finally rewarded. Finally gone. So that you can enjoy yourself in full."

show alexia 2 necklace concerned at edgeleft with dissolve
show rowan necklace concerned at midleft with dissolve

ro "We had one already."
        
al "It didn’t stick."

xz "Because your journey was not yet over. "
        
#xz yellow eye flash
        
show alexia 2 aroused at edgeleft with dissolve
show rowan necklace aroused at midleft with dissolve

xz "Your love can still grow. There is still much for you to discover. You need only to open yourself to it."
xz "I will help you, if you let me."

show alexia 2 necklace shocked at edgeleft with dissolve
show rowan necklace shock at midleft with dissolve

al "X’zaratl, what are you-"

"They stared, dumbfounded, as the demoness started to undo her clothes -"

menu:
    "See where things go.":
        $ released_fix_rollback() 
        jump xzaratlSex1
        
    "Stop it right now.":
        $ released_fix_rollback()
        show alexia 2 concerned at edgeleft with dissolve
        show rowan necklace angry at midleft with dissolve
        ro "X’zaratl, that’s… Please, cover yourself."
        "The demoness froze, then did as requested, swiftly and without a word of protest. Rowan blinked - he was certain she {i}would{/i} protest."
        xz "Ah, I apologize! I tried to rush things. Being here, with you…."
        show xzaratl aroused at midright with dissolve
        show alexia 2 aroused at edgeleft with dissolve
        show rowan necklace neutral at midleft with dissolve
        xz "It got me in the mood."
        "They tried to ignore her very obvious erection. It was a titanic task Rowan could compare only to repealing the first assault on karst."
        show alexia 2 neutral at edgeright with moveoutright
        show rowan necklace neutral at midright with moveoutright
        show xzaratl happy at midleft with moveoutleft
        xz "I will not overstay my welcome. Thank you for letting me see this place. You’re both very generous."
        al "It was nothing, really."
        xz "Not to me. And, gallant Rowan -  what I said before still stands."
        #xz yellow eye flash
        xz "What the two of you share... The bond of love between you, hardened through everything that happened, made stronger - I admire it. I think it’s special. Unique."
        xz "I will do what I can to see it grow. If any of you ever need my help, I will do my best to grant it."
        ro "We’ll keep it in mind."
        xz "That’s all I ask for. Take care!"
        hide xzaratl with moveoutleft
        "They watched her go, suddenly finding themselves amidst an uncomfortable silence. Rowan furrowed his brow. That was…"
        show alexia 2 necklace happy at edgeright with dissolve
        show rowan necklace concerned at midright with dissolve
        al "A little anticlimactic, wouldn’t you say?"
        ro "I suppose."
        al "Not how I imagine my first duel with a demon would go."
        show rowan necklace neutral at midright with dissolve
        ro "I don’t think X’zaratl makes for a good example."
        al "That’s good, no?"
        "She smiled at him. Should they really be joking about this? If he hadn’t asked X’zaratl to leave, then…"
        jump xzaratlAdvancesEarlyEnding
        

label xzaratlSex1:

$ RowanAlexiaXzaratlThreesomeRowan = False
$ RowanAlexiaXzaratlThreesomeAlexia = False

scene cg35 with fade
show xzaratl happy behind cg35
pause 3

"Perhaps that was the moment where either of them should have said something. Some praise, or maybe a protest. But all thoughts left them at the sight of the succubus’ perfect body."

xz "I know we just met. I know you have reasons to distrust me. And I know this might be a bit sudden. But I-"

scene cg36 with fade
show xzaratl naked behind cg36
show rowan necklace aroused behind cg36
pause 3

"X’zaratl brushed her hand against her crotch, a soft moan escaping her lips. The thin material that hid her crotch slipped aside, revealing a rapidly hardening male cock, and underneath it, a glistening female slit."

xz "I want you. Both of you. And I want to make you happy. I {b}can{/b} make you happy. I can show you things you never dreamed of. I can give you an ending you never dreamed of, a future bright and full of happiness like no other."

"Rowan swallowed heavily. He looked to his wife, but she was too transfixed on X’zaratl’s cock to say a thing." 

ro "X’zaratl, I don’t think this the right time to talk of the future."

xz "It’s still far away. I know. But I can give you a taste of things to come. Show you what your love can become."
xz "You need only to let me."
xz "Alexia."

scene cg37 with fade
show xzaratl naked behind cg37
show rowan necklace naked behind cg37
pause 3

"She finally tore herself gaze away. X’zaratl simply smiled, and started to remove her corset. Rowan felt an odd sensation around him - like a breeze. He realized his own clothes were slowly being discarded, as if taken by invisible hands."

xz "You know how hard your husband fights for you. Do you not wish to reward him for his efforts? "

"She nodded dumbly. X’zaratl ran a finger across her shaft, playing with the swollen tip of it."

xz "A man can reach new heights of pleasure, if he… Ah, {i}opens{/i} himself. Literally. To experience what you feel, while he thrusts inside of you - will be a delight like no other." 

"Something brushed against his ass, and Rowan shuddered - only to find himself on the receiving end of X’zaratl’s attention again."

xz "Rowan. Every week, you must leave the castle. Do you not wish to reward your wife with twice the affection when you come back?"
xz "I would never dream to defile her most sacred spot. Her pussy is for you, and you alone."
xz "But let me take her back. Let me take her bottom. Let her experience what is to be loved twice as intensely."

"He felt hot - and Alexia looked downright dazed. Already stripped to her panties, she was panting with desire as the Succubus invisible hands played with her body."

xz "You both deserve to be happy. You both deserve to find pleasure in each other's arms. And you will. Today, and next week, and the week after. I will always be there for you."
xz "But right now, you need only to ask one another - with everything that happened recently..."
xz "Who deserves to be rewarded for their struggles more?"

menu:
    "Rowan should be rewarded. [Rowan in the middle]":
        $ released_fix_rollback()
        jump xzaratlSex1Rowan
        
    "Alexia should be rewarded. [Alexia in the middle]":
        $ released_fix_rollback()
        jump xzaratlSex1Alexia


label xzaratlSex1Rowan:

$ RowanXzaratlInfluence += 3
$ AlexiaXzaratlInfluence +=2 
$ RowanAlexiaXzaratlThreesome = True
$ RowanAlexiaXzaratlThreesomeRowan = True
$ change_relation('alexia', 5)
$ change_base_stat('g', -3)
$ change_base_stat('c', 3)
$ change_corruption_actor('alexia', +5)
$ RowanXZaratlAnalTraining += 1

"He felt the gentle touch of Alexia’s fingers, as she grabbed him by the hand. Blushing furiously, she looked up to him, slightly abashed."

show alexia 2 necklace aroused behind cg37

al "You do… Do quite a lot. Maybe... You’d like to know how it feels? "

"He gasped as invisible fingers prodded his entrance, carrying with themselves promises of things to come. Both women looked at him expectedly - and he found himself nodding without thinking."

xz "A man after my own heart. Come."

#cgblurred
scene cg64 with fade
show xzaratl naked behind cg64
pause 3

"She crooked a finger at him - and a sudden force lifted him into the air, and floated to the sorceress as she laid down onto their bed."

xz "Now… Please relax, Rowan."

"She drew him closer, placing one hand on his back, then slid a finger up his ass, wet with magical lubrication. He drew a sharp breath, as three more hands all wrapped themselves around his body and pulled him down."

xz "And know bliss."

#show unblurred

"In one smooth motion, the demoness impaled Rowan with her cock. He shuddered as a violent wave of pleasure went through his body."
"And not just physical. Her cock radiated pleasing warmth that seeped into him - the slight fog of lust that covered his thoughts suddenly gave way to burning desire, and his cock hardened in an instant." 
"Meanwhile, Alexia admired it from afar, watching it sway in the air as X’zaratl shook her hips from side to side. Seeing her expression, the demoness giggled and bottomed out, causing a rather unmanly gasp escape Rowan’s lips." 

xz "It feels good, doesn’t it? And it will feel even better soon. "

"She hugged him close, pressing her breasts into his back. She kissed his shoulder, then his neck - but when he turned to look into her sparkling eye, she turned his head away - back at his entranced wife."

xz "Come, fair Alexia. Reward your husband for his struggles."

"Again, the cubi mistress crooked a finger, this time at her - and it was like a leash being tugged. Alexia stumbled forward, and heaving from desire, climbed her husband. Then- "

scene cg65 with fade
show xzaratl naked behind cg65
pause 3

"Another magical tug, and she felt her body turn around. She rested her back against Rowan’s chest, and looked into his eyes." 
"No words were exchanged - without thinking they found themselves locked in a passionate kiss, their whole world reduced to each other and the demonic mistress guiding them." 
"X’zaratl ran her hand through their hair, letting them enjoy the moment. Then, pushed her hips - causing the tip of Rowan’s cock to prod Alexia’s entrance. They both shuddered, knowing what was about to come- "
"She thrust her cock violently, causing both to jump up as Rowan’s cock drove into his wife's pussy. The demoness showed them not rest, quickly picking up the pace, making them bounce off her cock with seemingly no difficulty." 
"Alexia didn’t seem to mind. She sought his lips hungrily, surrendering to X’zaratl’s tempo."
"And Rowan discovered he didn’t care too, thrusting into Alexia in sync with X’zaratl’s movements. It felt good - the cock in his ass felt good, and Alexia’s warm, tight pussy made the whole experience mind-blowing." 
"He was only partially aware of X’zaratl whispering into both of their ears, telling them how amazing they were, how much she loved them, and how wonderful it was to be with them."

xz "And your ass is divine Rowan. Alexia must try it too. "

"His wife giggled, drunk with desire, but the innocent laughter soon turned to moans of ecstasy. She was coming - both from his cock, and from X’zaratl’s hands, who never ceased to roam their bodies, pleasing and arousing both of her lovers equally." 
"And he felt it too - felt it in every kiss, every sensuous touch, and every brutal thrust. The otherworldly, sexual skills of succubus. She wanted them to come at the same time - and he could do nothing but give himself to her completely."

show cg65 with sshake
show cg65 with sshake
show cg66 with flash
pause 2
show rowan necklace naked aroused behind cg66
show xzaratl naked behind cg66
show alexia necklace naked aroused behind cg66

ro "Ouhaa!"

"He felt a rush of hotness suddenly fill him almost to the brink, and with a loud cry of pleasure his own orgasm crashed over him. Rope after rope of his cum sprayed into his wife's passage, which in turn caused her to clamp down on him, screaming in delight."  
"It didn’t stop X’zaratl from thrusting, her face twisted in pleasure as well, as she kept pushing her hips, milking him with her cock, making his orgasm drag into infinity." 
"It was only when he finally felt all strength leave him, and he collapsed atop of her, exhausted, that she stopped. His wife soon followed suit, her arms no longer holding any strength to support her." 
"And as they laid there, panting, basking in the afterglow, they again felt X’zaratl’s gentle, guiding hand."

xz "Alexia, look at him."

"She turned her head to him. He smiled weakly, feeling his cock grow soft in her."

xz "No woman alive holds a candle to you. I cannot imagine a woman who could make her husband as happy as you do. You truly are his most precious treasure."

al "Ha… Don’t talk like that, it’s a little… It’s a little embarrassing."

ro "No more than, ah… Taking it in the back, dear."

scene black with fade

"He kissed her affectionately, and they stayed like that until darkness finally took them."

jump xzaratlSharedSexEnding

label xzaratlSex1Alexia:

$ RowanXzaratlInfluence += 2
$ AlexiaXzaratlInfluence += 3 
$ RowanAlexiaXzaratlThreesome = True
$ RowanAlexiaXzaratlThreesomeAlexia = True
$ change_relation('alexia', 5)
$ change_base_stat('c', 3)
$ change_corruption_actor('alexia', +5)

"Alexia felt Rowan ran his fingers through her hair, his face marred with concern - even as he struggled not to look at Alexia’s now bared breasts."

ro "… Do I leave you wanting, Alexia? When I come back… Is it not enough?"

show alexia necklace naked behind cg37

if alexiaJezObedient or alexiaAndrasObedient or all_actors["alexia"].relation < 30:
    al "… Sometimes."
    al "Sometimes… I feel like I want… More."

elif avatar.corruption < 31 and all_actors["alexia"].corruption > 30:
    al "… Sometimes."
    al "Sometimes… I feel like I want… More."
    
else:
    if rowan_shares_room_with_helayna == True:
        al "… You know the answer, my husband."
        "She didn’t say her name. She didn’t mention the woman who now stayed in this room, who Rowan had to send away just to spend some time with his wife again."
        "Twice the affection. For all the times when his own was divided."
    else:
        al "Never, my love."
        
ro "Then… Do you want to try it? "

"Her eyes went to Rowan’s crotch, his pants doing nothing to hide a hardness that threatened to rip them open. Then she turned her gaze to X’zaratl cock, which swayed enticingly before them."

al "… I do."

"He let his hands wander down, to her back, then further. He groped her bottom, wondering if he should feel jealous for having to share it with anyone." 
"Somehow, he didn’t. Almost without thinking, he nodded at the demoness, giving his consent."  

xz "You are a man like no other, Rowan Blackwell. Your wife is blessed to have you."

"She crooked a finger at them - a sudden force lifted Alexia into the air, and floated to the sorceress, as she laid down onto their bed."

xz "Now… Please relax, Alexia."

"The demoness drew her close, placing one hand on her back. She then slid a finger up his ass, wet with magical lubrication. Alexia drew a sharp breath, as three more hands all wrapped themselves around his body and pulled her down." 

xz "And ready yourself for bliss."

scene cg38 with fade
show alexia necklace naked aroused behind cg38
show xzaratl naked behind cg38
pause 3 

"In one smooth motion, the demoness impaled Alexia with her cock. She shuddered as a violent wave of pleasure went through her body."
"And not just physical. X’zaratl’s cock radiated pleasing warmth that seeped into her - the slight fog of lust that covered her thoughts suddenly gave way to burning desire, and she grew to realize how awfully empty her pussy was. "

al "A-ah~... Rowan…"

"Her magic stripped him to, and he watched, his cock rock hard, as X’zaratl spread his wife’s lower folds open."

xz "Speak your mind, Alexia. Tell him what you desire. Tell him how you feel every week when he returns to the castle."

"The demonic mistress pushed her hips forward, forcing more of her cock in, but that only served to accent what she was missing. Alexia licked her lips, and locking eyes with Rowan, let her emotions pour out-"

al "I want- I want your cock Rowan. Every day- every time I see you back at the castle - I fantasize how you’ll take me today."

"Her empty snatch quivered before his very eyes. He wanted nothing else but to thrust into it - but something in X’zaratl’s eye stopped him."

al "How you’ll fill me- How you’ll come inside of me! Rowan!"
al "Rowan, love, fuck me already!"

"A short nod, and a smile - and he felt like a dog released from his leash. Free again, Rowan rushed forward, climbing his wife and pushing his own cock into her womanly passage."

scene cg39 with fade
show alexia necklace naked aroused behind cg39
show xzaratl naked behind cg39
pause 3 

al "Ahamama..."

"She whimpered, her eyes rolling back in shock from the sensory overload."
"Rowan could feel the hardness of X'zaratl's shaft against his, separated only by a few soft walls. Sweet moans filled his ears, as he thrust again, and watched his wife giggle in delight."

xz "Relax, fair Alexia. Relax, and let the bliss take you."

"X’zaratl’s guiding whispers could be heard even through his wife’s lustful cries. The demoness arms wrapped themselves around him, and as she started thrusting, urged him to mimic her movements."  
"And as he saw Alexia’s supple tits jiggle with every thrust, and felt another hand guide his head down, he allowed X’zaratl to set the tempo, thrusting in unison with the demons, so he could focus on the wonders before him." 
"He started licking and sucking on Alexia’s nipples, and In response, the red head's moans soon almost grew into screams."
"These were quickly muffled by fingers pressed into her mouth by X'zaratl, which Alexia sucked and licked almost instinctively.  It was about the only thing she was doing at this point, the rest of her having gone limp from the incredible pleasure of the threesome."
"This went on for a long while - far longer, than he imagined. X’zaratl controlled the pace with grace and skill that befitted a sex demon." 
"And whenever he stopped showering his Alexia’s body with kisses and caresses, he found himself looking into the demoness sparkling eye."  

xz "I can feel your love for her with every thrust, gallant Rowan. You truly are a man like no other, and Alexia was blessed to be chosen by you."

show cg39 with sshake
show cg39 with sshake
show cg40 with flash
pause 3
show xzaratl naked behind cg40

"Finally, after what had to be several orgasms by his wife, Rowan could take it no more, and found himself unleashing his seed into her passage. As if on command, X’zaratl came too, filling Alexia twice over." 
"… And none of that seemed to have much of an effect on Alexia, who continued to give out muffled moans around X'zaratl's fingers, as her passage continued to quiver and clench around her husband's cock."

xz "Fill her in, Rowan. She deserves it."

"In spite of the increased sensitivity of having just came, Rowan was surprised to find that his hips wouldn't stop moving - they didn’t want to stop moving." 
"He kept thrusting, cumming into his wife - and only after the last drop was out, exhaustion seized him, would he collapse on top of her."

scene black with fade

"Her lips sought his, and soon after, darkness took him."

jump xzaratlSharedSexEnding

label xzaratlSharedSexEnding:

scene cg31 with fade
pause 3
show alexia necklace naked behind cg31
show rowan necklace naked behind cg31

"They woke in each other’s arms some hours later, tucked into their bed, cleaned, and embraced. He kissed his wife on the head, and she stirred in his arms."

al "That was… Wow."

ro "Yeah."

al " … Remind me - why were we reluctant to meet her?"

if RowanXzaratlDominantStart == True:
    "That made him stop. This wasn’t how this was supposed to end - they were supposed to keep things professional, and before either of them noticed, they were halfway through a threesome."
    
else:
    "That made him stop. This wasn’t how this was supposed to end - they were supposed to have a friendly conversation, not start a mindblowing threesome."
    
al "You seem worried."

ro "Did you feel… Controlled, in any way?"

al "… No? I don’t think so. Maybe a little lightheaded, but not “controlled”. You?"

if cliohnaHJ == True:
    "He shook his head. He knew magic like that - and it never managed to hold him, not for long. Even a mage like Cliohna had no success."
else:
    "He shook his head. He knew magic like that - and it never managed to hold him, not for long."

ro "And yet… Don’t you feel like we shouldn’t be… This open about welcoming X’zaratl into our bedroom?"

al "… Maybe not. Or maybe we’re just this starved for someone who doesn’t seem to have an agenda?"

ro "… Maybe. There’s still much we don’t know about her."
ro "Let’s keep an eye out, and our guard up, alright? Just in case. So that every encounter with X’zaratl doesn’t end like this."

al "Oh no, that would be horrible."

"He heard her giggle, and grunted in mock annoyance."

scene black with fade

"… It really would be “horrible”..."

return

label xzaratlAdvancesEarlyEnding:

show rowan necklace neutral at midleft with moveinleft
show alexia 2 necklace neutral at edgeright with dissolve

ro "Did you feel… Controlled? In any way?"

show alexia 2 necklace shocked at edgeright with dissolve

al "… No? I don’t think so? Maybe a little dazed, now that you mention it."

show alexia 2 necklace concerned at edgeright with dissolve

al "Rowan, do you think she’s doing something to us?"

show rowan necklace angry at midleft with dissolve

ro "I don’t know. If she is, it’s unlike anything I ever experienced. I never met a mage that managed to take hold of me - at least not for long."

al "If she {i}is{/i} doing something, how do we defend ourselves? How do we fight back?"

"His hand went to the amulet at his neck. He turned it in his fingers, furrowing his eyebrows."

show rowan necklace neutral at midleft with dissolve

ro "We don’t. We avoid her when we can. We don’t talk to her unless we feel like we need to. She seems inclined to play nice, so we don’t escalate unless the situation calls for it."
ro "I can’t keep chasing every demon with a possibly nefarious plan. I’d never sleep if I tried. "

"The blue crystal sparkled in the afternoon light. He had to take calculated risks. Maybe indulging X’zaratal was worth the information and influence. Or maybe not."

al "You’re sleep deprived as it is, Rowan. Try to look after yourself, will you?"

show rowan necklace concerned at midleft with dissolve

"He heard the worried undertones in her voice. Alexia stood in front of him, suddenly looking awfully lonely. She could use a companion - and protector too, for when he was away." 

show rowan necklace happy at midleft with dissolve
show alexia 2 necklace happy at edgeright with dissolve

ro "… I will. I promise."

scene black with fade

"And even though X’zaratl would no doubt love to play the role, neither of them knew what strings were attached."

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label trip_to_library:
# A Trip to the Library
# Requires post week 8, priority after week 11.

scene bg12 with fade
show cliohna neutral at cliohnaright with dissolve
show alexia 2 necklace neutral at midleft with moveinleft

cl "Ah Alexia, hello. Haven’t seen you in here for a while."

"Despite the arrival of the other woman, the sorceress did not look up from the tome on the desk before her, continuing to study intently whatever was contained between its covers."

al "Yes, I meant to visit sooner, but things have been a bit hectic since Rowan appeared and I haven’t had as much as free time as I did before."

cl "I was beginning to think that you had lost interest in our little collection."

al "Oh no! I love reading."

cl "Glad to hear it. It is nice to know there’s a least one other person in this castle who isn’t an ignorant savage."
cl "There’s hundreds of years of knowledge in this library, some of it lost to the rest of the world, and most of these books look like they have never been touched. "

"The librarian let out a loud sigh and closed the book in front of her."

cl "Anyway, how can I help you today?"

show alexia 2 necklace look away at midleft with dissolve

"The directness of her question seemed to set Alexia back a little, who looked down at the floor as she replied."

al "Well, I’ve been in this castle for months now, and to be honest I don’t know anything about it...."

cl "Hmmm?"

al "...or the people who inhabited it, and I was just wondering, if, maybe, somewhere…"

cl "Yes?"

al " ...there might be some books in the library about that sort of thing?"

cl "If it is information about the castle itself that you are interested in, you’d do better talking to Skordred instead, as he was originally involved with its construction. He’ll probably know more about it than any book that I have here."
cl "As for its inhabitants, there are no books on the twins themselves, but if it is knowledge of their line you are after, you might try demonology, aisle 67 on the left."

show alexia 2 necklace happy at midleft with dissolve

al "Oh, thank you."

cl "I’d take you myself, but I have a lot of work that needs to be done."

al "No, I’m sorry for taking up so much of your time."

cl "It is quite alright. If you will excuse me…"

"The blonde reopened the book on her desk and returned to whatever it was that she had been studying before the other woman had arrived. Armed with the knowledge of where she might find the book that she sought, Alexia headed off deeper into the library."

scene black with fade
scene bg12 with fade

"While she had spent quite a bit of time exploring the place when she had been a prisoner of the twins before being reunited with her husband, Alexia had never been this far into the library before."
"It took her longer than she thought it would to reach her destination as all the aisles began to look similar, and some of them seemed to be endless. Eventually, almost an hour after she had left the librarian at the desk, she stood before the demonology section."

show alexia 2 necklace neutral at midleft with dissolve

"Cliohna had elected not to mention how large it was. Nor that, as far as Alexia could see, any of the books had been written in any sort of language that she was able to recognize."
"One book stuck out from the others. It was large and bound in some sort of thick brown material that had begun to crack with age. She ran her finger over the strange gold symbols that adorned its spine, and it was thick with dust as the librarian had earlier lamented. "

show andras smirk behind bg12

an "I wouldn’t touch that one, if I were you."

show alexia 2 necklace shocked at midleft with dissolve
pause 1
show alexia 2 necklace neutral at midleft with dissolve

al "Oh, Andras! You scared me."

hide andras
show andras happy at midright with dissolve

an "Azar’s {i}Theologica Demonica{/i}, written after the mage was driven mad by his attempts to see beyond the veil into the Outer Dark, and bound in the flesh of his disciples."

"The woman withdrew her hand in disgust."

al "That’s… That’s…"

show alexia 2 necklace shocked at midleft with dissolve

al "How vile!"

show alexia 2 necklace neutral at midleft with dissolve

an "True. All humans who foolishly think that they can harness the power of chaos end up changed by the experience, more often than not in horrifying ways. That is, if they even survive."
an "It is seductive none the less though, as you can attest to."

"Terrifying as it was, the demon was right. There was no denying that she had felt drawn to the one book alone among all the others, and even now, having learned what she had, she still seemed unable to take her eyes off it."

an "Don’t worry, that book isn’t for you. I think you’ll find this one a lot more helpful."

if andras_alexia_sex == True:
    "The demon came and stood behind her in front of stack she was currently perusing. This is the closest she had been to him since the event that occurred a few weeks ago."
    "The return of her husband, as well as Andras’ actions, had made it easy for her to avoid him, but now there was nowhere for her to go."
    "He leaned forward to take something from the very top shelf, bring his front into contact with the woman’s back. She could feel the demon’s cock, still huge despite its currently dormant state, press against the small of her back."
    "The sensation caused her to grow flush, as flashes of memory came back to her; the waves of pleasure she had felt when he had used her so roughly. But was her redness shame at the way in which her body had betrayed her, or arousal?"
    "Using what was left of her willpower, she broke contact from Andras, pushing herself flat against the shelves before her. As she did, the demon, who had clearly been lingering, brought down another dusty old tome from the shelf."
    "While this one was different, bound in red leather and gilded with gold, the runes on the cover were just as indecipherable as all the rest."

else:
    "The demon came and stood behind her in front of stack she was currently perusing. He leaned forward to try and take something from the very top shelf, but Alexia was too smart to allow him to trap her this way."
    "Leaning flat against the shelves in front of her, she was able to avoid his obvious attempt at forcing contact."
    "More amused than angry at the human’s evasive tactic, he brought down what he had been reaching for, another dusty old tome from the shelf."
    "While this one was different, bound in red leather and gilded with gold, the runes on the cover were just as indecipherable as all the rest."

an "I think you will find that this is more along of the lines of what you were looking for."

"He took a step back and handed the book to her. It was surprisingly heavy for its size, and she almost dropped it when she took it from him. She cracked open to discover the book was filled with more of the strange language that she had seen on the cover."
"As she flipped through the pages, she discovered it also contained illustrations."

al "Andras, these images…."

"The book was filled with depictions of violence and lewd acts that shocked the human woman to her very core. She slammed it closed, and held it out to return it to the demon who had given it to her."

show alexia 2 necklace angry at midleft with dissolve

al "This is not something suitable to give to a woman!"

an "You wanted to learn about demons, and those are the things that demons do."

show alexia 2 necklace neutral at midleft with dissolve

al "Even so, I can’t understand a single word in it."

an "Take it to my sister, she’ll be more than happy to help with reading it."

"Alexia was torn as she looked at the book in her hands. What lay between its covers disturbed her, but there was a chance it could contain information that would be useful. That would be worth the potential risk, surely?"

al "I’ll… think on it. Thank you, Andras."

an "Think nothing of it, and if you need any more suggestions about books, you only have to ask."

hide alexia with moveoutleft
show andras smirk with dissolve
pause 2
# activate "the_demonic_tome" with a timer
$ activate_event('the_demonic_tome')
$ set_event_timer('the_demonic_tome', 'after_trip_to_library', dice(3)+3)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label goblin_family_dinner:
# Goblin family dinner
#Requires that Rowan have talked to Cla-Min about goblins.

$ gobFamDinner = True

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

ro "There, done."

"The hero let out a long sigh of relief. He was finished his duties for the day and would have the evening off before he had to go out again on his weekly scouting mission."
"He might still do some last minute decisions for construction or purchases, but the stuff that actually took up his time was done."

show clamin happy at midright with moveinright

cla "Rowan! How nice to see you're finished in time for a little dinner I've been putting together for you."

ro "No, you've been hiding behind that pillar for almost an hour waiting for me to finish."

cla "Oh don't be silly, why would I ever do that?"

ro "You also tried to catch me for breakfast and then lunch. You've been trying all day to get me to come to this family dinner."

# Cla-Min looks shocked.

cla "How? I thought..."

#Cla-Min smiles.

cla "Well, if you hadn't seen through a trick like that, I suppose you wouldn't be much of a hero for my people, would you?"
cla "Still, I do hope that you'll grace us with your sly presence. I really did put a lot of work into this, just for you."

show rowan necklace happy at midleft with dissolve

"Rowan rose from his work table, looking somewhat exasperated but also smiling."

ro "Alright, let's go meet your family."

"The goblin matriarch bounded up to him excitedly and grabbed his hand. She tried to drag him back to her caravan, but the difference in size and weight meant that in the end she was forced to just lead."

# Transition, show first CG.  Table inside a large wagon with Cla-Min's immediate family in the image.
scene bg19 with fade

"Even before they got in, the smell of roasted meat and potatoes was quite strong and many voices could be heard chattering away excitedly. In spite of the circumstances, the man felt his stomach growl in anticipation."
"As Rowan was ushered inside the wagon, he found he had to stoop slightly to avoid banging his head on the ceiling. Made sense, goblins didn't need as much headspace as humans. What was more surprising was the number of them crowded around the table."

scene cg613 with fade
show clamin neutral behind cg613
pause 3


cla "Everyone, may I present to you the great hero Rowan! And to you Rowan, we are all so happy to welcome you this evening to meet and let you sample true goblin hospitality!"

"She swept her arm wide around the table as the gathered crowded in and jostled against one another. Almost everyone was as excited as Cla-Min herself had been the first day she'd met Rowan. The excitement was plain on her face too, plus what looked like a triumphant smirk."
"There were a dozen of them, of various ages. Excited whispering broke out among them while the hero was led to a cushion on the floor, the rest of them were sitting on small chairs, but the table was too low for a human to sit on one of those comfortably."

scene cg614 with fade
show clamin neutral behind cg614
pause 3

cla "Take a seat here, right next to me and my dear twin brother, Cla-Bow."

"She indicated the goblin with an easy going air and a rather simple shirt. As Rowan sat down, he noticed a glint in the goblin's eye, just before it turned into an altogether different kind of smile."

cla "Don't underestimate him, he's really good at looking like he isn't any trouble, but he definitely is!"

scene cg615 with fade
show clamin neutral behind cg615
show rowan necklace neutral behind cg615
pause 3

cla "Back there is my paw, Cla-Sty. He led us all for many years before me, but he isn't as quick as he once was so he passed the reins on to me."

gob "But don't think for a moment I can't still match wits with my beautiful eldest girl."

"The old goblin chuckled mirthfully and nodded in appreciation to his daughter."

cla "Then we have my younger brother Cla-Sel.  He's actually a single born child, if you believe it. Great with the animals, both driving them and cooking them."

"In response he raised up a leg of meat, liberally dribbling some kind of gravy."

gob "Don't take sis's word, try it for yourself, we've got lots for everyone!"

ro "Yes, it looks good. I take it you cooked a lot today then?"

"His grin faltered slightly and signs of fatigue crept in, but he kept the smile on his face."

cla "Next we have my younger sisters Cla-Sel and Cla-Tre. Inseparable, good at chestwork and needles. Need someone to work on your clothes? They're your girls."

"The two pink haired girls in matching dresses didn't say anything, but one ran a bit of food around her lips, while the other pulled open her blouse even further than it already was and waved her hand as if she were hot."

ro "Hmm hmm."

scene cg616 with fade
show clamin neutral behind cg616
show rowan necklace neutral behind cg616
pause 3

cla "But as wonderful as my siblings are, the best bundles of joy here are my kids! Those two rambunctious rascals are Cla-Sty and Cla-Tod..."

gob "Pleased to meet the hero! We got out our best brew for the occasion!"
gob "Hey watch it Tod!"

"The two boys had been drinking when Rowan'd come in, and while they'd stopped just for a moment to look at the new arrival, but they were pretty tipsy already and quickly got distracted. However it was the girl next to them that caught Rowan's eye."

cla ".. and of course we have my darling daughter Cla-Min."

ro "So your daughter has the same name as you?"

cla "Well yes.  It's a really common name, there's three of us at the table! Sty was named after my father and Tod for his. If you have trouble keeping them apart, just call her Min and we'll know who you're talking to."

"The moment that Rowan locked eyes with Min again, she stretched her arms out on the table to emphasize her chest, then poked her tongue into her cheek with a sultry look in her eyes. It seemed like all the women here wanted him!"

cla "She's very gifted with her month, so I've been teaching her everything I know."

scene cg617 with fade
show clamin neutral behind cg617
show rowan necklace neutral behind cg617
pause 3

"Next were two notably smaller goblins, wearing robes far too big for them."

cla "Those two there are my youngest twins; Cla-Kes and Cla-Lij."

"She faltered slightly. Cla-Lij had taken advantage of how distracted everyone was and helped himself to the feast, while his brother made fun of him with a pair of fingers behind his head. These two made Rowan chuckle. Here were boys being boys, no different from humans."

cla "Ehem. Lij? Cla-Lij!"

gob "Oh uh? Hi there...."

"Realizing he'd been caught, he put the leg back down with a guilty look to his mother, then whipped a trickle of sauce on the sleeve of his shirt. A white sleeve. Cla-Min winced slightly, but moved on to the last two at the table."

cla "Here we have Ver-Tod, adopted fully into our family and the father of many of my children."

"Ver-Tod waved his hands above his head in a salute of sorts. The goblin's armor marked him as a warrior if Rowan's eyes didn't mistake him and he returned the gesture from one fighter to another."

cla "Lastly is Ver-Min, Ver-Tod's sister, and she'll be joining us as a guest this evening."

"Like the other women, the third Min at this table had a smoldering look in her eyes and she had climbed halfway onto the table to show off her cleavage to Rowan. Unlike the others though, Cla-Min gave a frown to her sister-in-law who shrugged in response."
"These two looked fairly different from the rest of the goblins, different skin tones and face shapes."

scene bg19 with fade
show rowan necklace happy at midleft with dissolve
show clamin happy at midright with dissolve

"Rowan swept his eyes across everyone at the table again, taking in the dozen new smiling faces. Faces filled with adoration at their sneaky sly hero of deception and trickery."

ro "It's good to meet you all."

cla "Welcome again Rowan!"

"Everyone at the table exploded into conversation all at once, drowning almost everything out. Some of the siblings were talking to one another, others were trying to address Rowan. The matriarch clapped her hands together to silence everyone."

cla "Hold on, quiet! Boys, please bring out the rest of the food. Let's show our guest a good time!"

"Her four sons plus her younger brother quickly jumped up and rushed out of the room. They returned shortly afterwards with steaming pots and placed them on the table, more than doubling the amount of food being served!"

scene cg311 with fade
show clamin happy behind cg311
show rowan necklace happy behind cg311
pause 3

"The meal served was roasted meat, potatoes and nuts. For the most part game and forage, but some of it obviously would have been traded for. Goblins could eat most things, but they really liked meat with bite sized bones and anything that had a good crunch to it."
"They were also fond of fresh blood, which was also served (probably from the same animals that supplied the meat), though Rowan passed on that."
"At first Rowan was the only one that anyone wanted to hear about. The family here wanted to hear all about their hero's goblin-like traits, famous tricks and feats of dexterity for the most part. It was interesting to learn which parts of his tales were the most famous from their perspective."
"He just wished that they didn't get annoyed at him everytime he mentioned anything that sounded heroic or honorable. This audience didn't like to hear that their ideal trickster had a goody two-shoes human scum side to him."
"Eventually the group shifted to small talk and several smaller conversations sprang up around the table."
"For the most part they discussed either the food or their latest trading operations. Before being pulled into one such talk himself, Rowan noted that these caravaners had been putting their access Jezera's portals to good use."
"Min was the only one at the table that didn't seem to have anything to say, always looking down shyly and only raising her head to steal glances at Rowan when she thought he wasn't looking at her."
"That girl almost certainly had a crush on him, the hero was fairly certain, but then he got distracted by her mother."

cla "So what do you think of my little family?"

ro "They're a lively bunch. I haven't seen too many goblin families before, but this does feel like a home. For all your talk of schemes and tricks, you all trust and love one another."

"The matriarch puffed up with an air of pride about her."

cla "Yes, family is a wonderful thing. It's one thing that we caravaners have learned about from the other races. I wouldn't trade any of my children or relatives here for anyone."

"She took Rowan's right hand, making him glance down in surprise. When he looked back up, he saw that she was giving him a very meaningful look."

cla "There's a place for you here too, if you'll join us. We goblins don't practise monogamy you see and are quite willing to invite anyone worthy into our ranks."

# to be added when we have cla-bow sprite
#"Rowan looked around, trying to find something to turn the conversation away from that direction. He found Cla-Bow on his other side who was watching them with interest."
#ro "What about you, Cla-Bow, have you got any children or another goblin family that you're away from tonight?"
#Cla-Bow: Nah, never been one for girls myself, last I checked you need those to make kids.  Handsome men like yourself have always been my thing.
# Now he took the man's left hand while flashing a big toothy grin!  Trapped between the two, with both hands held, one final shock was given as someone started to undo Rowan's pants!

"Cla-Bow, the goblin on his left, also made his interest in Rowan quite obvious, taking his hand. Trapped between the two, with both hands held, one final shock was given as someone started to undo Rowan's pants!"
"His gaze shot downwards and discovered the shy goblin girl, Min, was currently working at his pants with a look of reverence and her tongue hanging out. Was she about to... wait, had this entire dinner been a setup for this?"

menu:
# Choice:
    # "Receive a blowjob from Min."
    "Receive a blowjob from Min.":
        # Jump to Min's blowjob.
        jump .mins_blowjob

    # "Stop the girl."
    "Stop the girl.":
        "He shook his hands free from the two goblins on either side of him and pushed the young woman between his legs away from him."
        "This actually shocked the girl, and she intentionally made eye contact with Rowan for the first time this evening with a pleading look. Before he had a chance to say or do anything more, her mother placed her hands on his arm again and spoke softly into his ear."
        cla "Please accept our hospitality. My family is very eager to make you feel welcome in every way we can, especially my darling Min."
        "Rowan looked to meet the shy goblin's gaze once more, however she was looking at his pants again, lips slightly parted and pushing against his grip. Evidently she really did want him."
        menu:
            # Choice: "Give in and let Min blow you."
            "Give in and let Min blow you.":
                # Jump to Min's blowjob.
                jump .mins_blowjob
            # Choice: "No means no."
            "No means no.":
                "There was a final shake of his head, at which point Cla-Min relented and shooed her daughter away. The younger Min was obviously disappointed, but did as she was told."
                "The so-called goblin hero turned to apologize for rejecting this advance, but hesitated when he saw that Cla-Min was smiling conspiratorially at him."
                cla "Don't worry, next time I'll get you into my family for sure!"
                "With that, she returned to her meal and acted like nothing had happened."
                # Jump to meal ending.
                jump .meal_ending

label .mins_blowjob:
#Min's blowjob
# CG, under the table, Rowan being blown by a female goblin, Cla-Min's foot is giving direction.  Also cum variation.
$ goblin_family_dinner_mins_blowjob = True

scene cg94 with fade
show clamin happy behind cg94
show rowan necklace happy behind cg94
pause 3

"No resistance was given as the goblin girl undid his trousers and pulled them apart, allowing the man's cock to flop free. Rowan glanced around hurriedly to see if anyone was looking at him, though no one was paying any attention anymore except for Cla-Min and Cla-Bow."

"Evidently these two were in on it, what with all the holding his arms back so he didn't interfere with Min, who was now eagerly licking his semi-erect member."
"He started when she poked a finger underneath him and invaded his rear, though he couldn't do anything about it between not wanting to alert the table and being somewhat tied up."

cla "I must say Rowan, that there would be no human more worthy to join my family than you."

ro "Sorry, what was that?"

"He sharply inhaled as the younger Min opened wide and stuffed her face with his manhood, taking it up to the hilt with a single motion."

cla "Everyone here would be eager to have you join us anytime, in any way! Well, at least there'd always be someone who's willing to take you in whatever way you want."

"It was difficult to concentrate on what the matriarch was saying, being distracted two ways from trying to focus on both what was going on between Rowan's legs and what the girl's mother was saying."

ro "Well, that's a very nice offer of yours."

"Min began to bob her head up and down while also curling her finger that was embedded in him, trying to find something...."

cla "Of course! If you need someone on top of you, I'm your girl. If you're after some male company, Cla-Bow here has you covered. Min, when she decides to show her face again..."

"Cla-Min winked to Rowan."

cla "...I'm sure she'll eat up anything you need to get out of you."

"Rowan tried to shift in his seat, and was rewarded with a whining sound from under the table as the girl blowing him tried to keep him planted exactly where he was."
"He looked down, and was surprised to find that Cla-Min actually had a foot on her daughter's head, directing her movements!"

cla "We're a talented bunch, with a great matriarch and teacher. So just think of how much more we'll be with you in our numbers? Maybe our children can be even greater with such an amazing hero in their ancestry."

scene cg94 with sshake
scene cg94 with sshake
scene cg95 with flash
show clamin happy behind cg95
show rowan necklace happy behind cg95
pause 3

"A sudden jolt of pleasure flooded through Rowan's body as Min found what she was evidently looking for in his ass, which then sent him into the throws of orgasm. As he did so, Min's head dropped down to the hilt again and he came directly into her throat."
"She seemed to hum contentedly as he sputtered in her, the vibration adding something that the man had never felt before. This girl was quite good at giving blowjobs."
"Her skill was such that she never coughed or gasped when she finally pulled back off of him and retreated back to her side of the table."

# Rowan at the dinner table CG again.
scene black with fade
show clamin happy behind black
show rowan necklace happy behind black

cla "What do you think Rowan, will you join the Cla family? I'll make certain that you never regret it."

ro "I- wait, no I have a family. Alexia is-"

cla "She can join too! It's not a problem at all, just so long as she doesn't hog you all to herself."

"Rowan only frowned and pulled back, trying to collect himself again. However the goblin didn't seem to be taken aback at all, instead smiling conspiratorially."

cla "It's fine if you need a little time before you make the jump. It is a big life choice after all. Just remember that your goblin family is here, waiting for you."

"The conversation seemed to just end there, leaving Rowan feeling somewhat overwhelmed. This was, without a doubt, the strangest way of securing a mate he'd ever encountered."

# Jump to meal ending

label .meal_ending:
# Meal ending
"The rest of the evening was blessedly uneventful. While this was by no means a standard meal by human standards, Rowan had dined at the tables of many different races and was reasonably comfortable with unusual hosts or guests."
"Eventually he excused himself, and left the wagon to a chorus of happy goodbyes and questions of when he'd be joining them again."
"He took with him a bowl of deep fried potato wedges, intending to share some of the crispy things with Alexia. The thing he was most happy to leave behind was the annoying grinding sound from goblins gnawing on bones."
"Just thinking about it made him shudder. That was one thing that would be haunting his nightmares from now on."

$ activate_event("clamin_bribing_proposition")
$ set_event_timer('clamin_bribing_proposition', 'after_family_dinner', 3)
# End scene
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label problem_squad:
# Problem squad
# Req at least 10 orc soldiers and morale less than 70%.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show orc soldier neutral at midright with dissolve

ro "So this is all of them?"

os "Yes lord."

"Rowan surveyed the group. There were five of the orcs, four men, one slightly bigger than the others who'd become their leader, plus a woman."
"This group had become dissatisfied with serving in Andras's armies and were causing trouble now. They wanted better beds, better food, better everything. Even giving them the smallest of concessions had only made things far worse."
"Now the steward had to decide what to do with them.  Their troublemaking could no longer be ignored."

menu:
    # Choice: "Challenge the leader to a duel." - Req lv 1 Arena.
    "Challenge the leader to a duel." if castle.buildings['arena'].lvl >= 1:
        "It was time to deal with this problem in the traditional orc fashion, that would definitely get through to them. He stood and pointed at the leader."
        ro "It's time to see if you're worthy of everything you think you deserve. A duel to the death! Prepare yourself, we will soon face one another in the arena!"
        "All the orcs in the chamber erupted into guttural cheers, with one exception. The leader, who stared daggers to the man."
        # arena background.
        scene black with fade
        show rowan necklace neutral at midleft with moveinleft
        show orc soldier neutral at midright with moveinright
        play sound "music/SFX/sword_draw.ogg"
        pause 1
        play sound "music/SFX/orc_attack.ogg"
        pause 1.5
        play sound "music/SFX/sword_hit_1.ogg"
        show black with sshake
        pause 0.3
        play sound "music/SFX/sword_hit_2.ogg"
        show black with sshake
        pause 0.3
        play sound "music/SFX/sword_hit_3.ogg"
        show black with sshake
        pause 0.3
        "An hour later, the two fought one another in the arena. The battle was fierce, though the ending was not in doubt for Rowan. This orc was sloppy, poorly trained. He'd actively avoided learning how to fight, resenting the entire military system."
        os "Rawrg!"
        "Suddenly he dived forward, throwing himself entirely into a massive frontal attack."
        ro "(Idiot.)"
        "That move had left the orc complete exposed, allowing Rowan to easily duck forward and cut into the orc's chest, piercing its heart."
        show black with redflash
        "However much to Rowan's shock, this didn't disable the orc, instead it continued is attack and brought down all its strength into one final attack on the man. Apparently it never expected to actually win the duel, just wanted to hurt him!"
        #rowan hurt
        ro "Argh!"
        "He screamed in pain, desperately wrenching himself to the side before his entire body was torn in half. He nearly lost an arm in the process, but managed to get free of the mighty attack as the orc's blow hit the ground, then his broken heart finally caught up with him and he dropped to the ground unmoving."
        "Grunting with supreme effort, the hero stood up and raised his sword triumphantly above his head as the crowd of soldiers around him roared."
        # //End scene, Rowan is injured, -1 orc soldier, + morale.
        $ add_effect(Injury('Wound', 'strength', -2))
        $ castle.buildings['barracks'].troops -= 1
        $ castle.morale += 1
        return

    # Choice: "Fire them."
    "Fire them.":
        "It was time to cut this troublesome lot free."
        ro "You're fired.  The whole lot of you. If you can't follow orders or manage with the accommodations we give you, then you have no place in this army."
        "This seemed to startle the troublemakers and they glanced around between one another in confusion."
        ro "Get out of my sight."
        scene bg14 with fade
        show orc soldier neutral at midleft
        show andras displeased behind bg14
        "The group was lead away from the throne room and towards the castle entrance. Instantly the leader started loudly complaining that this couldn't be done, he was too important to Andras's armies and that the demon would not be happy about this."
        an "What was it that I wouldn't be happy about?"
        hide andras
        show andras displeased at midright with moveinright
        os "Uh, that yous wouldn't be happy about us being fired?"
        an "No, of course not."
        show andras smirk at midright with dissolve
        #stab SFX
        show bg14 with redflash
        hide orc soldier with dissolve
        play sound "music/SFX/BodyfallDirt.ogg"
        "With several quick motions, he blasted the group of five with bolts of demonic energy, killing all of them almost instantly."
        an "You should have been executed instead."
        # End scene.  -5 orc soldiers.
        $ castle.buildings['barracks'].troops -= 5
        return

    # Choice: "Force them into hard labor."
    "Force them into hard labor.":
        "Well, if they couldn't be soldiers at least there'd be another use for them."
        ro "The punishment for your transgressions will be hard labor. You five will become slaves and work in mines or as builders."
        "A collective sound of quiet outrage sounded not only from the troublemakers, but also from several of the other orcs in the room. Apparently this wasn't a popular sentence."
        ro "That's enough, the decision has been made.  Take them away."
        scene black with fade
        "It was done in spite of the complaints, though Rowan feared that the benefits might be outweighed by the decent his decision had caused."
        # End scene.  -5 orc soldiers, - morale, + treasury.
        $ castle.buildings['barracks'].troops -= 5
        $ change_treasury(50)
        $ castle.morale -= 1
        return

    # Choice: "Turn them over to the cubi sorcerers." - Req lv 1 Dark Sanctum.
    "Turn them over to the cubi sorcerers." if castle.buildings['sanctum'].lvl >= 1:
        "Well, if they couldn't be soldiers at least there'd be another use for them."
        ro "Those who will not fight in the armies will be used for other things. You five will be turned over to the cubies, to assist them in their research."
        "A collective sound of quiet outrage sounded not only from the troublemakers, but also from several of the other orcs in the room. Apparently this wasn't a popular sentence."
        "The one person who seemed to be happy was the succubus who'd been in attendance. Already she was dancing around what she called her new 'toys' with no small amount of glee."
        ro "That's enough, the decision has been made. Take them away."
        scene black with fade
        "It was done in spite of the complaints, though Rowan feared that the benefits might be outweighed by the decent his decision had caused."
        # End scene.  -5 orc soldiers, - morale, + one time research points.
        $ castle.buildings['barracks'].troops -= 5
        $ castle.morale -= 1
        $ castle.rp += 5
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label poisoned:
# Poisoned

show bg14 with fade

#ill rowan

show rowan necklace neutral at midleft with dissolve

ro "Ugh, what?"

show bg14 with sshake

ro "(My head is spinning...)"

show bg14 with sshake
hide rowan with dissolve
play sound "music/SFX/BodyfallDirt.ogg"

# If Alexia is pure
if all_actors['alexia'].corruption < 10:
    show alexia 2 necklace concerned at midright with moveinright
    al "Rowan?  What's wrong!?"

scene bg9 with fade
show rowan necklace naked behind bg9
show jezera neutral at midright with dissolve

ro "Hmm?"

show jezera happy at midright with dissolve

je "Ah good, you've awakened. I'm glad to see the initial shock has worn off."

ro "What happened?"

je "One of the castle staff tried to poison you with your lunch. I've taken care of them and will be more careful about hiring such potential problems in the future."

ro "What do you mean?"

show jezera neutral at midright with dissolve

je "That isn't your concern, just focus on your duties once you've recovered enough to continue. Your senses will probably be dulled from the after effects of the poison, but there hasn't been any permanent damage."

hide jezera with moveoutright

ro "Right."

# If Alexia is pure
if all_actors['alexia'].corruption < 10:
    show alexia 2 necklace happy at midright with moveinright

    al "Oh thank goodness, you're alright."

# End scene. Rowan is injured, -int for 3 weeks.
$ add_effect(Injury('Poison after effects', 'intelligence', -2, 3))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label salvaged_supplies:
# Salvaged supplies
# Requires pre-end of first year.

# Show workshop background (throne room for now)

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show skordred neutral at skorright with dissolve

sk "...musta been a hidden storeroom or a section that caved in during the attack. We found a few others like it before you became steward."

"The hero nodded, watching the builders bring in the supplies that they'd found under the castle while doing salvage work for materials."

sk "It isn't much, but given the state of things, every bit we can find counts."

ro "No, your men did well here. With all the unexpected expenses and setbacks, this will do much to bring us back on schedule. Is this enough to accelerate your projects or start a new one?"

sk "Aye. Give the word and I'll begin within the hour."

menu:
    # Choice: Sell the materials for 25 gold.
    "Sell the materials for 25 gold.":
        $ change_treasury(25)
        #gain 25 gold

    # Choice: Use the materials to accelerate current construction (Building/upgrade finishes instantly and trigger the event for that right after this one, if we change them to have time requirements.  Otherwise ignore this choice, also ignore it if nothing is currently being built or upgraded.)

    # Choice: Use the materials for a new project (Discount of 75 gold on next upgrade or building started)
    "Use the materials for a new project":
        # TODO discount for next project
        pass

sk "Understood... boss.  Thar was one other thing."

"After a moment's hesitation, the dwarf reluctantly handed Rowan a package."

sk "We also found this. As much as it pains me to offer it directly to you, I figured that it would be best for the masters if you had it."

# Rowan gets a free random piece of equipment.
$ get_rnd_item(0, 200)
# End scene.
return
