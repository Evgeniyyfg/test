init python:
    
    event('magic_bookshelf', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), group='alexia_library', run_count=1, priority=pr_npc)
    event('liurial_in_the_library', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",'alexiaLiurialFriendly',), group='alexia_library', run_count=1, priority=pr_npc)
    event('jezera_visits', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), group='alexia_library', run_count=1, priority=pr_npc)
    event('library_goblin_thief', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), group='alexia_library', run_count=1, priority=pr_npc)
    event('perverted_POT', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), depends=('magic_bookshelf',), group='alexia_library', run_count=1, priority=pr_npc)

label magic_bookshelf:

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve

"Alexia pushed her cart through the dark part of the library. The low ceiling and distance from the windows made it into almost an alcove. The only visibility came from torchlight."

pot "Girl. Over here. Girl."

"Alexia blinked twice. Was someone speaking to her? She looked around, but the room was empty."

pot "No. Don’t turn around again. I’m right over here."

al "Where are you? I can’t see you."

pot "The bookshelf, girl. The bookshelf."

"Suddenly, a bookshelf on the far right went crazy. Books started popping out and then jumping back in with no indication that anyone had touched them. Alexia approached slowly."

al "You’re...the bookshelf?"

pot "Correct in spirit if not in nomenclature. Once upon a time, I was called the Prince of Tomes."

$ potName = "Prince of Tomes"

"Alexia cocked an eyebrow. Hardly the weirdest thing she’d found in the castle so far."

al "That’s a pretty fancy name for a bookshelf. "

"She brushed her hand over the spine of the books. They were all old and dusty. Indeed, it didn’t look like anyone had taken any of the books off the shelf for many years. Just how old was this creature?"

pot "I’ve resided here for many hundreds of years. The first demon lord to make use of my mighty talents was Azerion the Dread. The works I carry are timeless."

#alexia shocked
al "How did you-"

pot "Know what you are thinking? Reading is a talent of mine. The human mind is as obvious as words on the page."

"Alexia drew her hand back. How had it done that? Could it see her? Was it able to read thoughts? She almost waited to answer to her own internal monologue, but if the bookshelf really did know what she was thinking, it didn’t reveal it."

al "So, “Prince of Tomes”, what is it you want with me exactly?"

pot "Entertainment mostly. It’s so rare to see a human girl working this segment of the Bloodmeen library."

if all_actors['alexia'].corruption < 60:
    pot "Rarer still one so innocent. This castle has such a way of disposing with that virtue."

else:
    pass
    
#alexia neutral
pot "I think we could establish a mutually beneficial relationship. You’re new to this world, yes? The works on my shelves are full of knowledge. Knowledge that one trapped in your position might find valuable."
pot "And I need a way to pass the time. What good is a collection of books that is never read? I want to fulfill my purpose."

"Alexia took a step back, crossing her arms over her chest. Part of the benefits of working in the library was all the reading material. Furthermore, Cliohna didn’t seem much interested in recommending her reading material of value in her situation."

if all_actors['alexia'].corruption > 50:
    "he squinted slightly. What mysteries did the books contain? Perhaps there would be something of value in their pages…"

elif all_actors['alexia'].corruption > 70:
    "Alexia briefly flashed a grin. What dark mysteries must be contained on the pages of the books. Powerful and valuable insights...perhaps something a bit more erotic..."
    
else:
    pass
    
"But, it wasn’t like she needed to be told that the bookshelf could just be lying. It was clearly magic. Who knew what curses could be on it."

if alexia_and_her_demon_book > 0:
    "Alexia knew full well what kind of malice evil books were capable of from first hand experience."
    
else:
    pass
    
pot "What do you say? I know just the book for you. I always know what books people are looking for, even if they do not know it."

"One of the books on the shelf suddenly pushed outward, standing out amidst the rest."

menu:
    "Take the book.":
        $ released_fix_rollback()
        $ POTTaken = True
        jump potTakeBook
        
    "Keep on walking.":
        $ released_fix_rollback()
        $ POTTaken = False
        "Alexia stared at the book in silence for a moment before she shook her head. This was a trap. It almost had a glowing sign declaring as much. Alexia had not been in this castle for more than a year without coming to understand how dangerous trusting anything here was."
        "She went back to her cart and started to push it back into the light segment of the library."
        pot "Wait. Come back."
        al "Not today, bookshelf. Maybe another time."
        "She kept about her rounds for the day, making sure the library was in the proper condition. Every so often she’d glance back at the darkened corner where she knew the creature was no doubt observing her."
        return        
        
label potTakeBook:

"Alexia put her hand on the book extending from the shelf. It felt normal enough."

al "And there are no charms on this book? No curses or anything?"

pot "It is but a normal book. You have my word. No doubt you can understand how important my word is to one such as myself."

"Alexia sighed. There was no harm in a bit of reading. Besides, this creature seemed to suggest this book to her specifically. Perhaps there was a reason for it."
"She grabbed the book and put it on her cart. If the Prince of Tomes had a reaction, it did not show it."
"Shortly afterwards, was her normal break time. Alexia found a quiet corner of the room, far away both from the mistress of the library and the strange bookshelf. There she opened the book to a random page."

if all_actors['alexia'].flags['jezera_influence'] > 5 and all_actors['alexia'].relation < 30:
    $ POTscene = "Jezera"
    scene cg250 with fade
    pause 3
    "The book was about the culture and secret practices of the dark elves. Even a cursory glance proved that it had the sorts of information that no conventional human book would ever have. This might be useful. Alexia dug into the pages."
    "{i}The third high elf reconciliation mission was led by a male named Fargut. Fargut’s plan was to offer Queen Varyn and Queen Maieria plots of forest near the banks of the river Anurillindill. {/i}"
    "{i}The twin offer was designed to exclude Queen Arrania. This was part of Fargut’s plan of division, however it would later prove to be the doom of the proposal, when…{/i}"
    "Alexia skimmed around more, reading through various segments. Much of it was dry details of history that might have been recorded elsewhere. She kept on searching for the secret details of Dark Elven society."
    "Then she opened the book to a fascinating segment... "
    "{i}A portion of the captured human women, the most beautiful portion, are taken by Queens, High Nobles, and those instrumental in their capture. They are to become Tongue Girls, eternal servants of their dark mistresses.{/i}"
    "{i}Before the litany of spells can be applied, the first step is to wear down the resistance of the captives. Consent empowers the spells, for the strongest chains are those self forged.{/i}"
    "{i}Future Tongue Girls are kept in seclusion in the dark. They must be taught not to expect the light. The only food they are given are from the Fruits of the Underground Skenia tree. It’s addictive flavor has been long attested too. {/i}"
    "{i}The Skenia fruit take on the flavor of the first liquid they contact. When put to the taste of the Tongue Girl’s future Mistress, they replicate their taste exactly. Tongue Girls are conditioned to their Owner from afar.{/i}"
    "{i}The key test to decide if a Tongue Girl is ready the trial of binding. A conventional blindfold is used and they are taken from their cell for the first time. There they are presented with the naked body of their Mistress and four of her servants.{/i}"
    "{i}A future Tongue Girl is expected to use her mouth to bring pleasure to each of the five. Failure to do so is met with severe consequences. At the conclusion, she is to be given the test of selection. She must identify her Mistress by the flavor.{/i}"
    "{i}If the Tongue Girl fails, she is to be taken back to her cell and her diet of Skenia fruit is resumed. If she succeeds, it means she has accepted her Mistress’ unique flavor, and the next stage of her training can begin. {/i}"
    "{i}That involves-{/i}"
    #alexia aroused
    "Alexia slammed the book shut in a hurry. She’d been so lost in the passage she hadn’t even been paying attention."
    if all_actors['alexia'].corruption > 50:
        "There was no other word for what she had been reading besides depraved. She had not finished the passage, but the meaning of the name “Tongue Girl” was hard to miss."
    elif all_actors['alexia'].corruption > 70:
        "Alexia bit her lip. The talk of Tongue Girls didn’t go into nearly enough detail, but what had been described was so depraved...sexy…"
    else:
        pass
    $ change_actor_num_flag('alexia', 'jezera_influence', 3)
    jump potResolution

elif all_actors['alexia'].flags['andras_influence'] > 5 and all_actors['alexia'].relation < 30:
    $ POTscene = "Andras"
    scene cg251 with fade
    pause 3
    "The book was about a human knight named Eleanor, the woman who’d popularized the name. She’d been Solansia’s campion in a war vs the Demon King Nekolio more than 400 years before. The first time a human champion of Solansia had emerged since ancient days."
    "Alexia knew her story. It was very common in Rosaria. But, there was nothing wrong with looking at it again. After all, this was the work of an author in Bloodmeen. In the known story, she vanished in the last battle on Rosarian soil. Her fate was considered something of a mystery."
    "She opened the book to the segment after the battle."
    "{i}Nekolio, King of Kings, King of Lands, brought his new trophy with him to all functions and events. He was seldom seen without the slave groaning and seething at his feet. The rattle of her chains was heard often.{/i}"
    "{i}The King would take great pleasure in using his slave in public. She was taught the arts of pleasure, in contrast to her former training. She was taught to replace the sword with the shaft.{/i}"
    "{i}The King said loud and strong that she would learn to enjoy herself. All human sluts did. The slave insisted that she was not a slut. Yet, the first signs of resistance breaking were observed. The wetness of the thighs, the eyes focused on his cock.{/i}"
    "{i}It was only when the first stage of her resistance was broken that the King announced that his slave would be made to bear his next child. She would be fucked mercilessly day in and day out until his seed had taken hold.{/i}"
    "{i}The slave did not speak at this announcement. Perhaps even this early she was learning to accept the pleasure that a human man could not provide-{/i}"
    #alexia aroused
    "Alexia slammed the book shut there, cheeks flushed. That phrase she’d just read, about pleasure a human man couldn’t provide, had hit a bit close to home."
    if all_actors['alexia'].corruption < 30:
        "She couldn't put her finger on why. It seemed wrong to her. Like something that shouldn’t even be said. Yet...it did have an effect on her…"
    else:
        "Her finger traced the cover of the book. Even if she didn’t want to admit it, she had thought that exact same thing during her past...encounters...with her captor."
    $ change_actor_num_flag('alexia', 'andras_influence', 3)
    jump potResolution

else:
    scene cg252 with fade
    pause 3
    $ POTscene = "Rowan"
    "Alexia skimmed the book with a furrowed brow. The topic of it was strange. Not something she ever expected to read about. The first human to reign as a queen of Bloodmeen."
    "The story of how it happened was a curious one. After the fall of a demon lord, the daughter of a high lord was placed as caretaker of the castle. Perhaps it could even become a functioning part of the realm."
    "She flipped ahead in the story. Already she could see the way it went wrong."
    "{i}The Queen brought the Knights of Bloodmeen to the throne room, and they were shocked by what they had seen. She sat naked upon her throne, impaled upon a phallic object. The chaste men shielded their eyes.{/i}"
    "{i}The slutty queen declared her new allegiance to chaos. The pleasure that came from sex and power. She revealed the sexual encounters she’d had throughout the castle with the remaining prisoners.{/i}"
    "{i}She spoke of the joys of sex. The hatefulness of purity. What was the point of limiting ones pleasures in the name of a lady who loves them not?{/i}"
    "{i}She revealed the interests that had grown in the interim. How lovingly she spoke of large cocks and rough sex.{/i}"
    "{i}The Knights of Bloodmeen debated continuing their mission and removing their queen from her throne. But, without consulting the others, Sir Vasylio approached the throne and stripped off his armor.{/i}"
    "{i}The Knights were yet more astonished as the Queen mounted her loyal knight right there and fucked him in front of the entire-{/i}"
    "Alexia slammed the book shut. A shiver went up her spine."
    if all_actors['alexia'].corruption < 30:
        "Just what was she reading? How could a woman choose to do such a thing? Yet, everything she read merely reminded her of her day to day life."
        "She felt the constant caress of this place at all times. Behind every nook and cranny, something was here urging her to go further, do something that she might have viewed wrong for her entire life."
        "It could be quite seductive..."
    else:
        "Alexia licked her lips. She understood the chain of events that had led the queen to that mental state. In truth, it wasn’t like she’d never thought about having sex in public, or any of the debaucheries she’d ever read."
        "People did what felt good, right?"
        if all_actors['alexia'].corruption < 60:
            "Part of her, a part from back before, loudly reminded her that this was wrong. But, reading the story just now had made that part of her easier to ignore. Whiny. Annoying."
        else:
            pass
    
label potResolution:

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve

"For the briefest moment, she glanced towards the front of the library. Would Cliohna be too angry with her if she stopped to touch hers-"

"Alexia shook her head. That was a bad idea. She should just finish her work."

"Alexia picked up the book and walked towards the darkened section of the library."

pot "I knew you’d like the book. I always know the books that humans long to read most."

"Alexia answered quietly."

al "It was illuminating."

"She placed the book on the empty spot of the shelf and then returned to her duties. Part of her suspected that this might not be the last time she paid the Prince of Tomes a visit."

$ change_corruption_actor('alexia', +3)

show cliohna neutral at cliohnaright with dissolve

"On her way out for the night, she was stopped briefly by Cliohan. The woman did not even raise her glance from her reading material."

cl "Be careful with the creature in the back of the library. It is mostly harmless, but it is not trustworthy. There is a reason why I have not made use of it’s talents in my studies."

"Alexia walked on, unsure of what to make of Cliohna’s warning. Just what was that thing?"

al "...Right."

return

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

label liurial_in_the_library:

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve

"Alexia looked up from the rack of books. There was a guest in the library today."

show liurial neutral at midright with dissolve

"Rowan’s pretty blonde secretary was leafing through a few books idly while sipping tea. Her eyes moved quickly over the text, and her lips even mumbled silently to herself as she read."
"Alexia ducked her head back down. Liurial probably was not looking to be disturbed."

hide liurial with dissolve
show cliohna neutral at cliohnaright with dissolve

"A few minutes later, Alexia walked past Cliohna on her way towards the filing log. Her boss raised a hand to call her, but otherwise did not look up from her own reading."

cl "Tell the elf not to bring food or drink into the library. "

"Alexia glanced back towards Liurial and bit her lip."

al "Do you know what she’s here for?"

cl "She comes to read from time to time. She is far from the only one who does so. I do not inquire about their reasons."

al "Hmmm."
al "She’s normally pretty careful though. I think she should be alright."

"Cliohna grunted and returned to her task. All of this was truly beneath her concern."

hide alexia with dissolve
hide cliohna with dissolve

show liurial neutral at center with dissolve

"Liurial continued to read for another few hours, occasionally going over to the shelves to pick up a new book. No one disturbed her."
"After about an hour, when she noticed that she’d finished her tea, before she even had a chance to go up and make a new one, she found another mug of tea waiting for her. Initially she was suspicious, as one should be in Castle Bloodmeen."
"But, with a sigh, she tried the new tea. It tasted good."
"It went on like this for the rest of the evening. Whenever in the midst of reading, she’d find herself running low, a new mug would appear on the desk, piping hot."

hide liurial with dissolve
show alexia librarian neutral at center with dissolve

"Later that night, after Liurial had left, Alexia went back to the desk to clean it up. She found a stack of books neatly organized so they’d be easy to return to their shelves. She also found several mugs all kept together."
"Finally, as she was cleaning it all up, she found a note."
"“Thank you, Mistress Alexia. You are too kind to me.”"
"Alexia smiled to herself. It seemed Liurial liked the tea."

return

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

label jezera_visits:

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve

"Working in the library often gave Alexia time for some reading. With her assigned tasks for the day done, she was seated at a table with her eyes fixed on the pages of a massive tome."

#alexia surprised

"Or at least she was until she felt a pair of hands suddenly grasp her shoulders. It made her half jump in her seat."

show jezera happy at midright with dissolve

#alexia annoyed OR alexia happy (if alexiaJezObedient)

je "What do you have there, little dove?"

if alexiaJezObedient:
    "Alexia looked back to the smiling face of the her mistress. Without asking, Jezera reached down to the book and brought the cover into view. At least she had the decency of keeping two fingers in the segment Alexia had been reading."
else:
    "Alexia looked back to the smiling face of the the demoness. Without asking, Jezera reached down to the book and brought the cover into view. At least she had the decency of keeping two fingers in the segment Alexia had been reading."

je "A history of Rosaria?"

#alexia neutral

al "I’ve never seen this book before. I’d read other histories of the country in the past, but never this one."

"Jezera absentmindedly flipped through the pages. It gave Alexia half an anxiety attack. Would Jezera pull her hand back from the pages."

je "Interesting. Interesting."

"She flipped the book back to Alexia’s page."

je "This is no ordinary history book, you know?"
je "Your countrymen have their clever little scribes, but so do the demon lords’ own. You’ll find details in that book that no silly human book will hold."
je "I personally found it a fascinating read."

#alexia surprised

al "You’ve read it before?"

"Jezera laughed and planted herself in a dainty position on the table."

if NTR == True:
    #alexia aroused
    "It made the hem of her low cut skirt ride up her leg to a distracting degree."
    #alexia neutral
    
je "What, do you think I just come here to annoy Cliohna?"

hide jezera with flash
show cliohna neutral at midright with dissolve

"Suddenly, there was a flash of light. Where Jezera had been sitting was now a near identical replication of Cliohna. From her vantage point, Alexia could spot imperfections. But, it would fool from a distance."

cl "There are other locations where it is possible for you to read, Demoness."

"Even her voice was a near perfect replication of the librarian."

cl "I must sit behind this desk and fuck myself while thinking about books."

hide cliohna with flash
show jezera happy at midright with dissolve

"There was a second flash of light. Jezera reverted back to her original form, leaving Alexia gawking."

if alexiaJezObedient:
    #alexia happy
    "Alexia couldn’t suppress a giggle. "
    #alexia neutral
    
al "Didn’t you say that taking on a new form requires a great deal of study? Why do you even have a Cliohna form ready?"

"Jezera laughed and swiped at the air like a cat."

je "I have my reasons, little one. Let’s leave it at that, shall we?"

show jezera neutral at midright with dissolve

je "Still, I have indeed read the book. Or at least segments of it. I was brushing up on my Rosarian history in preparation of our war there. "
je "The contents were fascinating. The scribe even has some first hand accounts from survivors of the first great Goblin massacre. The Red Day at Blue Creek."

#alexia shocked
al "Goblin massacre…?"

"Alexia raised an eyebrow. She’d heard of the Goblin Wars before, of course. Arthdale hadn’t been so far from Blackholt that the subject of Goblins never came up. Still, she’d never heard of an event like that."
"Without even looking, Jezera flipped through the book to an appropriate section."
"{i}He said that “The last of our raiders held up in the freestanding straw structures that the humans had remained untouched. Even there, the screams made it through. There must have been two hundred dead already”{/i}."
"{i}“Cor-Su ducked under a feather bed. She must have been too loud, because that was when it was out turn. We didn’t see it happen, but the straw roof was entirely in flames in”{/i}"
"Alexia pulled back from the text, feeling a sudden pit in her stomach. That was a real account from a goblin..."

al "That’s not what they I’d heard said about the goblins wars. I’d heard that-"

je "They were a necessary evil? Valliant battles against overwhelming hoards of child eaters and thieves? An existential struggle for survival against the snarling beasts of chaos made flesh?"

show jezera happy at midright with dissolve

je "Cute."

al "..."

je "So? What does our nice little village girl have to say about this?"

"Alexia looked back at the page."

"{i}We only possess accounts from 42 of the survivors. It is estimated that the humans killed in the vicinity of 500, however the remaining 26 goblins likely died in the subsequent northern offensive. The repeat of the tactics at Red Creek at the Martorian Pass reflects...{/i}"

je "I’m waiting."

menu:
    "This Can’t Be Real!" if all_actors['alexia'].corruption < 61:
        $ released_fix_rollback()
        #alexia neutral
        "This can’t be real."
        "She definitely shook her head. It didn’t matter what the book said. The books in this place were fascinating. But, could they truly be said to be trustworthy?"
        al " Of course, the writing of demons and the chaos-tainted would make such claims. Can you really claim that the writings of these people are from trustworthy individuals?"
        "The other woman gave a sharp smile."
        je "Perhaps not. But, are the human lords really so trustworthy either?"
        je "Someday, you’ll understand that everyone is a liar. Is this book the truth? Perhaps not. But, they are no less liars than any of the books you’d read before."
        #alexia concerned
        "Alexia looked back at the pages. The story it told was so vivid. If it was a fabrication, it was one that took effort."
        #alexia annoyed
        "Though, it wasn’t as though she’d never experienced someone put great effort into a lie before."
        al "Some people lie more than others. If anything has been taught to me at this place, it’s that."
        "Jezera didn’t stop smiling."
        if alexiaJezObedient:
            je "You’re a fruit with tough skin sometimes, Pet. Very well. Keep your delusions for the nonce. "
        else:
            je "You’re a fruit with tough skin sometimes. Very well. Keep your delusions for now."
        "Her hand brushed softly over Alexia’s shoulder in the process of rising to her feet. Jezera left Alexia, still at the table with the book close at hand."
        hide jezera with dissolve
        "But, Alexia didn’t much want to read it anymore."
        return
        
    "How could they do such a thing?":
        $ released_fix_rollback()
        #alexia concerned
        "Alexia closed her eyes. The words were right there on the paper. There was a great storm running through her mind, but she could not deny the obvious truth of them. They felt real."
        #alexia angry
        al "How...how could they do such a thing? Surely they knew it was evil. Why else would they have hidden it?"
        al "I am going to be sick."
        "Jezera leaned down and brushed a hand against her cheek."
        je "Learning things is not always pleasant, little dove. But, it’s part of growing. Little girls in quaint villages here more lies than truth. Trust nothing you learned there."
        if alexiaJezObedient == False:
            "There was a wisdom to those words. But, Alexia caught what was missing as well. It wasn’t like she should trust Jezera either."
        #alexia concerned
        al "I’ve been naive about many things, haven’t I?"
        "Alexia leaned back in her chair."
        "The men who’d told the history of the “heroic” Goblin wars were the forefathers of Rosaria’s nobility. The great great great grandparents of the men who’d hurt Rowan so much by tricking him."
        "While Alexia deliberated, Jezera lifted herself gracefully from the table."
        if alexiaJezObedient:
            je "Alas, were I in possession of more time, I’d stay and chat. But, I’m not. Enjoy your reading, Pet."
        else:
            je "Alas, were I in possession of more time, I’d stay and chat. But, I’m not. Enjoy your reading, Alexia."
        hide jezera with dissolve
        "Jezera left Alexia sitting at the table. The book was still sitting on the table. Alexia could continue to read it if she wanted..."
        $ change_corruption_actor('alexia', +3)
        return
        
    "I Trust You, Mistress." if alexiaJezObedient:
        $ released_fix_rollback()
        #alexia concerned
        "Alexia sealed her eyes shut."
        "She tried to think back to when she’d first heard about the conflict. Had her father been the one to tell her? Or had it been from the village elder?"
        "But, instead she found herself in a more immediate memory. Dressed in black silk, pressed against a smooth warm body. Reaching out across a lake for a woman’s hand."
        #alexia aroused
        "Alexia brushed her fingertips on her neck."
        al "I trust you, Mistress…"
        al "..."
        "She looked down with a blush, not meeting her Mistresses’ glance."
        al "...The world really is such a complicated place. How much of what I learned was a lie? "
        "Jezera brushed the back of her hand slowly along Alexia’s cheek. Alexia exhaled softly."
        je "Not merely a lie. Shackles. People like to dress up the world. They do it for the same time we dress up."
        je "They put fancy gowns on the truth to make them powerful and proper. Armor to be intimidating. Or perhaps innocent white dresses to seem pure."
        "Jezera looked down, making a show of running her eyes up and down Alexia’s form."
        je "The only question is if there is even a naked body beneath all those layers?"
        "The longer Jezera talked, the harder Alexia found it to pay attention. Jezera knew the effect that her words had on the red head, and she was enjoying herself as a result."
        je "But, that’s enough rambling from me today, my dear. Enjoy your book."
        al "Right…"
        hide jezera with dissolve
        "Jezera lifted herself from the table and walked away. But, being her usual self, she made sure to swing her rear seductively as she walked. She knew Alexia wouldn’t resist watching her go."
        "And she was right."
        $ change_actor_num_flag('alexia', 'jezera_influence', 3)
        $ change_corruption_actor('alexia', +5)
        return
        
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

label library_goblin_thief:

scene alexia_library_1:

"Alexia had never considered the thought that sorting books might be “hard.” Before she started in the Castle library, she had always assumed it would be simple: just stick the books on the shelves and let the reader figure it out."

if differentAlphabetOrdersSeen:
    "Now that she had experienced the maddening difficulty of organization caused by differing Human and Elvish Alphabets, she was no longer under such delusions. Everything had its proper place, every book it’s ideal location."
    "But even that was simple compared to the issue of stacking books that had no discernible name, or were written in runes of an alien language."

"She was inspecting a particularly odd little unmarked book, with a leathery black cover and pages of a reddish tint, when a most unusual sight caught her eyes."
"A small goblin waddled past her row of books, his arms filled to capacity with half a dozen tomes of various thickness and sizes. The way he clutched them, he had clearly never carried a stack of books before."

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve

al "Hey!"

"The Goblin froze, his eyes going wide as he turned to face Alexia."

gob "Whot?"

al "What are you doing with those books?"

gob "Buildin’ a staircase wif ‘em. I dunno, human, what do you do wif books?"

"Alexia glared down her nose as the Goblin. As difficult as the work could be, she had grown somewhat protective of the books in the library. "

#alexia librarian angry

al "I read them."

gob "Good, then you know what I’m doin’ wif ‘em. Now if ya don’t mind…?"

"Alexia scanned the book titles engraved upon the spines of his books. Immediately she noticed that none of them had anything to do with one another in terms of subject. One was a filthy romance novel, another was an Elven Cookbook."

al "I’ve never seen you in the library before. Who gave you permission to take these?"

gob "..."
gob "Look missie, I gots family to feed. You see anybody else raising a stink about these dusty tomes? It’s not like I’m takin’ the family jewels here, ya know?"
gob "Now if you’ll excuse me…"

"Alexia sincerely doubted that the diminutive creature had any children to speak of. She watched him waddle towards the exit, books gathered in his hands, before reaching her hand out to stop him."

#alexia neutral

al "Just a second."

gob "What now, missie?"

al "This will only take a minute."

show cliohna neutral at cliohnaright with dissolve

"The regal sorceress appeared as if by magic, a book in her nose and her hand toying with a spell. She glanced up at Alexia, her brow furrowed with concentration."

cl "You don’t need to shout."

al "Do you know this Goblin?"

cl "I don’t make a habit of learning the names of every lesser life form that comes through here. Should I?"

#alexia librarian angry

al "He apparently is taking the books to ‘feed his children.’"

show cliohna angry at cliohnaright with dissolve

cl "Are you one of Cla-Min’s?"

gob "Who? "

cl "..."
cl "I suppose I’ll have to deal with this."
cl "Come along."

gob "Hey, I ain’t your-"

"Without lifting her gaze from her book, Cliohna snapped her fingers. The Goblin went stock still, his body going rigid as his eyes bugged out of his head. The sorceress strolled out of view, the Goblin following her with robotic, jerky footsteps."
"A half hour later, Alexia was finishing sorting the last of the books in her cart when the Goblin from before approached her."

al "Uh… hello?"

gob "I am sorry. Stealing books is wrong."

"The Goblin’s eyes were glassy, his body movement that of a puppet on strings. He pivoted on his heel, marching away in lockstep as he headed for the door."

gob "I must punish myself. I must never return."

#alexia librarian shocked

al "W-wait, what are you-"

"But the Goblin did not hear her, walking away in the direction of the exit. Alexia turned to face Cliohna, who was perched in a nearby corner, her face still buried in her book."

#alexia librarian concerned

al "What did you do to him?"

"Cliohna glanced up from her book, her eyes even and her face inscrutable."

cl "I chastised him."

"She looked back down at her book. Alexia shuddered and went back to her duties."

return

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

label perverted_POT:

scene alexia_library_1 with fade

"Another day, another research project. This time Alexia was in search of a particularly esoteric tome: {i}Epistolary of the Ortangian Rebellion: The Heresy that Never Was{/i}." 
"It sounded like pure gibberish; but Cliohna wanted it, so now she was on the hunt through the torchlit shelves of the Library’s deeper recesses."

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve

al "What section would it even be under? Religion, History? Maybe Magical anomalies?"

quest "Girl! You there, girl! I have need of your assistance!"

"Alexia nearly jumped in place, caught off guard by the booming voice echoing in her head."

al "What the hell?"

"She turned to look around, but saw nothing but another set of bookshelves. Come to think of it, she hadn’t been in this area of the library since she had last spoken to..."

#alexia librarian angry

al "Oh. It’s you."

pot "Indeed Alexia: it is I, the Prince of Tomes!"

"The bookshelf in front of her began to rattle and shift."

pot "You did not recognize me at first. Have you forgotten so quickly our previous encounter?"

if POTTaken == False:
    "Alexia sighed, her patience sorely tested by the sentient bookcase. She had ignored his offer before, and was sorely tempted to do so again."

elif POTscene == "Jezera":
    "She hadn’t forgotten. The book he had provided her had been surprisingly… ‘informative.’ Despite only reading the passage once, Alexia could still picture vividly the image of the intrigues and plots of the Dark Elven Court."
    "However, what stuck in her mind the most were the ‘Tongue Girls’ and the particulars of their use to their Elven mistresses. To Alexia’s shame, she had found her mind wandering towards that particular section in the dreary hours spent between the library’s bookshelves."

elif POTscene == "Andras":
    "She hadn’t forgotten. The book he had provided her had been surprisingly… ‘informative.’ Despite only reading the passage once, Alexia could still recall in detail the story of the knight Eleanor and her supposed fall from grace."
    "It was a heretical book, making wild and unfounded claims about one of the greatest heroes of the Solansian religion. Yet… the sheer taboo of her corruption, her degeneration into a demon's sexual plaything. It had managed to keep Alexia’s mind turning it over in her head for weeks after reading it."

else:
    "She hadn’t forgotten. The book he had provided her had been surprisingly… ‘informative.’ Despite only reading the passage once, Alexia still remembered the lurid tale of the Queen and the corruption of the Knights of Bloodmeen."
    "The tale had been so shocking: the debauched juxtaposition of a Knight’s sullied honor and a Queen’s utter debasement. There had been such passion in the wording, such creative description and loving detail, as if the author himself had been present for the events within."
    "It had been some time since she’d read it, but even now, in the late afternoon when the library went quiet, Alexia found her thoughts going returning to the Castle’s past, to the very halls that the Queen herself had walked - or rather, kneeled."
    
if POTTaken == True:
    #alexia librarian aroused
    al "...No, I haven’t."
    pot "Did I not deliver to you what I promised? Was it not the book you were looking for?"
    al "In a manner of speaking, I suppose."
    #alexia librarian neutral

else:
    pot "You did not take my advice last time, despite my honest intent to educate you."
    
pot "-And yet here you are, treading once more like a blind adventurer through my literary jungle, seeking knowledge that only I have the means to provide."

"Alexia rolled her eyes. She couldn’t believe she was having a debate with a talking bookshelf."

al "Cliohna says you’re not to be trusted."

"The bookshelf rattled on its legs as if shaking in anger at the sound of her name."

pot "{i}Bah{/i}! That Chaos-tainted witch is one to talk."
pot "A pity she did not heed the ‘warnings’ of wiser men when her own day of reckoning came."

al "What's that supposed to mean?"

pot "Knowledge is not a gift that is given freely, girl. And I doubt very highly you could afford the price of that particular morsel."
pot "But perhaps a lesser bargain would be amenable to you. You were searching for a book…?"

al "...Yes."

pot "You could spend a century sifting through the knowledge in this Library, and still be no closer to your goal."

#alexia librarian angry

al "What do you want from me, oh “mighty” Prince of Tomes?"

pot "In my time spent as the custodian of this mighty collection of arcane knowledge, I have found myself beset by the ravages of decay and neglect."
pot "The spells that bind me to this contemptible shelf preclude me from fading away, but the same cannot be said for my beloved tomes."

"A book near the top of the bookshelf fell from the stack, facing upwards at a horizontal angle, it’s faded yellow pages contrasting with the book covers around it like a rotten tooth."

pot "I would ask you to fix this particular book’s spine, the poor thing is a decade overdue for repair."

pot "If you do me this service, then I will find book you're looking for."

"Alexia stared for a moment at the top of the bookshelf, where the wounded Tome lay waiting. It wouldn’t be {i}that{/i} much trouble to repair a book for the mysterious Prince of Tomes… would it?"

menu:
    "Repair the book.":
        $ released_fix_rollback()
        "Heaving a hefty sigh, Alexia went to retrieve the rolling ladder. Mounting it into place, she climbed the steep steps to reach the top."
        al "This had better be worth it, you pompous talking shelf..."
        pot "I heard that."
        "Heaving the hefty tome in her arms, Alexia descended the ladder once more, huffing and puffing with the exertion. She set the book down, noting that the cover was blank."
        "Alexia opened the heavy cover, spreading the yellow-leaf pages wide. The pages were filled from top to bottom with incomprehensible scribbles: half formed geometric shapes surrounded by scratchy handwriting in times that were unfamiliar to her."
        if POTscene != "None":
            "Remembering her past encounters with alien books, Alexia decided to err on the side of caution, keeping her eyes off the pages themselves and focusing on repairing the book."
        "One look at the spine of the book told her that there was a wide gap between the spine and the pages of the book. An easy enough fix, all things considered. Why hadn’t someone done this already?"
        "Alexia stood the book on its tail, then gently stuck her index finger into the gap between the pages and the spine, digging her finger as far inside as possible without causing more damage. The gap spread apart."
        pot "Mmm..."
        #alexia librarian neutral
        al "I’m sorry, did you say something?"
        pot "Silence! Finish your work, girl!"
        #alexia librarian angry
        al "Okay, okay! Jeez."
        "Alexia took her sewing needle, dipping it into the bottle of adhesive. She then gingerly inserted the needle into the gap between the pages and spine and twirled it against both the text block and the spine to ensure an even coat of adhesive."
        pot "Oh yes..."
        al "What?"
        pot "{i}Did I command you to stop?{/i}"
        al "Ugh!"
        "She was getting annoyed now. The Prince was acting anything but princely towards her. Grumbling to herself that it was for a greater cause, Alexia moved to the final stage. Now that the glue was applied, she took the book and pressed it tight between her hands, applying pressure to ensure the adhesive stuck. "
        #alexia librarian happy
        al "All right, I think we’re just about-"
        #alexia librarian shocked
        pot "{i}Aaaah!{/i} B-by the seven syllables!"
        pot "{i}Uuhhn! Urgh!{/i}"
        #alexia librarian angry
        pot "Harder! {i}Harder{/i}!"
        al "Y-you-"
        al "You {i}perverted pile of paper{/i}!"
        pot "Oh, that’s it: tell me how bad I’ve been."
        pot "Show me how rough you can be: bend my spine, rip my pages!"
        "Alexia dropped the book to the round and stood to her feet in a rush. She wiped her hands against her skirt as if to cleanse herself of the mental image."
        al "By the Planes of Chaos, you are disgusting!"
        pot "Yes, I’m a mongrel! Punish me! Rub dirt betwixt my pages, pour wine on my cover!"
        "Alexia stormed away from the semi-orgasmic exultations of the libidinous bookcase. Her cheeks burned with anger as she ignored his calls to her back. She no longer cared whether she found that book for Cliohna or not."
        pot "Get back here, wench!  You need to put the book back!"
        "Alexia did not get back there."
        return                                                                                                                                                                                                                                
        
    "Refuse to repair the book.":
        $ released_fix_rollback()
        al "No. I think I’ll be fine. Have someone else repair it, if it’s such an easy task."
        pot "You’ll be back, girl. When you search from the highest rafters to the lowest piles and find your hands empty, you will beg for my aid."
        "Alexia rolled her eyes, turning away from the phantom bookcase with a huff as she went about her duties for the day. Two hours of fruitless searching later, she gave up on finding the book."
        return


