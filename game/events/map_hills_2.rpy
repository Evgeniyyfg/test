# random map events that happen on hills
init python:

    #Iron Seam
    event('iron_seam', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Landslide
    event('landslide', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('clash_of_goblin_and_knight', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('talkative_traders', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('immortal', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('the_lost_tribes', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)

label iron_seam:
#Iron Seam
#No requirements

scene bg43 with fade

"A distant cliff-side catching the sunlight drew Rowan's eye as he traversed the mountainous territory. He picked his way along a valley to take a closer look."
"There was definitely something up there, on that wild, sheer cliff face - a wide stripe of grey, gently glittering rock. Iron? There were surely untapped seams to be found in this difficult and distant terrain."
"Taking a closer look, however, was going to be neither easy nor safe. Rowan pondered if it was worth the effort."

menu:
    "Climb the cliff.":
        $ released_fix_rollback()
        #climb check dc12
        $ event_tmp['climb_roll'] = roll_skill('climb')[0]

        if event_tmp['climb_roll'] < 8:
        #less than 8
            "Rowan put his equipment to one side and set his hands upon the rock, gaze set upon the tantalising glitter above. He had clambered about fifteen feet up the sheer cliff face before a toehold gave way beneath his boot."
            "He half fell, half slid back down, landing heavily upon his ribs with a horrible crack. He clambered back to his feet, cursing."
            "There was no chance of a second attempt with injury clutching his side - whatever the seam was, a traveller more skilled at climbing than he would have to find out."
            #gain 10 xp and 1 wound
            $ add_exp(10)
            $ take_damage(1)
            return
        elif event_tmp['climb_roll'] < 12:
        #8-11
            "Rowan put his equipment to one side and set his hands upon the rock, gaze set upon the tantalising glitter above."
            "The climb was tough, the rock jagged, and his heart almost leapt out of his mouth when he suddenly lost his grip and fell a few feet, jarring his ankle and bloodying his nose against the stone."
            "After he’d spent a few moments taking some long, deep breaths though, he was able to continue."
            #gain 1 wound and continue to reward step
            $ take_damage(1)
        else:
        #pass
            "Rowan put his equipment to one side and set his hands upon the rock, gaze set upon the tantalising glitter above. Using all of his experience, he scaled the sheer cliff face like a lizard up a sun-bleached wall."
            "The gradient became less severe further up, and he was able to stand upon a lip of rock next to the large stripe of discoloured rock, examining it closely."

        #reward step
        $ tmp = dice(5)
        if tmp <= 2:
            $ event_tmp['reward'] = 'Big'
        elif tmp <= 4:
            $ event_tmp['reward'] = 'Average'
        else:
            $ event_tmp['reward'] = 'No reward'

        if event_tmp['reward'] == 'Big':
        #40% chance - Big score
            "His spirits rose as he set a knife to it and heard the telltale 'clink'. Iron! And a concentrated amount of it, by the looks of things; this whole mountainside could well be thick with good quality ore."
            "The only problem was getting at it. He could call in a team to construct some platforms, ramps and pulleys, but it would take time."

            menu:
                "Use orcs.":
                    $ released_fix_rollback()
                    "Rowan summoned a surly pack of orcs and set them to work constructing some wooden scaffolding and rope lifts that would enable them to get at the rich iron seam and bring the ore back down."
                    "It took a tedious amount of time, but eventually the workers had a decent, makeshift system set up and picks were being set to the face. Weary but satisfied, Rowan set out again."
                    #lose 2 move points and 5 morale, gain 20 xp and a medium sized mine
                    $ change_mp(-2)
                    $ change_morale(-5)
                    $ add_exp(20)
                    # add iron/week as for "important mine" #7
                    $ castle.mines += 1
                    $ castle.iron_per_week += mines_defs[7][2]
                    return

                "Use humans.":
                    $ released_fix_rollback()
                    "Rowan followed the valley back down, found a village with men willing to be hired and set them to work constructing some wooden scaffolding and rope lifts that would enable them to get at the rich iron seam and bring the ore back down."
                    "It took a tedious amount of time, but eventually the workers had a decent, makeshift system set up and picks were being set to the face. Weary but satisfied, Rowan set out again."
                    #lose 2 move points and 30 treasury, gain 20 xp and a medium sized mine
                    $ change_mp(-2)
                    $ change_treasury(-30)
                    $ add_exp(20)
                    # add iron/week as for "important mine" #7
                    $ castle.mines += 1
                    $ castle.iron_per_week += mines_defs[7][2]
                    return

                "Decide against it.":
                    $ released_fix_rollback()
                    "There'd be iron mines in terrain far easier to access, Rowan decided, and he had no wish to spend an arduous amount of time and effort setting one up here. Reluctantly he climbed back down the cliff, retrieved his possessions and set off again."
                    #gain 20xp
                    $ add_exp(20)
                    return
        elif event_tmp['reward'] == 'Average':
        #40 chance - Average Score
            "His spirits rose as he set a knife to it and heard the telltale 'clink'. Iron! There wasn't quite as much of it as he had hoped, but there still seemed to be a decent amount here, surely enough to justify establishing a mine."
            "The only problem would be getting at it. He could call in a team to construct some platforms, ramps and pulleys, but it would take time."

            menu:
                "Use orcs.":
                    $ released_fix_rollback()
                    "Rowan summoned a surly pack of orcs and set them to work constructing some wooden scaffolding and rope lifts that would enable them to get at the rich iron seam and bring the ore back down."
                    "It took a tedious amount of time, but eventually the workers had a decent, makeshift system set up and picks were being set to the face. Weary but satisfied, Rowan set out again."
                    #lose 2 move points and 5 morale, gain 20 xp and a small sized mine
                    $ change_mp(-2)
                    $ change_morale(-5)
                    $ add_exp(20)
                    # add iron/week as for "small mine" #6
                    $ castle.mines += 1
                    $ castle.iron_per_week += mines_defs[6][2]
                    return

                "Use humans.":
                    $ released_fix_rollback()
                    "Rowan followed the valley back down, found a village with men willing to be hired and set them to work constructing some wooden scaffolding and rope lifts that would enable them to get at the rich iron seam and bring the ore back down."
                    "It took a tedious amount of time, but eventually the workers had a decent, makeshift system set up and picks were being set to the face. Weary but satisfied, Rowan set out again."
                    #lose 2 move points and 30 treasury, gain 20 xp and a small sized mine
                    $ change_mp(-2)
                    $ change_treasury(-30)
                    $ add_exp(20)
                    # add iron/week as for "small mine" #6
                    $ castle.mines += 1
                    $ castle.iron_per_week += mines_defs[6][2]
                    return

                "Decide against it.":
                    $ released_fix_rollback()
                    "There'd be better iron mines in terrain far easier to access, Rowan decided, and he had no wish to spend an arduous amount of time and effort setting one up here. Reluctantly he climbed back down the cliff, retrieved his possessions and set off again."
                    #gain 20xp
                    $ add_exp(20)
                    return
        else:
        #20 chance - Fuck you iron
            "Even before he set his knife to it, Rowan knew it would be useless. The blade easily passed through the glitter into crumbling rock. There was iron ore here, but it was merely a poor-quality sheen of the stuff over useless silicate."
            "Rowan clambered back down the cliff-side, retrieved his gear and set out again, attempting to shake off the feeling of being cheated by setting his best foot forward."
            #lose 2 move points, gain 20xp
            $ change_mp(-2)
            $ add_exp(20)
            return


    "Decide against it.":
        $ released_fix_rollback()
        "There'd be iron mines in terrain far easier to access, Rowan decided, and he had no wish to break a leg surveying something that might prove worthless. He secured his pack and set off again."
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label landslide:
#Landslide
#No Requirements

scene bg43 with fade

"The tinkle of falling pebbles. A distant, angry rumble. The warning signs of a landslide sound inconsequential, somebody else's problem. Until, very suddenly, it isn't, and it's not."
"Rowan jerked his head up in time to see the curtain of rock collapse off the mountainside, and the dusty load of boulders tumbling downwards towards him."

#spot check dc12
$ event_tmp['spot check'] = roll_skill('spot')

if event_tmp['spot check'][0] >= 12 or event_tmp['spot check'][1] == 20:
#pass
    "Rowan's highly trained subconscious had noticed the danger, however, even when the rest of his mind had been wandering."
    "Immediately he threw himself backwards, narrowly avoiding being crushed by one of the larger boulders that came crashing down, obliterating the path in front of him in a cloud of dust and debris."
    "It took him a while to stop coughing and to still his beating heart, but Rowan was otherwise unharmed. Counting his blessings and keeping a closer eye on the terrain above him, he picked out a new way forward."
    #gain 20xp
    $ add_exp(20)
    return
else:
#fail
    #escape artist check dc12
    $ event_tmp['escape artist check'] = roll_skill('escape')
    if event_tmp['escape artist check'][0] >= 12 or event_tmp['escape artist check'][1] == 20:
    #pass
        "Rowan threw his agile body into action, flinging himself beneath a lip of rock to avoid the larger weight of rocks. They flung up clouds of blinding dust as they thundered and span down in front of him, obliterating the path he had been standing on."
        "He heard the groan of rock giving above him and he swiftly rolled to one side, chest heaving as he watched the lip collapse under the weight of the last boulder that came thudding down."
        "It took him a while to stop coughing and to still his beating heart, but Rowan was otherwise unharmed. Counting his blessings and keeping a closer eye on the terrain above him, he picked out a new way forward."
        #gain 20xp
        $ add_exp(20)
        return
    elif (8 <= event_tmp['escape artist check'][0] <= 11):
    #8-11
        "Rowan threw his agile body into action, flinging himself beneath a lip of rock to avoid the larger weight of rocks. They flung up clouds of blinding dust as they thundered and span down in front of him, obliterating the path he had been standing on."
        "He heard the groan of rock giving above him, and although he tried to roll to one side he sprained his shoulder as the lip collapsed under the weight of the last boulder that came thudding down."
        "Clutching his arm and coughing, Rowan sat himself down and waited until his heart stopped trying to beat its way out of his chest. Pain clutched his shoulder and he found he could barely move it."
        "But, considering the devastation around him, things could have been a lot worse. Counting his blessings and keeping a closer eye on the terrain above him, he picked out a new way forward."
        #gain 10xp and 1 wound
        $ add_exp(10)
        $ take_damage(1)
        return
    else:
    #fail
        "Rowan froze for one fatal moment, and was enveloped in the falling debris. A brick-sized rock smashed him on the side of the head, stunning him and sending him sprawling to the deck."
        "This turned out to be a blessing in disguise - the larger boulders thudded and spun over his prone body, carried over by a lip of rock. Another chunk the size of a melon thumped into his back though, hard enough to break a rib."
        "After the landslide had subsided and at least some of the world had swum back into focus, a dust-coated Rowan dragged himself to his feet. He groaned and coughed, trying not to be sick."
        "Pain hammered through him, he felt that he could barely move, and yet he knew that he must. Clutching his side, he limped onwards."
        #gain 5 xp and 2 wounds
        $ add_exp(5)
        $ take_damage(2)
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label clash_of_goblin_and_knight:
    
scene bg43 with fade

"The squawking of ravens and the reek of decay filled the air atop a hill, which had been the site of a recent battle.  Rowan sat on a rock overlooking the scene with a chill in his stomach."
"A couple of hours ago he'd seen the circling birds.  An hour ago he'd arrived.  Now it was time to consider the evidence and try to explain why there were all these bodies lying about the ruins of an old watchtower."
"Men and women bearing the sigil of Rosaria plus several goblins were scattered about, wearing only undergarments and grievous wounds.  A battlefield where goblins and knights had killed one another."
"The nearby torn tents and fire pits suggested that his countrymen had been camping here, only to have been ambushed by goblins.  The winner was self-evident, as everything of value had been taken and the bodies left to rot."
"What had these knights been doing up here?  Were they hunting the people who ultimately killed them?  Looking for something else?"
"There was simply no way to find out now.  No written instructions or orders were to be found on the bodies or camp remains.  All that could be gleaned was speculation at best."
"These sorts of battles were not unheard of, but rarely did they target such a large group of well-trained warriors."
"All that Rowan could do now was make a note of it and continue his explorations.  Even burying the corpses was a dignity that he had neither the time nor the tools to grant."

$ add_exp(5)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label talkative_traders:
    
scene bg43 with fade
show rowan necklace neutral at midleft with dissolve

"It was sundown. Rowan knew that there was little more he could safely travel tonight. The hillsides were often alive with wolves and predators in the night time."
"He was so far out from civilization that it came as some surprise that there was someone else approaching him along the way. A large wagon drawn by two horses."
"Rowan approached wearily. Cloak over his head to obscure himself and a hand on his sword. But, he eased slightly when he saw a goblin directing the horses. These were caravan traders."
"He approached, albeit still with some caution. He didn’t recognize this goblin as one of Cla-Min’s brood." 

ro "Good evening friend."

rancou "And a good evening to you. I apologize that it’s getting dark. If you’d like I can find somewhere else to set up camp?"

"Rowan gave him a soft smile. The goblin’s remark seemed infused with a lifetime of the way that humans were likely to treat his kind."

ro "I would be honoured to share a fire with you. That is if you’re equally willing to share a fire with a human?"

$ rancou_name = "Ran-Cou"

rancou "I think I can manage that. My name is Ran-Cou."

ro "A pleasure to make your acquaintance."

"The goblin merchant continued to be apologetic, even as they set up a small campfire. But, every time, Rowan waved him off."
"Rowan brought the kindling to a strong and warm fire. They sat down together and settled in for the night’s conversation. Rowan planned to ask about the man’s caravan and it’s allegiance. Whether they were friendly with the Cla clan. Goblin politics was a new and vital topic."
"But, fate had a different conversation in store."

rancou "Do not worry about food. I will have my wife prepare a meal. She’s getting to be a good cook. Not at first though. Spoiled thing had to be taught."
rancou "Woman! Woman, come out here!"

"The woman who came from the tent was no goblin. Instead, it was a comely human with sparkling gold hair. She wore a skimpy vest and ragged skirt, that exposed much of her body. Yet, neither that nor her generally dirty appearance disguised her natural beauty."
"In her arms, she carried a bundle. It should not have been a surprise to Rowan, that it was a goblin infant, but something about the situation made that detail stand out."

rancou "There you are. We need to prepare portions for one extra tonight. We have a guest."

zelda "We do? Who is he?"

"The woman looked to him, blue eyes searching wide. Her voice was soft but surprisingly proper for her appearance. At once, Rowan knew she was castle born."
"Apparently, she overstepped her bounds. Her husband gave her a firm, but not especially hard, smack on the rear."

zelda "Eek!"

rancou "Questions are for when food is on the fire."

zelda "Right away."

"Ran-Cou turned back to Rowan, who was still slack-jawed from the display."

rancou "My new wife, Zelda. Hehe. I find that she thrives when you keep a firm hand with her."

$ zelda_name = "Zelda"

ro "A strange relationship you have."

rancou "A goblin and a human?"

"Rowan shook his head. Of course, that part he was curious about as well. But, something else from that interaction stood out to him."

ro "As I’ve said. I’ve met goblins before. I did not know you privileged the male sex so highly. I’ve met Goblin matriarchs and my understanding was that there is no dominant status for goblin males."

rancou "That’s relationships between goblins though."

"He nudged Rowan in the ribs."

rancou "Besides, technically speaking this girl is still my servant. I think she likes it that way too."

"Zelda blushed but didn’t look away from the cookfire."

rancou "Zelda here was given to me by my clan as a servant to take on the road. Didn’t quite intend to knock her up along the way."
rancou "My Papi raised a laugh when he found out about that part, let me tell ya. Especially considering how haughty she was when they first met."

"His answers just begged more questions. Rowan leaned slightly forward. For the first time, he noticed a slight swell in the woman’s stomach, unhidden by her skimpy outfit. Was she pregnant with Ran-Cou’s second child?"

ro "It’s not common for a human woman to end up a servant to a goblin either. I don’t think I’ve ever seen that before."

rancou "It ain’t. But, my Zelda’s not a common girl."
rancou "Woman, why don’t you tell him about it?"

"Zelda sighed."

zelda "You know the story is embarrassing, darling…"

rancou "Ha. That’s all the more encouragement to make you tell it!"

zelda "Fine. Fine."
zelda "The truth is, only a year back I was a knight. Formerly landed, but that was lost."

"If Rowan’s eyeballs could pop out of their sockets, they would have. Castle born was one thing. But, how did a knight end up in such a predicament?"

zelda "A knight of the western vassals of Prothea. You have know of the traitor, Zerias, no? The leader of the attackers at the seige of Karst."

"Rowan leaned back and tried not to strike a smug face."

ro "I’ve heard the name once or twice."

zelda "My father was sworn to him. A loyal supporter, no less. And when his host was shattered in the flight from Karst, my father died to protect him."
zelda "That was the end of my house’s fortunes. As eldest daughter, I inherited the title and the estate. I’d been training for it."
zelda "Our new liege demanded heavy tribune as recompense. When I sought to replay it, I didn’t find any gold. Just stacks of secret debt notes."
zelda "And no human money lender would aid us. We were a treacherous house. I sold the entire estate, top to bottom, but it was not enough."

rancou "That’s where we came in…"

"He reached out and wrapped a short stubby arm around his wife’s waist. Despite her larger form, she yielded to the touch with a sigh."

rancou "Papi offered her a fair price. As much as could barter for with whatever crap she still had."
rancou "But, we wanted a little more for the deal. Her father had tried to stiff us once, actually. Everyone thinks they can stiff the goblin. We’d have been well within our rights to tell her to shove it. But, Papi had a better idea. Why not take her a trophy?"

ro "As a slave?"

rancou "Goblins? Slaving humans? The price of that is death in human lands. No sirree."
rancou "But, a nice binding indenture contract. Five years of enforced servitude and labor? Now, that’s just fair dealmaking between responsible parties."
rancou "Ain’t nothing wrong with a freely negotiated contract, hehe."
rancou "So, when I went out on my own to do my rounds, Papi handed her as a gift. A pretty well bred servant with legal standing in the human lands. Real generous of him."

ro "You still haven’t explained how you ended up married, though?"

zelda "Sir, do you really think I’d have taken a deal like that without some idea of the...other...kind of uses such creatures might use me for?"

"She shruged to herself and laughs."

zelda "I guess chaos runs in the family. Not quite in the way father had intended..."

"The story continued from there. Zelda spoke about her entrance into the Ran household and setting off on the journey with Ran-Cou. Her husband liberally interjected in the story, and egged her on to reveal more and more details."
"Rowan suspected that this was more for Zelda’s benefit than his. Every time he made Zelda divulge something new, Ran-Cou looked to her for a reaction."

if avatar.corruption > 60:
    "Rowan grinned to himself. It was sadistic but in a fun and charming way. Something he could see himself doing in such a strange power dynamic."

"Not that Rowan made no use of the time. When he could, he asked for details about the clan and it’s trade practices. They were not rivals of the Cla clan, at least insofar as any set of goblin clans were not rivals. But, they were not as prosperous either."

rancou "Come on, woman. Get to the good stuff. The tent. The tent."

zelda "Are you sure? Isn’t that a little intimate?"

rancou "And?"

menu:
    "Ask to keep it chaste.":
        $ released_fix_rollback()
        "Rowan gave the goblin a friendly slap on the back. This was a step too far, especially with a new face."
        ro "How about you skip this part of the story, huh? Some things are better left unsaid."
        rancou "You sure? It’s a good story."
        ro "Not tonight, I’m afraid."
        "Ran-Cou laughed and turned back to his wife."
        rancou "Ya hear that, woman? Got left off easy. Say thanks to your saviour."
        "Zelda raised an eyebrow, then took out plates to serve the meal."
        zelda "Thank you for the help…"
        "Rowan was left not totally sure if what he was hearing from her was gratitude...or disappointment."
        jump rancouEnd
        
    "Listen intently.":
        $ released_fix_rollback()
        pass
        
scene black with fade
show rowan necklace neutral behind black

scene cg947 with fade
pause 2
show cg948 with dissolve
show rowan necklace neutral behind cg948
pause 3

zelda "It was on the tenth night that I knew that I wanted more. Cou has been a perfect gentleman to me, but it just was wrong. He had me wearing these revealing clothes yet never did anything to me."
zelda "I was the one who came to him."
        
ro "Truly?"

rancou "You shoulda seen it. She came practically begging me to fuck her. Ass in the air and everything."


zelda "It’s true. I tried to be subtle and seductive at first. But, I was never good at that. Training in arms doesn’t leave you much in the way of that kind of skill."
zelda "Eventually, I just told him what I wanted, and asked him for it."

show cg949 with dissolve
pause 3

rancou "Begged, more like."

zelda "Y-yes. Begged him for it."

#cg1
scene cg950 with fade
pause 2
show rowan necklace neutral behind cg950
pause 3

zelda "He told me that he wanted me down on all fours. So that’s what I did. It was the first time I ever looked up at him."
zelda "He didn’t, uh. He didn’t waste much time taking me."

rancou "And what did you think of Goblin cock, huh slut?"

zelda "Cou! He can hear us!"

rancou "Say it."

zelda "Uh. I didn’t expect it to be so big. Or to feel so good. He just kept pounding me and pounding me and it felt like, ugh."
zelda "There are no words for it."

rancou "You were a loud little minx, wasn’t you?"

zelda "Yeah. I had some problems controlling my voice..."

rancou "And what were you saying?"

zelda "I have to tell that part too?"

rancou "All of it."

zelda "I said...I just kept saying “Ruin me” over and over again. I guess, I decided that for a knight of honour, being fucked by a goblin was the end of the line."
zelda "I must have been pretty loud about it. In the morning, my voice was hoarse. How many people might have heard me screaming that?"
zelda " It just kept going and going. It was like I was losing my mind. I’d never been...taken...before. That’s what it felt like. Being taken."
zelda "Do I need to keep going?"

rancou "Yes."
 
zelda "I must have cum so many times. I don’t know. I lost track after awhile. I’d never even had an orgasm before that."

rancou "I could feel it too. No doubt. This bitch was shaking and squirting. I had a sleeping rug set up and she damn near ruined it."

#cg2
show cg951 with sshake
show cg951 with sshake
scene cg952 with flash
pause 3

zelda "By the time it was, over I knew I crossed a turning point. I was lying face down on the ground with goblin cum leaking out of me."
zelda "Sir Zelda met her end that night. I knew I’d be back the following day for more. And the day after that."
zelda "I belonged to him."
zelda "There was no question of what the effect of so many days of it would be. For all I know, he, little one was conceived on that first try."

scene black with fade
show rowan necklace neutral behind black

"By the time the story way over, Rowan had but one question."

if avatar.corruption < 31:
    ro "W-why did you tell me all of that? You could have warned me before going that in depth."
    
elif avatar.corruption > 60:
    ro "A good story. And one that I bet you have told to many others. Am I right?"

else:
    ro "Something tells me that the story wasn’t mostly for my benefit, was it?"

"The goblin and his wife exchanged a mischievous glance but didn’t actually give him a straight answer."

scene bg43 with fade
show rowan necklace neutral at midleft with dissolve

label rancouEnd:

"After storytime came dinner. True to the goblin’s word, Zelda proved to be a competent, albeit not spectacular cook. When the meal was done, Zelda begged off to take care of the newborn. Before she left, Rowan wanted to ask her a question."

ro "Are you happy with this? Truly? There’s still use in the world for women who have been trained in arms."

zelda "Your question speaks volumes to your concern. Truly, I thank you."
zelda "But, even if this was not the path I planned for myself…"
zelda "It’s one I can live with. I think."

"She gave him a smile then vanished into the tent."
"Rowan and Ran-Cou spent much of the night discussing more business-oriented questions. The Ran clan was noted for acquisitions and finance. Both of use to Bloodmeen."
"The only real problem was Cla-Min. She was too valuable as an ally by a country mile to unseat. But, she’d hardly let another clan muscle into her territory. By night’s end, Rowan had constructed a plan that would have the Cla’s act as intermediaries for any trade."
"By the end, Rowan felt he had a preliminary deal that even Cla-Min might be willing to accede to. It would line more gold into her pockets than anyone else. "
"In the morning, Ran-Cou and his small wagon went off in the other direction. He was heading back to the western dependencies of Prothea to relay the deal to his kinsmen. With him went his wife and son. The strange family they’d made together."

#TODO - slight income bump?
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label immortal:

scene bg43 with fade

"Rowan found a strange landmark atop a hill. At the very top there was a stone, but the stone was carved almost in the visage of a person."
"Yet, there were no villages nearby or any purpose to it."
"He looked in closer, and only found more proof that this was no accidental find. The face was clearly shaped with fine detail. Yet, most of it had weathered down to a state of being unrecognizable by time. "
"The longer he examined it, the more he was certain. This had once been in the shape of a specific person. A village hero? A lover?"
"The statue was meant to capture the visage of a person, and yet this was all that remained." 
"Thankfully, the mystery of why this statue was in the middle of nowhere was soon answered. He went down to the valley and found weathered stone amidst the dirt. With some light digging, he was able to excavate what might have been a village once."

if avatar.corruption < 60:
    "Rowan took a few trinkets and whatever gold he could find from the village site. But, he made sure to tread carefully and disturb as little as he could."
    "It was the least he could do to honour the memory of that person who was no longer remembered."
    
else:
    "Rowan made no bones about taking what he could from the site. Despite the passage of time, there were still a few trinkets of value to be found. Though, not so many that stripping it took long."
    "Rowan took no computation about it. Had the maker of the statue been here, they would have wanted Rowan to have as much as possible."

"Then, Rowan set off on his way. Soon enough, he’d scarcely remember he even had been there."


if avatar.corruption > 60:
    $ change_treasury(20)

else:
    $ change_treasury(10)

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label the_lost_tribes:

scene bg43 with fade

"Rowan trudged through the steep, rocky paths along the mountainside, careful not to veer too close to the edge lest he fall into the sharp ravine below. There was still some time to his journey and he would rather not spend it tumbling to an early death."
"A low growl caught his attention from the cliffs at his side and before he knew it, a sword came crashing down on his head."
"With expert precision, Rowan unsheathed his own weapon and blocked the surprise attack, forcing his assailant backward."
"An orcish warrior rolled back onto his heels but kept his stance, wielding his weapon with a strong but slender hand. The male orc was strangely handsome, with white hair softer than snow that brushed over the side of his face and nearly matched his ghostly greyish skin."

if rowanGaySex > 2:
    "Rowan didn’t often find himself saying this, but he sure was a morsel for an orc."

show rowan necklace angry at midleft with dissolve

keth "What need have you in our mountain?"

"Even his speech was different, delivering more intelligence than Rowan expected. Rowan was taken aback, used to having met several grotesqueries among the orcish race." 
"He held himself upright and stared at the orc head on, unwavering in his confidence."

ro "Simply passing through."

"The orc scoffed. Apparently Rowan was not the first to use that excuse."

keth "Doubt it."

"The orc attacked again, but despite his strength and experience, Rowan was faster. He disarmed the orc in two swift movements and the orc's sword clanked against the rocks as it tumbled down, echoing across the mountain." 
"The orc gritted his teeth and stared at Rowan, waiting for the next strike that would end his life. It did not come."


if avatar.corruption < 31:
    show rowan necklace neutral at midleft with dissolve
    "Rowan offered his hand instead." 
    ro "You needn't look so angry, friend. I have no intention of harming you. I'm just trying to find a spot to camp for the night."
    "The orc surveyed Rowan's hand, searching for a trick that was not there, before reluctantly taking it. Rowan helped him to his feet."

else:
    show rowan necklace neutral at midleft with dissolve
    "Rowan simply sheathed his blade. There was a story here, and Rowan intended to hear it."
    ro "Your style was sloppy. But, you will not die for it today. You interrupted me in my search for a spot to camp for the night."
    "The orc rose slowly to his feet."
    
keth "What is it you want then? What purpose do you have on our mountain?"

if avatar.corruption < 31:
    ro "To know who've I've offended so badly would be a nice start. My name is Rowan."
    "Rowan offered his hand again, but the orc did not take it this time. "
    
else:
    ro "Information for a start. I am Rowan. To whom am I speaking?"
    
$ ketharName = "Kethar"

keth "Kethar. You're looking for a camp, yes? Follow me."

scene black with fade

"Kethar and Rowan weaved through the narrow path of the mountainside until they came across a small orcish camp set up along a plateau." 
"There were less than a dozen orcs including Kethar, each of them more slender and pale than the last. Rowan cocked an eyebrow. This was not the lot of giant green monstrosities that was common to his experience with orcs. "
"Kethar noticed him staring as the other orcs eyed Rowan with suspicion, reluctantly making room for him beside the campfire."

scene bg43 with fade
show rowan necklace neutral at midleft with dissolve

keth "We are what you might call the runt of the litter. We've been exiled from our tribes, so we band together and form our own council."

"Despite the positive outlook Kethar seemed to have, there was shame in his eyes. Rowan knew firsthand how seriously the orcs took their position among their tribes, so to be exiled… It was a great shame indeed."

ro "You lead these men, then?"

keth "Yes."

"Kethar and Rowan sat down around the fire while the rest of the small band of men passed around bowls of stew. Rowan knew better than to ask of its contents and simply enjoyed the warmth the food provided him."
"Once everyone had their fair share, another orc spoke up from across the fire."

runto "He was 'spose to lead 'em all. Not just us, y'know."

ro "What happened?"

"Kethar looked reluctant to answer, but he pushed through, downplaying the events as much as he could."

keth "There is a trial in my tribe to test a leader's abilities. I did not meet the requirements."

"It was a nice way of saying he failed. Kethar looked into the crisp flames of their campfire and a new determination burned in his gaze."

keth "But, with some more training, I intend to come back and take my rightful place as leader. They cannot avoid me forever."

"Kethar reached out with a stick and stoked the fire, sending embers up into the air. The others around him ate silently, and Rowan guessed this was not the first time Kethar made such a proclamation."
"As Rowan surveyed the camp, he had little faith in Kethar's ability to lead this tiny troupe, much less an entire army of orcs. Their food supply was greatly dwindling and the rest of their supplies looked worn through and ready to break at any given moment."
"Unless someone stepped in soon, they would surely die on this mountain. Someone with a use for orcish fighters."
"On one hand, perhaps it wouldn't be so bad to leave them. Andras had no idea this little band of orcs existed, so there would be no one to reprimand him for leaving them behind. Bloodmeen would suffer."

if avatar.corruption < 31:
    "Surely, if he brought them back , it would add more fuel to Bloodmeen’s war machine. And alone here, he was uniquely positioned to get away with it."

"...But so would these orcs, dying out here in the cold from either starvation or other natural elements. Could Rowan live with himself if he did that?"

menu:
    "Leave them to die.":
        $ released_fix_rollback()
        if avatar.corruption < 61:
            $ change_base_stat('g', 5)
            ro "{i}It's for the greater good.{/i}"
            "He could not risk Andras's army growing any larger, even by a band as small as these orcs. If he wanted to keep peace in the world, some sacrifices had to be made."
            if avatar.corruption < 31:
                "That didn't mean he felt any better about it."
        else:
            ro "{i}Andras can suck my dick.{/i}"
            "Rowan still remembered how he’d fallen (quite literally) into Bloodmeen’s service. Just because there were consequences for refusal didn’t mean he was going to help those demon bastards of his own volition."
        scene black with fade
        "He ate in silence with the rest of the quiet group, fully aware that this could be the last time he ever saw them alive, before bidding them goodnight and taking a rest off to the side."
        "He woke up first thing in the morning and left without a word, hoping that he would never see them again."
        return
        
    "Recruit them and increase army size.":
        $ released_fix_rollback()
        $ castle.buildings['barracks'].troops += 5
        "Rowan couldn't bring himself to just leave these men out here to die. Kethar and his group offered a sort of intelligence that he hadn't seen in many orcs, and with any luck, they would prove to be useful both on and off the field."
        "At the very least, Andras would be happy to see more soldiers in his army."
        "So, Rowan gave them the offer, repeating the same spiel he had given many wandering orcs and travellers. Kethar seemed reluctant at first, but peering around his ruddy camp, he knew there were few options left but to accept."
        "Rowan gave him directions to the castle and they bid farewell in the morning. Rowan knew Andras would be pleased with his work, and Kethar's group would not die alone in the mountains. It was a win for everyone."
        return
        
    "Recruit them for Bloodmen in exchange for sexual favors." if avatar.corruption > 30:
        $ released_fix_rollback()
        $ change_base_stat('c', 5)
        $ castle.buildings['barracks'].troops += 5
        $ rowanGaySex += 1
        "Rowan eyed up Kethar and a new idea popped into the back of his mind. Kethar was quite handsome, especially for an orc, and with a slender body like that… Well, Rowan would have no trouble putting him to good use."
        "Finishing off his bowl of soup, Rowan set his bowl aside and the rest of the orcs got up to rest for the night. Kethar began to stand up as well, but Rowan grabbed his arm, pulling him back down."
        ro "Why are you in such a hurry? Come. Sit. You haven't even heard my offer yet."
        keth "Your offer?"
        "Kethar raised a brow in suspicion and eyed Rowan up and down. Rowan could not resist doing the same, enjoying Kethar's nimble physique."
        ro "I have something better than leading a tribe; you know your little party here won't last more than a few weeks at most without help, and I happen to have an army that needs soldiers."
        "Rowan could tell the offer tempted Kethar, but the orc was wary to latch onto his suggestion so easily."
        keth "That sounds… perfect, but you want something in return. What is it?"
        "Rowan supposed Kethar assumed he wanted money or loyalty, but as Rowan eyed him over, his gaze lingering along Kethar's crotch, he could see the wheels slowly turning in the orc's head."
        "Kethar stilled as Rowan leaned closer to him, his hot breath tickling Kethar's skin as he murmured a response in the orc's ear."
        ro "I think you know what I want."
        "Rowan rested his hand on Kethar's thigh, his fingers running up and down the orc's leg. Kethar glanced back at his sleeping men, but whether he was checking to make sure they were asleep or to gauge if this would be worth it, Rowan wasn't sure."
        "Without a word, Kethar stood up and motioned for Rowan to follow. Kethar led the hero a little ways back down the path until they reached a tree that had somehow grown sideways along the mountain's cliff."
        "Rowan admired the strange work of nature for only a moment before Kethar removed his shirt."
        "There wasn't much in terms of clothing for Kethar to begin with, but he removed the heavy pelts and fabric that hid his chest and crotch, hanging them over a hooked tree branch."
        "Rowan noticed Kethar was careful to be quiet as he stripped, but Rowan offered no such accommodation, his belts and fabric making loud clanks as he plopped them into a pile on the ground." 
        "Kethar swallowed hard when he saw Rowan's growing erection poking out in the night air."
        "He looked as though he were going to warn Rowan about keeping silent but thought better of it, instead turning around to bend over and grip the tree."
        "Kethar's skin was so pale that it practically illuminated in the dark, so Rowan had no trouble admiring each slender curve of the man as he stuck his pert ass out for him." 
        scene cg869 with fade
        pause 3
        show rowan necklace naked behind cg869
        "Spitting into his palm, Rowan coated his cock with saliva before easing it into Kethar's waiting asshole. The orc grunted in pain, his nails digging into the tree bark as Rowan eased into him."
        ro "Heh. You're so ready to just {i}take{/i} it. This isn't your first dick, is it?"
        "Rowan gripped the orc's hips and thrusted hard from behind. Kethar panted in response, his legs widening to accommodate Rowan as he pounded into his ass. No, this definitely wasn't his first time, and Rowan felt a surge of desire run through him at the thought."
        "He gripped Kethar's hair hard and yanked his head back to get a good look at his pretty face. The orc's lips were parted, his breath coming out in cold puffs against the night air." 
        "Rowan stuck a finger in his mouth. Then two. Kethar sucked them eagerly, desire lidding his eyes as Rowan fucked his gaping hole. Kethar moaned around Rowan's skin, his tongue darting over and across the fingers as they explored his mouth."
        "Kethar's cock twitched with each hard thrust, precum dripping down his tip and onto the solid ground beneath them. Rowan's own excitement built as he watched Kethar's cock bob in the night air."
        "Rowan removed his hand from the orc's mouth with a wet pop and wrapped his hand around Kethar's girth, pumping up and down. Kethar gasped, struggling to hold down a moan."
        ro "Is this what you needed? One cock in your ass isn't enough for you? You need to get jerked off, too?"
        "Kethar didn't answer, but the flushed look on his face told Rowan everything he needed to know. Rowan bucked against the orc's ass and Kethar jerked his hips feverishly against him, both working to get Rowan off as well as himself."
        "Rowan's wrist flicked as he ran his hand up and down Kethar's throbbing shaft. The orc's ass clenched, tightening pleasantly around Rowan's cock as he neared his climax."
        keth "Fuck… Fuck… Yes, yes, yes, like that, just like-- like--"
        "He didn't have time to finish his sentence as hot spurts of cum sprayed out against the tree. Kethar fell into a post-sex haze as Rowan finished up with him, still pulling at the orc's hair while his other hand fell against his slender waist."
        show cg869 with sshake
        show cg869 with sshake
        show cg870 with flash
        pause 2
        show cg871 with dissolve
        pause 2
        show rowan necklace naked behind cg891
        "Kethar panted and moaned as Rowan slammed into him, his erection sliding in and out of the orc's ass fully until he reached his own orgasm. His body convulsed, spilling his seed deep into the pretty-faced man." 
        "Rowan slapped Kethar's ass hard as he pulled out and enjoyed the sight of his cum dripping out of his open hole, the white fluids sliding down the orc's asshole and thigh."
        ro "Now that's a good sight."
        "The orc's face heated up as Rowan laughed, putting space between them."
        keth "...We'll be recruited into your army then?"
        "He watched as Rowan got dressed, his voice betraying his reluctance. Rowan slid his clothes back on easily, tucking his softening erection into his pants."
        ro "Well, I am a man of my word. And you did such a good job to earn that position."
        "Rowan's hand slid down Kethar's ass and he pressed a finger against the orc's asshole, stroking him inside once before pulling away. Kethar shuddered but offered no other words as he got dressed."
        scene black with fade
        "Once they were clothed, Kethar led Rowan back to the campsite. None of the other orcs had awakened, so they were entirely unaware of the agreement that transpired just down the pathway."
        "Rowan and Kethar parted as they settled down for the night, and Rowan slept with a dark smirk on his lips."
        return

