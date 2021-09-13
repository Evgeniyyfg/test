init python:
    
    event('cliohnas_Summons', triggers="week_end", conditions=('cliohnaSubmission >= 2',), depends=('another_visit_to_Cliohna',), group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="images/Backgrounds/library.jpg")
    

label cliohnas_Summons:

$ researchNotPicked = True
$ jezFavourNotPicked = True
$ AndrasFavourNotPicked = True
$ EquipmentNotPicked = True
$ DriderConditioningNotPicked = True


scene bg9 with fade

"Again, he received a letter from Cliohna. But unlike the usual evening summons, this one arrived in the morning, with explicit orders not to come till the sun set."

if Hypnosis2DomEnding == True:
    show rowan necklace concerned at center with dissolve
    "He shouldn’t be worried, but he was. He stared at the small, pointed letters, and could almost see Cliohna’s slender fingers working the quill, every dot and dash made with barely restrained annoyance."
    scene bg14 with fade
    "He folded the letter and burned it with one of the torches that illuminated the castle corridors. He should not have denied her last time. The wall between them was his doing, not hers."
    show rowan necklace concerned at center with dissolve
    "And for what? He couldn’t forget the disappointed, almost hurt look in her eyes. Yes, she was going too far, but… Maybe he was just overreacting? Maybe it was wrong of him to suspect her of ill intentions?"
    scene bg6 with fade
    show rowan necklace concerned at center with dissolve
    "… Or was he underreacting? Cliohna did not hesitate to use force to get what she wanted. To see her so invested in him… Maybe he should be worried?"
    show rowan necklace angry at center with dissolve
    "No matter how much he pondered on the matter, he could find no answer that satisfied him in full."
    "His only reward was a day wasted: More than once he found himself reading the same report twice, and in his absent-mindedness he was fairly certain he just allowed Cla-Min to scam the castle maids out of their savings."
    if alexia_away_weeks > 0:
        if all_actors['alexia'].corruption > 30:
            show rowan necklace concerned at center with dissolve
            "Even Alexia noticed he was out of it. He made up some weak excuse on how he was worried about orc equipment, but the playful smile she rewarded him with told him she wasn’t buying it one bit."
        else:
            #add if alexia is being trained as a spy
            #if all_actors['alexia'].corruption > 30:
                #deception test 7 - TO DO
                #success
                #pass
                #fail
                #show rowan necklace concerned at center with dissolve
                #"Even Alexia noticed he was out of it. He made up some weak excuse on how he was worried about orc equipment, but the but the sharp look in her eyes told him she wasn’t buying it one bit."
                #lower Alexia x Rowan score moderately. 
            #else
            #deception check 5 - TO DO
            $ res_roll = dice(6)
            if res_roll > 3:
                pass
            else:
                show rowan necklace concerned at center with dissolve
                "Even Alexia noticed he was out of it. He made up some weak excuse on how he was worried about orc equipment, but the dubious look on her face told him she wasn’t buying it."
                $ change_relation('alexia', -5)
                
        scene bg14 with fade
        show rowan necklace neutral at edgeleft with dissolve
        "Hours ticked by, but the relentless march of time brought him no answers, only an odd cocktail of uneasy, giddy anticipation, and nagging, festering fear." 
        "Inadvertently, his hand tended to reach for the amulet at his neck. Maybe…. Maybe there was little point in being overly cautious?" 
        "One more session, he promised himself. Then he’ll decide if it was worth the risk. “Just one more session”… He kept silently mouthing the words as he headed for her room, a quiet mantra to steady his step."
        scene bg12 with fade
        show rowan necklace shock at edgeleft with dissolve
        show cliohna happy at edgeright with dissolve
        "And Gods, did he need it. The moment he opened the doors, and saw the glimmer of excitement in her sharp, cold eyes, he knew it won’t be easy quitting her for good."
        show rowan necklace neutral at edgeleft with dissolve
        show cliohna neutral at edgeright with dissolve
        cl "Ah, Rowan, you’re early. I feared you would tally after your last hasty retreat. I am glad the opposite proved true. Please, do take a seat."
        show rowan necklace neutral at midleft with moveinleft
        "She closed the tome she was holding and pointed to a chair in front of her desk. He did so without a word, and followed her with his eyes as she took her sweet time putting the library books away."

else:
    show rowan necklace aroused at center with dissolve
    "Such insidious torture. He tried to go through his day as normal, but he could not focus on any of the tasks he had set for himself."
    if alexia_away_weeks > 0:
        if all_actors['alexia'].corruption > 30:
            "Even Alexia noticed he was out of it. He made up some weak excuse on how he was worried about orc equipment, but the playful smile she rewarded him with told him she wasn’t buying it one bit."
        else:
            #add if alexia is being trained as a spy
            #if all_actors['alexia'].corruption > 30:
                #deception test 7 - TO DO
                #success
                #pass
                #fail
                #show rowan necklace concerned at center with dissolve
                #"Even Alexia noticed he was out of it. He made up some weak excuse on how he was worried about orc equipment, but the but the sharp look in her eyes told him she wasn’t buying it one bit."
                #lower Alexia x Rowan score moderately. 
            #else
            #deception check 5 - TO DO
            $ res_roll = dice(6)
            if res_roll > 3:
                pass
            else:
                show rowan necklace concerned at center with dissolve
                "Even Alexia noticed he was out of it. He made up some weak excuse on how he was worried about orc equipment, but the dubious look on her face told him she wasn’t buying it."
                $ change_relation('alexia', -5)
    scene bg6 with fade
    show rowan necklace concerned at midleft with dissolve
    "It was embarrassing, really. He was acting like a horny teenager, impatiently awaiting the next tryst with his new lover. But he just couldn’t get his mind off her words from last time."
    show rowan necklace aroused at midleft with dissolve
    "She told him she had another “Ingenious” plan she wished to test out. Spent from their earlier session, he denied, out of fear she’d milk him dry. But now… He couldn’t stop thinking what would have happened had he stayed."
    show rowan necklace concerned at midleft with dissolve
    "He shouldn’t be like this. He shouldn’t be so… Unconcerned with being a toy, a plaything."
    scene bg14 with fade
    show rowan necklace concerned at midleft with dissolve
    "And he most certainly shouldn’t be walking to her room the moment the sun went over the horizon. He slowed his step, throwing a passing orc a hostile look, paranoid something in his expression betrayed the giddy, uneasy excitement he didn’t want to acknowledge. "
    "It had to be magic. Never in his life did he face a enchantment he couldn’t break, but he could see no other explanation. He had to put an end to it, before the problem grew any worse."
    show rowan necklace neutral at midleft with dissolve
    "Just one more session… Then he’ll put an end to it."
    scene bg12 with fade
    show rowan necklace happy at edgeleft with dissolve
    show cliohna happy at edgeright with dissolve
    "Finally at her door, he steeled his heart, reading himself for another evening with his Cliohna. He opened the door - and walked right into the sorceress. Her eyes briefly glimmered with excitement, just at the sight of him."
    cl "Ah, Rowan, you’re early. Please sit down and wait."
    show rowan necklace neutral at midleft with moveinleft
    show cliohna neutral at edgeright with dissolve
    "She closed the tome she was holding and pointed to a chair in front of her desk. He obeyed without a word, and followed her with his eyes as she took her sweet time putting the library books away."

show rowan necklace aroused at midleft with dissolve

"He’d swear she was intentionally picking the lower shelves, just so she could sway her ass right in front of him."

if Hypnosis2DomEnding == True:
    show rowan necklace neutral at midleft with dissolve
    cl "I suppose you are simply eager to learn if I’ll try to repeat our last session, or if I’ll perhaps try a new experiment."
    
else:
    show rowan necklace neutral at midleft with dissolve
    cl "I suppose I shouldn’t be surprised by the sudden arrival. You are no doubt eager to hear what our newest experiment will be."
    
"The thong strap that had no right to be part of a respectable sorceress outfit revealed everything as her firm bottom danced before his eyes."

show rowan necklace aroused at midleft with dissolve

"Ass hypnosis, he decided. It had to be ass hypnosis."

cl "Then I fear you will be disappointed to learn, that there will be no more of them."
    
"Did she exercise to keep them in such good shape? She’d never seen her do so, but it-"

show rowan necklace shock at midleft with dissolve

"What?"

show cliohna neutral at cliohnaright with moveinright

"He shifted in his chair uneasily as she took her own seat. A neatly written file rested on the side. She slid it over to him, the placed her fingers together, and watched him through half lidded eyes as he tried to make sense of the pages of notes."  

show rowan necklace concerned at midleft with dissolve

cl "I have reviewed the collected material extensively, and decided there’s enough of it to draw certain conclusions. As a brief reminder, the goal of these experiments was to determine the source of your extraordinary mental resilience."
cl "And to put the matter bluntly, you, Rowan Blackwell, are perfectly normal."
cl "You possess no magical abilities, no affinity for the craft, no innate power, nothing. You have no magical protections on you, no magical items, and no hidden runes that activate under magical pressure."
cl "You have no nonhumanoid ancestry, and no humanoid non-human ancestry. There is not a drop of dragon, demon, celestial or fae blood in you, that could manifest as latent defensive powers."
cl "Finally, there is no holy or unholy protection on you. At least none I could detect, which rules out most Gods."
cl "You are a textbook example of a horribly mundane, magically inept, regular human being."

if Hypnosis2DomEnding == True:
    cl "Who, after repeated, deep magical inductions, was still perfectly capable of shaking off my magic with almost laughable ease."
    ro "Cliohna, I-"
    show rowan necklace shock at midleft with dissolve
    show cliohna happy at cliohnaright with dissolve
    cl "I have also tested you for subterranean heritage, as the combination of stubbornness and insufferability is usually only found among dwarves. Alas, the results came back negative." 

else:
    cl "… And yet somehow, through some unclear though likely innate means, you have, time and time again, proved capable of breaking out of various types of highly sophisticated mind control."
    if cliohnaResistance == 3:
        cl "Even if you did, repeatedly, appear to be taking your sweet time. Would you mind shining some light on the reason behind said delay, Rowan?"
    else:
        cl "Cliohna: Even if you did, at times, appear to be taking your sweet time. Would you mind shining some light on the reason behind said delay, Rowan?"
        
menu:
    "Her spells are difficult to break.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "It’s powerful magic, Cliohna. I might have some skill, but it’s not easy to resist someone like you."
        if Hypnosis2DomEnding == False:    
            show cliohna happy at cliohnaright with dissolve
        cl "So I’ve been told, though mostly by people who wished to derive me of my underwear."
        
    "Avoid answering.":
        $ released_fix_rollback()
        show rowan necklace concerned at midleft with dissolve
        ro "It’s… Not an exact science, Cliohna. I do my best to break out, but sometimes it takes a while."
        show rowan necklace shock at midleft with dissolve
        cl "One would think a infallible mental defence would be more reliable. How silly of me."
        
"The light hearted joke took him aback. After such a rant he expected her to explode, but… Nothing seemed to come."

show rowan necklace neutral at midleft with dissolve
show cliohna neutral at cliohnaright with dissolve

ro "You seem rather… Tranquil about this. "

if Hypnosis2DomEnding == True:
    cl "It would petty of me to fuss over your recent disobedience, given how fruitful our initial experiments were. And as for the end result, I had my time to process the revelation."
    show cliohna angry at cliohnaright with dissolve
    cl "I will not pretend it was not upsetting. I have put much time and effort into this project, and to have nothing to show for it… One could only label the whole thing a complete and utter failure."
    
else:
    show cliohna angry at cliohnaright with dissolve
    cl "I had my time to process the revelation. I will not pretend it was not upsetting. I have put much time and effort into this project, and to have nothing to show for it… One could only label the whole thing a complete and utter failure."
    
cl "... At least that’s how I had viewed it at first."

"Cliohna pushed herself upwards. Even though she talked of disappointment, her gaze burned with the same intense anticipation that preceded their earlier sessions."

show rowan necklace concerned at midleft with dissolve
show cliohna neutral at cliohnaright with dissolve

ro "Cliohna?"

"She took a short stroll around the table, stopping right before him. Rowan scrambled to his feet, but Cliohna waved her hand, ordering him to remain seated.  The sorceress leaned against the table, her bare leg momentarily brushing against his own."

cl "When we started this little project, it was my ambition to sink my fingers into your head, and not stop digging until I discover something groundbreaking."

if cliohnaDeeper == True:
    "His mouth grew perched - her covered pussy was now right before him.  He still recalled the tightness of her slit as she rode him, the wet, hot pleasure, mixed with hypnotic magic to amplify the experience."
    
else:
    "His mouth grew perched - her covered pussy was now right before him. He still recalled the hotness of her slit, as he pressed his tongue against it, licking and prodding without thought, ensorcelled by both lust and magic."
    
cl "-some great secret, that would prepare me for the work I will need to do in Prothea. In that, I have failed."
cl "But what I have found instead… "

show rowan necklace shock at midleft with dissolve
show cliohna happy at cliohnaright with dissolve

"She touched his face, bringing him back to reality. She trailed her fingers along his jawline, then again, over his lips. Her touch sent a shiver down his spine. It brought promise of things to come."

show rowan necklace aroused at midleft with dissolve

cl "… Might prove this whole endeavour worthwhile after all."

"She took her hand away, and he found himself instinctively leaning forward, unwilling to part with the sensuous touch. Realizing his own behaviour, he turned away, ashamed."

show cliohna neutral at cliohnaright with dissolve

cl "Do you fantasize about me Rowan? Out there in the wilds, as you lay under the open sky. Do you hope to find a letter from me when you return to castle Bloodmeen?"
cl "Do you dream of what I’ll do to you next? Dream of tasting my pussy, of being pinned under me, or licking my tits? Of being dominated, body, mind and spirit? "

if Hypnosis2DomEnding == True:
    cl "Dream of what would have happened had you obeyed my orders, let me be your beautiful, smothering caretaker?"

show rowan necklace shock at midleft with dissolve

"He swallowed heavily and opened his mouth to respond, but the sorceress made a swift, zipping motion, and he found that no sound have left his lips."

show rowan necklace concerned at midleft with dissolve
show cliohna happy at cliohnaright with dissolve

cl "I know this part. This is where you mount some token resistance to convince yourself that you can’t, or shouldn’t, indulge in such desires?"

show cliohna neutral at cliohnaright with dissolve

cl "I think it’s time we move past such games Rowan. So for the moment, just listen to what I have to say."

#cg1

"She snapped her fingers, and a tiny, pink fire burst forth from between them. Burning slowly, it jumped between the tips of her fingers, splitting as it went, until her entire hand was enveloped in a soft, calming aura.  "

show rowan necklace neutral at midleft with dissolve

cl "It is time for you to be honest with yourself. To make matters easier, I will be honest first."
cl "Your tenacity. Your resourcefulness. And even that rebellious streak of yours. I have come to respect them. Admire them, even."

"The slow dancing glow drew his eyes in and pushed the world around them far away, limiting his reality to just him and Cliohna, her honeyed words entrancing him no less than the fire did."

cl "I wish to make them my own. I wish to make use of you, Rowan. Of {b}all{/b} of you."

show rowan necklace aroused at midleft with dissolve

"He felt the power behind the flame, he expected it’s magic to come crashing at any moment now. Yet this time, the hypnotics presence did not go beyond a subtle, relaxing throb."

cl "And I know the prospect both scares and excites you, Rowan. So listen closely... Whatever fears you have: {b}Cast them away{/b}. "

"She spread her fingers, move them to the side. He gasped, suddenly feeling himself able to speak again."

cl "I could’ve forced myself into your head earlier, used my powers for ill. I did not. I could’ve continued our sessions under false pretense, make you crave my hypnotics commands. I did not."
cl "Let this be proof of my good intent. I have no desire to take you against your will. You have your boundaries, and I respect that. I would see you remove them for me, rather than tear them down. "
cl "I would rather make you see I am the only mistress worthy of you. "
cl "So don’t fight it. Don’t fight your desires anymore."
cl "Put your trust in me, and I’ll reward you beyond your wildest dreams."

$ cliohnaBlackmailAvailable = True
$ cliohnaRefuseAvailable = True
$ cliohnaHurtAlexiaAvailable = True
$ cliohnaBloodmeenAvailable = True

label cliohnaFinalSubMenu:

menu:
    "Agree.":
        $ released_fix_rollback()
        jump cliohnaFinalSub
        
    "She blackmailed you into this in the beginning." if cliohnaBlackmailAvailable:
        $ released_fix_rollback()
        $ cliohnaBlackmailAvailable = False
        show rowan necklace concerned at midleft with dissolve
        ro "… You were not so understanding all these weeks ago. Remember?"
        "For the first time ever, he saw her hesitate, a feeling of guilt making itself apparent on her expression for a split of a second."
        cl "There is time for blunt force, and there is time for thoughtful deliberation."
        cl "You have every right to be upset, and I apologize for the heavy-handed approach. I was eager to see results and sought the path of least resistance."
        cl "But seeing as it brought us here, I stand by my decision."
        jump cliohnaFinalSubMenu
        
    "What if you refuse?" if cliohnaRefuseAvailable:
        $ released_fix_rollback()
        $ cliohnaRefuseAvailable = False
        show rowan necklace neutral at midleft with dissolve
        ro "Cliohna, I…  I’ve seen what you do to people who disobey you. Back in the abbey. You don’t take being disappointed well."
        "The flame diminished, and its presence lessened, if only for a moment. The sorceress waited a moment with the answer, before responding in a solemn tone."
        cl "You will face no repercussions, be it personal or work-related, should you refuse."
        jump cliohnaFinalSubMenu
        
    "You don’t want to hurt Alexia." if cliohnaHurtAlexiaAvailable:
        $ released_fix_rollback()
        $ cliohnaHurtAlexiaAvailable = False
        show rowan necklace concerned at midleft with dissolve
        ro "Cliohna… What you’re suggesting sounds pretty serious."
        cl "I rarely do frivolous things, Rowan. I have given this a great deal of deliberation."
        ro "But me and Alexia…"
        cl "Have failed. Surely you see it too? Marriage is supposed to be between the two people who complete one another."
        cl "And there are is yearning in you Alexia will never understand. And even she did, she would never be able to sate it."
        ro "It’s not that simple."
        cl "I know it is not easy to abandon something you’ve put so much heart into. But once a project has run its course, it must be reviewed, then - terminated."
        if all_actors["alexia"].relation > 50:
            show rowan necklace angry at midleft with dissolve
            #cliohna shocked
            ro "You presume a great deal about me and Alexia, Cliohna."
            "The sorceress lifted a single eyebrow, surprised by the sudden sharpness in his voice.  "
            show rowan necklace neutral at midleft with dissolve
            #cliohna neutral
            cl "… I see. If that is the case… Then feel free to resolve the matter in whatever way you deem fit."
            cl "Whatever relationships you have with others, whatever arrangements you make with your wife, they all matter little to me. All I care for is the bond between us, and no other. "
            jump cliohnaFinalSubMenu
        else:
            "The naked flame swayed slowly, bringing forth images of Alexia herself dancing in the grey dusk of Arthdale lazy nights. It felt like such a distant memory…"
            #cliohna sad
            "… Though perhaps, given the circumstances, I oversimplify things."
            show rowan necklace neutral at midleft with dissolve
            #cliohna neutral
            cl "Regardless, even though my proposal is indeed serious, know I will not interfere in your relationship with Alexia, or any other woman, as a matter of fact."
            cl "Resolve it as you see fit. All I care for is the bond between us, the rest is of no importance."
            jump cliohnaFinalSubMenu
            
    "Your allegiance isn’t really to Castle Bloodmeen. You can’t be serving her." if cliohnaBloodmeenAvailable:
        $ released_fix_rollback()
        $ cliohnaBloodmeenAvailable = False
        show rowan necklace neutral at midleft with dissolve
        ro "You know me and the twins aren’t the best of allies."
        cl "You were coerced into servitude after months of torture. Your actual performance as the twin’s servant notwithstanding, we all suspect you might hide some sort of an agenda."
        cl "You need not fear Rowan. My own alliance with the twins is purely out of convenience. As long as your plans do not impede my own, there is no reason for us to be at odds."
        ro "...And if they do?"
        "The flame flickered. They waited in silence, the question hanging like an executioner's axe."
        cl "We will cross that bridge when we get to it."
        jump cliohnaFinalSubMenu
        
    "You don’t want this.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        "The pink spiral beckoned. It offered safety. Comfort. Forbidden pleasure beyond his wildest dreams." 
        "And beyond it - a price unspoken."
        ro "Cliohna, I… I can’t. This isn’t who I am."
        #switch out of CG if it’s ever added. Rowan center left, cliohna center right. 
        show cliohna angry at cliohnaright with dissolve
        "Forcing his body, he lifted himself up. The sorceress closed her hand, the magical flame dispersing. Her beautiful lips formed a thin line, and no doubt held back questions and cutting remarks alike."
        ro "It has been fun, I admit that. And I am happy to have been of service. But that’s it."
        ro "It’s nothing personal- "
        #cliohna sad
        cl "I know. You value your independence. Or what little remains of it, given the circumstances."
        "Her fingers drummed the desk she sat on, a low rumble that reminded Rowan of a distant storm. "
        show cliohna neutral at cliohnaright with dissolve
        cl "… How vexing. But not entirely unexpected."
        cl " I had hoped your behaviour in private was more reflective of your true nature than the mask you put on when you sit on the twins’ throne, as the latter is clearly a far cry from who you truly are."
        cl "But it appears neither is entirely true. You are a very complex individual, Rowan Blackwell."
        show rowan necklace happy at midleft with dissolve
        #cliohna shocked
        ro "I rather think of myself as “horribly mundane.”"
        show cliohna happy at cliohnaright with dissolve
        "A thin smile broke through, and she caressed his face one last time, before pushing herself off the table and returning to her chair."
        cl "I will think of our time together fondly Rowan. And I hope we will continue to cooperate on other projects along the way. "
        show rowan necklace neutral at midleft with dissolve
        show cliohna neutral at cliohnaright with dissolve
        cl "Now, I did promise a boon for your support, regardless of the final outcome. What do you wish to ask for?"
        $ cliohnaBoon = 0
        label boonCount:
        if cliohnaBoon == 2:
            jump postBoon
        elif cliohnaBoon == 1:
            cl "Anything else?"
            jump boonMenu
        else:
            jump boonMenu
            
    "You want to, but it is just too dangerous.":
        $ released_fix_rollback()
        "The pink spiral beaconed. He knew what laid beyond - pleasure beyond his wildest imagination. But it came with a chain attached, one Cliohna would hold the end of." 
        "And his mental resistance notwithstanding… He knew once he’d let Cliohna take the lead, he would never be able to quit her."
        show rowan necklace concerned at midleft with dissolve
        ro "I’m sorry Cliohna, I… Can’t."
        cl "And why is that?"
        "He shifted uncomfortably in his chair, doing his best to avoid the enticing spiral. Cliohna moved her hand, and it entered his vision once more. He turned away, as quickly as he could."
        ro "It’s… Complicated."
        show cliohna angry at cliohnaright with dissolve
        cl "To the contrary Rowan, it’s very simple. Say you want to be mine. Say you love how I toy with your mind and body, and that you wish for us to continue."
        "She spoke in a seductive purr, but he heard the edge in her voice, the rising impatience. It almost made him blurt out he agrees, out of fear of displeasing her."
        ro "It’s not that I didn’t enjoy it, but…"
        show cliohna neutral at cliohnaright with dissolve
        cl "… But you won’t agree."
        show bg12 with pinkflash
        show cliohna angry at cliohnaright with dissolve
        show rowan necklace shock at midleft with dissolve
        cl "{b}*Explain to me why.* {/b}"
        "The magic washed over him. The words left his mouth before he could stop himself, the depths of both his fear and desire made apparent with but a few pointed sentences."
        show rowan necklace concerned at midleft with dissolve
        show cliohna neutral at cliohnaright with dissolve
        "A long silence followed. The spiral still hovered in the air, rotating lazily."
        cl "Ah."
        cl "So you {b}do{/b} want me after all."
        show rowan necklace shock at midleft with dissolve
        ro "Yes, but- Nngh?!"
        show rowan necklace aroused at midleft with dissolve
        show bg12 with pinkflash
        "A heavy fog invaded his thoughts, his limbs growing heavy, as if encased in lead. The world around him grew black, reduced to just {b}*Cliohna*{/b} and the pink flame."
        cl "{b}But nothing{/b}. You want {b}*me*{/b}."
        cl "You know all too well the limitations of mind control. Long term adjustments can be made, but only if the subject is at some capacity willing to embrace them."
        "He opened his mouth to scream, but all that left his lips was a tired groan. He felt himself… Deflate. The raising feeling of panic disappeared without trace, leaving him strangely empty."
        cl "All I need is to remove this fear. Remove your doubt. Remove the memories of us ever holding this conversation, and send you back to your room as if nothing ever happened."
        cl "Small adjustments, nothing that would impact you as a whole. But they would be enough to make you crawl back to {b}*me*{/b} before the sun sets again."
        show cliohna happy at cliohnaright with dissolve
        cl "I could make you mine Rowan. Just like you want."
        "She almost hissed the last few words. The pink flame consumed his view, but he could her eyes shine beyond it. The air crackled with magic, not all of it comfortingly warm."
        "He felt the low rumble rather than heard it. The gathering storm that would sweep his resistance away. He sighed and opened himself to it."
        cl "But you said no. So that will be the end of it."
        show rowan necklace shock at midleft with dissolve
        show cliohna neutral at cliohnaright with dissolve
        "The rumble stopped. The flame fizzled out, and the oppressive aura dissipated without a trace. The library returned, as did the strength in his limbs." 
        "He blinked, and gawked at the librarian. Cliohna simply sat on her desk, her deep eyes hiding something he couldn’t discern."
        cl "Well? What are you sitting here for? The matter has been decided. Our business for today is concluded."
        cl "The surrounding silence was deafening. Even though he was but arms length away, the distance between them couldn’t be greater."
        show rowan necklace concerned at midleft with dissolve
        ro "Y-yeah… "
        show rowan necklace concerned at edgeleft with moveoutleft
        "He lifted himself up. He couldn’t force himself to face the sorceress, so he turned around as quickly as he could, and headed for the exit on wooden feet."
        cl "Ah, one more thing."
        show cliohna neutral at midleft with moveinleft
        show rowan necklace shock at edgeleft with dissolve
        "He froze as he felt her lips briefly graze the back of his neck, her soft breasts pressed against him. She whispered in his ear as her hands closed over his shoulders."
        cl "This kiss is a promise, Rowan Blackwell."
        show rowan necklace concerned at edgeleft with dissolve
        cl "When Prothea lies in ruins, our enemies crushed, and my brethren free again, when the twins wear a crown of gold or a crown of thorns, whatever fate you hold in store for them-"
        cl "When the war is over, the realm stable, and my ultimate project complete- "
        cl "You will be out of excuses, and I will find you, and I will lock your cock in a golden cage, and will keep you in it for one year for every week you have made we wait."
        cl "You will eat my pussy every morning, worship my breasts every afternoon, and lick my feet every evening. You will be my toy, my servant, my most prized possession."
        cl "And you will love every minute of it."
        show cliohna neutral at center with moveoutright
        "He felt her withdrawn, her touch leaving a burning imprint on his back. She continued in a bored tone, as if nothing has happened."
        if (all_actors['andras'].total_favors + all_actors['jezera'].total_favors) > 5:
            cl "I will provide your orcs with additional magical equipment, and allocate more time for the Bloodmeen research now  that our project has ended."
            cl "Utilize it to attain a swift victory. You do not wish to prolong your punishment. "
            $ change_research_bonus(3)
            #Increase the basic fighting value of a single orc a little - TODO (more orcs for now)
            $ castle.buildings['barracks'].troops += 5
        else:
            cl "If you survive to this point. The twins are not as considerate as I am, you must be wary not to antagonize them."
            cl "I’ll provide Jezera with the information on Sea Naga’s she’s been pestering me about, and Andras with the schematics for the Qerazal needle trap he asked of."
            cl "I’ll tell them it was who you convinced me to help. Make good use of their following goodwill."
            $ change_favor('jezera', 3)
            $ change_favor('andras', 3)
        cl "You are free to go now, Rowan Blackwell. Do not be a stranger."
        ro "Y-yes… Of course."
        "He trudged on, unable to look back. By the morrow, they’ll return to the roles they held in castle Bloodmeen. But he didn’t think he’ll ever forget her words."
        "Or that she ever will."
        $ cliohnaDominationPromise = True
        return

label boonMenu:

menu:
    "More research." if researchNotPicked:
        $ released_fix_rollback()
        $ researchNotPicked = False
        cl "Given how I had taken your own personal time to indulge in side research, I suppose it’s only fair I return the favour."
        cl "Consider it done."
        $ change_research_bonus(3)
        $ cliohnaBoon += 1
        jump boonCount
        
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
        jump boonCount
        
    "Favour with Andras." if AndrasFavourNotPicked:
        $ released_fix_rollback()
        $ AndrasFavourNotPicked = False
        cl "He did wish to have detailed information on Qerazel needle traps… I suppose I can provide it to him, explain it was your insight that helped create an operational prototype."
        ro "Should I know what that is, in case he asks about them?"
        cl "There is no need. I will simply relay the information to him soon after you depart from Castle Bloodmeen. By the time you return, he will have moved to a different project, as he always does."
        $ change_favor('andras', 3)
        $ cliohnaBoon += 1
        jump boonCount
        
    "Magic equipment for the orcs." if EquipmentNotPicked:
        $ released_fix_rollback()
        $ EquipmentNotPicked = False
        show cliohna angry at cliohnaright with dissolve
        cl "You could not have picked a more monotonous task."
        ro "My apologies if it sounds horribly mundane to you."
        show rowan necklace happy at midleft with dissolve
        show cliohna happy at cliohnaright with dissolve
        cl "You will not live that down, will you?"
        show rowan necklace neutral at midleft with dissolve
        show cliohna neutral at cliohnaright with dissolve
        cl "I will place some basic enhancement on their equipment, though the psychological impact of doing so is likely to exceed the actual increase in power."
        ro "As long as they fight harder, that’s all I care for. "
        #Increase the basic fighting value of a single orc a little - TODO (more orcs for now)
        $ castle.buildings['barracks'].troops += 5
        $ cliohnaBoon += 1
        jump boonCount
        
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
        jump boonCount
        
label postBoon:

cl "I believe that to be suitable compensation for your efforts."
cl "Do take care Rowan."

"She offered him a small smile. For a moment, he wondered if it wasn’t too late to change his mind- "

scene black with fade

"But she turned around, and he felt the window close."

$ cliohnaRomance = False

return

label cliohnaFinalSub:

show rowan necklace aroused at midleft with dissolve

"The flame danced and danced, and he had seen his future in it. Cliohna twirled her fingers, and the pink trail formed a collar, just for a moment."

cl "Your desire is clear. But pride prevents you from giving it form. The world must always see the Hero of Karst, the castellan of Castle Bloodmeen, a general and warrior."

show cliohna happy at cliohnaright with dissolve

cl "So do not worry. I will require no public displays of your submission. The collar you will wear will be in your thoughts, not on your skin. Nobody besides us needs to know your true nature."

show rowan necklace concerned at midleft with dissolve

"He swallowed heavily. It was wrong, so wrong. What if it was all a long con just lower his guard, gain his trust so he would agree? Everything was possible in castle Bloodmeen. Could he really trust her…?"

show cliohna neutral at cliohnaright with dissolve

ro "… You promise?"

"She tilted her head, waiting for him to continue. His fist tightened, he felt his fingernails break skin. It was foolish, he knew that. She would use this against him, use it to destroy him completely." 
"But just once, he wanted to believe that something good could happen in this Gods' damned castle."

show rowan necklace neutral at midleft with dissolve

ro "Promise me this is not just some ploy to ensure I support you in your endeavours."

show rowan necklace shock at midleft with dissolve
show cliohna happy at cliohnaright with dissolve

"She chuckled unexpectedly, the cheerful laugh breaking the heavy silence of the library."

if (all_actors['andras'].total_favors + all_actors['jezera'].total_favors) > 5:
    cl "And was your continued, temporary submission a mere ploy to get into my good graces, ensure I am adequately committed to your war?"
    
else:
    cl "And was your continued, temporary submission a mere ploy to get into my good graces, ensure I am sufficiently placated to turn a blind eye to your little power struggles with the twins?"
    
ro "I- what?"

cl "You are not the only one who feels out of place here, Rowan. I spent many evenings trying to decipher the true intent behind your words and actions. But now I know what’s in your thoughts. And it’s {b}me{/b}."

"Again she twirled her fingers, sending the flames turning, into a small spiral of pink fire. Lethargic power started to seep out of it, robbing Rowan of the strength to look away. "

show rowan necklace neutral at midleft with dissolve

cl "So put your worries to rest, Rowan. I promise the offer is sincere."

"His body felt heavy, but his mind remained clear. He could no longer think of any reasons to deny her - and his heart made its choice a long time ago."

ro "What do you want me to say?"

show cliohna neutral at cliohnaright with dissolve

cl "Whatever it is you always wanted to say to me. {b}*Speak your mind.*{/b}"

show rowan necklace aroused at midleft with dissolve

"This time, the magic did not come barging in, forcing its way inside. Like an old friend, it knocked on the doors of his mind. A door that was no longer locked - but protocol demanded he invite him in, welcome to his house, and share everything he held inside."
"Like a calming mist, the hypnosis washed away everything Cliohna had no need for. Worries about the twins, Alexia, problems great and small. It reduced the world to just himself and the sorceress."
"Their own pocket paradise. If only for a moment."

show cliohna happy at cliohnaright with dissolve

ro "… Thank you, Cliohna. For everything."

"A warm glow enveloped his body, like a blanket. He closed his eyes and rested his head, for the first time in what felt like forever feeling at ease. Strangely, he could still see the sorceress and her spiral."

cl "You have only yourself to thank Rowan. It was your actions that brought us here. You yourself made that dream reality."

"He felt her touch his forehead, brushing his hair away. More magic whirled around him, seeping into him. He felt like this time, it would not leave, no matter what."

cl "I am glad you’ve chosen me. I know you have served many women in the past. The living saint… Jezera…"

show cliohna neutral at cliohnaright with dissolve

cl "And most importantly, Solansia. You’ve devoted your life to protecting this wicked order she’s created."

"Her hot breath tickled his cheek. He felt her lips brush against the tip of his nose, as her arms closed around him."

cl "But she was never worthy of your devotion, Rowan."
cl "From now on {b}I{/b} will be your Goddess."

"She sealed his fate with a deep kiss, that seemed to go forever. She pressed into him strongly, desiring to dominate him both physically and mentally." 
"He let her. Gods, it felt so natural to have her be on top, it always did, and now accepting that fact came with a soft tingle of pleasure that filled his body from his toes to the tips of his fingers. A small reward, from the divine to a faithful."

show cliohna happy at cliohnaright with dissolve

"Finally, the kiss broke, and he opened his eyes to see her sitting on him, her lips curled into a small smile."

cl "... And you will be {b}my{/b} champion. You will make {b}my{/b} dreams reality."
cl "Now, close your eyes again."

"She moved her hand over his eyes, and lower her voice so she could whisper seductively in his ear."

cl "I want to leave some surprises for our future… “Sessions”."

show rowan necklace happy at midleft with dissolve

ro "As you command… My Goddess."

cl "Oh Rowan, the things we’ll do together..."

"The glow grew in power, drowning his thoughts in soft pleasure. Slowly, his consciousness slipped away, lulled to sleep by the comforting warmth of Cliohna’s embrace."

cl "Ah, but before I forget... One last thing."

scene black with fade
show cliohna happy behind black

cl "The safe word is “paperwork”."

#The Submissive route rewards he player with “Cliohna’s Champion, a story perk that awards +1 diplomacy.” - TODO
$ cliohnasChampion = True
return