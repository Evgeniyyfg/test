init python:

    
    event('cla_nasim_quarrel', triggers="week_end", conditions=('nasimFirstVisit == False', 'nasimTF == False',), group='ruler_event', run_count=1, priority=pr_ruler)
    #TODO - Level one stealth required
    event('quarrel_follow_up', triggers="week_end", conditions=('claNasQuarrel',), group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="images/Backgrounds/library.jpg")
    #TODO - Perception Level 2
    event('counterfeit_coins', triggers="week_end", conditions=('week > 10','week < 60',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('counterfeit_consequences', triggers="week_end", conditions=('week > 60',), group='ruler_event', run_count=1, priority=pr_ruler)

label cla_nasim_quarrel:

scene bg14 with fade
show rowan necklace neutral at center with dissolve

quest "Three hundred gold, and you’ll deliver another batch next month."

quest "Three hundred fifty, and you’ll agree to buy the Desert Primrose as well, for two hundred total."

ro "Oh?"

hide rowan with moveoutright

scene bg19 with fade
show nasim neutral at midleft with dissolve
show clamin happy at midright with dissolve

nas "A steep price, though the product is no doubt of quality high enough to justify it. Which is why with some regret I must remind you I did not request any Primrose."

show clamin neutral at midright with dissolve

nas "I only need the Haleen Cacti, and I believe three hundred should not only cover the expense of acquiring it, but also leave you with a nifty profit of over seventy gold pieces."

show clamin sad at midright with dissolve

cla "If I was buying under the cloak of darkness, from a shady merchant in the back alleys, and did not inspect the product he was handing me, then maybe. But this is high quality stuff, straight from the main square!"
cla "Nasim, you know how much I’m investing in castle Bloodmeen. Three hundred fifty barely lets me cover the cost of the bribes! Any less than that, and I’m simply not breaking even!"

#nasim annoyed
show clamin neutral at midright with dissolve

nas "And yet somehow you return with two crates of Desert Primrose which I, again, did not request. A gift from a secret admirer, perhaps?"

show clamin happy at midright with dissolve

cla "Ah, funny that you ask, but no! It’s not thanks to me that we came in possession of this fine flower…"

show clamin at center with moveinright
show rowan necklace neutral at edgeleft with moveinleft

ro "How unlike of you to credit others with a successful transaction."

"Cla-Min greeted him a wide, if somewhat nervous smile. There were four crates by her side, and she was leaning against one of them. Nasim acknowledged him with a polite “Lord Rowan”, and gave him The Look."

#nasim tired

"The Look of a man who has lost his patience at the very start of the conversation, but had to maintain an air of civility to get what he needed."

cla "Rowan, my love, you know I value transparency. And since you’re here, have you by chance met Cla-Tan, my nephew?"

ro "I don’t think I have had the pleasure."

#nasim neutral
show rowan necklace shock at edgeleft with dissolve

nas "I have, as well as most of the library. It took us the better half of the evening to sort out the study room after Cliohna’s thunderbolt pushed him into one of the shelves. He shouldn’t have kept pestering her."

show rowan necklace happy at edgeleft with dissolve

cla "He just gets very enthusiastic when magic is concerned."

nas "One could describe it this way, though I believe Cliohna went with “being an impudent hyperactive brat”?"

cla "First impressions can be misleading."

nas "I think there was an F-word in there as well?"

cla "Great! Everybody knows a casual, informal atmosphere helps foster good teacher-student relationships."

show nasim happy at midleft with dissolve

nas "Does your nephew share that viewpoint? I haven’t seen him around recently."

cla "Of course he does! I just thought a short break would do him good, in some of the drier regions of the world."

show nasim neutral at midleft with dissolve
show clamin neutral at center with dissolve
show rowan necklace concerned at edgeleft with dissolve

cla "He keeps screaming during thunderstorms, the poor lad."

show clamin happy at center with dissolve
show rowan necklace neutral at edgeleft with dissolve

cla "Which is when he was with me when I was buying the Cacti. And what would you know, I leave him alone for a few hours, and that little rascal strikes this amazing deal on the primroses!"

"Something the way she said “amazing deal” made an uneasy feeling crawl up Rowan’s spine, and he was certain Nasim felt it too."

cla "Did you know they can be used in a variety of herbal ointments, with amazing effects that help treat chronic insomnia, head-splitting migraines and a variety of potentially lethal infections?"

#nasim confused
show rowan necklace concerned at edgeleft with dissolve

nas "I…"

#nasim neutral

nas "I thought they were primarily used in essential oils?"

"Cla-Min’s smile didn’t even flinch, but it didn’t need to. She knew."
"She knew from the start, and now so did Rowan and Nasim."
"Her nephew got duped into buying two crates of a completely useless plant, and now Cla-Min had to find a way to somehow make up for the losses."
"And knowing her she’d sooner swallow her own pride selling that crap, than admit a member of her family had the business sense of a six year old."

cla "I’ve been told the most common product is called “Midnight Solitude”."

"None of them shuddered, but they all wanted to."

show nasim happy at midleft with dissolve

nas "… Sounds like a marketable name? Perhaps you have a friend in Uvarth who’d be willing to lend a hand?"

cla "Oh I have friends everywhere, but are you sure? This is a golden- no, platinum opportunity!"

if society_type == "might":
    nas "And it will make somebody a very rich man, but all I need is the Haleen Cacti, miss Cla-min. We can settle for three hundred twenty, but that’s final."

else:
    nas "And it will make somebody a very rich man, but all I need is the Haleen Cacti, Lady Cla-min. We can settle for three hundred twenty, but that’s final."

show nasim neutral at midleft with dissolve

cla "You’re robbing me blind here Nasim. I suppose I could agree to that, IF you’d be so kind as to sneak a good word about Cla-Tan to-"

#nasim annoyed
#clamin shocked
show rowan necklace shock at edgeleft with dissolve

nas "No."

#clamin happy
show rowan necklace neutral at edgeleft with dissolve

cla "Oh I know, I know, as I said, a bit impressionable, but-"

nas "No."

cla "Really no reason to cross out a bright lad like him just because-"

#clamin shocked

if society_type == "might":
    nas "No. miss Cla-Min, please. You’re embarrassing yourself."

else:
    nas "No. Lady Cla-Min, please. You’re embarrassing yourself."

show clamin angry at center with dissolve

"… Not the wisest move on Nasim’s part. Rowan could almost feel the cold fury radiate of her."

menu:
    "Remind Nasim he should be more considerate of his allies’ needs.":
        $ released_fix_rollback()
        #$ change_relation('clamin', 3) TODO
        $ nasimAttitude -= 1
        ro "You should at least hear her out Nasim."
        show clamin happy at center with dissolve
        #nasim neutral
        cla "Ah, no, it’s fine my love."
        "Her chilly disposition disappeared unexpectedly, as if with a snap of a finger, replaced with her usual sunny smile. She sighed theatrically, and patted the crate by her side."
        
    "Reprimand Cla-Min for bothering everyone constantly.":
        $ released_fix_rollback()
        $ change_relation('cla_min', -3)
        $ nasimAttitude += 1
        ro "This really isn’t his problem Cla-Min."
        cla "..."
        show clamin happy at center with dissolve
        #nasim neutral
        "Her scowl deepened, only to disappear unexpectedly, as if with a snap of a finger, replaced by her usual sunny smile. She sighed theatrically, and patted the crate by her side."
        
    "Stay out of it.":
        $ released_fix_rollback()
        show clamin happy at center with dissolve
        #nasim neutral
        "But her chilly disposition disappeared unexpectedly, as if with a snap of a finger, replaced with her usual sunny smile. She sighed theatrically, and patted the crate by her side."
        
cla "This is hardly a fair price, but I suppose you can’t win them all. Three hundred twenty, but only because we’re friends, alright?"

nas "Of course. And another batch like this one, one month from now."

cla "Whatever you ask for, sweetheart."
        
"There was a deceptive sweetness in Cla-Min’s voice, that alarmed them both, but there was no way of discerning what the goblin was plotting."

if nasimAttitude >= 0:
    "He only hoped Nasim could handle it."
    
else:
    "Ah well, whatever it was Nasim had got himself into, it wasn’t Rowan’s concern."
    
$ claNasQuarrel = True
return

#######################################################################################################################


label quarrel_follow_up:

scene bg12 with fade
show rowan necklace neutral at center

quest "… While “Sunset Overdrive” really helps with respiration problems!"

nas "I wish the name wasn’t the most fantastic thing about this concoction."

"Before entering Nasim’s room, Rowan heard a familiar voice inside of it. Keeping a light step, he peered through the crack of the partially closed door."

hide rowan with dissolve

show clamin happy at midleft with dissolve
#nasim annoyed
show nasim neutral at midright with dissolve

"Cla-Min was at it again, trying to be rid of the Desert Primroses. They now took the form of a crate full of potions, with a smiling goblin painted on the side of it. The artist lacked talent, but Rowan thought it was a nice touch."
"Nasim, on the other hand, didn’t."

if society_type == "might":
    nas "Miss Cla-Min. I am grateful for the second batch of Haleen Cacti, but please, I have no desire to hear about your ess-"

else:
    nas "Lady Cla-Min. I am grateful for the second batch of Haleen Cacti, but please, I have no desire to hear about your ess-"

cla "Herbal medicine."

nas "About your essential oils problem! Just leave the cacti, and go."

if serveChoice == 4:
    "Rowan shook his head, wondering if he should go in to intervene."
    "In theory, keeping the various personas in the castle cooperating with one another was part of his job, but keeping these two at odds was that little bit of extra sabotage that required nothing but inaction on his part."

else:
    "Rowan shook his head, wondering if he should go in to intervene. The last thing he needed was another couple of squabbling children in the castle."

cla "Oh Nasim, I could do that! But then you wouldn’t get the chance to see what I have to offer to my platinum members!"

nas "With all due respect, I think the Qerazel heat might have-"

#clamin smirk
#nasim concered

cla "Oh no, I think you’ll really want to know about the platinum inventory."

"Rowan saw Cla-Min put a small, wooden box on top of the potion crate. She turned it around so it would face Nasim, inadvertently preventing Rowan for seeing the content as she opened it."

show nasim angry at midright with dissolve

"So he settled for watching Nasim’s reaction. It started with sudden surprised, then – turned into cold fury, which slowly receded to give way to reluctant acknowledgment."

#clamin happy
show nasim neutral at midright with dissolve

cla "I concede, Cla-Tan might be impressionable, absentminded and obnoxious, but he’s also very inquisitive when it comes to magic."
cla "Funny what one small goblin can find with a sack of coins and a full week to himself, isn’t it?"

nas "His tenacity and resourcefulness do him credit. So how much would it take to become the sole owner of the platinum box?"

cla "Why, it’s not just for anyone! It’s a premium offer available exclusively to the platinum members of our new Herbal Self-Care Club!"

nas "And you can become one by…?"

cla "Oh, it’s simple, really. All you need to do is buy… About two hundred gold coins worth of Cla-Min Caravan’s Limited Edition Herbal Medicine?"

nas "What an innovative sales structure. And do pray tell, how much for this crate of potions here?"

cla "Three Hundred."

show nasim angry at midright with dissolve

"Rowan could almost hear the grinding of his teeth."

show nasim neutral at midright with dissolve

nas "Do you accept magically infused gems?"

cla "At a fair market price."

"Rowan watched in awe as goods changed hands. What did Cla-Min have on him that made him part with three hundred gold coins without as much as a word of protest?!"

cla "Pleasure doing business with you Nasim! I do have a pamphlet on them somewhere-"

if society_type == "might":
    nas "I’ll make sure to study it extensively, miss Cla-Min. So, the platinum box…?"
    
else:
    nas "I’ll make sure to study it extensively, Lady Cla-Min. So, the platinum box…?"
    
cla "Don’t you want to hear about the benefits that come with the platinum card?"

#nas tired

if society_type == "might":
    nas "The box,miss Cla-Min."
    
else:
    nas "The box, Lady Cla-Min."

cla "Such high demand! But you might find the price on that a bit unorthodox, I’m afraid…"

nas "… It’s getting Cliohna to apprentice your nephew."

cla "It’s getting Cliohna to apprentice my nephew."

#nasim neutral

if society_type == "might":
    nas "Miss Cla-Min, I’m afraid you vastly overestimate how much sway any of us, including the twins, have over Mistress Cliohna. I can promise to arrange for a suitable tutor for Cla-Tan, but anything beyond that is simply not possible."
    
else:
    nas "Lady Cla-Min, I’m afraid you vastly overestimate how much sway any of us, including the twins, have over Mistress Cliohna. I can promise to arrange for a suitable tutor for Cla-Tan, but anything beyond that is simply not possible."

cla "It can be a few months from now, if it’s such a problem."

nas "Even then-"

cla "Perhaps teaching him directly would improve his chances?"

nas "… Perhaps. But doing so would hinder my research, and avoiding that is precisely why we’re having this conversation in the first place. I can throw in a personal session twice a week, as a sign of goodwill, but that’s all."

cla "Make it four times a week, Nasim."

nas "… Thrice a week."

show clamin angry at midleft with dissolve

cla "Four times a week."

show nasim angry at midright with dissolve
show clamin neutral at midleft with dissolve

nas "Thrice a week, and a solemn vow he will not fall prey to an unexplained yet lethal malady six months after our business is concluded."

"Cla-min pursed her lips as she considered his proposal, weighing how much further she could push the man."

show clamin happy at midleft with dissolve
show nasim neutral at midright with dissolve

"In the end, long term prospects triumphed over short term gains, and she answered with a dazzling smile."

cla "You drive a hard bargain Nasim, but I accept! The platinum box is yours-"

#clamin shocked
show bg12 with redflash

"Nasim snapped his fingers and the box burst into flames."

#clamin happy

cla "That’s one way of doing it."
cla "Another shipment of Haleen Cacti next month?"

nas "The current amount will suffice for the time."
nas "… You said you had friends in Uverth? Would it be possible to acquire Ogreberries?"

cla "I’ll ask around."

hide clamin with dissolve
hide nasim with dissolve
show rowan necklace neutral at center with dissolve

"Seeing the negotiations coming to an end, Rowan quietly sneaked away from Nasim’s room. What did Cla-Tan find that Cla-Min was able to use so effectively?"

#if NasimPressured: TODO
    #"The same thing that made Nasim strike the deal with Rowan a while ago. The guy could not get a break…"

#else:
"There was no way the goblin matron would spill the beans now that a deal was made, but perhaps later on, Nasim could be tricked into dropping his guard…"

$ claNasBlackmail = True
return

###############################################################################################################################################################
###############################################################################################################################################################
###############################################################################################################################################################

label counterfeit_coins:

$ CounterfeitGoblinDealtWith = True
$ change_treasury(+100)

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show clamin neutral at midright with dissolve

"Steepling his fingers, Rowan waited patiently while Cla-Min inspected one of the many coins piled in front of her, turning it in her fingers with great interest. She then grabbed a magnifying glass Rowan had laying on his desk, and inspected it more closely."

cla "No seam. Markings check out."
cla "Weight seems right, but…"

show clamin happy at midright with dissolve

"She grabbed a handful of the coins, and stacked them up together. The tower tilted slightly to the side, then toppled over. Cla-Min nodded with a smile."

cla "That’s what made you suspicious, wasn’t it?"

ro "I thought it weird. Was I right?"

"She balanced the remaining coin on the tip of her finger, and tapped it with her pipe. It made a quiet *thud* sound."

cla "Yes. They’re fake."
cla "Mind you, they’re pretty good fakes! Would fool most people. You’re lucky you have me and my family on your payroll."

show clamin neutral at midright with dissolve

ro "That’s up to debate."

show clamin happy at midright with dissolve

cla "Rowan, love, why are you always so cold when it comes to business? It wounds my heart!"
cla "Now, do tell, what happened?"

if 'castle.buildings["tavern"].lvl >= 1':
    cla "Bad luck during a raid, or did Indarah not pay attention?"
    
else:
    cla "Bad luck during a raid?"

ro "I’m afraid not, Cla-Min."

#cla shocked

ro "They’re yours."

show clamin angry at midright with dissolve

cla "Impossible. Every single coin that passes through my Caravan is personally checked by an esteemed member of my family. There’s no way-"

show clamin sad at midright with dissolve

"Her voice cut off suddenly, and Rowan watched the realization dawn upon her. Cla-Min tended to keep a good poker face, but for a brief moment, the hurt and anger were unmistakable."

show clamin neutral at midright with dissolve

cla "I apologize, Lord Blackwell. There is a small chance I may have misjudged a relative of mine."
cla "I will attend to the matter and cover the losses, as well as compensate you for the trouble. This will not happen again."

"“Lord Blackwell”? He was glad she took the matter seriously, but she wouldn’t get off the hook so easily."

ro "So you have a suspect already."

cla "I do."

ro "And...?"

"His piercing gaze bore into her, urging her to continue. As the heavy atmosphere thickened, a lesser woman might have squirmed and stammered out a name. But not Cla-Min."
"For her, the pressure had the opposite effect. It was like oil to her cogs, sharpening her wit, and kicking her mind into a higher gear."

show clamin happy at midright with dissolve

cla "Rowan, my love, you know my word is my bond. I already promised I would attend to the matter personally, so you don’t have to worry about a thing."

show clamin at center with moveinright

"He saw her raise up from her chair, and with a nimble motion climbed on to his desk. She fluttered her eyes at him, a dazzling, seductive smile dancing on her lips."

cla "You know how much you mean to me and my people, trickster, and I simply can’t stomach the fact I have disappointed you. So please, let me handle this…"

"She leaned in, her generous bosom almost spilling out of her shirt."

cla "Then later, if you still have doubts about how I run things, or whether the books check out, I wouldn’t mind you dropping by the caravan to… “Inspect my finances”."

menu:
    "Let her handle this, since she’s asking so nicely.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "Is this what counts as dirty talk among merchants?"
        cla "A ledger can be a very private thing to a woman."
        ro "It shouldn’t be, unless she’s hiding something dirty between its folds."
        "Cla-Min giggled in response, almost laying on his desk by this point. Rowan would roll his eyes at such shameless behavior, but then he wouldn’t be able to appreciate what was right in front of them."
        cla "If you wish to conduct a thorough audit, I can have the pages spread and ready this very evening."
        ro "Later, perhaps. In the meantime, go deal with that relative of yours."
        show rowan necklace shock at midleft with dissolve
        "Cla-Min launched herself forward, rewarding him with a long, passionate kiss. Before he could draw her in to take thing one step further, she was already leaping off his table, gathering the false coins to one of her sacks."
        show rowan necklace happy at midleft with dissolve
        cla "Thank you love, I knew you’d understand."
        ro "You have a way with words Cla-Min, among other things."
        show clamin at midright with moveoutright
        "She flashed him a quick grin, then grabbed the counterfeit coins and headed for the exit, giving Rowan ample time to appreciate her wide rear as she went."
        hide clamin with moveoutright
        ro " “Inspect her finances”… Goodness gracious."
        $ change_relation('cla_min', 10)
        return
         
    "Reprimand her for the constant and unwelcome flirtation, but let her handle the matter.":
        $ released_fix_rollback()
        "Rowan’s eyes flickered to coins she inadvertently spilled across the desk with her hips. He picked one, and presented it the goblin matron."
        #cla shocked
        ro "The fact you’re sitting on false gold your caravan delivered this very week undercuts the whole sales pitch a little."
        show clamin neutral at center with dissolve
        cla "Well-"
        show clamin at midright with moveoutright
        "He flicked her the coin. Cla-Min grabbed it on reflex, even though it was essentially worthless."
        ro "Cla-Min, I get it. You’re worried about your family. Since it’s this important to you, I won’t pry any further, as long as the problem is dealt with."
        show rowan necklace angry at midleft with dissolve
        ro "But can you *please* cut down on the constant flirting? Aren’t you supposed to be a professional?"
        show clamin sad at midright with dissolve
        cla "I- Of course, Lord Rowan. This wasn’t the right time."
        ro "There never is a right time for that, but I don’t have time to lecture you Cla-Min. Try to behave, and deal with that relative of yours quickly. One bad apple spoils the barrel, as they say."
        scene black with fade
        "A wave of relief washed over the goblin matron, and she quickly jumped off his desk, loudly expressing her gratitude as she grabbed the counterfeit coins. He assured her that it was nothing - as long as she had his back, so would he cover hers."
        $ change_relation('cla_min', 5)
        return
    
    "Pressure her into revealing who was behind the counterfeits.":
        $ released_fix_rollback()
        show rowan necklace angry at midleft with dissolve
        show clamin sad at center with dissolve
        ro "Cla-Min, you’ve been granted a lot of freedom here, but you forget your caravan business ceased to be your personal property the moment you threw your lot in with the twins."
        show clamin at midright with moveoutright
        "Rowan grabbed one of the counterfeit coins Cla-Min's hips inadvertently spilled across his desk, and presented it to the goblin matron."
        ro "Someone tried to bring false gold into my castle. I would very much want to know who it was."
        ro "And unless you want me to introduce your clan to the term “Collective Responsibility”, you will give me a name."
        cla "..."
        "Cla-Min swallowed heavily, the slowly slid back to her seat, defeated. Normally, she would try to bargain, but her position was far too weak for any negotiations."
        "Should Andras or Jezera hear the full story, there was little doubt who they’d side with."
        cla "It… it was my brother, Cla-Bin."
        show rowan necklace neutral at midleft with dissolve
        ro "Thank you."
        cla "Rowan, look, it’s…"
        cla "It’s not like that. Cla-Bin always argued we can’t trust humans, that sooner or later you’ll screw us over, so we have to get you first. We don’t see eye to eye on this, but given the history between our races, it’s not like his fears are unfounded."
        cla "He approached me a month ago, said it’s stupid that we keep bickering over this. He wanted to make up, help me run the Caravan. Guess it was just an act."
        ro "Then why cover for him?"
        cla "I don’t think he did for the profit. He probably thought it wise to start saving up while Castle Bloodmeen takes the heat."
        cla "He was trying to protect us in his own, stupid way."
        cla "So he might be a shortsighted idiot, but he’s still family. I know it doesn’t justify his actions, but please, don’t be too hard on him."
        
        menu:
            "Let Cla-Min handle this after all.":
                $ released_fix_rollback()
                ro "Me and my soft heart…"
                #cla shocked
                show clamin neutral at midright with dissolve
                ro "Fine. Cla-Min, you’re free to handle his punishment as you see fit, as long as you keep me informed."
                show clamin happy at midright with dissolve
                "The dazzling smile returned as if it was never gone. Cla-Min stood up and bowed her head respectfully, grateful beyond words."
                cla "Thank you, Lord Rowan. I will have a detailed report ready by the end of the next week."
                ro "Good. Consider yourself dismissed."
                $ change_relation('cla_min', 5)
                return
                
            "A light punishment – whip him publicly.":
                $ released_fix_rollback()
                ro "I don’t appreciate the fact there are members of your family who think they can play us like a fiddle, and I’d like it even less if they got away with it with a slap on the wrist."
                ro "Even if I ignored the betrayal, by law forgery is punishable with death, is it not?"
                cla "I- Yes. It is."
                ro "Still… I suppose that would be just proving his point…"
                show clamin neutral at midright with dissolve
                ro "Thirty lashes. And I want you and your family watch him take them. As a warning."
                cla "The message will be heard loud and clear."
                ro "Good. You can go now."
                cla "Of course. And… Thank you, Lord Rowan."
                $ castle.villages_income += 5
                return
                
            "The appropriate punishment – execute him.":
                $ released_fix_rollback()
                ro "The punishment for forgery is death. You know that."
                cla "Rowan if you would-"
                ro "I’ve passed my judgment, Cla-Min. One bad apple spoils the barrel."
                ro "And if you know what’s good for you and your family, I hope he won’t suddenly go “missing”."
                show clamin neutral at midright with dissolve
                cla "No, of course not."
                ro "Good, you can go now."
                cla "Yes, Lord Blackwell."
                $ castle.villages_income += 10
                $ change_relation('cla_min', -10)
                return
                
###############################################################################################################################################################
###############################################################################################################################################################
###############################################################################################################################################################

label counterfeit_consequences:

scene bg6 with fade

if CounterfeitGoblinDealtWith == True:
    "On his return, Rowan was handed the latest report covering Castle Bloodmeen activity."
    "At Andras’ behalf, a small delegation was sent to one of the Dragon Tail many islands, to recruit a mercenary band the twins have heard of. The negotiations ended up a success, and the band’s fearsome warriors have boosted the twins’ forces."
    $ change_treasury(-20)
    $ castle.buildings['barracks'].troops += 4
    return

else:
    "On his return, Rowan was greeted with unpleasant news."
    "Andras had a delegation sent to one of the smaller islands of Dragon Tail, with orders to recruit a local mercenary band. Everything went well, until the head of the delegation handed over the down payment."
    "It made its way back to Rowan, with one of their orcs, eyes gouged out and ears cut off. The coins turned out to be counterfeit, and the pirate lord accused Castle Bloodmeen of foul play. The entire delegation was slaughtered, and all chances of recruiting the band were now lost."
    "Neither of the twins were happy for this development, and Rowan lambasted himself over his own carelessness. He should’ve paid more attention to what coins made their way to their treasury."
    $ castle.buildings['barracks'].troops -= 4
    $ change_relation('jezera', -5)
    $ change_relation('andras', -5)
    $ counterfeitUndiscovered = True
    return
