init python:

    #Alexia visits with Cla-Min
    event('alexia_visits_with_cla_min', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    #X'zaratl's Guilt Solution
    #Requires Dark Sanctum built, Guilt higher than x (to do),  'X'zaratl's advances' event already triggered
    event('xzaratl_guilt_solution', triggers="week_end", conditions=('week >=22',
        "castle.buildings['sanctum'].lvl >= 1", 'avatar.guilt > 35'), depends=('xzaratl_s_advances',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Andras' Challenge
    #Requires: Arena built, at least 15 orcs
    event('andras_chanllenge', triggers="week_end", conditions=('week >=4', "castle.buildings['arena'].lvl >= 1", "castle.buildings['barracks'].troops >= 15"), group='ruler_event', run_count=1, priority=pr_ruler)
    #Orc Deserters
    #Low morale event. Requires at least 15 orcs
    event('orc_deserters', triggers="week_end", conditions=('week >=4', "castle.buildings['barracks'].troops >= 15", 'castle.morale < 20'), group='ruler_event', run_count=1, priority=pr_ruler)
    #Alexia visits with Skordred
    #No requirements, but will appear at some point during the second mission in the NPC slot eventually.
    # TODO NPC slot
    # TODO check for real goal2 being active
    event('alexia_visits_with_skordred', triggers="week_end", conditions=('week >=4', 'not goal2_completed'), depends=('first_village_captured',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Rowan is feeling guilty
    #Requires Rowan have enough guilt to trigger low guilt after decay.  High priority event.  Note that conquering Raeve Keep should give enough guilt on its own to trigger this event.
    event('rowan_is_feeling_guilty', triggers="week_end", conditions=('week >=4', 'avatar.guilt > 15'), group='ruler_event', run_count=1, priority=pr_ruler_high)
    #Disease outbreak
    #Req at least 10 soldiers.
    event('disease_outbreak', triggers="week_end", conditions=('week >=4', "castle.buildings['barracks'].troops >= 10"), group='ruler_event', run_count=1, priority=pr_ruler)
    #Pure morning with Alexia
    #Requires Rowan and Alexia be sharing a room and that Alexia be pure.
    event('pure_morning_with_alexia', triggers="week_end", conditions=('week >=4', "not alexiaSeparateRoom", "all_actors['alexia'].corruption < 5"), group='ruler_event', run_count=1, priority=pr_ruler)
    #Jezera's alliance making skills
    #Requires after week sixteen, high priority event after week eighteen.
    event('jezera_s_alliance_making_skills', triggers="week_end", conditions=('week == 16',), group='ruler_event', run_count=1, priority='pr_story')
    #Drinking buddies
    #Can trigger three weeks after the forge is built.  Requires that the tavern exist. (Activated in "forge_purchased")
    event('drinking_buddies', triggers="week_end", conditions=('week >=4',), active=False, group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg21")


label alexia_visits_with_cla_min:
#Alexia visits with Cla-Min

scene bg14 with fade
show clamin neutral pipe at midright with dissolve
show alexia 2 necklace happy at midleft with moveinleft

al "Good afternoon Cla-Min. I saw you'd stepped away from work and was hoping to catch a word with you."

cla "Alexia."

"The goblin woman tapped out her pipe and looked passed the woman for a moment at her family bringing in supplies from the portal chamber.  She sighed, then stowed the pipe."

show clamin neutral at midright with dissolve

cla "Yes, I suppose I can spare a minute. I don't suppose you're looking to offload some money you stumbled on?"

al "Uh, no."

cla "Pity. Alright, what is it?"

show alexia 2 necklace neutral at midleft with dissolve

al "You and your family aren't like most of the people here in the castle. Goblin caravans aren't really Karnas supporters, regardless of what rumors often say. What brought you to this castle? Was it the promise of Jezera's portals?"

show clamin happy at midright with dissolve

cla "I'm afraid that information doesn't come free, at least not for you. One good turn deserves another, if you catch my drift."

al "Are you asking for information or a favor?"

cla "A favor, just a small thing, I assure you."

al "I can't do much for you, but alright."

cla "Wonderful! Then I'd be happy to tell you a bit about my history with the twins."

show clamin neutral at midright with dissolve

cla " It was by chance we joined the twins, but probably not when you suspect. My caravan met up with them on the road before they'd taken up residence in this castle. They needed to bring people and supplies across the wastes, we needed their coin."

al "How long ago was that?"

cla "About two and a half years."

al "What were the twins like back then?"

cla "Less entitled, but we didn't talk much since I kept me and mine away from them. A good mother doesn't let demons mess with her family."

al "So why did you take the job if you didn't trust them?"

cla "Jobs like that are few and far between for goblins, so we usually take what we can get. That said, after the third trip over the wastes for more stuff, I was thinking it was time to call it quits. After all, I have to look out for my family and endless barrans are no place to raise children."
cla "However, it was then that things changed, as Jezera told me she'd managed to get that portal open and was in the process of opening up other gates around the whole of the Six Realms!"

"The goblin tapped a finger to her nose knowingly."

cla "Now I could see the way the wind was blowing if these two could go anywhere in the world at any time. If we agreed, gone would be the days of runs through dirt and sand, now we could go see woods, plains, or the sea whenever we wanted!"
cla "Even if the twin's plans don't pan out, this job has probably already made Cla the richest goblin caravan in the world and since things just keep getting better here, I have every intention of sticking around until the town bells are ringing."

al "Thank you very much for the story."

cla "If you're truly grateful, then I'll ask one simple thing of you."

al "Certainly."

cla "Don't get too fussed up if I or someone from my family makes a move on your husband. Thanks darling."

hide clamin with moveoutright

"Alexia was left speechless as the goblin matriarch headed off to rejoin the rest of her family who'd just finished unloading supplies. By the time she collected herself and followed after Cla-Min, they'd all left back through the portal."

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label xzaratl_guilt_solution:
#X'zaratl's Guilt Solution
#Requires Dark Sanctum built, Guilt higher than x (to do),  'X'zaratl's advances' event already triggered

$ released_block_rollback()
scene bg14 with fade
show rowan necklace neutral at center with dissolve
show xzaratl neutral behind bg14

xz "Oh, Rowan..."

if RowanXzaratlInfluence > 3:
    show rowan necklace happy at center with dissolve
    "The succubi's teasing, lilting voice echoed down the corridor, each syllable seeming to trail off into a disarming, intimate whisper. It brought back memories of their past encounters and he smiled, weakly, at the sight of her. "
    hide xzaratl
    show xzaratl happy at midright with dissolve
    hide rowan
    show rowan necklace happy at midleft with moveoutleft
    ro "X'zaratl. What do you want?"

else:
    "The succubi's teasing, lilting voice echoed down the corridor, each syllable seeming to trail off into a disarming, intimate whisper."
    show rowan necklace angry at center with dissolve
    "Rowan tensed. What new tricks was the creature going to try out on him this time? He was in no mood for them."
    hide xzaratl
    show xzaratl happy at midright with dissolve
    hide rowan
    show rowan necklace angry at midleft with moveoutleft
    ro "X'zaratl. What do you want?"

xz "To make you happy. You and your delightful wife. Didn't I make you happy last time? Wasn't it so good for you, once you abandoned your frigidity and etiquette and allowed me to open up a few new vistas of ecstasy to you?"

show rowan necklace neutral at midleft with dissolve

ro "This is not a good moment. "

show xzaratl neutral at midright with dissolve

xz "I know. I see it all too well. Dark clouds gather around you -  your face is marred with worry, and I can see the dark bags under your eyes. Something troubles you, gallant Rowan."

menu:
    "A hundred sins. Prelude to a thousand more.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        "His hollow laugh echoed across the castle hall. Was it that obvious?"
        show rowan necklace neutral at midleft with dissolve
        ro "I’m on a quest to conquer the very homeland I once saved from near-certain destruction. The things I’ve done- "
        show rowan necklace concerned at midleft with dissolve
        "He stopped. Where was he supposed to begin? Should he start from the smallest atrocity and work his way up, or the other way around?"
        "Or maybe it would be better to start with Briarbridge, and recount them chronologically? Maybe he should get Liurial to compile a list, perhaps do it alphabetically-"
        "A warm hand grabbed his own, he found himself looking into X’zaratl sympathetic eye."
        xz "I know. You don’t have to tell me. There are times when words fail."
        
    "Your guilty conscience is none of her business.":
        $ released_fix_rollback()
        show rowan necklace angry at midleft with dissolve
        ro "I don’t want to talk about it. And you shouldn’t pry."
        "She reached for his hand, and he pushed it away, throwing her an angry glare. Her inquisitive eye met his." 
        "It was the same look Alexia always gave him, when she felt something was wrong. Concern barely concealed."
        show rowan necklace concerned at midleft with dissolve
        "He was the first to look away."
        xz "You don’t have to tell me. That’s alright. There are times when words fail. I understand regardless."

xz "I see you every time you return from your excursions in Solansia. I know what the twins expect of you. And I know it doesn’t always align with what is right."

show rowan necklace neutral at midleft with dissolve

xz "It must be hard for you."

ro "If it were easy, anyone could do it. Now excuse me, there’s still work to be done."

"He didn’t have time for self-pity. Difficult compromises were just that - difficult. But they had to be done."

hide rowan
show rowan necklace angry at midleft with dissolve
show rowan necklace angry at midright with moveoutright
hide xzaratl
show xzaratl neutral at midright with dissolve
show xzaratl neutral at edgeright with moveoutright


ro "X’zaratl."

xz "Hear me out. Please. It pains me to see you like this."

if RowanXzaratlInfluence > 3:
    show rowan necklace neutral at midright with dissolve
    "She placed a hand on his chest, her voice begging him to stay. How could he say no?"
    jump xzaratlIdea
    
else:
    "She placed a hand on his chest, her voice begging him to stay. As always, she sounded genuine - but it had to be a trick. Everything in this damn castle was."
    show rowan necklace neutral at midright with dissolve
    "But if it wasn’t… Maybe there was no harm in just listening."
    menu:
        "Hear her out.":
            $ released_fix_rollback()
            jump xzaratlIdea
            
        "Leave.":
            $ released_fix_rollback()
            ro "I said I don’t have time. Don’t bother me with this again."
            hide rowan with moveoutright
            "He pushed past her, leaving the troubled succubus behind. Even if he could trust her, there were no words that would help. And no time to waste on them."
            return


label xzaratlIdea:

show rowan necklace neutral at midleft with moveinright
show xzaratl happy at midright with moveinright

"Her lips curled into a small smile as she saw him nod his head. They were alone in the castle corridor, but she still chose to lead him aside. "

xz "You are a just man, Rowan. And a just man cannot stand to see evil go unpunished, even if it is done by his own hands."

show rowan necklace concerned at midleft with dissolve

ro "Unless Solansia finally decides to smite me as I stand, I’m afraid it will. "

xz "Not necessarily."

show rowan necklace shock at midleft with dissolve

"X’zaratl reached under her robes, and Rowan saw her take out a thin, black rope, two meters long."

show rowan necklace neutral at midleft with dissolve

xz "Rowan, I can see you are near your breaking point. And I know your mind and body will not rest until you rid yourself of this guilt."

"She ran her hands over it, and it changed shape, thinning at one end, and thickening at the other.  "

xz "In that regard, you remind me of Albin the Penitent. Torn between duty and compassion, {i}his{/i} restless soul sought relief in the suffering of the flesh."

show rowan necklace shock at midleft with dissolve

"His mouth grew dry as he saw the item take shape. A black whip now laid in X’zaratl’s hand.  "

xz "Gallant Rowan, if your heart cries justice for the black deeds done by your own hand… If it’s punishment you seek…"
xz "It can be arranged."

"Her voice lowered to a gentle whisper. Was she really planning to-"

menu:
    "Agree. You want her to whip you.":
        $ released_fix_rollback()
        $ xzaratlWhip = True
        show rowan necklace aroused at midleft with dissolve
        show xzaratl shocked at midright with dissolve
        ro "… If it’s you X’zaratl… I wouldn’t mind."
        if RowanXzaratlInfluence < 3: 
            "He wanted to keep her at arm’s length, but at that very moment, the prospect of relief eclipsed all else." 
            "Meanwhile, X’zaratl’s lone eye widened in surprise, and for a moment, she didn’t know where to place it, blushing red."
        else:
            "X’zaratl’s lone eye widened in surprise, and for a moment, she didn’t know where to place it, blushing red."
        show rowan necklace shock at midleft with dissolve
        xz "Rowan, ah, that’s… Mmm…. Aha, ha… I mean."
        ro "X’zaratl?"
        show rowan necklace concerned at midleft with dissolve
        show xzaratl neutral at midright with dissolve
        xz "Rowan, I’m flattered but… I cannot agree."
        xz "Ah, not because I don’t want to! Gods, to the contrary - you are dear to me, and I would love nothing more than for you to accept such absolution from my own hands."
        show rowan necklace neutral at midleft with dissolve
        xz "But it is too soon for us. Not when your heart is so heavy with sin. If it is to work, it must be done by the one who is closest to you. By the one who knows you most."
        
    "Out of question.":
        $ released_fix_rollback()
        $ xzaratlWhip = False
        show rowan necklace angry at midleft with dissolve
        ro "If you think I’ll let you whip me, you are out of your damn mind."
        show xzaratl neutral at midright with dissolve
        xz "No, I do not. You are dear to me Rowan, and I will grant you whatever help I can, whenever I can. But I know I am not the right person for this. Not when your heart is so heavy with sin."
        show rowan necklace neutral at midleft with dissolve
        xz "If you are to accept such absolution, it must be done by the one who is closest to you. By the one who knows you most."


ro "…. Alexia."

xz "Yes. Rowan, the task ahead of you is a thousand times more difficult than slaying the Demon Lord. But just as before - you are not alone. "

#xzaratl eye flash gold
show rowan necklace aroused at midleft with dissolve

xz "Have faith in the woman you chose to be your wife. Let her stand by your side. Let her help you carry this burden in your heart! Trust in her!"

#xzaratl concerned
show rowan necklace concerned at midleft with dissolve

xz "I beg you. You are one of the strongest people I have ever met. But do not try to shoulder all of this by yourself. Please.  "

"She touched his arm, rubbing it gently, and he felt himself at loss of words. When he answered her, all he could manage was an embarrassed whisper."

ro "I’m supposed to save her. Not the other way around."

xz "You can save each other, gallant Rowan, there is no shame in that. Let her help you relieve this pain. Let her be the kind hand that delivers just punishment."

show rowan necklace neutral at midleft with dissolve

ro "She has never-"

show xzaratl happy at midright with dissolve

xz "I will be by her side, Rowan. I will help her through this, I promise."
xz "Please, Rowan. It will bring you closer."

label xzaratlIdeaMenu:

menu:
    "It should be X’zaratl. You want it to be her." if xzaratlWhip == True:
        $ released_fix_rollback()
        $ RowanXzaratlInfluence += 1
        $ xzaratlWhip = False
        ro "X’zaratl, the things I’ve done… Alexia doesn’t know half of it. And I don’t want to burden her with that knowledge."
        xz "You are already burdened by it. And a heavy load like this ought to be carried by two."
        show xzaratl shocked at midright with dissolve
        ro "Then why shouldn’t it be you? "
        if RowanXzaratlInfluence < 3: 
            "It felt wrong, to ask her, of all people. But he strayed from the light so much already, that maybe such a desperate choice was exactly what was needed."
        show rowan necklace happy at midleft with dissolve
        ro "Isn’t it demons who are supposed to deliver punishment to the wicked?"
        xz "I believe that’s, ah, more of a children’s tale- "
        hide rowan
        show rowan necklace happy at midleft with dissolve
        show rowan necklace happy at midright with moveoutright
        hide xzaratl
        show xzaratl aroused at midright with dissolve
        show xzaratl aroused at edgeright with moveoutright
        "He pushed on, pressing her against the wall. The demoness blushed like a courted virgin, fiddling with the whip in her hands."
        show rowan necklace neutral at midright with dissolve
        ro "Yet I have a suspicion you are no stranger to the whip. You must be more experienced with it than Alexia. And I feel like… You understand better the things I must do - and the consequences of them."
        xz "Rowan, I-"
        ro "You were right, I do need this. But I’d be more comfortable if it was you, X’zaratl."
        ro "Please."
        "This time, it was her who was at a loss for words. Her lips quivered, so close to his own-"
        menu:
            "Kiss her.":
                $ released_fix_rollback()
                $ RowanXzaratlInfluence += 1
                show rowan necklace aroused at midright with dissolve
                "Their cherry color drew him in, and he could no longer stop himself - he pulled her in, his lips seeking hers in a ravenous, needy kiss."
                xz "Mmm-! Mmmm-mmmm…."
                "She wriggled in his arms, her own flailing as she tried to gather her wits. And a moment later - she returned the kiss with twice the passion, her tongue invading his mouth, exploring it without restraint."
                xz "Mmm-!"
                "She shuddered, and Rowan felt a familiar, musky scent hit his nostrils. He pulled away -"
                show rowan necklace shock at midright with dissolve
                "And saw the stain at front of her loincloth, saw droplets of white dripping to the floor, from between her legs."
                "The demoness giggled nervously, and ran her hands over her dress, trying to restore it to some degree of modesty. To no avail."
                show rowan necklace happy at midright with dissolve
                xz "Oh Rowan~~ I apologise, just the thought~~~ Yes, Kharos take me, {b}yes{/b}, always. Whatever you ask of me I will do. I will make you experience things you never dreamt of."
                "She leaned in to kiss his cheek - it felt like a promise being made."
                
            "Let her answer.":
                $ released_fix_rollback()
                show rowan necklace aroused at midright with dissolve
                "-and turned into a wide smile. X’zaratl giggled nervously, then leaned in to kiss his cheek. It felt like a promise being made." 
                xz "Oh Rowan~~ Yes, of course. Whatever you ask of me, I will do. I will make you experience things you never dreamt of."
                
        show rowan necklace neutral at midleft with moveinright
        show xzaratl neutral at midright with moveinright
        xz "But gallant Rowan, that will take time to set up. And… It would make me feel guilty, if I did not grant Alexia the privilege first."
        xz "So please - let us propose the idea to her today. You need this, Rowan."
        $ xzaratlWhippingPromise = True
        jump xzaratlIdeaMenu
        
    "Let her propose the idea to Alexia.":
        $ released_fix_rollback()
        $ RowanXzaratlInfluence += 1
        ro "Maybe it’s worth trying… But only if she’s comfortable with the idea."
        "X’zaratl caressed his cheek gently, as if to soothe his worries. The whip disappeared from view, and she took his hand as they headed for his room."
        xz "Do not worry, gallant Rowan. It’s for the good of both of you."
        scene black with fade
        show xzaratl happy behind black
        xz "I’m sure she will see it too."
        
    "Refuse.":
        $ released_fix_rollback()
        if xzaratlWhippingPromise == True:
            $ RowanXzaratlInfluence += 1
            ro "I meant what I said. I want it to be you."
            show xzaratl aroused at midright with dissolve
            "The demoness bit her lip, blushing even further."
            xz "Ah, if you persued Alexia with the same tenacity~~"
            xz "Very well, if that is what you desire. Stay strong, my gallant hero. I’ll start making the right preparations for later."
            scene black with fade
            "She kissed him yet again, and hid the whip. He returned to his duties - and for once, he thought not of the thing’s he’s done, but of the days to come."
            $ change_base_stat('g', -10)
            return
        else:
            #xzaratl concerned
            ro "I’m not going to bring Alexia into this. She’s been held here for far too long, and I know she does her best to stay strong despite it all. The method aside, I cannot ask her to deal with my problems as well."
            xz "That is very noble of you Rowan. Yet I fear you will take too much on your shoulders, and break under the weight of it all."
            ro "If Karst didn’t break me, then neither will this."
            scene black with fade
            "She didn’t look convinced, but he was under no obligation to explain himself. He told her to hide the whip, then returned to his duties."
            return

scene bg9 with fade
show xzaratl happy at edgeleft with dissolve
show rowan necklace happy at midleft with dissolve
show alexia white neutral at midright with dissolve

$ alexiaWhipRowan = True

if AlexiaXzaratlInfluence > 2:
    "Alexia looked up from the book she held in her fingers, and watched Rowan and X’zaratl as they entered the room."
    al "X’zaratl, good to see you. Is something the matter, Rowan?"
    ro "Yes, in a way. And X’zaratl offered to help. Please, hear her out."
    #show alexia white shocked at midright with dissolve
    
else:
    "Alexa froze, fingers tense on the book in her hands when Rowan and X'zaratl entered her room."
    #show alexia white shocked at midright with dissolve
    ro "Relax, dear. She is here on my invitation." 
    al "I- I don't understand. I thought you said… "
    ro "I know. But please, hear her out."

show xzaratl happy at edgeright with moveoutright

"He turned his back to her, and began to remove his armour. Still not understanding, she didn’t realize when X’zaratl manoeuvred herself behind her, her gentle hands holding her shoulders as she leaned in to whisper in her ear."

show alexia white neutral at midright with dissolve

xz "Sweet Alexia, you’ve seen it too, have you now? The dark clouds hanging over your husband’s head. The things he must do - they are not always noble deeds."

show alexia white concerned at midright with dissolve

"The succubus took the book out of her hands, still whispering about her husband - telling her of his sins, and the guilt that plagued his heart. Much of it, she already knew - she was not blind - but what {i}could{/i} she do, when he kept to himself more often than not?" 

xz "… If he is to find peace again… - He must be punished."

#show alexia white shocked at midright with dissolve

"Something was placed in her hand. She looked down."

xz "And it must be done by your hand, and no other."

#show alexia white aroused at midright with dissolve

"She saw the black whip in her hands - and the whole world lost focus." 
"She was aware, just barely, of the things happening around her. Of her husband, stripping. Of X’zaratl, whispering and touching her. But it all seemed to come to her as if from behind a thick fog." 
"It was all so sudden, but the way X’zaratl painted it - a chance to bring relief to her husband, to draw closer to him -" 

show bg9 with sshake
#show alexia white shocked at midright with dissolve

"Her hand moved - and the whip struck the air with a loud crackle. She drew a sharp breath, once more realizing where she was. The room came into focus again, and she saw both sets of eyes looking at her expectantly."

show alexia white concerned at midright with dissolve

al "It’s - it’s magical, isn’t it?"

xz "Yes, just a little. So it does no true harm even when passion overtakes the user."

show rowan necklace naked concerned at midleft with dissolve

"She wondered how true that was. She looked to her husband - now standing before her naked. He looked so vulnerable - not just for the lack of clothes."

al "… Is this really what you want?  "

show rowan necklace naked neutral at midleft with dissolve

ro "It is."

"And he sounded so sincere - his voice was almost pleading! She stroked the whip in her hands - and found another pair placed over hers. She looked to the demoness, who smiled at her reassuringly."

xz "I’ll be by your side at all times. I promise."

if all_actors["alexia"].relation < 31 or rowan_shares_room_with_helayna:
    $ whipAlexiaMood = "angry"
    
elif tempWhip > 0:
    $ whipAlexiaMood = "skilled"

else:
    $ whipAlexiaMood = ""

menu:
    "Let X’zaratl guide you." if all_actors['alexia'].corruption < 31:
        $ released_fix_rollback()
        $ AlexiaXzaratlInfluence += 1
        #show alexia white aroused at midright with dissolve
        al "(Cessair, have mercy on me.)"
        "She had no choice but to trust in him, and in the demoness. She gripped the whip tightly, and raised her chin, trying to appear commanding."
        al "Kneel, my husband."
        scene cg117 with fade
        show xzaratl happy behind cg117
        pause 2
        "Rowan did as ordered, looking almost relieved. Already he felt a certain lightness - surrendering his body, readying himself for a punishment he so clearly required..."
        xz "An excellent start, sweet Alexia. Now, raise your hand"
        "The succubus grabbed her left hand, intertwining their fingers, as the right one helped her lift the whip. Alexia swallowed heavily, unsure of her own feelings. But there was no turning back."
        scene cg118 with sshake
        pause 3
        #aroused
        show alexia white neutral behind cg118
        show xzaratl happy behind cg118
        show rowan necklace naked aroused behind cg118
        "The whip cracked, evoking a quiet yelp from her husband. She gasped as well, as she felt the force of her blow - it traveled up her arm, making her own body shudder."
        xz "Ask him what he wants. And know his answer is true."
        "She watched the bright red mark on his ass, and licked her parched lips. The demoness fingers roamed her body, teasing her through her clothes, slipping under them at every moment. With her attention focused on Rowan alone, she almost didn’t notice them."
        al "Rowan. Tell me again. What do you want me to do?"
        ro "… Please, punish me for my sins. Whip me, my love."
        show cg117 with sshake
        "Her hand struck a second time before she even realized what she was doing. It felt like a spell was cast on her - the whip no longer felt alien in her hands, and the sight of Rowan on his knees no longer evoked any sympathy."
        
    "X’zaratl was right - Rowan deserved punishment. Also for the things he’s done to you." if whipAlexiaMood == "angry":
        $ released_fix_rollback()
        #show alexia white angry at midright with dissolve
        al "… If that is what you need of me."
        "She was surprised at how cold her voice was. She shouldn’t be - her husband {b}did{/b} have a lot of atoning to do - to her as well. She’d grant him the penance he so desperately desired." 
        al "Kneel."
        scene cg117 with fade
        pause 2
        "Rowan did as ordered, looking almost relieved. Already he felt a certain lightness - surrendering his body, readying himself for a punishment he so clearly required..."
        scene cg118 with sshake
        pause 3
        #angry
        show alexia white neutral behind cg118
        show xzaratl happy behind cg118
        show rowan necklace naked aroused behind cg118
        "The whip cracked without any warning, evoking a quiet yelp from him. Alexia smiled as she felt the force of her blow - it traveled up her arm, making her own body shudder."
        "She thought he felt X’zaratl tense from surprise - but only for a moment."
        xz "Well done, Alexia. Now ask him what he wants. And know his answer is true."
        "She watched the bright red mark on his ass, and licked her parched lips. The demoness fingers roamed her body again, teasing her through her clothes, slipping under them at every moment. She paid them no mind, focused entirely on Rowan."
        al "Tell me again, husband. What do you want me to do?"
        ro "… Please, punish me for my sins. Whip me, my-"
        show cg117 with sshake
        "Her hand struck again before he could finish, adding another red mark alongside the first."
        "It felt like a spell was cast on her - the whip no longer felt alien in her hands, and the sight of Rowan on his knees no longer evoked even the slightest sympathy. If anything, her love now looked like a juicy target for all that anger boiling inside of her."
        
    "You don’t need X’zaratl… But you can’t ask her to leave now." if whipAlexiaMood == "skilled" or all_actors['alexia'].corruption > 30:
        $ released_fix_rollback()
        if whipAlexiaMood == "skilled":
            show alexia white neutral at midright with dissolve
            "The demoness was far too close for her liking. She didn’t need her - she knew how to handle a whip. But she couldn’t ask her to leave, not when Rowan invited her. "
        else:
            show alexia white neutral at midright with dissolve
            "The demoness was far too close for her liking. She didn’t need her - the whip didn’t scare her, even if she didn’t know how to use it. But she couldn’t ask her to leave, not when Rowan invited her."
        show alexia white happy at midright with dissolve 
        "She vowed not to let X’zaratl distract her, and focused on the task at hand. She gripped the whip tightly, and raised her chin, a shadow of a smile dancing on her lips."
        jump whipDontNeed
       
    "You don’t need X’zaratl… But her body feels nice next to yours..." if whipAlexiaMood == "skilled" or all_actors['alexia'].corruption > 30:
        $ released_fix_rollback()
        $ AlexiaXzaratlInfluence += 1
        #show alexia white aroused at midright with dissolve
        "Her attention should be on Rowan alone, but she couldn’t ignore the demoness’ presence around her - it was like a warm blanket over her shoulders, soft and comforting."
        if whipAlexiaMood == "skilled":
            "Oh, she didn’t need her here, she knew how to handle a whip. But why should she deny herself the company - especially when such an ungrateful task was thrust upon her?"
        else:
            "Oh, she didn’t need her here - she was not afraid of a whip, even if she didn’t know how to use one. But why should she deny herself the company - especially when such an ungrateful task was thrust upon her?"
        "She gripped the whip tightly, and raised her chin, feeling a smile creep onto her lips."
        label whipDontNeed:
        al "Kneel, my husband."
        scene cg117 with fade
        #aroused
        show alexia white neutral behind cg117
        pause 2
        "Rowan did as ordered, looking almost relieved. Already he felt a certain lightness - surrendering his body, readying himself for a punishment he so clearly required."
        al "Since you want this so much… Ready yourself."
        scene cg118 with sshake
        pause 3
        #aroused
        show alexia white neutral behind cg118
        show xzaratl happy behind cg118
        show rowan necklace naked aroused behind cg118
        "The whip soared through the air and hit her husband with a loud crack, evoking a quiet yelp from him. She felt the force of her blow - it traveled up her arm, making her own body shudder. Her grin widened."
        xz "Well done, Alexia. Now ask him what he wants. And know his answer is true."
        al "Oh, I know."
        "She watched the bright red mark on his ass, and licked her parched lips. The demoness fingers roamed her body again, teasing her through her clothes, slipping under them at every moment. She paid them no mind, focused entirely on Rowan."
        al "Rowan, dearest, tell me again. What do you want me to do?"
        ro "… Please, punish me for my sins. Whip me, my love."
        show cg117 with sshake
        if whipAlexiaMood == "skilled":
            "Her hand struck again, adding another red mark alongside the first. The whip felt so natural in her hands now - like she wielded it all her life."
        else:
            "Her hand struck again, adding another red mark alongside the first. Already, the whip felt so familiar in her hand, as if she wielded it all her life."
            
    "Throw that thing aside. This was no solution.":
        $ released_fix_rollback()
        $ AlexiaXzaratlInfluence -= 1
        #shocked
        show rowan necklace naked concerned at edgeleft with moveoutleft
        show xzaratl concerned at center with moveinright
        #angry
        show alexia white neutral at edgeright with moveoutright
        "She pushed the demoness away, shoving the whip back in her hands."
        show rowan necklace naked concerned at edgeleft with dissolve
        al "I have no idea how you managed to talk my husband into - whatever this is supposed to be, but that’s not how we do things."
        xz "Alexia, he needs-"
        al "With all due respect, X’zaratl, I think I know better what my husband needs."
        "She glared at the impertinent demon - and X’zaratl looked away. Rowan did too, though she did not understand why."
        al "You should leave."
        xz "Of course. I apologise."
        if xzaratlWhippingPromise == True:
            ro "I warned you."
            xz "She just needs more time, Rowan."
            hide xzaratl with moveoutright
            show alexia white concerned at midright with moveinright
            "He didn’t seem convinced. Rowan reached for his clothes, and started dressing again. And even though Alexia tried to have him explain what this was all about, her husband wouldn’t budge."
        else:
            hide xzaratl with moveoutright
            show alexia white concerned at midright with moveinright
            "X’zaratl left the room, casting the two of them a longing room. Her husband sighed, and started dressing again."
            al "Rowan… What’s going on? For you to want to try something-"
            ro "I don’t want to talk about it."
        scene black with fade
        "In the end, he left the room feeling even worse than before."
        $ change_relation('alexia', -5)
        return

xz "You’re doing great, Alexia. Your husband knows he’s done wrong. So many sinful deeds… Their weight so great, he can no longer even stand before you. "
xz "Do you know what that makes him?"

al "… A bad boy. "

"She drew a sharp breath, and smiled wickedly. She delivered yet another powerful strike with her whip, and evoked yet another beautiful yelp."

xz "Yes, a wicked, bad boy.  That is why he is on his knees before you - to receive just punishment for his failings, from the one person he can trust to only spare the lash once he has been truly forgiven. "

"She struck a fourth time, and again Rowan couldn’t stop himself from letting out a shameful cry. He didn’t try to stop them. For so long, he tried so hard to be strong. He couldn’t anymore."

if avatar.corruption < 31:
    "Every misdeed, every sin, like a black spot on his soul. He tried to ignore them. Tried to power on through determination alone. It worked, really did. For a time."  
    "But now every strike brought back memories, forcing him to relive every bad decision he’s made since accepting Jezera’s offer."

else:
    "Every misdeed, every sin, like a black spot on his soul. For each, there was a reason - a justification, of sorts. Some good, some less so. Excuses, all of them. He could no longer lie to himself." 
    "Now every strike brought back memories, forcing him to relive every bad decision, and accept them for the atrocities that they were."

"His body ached, his wounds hurt, and he could almost feel Alexia’s gaze on his skin. He felt himself tremble - and not just from the pain. Just as X’zaratl said, there was liberation, in accepting punishment. A sweet release from sin." 
"And he felt himself grow hard from it."

ro "Ah!"

"The whip struck for the fifth time, and this time his cry wasn’t driven by pain alone. The excoriating sensation of atonement consumed all. Panting with desire, he hung his head low, and waited for the whip to strike yet again."  
"… Alexia watched her husband tremble, wondering if all that blood rushing to her head made her hear things. Did he just…? "

xz "Do not blame him, sweet Alexia. The whip purifies all, and as his heart grows lighter, the needs of the flesh make themselves known again. "

"She didn’t do this for his enjoyment! And yet…"

xz "It’s thanks to you that he can feel pleasure again. It’s thanks to you that he can be happy again. It is all because he knows he can place his body and soul in your hands."
xz "He might be a hero. He might be a saviour. But when it’s just the three of us… He could also be someone else entirely."

"X’zaratl’s fingers stroked her still, then slowly made their way up. One was placed on her back - and pushed her ever so gently, urging her to take a step forward. "

xz "Take a closer look, Alexia. See for yourself."
xz "Witness the result of your efforts."

menu:
    "Stay where you are - you aren’t doing this for your enjoyment either.":
        $ released_fix_rollback()
        "She clenched her teeth, trying to fight back the burning desire that threatened to overtake her. Even if Rowan enjoyed it a little too much… Even if she did too- she should remember what this was all about." 
        "She didn’t move. Sensing her hesitation, X’zaratl nodded slowly, then brought her lips to Alexia’s neck, kissing her gently."
        xz "I understand… This is a very delicate moment for both of you. Take your time, sweet Alexia."
        "The warmth of her lips felt amazing, tempting her to sink into the demoness arms. But she made her decision."
        "Steeling herself, Alexia raised her hand again."
        
    "Witness his submission.":
        #new CG
        scene black with fade
        $ whipAlexiaFantasy = True
        $ alexiaWhippingEnjoyment = True
        $ AlexiaXzaratlInfluence += 1
        $ change_corruption_actor('alexia', +5)
        "… It was only a moment, but it seared itself in her mind." 
        "Standing there, whip in hand, clothes in disarray, her body burning with desire, and her husband kneeling before her. A perfect moment, captured in time." 
        "In that very moment, nothing else mattered. Not the castle, not the amulet at her neck, and not even the damned war to conquer the six realms. It was just her, her husband, and X’zaratl’s whip in her hand." 
        "… And X’zaratl herself. The succubus was still behind her, waiting, slowly stroking her own cock. If she wanted to, could ask - she could order! -  and the demoness would slip it between her legs without any hesitation." 
        "Or she could have her fall to her knees and make her eat her out. Or she could ask Rowan to do it. Or ask him to fuck her. Or her to fuck him. Either or both, one after another - or even at the same time." 
        "Whatever she wanted, would be granted to her. As long as she held the whip…" 
        "She stroked it, smiling. Sensing her excitement, X’zaratl hugged her again." 
        scene cg117 with fade
        #aroused
        show alexia white neutral behind cg117
        show xzaratl happy behind cg117
        show rowan necklace naked aroused behind cg117
        pause 2
        xz "So much still awaits you. All you need to do is trust yourself, and trust in your husband."
        "Alexia grinned. She couldn’t agree more."
        "With a flair, she raised her hand again-"

"...For Rowan, the wait for the sixth strike was agonizing, but when it finally came, it brought more ecstasy than pain."

ro "A-ah! "

"His aching cock begged for attention, but he feared reaching for it, feared even asking for permission to attend to it."

xz "Ah, Rowan… I think he’s at his limit."

if whipAlexiaFantasy == True and whipAlexiaMood == "angry":
    al "Mmm…. I suppose...  Though I think I’d like to whip him some more~~~"
    xz "Later, lovely Alexia. For now… Let him taste release."

elif whipAlexiaMood == "angry":
    al "Is he though…I wonder…"
    xz "I believe so. We can repeat it again later, if you want to, lovely Alexia. For now… Let him taste release."
    
else:
    if whipAlexiaFantasy == True:
        al "Mmmm… I suppose…"
        xz "I think he earned his release… Hasn’t he?"
        al "Ah…. Since he’s been so obedient…"
    else:
        al "… Yes, agreed."
        
"Rowan couldn’t see it, but a surge of purple magic traveled down X’zaratl’s arm, seeping into the whip. Alexia raised her arm again, and flung it for the seventh time-"

scene white with flash
pause 1
scene black with fade
show rowan necklace naked aroused behind black
show xzaratl happy behind black

"His body exploded with pain and pleasure, and the cry died on his lips as his cock was overtaken with ecstasy, painting the floor white. All thoughts of his past misdeeds left his mind - all thoughts did, leaving only this amazing sensation that didn’t seem to end. "

if RowanXzaratlInfluence > 9 and all_actors["alexia"].relation > 50:
    "He knelt there for what seemed like eternity. At some point, a pair of hands helped him stand - and then enveloped him as he found himself embraced by the two most important women in his life."
    
else:
    "He knelt there for what seemed like eternity. At some point, a pair of hands helped him stand - and then enveloped him as he found himself embraced by both his wife and X’zaratl."
    
xz "It is done."

scene cg313 with fade
show alexia necklace happy behind cg313
show rowan necklace naked behind cg313
show xzaratl happy behind cg313
pause 3

"He let a sigh of relief, and leaned on them both. He felt weak, and he would be moving tenderly for a while - but the absolution of his guilt by way of the masochistic ritual more than made up for it."  
"Seeing his tired expression, Alexia’s lips made a thin line, and she ran her hands across the burning ridges that ran right down his back and ass." 
"Was it really her who had put them there? It seemed impossible... but her heart leapt as the memory of the {i}thrill{/i}, the release... "

if whipAlexiaFantasy == True:
    al "Ah… Incredible… "
    xz "It is. Thank you wife for this, Rowan. Thank your wife for punishing you."

else:
    "She buried her head into Rowan's chest to escape dotting the 'i's and crossing the 't's of those exciting thoughts."
    xz "Rowan. Thank your wife for punishing you."

ro "Th-thank you, Alexia."

"She smiled. It felt inescapably warm and wonderful to be hugged by his whipper, the rightful end to this painful yet incredibly gratifying experience." 
"And for the longest of time, neither of them pulled away. "

$ change_base_stat('c', 10)
$ change_corruption_actor('alexia', +10)
$ change_base_stat('g', -15)
#Damage: Normal (body bruises) - TODO
$ alexiaWhippedRowan = True
$ RowanXzaratlInfluence += 1
$ AlexiaXzaratlInfluence += 1
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label andras_chanllenge:
#Andras' Challenge
#Requires: Arena built, at least 15 orcs

$ released_block_rollback()
scene black with fade
show rowan necklace neutral behind black
show andras happy behind black

"Near to the muffled roar and hubbub of the castle's arena, Rowan ran into Andras."
"The male demon was leaning against a wall with an air of casualness, but it was obvious that he had been waiting specifically for the human to happen along, most notably by the malicious grin that spread across his face when he saw him coming."

an "Rowan! Has the Lord Commander come to review the arena?"

ro "Not specifically."

an "Let's put in a visit, shall we? There's a big fight on now, and it will do the troops good to see us both taking it in."

"Rowan knew it would be pointless to argue. He nodded and allowed the demon to steer him towards the small coliseum."

scene bg29 with fade
show rowan necklace neutral at midleft with dissolve
show andras smirk at midright with dissolve

"Inside the thronged arena, soldiers quickly made space so that Andras and Rowan had prime seats, halfway up a terrace near the centre. On the sand below, two helmeted orc gladiators clashed furiously with sword and shield."
"The mob roared and oohed each time a blow found its mark; around him, Rowan saw tokens exchanging hands, beer being swilled and other would-be competitors readying themselves."

an "You can see why this is popular, eh Rowan? Even a milquetoast human such as yourself can appreciate the rush and glory of one-on-one combat!"

"Several orcs nearby sniggered, throwing sidelong gazes at Rowan. His skin crawled as Andras raised his voice."

an "But not to worry. You're safely ensconced up here - as my little pet. You wouldn't last five seconds in the ring, and nobody would expect you to. Your talents run elsewhere, after all..."

#if Rowan has had sex with andras
if andrasIntroSex:
    "With a vindictive quirk of the lip, the demon leant back and slid his hand meaningfully down his abdomen, tracing the outline of his hardening cock."
#else
else:
    an "Studying books, being at the beck and call of my sister, that's more your thing!"

#remerge

"The crowd of orcs surrounding them guffawed, turning delighted eyes back to Rowan for the response."

menu:
    "Rise to the challenge.":
        $ released_fix_rollback()
        ro "You're pathetic. I could best any one of these orcs in combat, and you know it."
        an "Prove it!"
        "Down below, the fight came to an end - the bigger orc smashed his opponent's blade out of his hand, and the latter quickly yielded, knee on sand. The crowd roared their approval, getting even more raucous when Andras himself strode out and thrust the winner's hand to the sky."
        scene black with fade
        show andras smirk behind black
        an "And now, my dogs of war, my blood-drunk sons and daughters: a special treat. Our very own commander, Lord Rowan himself, will now step into the arena to take on your champion!"
        "By the time Rowan had stripped down to the waist, taken up helmet, blunted sword and shield and was striding into the arena, the murmuring around the terraces had built into a full-throated roar of excitement."
        scene bg28 with fade
        show rowan necklace neutral at midleft with dissolve
        "He could feel it vibrating through the sand as he took up stance opposite his opponent; all of the orcs, predictably, were bellowing the name of their champion. The big, sweat-streaked orc gave him a big, unfriendly grin."
        show wild orc neutral at midright with dissolve
        wo "I can't believe you agreed to this, hoo-man. I will crush you, and once I do, I will be Warlord!"

        #combat check dc 15
        # TODO change when combat will be defined
        #fail
        if not dice(20) > 15:
            "The sound of steel clanging and barking against itself punctuated the crowd's throbbing roar, Rowan and the orc stepping backward and forward across the muddled sand, blocking, feinting and parrying furiously."
            "At first Rowan thought he had the advantage - he forced the big greenskin back numerous times with his quicker blows - but his opponent had seemingly limitless endurance, and Rowan's limbs began to ache as the battle dragged on."
            "The orc suddenly stepped in behind Rowan's failing guard and smashed the pommel of his sword into his face. Nose bloodied and pain ringing in his ears, Rowan fell to the ground. Cheers and jeers spiralled to the spin of the sky above."
            show andras happy behind bg28
            an "Enough! Well fought, champion, you retain your belt. You and yours should be proud this day."
            wo "Pshaw! Retain my belt? His crown should be mine! Why do we take orders from this weakling anyway?"
            an "Because we are conquering a human world, not an orcish one. He is useful to us in ways you will never be. Revel in your victory today, but always remember that."
            "The Orc snorted in contempt at Rowan, before lifting both of his trunk-like arms to the crowd, who howled their approval at him."
            "With the receding of pain came the burn of humiliation, but Rowan knew better than to scurry away; he lifted his head, applauded the tusked warrior, and then walked away with his head held high."
            hide wild orc with moveoutright
            show andras smirk behind black
            an "You are braver than I thought - and more foolish, human. Brawling with orcs! At least you entertained them. And me."
            ro "Please do shut up and leave me alone."
            "The sadistic demon slapped him on the shoulder merrily."
            an "Get that nose of yours looked at, at least. You'll have to come up with some way of redeeming yourself, you know. The orcs won't forget you getting your ass handed to you easily."
            #gain 10 xp, a wound, and lose morale
            $ add_exp(10)
            $ take_damage(1)
            $ change_morale(-5)
            return
        #pass
        else:
            "The clang and shriek of steel punctuated the crowd's throbbing roar, Rowan and the orc circling backwards and forwards across the muddled sand, blocking, feinting and parrying furiously."
            "The big brute fought ferociously, with what seemed like limitless endurance, but Rowan was by far the more skilful and level-headed swordsman."
            "He allowed the orc to waste his huge haymakers on thin air whilst stinging him again and again with telling drives of his blade, until the orc's chest was heaving and creaking with exhaustion."
            wo "Stand... still!"
            ro "If you insist."
            "He stopped circling suddenly and stepped in, smashing his opponent with the blunt edge of his sword hard enough to send a bloody tusk flying. The orc collapsed to the deck, weapon falling out of his hand."
            "The crowd fell quiet, watching dumbstruck as Andras strode back out, grasped Rowan's wrist, and thrust it to the side."
            show andras happy behind bg28
            an "Your victor, your commander - Lord Rowan!"
            "A hushed murmur shuffled around the terraces, before growing slowly into a clamor. After a few seconds, all present were bellowing two syllables."
            cro "Ro-wan! Ro-wan! RO-WAN!"
            scene bg14 with fade
            show rowan necklace neutral at midleft with dissolve
            show andras happy at midright with dissolve
            an "Well fought, champion. I must admit that I didn't think you would be brave enough to pick up the gauntlet."
            ro "You just hoped to humiliate me, then?"
            an "One way or another: our troops were entertained. This way though, you demonstrated their leader's strength and steel. You grabbed the situation and made it your own! I liked that."
            "He gave Rowan a lingering eye before swaggering off with a smirk, completely unabashed. The demon was right about one thing, though; Rowan heard chatter echo throughout the fortress about his famous victory in the arena for many days to come."
            #gain 25xp, morale, and andras' favour
            $ add_exp(25)
            $ change_morale(5)
            $ change_favor('andras', 1)
            return

    "Try and provoke him back into fighting in the arena instead.":
        $ released_fix_rollback()
        ro " Seems to me that the being that spends most of his time bragging about how mighty his race is should be the one to prove his mettle in the ring."
        ro "But nobody expects that of you, Andras. Your talents run towards bragging about the size of your dick and hanging around the castle doing precisely nothing."

        #diplomacy check dc12
        #fail
        if not check_skill(12, 'diplomacy')[0]:
            an "Hah! I knew you would try and weasel out of fighting somehow. Don't shiver in your socks about it, Rowan - as I said, nobody would expect a human to risk his soft, clean skin in honorable combat."
            an "You stick to what your people are good at. Weaselling."
            "The soldiers around them sniggered, but when Rowan didn't dignify Andras' words with a response they turned back to the action down on the sand."
            "The fight ended soon after, and the male demon headed down to thrust the victor's hand up to the sky. Rowan slipped away quietly in the exultant clamor."
            return
        #pass
        else:
            "The orcs surrounding them ooh'ed, the human and demon's verbal jousting tickling their limited minds in ways the battles could not. Andras's face darkened."
            an "You dare question MY prowess? I'll show you how a true warrior fights, worm!"
            "Down below, the fight came to an end - the bigger orc smashed his opponent's blade out of his hand, and the latter quickly yielded, knee on sand."
            scene bg28 with fade
            show andras displeased behind bg28
            show rowan necklace neutral behind bg28
            "The crowd roared their approval, getting even more raucous when Andras himself strode out and held the winner's hand up to the air."
            an "And now, my dogs of war, my blood-drunk sons and daughters: a special treat. Your leader, red knight Andras the Immolator, shall battle your champion!"
            an "No magic, sword vs sword - honorable combat, so you may be reminded why you would follow him unto hell's gates themselves!"
            "The murmuring around the terraces had built into a full-throated roar of excitement by the time he had finished, the crowd lapping up the bold demon's words."
            "Rowan could feel it vibrating through the stone as he watched Andras took up stance opposite the burly orc champion, foregoing armor but taking up the blunt sword and shield the previous contestant had used."
            "The orc surprised Rowan by lasting longer than he expected. He weathered several of Andras's blows and then got a good one in himself, slashing the demon across his chest and forcing him back with a startled bark."
            "After that though, the devil-may-care smirk dropped off Andras's face and he came at his opponent like a berserk hummingbird."
            "The lumbering orc was struck with vicious precision again and again, barely even able to bring his shield up before he was attacked from yet another angle."
            "When at last the big brute collapsed to the sand, holding his hand up for mercy, Andras smashed him across the face, knocking out a tusk and laying him out cold."
            "He turned to the terraces and raised his arms, chest heaving, drinking in the cheers that rained down."
            cro "AND-RAS! AND-RAS! AND-RAS!"
            an "What do you think about that, worm?"
            ro "Oh, you certainly showed me about how honorable combat should be fought, demon. Particularly the bit where you hit your opponent after he surrendered."
            "Andras sneered at Rowan, but drunk upon his own victory and the jostling knot of backslapping orcs around him, he went no further with it."
            "In retrospect, Rowan realised as he listened in on the conversation of his guards in the days to come, the incident at the arena had worked out well."
            "The garrison had been reminded not only of their demon leader's ruthlessness and battle prowess, but their human leader's slyness and way with words."
            "Their expectations had been met; their world view affirmed."
            #gain morale (less than gain from rowan winning in arena), 10xp
            $ add_exp(10)
            $ change_morale(3)
            return

    "Don't take the bait.":
        $ released_fix_rollback()
        ro "Whatever."
        "Andras tried needling Rowan a couple more times, but both he and the orcs around them grew bored when Rowan refused to respond, and their attention drifted back to the battle."
        "The incident was completely forgotten by the following day."
        return

    "Respond submissively.":
        $ released_fix_rollback()
        $ rowanAndrasSex =+ 1
        $ rowanGaySex += 1
        ro "You are right, sir. I am your pet."
        an "Hell-damned right."
        "He reached out and pulled Rowan into his brawny side, flagrantly groping the human's flank and chest."
        "Rowan felt himself grow hot underneath the contemptuous eyes of the surrounding soldiers; where the burn of humiliation ended and the helpless lust he felt underneath Andras's rough touch."
        "The decadence of demons and the spinelessness of humans affirmed, the orcs lost interest and turn their attention back to the battle."
        "Andras though grew more and more bold with his gropes and caresses, his lust to dominate utterly interchangeable from that he felt watching blood spill and blade clash below."
        scene cg129 with fade
        pause 2
        show cg130
        show andras smirk behind cg130
        pause 2
        "His livid gaze fixed on a particularly fierce and savage wrestling match, he snatched Rowan's hardening penis and began to jerk it hard, making the human gasp to the helpless arousal pulsing up his spine and tightening his balls."
        "Andras suddenly stood up and pushed Rowan out of his seat."
        an "The chambers below. Now."
        scene cg62 with fade
        show andras smirk behind cg62
        pause 2
        "The sound of the crowd and clang of sword against shield was muffled in the sandy cell where Rowan got on his knees, coiled his hand around the base and spread his lips over the musky head of Andras's thick erection."
        "Drunk on violence and Rowan's willing submission, Andras had no interest in formalities; he grabbed the human by the hair and roughly pumped his cock past his lips, utterly unheeding to the splutters and gulps this precipitated."
        an "Ungh... tighten up and suck it up, whore! I know you can, it's what you're good for... that's it!"
        "Rowan hollowed his cheeks around the exacting thrust of his master's bulging erection, earning himself a groan of approval and a tightening of the grip on his hair."
        "Andras worked his muscular hips, filling Rowan's mouth with hard, delicious meat again and again, practically using him as a masturbation toy to reach a delicious high."
        show cg62 with sshake
        show cg62 with sshake
        scene cg63 with flash
        show andras smirk behind cg63
        pause 2
        "Rowan's cheeks swelled with hot demon cum as Andras found release with an ecstatic gasp. He swallowed it down only to receive another mouthful, and another, and another."
        "At last Andras released his cruel grasp and withdrew his wilting member, drool and thick seed trailing after it. He even went as far as to stroke Rowan along the line of his jaw."
        an "A prime seat at the entertainment, crowned by fifteen luscious minutes with my pet cock-polisher. Ah, this is the life I was born to lead!"
        "Did Rowan think of the tyrannical demon as 'master' during all of that? He shuffled the thought away as hurriedly as he got back to his feet and strode away from the arena. He could not deny the tiny shiver of pleasure it gave him, though."
        #gain corruption, gain andras' favour
        $ change_base_stat('c', 2)
        $ change_favor('andras', 1)
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label orc_deserters:
#Orc Deserters
#Low morale event. Requires at least 15 orcs

show bg6 with fade
show rowan necklace neutral at midright with dissolve

"Lost in his own thoughts, Rowan was slightly startled by the burly sergeant striding into the throne room. He and two other soldiers frog-marched five orcs in chains in. The prisoners looked ragged and resentful."

show orc soldier neutral at midleft with moveinleft
show wild orc neutral at edgeleft with moveinleft

os "These vermin tried to run away whilst out on patrol! Took us a day and a half to track 'em down and drag 'em back here."

wo "There's nuthin but piss and misery in this y'ere place! Takin orders from a weakling yuman who's got shit all clue what he's doin. You can stuff it up your bung'ole!"

os "Silence, coward! What do you want doing with 'em, lord?"

"Rowan knew the mood in the barracks had been low recently, but he had not been aware that it had gotten this bad."

show andras smirk at edgeright with moveinright

an "If I were you, I'd have them executed."

ro "Oh. You're skulking around here, are you?"

an "Naturally. You need all the advice you can get. I'll give you it again: Execute them. Orcs respond to hard discipline and blood-displays. Turn a problem into a boon!"

menu:
    "Put them in the stockade for a week.":
        $ released_fix_rollback()
        ro "No. We need every healthy soldier we can get. Spare them, and stick them in the stockade on half rations for the week. When they come out they can show their gratitude by following every order to the letter from now on."
        os "As you say... sir."
        an "*snort* What a fool you are! Do you think you're running a cake shop here? If they didn't think you were a weakling before, they certainly will now!"
        "Andras was right - once word got around that Rowan had spared the lives of the deserters, the mood in the barracks turned downright mutinous."
        "Still, after the orcs were released they agreed to continue serving, and Rowan walked with his back a little straighter for not having resorted to brute displays of power."
        #Military Strength unchanged, Morale down, Corruption down
        $ change_morale(-5)
        $ change_base_stat('c', -2)
        return

    "Execute them.":
        $ released_fix_rollback()
        ro "Desertion cannot be tolerated. Take them to the yard, gather the garrison and have them executed."
        os "Right away, sir!"
        hide wild orc with moveoutleft
        hide orc soldier with moveoutleft
        an "Good man. There is nothing weak about listening to experience, you know."
        "Andras was right - the garrison watched the beheadings in stunned silence, but it was noticeable afterwards how the orcs went about their tasks and snapped to attention when Rowan approached with considerably more vim."
        "Still, the certain knowledge that the old hero of Rosaria would never have stooped to executing his own men to keep them in line plagued Rowan's mind."
        #Military Strength down, Morale up a lot, Corruption up
        $ castle.buildings['barracks'].troops -= 5
        $ change_morale(10)
        $ change_base_stat('c', 2)
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label alexia_visits_with_skordred:
#Alexia visits with Skordred
#No requirements, but will appear at some point during the second mission in the NPC slot eventually.

#workshop bg
scene bg14 with fade
show alexia 2 necklace happy at midleft with moveinleft

al "Hello? Anyone in here? I hope I'm not interrupting anything."

show skordred happy at cliohnaright with moveinright

"Alexia spotted the dwarf working on something at a workbench right after she spoke, but he was already in the process of setting down his work and approached her with a smile on his face."

sk "Is no problem, nothin urgent. I don believe we've been intradused. I am Skordred, master builder, at yar service."

al "Alexia Blackwell, uh, housewife. It's nice to meet you. My husband warned me you might be a bit rough around the edges...."

sk "If I'm nah mistaken, you're the honored guest of my masters."

al "It's not exactly by choice."

sk "A regrettable state of affairs.  I'm very sorry that one such as yarself was unfortunate enough to fall in love with a regicide. However, know that I donna blame ya far the actions of yar husband. Yar always welcome in my shop."

"He held out his hands and, after a moment's hesitation, Alexia placed one of hers in them. The dwarf kissed her hand through his beard and then released it."

sk "Naw, tell me what brings ya here today?"

al "I was hoping you could tell me a bit about this castle, I really don't know anything about this place and it looks like I'll be calling it home for the foreseeable future."

sk "Is no problem at all.  If I may be permitted a moment of pride, I would call Bloodmeen my greatest creation."
sk "The castle is a sorry sight now, but just imagine what it looked like when the mortar was fresh and master Karnas was marching through the gate far the first time."

"The man was lost in memory for a moment before continuing."

sk "Bloodmeen actually refers to an entire series of castles, each serving as the seat of power for Kharos's holy vessel. My order of master builders exists to make certain that a proper fortress from which to liberate the world awaits each of them."
sk "Would you like to know the histories of the previous castles or thar lords?"

al "That's okay. Thank you for your help, master builder, it was very interesting hearing about the castle."

sk "It was my pleasure. Have a enjoyable day Alexia."

hide alexia with moveoutleft
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label rowan_is_feeling_guilty:
#Rowan is feeling guilty
#Requires Rowan have enough guilt to trigger low guilt after decay.  High priority event.  Note that conquering Raeve Keep should give enough guilt on its own to trigger this event.

scene bg4 with fade

"There were screams, blood flew in the air, figures pointed, and someone laughed."
"Rowan was walking forward, towards someone unarmed who begged for him to stop, to leave them alone."
"Then he raised his hand, a hand holding a sword, and brought it down on the defenseless person! Somehow now he knew that he was the one laughing."

scene black with fade

#if alexia is sharing a room with Rowan
if not alexiaSeparateRoom:
    show alexia necklace naked shocked behind black

    al "Rowan, Rowan!"

    scene bg9 with fade
    show alexia necklace naked shocked at center with dissolve
    #neutral
    show rowan necklace naked concerned behind bg9

    ro "Wha? Alexia, where?"

    show alexia necklace naked at center with dissolve

    al "Good.  You were tossing and crying out in your sleep. Saying no over and over to yourself."

    show alexia necklace naked at midright with moveoutright
    hide rowan
    show rowan necklace naked sad at midleft with dissolve

    ro "Oh, it was just a dream."

    al "A nightmare. I've never seen you like this before, it was nothing like the war terrors you sometimes had."

    "Rowan covered his face with his hands, feeling the cold tears on his face that had been brought forth from the horrific images in his mind."

    ro "It's getting to me. The guilt for the things I've done for the twins, the people I'm killing and enslaving...."

    al "Hey, take it easy.  You're not doing any of that right now, you're with me."

    "She wrapped her arms around him and tried to comfort her husband. The soft embrace brought forth both tears of guilt and gratitude. The hero cried against his wife, cried for the evil he'd done and for what he would still have to do for the two of them to survive."
    "After some time had passed, Rowan's tears finally stopped flowing and he pulled back."

    show rowan necklace naked concerned at midleft with dissolve

    al "Feeling better now?"

    ro "Not really, but I think I can bear it."

    al "Are you worried this is going to affect your work?"

    ro "No, this guilt definitely is going to hamper me a little. I can probably take some more before it seriously slows me down, but eventually I'll be crippled by it."

    al "You're a good man. Even after all that's happened, you're still a good man. Try to take it easy, we'll manage if you put off doing bad things while your consciousness is getting to you."

    show rowan necklace naked at midleft with dissolve
    "A wry chuckle escaped his lips, seeking a break from the morbidity of the discussion."

    ro "Yeah, try to balance the evil so I don't feel quite so bad about it. Great advice."

    #alexia necklace naked concerned
    al "Rowan?"

    show rowan necklace naked concerned at midleft with dissolve
    ro "I'm fine, I'm... fine."

    return

#else
else:

    show rowan necklace naked concerned behind black

    ro "No! No! Please!"

    "Rowan shook, his body was covered in cold sweat and he could feel tears on his face."

    ro "Where?"

    scene bg9 with fade
    show rowan necklace naked sad at midleft with dissolve

    ro "Oh, it was just a dream."

    scene bg14 with fade
    show rowan necklace neutral at midleft with dissolve
    show alexia 2 necklace concerned at midright with dissolve

    al "Rowan! You look awful, what happened?!"

    ro "Oh, hello Alexia, I had a bad night."

    al "Bad?  From the looks of things it was truly awful. Did you have another night terror from the war? No, wait, this looks much worse."

    "Rowan covered his face for a long moment, recalling the images that he'd seen and what was clawing at his insides."

    ro "It's getting to me. The guilt for the things I've done for the twins, the people I'm killing and enslaving...."

    show alexia 2 necklace happy at midright with dissolve

    al "Hey, take it easy.  You're not doing any of that right now, you're with me."

    show rowan necklace sad at midleft with dissolve
    "She wrapped her arms around him and tried to comfort her husband. The soft embrace brought forth both tears of guilt and gratitude. The hero cried against his wife, cried for the evil he'd done and for what he would still have to do for the two of them to survive."
    "After some time had passed, Rowan's tears finally stopped flowing and he pulled back."

    show rowan necklace neutral at midleft with dissolve

    al "Feeling better now?"

    ro "Not really, but I think I can bear it."

    al "Are you worried this is going to affect your work?"

    ro "No, this guilt definitely is going to hamper me a little. I can probably take some more before it seriously slows me down, but eventually I'll be crippled by it."

    al "You're a good man. Even after all that's happened, you're still a good man. Try to take it easy, we'll manage if you put off doing bad things while your consciousness is getting to you."

    show rowan necklace happy at midleft with dissolve
    "A wry chuckle escaped his lips, seeking a break from the morbidity of the discussion."

    ro "Yeah, try to balance the evil so I don't feel quite so bad about it. Great advice."

    show alexia 2 necklace concerned at midright with dissolve
    al "Rowan?"

    show rowan necklace neutral at midleft with dissolve
    ro "I'm fine, I'm... fine."
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label disease_outbreak:
#Disease outbreak
#Req at least 10 soldiers.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show orc soldier neutral at midright with moveinright
show andras angry at edgeright with moveinright

"That morning, shortly after Rowan had gotten to work he was approached by Andras and an orc soldier."

ro "Yes, how can I help?"

an "Show him."

"The demon motioned to the soldier with him, who promptly stripped down and revealed a large rash that was spreading across his abdomen."

an "This damn rash has spread to a bunch of our troops and it's making them weak."

show rowan necklace angry at midleft with dissolve

"Rowan gritted his teeth and cursed."

ro "Damn, that's bloodren pox. It's a very dangerous disease that usually either kills those it infects within a few days or clears out after a week. Tends to spread fast too, very dangerous to people closely packed together, like soldiers in a barracks."

an "Gheh, can we stop its spread by killing the infected?"

ro "We don't need to kill them, just isolate them. If you survive this, you're pretty much immune afterwards. Come on, we need to start moving the infected away from the barracks into the tunnels."
ro "That should at least slow the rate of infection, I hope."

show black with fade

"The two of them headed down to the barracks and organized Rowan's suggested quarantine. There did seem to be fewer new cases afterwards, but the hero wasn't sure if that was because the outbreak had already died down or because of his efforts."
"Many of the soldiers that had already come down with bloodren pox would be dead by the end of the week when Rowan returned from his exploration."

#Randomly lose between 5 and 20 soldiers, but not more than 50% of your total.
$ castle.buildings['barracks'].troops -= min(castle.buildings['barracks'].troops / 2, 4 + dice(16))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label pure_morning_with_alexia:
#Pure morning with Alexia
#Requires Rowan and Alexia be sharing a room and that Alexia be pure.

scene cg30 with fade

"Rowan awoke to the feeling of his wife laying on him.  Since she still seemed to be asleep, he decided to just enjoy her soft warm skin against his rather than waking her up."

show alexia necklace naked behind cg30

al "Good morning darling."

scene cg31 with fade
show alexia necklace naked behind cg31
show rowan necklace naked behind cg31

ro "Heh, it isn't often that you wake up before me. What gave it away?"

"Alexia slipped her hand under the sheets and brushed it over her husband's cock, which had grown hard next to her leg."

ro "Should I apologize for thinking you're beautiful?"

"They both grinned."

al "Never."

menu:
    "Time to get up.":
        $ released_fix_rollback()
        "The two of them shared a long kiss, then the hero climbed out of bed to start another day in glorious service to the twins."
        return

    "Flip over onto Alexia and make love to her.":
        $ released_fix_rollback()
        jump .alexiaPureMorning

label .alexiaPureMorning:

#CG of Rowan kissing Alexia while laying on top of her.
scene cg202 with fade
show rowan necklace naked behind cg202
show alexia necklace naked behind cg202
pause 3

"He rolled over, putting himself on top of Alexia and kissing her deeply. She welcomed him into her mouth and wrapped her arms around his head to keep him against her for several moments longer than Rowan had originally intended."
"When he was finally able to break the kiss, he had to take several deep breaths to recover."

ro "I knew you liked kisses, but I wasn't aware you liked to kiss my breath away."

al "If you're allowed to have surprises, so am I."

#CG of Rowan licking Alexia's nipple.


"As payback, Rowan shuffled a little ways down so that he could run his tongue around Alexia's nipple, as well as give it a playful nibble."
"This brought a sharp gasp to her lips, just as the man had hoped."

al "Ah! What's that for?"

ro "Just trying to steal your breath away."

al "I'm not sure you quite managed that, think you can try again?"

scene cg83 with fade
show rowan necklace naked behind cg83
show alexia necklace naked behind cg83
pause 3

"Instead of accepting that invitation, Rowan shifted once more to abruptly push himself inside Alexia's passage. She let out another gasp of surprise that quickly turned into a moan of pleasure."

ro "Nah, let's keep the train of surprises going."

al "Oh darling, you brute!"

"Her moans of pleasure between her words signaled that she was far from upset at this penetration. The feeling of her walls rippling around Rowan's cock, slick with the fluids of her arousal, added further evidence to that conclusion."
"Rowan began to slowly rock his hips forwards and back, his arms firmly planted on the bed on either side of Alexia's head for balance. His wife was content to let him take her, since he'd gotten lots of practise at learning the perfect pace to take their lovemaking."
"Gradually he increased his thrusts, timing them with Alexia's gasps and appreciative moans. Finally his own lusts caused him to lose control and he abandoned himself to them.  Sensing the change in her husband, the woman could only smile and whisper to herself."

al "Yes, Rowan please, please fill me!"

show cg83 with sshake
show cg83 with sshake
scene cg84 with flash
show rowan necklace naked behind cg84
show alexia necklace naked behind cg84
pause 3

"Rowan came, spurting deep into Alexia's hot passage and triggering her own orgasm in response. Still spurting more of his cum inside her, the man collapsed on top of his wife, weakened by the now finished sex."
"The woman wrapped her arms around her husband and kissed his neck while continuing to relish the feeling of him filling her. It was in these moments together without an audience that she was her happiest."
"After catching his breath and rolling off of Alexia, Rowan spoke again."

ro "Well, was your breath taken away?"

al "I don't know, you'd better try again to make sure."

"Both grinned at each other once more."

ro "How about tomorrow or next week?"

al "I'll see if I can fit you into my schedule."

ro "If you can't find the space, I'll be sure to work my way in anyway."

al "Ha. Darling, I think that's enough innuendoes for one morning."

"The two of them shared a long kiss.  Then, still smiling, the hero climbed out of bed to start another day in glorious service to the twins."

#Rowan loses some corruption
$ change_base_stat('c', -2)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label jezera_s_alliance_making_skills:

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with dissolve

"Rowan’s day off from the field came to a screeching halt at the interruption of the one woman who had the least compunction of anyone against disturbing you."

je "There you are, my hero. I need to ask a favor of you, I'm going to be meeting with a woman of some status shortly and I'd like to present you as my sex toy to demonstrate my power."
je "But, it would be simply criminal of me to go without an accessory. A prestigious prize to demonstrate my power."
je "{i}You.{/i}"

"Rowan wiped the sleep from his eyes, as if doing so might make her vanish from the air like a mirage."

ro "Jezera. It isn't like you to ask first. Is there a catch?"

je "Only if you mind wearing a collar and filling your mouth with pussy while two lovely ladies discuss politics."
je "..."

ro "..."

je "Oh, and I might lend you out to her too. You know how that sort of thing goes, by now. "

"She giggled to herself."

je "I called it a favour, because we’re going to need a bit of...acting on your part. Your value as a trophy is somewhat diminished if I can’t sell you as an {i}obedient{/i} trophy. So, much as it pains me to require assent, I will need your cooperation."


menu:
    "Pretend to be Jezera's sex slave.":
        $ released_fix_rollback()
        ro "..."
        "Rowan threw his hands up in defeat."
        ro "Fine."
        je "Most excellent."
        je "You must be on your best behaviour. I have worked long and hard to bring this moment to fruition. This is, perhaps, my finest masterstroke yet. One more impactful even then you!"
        "Her hand reached down and gave Rowan a playful slap on the ass. He jumped defensively, resisting the urge to draw his sword."
        je "Come, let's get you dressed up {i}properly{/i} and then we'll be on our way."
        scene bg10 with fade
        #rowan prisoner garb
        show rowan necklace neutral at midleft with dissolve
        show jezera neutral at midright with dissolve
        "In addition to a collar, the demoness also had the hero change out of his clothes into something quite similar to the prisoner garb he'd been forced to wear a few months prior."
        "The ensemble clashed severely with the elaborate sapphire necklace, but Jezera made no move to remove it."
        $ delfQueenSex = True
        jump delfqueenmeeting

    "Politely Refuse her “Dignified” Request.":
        $ released_fix_rollback()
        "Rowan kept his place, stone faced."
        ro "Jezera. I’m your castle’s stewart. I’m not going to just agree to that."
        "Jezera chuckled to herself and flashed Rowan a dark grin. A lesser man might shrink from that look."
        je "Surely, that isn’t a hint of defiance I hear from you? What’s so bad about being forced to parade around in chains?"
        je "Am I going to have to persuade you?"
        "She leaned forward, wiping the space between them away. So close there were mere inches between their chests. His pulse sped up."
        "But, he responded by taking a step back to regain space. Then, he crossed his arms over his chest defiantly."
        ro "Will this entire meeting of yours collapse if I don’t arrive in chains?"
        je "Well, I suppose not…"
        ro "I told you, I want no part in what you just described. I just returned from a week in the field doing your bidding. Is this really so important as to create a conflict?"
        show jezera neutral at midright with dissolve
        "She rolled her eyes and drew back. She reminded him of a cat whose favorite toy had been drawn away."
        je "Tsk. You’re as much of a bore as I feared."
        je "Very well. In my generosity, I will allow you to come merely as a prisoner, as opposed to a chained sex slave. The fun parts can be forgone, but you’re still valuable as a trophy. "
        show rowan necklace angry at midleft with dissolve
        ro "...I’m not arguing out of that part, am I?"
        je "This is an important meeting. Today, a plan many months in the making comes to fruition. A powerful new subject in our camp. I will not let your petulance sabotage it now."
        je "This will not be a difficult trip. Just stay with me and be quiet. "
        scene bg10 with fade
        show rowan necklace neutral at midleft with dissolve
        show jezera neutral at midright with dissolve
        $ delfQueenSex = False
        jump delfqueenmeeting

label delfqueenmeeting:

scene bg3 with fade
show jezera neutral at midleft with dissolve

"After that, the two left through the portal to a forested area nearby mountains that Rowan wasn't familiar with. He recognized the scenery, at once, from the war. This was the forests of Ealoaen, home of the elves."

#cave bg
scene cave1 with fade
show jezera neutral at midleft with dissolve

"Jezera led him to a nearby rock formation and opened up a hidden path down into a cave. She obviously knew where she was going, as she picked her way through a very specific path from tunnel to tunnel, ever downwards."
"Occasionally she'd use magical ribbons of energy to carry herself and Rowan down sheer cliffs or over difficult terrain. That particular spell seemed to be Jezera's magic of choice as she was very good at manipulating the energies and she always used it when she could."

if delfQueenSex == True:
    "Eventually they reached caverns that had been worked by intelligent hands. Here was where the show would begin, so a lease was taken up and a hood placed over the hero's head."
    scene black with fade
    show jezera happy behind black
    "Rowan would have to trust his mistress to lead him through the caves. Even without his eyes covered the man would have had a hard time making his way through here as the demoness no longer bothered to use lights and there was no other sources the man could make out."
    "Voices whispered about them and the soft pattering of feet other than their own was audible, but Rowan had no idea who they belonged to."
    "Eventually, they arrived at an underground building of some kind. The unseen guides lead them inside while Jezera conversed with another woman in a language that Rowan Didn’t understand. Likely dark elvish."
    "The purpose of the meeting was growing clearer to him by the moment."
    "Inside Rowan finally could see something again. Glinting lights would occasionally wink at him through the lines in the fabric covering his head. They were taken to a chamber deep inside the structure before someone spoke again."

else:
    "Eventually they reached caverns that had been worked by intelligent hands. Figures moved around them with little light, but he could see shadows playing over great structures and the occasional glint of crystal in the darkness."
    "They whispered and stepped softly, meer pattering accompanied their footfalls. That meant they were probably elves. Rowan smiled in spite of himself, it explained why Jezera was treating this meeting as such an important affair."
    "Rowan watched them with careful eyes, his hand always resting on the pommel of his sword. However no one challenged them or approached the two walking down the center of the artificial cavern."
    "Eventually they arrived at a particularly grand building, where Jezera briefly conversed with a woman in dark elvish. He couldn't understand what they were saying, but it confirmed Rowan's suspicions."
    "The inside was much better lit by glowing crystals, it's passages made up of stone and yet more crystals of different colours and cuts wrought in dazzling architecture and artistry. They were led to a deep chamber inside the building before anyone spoke again."
    scene cg466 with fade
    show jezera happy behind cg466
    pause 3
    "Inside was a regal dark elf woman dressed in an expensive silk gown that clung tightly to her body and accentuated her lithe womanly features."
    "It appeared to be a private sitting room, with the dark elf seated in a chair at a small two person table against the wall."

wom "Well now Jezera, let's see the great hero my attendant tells me you've brought."

"She spoke in the common tongue, either because it was Rowan's or Jezera's native language. Regardless of the reason, it meant that the man could understand it."

je "Of course."

if delfQueenSex == True:
    "Now Jezera roughly dragged Rowan forward and pushed him to his knees before pulling the hood up off his head."

je "May I present, the great hero of Karst and one of Deanara’s band to defeat Karnas, Rowan Blackwell."

if delfQueenSex == True:
    scene cg466 with flash
    show jezera happy behind cg466
    pause 3
    "Thanks to the light given off by some nearby crystals, Rowan could clearly see the regal dark elf woman that he'd been presented to. She was a lithe woman, dressed in an expensive silk gown that clung tightly to her body and accentuated her womanly features."
    "They were inside what appeared to be a private sitting room, with the dark elf seated in a chair at a small two person table against the wall."

else:
    je "Now an agent of Bloodmeen!"
    "Rowan stepped forward at Jezera's proclamation in full gear, hand on his sword and nodded to the two women. He leveled his gaze at the dark elf, wondering how this would go now."

"She stood up, revealing herself to be nearly a head taller than Rowan, and took a step forward to get a closer look at the man. A wicked smile graced her lips and the hero felt a flash of recognition that mirrored the expression on the woman's face."
"He knew this woman, but why?"

if delfQueenSex == True:
    jump delfPlayingSexSlave
    
else:
    jump delfPlayingPrisoner
    
##################################

label delfPlayingSexSlave:
    
wom "Hahaha! It is him! Well now Jezera, it seems I owe you an apology. Let's see how well he licks."

je "I'd be happy to."

"The two women sat down together at the table and Jezera pulled on Rowan's leash until he crawled up to her legs. While he wrapped his arms around her and lifted the fabric of her dress out of the way he continued to wonder where he'd seen this dark elf before."

scene cg67 with fade
show jezera happy behind cg67
pause 2

"He could feel the gaze of the lady from behind as he started his work on his mistress. First he kissed the insides of her legs and gently drew his fingers over the crevice of her skin where leg met hips. Then brushed his tongue over labia, nibbling slightly when he touched the other side."

wom "He's quite the romantic, isn't he?"

je "Yes, did you know that after the war he went back to his home village and married his peasant sweetheart?"

wom "Huh, no kidding? I admit, married men are among my favorites to make my own."

"Rowan extended his tongue and ran it up the inside of the lower lips, then flicked it ever so slightly over Jezera's clit, causing her to twitch once. She inhaled sharply as his tongue plunged deep into her passage several times in succession."

wom "It would sound like you're having a good time. Would you mind giving me a chance to enjoy him afterwards? The thought of having a hero of men between my legs is... appealing."

"A hand was placed on the back of Rowan's head as he continued to toy and tease. Then it pushed him against Jezera's sex as her thighs tightened up around his head. Taking the hint, he switched to a much more direct method of eating and licking as fast as he could."

"The effect was almost immediate. Gasps and moans of pleasure now emanated in response to his ministrations. Jezera exalted in this act and was soon leaking out her fluids all over Rowan's face in orgasm."

je "Hah, hah, I would say that he's probably good for a second round, aren't you pet?"

"She ran her fingers through his hair and smirked down at the man still between her legs."

je "You just love pussy, don't you? Go get more!"

scene cg231 with fade
show jezera happy behind cg231
pause 3

"Jezera relaxed her legs and directed Rowan towards the dark elf. He shuffled on the ground the short distance to the other woman, keeping his head down to avoid drawing too much attention."

"The unfamiliar lady uncrossed her legs and rolled up her gown to reveal an elven vagina. Her folds were thinner than Jezera's, fitting right in with her lithe frame. It was also already very wet, evidence of just how much the previous display had turned her on."

#CG of dark elf queen with Rowan eating her out.

wom "Like what you see? Good, drink up slave!"

"She lifted up her legs and wrapped them around Rowan's head, forcing him in without any setup or foreplay. Obediently, he started licking, hard."

wom "Oh yes. More, more."

"While the man redoubled his efforts, he felt a long finger brush over his face. Suddenly there was a sharp pain as the woman opened a small cut on his cheek which made him cry out."

wom "Uh, uh, uh, keep eating or it will get worse."

"He did so, licking and plunging and drinking from the dark elf. At the same time, she caught a few drops of his blood on a finger and brought it up to her lips. Rowan could just barely see her licking the finger sensually before she let out one long gasp that signalled her orgasm."
"Shortly after coming down from her high, the dark elf woman casually released the man from her grip and pushed him to the side so she could sit at the table properly again."

wom "That will do. Shall we talk business, Jezera?"

je "Yes, let's."

"The two of them pointedly ignored Rowan as he crawled away until the leash was taught and then sat down cross legged to watch their conversation. Well, he mostly listened since he didn't want to take the chance of making eye contact with the woman."

scene cg466 with flash
show jezera happy behind cg466

$ change_base_stat('c', 3)
$ change_favor('jezera', 1)
jump delfQueenEnding

####################

label delfPlayingPrisoner:

wom "It is him. Fully armed and unchained, no less. I didn’t expect you to be quite so trusting."

je "I considered bringing him in chains to show his obedience. But, that just seemed too...pedestrian. What better show of where his loyalties lay now then to show him, sword in hand. "

"The unfamiliar woman crossed her arms with an appraising look on her face."

wom "My trainers would be able to make short work of this one I assure you. A month or two in confinement, some torture, and he'll do anything you want to make it stop."

"Rowan let a smile play across his face."

je "A hero has more spirit than you give him credit for."

wom "He certainly thinks so. Letting a man walk so freely among us does not reflect well on you."

je "This is the last time he will. Nevertheless, you wanted proof of my abilities, here he is."

"After a moment more contemplation the elf let out a sigh and turned her attention back to Jezera."

wom "Very well, I admit you were correct. Shall we talk business, Jezera?"

je "Yes, let's."

"The two of them took chairs at the table and pointedly ignored Rowan. That was fine, it gave him a chance to listen in on the conversation while he leaned against the wall."

####################
label delfQueenEnding:

"They discussed an alliance between the woman and Bloodmeen castle, which Jezera seemed to claim to be the sole ruler of. Made sense, dark elf society was a matriarchy and wasn't exactly known for respecting men at all."
"The talk went on and on, covering various subjects. However a point of contention often was exactly what kind of relationship this would be. Jezera clearly wanted to be in charge, while the dark elf wanted something more equal."
"Jezera repeatedly offered different regions and fiefdoms, but the elven woman would respond that she should get more or all the lands she conquered. This did not sit well with the demon. In fact, the longer the conversation went on, the more visibly irritated she became."
"The conversation then moved on to personal matters. Rowan found himself distracted for a moment in old memories, trying to conjure up why the elf seemed so familiar. Had he seen her in the war? The reminiscence was cut off when Jezera abruptly lost her composure."

je "Being a vassal of the new rising of Bloodmeen and a lord of one of our provinces should be an honor for you! I've already given you generous gifts and proven I can capture a hero right under the church's nose, why won't you serve me?!"

"The dark elf woman laughed and shook her head at the sudden outburst."

wom "You don't really know anything about diplomacy, do you child? If I recall, you started this whole negotiation claiming we were equals. Now you want both my help and my submission? That's not how this works."

"Still smiling, she leaned forwards in her chair."

wom "I have eyes in many places. I know who I’m dealing with. I'm have the armies, and you desperately need them. If this alliance is to happen, you need to offer me something far better. And try to compose yourself."

"Jezera did not reply, but straightened in her chair and folded her trembling hands in front of her."
 
wom "Better. Now listen to me, child. I will join you, but as an equal not a subject. The price for helping you take the world will be half of it. Fair, is it not? We both get something we want, that's diplomacy."

je "You are not the equal of a demon, worm."

wom "Now you have it twisted. You should feel honored I’d even consider recognizing a little girl with delusions of grandeur as someone worth coming to an arrangement with."
wom "Know your place."

if delfQueenSex == True:
    "The demoness suddenly stood up and tossed the lead of Rowan's leash aside."

else:
    "The demoness suddenly stood up, knocking over her chair with a dull clatter."
    
"Ribbons of magic blazed to life around her. They lashed at the ground and threw the crystal furniture against the walls of the room."

wom "Sit down, you're not impressing anyone by -urk!"

scene cg459 with fade
show jezera neutral behind cg459 
pause 3

"One of Jezera's cords of magic snapped around the dark elf woman's neck, cutting off her words and causing her to struggle for breath!"

show cg460 with dissolve
pause 2

"Genuine fear was plain on the elven woman's face for the first time. She tried to signal something as her body was lifted up into the air by her neck."

show cg461 with dissolve
pause 2

je "The dark elf struggled at the demonic magic binding her while Jezera continued to watch her cooly."

show cg462 with dissolve
pause 2

"As moments passed, more and more tethers latched on until the combined force tore all the way through, beheading the dark elf."

show cg463 with dissolve
pause 2

"This sudden reaction from Jezera had caught Rowan completely off guard and he didn't even have time to think about how he should respond in the scant few seconds between when his mistress launched her attack and when the body fell to the floor."

if delfQueenSex == True:
    show cg464 with dissolve
    pause 2
    "Unarmed, Rowan could do nothing but watch in the scant few seconds that passed from when Jezera first lost her patience until the body fell to the floor. He tried to think of something he could say or do, but none of it would have mattered. He could only watch on in shock."
    "It was only when the woman's head fell past that Rowan finally regained his wits.  Instinctively he did a quick scan of the area for potential threats before he caught Jezera's eye looking at him."

else:
    "Rowan drew his sword and readied himself for combat in the scant few seconds that passed from when Jezera lost her patience until the body fell to the floor. However, no enemies ran into the room and there was nothing he could have done to stop Jezera's wrath."
    show cg464 with dissolve
    pause 2
    "Rowan's attention was brought back to the grizzly execution as the woman's head fell past him. In that instant Jezera and his eyes met."

play sound "music/SFX/BodyfallDirt.ogg"
scene cg465 with fade 
show jezera neutral behind cg465
pause 3

"Those eyes held murder."

je "We're leaving."

"She didn't bother waiting for a response before teleporting the two of them back to the castle."

scene bg10 with flash
show rowan necklace neutral at midleft with dissolve
#jezera angry
show jezera displeased at midright with dissolve

je "GRRRAGH!"

show bg10 with sshake

"Instantly after they arrived Jezera let loose an uncharacteristic shriek!"
"Then took a deep breath, clenching and unclenching her fist, and finally lowered her arm."

je "Grr, I'm going to have a bath. You're dismissed Rowan."

if delfQueenSex == True:
    "She started to walk away, then turned back and offered a smile to the man who was still sitting on the ground."
    show jezera happy at midright with dissolve
    je "At least I can count on you, {i}my hero{/i}."

hide jezera with moveoutright

"This whole episode worried Rowan greatly, as it was the first time he'd learned something of Jezera's activities away from the castle. If this was how she conducted all her negotiations, there could be dire consequences."
"Plus he still wasn't sure who the woman had been. It was clear that she had been someone of great power within the dark elf hierarchy, a general perhaps? He didn't know and it wasn't worth the risk of asking Jezera right now."

$ codex_add('dancer_s_whips')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label drinking_buddies:

show bg22 with fade
show rowan necklace neutral at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve

gh "Rowan, you are here early today."
gh "Was the last order of weapons not good enough? There is time still to fix them."

ro "No, nothing like that, Greyhide."
ro "I figured a nice change of scenery would do us both some good."
ro "We still haven’t gotten that drink."

"Greyhide smiled and set down his hammer, gently removing his massive leather apron from his broad shoulders."

gh "No, we have not."

ro "Wouldn’t you rather hang out somewhere a bit less cooped up than the forge?"

gh "I like the forge. It is peaceful. Calm."

ro "I’ve never heard someone describe a cramped room filled with soot and molten metal ‘calm.’"

"Greyhide grinned, flashing a glimpse of his square, flat teeth."

gh "Now you have."

ro "Have you ever seen the view from the castle battlements?"

gh "No."

ro "Would you like to?"

gh "Is there drink involved?"

ro "Oh, I’m sure we can procure a few bottles."

gh "Heh. You will need more than that."
gh "Lead the way, we will see if the view is better than my forge."

ro "I’m sure wine won’t hurt the scenic vistas any."

scene bg57 with dissolve
show rowan necklace neutral at midleft with dissolve

"Rowan stood at the top of the castle, staring out across the Rakshan Wastes with a wistful expression. A number of wine bottles sat at his feet, requisitioned from the castle larder."

show greyhide neutral at cliohnaright with dissolve

"The bull stood at his side, towering over him with his imposing size. The two looked out across the vast emptiness together."
"Rowan should have been unsettled by the hulking brute looming over him. But... he wasn’t. There was a peculiar, disarming quality about the Minotaurs’ quiet presence. He felt at ease."

ro "Have you ever had Rosarian wine before?"

gh "I have not."

ro "Then I hope you like the taste.  It’s a speciality of my home country."

"The minotaur took the bottle that Rowan offered him and drank the whole thing in one swig."

gh "Tell me about your homeland."

show rowan necklace happy at midleft with dissolve

ro "Rosaria is a beautiful place, verdant and green. It’s a land of great plains of grass dotted with farmland, with pleasant forests and rolling hills."

gh "Sounds like it's got a better view than here."

"Rowan chuckled, taking a sip from the bottle as he stared at the bleak mountains in the distance."

ro "The most wonderful place for me was always my home village. Arthdale is really beautiful this time of year."

show rowan necklace concerned at midleft with dissolve

ro "Or… was beautiful, I guess."

"The old bull let him stew for a moment in his dreary reminiscing, slurping loudly from his second fill as Rowan nursed his bottle in his hands."

gh "What do you remember most about it?"

"Rowan leaned back against the wall and closed his eyes, picturing his home as he described it."

ro "It’s mostly just images in my head: lazy mornings filled with the laughter of children, and the smell of fresh baked bread. Smiling faces and greetings from people you’ve known your whole life."

gh "I like the sound of your home. Very different from mine."

ro "Your kind lives in tribes, do they not?"

gh "Yes."

"The minotaur picked up another bottle and used his teeth to pull out the cork.  He spat it over the wall and took a big swig, nearly emptying the whole thing."

gh "My home was in the harsh mountains, living in caves scratched into the bedrock. We moved around a lot, searching for food. We mostly ate moss and tough bushes. "

ro "So, no bread bakers I take it."

"Greyhide let out a rumbling chuckle."

gh "No bread. Berries were a rare treat. It was rough country, mostly rocks and shrubs. I never saw a real tree that was taller than me until I was nine."

ro "Why was your tribe stuck in such a desolate place?"

"Greyhide’s expression softened. He took another long swing of his drink."

gh "Not stuck. The lowlands weren’t safe."

ro "Bandits?"

"Greyhide shook his shaggy mane."

gh "Humans. They would hunt us as retribution for our raids."

ro "Oh… I’m sorry."

gh "You are not them. You don’t have to apologize."
gh "Our customs did not make it easy for us, either. Every day was a struggle. A pack mate who wanted to be boss, or rivals posturing for mating rights."

ro "It sounds brutal."

"Greyhide shrugged."

gh "It was life. I knew nothing else."

"Rowan took a thoughtful drag off of his bottle, musing for a moment on the bull’s past."

ro "How did you get mixed up with the Twins?"

gh "That was a question I was going to ask you."

"Rowan’s brow clenched at the memory. He took another swig."

ro "My wife was kidnapped, my hometown burned. I sat in their prison cell for months. They only set me free once I agreed to serve them."

gh "You sound like you regret the decision."

menu:
    "Yes.":
        $ released_fix_rollback()
        "Rowan’s mouth twisted into a sour frown. He didn’t respond immediately, staring into the bottom of his bottle in the vain hope of finding an answer."
        ro "There’s no use in taking it back now; what’s done is done."
        ro "I didn’t have a choice."
        gh "I believe you."
        gh "...I am sorry you are stuck here."
        "Rowan let out a bleak chuckle."
        ro "You’re not the Twins. You don’t have to apologize."
        
    "No.":
        $ released_fix_rollback()
        "Rowan considered the thought. To his surprise, the answer came easier than he expected."
        ro "Not… exactly."
        ro "My life has taken a drastic turn, for certain. But not all of it is bad."
        ro "I’m alive, my wife is safe, and I have a cause to work towards. That’s more than many men can say."
        gh "Purpose is what drives us. I did not expect to end up here when I left my home."
        ro "Life makes strange bedfellows, eh?"
        
    "I don’t know":
        $ released_fix_rollback()
        "Rowan chewed on his lip. He was shocked at how conflicted he felt. By all rights he should {i}hate{/i} what’s happened to him, but…"
        ro "I’m not sure. It’s too early to tell."
        ro "I’m still getting used to this place and the strange people living here. It’s not {i}awful{/i}, it’s just… different."
        gh "I feel the same. Most of the Twins’ servants are tiring to be around."
        "Greyhide patted Rowan’s back with his large hand."
        gh "You are the exception."

"A calm silence fell between them. Rowan looked across the valley to see an Orc hunting party making its slow procession towards the castle."

if alexiaForgeIntro:
    gh "I met your wife recently."
    ro "Alexia?"
    gh "Yes. She has been helping me in the forge."
    show rowan necklace happy at midleft with dissolve
    ro "I struggle to picture her hammering molten metal."
    gh "She is… green. But spirited. Rest assured, I will make a proper smith of her."
    gh "I envy the softness you enjoy with your wife.  Minotaur women are nothing like that, even {i}my{/i} love was a passionate beast."

else:
    show rowan necklace happy at midleft with dissolve
    gh "Your wife, she is the red haired waif who sometimes wanders about the castle, yes?"
    ro "Heh… I wouldn’t exactly call her a ‘waif,’ but yes that's her."
    gh "I have seen you talking with her before. I envy the softness you enjoy with your wife.  Minotaur women are nothing like that, even {i}my{/i} love was a passionate beast."
    
ro "You were married?"

"A shadow passed over Greyhide’s countenance. He looked away towards the horizon."

gh "Not married. My kind do not marry. We were… joined."
gh "We earned the right to be together by defeating our rivals. I fought and won against her suitors, and she did the same for mine."
gh "She was a wild woman. Aggressive. Talkative. She often frustrated me with how fast she spoke. I could never keep up."

"Rowan smiled, imagining the shy smith shackled at the hip to a gregarious, chatty woman. It was a strangely fitting image for him."

gh "She was kind to those she cared about. Tender with me, when we were alone."

"The old bull’s snout curled into a soft smile."

gh "Before I knew it, I was in love."

ro "It’s a wonderful feeling."

"Greyhide’s smile wavered. His large eyes squeezed shut."

gh "It was."
gh "Then... she died."

ro "What happened to her?"

gh "We grew soft together. A mistake."
gh "Life in the mountains is difficult, always a battle. An ugly shrike thought herself worthy of me."
gh "She threw my mate off a cliff, then demanded I take her as my mate instead."

"He popped open the third bottle. This time he downed the whole thing in one gulp. He immediately opened another bottle and began to take swigs from it."

gh "I didn't care to fight for women after that. Nor did I enjoy them fighting for me. It felt so... hollow."
gh "Why fight for love? Why cause pain for others so you can feel pleasure?"

"Rowan looked at the last bottle, still half full. He handed it to the minotaur as he stared with a grim expression into the distance."

ro "This kind of conversation requires a bit more wine than we have, I think."
ro "I'll be back with a full barrel."

scene black with fade

"{i}A few hours later...{/i}"

scene cg792 with dissolve
show rowan necklace happy behind cg792
show greyhide neutral behind cg792
pause 3

"He knew he was drunk, because he kept realizing he was drunk and then promptly forgot about it again. That’s definitely something a drunk person would do. He really needed to remember to make a note of such things."
"For the first time in a long time (or maybe it was only a little while ago… what day was it, anyway?) he had cut loose."
"Or... perhaps the second bottle had simply loosened his tongue. He was, after all, laughing hysterically. At who or what he was not certain, but evidently Greyhide found it funny too."
"The bull clapped Rowan’s back with his big hand, chuckling merrily. Rowan nearly pitched forward off the wall from the impact. That only made him laugh harder."
"Greyhide lifted his sloshing tankard up to his lips like a king raising his crown at a coronation. His furry cheeks wept purple trails on either side as he gulped."
"Finished with his drink, he opened his gullet and let out a loud bellow, roaring out some incomprehensible noise that no human could make out into the empty wastes."
"The sound was strange and silly and funny and… other adjectives to Rowan. He was beset once more by breathless giggles." 
"Goddess fend, where had the sun gone? It wasn’t an eclipse, was it? And when had the hunting party found time to arrive?"

gh "Heh. You humans are all alike. Can’t hold your drink."

ro "Hey! Rosss-arian wine iss strong, okay? We can’t all be ten feet-tttall!"
ro "And ssstop dodging the… the question!"

gh "You did not ask a question."

ro "I’m {i}getting to it{/i}, oh-kay?"

"Evidently Rowan’s subconscious had been carrying on a very spirited conversation with the bull already, one it was completely comfortable with continuing without him. Best not to interrupt the two while they bonded."

ro "Sssso... think you cou- {i}ugh{/i}, could ever love again?"
ro "N-not that thatsh a {i}bad{/i} thing, just… you know-"

"Greyhide let out a low rumble in his chest. He shrugged."

gh "Who knows. Maybe not? I do not know."

"Rowan patted the top of the bull’s large finger like he was reassuringly patting the hand of a widower at a funeral."

ro "Ah, you’ll be fine. You’ll get ‘em."

gh "I’ll get what?"

ro "What?"

gh "I’ll get what?"

ro "Love!"

"Greyhide chuckled."

gh "Maybe."

menu:
    "Have you ever conshidered men?":
        $ released_fix_rollback()
        "Rowan blushed… or maybe that was just the wine coloring his cheeks. His fingers squeezed gently against the bulls thick digit."
        ro "Theresh lots of people out there."
        gh "Of course."
        ro "Not all of them Minotaursh."
        "The minotaur stared at Rowan for several moments, silent confusion playing over his visage at the suggestion. Then his eyes went wide."
        gh "Oh… I, um… "
        gh "I had not thought of it that way."
        ro "You ssshould! You’re a… a great guy, Greyhide. You {i}duh{/i}- deserve to… to be happy."
        "Greyhide seemed to have trouble looking directly at Rowan. Maybe the wine had finally got to {i}him{/i} as well."
        gh "I shall think about your suggestion."
        ro "Do that. I need to go passh out. I think I’m a little… you know…"
        ro "Tired."
        "Greyhide laughed again."
        gh "Sleep well, Rowan."
        "Rowan staggered back to his room through the gathering dark. He would recall most of that night's conversation with a great deal of embarrassment."
        "And… maybe, just a bit of hope."
        $ drinking_buddies_suggestion = 'men'
        return

    "Alexia livesh here too. You ssshould meet her!":
        $ released_fix_rollback()
        ro "Y-you sssshould meet my wife. Alex- uh, {i}Alexia{/i}!"
        "Rowan nodded to himself, proud that he had figured it out."
        ro "She- she- she’s great. {i}Super{/i} schweet. Like you! But… without the horns."
        gh "She would not be scared of my size?"
        "Rowan slapped the bull’s shoulder and waved him off."
        ro "N-{i}no{/i}! I don’t thinksho. She’s- she’s super schweet."
        gh "Heh. So you have said."
        ro "Would I ever lie to you, Greyhide?"
        gh "You do not seem like that kind of man, Rowan."
        ro "Good. Cause I’m not."
        "Greyhide took an experimental sip from his tankard."
        gh "I would enjoy meeting her. I have too few friends in this castle."
        ro "Itsh a date, then."
        "Rowan stood up on his unsteady legs, resolved to inform his wife about these latest developments. They had a friend! And a Minotaur, no less!"
        "He really was a kind fellow. Rowan was sure Alexia would get along swimmingly with him."
        "Now if he could {i}just{/i} figure out how to stumble back to his room..."
        $ drinking_buddies_introduce_alexia = True
        return
        
    "Doessh having a friend help?":
        $ released_fix_rollback()
        "Rowan chuckled and lifted his bottle, clinking it against Greyhide’s tankard."
        ro "At leash you got me, eh?"
        "Greyhide grinned and drank deep from his tankard."
        gh "I do. I was right on the first impression: you are a good man, Rowan."
        ro "And yooouuure a good man t-too, Greyhide."
        "The two drinking buddies clapped each other on the back, drifting away to simple conversations about life, the castle and their daily lives."
        "It would be hours yet before Rowan stumbled into bed."
        $ drinking_buddies_suggestion = 'friend'
        return
        