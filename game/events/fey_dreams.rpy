init python:

    event('heartsong_dream_1', triggers="week_end", conditions=('week == 17',), group='ruler_event', run_count=1, priority='pr_story')
    event('heartsong_dream_2', triggers="week_end", conditions=('week == 19',), group='ruler_event', run_count=1, priority='pr_story')
    event('heartsong_dream_3', triggers="week_end", conditions=('week == 21',), group='ruler_event', run_count=1, priority='pr_story')
    
label heartsong_dream_1:

#CG 1
scene cg790 with fade
pause 3

"Pine needles descend in a thorny rain upon the orphan’s head. They collect and tangle in his moppish hair, like the laurel crown of a woodland king."
"He can feel his heartbeat, quick and pattering as it beats a nervous furor in his chest. Tiny fingers clench tight upon the yew bow in his hand. His toes tremble in his boots, numb from the frosty snow that engulfs his legs up to his ankles."
"The boy’s left arm strains from the force of the draw, his elbow shivering as his fingers cling fast to the nock of the arrow." 
"Across the gulf of space and time, he stares, wide eyed, at the tiny creature standing in front of him." 
"Yellow eyes peer back. Fearless, curious, penetrating. Her black nose wrinkles as it sniffs the air." 
"The pale fox regards Rowan with curiosity, pausing mid-step in the snow as it waits for the human to make the first move. They are less than a dozen paces away from one another." 
"And yet, he hesitates." 
"How did he get here?" 
"Cold memories leak in to fill the yawning cracks. A blur of continuity spreads across his mind: the disappearance of his parents, the sudden, jarring shift from domestic bliss to orphaned isolation."
"Weeks of frightened solitude. The villagers coming to see him, alone and hungry in the family cabin. Words: empty explanations and quiet platitudes. He does not register them, he only asks why."
"They take him into the Elder’s home. Flashes of a strange bed, an unfamiliar hearth and foreign food made by a stranger’s hands scamper through his mind."
"Questions. Endless, unanswerable questions. No one can tell him anything. No one can explain what’s happened: where they have gone, why he is alone."
"Tears. Anger. Frustration. A desperate need to search, to find them, to make things go back to the way they were." 
"He packs his things in secret, squirreling away what food and supplies he can, then makes tracks to Da’s old hunting grounds."
"And now here he stands: three days into the wild with his supplies exhausted and not one step closer to discovering an answer he would never find."
"The fox’s reasons for being here are a mystery, but the rumble in Rowan’s belly was far less ambiguous." 
"He’d never killed anything before."
"Something hot and wet fills the small boy’s eyes, obscuring but not impeding his vision. He blinks them away. His breath issues forth in great, white gouts from his mouth as he lets loose a shuddering exhale."

menu:
    "He looses the nock, and the arrow flies.":
        $ released_fix_rollback()
        #CG of Rowan Shooting Fox
        scene black with fade
        "Quivering fingers release the arrow, and it fires forth with deadly precision. The yew groans as the bowstring twangs in his grasp."
        "A dark bolt speeds across the white landscape, punching into the small fox and sending her sprawling."
        "A startled yelp. Rowan lowers his bow and examines the kill from a distance. He caught her hard in the chest, just above her left leg." 
        "The little creature lies there, sprawled out in the snow, a shock of red glistening on her fur where the arrow has struck."
        "It was a clean kill, as clean as could be expected. Rowan lets out a downcast sigh and trudges over to where the fox has fallen." 
        "The indent of her body in the snowdrift makes it look almost as if she had fallen into a shallow grave." 
        "She lies motionless, her eyes closed as if she is merely resting. For some reason, it makes Rowan’s heart hollow to look at her this way."
        ro "I-I’m sorry."
        "The mumbled words slip out of his mouth without thinking as the breeze picks up, sending the boy’s hair tumbling across his face. He whispers a quiet prayer for the fox under his breath."
        "He knows what comes next. The skinning, cleaning, cooking and preparing. He may have made his first kill, but there is still so much to do. Mother had shown him how to do it." 
        "Something about the thought of his mother gives him pause. His hand hesitates as it reaches for his hunting knife." 
        "Wait… how did she do it? Rowan wracks his brain for a moment as he tries to remember his missing mother’s lessons."
        "A sudden terror grips him as he realizes he can recall next to nothing about her."
        "All he can remember are sensations: feelings rather than memories. A quiet recollection of nights spent huddled up by the hearth: of gentle lullabies whispered into dozing ears, a slender finger curling across rosy cheeks in the firelight."
        "Such a warm memory. Such a warm, blurry memory."
        "Rowan grasps at her fading image with desperation. He cannot picture the barest details of her face.The very thought of it causes the boy to panic."
        fox "Why?"
        "A voice cuts through the frigid stillness, interrupting the dream with its singular incongruity. Rowan lifts his head, his eyes widening as he realizes the dead fox is looking at him. Through blood-caked lips she opens her mouth and whispers."
        fox "Why?"
        "Horror grips the young boy as he stumbles, falling back onto his hands. His eyes go wide, watching as the injured Fox lifts her head and looks at him. Her body twitches and writhes upon the ground."
        ro "W-what?"
        fox "Why did you shoot?"
        "Rowan’s voice catches in his throat. He tries to form words, but the world is full of sludge."
        ro "I…"
        
    "He waits too long, and his arm grows tired from the strain.":
        $ released_fix_rollback()
        "The fox and the boy stand across from one another in the snow, time stretching onwards towards eternity. The wind blows a gentle breeze across his face, his hair buffeted by its touch. The same breeze ruffles the fox’s white fur."
        "She stares at him, her yellow eyes fixed to his. Empty of malice, devoid of judgement. She makes no move, content to watch the child decide her fate."
        #CG of Rowan Dropping Bow
        scene black with fade
        "Rowan’s vision fills with water for a second time. The bow slips, useless from his hands. He falls to his knees, sniffling and crying as he covers his face to hide his shame."
        "What a worthless son he’s become. His parents had shown him how to hunt a hundred times before. He’d been practicing with a bow since almost before he left his swaddling clothes. He could hit the fox from this distance with his eyes closed."
        "Yet… he cannot bring himself to do so."
        "Father would be ashamed of him. Had their roles been reversed, he would not have hesitated to loose the deadly quarrel. Rowan is sure of it."
        "Or... would he have?" 
        "What {i}would{/i} his father have said to him in this moment? A sudden panic strikes the boy as he realizes he does not know."
        "He cannot remember his voice, nor his words, nor even his face. He is a figure on the horizon, a hazy image in the mist." 
        "And that is all he will ever be. The little boy cries all the harder."
        fox "Why?"
        "A voice cuts through the frigid stillness, interrupting the dream with its singular incongruity. Rowan lifts his head, his eyes widening as he realizes the white fox is standing right in front him, close enough to touch."
        "The snowfall has stopped. The world around them has stilled into nothing."
        "The beast looks up at him with a quizzical expression. She opens her mouth, and repeats the question."
        fox "Why?"
        ro "W-why?"
        "Baffled by the sudden twist in the memory, Rowan rubs his tearstained eyes and stares at the talking fox. She curls her snowy tail around herself and sits, lifting her head to stare directly at him."
        ro "Why what?"
        fox "Why didn’t you shoot?"
        "Rowan’s voice catches in his throat. He tries to form words, but the world around him turns to sludge."
        ro "I..."
        
scene bg9 with fade
#rowan necklace naked shock
show rowan necklace naked concerned at midleft with dissolve

ro "{i}Guh{/i}!"

"Rowan leapt out of bed in a single, swift movement, carrying the blankets with him as he all but cartwheeled back into consciousness."
"His heart was pounding out of his chest, his mind racing. For a moment he forgot where he was, as lost as he’d been in the dream."

show rowan necklace naked concerned at midleft with dissolve

ro "N-no…"

show rowan necklace naked neutral at midleft with dissolve

ro "That wasn’t just a dream."

"No dream he’d had in his life had ever been so lucid. His skin shivered from the sensation of the cold, winter air. His arm still trembled from the stress of drawing the bowstring taut."

show rowan necklace naked concerned at midleft with dissolve

ro "Gods, I haven’t thought about that day in years."

"The events had played out just as the dream had shown them: with the notable exception of the fox talking to him." 
"The memory was among the earliest he could clearly recall of his childhood. It took the Elder half a week to finally track the half-starved and hypothermic boy down. He’d nearly died."
"It was there, at that moment, when he had the fate of another’s life in his hands, that Rowan finally came to terms with the truth."
"His parents weren’t coming back. He could no longer rely on them to keep him safe. From now on, he had to make his own decisions, for good or ill." 
"...So why was he dreaming of it now?"

return

########################################################################################################################
########################################################################################################################
########################################################################################################################

label heartsong_dream_2:

#karst bg
scene cg849 with fade
pause 2
scene cg850 with dissolve
pause 2
show rowan necklace concerned at edgeleft with dissolve
show rosarian knight neutral behind cg850

"Rowan’s eyes fluttered. The first thing that hit him was the sound of screaming. So many directions at once. The effect was pure disorientation."
"Then came the smell. To say it reeked could not possibly describe it. The scent that assaulted his nostrils would make a man think he would never smell something good again."
"Rowan’s eyes fluttered. He was on the ground. His tunic was dirty. His pike was lying by his side. That was wrong. The knight who commanded his division had told the men that anyone who lost their pike would be flogged. He scrambled to retrieve it on hand and knee."

ro "Ai-aiden?"

"He looked around. His unit was nowhere to be found. Only...only…"
"Rowan’s eyes fluttered. He was on a battlefield. Next to him, two armored men were fighting. Behind him, a member of his unit was being hacked apart by two giant orcish brutes. He looked down and realized that the stain on his tunic was blood."
"His blood? Someone else’s? There was no time to think about it. There was only instinct. Rowan ran."
"Shadows darted through the trees. Giant Orcish brutes and armored men wearing full metal facemasks stalked behind them, cutting down routed soldiers."
"He joined the bloody and chaotic mass flying towards the nearby keep. Men with gaunt faces. They had been turned into animals. Behind them, their once mighty army crumbled. Thousands were dead. Thousands more were sure to die."
"And in front of them stood the fortress. Built into a cliffside with jagged walls running up impossible angles. An impenetrable bastion camouflaged by the treeline and cliffs."
"Karst."
"Rowan’s eyes fluttered."
"He was standing in front of a sealed gate, along with a dozen or more men. They were pushing and shoving. Hands clutching the bars. Body parts were thrust through the small gaps, as if getting one's arm through to the other side might save the rest of him."

rkn "Please, let us in! Please! By {i}Balast{/i}, open the gate!"

"Another man clamored up above the screaming."

rkn "We’re going to die! You’re going to kill us!"

"A man on the ramparts above them looked down, his face gaunt. He kept glancing back out towards the battlefield. To where the sounds of screaming men and bloody slaughter still emananted." 

gkeeper "I...gods...I can’t open the gate! I’m sorry. {i}Fuck{/i}. They could be coming any second. Go away!"

rkn "Help us!"

gkeeper "They’ll kill us all!"

"The standoff was only broken when another man emerged on the rampart. He wore a soldier’s garb. Blood stained and damaged."

rkn "Goddess {i}bloody fend{/i}. Open the damn gate, you cunt! "

"There was the sound of a scuffle. Rowan couldn’t track it. All he knew was that the gate soon opened in front of him. The trapped men surged forward. One of the survivors in front fell down and was near trampled before rolling to the side."
"Rowan saw the man’s hand grasping towards the entrance. So close to safety…"
"The moment he crossed the threshold, his ears were struck by a thunder of a sound. Orcish shatter horns blowing. Men went to the ground, clutching their ears. Sound and sensation mixed to the point he could feel a sound. His bones shook and rattled inside of him."

hide rosarian knight
show rosarian knight neutral at midright with dissolve

"Rowan’s eyes fluttered. He was standing in front of the soldier who’d forced the gatekeeper to open up. Only now did Rowan see the long gash running down his arm. Where were the healers?"

ro "I’m just… I’m just looking for my unit…"
ro "I was with….er...I was with Duke Raeve’s levy. He must have made it back. He wasn’t in the front."

"The soldier just shook his head sadly."

rkn "Lived, probably. But, gone. Him and all the other lords with horses. Anyone on four legs scattered to the interior. Didn’t even stop by the keep to pick up his shit."
rkn "Raeve. Crevette. Probably even my own Duke Werden."

ro "Not Werden. He was caught with the vanguard. I saw it. At least, I think I did."

"He spat to the side."

rkn "Guess that means I don’t have a lord now, eh? Well, doesn’t matter if he’s a coward or a corpse."
rkn "We’re alone. "

hide rosarian knight with dissolve

"Rowan glanced back to the gate, to where the awful sounds of the battlefield still sounded, quieted only by distance and what meager cover the walls offered." 
"The slaughter continued unabated."
"Rowan’s eyes fluttered."
"He was walking along the side of the curtain wall, his gaze blurry and unfocused. Everything was numb."

ro "Aiden? Cal? Anyone?"

"He watched with drooping eyes as a group of men staggered past him, laughing near-hysterical. They held fine booze in their hands, and about their shoulders were draped fine coats of leather pulled over their bloody uniforms." 
"They stumbled and drank more. Whatever lord the goods once belonged to evidently wouldn’t be coming back for it."
"But, when Rowan got closer, he saw their wide, teary eyes. To these men, this was a cadaver’s party. A final send-off before the orcs reached the gates."
"There was a priestess of Solansia huddled in the corner. Rowan couldn’t help but stare at her hair. It was so vivid and red…"

ro "Alexia…"

"The priestess muttered desperate, pathetic prayers. A call to the heavens that would never receive an answer. Long streaks of tears rolled down her face."
"Rowan stumbled on. His eyes kept fluttering."
"Then, he was in front of a man he knew. Aiden, from just down the road. He’d been drafted in Trosshoven. Another member of his unit. Rowan was near silent as he applied a rag to the young man’s leg."
"The gash was ugly. Bits of muscle were exposed. The ground beneath him pooled with blood and piss. If Rowan could move him, he would have. If he could search for a healer without Aiden bleeding out, he would have."
"He watched as Aiden frantically twitched and groaned. Every fresh warhorn from outside the walls jolted him again. Rowan was forced to hold his leg down to keep the rag in place. "

aiden "My… my sister was just about to give birth. Don’t you know, Rowan, I’m probably an uncle by now?"
aiden "Can you believe it, an uncle. Isn’t that incredible?"
aiden "..."
aiden "I’m going to see him someday. Right? Right? I bet he’ll look just like her. Haha. Maybe afterwards I’ll try to find a girl so I can have one of my own."
aiden "Tsk. This is wrong. This is all wrong."

ro "Please…Please hold still. You’re going to make it-"

"Rowan’s hands balled up on the rag. They were near fists by this point. Aiden had broken into a tortured sob, but he just kept going."

aiden "None of this was supposed to happen. I’m good. My priest said so. My parents said so. I did everything I was supposed to."
aiden "I’m going to...I can just go. I did my service. I did what I had to do. I’m just going to go home."
aiden "Fuck."
aiden "She was supposed to protect me. That’s what the priest said. Goddess..."
aiden "I just want to see my sister..."

"Rowan bit his tongue. He was so numb, even if he wanted to put his feelings to words, it just wouldn’t happen. It was too much."
"Aiden’s sobbing grew more frantic and his words became gradually less coherent. Rowan kept on holding the rag down. Just… hold the rag down."
"Even when Aiden’s body went still, Rowan continued to press it tight against his leg. What else could he do?"
"Rowan’s eyes fluttered. Some men from his unit had dragged him from the ground. Someone was shouting his name. Rowan’s eyes kept on fluttering."

cal "Rowan! You need to listen to me! Rowan! Can you hear me!?"

ro "Huh?"

"Suddenly, a sharp pain spread from his cheek. It took him a moment to realize he’d been slapped. Rowan staggered back, blinking. The adrenaline put him back in reality."
"He looked around. These were men he recognized from his unit."

cal "That’s Aiden, right? Goddess fend, he looks a right mess."

ro "He’s dead."

cal "One more then."

"Cal gestured behind him. Two other men from the unit were holding a third. Rowan had to squint to recognize him as Raphael."

cal "Raphael’s in it bad, but we’re looking for a healer. We know some of them had to have made it back in."

"Rowan tested his grip with his hand. Forming a fist and opening it again. Something was missing, but he couldn’t remember what."
"A healer? He’d seen a priestess, hadn’t he?" 
"...Why hadn’t he thought of that when he was with Aiden? She’d had red hair…"

ro "We have to do something, yeah. I think… I think I saw a healer before. But, I don’t know if she’s in any shape to help him."

"The thought was interrupted by a sound from above. He looked on the ramparts and saw the dark outline of a figure falling. Everyone watched in horror. A few gasped as he hit the ground with a bone chilling {i}crunch{/i}."

show rosarian knight neutral behind cg850

rkn "I guess, that’s one way out of here."

"The small band of survivors trudged down the decayed path back the way Rowan had come in. The growing weight dawned on him. He’d lost his pike. Had he left it when tending to Aiden? Or... was it before?"
"Rowan chuckled slightly. If his officer were still intact, he’d be in real trouble."
"In the distance, Rowan saw a figure curled up against the wall. His eyes widened. Her hair was red..."

ro "Alexia."

"He closed his fists into balls. He needed a weapon. He needed to do something…."
"His eyes fluttered again." 

show rowan necklace concerned at midleft with moveinleft

"Rowan was striding towards the armory. There had to be something there. He’d left the former survivors of his unit behind. Most of them were too battle shocked to even think." 
"He found that a small crowd of men had gathered. One burly man had taken center in front of the main weapon rack, and was giving an impromptu speech."

burlys "We need to surrender now. If we give them the keep before they are forced to attack, they may be willing to show mercy."

"A clamoring went around. They’d seen what had happened on the field. They knew what was happening to their comrades outside the walls at that very moment."

burlys "Shut up. Shut {i}up{/i}, let me talk!"
burlys "Yes. I don’t think the orcs will spare us. But, Zerias is out there with them. He was a duke once. He’s one of them, but he’s not like the others. If we surrender to {i}him{/i}, specifically, he might spare us."
burlys "Look. Look."
burlys "Maybe...maybe they’ll keep us as slaves! I’ve heard of demons doing that. Keeping captured soldiers as slaves, for the mines. "
burlys "That can’t be worse then-"

"Rowan was done listening to this man. Without concern for the consequences, he walked over to the weapons rack. The defeatist was in the way, so Rowan shoved him lightly to the side."

burlys "Are you crazy, what are you doing?"

ro "I lost my pike. I need a weapon. Probably a bow. And a sword. I’m better with those…"

"The man didn’t intervene, even as Rowan pulled weapons down from the rack. The moment there was a bow in his hand, he felt good again. In the fight before he’d been forced to use that unwieldy stick. But, this was a weapon he knew."
"He faintly remembered trudging through snow, his sights on a fox…"

burlys "You can’t be serious. Look at you. You had to have just come from out there."

"Rowan shrugged."

ro "There are still people out there. The fight isn’t done."
ro "..."
ro "Can’t just stand around here doing nothing."

"Whatever calm remaining broke. Individual soldiers shouted words that might be extreme in another circumstance. Some were directed at the burly man who’d been giving the speech. Some probably were shouting at him. Rowan didn't much care."
"Rowan’s eyes fluttered. He walked out of the armory, back towards the gate. But, a dozen or so men followed him from the gathering. It was almost annoying, being followed. One particularly bothersome fellow was hovering at his shoulder, voicing his worries aloud."

hide rosarian knight
show rosarian knight neutral at edgeleft with dissolve

rkn "One man can’t keep the route of retreat open single handedly. The orcs will crash over you like a wave. This is suicide."

ro "Can’t just do nothing."

"The annoying man didn’t stop following him. Neither did any of the others. So Rowan kept marching forward."
"His eyes fluttered.  He was standing at the edge of the gate again. There were men all around him now. Others who’d seen them leaving. Rowan hadn’t planned any of this. "
"He stopped, and his little band of followers stopped too. Eyes on him. Waiting to see what he did. When he continued, they started back up in tandem."
"More of the survivors seemed to drift into the small band by the moment. By the time Rowan reached the gate, there must have been at least fifty of them."
"The gatekeeper raised the portcullis for this small force. Rowan’s grip tightened on his bow, the higher it got. There was a battle to fight on the other side. His day wasn’t done."
"Then, bloody chaos in front of him, Rowan charged forward. Around him a cry went out. The other men were shouting." 

hide rosarian knight with dissolve

"Rowan’s eyes fluttered. Then the sound drifted away. Rowan was alone."
"He looked behind him, and found a single soldier standing in awe. A female levy with a face that Rowan almost recognized...but he couldn’t place it..."

femsol "How did you do that?"

ro "How did I do what?"

femsol "Take command, lead those men back into that awful situation."
femsol "You kept a level head, when all the world was collapsing around you. No one else did. Just you."
femsol "You knew what awaited you when you led them back into those woods…"

"Rowan swallowed. His throat felt tight as he realized he wasn’t breathing. He’d never noticed it before in all the chaos of battle, but the soldier’s eyes were a brilliant, piercing yellow."

femsol "Why did you choose to go back out there?"

ro "It wasn’t even a choice. I… I just couldn’t sit by and let things happen."

femsol "Why not?"

"Rowan felt as if his heart was about to burst from his chest."

ro "Bec-"

scene bg9 with dissolve
#rowan necklace naked shock
show rowan necklace naked concerned at midleft with dissolve

ro "{i}Guh{/i}!"

return

########################################################################################################################
########################################################################################################################
########################################################################################################################

label heartsong_dream_3:

scene black with fade

"{i}...Someone’s coming.{/i}"
"{i}You’d best wake up.{/i}"

scene bg8 with fade
show rowan jail hurt at midleft with dissolve

"Rowan blinked the bleary sleep from his eyes and sat up off the cold ground. How long had he been asleep? His stomach rumbled with unfulfilled hunger."
"He was… in the dungeons. The Twins had captured him. He’d been their prisoner for months."
"His head swam as he looked around for the source of the voice that had woken him up."

ro "Hello?"

"No response. Perhaps he’d just imagined it."
"Soft footsteps echoed down the dungeon hallway. Rowan watched the flickering shadow beneath the door as the visitor stopped outside his cell."
"He held his breath. The door swung open with a yawning creak, revealing his tormenter."

show jezera neutral at midright with dissolve

je "Hello hero, it has been a while."

ro "Demon."

"Jezera’s eyes trailed across his bruised and broken form. Her mouth twisted into a dissatisfied frown."

je "It seems my brother’s goons have done a number on you."
je "I warned you that this would happen, didn’t I?"

ro "Is that what you came down here for? To say ‘I told you so’?"

je "No. I came to try and talk some sense into you."

ro "And I’m sure I can hazard a guess as to what you think the ‘sensible’ option is."

show jezera happy at midright with dissolve

je "Isn’t it obvious?"

show jezera neutral at midright with dissolve

je "It’s been months, Rowan. There’s no hope of escape. No one is coming to your rescue."
je "Are you really this stubborn? Do you honestly intend to rot alone in this cell for the rest of your life?"

ro "Compared to the alternative? Rotting is preferable."

"She sat down across from him on the cold floor of his cell, crossing her legs as she leaned her back against the wall."

je "You’ll die here if you refuse Andras’ offer, you realize that."

ro "I know."

je "Then why persist with this pointless resistance?"

ro "You two aren’t giving me much say in the matter."

je "Staying here is a choice, Rowan."

"There was an odd cadence to Jezera’s voice, a forlorn tone he could not quite place."

je "Why follow a hopeless path, when you know what it will cost you?"

ro "Because some things are worth more to me than my life."

je "..."
je "Like what?"

menu:
    "My honour.":
        $ released_fix_rollback()
        je "But what of your wife, Rowan? What of the people you swore to protect?"
        je "You cannot embrace a concept; you cannot hold honour in your arms and tell it that you love it."
        show jezera displeased at midright with dissolve
        je "No one save Andras and I will know what became of you. Your last valiant act will go unnoticed, unrecognized, unremembered."
        je "Your honour means nothing. It is as fleeting as a gust of wind. What about the life you’re trying to build? The family you’re trying to create?"
        show jezera neutral at midright with dissolve
        je "What good is honour to a man fettered in chains?"
        
    "My wife.":
        $ released_fix_rollback()
        show jezera displeased at midright with dissolve
        je "And you think {i}defying{/i} us will ensure her safety? "
        je "What makes you think we care about Alexia any more than the dozens of your townsfolk that we’ve slaughtered already?"
        show jezera neutral at midright with dissolve
        je "Will you really choose to die down here without ever seeing her again, deluded in the thought that she’s somehow safe in our clutches?"
        je "Are you really willing to let that happen to the woman you supposedly love?"
        
    "The lives of innocents.":
        $ released_fix_rollback()
        je "So you will damn yourself and your loved ones to a terrible fate, all for the sake of… an abstraction?"
        show jezera displeased at midright with dissolve
        je "What even {i}is{/i} an ‘innocent,’ Rowan? How do you measure the value of a stranger's life in comparison to your own?"
        je "You are gambling everything on the erroneous assumption that somewhere, somehow, the scales of cosmic justice will balance in your favour."
        show jezera neutral at midright with dissolve
        je "You will never live to see if you guessed correctly."
        
    "My pride.":
        $ released_fix_rollback()
        je "Your stubbornness is to be admired."
        show jezera displeased at midright with dissolve
        je "But what good is your pride, if everything you have reason to be proud of has been stripped away?"
        je "We’ve already stolen your life, your wife, your dignity, and your honor. We have been lenient thus far: if I hadn’t overruled Andras, he would have already thrown you into the wulump pit."
        show jezera neutral at midright with dissolve
        je "Your pride will not protect you from your fate, and it will be a trifling thing to take away from you."
        
    "You wouldn't understand.":
       $ released_fix_rollback() 
       je "No. I don’t. So help me understand, Rowan."
       je "Why go through all this suffering? Why fight so hard against an enemy you have no hope of winning against?"
       show jezera displeased at midright with dissolve
       je " Is it simple stubbornness? An inability to give in to a foe who has beaten you?"
       je "I am extending my hand to you, offering you every opportunity to have you join us as an ally."
       show jezera neutral at midright with dissolve
       je "Yet still you persist with this choice. Day after day, month after month. Doesn’t it get tiring? Don’t you wish you could just… give in?"
       
    "On second thought, let me get back to you on that.":
        $ released_fix_rollback() 
        show jezera happy at midright with dissolve
        "Jezera giggled, putting a hand up to her mouth to cover her smile."
        je "Ha ha ha!"
        je "I’m sorry, you caught me quite off guard with that last remark."
        ro "I live to please."
        show jezera neutral at midright with dissolve
        je "But perhaps, for all your japes, you understand me then? This path you've chosen leads nowhere. There is no coming back from this if you refuse my help."
        je "You’re running out of reasons to say no."
        
ro "What do you want from me, Jezera?"

je "Nothing."

ro "You wouldn’t be talking to me if that were the case."

"The Demon said nothing for a long moment, regarding him with an inscrutable expression. "

je " I’m just trying to understand, Rowan."
je "You know how to make hard choices - impossible ones, even - when lesser men would falter and crumble."
je "Very few people are capable of shouldering that kind of burden. You could even say I admire you for it."

ro "Spare me your false flattery."

show jezera displeased at midright with dissolve

je "It’s not flattery. It's the truth."

show jezera neutral at midright with dissolve

je "But the one thing I can’t figure out is how you do it. How do you decide? "
je "You’ve held the fate of thousands in your hand. You’ve sent men to their deaths, knowing they would perish without ever learning the reasons why."

ro "Sometimes, you just have to make that decision. You either make them or they're made for you, but you can't avoid them."

je "But... how do you know you’re making the right choice?"

ro "You don’t. That’s the point of choosing."
ro "Courage doesn’t happen when you have all the answers."

"To Rowan’s surprise, Jezera smiled."

show jezera happy at midright with dissolve

je "Then maybe that’s the answer we’re both looking for."

"Jezera stood up off the ground, brushing the stray grime from her outfit."

je "Think on what I’ve said. The time is coming soon where you’ll have to decide your own fate."

"Turning away towards the door, the Demon cast a last, fleeting glance back over her shoulder."

je "I think I’m beginning to understand you, Rowan."

"With that cryptic comment, she shut the door behind her, leaving Rowan alone with his troubled thoughts."

hide rowan with dissolve
scene black with fade
pause 1
scene bg8 with dissolve

"Some time later, (or was it mere moments?) Rowan was startled out of his sleepless reverie by a sharp jab of pain in his ribs."
"He opened his eyes to see an orc towering over him, the metal toe of the beast’s boot pressed into his side."

show orc soldier neutral at cliohnaright with dissolve

os "Get up humi, is time to go."

show rowan jail dirty at midleft with dissolve

ro "Where are you taking me?"

os "No questions, go."

scene black with dissolve
scene bg6 with fade

"When they reached the dais, the orc removed the manacles from Rowan’s wrists and retreated. He was left alone with Andras and Jezera."

show andras smirk at edgeright with dissolve

an "Greetings human, I trust you are enjoying the accommodations."

show rowan jail neutral at midleft with dissolve

ro "If your only purpose for bringing me here was to mock me, I’d rather stay in my cell."

show jezera neutral at midright with dissolve

je "That is enough, brother."

show andras displeased at edgeright with dissolve

an "You are decidedly no fun, sister."

ro "You two seem busy. I could come back later, if you‘d like."

show jezera happy at midright with dissolve

je "I am glad to see your sojourn in the dungeon has not harmed your sense of humour."

show jezera neutral at midright with dissolve

je "You really are a resilient person, aren’t you Rowan?"

"Andras shot his sister a curt side-eye."

an "…Very well. The reason we have summoned you is because my sister has convinced me to give you one final chance."
an "Has some time alone in that cell brought you to your senses?"

je "Will you serve us?"

menu:
    "Agree to serve them while biding your time.":
        $ released_fix_rollback()
        $ serveChoice2 = 1
        
    "Agree to serve them so you don't turn out like the other prisoner.":
        $ released_fix_rollback()
        $ serveChoice2 = 2
        
    "Agree to serve them so you can see Alexia again.":
        $ released_fix_rollback()
        $ serveChoice2 = 3
        
    "Agree to serve them because Jezera was convincing.":
        $ released_fix_rollback()
        $ serveChoice2 = 4
        
    "...You’re not really Jezera, are you?":
        $ released_fix_rollback()
        $ serveChoice2 = 5


if serveChoice2 == 5:
    "Jezera stared at him for a long moment. A soft smile curled at the corners of her lips."
    show jezera happy at midright with dissolve
    je "What makes you say that, Rowan?"
    ro "This isn’t real. None of this is real."
    "Rowan glanced in the direction of Andras. He had paused mid-motion, like a marionette whose strings had been cut, leaving him as still as cut marble."
    show jezera neutral at midright with dissolve
    ro "This is just another memory, isn’t it? Like the dream of the fox in the snow, and the vision of Karst."
    ro "Who are you?"
    je "I’m Jezera."
    ro "No. You’re not."
    ro "How are you doing this? Why have you brought me here?"
    show rowan necklace angry at midleft with dissolve
    ro "What do you want from me?"
    "Jezera’s doll-like face crinkled with confusion."
    je "H-how did you...?"
    "Rowan’s fingers clenched around the hilt of the sword that had materialized at his side. He drew it in one, swift movement, noting its surreal afterglow as it rippled through the watery air. The tip came to rest on the edge of her neck."
    ro "{i}Answer me!{/i}"
    "The Jezera-who-was-not-Jezera stared back at him, heedless of the threat of his blade. She did not flinch. If anything, she seemed transfixed."
    #jezera yellow eyes happy bust
    show jezera happy at midright with dissolve
    je "You’re not at all what I expected you to be, Rowan."
    
elif serveChoice2 != serveChoice:
    "Jezera opened her mouth to continue with her speech, then closed it again. She let out an uncharacteristic squeak of surprise."
    je "Wait… what?"
    show jezera displeased at midright with dissolve
    je "That’s not what happened."
    ro "What are you talking about?"
    je "That’s {i}not{/i} the reason you gave for joining us the first time."
    "He was wondering if she would catch that."
    ro "...And? Our previous conversation in the prison cell never happened, either."
    ro "Given how off-script we are already, I figured you’d play along."
    ro "After all: this is what you wanted, isn’t it? A recreation of the day I pledged myself to the Twins?"
    show jezera neutral at midright with dissolve
    je "How… how are you doing this? This is supposed to be your {i}memory{/i}!"
    "Rowan looked around, noting how blurry and indistinct the world around them had become."
    ro "I made a different choice this time."
    ro "Who are you? Why have you brought me here?"
    "To Rowan’s surprise, the thing that pretended to be Jezera laughed. It was a gentle laugh, full of warmth. Nothing like the mocking lilt of Jezera’s usual cackling."
    #jezera yellow eyes happy bust
    show jezera happy at midright with dissolve  
    je "Somehow, you keep finding new and interesting ways to surprise me, Rowan."
    
else:
    show jezera happy at midright with dissolve  
    je "Excellent, I knew you would come to your senses eventually."
    an "Do you swear to serve us then, human, and do whatever we ask of you?"
    "This was the moment. The culmination of all the choices in his life up to that point. Once he spoke the word, there was no going back."
    ro "Yes…"
    show jezera neutral at midright with dissolve
    je "..."
    je "..."
    "The silence dragged on for far longer than was comfortable or natural." 
    "Something was wrong. The sequence of events was off. Rowan knew what should happen next: the Twins would ask him to seal their hellish compact by sleeping with one of them."
    "...So why wasn’t Andras saying anything? Why was Jezera looking at him with such a melancholic expression?"
    show jezera displeased at midright with dissolve
    je "I don’t understand."
    ro "What’s there to understand? I’ve promised to serve you. This is what you wanted, isn’t it?"
    show jezera neutral at midright with dissolve
    je "But… why?"
    je "Why did you choose to serve them?"
    je "How did you finally decide?"
    "Rowan was taken aback. He fumbled for words for a moment, unable to reconcile the sadness in Jezera’s voice with the Demon herself."
    ro "...Who are you?"
    #jezera yellow eyes happy bust
    show jezera happy at midright with dissolve 
    je "It’s nice to finally meet you, Rowan."

scene black with pixellate

"The world turned to putty around them."
"The unbending stone walls of the throne room sloughed off of the fabric of reality like a moth emerging from its chrysalis. Behind the curtain of the dream, there was only the void."

scene white with pixellate

show rowan necklace shock at midleft with moveinleft

ro "W-what-"

#show heartsong happy at midright with moveinright
show heartsong neutral at midright with moveinright

"Standing before him was a being simultaneously unknown and intimate to him. There was a familiarity in her foreign features, a peculiar affection in the way her piercing yellow eyes held to his."

hear "Don’t be afraid. I’m not here to hurt you."

"Her smile was wide and welcoming, but her eyes gleamed with mischief."

show rowan necklace neutral at midleft with dissolve

hear "I’m sorry for spying on you. To tell you the truth, I was having so much fun with our talk that I completely lost track of time!"
hear "The dream’s almost over. We don’t have much time left."

"Rowan’s eyes widened. That voice… he had heard it before."

show rowan necklace concerned at midleft with dissolve

ro "You’re the fox who's been following me in my dreams."

"The trickster beamed, her tail flicking behind her in tiny twitches as she let out a soft giggle."

hear "Yes!"

show rowan necklace angry at midleft with dissolve

ro "You were there with me in the snow… and at Karst as well, weren’t you?"

"The feminine fox flashed him a fang-filled grin. She could barely contain her excitement."

hear "Yes! Just so. You have a keen memory, Rowan."

ro "Who are you? What do you want with me?"

hear "What makes you think I want anything from you in particular?"

ro "Enough with these lies."

hear "I haven’t lied to you, Rowan."

ro "You’ve been toying with my memories, without my knowledge or consent."

hear "Only to understand them. Only to try to understand {i}you{/i}."

ro "I don’t recall ever inviting you to do so."

"Rowan stepped forward. Instead of standing her ground, she shrank back from him. A red blush filled her cheeks."

hear "I… I-I’m sorry. I really didn't mean to intrude. When I first came here, my only purpose was to try to speak with you."
hear "But... you have such {i}amazing{/i} dreams!"

"Dreams that were universally drawn from painful experiences. Rowan’s fingers clenched around the hilt of his weightless blade."

ro "So you're here to judge me? Is that it?"

hear "What? No, of course not!"

ro "Why else would you make me relive the day I pledged myself to the Twins?"

"The fox’s bewildered expression belied an almost youthful naivete."

show rowan necklace neutral at midleft with dissolve

hear "N-no! Not at all!"
hear "Why would I judge you for that? You made an impossible decision for the sake of your own survival."
hear "I have no idea how you managed to choose, after everything you’ve gone through. That was what I was trying to figure out."
hear "I... you’re the most interesting mortal I’ve met. I’ve never spoken to one of your kind like this before."

show rowan necklace concerned at midleft with dissolve

ro "…‘Mortal?’"

hear "Yes. You are a mortal, and I am a Fae. What else should I call you?"

"Rowan couldn’t tell if her smile was guileless or glib."

show rowan necklace neutral at midleft with dissolve

ro "Fae?"

show rowan necklace shock at midleft with dissolve

ro "...{i}The{/i} Fae? Like the nature spirits in the children’s fables?"

"Her smile widened."

hear "Do you think you’re living in a fable right now, Rowan?"

show rowan necklace angry at midleft with dissolve

ro "I’m talking to a fairy tale."
ro "If this isn’t one, then I’ve descended into lunacy."

hear "Ha ha ha! No, you’re quite sane."
hear "Although I’d advise against telling the Twins about our adventures. They have enough problems with my people as it is; I wouldn’t want to get you into any more trouble."

show rowan necklace concerned at midleft with dissolve

ro "...The Twins know about the Fae as well?"

hear "They ought to, they’ve been using our Leyline network for ages, now."
hear "Well… ages in the mortal sense, at least."

show rowan necklace shock at midleft with dissolve

ro "{i}What?!{/i}"

hear "You didn’t know? Well, I suppose it’s to be expected: those two are not very forthcoming with you."

if serveChoice2 < 5 and (serveChoice2 != serveChoice):
    hear "I guess that’s how you figured me out, huh?"
    
"Rowan’s head spun with the implications of what that this so-called Fae was saying."

show rowan necklace angry at midleft with dissolve

ro "Why are you telling me all this?"

show heartsong neutral at midright with dissolve

"The Fox’s easy smile faltered. She lowered her head, staring glumly at her toes."

hear "...Father would not approve of me meddling in his affairs. But I had to warn you before he arrived."
hear "You’re the only person in the Castle that I think can get through to him, Rowan."

show rowan necklace neutral at midleft with dissolve

ro "Your father?"

hear "Whitescar. He will soon be delivering the Fae’s message of protest to the Twins in person."
hear "I’m frightened of what that could mean for my people... and for you."

ro "Is that what all this was about? You entered my dreams just to warn me?"

hear "No. That was what I {i}intended{/i} to do."
hear "But… your memories convinced me of something else."
hear "I think you can help my people, Rowan. And perhaps, in turn, we can help you."

ro "What do you mean?"

#show heartsong happy at midright with dissolve

"The Fae smiled at him, her eyes twinkling with mirth."

hear "The dream is ending. I must return to the Netherweald before we end up stuck in this place."
hear "We’ll speak again soon, I promise."

"The creature turned as if to depart into the white emptiness."

ro "Wait!"

"The Fae glanced back at him, her yellow eyes alight with mischief."

hear "Yes, Rowan?"

ro "What’s your name?"

"Her smile widened."

hear "H-"

scene bg9 with fade
#show rowan necklace naked shock at midleft with dissolve
show rowan necklace naked concerned at midleft with dissolve

ro "{i}Guh{/i}!"

return