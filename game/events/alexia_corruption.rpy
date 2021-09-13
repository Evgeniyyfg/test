init python:
    
    event('alexia_med_corruption', triggers='week_end', conditions=('all_actors["alexia"].corruption > 30',), run_count=1, priority=pr_story)
    event('in_her_hands', triggers='week_end', conditions=('all_actors["alexia"].flags["jezera_influence"] > 5','all_actors["alexia"].relation < 50', 'alexiaAndrasObedient == False', 'all_actors["alexia"].flags["jezera_influence"] > all_actors["alexia"].flags["andras_influence"]',), depends=('alexia_med_corruption',), run_count=1, priority=pr_story)
    event('alexiaJezVisits', triggers="week_end", conditions=('jezCorVisits < 3','alexiaJezObedient == True',), depends=('in_her_hands',), group='ruler_event', priority=pr_ruler)

label alexia_med_corruption:

    $ midCorHappened = True
    show smoke transition
    pause 6
    show bg31 behind smoke with dissolve
    pause 1
    hide smoke transition

    scene bg31
    show alexia intro neutral at midleft with dissolve

    "Alexia hummed to herself as she carried a pair of wooden buckets up the rolling hillside. A light breeze ruffled the tall grass to either side of the dirt trail. The faint sound of activity rose from the village below."
    "This was not the first time she’d made the trek this week. Not even the first time today. She was heading to the secret little garden of flowers that she’d been working on at the summit. Her plants were so hard to please. They always sang for more water."
    "It had everything. Petunias, Roses, Irises. In a sea of green hillside, it was a colorful landmark. A monument to the fact that Alexia lived here."
    "The first sign that something was off, was the absence of a frequent companion. The cat that had a home in a nearby tree wasn’t there at this afternoon. Despite herself, she was almost disappointed. He was a constant, almost always in his little perch."

    show alexia intro concerned at midleft with dissolve

    "But, when she reached the hilltop, where her garden was waiting, her jaw fell. She even dropped the buckets to the ground."
    "In the mere hours since she’d last been there, something horrible had happened. Something impossible. A large sapling was bursting out of the ground in the middle of the plot for the daisies. "
    "The wood of the invader was a repulsive black."
    "But, the effect it had extended to the entire garden. Long obsidian tendrils poked out of the dirt in all of the other plots. The sapling’s roots. Wherever it went, it brought death and chaos. Flowers that had hours before been fine were wilting."

    "She sunk to her knees."

    al "How could this have possibly happened?"
    al "I was here just hours ago. This is monstrous. This is impossible. I worked so hard to make this place perfect. "
    al "This was my private place."

    "Her eyes narrowed in on the sapling. Her heart swelled with emotion. It was disgusting. It was vile. It had destroyed the garden that she’d cared so much about. She should bring an axe and chop it down. She should destroy it."
    "She rose, and approached the sapling cautiously. It was almost as tall as she was, yet it was still thin and weak. Perhaps she could simply snap it in half with her bare hands. Let the broken black husk of the invader serve as the tombstone to this place that she loved."
    "It looked so smooth. Unnatural yet oddly appealing. In a strange way it was almost…"
    "Almost...beautiful…."
    "The tree shook slightly. It rattled the same way old bones do."
    "Then, in the center of the trunk, an eye opened. It’s wide iris looked directly at Alexia. It surveyed its new home. Alexia put her hands over her mouth. The eye looked at her with judgement. She felt undressed."
    "The eye swiveled around taking in the sights of the garden. Then it refocused on her."
    "Alexia felt her feet glued to the ground. Did she want to scream at it? Did she want to run from it? Did she want to understand how it had come to be."

    quest "You’re confused."

    "Alexia felt her mouth open, without understanding why."

    al "I’m afraid."

    quest "You’re confused. Why are you confused?"

    "Alexia’s mouth spoke again."

    al "Because you’re strange. You’re wrong. This is wrong. You don’t belong here?"

    quest "I don’t belong here? Are you sure?"

    al "…"
    al "No."

    quest "Come here. Will you still feel I don’t belong here if you come to know me?"

    "Alexia couldn’t argue with that logic. Yet, there were still voices in her head screaming. What had happened to her garden? How can such a black vile thing be trusted."

    show alexia intro aroused at midleft with dissolve

    "She approached the tree and put a hand on its perfect trunk. At once she felt a fire, spread through her body from the point of contact. It settled between her legs."

    al "Ah."

    quest "Now do you know me? Now are you confused?"

    al "I-"

    scene black with fade

    "Alexia blinked."
    "Alexia saw a blue storm rage overhead above a land where the trees grew from up to down. The broken incoherent landscape was as overwhelming and consuming as the storm over head. Yet, it too was almost beautiful."
    "Alexia blinked."
    "She was standing in front of a doorway. Inside all she could see was a winding traverse of paths. The structure was old. Writing carved into it had long since been erased. "
    "But, the area around the doorway was all wrong. The sand was pure crimson, and the sky was illuminated by dancing colors. Alexia had not been too many places, but she knew that this was not anywhere she’d ever even heard of."
    "Alexia blinked."
    "She was naked and kneeling on some strange platform. She gazed forward, and a familiar face gazed back at her. Rowan. The man she loved. The man she’d centered her entire life around. "
    "She wanted to open her mouth and tell him about the flower garden. About that beautiful horrible sapling. But, she couldn’t speak."

    if all_actors['alexia'].relation > 50 and avatar.corruption > 30:
        "Instead, she was forced to watch on in silent horror as the face in front of her distorted and twisted in on itself. Bones and cartilage twisted and contorted unnaturally. When it finally finished, she was staring at an entirely new, entirely different face."
        "The question was just if it was still Rowan’s face at all?"
        
    elif all_actors['alexia'].relation > 50 and avatar.corruption < 31:
        "Instead, she was forced to stare straight ahead as something happened to her. At first it was a little bit painful. It was only through him she knew something was happening. His mouth gaped in shock...in disgust at the changes that were happening. He was disgusted by her."
        "There was a creaking sound. Her entire face was shifting. Changing. Would she even recognize herself when she was done? Would he?"

    else:
        "She stared at Rowan’s face for a long time. The longer she looked the more angry she got. How could he just look at her like that? How could he expect her to keep on staring at him forever? Didn’t he know that she was her own person? That she didn’t owe him anything?"
        "Fuck him. Fuck him. Fuck him. Fuck him. Fuck him. She spat in Rowan’s face."

    "That was when the silence was broken. A single statement that pierced the veil."

    show rowan necklace neutral behind black 

    ro "Why?"

    "Alexia didn’t know. She blinked."

    if alexiaSeparateRoom == False:
        scene bg9 with fade
        show alexia white concerned at midleft with dissolve
        "Alexia felt cold. She blinked twice more, but the world around her didn’t fade away anymore. She was in bed with Rowan. The cold was the breeze through the slightly opened window."
        "Alexia rose from bed and shut the window. There was sand in her eyes."
        "Just what had that dream been?"
        "She looked back at Rowan. Her arm stretched and unstretched." 
        "The garden, the tree, that strange cacophony of images? She’d never had a dream like that before. Hell, she’d ever even kept a garden when she lived in Arthdale."
        "She had wanted too, though."
        "Rowan was on his side snoring loudly. It had been years since the peaceful post-war days. But, he still looked the same. Or at least mostly the same."
        if avatar.corruption > 30:
            "But, looks could be deceiving..."
        else:
            "After all, when it came down to it, she was the one who’d changed most..."
        al "...Rowan, I…"
        "She shook her head. What was there to even say to him?"
        show alexia white neutral at midleft with dissolve
        "Maybe she shouldn’t have shut the window. Alexia decided that perhaps she needed some air. Some real air." 
        "Alexia walked over to the closet. She needed to get dressed."

    else:
        scene bg7 with fade
        show alexia white concerned at midleft with dissolve
        "Alexia felt uncomfortable. She was sweating. She blinked twice and looked around. She was back in her guest room. All the blankets on her must have trapped the heat."
        "Just what had that dream been?" 
        "She stretched her arms and let out a big yawn. Her eyes scanned the room. It felt like there should be something else here."
        "The garden, the tree, that strange cacophony of images? She’d never had a dream like that before. Hell, she’d ever even kept a garden when she lived in Arthdale."
        "She had wanted too, though."
        "Alexia wrapped herself in her arms. Even that element of touch felt good. "
        al "I shouldn’t have wine before bed."
        "She rose from bed and walked automatically to her closet. The room had a malaise hanging over it. It was too stuffy and too quiet. It made Alexia want to get a bit of air. Use a walk to get that dream out of her system."
        
    scene cg262 with fade
    show alexia 2 necklace neutral behind cg262

    "The wind swept softly over the black Bloodmeen sky this morning. Alexia could feel it clearly from atop one of the unused castle spires that pierce the clouds. From this vantage point she could see the peaks of mountains miles away. The snow on their peaks was so beautiful."
    "Alexia brushed her hand along the stone railings. This was no the first time that she’d come up here. She liked to take private walks to clear her head. It was all in the castle, so her captors didn’t mind."
    "She looked over the railings and found a seemingly endless drop. From her readings, she’d learned that being thrown from the spires had once been a common execution method here. So it was strange that she found this a place of peace."
    "Alexia breathed in the air. It was rather thin here. It was easy to get light headed. Perhaps that was the point?"

    al "Sometimes, I feel like you don’t live out here, Solansia. That this is a place you can’t reach."

    "She spoke out towards the rising sun."

    al "Mother taught me that you were always watching over us. That you cared for your children above all else. "
    al "But, if you do, why did this all happen?"
    al "So, I have to believe it’s something about the place. That you want to help, but you can’t. Otherwise, mother was wrong."
    al "..."
    al "The more I think about it, the more it feels that mother was wrong about a lot of things…"

    "The back of her hand brushed against her bosom. Even that felt good."
    "She turned the corner of the spire, and found herself staring at something she hadn’t expected to see. Something that shook her bones."
    "Many of the spires had little gardens at the top. Because this was Bloodmeen, and thus designed by demons, they often had demonic roses or thickets of spiky plants designed less to lighten the place up and more to terrify. They clung to life on the moisture of passing clouds."
    "But, this garden had something she’d never seen before."
    "There was a tall strong hardwood tree bursting out of the ground, with its uppermost branches entwining with gargoyles on the spire. It was a tree that had grown together with the building. It was an astonishing sight, unlike anything she’d seen before…"
    "...and the wood of the tree was absolutely pitch black. All color drained from Alexia’s face."
    "It wasn’t the same tree exactly. It looked more real, more natural, then the gangly creature of last night. It was also old and strong, unlike the strange ephemeral sapling. The lack of a giant eye was also a fairly notable distinction."
    "However, the wood was the same unsettling black. More to the point, it certainly had a dark aura to it. As Alexia stood in its presence, she felt it like a gravity pool urging that she come closer."

    menu:
        "Flee from the tree.":
            $ released_fix_rollback()
            $ midCorFlee = True
            "Alexia took a step backwards. Then another. In moments, she broke into an open run away from the nightmare come to life. How had that got there? Had it always been there?"
            "She ducked back inside the building. Suddenly she didn’t seem to mind the stuffiness quite as much. Her mind was racing. Her heart was racing."
            "What had she just seen? And why had she...why has she wanted to approach it, just like she had in the dream?"
            if alexiaSeparateRoom == False:
                scene bg9 with fade
            else:
                scene bg7 with fade
            show alexia 2 necklace concerned at midleft with dissolve
            "She curled up in the corner, with her arms wrapped around her legs. Tears had started rolling down her face."
            "There was something strange going on. Something horrifying. That couldn’t have been an ordinary tree. It must have been somehow magic. After all, surely someone like Jezera or Clionha had the power to warp the dreams of their subject."
            "Alexia balled her hands into a fist."
            "But, did they have the power to make someone like those dreams?"
            if alexiaSeparateRoom == False:
                show rowan necklace naked at midright with dissolve
                ro "Alexia, are you okay? What’s wrong?"
                show alexia 2 necklace happy at midleft with dissolve
                al "It’s nothing really. You don’t have to worry about it at all. I’m just still getting used to this place. Even after all this time, it’s still so strange, you know?"
                al "...That’s all."
                al "That’s all."
            scene black with fade
            "Alexia has now reached medium corruption. Her reaction to different events and scenes will change as a result. At this rate, Alexia’s corruption will only grow and grow…"
            return
            
        "Approach the tree.":
            $ released_fix_rollback()
            $ midCorFlee = False
            "Alexia’s eyes glazed over slightly. What would be so wrong with taking a closer look? It wasn’t every day one saw the figment of a dream come to life. Maybe, it would just be a strange coincidence"
            "Her hips swayed ever so slightly as she stepped towards it. The dream had already started to blur, but that fire she’d felt hadn’t."
            "Her hand touched the exterior of the tree. Hard. Strong. Smooth. The smoothness was the most unnatural element. It should have felt more coarse and bumpy. But, what she didn’t feel was that same fire shoot up her body."
            "She stroked the tree softly. Perhaps it had all been her mind playing tricks on her. Perhaps she’d seen this tree before, and the reason there was a black tree in her dream was because her brain was playing tricks on her. Certainly this tree didn’t have a large eye in the middle of it."
            "Alexia sighed and slumped down against the tree. It was a good spot to lay against. Despite the tree’s hardness, it almost felt like laying down in freshly cleaned sheets."
            "She wasn’t even cold anymore. Her conscious mind didn’t even process it, but the closer she was to the tree the less she felt the high altitude wind and the chill it sent through her body."
            "She closed her eyes…and at once images went through her head."
            scene black with fade
            if all_actors['alexia'].flags['andras_influence'] > 6:
                "The strong embrace of a hand on the back of her neck. The knowledge she was about to...taken…and that there was nothing she could do about it. The feeling of a massive cock filling her body…"
                "...slamming into her with a strength not held back by sentiment or concern. The man wanted to user her body, and didn’t care what she thought on the matter…"
                "...Not that she disliked it..."
            elif all_actors['alexia'].flags['jezera_influence'] > 6:
                "The scent of female anatomy mere inches from her face. The feeling of her arms and legs tied down. No escape to be found anywhere. That intoxicating scent coming closer and closer..."
                "...Then smothering her. Making it impossible to breathe. Only one thing to do…"
                "...Open her mouth and put her tongue to work."
            else:
                "Hands were running up and down her body. It could have been two. It could have been a hundred. But, everywhere they touched, like rippled in a pond, electricity moved out in every direction. A thrilling, erotic lighting…"
                "...It was everywhere now. In her legs, in her arms, in her bosom. Her body squirmed outside of her control…"
                "...Everything was lost to the pleasure. Everything was the pleasure…"
            "When she opened her eyes, she found her own hands moving. They were rubbing her breasts, and her legs. Alexia gasped out. How had her body gotten so sensitive, so eager, in such a short amount of time?"
            "In a rush, she threw off her dress. She didn’t need it. The tree would be her warmth."
            #cg1
            scene cg301 with fade
            show alexia necklace naked aroused behind cg301
            pause 3
            "Now, without anything to get in her way, her hands went back to work. A long feminine groan slipped past her lips at the exact moment that two of her fingers sank into her cunt. Her other hand was busy pawing at her nipples, tweaking and rubbing them."
            "It had taken some time, but she could feel it now. Her body was alight. There was fire running through her veins. Fire between her legs. She felt like she bursting with constrained heat. She liked how that felt."
            al "Ah..."
            "Normally she liked to put more effort into rubbing her clit, but her fingers sank deep into her sex. It felt good to have something inside of her. She liked how it felt too."
            "That one thought prevailed over the others. She liked this. She liked the frantic movement of her fingers into her body. She liked the lewd display she was putting on. She liked the thought of someone coming up here and seeing what a slut she was."
            "That’s right. What a total slut."
            al "Fuck. Fuck. Fuck. I’m a slut. I’m a total slut. Ah."
            "The sound it made would be unmistakable. The watery sound of a pussy in use. So too would the smell. There was something deeply erotic about the knowledge that this place would smell like her lewdness if anyone passed."
            "Alexia worked her finger faster and faster. Building up to it. There was no restraint or consideration. Just a powerful desire to bring herself to orgasm. To bathe in the way that it felt."
            al "A slut. A slut. Ah. Such a slut. Such a fucking slut. Ah."
            "She was so close now. The heat was rising up. It was consuming her. It was mere moments from pouring out her body. Her fingers put everything they could into…"
            "Plop. There was an odd sound next to her. Alexia slowed down, though did not stop touching entirely, to see what it had been."
            #cg2
            scene cg302 with fade
            pause 3
            "One of the strange fruit growing high up in the tree had fallen right next to her. She used the hand that had been at her breast to pick it up and examine it."
            "Had it been...a gift for her? There would only be one way to find out…"
            "A voice in the back of her head pleaded for her to stop. Didn’t she understand what would happen to her if she indulged herself too much? Didn’t she see what was happening to her?"
            "Alexia didn’t listen to that voice. Instead she bit into the bizarre fruit."
            #cg3
            scene cg304 with fade
            show alexia necklace naked aroused behind cg304
            pause 3
            "The moment she tasted it’s sweet nectar, her head went fuzzy. It tasted like it had been dipped in honey. She took another bite. Orange juices dribbled down her chin, down her breasts, over her stomach…"
            "Her body was stained by its juices. The taste of it made her head buzz. It was so hard to think. She just wanted more."
            "The fingers between her legs slowly pumped away. They kept her riding the edge of a coming orgasm. So close she could feel it, but still building and building the longer she kept this high."
            al "I….Oh…"
            "She couldn’t help herself. She couldn’t stop biting into the sweet tasting fruit. She couldn’t stop fucking herself at just the right pace to keep her moaning and squirming."
            "With all the liquids running over her body, she was making herself dirty. The sticky filth of the fruit’s juices stained her skin, and pooled together underneath her with her own wetness. The strange mixture watered the dark tree."
            "Alexia’s mind had long since faded off. It was lost in the overpowering high that both the fruit and the eroticism of the moment offered her. Instead it was like her body was acting on its own. Like a marionette. "
            "Her empty moaning called out into the distance. It was like a cry to the heavens. How could she even care if she was being too loud? If everyone in the entire castle could hear what a fucking slut she was, that would make it all the sweeter."
            "Her nether region spasmed. Her cunt ache for pleasure. The fire in her body ached for release. The high in her mind ached for complete whiteness. The entirety of Alexia’s being cried out to go over the edge."
            "And it was obliged."
            quest "Cum."
            #cg4
            scene cg303 with fade
            show alexia necklace naked aroused behind cg303
            pause 3
            al "Ah! Ah! Ah!"
            "Alexia gasped and squirmed and spasmed. Her body was in the midst of pure release. The fire that had swept her insides exploded out with all of her energy. It was an eye rolling, mind melting orgasm."
            "In the process, her spasming cunt let loose a torrent of her own juices. It watered the base of the dark tree."
            "When the ghost of the orgasm had passed, it left the limp form of Rowan’s wife, curled up against the trunk. Her eyes fluttered weakly, and her mouth hung awkwardly. Her form was devoid of all strength, all energy."
            "As the fog over her head cleared, a single thought pierced through. If that what was the pleasure of living in a place like Bloodmeen, then why would anyone ever leave?"
            "But, that thought was followed by a second, less accepting one. A curiosity. Why had she done that? Didn’t she know that she shouldn’t have approached the tree? After all, it was surely magic. It had to be trying to do something to her."
            "...Something…"
            quest "Is this where you heard that noise from?"
            "Alexia blinked awake. There were voices in the distance, figures talking. With that realization, came the second realization that she was naked and covered in filth."
            quest "Do you think it’s some kind of infiltration?"
            quest "Idiot. Since when can humans fly?"
            "Alexia scrambled to her discarded dress, and threw it on as quickly as she could. That had been a fun...diversion, but it would be better if no one found her. Especially not like that."        
            scene bg14 with fade
            show alexia 2 necklace happy at midleft with dissolve
            show jezera happy at midright with dissolve
            "Later on, that same day, another odd occurrence happened. Alexia was walking down the hallway when she ran into Jezera. Her Mistress looked her up and down, as the woman always seemed to do, and kept going."
            "But, as she passed, she let loose a sly little comment."
            je "Someone is looking sunny today. Did something fun happen that I had the misfortune to miss?"
            "Alexia didn’t respond to the demoness. But, when she reflected on the encounter, she realized that Jezera had been right."
            "She really had been smiling."
            $ change_corruption_actor('alexia', +5)
            scene black with fade
            "Alexia has now reached medium corruption. Her reaction to different events and scenes will change as a result. At this rate, Alexia’s corruption will only grow and grow…"
            return


######################################################################################################################################
######################################################################################################################################
######################################################################################################################################

label in_her_hands:

scene black with fade

"{b}The Seed Was Always There.{/b}"

scene bg14 with fade

"Muffled footsteps tapped their way down the hall, but at this late hour there was no one awake to hear them."
"The footsteps crept along, past the living quarters down to the entry hall. All the sentries were outside on the gates. There was no one watching inside of the castle. No one to watch Alexia creep outside."

scene bg3 with fade
show alexia 2 necklace concerned at midleft with dissolve

if alexiaSeparateRoom == False:
    "Back in their room, Rowan was softly snoring. In his dreams, was his wife still sleeping beside him? This wasn’t the first time she’d snuck out in the middle of the night. He seemed none the wiser."
    "Alexia knew where she was heading. She’d found the place a few days prior and hadn’t been able to stop thinking about it since. It was just at the edge of the outer walls, tucked away in a grove of the strange trees that grew in the northern wastes."

"It was a large pond. Perhaps large enough to be considered a small lake. It stood alone in a large clearing, surrounded by menacing trees looming on every side."
"The moon shimmered atop its crystal waters. When she’d first seen it, Alexia had not thought it possible that such a thing could exist out here." 
"An oasis of beauty amongst the desolation."
"Alexia walked over to the edge of the pond and stared at her own reflection in the water. Despite the smooth perfection of the water’s surface, her own image was distorted."
"Without a word or a second’s hesitation, she worked one of her arms out of her dress. And then the other. Moments later, her garment fell to the earth at her feet."

show alexia necklace naked concerned at midleft with dissolve

"Now exposed, she stared at the reflection a moment longer. She’d thought about doing this since she’d found the pond. It reminded her of the place where she’d used to practice back home. That old lake by her father’s house."
"She put her hands on her head and started to sway her hips side to side. The motions were awkward, the gears had not been worked in a long time. But, she had always been a natural dancer. It came back to her quickly."

show alexia necklace naked at midleft with dissolve

"An hour later, and she was a blur of motion. Spinning and swaying, dipping and bowing. All of the dances she knew were twirls and circles. She twisted her body rhythmically as though guided by the sounds of unheard drums and flutes."
"How many years had it been since she danced like this? How did she even remember all of the steps? The longer it went on, the deeper and deeper the smile on her face became."
"What would Rowan think if he knew she was dancing like this, exposed in the moonlight? What would he-"

show alexia necklace naked angry at midleft with dissolve

"But, why should it matter what he thought?"
"She’d always studiously acted in a way that wouldn’t reflect badly on him, even while he was away. She shouldn’t do this. She shouldn’t do that. What would Rowan think? What would people say if they saw Rowan’s wife dancing naked by the pond?"
"What people would say didn’t seem to matter as much now."
"She stopped in place, forgetting where she was for a moment. The memory took up all the mental space needed to dance. But, then something brought her crashing back to reality."

show alexia necklace naked shocked at midleft with dissolve

quest "Don’t stop. It’s been such a delightful performance."

show alexia necklace naked concerned at midleft with dissolve

"Alexia looked around frantically. Her hands went flying to her body to cover whatever dignity could be salvaged. Someone had seen her? No no no no no no. That was impossible. She’d…"

show jezera happy at midright with dissolve

je "You can relax, my dear. It’s just me. Your little nighttime dalliances are safe with me."

"Alexia’s jaw dropped. Jezera strode out of the shadows, nibbling on an apple. If there was anyone who this knowledge could be turned into a weapon by, it was her. Though, if there was one person who wouldn’t be scandalized it would be her as well."

if alexiaJezeraSex > 0:
    "After all, not even their past...affairs...had reached Rowan’s ears. But thinking about that only made Alexia all the more red faced."

je "I never knew that you had a performance like that in you. How have you been my guest for so long now, yet I haven’t seen that?"

"She strode closer, bridging the distance between them. Alexia took a step back. "

je "Fruit, my dear?"

"She held out an apple for Alexia. It gleamed with juices from the light of the lake. Alexia opened her hand and grasped it. Jezera smiled at her gently."

al "You weren’t...supposed to see that."

"She took a bite of the apple. Juicy. Delicious. She really was quite famished."

#jez  smirk

je "And yet here I am. You happened to have selected one of my favorite spots in the entire castle as the place where you weren’t supposed to be seen. Perhaps you’re the trespasser. Perhaps, I ought to give you a few swats on the rear."

"Alexia lowered her eyes. The fruit dropped from her hands. Had she really thought that this magical place would be undiscovered? Of course, Jezera would have known about it. The castle and its vicinity was her territory."

#jez happy

je "Oh, keep that chin up, pretty dove. I was joking. It’s quite a beautiful little spot. More beautiful then you’d know even. I’d be quite the hypocrite if I shamed you for being attracted to it."

show alexia necklace naked at midleft with dissolve

"Alexia chuckled softly."

al "I suppose so. What did you mean by more beautiful than I’d know?"

je "Perhaps I’ll show you, someday. It’s quite the sight."

show alexia necklace naked concerned at midleft with dissolve

"As she said it, her eyes lowered slightly to take in another sight entirely. Alexia noticed for the first time once again that she was still naked. Without even thinking, she turned away to escape Jezera’s gaze."

je "Oh come now. It’s nothing I haven’t seen before."

"Alexia sighed. She was right, of course, but it wasn’t like she liked Jezera being right either. Jezera seemed more and more familiar by the day. With a reluctantly sigh, she turned back around and put her hands on her hips."

show alexia necklace naked angry at midleft with dissolve

al "Fine, just get all the oggling out of the way now, you lech."

"Jezera giggled, eyes shamelessly taking in Alexia’s form."

je "I’m glad we’re on the same page."
je "I hope you’d be a good girl and indulge my curiosity. But, what brought on this nocturnal adventure of yours? Or perhaps this is a tradition that I am just now becoming aware of…"

show alexia necklace naked concerned at midleft with dissolve

"Alexia shook her head."

al "No. No. It’s distinctly...distinctly a one time occurence. I just missed dancing. Back in Arthdale, I would dance all the time."

show alexia necklace naked sad at midleft with dissolve

"Alexia chuckled darkly to herself."

al "It’s actually...well, it was how I convinced Rowan to see me as more than his childhood playmate."

show alexia necklace naked at midleft with dissolve

"Jezera clapped softly and smirked. It was exactly the kind of thing she would approve of."

je "And you missed it. Thus, the excursion to my little pond for a twirl or two?"

al "Yeah."

if alexia_has_sex_with_jezera_during_demon_book:
    je "In fact, I firmly recall you telling me about your love of dancing in the past, no?"
    #dancing CG
    scene black with fade
    "Alexia felt a shot of embarrassment. She remembered that day when she’d told Jezera all too well. The tome. Tea time together."
    "..What had come after tea"
    scene bg3 with fade
    show alexia necklace naked at midleft with dissolve
    show jezera happy at midright with dissolve
    
je "I just have one question for you, my dear."
je "Why the choice of...apparel?"

show alexia necklace naked concerned at midleft with dissolve

"Alexia kept her mouth closed. She hadn’t really considered it at the time. She just took off her clothes without thinking. Why had she done that?"

show alexia necklace naked sad at midleft with dissolve

al "I wanted to see my reflection."
al "How much I’ve changed. Aged."

"Jezera tilted her head. There was truth to the answer. It simply hadn’t been the whole truth. But, what would a demoness say if Alexia told her that she found the experience...thrilling?"
"Jezera didn’t reply with words. She took another step closer. This time, Alexia didn’t back up. Then, in a sudden motion, she brushed her hand along Alexia’s face. How could the hands of a monster be so gentle?"

je "I see it now. This entire excursion...you feel cooped up, don’t you?"

al "I-"

je "Like you’re decaying. Losing the luster you once had, while trapped. Like a caged bird wondering if you’ll ever see the sun again."

al "..."

show alexia necklace naked angry at midleft with dissolve

"She tilted her head to the side, refusing to meet Jezera’s eyeline."

al "I am a prisoner. Your prisoner."

show jezera neutral at midright with dissolve

"Jezera shook her head."

je "In a sense yes. But, in another sense...you are your own prisoner. Rowan’s prisoner. The prisoner of all the lords and elders who told you how to live your life."

show alexia necklace naked concerned at midleft with dissolve

al "No. I’m...No."

"Jezera sighed and took a step back, leaving Alexia some space. It wasn’t true. Right? She was just making up excuses not to be the subject of Alexia’s resentment. This woman had kidnapped her and was now pretending to be innocent."
"Still, it wasn’t like she had many other people to talk to around here."

show alexia necklace naked angry at midleft with dissolve

al "I haven’t seen my home in so long. I haven’t even seen green grass. The only sun in my world is that is mellow washed out...thing...that hovers overhead. How can you tell me that you’re not the one keeping me here?"

"Jezera started to say something. No doubt a witty retort. But, then she thought better of it. For a brief second, there was a crack. No devious smirk. No eternal confidence. But, when an answer came to her, it all came roaring back with it."

je "You’re right. I am keeping you prisoner in this castle. Not my ideal state of affairs. I’m quite fond of you really. But, you are the key to the loyalty of our most valuable general. "
je "Would that I could without losing leverage over one of my most reliable catspaws, I’d let you walk out of here right now."
je "I’ve done what I could to make your stay comfortable. You may be bound in some ways, but I’ve tried to unbind you in others. I owe you that much, at least. And thus far you haven’t seemed entirely inclined against it."

if alexiaSecondsSex:
    scene cg203 with fade
    "Alexia shifted uncomfortably. Certainly, Jezera’s insistence on exploration had not been as unpleasant as she might have once anticipated."
    scene bg3 with fade
    show alexia necklace naked angry at midleft with dissolve
    show jezera neutral at midright with dissolve
    
je "Still, I cannot avoid the matter at hand."
je "Your enmity is not without my understanding or consideration, my dear. It truly isn’t. But, since I cannot let you walk out the gate here and now, let me at least give you something else. A taste of the kind of freedom that even a prisoner can have."
je "For an evening, I want us to not be Mistress and vassal. Just friends. Two women uncontent with the place that the universe set for us."
je "I don’t ask for much. Just the tiniest sliver of your trust."

"Jezera extended her hand to Alexia."

je "You want to see the natural sun? I can give you that again."
je "Come with me. There are some things I want to show you."

show alexia necklace naked concerned at midleft with dissolve

"Alexia stared down at the outstretched hand skeptically. How could she trust this woman, after everything that had happened to her? Jezera did nothing but lie. Nothing but deceive. And yet, she was the only one who seemed to understand what she was going through…"
"...and she was saying she’d let Alexia see the real sun again…"


label jezCorMenu:

menu:
    "Accept her offer.":
        $ released_fix_rollback()
        jump wholeNewWorld
        
    "Refuse.":
        $ released_fix_rollback()
        "This option may lock off certain segments of content. Alexia will have made her choice. Only select this if you really mean it."
        menu:
            "I mean it.":
                $ released_fix_rollback()
                "Alexia closed her eyes. The things that Jezera was saying sounded good. Letting her guard down for just a night. Accepting that Jezera might not want bad things for her."
                "It was true that in recent days she’d had so many thoughts and fantasies. It had been driving her wild. No matter what she might claim, Jezera was a part of them. She had thoughts about Jezera. Feelings about her."
                "All of that was true. But, something else was as well."
                al "You’re a liar."
                show jezera happy at midright with dissolve
                je "Well it’s not like I don’t understand a little bit of…"
                al "No."
                "She took a step forward. "
                al "I don’t trust you. This entire thing smells too fishy. I don’t know why but…"
                al "Did you know I was coming down here? Did you come down on purpose?"
                #jez surprised
                show jezera neutral at midright with dissolve
                je "What!? I.."
                "Alexia put up her hand. It had taken her a second. She’d almost believed Jezera’s little speech. But, ever since she came here, when had Jezera ever done anything but try to get into her panties? Every inch of trust had been exploited."
                show alexia necklace naked angry at midleft with dissolve
                al "Did you come down here on purpose knowing I was here? I know that you have the power to see things far away."
                show jezera happy at midright with dissolve
                "Jezera giggled slightly."
                je "You say such horrible things about me, but frankly I’m mostly just flattered that you think I’m capable of such manipulations. I’m flattered."
                al "Oh yeah?"
                "Alexia reached down and grabbed her clothes, covering her nakedness behind them. A screen layer between the two women."
                al "Well you can be flattered somewhere else."
                al "I’m sick of it."
                show jezera neutral at midright with dissolve
                al "You can kill me whenever you want. You can probably control my mind or turn me into a bat."
                al "But, all you do is play these fucking games with me. A grope here. A shoulder rub there. I know what you’re doing. I may be-"
                al "I may…"
                al "..."
                al "I’m a different woman from the one who you first brought here."
                al "Maybe, you’re right. Maybe all of my life I’ve been tied down by all the expectations people had of me. What people wanted from me. Maybe I need to explore what I want."
                "She jabbed a finger at Jezera."
                al "But, what I don’t want is to explore it with you. "
                "Jezera stood in place as if she stopped functioning. That usual smug grin on her lips just wasn’t there. It was an eerie sight. Alexia was the one without any clothes, but Jezera was the one who was naked."
                je "..."
                je "Are you sure about that?"
                al "I couldn’t be more sure."
                "Jezera sighed."
                #jez smirk
                je "A pity. After all the ways I’ve changed you already, you still don’t understand the source of your new perspective. But, I’m not mad. You’ll come crawling back to me before long. I always get what I want."
                je "Always."
                "Without a further word, the demoness turned on her heels and began the short trek back to the castle. Alexia wanted to shout at her back, saying that it would never happen. Where did that bitch get off saying that?"
                "But, she didn’t want to press the matter any further. Already she was walking on thin ice. So, Jezera walked into the distance, with nary a further word exchanged between them."
                scene bg9 with fade
                show alexia 2 necklace concerned at midleft with dissolve
                show rowan necklace concerned at midright with dissolve
                ro "You want me to try to keep you away from Jezera."
                "Alexia leaned against the wall and nodded, trying not to show the full weight of her feelings. A true fight between Jezera and Rowan would be bad for everyone."
                al "I don’t know what she’s up to, but I just want to be safe. I don’t want to be rude to her. God knows she isn’t the right enemy to make. But, I’m scared of what she might try if I do spend more time with her."
                "Rowan nodded. He would never decline a request like that. It would mean she couldn’t work as part of the household staff too since Jezera had so much power over them."
                "Alexia gripped her arms to her chest tighter. Jezera had not retaliated at all for her defiance since the confrontation at the pond. She didn’t even seem to have acknowledged anything was amiss when they passed each other in the halls."
                "Just what was Jezera’s game here? What had she wanted with Alexia in the first place? Alexia was forced to wonder in silence."
                $ jezNTR = False
                return

                
            "Take me back to the menu.":
                $ released_fix_rollback()
                jump jezCorMenu


label wholeNewWorld:

show jezera happy at midright with dissolve

"Alexia slowly reached down and grabbed her hand. Jezera’s smile widened."

je "Close your mouth!"

al "What?"

je "I said, close your mouth!"

show alexia necklace naked shocked at midleft with dissolve

"Suddenly, Jezera leapt forward. Startled and totally overwhelmed by Jezera’s superhuman strength, Alexia was dragged along with her. The two women, captor and captive, landed with a splash in the middle of the lake and then sank under the water."
"If someone had been watching above the surface, they would have swiftly become very alarmed. After all, Jezera and Alexia never came up."

scene black with fade

"Alexia slammed her eyes shut as her body hit the water. She had expected to feel water all around her. And for a moment, she did. But, in mere seconds she mostly felt air, save for a small puddle that she easily could have stood up in."
"Alexia opened her eyes."

scene caveanimation with fade
show jezera happy behind caveanimation
show alexia necklace naked shocked behind caveanimation

"She was sitting in some kind of cavern. Above her head, the water formed a flat surface, as though it were on the ground. It still rippled from the impact of the two bodies crashing through. But, just as wonderous was what was all around her."
"It seemed that she was now in a small crystalline cavern. Everywhere she looked, blue sparkling lights sparkled out of the cracks. Light reflected around the room, illuminating gems all around. A swirling cacophony of lights."

al "...So pretty…"

"It was impossible. A rush of colour and sensation that she couldn’t have even imagined. Swirling all around her. Gems peeked out of every crack and crevice. Like a sea of stars."

je "In truth, I don’t know how it formed. It must have been here for hundreds of years. It might even predate the castle itself."
je "It’s a little secret that only I know. Well, now only you and I."
je "It was always hidden here under the surface. Appearances can be deceiving, my dear."

"Alexia nodded along softly to Jezera’s words. She was captivated by the light. Who could have thought these dark lands held a wonder like this…"

al "May I...may I have a second. Just to take it all in."

je "Of course, as much time as you need. This is my gift. To you."

"Sometime later, Jezera leaned down and extended her hand to Alexia once more."

je "If you’re not too set on being a prisoner, there is more I could show you. So much more. All your life squirreled away in a dinky hut. Let me show you something incredible."

"Alexia’s eyes trailed around the interior of the lake. The lights, the ethereal beauty of it all. It was so incredible. Something she’d remember for her entire life."
"This time there was no hesitation when she gripped Jezera’s hand."
"Jezera gave Alexia a reassuring smile, and then turned to the wall of the cavern. Her hand glowed an unearthly purple, and a swirl of sound and mist appeared. A portal. Alexia and Jezera went through it together."

scene bg10 with fade

$ jezPortals = 0
$ visitTundra = True
$ visitMarket = True
$ visitCliffs = True
$ visitLibrary = True

label jezPortalsMenu:

"Where to now?"

menu:
    "The Frozen Tundra." if visitTundra == True:
        $ released_fix_rollback()
        "They went to a small hamlet in the Frozen Tundra outlands. It was near the layline, which made it a convenient destination, But Jezera mainly chose it for the town’s secret beer brewing tradition. Alexia tried a mug and instantly understood why."
        "Long after each sip, it left a warm feeling in her belly. The beer was room temperature, but the drink was made of heat. To the people of the frozen lands, a drink like this could save lives."
        "The people here were warm and friendly. They marveled at the appearance of guests at all so far away from any major towns or trade routes."
        $ visitTundra = False
        $ jezPortals += 1
        jump jezPortalsMenu
        
    "The Night Market of Travelers’ Rest." if visitMarket == True:
        $ released_fix_rollback()
        "Then they were off to Travelers Rest just in time to see the famous night market. Jezera had to fly them overwater for nearly an hour to get there. The most incredible things in the world could be found at the night market. Every twist and turn made Alexia’s eyes grow wider."
        "Six armed beasts from the east locked in golden cages. Spices in green and gold and rainbow. Milk squeezed fresh on the spot by a big breasted half-minotaur. Though, nothing was as stunning as the strange array of people who walked through the market."
        "Light skinned humans. Dark skinned humans. Some as black as coal and some as pale as the moon. Some had strange piercings in places that it frankly hurt to imagine. Humans and non humans. Spotless lords and perfumed dancers from the empire."
        "Jezera picked a man at random from the crowd, the son of a pirate lord with an intricately styled beard, and bet Alexia that she could have him fucking her in a nearby inn within half an hour. Alexia laughed and demanded that Jezera make him cum in that time too."
        "Jezera walked out of the place with a smirk just fifteen minutes later."
        $ visitMarket = False
        $ jezPortals += 1
        jump jezPortalsMenu
     
    "Hidden cliffs of Mithras." if visitCliffs == True:
        $ released_fix_rollback()
        "From there, Jezera took her to the hidden cliffs of Mithras, at the far end of the Dragon’s Tail. The great mammalian beasts that roamed the waves allowed them on their backs for a ride. They took it all the way to the ruins of an ancient city."
        "Jezera showed her the hidden temples and passageways that non-magical human explorers had never been able to penetrate. Inside she saw old sites and buildings that almost no living human had seen before."
        "Alexia stood around marveling at the grand structures and unique designs. It was so different from the way people built houses in Rosaria. Did people really live this way?"
        "Jezera took great delight in showing off special segments. She was especially familiar with all the curses and magical items around. The way she described the place was almost like a living organism. The lines of magic were the lifeblood of the place."
        "In that way, even now it was almost still alive."
        $ visitCliffs = False
        $ jezPortals += 1
        jump jezPortalsMenu
        
    "The Hidden Library, Tharafin." if visitLibrary == True:
        $ released_fix_rollback() 
        "Jezera took Alexia deep into the woods of Ealoean to the hidden library Tharafin. Once well populated, it now lies mostly undisturbed, protected by magic from the passage of time, and the respect of all elves from the ravages of war."
        "The library was built inside of a great tree that stands taller than the largest tower and wider than a castle. Only through magic can one even get in or out."
        "Still, a few of the elves can be seen going through the halls, consulting the wisdom of ancient times. Alexia is left to stare at the vast halls in wonder. The books are gibberish to any besides the elves themselves. But the sheer number of them, in their millions, is daunting."
        "Jezera let Alexia explore through the building, looking at all of the wondrous art pieces and design elements. Even if one cannot read their great books, the mere comprehension of the sheer amount of knowledge stored is...daunting."
        $ visitLibrary = False
        $ jezPortals += 1
        jump jezPortalsMenu
        
    "Home..." if jezPortals > 1:
        $ released_fix_rollback()
        jump jezCorHome
        
        
label jezCorHome:

show alexia necklace naked sad at midleft with dissolve
show jezera happy at midright with dissolve

al "Can you take me home?"

je "Back to the castle? Already? The sun is only just coming up."

"Alexia shook her head. Her bangs cast a shadow over her eyes."

al "No. Home."

"Jezera opened another portal, and the two walked through it together. Hand in hand."

scene bg38 with fade
show jezera disguised smirk at midright with dissolve
show alexia necklace naked at midleft with dissolve
pause 0.5
show alexia 2 necklace shocked at midleft with dissolve

"Jezera and Alexia stepped out in a vast countryside. They stood on top of green grass, wet from the morning dew. As they appeared, a green dress appeared on Alexia’s body. An illusion in case locals walked by."

"Her eyes swept the horizon. So much green. So much life. It was exactly how she remembered it."

al "..."

show alexia 2 necklace concerned at midleft with dissolve

al "..."

"She sank to her knees. All the strength left her body."
"In the distance, the darkened night sky started to twist into a glowing yellow. The sun was rising. It was morning."

al "..."

show jezera disguised neutral at midright with dissolve

"She felt a hand on her shoulder and looked up. Jezera was looking at her with a face that she’d never shown before. Almost like...almost like sympathy."

je "Do you want to stay here a bit longer? We can watch the sunrise here."

"Alexia looked around. This place seemed vaguely familiar. Not somewhere she’d been often. But, definitely somewhere she’d been before."

al "Can we go back to Arthdale?"

#if not rebuilt
je "We can. But, you know it’s still a ruin, yes? You might not find it such a pretty sight."

#if rebuilt TODO
#je "We can. But, you understand it’s a changed place? In some ways, that might be worse then if it was gone entirely."

"Alexia shook her head softly."

al "I know. I know. I just...I want to be there to see the sunrise."

je "..."
je "Okay. Let’s go."

"The two made it much of the way to Arthdale. Alexia’s pace grew slower and more unsteady the longer that they went on. Eventually, Alexia herself asked to stop. She’d changed her mind. She didn’t want to go any further."
"They watched the sun rise there on that Rosarian road, mere miles from the place Alexia once called home."

scene black with fade
show jezera disguised smirk behind black

"About two hours later, Jezera was leading Alexia down the intricately planned streets of Qerazel. Alexia marveled at the variety of colours they made buildings in. Red, blue, purple, green, gold, white, orange…"

je "If you don’t mind, this stop will be more for my personal enjoyment."

"Jezera led Alexia into domed building whose perfumed smell even radiated out into the street. Inside was a labyrinth of silk and smoke."

scene bg24 with fade
show alexia 2 necklace shocked at midleft with dissolve
show jezera disguised smirk at midright with dissolve

al "This is a…?"

je "A den of sin? Home of depravity? A jolly good time?"
je "It’s a brothel, yes. {i}The Empress of the Waters{/i}. This place is an old favourite of mine, from my own experimental days."

if 'castle.buildings["brothel"].lvl >= 1':
    je "You should recognize the design. It’s as much a second home to Shaya as it is to me. One could even say more so. Naturally, we took it as the template when designing our own services."
    je "Still. There is nothing quite like the original."

"The area where they were standing was fairly empty, but in the distance Alexia could hear muffled voices. Moans and gasps mostly. This must not have been the normal entrance. She did say she was...intimately familiar with this place, after all."

mada "Two?"

je "Two should be sufficient, yes. Unless my companion wants a little taste for herself."

"Jezera was speaking to an elder woman with a thick accent, no doubt the madam. Alexia’s cheeks flushed. Were they talking about her?"

al "No no, I’m just going to...just going to watch."

je "Just two then."

"Alexia and Jezera were ushered from there to a side room. A maze of silk that swirled around in a circle leading to a large circular bed. Tables and chairs were positioned around along with copious goblets and fruit."

show alexia necklace naked shocked at midleft with dissolve
show jezera naked happy at midright with dissolve

"When they were alone, Jezera snapped her fingers. In a whisk, the illusion of a dress vanished from Alexia’s shoulders. More than that, Jezera’s pale faced disguise, and clothing, disappeared at the same time."

je "No need for such deceptions here. They know me here. Nor are they particularly judgemental about nudity."

show alexia necklace naked concerned at midleft with dissolve

if 'castle.buildings["brothel"].lvl >= 1':
    "Alexia gripped her forearm. It was said that the prostitutes of the empire knew secret sexual arts. Having seen Shaya first hand, it was almost certainly true. Just what did those arts entail? What did it feel like…"

else:
    "Alexia gripped her forearm. It was said that the prostitutes of the empire knew secret sexual arts. Just what did those arts entail? What did it feel like…"
    
al "Do I have to watch?"

je "I’m not forcing you to do anything. If you want to leave here right now, you only have to say the word. It’s not about whether I want you to watch."
je "But, it’s not about what your father or whoever indoctrinated your mind back in Rosaria wants you to do either. They’re the reason you’re afraid to be seen dancing."
je "It’s about whether you want to watch."

"Alexia wondered what she wanted. That was the question of the hour, wasn’t it? The fact alone that she’d accepted Jezera’s proposal was proof of that. Her own desires had never been less clear to her then they were now."
"What did she want? Did she want to watch her captor in the arms of trained prostitutes? Bodies rubbing together. Touching. Kissing. Doing things to each other she could only imagine."

show alexia necklace naked aroused at midleft with dissolve

"Alexia walked over to one of the tables and filled the goblet with red wine. She poured down half of it in a single gulp. Some even spilled down her chin, leaving a crimson stain. It left her head pleasantly fuzzy."

if 'castle.buildings["tavern"].lvl >= 1':
    "She knew the taste. Indarah had a few bottles of this, though they only tended to come out on special occasions."

"Did she want to watch Jezera fuck these women? Would watching that turn her on?" 
"Yeah. It would."

al "...We can leave if I’m not feeling too good?"

je "Any time you want. You have only to say the word."

"Alexia padded over to one of the chairs, and lowered herself into it. She didn’t have the courage to say anything more. Besides, from the look that Jezera was giving her, it didn’t seem like she needed to say what she wanted. Jezera knew."
"Two women pushed their way through the veil curtains. Alexia started. Neither could have been a day older than twenty two. One was blonde and busty, the other dark haired and spritely. They must have been from different regions, but both had skin darkened by the eastern sun."
"They were adorned with bands all over. Around their ankles, around their necks, around their forearms and wrists. Bells jutted out from the bands, so when they’d give little wiggles, Alexia could see it as much as hear it."
"They didn’t wear any coverings though. Everything was on display."
"Alexia’s mouth watered slightly. They were fantasies on legs. Like visitors from a dream. Did Jezera really think her the equal of creatures as precious as these?"

blwho "You are The Lady With The Horns?"

je "You’ve heard of me? Excellent."

"The beautiful women approached from either side, kneeling on to the bed, with Jezera between them. Alexia studied the way they moved. The sashay of their nubile bodies back and forth, back and forth. Swinging their bodies like pendulums. It was almost hypnotic."
"Alexia reached again for her goblet."

je "My pretty companion will not be taking part, she’s simply the audience."

brwho "A pity. She hungers with her eyes."

"Alexia leaned backward. Was she really staring so much?"
"Jezera pointed to the blonde."

je "Do you know your way with your hands, my dear?"

blwho "I was taught to play the harp, the fiddle, and the flute. But, it is the body I can play best. Would you like me to prove it to you."

je "Excessive, but I admire the bravado. Let’s put those words to the test, pretty one. Come close to me, so I can explore your form. And you mine."

"She turned to the other woman."

je "Don’t think I don’t have plans for you as well, darling. Bring a pitcher of wine. The body of a beautiful woman can stir up quite a thirst. I want you by my other side, quenching it for me."

"She nodded and rushed to obey."

je "One last thing."
je "Tell me your names. If you’re good I need to know who to ask for next time."

blwho "They call me Katya. My beloved is Era. We will do everything in our meager power to make ourselves...memorable for you."

je "Get on with it then, Katya."

"Jezera turned back to Alexia one last time and gave her a wink. Then it was time for the show to begin."

#cg1
scene cg444 with fade
show jezera naked happy behind cg444
pause 3

"Katya pressed herself to Jezera’s right side, intertwining her arms around her. Era joined them, kneeling on the bed with her warm body close to Jezera’s left and a jug of wine in her hands."
"The demoness was far from inactive though. Soon her arms were looped around both of the women, her body moving and shimmying. She moved with a seductress’ finesse. Trailing a nail down Era’s side and massaging the small of Katya’s back."
"Neither of the whores were unresponsive by any means. Jezera’s touch eeked out soft purrs and coos from them, like eager kittens. The sound of it rung in Alexia’s ears."
"But soon it got hard to keep track of individual movements in the swirl of hands and bodies. The girls ground and rubbed themselves against Jezera and Jezera squirmed and rubbed right back. The friction of moving skin was so close that Alexia could almost feel it."
"There was a hypnotic sway to the way Era and Katya moved their bodies. Back and forth, back and forth. It captured Alexia’s eyes. Alongside the alcohol, it was making her head fuzzy. It was like she was watching a spinning spiral."
"She watched spellbound as Katya’s lips came close to Jezera’s. Lingering just lingering. Alexia could almost imagine the feeling of the other woman’s breath. The electricity running between them acting like a magnetic pull..."
"..and the soft delicate kisses when their lips finally met. The kind of kisses that would take a normal woman’s breath away."
"At the same time, their hands set to work on each other’s forms. Jezera’s fingers had crept lower and were exploring the perfection of Katya’s rear. Tracing her curves. With Era, they moved to the front and explored other, more sensitive, places."
"And Katya’s hands? Well, two of her fingers had already sunk themselves effortlessly into Jezera’s wet folds. "
"Alexia downed more of her wine. Maybe if she drank more, she’d stop squirming so much. Or at the very least, go so fuzzy as to not be quite so embarrassed about it."

je "Mmm."
je "You’ve been trained well. You know, ah, the right spots."

blwho "Whatever it takes to please you, Mistress…"

"Jezera groaned softly and rolled her head back. Her eyes met with Era. A nonverbal command. The brunette swiftly replied by bringing her pitcher over the lustful proceedings and tipping it over. Golden wine rained over the squirming bodies like a waterfall."
"Some of it went into Jezera’s throat, and she drank from it eagerly. The woman liked her wine. But, much of it missed and rolled down her soft skin. It got in the space between her and Katya, lubricating them and staining them with liquid gold."
"It even ran all the way down, over Katya’s nimble fingers. It dripped down from Her Mistresses’ pussy on to the bed. The sight of it captured Alexia. She couldn't look away. Sparkling golden wine mixing with Jezera’s juices."
"Alexia couldn’t help but let out a little whimper. Her head rolled back and her body danced in the musty air. Through it all, a single desire overtook her clouded mind."
"She wanted to run her tongue along Jezera’s wine covered lower lips. She wanted a taste..."

scene bg6 with fade
show jezera happy at midright with dissolve
show alexia 2 necklace aroused at midleft with dissolve

"Back at the castle, two forms stumbled out of a portal. Alexia and Jezera were giggling and leaning against one another, walking with a back and forth sway. The sun had only just risen. Most of the castle was still asleep."
"Once more, as they appeared, so too did clothing covering their bodies."

je "Don’t...don’t worry. We can go back to...back to my room. If that gadfly husband of yours asks, just say that you woke up early to do some work. Or something."

al "Will people see us?"

je "Silly girl. The only other people wandering about the castle right about now are the maids. And they all know who their queen is."

al "O...oh…"

"She nodded sagely, following along with the other woman. She was still holding Jezera’s hand."

scene bg18 with fade
show jezera happy at midright with dissolve
show alexia 2 necklace concerned at midleft with dissolve

"A little while later, the two were sitting on Jezera’s bed in her vast and luxurious bedroom. It was a room that Alexia had spent more time in already then she ever would have imagined." 
"The effect of the alcohol was wearing off, and it only left Alexia more confused. She wanted to kiss Jezera. She wanted to touch her. Feel her skin against her own. It wasn’t the booze doing it. The more sober she got, the more her loins cried out."

je "Is something wrong? You seem out of it."

al "I’m just thinking about everything that happened tonight. "
al "It’s been...ugh my head"

je "And I thought I was the one drinking a little bit too much of the wine."

"Jezera put a hand on Alexia’s and even that small contact felt so good."

je "You certainly gave me the impression that you were having an enjoyable time. You must not have seen very many displays like that before."

show alexia 2 necklace aroused at midleft with dissolve

al "Well I was a country girl..."

je "If I’d sent you home the moment that I’d gotten ahold of your beloved husband, would you have ever seen anything like what I showed you today? Would the absence of Rowan have prompted you to travel more?"

"Alexia couldn’t meet Jezera’s eyes. "

al "Probably not…"

je "Then consider this my gift to you. I may have had to bring you back to one cage, but I helped unlatch another."

al "Yeah…"

je "Of all of the new places that I showed you, was there any that piqued your interest most?"

menu:
    "The Night Market." if visitMarket == False:
        $ released_fix_rollback() 
        show alexia 2 necklace neutral at midleft with dissolve
        al "Probably the Night Market. It had all those people and things. I didn’t know so much of the world could all convene in a single place like that."
        al "It felt like I was visiting everywhere at once."
        je "It seems you might just have been a city girl this entire time. How’d a flower like you wind up trapped in the countryside?"
        al "Hrmm..."
        show alexia 2 necklace aroused at midleft with dissolve
        
    "The Frozen Tundra." if visitTundra == False:
        $ released_fix_rollback()
        show alexia 2 necklace happy at midleft with dissolve
        al "I guess I’d actually say that little Hamlet we went to in the Tundra. It’s weird. They live so far from everyone else, that their culture is just unique. It’s amazing to think there are so many unique little enclaves everywhere."
        je "You want to travel then? Explore new places? Find these little pockets and what makes them special."
        "Alexia paused. Did she want that? She didn’t know what she wanted. She was so confused…"
        al "Maybe. I guess I just know that I really liked going there."
        al "Maybe...hmmm…."
        show alexia 2 necklace aroused at midleft with dissolve
        
    "The Cliffs of Mithras." if visitCliffs == False:
        $ released_fix_rollback()
        show alexia 2 necklace neutral at midleft with dissolve
        al "Perhaps that old city."
        je "Mithras."
        al "Yeah. Mithras. I guess it’s just silly to think about. My village could only have been a few hundred years old at most. In the grand scheme of things, everything in my life seems smaller. Almost less important."
        je "Is that a bad thing?"
        "Alexia tilted her head. She hadn’t considered that."
        al "I don’t know. I guess it just makes all the things I’m anxious about seem almost smaller by comparison."
        al "I..."
        show alexia 2 necklace aroused at midleft with dissolve
        
    "The Hidden Library, Tharafin." if visitLibrary == False:
        $ released_fix_rollback()
        show alexia 2 necklace happy at midleft with dissolve
        al "I always liked to read. You know that. But, for me, it’s always been scattered books here and there. When I learned even about the library here I was stunned."
        al "So it has to be the elven library. Tharafin. I’ll never get the sight of so many books out of my mind. It’s really incredible. I never realized the world was so vast before."
        je "There’s so much you haven’t explored, little dove. Isn’t it proof of that?"
        al "..."
        al "I..."
        al "Hmm..."
        show alexia 2 necklace aroused at midleft with dissolve
        
    "The Empress of the Waters":
        $ released_fix_rollback()
        show alexia 2 necklace aroused at midleft with dissolve
        al "...uh…"
        je "Yes, little dove?"
        "Alexia already knew the answer, but admitting it out loud would be impossible. Still, Jezera was looking right at her, and try as she might she couldn’t fumble together another answer."
        "She had to tell her."
        al "I think I liked…"
        "Her voice went very quiet."
        al "...I liked the Empress of the Waters the most…"
        "Jezera’s grin went wide, like a cat who’d cornered a bird. But, she otherwise left Alexia to stew in her own admission."
        "Had she really just said that out loud?"
        

"Alexia went quiet for a long time. It was just them on the bed. Jezera and Alexia. The only distraction from her thoughts was the odd glance at the other woman’s body. She really was so beautiful…"

#in her eyes cg1
scene black with fade

"..Beautiful…"

scene bg18 with fade
show jezera happy at midright with dissolve
show alexia 2 necklace aroused at midleft with dissolve
        
je "Are you alright, dear?"
je "You looked distracted for a second?"
        
"Alexia looked down. She couldn’t meet Jezera’s eyes. There was too much. She just wanted her head to stop swirling."

show alexia 2 necklace concerned at midleft with dissolve

al "I…"
al "Well..."
al "You see..."
al "..."

"She felt a delicate hand on her shoulder. Jezera was trying to comfort her."

je "Breathe in. Breathe out. It makes the entire speaking thing a bit easier, I find."

"Alexia nodded. She inhaled sharply. Then exhaled. Simple breathing. It was the only thing that could steady her."

al "I...I’ve been very confused lately…"
al "By a lot of things…"
al "There was this dream, it had a tree in it…"

"Jezera raised an eyebrow."

je "A dream with a tree?"

al "It’s not important. It’s just…"
al "There’s so much I don’t understand about the world. There’s so much I don’t understand about myself. I used to think I did. But, then I was taken here, and everything is different."
al "So maybe...so maybe...maybe you’re right. Maybe I was a prisoner. Maybe there is more to life that I don’t understand."

show alexia 2 necklace aroused at midleft with dissolve

al "Maybe I have desires I don’t understand…"

"Jezera leaned closer. The distance between them was so small now. Close enough that Alexia could feel the other woman’s breath. It reminded her that the clothes she wore weren’t real."

je "What kind of desires?"
je "It’s alright, little one. You can tell me?"

al "I…"

"Her face burned. Her sex burned. What was wrong with her. What was she saying? She wasn’t being coerced into this. She was admitting this out in the open to a monster."

al "I…"

"She shouldn’t say it. She shouldn’t say it. She shouldn’t say it."

al "I…"

"But, if she said it, would Jezera….would Jezera touch her?"

al "I’ve been thinking about….thinking about…."
al "Girls."

#jez smirk

"Jezera smirked."

al "I’ve been thinking about girls. But, not just girls. Men too. Other men."

if garInfo == "4":
    al "Like what you had me do as a maid…"
    
elif visitMarket == False:
    al "Like the way you fucked that man at the Night Market. Not a moment’s hesitation. "

else:
    pass
    
al "I know it’s wrong. I’m a married woman. The wife of the fucking hero. But...I don’t know. I just have all these needs, and it’s been driving me crazy."
al "That’s why I went out there to the lake in the morning. I wanted to dance. I wanted to dance naked. Hell, what I really wanted was to do it in the castle courtyard, but that would be wrong. So I went to the lake…"

"Why was she saying all of this to Jezera? Was it the alcohol?"
"No...or at least not entirely…"

al "I feel like...I feel like...I feel like I’m going crazy. Like I can’t go home again."

"Alexia laid back on the bed spreading her arms and legs out. The pillow was so soft that her head sank into it. It was light and comfortable. It felt good."

al "I don’t know what I want anymore…"

"She felt a shadow overhead. Jezera had moved forward and was kneeling over her, looking."

scene jezsmirk with fade
#jez smirk
show jezera happy behind jezsmirk
show alexia 2 necklace aroused behind jezsmirk

je "Maybe. Maybe not. But, deep in that little head of yours, I think you do know what you want. What you desire. What you ache for here and now. It’s just hard to get out, because of all of the shackles in the way."

"She brushed a hand down the side of Alexia’s cheek."

je "You know what you want."
je "You want to tell me what you desire in this moment…"

$ uhmCount = 0

label jezCorFuckMenu:

menu:
    "Her.":
        $ released_fix_rollback()
        jump jezCorSexScene
        
    "Uhm...":
        $ released_fix_rollback()
        if uhmCount == 0:
            al "Uhm...I really…"
            al "I really don’t know."
            je "Yes you do….yes you do….Just dig deeper…dig deeper."
            $ uhmCount = 1
            jump jezCorFuckMenu
            
        elif uhmCount == 1:
            al " But...but...I don’t understand what I want."
            je "Oh, little one. You don’t have to understand it to want it. Don’t think so much. Just feel it. Let it flow through you."
            $ uhmCount = 2
            jump jezCorFuckMenu
            
        elif uhmCount == 2:
            al "I don’t know…"
            je "Yes you do. You’re thinking too much. Just relax. Let it slip out."
            $ uhmCount = 3
            jump jezCorFuckMenu
            
        elif uhmCount == 3:
            al "It’s embarrassing…"
            je "It’s just us girls here. Hehe. I promise I won’t tell a soul. You can trust me."
            $ uhmCount = 4
            jump jezCorFuckMenu
            
        elif uhmCount == 4:
            al "It’s wrong. I shouldn’t feel this way. I shouldn't want it."
            je "That’s your jailors talking. Your parents. Your village elders. Rowan. Everyone who told you how to live your life."
            $ uhmCount = 5
            jump jezCorFuckMenu
            
        elif uhmCount == 5:
            al "..."
            je "Breathe. Just breathe."
            $ uhmCount = 6
            jump jezCorFuckMenu
            
        elif uhmCount == 6:
            al "..."
            al "I..."
            je "These feelings you have are real. They’re the truth. They won’t go away. You can’t escape them. You can’t fight them. They’re going to come out eventually."
            $ uhmCount = 7
            jump jezCorFuckMenu
            
        elif uhmCount == 7:
            al "No...Please…Don’t make me say it..."
            je "This is who you are. You can fight it. You can embrace it. But, embracing it allows for so much fun."
            $ uhmCount = 8
            jump jezCorFuckMenu
            
        else:
            al "..."
            je "You can’t fight it any longer, can you?"
            jump jezCorFuckMenu

label jezCorSexScene:

al "I want... I want…"

"She couldn’t fight it anymore. Maybe...maybe it would be better just to admit it…"

al "I want you...I want to kiss you. I want to touch you. Please…"

"Jezera leaned down, brushed her lips against Alexia’s ear."

je "You want me to fuck you."

al "Y..yes…"

je "Well, why didn’t you say so earlier?"

"Jezera snapped. As she did, both her dress and Alexia’s faded away into mist. Jezera was on top of her. Body pressed against body. So tantalizingly close. So good..."

je "Alexia, my girl. I’m going to make you feel things that you’ve never felt before."
je "Close your eyes. Trust me."

"Alexia closed her eyes."

scene black with fade
show jezera naked happy behind black

"It was clear immediately that something was happening. Though what it was, she couldn’t exactly say. It was like the sheets underneath didn’t feel as present anymore. That is until she couldn’t feel them at all."
"But, what was around her? It almost seemed like...nothing."

je "Good girl. Good girl. Just keep your eyes closed. Everything is alright."

"Alexia kept her eyes closed, but that didn’t stop her mind from hazily wondering what was happening to her. It felt so strange."

je "Almost ready. Just a moment more…"

"She felt something soft brush along her breast and it made her shiver. It felt like skin. It felt like her."

je "There."
je "You’ve been such a good girl already. It’s time to open your eyes for me, little one."

"Alexia’s eyes fluttered open."

#In Her Hands CG 2 Variant 1
scene cg390 with fade
show jezera naked happy behind cg390
show alexia necklace naked aroused behind cg390
pause 3

"Alexia was floating in the middle of the air."
"A green glow surrounded her, and her body was twisting and turning several meters above the bed. No matter what she did, she couldn’t control her momentum. It felt so strange and surreal. Like being in a dream."

al "Wha…"

"But, she wasn’t alone. Jezera was floating right above her, facing downward. Their bodies were so close to one another, occasionally brushing together. Every point of contact sent another jolt through Alexia’s system."
"Without even the floor to ground her, the only thing she felt in that moment was Jezera. The other woman’s body was her entire world."
"That effect only grew as Jezera’s hand joined in the action. Her violet fingers explored Alexia’s skin. Her breasts. The nape of her neck. Her mound. Everywhere Jezera touched would consume Alexia’s attention."

al "Ah…"

"She was lost in it. Drifting away."

je "You need to do your part too, little one."
je "You need to touch me. You need to please me."

"Alexia’s eyes fluttered more. Jezera was so beautiful. Every inch of her was perfect. Was touching her really okay?"

al "I don’t know how to please...a woman…"

je "Yes, you do."

"Her hand brushed over Alexia’s lower lips. It made her head roll back and drew a load breathy moan from her lips. She was so wet now. Jezera would be able to feel how wet she was. How much of a slut she was…"

je "You know how to pleasure a woman. You’ve been doing it your whole life."
je "Men are different beasts. You need to guess with them. But, you’ve always known what a woman likes."
je "Touch me."

"Jezera’s other hand strayed up to Alexia’s nipple, toying with it softly between her fingers. It stiffened at her touch. But, once it was nice and firm, Jezera suddenly gave it a hard pinch."

al "Ah!"

"Her back arched. A long groan sunk out of her. But, despite the pain, it felt good. It was like she was already addicted to her. Alexia’s mind was floating away."

je "Touch me."

#In Her Hands CG 2 Variant 2
show cg391 with dissolve
pause 3

"Alexia obeyed. Her hand timidly sought out Jezera’s sex. It was slippery and wet. She almost imagined it was still soaked with wine. Her folds were so smooth. Absolutely perfect. Yet...familiar."

je "Yessss..."

"Alexia knew how to find a clit. She knew how to touch it. She knew how it good it felt. Her fingers found Jezera’s clit and just did what came naturally to her. The other woman certainly seemed to like it. She gave Alexia’s aching nipple a pinch of appreciation."

al "Ah…"

je "See...you do know how to do it..."

"Now they were fully locked together, hands exploring each other’s bodies. Alexia marveled at every inch of her. The curve of her breasts, the flatness of her stomach. The occasional shudder of her spine. She was almost more beautiful to touch than to look at. "
"Jezera similarly showed no reservations. Every inch of Alexia was hers to explore. Alexia’s body was entirely naked to her. Every secret place open to discover. Jezera knew all the right ways to touch her to elicit a reaction. She was being played like an instrument. "

je "Good girl...Good girl…"

"They floated along, far above the ground. Alexia wasn’t afraid. Her head was floating along with her body. Twisting and dancing in the air. Her world was Jezera’s body. Jezera’s pleasure."
"She wanted to make Jezera cum. She wanted to hear the sound Jezera would make when she went over the edge. Every soothing word from Jezera’s tongue made her want to please her more. She wanted to be a good girl."

je "See? You’ve always known how...Being with a woman is so easy….Natural. You know all the right...ah...buttons to press."
je "It’s so good…"
je "You want more…"

show cg392 with dissolve
pause 3

"Alexia’s fingers went faster. She did want more. Jezera’s pussy was so soft and wet. She just wanted to stroke it and touch it. Be near it. It captured her."
"She could feel the heat grow and grow from it. Jezera’s breathy moans growing louder and louder. Alexia was doing it. She was pleasing her. The other woman gave her rear and breasts soft appreciative pinches. It made Alexia groan and squirm with her own building lust."

je "Good girl. Girl girl. Just a little bit more...Just a little bit more...."

"Alexia felt Jezera’s hand force a grip into her hanging hair, digging into it. She was using Alexia’s entire body as a handle."

show cg393 with flash
pause 3

je "Ah…"
je "Ah."
je "Ah!!!"

"Jezera’s body shook with powerful force. Every motion and vibration went into Alexia. It was the only place for the force of it too. Jezera’s nails dug harder and harder into her hair. It hurt, but she didn’t care. She did it! She was a good girl!"
"The demoness kept on twisting and spasming, grinding her body against Alexia. It was almost too much for the human girl to bare. This was a dream. This was a dream. Writhing and grinding together in the air without a care for time or the world."

je "...See? Wasn’t that easy?"

"Alexia could barely process the words. Her pussy was throbbing. Her body was alight."

al "Uh...uh huh…"

"Jezera brought her lips inches from Alexia’s. Her breath was heavy as she recollected herself."

je "I see. You want attention now, don’t you girl?"

al "...Please…"

"Jezera planted a peck on Alexia’s lips and then drew backward slightly. For the first time, Alexia was left without her touch. She wiggled and groaned with desperation. "

je "You’re unskilled with a woman. But, you know your own body...and you have a lot of spirit. A lot of need. You’ll have many chances to learn."
je "I’m going to teach you so many things."
je "But, first..."

"Jezera spread her hands and a faint glow emerged from them. Alexia’s clouded mind didn’t need to wonder what magic she was performing for long. Alexia’s arms felt like they were wrapped in something hot."
"The pulsing waves of energy were moving them. It wasn’t forceful or brutal. But, all the same, they positioned her arms crossed behind her back. Bound and exposed. Floating helplessly in the air…"
"...Moaning and squirming like a desperate slut."

je "It’s time for a little reciprocation, my dear. Spread those legs of yours."

#In Her Hands CG 3 Variant 1
scene cg408 with fade
show jezera naked happy behind cg408
show alexia necklace naked aroused behind cg408
pause 3

"Alexia could barely form a coherent response. But, she did spread her legs as ordered. Like a good girl. Jezera floated gently back, positioning her head inches from Alexia’s crotch. Her pussy ached with anticipation."

je "Squirming for me. Gasping for me. So helpless. I can do whatever I want with you now. You’re like a puppet on my strings."
je "And you love it."

al "...Yes...Please…"

"She bucked her hips and whined. She needed it so bad. Why wouldn’t Jezera just taste her already? "

je "Delicious. You want me to give it a taste."

al "..Please...Please please please…"

je "Uh uh uh. You need to say “Please, Mistress.”"

"The words and their connotations barely even processed to Alexia. She was simply in a state of total need."

al "Please...Please, Mistress...Please taste me…"

je "Good girl. Now for your reward."

show cg409 with dissolve
pause 3

"Alexia gasped. She felt her lower lips part and a soft tongue work its way into her folds. Her entire back arched. Her arms struggled in their restraints. It took mere seconds and she was already so sensitive. A tongue always did that to her."
"But, this was no ordinate tongue. Jezera seemed to have complete mastery over the female anatomy. Being eaten by Rowan had never felt anything like this. The flick flick flick of her tongue against Alexia’s clit and the light sucking were totally new."
"She melted into the air. Now she truly was floating like a cloud."

al "Ahhh…ah..."

show cg410 with dissolve
pause 3

"Her hips started tingling and spasming uncontrollably. Without a surface to rest on, the vibration kept running all the way up and down her spine. Her entire body was shuddering. Every inch of her was being toyed with. "
"Jezera set the pace. She shifted rhythm sporadically as if to signal that she could. Alexia was nothing but reactions by then. Jezera sped up, and her body sped up. Jezera slowed down and her body slowed down. Time vanished, and for that moment she and Jezera were one."
"In this state, her arousal found new and higher peaks. Waves and waves crashing down on her, washing away everything. She was going to go over. She was going to…"

#In Her Hands CG 3 Variant 2
scene cg411 with fade
show jezera naked happy behind cg411
show alexia necklace naked aroused behind cg411
pause 3

al "I...fuck..I...So good...it feels so good….Rowan...fuck..."

"Alexia melted into the air. Every last remaining ounce of strength let her body through her pussy. She hung limp and exhausted. A puppet on a string. Raw mindless pleasure shooting down every nerve ending."
"But, Jezera was not done."

al "Wha…"

"Her tongue kept on attacking Alexia and attacking her. Alexia’s voice called out in desperate moan after desperate moan. Her brain couldn’t even fully process what was happening."
"But, her body could. It spasmed and danced to Jezera’s will all the more so. Before long, the pressure was welling up again. Rising higher and higher like an inescapable wall of tension."

al " I’m going to...I’m goi-"
al "Ah."

"It kept going, and going, and going. Orgasm after orgasm. Alexia had long since stopped participating, but her body just couldn’t stop. Each one dulled her further and further. Eventually, she wasn’t even there anymore."
"Totally lost in the feeling..."

scene white with fade

"…"
"..."
"What was this? What was she feeling?"
"It was like floating away. On a river. Everything disappeared but she was still here. Maybe she should have been worried, but how could she?"
"It was incredible…"
"Alexia never wanted to stop feeling like this. She could get lost in this forever…"
"..."

scene bg18 with fade

"Alexia breathed in and breathed out. She breathed in and breathed out. Thinking was too much. Moving was too much. She just needed to breathe. She was back to where she had been, laying on Jezera’s bed. When had the levitation spell ended?"

#Close up of Jezera (Amused/naked)
scene jeznakedsmirk with fade
show jezera naked happy behind jeznakedsmirk
show alexia necklace naked aroused behind jeznakedsmirk

"Jezera was kneeling right next to her, with a supremely satisfied expression. She was lapping at her hand like a cat. There were juices on it."

je "If you don’t get up soon, I’m going to get worried that I broke you."

al "Mmmmm."

je "Well, that’s a relief."

al "How long…"

je "Last I checked it had been two hours. But that was some time ago. It’s almost mid-day already. I had Rowan sent to do troop inspections all day, so he won’t notice your absence. I’m sure he’ll enjoy that."

"Alexia groaned slightly and ran her hands over her body. That had been...that had been something else."

je "I also sent a maid to the lake to pick up your clothes. She’ll be back shortly, I believe."

al "Mmm..thank you."

scene bg18 with fade
show jezera naked happy at midright with dissolve
show alexia necklace naked at midleft with dissolve

"Jezera gave Alexia a little bit of space to stretch. Already, Alexia’s mind was coming back to her. And with it came racing thoughts."
"That had been….that had been different. It felt like a page had been turned. The only way to go was forward."

al "So what happens now?"

"Jezera raised an eyebrow."

je "What happens now?"
je "What happens now is that you get dressed and return to your room. I have the maids bring you breakfast. You spend the day relaxing after having been through so much last night."
je "You’re still a prisoner here, of course. But, one who feels a little less trapped, I like to believe. But, we’ll see about further excursions out of the castle grounds."

"Alexia nodded slowly. She really would like to continue leaving the castle. It was like moving when you hadn’t stretched for a while."

al "And...us?"

je "Well my dear, where would you like things to stand between us?"

show alexia necklace naked concerned at midleft with dissolve

"Alexia averted her eyes."

al "I love Rowan. I won’t leave him."

je "I know you do, my love. Your little romance is so achingly sweet. It gives me cavities."
je "I am not a jealous lover. If you want to share my bed with some more regularity, I don’t mind you coming home to your husband afterwards. You certainly would not be the first woman I’ve had such a relationship with. "

"Alexia listened to it all but still felt so much unease. It sounded so appealing. More of the same adventures. But, it also felt like betrayal."

al "But, Rowan…"

#jez smirk
show alexia necklace naked aroused at midleft with dissolve

"Jezera leaned forwards. Her breasts draped over Alexia, and lips brushed against her ears. It was all so hypnotic."

je "You have certain needs that Rowan just can’t fulfill. A taste for pussy for example…"

#jez happy

je "That means, without a little help, sticking with Rowan will just leave you feeling...unsatisfied. You can imagine it, can’t you? That same boring vanilla sex with the same man day after day."
je "You’d grow to resent him. Now that you’ve seen outside the bars, living in the prison can’t be comfortable."
je "You don’t want to think of him that way. And I don’t want you thinking of him that way either. Think about it. I benefit from you two having a strong relationship. It makes you a more valuable hostage for me."
je "So here’s what you should do. "

#jez smirk

je "Spend your time with him. Be the good wife. The obedient wife. When he comes back from his missions, ask him how his day went. Fuck his brains out. Whatever you two do."
je "But, when the boy is away, well you don’t have a lot to do anyway. The girls might as well play. Release all of that…"

"Jezera let out a small groan."

je "...Tension."
je "Discover some new and exciting things. And then, when your dear husband returns, he’ll find his loyal wife waiting for him, not feeling trapped by him anymore. Perhaps with some...exciting...new skills that she can use for his pleasure as well."
je "Everyone benefits."
je "Rowan gets the benefit of a wife who won’t feel conflicted about her desire to please him, and her desire to be a…"

"Her voice went an octave deeper."

je "Little slut."
je "You get to explore all of these strange new feelings and sensations with a...practiced...lover."
je "And I get a beautiful woman to engage in some wholesome depravity with."
je "Appealing? No."

"That also sounded so good. Too good to be true...right? A way to get this feeling again without hurting Rowan?"

show alexia necklace naked concerned at midleft with dissolve

al "But, what if Rowan finds out?"

#jez happy

"Jezera giggled."

je "Alexia darling. I own this castle. I own him."
je "I know every secret passage. The entirety of the household staff lives to serve me. If I don’t want him to know about it. He won’t know about it."
je "You can save your marriage with my help, and he will be none the wiser."

al "..."

"What would make someone trust someone they knew they should not trust? Why would a person listen to arguments that they knew were being made in bad faith?"
"Perhaps, they wanted them to be true." 

al "I suppose, so long as it’s in secret, that I wouldn’t mind doing something like this again."

show alexia necklace naked at midleft with dissolve

al "But you have to promise me. Rowan comes first."

show alexia necklace naked aroused at midleft with dissolve

"Jezera leaned up. Alexia almost groaned from the feeling of Jezera’s breasts withdrawing from her skin. She was still so addicted to her touch."

je "If I must. If I must."
je "I promise you. Your relationship with your husband will always be paramount."

"Alexia settled down. So long as that was there, it would be okay…"

al "Alright then. I think...I think I can live with that."

"Jezera brushed Alexia’s cheek softly, as though she were stroking a cat. It felt oddly soothing."

#jez smirk

je "Excellent. Then I will explain to you the mechanics of our new...understanding."
je "In your normal affairs you may remain in your normal state. Serve Rowan as his wife. Do whatever job he wants. I may be...handsy...from time to time. But, assume I have no special claim to you, unless you’re serving as part of my household staff at that particular moment."
je "But, every so often I will send down a maid with a box. And in this box, I will put this."

"Jezera opened her palm."
"Then, there was a flash of purple light. Alexia covered her eyes weakly. When it subsided, she was holding something. She pressed it into Alexia’s hands."
"It was a collar. A fancy black lace choker made with intricate stitches. And in the front a metal ring hanging in an O shape."

je "When you receive this, it means that for the evening, you are my slave. My plaything. It means that I expect you to meet me inside my room with you wearing it."
je "And then the rest of the evening?"

"Alexia felt fingers brush along her sex, drawing an involuntary shudder from her. The lace collar slipper from her fingers on to the bed."

je "Discovery."
je "Intimacy."
je "Ecstasy."

al "...Ecstasy."

"Her eyelashes fluttered."

je "Do we have an understanding, my love?"

"Alexia nodded slowly. She felt like she handed over part of her soul. But, that only made it all the more thrilling."

#jez happy

je "Thank you, Alexia. For trusting me tonight. And for trusting me in the future. You really are more incredible than you know."

"Alexia gave her a weak smile, and reached for the choker again. It was so soft and smooth. Maybe she would look good in it…"
"Perhaps she really had wanted this all along…"

scene black with fade

"After a bit of relaxation and sobering up, Jezera had Alexia’s dress brought to the room. The two awkwardly hugged before Alexia departed. But, that was alright to Jezera since the human woman no doubt was quite confused and exhausted after such a long morning."
"Alexia would fall asleep the moment she reached her own bed, of course. It had been a long day."

scene bg18 with fade
show jezera naked happy at midright with dissolve

"This left Jezera, hovering alone in the room. The scent of her visitor and their activities together still hung in the air. A reminder of her most recent conquest."
"The moment Alexia walked through the door, Jezera’s smile faded. She walked slowly over to a game board on a side table that had been set up long before. The pieces were already arranged in a complex formation. It was well into the match."
"There was no opponent, no rival in sight. But, Jezera still studied the board as though she were facing against a skilled foe. After quite some time staring impassionately, Jezera reached out and moved one piece."

je "Satisfactory."

#bonus to maid job TODO
$ change_actor_num_flag('alexia', 'jezera_influence', 3)
$ change_corruption_actor('alexia', +5)
$ alexiaJezObedient = True
$ alexiaUnfaithful = True
$ alexiaJezeraSex =+ 1
return

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################

label alexiaJezVisits:

if alexiaSeparateRoom == False:
    scene bg9 with fade
    
else:
    scene bg7 with fade
    
show alexia 2 necklace neutral at midleft with dissolve

"Alexia was roused from her book by a knock at the door. It was the middle of the night, long after she expected any guests."

if alexiaSeparateRoom == False:
    "Perhaps Rowan was coming back? He’d been out all day on various assignments."

"Alexia padded to the door and opened it. On the other side was a dark skinned maid, with her head lowered and a pair of boxes, one larger and one smaller, in her hands."

maid "I was instructed to give you these by Mistress."

al "Hmm."

"Alexia relieved the packages from the maid’s hand and closed the door behind her. If Mistress Jezera wanted her to have these then that must mean..."
"She opened the small box. It held Jezera’s black choker. The one that meant she was Jezera’s slave for the evening…"

if jezCorVisits > 0:
    show alexia slave happy at midleft with dissolve
    
else:
    #in her hands CG
    scene black with fade
    "At once, Alexia was reminded of the last time she had seen it. Ever since that morning, the thoughts of it had left her so easily excited..."
    "...just like now."
    if alexiaSeparateRoom == False:
        scene bg9 with fade
    else:
        scene bg7 with fade
    show alexia 2 necklace aroused at midleft with dissolve
    "Alexia carefully opened the second box. The collar she recognized, but what else did Mistress Jezera have planned for her?"
    "Inside was a lacey black nightie and set of panties. Dark, sexy, and stylish like nothing she’d ever worn before. The fire grew. Without even thinking, her clothes were already piling up at her feet."
    show alexia slave happy at midleft with dissolve
    "When fully dressed, she did a little twirl in front of the mirror. The outfit clung to her curves and demonstrated that her looks had not faded with time." 
    "She struck a few more poses, sexy and luscious, and watched the way the ring on her collar bounced ever so slightly as she moved. She spoke in a raspy whisper."
    al "I’m such a slut..."
    $ jezCorFaceSittingSeen = False

jump jezCorVisitFaceSitting

label jezCorVisitManager:
    
menu:
    "Dancing." if jezCorDancingSeen == False:
        $ released_fix_rollback()
        jump jezCorVisitDancing

    "Infiltration." if jezInfiltrationSeen == False:
        $ released_fix_rollback()
        jump jezCorVisitInfiltration


#######################################################################################

label jezCorVisitFaceSitting:

if jezCorFaceSittingSeen == True:
    jump jezCorVisitManager
else:
    pass

$ jezCorVisitScene = "facesitting"
$ jezCorFaceSittingSeen = True
$ jezCorVisits += 1

scene bg18 with fade
show alexia slave concerned at midleft with dissolve

"This was not the first time that Alexia had been alone in Jezera’s room. But, the place always had an intimidating air to it. It was filled with objects with powers she probably could not even imagine. But, today was especially intimidating…"
"After all, today there was a noticeable addition to Jezera’s bed. Two sets of stern leather cuffs with animal fur on the inside and metal rings attached. Chains hung off the sides as if to make their intended use even more obvious."
"Alexia decided against going to look at them. Better to wait patiently for Jezera in the middle of the room. She debated whether or not to kneel in wait, but had no idea how Jezera would even react to that. This wait was torture in of itself..."

show jezera happy at midright with dissolve

je "There you are."

"The demoness strode casually into the room. For a moment, Alexia had expected an apology for being kept waiting. But, that was probably not how their new dynamic worked."
"...she was the one who wanted this."

if jezCorVisits == 1:
    je "I was hoping you’d look good in that. I picked out a style that I knew you were inclined towards. Only, I added a few touches to help make sure it gave the proper impression."
    
else:
    je "I do so enjoy seeing you dressed like that. I should have started improving your wardrobe a long time ago."
    
al "Thank you…"

"She couldn’t help but avert her gaze and clutch her arm. Her face turned towards the bed."

al "Are-are those for me, Mistress Jezera?"

#jez smirk

je "Impatient are we? That’s a question that will just have to wait, darling. There is a much more pressing one."

"Jezera closed the distance between them until she was standing intimidatingly close to Alexia. The effect was immediate. Her beauty, her scent, even the odd brush of her clothes overtook her. Alexia shrank."

je "Have you missed me since our last little...encounter?"

show alexia slave aroused at midleft with dissolve

al "I have, Mistress…"

je "Don’t you think that you should give me a little kiss then? A token of your affections?"

"Alexia closed her eyes and leaned forward with puckered lips. She did not have to wait long before she felt another pair match hers, and take her breath away. It was impossible to know how long they were standing there, tongue against tongue."

if jezCorVisits == 1:
    "This…"
    "Alexia could get used to this."

elif jezCorVisits > 2:
    "Alexia’s heart fluttered. She knew it was wrong, but a woman could get addicted to kisses like these."
    
else:
    pass
    
"If there was any proof of the difference between taking a woman as a lover and a man, it was what followed. Jezera and Alexia made their way to the bed and curled up next to one another. Alexia’s body rolled and twisted to Jezera’s soft molestations."
"It was talking. Just talking. Jezera asked her about how her days were going. Her job. The people she worked with."

if jezCorVisits == 1:
    "Since when did Jezera have such a soft side? Had she always been hiding this?"
    
if all_actors['alexia'].job_state.job == 'maid':
    al "I suppose I don’t have to tell you that much about my work. After all, you probably hear about everything I do..."
    je "Oh, you act as though every member of the maid staff is my secret informant."
    "Alexia didn’t know if Jezera was denying it or bragging about it."
    if maryKissLiked == True:
        "Alexia considered talking about her interactions with Mary, but decided she didn’t want to give Jezera more ammunition."
        
elif all_actors['alexia'].job_state.job == 'breeding':
    al "The breeding pits are always lively. Though, I can never tell if Draith likes me very much. I guess that’s just how he is with women…"
    "Jezera, for her part, seemed very interested about the kinds of creatures being bred there. Alexia answered to the best of her ability, but, in truth, she understood so little of what Draith was up to."
    
elif all_actors['alexia'].job_state.job == 'research_assistant':
    al "It is always fascinating to work among so many books, just this week I found an old tome about…"
    "Jezera, for her part, seemed very interested in Cliohna and her activities. In truth, Alexia didn’t know much about the cold librarian’s work, but at one point she said something that made Jezera stop to process it. So clearly she’d said something right."

elif all_actors['alexia'].job_state.job == 'barmaid':
    al "I like the people who come in to visit. I’ve never been exposed to so many different ways to live and so many points of view."
    "Jezera seemed to pick up on Alexia’s curiosity about Qerazel and happily regaled her about interesting details about life out east."

else:
    al "I’m not much of a smith. Greyhide normally has me doing mostly administrative work."
    if alexiaLiurialFriendly == True:
        al "I guess that makes me his version of Liural, almost…"
    "Jezera, for her part, smirked as she asked about Greyhide. The woman was bemused by the old bull, despite her protestations that her interest was entirely for the sake of operations success."

"Eventually, the topic turned to Rowan. But, what even was there to say about him? That he was out seemingly fucking the entire continent? That every morning she saw him, she felt like there was a slightly different man behind that face?"

al "I really don’t know about Rowan. I don’t. He risked everything to come to Bloodmeen and save me. But, months and months later and here we still are."

je "Am I so bad a host?"

al "It’s not that...It’s just…"

"Alexia kept her rhetoric about Rowan light. Frustrated but not detached. It was all reminding her how strange and {i}wrong{/i} it felt to be in this room, touching this woman. But, every time she went too far down that path, Jezera seemed to draw her back with a knowing remark."
"For better or for worse, it felt Jezera tried  to understand her feelings. Alexia had to admit that wasn’t an unpleasant feeling. It turned her mind back to matters at hand..."

al "...You called me here for a reason beyond just conversation though, right Mistress?"

je "What’s this? Eager to find out? I thought you were enjoying talking. Clearly, I am not the conversationalist I thought I was."

"Alexia blushed and looked away. Jezera was teasing her."

show jezera naked happy at midright with flash

"Jezera rose from Alexia’s side. She took a position kneeling over Alexia on the bed. In just a snap, the red dress vanished from her body."
"Alexia’s eyes drank in her nudity. Alexia was left having to choose between drawing back and gawking. She alternated between the two inconsistently. Had she really once believed that she had no special interest in other women?"

je "Today, my little dove, I’m going to teach you about the joys of an activity that has been called facesitting."

al "Facesitting?"

je "Indeed."
je "Don’t confuse it for using someone’s face for a chair. Though that could be fun. In actuality, it is a form of oral sex. Just not a form of oral sex that you’ve much experimented in with me."
je "In your prior experiences, cunnilingus has been like this."

"To demonstrate, she shifted posture until her face was low. Now mere inches from Alexia’s crotch. Alexia’s breath quickened. The feeling of breath between her legs did nothing to cool her excitement."

je "One girl on her back, or perhaps in the air, and the other showing her...appreciation. But, that’s a more mutual kind of cunnilingus. Equals."

"Jezera raised back up. Alexia groaned at the withdrawal of heat. Now Jezera was over her stomach, pinning her down by her weight. It kept Alexia where Jezera wanted her."

je "Face sitting. I will lower my beautiful pussy onto that little mouth of yours. So your entire world will be my sweet sex. No escape. In a position like that, you’ll have no choice but to work your tongue for dear life. Lick or be smothered."
je "This is not sex between equals, my sweet girl. It is the way that a slut worships her queen."

al "...Worships her Queen…?"

"Alexia looked to the straps, then back towards her mistress. The idea didn’t seem real to her. She was going to sit on Alexia’s face?"
"She was suddenly jolted back to reality. An electric touch to the front of her panties. How could she even try to focus on anything else?"

je "You want to try it, don’t you? Your body is telling me all the truth I need to hear. Don’t be afraid to listen to it too."

"Alexia nodded without thinking."
"Alexia offered no resistance as Jezera took hold of her wrists. Only a groan from the withdrawal of the hand from between her legs. Her eyelashes fluttered. Before she’d even realized what happened, the cuffs secured her tight. Her arms spread open and restrained."
"Her breath grew ragged. Jezera had shifted positions to get the ankle cuffs in place as well. They wrenched her legs apart and kept her body open to exploration. She couldn’t close her legs. Jezera could do anything she wanted to her."
"Her heart was a drum."

#a most excellent seat cg1 var 1
scene black with fade
show jezera naked happy behind black
show alexia slave aroused behind black

"Now, Jezera took her position kneeling right above Alexia’s face. Alexia almost gasped. Jezera’s pussy was mere inches from her face. She could feel its heat. She could smell its musk. She could almost taste it, even."
"Without thinking her head leaned upwards as much as her bondage would allow. But Jezera’s raised position made that impossible."

je "Here we are."

"All Alexia could do was stare at it. It was like she was falling into a trance."

je "Mmmm. You like it, don’t you? You think it’s pretty?"

al "Y-yes."

je "You want to smell it, don’t you?"

al "Y..yes."

je "You want to taste it."

al "Mhmh!"

"Why didn’t Jezera just start already? Alexia was squirming in her bonds, going mad. She couldn’t even see anything else. Mindless desperation was setting in."

je "Well if you want me to smother your face with my beautiful pussy, you’re just going to have to beg me for it. Your answers have been entirely insufficient."

"A sharp pain shot out through Alexia’s body. Her hardened nipples were being pinched through her outfit by sharp fingernails. She groaned out. It hurt...but not in a bad way..."

je "You must have heard me, pretty toy. I said beg."

al "I...fuck...uh…"
al "P-please Mistress let me lick your pussy…"
al "...Please…"

"Another shot of pain and adrenaline. Another pinch to her nipples. Alexia’s gasp was muffled by the other woman’s crotch."

je "I told you, didn’t I? This isn’t just eating a woman out. You’re going to worship the pussy of a queen. Beg properly. Beg to serve."

"She couldn’t even think anymore. She had to say whatever it took. She just wanted to taste it..."

al "Puh-please Mistress! Please!"
al "Ride my face! Use my mouth!"

"Something liquid rolled down her cheek. Was she crying? Or was it something else?"

al "Let me...uh...worship you, Mistress! Let me treat you like a Queen!"
al "Please, Mistress, Please! I need it!"

"She finished with a pathetic whine. She didn’t care what she had to say. She just wanted the teasing to end."
"There was a moment of silence. Alexia couldn’t see her mistresses’ face. Was she smiling or frowning?"

je "Better."
je "Since I’m such a kind queen, I suppose I’ll indulge my slut…"

#a most excellent seat cg1 var 2
scene cg415 with fade
show jezera naked happy behind cg415
show alexia slave aroused behind cg415
pause 3

"Jezera lowered herself slowly. First, until Alexia’s mouth made contact. But, then further and further until the pressure of her entire body was pressing down on Alexia’s face. Her world went into darkness."
"Alexia gasped for air. But, all she got was more musk. The scent of it was overpowering. It robbed her of whatever sense she had left."
"The redhead let out her tongue, and soon it was working at the slit above her. In her state of complete helplessness, it was the only thing possible. Lick and lick and lick."

je "Mmm. Good girl. That wasn’t so hard, was it? There’s only one way for this to end. You have to keep on going. All the way."

"Alexia let out a sigh, muffled by Jezera’s body."
"Alexia put her entire being into her tongue. It was hard to think. It was hard to even breathe. Her pussy was throbbing, but there was little she could do about it."
"The only thing she could do was work Jezera’s pussy. Nothing else mattered. Nothing else pierced the veil. Caught in the scent, and the emotion, and the thrill of it. There was one thing, one action, one desire." 
"Her efforts certainly seemed to be having an effect. After a few minutes, she felt the wetness above her grinding and sliding, covering her entire face with the thick moisture. Jezera was grinding on her as though she were a pillow."

je "Such a good girl. Such a good slave. Worshiping me. Worshipping your queen."

#a most excellent seat cg1 var 3
scene black with fade
show jezera naked happy behind black
show alexia slave aroused behind black

"Suddenly, Alexia’s mind was brought back through the haze by a sudden burst of pain. Her nipples being roughly pinched. She moaned out against the dominant woman’s body and squirmed in her restraints. But, there was no escaping the pain."
"She fell back into the fugue and went back to work on the folds above her. Her pussy was soaked from it all. The pain, the desperation. The sense of how overpowered her current situation left her. She couldn’t suppress the odd breathless gasp."

je "Ah. Almost...almost…"

"The body above her twisted and squirmed at the sensation. There was an odd pride in the idea that she was doing a good job."

if jezCorVisits > 2:
    "A pride that had grown increasingly common in recent weeks. The intoxication of service."

je "Ah..."

"There was a burst of movement and energy. Jezera was shivering. Then a sudden rush of taste and sensation. Her face was being absolutely covered with liquid. She could taste it. It clung to her taste buds, and no matter what she did she couldn’t get the taste out of her mouth."

je "You're not done. You're not done. Keep on going. Keep on…"

"Another burst of movement. Another set of spasms. Jezera was eeking out every bit of pleasure she could take from Alexia."

je "Ah. That's it. That's what I want, you little slut. Keep going. Keep going."

"Another spasm. This time, it left her almost slumped over on top of Alexia. The movement paused. The brief break in action reminded Alexia how badly her lungs ached. She gasped for air."
"The weight slowly lifted up. Jezera was rising from her face. At the first touch of oxygen, untainted by the other woman’s musk, Alexia panted for air."

je "Well now? Aren't you going to thank me for letting you worship me?"

"Alexia gasped and cough. She tried to form a word but found her tongue almost too exhausted to speak. The reason why required the input of no genius."

al "...Thank you...for riding my face... Mistress…"

"Alexia groaned. Jezera’s face was twisted in some kind of facial expression but it was almost impossible to see."

je "I see that your panties have gone all damp. Aww…"
je "Does the little lesbian slave girl want to touch herself just because she had her face ridden?"

"Jezera’s taunting reminded Alexia of her own arousal. Her pussy was throbbing from neglect. It cried out for its own attention."
"Alexia gasped more and nodded with as much energy as she could still give her head."

#a most excellent seat cg1 var 2
scene cg609 with fade
show jezera naked happy behind cg609
show alexia slave aroused behind cg609

"Jezera freed her from the cuffs and took a position reclining on a cushion. Alexia stumbled, groaning and panting, into a kneeling position in front of her. Even sitting up was a challenge."

je "Alright, but..."
je "With all the attention that my pussy got, it’s only fair you show appreciation to my feet as well. You will kiss them as you finger yourself for me."

"Alexia nodded her assent. Her mind had checked out some time ago, and only her lust drove her now."

if jezCorVisits > 2:
    "Besides, it wasn’t like she had the will to disobey Mistress Jezera anyway."
    
"Soon, Alexia had her lips planted to Jezera’s feet in further worship, while her fingers timidly worked at her clit. Jezera’s juices got the soles of the demoness’ foot damp. But, Jezera didn’t seem to care."
"For all she was doing, she couldn’t even taste the foot. All her tastebuds could process was the lingering sensation of pussy."
"Alexia let out a high pitch squeak. Having her face ridden must have really turned her on because within a minute she was already riding a powerful high."

je "So eager, So eager. I must have really done a number on you, girl."

"Alexia was far too gone even to process the taunting. She just wanted to cum. She couldn’t even really process the symbolism of licking and kissing another woman’s feet."
"She was almost there. She was so close. She had been so turned on when she started to touch, but now she was bordering on desperate. On a summit waiting for the drop."

al "I...I…"

je "It's alright, my love. You don't have to think. Just cum. Cum for me."

"And just like, that she fell. Her body shivered and she felt an orgasm rip through her. It ran from her pussy up her spine."

al "Fuck fuck fuck. Rowan. Fuck. Fuck. Ah."

"Alexia collapsed into an exhausted heap on the bed, twitching and groaning. It felt so good…So good…"

scene black with fade

"..Maybe it would be okay to rest a bit..."

jump jezCorVisitAftercare

################################################################################

label jezCorVisitDancing:

$ jezCorVisitScene = "dancing"
$ jezCorDancingSeen = True
$ jezCorVisits += 1

scene bg14 with fade
show alexia slave happy at midleft with dissolve

"Alexia gave Jezera’s door a soft knock. It was though she were afraid that any louder would announce to the whole castle what she was doing. But, that was enough to draw the demoness’ attention."

show jezera happy at midright with dissolve

je "You're here, darling. And here I was worrying you'd keep me waiting."

al "...I wouldn't do that."

"Her Mistress swung the door open, and moved to the back wall."

je "Delightful. Grab a cloak from the rack. My plan for today is a lesson. One that cannot be done here."

"Then, with a gesture of her hand, the surface of the wall gave way to a new passage that had not been there previously. Alexia stared in shock."

je "Come along. Come along."

scene bg58 with fade
show alexia slave happy at midleft with dissolve
show jezera happy at midright with dissolve

"They descended together into the bowels of the castle. The passage was too dark to see, but Jezera had her by the hand and acted as a guide. She just had to trust Jezera to take them where they needed to go."

al "Where does this lead though?"

je "The brothel."

#alexia slave shocked

"She nearly jumped."

al "The brothel!?"

"The brothel was public. People might see them there! And that was to say nothing of the sorts of {i}activity{/i} that a trip to the brothel might imply."

je "You needn't be so alarmed, sweet one. It's too a secret room. One I had made for my...personal indulgences. You needn't worry about squawking tongues."

"That served to soothe her, at least somewhat. It did nothing to assuage any worries of the activity itself."
"When they at last arrived, Jezera did indeed lead them to a back room. But, on the far edge was a curtain leading to a conjoined. Alexia peaked in to see what was waiting for her behind the threshold."

scene bg24 with fade
show alexia slave happy at midleft with dissolve
show jezera happy at midright with dissolve

al "Wait, there's a man in there!"

je "Mikael. One of my agents in the east."

#alexia slave angry

"She stormed back to Jezera. To avoid being overheard, she kept her voice down to a forceful hush."

al "I wasn't asking who he was! What's he doing here?"

je "Well, the lesson wouldn't be very effective without an audience, darling."

al "..."

"Jezera took a beautiful golden chair that dominated the center of the room and took it for a seat. Alexia remained standing before her, like a supplicant to a queen."

show jezera neutral at midright with dissolve

je "I suppose I've kept our activity of the night a secret for long enough."
je "I brought you here to seduce him."

if garInfo == 0:
    al "Excuse me?"
    "Jezera batted at the air as if that is where her anger hovered."
    je "Take a moment and listen to me, little one. You said that you’d trust me, did you not?"
    "Alexia crossed her arms over her chest."
    al "I suppose."

else:
    al "..."
    je "Don't act so surprised, dove. It's not as though it's the first time you've done such a thing for me."
    
je "In our agreement, I promised to help your relationship with that hard-working husband of yours."
je "If I know one thing about men, and I certainly know more then that, it is that they're fickle creatures."

je "Short attention spans. Wandering eyes. "

if raeve_keep_rowan_claimed_helayna == True:
    je "You know exactly what I speak of, Alexia."
    #if hel and alexia havent reconciled - TODO
    "Alexia had a flash of an exposed young woman, younger than her, being carried into Rowan’s bed."

al "Mistress, you must get to the point. What's going on with that man?"

show jezera happy at midright with dissolve

je "You need to learn the art of... arousing interest. Drawing eyes. The soft sigh and the subtle touch. Do it right and you can make men your slaves."

"She crossed her legs dramatically. A gesture that captured Alexia’s eyes for a split second. Then, she beckoned Alexia closer to her."

je "Now, you are not without your charms."

"The back of a purple hand brushed over Alexia’s side slowly and sensually. Alexia’s eyes fluttered slightly."

je "But, you need refinement."
je "I selected this particular task with care. You may not have much experience as a seductress. But, the art of moving your body is one you are already well acquainted with."
je "Men do so love dancers."

"Alexia glanced back to the other room and the outline of the man behind the curtain."

al "The kind of dances the women do in...this sort of establishment…"
al "I never learned how to do those. For me, dancing was always more…"

"Her tongue felt around, looking for a word. But, when she couldn’t find one she liked, she went with the best option she had."

al "Proper."

"Jezera scoffed to herself."

je "And yet, men got aroused watching you at times. They stared a little too much to only be focused on the movements. A very frequent occurrence, I’d imagine. Can you tell me I’m wrong?"

al "..."

je "And when they did look at you, you {i}liked{/i} it."

"She reclined back in the chair with the smug satisfaction of a conqueror. There was little Alexia could do to dissuade her of the notion. Jezera had an annoying way of being right about the most embarrassing things."

je "The difference between one dance and another. It's not so large. Not so large at all. I’m about to teach you some things."

"For the next ten minutes, Jezera gave Alexia instructions and tips on how to make her dancing more provocative. Alexia listened without argument, trying more so to take in what the other woman was saying."
"Yet, even when Jezera finished her tips, Alexia only felt marginally more equipped to go into that back room."

je "Mikael is trustworthy, as much as such a thing can be said of any. He's quite behold to me. You needn’t have to worry about a loose tongue."

"Jezera giggled to herself darkly."

je "Still, I procured this for you. Like the girls here wear. It will help you be... someone else...for a short time."

"In her hands, Jezera held a black veil. It was of the sort that dancers of Qerazel favored. In truth, Alexia had always wondered what such a thing felt like but had never taken the further step of trying one on."
menu:
    "Accept... for now.":
        $ released_fix_rollback()
        $ mikaelDance = True
        pass
    
    "Refuse.":
        $ released_fix_rollback()
        "Alexia slowly started to shake her head. She’d agreed to spend intimate time with Jezera. That was one thing. But, doing sexual performances for another man?"
        "Alexia placed the veil back in Jezera’s hands."
        al "I can’t do this, Mistress. If it was just you and me tonight…"
        "Jezera slumped down in her chair but actually accepted the veil."
        je "Tsk. Pushing you too hard and fast, am I?"
        je "And here I was claiming I could teach you about how to make others want something. You put the lie to me sometimes, girl."
        al "I’m sorry to have offended you."
        "Jezera rose from her chair and took Alexia by the hand."
        je "Off we go then. Poor Mikael won’t get his dance, but I’ll send down Shaya herself later to make sure he doesn’t miss it."
        je "Come along, love. I’ll think of another activity for our night!"
        return
        
"When put to her face the silky smooth texture felt oddly comforting. Like a layer of protection. Jezera was right. Draped in it, she could almost be another person…"

al "Wish me luck…"

hide alexia with moveoutleft

scene bg24 with fade
show alexia slave happy at midleft with dissolve

"She sauntered off towards the other room, trying to sway her hips. The black lace of Jezera’s nightie would certainly prove a seductive enough outfit for such an occasion."
"Yet, he didn’t even register her arrival. It was as though he were staring off into space. Alexia waited with her arms crossed over her chest."
"Then, with a jump, he noticed that he wasn’t alone any longer. "

mik "Oh. Oh. You’re here! You’re Jezera’s girl, yes?"

al "...I am."

mik "Ah, good. Good. I was just having a little nap while I was waiting. But now...now the show can begin."

"Alexia smiled to herself beneath the veil. He seemed...woozy. But, personable."

al "Of course, M’lord."

"Alexia breathed in. She just had to dance for him. She could do that. She could do that."

scene cg732 with fade
show alexia slave happy behind cg732
pause 3

"She started up the familiar steps. The twirls and sways of her body. She figured the scant outfit would help make it more enticing. But, she added a few obvious gestures pushing out her chest and rear wherever appropriate."
"Every so often, she would lose track of what she was doing. Breaking from routine was hard."
"But, she found strength in a memory. Dancing naked by the lakeshore. The thought of a pair of female eyes watching her. She didn’t know if she could dance for this man. But she could dance for her."
"She could be sexy for her."
"When the dance came to an end, she gave a long sweeping bow, just like she was used to doing back at the village."
"But, her audience did anything but clap. His eyes were half shut and he was slumped back into his chair. He was as zoned out as he had been when she first entered. It even took him a moment to acknowledge the dance had ended."

mik "Ah, yes yes. That was the warm-up performance, right? Very good. Very good."

al "Of course, M’lord. The warmup performance."

"She performed a smile."

al "One moment, if you’ll excuse me."

hide alexia with moveoutleft

scene bg24 with fade
show alexia slave concerned at midleft with dissolve
show jezera happy at midright with dissolve

"She ducked back behind the curtain to the other room, trying to keep a straight face. Trying not to let the tears form."
"Jezera was not alone. She had a succubus kneeling before her, giving her a foot massage. The lesser demon stared lovingly at the mistress of the castle’s feet. Alexia found herself feeling slightly envious."

al "I can’t do this."

je "Of course you can, darling."


if garInfo == 4:
    je "You’ve followed such commands before, after all. Shy Mr. Garforth was such a morsel too..."
    "She sighed."
    al "No. I mean. I do not know how to do this. I learned to dance for my village. For festivals. Not to make a man..."

je "I will admit that the dance was a bit...chaste. But, you have a body men salivate over, and you know how to move it. Surely a bit of abstraction isn’t beyond reason."

"Alexia continued to shake her head forcefully, undeterred."

al "I can’t do this."

show jezera neutral at midright with dissolve

"Jezera sighed to herself but did not seem especially perturbed."

je "If you insist."
je "I had prepared for this eventuality."

"Jezera kicked her feet forward, cruelly pushing the succubus to the ground. But, she only reacted with a soft sigh."

"Jezera rushed off briefly, but returned a moment later, holding a set of leather bands. Alexia looked at them curiously. All were small and easy to fit on her body. They also had strange runic markings on them."
"Mistresses’ magic, no doubt."

je "If you wish, I can teach you the moves as you dance. Work them into your muscle memory. "
je "These bands, combined with a very short ritual, allow me to control the limbs of a willing wearer. For a short time, of course. A party trick I rarely get a chance to take out, but very useful for when I do."
je "I can show you how to dance to arouse a man. And you will be able to experience it first hand."
je "But, of course, we needn’t continue with it if it is too much for you to ask."

"Jezera held her hand out to Alexia."

show jezera happy at midright with dissolve

je "Will you trust me, dove?"

menu:
    "Trust her.":
        $ released_fix_rollback()
        show alexia slave happy at midleft with dissolve
        pass
        
    "Don't trust her.":
        $ released_fix_rollback()
        "Alexia looked from the bands and down at her hand. Being controlled that way sounded too far for her. She was willing to obey Jezera, but to give up control of her own body…"
        "Alexia went down to her knees in a gesture of subservience."
        al "Mistress. I can’t do this."
        je "Come now, girl. You’re capable of more than-"
        al "Please. Not this. Not today. Please."
        "Jezera blinked twice, the smile briefly fading from her face. But, then it came back still warmer than before."
        je "Sweet girl, if you say you cannot do it, then what kind of Mistress would I be if I forced you?"
        je "Rise for me. Rise."
        "Jezera turned down to the succubus, still swooning by her feet."
        je "Girl, go entertain our guest. Take her form. Give him a good time."
        je "But, if you drain a single drop of his vitality, I will ensure you meet a most unfavorable end."
        je "Do we understand each other?"
        "The succubus nodded, with a slight smirk."
        "Alexia stared, wide eyed, as the succubus took on an approximation of her form after a minute of study. The appearance was imperfect. But, from some distance, it would suffice. Especially with the veil to conceal the facial divergences."
        "Then, her look-alike strut back behind the curtain. She was giggling and waving her rear. Alexia couldn’t help but note to herself that this...fascimile...would likely do a better job with him then she could…"
        je "Now, then, let’s come along. The night is still young, and even if it won’t be for dancing there are still some ways to put that ass to {i}use{/i}."
        "With a lowered head, Alexia followed her Mistress back up the stairs that led to Jezera’s room. But, as much as she enjoyed herself that night, she went back after with the nagging feeling that she had been a failure."
        $ change_actor_num_flag('alexia', 'jezera_influence', 1)
        $ change_corruption_actor('alexia', +3)
        return
        
"Alexia closed her eyes. She trusted Jezera. Jezera could order her to do most things and she would obey by this point. What difference would direct bodily control make?"

al "What do I need to do?"
        
"At Jezera’s direction, Alexia dutifully slipped the bands on her wrists and ankles. Then, she runs through a strange otherworldly chant Jezera explained to her. Supposedly it was simply to signal trust and confirmation to the ritual."
"Then Jezera joined in the chant, voices harmonizing. But, there was something different about the words. Even listening to them made Alexia’s head static. These were words of power."
"At first, they were incomprehensible, but the longer they went, the more Alexia understood them."

je "The strings of Aldrua call out to you from the wandering dark. They lead the secret path to a place where sky meets earth."
je "Where is the path? Say the name."

al "Jezera…"

"The moment she said the word, something was different. Her wrists felt strangely weighted down. Like there were chains leading from the bands. But, the chains didn’t seem to go anywhere." 
"She raised her, but the process was sluggish."
"But, that didn’t prepare her when her arm went down to her side. Alexia nearly gasped. She hadn’t done that. Yet, she’d still felt her arm move."
"She looked to Jezera, and her Mistress had a wide grin."
"Now, Alexia’s body sprung into movement. But, none of it was directed by her will. Alexia’s hands trailed sensually down her sides before landing on her hips. From there, she tilted her hips from side to side. Finally, she blew Jezera a sensually kiss and gave a wink."
"Alexia could barely make sense of it. It was her own body moving. But, the touch had the electricity of another’s hand. Sensual."

al "It feels...strange."

je "Not so strange that you wish to back out, yes?"

al "Correct..."

je "There is a certain thrill to new experiences, my dear. But, I don’t need to tell you that, do I?"

"Jezera settled back in her impromptu throne and crossed her legs. The succubus took that as cue to crawl back over and resume the act of worshipping Jezera’s legs."

je "Ready to resume your dance? I’m sure sleepy Mikael is waiting for you. Don’t worry your little head how you’ll do. I’ll be with you the entire time."

scene bg24 with fade
show alexia slave happy at midleft with dissolve

"This time, when Alexia returned to the room with Mikael, she walked with swaggering hips. The motion almost made her gasp."

mik "It’s a good thing I’m a patient man. You made me wait for a long time."

al "..."
al "I’m very sorry, Mister. I need to make it up to you."

"Alexia went to the center of the room and began a dance. But, this was no dance she’d ever learned. It mostly involved the twirling and gyration of different parts of her torso. Her hips, her ass, her breasts. All of it was emphasized."
"As she swayed her body back and forth, her hands reached up to grasp her breasts as if to present them to her audience."
"The entire time, Alexia was little more then a puppet. If she tried, she could fight it, but it was far easy to go on autopilot. To become an observer from an unusual vantage point. "
"She also tried to memorize every motion. She was here to learn a lesson, after all. It was easy to grasp when her own body was doing the dance. The way it would be easier to repeat an act you’ve done in the past."
"She almost didn’t notice as she closed the distance. Now, her body was provocative twisting and moving mere inches from his face."
"She caught a glimpse of his eyes, wide and alert. Sleepy Mikael had woken up. The unrestrained male hunger was etched on his face."
"Alexia’s heart skipped a beat. Jezera really was right. Dancing like this..dancing so lewdly...really did entrance men."
"Her hands reached up to the straps of her dress without Alexia even realizing it. She had to suppress a look of surprise as they slid away...before pulling them back up. The teasing guessing game was as effective as it was on Mikael."

al "Whoops. I’m not in control of myself."

"She spoke in a shaky voice. It was hard to seem in control of the room, when she as much a subject as he was."
"She took another step closer. His knees nearly touched her. Her body gyrated and her ass waved, so close he could reach out and grab her."

al "Do you like what you see, Mister? Am I doing good?"

mik "You are. You’re beautiful."

"Jezera made her hands return to the straps. This time the thin fabric fell to the floor. Her cheeks burned. The lustful man eagerly drank in the sight of her exposed body. Her breasts...her ass...the place between her legs."
"All the while, her body continued onward. She felt herself slide up atop his lap, straddling him. The hardness beneath his trousers pressed against her exposed thigh."
"Her mind flailed. What should she say? What should she do? If Rowan knew about this."
"His hand reached out, trying to grasp her side."

mik "Can I touch you?"

"Alexia found herself expecting Jezera to control her response somehow. It was easier when Jezera decided."
"But, with a sigh of relief, Alexia realized that Jezera wasn’t interceding. For this split second, she had control."

menu:
    "Agree.":
        $ released_fix_rollback()
        $ mikBJ = True
        scene cg733 with fade
        show alexia slave happy behind cg733
        pause 3
        al "How about you let me do all of the touching?"
        "Alexia spoke in a purr. This situation, the feeling of being watched. All of it was putting a fire to her."
        "Jezera was in control again, and she made her puppet sink down to her knees between his legs. Her fingers brushed against his thighs." 
        "Alexia sighed silently. The control was back. She could lean back and enjoy the ride."
        "Her hands eagerly worked the man’s cock free from his trousers. It sprung up, large and hard, into the open air. Alexia couldn’t help mentally comparing it to Rowan’s."
        "Then, her head went low. She offered no resistance, even as Jezera made her lips open and wrap around his cock."
        "Here, too, Alexia passively enjoyed the ride. She felt every sensation. She tasted the trademark salty male flavor. She felt the shaft hitting the back of her throat. But, it was as though it was a thing happening to her."
        "Her body was setting the pace, but to Alexia, it was like being face fucked."
        "At one point, she tried to pull her head back slightly for more air. But, soon found she couldn’t. She was left to gasp and rasp, but there was no way she could escape it."
        "...And yet, the entire time she was growing more and more wet…."

    "Don't agree.":
        $ released_fix_rollback()
        $ mikBJ = False
        al "Nope. You can look. But, you can’t touch, mister."
        "The dance continued on into the night. Mikael tried to reach out and grab her several times, but each time Alexia was allowed by Jezera to refuse. There was a line Alexia wouldn’t cross and it was here…"
        
scene bg18 with fade
show alexia slave happy at midleft with dissolve
show jezera happy at midright with dissolve

"Alexia laid back in Jezera’s grand bed, taking in what had just happened. The demoness had used her enhanced strength to carry Alexia back up after the dance."

if mikBJ == True:
    "Jezera pulled a handkerchief from a side cabinet and tossed it to Alexia."
    je "If you’d like to clean up your mouth a bit before we continue, little one."

"Alexia blinked a few times."

al "That was…"
al "That was something."
al "Did I just do that?"

je "Arguably. Depending on what you consider doing yourself to be."

"She eyed the bands. After the dance, she had not bothered to take the bands off, even if Jezera stopped actively controlling her body."

al "Dancing that way was strange. I remember every move. I could even probably repeat them right now if I tried. But, it wasn’t me."

"Then another image flashed to her mind. The way that Mikael had stared at her. She was used to being ogled. But, she’d never got a reaction quite like that from her dancing. Even when dancing for Rowan in the past."

al "Is that really how men like it when you dance?"

je "It drives them mad with lust."

"Jezera settled in next to her and softly brushed her hair."

je "A proper dance heightens everything men enjoy. It reinforces our natural beauty and draws the eye. It teases them and makes them long for more."
je "You remember the moment where I had you feint removing the dress? To inspire desire, but leave them on the edge of the seat. It’s a powerful emotion."

"Alexia blushed slightly. It wasn’t just Mikael who’d been filled by anticipation by that. She had been as much a spectator as he had been."

al "Still…"
al "I wonder if that’s what men were always looking for whenever I danced…"

"Jezera giggled softly to herself. Then she rose to the center of the room and took a prominent position. The plot worked. Alexia trained her eyes on her. "

je "So existential, my dear. But, let’s turn the question around. By now we’ve established you have a certain {i}appreciation{/i} for the bodies of other women."
je "Have you ever found yourself staring at any of your fellow dancers before? When you had, was it entirely chaste appreciation?"

"Alexia didn’t have an answer for her. She’d never thought about it, of course. But, what was the motive all those times she’d looked back at the other dancers?"
"Jezera leaned in closer. She smelled blood."

je "You’ve been a good girl tonight. I want to give you a reward. A dance of your own so you can see it from the other perspective."

al "Please…"

je "Just one thing."
je "Keep the bands on."

"Alexia shivered."

al "Yes, Mistress…"

scene cg734 with fade
show jezera naked happy behind cg734
show alexia slave happy behind cg734
pause 3

"In a single fluid motion, Jezera let her dress slip to the floor. Clad in nothing but her heels, she strutted up closer to Alexia before suddenly and provocatively bending low. Her hair whipped out. But, then in an equally fluid motion, she rose back up. Beneath her hair, Alexia saw her grin."
"The housewife was transfixed. Every element of her performance was practiced and smooth. And her body was...her body was having an effect on Alexia."
"Jezera put a hand to Alexia’s chin and forced a meeting of their eyes. Alexia was breathless."

je "Am I beautiful, pet?"

al "So beautiful."

je "Good."

"Jezera turned back and retook a position in the center of the room. Her ass swayed invitingly behind her." 
"That was when Alexia noticed that her own body was moving. Her right hand was ever so slowly gliding between her legs, fingertips brushing over her skin. She stifled a moan. Her stomach was butterflies. "
"She had no control over her hand. She couldn’t stop it. But, even if she could, there was little question if she would have actually done so. "
"Then, her fingers made contact with her clit. For some reason, it felt immeasurably better than masturbation ever had."

al "Oh."

"She could not help that her own hand was stroking herself to the exact rhythm of Jezera’s swaying and dancing. As if to reinforce the effect of each move."

al "Oh."

"The style she struck was different from how she masturbated when she had control. But, Alexia had to admit that Jezera’s method was more effective. She was getting very wet."

al "O-oh."

je "Distracted by something, little one? I don’t want you to miss my dance. It would be so rude~."

al "O-of course not, Mistress."

"The more Jezera danced, the more she took power over Alexia’s body. Now the squirming girl couldn’t look away if she tried. Her free hand went to her nipple and gave it a sudden pinch. Not so hard as to hurt. Just to make her jump."

al "Ah!"
       
"Now her hands continued the assault on her body. Stroking her clit and pinching her nipples. Her body was left jumping and squirming. Dancing in it’s own way."
"She was a puppet. Jezera was making her a puppet. Alexia tried to moan out, but even that was beyond her control."
"Jezera closed the gap once more. So close that her heavenly scent filled Alexia’s nostrils. It was intoxicating. And that was even before she pressed Alexia’s face to her bosom."
       
al "Mistress...Mistress I can’t stand it. I can’t take it."

je "Oh, so you want to stop?"

scene cg735 with fade
pause 2
scene cg736 with fade
show jezera naked happy behind cg736
show alexia slave happy behind cg736
pause 3


"At once, Alexia’s hands stopped their motion and fell limply to her sides. This time, Jezera let her moan out. They had been inches from taking her over the edge…"
"She tried to move her own hands, but they were outside her control. She even tried to grind against the bed, but her hips wouldn’t move."
"Jezera resumed her dance. Now, Alexia was a breathless spectator. Her cunt ached for attention and seeing Jezera’s beautiful body gyrating only caused her need to heat up to an aching inferno."

al "Please Mistress. Please…"

je "You have to be specific for what you’re asking for, sweet one."

al "Please Mistress...I want to touch my...no."
al "...Please, {i}make{/i} me touch myself…"
al "Please...goddess above, please."

"Jezera smirked to herself. A victorious conqueror."

scene cg739 with fade
show alexia slave happy behind cg739
pause 3

"Then, Alexia’s hand shot to her sex. A long low moan in thanks escaped her lips as Jezera penetrated her with her own fingers."
"Her hand fucked her hard and fast, sinking three whole fingers in." 
"In that moment, she imagined herself as an actual puppet. Stiff joints and wooden features. And at every limb strings. Jezera would pluck and toy with each string, and Alexia would dance for her and dance for her."

al "Almost...almost…"

scene cg740 with fade
show jezera naked happy behind cg740
show alexia slave happy behind cg740
pause 3

"Her hand stopped once more. This time Jezera left Alexia hump the air, body searching for the missing fingers."

al "Mistress...Mistress...why…"

je "You can’t hide it from me, you little tart. You whine, but when I make you stop you like that too. Not having any control whatsoever."

"Alexia answered in a wide-eyed moan. Words came to her throat, but it was hard to form them."

scene cg737 with fade
pause 2
scene cg738 with fade
show jezera naked happy behind cg738
show alexia slave happy behind cg738
pause 3

je "Admit it."

al "Y-yes."
al "I like it when...I like being controlled…"
al "Please...please make cum."

"Finally, Jezera placed her lips to Alexia in a long slow kiss. Alexia’s eyes fluttered." 

scene cg739 with fade
pause 2

"Then, with their tongues entwined, Jezera made Alexia’s hands come back to her pussy one final time. This time there was no more artifice. No more teasing. In a matter of seconds, Alexia was brought to a white, mind-melting orgasm."

show cg741 with sshake
show cg741 with sshake
pause 2
show cg742 with flash
pause 3

"Neither the kiss nor the touching let up. Jezera dominated her tongue for what felt like days while using her hands to eek out orgasm after orgasm from her shivering body."
"At some point, Jezera removed all the bands from her body. Now it was nothing but her own skilled hands doing this to her."
"Each time she exploded, it left Alexia more and more blank. She felt like she was slipping away…"

jump jezCorVisitAftercare

#################################################################################

label jezCorVisitInfiltration:

$ jezCorVisitScene = "infiltration"
$ jezCorFaceInfiltrationSeen = True
$ jezCorVisits += 1

scene bg18 with fade
show alexia slave happy at midleft with dissolve
show jezera happy at midright with dissolve

"Alexia’s hands fidgeted as she worked the knob on Jezera’s door. What “lesson” would Jezera have for her today? Something pleasurable hopefully. She almost expected her Mistress to be waiting for her with whips and chains in hand."
"Instead, she found Jezera sitting at her table, with a large painted map spread out over its surface."

al "I hadn't known there was a form of lovemaking that involved sheets of parchment."

"She covered her mouth with her hand while she giggled. Jezera rolled her eyes, but beneath them was a smile."

je "If you tease too much, I might have to actually find a sexual purpose for such a thing."
je "But, alas that’s an idea for another day. Today's visit will be of a more practical variety. At least for the moment."
je "You're already making great strides when it comes to seduction. Now it's time for you to learn about infiltration."

al "Infiltration?"

"Jezera leaned back in her chair and directed a sweeping gesture at the map in front of her. Alexia took the seat opposite her."

je "There's a great many things of value to learn from places you're not supposed to be. Knowing the right man or woman to flirt with can get you into the room…"
je "...But knowing the art of infiltration can take you from there to the places you shouldn’t be."

al "You mean like being a spy?"

"She shook her head softly. The image it brought to her mind was of an assassin scaling walls with daggers in hand."

show alexia slave neutral at midleft with dissolve

al "No..No. That’s absurd. I don't understand why I'd need to know about such a thing? I mean, you told me to visit you so I could learn more about how to be pleasing to Rowan…"

je "I said I’d teach you to be pleasing. But, I also promised to make you more useful, didn’t I?"
je "My sweet innocent little bird. You're a captive in a castle filled with secrets and you don't want to learn how to get places you don't belong? How many places in Bloodmeen do you think I’m keeping from you?"

"Alexa scoffed."

al "Why would you…"

je "Help you learn to be more sly when you're my prisoner? Maybe I'm curious what you do with it. Maybe, I'm not as much of an enemy to you as you might think."

"Jezera leaned forward, bringing together her fingers in a pyramid in front of her face."

je "...And maybe, just maybe, I don’t want you to be my prisoner at all."

"Alexia had no choice but to stare at her Mistress cynically. She might have warmed to the woman, but there was still no doubt in her mind that Jezera was her captor. Alexia’s eyebrows narrowed. Didn’t Jezera know if she wanted, she could release Alexia in an instant?"
"But, just as fast her brow softened. No doubt Jezera was simply insinuating that they could be friends if she so wished. Still, the question of motives was not the only misgiving that weighed on Alexia."

al "Hrmm."

"Alexia looked off to the side. She remembered those days in years past where she’d been home alone waiting for Rowan’s return. From her letters, he was saying that he’d done incredible things. Things Alexia could never imagine doing."
"It had been her lot in life to sit and await his arrival. It was how it always was."

al "I don't know if I'm cut out for something like this though. Being more pleasing to a man is one thing. But, learning the arts of spycraft? I’m sure you’re a great teacher, Mistress. But, you’d be better off teaching a-"

"Jezera put a finger to her lips to silence her."

je "Shhhh. Not a word more. You’ve put yourself down too much. I have an eye for talent, girl. And I know for a fact that you're more capable than you would imagine. "
je "Trust me. Mistress knows best."

al "..."
al "Fine. I can try."

"Alexia settled back into her seat. She was no more enthused than she had been minutes prior but thought it best to at least humour her Mistress. No doubt Jezera would see that this was a step outside her range and pull back soon enough."
"From there, Jezera broke into the lecture that she had been dying to start. Alexia did her best to pay attention...and not show her disappointment that Jezera had decided against playing with her."
"Among her first topics were the simple mechanics of exploring unfamiliar spaces. She demonstrated by pointing to different spots on the map, a reproduction of a base she has infiltrated once."

je "One of the follies of humans, the many many many follies, is complacency. You always want for nothing to be unusual so much. It makes things so much easier."
je "You see, one mistake will be ignored. A guard or a passerby will wish it away. You will be a gust of wind or a figment of his imagination."
je "It’s the second mistake that gets you caught. That’s when it becomes much harder for them to wish your presence away."

"From there, Jezera moved to consideration of what to do once Alexia had managed to get into the back rooms or secret locations."

je "A fool might search the obvious places. I do not train fools. When on the hunt for objects of interest, you must have a little switcheroo in mindset. You’re the one who is doing the hiding. Where do you hide it?"

"By the point Jezera reached discussion of what to do if caught, Alexia felt like her eyes were going to glaze over. The number of rules and axioms were almost too vast to deal with."

je "Of course, sometimes it's hard to get out just with honeyed words. Were it possible, I could talk my way out of the dungeons of Prothea itself. Have no doubt of that."

al "...Sure."

show jezera neutral at midright with dissolve

je "Still, this is yet another area where the superior sex reigns. Guards can be persuaded or bribed to look the other way, and it is here a woman can use her advantages."

"Alexia stared dumbly ahead for a moment before the implication of Jezera’s words came to her."

je "Advantages? You most surely don't mean using your body?"

show jezera happy at midright with dissolve

je "I {i}most surely{/i} do. You hire a guard hoping they’ll think with their eyes. But, more often they think with their crotch. Someone smarter or more capable would have a more prestigious job."

"Jezera sighed and gave the map beneath her a wistful glance. As if some memory were etched on its surface."

je "I cannot tell you how many seemingly fatal situations I've escaped with a pouting lip and a bit of cleavage. {i}Oh, mister guardsman, thank goodness you’re here. I just happened to get lost and I was so scared...{/i}"
je "Of course, sometimes you need to go a bit beyond that. But, that’s where the other training I’m giving you will be most useful, one must suppose."

"Alexia simply shook her head back and forth, as if the action could stop Jezera’s words from entering her ears."

al "You can’t be serious. You’re saying if I actually tried being a spy, that I’d need me to...to fuck my way out if I got caught?"

je "Well, if it came to that…"

"Alexia put her hands on the table."

al "Impossible. Just...no. I could never do something like that. Impossible."
al "All of it is simply so...so beyond me. Surely there are other people to train in these...these tactics. Smarter people. More capable."
al "This is just...it’s not me."

"In truth, Alexia had expected Jezera to burst into yet another round of assurances. More assuaging to calm her down. But, Jezera didn’t do that."
"She merely sat quietly, turning Alexia’s words over in her head. Then, Jezera smiled."

je "I had an inkling you’d say such a thing. Blame it on our growing familiarity. Thankfully, your Mistress was well prepared."

"Jezera rose from her seat and began the process that Alexia recognized by now as the formation of a portal."

je "It won’t take us far. Just to another portion of the castle."

"Jezera extended a hand to Alexia."

je "Do you trust me?"

"This was a question that had been answered firmly already. Alexia took Jezera’s hand and walked with her through the portal."

scene bg14 with fade

"On the other side, she found a design not much different from the area she had left. She’d expected to be taken to some strange secret chamber, but it was just a normal Bloodmeen corridor."

show alexia slave neutral at edgeleft with dissolve 
show jezera happy at midright with dissolve

"She went to a window and found the main bulk of the castle rising proud."

al "This is one of the outer spires, isn’t it?"

je "An unused one. There’s just so much of this damned castle, we haven’t occupied the whole structure. So a few locations have gone a bit..neglected."
je "Thus, it’s the perfect training yard."

"Alexia turned back to Jezera."

al "You still haven’t told me what it’s even a training yard {i}for{/i}."

je "Of course, of course."
je "The best place to start, though, would be having you get undressed. You can leave the choker on though. I like that on you."

"Alexia glanced to the side. The hallway was empty, but changing in public still felt..exposing."

al "Here?"

je "There’s a supply closet behind you. It will have to suffice."

hide alexia with moveoutleft
hide jezera with moveoutleft

"Alexia sighed and slipped into the confined space. Jezera followed, of course. Though, if there was one pair of eyes she didn’t mind watching her undress they were Jezera’s. Well, hers and Rowans. The dark fabric of her nightie fell to the floor. "
"Without thinking, her arms went to her chest, softly covering her exposed body. Jezera gave a nod of approval."

show jezera happy behind bg14

je "As ravishing as ever, my dear. Now then, I planted a case with some items of interest in the room earlier today. It should be right behind you. Please, be a dear and put on the items inside of it."

"Obediently, she turned to follow Jezera’s instruction. The first item she found was a set of black high heels. The sort some nobles wore."

je "To help you be aware of your own movement, of course."

"She worked her feet into the shoes and tested them. It was as if someone had put platforms beneath her feet. It took a few seconds of experimentation before she could even stand steadily."
"Next, Alexia went back to the box to collect the other items. Her face paled when she brought out the contents."
"One item was a lace black thong. All on its own it would have been far more indecent than any undergarments she might otherwise wear. But, they were made stranger for a pair of open circles with latches on the bottom string. "
"The purpose of the openings was made clear by the other items. A pair of white stone pillars shaped with one smooth end. They were made all the more slippery by a layer of oil-like substance over the surface."
"The bottom of the two pillars was complete with strange symbols that looked similar to Jezera’s magic runes."

je "Those go inside, love. A little something to make the task more...enjoyable."

"Alexia blushed fiercely."

show alexia slave aroused behind bg14

al "I was wondering when tonight’s visit would become more perverse..."

je "Tut tut, Alexia. Don’t dawdle."

"The complexity of the design made Alexia struggle to bring it all together. Then, with a deep breath, she lined the two phalli to her pussy and rear. Her eyes fluttered softly as she sank them in."

al "Oh!"

je "They have a few slightly unusual functions, but I don’t want to spoil the fun. Of course, you might feel an impulse to take them out early during the coming session."
je "So, I am going to have to make you give me a promise. No matter what, you’ll leave them in."

"Alexia could only pay attention to what she was saying with great struggle. It was far easier to focus on the sudden sense of fullness from having both of her holes stuffed at the same time."

al "But, you still haven’t even...er...even told me what I’m doing."

je "And I will. Though, after the promise, of course."

"Alexia steadied herself against the wall. It was quite like Jezera to play games with her this way. But, it was also becoming quite like Alexia to acquiesce to what Jezera had planned..."

al "Yes, Mistress. I...I promise I won’t take them out, no matter what happens."

"Jezera grinned wide and brushed the back of her hand against Alexia’s cheek. It burned all the more from the touch."

je "Delightful. Simply delightful."

"But, just as quickly as the touch had come, Jezera drew her hand away."

je "What will transpire now is a game of my own creation. One with the express intent of teaching you the principles I discussed before."
je "This tower has many rooms, but only three are unlocked. In one of those rooms, I have planted a delightful hand-carved figure in my own image. Very expensive, I assure you."
je "To win the game, you must navigate the area, and find the hidden treasure wherever I have decided to place it."

show alexia slave neutral behind bg14

"Alexia stared dumbly."

al "You want me to...to prance about the place without a shred of clothing?"

je "The nudity is to simply instill the right frame of mind. The sense of paranoia and vulnerability that an infiltrator feels. As I said before, there is no real risk of exposure. This tower is entirely unused and unoccupied."

"To emphasize the point, Jezera leaned down and stole away Alexia’s discarded clothes."

al "..."

je "It is just for the duration of the game. When you have found the figure, simply return to the base of the tower and I will be ready to sweep you up and bring you back to my quarters."
je "Entirely unseen, of course."

"Alexia shifted in place. She suddenly felt much more naked than she had even a moment before. Those damned insertions certainly weren’t helping."

al "But, where will it be? How am I expected to find it?"

"Jezera patted her shoulder and offered a reassuring smile. With her, any contact seemed to feel good."

je "I have left open an armoury, a bedroom, and a book-keeping library. The figure has been hidden in one of those rooms. "
je "As for which of the three...well, where do you think someone should hide something important?"
je "I think that should suffice, however. As adorable as you look, pouting like that, this isn’t a test of whether you have the skill to beg for a better result out of me."

"Without further warning, Jezera pulled back."

je "Ta ta, Dove. Try to remember my lessons."

"Alexia was so startled, that Jezera’s departure didn’t process until her Mistress had already left the closet. She followed into the hallway, near tripping in the tall high heels."

hide alexia
show alexia necklace naked at midleft with moveinleft

al "Wait! No!"

"But, by the time she looked around, Jezera was already gone. Vanished. Alexia was left to frantically look back and forth across the empty, torch-lit hallway."

al "...Come back…"

"Just then, she felt a breeze crawl down the hallway. Instinctively, she moved to cover herself with her hands. It drew her back to reality…"
"...She was alone here. And naked."

al "Crud."

"She was left to wrestle with her misgivings. Had her Mistress simply just abandoned her naked in the middle of the tower? What would happen if someone chanced along?"
"Jezera claimed that the spire was uninhabited. But, just how much was Alexia being forced to rest on that claim?"

scene cg971 with fade
pause 3

"Eventually, deep breaths steadier her resolve once again. The simplest way to return to the castle, and her clothes, would be to complete Jezera’s little game." 
"So, it was with great weariness that Alexia started down the hallway, hopefully towards the first of the rooms. But, even moving about proved a task in of itself."
"First, she had to master even walking in such extreme heels. There were numerous points she nearly tripped over her feet. But, with some steadying from the walls she managed to avoid any nasty falls."
"Next, she had to manage the phalli that were held by the thong. They proved a much more dramatic distraction when she moved. But, at rest she was able to calm herself down."
"In practice, Alexia was starting and stopping on her trek through the halls. The heels forced her to exaggerate her walk, but doing so just teased her with the insertions until she couldn’t continue."
"It was torture. Jezera had outdone herself this time."
"It was thus with great exertion that she finally found a door that had been left open. A peek inside revealed a prim and proper guest bedroom."

if all_actors['alexia'].job_state.job == 'maid':
    "It was in the standardized design that was common throughout the castle. In her daytime work, she’d cleaned ones like it hundreds of times."
    
show bg7 with fade
show alexia necklace naked at midleft with dissolve

al "Confound these things…"

"She reached a hand down and softly touched the base of the invader in her snatch."

al "Would she even know if I took it out?"

"Her eyes settled on the bed sheets at the same time. It wouldn’t be difficult to fashion them into a makeshift dress for herself. Jezera wouldn’t like that, but…"

al "..."

"Her hand slipped back down to the ground. Her gaze ducked back under the bed. She had a task to complete. Mistress Jezera had worked so hard to set it up for her."
"Still, her search of the room proved fruitless. If the object of her search was hidden here, it wasn’t in a place she could find it. That meant it was time to consider the next room. A small map posted to the door made that easier."

al "Armoury? Or Record Room?"

"The goal was to find where someone would put their secrets, right? The armoury sounded like a better bet."

show bg14 with fade
show alexia necklace naked at midleft with dissolve

"Once more, she started down the hallway. But, now with a growing confidence. She was getting better at walking in the heels. This was going to be much easier now that-"
"Alexia’s eyes wide went wide. She heard a sound. Footsteps."

quest "Well that’s what I told them. You want me to do extra shifts, I want extra tokens to use at the brothel. Maybe even some time at the slave pits doing…"

"Two shadows marched together in tandem on the wall. Alexia felt her heart beat so fast, it was as if it were trying to escape her chest. Jezera had said no one was here. Jezera had said no one would see her like this."
"...See her like this…"

al "Jezera said..."

hide alexia with dissolve

"Alexia’s body moved on its own. She threw herself behind one of the pillars, clutching the stone exterior for dear life. Every nerve ending in her body was crying out to her in panic." 
"What if she was seen? What if she was found?"

quest "What was that? Did you hear something over there?"

"Alexia threw her mouth over her hands in a panic. No, it wasn’t her whisper they’d heard. It must have been her footsteps. Jezera had made her wear these damned heels."

quest "Humie worries for nuthin’. Come on."

"Alexia remained frozen in place. Her chest rose and fell at a frantic pace. They seemed to have given up on her. But, she had to make sure. She couldn’t let out so much as a sound."
"But if her body was still, her mind was racing. How had this happened? Had Jezera just made a mistake? What if Rowan somehow found out about this?" 
"She slammed her eyes shut. If there was one thing she wanted to do, it was cry. But, if she did that, she’d make too much noise. What had Jezera said? That they’d just wish her away?"
"So, she remained still and in place until she was sure beyond doubt that the guards were gone. Only then did she continue to her destination."
"But, now she moved with new caution. Every so often she heard sounds down the corridors. There were other people here. More guards. She was trapped. Exposed."
"There was only one thing to do. Keep going. Find the figure and have Jezera spirit her out of here."

scene bg11 with fade
show alexia necklace naked at midleft with dissolve

"The next destination on her path was the armoury. But, her search here proved fruitless. She turned over racks of weapons and opened chests, but there was nothing that looked like Jezera. Nothing that even looked like it had been touched in decades."

al "Come on. Come on. Come on."

"That only left one location in her search. The record room."

scene black with fade

"She leaned against the wall to catch her breathing. Once more, she toyed with the urge to just throw in the towel. Jezera would be forgiving when she learned the tower actually was being guarded, right?"
"Alexia shook her head softly. Even if she didn’t want it to be the case, she knew the truth. Oh, Jezera would smile and be sympathetic if Alexia failed. But, beneath that encouragement would be that dreaded hint of disappointment. Alexia couldn’t fail her."

scene bg14 with fade
show alexia necklace naked at midleft with dissolve

"Once more she started down the hallway, taking careful measure to control the pace of her steps."
"But, suddenly there was a soft sound, almost like a click. Then, what had already been a difficult task for Alexia became harder."
"She’d grown used to the two phalli invading her lower holes. They still left her feeling full and worked up, but she’d learned how to advance without making their presence more unbearable. But, now they came alive."

al "Wha-"

"Yet, now they started to shake and vibrate inside of her. She had to bring both hands to her mouth to stifle the loud moan that almost slipped out. Her body throbbed with waves of pressure attacking her nethers."
"She had to stop herself from sinking to her knees. Her legs were turning to mush beneath her. The assault of sensation was almost so intense that it made it hard to question what was happening? Had Jezera enchanted the phalli? Why was this happening now?"
"It was with some great effort that she managed to start down the hallway once more. One hand gripped the wall to steady her, and the other remained perched over her mouth to block the onslaught of squeaks and moans that tried to bubble out."
"Her path forward was filled with more challenges. On several other occasions, she heard shadows on the wall or the sound of footsteps. Each time, Alexia was forced to duck into hiding and pray that she could maintain her silence."
"Her hips bucked softly at the air. The stimulation was driving her body crazy, even if it remained so low as to just keep her heavily teased. She felt her thong soak. Her inner thighs were growing damp."
"Naturally, she let out a sigh of relief when she arrived at the open door to the record room."

al "Al...almost…"

scene cg972 with fade
show alexia necklace naked aroused behind cg972
pause 3

"But, there was no relief waiting for her inside. Her search simply found dusty collections of books. Perhaps it was the lust getting to her. Or her own panic. But, she couldn’t find it anywhere she looked."
"She slowly sank to her knees, broken."

al "It couldn’t...unf...it couldn’t be in any of the other rooms. I’d have to…"

"She threw her head into her hands and sobbed quietly. A sound only broken up by weak moans. Even her despair didn’t grant her escape from the teasing phalli."
"This was it. This was the final defeat. She’d have to return to Jezera in failure." 
"Unless…"
"She steadied herself with her hands. Enough to try to think through the cloud of lust that was fogging over her mind. Jezera had said so many things during the lesson earlier. She formed an image of her mistress in her mind’s eye."

show jezera neutral behind cg972

je "{i}A fool might search the obvious places. I do not train fools. When on the hunt for objects of interest, you must have a little switcheroo in mindset. You’re the one who is doing the hiding. Where do you hide it?{/i}"

al "..."
al "Hrmm."

"She looked around the room. If she were hiding something important, where would she hide it? Surely, it would be in here. People would expect important things in a bedroom or armoury."
"Her eyes went to the book shelves. There was a section on one of the bottom rows for records of taxes paid from centuries past. Out of the way and boring."
"Alexia crawled on her hands and knees to that segment. Its books soon littered the ground as she threw them out, one by one. Soon, all of the tax books were scattered over the floor."
"...revealing a wooden figurine in the shame of a buxom woman hidden behind them."

al "Yes!!"

scene bg14 with fade
show alexia necklace naked at midleft with dissolve

"She started back down the hallway, squeezing hard on the figure. Her nails nearly dug into the soft wooden exterior." 
"This time, her trek was more bearable than it had been before. Yes, the insertions still left her body throbbing with desperation. Yes, the sounds of guards patrolling the hallway still stopped her every few corridors."
"But, now she was almost there. She just needed to reach the base of the tower. Then Jezera would take her away from this stressful place. Then, her Mistress would ease the endless need between her legs." 
"Just a little bit more..."

quest "Hey you!? Whassa pretty lil hummie gurl doin’ out here?"

"She turned sharply on her heels and found herself face to face with a female orc. She was tall and imposing with clear muscles and the armor of a soldier or mercenary. Her hair was shaped into a tall and imposing mohawk. One of the guards perhaps."

al "I...I…"

"All of the anxiety of the past hour hit her at once. The sense of exposure. Of being on display. The fear of failure. The fear of Rowan finding out. All were realized in the eyes of the woman who’d found her."

show alexia necklace naked concerned at edgeleft with moveoutleft
 
"Alexia took a step backwards, body shaking."

al "No...you’re not supposed to...no…"

femorc "Dis ain’t no place for nakie humie girls. No place at all. Youz a pretty one too. Must be one’a da girls from da slave pits, no?"

"The orcess took a step closer, one hand on her hips. Her glance was predatory. She made no compunctions about ogling Alexia’s naked form. The more she looked, the more Alexia’s cheeks burned."
"Could she run? Not in these heels, that was for certain. She couldn’t fight. Maybe she could pull rank. Point out her husband was an important man. But, that might just get back to him sooner."
"Yet, as her mind worked, her body was frozen stiff."

femorc "Out wit it, girlie."

"The guard crossed her arms over her chest and snorted." 
"Just as Alexia was about to move to her next denial, the phalli inside her chose this inopportune moment to spring to life. A wave of vibrations hit her strong enough to send her down to her knees, her lips opened into a pant."

show alexia necklace naked aroused at edgeleft with dissolve

al "Not now...No…"

"The figure of Jezera tumbled out of her open grip to the floor."
"That brought an evil smile to the guard’s face. There was no way she hadn’t seen the insertions. While she didn’t seem the brightest, even she must have realized the cause of Alexia’s bodily reactions."

femorc "Whateva ya doin’ out here, It’s naughty ain’t it? I gotsa admit doe. Ya do look real prutty on ya knees dat way."

"Alexia sealed her eyes shut, forcing herself to regain focus. The guard was...was saying she was attractive, right? Perhaps there was a way forward."
"But, did she really have the will to see it through? To debase herself so low?"

menu:
    "Seduce the guard.":
        $ released_fix_rollback()
        $ femorcSeduced = True
        "Alexia bit down on her lip and looked up at the imposing guardswoman with large wet eyes."
        al "Wait!"
        "Alexia drew her posture up into a more formal kneel. The sort Mistress Jezera liked. Of course, this had the secondary benefit of making her breasts more prominent. She drew her arms close to shove them up even further."
        al " I’m supposed to be here. I..I promise. But, if you want I can provide some...er...something to help you forget I was here.”"
        "The smile on the Orcess’ face grew from ear to ear. Her tusks curved."
        femorc "What kinda sumtin, you talkin’?"
        scene cg973 with fade
        pause 3
        "The taste was oddly familiar. Of course, Alexia was not such an expert on the flavor of other women that she could really make such a judgement. But, there was something soothing in that recognition."
        "Perhaps the juices of an Orcess was not much different from that of a human?"
        "Alexia was positioned with her head between the guardswoman’s legs, lapping steadily at her clit. She was practiced enough from her time with Mistress that she could do a passable job. Certainly the soft sighs of the woman above her suggested it was working."
        "To steady herself, she gripped the heels on her shoes. At least now they had some practical purpose. The other woman had one hand on the wall to steady herself."
        femorc "Ya musta been a slave. Musta. Ain’t no new pussy sucker got dis kinda skill."
        "Alexia moaned out into the green snatch in front of her and then went right back to work. Even as degrading and stressful as the situation was, there was still something about the words that had an effect on her. They were shameful. They were hot."
        "The sensations from the phalli didn’t help keep her calm. Her hips squirmed and bucked against them, as if they were attached to a man she was riding. The tempo of her tongue almost sped or slowed to the rhythm of the vibration."
        "A flow of female cum poured over her lips, dribbling down her chin and all the way down to her breasts. If any got low enough down, it might mix with the steady drip of her own wetness down the side of her leg."
        femorc "Dat's right take it. Take it. Ya little slut. Use dat fuckin’ mouth o’ urs."
        "Suddenly she grabbed Alexia’s head and jammed it harder into her crotch. Alexia gasped for air, but found no relief. So instead she threw herself deeper into the task, head twisting and shoving inward to help with the efforts to lap it all."
        "Her head grew fuzzy and white. That always seemed to happen now when she was overwhelmed by another woman’s scent."
        femorc "Take it like ya love it."
        "The other woman’s hips slammed into Alexia’s face. Her juices were everywhere. Alexia could only moan weakly into the orcess’ mons."
        femorc "Take it like...you're a little harlot who underestimated her own abilities. Who put herself down when she didn’t deserve it."
        "Alexia's eyes shot open. Did she hear that right?"
        femorc "Take it like a woman coming to realize her Mistress was right the entire time and she should have believed her."
        "Alexia put her hands to the Guardswoman’s thighs, and used the leverage to wrest herself free of the woman’s grasp."
        scene cg974 with fade
        pause 3
        "She looked up to see a face smirking down on her...and then the face shifted into the appearance of another person entirely..."
        scene bg14 with fade
        show alexia necklace naked shocked at midleft with dissolve
        
        
    "Stand her ground.":
       $ released_fix_rollback()
       $ femorcSeduced = False
       show alexia necklace naked at edgeleft with dissolve
       al "No."
       "Alexia shook her head. There was no way she could do it. Even with all of the...the tension from what had happened already. Whether it was a sense of dignity or whether it was Rowan, she couldn’t take that final plunge."
       "With some effort, she steadied herself to her feet and looked the Orcess in the eyes."
       al "I am an...an honored guest of Lady Jezera. What you have...oh...what you have s-seen here is nothing. If you don’t...oooh...want Jezera to be angry at you, you will f-f-forget you ever saw this."
       "The Orcess tilted her head to the side."
       femorc "Ya don’t look like a guest o’ da mistress."
       al "Looks can..can be deceiving. Do you want to bet your, er, life on it?"
       "A moment of silence passed. The only sound was the faint movement of the insertions inside her body...making it all the more difficult to maintain her composure. But, she couldn’t let herself show further weakness."
       femorc "Hrmm."
       "Suddenly, the guardswoman started to clap."
       femorc "I thought you’d attempt to be more seductive, but invoking the lady of the castle wasn’t a bad idea."
       femorc "There’d be no way for her to check, of course. But, were it so easy to escape with vague references to a higher authority, it would work more often, no?"
       femorc "Still, you deserve points for the effort! Not bad."
       show alexia necklace naked shocked at edgeleft with dissolve
       "Alexia blinked twice."
       al "Wha-"
       "Before she could get out another word, the image in front of her began to shift. In moments the smiling woman in front of her was no longer an orc…"

show jezera happy at midright with dissolve

al "Mistress Jezera!"

"Alexia looked around the hallway frantically. But, the purple skinned body in front of her didn’t vanish. She was really there."

al "How...Why…."

if femorcSeduced == True:
    "She brought one hand to her aching jaw and worked it slowly. With some effort she managed to work her way back up to her feet. An effort the heels didn’t make easier."
    
"Jezera smiled reassuringly and took Alexia’s hand to help her keep her footing."

show alexia necklace naked at midleft  with dissolve

je "Come now darling, did you actually think I'd leave you naked and terrified in a towerful of guards? That I'd so recklessly risk knowledge of our secret activities getting out?"
je "Tsk tsk. I really hoped you’d think better of me than that by now."

"She turned to the wall in front of her. She gave a wave of her hand, coated in blue magical tendrils. A shadow appeared on the wall, moving as if a person were there. Jezera repeated the gesture and the shadow vanished."

je "All illusions. The guards outside the bedroom. The ones on the stairs outside the armoury. The spire is truly uninhabited."
je "The insertions and their various activities were also me, of course. I made a little...game of trying to figure out the exact most devious time to turn them on."

"To emphasize her point, she snapped her fingers and the phalli came to a dead halt."

je "As for this latest exertion, well...I wanted to see how far you’d go."

"Alexia opened her mouth to speak but words didn’t come out. It took time for her brain to process what was being said. A task made monumentally easier by the reduction in stimulation."

al "I...I can't believe it. It’s…"
al "I was shaking. I was just shaking, the whole time. I thought I would be discovered like this. I didn't know what to do."

je "I know, darling. I know."

al "All I could do was go on instinct. I haven’t been so terrified in a long time. My heart was beating so fast it was as if it was going to burst from my chest."

"Jezera shifted from foot to foot not truly showing a reaction to what Alexia said. When she finished, Jezera cupped Alexia’s chin delicately with the tips of her fingers."

je "And yet..."
je "Look down by your feet. Do you see something?"

"Jezera guided Alexia’s glance down to the spot on the floor where the figure had slipped out of Alexia’s hand."

je "Proof that despite all your protestations that you accepted the wisdom of my lessons. "
je "A lesser woman would have buckled beneath the pressure of being alone in a dangerous space. But, you kept composure, remembered my lessons, and completed the task."
je "You've shown yourself a natural at infiltration...and shown yourself in need of a reward."

"She directed Alexia’s face back to meet hers. Alexia had more she wanted to get out. Questions. Accusations. A thousand mixed emotions."
"And yet, she said something else."

al "A reward? What..what kind of reward?"

show alexia necklace naked aroused at midleft  with dissolve

"Jezera snapped and the phalli roared back to life at full force. Alexia’s legs toppled beneath her and she fell to the floor, moaning and thrashing. The vibrations were so strong that they pounded deep at her core."

je "The sort of reward I give a girl who's done a {i}very{/i} good job."
je "Try to hold yourself together though, darling. This is just the start…"

scene cg975 with fade
show alexia necklace naked aroused behind cg975
show jezera naked happy behind cg975
pause 3

al "Ha...Ha...Ha…"

"Alexia’s breath came out in a ragged pant at the exact same tempo as the Strap-On Cock thrusting inside her." 
"Jezera had positioned her on all fours on her bed. In her words, she wanted to “take her the way Rowan would”. But, in this case, that certainly didn’t mean gentle. "
"The glass phallus was greater in girth than any human man could be. Jezera seemed to relish the sound it made when she worked it all the way inside Alexia’s body. Compared to it, the size of the insertions from before had been nothing."

al "Ha...ah…."

"A strange awareness had overtaken her. Jezera’s nails digging into her hips. The sweat running down her brow. The sploshing sound each time the Strap-On savaged her. All of it was so much more vivid and alive."
"She bit down on the bed sheets, to try to take control of herself. But, her body was running on pure sensation now."
"But, her mouth opened once more in another cry as yet another peak took her. A violent shake ran up and down her spine. Her thighs grew still damper."
"How many times had it been? Jezera had made her cum so many times now. Each one robbed a little more strength from her arms. Each one had made it slightly harder to speak. She was being consumed by it. And she wanted to be consumed all the more."
"Jezera was at her ear whispering things. Alexia couldn’t even make out what she was saying anymore. At the start, she’d called Alexia a slut. An addict to her strap-on. All of it was so true." 
"Even if she couldn’t hear these new words, she knew they were true too. The desperate way she pumped her hips back against Jezera’s phallic idol was all the proof she needed."
"Her Mistress drew a hand to the top of her back, and slowly ran her nails down the length of it. Alexia cried out. The talons drew their way down slowly and methodically. The pain of it was impossible to tell apart from the pleasure of the fake-cock inside her. "
"They became one in her mind."
"As quickly as the previous one had come, another orgasm came bubbling under the surface. Everything Jezera did raised the pressure. Every pump of her Mistresses hips pushed her closer to that edge."

al "...wh..ait…"
al "...wait…"

"Suddenly, it all came to a halt. She whimpered involuntarily. Her hips were still rolling, as if outside her command."

je "I haven’t totally broken you yet, I hope?"

"Jezera giggled. Alexia peered over her shoulder with droopy eyes. Jezera’s body was sweaty with exertion and her cheeks were red with desire. But, otherwise she maintained her normal composure."

al "I...you face…"

je "Huh?"

al "I...wanna...look into your..e-eyes…"

"Jezera smiled softly."

je "Of course, Dove. Whatever you desire."

scene cg976 with fade
show alexia necklace naked aroused behind cg976
show jezera naked happy behind cg976
pause 3

"Her Mistress skillfully eased her into a position atop her lap. Alexia sighed as she sank back down on the fake cock. Her sex was so abused and the strap-on so lubricated that it posed no challenge." 
"The natural impulse of her exhausted body was to make her eyes flutter. But, Alexia threw the last of her strength into keeping them open. To look Jezera in the eyes."

al "You never...never left? T-the entire time? You never left?"

je "The entire time. Every moment. I was there shadowing you and making sure you weren’t pushed further than you could handle."

"Alexia felt strong soft hands wrapped around her back. Feminine finger tips felt along the painful ridges of the new claw marks. Her other hand went to Alexia’s shoulder and pushed downward." 
"This time, her eyes slammed shut. Jezera’s insertion was so deep inside of her now. That last little bit of strength had faded. Jezera pushed her to move and her body followed along."
"The most perfect pair of lips went to her ear."

je "Cum."

"And Alexia did. Then, she lost her sense of place and the world...."

jump jezCorVisitAftercare

################################################################################

label jezCorVisitAftercare:
    
#aftercareCG
scene cg610 with fade
show jezera naked happy behind cg610
show alexia slave happy behind cg610

"She opened her eyes, to find that the situation had changed. She was now curled up and pressed to Jezera’s body. Soft feminine arms wrapped around her. She was being held in the way she’d imagined Rowan would hold her during the years of his absence."
"Alexia whimpered softly and pressed herself into the warm touch."

je "Shhh. Shhh…You did good today, you were a good girl."

al "Mmm..."

if jezCorVisits == 1:
    "Her back arched softly. She wasn't sure if she should recoil or not. Her mind was racing. Was this really okay? Being in this position? Being called a good girl by this woman…"
    "...a good girl..."

if jezCorVisits == 2:
    "Her back arched. She was still hesitant but didn’t recoil. Her mind was racing. As her mind returned to her, so did her uneasiness. But, it was hard to deny that there was a certain magic to hearing it."
    "...Hearing she was a good girl..."

else:
    "Her back arched. After a stressful training session there was nothing better than Jezera’s encouraging reminders. What had once been a source of some misgiving had almost entirely faded, save for a lingering sense of wrongness."
    "...She was growing to like being a good girl.."


"Alexia’s eyes drifted closed once more. Best, not to think about it. Best not to think at all."

if jezCorVisitScene == "facesitting":
    "Yet, even without trying to think about it, her mind went backwards. To the darkness. To the smell and taste overwhelming her senses. The desperation…"
    je "You’re starting to squirm again. Are you sure you can even handle another round?"
    je "It would be a shame if I broke you."
    "Alexia shuddered slightly. She wasn’t sure if that was teasing, a threat, or something in between."
    al "N-n no. I’m content. Even a bit w-worn out."
    je "If you insist, my dear. We will go at a pace that you can handle."
    "Alexia let herself smile this time."

if jezCorVisitScene == "dancing":
    "She subtly ran her hands over her wrists, now free from the bands. It had been strange, being so completely controlled. Not unpleasant, but definitely strange. Not something she would choose to do often, of course…"
    je "Thinking about it?"
    al "Yeah."
    "She smiled softly to herself. While she’d remember everything she learned about dancing tonight. That memory would be the most vivid."

if jezCorVisitScene == "infiltration":
    "Her hand danced to her abdomen. Everything beneath her waist was sore. Her ankles were almost more sore than her hips. Almost."
    je "Starting to think about the test?"
    al "Yeah…"
    al "At first I was doing it just because I had to. But, at some point I think I wanted to find it. If I did then I’d prove the hopes you’ve placed on me are well deserved."
    "Jezera reached to the side table and held the figure of herself aloft."
    je "Oh, I know I’m right. Even if you’d failed, I would have simply resolved to come up with an even more ingenious test to prove it."
    "Alexia shivered softly and squirmed into Jezera’s arms."
    al "I shudder to think of what kind of more elaborate event you would have come up with them."
    je "Shudder with fear? Or with something else?"
    "Alexia didn’t answer that."

"Alexia sighed. She felt like she was floating on a cloud. It made everything so fuzzy."
"She felt a pair of lips meet her own. Jezera’s mouth seeking hers to use. Alexia didn’t mind. She eagerly joined in, letting her mouth open wider to give the demoness more room to explore."
"How long did she spend kissing her? Time lost its meaning and her world shrunk to the single point of lips locked with lips. All she felt was the disappointment welling up from below as Jezera retreated backwards."

je "Well now, it seems we’ve had our fun. But, a promise is a promise. It’s time to return you to your husband, safe and sound."
je "If not a little...enlightened."

"Alexia blushed. Rowan..."

if jezCorVisits == 1:
    al "This is all still so new to me…"
    al "I don’t even know what to say…"
    "Jezera replaced the kiss with a finger, pressing it to Alexia’s lips to silence her."
    je "You don’t have to say anything at all, love. This was more about feeling then speaking, as I’m sure you’ve noticed. You will process all of this more in time."
    je "Perhaps even ask for more."
    "Jezera giggled. Alexia still didn’t know what to say. But, perhaps she wasn’t supposed to know?"

if jezCorVisits == 2:
    al "I still don’t even know what to say. All of this is so new still."
    "Jezera replaced the kiss with a finger, pressing it to Alexia’s lips to silence her."
    je "Put it into a word, love. An idea can be difficult, ephemeral things. Slipping through your fingers."
    je "One word."
    "Alexia searched herself. What could capture the strange excitement? The gnawing tension? The pleasure?"
    al "Thrill."
    "Jezera gave her a reassuring smile."
    je "A good word, Pet. What is life without thrills?"

else:
    al "If only I could stay. Surely, Rowan can wait for another few hours yet?"
    "Jezera replaced the kiss with a finger, pressing it to Alexia’s lips to silence her."
    je "Growing addicted to the pleasure, love? Be careful. The problem with addicts is that they tend to make poor choices?"
    al "True probably. Which is why I keep coming back here, at this point."
    je "Poor choices?"
    "The demoness laughed."
    je "I don’t know about that, Dove. Does coming for our little visits really seem like such a poor choice to you?"
    "Alexia went silent for a moment. Then she smiled softly."
    al "So what do you have planned for next time, Mistress?"
    "They both giggled."

scene bg14 with fade
show alexia 2 necklace aroused with dissolve

"Alexia dressed as normal before leaving. The choker was left on Jezera’s nightstand. The demoness even gave her a smack on the ass as she left. Alexia wasn’t able to suppress a moan at that."
"She had to return to her room now. It would not due for her to spend the night in Jezera’s room. People might notice. But, as she left, part of her was left imagining...what would happen if she did?"

$ change_actor_num_flag('alexia', 'jezera_influence', 3)
$ change_corruption_actor('alexia', +5)
$ alexiaJezeraSex =+ 1

return

