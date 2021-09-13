init python:
    
    event('a_slippery_meeting', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), run_count=1, group='alexia_breeding', priority=pr_npc)
    event('a_lesson_in_intelligence', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), depends =('a_slippery_meeting',), run_count=1, group='alexia_breeding', priority=pr_npc)
    event('an_aquatic_attachment', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), depends =('a_lesson_in_intelligence',), run_count=1, group='alexia_breeding', priority=pr_npc)
    event('a_stinging_confession', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), depends =('an_aquatic_attachment',), run_count=1, group='alexia_breeding', priority=pr_npc)
    event('a_silquien_auction', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), depends =('a_stinging_confession',), run_count=1, group='alexia_breeding', priority=pr_npc)
    event('biting_to_court', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), depends =('a_stinging_confession',), run_count=1, group='alexia_breeding', priority=pr_npc)
    event('clean_tank_for_happy_silquien', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), depends =('a_slippery_meeting',), run_count=1, group='alexia_breeding', priority=pr_npc)
    
label a_slippery_meeting:

$ silFavour = 0

scene bg25 with fade

"Scrubbing the cages clean was certainly not among Alexia's favorite tasks, but it had to be done. Once more she found herself hunched over the dirty stone floor, the bristles of her brush rubbed raw with soap and dirty water. Damned it all, this would be spotless by the time she was finished."
"As she dipped her brush into the bucket once more, the sharp scrape of metal against stone caught her attention." 

scene cg923 with fade
pause 2
show cg924 with dissolve
pause 2 
show cg925 with dissolve
pause 2

"Alexia looked up, surprised to see Draith and one of his assistants--a brutish Orc by the name of Gnash--hauling in a large glass tank, the inch of metal padding at the bottom groaning with each push. Water sloshes over the sides as something large moves inside of it, flitting from one end of the tank to the next."
"There were still a wide variety of cages to clean, but Alexia found herself distracted by all the noise."
"Draith and Gnash grunted as they hauled the tank into one of the cages, sighing in relief once the heavy lifting was finished. Alexia wandered to the cage's open door, peering inside."

scene bg25 with fade
show alexia breeding neutral at midleft with dissolve
show draith neutral at midright with dissolve
show orc soldier neutral at edgeright with dissolve

al "What is all of this?"

dra "Alexia! Perfect timing. Come welcome our newest recruit."

"Draith gestured toward the strange creature inside the tank: its arms connected to smooth flappy skin like a cape, golden eyes wide and fearful--hostile, even--as it soared through the water, desperately searching for a way out." 
"Alexia reached up and steadily brushed a hand along the side of the tank."

gnash "It's a Sil-queen--"

dra "{i}Silquien{/i}. They're a rare breed from the sea. They have a special venom in their tails that, once injected into their victims, will paralyze and shut down all of their organs within minutes. "

gnash "We're gonna give 'em as a gift to Andras for the army."

"Gnash grinned maliciously up at the creature. The Silquien hissed, barring its sharp fangs." 
"Draith glanced behind the Silquien and his eyebrows knit together in concern."

dra "Ah, Gnash, you may want to rethink that plan…"

"Alexia and the orc followed Draith's gaze to a rod poking out of the creature's lower back. It appeared to have been severed, its edges jagged and broken. Although it appeared to have healed on its own, even Alexia could see that something vital had been severely damaged."
"Gnash's fist slammed against the glass."

gnash "Fuck! Damn breed is useless now. Guess we can kill it, feed parts to the others…"

show alexia breeding concerned at midleft with dissolve

"Alexia paled. Even the Silquien seemed to catch Gnash's intentions, its hisses becoming louder, frantic. Alexia and Draith shared a look and immediately shook their heads."

al "You can't just kill this poor thing!"

dra "Absolutely not. I won't allow it."

gnash "Then what do you s'ppose we do with it? 'S got no use."

show draith happy at midright with dissolve

"Draith smiled coldly at him, all forced politeness and honeyed words. Even Alexia felt the chill of his changed demeanor."

dra "Don't worry your pretty little head about it. Why don't you take another look around the pits and find something else suitable to bring Andras? "

hide orc soldier with moveoutright
show draith neutral at midright with dissolve

"Gnash grunted, irritated by Draith's dismissal, but did just that. Draith's pleasant mask fell with the orc's departure, annoyance left in his wake."

dra "Why Andras sent him to work with me, I'll never know…"

"Draith sighed, looking back up at the Silquien. Its hissing had subsided, but the creature now curled up in the bottom corner of the cage and eyed the remaining workers with suspicion. Alexia could not blame him."

dra "He's right, though; we need to do something with him. Poor little guy…"

"Draith pressed a hand against the cool glass as though to pet the creature. The Silquien's eyes narrowed further."

show alexia breeding neutral at midleft with dissolve

al "Will you really get rid of him?"

dra "Of course not, but taking care of him myself is going to be too much work. If he's really disabled--and it looks like he is--then he's going to need extra attention."

show draith happy at midright with dissolve

"Draith spun on his heel and smiled at Alexia. She could practically see the wheels turning in his fair-haired head."

dra "Which makes you the perfect candidate!"

show alexia breeding concerned at midleft with dissolve

al "M-Me? I don't… I don't know…"

"She glanced back at the Silquien, unnerved by its harsh glare."

dra "You'll be perfect, Alexia. He's probably just uncomfortable, being in a new environment and all. Gnash's ugly mug probably scared the poor thing half to death."

"Draith laughed, but Alexia was sure he wasn't joking. Gnash unnerved her and they barely had any interaction. She could only imagine how the monsters he handled felt."

dra "This poor boy could use some nurturing back to health. You'll be great at it."

"Alexia looked back at the creature, but he had retreated into a makeshift rock home inside of the tank. Occasionally she saw his golden eyes poking out through the dark, watching her."

al "How can you tell it's a boy?"

"Draith tried to get a good look of the Silquien to point it out, but with it hiding, there wasn't an optimal angle. Draith sighed, giving up."

dra "It's hard to see, but at the front of the tail there's something like a compartment in male Silquiens; their cocks stretch right out when they're excited. Females, on the other hand, have large openings."

al "Oh."

show alexia breeding happy at midleft with dissolve

"Alexia bit her lip. She tried to smile at the Silquien, but whether he understood the gesture or not, she had no idea. How was she supposed to take care of a creature that wanted nothing to do with her?"
"That didn't seem to cross Draith's mind, though. Or, if it had, he simply didn't care."
"Draith led Alexia through the breeding pits to collect a few things for the Silquien's tank, rattling off information on how to care for the creature--what it ate, its daily patterns, what to avoid, how to apply medicine, anything Alexia needed to know as his caretaker."
"Alexia struggled to keep up with all the details of the task." 
"It was not so simple as most of the monsters in the pits; the Silquien was a sea creature, so she needed to take extra care to ensure his water was the right temperature and consistency, as well as other small tasks that she was not used to with the other monsters."
"By the time Draith had finished running her through all of the information, Alexia was sure she only retained half of it. She didn't tell Draith that, though. She would figure it all out somehow."
"Once they reached the tank again, the Silquien was out of his hiding spot, curiously watching the other monsters that passed by. Alexia paused, taking a moment to admire his childlike wonder." 
"This must have all been so new for him; she remembered when it was new for her as well, her own fears and notions mixed with a sense of excitement and curiosity. Like a new adventure was about to begin."

dra "I'll leave you to it."

hide draith with moveoutright

"Draith patted Alexia's shoulder before disappearing into the pits. The Silquien didn't even seem to notice her presence, his eyes focused on the door from which the dark elf had left."

al "Interesting creatures, aren't they?"

"She smiled at the Silquien, suddenly feeling silly for talking to him. It wasn't as though he could understand her. And yet, the Silquien cocked its head to the side, regarding her. Perhaps he was more attentive than she thought."
"Alexia's gaze drifted to an exposed flap of the Silquien and the rough cuts along it. The skin was not so smooth after all; tears and cuts aligned the creature's back, some long healed while others looked fresh or reopened."
"She pressed a hand to her mouth, horrified. Who--or what--had done this? Was this part of the effort to enslave the creature? Or was it being preyed on in the wild, seen as an easy target because of its broken tail?"
"A trickle of blood lifted from his back and dissipated in the water. Her heart plummeted." 
"Alexia took a step forward, arm outstretched. The Silquien suddenly turned on her, lifting his arms to appear large and intimidating as it hissed."

menu:
    "Heal his cuts.":
        $ released_fix_rollback()
        $ silFavour += 1
        "Alexia flinched at his harsh response but held her ground. He was her responsibility now, and she wasn't about to let his cuts get infected."
        al "You likely can't understand me, but please, I just want to take care of your cuts."
        "Alexia reached for the medicine supplies in the corner and held it up to the glass for him to get a good look." 
        "She felt ridiculous--none of the other caretakers talked to their monsters like this, as if they could truly understand what she was saying--but the Silquien closed his mouth, narrowing his eyes at her and the bottles."
        "After a few moments of silence, Alexia climbed up on the ladder to reach the edge of the tank. She had assumed she would need to wait there for a while, but the Silquien slowly positioned himself underneath her, his back flat against the surface."
        "Alexia stared at the marks, a twinge of guilt rising in her chest alongside… surprise? It was impossible that this creature understood her, but could he trust her already?"
        "Noticing her hesitation, the Silquien turned its head to glare up at her, his eyes slit with suspicion. Alexia carefully dabbed a cloth with the medicinal liquid and stroked it along his back."
        "The Silquien had howled at first, rushing back down to the tank to resume hissing at her from afar, but after some coaxing, he returned. He did not howl again, but he did watch her every move, wincing when the sting of medicine met his scars."
        al "I just want to help you.  This will make it hurt less, I promise."
        "Alexia repeated the mantra to him several times, her voice turning into a near soothing melody as she cleaned the Silquien's wounds." 
        "By the time she was finished, the Silquien did not hiss or bare his teeth at her. He simply watched as she packed up the medicine, gave him a warm smile, and returned to her other duties."
        return
        
    "Leave him to heal on his own.":
        $ released_fix_rollback()
        "Alexia stared at the poor creature, too afraid to take another step. As much as she wanted to take care of him, he was clearly hostile. There was no guarantee she would even be able to get near his back without his fangs digging into her skin."
        "With a heavy heart, Alexia turned and walked away. She would just have to hope he eased up on her or that the cuts would heal on their own."
        return
        
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label a_lesson_in_intelligence:

scene bg25 with fade

"Despite the dank smell of the breeding pits, Alexia found herself enjoying her time down there more often, sometimes even looking forward to her next shift." 
"She particularly looked forward to seeing her new waterbound charge. The creature that Draith had assigned her to care for."
"She brushed her fingers against the Silquien's healed back, the texture far smoother than the ragged misshapen cuts she had been treating. He was healing, perhaps in more ways than one."

show alexia breeding happy at midleft with dissolve

al "You're doing wonderfully, Sil! I'm so proud!"

"The Silquien vibrated pleasantly in response, rippling the water around him."
"Since their initial rocky meeting, Alexia had gotten better at handling the Silquien over time, eventually giving him the name Sil for her own memory's sake. Sil seemed quite happy with the name, beaming at her with approval once the nickname had been offered."
"Sil currently swirled around in his new tank, twisting and turning out of the rocky holes of coral with a look of pure delight on his face. He seemed to do that every time Alexia praised him these days, performing a little spin around his enclosure while he vibrated in delight."
"With more time spent between them, Alexia began to notice that many of Sil's behaviors were quite human in their nature: the way he regarded others, the looks of understanding they often shared." 
"She could swear she even heard Sil utter a few words under his breath as the other monsters passed, but she immediately chalked it up to her own overactive imagination." 
"With the rest of Sil's medicinal treatment completed for the day, Alexia lowered herself from the ladder beside his tank." 
"There were still several other tasks she needed to complete--many chores that she had been neglectful of in exchange for keeping Sil company--that would earn her a reprimand if she did not attend to them soon."
"Sil watched her lower herself down the prongs, his excitement suddenly muted. He always seemed sad to see her go, which only furthered Alexia's theory." 
"As she and the creature had gotten to know each other better, Alexia found it harder and harder to leave his side. He must be lonely sitting in that tank all day by himself. She knew that she certainly would be."
"Alexia hopped off the last step of the ladder, her shoes scraping against the stone floor." 
"Whereas she felt precarious--sometimes even whimsical--sitting atop the ladder, more than tempted to dive into the water and swim beside Sil, the ground felt solid. Real. It grounded her, reminded her that such thoughts were merely fantasy."
"The real way to escape her problems was not so easy."
"Before Alexia could remove herself from the cage, Draith rounded the corner, peering in curiously at the moping Silquien before settling his gaze on Alexia."

show draith happy at midright with moveinright

dra "He looks even more depressed than when we brought him in."

"Alexia glanced back at Sil. Sure enough, the Silquien was staring back at her, his fingers pressed up against the glass. Pleading her, begging her not to go."

show alexia breeding neutral at midleft with dissolve

al "He often gets like this when I have to leave. I always feel so bad."

"Draith nodded, approaching the tank. He observed the cuts on the Silquien's back. They had healed considerably over the past few weeks, nothing but pink scars now."

dra "You've done a great job back here; I was worried he was going to be infected when we brought him in, but he seems perfectly fine. Well, except for the tail."

"Draith looked back at the rod protruding from Sil's behind. Although Draith had done his best to help Sil, there was no fixing the tail that was damaged beyond repair."

al "He doesn't seem to mind it. Now that he's being fed regularly, there isn't much use for a weapon like that."

dra "No, I suppose not."

"Draith sighed, patting the glass tank once before turning back to Alexia."

dra " I have to admit, I like the guy. I'm always rooting for an underdog to make it out like this, but Gnash…"

"Alexia frowned, glancing back at Sil. Gnash had made his position on Sil clear: find a use for the creature or get rid of it. Alexia found the idea of tossing Sil out into the wild after she had worked so hard to heal him inhumane. There had to be a better way."
"Maybe there was."

al "Ah, Draith, there's something I've been meaning to ask you, actually."
al " How intelligent are the Silquiens? Can they… would it be possible to understand human behavior to some extent?"

show draith neutral at midright with dissolve

"Draith blinked, surprised by Alexia's sudden change in direction, but pondered the question. He rubbed his chin, eyeing up Sil in deep thought."

dra "To be honest, I don't have much personal experience with Silquiens--or at least their intelligence. The dark elves had some on hand, but usually they were trained and weaponized like most of the beasts in their care."
dra "As for Sil, I can't be sure. It would be interesting to see what he picks up under your care though."

show draith happy at midright with dissolve

"Draith smiled at her and Alexia felt a surge of hope. Maybe Draith didn't know exactly how smart the creatures were, but if Alexia could find out if Sil was intelligent to some degree, they wouldn't have to get rid of him after all."

show alexia breeding happy at midleft with dissolve

al "Thanks, Draith. I think I'll spend some time practicing with him for a little longer, if you don't mind."

dra "That's fine with me. It all counts as work in some way or another. Just make sure to clean your cages for the day."

hide draith with moveoutright

"Alexia nodded, a smile etched onto her face as Draith left. Sil observed her quietly from his tank, likely confused that she had not left as well. Alexia turned to him instead, a new sense of resolve coursing through her."
"She would not let Gnash take him away from her so easily."
"Once her work for the day was done, Alexia spent the rest of her evening and most of the night putting together a string of lesson plans for Sil: the basic alphabet, arithmetic, science, culture, history, anything she could think of that a young child--or in this case, a monster with a gentle gaze--might grasp onto."
"Sil watched her curiously as she carried in her books the next day, carefully tucking one under her arm as she reached the top of the ladder."
"Sil popped his head out at the top of the tank, eyes wide as he took in the book in Alexia's hands. She showed him the cover and a few pictures inside."

al "I think you're smarter than you look, Sil, so we're going to try something new today."
al "I want you to knock once if you understand. Can you do that for me?"

"Then, when Alexia asked him again, he thumped as well. Just once: he understood."
"A surge of pride overwhelmed her, but Alexia did well to calm herself. It could have been a coincidence, but the excited part of her brain told her it was no such thing."

scene black with fade

"So her lessons began. Alexia covered a wide range of subjects, jumping between small concepts at a time in an attempt not to overwhelm the creature." 
"She taught him basic commands: thump once for yes, twice for no, and three times if he was confused. Sil seemed to pick these up quickly and, although Alexia had a feeling he understood, part of her wondered if she was simply reading too much into it."
"After three days, however, Alexia was sure that it was no coincidence. Sil was learning."

scene bg25 with fade
show alexia breeding neutral at midleft with dissolve
show orc soldier neutral at midright with dissolve

gnash "Do you even work here anymore?"

"Gnash's rough voice cut in through one of Alexia's lessons. She frowned, peering down at the orc as he approached the tank. Sil didn't seem thrilled by his presence either."

gnash "What're you doing up there with 'em books?"

menu:
    "Testing Sil's intelligence.":
        $ released_fix_rollback()
        $ silFavour += 1
        "Although she was reluctant to give Gnash {i}any{/i} information on Sil that the orc could use to his advantage, Alexia was proud of Sil's accomplishments. Perhaps if Gnash saw that Sil was useful after all he wouldn't feel the need to threaten the creature with banishment or death."
        al "I'm teaching Sil the alphabet. He seems to understand the words, so we'll be practicing speaking next."
        "She smiled proudly at the Silquien and, if she wasn't mistaken, the Silquien smiled back. His tail thumped once against the glass."
        "Gnash barked out a laugh beneath her, startling Alexia."
        gnash "Monsters don't {i}learn{/i}! Stupid girl. Wasting time…"
        "The words crushed Alexia but she held her chin up and tried not to show it. She did not want to admit that she too had questioned her own abilities."
        al "You haven't spent enough time with him. Sil is quite the competent student."
        gnash "Believe it when I see it."
        
    "Taking a break from work.":
        $ released_fix_rollback()
        "Although Alexia was proud of Sil's accomplishments, the idea of conveying his intelligence to Gnash didn't sit right with her."
        "No doubt he would finally see that Sil was useful, but at what cost? She didn't like to think about what Gnash would do with him if he knew of Sil's comprehensive abilities."
        al "I'm just taking a break from work."
        "Alexia placed a bookmark between the pages and subtly hid the title behind her hand. She didn't need Gnash to see what she was reading and put two and two together."
        al "Was there anything you needed, Gnash?"
        "She smiled politely down at him, although the gesture felt forced. More than anything she wanted to push him out of the cage, keep his glaring eyes away from Sil." 
        "She saw the way he looked at the Silquien, viewing the creature more like a sack of meat instead of a sentient being. It was the same look he gave Alexia."
        gnash "Came to see what his use is. You got one yet?"
        al "...We're still working on it."
        
"Gnash snorted, his face becoming uncomfortably close to the glass. Sil moved away, his body taking shelter behind the coral structure inside. Apparently he did not like the way the orc stared at him either."

gnash "I been talkin' to some others. This thing should still have his venom inside, so if we cut 'em up, we can take it out and bottle it up."

"Alexia blanched, a slight tremor taking over her body. She had assumed she would have more time to prepare, some excuse she could throw his way and shield Sil with, but if what Gnash said was to be true, she could think of little that would dissuade him from gutting the poor Silquien."
"Sil seemed to grasp the meaning of Gnash's words, hissing once at the orc before disappearing entirely in the formation of coral. Alexia could see the glow of his eyes glaring out at Gnash through one of the holes."

al "Give me a little more time. I'll have something soon, I promise."

show alexia breeding concerned at midleft with dissolve

"Gnash grunted, his gaze raking over her body once. She shivered, clamping her skirt tightly between her legs."

gnash "Time's almost up, lady."

hide orc soldier with moveoutright

"Thankfully, the orc left, his heavy footsteps echoing through the chamber before disappearing entirely. Sil peeked out of his hiding spot, glaring after him."
"Alexia tried to smile, tried not to show her fear, as she flipped the book back open on her lap."

al "...Let's get back to it, shall we?"

"But even as they continued their lesson, neither one seemed to share much enthusiasm for the rest of the day."

return

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

label an_aquatic_attachment:

scene bg25 with fade
show alexia breeding happy at midleft with dissolve

al "Very good, Sil! You're adapting very quickly. I'm impressed."

sil "Thank you…"

"Sil grinned at her from inside of his tank, his tail swishing happily in the water as Alexia pulled out another block of flashcards she had prepared. Sil watched with eager anticipation, his lithe body swaying from side to side."
"Alexia found herself increasingly impressed by Sil's progress. They had moved from basic hand gestures as a form of communication to verbal language in a matter of days, and she was sure it would only be a matter of time before he mastered the art of reading as well."
"Sil truly was an intelligent creature. Alexia felt a surge of pride run through her as she presented the next batch of flash cards. As they ran through the next set of words, Alexia wondered if all Silquien's were this smart or if Sil was just lucky."

al "Alright, try to sound this one out. I know it's a long one, but I have faith in you."

"Alexia held up a card with the word {i}cherish{/i} written in her elegant looping scrawl. Sil squinted at the word, puzzled."

sil "Cah-er…"

al '"Not quite. Remember what sound these characters form? "{i}Ch{/i}".'

sil "Cher… Cherish…?"

al "Precisely."

"Alexia flipped the card over. She had made sure to write the definitions of each word on the back and would attach them to the side of Sil's tank before she left each day." 
"The method seemed to work, although she wished she could think of a waterproof option to go inside of his tank instead…"

al "{i}Cherish{/i}. To care for and protect someone in a loving manner. See?"

"She pressed the card flat against the glass for Sil to get a good look. His eyes flitted across the parchment, drinking in the scrawl, before nodding once."
"Alexia took a bit of the strange sticky goo out of the little glass bottle and stuck the card to the glass." 
"Draith had offered her a bottle of the stuff a while ago, but she didn't find a use for it until now. Alexia wasn't sure what monster it came from, or what it was in the first place, but she felt some things were better left unknown."
"She picked up the next card, ready to begin again."

sil "Alexia?"

"The way Sil said her name was strangely accented, and combined with his muffled voice underwater, it sounded like a melody coming from his lips. She loved the way he said it, drawing out each syllable."
"Alexia looked up at once, surprised by Sil's interruption. Usually he was so quiet during their lessons."
"Sil averted his gaze, suddenly nervous now that he had her attention. His mouth opened and closed as though he was searching for the right words." 
"She felt bad for him; communicating was not easy under normal circumstances, but it was doubly frustrating when there was a language barrier between them."

al "What is it, Sil?"

"She smiled at him patiently. Sil took his time as he constructed what he wanted to say."

sil "Sil… cherish… Alexia?"

show alexia breeding shocked at midleft with dissolve

"He said it as though he was asking permission. Alexia blinked, taken aback."

al "You cherish me?"

"Sil nodded confidently, but he still looked nervous. Was he afraid she would be mad?"

show alexia breeding happy at midleft with dissolve

"Alexia felt the opposite; she was touched by his declaration. His words brought a warm smile to her face. He probably didn't understand the romantic connotation behind the word, but Alexia couldn't bring herself to correct him. The gesture was too sweet."

al "That's very kind of you, Sil. I cherish you as well."

"Sil's face lit up in delight. He swirled around in his tank and Alexia laughed."

show orc soldier neutral behind bg25

gnash "Don't see no work getting done ov'r here."

hide orc soldier
show orc soldier neutral at midright with dissolve

"The mood deflated as Gnash approached the tank, his large orcish body casting a shadow over the glass. Sil moved back against his coral home, the structure protecting him as he glared at the orc."

show alexia breeding neutral at midleft with dissolve

"Alexia looked down at Gnash from atop her ladder, shifting to adjust her skirt more modestly over her legs. She hated the way he tried to stare up her skirt from below."

al "Hello, Gnash. Can we help you?"

gnash "Yeah. What's the beast's weight?"

al "His weight? I'm not sure. What do you need to know that for?"

gnash "Preppin' meals for other beasts. Wanna know how much this one'll feed."

"Gnash barked out a laugh, his grin vicious. Alexia felt a chill run down her spine but she remained composed, eyes narrowing in distaste."

al "That isn't funny, Gnash."

gnash "Not jokin'."

al "You can't talk like that in front of him. He knows what you're saying."

gnash "He don't know shit."

"Gnash set his eyes on the Silquien. Sil slid further into his coral structure, but gave no indication that he knew what Gnash was talking about. He appeared like most of the monsters Alexia had come across, compliant and mindless." 
"Gnash laughed again, the sound rough and throaty. It grated on Alexia's nerves. He left them there, the atmosphere soiled by his presence."

hide orc soldier with moveoutright

"Sil slid out from his hiding spot once Gnash was determinedly gone. He glared at the spot the orc was last seen, uncharacteristic hatred in his eyes. He knew exactly what Gnash was implying."
"Alexia reached into the tank to pet his head. Sil jolted, but any surprise he held was quickly erased by the soft caress of her fingers. His body vibrated, thriving on her touch."

al "I'm sorry you had to hear that. I'm not going to let him do anything to you, alright? I promise."

"But even as she said it, Alexia wasn't sure how realistic her promise would be. When it came down to it, she was ranked pretty lowly among the workers of the breeding pits."
"She may be able to get Draith on her side, but there was no guarantees that Gnash wouldn't fight tooth and nail for Sil."

"Sil seemed to understand that as well. His vibrations stopped, a solemn look on his face. It pained her to see it."
"But it was time for her to go."

al "I'll be back tomorrow, alright? You'll be safe until then."

"Her fingers lingered on his head then slowly pulled away. Sil caught her hand, eyes wide and pleading."

sil "Stay."

al " But my shift is over--"

"His grip on her hand tightened."

sil "Please."

"...Well, how was she supposed to say no to that?"

al "Alright. Just for a little bit longer, though."

show alexia breeding happy at midleft with dissolve

al "And we'll be using this time as an opportunity to study, alright?"

"Sil visibly relaxed. He smiled, releasing her hand. It didn't appear that he cared what they did, so long as Alexia stayed by his side."
"Gnash must have really scared him."
"Alexia settled herself on the ladder and continued flipping through their flashcards. Sil responded enthusiastically, trying to sound out and understand the words even more than usual. Alexia suspected he was trying extra hard in the hopes she would not leave when they were finished. "

show draith happy at midright with moveinright

"Draith strode into the room a little while later, a bemused expression on his face. Sil didn't seem to mind Draith in the slightest, observing the dark elf with no more than idle curiosity."

dra "How are the lessons going? Can he recite poetry yet?"

"Alexia chuckled, shaking her head."

al "No, but I'm sure we'll be there in no time. He's making excellent progress."

dra "I'll say."

"Draith looked the Silquien up and down with a smirk before directing his attention back to Alexia. There was no doubt the Silquien's lithe, muscular form was appealing to the dark elf. Alexia couldn't deny that Sil was rather attractive."

if silFavour > 0:
    dra "You've been spending a lot more time with him lately, Alexia. You haven't developed a crush on our new little monster, have you?"
    "Alexia laughed, grateful that {i}crush{/i} was not a word she taught Sil yet. He watched them both from the safety of his tank, confused."
    al "We have become quite close. I enjoy spending time with him."
    
else:
    dra "The poor thing looks so lonely when you leave, Alexia. I feel bad for him."
    al "Aw. Well, I miss him, too. We've become quite close."
    "Alexia smiled at Sil over the top of the tank. He grinned back at her, his expression soft."
    
"Draith glanced between the two of them, an impish smile curled on his lips. His gaze roved over Sil once more, stopping low on the Silquien's body."

dra "I think Sil wants to get even closer."

show alexia breeding aroused at midleft with dissolve

"Alexia followed Draith's line of sight, a blush creeping up her neck to her ears as she took in the sight of Sil's large member poking out below his stomach. She stared at it, trying to fathom how she had missed it before."

al "Is that…?"

"Draith nodded, his smirk growing wide."

dra "That would be his cock, yes. Male Silquiens are able to retract them most of the time, but sometimes they can't help it. I'm surprised you didn't notice sooner."
dra "They even have an airflap above their cockslit to provide air to their lungs! Fascinating, isn't it?"
dra "Oh, but you wouldn't have to worry about him losing breath - Silquiens have plenty of ways to take in air."

"Alexia's gaze fell to the flap above Sil's cock, making the connection." 
"Draith was enjoying this too much. Sil tilted his head to the side, oblivious to Alexia's embarrassment. Of course he wouldn't understand, he was just a Silquien..."
"But he was an incredibly smart and {i}sentient{/i} Silquien…"
"Draith patted Alexia's arm and turned to leave."

dra "I'll leave you two to your fun. Keep up the good work~!"

hide draith with moveoutright

"Alexia worked to contain her blush as Draith left, but she found her gaze continuously falling back onto Sil's erection. To his credit, Sil didn't seem to mind her staring. If anything, his erection grew larger."
"Sil cherished Alexia." 
"Perhaps he {i}did{/i} know the meaning behind it." 
"She looked back up at Sil; at those warm eyes and pretty sea-blue hair. He was attractive, for a beast. Alexia would be lying to herself if she pretended she didn't look at him a little {i}too{/i} fondly at times."

menu:
    "Give Sil a blowjob.":
        $ released_fix_rollback()
        $ silFavour += 2
        $ change_corruption_actor('alexia', +5)
        jump silBJ
        
    "Ignore Sil's erection.":
        $ released_fix_rollback()
        "She knew what Draith meant by leaving her alone with Sil after having pointed out the obvious, but she couldn't bring herself to act on it. Sil was still a monster, no matter how sentient and well-intentioned he was."
        show alexia breeding happy at midleft with dissolve
        "Alexia forced a polite smile on her face and did her best to push back the erotic thoughts surfacing in the back of her head as she continued Sil's lessons."
        return

label silBJ:

"Alexia felt her own desire well up inside of her, a sudden moisture forming between her legs." 
"How long had she been denying her own attraction to Sil? Was she depraved for the thoughts she had of him now? She couldn't take her eyes off of his light cock. Would it be as smooth as his back, or rough and scaly? "

al "Sil, would you come up here for a moment?"
 
scene cg926 with fade
pause 3 
show alexia breeding aroused behind cg926
 
"Sil popped his head out of the water, blue hair sticking to his face as he watched Alexia reach down to run her hands over his shoulders. His skin was considerably smoother than a normal human's, as if he had been coated entirely in lotion. "

al "You cherish me, don't you?"

sil "I do."

scene cg927 with fade
pause 3

"He breathed sharply as Alexia's nails trailed down his chest. Water splashed onto her dress, but she couldn't bring herself to care."
"The tank was deep; despite Draith's promises, Alexia felt the fear of drowning coil through her body. Sil watched her with wide eyes as she stripped down, carefully leaving her clothes on a pile on the ladder before climbing in."
"Alexia let out a gasp-- the water was freezing!-- but Sil pulled her in his arms, keeping her head out of the water while his cape-like flaps kept her snug against his body. A pleasant thrill ran through her as she felt his cock throb against her thigh."

sil "Alexia…"

"Alexia was always surprised to learn what Sil already knew, but none of his quick learning surprised her as much as the feel of his lips on hers, his tongue lightly tracing her bottom lip."
"She moaned against his mouth, deepening their kiss with her tongue before she took in a deep breath and lowered herself further in the water."
"Sil moved to pull her back up, but Alexia pushed his hands away, feeling around his body until she latched her mouth onto his cock."
"Oxygen filled her lungs at once, as well as the salty taste of his cock. Alexia almost released him in surprise but held on, her fingers digging into the Silquien's hips."
"She heard Sil gasp above her, but she kept her eyes shut, afraid to open them under the salty tank water. Draith had been very specific about the amount of salt…"
"Alexia felt two hands come down to press her face further down his cock. She took his member with ease, surprised and delighted by the smooth texture as it slid down her throat. She didn't even need to worry about controlling her breathing."
"Sil bucked against her, his tail curling around her waist. Alexia bobbed her head up and down, the feel of the end of his tail pressing down her belly sending a shudder through her. What would it feel like inside of her? What would he feel like inside of her?"

show cg928 with sshake
show cg928 with sshake
show cg929 with flash
pause 3

"The thought placated her as Sil reached his climax, his hips grinding against her face hard. She could hear Sil's muffled panting become more frantic through the water, his grip tightening on her hair and waist as he released his seed deep in her throat. "
"Alexia swallowed hard and took another deep breath from his cock before swimming up to the surface."
"Somehow the oxygen on land didn't taste as satisfying as the kind she had been sucking off of him. Sil helped keep her upright in the water as he swam her back to the tank's ledge. "
"He pressed soft kisses to her neck before lifting her back up onto the ladder. Alexia's legs felt shaky, but she quickly pulled her clothes back on, careful not to drip too much water onto her flashcards."
"As she began to climb down the ladder, Sil's voice caught her attention."

scene bg25 with fade
show alexia breeding happy behind black

sil "Alexia enjoyed?"

"She smiled back and nodded."

al "I really enjoyed it, Sil. Promise."

"Sil's face lit up. For once, he was still smiling as Alexia gathered her things and left the cage."

return

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

label a_stinging_confession:

scene bg25 with fade
show alexia breeding happy at midleft with dissolve

"The pits reeked of must and wet fur as Alexia weaved her way through the cages. She did her best to scrub the scent out-- from both the cages and the creatures themselves-- but there was only so much she could do while they waited for more supplies to be shipped in."
"Sil's tank was clean at least, and the Silquien creature's face lit up when Alexia approached with a stack of books in her arms."

sil "Alexia!"

"She smiled, utterly charmed by his childish excitement. It was hard to ever be upset at someone whose entire demeanor lit up when she walked in the room."

al "Good afternoon, Sil."

sil "Good afternoon."

"He grinned with a full row of sharp, pointed teeth. Somehow they didn't even look threatening on his sweet face."

al "Are you ready to begin our lessons for the day?"

"Alexia held up her books: an assortment of classic texts ranging from history to theology. She hadn't yet touched the subject of religion with him, but with Sil's progress, she was curious to see his take on it."
"Sil did a little spin in his tank, the excitement practically radiating out of him. He nodded, taking up his usual position near the top of the tank."
"Alexia climbed the ladder and joined him, flipping open one of the books to where they left off previously."
"Sil had proved to be of greater intelligence than either Alexia or Draith realized. He understood basic concepts as Alexia explained them to him and seemed to grasp critical thinking skills that even the most clever creatures in the pits seemed to lack."
"She didn't even know if she could call Sil a creature anymore. He possessed too much intelligence-- too much sentience-- to be deemed as such." 
"Was it right, then, for them to keep him in the pits? Sil didn't seem to mind his enclosure-- preferred it, even, when Alexia had asked if he missed the ocean-- but that didn't make her feel any less guilty for keeping him here among the strange animals and creatures that Draith came across."
"Alexia couldn't think of many places outside of the pits for his tank, though. Not without him facing harassment from others in the castle. Even her own chambers didn't spare the room, and anywhere public would only put Sil in harm's way."
"No, the pits were the best place after all, she decided. At least he was happy here, and he was safe."
"Relatively safe."
"Alexia had barely finished reviewing the territorial war of the River Red when Gnash came tromping over. She almost expected the stone to crack under his heavy footfalls."

show orc soldier neutral at midright with moveinright
show alexia breeding neutral at midleft with dissolve

al "Hello, Gnash."

"It was hard to hide her distaste as he approached the tank, his light, glassy eyes trailing Sil up and down like meat hanging on a rack. Sil glared at him but inched closer to Alexia, as though he would pull her into the water if things got out of hand."

gnash "You still wastin' your time on this piece'a meat?"

"Gnash's words came out discordant and jumbled, as if he were chewing each syllable, but Alexia understood him well enough by this point."

al "It is not a waste. Sil has made excellent progress, more than I can say for most creatures."

"If Gnash noticed the pointed look she gave him, he didn't let on. She was almost disappointed as he disregarded her entirely, his focus solely trained on the Silquien. Sil bared his teeth, a low hiss caught in the back of his throat."

gnash "Alright. If he's so smart, prove it. Show me what he's learned."

"Alexia sat up straight, donning the aura of an instructor at work."

al "Very well. Sil, won't you read this page for me and answer the questions at the bottom?"

"Alexia flipped to a different page, one they had covered extensively, and held the book out to him."
"Sil gave her a dubious look, hesitant to perform for the monstrous beast. He was a person of sorts, not a mindless animal."
"Still, it appeared he would do anything for Alexia's favor."
"The Silquien read back the paragraphs in full, darting annoyed glances in Gnash's direction as he did so, before answering the questions at the end of the page. Alexia had him do this a few more times with different books and subjects. "

show alexia breeding happy at midleft with dissolve

"By the end, Sil seemed more proud at his progress than annoyed by the tasks at hand. Alexia smiled at him, her own heart swelling with pride as well."
"She snapped the book shut and set it beside her."

al "As you can see, Sil has been studying very hard in your absence."

"Gnash stared at Sil, his silence unnerving. Alexia had to bite back her frustrated response." 
"Did he not see the potential Sil had? Was he not impressed by the progression they've made? Sil was a breakthrough study. There was still so much more to learn about him, so much more to test."
"Finally Gnash turned to her, and she dreaded the darkly satisfied gleam in his eye."

gnash "So he is smart. Heh. Maybe he won't be such a waste after all."

show alexia breeding neutral at midleft with dissolve

"Alexia shared a wary glance with Sil. The way Gnash stared at the Silquien sent a shiver down her spine. Compliments from Gnash were rare and Alexia felt strange to be on the receiving end of one."

al "Thank you. I'm glad you can finally see the value in our work."

gnash "Oh, I see the value alright. This beast's gonna make us a fortune."

show alexia breeding shocked at midleft with dissolve

al "What?"

"She felt the blood drain from her face and her lips part in shock. A battering ram to the chest would have been an easier blow than what Gnash was suggesting."
"The orc didn't seem to notice-- or even care-- about Alexia's state of shock. He carried on, staring at Sil as though he were made of gold instead of the dear Silquien he was."

gnash "I'll set the auction up for 'em. A beast this smart's gotta be good for battle, sure, but fools'll pay even more for 'em as a slave."

show alexia breeding concerned at midleft with dissolve

al "You-- You can't do that!"

"Sil, a {i}slave{/i}. No, she couldn't let that happen. Alexia refused to entertain the idea."
"Gnash snorted, the sound pig-like through his smooshed nose and protruding teeth. Angry tears pricked Alexia's eyes but she blinked them away, refusing to allow him the satisfaction of seeing them."

gnash "I can do what I want. Don't be bossin' me around."

al "Please, Gnash, just reconsider. There's no reason to sell him off. He can be useful--"

gnash "I made my choice. What we do with 'em is my decision, so say yer goodbyes now. He won't be around much longer."

"Gnash grinned at Sil through the tank and patted the glass with a large, rough hand. Sil hissed in response, the stub of his tail swishing angrily in the water."
"Gnash laughed and the sound raked on Alexia's patience. The orc walked off to plan the auction, leaving the anxious pair behind."

hide orc soldier with moveoutright

"Alexia swallowed hard, the urge to cry creating a lob in her throat. Would Sil really be leaving her behind, sold off to some rich patron like cattle?"
"She was certain whoever Gnash planned to sell Sil off to wouldn't treat him with the same kindness she had. The idea of someone else taking him in and causing the Silquien any harm left an ache in her chest."
"Alexia felt Sil watching her, gauging her reaction. He was smart enough to know what Gnash meant by selling him off. She almost wished he wasn't so intelligent, if only so she could protect him from his own fate."
"Taking a deep breath, Alexia grabbed one of the books and flipped it open. She didn't care where their lesson started today as long as she could keep her mind preoccupied."

show alexia breeding happy at midleft with dissolve

"With a shaky smile, she turned to Sil."

al "Let's get back to our studies."

"She couldn't bring herself to meet his gaze as they began a new subject entirely. Sil didn't seem to mind, easily keeping up with her questions and explanations, but Alexia struggled to push through their lesson."
"Each passing second felt like another step closer to Sil's inevitable slavery. Each correct answer left her feeling further and further away from him, until Alexia couldn't take it anymore. She shut the book and set it aside."

al "Perhaps we should end our lessons early today."

"She loathed the idea of ending their session early, but they would not be making any progress with her moping about. She was practically useless to him right now, too depressed to carry on for the day."

show alexia breeding shocked at midleft with dissolve

"Sil frowned and leaned over the edge of the tank. She gasped when his hand reached out to caress her cheek, his skin cold and unnaturally smooth against hers. Sil pulled back, afraid to have hurt her, but slowly reached out once more and touched her face again."

sil "Don't cry."

show alexia breeding concerned at midleft with dissolve

al "I'm not."

sil "You are."

"Alexia reached up, already aware of the tears spilling over. She hastily wiped them away and shook her head. Now was not the time for tears. If anything, Sil should have been the one crying; it was his life he was losing, after all."

al "You don't need to worry about me, Sil. This isn't about me, it's about you."

"Sil looked like he wanted to argue but kept his mouth shut, continuing to caress her cheek with utmost gentleness. She couldn't help inclining her head against his palm."

al "This isn't fair to you. What is it {i}you{/i} want?"

sil "What I want?"

"Sil seemed shocked, as if the idea of wanting anything had only just occurred to him. Alexia nodded in encouragement. Sil pressed his lips together tightly, consumed in thought."
"Then--"

sil "I want to stay by Alexia's side."

show alexia breeding happy at midleft with dissolve

"His statement nearly warmed her heart as much as it broke her."

al "You want to stay with me?"

"She tried to keep her voice light, flattered, but it was impossible to hide the heartbreak that seeped in. It was an impossibility."
"Sil nodded, fully confident in his answer. His fingers trailed closer to her lips. Looking to her for permission, his thumb ran over the soft curve of her bottom lip."

sil "I love you, Alexia. I want to stay with you."

"Alexia was about to answer but she stopped herself, seeing the look in Sil's eyes. This was not some attachment to a friend."
"This was his love confession."

menu:
    "Reciprocate Sil's feelings.":
        $ released_fix_rollback()
        $ silFavour += 3
        "Alexia's heart thundered in her chest, a hundred emotions soaring and crashing through her."
        al "I love you too, Sil."
        "The words were out before she could even think of taking them back. How long had she felt this way about him? How long had she suppressed this part of her, hoping it would go away like any other intrusive thought?"
        "Sil didn't give her the option of reconsidering. He leaned over the tank, took her face in his palms, and kissed her."
        "Sil was inexperienced, of course-- where would he have had the opportunity to learn how to kiss, being stuck inside of a tank?-- but Alexia didn't mind. She melted from his touch and helped guide him, her tongue easing its way inside of his mouth, careful to avoid brushing against the sharp points of his teeth."
        "Sil shuddered, his hands sliding to her arms and gripping her hard." 
        "He slipped, accidentally pulling her into the tank."
        #cg1
        scene black with fade
        show alexia breeding shocked behind black
        "Alexia grasped, clinging onto the Silquien for dear life. Sil pulled her back above the water, uttering apology after apology as she coughed up the lungful of water she'd sucked in."
        sil "I'm sorry, I'm so sorry--"
        show alexia breeding happy behind black
        al "It's fine."
        "She laughed, her throat still scratchy from the sudden intake of water. She was soaked through but didn't mind, the feel of being in Sil's arms easing any of her anxiety away."
        "Sil brushed some of her wet hair from her face, his expression soft. He kissed her again, and this time she felt his excitement hard against her leg."
        "Desire swelled in her lower abdomen. Her legs parted instinctively, wrapping around his waist. Sil's eyes widened in surprise but he didn't object."
        "Sil moved through the water with ease, carefully pressing her against the wall of glass. She gripped the edge of the tank to keep herself up, but it took little effort with the buoyancy of the water." 
        "Sil helped tug at her uniform and the heavy fabric floated down to the bottom of the tank. Alexia took in a deep breath, the sensation of the cool glass against her bare breasts sending a pleasant thrill through her body."
        "She could feel his cock hard between her legs, easing upward slowly until the tip pressed against her entrance. He paused, unsure."
        "Alexia smiled back at him with encouragement, her own need to be filled up by him nagging at her."
        show alexia necklace naked aroused behind black
        al "Go ahead, Sil. Fuck me. {i}Please{/i}."
        "She squirmed against him, pressing her ass against his groin for emphasis. Sil moaned, his hands finding their way to her hips before he thrust upward into her."
        "Alexia gasped, surprised to feel his full length shove inside of her. For as gentle as Sil was, she expected him to at least work up to it." 
        "The sensation wasn't unpleasant, though-- quite the opposite-- and it only took a few moments for the pain to subside into a more pleasurable feeling."
        "Sil stopped and Alexia whimpered, begging for more."
        al "Don't stop now! Please, Sil, keep going!"
        "The Silquien obliged, his hips jerking back and forth as he thrust in and out of her open cunt. Alexia panted, her nails scraping against the glass as she worked to keep herself upright."
        "The water and smooth texture of Sil's cock helped him slide in and out of her easily, each thrust emphasizing how well he fit inside of her. Alexia had seen his cock, knew its length, and still he felt bigger inside of her, stretching her walls wide open."
        al "Oohh… Sil… Sil…!"
        "She cried out his name as her own climax built up inside of her, her hips rocking back and forth against him for more, more, more--"
        "A sudden sharp pain pierced into the back of her neck. Alexia cried out, almost losing her grip on the tank as Sil bit and licked at the wound, his sharp teeth piercing against her skin."
        al "Fuck-- Fuck, Sil-- Yes--"
        "Tremors ran through her body as Alexia reached her orgasm, her pussy clenching around his cock tightly." 
        "Sil moaned in her ear from behind before blowing his own load inside of her. The excess cum dripped out and floated through the water."
        "Alexia touched the back of her neck, surprised to find the sharp indents of where his teeth had been in her skin. It was the last thing she expected from Sil of all people, but the passion and need he displayed was enough to push her over the edge."
        "She smiled a little to herself and maneuvered herself around in his arms to face him. Sil petted her hair gently and held her in his arms, the flaps folding around her like a cool blankets."
        "After a few minutes like that, embraced in each other's arms, Sil finally pulled away and fetched her gown. Alexia pulled it back on, only then realizing how miserable it would be to wear a drenched uniform around the drafty castle."
        "Picking up her books, Alexia reluctantly bid Sil farewell and, with the promise of more lessons tomorrow, finished up the rest of her shift."
        "She tried not to think about the fact that Gnash still intended to auction him off and that this may have been her last time with Sil."
        return
        
    "Tell him what a great friend he makes.":
        $ released_fix_rollback()
        show alexia breeding shocked at midleft with dissolve
        "Alexia stared back at him, momentarily speechless. She was not prepared for something like this."
        if all_actors["alexia"].relation > 40:
            "She was married, first of all. Rowan was her husband, although Sil didn't know that. It had never come up in their conversations."
        "Sil was… He wasn't even human. He was intelligent, yes, but he was a creature in the breeding pits." 
        "Did he even know what love was, or was he just repeating something they'd gone over in one of their books? Had they ever gone over this topic?"
        show alexia breeding neutral at midleft with dissolve
        "Alexia felt all out of sorts as she gathered up her books and pulled away. She needed space, some time to think. She couldn't do that here, not with Sil."
        al "I have to be going now."
        "She climbed down the ladder, afraid to meet his gaze. Out of the corner of her eye she could see him swimming down in his tank to reach her height with each step, his eyes wide and pleading." 
        show alexia breeding happy at midleft with dissolve
        "She couldn't leave him wondering if he'd done something wrong, so she smiled at him quickly, hoping to ease some of the tension."
        al "I'll see you again tomorrow for our lessons. Be good, Sil."
        hide alexia with moveoutright
        "Sil opened his mouth to call after her, but Alexia rushed from his cage, from the pits, as far as she could away from Sil."
        "She didn't even stop to wonder if he would even still be there tomorrow."
        return
        
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

label a_silquien_auction:

scene bg25 with fade
show alexia breeding neutral at midleft with dissolve

"Alexia sighed heavily as she finished substituting fresh hay in one of the cages of the breeding pits. What was usually easy monotonous work became a true chore in recent days."
"How was she supposed to focus when her favorite charge was going to be sold off like a piece of meat?"
"Gnash's plans to auction Sil off had been weighing down on her mind. Work became more difficult to complete when she knew every second spent scrubbing out cages was another second away from Sil."
"Supposedly Gnash had been busy bidding Sil's freedom to multiple sellers, all of whom were eager to get their hands on a creature as intelligent as Sil. The thought left Alexia feeling sick. It was only a matter of time before a final bid was placed."
"Alexia finished scrubbing her last cage of the day before making her way to Draith's office." 
"Draith sat at his desk, a pouty expression on his ashen face as he filled out paperwork. Alexia knew he would rather be wandering the pits and caring for the creatures firsthand, but certain duties had to be completed."

al "Draith, do you have a minute?"

show draith happy at midright with dissolve

dra "Of course!"

"Relief washed over his face. Draith smiled, gesturing for Alexia to enter. She did so, gently shutting the door behind her."

dra "What can I do for you, Alexia?"

al "Have you heard about what Gnash is up to? With Sil?"

"Draith's face fell. He sighed, nodding."

show draith neutral at midright with dissolve

dra "I have. He won't stop talking about it."
dra "I'm sorry for all the stress he's put on you. He's been pretty rash about things since Andras sent him over here."

"Draith's lips curled in distaste and he tapped his fingers against the tabletop in irritation. It appeared that Alexia wasn't the only one having troubles with the new assistant beast master."

dra "The boar could use a good kick in the head. Do you know what he tried to do yesterday?"

#draith angry

"Anger flared in Draith's eyes and Alexia shook her head. She had been so focused on Sil's inevitable departure that she had trouble remembering much of anything that happened on her shift yesterday."

dra "This {i}barbarian{/i} thought it would be a {i}brilliant{/i} idea to put the female Loricians in with the males. Can you believe it?"

"Draith shook his head in disgust."
"Alexia only had a vague idea of which creatures he was currently upset about-- there were so many Draith talked about that sometimes she just simply lost track-- but she understood the gist of his anger."

al "That's terrible."

dra "It was genocide! I had to pry the females off before they slaughtered every last male available. Those poor Loricians didn't stand a chance…"

show alexia breeding concerned at midleft with dissolve

#draith sad

"A shadow of mourning passed Draith's face and Alexia felt for him. He cared about these beasts like they were his children, and to see their deaths surely hurt him deeper than the mistake itself."

al "I'm so sorry."

dra "That idiot. If I could have, I would have fed him to the Loricians himself."

show alexia breeding neutral at midleft with dissolve

al "We may not be able to do anything about the Loricians… but we can do something for Sil, can't we?"
al "You can't let him sell Sil, Draith. You know he won't care who Sil goes to; it's inhumane!"

#draith neutral

"Draith rubbed his tired face, and Alexia could see that his time working with Gnash had exhausted him more than she realized. Draith appeared to be at his wit's end."

dra "I know, I know."

show draith happy at midright with dissolve

"He pursed his lips in thought. He suddenly looked up at Alexia, his eyes bright and cheerful with a new idea."

dra "You know, we could always kill him! That's how things were done among the dark elves."

"Draith beamed at her, his smile full of humour."

al "You aren't serious?"

dra "No, but it is tempting, is it not?"

"Alexia sighed. Perhaps it was more tempting than she wanted to admit, but she could never be the kind of person to take someone else's life. No, killing the orc would not be an option, and it was not one either of them took seriously."
"The door swung open then, interrupting their conversation. Alexia didn't bother to hide the sneer on her face as Gnash came trudging in."

show orc soldier neutral at edgeright with moveinright
show alexia breeding concerned at midleft with dissolve
show draith neutral at midright with dissolve

"Draith's smile dropped and he regarded the grinning orc with a raised brow. Alexia blanched, already knowing what the orc's smug expression meant."

dra "Can I help you, Gnash?"

gnash "Got a buyer ready. Need ya to prep the monster."

"Her heart plummeted. Yes, this was exactly what she feared. Alexia hadn't even been able to see Sil today, let alone talk to him, and now suddenly he was going to be shipped off to some stranger."
"Draith and Alexia shared a look, a grim mutual understanding passing between them."

dra "I see. When is the buyer arriving?"

gnash "On his way now."

al "Now? Can't you tell them to come later? Tomorrow, or next week?"

"There was a hint of desperation in Alexia's voice as she objected. She glanced at Draith, hoping he would interject and find some excuse to stop this. But the dark elf seemed to be at a loss."

gnash "Buyer's only here today. He'll be here in an hour."
gnash "Make sure the beast's ready."

hide orc soldier with moveoutright

"Alexia winced as Gnash slammed the door on his way out."

scene black with fade

"….."

scene bg25 with fade
show alexia breeding concerned at midleft with dissolve
show draith neutral at midright with dissolve

"Sil knew something was up the minute she and Draith arrived at his tank."
"Alexia felt sick, her eyes stinging as she assisted Draith in cleaning the tank and helping Sil look presentable-- as presentable as any Silquien could, anyway."
"Sil watched her with wide sad eyes, barely registering Draith's presence. The way he stared at her broke her heart; like a lover being left behind."

sil "Alexia…"

"She looked up, surprised to find Sil's blurry hand reaching to wipe the tears from her face. She inclined her cheek into his palm, no longer as comforted by his hand when she knew it would inevitably be torn from her face when Gnash arrived."

sil "Am I leaving now?"

al "I--"

"{i}Yes, Sil. You're being sold{/i}. That's what she was supposed to say, but Alexia couldn't get the words out."

al "Isn't there anything we can do, Draith?"

dra "I've been trying to think of something, but…"

al "What if we hide him? Gnash can't auction him off if Sil isn't there."

"It was a silly, ridiculous idea-- something she had just blurted out in a weak grasp for control over this spiralling situation-- so it came as a surprise to her when Draith seriously considered her idea."

dra "That's not bad. If the buyers arrive and there's no Silquien here at all, they may even think Gnash is lying. It could ruin his reputation among potential buyers in the future as well."
dra "What do you say, Alexia? Shall we hide him?"

menu:
    "Hide Sil.":
        $ released_fix_rollback()
        show alexia breeding happy at midleft with dissolve
        "Hope soared through her. If there was any chance of saving Sil from being sold off, this was it."
        al "Yes, let's hide him."
        al "Are you okay with that, Sil?"
        sil "If it means I get to stay with you, of course I'm okay with it."
        "Spurred on by his touching words, Alexia climbed the ladder and helped Sil out of the tank. Draith reached out as well and together the pair did their best to lower Sil to the ground."
        al "Is he going to have trouble breathing out of the water?"
        dra "He'll be fine; Silquiens have evolved for land and sea, although walking on land is-- so I've heard-- very uncomfortable for them for the first hour or so. Look, his legs are already coming out."
        al "Legs--? Oh!"
        show alexia breeding shocked at midleft with dissolve
        "Alexia cried out in shock as she watched two legs extend from his hips. She nearly dropped him but Sil caught himself, his webbed feet landing with a wet smack on the stone floor."
        al "I-I didn't-- I had no idea you could do that!"
        "Sil looked at her shyly, an embarrassed smile on his face."
        sil "I thought you liked me better without them."
        show alexia breeding happy at midleft with dissolve
        al "...Oh. No, Sil. That isn't the case at all. I think you look lovely no matter what."
        "Although he didn't blush, Sil suddenly became flustered, wringing his hands together nervously as he stared down at the floor."
        "Draith cleared his throat from behind."
        show draith happy at midright with dissolve
        dra "If you're done flirting, we are supposed to, you know, {i}hide{/i} him…"
        al "Yes, of course!"
        "Alexia and Draith led Sil to the corner of the cage where several feeding and general supplies are kept to take care of the Silquien and his tank. Sil maneuvered himself between the supplies, crouching down and disguising himself underneath a tarp." 
        "It was not the most original hiding spot, but in a pinch, Alexia and Draith found it worked fine."
        show orc soldier neutral at edgeright with moveinright
        show draith neutral at midright with dissolve
        show alexia breeding neutral at midleft with dissolve
        "Gnash entered the cage a few minutes later, inspecting the clean tank with a sharp eye. Of course, Sil was nowhere to be seen."
        "Gnash approached the tank and banged a heavy fist against the glass. The water sloshed inside, some spilling out over the edge, but Gnash didn't seem to care."
        gnash "Ay! Beast! Come out!"
        "He squinted and peered into the cracks of coral, searching for the Silquien. When Sil did not appear, he rounded on Alexia and Draith, his large hands balled into tight fists."
        gnash "Where is he?!"
        al "I don't know what you mean."
        "Gnash glared between the two, his temper rising. He was silent for a moment, the wheels slowly turning in his head, before a new idea struck him."
        gnash "Yer hiding him. Ya plan to sell him for yerselves, don't'cha?!"
        show alexia breeding shocked at midleft with dissolve
        "Before Alexia could object, the orc grabbed her by the hair and dragged her toward the tank. She shrieked and pried at his hand, but Gnash's grip was firm."
        gnash "If ya won't tell me where he is, I might just sell ya instead."
        "Gnash yanked on her hair again, nearly lifting Alexia off of her feet."
        #draith angry
        dra "Gnash, put her down {i}now{/i}!"
        "The orc ignored Draith, a malicious grin on his face as he held Alexia in front of him. She realized with an ounce of fear that he could crush her head between his palms if he wanted to."
        "And it definitely looked like he wanted to. Or worse."
        "A rustling caught her attention, but Gnash seemed oblivious to the noise."
        "Alexia's eyes widened as she watched Sil spring out from his hiding place. She opened her mouth, the {i}No{/i} already formed on her lips, but Sil dove onto the orc from behind and knocked him down. Alexia stumbled out of his grip, barely catching herself on one of the ladder's steps."

    "Don't hide Sil.":
        $ released_fix_rollback()
        "Alexia considered it, her chest aching with longing at the idea, but deep down she knew it would be ridiculous. There weren't many places to hide Sil in the breeding pits in the first place, let alone the ability to hide him somewhere on such short notice."
        "She shook her head, defeated."
        al "...No. Gnash isn't that stupid, he'll find him in no time."
        "Draith gave her a surprised look but didn't object, climbing back down from the ladder and placing the cleaning supplies away. Alexia could feel Sil watching her with growing anxiety, but she couldn't bring herself to meet his gaze."
        show orc soldier neutral at edgeright with moveinright
        "Gnash trudged into the cage a few minutes later, his eyes full of greed as he took in Sil's cleaned tank."
        gnash "There we go! Buyers'll be here any minute."
        "The orc's expression fell, and Alexia finally dared to look at Sil to see what the problem was. The Silquien moped about his tank, obviously depressed as he moved from side to side."
        "Gnash banged a heavy fist against the glass."
        gnash "Ay! Knock it off! We got buyers comin', they wanna see ya smilin'!"
        "Sil glared at the orc and made no attempts to adjust his attitude. He flung an obscene gesture at the orc."
        show alexia breeding neutral at midleft with dissolve
        "Alexia raised an eyebrow at Draith, suspicious of where he'd learned that one. {i}She{/i} certainly didn't teach him that. Draith just smiled back at her."
        gnash "Don't have time for this."
        "Gnash grumbled under his breath as he climbed the ladder and reached an arm into the tank. Sil easily dodged his advances, swimming away from the orc's large hand."
        gnash "Get the fuck up here! We're not playin' fuckin' games!"
        "Gnash leaned into the tank more and this time managed to grab Sil by the stunted rod of his tail. Sil gasped as Gnash managed to yank him upward by the rod, pulling him out of the water. Sil's face contorted in pain and he struggled to escape Gnash's grasp."
        show alexia breeding shocked at midleft with dissolve
        "Alexia ran to the edge of the ladder, unsure of what to do but terrified to see Sil being harmed."
        al "Stop it! You're hurting him!"
        gnash "'Is fine!"
        al "He's {i}not{/i}! Let him go!"
        "Gnash ignored her, managing to yank Sil out of the tank. He dropped him onto the floor with a wet {i}smack{/i}, ignoring the height difference between the top of the tank and the floor below."
        "Sil gasped, clutching his arm in pain. Alexia rushed to his side."
        show alexia breeding concerned at midleft with dissolve
        al "Sil, are you okay? Hey, look at me. Can you breathe?"
        "Sil nodded, and Alexia was surprised to see a new change in him: legs began to extend out from his hips, as human as hers aside from his webbed feet. She gawked, unable to take her eyes off of the new limbs."
        show alexia breeding shocked at midleft with dissolve
        "Seeing her surprise, Draith chimed in."
        dra "Oh, I didn't tell you this, did I? Silquiens evolved for land and sea; their legs aren't needed often, but they are there. They can be dreadfully uncomfortable to walk on for the first hour or so, though."
        "Gnash observed this transformation from the ladder, his eyes wide."
        gnash "Why didn't ya tell me he did this shit?"
        #draith angry
        "Draith glared at Gnash through narrowed eyes, pretending to clean his nails."
        dra "You didn't ask."
        "Gnash nearly broke the ladder with his heavy footsteps, his feet slapping hard against the ground as he towered over Sil."
        gnash "Shit! This beast's gonna make us rich."
        "He grabbed the Silquien by the hair and raised him to eye level. Sil glared back at him, no longer defenseless with his newfound legs."
        
al "Sil--"

"Her warning died in her throat. Sil did not look like the sweet, nervous Silquien she knew; he was, in every sense, a {i}beast{/i}."
"Sil's sharp teeth protruded from his gums as he bit hard on Gnash's neck. The orc yelled and Sil yanked his head back, easily tearing the flesh open." 
"Alexia didn't even see the claws protruding from Sil's fingers until they were deep on the other side of Gnash's neck, thick blood pooling out from his side."
"Alexia gawked, unable to tear her eyes away from the scene. Sil, her sweet Sil, was shredding the flesh on Gnash's neck, ignoring the punches and scratches the orc returned in retaliation." 

hide orc soldier with redflash

"Then the struggling stopped. Gnash landed on the floor in a pool of his own blood, his thick skull practically severed from his body. Blood dripped from Sil's mouth and claws."
"The Silquien stood on shaky legs, refusing to meet Alexia's gaze. Draith appraised Sil with an approving gleam in his eyes."

dra "...Well! That settles that, don't you think?"

"Alexia didn't know what to say. It was all over and done with so quickly. She just stood there, mouth agape, processing."

dra "Alexia?"

al "Ah, um, yes?"

dra "I'll take care of the body, so how about you help Sil clean up in my office? There should be some bandages in there."        

al "Sure."

scene bg25 with fade
show alexia breeding neutral at midleft with moveinleft

"Alexia took Sil's hand in her own and led him to Draith's office, trying to ignore the feel of warm blood in his palm. They said nothing as they entered Draith's office." 
"Sil took a seat on the edge of the desk while Alexia searched the room for supplies to clean his wounds. Silence stretched between them, deafening."

sil "Are you angry at me?"

al "Huh?"

sil "You seem… angry."

al "No, I'm not angry at you, Sil. I'm… surprised, certainly. But I'm not angry."

"Sil finally met her gaze then, his large eyes wide and doubtful."

sil "You don't hate me then?"

"And there it was, the shy Silquien she had come to know. Alexia's heart melted a little at the sight. Yes, this was her Sil. That hadn't changed."

show alexia breeding happy at midleft with dissolve

al "I could never hate you, Sil. "

"Sil smiled in relief but didn't allow his body to relax entirely. Alexia eventually found the medical supplies and tended to his wounds. The sight of him yanking Gnash's flesh out with his teeth still lingered in the back of her mind."

al "...But I do want to know… Why did you murder him?"

sil "Because I wanted to stay with you."

"He stared at her as if his explanation was obvious."

menu:
    "Disapprove of his murdering Gnash.":
        $ released_fix_rollback()
        show alexia breeding neutral at midleft with dissolve
        al "I… Even so, you shouldn't have murdered him, Sil. That's wrong."
        "Sil frowned, and Alexia could see there was a flicker of confusion on his face although he tried to hide it."
        sil "I thought you didn't like Gnash."
        al "I don't-- didn't-- but we can't solve every problem with murder. Promise me you won't do something like that again."
        "Sil bowed his head in shame, clearly wishing this conversation had taken a different turn. He nodded solemnly."
        sil "I promise."
        show alexia breeding happy at midleft with dissolve
        al "Good. Now let's get you cleaned up."
        "Sil seemed to soften as Alexia continued bandaging him up." 
        "She still wasn't comfortable with his methods of getting rid of Gnash, but she would be kidding herself if she said she wasn't happy that she got to stay with Sil now."
        return
        
    "Show your appreciation.":
        $ released_fix_rollback()
        if silFavour > 3:
            "How could she be angry at him if he was so desperate to stay by her side? Alexia couldn't bring herself to explain the intricacies of murder tonight, not when he'd risked his life for her."
            "Alexia ran her hands over his thighs, surprised by just how smooth his skin was." 
            al "I want to stay with you too, Sil. You mean so much to me."
            "She leaned forward, her voice taking on a more sultry tone as she ran a finger down his chest."
            al "Let me show you how much you mean to me."
            #cg 1
            scene black with fade
            show alexia breeding aroused behind black
            "Sil smiled softly, his fingers reaching out to stroke through her hair. Alexia sighed in contentment, savoring the feel of his touch."
            "She reached down and peeled her panties off, the fabric already damp with her own excitement. Sil licked his lips and Alexia watched as his arousal hardened in front of her."
            "Alexia climbed onto his lap, straddling him, and ground against his erection. Sil held her waist, his breath coming out heavier with each roll of her hips."
            "Her cunt was already dripping when she reached down and slid him inside of her. Alexia whimpered as he thrust inside of her at once, pushing the full length of himself as far as her pussy would allow."
            al "You don't waste any time, do you?"
            "Her laugh came out breathy and receded into a moan as Sil dragged himself in and out of her, lifting her up and down on his cock in a quick, steady motion."
            "Alexia's fingers dug into his shoulders, the tip of his cock pressing deep inside her waiting cunt. She could already feel her climax approaching when Sil removed one hand from her waist."
            "She gasped as he stuck a finger in her asshole, then two, curling them in and out of her in tandem with the motion of his cock."
            "Her thighs clenched. Oh fuck, she felt {i}good{/i}. Everything about Sil was smooth and slippery and so easy to slide and stretch inside of her, morphing her body to his pleasure with ease. She didn't even need to worry about lubrication when his body naturally provided it."
            "Alexia's moans turned to quick pants as she reached her orgasm, her nails clawing into his back as violent tremors shook her body."
            "Sil didn't stop, his movements only growing more fervent with his own growing climax. It was so easy for her to give into him, to let him fuck, fuck, fuck her until he came."
            "And came he did. Sil's choked out a gasp as his cum shot out deep into her pussy. He clutched Alexia tightly to him, their bodies rubbing until he was finished."
            scene bg25 with fade
            show draith happy at midleft with dissolve
            show alexia breeding aroused at midright with dissolve
            dra "...I see my desk was put to good use."
            "Heat rushed to Alexia's face as she finally noticed Draith standing in the doorway. He raised an amused eyebrow at them, and Alexia could see him admiring Sil's masculine features."
            "Despite her shaky legs, Alexia climbed off of Sil and yanked on her uniform. Draith held up a hand."
            dra "No need to rush on my account. I'll come back later."
            dra "Make sure to clean up when you're done!"
            "He winked at them before stepping out of the office and shutting the door in his wake."
            return
        else:
            "How could she be angry at him if he was so desperate to stay by her side? Alexia couldn't bring herself to explain the intricacies of murder tonight, not when he'd risked his life for her."
            al "Well, thank you. I'm happy we get to be together."
            "Sil beamed, her words putting him in a better mood."
            "Alexia dug around the office a little bit until she came across some extra treats. She gave them to Sil as a reward."
            al "Don't eat them all at once. I don't want you to get sick."
            "Sil grinned and nodded, munching on the snacks while she finished bandaging him up. At least she wouldn't have to worry about him being sold off anymore."
            return
            
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

label biting_to_court:

scene bg25 with fade
show alexia breeding happy at midleft with dissolve

"Sil was certainly the smartest beast she'd ever encountered, but there was still so much for him to learn about her world."
"Today, that was mating."
"Alexia was sure Sil knew what mating was-- or at least the basic concept, he was a beast after all-- so she focused her efforts on the more social aspects, such as manners and dress."
"Sil rested his head in his arms on the ledge of the tank, his face pinched in concentration and confusion as he watched Alexia read another passage from her book." 
"It was not one of their usual textbooks, but some kind of guide to etiquette and romance she had found abandoned in a dusty corner of the library."
"It had been exactly what she was looking for."
"Well, for the most part. She doubted Sil would need to know the finer details of salad forks or the different meanings of a lady fanning herself, but there were some basic manners and courtesies the book covered that, if Sil were ever to enter into basic society, he would need."

al "--And, last but certainly not least, it is expected of a gentleman to ensure his host or hostess is shown gratitude and respect for the invitation into their household."

sil "Your kind have so many rules."

"Sil pouted and Alexia laughed softly, nodding in agreement."

al "And that's only in the second chapter. Just wait; we haven't even reached the rules of courtship yet."

"Sil looked even more confused, his tail swishing back and forth in the water with wary curiosity."

sil "What is courtship?"

al "Ah-- Well, you know. Dating. It's usually the step before marriage or intercourse."

if silFavour > 3:
    "{i}Usually{/i}, Alexia had emphasized, easily recalling the feel of the Silquien's cock thrusting within her. Such traditions had been abandoned between them and, while she hadn't been considered in the moment, now she wondered if Sil regretted missing out on such things." 
    
sil "Hm."

"Sil hummed in response, his face tense with concentration. Alexia tried to guess what was going on in that strange head of his and failed."

al "What are you thinking about?"

sil "Courting. You humans have so many rules already. I think you complicate it too much."

"Alexia smiled wryly. The Silquien had a point, even if she felt some of those complications were justified."

al "Well, we have a tendency to do that. Things are not so black and white, though, whether we like it or not…"

"Sil stared at her blankly. Even with his displayed intelligence, she couldn't expect him to understand everything she did. Sometimes she didn't even fully comprehend everything going on."

al "Forget it. It's not something you will need to worry about, I'm sure. Silquiens just mate, after all--"

sil "We have courtship."

show alexia breeding shocked at midleft with dissolve

al "What?"

"Alexia stared at him in shock. Sil hesitated, and Alexia was familiar with the tension on his face that told her he was struggling to find the right words. Communication may have been easy between them, but that did not mean words themselves were as kind."

sil "It's not like what you humans have, I think. We select a mate and make it known they are ours."

show alexia breeding neutral at midleft with dissolve

al "That's… Well, I suppose that's sort of courtship. Humans have a lot more put into it…"

"Sil sighed, exasperated."

sil "Overcomplicating things again."

show alexia breeding happy at midleft with dissolve

"Alexia chuckled. Oh, if only he knew just how complicated her situation was. That was not something she was ready to divulge with him yet, though, so Alexia attempted to keep their topic light."

al "What do Silquiens do for courting?"

sil "We bite."

"He flashed his sharp teeth with a smile. His eyes fell on her neck, as if he would leap forward and sink his teeth into her soft flesh now if she gave him the chance."

if silFavour > 3:
    "Alexia touched the back of her neck, her mind immediately snapping back to the puncture of his teeth against her skin during intercourse. A rush of heat colored her cheeks."
    al "You… bite? Why?"
    sil "There is… I can't think of the word… But we have something here--"
    "Sil tapped the points of his teeth."
    sil "--that releases a scent, so we know when someone is mated and should leave them alone."
    "Alexia paused, her fingers brushing over the small indents his teeth left. They were hardly noticeable now, fading away into a light scar that would disappear entirely with time, but in that moment, she felt as though it were visible to anyone within a ten mile radius."
    al "So you would say we're already courting?"
    "Sil nodded, obviously pleased that Alexia had picked up on this so quickly. She wasn't sure how to feel about that." 
    show alexia breeding aroused at midleft with dissolve
    "On one hand, Alexia felt embarrassed-- even ashamed-- to be sporting such an obvious mark of claim on her neck. On the other hand, this was Sil, and the idea that he had even {i}claimed{/i} her in such a way sent an excited thrill through her body."
    if all_actors["alexia"].relation > 40:
        "But she had a husband. A husband that Sil still knew nothing about. And now she suddenly hoped he would {i}never{/i} find out about it."
    "Sil didn't seem to notice her internal debate, his smile wide and eyes full of pride as he confirmed her suspicions."
    sil "We are. I thought you knew about it already, but that's okay!"
    sil "I'm just happy to be so close to you, Alexia."
    show alexia breeding happy at midleft with dissolve
    "Sil reached forward and cupped her face in his palms. Alexia couldn't help leaning into his touch, too easily comforted by him; his face, his lips, his hands, anything that touched her and reminded her that everything would be okay."
    "Sil's thinking was so much simpler than Alexia's. Sil didn't need to worry about jealousy if other Silquiens didn't bother going after each other's mates. He didn't need to think about social etiquette, or long courtships, or even the ins and outs of marriage complications."
    "If only she could have been so lucky."
    "Still, seeing the smile on Sil's face, the knowledge that in some way she was {i}his{/i}…"
    "She didn't have the words to describe her happiness."
    al "And I'm happy to be yours, Sil."
    "The Silquien beamed and pressed a kiss to her cheeks. Alexia giggled, and Sil pressed more kisses around her face, relishing in her laughter." 
    "Then, suddenly, he pulled away."
    show alexia breeding shocked at midleft with dissolve
    "Alexia blinked, startled and sure she had somehow done something wrong, but Sil stared at her with a burning curiosity that killed the settling doubt in her mind."

else:
    "Alexia stared at the pointed rows of teeth behind his lips and swallowed hard. She couldn't imagine them piercing her skin, claiming her as his." 
    "She enjoyed Sil's company of course, but their friendship wasn't something she wanted to get more out of. Alexia was quite happy where they were."
    "But she wasn't oblivious; Alexia saw the longing in Sil's eyes, the way his gaze would flicker to her lips and sometimes lower. She saw the desire there, the want and the need to turn their friendship into something more." 
    "Sil had not pushed on the subject since he first confessed his love, but didn't mean his emotions had gone away. He had simply tried to keep them hidden the best he could with what little skill he had in deception." 
    "Not today, however. Alexia saw a change in his expression, a new wave of confidence in the usually timid Silquien. She could already guess what he was going to say before the words came tumbling out of his mouth."
    sil "Do you think I could court you, Alexia?"
    "Sil stared at her with wide, pleading eyes. She saw the look he gave the exposed flesh on her neck, his desire to sink his teeth into her and claim her as his written clearly on his face."
    menu:
        "Let him court you.":
            $ released_fix_rollback()
            "Alexia bit her lip, struggling to find the words to deny him." 
            "Then, she realized she didn't want to."
            "Maybe it was her buoyant mood with him or something in the air. Maybe it was her desire for Sil's arms around her or the charming, childish smile he made that sometimes melted her heart."
            "Or maybe she liked him all along and kept trying to find excuses to avoid dealing with her feelings about the subject. About him. But as soon as he asked that question, it felt like something clicked."
            "Sil was right; humans were very, very complicated."
            al "Yes. I would love for you to court me, Sil."
            "Sil's jaw slacked, and Alexia almost laughed at the obvious shock on his face. Clearly he hadn't expected her to agree after her last rejection."
            "Flustered, Sil pushed himself up onto the tank's ledge and nodded, his eyes locked on her throat. Alexia tilted her head to the side to give him better leverage, closing her eyes."
            "She felt him hesitate at her side. Was he unsure? No, she could feel his breath against her neck, as if he was savoring this closeness between them."
            "Then came the pain."
            show alexia breeding shocked at midleft with dissolve
            "Alexia gasped as Sil sunk his teeth into her neck. It was dizzying, as if he was pushing something inside of her more than his teeth. Her whole body felt warmer, like she had been laid out in the sun."
            "Sil pulled away and Alexia touched the mark, her fingers tracing over the bloody indents. They weren't so deep that they would scar, but it would definitely take a little time for them to heal properly."
            show alexia breeding happy at midleft with dissolve
            "Sil licked the blood from his teeth and lips, his eyes wide and hazy with what Alexia could only believe to be love. She too felt the same."
            al "Was that how you imagined it?"
            "It took a moment for Sil to find his words, still floundering over the fact she had allowed him to claim her at all."
            "Then his eyes widened and a new idea came to his mind."
        
        "Tell him you just want to be friends.":
            $ released_fix_rollback()
            show alexia breeding neutral at midleft with dissolve
            "Alexia bit her lip, struggling to find the words to deny him. She didn't want to hurt his feelings, but she had to make it clear that she only saw him as a friend."
            al "I… don't think that's the best idea, Sil. You're a very good friend to me, and I would hate to ruin that."
            "Hurt flashed across Sil's face and he struggled to reign it in."
            sil "Oh. I see."
            "Sil lowered his head and nodded, more to himself than in agreement. Alexia felt a little bad for him. There weren't any other Silquien around to meet, and she knew the company in the pits usually left something to be desired." 
            "Sil wouldn't be meeting his future mate anytime soon, that much she was sure."
            "So, she didn't complain when Sil sat a little closer to her, or sometimes not-so-accidentally brushed her hand with his. An attachment between them would be natural, but Alexia made sure any chances ended there." 
            "Even if she pitied his situation, she would not lead him on."
            "Alexia stared at his teeth once more, another confirmation to herself that there would be nothing more between them. She could already feel the phantom pain of his teeth latching onto her skin, sinking in and drawing blood. What Sil saw as courtship, Alexia saw as a horror novel's scene come to life."
            "She silently wished whoever earned his affections in the future would have tough skin."
            "Sil cocked his head to the side, and Alexia realized she had been so lost in her own thoughts that she had missed his question entirely."
            al "I'm sorry, Sil. Could you repeat that?"
    
sil "What about humans? What sort of things do you do?"

"Even though he asked her, Sil looked as though he dreaded the coming answer. Perhaps this etiquette book had been more daunting for him than Alexia anticipated. Still, there was something charming about his serious concern, as if he was afraid to misstep with her."

show alexia breeding happy at midleft with dissolve

al "There are lots of things people do for courting ladies: asking the parents' permission, going out to eat together… one of my favorites was always receiving flowers, though."

"Alexia smiled fondly at the memory of Rowan striding up the path to her home, a large bouquet of beautiful lilies and hydrangeas bundled into his fist."

sil "Flowers?"

"The Silquien peered around the contents of his tank: a coral structure, a few smaller fish, lots of sand, but certainly no flowers. Alexia couldn't even imagine what an underwater flower might look like."

al "Yes-- bouquets, usually, but sometimes even a single flower is nice to have."
al "A lot of the men I knew in the village would simply spoil their ladies with gifts when they were courting. Sometimes after, too. It was quite romantic."

"Sil's lips pressed together tightly. He held up a finger, indicating for her to wait, and dove into the tank. Alexia watched him swim around near the bottom, searching for something."
"He popped back up shortly after with a bundle of seaweed drooping in his hand. With his brightest smile, Sil offered it out to her."
"It took all of Alexia's willpower not to laugh. She accepted his makeshift bouquet with a grin, ignoring how gross the slime felt over her fingers."

al "Thank you, Sil. This is beautiful."

"Sil beamed, proud of his work. There were no more distractions as they dove back into his lesson."

return
    
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

label clean_tank_for_happy_silquien:

scene bg25 with fade
show alexia breeding shocked at midleft with dissolve

"When Alexia arrived at Sil's tank for the day, she was aghast by how dirty it had become."
"Had she been ignoring it all this time? Was she really only noticing it for the first time now? She felt a prick of shame stab at her pride. She was usually so dutiful at cleaning up the breeding pits, and here she was letting poor Sil live in squalor."

show alexia breeding neutral at midleft with dissolve

"Sil popped up with a smile over the edge of the tank, but it quickly disappeared when he saw Alexia's stubborn frown."

sil "What's wrong?"

al "Sil, I'll need you to leave the tank today. We have some cleaning to do."

"And so, after helping Sil relocate to a much smaller barrel of water she convinced some of the other staff to fill up and carry in, Alexia got to work."
"Cleaning Sil's tank was not easy by any means-- having to remove all of the water had been a nightmare, not to mention climbing in and standing atop her ladder to scrub every nook and cranny-- but some things had to be done."
"Sil watched her clean from the top of his cramped barrel, both fascinated and confused by her determination to wipe away the familiar grime of his home."

sil "Alexia?"

"Alexia grunted, squished somewhere between the coral structure as she rubbed a particularly obstinate stain on the glass. How had this even managed to collect grime?"

al "Yes, Sil?"

"The question took Alexia by surprise, and after maneuvering herself out from a piece of coral that grabbed at her hair, she found a reasonable answer."

al "Humans don't have to live in tanks, we breathe air."

sil "But I breathe air."

al "But you're used to the ocean, and we're used to land. We want to make you comfortable, so hence, the tank."

"Sil looked as though he wanted to object but kept his mouth shut. {i}Was{/i} his tank comfortable? He had told her as much, but was it only so he wouldn't worry her? Looking around the rest of the pits, she realized she hadn't truly considered if any of the animals were satisfied with their cages."

"Sil was different, though. Sil was sentient and intelligent, so was it okay keeping him in a tank? Did he feel trapped?"
"She was about to ask him, but Sil cut her off with another question. Alexia was secretly grateful for the disruption of her thoughts."

sil "Do you swim?"

al "Recreationally, yes. I used to go swimming quite often as a child."

"She could remember fond summers of diving into cool water to escape the heat, her legs kicking and flailing as she dove in and out of rivers, lakes, oceans, ponds, anything she could slip into. Her excitement for the activity had diminished over time, as most things do."

sil "Would you like to swim in my tank?"

menu:
    "Yes, I'd like to go swimming.":
        $ released_fix_rollback()
        show alexia breeding happy at midleft with dissolve
        "Alexia pressed her lips together, considering. She wasn't exactly prepared for a swim today, but after spending hours cleaning his tank, it might be nice to go for a swim. Especially since the tank would be clean after." 
        "She still had work to do, but maybe she would just stay late today to get it done."
        al "Sure, that sounds like fun. Let's finish cleaning it first, though."
        "Sil nodded and watched eagerly as Alexia finished cleaning his tank. Once she was finished, it took some time to fill back up and adjust to the right temperature before she helped Sil back into the water."
        "He waited patiently at the top of the tank as Alexia lingered on the ladder."
        sil "You are still swimming, aren't you?"
        al "Yes, of course."
        "Slipping out of her uniform, Alexia climbed into the water. It still hadn't fully adjusted to the temperature, and she let out a little yelp at how cold it felt against her toes as she climbed in."
        #cg 1
        scene black with fade
        "Once she was fully submerged though, her body adapted quickly."
        "Sil grinned and, taking her hand in his, led her around the tank. It was different being inside of the glass cage while it was filled with water versus when it was dry; the dull underwater plants and structures looked more vibrant, more alive." 
        "It was interesting swimming beside Sil. Alexia felt clumsy with her long legs kicking and splashing around in between her resurfaces for air and dives back down beside him to explore more of his tank." 
        "She had helped pick out things for the tank, but she never realized how much Sil would take to them; would refer to them as pieces of his home."
        "Seeing the little things Sil got excited about in his tank made her want to take him back out and show him her rooms in the castle, or her home back in the village. She wanted to show him her books, her jewelry, her dresses, her bed." 
        "Alexia wanted to introduce him to that part of her as well."
        "There were more air breaks than Alexia was proud of. Every couple of minutes she lost the strength to hold in her air, especially as they dove deeper toward the sandy floor, and would kick back up for more oxygen. Sil didn't seem to mind, but she felt bad nonetheless."
        "Eventually her limbs felt too weak to carry on, and Sil helped her climb back out of the tank and balance on the ladder as she dressed in her uniform."
        scene bg25 with fade
        show alexia breeding happy at midleft with dissolve
        sil "Thank you for swimming with me, Alexia. I had fun."
        al "I did, too. Maybe you'll come see where I live sometime."
        "Sil's face lit up, although a part of her regretted making the suggestion. She had no idea if she would even be allowed to bring him up there, let alone how long he could go without being in his tank."
        sil "Yes! I would love that!"
        al "Great. I'll see what I can do, then."
        "Alexia smiled at him once more before shakily climbing down the ladder and returning to work."
        return
        
    "No thank you, I'm not prepared.":
        $ released_fix_rollback() 
        show alexia breeding neutral at midleft with dissolve
        "She couldn't deny that the offer was tempting; after spending hours cleaning his tank, Alexia almost felt she deserved a bit of fun and relaxation."
        "But Sil was only one of the creatures she had to care for today, and there was still plenty of work to get done. Not to mention the fact she had nothing to wear, and the idea of working the rest of the day in a wet uniform was less than appealing."
        al "Maybe some other time. I'm not quite prepared for a swim today."
        "Sil nodded, clearly disappointed but understanding. Alexia finished cleaning the tank and helped Sil back into it, spending a few minutes to chat with him before she moved onto her next task for the day."
        return
        




