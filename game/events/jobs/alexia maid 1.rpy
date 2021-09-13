init python:

    # special system event to update harassment counter and timer of maid job for some maid events
    event('alexia_maid_harassment_counter', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), init_flags={'harassment_counter': 0}, priority=pr_system_last)
    event('maid_orientation', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), group='alexia_maid', run_count=1, priority=pr_story)
    #Jezera sexcapading in front of Alexia
    event('jezeara_sexcapading_in_front_of_alexia', triggers="npc_events",
        conditions=("get_actor_job('alexia')=='maid'","alexiaAndrasObedient == False", "alexiaJezObedient == False", "get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') == 0"), group='alexia_maid', run_count=1, priority=pr_story)
    event('picky_cleanup', triggers="npc_events",
        conditions=("get_actor_job('alexia')=='maid'", "alexiaAndrasObedient == False", "alexiaJezObedient == False", "get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') == 0"), group='alexia_maid', run_count=1, priority=pr_story)
    event('wandering_hands', triggers="npc_events",
        conditions=("get_actor_job('alexia')=='maid'", "alexiaAndrasObedient == False", "alexiaJezObedient == False",  "get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') == 0"), group='alexia_maid', run_count=1, priority=pr_story)
    #Jezera wants a new agent
    #Scene triggers on fourth harassment trigger (after three main scenes have triggered).
    event('jezera_wants_a_new_agent', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'", "get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') == 0", 'NTR == True'),
        depends=('jezeara_sexcapading_in_front_of_alexia', 'picky_cleanup', 'wandering_hands'), group='alexia_maid', run_count=1, priority=pr_story)


label alexia_maid_harassment_counter:
    # update harassment timer on Alexia (until harassment sequence will not be ended)
    python:
        if get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') > 0:
            set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') - 1)
    return


label maid_orientation:
#Orientation
#Event triggers the first time that Alexia works as a maid

if alexiaJezObedient == False:
    jump nonObedientOrientation
else:
    "Event coming in the next release."
    $ set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', dice(3))
    return

label nonObedientOrientation:

scene bg14 with fade
show jezera neutral at midright with dissolve
show alexia 2 necklace neutral at midleft with moveinleft

"Jezera was interrupted from lazily scanning a tattered book by the arrival of an unexpected guest. Alexia gave a polite half-cough to get her attention."

je "Rowan’s little dove approaches. What have I done to deserve this honour?"

"Alexia curtsied slightly, like she'd seen the castle staff do to Jezera when they crossed paths."

al "Rowan and I have been speaking. We recently decided that it would be good for me to use my time productively. The castle staff always needs more help, so I decided to ask you about joining."

show jezera happy at midright with dissolve

je "My dear, you're under no obligations to do anything to help us."

al "I know. But, there must be some way I can be of use. How could I even look my husband in the eye if he suffered while I lavished in a castle?"

"Jezera snapped her book shut, eyes scanning Alexia."

show jezera neutral at midright with dissolve

je "Then be aware that I have high standards for my staff. If you're going to join their ranks, you best be prepared to meet those or be punished. Are you prepared to work for me?"

al "I am."

show jezera happy at midright with dissolve

je "Splendid. Let’s go down and get you fitted for a uniform. I’m sure it will look just marvelous on you!"

scene alexia_maid_1 with fade

"For most of the week, Alexia busied herself as a member of the castle's domestic staff. She cooked, cleaned, laundered, and even sewed clothing. There was no end to the work and Jezera was a harsh taskmaster."
"Much of the task concerned the restoration of unused segments of the castle. Bloodmeen was built to be the capital of a great demon empire, so only segments of it were actively in use." 
"When the staff had finished tidying the castle rooms in active service, they were sent out to continue reclaiming some long-forgotten wing."
"There was a quiet serenity to the work. What might have been an hour of hard scrubbing could leave a totally different place in its wake."
"She was good at it too. Or at least she thought she was. All that time working on homemaking skills in preparation of life as a village wife for Rowan was finally coming in handy. For once."
"On the third day, she’d heard the overseer praising her from afar in a conversation with another maid."

if all_actors["alexia"].corruption < 60:
    "Alexia didn’t consider herself a proud woman, but there was a quiet thrill in that."

scene bg6 with fade
show jezera happy at midright with dissolve
show alexia maid neutral at midleft with dissolve

"Alexia stood stiffly in front of the throne at the conclusion of her first week’s review. Jezera broke from normal precedent by conducting it first hand."

je "High marks from co-workers. A strong recommendation from your overseer. Clearly, the job will remain yours to keep. My only true concern is that you might be wasting your talents."

"Alexia blinked twice."

al "Whatever do you mean?"

show jezera neutral at midright with dissolve

je "Nothing. Nothing. Just that, that a lady of your mind and...appearance...has more options available to her than just...busy work."

#show alexia maid angry at midleft with dissolve
show jezera happy at midright with dissolve

je "Ah. I’ve overstepped, haven’t I?"
je "Just a morsel for you to feed on. I’m sure there will be more opportunities for us to speak on the topic in the future."
je "After all...you work under me now."

#Roll harassment timer
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', dice(3))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label jezeara_sexcapading_in_front_of_alexia:
#Jezera sexcapading in front of Alexia

scene bg7 with fade
show alexia maid happy at midleft with dissolve

"Alexia was humming a tune under her breath, while washing stains out of the furniture in one of the guest rooms. A quiet normal day. But, one about to be interrupted."

show jezera naked happy at midright with moveinright
show alexia maid shock at midleft with dissolve

al "Uh...."

"Behind the demoness were a couple of very handsome men, who were also quite naked. She had one arm wrapped around each of their waists."

al "Excuse me, I'll come back after-"

je "You needn’t trouble yourself on our account, dove. Keep working, keep working. We’ll be very...quiet."

#jez smirk
show alexia maid aroused at midleft with dissolve

"Alexia, naturally, was still on her way to the door. But, Jezera shut it behind her and locked it with a key. Alexia went so far as to reach for it, but Jezera lazily tossed it over her shoulder behind a large, immobile dresser."

je "Whoops. I dropped it. Seems I’ll have to get one of these strapping young gentlemen to help find it."
je "..after we’ve had our fun, of course."

hide jezera with moveoutright
#alexia maid blush

"To Alexia's horror, the three of them started fornicating right in front of her!  Apparently these guests either didn't care that she was watching them go at it. One of them even kept looking back to see if Alexia was watching.!"
"She pushed that thought as far away as she could and desperately tried to distract herself by setting to work once again on the furniture, while Jezera loudly worked on soiling other pieces."
"At one point, she heard a particularly loud moan emerge from one of the men. Part of her wanted to look. Part of her thought that was the worst idea possible."

menu:
    "Look.":
        $ released_fix_rollback()
        "The moment she glanced that way, she regretted it. One of the men had half his cock buried deep in Jezera’s ass. The other was being throat fucked by Jezera’s fingers as though he were giving a blowjob."
        "Alexia stifled a gasp and looked down again."
        "She just had to focus on her work. That’s all she had to do..."
        $ change_corruption_actor('alexia', 2)
        $ all_actors['alexia'].job_state.stress += 2
        
    "Keep working.":
        $ released_fix_rollback()
        "The impulse soon passed though. She would survive this indignity, as she had survived all the others since her imprisonment…"


#Alexia gains a bit of corruption and stress.  Re-roll harassment timer, increase harassment event count by one.
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_counter', get_event_flag('alexia_maid_harassment_counter', 'harassment_counter') + 1)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', dice(3) + get_event_flag('alexia_maid_harassment_counter', 'harassment_counter'))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label picky_cleanup:
#Picky cleanup

$ pickyCleanupSeen = True

scene alexia_maid_1 with fade
show alexia maid neutral behind alexia_maid_1

"Alexia’s work today was slower than her usual. Her mind was elsewhere. Green fields that stretched out for miles. A blue sky. A young man returning home after being away for so long."
"Somewhere else..."


scene bg14 with fade
show alexia maid neutral at midleft with dissolve
show jezera neutral at midright with moveinright

je "Ah, there you are Alexia."

"Alexia stopped her sweeping, turned around to face Jezera and curtsied."

al "Yes Mistress? How may I help you?"

show jezera happy at midright with dissolve

je " I have an especially exciting task for you today, my little tart. You’re getting the luxurious honor of cleaning my bedroom today. "

#show alexia maid angry at midleft with dissolve

al "But-"

je "Not a word. I’ve ensured that someone else will handle the hallway instead."

"The half-demon stepped to the side and allowed another maid to pass. After a moment's annoyance, Alexia handed the newcomer her broom and followed Jezera."

hide jezera with moveoutright
hide alexia with moveoutright

scene bg18 with fade
#show alexia maid concerned at midleft with dissolve
show alexia maid neutral at midleft with dissolve
show jezera happy at midright with dissolve

je "Behold! My humble abode!"

"The room was in quite the state of disarray, with cushions and blankets strewn all over the place as well as at least one pool of something unmentionable on the floor."

je "I expect it to be spotless and in perfect order when I return."

show alexia maid neutral at midleft with dissolve

al "...  Very well, when will you return?"

je " In an hour? Perhaps two. Better get to work, chop chop."

"Alexia felt a sudden sharp pain. The demoness had casually given her a slap on the ass, with enough force to leave Alexia on the tips of her toes. "

show alexia maid shock at midleft with dissolve

al "Hey!"

show jezera happy at midright with dissolve

je "Ta ta, love"

hide jezera with moveoutright

"She walked out of the room, leaving the red haired woman to her work."

scene black with fade

scene bg18 with fade
show alexia maid neutral at midleft with dissolve

"A little over an hour and a half later, Alexia had taken all of the sheets and soiled cushions down to the laundry and brought up replacements. She'd made up the bed and was working on cleaning up the unmentionable mess when Jezera returned."

show jezera displeased at midright with moveinright

je "What is this? No, no, no!"

show alexia maid shock at midleft with dissolve

"Taken aback by the harshness of her mistress's words, Alexia shied back from her and managed to soil her uniform in the mess she was cleaning."

al "What's wrong? What did I do?"

je "Do? What did you do?!"
je "YOU PUT GREEN BLANKETS ON MY BED!"

al "Wha-what's wrong with green?"

je "Does it look like green is my colour? Think! You’re smarter than that!"
je "A woman must grasp aesthetics if she wants to do anything in this world."

#show alexia maid concerned at midleft with dissolve

al "I'm sorry, this really is out of my league. Court fashion and art just isn't something a common housewife like me should-"

je "Shh. No more talking."

"Jezera walked slowly, almost tenderly, up to Alexia and looked her in the eyes. Then, in a superhuman flash of movement, Jezera had a hand in her hair and was twisting it. Alexia cried out from a sudden rush of pain. Her form contorted."

je "You are going to fix this. You are going to go to supplies with this trash. You are going to return with proper blankets. You are going to keep trying until you learn. You will do it perfectly."
je "You will replace every cushion. You will replace every rug. You will replace every curtain. You will learn to serve a lady of class. You will be perfect."

show jezera happy at midright with dissolve

je "Is that understood, darling?"

al "Y-yes."

"Alexia rushed out of the room and searched for a wall to lean against. She needed to catch her breath."

#Increase Jezera influence over Alexia.  Re-roll harassment timer, increase harassment event count by one.
$ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 2)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_counter', get_event_flag('alexia_maid_harassment_counter', 'harassment_counter') + 1)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', dice(3) + get_event_flag('alexia_maid_harassment_counter', 'harassment_counter'))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label wandering_hands:
#Wandering Hands

scene alexia_maid_1 with fade

"For the most part, Alexia found working in the castle to be enjoyable. Her skills translated well and most of the staff was at least cordial most of the time."
"There were always bad apples, but the housewife felt like she was making friends and finding her place."

scene bg14 with fade
show alexia maid happy at midleft with dissolve

"The main unfortunate part of her work was her boss."

show jezera happy at center with moveinright
hide jezera with moveoutleft

show alexia maid shock at midleft with dissolve

al "Hey!"

scene bg6 with fade
show jezera happy at center with dissolve
#show alexia maid angry at midleft with dissolve
show alexia maid neutral at midleft with dissolve

al "My Lady...I really would appreciate it if you didn’t touch me...down there…"

"Alexia tried to extricate herself from the feminine hand that had managed to get a firm grasp of her rear end. But, not only could she not wrench herself free, the struggle just left her more overstimulated."

je "Oh darling, I'm just showing how much I appreciate you. What’s a little physical expression of closeness between friends?"

"The sudden jolt of a new squeeze was enough to remove any of Alexia’s compunctions about more forceful resistance. She grabbed Jezera’s hand and managed to yank it away with some effort."

show alexia maid shock at edgeleft with moveoutleft

al "Ah!  Hands off!  Don't grope me!"

"Jezera pulled back with a satisfied giggle. What did she enjoy more? The groping itself or Alexia’s more forceful reaction?"

je "It seems you passed today’s special inspection. Keep up the good work, darling. You’re a joy to have around."

scene alexia_maid_1 with fade

"This hadn’t been the first time Jezera had gotten a grip on her, and it wouldn’t be the last. Alexia was starting to accept that the odd inappropriate touch was just the cost of being allowed to participate on the castle staff."


#Jezera gains influence on Alexia, Alexia gains a little corruption.  Re-roll harassment timer, increase harassment event count by one.
$ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 2)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_counter', get_event_flag('alexia_maid_harassment_counter', 'harassment_counter') + 1)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', dice(3) + get_event_flag('alexia_maid_harassment_counter', 'harassment_counter'))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label jezera_wants_a_new_agent:
#Jezera wants a new agent
#Scene triggers on fourth harassment trigger (after three main scenes have triggered).

# deactivate harassment counter and timer
#~ $ deactivate_event('alexia_maid_harassment_counter')

scene bg14 with fade
#alexia maid happy
show alexia maid neutral at midleft with dissolve
show jezera happy at midright with moveinright

"Alexia had scarcely finished putting on her uniform for her shift before a shadow descended on her."

je "Alexia dear? It’s amusing that I stumbled on you. I was just thinking about which girl might be perfect for a very special job."

al "A special job?"

if alexiaJezObedient:
    "Alexia lowered her head in deference. Inwardly, she was brimming with curiosity."
    al "What would you have me do, Mistress?"

else:
    "Alexia shifted in place. With all the groping and violations to her comfort zone she’d already received, dread sat in immediately. Whatever this could be, it wasn’t going to be good."
    "Still, she had enough sense to avoid openly antagonizing the lady of the castle. So she held her tongue for the moment."


je "There's a man of some magical power who is currently my guest at Bloodmeen. He has a history with demons and is rather cautious around me. Thus far he's been, difficult, to get information out of."
je "I would like you to spend some time with him, intimate time. Enough so that he lets his guard down and tells you things."

if alexiaJezObedient == False:
    show alexia maid shock at midleft with dissolve
    al "..."
    "Her mouth hung. The words seemed impossible to process."
    al "You’re telling me you want me to...to...prostitute myself out so you can get some information?"
    #jez smirk
    je "Oh darling, you make it sound like I’m asking you to jump off a bridge. No no, just spend a little quality time with him. Be there to listen to him. Stroke his leg a bit."
    je "Maybe stroke a little bit more if you’re feeling adventurous."
    "She gave a wicked grin."
    al "But...but, I’m married..."
    je "Alexia, darling. You were the one who said that you wished to be useful to us. Did you not? That’s why you’re standing here in that scrumptious outfit of yours?"
    al "Yeah, but I didn’t mean…"
    "A finger went to her lips, silencing her objections."
    je "This is what it would take to be useful to us. Any of the other girls on the castle staff would do it without question. That’s what it means to serve as my maid."
    #show alexia maid angry at midleft with dissolve
    show alexia maid neutral at midleft with dissolve
    "Alexia took a step back, clutching her hands into fists. An unconscious reaction. To swing at the demoness might have meant death."
    al "I said I’d help Rowan. That’s what I want. To help him."
    je "To help him, you need to help me."
    "Her hand brushed down the side of Alexia’s body with the practiced smoothness of a woman who knew what other bodies felt like. Alexia couldn’t help shuddering slightly."
    al "Wh-why me? You said the other girls…"
    je "The other girls are not you."
    show jezera displeased at midright with dissolve
    "Jezera took a step forward. Alexia ceded space, in moments she was pressed with her back to the wall. Jezera’s piercing hypnotic eyes trained with intensity on her."
    je "On your first day as {i}my{/i} maid, I told you that you had more options available to you than just busy work."
    je "You have considerable talents, my dear. I could send another maid to attempt it. But none could accomplish what you could."
    show alexia maid shock at midleft with dissolve
    "Alexia blinked and shied from Jezera’s glance. Surely that wasn’t true? She was just a housewife…"
    show jezera happy at midright with dissolve
    je "It has to be you. I consider it something of a…"
    je "...well, let’s call it an investment."
    "Alexia ducked to the side, so that Jezera no longer had her pinned. The demoness backed up slightly and giggled softly at the way the redhead tried to catch her breath."
    
else:
    show alexia maid shock at midleft with dissolve
    al "By intimate, you mean...?"
    je "Fool around with him? Give the boy a good time?"
    je "Yes. I do."
    show alexia maid aroused at midleft with dissolve
    "Alexia gasped to herself, cheeks growing flush."
    al " Mistress! You can’t mean to-"
    #jez smirk
    "Jezera moved closer, pushing Alexia back against the wall. The redhead couldn’t stop herself from arching her back. No matter the situation, Jezera’s body felt good…"
    if mikaelDance:
        je "Protesting now? I seem to recall you a bit more..pliable...when my friend Mikhael came to visit. Surely if that was okay, then this is no problem."
        je "Just as reasonable a request."
        "Alexia flushed slightly at the memory..."
    else:
        "I can mean whatever I want to mean, little one. You’re not such an innocent flower anymore, now are you?"
    je "I need a good little maid to flirt with him and make him want to run his mouth. And what girl on my staff do I trust more than you?"
    je "Besides…"
    "A finger trailed Alexia’s ear."
    je "This is for your benefit."
    "Alexia’s eyelashes fluttered."
    al "My…"
    je "Mhm. You need to learn how to make a man feel good. For Rowan’s sake, of course."
    al "For Rowan’s sake…"
    je "And you need to learn how to use that body and mind of yours properly. I didn’t take you on for training because I thought you’d just make a good maid."
    je "You have incredible potential, little dove. The power to twist your way into the hearts of men. To traffic in important secrets. To put that mind of yours to work. Where it belongs."
    #show alexia maid concerned at midleft with dissolve
    "Alexia brushed herself from Jezera’s grasp. Her heart was beating so fast now. Part of her was screaming at herself for even considering it. But, Mistress was speaking so persuasively..."

show alexia maid neutral at midleft with dissolve

al "Wh-what information...exactly...are you trying to extract from him?"

show jezera happy at midright with dissolve

je "That sounded like a yes, darling."
je "Well, that's your test. The more you find out, the more impressed I'll be. So, are you ready to meet with Mr. Garforth?"

menu:
    "Accept Jezera's task.":
        $ released_fix_rollback()
        if alexiaJezObedient == False:
            #show alexia maid concerned at midleft with dissolve
            "Alexia’s lip trembled. Then she closed her eyes."
            al "Would I have to go all the way with him? If I could get the information without...doing anything. Would that be acceptable?"
            show jezera displeased at midright with dissolve
            "Jezera rolled her eyes."
            je "One supposes."
            al "..."
            al "Alright. I will try."
        else:
            show alexia maid aroused at midleft with dissolve
            "She breathed in, searching for air. Even here, even now, she trusted Jezera. There was no question how she’d answer."
            al "If that’s what you wish of me…"
            #jez smirk
            "Her head started to lower, but Jezera bid it back up and planted a kiss on her lips."
            "Jezera’s hand locked with hers, and she felt something soft being pushed into her grasp."
            je "Take it with you, dove. A sign of my affection. So you know that your Mistress is with you the entire time."
            "Alexia looked down at her hand and found she was holding a familiar black choker..."
        jump garforthMeet

    "Reject Jezera's task.":
        $ released_fix_rollback()
        #show alexia maid concerned at midleft with dissolve
        al "Please, Jezera. Don’t make me do this."
        al "...Please."
        "She looked Jezera closely in the eyes. She wanted to make it impossible to miss her discomfort with such an assignment. She was a married woman. A married woman."
        if alexiaJezObedient == False:
            show jezera displeased at midright with dissolve
            je "Clearly, you have a long way to go if you wish to really be of use. But potential cannot be forced, it can merely be cultivated."
        else:
            "She had a line she would not cross. No matter how strong the desire to please was…"
            show jezera displeased at midright with dissolve
            "Jezera sighed and took a step back."
            je "..."
            show jezera happy at midright with dissolve
            je "Of course, my dear. You’ve already proven yourself more than willing to be obedient. You needn’t push yourself in every circumstance."
            je "A shame. This would have been a perfect chance for you to...develop...but there will be other opportunities. I’ll make sure of that, sweetling."
            "Jezera reached forward and gently caressed a strand of Alexia’s hair."
        show jezera neutral at midright with dissolve
        je "I will have another maid take up the task. Resume your usual duties, girl."
        "Then, the demoness strut back the way she came. For a lingering moment, Alexia watched the sway of her rear on the way out."
        show alexia maid neutral at midleft with dissolve
        "Alexia’s breath caught in her throat."
        if alexiaJezObedient == False:
            "Had that monster really asked her to do such a thing?"
        else:
            "Had she really said no to her Mistress that way?"
        return

label garforthMeet:

scene bg14 with fade
#show alexia maid concerned at midleft with dissolve

"It was late in the evening by the time she found herself standing in front of Mr. Garforth’s door."
"Alexia fidgeted in place, nervous about what was going to happen. (She squeezed down on the thin strip of cloth in her hand.)" 

play sound "music/SFX/door knock.ogg"
pause 1

#CG of Alexia speaking to Mr. Garforth.  CG is inside the generic guest room.
scene cg406 with fade
show alexia maid neutral behind cg406
pause 3

gar "Yes? A redhead? She knew about my weakness for redheads, huh?   Come in, come in.  I'm curious what you're going to try on me."

"Alexia cautiously entered the room. Not quite the reaction she had expected... "
"Mr. Garforth was a rather small thin man.  A quick glance was more than enough to know he was no common visitor, though. Tomes of power, similar to the library, were scattered in a mess across the room. The result of sleepless nights of study, no doubt. "

al "Uh, Mr. Garforth, right?"

$ garforth_name = "Mr. Garforth"

gar "Yes. The nervous maid routine?  Hmm, seems lazy.  Honestly, I thought that Jezera herself would come by to try and loosen my lips, but you don't exude that level of power.  I wonder, what class of demon are you, girl?"

#scene black with flash
#cg variant
#scene black with dissolve
#show alexia maid neutral behind black

"Alexia felt an indignant reply start to rise up. But it died on her lips when a bright flash of light blinded her for a moment. Her vision cleared, and there was a look of absolute terror on Mr. Garforth's face."

al "What was that for?!"

gar "Y-y-you're not a demon!"

al "If you’d have let me, I would have simply told you that."

gar "Oh, uh, I'm s-s-so sorry! I, uh, I'm not..."

"His voice trailed off too quiet for Alexia to hear him. The two simply looked at one another for a long awkward moment before the woman cleared her throat and spoke up again."

al "I didn't catch the end of that."

gar "I'm not good around girls. When you were a demon, it was…"
gar "Well, rather easier, I suppose..."

al "Please relax, Mr. Garforth.  I'm not going to do anything to you. I just want to talk. "

gar "Of course, right."

al "Why were you much more confident when you thought I was a demon?"

gar "Well, I studied a lot about demons when I was an apprentice. Especially safeguards against their influence and power." 
gar "This was going to be how I tested myself. I was going to find the demons of this place and show they could do nothing to me."

al "That sounds very brave. But what made you think that there'd be demons here?"

gar "Well, I noticed a strange nexus in the world's flux field about a year and a half ago.  I'd been tracking it since, and eventually figured out it originated here."

al "That sounds impressive! All this magic talk is beyond a simple maid like me. Have other sorcerers done the same thing?"
   
gar "It's not something a normal sorcerer would notice. Most don't gaze around the outer dark looking for the specific kinds of demons I do."

al "Specific kinds of demons?"

gar "Yeah, they... uh... "
gar "Well, I, er, don’t suppose the rest is something I should be talking about. You said yourself you wouldn’t understand."

"Despite her attempts to convince him otherwise, it seemed that Garforth was quite done saying anything to Alexia."

scene black with fade
#show alexia maid concerned at center with dissolve
show alexia maid neutral at center with dissolve

"Alexia slammed her eyes shut."

if alexiaJezObedient:
    "She had hit a brick wall and she knew it. What was her Mistress going to say when Alexia returned, with barely anything to show for it?"
    "Her Mistress…"
    "She opened her palms and saw the thin strip of fabric. Without thinking, she slid it around her neck. There was no more need to worry. She knew what to do."
else:
    "Her hands shook. She couldn’t do it. She couldn’t extract information from him by just talking, no matter what. Jezera was going to be so mad at her…"
    "Alexia blinked twice. Jezera hadn’t sent her into this room to {i}talk{/i} information, had she?"
    "On the outside, she tried to seem engaged in Garforth and the conversation. But inside a tempest was raging." 
    "What was she doing here? How had she let herself be talked into this?"
    if all_actors["alexia"].corruption < 31:
        "She was married. She’d made vows. She was a good and proper wife, and they didn’t go around fucking other men behind their back. No matter who it would please."
        "But, then good and proper wives wouldn’t be in this situation in the first place. If she were the woman she thought she was, she would have told Jezera to shove it the moment the demoness had even suggested coming here to flirt with him."
        al "I’m so stupid…"
        gar "Hrmm?"
        al "Oh! Nothing. Nothing. I just got confused about something."
        "Confused about a lot of things…"
        "There was only one thing she could do. Only one way to resolve this. She had to let instinct take over. In a room with him and pressed for time, she couldn’t think it through."
        "She would…"
    else:
        "Alexia shook her head. It wasn’t as if getting naughty with some stranger was quite the ask it might have once been. But, was this who she was now? Someone who Jezera could just talk into sleeping with some stranger?"
    menu:
        "”Seduce Garforth”":
            $ released_fix_rollback()
            pass
            
        "”She couldn’t do it”":
            $ released_fix_rollback()
            scene bg14 with fade
            #show alexia maid angry at center with dissolve
            show alexia maid neutral at center with dissolve
            "Without a further thought, Alexia made for the door. She shook her head slightly as she walked. This was too much for her. How could Jezera ask this of her?"
            gar "Erm, where are you going?"
            "Alexia kept walking without listening. Her mind was made up. Jezera would be mad, of course, but compared to the prospect of being a whore on her command, this was preferable."
            "She swore at herself under her breath. How had she almost been lured into this? And, as she walked, her thoughts turned to Jezera and how she’d been treating her until now."
            "Jezera liked to pretend she was a friend helping her out. But she wasn’t. Alexia would have to remember that…"
            $ change_actor_num_flag('alexia', 'jezera_influence', -3)
            return


scene cg98 with fade
pause 3

"Abruptly, Alexia pulled Garforth into a sudden meeting of their lips. His eyes shot open from surprise, but he didn’t try to shove her away."
"What’s more, as Alexia kissed him, his posture relaxed slowly. All of the tension melted into her arms. Very unlike how Rowan normally was…"
"The distance between them closed. Her bosom brushed against his chest, close enough that she was sure he could feel it. His hands wriggled to the side, but didn’t even dare to actually touch her body." 
"It was funny, she actually would have let him."


scene cg97 with fade
pause 3
show alexia maid aroused behind cg97

"Finally, Alexia broke it off. The man was left standing in place, dazed and bewildered."

al "You don’t have to be nervous. Really. The truth is, I’m here against Jezera’s orders. She told us that no one was to meet with the sorcerer. But, I was curious."
al "Can you forgive me, Sir?"

gar "...Huh? Really?"

al "You can trust me."

scene cg96 with fade
show alexia maid aroused behind cg96
pause 3

"Alexia led him by the hand to a large leather seat at the front of the bed. Garforth, still blinking rapidly, proved willing to let her lead."

al "Why don't we start over? I haven’t even asked for your first name yet, have I?"

gar "It’s...it’s Berrington."

al "What a nice name, I think I'll call you Berry. You don't mind, do you?"

gar "N-no."

if alexiaJezObedient == False and all_actors["alexia"].corruption < 60:
    "Alexia breathed inwardly."
    
"She placed her hand on his leg and slowly trailed it up. Garforth’s breathing hiked, but he was too stiff to escape her. Soon, her fingers were between his legs tracing the outline of a hardening bulge through the fabric. His eyes bulged."

al "Berry, do you think you could tell me more about yourself? I’m risking a lot coming down here… "

"The man proved as pliable a source of information as he was a pliable toy for Alexia to fondle. He spoke about his magical interests, his path to the castle and more."
"Whenever the string of new information would stop, Alexia’s hand would “mysteriously” pull backwards. Only to return whenever he complied with her latest question."
"Still, Alexia’s brow was starting to furl. There were parts of the story she wasn’t getting."

al "Oh, but Berry. What about your teacher? Was learning it all exciting? What were they like?   "

gar "Oh...oh, you’re really good at. No one has ever…"

al "Hrmm? What was that? You were talking about your teacher?"

"She punctuated her last sentence with a much harder stroke, then slowed her fondling to a near stop."

gar "I... I... I really shouldn't say anymore."

"Alexia suppressed her frown. Somewhere along the line, she’d started to do this more of her own volition than to fulfill a mission. When he told her some new secret, it made her want to push him further. To see how far she could go."
"But now she was staring at that brick wall again." 
"Toying with his cock through his trousers had only gotten her so far. If she wanted the last important parts, she’d need to take it further."

menu:
    "This is good enough." if alexiaJezObedient == False:
        "Alexia closed her eyes and got control of her breathing. Part of her was still urging her on. She wanted to know the rest. She wanted to melt this boy as though he were a candle."
        "But the rest of her knew something more important was true. Rowan would be waiting for her tonight."
        al "Hehe. I suppose everyone is allowed their secrets. I’m just so excited about meeting you!"
        gar "Oh. Yes yes. Of course."
        "Alexia tried to move the topic to other matters, but she found herself frustrated on all points. It was not long before she was wishing the timid man goodbye."
        "By the time she was approaching the door, he was left panting and half out of breath. This time she couldn’t suppress her own smirk. Surely once she left, he’d finish the job she started…."
        jump garEnding
        
    "Take him all the way. ":
        $ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 3)
        $ change_corruption_actor('alexia', 5)
        pass
        

scene black with fade
show alexia maid happy behind black

if all_actors["alexia"].corruption < 31:
    "Alexia bit her lip."

if alexiaJezObedient:
    "Alexia brushed her fingers over the choker...her collar. She wasn’t alone."

"Without a word of warning, she pushed the sorcerer backwards. He continued to yield to her until he was half reclining and she was straddling his lap." 
"Her hips softly ground into him. If he could process what was going on, he might notice how damp the point of contact was. He had not been the only one growing excited."

if all_actors["alexia"].corruption < 31:
    al "(Goddess...I’m really going to do it…)"

else:
    al " (I’m such a slut…)"
    
gar "What was…?"

al "Shhh. Just relax."

if all_actors["alexia"].corruption < 31:
    "She brushed her lips against his ear awkwardly. A timid attempt to replicate the kind of seductions she’d seen Jezera perform flawlessly."

else:
    "She brushed her lips against his ear as seductively as she could."
    
al "I’ve always wanted to fuck a sorcerer..."


scene cg92 with fade
show alexia maid aroused behind cg92
pause 3

"Every part of him yielded to her. When she drew it out, his cock sprang to attention. When she set him into position, he followed suit. And when she kissed him, he fell into her lips."

gar "Wait, I’ve never…"

al "No words. Shh..."

"He sputtered weakly, but couldn’t look away. She raised her skirt, unhooked her panties, and made a show of pulling them away."
"Then, she grabbed his cock in her hand, bulging and hard, and settled it beneath her. She suppressed a giggle. It was smaller than she expected. Even still, she dutifully aligned it between her legs...and then lowered herself down."

gar "Oh...my word...my word…."

"Alexia groaned and tested with a quick buck of her hips. Small perhaps, but not too small for her to enjoy. She reached down, cradling Garforth’s head in her hands so she could look him in the eyes."
"Beneath her, the man was a mess of squeaks and groans. His mouth seemed to twist into a new shape with every roll of her hips. She sped up the pace of her movements, just to eke out more intense reactions from him. He never disappointed."
"That aspect was almost...almost more pleasurable than being filled. Rowan was always so composed, even when she was nominally on top. But Garforth yielded to every sensation. She was desirable to him. She was riding him." 
"For a brief flash of a moment, she was young again." 

gar "I...I never knew it felt like...oh...oh…"

"Alexia leaned back and made a point of rolling her hips. Every technique and every skill she’d learned in a decade of marriage went into it. Garforth half laid still, more a saddle to ride than a partner in motions."
"But that was okay, Alexia would lead."
"In fact, with even a bit faster a pace of stimulation, Garforth seemed to be advancing to a release. Alexia could hear his breath quicken and see the contortions of his face growing more dramatic. She frowned."
"And slowed the movement of her hips quite a bit. It took a few seconds for Garforth to even notice. He bucked slightly under her, but her control over their pace was not even budged."

gar "Wha-"

al "Shhhhh. I don’t want it to end."

gar "Oh….oh."

"The following minutes of slow deliberate grinding were a form of torture. Every time his breath caught, she’d slow slightly more." 
"The rise and fall of her chest only continued to grow heavier. His faces were too much. The desperation, the lack of control over sensation. She rode each expression as much as she rode his cock."

gar "Pleasee...oh...I can’t take it...please!"

"Alexia blinked twice and gasped. What had she been doing? She’d really gotten into it..."

al "Y-yes, of course. Together."

"At once her hips sped up into a heavy rhythm. The air rang with the slapping of flesh against flesh. It was the kind of attack that a man such as Garforth would never be able to withstand."

gar "Oh! Oh, I’m...I’m going to-"

al "Me too! I’m going to-"

"She was lying."

scene cg92 with sshake
scene cg92 with sshake
scene cg93 with flash
show alexia maid aroused behind cg93
pause 3

"When it was over, and when he returned to consciousness, he did so to Alexia’s face smiling right beside him."

al "So, you were going to tell me about your teacher, Berry?"

$ alexiaUnfaithful = True
$ garInfo = "4"

label garEnding:

scene bg14 with fade
show jezera happy at midleft with dissolve
show alexia maid neutral at midright with moveinright

"Alexia took a deep breath and then gave the door two quick knocks. In between, she straightened her hair and outfit. The door opened, revealing the inquisitive face of the demoness."

if garInfo < 4:
    je "You’re flushed, darling. Did I put you through too much?"
    #show alexia maid concerned at midright with dissolve
    al "...still?"
    je "Oh, hush. I’m sure you’d fool someone less initiated if they saw you. Your husband perhaps."
    
else:
    je "Welcome back, darling. It’s good you came straight here. I wonder what your husband would think of that little {i}mess{/i} that our dear visitor left on your dress."
    show alexia maid aroused at midright with dissolve
    "Alexia looked down at her dress. At once she went white. There was no mistaking what had been spilled over her uniform."

je "What did you think of Mr. Garforth?"

show alexia maid neutral at midright with dissolve

al "I don't know.  He seemed ... weak?"

je "A perfect first target, no? A woman should learn to adore men of that sort. They offer more and more to please you and don’t say a word in protest when you take more still."
je "To such a man, any woman can be a queen. From a powerful demoness...down to a castle maid."

show jezera neutral at midleft with dissolve

je "Now, let's hear what you discovered from our guest."

scene black with fade
pause 1
scene bg14 with fade
show jezera happy at midleft with dissolve
show alexia maid neutral at midright with dissolve

if garInfo < 4:
    show jezera neutral at midleft with dissolve
    je "So you weren't willing to take that last step? Tsk tsk. And from the sound of it, you were doing so well, too. Tsk."
    show jezera happy at midleft with dissolve
    je "Still, for the moment, I'm suitably impressed by your efforts."
    
else:
    je "Fascinating. Very fascinating. I suspected, in truth, that was who he was learning this from. But I needed proof. You’ve done very well tonight, my maid."
    show alexia maid happy at midright with dissolve
    "Alexia blushed softly."
    al "I wanted to test myself. I wanted to see if I could do it. To see how much I could milk from him."
    je "From the looks of it, quite a bit. But to me there was no test involved. I had every confidence from the moment I sent you that you’d return with all I wanted and more."
    je "You’re a good girl, Alexia."
    
if alexiaJezObedient == False:
    je "As a reward, I believe that I'll be able to restrain myself while you're working as a member of my staff."
    if all_actors["alexia"].corruption < 31:
        #show alexia maid concerned at midright with dissolve
        "Alexia blinked twice."
        al "Is that what is considered a reward here?"
        #jez smirk
        je "If you’re displeased, I can continue toying with you when the mood arises?"
        "Alexia shook her head fast."
        al "No, no! Thank you for the reward, Mistress."
        "Alexia lowered her head and ducked to the side. Even as she retreated down the hall, she could still hear the faint sound of Jezera’s laughter."
    else:
        show alexia maid aroused at midright with dissolve
        "Alexia glanced sideways."
        al "Are you implying that your attention is a punishment? I thought you were trying to make me enjoy it."
        #jez smirk
        je "When did you get so clever, girl?"
        al "I’ve been in Bloodmeen too long."
        "Jezera rolled her eyes and shooed her off. Alexia left with a smile on her lips. All witty retorts aside, she’d done a good job. And the feeling of Garforth melting in her hands."
        "She flexed her fingers and then closed them into a balled fist."

else:
    je "I am sure I can come up with some kind of suitable reward for you...the next time I call you for an evening visit."
    show alexia maid aroused at midright with dissolve
    "Alexia blushed a dark shade of red."
    al "I have no doubt of your abilities, Mistress."
    "Alexia turned to leave. Jezera was a woman with important duties to attend to after all. But, before the door closed, she came up with one last thing to say."
    al "By the way...the choker helped. A lot."
    #jez smirk
    "Jezera didn’t answer her. But Alexia was sure she saw a smirk as the door closed behind her."

return


