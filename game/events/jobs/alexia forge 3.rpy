init python:
    event('clash_of_empires', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'", 'week > 24',), run_count=1, group='alexia_forge', priority=pr_npc)
    event('alexia_shackle_fantasy', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'",'all_actors["alexia"].corruption > 30',), run_count=1, group='alexia_forge', priority=pr_npc)
    event('angel_in_the_ash', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'", 'week > 24',), run_count=1, group='alexia_forge', priority=pr_npc)
    
label clash_of_empires:

scene bg22 with fade
show alexia forge neutral at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve

"Alexia came to work that morning to a contentious sight. Greyhide was leaning against his anvil, his hammer set aside on his work bench."
"Normally the burly Minotaur would already be hard at work by the time Alexia arrived, but the presence of the two warriors arguing back and forth in front of him had broken his peaceful routine."

gh "I can’t fill two orders at once."

"The first warrior, a tall, imposing human clad in black armour and a long, white cloak let out a contemptuous snort."

merc "Then fill mine first. The Orc can wait."

"The Orc commander standing next to him let out a growl, baring his long rows of teeth."

show orc soldier neutral behind bg22

os "Shut yer trap, Human. I as’ed first, and the bull don’ take orders from {i}you{/i}."

show alexia forge concerned at midleft with dissolve

"Alexia watched with growing concern as the human mercenary turned to face the Orc. Despite the Orc’s larger stature, he did not seem fazed in the slightest."

merc "I can tell by the doltish look in your eyes that basic arithmetic is not your expertise, greenskin."
merc "But even {i}you{/i} should know the difference between a gaggle of Orcs and a force of well-trained soldiers."

"The Orc let out a boisterous guffaw, as if the very idea of the mercenary quoting numbers at him was a joke."

os "One Orc is worth fifty o’ yer twiggy gits, humi. Let’s see what ‘dat training does ya when me and my boys crash into yours."
os "You’ll he hidin’ behind ‘dat shield wall just long enough fo’ me to bash yer head in."

"The tension in the room grew. Alexia found herself taking several steps back so as to avoid getting caught in the middle. Greyhide remained unmoved."

merc "I’m fielding two companies for the Twins near Reave Keep. You’re leading a glorified rabble."
merc "My men are fighting with rusted blades and cracked maces, they need these weapons to be an effective fighting force."

os "Sod that! My lads are headin’ to the front lines. We need shiny new axes for skull-splittin’."

merc "Why bother? Give a rat a bastard sword, he still won’t know how to swing it. Your kind couldn’t hold a battle line if they were tied in chains to one."

"The Orc let out a roar of anger, reaching for his weapon. The mercenary did the same."

os "You callin’ my boys weaklings, ya mouthy pinkskin?"

merc "I’m calling them cowards."

#greyhide angry

gh "{i}Enough!{/i}"
    
show alexia forge shocked at midleft with dissolve 

"The booming roar of the enraged Minotaur silenced the two’s bickering."

gh "No weapons. This is my forge, not your battlefield. Besides…"

#greyhide neutral

"Greyhide gave a little wink in Alexia’s direction."

gh "You’re scaring my assistant."

if society_type == "feudalism":
    gh "This should settle things: what is your noble rank?"
    "The mercenary shot the Minotaur a look of confusion."
    merc "My… rank? I’m the Commander of the Third Sons."
    gh "No. Your court rank. The Twins assigned noble titles."
    gh "They sent a letter to the castle staff. We are instructed to favour men of higher rank when conflicts arise."
    gh "We have a conflict. What is your rank?"
    "The mercenary huffed and blustered."
    merc "I-I have not been granted one, yet!"
    "Sensing blood in the water, the Orc let out a booming guffaw."
    os "Aw, has the poor humie not earned ‘is fancy title, yet?"
    os "Too bad, ‘cause as a servant o’ the Twins, serving directly under ol’ Andras, I’s a Paigon."
    "The ennobled Orc flashed his opponent a roguish grin, coming almost nose to nose with him as he revelled in his superior station."
    os "But {i}you{/i} can just call me ‘M’lord.’"
    "The Orc commander then turned to Greyhide, ignoring the mercenary completely."
    os "So, about them’s axes."
    gh "I’ll get started today. You should have the shipment by next week."
    os "Good, see dat it’s done fast, Lord Andras doesn’t like to be kept waitin’."
    "The Orc turned, strolling from the room as though he were an Emperor at his coronation. Alexia watched him pass, and he shot her an unsubtle wink."
    "The mercenary looked like he was inches away from drawing his blade. He thought better of it after glancing at the huge minotaur, releasing his white-knuckled grip on the hilt and turning to leave as well."
    merc "Bloody, {i}fucking{/i} greenskins."
    "The Mercenary continued to mutter to himself as he swept from the room, moving with an angry quickstep as he seethed at the insult. He was powerless, and he knew it. It made the sting of the indignity that much worse."
    show alexia forge neutral at midleft with dissolve 
    "Alexia approached Greyhide. He rubbed his chin thoughtfully."
    al "That went well."
    gh "It seems the Twin’s choice was correct."
    al "Which one?"
    gh "Making nobles. It streamlined the process. Now everyone has a superior."
    al "You’re probably right, could have turned bloody otherwise."
    al "...I suppose I should be grateful we’ll have a lighter workload this week."
    "Greyhide shot her a grin, taking his hammer in hand and turning to his anvil."
    #greyhide happy
    gh "Fewer blades doesn’t mean less work. Just more time to get it right."
    gh "Come, the forge awaits."
    return

else:
    "The mercenary lifted his head and laughed."
    merc "You have… what, maybe fifty? I have four times as many men as you at least."
    merc "If those axes end up in your hands before {i}my{/i} men get supplied..."
    merc "I’ll burn down your camp, slaughter your soldiers and sell your pretty new axes myself to pay for my weapons."
    os "You’d dare attack one o’ the Twins’ servants, human?"
    merc "It’s a new day, Orc. Like the Twins themselves say: might makes right."
    merc "Who do you think they'll miss more: fifty greenskin barbarians on guard duty, or a force of hardened mercenaries?"
    "The Orc glared at the mercenary, but Alexia could see the wheels turning in his head. He growled, then stormed out of the room without another word."
    "The mercenary smirked, turning to face Greyhide with a flourish."
    "If that is all? I expect my blades as soon as possible, Blacksmith. Good day."
    "The mercenary strode from the room with a happy bounce in his step, humming a tune as he blithely brushed past Alexia."
    "Alexia approached Greyhide, who let out a small sigh."
    #greyhide annoyed
    gh "Arrogant ass."
    show alexia forge neutral at midleft with dissolve 
    al " ...Guess we have a lot more work to do, huh?"
    gh "Yes."
    #greyhide neutral
    gh "Come, enough politics. The forge awaits us."
    return

##############################################################################
##############################################################################
##############################################################################

label alexia_shackle_fantasy:

scene bg22 with fade
show alexia forge neutral at midleft with dissolve

"The time had come to do inventory again. Monotony personified; Alexia hated it. Of all the odious tasks she had to perform in the smithy, this one was by far the most mind numbing."
"Every errant piece of metalwork, every stray nail and every rusty hinge had to be accounted for. Some of the pieces lined across the shelves and stacked on the walls had decades of dust layers, coating them in a fine sheen of grayish moss."
"Bloodmeen was, after all, still only half-occupied by its new ownership."
"Alexia had made a game of the tiresome task: keeping track like a scorekeeper for a children’s game with little tally marks on her clipboard. It was wasteful, but at least it helped to mitigate the tedium."

show alexia forge angry at midleft with dissolve

"The pounding cacophony of Greyhide’s hammer was particularly piercing today, even in the farthest corners of his forge. Alexia had never quite gotten used to the harsh clanging of metal upon metal, but today it was giving her an especially nasty headache."
"She ignored the racket as much as she could as she moved slid like an abacus from object to object, shelf to shelf, itemizing and tallying everything she came across."

show alexia forge neutral at midleft with dissolve

"It was only once she came to a particular dusty shelf that she was given pause. There, sprawled in great heaps in a disorganized pile, was a mass of dark metal." 
"Shackles, rough hunks of black iron and chain hammered into the shape of human wrists. The mark of slavery."
"Some dim part of Alexia’s mind knew that this was the true horror of the Twin’s regime. For them, Slavery was a means and an end, a literal and figurative state in which there are only those who rule, and those who serve. And the ‘rulers’ could be counted on but one hand."
"Domination, control, the dismemberment of all other’s wills in the face of their own, crowning ambition. This was the future that the Twins envisioned." 
"Staring at the row upon row of slave shackles, only half-listening to the heaving roar of Greyhide’s furnace as he forged their weapons of war, Alexia felt their domineering presence acutely."
"But… was it really that bad?"

if alexiaJezObedient == True:
    "Jezera had expanded her horizons on the subject. Where once Alexia had recoiled in horror and disgust at the humiliations, now she appraised it with a gemcutter’s practiced gaze."
    "Lady Jezera was good at that: changing opinions, shifting one’s point of view from the norm."
    "Perspective was a curious thing. Entire world views shifted and internal realities collapsed at the slightest tectonic shift, and Alexia’s had been particularly shaken."
    "It was not her own submission she sought, so much as the subtle power play at work between the competing personalities."
    "Sure, Alexia might attempt to rise up, only to be struck down every time by Jezera’s more dominant force of personality, but that was ultimately not the point of the exercise. Sex had become, for the first time in Alexia’s adult life, a dangerous, exciting thing again."

elif alexiaAndrasObedient == True:
    "Andras was a brute. A foul-mouthed and foul-tempered tempest whose rages were as fierce as his lovemaking."
    " He had subjugated her, {i}humiliated{/i} her, left her a wet and quivering mess on the floor, making all the while an abject mockery of her broken marriage."
    "...And yet, he had taught her so much. He had shown her the ugly truth of things: that mutual animosity could breed intense passion, that submission could be daring, that ecstasy was not the {i}antithesis{/i} to agony, but rather its parallel."
    "Humiliation was not a punishment to be meted out. Rather, it was a delicacy to be savoured."
    
else:
    "Alexia was no great lover of the Twins, to be certain. They had burned her home, slaughtered her loved ones and ripped her and her beloved husband from the only peaceful life that they had ever known."
    "But she had learned much in her time here in Bloodmeen Castle, scurrying about like a rat beneath the floorboards."
    "Slow indoctrination into the deeper mysteries of her own repressed sexuality had taught her that submission was not as repulsive a state of being as she had once thought."

"As she stared at the row upon row of manacles, Alexia wondered what kind of use they had seen, what use they might see in the future."

menu:
    "Continue with work.":
        $ released_fix_rollback()
        "Alexia shook herself. What was she doing? She still had a mountain of work to do, and so little time to do it."
        "Casting a long, thoughtful look at the manacles, she returned to her task, tallying up and listing the inventory, praying for a respite from the interminable tedium."
        return
        
    "Daydream about the shackles.":
        $ released_fix_rollback()
        jump alexiaShacklesSex

label alexiaShacklesSex:

show alexia forge happy at midleft with dissolve

"She closed her eyes and pictured it, her mind's eye brimming with lurid imagination as the fantasy began to play out inside her head."

scene cg603 with fade
pause 3

"She was in the courtyard, standing atop a huge wooden platform in the middle. A crowd had begun to form, milling about in excited disharmony as chattering voices and the rough grunts of Orcs filled the air."
"She was naked, stripped of all pretense of dignity by her captors, not even a scrap of loincloth to cover her womanhood as she was paraded out upon the stage."
"They had shackled her, slapping heavy chains of black iron around her wrists. It was mostly for show - it’s not like Alexia could actually {i}go{/i} anywhere, even if she tried to run."
"But such wasn’t the point of the manacles, for they were merely the physical indication of her submission. As a crown is to a King, so too are chains to a Slave."
"She was not alone. Others had been gathered here for this sinister auction. Humans, Elves, Goblins and Orcs. All female, all shackled and bound and nude, paraded across the stage like a menagerie at a circus."
"The roar of hundreds of masculine voices greeted her as she was led across the stage in turn. Hooting catcalls and jeering laughter followed her every trembling footstep, her face growing hot and her cheeks flushing. "
"She heard them, the hungry jackals. They snarled like beasts, held at bay only by the meager cadre of armed guards standing watch at the edges of the platform. Imploring arms reached out, scratching at the air as if to seize Alexia from the stage through sheer force of will alone."
"But these beasts were not driven to such frenzy by Alexia herself. “Alexia” was immaterial. They were baying for {i}her{/i}, for the captive female in their midst. She wasn’t a person, she was instead the embodiment of her physical traits: her red hair, her perky breasts, her soft curves and milky skin."
"A kind of lurid malaise fell upon the monsters lurking out in the crowd, a lust borne of malicious envy, of selfish covetousness. As she looked out across the crowd, she saw not horniness, but hunger and greed. She was a product, a thing to be purchased."
"The auctioneer, a tall, leering human with a bearded face and venturesome hands led her along to the front of the platform. It was her turn to be sold."

auct "Now we got us some prime meat!"

"The crowd let out a raucous roar of approval. Alexia, unable to look away or avert her gaze from the leering throng of voyeurs staring directly at her, shivered and gasped, mortified and electrified in equal measure."

auct "I know how you lads love a good story, and by is this one a doozie!"
auct "Number 423 is a special case: a {i}volunteer{/i}!"

"Jeering laughter followed his statement, and Alexia felt her face falling. Was this really all she was now? A number in a list? A morsel of meat to be savored by the mighty?"

auct "She’s young, fresh, but most importantly: {i}experienced{/i}."

"Alexia yelped as she felt the auctioneer suddenly reach down and inexpertly finger her, directly in front of everyone. To her everlasting shame, she was wet. His finger slid right in."

auct "Don’t mistake the doe eyes for innocence lads, this one’s a Grade A Whore."
auct "Her cunts as tight as a bear trap."

"{i}SMACK{/i}. The Auctioneer planted an open palm directly across Alexia’s bare bottom, leaving a stinging red mark in its place."

auct "Her arse is as perky as a bar wench after a few stiff ones on the job! And those {i}lips{/i}..."

"Alexia said nothing as the Auctioneer withdrew his curling fingers from her pussy and stuck them in her mouth, applying his own form of lipstick as he ran them around."

auct "These luscious lips of hers have milked more than their fair share of cocks, let me tell you. She’ll suck you dry, then beg for seconds!"

"More laughter. Alexia’s face burned red hot with humiliation. She could not bear to look at them, yet she could not look away. They were all there, {i}staring at her{/i}."

auct "We’ll start the bidding at 500 pieces. Now that may seem steep to the keen-eyed among you, but she’ll earn her keep in a day. Trust me on this one boys, I speak from experience! Har!"
auct "Now, do I hear Five hundred?"

"To Alexia’s horror (and, secretly, to her thrill) a dozen hands or more raised. A vicious bidding war ensued, where her price climbed higher and higher, till even the Auctioneer was breathless in his excitement over the prospective monetary windfall."
"Finally, a lone hand raised, when none others were willing to go higher. A clear voice called out through the din, giving the highest number yet by a wide margin."

if alexiaJezObedient == True:
    scene cg673 with fade
    show jezera happy behind cg673
    pause 3
    je "Three thousand gold pieces. And fifty more if you can stick her in some finery first."
    "To Alexia’s shock, it was not a man who had purchased her, but rather the graceful, purple form of a woman. She had been lurking in the crowd the entire time, like a quiet spider spinning her web amongst the cover of foliage."
    "The woman caught Alexia’s gaze, and she smirked. And just like that, Alexia knew she was owned. It was that easy, a simple smile had convinced her of the futility of resistance. This woman could pin her down in a way that no manacles ever could."
    "...Worse still, Alexia’s heart began to pump faster at the thought of it. It was one thing to be ravished by a man seeking some piece of meat, it was quite another to be coveted by {i}her{/i}."

elif alexiaAndrasObedient == True:
    scene cg604 with fade
    show andras smirk behind cg604
    pause 3
    an "Three thousand gold pieces, and not a penny more."
    "Alexia’s heart skipped a beat. A hulking red brute had somehow managed to weave his way through the crowd without her noticing. Like a shark circling chum he had come upon her silently, with a unity of purpose not unlike that of a predator."
    "Sizing up his prey, his laughing, mocking eyes locked with hers, and an unspoken conversation ensued."
    "In an instant he disarmed her of her internal defenses. Left helpless in form by the shackles, she was now also shackled in spirit. She was his, a piece of property to do with as he would." 
    "And Alexia knew it. Despite her own embarrassment, if this hulking creature were to take her then and there atop the platform, with all present watching, she would spread her legs and cry out his name."

else:
    scene cg674 with fade
    show rowan necklace neutral behind cg674
    pause 3
    ro "Three thousand gold pieces."
    "Alexia’s heart leapt. There, in the crowd was her buyer: a slender man in a heavy cloak, whose piercing gaze she could make out even from this distance."
    "Her body trembled as they made eye contact, a true sense of helplessness washing over her. The Auctioneer made a great show parading Alexia around like a trained beast who had won a contest, but she was only half paying attention now."
    "He was there, watching her: the perfect specimen. A being whom Alexia - enslaved, ensnared and surrounded by threats - could give her all to. He {i}owned{/i} her now in body."
    "All that was left was to own her in spirit as well."

"It was all so wrong. She didn’t want to be owned! She was a human being, with feelings and thoughts and-"
"But the pale excuses sputtered and died like withering vines in a fire. She could not even finish the thought before they blew away into the wind. Alexia realized that she was merely fooling herself. It was as the auctioneer said:"
"She had {i}volunteered{/i}."
"The manacles were heavy about her wrists. Her body twisted this way and that, her hips swaying as she felt a profound warmth rise like a tide in her nethers. "
"Her need to be ruled, to be {i}subdued{/i}, to be put on her back and left helpless to the machinations of others overrode her instincts. Naked, she reached down with her manacled hands and began to finger herself in front of everyone, proclaiming to the world that-"

scene black with fade
show greyhide neutral at center with dissolve

gh "{i}Alexia{/i}! Where are you, girl?"

scene bg22 with fade
show alexia forge shocked at midleft with dissolve
show greyhide neutral behind bg22

al "{i}Ah?{/i}"

"Alexia’s mind roared back to the present with enough speed to give her whiplash. She glanced around in confusion, carried back to reality from her horny fantasy by the booming roar of the Minotaur in the room."

gh "The forge needs heating, but you are still doing inventory!"


"Alexia looked down stupidly at her hands, momentarily taken aback at where she was and what she was doing… it had all been so {i}real{/i}. It took her several seconds to find her voice, and when it came, it came as a croaky whisper."

show alexia forge aroused at midleft with dissolve

al "I-I was just-"

"She stared for a long moment at the manacles stacked upon the shelves. Her spine tingled at the vivid daydream, her mind alight with the sights and sounds of what she had experienced as a would-be slave on the auction block."

gh "There is no time, come tend the bellows!"

show alexia forge concerned at midleft with dissolve

al "Y-"

"Alexia hesitated for a half second, staring for another long moment at the shackles. She (regretfully) shoved the image from her mind and returned to the present."

show alexia forge neutral at midleft with dissolve

al "Coming, Greyhide!"

"At least she’d have something to think about after the work day was over…"

return

##############################################################################################################
##############################################################################################################
##############################################################################################################

label angel_in_the_ash:

scene alexia_forge_1 with fade

"Busy days in the forge could make the workspace look like a child’s tale of the hellish Planes of Chaos." 
"Volcanic heat from white-hot forges spewed pyroclastic ash into the narrow, cramped spaces. The air was choked, and burning and stuffy. Black soot rained down on Alexia’s head in a near constant stream as the fires belched and the metal sang."
"Greyhide’s hammer rose and fell, rose and fell in an endless beating pattern. The loud roar of the fire as the bellows blew became a snarling beast, huffing and snorting as molten light poured from its gaping maw."
"Alexia did her best to cope in the bleak circumstances. She went where she was bidden, taking on whatever task was needed to ease the old Smith’s burden."
"Greyhide churned out weapon after weapon in an endless cycle of heating and cooling, shaping and warping and hammering till the blade tips shined and the sword edges glimmered."
"It was hard work, and it was grim work. Greyhide bent himself utterly to the work, his thick brow knitting together and his flat teeth grinding as he spent his prodigious  strength in mighty swings."
"So great was the task, and so engrossed was he in his duty, that Greyhide had already foregone even a meager luncheon, choosing instead to use the time productively. Greyhide pushed it to its blasting height, stifling the already stuffy air with hot ash."
"Alexia felt a momentary pang, a selfish longing to feel a breath of fresh air and the wind on her face. Her lips twisted into a grimace as she pumped the bellows harder, redoubling her efforts in the hopes that Greyhide would, with her aid, be finished faster. "
"Lost, alone, trapped in a place that reminded her very much of a demon’s realm, Alexia found her mind wandering back to happier, more innocent days. As she looked at Greyhide, a song arose unbidden to her lips. She began to hum a tune."

scene bg22 with fade
show alexia forge concerned at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve

al "How cold, how cold,\n Do the barren hearths grow,\n When the wind is wafting with winter’s chill?"

"It was an old tavern song, one she had heard her mother sing a hundred times or more growing up as a child in Arthdale."

al "Do you know, do you know,\n What the frigid mind will do,\n When the fires die low, and the creaking walls grow shrill?"

"As she hummed her voice grew louder, carrying over the hammer of the forge. Though Greyhide gave no indication he had taken notice, his ear turned to listen."

show alexia forge neutral at midleft with dissolve

al "A bull, a bull,\n Freezing in his bull’s pen\n Every night, thinking might he never be warm again?"
al "So cold, so cold,\n Was the wind in the weald,\n That surely soon the Bull would by dire chill be slain."

"The Minotaur paused in his hammering, casting a short glance in Alexia’s direction before resuming his work."

show alexia forge happy at midleft with dissolve

al "But a light, but a light,\n Was shining hot, burning bright\n In the farmhouse of his mistress through the window pane."

show alexia forge neutral at midleft with dissolve

al "How wild, how wild,\n Was the wind in the weald,\n As it blew a stray thought through the weary beast’s brain?"

"Had things proceeded as expected, Alexia’s squalid tune would have likely faded off into nothingness as her mind drifted, and the arduousness of the bellows stole her attention." 
"But then, like a rising storm, the deep bass of Greyhide’s voice sang above the din of his hammer strokes."

show alexia forge shocked at midleft with dissolve

gh "Stand up, stand up,\n It couldn’t hurt much to look\n Perhaps her wide hearth is a little warmer than this pen."

show alexia forge happy at midleft with dissolve

al "How bold! How bold!"

gh "How bold! How bold!"

al "Trudging through ice and snow,"

gh "Trudging through ice and snow,"

al "As the Bovine cross’d the wintry gap of glade and glen."

gh "As the Bovine cross’d the wintry gap of glade and glen."

"Together their voices formed a lyrical harmony, trading words back and forth as each took up the tune in turn." 
"The sway of Greyhide’s hammer took a new cadence, following the beat of the simple song. Despite herself, Alexia found her turns at the bellow taking on much the same rhythm."

show alexia forge concerned at midleft with dissolve

al "A knock, a knock,"

gh "A knock, a knock,"

al "A gentle jingling at the lock."

gh "A gentle jingling at the lock."

al "Alerted the fair maiden to the Bull in the snow."

gh "Alerted the fair maiden to the Bull in the snow."

"At this Greyhide took up the voice of the Bull. Alexia watched in awe as his booming voice filled the room."

show greyhide sad at cliohnaright with dissolve
show alexia forge shocked at midleft with dissolve

gh "Hello, hello\n I do not mean to bring woe\n But I couldn’t help but notice your hearth’s warm glow."

show alexia forge concerned at midleft with dissolve

gh "I’m cold, I’m cold,\n Many things I don’t know,\n But even an old Bull knows when he’s run out of road."

show greyhide neutral at cliohnaright with dissolve
show alexia forge neutral at midleft with dissolve

gh "I’m tired, I’m tired,\n May I rest by your fire?\n I will do any task, and bear any load."

"Alexia laughed aloud, charmed beyond words at the wondrous, discordant experience of such a song in the midst of all this ash and misery. Her voice sang as bright and flowing as her bellow-strokes."

show alexia forge happy at midleft with dissolve

al "She smiled, she smiled!\n The fair maiden was beguiled,\n And she let the old Bull share her hearth for awhile,"
al "Time passed, time passed,\n As the frost turned to grass,\n And the shivering cold winter was finally exiled."

"Time was passing much as the song said. Before Alexia knew it, they were much farther along in their work order. Still the song continued, the Minotaur and his human helper’s voices blending together towards the rising crescendo."

al "But the bull, but the bull,"

gh "But the bull, but the bull,"

al "Rested, warm and so full,"

gh "Rested, warm and so full,"

al "No longer wished to be stranded alone in the cold."

gh "No longer wished to be stranded alone in the cold."

show greyhide sad at cliohnaright with dissolve
show alexia forge neutral at midleft with dissolve

gh "Please no, Please no,\n I do not want yet to go.\n For I still recall the feeling of your hearth’s warm glow."

"Greyhide’s large eyes were upon her as he sang, his hammer rising and falling a little slower than usual. There was a wide, toothy smile upon his bestial visage."

show greyhide neutral at cliohnaright with dissolve
show alexia forge shocked at midleft with dissolve

gh "I’m warm, I’m warm\n And we have pass’d the snowstorm,\n But I’d dearly like to bathe in your heart’s heat, again."

if alGreyhideForgeSex == True:
    show alexia forge aroused at midleft with dissolve
    "Alexia blushed, seeing the low, sexual undertone of Greyhide’s voice as he sang the insinuating lyric."

gh "Why try, why try,\n Why work when you can lie,\n Upon a bed of green grass, and soft summer rain?"

"Greyhide set aside his hammer, and Alexia let go of the bellows, their voices carrying and echoing in the cramped confines of the forge as they turned to face one another."

show alexia forge happy at midleft with dissolve

al "Fair maiden, fair maiden,\n So many burdens ‘pon you are laden\n But the Bull ne’er the less, will still go where he wills."

"Their voices rose, together forming a perfect note as they reached the final line. Alexia walked slowly towards Greyhide, a soft smile spreading across her face as the two finished the song in harmonious unison."

show alexia forge neutral at midleft with dissolve

al "Do you know, do you know,"

gh "Do you know, do you know,"

al "What the frigid mind will do,"

gh "What the frigid mind will do,"

al "When the fires grow high, and the creaking walls..."

gh "When the fires grow high, and the creaking walls..."

al "grow..."

gh "grow..."

if alGreyhideForgeSex == True:
    show alexia forge concerned at midleft with dissolve
    al "...still?"
    "She held the note for a long movement, trailing off into a sonic lull that made the forge’s fires sound like deafened whispers."
    "Alexia’s footsteps crossed the final threshold between herself and the anvil on which he worked. Greyhide turned to face her, his rippling muscles silhouetted in the harsh light of the blazing forge. He looked down his snout at her, a soft smile tugging at his snout."
    gh "You sing well, little one."
    "Alexia could not help herself. Something heavy in her chest bade her to feel the grasp of this gentle giant. She reached out and took Greyhide’s hand in hers, pulling him down to her level."
    "The old Bull obliged, leaning forward as the fair maiden planted a nervous peck upon his cheek. Her face, covered in soot and ash as it was, left a little black smudge on his fur when she withdrew."
    show alexia forge aroused at midleft with dissolve
    al "As do you."
    "Greyhide’s smile deepened. He said nothing, merely picking up his hammer and resuming his work. But Alexia could see it: a soft relaxing of the shoulders, a gentle soothing of the spirit."
    "Greyhide worked as hard as ever, but something in the song had given him the strength to continue. Filled with newfound purpose, the two finished the day’s heavy labours with a song in their hearts and a warmth in their hearts."
    #small bonus to forge production - TO DO
    return
    
else:
    show greyhide sad at cliohnaright with dissolve
    gh "..still?"
    "Alexia’s footsteps crossed the final threshold between herself and the anvil on which he worked. Greyhide turned to face her, his rippling muscles silhouetted in the harsh light of the blazing forge. He looked down his snout at her, a soft smile tugging at his snout."
    show alexia forge happy at midleft with dissolve
    al "You have a wonderful voice, Greyhide."
    "Greyhide’s large cow eyes gleamed with mirth. He let out a happy grunt and turned away, hiding his appreciative smile behind his rippling shoulder blades."
    gh "Thank you."
    "As if those words alone were enough, Greyhide picked up his hammer and went to work."
    "He said nothing more on the matter, nor did he reference the fact that he had joined her in song again. But the happy memory of the event played on repeat in her mind for the remainder of their labours."
    "She found herself humming the song of the Winter Bull for the rest of the day, easing the work and making the long hours seem just a little bit shorter."
    #small bonus to forge production - TO DO
    return

