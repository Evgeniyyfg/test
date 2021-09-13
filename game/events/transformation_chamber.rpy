init python:
    
    event('transformation_chamber_built', triggers='week_end', conditions=('castle.buildings["nasim_chamber"].lvl > 0',), run_count=1, priority=pr_story)
    event('transformation_chamber_reminder', triggers='week_end', conditions=('week == 38', 'castle.buildings["nasim_chamber"].lvl > 1',), run_count=1, priority=pr_story)
    event('transformation_chamber_late', triggers='week_end', conditions=('week == 62', 'castle.buildings["nasim_chamber"].lvl > 1',), run_count=1, priority=pr_story)
    
    
label transformation_chamber_built:

scene black with fade

"Squeezing himself past Skordred workers, Rowan made his way down through the barely uncovered corridors that ran beneath Castle Bloodmeen."

show rowan necklace neutral at center with moveinleft

"As the dwarf told him, it would take weeks to stabilize the underground passages, and then months to fully clear out all the collapsed tunnels. But these were long term plans, which weren’t as important at the moment." 
"Because this morning, a direct passage to the Transformation Chamber was uncovered."

show rowan necklace angry at center with dissolve

"Rowan wrinkled his nose and covered his face. He felt the chamber long before he saw it. Some sort of sweet, putrid smell assaulted him, one he couldn’t quite define. But if felt vile." 
"Perhaps some things ought to be sealed forever."

show rowan necklace neutral at edgeright with moveoutright

"But it was too late for regret. He shielded his eyes as he noticed a sickening, pinkish sheen ahead of him, then headed down."

scene bg59 with pinkflash
show rowan necklace neutral at edgeright with dissolve

"..."
"… He let out a soundless laugh. “Chamber”? The room in front of him was massive, wide open, with a ceiling too high for the torchlight to reach!"
"Built into a natural cavern, he still saw elements of it remain. Not one wall was straight, and he saw hints of stone stalactites, disappearing into the darkness."

show rowan necklace neutral at midleft with moveoutleft

"He took a careful step forward, and stopped halfway. White lines decorated the floor, just visible through a pinkish mist that filled the room, warning people not to cross them recklessly."

ro "Had any accidents?"

show nasim neutral at midright with dissolve

nas "None so far, but one would be foolish to explore a nexus of magic such as this and not take adequate precautions."

show nasim happy at midright with dissolve

nas "Out of fear for causing irreparable damage to any knowledge residing inside, and out of fear for possible traps. In that order."

show nasim neutral at midright with dissolve

"The wizard dusted his hands, getting rid of the remaining chalk. Besides him, there was only one more person in the room."

show rowan necklace shock at edgeleft with moveoutleft
show nasim neutral at center with moveoutleft
show cliohna neutral at cliohnaright with dissolve

cl "And as the former is unlikely, for once it would be better to simply throw orcs at the problem."

show rowan necklace neutral at edgeleft with dissolve

nas "I’m not sure if either Master Andras and Lord Blackwell would approve of such liberal use of their resources."

"Nasim looked to him for confirmation. Rowan rolled his eyes, and simply addressed the librarian. "

ro "That’s a rather harsh assessment. Is something wrong with the chamber?"

show cliohna angry at cliohnaright with dissolve

cl "There’s nothing “wrong” with the chamber. But as you can see… "

"He saw her looking at the many half-destroyed murals that decorated the chamber walls. Most, Rowan noticed, depicting demons of the most bizarre forms and proportions. Creatures that ought not to exist.  "

show rowan necklace concerned at edgeleft with dissolve

"He recognized one, from many years ago. He wished he hadn’t."

show rowan necklace neutral at edgeleft with dissolve

cl "This chamber is more of a temple than a place of arcane research. I suspected that might be the case, given the library's lackluster records regarding it. "

show cliohna neutral at cliohnaright with dissolve

cl "There was a chance that some materials were simply held on-site. As it is now plain to see, that is not the case. Instead, we have… This. "

show cliohna angry at cliohnaright with dissolve

"With visible distaste, she pointed to a slightly faded depiction of a massive, four-legged beast, with a cock as big as itself. It was ejaculating a stream of cum, beheading some random knight through sheer pressure." 

show cliohna neutral at cliohnaright with dissolve

"Besides her, Nasim coughed."

nas "While the lack of additional research material is disappointing, it’s not exactly unexpected, nor is it a major setback for us. "
nas "The chamber’s strength has always laid in its versatility. It’s true the Dark Lords used it as a place of communion between themselves and Kharos, so calling it a temple isn’t that far off."

show nasim happy at center with dissolve

nas "But there is no reason for us to follow in their footsteps. We are not limited by doctrine. We can utilize its ability to focus chaos magic in ways Kharos servants never dreamed of!"

"Nasim’s bright smile could bring Cla-Min to shame. But Cliohna did not share it."

show nasim neutral at center with dissolve

ro "You disagree."

cl "All chaos magic is Kharos magic. I have no interest in singing praises to a mindless god of destruction, even if it is just lip service."
cl "But the theory is sound, and all of the library staff is free to pursue their own research - as long as they don’t neglect their duties to the twins."

nas "I am ever at your and the Masters’ disposal, Mistress Cliohna. "

cl "It goes without saying, Nasim."

hide cliohna with moveoutleft
show rowan necklace neutral at midleft with moveinleft
show nasim neutral at midright with moveoutright

"The sorceress waved his remarks off, and headed to the exit, leaving the two men alone."

show rowan necklace concerned at midleft with dissolve

"Rowan took a look at the chamber again. A shattered statue loomed in the distance, its broken elements casting ominous shadows."

show rowan necklace neutral at midleft with dissolve
show nasim happy at midright with dissolve

ro "… Kharos Magic? You aren’t a priest Nasim. Or at least you never struck me as one."

nas "What gave me away? The lack of maniacal grin? The ability to form coherent, evidence-based theories?   "

ro "Your incredible humility."

nas "Ha! Most fair, Lord Backwell. But I will remark, if one’s knowledge and ability are both clear and known, then pretending humility is worse than arrogance. One must always take pride in their capabilities."
nas "But back to the topic at hand. No, I am no priest, and I never considered pursuing a career in that area, even though I would likely excel in it."
nas "It is well documented that inherent magical aptitude and extensive knowledge of magical theory allow for greater use of Solansia’s divine power. As you know, it’s one of the main reasons Rosaria recruits their lay priests from among the magically gifted."

show rowan necklace shock at midleft with dissolve

nas "As it happens, the same principle applies to Kharos’ Chaos magic. And unlike Solansia, Kharos cares neither for servitude, nor the exact way his gifts are employed."
nas "A… “Will to power”, so to speak, is enough to summon forth a considerable amount of his energy."

show rowan necklace neutral at midleft with dissolve

ro "How much are we talking here?"

nas "Enough."

"Rowan shot him an aside glance. Nasim only smiled."

menu:
    "A bold strategy. And maybe that’s what they needed.":
        $ released_fix_rollback()
        $ nasimAttitude += 1
        show nasim neutral at midright with dissolve
        ro "The way you phrase it… You almost make it sound like Kharos would approve of us turning his powers against him."
        show nasim happy at midright with dissolve
        nas "Not against him, precisely, but against his followers? I imagine so!"
        show nasim neutral at midright with dissolve
        nas "While Cliohna’s expertise in magic and knowledge of the arcane are both unparalleled, her outlook on matters of theology is somewhat... Simplistic."
        nas "One should not think of Kharos as a mere god of destruction. He is, foremost, a God of change and competition."
        show nasim happy at midright with dissolve
        nas "To best his followers with the very magic they use… Would it not be “Might makes right” in its purest form?"
        show rowan necklace happy at midleft with dissolve
        if serveChoice != 4:
            "A dry laugh escaped Rowan’s lips. To turn Kharos magic against the children of his very own Demon Lord… He could almost taste the irony."
        else:
            "A dry laugh escaped Rowan’s lips. What a wicked ideology… And to think they might find themselves working with some of Kharos followers soon."
        ro "Keep up the good work then. How long till the chamber is operational?"
        show nasim neutral at midright with dissolve
        nas "At least some months. I do not cut corners, Rowan, not when dealing with forces as dangerous as these."
        
    "Idiotic. People tried to bargain with Kharos before. It never ends well.":
        $ released_fix_rollback()
        $ nasimAttitude -= 1
        show nasim neutral at midright with dissolve
        show rowan necklace angry at midleft with dissolve
        ro "And so you add your name to the ever expanding list of people thinking they can toy with Kharos powers without consequences. Right after General Zerias."
        show rowan necklace happy at midleft with dissolve
        ro "Need I remind you of the full story, or will you be satisfied with the highlights?"
        show rowan necklace angry at midleft with dissolve
        nas "I know the gist of it. Worry not, Lord Blackwell. Unlike Zerias, I am well aware of the limitations of my abilities."
        nas "… And from what I understand, the list now ends with “Rowan Blackwell.”"
        ro "I do not- "
        if castle.buildings['sanctum'].lvl >= 1 and castle.buildings['pit'].lvl >= 1 and castle.buildings['forge'].lvl >= 1:
            nas "You manage a castle filled to the brim with orcs, cubi and driders, and your armies are equipped by a minotaur and looked after by a drow."
        elif castle.buildings['sanctum'].lvl >= 1 and castle.buildings['pit'].lvl < 1 and castle.buildings['forge'].lvl >= 1:
            nas "You manage a castle filled to the brim with orcs and cubi, and your armies are equipped by a minotaur."
        elif castle.buildings['sanctum'].lvl >= 1 and castle.buildings['pit'].lvl < 1 and castle.buildings['forge'].lvl < 1:
            nas "You manage a castle filled to the brim with orcs and cubi, and I can only imagine what fantastic creatures Andras and Jezera will have you add to the repertoire before long."
        else:
            nas "You manage a castle filled to the brim with orcs, and trained by a half-demon with a questionable grasp on non-lethal discipline regiments."
        if week > 60:
            nas "By your machinations, hundreds of knights and men-at-arms now lay dead at Astarte fields."
        elif week > 20:
            nas "By your machinations, Raeve has fallen, exposing the heartland of Rosaria to orcs, demons, and likely - common bandits."
        else:
            nas "Every day, you work tirelessly to loosen Solansia’s hold over your very homeland, and expose it to orcs and demons alike."
        show nasim happy at midright with dissolve
        nas "For someone *not* serving Kharos, you’re doing an exceptional job at undermining his main adversary."
        "If looks could kill, Cliohna would be looking for a new assistant right now. As always, the wizard took it in stride, meeting his glare without as much as a blink."
        if serveChoice == 1 or serveChoice == 3:
            "He couldn’t tell him it was all a rouse, a long con. He had to keep up appearances, as much as it sickened him."
        elif serveChoice == 2:
            "So much wrong, done because he let himself falter in the dungeons. But he could never admit it. Not to himself, not to Nasim."
        else:
            pass
        show nasim neutral at midright with dissolve
        ro "Do not equate me with Zerias nor yourself. I am not doing this out of ambition or on a whim. I am making a better world for us all, Nasim."
        if avatar.guilt > 30:
            "The wizard arched an eyebrow at him. Even to Rowan, the words sounded hollow."
        else:
            "The wizard arched an eyebrow at him. Rowan’s voice didn’t waver, but it didn’t make his words any more convincing."
        nas "Your reasons are your own, Lord Blackwell, as are mine. But if what you do is for the good of us all, then there is no reason for us to be at odds with one another."
        nas "As for the chamber itself, and the dangers associated with it… "
        show rowan necklace neutral at midleft with dissolve
        nas "I know. I assure you, Rowan, I will take the utmost precautions whilst handling it. It will take months before I will even start planning a test ritual."
        ro "I hope that’s enough."
        nas "It will be."
        
show nasim neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve

nas "I will keep you updated, Lord Blackwell." 

ro "Do so."

show rowan necklace neutral at edgeleft with moveoutleft
hide nasim with moveoutright

"He headed for the exit, leaving Nasim to his work. Right before leaving, he stopped, and shot one last glance at the poorly lit chamber. Temple to Kharos…"

scene black with fade

"He only hoped it wasn’t a mistake to dig it out."

return

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label transformation_chamber_reminder:

scene bg6 with fade
show rowan necklace neutral at midright with dissolve
show nasim neutral at midleft with dissolve

nas "Lord Blackwell."

ro "Nasim. To what do I owe the pleasure?"

#nasim concerned
nas "I wanted to ask, has any progress been made on excavating the transformation chamber, per my earlier request?"

show rowan necklace angry at midright with dissolve

ro "Given your tone, I take it you know the answer already. "

nas "It’s been half a year Rowan, give or take. I understand your position often forces you to make compromises, sometimes on several fronts, but I find it difficult to believe you haven’t had the opportunity to adjust the excavation plans to reach it."

menu:
    "It slipped your mind. ":
        $ released_fix_rollback()
        show rowan necklace concerned at midright with dissolve
        ro "Will you believe me if I say I simply forgot about it?"
        "He recognized the look in Nasim’s eyes. The barely restrained desire to strangle your commanding officer for his incredible idiocy. He himself used to hold it quite often."
        #nasim neutral
        show rowan necklace happy at midright with dissolve
        nas "… I will, if you, ever so kindly, make the necessary adjustments."
        nas "I believe Skordred has made considerable progress on cleaning out the lower levels since we last discussed the topic. Uncovering the chamber shouldn’t be that difficult now."
        ro "That’s good to know."
        show rowan necklace neutral at midright with dissolve
        nas "So please, Lord Blackwell, see that the matter is resolved. My research has stalled, and despite whatever differences there might be between us, I believe our interests align."
        nas "I need that chamber as soon as possible, if I am to ever be of use to you."
        "He tried to paint it as mutual interest, but Rowan knew Nasim’s courtesy extended only so far. If he wanted to stay on his good side, he would have to get him that damned chamber."
        return
        
    "It hasn’t been a priority.":
        $ released_fix_rollback()
        ro "Nasim, I have a world to conquer, and enough men and swords to maybe raid a pantry. Your chamber of poorly documented capabilities simply wasn’t a priority."
        nas "If that’s the excuse you’re going for, then I will remark that given the scarcity of options, you of all people should understand the need for unorthodox solutions."
        ro "That just so happen to align with your research."
        #nas neutral
        nas "If you expect selfless commitment to the cause, then you will soon find yourself short on allies, Lord Blackwell."
        nas "I believe Skordred has made considerable progress on cleaning out the lower levels since we last discussed the topic. Uncovering the chamber shouldn’t be that difficult now."
        show rowan necklace neutral at midright with dissolve
        show nasim angry at midleft with dissolve
        ro "I will be the judge of that. "
        show nasim neutral at midleft with dissolve
        nas "… Of course. And I hope, for the sake of our future cooperation, that you will see I am not asking for much."
        hide nasim with moveoutleft
        show rowan necklace concerned at midright with dissolve
        "The mage lowered his head slightly and departed the room. Rowan rubbed his face, exhausted. If he wanted to stay on Nasim’s good side, he would have to get him that damned chamber."
        $ nasimAttitude -= 1
        return
        
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label transformation_chamber_late:
    
scene black with fade

"Rowan made his way through the castle lower levels, offering a casual nod to the occasional worker. Normally, he wouldn’t bother with these old halls, as they held little to none of the castle’s vital infrastructure." 
"But they were being continuously cleared out, to prepare for Bloodmeen’s inevitable expansion. And today, after a year of hard work, the excavation process finally reached Nasim’s transformation chamber."

show rowan necklace angry at center with moveinleft
 
"As he continued to walk down, he felt it long before he saw it - a sort of sweet, putrid smell hung in the air." 
"He wrinkled his nose and covered his face. He couldn’t quite define it, but it felt vile. Perhaps some things ought to be sealed forever."

show rowan necklace neutral at edgeright with moveoutright

"But there was nothing he could do about it now. He saw a sickening, pinkish sheen ahead of him, and headed for it."

scene bg59 with pinkflash
show rowan necklace neutral at edgeright with dissolve

"..."
"… He let out a soundless laugh. “Chamber”? The room in front of him was massive, wide open, with a ceiling too high for the torchlight to reach!"
"Built into a natural cavern, he still saw elements of it remain. Not one wall was straight, and he saw hints of stone stalactites, disappearing into the darkness."
"He made another step, then looked down. White lines decorated the floor, just visible through a pinkish mist that filled the room, warning people not to cross them recklessly."

show rowan necklace neutral at edgeleft with moveoutleft
show nasim angry at midright with dissolve
show orc soldier neutral at edgeright

nas "Slowly, you oaf! One step at a time!"

"And just past them, a lone orc carefully trekked through the chamber, directed by the purple-clad wizard."

show rowan necklace neutral at midleft with moveinleft

ro "Checking for traps? That’s quite the brute-force approach."

nas "I would not resort to it, had I have the time to apply the proper procedure."

"There was no denying the hostility in Nasim’s voice. It was to be expected, after being snubbed for so long."

hide orc soldier with moveoutright
show cliohna neutral at edgeright with dissolve
show nasim neutral at midright with dissolve

cl "There are exceptions to every rule. Time is limited, and orcs are bred by the dozens."

"Rowan saw the library mistress studying the many half-destroyed murals that decorated the chamber walls. Most, Rowan noticed, depicting demons of the most bizarre forms and proportions. Creatures that ought not to exist."  

show rowan necklace concerned at midleft with dissolve

"He recognized one, from many years ago. Another reason why the chamber should’ve stayed buried."

show rowan necklace neutral at midleft with dissolve

ro "What’s your take on the place, Cliohna?"

cl "This chamber is more of a temple than a place of arcane research. I suspected that might be the case, given the library's lackluster records regarding it."
cl "There was a chance that some materials were simply held on-site. As it is now plain to see, that is not the case. Instead, we have… This. "

show cliohna angry at edgeright with dissolve

"With visible distaste, she pointed to a slightly faded depiction of a massive, four-legged beast, with a cock as big as itself. It was ejaculating a stream of cum, beheading some random knight through sheer pressure. "

show cliohna neutral at edgeright with dissolve

nas "Should Master Andras express the desire to decapitate his enemies with his cock alone, we are obliged to provide him with the means to do so."

cl "The compromises we must make in the name of progress…"

show cliohna angry at edgeright with dissolve

cl "Not that resorting to Kharos worship should ever constitute as “progress”."

show cliohna neutral at edgeright with dissolve

cl "But I have spoken about the topic at length already. I understand you’re on a tight schedule Nasim. As per our agreement with Jezera, you are free to commit fully to the chamber’s restoration." 

show nasim happy at midright with dissolve

nas "Thank you, Mistress Cliohna. I appreciate the understanding."

show nasim neutral at midright with dissolve

cl "Spare me. Just make sure the twins are satisfied. "

hide cliohna with moveoutleft

"The sorceress headed to the exit, leaving Rowan alone with Nasim, and the unfortunate orc, who took the opportunity to take a short break from his borderline suicidal assignment." 
"Rowan ignored the latter, and took another look at the chamber. A shattered statue loomed in the distance, its broken elements casting ominous shadows. Cliohna called it a temple, and it certainly looked the part." 

ro "I didn’t take you for a priest, Nasim."

nas "I am not."

ro "Then do you want to explain what was this all about? Especially that part about worshipping Kharos?"

show nasim angry at midright with dissolve

nas "Do not feign interest. We both know it’s not genuine."

menu:
    "Apologize.":
        $ released_fix_rollback()
        show rowan necklace concerned at midleft with dissolve
        ro "Nasim, I’m sorry, but- "
        nas "{i}Please{/i}, do not waste your breath on apologies. Actions speak louder than words."
        nas "But very well, I’ll explain the principle, if you must know."
        
    "“Suck it up.” ":
        $ released_fix_rollback()
        show rowan necklace angry at midleft with dissolve
        ro "Regardless of my opinion on the chamber, it’s here to stay. I would like to know how it’s supposed to work."
        nas "… Very well."
        
show rowan necklace neutral at midleft with dissolve
show nasim neutral at midright with dissolve

nas "No, I am not a priest. But I don’t need to be. Arcane knowledge and magical aptitude are both invaluable when it comes to channeling divine power. It’s one of the reasons Rosaria recruits their lay priests from among the magically gifted."

show rowan necklace shock at midleft with dissolve

nas "The same principle applies to Kharos’ Chaos magic. But unlike Solansia, Kharos cares neither for servitude, nor the exact way his gifts are employed."

show rowan necklace neutral at midleft with dissolve

nas "Because of that, a…”Will to power”, so to speak, is all that it takes to summon forth a considerable amount of his energy."

ro "But there are limits."

nas "With the chamber {i}finally{/i} within my grasp? Not for long. It’s a nexus of chaos energies."

show nasim happy at midright with dissolve

nas "Servants of Kharos used them as their religion dictated. I am bound by no such limitations."

show nasim neutral at midright with dissolve

nas "Does this satisfy your curiosity, Lord Blackwell? If so, then I must politely ask you to leave. I need this place cleared of traps by supper. And you have a city to take, if I am not mistaken."

ro "No, you are not. I’ll leave you to your work."

"That was as much as he could expect Nasim to tell him. He gave the man a polite nod, and headed for the exit. "

show rowan necklace neutral at edgeleft with moveoutleft
hide nasim with moveoutright

"Just before leaving, he stopped, and shot one last glance at the poorly lit chamber. A temple to Chaos, long forgotten, now uncovered."

scene black with fade

if serveChoice == 4:
    "He better deliver Rastedel to the twins on a silver plate, before they decide their only way forward was to follow in their father’s footsteps." 
    
else:
    "He suppressed a shudder. He better find a way to get Alexia to safety, and do so soon, before the twins’ crusade spirals out of his control."
    
$ nasimAttitude -= 5
return