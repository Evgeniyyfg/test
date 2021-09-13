init python:
    event('greyhide_finale_alexia', triggers="week_end", conditions=('alexia_greyhide_sex', 'rowanGreyhideLiquorSex == False',), depends=('after_drinking_greyhides_alchol',), group='ruler_event', run_count=1, priority=pr_ruler_high)
    event('greyhide_finale_rowan', triggers="week_end", conditions=('alexia_greyhide_sex == False', 'rowanGreyhideLiquorSex',), depends=('after_drinking_greyhides_alchol',), group='ruler_event', run_count=1, priority=pr_ruler_high)
    event('greyhide_finale_platonic', triggers="week_end", conditions=('alexia_greyhide_sex == False', 'rowanGreyhideLiquorSex == False',), depends=('after_drinking_greyhides_alchol',), group='ruler_event', run_count=1, priority=pr_ruler_high)
    event('greyhide_finale_poly', triggers="week_end", conditions=('alexia_greyhide_sex', 'rowanGreyhideLiquorSex',), depends=('after_drinking_greyhides_alchol',), group='ruler_event', run_count=1, priority=pr_ruler_high)
    

label greyhide_finale_alexia:

if alexiaSeparateRoom == False:
    scene bg54 with flash
    show alexia necklace naked shocked at midleft with dissolve
    al "{i}Ah{/i}!"
    "Alexia sat up in a rush, her heart racing as her body thrummed with frantic energy."
    show alexia necklace naked concerned at midleft with dissolve
    al "Hah… hah..."
    "It took her several seconds to reorient herself once again to the bedroom’s midnight interior. The heavy shadows set her animal mind aflame with the threat of danger."
    "...Another dream. Another nightmare. How many did that make now? Three that evening?"
    "It had been like this for days." 
    "Rowan had warned her about the side-effects of the drug Jezera had inflicted on them. Of insomnia and lucid dreams." 
    "Their bodies were simply working the toxin out of their systems. But knowing that didn’t change the fact that she was utterly miserable." 
    "Every night now she awoke with a confusing bundle of emotions. Guilt and anger and worry and… and…"
    "Her hand reached up to touch her chest, feeling the heavy pumping of her heart. It refused to abate. She didn’t know quite what to call this final feeling, precisely. A queer admixture of fear and longing."
    show alexia necklace naked angry at midleft with dissolve
    al "{i}Damn{/i} it, Greyhide!"
    "She threw off the covers and got out of bed, her mind whirling in dangerous directions." 
    "Things just couldn’t go on like this."
    
else:
    scene bg7 with flash
    show alexia necklace naked shocked at midleft with dissolve
    al "{i}Ah{/i}!"
    "Alexia sat up in a rush, her heart racing as her body thrummed with frantic energy."
    show alexia necklace naked concerned at midleft with dissolve
    al "Hah… hah..."
    "It took her several seconds to reorient herself once again to the bedroom’s midnight interior. The heavy shadows set her animal mind aflame with the threat of danger."
    "...Another dream. Another nightmare. How many did that make now? Three that evening?"
    "It had been like this for days."
    "Rowan had warned her about the side-effects of the drug Jezera had inflicted on them. Of insomnia and lucid dreams." 
    "Their bodies were simply working the toxin out of their systems. But knowing that didn’t change the fact that she was utterly miserable." 
    "Every night now she awoke with a confusing bundle of emotions. Guilt and anger and worry and… and…"
    "Her hand reached up to touch her chest, feeling the heavy pumping of her heart. It refused to abate. She didn’t know quite what to call this final feeling, precisely. A queer admixture of fear and longing."
    show alexia necklace naked angry at midleft with dissolve
    al "{i}Damn{/i} it, Greyhide!"
    "She threw off the covers and got out of bed, her mind spiraling in dangerous directions." 
    "Things just couldn’t go on like this."
    
scene bg14 with fade
show alexia 2 necklace angry at midleft with dissolve

"She swept down the castle halls with a harried stride, every footstep bringing her closer to her destination. She ignored completely the curious looks she got from the castle staff, all but sprinting to the forge."

hide alexia with moveoutright

show bg22 with fade
show alexia 2 necklace angry at edgeleft with moveinleft

al "Greyhide! {i}Greyhide{/i}!"

"He had been silent for almost a week now, refusing to leave his room for any reason and barring all visitors."
"This time, she would not take no for an answer. She pounded her fist against the sealed door."

al "{i}Greyhide{/i}! I know you’re in there!"
al "...Just let me in! We need to talk!"

show orc soldier neutral at midleft with moveinright
show greyhide neutral at midright with moveinright
show wild orc neutral at edgeright with moveinright

"The door unlatched and slammed open. Alexia jumped back in surprise as a pair of guards marched from the room, a slump-shouldered Greyhide in tow."
"He was in chains, his hands manacled together and his head bowed. He hobbled forward at the urging of the Orcs, who tugged on his chains to make him go faster."

al "{i}H-hey{/i}!"

al "Stop! What’s going on? What are you doing to him?!"

"Greyhide did not even lift his head at the sound of her voice. His body language that of a beaten dog. He quietly shuffled past as the guards shoved him out of the room."

hide orc soldier with moveoutleft
hide greyhide with moveoutleft

al "What’s the meaning of this? Where are you taking Greyhide? "

wo "Boss’ orders. Forgemaster won’t work."

al "What are you talking about?"

wo "I mean what I says. He won’t work. So Boss tries to talk to ‘em. But Forgemaster won’t say nothin’."
wo "So Forgemaster gits tossed in a cell."

show alexia 2 necklace shocked at edgeleft with dissolve

al "{i}What{/i}?!"

show alexia 2 necklace angry at edgeleft with dissolve

al "B-but he didn’t do anything wrong!"

wo "Bring it up wit’ the boss then."

al "..."

hide wild orc with moveoutleft

scene bg8 with fade
show alexia 2 necklace concerned at midleft with dissolve
show orc soldier neutral at midright with dissolve

os "Oi, whatchu doin’ here lady? No visitors."

"Alexia felt a tremor at the base of her spine. She took in a deep breath and spoke in a clear, authorial tone."

show alexia 2 necklace neutral at midleft with dissolve

al "Mistress Jezera sent me to speak with the prisoner."

"The Orc hesitated, his beady eyes glancing from the cell door to the lone woman as if weighing the truth of her alibi. She did her best to maintain a stern expression."

os "Dis way."

"At last the Orc relented. He took out his keys and turned the lock, swinging open the heavy oak door to Greyhide’s cell."

os "Jus… knock if ya need me to open up again, eh?"

hide orc soldier with moveoutright

show alexia 2 necklace concerned at midleft with dissolve

"An eerie silence fell as the door slammed shut behind her. She stared, lips quivering, at the sorry sight of the Minotaur sitting in front of her."

show greyhide sad at cliohnaright with dissolve

al "...Hey."

"His eyes did not lift, his flat gaze stared dully into his lap.The Minotaur breathed in, his thick chest filling with air, then exhaled heavily through his nose. Alexia felt her chest tighten."

al "I..."

show alexia 2 necklace neutral at midleft with dissolve

"She trailed off. She couldn’t find the words to say to him. The silence was deafening."

menu:
    "I heard you’d stopped working… what were you thinking?":
        $ released_fix_rollback()
        gh "..."
        show alexia 2 necklace angry at midleft with dissolve
        al "You know what the Twins are capable of, what kind of risk you’re taking by defying them."
        gh "..."
        al "This isn’t like you."
        gh "..."
        al "Why wont you say anything to me?"
        show alexia 2 necklace concerned at midleft with dissolve
        
    "Are you okay? They haven’t hurt you, have they?":
        $ released_fix_rollback()
        gh "..."
        show alexia 2 necklace concerned at midleft with dissolve
        al "I swear, the moment Rowan returns, we’ll get you out of here."
        gh "..."
        show alexia 2 necklace happy at midleft with dissolve
        al "This is… it’s all just a big misunderstanding. I promise."
        gh "..."
        show alexia 2 necklace concerned at midleft with dissolve
        al "Why wont you say anything to me?"
        
    "It's not too late, you can still make things right with the Twins.":
        $ released_fix_rollback()
        gh "..."
        if alexiaJezObedient:
            al "Lady Jezera played a terrible prank on you, but that doesn’t mean she won’t listen to reason."
            gh "..."
            al "L-let me talk to her, I’m sure I could get her to… to…"
            gh "..."
        elif alexiaAndrasObedient:
            al "Lord Andras can be- {i}strict{/i} at times, but he’s not heartless."
            gh "..."
            al "If he knew his favorite forgemaster was locked down here, surely he’d-"
            gh "..."
        else:
            al "I know how hard it is to deal with them, Greyhide."
            al "But this isn’t the way, is it?"
            gh "..."
            al "You… you want to see sunlight again, yeah? And the birds?"
            gh "..."
            show alexia 2 necklace concerned at midleft with dissolve
            
    "I've missed you.":
        $ released_fix_rollback()
        gh "..."
        show alexia 2 necklace happy at midleft with dissolve
        al "I’ve thought about you a lot."
        gh "..."
        show alexia 2 necklace concerned at midleft with dissolve
        al "T-they can’t do this to you. You didn’t do anything wrong."
        gh "..."
        al "Why wont you say anything to me?"
        
"The bull flinched at her words. He lifted his head, just slightly. Only slightly."        
        
gh "No need… to protect me, little one."   

al "Why are you doing this, Greyhide?"

gh "Tired… tired of hurting others."
gh "Tired of trying... so hard."

al "You don’t mean that."

gh "..."

menu:
    "I care about you.":
        $ released_fix_rollback()
        gh "No. Not real. It is… not real."
        "Righteous anger rose up in Alexia’s chest."
        show alexia 2 necklace angry at midleft with dissolve
        al "You didn’t hurt me, Greyhide. You didn’t cause any of this!"
        al "I {i}chose{/i} to be with you."
        gh "Just... drug."
        "Alexia felt tears build up in the corners of her eyes. She took a purposeful step towards him, her hands balling into fists."
        #alexia crying
        show alexia 2 necklace concerned at midleft with dissolve
        al "{i}It would be so much easier if it was just the stupid drug!{/i}"
        al "Don’t you get it? I don’t regret what happened between us, I don’t regret any of it!"
        "She bent down, reaching out to caress his cheek. His lips pulled back in a pained grimace, he turned his face away."
        "She reached out anyway, fingers brushing across the fur of his snout. He flinched, but did not push her away."
        #alexia concerned
        al "Please... don’t give up on me like this."
        
    "It was just a fling.":
        $ released_fix_rollback()
        gh "To you."
        "Greyhide shook his head back and forth."
        gh "What of Rowan?"
        if all_actors["alexia"].relation < 30:
            show alexia 2 necklace angry at midleft with dissolve
            al "My husband would know a thing or two about infidelity."
        else:
            al "Rowan isn’t here, Greyhide. I am. "
        show alexia 2 necklace neutral at midleft with dissolve
        al "You don’t need to beat yourself up over a bit of harmless fun."
        "The bull’s head drooped. The conversation only seemed to be making him more miserable."
        show alexia 2 necklace concerned at midleft with dissolve
        "Uncertain how to proceed, Alexia gently patted his shoulder."
        al "Look, this wasn’t anything serious. And it never has to happen again."
        al "You can’t destroy yourself over something you didn’t have any control over."
        show alexia 2 necklace happy at midleft with dissolve
        al "...For what it’s worth, I enjoyed the time we spent together."
        
    "The drug made us do it":
        $ released_fix_rollback()
        gh "No."
        gh "No excuse."
        al "It’s not an excuse, Greyhide. It’s the truth. That same feeling overtook me."
        al "I don’t blame you for what’s happened."
        show alexia 2 necklace neutral at midleft with dissolve
        al "You’re my friend. I trust you. The fact that you feel this guilt at all just proves your good intentions."
        "Greyhide set his jaw and stared at the floor. She saw tears build in the corners of his eyes."
        show alexia 2 necklace happy at midleft with dissolve
        al "Hey, come on: it’s me."
        "Alexia got down on one knee, placing her hand on top of his own with a reassuring smile."
        al "You don’t have to hide it."
            
"Greyhide’s shoulders trembled, his body shuddered at her touch. He turned to look at her, his large eyes meeting hers for the first time."

gh "I-"

"The {i}snap{/i} of the lock unlatching behind Alexia brought them both screeching back to reality. The cell door opened wide, slamming against the outside wall from the force of the swing. "

show andras displeased at edgeleft with dissolve

al "L-Lord Andras!"

"Alexia stood up in a rush, scooting backwards till her back was against the cell wall. She made space between herself and Greyhide, giving way as Andras stalked into the room."
"The demon planted his hands upon his hips, his eyes shifting back and forth between Alexia and Greyhide for a short moment before he let out a huff of amusement."

an "I see you outwitted that dunce at the door."

"Far from being angry at her intrusion, the demon’s lips split wide into a smug, toothy grin. "

show andras happy at edgeleft with dissolve

an "Why am I not surprised to see you here?"

gh "Don’t…  blame her. I… I made her come-"

show andras displeased at edgeleft with dissolve

an "Oh, pipe down will you? You’ve played the part of the dreary martyr for long enough."

"Andras studied Greyhide for a long moment, his lips twisting with contempt at his downturned expression."

show alexia 2 necklace concerned at midleft with dissolve

if society_type == 'feudal':
    an "Is this any way to greet your Emperor?"
    
else:
    an "Is this any way to greet your master?"
    
show andras happy at edgeleft with dissolve

an "Stand up and look me in the eyes, like a real man would."

"Greyhide pulled himself painfully to his feet, rising up in the cramped cell till his horns were brushing against the ceiling. He had to hunch to fit inside, dipping his head low in deference."

if society_type == 'feudal':
    gh "Emperor Andras."
    
else:
    gh "Master Andras."

show andras displeased at edgeleft with dissolve

an "You’d better have a good explanation for yourself, you old fool."

gh "..."

an "I’ve spent the better part of a week at the muster yard listening to sob stories from my men. How all their broken equipment is being left to rust. One idiotic complaint after another."
an "At first I just chalked it up to you being preoccupied with work. But then I learned that your forge hasn’t been lit in {i}days{/i}."

gh "..."

show andras angry at edgeleft with dissolve

an "Stop staring at the floor like a drooling imbecile and {i}answer me{/i}."

gh "I… have no excuse."

show andras displeased at edgeleft with dissolve

an "Well that's too bad, old man. I’d at least be willing to hear it if you had one."
an "You are the castle Forgemaster, and we are at war. My men need weapons, and you are expected to provide them."
an "There is no excuse for failure. None whatsoever."
an "You have served me well thus far, and I’d hate to lose a tool as useful as you to such a frivolous matter."

"Andras cast a sidelong glance in Alexia’s direction, smirking at her discomfort."

show andras smirk at edgeleft with dissolve

an "What you do and who you do it with in your spare time is no concern of mine… up to and until it affects {i}me{/i}."

show andras displeased at edgeleft with dissolve

an "Consider this imprisonment your one and only warning. If I can’t count on you to do your duties, then I will find someone who can."

gh "That would… probably be for the best."

show alexia 2 necklace shocked at midleft with dissolve

"Andras was just starting to turn away when his head snapped around."

an "...Excuse me?"

gh "It would be... best. If you… found a better Forgemaster."

show andras angry at edgeleft with dissolve

"Alexia had never seen a look like the one that crossed Andras’ face in that brief moment. His expression twisted into something inhuman. Unrecognizable."
"Greyhide refused to meet his eyes, keeping his gaze trained to the floor. That only seemed to make the demon madder."

show andras displeased at edgeleft with dissolve

an "I see... so that’s how it is, then."

show bg8 with flash

gh "{i}Hurk!{/i}"

"Red energy surrounded Greyhide. A circle of profane magic grew above his head as Andras cast his torturous spell. The stoic minotaur fell to one knee, his body shuddering from the sudden onrush of pain."

an "So be it. Seeing as you no longer serve a purpose, I suppose there’s no use in keeping you around."

al "{i}Greyhide!{/i}"

"Andras released his concentration, allowing the spell to dissipate. The minotaur let out a gasp of air. Without missing a beat Andras’ fists clenched and the magic returned, stronger than before. It engulfed Greyhide in blinding agony."
"The bull let out a roar of pain, falling onto his hands and knees. His manacles jingled as he shuddered from the force of the magic assault."

al "Stop! Stop it!"
al "Please, don’t hurt him!"

show andras angry at edgeleft with dissolve

"Andras didn’t answer. He merely clenched his brow and redoubled his efforts." 
"Another pulse, this time for nearly five full seconds. Greyhide let out a bellow of pain. He writhed on the ground in agony as the red circle of energy roiled and contorted about him."

gh "{i}HRRRRRAAAGH!{/i}"

show alexia 2 necklace concerned at midleft with dissolve

al "{i}Stop! Stop it! You’re killing him!{/i}"

"Andras unclenched his hands, and the magic dissipated. Greyhide collapsed onto the ground and lay still. His body twitched, his muscles spasming as he whimpered. The only indication he yet lived was the uneven rise and fall of his breath."
"Andras turned with slow deliberateness to face Alexia, his face a dark stormcloud."

show andras displeased at edgeleft with dissolve

an "You and your cow lover have a lot to answer for."
an "I demand that he work, he does nothing for over a week. I ask for answers, and he feeds me useless platitudes."

show alexia 2 necklace shocked at midleft with dissolve

al "He’ll keep working, I know he will!"

show andras angry at edgeleft with dissolve

an "Why bother? He’s a lamed bull, useless to me now. Jezera’s little prank revealed just how brittle he is."

show andras displeased at edgeleft with dissolve

an "The miserable wretch won’t even struggle to save his own skin. "

show alexia 2 necklace concerned at midleft with dissolve

al "Please my Lord, he is just under a lot of stress-"

"Andras ignored her, nodding to the guard outside."

an "Bring him out to the courtyard and put him out of his misery."

show alexia 2 necklace angry at midleft with dissolve

al "{i}No!{/i}"

show andras smirk at edgeleft with dissolve

"Against her own instincts Alexia took a strong step towards the demon. Amused at her audacity, Andras’ lips twisted into a grin."

show alexia 2 necklace concerned at midleft with dissolve

an "...Come again?"

al "H-he’ll make you your weapons, I know he will. Please my Lord: give him another chance."

an "Why should I?"

"Alexia swallowed, bowing her head and staring at her toes. She had nothing to offer, and she knew it."

menu:
    "I’ll do whatever it takes to help him.":
        $ released_fix_rollback()
        an "How touching. You must really care about this moldy slice of beef."
        al "H-he’s my friend."
        an "That’s not how my dear sister tells it."
        "She did not dare to lift her gaze in that moment to meet his mocking smile. She heard him let out a self-satisfied laugh."
        
    "I’ll do... {i}anything{/i} you ask of me, Lord Andras.":
        $ released_fix_rollback()
        "Andras smirked. He stepped forward and took her chin in hand, lifting it up to look at him."
        an "Anything, hm?"
        an "Careful, dear. I might just make you forget why you came here in the first place."
        "He let the tension simmer in the air for a long moment before letting go of her and stepping back. He let out a self-satisfied laugh."
        
    "You at least owe him an opportunity to prove himself.":
        $ released_fix_rollback()
        an "I owe him nothing. He owes {i}me{/i} weapons."
        "Alexia lifted her chin and stared defiantly back at him."
        al "You’ll never get them from him if he’s dead."
        "Andras stared her down, his lips flattening. He let out a self-satisfied laugh."
        
an "...Very well. I’ll let him off the hook. On {i}one condition{/i}."
an "You have been his apprentice for some time, have you not?"

"A thrill of alarm ran up her spine."

al "I have... helped him in the forge on occasion."

an "And has your illustrious master taught you anything about the art of smithing?"

al "A… a bit, I suppose."

an "Good. Then I’ll make you a deal."

"He held up a lone finger, wagging it back and forth."

an "One. One sword, made from his forge, using his tools, using his methods. That’s all I ask in return for his freedom. You can do that for me, can’t you?"
an "If you can make me just one sword, I’ll forgive his insolence."

"She didn’t know what cruel game Andras was playing. There was a crafty grin on his face. His eyes were alight with malice."
"Alexia looked down at Greyhide, at his shuddering form as he struggled to pick himself up off the ground. The tremble at the base of her spine abated."
"She clenched her fists, set her jaw and looked Andras straight in the eye. She nodded."

al "One sword."

scene bg22 with fade
show alexia forge concerned at midleft with dissolve
show andras smirk at edgeleft with dissolve

"The forge was heated, the tools laid out. She had prepared everything as Greyhide had instructed." 
"Alexia stood at the anvil, staring blankly at the heavy hunk of iron in her hand. There was a pit in her stomach deep enough to swallow a mountain whole."

an "Are you watching closely, Greyhide?"

show greyhide sad at cliohnaright with moveinright

"Greyhide stood in anxious silence, his hands manacled together as he shifted back and forth on his hooves. His eyes were wide, his face clenched. He shared a long, frightened look with Alexia."

gh "You don’t have to… I’ll make the blades, I swear it. Just don’t-"

show andras displeased at edgeleft with dissolve

an "Shut up and let her get started."

show andras smirk at edgeleft with dissolve

an "This is for {i}your{/i} benefit, after all."

"Nothing for it now. She was committed. Alexia took in a deep breath, steeled herself, and placed the hunk of iron into the forge."

#story CG 1

"At the outset the quixotic nature of her endeavor became abundantly clear to everyone." 
"Alexia had never forged so much as a kitchen knife before, much less a sword. All she had to go by was observation and her own will to see this cruel farce through."
"Everywhere the threat of severe injury lurked, acting as a constant stress upon her mind.  The forge was blisteringly hot, such that Alexia had to squint to even look inside."

an "Ha! You see that? She took the iron out too early."

gh "..."

"Alexia, her cheeks cherry-red from both the heat and the taunting, placed the vaguely orange-red metal back into the forge’s flames. She waited this time till the metal was yellow-white, then pulled it free."

show alexia forge shocked at midleft with dissolve

al "{i}Ah!{/i}"

"Her grip on the metal was a bit too uneven with the tongs as she moved it to the anvil, and the heated hunk of iron slipped from her grasp, clattering to the ground. She had to almost leap out of the way to avoid catching it on her foot."

gh "{i}Hnnh{/i}!"

"Greyhide twitched. He stepped forward to help her, but Andras held an arm out to keep him back. "

an "Is this all that you’ve been teaching her, old man? Shameful. It's a wonder anything ever gets done in here."

show alexia forge angry at midleft with dissolve

gh "Let me help her."

an "No. You chose to do nothing, so nothing is what you’ll do. Blame your apathy for bringing us here."

gh "..."

"Greyhide’s eyes were wide like dinner plates. When Alexia met his gaze, he shook his head back and forth, as if urging her to stop." 
"Andras grinned and gestured for her to continue. Alexia set her jaw, and moved to retrieve the fallen metal from the floor."

show alexia forge neutral at midleft with dissolve

"It was so damned heavy and cumbersome. After heating it up again, she set the crooked hunk upon the center of the anvil. She kept a death grip on the hammer, struggling to lift the weight of even one of Greyhide’s smaller tools." 
"She tried to replicate the smooth form of the forge’s true master, lifting and lowering her hammer in the slow, methodical fashion she’d seen Greyhide do countless times before." 
"It was clumsy and inefficient. She struck the heated metal off-center, and sometimes missed it entirely. Sparks flew upwards in a haphazard stream."

an "A fine blade for a cripple! With how many kinks she’s added to it, you’re more likely to kill a man with a tablespoon."
an "I suppose she’d know a thing or two about ‘kinks’ though, hm?"

gh "{i}Hrrmh{/i}…"

an "Look: she’s not even scraping off the scale! Now that’s how you get a pitted sword."
an "What {i}were{/i} the two of you doing down in the forge all this time? Fucking?"

"Andras’ words were too pointed, {i}too{/i} goading. His mocking laughter came with an almost theatrical flair." 
"Alexia spared a glance in his direction, realizing his gaze wasn't even focused on her efforts, but on the seething Minotaur standing rigid at his side."

show alexia forge shocked at midleft with dissolve

"A sudden surge of sparks fountained up at her face, and Alexia jerked back reflexively to avoid them. Her grip loosened, and the hammer clattered out of her hands."

show alexia forge angry at midleft with dissolve

an "Enough."
an "This charade has gone on for too long. It's evident she couldn’t forge slag, much less a half-decent sword."

show andras displeased at edgeleft with dissolve

an "It was funny at first, but now it’s just gotten pathetic. It seems your teaching methods are as flaccid as your excuses, old man."

gh "...Hrmh."

show andras smirk at edgeleft with dissolve

an "You’ve failed to show her anything of substance, aside from your cock. You're no warrior, and you're certainly no teacher."
an "Are you really this worthless? Is there nothing you can give this woman?"

"Greyhide was shaking. Alexia had never seen his face in such a state with furrowed brow and grimacing expression. A dark, malicious grin grew on Andras’ face."

an "Death would be preferable to having a mate like you."

show bg22 with sshake

gh "{i}RAAAAAAAAAAAAH!{/i}"

"The roar of an enraged beast pierced the soot-filled air. Whatever further taunt Andras had been about to say was drowned out entirely. The furious bull flexed, clenching his hands as he strained against his manacles."
"{i}Snap{/i}. The chain links broke apart like brittle sticks. Freed from his bonds, Greyhide lowered his head and charged the Demon."

#story CG 2

scene cg955 with sshake
pause 3

"Andras did not even have time to raise his hands before the bull reached him. Greyhide cranked his arm back and smashed his fist into the Demon’s face."
"The blow connected against Andras’ jaw with the weight of a warhammer. Andras staggered, his head snapping to one side." 
"Greyhide did not give him space to recover, his fist connecting with his chin a second time and causing Andras to take a step back to steady himself."

scene cg956 with sshake
pause 3

"Greyhide tackled Andras to the ground, nearly goring him in the process with his horns. Planting himself atop him, he headbutted the demon as hard as he could into the ground."

hide andras with dissolve

"Alexia heard the loud {i}crack{/i} of Andras’ head as it hit the stone floor with earth-shaking force. She watched, flabbergasted as Greyhide assaulted the demon with the full might of his rage."

scene cg957 with fade
show alexia forge shocked behind cg957
pause 3

"Andras raised his hands to ward him off, but the raging Minotaur would not be dissuaded. Greyhide rained blows down on Andras, his fists rising and falling in a reckless repetition, all restraint disappeared from his face."

al "Greyhide!"

"He either didn't hear her, or didn’t listen. His brutal assault continued unabated. There was a crazed look in his eye. A look of madness."

#behind CG
show alexia forge angry behind cg957

al "{i}Greyhide{/i}!"

"It was only after several seconds of frenzied aggression that Greyhide slowed his assault, turning his head sharply to glare at Alexia. For a brief moment, she could not see the man beneath the beast."

#behind CG
show alexia forge concerned behind cg957

"He met her eyes. The longer they looked at each other, the more his anger drained away, and he became himself again. Greyhide looked away from her, wiping at his eyes with the back of his hand."
"He looked drained now, having spent himself in the frenzy. The bull stood up off Andras, his legs shaking with the effort. Beneath him, Andras wasn’t moving."
"There was a long silence. All that could be heard in the room was the crackling of the coals."

al "W-what have you-"
al "Is he…?"

scene bg22 with fade
show andras happy at edgeleft with dissolve
show alexia forge shocked at midleft with dissolve

an "{i}HA!{/i}"

"As if waiting for his cue, the demon sprang up."
    
an "Haha, yes! Now {i}that’s{/i} more like it!"

"Andras spat a wad of blood onto the ground next to him, rubbing blithely at his chin."

an "Good swing, old man!"

show alexia forge concerned at midleft with dissolve

"Greyhide, for his part, looked horrified. He stepped forward, extending his hands out towards the man he had been so hatefully beating upon mere moments before."

gh "I… Lord Andras, I am so-"

show andras angry at edgeleft with dissolve

an "Don’t you {i}dare{/i} try to apologize to me, fool."

show andras happy at edgeleft with dissolve

"The demon, still chuckling, picked himself up off the ground. Dark bruises and cuts checkerboarded his skin; Greyhide had {i}literally{/i} dented his face."
"Andras paid the injuries no mind. Already his hellish constitution was regenerating itself, the wounds fading even as he spoke."

an "Who would have thought a silly little comment like {i}that{/i} would have been what it took to finally wake you up? "
an "You always were slow on the uptake, beast."

"He reached out and took hold of Greyhide’s shoulder. Andras patted him on the back as if he were encouraging a trusted friend."

an "I’m glad we finally understand each other."

gh "I..."

show andras displeased at edgeleft with dissolve

an "Shut up. Listen closely now, because this is the first and last time I will ever say this."
an "I have no use for weaklings, still less for those who {i}pretend{/i}. You are who you are. Embrace it."

show alexia forge neutral at midleft with dissolve

"Andras cast a teasing smirk in Alexia’s direction. He winked at her."

show andras happy at edgeleft with dissolve

an "You owe me work, starting now. I expect to see twice the normal output by the end of next week, or your head’s back on the chopping block."

gh "Y-yes, Lord Andras…"

show andras displeased at edgeleft with dissolve

an "No more excuses, no more distractions. You bring me my weapons, or you face the consequences."
an "Do I make myself clear?"

gh "Yes, Lord Andras."

show andras happy at edgeleft with dissolve

an "Good. Find something to cut the Forgemaster’s manacles, and then get to work."

hide andras with moveoutleft

"Alexia stared at Andras’ retreating form as he strode from the forge, whistling to himself." 
"Her attention was drawn sharply back to the exhausted blacksmith as he sank to the floor. Alexia rushed over to him."

al "Are you okay?"

gh "Hmh… I should not have done that."

"Alexia choked out a laugh through her tears. She embraced him."

al " We should... talk. The three of us."

scene bg22 with fade
show rowan necklace concerned at edgeleft with dissolve
show alexia 2 necklace neutral at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve

al "So… that’s the situation."

ro "He wanted {i}you{/i} to forge the sword?"

show rowan necklace angry at edgeleft with dissolve

an "Andras always did have a sick sense of ‘justice.’"

gh "I am sorry for the trouble I have caused. For the danger I put you both in. "
gh "I would... understand if you hate me."

show rowan necklace neutral at edgeleft with dissolve

ro "I don’t hate you, Greyhide. The Twins have been meddling with us since the day we met."
ro "First Jezera, and now Andras… I don’t quite know what to make of it all."

show alexia 2 necklace angry at midleft with dissolve

al "There’s nothing to make of it. Andras used me to hurt Greyhide."

show rowan necklace concerned at edgeleft with dissolve

ro "I’m - uh… not sure that’s the whole story."

gh "The Twins do what they will. We are at their mercy. But I have no excuse."
gh "I have... grown close to you. To both of you. But I have betrayed that trust, come between mates."
gh "In my tribe, such an affront would warrant a fight to the death."

show alexia 2 necklace concerned at midleft with dissolve

al "Y-you don’t have to go {i}that{/i} far, Greyhide."

gh "My apologies, little one. But that is not your decision to make."

"Greyhide got down on one knee in front of Rowan, bowing his head to him."

gh "I am sorry, my friend. I have trampled upon your dignity."
gh "I will not fight you if you choose to take vengeance."

show rowan necklace happy at edgeleft with dissolve

ro "Stand up, Greyhide. I’d rather not have to look down on you while we talk."

show rowan necklace angry at edgeleft with dissolve

ro "I’ve felt the effects of Jezera’s drug firsthand. While I can’t say I was exactly thrilled to learn what you two have been up to, I can’t really blame you, given the circumstances."

"Greyhide glanced in Alexia’s direction. He let out a grunt of discomfort."

gh "I have a further confession to make."
gh "The drugs were… not the only cause."
gh "I have... feelings for Alexia. The feelings one has for a mate."

show rowan necklace shock at edgeleft with dissolve
show alexia 2 necklace shocked at midleft with dissolve

ro "Ah, I - uh… I see."

show alexia 2 necklace concerned at midleft with dissolve

al "Greyhide..."

gh "This changes nothing. I know what I have done, and I refuse to come between you."

"Greyhide turned and stared meaningfully into Alexia’s eyes."

gh "If it is a problem... then I will accept the pain of losing you. My feelings mean less to me than our friendship. "

"Alexia felt Rowan’s gaze turn to her. She couldn’t look him in the eye. Her throat grew thick."

ro "So… what do you think?"

al "I-I love you, Rowan. We are husband and wife and that will never-"

show rowan necklace angry at edgeleft with dissolve

ro "Stop. You know that’s not what I’m asking."

show rowan necklace concerned at edgeleft with dissolve

ro "What do you think about Greyhide’s confession?"

menu:
    "I… feel something for him, too.":
        $ released_fix_rollback()
        "Rowan stared at them both thoughtfully for a moment, then shrugged."
        show rowan necklace neutral at edgeleft with dissolve
        ro "It’s not like I didn’t already know."
        al "Rowan, I-"
        show rowan necklace happy at edgeleft with dissolve
        ro "You have my blessing."
        show alexia 2 necklace shocked at midleft with dissolve
        al "Huh?"
        ro "I can’t say I get what’s going on between you two, or even what I’m supposed to {i}feel{/i} about it exactly, but…"
        ro "I know what it feels like to be willing to sacrifice everything for someone you love."
        ro "If this is what you two truly want, then I suppose I’m okay with it."
        "Alexia’s heart leapt at the sight of Rowan’s reassuring smile."
        al "Are we-?"
        ro "We’re okay, Alexia."
        ro "...We’ll just have to see what this means, for {i}all{/i} of us, moving forward."
        show alexia 2 necklace happy at midleft with dissolve
        ro "For now, let’s take this one day at a time."
        gh "Th-thank you, friend Rowan."
        "Rowan extended his hand to Greyhide. The Minotaur stared at it for a long moment before taking it. Alexia felt her heart flutter with joy as the two friends shook hands."
        ro "Well, I hate to cut this reunion short, but I still have some paperwork to finish… something about a backlog of iron?"
        "Rowan nudged Greyhide’s elbow, smirking. The embarrassed bull rubbed sheepishly at the back of his neck."
        ro "What say we continue this conversation at dinner tonight, huh? Just the three of us."
        gh "I would like that."
        al "As would I."
        ro "Perfect, see you two then."
        "Rowan gave his wife a knowing wink as he made himself scarce. And just like that, the two lovers were left alone with one another."
        hide rowan with moveoutleft
        jump ghAlexiaFinaleSex
        
    "Let’s just forget this ever happened.":
        $ released_fix_rollback()
        "Greyhide let out a sigh of relief."
        gh "I would… like that. Very much so."
        ro "Barring some kind of trial by combat, I suppose your apology will have to do."
        gh "I-I will submit to whatever judgement you-"
        show rowan necklace happy at edgeleft with dissolve
        ro "Goddess fend Greyhide, I’m {i}joking{/i}."
        ro "I forgive you. Both of you. The best thing we can try to do from here is to move on, as friends."
        gh "You do me a great honour, Rowan. I will not forget this."
        "Greyhide rose to his feet and extended a hand out to Rowan. He smiled and took it."
        gh "And you, little one. You are… okay with still seeing me around the castle?"
        show alexia 2 necklace happy at midleft with dissolve
        "Alexia smiled and nodded."
        al "Of course, Greyhide. I trust you."
        "The bull blushed and glanced away, rendered bashful by her shy admittance."
        gh "I will try… to live up to that expectation."
        gh "...Friends?"
        "Alexia and Rowan shared a look. They smiled at one another."
        ro "Friends."
        al "Friends."
        $ greyhideRelationship = 'platonic'
        return
        
label ghAlexiaFinaleSex:

gh "Thank you, Alexia. For reminding me who I am. Even when I forgot."

"The Minotaur’s voice grew haggard as he looked away from her."
        
gh "You… you are the reason I yet live."
gh "There are no words… for what you mean to me. "

menu:
    "Tears in her eyes, Alexia leapt into Greyhide’s arms.":
        $ released_fix_rollback()
        show alexia 2 necklace concerned at midleft with dissolve
        "Overcome with emotion, Alexia’s footsteps quickened to a run."
        "Greyhide let out a startled grunt as she threw herself against him. She wrapped her arms around his thick frame and buried her face into his chest."
        al "Gods, I thought I was going to lose you!"
        "His big arms wrapped tight around her. She heard his deep, comforting voice whisper in her ear."
        gh "I am here, little one."
        "He was, thank all the stars in the sky. Gryhide held her off the ground so effortlessly, it was like she was floating. He engulfed her in his warmth."
        show alexia 2 necklace angry at midleft with dissolve
        al "D-don’t you {i}ever{/i} scare me like that again!"
        "Greyhide chuckled, a deep rumble in his chest that vibrated pleasingly through her body. She felt his arms pull her closer."
        gh "For you, I promise."
        show alexia 2 necklace happy at midleft with dissolve

    "“Seems like you’re stuck with me, huh?” She said with a smile.":
        $ released_fix_rollback()
        "Greyhide’s chuckle rumbled deep in his chest."
        gh "Believe me little one, it is the exact opposite."
        gh "Though, judging from the quality of your work today, you have much left to learn."
        show alexia 2 necklace shocked at midleft with dissolve
        "Alexia, caught off guard by his teasing tone, began to laugh."
        show alexia 2 necklace happy at midleft with dissolve
        al "You ungrateful {i}brute{/i}!"
        "The bull grinned at her, flashing her a rare glimpse of his flat teeth."
        gh "Heh."
        
    "Seeing his vulnerable look, Alexia opened her arms for a hug.":
        $ released_fix_rollback()
        al "Hey, come here."
        "The Minotaur hesitated, but eventually shuffled over into her arms. His fur felt warm in her grasp, soft and downy like a soothing blanket."
        gh "I am… unworthy of someone as lovely as you."
        al "Hush. No more of that."
        "He trembled, but her grip was firm, and he eventually settled into her arms."
        gh "I ought to be the one who comforts."
        al "Why? Because I’m small?"
        gh "...Yes."
        "Alexia chuckled, running her hands up and down his back."
        al "Well, tough luck. You’re big, and you could use a hug."
        
    "Taking his hand, she said “I will always be there for you, Greyhide.”":
        $ released_fix_rollback()
        show alexia 2 necklace neutral at midleft with dissolve
        "The bull’s eyes widened. He opened his mouth to say something, but the words would not come. He let out a nervous grunt."
        gh "Hrmh…"
        show alexia 2 necklace happy at midleft with dissolve
        al "I mean it."
        gh "I know. I am just... unused to hearing such things."
        "The bull squeezed her hand. It was warm and gentle."
        gh "I… will always be there for you, too."
        "Alexia smiled at Greyhide, and the Minotaur smiled back. A quiet lull fell between them, like the day they'd first met in the woods."

menu:
    "Lead him to the bed.":
        $ released_fix_rollback()
        pass
        
    "Part ways… for now.":
        $ released_fix_rollback()
        al "I could use a bath."
        "Greyhide chuckled. He rested his large hand on the top of her head, ruffling her hair."
        gh "Go, little one. There has been enough excitement for one day, I think."
        show alexia 2 necklace angry at midleft with dissolve
        al "More than enough to last a lifetime."
        "The bull smiled at her, and she smiled back. The two newfound lovers spent a long moment staring at one another, before Alexia blushed and looked away."
        show alexia 2 necklace aroused at midleft with dissolve
        al "I-I should go."
        gh "Be well, Alexia."
        "Alexia paused at the door, casting one last look at the tired blacksmith."
        al "…You too, Greyhide."
        $ greyhideRelationship = 'alexia'
        return

"Alexia turned her gaze towards his oversized bed. She nodded towards it, then shot Greyhide a searching look."
"Greyhide smiled and said nothing. He hefted her tiny frame, cradled her in his arms, and carried her over to it."
"Greyhide set her gently on the mattress, cautious, as if he thought she was a porcelain doll and was afraid to break her. Alexia giggled at his excessive display." 
"She ran her fingers across his chest, marveling at the feel of his taut muscles beneath the fur. His large hands roamed across her, gently undoing her clothing as she struggled to remove his loincloth."

#cg1
scene cg958 with fade
pause 2
show cg959 with dissolve
pause 2
show cg960 with dissolve
show greyhide neutral behind cg960
show alexia necklace naked aroused behind cg960
pause 3

"He was already hard. No amount of leather coverage could conceal that. No sooner had he exposed her breasts to the open air than a sizeable bulge had lifted the paltry fabric like a pillar upwards." 
"Curious, she took an experimental squeeze, and the bull let out a low grunt of pleasure."

gh "No fair."

al "Hehe, I wasn’t trying to be."

gh "{i}Hrmh{/i}… troublesome woman."

"She laughed at his bashful reticence. She was feeling rather nervous herself, all things considered. Her hands tremored as she at last managed to remove his loincloth, exposing his erect cock." 
"She reached out and touched it, wrapping her fingers tight around its length. She marveled for a moment at its heat, at the pleasant manner in which it throbbed to the beat of the beast’s heart."
"{i}Her{/i} beast. She smiled to herself, leaning forward to plant a kiss on the tip."

gh "Mmh… Alexia."

"His hand went to the back of her head, gently guiding her forward. She let him, lathering the head of his cock with love as she went. Her fingers clenched tight, and she began to stroke."
"It was slow… sensual, methodical; like Greyhide himself. She took her time, moving up and down his length with her tongue, savoring the taste of his skin. "
"Every kiss and lick and stroke was carefully timed, perfectly placed to elicit the precise reaction she wanted from him. She covered his cock in her saliva, marking him as hers."
"The Minotaur’s thick fingers ran through her hair, curling through her red locks with tender affection. Alexia smiled, suckling on his cockhead as she stared up into his eyes."
"She took him in both hands and leaned forward, planting trailing kisses across the top of his cock as she jerked him. He urged her onwards, his breath issuing forth in sharp retort to her illicit touch."
"Her touch trailed lower, tickling across the underside of his furry nutsack as she worshipped his masculinity."
"Alexia’s thighs shifted back and forth, struck with an itch that refused to be scratched. She was wet, {i}desperately{/i} so; her body yearned at the emptiness."

al "Greyhide…"
al "I want you inside me."

"The bull paused, his snout crinkling with concern."

gh "But… it will not fit."

"Alexia let out a breathy giggle, her attention refocusing on the dick that so captivated her. Her cheeks burned with her own audaciousness."

al "Still. I want to try."

"Greyhide stared at her, his lips curling upwards into a deep smile. There was a hunger in his eyes, the same hunger with which he’d first looked at her at that first, fateful dinner together."
"The two shared a smouldering look. Alexia’s heartbeat quickened as she felt his turgid cock twitch between her fingers. She sat up, exposing her narrow shoulders and frail form to his large, domineering frame."

al "...Well? What are you waiting for?"

"The bull took the playful bait. He let out a snort, rising up over her and planting his hands on either side of her shoulders, overwhelming her with his presence. The bed creaked from his weight."

#cg2
scene cg961 with fade
show greyhide neutral behind cg961
show alexia necklace naked aroused behind cg961
pause 3

gh "Are you certain?"

"The question was genuine, but it was spoken with the kind of sovereign eroticism that commanded - nay, {i}demanded{/i} - her attention. It was a choice, but the hot breath on her neck ensured that it was no real choice at all."
"Wordless, she nodded, biting her lip and spreading her legs as he angled himself against her. She shivered as his long length dragged across her stomach, leaving a trail of glistening precum on her skin."
"His weight was such that he could crush her just from laying down, yet he held himself at bay. All that strength, yet he did not use it. He held himself in check."
"Sometimes Alexia wondered if she was {i}crazy{/i} to find a Minotaur attractive, to find pleasure in the perversion of such bestial countenance." 
"But not now, not in this moment. At this moment, everything made sense."
"His massive, flat cockhead pressed against her entrance. She was lubricated, practically drooling down there. Alexia wanted him, she wanted him so {i}bad{/i}. The bull grunted, and leaned his hips into her."
"Oh… {i}oh{/i}, how slow it was. How delightfully it pushed against her labia, how slowly her lips yielded to the girth now stuffing her insides. He was barely past the tip, but already her hands were filled with bedsheet, clenching tight for dear life."

al "Aaa-{i}aaah{/i}!"

"He did not say a thing, her stallion. He merely shifted his hips back, then pushed in again. Deeper this time. The friction of his thick dick sliding into her sent Alexia into conniption fits."
"It was loud. The wet {i}squelch{/i} of her hungry pussy as she greedily tried to devour his length filled the air with every thrust. He’d barely cleared the head inside before she was twisting and gasping beneath him."
"People would think her mad. Hell, her own husband must think she was crazy! But when the bull bucked his hips forward, gave her the tantalizing taste of what a {i}real{/i} ride might feel like, such worries disappeared before sheer, aching pleasure." 
"The size… the size was the whole point! {i}Gods{/i} what a rush, what heart-pounding euphoria. It made her whole body blush, it made a song out of her breathless cries as he shifted back and forth, {i}back and forth{/i} again inside her."
"The bull was as entranced as she, his leathery face scrunching up into a mess of worried wrinkles. His breath came out in heavy bursts, open mouthed and haggard. It was everything he could do to hold himself back."
"He had wriggled over a quarter of his length inside her, but it was clear he wanted more. Every impulse in his mind had to be {i}screaming{/i} at him to take the plunge, to bury himself into her deepest folds and claim her as his mate."
"But… he didn’t. Her stallion held his will. He thrust and pushed and withdrew in precise (if trembling) movements. It only reinforced the faith she had in him, and the joyous feeling of their now-consummated union."
"She trusted him completely, and he rewarded her with toe-curling pleasure."

al "Aaah! {i}G-Greyhide{/i}!"

"Greyhide did not answer, he did not dare. Every iota of his concentration was bent upon holding himself back, from denying himself that most “base” of illicit pleasures. All it would take, was one, strong thrust..."
"She felt the thrumming of his heartbeat through the end of his wettened cock, it hammered with a weight so heavy she felt like he was already cumming inside her. Alexia’s eyes fluttered as she struggled to maintain some semblance of her composure."
"He thrust again, inches sinking deeper. It was like the whole world was entering her. Alexia opened her mouth to gasp, but the next thrust stole the very breath from her lungs."

al "{i}Aa-AAAH! Hnnnnngh{/i}!"

"Liquid electricity tickled up her spine. Her muscles clenched, her back lifting clear off the mattress in a feminine curl. A full-body orgasm swept over her helpless form like thunder rolling over the mountains. "
"For a brief moment, all she was was white. Her feminine juices squirted out, splashing both the bedsheets and the bull’s groin, nearly a foot away from the clenching culprit’s creaming pussy."

gh "{i}Hrrmph{/i}!"

"He growled so deeply that she felt the exhalation through his cock. It thickened inside her, and his hips paused in their movement. Alexia gasped, her eyes fluttering as her chest lifted and lowered in frantic pace."

al "O-oh G-G-{i}Gods{/i}…!"

"She covered her face in shame, her cheeks burning red with the sheer taboo of the delightful sensation. She was spitted on the end of him, mere putty in his hands."
"A large hand gently peeled away her own, exposing her face to him. Greyhide looked into her eyes, cupping her cheek - and the entire side of her face besides - with the palm of his hand."

gh "Are you… all right, little one?"

"She gaped at him. He… he really thought she was in {i}pain{/i}! Despite her crowning embarrassment, Alexia choked out a shaky laugh."

al "H-hurry up, you dummy. I’m {i}way ahead{/i} of you!"

"The bull smiled and obliged, thrusting into her with sudden force. Her cheeky bravado dissipated in an instant, replaced by a wordless, feminine whine. The wet {i}schlick{/i} of her pussy was the loudest sound of all."
"Desperate for support, she wrapped her hands around his thick forearm, and leaned her head against his hand. She squeezed her eyes shut as he rode her to completion."
"Finally, after who-knows-how many orgasms were squelched out of her stretched womanhood, Alexia felt Greyhide’s breathing shorten."
"His breath grew shallow as his hips began to piston in and out of her. The thrusts grew shorter, but deeper, adding an element of intensity to their final race to the finish."
"Who knew how much she’d taken of him… clearly not enough, as she had yet to feel his hips against her own. The only point of contact between them was the swelling cock in her nethers."
"But, judging from Greyhide’s sharp inhale, that was {i}more{/i} than enough."

gh "Mmrrh, {i}Alexia{/i}!"

"He snorted, grunted and came. The cumvein bulged within her, and she felt the first line of liquid hot love burst forth in a torrent within."

#cg2 - cum
show cg961 with sshake
show cg961 with sshake
scene cg962 with flash
show greyhide neutral behind cg962
show alexia necklace naked aroused behind cg962
pause 3

"A fountain of something hot and creamy spurted inside of her. Alexia gasped, feeling the weight of his seed in a real, tangible manner inside her belly." 
"The bull seemed to recognize the lack of space for his seed, as he immediately began to pull out. Such efforts proved too little, too late, as even before he could pull free spurts of pearlescent cum squeezed past the length of his shaft and squirted out onto the bedsheets."
"Alexia came hard, her body twitching as the breath stole from her lungs. At last the bull pulled free, dragging his shaft forward across her body as it fired its copious load upon her belly, her breasts and groin." 
"A few particularly energetic ejaculations even managed to reach her face and lips. She coughed and spluttered as she felt the sudden taste of something salty on her tongue."
"The two lay like that, panting and gasping in tune to one another until the cumming stopped, and then for some time after that. Both were exhausted, drained in body and spirit from all that had happened that day."
"But… they were together. They had both admitted their feelings, and they had resolved themselves to each other. That alone had made the whole ordeal worth it."

scene bg22 with fade
show greyhide neutral at center with dissolve

"After they’d cleaned up, Alexia dozed on Greyhide’s bed. The bull pulled his woolen blanket over her and let her rest." 
"He walked, a little unsteadily to his work stool, and sat down. Staring at her in the warm light of the forge, a soft smile graced his lips."

gh "Sleep well, little one."

$ greyhideRelationship = 'alexia'
return

##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################

label greyhide_finale_rowan:
    
scene bg54 with fade

"Rowan couldn’t sleep. He hadn’t gotten any real sleep in days."
"The usefulness of his idle thoughts had evaporated hours ago, yet his mind remained abuzz with needless worry."
"A few stolen hours here and there, a smattering of delirious submersions into unconsciousness, followed by sudden, rushing wakefulness." 
"He wondered if Greyhide was suffering from such aftereffects."
"Rowan grunted in discomfort at the thought of the Minotaur, turning over on his side and squeezing his eyes shut." 
"Everything was a distraction: distant sounds became a resounding chorus; the pale moonlight drew his wavering eye as it peeked through the window of his room."
"A signal horn blared from the wall, echoing with maddening volume through his bedroom window. Wordless chatter rose up from far below, voices and grunting, noise without end."
"And on and on it went."

show rowan necklace naked neutral at midleft with dissolve

if alexiaSeparateRoom == False:
    "Alexia was asleep at his side, her brow clenched in quiet - if not entirely restful - slumber. Rowan could not help but feel envious of how she managed to find any at all."
    "She’d complained of bad dreams of late, but that was better than his predicament."
    "Jezera’s drug had affected them both differently, and insomnia was his ‘gift.’ The toxin slowly working its way out of his system had stolen both his rest and his peace of mind."

"Rowan grunted and turned over, his mind turning like a rusty crank as he ruminated on all that had happened in the last week. Gods only knew what Greyhide thought of all this."

ro "..."

show rowan necklace naked angry at midleft with dissolve

ro "To hell with it, not like I’m getting any sleep anyway."

"Rowan threw off the covers and went to find his clothes. He couldn’t stand the silence any longer."

scene bg14 with fade
show rowan necklace angry at midleft with dissolve

"The tired hero hustled down the castle corridors, barely sparing a glance for those he passed. It was late, almost no one was about. He made straight for Greyhide’s forge."
"{i}A secret meeting. An illicit dalliance{/i}. Rowan shook his head angrily at the taunting voices in his head. His heart hammered heavy in his chest."

ro "I just need to know that he’s all right."

"The flimsy excuse fell flat in the empty corridor."

scene bg22 with fade
show rowan necklace concerned at edgeleft with dissolve

ro "Greyhide! Are you in there?"

"They hadn’t spoken in nearly a week. Rumors from the castle staff were he was refusing to leave his room for any reason, barring all visitors."
"Rowan sighed, leaning his head against the door when he got no response. He took a moment to collect himself, then pounded harder on the heavy door with his fist."

ro "...Come on, Greyhide. It’s me. "

show rowan necklace shock at edgeleft with dissolve

show orc soldier neutral at midleft with moveinright
show greyhide sad at midright with moveinright
show wild orc neutral at edgeright with moveinright

"Rowan stepped back from the swinging door in time to see a pair of guards march from the room. To his shock, a chained Greyhide followed in their wake."
"His hands were manacled together, his head bowed low. He hobbled forward at the urging of the Orcs, who tugged on his chains to make him go faster."

ro "What in the planes of chaos are you {i}doing{/i}?"

show rowan necklace angry at edgeleft with dissolve

ro "Unhand the Forgemaster at once! That is a direct order."

"The two Orcs paused in their march, exchanging uneasy looks. The lead piped up, scratching awkwardly at his cheek."

os "Uh… can’t, boss. Lord Andras’ ordered dis hisself."

show rowan necklace shock at edgeleft with dissolve

ro "{i}What{/i}?"

"Greyhide did not even lift his head at the sound of Rowan’s voice. His shoulders were slumped, his body language that of a beaten dog. He quietly shuffled past as the guards prodded him out of the room."

hide orc solder with moveoutleft
hide greyhide with moveoutleft

ro "Why in the world would Andras arrest his own blacksmith?"

wo "He sez the Forgemaster won’t work. Won’t talk about it neither. "
wo "So Forgemaster gits tossed in a cell till he talks."

show rowan necklace angry at edgeleft with dissolve

"The Orc shrank back from Rowan’s enraged expression."

wo "B-boss also sez you ain’t s’posed to-"

"Rowan spun on his heel and made straight for the dungeon. If he was quick, he could arrive before Greyhide got there."

scene bg8 with fade
show rowan necklace angry at edgeleft with dissolve

"Rowan sat brooding in the darkness of the cell. He’d managed to sneak past the guards and slip in undetected. Now it was all he could do to not pace the room."
"The sound of a lock unlatching caught his ear. He pressed his back tight against the wall towards the far corner of the cell, shrouded in darkness."
 
show greyhide sad at cliohnaright with dissolve
show orc soldier neutral at midleft with dissolve

os "In ‘dere, hurry up."

gh "..."

"The bull made no effort to resist, shuffling into the room and allowing the Orc to push him through." 
"The gaoler did not bother to undo his manacles before he slammed the door shut behind him. Greyhide let out a heavy sigh."

hide orc solider with moveoutright
show rowan necklace happy at midleft with moveinleft

ro "You’re not getting out of a talk with me {i}that{/i} easily."

"The bull jerked back, his eyes going wide as they swiveled the room. Rowan stepped out from the shadows."

show rowan necklace neutral at midleft with dissolve

ro "Relax. It's just me."

gh "..."

"Greyhide, realizing who it was, visibly deflated."

gh "Rowan."

"His looked away, a conflicted expression rising on his face."

gh "You should... not have come here."

show rowan necklace happy at midleft with dissolve

ro "Why? Afraid I might spring you?"

gh "Do not joke about such things."
gh "You... need to leave. You are in grave danger."

show rowan necklace neutral at midleft with dissolve

ro "So what else is new?"

gh "If... someone finds you here…"

show rowan necklace happy at midleft with dissolve

ro "Then I’ll tell them to take it up with the Twins."

"The bull let out a frustrated snort. He sat down on the floor, leaning his back against the wall."

show rowan necklace neutral at midleft with dissolve

gh "That is what I fear."
gh "You do too much. You always do too much for me."

menu:
    "Says you.":
        $ released_fix_rollback()
        gh "Yes. Says me. I am nothing. A blacksmith... a beast."
        gh "I do not deserve your help."
        show rowan necklace happy at midleft with dissolve
        ro "Yes, you do. But even if you didn’t, what does it matter?"
        ro "I’m here because I want to be."
        
    "I do it because I care.":
        $ released_fix_rollback()
        gh "You should not say such things. It will only hurt us both."
        ro "I’m only telling the truth."
        gh "{i}Hmh{/i}. Just… leave me here."
        show rowan necklace angry at midleft with dissolve
        ro "Not a chance in hell. "
        
    "Would you rather I did nothing?":
        $ released_fix_rollback()
        gh "Yes."
        show rowan necklace happy at midleft with dissolve
        ro "You know I’d never leave you behind like this."
        gh "You do not know... the effect you have on people."
        show rowan necklace concerned at midleft with dissolve
        gh "I was… content. I was at peace with- "
        gh "..."
        gh "You are wasting your time on me. There are… others more deserving."
        show rowan necklace neutral at midleft with dissolve
        ro "Maybe. That’s for me to decide."
        
    "You're my friend, of course I want to help.":
        $ released_fix_rollback()
        gh "Friends do not do what I have done."
        gh "I have ruined everything."
        show rowan necklace concerned at midleft with dissolve
        ro "The fact that I’m here proves you wrong."
        gh "The fact that you are here... only makes things worse."

"Greyhide sighed, a rough exhalation filled with emotion. He lowered his head and stared at the ground."

show rowan necklace concerned at midleft with dissolve
        
ro "What’s going on, Greyhide?"

gh "..."

"Rowan moved to take a seat at his side, but the bull jerked in place. He shook his head firmly back and forth. The strain in his voice bordered on panic."

gh "{i}Please… {/i}"
gh "Please, do not make this... harder for me."

show rowan necklace happy at midleft with dissolve

ro "Threatening me with a good time now, are we?"

show rowan necklace neutral at midleft with dissolve

"Greyhide did not so much as chuckle. The solemn look on his face caused Rowan to relent. He leaned back against the wall facing the Minotaur."

ro "...I think I can hazard a guess as to what’s happened."

gh "{i}Hrmph{/i}. Do not say it."

show rowan necklace angry at midleft with dissolve

ro "Andras finally figured out you’ve stopped working the forge, hasn’t he?"

gh "I have not stopped. I just…"

show rowan necklace neutral at midleft with dissolve

gh "I have failed him."

menu:
    "Good. The more the Twins fail, the better.":
        $ released_fix_rollback()
        gh "You cannot say such things."
        show rowan necklace happy at midleft with dissolve
        ro "This, coming from the man bound in chains."
        gh "I have nothing left to lose. You... have far too much."
        show rowan necklace concerned at midleft with dissolve
        ro "If you’re so worried about the Twins’ opinion, then why stop working?"

    "He’ll forgive you if you get back to work.":
        $ released_fix_rollback()
        gh "I am not so certain."
        ro "Andras only cares about results. This could easily just be a hiccup, a stumble in production."
        ro "Accidents happen. I can vouch for you."
        gh "This was no ‘accident.’ He... knows that."
        show rowan necklace angry at midleft with dissolve
        ro "If that’s the case, then why did you stop working?"

    "It’s not Andras who I’m worried about.":
        $ released_fix_rollback()
        gh "..."
        show rowan necklace concerned at midleft with dissolve
        ro "Greyhide come on, {i}talk to me{/i}. I’m your friend."
        gh "That is a mistake. A friend like me will only ever hurt you."
        show rowan necklace neutral at midleft with dissolve
        ro "That’s a patently untrue statement."
        show rowan necklace concerned at midleft with dissolve
        gh "..."
        ro "...Why have you stopped working?"
        
gh "You know why."

show rowan necklace happy at midleft with dissolve

ro "Indulge my curiosity, then."

show rowan necklace neutral at midleft with dissolve

gh "I have... shamed you. Hurt your wife. Betrayed your trust."

ro "You say it like {i}I{/i} had no say in the matter."

gh "Not real. Just the drug. Just… instinct."

menu:
    "Bullshit. What we have is special.":
        $ released_fix_rollback()
        gh "Rowan-"
        "Rowan shook his head back and forth."
        show rowan necklace angry at midleft with dissolve
        ro "No. Stop it. You don’t get to let yourself off the hook like that."
        ro "Nothing would have happened if there was nothing there in the first place."
        "Rowan rose to his feet and approached the Minotaur. Greyhide’s shoulders trembled. Rowan bent down, cupping the bull’s cheeks in his hands."
        show rowan necklace concerned at midleft with dissolve
        ro "Stop killing yourself over this. Over {i}us{/i}."
        "The gentle stroke of Rowan's finger on his face made the Minotaur grimace. He lifted his large eyes to look at Rowan, his gaze meeting his for the first time."
        
    "So what if it was? Didn’t we enjoy ourselves?":
        $ released_fix_rollback()
        gh "At the cost of your mate. At the cost of... harming you."
        ro "Do I look like I’m in pain right now, Greyhide?"
        gh "..."
        show rowan necklace happy at midleft with dissolve
        ro "Not everything has to be as complicated as you make it out to be."
        ro "We had our fun, and I don’t regret it for a second."
        ro "Whatever happens between me and Alexia, that’s for us to work out. You aren’t to blame for {i}my{/i} choices."
        "He lifted his eyes to look at Rowan, his gaze meeting his for the first time."
        
    "That's exactly why you shouldn’t beat yourself up about it.":
        $ released_fix_rollback()
        gh "If I do not do it... then who will?"
        ro "Greyhide, {i}we were drugged{/i}. We didn’t even know what was going on."
        gh "No... excuse. I lost control."
        show rowan necklace angry at midleft with dissolve
        ro "As did I. But if I have to live with that guilt, then so do you."
        show rowan necklace happy at midleft with dissolve
        ro "Besides… the castle would get awfully lonesome without you around."
        "Rowan reached out and put a hand on the Minotaur’s back. Greyhide lifted his eyes to look at Rowan, his gaze meeting his for the first time since he’d entered the cell."
        
gh "I-"

"The {i}snap{/i} of the lock unlatching behind Rowan yanked them both back to reality. The cell door opened wide, slamming against the outside wall from the force of the swing." 
"Rowan stood in a rush, pivoting on his heel to face his demonic opponent. He’d been expecting him to arrive sooner or later."

show rowan necklace angry at midleft with dissolve
show andras displeased at edgeleft with moveinleft

ro "Lord Andras."

"Andras said nothing for a moment, his eyes shifting back and forth between Rowan and Greyhide. He clutched what looked like a half-melted hunk of metal in his hand."

an "I was wondering if I’d find you skulking about."
an "So, my sister wasn’t lying. How bothersome. And now I’m left to clean up her mess."

gh "Do not…  blame Rowan. I-I made him come here-"

an "Oh, pipe down will you? You’ve played the part of the sobbing martyr for long enough."
an "You’d better have a good explanation for yourself, you old fool."

gh "..."

an "You are the castle Forgemaster, and we are at war. My men need weapons, and you are expected to provide them."

"Ignoring Rowan completely, Andras hauled Greyhide to his feet, thrusting the blade beneath his nose for him to inspect."

show andras angry at edgeleft with dissolve

an "Does {i}this{/i} look like a week's worth of work to you?"

gh "..."

an "Stop staring at the floor like a drooling imbecile and answer me."

gh "I… have no excuse."

show andras displeased at edgeleft with dissolve

an "Well that's too bad, old man. I’d at least be willing to hear it if you had one."

"Andras tossed the malformed blade at Greyhide’s hooves. It clanged with sharp retort against the stone floor."

an "There is no excuse for failure, none whatsoever."
an "I heard about my sister’s antics. I never would have thought something so inconsequential could have brought you to such a pathetic state."
an "You have served me well thus far, and I’d hate to lose a tool as useful as you to such a frivolous matter." 

"Andras cast a sidelong glance in Rowan’s direction, smirking at his grim expression discomfort."

show andras smirk at edgeleft with dissolve

an "What you do and who you do it with in your spare time is no concern of mine… up to and until it affects {i}me{/i}."
an "Consider this imprisonment your one and only warning: if you can’t fulfill your duties in this castle, then I will find someone who can."

gh "That would… probably be for the best."

show rowan necklace concerned at midleft with dissolve
show andras angry at edgeleft with dissolve

"Andras was just starting to turn away when his head snapped around. "

an "...What did you just say?"

"Greyhide refused to meet his eyes, keeping his gaze trained to the floor. His subservience only seemed to make him madder."

show andras displeased at edgeleft with dissolve

an "I see... so that’s how it is, then."

#story cg
show bg8 with flash
show rowan necklace shock at midleft with dissolve

gh "{i}Hurk{/i}!"

"Red energy surrounded Greyhide. A circle of profane magic grew above his head as Andras cast his torturous spell. The stoic Minotaur fell to one knee, his body shuddering."

an "So be it. Seeing as you no longer serve a purpose, I suppose there’s no use in keeping you around."

ro "{i}Greyhide{/i}!"

"After a few seconds Andras released his concentration, allowing the spell to dissipate. The Minotaur let out a gasp of air." 
"Without missing a beat Andras’ fists clenched and the magic returned, engulfing Greyhide in blinding agony once more."
"The bull let out a cry of pain, falling onto his hands and knees. His manacles jingled as he trembled from the force of the magic assault."

show rowan necklace angry at midleft with dissolve

ro "Stop! You’ve proved your point!"

show andras angry at edgeleft with dissolve

"Andras did not answer. He merely clenched his brow and redoubled his efforts."

show bg8 with flash
show rowan necklace shock at midleft with dissolve

"Another pulse, this time for nearly five full seconds. Greyhide let out a roar of pain, writhing on the ground in agony as the red circle of energy roiled and contorted about him."

gh "{i}HRRRRRAAAGH{/i}!"

show rowan necklace angry at midleft with dissolve

"Rowan stepped forward, his hand going to his sword."

ro "{i}ANDRAS!{/i}"

"Andras unclenched his hands, and the magic dissipated for good. Greyhide collapsed onto the ground, and lay still." 
"His body twitched, his muscles spasming as he whimpered in pain. The only indication he yet lived was the uneven rise and fall of his breath."
"Andras turned with slow deliberateness to face Rowan, his face a dark stormcloud."

show andras displeased at edgeleft with dissolve

an "A weakling. He’s a spineless weakling."
an "I tell him to work, he does nothing for over a week. I demand he give me answers, and instead he wallows in his own self pity."
an "I have given him every chance to redeem himself, but even {i}my{/i} patience has its limits."

"Rowan steeled himself. Despite his fear for Greyhide’s safety, he knew he couldn’t afford to show it. Not now." 
"There was only one angle he could play here.  Andras needed a different outlet, a distraction that could placate the demon’s childish need to put something in its place."

show rowan necklace neutral at midleft with dissolve

ro "My Lord… if I may?"

"Surprised by Rowan’s deferential tone, Andras glanced in the direction where his servant was pointing. The demon’s brow rose in surprise. He let out an annoyed grunt."

an "Take it. It’s practically scrap metal."

"Rowan picked his way past Greyhide’s prostrate body, making a point not to glance in his direction, lest the demon continue his torture. He picked up the discarded blade that was the sum total of the blacksmith’s efforts that week."
"He turned it about in the dim light, as if inspecting its contours. It was hardly a blade at all: more like a jagged hunk of flint a barbarian might wield." 
"Rowan ran his finger across the uneven edge to test its sharpness. His palms clenched around the ‘hilt’ to feel its uneven grip."

show rowan necklace happy at midleft with dissolve

ro "A fine weapon. I can see why it took so long to forge."

"Andras stared at Rowan for a long moment, then burst into mocking laughter."

show andras smirk at edgeleft with dissolve

an "Really, Rowan? {i}That’s{/i} your excuse?"

"But Rowan had already embraced the performance. He took a few practice swings with the unbalanced blade."

ro "If only he could make work of this quality every week. We’d never lose a battle."

an "{i}Hah{/i}! You absolute fool."
an "Fine. You’re so ready to defend him? Then put that slab of metal to use."
an "Since this is partially your fault anyways, I’ll make you a deal."

"Rowan didn’t know what game Andras was playing. There was a suspiciously crafty grin on his face."

an "If you can prove you can really use that “mighty blade” of yours to kill something of consequence, I’ll give this fool another chance."

show rowan necklace neutral at midleft with dissolve

ro "...And if I fail?"

show andras displeased at edgeleft with dissolve

an "You’ll be dead. And I’ll be in need of a new steward to go along with my new blacksmith."

show rowan necklace angry at midleft with dissolve

"Rowan looked down at Greyhide, at his shuddering form as he struggled to pick himself up off the ground. The Hero of Rosaria clenched his fists, set his jaw and looked Andras straight in the eye."

ro "Very well. I accept."

#courtyard BG
scene black with fade
show rowan necklace angry at midleft with dissolve
show andras smirk at edgeleft with dissolve

"The castle courtyard was cleared of traffic, the gates of Bloodmeen temporarily sealed. A small crowd of Orcs had gathered to watch, but Andras ordered them away."
"This was a private wager. One intended only for the contestants’ eyes."
"Across from Rowan stood a large, stone pot. Six feet in height and sealed shut with a heavy lid. It had taken a half dozen Orcs to lug the thing up from the depths of wherever Andras had been hiding it."

an "Are you watching closely, Greyhide?"

show greyhide sad at cliohnaright with moveinright

"Greyhide stood in anxious silence, his hands manacled together as he shifted back and forth on his hooves. His half-forged sword was clenched tight in Rowan’s hands."

gh "You don’t have to… I’ll make the blades, I swear it. Just don’t-"

show andras displeased at edgeleft with dissolve

an "Shut up and let's get started."

show andras smirk at edgeleft with dissolve

an "This is for {i}your{/i} benefit, after all."

ro "So what am I supposed to be facing anyway? An oversized flower pot?"

an "A Mandragorgon."

"Andras waved his hands, magic spilling freely from his fingertips and pouring into the pot. There was a rumbling, and then something terrible burst out, slithering from the pot lid like a snake from a rodent burrow."

#story CG

"It was hideous, vaguely plantlike yet unnervingly alien in shape. It’s long, centipede-like carapace stretched a dozen feet in height like the trunk of an overthin tree."
"From its main stem sprouted many waving tentacles of varying thickness and length. Sickly brown in color, like the bark of a diseased tree." 
"Dozens of long, sticky filaments tipped with a dewy substance jutted forth from the tentacles like innumerable fingers on a hand."
"Perched at the very top of its pungent-odored body was a wide, lipless maw, like that of a flytrap. Long, needle-thin teeth sprouted from its mouth, wiggling back and forth nervously in the air."
"It had no eyes, but Rowan could feel it {i}looking{/i} at him all the same."

show rowan necklace shock at midleft with dissolve

ro "What in Kharos’ flaming hellscape is {i}that{/i}?"

an "I already told you, fool. A Mandragorgon, from the far elven jungles."
an "They usually only feast on the giant insects that buzz around the rotting treetops… but thanks to my help, this one will make an exception. Just for you."
an "Best of luck, hero."

"The thing wiggled and wobbled back and forth in place, it’s stringy tentacles reaching out towards the hero with disturbing intent. It seemed to… {i}sense{/i} him."
"Greyhide’s eyes went wide. He shared a long, frightened look with Rowan. The Hero of Rosaria set his jaw, clenched tight the blade in his hand, and charged the creature."
"He was immediately beset by its writhing limbs. The Mandragorgon’s tentacles were slow, sluggish and sedated, but far too numerous to simply avoid." 
"He dodged the first few, but soon found himself surrounded as it responded like a trap slowly collapsing in on itself." 
"One swing of the warped blade in his hand told him he’d be lucky if it didn’t break off in his grasp, Rowan hacked at one of the tentacle branches that got too close, but recoiled when the blade failed to cut through."

an "Is this the best steel you can make, old man? Shameful. It's a wonder you ever bothered to pick up a hammer."

gh "..."

"The tentacles were coiling in around Rowan. Each sticky filament that found errant purchase on his clothing clung fast and would not let go." 
"He had no hope of freeing himself from the creature’s clutches, to try to fight it one branch at a time was a slow death by inches. He had to take a chance and strike at the body."

gh "Please stop this. You have... made your point."

an "No. You still don’t understand."

"Desperate now to reach the central stalk, Rowan pressed forward. It was getting harder and harder to move. Every step was like climbing up a steep slope, the tendrils were surprisingly strong, sticky and immobile once locked to him."
"Seeing an opening, he slashed with all his might against the rubbery brown carapace. The blade barely broke the outer layer, slicing only a half inch deep before lodging itself into the trunk."
"Rowan tugged and strained against the hilt, but could not pull it free. His feet left the ground as he felt the slow drag of the tentacles pulling him upwards. Greyhide’s fists clenched as he strained against his manacles."

gh "Enough. {i}Enough{/i}! It is my blade that failed, not him."
gh "Punish me. I have done wrong… but let him go."

an "No."
an "This is what happens when you let braver men fight your battles for you."

"Andras’ words were too pointed, {i}too{/i} goading. His mocking laughter came with an almost theatrical flair. But Rowan couldn’t focus on that, right now. He had to free himself."
"He kicked and struggled, but the sticky filaments would not let go. He tried to reach for his dagger, but his arms had been rendered immobile."

show rowan necklace angry at midleft with dissolve

ro "Damn it!"

"The plant was pulling him up its length, coiling ever tighter around him with its myriad appendages. If he didn’t free himself soon, he’d be lifted to the top of the tree… up towards its hideous mouth."

gh "{i}Let me help him.{/i}"

an "No."

gh "{i}Hrrmh…{/i}"

an "What’s wrong? Having second thoughts? Then {i}do{/i} something about it, old man."

gh "..."

an "You’re not going to lift a finger. Admit it: you’re too much of a coward."
an "You’d rather just sit back and watch. You're no Forgemaster, and you're {i}certainly{/i} no man. "

"Greyhide was shaking. A dark, malicious grin grew on Andras’ face."

an "Death would be preferable to having a mate like you."

#courtyard BG
show black with sshake

gh "{i}RAAAAAAAAAAAAH!{/i}"

"Whatever further taunt Andras had been about to fling was drowned out entirely. The furious bull flexed, clenching his hands as he strained against his manacles."
"{i}Snap{/i}. The chain links broke apart like brittle sticks. Freed from his bonds, Greyhide lowered his head and charged the Demon."

scene cg963 with sshake
pause 3

"Greyhide cranked his arm back and smashed his fist into the Demon’s face. The blow connected against Andras’ jaw with the weight of a warhammer. The demon staggered, his head snapping to one side." 
"Greyhide did not give him space, his fist connecting with his chin a second time and causing Andras to take a step back to steady himself."

hide andras with dissolve

scene cg964 with sshake
pause 3

"Greyhide tackled Andras to the ground, nearly goring him in the process with his horns as he headbutted the demon as hard as he could into the ground. Rowan heard the loud {i}crack{/i} of the demon’s head as it hit the stone floor with earth-shaking force."

scene cg965 with fade
show rowan necklace angry behind cg965
pause 3

"Andras raised his hands to ward him off, but the raging Minotaur would not be dissuaded. Greyhide rained blows down on Andras, his fists rising and falling in a reckless repetition, all subtlety and restraint gone from his face."

ro "Greyhide!"

"He either didn't hear him, or he didn’t listen. His brutal assault continued unabated."

ro "{i}Greyhide!{/i}"

"It was only after several seconds of frenzied aggression that Greyhide slowed his assault, turning his head sharply to glare at Rowan. For a brief moment, he could not see the man beneath the beast."

ro "...A little help?"

"The crazed look in his eye faded for a moment, then narrowed upon the Mandragorgon. Greyhide let out a snort, then charged it."
"His efforts to free Rowan turned out to be unnecessary. Whatever fell power Andras had been feeding it dribbled away. All of a sudden, the Mandragorgon went limp." 
"By the time Greyhide’s horns connected with its trunk, the filaments were already coming undone. The thing shuddered, then released him."

scene black with fade
show rowan necklace shock at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve

ro "{i}Gah{/i}! Shit!"

"Greyhide managed to catch him as he fell. The bull set him down gently on the ground, fussing over him like a worried wife."

show rowan necklace concerned at midleft with dissolve

gh "Are you... all right?"

ro "Sticky. But… yes."

show rowan necklace happy at midleft with dissolve

ro "Thanks for the rescue."

show rowan necklace concerned at midleft with dissolve

"Rowan cast a worried glance in the direction of the demon lord lying flat on his back. He wasn’t moving."

ro "...Gods, you really hit him."

show andras happy at edgeleft with dissolve

an "{i}HA!{/i}"

"As if waiting for his cue, the demon sprang up."

an "Yes! Now {i}that’s{/i} more like it! Haha!"

"He spat a wad of blood onto the ground next to him, rubbing blithely at his chin."

an "Good swing, old man!"

"Greyhide looked horrified. He set Rowan gently down then rushed over to the demon lord."

gh "I… Lord Andras, I am so-"

show andras angry at edgeleft with dissolve

an "Don’t you {i}dare{/i} try to apologize to me, fool."

"The demon, still chuckling, picked himself up off the ground. He was black and blue, his face a tattered mess of cuts and bruises." 
"Greyhide had {i}literally{/i} dented his face. But already his hellish constitution was regenerating itself, the wounds fading even as he spoke."

show andras happy at edgeleft with dissolve

an "Who would have thought a silly little comment like {i}that{/i} would have been what it took to finally wake you up? "
an "You always were slow on the uptake."

"He reached out and took hold of Greyhide’s shoulder."

an "I’m glad we finally understand each other."

gh "I..."

show andras displeased at edgeleft with dissolve

an "Shut up. Listen closely to me now, because this is the first and last time I will ever say this."
an "I have no use for weaklings, still less for those who {i}pretend{/i}. You are who you are. Embrace it."

"Andras cast a teasing smirk in Rowan’s direction. He winked at him."

show andras smirk at edgeleft with dissolve

an "You owe me work, starting now. I expect to see twice the output by the end of next week, or your head’s going back on the chopping block."

gh "Y-yes, Lord Andras…"

show andras displeased at edgeleft with dissolve

an "No more excuses, no more distractions. You work, or you die. Do I make myself clear?"

gh "Yes, Lord Andras."

show andras happy at edgeleft with dissolve

an "Good. Steward, find something to cut the Forgemaster’s manacles and get back to work."

hide andras with moveoutleft

"Rowan stared at Andras’ retreating form as he left the courtyard. Greyhide, exhausted, sank to the ground. Rowan glanced back over his shoulder at the placid, swaying form of the Mandragorgon."

ro "I guess it was harmless, after all."

gh "Hmh… I should not have done that."

show rowan necklace happy at midleft with dissolve

ro "What are you talking about? Seeing you beat Andras into the ground damn near made this all worth it."

gh "Heh."

"Greyhide let out a chuckle, a quiet rumble in his chest. Rowan smiled at the pleasant sound. He put his hand on the bull’s shoulder."

ro "I think it’s high time the three of us had a talk."

scene bg22 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace concerned at edgeleft with dissolve
show greyhide sad at cliohnaright with dissolve

ro "So… that’s what’s happened."

al "Gods, what a mess."

gh "I am sorry for the trouble I have caused. For the danger I’ve put you in. "
gh "You are my friends, and my actions have hurt you both."
gh "I… would understand if you hate me."

show alexia 2 necklace neutral at edgeleft with dissolve

al "Don’t be ridiculous, Greyhide. You weren’t the one who drugged us."

show rowan necklace angry at midleft with dissolve

ro "You also didn’t sic a mutant plant on me for the fun of it."

gh "The Twins do what they will. We are at their mercy. But I have no excuse."
gh "I have... grown close to you. To both of you. But I have betrayed that trust, come between mates."
gh "In my tribe, such an affront would warrant a fight to the death."

show rowan necklace concerned at midleft with dissolve

ro "I don’t think we need to get {i}that{/i} crazy."

gh "My apologies, Rowan. But I am not referring to you."

"Greyhide got down on one knee in front of Alexia, bowing his head to her."

gh "I am sorry, little one. I never intended any of this."
gh "I will not fight you if you choose to take vengeance."

show alexia 2 necklace angry at edgeleft with dissolve

al "Oh for goodness sake, Greyhide. Get up."

show alexia 2 necklace neutral at edgeleft with dissolve

al "W-while I will admit, I was not happy to learn what’s gone on between you two, this wasn’t malicious, or planned. "
al "You two were out of your minds on Jezera’s drug. Having felt the effects of it myself, I can’t exactly blame you for giving in."

"Greyhide glanced in Rowan’s direction. He let out a grunt of discomfort."

gh "I have a further confession to make."
gh "What you say may be true. But the drugs were not the only cause."
gh "I have... feelings for Rowan. The feelings one has for a mate."

show alexia 2 necklace shocked at edgeleft with dissolve
show rowan necklace shock at midleft with dissolve

al "Oh."

show rowan necklace concerned at midleft with dissolve

ro "Greyhide..."

gh "This changes nothing. I know what I have done. And I refuse to come between you. "

show alexia 2 necklace concerned at edgeleft with dissolve

"Greyhide turned and stared meaningfully into Rowan’s eyes."

gh "If it is a problem... then I will accept the pain of losing you. My feelings mean less to me than our friendship."

"Rowan felt Alexia’s gaze upon him. A nervous blush rose upon his cheeks."

show alexia 2 necklace neutral at edgeleft with dissolve

al "Well? What do you have to say for yourself?"

ro "Alexia, you’re my wife. You know that I love you-"

show alexia 2 necklace angry at edgeleft with dissolve

al "None of that. Tell me the truth, Rowan."

show alexia 2 necklace concerned at edgeleft with dissolve

al "What do {i}you{/i} want?"

menu:
    "I don’t know, I care about him.":
        $ released_fix_rollback()
        "Alexia let out a long-suffering sigh."
        al "Then I guess I have my answer."
        ro "Alexia…"
        al "It’s okay, Rowan."
        al "I can’t say I fully understand this, or even what I’m supposed to {i}feel{/i} about it, but…"
        show alexia 2 necklace happy at edgeleft with dissolve
        al "I will just have to make the effort to understand."
        gh "What do you mean?"
        al "It’s clear my husband cares about you, Greyhide. And for that matter, I care about you too."
        show alexia 2 necklace concerned at edgeleft with dissolve
        al "Though, maybe a little less {i}enthusiastically{/i} than he does."
        show alexia 2 necklace neutral at edgeleft with dissolve
        al "If this is what you two truly want, then I suppose I’m okay with it."
        ro "Are we-?"
        al "We’ll get through this, Rowan."
        al "What all this means for us… we’ll just have to see. Just take it one day at a time."
        show rowan necklace happy at midleft with dissolve
        ro "You are still my wife."
        al "Of course. The real trick here is figuring out what {i}you two{/i} are."
        gh "I swear, I will never come between you and your husband, little one."
        show alexia 2 necklace happy at edgeleft with dissolve
        al "I know, Greyhide."
        al "I’m... glad you’re the man my husband chose."
        "Alexia opened her arms, beckoning him for a hug. The Minotaur hesitated, then stepped into her grasp. A smile flitted across Rowan’s face as he watched the two friends embrace."
        al "I think maybe…  you two could use some time to talk."
        al "Maybe tonight we could all have dinner together? Just the three of us?"
        ro "I’d love to."
        gh "As would I."
        al "Good. Then… I guess this is goodbye, for now."
        hide alexia with moveoutright
        "Alexia shot her husband a soft smile as she passed. And just like that, the two lovers were left alone with each other."
        jump ghRowanFinaleSex
        
    "Let’s just forget this ever happened.":
        $ released_fix_rollback()
        "Greyhide let out a sigh of relief."
        gh "I would… like that. I would like that very much."
        al "I think I would too."
        al "I don’t know what else to say. I guess... I forgive you?"
        gh "You do me a great honour, Alexia. I will not forget this."
        "Greyhide rose to his feet and extended a hand out to Alexia. After looking at it for a long moment, she took it."
        gh "And you, Rowan. You are… okay with still seeing me around the castle?"
        show rowan necklace happy at midleft with dissolve
        "Rowan reached out and patted the gentle Minotaur on the shoulder."
        ro "You don’t even have to ask that question, my friend."
        show alexia 2 necklace happy at edgeleft with dissolve
        al "Really, I wish you’d stop apologizing."
        al "Whatever else you think you are, Greyhide: you’re a good man."
        gh "I will try… to live up to that expectation."
        gh "Friends?"
        "Rowan and Alexia shared a mutual look. They smiled at one another."
        ro "Friends."
        al "Friends."
        $ greyhideRelationship = 'platonic'
        return

label ghRowanFinaleSex:

gh "Thank you, Rowan. For reminding me who I am. Even when I forgot."

"The Minotaur’s voice grew haggard as he looked away from him."

gh "You… you are the reason I yet live. "
gh "There are no words… for what you mean to me."

menu:
    "Sensing Greyhide’s melancholy, he cracked a bad joke.":
        $ released_fix_rollback()
        ro "...No words for it?"
        ro "What about ‘sex,’ ‘dick,’ or ‘balls?"
        show rowan necklace concerned at midleft with dissolve
        ro "...Maybe ‘orgasm?’ Nah, too formal."
        show rowan necklace happy at midleft with dissolve
        "The tension broke. Greyhide let out a low, rumbling chuckle as he wiped at the corners of his eyes."
        gh "Heh."
        gh "At least you know how to make me smile."
        ro "It’s just a shame we’re both terrible at wordplay."
        gh "I would not say that. Your choices were not far off from the mark."
        "The bull put his arms around him, engulfing him in his body heat."
        gh "I… I am not as well versed in these matters as you are. But you ignite that curiosity in me."
        gh "...I have not felt such desire in a very long time."
        
    "“You are the world to me.” Rowan whispered.":
        $ released_fix_rollback()
        "The shy Minotaur stared at him, his lower lip trembling."
        gh "You… I do not deserve y-"
        "Rowan kissed him, silencing any further self-deprecation. Greyhide sighed and leaned into it, his eyes sliding closed. They stayed like that for a small eternity."
        ro "I’m glad you’re here."
        "Greyhide stroked the side of Rowan’s face with his thick finger. It was soft. Comforting."
        gh "I would not be anywhere else."
        gh "You… are something special, Rowan."
        gh "No matter what others say. You are the most... remarkable thing in this castle."
        gh "Maybe anywhere."
        "Rowan smiled. He leaned in to kiss him again. The bull accepted it, his heavy breath tickling Rowan’s nose with warmth."
        
    "Rowan’s composure broke, and he threw his arms around him.":
        $ released_fix_rollback()
        show rowan necklace concerned at midleft with dissolve
        ro "Don’t you {i}ever{/i} do something stupid like that again, you suicidal bastard."
        "Rowan buried his face in the bull’s chest, feeling the heat of his fur on his face. Greyhide, taken aback, simply stood there for a moment. His hands awkwardly encircled Rowan."
        gh "I did not mean to worry you."
        show rowan necklace angry at midleft with dissolve
        ro "Well you did."
        "The bull let out a sigh, holding the small human close. Rowan’s breathing - for a brief moment - grew uneven and shaky."
        show rowan necklace concerned at midleft with dissolve
        ro "You know what Andras is capable of. You could have been killed."
        gh "{i}You{/i} could have been killed, too."
        show rowan necklace angry at midleft with dissolve
        ro "I can handle myself. You are-"
        gh "Bigger than you."
        show rowan necklace neutral at midleft with dissolve
        ro "-And also too kind hearted by half."
        gh "Heh. I could say the same of you."
        "Rowan blinked away something wet from his eyes. He let out a soft laugh."
        show rowan necklace happy at midleft with dissolve
        ro "Well… I guess we’re perfect for each other, then."
        "Their brief quarrel resolved, the two lovers clung to each other for a time, enjoying the feel of one another’s presence."
        
    "He playfully nudged the Minotaur’s shoulder. “Hey, no tears.”":
        show rowan necklace concerned at midleft with dissolve
        gh "That is a tall order to ask of me, Rowan."
        show rowan necklace concerned at midleft with dissolve
        ro "It all worked out in the end, didn’t it?"
        gh "Only thanks to you. "
        show rowan necklace happy at midleft with dissolve
        ro "The bruises on Andras’ face would beg to differ."
        gh "-As would the Mandragorgon, I suppose."
        show rowan necklace angry at midleft with dissolve
        ro "Hey, I had him right where I wanted him!"
        gh "Heh. Of course you did."
        show rowan necklace happy at midleft with dissolve
        ro "Now you’re gonna make {i}me{/i} cry. My pride as a man is at stake here!"
        "Greyhide chuckled."
        gh "If you say so."
        
menu:
    "Lead him to the bed.":
        $ released_fix_rollback()
        pass
        
    "Part ways… for now.":
        $ released_fix_rollback()
        ro "I could use a bath."
        show rowan necklace angry at midleft with dissolve
        ro "...Maybe several. That Mandragorgon stank to high heavens."
        "Greyhide chuckled. He pulled Rowan into a tight hug and held him there for a long moment."
        gh "There has been enough excitement for one day, I think."
        show rowan necklace happy at midleft with dissolve
        ro "You say that, but at this point I wouldn’t be surprised if Daenara herself showed up riding a dragon."
        "The bull smiled, and he smiled back. The two newfound lovers spent a long moment staring at one another, before Rowan let out a soft sigh."
        show rowan necklace aroused at midleft with dissolve
        ro "I don’t want to leave."
        gh "Go. We will see each other again soon."
        "Rowan paused at the door, casting one last look at the tired blacksmith."
        show rowan necklace happy at midleft with dissolve
        ro "...See you soon, Greyhide."
        $ greyhideRelationship = 'rowan'
        return

"Rowan glanced in the direction of Greyhide’s oversized bed. The two shared a look. A soft smile broke out on Rowan’s face."

ro "...Just like old times, huh?"

gh "Except this time, I am not drunk."

ro "Would you rather be?"

"Greyhide shook his head, planting his hands on Rowan’s shoulders. He was so much bigger, a veritable giant towering over him. The bull leaned in and whispered in his ear."

gh "No. I would prefer to remember this. Every moment."

"He hefted Rowan up and into his arms, carrying him over to the bed."

#cg1
scene cg966 with fade
show rowan necklace naked behind cg966 
show greyhide neutral behind cg966 
pause 3

"Rowan fell back onto the covers, his cheeks turning beet red as the Minotaur towered over him. Almost unconsciously, his eyes drifted down towards the bulging strain in his loincloth."

ro "You planning on showing me your friend?"

gh "No."

"Greyhide put his hand’s on Rowan’s hips, his large fingers pulling down his pants and exposing his own erection. It was only once the bull advanced upon him on the bed that he realized what he was doing."

gh "Not this time. Not yet."

show rowan necklace naked aroused behind black

ro "O-oh."

"Greyhide leaned forward, nudging the hero’s erection with his snout. He took in a long, deep sniff, sending warm goosebumps up Rowan’s stomach from the heavy exhale across his skin."

gh "You are handsome. A wonder."

"Greyhide puckered his lips and kissed it, his eyes sliding shut as he began to nudge his cock back and forth with his mouth. The stimulation was thrilling and exotic, a peculiar yet erotic sensation that sent Rowan’s heart pumping in his chest."
"He kissed the tip, his lips easily engulfing the whole head in the motion. Rowan leaned his head back and moaned as he felt the warm, wet passage form an unintentional suction on his cockhead."

ro "Aaah, {i}damn{/i}."

"Greyhide chuckled, a deep rumble that resonated inside his mouth, down Rowan’s shaft and vibrated down to his testicles. The bull was unwittingly giving him an astonishing - if supremely unconventional - blowjob."
"After what felt like an age of agonized teasing, the bull finally engulfed Rowan’s erection with his mouth. In one smooth movement, he had the whole of him in his maw."
"The feeling was unlike anything he had ever experienced. In the space of one, smooth movement the bull had effortlessly throated the whole of Rowan’s cock. It was engulfed in the bull’s mouth, surrounded by his eager sucking."
"The bull’s long, thick, tongue ran down the length of his shaft, even curling fast around his balls. Rowan gripped the bedsheets for dear life, his face clenching as Greyhide eagerly massaged his privates from every conceivable angle."

ro "Ooof- {i}fuck{/i} you’re so good."

"There was a {i}pop{/i}, and suddenly, Rowan’s twitching cock was exposed to the open air. Compared to the warm, wet home it had found mere moments ago, the breeze felt downright chilly. His dick was covered in Greyhide’s saliva."

gh "I like your taste."

ro "I-I can {i}tell{/i}!"

gh "Heh. Your blush is sweet, I enjoy seeing you like this."

ro "Don’t stop, Greyhide."

"The horny Minotaur nodded, leaning forward to lick up the full length of Rowan’s shaft. He groaned in pleasure as the bull returned to his sucking, leaning down to nuzzle his testicles before lathering him once more in bullish love."
"Rowan’s fingers curled through his mane, running across the stiffness of his horns, through the downy fur of his mane. He could do little but hold on as the bull redoubled his efforts."
"His fingers clenched tight against the back of Greyhide’s head as the bull caught him in his oral vice once more, milking his cock in short, swift compressions. The pull was so intense, it was as if he was balls deep in another orifice entirely. Someplace… tighter."
"Greyhide sucked and licked, leaning forward to kiss the base of Rowan’s groin even as his tongue slathered him in a viper’s coil tight around his manhood. The sensation was too much, Rowan practically had to {i}shove{/i} him off his nethers."

ro "W-wait! {i}Wait{/i}!"

"He got up, knees shaking, and spun around turning his flank to the randy Minotaur. Greyhide’s eyes trailed across the bare expanse of Rowan’s shapely ass, his eyes filled with animalistic lust."

ro "I want you to feel good too."

gh "You are… too good to me."

ro "Shut up and climb on."

#cg2
scene cg967 with fade
show rowan necklace naked aroused behind cg967
show greyhide neutral behind cg967
pause 3

"Greyhide obliged, stripping off his loincloth as Rowan shot him a heated stare. He clambered up onto the bed, draping himself over the smaller human with a pleasing, masculine weight on his back."

gh "{i}Mmh.{/i}"

"The bull angled his hips and positioned himself behind Rowan, adopting a dominant angle. Rowan shivered when he felt the bull’s furry groin press against his rear."
"Greyhide’s painfully erect cock jutted forth beneath him, stretching out farther than his own hardness did. Rowan might have been envious… but in reality, the tingly feeling in his stomach was that of breathless excitement."
"His thighs were already lubricated by Greyhide’s oral, all it took was for him to press them together, and in an instant he had his cock sandwiched between them. There was a warm, pulsing feeling between his legs, warmer even than the bull’s body atop him."
"Rowan reveled in the ticklish feel of Greyhide’s mammoth length as trailed across the underside of his balls. He began to thrust, rutting his hips against Rowan’s in a slow, sedated back and forth."
"Rowan rocked back and forth, reveling in the teasing pace. His own cock twitched and thickened at the stimulation, the illicit feeling of Greyhide’s heartbeat thumping between his legs as he thrust past the airtight split of his well-lubed thighs."
"Greyhide’s thick biceps wrapped around his lover, crushing him tight against his chest.  He felt the trailing heat of his breath at his neck, at his ear. It was heavy, almost strained."

gh "{i}Rowan…{/i}"

"His name, spoken with a kind of hopeless longing, made Rowan’s heart hammer even harder in his chest. It seemed to take everything Greyhide had to hold himself back, but hold himself back he did."
"Rowan trusted him in a way he had rarely felt with another. All this size, all this might… and yet he was as comfortable as could be, safe in his firm grip and slow thrusts. This wasn’t a beast taking base pleasure from a disposable partner… this was two lovers reveling in one another’s company."
"As if to underscore that point, Greyhide hand trailed down, running across and gently squeezing Rowan’s hip before reaching below it. He pinched Rowan’s prick between his thumb and forefinger, and - with a gentleness that belied his strength - began to jerk him off."
"Rowan moaned, caught between the potent sensation of Greyhide’s bulging bullcock sliding wetly between his thighs and the swift, anxious up-and-down of his surprisingly deft fingers on his member. "

gh "You’re so… soft."
gh "You make me want more of you."

ro "Then take it."

gh "Heh. Another time, maybe. Tonight is for you."

"Rowan’s knees trembled, his body struggling to stay upright under the twin assault of pleasing sensations."
"Each time Greyhide drew back his hips, he watched in lurid fascination as the flat tip drew back beyond sight… then {i}thrust{/i} forward in full glory as the sheath bunched between his legs. It was heavenly."
"The bull grunted, his breath growing shallower as he quickened his jerking motion. His grip was soft but insistent: he {i}wanted{/i} Rowan to cum first. Ever the competitor, Rowan tightened his thighs and sucked in his gut, determined not to lose."

ro "You’re gonna cum first."

gh "{i}Hrmph{/i}. Cocky."

"The tone suddenly shifted: no longer was this a tender lovemaking. Greyhide thrust hard against Rowan’s flank, resting his groin squarely against his ass as the hero struggled to keep his thighs clenched." 
"The Minotaur’s fingers became a blur, jerking Rowan’s precum-soaked dick in swift, sure movements. It was everything he could do to hold himself back from cumming: the lure was too intense."
"Out of options, Rowan resorted to a dirty trick. Taking care to steady himself, he reached up with one hand and took a firm grip of Greyhide’s dick. He circled his fingers around the tip and began jerking him in kind."
"Their heavy breathing became a chorus of mannish grunts, punctuated by the occasional moan or groan that led to still further attempts to make the other cum."
"By the end of their impromptu competition, Greyhide was breathing through his nose, and Rowan had to grit his teeth to bear the burning pleasure rolling through his painfully erect cock."

gh "{i}Hnnnnh! R-Rowan!{/i}"

#cg2 - cum var
show cg968 with sshake
show cg968 with sshake
scene cg969 with flash
pause 3

"In the end, Rowan won. He felt the building eruption {i}long{/i} before he saw it: a throbbing swell of Greyhide’s meat between his legs that presaged his budding orgasm." 
"The cock grew, bloated, then burst forth like a dam, white streams of pearlescent cow-cum spurting forth in virile streams across the bedsheets beneath him. All the while, Greyhide kept thrusting against him."
"The bull’s monstrous ejaculation was indiscriminate in its target: hitting Rowan’s chest and stomach on the upthrust and splattering his knees on the pullback. Rowan’s groin was soaked in his sloppy lust."
"Seeing the potency of his lover, smelling the metallic, salty scent of his sperm, sent Rowan into an orgasm of his own." 
"Greyhide’s insistent fingers proved too much for him, and he felt a tinge in his testicles. The tingling feeling traveled up, up and {i}outward{/i}, his body trembling from the force of the release." 
"While nowhere near as dramatic as Greyhide’s orgasm, he nonetheless added his own color to the now-thoroughly painted bedsheets."
"He bit his lip, for a moment overwhelmed by the rush of feelings, of elation and joy and release. In the space of a few moments, all the heartache and tension of the day melted away, and the two were left alone in their bliss."
"Panting, the two collapsed into one another’s arms. They lay together like that, nestled in their collective love upon the bed, soaked in one another’s juices. Both were exhausted, drained in body and spirit from all that had happened that day."
"But… they were together. They had both admitted their feelings, and they had resolved themselves to each other. That alone had made the whole ordeal worth it."

scene bg22 with fade
show greyhide neutral at center with dissolve

"After they’d cleaned up, Rowan dozed awhile on Greyhide’s bed. The bull pulled his woolen blanket over her and let him rest." 
"He walked, a little unsteadily to his work stool, and sat down. Staring at him in the warm light of the forge, a soft smile graced his lips."

gh "Sleep well, Rowan."
$ greyhideRelationship = 'rowan'
return

##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################

label greyhide_finale_platonic:
    
scene bg6 with fade
show rowan necklace neutral at midright with dissolve

"Rowan was busy sifting through the latest castle reports, when a most unexpected visitor showed up at his door."

show alexia 2 necklace shocked at midleft with dissolve

ro "Alexia? Is something wrong?"

al "Rowan, come quick! Andras just attacked Greyhide in the forge!"

show rowan necklace shock at midright with dissolve

ro "{i}What?{/i}!"

scene bg14 with fade
show rowan necklace angry at midright with dissolve
show alexia 2 necklace concerned at midleft with dissolve

ro "Tell me everything you saw."

al "I-I tried going to the forge today to convince Greyhide to start working again, but-"

show alexia 2 necklace neutral at midleft with dissolve

al "Andras was waiting for me at the door."

show rowan necklace concerned at midright with dissolve

ro "I thought you said Greyhide had barred the door and wasn’t letting anyone in."

show alexia 2 necklace concerned at midleft with dissolve

al "H-he had! But Andras, he just kicked it open. He had a sword in his hand, and he…"
al "Rowan, I’ve never seen Andras look so angry. I think he’s going to kill him!"

show rowan necklace angry at midright with dissolve

ro "No he wont. Not if we can help it."

scene bg22 with fade
show rowan necklace shock at midleft with dissolve
show alexia 2 necklace shocked at edgeleft with dissolve

"As the couple entered the forge they stopped short, their jaws dropping at the sight."

al "Oh {i}Goddess{/i}!"

#story CG
scene black with fade
show greyhide sad behind black
show andras displeased behind black
show rowan necklace angry behind black
show alexia 2 necklace concerned behind black

"Greyhide’s workshop had been all but wrecked by the furious combat that had taken place. Tools and weapons lay strewn about the shattered workspace like trampled metal grass. Chipped splinters of wood and hunks of raw metal were everywhere."
"Andras was a whirlwind, rushing at the hapless bull with reckless swings of the blade. He overturned a table, and Greyhide stumbled back in a desperate attempt to make distance." 

gh "Please my Lord. You don’t have to… I’ll make the blades, I swear it. Just do not-"

"Andras did not answer. His eyes were burning yellow stars in his sunken sockets. He fixed the bull with a savage look, then charged him once more."
"The demon crossed the distance with frightening speed, his feet pounding across the debris-strewn floor as he lifted his weapon high over his head."
"The bull clumsily lifted his hammer up, almost too late to meet the strike. The weapons rang as the sword edge met the blunt end of his hammer. Greyhide backpedaled, driven almost to his knees by the sheer force of Andras’ attack."

"They pulled apart, and Andras advanced on him once more, his weapon at his side and his bare chest exposed. Greyhide did not even pretend to take a swing."

an "You fight like a coward."

gh "I will not… hurt you."

an "Hurting me’s the only way you leave this room alive, old man."

ro "Lord Andras, what is the meaning of this?!"

an "Stand aside, fool."

al "G-greyhide didn’t do anything wrong!"

show andras angry behind black

an "He’s {i}wasted my time{/i}."
an "I’ve spent the better part of a week listening to sob stories from my men at the training yard. How all their broken equipment is being left to rust at the foot of his door."
an "At first I just chalked it up to this wretch being preoccupied with work, but then I learned that his forge hasn’t been lit in {i}days{/i}."

gh "..."

an "-And now this pathetic weakling refuses to explain himself!"
an "I promised him he wouldn’t ever have to fight… so long as he made my weapons of war. But now he won’t even try to save his own skin."

"Andras was revved up, ready to kill. Greyhide by contrast was panting, breathless from his desperate attempts to avoid the demon’s blade. There was a red tint to the fur beneath his left nipple, a dripping splotch that stained his fur."
"Alexia cast a worried glance in Rowan’s direction. The hero set his jaw."

ro "Lord Andras, whatever crimes you think Forgemaster Greyhide is guilty of, this is not the way to punish him. "
ro "We need him."

"Andras ignored Rowan, thrusting his sword forward lazily at Greyhide’s face. The Minotaur stumbled backwards, narrowly avoiding getting the tip lodged in his eye. Andras rushed forward, cutting long X’s back and forth in his direction."

al "No! Stop!"

"Rowan stepped forward, but the demon spun around on his heel and brandished his blade."

an "Come between me and that bull’s punishment, and I’ll gut you in front of your wife. That goes double for you, girl."

ro "Lord Andras you {i}can’t{/i}-"

gh "Friend Rowan, dear Alexia…"
gh "Do not... interfere."
gh "This is my sin. Not... yours."

show rowan necklace concerned behind black

ro "Greyhide, what the hell are you-"

"But Andras was already upon him once more. The couple watched anxiously from the sidelines. Rowan felt the cold grip of his sheathed sword clenched tight in his hand. Alexia clutched at his other arm, hiding partially behind him as if to shield herself from the violence."
"Andras continued to attack him, and Greyhide continuously retreated, holding his hammer up to feebly bat away the careless swings Andras sent in his direction. The demon was getting visibly irritated."

show rowan necklace angry behind black

an "...What’s he doing? "

al "W-who?"

ro "Andras. He’s not trying to kill him… he’s toying with him."

an "{i}Come on{/i}! Hit me! Take a fucking swing!"

gh "..."

show andras displeased behind black

an "Is this the fabled might of the Minotaurs? Are all your kind so damned pathetic?"

gh "No. Just… me."

an "You spineless worm."

show andras angry behind black

"Andras’ attacks grew wilder. He put his weight into the swings, hacking at Greyhide’s defenses with blow after unsubtle blow. Each time, Greyhide only just managed to bat away the weapon with his hammer, but he was struggling to keep up."

show andras displeased behind black

an "Is this what it was like for Rowan and Alexia, huh? Timid, feeble, flaccid flailings?"

show andras smirk behind black

an "Is this why they rejected you? A beast with no balls, a coward with no cock? No wonder you’re alone."

gh "{i}Hrmh{/i}."

"Andras’ words were too pointed, {i}too{/i} goading. His mocking laughter came with an almost theatrical flair."
"Greyhide was panting, his breath coming in and out in great gouts. Andras, utterly unconcerned, took a brief moment to turn his back on the bull and address the two bystanders."

an "Tell me you two: when you were drug-drunk with my sister’s lust potion, did it ever even {i}occur{/i} to you that this unsightly beast might tickle your fancy?"

"Andras spun around on his heel, swinging hard at Greyhide’s face. The bull lifted his hammer, but it was knocked from his hands. The tip of Andras’ blade swept across his snout, making a shallow incision just below his left nostril."

gh "{i}Urgh!{/i}"

show alexia 2 necklace shocked behind black

al "{i}Greyhide!{/i}"

ro "Damn it Andras, {i}stop{/i}! You’ve made your damned point!"

"Blood trickled down from his nose where he’d been nicked. Greyhide held a hand up to it, breathing heavily. Andras shook his head at him like a stern schoolteacher lecturing a misguided pupil."

show andras displeased behind black

an "No. They never fancied you, I think."
an "After all, who could love a creature as gutless and weak-kneed as you?"
an "You're no Forgemaster, and you're {i}certainly{/i} no man. "

"Greyhide was shaking. His eyes clenched shut as he struggled to contain himself. A dark, malicious grin grew on Andras’ face."

an "Death would be preferable to having a mate like you."

#show story CG with sshake

gh "{i}RAAAAAAAAAAAAH{/i}!"

"The roar of an enraged beast pierced the soot-filled air. Whatever further taunt Andras had been about to say was drowned out entirely. Greyhide lowered his head and charged the Demon."

scene cg955 with sshake
pause 3
#alexia shocked
#rowan angry

"Greyhide cranked his arm back and smashed his fist into the Demon’s face. The blow connected against Andras’ jaw with the weight of a warhammer. The demon staggered, his head snapping to one side." 
"Greyhide did not give him space. He yanked the sword from his hands and snapped it in one, titanic strain with his clenched fists." 
"He cast aside the broken pieces, swinging wildly at Andras’ face. His thick mitts connected with the demon’s chin a second time, causing Andras to take a step back to steady himself."

scene cg956 with sshake
pause 3

"Greyhide tackled Andras to the ground, nearly goring him in the process with his horns as he headbutted the demon as hard as he could into the ground. The couple heard the loud {i}crack{/i} of the demon’s head as it hit the stone floor with earth-shaking force."

scene cg957 with fade
show alexia forge shocked behind cg957
show rowan necklace angry behind cg957
pause 3

"Andras raised his hands to ward him off, but the raging Minotaur would not be dissuaded. Greyhide rained blows down on Andras, his fists rising and falling in a reckless repetition, all subtlety and restraint gone from his face."

al "G-Greyhide!"

"He either didn't hear her, or he didn’t listen. His brutal assault continued unabated."

ro "{i}Greyhide{/i}!"

"It was only after several seconds of frenzied aggression that Greyhide slowed his assault, turning his head sharply to glare at the two of them. For a brief moment, they could not see the man beneath the beast."

show rowan necklace concerned behind black

ro "You’ve done... enough."

"He met their gazes. The longer he looked at them, the more his anger drained away, and he became himself again. Greyhide glanced away, wiping at his eyes with the back of his hand as he picked himself up off the ground. Rowan and Alexia hurried over."
"He looked drained now, having spent himself in the frenzy. The bull stood up off Andras, his legs shaking with the effort. Beneath him, Andras wasn’t moving."

show alexia 2 necklace concerned behind black

"Is he…?"

scene bg22 with fade
show alexia 2 necklace concerned at edgeleft with dissolve
show rowan necklace concerned at midleft with dissolve
show greyhide sad at cliohnaright with dissolve
show andras happy at edgeright with dissolve

an "{i}HA!{/i}"

"As if waiting for his cue, the demon sprang up."

an "Yes! Now {i}that’s{/i} more like it! Haha!"

"He spat a wad of blood onto the ground next to him, rubbing blithely at his chin."

an "Good swing, old man!"

"Greyhide looked horrified. He stepped forward, extending his hands out towards the man he had been so enthusiastically beating upon, mere moments before."

gh "I… Lord Andras, I am so-"

show andras angry at edgeright with dissolve

an "Don’t you {i}dare{/i} try to apologize to me, fool. "

"The demon, still chuckling, picked himself up off the ground. He was black and blue, his face a tattered mess of cuts and bruises." 
"Greyhide had {i}literally{/i} dented his face. But already his hellish constitution was regenerating itself, the wounds fading even as he spoke."

show andras happy at edgeright with dissolve

an "Who would have thought a silly little comment like {i}that{/i} would have been what it took to finally wake you up? "
an "You always were slow on the uptake, cow."

"He reached out and took hold of Greyhide’s shoulder. Andras patted him on the back as if he were encouraging a trusted friend."

an "I’m glad we finally understand each other."

gh "I..."

show andras displeased at edgeright with dissolve

an "Shut up. Listen closely to me now, because this is the first and last time I will ever say this."
an "I have no use for weaklings, still less for those who {i}pretend{/i}. You are who you are. Embrace it."

"Andras cast a teasing smirk in the couple’s direction. He winked at them."

show andras happy at edgeright with dissolve

an "You owe me work, starting now. I expect to see twice the normal output by the end of next week, or your head’s back on the chopping block."

gh "Y-yes, Lord Andras…"

show andras displeased at edgeright with dissolve

an "No more excuses, no more distractions. You bring me my weapons, or you face the consequences. "
an "Do I make myself clear?"

gh "Yes, Lord Andras."

show andras happy at edgeright with dissolve

an "Good, then get back to work. You owe me a new sword."

hide andras with moveoutright

"The couple stared at Andras’ retreating form as he left the forge. Greyhide, exhausted, sank to the ground. They rushed over to him."

al "Greyhide!"

ro "Goddess, are you all right?"

gh "Hmh… I should not have done that."

ro "Something tells me that’s the reason you’re still alive right now."

al "You had us worried sick."

"The bull had trouble looking either of them in the eye."

gh "I… thank you for your concern. But...  you need not worry about me. Not after what I-"

show rowan necklace happy at midleft with dissolve

ro "Hold on, I’ll get something to patch these wounds. Alexia, will you stay with him?"

show alexia 2 necklace happy at edgeleft with dissolve

al "Of course. Just rest for now, we’re here for you."

"The dazed bull could do little but nod as his friends surrounded him."

gh "I… perhaps we should talk."

scene bg22 with dissolve
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve
show greyhide sad at cliohnaright with dissolve

"It was some work bringing the forge back to some semblance of working order. Andras’ intrusion had left most of Greyhide’s workspace a destroyed mess. It would take days to fully clean, and much of the furniture would have to be replaced." 
"Still, the Minotaur was in better spirits than he’d been in over a week."

gh "I am sorry for the trouble I have caused. For the danger I put you both in."
gh "I would... understand if you hate me."

al "Don’t be ridiculous, Greyhide."

ro "She’s right. Why would we ever be mad at you?"

"Greyhide’s eyes watered. He did his best to hide it, but his slumped shoulders said it all."

gh "B-because of… what Jezera said, with the drug-"

"The couple exchanged a look."

show rowan necklace happy at midleft with dissolve

ro "Is that it? You don’t have to beat yourself up over that."

show alexia 2 necklace happy at edgeleft with dissolve

al "You are our friend, Greyhide. We would never judge you for what Jezera did."

gh "But… I almost-"

show rowan necklace neutral at midleft with dissolve

ro "But you didn’t. You kept in control. "

show alexia 2 necklace concerned at edgeleft with dissolve

al "It was the Twins who caused this, not you."

gh "The Twins do what they will. We are at their mercy. But I have no excuse."
gh "I have... grown close to you. To both of you. But I betrayed that trust, nearly came between mates."
gh "In my tribe, such an affront would warrant a fight to the death."

"Greyhide got down on one knee in front of them, bowing his head."

gh "I am sorry. I will not fight you if either of you choose to take vengeance."

show alexia 2 necklace angry at edgeleft with dissolve

al "Oh for goodness sake, Greyhide. Get up."

show rowan necklace happy at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve

ro "She’s right. I’d rather not have to look down on you while we talk."

al "That drug… we were {i}all{/i} affected. But none of us gave in."

ro "You are a true friend. There’s no reason to feel ashamed."

"The Minotaur, clearly touched, began to sniffle, rubbing at his eyes."

gh "You two… mean much to me. More than I can say. I was so scared I had… ruined things between us."
gh "I do not wish to be... that beast. I do not wish to hurt others, or to act as callous as the Twins do."

ro "You never have to worry on that account, Greyhide."

gh "Friend Rowan…"

al "If you’re {i}ever{/i} afraid of losing control like that, you can come to us."

gh "Little one…"

"The bull shook his head back and forth."

gh "I… I will think on what you have said. My mind has not been itself these last few days. I did not know… what you thought of me."

"Greyhide let out a sigh of relief."

gh "I would… very much like to be your friend again."

show alexia 2 necklace happy at edgeleft with dissolve

al "You never stopped."

gh "Jezera’s trick will never happen again, I swear it. Even if I have to give up Firegrout."

"Rowan began to laugh."

ro "Hey, let’s not be hasty now."

al "It {i}was{/i} a very tasty drink!"

gh "You two. You are beautiful together."
gh "You do me a great honour with your kindness. I will not forget this."

al "You are a good man, Greyhide. That is a hard thing to come by, these days."

"The bull blushed and glanced away bashfully."

gh "I will try… to live up to your expectation."
gh "...What day we have another dinner together tonight? Your company is a great comfort to me."

"Rowan smirked as Alexia blanched at the prospect of seeing Greyhide’s eating habits once more. She did her best to put on a wavering smile."

show alexia 2 necklace concerned at edgeleft with dissolve

al "O-of course!"

ro "We’d be delighted to, Greyhide."

gh "Work can wait. Friends come first."
gh "...Thank you for reminding me of that."

$ greyhideRelationship = 'platonic'
return

##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################

label greyhide_finale_poly:

scene bg9 with fade
show alexia 2 necklace concerned at midleft with dissolve
show rowan necklace angry at midright with dissolve

"It took a week of simmering tension to come to a boil, but the argument - when it finally came - was explosive."

al "No, we {i}need{/i} to talk about this, Rowan."

ro "Why? What is there even left to say?"

show alexia 2 necklace angry at midleft with dissolve

al "A lot. A whole novel’s worth. Stop trying to sweep this under the rug."

menu:
    "I’m not trying to ‘sweep’ anything under the rug.":
        $ released_fix_rollback()
        al "Then why won’t you talk to me?"
        ro "Because it’s difficult! What the hell am I supposed to say?"
        show rowan necklace happy at midright with dissolve
        ro "‘Dearest wife: I hope you enjoyed Greyhide’s company half as much as I did while we were lust-drunk!’"
        show rowan necklace angry at midright with dissolve
        ro "Where do we even go from here? What could we say or do to make things right with each other? Or with him?"
        "Alexia - seeming to sense the growing distance between herself and her husband - reached out and took his hand."
        show alexia 2 necklace concerned at midleft with dissolve
        
    "What do you want from me, Alexia?":
        $ released_fix_rollback()
        al "{i}I don’t know{/i}! Something to make sense of this? "
        al "We fucked a {i}Minotaur{/i}, Rowan. {i}Both of us{/i}."
        ro "You don’t need to remind me."
        show rowan necklace neutral at midright with dissolve
        ro "There’s no sense to be made of the matter. We were drugged, we weren’t thinking clearly…"
        "Alexia shook her head, resolute in her worry."
        show alexia 2 necklace concerned at midleft with dissolve
        
    "I’d rather we forget this ever happened":
        $ released_fix_rollback()
        al "Well too bad: our… our {i}friend{/i} is locked up in his forge, and we’re at each other’s throats."
        show alexia 2 necklace concerned at midleft with dissolve
        al "We need to figure this out. Pretending it didn’t happen won’t solve anything."
        "Rowan struggled to look Alexia in the eye as she stared at him."

    "Don’t try to act guiltless with me, you whore.":
        $ released_fix_rollback()
        show alexia 2 necklace shocked at midleft with dissolve
        "Alexia’s mouth gaped. Her stunned silence soon gave way to raging indignation."
        show alexia 2 necklace angry at midleft with dissolve
        al "{i}Excuse me{/i}?!"
        al "How dare you even say those words, you bastard! You had sex with him too!"
        ro "Oh yeah? And who jumped into his bed first?"
        al "This isn’t a damned footrace! We were {i}both{/i} drugged! If I’m at fault, then so are-"
        "Alexia trailed off. She took in a deep breath, then let it out in a heavy exhale."
        $ change_relation('alexia', -5)
        show alexia 2 necklace concerned at midleft with dissolve
        
al "Rowan, I haven’t slept well in almost a week. I’ve been having nightmares. Every morning, I wake up sick to my stomach."

show alexia 2 necklace neutral at midleft with dissolve

al "Solansia preserve me, but I can’t take it anymore."

show rowan necklace angry at midright with dissolve

"Rowan’s fists clenched at his sides."

menu:
    "...You care about him":
        $ released_fix_rollback()
        al "{i}And you don’t{/i}?"
        show rowan necklace shock at midright with dissolve
        "Rowan’s breath caught in his throat. He opened his mouth to speak, then closed it. His chest hurt."
        "It… might have been easier for all of them if it had just been about sex."
        show rowan necklace concerned at midright with dissolve
        ro "I don’t know."
        show alexia 2 necklace concerned at midleft with dissolve
        
    "I can’t take it anymore either.":
        $ released_fix_rollback()
        show rowan necklace neutral at midright with dissolve
        ro "...I haven’t slept in days. I think it’s a side-effect of the drug Jezera put in the tea."
        show alexia 2 necklace concerned at midleft with dissolve
        al "Damn the drugs, what are we supposed to do about {i}him{/i}?"

    "We’ve got to suffer through it":
        $ released_fix_rollback()
        ro "The worst is almost over, the drug’s toxin will be out of our system soon."
        show alexia 2 necklace angry at midleft with dissolve
        al "I don’t give a damn about the drug, Rowan. We need closure. "
        show alexia 2 necklace concerned at midleft with dissolve

al "Greyhide’s locked himself in the forge and won’t come out for anyone."

show rowan necklace angry at midright with dissolve

ro "Then… I guess we have to go talk to him."

"Rowan heaved a heavy sigh, pinching the corners of his brow. He shook his head back and forth in frustration."

ro "Gods, when did things get so damned complicated?"

scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve
show rowan necklace neutral at midright with dissolve

"The couple said nothing to each other as their twin footsteps echoed through the castle corridors." 
"The fiery anger of their confrontation had spent itself, and they had lapsed back into that same, uncomfortable politeness that had dogged their interactions for almost a week." 

ro "Has he left his room at all?"

al "Not that I’m aware of. He said he wanted to be left alone."

show rowan necklace concerned at midright with dissolve

"Another long silence. It was unbearable. Rowan glanced over at his wife, whose gaze was set in front of her. She walked with a notable stiffness in her step, as if she was just barely holding back tears."

menu:
    "He reached out and took her hand.":
        $ released_fix_rollback()
        show alexia 2 necklace concerned at midleft with dissolve
        "His grip was firm as it took hold of her. Alexia was momentarily startled, and cast a short glance in his direction."
        show rowan necklace happy at midright with dissolve
        "Rowan returned a smile. Alexia’s lips curved involuntarily upwards, and she glanced away from him. A gentle blush filled her cheeks." 
        "With some hesitation, her fingers interlaced with his. The two walked hand in hand down the hall to the forge."
        "A quiet gesture, but an important one. A little bit of warmth had just reentered their relationship."
        $ change_relation('alexia', 3)
        
    "He focused on what he was going to say to Greyhide":
        $ released_fix_rollback()
        "There was no time to worry about the stormcloud hovering over her thoughts, not when he had his own to contend with. Rowan had too much to think about already."
        "The two walked in grim silence to Greyhide’s door, like two warriors approaching the sounds of battle."
        
scene bg22 with fade
show rowan necklace angry at midleft with dissolve
show alexia 2 necklace concerned at edgeleft with dissolve

al "Wait, why is there an Orc at the door?"

show orc soldier neutral at midright with dissolve

ro "...Something’s wrong."
ro "You there! What’s the meaning of this? Why is the forge locked?"

al "Where’s Greyhide?"

os "Boss had ‘em tossed in a cell. I’s guardin’ the weapons while ‘e is gone."

show rowan necklace shock at midleft with dissolve
show alexia 2 necklace shocked at edgeleft with dissolve

al "{i}What{/i}?!"

show rowan necklace angry at midleft with dissolve

ro "On what grounds?"

os "Boss’ orders. He sez the Forgemaster won’t work. Won’t talk about it neither. "
os "So Forgemaster gits tossed in a cell till he talks."

show alexia 2 necklace angry at edgeleft with dissolve

al "B-but he didn’t do anything wrong!"

os "Bring it up wit’ the boss then."

"Rowan gritted his teeth. He stepped up to the orc and yanked him forward by the cuff of his armour."

ro "{i}Where did they take him?{/i}"

scene bg8 with fade
show rowan necklace angry at midleft with moveinleft 
show alexia 2 necklace concerned at edgeleft with moveinleft

"Rowan and Alexia brushed past the gaoler as if he wasn’t even there, commanding him to open up Greyhide’s cell."

show orc soldier neutral at midright with dissolve

os "Jus… knock if ya need me to open up again, eh?"

hide orc soldier with dissolve

show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve

"The door slammed shut behind them. They were engulfed in shadows. A hulking figure sat hunched in the far corner."

show greyhide sad at cliohnaright with dissolve

al "...Greyhide, it’s us."

ro "We came as soon as we heard what had happened."

al "Are you okay?"

"His eyes never lifted, his flat gaze stared dully into his lap.The Minotaur breathed in, his thick chest filling with air, then exhaled heavily through his nose. The couple shared a look."

menu:
    "We’re going to get you out of here.":
        $ released_fix_rollback()
        ro "I know that this looks bad, but we can make things right."
        show rowan necklace happy at midleft with dissolve
        ro "Whatever they think you’ve done, I’m sure I can get you off the hook."
        "Alexia nodded along with her husband."
        al "I can vouch for you too, I’ll say you were held up with work orders."
        show alexia 2 necklace happy at edgeleft with dissolve
        al "We’re here to help. However we can."
        
    "You shouldn’t have defied the Twins.":
        $ released_fix_rollback()
        ro "You know how volatile they can be. Especially when they don’t get what they want."
        "Alexia cast a worried glance in her husband’s direction. Her fingers reached up to toy with the sapphire necklace around her neck."
        al "He’s right, Greyhide."
        al "I… {i}we{/i} don’t want to see you stuck in the same situation as us."

    "We were hoping to talk about what happened.":
        $ released_fix_rollback()
        show alexia 2 necklace angry at edgeleft with dissolve
        "Alexia cast a sharp look in Rowan’s direction, but he continued."
        ro "I know you’re probably not in the mood to discuss something like that, given the circumstances, but I’m pretty sure its the reason why we’re all here."
        show rowan necklace concerned at midleft with dissolve
        ro "...Maybe talking about it might help resolve things."
        show alexia 2 necklace concerned at edgeleft with dissolve
        al "We’re worried about you. You’ve never been like this before."
      
    "We missed you.":
        $ released_fix_rollback()
        show alexia 2 necklace concerned at edgeleft with dissolve
        "Alexia shot a worried glance in Rowan’s direction. She swallowed and nodded."
        al "It’s true. We’ve both been worried sick about you."
        al "Now… with all this…"
        ro "We want you to know that we’re here for you."
    
"The silence that followed was deafening. Neither knew what to say. The manacles around Greyhide’s wrists were self-evidently superfluous: he had no intent of resisting his fate."

ro "Look, a lot has happened in the last week. And believe me: I’ve got plenty to say."

gh "..."

ro "But right now, the important thing is getting you out of this cell."

gh "..."

show alexia 2 necklace angry at edgeleft with dissolve

al "Goddess fend Greyhide, {i}talk to us{/i}! We’re your friends!"

show alexia 2 necklace concerned at edgeleft with dissolve

"The bull flinched at her words. He lifted his head, just slightly. Only slightly."

gh "Please… dear friends, you do not need... to bother with me."

show rowan necklace concerned at midleft with dissolve

ro "You didn’t do anything wrong, Greyhide."

show rowan necklace neutral at midleft with dissolve

"Greyhide shook his head firmly back and forth."

gh "Did to myself. Did… to you."
gh "No reason. No control. Just... did it."
gh "I am sorry. I am so sorry."

show alexia 2 necklace concerned at edgeleft with dissolve

al "We don’t blame you for what happened."

gh "It is my shame to bear."
gh "Tired... of trying so hard."

al "You don’t really mean that."

gh "..."

show rowan necklace concerned at midleft with dissolve

menu:
    "Rowan hugged him, while Alexia took his hand.":
        $ released_fix_rollback()
        "The bull trembled as his two companions approached. Alexia's tiny fingers interlaced with his. She stroked his thick digits with a tender touch."
        show alexia 2 necklace happy at edgeleft with dissolve
        "Rowan got down on one knee and embraced him. His arms settling with a comforting warmth around his body. His warm fur tickled as he held him close."
        show rowan necklace happy at midleft with dissolve
        ro "Don’t give up on us, Greyhide."
        "Rowan cupped Greyhide’s cheek with his hand, tilting it to face him. The Minotaur grimaced, but did not push either of them away."
        
    "Alexia embraced him, while Rowan put a hand on his shoulder.":
        $ released_fix_rollback()
        "The bull trembled as his two companions approached. Rowan stood at his side, staring down at him with a gentle smile as he patted his shoulder."
        show rowan necklace happy at midleft with dissolve
        "Alexia, overcome with emotion, was far bolder. She threw her arms around him, burying her face in his chest as she held him close."
        al "You’re not alone, Greyhide."
        show alexia 2 necklace happy at edgeleft with dissolve
        "She traced the line of his lips with her finger, smiling softly at him. The Minotaur grimaced, but did not push either of them away."
        
    "Both husband and wife embraced him":
        $ released_fix_rollback()
        "The bull trembled as his two companions approached. The couple got down on their knees, each taking a side of Greyhide. They hugged him, arms intertwining like vines across a tree trunk."
        show rowan necklace happy at midleft with dissolve
        show alexia 2 necklace happy at edgeleft with dissolve
        "Rowan held him close, his fingers clenching tight as if to never let go. Alexia leaned flush against his form, resting her head against his shoulder. His warm fur tickled them both."
        ro "We’re here for you, Greyhide."
        al "We would never leave you alone like this."
        "The Minotaur took in a stuttering inhale, but did not push either of them away."
        
    "Alexia took his hand, while Rowan put his hand on shoulder":
        $ released_fix_rollback()
        "The bull trembled as his two companions approached. Rowan stood at his side, staring down at him with a gentle smile as he patted his shoulder. Alexia took Greyhide’s hand in hers, her fingers softly  stroking across his thick digits."
        show rowan necklace happy at midleft with dissolve
        ro "You’re our friend, Greyhide. And nothing can change that."
        show alexia 2 necklace happy at edgeleft with dissolve
        al "You never have to hide from us."

"Greyhide shuddered at their collective touch. At last he lifted his eyes to look at them, his gaze meeting theirs for the first time since they’d arrived."

gh "I-"

show rowan necklace shock at midleft with dissolve
show alexia 2 necklace shocked at edgeleft with dissolve

"The {i}snap{/i} of the lock unlatching startled the three of them back to reality. The door opened wide, slamming against the outside wall from the force of the swing. "

show andras displeased at edgeright with dissolve

al "L-Lord Andras!"

show rowan necklace neutral at midleft with dissolve

"Alexia stood up in a rush, scooting backwards till her back was against the cell wall. Rowan stood his ground, staring Andras down as he walked slowly into the room."

show alexia 2 necklace concerned at edgeleft with dissolve

"The demon planted his hands upon his hips, his eyes shifting back and forth between Rowan, Alexia and Greyhide for a short moment before he let out a snort of amusement."

an "Well, well, everybody’s here! Kharos’ sweaty ballsack, but my sister wasn’t lying."

show andras smirk at edgeright with dissolve

"The demon’s lips split wide into a smug, toothy grin."

an "Oh a {i}thousand{/i} pardons, am I interrupting the wedding ceremony?"
an "I’m not sure what kind of bride price you two expect to receive. Usually the dowry {i}is{/i} the cow!"

show rowan necklace angry at midleft with dissolve

ro "Lord Andras, you need to release Forgemaster Greyhide immediately."

show andras displeased at edgeright with dissolve

an "...I ‘need’ to, mortal?"

al "H-he’s done nothing wrong."

show andras smirk at edgeright with dissolve

an "Is that so? So why have you two snuck into his cell like a pair of horny catspaws?"

show andras displeased at edgeright with dissolve

an "Oh, pipe down will you? You’ve played the part of the whinging martyr for long enough. "

"Andras studied Greyhide for a long moment, his lips twisting with contempt at his downturned expression."

an "You’d better have a good explanation for yourself, you old fool."

gh "..."

an "I’ve spent the better part of a week listening to sob stories from my men at the training yard. How all their broken equipment is being left to rust at the foot of your door."
an "At first I chalked it up to you being preoccupied with work, but then I learned that your forge hasn’t been lit in {i}days{/i}."

gh "..."

show andras angry at edgeright with dissolve

an "Stop staring at the floor like a drooling imbecile and {i}answer me{/i}."

gh "I… have no excuse."

show andras displeased at edgeright with dissolve

an "Well that's too bad, old man. I’d at least be willing to listen if you had one."
an "You are the castle Forgemaster. We are at war. My men need weapons, and you are expected to provide them. "
an "There is no excuse for failure, none whatsoever."

show alexia 2 necklace angry at edgeleft with dissolve

ro "That's not fair, Andras."

al "M-my Lord, Greyhide has always done his best to-"

show andras angry at edgeright with dissolve
show alexia 2 necklace concerned at edgeleft with dissolve

an "Shut up. Your lecherous antics are the reason he’s down here in the first place. If you want to make it worse for him, keep talking."

"Andras turned to glare at Greyhide’s downcast expression."

show andras displeased at edgeright with dissolve

an "Your bed partners are quite the handful. Shame they chose a lamb to lay with."

gh "..."

an "Consider this imprisonment a warning. The only one you’ll ever get from me."
an "If you won't do your duties, then perhaps the display I make of your entrails will deter these two from romancing your successor."

gh "That would… probably be for the best."

show andras angry at edgeright with dissolve
show alexia 2 necklace shocked at edgeleft with dissolve
show rowan necklace concerned at midleft with dissolve

"Andras was just starting to turn away when his head snapped around. His expression twisted into something unrecognizable. Inhuman."
"Greyhide refused to meet his eyes, keeping his gaze trained to the floor. His subservience only seemed to make him madder."

show andras displeased at edgeright with dissolve

an " I see... so that’s how it is, then."

show bg8 with flash
show rowan necklace shock at midleft with dissolve

gh "{i}Hurk!{/i}"
    
"Red energy surrounded Greyhide. A circle of profane magic grew above his head as Andras cast his torturous spell. The stoic Minotaur fell to one knee, his body shuddering from the sudden onrush of pain."    

an "So be it. Seeing as you no longer serve a purpose as a Forgemaster, I suppose I’ll have to find a new use for you."

ro "{i}Greyhide{/i}!"

al "{i}Greyhide{/i}!"

"After a few seconds Andras released his concentration, allowing the spell to dissipate. The Minotaur let out a gasp of air."

an "Do you remember the promise I once made to you, old man?"
an "You don’t have to fight… so long as you make my weapons of war."

"Andras’ fists clenched and the magic returned, stronger than before. It engulfed Greyhide in blinding agony."
"The bull let out a roar of pain, falling onto his hands and knees. His manacles jingled as he shuddered from the force of the magic assault."

show rowan necklace angry at midleft with dissolve

ro "{i}Andras{/i}, stop!"

show alexia 2 necklace concerned at edgeleft with dissolve

al "Don’t hurt him!"

show alexia 2 necklace shocked at edgeleft with dissolve
show rowan necklace shock at midleft with dissolve

"Another pulse, this time for nearly five full seconds. Greyhide let out a roar of pain, writhing on the ground in agony as the red circle of energy roiled and contorted about him."

gh "{i}HRRRRRAAAGH!{/i}"

show rowan necklace angry at midleft with dissolve

"Alexia covered her mouth in horror. Rowan stepped forward, his hand almost unconsciously going to his sword."

ro "{i}ANDRAS{/i}!"

show alexia 2 necklace concerned at edgeleft with dissolve

al " Stop! {i}Please{/i}, just stop!"

"Andras unclenched his hands, and the magic dissipated. Greyhide collapsed onto the ground, panting heavily."

an "Look at him: this miserable wretch won’t even struggle to save his own skin."
an "He’s a lamed bull, useless to me. Jezera’s little prank revealed just how brittle he is."

al "I beg you, my Lord. He is just under a lot of stress-"

"Andras ignored her, nodding to the guards outside."

show andras displeased at edgeright with dissolve

an "Bring him out to the courtyard, it’s high time I put him out of his misery."

"Rowan stepped forward, squaring his chest. Andras shot him a cold glare."

an "...You have something to say, Rowan?"

ro "Just give him a chance, Lord Andras."

show andras smirk at edgeright with dissolve

an "What do you think I’m doing? The fool won’t work, so instead he’s going to fight."

ro "Fight who, exactly?"

"Andras’ calico grin widened."

#courtyard BG
scene black with fade
show andras smirk at midleft with dissolve
show greyhide sad at cliohnaright with dissolve

"The castle courtyard was cleared of traffic, the gates of Bloodmeen were temporarily sealed. A small crowd of Orcs had gathered to watch, but Andras ordered them away."
"This was a private matter."
"Andras stood across the long gap from Greyhide, a sword grasped in his fist. Greyhide held a similar weapon in his grasp, though it looked more like he was clutching a toothpick."
"Alexia and Rowan stood to the side, forbidden on pain of death to interfere. Andras had been very clear: Greyhide would fight, or he would die. Any attempt to rectify the situation risked making things much, much worse for them all."
"Greyhide shifted back and forth on his hooves, clearly uneasy.  Andras - for his part - looked utterly content, perhaps even a little excited."

an "Are you ready, cow?"

gh "This is… unnecessary."

show andras smirk at midleft with dissolve

an "It is very necessary."

gh "Please my Lord. You don’t have to… I’ll make the blades, I swear it. Just do not… make me-"

"Andras did not answer. He took a few experimental swipes with his sword, fixed the bull with a savage look, then charged."

#story CG

"The demon crossed the distance between them with frightening speed, his feet pounding across the stone as he lifted his weapon high over his head."
"The bull clumsily lifted his sword up, almost too late to meet the strike. The weapons rang as the edges met. Greyhide backpedaled, driven back by the force of Andras’ attack."
"The blades bent from the sheer pressure of the two behemoths clutching them. For a moment Andras indulged in the struggle, then shoved forward, causing Greyhide to lose balance."
"They pulled apart, and Andras advanced on him once more, his weapon at his side and his bare chest exposed. Greyhide did not even pretend to take a swing."

an "You fight like a coward."

gh "I will not… hurt you."

an "Hurting me’s the only way you leave this courtyard alive, old man."

"Andras thrust lazily at his face, and Greyhide stumbled backwards, giving room as he tried to avoid the blade. Andras did not let up. He attacked again, cutting long X’s back and forth in the direction of Greyhide’s face."
"The couple watched anxiously from the sidelines. Rowan felt the cold grip of his sheathed sword clenched tight in his hand. Alexia clutched at his other arm, hiding partially behind him as if to shield herself from the violence."

show rowan necklace angry behind black

ro "...What’s he doing?"

show alexia 2 necklace concerned behind black

al "W-who?"

ro "Andras. He’s toying with him."

"Andras continued to advance upon him, and Greyhide continuously retreated, holding his weapon up to feebly bat away the swings Andras sent in his direction. The demon was getting visibly irritated."

#behind cg
show andras angry at midleft with dissolve

an "{i}Come on{/i}! Hit me! Take a fucking swing!"

gh "..."

#behind cg
show andras displeased at midleft with dissolve

an "Is this the fabled might of the Minotaurs? Are all your kind so damned pathetic? "

gh "No. Just… me."

#behind cg
show andras angry at midleft with dissolve

an "You spineless worm."

"Andras’ attacks grew wilder. He put his weight into the swings, hacking at Greyhide’s defenses with blow after unsubtle blow. Each time, Greyhide only just managed to lift his blade in time to block them, but he was struggling to keep up."

#behind cg
show andras displeased at midleft with dissolve

an "Was this what it was like for Rowan and Alexia, huh? Timid, feeble, flaccid flailings?"

#behind cg
show andras smirk at midleft with dissolve

an "When you led them to the bed, blushing and squirming with your cock half-limp, did {i}they{/i} have to put in all the effort? Did you ever even ‘rise’ to the occasion? "

gh "{i}Hrmh{/i}."

"Andras’ words were too pointed, {i}too{/i} goading. His mocking laughter came with an almost theatrical flair."
"Greyhide was panting, his breath coming in and out in great gouts. Andras, utterly unconcerned, took a brief moment to turn his back on the beast and address the two bystanders."

an "Tell me you two: what was it that finally won you over? His winning smile, his delightful conversation? Perhaps his {i}dashing{/i} complexion?"

"Andras spun around on his heel, swinging hard at Greyhide’s face. The bull lifted his blade, but it turned and spun out of his hands, clattering to the ground. The tip of Andras’ blade swept across his snout, making a shallow incision just below his left nostril."

gh "{i}Urgh{/i}!"

show rowan necklace shock behind black
show alexia 2 necklace shocked behind black

ro "{i}Greyhide{/i}!"

al "{i}Greyhide{/i}!"

"Blood trickled down from his nose where he’d been nicked. Greyhide held a hand up to it, breathing heavily. Andras shook his head at him like a stern schoolteacher lecturing a misguided pupil."

#behind cg
show andras displeased at midleft with dissolve

an "No. None of that, I think. Just a broken shell of a beast who got lucky with the help of a drug."
an "You're no Forgemaster, and you're {i}certainly{/i} no man. "

"Greyhide was shaking. His eyes clenched shut as he struggled to contain himself. A dark, malicious grin grew on Andras’ face."

an "Death would be preferable to having a mate like you."

show black with sshake

gh "{i}RAAAAAAAAAAAAH!{/i}"

"The roar of an enraged beast pierced the air. Whatever further taunt Andras had been about to say was drowned out entirely. Greyhide lowered his head and charged the Demon."

scene cg963 with sshake
pause 3

"Greyhide cranked his arm back and smashed his fist into the Demon’s face. The blow connected against Andras’ jaw with the weight of a warhammer. The demon staggered, his head snapping to one side." 
"Greyhide did not give him space. He yanked the sword from his hands and snapped it in one, titanic strain with his clenched fists. He cast aside the broken pieces, rushing forward. His fist connected with his chin a second time, causing Andras to take a step back to steady himself. "

hide andras with dissolve

scene cg964 with sshake
pause 3

"Greyhide tackled Andras to the ground, nearly goring him in the process with his horns as he headbutted the demon as hard as he could. The couple heard the loud crack of the demon’s head as it hit the stone floor with earth-shaking force."

scene cg970 with fade
show rowan necklace angry behind cg970
show alexia 2 necklace shocked behind cg970
pause 3

"Andras raised his hands to ward him off, but the raging Minotaur would not be dissuaded. Greyhide rained blows down on Andras, his fists rising and falling in a reckless repetition, all subtlety and restraint gone from his face."

al "G-Greyhide!"

"He either didn't hear her, or he didn’t listen. His brutal assault continued unabated."

show rowan necklace angry behind black

ro "{i}Greyhide{/i}!"

"It was only after several seconds of frenzied aggression that Greyhide slowed his assault, turning his head sharply to glare at the two of them. For a brief moment, they could not see the man beneath the beast."

show rowan necklace concerned behind black

ro "You’ve done... enough."

"He met their gazes. The longer he looked at them, the more his anger drained away, and he became himself again." 
"Greyhide glanced away, wiping at his eyes with the back of his hand as he picked himself up off the ground. Rowan and Alexia hurried over." 
"He looked drained now, having spent himself in the frenzy. The bull stood up off Andras, his legs shaking with the effort." 
"Beneath him, Andras wasn’t moving."

show alexia 2 necklace concerned behind black

al "Is he…?"

#courtyard BG
scene black with fade
show alexia 2 necklace shocked at edgeleft with dissolve
show rowan necklace shock at midleft with dissolve
show greyhide sad at midright with dissolve
show andras happy at edgeright with dissolve

an "{i}HA{/i}!"

"As if waiting for his cue, the demon sprang up."

an "Yes! Now {i}that’s{/i} more like it! Haha!"

"He spat a wad of blood onto the ground next to him, rubbing blithely at his chin."

an "Good swing, old man!"

"Greyhide looked horrified. He stepped forward, extending his hands out towards the man he had been so enthusiastically beating upon mere moments before."

gh "I… I am so-"

show andras angry at edgeright with dissolve

an "Don’t you {i}dare{/i} try to apologize to me, fool."

"The demon, still chuckling, picked himself up off the ground. He was black and blue, his face a tattered mess of cuts and bruises." 
"Greyhide had {i}literally{/i} dented his face. But already his hellish constitution was regenerating itself, the wounds fading from his visage even as he spoke."

show andras happy at edgeright with dissolve

an "Who would have thought a silly little comment like {i}that{/i} would have been what it took to finally wake you up?"
an "You always were slow on the uptake."

"He reached out and took hold of Greyhide’s shoulder. Andras patted him on the back as if he were encouraging a trusted friend."

an "I’m glad we finally understand each other."

gh "I..."

show andras displeased at edgeright with dissolve

an "Shut up. Listen closely to me now, because this is the first and last time I will ever say this."
an "I have no use for weaklings, still less for those who {i}pretend{/i}. You are who you are. Embrace it."

"Andras cast a teasing smirk in the couple’s direction. He winked at them."

show andras happy at edgeright with dissolve

an "You owe me work, starting now. I expect to see twice the normal output by the end of next week, or your head’s back on the chopping block."

gh "Y-yes, Lord Andras…"

show andras displeased at edgeright with dissolve

an "No more excuses, no more distractions. You bring me my weapons, or you face the consequences."

an "Do I make myself clear?"

gh "Yes, Lord Andras."

show andras happy at edgeright with dissolve

an "Good, then get back to work. You owe me a new sword."

hide andras with moveoutright

"The couple stared at Andras’ retreating form as he left the courtyard. Greyhide, exhausted, sank to the ground. They rushed over to him."

show alexia 2 necklace concerned at edgeleft with dissolve

al "Greyhide!"

show rowan necklace concerned at midleft with dissolve

ro "Are you all right?"

gh "Hmh… I should not have done that."

show alexia 2 necklace happy at edgeleft with dissolve
show rowan necklace happy at midleft with dissolve

"His deadpan delivery elicited startled laughter from the both of them. Soon, Greyhide joined in, a deep chuckle that rumbled in his chest. Rowan put a hand to his shoulder."

ro "I think it’s high time the three of us had a talk."

scene bg22 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve
show greyhide sad at cliohnaright with dissolve

gh "I am sorry for the trouble I have caused. For the danger I put you both in."
gh "I would... understand if you hate me."

ro "Why would we be mad at you? It was the Twins who caused this. We wouldn’t even be in this mess if Jezera hadn’t intervened."

gh "The Twins do what they will. We are at their mercy. But I have no excuse."
gh "I have... grown close to you. To both of you. But I have betrayed that trust, come between mates."
gh "In my tribe, such an affront would warrant a fight to the death."

"Greyhide got down on one knee in front of them, bowing his head."

gh "I am sorry. I will not fight you if either of you choose to take vengeance."

show alexia 2 necklace angry at edgeleft with dissolve

al "Oh for goodness sake, Greyhide. Get up."

show rowan necklace happy at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve

ro "She’s right. I’d rather not have to look down on you while we talk."

al "That drug… we were {i}all{/i} affected. You don’t have any special reason to apologize to us."

ro "Hard to heap hate on you in particular when we gave in just as readily."

gh "The drugs were… not the only cause."
gh "I have... feelings for you. For both of you. The feelings one has for a mate."

show rowan necklace neutral at midleft with dissolve

ro "Hm…"

show alexia 2 necklace concerned at edgeleft with dissolve

al "I-I gathered as much."

gh "I have never felt this before about… two at once. Much less with {i}humans{/i}."
gh "But this changes nothing. I know what I have done. And I refuse to come between you. "

"Greyhide stared meaningfully at each of them in turn."

gh "If it is a problem... then I will accept the pain of losing you. My feelings mean less to me than our friendship. "

"The couple exchanged a look. Alexia’s expression was conflicted, there was a question in her eyes."

al "What… what do you think, Rowan?"

menu:
    "I don’t know, I care about him.":
        $ released_fix_rollback()
        "Alexia let out a sigh of relief."
        al "As do I."
        al "B-but that doesn’t mean I don’t love you!"
        show rowan necklace happy at midleft with dissolve
        ro "Nor I you."
        gh "My friends, I am confused."
        gh "You two are mates, but… you desire me as well?"
        ro "...I guess we do."
        gh "What does this mean?"
        "Rowan shared another look with his wife, and she picked up on his intent. The two stepped forward and embraced the surprised Minotaur in a tripartite hug."
        show alexia 2 necklace happy at edgeleft with dissolve
        ro "I’m not sure. I guess we’ll just have to figure it out."
        al "The three of us. Together."
        "Greyhide took in a stuttering breath, then let out a low, pained exhale. His large arms encircled them both, crushing them tight against him."
        gh "Thank you, dear friends. For reminding me who I am. Even when I forgot."
        "The Minotaur’s voice grew haggard."
        gh "You… you two are the reason I yet live."
        gh "There are no words… for what you mean to me."
        al "How about… ‘love?’"
        ro "That sounds about right. Come here, you sappy fool."
        "Rowan leaned up and kissed his cheek. Not to be outdone, Alexia did the same on the other side. The bull blushed."
        gh "I… would like to be with you two tonight."
        show alexia 2 necklace aroused at edgeleft with dissolve
        al "Seconded."
        show rowan necklace aroused at midleft with dissolve
        ro "No complaints here."

    "Let’s just forget this ever happened":
        $ released_fix_rollback()
        "Greyhide let out a sigh of relief."
        gh "I would… like that. I would like that very much."
        al "I… I-I think I would too."
        ro "Like you said, Greyhide: our friendship means more than some drug. The best thing we can try to do from here is to move on from what happened."
        gh "It will never happen again, I swear it."
        show alexia 2 necklace happy at edgeleft with dissolve
        al "You don’t even need to say it, Greyhide."
        show rowan necklace happy at midleft with dissolve
        ro "She’s right, we trust you."
        "The couple, now reconciled, hugged each other. Greyhide beamed, folding his thick arms together as he let out a grunt of approval."
        gh "You two. You are beautiful together."
        gh "You do me a great honour with your kindness. I will not forget this."
        al "You are a good man, Greyhide. That is a hard thing to come by, these days."
        "The bull blushed and bashfully glanced away."
        gh "I will try… to live up to your expectation."
        gh "...Friends?"
        "Alexia and Rowan shared a mutual look. They smiled at one another."
        ro "Friends."
        al "Friends."
        $ greyhideRelationship = 'platonic'
        return

$ greyhideRelationship = 'poly'

menu:
    "Rowan takes charge.":
        $ released_fix_rollback()
        jump greyhideFinalePolyRowanSex

    "Alexia takes charge.":
        $ released_fix_rollback()
        jump greyhideFinalePolyAlexiaSex

    "Greyhide takes charge.":
        $ released_fix_rollback()
        jump greyhideFinalePolyGreyhideSex


##########################################################################

label greyhideFinalePolyRowanSex:
    
al "Why don’t we… take this somewhere more comfortable?"

ro "Yes, lets."

"The couple seemed to be of one mind on the matter. Each took a hand of the burly Minotaur and led him, laughing to his bedside."

show rowan necklace naked at midleft with dissolve

"Rowan couldn’t help but feel Greyhide’s gaze trail across him as he stripped, shedding first his armor, then his clothing in rapid succession."

ro "...See something you like?"

gh "There is much to see. You are very handsome, Rowan."

"The hero of Rosaria smirked as Greyhide pulled his loincloth free, exposing his hard erection to the air. It twitched in response to Rowan’s growing smile."

ro "...You aren’t so bad yourself there, friend."

show alexia necklace naked angry at edgeleft with dissolve

al "You boys sure now how to make a girl feel like the third wheel."

ro "Relax, beloved. You’ve still got the best breasts among us."

"Greyhide flexed his pecs, grinning as the two stared in unabashed arousal at his thick, muscled build."

gh "Speak for yourself."

ro "Mmm, on second thought, he’s got a point."

show alexia necklace naked at edgeleft with dissolve

al "He’s definitely got you beat when it comes to physique."

"Rowan flexed his arm, marveling for a moment at its strength and consistency as he showed himself off."

ro "‘Speak for yourself.’"

"Alexia giggled, and Greyhide chuckled as well. For all their playful ribbing, they really {i}were{/i} all attracted to one another. Their blushing faces and soft, sexual smiles put paid to that."
"Rowan in particular had a deep hunger in his eye. His gaze kept flicking back and forth between his wife's crotch and Greyhide’s erection. He reached out, brazenly taking both in hand, leading them towards the bed."

ro "I’ve got an idea."

al "Dangerous."

ro "I promise, I think you’ll like it. Both of you."

#cg1
scene black with fade
show rowan necklace naked aroused behind black
show alexia necklace naked aroused behind black
show greyhide neutral behind black

"Rowan arranged them in a rough triangle around each other, each with the other’s genitals facing one another. Unsurprisingly, Alexia had quickly chosen her spot, with Greyhide and his notoriously long tongue at her crotch."

ro "Spoilsport."

al "You’re just jealous I got there quicker."

"Settling herself into place, she nuzzled Rowan’s crotch, planting a gentle kiss on his erection. She let out a low, sexual coo as Greyhide began his own work, his tongue slithering forth and trailing along her pussy lips with pleasing slowness."

al "Besides, now I get to reward you for the plan."

"Rowan had the more… ‘gargantuan’’ task ahead of him. Greyhide’s thick erection and heavy, hanging balls took up more than just his face. If he were to have any hope of pleasuring the horny bull, he’d have to work for it."
"He took to the process with adroit eagerness, leaning down to kiss one of the Minotaur’s heavy, hanging balls before sliding his tongue across the skin. Greyhide seemed pleased with the attention, as he soon spread his legs further."
"He grunted as he felt Alexia’s succulent lips encircle the head of his cock, taking it in her mouth as her hand jerked his shaft. She in turn moaned when Greyhide laid his flat tongue across the length of her pussy and began to lick it like he was sampling a sweet."
"Greyhide let out a soft groan when Rowan kissed the base of his shaft, using a hand to massage his tip as his thumb ran across the flat top. He was sensitive, overly so, given how easily the precum built at the top."
"The bull, properly encouraged, slid his tongue deep into Alexia’s folds. He pushed so far forward that his snout met her groin, and it looked for all the world like he was making out with her pussy."
"Alexia trembled in place, letting out a gasp that briefly cut off the oral contact she had with Rowan’s twitching cock. She soon righted herself, returning to the horny task of stimulating him yet further with hands and lips and swirling tongue."
"She lathered his cock with her love, giving it a glistening sheen as she took him in her mouth and down her throat, bobbing up and down as her mouth made short work of his most sensitive areas."
"Her legs spread wide, her hand reaching down to fondle his balls as Greyhide’s efforts grew more spirited."
"Rowan was not idle. He took the Minotaur’s cock in both hands and began to jerk him vigorously, using his mouth to plant little kisses on every sensitive spot he could find."
"He even managed to lean up and angle his head around to pleasure the bull’s cockhead with his searching tongue."
"There was little talking; there was little {i}need{/i} for it. They were expressing their mutual love for one another in a much more direct way."
"The slight gagging sound of his wife was the first indication that she came. Her back arched, her body went taut, and she let out a muffled cry with her husband’s cock between her lips."
"Rowan was himself fit to bursting. He drew his hips back, breathlessly indicating Alexia do the same. She laid back, letting out an exhausted sigh."

gh "Are you all right, little one?"

al "Y-yeah, I just...  need a minute."

ro "I can’t wait that long."

"Rowan reached out, pulling Greyhide towards him. The bull did not seem to understand what he was doing at first, hesitantly planting his hooves on either side of the horny hero as he was guided to do. His furry ass hovered over Rowan’s erection."

gh "Rowan… what are you-"

ro "I’m gonna fuck you, Greyhide."

gh "O-oh!"
gh "Oh, of course."

ro "You’re uh… gonna be a bit tight."

gh "{i}Hrmh…{/i}"

"The bull, almost as an afterthought, reached over and wiped his hand across the still-cumming Alexia’s groin. Undeterred, he spread the slick substance along the slim crevice of his ass. Now properly lubricated, he sank down on Rowan’s waist."

#cg2
scene black with fade
show rowan necklace naked aroused behind black
show alexia necklace naked aroused behind black
show greyhide neutral behind black

ro "Oh, {i}fuck{/i}-"

"Greyhide leaned back, resting his arms on either side of Rowan as he draped himself against his chest. Rowan’s cock slid with painful slowness into the bull’s furry rump, tighter than anything he’d felt before."
"The Minotaur let out a low grunt but continued his downward thrust. Alexia lazed upon the bed and watched, her eyes alight with interest. She moaned as she watched them, her two males in the midst of tender fucking."
"Rather than saying anything, she got up off the bed, circling around to face them. Rowan was unable to contain himself any longer, and thrust upwards. Greyhide inhaled sharply, his arms trembling as he held himself aloft."
"He was tight. {i}Unbelievably{/i} tight. His ass constricted around Rowan’s cock with a vice like grip, yielding only with severe reticence to his intrusion."
"Greyhide didn’t seem to be in pain though; if anything he was even more aroused. His massive dick strained the air, rock hard as it jutted upwards."
"Alexia found her place, bending forward at the hips to plant her mouth upon his swaying tip. Greyhide let out a soft gasp at her unexpected appearance. Smiling, she took him in hand and jerked at his manhood, still wet from the saliva of her husband."

gh "{i}Unnnh{/i}-"

"The bull bounced upon Rowan’s lap, his heavy weight always teasingly coming to rest against his hips before drawing upwards again. Just a little extra weight and he could crush Rowan’s pelvis, but he was remarkably restrained."
"Rowan’s hands found purchase on his large hips, guiding him up and down, up and down in long strokes as Alexia gave Greyhide a spirited blowjob. Rowan was, for all intents and purposes, trapped beneath the bull’s weight… and loving every minute of it."
"Alexia’s hands were a blur as they jerked him hard, sliding up and down the full length of his manhood while she passionately made out with his cock tip. After a long stretch of oral loving, she kissed the tip and pulled back."

al "{i}Mwah{/i}!"

al "Goddess fend, I never thought I’d get to see you two like this."

"Her hands trailed across his chest, running through his fur and caressing his face. He turned to look at her and she took the opportunity to lean up and kiss his snout."

gh "{i}Rrrh{/i}- L-little one..."

al "Shhh… keep going, I want to see how it ends."

"She stroked his cheek a moment, then bent down once more to suckle at his cock. Her hands strayed downwards, cupping one of his hanging orbs, running her fingernails across them and only adding to his sensitivity."
"Rowan couldn’t hold it any longer. He felt the bull’s weight above him with a relentless, bouncing beat. Each time he sank deep into Greyhide’s ass, he felt his cock twitch and swell, building to a budding orgasm."

#cg2 - cum var
scene black with fade
show rowan necklace naked aroused behind black
show alexia necklace naked aroused behind black
show greyhide neutral behind black

"But - to {i}everyone’s{/i} shock - Greyhide came first. His breath pumped heavily in his chest as his body tensed up. His balls clenched and his arms strained. Alexia felt him through her fingers, his mammoth cock bulging as it swelled, rose, then burst like a dam."
"He thrust once, twice, {i}three{/i} times in her hands, then erupted, spurting forth a monstrous stream of seed that sprayed into the air and splattered across Alexia’s face and chest, as well as his own. Rowan was not far behind. "

ro "{i}Hnnngh{/i}!"

"He thrust and humped and erupted within the Minotaur’s ass. He felt building pillar of pleasure as Greyhide thrust downwards and held, keeping him deep within. They grinded against one another, his load firing forth in unhindered spurts deep within him."
"That was only the first titanic burst, however. Soon a second stream of Greyhide’s cum shot upwards, coating his groin and chest. He was a mess, made doubly so by the anal stimulation."
"Alexia - herself so aroused that she’d been fingering herself - came last, a final feminine elucidation of their lust as she reveled in the scent and smell of masculine ejaculate all around."
"Rowan collapsed upon the bed, followed soon after by an equally-spent Greyhide. He remained inside the bull, chuckling at the feel of his slim tail tickling his stomach."
"Alexia crawled into Greyhide’s arms, allowing the three of them to spoon together on the oversized bed."

gh "That was…"
gh "I have never felt like that before."

"Rowan let out a breathless chuckle, putting a hand to his forehead to wipe away the sweat he found there."

ro "You and me both."

al "That was… {i}amazing{/i} to watch."

ro "I can’t feel my legs."

al "You two make a cute couple."

ro "-And you don’t?"

gh "You are plenty ‘cute,’ little one."

al "Maybe, but that was something else."

"They laid together for a moment, enjoying the simple pleasure of being with one another. Rowan wrapped his arms around Greyhide, who cradled Alexia in his arms in turn."
"They lay like that, panting and gasping in tune to one another for some time after that. They were exhausted, drained in body and spirit from all that had happened that day."
"But… they were together. They had all admitted their feelings, and they were resolved to one other. That alone had made the whole ordeal worth it."

scene bg22 with fade
show greyhide neutral at center with dissolve

"After they’d cleaned up, the couple dozed on Greyhide’s bed. The bull - careful not to wake either of them - pulled his woolen blanket over them both and let them rest."
"He walked, a little unsteadily to his work stool, and sat down. Staring at Rowan and Alexia in the warm light of the forge, a soft smile graced his lips."

gh "Sleep well… my loves."

return

##########################################################################

label greyhideFinalePolyAlexiaSex:

al "Why don’t we… take this somewhere more comfortable?"

ro "Yes, lets."

"The couple seemed to be of one mind on the matter. Each took a hand of the burly Minotaur and led him, laughing to his bedside."

ro "So Greyhide, since everything’s out in the open now, I’ve got a question."
ro "What’s your favorite part of my wife?"

al "R-{i}Rowan{/i}!"

"Alexia went beet red, her eyes flicking from Rowan to Greyhide with flustered indignance."

gh "Her kindness."

show alexia 2 necklace happy at edgeleft with dissolve

al "Aww."

ro "Kiss ass."

show alexia 2 necklace angry at edgeleft with dissolve

al "Keep that up - {i}beloved{/i}, and you’ll never get another chance to kiss it."

show rowan necklace happy at midleft with dissolve

ro "Dearest wife, your beauty outshines the world."

show alexia 2 necklace happy at edgeleft with dissolve

al "Better."

gh "-Oh! You meant physically."

show rowan necklace neutral at midleft with dissolve

gh "I prefer her teats."

show alexia 2 necklace shocked at edgeleft with dissolve

al "..."

show rowan necklace happy at midleft with dissolve

al "O-one word out of you Rowan Blackwell, and I {i}swear{/i}-"

ro "Say Greyhide."

gh "Yes, Rowan?"

ro "I get the feeling my wife wants to be in control this evening."

gh "I think you are right. "

ro "Shall we indulge her?"

show alexia 2 necklace aroused at edgeleft with dissolve

al "That’s it! On the bed, both of you!"

"Flashing a cocky grin at his wife, Rowan tore off his clothing and strutted over to the bedside. Greyhide apologetically complied as well, shuffling over and taking a seat next to him once he’d removed his loincloth."

show rowan necklace naked at midleft with dissolve

"Alexia pulled off her clothing with halting annoyance, doing her best to act annoyed when she was clearly embarrassed beyond belief. She did her best to keep up the tough girl act."

show alexia necklace naked angry at edgeleft with dissolve

al "Lie back. Rowan, flip around to the other side."

ro "Yes, dear."

al "And no more back talk!"

ro "I wouldn’t {i}dream{/i} of it."

"Chuckling, Rowan flipped himself around so that his cock was roughly level with Greyhide’s head, and he in reverse. Their matching erections pointed up like an arch."

#cg1
scene black with fade
show rowan necklace naked behind black
show alexia necklace naked angry behind black
show greyhide neutral behind black

"After a moment’s hesitation, Alexia clambered up onto Greyhide’s lap. She could not conceal the full body blush that covered her skin as she straddled him, setting her crotch purposefully on top of his manhood. "

ro "…Is this your punishment, beloved? Did I go too far?"

al "Bad husbands have to wait their turn. You can touch yourself in the meantime."

ro "Now that’s just cruel."

"Alexia rolled her eyes at Rowan’s teasing smile. She leaned over, taking hold of his erect cock. He let out a low grunt, his breath shortening as she began to jerk him in short bursts."

al "...Satisfied?"

ro "No, but now I’m willing to wait my turn."

gh "You may take your turn first if you really wish it, friend Rowan."

ro "And risk {i}her{/i} wrath? No thank you. Just enjoy the ride."

"Her husband was an arse. Alexia was convinced of that. However, she was also {i}agonizingly{/i} wet, and Greyhide’s thick cock settled beneath her like a magnet to her womanhood." 
"Ignoring the amused glint in Rowan’s eye, she began to shift her hips back and forth atop the bull. The teasing repartee soon gave way to tender humping, her glistening lips sliding up and down, up and down the length of the bull’s erection."
"{i}However{/i} mad he made her, Rowan was still her husband. She might still have been reveling in the novelty of Greyhide’s massive dick, but she was nonetheless attracted to her first love’s as well. "
"However begrudgingly, she continued to jerk him off, sticking her tongue out at him as payback for his childish antics. Rowan rewarded her by leaning back, displaying the toned athleticism of his form in stark contrast to Greyhide’s thick, muscled body."
"She reveled in the sensation of control, of straddling two males who were equally infatuated with her. The sensation was empowering… and {i}deeply{/i} arousing. Her hands were clenched around cock, her hips and ass were sliding across it, her own womanhood was tantalizingly close to penetration."
"Greyhide groaned, his hips shifting forward even as Alexia drew back, adding a pleasing friction to her slow slide across his cock."
"His hand reached up, kneading the flesh of her ass, urging her ever onwards into longer and deeper strokes across the top of him. His heavy grip was so comforting, his thick digits digging deep into her flesh with the most gentle application of pressure."
"Their simulated coitus was slow, passionate. As Alexia looked down at her husband she saw the beginnings of a blush to creep across his face. He was staring at her, watching her move up and down, riding the bull as she jerked him off. His eyes lidded."

show rowan necklace naked aroused behind black

ro "You’re beautiful, beloved."

show alexia necklace naked aroused behind black

al "{i}Mmmh{/i}! D-don’t forget it."

"Her fingers curled around his cock, threading down low as she bent her back forward to briefly fondle his balls. Rowan’s back arched, his body tensing from the unexpected contact." 
"As she did so she slid farther back, her hips connecting hard against Greyhide’s stomach. The bull was equally enthralled, his hands sliding up to gently grab her hips and aid in her humping motion."
"The sensation was electricity, pure pleasure. A teasing thread of implied penetration came at the apex of each hump, as the tip of Greyhide’s cock brushed in brief contact with the clenching hole that slid across it, kissed briefly, then drew forward once more."

gh "So… soft. Little one, you- {i}hrnh{/i}!"

"Alexia rolled her hips, her hand moving even faster as it jerked Rowan off with harried speed. She needed him. She needed both of them. The men she’d fallen for, the couple now forged into three."
"Her humping sped up, building to a crowning crescendo that culminated in her body tensing up, her back arching as she let out a cry of elation. She came, shuddering, trembling atop Greyhide’s grip. It was almost  too much for her."
"Rowan sat up off the bed, pulling Alexia into his arms as she suffered through the torturous elation elicited by her body’s natural reaction to the men around her. He held her close, her breasts squishing tight to his chest as she cotinued doing what she was doing."

ro "Get over here, spread those legs."

"Breathless, rendered helpless by her own desperate need to fuck, she could do little but comply."

#cg2
scene black with fade
show alexia necklace naked aroused behind black
show greyhide neutral behind black

"Rowan turned himself around on the bed, facing Greyhide. He pulled Alexia into his lap, angling himself against her insides even as her face fell into Greyhide’s lap." 
"Her lips met the bull’s half-wettened cock at the same moment Rowan’s dick slid smoothly into her quivering quim. A loud {i}squelch{/i} announced the commencement of the second round of their collective lovemaking."

al "{i}Mmmh{/i}-"

"She felt the blissful penetration, her legs spreading wide as Rowan humped into her. He slid deep within her with a perfect, pleasing conncetion, their lovemaking only enhanced by the addition of a third party to the mix."
"That third party was {i}thoroughly{/i} enjoying himself, at Alexia’s mercy. Her hands encircled his thick, bulging cock, her fingers gripping tight to his manhood as she jerked him up and down in long, sure strokes."
"Encouraged by the gentle {i}moos{/i} and soft grunts of her husband at her flank, Alexia leaned in and kissed Greyhide’s cock. She could taste herself on his hardness, a lingering tang of feminine lust that had splattered itself across him in the throes of her earlier ecstasy."
"Rowan’s thrusts were slow, deep, methodical. He knew how to pleasure his wife, knew her most intimate responses to the back and forth of their romantic connection. Every time he moved in her, she felt her nerves light up little electric tingles within her tummy."
"Whatever cheeky conflict they had engaged in prior to the onset of their desperate mating was forgotten, lost in the passion with which one another met in the middle."
"Her hips pressed tight against his, wiggling back and forth even as he thrust hard against her, using her outstretched leg as leverage."
"Greyhide put a heavy hand upon Alexia’s head, gently urging her onwards as her kisses and licks grew ever bolder. She fondled his balls, kissed the tip of his dick, gripped him by the base and jerked him in fast, furious strokes."
"Each action elicited still further grunts from the gentle giant, which only further encouraged her. She suckled at the tip of his cock, rolling her tongue across his slit and delighting in the salty taste of what came out."

gh "{i}Hrrnh{/i}- L-little one-"

"She refused to relent, jerking him off with both hands as she licked and kissed and nibbled at his towering meat. Rowan’s thrusts grew shorter as his breath hissed out through gritted teeth."
"Alexia was no better. Her body was aflame, her every nerve ending {i}screamed{/i} for release. It was like a deep pressure was building in her chest, an echo rebounding back and forth louder and louder until it could no longer be contained within her."
"Her pussy clenched, her body going rigid as she let out a light squeal of joy. She was no longer in control. Maybe she’d {i}never{/i} been in control. The two males that surrounded her with their warmth were both on the verge of cumming, yet she was the first to let loose."

al "{i}Aa-aaaaaahhhn{/i}!"

"Her shameful screech brought a fierce blush to her face, but neither of her lovers seemed to mind. If anything, it only encouraged their rapidly-arriving orgasms."

gh "{i}Hrmmh{/i}!"

#cg2 - cum var
scene black with fade
show rowan necklace naked aroused behind black
show alexia necklace naked aroused behind black
show greyhide neutral behind black

"Greyhide - to Alexia’s shock - came first. His breath pumped heavily in his chest as his body tensed up. She felt him through her fingers, his mammoth cock bulging with heat and bull sperm as it swelled, rose, then burst like a dam."
"He thrust once, twice, {i}three{/i} times in her hands, then erupted, spurting forth a monstrous stream of seed that sprayed into the air and splattered across Alexia’s face and chest. Rowan was not far behind."

ro "{i}Aaaah, fuck{/i}-"

"He thrust and humped and erupted within her, his cock swelling, twitching, then pulsing inside her shuddering womanhood."
"She felt the warm rush of his seed shoot deep within her, even as his humping continued unabated, ensuring his seed was planted as deeply as could be within his loving wife."
"That was only the first titanic burst, however. Soon a second stream of Greyhide’s cum shot upwards, coating both him and Alexia in his lust. Rowan pulled out of Alexia, allowing his second load to shoot across her groin and legs, coating her in masculine cum."
"Alexia collapsed upon the bed, followed soon after by her equally-spent husband. Greyhide, his knees trembling, laid back on the bedside next to them, breathless by the ordeal."

al "L-let that- be a… {i}lesson{/i} to you!"

"Alexia’s gasping retort sounded weak and halfhearted, even in her own ear. Rowan bent down kissed her nose, mussing her hair with his hand."

ro "Beloved, I’ve learned nothing."

al "Ugh. You’re hopeless."

ro "That was..."

show rowan necklace naked behind black

ro "Intense?"

gh "Words do not describe it."
gh "It was wonderful."

"The couple laid together for a moment, enjoying the simple pleasure of being with one another. Eventually, a shaky beckon from Alexia compelled Greyhide to join them, who scooped them up in his arms as the three cuddled together on the bed."
"They lay like that, panting and gasping in tune to one another for some time after that. They were exhausted, drained in body and spirit from all that had happened that day."
"But… they were together. They had all admitted their feelings, and they were resolved to one other. That alone had made the whole ordeal worth it."

scene bg22 with fade
show greyhide neutral at center with dissolve

"After they’d cleaned up, the couple dozed on Greyhide’s bed. The bull - careful not to wake either of them - pulled his woolen blanket over them both and let them rest."
"He walked, a little unsteadily to his work stool, and sat down. Staring at Rowan and Alexia in the warm light of the forge, a soft smile graced his lips."

gh "Sleep well… my loves."

return

##########################################################################

label greyhideFinalePolyGreyhideSex:

al "Why don’t we… take this somewhere more comfortable?"

ro "Yes, lets."

"The couple seemed to be of one mind on the matter. Each took a hand of the burly Minotaur and led him, laughing to his bedside."
"Together the couple divested him of his loincloth, peeling off his clothing even as his hands idly trailed across them both, groping and squeezing with a gentle touch."

gh "You two are so… soft."

ro "Funny, cause you’re pretty hard."

"Alexia giggled, lightly slapping her husband's shoulder in playful rebuke."

al "{i}Rowan{/i}!"

ro "Am I wrong?"

al "Hehe… I guess not."
al "Goodness, you’re big."

ro "Now I’m getting jealous."

al "Oh {i}stop{/i}. You’re big too."

"A teasing gleam entered Alexia’s eyes as she stripped out of her clothes."

show alexia necklace naked aroused at edgeleft with dissolve

al "...For your size."

"Rowan faked a pained wince as he followed suit."

show rowan necklace naked aroused at midleft with dissolve

ro "Ouch. My pride."

gh "You have a very pretty cock, Rowan."

ro "See? {i}He{/i} likes it!"

al "Greyhide’s just trying to get on your good side."

gh "What is wrong with that?"

ro "Traitors, the both of you."

"Their teasing banter soon gave way to pleasured marveling at one another’s nakedness. Here they were, the three of them: together."

al "Where should we start, husband of mine?"

ro "I’ve got a few ideas."

al "Mmm, I bet you do. Why don’t you show me where {i}you two{/i} got started?"

ro "About the same place you did, I expect."

"Chuckling, the couple surrounded the bull. Greyhide, for his part, was rendered speechless by their seductive approach. They pushed him back onto the bed."

#cg1
scene black with fade
show rowan necklace naked aroused behind black
show alexia necklace naked aroused behind black
show greyhide neutral behind black

"Alexia clambered up next to him, nuzzling his crotch with her nose as she planted a dainty kiss upon his heavy shaft." 
"Rowan chose a spot between Greyhide’s knees, spreading the bull’s legs apart before reaching out to palm his hefty balls."

gh "{i}Hmmh{/i}!"
gh "You… y-you do not need to focus on me. I want to make you feel good as well."

al "Hush now, tonight’s for you."

ro "That can come later."

"Together, husband and wife set to the supremely satisfying task of pleasuring the old Minotaur. Their mouths met his skin simultaneously, coming at it from vastly different angles."
"Alexia attacked the problem from the top, lifting her head to plant a wet kiss upon his flat tip. She leaned into his lap, settling into his groin like she was reclining on a couch."
"Rowan, meanwhile, focused on his lower nethers, licking along the seam of his testicles before leaning close to passionately kiss the vein at the base of his shaft."
"Greyhide moaned, settling his hand on the top of Rowan’s head while the other gently trailed down the length of Alexia’s bare back."
"Feeling adventurous, Rowan leaned in and planted a suckling kiss on one of Greyhide’s bulging testicles. He rolled his tongue across the virile orb, reveling in the salty taste of his sweat on his tongue."
"Not to be outdone by her husband, Alexia began to worship of his bulging bullcock. She licked up and down his length in long drags of her tongue, coating his dick in a layer of saliva."
"The Minotaur was rendered helpless by the couple’s equally ardent oral. No sooner had one finished in one spot than the other had moved elsewhere to pleasure the thoroughly overwhelmed bull."
"At one point, their lips met in the middle, tongues intertwining as lips slid across Greyhide’s cock as easily as they did one another’s mouths. The two traded a long, passionate kiss, before returning to their appointed task with gusto."

al "{i}Mwah{/i}!"
al "G-goddess, I never knew this could be so…"

ro "Erotic?"

al "Fun!"

"She wasn’t wrong. If Greyhide wasn’t as large as he was, they might have struggled to share. As it stood, there was plenty of cock to go around for the both of them."
"Alexia opened her mouth as wide as it could go and did her best to swallow Greyhide’s cock. She wasn’t quite able to get it down her throat, but the spirited effort was more than enough to get Greyhide squirming."
"Rowan cupped the bull’s balls in both hands, massaging them back and forth as he licked along his length, ensuring not one inch of his throbbing manhood was lacking in attention."
"Greyhide panted through his nose, his eyes fluttering through sheer sensory overload. The bull let out a heavy snort, then sat up in a rush."

gh "On the bed. Both of you."

"The couple shared a shocked look, but quickly complied. Greyhide’s voice had taken on a peculiar, dominant tone. One that would brook no defiance."
"Alexia, already on the bed, positioned herself on her hands and knees, raising her rump high in the air in preparation for imminent pounding. Greyhide’s open palm {i}spanked{/i} her hard across her asscheek, and she let out a breathless yelp."
"Rowan took a little too long in getting into position. Greyhide seized him by his narrow hips and hefted him onto the bed, stacking him atop Alexia in a pile of human lust."

#cg2
scene black with fade
show rowan necklace naked aroused behind black
show alexia necklace naked aroused behind black
show greyhide neutral behind black

"Greyhide did not even wait for the two to be properly situated before he thrust his painfully hard erection between them. The wet cock slid between their bodies with a pleasing, slippery salience."

ro "O-oh fuck-"

"Greyhide’s hips connected heavily against their collective rumps, shoving both humans down onto the bed and nearly toppling them hard on top of one another. His thrust was hard and heavy, a vigorous expression of his masculine might."
"Alexia’s spine tingled with the hot, almost burning feel of Minotaur’s cock sliding down her lower back. Rowan shivered as he felt the bull’s length drag across his undercarriage, briefly brushing across the length of his cock before drawing back behind him once more."
"But this was only the beginning. Greyhide let out a deep grunt, and thrust again, effortlessly propelling the couple forward together, simulating to both simultaneously the sheer, rutting strength of their shared bed partner."

al "{i}Aaah{/i}!"

"Alexia’s back curled in surprise as something heavy slapped against it. It took her a moment to realize it was Greyhide’s furry nutsack, his latest thrust propelling it hard enough against her to give her the briefest feeling of sexual contact against her soaking womanhood."
"Rowan struggled to remain static, trapped in place with Alexia beneath him and Greyhide at his flank. The bull did not say anything as he thrust against them, utterly confident in his ability to please both lovers at the same time. Judging from how hard Rowan was… he was succeeding."

gh "...Rowan."

"Greyhide’s deep voice rumbled in his chest, sending shivers down the couple’s spines from the vibration. He put a heavy hand upon Rowan’s back, drawing his fingers low, to feel his lower spine and grope his supple ass."

gh "Put it in her."
gh "I want to see you with her."

#cg2 - var 1
scene black with fade
show rowan necklace naked aroused behind black
show alexia necklace naked aroused behind black
show greyhide neutral behind black

"The bull drew back his hips, giving room for Rowan to reorient himself at Alexia’s flank. Alexia moaned, using the brief interlude to run a hand across Rowan’s side and slide a pair of naughty fingers deep into her clenching twat."
"He planted himself on top of her like a dog ready to mount. He slid in effortlessly, his cock reaching deep inside as it belonged. Alexia’s moan turned into a gasp of pleasure, her body shuddering with the contact."
"For whatever reason, knowing Greyhide was there, waiting behind them made the sex that much more intense. Within moments Rowan was rutting against her, humping with short, sure thrusts into the depths of her womanhood."

ro "Aaah, A-alexia!"

al "Rowan! Oh Goddess, {i}Rowan{/i}!"

"Their voices were on the edge of hearing, quiet whispers to one another like they had in the old days, when their love first blossomed. The bull let out an appreciative grunt, reaching out to caress first Rowan’s hips, then Alexia’s bottom. His lips spread wide into a horny grin."

gh "Beautiful."

"The Minotaur took hold of Rowan’s hips and thrust against them, adding his own weight to the frantic lovemaking. Alexia let out a squeal of joy as Rowan inadvertently reached into her deepest spot. Her knees began to tremble."
"Greyhide’s length ran down the line of Rowan’s asscrack, sliding effortlessly along his back as the bull indulged in a series of short, hard thrusts. Rowan and Alexia were helpless in his grasp, pinned in place and propelled forward by his weight."
"The bull drew back, and Rowan drew back, and Alexia took in a shuddering breath. Then, Greyhide slammed his hips forward, shoving Rowan deep inside Alexia, who cried out in breathless pleasure. And on and on the process repeated itself."
"They were one. It was a strange, exhilarating, almost {i}alien{/i} sensation: three lovers, in perfect sync, having sex with one another in the truest meaning of the wording. Equally attracted to each other, each uniquely drawn to the others."

al "{i}Hah… hah… hah…{/i}"
al "I can’t- I-I can’t- I can’t {i}breathe{/i}!"

gh "Calm yourself, little one. We are here."

ro "{i}Aaah{/i}-"

"Rowan, responding to Greyhide’s words, wrapped his arms around Alexia, whose gasping breath was on the very verge of orgasm. She settled back against him, leaning flush with his body even as Greyhide continued to thrust."

al "I-I love you!"

ro "I love you too."

gh "{i}Hrmh{/i}. I love you both."

"Their tawdry exchange was so embarrassing that they all began to laugh, briefly breaking the tempo, before Greyhide righted them back on course, his certain thrusts bringing them back to the passion of the moment. "
"Alexia came first, setting off a chain reaction that soon spread to her bedpartners. Her trembling orgasm was so intense her eyes rolled for a moment as her jaw slackened. Rowan felt the tightness constrict like a vice, and then he was off."

#cg2 - cum var
scene black with fade
show rowan necklace naked aroused behind black
show alexia necklace naked aroused behind black
show greyhide neutral behind black

ro "{i}Aaaah, fuck-{/i}"

"He erupted within her, his cock swelling, twitching, then pulsing inside her shuddering womanhood. Even as he came Greyhide kept thrusting forward, ensuring Rowan’s seed was planted as deeply as it could be within his loving wife."
"Greyhide came last, his breath pumping heavily in his chest as if he were rising to a gallop. He thrust once, twice, {i}three{/i} times, then erupted, spurting forth a monstrous stream of seed that lifted into the air and splattered across Rowan’s back."
"That was only the first titanic burst, however. Soon a second stream shot past Rowan’s shoulder, nearly nicking his cheek as some of it got in Alexia’s hair. Greyhide pulled back, holding himself in his hand as he shot the next load across Rowan and Alexia’s flank and back."
"Alexia collapsed upon the bed, followed soon after by her equally-spent husband. Greyhide, his knees trembling, slowly lowered himself onto the bed next to them, left breathless by the ordeal."
"The couple, still coated in (or even still actively leaking) sexual juices, fell into one another’s arms. A shaky beckon from Rowan compelled Greyhide to join them, who scooped them up in his arms as the three cuddled together on the bed."
"They lay like that, panting and gasping in tune to one another for some time after that. They were exhausted, drained in body and spirit from all that had happened that day."
"But… they were together. They had all admitted their feelings, and they were resolved to one other. That alone had made the whole ordeal worth it."

scene bg22 with fade
show greyhide neutral at center with dissolve

"After they’d cleaned up, the couple dozed on Greyhide’s bed. The bull - careful not to wake either of them - pulled his woolen blanket over them both and let them rest."
"He walked, a little unsteadily to his work stool, and sat down. Staring at Rowan and Alexia in the warm light of the forge, a soft smile graced his lips."

gh "Sleep well… my loves."

return