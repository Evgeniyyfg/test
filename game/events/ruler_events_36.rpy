init python:
    
    event('more_appropriate_profession', triggers="week_end", conditions=('alexiaJezObedient == True', "get_actor_job('alexia')!='maid'", "get_actor_job('alexia')!='none'",), group='ruler_event', run_count=1, priority=pr_ruler)
    event('francois_the_orc_chef', triggers="week_end", conditions=('week > 34','avatar.corruption < 31', 'all_actors["alexia"].corruption < 31', 'all_actors["alexia"].relation >= 50',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('discovery_of_catacombs', triggers="week_end", conditions=('week > 34','avatar.corruption > 30', 'all_actors["alexia"].relation >= 30',), depends = ('resistance_futile',), group='ruler_event', run_count=1, priority=pr_ruler)
    
label more_appropriate_profession:

scene bg14 with fade

if get_actor_job('alexia')=='breeding':
    show alexia breeding concerned at midleft with dissolve
    "A disgusting shambling mess marched down the hallway. That mess was Alexia. Her work uniform was absolutely covered in drider shit. It had even gotten into her hair." 
    "The expression on her face matched the outfit. Disgust. Her nose twitched with the stench. This was going to take hours to clean up. Hours."
    "Draith had told her that someone needed to clean up the mess. But, how could he stutter so heavily when talking about the broken segment of the railing? It was too important to misspeak about."

elif get_actor_job('alexia')=='forge':
    show alexia forge concerned at midleft with dissolve
    "A figure, covered completely black from head to toe in coal soot, marched down the hallway, leaving a black trail in her wake. The figure was Alexia. Her entire body, work uniform, hair, face was covered in it."
    "The expression on her face matched the outfit. Supreme discomfort. Every so often, she’d sneeze out dust. This was going to take hours to clean up. Hours."
    "Oh, Greyhide had been apologetic about it. Falling into the waste pit had been an accident. It almost made it hard for Alexia to maintain her rage. Almost."
    
elif get_actor_job('alexia')=='research_assistant':
    show alexia librarian concerned at midleft with dissolve
    "A figure in a burning uniform shambled down the hallway. The figure was Alexia. The fire was mostly out, but little embers remained on the uniform and even in her hair." 
    "No real damage or scarring, but her outfit was mostly destroyed and she’d need to do something about any singed hairs. Her expression matched her outfit. Annoyance." 
    "This was the last time she’d act as a spell test dummy for one of Cliohna’s apprentices. Had the sorceress not acted fast, the damage might have been less trivial."

else:
    show alexia barmaid concerned at midleft with dissolve
    "A figure shambled down the hallway, covered in what had to be several layers of spilled liquid. Some of which certainly included vomit. The figure was Alexia. Every part of her outfit was a mess."
    "She has a facial expression to match her disheveled state. Exhaustion. The stink of alcohol radiated from her clothes and even her hair."
    "She hadn’t had any herself. But, Indarah had suggested she serve the main group from a rowdy horde of dragons tail pirates who’d stopped in. Indarah didn’t want to be the one to serve them. She didn’t say why."
    "The process had not been fun. As they got progressively more drunk, they got progressively more disgusting. It had been a nightmare shift, from which she’d only just now returned."

"But, before Alexia could make her way to a much needed bath, someone stopped her in the hallway."

show jezera happy at midright with dissolve

je "I see you dressed to impress, Dove."

#alexia embarrassed

al "Oh no."

"Alexia tried to duck away as fast as she could. Her Mistress was the last person who she wanted to be seen by in this state."

al "Apologies, but I-"

"Jezera just giggled."

je "Don’t be shy. I’m a demoness and you’re worried I’ll recoil because you’re icky. I’m made of sterner stuff, darling."

"She put a hand on Alexia’s shoulder, not even caring one wit about what might get on her skin."

je "You’re having a bad time at work, aren’t you?"

al "I wouldn’t know if I’d say that…"

je "Well, that’s perfectly alright. How about we go somewhere and talk about it?"

scene bg9 with fade
show alexia 2 necklace angry at midleft with dissolve
show rowan necklace neutral at midright with dissolve

al "I want to work as a maid, Rowan."

ro "Hrmmm?"

"Rowan looked up towards Alexia from the bed. He’d only returned from doing paperwork moments earlier." 
"Alexia’s appearance showed little sign of her earlier mishaps. There’d been plenty of time to clean off. But, her anger had not cooled."

al "I’m sick and tired of my current post. It’s too stressful working there."
al "So, I was thinking about it earlier. The castle staff have a much easier time. Much less difficult. And Jezera largely makes sure no one harasses them."
al "So I want you to schedule me to work with the castle staff."

"Rowan put a hand to his head. Did he really have to think about this now? The day had been long and difficult for him. Alexia’s anger didn’t quite have the visual punch that it had before her shower."

ro "I’ll review your working arrangements in a week or two. We can see how your current job is-"

al "No. I want you to change my job, first thing in the morning."

menu:
    "Agree to Alexia’s demand":
        $ released_fix_rollback()
        show rowan necklace concerned at midright with dissolve
        "Rowan’s head was killing him. He was the one who was supposed to place her for work. But, she clearly wanted to work somewhere else. Hadn’t he been picking for her sake? It’s not like it would seriously damage the function of the castle."
        "She was just one woman, after all."
        "Mainly though, he just wanted to escape this conversation. Alexia was in his face. She was angry. Rowan didn’t know what to do."
        ro "Okay. I’ll do it."
        ro "First thing in the morning, I’ll go in and change your workplace assignment to the castle staff."
        show alexia 2 necklace happy at midleft with dissolve
        "His wife visibly brightened."
        al "You will?"
        ro "Having a big outing about it isn’t worth it. If you want to work as a maid, that your choice. I won’t get in the way."
        al "I-"
        al "Thank you, Rowan. You listened to me. I’m sorry I lost my temper too."
        al "I’m going to be much happier with work now. You’ll see."
        "She leaned forward and planted a kiss on his cheek. Rowan groaned and put a hand to his temple."
        $ do_job_maid('alexia')
        #stress cost of alexia working as a maid reduced - TODO
        return
        
    "Refuse.":
        $ released_fix_rollback()
        show rowan necklace angry at midright with dissolve
        ro "Alexia, you can’t just come in here and demand that I change the castle schedules without sitting down to review. I’ve spent the better part of months trying to beat this castle into shape."
        "Alexia held her ground with arms crossed."
        al "You do not know how terrible a day I had. I am your wife. I am telling you that I want to work as a maid with the castle staff."
        al "It upsets me when you don’t listen to me."
        "The two held their ground, locking eyes with one another. This had not been their first fight of late. They were getting more adept at it."
        "Alexia really seemed, to Rowan, to mean it. If he held up on his refusal, Alexia would not be quick to forget this."
        menu:
            "Just agree.":
                $ released_fix_rollback() 
                show rowan necklace concerned at midright with dissolve
                "Rowan’s head was killing him. He was the one who was supposed to place her for work. But, she clearly wanted to work somewhere else. Hadn’t he been picking for her sake? It’s not like it would seriously damage the function of the castle."
                "She was just one woman, after all."
                "Mainly though, he just wanted to escape this conversation. Alexia was in his face. She was angry. Rowan didn’t know what to do."
                ro "Okay. I’ll do it."
                ro "First thing in the morning, I’ll go in and change your workplace assignment to the castle staff."
                show alexia 2 necklace happy at midleft with dissolve
                "His wife visibly brightened."
                al "You will?"
                ro "Having a big outing about it isn’t worth it. If you want to work as a maid, that your choice. I won’t get in the way."
                al "I-"
                al "Thank you, Rowan. You listened to me. I’m sorry I lost my temper too."
                al "I’m going to be much happier with work now. You’ll see."
                "She leaned forward and planted a kiss on his cheek. Rowan groaned and put a hand to his temple."
                $ do_job_maid('alexia')
                #stress cost of alexia working as a maid reduced - TODO
                return
                
            "Continue to refuse.":
                $ released_fix_rollback()
                ro "You’re never going to convince me this way. I’m the one who makes the castle assignments. You agreed to it."
                ro "This entire outburst is making me want to change your job even less."
                al "..."
                "There were words on Alexia’s tongue. Rowan didn’t hear them, but he knew they were there. But, those words never came out. Instead, came a different, more terse, answer."
                al "Fine. I understand."
                al "Don’t forget what I asked for."
                hide alexia with moveoutleft
                "Without giving him another look, she turned on her heels and stormed out of the room. Rowan watched her go with a frown. He could still go after her. But, nothing short of telling her that he’d give in would appease her now."
                "Rowan ran a hand through his hair."
                "Why couldn’t she be obedient? That’s how she’d always been back in Arthdale."
                $ change_relation('alexia', -10)
                #stress cost of alexia working as a maid reduced - TODO
                return

#############################################################################################
#############################################################################################
#############################################################################################

label francois_the_orc_chef:
    
scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera neutral at midright with dissolve

je "...Are you even listening to me, Rowan?"

show rowan necklace shock at midleft with dissolve

"Rowan nearly jumped out of his skin at the sound of Jezera’s voice. He’d been working for so long that he’d started daydreaming." 
"He’d been thinking of Arthdale, of those precious years spent between the war and this new, hellish existence. Happy memories spent with Alexia in Arthdale spun with a whimsical flourish through his mind as he lost track of the relentless tedium of his labours."

ro "Y-yes!"

show rowan necklace neutral at midleft with dissolve

ro "Sorry, I got distracted."
ro "Please, continue… you were saying something about this month’s goblin supply shipments?"

show jezera displeased at midright with dissolve

je "Oh, nevermind. I suppose it is getting late. We can talk about this tomorrow."

show jezera happy at midright with dissolve

je "It seems even a Divine Hero needs a rest from time to time, hm?"

"Jezera’s eyes went up and down his body with an appraiser's glint."

je "I suppose you’ve earned a break. You’ve been at it for so {i}long{/i}, haven’t you, Rowan?"

show rowan necklace angry at midleft with dissolve

"Rowan pointedly ignored the caustic smile that built upon his captor’s lips. A beat passed. Then, her posture lowered to a shrug."

je "Very well. Another time, perhaps."

show rowan necklace neutral at edgeleft with moveoutleft

"Rowan bowed to the Lady of Bloodmeen and made to leave, his footsteps echoing on the throne room floor. He stopped short when he heard Jezera’s voice call out to him."

je "Oh, Rowan! I almost forgot: I have a surprise for you."

show rowan necklace neutral at midleft with moveinleft

"Rowan didn’t like surprises, least of all {i}Jezera’s{/i} kind of surprises. He tensed in place, his hand palming the pommel of his sword. An old comfort."

ro "...What is it?"

show jezera displeased at midright with dissolve

je "Oh don’t be so sour, Rowan! You look like you swallowed a lemon."

show jezera happy at midright with dissolve

je "You should be excited. It’s not often I reward someone for a job well done."
je "I read the latest reports."

"That was a surprise."

je "We’re making more from our pre-existing revenue streams, and our new revenue streams are all doing well. This past year, you’ve essentially transformed the castle’s finances. A job well done."
je "I thought it was only appropriate that I reward a loyal servant for his good service."

"The demoness put a contemplative finger to her chin, her eyes alight with mischief."

je "I’ve set aside a small stipend for you, to do with as you will."
je "You might not want to ask about where we got it though. It might not sit well with your… delicate sensibilities."

"Rowan took her up on that advice."

scene bg27 with fade

"A few days later, Rowan stood at the head of a long table in one of the sumptuous dining halls in the castle, wrestling with the butterflies in his stomach. He paced back and forth upon the polished tile, his footsteps echoing in the empty room."

show rowan necklace angry at midleft with dissolve

ro "Where in the Planes of Chaos is he?"

"He couldn’t afford to waste any more time on the surprise; Alexia would be here any minute."
"Rowan had heard that a traveling chef was crossing the wastes as part of a caravan that had stopped nearby. It had cost him an arm and a leg, but he’d persuaded the chef to make a detour using most of Jezera's stipend."
"The mystery chef was known only by his first name moniker: “Francois.”" 
"Rowan himself had only communicated with the man via letter. But, he had the famous chef-cum-sommelier come to the castle for an exclusive meal. A treat to his loyal and loving wife." 
"...but the chef was late."

show rowan necklace neutral at midleft with dissolve

"As if on cue a large, a gregarious fellow swept into the room. It took several seconds of staring for Rowan to process the fact that the large man in the white apron and tall toque hat was an Orc."

fran "‘Allo!"

show rowan necklace shock at midleft with dissolve

fran "It is I, {i}Francois{/i}! Ze gourmet of yo’ dreams! "

$ franName = "Francois"

fran "And yo’ wifey’s dreams too, eh? Ah ha ha ha ha!"

"Rowan’s squinted so tightly he looked like his eyes were closed."

ro "{i}Y-you’re{/i} Francois?!"

fran "But o’ course! Can thou not see a masta’ o’ his craft when thou see’s one?"

"The Orc flourished like a preening magician after a stunning performance, grinning at Rowan with a face full of fangs." 
"Had this all just been some horrible prank on Jezera’s part? Rowan spun his head about in anxious pivots, searching the room for some sign of trickery."

ro "Uh… I-I guess not?"

fran "Then don’ worry ya noggin’ and get to nommin’! My meals are to {i}die{/i} for, thou shalt see for yo’ self!"

"His accent was a curious blend of an Orc’s brutish linguism, mixed with a peasant’s idea of blueblood speak. Rowan was taken aback by his seeming ‘fluency’ with the peculiar dialect."

show rowan necklace concerned at midleft with dissolve

ro "Look, can you just… will the food be ready on time?"

fran "Not ta’ worry young masta’, thou art in good hands! Just sit thouself down and I’ll be back in a fort-minute!"

"The nonsensical Orc boomed with laughter and sped off towards the kitchens. He was gone before Rowan realized what the supposed ‘chef’ had just said to him. He’d just arrived, but he said the food would be done in… a ‘fort-minute?’"
"A fort-minute? Like a fortnight, but in minutes?"
"{i}...The food would be ready in fourteen minutes?!{/i}"

scene bg27 with fade

show alexia 2 necklace neutral at midright with dissolve

"After a few more minutes of anxious worry, Alexia appeared."

show rowan necklace happy at midleft with dissolve

"Seeing her again, even after such a brief time apart brought a childlike grin to Rowan’s face."

ro "Alexia…"

"She’d dressed in her green outfit, her hair done up just as he’d remembered it during their days together in Arthdale. She smiled at him in that wonderful way of hers, standing in the entryway with her arms behind her like some shy maiden at a festival."

al "Hello, darling."

"Her eyes trailed past him, to the long dining table festooned with intricate table settings, red silk napkins and garish silver cutlery." 
"The sumptuous table settings had once belonged to a Rosarian noble whose estates had been… ‘confiscated’ by the Twins. It was far more than the two of them would need, but Rowan had paid to impress. Her green eyes lit up."

show alexia 2 necklace happy at midright with dissolve

al "Is all this for me?"

"Rowan couldn’t contain a cocky smile."

ro "For us."

al "Oh Rowan, you shouldn’t have!"

"He extended his hand to her. Alexia took it, flashing him a toothy smile as he led her like a Lady of the Court to her seat at the head of the table. She giggled at his exaggerated formality."
"Rowan pulled closer to her, putting her hand on his shoulder and draping his arm around her waist. She reciprocated, leaning in so that they were face to face with each other."

show alexia 2 necklace aroused at midright with dissolve

al "...What’s the occasion, my darling?"

show rowan necklace aroused at midleft with dissolve

ro "Can’t a man do something nice for his beloved from time to time?"

"He kissed her. Their lips met and for a long moment they forgot the world around them. At last Alexia pulled away, smirking."

al "Mmmm, I wouldn’t mind it if you made a habit out of this."

ro "Make it worth my while, and I just might."

"He decided it would be best not to mention the moral costs of a dinner like tonight."

show alexia 2 necklace happy at midright with dissolve

al "Tease!"

"Alexia eagerly took her seat at the head, with Rowan pulling the chair back for her before taking his place to her direct left."

al "So, what’s on the menu for this evening?"

ro "Ah… well, to be honest it's kind of a mystery to me as well."

show alexia 2 necklace concerned behind black

al "Hm?"

ro "I hired a special chef from outside the Castle for us to enjoy. But he’s... uh-"

#cg1 - Meal
scene cg618 with fade
pause 3

"As if on cue, the ridiculous Orcish chef flounced into the room, bearing two massive platters on the palms of his oversized green hands."

scene cg619 with fade
pause 3

fran "Ha ha! Dis dinner is {i}served{/i}!"

scene cg618 with fade
show alexia 2 necklace shocked behind cg618
show rowan necklace shock behind cg618
pause 1.5

al "O-{i}oh{/i}! It's an Orc."

fran "‘Course I’s an Orc, blind lady! Does I look like a wee-skinny Elf to thou?"
fran "Dis ‘Orc’ is Francois! The greatest Chef in all Solanse!"

"Alexia turned to Rowan with a blank look of confusion. Rowan shrugged."

fran "Worry not pretty lady, thou art in the {i}best{/i} o’ hands!"

"He pirouetted in place once he reached the two and placed the platters before them. Rowan was astonished at the heat radiating off of the plate… how had the Orc managed to prepare a full meal so quickly?"
"The reason became obvious when he lifted the covers and revealed the hideous looking slop beneath. It looked like a heap of indecipherable gelatinous mush, caked in the color of boiled-spinach green."

fran "‘Tis an old Orcish specialty. Darkwood Goulash. Yo’ taste buds will thank me! {i}Ha ha{/i}!"

"Interspersed between the vaguely-meat textured broth were hints of yellow and orange… carrots and corn? Rowan desperately hoped that that was the case. The food looked more venomous than scrumptious."

fran "Dig in! Da’ second course is on its way!"

"The Orc swept his large hand across the tops of their food like a ship’s sail to clear the steam, then bowed and retreated."
"Rowan and Alexia exchanged a look, their shared worry at the dreadful looking meal causing matching awkward smiles to spread across their faces."

show rowan necklace neutral behind cg618

ro "-Like I was trying to say."

show rowan necklace concerned behind cg618

ro "I hired a chef, but he’s…"

show alexia 2 necklace happy behind cg618

al "Not what you expected?"

show rowan necklace happy behind cg618

ro "Is it that obvious?"

"The couple laughed. Horrifying food aside, it was good to share an intimate moment like this together. They’d had too few of these simple pleasures since coming to Castle Bloodmeen."

show alexia 2 necklace concerned behind cg618

"Alexia - ever the brave one - took the first, hesitant bite. She spun her fork into the yielding food, surprised at how it stuck like gelatin to the teeth of the utensil. She brought it up to her lips and took a delicate nibble."

al "..."

show alexia 2 necklace shocked behind cg618

al "...Rowan, you have to try this!"

"Rowan quirked an eyebrow. Was it really that good, or was his dearly-beloved wife leading him on as punishment for his culinary sin?" 
"He had little choice in the matter. He {i}had{/i} been the one to hire Francois, after all. Steeling himself, Rowan took a bite of the noxious-looking food. "
"Scintillating flavor burst across his stunned taste buds like wildfire. The food was earthy, but savory, full of spices and sauces whose origin were as ambiguous as the chef who made the dish."
"Alexia had a second bite in her mouth before Rowan could finish chewing his first. She let out an appreciative gasp of pleasure."

show alexia 2 necklace happy behind cg618
show rowan necklace happy behind cg618

al "{i}Mmh{/i}, it’s so good!"

ro "Kharos take me, it really is."

"Alexia’s fork shot out in front of Rowan’s face. She waggled it back and forth as she chewed."

al "{i}Mmmph mmph{/i} no cursing at the dinner table!"

"The playful twinkle in her eye made Rowan smile. He took her fork-hand by the wrist and nabbed the food still hanging off of it with his mouth."

al "Hey!"

"She wrenched her wrist away, but the damage was done. Rowan savored his victory with a long, deliberate swallow."

ro "Mmm… delicious."

al "You’re lucky you married such a forgiving wife, Rowan. A noble lady wouldn’t stand for such scandal."

ro "A shame then that you weren’t born a noble, darling. I guess you’ll just have to suffer me instead. "

"They laughed. Alexia’s took another savory bite as she fluttered her eyelashes at him. Her warm smile alone made Francois’ cooking worth every copper."
"An hour passed as Francois brought meal after bafflingly-tasty meal to them. Each one more hideous looking than the last, yet they were all delectable in an exotic sort of way. By the end both of them were stuffed."

scene bg27 with fade
show alexia 2 necklace happy at midleft with dissolve
show rowan necklace happy at midright with dissolve

fran "Was mah food not the *mwah* tastiest?"

"Francois mimed kissing his fingers then threw it out into the air in an energetic rush."

al "It was amazing!"

ro "Thank you, Francois. You did an excellent job."

fran "Ha ha! O’ course I did! I am {i}Francois{/i}, after all! Ze quality is in ze name!"
fran "And thou two! Such a loving couple! Such a fine pair!"
fran "They say mah meals are more filling than a feast, and more {i}potent{/i} than a love potion. Perhaps it shall grant you two stamina in ze sack as well, eh?"

"Rowan cleared his throat awkwardly, and Alexia blushed beet red. This only seemed to amuse the eccentric chef."

fran "{i}Ah{/i} ha ha ha ha!"
fran "I shall take mah leave of thou lovebirds. A thousand blessings to your tastebuds, and tell all you know that your finest meal came on ze day you met {i}Francois{/i}!"

"Francois bid them farewell with a theatrical flourish and swept from the room, leaving the two to marvel in the aftermath of such a colorful character."

al "This was wonderful, Rowan."

ro "I am glad I could provide, darling."

menu:
    "Invite her to bed":
        $ released_fix_rollback()
        jump francoisSex
        
    "Escort her back to the room.":
        $ released_fix_rollback()
        "Rowan had enjoyed himself this evening, but all good things must come to an end. Alexia was yawning, and it was obvious she would last much longer."
        ro "Shall I escort you to your room, Milady?"
        "Alexia giggled and extended her hand."
        al "Thank you, darling."
        scene bg14 with fade
        "They walked hand in hand through the castle halls, chatting about nothing and just enjoying one another’s presence."
        "There was joy in their voices, but in many ways it was forced. Removed from the warm atmosphere and laughing Orc chef, a silent pall fell upon them both."
        "For all the fun they’d had, for all the happiness they’d shared, they were still prisoners in this place. Even the meal itself had been paid with the blood of others."
        "Alexia fell silent as they neared the bedroom."
        show alexia 2 necklace concerned at midright with dissolve
        al "Rowan…"
        ro "Yes?"
        al "Do you ever get the feeling that you’re living in a dream?"
        al "All that food, all that fun…"
        al "We’re living in a gilded cage."
        show rowan necklace neutral at midleft with dissolve
        "Rowan didn’t know how to respond to that. Nor to the searching look Alexia gave him when she looked at him with sad eyes."
        "He sighed, wrapping his arm around her as they came to the door of the bedroom."
        ro "We can only do what we can, beloved."
        "She rested her head against his shoulder. They stood there, comforting each other as husband and wife for a long moment."
        al "...I know, Rowan. I just wish we could do better."
        return
        
label francoisSex:

"Channeling his inner romantic, Rowan shot bedroom eyes at his beloved wife."

ro "You look beautiful this evening, beloved."

al "Why thank you, darling."

show alexia 2 necklace aroused at midleft with dissolve

al "You know… I don’t believe Francois prepared dessert to go with the meal."

show rowan necklace aroused at midright with dissolve

ro "Oh? Did you have something particular in mind?"

"Alexia took Rowan’s hand and squeezed it, pulling him out of his chair. The corniness of the line was almost a game unto itself."

al "I might have a few ideas."

ro "Then lead on, my darling."

"Giggling, the two retired for the evening to their shared bedroom."

#CG 2 sex scene
scene cg670 with fade
pause 1
show cg671 with dissolve
show rowan necklace aroused behind cg671
show alexia 2 necklace aroused behind cg671
pause 3

"No sooner had they closed the door to the bedroom than Alexia had Rowan up against the wall. She kissed him, pressing close as she clung to his chest with his hands. Rowan encircled her with his arms, holding his beloved wife tight as if desperate to let her slip through his fingers."
"At last they pulled away from each other, their lungs empty of breath and their eyes smouldering."

al "Tonight was wonderful."

"Her earnest tone and honest expression belied the heavy blush on her cheeks. She smiled."

al "You really are good to me, Rowan."

if alexiaThreesomeStormout or raeve_keep_rowan_claimed_helayna:
    al "At least, as good as anyone can be in this terrible place."

else:
    al "I know it isn’t easy to be either."

"He chuckled, running his hands down her hips before groping at her ass."

ro "I have a lot of incentive to be."

"Alexia let out a low, sexual coo. She peeled his jacket off, then his shirt, her hands spreading across his bare chest as if kneading clay. Her slender fingers tugged at the buckle of his trousers."

al "Let me be good to you."

"She led him by his belt to the bed, backing up with sultry steps until she was butting up against it. With a wink she undid the straps of her shirt, exposing her pale breasts."
"Rowan helped her with her skirt, peeling them down off her hips with his thumbs, till she was naked."
"It was marvelous how she could still excite him. Nearly a decade spent together had not dampened their romance in the slightest. He was hard beneath his trousers, and her searching fingers found purchase against his length."

al "I want to try something…"

"Rowan smirked at her embarrassed tone and heavy blush."

al "Lie back on the bed."

"He did as he was bid, reclining on the bed as she peeled his leggings off of him. She crawled up between his legs, pausing to plant a long kiss upon the head of his penis before continuing forward. Soon they were face to face again."

ro "My, wasn’t that ambitious?"

"She laughed and lightly slapped his cheek."

al "Shut up! You’re just making it harder to go through with."

"They kissed again. Alexia pulled close, her nipples rubbing in pleasant circles on his chest. She moaned as he ran his fingers through her hair."
"Smiling down at him, Alexia pulled away. For a second Rowan was confused, but then the nature of her maneuvering became obvious." 
"She pivoted in place atop him, spinning around so her ample ass was in his face. He felt rather than saw her fingers take hold of his dick, and then a wet, warm sensation as her lips touched down on his cockhead."

#CG 3 sex scene
scene cg620 with fade
pause 3

"She leaned her hips back, and suddenly all Rowan could see was her wet slit staring back at him."

scene francois69 with fade
pause 3

"He took the gift that was offered to him, leaning up with his face to roughly make out with his wife’s pussy. He groaned into her crotch when he felt her head bob on his cock."
"The pair began a rough back and forth, licking and sucking one another in a friendly competition to see who could make the other cum fist."
"Alexia gasped when Rowan’s tongue tickled her clit. She got back at him by cupping his balls, her hands moving with expert ministrations across the skin of his cock that wasn’t buried in her mouth."
"Rowan riposted, using his fingers to spread her pussy lips wide as he sucked her nectar directly from the source. Alexia let out a muffled cry as Rowan’s fingers dived deep into her dripping delta."
"Not to be outdone, Alexia got daring. Using his hips for leverage, she thrust her head down, deepthroating him in a single move that nearly stole the breath from his lungs."
"Her throat was a vice, wet and warm, with the wriggling from her tongue lathering his dick in saliva. He dove nose-first into her cunt, swirling his tongue around as he heard Alexia squirm and gasp and drip onto his face."
"They both stopped their oral attack at almost the same moment. Breathless, Alexia sat up off his face and glanced over her shoulder at him. There was a moment of mutual understanding, and then she crawled forward."

#CG 4 sex scene
scene cg630 with fade
pause 3

"Randy, horny, driven wild by their partner’s expert attention, Rowan and Alexia moved almost as one on the bed. Alexia positioned herself above Rowan’s dick at the same time he aligned it to her wet pussy." 
"She sank down on him, and just like that they were fucking." 

scene francoissex with fade
show alexia necklace naked aroused behind francoissex
pause 3

"She moved with a particular feminine sway, bouncing atop his cock as she balanced herself with her hands and feet." 
"Rowan loved the little details: the feminine curl of her spine, her long red hair draping down her back like fire. Alexia moved slowly, but with energetic zeal atop him. "
"The soft, wet {i}slaps{/i} of their genitalia coming together added a lovely staccato to the tight, warm sensation of her clamping down on his prick."

al "Mmmh, {i}Rowan{/i}."

"The way she said his name made him smile, made him drift for a brief moment back to happier days spent as youthful puppy-lovers under the elms of Arthdale. How far astray life had taken them from that simple place. But despite everything, at least {i}they{/i} had stayed the same."
"He took his wife’s naked body by the hips, pulling her deeper into his thrust. She gasped, tilting her head back to look at him with heavy-lidded eyes." 
"Rowan planted a rough {i}spank{/i} on her plump behind, causing Alexia to tense and let out a yelp of surprise. Her pussy tightened around him, nearly driving Rowan to orgasm."
"She cast a heated glance back in Rowan’s direction. Far from being provoked by his cheeky strike, she let out a heated moan. Kharos take him, he loved this woman."

scene francoissex2 with fade
show rowan necklace naked behind francoissex2
show alexia necklace naked aroused behind francoissex2
pause 1.5

"They picked up the pace, Alexia bouncing atop him with a hefty weight as Rowan took her by the hips and drove her downwards. Their romantic lovemaking turned into a hot, wet fuck. "
"Rowan began to take deep inhales from his nose as the rising tide of his pleasure built to a thundering crescendo. Alexia, his beloved, let out a cry and bottomed out on him, rolling her ass atop his waist as an orgasm shuddered up her spine."

show cg638 with sshake
show cg638 with sshake
show cg639 with flash
pause 2


"He grunted and thrust and came, his balls clenching as he unloaded himself inside of her. All their love, all their affection and mutual attraction culminated in this final, exemplary sensation."
"He kissed the back of her shoulder as he came, leaning up and wrapping his arms around her stomach as they clung to each other on the bed. Alexia’s breath came out in great gouts as he held her tight, a subtle promise of protection in his enshrouding embrace."

al "Oh Rowan."

"Her quiet whisper of his name made him smile. He let out a pleasured breath as the last of his cum shot into her."

ro "I hope you enjoyed the meal, my darling."

"She looked back at him over her shoulder, taking his cheek in hand and pushing her lips against his own. Alexia planted a soft peck on his lips, then went in for a longer one." 
"For a brief moment, they forgot the world around them: the twins, the castle, the accursed necklaces around their necks."
"After several seconds of intimate contact, the two came up for air breathless once more. The woman of Rowan’s dreams smiled at him in the sexual afterglow of their lovemaking. Alexia stroked his cheek."

al "More than you know, beloved."
al "I love you, Rowan Blackwell."

ro "I love you too, Alexia Blackwell."

$ change_favor('jezera', 1)
$ change_relation('alexia', 5)
return

#############################################################################################
#############################################################################################
#############################################################################################

label discovery_of_catacombs:

scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve

"Another day, another tedious shift working in the castle. Alexia had grown increasingly weary of the backbreaking work."
"All things considered though, she supposed it could be worse."

if alexiaWulump == True:
    "After all, there were far worse things lurking in the depths of the castle. And the Twins were not above throwing those who displeased them in the darkness to join them."
    "She shivered."

"Alexia headed to work, traversing the now-familiar hallways of the castle with ease. Despite the dreadful reputation of the place, the decor could at times be surprisingly homey."
"Take for example the hall she was in now. It was decorated with sumptuous red carpeting, warm colorful tapestries on the walls, even a full suit of ceremonial armour standing sentinel against the wall."
"Despite everything Alexia found herself smiling. Perhaps her circumstances were difficult, but at least she could take pleasure in the little things in-"

statue "{i}Wuuuuuh!{/i}"

show alexia 2 necklace shocked at midleft with dissolve

"Alexia nearly jumped out of her skin at the sound of air whooshing by her. She turned to see what looked like the armoured statue {i}groaning{/i} at her."

al "{i}Aaah!{/i} What in the flaming Planes of Chaos is that?!"

"She froze like a hare who’d caught sight of a wolf in the brush. The hair on the back of her neck stood on end. She stared wide-eyed at the motionless statue for a long moment, but nothing happened."

al "Um, hello?"

"There was no answer. As far as she could tell the suit of armour was just that: a hollow suit of armour. She took a tentative step forward."

show alexia 2 necklace angry at midleft with dissolve

al "Solansia preserve me, if this is another one of Andras’ tricks..."

"She reached out a tentative hand and brushed her finger across the statue’s metal chest plate. Nothing happened."

show alexia 2 necklace neutral at midleft with dissolve

al "...Am I dreaming? I definitely heard something."

quest "{i}Wuuuuuh!{/i}"

show alexia 2 necklace shocked at midleft with dissolve

al "{i}Aaah!{/i}"

show alexia 2 necklace neutral at midleft with dissolve

al "...Wait, that’s not the statue. It’s coming from {i}behind{/i} the statue!"

"Alexia craned her head to look around the statue, but found nothing lurking behind it but the wall. She blinked in confusion."

"Now determined to discover the source of the strange sound, Alexia felt around the edges of the wall. She stopped when her fingers ran across a strange divot near where the stone gave way to wood paneling."

al "Wait…"

"Her fingers found the edge line and moved upwards. She could feel the heavy flow of air drifting across her fingertips."
"Moving farther up, she was shocked to discover the strange divot went all the way around like the frame of a doorway."

al "This is a fake wall!"

"Now curious to the point of adventurous, Alexia put her shoulder against the false wall and pushed. It gave way with little difficulty. Pivoting on an axis to swing open silently."
"The fake wall opened into a narrow tunnel. It was dark and dimly lit, but she could just make out light in the distance."
"Alexia looked around the deserted hallway with furtive worry, feeling very much like a toddler caught with her hand in the pastry basket. She probably wasn’t supposed to go in there… wherever ‘there’ led to."

scene bg58 with fade
show alexia 2 necklace neutral at midleft with dissolve

"But curiosity got the better of her. With many a backwards glance she walked into the tunnel, her shoes echoing with every step."
"The tunnel led quickly to more tunnels… and more tunnels after that. It got to the point that Alexia made sure to double back every so often to remember where she’d been."
"She was moving through the innards of Bloodmeen castle, that much was clear. The muffled sounds of voices on the other sides of the walls, as well as thumping footsteps from passers-by told her so."
"Many of the passages were blocked by large rocks and assorted barricades, lit with strange tunes and markings that Alexia couldn’t make heads or tails of."

if alexia_knows_magic == True:
    "She peered closer, examining the magic glyphs the way Cliohna had taught her."
    "None of the simple runes Sorceress had shown her in her studies looked anything like the complex geomantic web that covered these stones."
    "Whoever had placed them was a powerful magician, the magic contained therein equally so." 
    "Bloodmeen had been home to many such sorcerers over the centuries. Best to steer clear of things she didn’t understand."

"The tunnels led in all directions, honeycombing the length and breadth of Bloodmeen. The sound of activity was all around her, and Alexia became more and more convinced that they could lead {i}anywhere{/i}."
"Something told her that she could even reach the Twin’s chambers... if she was determined enough to find them."
"Doors, ladders and false panels were everywhere, streaming in faded light through the cracks. Despite the dimness, it was always light enough to see. Magic was at work here, that much was clear."
"Some of the larger tunnels sloped downwards. Following her instincts, Alexia took one of these routes far into the inner depths. She descended so deep that the walls began to grow moist, the air heavy."
"At one point the floor leveled out, turning temporarily from stone into a long, metal grating."
"Some strange smell wasted up from the bottomless pit, a foul stench that smelled like a disturbing amalgamation of rotten eggs and sulfur."

show alexia 2 necklace concerned at midleft with dissolve

"Alexia heard strange slithering sounds arising from beneath her. Her heart crept up into her throat."

if alexiaWulump != True:
    "Something about the musky smell made Alexia shiver. Whatever the thing lurking beneath her feet was, she probably didn’t want to lay eyes on it."
    
else:
    "A chill ran down her spine. This smell, noxious and oppressive, was the same one she’d smelled while confined in the dungeons with that monstrous creature, the Wallump. Sulfur, mixed with rotten eggs. She suppressed a gag."
    "There was no mistaking it. She was near the Dungeons."

"It had been hours since she’d started her unexpected sojourn into the hidden tunnels, and it was getting harder and harder to retrace her steps. Having pushed her luck as far as she dared, Alexia decided to retreat."
"The discovery was monumental in scope. These tunnels were frightening, claustrophobic and strange."
"...And might prove to be extremely useful, should someone have need of them."

scene bg6 with fade
show rowan necklace neutral at midright with dissolve

"Rowan was just polishing off the last letter of the day in his office when his wife - of all people - burst into the room."

show alexia 2 necklace shocked at midleft with moveinleft

al "Rowan, you must come with me, immediately!"

ro "Why, what’s happened? Is everything all right?"

al "Quickly!"

"And just like that his dearest wife left the room in a rush. Rowan scratched his head for a moment before letting out a sigh. He put away his paper and quill and moved to follow her."

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at midright with dissolve

ro "{i}Now{/i} will you tell me what all the fuss is about?"

al "Hold on, we’re almost there."

if avatar.corruption < 31:
    "Rowan’s brow tightened. It wasn’t like his wife to pull him away from work like this." 
    "Had something happened to her? Was there some new threat? The last thing either of them needed was more trouble." 

else:
    "Rowan let out a condescending sigh. Alexia had an unfortunate habit of finding new - and increasingly {i}stupid{/i} - ways of getting herself into dangerous situations. It tried his patience." 
    "Perhaps it was just a side effect of spending the whole day pouring over monotonous military details in his office, but Rowan found it hard to take her trivial affairs seriously." 
    "Instead of focusing on her words, he idly watched the sway of her hips as she walked."

"Alexia brought him before an innocuous looking suit of armour standing in an empty hall. She gestured at it, as if expecting him to respond."

ro "...It’s a suit of armour."

show alexia 2 necklace angry at midright with dissolve

al "Can’t you hear it?"

ro "Hear what?"

"Alexia let out a melodramatic sigh and approached the statue. Reaching past it, she shoved at the wall with her shoulder. "

show rowan necklace shock at midleft with dissolve

"To his astonishment, wall gave way, revealing a crack in the wall that led into darkness."

ro "What… what {i}is{/i} that?"

show alexia 2 necklace happy at midright with dissolve

al "It's a whole network of tunnels!"

if week < 60:
    ro "{i}Inside{/i} the castle?!"
    "Alexia grinned at him like a child showing off a secret hiding place."
    show rowan necklace neutral at midleft with dissolve
    al "I’m uh… not sure. I spent the whole day in there, but I didn’t reach the end."
    al "There’s dozens of tunnels down there, maybe even hundreds. I’m pretty sure they run all the way down the mountain."
    ro "But… how is this possible? The Twins have never mentioned anything about this!"
    if all_actors["alexia"].flags["andras_influence"] > 5:
        show alexia 2 necklace aroused at midright with dissolve
        al "I don’t know, m-maybe Master Andras forgot to mention it?"
        show rowan necklace angry at midleft with dissolve
        ro "Andras wouldn’t just “forget” about a detail like this."
        "The Twin was many things, but subtle wasn’t one of them. Given his brute force approach to most problems, it was unlikely that he knew about this. Rowan had a hard time conceiving of the red giant skulking about in the tunnels."
        show alexia 2 necklace neutral at midright with dissolve
    elif all_actors["alexia"].flags["jezera_influence"] > 5:
        al "Hmm, it {i}would{/i} be very much like Mistress Jezera to withhold this kind of information from you."
        al "Perhaps she didn’t think it “relevant” to your job as her general?"
        show rowan necklace concerned at midleft with dissolve
        ro "A fair point..."
        "Jezera might well be aware of this unexpected network. If so, Rowan wouldn’t be surprised if she’d already utilized it to her own, uncertain ends."
        show alexia 2 necklace neutral at midright with dissolve
    else:
        show alexia 2 necklace neutral at midright with dissolve
        al "Well…"
        al "Maybe they don’t have to know?"
        "Rowan had to blink a few times to process what she was saying."
        ro "I… suppose they don’t, do they?"
        "The couple shared a long look, mutual understanding underscoring the treasonous thought."
        
else:
    "Rowan stopped short. Had Alexia managed to stumble upon the tunnels that Jezera had shown him? His mind swirled with the possibilities of having a reliable entrance to the extensive labyrinth."
    "He decided to play dumb."
    ro "A tunnel?"
    al "More than just ‘a’ tunnel, Rowan. {i}Lots{/i} of them, running through the whole castle!"
    "She definitely had stumbled onto Jezera’s network. Rowan suppressed a satisfied smile."
    ro "How deep does it go?"
    show alexia 2 necklace neutral at midright with dissolve
    al "I’m uh… not sure. I spent the whole day in there, but I didn’t reach the end."
    al "There’s dozens of tunnels down there, maybe even hundreds. I’m pretty sure they run all the way down the mountain."
    show rowan necklace happy at midleft with dissolve
    ro "It seems we’ve stumbled upon a mystery."

show rowan necklace neutral at midleft with dissolve

ro "Can you show me what you found?"

"Alexia nodded, slipping into the tunnel’s confines like a practiced cave spelunker. Rowan smirked and moved to follow."

scene bg58 with dissolve
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at midright with dissolve

"Side by side, husband and wife traversed the narrow corridors and dim light of the hidden tunnel network. True to her word, Alexia led him through a dizzying series of switchbacks and forks between tunnels."
"It was a marvel she could find her way at all. Even an experienced tracker like Rowan struggled to keep straight all the directions they could go. It became rapidly apparent that she had not been speaking in hyperbole: the tunnels ran through every nook and cranny of the Castle."
"Hidden gaps in the ceiling revealed peeping holes in bedrooms for prying eyes to spy upon. Several of the hallways were blocked up by hard to move decorations. Rowan tested a few, finding himself suddenly in different parts of the castle entirely."
"The sound of voices through the walls followed them everywhere, the rough thud of footsteps above their heads followed by trailing dust indicating how close they were to the Castle’s denizens."
"This was more than a token discovery, this could change everything… albeit not immediately."

ro "Kharos take me, if only we’d known about this sooner..."

al "The entrances are well hidden. Not to mention many of the halls are blocked off. Who knows how many openings like this there are?"

if avatar.corruption < 31:
    "Rowan’s mind raced with the possibilities this glut of information afforded him. Assuming he could keep the Twins in the dark about this particular ‘discovery,’ he had a near-limitless access to the secrets of Bloodmeen."
    "Alexia had given him a gift that Rowan had been starved of since coming to Bloodmeen: information he could use to his advantage."
    show rowan necklace happy at midleft with dissolve
    "She made to continue downwards into the farther depths, but Rowan caught her wrist."
    ro "I’ve seen enough for one day."
    ro "But… thank you. You did a great job in finding this for me."
    "Alexia’s eyes filled with pride. Rowan leaned forward and planted a chaste kiss on her lips. She smiled shyly at him."
    show alexia 2 necklace happy at midright with dissolve
    al "I’m happy to help you in whatever small way I can, beloved."
    ro "This was more than a ‘small’ help, darling."
    show rowan necklace neutral at midleft with dissolve
    ro "I don’t want to get high hopes just yet. Maybe the Twins know about this place, and simply never told us about it."
    show rowan necklace happy at midleft with dissolve
    ro "But this has the potential to change things in a big way, if we play our cards right."
    ro "Come on, we have spent enough time down here today. The last thing we want is for people to start asking questions about where we’ve been."
    "Together, hand in hand, Rowan and Alexia picked their way back to the original entrance, armed with new knowledge about Castle Bloodmeen."
    $ catacombsKnowledge = True
    #award conquest / rebellion points TO DO
    return
    
else:
    "Rowan’s calculating mind took in this new detail like a spider spinning its web. Knowledge was more valuable than gold, and his beloved wife had just inadvertently stumbled onto a dragon’s hoard."
    show rowan necklace aroused at midleft with dissolve
    "She made to continue downwards into the farther depths, but Rowan caught her wrist."
    ro "I’ve seen enough for one day."
    if all_actors["alexia"].flags["andras_influence"] > 5 or all_actors["alexia"].flags["jezera_influence"] > 5:
        jump catacombsEnd
    else:
        menu:
            "Grope her.":
                $ released_fix_rollback()
                jump catacombsSex
            "Send her on her way.":
                $ released_fix_rollback()
                jump catacombsEnd
    
label catacombsEnd:

ro "You did an excellent job finding this for me."

show alexia 2 necklace happy at midright with dissolve

al "Of course, Rowan. I just hope it helps."

"{i}More than you know{/i}. He thought to himself."

ro "It has. Thank you for bringing my attention to this."
ro "Come on, we have spent enough time down here today. The last thing we want is for people to start asking questions about where we’ve been."

"Together, Rowan and Alexia picked their way back to the original entrance, armed with new knowledge about Castle Bloodmeen."

$ catacombsKnowledge = True
#award conquest / rebellion points TO DO
return


label catacombsSex:

scene cg577 with fade
show rowan necklace happy behind cg577 
pause 3

"Rowan stepped into her personal space. Alexia tensed, sensing immediately her mate’s sudden shift in demeanor. He moved as if to hug her, but his hands went down to knead at her ass instead."

if all_actors["alexia"].corruption < 31:
    "Alexia’s gave a nervous smile, watching the predatory look build in his eyes. Rowan grinned."
    "She was so delicate, this little guileless dove. It was amusing to watch her squirm, to see her try to maintain her dignity in the face of his amorous attention. His probing fingers sank into the fabric of her pants, and she gasped."
    "She wasn’t fooling anyone."

else:
    "Alexia’s eyebrow raised, a sly smile growing on her lips as she reasoned out her husband's intentions."
    "She bit her lip, her hands running down his chest as she let out a low moan."
    al "Something on your mind, Rowan?"

ro "Turn around, darling. I want to reward you for your efforts."

"Alexia did as she was bid, heeding her submissive instincts. Her shoulders narrowed as she huddled into herself."
"Rowan settled his hands upon her, clenching them in a possessive manner. He often forgot how much smaller than him she was, how frail and dainty her frame."
"His fingers were mere inches from her slender neck. It was a delicate game, holding so close that it almost felt like he was choker her...yet not quite moving his fingertips that last bit forward. There was eroticism in that gap. She was in his power, and he could do whatever he wanted with her."
"It was a morbid thought, but not one considered with any serious malice or intent. She was his beloved wife, his {i}mate{/i}. If there was anything he was willing to sacrifice for to protect, it would be her."
"Still… the thought of holding such power over her, of physical dominance and giving in to the illogical, bestial urge was strangely captivating."

if all_actors["alexia"].corruption < 31:
    "Innocent little Alexia tilted her head back, her uncertain eyes meeting his own as he stared back at her with avaricious lust."
    "He ran his fingers down her slender back, and she quivered, bending forward ever so slightly in quiet acceptance of her place beneath him."
    "Perhaps it was her pliant meekness that pleased Rowan the most: the low-key subservience to his every whim, hidden beneath a pretense of purity and wifely duty. It made for an oddly stimulating juxtaposition: the blushing maid who played the willing whore."
    "...or perhaps it was the opposite. The time had come to test the theory."

else:
    "Alexia craned her neck back, leaning flush against Rowan’s body. She winked at him, grinding her ass against his crotch as her hands dropped limp to her sides to let him do as he willed with her." 
    "She must have read his movements, the little minx. For when she pulled against him, she bared her throat like a defeated beast of the forest offering submission. Rowan’s fingers trailed gently across her neck, and she let out a soft sigh."
    "{i}The whore knows what I intend to do{/i}. Rowan thought. The mood in the room became all the more electrified from the realization."
    "She had grown in their time in the castle, that much was certain. Like a sinful flower she has bloomed into this new, wondrous creature: always ready to push the boundaries, to take chances."
    "She had become his willing plaything."

"A wicked idea built in Rowan’s head. Alexia was his most loyal companion, the one person in his life who trusted him without question, who would follow him to the deepest pit of the six hells."
"Maybe he could push that boundary, see how deep the Well really was."
"He ran his hand down her side, taking hold of her hip. His other hand seized her by the scruff of the neck, and she let out a surprised yelp."

scene cg578 with fade
show rowan necklace happy behind cg578 
show alexia 2 necklace aroused behind cg578 
pause 3

ro "Bend over. Up against the wall."

"Alexia let out a shuddering breath, her body moving without question as her dominant partner asserted his superiority."
"She planted her hands on the wall, bending forward so her ass was out."
"She was wearing that frilly green dress again. That wouldn’t do. If they were to submit to their most primal urges, {i}nothing{/i} should separate them."
"Rowan planted a hard {i}spank{/i} upon her ass, reaching down and without preemption pulling her dress up, exposing her panties."
"Alexia shivered, but remained still. Something wordless had passed between them, and she was frozen by his commanding physicality."
"Rowan made short work of her underwear, ripping the dress up off her head and tossing it aside. Alexia cast her gaze back at him, her eyes lidded and her breath short. She was already wet, the randy slut."

if all_actors["alexia"].corruption < 31:
    "A loud {i}thump{/i} above them caused the couple to jump in place. Alexia cast a worried glance back at Rowan."
    al "W-we shouldn’t do this here. We could get caught!"
    "Her fear was palpable, but so was her excitement. She truly didn’t want them to be discovered… but what was the harm in toying with her?"
    "Rowan’s lips curled into a dark smile. He stepped into her personal space, spreading her asscheek with one hand and dipping two fingers deep into her pussy in one stroke."
    ro "Good. Let them listen."

else:
    "The distant sound of voices echoing down from above them gave Alexia pause."
    "She turned her head back to look at him, her eyes aflame. She lifted a finger to her lips, breathing out a silent {i}Shh{/i}."
    "Rowan knew a whore’s lie when he saw one. Her “fear” was just a minstrel’s show. She {i}wanted{/i} them to be discovered; the sheer taboo of it excited her."
    "A shame. Rowan was tempted to indulge her, but he still had practical use for this place."
    ro "Let’s play a game: see if you can hold your tongue, beloved."
    "He jammed twin fingers into her cunt, wriggling about her insides like a puppeteer’s manipulations."
    
"Rowan didn’t wait for her surprised gasp to finish. He began thrusting his fingers in and out of her, curling the digits like a spider’s crawling toes against her insides."
"Alexia cried out, muffling her mouth with a hand as the sound of footsteps echoed above their head. Indistinct voices could be heard, echoing beneath the floorboards."

al "{i}Mmph!{/i}"

"The lewd sounds emanating from her cunt were sweeter than a harpischord’s tune to Rowan’s ears. He bent down, gripping a fistful of her hair as he continued his merciless fingering."
"Rowan leaned his lips to her ear, whispering as her warm insides clenched and jelled against him."

ro "I know just what you need, slut."

"Alexia gasped and shook her head, keeping her mouth covered."

ro "If you can say my name without squealing “darling,” I’ll make sure you don’t make a peep while I’m fucking your brains out."

al "{i}Nngh!{/i}"

"Oh! She clenched up at that. The innocent little village girl routine was more of a front than he’d thought. He clenched his fingers in her silky hair."

ro "{i}Say{/i} it. Say my name without screaming it, and maybe I’ll let you look me in the eyes when I “thank” you for finding this place."

"He let go of her hair, reaching around to pull her hand from her lips. She let out a low, feminine whine as his fingers pushed and pulled and twisted within her."

al "R-{i}rowan{/i}!"

scene cg579 with fade
show rowan necklace happy behind cg579 
show alexia 2 necklace aroused behind cg579 
pause 3

"Rowan smiled. She was ready."
"Without a word he hooked his arms under her waist, lifting her bodily and spinning her around, plopping her down face to face with him."
"Her eyes were like jade dragonfire, she huddled into Rowan’s chest, her body warm to the touch, shivering with feminine excitement."
"Rowan reached his hand up, caressing her throat with his fingers before gently tilting her chin to look up at him."

ro "Are you ready to accept my gratitude?"

"Breathless, she nodded. It was all the invitation he needed."

"Like the snapping string of a bow pulled beyond its apex, Rowan let loose. He shoved Alexia backwards, pinning her to the wall with his weight."
"She let out a surprised gasp, but he did not grant her time to recover. He lifted her up into the air, forcing her to straddled his waist as he threw one of her legs over his shoulder, spreading her thighs apart while keeping her at eye level."
"His free hand darted out, encircling her throat in a light grip. Her breath caught short, but he did not tighten his grasp, nor close the windpipe completely."
"They held there for half a breath, the two staring deep into one another’s eyes."

if all_actors["alexia"].corruption < 31:
    "Alexia’s blush deepened. She relaxed into his grip, her wide, green gaze holding firm to his." 
    "She trusted him; the innocent little dove really did trust him. Rowan smirked."
    "Whatever else could be said for his beloved, Alexia was brave. Many would have shied away from the intensity of the moment, but she faced it with dignified grace."

else:
    "Alexia’s eyes filled with list. She shot back a teasing smirk, bending a coquettish eyebrow upwards."
    "{i}Is that all?{/i} She mouthed, insolence and amusement flowing across her face in equal measures."
    "Rowan chuckled. Here he was, worried that she would be afraid, and the randy wench was begging for more!"
    "She was a witch's bubbling cauldron in his grasp: threatening to boil over at any moment with uncontrollable lust."

"Best not to keep her waiting."
"He removed his hand from her throat for a brief spell, only long enough to fish his painfully hard cock from his pants and align it to the dripping, twitching sheath that eagerly awaited it."
"Alexia squirmed in place, but that was mere halfhearted foreplay."

show catasex with fade
pause 3
#rowan smirk
show rowan necklace happy behind catasex
show alexia 2 necklace aroused behind catasex

"When his cockhead pressed into her she took in a shuddering inhale and went slack against his chest, letting Rowan hold her up against the wall as he began to roughly thrust into her."
"He held her there, helpless to his not-so-tender ministrations as he rolled his hips into Alexia’s deepest valley. Her pussy twitched and clenched, sucking him in with an almost desperate alacrity."
"Alexia trembled, the wet {i}slap{/i} of their hips connecting adding further instability to her already precarious balance. If Rowan hadn’t been holding her firmly in place with his own weight, she’d have toppled over."
"She let him take her, ceding total control to him like it was a blessed weight off her shoulders. Rowan thrust as deep and as hard as he could, and she accepted it, squeezing her eyes shut as she grimaced in painful pleasure."
"Rowan’s hand went around her neck, applying gentle pressure to the sides. She gasped as breathing became a sudden, shuddering trial."
"His palm acted as a barrier to her sensitive region: avoiding harming her windpipe while pinching off easy airflow." 
"He used her jawline as a grip, tilting her head sideways to add to the feeling of helplessness to the proceedings. She looked at him askew, her eyes going wide as dinner plates."

if all_actors["alexia"].corruption < 31:
    "Her faux-farmgirl routine wasn’t fooling anyone. When Rowan thrust inside again he felt a noticeable tightening in her womanly hole. The little lamb wasn’t innocent enough to avoid getting off to his rough treatment."
    "He rewarded her by releasing his grip pulling back his hand and dealing a soft {i}whap{/i} to her cheek." 
    "The stinging blow knocked her from her sexual stupor, and Alexia recovered enough of herself to manage a halfhearted blush of embarrassment."
    "She didn’t tell him to stop, though. She simply moaned and clung tighter to him."

else:
    "Alexia couldn’t even manage to affect a proper look of shame for her abject humiliation. Rather: her eyes dilated, her muscles clenched, and a wet, squirting spurt of something splattered down Rowan’s thighs."
    "The lewd bitch. She’d cum just from the tightness of his grip."
    "Such overenthusiastic eagerness merited a proper punishment. Rowan let go of her throat. Alexia began to moan out a complaint, but was cut off by the loud {i}smack{/i} of his hand across her cheek."
    "She let out a pleasured squeal, the sudden, explosive action catching her completely off guard. When her lustful eyes opened, they practically begged him to give her another."

"Her moans were getting too loud. Fun or no, Rowan had a future use for these tunnels, one that transcended the petty pleasures he was experiencing in the moment."
"As fun as it was to indulge in his wife’s lurid cries of pleasure, he needed her quiet. His hand closed lovingly around her throat once more, muffling her whorish exhales."
"Alexia’s pulse quickened, he could feel it in his fingertips. As his grip tightened she grew ever more excited, her eyelids fluttering as he alternated between deep, pounding strokes and short, shallow thrusts."
"She let out choked moans of pleasure, her body tensing every time he paused at the precipice of his downstroke. Rowan smiled, deciding to toy with her one last time."

scene cg579 with dissolve
#rowan smirk
show rowan necklace happy behind cg579 
show alexia 2 necklace aroused behind cg579 
pause 3

"His thrusts slowed, dwindling down to nothing. Alexia opened her eyes, her face flushing with confusion as he loosened his grip on her neck. She took in a deep breath of air."

al "W-why did you-"

ro "How hard do you want me to fuck you?"

if all_actors["alexia"].corruption < 31:
    "Her face, already red, went positively crimson. She took the momentary pause in their rough lovemaking to catch her breath."
    al "I..."
    "Alexia bit her lip and glanced away. Rowan chuckled: the little dove couldn’t even admit how much she was enjoying herself!"
    "No matter. He had his answer."
    
else:
    "Alexia’s gaze was trained to his with unblinking intensity. They stared into one another’s eyes, mutual understanding passing between them in the intimacy."
    al "{i}Harder.{/i}"
    "Her voice was raspy, empty of breath. Rowan smiled, running the back of his fingers across her cheek."
    "He slapped Alexia again, just hard enough to startle her. She let out a surprised gasp that swiftly transitioned into an erotic moan."

scene catasex2 with fade
#rowan smirk
show rowan necklace happy behind catasex2
show alexia 2 necklace aroused behind catasex2
pause 2

"Rowan began to thrust. Harder this time, heedless of their slower pace before. He covered Alexia’s mouth with his hand, fucking her with wild abandon."
"Her screams of pleasure could be heard through the gaps of his fingers. Rowan did his best to silence her, but it was a loser’s game."
"He choked her again, thrusting his hips as his wife’s smothered cries drifted up through the narrow channel that his grip allowed."
"She was his. Now and forever."
"At last the vice like grip of her drooling love tunnel proved too much for him. Letting out a low, animalistic growl, Rowan jerked forward sandwiching Alexia tight between the wall and him."
"He pulled her tight to him, shoving his cock into her deepest place as he thickened and came inside her."

show cg655 with sshake
show cg655 with sshake
show cg656 with flash 
pause 2

al "{i}Aaahn!{/i}"

"She didn’t even bother to cover up her cry of pleasure this time. Her body shuddered as her eyes squeezed tight, wet squirts of feminine liquid jettisoning from her abused twat as Rowan finished in her."
"Luckily for the both of them, the sounds coming from above had long since faded to silence." 
"Rowan humped her to completion, stepping back once he was finished and letting her entrapped leg off his shoulder. It slid hopelessly to the ground. "
"Her legs gave out on her, and Rowan found himself having to hold up his insatiate wife as she gasped and trembled out a colossal orgasm."
"Rowan smiled leaning in so his lips were at her ear, his quiet whisper echoing in the cavernous tunnel."

ro "Thank you."

if all_actors["alexia"].corruption < 31:
    scene bg58 with fade
    show rowan necklace happy at midleft with dissolve
    show alexia 2 necklace happy at midright with dissolve
    "Alexia threw her arms around him, clinging tight to his form as she settled her head on his shoulder. He felt the soft touch of her hands begin to rub his back in slow circles."
    "Rowan smiled at his wife’s guileless affection. For all her pretensions of purity, she really {i}was{/i} devoted to him body and soul."
    "Her persistent naïveté was an annoying liability. But Rowan could not deny the simple pleasure to be had in being with someone who was unwaveringly loyal to him. Such uncomplicated relationships were a rarity in Bloodmeen."
    "He put a hand to her cheek, rubbing with his thumb the red spot he’d made when he slapped her."
    ro "We should leave, beloved. We have tarried too long already."
    "Alexia nodded, a tremulous smile building on her features. She closed her eyes and plumped her lips for a kiss."
    "Rowan humored her, leaning in to kiss her as they traded tongues."
    "She still insisted on playing the blushing maid. Rowan would have to work that particular kink out of her, yet."
    $ catacombsKnowledge = True
    $ change_corruption_actor('alexia', +5)
    #award conquest / rebellion points TO DO
    return
    
else:
    scene bg58 with fade
    show rowan necklace aroused at midleft with dissolve
    show alexia 2 necklace happy at midright with dissolve
    "Alexia shot back a whore’s practiced smile. Her brows arched, her lips parting to flash him just the barest hint of teeth."
    show alexia 2 necklace aroused at midright with dissolve
    al "That’s all you’ve got?"
    ro "For now. "
    show alexia 2 necklace angry at midright with dissolve
    "Alexia puffed out her cheeks in feigned annoyance. She was looking for more rough play, and was hoping he would punish her for her insolence."
    "But they had spent too much time down here already. Rowan instead released his grip and stepped back, observing with wry amusement her debauched, naked state. Cum and feminine juices ran down her legs." 
    "She looked like a whore. {i}His{/i} whore."
    "Rowan put a hand to Alexia’s cheek, his fingers trailing downward to grab her by the throat once more. Alexia let out a pleasured gasp."
    ro "If you really want more, you’ll have to earn it."
    ro "You’ve received a reward worthy of your service to me. Anything more, and I'd be spoiling you."
    show rowan necklace happy at midleft with dissolve
    ro "Collect your clothes, beloved. You can walk back to our room naked."
    "An enthusiastic grin grew across his wife’s face. The sheer taboo of it excited her." 
    "Rowan chuckled to himself: she was far too easy to toy with."
    $ catacombsKnowledge = True
    $ change_corruption_actor('alexia', +5)
    #award conquest / rebellion points TO DO
    return
