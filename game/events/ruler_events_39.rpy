init python:
    
    event('jezera_rowan_stressed', triggers="week_end", conditions=('week > 30', "all_actors['jezera'].total_favors > 0", "castle.buildings['forge'].lvl >= 1",), group='ruler_event', run_count=1, priority=pr_ruler)
    event('cliohnas_menial_help', triggers="week_end", conditions=('week > 10', "castle.buildings['forge'].lvl >= 1",), group='ruler_event', run_count=1, priority=pr_ruler)
    event('alexia_consultation', triggers="week_end", conditions=('week > 10',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('alexia_potion_stealing', triggers="week_end", depends=('alexia_consultation', 'nasim_intro',),group='ruler_event', run_count=1, priority=pr_ruler)
    event('rowan_frustration_venting', triggers="week_end", conditions=('week > 10', 'avatar.corruption > 50', 'all_actors["alexia"].relation < 30', 'bootlegAlexiaSeen == True',),group='ruler_event', run_count=1, priority=pr_ruler)
    event('cup_of_tea', triggers="week_end", conditions=('privateDanceSeen',),group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg24")
    event('password_is_fidelio', triggers="week_end", depends=('cup_of_tea',),group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg24")

label jezera_rowan_stressed:

scene bg6 with fade
show rowan necklace angry at midleft with dissolve
#liurial concerned
show liurial neutral at midright with dissolve

liur "Are you sure you’re okay?"

ro "I’m {i}fine{/i}."

liur "We can just file the reports later if you need time to-"

"Rowan let out an angry sigh, pinching his brow together in frustration. He had to keep a level head. After all, it wasn’t her fault."

ro "There’s no time, Liurial! Greyhide’s shipments have been backed up for days. Andras is about to lose his mind cause his men aren’t getting refitted."
ro " I’ve got Cla-Min breathing down my neck about her new caravan routes, and now {i}Cliohna{/i} of all people is asking for a procurement of..."

"Rowan double checked the small, prim writing scrawled out on the requisition form."

ro "‘Ostenfish slime?’"

liur "I- uh… believe that’s a fish native to the Dragon’s Tail? I could be mistaken."

ro "It doesn’t matter. If I don’t get this paperwork done by tomorrow, we’ll be delayed for a week or more."

liur "It’s not the end of the world, I can take care of it for you."

ro "No. I need to do this."

liur "Rowan, you’ve been at it nonstop since I got here. When was the last time you took some actual time for yourself?"

"Rowan didn’t know, but he wasn’t about to admit it."

ro "I’m fine, leave me be."

show jezera neutral at edgeleft with moveinleft

je "No. You really aren’t."

"Rowan only realized that his mistress was in the room when he looked up from his desk. Liurial had frozen stiff, a worried expression coming to her face as she did her best to fade into the background."

ro "Mistress Jezera! I... didn’t see you come in."

show jezera happy at edgeleft with dissolve

je "You seemed so preoccupied, I didn’t want to interrupt."

ro "I’m sorry, I didn’t even realize-"

je "It’s perfectly fine, my hero. I can hardly fault you for your diligence."

show jezera neutral at edgeleft with dissolve

je "What's all this about a shipment?"

ro "Nothing you need concern yourself with, my lady, I’ve got it taken care of."

show jezera displeased at edgeleft with dissolve

je "..."

show jezera happy at edgeleft with dissolve

je "Liurial, does Rowan speak true?"

liur "M-my lady?"

show jezera neutral at edgeleft with dissolve

je "You seemed to be of the opinion that he was overwhelmed with work. Is this so?"

liur "Rowan is... a perfectly able administrator, my lady. I have complete confidence in his ability to-"

show jezera displeased at edgeleft with dissolve

je "That’s not what I asked."

#liur concerned

liur "Um…"

"Liurial’s worried frown bespoke her hesitation. Much like Rowan, she didn’t want to say the wrong thing to their mistress."

liur "He is… "

#liurial neutral

liur "He could use a break, my Lady."

je "Are you capable of completing these tasks on his behalf, odious as they might be?"

show liurial happy at midright with dissolve

liur "To perfection, my lady."

show jezera happy at edgeleft with dissolve

je "Good! Then I leave them in your capable hands."

liur "Yes, my lady."

ro "But-"

je "Come along Rowan, there’s something I need to discuss with you."

scene bg18 with fade
show rowan necklace concerned at midleft with dissolve
show jezera happy at midright with dissolve

"Jezera led him in a direct beeline to her private chambers, pausing only long enough to exchange a few muttered words with a passing maid." 
"She repeatedly shot eyes in Rowan’s direction, teasing glances that made him only worried him more. It worsened once they were left alone in her room."

ro "What is this about? "

"Jezera’s eyebrow quirked with amusement. She let out a giggle."

je "What do you think this is about?"

ro "Have I done something to displease you?"

je "Why, Rowan! I’m insulted!"
je "I invite you into my private chambers, and the only thing you can think of is that I’m here to {i}chastise{/i} you?"

"Smiling, the half demon gestured towards the modest dinner table on the other side of her room from her bed. Wary, Rowan took a seat."
"Far from giving him a tongue lashing, the sultry creature settled into the seat across from him, crossing her leg over her knee in a coquettish posture as she leaned back into her chair."

je "You seem pent up."

ro "I’m fine."

je "Come now, hero. It’s me: there’s no need to play games."

ro "It seems like that’s all we ever do."

"The Demon’s smile widened. She leaned forward, giving him a glimpse of her ample cleavage as she boldly uncrossed her legs and recrossed them again."

je "Really? That’s all there is between us?"

ro "I don’t know what you want."

je "A romantic dinner."

"Rowan stared at her a moment, his brain trying and failing to connect the dots."

ro "...Excuse me?"

show jezera displeased at midright with dissolve

je "Her faithful servant seemed so distracted lately, the lady began to despair. She was so lonely... wasn’t she worthy of his attention anymore?"

show jezera neutral at midright with dissolve

"The Demon leaned forward again, her eyelids dropping as her lips gently pursed."

je "The fear of his apathy ate at her… didn’t he care for {i}her{/i} feelings? Couldn’t he see how desperate she was to spend time with him, even if was only under pretense?"

show rowan necklace angry at midleft with dissolve
show jezera happy at midright with dissolve

ro "Stop it."

"Jezera settled back into her seat with a triumphant grin, her eyes dancing dangerously in their sockets."

je "And here I took you for a romantic."

ro "I thought you were done playing games with me."

je "There are a few left to play, I’ll admit… but isn’t the chase better than the catch, anyway?"

ro "I wouldn’t know."

je "Oh, I think you would."

"Jezera clapped her hands, and the doors to her bedroom were opened. Four maids carrying stacked trays emerged."
"Their attire was skimpy, their movements quick and precise as they laid out a sumptuous meal for the two of them. Rowan watched with unease as they set out a complex arrangement of silverware in front of him."

if all_actors["alexia"].relation >= 30:
    ro "I… I need to get back to my wife."
    je "Don’t be silly, Rowan. I let you off work early precisely to avoid inconveniencing you. There will be time enough for her later, I’m sure."
    je "For now, you’re all mine."

else:
    ro "I… I really should finish that work."
    je "Liurial has it well in hand, my faithful servant."
    je "Your dedication to our cause is admirable, but you really need to learn the value of relaxation."
    
"Rowan settled into an uncomfortable repose. He was overenergized, his thoughts darting off in different directions at all that he had left to do, all that he had left undone."

show mary neutral at edgeright with dissolve

mary "{i}Oh!{/i}"

"One particular maid jumped in place as Jezera casually groped her bum. Her face went red as she continued to lay out the pork roast, but there was a tugging smile on her lips."

je "So tell me Rowan: how have you been?"
je "All these months of toil, of working so hard for my brother and I… such efforts would wear down any man."
je "Even you."

menu:
    "Admit you are stressed.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        "Rowan sighed, putting his hand over his eyes as the maids removed the covers of the platters to reveal the numerous courses."
        ro "I’m… it has been a trial."
        je "I know. I can see it in your eyes."
        ro "There’s so much to do, so many hurdles to overcome. And it never ceases."
        je "Yet you tackle each one with such {i}tenacity{/i}."
        ro "I don’t know about that."
        je "You are a diligent steward, Rowan. Too diligent, sometimes. You need to learn when to relax."
        "Rowan huffed, gesturing around at the ostentatious room, the sumptuous arrangement of food and the blushing maids who Jezera kept groping."
        ro "And… this is relaxing to you?"
        "Jezera smirked, her eyes alight with mischief."
        je "It isn’t to you?"
        ro "Evidently, not in the same way."
        je "You just haven’t been properly introduced to the method. Here, allow me..."
        
    "Play it off.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        ro "I am fine, lady Jezera. You just caught me at a bad moment."
        je "You don’t have to pretend for my sake. Your ego can stand the shock, I’m sure."
        ro "I’m not pretending."
        je "Then, sweet hero, you’re deluded."
        je "You’re wound so tightly I’m afraid you’re going to snap like a bedspring."
        je "This meal is for {i}your{/i} sake. So stop putting up such a brace face and embrace it. You’ll feel better afterwards, I promise."

"Jezera clapped her hands again, and the maids froze at attention. They filed into a line in front of her, for Jezera’s viewing pleasure." 
"After a long moment of deliberation, she pointed at one of them."

je "You."

mary "Yes, my lady?" 

je "You’ll do. Come here, I have need of entertainment for the meal."

"Giggling, the maid sidled over into Jezera’s lap. The Demon wasted little time in getting to know the ins and outs of her maids’ curvy features. Her hand disappeared down her skirt."

je "Feel free time take your pick, Rowan. It is, after all, {i}our{/i} evening. You deserve some stress relief."

menu:
    "Pick a maid for ‘stress relief’.":
        $ released_fix_rollback()
        "Rowan let out a dissatisfied grunt. He wasn’t {i}happy{/i} this was happening, but perhaps it was for the best after all."
        "He perused the faces of the remaining three maids, settling on one whose innocent face and long, blonde curls were particularly pleasing to him. With some reluctance he gestured to her."
        ro "You."
        "She tittered and approached him, her long legs pronounced within the thigh-high black stockings she wore. As she came close Rowan saw the floral detail in the filigree." 
        "She plopped down in his lap, adding an eager wiggle from her bottom as she did so."
        #CG1
        scene cg806 with fade
        show jezera happy behind cg806
        show rowan necklace neutral behind cg806
        show mary neutral behind cg806
        pause 3
        je "See? Was that so hard?"
        je "Then again… I suppose that is the point for you men, isn’t it?"
        "Chuckling at her own joke, the Demon gestured with an enthusiastic flourish towards the food."
        je "Eat! Enjoy yourself, you have my permission."
        je "Sample the food, sample the maids, sample whatever you desire. It makes no difference to me where you find your pleasures, only that you find them."
        "The curvaceous maid with the curly locks of hair smiled at him. She picked up a morsel from the table and popped it into his mouth. Rowan smirked as he chewed, tasting the expensive pork on his tongue."
        "The maid squirmed in Rowan’s lap, making a great show of struggling to find a comfortable spot on her makeshift chair. Rowan felt himself harden as she made contact with his groin. She cooed and repeated the process." 
        "He settled into his seat, leaning back as the maid began to softly grind against him. {i}Perhaps this isn’t so bad after all{/i}, he thought as he plucked another morsel of meat and slipped it into his mouth." 
        "Jezera was openly groping the other maid’s breast, her nimble fingers peeling back her constricting top and exposing her pretty pink nipple. She toyed with it between her fingers as the maid squirmed and groaned."
        ro "Quite the romantic dinner."
        je "It is, isn't it? I couldn’t have picked a better person to share it with."
        "It was hard to take her seriously when her hands were all over the other maid. Her fingers worked furiously at something beneath her skirt, and her other hand roamed with greedy aplomb across the bare skin of her breasts."
        "Rowan got into the act as well. His hands slid beneath the too-short fabric of the blonde maid’s skirt. He was shocked to feel warm, yielding flesh between his fingers. The tramp wasn’t even wearing undergarments!"
        "She gasped in his grasp as he slid a few fingers into her sodden box. She shook her head back and forth, sending her blonde curls spinning about in pleasing circles."
        je "My hero and I are weary. Feed us, servants."
        "The two maids not in the midst of being molested moved to comply, but Rowan held up a hand."
        ro "No. You two."
        "The two blushing maids sitting in Rowan and Jezera’s lap shared a sultry look. With trembling fingers and muted gasps they did as they were told, picking grapes and feeding them into the mouths of their aggressors."
        "Jezera bent her head down and planted a love bite on her maid’s neck. She shivered and gasped, going stiff from the firm contact." 
        "A subtle wink from Jezera spurred on Rowan to repeat the action with his own. Taking the initiative, he took her chin firmly in hand and tilted her face downward. Their lips met, and they shared a short, passionate kiss."
        je "Enough distractions. We have yet to finish our meals, after all."
        "At first Rowan thought he had gone too far, but the naughty look in Jezera’s eyes reassured him that this was merely the first step."
        scene cg807 with fade
        pause 1
        show cg808 with dissolve
        pause 1
        show cg809 with dissolve
        pause 2        
        show jezera happy behind cg809
        show rowan necklace neutral behind cg809
        show mary neutral behind cg809
        "The Demon worked her fingers around beneath the helpless maid’s skirt for a few moments more, then slid her off her lap." 
        "Her hand went to the top of the maid’s head, and she quickly got the message. With Jezera’s help, she bent down beneath the table, her head disappearing suspiciously close to Jezera’s lap."
        "Rowan got a last, casual grip on the blonde maid’s behind, pinching it before letting her slide ever so slowly off his lap. She giggled and spun around, clambering down on hand and knee till she was kneeling at the altar of his manhood."
        je "{i}Mmmh{/i}, now where were we?"
        "Rowan grimaced in repressed pleasure as he felt the maid’s fingers encircle his manhood through his trousers and began to stroke."
        ro "Something about releasing stress?"
        "Jezera smirked, her blush deepening as the wet sounds of slurping rose up from beneath her."
        je "Sorry, I can't say I’m very well versed in releasing something I rarely feel."
        "The blonde maid’s talented fingers peeled away Rowan’s pants, exposing his rock hard member to her viewing pleasure. He felt the wet warmth of her lips compress around his cockhead as he took a brief sip of wine."
        ro "I’ve some experience in the subject."
        je "Then tell me: is a night like this- {i}mmmmh{/i}! S-sufficient to release some of that… {i}tension{/i}?"
        "Rowan wasn’t imagining things. Jezera was shooting bedroom eyes at him while getting eaten out. The scene would have once been ludicrous to him before coming to Bloodmeen. Now, it just quickened his heartbeat."
        "The blonde maid was already well on her way to cramming every inch of his dick down her throat. He glanced briefly under the table to see her legs were spread, a small puddle of wetness beneath her as she greedily gobbled him up."
        "It is… effective, for sure."
        "Jezera grinned as the two remaining maids stood stock still at her side. From the way they shifted back and forth on their heels, they evidently were enjoying the view. Jezera reached out and groped one of them as her other hand went under the table."
        je "Good help is so hard to find, these days. I’m glad I can at least count on {i}someone{/i} in this castle."
        show cg810 with dissolve
        pause 2        
        show jezera happy behind cg810
        "Rowan picked a small crabapple that sat upon a platter, biting into the juicy flesh of it as the blonde maid reached the base of his cock. His hand filtered through her hair, fingers clenching tight against the back of her head."
        "He held her there for several seconds, reveling in the control he had over her. Maybe there really was something to Jezera’s method, after all. He was certainly starting to feel better about things."
        je "It’s moments like these that we struggle for, hero. The times when we can- {i}hmm{/i} - lie back, and enjoy the fruits of our labours."
        scene cg811 with fade
        pause 3       
        show jezera happy behind cg811
        show rowan necklace neutral behind cg811
        "The blonde maid’s head bobbed back and forth, back and forth against his crotch as she cupped his balls in her hand. Her movements were precise, her rhythm impeccable. It did not take long for Rowan to feel a rough stirring in his groin."
        "Jezera smiled at him, her lips curling into a seductive smirk. The way her eyes were fluttering, she looked close too."
        je "Cum. I know you’re holding back."
        ro "I’m not holding back."
        je "-Says every man ever. No need to be modest, Rowan. It’s not {i}our{/i} romantic evening… yet."
        show cg812 with dissolve
        pause 1
        show cg813 with sshake
        show cg813 with sshake
        show cg814 with flash
        pause 1
        show cg815 with dissolve
        pause 2
        show mary neutral behind cg815
        "The fantasy of Jezera being where the maid was in that moment was enough to push Rowan over the edge. He gripped her by her blonde, curly hair and held her fast to his stomach."
        "Mental images of fucking the entrancing Demon in every despicable, degenerate way possible ran through his head as he thickened and came."
        "White ropes of masculine virility let loose within the maid’s mouth. She grunted and gagged, but Rowan held her firm."
        "Jezera’s eyes rolled upward, her back arching as she grabbed onto the back of her chair for support. The Demon and her hero watched with smouldering arousal as their significant other came at the table."
        je "{i}Mmmh{/i}! Goodness, that was a great one."
        "She poked her head under the table and patted the maid’s head."
        je "Well done. You can come out from under there now."
        mary "At once, my lady!"
        "The grinning maid flounced out from under the table like a cat that had gotten its cream. Beaming, she took her place alongside the other two maids, her face still splattered with Jezera’s juices."
        je "How was it, Rowan?"
        "Rowan leaned back and looked under the table. The blonde maid met his eyes with a submissive smile, his cock between her suctioning lips still."
        "She pulled free, stroking him one more time before clambering out from under the table as well. She took her place next to her fellow maids, her face a hot mess of dripping cum."
        je "…I suppose the question answers itself, doesn’t it?"
        return
        
    "Politely decline.":
        $ released_fix_rollback()
        "Rowan sat up stiffly in his chair, his back as rigid as a washboard."
        ro "I promise you, my lady, I’m fine."
        ro "It’s not that I don’t appreciate the gesture, I’m just… not in the mood."
        "Jezera’s eyes held to his for a long moment, then she shrugged."
        je "Suit yourself. You can’t claim I never tried."
        je "I trust you’ll at {i}least{/i} accompany me for the remainder of the meal?"
        ro "I’d be happy to."
        je "Good! I could use some lively conversation while I enjoy my meal."
        "Jezera’s roaming hands across the maid’s blushing body made it somewhat unclear what she precisely meant by ‘meal.’"
        $ change_favor('jezera', -1)
        return

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################

label cliohnas_menial_help:

$ tempMCDenied = False

scene bg22 with fade
show rowan necklace angry at midleft with dissolve

"Browsing through the reports, Rowan walked into the forge, fuming."

ro "Greyhide, I’ve been getting complaints about delays this week. What is- "

show rowan necklace shock at midleft with dissolve

ro "Greyhide?"

show rowan necklace shock at center with moveinleft

"The minotaur was nowhere to be seen. Only his help remained, doing his best to keep up the production. But not one of them had his skills, nor his strength."

show rowan necklace neutral at center with dissolve

ro "Where’s the forgemaster? "

"The men all looked away, except for one brave soul. He approached Rowan, and in a hushed voice, explained everything to him."

scene black with fade

"..."

scene bg12 with fade

show rowan necklace angry at midleft with moveinleft
show cliohna neutral at cliohnaright with dissolve

ro "Cliohna…"

cl "Rowan. Unless it’s something important, I’m afraid you will have to wait. I am preoccupied with a project."

if cliohnasChampion == True:
    show rowan necklace aroused at midleft with dissolve
    show cliohna happy at cliohnaright with dissolve
    cl "Unless you’re that starved for my attention. Then maybe I might find a moment to sneak away."
    "She flashed him that small smile that made his knees go weak. Mindful of the people around them, he coughed awkwardly, and pretended not to see it."

show rowan necklace neutral at midleft with dissolve

ro "That’s exactly what I’m here about."

if cliohnasChampion == True:
    show cliohna neutral at cliohnaright with dissolve

ro "It has come to my attention that {i}you have stolen my forgemaster{/i}."

show rowan necklace neutral at edgeleft with moveoutleft
show cliohna neutral at center with moveinright
show greyhide neutral at edgeright with dissolve

"He extended his hand to the middle of the room. At the heart of it, stood Greyhide, holding a massive sphere of sorts, with runes all over it." 
"The tame minotaur kept turning it in various directions, at the behest of one of Cliohna’s assistants. He looked to Rowan, resignation clear on his muzzled face."

libass "Eyes on the artifact, forgemaster."

gh "Of course. I apologise."

hide greyhide with moveoutright
show cliohna neutral at cliohnaright with moveoutright
show rowan necklace neutral at midleft with moveinleft

"Rowan waited for Cliohna to explain herself, but the librarian only tilted her head a little, confused at what all the fuss was about."

ro "Cliohna, you can’t just take away Greyhide because it’s convenient for you. He has responsibilities."
ro "Why do you even need him in the first place?"

show cliohna happy at cliohnaright with dissolve

cl "Ah, because he’s the perfect help for what I’m struggling with at the moment!"
cl "This container we’ve recently uncovered has been forged with a specific type of metal that disrupts magic."
cl "This makes manipulating it through telekinesis bothersome, and I can’t exactly roll it around the floor. It’s a precious artifact, not a playing ball."
cl "So I asked the minotaur - Greyhide, that is - to lend us a hand. His massive strength and tranquil disposition are exactly what I needed here."

if cliohnasChampion == True:
    ro "Just asked, or…?"
    "She flashed him another smile. How long has it been since the two of them had a moment to themselves? Too long."
    cl "Just asked."
    show cliohna neutral at cliohnaright with dissolve
    
else:
    show rowan necklace angry at midleft with dissolve
    show cliohna neutral at cliohnaright with dissolve
    ro "You mean you bullied him into it."
    cl "I asked. Politely."
    show rowan necklace neutral at midleft with dissolve
    
ro "… You know, you could just ask Skorderd to have one of his people prepare you a specialized stand for it."

cl "I could. But that would take time to make."

if cliohnasChampion == True:
    "Her eyes briefly ventured from side to side. Everyone was busy with the sphere, even Greyhide."
    show bg12 with pinkflash
    show rowan necklace aroused at midleft with dissolve
    show cliohna happy at cliohnaright with dissolve
    "Her hand made a small gesture, and Rowan saw the pink flames dance between her fingers again. The pleasant fog settled into his thoughts again, and he struggled not to moan."
    cl "Rowan, you know how glad I am that you always find the time to {b}listen to me{/b}. I understand your concerns, but {b}there is nothing to worry about{/b}."
    cl "Simply {b}let me do as I please{/b} with Greyhide for a few hours."
    show rowan necklace neutral at midleft with dissolve
    "It wasn’t a strong spell. More of a pleasant reminder. He could shake it, without any trouble."
    show rowan necklace aroused at midleft with dissolve
    "But why would he?"
    menu:
        "She’s free to use Greyhide for however long she wants.":
            $ released_fix_rollback()
            show rowan necklace neutral at midleft with dissolve
            ro "… If he’s that imperative for your work, I suppose the forge will have to do without him for the afternoon. Just don’t overdo it, okay?"
            cl "Of course. Now if you don’t mind, I believe you must {b}focus on your own duties{/b}."
            hide rowan with moveoutleft
            scene black with fade
            "Her mental command pushed him to the door. The spell didn’t lift - instead, it lingered in the back of his mind as he went on with his day, making even the smallest of tasks feel exhilarating."  
            "He probably shouldn’t let her toy with Greyhide like that, but… No harm, no foul." 
            $ change_research_bonus(3)
            $ castle._iron -= 3
            return
            
        "“But the paperwork…”":
            $ released_fix_rollback()
            show rowan necklace concerned at midleft with dissolve
            show cliohna neutral at cliohnaright with dissolve
            ro "… from all of this is going to be a massive headache. For both of us."
            "For a moment, her eyes flickered with disappointment, but it disappeared as quickly as it appeared, along with the pink flames. Rowan felt the fog lift, and breathed a sigh of relief."
            show rowan necklace happy at midleft with dissolve
            show cliohna happy at cliohnaright with dissolve
            cl "Of course. I wouldn’t want to cause you trouble Rowan."
            show rowan necklace neutral at midleft with dissolve
            show cliohna neutral at cliohnaright with dissolve
            cl "So what will it be?"
            $ tempMCDenied = True
            jump stolenFMChoice
            
else:
    cl "Don’t worry, I won’t keep him occupied for long."
    
label stolenFMChoice:
    
menu:
    "Use the orcs. They’re trained enough.": #if morale < 79
        $ released_fix_rollback()
        show cliohna angry at cliohnaright with dissolve
        ro "I’m sure you could replace Greyhide with an orc or two."
        cl "Rowan, this task requires precision and care. If one of them drops it-"
        ro "They won’t. I’ve been making sure they treat their duties seriously. I wouldn’t suggest them otherwise."
        show cliohna neutral at cliohnaright with dissolve
        cl "Hm. Very well. But if something happens, that’s on you."
        show rowan necklace neutral at edgeleft with moveoutleft
        show cliohna neutral at center with moveinright
        show greyhide neutral at edgeright with dissolve
        cl "Forgemaster, please set the container over there. Your assistance has been greatly appreciated."
        hide rowan with moveoutleft
        hide greyhide with moveoutleft
        "The minotaur lowered his head respectfully, then quickly hurried out of the room, before Cliohna changed her mind. Rowan bid the sorceress goodbye, and followed after him."
        $ change_research_bonus(3)
        $ change_morale (-5)
        jump leavingWithGreyhide
        
    "Let her use Greyhide.":
        $ released_fix_rollback()
        show cliohna happy at cliohnaright with dissolve
        ro "If it’s really just for a few hours, and he did agree… Fine. But don’t make a habit out of it, alright?"
        if tempMCDenied == True:
            cl "And after complaining about the paperwork behind it… You do enjoy playing with me, don’t you Rowan?"
            "The latter was spoken in a soft murmur intended for his ears only. She smiled again, but he didn’t return the gesture. It was important to set boundaries, especially where Bloodmeen business was involved."
        show cliohna neutral at cliohnaright with dissolve
        cl "Only a few hours. I promise."
        hide rowan with moveoutleft
        show cliohna at center with moveinright
        show greyhide neutral at edgeright with dissolve
        "Greyhide threw him a pitiful look, but didn’t speak up. Whatever Rowan’s opinion of the forgemaster, the minotaur had to stand up for himself, especially in situations like these. "
        $ change_research_bonus(3)
        $ castle._iron -= 3
        return
        
    "Have her commission for a stand. It will be useful later.":
        $ released_fix_rollback()
        show cliohna angry at cliohnaright with dissolve
        ro "It’s not like you to cut corners Cliohna. Ask Skorded to craft whatever specialized tools you need."
        show cliohna neutral at cliohnaright with dissolve
        cl "I suppose there is some truth in that statement. Very well."
        show rowan necklace neutral at midleft with dissolve
        show rowan necklace neutral at edgeleft with moveoutleft
        show cliohna neutral at center with moveinright
        show greyhide neutral at edgeright with dissolve
        cl "Forgemaster, please set the container over there. Your assistance has been greatly appreciated."
        hide rowan with moveoutleft
        hide greyhide with moveoutleft
        "The minotaur lowered his head respectfully, then quickly hurried out of the room, before Cliohna changed her mind. Rowan bid the sorceress goodbye, and followed after him."
        $ change_research_bonus(1)
        $ change_treasury (-20) 
        jump leavingWithGreyhide

label leavingWithGreyhide:

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve

ro "Miss Cliohna is not as intimidating as the masters, but I still wouldn’t want to get on her bad side."

if hypnosis2SubEnding == True:
    show rowan necklace happy at midleft with dissolve
    ro "She might be a little intimidating, but she has a softer side too. You just have to be honest with her."
    gh "That is a virtue few people appreciate."
    gh "And if I were to be honest, I would have to ask about her dress."
    ro "Surely not to complain?"
    gh "… … … … … … … … … No."
    
elif breakingCliohna == True:
    #rowan smirk
    show rowan necklace happy at midleft with dissolve
    ro "She talks big, but she respects people who push back."
    #rowan happy
    gh "I do not have a deathwish, Rowan. "
    
else:
    show rowan necklace neutral at midleft with dissolve
    ro "She is something of a mystery. Probably wise to play it safe."
    gh "My thoughts exactly, Rowan."
    show rowan necklace happy at midleft with dissolve

gh "I will resume my duties at once. You have my thanks."
ro "Anytime, Greyhide."
return

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

label alexia_consultation:

scene bg20 with fade
show rowan necklace neutral at midleft with dissolve
show skordred neutral at midright with dissolve

ro "Skordred, look, I share your concerns about the sanitary regime within the castle, but it’s not a problem I can fix either on my own or within a week’s span. But if we talked to the twins about it… "

show alexia 2 necklace neutral at edgeleft with moveinleft

al "You wanted to see me, dear?"

if all_actors["alexia"].relation < 50:
    show rowan necklace happy at midleft with dissolve
    ro "Ah, Alexia. Well, not me exactly..."
else:
    show rowan necklace angry at midleft with dissolve
    al "Finally. And no, not me exactly, but…"
    
show rowan necklace concerned at midleft with dissolve

"He pointed to the dwarf on his right. Before them laid the castle’s latest blueprints, heavily drawn over, with scribbles on every corner. Result of countless hours of work."

show rowan necklace angry at midleft with dissolve

"Pointless work."

show skordred happy at midright with dissolve

sk "Lady Alexia, terribly sorry to bother ya, but I had hoped ya would, ah, share with us some of yer womanly insight?"

show alexia 2 necklace shocked at edgeleft with dissolve

ro "Skordred believes we will need a nursery."

show alexia 2 necklace neutral at edgeleft with dissolve

"He rubbed his eyes, trying to keep the irritation out of his voice. Skordred was all but oblivious to that, and instead regarded Alexia with a wide smile."

sk "Indeed! For centuries, the castle was forced to be rebuilt after each failed invasion, Kharos’ chosen slain by the Solansian bastards! But never again!"
sk "Masters are here to finish what Karnas started, and their children will carry Kharos’ will into a new era! The Twins will start a dynasty that will last a thousand years!"

show alexia 2 necklace happy at edgeleft with dissolve

al "And you want to make sure the castle is prepared for it. That’s very thoughtful of you Skordred."

ro "Maybe so, but it’s not exactly our priority concern at the moment… "

show rowan necklace neutral at midleft with dissolve

al "Of course. But it doesn’t hurt to plan when there’s still time. World conquest can wait for one afternoon."

show skordred neutral at center with moveinright
show rowan necklace neutral at midright with moveoutright
show alexia 2 necklace neutral at midleft with moveinleft

"Rowan watched as his wife accepted the plans for the dwarf, smiling graciously. At first, she was slightly confused at the technical drawings - not something he could blame her for - until Skordred laid down the basics."

al "... You’re not honestly planning to keep the kids underground? And right under the barracks?"

sk "The twins’ heirs are going to be the castle’s most precious treasure. They must be well protected."

ro "They are bound to be prime targets for all kinds of assassins and troublemakers."

#skor shocked
show alexia 2 necklace angry at midleft with dissolve

al "But that doesn’t mean you can just lock them in some dark, mossy vault! The kids will need fresh air! And Sun!"

#skor neutral
show alexia 2 necklace neutral at midleft with dissolve

al "And constant attention. We probably want somewhere Jezera wouldn’t complain about when passing through to see her kids."

show rowan necklace happy at midright with dissolve
show skordred angry at center with dissolve
show alexia 2 necklace angry at midleft with dissolve

"Rowan coughed violently, trying to conceal his laughter. Somehow, he managed to earn disapproving glances from not only Skordred, but his wife as well."

show rowan necklace neutral at midright with dissolve
show skordred neutral at center with dissolve
show alexia 2 necklace neutral at midleft with dissolve

ro "I apologize. I just… Find it hard to imagine Jezera as a mother. I mean…"

"He made a vague motion with his hand. It was hard to mention just one thing, from the controlling attitude, to the borderline sadistic personality."

al "She might be a bit of a strict parent, but we can’t be one hundred certain she’d be a bad one."

show alexia 2 necklace happy at midleft with dissolve

al "Motherhood is a wonderful thing. It’s one thing to conquer the world, another to bring life into it."

show alexia 2 necklace angry at midleft with dissolve

ro "If you say so. Now, about the nursery..."

scene black with fade

"He thought to argue, but knew better than that. Instead, he had them all study the map again, in yet another attempt to find a perfect spot for the future nursery."  
"In the end, they settled on a small room in the northern side of the castle, on the second floor."

scene bg20 with fade
show skordred neutral at center with dissolve
show rowan necklace neutral at midright with dissolve
show alexia 2 necklace happy at midleft with dissolve

"Skordred hummed for a long half a minute as he considered it, then finally gave the idea his blessings. "

sk "Aye, that will work… And it’s close to yer room as well, if you two ever decide on having kids yerself."

show rowan necklace concerned at midright with dissolve

if serveChoice == 4:
    "The thought made him shiver. The whole project was still in its infancy. If the protheans ever discover his involvement- "
else:
    "The thought made him shiver. The amount of control the twins would have over them- "

show rowan necklace shock at midright with dissolve

al "We’ve been trying for eight years and running, so… Here’s to hoping!"

show rowan necklace neutral at midright with dissolve
show skordred happy at center with dissolve

sk "Ah, that’s unfortunate. Once the nursery is ready, ya should bring the subject up with Jezera, or that pissy lackey of hers. Maybe they got some magic that can help ya here."

al "I’ll keep that in mind Skordred, thank you. "

show alexia 2 necklace shocked at midleft with dissolve

sk "Thank ya! Can ya believe Cla-Min wanted a “consultation fee” fer this?"

show skordred angry at center with dissolve
show alexia 2 necklace happy at midleft with dissolve

sk "Turns the castle into her personal pit stop, then still asks fer more? The nerve on that woman!"

show skordred neutral at center with dissolve

sk "I’ll run this through the masters Rowan. Let’s meet again in an hour or so."

ro "… Of course."

hide skordred with moveoutright

"The dwarf hurried out of the room, clutching the plans. Alexia chuckled, and beamed at her husband."

al "I wasn’t aware I could charge for this! No wonder Cla-Min is the one running the caravans."

if avatar.corruption < 31:
    show rowan necklace concerned at midright with dissolve
else:
    show rowan necklace angry at midright with dissolve
    
ro "Alexia…" 

show rowan necklace shock at midright with dissolve

al "I know."

show rowan necklace neutral at midright with dissolve

"She cut him short. She was no longer looking at him - rather through him, staring into the distance with that sad smile he saw on her face from time to time."

al "It’s just harmless talk. I know what a disaster it would be for us to have a baby right now. You don’t need to tell me."

show alexia 2 necklace neutral at midleft with dissolve

al "But I don’t think we have to worry about it. After eight years, I’m not exactly keeping my hopes up."

show alexia 2 necklace happy at midleft with dissolve

al "It’s just.. Nice to fantasize, sometimes. At what could be."

menu:
    "Hold her. She needs to be strong.":
        $ released_fix_rollback()
        show rowan necklace concerned at midright with dissolve
        show alexia 2 necklace concerned at midleft with dissolve
        "He reached through the table, and held her hand reassuringly. Thrust into the whirlwind of events, he sometimes forgot just how much his wife had lost, and how long she had been in the castle."
        ro "… It won’t always be like this. But we have to focus on what’s important at the moment."
        show alexia 2 necklace happy at midleft with dissolve
        al "Of course." 
        "They stayed like that for a while. A moment later she started to pull away. Her sad smile didn’t change one bit."
        al "Maybe next year."
        ro "Maybe next year."
        show rowan necklace neutral at midright with dissolve
        show alexia 2 necklace neutral at midleft with dissolve
        al " Don’t let me keep you Rowan, I know you have a lot of work. Just don’t stay late, alright?"
        ro "I won’t. I promise."
        hide alexia with moveoutleft
        "She gave him a quick kiss on the cheek, then hurried out of the room without another word."
        
    "They have no room for pointless fantasies. She must be strong.":
        $ released_fix_rollback()
        $ change_base_stat('c', 2)
        show rowan necklace neutral at midright with dissolve
        show alexia 2 necklace neutral at midleft with dissolve
        "He gave her a slow nod, and started to sort through all the scattered plans."
        ro "As long as it’s just fantasies. There are other things we must focus on right now."
        al "Of course."
        al "Don’t stay long, alright?"
        ro "I won’t."
        hide alexia with moveoutleft
        "Her faraway gaze didn’t change one bit. Still holding that sad smile, she hurried out of the room without another word."
        
scene black with fade

"..."

scene bg14 with fade
show alexia 2 necklace concerned at midleft with dissolve

"Alexia walked through the corridor briskly, trying to ignore the aching in her heart." 
"Rowan Blackwell, the most talented tracker in all Six Kingdoms. Sometimes blind as a bat. Most agonizingly often - when it came to her."

#If Rowan claimed Helayna, and she’s still in his room AND alexia and helayna haven’t resolve their differences yet. -TODO
    #show alexia 2 necklace neutral at midleft with dissolve
    #"She had to congratulate herself on her self-restraint. Thrice, she wanted to ask Rowan if he wouldn’t want to discuss this with Helayna instead."
    #show alexia 2 necklace angry at midleft with dissolve
    #"But Helayna was to be “saved”, and fucked. She was the one everyone expected to keep a stiff upper lip and keep playing the obedient wife."
    
"As if it wasn’t bad enough that the goblin whore kept flaunting her tits, hips and kids around him…"

show alexia 2 necklace neutral at midleft with dissolve

"It was always like that. Rowan… Simply didn’t care. Even back at Arthdale. Oh, she can’t say he hasn’t tried. But whenever she tried to bring up the topic of kids, the discussion always just… Petered out."

show alexia 2 necklace angry at midleft with dissolve

"She was always the one making the effort. Always talking to the village wise women, always consulting the abbots, always checking with the traders, to see if they’re carrying some herbs that might help. Year after another."

show alexia 2 necklace concerned at midleft with dissolve

"All for naught."

show alexia 2 necklace shocked at midright with moveoutright
show orc soldier neutral at midleft with moveinleft
show wild orc neutral at edgeleft with moveinleft

if castle.morale > 50 or all_actors["alexia"].flags["andras_influence"] > 3:
    os "Lady Blackwell."
    hide orc soldier with moveoutright
    hide wild orc with moveoutright
    show alexia 2 necklace happy at center with moveinleft
    "A contingent of orcs went through, bowing their heads to her. She smiled nervously, pressing herself against the castle wall to give them some room."
    show alexia 2 necklace concerned at center with dissolve

else:
    os "Move it, ya slut."
    hide orc soldier with moveoutright
    hide wild orc with moveoutright
    show alexia 2 necklace concerned at center with moveinleft
    "A contingent of orcs went through, pushing her to the wall. She stifled a yelp, and pressed herself against it."
    
"Her hand went to her chest, and she brushed the blue amulet hanging from her neck. Year after year, all for naught. And now… Now she was here."

show alexia 2 necklace happy at center with dissolve

al "… “There’s always time”, no?"

"That’s what she used to tell herself. There’s still time. There’s no reason to hurry." 
"She laughed, and wiped away the tears. There was always time. Until there wasn’t." 

if NTR == False:
    jump consultationRetire
    
else:
    pass
    
menu:
    "Check the nursery site.":
        $ released_fix_rollback()
        scene black with fade
        "She wasn’t sure what masochistic need made her turn her steps to the nursery site. But she did regardless, paying no mind to the castle staff she passed by."
        jump consulationAndrasMeeting
         
    
    "Retire for the evening. She's tortured herself enough.":
        $ released_fix_rollback()
        jump consultationRetire

label consulationAndrasMeeting:

scene bg14 with fade
show alexia 2 necklace neutral at center with moveinleft
show andras happy behind bg14

"Compromises. That’s how the location was picked. It was a small, currently unused room, full of old furniture. Far away from the orcs, far away from all the action, with only a single corridor leading to it." 
"Close enough to reach the battlements and the castle courtyard in times of peace. Remote enough to prevent potential assassins wandering about in disguise. And nearby both of the twins' rooms, in case they wanted to drop by. "
"She had to agree with Rowan - that didn’t seem probable."

an "Making plans, Alexia? "

hide andras

show alexia 2 necklace angry at midleft with moveoutleft
show andras happy at midright with dissolve

al "What is it with people sneaking up on me today! I am not in the mood!"

an "And here I was under the impression that an unexpected surprise is exactly what you’re hoping for."

show andras smirk at midright with dissolve

"Like a hawk, Andras circled around her, his eyes shamelessly wandering from her belly to her chest. She scoffed in response."

show andras happy at midright with dissolve

al "I didn’t take Skordred for a tattletale."

an "Rightly so. But the castle is the only child he will ever have, so he lacks certain... Sensibilities."

show alexia 2 necklace neutral at midleft with dissolve

al " I see. And what’s your excuse?"

an "I don’t give a shit what people think."

#generic room BG

"He walked into the room, pushing past her. He ran his fingers over the dusty surface of one of the tables, then shook his hand."

show andras displeased at midright with dissolve

an "Charming. Then I suppose I should redouble my effort in making sure it’s full of screaming kids?"

al "If you want. But this place is nowhere near ready." 

show andras happy at midright with dissolve

an "No, it’s not. But why wait?"

"He ordered her to walk inside, and she followed, suddenly unsure of herself at the sight of his smile."

an "Planning… Preparing… Ha! Pointless bullshit! All that needlessly convoluted crap is my sister’s domain."

show andras smirk at midright with dissolve

an "I don’t wait. I take what I want!"

show alexia 2 necklace concerned at midleft with dissolve

al "You had no trouble playing the gentleman captor when you first brought me here."

an "Because I wanted you. And I wanted you willing." 

show andras smirk at center with moveinright

if all_actors["alexia"].flags["andras_influence"] > 0:
    show alexia 2 necklace aroused at midleft with dissolve
    "He grabbed her by the chin, and made her look into his eyes as he came near. She felt his hot breath on her skin - or was she getting warm for some other reason?"

else:
    show alexia 2 necklace neutral at midleft with dissolve        
    "He grabbed her by the chin, and made her look into his eyes as he came near. She stood unmoved, meeting his gaze defiantly."

an "When I {b}want{/b} something, I work for it tirelessly, without rest, and without restraint."

show alexia 2 necklace concerned at midleft with dissolve

al "It always has to be about you, doesn’t it?"

show alexia 2 necklace shocked at midleft with dissolve
show andras smirk at midright with moveoutright

"And just like that - he let her go, taking a step back, arms wide. "

an "Ha! You’re right, how awfully inconsiderate of me!"

show alexia 2 necklace concerned at midleft with dissolve

an "Then let’s make it about you. About what you want. About what you desire."

al "I don't-"

show andras angry at midright with dissolve
show bg14 with sshake
show alexia 2 necklace shocked at midleft with dissolve

an "{b}NO!{/b}"
an "Enough of that! You sound just like your husband! “Don’t do that”! “It’s not right”! “Stop and think for a moment”!"
an "Always waiting, always questioning, always hesitating! "
an "Humour me here: for once in your life, at least {b}say{/b} what you want!"

show andras smirk at midright with dissolve

"She didn’t know if she was more insulted or hurt when he pointed his finger at her accusingly. In Andras’ world, everything was always so simple. How it must have felt, to be a part of it…"

menu:
    "Say what you want.":
        $ released_fix_rollback()
        $ change_actor_num_flag('alexia', 'andras_influence', 1)
        pass
        
    "Rebuke him.":
        $ released_fix_rollback()
        $ consultationAndrasRebuke = True
        show alexia 2 necklace neutral at midleft with dissolve
        show andras displeased at midright with dissolve
        al "… What a convenient, cozy outlook. Take what you want, and to hell with the consequences."
        al "But it’s not all about what I, or even what my husband wants. It’s about both of us."
        al "But you wouldn’t understand."
        al "Good night to you, Lord Andras. I hope you the best of luck on your future “conquests”, in the castle and outside of it."
        hide alexia with moveoutleft
        "She saw the rage enter his eyes. She turned on her heels, and rushed out of the room before she found herself on the receiving end of it."
        return

al "I..."
al "I want to have kids."

an "What’s that? I didn’t hear you!"

show alexia 2 necklace neutral at midleft with dissolve

al "I want to have kids!"
al "I- I’m a healthy woman in my prime, and I want to have kids! And it’s not wrong, or unreasonable, or selfish of me! "

an "But it is selfish!"

hide andras
show andras smirk at midright with dissolve
show andras smirk at midleft with moveoutleft
hide alexia
show alexia 2 necklace aroused at midleft with dissolve
show alexia 2 necklace aroused at center with moveinleft


"Like a snake, he was suddenly right next to her, his hand on her hips, whispering into her ear."

an "It’s what you want, not what Rowan wants! If he did, he’d do something about it!"
an "And do you still want it?"

menu:
    "Yes.":
        $ released_fix_rollback()
        $ consultationAndrasAgree = True
        $ change_corruption_actor('alexia', 2)
        show alexia 2 necklace neutral at center with dissolve
        al "… Yes. Even if it is selfish."
        al "I have the right to be selfish from time to time."
        al "And Rowan would be a good father."
        an "He’s been a lousy husband so far."
        show alexia 2 necklace aroused at center with dissolve
        "His hand felt like burning iron. Why has she not yet pushed it away?"
        an "And he doesn’t have to be the father."
        "Something hard pressed against her backside-"
        show alexia 2 necklace aroused at midright with moveoutright
        "She jumped away, instantly. Holding her hands to her chest like an invisible shield, she watched Andras grin at her. He spread his arms open wide."
        show andras happy at center with moveinleft
        an "If it were up to me, this place would hold nothing but your kids, Alexia." 
        show alexia 2 necklace neutral at midright with dissolve
        al "You are woefully misinterpreting my words."
        an "Maybe. Just remember - my doors are always open."
        an "Think about it."
        hide andras with moveoutleft
        "And he left just like that, leaving her alone in an empty room that one day might house their children. Hers and Rowans. Andras’ and…"
        scene black with fade
        "… She wasn’t sure."
        return
        
    "Maybe.":
        $ released_fix_rollback()
        $ consultationAndrasUncertain = True
        show alexia 2 necklace aroused at midright with moveoutright
        "Still flushed, she pushed herself away from him, stumbling in her steps."
        al "I-"
        show alexia 2 necklace concerned at midright with dissolve
        al "You’re just doing this to mess with me!"
        an "To the contrary. I am hoping to clear your mind."
        al "Well you’re not being very good at it!"
        an "Neither is Rowan at getting you pregnant, but at least I try."
        show alexia 2 necklace aroused at midright with dissolve
        an "And I will always keep trying."
        show alexia 2 necklace neutral at midright with dissolve
        "He spread his arms open wide."
        an "Remember, you ever want to double your chances -  my doors are always open."
        hide andras with moveoutleft
        "And he left just like that, leaving her alone in an empty room that one day might house their children."
        scene black with fade
        "… Might."
        return


label consultationRetire:

al "(Ha… And Jezera always jokes Rowan is the masochistic one.) "

hide alexia with moveoutright

"Shaking her head, she turned her steps back to her room. She had to make herself presentable in case Rowan did end up early… For a change. "

scene black with fade

"And maybe this night they will have the misfortune of being lucky."

return

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

label alexia_potion_stealing:

$ alexiaPotionStolen = True

scene bg12 with fade
show alexia 2 necklace concerned at center with dissolve

"Again, her husband was busy, with some castle business nobody saw fit to inform her of. She didn’t complain. She understood."

if alexiaSeparateRoom:
    "At least he wasn’t with Helayna. Such a strange thought to draw comfort from… "
    

show alexia 2 necklace neutral at center with dissolve

"With nothing left to do, she decided to spend her afternoon in the castle library, browsing books. She was checking “Herbs of the western coast” by some man whose name she couldn’t read, when a polite cough interrupted her."

show alexia 2 necklace neutral at midleft with moveoutleft
show nasim neutral at midright with moveinright

nas "Lady Blackwell, if you’re not using it for anything important, I’m afraid I will have to request Master Laram’s catalogue."

show alexia 2 necklace happy at midleft with dissolve

al "I was only checking it. Here."

"The man accepted the book with a respectful nod, and was quick to leave. She had seen him before… But couldn’t put a name to the face. "

show alexia 2 necklace neutral at midleft with dissolve

al "Excuse me, but I don’t think we’ve ever been properly introduced. Alexia Blackwell."

show nasim happy at midright with dissolve

nas "Researcher Nasim. A pleasure." 

"He slowed his pace just enough for her to catch up, if only because manners demanded so. It wasn’t the first time she was given a cold shoulder in the castle, and she would hardly let herself be bothered by it."

if alexiaAndrasObedient == True:
    "If he’s too unpleasant, she can always complain to Andras. See how long that aloof attitude of his manages to hold when Andras rips him a new one. "

show alexia 2 necklace happy at midleft with dissolve

al "Is herbology something you specialize in, Researcher Nasim?" 

show nasim neutral at midright with dissolve

nas "I possess some expertise, but to my great regret I cannot yet claim mastery in that particular field."

show nasim angry at midright with dissolve

nas "… This is, sadly, why I must rely on Master Laram’s work. If one looks past the elven revanchism, his insight into the wild fauna of the western wastes is quite invaluable."

show nasim neutral at midright with dissolve

al "The western wastes… I can’t say I know much about the region. How “wild” are we talking here?"

show nasim happy at midright with dissolve

nas "Quite wild."

"The man sent her a knowing smirk, paying no mind to Alexia following him into his study. Was he *that* enamoured in his own voice?"

show nasim neutral at midright with dissolve

nas "That particular area tends to avoid the inevitable Solansian counterattacks that follow each demonic invasion, which have, more or less, ensured the Rackshan waste will never be anything but a wasteland."

show alexia 2 necklace shocked at midleft with dissolve

"Alexia snuck a curious glance at Nasim’s room. Instantly, she was struck by how impersonal and barren it felt. If she didn’t know better, she’d swore the man moved here last week."

show alexia 2 necklace neutral at midleft with dissolve

nas "In the western regions nature is free to flourish, to the point where it can sustain life. Because of that, the area often harbours some of the more isolationist of the chaos races. Orcs more often than not."

"The second thing that struck her was Nasim’s desk, and the pitch-black potion occupying the centre of it. It was half empty, and surrounded by notes and vials with various fluids she couldn’t recognize."

nas "And while one could be excused for thinking orcs as mere fodder, I must admit tribes who have remained in Solansian for a long time can exhibit most fascinating cultures."

show nasim happy at midright with dissolve

nas "Take, for example, the “Ugrak-ic”."

"The man approached his desk, and tapped the potion lightly. The black surface {i}wobbled{/i}, the liquid inside impossibly dense, and a black bubble rose to the surface."

show alexia 2 necklace concerned at midleft with dissolve

"She almost shivered when she saw the vile thing *pop*. Nothing of that colour or consistency could be any good, for anyone."

show alexia 2 necklace neutral at midleft with dissolve
show nasim neutral at midright with dissolve

nas "The “Ugrak-ic”, like most orcs, believe that physical might is the sole prerequisite of leadership. But unlike most orcs, they don’t prove it in combat."
nas "Instead, the females seek out the most physically intimidating specimens of other races, sometimes venturing hundreds of miles to find them and, well, “copulate” with them.  "
nas "What we have here is the “Korot-Baru”. A sacred potion of the tribe, whose name roughly translates to “Devourer of reason, dawn of apocalypse.”"

show alexia 2 necklace shocked at midleft with dissolve

nas "A rather pompous title for an orc fertility potion, but the demonkind and their descendants aren’t exactly known for their restraint, naming conventions included."   

show alexia 2 necklace neutral at midleft with dissolve

"Alexia watched the potion go “pop!” again. If Nasim was not busy browsing through the book and taking notes, he might have noticed the shift in her voice."

al "… Does it work?"

nas "I have yet to perform a test on a live sample, but I see no reason why it should not. The ingredients are mostly herbs known to boost fertility."
nas "Though, of course, the real magic is in the ritual that finalizes the brewing process."

"To him, it was obvious. To her… She could hardly care for the fine details involved."

al "I’m surprised the orcs even need such potions. "

show alexia 2 necklace happy at midleft with dissolve

"In a way, it was almost reassuring-"

show alexia 2 necklace neutral at midleft with dissolve

nas "They don’t, not usually. The “Korot-Baru” is brewed specifically for the purpose of the “hunt”, as orcs are notoriously difficult to interbreed with, with half-orcs being born on average only once every five hundred intercourses."
nas "A statistic brought to us by the downfall of Fortress Jarandal. May Solansia guard the souls of its garrison for all eternity. "

al "O-of course. May Solansia guard their souls."

"He didn’t even notice her stammer. For once, she was grateful for how irrelevant she was to some people in the castle." 
"But before she could ask any more questions, Nasim stood up, checking his collection for something, and being clearly dissatisfied with what he had found."  

show nasim angry at midright with dissolve

nas "Why must chaos script be so difficult to work with… Someone needs to introduce it to a proper syntax."

show nasim happy at midright with dissolve
show alexia 2 necklace happy at midleft with dissolve

nas "A project for next year, perhaps. You must excuse me now, [alexia title] Blackwell. There’s still work to be done. I could send you the notes once they’re finished, if the topic interests you?"

show alexia 2 necklace neutral at midleft with dissolve
show nasim neutral at midright with dissolve

al "I would appreciate it, but I fear I might not be able to make heads or tails of it."

"She left his room before he thought to lead her out, and Nasim closed the door behind them."

show alexia 2 necklace happy at midleft with dissolve

nas "If that is a concern, then I would suggest starting with “The Crimson Mark.” It’s more of a journal than a guide to botany, which makes it quite accessible to beginning alchemists."

show alexia 2 necklace concerned at midleft with dissolve

nas "Banned in every civilized realm south of here. Goes into slightly too much detail about practical applications of human blood in soil cultivation. But a great read nonetheless."

al "… I’ll look into it? "

show nasim happy at midright with dissolve
show alexia 2 necklace happy at midleft with dissolve

nas "You should. Have a good day [alexia title] Blackwell. It’s been a pleasure."
al "Thank you. Good luck on your work, Researcher Nasim. "

hide nasim with moveoutright
show alexia 2 necklace happy at center with moveinleft

"The man offered her a polite smile, and ventured into the library again."

show alexia 2 necklace neutral at center with dissolve

"Behind her, his study waited." 
"He didn’t lock it."

menu:
    "Steal the potion.":
        $ released_fix_rollback()
        hide alexia with moveoutright
        "She didn’t wait. The moment he left her sight, she turned around, and casually strolled back into his room."
        "The “Korot-Baru” beaconed. The pitch-black remedy for her woes."
        scene black with fade
        "She hid it under her skirt, and was gone from the library before anyone noticed."
        jump rowansHeadache
        
    "Hesitate. ":
        $ released_fix_rollback()
        "Her hand trembled, and she found herself rooted to the floor. Behind her laid what could be the remedy to her woes." 
        "She didn’t have to drink it now. She could hide it, take it with her once all that Bloodmeen business is done for. Find an alchemist to see if it was safe." 
        if alexiaAndrasObedient == True:
            "Nasim might notice, but if so, then what? Nobody could touch her. Not as long as Andras was Master of Castle Bloodmeen. And he would always be Master of Castle Bloodmeen."
        elif alexiaJezObedient == True:
            "They wouldn’t catch her. And if they did, she could lie herself out of it. Men were easy to manipulate."
        else:
            "Nasim might notice, but if so, then what? She was the chain that bound Rowan to the twins. She couldn’t be hurt, couldn’t be disposed of."
        "She could take it. It was now or never."
        menu:
            "Steal the potion.":
                $ released_fix_rollback()
                scene black with fade
                "… A moment later, she was walking out of Nasim’s room with the pitch black potion under her skirt." 
                "She was gone out of the library before anyone noticed." 
                jump rowansHeadache
            "Abandon your dreams of children.":
                $ released_fix_rollback()
                show alexia 2 necklace concerned at center with dissolve
                "… She didn’t move. One of Cliohna’s assistant passed her by, and she greeted him with a distant smile." 
                "Slowly, she turned her steps away from Nasim’s room. There was just one reason to take the potion, and a million not to. She didn’t know which one to focus on. She wasn’t sure if she wanted to anyway." 
                "So for once, she took a page out of her husband’s book."
                scene black with fade
                "And choose not to think about it anymore."
                show alexia 2 necklace concerned behind black
                al "…  Maybe next year."
                $ abandondedPregnancyAspirations = True
                return

label rowansHeadache:

"..."

scene bg6 with fade
show rowan necklace concerned at midright with dissolve

"Rowan rubbed his eyes, trying, with no success, to fight off his exhaustion. The day couldn’t get any worse."

show nasim neutral at midleft with dissolve

if nasimAttitude >= 0:
    ro "Nasim, please tell me you come with an unexpected yet ultimately positive breakthrough, that will help alleviate literally any of the thousand issues that plague this castle."
    nas ".. I wish I could."
    ro "Is something the matter?"
    
else:
    show rowan necklace angry at midright with dissolve
    ro "Ah, of course."
    ro "Nasim, I am not in the mood for your complaining."
    nas "And neither am I for having this conversation. And yet here we are."
    
#if transchamber built
    #show rowan necklace neutral at midright with dissolve
    #nas "After excavating the transformation chamber, I had hoped our future cooperation would proceed smoothly. I am most disappointed that is not the case. "

#else:
show rowan necklace neutral at midright with dissolve
nas "I had hoped that even though you continue to delay excavating the transformation chamber, you would at the very least allow me to continue my other research undisturbed."

ro "Nasim, what are you talking about?"

show nasim angry at midleft with dissolve

nas "I am speaking of the “Korot-Baru”, of course."

"Nasim held his chin high. His eyes narrowed and he threw the hero of the six realms a most withering look."
"Said hero opened his arms, absolutely confounded."

#show nasim shocked at midleft with dissolve

ro "What?"

nas "..."

show nasim neutral at midleft with dissolve

nas "Give me a moment while I consider the possibility that you might not have ordered your wife to spy on me and sabotage my research."

if nasimAttitude >= 0:
    ro "Nasim, with all due respect, your projects can’t be nearly half as dangerous as what Andras and Jezera do on a daily basis."
    show nasim happy at midleft with dissolve
    nas "You wound me, Rowan."
    show nasim neutral at midleft with dissolve
    nas "… But I must confess it would be out of character for you to go after me, of all the people in the castle."
    ro "I hope you don’t mind not being at the top of the list for a change."
    nas "I am more than comfortable in feigning mediocrity when it serves my purposes, but assuming you are being honest, this is not the time for idle talk. I’ll try to keep it brief. "

else:
    show rowan necklace angry at midright with dissolve
    ro "Nasim, you really need to get that massive ego of yours checked."
    nas "And you should keep your wife on a shorter leash, Master Blackwell." 
    nas "But perhaps we have both miscalculated our importance in the eyes of others."
    nas "I’ll give you the benefit of the doubt, and try to keep it brief."
    
scene black with fade

"Word after word, in the quiet of Rowan’s study, the hero has learned of all that transpired in the library earlier that day."

scene bg6 with fade
show rowan necklace concerned at midright with dissolve
show nasim neutral at midleft with dissolve

"He hid his face in his hands, trying not to groan."

show rowan necklace angry at midright with dissolve

ro "… Why did you even tell her about this… “Korot-Baru”?"

nas "Why would I not? Regardless of one’s circumstances, Castle Bloodmeen continues to be a treasure vault of knowledge one would never find elsewhere."
nas "It would be a crime to make no use of it. Lady Blackwell ought to be commended for her open-mindedness."
nas "... Once the “Korot-Baru” is retrieved."

show rowan necklace neutral at midright with dissolve

ro "So you can continue your research."

nas "Also, but primarily, so Lady Blackwell does not think to use it. "

show rowan necklace shock at midright with dissolve

nas "The potion has a long list of side effects, and has never been tested on non-orcs. Should she drink it, the effects might be… Highly unpredictable. Potentially deadly."

if nasimAttitude >= 0:
    show rowan necklace concerned at midright with dissolve
    nas "You know I hold no ill will towards you or your wife, Rowan. Even if this wasn’t about my research, I would advise you to retrieve it at haste."
    show rowan necklace neutral at edgeleft with moveoutleft
    "He was halfway through the room before the man finished his last sentence. Nasim might have been unpleasant at times, but he was never unreliable."
    ro "I’ll handle this. And thank you, Nasim."
    hide rowan with moveoutleft
    "The man lowered his head politely, and Rowan patted him on the shoulder. Not wishing to waste even a moment, he headed for Alexia."
    
else:
    show rowan necklace angry at midright with dissolve
    nas "For Lady Blackwell to come to harm because of a potion I brought to this castle… Would be an unwelcome complication." 
    "His blood turned to ice. Slowly, he stood up from behind his deck."
    show rowan necklace angry at center with moveinright
    ro "Perhaps next time, you’ll make sure your potentially lethal potions are kept in a more secure location."
    show nasim angry at midleft with dissolve
    nas "I will, if only to avoid further thievery."
    nas "And perhaps you should consider making sure this situation does not repeat on your end either. A stern talk with your wife, at least?"
    ro "Duly noted, Researcher Nasim. Now get the fuck out of my way before you piss me off further."
    hide rowan with moveoutleft
    "The man bowed his head politely, and moved aside as Rowan stormed out of the room."
    
scene bg14 with fade
show rowan necklace angry at center with moveinright

ro "Unbelievable."

if all_actors["alexia"].relation < 31:
    if avatar.corruption > 30:
        "His fury rose with every step. Alexia had one job, one fucking job - to not make his life any more difficult than it was."
    else:
        "He tried to keep his anger in check. Things haven’t been ideal between them lately, so all he wanted - all he expected - was for her to not make his life any more difficult than it already was."
        
else:
    if avatar.corruption > 30:
        "His anger rose with every step. Alexia had one job - to be strong, and not make his life any more difficult than it already was."
    else:
        "He knew she had it difficult, he really did. So he wasn’t expecting much of her: simply to be strong, and not cause him any trouble."
        
"Apparently he was expecting too much."

if alexiaSeparateRoom:
    "He stopped in front of her room, trying to force his emotions in check. Partially succeeding, he knocked on the door and invited himself in."
    scene bg7 with fade
    
else:
    "He stopped in front of their room, trying to force his emotions in check. Partially succeeding, he knocked on the door and invited himself in."
    scene bg9 with fade
    
show alexia 2 necklace neutral at midright with dissolve
show rowan necklace angry at midleft with moveinleft

ro "Alexia, do you have a moment?"

if alexiaJezObedient == True:
    show alexia 2 necklace happy at midright with dissolve
    al "Always, dear. Did something happen?"
    ro "We have to talk. About Nasim’s potion."
    show alexia 2 necklace shocked at midright with dissolve
    show rowan necklace shock at midleft with dissolve
    al "What potion?"
    "“What potion?” And spoken with such genuine surprise!"
    show alexia 2 necklace neutral at midright with dissolve
    show rowan necklace angry at midleft with dissolve
    "It {i}almost{/i} made him wonder if Nasim wasn’t setting him up. But for all of the man’s fault… An easily disproved lie like that didn’t seem his style." 
    ro "The fertility potion. The one that’s missing."
    al "Was it stolen?"
    show rowan necklace shock at midleft with dissolve
    al "Maybe it’s one the library mages hoping to further his position? Or maybe one of Cla-Min’s brood wanted to punish him for not acquiring it through them?"
    show rowan necklace angry at midleft with dissolve
    "She tapped her cheek, as if in deep thought."
    al "Could also be one of the castle’s mercenaries. These people hold no allegiance to anyone."
    show alexia 2 necklace happy at midright with dissolve
    al "It’s okay if you have to spend the evening interrogating them. I’ll understand."
    show rowan necklace concerned at midleft with dissolve
    ro "..."
    ro "Alexia … It’s not like you to point fingers at others so quickly."
    ro "Are you sure there’s nothing you want to tell me?"
    show rowan necklace angry at midleft with dissolve
    "He narrowed his eyes at her. She gave him the most serene, honest smile he had ever seen."
    show alexia 2 necklace concerned at midright with dissolve
    show rowan necklace concerned at midleft with dissolve
    "… … … … … It broke, and she looked away."
    show rowan necklace angry at midleft with dissolve
    ro "Unbelievable."
    al "… I am not giving it back."
    "He blinked, unsure if he heard her right. Gone was the fake, pleasant smile. In its place, laid grim determination he had only ever seen in soldiers ready to face death."
    jump potionArgument
    
elif alexiaAndrasObedient == True:
    al "Yes, Rowan?"
    "She didn’t even turn to look at him. She was looking through the window, with her hands on her knees."
    ro "We have to talk. About Nasim’s potion."
    ro "Did you take it?"
    show rowan necklace angry at center with moveinleft
    "She didn’t answer him, not at first. He walked up, and grabbed her by the shoulder-"
    show rowan necklace shock at midleft with moveoutleft
    show alexia 2 necklace angry at midright with dissolve
    "She pushed his hand away, and looked up, a defiant look in her eyes."
    al "And what if I did?"
    show rowan necklace neutral at midleft with dissolve
    ro "That’s-"
    al " Tell that wizard to man up and get himself a new one. Andras changes orcs all the time, he can replace one lousy potion!"
    al "Because I am not giving it back!"
    "He didn’t know how to react to the sudden outburst. It cooled a moment later - only to be replaced by a steeled look of grim determination."
    jump potionArgument
    
else:
    show alexia 2 necklace happy at midright with dissolve
    show rowan necklace neutral at midleft with dissolve
    al "Always, dear. Did something happen?"
    show alexia 2 necklace concerned at midright with dissolve
    ro "We have to talk. About Nasim’s potion."
    al "Ah."
    al "I suppose I shouldn’t be surprised. I haven’t been exactly subtle about taking it."
    ro "No. Not really."
    show alexia 2 necklace neutral at midright with dissolve
    show rowan necklace shock at midleft with dissolve
    al "… But I’m not giving it back."
    "He blinked, unsure if he heard her right. Her sad expression gave way to a determined one, and she continued, her voice sad, but steady."
    jump potionArgument

label potionArgument:

show alexia 2 necklace neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve

al "You don’t have to worry, I have no intention of using it right now."

if consultationAndrasAgree:
    al "Even though part of me really wants to."
    
elif consultationAndrasRebuke:
    al "And most certainly not without discussing it with you first."
    
else:
    pass

al "But I do intend to keep it."

ro "Alexia-"

show alexia 2 necklace angry at midright with dissolve

al " I know. Whatever it is you want to say, I know."

"She tugged at the amulet at her neck, scowling."

al "I know this is not the right time, and I know we have the twins to worry about, and I know you have to look after everything in the castle, and I know your weekly endeavours into Rosaria aren’t exactly recreational visits."
al "{b}I know{/b}. I know all of this."  

show alexia 2 necklace concerned at midright with dissolve

al "But Rowan, I…"

show rowan necklace concerned at midleft with dissolve

al "... I’m miserable."

"She swallowed heavily and gave him another sad smile. Nowadays, they were all too common."

if all_actors["alexia"].relation > 30:
    al "Oh, don’t get me wrong, I’m glad that you’re here. Whatever the situation, having you by my side makes it all bearable."
    if all_actors["alexia"].corruption > 30:
        show alexia 2 necklace happy at midright with dissolve
        al "And even thought this castle isn’t as bad as I thought.... I’ve met people I would have never dreamed to met, and experienced things I would never risk to try otherwise..." 
        show alexia 2 necklace concerned at midright with dissolve
        al "This is not home."
    else:
        al "But this castle is a nightmare. Feels like even the walls themselves want to twist me into something I am not."
        al "Even a gilded cage would be difficult to live in for a year. This isn't even that."
        
else:
    al " I thought things would be better with you here. But more often than not, even when you are with me, it feels like you’re doing it simply out of necessity."
    if all_actors["alexia"].corruption > 30:
        al "At least this castle isn’t as bad as I thought.... I’ve met people I would have never dreamed to met, and experienced things I would never risk to try otherwise..."
        al "But still - this is not home."
    else:
        al "And this castle is a nightmare. Feels like even the walls themselves want to twist me into something I am not."
        al "So how could I not be miserable?"

show alexia 2 necklace neutral at midright with dissolve

al "… I had a life in Arthdale Rowan. And hope. Hope of having a family. Hope of giving you a son, or a daughter, and raising them with you. Hope of growing old together, and hope of maybe dying with you by my side."

show alexia 2 necklace happy at midright with dissolve

al "Now, at best, I can maybe hope for the last one."

"Several times, her voice was at the edge of breaking. Yet, she continued, holding back the tears. "

show alexia 2 necklace neutral at midright with dissolve

al "Rowan, I intend to keep the potion. Not to use it now. For later. For the day when we are finally free again. For the day when I can finally dream of having a future again. So that I can have any hope again."

show alexia 2 necklace angry at midright with dissolve
show rowan necklace shock at midleft with dissolve

al "… Or am I to give that away too?"

#and the two havent reconcilded - TODO
if alexiaSeparateRoom:
    show rowan necklace concerned at midleft with dissolve
    al "Just like I gave our marriage bed to another?" 

show rowan necklace neutral at midleft with dissolve

"She looked up, daring him to say she must."

if avatar.guilt > 30 or avatar.corruption > 60:
    "As if he hadn’t done worse things. "

menu:
    "Console her.":
        $ released_fix_rollback()
        show rowan necklace concerned at midleft with dissolve
        show alexia 2 necklace concerned at midright with dissolve
        "Before he even said anything, he knelt before his wife, and wrapped his arms around her, hugging her close to his chest."
        if alexiaAndrasObedient and all_actors["alexia"].relation < 30:
            "… She didn’t return the gesture."
        else:
            "A painfully long moment passed, until he finally felt her own arms around him, touching him lightly, shyly almost."
        "They stayed like that for a moment. Finally he kissed her on the head, and let her go."
        "He almost didn’t want to mention the potion again, but the elephant in the room had to be addressed."
        $ alexiaPotionConsoled = True
        $ change_relation('alexia', 3)
        jump alexiaPregnancyChoice
        
    "Just get to the point.":
        $ released_fix_rollback()
        jump alexiaPregnancyChoice
        
    "Scold her for stealing the potions.":
        $ released_fix_rollback() 
        $ alexiaScolded = True
        show rowan necklace angry at midleft with dissolve
        ro "That’s all you have to say for yourself?"
        show alexia 2 necklace shocked at midright with dissolve
        "He seized the amulet at her neck and yanked it up, forcing her to stare at the sparkling sapphire."
        ro "Do you {i}actually{/i} understand how precarious our situation is? Because apparently it’s not enough that the twins hold us by the throats, you want other people to have leverage over us as well!"
        show alexia 2 necklace concerned at midright with dissolve
        al "Nasim-"
        if nasimAttitude >= 0:
            ro "Nasim might not have horns, and he might be slightly more civil than the rest of the bunch. But it doesn’t change the fact he works for the twins, and does so willingly."
            ro "He’s out for himself. We must be too."
        else:
            ro "Nasim is a selfish, arrogant piece of crap who would rim Andras’ ass if it got him ahead."
            ro "Just because he doesn’t have horns doesn’t mean he’s not rotten to the core. Don’t be fooled by the fact he sometimes pretends to be civil."
        "He let go of the amulet, trying not to unload on his wife any further. How could she be this stupid?"
        ro "Don’t do it again. Think before you act, for crying out loud."
        if alexiaAndrasObedient:
            show alexia 2 necklace angry at midright with dissolve
            "If he thought her eyes held anger before, they were made from pure vitriol now. She said nothing, only waited for him to continue."
            show alexia 2 necklace neutral at midright with dissolve
        elif alexiaJezObedient:
            show alexia 2 necklace neutral at midright with dissolve
            al "… Of course. That’s good advice."
            "He couldn’t read her expression. First she lies to his face, now this?"
            "What was going on with her? He should start paying more attention to what she was doing when he was not in the castle. But first - the potion."
        else:
            show alexia 2 necklace neutral at midright with dissolve
            "She didn’t argue with him, only looked away. If it was to hide anger or pain, he couldn’t say."
        $ change_relation('alexia', -5)
        jump alexiaPregnancyChoice
        
label alexiaPregnancyChoice:

show alexia 2 necklace neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve

ro "Do you have the potion here?"

"Reluctantly, she nodded her head."

ro "… I’ll have to take it. It’s dangerous, Alexia. It might even kill you."

if all_actors["alexia"].relation < 30 and all_actors["alexia"].corruption < 31:
    show alexia 2 necklace happy at midright with dissolve
    al "What a shame would that be."
    if avatar.corruption < 31:
        show rowan necklace concerned at midleft with dissolve
        ro "Alexia, please…"
        show alexia 2 necklace neutral at midright with dissolve
        al "… That was in bad taste. I apologize."
        show rowan necklace neutral at midleft with dissolve
    
show alexia 2 necklace angry at midright with dissolve

al "How do you know it’s dangerous? From Nasim? What if he’s lying?"

ro "… I suppose that is possible. Does it look safe?"

show rowan necklace concerned at midleft with dissolve

al "..."

show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace concerned at midright with dissolve

al "I could find an alchemist first. Check it before I use it."

ro "I don’t think we’ll ever find anyone willing to want to touch anything that came out of Castle Bloodmeen. If they’ll even understood a thing about orc potions."

show alexia 2 necklace angry at midright with dissolve

al "Well, maybe I could take a sip first. Nobody said I have to drink all of it at once."

ro "That’s not how magical brews work. "

"She bit her lip. He pretended not to see the tears in her eyes."

show alexia 2 necklace concerned at midright with dissolve

al "Maybe I could water it down. Share it with someone."

ro "And hurt both of you. If the potion does not catch on fire the moment it touches water. I’ve seen them do that."

"… She didn’t argue further. She wanted to, he saw it in her eyes."

show rowan necklace concerned at midleft with dissolve

"She just didn’t know what to say."

al "… Damn you."

show rowan necklace neutral at midleft with dissolve
hide alexia with moveoutright

"She stood up, dragging her body as it was made of iron. She walked across the room, and knelt by one of the corners." 
"She pried one of the wooden planks open. Rowan didn’t know it could be removed." 

if all_actors["alexia"].corruption < 31:
    show alexia 2 necklace concerned at midright with moveinright
    "A moment later, his wife placed a black potion on the table in front of him, shoulders slumped."
else:
    show alexia 2 necklace neutral at midright with moveinright
    "A moment later, his wife placed a black potion on the table in front of him, expression unreadable."
    
show rowan necklace shock at midleft with dissolve

"He took it in his hands. The pitch-black liquid swirled lazily. It looked thick, unreasonably so - like a pool of tar."

show rowan necklace concerned at midleft with dissolve

"{i}This{/i} was what his wife put her faith into? Just how desperate was she?"

show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at midright with dissolve

al "… Is that all?"

menu:
    "Promise her to look into safer treatments.":
        $ released_fix_rollback()
        if alexiaScolded == True or all_actors["alexia"].relation < 30: 
            show rowan necklace concerned at midleft with dissolve
            "Every day, he felt the wall between them grow. Brick after brick, so high he almost couldn’t see it end. Greater than even the Bloodmeen walls."  
            "He couldn’t let this continue. And if it meant doing something stupid… Then so be it." 
            show rowan necklace neutral at midleft with dissolve
        "He grabbed her chin. She tried to avoid his gaze, but he forced her to look at him."
        if alexiaScolded == True:
            ro "Alexia, I… I’m sorry I shouted at you. It’s been-"
            show rowan necklace concerned at midleft with dissolve
            show alexia 2 necklace concerned at midright with dissolve
            ro "Gods damn it, this is my fault too. I should’ve paid more attention. Should’ve realized how important this was to you."
        else:
            if all_actors["alexia"].relation < 30:
                ro "Alexia, I’m sorry. I… I know I’ve been distant. And now…"
                show rowan necklace concerned at midleft with dissolve
                show alexia 2 necklace concerned at midright with dissolve
                ro "his is my fault too. I should’ve paid more attention. Should’ve realized how important this was to you."
            else:
                show rowan necklace concerned at midleft with dissolve
                show alexia 2 necklace concerned at midright with dissolve
                ro "Alexia, I’m sorry. I… I wasn’t aware how important this was to you."
        show alexia 2 necklace happy at midright with dissolve     
        al "… Blind as a bat."
        "She let out a humourless laugh. She didn’t seem surprised by his admission. And that just made him even more ashamed of himself."
        show alexia 2 necklace neutral at midright with dissolve
        al "Thank you. But it doesn’t matter anymore."
        show rowan necklace neutral at midleft with dissolve
        ro "It does."
        show alexia 2 necklace shocked at midright with dissolve
        ro "Alexia, I’ll find another way."
        al "… What?"
        ro "You heard me - I’ll find another way. We will be a family yet. I promise."
        ro "Nasim’s potion was dangerous, but maybe there are alternatives."
        show alexia 2 necklace happy at midright with dissolve  
        ro "I can try to pressure him or maybe appeal to his self-interest. Or try and get Cliohna to do me a favour, or-"
        show rowan necklace shock at midleft with dissolve
        "She threw herself at him, almost knocking him over. She sealed his lips with a desperate kiss, and he felt the tears running down her face."
        show rowan necklace happy at midleft with dissolve
        "He held her for as long as she needed it. And when she finally pulled away, and he saw the pain in her eyes - ah, Solansia, it was like a thousand needles in his heart." 
        show rowan necklace neutral at midleft with dissolve
        show alexia 2 necklace concerned at midright with dissolve
        al "Rowan, you shouldn’t."
        al "You were right. This is not the right time."
        ro "People waiting for the perfect moment often miss their only chance."
        ro "I should’ve done something years ago. But I can’t turn back time, so… I’ll see what I can do right now."
        al "What if we have to run away?"
        if serveChoice == 4:
            show rowan necklace happy at midleft with dissolve
            show alexia 2 necklace happy at midright with dissolve
            ro "I can have us evade both orcs and protheans. Never had trouble in misleading either."
        else:
            show rowan necklace happy at midleft with dissolve
            show alexia 2 necklace happy at midright with dissolve
            ro "Then I’ll just have to save us before your belly starts showing."
        ro "Besides, rescuing his pregnant wife would only add to the tale of Rowan Blackwell, no?"
        al "We could tell it to our kids once they’re older."
        ro "I would tell it every time we’d sat down by the fireplace. They’d be sick of it by the time they’re six."
        "She laughed, and hugged him again. She was right. It was nice to have something to look forward to. Even if it was just a fantasy."
        scene black with fade
        "… Now he would have to make sure it wouldn’t remain just that."
        $ promisedFertilityTreatment = True
        $ change_relation('alexia', 15)
        return
        
    "That’s all. You feel for her, but this really is not the right time.":
        $ released_fix_rollback()
        show rowan necklace concerned at midleft with dissolve
        ro "Alexia… You know I care for you, but-"
        al "But this is not the right time for kids. I know."
        if serveChoice == 4:
            ro "I don’t want to put them in danger too. I have to protect you first."
            al "I’d like to see some progress on that. But I suppose you can be content knowing you at least managed to protect your wife from herself."
        else:
            ro "I don’t want to put them in danger too. I have to save you first."
            al "I’d like to see some progress on that. But I suppose you can be content knowing you at least managed to protect your wife from herself."
        show alexia 2 necklace happy at midright with dissolve
        al "Congratulations are in order, Rowan. Good job."
        if alexiaScolded == True:
            show alexia 2 necklace neutral at midright with dissolve
            al "I’d like some time alone now, if you don’t mind."
        else:
            if all_actors["alexia"].relation < 30:
                show alexia 2 necklace neutral at midright with dissolve
                ro "… I’m sorry. For everything."
                al "I know you are."
                al "I’d like some time alone now, if you don’t mind."
            else:
                show alexia 2 necklace concerned at midright with dissolve
                ro "Please, don’t. I know you don’t mean it. And if it was anything else…"
                al "… You would do your best."
                show alexia 2 necklace happy at midright with dissolve
                al "Like you always do."
                show alexia 2 necklace neutral at midright with dissolve
                al "…. I think I’d like some time alone now, if you don’t mind."
        if alexiaPotionConsoled:
            "He hugged her close and kissed her on the head again. There was nothing he could say to make that pain any lesser.  He would have to make this up for her somehow."
            hide rowan with moveoutleft
            "Tomorrow, they would be back to acting as if nothing ever happened, but for now… "
        else:
            show rowan necklace concerned at edgeleft with moveoutleft
            "He took a step back, and watched her turn around as he headed for the door."
            hide rowan with moveoutleft
            "Tomorrow, they would be back to acting as if nothing ever happened, but for now… "
        scene black with fade
        if alexiaAndrasObedient or alexiaJezObedient:
            "… For now he just wanted to know what did that distant look in her eyes meant, or that eeries silence that followed after his departure."
        else:
            "For now he wished he didn’t hear her weep from behind the door."
        $ promisedFertilityTreatment = False
        $ change_relation('alexia', -3)
        if consultationAndrasAgree:
            $ change_relation('alexia', -3)
        if consultationAndrasRebuke:
            $ change_relation('alexia', 3)
        return
        
    "You don’t want to hear about her pregnancy issues ever again.":
        $ released_fix_rollback()
        if alexiaScolded == True or avatar.corruption > 59:
            show rowan necklace angry at midleft with dissolve
            show alexia 2 necklace concerned at midright with dissolve
            ro "I don’t know Alexia. Is it?"
            ro "Because I don’t want to have this conversation again in the near future."
            show alexia 2 necklace angry at midright with dissolve
            al "… You never wanted to have them before."
            show rowan necklace neutral at midleft with dissolve
            ro "And the threat of imminent demise doesn’t make them any more appealing."
            ro "No more talk about kids, do you understand? If I think the time is right, I’ll bring the subject up. Are we clear?"
            show rowan necklace angry at midleft with dissolve
            ro "… I said, “are we clear”?"
            show alexia 2 necklace angry at midright with dissolve
            al "… Crystal clear."
            ro "Good. Now excuse me. I have a castle to run."
            al "… Of course."
            hide rowan with moveoutleft
        else:
            show rowan necklace concerned at midleft with dissolve
            show alexia 2 necklace concerned at midright with dissolve
            ro " Alexia, I know this isn’t easy on you. But… Please, don’t bring this up again."
            show rowan necklace neutral at midleft with dissolve
            ro "This conversation is painful for me too."
            al "… No doubt."
            ro "I can’t afford to be distracted. "
            show rowan necklace concerned at midleft with dissolve
            show alexia 2 necklace happy at midright with dissolve
            al "I know. I’m sorry. Me and my stupid problems, right?"
            ro "This isn’t like that-"
            show alexia 2 necklace neutral at midright with dissolve
            al "I heard you Rowan. I won’t say a word about this again." 
            ro "It’s not that I-"
            show alexia 2 necklace angry at midright with dissolve
            al "{b}I said I heard you.{/b}"
            "He could hang an axe in the air. But he had no other choice. He had to make a point, even if it was an unpleasant one."
            show alexia 2 necklace neutral at midright with dissolve
            ro "Alright… I’ll bring the potion back to Nasim."
            ro "Take care, love."
            hide rowan with moveoutleft
            al "Good day, Rowan."
        $ promisedFertilityTreatment = False
        $ change_relation('alexia', -15)
        if consultationAndrasAgree:
            $ change_relation('alexia', -3)
        return

###################################################################################################################################
###################################################################################################################################
###################################################################################################################################

label rowan_frustration_venting:

scene bg14 with fade
show rowan necklace concerned at center with dissolve

"Again, the twins demanded his attention with some minor problem that anyone with a working brain could prevent from happening in the first place." 
"Again, he was forced to spend an hour explaining the most basic concepts to a man who could break him in half should the mood strike him." 
"{i}Again{/i}, he was forced to endure the countless teasing of a woman who, no matter her charms, would gladly exchange his amulet for a collar. As if it wasn’t one already."

show rowan necklace angry at center with dissolve

if serveChoice == 4:
    "Again, and again, and again, stuck in a constant loop of having to put out countless fires, never finding time to actually do some good for a change."
    
else:
    "Again, and again, and again, stuck in a constant loop of endlessly appeasing and lying through his teeth, constantly searching for a moment of distraction to sneak away and plan their escape."  
    "Too often, with little to no success."
    
show rowan necklace concerned at center with dissolve

"His patience ran thin a long time ago. But he kept going regardless."

show rowan necklace concerned at midleft with moveoutleft
show alexia 2 necklace neutral at midright with dissolve

al "Someone’s in a bad mood today."

"He almost didn’t notice her. His wife was standing in front of the castle window, watching the rain outside. Did she have nothing better to do?"

show rowan necklace neutral at midleft with moveoutleft

ro "I’m fine. Just focusing on what needs to be done."

al "Will you have time for dinner today? "

"He wouldn’t."

show rowan necklace concerned at midleft with dissolve

"It wasn’t right, but he couldn’t help it. He kept promising himself to find time for her, but there was no shortage of important matters to attend to. Too often, Alexia simply wasn’t a priority."

show rowan necklace neutral at midleft with dissolve

"Not that she was ever grateful if he did find the time after all."

ro "I don’t know. I don’t think so. Andras has been threatening to decimate the orcs again."

show alexia 2 necklace concerned at midright with dissolve

al "He always does that."

ro "Yeah."

show rowan necklace neutral at edgeright with moveoutright
show alexia 2 necklace concerned at midleft with moveoutleft

"He walked past her, trying his best to keep his expression neutral. Next week. Next week for sure-"

show alexia 2 necklace angry at midleft with dissolve
show rowan necklace concerned at edgeright with dissolve

al "… Feels like there’s always a crisis whenever I want something."

"He stopped. He turned his head just enough to look at her from the corner of his eyes."
"And he saw the accusing look in her eyes."

show alexia 2 necklace neutral at midleft with dissolve
show rowan necklace neutral at midright with moveinright

ro "I can’t plan for sudden mass executions, Alexia."

al "It’s unlike you not to. They’re not exactly that rare of an occurrence."

ro "Mystical foresight would be of great use to me. Alas, I do not possess it."

show alexia 2 necklace angry at midleft with dissolve

al "Don’t try to turn this into a joke!"

show alexia 2 necklace shocked at midleft with dissolve

ro "I could even use it to avoid this conversation."

show alexia 2 necklace angry at midleft with dissolve

al "Unbelievable. And all I wanted was one afternoon together. Was it really that much to ask for?"

show rowan necklace angry at midright with dissolve

al "Castle Bloodmeen wouldn’t collapse overnight, not that it would be much of a loss if it did."
al "Or are you that busy with-"

show alexia 2 necklace shocked at midleft with dissolve

ro "Alexia, I don’t have the time to fucking babysit you today. Whatever it is you’re dealing with at the moment, handle it yourself."

if all_actors["alexia"].corruption < 31:
    show alexia 2 necklace concerned at midleft with dissolve
    al "W-what?"
    "There it was - the fucking wounded gazelle gambit, complete with a breaking voice and teary eyes." 
    "Always there. First, she has the fucking {i}audacity{/i} to look at him with such contempt, and now she pulls this shit again."
    show rowan necklace shock at midright with dissolve
    ro "… Who exactly are you hoping to fool with that?"
    show rowan necklace neutral at midright with dissolve
    ro "Can’t be Andras, he murders people for breakfast, and if he was any more like his father, it probably wouldn’t be a euphemism."
    ro " Can’t be Jezera, saw one maid try to pull that shit on her, and it didn’t end well."
    show rowan necklace angry at midright with dissolve
    ro "Which leaves me. So let me be perfectly clear about it - {b}stop{/b}. Just. Fucking. Stop."
    al "… Rowan? I- I’m your wife! How-"
    al "… How can you even talk to me like that?"
    "And now demanding explanations, and probably apologies along the way. Always the same."
    ro "I have to play diplomat seven days a week from dawn till dusk, so you will have to forgive me for wanting to be frank for ten seconds."
    ro "You have one job - don’t get in my way while I take care of everything here. Is that clear?"
    al "Rowan? I don’t-"
    ro "Fucking hell."
    "More complaints. He couldn’t stand it. He didn’t have time to listen to it. He didn’t {i}want{/i} to listen to it. Not anymore." 
    hide rowan with moveoutright
    "He turned around, and left right there, feeling the rage swell inside of him."
    show alexia 2 necklace shocked at midleft with dissolve
    al "Rowan?"
    al "Rowan!"
    scene black with fade
    "... He didn’t look back."
    jump ventingDungeonsFirstTime
    
elif alexiaAndrasObedient or alexiaJezObedient:
    show alexia 2 necklace neutral at midleft with dissolve
    al "... Huh."
    "She scoffed - scoffed at him! The uppity bitch-"
    if alexiaJezObedient:
        al "If you’re trying to emulate our captors, you should at least try to keep your voice down. Jezera never has to raise it."
    else:
        al "If you’re trying to be intimidating, you’re not doing a very good job at it."
        al " Then again, you never had."
    ro "Listen here-"
    al "You’ve made your point Rowan. I wish you a good day."
    hide alexia with moveoutright
    show rowan necklace shock at midright with dissolve
    "She turned away - actually turned her back on him!"
    "He couldn’t believe it."
    show rowan necklace angry at midright with dissolve
    " … Well, good. He had no intention of being in her company either."
    hide rowan with moveoutright
    "He walked away too - and did not look back."
    jump ventingDungeonsFirstTime
    
else:
    show alexia 2 necklace angry at midleft with dissolve
    al "… What? What the hell is your problem today?"
    "First, she had the nerve to look at him with such contempt, and now she was trying to blame {i}him{/i}? The god damn audacity of that woman!"
    ro "Here’s my problem-"
    show alexia 2 necklace neutral at midleft with dissolve
    al "No. You know what? No."
    show alexia 2 necklace angry at midleft with dissolve
    al " I’m not one of your servants. I don’t have to stand here and listen to you give me shit."
    al "You’ve made your point. I wish you a good day."
    hide alexia with moveoutleft
    show rowan necklace shock at midright with dissolve
    "She turned away - actually turned her back on him!" 
    "He couldn’t believe it."
    show rowan necklace angry at midright with dissolve
    " … Well, good. He had no intention of being in her company either."
    hide rowan with moveoutright
    "He walked away too - and did not look back."
    jump ventingDungeonsFirstTime
    
label ventingDungeonsFirstTime:

$ bootlegRepeatAvailable = True
$ bootlegSexCount = 0

scene black with fade

"For once, he understood how Andras felt. If someone dared to stop him right now, he wouldn’t guarantee they would leave unharmed." 
"But that would do nothing to extinguish his anger. What he needed… What he {i}wanted{/i}…" 

scene bg8 with fade
show rowan necklace angry at midleft with moveinleft
show orc soldier neutral at midright with dissolve

ro "The key."

"One of the dungeon guards offered it without question. There was only one key that this particular orc held, that Rowan could ask for. One key, to one specific cell."

hide orc soldier with moveoutright

"Without stopping, Rowan ventured further into the dungeon. Past his own cell, past the cells that kept Rosarian prisoners. These were used more often, but the Bloodmeen dungeons were massive, and held many rooms."    
"And deep down, laid the cells of those who were meant to be forgotten. Rowan headed for one of those, and turned the lock open." 

show bg8 with flash

boot "Bwuh?! M-mastah?!"

show rowan necklace neutral at midleft with dissolve

"The orcess inside sprung to her feet, making her obscene tits wobble. Specimen 03. Nasim’s ill-thought project to please Andras." 
"The orcess who was meant to be Alexia."

ro " Is that how you greet the seneschal of Castle Bloodmeen?"

show rowan necklace angry at midleft with dissolve

"Confusion set into her eyes. He narrowed his."

show rowan necklace neutral at midleft with dissolve

"Instantly, she was on her knees, pressing her forehead to the ground. Rowan saw her fat tits squished against the floor, once again reminding him Nasim really held nothing back when it came to his experiments." 
"… And the wizard must have visited the orcess since their last meeting, he realized. A carpet now laid in the middle of the room, and a vanity table was placed against one of the walls, with a large mirror next to it. Guilty conscience much?"

ro "Nasim has brought you gifts. I take it you’re grateful? "

boot "A-ah, yes, Mastah! Vewy grateful!" 

ro "You can look at me when you speak."

"She looked up - and Rowan found himself staring into Alexia’s confused face. Same beautiful features, same green eyes, same red hair. He paid no attention to the tusks, the flat nose, the green hue of her skin, or anything else."

ro "You’re grateful I came to visit, are you not? "

boot "Y-yes! Very much!"

"Her eyes lit up, and she gave him the most, beautiful, radiant smile. He held his breath, as his hand went to her face, and his fingers slowly traced her puffed lips."

ro "And you liked it when I fucked your tits, haven’t you, “Alexia”?"

"The crimson blush was his answer. She raised her hands to her breasts, only to lower them immediately as she remembered this wasn’t the time to start masturbating, and somehow stammered out a response." 

$ BootlegName = "“Alexia”"

boot "Y-y-yyes, mastah… I- I- play with them ah lot, b-but… I-it felt...  ‘eally g-good when ya t-touched them."

ro "Do you want me to fuck them again, Alexia?" 

boot "Y-yes mastah!"

ro "… It’s Rowan."

boot "Y-yes, mastah ‘owan!"

"He opened his mouth to correct her. He hesitated. And the orcess opened her own mouth in return, her thick, pillowy lips forming an inviting “O” even despite the tusks."

show rowan necklace aroused at midleft with dissolve

"Swallowing, he pushed his finger forward. The orcess closed her lips, and started to slowly suck it, her green eyes looking at him expectedly." 
"He could stare into these dull, trusting eyes for all eternity. But he only had a few hours, and then it would be back to his responsibilities, as seneschal of Castle Bloodmeen, and as the hero who traversed the continent to save his wife." 

show rowan necklace angry at midleft with dissolve

"To save a wife who now only ever looked at him in contempt." 

"Suppressing a snarl, he pulled his finger out and seized the woman by the hair, pulling them roughly. The orcess gave a surprised yelp, but didn’t resist one bit." 
"If anything, she started breathing heavily, her eyes breaking his gaze for a moment, wandering to his crotch. Wandering to his hard, erect cock, so clearly visible through his pants." 

"And eyeing it hungrily."

jump ventingMenu

label ventingRepeatVisit:

scene bg8 with fade
show rowan necklace neutral at center with dissolve

"No one disturbed him as he headed for the dungeons. He opened the door to the same cell as before, and was once again greeted by a surprised yelp and a pair of mountainous tits swaying before his very eyes." 

boot "Mastah ‘owan!"

"The orcess fell to her knees immediately, already growing flushed as she looked at his cock."

if bootlegSexCount == 0:
    "He held his breath as he walked up to her, brushing his hand against her red hair. The orcess smiled, and waited for his order."

elif bootlegSexCount == 1:
    "He walked up to her, and ran his fingers through her red hair. The orcess smiled, looking at him with those dull, needy eyes, waiting to be used again."

else:
    #ro smirk
    "He walked up to her, and lovingly ran his fingers through her hair - then yank her head back. The orcess half moaned, half yelped, and looked up to him with that hopeful, {i}hungry{/i} look in her eyes." 
    
jump ventingMenu

label ventingMenu:

menu:
    "You want to look her in the eyes as she takes your cock.":
        $ released_fix_rollback()
        "Rowan seized her by the arm, and shoved her violently onto the bed."
        #ro smirk
        "It creaked dangerously under the weight of her heavy body. Rowan feasted his eyes on her absurd curves, again admiring her massive tits and fat ass. He smiled as he noticed her pussy glistening in the torchlight."
        ro "You look like a slut."
        boot "Uh-huh!"
        #ro angry
        ro "That wasn’t a compliment!"
        show bg8 with sshake
        "He struck her ass, leaving a red imprint of his hand, and arousing a lustful moan from the obscene orcess. Already she was panting with need, waiting to see his cock, waiting to feel it inside her."
        show rowan necklace naked at midleft with dissolve
        "And he would give her just that. He undid his pants, freeing his painfully erect cock. He wouldn’t deny it the comfort of her wet pussy for long."
        scene black with fade
        "… Maybe a little."
        #cg1
        scene cg876 with fade
        show rowan necklace naked behind cg876
        pause 3
        "Her eyes widened at the sight of it, and her mouth went slack, almost salivating at the thought of tasting it. Without an order being given, she spread her legs for him, urging him to plunge in."
        "He chuckled, and ran the tip over her puffy vulva, eliciting a needy moan."
        boot "A-aah! Mastah ‘owan!"
        "Music to his ears. Lightly, he pushed his hips, rubbing the full length of his cock against her pussy, and watched her expression melt."
        boot "M-mastah ‘owan! Ph-phleease!"
        ro "“Please” what?"
        boot "Phlee-ease put it in!"
        ro "Is that how a slut begs?"
        "He reached out and twisted her nipple, and the orcess cried out, not holding back one bit."
        boot "PUT IT IN! MASTAH, PHLEASE PUT- PUT YOUS COCK IN! I WANT COCK! I WANT YOUS COCK MASTAH ‘OWAN! MASTAA-AAAAAH!"
        "Her desperate pleadings turned to ecstasy as he thrusted into her with one, brutal motion."
        boot "A-AAAH! AAAAH! MASTAH!"
        "She wasn’t tight - of course a slut like her wouldn’t be tight - but she was wonderfully wet, to the point where his cock made obscene squelching noises every time he pushed into her."
        "He wasn’t sure what he enjoyed more - that, or her lustful moans. He only knew he wanted more - of both."
        "He pulled out, and thrust again, pushing his cock to the very base, making his balls slap against her fat ass. Then again, and again, hammering into her pussy without restraint nor consideration."
        boot "HARDER! HAA-AAA-AARDER!"
        "And all she did was beg for more."
        scene cg878 with fade
        show rowan necklace naked behind cg878
        pause 3
        "Grunting, he did just that, thrusting his hips with such force that the whole bed creaked dangerously. His hands went to her tits, and he kneaded them roughly. Ah, how soft they were!"
        boot "AAAAAH! AAAAAH!!! MASTAH!!!"
        "And how sensitive! He held on to her, as he kept plowing into her. There was no rhythm to his movements, and he couldn’t care less for it. All that mattered was putting that dumb slut in her place."
        boot "AA-AAAH!! MASTAH ‘OWAN!! HARDER!! HARDER!!"
        "All that mattered was making her scream his name out from the bottom of her lungs while she took his cock."
        boot "MASTAH ‘OWAN!! FE-EELS SHO GOOOOOD! YOUS C-COCK IS SHO GOOD!!! AAAH!"
        "All that mattered was making those green eyes look at him with worship."
        boot "I LO-OOOO-OVE YOUS COCK MASTAH ‘OO-OOO-OWAN!!!"
        "As they did years ago."
        boot "AA-AAAH!! MASTAH ‘OWAN!! MASTAH ‘OWA-AAAA-AANN!!"
        "He was too soft on her before."
        menu:
            "Put the bitch in her place.":
                $ released_fix_rollback()
                scene cg877 with fade
                show rowan necklace naked behind cg877
                pause 3
                boot "AA-A?!"
                "Her screams came to an abrupt end as his hand tightened around her throat. Still thrusting his cock relentlessly, he watched as ecstasy slowly faded from her eyes and lips." 
                "He watched it be replaced by fear."
                boot "..."
                "{i}And subservience.{/i}"
                "Grinning from ear to ear, he loosened his grip just enough to let her breath again. She gasped - and only barely stopped herself from moaning again." 
                "Chuckling, he twisted her nipple again, and saw her wriggle in agonizing ecstasy. That was the expression he wanted to see. That was the expression that suited *her.*"
                "He redoubled his efforts, driven by desires he didn’t want to name, but couldn’t deny anymore." 
                "Did she come at some point? He wasn’t sure, and he didn’t care. When he felt his own urge rise, he rammed his cock all the way inside, cumming again and again, grunting as he did."
                show cg877 with sshake
                show cg877 with sshake
                show cg880 with flash
                pause 3
                "Painting her insides white."
            
            "Be lenient. This time.":
                $ released_fix_rollback()
                "He felt the rage well inside of him, but how could he punish the lips that cried such sweet things right now? Even if later they would turn into a sneer… He could be compassionate. Unlike her."
                boot "OOO-OOOH?!"
                ro "Enjoy your reward, slut."
                "He started to knead her tits more enthusiastically, even going as far as to slow his thrust a little to give them proper attention. They were a work of art - perverted art, but still."
                boot "OOO-OOH- AAAAAAH!!!"
                ro "… Did you just come?"
                ro "Ha! You filthy {i}slut{/i}!"
                "He twisted her nipples again, provoking yet another moan full of agonizing ecstasy. Laughing, he resumed his thrusts, and didn’t slow again until he felt himself approaching the edge."
                ro "Take it! Take my cock you filthy whore! Nngh-!"
                "Thrusting his cock all the way inside, he came, again and again."
                show cg879 with sshake
                show cg879 with sshake
                show cg880 with flash
                pause 3
                "Painting her insides white."
        
        scene bg8 with fade
        show rowan necklace naked at center with dissolve
        "Finally, he pulled himself off her. Panting, he looked down to admire the results of his effort."
        "The gasping mess of a woman, cum spilling out of her pussy, without the strength to pull her heavy body up from the bed."
        show rowan necklace happy at center with dissolve
        show bg8 with sshake
        "He slapped her thigh, eliciting another yelp, and garnering her attention again."
        ro "What do you say?"
        boot "A-ah… A-ah… Thank you… Mastah ‘owan…"
        "… And she capped it with that shy, {i}expecting{/i} smile. “Come again”, it said." 
        ro "Clean yourself up."
        if bootlegSexCount == 0:
            show rowan necklace neutral at center with dissolve
            ro "Say nothing of this to Nasim. Understood?"
            show rowan necklace neutral at center with dissolve
            boot "Y-yes mastah ‘owan."
        "Unable to stop his smile, he chuckled again, and left her cell, locking the door behind."
        $ bootlegSexCount += 1
        if bootlegSexCount == 1:
            jump ventingRealization
        else:
            return
            
    "Leave.":
        $ released_fix_rollback()
        if bootlegSexCount == 0:
            show rowan necklace concerned at center with dissolve
            "Very slowly, he pulled away from her. It should’ve been easy, but wasn’t so. He couldn’t hear his own thoughts through the deafening sound of his blood rushing."
            show rowan necklace neutral at center with dissolve
            ro "… That’s enough."
            hide rowan with moveoutleft
            "He left without looking back, leaving the puzzled orcess behind. If he stayed any longer, he could’ve done something he shouldn’t have."
            scene black with fade
            "Something there would be no turning back from."
        else:
            show rowan necklace happy at center with dissolve
            "He pulled away from her. Just seeing that devoted, adoring expressions of hers made him feel better."
            ro "… Keep it up."
            hide rowan with moveoutleft
            "He left without a word of explanation, leaving the puzzled orcess behind. She wouldn’t understand. He wasn’t certain he did."
            scene black with fade
            "Nor if he wanted to."
        return
        
label ventingRealization:

scene black with fade

"The smile would not leave his face, but it kept losing all meaning with every step he took."

scene bg8 with fade
show rowan necklace shock at center with dissolve

"Heaving, he leaned against the dungeon walls, trying not to collapse as the realization of what he had just done started to set it."

show rowan necklace concerned at center with dissolve

"Swallowing, he forced himself forward. Step by step. Towards the exit. Past the cells dedicated to his very people. Past his own." 
"He peered past the bars, half expecting to find the shriveled, decaying body of Rowan Blackwell inside." 
"There was none." 

show rowan necklace neutral at center with dissolve
        
"… Of course there wasn’t."

show rowan necklace angry at center with dissolve

"Only a fool would let himself die there."

show rowan necklace neutral at midright with moveoutright
show orc soldier neutral at midleft with dissolve

"...  Straightening himself, he headed for the guarding orc. He handed him the keys - then grabbed him by the armor and pulled close." 

show rowan necklace angry at midright with dissolve

ro "You saw nothing. You tell anyone anything, I’ll snap your neck. If Nasim threatens you with anything, tell him I’ll snap his fucking neck too if he keeps sniffing around. Understood?"

os "Yes, masta Rowan."

show rowan necklace neutral at midright with dissolve

"Good."

hide rowan with moveoutleft

"He released the man, and headed into the castle, ready to resume his duties."

return

######################################################################################################
######################################################################################################
######################################################################################################

label cup_of_tea:

scene bg24 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan walked briskly through the threshold of the brothel. The girls inside, he knew, would show discretion. But, it would be best if he were not seen by many people."
"He found a familiar face waiting for him at the desk. Lia, the attendant from his first visit, was on duty today. Evidently, it had not been a very interesting shift. The girl was half slumped over her desk."
"But, when she saw him, her eyes lit up."

lia "Oh, I remember you! You’re-"

"Rowan held a finger to his lips, silencing her."

ro "Not so loud."

lia "Oh. Sorry."

if liaAttitude == "flirt":
    lia "You were the customer interested in a session with me, right? The one who smacked my ass."
    show rowan necklace happy at midleft with dissolve
    "Rowan smirked to himself slightly at the memory of it. Meanwhile, Lia glanced around rapidly."
    lia "Technically, I’m not supposed to go off by myself with a client. The madam has a real stick up her ass when it comes to attendants having encounters with clients."
    lia "But you know, it’d be a shame if I sat out my best years doing desk work. Don’t you think I’m too pretty to waste my time with that?"
    "She made a pouting expression with her lips that came across as an almost amateurish attempt at seduction."
    lia "You know, if you brought coin with you, perhaps I could-"
    show rowan necklace neutral at midleft with dissolve
    ro "No."
    ro "Enticing as it sounds, if Shaya told you not to, I’m sure she meant it. In fact, I came today to see her myself."
    lia "...Oh."

else:
    lia "You were the one who gave that big tip! The only girls who get tips like those are the ones who go with clients."
    show rowan necklace happy at midleft with dissolve
    ro "You still haven’t been allowed a promotion to actual courtesan?"
    "The attendant rolled her eyes."
    lia "The Madam says that at the brothel that trained her, apprenticeships on attendant duty could last for years. Years!"
    lia "It’s madness. I’m wasting away my best years doing desk work. My beauty is being wasted."
    "Rowan shrugged."
    ro "I’m sure Shaya has her reasons. Speaking of which, I’m here to speak with her."
    show rowan necklace neutral at midleft with dissolve
    
lia "The Madam is back in her room for the afternoon. She is taking tea with another woman, and asked for none of us to disturb her. Though, if you wish to stop in, I am sure it would be allowed. She asked us to bring you to her should you ever return."

show shaya happy at midright with dissolve

"True to his word, he found Shaya in her personal back room. It was among the largest in the brothel, with a small private stage and multiple segments divided by partitions. As much a place to engage in business as to engage in pleasure."
"And, of course, the guest was someone Rowan might have expected."

show jezera happy at edgeright with dissolve

je "Oh, now there’s a delightful little surprise. Has the valiant hero come down to this den of sin to pay us a visit?"

sha "{i}Jezer’aca! Hush!{/i}"
sha "It’s bad form to scare a client away."

je "You hush. It’s just a little fun. What good is keeping such a prestigious trophy if you don’t prod him a bit here and there?"

show rowan necklace happy at midleft with dissolve

"Rowan sighed and walked over to the immaculately carved low table they sat around. A porcelain kettle sat in the middle, which they were using to pour into small cups."

ro "Ladies. I had hoped to catch Shaya alone."

"He took a seat on a recliner on the far side of the table."

je "Oh, I’m interrupting your personal intimate time, am I? Truly the worst of my sins. I know the jobs I give you must leave you with a lot of tension."

sha "{i}Jezer’aca! What did I just say!?{/i}"

"Jezera simply rolled her eyes."

ro "Have I walked in on anything important?"

je "Why, of course, you are. Is tea time with an old friend not something you’d call important?"

sha "She exaggerates, Sir Rowan. Your presence is hardly ruining anything."
sha "In fact, please allow me to pour you a cup as well. It is the least of my obligation as a host."

"She gave a short bow and rose to grab another delicate cup from her cupboard."

je "A waste of good Imperial Tea if you ask me. Peasant boy over here hasn’t quite developed a taste for the finer things."

sha "Then what good am I if I cannot instruct him? Is it not a courtesan’s job to ensure that her client receives the finest in all aesthetic delights?"

je "Oh, I’m sure you’re going to show him some delights. But, if you’re as good a whore as you say, you ought to have better weapons in your arsenal than eastern tea."

"Rowan thanked Shaya softly and took a sip from the drink. It was a strange and bitter mixture. Surely this is not what they drank in Qerazel for fun?"

#if diplomacy is above (x - moderate difficulty) - TO DO
if shayaClue3 == False:
    ro "You make it sound like you don’t approve of her profession, Jezera. I didn’t take you for a prudish woman."
    je "Prude?"
    "She rolled her eyes."
    je "I was the one who picked her profession. And paid for her training out of my own damn pocket. I just wish my money bought more."
    "Shaya chuckled and took a gentle sip from her drink. She had to take an extra moment to work it beneath her veil, without exposing any of her hidden features to Rowan."
    sha "{i}Jezer’aca{/i} enjoys her jokes. But, she knows that I have very happy clients."
    $ shayaClue3 = True
    $ shayaClueScore += 1
    
else:
    ro "A strange sentiment for a woman with a sexual history that could fill a book."
    "Jezera giggled."
    je "Oh hush you. Don’t interfere when I’m trying to rile her up. She’s gotten good at maintaining that calm facade of hers. But, don’t think she isn’t seething."

je "Now then, I’m normally one to stick around when two become three. So, unless you plan on bringing me to bed with you…"

scene black with fade
#jez smirk
show jezera happy at center with dissolve
je "...A request that would come with some invasive stipulations for you both, to be sure…"

scene bg24 with fade
show rowan necklace happy at midleft with dissolve
show shaya happy at midright with dissolve
show jezera happy at edgeright with dissolve

je "..Now is going to have to be when I take my leave. Have fun with her, Rowan. That’s what she’s here for."

"Jezera rose from her cushion and planted a soft kiss on Shaya’s cheek. For a split second, he thought he saw Jezera staring at him, even as she did so. Then with nothing but a final wave, she departed."

hide jezera with moveoutright
show rowan necklace neutral at midleft with dissolve

"Rowan’s eyebrows narrowed."

ro "Did you tell her about my prior visit? I had not told her I would be making use of her gift."

sha "Of course not, Sir Rowan. She is a spymaster. She already knew before I could tell her."

#if rowan has an hig intrigue skill - TO DO
"He chewed on her words for a lingering moment. Of course, it would not be surprising if Jezera were keeping tabs on this place...and on him. But, there was something that didn’t quite come together here. It wasn’t like Jezera to simply.."
"Why had Jezera chosen the brothel specifically as a reward for him? Why Shaya?"
scene bg9 with fade
quest "Perhaps having you be the one to tell her is the point? There are some people in the castle she trusts, and some whom she does not."
scene bg24 with fade
show rowan necklace neutral at midleft with dissolve
show shaya happy at midright with dissolve
"There was something else going on here…"
$ shayaClue7 = True
$ shayaClueScore += 1

show rowan necklace happy at midleft with dissolve

ro "That would make sense. It would be pretty surprising if she didn’t have someone else on your staff who was reporting to her."

"Shaya smiled faintly behind her veil."

sha "There are a few candidates for that position of whom I’d suspect. But, it matters not. Were they not reporting a fact to her, I would do so instead. I have no secrets from my blood sister."

"Rowan swished the vile liquid around in his little cup."

show rowan necklace concerned at midleft with dissolve

sha "You seem troubled. Shall we move this rendezvous behind the bedroom screen?"

ro "No...no. I think just tea is enough for today."

sha "Ah, once more that vile temptress has stolen a client from me. I must be fairly undesirable to lose out to a drink that you don’t even like."

ro "I never said I didn’t like it."

"Shaya poured another glass for herself. She clutched the drink daintily in both hands."

sha "Yet, it’s still true."
sha "That is quite alright, it simply means more for me. I fear I’m starting to nurse a small addiction to the substance. It’s quite fashionable in Qerazel high society to consume a cup with every meal."

show rowan necklace neutral at midleft with dissolve

"Rowan leaned back in his recliner and crossed his legs."

ro "You must be pretty well acquainted with Qerazel high society then? Were they your main customers before you were called here?"

sha "Oh, Sir Rowan. You needn’t waste time asking about me. All my stories are woefully boring. I’m the one sitting with a war hero. Surely you have-"

if avatar.corruption < 31:
    ro "I’m, er, flattered by your interest. But, I’d rather not."
    
else:
    ro "No. None of that shit."

ro "I’m not really in the mood to talk about myself."

show shaya neutral at midright with dissolve

sha "Hrmm."

show shaya happy at midright with dissolve

sha "Then feel free to talk to me on another subject. You know that I am your service, Sir Rowan."

$ shayaMenuCount = 0
$ shayaChildhoodSeen = False
$ shayaServingSeen = False
$ shayaPrefsSeen = False
$ shayaRowanSeen = False
$ shayaFutureSeen = False
$ shayaCustomerSeen = False
$ shayaCubiSeen = False

label shayaMenu:

if shayaMenuCount == 3:
    jump postShayaMenu

elif shayaMenuCount == 2:
    "One choice remains."
    
elif shayaMenuCount == 1:
    "Two choices remain."
    
else:
    pass
    
menu:
    "“About her Childhood”." if shayaChildhoodSeen == False:
        $ released_fix_rollback()
        $ shayaChildhoodSeen = True
        "Rowan gave a nervous chuckle."
        ro "You might find this an unusual question for a concubine…but, I was wondering about your childhood?"
        sha "It’s not that unusual a question. Simply one with a boring answer."
        sha "I was the daughter of spice merchants. Of which, Qerazel has many. When I was young I joined a posse of local girls. Of whom Jezera joined. After that, my destiny was with her."
        "Rowan scratched the side of his head."
        ro "You jumped over the family part. Any living siblings? Do you still speak to them? Do they know about your profession?"
        "Shaya simply shook her head."
        sha "I jumped over it because it is barely worth remarking upon. From my teenage years, Jezera has been my only family that matters. I have not seen them or spared them more than a passing thought in years."
        show shaya neutral at midright with dissolve
        sha "In fact, if my father saw me today, I have no doubt he would fail to recognize me. I would be a stranger to him."
        ro "I see…"
        "That seemed unlikely to Rowan’s eyes. He’d been able to recognize people he’d last seen as teenagers before. Did Shaya have so little affection from her birth family?"
        show shaya happy at midright with dissolve
        $ shayaClue8 = True
        $ shayaClueScore += 1
        $ shayaMenuCount += 1
        jump shayaMenu
        
    "“About Serving Qerazel’s Nobility”." if shayaServingSeen == False:
        $ released_fix_rollback()
        $ shayaServingSeen = True
        ro "Tell me about your life Qerazel. I’ve always considered taking a trip there. Al-Serah spoke glowingly of it."
        ro "Clearly, you were no street whore. Did you serve the upper class?"
        "Shaya nodded slowly."
        sha "Would I cease to be humble if I admitted it to be the case? Yes, I had a tendency to serve a clientele among the city's elite. Truth be told, I was even called upon occasionally by a Doux and a Strategos..."
        "Rowan sat eagerly as she regaled him with stories of Qerazel high society. Even for a man who had witnessed the vain pettiness of noble politics in Rastedel, the opulence and instability of Imperial high society was shocking."
        sha "...After my debut, my perspective shifted. The clientele I received was so much higher up the food chain, I could not help but see it from a similar vantage point. Is there any more noble a woman than the whore whom the nobles share a bed with?"
        ro "..."
        ro "Your debut?"
        sha "Ah, of course. I shall explain."
        sha "For a time, I plied my art in lower venues and the like. But, Jezera went out of her way to ensure I had the training and presentation of a more proper courtesan. Afterwards, she helped me conduct a formal “debut” at the {i}Empress of Waters{/i}."
        ro "And such a debut is normal?"
        sha "Above a certain rung, yes. Prostitution is social, Sir Rowan. On a street level, it functions through the same channels of information as slum gossip. But, among the social elite, it must take on the same character."
        if avatar.corruption < 31:
            ro "I’m learning much today, it seems. About topics I would never have thought to be well acquainted with."
        else:
            ro "I’m learning much today, it seems."
        sha "A good thing, Rowan. Information is a valuable currency."
        $ shayaClue9 = True
        $ shayaClueScore += 1
        $ shayaMenuCount += 1
        jump shayaMenu

    "“About her Sexual Preferences”" if shayaPrefsSeen == False:
        $ released_fix_rollback()
        $ shayaPrefsSeen = True
        show rowan necklace aroused at midleft with dissolve
        "His eyes trailed down her body, showing little effort to hide what he was doing. He may not have planned on moving this to sex, but Rowan had not forgotten the original purpose of his visit either…"
        ro "You’re a woman who knows a good deal about sex and her own sexuality. I am sure that you have your own tastes. Tell me, in bed what is it that you want?"
        "Shaya sighed and spread her legs ever so slightly."
        sha "Whatever you desire. You say the word, and I will show you unique esoteric pleasures."
        if avatar.corruption < 31:
            ro "That’s, uh, not what I meant."
        else:
            ro "That's not what I meant."
        ro "I mean, what gets you personally going. As if you were not with a customer and just wanted to enjoy it for yourself."
        sha "Looking out for my pleasure? You’re a sweet man, Sir Rowan."
        if avatar.corruption < 60:
            ro "What’s a hero for if not to save blushing maidens?"
            "Shaya giggled softly."
        else:
            #ro smirk
            ro "Maybe I’m just trying to find the right buttons to leave you addicted to my cock. It’s entirely selfish, I assure you."
            sha "You would not be the first man or woman to attempt such a thing."
        "She leaned back in her seat."
        sha "But, you may be disappointed. My first answer was more correct than I let on. What you desire…"
        sha "When I have pleased my partner...when they have enjoyed the encounter...and when I can see it on their face. When I have fulfilled my purpose. That is the utmost of the erotic."
        show rowan necklace happy at midleft with dissolve
        ro "That seems like a useful fetish for a whore to develop."
        sha "Perhaps you have it backward. A woman with such a selfless sexual predilection is inclined to find much more joy in a courtesan’s craft then most."
        show rowan necklace neutral at midleft with dissolve
        $ shayaMenuCount += 1
        jump shayaMenu
        
    "“About her Feelings about Rowan”." if shayaRowanSeen == False:
        $ released_fix_rollback()
        $ shayaRowanSeen = True
        "Rowan used his hand to bat the cup around on the table. Looking at Shaya, it was not hard to be constantly reminded of who she was and what she did."
        ro "Alright, let’s try this one."
        ro "..."
        ro "What do you think about me? What kind of impression have I left on you?"
        "Shaya reached out softly and steadied his hand, so as to prevent the cup from spilling. Rowan didn’t care about the reason. The moment her skin touched his, the contact was all he could think about."
        sha "You, Sir Rowan? I think you’re handsome and wise. A man of clear talent. But, a talent many would not recognize. An ability to clearly when everyone else covers their eyes."
        sha "But also...not very used to this. Your new home, of course. But also, not used to having your ability {i}seen{/i} either."
        if avatar.corruption < 31:
            sha "And of course, so humble and selfish. I think you are a man who would not hesitate to save my life if bandits were to be set upon me. Even if you had to sacrifice yourself to do it. There is a warmth. Like a blanket from Uvraith."
        elif avatar.corruption > 60:
            sha "And of course, a man with a hunger. For sex. For control. The type of man a woman should be careful about, lest she be used to sate his hunger. Yet...not entirely an unattractive quality either..."
        else:
            sha "And of course, you are a man with a taste. There are a great many things you enjoy...but also discipline. The restraint not to succumb to base impulses. A frustrating tendency for one who peddles in base impulses, like myself. But, admirable still."
        ro "Er, right. But, I suppose what I meant is, what am I to {i}you{/i}?"
        "She looked down at her hand on his wrist. Slowly, she massaged a circle into his skin...before withdrawing back to her cushion."
        sha "What would you like me to be for you?"
        sha "In the hands of the right customer, I can be whatever is required. A fucktoy. A proxy wife. Whatever your heart desires."
        "Rowan drew his hand back slowly and stared at the place she’d touched him."
        ro "The right customer…"
        "Best not to follow that line of thought too far…"
        $ shayaMenuCount += 1
        jump shayaMenu
        
    "“About Her Plans for the Future”." if shayaFutureSeen == False:
        $ released_fix_rollback()
        $ shayaFutureSeen = True
        "Rowan paused for a moment to consider his next question. But, he kept finding himself hitting blank spots. So, he chose as basic a question as he could."
        ro "So, er, after this job is done, when you’re not working as madam here any longer, what do you plan to do? Is there anything you want?"
        "Shaya smiled faintly."
        sha "Whatever {i}Jezer’aca{/i} asks me to do after. If she desires for me to remain madam for all my days, then it will have been a life well spent."
        ro "Really, there’s nothing else you want to do? No personal ambition."
        sha "I am content. There is nothing."
        ro "...Right."
        $ shayaMenuCount += 1
        jump shayaMenu
        
    "“About Her Wildest Customer”." if shayaCustomerSeen == False:
        $ released_fix_rollback()
        $ shayaCustomerSeen = True
        "Rowan laughed to himself and leaned over the table. He had to be careful not to knock over his cup with his elbow."
        ro "How about something fun then? Tell me about your wildest experience with a customer."
        sha "That may prove a challenging question, Rowan. There are more than one good option. But, for you, I’ll consider it."
        sha "Hrmmm."
        sha "Perhaps this story will do."
        sha "One morning, I was visited by a woman in her fineries who wished for a taste of pleasure. Her husband failed to provide for her, you see. So, the morning was spent showing her what she had been missing from her life."
        sha "The following afternoon, a merchant came to escape the pressures of marriage to frigid and joyless marriage. So, I gave him some of the pleasure he’d been lacking."
        sha "But, can you guess what I discovered that night when reviewing the records?"
        show rowan necklace happy at midleft with dissolve
        "Rowan scratched his chin."
        ro "They were husband and wife?"
        sha "Indeed."
        ro "And you slept with both of them on the same day?"
        sha "Indeed."
        "Rowan paused to consider his words."
        ro "Why didn’t you tell them? I mean, if they were both coming to you because they were unsatisfied, perhaps…"
        sha "If I had done that, all that would have happened would have been the eruption of their already precarious marriage. The news they were being cheated upon would not have been kind. The only question is who would feel more aggrieved."
        sha "Besides...it would have cost me two customers."
        "She giggled to herself softly into her hand."
        sha "Is that the sort of story you were looking for, Sir Rowan?"
        menu:
            "It was.":
                $ released_fix_rollback()
                "Rowan nodded with a laugh and then tortured himself with another swig from the vile tea."
                ro "Definitely."
                show rowan necklace neutral at midleft with dissolve
            "Something more sexual.":
                $ released_fix_rollback()
                show rowan necklace aroused at midleft with dissolve
                "Rowan’s eyes briefly glanced down at her chest. He was sitting close enough to get a prominent view. The low angle of the table certainly helped."
                ro "I was thinking something with a bit more...err, spice."
                sha "Ah. Your motives in the question grow clearer and clearer."
                sha "Well, if that is the sort of story you wish for…"
                sha "In my line of work, one occasionally receives a request to visit a home. More travel time and less safety, so such jobs normally pay quite well."
                sha "In this particular case, it was with a man with a certain peculiar fetish. He brought to me the clothing of an older woman and told me to wear it. Afterwards, he instructed me to pretend he was a child." 
                sha "When he spoke to me he called me...well it’s a term for mother."
                sha "This continued even into the bedroom itself. The entire time calling me mother over and over as our bodies came together."
                show rowan necklace neutral at midleft with dissolve
                ro "It was...interesting."
                ro "..."
                ro "Well, that is a more sexual story. I’ll admit."
                "They both shared a quiet laugh."
        $ shayaMenuCount += 1
        jump shayaMenu
        
    "“About Managing Cubi”" if shayaCubiSeen == False:
        $ released_fix_rollback()
        $ shayaCubiSeen = True
        "Rowan glanced back at the door of the room. The faint sounds of activity could be heard beyond. Though, the sounds of sex were less prominent in the daytime."
        ro "Do you have any skill with magic? I imagine it must be hard to control the Cubi without it. And they seem to really respect you."
        sha "Magic? No no. Nothing I can do myself."
        sha "I simply understand the creatures I have been assigned to watch. The cubi are powerful, but they are also rather straightforward. They want pleasure and get upset when they don’t get it. Once you understand incentive, control is a simple affair."
        "Rowan shifted his leg uneasily."
        ro "You sound like you’ve had a lot of contact with them before taking this job."
        sha "An astute guess, Sir."
        sha "By Jezera’s side, there was no end to the strange and arcane things I have encountered. As the daughter of a Demon Lord, the cubi of Qerazel used to flock to her."
        sha "Some to control her. Some to seek alliances."
        sha "One grows used to them and the rather odd ways they compose themselves. At least, provided that they don’t end up a thrall or a corpse."
        "Rowan scratched his head softly. In his mind, he could not help but think about..."
        menu:
            "...Jezera.":
                $ released_fix_rollback()
                ro "Well, the reason I asked was that I know well about Jezera’s tendency to experiment with magic. I had thought she might have involved you."
                "Shaya blinked twice then reclined further into her seat."
                sha "Involved, perhaps. But, never taught."
                sha "If she deems one of her innovations needed to fulfill a task, then I comply. Her work is quite miraculous for one in my profession."
                sha "..."
                sha "...And of course, when we were younger there were times she’d come to me to help her with some discovery. A charm, perhaps. Or an illusion."
                sha "I was her original test subject."
                ro " Heh. That sounds like her. I can imagine some hijinks you might have gone through."
                sha "Indeed."
                $ shayaClue10 = True
                $ shayaClueScore += 1
                
            "Something Lewd.":
                $ released_fix_rollback()
                #ro smirk
                "Rowan couldn’t help but smirk."
                ro "Okay, you have to tell me the truth then. Have you ever personally slept with a cubi?"
                if xzaratl_s_advances_rowan_sex:
                    "Rowan didn’t mention his own succubus experiences before. But, in his case they were with a rather...atypical succubus."
                "Shaya didn’t waste a beat in her reply."
                sha "Both."
                sha "Not without certain protections, of course. And it is best to avoid it if it can be helped unless it’s with a particularly self-assured cubi."
                sha "But, they are well reputed lovers and I can personally attest that said reputation is not an exaggeration. "
                #ro neutral
                $ change_base_stat('c', 3)
        $ shayaMenuCount += 1
        jump shayaMenu
        
label postShayaMenu:

"By this point, Shaya’s tea had turned cold. How long had Rowan just spent here talking with her? Longer then he’d intended the visit to be when he’d planned to come for other reasons, no doubt."
"Shaya rose from her seat and gave a soft bow."

sha "Please give me leave to put away the tea set."

show rowan necklace happy at midleft with dissolve

ro "Yes, yes."

"He watched her glide from the table with the cups and kettle in hand. Even alone between them, and engaged in simple tasks, the sway never left her walk."

sha "I presume you will be taking your leave of me soon. I can see it on your face."
sha "Before you leave, however, I have a request for you. If you’re willing to let me impose on you, of course."

if avatar.corruption < 61:
    ro "It’s quite alright."
    
else:
    show rowan necklace angry at midleft with dissolve
    ro "Get on with it."

"Shaya went to her desk and pulled forth a letter sealed in an envelope. Then, she returned to Rowan and placed it in his hand."

ro "What is this?"

sha "A formal invitation, written in my own hand."
sha "In the coming days, there is to be a party here. I wish for you to attend with me."

show rowan necklace neutral at midleft with dissolve

ro "A party?"

sha "Indeed. Much of our clientele comes from outside of Bloodmeen. Small stable portals have been set up along key points over several realms. There, we have set up the buildings that customers believe to be brothels. All just way stations in a larger operation."
sha "One such way station is on an island not far from Qerazel harbour. A short day trip for the wealthy and powerful of Qerazel."
sha "They will come believing it a party on the island, not truly knowing where they are. The staff has been carefully prepared and the agents will be ready to collect information. Perhaps to enthrall strategic officials."
            
ro "Sounds like a very useful event. Why am I to attend? Do you have some kind of plan that requires my skills?"

"Shaya returned to the table and kneeled down by his side. Her eyes shone brilliantly with interest."

sha "I want you there to be my {i}escort{/i}."
sha "Of course, I will be spending the night with an attendee of the party. Whoever pays the proper sum."
sha "But, technically, I have been instructed to treat you as a paying customer, free of charge. You could buy me for the night without wasting a copper. And it would be far more entertaining spending the evening with you."
sha "What say you?"

ro "That’s it? You want me to be there so you can fuck me instead of one of those men?"

sha "If you’d oblige the request of a humble whore, of course."

"Rowan paused for a moment. Another night with Shaya wouldn’t be the most unpleasant thing he could imagine. Still…"

if shayaClue7:
    "...Why would she be spending her time with him when she could be doing something more valuable to her mission? Surely, as the best trained courtesan her skills were needed for some of that “enthralling”."

menu:
    "“I won’t miss it”":
        $ released_fix_rollback()
        $ orgyPromise = True
        show rowan necklace aroused at midleft with dissolve
        "Rowan gave a half bow."
        ro "Then for you, I will move all six realms if it means being able to attend. You can count on it."
        "Shaya giggled."
        sha "You needn’t be so dramatic, Rowan. That’s my specialty. You’d put me out of the job."
        ro "Never."
        if avatar.corruption < 31:
            show rowan necklace concerned at midleft with dissolve
            "Rowan frowned silently. Such a party would be a good chance to collect more information, right?"

    "“I will have to think about it.”":
        $ released_fix_rollback()
        $ orgyPromise = False
        "Rowan made a half smile."
        ro "I will have to consider it more fully. You know that your prior guest keeps me a busy man."
        "Shaya gave him a respectful bow in answer."
        sha "Then I will await the signs of your coming with bated breath."
        
    
"She leaned closer, pressing her face to his ear."

sha "{i}...And if you do attend, I will make it worth your while. I can do things you could only dream of your wife doing.{/i}"

show rowan necklace aroused at midleft with dissolve
   
"With that, Shaya rose and motioned for the door. She waited before Rowan left before closing it. Rowan was left standing in the lobby…"

hide shaya with moveoutright

if shayaClue4:
    "...With more questions than answers, even after having finally gotten her to speak."
else:
    "...With thoughts of what she could have meant by “worth your while” rampaging around his brain."

scene bg9 with fade
show rowan necklace neutral at midleft with dissolve

"As soon as he got back to his desk, Rowan had his investigation parchment out and was already at work scribbling in the results from today’s conversation. He’d never had such a detailed chance to interrogate Shaya about her life before."

if shayaClue7:
    "Above all else, there was one question that stuck out to him. He knew why he was investigating Shaya. For the most part. But, why was she so interested in turn? Was it mere curiosity on her part?" 
    "And what was Jezera’s role in all this? There was no possibility at all that she’d arranged for him to have free sessions with Shaya merely for his benefit."
    "{i}Why did Jezera gift me sessions with Shaya? How does she benefit?{/i}"
    "He ran a hand through his hair, but thinking about it only gave him more questions, not more answers. So, eventually, he gave up and considered other elements of the conversation."

if shayaClue8:
    "The discussion of her family struck him as odd. It was very rare to find someone so disinterested in her own relationship to her family." 
    "Had there been a fight with them in the past? But, such a thing tended to arouse strong passion, not total disinterest. And whatever must have been mutual, because if her own family wouldn’t even recognize her, it would take more than a normal process of growing apart."
    "{i}Why is she so estranged from her family?{/i}"

if shayaClue9:
    "Another element that struck him was the subject of the debut. That before she’d been a lower level courtesan, but that Jezera had arranged for her appearance in Qerazel society."
    if shayaClue15:
        "Perhaps that is why her list of clients seemed to have such a definitive start date. That must have been around when she first made her debut."
    "But, Rowan sensed there was more of a story there. Especially because it was another area where Jezera had taken action."
    "{i}What was Jezera’s role in her debut?{/i}"
    
if shayaClue10:
    "One topic was her past conflicts with Cubi. He scribbled down as much detail as he could remember from the discussion." 
    "There was, of course, the mention that Jezera had used her as a test subject in the past. She had said it in passing, but like all mention of Jezera, it had made his ears perk up. Perhaps she was more capable of magic than she let on." 
    "Perhaps it had even impaired her or harmed her somehow. That could explain why Shaya normally kept her face hidden behind a veil."
    "{i}Did Jezera teach her magic? Or did she just use Shaya as a test dummy? Did she scar Shaya’s face?{/i}"

if shayaPrefsSeen:
    "But, Rowan could only focus so much on the serious questions without sneaking in a little something more...enjoyable."
    "{i}If Shaya likes to please her partners...does she prefer riding on top, or laying back with a good view?{/i}"
    "He smirked softly."
    
"Rather than continue to write, he just started to doodle in an unsteady hand. When he looked down he realized that he’d drawn a crude picture of a human woman with a big pair of tits bared to the page."
"He wondered if that surprise of Shaya’s involved another tit-job. The memory of how the last one felt was still so vivid in his mind…"

if shayaClue7:
    "He shook his head and pulled the quill back. He needed to focus on what was really important. Investigating who Shaya was. It was unbecoming to fall for such distractions."
else:
    "...But, no it had to be something more impressive than that, right?"
    "He tapped his quill against the parchment a few more times."
    "{i}Is the surprise anal?{/i}"
    if shayaClueScore < 5:
        "He laughed to himself. The intended purpose of the parchment was nearly forgotten in the moment."
    else:
        "He shook his head and pulled the quill back. He needed to focus on what was really important. Investigating who Shaya was. It was unbecoming to fall for such distractions."
        
"When he finished, the parchment was tucked back into the book, where it would await the next time he met with Shaya..."

return

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

label password_is_fidelio:

scene bg24 with fade
show rowan necklace concerned at midleft with dissolve
show shaya happy at midright with dissolve

"After entering the brothel, Rowan was immediately ushered into a back room, where Shaya was waiting for him."
"Today was the day of the party. He found entry from castle residents restricted, and the brothel staff hard at work setting up."

if orgyPromise:
    "He’d been greeted warmly at arrival. There’d been no doubt that he’d be here in attendance, of course. He had promised to come, after all."

else:
    "There had been some surprise and scrambling to account for his arrival. His vague answer had made it hard to account for his coming. But, he’d decided to attend because of…"

    menu:
        "...His growing interest in Shaya.":
            $ released_fix_rollback()
            pass
            
        "...His continued efforts to investigate the brothel.":
            $ released_fix_rollback()
            pass
            
        "...It sounded like fun!":
            $ released_fix_rollback()
            $ change_base_stat('c', 3)
            pass
            
        "...He wasn’t quite sure himself…":
            $ released_fix_rollback()
            pass
        
"Besides, he hadn’t forgotten her promise."

sha "{i}...And if you do attend, I will make it worth your while. I can do things you could only dream of your wife doing.{/i}"

"Now, here he was, with Shaya standing in front of him, holding a box filled with elaborate disguises."
"The changing room was a large and elaborate hall filled with tall mirrors on every side. Locked metal trunks lined the walls, each labeled with the name of a particular courtesan. An armory for a different kind of warrior."

sha "It is a costume party, Sir Rowan. Always popular. Anonymity and pageantry in the same gimmick."
sha "It wouldn’t do for you to traverse through such a sensual affair dressed in your field dress, rugged though you look in it."

show rowan necklace neutral at midleft with dissolve

ro "I like this outfit."

"Shaya just shook her head at his rural intransigence."

sha "-And I like my standard ensemble. But, it wouldn’t be wise for me to wear it while visiting a nunnery."

"Rowan had to pause to consider what she had said. Just how many situations had he stumbled into wearing this same tunic, especially since first arriving at Bloodmeen?"

ro "You’d be surprised by all the places I’ve managed to get into while wearing this."

sha "Oh, I have no doubt."

"She returned to a nearby cabinet and rifled through it. Rowan was left to squirm on the bench, waiting in dread for her return. When she finally did, her arms were filled with a mountain of fabric."

show rowan necklace shock at midleft with dissolve

ro "Priestly robes?"

"She set out the costume for him. The long, flowing robes of blue were the vestments of a Solansian priest. But this particular one was unique, towering habits on male robes were a unique feature of the sect in Qerazel." 
"Between it and the jeweled white mask she’d selected for him very little of his features would be visible. "

sha "I am sure you can see the irony in the selection."

ro "Is that...a hole in the crotch? Really?"

"He poked a finger through a well disguised slit in the robes."

sha "Made for ease of access. This is a brothel, after all." 
sha "I can find another costume if you would prefer, Rowan. Your pleasure is a gift to me. But, I fear you would find most of the other options… similarly disagreeable."

show rowan necklace angry at midleft with dissolve

"Rowan sighed softly. There was no backing out of his promise now. Shaya’s reward at the end had better be worth it."

ro "Don’t tell Jezera about this."

sha "You understand, of course, that I cannot promise that."

"Rowan sighed."

#cg 1
scene cg881 with fade
pause 3

"In some ways, the party remembers the kind of nobleman’s get-together that he so loathed in Rastedel. But, those didn’t normally have a fuckpit with dozens of people giving each other oral sex in a circle. One mouth to their neighbor’s crotch."
"Normally, the brothel was a maze of small rooms created by dividers and screens. But, for this occasion, the floor had been cleared into one large hall with hallways off to the side. And in the center was where the carnality was happening."
"In one corner of the sultry bordello, two of the courtesans had stripped naked and were engaged in a long drawn out kiss with one another. From the small group of men gathered around them, this was clearly for the patrons’ benefits. "
"One man approached them and produced two pairs of wrist cuffs. Moments later, the girls resumed their provocative display...only now with wrists behind their backs."
"In another segment of the pit, a masked lady wearing a poor mockery of a serving wench’s outfit was busy riding a male courtesan as though he were her saddled steed. Another man approached behind her and kissed her neck, eliciting a low groan from her."
"Other pairings could be seen everywhere, cast about like leaves in autumn. Two masked men had dragged a bed in from one of the private rooms and were in the midst of using each other for their personal pleasure." 
"Next to them, a male courtesan was slamming his shaft into a woman wearing a large fur mask meant to represent a bunny rabbit. But, the most interesting element was the man, dressed identically to her, being used as a piece of furniture in their fornication. Perhaps her husband?"
"Yet, during this entire affair, Rowan was..."

menu:
    "Accompanying Shaya.":
        $ released_fix_rollback()
        #cg2
        scene cg882 with fade
        show rowan necklace neutral behind cg882
        show shaya happy behind cg882
        pause 3

        "Rowan stood on the periphery, taking in the scope of this strange scene. Not so distant that he couldn’t always see and hear what debauchery was going on. But, not so close that someone might try to drag him into the festivities. Shaya, who he was arm in arm with, acted as his guide."
        "She was dressed in an erotic mockery of a wedding dress. It was white and flowing, with a long skirt. But the breasts and crotch had been cut out, along with the sides. Her normal red veil was replaced with a similar design in white."
        "She had a strange ability to navigate the chaos. She always knew where the intertwining bodies were to sidestep them. Or else knew the exact path to circle towards one of her girls to check up on them. The swordsman in him respected it."

        if orciad_ally == "batri":
            "Such a sight was a debauched one, beyond all doubt. If they reminded him of anything, it was the fuck pits of Batri’s tribe. But, where those had been brutal, careless, and inelegant, this was more… indulgent."

        elif orciad_ally == "ulcro":
            "Such a sight was a debauched one, beyond all doubt. If they reminded him of anything, it was the fuck pits of Ulcro’s tribe. But, where those had been brutal, careless, and inelegant, this was more… indulgent."

        elif orciad_ally == "tarish":
            "Such a sight was a debauched one, beyond all doubt. If they reminded him of anything, it was the fuck pits of Tarish’s tribe. But, where those had been brutal, careless, and inelegant, this was more… indulgent."

        elif avatar.corruption < 31:
            "The sheer taboo on display saw Rowan frequently covering his eyes or averting his gaze in embarrassment. How had he let himself be talked into this?"
            
        else:
            "Rowan found himself stealing glances at different corners of the room. Such raw, sexual degeneracy on display... If they hadn’t wished to be seen, they wouldn’t be at an orgy, would they?"
            
        "He turned back to the host of the affair, grinning like a mischievous cat at his side."

        if avatar.corruption < 31:
            ro "You didn’t say it would be quite so…"
            sha "Overwhelming?"
            ro "Yes."
            "She warmly rubbed his upper arm. It would have been almost a romantic gesture if not for the man in the goat mask fucking a prostitute mere inches away from them."
            sha "Worry not, my friend. You needn’t participate in any of the festivities if you are not comfortable."
            ro "No one will find it strange if I stay back?"
            sha "They will assume you are here simply to…spectate. You would not be the only one."
            "She gestured towards one of the back walls. Several masked men, and one woman, were indeed lurking on the periphery, their eyes locked intensely to the hedonistic orgy. One was stroking his cock through his costume."
            "Rowan stared back at them silently."

        elif avatar.corruption > 60:
            "Rowan smirked."
            ro "You do this often?"
            sha "As often as such  things can be arranged. In practice, every fortnight or so. Why do you ask?"
            ro "No reason. Perhaps I simply want to attend another, one day."
            sha "She gave a slight bow. For a moment, he was reminded of that deep bow she’d greeted him with when they’d first met..."
            sha "For you, hero, it can be arranged. I am {i}always{/i} at your service."

        else:
            sha "You look like you’re enjoying yourself, friend."
            "Through the veil, Rowan was sure she was smirking. He averted his gaze. Though, in the process, he caught an eyeful of a man in faux-knight armor devouring fruit from between a courtesan’s bosom."
            ro "I’m not. I’m just curious. I’ve never been to this sort of… ‘thing’ before."
            sha "Curiosity can be a healthy thing, Sir Rowan. And there are many ways to sate it during a party such as this."

        "The longer he stayed, the fuzzier his head seemed to become. Perhaps it was the overwhelming smell of cum bursting through even the masking incense. Perhaps it was the dizzying array of bodies pressing against bodies." 
        "Their meandering journey through the degenerate fornication became a surreal tour. She led him to the back of the hallway, some distance from the pit. They were left somewhat alone. Shaya pulled close, her lips leaning up to whisper into his ear."

    "Investigating on the side.":
        $ released_fix_rollback()
        scene bg25 with fade
        show rowan necklace neutral at midleft with dissolve
        "...far away from where the main action of the orgy was happening. He’d found a place along the side walls, where he could observe."
        if avatar.corruption < 31:
            "His lip curled into a slight frown as he watched. He was too used to Bloodmeen to be truly shocked by such a display. But, he had yet to shake the discomfort of watching men and women so wantonly and openly engaging in sexual depravities."
        elif avatar.corruption > 60:
            "Rowan took a few moments here and there to oggle the scene. There were more important things he could do with his time than cavort around a sex pit. Yet, even he had to admit that it looked like a good time. Perhaps if he wasn’t here with a goal..."
        else:
            "He watched expressionless. Even by Bloodmeen standards, this was a pit of seuxal immorality and hedonistic decadance. Yet, he’d grown too hard-hearted to let such things affect him. Even at their most overwhelming."
        show shaya neutral at midright with dissolve
        "Shaya, of course, was making her rounds through the party, stopping to glad hand with men and women who were of seeming importance. Rowan observed her from a distance, taking note of her particular approach to ingratiating herself with the wealthy and powerful."
        "But, most of all, he took note of where her attention lay. A distracted Shaya was a Shaya who couldn’t stop him from exploring. It was only when he was absolutely sure that she was distracted that he made a beeline for the back hallway."
        hide shaya with dissolve
        "As he entered the hall, he took a moment of pause to consider his next step." 
        "There was Shaya’s private room, of course. Though, he’d had several chances to look inside there already. There was also the room filled with mirrors and trunks where the courtesans changed." 
        "Finally, there was that padlocked door. He’d never gotten a chance to explore that room yet. A juicy target."
        if shayaClue15:
            "On his last stealth mission back here, he’d tried the door, but it simply was too difficult a task to break through. But, this time Rowan was prepared."
        "When Shaya had helped him change, Rowan had made absolutely sure she wouldn’t find the lockpicks he was sneaking in."
        "The moment he reached the door, he set to work with the picks. He worked as fast as he could...but not quite fast enough."
        show rowan necklace neutral at midright with moveoutright
        quest "Hello? Is someone back there?"
        "Rowan turned quickly, and found a woman dressed in a luxurious black bustier. She held an oiled black riding crop in one hand. The look was completed by a mask in a grotesque shape. An artistic rendering of a demon."
        if avatar.corruption > 30:
            "She seemed like one of the courtesans. Perhaps a specialist for customers with a kink for masochism."
        quest "You’re not on the staff, ain’t ya? Why are you back here? This is a restricted area."
        show rowan necklace happy at midleft with dissolve
        "Rowan swore under his breath, but his composure appeared steady behind the layers of his costume. That he was dressed as a guest was his greatest advantage."
        ro "Oh? You mean the lavatory isn’t back here? My word, this place is like a maze!"
        quest "A lavatory? That’s all you’re looking for? I tell you, you went in the {i}total{/i} wrong direction. Let me give you the real directions."
        "A minute later, a less than successful Rowan was marching back into the general floor of the brothel. The courtesan in the demon mask waved him off politely."
        hide rowan with moveoutleft
        "But, once he was gone, the form of the courtesan began to shift into one that Rowan might have found more familiar."
        show jezera displeased at midleft with dissolve
        je "Rowan, Rowan, Rowan. Now what were you doing back here?"
        je "Ugh, and right as I was starting to enjoy the party..."
        hide jezera with dissolve
        show rowan necklace angry at center with dissolve
        "Still seething from the disappointment, he took the chance to scout around the edges of the room. But, his quiet contemplation on how to return to the back rooms was spoiled by another of the patrons. It was an elderly man wearing an elaborate golden headpiece."
        patron "This is your first time at one of Shaya’s parties, young man?"
        ro "How did you know?"
        patron " Because I have eyes. And they happen to notice that you’re out of place here. You look like you’re standing on the edge of a sludge pit, trying not to step in anything."
        patron "Ehehe. If you knew what you were doing, you’d be trying to step {i}in{/i} the sludge."
        ro "If you’re so experienced, why are you off to the side with me?"
        "The man smiled faintly."
        patron "I told you, didn’t I? I have eyes. I’m partaking in my own way. Ehehehe."
        ro "..."
        "He glanced at the wizened old man. His dark skin suggested his Qerazeli origin. And he was clearly familiar with Shaya."
        ro "So I take it then, you’re familiar with Shaya’s parties."
        patron "Oh yes, she’s an excellent host. The best in the city. She stopped for a time, after she left the {i}Empress{/i}, but she’s been even better since going off on her own. Excellent entertainment indeed."
        show rowan necklace neutral at center with dissolve
        ro "You sound knowledgeable. I take it  you attend many...rendezvous like this?"
        patron "Oh yes. If you ever want to know where the latest festivities are, you go to my old bones."
        ro "And you’ve been doing this for many years?"
        patron "Ehehehe. You could say that."
        ro "..."
        ro "How long has Shaya been throwing events for? Is she a newcomer?"
        ro "How long has…"
        patron "Oh. Yes."
        patron "Quite new, but the best talent in a decade. At least. She must have had her debut, a few years back now.. Though, it was a rather strange occasion, wasn’t it?"
        "The old man scratched the flakey top of his head. A suddenly interested Rowan’s posture instantly straightened."
        ro "Strange how?"    
        patron "Well, a normal debut happens after word of mouth has taken time to go around. You always know who the next girl the empress is going to debut will be. But, one day they announced Shaya’s debut. No buildup. No word of mouth."
        patron "Of course, she did marvelously. She’s quite the charmer, eheheh. But, still. strange that she just appeared the way she did...."
        $ shayaClue17 = True
        $ shayaClueScore += 1
        show shaya neutral at midright with dissolve
        "Before he could go further into it, who should appear but the subject of conversation herself?"
        sha "Ah, that’s where you wandered off to. I had been worried you’d be lost in the entertainment. It can be hard to find a man who doesn’t want to be found."
        "She was dressed in an erotic mockery of a wedding dress. It was white and flowing, with a long skirt. But the breasts and crotch had been cut out, along with the sides. Her normal red veil was replaced with a similar design in white."
        "She wrapped her arms around Rowan’s arm, the bare breast of her costume ensured that plenty of sensation made it through the layer of fabric. The patron he’d been speaking to certainly noticed. His eyes had  widened slightly."
        patron "Ah it seems you’re acquainted after all. I’ll leave you to your fun then. Unless you decide to take it in public, ehehehe."
        "Shaya bowed softly to the man."
        sha "M'lord."
        "Ultimately, Rowan had little objection to rejoining Shaya at this point. His ploy to get into the locked room had been a failure. But, at least he’d come away with something..."
        "Besides, accompanying Shaya was enjoyable. She was always quick to lavish praise on him. And, of course, she was never shy about bodily contract. "
        
    "Participating in the fun.":
        $ released_fix_rollback()
        scene black with fade
        show rowan necklace aroused behind black
        "...in the middle of it. The story of how he went from voyeur to participant was a slow one. It started with eager observation, turned to growing lust, and then to indulgence in curiosity."
        "Being on the receiving end of a sensory deluge so obscene had a curious effect on the mind. Perhaps it was the smell. Perhaps it was the impersonal nature of so many people together doing things that’d be unspeakable in the society he grew up in."
        "After a dizzying array of time, Rowan found himself on one end of a large ornately carved table. On the other end was another masked man."
        "And between them, strapped down to the surface, was a squirming, naked woman. Her only covering was an obscene mask in the shape of a comical whore. With a single hole at a pronounced pair of lips." 
        "Rowan had lined himself up in front of her face, while the other man was positioned between her legs. Rowan’s cock had been pulled out from the front of his robes. Ease of access, indeed."
        "Then, at the exact same moment, they plunged into her. Rowan into her mouth hole, and the other man into her rear end. Together they set to work on her. Pumping their hips together at the same time. The force of being caught between them got the courtesan gagging and dancing."
        "Rowan blinked twice. His head was pounding. Was it all the smoke?"  
        "He wanted to keep going...He wanted to see what he could do to her." 
        "His cock rammed down her throat over and over again. The mask stripped away every part of her face that wasn’t fuckable. He held her by the throat to keep her lined up perfectly. The whore sputtered on his cock, saliva running down her lips."
        "Her body thrashed like an animal. She was being pounded from the front. Pounded from the rear. The bonds on her wrist held her down."
        man "Yeah. Fucking slut. You don’t deserve it in your pussy. Right there."
        ro "..."
        "His head was pounding...he just wanted to see more."
        "The pleasure helped guide him forward. There was no skill to the blowjob. No technique. Whatever abilities she had were trapped behind the restraints and the mask. Instead, Rowan felt the obscene derogatory pleasure of using a woman as meat."
        "The same process spared him. The mask shielded him with anonymity. No observer  could see that Rowan was the one doing this. He could have been anyone. He was no one."
        "His mass went down her throat. And she took it. He moved his body. And she took it. In the moment, she was less of a person and more of an instrument of masturbation."
        ro "..."
        whore "Mmph!"
        "Her body thrashed beneath him. She must have been in a state of total over-stimulation. The subject of brutal fucking to her rear and her throat at the same time. The other patron had begun to slap her crotch every time she moved, only adding to the intense frenetic energy of the moment."
        "Rowan breathed in the lustful air. Others were engaged in depravities behind him...to his sides...all around. It took on an inevitable quality, like the turning of the wheel. Men getting fucked. Women getting fucked. Moaning. Panting. Screaming."
        "So easy to keep on going...All the way too…"
        ro "Grru-"
        "He took a step back, involuntarily. His leg had begun to shake wildly, right as the inevitable conclusion came to him. As his cock pulled free, a fountain of seed shot into the air. It landed across the length of the woman’s mask. It splattered the entire surface with his presence."
        "Yet, there would be no rest for the girl. Even as he stepped back, another man rushed forward into his place. One plug for the hole replacing another."
        "He stumbled further backwards, panting rapidly. The woman strapped to the table let out a long moan, that only sputtered weakly past the man’s cock. From the way shakes ran over her body, Rowan must not have been the only one who reached his peak."
        scene black with fade
        show rowan necklace aroused behind black
        show jezera happy behind black
        show shaya happy behind black
        "His vision slipped in and out of focus. Time seemed to pass, without any input from him. For a moment he thought he saw Jezera’s face staring at him from the crowd. Judging him."
        je "I knew this was what you really wanted, Rowan... "
        "He found himself reclining in a disheveled heap on a cushion. To his side, there was something soft and warm pressing to him. "
        "His eyes turned to the presence and found something not altogether unsurprising. The large breasted bosom of a woman who was barely paying attention to him." 
        "She was blowing rings of smoke from the end of a strange long pipe with a watery basin at the bottom."
        ro "...hrmm…"
        "Just how long had he been out for?" 
        "He returned to his legs and found strength had returned to him. And as he surveyed the lustful display in the center of the room, he found his member hardening again. Long enough to have made it through his refractory period, it seemed. "
        sha "Ah, once more you’re found. I had worried that you might never have been found. {i}Jezer’aca{/i} would be most displeased if she lost her steward."
        "Shaya was dressed in an erotic mockery of a wedding dress. It was white and flowing, with a long skirt. But the breasts and crotch had been cut out, along with the sides. Her normal red veil was replaced with a similar design in white."
        "Rowan put a hand to his mask, straightening it."
        ro "Water."
        sha "Of course, follow me."
        scene bg24 with fade
        show rowan necklace neutral at midleft with dissolve
        show shaya neutral at midright with dissolve
        "He followed Shaya, first to refreshments, and then treading along with her as she struck up conversations with some of the guests. But, Rowan’s head was still in the sex pit."
        "For a moment everything had been so...so…"
        "Well, it seemed he now understood the appeal of a party such as this, at least."
        sha "Surely your prior pleasures didn’t take too much from you, my friend. A man who gorges on the appetizers may be left with insufficient room for the main course."
        "Rowan let his eyes drift down Shaya’s body, from the exposed breasts on her wedding outfit, down her naval, all the way to her thighs. The renewed stirrings he’d felt earlier blossomed into something more."
        #ro smirk
        ro "I assure you, my lady. I have room for more."
        sha "{i}Good.{/i}"
        "And so, they continued on through the soiree, Rowan at Shaya’s side from them on. Where she went, he went. Until…"
        $ change_base_stat('c', 10)

sha "Stop for a moment, if you please…"

scene bg24 with fade
show shaya happy at center with dissolve
show rowan necklace concerned at edgeleft with dissolve

"She motioned with her eyes towards a bench near the edges of the party. A dark skinned older man was stationed on it, dressed in an immaculate lion outfit with strands of gold woven in. The gaudy costume was a stark contrast to his wrinkled, aging body."
"He watched the debauched proceedings with a faint grin. The younger man in the tiger costume to his side, however, was leaning forward with his jaw open. He was enraptured by the bodies in motion. A courtesan stood by their side, filling the man’s wine cup."

sha "That is Lord Magistros Lirio. Very important in the Imperial Bureaucracy. Along with his son, it looks like! It would be bad form for me not to give him some attention."

"She led Rowan, arm in arm, towards this most high ranking of guests."

show rowan necklace neutral at midleft with moveinleft

sha "My friend, you made it! I was worried that we wouldn’t be blessed with your presence today. It would have turned our joy to ashes."

"The wrinkled man flashed her a pleasant smile."

lirio "The woman of the hour! Ah, those pretty tits are a sight for these old eyes. After you departed from Qerazel, I had been worried that would be the last I heard of you. Would be such a shame. Such a shame."
lirio "And here you are putting on your own events. I knew I just had to come and see for yourself. "
lirio "And my word, it’s not a disappointment. The little show from the start? The one with the girl covered in milk? Oh, that was ingenious. The only improvement this foggy old brain could imagine would be if you’d been the performer."

sha "Still, I suppose my presence could add a certain spice to the display. Perhaps I will have to consider including a more personal performance at my next event."

"She poked the old man’s cheek playfully."

sha "But, you forget who you’re speaking to. I’m the madam now. Aren’t such affairs more for the peons?"

lirio "Do Madams still make house calls though? Now that you’ve resurfaced, I know quite a few friends who’d be eager to get some of their missing fix, eh?"
lirio "What say you, girl? I could arrange a ferry to come to the island and pick you up?"

"Shaya bowed slightly and then she took a seat on the bench. She gestured for Rowan to sit by her side."

sha "That would be most kind of you, sir. However, I do not think I could make particularly many such trips. I am deathly afraid of the sea."

lirio "Oh? Is there a story there?"

sha "Not an interesting one, I fear. My friend and I were invited aboard the yacht of a nobleman who proved less than capable as a seaman. I was left with quite the scar to prove it too."

"The Magistros frowned slightly."

lirio "Seems an odd thing for a woman with such a potent fear, to surround herself with water."

sha "But, my lord magistros. Odd women are the best sort. Don’t you agree?"

"Rowan watched silently. He could see the Magistros’ intentions clearly on his face. Shaya was dancing around the true question."

lirio "Tell me, surely I am too late to buy you for the night, yes?"

"She brushed a soft hand up his arm. Faint teasing touches."

sha "You are. You may have noticed my silent friend? He is quite a fan of mine. There was no chance of anyone beating him to the prize."

"Lirio glanced to the side at Rowan, finally acknowledging his presence. His frown grew."

lirio "Must have quite the coin purse to do so. Tell me friend, are you someone who I should be getting to know better?"

"But, Shaya leaned forward, blocking Rowan’s face."

sha "Earlier he told me that he’d prefer not to speak tonight. Suffice to say he is from a profession where it would not be looked upon...kindly if even rumor were to escape."
sha "..."
sha "In fact, would you be so generous as to excuse me for the briefest of moments?"

show rowan necklace neutral at edgeleft with moveoutleft
show shaya neutral at midleft with moveoutleft

"Without a further word of warning, Shaya ushered Rowan to his feet and nudged him over to a side corner where they could speak more freely."

sha "I will remain and speak to Lirio for some time more. Ply him for what secrets I can get. Once I have him behind closed doors with a succubus, I will find you."

if avatar.corruption < 31:
    "Rowan looked around, barely able to hide his discomfort. To be alone at an event like this...it was not something he was especially comfortable with…"
    
else:
    "Rowan looked around. As fascinating as this event was, for an outsider like Rowan it was one easier to get into with a guide…"
    
show rowan necklace angry at edgeleft with dissolve

ro "Seems rude to leave me here by myself considering all that time you spent begging me to come."

"She giggled softly into her hand."

sha "It is a party! I am sure you can find something entertaining. Consider it practice in networking. A valuable skill for someone in your line of work."
sha "Simply seek me out afterwards. I have not forgotten what I owe you. Tonight, I’m yours, after all…"

"Shaya turned her back to him and started back towards the Magistros. But, before she could go far, there was something Rowan considered. A moment from the prior conversation that struck out to him."

show rowan necklace neutral at edgeleft with dissolve

ro "...Wait."
ro "Was the story about the boat true? Or were you just making an excuse to not pay him a house visit?"

sha "Hm?"

"She turned her back to him and tilted her head."

sha "An excuse, but one that really happened. I simply left out Jezera’s role in the whole...affair."
sha "Now then. Do try to enjoy the party. If you attempt to indulge, you might be surprised by how enjoyable it can be."

hide shaya with moveoutright

"She brought her veil to the cheek of Rowan’s mask and planted a kiss on it. Rowan couldn’t feel the warmth from her lips, but he did notice the soft press of cold porcelain against his cheek. Then, with a wink, she made her way back to Lirio."

if shayaClue7:
    "Rowan stood in place, watching with a skeptical eye."
    "This Lirio man was clearly of some importance. That she had chosen Rowan as her partner for the night and not Lirio seemed almost a dereliction of duty, if collecting knowledge was the goal."
    "So, why bother with Rowan here? Perhaps she was not being truly honest when she professed to genuinely want to spend time in his company."
    "He shook his head."

"Rowan wandered around lost. He was a stranger in a strange land. There was no one whom he knew, and it would be hard for him to make a new friend when everyone was too busy slapping bodies together."
"He looked back to Shaya and Lirio. Another girl had joined them and was whispering something into Lirio’s ear, while Shaya had placed herself by Lirio’s side." 
"With a sigh, he turned away. The wait was one thing, but the attention she was showing to this other man produced a different set of emotions entirely. He knew that no man could lay exclusive claim to a courtesan."
"Still, she’d made him a promise. She actually intended to come back and show him {i}“things you could only dream of your wife doing”{/i} right?"
"Right?"

menu:
    "Get annoyed at being brushed off.":
        $ released_fix_rollback()
        $ lirioConfront = True
        show rowan necklace angry at midleft with dissolve
        "Rowan’s eyebrows narrowed. He really had been left here entirely on his own, hadn’t he?"
        "Well, there was no way he was going to just stand for that. She made him a promise and she was going to deliver on it. "
        show shaya neutral at midright with dissolve
        "He boldly rose to his feet and returned to where she and Lirio were reclined. The fat Magistros hailed his return, but Shaya raised an eyebrow skeptically. "
        ro "I apologize for interrupting. But, the woman has a certain contract with me she needs to fulfill. So I’m going to need to take her back."
        sha "Hmmm?"
        "He grabbed her by the arm and pulled her gently from the older man’s lap. He gave Rowan a quizzical look but didn’t offer any immediate protestations."
        sha "Ah, apologizes, my friend, but I’m just going to be a minute longer with Lirio- "
        "Rowan pushed her into the wall. The wall rattled with a slam from the force of it. She gasped softly, but demurred her head to the side. She offered no resistance as he forced her wrists together above her head."
        ro "No minutes longer. You’re mine tonight, Shaya. That’s the promise you made me. It’s cruel to keep me waiting."
        "Rowan made out a twist of her lips beneath her veil. Was that a smile? His focus was so intensely focused on her that he hadn’t noticed just how many people had stopped to look at them."
        "It seemed one could not go about manhandling the hostess without drawing interest."
        lirio "Ah, he hasn’t started to bother you, has he {i}tsorachi{/i}? If you need help, you have only to-"
        show shaya happy at midright with dissolve
        sha "Not at all!"
        "Her voice came out in a delighted sing-song."
        sha "My friend here is just {i}forcefully{/i} showing how eager he is for later, isn’t he? It seems I’ve overestimated how patient a man he is. "
        "She leaned forward as much as Rowan’s grip would allow, pressing her lips to his ear."
        sha "{i}But, perhaps I am a less patient woman then I appear.{/i}"
        show rowan necklace happy at midleft with dissolve
        "She turned back to Lirio. He, and the others nearby, visibly softened once it was clear that Shaya did not seem genuinely in trouble."
        sha "I must apologize most sincerely, Magistors. I would but stay and talk longer, but it seems that duty calls."
        "The man rolled his eyes."
        lirio "Go. Go. Give the impatient lad what he wants."
        "Rowan didn’t wait a second longer. Rather than let go of her wrists, he used them as a handle to drag her along behind him. Shaya followed along, giggling and not making the slightest effort to wrench herself free from his grasp."
        sha "So eager...And all for a humble girl like me…."
        "A few noticed them pass as he pushed his way to the attendant desk and the door behind it. But, for the most part, they didn’t let this little disturbance interrupt the party."

    "Accept the wait.":
        $ released_fix_rollback()
        #cg1 var 3
        scene cg883 with fade
        pause 3
        "With a sigh, he let his shoulders settle. He’d waited some time already. Surely he could be patient until she was done with her job."
        "In the seat next to him, a woman was being eaten out. She was naked save for a jeweled blue mask with peacock feathers emerging. The man between her legs was naked, safe for a gold collar around his neck."
        if rowanGaySex > 2:
            "Rowan’s vision settled back on the two men in the bed. The smaller man was groaning while bouncing up and down atop the cock of the one under him. A third man had joined in and was suckling on the nipples of the man on bottom. The entire pile had turned to a heap of groaning."
        else:
            "Rowan’s vision settled back on the two courtesans pleasuring each other for the erotic amusement of the spectators. Now, a golden double sided phallus has been placed between them with both their bodies in doggystyle pose."
            "The girls moaned loudly as they threw their asses backwards towards each other. The wet sound of slapping ringing out with each movement."
        if avatar.corruption > 30:
            "Rowan felt his cheeks grow red underneath his mask. He didn’t realize it, but there was another bodily reaction happening too…"
        else:
            "Rowan sighed. It was no surprise that such a cavalcade of erotic sights was having an effect on him. A bulge had started to form beneath his robes"
        #cg2
        scene cg884 with fade
        show rowan necklace neutral behind cg884
        pause 3
        court "I could help you with that, Sir?"
        "He looked down. His cock was semi-hardened and sticking out of his robes. He briefly remembered the slit in the costume he’d discovered before."
        "The courtesan knelt down by his side. She was dark skinned and relatively young. Even in the low light, he could make out her dimples." 
        "Her dress was comical, yet provocative. A skimpy blue silk robe in an elvish style that showed her entire body. The look was even completed by obviously fake elvish ears."
        if avatar.corruption < 31:
            "Rowan shook his head."
            ro "You don’t have to do that if you don’t want to, girl."
            court "It’s what I’m here for."
        else:
            "Rowan grunted."
            ro "I suppose you’d be quite good at it, huh?"    
        ro "You’re one of Shaya’s girls, right?"
        show cg885 with dissolve
        show rowan necklace neutral behind cg885
        pause 3
        "The girl nodded slowly. Her hand slowly crept over towards his waist."
        menu:
            "Stop her.":
                $ released_fix_rollback()
                $ orgyHJ = False
                hide cg885 with dissolve
                show rowan necklace neutral behind cg884
                pause 2
                "Rowan grabbed her wrist softly when her hand was mere inches away. He shook his head softly."
                ro "Just talk."
                "He let her hand go, and it returned to her side. She nodded slowly."
                court "If that’s what you would prefer..."
                "Rowan eyed her exposed body, though kept his glance away from more intimate places. The tone of her skin stood out."
                
            "Let Her Continue.":
                $ released_fix_rollback()
                $ orgyHJ = True
                show cg886 with dissolve
                show rowan necklace neutral behind cg886
                pause 3
                "Rowan did nothing to impend her progress. He grunted softly as her fingers wrapped around his shaft. If it had been slowly growing erect before, now it was starting to strain."
                "She took a few seconds to work into it before her motions took on a regular pumping pace." 
                "She was good at it, as was to be expected of a woman in her profession. She was careful not to hurt him, but still held firm enough to provide plenty of pressure where it was needed most."
                "He eyed her breasts, making note of their unusually dark complexion."

        ro "Where are you from? Not from Qerazel, I assume?"
        court "Hehe. Can’t you see that I’m an elf?"
        ro "No, really. Are you from Qerazel?"
        court "..."
        court "Okay, okay, I am from Qerazel. City girl, born and raised. Don’t worry, Sir. Lots of people make that mistake. Skin tone and all. My parents were from the Dragon’s Tail."
        ro "Hrmmm…."
        if orgyHJ:
            "He shivered slightly. The softness of her skin was electric. His hips shifted so he could feel even more as her hand continued its motion."
            "His body started to recline, and his breathing sped up. It was not just the sensation of being masturbated by this girl. The sights, the sounds, all of it was erotic. All of it produced an air of lust that swept him up too."
            court "Just relax sir. Let me take care of you. It’s a party. You should enjoy yourself."
            "She looked him in the eye, even as she spoke. She might not be able to see behind his mask, but that form of intimacy, at least, was still available to her."
        else:
            "Rowan slowly tucked his cock back in his robes as they spoke. She glanced down at it but quickly darted her attention back up towards his eyes. The only part of his face not hidden by the mask."
        if shayaClue6:
            "...And as he looked at her, a thought nibbled on his brain. Something he had not truly considered until now…"
            "She was not wearing a veil over her face. He could see it, dimples and all. In fact, none of the other courtesans seemed to be wearing anything similar."
            menu:
                "Ask about Shaya’s veil.":
                    $ released_fix_rollback()  
                    ro "Wait."
                    if orgyHJ:  
                        #cg2
                        hide cg886 with dissolve
                        show rowan necklace neutral behind cg884
                        pause 2
                        "Rowan placed a hand on her wrist and stopped her hand’s movement. He groaned slightly at the sudden absence of stimulation."
                        "But, for this brief moment, his curiosity outweighed his lusts."
                    court "Hrmm?"
                    ro "You aren’t wearing a veil over your face? Is that not just what courtesans from Qerazel wear?"
                    "She tilted her head."
                    court "Like the Madam, you mean?"
                    court "Some special girls learn dances involving veils. But, even then, it’s just for the performance…."
                    court "You may have heard gossip about it back in the city? Hehe. There is a rumour that beneath the veil, she hides powerful fangs."
                    "Rowan would have scratched his chin if there had not been a mask in the way. The more he learned about Shaya, the stranger she seemed."
                    ro "Do you believe these rumors?"
                    court "Of course not. She’s a good madam."
                    ro "..."
                    if orgyHJ:  
                        ro "Continue."
                        #cg2 var 1
                        show cg886 with dissolve
                        show rowan necklace neutral behind cg886
                        pause 2
                        "Rowan pulled his hand away, allowing her to resume the process of working on his shaft."
                        $ shayaClue11 = True
                        $ shayaClueScore += 1
                        
                "Ignore it.":
                    $ released_fix_rollback() 
                    "Rowan shook his head. It was a fascinating question, of course, but this really was not the situation to ask such a thing…"

        "But, as the minutes ticked by, Rowan began to feel restless. He was with this girl, and should have been paying attention. But, something else was on his mind."
        if orgyHJ: 
            "It wasn’t that the girl was bad at giving pleasure. Far from it. But, the touch of her hand was almost an appetizer. When the promised special encounter with Shaya was so close, how could he truly be happy with her touch?"
            "He grunted and moved to her rhythm, but he soon started to daydream of what he would do with Shaya afterwards. For now, he had to settle with a lesser copy."
            "Then and there, Rowan decided to rise to his feet. The girl staggered backwards, clearly not expecting her actions to be interrupted."
        else:
            "The girl was still trying to flirt with him. But he hadn’t come here for her. The more she hinted at touching his cock, the longer the wait seemed to grow."
            "Perhaps Shaya was done by now?"
            "With a gentle hand, he pushed the girl back. It allowed him the space to rise to his feet."
    
        court "Have I done something to displease you?"
        ro "Of course not. You’ve been excellent entertainment. But, I have reason to believe I’m going to be with my date again very soon."
        court "Of course, sir. I hope you enjoy yourself…"
        scene bg24 with fade
        show rowan necklace neutral at midleft with dissolve
        show shaya happy at midright with dissolve
        "He found Shaya back where he left her on the bench. But, the Magistros had already departed, along with the succubus whom Shaya had sent to speak to him. Now, she was half curled up with the man’s scrawny son whispering into his ear."
        "When she saw Rowan approaching, however, she perked up in place."
        sha "Ah, my friend. I was right about to call on you. Your timing is perfect."
        ro "So you’re all done here?"
        sha "But of course. I have obligations I must meet with certain eager individuals, do I not?"
        "Rowan extended his arm to Shaya and she clutched it with the dainty courtesy of a lady at court. In that way, he led her back the entire stretch of path to her back room. Amidst the chaos of the orgy, they only had to walk around a modest few fornicated orgy-goers."
        
show rowan necklace neutral at midleft with dissolve

"It was only once they were back alone in her room that Rowan let his guard down. The dionysian insanity of the party rumbled through the walls, but the sounds didn’t penetrate in detail into this private space." 
"Rowan removed his mask and breathed a sigh of relief."

ro "Well now. I’ve been told by someone that I’m about to experience types of pleasures I’ve never experienced before. Am I about to be impressed?"

sha "I should hope so."

"She brushed against his shoulder. She pressed in close to his mask, letting her words come out in a purring whisper."


sha "I don’t think there’s much need to delay with further anticipation building, is there? We should remove some of this cumbersome clothing…"

show rowan necklace naked at midleft with dissolve
hide shaya with dissolve

"What followed was a chaotic dance of hands on bodies. Rowan’s on Shaya’s. Shaya’s on Rowan’s. One by one, every article of clothing found its way onto the floor. Rowan’s costume was discarded with thoughtless abandon. All that remained was Shaya’s veil."
"She beckoned him forward, leading him up to the concave in the back of her private quarters that formed a stage. Rowan had never been back here before, and thus never quite grasped how large private stage was." 
"It had already been prepared for his arrival. Two long silk curtains descended from the ceiling all the way down to the floor. Rowan had never noticed how large this area was before. "

show shaya behind bg24

ro "Why the new decor?"

sha "Patience, Rowan."

"For a fleeting moment, her hand brushed against his chest. He sighed involuntarily. But, before he could embrace her, she backed all the way to the set of hanging curtains." 
"That had to mean whatever she planned was about to begin. He slowly settled with his back along the wall and his arms crossed over his chest. But, his eyes never left her. Even now they traced the fleeting contours of her body."

scene cg910 with fade
pause 3

"But, his hungry gazing was broken by a sudden burst of movement that nearly made him lose track of the girl as she gracefully leapt in the air. Her movement defied expectation as she caught the strands in her hands. Her legs followed suit, wrapping themselves in the fabric."
"It was as if she was floating in the air."
"This, however, was only the beginning. A performance unfolded of limbs twisting in and out of the silk. It was astonishing to see the ease that Shaya was able to glide up higher without slowing or shifting the pace of her acrobatic dance."
"The flurry of movements stopped for a brief moment, and Rowan caught Shaya looking him in the eye over her shoulder.  It was the tiniest flirtation. A tease of what was to come. Then, her legs slowly spread into a wide split. It left her delicate places forcefully exposed to his eyes."
"Rowan shifted subtly in place, eyes transfixed on the provocative display. The elegance of the dance, contrasted by her shameless nudity, was surreal."

scene cg911 with fade
pause 2
show cg912 with dissolve
show rowan necklace naked behind cg912
show shaya happy behind cg912

"But, that had been merely a momentary pause in the dance. She brought her legs together and tumbled like a ball. It left her hanging upside down at eye level, but with her form so contorted that her feet rested on her hair."
"Rowan caught himself slackjaw, wondering just how flexible this woman was. Her mastery of the human body reminded him of a trained warrior."
"Without thinking, he stepped forward and placed a hand on her thigh. His manhood stood erect in the open air. The dance had only left him more eager, more frenzied. He wanted her now."

ro "That’s quite impressive...but I didn’t just come for another show. You made me a promise."

sha "This isn’t a performance where the audience must keep off the stage, Rowan. {i}You can do whatever you want to me{/i}." 

"She put herself right side up and pulled her body slightly higher. Her arms and legs wrapped themselves tight in the silk. The entire time, his hand never left her thigh. Now he could even feel the motion of her muscles as she controlled her movements."
"Shaya slowly uncurled backwards, bringing herself upright. Rowan’s hands guided her into proper pose. The pose brought Rowan's cock, strained to attention, pressed into her belly. He would have kissed her, if not for the veil."
"However, the momentary distraction made him realize how hard Shaya was breathing.  Perhaps, her dance was not as effortless as it first appeared."
"His thoughts turned briefly to foreplay. But such considerations soon proved moot when the folds of her sex brushed against his member. She was most certainly {i}not{/i} dry."

sha "Hold me tight…"

scene cg913 with fade
show rowan necklace naked behind cg913
show shaya happy behind cg913

"He drew her into a possessive embrace as Shaya lowered herself ever so slightly more.  A heartbeat passed and then instead of merely nudging against her, her tightness was wrapped about him."

ro "Eurgh."

"It was when their hips began to press together that Rowan saw the value of this pose. Despite the position, Shaya had full freedom of motion. She was held aloft by her own power." 
"So, when she moved, it was not merely in reaction to Rowan’s thrusting. She could fuck him with her own force. More than that, with gravity itself."
"Her hips twisted and bucked expertly, working down on his cock. The contractions and motions were like an assault of sensation striking right to the brain. He grimaced slightly, but dug his fingers deeper into her shapely hips."

sha "You...you like this?"

ro "It’s...it’s different."

"She leaned forward, nuzzling her face into Rowan’s neck. The sound of her soft panting rattled his ears. At the same time, her breasts rubbed eagerly against his naked chest, bringing with them their own pleasant mix of sensations."
"The curtains acted as a sort of anchor. She supported every motion with a corresponding movement of her arms. The power of gravity would always do the rest."

sha "Oh."

"As a result, she looked less like she was fucking him, and more like she was dancing in the air. Her arms and legs would shoot out and then retract together in strange patterns. It was almost beautiful."
"But, any appreciation for such aesthetics were not to last. When Shaya picked up her pace, it left him groaning. His own hips moved to match her pace. They were soon driven by a hungry animalistic energy. A contrast to the controlled waves she moved in."
"Only a moment later, Shaya did something he couldn’t have expected. She freed her arms and wrapped them around him. Delicate fingers wove through his dark hair. Sharp nails dug into his shoulder."
"Yet, losing the control that her arms gave her didn’t impede her abilities. She continued rolling and thrusting down with the same hammer-like intensity, only now directed only by her legs. The silk strands kept her body moving and gliding through the air."

sha "Oh! Oh!"

"Her eyes seemed to roll backwards. Even her toes curled into the silk. Whenever she slammed down on Rowan, it left him overwhelmed. But, what effect was it having on her? Surely with every thrust, she was taking his cock in deeper then her anatomy was designed for?"
"From outside, the constant low sounds of moaning and thrusting permeated through. The collective lust of the other patrons soaked in and drove their lustmaking to more animalistic places."
"Shaya drove his head close to hers. Her lips were separated from his ear merely by the fabric of her veil. Her voice came out in a  hoarse whisper."

sha "Rowan, I’m about to…"
sha "{i}Ah{/i}…"

"Her body shuddered and went still. It hung limply in the silk. But, Rowan was not done yet. He was already worked into a frenzy. His hands clung harder to her hips and slammed them down on his cock. Now he was finally commanding the motion."
"She shuddered with every thrust. Her eyes fluttered weakly. But, she continued fighting to stay in the moment. Her hips rolled and fell, only at a far weaker pace." 
"It was a small thing, but it drove him mad. The faint, honest reactions of her body. If a sight could be a feeling, it would have stroked his cock as hard as her lower muscles."

sha "Almost...{i}a-again{/i}..."

"Her body spasmed again. For a lingering tense moment, it looked like she might fall from her precarious place in the curtains. Her hand had to return to them to steady herself again."
"Rowan’s leg began to shake. This electric energy seemed to spread out all over his body, driving him towards a peak. Each heavy thrust into Shaya’s receptive body pulled it closer and closer."
"His eyes slammed shut."

ro "Eurgh."

show cg914 with sshake
show cg914 with sshake
pause 2
show cg915 with flash
pause 3

"Then, in a single motion, he pulled her down onto him as hard as he could, forcing his cock deep inside as he sprayed his cum into her hot,sodden cunt."
"Finally spent, he began to sink to his knees. From the corner of his eye, he saw Shaya roll limply down the chords of silk. She hovered mere inches above the ground for a moment...before letting her body fall to the wooden stage beneath."
"They lay there, panting and gasping. The sounds of the orgy faded from consciousness, even if Rowan knew it was still going on."

sha "It..it seems...you enjoy...ed that. Yes?"

ro "I can...heh...I can say the same about you."

sha "Is it...is it such a surprise...that I..I actually enjoy sex?"

"Rowan laughed as much as his breathless lungs would allow. He took another moment to recover before speaking again."

ro "I propose...we move this to the bed...unless you’re enjoying...the floor."

sha "Proposal accepted...but you have to carry me…"

scene black with dissolve
show rowan necklace naked aroused at midleft with dissolve
show shaya happy at midright with dissolve

"Rowan stirred briefly to see that there was still another body beside him in bed. Shaya’s beautiful femine form." 
"From the faint sounds from outside the door, the party was still raging. But, even now, she was still spending her time resting in bed with him."
"Despite himself, Rowan smiled."

#if Perception is above x (moderate difficulty mid game) - TODO
show rowan necklace naked at midleft with dissolve
"However, then something shook him, if only for a brief moment."
"His hand reached out and traced Shaya’s back. Her skin was so beautiful and soft, all in that warm shade of olive. It would be easy to just get lost in the sensations. "
sha "Mrrr... Rowan?"
ro "Rest more. I just wanted to touch you."
sha "Of course...feel away…"
"But, Rowan was not touching her body for enjoyment. He was looking for something. And the more he touched her skin, the more he examined her with his eyes, the more one thing became clear."
"Her back was near totally without blemish. It certainly didn’t have any scars or deformities."
sha "{i}...My friend and I were invited aboard the yacht of a nobleman who proved less than capable as a seaman. I was left with quite the scar to prove it too...{/i}"
"Had that been a lie after all? If so, why had she bothered to tell Rowan it was true? His stomach felt uneasy all of a sudden."
$ shayaClue12 = True
$ shayaClueScore += 1

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve

"It was only later, once Rowan began the morning march back to his room, that he had a chance to compartmentalize and go over what had happened. Even then, his head was still pounding."
"The party. The round of socializing with Shaya. The private session."

if shayaClue11 or shayaClue12 or shayaClue17:
    "It was certain that he’d have questions to add to his little investigation parchment."
    if shayaClue11:
        "{i}If Qezeli Courtesans didn’t wear Veils outside of performances, why did Shaya never take hers off?{/i}"
    if shayaClue12:
        "{i}If she claimed to have been scarred in the past, why was her skin near totally without blemish or marking?{/i}"
    if shayaClue17:
        "{i}Why would Shaya have gotten a debut if she had no pre-existing reputation?{/i}"

else:
    show rowan necklace aroused at midleft with dissolve
    "But, it was the last of those that hung most totally in his memory. The way her body had moved. Her seemingly endless skill in the sexual arts." 
    "She really was incredible, wasn’t she?"

return
