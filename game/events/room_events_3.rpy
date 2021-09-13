label greyhideBatriHelp:

scene bg22 with fade
show rowan necklace neutral at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve


if ghBatriLater == True:

    gh "Rowan. Have you decided the size of Batri’s 'care package'?"

    ro "Hmmmm."

    jump ghBatriHelpMenu

else:
    pass


"Rowan found Greyhide with a freshly finished waraxe in hand. The minotaur kept staring at his creation, apparently lost in thought."

show rowan necklace concerned at midleft with dissolve

ro "Is something on your mind, Greyhide?"

"With a sigh, the minotaur put the axe away, next to a dozen similarly made weapons."

gh "No."
gh "Yes..."
gh "The usual. Working the forge can be… Tedious."

"The minotaur smiled at him, in this weird way only a creature with a muzzle could."

if alexiaForgeIntro == True:
    gh "But you and Alexia are always a pleasant distraction from the usual drudgery."
    
else:
    gh "But your rare visits are always a pleasant distraction from the usual drudgery."
    
gh "What do you need, Rowan?"

ro " ..."
ro "I need you to make even more weapons."

gh "..."

"The minotaur gave him the thousand yard stare."

show rowan necklace happy at midleft with dissolve

"Rowan smiled apologetically."

gh "Of course. That is why I’m here. "
gh "What exactly do you need?"

show rowan necklace neutral at midleft with dissolve

ro "Not the usual stuff we give to our troops. This time, quality and practically are secondary."
ro "What I need are axes that first and foremost look impressive."
ro "I want every orc who sees them green with jealousy."

gh "As opposed to their usual shade of green?"

show rowan necklace happy at midleft with dissolve

ro "… Yes."

show rowan necklace neutral at midleft with dissolve

ro "I need them awed by them. I need them to think ”This is what I'll be able to get if I join Batri”."
                                                                   
gh "Simple enough. Our forge is more than capable of making equipment like that, and so am I."
gh "You only need to tell me how many do you need."

"Now that was an interesting question."

if batri_power < 4:
    "Batri still needed a lot of support. Even if Rowan ordered Greyhide to work on this full time for several weeks, it won’t be enough to give the orc the boost he needed."
    
elif batri_power > 3 and batri_power < 6:
    "Batri’s support has already grown considerably. Should he order Greyhide to work on this full time for several weeks, they will likely get close to full support by the end of the month."
    
elif batri_power > 5 and batri_power < 8:
    "Batri was almost ready. If Greyhide works on this full time, the weapons will most certainly give him the final push he needed. They can probably settle for a medium delivery."
    
else:
    "Batri was almost ready. Rowan only needed some equipment to give Batri the final push he needed, so a small delivery would be enough."


"For logistic reasons, it was better to make it a onetime deal. Besides, if this became a regular occurrence, Batri could get the wrong message – he could be tempted to delay the raid so he could con Rowan out of more free equipment."
"Well, free for him. For Rowan, this entire project would be a considerable drain on the castle’s iron reserves. But if compared to the raids, it was a much more reliable way of boosting Batri’s powerbase."
"What package should he send him then?"

label ghBatriHelpMenu:

menu:
    "Small package." if castle.iron_per_week > 2:
        $ released_fix_rollback()
        $ castle._iron -= 3
        $ batri_power += 1
        jump ghBatriConclusion

    "Medium package." if castle.iron_per_week > 5:
        $ released_fix_rollback()
        $ castle._iron -= 6
        $ batri_power += 2
        jump ghBatriConclusion
        
    "Large package." if castle.iron_per_week > 8:
        $ released_fix_rollback()
        $ castle._iron -= 9
        $ batri_power += 3
        jump ghBatriConclusion
        
    "Full package." if castle.iron_per_week > 11:
        $ released_fix_rollback()
        $ castle._iron -= 12
        $ batri_power += 4
        jump ghBatriConclusion
        
    "Decide later.":
        $ released_fix_rollback()
        $ ghBatriLater = True
        gh "Alright, once you make up your mind, you know where to find me."
        return

label ghBatriConclusion:

gh "Very well, I’ll see that it’s done."
gh "Give me the camp location, I’ll tell the orcs to bring the package over once it’s ready for delivery."

show rowan necklace happy at midleft with dissolve

ro "How often do I tell you’re a joy to work with Greyhide?"

gh "Not often enough."

$ ghBatriHelp = "got"
$ journal.complete_quest_note('orciad', 'note9')

return


###########################################################################
###########################################################################
###########################################################################

label jezeraDelaneHelp:

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan didn’t exactly like asking the twins for help."

if serveChoice == 4:
    "A foolish sentiment, perhaps. They were in this battle together, and only by supporting one another would victory be assured."
    "It would be nice if the twins finally acknowledged that. They were a nuisance as often as they were of help to him."

else:
    "He was held captive, chained with a cursed amulet and forced to commit countless atrocities in order to protect himself and his wife."
    "Asking his torments for favors felt... Wrong."

"However, he had to acknowledge that when it came to finding gifts for a noblewoman there was but one expert in the whole castle he could rely on."
"And he was now knocking on her doors."

show jezera neutral behind bg14

je "Enter!"

scene bg18 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with moveinright

"For once, she was fully clothed, and she seemed to be in a good mod. Praise the Goddess."

je "Rowan, my hero! What brings you to my chambers? "

show rowan necklace happy at midleft with dissolve

ro "Mistress Jezera. I have a favor to ask of you."

je "Oh? Now that’s new. Do tell."

show rowan necklace neutral at midleft with dissolve

ro "Are you familiar with the orc camp in the northern regions of Rosaria?"

je "The one locked in a duel over some minor noblewoman? Yes, Andras filled me in."

ro " I managed to gain the favor of one of the warchiefs, Ulcro. But he won’t join us unless I provide him with suitable gifts for Delane- the noblewoman, I mean."

show rowan necklace happy at midleft with dissolve

ro "So I was wondering if you have any jewelry you would be willing to part with. Some things you are no longer fond of, perhaps?"

if (all_actors['jezera'].favors + all_actors['andras'].favors) < 3:
    show jezera neutral at midright with dissolve
    je "Oh, Rowan I’m not sure how to tell you this."
    je "I talked with Andras about it earlier, and…"
    je " He believes either Batri or Tarish would make for better leaders. Ulcro is, and I quote here, “A coward and delusional fool.”"
    show rowan necklace angry at midleft with dissolve
    je "I fear my hands are tied. Everything relating to orcs is his responsibility."
    ro "Is that so?"
    show jezera happy at midright with dissolve
    "Jezera sent him an innocent smile. Now he was sure she was messing with him."
    show rowan necklace neutral at midleft with dissolve
    "But there was no way he could pressure her into helping. He hadn't been playing nice with them either."
    ro "… I’ll reconsider my position then. I apologize for taking your time, Mistress."
    je "Oh no, I apologize for not being of any use. After taking the time to visit me..."
    je "You know... Maybe I could dig something up. But I wouldn't want to encroach on my brother's territory."
    show rowan necklace angry at midleft with dissolve
    je "But If I were to tell him you literally begged me for help, I am sure he would be more understanding of my actions."

    menu:
        "Beg for help.":
            $ released_fix_rollback()
            show rowan necklace neutral at midleft with dissolve
            ro "..."
            je "So? What will it be?"
            je "Will you crawl at my feet, just to get a couple of old trinkets, or will you leave empty-handed?"
            "In a true display of heroic willpower, Rowan stopped himself from visibly scowling."
            "Compared to Batri and Tarish, Ulcro was the lesser evil. If he had to humiliate himself to ensure his support..."
            "Then so be it."
            hide rowan
            show rowan necklace neutral behind bg18
            show jezera happy at center with moveinright
            "With some hesitation, Rowan knelt before Jezera. The half-demoness grinned from ear to ear, basking in his submission."
            ro "Please... Mistress Jezera..."
            ro "I really need those gifts..."
            "Gritting his teeth, he pressed his forehead to the cold floor."
            "... Something tapped his head gently."
            "He raised his head slightly. Jezera's black boot was right before his eyes."
            je "Kiss it."
            
            menu:
                "Do it.":
                    $ released_fix_rollback()
                    "Trying not to think about his own actions, Rowan leaned in, pressing his mouth against the black leather."
                    "Jezera was almost giddy with excitement, and she actually knelt before him, so she could pat him on the head in a condescending manner."
                    je "Oh Rowan, if only you did as you were told when in the field."
                    je "I'd love to take this a step further, but I fear other responsibilities call us both."
                    je "But I do hope this small display heralds a change in your behavior."
                    "She ran her fingers through his hair. Rowan kept his eyes down."
                    je "You will find servility... Rewarding."
                    "She rose up abruptly."
                    je "I will get you the jewelry."
                    je "Consider yourself dismissed."
                    jump jezDelaneLarge
                    
                "Don't.":
                   $ released_fix_rollback() 
                   "Rowan couldn't force himself to do it."
                   je "Aww... And you were doing so well!"
                   je "But I will recognize the effort."
                   je "I will get you your jewelry, but I hope you will rethink your behavior from now on."
                   je "Think will be so much easier for you if you just do as you are told."
                   "Still on his knees, Rowan said nothing."
                   je "Consider yourself dismissed, Rowan."
                   jump jezDelaneSmall
                   
        "You'll manage.":
            $ released_fix_rollback()
            ro "I wouldn't want to drive a wedge between you and your brother. I'll think of something."
            je "Of course. You are nothing if not resourceful."
            ro "That's why I'm here."
            "Rowan bowed his head stiffly and headed out, holding in his anger."
            $ jezDelaneHelp = "got"
            return
            
else:
    je "Hmm…"
    je "I might have something laying around. Give me some time to look things over."
    ro "Of course, Mistress."
    "Promising. He’ll see what Jezera was willing to part with."
    


if (all_actors['jezera'].favors + all_actors['andras'].favors) < 5:
    label jezDelaneSmall:
    scene bg9 with fade
    "In the evening, he found a small case in his room." 
    "Rings, bracelets, necklaces. Nothing too fancy, but fine gifts nevertheless."
    $ delane_gifts +=10
    $ jezDelaneHelp = "got"
    $ journal.complete_quest_note('orciad', 'note18')
    return
    
else:
    label jezDelaneLarge:
    scene bg9 with fade
    "In the evening, he found a small, open box in his room."
    "Rings, bracelets, necklaces, books, poems…"
    "Fresh, comfortable underwear?"
    "Now that he thought of it, Delane probably could use some..."
    "Surprisingly considerate of Jezera. Delane will be pleased with it."
    $ delane_gifts +=20
    $ jezDelaneHelp = "got"
    $ journal.complete_quest_note('orciad', 'note18')
    return    

###########################################################################
###########################################################################
###########################################################################

label cliohnaDelaneHelp:

scene bg12 with fade
show rowan necklace neutral at midleft with dissolve

ro "Cliohna, do you have a moment?"

show cliohna neutral at cliohnaright with dissolve

"The sorceress looked away from her books and narrowed her eyes, obviously displeased at being interrupted."

cl "A short one."

ro "I need some books that could be of interest to a noblewoman. Do you have anything that fits the profile, that you might be willing to part with?"

if castle.researches['history_of_rosaria'].completed:
    cl "Yes. My assistant will point you towards nonessential tomes. Take as many as you need."

    ro "Excellent."

    hide rowan
    hide cliohna

    "Having already studied and cataloged all of them, it was easy to pick some of the more interesting books for Delane."
    "She should be quite pleased with them."

    $ delane_gifts +=15
    $ cliohnaDelaneHelp = "got"
    return

elif castle._current_research == 'history_of_rosaria':
    
    cl "As you know, I am currently studying the tomes pertaining to Rosaria nobility."
    cl "I will determine what is nonessential to my research, and have it delivered to your room by the end of the week."
    ro "Ah, excellent."

    hide rowan
    hide cliohna

    "Rowan doubted anything in Cliohna's library would prove to be particularly interesting, but even boring books will help Delane pass the time."

    $ delane_gifts +=10
    $ cliohnaDelaneHelp = "got"
    return

else:
    cl "I have yet to study the tomes pertaining to Rosaria nobility."
    cl "But I will have to do so at some point anyway, so if you want to, I can spend the next week sifting through them. Find some that will be of no use to us."

    show rowan necklace concerned at midleft with dissolve

    ro "But it will take you away from your current research."

    cl "Precisely."

    show rowan necklace neutral at midleft with dissolve

    ro "Hm…"

    "Should he tell Cliohna to look through the tomes?"

    menu:
        "Yes.":
            $ released_fix_rollback()
            ro "Do so. Have the books delivered to my room by the end of next week."
            cl "Very well."
            hide rowan
            hide cliohna
            "Rowan doubted anything in Cliohna's library would prove to be particularly interesting, but even boring books will help Delane pass the time."
            $ castle.rp -= 10
            $ delane_gifts +=10
            $ cliohnaDelaneHelp = "got"
            $ journal.complete_quest_note('orciad', 'note17')
            return

        "No.":
            $ released_fix_rollback()
            ro "No. I need you focused on the task at hand."
            cl "Very well."
            "Cliohna's research was too important, he'd have to find another way to gather the gifts he needed to persuade Delane to choose Ulcro."
            $ cliohnaDelaneHelp = "got"
            return

###########################################################################
###########################################################################
###########################################################################

label shaya_Show:


scene bg24 with fade
show rowan necklace neutral at midleft with dissolve

if shayaShowFirst == False:
    jump shayaShowDance
    
else:
    pass

"Rowan arrived at the brothel to find a small crowd waiting in the lobby." 
"Much of the audience consisted of orcs who stood around with impatient expressions. But, a few human mercenaries could be found strewn about waiting. One must have been a commander because he has a large ornate cape hanging down his back."
"He didn’t have to wait long before the brothel’s attendant came to call. She was a pretty girl, with a shapely body and short, styled brown hair." 
"Upon getting a good look at her dress, his eyes widened slightly. It was sheer and made from a fabric so translucent that she nearly looked naked."

lia "Welcome, valued customer. My name is Lia, and I’m here to serve you. You’ve come just in time for the Madam’s show, yes?"

ro "I have. Are you one of the performers?"

lia "Of course not. I’m just the attendant."

menu:
    "Be polite.":
        $ released_fix_rollback()
        show rowan necklace concerned at midleft with dissolve
        ro "Oh, I hadn’t meant to presume."
        lia "You needn’t worry, Sir. I work here by choice. I wish I was allowed to perform like she does."
        $ liaAttitude = "polite"
        
    "Flirt.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        "Rowan took a step closer and examined her more firmly."
        ro "Perhaps they’re making a mistake by not putting you on the stage then. You’re wasted on receptionist duty."
        "He almost began to reach out and touch her, before she took a step backwards to add space between them."
        lia "You may look, but not touch. I’m not one of the girls for sale."
        ro "Of course."
        "But, before he could fear that he overstepped, she smirked softly."
        lia "But, you’re right. I am wasted on receptionist duty."
        "She let out a wistful sigh."
        lia "No girl gets near the stage if the madam doesn’t think her ready."
        $ liaAttitude = "flirt"

"She coughed and held out her hand."

lia "A fascinating discussion, but if you wish to watch the show today, I will have to insist on Payment."

show rowan necklace neutral at midleft with dissolve

"Rowan raised an eyebrow. Payment?"

ro "I was invited here personally by Shaya."

lia "Rowan? Ah, I was told to expect you. No fee."

if liaAttitude == "polite":
    show rowan necklace happy at midleft with dissolve
    "Rowan nodded, but went to the pocket of his belt anyway. There he produced a shining coin and placed it into the girl’s hand."
    ro "Of course. Here’s something for your trouble."
    "The girl’s face lit up at once."
    lia "Ooh. Thank you, Sir. You didn’t have to."
    if avatar.corruption > 30:
        #ro smirk
        "She was right, of course. He didn’t have to. But, in a place like this making a good impression could pay dividends down the road."
    show rowan necklace neutral at midleft with dissolve

"Incense burned at strategic locations around the room, ensuring the lobby was covered in a soft haze. Perhaps to cover the smell?"
"One direction seemed to head down a hallway willed with silk sheets and bead covered gateways. That was almost certainly the path to the private rooms." 
"Another pathway seemed to go back from behind the desk. He strained to see what was back there, but was limited somewhat by his vantage point." 
"Perhaps with a distraction he could see for himself what was back there?"

menu:
    "Just go to the show.":
        $ released_fix_rollback()
        "Rowan shook his head. Trying to sneak away in the middle of a brothel filled with spies seemed a little out of his depth. The best thing to do would be to just go to the show."
        "So he waited until Lia began to usher the audience into the area with the stage."
        "As she led him in, the girl turned back to him."
        if liaAttitude == "polite":
            lia "Right this way, Sir Rowan. I’ll make extra sure you get a good seat."
        else:
            "Right this way, Sir Rowan."
        jump shayaShowDance

    "Create a distraction.":
        $ released_fix_rollback()
        "Rowan slid over to where the mercenary captain with the long cape was sitting. The man didn’t even notice when Rowan placed it’s fabric over one of the softly burning sticks of incense. Then, it was just a matter of waiting."
        lia "Sir! Your Cape!"
        "A few minutes later, the man turned to find a small flame sprouting from his back. The cape had started to burn. Critically, it got the attendant’s attention fixated enough on him that she rushed over. Now was his chance."
        #stealth check - very easy - TODO
        #PASS
        "Rowan made extra sure not to make any noise as he snuck past the desk and slid the door open. Without any eyes on him, he made it into the back hallway."
        "He crept along silently, searching for signs of movement. On one side, he found the entrance to what seemed like a changing room with numerous tall mirrors and locked chests." 
        "Near the back of the hall was a room protected by imposing and ornate locks. The vault for profits, perhaps. But, who knew what else could be back there?"
        "The final room was a combination of living quarters and an office that must have belonged to Shaya. He double checked to ensure he wouldn’t be discovered here, but it seemed like the brothel keeper had already departed for the stage area. "
        "The room was as fancy as any in the brothel. It was filled with furniture, including numerous recliners, a low table, and a work desk. The bed in the far corner was large enough for numerous people."
        "He also took a brief note of the alcove on the back wall that included a small stage. For private performances, perhaps?"
        "To start, he made his way over to the desk. If there were any valuable tidbits of information, they’d be here."
        show rowan necklace angry at midleft with dissolve
        "But, his search rapidly proved fruitless. Most of what the desk contained were records of various stripes, mostly associated with the brothel itself. It seemed that any actual secret intelligence was kept somewhere more secure. Perhaps that room in the back?"
        show rowan necklace neutral at midleft with dissolve
        "What he did find that piqued his interest was a ledger she kept of her own personal clients. Not a large book, for the most part. It seemed a prostitute of her standing dealt with a few clients of high standing, rather than a large quantity of lesser clients."
        "What did stand out to him, however, was the dates in the book. All of them were recent, from the past 2 years." 
        "Why only so many clients recently? She was old enough that she could have plausibly started years before that. Had she simply not had a significant clientele before that point?"
        $ shayaClue15 = True
        $ shayaClueScore += 1
        "Rowan looked around the room. Perhaps he could find something else of note?"
        menu:
            "Search her bed.":
                $ released_fix_rollback()
                "Rowan stopped at her bed and searched around to the best of his ability. He had to be careful, so as to not disturb the state of the sheets." 
                "He noted, with slight amusement, that she hadn’t made her bed. He hadn’t thought her to have much of a lazy side before."
                "Searching beneath the mattress and the sheets offered nothing. It seemed that she didn’t put much stock into “under her bed” as a hiding place. He did find a pair of crimson silk panties, however. From how crumpled they were, it seemed they’d been worn recently."
                menu:
                    "Sniff it":
                        $ released_fix_rollback()
                        show rowan necklace aroused at midleft with dissolve
                        "Rowan smirked and placed the panties to his nose to get a whiff. Once he’d had his fun, he snuck them into the same exact spot he’d left them."
                        $ change_base_stat('c', 3)
                    
                    "Put it back.":
                        $ released_fix_rollback()
                        "Rowan shook his head and placed them back in the exact spot he’d found them."
                    
                "With a sigh, he made sure the bed was in the exact same state he’d left it."
                
            "Search her changing corner.":
                $ released_fix_rollback()
                "Rowan went to the ornate wood carved changing screen and looked behind it." 
                "To no surprise, it was a mostly sparse segment of the room, with a few cabinets on a side table. Prominently there was a small chest with jewelry in it. Bangles, golden beads, even a few piercings. Though, from its small size, it was unlikely it was her main jewelry chest."
                "Another small chest next to the table held a few quick outfits. Mostly a few pieces of lingerie, likely in case a client wanted her to wear them."
                "There was a small tray with a few types of makeup in place. Some of it was black eyeshadow, of the sort that he’d heard was popular in Qerazel. But, that tray was fairly sparse."
                #Perception check: Difficulty: Hard for early game. Medium for mid game. - TODO
                #PASS
                "Rowan raised an eyebrow. When he’d stopped by the general changing area, he’d seen large makeup trays along with any of the open chests. Looking sexy was such a vital part of their job, after all. There was almost none here by comparison."
                "Did she have more makeup somewhere else? Then again, makeup didn’t require taking up space as jewelry or outfits might. Why would the most important courtesan have less than any of the others?"
                "Thinking about that made him notice something else. The absence of mirrors was curious. There was a small hand mirror for makeup on the table. But, no other reflection. He’d expected mirrors on the other side of the changing screen, but there was nothing."
                "The changing area for her girls had such large mirrors. Why weren’t there any here?"
                "Rowan stroked his chin. Perhaps she rarely felt she needed a mirror? Or makeup too for that matter. Was she so confident in her own beauty?"
                "Well, considering the way she looked, why shouldn’t she be confident?"
                $ shayaClue16 = True
                $ shayaClueScore += 1
                
                #FAIL
                #"Rowan sighed. Nothing else here either. It seemed this entire risky excursion might prove a pointless risk."

        "Shaking his head, Rowan ensured that everything was in the exact place he’d found it before his search."
        "His little scouting mission complete, Rowan crept back towards the lobby. With some luck, the show would not have begun by now. Too bad his search had been for nothing..."
        jump shayaShowDance
        
            #FAIL
            #"Rowan had put a hand on the door handle before the effort ended in failure. In opening the door, there was a loud creak."
            #lia "What was that?"
            #"She only failed to catch Rowan because he ducked under the desk before she could turn her head. He swore under his breath. But, that likely represented the end of his espionage efforts. Lia was looking right at the door now."
            #"He was forced to sneak back into the crowd of waiting men. At the very least, he’d still get a chance to see Shaya’s show…"
            #jump shayaShowDance


label shayaShowDance:

#shaya dance CG
scene cg219 with fade
pause 3

"A cheer roared out amongst the crowd. Shaya lowered herself into a squat behind the onyx cock and rubbed her crotch from base to head, in a rhythmic motion, steadying herself with her right hand."

show cg220 with dissolve
pause 2

"It was a dance, and the cock was her partner. She shifted position, dancing around it. At one point leaning over so the entire audience could stare down her top while rubbing her behind against the fake cock’s surface."

show cg221 with dissolve
pause 2

"This posture, positioned as if she was being taken from behind, was the one she settled into. What followed was the most provocative display of all. She rolled her hips up and down and even let out a long low moan."

show cg222 with dissolve
pause 2

"At first it was slow, She rolled her head in a circle and faked a long moan. But, as she went the dance became more frantic, almost leaping in place."
"She concluded the dance by jumping, a simulation of an orgasmic spasm, and spinning in a circle to wrap her arms around the prop. When she came to a stop, it was with her arms wrapped around her onyx co-performer and body pressed to it like a lover."

show cg223 with dissolve
pause 1
show cg224 with dissolve
pause 3

scene bg24 with fade
show rowan necklace aroused at midleft with dissolve
show shaya happy at midright with dissolve

"When the music came to a halt, a cheer went through the crowd. How could they not love a performance like that? Roman himself could attest to its effectiveness."

if shayaShowFirst == True:
    "This Shaya he’d never seen before, this vixen on stage, let out an appreciative purr. She basked in the attention of the crowd. "
    
else:
    pass

"But, Rowan didn’t bother to approach the stage or try to talk to her. Shaya was working. As soon as the performance was done, men were calling out from the seats asking to be first in line. Shaya walked into the crowd and threw herself into the arms of a hungry looking mercenary."
"Rowan stood up and made for the exit. But, even as he did, he looked back at Shaya in the moment before she disappeared into the silks of the back rooms. She was eyeing him as well. Once more he could only suppose she was smiling."

if shayaShowFirst == True:
    $ shayaShowFirst = False
    scene bg9 with fade
    show rowan necklace neutral at midleft with dissolve
    "That night, before anything else, Rowan sat down in the chair by his desk. The segment of parchment he’d drawn up the day he met Shaya was in his hands."
    "{i}Who is Shaya?{/i}"
    "Rowan frowned and started to write."
    "{i}Shaya is…{/i}"
    "But he could go no further. He hadn’t really answered that question, had he?"
    if shayaClue15 == True:
        "He put down some notes on what he discovered from his excursion back in her chambers. A few details from the notes that he found in her desk, for example."
        "The one detail that stood out to him the most was the absence of client records until relatively recently." 
        "Perhaps those records were hidden somewhere else? Maybe her training had taken more years than he’d anticipated? Or maybe she just hadn’t had any high calibre clients until the recent past?"
        "But, surely a courtesan of her beauty and training must have had some high profile clients even when she was still new?"
        "On his parchment, he jotted down a question." 
        "{i}Where are her original clients' records?{/i}"
        if shayaClue16 == True:
            "He almost folded the parchment back up before he remembered another detail particularly worthy of note. It had almost slipped his mind, amidst other thoughts."
            "{i}Why doesn’t Shaya keep much makeup or any large mirrors?{/i}"
            "At the time, it had seemed odd. After having seen her performance, and the near perfection of her beauty, it felt damn near impossible."
        "When he finished, he slid the parchment back into its particular hiding spot and slumped down in his chair. Somehow, he felt no closer to understanding who Jezera’s mysterious friend was. Perhaps he’d get another chance to learn more in the future?"
        "Certainly, there were less exciting ways to spend an afternoon than learning about the glamorous brothel keeper by exploring her perfumed halls..."
    else:
        "Rowan let his hand with the quill fall to his side. He really hadn’t discovered much about her today, had he?"
        "His main observation had been…."
        scene cg219 with fade
        pause 2
        show cg220 with dissolve
        pause 2
        show cg221 with dissolve
        pause 2
        show cg222 with dissolve
        pause 2
        show cg223 with dissolve
        pause 1
        show cg224 with dissolve
        pause 3
        scene bg9 with fade
        show rowan necklace aroused at midleft with dissolve
        "Rowan frowned and brought his quill back to the parchment."
        "{i}Shaya is…radiant.{/i}"
        "Then, he tucked the parchment back in its book and retreated to bed. He had a lot of important things on his mind that he needed to...work out."

else:
    pass

return


