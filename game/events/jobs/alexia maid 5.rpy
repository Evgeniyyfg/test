init python:

    event('mary_and_the_cabinet', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), depends=('alexia_and_mary',), group='alexia_maid', run_count=1, priority=pr_npc)
    event('trapped_in_the_closet', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'", 'alexiaJezObedient == True', 'all_actors["alexia"].corruption > 30',), group='alexia_maid', run_count=1, priority=pr_npc)
    event('jezeras_revenge', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'", 'alexiaJezObedient == False', 'all_actors["alexia"].corruption > 30', 'NTR == True',), depends=('more_with_mary', 'in_her_hands',), group='alexia_maid', run_count=1, priority=pr_npc)
    event('dirty_deeds', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",'castle.buildings["brothel"].lvl >= 1',), group='alexia_maid', run_count=1, priority=pr_npc)
    event('recycled_crops', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'", 'alexiaJezObedient == True', 'all_actors["alexia"].corruption > 30',), group='alexia_maid', run_count=1, priority=pr_npc)


label mary_and_the_cabinet:

scene bg14 with fade
show alexia maid shock at midleft with dissolve

"Alexia heard a high pitched scream coming from a nearby room and rushed to find the source. Much of the servant staff was in one of the unused wings clearing it out for future use."
"The scream had sounded like Mary."
"She rushed into one of the empty rooms. A dark dusty place that hadn’t seen life in a long long time."

#show alexia maid concerned

"Only, no one was there. No Mary. Everything in the room was exactly what one would expect from any of the castle’s hundreds of old rooms."
"The only notable distinction was that one of the cabinets, a large oak creation nearly ten feet tall, had fallen over to the ground. Alexia slowly approached it."

#show alexia maid shock at midleft with dissolve

show mary neutral behind bg14

mary "Help me! Help me!"

"Alexia nearly jumped. Mary’s voice was coming from underneath the cabinet, so muffled as to be hard to make out."

al "Mary!? Are you alright? What happened?"

mary "I don’t know! I don’t know! I was just cleaning the cabinet and it attacked me. Started coming right at me and fell over on top of me!"

al "W-what?"

"She glanced at the cabinet. She’d seen nearly 100 in this exact make today alone. None had attacked her yet."

show alexia maid neutral at midleft with dissolve

al "Doesn’t matter right now. We need to focus on getting you out. Lift together on the count of three."

al "One."
al "Two."
al "Three."

hide mary
#mary tired or similar
show mary neutral at midright with dissolve

"At first, the going was difficult. The cabinet was so heavy, they barely made it budge. But, through screaming and shaking, they eventually made the cabinet lift just enough that Mary was able to wriggle her tiny body through a gap."
"Mary rolled on to her back. Eyes closed and panting."

show alexia maid happy at midleft with dissolve
show mary happy at midright with dissolve

"When her eyes opened again, she saw Alexia just standing there, dumbfounded. Mary squealed and hugged Alexia’s leg."

mary "My lady... I thought I was going to die under there! You’re amazing."

#if they've had sex - TODO
#mary aroused
#"Mary giggled to herself and smirked."
#mary "Well, I already knew you were amazing, but…"
#alexia maid angry
#"Alexia rolled her eyes."

show alexia maid neutral at midleft with dissolve

al "How did you even end up under there? You said it tried to attack you?"

"Mary rose to a ball, her eyes wearily trained on the heavy piece of furniture."

#mary angry

mary "Mhm. Right after I entered the room, it just came lunging at me out of nowhere. This place hasn’t been cleaned out since the days of Mistresses’ father. Who knows who used to live here?"

"Alexia leaned down, brushing her hands on the cabinet. She traced it with her fingers looking for unusual markings. Perhaps just waiting for it to move. It did not."

al "This is a totally normal cabinet."

"She gave it a hard kick. No response."

al "Not moving or anything. Are you sure about that?"

mary "It’s a monster! Really! I don’t know why it’s not moving now. But, it was before. It was. I promise."

#alexia maid angry

"Alexia sighed to herself. She liked Mary. But, she didn’t really understand Mary."

al "Let’s get you back to the house keeping room. You’ve got a bunch of scrapes and bruises. There are bandages there."

#mary neutral

"Mary rubbed her wrists and nodded slowly."

mary "Okay."

"As they turned to leave though, she turned back into the room and yelled out loudly towards the inert hunk of wood."

#mary angry

mary "But, right after we’re going to bring a bunch of tough orcs with axes down here."
mary "You hear me, asshole!? They’re going to turn you into firewood."

"Mary slammed the door behind them."

hide alexia with moveoutleft
hide mary with moveoutleft

cabinet "They’re going to have to find me first..."

return

############################################################################################################
############################################################################################################
############################################################################################################

label trapped_in_the_closet:
    
scene bg14 with fade
show alexia maid neutral at midleft with dissolve
show mary happy at midright with dissolve

"Early in the morning, Alexia joined a line of servants. Jezera had wanted them for something important before tasks began for the day. The entire castle staff was standing in ranks like a military unit."

show jezera displeased at edgeleft with dissolve

"They had to wait five minutes before Jezera, hair still a mess, wandered in."

je "Good morning, boys and girls."

"She advanced slowly down the line, looking up and down at whomever she passed. The maid or servant in question straightened their posture and prayed to whatever deity they respected that Jezera would not notice an imperfection in their posture."
"Alexia went into the same posture as the others."

je "We have a guest coming from the east. I will need four staff working, specifically, under me today, for the sake of ensuring his room is kept constantly clean and whatever he desires is given to him. That means that representing Bloodmeen is your job."
je "Alright alright alright. As lovely as my voice is, I’m sure you’re all just wondering who has the job."

"She walked up and down the line. Then, she suddenly pointed at one of the maids."

je "You."

"She moved her finger to the maid’s neighbour."

je "You."

"She paused in place, putting her finger to her lips. Then, she suddenly picked one in the back."

je "You."

"Jezera kept on walking down the line, absentmindedly looking over potential prospects. Alexia’s heart thumped along with the clacking of Jezera’s heels. Was she about to be picked?"
"Jezera reached Alexia...and kept on walking along."

show alexia maid aroused at midleft with dissolve

"But, as she did, Alexia exchanged glances with her for a brief moment. Jezera’s eyes reached into hers, and for the briefest of seconds, her Mistress gave her a secret smile. Just for her. It made Alexia think of satin and chokers."
"Alexia was still giving a goofy grin towards empty air even seconds after Jezera passed."

je "Hrmm. Perhaps, Mary. How do you feel about the idea of being the face of our hospitality?"

show mary neutral at midright with dissolve

"Mary stood at attention a few paces over from Alexia. When her name was called out, she gave a proper curtsy. Or at least as much of one as she could manage with that minuscule skirt of hers."

mary "Such a position would be an honour. I’d love to work under you. Mistress."

"Jezera brushed one her long fingernails down her cheek slowly."

je "No. Not the right kind of guest."

"She turned away. Mary didn’t seem to consider it much of a slight. With a lowered head, she returned to proper attention."

je "I think Sazaria. You will join them as well."

hide jezera with moveoutleft

"Alexia barely noticed as the meeting broke up. Jezera had other work to be done, of course. The entire castle relied on her. Alexia and the other maids remained to receive their assignments."
"Yet, Alexia was half in a trance as she went about her morning. What did Jezera have planned for the next time she was summoned down to her quarters? The thought consumed her."

show alexia maid shock at midleft with dissolve

"So much so, in fact, that it took a sudden and shocking pinch in the rear to break her from her stupor."
"She was standing a hallway alone now. That is, except for Mary."

show mary happy at midright with dissolve

mary "You were walking in the wrong direction, silly. We’re on kitchen duty today."

show alexia maid neutral at midleft with dissolve

"She blinked twice. The petite maid was standing in front of her with a beaming facial expression. Her usual unquenchable cheerfulness was on full display."

al "Oh? You’re right."

"Mary giggled in a high girlish tone."

mary "You don’t gotta say a word about it. I understand. You were all giddy thinking about Mistress Jezera, right? Totally normal."

al "I was-"

show alexia maid shock at midleft with dissolve

"Alexia blinked again."

al "What?"

"Mary raised her shoulders and struck up a mischievous smile."

mary "I’m not blind, silly goose. Those “Fuck me” eyes you were making at her. Those “I will” eyes she was giving you back. And all of those late night visits to-"

#alexia maid angry
show alexia maid neutral at midleft with dissolve

"Alexia moved without thinking. No one else was in the hallway. So she shoved the smaller girl to the wall and loomed over her with narrowed eyebrows. Her arms slammed the wall, holding Mary in place."
"She couldn’t know. If people knew they could tell Rowan."

al "I don’t know what you think you saw, Mary. But, you don’t know what the slightest thing about what you’re talking about."

"Mary, for her part, just kept on smiling. She hadn’t even reacted to being shoved against the wall, except with a mouse-like squeak."

mary "Ooh, rough."
mary "Don’t worry. I’m not about to run around screaming about it. No worries. I know how to be to keep my lips gagged."

#alexia maid concerned

"Alexia slowly eased backwards, moving her arms to the side. As the surprise faded, so too did the rage. Mary would not be telling her this if she planned to skip off to Rowan. Besides, that wasn’t Mary’s style."
"Besides, she knew Mary. Would Mary actually try to harm her?"

al "Is there something you want from me?"

mary "Oh, nothing at all. We’re friends, silly.  I’m just glad to have you as a serving sister is all."

#alexia maid neutral

"Alexia tilted an eyebrow."

al "Serving sister?"

show alexia maid shock at midleft with dissolve
#show mary naked happy

"Instead of answering in words, Mary answered by lifting up her skirt. Alexia froze, dumbfounded. For starters, Mary was not wearing any panties."

if maryNakedSeen == True:
    "Alexia already knew what she would find, but could not help looking down. She’d seen it all before."
    scene cg399 with fade
    pause 3
    "The intricate tattoos, the piercings to most intimate places. Even the word slave written dramatically above her sex."
    "It had been shocking at the time. In truth, even all this time later, it was still stunning."
    scene bg14 with fade
    show alexia maid shock at midleft with dissolve
    #show mary naked happy
    show mary happy at midright with dissolve
    "Now Mary was showing it all to her voluntarily. Did this mean that-"
    
else:
    "But, had the pussy it revealed been an average one, Alexia would not have been left so shocked."
    "No, Mary’s pussy was something unique entirely. It was laced with a string of piercings. Alexia struggled to count them." 
    "More than that, it was marked with the word “Slave” written in beautiful cursive above it."
    "Alexia took a step back and muttered under her breath. How? Why? Who would do something like this to their body?"

mary "A slave must have an Owner, after all. Perhaps one beautiful and a bit sadistic. Now we have the same Owner!"

show alexia maid aroused at midleft with dissolve

"Alexia’s knees shook. Without even meaning to she took a step backwards, ceding ground to Mary. She didn’t mean...she couldn’t mean...But, yet.."

al "D-Did she make you get all that?"

"Mary giggled softly and played with the hem of her skirt."

mary "Worried it might be your turn next? Hehe. Don’t worry. I was the one who asked her to get them. My idea. It was too sexy not too."

#show mary happy

"Finally, she brought the skirt back down, removing the depraved sight from Alexia’s gaze."

mary "So, tell me the story, sister. Oh, you have got to tell me everything. I want to hear every last juicy detail!"

show alexia maid happy at midleft with dissolve

"Alexia rolled her eyes. This was much more like the Mary that she knew." 
"Still, here was someone who not only would keep a secret, but probably had a similar experience. Alexia had to admit it would be interesting to open up to someone about it."
"Oh, she didn’t say everything. If a detail concerned Rowan, Alexia kept it from her tongue. She also didn’t mention the trip to Rosaria." 
"Still, Mary hung on every last word, asking the occasional clarification question. When the story finished, Mary clapped her hands together."

mary "Wow! You must really be a prize to her. She never did anything remotely that impressive for me!"

show alexia maid neutral at midleft with dissolve

al "You serve her, but she doesn’t value you?"

mary "Nope. I’m just a toy! You’re clearly much more important to her."

"Mary sighed happily. Alexia couldn’t help raising an eyebrow. Mary had said it so matter-of-factly. No, she almost relished it. Shouldn’t that make her sad?"

mary "But, that’s okay. Everyone has their place. Mine just happens to be on my knees. "

#alexia maid concerned

"Alexia’s heart was torn by this. Mary was her friend. How had she had internalized the idea of her own inferiority to the point where it no longer even bothered her?"
"Yet, Alexia couldn’t help turning over what Mary was saying in her mind. She’d known for awhile that Jezera had other pets. If Jezera really was treating her as something special, did that mean that she really did..."
"She lost her footing slightly. She suddenly felt woozy."

al "This all feels...I don’t know how to say it...wrong? What kind of woman enjoys something like that?"

"Alexia blurted it out before she realized that she’d just insulted her friend."

show alexia maid shock at midleft with dissolve

al "Oh. I’m sorry. I didn’t mean to-"

"Mary interjected."

mary "A fuckslave!"

"Alexia blinked twice."

mary "I’m a pussy addicted fuckslave. That’s the kind of woman who enjoys something like that."

"For the first time since they’d met, Mary wasn’t smiling. She wasn’t angry. Just...serious."

mary "I’m a slave with a Mistress. I have a purpose. And it’s to serve with everything I have. Especially my body."
mary "Back in my home village, they had all these dumb rules about who I could fuck. Who I couldn’t fuck. It had to be a man. It had to be someone I was married too. My parents had to approve."
mary "But, that just wasn’t me. I wanted to be kissing, rubbing, and fucking every pretty girl that crossed my path. That’s why Mistress made me her slave. Now I can fuck and fuck all I want, and no one cares. I’m just a slave. What’s wrong with enjoying myself?"

"Alexia found herself silent yet again. Mary had a way of disarming her with her bluntness. Especially about such lewd topics."

"Mary stepped closer and placed a hand on Alexia’s waist."

mary "You don’t need to struggle so much with it, cutie. Do you like having sex with Mistress?"

show alexia maid aroused at midleft with dissolve

"Alexia sighed."

al "...Yes."

mary "So you do like fucking girls, then?"

"She was suddenly much more aware of Mary’s hand."

al "Well, I don’t know if it’s all girls…"

mary "But, when you see her perfect purple skin, it makes you all hot and steamy, doesn’t it?"

"Alexia closed her eyes."

scene black with fade
show jezera happy at center with dissolve

"…"

scene bg14 with fade
show alexia maid aroused at midleft with dissolve
show mary happy at midright with dissolve

al "I suppose so."

mary "And when Mistress fucks you, is it tame and chaste?"

"Mary was brushing her hand now along Alexia’s stomach in a slow rhythmic fashion. Light, fleeting touches constantly moving."

al "Well no…"

mary "And she wants you to develop your skills at sex and using your body, right?"

al "..."

"Alexia sealed her eyes shut. Was Mary...insinuating they were the same? That couldn’t be right."
"Mary’s hand trailed up slightly. Alexia let out a slight gasp. She’d felt the back of Mary’s hand brush over her nipple through her outfit."

mary "And do you like it when she teaches you those things? When you get to act like a bad girl?"

"Alexia tried to formulate a way to say that Mary didn’t understand. That it was more complicated than that. Nothing of the sort ever came out."

al "...Yes."

"Mary drew her hand back suddenly. Alexia suppressed a groan. Her eyes fluttered open to see Mary grinning in a way she’d never seen before. Less cutesy and more...hungry."

mary "See! You’re a fuckslave too! You just haven’t accepted it yet!"

"Alexia stumbled back a step. The back of her foot hit the wall."

al "I’m not..I’m not that…"

mary "Mm. Silly silly. Your slave sister Mary is here to help drive all those silly lies away."

"Mary advanced slowly."

mary "In fact, you probably got all wet and steamy just from talking about it, didn’t you? I’m willing to bet a pretty penny on it."

"Alexia huffed. She was letting Mary get the better of her. Letting her read her mind. Letting her read her body. This had gone far enough already."

#alexia maid angry
show alexia maid neutral at midleft with dissolve

al "I’m not a fuckslave like you. There isn’t a tattoo on my crotch. Jezera is just showing me a few things. I still have control of myself. I still have choices."

"Mary did a twirl and giggled to herself. Alexia let herself exhale."

mary "Well, fuckslave or no. Jezera does always allow her toys to spend quality time together."
mary "So, miss self-control. We could always take a teeny little break in that closet over there. I could help you with that wet pussy of yours. What do you say, sister? Think you’re going to, hehe, choose to do that?"

show alexia maid aroused at midleft with dissolve

al "..."

"Alexia’s attention distinctly went between her own legs and the sensations emanating from them. Her eyes couldn’t help drifting to the opening of the closet."
"Mary leaned up to her ear and gave her final pitch in a husky whisper."

mary "No one would have to know. It would just be between us girls."

menu:
    "Nod.":
        $ released_fix_rollback()
        $ marySex = True
        "Alexia almost shook her head. She’d spent the better part of the conversation denying all of Mary’s totally baseless assertions."
        "And yet.."
        "Alexia nodded." 
        al "I don’t think...I don’t think that would be so bad..."
        "The words flowed from her mouth, as though she hadn’t been the one to say them." 
        "Why had she said it?"
        "Alexia wondered that even as a grinning Mary pulled her by the hand towards the waiting closet. She had all the eagerness of a puppy."
        "Still, the reason why she was doing this could not be denied for long. Mary had been right about one thing, at least. She was wet."
        "The closet itself was small. An old stone enclave into the castle for the purpose of storing supplies. Alexia nearly hit a broom on the way in." 
        "The space was cramped and dark. The only light came from a crack in the door that Mary left open behind them. The size of the closet forced their bodies together. Already Alexia’s bosom pressed to Mary’s. That wasn’t an unpleasant feeling."
        "To her surprise, Mary didn’t start throwing herself at Alexia the moment they were safe in the darkness. She actually dutifully removed her glasses and stashed them away in a spot out of reach. It was a smooth, practiced gesture, like a habit she’d built up over time."
        al "I've never quite had a tryst this way before. What now?"
        mary "Now this."
        #mary aroused
        "Mary went to the tips of her toes, and slowly brought her lips to Alexia’s. Her lips tasted good. Like cherries. After only a few seconds, Alexia was starting to get into it."
        #CG1
        scene cg563 with fade
        #mary naked
        show mary happy behind cg563
        show alexia necklace naked aroused behind cg563
        pause 3
        "In the darkness, there were a flurry of hands. Grasping. Undressing. Garments fell to the floor of the closet. The largest of which was the longer maid dress Alexia wore. Mary’s entire dress slipped off like it was hardly there, though. Had it been made to be removed easily?"
        "Alexia and Mary both started to sink, landing gently on their knees. It put them on an even plane. By now, Mary was down to little more than her lace undergarments and her heels. Mary didn’t even have undergarments."
        "Their hands explored each other’s bodies and their tongues explored each other’s mouths. Mary was so soft. It felt good to rub against her body. Their breasts and stomachs met." 
        "Her companion quickly had her pussy pressed against Alexia’s leg. Alexia followed suit." 
        "Mary’s body had a strange texture to it. Alexia was only still getting used to the soft sweet feeling of another woman’s body. Mary’s petite form certainly fit that bill." 
        "But, as Mary ground her nipples and crotch into her, the feeling was interspaced with hard metal. Each sensation heightened her awareness of the other. The piercings made her softer, and her body made the piercings more overpowering."
        "It was driving Alexia crazy."
        mary "Mph. Mph. I'm getting all wet…"
        "Alexia rode Mary’s thigh. It reminded her of the way she’d use a pillow back during her youthful experimentations. The harder she ground herself, the more and more she drowned in the pleasure. Her juices coated everywhere she rubbed. Hot and wet."
        "The same was happening to Mary. Her head rolled back and her posture grew more restless by the moment. Alexia’s thighs were getting wet with juices besides her own."
        "It went on and on without advancing or progressing. There was none of the urgency of sex with a man. When her body was locked with another woman’s she could rub and tease and play for so long that it was hard to pay attention to time."
        "Who would even want to think about time when her breath was at your neck and your entire body felt so good?"
        "Alexia's breath caught at her throat. A long throating moan was building up...only to be silenced by Mary’s hand."
        mary "We have to be quiet, sis. We can't have someone open up and see a p...pair of sluts in here."
        "Mary’s voice came out in a breathy whisper."
        "Alexia nodded slowly. A pair of sluts..."
        al "Dizzy…"
        "Without thinking, Alexia kicked out her leg. She’d been so lost in the fog that her space constraints were not on her mind. When she kicked out, it hit the wall with a loud bang."
        "Alexia and Mary both froze in place. Alexia’s eyes shot open. What had she just done?"
        "Then, from outside the closet, the sound of heavy male footsteps grew louder and louder. Mary silently drew the door totally closed, leaving them in darkness."
        scene bg14 with fade
        show andras displeased at midleft with dissolve
        "Andras walked slowly down the hallway. His muscles were tense. He looked as though he were preparing for battle." 
        "Suddenly, Andras froze in place." 
        "He thought he heard something. Breathing perhaps. Only it was very heavy. He sniffed the air. His large frame towered over the hallway."
        "No one was there. Seemingly." 
        "He brushed his hair back and kept on walking. Though, if he looked tense before, it was only more so now."
        #CG1
        scene cg563 with fade
        #mary naked
        show mary happy behind cg563
        show alexia necklace naked aroused behind cg563
        pause 3
        al "Mary…"
        "Alexia panted softly. It was hard to even form words."
        al "Why were you teasing me? We could have been found out…"
        "The entire time that someone had been walking past, Mary’s hand had been between Alexia’s legs. It would have been a struggle to keep totally quiet even without the mischievous touches."
        "Mary gave a breathy giggle."
        mary "Why did you like it so much, then?"
        "Alexia sealed her eyes shut. Then she opened them once more. Some of the lust that clouded her gaze receded."
        al "No more teasing."
        al "You’re the lesbian fuckslave, right? The one who spends all of her time with other girls? You like to pretend that you’re so skilled."
        "Alexia brushed a hand over Mary’s cheek."
        al "Prove it."
        "Alexia leaned back, as much so as space would allow, and pulled away her panties. By now, they were so soaked that they were practically unwearable."
        mary "..."
        mary "As you command."
        #CG2
        scene cg564 with fade
        show alexia necklace naked aroused behind cg564
        pause 3
        "If Alexia had actually believed Mary to be bluffing, she had made a real mistake. Without another word, Mary was on all fours, practically throwing her face between Alexia’s legs."
        "Alexia’s eyes flew open. Mary’s tongue had plunged deep inside of her and was now frantically exploring her inner walls." 
        "Mary didn’t have a technique built on slow and steady buildup. She attacked Alexia’s sex like a woman possessed. Her tongue twisted and flicked at expert speeds."
        "She was completely unprepared."
        al "Oh...fuck…"
        "In mere moments, her head was rolled back and her chest was rising and falling fast. Alexia sucked in air but couldn’t stop feeling breathless. Mary’s tongue always seemed to find the exact right spot to do the maximum damage."
        "Already dripping, she was soon bucking and spasming. She was going to cum. She was going to cum."
        al "M...Mary…"
        #CG2 - var 1
        scene black with fade
        "Alexia spasmed. Waves of toe curling delight filled her body. Every nerve ending was alight."
        "But, Mary wasn’t done. Games between girls don’t have to stop after one."
        "For the next half hour, the closet was filled with the sounds of desperate moaning. At times even aroused screaming. Alexia was pushed past the edge over and over again."
        "Mary’s tongue never seemed to tire or grow sore. She just kept on attacking and attacking. A flick of the clit. A move deeper into her folds. All of it made Alexia squirm."
        "By the time she was done, she’d left the redhead crumpled on the closet floor like a puppet whose strings had been cut."
        scene bg14 with fade
        show alexia maid aroused at midleft with dissolve
        show mary happy at midright with dissolve
        "Both women, fully clothed once more, left the closet holding hands. They were both flushed red, although Mary was not half as flushed as Alexia." 
        "Mary’s glasses were crooked. She’d put them back on in the dark." 
        "Alexia, meanwhile, found it hard to even hold Mary’s hand. Her hand would still spasm every few seconds. Aftershocks."
        al "You’re such a slut, Mary."
        mary "I thry. Sisth."
        "Her words came out so slurred that Alexia could barely understand it. So, she just kissed Alexia’s cheek instead to get the point across."
        "Alexia groaned. Something told her that Mary wouldn’t be content with a single tryst."
        al "Sisters, huh…"
        "She brushed a shaky hand along her neck."
        $ change_actor_num_flag('alexia', 'jezera_influence', 3)
        $ change_corruption_actor('alexia', +5)
        return

    "Shake head.":
        $ released_fix_rollback()
        "Alexia paused. She was wet. She could feel it. The proximity of Mary’s body did nothing to alleviate that. Neither did the feeling of her breath at Alexia’s ear."
        "But, was she so wet that she couldn’t maintain control of herself?"
        show alexia maid neutral at midleft with dissolve
        "Alexia shook her head firmly, and playfully pushed Mary out of her personal space."
        al "Nice try, Mary. Did you really think I would be that easy? The answer is no."
        mary "But, what if-"
        show mary neutral at midright with dissolve
        "The smaller maid pouted. Alexia’s head was already starting to defog."
        al "Nope."
        "Alexia glared into Mary’s eyes and Mary glared back. They held their stare for a few seconds that felt like minutes. Like two sams circling each other with horns out." 
        "Mary broke her glance first."
        mary "Mph. Darn it."
        "She stomped her foot."
        mary "I was doing my best purring seductress voice too!"
        show alexia maid happy at midleft with dissolve
        show mary happy at midright with dissolve
        "They both laughed a little bit."
        "Alexia rolled her eyes. Was this what Mary was like with other girls who she’d seduced? A little disappointment and she turned to a petulant child. Her parents really must not have done a good job with her."
        al "You were. It almost worked even. Almost."
        "Mary sighed. They started walking towards the Kitchen, where they were both expected for work."
        mary "You may have won this battle, sis. But, I’ll get you next time. Don’t think I’ve given up yet!"
        "She giggled playfully. Alexia couldn’t help but smile a bit too."
        al "Sister, huh?"
        mary "Mhm. Sister slaves to the same Mistress."
        al "I see."
        #alexia maid concerned
        show alexia maid neutral at midleft with dissolve
        "It was almost like there was an entire kingdom beneath Jezera. A series of feudal dues and power structures invisible to anyone who wasn’t clued into the network."
        "The question for Alexia was...where exactly was she in this kingdom? Was she a duke? Or a peasant?"
        return

############################################################################################################
############################################################################################################
############################################################################################################

label jezeras_revenge:

scene bg14 with fade
show alexia maid neutral at midleft with dissolve
show mary concerned at midright with dissolve

"Something was off today, Alexia could feel it."
"She was working with Mary today. The first time in what seemed like weeks. The maid in charge of scheduling just wasn’t placing them together so much."
"Yet, Mary didn’t seem to be glad about working with her. The petite maid kept her distance and hardly spoke a word. It took fully hours of start and stop attempts to start up a conversation before she finally got a reply."

al "...Mary? Is everything okay?"

mary "Hmm?"

al "You’re really quiet today. I didn’t think it was possible."

"Mary didn’t meet her eyes."

mary "What’s that supposed to mean?"

"Alexia blinked."

mary "I can be quiet if I want to. You don’t have to be so judgemental all the time."

al "I-"
al "What?"

"Mary still refused to meet her eyes. Her handles slightly shook as she folded a sheet."

mary "I think that…"
mary "I think it would be a better idea if we didn’t have work duty together anymore, you know? It’s not like I’m mad or anything. Just thinking."

show alexia maid sad at midleft with dissolve

al "..."

"Had she really done something so awful? Alexia could scarcely believe what was happening. Mary had been her best friend on the castle staff…"

mary "Oh don’t give me that face. I’m just saying…"

al "Wait. Why are you saying this? Aren’t we fri-"

mary "Look, this is what I have to do. We can’t work together anymore. Don’t make it harder than it has to be."

"The illusion of a normal day’s work was totally broken. Alexia thought she saw the start of tears behind Mary’s glasses. All of it was so confusing. What could she have possibly done to have offended her?"

mary "I don’t even know why we’re on a shift together, today. You know what? Fuck it."

"Alexia was still too stunned to speak, even as Mary marched out of the room. At first, she thought her friend would return, but as the minutes ticked on, it was clear what had happened. Mary had left her here."

hide mary with moveoutright

"The confusion only grew as the day went on. Others seemed to be keeping a wide arc around her too. She went to work in the kitchen and none of the other maids, people she knew, even showed up."
"Something was going on. She could feel it from the way people were looking at her."

scene bg18 with fade
show jezera neutral at midright with dissolve
show alexia maid neutral at midleft with dissolve

al "Jezera?"

"The demoness was sitting at her desk working on a scroll of some sort. She had not risen to look at Alexia since she’d entered the room."

al "I wanted to talk to you about my placement on the maid staff."

je "Oh? Is there a problem, dear?"

"Alexia looked sideways."

al "For some reason, people have been avoiding me. Early on, I thought it was just Mary, but some of my other friends from the staff haven’t been talking to me."

show jezera happy at midright with dissolve

je "Perhaps you have merely done something that put them off. You do have a certain...cold disposition to people who want to be your friend."

"Alexia raised an eyebrow."

al "What do you mean by that?"

je "Oh. Nothing. Nothing."

#alexia maid concerned

"Alexia crossed her arms. Something was off. She could feel it in the pit of her stomach."

al "I was wondering if there was something you could do to help me. You are the one who runs the castle staff, after all."

je "Oh sweetie. It’s not my business to intercede in the personal nothings of the maids. I am the lady of the castle."

al "Uh-huh."

#alexia maid angry

"Alexia’s eyebrows narrowed further."

al "Do you know why so many people have been acting strangely cold to me, lately?"

"Jezera smiled wide."

je "Of course not. As your host, all I want is for you to feel comfortable in this castle. I only wish I could do more."

"Did she mean what had happened back at that secret lake. Yet, she hadn’t even been mad about Alexia’s rejection at the time..."

al "Well, whatever is happening, it is making me uncomfortable on the castle staff. Perhaps, if you figure out what’s happening, you should help me stop it."

je "Perhaps, the problem is you? You simply might just get on poorly with the rest of the castle staff."
je "In fact…"

"She put a finger to her lip."

je "Perhaps it might be better if you found another place to work. Perhaps a place where you wouldn’t anger so many people."

"Alexia threw her hands to her hips. The implication was clear."

al "I happen to like working on the castle staff."

je "Oh, I know. But, if it’s creating so many problems, I just have to look out for you and ensure something is done."
je "I’m afraid you’re going to need another job."

al "I-"

#jez smirk

je "I insist."

#alexia maid concerned

"Alexia sighed. There was no point in trying to argue with the woman who held all the cards."

al "Fine. I’m sorry for having taken up your time."

#jezera happy

je "Oh, of course. I’m always here to help Alexia. You know that."

"Alexia half slammed the door on her way out. For the rest of the day, she looked damn near like she was going to burst with anger."

$ all_actors["alexia"].job = None
#TODO - remove maid job
return

############################################################################################################
############################################################################################################
############################################################################################################

label dirty_deeds:
    
scene bg24 with fade
show alexia maid shock at midleft with dissolve
show shaya neutral at midright with dissolve

"Alexia had expected many things when she was called down to help the brothel, but she had not expected this."
"Alexia, and the other maid, were looking out at a side room that was covered in blood and semen. Beautiful purple tapestries were stained red. Bits of bone littered the ground."
"This was a murder scene."

if all_actors["alexia"].corruption < 31:
    al "Lady Above…"

else:
    al "What the fuck…"
    
"The keeper of the brothel was with them, and all she could offer was a deep sigh and shake of her head."

sha "An unfortunate scene. I am aware."

"Shaya calmly walked over to a large chunk of bone and held it aloft. After a few seconds staring at it, she deposited it unceremoniously on a side table. There was something unnerving about how little the sight phased her."

sha "To keep a ravenous succubus under control is a challenging task for any human. A task I accomplish skillfully at normal times. Still, accidents cannot always be avoided."

"Shaya sighed."

sha "My friends, please remember that it is more important to be thorough then it is to be speedy."
sha "The room may be sidelined in favor of others for a time. But, were one of my compatriots to attempt to ply her art, it would not do for her patron to find a man’s femur."

"The maids were still collecting themselves when Shaya gave a short bow and moved towards the entrance of the room."

sha "If you need my assistance, I am near."

hide shaya with dissolve

show alexia maid neutral at midleft with dissolve

"Alexia turned back to the splatter that had once been a human being. Her glare narrowed and she rolled up her sleeves. This was going to be a rough shift."

if alexiaJezObedient == True:
    "Hours later, Alexia returned to the office of the Brothel. She was a mess. Her uniform was stained with bodily fluids. Some had even gotten into her hair."
    show shaya neutral at midright with dissolve
    sha "The task is complete?"
    "Alexia nodded"
    sha "And no blood or gore shall be discovered later?"
    al "We combed the entire room. Beneath every piece of furniture too. I don’t think we missed anything."
    "Shaya nodded softly and brushed the back of her hand against Alexia’s arm. She noted to herself that Shaya had chosen a clean segment to reassuringly touch."
    sha "You have my most humble thanks. Please tell your compatriot that you may use our baths to clean yourselves. Our ladies must be kept clean, so our waters are among the finest in the castle."
    sha "A hard job must be rewarded."
    "Alexia broke into a smile. She had to admit that after everything she’d just done, a nice and rewarding bath actually sounded quite good."
    hide alexia with moveoutleft
    "As Alexia left, Shaya made her way back to the side room to inspect how the maids had done. She whispered to herself beneath the veil."
    sha "Rather plain seeming from her first test."
    sha "Still, I shouldn’t doubt Mistresses’ wisdom…."
    return

else:
    return
    
############################################################################################################
############################################################################################################
############################################################################################################

label recycled_crops:
    
scene bg14 with fade
show alexia maid neutral at midleft with dissolve

"Alexia was starting work early in the morning, just after she’d changed into her maid uniform. A tap on her shoulder drew her attention."

maid "The Mistress wishes for you to attend her in her quarters."

scene bg18 with fade
#show alexia maid concerned at midleft with dissolve
show alexia maid neutral at midleft with dissolve
show jezera neutral at midright with dissolve

"Shortly after, she was at Jezera’s door knocking. When a voice called for her to enter, she shuffled inside with her head down and gave a well trained curtsy."

"You called for me, Mistress? How might I be of service?"

"Jezera looked up lazily from the large tome in her hands. Two more books scattered on the table seemed to be of a similar topic. It was a marvel she could split her attention in so many ways."

show jezera happy at midright with dissolve

je "Alexia? Good good. I told them to send you, but sometimes those fools need a swat in the rear for a reminder."

$ res_roll = dice(4)

if res_roll == 1:
    je "I need a maid to attend me. Last night, I and this delightful Uvraithi man made such a mess. I need someone to replace the sheets and make this place spotless."

elif res_roll == 2:
    je "I need a maid to attend me. Last night, I and this delightful Prothean made such a mess. I need someone to replace the sheets and make this place spotless."

elif res_roll == 3:
    je "I need a maid to attend me. Last night, I and this delightful Rosarian slut made such a mess. I need someone to replace the sheets and make this place spotless."
    
else:
    je "I need a maid to attend me. Last night, I and this delightful Qeratzeli contortionist made such a mess. I need someone to replace the sheets and make this place spotless."
    
show alexia maid aroused at midleft with dissolve

"Alexia scanned the room. She wasn’t lying about the state of the room. The bed alone looked like it had been a battlefield."
"She bowed her head slightly in a maid’s practiced reverence."

if pickyCleanupSeen == True:
    show alexia maid happy at midleft with dissolve
    al "But, nothing in green, right Mistress? It isn’t your colour, after all."
    "Jezera smirked."
    je "Actually, perhaps something green is in order this time around. You know how I like the occasional change of pace."
    show alexia maid aroused at midleft with dissolve
    
"But, before Alexia could even start on the room, Jezera had more demands."

#jez smirk

je "One more thing. You needn’t remain so stiflingly dressed when it’s just us girls in here, do you? The boys are away, after all."
je "Sweet dove, I called you for a reason. I want service...and a {i}show{/i}."

"A blush crept over Alexia’s cheeks. But, such a request from her Mistress was hardly a surprise by this point."

#CG1 
scene cg898 with fade
show alexia maid aroused behind cg898
#jez smirk
show jezera happy behind cg898
pause 3

"She didn’t issue a word of complaint, even as her uniform polled at her feet." 
"She settled on leaving on her bra and stockings. But, most everything else was openly on display for Jezera’s viewing pleasure."
"It was only after she finished that she noticed the implement in Jezera’s hand. A small leather riding crop."

al "What’s that for-"

"She was interrupted by a lightning quick, but not especially hard, strike to her rear. An involuntary squeak burst from her lips."

je "In case you mess up, darling. I'm not quite the sadist my brother is. But, surely it's well within my rights to punish my service staff if they don't perform their duties adequately."

al "I-yes. Of course, Mistress."

"Alexia set to work on the delicate task of cleaning Jezera’s room. She was not some first-time maid now. She’d been on the job long enough to approach the task with the special delicacy it deserved."
"Jezera occasionally hovered over her, crop in hand. But, she mostly stayed by her table with multiple books in hand at the same time."
"Yet, every time she looked up at Alexia’s creamy nudity, the poor maid was left flustered. To Jezera, she was prey to be eaten."
"Despite herself, the more she cleaned, the more worked up she would get. There was hardly a moment she wasn’t secretly hoping for the demoness to look her way."
"For the sun to shine down on her. When Jezera didn’t look for too long, she found herself taking more provocative poses."
"She’d clean with her rear bent over dramatically. Or else, she’d make extra sure to stand straight when she needed to reach something high up. This was Jezera, surely she’d soon be making suggestive remarks to her?"
"Of course, it wasn’t like Jezera wasn’t paying occasional mind to Alexia. But, an ache set in every time Jezera returned her glance to the book."
"She wanted more."
"The moment of opportunity came when Alexia had moved on to the bookshelf. It was filled with unordered books and scrolls. Nothing that couldn’t survive a fall..."

menu:
    "Resist the impulse.":
        $ released_fix_rollback()
        "She shook her head slightly."
        "This was a job. Yes, she was getting the personal benefits of one on one time with her Mistress. But, why had she joined the castle staff if not to keep things in smooth working order?"
        "She brought her duster to the bookshelf, and to the best of her abilities, wiped the accumulated residue from them. She even took the time to sort some of the books by title."
        "At the end of the work period, Alexia returned to Jezera and gave a deep bow. Jezera had not budged from her spot, save for bringing in new reading materials. Whatever work she was doing, it had a stronger hold on her attention then Alexia."
        "It was a strange thing, being jealous of a stack of parchment."
        al "I have completed the task as you commanded."
        "Jezera playfully waved the riding crop back and forth in Alexia’s face."
        je "Did you now? Let’s see about that."
        je "The bedding is...competent this time."
        je "The shelves are cleaned. Even organized. Risky. I might have had things where they were for a reason."
        "Alexia kept her eyes low."
        al "I know you better than that, by now."
        je "So you do."
        je "It appears that everything is in order."
        "The demoness strolled back into her seat, crossing her legs. Alexia couldn’t resist the urge to peek at her."
        je "It seems you’ve avoided the crop for today. You must be overjoyed."
        al "Very much so."
        je "One last thing…"
        "She raised her foot into the air. From Alexia’s hunched bow, it hung nearly a hair from her face."
        je "A kiss."
        "Alexia’s final act before departing was giving that foot a respectful little peck. The sensation lingered on her lips even as she dressed, even as she returned to work. Nothing else from the day stayed in her memory long after."
        return
        
    "Provoke a punishment.":
        $ released_fix_rollback()
        "With an “ill” placed swipe of the hand, scrolls and books went tumbling to the floor. It seemed half the shelf had been dislodged. Alexia immediately went to her hands and knees scrambling to collect the fallen material."
        "But, she peaked up over her bangs to see if Jezera would shine her attention back on her. Jezera did not disappoint."
        al "I was just trying to get some of the dust on top of the-"
        je "{i}Shhh.{/i}"
        #CG2 
        scene cg954 with fade
        show alexia maid aroused behind cg954
        #jez smirk
        show jezera happy behind cg954
        pause 3
        "Nailed fingers worked their way into Alexia’s hair. Then, inhumanly strong arms raised her like a ragdoll and shoved her hard against the wall. A gasp escaped her lips."
        "Jezera was close. She was using her weight to press Alexia against the wall. In practice, that meant bodies touching. Breast against breast. Lips so close that Alexia wanted to taste them."
        al "No, I-"
        je "{i}Shhh. Shhh.{/i} No words, no words."
        je "I know why you did it. Such a needy little creature. I know just the {i}punishment{/i} you need."
        "Alexia’s eyes widened slightly. She felt something brushing between her legs. There was no need to look down. She knew what it was. The crop. The friction of the leather running over such a sensitive place stole a gasp from her."
        al "Ah…"
        "But, even as she was getting used to the skilled rubbing, another sensation entered the mix. Jezera pulled the crop back and put a light strike between Alexia’s legs."
        al "Ah!"
        "Alexia’s hips squirmed. Her clit burned with pain, but before she could adjust, Jezera had switched back to rubbing. Her body had a quick sensation." 
        "Soon she was squirming to the rhythm of her Mistresses’ ministrations. The crop was growing damp from the state of Alexia’s exposed crotch."
        je "Such a desperate little creature. Disobeying me so she can be played with. That’s not how a good and proper maid behaves."
        al "No, it’s-AH!"
        "Her response was silenced by another swat of the crop between her legs. Her lips twisted into a wide and desperate gasp."
        je "{i}Shh{/i}. No words."
        "Alexia’s hips rolled with greedy intensity against the surface of the crop. In truth, she preferred fingers, but in Jezera’s hands, the strip of leather was overpowering. Her Mistress rolled it in a circle, the crop turning into an instrument in the hands of a violinist."
        "And, whenever Alexia settled into a rhythm, the source of mind melting pain."
        al "Ah!"
        "The swats of the crop seemed to bleed into the rubbing. Every time her pussy was struck, it was left more sensitive to the next round of pleasure." 
        "It was almost too much. Her lungs felt empty of air. The weight of sensations threatened to crumble her. Had Jezera not been holding her aloft with the hand cruelly gripping her hair, Alexia would have collapsed to her knees."
        al "Ah...Ah...ah…."
        je "You just have no self-control, pet. So desperate to be used that you’d misbehave just for a bit of...{i}sensation{/i}."
        je "You need to learn a lesson."
        "Her cheeks grew red. Her fingers squeezed and opened. The frantic spastic moves of a woman riding an edge." 
        "And then...it stopped. The crop was gone."
        al "I-"
        je "{i}Shh.{/i}"
        je "Did you really think I was going to let you get off, after you misbehave? I’d just be training you to make a mess of things in my room every time you’re horny."
        "Alexia whimpered softly as Jezera withdrew. Her hair no longer being gripped, she sank halfway down the wall. Her chest rose and fell, searching for missing breath."
        "All the while, her cunt pulsed...ached…"
        je "Clean up the mess you made from the bookshelf. I want it exactly as I left it before."
        al "But…"
        je "And then leave. You are clearly in need of further training before you can have the privilege of personally tidying my room."
        je "But, I’m a generous Mistress. Further training is not something you will have to wait long for."
        al "..."
        al "May I speak...Mistress?"
        "Jezera giggled to herself."
        je "I don’t know why that would be necessary, darling."
        "And so, Alexia set back to work. The mess from the book shelf was advanced enough to require a surprising amount of effort to clean up."
        "The ache didn’t help. It didn’t help at all..."
        $ change_corruption_actor('alexia', +3)
        return
