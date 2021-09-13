init python:

    #Greyhide shares his people's liquor
    #Follow up to Drinking buddies if men was chosen.
    event('greyhide_shares_his_people_s_liquor', triggers="week_end", depends=('greyhide_s_table_manners',), group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg22")
    #Jezera is stressed
    event('jezera_is_stressed', triggers="week_end", conditions=('week >=4', ), group='ruler_event', run_count=1, priority=pr_ruler)


label greyhide_shares_his_people_s_liquor:
#Greyhide shares his people's liquor
#Follow up to Drinking buddies if men was chosen.

$ rowanGreyhideLiquorSex = False

scene bg22 with fade
show rowan necklace neutral at midleft with moveinleft

"Rowan was worried about Greyhide."
"It was a strange thought, to worry about the well being of a Minotaur. Rowan couldn’t have imagined it prior to his servitude to the Twins."
"But the man had become a good friend since his arrival in Bloodmeen. One of the few Rowan truly trusted. So it was concerning when he realized the bull seemed to be avoiding him."
"He found Greyhide hard at work at his forge, hammering away at a piece of molten metal."

show rowan necklace happy at midleft with dissolve
show greyhide sad at cliohnaright with dissolve

ro "Good evening my friend, how have things been going for you down here these last few weeks?"

"The bull, startled, whipping around to face him with the molten metal still in his grasp. Rowan had to take a judicious step backward to avoid a grisly burn."

gh "Rowan!"

show rowan necklace shock at midleft with dissolve

ro "{i}Goddess fend{/i}, watch where you’re pointing that thing!"

gh "Sorry, sorry!"

show rowan necklace concerned at midleft with dissolve

"The bullish blacksmith, flustered, turned and dunked the heated hunk of metal into a water barrel. It was the clumsiest Rowan had ever seen him with his work."

ro "Is everything okay?"

gh "Yes!"
gh "Yes, you just... startled me."

ro "Are you sure? I come back later, if you’d rather be al-"

show greyhide neutral at cliohnaright with dissolve

gh "No. Now is fine."

"The Minotaur brushed himself down and fixed an awkward smile onto his face."

gh "I am glad you came to visit."

show rowan necklace happy at midleft with dissolve

ro "Really? I’m starting to kind of regret the choice, myself."
ro "I almost got to learn what a mouthful of molten iron tastes like."

gh "Please, forgive me. I did not mean to-"

ro "It was a joke, Greyhide. No harm done."
ro "So… how are things?"

gh "Well enough."
gh "I... hope that the whelp has not been driving you too hard on the surface."

ro "Heh. I'm managing."
ro "But what about you? I’ve heard you’ve hardly left the forge lately."

gh "You need not worry about me. It is… comfortable down here."

ro "-Says the man who almost just gored me with a bit of hot metal."

show rowan necklace neutral at midleft with dissolve

ro "You should try to get out more. Staying cooped up in this forge all the time can’t be good for you."
ro "Alexia really enjoyed the evening you spent together."

gh "..."

ro "Maybe a little too much, huh? Seems she got almost as drunk as I did the first time."
ro "I’m glad you two had fun though. I’m sorry I missed the festivities."

gh "I..."
gh "Thank you. For your kindness. I do not deserve it."

show rowan necklace happy at midleft with dissolve

"Rowan smiled, putting a reassuring hand on the Minotaur’s shoulder."

ro "You’re too modest, my friend."
ro "What say we have another drinking night, eh? Just the two of us."

"A conflicted look came to the Minotaur’s face."

gh "I would… like that."

ro "Are you certain? If you’re not feeling up to it tonight-"

gh "No. I am sorry, I am being impolite."
gh "Of course, friend Rowan. Let us drink."
gh "Perhaps that is what I need to clear my head."

"Greyhide set aside his hammer, motioning for Rowan to take a seat on a nearby workbench. He then moved to retrieve something from within the drawer of his oversized desk."

ro "So what’s got you so preoccupied?"

show rowan necklace concerned at midleft with dissolve

ro "I’ve never seen you so absentminded."

gh "..."
gh "It is a difficult thing to talk about."

show rowan necklace happy at midleft with dissolve

ro "I promise I’m a good listener."

"The bull let out a rumbling chuckle."

gh "I know you are... Maybe that is the problem."
gh "I am not used to this. Telling others about myself."

"The Minotaur extracted two flasks from the drawer and handed one of them to Rowan. Then he sat down next to him on the bench."

ro "What’s this?"

gh "Firegrout draft."
gh "You shared with me your people's drink, so I wanted to share mine."

ro "Cheers."

"They clicked their flasks together and raised it to each other’s health. Greyhide popped the stopper out with his teeth and downed the contents of the flask in a quick gulp. Rowan took a deep swallow of his, and came up spluttering."

ro "{i}Gah{/i}, that’s strong!"

gh "Ah! I am sorry, I forgot to tell you to only sip at it. It was made with my people’s livers in mind."

"Rowan swallowed the hefty lump of alcohol with a bit of difficulty, his eyes tearing up at the spicy burn it left in the back of his throat. His cheeks flushed with the heat of the drink."

ro "I can tell!"

"Rowan took a more measured sip this time, smiling at the rich texture of the drink. It settled with a comforting warmth in the pit of his stomach."

ro "It's quite good. You said this is your people’s drink?"

gh "Yes. It is hard to come by, outside of the Dragon’s Tail."

ro "I’m honored you’d share it with me, then."

"Greyhide smiled, finally seeming to relax a little."
"He leaned over and pulled a second flask from the drawer without leaving his seat, his massive shoulder blades flexing as he did so. Rowan found his eyes begin to idly wander."

gh "The honour is mine. You are a kind man, too kind for my sake."

ro "Of all the people I’ve drank with in this castle, you are by far the best company."

gh "Heh. A short list, to be sure."

"Greyhide finished off his second flask, and Rowan took another, larger swig from his own. The stuff was absolutely {i}delicious{/i}."

ro "I can see why you’d miss having Firegrout,  Why is it so hard to come by?"

gh "One of the key ingredients is redheart moss, a rare plant native to my homeland.  It grows nowhere else, and even there it is difficult to find."
gh "I had to ask Jezera herself to help me acquire some. I am very glad you like it."

ro "Jezera got this for you?"
ro "That’s… unexpected."

gh "I will be honest, I did not think she would agree to send someone to retrieve it. It was a pleasant surprise when she did."

"Rowan didn’t like the thought of Jezera going out of her way to help an underling acquire something so mundane as an ingredient for alcohol. Mainly because he couldn’t fathom what she stood to gain from it."
"Wheels within wheels, that one. Rowan took another thoughtful sip of his drink."

ro "So what’s bothering you, friend? I’ve never seen you this unsettled."

"The bull nursed his flask, letting out a dissatisfied rumble from deep within his throat."

gh "I am… struggling."

ro "With what?"

gh "With myself."
gh "With what I am."
gh "...I have lived much of my life at the mercy of my instincts, Rowan. My kin are simple, ruled by our urges."
gh " If we are hungry, we eat. If we want something, we take it. And if…"

"He trailed off. A worried frown settled on his bestial features. He stared at the ground."

gh "I do not much like this part of me. I have done what I could to hold it back."

ro "Is that why you spend so much time down here alone?"

gh "The forge is simple. I know my tasks, and completing them gives me joy."
gh "I do not have to worry if what I do or what I say harms others. I can just… work."

ro "You’re living half a life, Greyhide. You need more than just work to keep you going, you need purpose."

"The bull let out a low grunt, reaching out to take another flask from the drawer. Rowan’s cheeks flushed. Was it getting hotter in here?"

gh "I would not know what purpose is. I have not felt it in many years. Work is enough. Work is simple."

ro "You’re not a simple man, Greyhide."

gh "Heh. I am not a man at all, Rowan."

ro "Whether you want them or not, those feelings are still your own. Ignoring them only makes it worse."

"Rowan couldn’t fathom why Greyhide’s expression grew so solemn after he said that. The Minotaur popped open the cork of the flask and downed the contents in one gulp."

gh "Perhaps it is best if I did just that."

ro "Hey, none of that doom and gloom, we’re supposed to be having fun, remember?"
ro "Life’s not just about dwelling on the low moments, it's about enjoying the good ones."
ro "When I shared that Rosarian wine with you, I did it because I wanted you to enjoy yourself, to cut loose and have fun. Isn’t this what you wanted for me with the Firegrout?"
ro "Sometimes, it's okay to cut loose."

"Greyhide stared at the bottle for several seconds, then looked Rowan in the eyes again."

gh "I will… think on what you have said."

"Rowan gave a gentle smile, patting his friend reassuringly on the back."

ro "Let’s just enjoy the moment, huh?"
ro "How about another drink?"

scene black with fade 
pause 2

scene bg22 with fade
show rowan necklace happy at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve

"The Firegrout hit Rowan harder and faster than he would have ever expected." 
"The last time he drank with Greyhide, he’d had a few bottles of wine over the course of several hours. Here, he finished most of the flask in half an hour, and already he felt woozy."
"A strange feeling engulfed him, like fluffy pink cobwebs enshrouding his higher thought functions."

ro "Youuu know what? This ish shome great stuff."

gh "So you… keep saying."

"Greyhide, for all his faux-indignance, was deep in his cups as well. He’d finished off a fourth flask while Rowan wasn't looking, and was already working on a fifth."

ro "Aw, come on, {i}really{/i}?"
ro "Why the-"
ro "W-why the- "
ro "uh..."
ro "Wh-{i}why{/i} the rush, Greyh-uh… guy?"
ro "We got {i}aaaaaall{/i} night to enjoy ourshelves, eh? No need to get {i}schuper{/i} drunk!"

gh "I would… rather… forget."

ro "{i}Pffff{/i} why?"

gh "I would… rather not say..."

ro "Ah, come on, itsh me! "

"Rowan poked him in the chest, chuckling at how uncomfortable Greyhide seemed with his gentle prodding."

ro "Row-han! Yer ol’ friend! Hero of Rosharia! Loyal {i}ssshhh{/i}-ervant of the Twins!"

"Rowan elbowed Greyhide in the arm, laughing at how he jolted in place next to him on the bench. He really was a big softie at heart."
"Greyhide huffed and rubbed at his eyes, taking care to try to hide it from Rowan."

ro "Aw, come on man. Don’t cry! Itsh just a bit of fun!"

gh "It is not… that."

if alexia_greyhide_sex == True:
    gh "It is just… I… your wife…"
    ro "Alexshia? Yeah, she’s a schweetie, huh?"
    ro "I’m glad you two hit it off."
    gh "..."
    ro "You deserve to be ha- {i}huh{/i}… h-happy, Greyhide!"
    gh "Not like… this..."
    
else:
    gh "It is just… your wife… I almost…"
    ro "Wuh? Alexshia?"
    ro "She say somethin’ about you?"
    gh "No… nothing like... that."
    gh "It is… my fault."
    ro "Ahh, you’re just too hard on yourshelf."
    
"The Minotaur put his head in his hands."

gh "I do not know… what to do..."

"Rowan put a hand to Greyhide’s shoulder and gently patted it."

ro "Hey, hey, wotsh all this about?"

gh "I am… a beast… I cannot stop... myself."

"A beast?! Now Greyhide was making Rowan mad. Mustering the kind of courage that could only come from profound inebriation, Rowan shook him hard and forced Greyhide to look him in the eye."

ro "Hey! {i}Hey{/i}! You don’t shay that kind of schtuff, huh?"
ro "You aren’t a beast and that’s the end of it! You’re a good man."

gh "You are… too kind."
gh " I do not… deserve this… kindness."

ro "Thatsh just the liquor talking. And he’s an asshole! He made me drink him too!"

"Rowan knew a thing or two about drinking. He’d never felt {i}quite{/i} like this during his other, infrequent bouts. In fact, he’d never been quite so warm. Quite so uncomfortable."

gh "You do not… understand. I…"
gh "I am trying… so hard... to hold back."

"At this, Rowan drew close, putting a hand atop his larger mitt. He wasn’t about to let Greyhide wallow in self pity. Not with those big, brown eyes of his."
"...Wait, where did that come from? Rowan’s cheeks burned in embarrassment."

ro "You aren’t a beasht, Greyhide."

menu:
    "You’re a man. (Kiss him)":
        $ released_fix_rollback()
        "Rowan wasn’t thinking straight. His hand moved on its own, cupping the side of Greyhide’s snout and tilting it to face him."
        "He saw the uncertainty, the fear in the old bull’s eyes. He wanted to do something about it."
        ro "...You’re a man."
        "His lips pressed against the tip of Greyhide’s snout, the leathery texture a fascinating contrast to any mouth he’d ever kissed before."
        "He pulled away, his eyes lidded low as he fixed his friend with a drunken smile."
        gh "Rowan..."
        ro "Hah, I- oof, think I might have had too much to drink."
        "The Minotaur froze, his body caught in limbo as Rowan pulled his heavy frame closer."
        gh "I… you are… so fragile…"
        gh "Wait, I… apologize. I think your… body is beautiful."
        ro "So is yoursh."
        show rowan necklace aroused at midleft with dissolve
        "Rowan’s cheeks were burning. There was a fire in his gut, spreading outwards to the rest of his body, enflaming his senses and numbing his mind. It didn't help that he was feeling pretty hot under the collar as well."
        ro "*Hic*"
        ro "Wow, that stuff goes through you fast."
        gh "I have… never felt that before…"
        gh "That was… a kiss?"
        ro "Yeah."
        gh "I enjoyed that."
        ro "Me too."
        "Greyhide shifted uncomfortably in his seat, stealing glances at Rowan and adjusting his garment about his waist."
        gh "I have... hesitated to act on this. I don’t… want to… "
        "The beast let out a low grunt, almost a growl in the back of his throat."
        gh "I cannot... lose control again."
        gh "But… I desire you… friend Rowan."
        ro "The feelingsh mutual."
        gh "May I… have another?"
        ro "A kiss?"
        "Greyhide swallowed, unable to bring himself to say yes. He gave a curt nod, his horns swaying as he bobbed his head. It was everything he could do to not to throw himself at Rowan in that moment."
        "Rowan smiled, leaning in and planting another kiss upon the Minotaur’s lips. His heavy breath sighed out as if a great weight had fallen from his shoulders."
        ro "Oh, haha. That wash a good one."
        gh "I want to... see you. Feel you… Taste... you."
        "How had things escalated so quickly? Rowan struggled to make sense of it in his head. It was hard to focus. All he could comprehend was his breathless attraction to this gentle giant."
        ro "*hic*  With how big that bulge is, I doubt you're getting inshide me."
        gh "I… do not mind."
        ro "Show me what you've got."
        scene cg443 with fade
        pause 3
        show rowan necklace aroused behind cg443
        show greyhide neutral behind cg443
        "Hardly had those words left Rowan's mouth, than Greyhide was pulling his breastplate vest up and over his body."  
        "Instantly the man's eyes were drawn to the enormous throbbing member that now stood at full height."
        ro "Woah. That’sh big. Even bigger than I thought it'd be."
        gh "Let me… see yours."
        "Rowan didn’t give much thought to what he was doing. It was easier to just go along with what was happening."
        "Rowan quickly peeled his clothing off and held his arms out theatrically. He was hard. Painfully so. The situation seemed odd somehow, but the hero paid it no mind."
        show rowan necklace naked aroused behind cg443
        gh "Beautiful."
        ro "Thaanksh! I’m quite proud of it!"
        "Greyhide’s eyes were locked to his. There was something distinctly bestial in his gaze. He was breathing heavily, his thick chest lifting and lowering as he let out a low rumble in his chest."
        ro "Uhh… Greyhide?"
        ro "Eh?"
        scene cg108 with fade
        pause 3
        show rowan necklace naked aroused behind cg108
        show greyhide neutral behind cg108
        "The horny Minotaur reached out and took him by the shoulders, lifting Rowan up completely off the ground. He carried the drunken hero like he was a rag doll across the room, clambering up onto his desk."
        "He laid down on the table spinning the man around and laying him out across his well muscled chest."
        ro "Woah! Ha ha ha!"
        "That giant manhood filled his vision, a throbbing pillar of masculinity. He could see the sizable heft of his fuzzy balls beneath."  
        "There was a tickling sensation, the feeling of hot breath against Rowan’s nethers. He craned his neck back to see Greyhide examining his ass and exposed nethers."
        "Well, ‘when in Rosaria,’ as the saying goes…"
        "Rowan reached out to stroke his friend's member. In response, something warm and wet started playing over the skin around his groin, paying particular attention to his scrotum."
        "Greyhide’s tongue was hot, and wet, and… and {i}long{/i}! Gods, it was enormous. Almost as big as the cock in front of him. Rowan was sure he’d have little trouble wrapping that thing around Rowan's cock. The idea was imminently appealing."
        menu:
            "Encourage Greyhide to go for your ass.":
                $ released_fix_rollback()
                "As it turned out, the Minotaur didn’t need any convincing. Before Rowan could even say anything, Greyhide’s tongue had traced a path up and over his asshole."  
                "The sudden, wet feeling of against his rear caused Rowan to inhale sharply in response."
                "Greyhide was not fazed when Rowan clenched up. His large hands started massaging the man's toned asscheeks with his thumbs. Little by little, Rowan relaxed until he finally allowed his long bovine tongue to invade his backdoor."
                "Rowan, not about to be outdone, took to his new task with gusto. He kissed the head of the Minotaur’s bestial cock, marveling at it’s strange contours."
                "Greyhide’s tongue was hot, wet and insistent. It curled across his buttcheek as he lathered Rowan’s rump in his saliva, marking him as his. The sudden stimulation drove Rowan wild, making it impossible for him to focus."
                "Rowan licked the shaft, jerking the beast as his leathery skin bunched and bulged between his fingers. His head swam with erotic need."
                "Greyhide’s proving tongue slid inside him, wriggling about as it sought Rowan’s deeper spaces. He was left gasping at the sensation, all but clinging to Greyhide’s cock as he did everything he could to bring him to a quick finish."
                "Then, almost as suddenly as it had started, the two reached their climax. Greyhide seemed to sense that Rowan was at his peak, lifting him up over his head as he brought the man to an anal induced climax."
                show cg108 with sshake
                show cg108 with sshake
                show cg109 with flash
                pause 2
                "This was enough to push Greyhide over the edge. He grunted, letting out a pleasured groan as he jerked his hips upward. Rowan kissed the base of his cock, watching in awe as it pumped a truly massive load into the air."
                "It fountained upwards, costing Greyhide’s own chest with the fruit of his sticky love."  
                "Greyhide's arms gave out, and Rowan fell forwards onto the warm stains of white, marveling at the virile sensation of being surrounded by bull cum."
                "The two simply lay there for several moments, panting with exhaustion at the unexpected surge of passion the two men had shared. A wave of dizziness overcame Rowan and he put a hand to his forehead."
            
            "Have Greyhide get a taste of your cock.":
                $ released_fix_rollback()
                ro "Y-you know you want to taste it."
                "Greyhide didn’t answer, he merely grunted."
                "A moment later, Rowan felt the slick slide of his fat, wet tongue engulf his dick.  This elicited an approving moan of pleasure from the human."
                "It was a transcendental feeling; the warmth of the Minotaur’s mouth sent shivers down his spine. He basked in the pleasure of their entanglement for a few blissful seconds."
                "However, Rowan wasn't the only one in need of stimulation. Never one to shirk his duty, Rowan began jerking and teasing the massive meat that was in front of him." 
                "It was huge, hard going, and arduous work… but Greyhide’s warm tongue made it all worth it."
                "Caught up in the moment, Rowan began to worship it with his mouth, alternating between licking and nibbling on the tip."
                "Greyhide's impressive length was surprisingly convenient for their current position, as he was able to easily sixty-nine with someone so much shorter than him."  
                "When some doors closed, others opened: he might not fit in Rowan’s ass, but he sure could have fun with his mouth!"
                "As if reading his mind, the Minotaur jerked Rowan backwards. Rowan gasped as his cock dropped straight down into Greyhide's maw!" 
                "The shock of the sudden suction and engulfment pushed him over the edge and he let loose a few spurts of seed down the randy beast’s throat."
                show cg108 with sshake
                show cg108 with sshake
                show cg109 with flash
                pause 2
                "Apparently this was enough to push the Minotaur over as well. Greyhide grunted, letting out an impressive howl as he jerked his hips upward, the skin of his cock bunching between Rowan’s fingers."
                "He humped and pumped and came, spurting an impressive coating of semen all over his own chest."  
                "Then Greyhide's arms gave out, and Rowan fell forwards onto the warm stains of white."
                "The two simply lay there for several moments, panting in sudden exhaustion as a wave of dizziness swept over him."
        scene bg22 with fade
        show rowan necklace naked aroused at midleft with dissolve
        show greyhide neutral at cliohnaright with dissolve
        gh "That was… {i}hrrrh{/i}..."
        ro "*hic*"
        ro "Intenshe?"
        gh "Y-yes…"
        "Greyhide shook his head back and forth, dazed in the aftermath. He looked around the forge, his breath shortening as he took in the scope of the room."
        gh "We… I…"
        gh "Oh gods… what did we do?"
        "Weird. The fog around Rowan’s mind hadn’t really let him properly consider what was happening in the moment. But now, once the post orgasmic bliss began to recede…"
        ro "W-whuh? Wha- whashappenin?"
        "He…" 
        "Did he just have sex with Greyhide?"
        "Rowan blinked repeatedly. His mind was made of sludge. He got up off the bull’s chest with a drunken stagger."
        if alexia_greyhide_sex == True:
            gh "No…"
            gh "{i}No{/i}! Not… again!"
            ro "Greyhide?"
        else:
            gh "What have I…"
            gh "What did... we…?"
        "The bull let out a gasp and leapt to his feet. Rowan was startled at the speed with which he could move." 
        "Naked, Greyhide rushed over to his anvil, yanking the towel he had hanging off the edge and hurriedly wiping himself down."
        gh "I am… sorry. I… you must go."
        ro "Hey, watsh wrong?"
        "The surreal reaction caused Rowan to glance down at himself. Naked, his back coated with the remainder’s of the Minotaur’s hot load. Something was off about all this, but he couldn’t quite figure it out."
        gh "Please, friend Rowan… I… I did not intend… for this."
        "The Minotaur circled around Rowan’s back, gently wiping him down before collecting the heap of Rowan’s discarded outfit and pushing it into his arms."
        ro "Itsh okay, Greyhide. Jusht take a second and-"
        gh "I-I need to… get back… to work!"
        scene black with fade
        "Startled, Rowan was all but shooed out of the room. Greyhide gave him just enough time to pull on his trousers before the door slammed shut behind him."
        "Rowan, drunk and disheveled, was left to stumble to his room. Thankfully, it was late enough that no one saw his impromptu (and wholly unexpected) walk of shame."
        $ rowanGreyhideLiquorSex = True
        $ rowan_non_alexia_sex += 1
        $ change_base_stat('c', 2)
        jump peopleLiquorEnding
        
    "You are my friend.":
        $ released_fix_rollback()
        "Rowan did his best in his drunken state to flash Greyhide a winning smile."
        show rowan necklace happy at midleft with dissolve
        ro "You are my friend. And I won’t schtand for all this beasht crap."
        ro "Friends gotta- {i}oof{/i}, schtick together, huh?"
        ro "Thats why it’s called ‘friendssssship.’ Cause we sssss-chtick together."
        "Greyhide leaned in towards Rowan, his eyes lidding. It took him several seconds for him to realize just how uncomfortably close he had gotten. He shook himself, his lips twisting into a fearful frown."
        ro "...You okay, friend?"
        gh "I… I cannot do… this."
        if alexia_greyhide_sex == True:
            gh "Not… again."
        ro "What are you talking about? You’re sho serious!"
        ro "Ha ha, come on: another drink, see if we can’t beat our record, eh?"
        "But something had changed in the bull’s demeanor. Perhaps it was just Rowan imagining things, but he seemed almost… frightened of him?"
        "Greyhide rose to his feet, tossing the half-full flask of Firegrout across the room with uncharacteristically careless force." 
        ro "Woah! What is-"
        gh "You… you must leave… friend Rowan."
        gh "Please… I cannot-"
        "The Minotaur half-stumbled towards his anvil, picking up his hammer as if to return to forging."
        gh "You must go. Still… so much to do."
        ro "But itsh so late-"
        show rowan necklace shock at midleft with dissolve
        gh "{i}Go!{/i}"
        "His desperate shout startled Rowan from his stupor. He rose, sensing that the bull was saying it more for Rowan’s sake than for his own."
        ro "O-okay, I’ll… shee you later, Greyhide."
        scene black with fade
        "Greyhide did not respond, staring down at the hammer in his hand as he steadied himself on the anvil. It was clear he was in no condition to continue working, but Rowan could sense the mood had changed."
        "Rowan left, abandoning the forlorn blacksmith to his lonely vigil. He retraced his steps, drunkenly stumbling back to his bed. He was too addled to consider the matter properly in the moment, but he resolved to think more on what had happened in the morning."

label peopleLiquorEnding:

scene bg9 with fade
show rowan intro necklace neutral at midleft with dissolve
    
"The next morning, Rowan awoke with a splitting headache, and the profound revelation that something had gone wrong the night before."

ro "Ugh, that wasn’t… any normal drink."

"He’d been drunk before, but never with that kind of sensation. It was like all his inhibitions had drifted away, he had been left bare, open to any impulse that might strike his fancy."

if rowanGreyhideLiquorSex == True:
    "…such as sleeping with a Minotaur."
    
"The pink clouds in his mind might have cleared, but he was far from back to normal. Looking at his hands, he could see that they still tremored. How could a single flask of spirits cause such trouble?"
"Memories of the night before spilled into his head. Greyhide had been desperate for him to leave. He had been just as caught off guard as Rowan by what had happened."
"Something was {i}very{/i} wrong with that drink. As soon as his duties gave him the chance, Rowan would get to the bottom of this."

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label jezera_is_stressed:
#Jezera is stressed
#No requirements.

scene bg6 with fade

show rowan necklace neutral at midleft with dissolve
show jezera happy behind bg6

je "-Rowan, be a darling and come up to my room, I need some help unwinding."

ro "What exactly do you have in mind?"

je "Oh, just a massage from handsome company."

ro "... and?"

je "Well, maybe I'll tease you a bit too. You'd rather have a playful mistress than a grumpy one, wouldn't you?"

menu:
    "Tell her you're too busy.":
        $ released_fix_rollback()
        ro "Now really isn't a good time. You only give me a day to do all this work, you'll probably be a lot grumpier if I don't get it done."
        "There was no answer for a painfully long moment."
        show jezera neutral behind bg6
        je "Fiiiine. I'd have thought you'd have jumped at the chance to touch a lady's fine skin, but you just take care of those duties of yours then. I'll find someone else."
        "Rowan let out a breath he hadn't realized he was holding, then waited for several more moments before returning to his work."
        "Jezera wasn't as overtly frightening as her brother was, but that just meant she could be intimidating in other ways. Who could say when she felt offended?"
        #note rowan's refusal to give a massage
        $ jezera_is_stressed_massage_refusal = True
        return

    "Go up to Jezera's room.":
        $ released_fix_rollback()
        jump rowanJezMassage

label rowanJezMassage:

$ rowanJezSex =+ 1

ro "Alright, on my way."

je "Excellent."

scene bg14 with fade
show rowan necklace neutral at midleft with moveinleft

je "Enter."

"Rowan stopped, his hand raised about to knock on the door."
"Of course, since Jezera was expecting him, she'd been watching his position. It made sense that she knew he was there."

scene bg18 with fade
show jezera naked happy at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

"Entering into the finely decorated room, he found Jezera was laying down on her bed, propped up on one arm and running the other up and down her body enticingly."

je "I'm so glad you weren't too busy to come by and help me out."

"She let out long groan, then exaggeratedly stretched out."

je "Today was a damn frustrating one, so I just need a chance to unwind.  Come over here and give me a well deserved massage."

#massage CG
scene cg370 with fade
show jezera naked happy behind cg370
show rowan necklace neutral behind cg370
pause 3

"Knowing better than to keep his mistress waiting, Rowan immediately stepped next to the bed where she'd rolled onto her chest and placed his hands onto her back."

show cg371 with dissolve
pause 3

"Right away he noticed that her flesh was unusually soft and felt more pliable than normal human flesh. Yet there were no creases and no wrinkles, just perfect violet skin."

je "Hmm? Come, my hero, put some force into it. I am not so delicate that I'll snap in two if you don't restrain yourself."

"Deciding to test that limit, if just for a moment, Rowan put the whole of his upper body weight down on his hands. Then dragged them down between her shoulder blades. A long reassuring sigh was his response."

show cg372 with dissolve
pause 3

je "Oh, yes. That's much better."

show cg373 with dissolve
pause 3

"Demon, the man reminded himself, trying to put the same weight behind his touch as he continued the massage. This was difficult going and wore him down rather quickly. So he tried moving onto her arms instead."
"Abruptly Jezera rolled over onto her back, locking eyes with Rowan."

je "Nah, could you give my chest a massage instead? They're just so tender and perky right now."

"He hesitated, unsure what of make of this. Was it a proposition? Did she want to see how he'd interpret this?"

scene cg214 with flash
show jezera naked happy behind cg214
show rowan necklace neutral behind cg214
pause 3

je "Too slow, too slow."

"Or maybe she was just looking for an excuse to move onto something else. In an instant, Rowan had found himself completely tied up in magical bindings of blue light."

ro " I-"

"One of the tendrils wrapped around his face, cutting off his voice."

je "Shh. Now it's time for me to have some fun."

"Rowan was pulled forward up onto the bed and deftly freed of his garments as Jezera leaned back onto her arms and reached out with her toes to caress the man's cock."

scene cg872 with fade
pause 3
show jezera naked happy behind cg872
show rowan necklace neutral behind cg872

je "How does that feel? Hah, I love seeing you squirm around like that."

"Her teasing was ever so light, just barely touching him. Try as he might, there was no way that Rowan could either pull free, or get her to touch him more fully as he grew harder and harder.  The hero was fully in his captor's power."
"Now the demon's second foot came up and curled around the glans while the other continued to brush up and down Rowan's length. Still, she kept taking it slow. Such a pace was agonizing, Rowan couldn't help but let out a bit of a whimper."

je "Aww, is something wrong? You look like you're enjoying this."

"It did feel good to have those small, taloned toes touch him, tease him, toy with him. He wanted more. That was probably what Jezera wanted him to feel, but Rowan couldn't tell if it was his own desires or those which had been foisted on him."

je "I bet you'd like this too."

"Finally seeming to be done with the prelude, the demoness repositioned her feet so that one was on either side of Rowan's cock, toes up and pointed to his belly, and let him slide up through the gap between them."
"Rowan gave a satisfied grunt, now that the teasing seemed to be at an end.  Even still, Jezera took it slow.  Her violet souls went up and down a gentle steady pace."

je "Looks like you do, but what's with that face? Wanna cum? I bet you do."

"Her movements remained steady however, as she locked eyes with her servant."

je "In a moment, I'm going to take off your gag. I only want to hear three words from you, my hero, okay?"

"A grunt was the only answer Rowan could give."

je "Good, now say, 'Yes, mistress Jezera.' Do you want to cum?"

"The tendral came away."

menu:
    "Do as she wants.":
        $ released_fix_rollback()
        show rowan necklace naked behind cg214
        ro "Yes mistress Jezera."
        "Then his mouth was blocked again."
        je "Good boy.  Now, about your reward..."
        "At long last the pace increased, quickly driving Rowan towards his peak."
        show cg873 with sshake 
        show cg873 with sshake 
        show cg874 with dissolve
        pause 2
        show cg875 with dissolve
        pause 2
        show jezera naked happy behind cg875
        "Only a few moments later he felt his insides clench and let loose his seed over the soft flesh of Jezera's feet. She didn't let up her stroking until a moment after he'd finished, just before it started to hurt."
        je "I see you really like every part of your mistress, from top to bottom. There's still so much fun we will have together."
        "After wriggling her toes for a moment and working the white goo he'd covered them with in, she pressed the big one into his chest and drew a circle. A trail of cooling liquid was left in the wake."
        scene bg18 with fade
        show jezera naked happy at midright with dissolve
        show rowan necklace naked at midleft with dissolve
        "The tendrils of power retreated, releasing Rowan and allowing him to gather up his clothes."
        je "Well, I am thoroughly relaxed and satisfied now. Thank you, my hero, you are dismissed."
        #gain favour with Jezera
        $ change_favor('jezera', 1)
        return

    "Deny her.":
        $ released_fix_rollback()
        show rowan necklace naked behind cg214
        ro "I'm not saying it."
        "Then his mouth was blocked again."
        #denial cg
        scene cg875 with fade
        show jezera naked happy behind cg875
        je "I guess then you don't want to cum. Well, I'm fine either way."
        "Her teasing didn't let up, if anything it adopted a pace that was intended to bring Rowan to the edge again and again, but then relax just before he hit his peak. It seemed that Jezera took great pleasure in this, constantly taunting him each time she did so."
        "Denying Rowan seemed like it was actually getting her off, as the demoness started to touch and run her fingers over her womanhood as the torture continued and brought herself to orgasm on at least two occasions."
        scene bg18 with fade
        show jezera naked happy at midright with dissolve
        show rowan necklace naked at midleft with dissolve
        "As she promised, the man never came. He simply was set down about an hour after he'd been summoned."
        je "Well, I am thoroughly relaxed and satisfied now. That is the important thing. Gather up your things Rowan, you are dismissed."
        "Rubbing a bit of feeling back into his limbs, Rowan scooped up his clothes and started towards the door."
        je "Oh, just so you know, today is going to be an inspection day. I hope you focus extra hard on your work and don't get caught up in any further pleasure seeking. You will have a very cross mistress if I catch you trying to get off today."
        #gain favour with Jezera
        $ change_favor('jezera', 1)
        return


