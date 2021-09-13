#Level 3 party:
#Requirement: None. Triggers on entering mine, usual mine menu appears at the end of the event
init python:

    event('mine_level_3_party', triggers=('map_res_6', 'map_res_7', 'map_res_8',), group='mine', run_count=1, priority=pr_map_res)
    event('deep_in_her_mines', triggers=('map_res_6', 'map_res_7', 'map_res_8',), group='mine', run_count=1, priority=pr_map_res)

label mine_level_3_party:
scene bg55 with fade
show rowan necklace neutral behind bg55

"Taking a bit of a detour, Rowan approached what he knew was an abandoned iron mine. A couple of years back, he heard from a passing merchant about it being overrun by monsters, though by then he had already retired from being a hero and general, and was enjoying a peaceful family life with Alexia."
"Never really one for adventuring – he was a soldier in the past, not a glorified mercenary for hire – he chose to leave the matter to the local authorities."
"Though knowing the level of enthusiasm with which lords react to peasants asking them to do their damn job of protecting the countryside, he honestly expected the mine to be still filled with monsters."

if avatar.corruption > 59:
    "Not like that would be an issue, now that he had literal disposable orcs at the snap of his fingers. "
else:
    "Not like that would be an issue, with the orcs he had under his command."

"Maybe if said monsters turned out to be driders, he might get a chance to grab a couple of eggs. Two birds with one stones, if lady luck smiles on him."
"Filled with such optimistic thoughts, he approached the slope leading to the mine entrance-"
"- and instantly noticed the faint trail of campfire smoke on the horizon."
"Sensing trouble, Rowan stepped off the dirt path he was on, and entered the nearby forest. With his usual expertise, he started sneaking up to the source of the unexpected smoke."
"As he drew nearer, he started overhearing snippets of a conversation between two particularly agitated people. A minute later, he was close enough to grasp the words being said."

qais" … then you shouldn’t have tossed in so much wood into the fire!"

"The first voice complained, annoyed. It sounded male, young."

shee "Yes, yes, blame everyone but yourself."

"Another answered. This one was high pitched. Girly."

qais "I did everything right! I got the recipe from the innkeeper in Rastedel and followed it to the letter!"

shee "Horseshit! Show me that- "

qais "Hey knock it of you bi-"

isaa "Please, there’s no reason to be upset! We still have rations!"

"A third voice, sounding very young. Either a young boy or another girl."
"Rowan crept in closer. A minute later, he was close enough to see who the voices belonged to."
"Near the entrance to the mine, a group of… Adventurers, apparently, set up camp, and was in the middle of bickering with one another in a rather lively fashion."
"A young sorceresses, dressed in red robes, tried to lay her hands on a piece of paper desperately protected by a young man in leather armor. These must have been the first voices he heard."
"To the side, he noticed the likely owner of the third voice – a short haired… Boy, Rowan guessed? No older than 16. Hiding his face in his hands, he looked like was about to cry."
"There was another person, who kept his silence so far. A burly, serious man, with a long beard, tanned skin and a gentle, if disapproving gaze, sat next to the young boy. He wore a simple shirt, but Rowan quickly noticed a breastplate and a shield lying nearby."
"Again, Rowan crept a bit closer, kneeling behind one of the trees, trying to get a better look at the odd party, and to wait and see how the situation develops -"
"- but he wouldn’t get the opportunity to do so."
"He must have passed some sort of invisible line, because the the sorceresses head suddenly snapped upwards, and she turned her gaze in his direction."

$ sheenaName = "Sorceress"

shee "We have company."

"Like a well oiled dwarf mechanism, the group instantly sprung into action. The big man in the back jumped forward, grabbing his shield and sword, placing himself in the front."
"The other man and the woman positioned themselves behind him, by his sides, with the man taking out a crossbow, while the sorceress’s hand burst ablaze with magical fire."
"The boy lingered in the back, protected by the three clearly more experienced fighters."

$ qaisName = "Burly man"

qais "Show yourself, interloper!"

"With a soft sigh, Rowan stood up, and waved his arm from behind the tree."

ro "I mean you no harm! But I would prefer if the other guy lowered his crossbow before I leave cover."

"The three exchanged glances, then with some hesitation lowered their weapons."

hide rowan
show rowan necklace neutral at midleft with dissolve

"Rowan showed his face-"
"-and the woman gawked at him instantly."

shee "Holy shit."
shee "It’s Rowan Blackwell."

show rowan necklace shock at midleft with dissolve

"All of them, Rowan included, looked at her in surprise. It wasn’t often he would be recognized so quickly. There wasn’t anything particularly characteristic about his face or clothes – bar the magical amulet, but this was a recent addition."

qais "… Are you certain?"

shee "Yes! How could I not be!"

shee "Didn’t I tell you like, a thousand times how I saw Deanara and her party in Rastedel!  Of course I would recognize him!"

show rowan necklace neutral at midleft with dissolve

"The sorceress quite literally jumped up with giddiness, and waved at him, urging him to come closer."

shee "Mister Blackwell, please, join us!"

show rowan necklace happy at midleft with dissolve

shee "… We’d offer drider omelettes, but SOMEONE fucked up the recipe!"

show rowan necklace neutral at midleft with dissolve

"… Drider omelettes?"

$ bernName = "Young man"

bern "I told you I did not!"

qais "I don’t think it’s even possible to cook a drider egg…."

"Rowan shook his head as the group almost instantly forgot about his presence and descended into what he assumed was their usual bickering. It had been some time since he had seen a honest, proper adventuring group."
"Not that they weren’t present in Rosaria. With the nobles more or less completely ignoring the countryside, it wasn’t uncommon for people to hire mercenaries to deal with their problems."
"Though Rowan couldn’t help but feel the group in front of him was considerably more… Lighthearted than he had expected them to be."
"A sign of times, perhaps. With Karnas defeated, hope returned to Rosaria."

show rowan necklace concerned at midleft with dissolve

"… For a time, at least."

hide rowan with dissolve

"Normally Rowan might have paid no attention to random adventurers like that, but judging by their location, it was safe to assume they were here for the same purpose as he was. If they already scouted they mine, it would make his job that much easier."
"Adopting a pleasant smile, he joined the group for supper. With the “innovative” dish ruined, the party offered him some of their usual dried rations, and with them – customary introductions."
"The sorceress’s name proved to be Sheera. She was a fire mage who used to study in Rastedel and dreamed of becoming a heroine, just like Deanara was."
"The burly man called himself Qais. He was a mercenary from the Empire of Sand, but after seeing the destruction caused by Karnas he chose to quit the life of a sellsword and devote himself to hunting down the monsters that now plagued the countrysides of all the nations Karnas invaded."
"The man in leather told Rowan his name was Bernard, and that was that. He didn’t seem like the talkative kind, which contrasted with his earlier, loud behavior. Guess he only ever opened to people he was close with?"
"The last adventurer was a scrawny boy who, contrary to Bernard, just didn’t seem like the kind to open up at all. Sheera said his name is Isaac, and that the group rescued him from orc slavers two years ago. Ever since, the four of them travel together."
"Frowning, Rowan asked why exactly did they think that dragging an adolescent boy around for monster hunting was a good idea. This was no life for a kid!"

$ bernName = "Bernard"
$ sheenaName = "Sheena"
$ qaisName = "Qais"
$ isaaName = "Isaac"

shee "It’s fine, it’s fine."
shee "Isaac is stronger than he looks. He’s blessed by Solansia, you know?"

bern "Sheera!!"

"Bernard hissed at his companion, but the sorceress waved him off."

shee "Oh come on, you want me to keep things away from the Hero of Karst? He’s the most trustworthy person we could ever possibly meet, bar Deanara herself!"

bern "This is NOT your secret to tell!"

"The sorceress pouted."

shee "Sheesh, whatever… "

"Rowan looked at the boy, who turned his eyes away. He chose not to pry on the subject… At least not yet. "
"After they all exchanged backstories, before Sheera could shower with various question regarding his  time spent with Deanara, Rowan asked them what were they doing in the area."
"As he expected, they also heard the rumors about the mine being occupied by monsters, so they came to clear it out. But they didn’t find anything except a lone drider – whatever used to haunt the tunnels must have left a long time ago."
"As for the mine itself, they still saw traces of ore here and there, but it was hard to say if it was abandoned because of monsters, or because it was no longer profitable. Regardless, it could be reopened, and Rowan did a mental note to inform the castle of that as soon as possible."
"With his main objective achieved and the day nearing its end, Rowan asked if the group would mind if he joined them for the evening. It was always safer in a group, and he wouldn’t mind having some company for a change."
"Isaac didn’t mind at all, and if Bernard had anything against it, he decided to keep it to himself. Now, Sheera and Qais…"
"Both of them were all too happy about Rowan’s company. The sorceress kept finding more and more excuses to rub her body against him, or to lean forward so he could look down her cleavage."
"Her robes were loose enough that Rowan could easily see her modest breasts whenever she did so, and it would be a lie to say he didn’t look at least once. The sorceress noticed, the corners of her cute mouth turning upwards into a devious smirk."

if avatar.corruption > 49:
    "Rowan found himself responding to their flirtations, wholeheartedly enjoying the feeling of being courted. After all the time spent in Castle Bloodween, it was nice to spend some time with someone who didn’t have an ulterior motive when attempting to fuck him."
    "There would be nothing wrong with fooling around a bit, would there?"

elif avatar.corruption <= 50 and all_actors['alexia'].relation < 30:
    "Rowan found himself responding to their flirtations. With Alexia giving him the cold shoulder, he couldn’t help but enjoy being courted."
    "Surely nobody would blame him if he let himself have a little bit of fun for a change, would they?"
else:
    "Despite himself, Rowan found himself responding to their flirtations. He felt a bit guilty about doing so – with Alexia waiting for him back in Castle Bloodmeen, it didn’t feel right to mess around with other people."
    "Though It would be a nice way to release some tension… "

menu:
    "Encourage Sheena.":
        $ released_fix_rollback()
        jump encourageSheena
        
    "Encourage Qais.":
        $ released_fix_rollback()
        jump encourageQais

    "Keep things platonic.":
        $ released_fix_rollback()
        jump adventurersPlatonic


label encourageSheena:

scene black with fade
show rowan necklace happy behind black

"Smiling, Rowan turned his attention to Sheera, happily indulging her many questions about his past adventures."
"Sheera’s enthusiasm and general sunny disposition proved to be infectious, and Rowan quickly forgot about the many struggles he was forced to endure in present days."
"He gladly spent the evening reminiscing about old times, when thing weren’t nearly as complicated, and he didn’t need to balance his soul and Alexia’s safety with every decision."
"At one point, when they thought he wasn’t looking, he saw the sorceress smile triumphantly at Qais, who raised his hands in defeat."
"When night came, he laid to bed with the others, agreeing to take the last watch. But he didn’t sleep. He waited patiently, and as expected, half an hour later, he heard someone approach him."
"He opened his eyes and smiled at Sheera, who stared in surprise, before returning the gesture, again offering him that cute, devious smile of hers."
"She helped him get up, and with a skip in her step started to drag him into the woods."

ro "Should we just leave them like that?"

"Rowan asked, casting a glance at the reminder of the party. The sorceress smirked in response."

shee "We literally just killed the only thing that could ambush us, and I have magical alarms all around the camp. How did you think I noticed you earlier?"

ro "Fair."

"Choosing their steps carefully – at least Rowan was, the concept of sneaking was foreign to the woman – they left the camp, and started walking deep into the forest."
"Deep enough for that the two of them could talk comfortably, without the fear that they might be overheard. Or that they would wake up the others."

shee "Mhm! Yes, this will be perfect!"

"The sorceresses declared suddenly, once they were a fair distance from the camp. Without allowing Rowan a chance to respond, she jumped him, using the momentum to press him against the nearby tree."
"Her lips sought his, while her hands started to undress them both. She wasn’t wasting any time, and Rowan felt she’d rather just tear the clothes off him, if given the option."

ro "No foreplay?"

shee "Fuck foreplay. I want to feel the Hero of Karst inside of me already!"

ro "(Oh, so that’s what this is…)"

scene cg675 with fade
show rowan necklace happy behind cg675
pause 3

"Rowan didn’t mind a casual encounter, but he had no intention of letting the lively sorceress treat him like a trophy fuck. Annoyed, he grabbed her by the wrists, and with one swift motion turned their positions around, pinning her to the tree, arms over her head."

ro "Young lady, I think you got the wrong idea about who’s claiming who here."

"Sheera giggled in response, not at all dissatisfied with the sudden turnaround. She tried to lean in to kiss him again, but Rowan kept her firmly in place. Her enthusiasm was quite flattering – but he had no intention of letting her dictate the tempo."
"Exploiting the physical advantage he had over her, he locked the sorceress wrists with one hand, and used the other to undo the front of her robe."
"Sheera’s accursed mounds, previously taunting him with occasional appearances through the entire evening, were finally revealed to him in full glory."
"They were petite, but perky, with small, erect nipples. Rowan pinched one of them teasingly, then grabbed the teat forcefully, making his partner gasp."

shee "If you like them, why not give them a kiss?"

"The sorceress smirked at him mischievously, again, not at all discouraged by her current position. She kept trying to free herself, but it was a token effort."
"Rowan’s arm trailed lower, and with deliberate slowness started undoing her belt, revealing her nether regions."
"As he expected, her lower lips were not unlike her upper ones. Just like the sorceress couldn’t shut up her mouth for 5 minutes, so was her slit partially open, already wet and ready."

shee "You won’t be needing to force these gates open, general Zerias!"

ro "..."

"Rowan stared at her through half-lidded eyes. Sheera giggled again."
"Rowan thrust two fingers inside of her, evoking a delightful gasp from the sorceress."

ro "You talk too much."
ro "I’d much rather hear you keep squealing like this."

scene cg676 with fade
show rowan necklace happy behind cg676
pause 3

"Sheera smiled impishly, but this time spared him the commentary. Satisfied the girl was starting to listen, Rowan began to lazily explore her insides, setting up a steady, slow tempo, as he kept driving his fingers further into her."
"Sheera tried to get him to speed up, gyrating her hips to his movements, but whenever she did so, Rowan simply stopped. She grumbled with frustration, but rather than keep struggling, surrendered herself to his caresses."
"Satisfied with the result of his ministrations, Rowan started to thrust his fingers with greater enthusiasm."
"He released Sheera’s arms, staring her in the eyes as he did so. She dropped them to her sides obediently, while he used his newly freed hand to reach out and grab her perky breasts again."

shee "Aa-aah!"

"She left herself at Rowan’s mercy, moaning sweetly. Her eyes, her green eyes, betrayed her excitement as she awaited his next move."
"Not being in any hurry, Rowan kept exploring her pussy for a longer moment, paying careful attention to her growing excitement."
"When he breathing grew even deeper, he decided she’s finally ready. He leaned in for a passionate kiss, which the sorceress eagerly returned, then whispered in her ear:"

ro "Turn around. Hands on the tree."

"Sheera obeyed without a moment of hesitation, giddy at the prospect of finally being fucked by the hero of her childhood. She eagerly presented her cute ass to him, swaying it to the sides enticingly."
"Rowan undid his pants and, again, without any haste whatsoever, started to rub his phallus against her overflowing opening. Sheera whined in response, much to Rowan’s delight."

shee "Please… Haven’t you toyed with me enough, Rowan?"

ro "Maybe."

"It was tempting to just keep on toying with the sorceress, but doing it anymore would be simply cruel. For all her faults, Sheera did choose to play along, and it was high time she was rewarded for her obedience."
"Though perhaps not in a way the sorceress expected."
"He pushed the tip in, into the welcoming, warm folds of Sheera pussy. The woman tensed in anticipation. Was this finally it? Was her sweet torture at an end?"
"But Rowan’s tool would retreat as unexpectedly as it thrust in. Sheera turned her head to the hero, letting Rowan get a good look at her confused, fearful expression."

scene cg200 with fade
show rowan necklace happy behind cg200
pause 3

"With a smile, Rowan spread her ass-cheeks and started to push the tip of his penis forward, but not into the same hole as before."

shee "Oooo-ooooo?"

"The sorceress gasped in surprise, and unexpectedly burst into giggles. She threw him a wild smile, then braced herself better, ready to accommodate him with her tight asshole."
"His cock, wet with her juices, worked its way steadily into her depths. Her insides squeezed around him, too tight for his size. But rather than force his way in with one brutal stroke, Rowan kept pushing in gently, allowing Sheera’s anus to stretch with minimal pain."

ro "Brave girl. "

"Finally, his balls touched her ass. Against all odds, she managed to take him all the way in. His hand trailed against her back possessively, as Sheera waited for him to start moving."
"And he did just that."
"Slowly, but mercilessly, he started to fuck her tight asshole, pushing against her twitching inner muscles. She wasn’t used to it, but what she lacked in experience, she   made up with enthusiasm and endurance."

ro "Ready for me to go faster?"

shee "Yes!"

"Smirking, Rowan pick up the tempo methodically pounding her tight ass. Sheera moaned something incoherently – she no longer had the strength to keep throwing cheeky responses as she loved to do."
"Her head hung low, as she focused her attention on keeping her sphincter nicely relaxed for him."
"Ever the gentleman, Rowan resisted the temptation to pick up the pace any further – the poor sorceress was already barely holding herself together."
"He grabbed her sides firmly, helping her keep her posture as he kept thrusting in – her tight insides constantly trying to keep his cock in place, and constantly giving way as kept pushing in and out of her."

shee "A-aah! Aaah!"

"Rowan’s grunts and Sheera’s half-pained, half-ecstatic moans were the only sounds filling the forest now – and it would stay that way for a while, as Rowan was in no hurry to finish the girl off."

"But despite that, there was an end to even his endurance. Her narrow ass was simply too good to resist for long, and Rowan felt himself approach his limit."
"He buried himself deep inside of her, and reached between her legs once more, his hand seeking her overflowing pussy. He pushed his fingers into her, their movement mirroring the pistoning of his cock -"

shee "Aah!!"

"- and finally pushing her over the edge."
"A moment later, he came as well, his hot cum pouring into her freely. Sheera trembled in joy, and Rowan had to grab her by the stomach so she wouldn’t fall."
"He remained like that for a moment, lazily exploring her breasts as the sorceresses rested  with her body against the tree trunk."
"Breathing heavily, she turned her head around, and familiar devious smile forming on her lips."

shee "So that’s why general Zerias lost."
shee "He kept trying to force the front gate, rather then push into the backdoor!"

"Sheera's delighted giggle filled the forest, only to be stopped when Rowan thrust into her ass once more, shutting her up again."

#Set flag = “Fucked Sheera”, “Isaac mage”
$ fucked_sheera = True
$ isaac_mage = True
jump adventurersConclusion

############################################################

label encourageQais:

"Rowan turned to face the big man, flashing him a wide smile. The man was handsome, bronze skin stretched over a taut, muscled body. He was comely, to be certain." 
"Rowan decided to innocently prod him on his backstory. Out of the corner of his eye, he saw Sheera pout angrily. Her sulking did no escape Qais either, as the large man let out a low chuckle in his deep voice before answering him."

qais "There isn’t much to tell. My father owned a small farm in the southern regions. I worked there for most of my youth. "

"He cracked his neck and flexed his impressive shoulder muscles. Rowan noted the girth of them."
 
qais "It’s thanks to him that I’m as strong as an ox. "

shee "And almost as dumb as one, too."

"Qais snickered, making a rude gesture in the direction of the sorceress, who smirked and turned to talk to her other companions. She seemed resigned to Rowan’s choice of partner."

qais "The old man sired four of us, brothers all. He used to call us his little soldiers... till we all ended up a full head or so taller than him.  "

"His voice took a melancholic tone. Rowan saw Sheera roll her eyes in the background."

qais "Back then... I thought my might made me special. I was the youngest you see, and by the time I reached adolescence, my father was old and decrepit. I didn’t want to listen to his wisdom-"

shee "Oh Goddess, I can’t listen to this again! Ladies and gentlemen: the master of the mood-slayer! It’s like  the knight from Uverth all over again!"

"The gentle giant spread his hands defensively to try to calm the sorceress down."

qais "Sheera, that knight needed a night of comfort, not passion. A man like that… let’s just say tears dont make for good pillow talk."

bern "Is that why you make this story so fucking depressing every time you tell it?"

qais "Maybe I’m just hoping one day it will give life to your ironclad heart? Maybe even let me sneak my way into it?"

bern "Oh, fuck off."

qais "Hmm, I guess there’s still room for improvement."

"He winked at Rowan, and the hero shook his head with a smile. It was refreshing to see a man who wasn’t just looking for an easy lay." 
"…Though that did make Rowan somewhat self-conscious. An easy lay was exactly what he was looking for."

scene black with fade
show rowan necklace happy behind black

"The lighthearted, cozy atmosphere continued on through the evening, with the bratty sorceress doing her best to get under Qais’s skin, and the unflappable giant taking it all in stride." 
"It was almost a shame to see the sun go down. Stifling yawns, the rest of the group headed to their bedrolls." 
"Leaving Rowan and Qais alone to take the first watch."

shee "… If you two wake me up before daybreak, I’m flinging fireballs."

"Rowan shared a smile with Qais, but said nothing.  The burly man’s dark eyes gleamed with mirth in the firelight. There was no hurry, and the quiet conversation was pleasant."
"Almost an hour passed, the night deepening to a comforting stillness. After a while, Qais stood up from the campfire and stretched. Rowan liked the sight of his tanned muscles flexing, the casual strength of his thick biceps." 
"Without a word, Qais headed for the woods. He shot Rowan a glance and a smile over his shoulder, indicating with his eyes for him to follow."
"Rowan tramped a short ways behind Qais through the woods, fascinated by the calm, assertive way he moved. He was a bulky fellow, but he carried himself with the ease of a far more limber man." 
"Qais stopped only a short distance away from the camp. Rowan looked back - the tents were still within eyeshot. Qais chuckled at his unspoken concern."

qais "We’re on guard duty, it would be irresponsible to leave them {i}completely{/i} unprotected."

ro "And on the off-chance someone hears us…?"

qais "Isaac sleeps like a log, and Bernard - despite his attitude - understands all too well how necessary stress release can be."

"The big man shrugged, flashing Rowan a sultry smile."

qais "Besides, Sheera is going to be insufferable whether we wake her or not. So we might as well give her ample reason to be."

ro "And here I thought you were the ‘matron’ of the team."

"Rowan felt a thrill run down his spine at the smirk Qais gave in response to the little jab."

qais "I am. But even a matron needs to let her kids run free and focus on herself, for once."

"Qais quirked an eyebrow, looking Rowan up and down before unbuckling his sword belt. Rowan noticed for the first time how large his hands were."

qais "-And just so we’re clear:  you’re gonna pay for that last comment."

"Rowan’s heart pumped a little faster as he hurriedly undid his own sword belt."

ro "Don’t threaten me with a good time unless you intend to follow through on that threat."

"Qais chuckled, his deep voice rolling off into a masculine purr. Rowan watched, mesmerized as he removed his shirt, exposing his rippling chest. He was hairy, with fine black curls coating his tawny skin in a patch of thick fuzz."
"Here, was a man."
"As Qais removed his trousers, he let out a low grunt, nodding at Rowan’s still-clothed body. Rowan peeled off his shirt, exposing his pale chest. Qais’ eyes drifted across his body with the appraisal of a man who knew the value of things."

qais "There’s something I wanted to ask you. Everybody knows of your skill in commanding men."
qais "But was there ever a man you wished to serve {i}under{/i}?"

"Rowan  narrowed his eyes at the large man, doing his best to hold back a smile as he unbuttoned his pants. Qais expression was that of pure innocence, as if his words were not dripping with innuendo."

ro "Perhaps there was. "

qais "They must have been quite remarkable, to attract your attention. "

ro "Would you rather be {i}with{/i} them?"

qais "No. I’d rather {i}be{/i} them."

"And just like that he was in the man’s arms. Rowan let out a heavy breath, settling into Qais’ embrace as the two locked lips. His thick beard tickled his chin, his cock stiffening as he drew close to the imposing warrior."
"Qais’ large hands settled on Rowan’s shoulders, rubbing his back in soft circles. Despite his formidable frame, the man was quite the gentle giant. Rowan let out a groan of pleasure, kneading Qais’ biceps in wonder at their thickness."
"His scent was heavy, masculine and potent. A lingering sheen of sweat made his swarthy skin glisten in the night air. Rowan breathed it in with a pleasured sigh."
"There was little time for foreplay. Despite their mutual attraction, both men were still professionals. An absent night watchman spelled doom for a sleeping camp. They would have to be quick about this."
"Fortunately for Rowan, Qais knew what he wanted. His thick hands drifted down to cup Rowan’s butt, kneading the cheeks as he pulled him close. Rowan could feel Qais’ large erection poking him in the stomach."

qais "Supple."

scene cg565 with fade
pause 3

"Qais said the word as if that was all there was to say on the matter. Rowan almost let out a bawdy joke, but instead groaned as he felt Qais’ large finger sink into his ass."

qais "Turn around, Hero."

"His voice was deep, but his tone was soft. Rowan, blushing, turned around. Qais sat back against a nearby tree trunk, spreading Rowan’s cheeks as he examined his nethers."
"Rowan stood half bent over with his hands to his thighs, bearing the embarrassing position as best as he could."
"Thick fingers trailed across Rowan’s growing erection before moving once more to his ass."
"He stuck his index finger in his rump again, letting out a huff of appreciation when he managed to push to the second joint before encountering stiffer resistance."

"Qais pulled his index finger free, only to replace it with the one on his other hand. Rowan groaned as he felt the finger press deep inside, wigging back and forth to test the proverbial waters."

qais "Relax, Rowan. Breathe..."

"Qais’ warm breath at his neck made Rowan shudder with anticipation. He did as he asked, taking in slower, deeper breaths as he relaxed his contracting muscles. Qais pulled free from Rowans ass, planting his hands on the hero’s hips."

qais "Easy now, slow and steady. Lean back into me."

scene cg566 with fade
pause 3
show rowan necklace naked aroused behind cg566

"Rowan leaned back, falling into Qais’ lap as the heat of his skin suffused him. Rowan felt the weight of the man beneath him, his back rubbing up against Qais’ hairy chest." 
"He positioned himself as best he could, spreading his legs to either side of Qais’ as the burly man angled his thick erection towards his ass. Rowan’s knees trembled, his face scrunching in both embarrassment and excitement."
"He shuddered as he felt the head of Qais’ dick press against his anus. His large hands pulled Rowan downwards, drawing him inexorably deeper onto a proper mounting of the adventurer’s cock."
"It came as a shock when their genitals made physical contact. An electric thrill ran up Rowan’s spine, pain and pleasure mixed together as he sank down onto Qais’ dick."

qais "Relax…"

"His big hands were at Rowan’s shoulders now, kneading them softly to accentuate his point. Rowan took in a deep breath and relaxed, feeling his whole body follow suit." 
"Qais’ cock slowly entered him, inch by inch, sinking deep into his ass. Rowan felt his own erection harden still further as the girthy length entered him, blood flowing like a river to his extremities."
"He got nearly halfway down the shaft before Rowan had to pause. He was panting, his stomach clenching tight from the sensation of the intruder in his insides."
"It was a deep, filling sensation. Qais’ cock throbbed inside of him, like a second heartbeat radiating erotic heat into his body."
"Qais’ hands lifted him, guiding Rowan upwards. They paused at the apex of the thrust, with just the tip of his cock still inside of him."

qais "Ready?"

ro "Yeah..."

"The big man’s hands pulled down on him again, sliding deep into his rectum. Rowan grunted, feeling every inch entering him as Qais’ member throbbed with each stroke."
"The thrusts were slow at first, building in momentum as they continued onward."
"Soon the hot, wet {i}slaps{/i} of human copulation filled the night air. Rowan moaned, reaching down to jerk himself off as Qais took control, bucking his hips upwards in tune with Rowan’s downstrokes."

ro "{i}Aaah!{/i}"

"Rowan’s hand leapt from his precum-slick dick to cover his mouth in embarrassment."
"Qais had poked his prostate so hard and so suddenly that he had nearly cum then and there. The large man chuckled, his hot breath tickling the back of Rowans neck."

qais "Careful, hero. Wouldn’t want our fun to end so soon, would you?"

"Qais leaned his head forward and kissed the back of Rowan’s shoulder, the tanned adonis’ thick beard tickling his skin with its raspy texture. Rowan moaned, reveling in Qais’ masculine body, the way he held him tight and wouldn’t let go."
"He was beautiful, this untamed stallion that Rowan was riding."
"Having found Rowan’s g-spot, Qais made a point to time his thrusts to caress it each time he reached the downswing. It was maddening, like he was trying to test the limits of Rowan’s resistance."
"Rowan moaned, leaning back to plant his hand on Qais’ tanned shoulder for support as the thrusts went ever deeper. He continued to jerk himself furiously with the other hand, an orgasm rising like a crashing wave."
"Qais let out a deep growl at the base of his throat. While he’d been a gentle lover at first, now he had revved up to full speed. His breathing deepened, manly exhales of exertion that Rowan replied in desperate kind."
"The thrusts came shorter and deeper now. More than once Rowan felt his hips connect with Qais’ own, their balls touching together as Rowan settled onto his man-made love seat. The pain was gone, replaced only by a growing need to cum."
"Qais’ cock twitched once, twice, three times, then unloaded. Rowan heard his breathing quicken into shallow breaths, then a final, loud exhale."

qais "{i}Aaahn{/i}, R-rowan!"

"Rowan jerked himself like a horny , his body clenching in pleasure as he created a vice-like grip on Qais’ fat cock. He gasped, feeling it thicken and bulge inside of him as Qais’ testicles clenched beneath him."

ro "Come on! Let it out!"

"Qais did as he was told. His large hands dragged Rowan down into his lap and held him there, his breath expelling in great gouts as he came. Rowan felt a sudden warmth blossom inside him, spurts of cum firing off into his deepest places as he felt himself."
"Rowan took his own advice, letting out a cry of pleasure as his cock spurted a jet of ivory liquid high into the air, he clenched and held in place, feeling the warmth blooming from inside his ass."
"The two stayed there for a long moment, reveling in the joy of post-orgasmic bliss. Qais tilted Rowans head around to look at him fondly for a moment, then planted a slow kiss on his lips."

qais "Just as good as I imagined."

"His quiet voice was comforting, but also filled with a certain… pride? As if Rowan had been the easy lay, rather than the other way around."

ro "Does that mean you’re ready for round two?"

"Qais let out a low laugh."

qais "I’ll be lucky to feel my legs in the morning, at this point."

$ rowanGaySex += 1
$ isaac_mage = True
jump adventurersConclusion

###########################################################
label adventurersPlatonic:

#If Alexia influence is 50 or higher.
if all_actors['alexia'].relation > 50:
     "Rowan turned down both of them, kindly noting that he was, in fact, a married man."
else:
    "Rowan turned down both of them, preferring not to sleep with every random stranger he met on his travels."

#rejoin.
"Instead, he paid more attention to the other half of the party, hoping to get them to open up."
"With no success. Bernard said he had no intention of sharing his life story with every stranger on the road, hero or not-"

shee "He’s a reformed criminal who killed his bandit chief when he learned he was engaged in child slavery!"

bern "Dammit woman!"

"… While Isaac still didn’t want to open up. The kid kept staring at him though, like there was something he wanted to say after all, but couldn’t bring himself to do it."
"Every attempt and finding some common ground with the boy proved unsuccessful. As night came, Rowan headed to bed defeated, informing the others he would take the last watch.
Isaac took the one before him."
"…"
"The boy woke him up at the agreed hour. With a polite “Thanks kid”, the hero headed to the front of the camp."
"Isaac stood motionless for a moment, then followed suit."

show rowan necklace happy at midleft with dissolve

ro "Something bothering you, Isaac?"

isaa "…"

show rowan necklace concerned at midleft with dissolve

isaa "There is darkness in you. I feel it."

"Isaac kicked the ground, eyes down."

if avatar.corruption > 69:
    isaa "It’s… Suffocating. It envelops you. Surrounds you. Taints everything you touch."

elif avatar.corruption < 69 and avatar.corruption > 30:
    isaa "It’s like a… Stain. Living… Expanding. Tainting you."

else:
    isaa "It’s… Subtle. But it’s there."

isaa "But you don’t seem bad… So I didn’t want to say anything with the others listening."
isaa "Are you…"
isaa "Are you okay, Mister Blackwell?"

show rowan necklace shock at midleft with dissolve

ro "What?"

isaa "Well… Everyone kept saying what a great hero you were, so… Something bad must have happened to you… Against your will… I think?"

show rowan necklace neutral at midleft with dissolve

"Goodness gracious…  It was heartwarming to see the kid show such concern for someone who in his eyes had to be tainted."
"Naive as well. Heartwarming, but naive."

ro "You could say so."

"Still..."

if avatar.corruption > 69:
    "“Tainting everything he touched”?  That sounded pretty ominous."
    "He knew, the moment he agreed to serve the twins, that he wouldn’t be able to keep himself pure. But was the situation this bad already?"

else:
    "He wasn’t surprised his aura wasn’t entirely pure. He knew this would happen the moment he agreed to serve the twins."

ro "I was forced to make some… Difficult choices."
ro "It’s a long story."

isaa "… I see."

"The kid wasn’t one to push an uncomfortable subject, and for that, Rowan was grateful."
"Though the fact he was capable of seeing the twin’s influence on him was… Worrying. It shouldn’t be possible for most faithful – the kid obviously had strong affinity for divine magic."

show rowan necklace concerned at midleft with dissolve

ro "Do you… See such things often?"

"Isaac kicked the ground again. He still refused to meet his eyes."

isaa "Sometimes."
isaa "An abbey we passed a while ago felt… Wrong."
isaa "The others wanted to investigate it, but I begged them not to."

"His voice dropped to a whisper."

isaa "I don’t think we’d survive if we did."
isaa "Then there was this big woman in Rastedel… "
isaa "I… Think she felt I felt something, because when we crossed gazes, she smiled this sweet, friendly smile, and started walking in my direction. "
isaa "But then I think she saw Qais and Bernard, and I quickly lost her in the crowd."

#if past week 49
if week > 49:
    isaa "And recently, the entire region just feels… Wrong."
    isaa "I don’t think we’ll stay here."
else:
    pass

"Rowan studied the boy closely. He was no expert on the matter of magic, but he could see a hero in the making when he saw one."

ro "You have a rare gift. Why haven’t you joined the church?"
ro "They would welcome you with open arms in Prothea."

isaa "… It wasn’t Prothea that saved me. And It wasn’t Solansia that protected me."
isaa "Or my family."

"His voice was now that of an angry whisper. He turned his head to the sleeping adventurers."

isaa "I owe everything to them. I won’t abandon them."
isaa "Not even for a Goddess."

menu:
    "Tell him he could serve Solansia and still help his friends.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "You don’t have to. You can embrace your gift without turning your back on them."
        ro "Didn’t Deanara herself lead a ragtag bunch of heroes despite being Solansia’s chosen?"
        "Isaac smiled gently, but didn’t seem fully convinced."
        isaa "I guess she did."
        ro "We all have our part to play in all of this, Isaac. We might not always like the roles that have been given to us… But Solansia picks her chosen for a reason."
        ro "Sometimes to save people she herself couldn’t reach."
        ro "You can do much good in the world, but you’ll have to put your faith in the Goddess."
        "Isaac finally met his eyes, hesitating with his response. Coming from someone else, Rowan’s word would ring hollow."
        "But hearing them from the Hero who helped slay Karnas… It gave them weight."
        isaa "… I’ll think about it."
        "Rowan nodded solemnly-"
        "- then, he ruffled his hair affectionately."
        isaa "H-hey! Stop it!"
        "He couldn’t help himself. Precious kid. Goddess knew he needed it."
        #set flag = “Isaac Cleric”. Gain small favour with Solansia.
        $ isaac_cleric = True
        #$ change_favor('solansia', 2)

    "Tell him he should follow his own path.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        ro "I understand."
        ro "… When we slayed Karnas, many years ago, not everyone had their fill of blood yet."
        ro "Some people had enough of the noble rule. They thought it was time for a change."
        show rowan necklace concerned at midleft with dissolve
        ro "They came to me, and asked me to lead them into battle. To tear down the society they thought unjust."
        show rowan necklace neutral at midleft with dissolve
        ro "I refused. All of them. I didn’t… I didn’t want to spend all my life fighting. I had someone waiting for me back home. I wanted a different life for us both."
        isaa "… I take it that didn’t work out, then?"
        "Rowan laughed bitterly."
        ro "Oh, it did… For a while."
        ro "But I guess destiny doesn’t look kindly on people who refuse its call."
        ro "And I never regretted my choice, present complications notwithstanding."
        ro "The point is, kid – never let anyone rope you into a war that isn’t yours. Always fight for what you believe in."
        if serveChoice == 2:
            "His own words sounded hollow to him. Never fight a war you don’t believe in? He joined the twin’s out fear, not conviction."
            "And now he paid the price fort that. Every day. Some role model he was."
            "… But that wasn’t what the boy needed to hear right now."
        else:
            pass
        ro "You can be who you want to be.  Don’t let anyone convince you otherwise, Solansia blessing or not."
        "Isaac nodded solemnly, a determined expression on his face."
        isaa "I will. I promise."
        "He would grow up to be someone noteworthy, of that, Rowan was certain."
        #Set flag = “Isaac mage”, slightly increase favor with Kharos.
        $ isaac_mage = True
        $ change_favor('kharos', 2)

        show rowan necklace happy at midleft with dissolve

ro " Alright, that’s enough philosophical discussions for today."

isaa "… The sun has yet to come up. "

ro "Yes."

show rowan necklace neutral at midleft with dissolve

ro "Yes, the sun has yet to come up."

show rowan necklace happy at midleft with dissolve

ro "Get some rest. Even if only for an hour."
"The boy nodded, and left Rowan alone for the reminder of the night."

label adventurersConclusion:

scene bg55 with fade

"Morning came, and the adventuring party gathered for breakfast, with Rowan joining them."
"They inquired if he would also join them in their travels, at least for a while. The group was heading west, planning to walk the southern bank of river Yael till they reach the coast, and then turn north, into forest Ealoaen."
"The prospect of some honest company wasn’t an unpleasant one, but Ealoaen wasn’t his target at the moment, and even if it was, he couldn’t allow himself to be limited by people who didn’t know the nature of his present quest."
"So instead, they exchanged some information on the surrounding area."
"Among the general advice, they also told him there were rumors of a massive orc camp between the river and the mountains to the north, west of Rastadel. That’s why the wanted to stick to the southern bank, to avoid any possible orc raiding parties."

show rowan necklace neutral at midleft with dissolve

#if rowan has visited the orciad camp
if orciad_state > 0:
    ro "(That would be Ulcro’s/Batri’s/Tarish’s camp. Wise choice on their part.)"
else:
    ro "(Hmm. Might be worth checking out.)"

#rejoin
"With that, their business was concluded, and it was time say their goodbyes."

qais " It was an honour meeting you, Rowan."

show rowan necklace happy at midleft with dissolve

ro "The honor is all mine. I still can’t believe I ran into an actual adventuring party!"

shee "Ha, how is that surprising? Do you know how many orc camps they have in Rosaria? Dozens!"

#if Rowan has claimed at visited 3 orc camps
#bern "But they haven’t been very active recently… "
#bern "Something must be going on."
#qais "Perhaps. But I fear that this time we’ll have to leave that to the nobles."
#"Bernard spit to the side, obviously not convinced they would be of any use."
#"And being very right in that regard."
#else
#pass

ro "Regardless, let’s just say it was a nice change of pace."
ro "I wish you all good luck."

shee "Aye aye! Tell Deanara to ask about Sheera of Arkeny, if she’ll be visiting the elf lands next year by any chance!"

bern "Yeah, take care."

isaa " … Stay safe, Mister Blackwell."

"They lingered for a moment, delaying the goodbye, until Qais nudged Isaac gently, and the four finally started moving. Rowan stayed behind, having told them he needed to take one last look at the mine – and already contacting Castle Bloodmeen to have them send people in."
"If he ever finds himself in Ealoaen, he should keep an eye out for these guys."

#Show usual mine menu.
# Gain normal mine rewards. Reduce corruption a little. Reveal all hexes within a radius on 3, but keep them unexplored/ grayed out.
# roll 1d10.
# on 10, add “Drider omelette recipe” to the inventory.
#Drider omelette recipe
#Icon: A piece of paper.
#Value: 0
#Description: “The fabled omelette recipe. Someone must have put it in your backpack by mistake. Due to wet stains on the paper, likely from being left in the open during a passing rain, the writing has been rendered completely Illegible.”
$ change_base_stat('c', -2)
$ temp2 = mines_defs[eventHex[6]][1]
$ temp3 = mines_defs[eventHex[6]][2]
$ temp4 = temp2 * miner_cost
menu:
    # Choice 1: Hire workers
    # costs some gold.
    "Hire workers ([temp4] gold)" if castle.treasury >= temp4:
        $ released_fix_rollback()
        $ change_treasury(-temp4)
        $ castle.mines += 1
        $ castle.iron_per_week += temp3
    # Choice 2: Deploy Soldiers
    # costs some soldiers, but also some morale.
    # TODO count soldiers able working at mine (different barracks)
    "Deploy Soldiers ([temp2] soldiers)" if castle.buildings['barracks'].troops >= temp2:
        $ released_fix_rollback()
        $ castle.buildings['barracks'].troops -= temp2
        $ castle.morale -= temp2
        $ castle.mines += 1
        $ castle.iron_per_week += temp3
    #Choice 3: Leave
    #does nothing, but leaves the mine unexplored so that the player can come back later.
    "Leave":
        $ released_fix_rollback()
        $ prevent_tile_exploration()
return

#################################################################################################################
#################################################################################################################
#################################################################################################################

label deep_in_her_mines:

scene bg55 with fade

"Rowan cut through the bramble overtaking an old dirt path and thorny branches fell to the wayside. As the sun dipped low beneath the trees and a crash of thunder sounded nearby, he knew his options for places to rest had become limited."
"A large abandoned mine loomed through the darkness. It was not an ideal choice, considering how dangerous it could be to explore at night, but the oncoming storm left him little choice."
"Rowan ducked into the constructed cavern and lit a torch, its soft glow barely illuminating the space. He raised his torch up to get a better look, but the mine stretched onwards, the tracks of old mine carts disappearing into pitch blackness."
"He followed the tracks into the mine, each step echoing throughout the cave. It felt as if the mine stretched on for miles. How far did this thing go?"
"As he took another step forward, the earth shifted underneath his foot, and Rowan found himself falling into the darkness."

show rowan necklace shock at center with dissolve

ro "Wha--Ahhhh!"

hide rowan with dissolve

"He plummeted through the darkness, panic surging through his body as he wondered how deep this hole might be and if this mine may be the last place he is ever seen, before he landed on the hard, stiff ground."

scene cave1 with fade

show rowan necklace concerned behind cave1 

"There was a brief flash of light as his torch tumbled after him, the light distinguishing as it fell against the floor."
"It took a few minutes for his eyes to adjust. Rowan sat up cautiously, wincing as his backside throbbed in pain. He felt around the walls of the mine, searching for a ladder or some device that could pull him back up."
"Nothing."

ro "Shit."

"This wasn't good. There was only so much food and water in his pack to last him a few days, but who knew how long he would be trapped in his cave? He might just have to message back to the twins and hope they could send rescue. "

quest "What are you doing here?"

"Rowan spun at the sound of a feminine voice behind him, unsheathing his sword at his side. He could barely make out her figure in the darkness, but he could hear her footsteps shuffling against the dirt, stopping just in front of him."

show rowan necklace neutral behind cave1 

ro "I thought this mine was abandoned?"

quest "Well it clearly isn't. I ask that you leave at once and do not bother me or my home again."

"Home? Rowan looked around the pitch black cave skeptically."

menu:
    "Ask for help.":
        $ released_fix_rollback()
        ro "...Right. That's sort of impossible considering I can barely see my hand in front of my face."
        ro "Would you mind helping me get out of here?"
        "The woman cocked her head to the side, her figure becoming more visible as Rowan's eyes continued to adjust to the darkness. She has a curvaceous figure with a high slit dress that swished as she circles him."
        quest "You would ask for {i}my{/i} help? {i}You're{/i} the one that invaded my home… "
        "She stopped in front of him, and although he had trouble seeing her, Rowan could feel her gaze trailing up and down his body."
        quest "But I suppose you could {i}convince{/i} me to help you. What do you say?"
        "Rowan tensed up as she ran a hand down his chest. Suffice to say, there was little ambiguity in the form of persuasion she desired."
        menu:
            "If I have to…":
                $ released_fix_rollback()
                jump velrysSex
                
            "Just tell me how to get out of here.":
                $ released_fix_rollback()
                "The woman scoffed and put some distance between them."
                quest "A lot of fun you are. Fine; I want you out of here as soon as possible, so better for me."
                ro "And who are you, exactly?"
                vel "You can call me Velrys."
                jump velExit
                
    "Find your own way out.":
        $ released_fix_rollback()
        ro "Right… I'll be on my way then."
        "Rowan nodded to himself, feeling around the tunnel for any sort of light source. He found one by accidentally bumping his head on a hanging lantern, hissing between his teeth in pain."
        "Pulling a match from his pack, Rowan lit the lantern and held it up high. The hole he fell from was steep, but not too large. Still, it was a wonder he managed to survive that without any broken bones."
        "There had to be another way out of here. As he looked around the pit he'd fallen in, there were various tunnels leading in different directions."
        "But if he wanted any hope of making it out of here tonight, he had to choose one now."
        "Keeping the lantern in front of him, Rowan looked down one of the tunnels and walked."
        #survival check - TO DO
        #pass
        "…"
        "…….."
        "……….."
        "After a few minutes of walking through endless tunnels, Rowan doubted the way he chose and started to suspect that he was walking in circles."
        "That is, until he heard the hoot of an owl nearby. Rowan followed the sound, managing through the winding tunnels until he was spit back out of a separate entrance to the mine."
        scene bg55 with fade
        show rowan necklace neutral at midleft with dissolve
        "He gulped in the fresh night air, pleased to find that the rain had stopped."
        quest "Impressive. I didn't think you would make it out of there until dawn at least."
        "Rowan spun and reached for his sword, surprised to find the woman standing at the entrance to the mines. Now with the moonlight shining down, he could see that she was a modest half-elf."
        ro "With no thanks to you. Were you waiting here to gloat if I failed?"
        quest "No. I was simply curious to see if you would make it tonight, and you did. Bravo."
        ro "Who are you?"
        quest "If I tell you, does that mean you will go away?"
        ro "Perhaps."
        vel "My name is Velrys. Are you satisfied?"
        ro "Not quite. I don't know how else to tell you this, but I need to take this mine here. I'll be putting it to good use, if that's of any consolation."
        vel "Absolutely not! This is my home! What right do you have to come take it?!"
        ro "You aren't using it--"
        vel "The hell I'm not!!"
        "Rowan sighed and rubbed the bridge of his nose. He needed to get through to her somehow if he wanted to avoid this thing ending in bloodshed."
        ro "Why are you here?"
        "Velrys looked hesitant to answer. She glanced away, crossing her arms indignantly over her chest."
        vel "I had to leave, okay? I'm not fit to be a whore. I refuse to be a whore. This is my only choice."
        "Her words took on an edge, and Rowan got a pretty clear idea of what kind of life she led. Even so, he still needed the mine, and if she continued to stand in the way of that, the twins would not be so merciful."
        ro "What were you before that?"
        vel "A blacksmith."
        "A blacksmith? He could use that."
        ro "Perhaps we can make a deal then. You could work under my protection as the mine’s manager? You can stay here as long as you want, so long as you continue to take care of the mine for me and my workers."
        ro "What do you say?"
        #persuasion check - TO DO
        #pass
        "Velrys eyed him skeptically, but she did not seem opposed to the idea. Rather, she almost looked excited at the prospect."
        vel "...Would it be slave work? Do I get paid?"
        ro "No, you'll get paid. By the time you’re done you will be quite wealthy."
        "She considered the offer carefully, searching for any kind of loopholes or lies in Rowan's statement."
        vel "...Fine. As long as I get to stay here and I get paid for it, I can do that."
        vel "But if I find out that this is some scheme of yours, I'm coming for your head, you got that?"
        "She held a threatening finger out to him, as though she was half-tempted to decapitate him here and now. Rowan held his hands up in defense."
        ro "I understand. It's no scheme, I promise. The mine is yours, we just want to work it."
        "Velrys straightened herself and nodded."
        vel "Good. Then send me the workers and we shall start."
        vel "Until then."
        "She gave him a small wave before walking back into the mines, her figure disappearing in the darkness. Rowan watched her go, amazed that she knew the mines well enough to figure it out in the dark."
        "At least the twins will be pleased. With not only a mine but a mine manager, this is going better than he could have imagined."
        #production bonus - TO DO
        return
                
        #persuasion fail - TO DO
            #val "Pay or not, you're coming to invade my home. You're no better than a slaver."
            # "She spat at Rowan's feet."
            # val "I hope you get eaten in the woods, boy."
            #"With that, Velrys stormed back inside of the mines. Rowan watched her go, running his hand up and down his wrist."
            #"There would be no point trying to follow her. Even if he could find her, there was no way to convince her. With a sigh, Rowan left. He could only hope Andras wouldn't be the one to handle her."
            #return
                
        #survival fail - TO DO
            #"Rowan felt that he had been walking for ages. Perhaps he had. Surely it would be dawn when he reached the end of the tunnel, right?" 
            #"But as he made yet another turn, the familiar sight of the pit came into view. He did a double take, glancing back down the tunnel he left, the tunnel he came from, and the hole he originally fell down."
            #ro "(I just walked in a big circle!! Damn it!!)"
            #"Rowan kicked the rock wall in frustration, wincing a little as pain reverberated through his toes."
            #"He was exhausted. There was no doubt he had been walking for hours and, if he wanted to have any energy to keep moving tomorrow, he needed to rest."
            #"With no shortage of defeat, Rowan set up camp in the pit."
            #"..."
            #"......"
            #"………"
            #"Morning came at last and Rowan could just make out the blinding peeks of sunlight filtering down one of the tunnels he had failed to explore."
            #scene bg55 with fade
            #"He followed the sunrays and came out along another entrance to the mines."
            #"There was no sign of the woman from last night, or even a trace that she had existed. For all he knew, she could be trapped in the mines herself and had lied about knowing a way out."
            #"Oh well. At least Rowan could continue his journey now, although he lost a day to the mines."
            #lose MP - TO DO
            #return


label velrysSex:

"It's not as if he had another  chance of getting out on his own in the middle of the night. If this is what she required for him to avoid getting trapped in this mine, Rowan he would just have to pay the price."

ro "Alright. If that's what it--"

"Rowan was cut off as he suddenly was pushed down to his knees, two strong hands grasping his shoulders. He didn't expect her to be this strong."

"She leaned in close, her nails lightly caressing his throat."

vel "Perfect. You can call me Velrys… But I might prefer hearing you call me “My Lady” instead."

"She waited expectantly for his response."

ro "...Yes, My Lady."

vel "Good. Now strip."

"Rowan did as told, removing his various belts and fabrics until he was bare before her. He heard her continue to circle him, her nails occasionally caressing his scalp and shoulders."

vel "You'll do anything to get out of this mine, won't you? Any little thing I want?"

"She sounded delighted by the fact. He heard fabric shift, followed by the collapse of her dress onto the ground."

ro "Yes, My Lady."

"The mystery of it came with a certain...thrill. He had no idea what this woman really looked like or who she was: he just knew that she wanted him to obey."
"Something hard--a shoe?--pressed against his forehead and shoved him down. Rowan gasped as he landed hard on his back."
"His cock hardened as he felt Velrys crawl over him, her leg coming to rest against his erection."

vel "What's this? Are you already getting excited? You can't even see me, you pervert. "

"Her leg rubbed against his growing erection, each movement sending an eager twitch through his cock. Rowan bucked against her, unable to help himself from the pleasure."

show rowan necklace naked aroused behind cave1 

ro "A-Aaahh…"

"Velrys dug her knee into his hip, forcing him back down."

vel "Did I say you could do that?"

"Her words contained enough authority that he decided to back down. Seemingly satisfied, Velrys lightly stroked her nails over his stomach to his chest."
"She found his nipples and pinched tight."
"Rowan released a muffled whimper between closed lips, his body arching toward her touch as she continued to fondle him."

vel "Do you enjoy that, you little pervert? For all you know, I could be a disgusting creature born out of the iron mines, and you're getting off on it."

"But she did not feel like a disgusting creature, and every supple touch only fueled his desire further."
"Velrys dipped her mouth low, her breath hot against his skin as he took one of his nipples into her mouth. Rowan tilted his head back, unable to resist whimpering in delight as she toyed with his body."
"After a few minutes of assault on his chest, Velrys climbed further over him and Rowan's nostrils filled with the scent of her musk as she hovered her wet pussy above his face."

vel "Please me, boy. "

"She lowered herself on top of him, smothering him with her sodden cunt. Despite taunting him for his own perversions, Velrys was soaked with arousal, her fluids dripping against his chin."
"Rowan tilted his mouth up and licked her slit, his tongue lightly lapping up her excess fluids."
"Velrys let out a sigh."

vel "Surely you can do better than that."

"She gripped the back of his head and shoved herself as far down on him as she could go, crushing Rowan's face between her thighs. He tried to breathe, but all he could take in was the strong scent of her pussy."
"Dizzied but excited, Rowan pressed his tongue into her folds, emitting a content sigh from the mysterious woman. Velrys ground herself against his face, urging him deeper."
"Rowan complied, his tongue picking up the pace as she rode his face. Her fluids flowed easily into his mouth and down his throat, each salty drip coating his tongue and encouraging him forward."
"Velrys moaned as she bucked her hips over him, reaching a frenzied state with her orgasm. She continued to ride him past her first one, second one, and well into her third, suffocating Rowan under the thick drench of her pussy."
"He gasped when she finally pulled away, her fluids covering the lower half of his face."

vel "That was… quite delightful. Wouldn't you say so?"

ro "Yes, My Lady."

"Repositioning herself over him, Velrys slid down to Rowan's thighs and gripped his erection in her rough palm."

ro "Aahh..."

"He involuntarily bucked in response, the sudden grip of her hand sending an exciting jolt through his body."

vel "So pathetic… I'm barely even touching you and you can hardly stand it."

"She stroked his length up and down in a swift motion, her fingers rubbing eagerly over the tip. The woman leaned down to drip some of her spit onto his shaft for lubrication, her wrist flicking up and down with more ease."
"Rowan jerked his hips toward her with each motion, precum dripping down his erection as he neared his climax." 
"Velrys noticed the movement and stopped stroking him at once."

vel "Not yet."

"Rowan gritted his teeth in frustration, just barely able to resist spilling his load over her. Once she saw he wouldn't cum, Velrys slowly began to stroke him again, once more building up momentum."
"But just before he could cum, she stopped."

ro "Please… Please, I need to cum…"

"Velrys laughed and moved her hand up and down once again."

vel "Who said I would let you cum at all?"

"She picked up speed with her hand, flicking her wrist down his base and over his tip until Rowan was once again near his orgasm." 
"He tried to restrain himself, tormented with the thought that this woman just very well may keep him on the edge as long as she wanted."
"She continued this back and forth for a little while longer, pumping his erection until he was just on the verge of climax before stopping altogether."

vel " I don't usually allow men to cum on their first try with me, but tonight I'll be merciful. You can cum on ten. Ready? Nine… Eight…"

"Her hand once again picked up speed and Rowan bucked eagerly into her palm, desperate for her to reach the end."

vel "Seven… six… five…"
vel "Four… Three…"
vel "Two…"

"Rowan could feel himself on the edge, just a second away from releasing his seed."

vel "Two…"
vel "Twooo~"

"She dragged out the word, giggling a little to herself as his cock twitched impatiently in her hand. He wasn't sure how much longer he could hold off."

ro "P-Please! Please let me cum!"

vel "One."

"She barely had the word out before Rowan's load was spurting out, coating along the woman's belly and thighs before dripping down over himself." 
"Velrys climbed off of him and settled down on the ground, haphazardly pulling her dress back over her bodice."

vel "I suppose you want to know the way out now, hm?"

ro "Actually, I would like to hear a little more about who I just slept with, exactly."

"Velrys was quiet. For a moment, he wondered if she snuck off. Then he heard a match strike."

label velExit:
    
"A hanging lantern on the wall suddenly flickered on, revealing a modest woman with long white hair and pointed ears."

show rowan necklace neutral at midleft with dissolve

ro "You're an elf."

vel "{i}Half{/i}-elf. Don't try to flatter me."

"Velrys shook the match in her hand, allowing it to diminish to nothing."

vel "Come along, unless you want to wait until daylight."

"Velrys turned toward another dark tunnel, unlatching the lantern from the ceiling to help guide her way."

ro "Wait a second! Who are you?"

"She gave out a sigh of frustration and glared back at him, uninterested in delving into more conversation about herself."

vel "Isn't my name enough? Will that not satisfy you?"

ro "No, not quite. I think it's at least a little important to know whose… er, home I'm invading…"

vel "And why is that so important? You don't plan to come back so--"

"She stopped herself, eyes narrowing in suspicion as she regarded her intruder."

vel "...You plan to take this mine."

"There was no use in lying, especially when he'd be back with workers to prove it. Rowan nodded."

vel "...Now you're just giving me a reason not to show you the way out."

ro "If you don't show me, I'll just figure it out myself when daylight comes. I'll be back here regardless."

"Velrys bit her lip, and he could almost see her inwardly cursing herself for offering him any hope for assistance in the first place."

vel "This is all I have. I’m not about to treat a threat to that kindly."

"Velrys sighed and touched one of the mine's walls. Her finger tips seemed to search for lost memories."

ro "It's not common to walk into an abandoned mine and discover it...occupied. Surely there is more to this story."

"Velrys cut a glare in his direction but softened when she looked back at the walls of her mine. She sighed deeply."

vel "I didn't have a choice. I used to make a proper living, you know; I was a blacksmith in my village. I loved working with metals."
vel "...Until our village was sacked, and I was carted around between brothels. Some people choose that line of work, but I wasn't one of them."
vel "I managed to escape a few months ago, but I know they're still looking for me. These mines are the closest I have to a home now. I ask that you don't take that away."

"She looked to Rowan with strength and sadness in her eyes."
"There was no way Rowan could simply let her stay here, but another, better idea came to him as he tried to think of possible solutions."

ro "I'm sorry to hear that happened to you, Velrys. No one should ever suffer in that way..."
ro "But how about I offer another solution that could benefit the both of us?"

"Velrys crossed her arms tightly over her chest and eyed him up with suspicion."

vel "And that is…?"

ro "I have to take this mine one way or another, but what if you ran the mine in my stead? You could become the mine's manager. It would be a paid position, and you could have the freedom of staying here as long as you would like."

#persuade check - todo

#pass
"Velrys seemed to take her time considering the idea, hesitant to accept his word outright."
vel "And why would you offer me that position? Surely you can think of someone else that would be more beneficial to you."
"Still, she didn't seem to be outright opposed to the suggestion. That was encouragement enough."
ro "Who more beneficial than the woman that knows the mines the best? What do you say?"
vel "...And I get to stay in the mines? This will be my home?"
ro "You can stay as long as you'd like, but you would be working as a manager for me. Does that sound fair?"
vel "...Yes, I think it does. Very well, I will be your manager. Send me the workers I need and I can begin setting up shop."
"Excellent. I'll be sure to send them here when I return."
scene black with fade
"Satisfied, Velrys held up the lantern high and led Rowan out of the mines."
"It was still dark when he reached the outer cave, but at least the rain had stopped. On top of that, he managed to secure both the mines and a manager, so perhaps this was a larger win than he expected."
#bonus mine production - TO DO
return

#fail - TO DO
#"Velrys sneered at him. Any connection made among them was tossed to the side."
#vel "Absolutely not. Why should I work for you when you're here to take the mines away from me? You cannot just come in and claim something because you want it. You are no better than the slave-traders I was sold " 
#"Velrys spat at his feet."
#vel "I'll show you the way out only because I'm a woman of my word, but I dare you to come back and take this mine from me. I will not make it easy."
#"Velrys snatched her lantern and sped up down the tunnel. Rowan stumbled after her, struggling to keep up.
#"Once they reached the entrance to the mines, Velrys put out her lantern and walked back into the darkness without so much as a goodbye, leaving Rowan alone in the dark."
#"Rowan could not tell her that he was duty bound to bring back a detachment of orcs as soon as he left. What they would do to an interloper would not be pleasant."
#"He looked up at the night sky miserably as he stepped out and began to set up camp." 
#"Well, at least it had stopped raining."
#return