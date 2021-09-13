init python:
    
    event('arrival_of_the_emmisiaries', triggers="week_end", conditions=('week ==25',), group='ruler_event', run_count=1, priority=pr_story)
    event('paperwork_sabotage', triggers="week_end", conditions=('week >=30', 'castle.buildings["barracks"].troops >= 6',), group='ruler_event', run_count=1, priority=pr_ruler)
    
label arrival_of_the_emmisiaries:

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

"In the warm light of the midafternoon sun, Rowan dozed."
"He rested his elbow on the table and leaned his head against his palm, hoping the extra support would keep him stable as he read through the dreary paperwork. "
"But for some reason today, he just… couldn’t... stay-"

scene black with fade

"His head drooped. His eyelids slid shut. A soothing calm washed over him as Rowan settled into a quiet rest."
"…"
"…"
"{i}Rowan.{/i}"
"{i}They’re here.{/i}" 
"{i}You need to get to the portal.{/i}"
"..."
"{i}Please, wake up.{/i}"

scene bg6 with fade
show rowan necklace shock at edgeleft with dissolve

ro "{i}Guh!{/i}"

show rowan necklace concerned at edgeleft with dissolve

ro "What- who...?"

"Rowan’s head swiveled around the room in confusion. There was no one there. His drowsiness had vanished. He was wide awake, alert and energetic." 
"That voice…"
"Driven by a compulsion he could not explain, Rowan rose from his seat and hurried out the door. "

scene bg10 with fade
show rowan necklace neutral at edgeleft with dissolve

"Rowan stepped into Bloodmeen’s cavernous portal room to the sound of shouting. A dozen Orc guards stood in a semicircle around the entrance of the portal, their weapons drawn."
"There was something standing at the portal." 
"Something big."

show cg857 with fade
pause 3

scene bg10 with fade
show whitescar neutral at center with moveinright
show rowan necklace neutral at edgeleft with dissolve


"Sharp yellow eyes swept the room with a hunter’s calm alertness. His sinewy form and pale, snowlike fur stood resplendent in the indirect glow of the portal behind him."
"Sensing his profound lack of concern for their presence, the phalanx of Orcish guards gave the creature a wide berth." 

ro "What's going on here?"

show orc soldier neutral behind bg10

os "Boss… ‘e just appeared outta {i}nowheres{/i}."

show rowan necklace shock at edgeleft with dissolve

ro "Through the portal?"

os "Y-yeah."

show rowan necklace neutral at edgeleft with dissolve

"The wolf lifted his nose and took a few experimental sniffs of the air. He didn’t seem hostile… yet."

menu:
    "Confront him":
        $ released_fix_rollback()
        "Rowan took a step forward, ignoring the flutter of unease that crept up his spine. There was something unnerving in the beast's eyes, something primal and predatory."
        show rowan necklace angry at edgeleft with dissolve
        ro "Who are you, how did you get in here?"
        "Rowan felt the bottom go out of his stomach as the creature's piercing eyes snapped to him. He resisted the urge to freeze in place."
        whit "{i}Hmmh{/i}."
        whit "Ugly. Worse than I expected."
        ro "Excuse me?"
        whit "Ill omens all around. Stench of fate in the air."
        whit "I do not like it."
        show rowan necklace shock at edgeleft with dissolve
        ro "You don’t like… what?"
        whit "Everything. All of it. You included."
        show rowan necklace angry at edgeleft with dissolve
        whit "This place is wrong. Twisted and gnarled. Like a strangling vine."
        ro "What are you, beast?"
        "A glint of humor grew in the wolf’s eyes."
        whit "Beast, is it?"
        ro "You haven’t given me a name."
        whit "Pointless. My name means nothing to you. You would not know me by its use."
        ro "I might be more inclined to listen to what you have to say, at the very least."
        whit "..."
        whit "Fair."
        $ whitescarName = "Whitescar"
        whit "I am Whitescar. Emissary of the Fae. I have business with your masters."
        "Rowan’s eyebrow twitched. So the dreams were true..."
        show rowan necklace neutral at edgeleft with dissolve
        ro "And what business would that be, Fae?"
        "The wolf’s upper lip curled. He bared his fangs."
        whit "Bring me to them, and you will know of it."
        ro "And if I refuse?"
        "The wolf sneered. His shoulders lowered a half inch as his stance shifted. He flexed his arms casually extending his claws as he stretched."
        whit "It matters not. I will deliver the Queen's message regardless."
        show rowan necklace angry at edgeleft with dissolve
        ro "Bold words."
        whit "Bold words lead to bolder action. You will not deny me my sacred task."
        ro "You’ll die if you try anything."
        whit "A Fae unwilling to die for something is not fit to live in the first place."
        
    "Wait to see what happens.":
        $ released_fix_rollback()
        "Rowan hovered at the edge of the crowd, keeping his distance. Better to observe and see what this creature could do, rather than force a confrontation."
        "The wolf man - by contrast - seemed almost bored. After sizing up the Orcish guards he began to glance about the room."
        whit "{i}Mmmh{/i}, Ugly. Worse than I expected."
        "Silence followed the beast’s statement. His eyes found Rowan, and they narrowed down to slits."
        whit "You. Human."
        "Rowan didn’t respond, cooly meeting his gaze."
        whit "...Can you understand me? Is this not your native tongue?"
        ro "More or less."
        $ whitescarName = "Whitescar"
        whit "Then bring word to the Twins that Whitescar, Emissary of the Fae, is here. I would speak with them."
        "That name… the fox from the dream had mentioned her father. Rowan struggled to keep an empty expression at the news."
        ro "...How did you get in here?"
        whit "That is what I will be discussing with your masters."
        show rowan necklace angry at edgeleft with dissolve
        whit "You will bring me to them."
        ro "I will?"
        whit "Yes."
        ro "You realize whose castle this is."
        whit "The halfbreed spawn of Karnas. Yes."
        "Rowan had to suppress a wry smile at the jab."
        show rowan necklace neutral at edgeleft with dissolve
        ro "You have quite the tongue for an ‘ambassador.’"
        "The Fae’s eyes narrowed. There was the slightest curl of flesh at the base of his snout. Rowan saw the glint of sharp canines."
        whit "If you will not send for them, then I will find them myself."
        ro "You’d face a castle full of soldiers alone?"
        "The Fae let out a low sound, almost like a growl. It took Rowan a moment to realize he was chuckling."
        whit "Your numbers don’t concern me."
        "Rowan tensed. There was a terrifying nonchalance in the threat."
        
show rowan necklace angry at edgeleft with dissolve

"Rowan’s hand drifted unconsciously to the hilt of his sword. The Orcs around him raised their weapons. Whitescar’s brow lowered. Rowan felt a thrill of alarm run up his back."

show bg10 with flash

"Suddenly, there was a flash. A flickering of energy spiked within the portal, and in an instant another figure had appeared."

show cg858 with fade
pause 2
show cg859 with fade
pause 3

scene bg10 with fade
show arzyl neutral at edgeright with dissolve
show whitescar neutral at center with dissolve
show rowan necklace angry at edgeleft with dissolve

arz "Goodness, what a commotion."

"Rowan drew his sword in a blur. Whitescar bared his fangs and let loose an enraged growl."

show rowan necklace shock at edgeleft with dissolve

"To Rowan’s shock, it wasn’t directed at him, but rather towards the tall, statuesque woman who had just materialized out of thin air."

arz "Dearest Whitescar. We’ve only just arrived, and already you’re threatening our hosts!" 

whit "What are {i}you{/i} doing here, witch?"

"The pale, vaguely Elven being smirked."

arz "My, my. Now is that any way to address your fellow Emissary?"

"The wolf rose to his full height, looming over her as if readying to devour her."

whit "The Queen sent me alone to handle this."

arz "-And evidently she was right to second guess her judgement. I have been dispatched to help you."

whit "To hinder and delay me. {i}Leave{/i}."

"The woman merely smiled."

arz "No."

"She forgot him in an instant, turning to face Rowan as if the imminent threat of Whitescar’s rage simply didn’t exist."

$ arzylName = "Arzyl"

arz "Greetings, Rowan Blackwell. I am Arzyl, Lady of the Midnight Court. I do apologize for the abruptness of our arrival."
arz "This uncouth brute standing next to me is Whitescar, Chieftain of the Netherweald. We come as emissaries of Good Queen Kassandra. "

show rowan necklace concerned at edgeleft with dissolve

ro "...You are Fae, as well?"

"Her smile broadened. She fluttered her eyelashes at him. Her voice was low and breathy, as if the two were exchanging pillow talk."

arz "So astute."
arz "We seek an audience with the Twins, if they will deign to see us."

whit "We do not ask. We {i}demand{/i} that you bring us to them."

"Arzyl laughed at Whitescar’s snarling retort."

arz "My companion suffers from a somewhat choleric disposition, as you can see from this latest misunderstanding."
arz "Whitescar, we came here to talk, not do battle."

whit "You shouldn’t {i}be{/i} here at all!"

arz "Shall I leave you to your bumbling, then? You seemed to have the situation well out of hand."

"Rowan looked from Arzyl to Whitescar in puzzlement. The hostility between the two was both immediate and overwhelming."
"Sensing his eyes hovering upon her, Arzyl smoothly refocused her attention on Rowan."

arz "Enough banter. We can save such salacious gossip for later."

"Arzyl bowed her head, exposing the curve of her milky cleavage to Rowan’s viewing as she did so."

arz "Will you grant us the privilege of an audience with the Twins, Rowan?"

show rowan necklace angry at edgeleft with dissolve

"Rowan let out a sigh and fingered the amulet around his neck."

if society_type == "might":
    ro "Lady Jezera, Lord Andras? I need you to come to the Throne room immediately."

else:
    ro "Empress Jezera, Empreror Andras? I need you to come to the Throne room immediately."

show andras displeased behind bg10

an "I’m in the middle of something, servant."

show jezera neutral behind bg10

je "Can’t it wait, Rowan?"

ro "No. It can’t. We have-"

"Rowan almost said “Fae,” but hesitated."

ro "...Guests."

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera neutral at midright with dissolve
show andras displeased at edgeright with dissolve

je "What is the meaning of this intrusion, Rowan?"

ro "Two strangers have arrived through the castle portal. They seek an audience with you."

an "…‘Strangers’?"

ro "They claim to be ambassadors of the Fae."

"The Twins shared a look. Rowan frowned."

show rowan necklace angry at midleft with dissolve

ro "...You two don’t seem all that taken aback."

an "You said you had it handled, sister."

show jezera happy at midright with dissolve

je "And I do, dear brother. Their arrival is surprising, but hardly unexpected."

show rowan necklace concerned at midleft with dissolve

ro "You've met the Fae before?"

je "Once or twice during my research into the leylines."

ro "I thought they were just children’s bedtime stories."

je "Most legends about them are."
je "They are an elusive race, scorning both Solansia and Kharos. For them to appear to us now… we must have done something to draw their attention."

ro "Can they be trusted?"

"Jezera let out a contemptuous laugh."

je "As much as {i}you{/i} can be, Rowan. You may send them in now."

"Rowan let out a dissatisfied grunt and gestured towards the door. The Orcish guards pushed open the heavy doors."

hide rowan with dissolve
hide jezera with dissolve
hide andras with dissolve
show whitescar neutral at edgeleft with dissolve
show arzyl neutral at midleft with dissolve

if society_type == "might":
    arz "Lady Jezera! What a pleasure it is to see you again, my girl."
    
else:
    arz "Empress Jezera! What a pleasure it is to see you again, my girl."

show jezera happy at midright with dissolve

je "The pleasure is all mine, Lady Arzyl. I did not expect to see you here."

if society_type == "might":
    arz "Nor, I my Lady. My recent appointment to this diplomatic mission was a bit… spur of the moment."
    
else:
    arz "Nor, I my Empress. My recent appointment to this diplomatic mission was a bit… spur of the moment."
    
arz "I take it this handsome fellow is your oft-mentioned twin?"

show andras happy at edgeright with dissolve

if society_type == "might":
    an "That's right. Lord Andras."

else:
    an "That's right. Emperor Andras."

"Arzyl fluttered her eyelashes at the both of them."

arz "Charmed, my Lord. Allow us to introduce ourselves-"

whit "{i}Enough{/i}! Enough honeyed words. "
whit "You, Children of Karnas: you abuse the ancient leylines. You corrupt the Netherweald. This will stop. Immediately."

show jezera displeased at midright with dissolve
show andras displeased at edgeright with dissolve

an "Come again, beast?"

arz "What my- {i}exorbitantly{/i} blunt companion is trying to say, is-"

"The white wolf cut her off with a heated snarl."

whit "Do not interrupt me, witch."
whit "Queen Kassandra is kind. Too kind. You abuse her mercy. You ignore our warnings."
whit "This will not continue. The magic of the leylines are not yours to tamper with."

show andras angry at edgeright with dissolve

an "You dare to tell me what to do in {i}my{/i} castle, beast?"

whit "Your reckless meddling ranges far beyond these walls. I scold you as I would any wayward cub."

je "Lady Arzyl, what is the meaning of this?"

"The Fae woman flashed a contemptuous smile. She lifted her hand up and cast it about in a lazy circle."

arz "You must forgive the Chieftain. He bears a certain distaste for the...  {i}nuances{/i} of negotiation. Hence, my presence."

show jezera neutral at midright with dissolve

arz "Queen Kassandra has taken a keen interest regarding your recent activity in the mortal realms."

show andras displeased at edgeright with dissolve

arz "Raeve Keep was quite the prize, was it not?"

show andras happy at edgeright with dissolve

an "It was a great victory. The first of many."

arz "Be that as it may, the Queen has grown concerned about the extra strain it’s put on the magic of the leylines."
arz "We wish to find a compromise."

whit "You tamper with powers you don’t understand."

show jezera displeased at midright with dissolve

je "Oh, I understand this power perfectly well, Chieftain."

show jezera neutral at midright with dissolve

je "You want us to stop? I can save you both a lengthy audience. Here is your answer:"

show jezera happy at midright with dissolve

je "No. We won’t. We will continue to use the leylines as we see fit."

show andras displeased at edgeright with dissolve

an "Now scurry back the way you came beast, and be grateful I’m in a forgiving mood today."

whit "{i}Ash’a Vess{/i}!"

"Whitescar let out a roar that shook the room. Before anyone could respond he’d leapt to the base of the Twins’ throne and ascended the steps in rapid succession."

show jezera displeased at midright with dissolve
show andras angry at edgeright with dissolve

whit "Doe-eyed fools. You nibble at the world’s foundation like termites. Heedless. Impulsive."
whit "You would undo the work of a millennia. For what? Fleeting vainglory. Childish ambition. "

an "Take one more step up that stair, beast, and I’ll have your pelt for a rug."

"Rowan tensed. The mood turned deadly serious. Even Jezera had dropped her usual, mocking smile."
"Whitescar was terrifyingly close to triggering a violent confrontation. Judging from the self-satisfied smirk on Arzyl’s face, she seemed more than happy to let him do so."

menu:
    "Intervene on the Fae’s behalf.":
        $ released_fix_rollback()
        show rowan necklace neutral behind bg6
        ro "Might I interject?"
        je "...Speak, hero."
        show rowan necklace angry behind bg6
        ro "This audience has gotten off on the wrong foot."
        an "What was your first clue, fool?"
        ro "From what little I know of the Fae, they are not the type to initiate contact, and they are quite evidently skilled in magic."
        "{i}And in dreamwalking{/i}. He added, thinking ruefully of the white fox."
        show rowan necklace neutral behind bg6
        ro "Frankly, we don’t have the luxury of dismissing them outright."
        "Jezera’s eyes never left Whitescar’s face."
        je "Oh, I think we do. Especially when they’re as rude as this."
        show rowan necklace angry behind bg6
        ro "With all due respect, Jezera, we are attempting to conquer a {i}continent{/i}. Every choice we make affects the challenge of this task."
        show rowan necklace neutral behind bg6
        ro "You yourself said that the Fae shun both Kharos and Solansia. Having an ally whose interests align with ours is far more useful in the long run."
        ro "Why add a new enemy to such a long list, already?"
        show jezera neutral at midright with dissolve
        je "We are not the ones threatening the Fae in their own throne room."
        ro "No. But they wouldn’t have come here asking for an audience without cause. It’s obvious that they are looking for a compromise."
        "Andras glared at Whitescar. The two alpha males stared each other down."
        an "Could have fooled me."
        "The Twins were wavering. Rowan rounded on the Fae ambassador."
        show rowan necklace angry behind bg6
        ro "Chieftain, your passion in this matter is obvious. But is this really the way you plan to go about convincing us to stop?"
        ro "You entered the Twin’s domain and immediately began making demands, with nothing to offer us in return but vague threats."
        show rowan necklace concerned behind bg6
        ro "How do you {i}expect{/i} us to respond?"
        whit "The Fae should not have to beg and scrape to preserve their way of life."
        show rowan necklace neutral behind bg6
        ro "Yet… here you are."
        ro "If you had the power to force us to stop you’d have done so already, not sent a diplomatic mission to issue a protest."
        ro "“What should be” isn’t what is at stake here."
        "Whitescar fell silent. Rowan saw his opening and pressed the advantage."
        ro "Perhaps with time we can come to understand your position better. Don’t let your pride blind you to your ultimate goal."
        "Whitescar glared from the Twins, to Rowan, to a profoundly amused looking Arzyl. After a long moment he let out a dissatisfied huff, retracting his claws."
        whit "The mortal speaks sense."
        whit "So be it. My words were poor. I chose them out of anger."
        whit "...Forgive my outburst."
        show andras displeased at edgeright with dissolve
        "The apology came through gritted teeth, but it seemed genuine enough."
        ro "Maybe we should adjourn for now, and speak about this again when tempers have cooled?"
        "Arzyl’s eyes gleamed with interest as they stared directly at Rowan."
        arz "I think that would be for the best, yes."
        je "Very well. We will have rooms made ready for you to stay in, as our ‘honoured’ guests. Rowan will see to the arrangements."
        whit "I want to be as far away from that witch as possible."
        arz "Goodness, Whitescar, you’ll break my tender heart!"
        show rowan necklace concerned behind bg6
        ro "Separate rooms it is. I’ll see to it at once."
        show jezera happy at midright with dissolve
        je "One moment, hero. We wish to speak with you alone first."
        hide whitescar with moveoutleft
        hide arzyl with moveoutleft
        hide rowan
        show rowan necklace neutral at midleft with dissolve
        "Rowan stood still as stone as the two Fae shuffled past him. Whitescar did not do much as glance in his direction. Arzyl shot him a subtle wink as she passed."
        "The door closed behind the Fae with a resounding {i}thud{/i}."
        show jezera neutral at midright with dissolve
        je "Well, that was an interesting exchange."
        an "That wolf needs to learn some respect."
        show jezera happy at midright with dissolve
        je "Come now, brother. Did you really expect beings as wild as the Fae to adhere to proper etiquette?"
        an "He’s lucky I didn’t skin him."
        show jezera displeased at midright with dissolve
        je "There’ll be time enough for that one day, I’m sure."
        show jezera happy at midright with dissolve
        "Jezera turned to face Rowan, a knowing smile on her face."
        je "Well done, hero. You managed to deflect Whitescar’s anger, and bought us precious time to prepare."
        show rowan necklace shock at midleft with dissolve
        ro "What are you talking about?"
        je "We have been aware of the Fae and their connection to the leylines for some time now."
        show jezera neutral at midright with dissolve
        je "Obviously, since they have access to the portal network, they are a threat to our new dominion."
        je "We have plans in motion for neutralizing them. But for now - as you so rightly pointed out - they are a secondary concern."
        show rowan necklace angry at midleft with dissolve
        ro "Then these negotiations were just a ruse."
        show jezera happy at midright with dissolve
        je "So long as the Emissaries are convinced that they can still plead their case, we can continue to act freely without fear of repercussion from the Fae."
        show rowan necklace neutral at midleft with dissolve
        ro "What of their warnings regarding the leylines themselves?"
        an "We aren’t going to stop using them."
        show jezera neutral at midright with dissolve
        je "Whatever doom they think we are heralding is none of our concern."
        je "For now, we will humor them, string them along as much as possible. In time, the Fae will leave of their own accord."
        show andras happy at edgeright with dissolve
        an "Or we’ll {i}make{/i} them leave."
        je "Until then, I want you to keep an eye on them. But take care not to get mixed up in their conflicts."
        ro "What conflicts?"
        "Jezera smirked."
        #jez smirk
        show jezera happy at midright with dissolve
        je "Come now, Rowan. We both know you aren’t that stupid."
        show jezera neutral at midright with dissolve
        je "You think those two are fast friends? If I had to guess: they were sent here together for a reason."
        show jezera happy at midright with dissolve
        je "It would seem that not all is well in the court of Queen Kassandra."
        show rowan necklace angry at midleft with dissolve
        ro "You know more than you’re letting on."
        je "Perhaps. But for now, this is all you need to know."
        show jezera neutral at midright with dissolve
        je "Speak with the Emissaries, learn what you can of the situation, but take no action either way."
        show rowan necklace neutral at midleft with dissolve
        "Rowan clenched his jaw and nodded. He bowed to the Twins and moved to make his exit. Jezera called to him over his shoulder."
        je "You surprised me today, hero."
        ro "How so?"
        je "I didn’t expect you to speak up on the Fae’s behalf."
        ro "..Neither did I, really."
        je "Then what made you decide to do so?"
        "Rowan thought back to the dream of a few weeks before, when a very-different Jezera asked him that same question. His lips pressed into a flat line."
        show rowan necklace angry at midleft with dissolve
        ro "Call it intuition, but I think there’s more to the Fae than what we’ve seen so far."
        je "Undoubtedly."
        "Her smile was either playful or mocking. Rowan couldn’t quite tell which."
        je "That will be all for now, Rowan."
        scene black with fade
        "..."
        "That night, Rowan dreamt of pleasant days. Of warm summer nights and placid hours of lazy contentment."
        "He could not recall the specifics of the dream, but he remembered the feeling of a soft hand squeezing his shoulder, and a quiet voice whispering in his ear."
        "{i}Thank you…{/i}"
        $ emissariesPresent = True
        return
        
    "Stay silent and let them be banished.":
        $ released_fix_rollback()
        "Rowan kept his counsel. First the dreams, and now this… the Fae were evidently more trouble than they were worth."
        "Despite - or, rather {i}because{/i} of - the fox woman’s cryptic warning, he decided to do nothing." 
        "The events played out to their logical conclusion."
        "Whitescar let out a low snarl. He took another step up the stair. Andras rose to his feet. Jezera uncrossed her legs and sat up. The glow of magic danced in her eyes."
        je "You have outstayed your welcome, ambassador. Leave, immediately."
        whit "I’m not half done with you, whelps."
        an "I’ll {i}gut{/i} you here and now, beast!"
        "Whitescar took another step up the stair, and Andras did the same towards him. The mood in the room took on a murderous air."
        "To Rowan’s surprise, it was Arzyl who broke the tense silence."
        arz "Chieftain, you really do need to learn when to take a hint."
        whit "Stay out of this, witch."
        arz "With pleasure! Though I’ll hasten to add that the Queen commanded you to talk with our hosts, not murder them on their thrones."
        je "We are far beyond talking."
        "Arzyl grinned triumphantly."
        arz "Then it seems we have already lost! A pity. I had so hoped to spend more time with you, my Lady."
        "The Fae turned her back on the proceedings, casting a careless hand backward in halfhearted farewell."
        arz "I shall take my leave then. The Chieftain seems to have things well in hand."
        arz "Oh, and Whitescar?"
        "The wolf’s eyes did not waver from Andras."
        arz "Do try to recall the orders the Queen sent us with. If you happen to get into an… ‘altercation,’ you do so alone."
        arz "Queen Kassandra disavows those who break the compact. The Twins will find no retribution forthcoming from us, should he take such a barbaric step."
        hide arzyl with moveoutleft
        "And with that she left the throne room, taking a leisurely stroll back towards the portal room."
        "Arzyl’s mocking tone seemed to deflate Whitescar. His eyes blazed with anger, and his lips pulled back to expose the full breadth of his jaws."
        hide whitescar with moveoutleft
        "He let out a deep, rumbling growl, then spun around, loping out of the throne room like a predator on the prowl. He cast one last, dark look behind him, then disappeared."
        "A long silence followed the departure of the Fae. Then Jezera rose from her seat."
        je "Rowan, send orders to all our subjects."
        show rowan necklace neutral at midleft with dissolve
        je "The Fae are a threat to our rule, and are to be treated as enemies wherever we find them."
        an "We shouldn’t have let them leave."
        je "A final courtesy, for the help Arzyl has given me in the past. It will not be repeated."
        an "I’ll kill that wolf myself, the next time we meet."
        je "And I’ll gladly watch the spectacle, brother."
        ro "They are a volatile race."
        je "You see now why we didn’t deal with them in the past."
        "It was a tall order, but they had somehow managed to come across as more arbitrary and emotional than the Twins themselves."
        "Rowan was glad to be rid of them. Hopefully now the intrusive dreams would stop. Only time would tell."
        $ emissariesPresent = False
        return
        

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

label paperwork_sabotage:

scene bg6 with fade
show rowan necklace neutral at center with dissolve

"With a sight, Rowan eyed the seemingly never-ending pile of paperwork before him."

if week < 80:
    "It was deceptively small now, but with time, Rowan had no doubts it would grow large enough to tower over him."
    
else:
    "As the twins realm expanded, so did the paperwork, and he knew it would only get worse with time."

"And yet there was no escaping it. Every half-competent commander knew wars were won and lost by the small details hidden inside of them."
"Just like the ones he just noticed in a seemingly simple request from Cla-Min, that now laid on his desk."
"She wanted to send a caravan south from the Rosaria portal, but since the area it would pass banned goblin traders, she wanted half a dozen orcs to act as caravan guards as she sneaked through it."
"It was a reasonable request, if not for the fact Rowan was fairly certain the caravan would be slaughtered. He knew the region Cla-Min wanted to send it through, and he was familiar with the lord who oversaw it. During the war, the two of them worked together briefly, not so long after Rowan was named general."
"If he thought hard, he’d probably remember his exact title and full name, but neither his titles nor his face was important at the moment. What mattered was the intellect and ruthlessness, and his devotion to Solansia's most hardline doctrines." 
"He ruled over a small fief, but did so efficiently, and without mercy. During the military campaigns, he always advised for the most radical course of action – and often made a very compelling point."
"Rowan never liked him, but he knew for a fact there were no bandits or orcs in his lands. The noble did not tolerate opposition, and all who entered his lands met a swift end."  
"A goblin caravan accompanied by a detachment of orcs would not pass his fiefdom unnoticed. Once they enter his lands, they would not emerge from it."  

if serveChoice == 4:
    jump rerouteCaravan
    
else:
    "It would be such a simple thing to grant Cla-Min’s request, and claim ignorance once the Caravan would no doubt end up assaulted and destroyed. Neither Cla-Min nor Jezera would have any right to blame him for the unexpected loss."
    "After all, how could he have known any better?"
    "It wasn’t often he got a chance to sabotage the twin’s efforts just by doing his job only adequately. The question was - could he afford to do so right now?"

    menu:
        "Grant Cla-Min’s request, send the caravan to its doom.":
            $ released_fix_rollback()            
            "One signature, and the orc and goblin lives were now forfeit."
            if avatar.corruption > 60:
                "Rowan chuckled to himself. He spent half his adolescent life learning the sword so he could slay beasts like that in the name of Solansia, and just now he killed half a dozen of them with his pen only."
                "Who could have known the most efficient way of killing his enemies was by being intentionally inept?"
                "It was so much cleaner too!"
                "He chuckled again, then put the request on the finished pile and reached for the next one. With luck, maybe there would be another request like that."
            else:
                "He furrowed his brows as he stared at his signature. He spent half his adolescent life learning the sword so he could slay beasts like that in the name of Solansia, and just now he killed half a dozen of them with his pen only."
                "… The bards did sing the pen was mightier than the sword. Guess there was something to it after all."
                "He sighed to himself, then put the request on the finished pile and reached for the next one."
            $ change_base_stat('c', -5)
            $ change_treasury(-50)
            $ castle.buildings["barracks"].troops -= 6
            return

            
        "Order Cla-Min to reroute the caravan.":
            $ released_fix_rollback()
            label rerouteCaravan:
            if serveChoice != 4:
                "He stared at the parchment for a long time. Going out of his way to save orc lives…"
                "But he had no choice. If the twins’ army did not perform adequately, he would be blamed for it, no matter what external circumstances led to such results."
                "He needed more time, as much as he loathed to admit it."
            else:
                pass
            "He wrote “Request Denied” on Cla-min’s letter, then added “Route dangerous. See me for alternatives.” underneath."
            if serveChoice == 4:
                "Cla-Min would no doubt be grateful for his diligence. The twins were lucky they had him on their side."
            else:
                "At least Cla-Min would be grateful for his intervention. If nothing else, keeping her happy might come in useful later on."
            $ all_actors['cla_min'].relation += 5
            return









