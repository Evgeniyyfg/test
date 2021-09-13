init python:

    #Cla-Min bribing a proposition (benediction, sex)
    #Requires that Cla-Min's family dinner have happened at least 3 weeks prior and will require mission three to have started once the game timer has been extended.  Event can possibly be a trigger point for Cla-Min's stock to be updated.
    # activated in "goblin_family_dinner" with timer=3
    event('clamin_bribing_proposition', triggers="week_end", depends=('goblin_family_dinner', 'raeve_keep_visit_goal2'), conditions=('week >=4',), active=False,
        group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg19")
    #Helayna has been claimed
    #Requirements - Rowan claimed Helayna during assault on Raeve Keep
    #High priority event, triggers the week that Helayna was claimed.
    event('helayna_has_been_claimed', triggers="week_end", conditions=('raeve_keep_rowan_claimed_helayna', 'week >=4'), group='ruler_event', run_count=1, priority=pr_ruler_high)
    #Delf Dipping
    #Pre requisites - Breeding pit / met Draith
    #should probably occur within a few weeks of building
    event('delf_dipping', triggers="week_end", conditions=('week >=4', 'castle.buildings["pit"].lvl >= 1'), group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg25")
    #Greyhide's table manners
    #Follow up from Drinking Buddies if player chose to introduce Greyhide to Alexia, and if Alexia and Greyhide have not met before.
    event('greyhide_s_table_manners', triggers="week_end", conditions=('week >=4',), depends=('drinking_buddies','greyhide_meets_alexia',), group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg22")


label clamin_bribing_proposition:
#Cla-Min bribing a proposition (benediction, sex)
#Requires that Cla-Min's family dinner have happened at least 3 weeks prior and will require mission three to have started once the game timer has been extended.  Event can possibly be a trigger point for Cla-Min's stock to be updated.

$ cla_tit_job = True

scene bg19 with fade
show rowan necklace happy at midleft with dissolve
show clamin happy at midright with dissolve

ro "... and that's it for this weeks main orders."

cla "Excellent, then we can move onto more important matters!"

show rowan necklace neutral at midleft with dissolve

ro "Cla-Min, what is this about?"

"The goblin woman didn't answer, instead she busied herself with extracting a package from some nearby boxes, obviously intentionally taking the time to show off her backside to Rowan at the same time."
"As she came back around, her brother made his appearance and did an exaggerated stretch as he leaned against the nearby wagon. Rowan raised an eyebrow, realizing right away that this was a planned display."

#if Rowan was sucked off by Cla-Min's daughter
if goblin_family_dinner_mins_blowjob:
    "No doubt they were going to be making an attempt to earn his favor again, same as her family dinner.  Rowan felt himself become semi-hard at the thought of that night, to his discomfort."
#If Rowan refused the goblin blowjob
else:
    "Rowan rolled his eyes at this.  The Cla caravan was persistent, he'd give them that much.  Though he had to admit he was curious what they had planned for him this time, especially what that package was."

#rejoin
ro "Well, are you expecting me to ask what's in the package?"

cla "A little gift, of sorts."

ro "There's a catch then, isn't there?"

cla " Oh, I would hardly call this a catch. This item here is very powerful and rare, and I could never part with it for free to someone who wasn't a part of my family or I knew cared about them greatly."

"She unwrapped the package, revealing a glimmering sword of exquisite make and quality. It wasn't intended to be showy or beautiful, this was a weapon of function."
"Rowan could tell from a glance that it wasn't made of iron and might even have some magic in it."

ro "Couldn't I just buy that from you? I'm certainly interested, if that's not a brand made by the priest's of Balast, it is an extremely convincing forgery."

show clamin neutral at midright with dissolve

cla "You could, I would certainly part with it for a fair price."

show clamin happy at midright with dissolve

cla "However, wouldn't you rather an alternative? Why don't we have a nice personal discussion in my wagon, just let me take a seat on you until you fill me up with your cunning and sneaky spunk?"
cla "My brother could also discuss the details, if you'd rather have a man take you on for the time being. We'll worry about transferring the essence to a more compatible member of my family afterwards."

ro "It sounds like you're trying to pay for my body, am I a whore then?"

"The two goblins burst out laughing."

cla "No! No! Haven't you ever heard of a dowry, hero Rowan? It's traditional to give a gift when one departs their clan to join yours as a lover."
cla "Since you aren't really leaving a clan, I think it's appropriate that you receive the gift."
cla "We would be family then, after all?"

#If society chosen was feudal and Rowan has an unspent favor with Jezera or Andras.
if society_type == 'feudalism' and (all_actors['jezera'].favors >= 1 or all_actors['andras'].favors >= 1):
    cla "I suppose that since you've got the ears of our masters, if you could instead get them to grant a title to my brother here, that would convince me that you have my family's best interests at heart."

menu:
    "Have sex with Cla-Min":
        $ released_fix_rollback()
        jump claminSwordSex

    "Have sex with Cla-Min's brother, Cla-Bow.":
        $ released_fix_rollback()
        $ rowanGaySex += 1
        jump brotherSwordSex

    #if feudal and you have the neccesary favour
    "Convince Jezera to grant a title to Cla-Bow." if society_type == 'feudalism' and all_actors['jezera'].favors >= 1:
        $ released_fix_rollback()
        #lose 1 favour with Jezera
        $ event_tmp['using favor'] = 'Jezera'
        $ change_favor('jezera', -1)
        jump clabowTitleGranting

    #if feudal and you have the neccesary favour
    "Convince Andras to grant a title to Cla-Bow." if society_type == 'feudalism' and all_actors['andras'].favors >= 1:
        $ released_fix_rollback()
        #lose 1 favour with Andras
        $ event_tmp['using favor'] = 'Andras'
        $ change_favor('andras', -1)
        jump clabowTitleGranting

    "Refuse":
        $ released_fix_rollback()
        ro "I think I'm good. Thank you for showing off your new stock, I'll definitely be considering a purchase soon."
        show clamin neutral at midright with dissolve
        cla "Such a shame.  Very well, this sword is now on sale. I hope you'll reconsider your other position soon. I assure you that under me is a very good place to be."
        #//End scene, Cla-Min's stock is updated to include the Balast's Brand at 300 gold, possibly other things as well.
        $ castle_shop_trader.inventory.add('balasts_brand_discounted')
        return

################################################################################

label claminSwordSex:

"Cla-Min was bouncing again and Rowan was having a hard time keeping his eyes off of her."

cla "Come on, you hot, wonderful, sneak, let's have a nice one-on-one."

scene black with fade

"A few minutes later inside Cla-Min's wagon..."

#CG1
scene black with fade
show rowan necklace happy behind black
show clamin happy behind black

ro "Well, someone is prepared."

cla "I'm always prepared for you."

"She was sitting on Rowan's lap, with both of them inside her caravan on a set of cushions arrayed in a corner. Her other family members weren't around and several incense sticks had been lit on a table nearby."

ro "Do you normally have discussions with people while you're sitting on them?"

cla "Normally? No. Preferably? Yes."

scene cg127 with fade
show rowan necklace happy behind cg127
#clamin naked
show clamin happy behind cg127
pause 3

"The goblin woman put a hand behind her and lifted the band of her top up and over her head, letting her breasts spill forth now that there was nothing to support them. Rowan's breath caught for a moment as he watched them bounce, then he took a deep breath."

cla "Now that's the reaction I was hoping for."

"There was a knowing smile on her face, the short-stack had taken note of the fact that she tended to distract the hero when she moved around."
"Now he was giving her his undivided attention and Min loved it. She grabbed one of his hands and brought it onto her breast."

scene cg128 with fade
show rowan necklace happy behind cg128
#clamin naked
show clamin happy behind cg128
pause 3

cla "Come on, get a nice feel for them. Make sure I've got the goods for your kids."

"With that encouragement, Rowan felt a little dirty as he got a firm grip of her flesh and ample endowments. He suspected that was part of the point."

ro "Can goblins and humans have kids with one another?"

"As he asked, the green woman on top of him busied herself with freeing his cock from his pants. Once his hardening member had been exposed, she looked up at him again, still smiling."

cla "Dunno, but I plan to find something else if the normal way doesn't work."

"One of her legs came up, a bare foot sliding across Rowan's chest, then she brought it back down on the other side so she could slip off her yellow silk pants."

ro "You sure you don't need me to help out, even a little bit?"

"Rowan could feel something hot and wet brushing over his leg as Cla-Min once again moved to be astride him."

cla "As the clan matriarch, I always make sure I'm the one on top at the end of all discussions."

scene cg69 with fade
show rowan necklace happy behind cg69
show clamin happy behind cg69
pause 3

"The goblin pushed her partner back as she rose up, then set herself down onto Rowan's stiff cock. This elicited a sharp gasp as her heat engulfed him."

ro "I see. Didn't take you for someone who'd be that fond of other races."

"She just smirked."

cla "As a secret just for you, I'm not. My pussy has felt non-goblin tongues, but yours is the first outsider's cock. Hmm...."

"She started rising and falling, while squeezing down tightly on her prize."

cla "...but I don't think of you as an outsider. You were born to the wrong family, you're a true goblin at heart."

ro "Gha, whoa. You're real tight."

"As it turned out, goblin women had some really strong muscles downstairs. Cla-Min might not be able to get her arms around Rowan for a bone crushing hug, but she was doing her best to do the same on his shaft."

cla "Don't want you trying to get away, hunny."

"Now the goblin started fucking in earnest, quickly pushing her small body up with her bare feet on the pillows, then letting herself fall back down at full speed."
"Rowan found his eyes drawn once again to her chest and watched those large breasts bounce and spin with her motion."


"Encouraged, he grabbed hold with both hands, using them to feel up those enthralling breasts once again. His lover approved."
"Finally, one more groan of pleasure escaped from Rowan's lips and he bucked against Min's hips, carrying her up into the air for a moment as he let out his seed into her womb. Just as she'd wanted him to."

ro "Hah, hah, you kinda make it hard to hold back."

cla "That was holding back? Goblin guys usually cum in half that time!"

ro "Hmm, normally I think guys would get annoyed for being compared to past lovers, but maybe I should take that as a compliment?"

cla "I think we'll be spending lots of time together, especially if this doesn't take. Who knows, maybe I'll want you to be my favored mate from now on? At the very least, I'm happy to welcome you to the Cla clan with a special gift."

"She slid off of him and happily trotted over to the wagon door."

cla "Come on hero.  I've got a gift for you."

#//End scene, gain Balst's Brand item, but flag that she'll be upset if you lose the item or refuse to have sex with her clan later.
$ set_actor_flag('cla_min', 'rowan_accepted_clamin_s_sword', True)
$ give_item('balasts_brand_gifted')
return

################################################################################

label brotherSwordSex:

"Rowan had been periodically stealing glances at Cla-Bow this whole time, there was some part of him found the goblin man attractive. His gaze had obviously been noted, as Bow stepped forward and ran a hand up and down Rowan's leg."

bow "Come on hero, we both know what you want. You big, beautiful hunk."

#CG1, Cla-Bow posing.
scene black with fade
show rowan necklace happy behind black

"A couple of minutes later, Cla-Min had excused herself and the two men had made themselves comfortable on a set of cushions that had been prepared for them inside the wagon."

bow "My sister had prepared some exotic items for this. I hope you don't mind if I dispense with most of them, not my style you see."

ro "Cla-Min does seem a bit overbearing."

bow "Yeah, let's forget about her for now. She isn't the one you just invited inside for some intimate negotiations about your future in our family. Speaking of which, I want to dispense with dancing around the subject too."

"He smirked and dropped his pants, revealing his semi-erect cock and tight sack."

bow "Let's fuck."

ro "Well you certainly get right to the..."

scene cg89 with fade
show rowan necklace happy behind cg89
pause 3

"As the hero spoke, the goblin popped open a bottle of some kind of ointment and got down on his hands and presented his ass up in the air towards Rowan."

ro "... point. Wow. Are you sure that's how you want to do this?"

"The short man twisted his head around to make eye contact while also starting to work the ointment into his anus, revealing his teeth in a wide grin at the same time."

bow "Hey, I figured that there aren't many guys in the castle who'd be willing to let you pack in their shit. So that's where I come in, or should I say, fill out?"

"He turned back away as Rowan undid his trousers and let his cock slip free, which had straining against its confines for the last minute or so. He'd finished lubbing up now but kept one of his hands back there to hold a cheek open."

bow "Besides, I like being with big studs like yourself. I don't get many chances, but when I do, ohhhh yessss...!"

scene cg90 with fade
show rowan necklace happy behind cg90
pause 3

"He'd slid in easy enough, that ointment worked well, but just how tightly his partner was squeezing down on him was tough to bear."

bow "Come on big guy, pound me."

"The egging on drove Rowan to do just that and he started thrusting in and out hard. Evidently Bow wanted this, so there was no reason to hold back and be soft. This was a romp, a chance to cut loose and just have fun."
"It was exhilarating to fuck a man's ass like this. He might be half Rowan's size, but Bow was a grown adult and his sounds made it clear he was loving every second of this. Evidently he was also adept at pleasing cocks, given how that ring was squeezing and teasing Rowan's shaft."
"In and out, push and pull. This tight muscular backside was a joy to have all to himself. The hero let himself go, giving into the rut and enjoying it as best he could."

bow "Dump everything inside me! Come on, you'll have plenty leftover, give me this load."

#CG2 variation 2, Rowan cumming.
scene cg90 with sshake
scene cg90 with sshake
scene cg91 with flash
show rowan necklace happy behind cg91
pause 3

"With one last growl, Rowan did so. He pushed himself up to the hilt on the goblin and unloaded several sprays of his seed deep inside Bow's asshole. Then he stepped back somewhat unsteadily."
"As the hero's head plopped out with a small strand of semen following it, Cla-Bow reached back and pressed a hand over his ass. He reorientated himself, while trying to hold everything in."

bow "Man, that felt really good. If it isn't too much trouble, I'd like to keep this souvenir for myself. I'll give you a blowjob in a few minutes, after you've had a chance to recover and I've had a chance to clean you off."

ro "Yeah, I think I can manage."

"Once again the goblin man grinned at him."

bow "Then I'll be sure to get sister to give you the promised gift. Maybe you'd like to go again after that? I'm not satisfied yet."

ro "You haven't gotten off yet?"

bow "No, I came three times while you were fucking me. Really, I just want to do it again!"

"Rowan shook his head in dismay."

ro "You're insatiable!"

#//End scene, gain Balst's Brand item, but flag that she'll be upset if you lose the item or refuse to have sex with her clan later.
$ set_actor_flag('cla_min', 'rowan_accepted_clamin_s_sword', True)
$ give_item('balasts_brand_gifted')
return

################################################################################

label clabowTitleGranting:

show rowan necklace happy at midleft with dissolve

ro "I think I could probably pull some strings on your behalf. What sort of a title where you thinking of? If I remember right, Cla-Bow doesn't have any children, does he?"

cla "Oh no, he just likes guys more than girls. That doesn't mean he doesn't have any kids that a nice title might not be passed on to. Anyway, I was thinking that..."

scene bg6 with fade

#if using Jezera favour
if event_tmp['using favor'] == 'Jezera':
    show rowan necklace neutral at midleft with dissolve
    show jezera neutral at midright with dissolve

    ro "... so I thought that would be an appropriate reward for his help."

    show jezera happy at midright

    je "Such a simple thing it is to give a title, just say it and it is. I rather like this system that Solensia has come up with, but she does seem far too stringent with who is honored."
    je "I'll perform the ceremony this evening at supper, please make certain that Cla-Bow is in attendance."

    "Rowan bowed to his mistress."

    ro "Of course."

    je "Will there be anything else?"

    ro "Let me see, domestic fees, new hirings, rewards, no we've covered everything."

    je "Excellent, I believe I will take a bath. Should you need me I will be in my chambers."

    hide jezera with dissolve

#if using favour with Andras
elif event_tmp['using favor'] == 'Andras':
    show rowan necklace neutral at midleft with dissolve
    show andras displeased at midright with dissolve

    ro "... so I thought that would be an appropriate reward for his help."

    an "These goblins are quite the strange sort to be so easily satisfied with words. It's by no means how I would have rewarded him, but if you say so I will agree to it. Inform me when it is time to grant the title and I will do so."

    "Rowan bowed to his master."

    ro "Of course."

    an "Is that everything, servant?"

    ro "Hmm, troop upkeep, recruitment, rewards, yes I believe we've covered all official business."

    an "Good, excuse me."

    hide andras with dissolve

#rejoin
show clamin happy at edgeleft with moveinleft

cla "I would say that went rather well. I'll tell my brother the good news, and you'll have a shiny new sword right after the ceremony finishes."
#End event, gain Cla-Min's item with no strings attached.
$ give_item('balasts_brand')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label helayna_has_been_claimed:
#Helayna has been claimed
#Requirements - Rowan claimed Helayna during assault on Raeve Keep
#High priority event, triggers the week that Helayna was claimed.

scene bg14 with fade

show alexia 2 necklace angry at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

al "Rowan! What is going on? I just saw a naked woman get carried into your room!"

show rowan necklace sad at midleft with dissolve

ro "It was Helayna."

show alexia 2 necklace shocked at midright with dissolve

if (helaynaRelationship == 0):
    al "That noble girl that studied under you a few years back?"

else:
    al "Wait, I remember you telling me about that girl, Duke Raeve's niece was it? Why is she here?"

ro "Yes, that's her. She was corrupted, twisted by Jezera. I protected her from being gangraped, by claiming her as my own."

show alexia 2 necklace happy at midright with dissolve

al "So it isn't what it looks like? She isn't some sex slave for you."

"Rowan found himself freeze up, unable to find the words to answer his wife."

al "That's a relief, I was so worried that-"

ro "Alexia."

"Finally he was able to speak again. The way he said her name silenced Alexia immediately, and a creeping dread began to fill her heart again."

ro "To claim her, I had to do it physically, sexually. Not just because that's what Jezera wanted, but because Helayna had become so crazed that she needed someone, anyone, to fuck her."

"There was no question that this was going to drive a wedge between the two of them, only what form it would take. That all came down to why he'd claimed Helayna for himself."

if (helaynaRelationship == 0):
    menu:
        "A part of Rowan loved Helayna, his best student.":
            $ released_fix_rollback()
            ro "She looked like she was in such pain, someone I'd seen grow under my tutelage into a great young woman. In the moment I needed to make sure that it was me that she gave herself to, not some orc or brute."
            ro "I care about her. I had to protect her."
            show alexia 2 necklace concerned at midright with dissolve
            "For all his noble words, there was one part he left out. Alexia was not to be fooled."
            al "You care about her? Or love her?"
            "Rowan didn’t know how to answer that."
            "A loud cry suddenly came up from inside Rowan's room."            
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "And now you're going to do it again, aren't you? You have to, or it would have been for nothing."
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "Alexia wrapped her arms around her chest while tears streamed down her cheeks."
                al "When I think about all that has transpired since our ordeal began…" 
                "She cut herself off."
                al "I should understand. I should be able to forgive. You were with someone you cared about and you couldn’t control yourself. And yet.."
                al "You’re my anchor and you were sleeping with another woman. Loving another woman. Where’s my anchor now?"
            else:
                "Alexia reached out a placed a hand on his cheek. Tears had started to fall down hers."
                al "My Rowan. My sweet Rowan. What is this place doing to you?"
            #Alexia's relationship with Rowan falls.
            $ change_relation('alexia', -20)

        "Rowan had to protect someone who was in danger in whatever way he could.":
            $ released_fix_rollback()
            ro "I needed to do what I could to save someone, anyone, from what my actions had caused. I'd just helped the twins conquer Reave Keep, I couldn't bear to what what was going to happen!"
            show alexia 2 necklace concerned at midright with dissolve
            "Alexia chuckled softly and sadly."
            al "You’re such a hero. You always have been. More than that, you care about this girl, don’t you? You had to save her, right?"
            ro "Exactly."
            al "But, did you want to fuck with her?"
            ro "What?"
            al "When Jezera told you to sleep her, did you enjoy yourself? Did you want to do it?"
            ro "I had to save her…"
            al "You did. But, sometimes that means you grin and bear it. Something, you tell yourself that you had to, and you really liked it. Did you want fuck her?"
            menu:
                "Yes.":
                    $ released_fix_rollback()
                    "Rowan straightened up his back and looked Alexia in the eyes. The moment she asked the question, he knew the answer. Still, saying it out loud was going to hurt."
                    ro "I think...I think I did...I had to, but you might be right. I might have liked it."
                "No.":
                    $ released_fix_rollback()
                    "Rowan felt caught in a vice. The moment she asked the question, in a moment he instantly understood there was a true answer and one he had to give."
                    ro "No of course. She was my student. I felt like I was violating her."
                    "Alexia studied his eyes closely."
                    al "I don’t believe you."
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "You're even going to do it again, aren't you?  You have to, or it would have been for nothing."
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "Alexia shivered softly and wrapped her arms around her chest."
                al "Look at me, getting worked up over this. I understand the temptations of this place…"
                al "But, you’re my hope. You’re my lodestar. Look what they’re twisting you into."
            else:
                al "Goddess. What are these fiends doing to you? Every day a little piece of you diminishes."
            #Alexia's relationship with Rowan severely falls, Rowan's guilt is reduced slightly.
            $ change_relation('alexia', -10)
            $ change_base_stat('g', -2)

        "Helayna's begging and Jezera's edging was too much to resist.":
            $ released_fix_rollback()
            ro "I didn't want to do it, I wouldn't have done it, but when Helayna started screaming it was me that she called for. She turned to me for help and, I'm ashamed to admit it, but I wanted to take her."
            show alexia 2 necklace concerned at midright with dissolve
            al "Oh Rowan, what have those monster doing to you?"
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "She turned her head to the side, refusing to meet him eye to eye. Then in a soft voice she added a whisper."
                al "What are they doing to us?"
            else:
                pass
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "My love, darling, please. Please don't give into the darkness. Keep your soul, keep your heart.  Please stay my Rowan."
            #Alexia's relationship with Rowan falls slightly, Rowan's corruption increases.
            $ change_relation('alexia', -3)
            $ change_base_stat('c', 2)

elif (helaynaRelationship == 1):
    menu:
        "Rowan had always wanted more than just friendship with Helayna.":
            $ released_fix_rollback()
            ro "She was one of the few nobles that ever cared about me, who ever put herself on the line for my sake. Who I ever cared about in turn. I hadn't forgotten that, and when I was in the moment and saw what had become of her..."
            ro "I had to protect her."
            show alexia 2 necklace concerned at midright with dissolve
            "For all his noble words, there was one part he left out. Alexia was not to be fooled."
            al "You care about her? Or love her?"
            "Rowan didn’t know how to answer that."
            "A loud cry suddenly came up from inside Rowan's room."            
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "And now you're going to do it again, aren't you? You have to, or it would have been for nothing."
            if alexiaJezeraSex == False and alexiaAndrasSex == False:
                "Alexia wrapped her arms around her chest while tears streamed down her cheeks."
                al "When I think about all that has transpired since our ordeal began…" 
                "She cut herself off."
                al "I should understand. I should be able to forgive. You were with someone you cared about and you couldn’t control yourself. And yet.."
                al "You’re my anchor and you were sleeping with another woman. Loving another woman. Where’s my anchor now?"
            else:
                "Alexia reached out a placed a hand on his cheek. Tears had started to fall down hers."
                al "My Rowan. My sweet Rowan. What is this place doing to you?"
            $ change_relation('alexia', -20)

        "Rowan had to protect someone who was in danger in whatever way he could.":
            $ released_fix_rollback()
            ro "I needed to do what I could to save someone, anyone, from what my actions had caused. I'd just helped the twins conquer Reave Keep, I couldn't bear to what what was going to happen!"
            show alexia 2 necklace concerned at midright with dissolve
            "Alexia chuckled softly and sadly."
            al "You’re such a hero. You always have been. More than that, you care about this girl, don’t you? You had to save her, right?"
            ro "Exactly."
            al "But, did you want to fuck with her?"
            ro "What?"
            al "When Jezera told you to sleep her, did you enjoy yourself? Did you want to do it?"
            ro "I had to save her…"
            al "You did. But, sometimes that means you grin and bear it. Something, you tell yourself that you had to, and you really liked it. Did you want fuck her?"
            menu:
                "Yes.":
                    $ released_fix_rollback()
                    "Rowan straightened up his back and looked Alexia in the eyes. The moment she asked the question, he knew the answer. Still, saying it out loud was going to hurt."
                    ro "I think...I think I did...I had to, but you might be right. I might have liked it."
                "No.":
                    $ released_fix_rollback()
                    "Rowan felt caught in a vice. The moment she asked the question, in a moment he instantly understood there was a true answer and one he had to give."
                    ro "No of course. She's my friend. I felt like I was violating her."
                    "Alexia studied his eyes closely."
                    al "I don’t believe you."
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "You're even going to do it again, aren't you?  You have to, or it would have been for nothing."
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "Alexia shivered softly and wrapped her arms around her chest."
                al "Look at me, getting worked up over this. I understand the temptations of this place…"
                al "But, you’re my hope. You’re my lodestar. Look what they’re twisting you into."
            else:
                al "Goddess. What are these fiends doing to you? Every day a little piece of you diminishes."
            #Alexia's relationship with Rowan severely falls, Rowan's guilt is reduced slightly.
            $ change_relation('alexia', -10)
            $ change_base_stat('g', -2)

        "Helayna's begging and Jezera's edging was too much to resist.":
            $ released_fix_rollback()
            ro "I didn't want to do it, I wouldn't have done it, but when Helayna started screaming it was me that she called for. She turned to me for help and, I'm ashamed to admit it, but I wanted to take her."
            show alexia 2 necklace concerned at midright with dissolve
            al "Oh Rowan, what have those monster doing to you?"
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "She turned her head to the side, refusing to meet him eye to eye. Then in a soft voice she added a whisper."
                al "What are they doing to us?"
            else:
                pass
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "My love, darling, please. Please don't give into the darkness. Keep your soul, keep your heart.  Please stay my Rowan."
            #Alexia's relationship with Rowan falls slightly, Rowan's corruption increases.
            $ change_relation('alexia', -3)
            $ change_base_stat('c', 2)

else:
    menu:
        "Rowan had to protect someone who was in danger in whatever way he could.":
            $ released_fix_rollback()
            ro "I needed to do what I could to save someone, anyone, from what my actions had caused. I'd just helped the twins conquer Reave Keep, I couldn't bear to what what was going to happen!"
            show alexia 2 necklace concerned at midright with dissolve
            "Alexia chuckled softly and sadly."
            al "You’re such a hero. You always have been. More than that, you care about this girl, don’t you? You had to save her, right?"
            ro "Exactly."
            al "But, did you want to fuck with her?"
            ro "What?"
            al "When Jezera told you to sleep her, did you enjoy yourself? Did you want to do it?"
            ro "I had to save her…"
            al "You did. But, sometimes that means you grin and bear it. Something, you tell yourself that you had to, and you really liked it. Did you want fuck her?"
            menu:
                "Yes.":
                    $ released_fix_rollback()
                    "Rowan straightened up his back and looked Alexia in the eyes. The moment she asked the question, he knew the answer. Still, saying it out loud was going to hurt."
                    ro "I think...I think I did...I had to, but you might be right. I might have liked it."
                "No.":
                    $ released_fix_rollback()
                    "Rowan felt caught in a vice. The moment she asked the question, in a moment he instantly understood there was a true answer and one he had to give."
                    ro "No of course. She's my friend. I felt like I was violating her."
                    "Alexia studied his eyes closely."
                    al "I don’t believe you."
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "You're even going to do it again, aren't you?  You have to, or it would have been for nothing."
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "Alexia shivered softly and wrapped her arms around her chest."
                al "Look at me, getting worked up over this. I understand the temptations of this place…"
                al "But, you’re my hope. You’re my lodestar. Look what they’re twisting you into."
            else:
                al "Goddess. What are these fiends doing to you? Every day a little piece of you diminishes."
            #Alexia's relationship with Rowan severely falls, Rowan's guilt is reduced slightly.
            $ change_relation('alexia', -10)
            $ change_base_stat('g', -2)

        "Helayna's begging and Jezera's edging was too much to resist.":
            $ released_fix_rollback()
            ro "I didn't want to do it, I wouldn't have done it, but when Helayna started screaming it was me that she called for. She turned to me for help and, I'm ashamed to admit it, but I wanted to take her."
            show alexia 2 necklace concerned at midright with dissolve
            al "Oh Rowan, what have those monster doing to you?"
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "She turned her head to the side, refusing to meet him eye to eye. Then in a soft voice she added a whisper."
                al "What are they doing to us?"
            else:
                pass
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "My love, darling, please. Please don't give into the darkness. Keep your soul, keep your heart.  Please stay my Rowan."
            #Alexia's relationship with Rowan falls slightly, Rowan's corruption increases.
            $ change_relation('alexia', -3)
            $ change_base_stat('c', 2)

"Another loud cry of frustration filled the air from Rowan's chamber."

ro "Alexia, I need to go to her.  If I don't, she'll probably go find someone or something else to try and deal with her uncontrollable lust."

#If Alexia was sleeping in Rowan's room, she tells him that she's moved out.
if not alexiaSeparateRoom:
    al "Then I'm going to move out. I don't want to see Helayna, I don't want to see you breaking our vows with her, even if it is to protect her. I'm sorry, darling."
    #Alexia is set to be sleeping separate.
    $ alexiaSeparateRoom = True

#rejoin
al "Go, deal with Helayna. I need some time to myself right now."
$ rowan_shares_room_with_helayna = True

#Helayna Sex
scene bg9 with fade
show helayna naked aroused at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "Hello Helayna."

"Rowan entered into his room and found Helayna sprawled out on his bed, furiously fisting her womanhood in a desperate effort to get off. When he spoke to her, she froze up for a second and then started frantically looking around the room to find him."
"When she did, her unfocused eyes seemed to clear for a moment and she cried out."

hel "Rowan!  My [helaynaTitle]!  Please, please help me...."

"Then she once again became unfocused. She reorientated herself, presenting her puffed up womanhood to him as it drooled down onto his blankets incessantly."

hel "I... I need you inside me, I need you to fuck me, again and again...."

ro "It hurts to see you like this, you aren't yourself."

"In spite of his words, the hero was getting aroused at the display. Jezera wasn't here to egg him on this time, but there was no denying that some part of him wanted to claim Helayna again. He only hoped that he wouldn't be corrupted to his core by that part of him."

show rowan necklace naked at midleft with dissolve

"The hero shed his clothing and stepped towards Helayna as she mewled in excitement."

hel "Yes! Come to me! Fill meeee!"

ro "You might not understand me now, but know that I do this to protect you from yourself."

#CG1, Rowan fucking Helayna
scene cg112 with fade
pause 3
"As he said that, he climbed up onto the bed. A moment later, he was in position to start fucking her. He hesitated for a moment, letting his hand run over Helayna's smooth skin and over the shape of her soft cheeks and curve of her breasts."
"This wasn't for Helayna, it was for him. The fallen noblewoman only wanted him to fuck her, hard and fast. That's why, after that moment ended, he took her as she wanted, no needed, him to do."
"A loud cry of pleasure erupted as Rowan penetrated Helayna for the second time. Her passage was well and truly soaked, and it quivered and tensed around the man's shaft uncontrollably."
"He didn't wait for her to adjust to his violation of her, there was no need, instead Rowan just bucked against her body, making a loud wet slapping as their hips met again and again. Each of his thrusts was met by another sharp gasp or babble from Helayna."
"Soon the sensations were too much to her and her eyes rolled back in her head. Knowing that the worst thing he could do now was slow down, or worse - stop, the man took a firm grip of the woman's hips, grit his teeth, and kept fucking her."

#CG1 variation - cum
scene cg112 with sshake
scene cg112 with sshake
scene cg113 with flash
pause 3
"The frantic pace meant that orgasm would come swiftly, though Rowan grit his teeth through it and kept fucking Helayna right through it, in spite of his discomfort. One time wouldn't be enough for her, he needed to keep going and going until her fire was at least partially quenched."

#CG1 variation - super cum
scene cg113 with sshake
scene cg113 with sshake
scene cg114 with flash
show rowan necklace naked behind cg114
show helayna naked aroused behind cg114

"After cumming inside her three more times, and leaving quite a mess, Rowan was finally unable to go any more. Helayna seemed to want more afterwards, but didn't sound quite so desperate."
"Hopefully she'd be satisfied for now and wouldn't have to seek out help from someone else in the castle. The hero shuddered at the thought."

ro "I wish I could do more for you. Will you be able to last a week while I'm away though? Can I really just leave you in here?"

hel "Rowan... it's fine. As long as I know you'll come back to me, I can last."

"Something of her seemed to have surfaced, maybe Helayna was still in there, deep down?"

ro "I hope so. I'll watch over you whenever I can, whenever my duties don't take me away from you. It's the only way I can protect you."

hel "Thank you, thank you. I will do what I can to help, I'm still a knight."

ro "(Oh Helayna....)"

#Rowan gains corruption.  End scene.
$ change_base_stat('c', 2)

if NTR == True:
    jump AfterArgument
    
else:

    return

label AfterArgument:
    
scene bg7 with fade

show alexia 2 necklace concerned at midright with dissolve

al "(I can’t believe Rowan would do this to me. It is one thing to be unfaithful, but to bring this woman into our bed?)"

"The redhead had only recently managed to stop herself from crying, despite the argument with her husband happening hours ago. She now found herself back on the verge of tears."

al "(I know he was only trying to protect her, but could he really not see how that would hurt me?)"

play sound "music/SFX/door knock.ogg"
pause 1

"Her thoughts were interrupted by a knock at the door. Who could it be? Had Rowan come to apologize for the events earlier? Probably, but she wasn’t ready to see him, she was still too raw, and already felt as if she were about to start bawling again."

play sound "music/SFX/door knock.ogg"
pause 1

show andras happy behind bg7

an "Hello? Alexia? It is Andras, I just wanted to check that you are okay."

menu:
    "Don’t answer the door.":
        $ released_fix_rollback()
        "The demon must have taken the hint because he left without any further prodding. Alexia was glad, as she didn’t know if she could deal with him and whatever nonsense he was up to in her current state."
        "Still trying not to cry she lay on the bed, closed her eyes, and tried not to think about anything."
        return
        
    "Answer the door.":
        $ released_fix_rollback()
        show alexia 2 necklace concerned at edgeleft with moveoutleft
        "She opened the door just enough to converse, but not enough for it to seem inviting. The demon stood there, waiting, with a smile on his face."
        al "What do you want Andras? I’m not in the mood."
        an "So I hear, I just wanted to drop by and make sure you were okay, as I said."
        al "I’m {i}sure{/i} you did."
        an "And what is that supposed to mean?"
        al "If you cared about my well being, you wouldn’t have kidnapped me in the first place." 
        an "Did we lock you up in the dungeons? Have you been harmed in any way?"
        al "No, but-"
        an "Have you been forced to do anything against your will?"
        al "I suppose not…"
        an "I take time out of my busy schedule to come and check on you, because I’ve heard you were upset, and this is what I get?"
        al "I’m sorry, I’ve just had a rough day."
        an "It is perfectly fine, there’s no need to apologize. Anybody would be upset in your position, and if lashing out at me makes you feel better, I don’t mind."
        al "No, I shouldn’t be taking it out on you. You aren’t the one who has done anything, so it isn’t fair to you."
        an "Would you like to talk about it?"
        menu:
            "Yes.":
                $ released_fix_rollback()
                jump argumentSexScene
                
            "No.":
                $ released_fix_rollback()
                al "Thanks for the offer, but it is has been a long day, and I just need to rest."
                an "Okay, I won’t push you. If you ever want to talk about it, let me know. I’ll let you rest."
                al "Thank you Andras, and sorry again."
                an "Think nothing of it."
                "The demon left, and Alexia lay on the bed, closed her eyes, and tried not to think about anything."
                return
            
label argumentSexScene:

al "It is very kind of you to offer. I think it might help, please, come in."

scene black with fade
scene bg7 with fade
show andras happy at midleft with dissolve
show alexia 2 necklace happy at midright with dissolve

an "… and then the maid fell backward, and the chamberpot went flying, hitting Jezera. I thought she was going to skin the poor woman alive, but she just screamed and ran off."

"A loud giggle escaped from the mouth of the redhead."

al "I can’t really imagine Jezera as a girl, I suppose you don’t really think of demons being children."

an "Probably for the best, she was worse than she is now!"

"Alexia giggled again, before stopping herself."

al "Now, that is not a very nice thing to say about your sister."

"The demon pulled a purposely exaggerated face to feign exasperation, before a smile returned to his face."

an "I’m sure she’d be happy to know she has such a staunch defender."
an "Anyway, it has gotten quite late and this bottle is empty, I should let you get your beauty sleep."

"The demon stood, empty bottle in hand."

an "I hope I was able to cheer you up a little, or at the very least take your mind off your troubles for a little while"

scene cg20 with fade
show andras happy behind cg20
show alexia 2 necklace happy behind cg20
pause 3

"She stood now, to thank him."

al "Thank you Andras, it did help. Sometimes you just need a laugh, I think."

an "If you ask me though, I think your husband is a fool."

if all_actors['alexia'].flags['andras_influence'] > 0:
    jump argumentSex1

else:
    scene bg7 with fade
    show andras happy at midleft with dissolve
    show alexia 2 necklace happy at midright with dissolve
    al "You’d better go now, I need to lie down."
    an "Okay. Goodnight Alexia."
    al "Goodnight."
    hide andras with moveoutleft
    return
    
label argumentSex1:
    
scene cg21 with fade
show andras happy behind cg21
show alexia 2 necklace happy behind cg21
pause 3 

"She didn’t know if it was the alcohol, the fact he was being so nice to her, or even subconscious anger at Rowan for his actions earlier, but now face to face with the demon she leaned in."
"First their lips met, and then she opened her mouth to allow his tongue to make it’s forceful entry."

scene cg553 with fade
show andras happy behind cg553
pause 3

"Andras sat down on the bed, and pulled the much smaller woman down onto his lap with ease. The movement was strong and forceful, completely different from how her husband treated her; almost as if he were moving an object and not a person."
"Now, facing him, she resumed french kissing him. His mouth was hot and still tasted of wine, and their tongues pressed together, snaking side to side as saliva co-mingled."
"It was almost as if she were lost in a haze, until she felt that the demon’s substantial member had awoken and was pressing against her."

if all_actors['alexia'].flags['andras_influence'] > 1:
    jump argumentSex2

else:
    scene bg7 with fade
    show alexia 2 necklace concerned at midright with dissolve
    show andras happy at midleft with dissolve
    al "No, I can’t. Andras, please stop."
    an "Are you sure?"
    al "Yes, please… I’m just upset, and a little drunk."
    an "Okay then, I’ll leave you be."
    al "Thank you. I’m sorry, I’m just not feeling like myself."
    an "Say no more."
    hide andras with moveoutright
    "The demon left, and Alexia lay on the bed, closed her eyes, and tried not to think about anything."
    return

label argumentSex2:

an "Turn around."

#Alexia on Andras lap, reverse cowgirl (crotch to crotch), Andras gropes her breasts 
scene black with fade
show andras happy behind black
show alexia 2 necklace aroused behind black

"The redhead did what he said without reply, and now sat with her back against his chest. He reached down with one clawed hand and roughly groped her breast, causing her to let out a soft moan."
"Happy with the reaction, he ran his hand over her erect nipple, teasing her by lightly grazing it."
 
al "No fair…"

"As a response to the lack of stimulation, Alexia began to grind on the demon’s lap, her sodden cunt rubbing against his hard cock through her soaked panties."

#neck kiss variant
scene black with fade
show andras happy behind black

"Andras leaned in and began to softly kiss her neck, while continuing to grope her breasts."
"As he pinched her nipple, she let out a sharp cry, and increased her grinding to almost a bucking, trying to get off from the friction between their loins."

an "Take off your panties."

if all_actors['alexia'].flags['andras_influence'] > 3:
    jump argumentSex3

else:
    scene bg7 with fade
    show alexia 2 necklace concerned at midright with dissolve
    show andras happy at midleft with dissolve
    al "No, I can’t. Andras, please stop."
    an "Are you sure?"
    al "Yes, please… I’m just upset, and a little drunk."
    an "Okay then, I’ll leave you be."
    al "Thank you. I’m sorry, I’m just not feeling like myself."
    an "Say no more."
    hide andras with moveoutright
    "The demon left, and Alexia lay on the bed, closed her eyes, and tried not to think about anything."
    return

label argumentSex3:

scene cg115 with fade
show andras happy behind cg115
show alexia 2 necklace aroused behind cg115

"Again she complied with his order without a reply, she was desperate to get off now, and damn the consequences! She quickly whipped her underwear off, and the demon slid one of his hands down to her wet snatch."
"Without waiting on ceremony, he inserted two fat fingers into her and began to slowly frig her."
"Due to his abnormal size, it was like being fucked by an average size cock, and she let out a long moan as the slippery fingers slid in and out between her lips."

al "uhhhhh…"

"Andras grinned, and began to speed up, causing her moans to grow louder and longer."
"He slipped in a third finger, stretching her cunt, to which she gave a squeal of approval, and began to make come hither movements, stimulating her g-spot."
"Before long, she couldn’t take anymore."

al "Nnnnnn!! Oh gods, I’m going to cum!"

scene cg115 with sshake
scene cg115 with sshake
scene cg116 with flash
show alexia 2 necklace aroused behind cg116

"Deftly he quickly removed the fingers, and began to rub her clit. The stimulation was almost too much for Alexia, she felt as if she were going to go crazy."
"It didn’t take long for her to climax, and as she did she let out a scream, and squirted. A stream of clear liquid arced through the air, as she slumped back against the demon’s muscular chest, exhausted."

al "Wow, that’s never happened before…"

scene black with fade
"Suddenly tired, she closed her eyes. Sometime afterwards, she felt strong arms pick her up and lie her on the bed. She felt the wet brush of lips against hers, before she drifted off to sleep."

$ alexiaUnfaithful = True
$ alexiaAndrasSex =+ 1
$ all_actors['alexia'].corruption += 3
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label delf_dipping:
#Delf Dipping
#Pre requisites - Breeding pit / met Draith
#should probably occur within a few weeks of building

scene bg25 with fade

"Whilst doing his regular rounds about the castle, Rowan heard raised voices from the breeding pits. He didn't have to draw too close to recognise the female party: Jezera, in full, strident form."

show jezera displeased at midright with dissolve
show draith neutral at midleft with dissolve

je "...not good enough. We give you shelter and succour, more than a male dark elf deserves, and you repay us with laziness and insubordination! Where are my legions of wargs, worm?"
je "Where are the vast kennels of driders that you promised us?"

show rowan necklace neutral at edgeleft with moveinleft

"Rowan entered the main chamber to find Draith stood on the viewing dais, wringing his hands, staring at a floor he clearly wished would swallow him up. Jezera had one hand on her hip, the other waving disgustedly at the mostly empty pits."

dra "S-sorry, Mistress. I... I did say it was going to take time..."

je "If I had a piece of gold for every time I heard that, I could have bought the six realms by now! You will work your snivelling little ass off every hour of every day from now on, or by my own father I shall march you back to the Undersisters myself!"

ro "That's enough. What is to be gained from yelling at him like that?"

je "Huh? Oh, it's you. Well, of course {i}you{/i} would encourage such weakness. Go ahead Rowan, coddle the sissy. Ultimately it will be you who will be paying for his failures!"

hide jezera with moveoutright

"Jezera strode out of the room, leaving Rowan alone with the lithe, dusky male."

dra "Th- thank you. I hate it so much when she shouts at me. It makes me remember how - how it was in Cerandil. Th- the cold... the morning shriek and the bite of the whip..."

ro "Are you taken back to that whenever anybody gives you orders?"

dra "Oh no! When you do it, it feels good. Your voice is so kind and- and warm. And strong. Like the person it comes from."

"The dark elf had drawn closer to Rowan as he talked, as if the human was indeed a source of warmth in this dank underchamber. His hairless, delicate face shone with naked adoration."

menu:
    "Fuck him.":
        $ released_fix_rollback()
        $ rowanGaySex += 1
        "Had Rowan ever felt attracted to males before the demons installed him here? He couldn't recall any occasion when he'd looked at another man's body and felt heat draw inexorably into his crotch like it did now, certainly not when he had been in Rosaria's service."
        "But the dark elf was so lithe, so delicate in appearance, so sultrily exotic in dress and shade, that to compare him to a fighting human male such as himself seemed ridiculous."
        "And when Rowan looked into Draith's eyes and saw the naked hero worship and arousal that shone there, the temptation became far too much."
        "He stepped forward and drew the little guy into his arms commandingly. Draith gave a short gasp, giddy joy flickering in his tone as Rowan nakedly enjoyed the supple feel of the elf's flesh, plaining his hand down his slim back."
        ro "You belong to me, beastmaster. Not the Undersisters; not the demons. Me, and me alone. So pay no attention to them. Understand?"
        dra "I - yes, sir. Absolutely."
        "Draith exhaled, moulded his frame into Rowan's as the human's touch roamed down further, squeezing his delightfully pert ass."
        dra "I- I'm very good with all sorts of beasts, master. Perhaps there's one in particular you'd like to show me?"
        "Rowan laughed at this, making purple bloom over Draith's china-bone cheeks. Still, he stepped away from the dark elf and stepped out of his clothes, ripping away his breeches to allow his thick, hot erection to loll outwards, never taking his eyes off the subby, smaller male."
        dra "Yes... I think I might have something for a big, powerful monster like that."
        "He turned, deliberately flaring his narrow hips in order to swing his cute apple-shaped backside over to a bottle-cluttered shelf above his desk. He withdrew a vial filled with clear fluid, removed the stopper and pooled the unguent onto his hands, rubbing it into his palms."
        "Heart beating, Rowan sat himself down on a bench and opened his thighs. Draith smiled at him shyly as he slowly descended onto his knees in front of the human."
        "Rowan sighed, and then groaned with pleasure as the dark elf wrapped his fingers around the human's cock, slithering his slender grip up and down his shaft, working the warm, coating oil into it until it was hard as oak and sang with pleasure."
        "Draith smiled and laughed, eyes darting up to Rowan's face and then batting submissively away again every time he drew a gratified sound out of the human; the act of giving pleasure seemed to give him genuine pleasure as well."
        "Lust throbbed through Rowan, enflaming his senses as the dark elf slid the long, nimble fingers of one hand in deeper, jerking his cock assiduously whilst cupping his balls, polishing every inch of Rowan's sex in warm, slick oil."
        scene cg556 with fade
        #draith aroused
        show draith happy behind cg556
        pause 3
        "Feral lust gripping him now, Rowan rose up and grabbed the smaller male, turning him around and bending him over the bench, drawing a surprised squeal out of the submissive."
        "He pulled Draith's tight-fitting breeches down and admired his pert, naked ass for a long moment, slapping his urgently erect, oil-soaked cock between its crack as he did. Draith looked at him over his shoulder, color high in his cheeks."
        dra "Please go slow first, sir... then hard."
        "Rowan drew his hips back, allowing his erection to slither downwards meaningfully, lining himself up with Draith's cute little rose, enjoying the twitch and expectant inhalation it brought out of the dark elf."
        "Then he pushed forward, slowly penetrating it, gloving his cock-head in wonderful, clinging warmth, carefully working him loose with slow movements of his hips."
        "Draith gasped and clutched at the wood beneath him, a chorus of cute little grunts and huffs... but he never bade Rowan to stop."
        "Soon the human found himself easily sliding his length deep into the elf's tight tunnel."
        "Draith's own cock, as slender and cute as its owner, jerked in response to Rowan's efforts, wagging like a puppy's tail as the human pushed himself home into the boy-slut's tight, oiled warmth again and again."
        "Genuine excitement and slight giddiness energised Rowan; he was a complete novice to this, but his roughness seemed only to excite the dark elf, moaning at him to keep going, pulling Rowan’s hand to his flat chest and small, erect nipples."
        scene cg72 with dissolve
        pause 2
        "Animal lust overcame Rowan, and he suddenly grabbed Draith around the hips, hoisted him into the air and then firmly sat him down on his cock, thrusting into the dark elf’s opened asshole from below."
        scene cg73 with dissolve
        pause 2
        show cg73 with sshake
        show cg73 with sshake
        show cg74 with flash
        pause 2
        show cg74 with sshake
        show cg74 with sshake
        show cg75 with flash
        pause 2
        show draith happy behind cg75
        "Draith cried out with joy, slim arm thrown around Rowan's neck, his own dick gleefully erect, his tone of ecstasy climbing down to a coo of deepest satisfaction when the bigger human came with spectacular force, fluming a guttering fountain of cum deep into his gaping hole."
        "The dark elf's fingers curled up his shoulder, his silky hair tickling Rowan's jaw, nuzzling him happily."
        dra "I hope you will come by often, sir. A big, energetic beast like that needs a lot of care... and there's nobody better trained to give it than me."
        "With his impulsive ardour bitten, Rowan's thoughts now sank back to Alexia, somewhere in this very keep and blissfully unaware that her husband had just cheated with another man."
        "Still, he did not betray his feelings of guilt and uneasiness to Draith, who stroked his arm trustingly as the human dressed and departed."
        scene bg14 with fade
        show jezera happy at midright with dissolve
        show rowan necklace neutral at midleft with moveinleft
        je "Oh, Rowan..."
        "That taunting, teasing voice froze Rowan in the corridor cold. He slowly turned to face the female demon, leaning against the wall outside the dungeon he'd just exited."
        ro "What are you doing? Were you listening in?"
        je "Of course! I didn't set that succulent little twink to all but fall into your arms just to miss you fucking him senseless. Mmm... I must say Rowan, beneath that dour exterior of yours, you are quite the surprise."
        je "So passionate and impetuous and energetic. You need to let that side of you come out more often."
        ro "...you were cruel to Draith just so I would be nice to him."
        je "Of course! I wouldn't be nasty to that slutty piece of violet sweet for no reason. Who do you take me for, my brother? But I couldn't have done it if you didn't already have the lust for it."
        je "Two handsome boys rutting each other for my entertainment... it was even better than I was anticipating."
        "She slid her claws along the insides of her thighs, sighing with contentment."
        je "I will remember this, Rowan. Those who entertain me are richly rewarded... in all sorts of ways."
        hide jezera with moveoutright
        "She left with a malicious titter. Waves of conflicting emotion washed through Rowan. The guilt he'd felt for cheating on Alexia was all the more gnawing for the knowledge that Jezera had deliberately set him up to it."
        "On the other hand... the sex had been undeniably good, and it had  certainly comforted that sensitive little beastmaster of his. And perhaps this favour he had inadvertently earned off Jezera could be turned to good purpose?"
        #gain small guilt amount of guilt, gain Draith relationship, +1 Jezera favour
        $ change_base_stat('g', 1)
        $ change_relation('draith', 3)
        $ change_favor('jezera', 1)
        $ rowan_draith_sex = True
        return

    "Give him a manly hug.":
        $ released_fix_rollback()
        show rowan necklace happy at edgeleft with dissolve
        "Rowan strode across and gripped the slight dark elf firmly in his arms, clapping him on the back a couple of times. He hoped with each strong slap he made crystal clear that brotherly, lordly affection was what was being expressed here."
        ro "You are my subject. Not the Undersisters; not the demons. Pay no attention to them - I know you have the potential to be a great beast-master, given enough space and time. I shall see to it that you have both."
        "Draith hugged him back tightly. Rowan presumed the message had gotten through - at least for now - because this time the supple little guy made no attempts to unsubtly hump him."
        show draith happy at midleft with dissolve
        dra "Thank you, sir. As long as you're - you're around... my hands won't shake. I'll do my best to fill these pits with creatures loyal to your name... and your name only."
        hide rowan with moveoutleft
        "Draith smiled at him shyly as Rowan released him and strode out of the Breeding Pits."
        scene bg14 with fade
        show jezera displeased at midright with dissolve
        show rowan necklace neutral at midleft with moveinleft
        je "Hell and beyond Rowan, are you always this boring?"
        "That taunting, teasing voice froze Rowan in the corridor cold. He slowly turned to face the female demon, leaning against the wall outside the dungeon he'd just left."
        ro "What are you doing? Were you listening in?"
        je "Of course! I'd set that succulent little twink to all but fall into your arms... I was sat here waiting to lap up you two getting hot and heavy with each other... and what to do you do? Spurn the opportunity!"
        je "When are you ever going to loosen up some, you sexless grump?"
        ro "...you were cruel to Draith just so I would be nice to him."
        je "Yes! I wouldn't be nasty to that slutty piece of violet sweet for no reason. Who do you take me for, my brother? Pshh, but it was all for naught, thanks to you. I'll have to find some other form of entertainment."
        je "I wonder what your wife is up to?"
        ro "Stay away from her!"
        hide jezera with moveoutright
        "The female demon tittered, a sly, lingering look her only response as she slinked off."
        "Rowan was left feeling conflicted - he felt glad that he'd extended kindness to his dark elf servant and foiled Jezera's perversions, but inadvertently getting into the demon’s bad books did not bode well."
        #Guilt slightly down, small increase to Draith relationshop, -1 Jezera favour if possible
        $ change_base_stat('g', -1)
        $ change_relation('draith', 2)
        $ change_favor('jezera', -1)
        return

    "Tell him to stand up for himself.":
        $ released_fix_rollback()
        ro "Draith, I'm not always going to be around to stop others picking on you. You're not a slave to the Undersisters anymore, but nobody in this castle suffers the weak. Frankly, you're going to have to grow a harder skin if you're going to be one of my taskmasters."
        ro " Tell Jezera, and Andras for that matter, to get gone if they talk to you like that. If they have a problem, they can take it to me."
        "Draith looked thoroughly miserable, and Rowan didn't like the way he shrank away and wrung his hands in the exact same way he had when the demon had been bad-mouthing him."
        "Still, once Rowan had finished, the dark elf set his delicate jaw and made an effort to look his commander in the eye."
        dra "I understand, s-sir. I'll do my best to let them know they can't- can't talk to me that way."
        hide rowan with moveoutleft
        "Rowan gave him a firm nod, and strode out of the Breeding Pits."
        scene bg14 with fade
        show jezera displeased at midright with dissolve
        show rowan necklace neutral at midleft with moveinleft
        je "Hell and beyond Rowan, are you always this boring?"
        "That taunting, teasing voice froze Rowan in the corridor cold. He slowly turned to face the female demon, leaning against the wall outside the dungeon he'd just left."
        ro "What are you doing? Were you listening in?"
        je "Of course! I'd set that succulent little twink to all but fall into your arms... I was sat here waiting to lap up you two getting hot and heavy with each other... and what to do you do? Spurn the opportunity!"
        je "When are you ever going to loosen up some, you sexless grump?"
        ro "...you were cruel to Draith just so I would be nice to him."
        je "You weren't nice to him at all! Being nice to that slutty piece of violet sweet would have been to give him the good, hard ass-fucking he was practically begging for. And you've managed to disappoint us both, because now I'm going to have to find some other form of entertainment."
        je "I wonder what your wife is up to?"
        ro "Stay away from her!"
        hide jezera with moveoutright
        "The female demon tittered, a sly, lingering look her only response as she slinked off."
        "Rowan scowled. Somehow, an honest attempt to get one of his servants to stand on his own two feet and gone very badly indeed."
        #-1 Jezera favour if possible
        $ change_favor('jezera', -1)
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label greyhide_s_table_manners:
#Greyhide's table manners
#Follow up from Drinking Buddies if player chose to introduce Greyhide to Alexia, and if Alexia and Greyhide have not met before.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with dissolve

"Jezera had a look on her face that could only mean trouble. It was the kind of sinister smirk she wore when she was thinking of something devious."

show rowan necklace angry at midleft with dissolve

ro "Jezera, are you even paying attention?"

show jezera displeased at midright with dissolve

je "Of course I am."

show rowan necklace concerned at midleft with dissolve

ro "You just seem… distracted."

je "My apologies if the mundane matters my castellan brings before me causes the mind to wander."

show rowan necklace angry at midleft with dissolve

ro "We don’t have to deal with this right now if you’re not in the mood."

show jezera happy at midright with dissolve

je "Come now, hero: no need to sport such a sour frown. Have you anything interesting to report?"

show rowan necklace angry at midleft with dissolve

ro "Nothing else really springs to mind."

show jezera neutral at midright with dissolve

je "What of our new Forgemaster?"

show rowan necklace concerned at midleft with dissolve

ro "...Greyhide?"

show jezera happy at midright with dissolve

je "Oh, is that his name? How quaint."
je "Rumour has it you two were seen getting drunk together on the castle walls."

ro "I assure you my Lady, it was only for an evening. I had already finished the tasks for the day and-"

show rowan necklace neutral at midleft with dissolve

je "Now now, Rowan. I don’t begrudge you your fun. By all means: indulge yourself!"
je "As a matter of fact, I’m delighted you’ve taken an interest in making new friends in the castle. It means you’re finally putting down roots."

show rowan necklace concerned at midleft with dissolve

ro "If you say so."

je "He’s a big fellow, isn’t he?"

show rowan necklace angry at midleft with dissolve

ro "Most Minotaurs are."

show jezera displeased at midright with dissolve

je "There you go again with that sour frown of yours."

show jezera happy at midright with dissolve

je "Tell you what: to prove my magnanimity I grant you the evening to yourself. Spend it as you will!"

show rowan necklace concerned at midleft with dissolve

ro "I..."

show rowan necklace neutral at midleft with dissolve

ro "Thank you, my Lady."

je "There’s just one condition: you and your lovely wife should spend it with your new friend."

"Rowan’s hackles rose. Her rapidfire shifts in topic were giving him mental whiplash."

ro "Why?"

je "Why else? Because it amuses me."
je "Of all the people you could have struck up a friendship with, you chose a bull man who forges weapons of war."
je "The very idea of it is humorous to me! I’m interested in seeing where this all leads."

"Jezera leaned back in her throne, waving Rowan off in curt dismissal."

je "If I have any further need of you, I will call."
je "That will be all for today, Rowan."

scene bg9 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace concerned at midright with dissolve

al "An evening with Greyhide?"

ro "That’s what Jezera said."

show alexia 2 necklace happy at midright with dissolve

al "Well, that doesn’t sound so bad. He’s a pleasant enough person. I wouldn’t mind getting to know him a bit better."
al "Oh! Rowan, what if we all had dinner together? Just the three of us."
al "We could ask the cooks to prepare a vegetarian meal for him, make an evening of it!"

show rowan necklace concerned at midleft with dissolve

ro "Are you sure about this?"

show alexia 2 necklace neutral at midright with dissolve

al "It’s been too long since we had a real night together, Rowan."

show alexia 2 necklace concerned at midright with dissolve

al "...From what little he’s told me, it sounds like Greyhide has led a difficult life."

ro "Yeah. That he has."

show alexia 2 necklace happy at midright with dissolve

al "Then maybe he’s due for a fun evening as well. Does he even have any other friends at the castle?"

show rowan necklace neutral at midleft with dissolve

ro "None that I’m aware of."

al "Then we can be his first."

show rowan necklace happy at midleft with dissolve

ro "You know what? Sure, let’s do it. I’ll make the arrangements."

al "It should be a fun night!"

scene cg105 with fade
pause 3

"...Things weren’t going quite as Alexia had expected."
"It had begun amiably enough: happy introductions and pleasant greetings were exchanged, as the bull - fresh from the forge - wiped the soot from his apron and took her hand in his massive mitt in greeting."
"But no sooner had Greyhide taken his seat at the table, than things took a turn. He began to eat." 
"Though... “eating” was a kind way to put it. He {i}gorged{/i} himself, grabbing large chunks directly out of the salad bowls around him and stuffing them into his mouth."
"He didn’t even bother with a plate or utensils, shoveling handfuls of lettuce and carrots and other vegetables wholesale into his yawning gullet. He didn’t eat fast, but he was efficient."
"Alexia was appalled. She’d never thought of herself as a stickler when it came to food etiquette - goodness knows Rowan himself could be a handful at times - but this was another thing entirely."
"So caught up was Alexia in the disgusting display, that she didn’t even notice Rowan politely ask her to pass him the water until he was all but yelling in her ear."

show rowan necklace neutral behind cg105

ro "Alexia? "

show alexia 2 necklace angry behind cg105

al "..."

show rowan necklace angry behind cg105

ro "{i}Alexia?{/i}"

show alexia 2 necklace shocked behind cg105

al "{i}Ah{/i}! What? What?"

"At this point, Greyhide also noticed that the red haired woman was staring at him. He swallowed the latest mouthful, then spoke."

show greyhide neutral behind cg105

gh "Is there something troubling you?"

al "No, of course not! I just, uh-"

"Across the table, on the other side of Greyhide’s bulky form, Rowan was smirking. He knew {i}exactly{/i} what was bothering her! Desperate to avoid the awkward topic, Alexia changed the subject."

show alexia 2 necklace concerned behind cg105

al "Um… how is the meal?"

gh "Quite good, a very hearty feast! I am touched that you remember my diet."

show rowan necklace happy behind cg105

ro "Well, it wouldn’t look good on us as hosts to serve you raw steak, now would it?"

"Alexia shot a subtle death glare in the direction of her husband. Rowan simply laughed."
"Far from being insulted by the jab, Greyhide chuckled."

gh "Please do not do that. The whelp would never let me hear the end of it."

al "The whelp?"

gh "Ah, I apologize. Sometimes I forget whose castle this is."
gh "You know him as Andras. "

"Alexia shared a look with her husband. Greyhide had just called their demon master a {i}whelp{/i}. The bull’s deadpan delivery elicited shocked laughter from the both of them."

show alexia 2 necklace shocked behind cg105

al "W-why do you {i}call{/i} him that?"

gh "It was the only name I could think of at the time."

ro "And your first instinct was “whelp?”"

gh "Heh. It was."
gh "We met years ago, after he showed up one day at my old forge. He wanted to know how I made my weapons."
gh "He was as brash then as he is now, only smaller. Like a little dog."

"Rowan grinned from ear to ear. Alexia had to cover her mouth with a napkin to hide her uncontrollable giggles."

show alexia 2 necklace happy behind cg105

al "Why do you still call him that?"

gh "Why not?"

show rowan necklace neutral behind cg105

ro "Well, for one thing: you work for him."

gh "I’ve known him for too long to think of him as anything else. He is still a whelp."

al "Is {i}everyone{/i} at the castle “little” to you?"

gh "For the most part."

al "Just don’t start calling me whelp and we’ll be fine."

gh "You are smaller than most, little one."

show rowan necklace happy behind cg105

ro "I think we found a new nickname!"

show alexia 2 necklace angry behind cg105

al "{i}Hey!{/i}"

"Laughter circled the table like a welcome guest. Greyhide returned to loudly munching on his meal, a broad smile on his lips. The tension in the room had been utterly broken."
"The jovial atmosphere was ended soon after, however. Rowan’s features sharpened. His hand went instinctively to the amulet around his neck. His brow furrowed."

show rowan necklace angry behind cg105

ro "Really? Now? But you said-"

"Rowan trailed off into silence as Alexia and Greyhide shared a look."

ro "You were the one who gave me the night off. Are you {i}certain{/i} this can’t wait until tomorrow?"

"A longer silence. Alexia’s mood fell as she looked upon Rowan’s deepening frown. They’d all been having such fun together!"

ro "Very well. I’ll be there immediately."

"As Rowan rose from his seat, his two companions made to rise as well. Rowan waved them back into their chairs."

show alexia 2 necklace concerned behind cg105

al "Is something wrong?"

show rowan necklace neutral behind cg105

ro "A minor matter, but it cannot wait."

gh "Is it the whelp?"

show rowan necklace happy behind cg105

ro "Heh, no. Jezera."

al "Will it take long?"

show rowan necklace neutral behind cg105

ro "Hopefully not, but it’s hard to say. I might be a few hours."

al "Oh..."

show rowan necklace happy behind cg105

ro "Hey, don’t end the evening on {i}my{/i} account. If all goes well, I’ll be back before the meal is finished."

al "Okay… hurry back."

gh "Be well, Rowan."

ro "Take care of my wife while I’m gone, will you?"

gh "Of course. You have my word."

scene bg27 with fade
show alexia 2 necklace concerned at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve

"An awkward silence filled the room. Despite the earlier jovial atmosphere, Alexia found herself uncertain of what to say."
"It was only after a long moment of staring at her food that she noticed Greyhide had stopped eating and was looking at her."

gh "You are quiet. Have I said something wrong?"

al "No Greyhide. Sorry, I’m being rude."

gh "Silence is not rudeness. It is just silence."
gh "...Do I frighten you?"

menu:
    "Yes.":
        $ released_fix_rollback()
        "Alexia bit her lip and nodded."
        al "Well, a little. "
        al "I'm sorry, I know it's silly but-"
        "The bull raised a hand to stop her."
        gh "I know what I am. You do not need to excuse yourself."
        gh "In normal circumstances, you would have good reason to be afraid."
        show alexia 2 necklace neutral at midleft with dissolve
        al "This castle is about as far from ‘normal’ as you can get."
        gh "I know."
        show alexia 2 necklace happy at midleft with dissolve
        al "It’s also not fair to you, Greyhide. You are… a kind man."
        gh "Heh."
        
    "No.":
        $ released_fix_rollback()
        "Alexia shook her head."
        show alexia 2 necklace neutral at midleft with dissolve
        al "It’s not that, Greyhide. It’s just… awkward."
        gh "What is?"
        al "Finding something to talk about with you. I’m no blacksmith, and I know next to nothing about your people."
        gh "Why do we need to talk about something?"
        show alexia 2 necklace concerned at midleft with dissolve
        al "Because… that’s what friends do?"
        gh "Are we only friends because we talk?"
        show alexia 2 necklace happy at midleft with dissolve
        al "Hehe, of course not!"
        gh "Your kindness is enough."
        
"The minotaur stood up, circling the long table.  He took two flasks of something from his belt and held one out to Alexia."

gh "Here. For your nerves."

show alexia 2 necklace shocked at midleft with dissolve

al "What is this?"

gh "Firegrout draft, one of the few things I enjoyed from my old home."
gh "It is potent, so take only a few sips."

show alexia 2 necklace concerned at midleft with dissolve

al "Aah, o-okay. "

show alexia 2 necklace neutral at midleft with dissolve

al "Thank you."

"Alexia accepted the drink after only a moment's hesitation. They clinked their flasks together and drank as one. Greyhide downed it in one gulp, while Alexia took a paltry sip."

al "..."

show alexia 2 necklace happy at midleft with dissolve

al "Wow, that's not bad!"

gh "Smooth, is it not?"

al "It’s so spicy. It almost tastes like cinnamon."

gh "It comes from a rare herb native to my homeland. It is hard to get the ingredients from so far away."
gh "This batch seems a bit stronger than usual."

"Alexia felt a pleasing warmth spread through her tummy as her cheeks flushed. It really was strong! She took another measured sip."

al "Thank you for sharing it with me."

gh "I am glad you enjoy it."
gh "Would you like to hear about the Dragon's Tail?"

al "Your homeland?"

gh "Yes."

al "I’d love to!"

"Alexia giggled - perhaps a little too eagerly - as she took another dainty sip. The firegrout settled in her stomach with a welcoming heat."

scene black with fade
pause 1
scene bg27 with fade
show alexia 2 necklace aroused at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve

"...What time was it?"
"Alexia didn’t know. She was having trouble concentrating. The conversation had been so enthralling that she hadn’t even noticed the minutes ticking by."
"She couldn’t remember when she’d gotten so close to the hulking Minotaur, who sat spread eagle next to her. His legs were so wide she practically sat between his lap in her own chair. "
"Greyhide tipped another flask back and downed its contents. It was his third one of the night. They were both struggling to hold a coherent conversation."

gh "Your... husband gave me Rosarian wine…"

al "Hehe, when?"

gh "When…"
gh "When? When last we spoke."

"The Minotaurs cheeks were flushed, his mouth opened and closed in slow, deliberate fashion. He talked in a plodding tone, even moreso than usual. Alexia found it funny."

gh "I… wished to find and share the drink... my people make. With him."

"Alexia giggled with a girlish intonation, clutching the half-empty flask to her chest like a treasured heirloom."

al "Noooo! Don’t do that! It’s mine!"

gh "Too... late now."

al "That’s right. It’s {i}our{/i} little secret."

gh "Heh…"

"Alexia was blushing. Gods, she was {i}burning{/i} up. Frilly pink clouds had drifted over the higher functions of her mind." 
"Everything about this evening was perfect, as far as she was concerned. Greyhide evidently felt the same way, judging from his blissful smile and slumped demeanor."

al "I’m glad we met you."

gh "Glad… I met you too."

"She looked at him for a long moment, impressed at his powerful physique and strong features. How had she never noticed them before?"
"She poked his massive knee, and he lifted his head to look at her."

menu:
    "What do you like most about me, Greyhide?":
        $ released_fix_rollback()
        "Greyhide put a finger to his snout, tapping it gently against his nostril as he contemplated. To Alexia he looked like a cow trying to be philosophical."
        gh "{i}Hrmm…{/i}"
        al "{i}Pft-{/i}"
        al "Hahaha!"
        gh "What is so funny?"
        al "Your face."
        gh "What is… wrong with my face?"
        al "Nothing! You just make funny faces."
        gh "My face… is… my face…"
        al "Well, {i}obviously{/i}!"
        "A long silence passed between them. Then, the dam broke, and they erupted into gales of drunken laughter."
        
    "You know what I like most about you, Greyhide?":
       $ released_fix_rollback() 
       gh "What do you... like most about me?"
       al "You’re big."
       gh "And you are... small."
       al "{i}Hey!{/i}"
       gh "Heh… am I wrong?"
       al "N-no, but-"
       gh "You are... soft. Delicate."
       gh "I would be... afraid you would break... if I touched you."
       "Alexia puffed out her cheeks in mock-annoyance."
       al "I’m not {i}that{/i} fragile!"
       "Greyhide leaned towards her. Her face went beet red. With a gentle push he nearly tipped her over in her chair."
       al "{i}Hey!{/i}"
       gh "Heh… see?"
       
"The Minotaur quieted down, his lips curling into a gentle smile."

gh "You are… nice to be around, Alexia."

al "You’re nice to be around too, Greyhide."
al "Hehe, I never thought I’d say that about a Minotaur."

gh "Nor I a… human."

"A strange, simmering warmth was working its way through her body, settling snugly in her groin. She took another idle sip from the flask to settle the butterflies in her stomach."
"Her eyes began to wander. Thoughts she’d never considered before danced dangerously in her head. She couldn’t quite think straight."

gh "What are... you looking at?"

al "You."
al "What are {i}you{/i} looking at?"

gh "Nothing…"

"Despite his best efforts to hide it, Greyhide was sporting something beneath his paltry loincloth."
"An obscene question popped into Alexia’s head: how big was he down there?"
"No matter how much she tried to beat down the thought, there it was. For whatever strange reason, the pink clouds in her head wouldn’t let her look away."

menu:
    "Ask the question.":
        $ released_fix_rollback() 
        "She couldn’t help herself, her inhibitions had been cast to the wind. There was a fire in her belly and a burning question in her mind."
        al "Greyhide…"
        gh "Yes?"
        al "Can I see it?"
        gh "See what?"
        al "I think you know."
        "Greyhide’s eyes widened. He tried to sit up straighter in his seat, but his movements were sluggish. Impeded."
        gh "W-what?"
        "Alexia giggled, her hand reaching over and patting his leg, just on the inside of the thigh."
        al "I want to see your-"
        "The bull jerked back, his legs closing as he let out a loud, masculine snort."
        gh " I..."
        al "Come on… I’ve been wondering about this for a {i}while{/i}."
        al "Does it look like a human’s? Is it bigger?"
        gh "I wouldn’t… know."
        "Greyhide swallowed heavily. He was panting. His eyes lidded as he spread his legs again. Despite his feeble protests, he was just as turned on as Alexia."
        "The world moved in slow motion. His large hand reached down and adjusted the loincloth, revealing the turgid member hiding beneath."
        "The moment she saw it, Alexia’s blush deepened."
        al "Oh!"
        al "...That's some big balls."
        "Her innocent statement of fact broke the tension, and the two began to laugh."
        gh "What are… we doing?"
        al "Haha, I don’t know!"
        "Still, the horny fog in her head refused to recede. A burning need filled her nethers as she looked at him, this masculine creature of virile potential."
        "She wondered what it felt like. How warm it was. Her head was spinning."
        "She..."
        menu:
            "Touch it.":
                $ released_fix_rollback() 
                "Before she even knew what she was doing, her hand reached out and touched it. Greyhide stiffened, in more ways than one."
                gh "You…"
                gh "You are so soft…"
                gh "So… beautiful…"
                "A queer spell had taken hold of them both. Alexia, in a daze, gently stroked his thick cock."
                "She looked up at the Minotaur, a moment of wordless understanding passing between them."
                scene cg76 with fade
                pause 3
                show greyhide neutral behind cg76 
                show alexia 2 necklace aroused behind cg76
                "Without hesitation, Greyhide unhitched his breast plate and lifted the entire affair off of his body. Then he plopped down on the table."
                "Alexia got her first proper look at his very sizable, fuzzy sack. It was, as she first observed, {i}big{/i}."
                al "Wow..."
                "Without thinking, she stepped forward and took hold of him again.  Her fingers ran down the fleshy tube of his sheath and then cupped the furred balls underneath."
                "His fur tickled her fingers. It felt funny to her."
                al "Hehe!"
                "The beast reached out, his trembling fingers brushing across her bangs. He seemed to be struggling to hold himself back."
                gh "Red… like fire…"
                al "You like my hair?"
                gh "Yes."
                "She giggled. Her fingers reached out and tickled the furry underside of his sack."
                al "I like your hair, too."
                "She was dizzy, horny beyond compare. The Minotaur’s lidded eyes bespoke his own arousal. Alexia’s voice lowered to a throaty whisper."
                al "You smell… {i}nice{/i}."
                gh "You… too."
                gh "Your touch is… very nice."
                al "I don’t- I don’t think you’d fit."
                scene cg77 with fade
                pause 3
                show greyhide neutral behind cg77 
                show alexia 2 necklace aroused behind cg77
                "Greyhide reached over and lifted the woman onto his lap. Alexia made no effort to stop him."
                gh "That is fine. I am happy as long as you are touching me."
                "Alexia started playing with his erection, a dazed smile on her face. The two were in an almost trancelike communion."
                "The bull started pulling her dress away; he tugged off her top, exposing her breasts."
                gh "So small, so... delicate."
                "He dragged one of his thick digits across her breast, the long nail pressing gently against her nipple. Hard, coarse skin met Alexia's much softer skin, sending a shiver up her spine."
                gh "...No milk?"
                al "No. I haven’t had any kids with Rowan yet."
                "At the sound of her husbands name, Alexia felt a twinge of something strange in the back of her mind. She felt like she should be worried about something."
                gh "Only… time humans do?"
                al "Yeah."
                gh "Heh… Minotaur women… all the time."
                scene cg78 with fade
                pause 3
                show greyhide neutral behind cg78 
                show alexia necklace naked aroused behind cg78
                "Frustrated at his inability to disrobe her, the Minotaur started pulling the dress open by force. He all but yanked her shirt open, tearing off one of the buttons in the process."
                gh "Oh, I… sorry…"
                "Don't worry. I can fix it later.  Right now, I want…"
                "Alexia wrapped both arms around his shaft. She started bobbing up and down, delighting in the lurid feel of her womanhood sliding over the ridge where fur gave way to flesh."
                al "{i}You.{/i}"
                "Before she knew it, she found herself licking the head of his cock.  His pre-cum tasted so good, like the pleasant aftertaste of the firegrout."
                "Greyhide moved slowly beneath her, thrusting upwards in slow, powerful movements. She rode him, lifting and lowering like a horse in full gallop."
                "By the end of it they were both panting, gasping for air as they met each other’s smouldering gaze. Greyhide’s deep voice drifted off into nonsense."
                gh "Oh sweet soft lady… you, you are so good to me.  I think, I think…"
                "He growled in his deep, rumbling voice, and then he came."
                show cg78 with sshake
                show cg78 with sshake
                scene cg79 with flash
                pause 2
                show greyhide neutral behind cg79 
                show alexia necklace naked aroused behind cg79
                "A huge geyser of hot, misty fluid blasted Alexia in the face. She was so caught up in the blissful sensation that she nearly wasn’t ready for the second wave, nor the third."
                "The storm caught her by complete surprise but, after a few moments of complete confusion, Alexia just started giggling incessantly."
                "She was soaked, both in his and in her juices. She took an idle swipe of his cum from her cheek and brought it to her mouth. It tasted salty."
                gh "Oh Alexia… Alexia…"
                "Still giggling, Alexia tried to wipe her face clean with her hands, then accepted the tablecloth from Greyhide."
                al "Oh, you really know how to make a lady feel like a woman."
                gh "You… what did we…?"
                al "Gosh, I’m practically soaked now! You came a lot."
                "Greyhide’s eyes snapped open, his jaw dropping as he seemed to regain some semblance of his senses."
                "He sat up in a rush, his hands trembling as he gently took Alexia by the hips and set her down onto the ground."
                gh "I… we…"
                gh "What’s come over me?"
                "How strange. That thought had crossed Alexia’s mind as well."
                "Come to think of it… what were they doing?"
                "Alexia blinked, her eyes going wide as the real implications of their actions pierced through the pleasant fog that had settled over her mind."
                "She looked down at herself, naked and covered in the Minotaur’s juices. A wave of confusion and fear struck."
                "What… what were they {i}doing{/i}?!"
                scene bg27 with fade
                show alexia 2 necklace concerned at midleft with dissolve
                show greyhide neutral at cliohnaright
                "The two recent lovers both rushed to clean themselves up and re-dress. Neither seemed ready to look the other in the eyes."
                "Greyhide’s breathing was ragged, his movements sloppy and uncoordinated. Alexia was little better: half stumbling as she struggled to pull up her knickers."
                al "I… I have to go."
                gh "M-me… too."
                scene black with fade
                "After a perfunctory goodbye, the two drunken friends all but fled from the scene of their recent debauchery."
                "Alexia would lie awake that night, restless and drunk, wondering to herself what had just happened."
                "The worst part about it was, for all her worries, it had been a really lovely experience..."
                $ alexiaUnfaithful = True
                $ change_corruption_actor('alexia', 3)
                $ alexia_greyhide_sex = True
                return
                
            "Tease him for flashing her.":
                $ released_fix_rollback()
                "She started to laugh."
                al "Oh {i}goddess{/i}, you’re naked!"
                "A look of muddled confusion crossed Greyhide’s face, followed by growing shock."
                gh "Oh.."
                gh "...{i}Oh{/i}!"
                "Alexia couldn’t stop laughing. Things had taken a ludicrous turn. How had they even gotten to this point?"
                "The beast, profoundly embarrassed, moved to cover himself. Alexia couldn’t bring herself to look away."
                al "Hehe! I see the carpet matches the drapes."
                gh "I… what?"
                gh "I am… what am I doing?"
                al "Having a bit too much to drink, I think."
                "Greyhide stood up in a rush, his hands fumbling as he tried to cover his shame. His cheeks were burning, his large eyes darting this way and that in an unfocused blur."
                gh "I-I-"
                gh "I... must go. Excuse me. Please…"
                scene black with fade
                "He nearly overturned the table in his haste to stand up. Alexia tried to reach out to stop him, but the hulking bull was deceptively fast."
                "Alexia watched with a sort of dazed confusion as the Minotaur all but fled from her presence."
                "...Why did he leave? Was it something she’d said? They were having such a fun time together!"
                "Dejected, she waited as long as she could for Rowan to return. He ended up finding her several hours later, face down on the table. He carried her back to bed."
                return
                
    "Get ahold of yourself, woman!":
        $ released_fix_rollback()
        "Alexia shook her head back and forth, shoving the strange, unusual thought from her mind. Goddess fend, she’d been fantasizing about a {i}Minotaur{/i}, of all things!"
        "She did her best to steer the conversation towards more mundane matters, but her body simply refused to ignore the presence of this virile beast nearby. She squirmed in discomfort at this artificial feeling."
        "It didn’t help that Greyhide was staring at her. His eyes were lidded low, is jaw dropping ever so slightly, exposing his thick tongue."
        al "Uh… Greyhide?"
        gh "What… is it?"
        al "You’re uh- staring at me."
        gh "I am?"
        "A look of muddled confusion crossed Greyhide’s face, followed by a look of shock. His face contorted in horror."
        gh "...{i}No{/i}!"
        "The Minotaur stood up in a rush. His cheeks were burning, his large eyes darting this way and that in an unfocused blur."
        gh "I-I-"
        gh " I... must go. Excuse me. Please…"
        "He nearly overturned the table in his haste to stand up. Alexia tried to reach out to stop him, to ask what was the matter, but the hulking bull was deceptively fast."
        al "Wait, what-"
        scene black with fade
        "But he was already gone. Greyhide all but fled from her presence, driven from the room by her mere existence. Alexia, still drunk, didn’t quite understand why."
        "Though later, if she was being honest with herself, she had a sneaking hunch as to the reason."
        "Dejected at the dreary end to the night’s fun, she waited as long as she could for Rowan to return. He ended up finding her several hours later, face down on the table. He carried her back to bed."
        return
        