init python:
    
    event('alexia_nileth', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'", "alexia_knows_magic", "arzylDialogueStage > 2",), group='alexia_library', run_count=1, priority=pr_npc)
    event('library_lovers_1', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), group='alexia_library', run_count=1, priority=pr_npc)
    event('library_lovers_2', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), depends=('library_lovers_1',), group='alexia_library', run_count=1, priority=pr_npc)
    event('library_lovers_3', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), depends=('library_lovers_2',), group='alexia_library', run_count=1, priority=pr_npc)
 
label alexia_nileth:

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve

"Alexia always felt a sort of watchful discomfort when walking through these particular bookshelves. It was late in the day, and she had been assigned to the magical section of the library." 
"It was a place where a book was as likely to come to life and devour your research as it was to teach you a useful spell." 
"Cliohna might feel comfortable strolling through these halls as one would through an aromatic garden, but Alexia - despite her own growing magical knowledge - was wary in the extreme."
"So it came as some surprise to her when a creature out of a children’s fable appeared amongst the bookshelves."

show nileth neutral at edgeright with dissolve

"He was a small thing, going almost unnoticed when she strode between the rows. Only the multicolored glow of his gossamer wings had tipped her off that he was there."
"He walked up the aisle facing away from her, his hands folded behind his back as he took gentle steps, reading the spine of each book he came across. A soft smile graced his lips, as if he were reminiscing about an old friend while he read."

al "Um… hello?"

"The strange fairy creature tensed, his wings flapping wildly as he spun around to face her. His eyes went wide, and he held his hands up as if to protect himself."

#nil concerned

nil "{i}Ah{/i}! By Kassandra’s eternal mercy!"
nil "I-I’m sorry, I didn’t see you there."

"Alexia kept her distance. If her time studying the occult had taught her one thing, it was that appearances could be deceiving." 
"She had no idea who this being was, if he was a real creature, or if he was some spectral projection cast by one of the (very much alive) books on the shelf."

al "Who are you?"

#nil happy

nil "Oh! A polite mortal! How refreshing."
nil "My name is Nileth. Pleased to meet you!"

"His smile was innocent. His body posture almost childlike in stance. But, Alexia nevertheless kept her distance." 
"He had a strange, otherworldly nature about him. Simultaneously ancient and youthful. There was more to this creature than meets the eye."

#nil neutral

nil "I’m sorry for reacting like I did. I didn’t hear you sneak up on me."

al "I didn’t sneak up on you."

#nil sad

"Her words deflated him for some reason. He hunched his shoulders, muttering to himself in some strange, foreign tongue."

nil "Of course… I guess I’m just not used to being caught off guard by mortals. Usually only my mistress does that."
nil "But ever since Arzyl cursed me, I haven’t been able to-"

al "Arzyl? Arzyl the witch?"

"Nileth nodded at her, his delicate wings fluttering behind him as he hovered. "

al "You’re one of the Fae?"

#nil happy

nil "I am! I hadn’t expected our presence here to be common knowledge around the castle yet."
nil "Pleased to meet you, Miss…?"

show alexia librarian happy at midleft with dissolve

al "Alexia."

#nil shocked

nil "Oh! You’re Rowan’s wife?"

"Now it was Alexia’s turn to be surprised. She felt her stomach turn at the ease with which he had identified her."

show alexia librarian concerned at midleft with dissolve

al "...Yes. How do you know that?"

#nil neutral

nil "My Lady Arzyl told me you were here in the castle."

"Alexia wasn’t sure how happy she was to learn how well known she was in Castle Bloodmeen. The Fae were relative newcomers, and yet she was already the subject of court gossip."
"..Goodness knows what else they knew."

show alexia librarian angry at midleft with dissolve

al "What are you doing in our library, Nileth?"

#nil shocked

nil "O-oh! Am I not allowed to be in here? Lady Arzyl didn’t mention any restrictions about this part of the Castle."

"The Fae glanced up at the row of spell books sitting on the shelf above his head, a tremulous smile building upon his youthful features."

#nil happy

nil "I’m sorry, I was just marveling at all the magical tomes you have stored here! You’ve got quite the collection."

show alexia librarian neutral at midleft with dissolve

al "If you intend to borrow a book, you should check in with Cliohna first."

nil "Oh, I wouldn’t want to trouble her, I’ve read most of these already. It was just a rare treat to see so many gathered together again in one place."
nil "You see that one?"

"Nileth pointed to a particular book, with a blue, wavy cover the texture of seaweed."

nil "That is a replication of the spellbook of Ursaali the Sea Witch. They say she was so powerful in the art of water magic that she could actually change the tides of the sea itself. She brought hurricanes and shifted the coastlines at her whim."
nil "She supposedly sank an entire continent that once existed off the coast of the Dragon’s Tail, because the men of the region dared to spearfish near her coral palace! Legend says she married a Marlin-man, and rode a tamed sea-dragon as her steed."

show alexia librarian shocked at midleft with dissolve

al "...Is any of that true?"

#nil happy

nil "Probably not. But it makes for a fun story, don't you think?"

"Despite herself Alexia found herself smiling. There was a charming sort of earnestness in the little Fae’s personality. She began to relax: if he was indeed a threat, he was doing a great job of concealing his motives."

#nil neutral

nil "The spells in the book, however, are very real."

show alexia librarian neutral at midleft with dissolve

al "I learned a bit of water magic myself, recently. I am no Sea Witch, but-"

#nil happy

nil "Oooh! Could you show me?"

"Alexia considered the idea. She {i}had{/i} been looking for opportunities to display her newfound powers. And the Fae seemed to be a harmless enough sort."

show alexia librarian happy at midleft with dissolve

al "Okay. Stand back."

"Using the methods that Cliohna had shown her, Alexia drew upon her power. She brought her hand up, her palm glowing with raw energy."

show bg12 with flash

show alexia librarian shocked at midleft with dissolve

"It was only after the bolt of ice was free from her hand that Alexia realized she had put too much into the shot. A thick spear of ice far larger than she had been expecting leapt from her hand."
"It threw off her aim, causing the bolt of magic to fly directly past the astonished Nileth’s head."

#nil concerned

nil "{i}Aaah!{/i} Seven Agonies!"

al "{i}Ah!{/i} Are you okay?"

"Nileth’s wings fluttered at a hummingbird’s pace. He had only just managed to dodge out of the way of Alexia’s magical might. He now hovered several feet above her, staring down at her with a mixture of surprise and awe."

#nil happy

nil "Gosh Alexia, was quite the bolt! You darn near clipped my wing off!"

show alexia librarian concerned at midleft with dissolve

al "I am so sorry, Nileth!"

nil "You don’t have to apologize. That was a very impressive spell."

#nil neutral

nil "{i}Maybe{/i} you could work on your aim, though?"

"His wide smile made Alexia cover her mouth to hide her laughter. He reminded her almost of a cavorting jester who had passed through Arthdale in her youth."
"He had been a silly fellow: all ridiculous expressions and tumbling buffoonery, but he had made the children smile, and he had always been kind to her. Nileth wore his same, eager grin."

nil "Tell you what, why don’t I give you some pointers! You have quite a skill there. Maybe just a bit... rough around the edges."

show alexia librarian neutral at midleft with dissolve

al "Pointers?"

nil "Well, did you see how you kept your stance so wide? You drew  too much energy into you at once, and didn’t know where to put it. It’s why that ice nearly took my head off."
nil "Notice too that you’re now out of breath. You expended too much energy for too little gain. You can get the same deadly effect from a Ice Shard with less effort."

al "...Really? How?"

nil "It’s all in the stance. Look: If you just narrow your hips, like so…"

"It took several minutes of effort for Alexia to get what Nileth was getting at with her stance. But he was patient with her, gently nudging her torso in one direction while positioning her arm." 
"His touch was gentle, his body moving in graceful circles around her as he sized up her spellcasting talent."

nil "So you see, when you let the energy flow {i}through{/i}-"

"A far slimmer, far sharper Ice Shard leapt forth from Alexia’s hand like it had been hit with a sudden gale. It flew down the corridor of books at a speed that astounded the would-be mage. Alexia’s jaw dropped."

show alexia librarian happy at midleft with dissolve

al "I did it!"

#nil happy

nil "Amazing!"

al "I really did it!"

"Nileth did a little swoop with his wings, pirouetting in the air, displaying his honest excitement through flight. He landed on his toes, fluttering in the air as he smiled that wide, innocent smile at her."

nil "Ha ha ha!"

al "You’re a really good teacher, Nileth. Are you a mage yourself?"

#nil neutral

nil "Oh, no. I don’t do magic anymore. Arzyl would {i}never{/i} allow that."

show alexia librarian neutral at midleft with dissolve

al "She won’t... ‘allow’ it?"

"Nileth nodded, flashing Alexia a nervous grin that told her there was more to the story than mere ‘allowance.’"

nil "I am Arzyl’s servant. It wouldn’t do for me to practice spells behind her back."

al "...Is she your Lady, or your owner?"

"Nileth shrugged, his wings fluttering as he hovered in the air."

nil "Both, I suppose."
nil "Besides: I no longer have any magical talent to speak of. But I haven’t forgotten the basics. It’s a skill, just like any other. Once you know the tricks, it's easy to teach others."

al "Wait, you don’t have any magical ability yourself?"

"Nileth shook his head. Alexia couldn’t wrap her head around the idea. How would one go about ‘losing’ their magical abilities? She had never heard of such a thing."
"She was about to ask him something more, but a small, glowing creature buzzed up between them both."

dag "Hey! Get your grubby little mitts off the walking sperm bank, would ya?"

show alexia librarian angry at midleft with dissolve

al "What the hell?"

#nil happy

nil "Oh, that’s Daggertongue. My Imp friend."

dag "Friend, nothin’. I’m just here to make sure you don't end up on the wrong end of an Orc gangbang again."

nil "Hello, Daggertongue!"

dag "Yeah, hey. Hello. What are you doin’ in here, Twinky?"

"If Nileth was bothered by the Imp’s insulting tone, he didn’t show it. He smiled at the Imp as if he was an old drinking buddy, gesturing in the direction of Alexia as he fluttered in the air."

#nil neutral

nil "Daggertongue, let me introduce you to my new friend Alexia. She’s-"

dag "Yeah, hello toots."

"The Imp spared less than half a glance in Alexia’s direction before he rounded on the Fae."

dag "D’you know how long its been since Lady Arzyl has heard from you? Sol’s Bones, if I hadn’t found you sooner, you was gonna be {i}late{/i} for your daily ‘session,’ if you catch my drift."

#nil concerned

nil "I-I wasn’t gone for long! I was just showing Alexia-"

dag "-Your fat ass as you fly outta here. I know. "
dag "You need to get back to Arzyl, and pronto. Cause I am {i}not{/i} takin’ the punishment she’s gonna dish out to you if you’re not around when she comes calling."

"Nileth wilted into himself. The strength went out of his wings, his shoulders sagging as he let out a tired sigh. Alexia frowned, seeing the wind go out of her newfound friend’s sails right before her eyes."

#nil sad

nil "Of… of course. Thanks for looking out for me, Daggertongue."

dag "Don’t mention it. Now make like a shepard and get the {i}flock{/i} outta here."

"Nileth’s wings lifted him off the ground and he flew for one of the high windows in the library. He glanced back at her one last time and gave a wave and a small smile."

#nil happy

nil "It was nice to meet you, Alexia."

show alexia librarian happy at midleft with dissolve

al "It was nice to meet you too, Nileth."

"The Fae lifted off the ground, floated away into the rafters. He spared a last, nervous glance back in the direction of Alexia, who waved as he left. She saw him smile."

hide nileth with dissolve

"Then, like a flash of fairy dust, he was gone. She was alone with the angry, glowing Imp. Daggertongue fluttered in the air for a long moment, his eyes trained to the distance as if waiting to make sure Nileth was gone."

dag "Listen, toots. For your own sake: keep well away from that little rainbow twinkle. That guy? He’s trouble."

show alexia librarian neutral at midleft with dissolve

al "He seemed nice enough to me."

dag "‘Nice’ ain’t got nothing to do with it."

show alexia librarian angry at midleft with dissolve

al "And who are you to tell him what to do? He didn’t do anything wrong. We just met, and he {i}helped{/i} me."

dag "Oh I’m sure he did, toots. He’s got a bad habit of helpin’ people he shouldn’t be helpin’. Tends to end poorly, for all parties involved. Just look at me."

show alexia librarian neutral at midleft with dissolve

al "What’s that supposed to mean?"

dag "Nothin’ you need to worry your big red head about. You see Nileth again? You keep on walking. S’better for everybody that way. Including him."

"And just like that, the Imp shot off into the air after his erstwhile companion, leaving Alexia confused and alone in the row of bookshelves, wondering what exactly had just happened."

return

##############################################################################################
##############################################################################################
##############################################################################################

label library_lovers_1:

scene bg12 with fade
show alexia librarian happy at midleft with dissolve

al "{i}Hmmm{/i} hmmm hm!"

"Work in the Library could often be a droning, dull affair. But not today. Today had seen Alexia awaken with a spring in her step and an eagerness to work."
"She spent the first few minutes thumbing through one of the thousands of unsourced books lying in piles in the storage section of the Library before taking it upon herself to continue the eternal task of organizing."
"Alexia hummed an old village tune to herself as she strolled from aisle to aisle, her eyes sweeping across the pleasing contours of the row upon row of books. A wide smile crossed her face as she marveled at the sheer breadth of knowledge that was available at her fingertips."
"She strolled into a more remote section of the library. It was covered in dust, ancient cobwebs piling around the corners and cluttering the tops of shelves like the mummified vestiges of some mythical empire of spiders."
"She set to work, stacking books and organizing shelves as she hummed to herself, feeling a kind of verve and energy she had not often had in these dire days."
"The intrigue and relentless machinations of the Castle had sapped so much from her as of late… it was good to finally indulge in some simple, uncomplicated-"

show alexia librarian shocked at midleft with dissolve

quest "Cla-Yil? Cla-Yil, are you there?"

"Alexia tilted her head in confusion. The voice was vaguely familiar to her. It was a man’s voice, coming from a few shelves over. She almost called out to him, but stopped short when she heard another voice respond."

quest "I’m here, Rickon."

"The male voice let out a palpable sigh of relief."

show alexia librarian neutral at midleft with dissolve

rick "Thank Solansia! I thought Berwyn had failed to deliver my note… or worse yet, tossed it in the rubbish pit and dropped the whole affair entirely."

"The feminine voice let out a soft giggle in response."

clayil "Nothing so dramatic as all that."
clayil "He was a bit intimidated by my sisters, I’ll admit. But I got your letter just fine."

show alexia librarian shocked at midleft with dissolve

"A letter? This strange conversation was getting juicer by the moment. Her curiosity piqued, Alexia left the aisle she was working on, weaving her way down the hall in the direction of the voices."
"She stopped when she figured out their location, ducking into an aisle directly over from where the two voices were quietly conferring."

rick "Goodness, I can just imagine the sight. Your family frightens me more than a bloody battlefield."

clayil "Hehe! They ought to, we’re a protective bunch, especially when it comes to family."

show alexia librarian neutral at midleft with dissolve

"The man - whose voice Alexia recognized as belonging to a young mercenary she had bumped into a few times in passing at the castle - let out a soft sigh."

rick "...I’ve missed you, Yilly."

clayil "And I’ve missed you, Rickon."

"Alexia did not recognize the woman’s voice. It was high pitched, almost girlish in tone. She peeked through the openings of the bookshelf and tried to peer at the couple. All she could see was Rickon however, standing looking down at something near his feet. "
"He was a handsome enough young man, with charcoal black hair and a comely visage. He was fit but gangly, awkward in his movements and uncertain in his posture."
"He projected an air of confidence, but was a bit too young and too inexperienced to truly carry himself like the man he might one day become."

rick "I-I’m sorry I didn’t turn up last time. It’s been very hard to find the free time, and Father has been keeping a very close eye on m-"

"Cla-Yil let out a sultry giggle."

clayil "It’s all right, Rickon. You don’t have to explain yourself."
clayil "The two of us are stuck in… unique circumstances."
clayil "If my Auntie knew what we were up to… oh how mad she’d be! It’d throw off the family’s marriage plans for years."

"Rickon shifted back and forth on his heels, looking profoundly uncomfortable with that particular revelation. Alexia strained to peer through the maze of books to catch a glimpse of Cla-Yil, but could find no one. Rickon stared at his feet for a moment."

rick "...She sounds like my father. If he had any idea I was talking to you-"

clayil "‘He’d string you up by your heels?’"

show alexia librarian happy at midleft with dissolve

"Rickon smiled, Cla-Yil’s sarcastic retort causing all the tension to let out of his shoulders. He laughed."

rick "Kharos take me, am I really that predictable?"

clayil "You’ve described the scene to me no less than a dozen times, love."

show alexia librarian neutral at midleft with dissolve

clayil "At this rate, I’m struggling to picture your father as anything short of a fire-breathing dragon, ready to burn down the whole castle at a moment’s notice."

"The young Mercenary laughed, putting his hand upon the pommel of his sword as he struck an exaggerated hero’s pose."

rick "To be fair, ‘tis not far from the truth."
rick "On my oath as a knight’s squire I shall protect you, M’lady."

show alexia librarian shocked at midleft with dissolve

clayil "Hmm, now wouldn't that make for a silly song? A squire sparring with his knightly lord, a son battling his father in a duel of honor… "
clayil "To earn the hand of a {i}greenskin{/i}, of all things."

"Rickon’s expression softened, and he went down on one knee. Alexia, realizing at last what was going on, lowered her own gaze down a few shelves. Peeking through the cracks between the books, she saw at last the woman who Rickon was talking to."
"Rickon took Cla-Yil’s small, green hand in his larger palm and stroked it, staring directly into her eyes."

rick "Don’t say such things, Yilly. You’re not just a ‘greenskin’ to me."

"The red headed Goblin smiled, using her free hand to push the stray locks of hair from his face before reaching down to gently pinch his earlobe."

show alexia librarian neutral at midleft with dissolve

clayil "Sweet Knight, neither are you just a nobleman’s son to me. But there’s a reason the Bards never sing songs about people like us."

rick "To hell with the bards! I never liked their singing, anyway."

"Cla-Yil smirked at her companion’s youthful passion."

show alexia librarian happy at midleft with dissolve

clayil "Oh! Do go on, milord. Your righteous fury has set this maiden’s heart all aflutter."

"Rickon - embarrassed in a way that only a young man could be - blushed and looked away."

rick "Y-you don’t have to make fun of me {i}all{/i} the time, you know."

"Cla-Yil, charmed by Rickon’s moment of vulnerability, took his face in her hands. She smiled at him, her eyes lidding low as she stared deep into his eyes."

clayil "Hush, Rickon. Kiss me."

show alexia librarian shocked at midleft with dissolve

"The small Goblin leaned forward, her lips matching to his as they shared a long, intimate embrace." 
"Alexia stood to her feet in a rush, putting her hands over her mouth to cover her shock. Her face went beet red. A goblin and a human romance, right here in the castle!"
"The two star-crossed lovers had good reason to hide their romantic dalliance. Such entanglements were rare between the two species, and often looked down on by both sides." 
"Alexia hurried away as quickly and quietly as she could. She felt guilty about eavesdropping, but was still excited at the strange development. It appeared that even in the midst of war and death, unlikely love could bloom."

return

##############################################################################################
##############################################################################################
##############################################################################################

label library_lovers_2:

scene bg12 with fade
show alexia librarian happy at midleft with dissolve

"It was a wonderful day for a stroll through the library. Alexia hummed a pleasant tune to herself as she walked, her gaze turning left and right and taking in the magnificent sight of so much knowledge gathered together."
"For some reason, Alexia always found solace standing amongst the collected words of thousands of minds. All with their own story to tell or knowledge to impart, all with their own unique flavor and eccentricities."
"She never felt lonely when she was in the library, not when a rousing conversation or titillating story was just a page turn away."

show alexia librarian neutral at midleft with dissolve

"She wandered without thought towards direction or task, moving through the shelves with a kind of aimless adventurousness. She had only ever been a casual reader back in Arthdale, but here… here in Bloodmeen, they had become her refuge."
"Walking through the aisles, she paused in one particular area. It was dusty and dim, and as she regained her bearings she realized she remembered this place. The last time she’d been here, a young Squire and a Goblin were carrying on a secret romance."

show alexia librarian happy at midleft with dissolve

"Alexia smiled to herself, wondering if their short dalliance had yet ended. Young love was such a strange thing: intense yet fleeting. "

if all_actors["alexia"].relation < 30:
    "...She of all people knew the truth of that."

"She doubted that their affair had stood the test of time. Like as not, they had already tearfully parted ways with one another."

quest "{i}Mmmph!{/i}"

"No sooner had Alexia turned the corner on the next aisle than she found herself skittering back behind the shelf to take cover. She put her hands over her mouth to cover the audible gasp that issued from her lips."
"What appeared to be a Goblin and a human were in the midst of desperate flagrance with one another. Alexia had gotten but a peek, but she knew beyond a shadow of a doubt that they were… ‘involved’ with one another."

menu:
    "Peek around the corner.":
        $ released_fix_rollback()
        jump loversPeek
        
    "Leave them to their secret affair.":
        $ released_fix_rollback()
        "Alexia gulped. She had {i}not{/i} been expecting to see something like that today! Leaving the two lovers to their excessive moaning, she creeped away, keeping an eye on her back to make sure she wasn’t noticed. She did her best to ignore the shy blush that grew hot on her cheeks."
        "The Library could be a strange place, sometimes."
        return
        
label loversPeek:

#CG1
scene cg863 with fade
pause 3

"She had not been expecting to see the plump lips of a diminutive Goblin busily polishing off a much-taller human male. The mortified librarian had caught a brief glimpse of the human hunched over her, with his crotch in her face and his fingers in her red shock of hair, urging her ever onward."
"Alexia went stiff as a statue, {i}praying{/i} that the two engaged lovers had not noticed her sudden, explosive outburst through her closed mouth. The sight had been so jarring and unexpected that she’d been caught totally off guard." 
"The soft sound of the human’s groans, and the wet, gurgling sound coming from the preoccupied Goblin’s throat indicated that they had not noticed her at all."
"Alexia snuck a surreptitious peek around the corner of the bookshelf, confirming her suspicions that she had, indeed, seen what she thought she had."
"Cla-Yil was eagerly sucking Rickon’s dick, bending her head into the action as she relaxed her throat and allowed his cock to lodge itself deep inside her."
"She had good head action, widening her mouth and allowing her lips to slide freely, leaving wet strands of saliva on his turgid length as she went up and down, up and down."
"Rickon moaned, lifting his head to the sky as he hunched his back in the rough shape of a question mark, culminating in the point of contact between him and his Goblin lover."
"His hand urged her on, pulling her deep into his lap as Cla-Yil’s face moved nearer and nearer to his midsection."

rick "Oh Yilly..."

"The Goblin gulped, making a strained sound in her packed throat. Her brow narrowed, her nostrils flared, and she closed her eyes. Sensing her preparation, Rickon’s fingers clenched against the back of her head, pulling her firmly down his length to properly deepthroat him."
"Cla-Yil made a slight choking sound, but somehow managed to take him down to the base, her cute button nose bunching up against his midsection. She took a short inhale, savoring his masculine scent as her eyes fluttered."
"Rickon held her there for a long moment, then pulled back, allowing her to gasp in a breath of air, exposing his rock-hard cock, coated in her saliva."
"Cla-Yil rubbed at her cheek, noting with a wry smile that her dark lipstick had left a series of concentric lipstick rings running down to his base, culminating in a puckered kiss at the very bottom of his cock."
"Her eyes flicked up to look at her lover as she leaned back to inspect her work. Her hand reached out to fondle his balls."

clayil "Told you I could do it!"

rick "Kharos take me, I never thought I’d be so happy to be so {i}wrong{/i}."

"The two laughed, sharing a brief moment of levity in the midst of intimate eroticism. Alexia peeked around the corner, keeping her mouth covered so as not to alert the two lovers to her surreptitious snooping. The thought of being discovered was mortifying."
"Rickon bent down and kissed the top of Cla-Yil’s head. She huffed and flicked the underside of his chin."

clayil "I’m wetter than a rainstorm at the moment Rickon, a kiss on the head’s not gonna cut it."
clayil "Pick me up, jam me against the wall, and {i}get inside me{/i}."

rick "Y-yes ma’am!"

"The little Goblin grabbed Rickon by the scruff of his collar and yanked, pulling him into a harsh kiss that the young Squire eagerly reciprocated."
"He stripped her of the few remaining bits of clothing she had not already cast aside like so much flotsam, taking hold of her thick hips and lifting her up in his arms."

#CG2
scene cg864 with fade
pause 3

"Cla-Yil let out a pleasured gasp at the feel of Rickon’s cock sliding against her bottom. She reached out to steady herself against the bookshelf, her nails digging into the wood as her legs swung freely in the air."
"Her big green bottom wiggled back and forth eagerly while Rickon angled himself against her feminine folds."
"True to her words, she was leaking. There was no resistance whatsoever as Rickon’s cockhead pierced her womanhood, sliding in to the hilt in one, smooth stroke."
"Cla-Yil let out a small gasp, her tiny frame squishing up against the bookshelf as Rickon took firm grasp of her hips and began to thrust."

clayil "{i}Ooooh{/i} yes! Come on love, {i}fuck me{/i}!"

"Rickon let out a deep grunt, bending his legs to get better leverage as he thrust upwards back and forth, back and forth again. Cla-Yil squealed as he slid home into her deepest place and then withdrew, only to find the air knocked from her lungs by the upstroke."
"The wet {i}smack{/i} of her green ass connecting with his hips filled the air, the two randy lovers heedless of anyone who might be unintentionally peeping."
"Alexia watched in shock, astounded at the passion with which these two very different species engaged with one another. The Goblin’s smaller scale made for a strange sight, as Rickon’s larger frame seemed to loom over her like a giant."
"Such size issues did not seem to bother either of the participants in the slightest… if anything, it made them {i}more{/i} lustful."
"Rickon fucked Cla-Yil with all his strength, thrusting against the Goblin’s fat bottom like a man possessed. Cla-Yil’s fingers clenched against the shelf, her body bouncing against the bookcase, her mewling cries echoing in the narrow spaces."
"The horny Goblin bounced back and forth between the bookshelf and Rickon’s postponing hips like a rag doll, her body absorbing the sordid thrusts of her chosen mate with the eagerness of an animal in heat."
"She cast a long, lustful look back over her shoulder at Rickon, who returned the look with equal verve and passion."

rick "I love you Yilly!"

"Cal-Yil’s body clenched up in orgasm when he said those words, her body seizing up as she let out a cry of pleasure."

clayil "I... {i}aah{/i}! l-love you too, Rickon!"
clayil "Cum for me, my Knight. C-{i}cuhhh{/i}!"

#CG2 - cum var
show cg864 with sshake
show cg864 with sshake
scene cg865 with flash
pause 3

"She never finished her sentence, for her mate was already acquiescing to her wish. Rickon thrust once, twice, three times, then jammed Cla-Yil as tight against the shelf as he could, causing a loud {i}thump{/i} from the weight of their impact."
"He draped himself across the top of his lover and planted kisses against the back of her neck."
"Cla-Yil cried out and went stiff, the two holding in the stillness as they reveled in their mutual orgasm."
"The Goblin gasped and squirmed and squealed, and her lover let out great gouts of air from his nose as he thrust against her again and again, keeping her tight to his waist as he drained himself within her."
"Exhausted, spent, unable to hold her up any longer, Rickon gently pulled free from Cla-Yil’s cunny and set her down onto her wobbling and unsteady feet."
"Cla-Yil moaned, holding fast to the shelf for leverage as a strong trickle of white cum dribbled out of her pussy. She let out a shuddering sigh, almost like a laugh."

clayil "R-ready for round two?"

"Rickon, breathless, began to laugh. He sat down on the ground, crossing his legs as he smiled at his little lover."

rick "More ready than you are, looks like."

"Cla-Yil tried to affect a scowl, but her body was still trembling from the aftermath of her explosive orgasm."
"Instead of growling at him in annoyance, she let out a small sigh, walking over to Rickon in a few footsteps. She bent down over him and took his face in hands, planting a soft kiss to his lips."

clayil "Careful now, love. We can waste a whole day here together."

"Rickon laughed, patting Cla-Yil’s bare bottom with his hand before kissing her again."

rick "Not without getting spotted. We should get dressed, lest we scare some poor librarian sorting books."

"Cla-Yil let out a sultry chuckle. Alexia, seeing her chance now that the not-so-surreptitious lovers were readying to leave, fled with all possible stealth from the site of the romantic dalliance."
"It was to her shame (or perhaps it was excitement?) that her face was flushed, and her heart beating a lot faster than normal."
"Who could have expected two different species with such differences would have such passionate sex?"

return

##############################################################################################
##############################################################################################
##############################################################################################

label library_lovers_3:

scene bg12 with fade
show alexia librarian angry at midleft with dissolve

"Things just weren’t going Alexia’s way today."
"Her rotten luck began when she bumped her head against the headboard as she was getting out of bed in the morning, and things only worsened from there. She was nearly trampled by a patrol of Orcs as she emerged out of her living quarters."
"Shortly afterward, she was accosted by one of the brutes, who only backed off after a swift and furious tongue lashing."
" It didn’t help things when Alexia then tripped on the rug and - in front of all of them - face planted onto the ground. She marched up the hall away from the orcs with burning red cheeks and the sound of jeering laughter following behind."
"She’d even stubbed her toe against one of the Castle’s multifarious and equally-superfluous armor statues, she’d taken her anger out upon the makeshift Knight-stand by kicking it a second time, earning herself a jolt of pain and a profound sense of injustice in this world."
"To top it all off, her usual outfit had somehow gotten soaked through by some unknown but sticky substance lying on the ground in her room. What that substance was or where it had come from were questions Alexia did not want to know the answers to. "
"All that she knew was that now she was stuck wearing her normal clothes for the duration until the scullery maids could scrub the grime and… whatever it was off of her precious librarian outfit."
"So it was with a heavy heart and a sour expression that she all but ignored her surroundings as she trudged through the aisles of the Library, seeking some meaningless job to do to pass the time and perhaps take her mind off of her horrid circumstances."
"That is, until she stumbled once more upon a pair of clandestine voices whispering conspiratorially back and forth to one another."
"Passing through the rows of books, Alexia passed one particular cove that was occupied. Stopping short, she craned her neck around the edge to look for a moment in confusion at the two figures huddled together on the other end of the row."
"It was Rickon and Cla-Yil, the two young lovers whom Alexia had inadvertently peeked on in the past."
"Low voices could be heard, and as Alexia strained to listen she could just make out their furtive back and forth."

if all_actors["alexia"].corruption > 30:
    "She recalled in vivid detail their sordid affair the last time she had seen the two together. Truth be told, she had thought of the two on occasion while lying in bed, thinking of… other things."
    "The size difference alone had added an exciting dimension to their lustful adventures."
    
else:
    "She remembered with a flush of embarrassment how she had peeked in on the two in the midst of their flagrant détente. She had not intended to come off as a letch, though Alexia had to admit that their passionate lovemaking was… {i}inspiring{/i}. "
    "The two were clearly in love with one another."

show alexia librarian concerned at midleft with dissolve

clayil "...So what does this mean?"

rick "For us, or for me?"

"Cla-Yil reached up and slapped Rickon lightly in the face. He recoiled, shocked at his small companion’s aggression."

show alexia librarian shocked at midleft with dissolve

clayil "For {i}you{/i}, you lovestruck fool! I’m not the one being sent to die for the sake of your father’s vanity."

rick "It’s not that bad, Yilly."

"Cla-Yil turned away from Rickon, covering her eyes with her hand. She shook her head back and forth slowly, letting out an exhausted sigh."

clayil "It is, Rickon. If you go on that fool’s errand, you’re never coming back."

"Rickon reached down and put a hand on her shoulder. She gently stroked his large fingers with her own."

rick "I’m not leaving you for good, my love. It’s only a short campaign. My father believes we’ll take the castle handily. He even made me a Knight-"

"Cla-Yil spun around to face Rickon, a rage building in her face."

clayil "Because {i}he wants you to join him{/i}! He knows how distant you’ve become. If he doesn’t know about us, he at least {i}suspects{/i}."
clayil "Don’t you see, Rickon? His mad quest to reclaim your family’s land is going to get you killed."

rick "It’s… our heritage. For five hundred years the Terrascens have ruled from Urstaleed-"

clayil "You're feeding me your father’s poison, Rickon."
clayil "Tell me truthfully: did you ever really care about the ‘legacy’ of your family name? You never did, did you?"
clayil "Otherwise, why would you bother with a greenskin like me?"

rick "Yilly-"

clayil "Your father takes back your ancestral castle. And then what? You two cower behind its walls for a year before the local lords starve you out?"

rick "The Twins will send us aid-"

clayil "Don’t you {i}dare{/i} lie to me right to my face, Rickon. The Twins don't give a fig about your father’s holdings, rightful or otherwise. They’re remote; out of the way."
clayil "How long do you think their ‘support’ will last once your father becomes isolated, inconvenient to their plans?"

show alexia librarian neutral at midleft with dissolve

"A long silence followed Cla-Yil’s words. Alexia watched the little Goblin reach up and pull Rickon into her thin arms."

clayil "I can’t stand the thought of you dying for a man who doesn’t care about you, Rickon. It… It’d be one thing if you actually {i}wanted{/i} this, b-but-"

"The Goblin began to cry. Rickon’s arms tightened protectively around her."

rick "It won’t come to that, Yilly. I swear it."

"She clung all the tighter to him as she shook her head back and forth."

clayil "You can’t promise me that, Rickon."
clayil "{i}Please{/i}: if this is to be the end of us, will at least you be honest with me?"

show alexia librarian concerned at midleft with dissolve

rick "I… I don’t know if-"

clayil "I {i}love you{/i}, Rickon. I can’t bear the thought of you dying for a hunk of rubble in a swamp. "
clayil "You can’t go through with this. Don’t die for someone else’s dream."

"The Goblin buried her head in Rickon’s shoulder, sniffling and crying as she held tight to him. Rickon’s expression fell. He seemed to contemplate the whole world in those brief, desperate moments."

rick "...There’s only one option that I can think of, love."

clayil "Then do it. Do it no matter what it takes, even if it means we never get to see each other again."
clayil "I need to know that you're safe."

rick "I’ll take you with me."

show alexia librarian shocked at midleft with dissolve

"Cla-Yil pulled away from Rickon, staring at him in blank incredulity."

clayil "...{i}What{/i}?!"

"Rickon, emboldened, took the startled Goblin in her hands and gifted her a wide, earnest smile."

rick "I’ll take you with me. You’ll ‘accompany’ the baggage train as a hangers-on."

"The Goblin peeled her hands out of his grasp, staring at her newly-christened Knight like he had gone utterly mad."

clayil "Rickon, sacrificing {i}both{/i} of us at the altar of your father’s ambition is not a solution. "

rick "To hell with taking back Urstaleed, Yilly. I’m talking about running away."

"The little Goblin froze in her large lover’s arms. She stared deep into his eyes, unable to comprehend his words."

clayil "...What are you saying?"

rick "I love you, Yilly. But we will never have a life together if either of our families have a say in it."
rick "Even if I were to abandon my father and remain here with you at Bloodmeen, how long could this really last?"
rick "Your Aunt will find a partner for you, and then you’ll be wedded-"

clayil "Like hell I will be!"

"Rickon chuckled, stroking his thumb across the smooth green skin of Cla-Yil’s cheek."

rick "Exactly my thoughts, love. Mayhaps instead we choose a different route, one {i}neither{/i} of us returns from."
rick "We’ll join my father’s caravan. Then, after a few days' travel, we disappear. Make for the nearest city and start anew."

clayil "...Together?"

rick "Together."

clayil "But… what about coin? A place to live? What will the other humans say if they see you-"

rick "I’ll find work, even if I have to shovel shit off the ground. We’ll find a place to live together, and {i}Kharos{/i} take what anyone else says about us."
rick "If I can spit on my family name and my oaths as a Knight, the {i}least{/i} I can do is ignore a bunch of illiterate fools who don’t understand what happiness looks like."
rick "You’re the woman I’ve always waited for, Yilly. "

clayil "Rickon…"

"The two embraced, fresh tears flowing down both their cheeks as the two shared a deep, romantic kiss. They held fast to one another for a long time before either said anything."

rick "...I need to leave immediately, make the necessary preparations and grease the right palms. Can you convince your aunt to let you go on this expedition?"

clayil "I will {i}be{/i} on that supply wagon when it departs, Rickon. By all the Planes of Chaos, I promise you."

rick "Then we will speak again tomorrow, when the time has come to set off. Till then my love…"

"Rickon bent down, and Cla-Yil lifted her chin. The two embraced in a final, deep kiss. Sensing their impending departure, Alexia sidled away, thoroughly shocked at the recent developments, and of the fated lover’s plans."
"She rushed as best as she could to the front of the Library, doing her best to seem like she was in no particular hurry. She was so harried by what she had just witnessed that Alexia inadvertently turned a corner and slammed into the equally-harried young Knight."

al "{i}Aaah{/i}!"

rick "Oof!"

"Alexia bounced off of Rickon’s chest and fell back on her bottom."

rick "Solansia’s Spirit! Are you all right, Ma’am?"

"The shocked Knight bent down and immediately offered his hand. Alexia hesitated for an instant before accepting it as he pulled her to her feet."

rick "A {i}thousand{/i} pardons, my lady! I was in such a hurry I did not look where I was going."

show alexia librarian concerned at midleft with dissolve

al "O-{i}oh{/i}! It’s quite alright, Rickon."

"Rickon’s face went queer. It was only after a few seconds of awkward silence that she realized she’d just blurted out his name."

rick "...How do you know my-?"

show alexia librarian happy at midleft with dissolve

al "O-oh! I’ve…"

"Alexia spun a quick lie."

show alexia librarian neutral at midleft with dissolve

al "-I’ve seen you here in the Library a few times before. A little Goblin was asking earlier about a man who fit your description. She said your name was Rickon."

"Now it was Rickon’s turn to look uncomfortable."

rick "Ah! Y-yes of course."
rick "Did she… she didn’t tell you anything about-"

show alexia librarian happy at midleft with dissolve

al "Did you end up getting the shipment she was trying to deliver?"

"Rickon’s eyes lit up, seeing an out from his own clumsy conundrum."

rick "...Yes!"
rick "Yes I did, thank you."

al "Good. She seemed very excited to see you."

"Alexia couldn't help but grin inwardly at the warmth that built in Rickon’s eyes when she said that. He really did love the little Goblin."

al "Anyways, I’m sorry for bumping into you like that. I hope you have a good day!"

rick "Thank you! You as well, uh-?"

al "Alexia."

rick "Alexia. It was a pleasure to see you."

"Alexia suppressed a smile as Rickon rushed out of the library, on to prepare for his and his lover’s grand adventure together. From personal experience, Alexia knew how easy it was for young love to end in tragedy and suffering."
"...Yet, she could not help but feel a warmth in her chest as she thought of the unlikely pair. For all the ill that had happened to her today, their tiny struggle to find love and happiness in a world full of pain and suffering was charming. "
"She hoped they would find the peace Alexia had failed to find in her own life."

return
